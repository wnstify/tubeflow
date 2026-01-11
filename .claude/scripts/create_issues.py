#!/usr/bin/env python3
"""
Create GitHub Issues from roadmap.json for community voting.
Also generates ROADMAP.md with links to issues.

Usage:
  python .claude/scripts/create_issues.py
  python .claude/scripts/create_issues.py --dry-run

Prerequisites:
  - gh CLI installed and authenticated
  - Run from repository root
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional

import yaml


# === CONFIGURATION LOADING ===

def find_config_path() -> Path:
    """Find config.yaml by searching up from script location."""
    script_dir = Path(__file__).parent

    # Try .claude parent directory first
    claude_config = script_dir.parent / "config.yaml"
    if claude_config.exists():
        return claude_config

    # Try repo root
    repo_root = script_dir.parent.parent
    root_config = repo_root / "config.yaml"
    if root_config.exists():
        return root_config

    # Fall back to example config
    example_config = repo_root / "config.example.yaml"
    if example_config.exists():
        print(f"Warning: Using example config. Copy config.example.yaml to config.yaml and customize.")
        return example_config

    raise FileNotFoundError(
        "No config.yaml found. Please create one from config.example.yaml"
    )


def load_config() -> dict:
    """Load configuration from config.yaml."""
    config_path = find_config_path()
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# Load configuration
try:
    CONFIG = load_config()
except FileNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(1)


# === DERIVED CONFIGURATION ===

ROADMAP_PATH = "roadmap.json"
ROADMAP_MD_PATH = "ROADMAP.md"


def get_repo_identifier() -> str:
    """Get GitHub repo identifier from config or environment."""
    if os.environ.get("GITHUB_REPO"):
        return os.environ["GITHUB_REPO"]

    # Extract from voting_repo URL in config
    voting_repo = CONFIG.get("links", {}).get("voting_repo", "")
    if voting_repo:
        # Extract owner/repo from URL
        match = re.search(r'github\.com/([^/]+/[^/]+)', voting_repo)
        if match:
            return match.group(1).rstrip('/')

    print("Error: No GitHub repo configured")
    print("Set GITHUB_REPO environment variable or configure links.voting_repo in config.yaml")
    sys.exit(1)


def get_channel_info() -> dict:
    """Get channel information from config."""
    return CONFIG.get("channel", {
        "name": "Your Channel",
        "handle": "@yourchannel"
    })


def run_gh(args: list, repo: str, check: bool = True) -> subprocess.CompletedProcess:
    """Run gh CLI command."""
    cmd = ["gh"] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"  Error: {result.stderr.strip()}")
    return result


def label_exists(label: str, repo: str) -> bool:
    """Check if label already exists."""
    result = run_gh(["label", "list", "--repo", repo, "--json", "name"], repo, check=False)
    if result.returncode == 0:
        labels = json.loads(result.stdout)
        return any(l["name"] == label for l in labels)
    return False


def create_label(name: str, color: str, repo: str, description: str = "", dry_run: bool = False) -> bool:
    """Create a GitHub label."""
    if label_exists(name, repo):
        print(f"  Label '{name}' already exists, skipping")
        return True

    if dry_run:
        print(f"  [DRY RUN] Would create label: {name} (#{color})")
        return True

    args = ["label", "create", name, "--repo", repo, "--color", color]
    if description:
        args.extend(["--description", description])

    result = run_gh(args, repo, check=False)
    if result.returncode == 0:
        print(f"  Created label: {name}")
        return True
    else:
        print(f"  Failed to create label '{name}': {result.stderr.strip()}")
        return False


def get_issue_number(title: str, repo: str) -> Optional[int]:
    """Get issue number by exact title match."""
    result = run_gh([
        "issue", "list",
        "--repo", repo,
        "--search", f'"{title}" in:title',
        "--json", "title,number",
        "--state", "all",
        "--limit", "100"
    ], repo, check=False)

    if result.returncode == 0:
        issues = json.loads(result.stdout)
        for issue in issues:
            if issue["title"] == title:
                return issue["number"]
    return None


def create_issue(video: dict, categories: dict, repo: str, dry_run: bool = False) -> Optional[int]:
    """Create a GitHub issue for a video idea. Returns issue number."""
    title = video["title"]

    # Check if exists
    existing = get_issue_number(title, repo)
    if existing:
        print(f"  Issue #{existing} '{title[:40]}...' exists, skipping")
        return existing

    # Build labels
    labels = []

    # Category label
    category = video.get("category")
    if category and category in categories:
        labels.append(categories[category]["label"])

    # Complexity label
    complexity = video.get("complexity")
    if complexity:
        labels.append(complexity)

    # Series label
    if video.get("series"):
        labels.append("series")

    # Build body
    body_parts = []

    if video.get("notes"):
        body_parts.append(f"**Notes:** {video['notes']}")

    if video.get("seriesInfo"):
        body_parts.append(f"**Series:** {video['seriesInfo']}")

    body_parts.append("")
    body_parts.append("---")
    body_parts.append("")
    body_parts.append("Vote with :+1: to help prioritize this video!")
    body_parts.append("")
    body_parts.append("_This issue was auto-generated from the video roadmap._")

    body = "\n".join(body_parts)

    if dry_run:
        print(f"  [DRY RUN] Would create issue: {title}")
        return None

    args = [
        "issue", "create",
        "--repo", repo,
        "--title", title,
        "--body", body
    ]

    for label in labels:
        args.extend(["--label", label])

    result = run_gh(args, repo, check=False)
    if result.returncode == 0:
        # Extract issue number from URL
        issue_url = result.stdout.strip()
        issue_num = int(issue_url.split("/")[-1])
        print(f"  Created #{issue_num}: {title[:50]}...")
        return issue_num
    else:
        print(f"  Failed: {title[:40]}... - {result.stderr.strip()}")
        return None


def generate_roadmap_md(data: dict, issue_numbers: dict):
    """Generate ROADMAP.md with links to issues."""
    channel = get_channel_info()
    categories = {c["id"]: c for c in data["categories"]}
    videos = data["videos"]

    # Group videos by category
    by_category = {}
    for video in videos:
        cat = video.get("category", "misc")
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(video)

    # Count stats
    total = len(videos)
    series_count = sum(1 for v in videos if v.get("series"))
    complexity_counts = {}
    for v in videos:
        c = v.get("complexity", "unknown")
        complexity_counts[c] = complexity_counts.get(c, 0) + 1

    lines = []
    lines.append("# Video Roadmap")
    lines.append("")
    lines.append(f"Upcoming video ideas for the [{channel['handle']}](https://youtube.com/{channel['handle']}) channel.")
    lines.append("")
    lines.append("## How to Vote")
    lines.append("")
    lines.append("1. Click on any video topic below")
    lines.append("2. Give it a :+1: reaction")
    lines.append("3. Most voted topics get prioritized!")
    lines.append("")
    lines.append("Want to suggest a new topic? [Open a suggestion](../../issues/new?template=video-suggestion.yml)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(f"**{total} video ideas** across {len(categories)} categories")
    lines.append("")
    lines.append("| Difficulty | Count |")
    lines.append("|------------|-------|")
    lines.append(f"| Beginner | {complexity_counts.get('beginner', 0)} |")
    lines.append(f"| Intermediate | {complexity_counts.get('intermediate', 0)} |")
    lines.append(f"| Advanced | {complexity_counts.get('advanced', 0)} |")
    lines.append("")
    lines.append(f"*{series_count} multi-part series included*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Table of contents
    lines.append("## Categories")
    lines.append("")
    for cat_id in by_category.keys():
        if cat_id in categories:
            cat_name = categories[cat_id]["name"]
            anchor = cat_name.lower().replace(" ", "-").replace("&", "")
            lines.append(f"- [{cat_name}](#{anchor}) ({len(by_category[cat_id])})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Each category
    for cat_id, cat_videos in by_category.items():
        if cat_id not in categories:
            continue

        cat_info = categories[cat_id]
        lines.append(f"## {cat_info['name']}")
        lines.append("")
        lines.append("| Video | Difficulty | Vote |")
        lines.append("|-------|------------|------|")

        for video in cat_videos:
            title = video["title"]
            complexity = video.get("complexity", "").capitalize()
            series_badge = " *(series)*" if video.get("series") else ""

            # Link to issue
            issue_num = issue_numbers.get(video["id"])
            if issue_num:
                vote_link = f"[Vote](../../issues/{issue_num})"
                title_display = f"[{title}](../../issues/{issue_num}){series_badge}"
            else:
                vote_link = "-"
                title_display = f"{title}{series_badge}"

            lines.append(f"| {title_display} | {complexity} | {vote_link} |")

        lines.append("")

    # Footer
    lines.append("---")
    lines.append("")
    lines.append("*Last updated: " + data.get("lastUpdated", "2026-01-11") + "*")
    lines.append("")
    lines.append("*[Video Library](VIDEOS.md) | [Suggest Topic](../../issues/new?template=video-suggestion.yml) | [Project Board](../../projects)*")
    lines.append("")

    content = "\n".join(lines)

    with open(ROADMAP_MD_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\nGenerated: {ROADMAP_MD_PATH}")


def main():
    parser = argparse.ArgumentParser(
        description="Create GitHub Issues from roadmap.json for community voting"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without creating issues"
    )
    parser.add_argument(
        "--roadmap",
        type=str,
        default=ROADMAP_PATH,
        help=f"Path to roadmap.json (default: {ROADMAP_PATH})"
    )
    args = parser.parse_args()

    roadmap_path = args.roadmap
    dry_run = args.dry_run

    # Check if we're in repo root
    if not os.path.exists(roadmap_path):
        print(f"Error: {roadmap_path} not found. Run from repo root.")
        sys.exit(1)

    # Get repo identifier
    repo = get_repo_identifier()
    print(f"Target repository: {repo}")

    # Load roadmap
    print(f"Reading from: {roadmap_path}")
    with open(roadmap_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = {c["id"]: c for c in data["categories"]}
    complexity_labels = data["complexityLabels"]
    videos = data["videos"]

    print(f"Found {len(videos)} video ideas\n")

    if dry_run:
        print("[DRY RUN MODE - No changes will be made]\n")

    # Create labels
    print("Creating labels...")

    # Category labels
    for cat in data["categories"]:
        create_label(cat["label"], cat["color"], repo, cat["name"], dry_run)

    # Complexity labels
    for comp in complexity_labels:
        create_label(comp["id"], comp["color"], repo, f"{comp['name']} difficulty", dry_run)

    # Series label
    create_label("series", "ffc107", repo, "Multi-part series", dry_run)

    # Video-suggestion label
    create_label("video-suggestion", "a2eeef", repo, "Community video suggestion", dry_run)

    print()

    # Create issues
    print("Creating issues...")
    issue_numbers = {}
    created = 0
    skipped = 0
    failed = 0

    for i, video in enumerate(videos, 1):
        print(f"[{i}/{len(videos)}]", end="")

        issue_num = create_issue(video, categories, repo, dry_run)
        if issue_num:
            issue_numbers[video["id"]] = issue_num
            if get_issue_number(video["title"], repo) == issue_num:
                skipped += 1
            else:
                created += 1
        else:
            if not dry_run:
                failed += 1

        # Rate limiting
        if not dry_run:
            time.sleep(0.3)

    print(f"\nIssues:")
    print(f"  Created: {created}")
    print(f"  Existing: {skipped}")
    print(f"  Failed: {failed}")

    # Generate ROADMAP.md
    print("\nGenerating ROADMAP.md...")
    generate_roadmap_md(data, issue_numbers)

    if dry_run:
        print("\nThis was a DRY RUN. Run without --dry-run to create issues.")


if __name__ == "__main__":
    main()

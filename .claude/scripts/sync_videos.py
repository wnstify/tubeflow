#!/usr/bin/env python3
"""
Sync videos from youtube-index.json to public GitHub repository.

Creates README files, updates VIDEOS.md, closes matching roadmap issues.

Usage:
  python .claude/scripts/sync_videos.py              # Sync new videos
  python .claude/scripts/sync_videos.py --dry-run    # Preview without changes

Run from public video repository root.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Set, Tuple

import yaml


# === CONFIGURATION LOADING ===

def find_config_path() -> Path:
    """Find config.yaml by searching up from script location."""
    # Check for config in repo root (when running from .claude/scripts/)
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

def get_youtube_index_path() -> str:
    """Get path to youtube-index.json from config or environment."""
    # Environment variable takes precedence
    if os.environ.get("YOUTUBE_INDEX_PATH"):
        return os.path.expanduser(os.environ["YOUTUBE_INDEX_PATH"])

    # Try to construct from config structure
    structure = CONFIG.get("structure", {})
    youtube_root = structure.get("youtube_root", "03-YouTube")

    # Check common locations
    potential_paths = [
        Path.home() / "obsidian" / youtube_root / "youtube-index.json",
        Path.home() / "vault" / youtube_root / "youtube-index.json",
        Path.cwd().parent / youtube_root / "youtube-index.json",
    ]

    for path in potential_paths:
        if path.exists():
            return str(path)

    # Fallback to environment variable requirement
    print("Error: Cannot find youtube-index.json")
    print("Set YOUTUBE_INDEX_PATH environment variable or place file in expected location")
    sys.exit(1)


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


VIDEOS_DIR = "videos"
VIDEOS_MD_PATH = "VIDEOS.md"


def fetch_youtube_description(video_id: str) -> Optional[str]:
    """Fetch full description from YouTube using yt-dlp."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--get-description", f"https://www.youtube.com/watch?v={video_id}"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


# === CATEGORY KEYWORDS ===
# These can be customized or loaded from config
# Order matters: first match wins

DEFAULT_CATEGORY_KEYWORDS = {
    "Self-Hosting": ["self-host", "nextcloud", "immich", "home server", "homelab"],
    "Security": ["authentik", "security", "2fa", "password", "firewall", "ssh"],
    "VPN": ["vpn", "wireguard", "tailscale", "zero trust", "tunnel"],
    "Docker": ["docker", "container", "compose", "kubernetes", "k8s"],
    "Backup": ["backup", "borg", "restic", "migration", "restore"],
    "Automation": ["automation", "ansible", "n8n", "automate", "workflow"],
    "Monitoring": ["monitoring", "uptime", "analytics", "observability", "logs"],
    "AI": ["ai", "llm", "openwebui", "ollama", "machine learning"],
    "Tools": []  # Default fallback
}

DEFAULT_CATEGORY_SECTIONS = {
    "Self-Hosting": "## Self-Hosting",
    "Security": "## Security & Authentication",
    "VPN": "## VPN & Zero Trust",
    "Docker": "## Docker & Containers",
    "Backup": "## Backup Solutions",
    "Automation": "## Automation",
    "Monitoring": "## Monitoring & Analytics",
    "AI": "## AI & Machine Learning",
    "Tools": "## Tools",
}


def get_category_keywords() -> Dict[str, List[str]]:
    """Get category keywords from config or use defaults."""
    return CONFIG.get("categories", {}).get("keywords", DEFAULT_CATEGORY_KEYWORDS)


def get_category_sections() -> Dict[str, str]:
    """Get category section headers from config or use defaults."""
    return CONFIG.get("categories", {}).get("sections", DEFAULT_CATEGORY_SECTIONS)


def slugify(title: str) -> str:
    """Convert title to URL-friendly slug."""
    slug = re.sub(r'[^\w\s-]', '', title)
    slug = slug.lower()
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    if len(slug) > 60:
        slug = slug[:60].rsplit('-', 1)[0]
    return slug


def clean_title(title: str) -> str:
    """Remove emojis and clean title for display."""
    clean = re.sub(r'[^\w\s\-\|\:\&\'\"\(\)\[\]\,\.\!\?\/]', '', title)
    clean = re.sub(r'\s+', ' ', clean)
    return clean.strip()


def format_date(date_str: str) -> str:
    """Format date as 'Month Day, Year'."""
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%B %d, %Y").replace(" 0", " ")


def auto_categorize(title: str, summary: str) -> Tuple[str, List[str]]:
    """
    Determine categories based on keywords in title and summary.
    Returns (primary_category, all_categories).
    Primary is used in All Videos table, all are used for section insertion.
    """
    text = (title + " " + summary).lower()
    matched = []

    category_keywords = get_category_keywords()

    for category, keywords in category_keywords.items():
        if not keywords:
            continue
        if any(kw in text for kw in keywords):
            matched.append(category)

    if not matched:
        return ("Tools", ["Tools"])

    return (matched[0], matched)  # First match is primary


def get_existing_video_ids() -> Set[str]:
    """Get set of video IDs already synced to repository."""
    existing = set()
    videos_path = Path(VIDEOS_DIR)

    if not videos_path.exists():
        return existing

    for readme_path in videos_path.glob("*/*/README.md"):
        content = readme_path.read_text(encoding="utf-8")
        match = re.search(r'youtube\.com/watch\?v=([a-zA-Z0-9_-]+)', content)
        if match:
            existing.add(match.group(1))

    return existing


def create_video_readme(video: Dict) -> str:
    """Generate README.md content for a video."""
    title = clean_title(video["title"])
    video_id = video["video_id"]
    date = format_date(video["date"])
    url = video["url"]

    # Fetch full description from YouTube, fallback to summary
    description = fetch_youtube_description(video_id)
    if not description:
        description = video.get("summary", "")
        print(f"  Warning: Could not fetch YouTube description, using summary")

    return f"""# {title}

[![Watch on YouTube](https://img.youtube.com/vi/{video_id}/maxresdefault.jpg)]({url})

**Published:** {date}

[Watch on YouTube]({url})

---

## Description

{description}
"""


def insert_into_all_videos_table(content: str, video: Dict, category: str) -> str:
    """Insert new row into 'All Videos' table at top (newest first)."""
    title = clean_title(video["title"])
    year = video["date"][:4]
    slug = slugify(video["title"])

    new_row = f"| [{title}](videos/{year}/{slug}) | {year} | {category} |"

    lines = content.split('\n')
    result = []
    inserted = False

    for i, line in enumerate(lines):
        result.append(line)

        # Insert after the table header separator
        if line.startswith("|-------") and not inserted:
            # Check if next lines are table content (All Videos table)
            if i + 1 < len(lines) and lines[i + 1].startswith("| ["):
                result.append(new_row)
                inserted = True

    return '\n'.join(result)


def insert_into_category_section(content: str, video: Dict, category: str) -> str:
    """Insert new row into appropriate category section at top."""
    title = clean_title(video["title"])
    year = video["date"][:4]
    slug = slugify(video["title"])

    category_sections = get_category_sections()
    section_header = category_sections.get(category, category_sections.get("Tools", "## Tools"))
    new_row = f"| [{title}](videos/{year}/{slug}) | {year} |"

    lines = content.split('\n')
    result = []
    found_section = False
    inserted = False

    for i, line in enumerate(lines):
        result.append(line)

        # Find target section
        if line.strip() == section_header:
            found_section = True
            continue

        # Insert after table separator in this section
        if found_section and not inserted and line.startswith("|-------"):
            result.append(new_row)
            inserted = True
            found_section = False

        # Reset if we hit another section
        if found_section and line.startswith("## "):
            found_section = False

    return '\n'.join(result)


def update_video_count(content: str, new_count: int) -> str:
    """Update the video count in VIDEOS.md header."""
    pattern = r'\*\*\d+ videos\*\*'
    replacement = f'**{new_count} videos**'
    return re.sub(pattern, replacement, content)


def update_year_range(content: str, max_year: str, min_year: str = None) -> str:
    """Update year range in header if needed."""
    if min_year:
        pattern = r'\*\*\d{4} - \d{4}\*\*'
        replacement = f'**{min_year} - {max_year}**'
    else:
        pattern = r'\*\*\d{4} - \d{4}\*\*'
        replacement = f'**2022 - {max_year}**'
    return re.sub(pattern, replacement, content)


def update_readme(latest_video: Dict, total_count: int) -> None:
    """Update README.md with latest video and video count."""
    readme_path = Path("README.md")
    if not readme_path.exists():
        return

    content = readme_path.read_text(encoding="utf-8")

    # Update video count in "Browse X Published Videos"
    content = re.sub(
        r'Browse \d+ Published Videos',
        f'Browse {total_count} Published Videos',
        content
    )

    # Create latest video section
    title = clean_title(latest_video["title"])
    year = latest_video["date"][:4]
    slug = slugify(latest_video["title"])
    video_id = latest_video["video_id"]
    url = latest_video["url"]

    latest_section = f"""## Latest Video

[![{title}](https://img.youtube.com/vi/{video_id}/mqdefault.jpg)]({url})

**[{title}](videos/{year}/{slug})** - [Watch on YouTube]({url})

---

## Video Library"""

    # Replace or insert latest video section
    if "## Latest Video" in content:
        # Replace existing latest video section up to Video Library
        content = re.sub(
            r'## Latest Video.*?---\s*\n\n## Video Library',
            latest_section,
            content,
            flags=re.DOTALL
        )
    else:
        # Insert before Video Library section
        content = content.replace(
            "## Video Library",
            latest_section
        )

    readme_path.write_text(content, encoding="utf-8")


def close_roadmap_issue(title: str, video_url: str, repo: str) -> Optional[int]:
    """Close matching roadmap issue if exists."""
    clean = clean_title(title)
    search_terms = clean[:40]

    result = subprocess.run(
        ["gh", "issue", "list", "--repo", repo,
         "--search", f'"{search_terms}" in:title',
         "--json", "number,title", "--state", "open", "--limit", "10"],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        return None

    try:
        issues = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None

    if not issues:
        return None

    # Find best match
    title_words = set(re.findall(r'\w+', clean.lower()))

    for issue in issues:
        issue_title = issue["title"]
        issue_words = set(re.findall(r'\w+', issue_title.lower()))

        # Match if 50%+ of issue words are in video title
        if issue_words and len(title_words & issue_words) >= len(issue_words) * 0.5:
            issue_num = issue["number"]

            comment = f"Published! Watch here: {video_url}"
            subprocess.run(
                ["gh", "issue", "close", str(issue_num),
                 "--repo", repo, "--comment", comment],
                capture_output=True
            )
            return issue_num

    return None


def sync_videos(dry_run: bool = False) -> Dict:
    """Main sync function."""

    # Get paths from config
    youtube_index_path = get_youtube_index_path()
    repo = get_repo_identifier()

    # Verify source exists
    if not os.path.exists(youtube_index_path):
        return {"error": f"youtube-index.json not found at {youtube_index_path}"}

    # Verify target exists
    if not os.path.exists(VIDEOS_MD_PATH):
        return {"error": f"VIDEOS.md not found. Run from video repository root."}

    # Load youtube index
    with open(youtube_index_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    all_videos = data["videos"]
    existing_ids = get_existing_video_ids()

    # Find new videos
    new_videos = [v for v in all_videos if v["video_id"] not in existing_ids]

    if not new_videos:
        return {"synced": 0, "message": "No new videos to sync"}

    # Read current VIDEOS.md
    with open(VIDEOS_MD_PATH, "r", encoding="utf-8") as f:
        videos_md = f.read()

    synced = []
    issues_closed = []

    for video in new_videos:
        year = video["date"][:4]
        slug = slugify(video["title"])
        primary_category, all_categories = auto_categorize(
            video["title"], video.get("summary", "")
        )

        print(f"\nSyncing: {clean_title(video['title'])[:60]}...")
        print(f"  Primary: {primary_category}")
        if len(all_categories) > 1:
            print(f"  All categories: {', '.join(all_categories)}")
        print(f"  Path: videos/{year}/{slug}/")

        if not dry_run:
            # Create README
            video_dir = Path(VIDEOS_DIR) / year / slug
            video_dir.mkdir(parents=True, exist_ok=True)
            readme_content = create_video_readme(video)
            (video_dir / "README.md").write_text(readme_content, encoding="utf-8")

            # Update VIDEOS.md - primary category in table
            videos_md = insert_into_all_videos_table(videos_md, video, primary_category)

            # Insert into ALL matching category sections
            for cat in all_categories:
                videos_md = insert_into_category_section(videos_md, video, cat)

            # Close roadmap issue
            issue_num = close_roadmap_issue(video["title"], video["url"], repo)
            if issue_num:
                issues_closed.append(issue_num)
                print(f"  Closed issue: #{issue_num}")

        synced.append({
            "title": clean_title(video["title"]),
            "slug": slug,
            "year": year,
            "category": primary_category,
            "categories": all_categories,
            "video_id": video["video_id"]
        })

    if not dry_run and synced:
        # Update counts
        new_count = len(all_videos)
        videos_md = update_video_count(videos_md, new_count)

        # Update year range
        max_year = max(v["date"][:4] for v in all_videos)
        min_year = min(v["date"][:4] for v in all_videos)
        videos_md = update_year_range(videos_md, max_year, min_year)

        # Write updated VIDEOS.md
        with open(VIDEOS_MD_PATH, "w", encoding="utf-8") as f:
            f.write(videos_md)

        # Update README.md with latest video and count
        latest_video = all_videos[0]  # First video is newest
        update_readme(latest_video, new_count)

    return {
        "synced": len(synced),
        "videos": synced,
        "issues_closed": issues_closed,
        "dry_run": dry_run
    }


def main():
    parser = argparse.ArgumentParser(
        description="Sync videos from youtube-index.json to public GitHub repository"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without applying them"
    )
    parser.add_argument(
        "--index-path",
        type=str,
        help="Path to youtube-index.json (overrides config)"
    )
    args = parser.parse_args()

    # Override index path if provided
    if args.index_path:
        os.environ["YOUTUBE_INDEX_PATH"] = args.index_path

    print("=" * 60)
    print("YouTube Video Sync")
    print("=" * 60)

    if args.dry_run:
        print("\n[DRY RUN MODE - No changes will be made]\n")

    result = sync_videos(dry_run=args.dry_run)

    if result.get("error"):
        print(f"\nError: {result['error']}")
        sys.exit(1)

    print("\n" + "=" * 60)
    print(f"{'Would sync' if args.dry_run else 'Synced'}: {result['synced']} video(s)")

    if result.get("videos"):
        print("\nVideos:")
        for v in result["videos"]:
            cats = v.get("categories", [v["category"]])
            cat_str = ", ".join(cats)
            print(f"  - {v['title'][:50]}... [{cat_str}]")

    if result.get("issues_closed"):
        print(f"\nClosed issues: {', '.join(f'#{n}' for n in result['issues_closed'])}")

    if args.dry_run and result["synced"] > 0:
        print("\nRun without --dry-run to apply changes.")

    print("=" * 60)


if __name__ == "__main__":
    main()

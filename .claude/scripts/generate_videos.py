#!/usr/bin/env python3
"""
Generate video README files organized by year.

Reads from youtube-index.json and creates:
  videos/{year}/{slug}/README.md

Usage:
  python .claude/scripts/generate_videos.py
  python .claude/scripts/generate_videos.py --output-dir /path/to/videos
  python .claude/scripts/generate_videos.py --index-path /path/to/youtube-index.json

Run from video repository root.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
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
    print("Set YOUTUBE_INDEX_PATH environment variable or use --index-path argument")
    sys.exit(1)


def get_videos_full_path() -> str:
    """Get path to videos-full.json (with full descriptions)."""
    return os.path.join(os.path.dirname(__file__), "videos-full.json")


def slugify(title: str) -> str:
    """Convert title to URL-friendly slug."""
    # Remove emojis and special characters
    slug = re.sub(r'[^\w\s-]', '', title)
    # Convert to lowercase
    slug = slug.lower()
    # Replace spaces with hyphens
    slug = re.sub(r'[\s_]+', '-', slug)
    # Remove multiple consecutive hyphens
    slug = re.sub(r'-+', '-', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    # Limit length
    if len(slug) > 60:
        slug = slug[:60].rsplit('-', 1)[0]
    return slug


def format_date(date_str: str) -> str:
    """Format date as 'Month Day, Year'."""
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%B %d, %Y").replace(" 0", " ")


def clean_title(title: str) -> str:
    """Clean title of emojis for README heading."""
    return re.sub(r'[^\w\s\-\|\:\&\'\"\(\)\[\]\,\.\!\?]', '', title).strip()


def create_readme(video: dict) -> str:
    """Generate README.md content for a video."""
    title = video["title"]
    # Clean title of emojis for README heading
    cleaned_title = clean_title(title)

    description = video.get("summary", "")
    date = format_date(video["date"])
    video_id = video["video_id"]
    url = video["url"]

    readme = f"""# {cleaned_title}

[![Watch on YouTube](https://img.youtube.com/vi/{video_id}/maxresdefault.jpg)]({url})

**Published:** {date}

[Watch on YouTube]({url})

---

## Description

{description}
"""
    return readme


def main():
    parser = argparse.ArgumentParser(
        description="Generate video README files organized by year"
    )
    parser.add_argument(
        "--index-path",
        type=str,
        help="Path to youtube-index.json (overrides config)"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="videos",
        help="Output directory for video READMEs (default: videos)"
    )
    parser.add_argument(
        "--prefer-full",
        action="store_true",
        default=True,
        help="Prefer videos-full.json if it exists (has full descriptions)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be created without writing files"
    )
    args = parser.parse_args()

    # Override index path if provided
    if args.index_path:
        os.environ["YOUTUBE_INDEX_PATH"] = args.index_path

    # Determine source file
    videos_full_path = get_videos_full_path()
    youtube_index_path = get_youtube_index_path()

    # Prefer videos-full.json if it exists (has full descriptions)
    if args.prefer_full and os.path.exists(videos_full_path):
        source_path = videos_full_path
    else:
        source_path = youtube_index_path

    print(f"Reading from: {source_path}")
    with open(source_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    videos = data["videos"]
    print(f"Found {len(videos)} published videos")

    if args.dry_run:
        print("\n[DRY RUN MODE - No files will be created]\n")

    # Create output directory
    output_path = Path(args.output_dir)
    if not args.dry_run:
        output_path.mkdir(exist_ok=True)

    # Track stats
    years = {}
    created = 0

    for video in videos:
        # Extract year from date
        year = video["date"][:4]

        # Create slug from title
        slug = slugify(video["title"])

        # Create directory structure
        video_dir = output_path / year / slug

        if args.dry_run:
            print(f"  Would create: {video_dir}/README.md")
        else:
            video_dir.mkdir(parents=True, exist_ok=True)

            # Generate and write README
            readme_content = create_readme(video)
            readme_path = video_dir / "README.md"
            readme_path.write_text(readme_content, encoding="utf-8")

        created += 1

        # Track stats
        years[year] = years.get(year, 0) + 1

    # Print summary
    print(f"\n{'Would generate' if args.dry_run else 'Generated'} {created} video READMEs:")
    for year in sorted(years.keys()):
        print(f"  {year}: {years[year]} videos")

    if not args.dry_run:
        print(f"\nOutput: {output_path.absolute()}")
    else:
        print("\nRun without --dry-run to create files.")


if __name__ == "__main__":
    main()

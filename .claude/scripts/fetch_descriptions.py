#!/usr/bin/env python3
"""
Fetch full video descriptions from YouTube using yt-dlp.

Updates youtube-index.json with full descriptions.

Usage:
  python .claude/scripts/fetch_descriptions.py
  python .claude/scripts/fetch_descriptions.py --output /path/to/output.json
  python .claude/scripts/fetch_descriptions.py --index-path /path/to/youtube-index.json

Prerequisites:
  - yt-dlp installed (pip install yt-dlp or brew install yt-dlp)
"""

import argparse
import json
import os
import re
import subprocess
import sys
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


def get_default_output_path() -> str:
    """Get default output path for videos-full.json."""
    return os.path.join(os.path.dirname(__file__), "videos-full.json")


def fetch_description(video_url: str) -> Optional[str]:
    """Fetch full description from YouTube using yt-dlp."""
    try:
        result = subprocess.run(
            [
                "yt-dlp",
                "--skip-download",
                "--no-warnings",
                "--print", "description",
                video_url
            ],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"  Error: {result.stderr.strip()}")
            return None
    except subprocess.TimeoutExpired:
        print(f"  Timeout fetching description")
        return None
    except FileNotFoundError:
        print("  Error: yt-dlp not found. Install with: pip install yt-dlp")
        return None
    except Exception as e:
        print(f"  Exception: {e}")
        return None


def check_yt_dlp() -> bool:
    """Check if yt-dlp is installed."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Fetch full video descriptions from YouTube using yt-dlp"
    )
    parser.add_argument(
        "--index-path",
        type=str,
        help="Path to youtube-index.json (overrides config)"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output path for videos-full.json (default: .claude/scripts/videos-full.json)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Limit number of videos to process (0 = all)"
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip videos that already have descriptions longer than summary"
    )
    args = parser.parse_args()

    # Check yt-dlp is available
    if not check_yt_dlp():
        print("Error: yt-dlp is not installed or not in PATH")
        print("Install with: pip install yt-dlp")
        print("Or: brew install yt-dlp (macOS)")
        sys.exit(1)

    # Get paths
    if args.index_path:
        os.environ["YOUTUBE_INDEX_PATH"] = args.index_path

    youtube_index_path = get_youtube_index_path()
    output_path = args.output or get_default_output_path()

    # Load youtube index
    print(f"Reading from: {youtube_index_path}")
    with open(youtube_index_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    videos = data["videos"]
    total = len(videos)

    if args.limit > 0:
        videos = videos[:args.limit]
        print(f"Processing {len(videos)} of {total} videos (limited)")
    else:
        print(f"Found {total} videos\n")

    updated = 0
    skipped = 0
    failed = 0

    for i, video in enumerate(videos, 1):
        title = video["title"][:50] + "..." if len(video["title"]) > 50 else video["title"]
        print(f"[{i}/{len(videos)}] {title}")

        # Skip if already has full description
        if args.skip_existing:
            existing = video.get("summary", "")
            if len(existing) > 500:  # Likely already has full description
                print(f"  SKIPPED - already has description ({len(existing)} chars)")
                skipped += 1
                continue

        description = fetch_description(video["url"])

        if description:
            video["summary"] = description
            updated += 1
            print(f"  OK ({len(description)} chars)")
        else:
            failed += 1
            print(f"  FAILED - keeping existing")

    # Save to output file (not updating original index)
    print(f"\nSaving to: {output_path}")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nDone!")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Failed: {failed}")
    print(f"\nNext step: python .claude/scripts/generate_videos.py")


if __name__ == "__main__":
    main()

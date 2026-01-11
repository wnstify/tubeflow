#!/usr/bin/env python3
"""
TubeFlow Template Processor

Replaces {{VARIABLE}} placeholders in all template files with values from config.yaml.
Used by install.sh during initial setup and can be run manually to update templates.

Usage:
    python process_templates.py config.yaml [base_dir]
    python process_templates.py --help
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Dict, Optional

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)


# Files and directories to process
TEMPLATE_DIRS = [
    ".claude/agents",
    ".claude/commands",
    ".claude/skills",
    "templates",
]

TEMPLATE_EXTENSIONS = [".md", ".yaml", ".yml", ".json"]

# Variable mapping from config.yaml structure to template variables
VARIABLE_MAP = {
    # Channel
    "CHANNEL_NAME": "channel.name",
    "CHANNEL_HANDLE": "channel.handle",
    "CHANNEL_TAGLINE": "channel.tagline",

    # Voice
    "VOICE_STYLE_FILE": "voice.style_file",
    "CHANNEL_OVERVIEW_FILE": "voice.channel_overview_file",

    # Structure
    "YOUTUBE_ROOT": "structure.youtube_root",
    "SOCIAL_ROOT": "structure.social_root",
    "TEMPLATES_ROOT": "structure.templates_root",

    # Links
    "DISCORD_URL": "links.discord",
    "BUSINESS_URL": "links.business",
    "GITHUB_ORG": "links.github_org",
    "VOTING_REPO": "links.voting_repo",
    "DOCKER_REPO": "links.docker_repo",
    "LINKEDIN_URL": "links.linkedin",
    "FACEBOOK_URL": "links.facebook",
    "TWITTER_URL": "links.twitter",
    "REVIEWS_URL": "links.reviews",
    "FEATURED_VIDEO_URL": "links.featured_video",
    "FEATURED_VIDEO_TITLE": "links.featured_video_title",

    # About
    "ABOUT_COMPANY": "about.company_name",
    "ABOUT_ESTABLISHED": "about.established",
    "ABOUT_LOCATION": "about.location",
    "ABOUT_TAGLINE": "about.tagline",
    "APPLICATION_URL": "about.application_url",
}


def get_nested_value(config: Dict[str, Any], path: str) -> Optional[str]:
    """Get a value from nested dict using dot notation."""
    keys = path.split(".")
    value = config
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return None
    return str(value) if value is not None else None


def load_config(config_path: Path) -> Dict[str, Any]:
    """Load configuration from YAML file."""
    if not config_path.exists():
        print(f"Error: Config file not found: {config_path}")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_replacements(config: Dict[str, Any]) -> Dict[str, str]:
    """Build replacement dict from config using variable map."""
    replacements = {}

    for var_name, config_path in VARIABLE_MAP.items():
        value = get_nested_value(config, config_path)
        if value:
            replacements[var_name] = value
        else:
            # Keep placeholder if no value
            replacements[var_name] = f"{{{{CONFIGURE_{var_name}}}}}"

    return replacements


def process_content(content: str, replacements: Dict[str, str]) -> str:
    """Replace all {{VARIABLE}} placeholders in content."""
    result = content

    for var_name, value in replacements.items():
        # Match {{VARIABLE}} pattern
        pattern = r"\{\{" + var_name + r"\}\}"
        result = re.sub(pattern, value, result)

    return result


def process_file(file_path: Path, replacements: Dict[str, str], dry_run: bool = False) -> bool:
    """Process a single file, replacing variables."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            original_content = f.read()

        processed_content = process_content(original_content, replacements)

        if original_content != processed_content:
            if dry_run:
                print(f"  Would update: {file_path}")
            else:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(processed_content)
                print(f"  Updated: {file_path}")
            return True
        return False
    except Exception as e:
        print(f"  Error processing {file_path}: {e}")
        return False


def find_template_files(base_dir: Path) -> list:
    """Find all template files to process."""
    files = []

    for template_dir in TEMPLATE_DIRS:
        dir_path = base_dir / template_dir
        if dir_path.exists():
            for ext in TEMPLATE_EXTENSIONS:
                files.extend(dir_path.rglob(f"*{ext}"))

    return files


def validate_config(config: Dict[str, Any]) -> list:
    """Validate config and return list of warnings."""
    warnings = []

    required_fields = [
        ("channel.name", "Channel name"),
        ("channel.handle", "Channel handle"),
        ("links.discord", "Discord URL"),
        ("links.business", "Business URL"),
        ("links.github_org", "GitHub org URL"),
    ]

    for path, name in required_fields:
        if not get_nested_value(config, path):
            warnings.append(f"Missing required field: {name} ({path})")

    return warnings


def main():
    parser = argparse.ArgumentParser(
        description="Process TubeFlow templates by replacing {{VARIABLE}} placeholders"
    )
    parser.add_argument(
        "config",
        type=Path,
        help="Path to config.yaml file"
    )
    parser.add_argument(
        "base_dir",
        type=Path,
        nargs="?",
        default=Path.cwd(),
        help="Base directory containing template files (default: current directory)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without making changes"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed output"
    )

    args = parser.parse_args()

    # Load config
    print(f"Loading config from: {args.config}")
    config = load_config(args.config)

    # Validate config
    warnings = validate_config(config)
    for warning in warnings:
        print(f"Warning: {warning}")

    # Build replacements
    replacements = build_replacements(config)

    if args.verbose:
        print("\nVariable replacements:")
        for var, value in sorted(replacements.items()):
            if not value.startswith("{{CONFIGURE_"):
                print(f"  {var}: {value[:50]}{'...' if len(value) > 50 else ''}")

    # Find and process files
    print(f"\nProcessing templates in: {args.base_dir}")
    files = find_template_files(args.base_dir)

    if not files:
        print("No template files found to process.")
        return 0

    updated_count = 0
    for file_path in files:
        if process_file(file_path, replacements, args.dry_run):
            updated_count += 1

    print(f"\nProcessed {len(files)} files, updated {updated_count}")

    if args.dry_run:
        print("\n(Dry run - no files were actually changed)")

    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env bash

# TubeFlow Installer
# Interactive setup wizard for TubeFlow YouTube Content System
# Works on: macOS, Linux (Debian/Ubuntu, Fedora, Arch), WSL2
#
# Requirements:
#   - Bash 4.0+ (macOS: brew install bash)
#   - Python 3.10+
#   - Claude Code CLI
#
# Usage:
#   ./install.sh              Interactive mode
#   ./install.sh --help       Show help

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo ""
echo -e "${CYAN}${BOLD}"
echo "  ████████╗██╗   ██╗██████╗ ███████╗███████╗██╗      ██████╗ ██╗    ██╗"
echo "  ╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔════╝██║     ██╔═══██╗██║    ██║"
echo "     ██║   ██║   ██║██████╔╝█████╗  █████╗  ██║     ██║   ██║██║ █╗ ██║"
echo "     ██║   ██║   ██║██╔══██╗██╔══╝  ██╔══╝  ██║     ██║   ██║██║███╗██║"
echo "     ██║   ╚██████╔╝██████╔╝███████╗██║     ███████╗╚██████╔╝╚███╔███╔╝"
echo "     ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝ "
echo -e "${NC}"
echo -e "${BOLD}  AI-Powered YouTube Content System for Claude Code${NC}"
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""

# Check prerequisites
echo -e "${BLUE}Checking prerequisites...${NC}"
echo ""

# Check Claude Code
if command -v claude &> /dev/null; then
    CLAUDE_VERSION=$(claude --version 2>/dev/null || echo "installed")
    echo -e "  ${GREEN}✓${NC} Claude Code CLI: ${CLAUDE_VERSION}"
else
    echo -e "  ${RED}✗${NC} Claude Code CLI: Not found"
    echo ""
    echo -e "  ${YELLOW}Claude Code is required. Install from:${NC}"
    echo "    https://claude.ai/claude-code"
    echo ""
    exit 1
fi

# Check Python (3.10+ required)
PYTHON_CMD=""
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
fi

if [[ -n "$PYTHON_CMD" ]]; then
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1)
    # Extract version numbers
    PY_MAJOR=$($PYTHON_CMD -c "import sys; print(sys.version_info.major)")
    PY_MINOR=$($PYTHON_CMD -c "import sys; print(sys.version_info.minor)")

    if [[ "$PY_MAJOR" -ge 3 && "$PY_MINOR" -ge 10 ]]; then
        echo -e "  ${GREEN}✓${NC} Python: ${PYTHON_VERSION}"
    else
        echo -e "  ${RED}✗${NC} Python: ${PYTHON_VERSION} (requires 3.10+)"
        echo ""
        echo "  Python 3.10+ is required. Download from:"
        echo "    https://www.python.org/downloads/"
        exit 1
    fi
else
    echo -e "  ${RED}✗${NC} Python 3: Not found"
    echo ""
    echo "  Python 3.10+ is required. Download from:"
    echo "    https://www.python.org/downloads/"
    exit 1
fi

# Check pip
if command -v pip3 &> /dev/null || python3 -m pip --version &> /dev/null; then
    echo -e "  ${GREEN}✓${NC} pip: Available"
else
    echo -e "  ${YELLOW}!${NC} pip: Not found (optional but recommended)"
fi

# Check Git
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version 2>&1)
    echo -e "  ${GREEN}✓${NC} Git: ${GIT_VERSION}"
else
    echo -e "  ${YELLOW}!${NC} Git: Not found (required for sync features)"
fi

# Check yt-dlp
if command -v yt-dlp &> /dev/null; then
    YTDLP_VERSION=$(yt-dlp --version 2>&1)
    echo -e "  ${GREEN}✓${NC} yt-dlp: ${YTDLP_VERSION}"
else
    echo -e "  ${YELLOW}!${NC} yt-dlp: Not found (optional, for sync features)"
    echo "      Install with: pip install yt-dlp"
fi

# Check PyYAML (6.0+)
if $PYTHON_CMD -c "import yaml; v=yaml.__version__; exit(0 if tuple(map(int, v.split('.')[:2])) >= (6,0) else 1)" 2>/dev/null; then
    PYYAML_VERSION=$($PYTHON_CMD -c "import yaml; print(yaml.__version__)")
    echo -e "  ${GREEN}✓${NC} PyYAML: ${PYYAML_VERSION}"
elif $PYTHON_CMD -c "import yaml" 2>/dev/null; then
    PYYAML_VERSION=$($PYTHON_CMD -c "import yaml; print(yaml.__version__)")
    echo -e "  ${YELLOW}!${NC} PyYAML: ${PYYAML_VERSION} (recommend 6.0+)"
    echo -e "      Upgrading PyYAML..."
    pip3 install -U pyyaml --quiet 2>/dev/null || $PYTHON_CMD -m pip install -U pyyaml --quiet
else
    echo -e "  ${YELLOW}!${NC} PyYAML: Not found"
    echo -e "      Installing PyYAML..."
    pip3 install pyyaml --quiet 2>/dev/null || $PYTHON_CMD -m pip install pyyaml --quiet
fi

echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
echo -e "${BOLD}Channel Configuration${NC}"
echo ""
echo "Let's set up TubeFlow for your YouTube channel."
echo ""

# Channel Identity
echo -e "${CYAN}Channel Identity${NC}"
echo ""

read -p "  Channel name (e.g., TechWithTim): " CHANNEL_NAME
while [[ -z "$CHANNEL_NAME" ]]; do
    echo -e "  ${RED}Channel name is required${NC}"
    read -p "  Channel name: " CHANNEL_NAME
done

read -p "  Channel handle (e.g., @techwithtime): " CHANNEL_HANDLE
if [[ ! "$CHANNEL_HANDLE" =~ ^@ ]]; then
    CHANNEL_HANDLE="@$CHANNEL_HANDLE"
fi

read -p "  Channel tagline (one line): " CHANNEL_TAGLINE
CHANNEL_TAGLINE="${CHANNEL_TAGLINE:-Your tagline here}"

echo ""
echo -e "${CYAN}Links (Required)${NC}"
echo ""

read -p "  Discord URL: " DISCORD_URL
while [[ -z "$DISCORD_URL" ]]; do
    echo -e "  ${RED}Discord URL is required${NC}"
    read -p "  Discord URL: " DISCORD_URL
done

read -p "  Business/Contact URL: " BUSINESS_URL
while [[ -z "$BUSINESS_URL" ]]; do
    echo -e "  ${RED}Business URL is required${NC}"
    read -p "  Business URL: " BUSINESS_URL
done

read -p "  GitHub Org URL (e.g., https://github.com/yourorg): " GITHUB_ORG
while [[ -z "$GITHUB_ORG" ]]; do
    echo -e "  ${RED}GitHub Org URL is required${NC}"
    read -p "  GitHub Org URL: " GITHUB_ORG
done

echo ""
echo -e "${CYAN}Links (Optional - press Enter to skip)${NC}"
echo ""

read -p "  Voting Repo URL (for community voting): " VOTING_REPO
read -p "  Docker Repo URL (for Docker content): " DOCKER_REPO
read -p "  LinkedIn URL: " LINKEDIN_URL
read -p "  Facebook URL: " FACEBOOK_URL
read -p "  Twitter/X URL: " TWITTER_URL
read -p "  Reviews URL (Trustpilot, etc.): " REVIEWS_URL
read -p "  Featured Video URL (your flagship video): " FEATURED_VIDEO_URL
read -p "  Featured Video Title: " FEATURED_VIDEO_TITLE

echo ""
echo -e "${CYAN}Features${NC}"
echo ""

read -p "  Enable public repo sync? [Y/n]: " ENABLE_SYNC
ENABLE_SYNC="${ENABLE_SYNC:-Y}"
[[ "$ENABLE_SYNC" =~ ^[Yy] ]] && ENABLE_SYNC="true" || ENABLE_SYNC="false"

read -p "  Enable social media workflow? [Y/n]: " ENABLE_SOCIAL
ENABLE_SOCIAL="${ENABLE_SOCIAL:-Y}"
[[ "$ENABLE_SOCIAL" =~ ^[Yy] ]] && ENABLE_SOCIAL="true" || ENABLE_SOCIAL="false"

read -p "  Enable research agents? [Y/n]: " ENABLE_RESEARCH
ENABLE_RESEARCH="${ENABLE_RESEARCH:-Y}"
[[ "$ENABLE_RESEARCH" =~ ^[Yy] ]] && ENABLE_RESEARCH="true" || ENABLE_RESEARCH="false"

read -p "  Enable sponsorship research? [Y/n]: " ENABLE_SPONSORSHIP
ENABLE_SPONSORSHIP="${ENABLE_SPONSORSHIP:-Y}"
[[ "$ENABLE_SPONSORSHIP" =~ ^[Yy] ]] && ENABLE_SPONSORSHIP="true" || ENABLE_SPONSORSHIP="false"

read -p "  Using Obsidian? [Y/n]: " USE_OBSIDIAN
USE_OBSIDIAN="${USE_OBSIDIAN:-Y}"
[[ "$USE_OBSIDIAN" =~ ^[Yy] ]] && USE_OBSIDIAN="true" || USE_OBSIDIAN="false"

echo ""
echo -e "${CYAN}Folder Structure${NC}"
echo ""

if [[ "$USE_OBSIDIAN" == "true" ]]; then
    read -p "  YouTube folder name [03-YouTube]: " YOUTUBE_ROOT
    YOUTUBE_ROOT="${YOUTUBE_ROOT:-03-YouTube}"
    read -p "  Social folder name [04-Social]: " SOCIAL_ROOT
    SOCIAL_ROOT="${SOCIAL_ROOT:-04-Social}"
    read -p "  Templates folder name [05-Templates]: " TEMPLATES_ROOT
    TEMPLATES_ROOT="${TEMPLATES_ROOT:-05-Templates}"
else
    read -p "  YouTube folder name [youtube]: " YOUTUBE_ROOT
    YOUTUBE_ROOT="${YOUTUBE_ROOT:-youtube}"
    read -p "  Social folder name [social]: " SOCIAL_ROOT
    SOCIAL_ROOT="${SOCIAL_ROOT:-social}"
    read -p "  Templates folder name [templates]: " TEMPLATES_ROOT
    TEMPLATES_ROOT="${TEMPLATES_ROOT:-templates}"
fi

echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
echo -e "${BOLD}Generating Configuration...${NC}"
echo ""

# Create config.yaml
cat > "$SCRIPT_DIR/config.yaml" <<EOF
# TubeFlow Configuration
# Generated by install.sh on $(date)

version: "1.0"

channel:
  name: "$CHANNEL_NAME"
  handle: "$CHANNEL_HANDLE"
  tagline: "$CHANNEL_TAGLINE"
  niche: "self-hosting"

voice:
  style_file: "writing-style.md"
  channel_overview_file: "channel-overview.md"
  tone: "friendly"

structure:
  type: "$([[ "$USE_OBSIDIAN" == "true" ]] && echo "obsidian" || echo "markdown")"
  youtube_root: "$YOUTUBE_ROOT"
  social_root: "$SOCIAL_ROOT"
  templates_root: "$TEMPLATES_ROOT"
  ideas_folder: "ideas"
  drafts_folder: "drafts"
  published_folder: "published"
  research_folder: "research"

links:
  discord: "$DISCORD_URL"
  business: "$BUSINESS_URL"
  github_org: "$GITHUB_ORG"
  voting_repo: "$VOTING_REPO"
  docker_repo: "$DOCKER_REPO"
  linkedin: "$LINKEDIN_URL"
  facebook: "$FACEBOOK_URL"
  twitter: "$TWITTER_URL"
  reviews: "$REVIEWS_URL"
  featured_video: "$FEATURED_VIDEO_URL"
  featured_video_title: "$FEATURED_VIDEO_TITLE"

features:
  public_repo_sync: $ENABLE_SYNC
  social_media: $ENABLE_SOCIAL
  research_agents: $ENABLE_RESEARCH
  sponsorship_research: $ENABLE_SPONSORSHIP
  obsidian_links: $USE_OBSIDIAN
  include_about_section: true

about:
  company_name: "$CHANNEL_NAME"
  established: "$(date +%Y)"
  location: ""
  tagline: "$CHANNEL_TAGLINE"
  application_url: ""

advanced:
  research_model: "haiku"
  strategy_model: "opus"
  content_model: "sonnet"
  parallel_research: true
  auto_publish_prompt: true
EOF

echo -e "  ${GREEN}✓${NC} Created config.yaml"

# Process templates
echo ""
echo -e "${BOLD}Processing Templates...${NC}"
echo ""

$PYTHON_CMD "$SCRIPT_DIR/.claude/scripts/process_templates.py" "$SCRIPT_DIR/config.yaml" "$SCRIPT_DIR"
if [[ $? -eq 0 ]]; then
    echo -e "  ${GREEN}✓${NC} Templates processed successfully"
else
    echo -e "  ${YELLOW}!${NC} Template processing had warnings (check output above)"
fi

# Create voice files if they don't exist
echo ""
echo -e "${BOLD}Creating Voice Files...${NC}"
echo ""

if [[ ! -f "$SCRIPT_DIR/writing-style.md" ]]; then
    cat > "$SCRIPT_DIR/writing-style.md" <<EOF
# Writing Style Guide

This file defines how content should sound. Customize this to match your voice.

## Tone
- Friendly and approachable
- Direct and clear
- Solution-focused

## Sentence Style
- Short sentences (5-15 words ideal)
- Start with action verbs
- Use questions to engage

## Phrases to Use
- "Here's the thing..."
- "Let me show you."
- "No fluff. Just what works."

## Things to Avoid
- Jargon without explanation
- Filler words
- Overly formal language

## Emoji Usage
- Strategic, not spam
- Use for visual breaks
- Keep professional
EOF
    echo -e "  ${GREEN}✓${NC} Created writing-style.md (customize this!)"
else
    echo -e "  ${YELLOW}!${NC} writing-style.md already exists"
fi

if [[ ! -f "$SCRIPT_DIR/channel-overview.md" ]]; then
    cat > "$SCRIPT_DIR/channel-overview.md" <<EOF
# Channel Overview

## About ${CHANNEL_NAME}

${CHANNEL_TAGLINE}

## Core Values

1. **Value 1** - Description
2. **Value 2** - Description
3. **Value 3** - Description

## Content Focus

- Topic 1
- Topic 2
- Topic 3

## Target Audience

Who watches your content and what do they want to learn?
EOF
    echo -e "  ${GREEN}✓${NC} Created channel-overview.md (customize this!)"
else
    echo -e "  ${YELLOW}!${NC} channel-overview.md already exists"
fi

echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
echo -e "${GREEN}${BOLD}Setup Complete!${NC}"
echo ""
echo -e "${BOLD}Next Steps:${NC}"
echo ""
echo "  1. ${CYAN}Customize your voice:${NC}"
echo "     Edit writing-style.md and channel-overview.md"
echo ""
echo "  2. ${CYAN}Copy to your vault:${NC}"
echo "     cp -r .claude/ /path/to/your/vault/.claude/"
echo "     cp -r templates/ /path/to/your/vault/${TEMPLATES_ROOT}/"
echo ""
echo "  3. ${CYAN}Test with a simple command:${NC}"
echo "     /youtube idea \"Test Topic\""
echo ""
echo "  4. ${CYAN}Read the docs:${NC}"
echo "     cat docs/GETTING_STARTED.md"
echo ""
echo -e "${BOLD}Commands Available:${NC}"
echo ""
echo "  /youtube idea \"Topic\"      Quick idea capture"
echo "  /youtube full \"Topic\"      Complete draft package"
echo "  /youtube publish \"Topic\"   Move to published"
echo "  /youtube sync              Sync to public repo"
echo "  /youtube-research \"Topic\"  Deep research"
echo "  /social all \"Topic\"        All platforms"
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""

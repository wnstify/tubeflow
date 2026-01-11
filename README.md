# TubeFlow

```
  ████████╗██╗   ██╗██████╗ ███████╗███████╗██╗      ██████╗ ██╗    ██╗
  ╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔════╝██║     ██╔═══██╗██║    ██║
     ██║   ██║   ██║██████╔╝█████╗  █████╗  ██║     ██║   ██║██║ █╗ ██║
     ██║   ██║   ██║██╔══██╗██╔══╝  ██╔══╝  ██║     ██║   ██║██║███╗██║
     ██║   ╚██████╔╝██████╔╝███████╗██║     ███████╗╚██████╔╝╚███╔███╔╝
     ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝
```

**Research-First YouTube Content Creation Pipeline for Claude Code**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-green.svg)](https://claude.ai/claude-code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](docs/CONTRIBUTING.md)

TubeFlow is an open-source content creation system that transforms how you produce YouTube videos and social media posts. Built for Claude Code, it provides a complete pipeline from research to publication with proper formatting, voice preservation, and community integration.

---

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Installed Components](#installed-components)
- [Commands Reference](#commands-reference)
- [Pipeline Overview](#pipeline-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Why TubeFlow?](#why-tubeflow)
- [Unique Features](#unique-features-no-alternative-exists)
- [Market Position](#market-position)
- [By the Numbers](#by-the-numbers)
- [Author](#author)
- [About Webnestify](#about-webnestify)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### Research-First Content Creation
5 specialized AI agents work in parallel to gather comprehensive research before you write a single word:
- **Topic Gatherer** - Features, documentation, complexity analysis
- **Competitor Gatherer** - Existing videos, content gaps, differentiation
- **SEO Gatherer** - Keywords, search trends, optimal titles
- **Community Gatherer** - Reddit, forums, real user questions
- **Research Strategist** - Synthesizes findings into actionable strategy

### YouTube-Native Formatting
Content is formatted correctly for YouTube from the start:
- `*bold*` not `**bold**` (YouTube doesn't support Markdown)
- Proper link formatting with `https://` prefix
- Character-limit aware (100-160 chars above the fold)
- Platform-specific emoji and hashtag guidelines

### Complete 6-Step Pipeline
```
Research → Create → Review → Publish → Sync → Social
```
From idea to multi-platform promotion in one workflow.

### Voice & Style Preservation
Your content sounds like you, not AI. TubeFlow uses your personal writing style guide to maintain consistent voice.

### Open-Source Acknowledgment Automation
Automatically researches and credits open-source projects:
- Finds developer/maintainer names
- Discovers FUNDING.yml, GitHub Sponsors, Open Collective
- Generates genuine attribution and support links

### GitHub Community Integration
- Public video repository for community voting
- Roadmap issues auto-close when videos publish
- Video catalog stays in sync with your channel

### Multi-Platform Social Media
Platform-optimized posts for LinkedIn, Twitter/X, and Facebook from a single command.

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/wnstify/tubeflow.git
cd tubeflow

# Run interactive installer
./install.sh

# Test with your first command
/youtube idea "My First Video Topic"
```

---

## Installed Components

TubeFlow includes **46 files** across 10 categories:

### Agents (9 files)

Specialized AI agents in `.claude/agents/`:

| Agent | File | Purpose |
|-------|------|---------|
| **YouTube Creator** | `youtube-creator.md` | Creates video scripts, ideas, descriptions, full packages |
| **YouTube Publisher** | `youtube-publisher.md` | Handles post-upload workflow, moves files, creates metadata |
| **YouTube Syncer** | `youtube-syncer.md` | Syncs published videos to public GitHub repository |
| **Topic Gatherer** | `yt-topic-gatherer.md` | Deep research into subject matter, features, docs |
| **Competitor Gatherer** | `yt-competitor-gatherer.md` | Analyzes existing YouTube videos, finds gaps |
| **SEO Gatherer** | `yt-seo-gatherer.md` | Researches keywords, trends, optimal titles |
| **Community Gatherer** | `yt-community-gatherer.md` | Researches Reddit, forums, community questions |
| **Research Strategist** | `yt-research-strategist.md` | Synthesizes all research into strategic recommendations |
| **Social Creator** | `social-creator.md` | Creates LinkedIn, Twitter, Facebook posts |

### Commands (3 files)

Slash commands in `.claude/commands/`:

| Command | File | Description |
|---------|------|-------------|
| `/youtube` | `youtube.md` | Main YouTube workflow (idea, full, publish, sync) |
| `/youtube-research` | `youtube-research.md` | Comprehensive 5-agent research workflow |
| `/social` | `social.md` | Social media content creation |

### Skills (3 folders)

Workflow skills in `.claude/skills/`:

| Skill | Folder | Purpose |
|-------|--------|---------|
| **YouTube Workflow** | `youtube-workflow/` | Content creation methodology, templates, voice integration |
| **YouTube Research** | `youtube-research/` | Research orchestration, agent coordination |
| **Social Workflow** | `social-workflow/` | Platform-specific posting guidelines |

### Python Scripts (5 files)

Utility scripts in `.claude/scripts/`:

| Script | Purpose |
|--------|---------|
| `sync_videos.py` | Syncs videos to public repo, creates READMEs, updates catalog |
| `create_issues.py` | Creates GitHub Issues from roadmap for community voting |
| `fetch_descriptions.py` | Fetches full descriptions from YouTube via yt-dlp |
| `generate_videos.py` | Generates video README files from index |
| `process_templates.py` | Replaces {{VARIABLE}} placeholders during install |

### Templates (8 files)

Content templates in `templates/`:

| Template | Purpose |
|----------|---------|
| `youtube-description.md` | YouTube description with all sections |
| `youtube-pinned-comment.md` | Engagement-driving pinned comment |
| `youtube-script.md` | Full video script structure |
| `youtube-idea.md` | Quick idea capture format |
| `youtube-formatting-reference.md` | YouTube-native formatting guide |
| `social-linkedin.md` | LinkedIn post template |
| `social-twitter.md` | Twitter/X post and thread template |
| `social-facebook.md` | Facebook post template |

### Documentation (4 files)

Guides in `docs/`:

| Document | Description |
|----------|-------------|
| `GETTING_STARTED.md` | Step-by-step setup and first workflow |
| `CONFIGURATION.md` | Complete config.yaml reference |
| `WORKFLOWS.md` | Detailed workflow documentation |
| `CONTRIBUTING.md` | How to contribute to TubeFlow |

### GitHub Templates (4 files)

Issue and PR templates in `.github/`:

| Template | Purpose |
|----------|---------|
| `ISSUE_TEMPLATE/bug_report.md` | Structured bug report with environment info |
| `ISSUE_TEMPLATE/feature_request.md` | Feature request with use cases and priority |
| `ISSUE_TEMPLATE/config.yml` | Template chooser configuration |
| `PULL_REQUEST_TEMPLATE.md` | PR template with checklist and testing |

### Root Files (8 files)

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `USAGE.md` | Comprehensive usage guide |
| `CHANGELOG.md` | Version history and changes |
| `LICENSE` | MIT License |
| `install.sh` | Interactive setup wizard (macOS/Linux/WSL2) |
| `install.ps1` | Interactive setup wizard (Windows PowerShell) |
| `config.example.yaml` | Example configuration with all options |
| `.gitignore` | Git ignore patterns |

### Examples (2 files)

Production example in `examples/webnestify/`:

| File | Purpose |
|------|---------|
| `config.yaml` | Real production configuration example |
| `README.md` | Example documentation |

---

## Commands Reference

### YouTube Commands

| Command | Description | Output |
|---------|-------------|--------|
| `/youtube idea "Topic"` | Quick idea capture | `{{YOUTUBE_ROOT}}/ideas/YYYY-MM-DD-topic.md` |
| `/youtube full "Topic"` | Complete draft package | `{{YOUTUBE_ROOT}}/drafts/YYYY-MM-DD-topic/` |
| `/youtube publish "Topic"` | Move to published | `{{YOUTUBE_ROOT}}/published/YYYY/topic-slug/` |
| `/youtube sync` | Sync to public repo | Updates public GitHub repository |
| `/youtube-research "Topic"` | Deep research | `{{YOUTUBE_ROOT}}/research/YYYY-MM-DD-topic/` |

### Social Commands

| Command | Description | Output |
|---------|-------------|--------|
| `/social linkedin "Topic"` | LinkedIn post | `{{SOCIAL_ROOT}}/linkedin/YYYY-MM-DD-topic.md` |
| `/social twitter "Topic"` | Twitter post/thread | `{{SOCIAL_ROOT}}/twitter/YYYY-MM-DD-topic.md` |
| `/social facebook "Topic"` | Facebook post | `{{SOCIAL_ROOT}}/facebook/YYYY-MM-DD-topic.md` |
| `/social all "Topic"` | All platforms | All three platform files |
| `/social video "slug"` | From published video | All platforms from video metadata |

For detailed usage, see [USAGE.md](USAGE.md).

---

## Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         TUBEFLOW VIDEO PIPELINE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. RESEARCH (Optional)           /youtube-research "Topic"                  │
│     ├── Topic Gatherer ────────── Features, docs, complexity                 │
│     ├── Competitor Gatherer ───── Existing videos, gaps                      │
│     ├── SEO Gatherer ──────────── Keywords, trends                           │
│     ├── Community Gatherer ────── Reddit, forums, questions                  │
│     └── Research Strategist ───── Strategic synthesis                        │
│         Output: research-pack.md + series-structure.md (if series)           │
│                                                                              │
│  2. CREATE                        /youtube full "Topic"                      │
│     └── YouTube Creator ───────── Script, description, thumbnail, comment    │
│         Output: drafts/YYYY-MM-DD-topic/                                     │
│                 ├── script.md                                                │
│                 ├── description.md                                           │
│                 ├── thumbnail-text.md                                        │
│                 └── pinned-comment.md                                        │
│                                                                              │
│  3. FILM & UPLOAD                 [You do this manually]                     │
│                                                                              │
│  4. PUBLISH                       /youtube publish "Topic"                   │
│     └── YouTube Publisher ─────── Verify upload, fetch metadata              │
│         Output: published/YYYY/topic-slug/                                   │
│                 ├── video.md (YouTube metadata)                              │
│                 ├── script.md                                                │
│                 ├── description.md                                           │
│                 ├── thumbnail-text.md                                        │
│                 ├── pinned-comment.md                                        │
│                 └── social-content.json                                      │
│                                                                              │
│  5. SYNC TO PUBLIC REPO           /youtube sync                              │
│     └── YouTube Syncer ────────── Push to GitHub, update catalog             │
│         Output: Public repository with:                                      │
│                 ├── videos/YYYY/topic-slug/README.md                         │
│                 ├── VIDEOS.md (updated catalog)                              │
│                 ├── README.md (latest video)                                 │
│                 └── Closed roadmap issues                                    │
│                                                                              │
│  6. SOCIAL PROMOTION              /social video "topic-slug"                 │
│     └── Social Creator ────────── Platform-optimized posts                   │
│         Output: {{SOCIAL_ROOT}}/                                             │
│                 ├── linkedin/YYYY-MM-DD-topic.md                             │
│                 ├── twitter/YYYY-MM-DD-topic.md                              │
│                 └── facebook/YYYY-MM-DD-topic.md                             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Prerequisites

| Requirement | Version | Required | Notes |
|-------------|---------|----------|-------|
| **Claude Code CLI** | Latest (2026) | Yes | Core functionality |
| **Python** | 3.10+ (3.14.2 recommended) | Yes | Scripts and template processing |
| **pip** | Any | Yes | Python package management |
| **Git** | 2.40+ | Yes | Repository management |
| **PyYAML** | 6.0+ (6.0.3 recommended) | Yes | Auto-installed by installer |
| **yt-dlp** | 2025.12+ | No | For sync metadata extraction |

### Platform Support

| Platform | Status | Installer |
|----------|--------|-----------|
| **macOS** (Intel/Apple Silicon) | Fully supported | `./install.sh` |
| **Linux** (Ubuntu/Debian/Fedora/Arch) | Fully supported | `./install.sh` |
| **Windows 10/11** | Fully supported | `.\install.ps1` |
| **WSL2** | Fully supported | `./install.sh` |

### Optional MCP Servers

For enhanced research capabilities:

| MCP Server | Purpose |
|------------|---------|
| Perplexity | Web search for research agents |
| Sequential Thinking | Complex reasoning support |

---

## Installation

### macOS / Linux / WSL2

```bash
# Clone the repository
git clone https://github.com/wnstify/tubeflow.git
cd tubeflow

# Make installer executable (if needed)
chmod +x install.sh

# Run interactive installer
./install.sh
```

### Windows (PowerShell)

```powershell
# Clone the repository
git clone https://github.com/wnstify/tubeflow.git
cd tubeflow

# Run interactive installer
.\install.ps1
```

**Note**: If you see an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### What the Installer Does

1. Checks prerequisites (Python, Claude Code, Git, etc.)
2. Asks for your channel details
3. Generates `config.yaml`
4. Processes templates with your values
5. Creates voice files

### Manual Setup (All Platforms)

```bash
git clone https://github.com/wnstify/tubeflow.git
cd tubeflow

# Copy and edit configuration
cp config.example.yaml config.yaml
# Edit config.yaml with your values

# Process templates
python3 .claude/scripts/process_templates.py config.yaml .

# Create voice files
touch writing-style.md channel-overview.md
# Edit these files with your style guide
```

### Copy to Your Vault

**macOS / Linux:**
```bash
cp -r .claude/ /path/to/your/vault/.claude/
cp -r templates/ /path/to/your/vault/{{TEMPLATES_ROOT}}/
cp writing-style.md channel-overview.md /path/to/your/vault/
```

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse .claude\ C:\path\to\your\vault\.claude\
Copy-Item -Recurse templates\ C:\path\to\your\vault\{{TEMPLATES_ROOT}}\
Copy-Item writing-style.md, channel-overview.md C:\path\to\your\vault\
```

---

## Configuration

TubeFlow uses a single `config.yaml` file:

```yaml
# Channel Identity
channel:
  name: "Your Channel"
  handle: "@yourchannel"
  tagline: "Your tagline"
  niche: "self-hosting"

# Voice & Style
voice:
  style_file: "writing-style.md"
  channel_overview_file: "channel-overview.md"
  tone: "friendly"

# Folder Structure
structure:
  type: "obsidian"  # or "markdown"
  youtube_root: "03-YouTube"
  social_root: "04-Social"
  templates_root: "05-Templates"

# Links
links:
  discord: "https://discord.gg/your-server"
  business: "https://yoursite.com/contact"
  github_org: "https://github.com/yourorg"
  voting_repo: "https://github.com/yourorg/youtube"
  # ... more links

# Features
features:
  public_repo_sync: true
  social_media: true
  research_agents: true
  sponsorship_research: true
```

See [docs/CONFIGURATION.md](docs/CONFIGURATION.md) for complete reference.

---

## Project Structure

```
tubeflow/
├── .claude/
│   ├── agents/                    # 9 AI agent definitions
│   │   ├── youtube-creator.md
│   │   ├── youtube-publisher.md
│   │   ├── youtube-syncer.md
│   │   ├── yt-topic-gatherer.md
│   │   ├── yt-competitor-gatherer.md
│   │   ├── yt-seo-gatherer.md
│   │   ├── yt-community-gatherer.md
│   │   ├── yt-research-strategist.md
│   │   └── social-creator.md
│   ├── commands/                  # 3 slash commands
│   │   ├── youtube.md
│   │   ├── youtube-research.md
│   │   └── social.md
│   ├── skills/                    # 3 workflow skills
│   │   ├── youtube-workflow/
│   │   ├── youtube-research/
│   │   └── social-workflow/
│   └── scripts/                   # 5 Python utilities
│       ├── sync_videos.py
│       ├── create_issues.py
│       ├── fetch_descriptions.py
│       ├── generate_videos.py
│       └── process_templates.py
├── templates/                     # 8 content templates
│   ├── youtube-description.md
│   ├── youtube-pinned-comment.md
│   ├── youtube-script.md
│   ├── youtube-idea.md
│   ├── youtube-formatting-reference.md
│   ├── social-linkedin.md
│   ├── social-twitter.md
│   └── social-facebook.md
├── docs/                          # 4 documentation files
│   ├── GETTING_STARTED.md
│   ├── CONFIGURATION.md
│   ├── WORKFLOWS.md
│   └── CONTRIBUTING.md
├── examples/
│   └── webnestify/                # Production example
│       ├── config.yaml
│       └── README.md
├── README.md                      # This file
├── USAGE.md                       # Detailed usage guide
├── LICENSE                        # MIT License
├── install.sh                     # Interactive installer
├── config.example.yaml            # Configuration template
└── .gitignore                     # Git ignore patterns
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [USAGE.md](USAGE.md) | Detailed usage guide with examples |
| [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md) | Step-by-step setup guide |
| [docs/CONFIGURATION.md](docs/CONFIGURATION.md) | Complete config.yaml reference |
| [docs/WORKFLOWS.md](docs/WORKFLOWS.md) | Pipeline and workflow documentation |
| [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) | How to contribute |

---

## Why TubeFlow?

### The Problem

YouTube content creation involves repetitive tasks that drain creative energy:
- Researching topics across multiple sources
- Writing descriptions with proper formatting (YouTube ≠ Markdown)
- Creating platform-specific social posts
- Managing drafts, published content, and metadata
- Crediting open-source projects correctly

Existing tools are either too simple (just templates) or too complex (enterprise video production). Nothing exists specifically for **technical content creators** using **AI-assisted workflows**.

### The Solution

TubeFlow is the first **research-first content pipeline** built natively for **Claude Code**. It transforms a 4-hour content process into 30 minutes of focused work.

---

## Unique Features (No Alternative Exists)

Based on market research (January 2026), TubeFlow offers capabilities not found in any other tool:

### 1. Research-First Architecture

**What it is:** 5 specialized AI agents work in parallel before you write anything.

**Why it matters:** Most tools start with a blank page. TubeFlow starts with:
- Topic analysis (features, docs, complexity)
- Competitor research (existing videos, content gaps)
- SEO intelligence (keywords, trends, optimal titles)
- Community insights (Reddit, forums, real questions)
- Strategic synthesis (single video vs. series recommendation)

**Result:** Every piece of content is informed by real data, not guesswork.

### 2. Claude Code Native

**What it is:** Built from the ground up for Claude Code's agent/skill/command architecture.

**Why it matters:** Other YouTube tools are:
- Standalone apps (require context switching)
- Web-based (can't access your local files)
- API wrappers (no real intelligence)

TubeFlow lives in your development environment. Research, write, and publish without leaving your terminal.

**Comparison:**

| Tool | Type | Claude Code Integration |
|------|------|------------------------|
| **TubeFlow** | Pipeline | Native (agents, skills, commands) |
| ShortGPT | Framework | None |
| text2youtube | Script | None |
| Kenny Liao's Plugin | Plugin | Partial (ideation only) |

### 3. Complete 6-Stage Pipeline

**What it is:** End-to-end workflow from idea to social promotion.

```
Research → Create → Review → Publish → Sync → Social
```

**Why it matters:** Other tools handle 1-2 stages. TubeFlow handles all 6:

| Stage | TubeFlow | Typical Tools |
|-------|----------|---------------|
| Research | 5-agent parallel research | Manual |
| Create | Script + description + thumbnail + comment | Template only |
| Review | Drafts folder with versioning | None |
| Publish | Metadata extraction, file organization | Manual |
| Sync | GitHub repo with voting | None |
| Social | 3 platforms, optimized per platform | Copy-paste |

### 4. Platform-Native Formatting

**What it is:** Content is formatted correctly for each platform from the start.

**Why it matters:** Each platform has quirks that break copy-paste:

| Platform | Gotcha | TubeFlow Handles It |
|----------|--------|---------------------|
| YouTube | Uses `*bold*` not `**bold**` | Yes |
| YouTube | First 100-160 chars visible before "Show more" | Yes |
| LinkedIn | Links in post = algorithm penalty | Yes (puts in first comment) |
| Facebook | 2 link posts/month limit | Yes (links in comments) |
| Twitter | Emojis count as 2 characters | Yes |
| Twitter | URLs always count as 23 chars | Yes |

No more reformatting. Write once, publish correctly.

### 5. Voice Preservation System

**What it is:** Your personal writing style guide informs all generated content.

**Why it matters:** AI content often sounds generic. TubeFlow uses:
- `writing-style.md` - Your tone, phrases, sentence patterns
- `channel-overview.md` - Your brand values and content pillars

**Result:** Content sounds like you, not AI.

### 6. Open-Source Attribution Engine

**What it is:** Automatically researches and credits open-source projects.

**Why it matters:** Technical creators often feature open-source tools. TubeFlow:
- Finds maintainer/developer names
- Discovers FUNDING.yml, GitHub Sponsors, Open Collective
- Generates genuine thank-you messages
- Includes support links for viewers

**Example output:**
```
A huge thanks to the Nextcloud team for building this incredible
self-hosted cloud platform. If you find it useful, consider
supporting the project: https://nextcloud.com/contribute/
```

### 7. Community-Driven Roadmap

**What it is:** GitHub Issues integration for audience video voting.

**Why it matters:** Let your community decide what you make next:
- `/youtube sync` creates roadmap issues
- Viewers vote with thumbs up
- Publishing auto-closes the issue
- Full transparency on upcoming content

### 8. Cross-Platform Installation

**What it is:** Native installers for every major platform.

| Platform | Installer | Status |
|----------|-----------|--------|
| macOS (Intel/Apple Silicon) | `./install.sh` | Full support |
| Linux (Ubuntu/Debian/Fedora/Arch) | `./install.sh` | Full support |
| Windows 10/11 | `.\install.ps1` | Full support |
| WSL2 | `./install.sh` | Full support |

Interactive wizard handles prerequisites, configuration, and template processing.

---

## Market Position

### What Exists Today (January 2026)

| Category | Tools | Limitation |
|----------|-------|------------|
| **YouTube Automation** | ShortGPT, text2youtube, youtube-automation-agent | No Claude Code integration, focused on shorts/TikTok |
| **Claude Code Plugins** | 2,487 repos indexed | None with full YouTube pipeline |
| **Content Ideation** | Kenny Liao's plugin | Ideation only, no production workflow |
| **Template Systems** | Various | No research, no formatting intelligence |

### TubeFlow's Niche

**Technical content creators** who:
- Use Claude Code for development
- Create tutorials, reviews, or educational content
- Value research-backed content over viral trends
- Want to maintain consistent voice and brand
- Feature open-source projects

### Not For

- Short-form content (TikTok, YouTube Shorts)
- Entertainment/vlog content
- Teams needing collaboration features
- Non-technical workflows

---

## By the Numbers

| Metric | Value |
|--------|-------|
| **Agents** | 9 specialized AI agents |
| **Commands** | 3 slash commands |
| **Skills** | 3 workflow skills |
| **Templates** | 8 content templates |
| **Scripts** | 5 Python utilities |
| **Platforms** | 4 (YouTube + LinkedIn + Twitter + Facebook) |
| **Research agents (parallel)** | 4 + 1 strategist |
| **Total files** | 46 |
| **License** | MIT (fully open-source) |

---

## Author

### Simon

TubeFlow was created by **Simon**, a self-hosting enthusiast and content creator focused on making complex technical topics accessible to everyone.

Simon runs the **@webnestify** YouTube channel, where he creates tutorials on Docker, self-hosting, home labs, and cloud infrastructure. TubeFlow was born from his own production workflow, refined over years of creating technical content.

**YouTube:** [@webnestify](https://youtube.com/@webnestify)

**Featured Content:**
- [The Definitive Self-Hosting Guide](https://youtube.com/watch?v=tTyq9xGy1pM) - Comprehensive guide to self-hosting

---

## About Webnestify

```
██╗    ██╗███████╗██████╗ ███╗   ██╗███████╗███████╗████████╗██╗███████╗██╗   ██╗
██║    ██║██╔════╝██╔══██╗████╗  ██║██╔════╝██╔════╝╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝██╔██╗ ██║█████╗  ███████╗   ██║   ██║█████╗   ╚████╔╝
██║███╗██║██╔══╝  ██╔══██╗██║╚██╗██║██╔══╝  ╚════██║   ██║   ██║██╔══╝    ╚██╔╝
╚███╔███╔╝███████╗██████╔╝██║ ╚████║███████╗███████║   ██║   ██║██║        ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝        ╚═╝
```

**Webnestify** is a cloud solutions company established in **Slovakia in 2021**.

> *"We're here to ensure your company doesn't just keep up with the digital age but thrives in it."*

Webnestify is more than a cloud solutions provider. We're your strategic partner in digital transformation. Businesses of all sizes deserve the best technology.

### What We Do

- **Self-Hosting Solutions** - Docker, Kubernetes, home lab setups
- **Cloud Infrastructure** - Architecture, deployment, optimization
- **Technical Education** - YouTube tutorials, guides, documentation
- **Open-Source Advocacy** - Supporting and promoting open-source projects

### Connect With Webnestify

| Platform | Link |
|----------|------|
| **Website** | [webnestify.cloud](https://webnestify.cloud) |
| **YouTube** | [@webnestify](https://youtube.com/@webnestify) |
| **Discord** | [wnstify.cc/discord](https://wnstify.cc/discord) |
| **GitHub** | [github.com/wnstify](https://github.com/wnstify) |
| **LinkedIn** | [linkedin.com/company/webnestify](https://linkedin.com/company/webnestify) |
| **Twitter** | [twitter.com/webnestify](https://twitter.com/webnestify) |
| **Facebook** | [facebook.com/webnestify.cloud](https://facebook.com/webnestify.cloud) |
| **Trustpilot** | [Reviews](https://www.trustpilot.com/review/webnestify.cloud) |

### GitHub Repositories

| Repository | Description |
|------------|-------------|
| [wnstify/tubeflow](https://github.com/wnstify/tubeflow) | This project - YouTube content pipeline |
| [wnstify/wn-youtube](https://github.com/wnstify/wn-youtube) | Video roadmap and community voting |
| [wnstify/docker](https://github.com/wnstify/docker) | Docker Compose files from tutorials |

### Work With Us

- **Business Inquiries:** [webnestify.cloud/contact](https://webnestify.cloud/contact)
- **Apply for Services:** [webnestify.cloud/webnestify-application](https://webnestify.cloud/webnestify-application/)

---

## Contributing

Contributions welcome! See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for:

- Bug reports and feature requests
- Pull request guidelines
- Code style and testing
- Development setup

```bash
# Fork and clone
git clone https://github.com/yourusername/tubeflow.git
git checkout -b feature/your-feature

# Make changes and submit PR
```

---

## License

TubeFlow is open-source software licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- **Claude Code** by Anthropic - AI-powered development
- **Open-Source Community** - Standing on the shoulders of giants
- **Content Creators** - Inspiration from real production workflows

---

## Support

- **Issues**: [GitHub Issues](https://github.com/wnstify/tubeflow/issues)
- **Discussions**: [GitHub Discussions](https://github.com/wnstify/tubeflow/discussions)
- **Discord**: [wnstify.cc/discord](https://wnstify.cc/discord)
- **Documentation**: [docs/](docs/)

---

*Built with care for content creators who value quality over quantity.*

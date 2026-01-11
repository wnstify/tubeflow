# Getting Started with TubeFlow

This guide walks you through installing TubeFlow and creating your first video content package.

---

## Prerequisites

Before installing TubeFlow, ensure you have the following:

### Required

| Requirement | Version | How to Check | Installation |
|-------------|---------|--------------|--------------|
| Claude Code CLI | Latest (2026) | `claude --version` | [Install Guide](https://docs.anthropic.com/claude-code) |
| Python | 3.10+ (3.14 recommended) | `python3 --version` or `python --version` | [python.org](https://python.org) |
| pip | Latest | `pip3 --version` or `python -m pip --version` | Included with Python |
| Git | 2.40+ | `git --version` | [git-scm.com](https://git-scm.com) |
| PyYAML | 6.0+ | Auto-installed by installer | `pip install pyyaml` |

### Platform Support

| Platform | Status | Installer |
|----------|--------|-----------|
| macOS (Intel/Apple Silicon) | Fully supported | `./install.sh` |
| Linux (Ubuntu/Debian/Fedora/Arch) | Fully supported | `./install.sh` |
| Windows 10/11 | Fully supported | `.\install.ps1` |
| WSL2 | Fully supported | `./install.sh` |

### Optional (for full functionality)

| Requirement | Purpose | Needed For |
|-------------|---------|------------|
| yt-dlp | Fetch video metadata | `/youtube publish` command |
| YouTube Channel | Publishing features | `/youtube publish` command |
| GitHub Account | Sync & voting features | `public_repo_sync` feature |
| MCP Servers | Enhanced research | Perplexity, Context7 integrations |

### Verify Prerequisites

**macOS / Linux / WSL2:**
```bash
python3 --version && pip3 --version && git --version && claude --version
```

**Windows (PowerShell):**
```powershell
python --version; pip --version; git --version; claude --version
```

Expected output should show versions for all four tools.

---

## Installation

### macOS / Linux / WSL2

```bash
# Clone the repository
git clone https://github.com/your-org/tubeflow.git
cd tubeflow

# Make installer executable (if needed)
chmod +x install.sh

# Run interactive installer
./install.sh
```

### Windows (PowerShell)

```powershell
# Clone the repository
git clone https://github.com/your-org/tubeflow.git
cd tubeflow

# Run interactive installer
.\install.ps1
```

**Note**: If you see an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### What the Installer Does

1. Checks all prerequisites with version validation
2. Prompts for your channel details
3. Generates `config.yaml` from your answers
4. Processes templates with your configuration
5. Creates voice files (writing-style.md, channel-overview.md)

### Manual Setup (All Platforms)

If the installer fails or you prefer manual control:

**macOS / Linux:**
```bash
# 1. Clone the repository
git clone https://github.com/your-org/tubeflow.git
cd tubeflow

# 2. Copy example config
cp config.example.yaml config.yaml

# 3. Edit config.yaml with your details
# See CONFIGURATION.md for all options

# 4. Process templates
python3 .claude/scripts/process_templates.py config.yaml .

# 5. Copy to your vault
cp -r .claude/ /path/to/your-vault/.claude/
cp -r templates/ /path/to/your-vault/05-Templates/

# 6. Create required directories
mkdir -p /path/to/your-vault/03-YouTube/{ideas,drafts,published,research}
mkdir -p /path/to/your-vault/04-Social/{linkedin,twitter,facebook}
```

**Windows (PowerShell):**
```powershell
# 1. Clone the repository
git clone https://github.com/your-org/tubeflow.git
cd tubeflow

# 2. Copy example config
Copy-Item config.example.yaml config.yaml

# 3. Edit config.yaml with your details

# 4. Process templates
python .claude\scripts\process_templates.py config.yaml .

# 5. Copy to your vault
Copy-Item -Recurse .claude\ C:\path\to\your-vault\.claude\
Copy-Item -Recurse templates\ C:\path\to\your-vault\05-Templates\

# 6. Create required directories
New-Item -ItemType Directory -Path C:\path\to\your-vault\03-YouTube\ideas, C:\path\to\your-vault\03-YouTube\drafts, C:\path\to\your-vault\03-YouTube\published, C:\path\to\your-vault\03-YouTube\research -Force
New-Item -ItemType Directory -Path C:\path\to\your-vault\04-Social\linkedin, C:\path\to\your-vault\04-Social\twitter, C:\path\to\your-vault\04-Social\facebook -Force
```

---

## Configuration

After installation, edit `config.yaml` with your channel details:

```yaml
channel:
  name: "Your Channel Name"
  handle: "@yourchannel"
  tagline: "Your channel tagline"
  niche: "self-hosting"  # or: programming, gaming, devops, etc.

links:
  discord: "https://discord.gg/your-server"
  business: "https://yoursite.com/contact"
  github_org: "https://github.com/yourorg"
```

See [CONFIGURATION.md](CONFIGURATION.md) for the complete configuration reference.

---

## First Video Workflow

Let's create your first video content package to verify everything works.

### Step 1: Capture an Idea

Open Claude Code in your vault directory and run:

```bash
/youtube idea "Test Topic"
```

**What happens:**
- Creates a file at `{{YOUTUBE_ROOT}}/ideas/YYYY-MM-DD-test-topic.md`
- Pre-fills with idea template
- Adds `#status/idea` tag

**Check the output:**

```bash
cat 03-YouTube/ideas/$(date +%Y-%m-%d)-test-topic.md
```

You should see:
```markdown
---
title: Test Topic
status: idea
created: 2024-01-15
tags:
  - status/idea
  - platform/youtube
---

# Test Topic

## Concept
[Initial concept captured here]

## Target Audience
[Who this video is for]

## Key Points
- Point 1
- Point 2
- Point 3

## Notes
[Additional thoughts]
```

### Step 2: Create Full Package

Now create the complete video production package:

```bash
/youtube full "Test Topic"
```

**What happens:**
- Researches the topic (if research agents enabled)
- Creates a folder at `{{YOUTUBE_ROOT}}/drafts/test-topic/`
- Generates 4 files in your voice

**Review generated files:**

```
03-YouTube/drafts/test-topic/
├── script.md              # Full video script with timestamps
├── description.md         # YouTube description (YouTube formatting)
├── thumbnail-text.md      # Thumbnail text suggestions
└── pinned-comment.md      # Engagement comment with links
```

### Step 3: Review Each File

**script.md** contains:
- Hook (first 30 seconds)
- Main content sections
- Timestamp markers
- Call-to-action
- Outro

**description.md** contains:
- Above-the-fold summary (first 100-160 chars)
- Full description with YouTube formatting
- Timestamps (copy from script)
- All your configured links
- About section (if enabled)

**thumbnail-text.md** contains:
- BOLD text (3-5 words)
- Description text (13-18 words)
- Multiple options to choose from

**pinned-comment.md** contains:
- Engagement question or call-to-action
- Links to Discord, voting repo, etc.

### Step 4: After Filming

Once you've filmed and uploaded the video:

```bash
/youtube publish "Test Topic"
```

**What happens:**
- Prompts for YouTube video URL
- Moves draft to `{{YOUTUBE_ROOT}}/published/YYYY/test-topic/`
- Creates `video.md` with YouTube metadata
- Creates `social-content.json` for social posts
- Updates `youtube-index.json`
- (Optional) Syncs to public GitHub repo

---

## Directory Structure

After installation, your vault will have this structure:

```
your-vault/
├── {{YOUTUBE_ROOT}}/              # Default: 03-YouTube
│   ├── ideas/                     # Video ideas (#status/idea)
│   │   └── YYYY-MM-DD-topic.md
│   ├── drafts/                    # Active production (#status/draft)
│   │   └── topic-slug/
│   │       ├── script.md
│   │       ├── description.md
│   │       ├── thumbnail-text.md
│   │       └── pinned-comment.md
│   ├── published/                 # Completed videos (#status/published)
│   │   └── YYYY/
│   │       └── topic-slug/
│   │           ├── video.md       # YouTube metadata
│   │           ├── script.md
│   │           ├── description.md
│   │           ├── thumbnail-text.md
│   │           ├── pinned-comment.md
│   │           └── social-content.json
│   ├── research/                  # Research packs from /youtube research
│   │   └── YYYY-MM-DD-topic/
│   │       ├── research-pack.md
│   │       ├── series-structure.md
│   │       ├── summaries/
│   │       └── raw/
│   ├── channel-overview.md        # Your brand guide
│   └── youtube-index.json         # Master video index
│
├── {{SOCIAL_ROOT}}/               # Default: 04-Social
│   ├── linkedin/
│   │   └── YYYY-MM-DD-topic.md
│   ├── twitter/
│   │   └── YYYY-MM-DD-topic.md
│   ├── facebook/
│   │   └── YYYY-MM-DD-topic.md
│   ├── cross-post/                # Multi-platform campaigns
│   └── social-index.json          # Master social index
│
├── {{TEMPLATES_ROOT}}/            # Default: 05-Templates
│   ├── youtube-formatting-reference.md
│   ├── social-formatting-reference.md
│   ├── youtube-description-template.md
│   └── youtube-pinned-comment-template.md
│
├── writing-style.md               # Your voice guide
│
└── .claude/
    ├── agents/                    # AI agent definitions
    │   ├── yt-topic-gatherer.md
    │   ├── yt-competitor-gatherer.md
    │   ├── yt-seo-gatherer.md
    │   ├── yt-community-gatherer.md
    │   └── yt-research-strategist.md
    ├── commands/                  # Slash commands
    │   ├── youtube.md
    │   └── social.md
    └── skills/                    # Reusable workflows
        ├── youtube-workflow/
        ├── youtube-research/
        └── social-workflow/
```

---

## Troubleshooting

### Agent Not Found

**Symptom:** Error message "Agent @yt-topic-gatherer not found"

**Causes:**
1. `.claude/agents/` directory missing or empty
2. Agent files not copied during installation

**Solution:**
```bash
# Check if agents exist
ls -la /path/to/your-vault/.claude/agents/

# If empty, copy from TubeFlow
cp -r /path/to/tubeflow/.claude/agents/* /path/to/your-vault/.claude/agents/
```

### Variable Not Replaced

**Symptom:** Output contains `{{YOUTUBE_ROOT}}` instead of actual path

**Causes:**
1. `config.yaml` not found
2. Variable not defined in config

**Solution:**
```bash
# Verify config exists
cat /path/to/your-vault/config.yaml

# Check for the variable
grep "youtube_root" /path/to/your-vault/config.yaml
```

Ensure your `config.yaml` has:
```yaml
structure:
  youtube_root: "03-YouTube"  # Your actual folder name
```

### Permission Errors

**Symptom:** "Permission denied" when running commands

**Causes:**
1. Install script not executable
2. Vault directory not writable

**Solution:**
```bash
# Make install script executable
chmod +x install.sh

# Check vault permissions
ls -la /path/to/your-vault/

# Fix permissions if needed
chmod -R u+rw /path/to/your-vault/
```

### MCP Servers Not Configured

**Symptom:** Research features fail or timeout

**Causes:**
1. MCP servers not installed
2. API keys not configured

**Solution:**

Research features work best with MCP servers but are optional. To enable:

1. Install Perplexity MCP server:
```bash
# Add to claude_desktop_config.json
{
  "mcpServers": {
    "perplexity": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-perplexity"],
      "env": {
        "PERPLEXITY_API_KEY": "your-key-here"
      }
    }
  }
}
```

2. Restart Claude Code

Without MCP servers, TubeFlow falls back to web search via the WebSearch tool.

### Command Not Recognized

**Symptom:** `/youtube` command not found

**Causes:**
1. Commands directory not set up
2. CLAUDE.md not configured

**Solution:**

Ensure your vault's CLAUDE.md or `.claude/commands/` includes the youtube command:

```bash
# Check for command file
cat /path/to/your-vault/.claude/commands/youtube.md

# If missing, copy from TubeFlow
cp /path/to/tubeflow/.claude/commands/youtube.md /path/to/your-vault/.claude/commands/
```

### Research Takes Too Long

**Symptom:** `/youtube research` runs for 10+ minutes

**Causes:**
1. Sequential research instead of parallel
2. Network issues
3. API rate limits

**Solution:**

Check your `config.yaml`:
```yaml
advanced:
  parallel_research: true  # Should be true
```

If still slow, check network connectivity and API status.

---

## Next Steps

1. **Read [CONFIGURATION.md](CONFIGURATION.md)** for detailed configuration options
2. **Create your writing style guide** to ensure consistent voice
3. **Set up your channel overview** to define brand guidelines
4. **Try `/youtube research "Topic"`** for comprehensive topic analysis
5. **Enable social media** with `/social` commands

---

## Getting Help

- **GitHub Issues:** Report bugs or request features
- **Discussions:** Ask questions and share tips
- **Documentation:** Check the `/docs` folder for detailed guides

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `/youtube idea "Topic"` | Capture quick idea |
| `/youtube full "Topic"` | Create complete draft package |
| `/youtube research "Topic"` | Deep research before content |
| `/youtube publish "Topic"` | Move to published after upload |
| `/social linkedin "Topic"` | Create LinkedIn post |
| `/social twitter "Topic"` | Create Twitter post/thread |
| `/social facebook "Topic"` | Create Facebook post |
| `/social all "Topic"` | Create for all platforms |
| `/social video "slug"` | Create social from published video |

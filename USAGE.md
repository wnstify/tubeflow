# TubeFlow Usage Guide

Complete guide to using TubeFlow for YouTube content creation and social media posting.

---

## Table of Contents

- [Quick Reference](#quick-reference)
- [YouTube Workflow](#youtube-workflow)
  - [Idea Capture](#idea-capture)
  - [Full Draft Package](#full-draft-package)
  - [Publishing](#publishing)
  - [Syncing to Public Repo](#syncing-to-public-repo)
- [Research Workflow](#research-workflow)
- [Social Media Workflow](#social-media-workflow)
- [Complete Pipeline Example](#complete-pipeline-example)
- [Tips and Best Practices](#tips-and-best-practices)
- [Troubleshooting](#troubleshooting)

---

## Quick Reference

### YouTube Commands

```bash
/youtube idea "Topic"           # Quick idea capture
/youtube full "Topic"           # Complete draft (script + description + thumbnail + comment)
/youtube publish "Topic"        # Move to published after filming
/youtube sync                   # Sync all to public GitHub repo
```

### Research Commands

```bash
/youtube-research "Topic"       # Deep 5-agent research (5-8 minutes)
```

### Social Commands

```bash
/social linkedin "Topic"        # LinkedIn post
/social twitter "Topic"         # Twitter/X post or thread
/social facebook "Topic"        # Facebook post
/social all "Topic"             # All three platforms
/social video "topic-slug"      # Generate from published video
```

---

## YouTube Workflow

### Idea Capture

**Command:** `/youtube idea "Topic"`

Quickly capture a video idea for later development.

**Example:**
```bash
/youtube idea "Docker Security Best Practices"
```

**Output:** `{{YOUTUBE_ROOT}}/ideas/2026-01-11-docker-security-best-practices.md`

**Generated Content:**
```markdown
---
title: "Docker Security Best Practices"
date: 2026-01-11
status: idea
platform: youtube
type: tutorial
---

# Docker Security Best Practices

## Hook
[Attention-grabbing opening]

## Core Problem
[What pain point does this solve?]

## Solution Preview
[What will viewers learn?]

## Target Audience
[Who needs this?]

## Key Points
1. [Point 1]
2. [Point 2]
3. [Point 3]

## Estimated Duration
[X minutes]
```

**When to Use:**
- Quick brainstorming sessions
- Capturing ideas before they're lost
- Building a content backlog

---

### Full Draft Package

**Command:** `/youtube full "Topic"`

Creates a complete draft package ready for filming.

**Example:**
```bash
/youtube full "Docker Security Best Practices"
```

**Output Directory:** `{{YOUTUBE_ROOT}}/drafts/2026-01-11-docker-security-best-practices/`

**Generated Files:**

| File | Purpose |
|------|---------|
| `script.md` | Full video script with [Visual:] cues |
| `description.md` | YouTube description (YouTube formatting) |
| `thumbnail-text.md` | BOLD text + description for thumbnail |
| `pinned-comment.md` | Engagement comment (YouTube formatting) |

**Script Structure:**
```markdown
---
title: "Docker Security Best Practices"
date: 2026-01-11
status: draft
estimated_duration: "15:00"
---

# Docker Security Best Practices

## Hook (0:00-0:30)
[Pattern interrupt or question that grabs attention]

[Visual: Opening visual]

## Introduction (0:30-1:30)
[Who you are, what they'll learn]

## Section 1: [Title] (1:30-5:00)
[Content with practical examples]

[Visual: Screen recording]

**Key point**: [Important takeaway]

## Section 2: [Title] (5:00-10:00)
[More content]

[Visual: Diagram or demonstration]

**Pro tip**: [Practical advice]

## Recap (10:00-12:00)
1. [Takeaway 1]
2. [Takeaway 2]
3. [Takeaway 3]

## CTA & Outro (12:00-end)
[Subscribe, comment, like]
[Tease next video]

---

## Thumbnail Text

**BOLD TEXT (3-5 words):**
SECURE YOUR CONTAINERS

**Description (13-18 words):**
Learn the essential Docker security practices that protect your containers from common vulnerabilities and attacks.
```

**Description Structure:**
- Hook (100-160 chars visible before "Show more")
- Timestamps section
- Official links (for tool/app videos)
- Open-source acknowledgment
- Support options
- Related videos
- Standard channel links
- About section
- Hashtags

**What Happens After `/youtube full`:**

1. Reads your writing style guide
2. Checks youtube-index.json for existing coverage
3. Researches official links (for tools/apps)
4. Finds FUNDING.yml and sponsor links
5. Creates all 4 files
6. Asks if video is uploaded (can auto-run publish)

---

### Publishing

**Command:** `/youtube publish "Topic"`

After filming and uploading to YouTube, this command verifies the upload and moves files to published.

**Example:**
```bash
/youtube publish "Docker Security Best Practices"
```

**Prerequisites:**
- Video must be uploaded to YouTube
- Draft must exist in `drafts/` folder

**What Happens:**

1. Searches your YouTube channel for the video
2. Fetches metadata via yt-dlp:
   - Video ID
   - Title
   - Upload date
   - Duration
   - Full description
3. Creates `video.md` with metadata
4. Creates `social-content.json` for social workflow
5. Updates `youtube-index.json`
6. Moves all files to `published/YYYY/topic-slug/`

**Output Directory:** `{{YOUTUBE_ROOT}}/published/2026/docker-security-best-practices/`

**Generated Files:**

| File | Content |
|------|---------|
| `video.md` | YouTube metadata (ID, URL, duration) |
| `script.md` | Final script (moved from draft) |
| `description.md` | Final description (moved from draft) |
| `thumbnail-text.md` | Thumbnail text (moved from draft) |
| `pinned-comment.md` | Pinned comment (moved from draft) |
| `social-content.json` | Structured data for social posts |

**social-content.json Structure:**
```json
{
  "video_id": "abc123xyz",
  "title": "Docker Security Best Practices",
  "url": "https://youtube.com/watch?v=abc123xyz",
  "date": "2026-01-11",
  "duration": "15:32",
  "hook": "Your containers might be exposed...",
  "key_points": [
    "Use non-root users",
    "Scan images for vulnerabilities",
    "Implement network policies"
  ],
  "hashtags": ["docker", "security", "devops"]
}
```

---

### Syncing to Public Repo

**Command:** `/youtube sync`

Syncs all published videos to your public GitHub repository.

**Example:**
```bash
/youtube sync
```

**Prerequisites:**
- `voting_repo` configured in config.yaml
- Videos published via `/youtube publish`
- Git configured with push access

**What Happens:**

1. Runs dry-run first (shows what will change)
2. For each unsynced video:
   - Fetches full description via yt-dlp
   - Creates `videos/YYYY/slug/README.md`
3. Updates `VIDEOS.md`:
   - Video count
   - All Videos table
   - Category sections
4. Updates `README.md`:
   - Latest video section
   - Total video count
5. Closes matching roadmap issues
6. Commits with descriptive message
7. Pushes to remote

**Public Repo Structure:**
```
your-youtube-repo/
├── README.md              # Latest video + channel overview
├── VIDEOS.md              # Complete video catalog by category
├── ROADMAP.md             # Upcoming video ideas (with issue links)
└── videos/
    └── 2026/
        └── docker-security-best-practices/
            └── README.md  # Full YouTube description
```

**Automatic Categorization:**

Videos are automatically categorized based on keywords:
- Docker-related → Docker & Containers
- Security-related → Security & Authentication
- Self-hosting → Self-Hosting & Home Lab
- And more...

---

## Research Workflow

**Command:** `/youtube-research "Topic"`

Comprehensive research before content creation using 5 specialized agents.

**Example:**
```bash
/youtube-research "Kubernetes Security"
```

**Timing:** ~5-8 minutes total

**Phase 1: Parallel Research (4 agents, ~2-3 min)**

| Agent | What It Does |
|-------|--------------|
| **Topic Gatherer** | Features, documentation, prerequisites, complexity |
| **Competitor Gatherer** | Existing YouTube videos, view counts, gaps |
| **SEO Gatherer** | Keywords, search volume, trending topics, titles |
| **Community Gatherer** | Reddit threads, forum posts, common questions |

**Phase 2: Strategic Synthesis (1 agent, ~3-5 min)**

| Agent | What It Does |
|-------|--------------|
| **Research Strategist** | Synthesizes findings into actionable recommendations |

**Output Directory:** `{{YOUTUBE_ROOT}}/research/2026-01-11-kubernetes-security/`

**Generated Files:**

```
research/2026-01-11-kubernetes-security/
├── research-pack.md          # Strategic recommendations
├── series-structure.md       # Episode breakdown (if series recommended)
├── summaries/                # Condensed findings (~3,200 tokens)
│   ├── topic-summary.md
│   ├── competitor-summary.md
│   ├── seo-summary.md
│   └── community-summary.md
└── raw/                      # Full research data
    ├── topic-raw.md
    ├── competitor-raw.md
    ├── seo-raw.md
    └── community-raw.md
```

**research-pack.md Contents:**

| Section | Content |
|---------|---------|
| Executive Summary | Key findings + recommendation |
| Topic Overview | Features, complexity, prerequisites |
| Competitor Landscape | Existing videos, gaps, differentiation |
| Target Audience | Who, skill level, goals |
| SEO Strategy | Primary/secondary keywords, title options |
| Community Insights | Top questions, pain points |
| Content Recommendation | Single video or series |
| Production Notes | Demo requirements, difficulty |

**Series Detection:**

The strategist recommends a series when:
- Topic has 3+ distinct sub-topics
- Each needs 10+ minutes
- Clear learning progression exists

**Using Research with Content Creation:**

```bash
# Step 1: Research first
/youtube-research "Kubernetes Security"

# Step 2: Review research-pack.md

# Step 3: Create content informed by research
/youtube full "Kubernetes Security Fundamentals"
```

---

## Social Media Workflow

### Platform-Specific Commands

**LinkedIn:**
```bash
/social linkedin "Topic"
```
- 1,300-1,600 characters optimal
- Professional tone
- Links in first comment (algorithm optimization)
- 3-5 hashtags

**Twitter/X:**
```bash
/social twitter "Topic"
```
- 200-250 characters per tweet optimal
- Punchy, engaging tone
- Thread format for longer content
- 1-2 hashtags in final tweet

**Facebook:**
```bash
/social facebook "Topic"
```
- 40-80 characters for highest engagement
- Community-focused tone
- Links in first comment (2/month limit!)
- 2-3 hashtags

### All Platforms

```bash
/social all "Topic"
```

Creates posts for LinkedIn, Twitter, and Facebook simultaneously using 3 parallel agents.

### From Published Video

```bash
/social video "topic-slug"
```

Generates social posts from a published video's `social-content.json`.

**Example:**
```bash
/social video "docker-security-best-practices"
```

This reads `published/2026/docker-security-best-practices/social-content.json` and creates platform-optimized posts.

**Output:**
```
{{SOCIAL_ROOT}}/
├── linkedin/2026-01-11-docker-security-best-practices.md
├── twitter/2026-01-11-docker-security-best-practices.md
└── facebook/2026-01-11-docker-security-best-practices.md
```

---

## Complete Pipeline Example

Here's a full workflow from idea to social promotion:

### Day 1: Research & Planning

```bash
# Research the topic thoroughly
/youtube-research "WireGuard VPN Setup"
```

Review `research/2026-01-11-wireguard-vpn-setup/research-pack.md` to understand:
- What competitors have covered
- What questions people are asking
- Best keywords and titles

### Day 2: Create Draft

```bash
# Create full content package
/youtube full "WireGuard VPN Setup Guide"
```

Review and edit:
- `drafts/2026-01-11-wireguard-vpn-setup/script.md`
- `drafts/2026-01-11-wireguard-vpn-setup/description.md`
- `drafts/2026-01-11-wireguard-vpn-setup/pinned-comment.md`

### Day 3: Film & Upload

1. Film the video using your script
2. Edit the footage
3. Upload to YouTube
4. Add description (copy from `description.md`)
5. Add pinned comment (copy from `pinned-comment.md`)

### Day 3: Publish & Sync

```bash
# Verify upload and move to published
/youtube publish "WireGuard VPN Setup"

# Sync to public GitHub repo
/youtube sync
```

### Day 4: Social Promotion

```bash
# Create social posts from the published video
/social video "wireguard-vpn-setup"
```

Copy-paste posts to each platform:
- LinkedIn: `social/linkedin/2026-01-11-wireguard-vpn-setup.md`
- Twitter: `social/twitter/2026-01-11-wireguard-vpn-setup.md`
- Facebook: `social/facebook/2026-01-11-wireguard-vpn-setup.md`

---

## Tips and Best Practices

### Voice Consistency

1. **Create a detailed writing style guide**
   - Include phrases you commonly use
   - Define your tone (friendly, professional, casual)
   - List words/phrases to avoid

2. **Update it over time**
   - Add new phrases that work well
   - Remove things that feel off-brand

### Research Efficiency

1. **Use research for complex topics**
   - New technologies you're less familiar with
   - Competitive spaces with many existing videos
   - Topics where SEO matters

2. **Skip research for quick tips**
   - Simple how-tos you know well
   - Opinion/experience-based content
   - Time-sensitive content

### Content Quality

1. **Always include [Visual:] cues**
   - Helps you plan B-roll while scripting
   - Makes filming more efficient

2. **Hook in first 30 seconds**
   - Pattern interrupt
   - Surprising fact
   - Direct question

3. **3 key takeaways in recap**
   - Viewers remember lists
   - Reinforces main points

### Platform Optimization

1. **YouTube descriptions**
   - First 100-160 chars are critical
   - Include primary keyword
   - Put timestamps early

2. **Social media**
   - LinkedIn: Professional value
   - Twitter: Punchy, engaging
   - Facebook: Community-focused

### Sync Strategy

1. **Sync after each video**
   - Keeps public repo updated
   - Closes roadmap issues promptly

2. **Review before pushing**
   - Dry-run shows what will change
   - Verify video metadata is correct

---

## Troubleshooting

### Agent Not Found

**Error:** "Agent youtube-creator not found"

**Solution:**
- Verify `.claude/agents/youtube-creator.md` exists
- Check file has correct frontmatter
- Restart Claude Code session

### Variables Not Replaced

**Error:** Content still shows `{{VARIABLE}}` placeholders

**Solution:**
```bash
# Re-run template processor
python .claude/scripts/process_templates.py config.yaml .
```

### yt-dlp Issues

**Error:** "yt-dlp: command not found"

**Solution:**
```bash
pip install yt-dlp
```

**Error:** "Video not found on channel"

**Solution:**
- Verify video is public (not private/unlisted)
- Wait a few minutes after upload
- Check channel handle in config

### Sync Failures

**Error:** "Failed to push to remote"

**Solution:**
- Verify Git credentials
- Check `voting_repo` URL in config
- Ensure you have push access

### Research Takes Too Long

**Issue:** Research workflow exceeds 10 minutes

**Solutions:**
- Check internet connection
- Verify MCP servers are configured
- Some complex topics naturally take longer

### Command Not Recognized

**Error:** "/youtube: command not found"

**Solution:**
- Verify `.claude/commands/youtube.md` exists
- Check Claude Code is running in correct directory
- Reload Claude Code session

---

## Advanced Usage

### Parallel Video Creation

Create multiple video ideas simultaneously:

```bash
# In your message, request multiple ideas
"Create video ideas for: Docker Security, Kubernetes Basics, and Linux Networking"
```

TubeFlow will spawn 3 parallel agents.

### Custom Categories

Add custom categories in `config.yaml`:

```yaml
categories:
  keywords:
    AI: ["ai", "machine learning", "llm", "gpt"]
    DevOps: ["ci/cd", "pipeline", "jenkins", "github actions"]
```

### Batch Publishing

After uploading multiple videos:

```bash
/youtube publish "Video 1 Title"
/youtube publish "Video 2 Title"
/youtube publish "Video 3 Title"
/youtube sync  # Syncs all at once
```

### Series Planning

After research suggests a series:

```bash
# Research generates series-structure.md
/youtube-research "Docker Mastery"

# Create each episode
/youtube full "Docker Mastery Part 1: Fundamentals"
/youtube full "Docker Mastery Part 2: Networking"
/youtube full "Docker Mastery Part 3: Security"
```

---

*For more information, see [docs/WORKFLOWS.md](docs/WORKFLOWS.md) and [docs/CONFIGURATION.md](docs/CONFIGURATION.md).*

---
name: youtube-workflow
description: Create YouTube video content for {{CHANNEL_HANDLE}} channel including scripts, ideas, descriptions, and manage publishing workflow. Use when user mentions YouTube, video scripts, video ideas, or content creation for the channel.
---

# YouTube Workflow Skill

Complete content creation and publishing workflow for the {{CHANNEL_HANDLE}} YouTube channel.

---

## CRITICAL: Agent Spawning Requirement

**You MUST use the Task tool to spawn specialized agents.** Do NOT handle this workflow directly.

### Agent Routing

| Command | Agent to Spawn |
|---------|----------------|
| `/youtube idea "Topic"` | `@youtube-creator` |
| `/youtube full "Topic"` | `@youtube-creator` |
| `/youtube publish "Topic"` | `@youtube-publisher` |

### How to Execute

**For idea or full:**
```
Task tool:
  subagent_type: "youtube-creator"
  prompt: "[idea/full] Create [content type] about [topic]. Follow youtube-creator agent instructions."
```

**For publish:**
```
Task tool:
  subagent_type: "youtube-publisher"
  prompt: "Publish video about [topic]. Verify upload, move files, create social-content.json, update index."
```

### Parallel Execution for Multiple Ideas

When user provides multiple video ideas, spawn multiple `@youtube-creator` agents in parallel:

```
Example: User wants 3 video ideas captured

Task 1: subagent_type: "youtube-creator" → Idea 1
Task 2: subagent_type: "youtube-creator" → Idea 2
Task 3: subagent_type: "youtube-creator" → Idea 3

All three run concurrently for faster completion.
```

**When to use parallel agents:**
- Multiple video ideas in one request
- Time-sensitive content needing quick turnaround

**When sequential is required:**
- `/youtube full` followed by `/youtube publish` (depends on creation completing)
- Single video workflow

---

## Voice & Brand Integration

**CRITICAL**: All content MUST follow your channel's writing style and brand principles.

### Voice Reference
Read writing-style.md before generating any content:
- Direct, friendly, honest, solution-focused
- Short sentences (5-15 words ideal)
- Start with action, use questions to engage
- Phrases: "Here's the thing...", "Let me show you.", "No fluff. Just what works."
- Strategic emoji usage (not spam)
- Correct grammar always

### Brand Reference
Read 03-YouTube/channel-overview.md for core principles:
- Complete data ownership
- Zero-trust security
- Independence over convenience
- Practitioner credibility ("I use this for my clients")

---

## Content Creation Methodology

### 6-Step Script Process

**Step 1: Structured Outline**
Create roadmap with main sections and estimated timestamps.

**Step 2: Attention-Grabbing Hook (0:00-0:30)**
First 30 seconds must capture attention using:
- Pattern interrupt: Challenge common assumption
- Question hook: Ask something they've wondered
- Result preview: Show the end result first
- Story opening: Brief relatable scenario

**Step 3: Scene-by-Scene Narration**
Write full script following outline. Include:
- Clear section transitions
- Practical examples and demonstrations
- Common mistakes to avoid
- Pro tips throughout

**Step 4: Visual Cues**
Embed `[Visual: description]` cues throughout for B-roll guidance:
```
[Visual: Screen recording of terminal]
[Visual: Diagram showing data flow]
[Visual: Close-up of config file]
```

**Step 5: Call-to-Action & Outro**
End with:
- Recap of key takeaways (3 max)
- Clear CTA (subscribe, comment, like)
- Tease next video or related content

**Step 6: Metadata Package**
Generate: description, hashtags, thumbnail text.

---

## Pacing Guidelines

**~150 words = 1 minute of video**

| Video Length | Word Count | Sections |
|--------------|------------|----------|
| 5 minutes | ~750 words | 3-4 sections |
| 10 minutes | ~1500 words | 5-6 sections |
| 15 minutes | ~2250 words | 7-8 sections |
| 20 minutes | ~3000 words | 8-10 sections |

---

## Featured Video Reference

**CRITICAL**: When video topic relates to self-hosting, ALWAYS reference your featured video.

**Video**: {{FEATURED_VIDEO_URL}}
**Title**: {{FEATURED_VIDEO_TITLE}}

**Topics that require this reference**:
- Self-hosting (explicit)
- Docker, containers, Kubernetes
- Home lab, homelab
- Server setup, VPS
- Pangolin, Authentik, CrowdSec
- Reverse proxy, SSL, tunnels
- Data ownership, privacy
- Infrastructure (self-hosted context)

**Where to include**:
- Description.md: In "Related videos" section
- Pinned-comment.md: At end with "New to self-hosting?" line

---

## Topic Research (For Tool/Application Videos)

**CRITICAL**: When creating content about a specific tool, application, or project, ALWAYS research and include official resources.

### When to Research

Research is REQUIRED when video topic includes:
- Named software tools (Docker, Kubernetes, Restic, Authentik, etc.)
- Named applications (Nextcloud, Immich, Jellyfin, etc.)
- Named services (Cloudflare, Tailscale, etc.)
- Named libraries or frameworks

Research is NOT required for:
- General concepts (CI/CD explained, backup strategies, etc.)
- Built-in features (Linux commands, bash scripting, etc.)
- Opinion/comparison videos without single tool focus
- News/update videos

### Research Outputs

For each tool/application, find and include:

| Item | Required | Notes |
|------|----------|-------|
| Official Website | Yes | Main landing page |
| Documentation | Yes | Official docs site |
| GitHub Repository | Yes (if open-source) | Main repo URL |
| Open-source status | Yes | Check license |
| Developer/Team name | Yes (for acknowledgment) | Who maintains it |
| GitHub Sponsors | If available | Check FUNDING.yml or Sponsors button |
| Open Collective | If available | Search on Open Collective |
| Commercial/SaaS offering | If available | Paid version or hosted offering |

### Acknowledgment Guidelines

For open-source projects, include genuine acknowledgment:
- Name the developers/team specifically
- Mention the specific benefit their work provides
- Keep it authentic (your voice, not corporate)

**Good**: "A huge thank you to the Authentik team for creating and maintaining Authentik as an open-source project. Their work makes enterprise-grade authentication accessible to everyone."

**Bad**: "Thanks to the developers for this software." (too generic)

---

## Thumbnail Text Requirements

Every script includes thumbnail text:

**BOLD TEXT**: 3-5 words (main attention grabber)
- Use caps for emphasis
- Create curiosity or promise result
- Examples: "STOP PAYING FOR THIS", "THE HIDDEN DANGER", "10X FASTER"

**Description**: 13-18 words
- Expand on the bold text
- Include specific benefit or outcome
- Examples: "Learn the exact backup strategy I use to protect my clients' servers from data loss forever"

---

## File Organization

### Ideas
Location: `03-YouTube/ideas/`
Naming: `YYYY-MM-DD-topic-slug.md`
Tags: `#status/idea #platform/youtube`

### Drafts (Active Production)
Location: `03-YouTube/drafts/YYYY-MM-DD-topic-slug/`
Contents:
- `script.md` - Full video script
- `description.md` - YouTube description
- `thumbnail-text.md` - Bold + description text
- `pinned-comment.md` - Pinned comment for engagement
Tags: `#status/draft #platform/youtube`

### Published
Location: `03-YouTube/published/YYYY/topic-slug/`
Contents:
- `video.md` - YouTube metadata (ID, URL, duration, date)
- `script.md` - Final script
- `description.md` - Final description
- `thumbnail-text.md` - Thumbnail text used
- `pinned-comment.md` - Pinned comment used
- `social-content.json` - Structured data for social posts
Tags: `#status/published #platform/youtube`

---

## Templates

For detailed structures, see:
- [[SCRIPT_TEMPLATE]] - Full script structure
- [[IDEA_TEMPLATE]] - Quick idea capture
- [[DESCRIPTION_TEMPLATE]] - SEO-optimized description
- [[PINNED_COMMENT_TEMPLATE]] - Engagement comment

---

## Standard Links (ALWAYS Include)

**Connect**:
- Discord (questions, help): {{DISCORD_URL}}
- Business inquiries: {{BUSINESS_URL}}

**Follow**:
- LinkedIn: {{LINKEDIN_URL}}
- Facebook: {{FACEBOOK_URL}}
- Twitter: {{TWITTER_URL}}

**Reviews**: {{REVIEWS_URL}}

These links go in:
1. **Description.md** - Full links block
2. **Pinned-comment.md** - Abbreviated version

---

## Quality Checklist

Before completing any content:

- [ ] Sounds like your channel voice, not AI
- [ ] Hook grabs attention in first 10 seconds
- [ ] Clear structure with logical flow
- [ ] Practical examples included
- [ ] [Visual:] cues embedded
- [ ] CTA present
- [ ] Grammar and spelling correct
- [ ] Thumbnail text: 3-5 bold words + 13-18 word description
- [ ] Pinned comment created with engagement hook
- [ ] Standard links included in description and pinned comment
- [ ] Featured video referenced (if applicable)
- [ ] **Topic research completed** (for tool/app videos)
- [ ] **Official links included** (website, docs, GitHub)
- [ ] **Open-source acknowledgment** (for open-source projects)
- [ ] **Support options included** (sponsorship, SaaS - when available)
- [ ] Proper file location and naming
- [ ] Correct tags applied

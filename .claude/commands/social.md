---
description: Social media content workflow - create posts for LinkedIn, Twitter/X, Facebook, or all platforms
argument-hint: [platform] [topic]
allowed-tools: Read, Write, Edit, Glob, Grep, Task
---

# /social Command

Create platform-optimized social media content for {{CHANNEL_HANDLE}} brand.

---

## CRITICAL: Agent Spawning Requirement

**You MUST use the Task tool to spawn the `@social-creator` agent.** Do NOT handle this workflow directly.

```
Task tool:
  description: "Create [platform] post"
  subagent_type: "social-creator"
  prompt: "Create [platform] post about [topic]. Follow social-creator agent instructions."
```

### MANDATORY: Parallel Execution for `/social all` and `/social video`

**You MUST spawn 3 agents in parallel when using `/social all` or `/social video`:**

```
Task 1: description: "Create LinkedIn post"
        subagent_type: "social-creator"
        prompt: "Create LinkedIn post about [topic]."

Task 2: description: "Create Twitter thread"
        subagent_type: "social-creator"
        prompt: "Create Twitter thread about [topic]."

Task 3: description: "Create Facebook post"
        subagent_type: "social-creator"
        prompt: "Create Facebook post about [topic]."
```

**This is NOT optional.** Do NOT spawn one agent to handle all three platforms.

---

## Usage

```
/social linkedin "Topic"   - Create LinkedIn post
/social twitter "Topic"    - Create Twitter post/thread
/social facebook "Topic"   - Create Facebook post
/social all "Topic"        - Create for all platforms
/social video "video-slug" - Create all from YouTube video
```

## Arguments Received

- **Platform**: `$1` (linkedin, twitter, facebook, all, video)
- **Topic/Slug**: `$2` (topic or video slug)
- **Full args**: `$ARGUMENTS`

## Routing Logic

### If `$1` = "linkedin"

Spawn ONE `@social-creator` agent via Task tool to:
1. Read style guide
2. Create LinkedIn post (1,300-1,600 chars, 3-5 hashtags)
3. Save to `04-Social/linkedin/YYYY-MM-DD-topic.md`
4. Apply tags: `#status/draft #platform/linkedin`
5. Update `social-index.json`

### If `$1` = "twitter"

Spawn ONE `@social-creator` agent via Task tool to:
1. Read style guide
2. Create single tweet + thread version (1-2 hashtags)
3. Save to `04-Social/twitter/YYYY-MM-DD-topic.md`
4. Apply tags: `#status/draft #platform/twitter`
5. Update `social-index.json`

### If `$1` = "facebook"

Spawn ONE `@social-creator` agent via Task tool to:
1. Read style guide
2. Create Facebook post (40-80 chars optimal, 0-3 hashtags)
3. Save to `04-Social/facebook/YYYY-MM-DD-topic.md`
4. Apply tags: `#status/draft #platform/facebook`
5. Update `social-index.json`

### If `$1` = "all"

**MUST spawn 3 `@social-creator` agents in parallel** (see CRITICAL section above):

```
Task 1: description: "Create LinkedIn post", prompt: "Create LinkedIn post about [topic]..."
Task 2: description: "Create Twitter thread", prompt: "Create Twitter thread about [topic]..."
Task 3: description: "Create Facebook post", prompt: "Create Facebook post about [topic]..."
```

Each agent handles ONE platform:
1. Read style guide
2. Create platform-specific post
3. Save to platform folder
4. Apply tags
5. Update `social-index.json`

After all 3 complete, create cross-post index in `04-Social/cross-post/YYYY-MM-DD-topic.md`

### If `$1` = "video"

First, read video data from `03-YouTube/published/*/$2/social-content.json`.

Then **MUST spawn 3 `@social-creator` agents in parallel**:

```
Task 1: description: "Create LinkedIn video post", prompt: "Create LinkedIn post for video [slug]. Video data: [include social-content.json]"
Task 2: description: "Create Twitter video thread", prompt: "Create Twitter thread for video [slug]. Video data: [include social-content.json]"
Task 3: description: "Create Facebook video post", prompt: "Create Facebook post for video [slug]. Video data: [include social-content.json]"
```

Each agent:
1. Uses video data (title, hook, key_points, video_url)
2. Creates platform-specific post with video link
3. Saves to platform folder
4. Updates `social-index.json` with source: youtube

After all 3 complete, create cross-post index

## Context Files (Always Read First)

1. `writing-style.md` - Voice and tone
2. `03-YouTube/channel-overview.md` - Brand principles
3. `05-Templates/social-formatting-reference.md` - **CRITICAL** platform formatting rules

## Output Locations

| Platform | Location |
|----------|----------|
| LinkedIn | `04-Social/linkedin/YYYY-MM-DD-topic.md` |
| Twitter | `04-Social/twitter/YYYY-MM-DD-topic.md` |
| Facebook | `04-Social/facebook/YYYY-MM-DD-topic.md` |
| Cross-post | `04-Social/cross-post/YYYY-MM-DD-topic.md` |
| Index | `04-Social/social-index.json` |

## Examples

```
/social linkedin "Zero Trust Security"
→ Creates: 04-Social/linkedin/2026-01-10-zero-trust-security.md
→ Updates: social-index.json

/social twitter "Docker Tips"
→ Creates: 04-Social/twitter/2026-01-10-docker-tips.md
  (includes single tweet + thread version)
→ Updates: social-index.json

/social facebook "Backup Reminder"
→ Creates: 04-Social/facebook/2026-01-10-backup-reminder.md
→ Updates: social-index.json

/social all "Kubernetes Security"
→ Creates: 04-Social/linkedin/2026-01-10-kubernetes-security.md
→ Creates: 04-Social/twitter/2026-01-10-kubernetes-security.md
→ Creates: 04-Social/facebook/2026-01-10-kubernetes-security.md
→ Creates: 04-Social/cross-post/2026-01-10-kubernetes-security.md
→ Updates: social-index.json

/social video "docker-backup-strategies"
→ Reads: 03-YouTube/published/2026/docker-backup-strategies/social-content.json
→ Creates: All platform posts + cross-post index
→ Updates: social-index.json with source: youtube
```

## Platform Specs Quick Reference

| Platform | Length | Hashtags | Tone |
|----------|--------|----------|------|
| LinkedIn | 1,300-1,600 chars | 3-5 | Professional |
| Twitter | 200-250 chars/tweet | 1-2 | Punchy |
| Facebook | 40-80 chars | 2-3 | Community |

---

## CRITICAL: Content Rules

### No Harsh Language

**AVOID these words:**

| Don't Say | Say Instead |
|-----------|-------------|
| "is dead" | "is no longer actively maintained" |
| "killed it" | "development has slowed" |
| "abandoned" | "seeking new maintainers" |
| "defunct" | "development paused" |

**Be respectful of open-source maintainers.**

### No Double Dashes or Em Dashes

**NEVER use:** `--`, `—`, or `–`

These sound AI-generated. Use periods or commas instead.

---

## CRITICAL: Platform Formatting Rules

### LinkedIn

**Does NOT support Markdown.** No native bold/italic.

| Rule | Detail |
|------|--------|
| Links | **Put in FIRST COMMENT** (algorithm penalizes) |
| Above fold | First 140-210 chars visible |
| Hashtags | 3-5 at end, #CamelCase |
| Paragraphs | Short (1-3 sentences) |

### Facebook

**Does NOT support Markdown.** No native bold/italic for Pages.

| Rule | Detail |
|------|--------|
| Links | **Put in FIRST COMMENT** (2/month limit in posts!) |
| Above fold | First 125 chars visible on mobile |
| Optimal length | **40-80 chars** for 66% higher engagement |
| Hashtags | 2-3 maximum, no special chars |

### Twitter/X

**HAS native bold/italic buttons.** Highlight text and click B or I.

| Rule | Detail |
|------|--------|
| Emojis | **Count as 2 chars each** |
| URLs | Always count as 23 chars |
| Hashtags | 1-2 in final tweet only, #CamelCase |
| Thread format | Numbered (1/, 2/, etc.), 5-15 tweets |
| Tweet length | 200-250 chars optimal |

### Link Formats (All Platforms)

| Platform | USE | NOT |
|----------|-----|-----|
| Twitter | `twitter.com` | ~~`x.com`~~ |
| Facebook | `facebook.com` | `fb.com` |
| All | Include `https://` | Skip protocol |

See `05-Templates/social-formatting-reference.md` for complete specification.

---

## Quality Standards

All content must:
- Sound like your channel voice (see `writing-style.md`)
- Follow platform-specific specs
- Include appropriate CTA
- Have correct grammar
- Use proper file naming and tags

## Integration with YouTube Workflow

After publishing a YouTube video:
```
/youtube publish "Docker Basics"
→ Creates: social-content.json

/social video "docker-basics"
→ Creates: All social posts from video content
```

---

## Validation Checklist

Before completing any `/social` command:

**Content Rules:**
- [ ] NO harsh language ("dead", "abandoned", "defunct")
- [ ] NO double dashes (--) or em dashes (—)
- [ ] Sounds like your channel voice, not AI
- [ ] Grammar correct

**LinkedIn Formatting:**
- [ ] Links in FIRST COMMENT (not main post)
- [ ] First 140-210 chars contain hook
- [ ] 3-5 hashtags at end
- [ ] Short paragraphs (1-3 sentences)

**Facebook Formatting:**
- [ ] Links in FIRST COMMENT (2/month limit!)
- [ ] Optimal 40-80 chars (or up to 150)
- [ ] 2-3 hashtags maximum
- [ ] Question to drive engagement

**Twitter/X Formatting:**
- [ ] 200-250 chars per tweet (not 280)
- [ ] Thread numbered (1/, 2/, etc.)
- [ ] 1-2 hashtags in final tweet only
- [ ] Emojis counted (2 chars each)
- [ ] #CamelCase for accessibility

**All Platforms:**
- [ ] Twitter links use `twitter.com` NOT `x.com`
- [ ] Facebook links use `facebook.com` NOT `fb.com`
- [ ] All links include `https://`
- [ ] Standard links in first comment/final tweet

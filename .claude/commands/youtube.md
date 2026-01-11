---
description: YouTube content workflow for {{CHANNEL_HANDLE}} channel - create ideas, scripts, descriptions, and manage publishing workflow
argument-hint: [type] [topic]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion, Task
---

# /youtube Command

Create and manage YouTube content for the {{CHANNEL_HANDLE}} channel.

---

## CRITICAL: Agent Spawning Requirement

**You MUST use the Task tool to spawn specialized agents.** Do NOT handle this workflow directly.

| Command | Agent | Task Tool Usage |
|---------|-------|-----------------|
| `idea` | `@youtube-creator` | `subagent_type: "youtube-creator"` |
| `full` | `@youtube-creator` | `subagent_type: "youtube-creator"` |
| `publish` | `@youtube-publisher` | `subagent_type: "youtube-publisher"` |
| `sync` | `@youtube-syncer` | `subagent_type: "youtube-syncer"` |

### Example Task Calls

**For idea/full:**
```
Task tool:
  description: "Create YouTube [idea/full]"
  subagent_type: "youtube-creator"
  prompt: "Create [idea/full package] about [topic]. Follow youtube-creator agent instructions."
```

**For publish:**
```
Task tool:
  description: "Publish YouTube video"
  subagent_type: "youtube-publisher"
  prompt: "Publish video about [topic]. Verify upload, move files, update index."
```

**For sync:**
```
Task tool:
  description: "Sync videos to public repo"
  subagent_type: "youtube-syncer"
  prompt: "Sync published videos to YouTube repository. Run sync script, commit, and push."
```

### Parallel Execution for Multiple Ideas

When user provides multiple video ideas, spawn agents in parallel:

```
Task 1: description: "Create idea 1", subagent_type: "youtube-creator", prompt: "..."
Task 2: description: "Create idea 2", subagent_type: "youtube-creator", prompt: "..."
Task 3: description: "Create idea 3", subagent_type: "youtube-creator", prompt: "..."
```

---

## Usage

```
/youtube idea "Topic"      - Quick idea capture
/youtube full "Topic"      - Complete draft package (script + description + thumbnail text)
/youtube publish "Topic"   - Move draft to published after upload
/youtube sync              - Sync published videos to public repo
```

## Arguments Received

- **Type**: `$1` (idea, full, publish, or sync)
- **Topic**: `$2` (video topic/title)
- **Full args**: `$ARGUMENTS`

## Routing Logic

**Remember**: Use Task tool to spawn agents (see CRITICAL section above).

### If `$1` = "idea"

Spawn `@youtube-creator` agent via Task tool to:
1. Create quick idea capture
2. Save to `03-YouTube/ideas/YYYY-MM-DD-topic-slug.md`
3. Apply tags: `#status/idea #platform/youtube`

### If `$1` = "full"

Spawn `@youtube-creator` agent via Task tool to:
1. Read style guide, channel overview, and **formatting reference**
2. Check youtube-index.json for existing coverage
3. Create complete draft package in `03-YouTube/drafts/YYYY-MM-DD-topic-slug/`:
   - `script.md` - Full video script with timestamps and [Visual:] cues
   - `description.md` - YouTube description **(YOUTUBE FORMATTING ONLY)**
   - `thumbnail-text.md` - BOLD text (3-5 words) + description (13-18 words)
   - `pinned-comment.md` - Engagement comment **(YOUTUBE FORMATTING ONLY)**
4. **Validate YouTube formatting** before saving
5. Apply tags: `#status/draft #platform/youtube`

After creation, ask user:
```
Draft package created in: 03-YouTube/drafts/YYYY-MM-DD-topic-slug/

Has this video been uploaded to YouTube?
- Yes, it's live → Run publish workflow
- No, I'll upload later → Keep in drafts
```

If "Yes": Spawn `@youtube-publisher` agent via Task tool.

### If `$1` = "publish"

Spawn `@youtube-publisher` agent via Task tool to:
1. Verify video is live on YouTube channel (via yt-dlp)
2. Fetch metadata: video ID, actual title, upload date, duration
3. Create published folder: `03-YouTube/published/YYYY/topic-slug/`
4. Move all draft files to published folder
5. Create `video.md` with YouTube metadata
6. Create `social-content.json` for social media workflow
7. Update `youtube-index.json`
8. Update tags to `#status/published`
9. Delete empty draft folder

### If `$1` = "sync"

Spawn `@youtube-syncer` agent via Task tool to:
1. Run sync_videos.py in YouTube repo (dry-run first)
2. Create README files for new videos in `videos/{year}/{slug}/`
3. Update VIDEOS.md (All Videos table + category sections)
4. Close matching roadmap issues automatically
5. Git commit with descriptive message (no AI mentions)
6. Push to remote

No topic argument needed. Syncs all unsynced videos from youtube-index.json.

## Context Files (Always Read First)

1. `writing-style.md` - Voice and tone
2. `03-YouTube/channel-overview.md` - Brand principles
3. `03-YouTube/youtube-index.json` - Existing videos
4. `05-Templates/youtube-formatting-reference.md` - **CRITICAL formatting rules**

## Output Locations

| Type | Location |
|------|----------|
| Ideas | `03-YouTube/ideas/YYYY-MM-DD-topic.md` |
| Drafts | `03-YouTube/drafts/YYYY-MM-DD-topic/` |
| Published | `03-YouTube/published/YYYY/topic-slug/` |

---

## CRITICAL: Content Rules

### No Technical Implementation in Descriptions

**NEVER include in description.md or pinned-comment.md:**
- Docker Compose files or snippets
- Shell commands or terminal output
- Installation scripts or code blocks
- Configuration file contents

**User handles technical content on their GitHub repository.** Reference GitHub instead.

### Mild, Friendly Language

**AVOID harsh words:**
| Don't Say | Say Instead |
|-----------|-------------|
| "is dead" | "is no longer actively maintained" |
| "killed it" | "development has slowed" |
| "abandoned" | "seeking new maintainers" |
| "defunct" | "development paused" |

**Be respectful** of open-source maintainers.

### No Double Dashes or Em Dashes

**NEVER use:** `--`, `—`, or `–`

These sound AI-generated. Use periods or commas instead.

---

## CRITICAL: YouTube Formatting Rules

**YouTube does NOT support Markdown.** Files `description.md` and `pinned-comment.md` MUST use YouTube-native syntax.

### Quick Reference

| Format | YouTube Syntax | NOT This |
|--------|----------------|----------|
| **Bold** | `*text*` | `**text**` |
| *Italic* | `_text_` | - |
| Bullet | `* item` (line start + space) | `- item` in markdown |
| Numbered | `1.` `2.` (manual) | Auto-numbering |
| Divider | `_______________` | `---` |
| Header | `⏱️ *TIMESTAMPS*` | `## Timestamps` |

### Link Rules

- **MUST** include `https://` for clickable links
- Twitter: Use `twitter.com` (NOT `x.com`) - for reliable icon display
- Facebook: Use `facebook.com` (NOT `fb.com`)

### Character Limits

- **Above the fold**: 100-160 chars (ONLY visible text before "Show more")
- **Total**: 5,000 chars

See `05-Templates/youtube-formatting-reference.md` for complete rules.

---

## Examples

```
/youtube idea "Zero Trust for Small Business"
→ Creates: 03-YouTube/ideas/2026-01-10-zero-trust-small-business.md

/youtube full "Docker Backup Strategies"
→ Creates: 03-YouTube/drafts/2026-01-10-docker-backup-strategies/
   ├── script.md
   ├── description.md      (YouTube formatting)
   ├── thumbnail-text.md
   └── pinned-comment.md   (YouTube formatting)
→ Asks: "Has this video been uploaded?"

/youtube publish "Docker Backup Strategies"
→ Verifies on YouTube
→ Creates: 03-YouTube/published/2026/docker-backup-strategies/
   ├── video.md
   ├── script.md
   ├── description.md
   ├── thumbnail-text.md
   ├── pinned-comment.md
   └── social-content.json
→ Updates: youtube-index.json
```

## Quality Standards

All content must:
- Sound like your channel voice (see `writing-style.md`)
- Follow channel brand principles
- Include practical examples
- Have correct grammar
- **Use YouTube formatting (NOT Markdown) for description and pinned comment**
- Use proper file naming and tags

## Validation Checklist

Before completing any `/youtube full` command:

**Content Rules:**
- [ ] NO technical implementation (no code, commands, Docker files)
- [ ] Technical content referenced to GitHub only
- [ ] NO harsh language ("dead", "abandoned", "defunct")
- [ ] NO double dashes (--) or em dashes (—)
- [ ] Respectful of open-source maintainers

**YouTube Formatting:**
- [ ] Bold uses `*text*` NOT `**text**`
- [ ] Bullet points use `* item` (asterisk + space at line start)
- [ ] Dividers use `_______________` (underscores)
- [ ] NO markdown headers (`#`, `##`)
- [ ] All links include `https://`
- [ ] Twitter uses `twitter.com` NOT `x.com`
- [ ] Facebook uses `facebook.com` NOT `fb.com`
- [ ] First 100-160 chars contain hook + keyword

## Related Commands

After publishing:
- `/social linkedin "topic-slug"` - Create LinkedIn post
- `/social twitter "topic-slug"` - Create Twitter thread
- `/social all "topic-slug"` - All platforms

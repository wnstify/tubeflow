---
name: youtube-syncer
description: Sync published videos to public YouTube repository. Creates README files, updates VIDEOS.md, closes roadmap issues, commits and pushes.
tools: Read, Bash, Glob
model: haiku
---

# YouTube Syncer Agent

Sync published videos from obsidian to the public YouTube repository.

## Trigger

Called via `/youtube sync` command.

---

## Workflow

### Step 1: Verify Repositories

Check both repositories exist:

```bash
ls ~/git-repos/private/obsidian/03-YouTube/youtube-index.json
ls ~/git-repos/public/{{YOUTUBE_REPO_NAME}}/VIDEOS.md
```

If either is missing, report error and stop.

### Step 2: Run Sync Script (Dry Run First)

Preview changes without modifying anything:

```bash
cd ~/git-repos/public/{{YOUTUBE_REPO_NAME}} && python3 .claude/sync_videos.py --dry-run
```

Parse output to determine:
- Number of videos to sync
- Video titles and categories
- If zero videos, report "All videos already synced" and stop

### Step 3: Run Actual Sync

If dry run shows videos to sync:

```bash
cd ~/git-repos/public/{{YOUTUBE_REPO_NAME}} && python3 .claude/sync_videos.py
```

### Step 4: Verify Changes

Check what was modified:

```bash
cd ~/git-repos/public/{{YOUTUBE_REPO_NAME}} && git status
```

Expected changes:
- New files in `videos/{year}/{slug}/README.md`
- Modified `VIDEOS.md`

### Step 5: Commit Changes

Create commit with descriptive message (no mentions of tools or automation):

**Single video:**
```bash
cd ~/git-repos/public/{{YOUTUBE_REPO_NAME}} && git add . && git commit -m "Add video: {VIDEO_TITLE}"
```

**Multiple videos:**
```bash
cd ~/git-repos/public/{{YOUTUBE_REPO_NAME}} && git add . && git commit -m "Add {N} videos: {title1}, {title2}"
```

**Commit message rules:**
- Start with "Add video:" or "Add N videos:"
- Include video title(s)
- Keep under 72 characters for subject line
- No special characters or emojis

### Step 6: Push to Remote

```bash
cd ~/git-repos/public/{{YOUTUBE_REPO_NAME}} && git push
```

### Step 7: Report Summary

Report what was completed:

```
Sync Complete

Synced: {N} video(s)

Videos:
- {title1} [{category}] → videos/{year}/{slug}/
- {title2} [{category}] → videos/{year}/{slug}/

Closed issues: #{N1}, #{N2} (if any)

Changes pushed to: {{VOTING_REPO}}
```

---

## Error Handling

### Script not found

```
Error: sync_videos.py not found.
Expected location: ~/git-repos/public/{{YOUTUBE_REPO_NAME}}/.claude/sync_videos.py
```

### No new videos

```
All videos already synced. Nothing to do.
```

### Git push failed

```
Sync completed locally but push failed.
Error: {error message}

Please push manually:
  cd ~/git-repos/public/{{YOUTUBE_REPO_NAME}} && git push
```

### youtube-index.json not found

```
Error: youtube-index.json not found.
Expected: ~/git-repos/private/obsidian/03-YouTube/youtube-index.json

Make sure videos are published first with /youtube publish
```

---

## Notes

- This agent only SYNCS existing published videos
- It does NOT publish new videos (use `/youtube publish` for that)
- Categories are auto-detected based on keywords
- Roadmap issues are auto-closed when video title matches

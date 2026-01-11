# TubeFlow Workflows

Complete documentation of TubeFlow's content creation pipeline and agent architecture.

---

## Complete Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    TUBEFLOW VIDEO PIPELINE                       │
├─────────────────────────────────────────────────────────────────┤
│  1. RESEARCH (Optional) → /youtube-research "Topic"             │
│  2. CREATE             → /youtube full "Topic"                  │
│  3. FILM & UPLOAD      → [You do this manually]                 │
│  4. PUBLISH            → /youtube publish "Topic"               │
│  5. SYNC               → /youtube sync                          │
│  6. SOCIAL             → /social video "slug"                   │
└─────────────────────────────────────────────────────────────────┘
```

### Quick Reference

| Step | Command | Time | Output |
|------|---------|------|--------|
| Research | `/youtube-research "Topic"` | 5-8 min | research-pack.md, series-structure.md |
| Create | `/youtube full "Topic"` | 3-5 min | Complete draft package |
| Film & Upload | Manual | Varies | Video on YouTube |
| Publish | `/youtube publish "Topic"` | 1-2 min | Published folder with metadata |
| Sync | `/youtube sync` | < 1 min | Public repo updates |
| Social | `/social video "slug"` | 2-3 min | Platform-specific posts |

---

## YouTube Research Workflow

The research workflow uses 5 specialized agents to gather comprehensive information before content creation.

### When to Use Research

**Use research for:**
- New topics you haven't covered before
- Complex topics with many subtopics
- Series planning (multiple related videos)
- Competitive analysis before entering a niche
- SEO-focused content planning

**Skip research when:**
- Quick tip videos
- Updates to existing content
- Simple how-to tutorials on familiar topics
- Time-sensitive content

### Command

```bash
/youtube-research "Topic Name"
```

### The 5 Research Agents

```
/youtube-research "Topic"
         │
    [Main Claude Agent handles orchestration]
         │
         ├── @yt-topic-gatherer (Haiku)      ─┐
         ├── @yt-competitor-gatherer (Haiku) ─┼─ Phase 1: Parallel
         ├── @yt-seo-gatherer (Haiku)        ─┤
         └── @yt-community-gatherer (Haiku)  ─┘
                      │
                      ▼
         └── @yt-research-strategist (Opus)  ─── Phase 2: Sequential
                      │
                      ▼
              research-pack.md + series-structure.md
```

#### Agent Responsibilities

| Agent | Model | Phase | Responsibility |
|-------|-------|-------|----------------|
| **Topic Gatherer** | Haiku | 1 (Parallel) | Features, documentation, complexity assessment, prerequisites |
| **Competitor Gatherer** | Haiku | 1 (Parallel) | Existing YouTube videos, content gaps, differentiation opportunities |
| **SEO Gatherer** | Haiku | 1 (Parallel) | Keywords, search trends, optimal titles, tags |
| **Community Gatherer** | Haiku | 1 (Parallel) | Reddit discussions, forum questions, pain points |
| **Research Strategist** | Opus | 2 (Sequential) | Synthesizes all data into actionable recommendations |

### Workflow Timing

- **Phase 1** (4 parallel agents): 2-3 minutes
- **Phase 2** (strategist synthesis): 3-5 minutes
- **Total**: 5-8 minutes

### Output Structure

```
{youtube_root}/research/YYYY-MM-DD-topic/
├── research-pack.md        # Strategic recommendations
├── series-structure.md     # Episode breakdown (if series)
├── summaries/              # Condensed findings (~3,200 tokens)
│   ├── topic-summary.md
│   ├── competitor-summary.md
│   ├── seo-summary.md
│   └── community-summary.md
└── raw/                    # Full research data
    ├── topic-raw.md
    ├── competitor-raw.md
    ├── seo-raw.md
    └── community-raw.md
```

### Research Pack Contents

The `research-pack.md` file contains:

| Section | Description |
|---------|-------------|
| Executive Summary | Key findings and primary recommendation |
| Topic Overview | Features, complexity level, prerequisites |
| Competitor Landscape | Existing videos, gaps, how to differentiate |
| Target Audience | Who benefits, what they need to know first |
| SEO Strategy | Primary/secondary keywords, title options, tags |
| Community Insights | Real questions from forums, pain points |
| Content Recommendation | Single video or series with reasoning |
| Production Notes | Demo requirements, technical difficulty |

### Series Detection

The strategist agent automatically determines if a topic warrants a series.

**Recommends series when:**
- Topic has 3+ distinct subtopics
- Each subtopic needs 10+ minutes of coverage
- Clear learning progression exists
- Audience benefits from structured learning

**Recommends single video when:**
- Topic is focused and contained
- Can cover thoroughly in 15-30 minutes
- No natural breaking points
- Concept-focused rather than multi-step

### Using Research in Content Creation

After completing research:

```bash
# Review the research pack
cat research/YYYY-MM-DD-topic/research-pack.md

# Create content informed by research
/youtube full "Topic Part 1"
```

The content creation agents reference the research pack for:
- Accurate terminology and features
- SEO-optimized titles and descriptions
- Content gaps to address
- Community questions to answer

---

## YouTube Content Creation Workflow

### Available Commands

| Command | Description | Output Location |
|---------|-------------|-----------------|
| `/youtube idea "Topic"` | Quick idea capture | `{youtube_root}/ideas/` |
| `/youtube full "Topic"` | Complete draft package | `{youtube_root}/drafts/topic/` |

### Quick Idea Capture

```bash
/youtube idea "Docker Security Best Practices"
```

Creates a quick idea file with:
- Topic title
- Brief description
- Initial thoughts
- Status: `#status/idea`

**Output**: `{youtube_root}/ideas/YYYY-MM-DD-docker-security.md`

### Full Draft Package

```bash
/youtube full "Docker Security Best Practices"
```

Creates a complete production-ready package:

```
{youtube_root}/drafts/docker-security/
├── script.md              # Full video script with timestamps
├── description.md         # YouTube description (YouTube-native format)
├── thumbnail-text.md      # BOLD (3-5 words) + description (13-18 words)
└── pinned-comment.md      # Engagement comment with links
```

#### Script.md Contents

- Hook (first 30 seconds)
- Main content with sections
- Timestamp markers
- CTAs (calls to action)
- Outro

#### Description.md Contents

- Above-the-fold hook (100-160 chars)
- Video summary
- Timestamps
- Relevant links (based on topic)
- Standard channel links
- About section

**Important**: Uses YouTube-native formatting (`*bold*`, `_italic_`), not Markdown.

#### Thumbnail-text.md Contents

Two-line format:
```
DOCKER SECURITY
Master container protection with proven techniques
```

- Line 1: BOLD text (3-5 words, all caps)
- Line 2: Description (13-18 words)

#### Pinned-comment.md Contents

- Engagement question
- Additional resource links
- Community links (Discord, etc.)
- Video voting link

### Voice and Style Integration

All content automatically references:
- `writing-style.md` - Your voice and tone
- `channel-overview.md` - Brand principles

Content rules enforced:
- No harsh language about open-source projects
- No double dashes or em dashes
- Respectful tone toward developers and maintainers
- Platform-native formatting

### Duplicate Prevention

Before creating content, TubeFlow checks `youtube-index.json` to prevent:
- Duplicate topics
- Similar titles
- Overlapping content

---

## Publishing Workflow

### Prerequisites

Before running publish:
1. Video is uploaded to YouTube
2. Video is set to Public or Unlisted
3. You have the YouTube URL

### Command

```bash
/youtube publish "Docker Security" --url "https://youtube.com/watch?v=VIDEO_ID"
```

Or without URL (will prompt):

```bash
/youtube publish "Docker Security"
```

### What Publishing Does

1. **Moves draft to published**:
   ```
   drafts/docker-security/ → published/YYYY/docker-security/
   ```

2. **Fetches metadata via yt-dlp**:
   - Actual video title
   - Video ID
   - Duration
   - Upload date
   - Thumbnail URL

3. **Creates video.md**:
   - YouTube metadata
   - Links to all content files
   - Status: `#status/published`

4. **Generates social-content.json**:
   ```json
   {
     "title": "Docker Security Best Practices",
     "url": "https://youtube.com/watch?v=VIDEO_ID",
     "description": "Short description for social",
     "hooks": ["LinkedIn hook", "Twitter hook", "Facebook hook"],
     "hashtags": ["Docker", "Security", "DevOps"]
   }
   ```

5. **Updates youtube-index.json**:
   - Adds video to master index
   - Marks topic as covered

### Output Structure

```
{youtube_root}/published/YYYY/docker-security/
├── video.md               # YouTube metadata
├── script.md              # Original script
├── description.md         # YouTube description
├── thumbnail-text.md      # Thumbnail text
├── pinned-comment.md      # Pinned comment
└── social-content.json    # For social workflow
```

---

## Sync Workflow

The sync workflow connects your private vault to a public GitHub repository, enabling community engagement and video voting.

### Command

```bash
/youtube sync
```

### What Sync Does

1. **Scans published videos** since last sync

2. **Updates public repository**:
   ```
   your-public-repo/
   ├── README.md           # Channel overview, recent videos
   ├── VIDEOS.md           # Complete video catalog
   └── videos/
       └── YYYY/
           └── docker-security.md  # Public video info
   ```

3. **Updates README.md**:
   - Recent videos section
   - Quick links
   - Video counts

4. **Updates VIDEOS.md**:
   - Chronological video list
   - Categories
   - Links

5. **Closes roadmap issues**:
   - Finds GitHub issues matching video topic
   - Adds comment with video link
   - Closes issue

### Public Repository Structure

The sync creates a public-facing repository with:

```
public-repo/
├── README.md              # Channel overview
├── VIDEOS.md              # Video catalog
├── ROADMAP.md             # Community voting via issues
├── videos/
│   └── YYYY/
│       └── topic-slug.md  # Per-video pages
└── .github/
    └── ISSUE_TEMPLATE/
        └── video-request.md
```

### Community Voting

Users can:
1. Open issues to request videos
2. Upvote existing requests
3. Discuss topics in issue comments
4. See their request closed when video publishes

---

## Social Media Workflow

### Available Commands

| Command | Description |
|---------|-------------|
| `/social linkedin "Topic"` | LinkedIn post (1,300-1,600 chars) |
| `/social twitter "Topic"` | Twitter post + optional thread |
| `/social facebook "Topic"` | Facebook post (40-80 chars optimal) |
| `/social all "Topic"` | All platforms + cross-post index |
| `/social video "slug"` | All platforms from published video |

### Platform-Specific Creation

```bash
/social linkedin "Docker Security Best Practices"
```

Creates platform-optimized content with:
- Correct character limits
- Platform-native formatting
- Appropriate hashtags
- Links in correct location (first comment for LinkedIn/Facebook)

### All Platforms

```bash
/social all "Docker Security Best Practices"
```

Creates:
```
{social_root}/
├── linkedin/YYYY-MM-DD-docker-security.md
├── twitter/YYYY-MM-DD-docker-security.md
├── facebook/YYYY-MM-DD-docker-security.md
└── cross-post/YYYY-MM-DD-docker-security.md  # Index file
```

### From Published Video

```bash
/social video "docker-security"
```

Reads `social-content.json` from the published video and creates all platform posts automatically. This ensures:
- Consistent messaging across platforms
- Correct video URL included
- Hashtags from video applied

### Platform Formatting Differences

| Platform | Length | Hashtags | Links | Formatting |
|----------|--------|----------|-------|------------|
| **LinkedIn** | 1,300-1,600 chars | 3-5 at end | First comment | Plain text, emojis |
| **Twitter** | 200-250 chars | 1-2 | In post | Native bold/italic |
| **Facebook** | 40-80 chars | 2-3 | First comment | Plain text |

### Content Rules

All social content follows:
- Your writing style guide
- No harsh language about projects
- No double dashes
- Platform-specific best practices

---

## Agent Architecture

### Model Selection

TubeFlow uses different models optimized for each task:

| Task | Model | Reasoning |
|------|-------|-----------|
| Research gathering | Haiku | Fast, cost-effective for parallel data collection |
| Research synthesis | Opus | Powerful reasoning for strategy development |
| Content creation | Sonnet | Balanced quality and speed for writing |

Configure in `config.yaml`:

```yaml
advanced:
  research_model: "haiku"
  strategy_model: "opus"
  content_model: "sonnet"
```

### Parallel vs Sequential Execution

**Parallel execution** (Phase 1 research):
- 4 research agents run simultaneously
- Total time: 2-3 minutes (not 8-12 minutes)
- Reduces cost through parallelization

**Sequential execution** (Phase 2 and content):
- Strategist waits for all research
- Content creation is inherently sequential
- Ensures proper dependency handling

### Agent Communication

Agents communicate through:
1. **File-based handoffs**: Output files become input for next stage
2. **Context passing**: Summaries condensed to ~3,200 tokens for efficiency
3. **Index files**: Track state and prevent duplicates

### Spawning Pattern

```
Main Claude Session
    │
    ├── Spawns: Research Agents (parallel)
    │   ├── @yt-topic-gatherer
    │   ├── @yt-competitor-gatherer
    │   ├── @yt-seo-gatherer
    │   └── @yt-community-gatherer
    │
    ├── Waits for completion
    │
    └── Spawns: Strategist (sequential)
        └── @yt-research-strategist
```

---

## Workflow Integration Examples

### Full Pipeline Example

```bash
# 1. Research (optional but recommended for new topics)
/youtube-research "Kubernetes Security"

# Review research
# Make adjustments to series plan if needed

# 2. Create content
/youtube full "Kubernetes Security Part 1: Pod Security"

# Review and edit script as needed

# 3. Film and upload to YouTube
# [Manual step]

# 4. Publish (updates vault with metadata)
/youtube publish "Kubernetes Security Part 1" --url "https://..."

# 5. Sync to public repo (if enabled)
/youtube sync

# 6. Create social media posts
/social video "kubernetes-security-part-1"
```

### Quick Tip Video (No Research)

```bash
# Skip research for quick tips
/youtube full "Quick Tip: Docker Compose Override Files"

# Film and upload
# [Manual step]

# Publish
/youtube publish "Quick Tip Docker Compose Override"

# Social
/social video "docker-compose-override"
```

### Idea to Research Pipeline

```bash
# Capture idea first
/youtube idea "Home Lab Networking Deep Dive"

# Later, when ready to develop
/youtube-research "Home Lab Networking"

# Review research, then create
/youtube full "Home Lab Networking Part 1"
```

---

## Troubleshooting

### Research Takes Too Long

- Ensure parallel execution is enabled in config
- Check network connectivity
- Consider reducing research scope

### Duplicate Topic Warning

- TubeFlow checks `youtube-index.json`
- If legitimate new angle, proceed with different title
- If actual duplicate, create update video instead

### yt-dlp Errors During Publish

- Ensure yt-dlp is installed: `pip install yt-dlp`
- Video must be Public or Unlisted
- Check video URL format

### Social Content Missing

- Ensure `social-content.json` was generated during publish
- Re-run publish if needed
- Manually create social-content.json if necessary

---

## Configuration Reference

Key `config.yaml` settings affecting workflows:

```yaml
features:
  public_repo_sync: true      # Enable /youtube sync
  social_media: true          # Enable /social commands
  research_agents: true       # Enable /youtube-research
  sponsorship_research: true  # Research open-source support options

advanced:
  parallel_research: true     # Run research agents in parallel
  auto_publish_prompt: true   # Ask about publishing after /youtube full
```

See [config.example.yaml](../config.example.yaml) for complete options.

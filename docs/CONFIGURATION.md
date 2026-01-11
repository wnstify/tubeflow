# TubeFlow Configuration Reference

Complete reference for all configuration options in `config.yaml`.

---

## Quick Start

```bash
# Copy example config
cp config.example.yaml config.yaml

# Edit with your details
nano config.yaml  # or your preferred editor
```

---

## Configuration File Location

TubeFlow looks for `config.yaml` in these locations (in order):

1. Current working directory: `./config.yaml`
2. Vault root: `/path/to/your-vault/config.yaml`
3. TubeFlow installation: `/path/to/tubeflow/config.yaml`

---

## Configuration Sections

### Version

```yaml
version: "1.0"
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | string | Yes | Config file version. Do not change. |

---

## Channel Identity

Define your channel's basic information.

```yaml
channel:
  name: "Your Channel Name"
  handle: "@yourchannel"
  tagline: "Your channel tagline here"
  niche: "self-hosting"
```

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `name` | string | Yes | - | Your channel's display name. Used in descriptions and references. |
| `handle` | string | Yes | - | Your YouTube handle with @ prefix. Example: `@webnestify` |
| `tagline` | string | No | - | Short phrase describing your channel. Used in about sections. |
| `niche` | string | No | `"general"` | Primary content category. Helps with content suggestions and research focus. |

**Niche Options:**
- `self-hosting` - Home servers, Docker, self-hosted apps
- `programming` - Coding tutorials, software development
- `devops` - CI/CD, infrastructure, cloud
- `gaming` - Game reviews, walkthroughs, streaming
- `education` - Learning, courses, explainers
- `tech-reviews` - Product reviews, comparisons
- `ai-ml` - Artificial intelligence, machine learning
- `cybersecurity` - Security, privacy, hacking
- `general` - Mixed content

---

## Voice and Style

Configure how your content sounds.

```yaml
voice:
  style_file: "writing-style.md"
  channel_overview_file: "channel-overview.md"
  tone: "friendly"
```

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `style_file` | string | No | `"writing-style.md"` | Path to your writing style guide (relative to vault root). |
| `channel_overview_file` | string | No | `"channel-overview.md"` | Path to your channel brand guide. |
| `tone` | string | No | `"friendly"` | Default content tone. |

**Tone Options:**
- `friendly` - Warm, approachable, conversational
- `professional` - Business-appropriate, polished
- `casual` - Relaxed, informal, like talking to a friend
- `educational` - Clear, instructive, teacher-like

### Creating a Writing Style Guide

Your `writing-style.md` should include:

```markdown
# Writing Style Guide

## Voice Characteristics
- Direct and clear
- Uses "you" and "your" to address viewers
- Avoids jargon unless explaining it
- Never uses double dashes (--) or em dashes

## Phrases to Use
- "Let me show you..."
- "Here's the thing..."
- "The cool part is..."

## Phrases to Avoid
- "In this video, I will..."
- "Please like and subscribe"
- "Without further ado"

## Technical Content
- Always explain acronyms on first use
- Use code blocks for commands
- Include expected output

## Formatting
- Short paragraphs (1-3 sentences)
- Bullet points for lists
- Bold for emphasis, not all caps
```

### Creating a Channel Overview

Your `channel-overview.md` should include:

```markdown
# Channel Overview

## Mission
Help developers master self-hosting and take control of their infrastructure.

## Target Audience
- Developers wanting to self-host
- IT professionals exploring alternatives
- Hobbyists building home labs

## Content Pillars
1. Docker and containerization
2. Self-hosted applications
3. Home lab infrastructure
4. DevOps automation

## Brand Values
- Practical over theoretical
- Honest about limitations
- Community-focused
- Open source advocacy

## Visual Style
- Clean, minimal thumbnails
- Dark mode code examples
- Terminal-focused demos
```

---

## Folder Structure

Configure where TubeFlow stores content.

```yaml
structure:
  type: "obsidian"
  youtube_root: "03-YouTube"
  social_root: "04-Social"
  templates_root: "05-Templates"
  ideas_folder: "ideas"
  drafts_folder: "drafts"
  published_folder: "published"
  research_folder: "research"
```

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `type` | string | No | `"obsidian"` | Vault type: `obsidian` or `markdown`. Affects link formatting. |
| `youtube_root` | string | No | `"03-YouTube"` | Root folder for all YouTube content. |
| `social_root` | string | No | `"04-Social"` | Root folder for social media content. |
| `templates_root` | string | No | `"05-Templates"` | Root folder for templates. |
| `ideas_folder` | string | No | `"ideas"` | Subfolder for video ideas. |
| `drafts_folder` | string | No | `"drafts"` | Subfolder for active drafts. |
| `published_folder` | string | No | `"published"` | Subfolder for published videos. |
| `research_folder` | string | No | `"research"` | Subfolder for research packs. |

**Resulting Structure:**

```
your-vault/
├── 03-YouTube/         # youtube_root
│   ├── ideas/          # ideas_folder
│   ├── drafts/         # drafts_folder
│   ├── published/      # published_folder
│   └── research/       # research_folder
├── 04-Social/          # social_root
└── 05-Templates/       # templates_root
```

**Custom Example:**

```yaml
structure:
  type: "markdown"
  youtube_root: "content/youtube"
  social_root: "content/social"
  templates_root: "resources/templates"
```

Results in:
```
your-vault/
├── content/
│   ├── youtube/
│   │   ├── ideas/
│   │   ├── drafts/
│   │   ├── published/
│   │   └── research/
│   └── social/
└── resources/
    └── templates/
```

---

## Links

Configure URLs included in your content.

```yaml
links:
  # Required
  discord: "https://discord.gg/your-server"
  business: "https://yoursite.com/contact"
  github_org: "https://github.com/yourorg"

  # Recommended
  voting_repo: "https://github.com/yourorg/youtube-videos"
  docker_repo: "https://github.com/yourorg/docker"

  # Social Media
  linkedin: "https://linkedin.com/company/yourcompany"
  facebook: "https://facebook.com/yourpage"
  twitter: "https://twitter.com/yourhandle"

  # Optional
  reviews: "https://trustpilot.com/review/yoursite"
  featured_video: "https://youtube.com/watch?v=xxxxx"
  featured_video_title: "Getting Started with Self-Hosting"
```

### Required Links

| Field | Description | Example |
|-------|-------------|---------|
| `discord` | Community Discord server | `https://discord.gg/abc123` |
| `business` | Business inquiries page | `https://yoursite.com/contact` |
| `github_org` | GitHub organization/user | `https://github.com/yourorg` |

### Recommended Links

| Field | Description | Example |
|-------|-------------|---------|
| `voting_repo` | Repository where viewers vote on upcoming videos | `https://github.com/yourorg/youtube` |
| `docker_repo` | Repository with Docker Compose files | `https://github.com/yourorg/docker` |

### Social Media Links

| Field | Description | Format Notes |
|-------|-------------|--------------|
| `linkedin` | LinkedIn company/personal page | Use full URL |
| `facebook` | Facebook page | Use `facebook.com` not `fb.com` |
| `twitter` | Twitter/X profile | Use `twitter.com` not `x.com` for icon display |

### Optional Links

| Field | Description | When Used |
|-------|-------------|-----------|
| `reviews` | Review site (Trustpilot, G2, etc.) | Added to descriptions if set |
| `featured_video` | Your most important video URL | Referenced in descriptions |
| `featured_video_title` | Title for the featured video | Displayed with the link |

**Link Format Rules:**

```yaml
# CORRECT - Full URLs with https://
twitter: "https://twitter.com/yourhandle"
facebook: "https://facebook.com/yourpage"

# INCORRECT - Missing protocol or wrong domain
twitter: "twitter.com/yourhandle"      # Missing https://
twitter: "https://x.com/yourhandle"    # Use twitter.com for icon
facebook: "https://fb.com/yourpage"    # Use facebook.com
```

---

## Features

Enable or disable TubeFlow capabilities.

```yaml
features:
  public_repo_sync: true
  social_media: true
  research_agents: true
  sponsorship_research: true
  obsidian_links: true
  include_about_section: true
```

| Feature | Type | Default | Description |
|---------|------|---------|-------------|
| `public_repo_sync` | boolean | `true` | Sync published videos to public GitHub repo. Creates README, updates catalog. |
| `social_media` | boolean | `true` | Enable `/social` commands for social media content. |
| `research_agents` | boolean | `true` | Use 5 specialized agents for topic research before content creation. |
| `sponsorship_research` | boolean | `true` | Research FUNDING.yml and GitHub Sponsors for open-source projects. |
| `obsidian_links` | boolean | `true` | Use `[[wiki-links]]` instead of `[markdown](links)`. |
| `include_about_section` | boolean | `true` | Include "About" section at end of YouTube descriptions. |

### Feature Details

**public_repo_sync**

When enabled:
- Creates `README.md` in published video folder
- Updates `youtube-index.json` with video metadata
- Closes related issues in voting repo (if configured)

When disabled:
- Videos stay local only
- No GitHub integration

**research_agents**

When enabled:
- `/youtube full` runs research phase first
- Uses 4 parallel Haiku agents + 1 Opus strategist
- Takes 5-8 minutes but produces higher quality content

When disabled:
- Skips research phase
- Creates content from Claude's base knowledge
- Much faster but may miss current information

**sponsorship_research**

When enabled:
- Checks GitHub for FUNDING.yml and Sponsors
- Includes support links in descriptions
- Thanks maintainers by name

When disabled:
- No sponsorship information gathered
- You'll need to add support links manually

---

## About Section

Configure the "About" section for YouTube descriptions.

```yaml
about:
  company_name: "Your Company"
  established: "2024"
  location: "Your Location"
  tagline: "Your mission statement here"
  application_url: "https://yoursite.com/apply"
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `company_name` | string | Yes (if about enabled) | Your company or channel name. |
| `established` | string | No | Year established. |
| `location` | string | No | Geographic location. |
| `tagline` | string | Yes (if about enabled) | Mission statement or tagline. |
| `application_url` | string | No | URL for applications/signups. |

**Generated Output:**

```
*ABOUT WEBNESTIFY*

Established in Slovakia in 2021. Webnestify is more than a cloud solutions
provider. We're your strategic partner in digital transformation. Businesses
of all sizes deserve the best technology. We're here to ensure your company
doesn't just keep up with the digital age but thrives in it.

Join Webnestify and let's redefine success together.
Apply for exclusive access: https://yoursite.com/apply
```

---

## Advanced Configuration

Fine-tune TubeFlow behavior.

```yaml
advanced:
  research_model: "haiku"
  strategy_model: "opus"
  content_model: "sonnet"
  parallel_research: true
  auto_publish_prompt: true
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `research_model` | string | `"haiku"` | Model for research gathering agents. Fast and cheap. |
| `strategy_model` | string | `"opus"` | Model for research synthesis. Most powerful. |
| `content_model` | string | `"sonnet"` | Model for content creation. Balanced. |
| `parallel_research` | boolean | `true` | Run research agents in parallel (faster) vs sequential (cheaper). |
| `auto_publish_prompt` | boolean | `true` | Ask about publishing after `/youtube full` completes. |

### Model Options

| Model | Speed | Cost | Best For |
|-------|-------|------|----------|
| `haiku` | Fastest | Lowest | Quick research, simple tasks |
| `sonnet` | Balanced | Medium | Content creation, editing |
| `opus` | Slowest | Highest | Complex synthesis, strategy |

### Parallel vs Sequential Research

**Parallel (`parallel_research: true`)**
- Runs 4 research agents simultaneously
- Completes in ~2-3 minutes
- Uses more API calls at once

**Sequential (`parallel_research: false`)**
- Runs research agents one at a time
- Completes in ~8-10 minutes
- Lower concurrent API usage

---

## Environment Variables

TubeFlow respects these environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `TUBEFLOW_CONFIG` | Override config file path | `/custom/path/config.yaml` |
| `TUBEFLOW_VAULT` | Override vault root path | `/path/to/vault` |
| `TUBEFLOW_DEBUG` | Enable debug logging | `true` |

**Usage:**

```bash
# Use custom config
TUBEFLOW_CONFIG=/custom/config.yaml claude

# Enable debugging
TUBEFLOW_DEBUG=true claude
```

---

## Updating Configuration

After changing `config.yaml`:

1. **No restart required** - Changes take effect on next command
2. **Validate syntax** - YAML is indentation-sensitive

```bash
# Validate YAML syntax
python3 -c "import yaml; yaml.safe_load(open('config.yaml'))"
```

### Migrating Configuration

When upgrading TubeFlow:

1. Backup your current config:
```bash
cp config.yaml config.yaml.backup
```

2. Compare with new example:
```bash
diff config.yaml config.example.yaml
```

3. Add any new fields from example to your config

4. Test with a simple command:
```bash
/youtube idea "Test"
```

---

## Complete Example

Here's a complete, production-ready configuration:

```yaml
version: "1.0"

channel:
  name: "TechExplorer"
  handle: "@techexplorer"
  tagline: "Exploring technology one video at a time"
  niche: "self-hosting"

voice:
  style_file: "writing-style.md"
  channel_overview_file: "channel-overview.md"
  tone: "friendly"

structure:
  type: "obsidian"
  youtube_root: "03-YouTube"
  social_root: "04-Social"
  templates_root: "05-Templates"
  ideas_folder: "ideas"
  drafts_folder: "drafts"
  published_folder: "published"
  research_folder: "research"

links:
  discord: "https://discord.gg/techexplorer"
  business: "https://techexplorer.dev/contact"
  github_org: "https://github.com/techexplorer"
  voting_repo: "https://github.com/techexplorer/youtube"
  docker_repo: "https://github.com/techexplorer/docker-stacks"
  linkedin: "https://linkedin.com/company/techexplorer"
  facebook: "https://facebook.com/techexplorerdev"
  twitter: "https://twitter.com/techexplorer"
  reviews: ""
  featured_video: "https://youtube.com/watch?v=abc123"
  featured_video_title: "Complete Self-Hosting Guide"

features:
  public_repo_sync: true
  social_media: true
  research_agents: true
  sponsorship_research: true
  obsidian_links: true
  include_about_section: true

about:
  company_name: "TechExplorer"
  established: "2023"
  location: "United States"
  tagline: "Making technology accessible for everyone"
  application_url: ""

advanced:
  research_model: "haiku"
  strategy_model: "opus"
  content_model: "sonnet"
  parallel_research: true
  auto_publish_prompt: true
```

---

## Troubleshooting Configuration

### YAML Syntax Errors

**Symptom:** Config not loading, strange behavior

**Common Issues:**
```yaml
# WRONG - Bad indentation
channel:
name: "Test"

# CORRECT - Proper indentation
channel:
  name: "Test"

# WRONG - Missing quotes on special characters
tagline: Here's my tagline

# CORRECT - Quoted strings with special chars
tagline: "Here's my tagline"
```

### Missing Required Fields

**Symptom:** Errors about missing configuration

**Solution:** Ensure all required fields are present:
```yaml
channel:
  name: "Required"
  handle: "@required"

links:
  discord: "Required"
  business: "Required"
  github_org: "Required"
```

### Links Not Appearing

**Symptom:** Links missing from generated content

**Check:**
1. Links have full `https://` prefix
2. Links field is not empty string for required links
3. Feature using the link is enabled

```yaml
# Empty string = link not included
reviews: ""

# Proper URL = link included
reviews: "https://trustpilot.com/review/example"
```

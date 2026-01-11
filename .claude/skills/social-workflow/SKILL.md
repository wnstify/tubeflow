---
name: social-workflow
description: Create social media posts for LinkedIn, Twitter/X, and Facebook. Use when user requests social posts, cross-platform content, or wants to promote YouTube videos on social media.
---

# Social Media Workflow Skill

Create platform-optimized social media content for {{CHANNEL_HANDLE}} brand across LinkedIn, Twitter/X, and Facebook.

---

## CRITICAL: Agent Spawning Requirement

**You MUST use the Task tool to spawn the `@social-creator` agent.** Do NOT handle this workflow directly.

### How to Execute

```
Task tool:
  subagent_type: "social-creator"
  prompt: [Include platform, topic, and any source material]
```

### MANDATORY: Parallel Execution for `/social all`

**When `/social all` or `/social video` is used, you MUST spawn 3 agents in parallel - one per platform.**

```
/social all "Topic" OR /social video "slug"

MUST spawn all 3 simultaneously:

Task 1: subagent_type: "social-creator"
        prompt: "Create LinkedIn post about [topic]. Follow social-creator agent instructions."

Task 2: subagent_type: "social-creator"
        prompt: "Create Twitter thread about [topic]. Follow social-creator agent instructions."

Task 3: subagent_type: "social-creator"
        prompt: "Create Facebook post about [topic]. Follow social-creator agent instructions."
```

**This is NOT optional.** The whole point of `/social all` is to create 3 posts concurrently.

### Single Agent Usage

**For single platform commands, spawn ONE agent:**

| Command | Spawn |
|---------|-------|
| `/social linkedin "Topic"` | 1 agent → LinkedIn |
| `/social twitter "Topic"` | 1 agent → Twitter |
| `/social facebook "Topic"` | 1 agent → Facebook |

---

## Voice & Brand Integration

**CRITICAL**: All content MUST follow your channel's writing style.

### Voice Reference
Read writing-style.md before generating any content:
- Direct, friendly, honest, solution-focused
- Short sentences (5-15 words ideal)
- Phrases: "Here's the thing...", "Let me show you."
- Strategic emoji usage (not spam)
- Correct grammar always

### Brand Principles
From 03-YouTube/channel-overview.md:
- Complete data ownership
- Zero-trust security
- Independence over convenience
- Practitioner credibility

---

## Platform Specifications

### LinkedIn

| Spec | Value |
|------|-------|
| **Optimal length** | 1,300-1,600 characters |
| **First 150 chars** | Critical - visible before "See more" |
| **Hashtags** | 3-5 at end |
| **Best times** | Tue-Thu, 8-10 AM |
| **Tone** | Professional, insight-focused |

**Hook Types That Work**:
- Contrarian statements (+49% reach)
- Specific numbers (+37% reach)
- Bold questions
- Story-based openers

**Structure**:
```
[Hook - first 150 chars]

[Value content - insights, lessons]

[CTA - question or action]

#Hashtag1 #Hashtag2 #Hashtag3
```

**Avoid**:
- Starting with "I"
- External links in main post (put in comments)
- More than 5 hashtags
- Generic endings like "thoughts?"

---

### Twitter/X

| Spec | Value |
|------|-------|
| **Optimal length** | 71-100 characters per tweet |
| **Thread length** | 5-10 tweets (sweet spot: 5-7) |
| **Hashtags** | 1-2 maximum |
| **Best times** | Tue-Thu, 9-11 AM |
| **Tone** | Conversational, punchy |

**Single Tweet Formula**:
```
[Hook + Value in 71-100 chars]

#Hashtag1 #Hashtag2
```

**Thread Structure**:
```
1/7 [Hook - bold statement or question]

2/7 [Point 1 - one idea]

3/7 [Point 2 - one idea]

...

7/7 [CTA + link]

#Hashtag1 #Hashtag2
```

**Hook Types**:
- Numbers: "7 things I learned..."
- Questions: "Why do 90% of..."
- Bold claims: "This changed everything..."

**Avoid**:
- More than 2 hashtags (21% less engagement)
- Hashtag at start of tweet
- External links without context

---

### Facebook

| Spec | Value |
|------|-------|
| **Optimal length** | 40-80 characters (66% higher engagement) |
| **First 125 chars** | Visible on mobile before "See More" |
| **Hashtags** | 0-3 maximum |
| **Best times** | Wed-Thu, 9 AM-2 PM |
| **Tone** | Community-focused, casual |

**Structure**:
```
[Short hook - 40-80 chars]

[Optional: 1-2 sentence context]

[Video/link if applicable]

[Question to drive comments]
```

**What Works**:
- Native video (135% more reach than photos)
- Questions that spark discussion
- Behind-the-scenes content
- Short, punchy text

**Avoid**:
- Engagement bait ("Like if you agree!")
- External links (algorithm penalty)
- More than 3 hashtags
- Long paragraphs

---

## Emoji Usage in Main Content

**CRITICAL**: Use logical emojis in post content to improve readability and engagement. Not just in links section.

### Emoji Guidelines

| Platform | Count | Placement |
|----------|-------|-----------|
| LinkedIn | 3-5 | Hook, key points, CTA |
| Twitter | 1-2 per tweet | Start of key points |
| Facebook | 2-3 | Hook, CTA |

### Recommended Emojis by Purpose

| Purpose | Emojis |
|---------|--------|
| Insight/Tip | light bulb |
| Key point/Benefit | check mark |
| Warning/Problem | warning sign |
| Goal/Target | target |
| Growth/Launch | rocket |
| Important | key |
| Question/Think | thinking face |

### Placement Rules

**DO**:
- Start hook with emoji: "Insight: Mistborn development has slowed."
- Mark key points: "Check: WG Easy handles VPN management"
- Highlight CTA: "Target: What's your setup?"

**DON'T**:
- Use emoji in every sentence
- Stack multiple emojis together
- Use decorative/random emojis
- Overdo it (keep it subtle)

---

## Featured Video Reference

**CRITICAL**: When post topic relates to self-hosting, ALWAYS reference your featured video.

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

**Placement per platform**:
- LinkedIn: In comments section with other links
- Twitter: In final tweet of thread
- Facebook: In first comment

---

## Standard Links

**ALWAYS include these links** in comments/final tweet:

**Connect**:
- Discord (questions, help): {{DISCORD_URL}}
- Business inquiries: {{BUSINESS_URL}}

**Follow**:
- LinkedIn: {{LINKEDIN_URL}}
- Facebook: {{FACEBOOK_URL}}
- Twitter: {{TWITTER_URL}}

**Link placement per platform**:
| Platform | Where to put links |
|----------|-------------------|
| LinkedIn | First comment (NOT in main post) |
| Twitter | Final tweet of thread OR reply |
| Facebook | First comment (NOT in main post) |

---

## Cross-Platform Adaptation

### Same Message, Different Expression

| Platform | Approach |
|----------|----------|
| **LinkedIn** | Professional framing, industry insight angle |
| **Twitter** | Punchy, opinionated, conversational |
| **Facebook** | Community question, casual tone |

### Example Transformation

**Topic**: Docker backup strategies

**LinkedIn** (1,300+ chars):
```
Most businesses learn about backups the hard way.

Last month, I helped a client recover from a server failure.
They had backups. Sort of. The restore took 6 hours because
no one had tested it in 18 months.

Here's what I tell every client now:

1. Backups you haven't tested don't exist
2. The 3-2-1 rule isn't optional
3. Encryption isn't paranoia - it's basic hygiene

I've deployed this exact strategy for dozens of clients.
Zero data loss incidents.

What's your backup testing schedule?

#DevOps #DataProtection #CloudSecurity
```

**Twitter** (thread):
```
1/5 Your backups are probably broken.

Not missing. Not deleted. Just never tested.

Here's how to fix that:

2/5 The 3-2-1 rule:
- 3 copies of data
- 2 different media types
- 1 offsite

Simple. Non-negotiable.

3/5 Test monthly. Not yearly.

Set a calendar reminder. Actually restore something.
If it fails, you'll find out now - not during a crisis.

4/5 Encrypt everything.

Your backup drive gets stolen? Your cloud provider gets breached?
Encryption means they get nothing useful.

5/5 I've deployed this for dozens of clients.

Zero data loss incidents.

Full guide: [link]

#DevOps #Backups
```

**Facebook** (short):
```
When was the last time you actually tested your backups?

Not "assumed they work" - actually restored something.

Most people can't remember. That's the problem.
```

---

## Video Promotion Mode

When creating posts from YouTube `social-content.json`:

1. Read `03-YouTube/published/YYYY/video-slug/social-content.json`
2. Extract: title, description, hook, key_points, hashtags, video_url
3. Adapt for each platform's specs
4. Include video link appropriately per platform

**Link Placement**:
- LinkedIn: In comments (better reach) or end of post
- Twitter: Last tweet of thread
- Facebook: Native video preferred, link in comments if sharing YouTube

---

## File Organization

### Output Locations

| Platform | Location | Naming |
|----------|----------|--------|
| LinkedIn | `04-Social/linkedin/` | `YYYY-MM-DD-topic.md` |
| Twitter | `04-Social/twitter/` | `YYYY-MM-DD-topic.md` |
| Facebook | `04-Social/facebook/` | `YYYY-MM-DD-topic.md` |
| Cross-post | `04-Social/cross-post/` | `YYYY-MM-DD-topic.md` |

### Tags

- `#status/draft` - Created, not yet posted
- `#status/scheduled` - Ready to post
- `#status/published` - Posted to platform
- `#platform/linkedin`, `#platform/twitter`, `#platform/facebook`

---

## Index Management

Update `04-Social/social-index.json` after creating posts:
- Add new entry to `posts` array
- Update `stats` counters
- Track platform status

---

## Templates

For detailed structures, see:
- [[LINKEDIN_TEMPLATE]] - Professional format
- [[TWITTER_TEMPLATE]] - Tweet and thread format
- [[FACEBOOK_TEMPLATE]] - Community format

---

## Quality Checklist

Before completing any content:

- [ ] Sounds like your channel voice, not AI
- [ ] Hook grabs attention immediately
- [ ] **Logical emojis in main content** (not just links)
- [ ] Platform length specs followed
- [ ] Correct hashtag count per platform
- [ ] CTA included (question or action)
- [ ] Standard links included (in comments/final tweet)
- [ ] Featured video referenced (if applicable)
- [ ] Grammar and spelling correct
- [ ] Proper file location and naming
- [ ] Correct tags applied
- [ ] social-index.json updated

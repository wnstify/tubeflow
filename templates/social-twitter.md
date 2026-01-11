# Twitter/X Post Template

Twitter posts and threads optimized for engagement within character limits.

---

## How to Use

1. Choose between single tweet or thread format
2. Replace all `{{VARIABLE}}` placeholders with your content
3. Count characters carefully (emojis = 2 chars, URLs = 23 chars)
4. For threads, hashtags go in final tweet only

---

## Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `{{TWEET_CONTENT}}` | Main tweet text (200-250 chars) | "Docker backups don't have to be complicated..." |
| `{{THREAD_HOOK}}` | Thread opener (stop the scroll) | "I've deployed Docker for 5 years. Here's what I wish I knew on day 1:" |
| `{{POINT_X}}` | Thread point (200-250 chars each) | "First, always use volumes for data..." |
| `{{CTA}}` | Call to action | "Follow for more Docker tips" |
| `{{HASHTAG_1}}` | Primary hashtag | "#Docker" |
| `{{HASHTAG_2}}` | Secondary hashtag (threads only) | "#DevOps" |
| `{{VIDEO_URL}}` | YouTube video link | "https://youtube.com/watch?v=XXX" |
| `{{DISCORD_URL}}` | Discord community URL | "https://discord.gg/yourserver" |
| `{{GITHUB_ORG}}` | GitHub organization URL | "https://github.com/yourorg" |
| `{{DOCKER_REPO}}` | Docker Compose files repo | "https://github.com/yourorg/docker" |
| `{{TWITTER_URL}}` | Twitter profile URL | "https://twitter.com/yourhandle" |
| `{{FEATURED_VIDEO_URL}}` | Featured/guide video URL | "https://youtube.com/watch?v=XXX" |

---

## Single Tweet Template

```
{{TWEET_CONTENT}}

{{HASHTAG_1}}
```

---

## Thread Template

```
1/{{TOTAL}} {{THREAD_HOOK}}

2/{{TOTAL}} {{POINT_1}}

3/{{TOTAL}} {{POINT_2}}

4/{{TOTAL}} {{POINT_3}}

5/{{TOTAL}} {{POINT_4}}

6/{{TOTAL}} {{POINT_5}}

{{TOTAL}}/{{TOTAL}} {{CTA}}

💻 GitHub: {{GITHUB_ORG}}
🐳 Docker files: {{DOCKER_REPO}}

💬 Discord: {{DISCORD_URL}}
🐦 Follow: {{TWITTER_URL}}
🔥 Full guide: {{FEATURED_VIDEO_URL}}

{{HASHTAG_1}} {{HASHTAG_2}}
```

---

## Character Counting Rules

**CRITICAL**: Not all characters count equally.

| Element | Character Count |
|---------|-----------------|
| Regular letters/numbers | 1 each |
| Spaces, punctuation | 1 each |
| Line breaks | 1 each |
| **Emojis** | **2 each** |
| CJK characters | 2 each |
| URLs (any length) | **Always 23** |
| Media attachments | **0** (don't count) |
| @mentions (in replies) | **0** (at start only) |

### URL Examples

```
https://example.com                    = 23 chars
https://very-long-domain.com/path/page = 23 chars
```

---

## Twitter Formatting Rules

### Text Formatting

**Twitter/X HAS native bold/italic buttons.**

| Format | How to Apply |
|--------|--------------|
| **Bold** | Highlight text, click "B" button |
| *Italic* | Highlight text, click "I" button |

**Notes:**
- Available on desktop and mobile
- Formatting from external apps gets stripped on paste
- Must reapply in X's composer

### Character Limits

| Content Type | Limit | Notes |
|--------------|-------|-------|
| Standard tweet | 280 chars | All users |
| Premium tweet | 25,000 chars | X Premium subscribers |
| Optimal engagement | 200-250 chars | Leave breathing room |

### Line Breaks

- Count as 1 character each
- Improve readability (20-30% higher engagement)
- Use for visual separation

### Hashtags

| Rule | Recommendation |
|------|----------------|
| Quantity | 1-2 maximum |
| Placement | End of tweet |
| Style | #CamelCase for accessibility |
| Thread placement | Final tweet only |

**Accessibility**: Use CamelCase (#DevOps not #devops) so screen readers parse correctly.

---

## Thread Best Practices

| Element | Best Practice |
|---------|---------------|
| Length | 5-15 tweets optimal |
| Numbering | 1/, 2/, 3/ or 1/7, 2/7, 3/7 format |
| Tweet length | 200-250 chars (not full 280) |
| Hashtags | Final tweet only (1-2 max) |
| Hook | First tweet must stop scrolling |
| CTA | Last tweet with clear action |

---

## Post Type Templates

### Quick Tip Tweet

```
[Quick insight or tip in 200-250 chars]

[Optional: brief context]

#Hashtag
```

### Question Tweet

```
[Thought-provoking question]

[Brief context if needed]

#Hashtag
```

### Announcement Tweet

```
[What's new/changed]

[Key benefit]

[Link to resource]

#Hashtag
```

### Thread: Lessons Learned

```
1/7 [X] things I learned from [experience]:

(A thread)

2/7 Lesson 1: [Insight]

[Brief explanation]

3/7 Lesson 2: [Insight]

[Brief explanation]

4/7 Lesson 3: [Insight]

[Brief explanation]

5/7 Lesson 4: [Insight]

[Brief explanation]

6/7 Lesson 5: [Insight]

[Brief explanation]

7/7 The biggest takeaway:

[Summary insight]

[CTA]

#Hashtag1 #Hashtag2
```

### Thread: How-To

```
1/6 How to [achieve outcome]:

(A thread)

2/6 Step 1: [Action]

[Brief explanation]

3/6 Step 2: [Action]

[Brief explanation]

4/6 Step 3: [Action]

[Brief explanation]

5/6 Bonus tip: [Extra value]

[Brief explanation]

6/6 That's it!

[CTA + links]

#Hashtag1 #Hashtag2
```

---

## Quality Checklist

Before publishing:

**Content:**
- [ ] Single tweet: 200-250 chars (not 280)
- [ ] Thread: numbered format (1/, 2/, etc.)
- [ ] Hook stops the scroll
- [ ] Clear CTA in final tweet
- [ ] No harsh language about open-source projects
- [ ] No double dashes or em dashes

**Character Counting:**
- [ ] Emojis counted as 2 chars each
- [ ] URLs counted as 23 chars each
- [ ] Within 280 limit per tweet

**Hashtags:**
- [ ] 1-2 hashtags only
- [ ] In final tweet (threads)
- [ ] #CamelCase for accessibility

**Links:**
- [ ] All links include `https://`
- [ ] Twitter uses `twitter.com` (not `x.com`)
- [ ] GitHub, Discord links in final tweet

---

## Algorithm Notes

Twitter/X prioritizes:
- Early engagement (first hour)
- Thread engagement (likes/replies across tweets)
- Native content (text, images)
- Replies and conversations

Optimize for:
- Strong hook that stops scrolling
- Easy-to-read tweet length (not maxed out)
- Question or CTA that invites replies
- Consistent thread numbering

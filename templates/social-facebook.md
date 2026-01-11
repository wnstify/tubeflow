# Facebook Post Template

Facebook posts optimized for engagement with the new algorithm constraints.

---

## How to Use

1. Copy the template below for your Facebook post
2. Replace all `{{VARIABLE}}` placeholders with your content
3. Keep posts SHORT (40-80 chars optimal for 66% higher engagement)
4. Put ALL links in the first comment (2/month limit for link posts!)

---

## Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `{{HOOK}}` | Short attention grabber (40-80 chars) | "Docker made simple." |
| `{{CONTEXT}}` | Optional 1-2 sentences of context | "Just published a new tutorial..." |
| `{{CTA_QUESTION}}` | Question to drive comments | "What tool do you use?" |
| `{{HASHTAG_1}}` | Primary hashtag | "#Docker" |
| `{{HASHTAG_2}}` | Secondary hashtag | "#SelfHosted" |
| `{{VIDEO_URL}}` | YouTube video link | "https://youtube.com/watch?v=XXX" |
| `{{DISCORD_URL}}` | Discord community URL | "https://discord.gg/yourserver" |
| `{{BUSINESS_URL}}` | Business inquiries URL | "https://yoursite.com/contact" |
| `{{GITHUB_ORG}}` | GitHub organization URL | "https://github.com/yourorg" |
| `{{DOCKER_REPO}}` | Docker Compose files repo | "https://github.com/yourorg/docker" |
| `{{LINKEDIN_URL}}` | LinkedIn page URL | "https://linkedin.com/company/yourcompany" |
| `{{FACEBOOK_URL}}` | Facebook page URL | "https://facebook.com/yourpage" |
| `{{TWITTER_URL}}` | Twitter profile URL | "https://twitter.com/yourhandle" |
| `{{FEATURED_VIDEO_URL}}` | Featured/guide video URL | "https://youtube.com/watch?v=XXX" |

---

## Main Post Template (Short Format - Recommended)

```
{{HOOK}}

{{CTA_QUESTION}}
```

---

## Main Post Template (Extended Format)

```
{{HOOK}}

{{CONTEXT}}

{{CTA_QUESTION}}

{{HASHTAG_1}} {{HASHTAG_2}}
```

---

## First Comment Template

Post this immediately after your main post:

```
🎥 Full video: {{VIDEO_URL}}

💻 GitHub: {{GITHUB_ORG}}
🐳 Docker Compose Files: {{DOCKER_REPO}}

💬 Discord: {{DISCORD_URL}}
💼 Business: {{BUSINESS_URL}}

📘 Facebook: {{FACEBOOK_URL}}
🔗 LinkedIn: {{LINKEDIN_URL}}
🐦 Twitter: {{TWITTER_URL}}

🔥 {{FEATURED_VIDEO_TITLE}}: {{FEATURED_VIDEO_URL}}
```

---

## Facebook Formatting Rules

### Character Limits

| Zone | Limit | Importance |
|------|-------|------------|
| Above fold (mobile) | 125 chars | Only visible before "See more" |
| Optimal engagement | **40-80 chars** | **66% higher engagement** |
| Total post | 63,206 chars | Maximum allowed |

**CRITICAL**: Short posts (40-80 chars) dramatically outperform long posts.

### Text Formatting

**Facebook Pages/Profiles do NOT support native formatting.** Only Groups have native bold/italic.

| Format | How to Create | Notes |
|--------|---------------|-------|
| Bold | Unicode converter | Same as LinkedIn |
| Italic | Unicode converter | Same as LinkedIn |
| Line breaks | Enter key | May collapse multiple breaks |

**What does NOT work:**
- Any Markdown syntax
- HTML tags
- Multiple consecutive line breaks (get collapsed)
- Pasted formatting from Word/Docs

### Line Breaks

**CRITICAL**: Facebook collapses multiple consecutive line breaks.

**Workarounds:**
1. Use Unicode whitespace characters (invisible spacers)
2. Use single breaks between paragraphs
3. Accept that formatting may simplify

### Hashtags

| Rule | Recommendation |
|------|----------------|
| Quantity | 2-3 maximum (less is more) |
| Placement | End of post or naturally integrated |
| Style | #CamelCase for multi-word |
| Characters | NO special characters (breaks hashtag) |

**What breaks Facebook hashtags:**
- Spaces: `#Taco Tuesday` (only #Taco works)
- Punctuation: `#50%` (doesn't work)
- Special chars: `#C++` (doesn't work)

### Links (CRITICAL)

**WARNING**: Facebook limits most Pages to **2 external link posts per month**.

| Link Type | Limit | Strategy |
|-----------|-------|----------|
| Main post links | 2/month | Reserve for major content |
| Comment links | Unlimited | Put links in first comment |
| Meta platform links | Unlimited | Instagram, WhatsApp, FB |
| Boosted/paid posts | Unlimited | Paid bypasses limit |

**Best practice**: Always post content without links, add all links in first comment.

### Emojis

| Usage | Recommendation |
|-------|----------------|
| Quantity | Moderate (2-4 per post) |
| Type | Functional and community-focused |

**Recommended emojis:**
- Fire, trending
- Ideas
- Checkmarks
- Point to comments
- Love, appreciation
- Celebration
- Discussion, comments

---

## Post Type Templates

### Quick Announcement

```
{{SHORT_ANNOUNCEMENT}}

{{QUESTION}}
```

Example:
```
New Docker tutorial just dropped.

What should I cover next?
```

### Community Question

```
Quick question for the community:

{{QUESTION}}

#Hashtag
```

Example:
```
Quick question for the community:

What's your go-to backup solution?

#SelfHosted
```

### Video Promotion (Link in Comment)

```
{{VIDEO_TOPIC}} explained simply.

Link in first comment.

What questions do you have about {{TOPIC}}?
```

Example:
```
Docker networking explained simply.

Link in first comment.

What questions do you have about containers?
```

### Tip/Insight

```
{{QUICK_TIP}}

{{BRIEF_CONTEXT}}

#Hashtag1 #Hashtag2
```

Example:
```
Always test your backups.

I learned this the hard way.

#DevOps #Backups
```

---

## Quality Checklist

Before publishing:

**Content:**
- [ ] First 125 chars contain hook (mobile fold)
- [ ] 40-80 chars optimal (or up to 150)
- [ ] Question to drive comments
- [ ] No harsh language about open-source projects
- [ ] No double dashes or em dashes

**Formatting:**
- [ ] 2-3 hashtags maximum
- [ ] #CamelCase for multi-word hashtags
- [ ] NO links in main post
- [ ] First comment prepared with links

**Links (First Comment):**
- [ ] All links include `https://`
- [ ] Facebook uses `facebook.com` (not `fb.com`)
- [ ] Twitter uses `twitter.com` (not `x.com`)

---

## Algorithm Notes (2025-2026)

Facebook prioritizes:
- Reels and video content (native)
- Short posts (40-80 chars)
- Native content over link-outs
- Comments and engagement

Constraints:
- 2 link posts/month for non-verified Pages
- External links reduce reach
- Long posts get less engagement

Optimize for:
- Ultra-short, punchy content
- Questions that invite comments
- All links in first comment
- Native video when possible

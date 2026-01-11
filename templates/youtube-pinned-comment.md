# YouTube Pinned Comment Template

A template for pinned comments that drive engagement and provide quick access to resources.

---

## How to Use

1. Copy everything below the `---` line into your pinned comment
2. Replace all `{{VARIABLE}}` placeholders with your actual content
3. Post as first comment on your video
4. Pin the comment to keep it at the top

---

## Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `{{ENGAGEMENT_QUESTION}}` | Question related to video topic | "What backup strategy do you use?" |
| `{{BONUS_OFFER}}` | Optional extra value | "Docker Compose file available in Discord!" |
| `{{DISCORD_URL}}` | Discord community URL | "https://discord.gg/yourserver" |
| `{{BUSINESS_URL}}` | Business inquiries URL | "https://yoursite.com/contact" |
| `{{GITHUB_ORG}}` | GitHub organization URL | "https://github.com/yourorg" |
| `{{DOCKER_REPO}}` | Docker Compose files repo | "https://github.com/yourorg/docker" |
| `{{VOTING_REPO}}` | Video voting/suggestions repo | "https://github.com/yourorg/youtube" |
| `{{LINKEDIN_URL}}` | LinkedIn page URL | "https://linkedin.com/company/yourcompany" |
| `{{FACEBOOK_URL}}` | Facebook page URL | "https://facebook.com/yourpage" |
| `{{TWITTER_URL}}` | Twitter profile URL | "https://twitter.com/yourhandle" |
| `{{FEATURED_VIDEO_URL}}` | Featured/beginner guide URL | "https://youtube.com/watch?v=XXX" |
| `{{FEATURED_VIDEO_TITLE}}` | Featured video title | "Getting Started Guide" |

---

## Template (Copy Below This Line)

```
{{ENGAGEMENT_QUESTION}}

{{BONUS_OFFER}}

_______________

💻 GitHub: {{GITHUB_ORG}}
🗳️ Vote for next videos: {{VOTING_REPO}}
🐳 Docker Compose Files: {{DOCKER_REPO}}

💬 Discord: {{DISCORD_URL}}
💼 Business: {{BUSINESS_URL}}

🔗 LinkedIn: {{LINKEDIN_URL}}
📘 Facebook: {{FACEBOOK_URL}}
🐦 Twitter: {{TWITTER_URL}}

🔥 {{FEATURED_VIDEO_TITLE}}: {{FEATURED_VIDEO_URL}}
```

---

## Minimal Template (Quick Version)

For simpler pinned comments:

```
{{ENGAGEMENT_QUESTION}}

_______________

💻 GitHub: {{GITHUB_ORG}}
💬 Discord: {{DISCORD_URL}}
🐦 Twitter: {{TWITTER_URL}}
```

---

## Engagement Question Examples

Choose questions that are:
- Specific to the video topic
- Easy to answer
- Encourage sharing experiences

**Tutorial videos:**
- "What's your current setup? Drop it in the comments!"
- "Have you tried this before? What was your experience?"
- "What would you add to this configuration?"

**Comparison videos:**
- "Which option are you using? Why?"
- "What factors matter most to you when choosing?"

**Problem-solving videos:**
- "Did you run into this issue? How did you solve it?"
- "What other problems should I cover next?"

**Tool/application videos:**
- "Are you using {{TOOL_NAME}}? What's your favorite feature?"
- "What made you choose {{TOOL_NAME}} over alternatives?"

---

## Bonus Offer Examples

Add extra value to increase engagement:

**Resource offers:**
- "Docker Compose file available in Discord!"
- "Full configuration files in the GitHub repo linked below."
- "Cheat sheet PDF in the description!"

**Community offers:**
- "Join the Discord for live help with your setup!"
- "Share your implementation in our community!"

**Content offers:**
- "Part 2 coming next week, subscribe to catch it!"
- "Check the description for the complete playlist."

---

## Formatting Reminders

**CRITICAL**: YouTube comments do NOT support Markdown.

| Format | YouTube Syntax |
|--------|----------------|
| **Bold** | `*text*` |
| *Italic* | `_text_` |
| Divider | `_______________` |

**Links MUST include `https://`** to be clickable.

**Social media icon display:**
- Twitter: Use `twitter.com` (not `x.com`)
- Facebook: Use `facebook.com` (not `fb.com`)

---

## Pinned Comment Checklist

Before posting:

- [ ] Engagement question is specific and answerable
- [ ] Bonus offer adds real value (if included)
- [ ] All links tested and working
- [ ] Links include `https://`
- [ ] Twitter uses `twitter.com`
- [ ] Facebook uses `facebook.com`
- [ ] Comment is pinned after posting

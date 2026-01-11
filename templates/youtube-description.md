# YouTube Description Template

A complete, SEO-optimized YouTube video description template with all standard sections.

---

## How to Use

1. Copy everything below the `---` line into your YouTube description
2. Replace all `{{VARIABLE}}` placeholders with your actual content
3. Delete sections that don't apply (e.g., Open Source section for proprietary tools)
4. Ensure first 100-160 characters contain your hook and primary keyword

---

## Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `{{VIDEO_HOOK}}` | First 100-160 chars, hook + keyword | "Stop paying for backup services. Own your data." |
| `{{VIDEO_DESCRIPTION}}` | 2-3 sentences expanding on value | "In this video, I'll show you..." |
| `{{TIMESTAMP_X}}` | Section timestamps | "3:45 - Setting up Docker" |
| `{{TOOL_NAME}}` | Name of tool/app covered | "Restic" |
| `{{TOOL_WEBSITE}}` | Official website URL | "https://restic.net" |
| `{{TOOL_DOCS}}` | Documentation URL | "https://restic.readthedocs.io" |
| `{{TOOL_GITHUB}}` | GitHub repository URL | "https://github.com/restic/restic" |
| `{{DEVELOPER_NAME}}` | Open source developer/team | "Alexander Neumann" |
| `{{PROJECT_BENEFIT}}` | Specific benefit they provide | "reliable backups accessible to everyone" |
| `{{SPONSOR_URL}}` | GitHub Sponsors/Open Collective URL | "https://github.com/sponsors/username" |
| `{{RELATED_VIDEO_TITLE}}` | Related video title | "Docker Volume Backups" |
| `{{RELATED_VIDEO_URL}}` | Related video URL | "https://youtube.com/watch?v=XXX" |
| `{{DISCORD_URL}}` | Discord community URL | "https://discord.gg/yourserver" |
| `{{BUSINESS_URL}}` | Business inquiries URL | "https://yoursite.com/contact" |
| `{{GITHUB_ORG}}` | GitHub organization URL | "https://github.com/yourorg" |
| `{{DOCKER_REPO}}` | Docker Compose files repo | "https://github.com/yourorg/docker" |
| `{{VOTING_REPO}}` | Video voting/suggestions repo | "https://github.com/yourorg/youtube" |
| `{{LINKEDIN_URL}}` | LinkedIn page URL | "https://linkedin.com/company/yourcompany" |
| `{{FACEBOOK_URL}}` | Facebook page URL | "https://facebook.com/yourpage" |
| `{{TWITTER_URL}}` | Twitter profile URL | "https://twitter.com/yourhandle" |
| `{{REVIEWS_URL}}` | Trustpilot review page | "https://trustpilot.com/review/yoursite.com" |
| `{{FEATURED_VIDEO_URL}}` | Featured/guide video URL | "https://youtube.com/watch?v=XXX" |
| `{{HASHTAGS}}` | 5-10 relevant hashtags | "#docker #selfhosted #devops" |
| `{{CHANNEL_NAME}}` | Your channel/brand name | "YourChannel" |
| `{{CHANNEL_ABOUT}}` | About section text | "Your channel description..." |
| `{{CONFIGURE_APPLICATION_URL}}` | Application/signup URL | "https://yoursite.com/apply" |

---

## Template (Copy Below This Line)

```
{{VIDEO_HOOK}}

{{VIDEO_DESCRIPTION}}

_______________

⏱️ *TIMESTAMPS*

0:00 - Introduction
{{TIMESTAMP_1}}
{{TIMESTAMP_2}}
{{TIMESTAMP_3}}
{{TIMESTAMP_4}}
{{TIMESTAMP_RECAP}} - Recap
{{TIMESTAMP_CTA}} - CTA

_______________

🔗 *OFFICIAL LINKS*

*{{TOOL_NAME}}:*
🌐 Website: {{TOOL_WEBSITE}}
📚 Docs: {{TOOL_DOCS}}
💻 GitHub: {{TOOL_GITHUB}}

_______________

❤️ *OPEN SOURCE THANK YOU*

A huge thank you to *{{DEVELOPER_NAME}}* for creating and maintaining *{{TOOL_NAME}}* as an open-source project. {{PROJECT_BENEFIT}}

_______________

⭐ *SUPPORT THE PROJECT*

* Star on GitHub: {{TOOL_GITHUB}}
* Sponsor: {{SPONSOR_URL}}

_______________

📺 *RELATED VIDEOS*

🔥 The Ultimate Home Lab Guide: {{FEATURED_VIDEO_URL}}
{{RELATED_VIDEO_TITLE}}: {{RELATED_VIDEO_URL}}

_______________

💻 *GITHUB*

💻 GitHub: {{GITHUB_ORG}}
🗳️ Vote for next videos: {{VOTING_REPO}}
🐳 Docker Compose Files: {{DOCKER_REPO}}

_______________

💬 *CONNECT*

💬 Discord: {{DISCORD_URL}}
💼 Business: {{BUSINESS_URL}}

🔗 LinkedIn: {{LINKEDIN_URL}}
📘 Facebook: {{FACEBOOK_URL}}
🐦 Twitter: {{TWITTER_URL}}

⭐ Trustpilot: {{REVIEWS_URL}}

_______________

❤️ *ABOUT {{CHANNEL_NAME}}*

{{CHANNEL_ABOUT}}

👉 Apply for exclusive access: {{CONFIGURE_APPLICATION_URL}}

_______________

{{HASHTAGS}}
```

---

## Section Usage Guide

### Always Include
- Hook (first 100-160 chars)
- Video description
- Timestamps
- GitHub section
- Connect section
- Hashtags

### Include When Applicable
- **Official Links**: When video covers a specific tool/application
- **Open Source Thank You**: For open-source projects only
- **Support the Project**: When sponsorship options exist
- **Related Videos**: When you have relevant content
- **About Section**: For channel branding (optional)

### Remove If Not Applicable
- Official Links section (for general concept videos)
- Open Source Thank You (for proprietary tools)
- Support the Project (if no sponsorship options)
- Docker Compose Files link (for non-Docker topics)

---

## Formatting Reminders

**CRITICAL**: YouTube does NOT support Markdown. Use YouTube-native syntax:

| Format | YouTube Syntax | NOT This |
|--------|----------------|----------|
| **Bold** | `*text*` | `**text**` |
| *Italic* | `_text_` | - |
| Bullet | `* item` (at line start) | `- item` |
| Divider | `_______________` | `---` |
| Header | `⏱️ *TIMESTAMPS*` | `## Timestamps` |

**Links MUST include `https://`** to be clickable.

**Social media icon display:**
- Twitter: Use `twitter.com` (not `x.com`)
- Facebook: Use `facebook.com` (not `fb.com`)

---

## SEO Checklist

Before publishing:

- [ ] First 100-160 chars contain hook + primary keyword
- [ ] Video title keyword appears in description
- [ ] All timestamps accurate
- [ ] All links tested and working
- [ ] Bold uses single asterisk `*text*`
- [ ] Links include `https://`
- [ ] Twitter uses `twitter.com`
- [ ] Facebook uses `facebook.com`
- [ ] 5-10 relevant hashtags included

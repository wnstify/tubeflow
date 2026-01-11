# YouTube Description Formatting Reference

**CRITICAL**: YouTube does NOT support Markdown. Use YouTube-native syntax only.

---

## Text Formatting

| Format | YouTube Syntax | Example | Result |
|--------|----------------|---------|--------|
| **Bold** | `*text*` | `*TIMESTAMPS*` | **TIMESTAMPS** |
| *Italic* | `_text_` | `_emphasis_` | *emphasis* |
| ~~Strikethrough~~ | `-text-` | `-removed-` | ~~removed~~ |

### Bold Rules (CRITICAL)

```
CORRECT:
*This is bold*                    → Bold text
*SECTION HEADER*                  → Bold header

WRONG (will show asterisks):
**This is not bold**              → Shows **text**
*bold*,                           → Asterisk next to punctuation fails
*bold*.                           → Asterisk next to punctuation fails

WORKAROUND for punctuation:
*bold* ,                          → Add space before punctuation
*bold* .                          → Add space before punctuation
```

---

## Lists

### Bullet Points

Use `*`, `-`, or `+` at START of line followed by SPACE:

```
* First item
* Second item
* Third item
```

or

```
- First item
- Second item
```

**CRITICAL**: The `*` character does DOUBLE DUTY:
- `*text*` = **bold** (wrapping text)
- `* text` = bullet (start of line + space)

### Numbered Lists (Manual Only)

YouTube does NOT auto-number. Type numbers manually:

```
1. First step
2. Second step
3. Third step
```

---

## Dividers

```
_______________          (underscores - RECOMMENDED)
---------------          (hyphens)
```

---

## Links

### Clickable Links

MUST include `https://` prefix:

```
CORRECT (clickable):
https://github.com/user/repo

WRONG (plain text, not clickable):
github.com/user/repo
www.github.com/user/repo
```

### Social Media Icons

YouTube displays icons for recognized platforms. Use EXACT formats:

| Platform | USE THIS | NOT THIS |
|----------|----------|----------|
| Twitter/X | `https://twitter.com/username` | `https://x.com/username` |
| Facebook | `https://facebook.com/pagename` | `https://fb.com/...` or `https://m.facebook.com/...` |
| LinkedIn | `https://linkedin.com/company/name` | Works as-is |
| YouTube | `https://youtube.com/...` | Works as-is |
| Discord | `https://discord.gg/...` | Works as-is |

**Facebook Requirements**:
- Must use `facebook.com` domain
- Page must have username set (not PHP ID like `profile.php?id=123`)

### Link Truncation

YouTube auto-truncates links after ~37 characters with `...`
- Use URL shorteners (bit.ly, tinyurl) for cleaner display
- Or accept truncation for long URLs

---

## Section Headers

YouTube has NO header hierarchy. Create visual headers with:

```
OPTION 1 - Emoji + Bold:
⏱️ *TIMESTAMPS*

OPTION 2 - Emoji + Caps:
🔗 OFFICIAL LINKS

OPTION 3 - Bold only:
*Resources*
```

---

## Character Limits

| Zone | Limit | Importance |
|------|-------|------------|
| Above the fold | 100-160 chars | **CRITICAL** - Only visible text before "Show more" |
| Total description | 5,000 chars | Full description limit |

**First 100-160 characters MUST**:
- Hook the viewer
- Include primary keyword
- Communicate value proposition

---

## Emojis

- Display correctly on all platforms
- Great for section markers
- Use strategically (10-20% of content max)
- Do NOT overuse

**Recommended section emojis**:
```
⏱️  Timestamps
🔗  Links / Official Links
❤️  Acknowledgments / Thank you
⭐  Support / Star on GitHub
📺  Related Videos
💬  Connect / Community
🔥  Featured / Hot content
💻  GitHub / Code
🌐  Website
📚  Documentation
🐳  Docker
```

---

## What Does NOT Work

| Markdown | YouTube | Result |
|----------|---------|--------|
| `# Header` | Not supported | Shows `# Header` as text |
| `## Header` | Not supported | Shows `## Header` as text |
| `**bold**` | Not supported | Shows `**bold**` as text |
| `[text](url)` | Not supported | Shows `[text](url)` as text |
| `<b>bold</b>` | Not supported | Shows `<b>bold</b>` as text |

---

## Complete Description Structure

```
[HOOK - First 100-160 chars with keyword and value proposition. This is the ONLY text visible before "Show more".]

[2-3 sentences expanding on what viewer will learn/achieve.]

_______________

⏱️ *TIMESTAMPS*

0:00 - Introduction
1:30 - [Section 1]
5:00 - [Section 2]
10:00 - [Section 3]
15:00 - Recap & CTA

_______________

🔗 *OFFICIAL LINKS*

*[Tool Name]:*
🌐 Website: https://example.com
📚 Documentation: https://docs.example.com
💻 GitHub: https://github.com/org/repo

_______________

❤️ *OPEN SOURCE THANK YOU*

A huge thank you to *[Developer Name]* for creating and maintaining *[Project]* as an open-source project. [Specific benefit statement].

_______________

⭐ *SUPPORT THE PROJECT*

* Star on GitHub: https://github.com/org/repo
* Sponsor: https://github.com/sponsors/developer

_______________

📺 *RELATED VIDEOS*

🔥 [Video Title]: https://youtube.com/watch?v=XXX
📚 [Another Video]: https://youtube.com/watch?v=YYY

_______________

💻 *GITHUB*

💻 GitHub: https://github.com/yourorg
🗳️ Vote for next videos: https://github.com/yourorg/youtube
🐳 Docker Compose Files: https://github.com/yourorg/docker

_______________

💬 *CONNECT*

💬 Discord: https://discord.gg/yourserver
💼 Business: https://yoursite.com/contact

🔗 LinkedIn: https://linkedin.com/company/yourcompany
📘 Facebook: https://facebook.com/yourpage
🐦 Twitter: https://twitter.com/yourhandle

_______________

#hashtag1 #hashtag2 #hashtag3 #hashtag4 #hashtag5
```

---

## Complete Pinned Comment Structure

```
[Engagement question related to video topic]

[Optional: Bonus offer or extra tip]

_______________

💻 GitHub: https://github.com/yourorg
🗳️ Vote for next videos: https://github.com/yourorg/youtube
🐳 Docker Compose Files: https://github.com/yourorg/docker

💬 Discord: https://discord.gg/yourserver
💼 Business: https://yoursite.com/contact

🔗 LinkedIn: https://linkedin.com/company/yourcompany
📘 Facebook: https://facebook.com/yourpage
🐦 Twitter: https://twitter.com/yourhandle
```

---

## Quick Validation Checklist

Before publishing, verify:

- [ ] First 100-160 chars contain hook + keyword
- [ ] Bold uses single asterisk `*text*`
- [ ] Bullet points use `* item` (asterisk + space)
- [ ] All links include `https://`
- [ ] Twitter link uses `twitter.com` (not `x.com`)
- [ ] Facebook link uses `facebook.com` (not `fb.com`)
- [ ] Section dividers use `_______________`
- [ ] No markdown headers (`#`, `##`)
- [ ] No markdown bold (`**text**`)
- [ ] Emojis used strategically, not spam

# YouTube Idea Template

Quick capture format for video ideas. Minimal fields to reduce friction when inspiration strikes.

---

## How to Use

1. Create a new file when you have a video idea
2. Fill in at least the Quick Capture fields (Hook, Problem, Duration)
3. Expand to Full Format when ready to develop further
4. Run through validation checklist before developing into a script

---

## Quick Capture (Minimum Viable Idea)

When you're in a hurry, capture at minimum:

```markdown
---
title: "{{WORKING_TITLE}}"
date: {{DATE}}
status: idea
platform: youtube
---

# {{WORKING_TITLE}}

**Hook**: {{OPENING_LINE}}
**Problem**: {{PAIN_POINT}}
**Duration**: {{ESTIMATE}}
```

---

## Full Idea Format

For more developed ideas:

```markdown
---
title: "{{WORKING_TITLE}}"
date: {{DATE}}
status: idea
platform: youtube
type: {{VIDEO_TYPE}}
topic: [{{TOPIC_1}}, {{TOPIC_2}}]
---

# {{WORKING_TITLE}}

## Hook
{{OPENING_LINE}}

## Core Problem
{{PAIN_POINT}}

## Solution Preview
{{WHAT_VIEWERS_LEARN}}

## Target Audience
{{WHO_NEEDS_THIS}}

## Key Points (3-5)
1. {{POINT_1}}
2. {{POINT_2}}
3. {{POINT_3}}

## Estimated Duration
{{DURATION_ESTIMATE}}

## Why Now?
{{RELEVANCE_REASON}}

## Notes
{{ADDITIONAL_THOUGHTS}}
```

---

## Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `{{WORKING_TITLE}}` | Draft video title | "Docker Backup Strategies" |
| `{{DATE}}` | Capture date | "2026-01-15" |
| `{{VIDEO_TYPE}}` | Content type | "tutorial", "comparison", "guide" |
| `{{TOPIC_1}}` | Primary topic tag | "docker" |
| `{{OPENING_LINE}}` | Hook that grabs attention | "Your containers are one crash away from disaster" |
| `{{PAIN_POINT}}` | What problem does this solve? | "Most Docker users have no backup strategy" |
| `{{WHAT_VIEWERS_LEARN}}` | Outcome/skill they gain | "Set up automated, encrypted backups in 15 min" |
| `{{WHO_NEEDS_THIS}}` | Target audience | "Self-hosters running Docker on a single server" |
| `{{DURATION_ESTIMATE}}` | Video length | "10-15 minutes" |
| `{{RELEVANCE_REASON}}` | Why is this timely? | "Common question in Discord, no good tutorials exist" |

---

## Idea Validation Checklist

Before developing into a full script:

- [ ] Solves a real problem (not just interesting to me)
- [ ] Fits channel brand and content pillars
- [ ] Not already covered in existing videos
- [ ] Can demonstrate practically, not just explain
- [ ] Audience would search for this
- [ ] I have the expertise to cover this well

---

## Idea Sources

Common triggers for good video ideas:

| Source | Example |
|--------|---------|
| Audience question | "How do I backup my Docker volumes?" |
| Community discussion | Repeated questions in Discord/forums |
| Competitor gap | Topic others explain poorly |
| Tool update | New feature in popular software |
| Personal solution | "I just built this for a client" |
| Trend | Rising interest in topic |
| Mistake | "I wish I knew this when starting" |
| Comparison | "Tool A vs Tool B" discussions |

---

## Status Flow

Ideas progress through these statuses:

```
idea → draft → review → scheduled → published
```

| Status | Meaning |
|--------|---------|
| `idea` | Initial concept, needs validation |
| `draft` | Being developed into full script |
| `review` | Script complete, ready for review |
| `scheduled` | Approved, filming scheduled |
| `published` | Video is live |

---

## File Naming Convention

`YYYY-MM-DD-topic-slug.md`

Examples:
- `2026-01-15-docker-backup-strategies.md`
- `2026-01-18-zero-trust-small-business.md`
- `2026-01-20-coolify-v4-migration.md`

---

## Video Type Reference

| Type | Description | Typical Length |
|------|-------------|----------------|
| `tutorial` | Step-by-step how-to | 10-20 min |
| `comparison` | A vs B analysis | 8-15 min |
| `guide` | Comprehensive overview | 15-30 min |
| `tip` | Quick single tip | 3-8 min |
| `announcement` | News/updates | 5-10 min |
| `review` | Tool/product review | 10-20 min |
| `behind-the-scenes` | Process/workflow | 8-15 min |

---

## Quick Development Path

When ready to develop an idea:

1. **Validate**: Run through validation checklist
2. **Research**: Gather official docs, GitHub links, alternatives
3. **Outline**: Expand key points into sections
4. **Script**: Use the Script Template for full development
5. **Describe**: Create description using Description Template
6. **Thumbnail**: Design thumbnail with text from script

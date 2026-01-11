# YouTube Script Template

A complete video script structure with hook formulas, section templates, and visual cues.

---

## How to Use

1. Create a new file using the Script File Format below
2. Fill in the frontmatter with video metadata
3. Write each section following the structure
4. Include `[Visual:]` cues for editing
5. Complete the thumbnail text section
6. Run through quality checklist before filming

---

## Script File Format

```markdown
---
title: "{{VIDEO_TITLE}}"
date: {{DATE}}
status: draft
platform: youtube
type: {{VIDEO_TYPE}}
topic: [{{TOPIC_1}}, {{TOPIC_2}}]
estimated_duration: "{{DURATION}}"
---

# {{VIDEO_TITLE}}

## Hook (0:00-0:30)
{{HOOK_CONTENT}}

[Visual: {{OPENING_VISUAL}}]

---

## Introduction (0:30-1:00)
{{INTRO_CONTENT}}

[Visual: {{INTRO_VISUAL}}]

---

## Main Content

### Section 1: {{SECTION_1_TITLE}} (1:00-{{SECTION_1_END}})
{{SECTION_1_CONTENT}}

[Visual: {{SECTION_1_VISUAL}}]

**Key point**: {{SECTION_1_TAKEAWAY}}

### Section 2: {{SECTION_2_TITLE}} ({{SECTION_2_START}}-{{SECTION_2_END}})
{{SECTION_2_CONTENT}}

[Visual: {{SECTION_2_VISUAL}}]

**Pro tip**: {{SECTION_2_TIP}}

### Section 3: {{SECTION_3_TITLE}} ({{SECTION_3_START}}-{{SECTION_3_END}})
{{SECTION_3_CONTENT}}

[Visual: {{SECTION_3_VISUAL}}]

**Common mistake**: {{SECTION_3_MISTAKE}}

---

## Recap ({{RECAP_START}}-{{RECAP_END}})
Three things to remember:
1. {{TAKEAWAY_1}}
2. {{TAKEAWAY_2}}
3. {{TAKEAWAY_3}}

---

## CTA & Outro ({{OUTRO_START}}-end)
{{CTA_CONTENT}}

{{NEXT_VIDEO_TEASE}}

[Visual: End screen with subscribe button]

---

## Thumbnail Text

**BOLD TEXT (3-5 words)**:
{{THUMBNAIL_BOLD}}

**Description (13-18 words)**:
{{THUMBNAIL_DESCRIPTION}}
```

---

## Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `{{VIDEO_TITLE}}` | Full video title | "Docker Backup Strategies" |
| `{{DATE}}` | Creation date | "2026-01-15" |
| `{{VIDEO_TYPE}}` | Content type | "tutorial", "comparison", "guide" |
| `{{TOPIC_1}}` | Primary topic tag | "docker" |
| `{{DURATION}}` | Estimated length | "12:30" |
| `{{HOOK_CONTENT}}` | Opening attention grabber | Pattern interrupt or question |
| `{{SECTION_X_TITLE}}` | Section heading | "Setting Up Restic" |
| `{{THUMBNAIL_BOLD}}` | 3-5 word thumbnail text | "BACKUP OR LOSE IT" |
| `{{THUMBNAIL_DESCRIPTION}}` | 13-18 word description | "The exact backup strategy..." |

---

## Hook Formulas

### Pattern Interrupt
> "Everyone tells you to [common advice]. They're wrong. Here's why."

### Question Hook
> "Have you ever wondered why [common frustration]? There's a reason, and a fix."

### Result Preview
> "By the end of this video, you'll have [specific outcome]. Let me show you how."

### Story Opening
> "Last week, a client asked me [question]. My answer surprised them."

### Problem-Agitation
> "Your [thing] is probably [problem]. And it's costing you [consequence]."

---

## Section Templates

### Explanation Section
```markdown
### [Concept Name] (X:XX-X:XX)

Here's the thing about [concept]:

[Simple explanation, no jargon]

[Visual: Diagram showing concept]

In practice, this means [practical implication].

**Key point**: [One sentence summary]
```

### Demonstration Section
```markdown
### [Task Name] (X:XX-X:XX)

Let me show you how to [task].

[Visual: Screen recording starts]

First, [step 1].

[Visual: Highlight relevant area]

Then [step 2].

[Visual: Show result]

**Pro tip**: [Practical advice that saves time or prevents errors]
```

### Comparison Section
```markdown
### [Option A] vs [Option B] (X:XX-X:XX)

You might be wondering which to use. Here's the difference:

[Visual: Side-by-side comparison]

**[Option A]**: Best when [use case]. [Brief explanation].

**[Option B]**: Better for [different use case]. [Brief explanation].

My recommendation? [Clear guidance based on audience needs].
```

---

## Timestamp Format

Always include timestamps in this format:

```
0:00 - Introduction
0:30 - [Section 1 Title]
3:45 - [Section 2 Title]
7:20 - [Section 3 Title]
10:15 - Recap & Next Steps
```

---

## Visual Cue Reference

| Cue | Use For |
|-----|---------|
| `[Visual: Screen recording]` | Terminal, browser, IDE demos |
| `[Visual: Diagram]` | Explaining architecture, flow |
| `[Visual: Code snippet]` | Highlighting specific code |
| `[Visual: Comparison]` | Before/after, A vs B |
| `[Visual: Result]` | Final outcome, working demo |
| `[Visual: B-roll]` | Generic footage for narration |

---

## Word Count Reference

| Duration | Target Words | Sections |
|----------|--------------|----------|
| 5 min | 700-800 | 3-4 |
| 10 min | 1400-1600 | 5-6 |
| 15 min | 2100-2400 | 7-8 |
| 20 min | 2800-3200 | 8-10 |

---

## Thumbnail Text Guidelines

**BOLD TEXT (3-5 words):**
- ALL CAPS for impact
- Create urgency or curiosity
- Numbers work well
- Examples: "STOP DOING THIS", "5 MINUTE FIX", "FREE FOREVER"

**Description (13-18 words):**
- Expand on the benefit
- Answer "what will I get?"
- Be specific about outcome
- Example: "The exact backup strategy I use for my clients that has never failed"

---

## Quality Checklist

Before marking script complete:

- [ ] Hook creates curiosity in first 10 seconds
- [ ] Each section has clear `[Visual:]` cues
- [ ] Practical examples, not just theory
- [ ] Pro tips and common mistakes included
- [ ] Recap has exactly 3 key takeaways
- [ ] CTA is clear and specific
- [ ] Thumbnail text included (3-5 bold + 13-18 description)
- [ ] Estimated duration matches content length
- [ ] Content sounds natural when read aloud
- [ ] No harsh language about open-source projects
- [ ] No double dashes or em dashes

---

## Video Type Reference

| Type | Description | Structure |
|------|-------------|-----------|
| `tutorial` | Step-by-step how-to | Hook, Setup, Steps, Verification, Recap |
| `comparison` | A vs B analysis | Hook, Criteria, Side-by-side, Recommendation |
| `guide` | Comprehensive overview | Hook, Concept, Deep-dives, Best Practices |
| `tip` | Quick value | Hook, Problem, Solution, Bonus tip |
| `announcement` | News/updates | Hook, What's new, Impact, Next steps |

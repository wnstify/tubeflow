---
name: youtube-research
description: Comprehensive YouTube research workflow with parallel agents for topic analysis, competitor research, SEO, and community insights. Use when user wants to research before creating YouTube content.
---

# YouTube Research Workflow Skill

Comprehensive research system for YouTube video/series planning. Uses 5 specialized agents to gather, analyze, and synthesize research into actionable content strategy.

---

## CRITICAL: Direct Agent Spawning

**You (the main Claude agent) MUST spawn the gatherer and strategist agents directly.**

Agents cannot spawn subagents, so there is no orchestrator. You handle the orchestration by:
1. Creating folders
2. Spawning 4 gatherers in parallel
3. Waiting for completion
4. Spawning the strategist

---

## Architecture

```
/youtube research "Topic"
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

---

## Agent Summary

| Agent | Model | Purpose | Token Limit |
|-------|-------|---------|-------------|
| `@yt-topic-gatherer` | Haiku | Subject matter, docs, features | 1,000 |
| `@yt-competitor-gatherer` | Haiku | YouTube videos, gaps | 1,000 |
| `@yt-seo-gatherer` | Haiku | Keywords, trends, titles | 800 |
| `@yt-community-gatherer` | Haiku | Reddit, forums, questions | 800 |
| `@yt-research-strategist` | Opus | Synthesis, series structure | N/A |

**Total: 5 agents** (4 gatherers + 1 strategist)

---

## Workflow Phases

### Phase 1: Parallel Gathering (~2-3 min)

**Main Claude agent spawns 4 Haiku agents simultaneously** (single message with 4 Task calls):

| Agent | Researches | Output Summary |
|-------|------------|----------------|
| Topic | Official docs, features, complexity | topic-summary.md |
| Competitor | Existing YouTube videos, gaps | competitor-summary.md |
| SEO | Keywords, trends, titles | seo-summary.md |
| Community | Reddit, forums, questions | community-summary.md |

Each agent:
1. Gathers comprehensive raw data
2. Saves raw data to `raw/` folder
3. Creates condensed summary under token limit
4. Saves summary to `summaries/` folder

### Phase 2: Strategic Synthesis (~3-5 min)

**After all 4 gatherers complete**, main Claude agent spawns Opus strategist:

1. Reads all 4 summaries (~3,200 tokens)
2. Uses sequential thinking for complex analysis
3. Determines single video vs series
4. Creates `research-pack.md`
5. Creates `series-structure.md` (if series)

---

## Output Structure

```
03-YouTube/research/YYYY-MM-DD-[slug]/
├── research-pack.md        # Strategic recommendations (always)
├── series-structure.md     # Episode breakdown (if series)
├── summaries/              # Condensed inputs (~3,200 tokens)
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

---

## Research Pack Contents

| Section | Description |
|---------|-------------|
| Executive Summary | 4-5 bullet points + recommendation |
| Topic Overview | Features, complexity, prerequisites |
| Competitor Landscape | Existing videos, gaps, differentiation |
| Target Audience | Who, what they know, what they want |
| SEO Strategy | Keywords, title suggestions, tags |
| Community Insights | Questions to answer, pain points |
| Content Recommendation | Single video or series + reasoning |
| Production Notes | Demo requirements, difficulty score |
| Next Steps | What to do after research |

---

## Series Detection Criteria

**Recommend Series When:**
- Topic has 3+ distinct sub-topics
- Each sub-topic needs 10+ minutes coverage
- Clear learning progression exists
- Community has questions at multiple levels
- Too complex for single video

**Recommend Single Video When:**
- Topic is focused and contained
- Can cover in 15-30 minutes
- No natural breaking points
- Simple enough for one session

---

## Tools Used by Agents

### Topic Gatherer
- Perplexity (search, ask)
- Context7 (library docs)
- DeepWiki (GitHub projects)
- WebFetch

### Competitor Gatherer
- Perplexity (search)
- WebSearch
- WebFetch

### SEO Gatherer
- Perplexity (search)
- WebSearch

### Community Gatherer
- Perplexity (search)
- WebSearch
- WebFetch

### Strategist
- Sequential Thinking (complex analysis)
- Read, Write, Glob

---

## Usage Examples

```bash
# Research for potential series
/youtube research "XCloud tutorial series"

# Research for single video
/youtube research "Docker networking basics"

# Research for advanced topic
/youtube research "Kubernetes security hardening"

# Research for beginner content
/youtube research "Self-hosting for beginners"
```

---

## Timing Expectations

| Phase | Agents | Duration |
|-------|--------|----------|
| Setup | Main agent | ~10 sec |
| Phase 1 | 4 Haiku (parallel) | ~2-3 min |
| Phase 2 | 1 Opus | ~3-5 min |
| **Total** | 5 agents | **~5-8 min** |

---

## Integration with YouTube Workflow

```
/youtube research "Docker Security"
    ↓
review: research-pack.md
    ↓
/youtube full "Docker Security"  (or Part 1 if series)
    ↓
/youtube publish "Docker Security"
    ↓
/social video "docker-security"
```

---

## Token Efficiency

**Problem Solved**: If 4 gatherers each return 10,000 tokens, strategist receives 40,000+ tokens - too much.

**Solution**: Each gatherer summarizes to strict token limits:
- Topic: 1,000 tokens max
- Competitor: 1,000 tokens max
- SEO: 800 tokens max
- Community: 800 tokens max
- **Total to strategist: ~3,600 tokens**

Raw data preserved in `raw/` folder for reference if needed.

---

## Quality Checklist

Before research is complete:

- [ ] Folders created (summaries/ and raw/)
- [ ] All 4 gatherers ran in parallel (single message)
- [ ] All 4 summary files exist
- [ ] Summaries are within token limits
- [ ] Raw data preserved
- [ ] research-pack.md is comprehensive
- [ ] Series detection reasoning is clear
- [ ] series-structure.md exists (if series)
- [ ] Next steps are actionable

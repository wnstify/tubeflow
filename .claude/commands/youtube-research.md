---
description: Comprehensive YouTube research workflow - topic analysis, competitors, SEO, community insights
argument-hint: "Topic or Series Name"
allowed-tools: Task, Read, Write, Glob, Bash
---

# /youtube research Command

Comprehensive research workflow for YouTube video/series planning.

---

## CRITICAL: Direct Agent Spawning

**You (the main Claude agent) MUST spawn the gatherer and strategist agents directly.**

Agents cannot spawn subagents, so there is no orchestrator. You handle the orchestration.

---

## Execution Steps

### Step 1: Setup

1. Parse the topic from `$1`
2. Create slug: lowercase, hyphens, no special chars (e.g., "XCloud Tutorial Series" → "xcloud-tutorial-series")
3. Get today's date: YYYY-MM-DD
4. Create output folders using Bash:

```bash
mkdir -p "03-YouTube/research/YYYY-MM-DD-[slug]/summaries"
mkdir -p "03-YouTube/research/YYYY-MM-DD-[slug]/raw"
```

### Step 2: Phase 1 - Spawn 4 Gatherers IN PARALLEL

**CRITICAL: You MUST spawn all 4 agents in a SINGLE message with 4 Task tool calls.**

This is NOT optional. Spawning them sequentially defeats the purpose.

```
Task 1:
  description: "Research topic details"
  subagent_type: "yt-topic-gatherer"
  model: "haiku"
  prompt: "Research topic: [TOPIC].

    Output folder: 03-YouTube/research/YYYY-MM-DD-[slug]

    Save your findings:
    1. Raw data: raw/topic-raw.md (all gathered information)
    2. Summary: summaries/topic-summary.md (condensed, under 1000 tokens)

    Follow your agent instructions exactly."

Task 2:
  description: "Research YouTube competitors"
  subagent_type: "yt-competitor-gatherer"
  model: "haiku"
  prompt: "Research YouTube competitors for: [TOPIC].

    Output folder: 03-YouTube/research/YYYY-MM-DD-[slug]

    Save your findings:
    1. Raw data: raw/competitor-raw.md (all gathered information)
    2. Summary: summaries/competitor-summary.md (condensed, under 1000 tokens)

    Follow your agent instructions exactly."

Task 3:
  description: "Research SEO keywords"
  subagent_type: "yt-seo-gatherer"
  model: "haiku"
  prompt: "Research SEO and keywords for: [TOPIC].

    Output folder: 03-YouTube/research/YYYY-MM-DD-[slug]

    Save your findings:
    1. Raw data: raw/seo-raw.md (all gathered information)
    2. Summary: summaries/seo-summary.md (condensed, under 800 tokens)

    Follow your agent instructions exactly."

Task 4:
  description: "Research community discussions"
  subagent_type: "yt-community-gatherer"
  model: "haiku"
  prompt: "Research community discussions for: [TOPIC].

    Output folder: 03-YouTube/research/YYYY-MM-DD-[slug]

    Save your findings:
    1. Raw data: raw/community-raw.md (all gathered information)
    2. Summary: summaries/community-summary.md (condensed, under 800 tokens)

    Follow your agent instructions exactly."
```

### Step 3: Verify Phase 1 Completion

After all 4 Task calls return, verify files exist:

```bash
ls -la "03-YouTube/research/YYYY-MM-DD-[slug]/summaries/"
```

Expected: 4 summary files. If any missing, report which agent failed.

### Step 4: Phase 2 - Spawn Strategist

**Only after Phase 1 completes**, spawn the strategist:

```
Task:
  description: "Synthesize research into strategy"
  subagent_type: "yt-research-strategist"
  model: "opus"
  prompt: "Synthesize all research for: [TOPIC].

    Research folder: 03-YouTube/research/YYYY-MM-DD-[slug]

    Read all 4 summaries from the summaries/ folder:
    - topic-summary.md
    - competitor-summary.md
    - seo-summary.md
    - community-summary.md

    Use sequential thinking for complex analysis.
    Determine if this should be a single video or series.

    Create output files in the research folder root:
    - research-pack.md (always)
    - series-structure.md (only if series detected)

    Follow your agent instructions exactly."
```

### Step 5: Report Completion

After strategist completes, report:

```markdown
## YouTube Research Complete

**Topic**: [Topic]
**Folder**: 03-YouTube/research/YYYY-MM-DD-[slug]/

### Files Created

| File | Description |
|------|-------------|
| research-pack.md | Strategic recommendations |
| series-structure.md | Episode breakdown (if series) |
| summaries/ | 4 condensed research files |
| raw/ | 4 full data files |

### Next Steps

1. Review: `03-YouTube/research/YYYY-MM-DD-[slug]/research-pack.md`
2. Create content: `/youtube full "[Topic]"`
```

---

## Output Structure

```
03-YouTube/research/YYYY-MM-DD-[slug]/
├── research-pack.md        # Strategic output (Opus)
├── series-structure.md     # Episode breakdown (if series)
├── summaries/              # Summarized inputs (~3,200 tokens)
│   ├── topic-summary.md
│   ├── competitor-summary.md
│   ├── seo-summary.md
│   └── community-summary.md
└── raw/                    # Full data for reference
    ├── topic-raw.md
    ├── competitor-raw.md
    ├── seo-raw.md
    └── community-raw.md
```

---

## Usage Examples

```
/youtube research "XCloud tutorial series"
/youtube research "Docker networking fundamentals"
/youtube research "Kubernetes security best practices"
```

---

## Timing

| Phase | Duration |
|-------|----------|
| Phase 1 (4 parallel agents) | ~2-3 minutes |
| Phase 2 (strategist) | ~3-5 minutes |
| **Total** | **~5-8 minutes** |

---

## Error Handling

**If a gatherer fails:**
- Report which agent failed
- List which summaries were created
- Suggest re-running or manual investigation

**If strategist fails:**
- Report that Phase 1 succeeded
- Note summaries are available for manual review

---

## Agent Architecture

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
```

**Total: 5 agents** (4 gatherers + 1 strategist)

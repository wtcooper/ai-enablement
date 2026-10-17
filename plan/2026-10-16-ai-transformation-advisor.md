# Plan: AI transformation advisor v1 (from intent 2026-10-16, spec revision 5)

Date: 2026-10-17 · Status: draft, revised after the research pilot ([retro](../research/runs/pilot/RETRO.md)) and wave 1 ([retro](../research/runs/wave1/RETRO.md)).

> Stage 3 (Build) artifact. It says which files change, in what order, the risks, and how we prove
> each step works. The *what* is in [`spec/2026-10-16-ai-transformation-advisor.md`](../spec/2026-10-16-ai-transformation-advisor.md).

## What ships and what doesn't

The **product** is only what is inside `plugins/transformation-advisor/`. That means the
orchestration skill, the method logic, the archetype packs, the backbone library and the reference
files they need. Everything else in the repo is how we build, test and maintain it. Research is a
**build activity**: we do it once, deeply, to write the archetype packs and method files, and rerun it
to refresh them. The research tooling and its raw output never ship.

| Ships (the product) | Build-only (this repo) |
|---|---|
| `plugins/transformation-advisor/**` | `intent/`, `spec/`, `plan/`, `docs/` |
| The marketplace index files (needed for install) | `research/`: briefs, raw subagent output, source logs |
| | `evals/`: scenarios, results |
| | `scripts/`: validators, build helpers |
| | `templates/workspace/`: a starter workspace users can copy (documentation, not loaded by the skill) |

## Files that change

```
ai-enablement/
├── .claude-plugin/marketplace.json            # M2
├── .agents/plugins/marketplace.json           # M2
├── .github/plugin/marketplace.json            # M2
├── .cursor-plugin/marketplace.json            # M2
├── plugins/transformation-advisor/
│   ├── plugin.json                            # M2  Agent Plugins 1.0
│   ├── .claude-plugin/plugin.json             # M2
│   ├── .cursor-plugin/plugin.json             # M2
│   └── skills/transformation-advisor/
│       ├── SKILL.md                           # M2 stub → M5 full
│       └── references/
│           ├── method/                        # M5 (from stream M research)
│           ├── library/                       # M5 (from stream B research)
│           ├── archetypes/                    # M1 pilot module → M4 all three archetypes
│           ├── briefs/                        # M5 runtime subagent briefs
│           ├── schemas/                       # M0
│           └── templates/                     # M5
├── research/
│   ├── README.md                              # M0 how the research program runs
│   ├── briefs/                                # M0 templates → M1 pilot → M3/M4 all briefs
│   └── runs/<wave>/                           # raw subagent output, kept for traceability
├── scripts/
│   └── validate.py                            # M0 schema, size and link checks
├── evals/                                     # M6
├── templates/workspace/                       # M5
└── README.md                                  # M7 install instructions per client
```

## Order of work

### M0. Foundations (small) · **done**

Delivered: `scripts/validate.py`, `references/schemas/vocabulary.yaml` and the brief templates. The
full JSON schemas for plan and opportunities files are still to do; they come with M5.


- Turn the spec's schemas into files: use-case, plan, opportunities.
- Write `research/README.md` and the brief templates: landscape scan, deep-dive angle, cross-cutting,
  synthesis, verifier.
- Write `scripts/validate.py`. It checks:
  - YAML against the schemas
  - `SKILL.md` ≤ 500 lines (target ≤ 400)
  - each reference file ≤ 300 lines, with a table of contents when over 100
  - every pointer in `SKILL.md` and each index file resolves
  - every use case cites at least one dated source

### M1. Research pilot: assurance → controls testing · **done**

**Result:**

- 25 verified use cases, 64% graded A or B
- a 293-line module file
- 0 validator errors
- about 2.15M tokens, about 67 minutes of wall-clock time

The pilot led to these changes, applied to the briefs, vocabulary, validator and spec (revision 5):

- reading the pages themselves through `curl`
- precision rules
- provenance and access fields
- `ladder` + `change_scope` replacing "lens"
- shared source keys
- module routing
- deep dives scaled to each module's evidence density

See the [retro](../research/runs/pilot/RETRO.md).

The original pilot plan:


This calibrates depth, briefs and schema before the large fan-out.

1. **Landscape scan** for assurance (1 agent). Output: `research/runs/pilot/landscape-assurance.md`,
   a draft of `sources.md`.
2. **Deep dives** on controls testing (3 agents in parallel): practice, discourse, governance &
   evidence.
3. **Synthesis** (1 agent). Output: draft `archetypes/assurance/modules/controls-testing.md` and
   `use-cases/controls-testing.yaml`.
4. **Verification** (1 agent). Checks every claim against its source, sets evidence grades, removes
   anything unsupported.
5. **Retro.** Review depth, source quality, evidence mix, time and token cost, and gaps. **Update this
   plan, the briefs and, if needed, the spec.**

That is 6 agents in total.

### M2. Install skeleton and client verification (can run alongside M1) · **Claude Code done; other clients with the owner**

Status: built with the full skill rather than a stub. Marketplaces and manifests pass `claude plugin validate
--strict`; the plugin installs from a local clone in Claude Code 2.1.302 and the skill triggers and reads its
references. The per-client checklist is [`docs/install-testing.md`](../docs/install-testing.md).

- Marketplace indexes and manifests for every target client (spec §7.5).
- A stub `SKILL.md` that:
  - reads one reference file and one index → archetype file (checks progressive disclosure and the
    two-step index lookup)
  - asks for a two-item subagent fan-out with the tool-agnostic wording (checks delegation, and the
    inline fallback)
- A smoke-test checklist per client: install, skill triggers, reference read, subagents spawn. Claude
  Code is tested here. Codex / ChatGPT desktop, Cursor and Copilot CLI / VS Code need the owner to
  run the checklist on a machine with those tools.

### M3. Research waves: method and backbone

| Stream | Research agents | Synthesis | Verify | Total |
|---|---|---|---|---|
| **M: Method** (8 topics, see below) | 8 | 2 | 2 | 12 |
| **B: Backbone** (11 patterns, 10 function cards, journey stages; grouped 2–3 per agent) | 10 | 2 | 2 | 14 |

The eight method topics are:

1. lean and Six Sigma for knowledge work
2. PE value creation, the 100-day plan and program office practice
3. AI transformation frameworks and evidence
4. agentic workflow redesign
5. AI maturity models
6. change, workforce and fear
7. value measurement and business cases
8. process-discovery interviewing

### M4. Research waves: archetypes

These run in order: assurance (the rest of it), then tax, then professional services. Each archetype
uses the same recipe.

| Step | Agents per archetype |
|---|---|
| Landscape scan | 1 |
| Module deep dives: 3 angles for high- and medium-density modules, 1 combined agent for low-density ones (typically 5 × 3 + 3 × 1) | ~18 (up to 24) |
| Cross-cutting: economics & business model, workforce & talent, guardrails & regulation, state of AI & disruption | 4 |
| Synthesis: 8 modules + 1 archetype-level | 9 |
| Verification: 8 modules + 1 archetype-level | 9 |
| **Total** | **~41 (up to 47)** |

The landscape scan rates each module's evidence density (from the pilot retro). For assurance, the
landscape is rerun with network access, and the controls-testing module from the pilot is kept.

### What the agent count means

A "research agent" is **one focused task** (for example, "what are practitioners saying at
conferences about AI in controls testing?"). It runs in its own context window, reads many sources,
and returns one structured file. Depth comes from keeping each task narrow, so a broad archetype is
split into many tasks.

| | Agents |
|---|---|
| Stream M | 12 |
| Stream B | 14 |
| Stream A: 3 archetypes × ~41 (up to 47); the pilot's agents count toward assurance | ~123 (up to 141) |
| **Full build** | **~150 (up to ~167)** |

These are **build-time** agents. Most of the research is finished before release, so users get deep
archetypes immediately. The optional on-the-spot research (spec §7.4) is only for businesses no built
archetype covers.

**Cost, measured in the pilot.** A deep agent uses **300k–400k tokens** (about 350k on average), and
one module end to end costs about 1.85M.

| Scope | Tokens |
|---|---|
| One archetype | ~14M |
| Three archetypes | ~41M |
| Streams M and B | ~9M |
| **Full build** | ~~~50M~~ → **~75M, revised after wave 1** (pilot about 2M, wave 1 about 23M, remaining about 50M) |

Two levers can reduce this:

- low-density modules get one deep dive instead of three (already counted above)
- the deep dives could run on a faster, cheaper model, with synthesis and verification on the
  strongest model. This is tested in wave 1 by comparing the verifier's correction rate with the
  pilot's 21 of 25.

**Time.** A module's chain (deep dives → synthesis → verification) takes about an hour. Modules run in
parallel, in waves of up to about 25 agents. One archetype takes roughly 2–3 hours of wall-clock time.

### Models

- **Research legs** run on **Sonnet** (owner decision, 2026-10-16): landscape scans, module deep dives,
  cross-cutting topics and method topics. They are cheaper than Opus.
- **Synthesis and verification** stay on the strongest model (Opus). The verifier is the quality
  gate.
- Wave 1 compares the verifier's correction rate with the pilot's (21 of 25 entries corrected, all
  research on Opus).

### Wave order (after the pilot)

| Wave | Content | Agents |
|---|---|---|
| 1 · **done** | The rest of assurance (the landscape grew it to 10 modules), cross-cutting topics, archetype-level files, consistency pass. Stream M (method): 11 files. 63 agents, about 23M tokens, about 2 hours. See the [retro](../research/runs/wave1/RETRO.md) | 63 |
| 2 · **in progress** | Tax. Landscape done (160 sources); module set revised to 8 modules plus 4 cross-cutting topics; 26 research agents, then synthesis and verification | ~50–60 |
| 3 | Professional services, plus stream B (backbone library) | ~50–60 + ~15 |
| 4 | Security (added 2026-10-17). Landscape first, then module sign-off with the owner before the deep dives. Up to 11 proposed modules, so likely the largest archetype | ~55–70 |

**Changes adopted after wave 1:**

- The landscape scan runs alone, before the deep dives, so they don't compete for the shared web-search quota.
- Every agent works in a private working folder.
- The text mirror is available for sites that block direct access.
- Plans allow for the landscape adding modules (about 25% extra).
- The A/B target applies only where public evidence exists. Thin modules are rated in `ARCHETYPE.md`.

M2 (install skeleton) and M5 (authoring) can start during wave 1, using the pilot module as the first
real archetype content.

### M5. Author the skill · **first version done** (library pattern and function files wait for stream B)

Status: `SKILL.md`, `library/index.md`, `archetypes/index.md`, six briefs, schemas, templates and
`templates/workspace/` are written and pass the validator. The library index carries short working definitions
of patterns and functions until stream B produces the detailed files.

- `SKILL.md`, following spec §7.2 (the conductor), with the rules first.
- `method/` files from stream M. Each has its expert moves, question bank, traps and examples.
- `library/` index and pattern and function files from stream B.
- `archetypes/index.md` and each `ARCHETYPE.md` with its interview guide, from stream A.
- Runtime `briefs/`: analyze-document, scout-use-cases, desk-review-unit, review-opportunities,
  rollup-unit, and **research-archetype**. The last one is an optional, lighter runtime version of the
  build recipe for businesses with no built archetype. It writes a provisional archetype into the
  user's overlay. It is adapted from `research/briefs/templates/` once the pilot has proven them.
- `templates/` (plan and brief skeletons) and `templates/workspace/`.

### M6. Evals

- 30–50 scenarios (spec §10). The audit-partner scenario is the reference case.
- A runner that drives a scripted user through the skill headlessly in one client, captures the files
  written, validates them, and grades the transcript against a rubric. Other clients get install
  and smoke tests only.
- Subject-matter review of the reference scenarios and the archetype content.

### M7. Release v0.1.0

- Install instructions per client in `README.md`.
- Version tagged. Refresh cadence recorded (rerun the research briefs twice a year).

## Risks

| Risk | Mitigation |
|---|---|
| Research invents or misreads sources | A verifier agent checks every claim against its source. The validator requires dated sources. URLs are spot-checked. Unsupported entries are dropped |
| Research is broad but shallow | Narrow tasks (one module × one angle). The pilot checks depth before scaling |
| Some sources are blocked or behind paywalls | Each brief lists several source types. Gaps are recorded in `sources.md`, not filled by guessing |
| Token cost and time | Waves of 10–25 agents. Pilot measurement. Briefs reused for refreshes |
| Content goes stale fast | `last_researched` on every file. Briefs kept for a twice-yearly rerun |
| Copyright | Summaries in our own words. No long quotations |
| Client differences break installation | M2 runs the skeleton first. A per-client checklist |
| `SKILL.md` grows past its budget | The validator enforces the line limits. Detail moves to method files |
| Subagent delegation not followed in some clients | Explicit wording. The inline fallback gives the same contract. An eval checks it |
| No subject-matter reviewer | Find an audit and a tax reviewer before M6 |

## Proof

| Milestone | Done when |
|---|---|
| M0 | `scripts/validate.py` passes on the schema examples and fails on deliberately broken ones |
| M1 | The pilot module meets the spec §6.8 targets (15–25 use cases, at least 50% graded A or B, dated sources, frontier signals), the retro is written, and this plan is updated |
| M2 | The skeleton installs and passes the smoke checklist in Claude Code. The owner confirms the other clients |
| M3 / M4 | Every module and method file passes the validator and verification. The verifier's rejection rate is recorded |
| M5 | The skill passes the validator. A manual end-to-end run of the audit-partner scenario writes valid files |
| M6 | The eval suite passes its agreed threshold. All §9 rules pass |
| M7 | Installed from a clean machine in each target client using only the README |

# Spec addendum: the skill suite

From: owner decision of 2026-10-20 (skill suite, plugin renamed `ai-transformation`) · Extends:
[`2026-10-16-ai-transformation-advisor.md`](2026-10-16-ai-transformation-advisor.md) §7 · Status: draft

## Contents

1. [Why a suite](#1-why-a-suite)
2. [The skills](#2-the-skills)
3. [Shared knowledge and shared rules](#3-shared-knowledge-and-shared-rules)
4. [Workspace and handoffs](#4-workspace-and-handoffs)
5. [What each new skill writes](#5-what-each-new-skill-writes)
6. [Content added to the shared knowledge](#6-content-added-to-the-shared-knowledge)
7. [Quality gates](#7-quality-gates)
8. [Simplicity and deferred features](#8-simplicity-and-deferred-features)

## 1. Why a suite

The advisor finds and plans AI opportunities. Running an AI program also means running a portfolio of
those opportunities, delivering solutions into production, raising fluency across the workforce and setting
governance. These are different jobs with different triggers, inputs and outputs. Folding them into one
`SKILL.md` would blur its description and push it past the size where a conductor stays reliable; separate
plugins would duplicate the knowledge base. So the plugin becomes a **suite**: several skills, one shared
knowledge base, handoffs through files in the user's workspace.

This revisits spec §7.1. The structure research
([`docs/research/2026-10-16-skill-structure.md`](../docs/research/2026-10-16-skill-structure.md)) found that
real plugins keep shared libraries read by relative path, hand off by naming the next skill with a file-read
fallback, and write descriptions that name the moment and point to sibling skills. The suite follows those
practices. Packs (archetypes) stay data, not skills.

## 2. The skills

| Skill | Job | Triggers on (the moment) |
|---|---|---|
| `transformation-advisor` | Find where AI can change the work and plan it (onboarding, the loop, Break down and Roll-up, acquisition assessment) | "where could AI help my team/practice/firm", a transformation plan or business case, resuming a plan |
| `ai-portfolio` | Run the firm's AI portfolio: intake, screening and scoring, stage gates, portfolio reviews, stop or redirect, value tracking, the rollout playbook for acquired firms | "review our AI portfolio", a new idea to log or score, "should we stop/scale this pilot", benefits tracking, rolling capabilities into an acquired firm |
| `ai-solution-delivery` | Take one opportunity to a supported production solution: problem framing, build versus buy, design brief, evaluation plan, production readiness, post-launch review | "we want to build/buy X", a pilot to take live, an evaluation plan, "is this ready for production" |
| `ai-enablement` | Raise fluency and sustained use: assess and segment users, design the program, role-based curriculum, champions and office hours, workflow library, adoption and impact measures, bringing partners and skeptics along | training, office hours, champions, adoption is uneven, "people aren't using the tools" |
| `ai-governance` | Set practical governance: AI policy, data rules, risk tiers and human review, records of AI use, profession-specific duties, vendor and tool evaluation, the approved-tool catalog | an AI policy, "can we use tool X with client data", vendor evaluation, IT or security concerns |

Each description names its moment and points to its siblings to avoid trigger conflicts. A skill hands off
by name with a fallback: "Next, use the **ai-portfolio** skill. If you can't invoke a skill by name, read
`../ai-portfolio/SKILL.md` and follow it."

## 3. Shared knowledge and shared rules

- **Shared knowledge stays where it is**, under `skills/transformation-advisor/references/` (method, library,
  archetypes, schemas, templates, briefs). Sibling skills read it by relative path
  (`../transformation-advisor/references/...`). Nothing moves, so no existing pointer breaks. Each new skill
  keeps its own `references/` for content only it uses.
- **Shared rules.** Every `SKILL.md` carries the same core rules block (no actions on named individuals, ranges
  not point estimates, never invent sources, grades exactly as recorded, no client-confidential data, design
  and plan but never claim to build or run, sequence by dependencies not calendar deadlines, honest about
  roles). The validator checks that the copies match one source,
  `skills/transformation-advisor/references/schemas/core-rules.md`.
- **Overlay first.** Every skill reads `overlay/guardrails.md` and `overlay/tool-catalog.yaml` when they exist.

## 4. Workspace and handoffs

```
<workspace>/
├── transformation-plan.md · opportunities.yaml · units/     # advisor (unchanged)
├── portfolio/                                              # ai-portfolio
│   ├── portfolio.yaml          # every initiative, its stage, scores, owner, decisions
│   ├── intake/<id>.md          # one intake record per idea
│   ├── reviews/<n>-review.md   # portfolio review packs and decisions (numbered, not dated deadlines)
│   └── benefits.yaml           # benefits register: forecast versus realised, by named metric
├── solutions/<id>/                                         # ai-solution-delivery
│   ├── brief.md                # problem, build-or-buy decision, design, data, security
│   ├── eval-plan.md            # test set, thresholds, human evaluation, monitoring
│   ├── readiness.md            # production-readiness checklist and sign-offs
│   └── post-launch.md          # post-launch review
├── enablement/                                             # ai-enablement
│   ├── program.md              # segments, curriculum, champions, office hours, leader expectations
│   ├── workflows/<id>.md       # reusable workflows (prompt, skill or procedure) by role
│   └── measures.yaml           # adoption and impact measures
└── overlay/                                                # ai-governance writes; every skill reads
    ├── guardrails.md · tool-catalog.yaml                    # already read by the advisor
    ├── policy.md               # acceptable use, data rules, risk tiers, records of AI use
    └── vendors/<vendor>.md     # vendor and tool evaluations
```

Handoffs: the advisor's `opportunities.yaml` items enter `portfolio.yaml` through intake (with a back-link);
a portfolio item in `discover` or later may open `solutions/<id>/` (a brief opened in `discover` is evidence for
`g1`), and ai-solution-delivery then hands back so ai-portfolio sets the item's `solution` (a `g0` Go does not set
it; it is set only when `solutions/<id>/brief.md` exists and delivery has handed back); launched
solutions add rows to `benefits.yaml` and workflows to `enablement/workflows/`; governance outputs constrain
every skill through the overlay.

## 5. What each new skill writes

Each new skill has: a `SKILL.md` conductor (target 150-250 lines, hard limit 500), a `references/` folder
with one method file per step (at most 300 lines each, contents list over 100 lines), templates for its
workspace files, and a schema for each YAML file it writes (`portfolio/v1`, `benefits/v1`, `measures/v1`).
Schemas live with the skill that owns the file; vocabulary ids stay in the shared `vocabulary.yaml`.

## 6. Content added to the shared knowledge

- **Partner and stakeholder change** (advisor): stakeholder mapping, partner briefings, objection handling
  and leader expectations in `method/people-and-change.md` or a companion file.
- **Acquisitions** (advisor and ai-portfolio): an acquisition path in the advisor (assess a target or
  acquired firm's AI maturity, with a subagent brief) and a rollout playbook in ai-portfolio.
- **Advisory archetype** and **mid-market modules** in tax and assurance: archetype content under
  `archetypes/`, researched and verified like the others.

## 7. Quality gates

- Research for each new skill uses the method-topic recipe (Sonnet), authoring on Opus, then a fact-check
  (Opus) of every research-backed claim, as for the method files.
- The validator covers the new skills: sizes, contents lists, links (including `../transformation-advisor/`
  paths), schema examples that parse, and identical core-rules blocks.
- A smoke test in Claude Code: each skill triggers on its moment, reads a shared reference across the skill
  folder, and writes its workspace file; a short end-to-end run hands off advisor → portfolio → delivery.

## 8. Simplicity and deferred features

Owner decision of 2026-10-22: transformation-advisor is the key skill. The four siblings should be robust but not
overcomplicated, and grow as they are tested with real users. They were trimmed moderately: every step and file
kept, each `SKILL.md` at 160 lines or fewer, method files about 40% shorter. Behaviour that an end-to-end test proved
necessary was kept. Features were cut, not lost. Each comes back when a test or a user shows it is needed:

| Skill | Deferred features (detail and "worth it when" in the trim report) |
|---|---|
| ai-portfolio | Tailoring by journey stage; payback hurdles and spend thresholds per item class; benefit dependencies; configurable screening axes; a separate benefits-review rhythm; an independent challenge before big-bet gates; budget-split benchmarks; partner economics at case gates; wider acquired-firm guidance; private-equity benchmarks; the central team's shift from gatekeeper to advisor |
| ai-solution-delivery | Question banks per step; expert-move notes; full common-traps tables; long worked examples; a per-block readiness template |
| ai-enablement | Scope tags and full question banks; an equity check on uneven take-up; a richer forum catalogue; simulated practice environments; a delegation-depth signal; per-step checklists |
| ai-governance | A per-pattern risk table; per-runtime-class control notes; an internal-audit frame for tier-4 uses; mapping to ISO/IEC 42001 and the CSA controls matrix; non-US regimes; contract and liability depth; survey context for a business case |

Trim reports: [`research/runs/trim/`](../research/runs/trim/). The detailed text is in git history at the commit
before each trim.

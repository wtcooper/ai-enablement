# Schema: solution files (solution/v1)

Each solution has its own folder, `solutions/<id>/`, with four markdown files. Each file starts with YAML
frontmatter for state, then a body written from its template in `../templates/`. The brief carries the solution's
state for resume; the other three files carry only what their own step decides. Shared ids (pattern, ladder,
change scope, runtime class, work types, archetype, levers) come from
`../../../transformation-advisor/references/schemas/vocabulary.yaml`.

## Contents

1. [Frontmatter: brief.md](#1-frontmatter-briefmd)
2. [Frontmatter: eval-plan.md, readiness.md, post-launch.md](#2-frontmatter-eval-planmd-readinessmd-post-launchmd)
3. [Controlled values owned by this skill](#3-controlled-values-owned-by-this-skill)
4. [Field rules](#4-field-rules)
5. [Example](#5-example)

## 1. Frontmatter: brief.md

```yaml
schema: solution/v1
doc: brief
id: string                        # same as the folder name, e.g. ct-evidence-matching
title: string
source:
  portfolio_item: string | null   # the item id in portfolio/portfolio.yaml
  opportunity: { file: path, id: string } | null   # the advisor option, e.g. opportunities.yaml + its id
scope: { name: string, level: team | function | business-unit | organization }
owners:
  business: role                  # accountable for the outcome; reviews outputs on a rhythm
  delivery: role                  # leads this solution through the six steps
  support: role | null            # owns it after launch (set by step 5)
classification:
  archetype: id | null
  modules: [ id ]
  work_types: [ id ]
  pattern: id                     # the shared pattern file whose checkpoints the design uses
  ladder: assist | augment | automate | delegate          # the rung at launch
  ladder_target: assist | augment | automate | delegate | null   # a rung evidence may later earn
  change_scope: step | process | model
  runtime_class: id
sourcing: buy | configure | build-on-model | build-custom | undecided
tools: [ string ]                 # overlay catalog entries, or runtime-class descriptions
vendor_evaluations: [ path ]      # e.g. overlay/vendors/<vendor>.md, written by ai-governance
risk_tier: string | null          # tier id from overlay/policy.md (e.g. tier-3); null until set
status: in-progress | live | paused | stopped | retired
step_completed: 0-6
next_step: 1-6 | null
updated: YYYY-MM-DD
```

## 2. Frontmatter: eval-plan.md, readiness.md, post-launch.md

```yaml
# eval-plan.md
schema: solution/v1
doc: eval-plan
solution: string                  # the brief's id
version: integer                  # +1 whenever tasks, graders or thresholds change
status: draft | agreed
thresholds_agreed_by: role | null # the business owner or quality owner who accepted them
---
# readiness.md
schema: solution/v1
doc: readiness
solution: string
decision: pending | go | go-with-conditions | no-go
decided_by: role | null
conditions: [ string ]            # each with an owner and the event that clears it
---
# post-launch.md
schema: solution/v1
doc: post-launch
solution: string
reviews_completed: integer
last_decision: continue | tighten | loosen | redesign | retire | null
next_review_when: string          # the event that triggers the next review, never a calendar date
```

## 3. Controlled values owned by this skill

These values are local to the solution files. They are not in the shared `vocabulary.yaml`.

| Field | Values | Meaning |
|---|---|---|
| `sourcing` | `buy` | Use a bought tool as it is |
| | `configure` | Configure a bought tool: settings, templates, approved content, connectors |
| | `build-on-model` | Build a workflow, retrieval and checks around a bought model or platform |
| | `build-custom` | Build most components in-house |
| | `undecided` | Before step 2 ends |
| `status` | `in-progress` · `live` · `paused` · `stopped` · `retired` | Where the solution stands |
| `eval-plan.status` | `draft` · `agreed` | Agreed once the owner accepts tasks, checks and thresholds |
| `readiness.decision` | `pending` · `go` · `go-with-conditions` · `no-go` | The step 5 decision |
| `post-launch.last_decision` | `continue` · `tighten` · `loosen` · `redesign` · `retire` | The outcome of the latest review; `tighten` and `loosen` refer to human review and autonomy |

## 4. Field rules

- **One folder per solution.** `id` matches the folder name and, where one exists, the portfolio item id.
  `source` keeps the back-link to the portfolio item and the advisor option; never copy their content.
- **State.** After every step set `step_completed`, `next_step` and `updated` in `brief.md`, and tick the step in
  its Progress list. After step 6, `next_step: null`; later reviews add numbered sections to `post-launch.md` and
  update its frontmatter.
- **Ids from the shared vocabulary.** `classification` values must be ids from `vocabulary.yaml`. If the step 3
  design changes the rung or runtime class from the advisor option, record the change and the reason in the
  brief's decisions log.
- **Owners are roles.** Never record performance judgments about named individuals (rule 1).
- **Risk tier** is the tier id from `overlay/policy.md` (the **ai-governance** skill defines `tier-1` to
  `tier-4`), copied, never invented here. With no policy, leave `null` and hand off to **ai-governance**.
- **Portfolio link.** When `source.portfolio_item` is set, the portfolio item's `solution` field points back to
  `solutions/<id>/`; the **ai-portfolio** skill writes that field and the benefits rows, not this skill.
- **No dates as deadlines.** `updated` is a timestamp. Review triggers are events (`next_review_when`), never
  calendar dates.
- **Quote free text.** Put every free-text value in double quotes; an unquoted colon breaks the file.
- **No client-confidential content.** The files describe cases by type, source system and id, never their
  content (rule 5).

## 5. Example

```yaml
schema: solution/v1
doc: brief
id: ct-evidence-matching
title: "AI first-pass matching of control evidence to test attributes"
source:
  portfolio_item: ct-evidence-matching
  opportunity: { file: opportunities.yaml, id: ct-evidence-matching }
scope: { name: "Regional audit practice", level: team }
owners:
  business: "Audit partner leading the practice"
  delivery: "Pilot lead (senior manager)"
  support: "Audit methodology team"
classification:
  archetype: assurance
  modules: [ controls-testing ]
  work_types: [ review-assurance ]
  pattern: document-to-decision
  ladder: augment
  ladder_target: automate
  change_scope: step
  runtime_class: workflow-automation
sourcing: configure
tools: [ "Evidence-matching feature of the firm's approved audit platform (catalog entry)" ]
vendor_evaluations: []
risk_tier: tier-4
status: in-progress
step_completed: 3
next_step: 4
updated: 2026-10-20
```

The values in this example are illustrative.

# Schema: opportunities.yaml (opportunities/v1)

One file per scope, next to `transformation-plan.md`. Options are added in Reimagine, scored in Prioritize,
completed in Make the case and given next steps in Plan. Ids come from `vocabulary.yaml`.

## Contents

1. [Format](#1-format)
2. [Field rules](#2-field-rules)
3. [Example](#3-example)

## 1. Format

```yaml
schema: opportunities/v1
scope: path                        # the plan this file belongs to, e.g. transformation-plan.md
items:
  - id: string                     # short, stable, unique in this file, e.g. ct-evidence-matching
    title: string
    process: string                # the process from Map
    work_types: [ id ]
    pattern: id
    ladder: assist | augment | automate | delegate
    change_scope: step | process | model
    runtime_class: id
    description: string            # today → future
    value: [ { lever: id, low: number, high: number, unit: string, assumptions: string } ]
    scores: { value: 1-5, feasibility: 1-5, data_readiness: 1-5, risk: 1-5, time_to_value: 1-5, strategic_fit: 1-5 }
    weighted_score: number
    category: quick-win | foundation | big-bet | park
    revisit_when: string           # parked items only
    depends_on: [ id ]             # other items in this file that must come first
    prerequisites: [ string ]
    risks: [ string ]
    human_checkpoints: [ string ]
    role_evolution: { tasks_moving: string, new_work: string, capacity_use: redeploy | reduce | mixed }
    evidence: [ id ]               # archetype or overlay use-case ids, e.g. assurance-controls-testing-05
    label: draft-to-validate | null   # set for desk-review or subagent drafts not yet confirmed by the user
    rolled_up_from: [ path ]       # set by Roll-up
    next_step: { action: string, owner: role, depends_on: [ string ] }
```

## 2. Field rules

| Phase | Fields that must be filled |
|---|---|
| 4 Reimagine | `id`, `title`, `process`, `work_types`, `pattern`, `ladder`, `change_scope`, `runtime_class`, `description`, `evidence` (may be empty, with the option described as an idea) |
| 5 Prioritize | `value` (ranges), `scores`, `weighted_score`, `category`, `depends_on`, `prerequisites`, `risks`; `revisit_when` for parked items |
| 6 Make the case | For top options: `value` with assumptions, `human_checkpoints`, `role_evolution`, `evidence` checked |
| 7 Plan | For chosen options: `next_step` |

- **Ranges only.** `low` and `high` with a unit and period (for example `hours/year`, `GBP/year`, `days cycle time`)
  and the assumptions they rest on. Never a single-point ROI.
- **Scores** use the anchors in `../method/prioritize.md` §3.3. `risk`: a higher score means lower risk.
  `weighted_score` = sum of the plan's weights × scores, rounded to two decimals.
- **Role evolution** is required for team-level and higher options (rule 2). `capacity_use` states the
  redeploy-or-reduce choice. Describe roles and capacity, never named people.
- **Evidence** lists ids only; the grade and provenance live in the use case. Overlay use cases are labelled
  internal when cited.
- **Sequencing** uses `depends_on` and `next_step.depends_on`; never dates or deadlines.
- **Roll-up.** Parent items merged from units list each unit's path in `rolled_up_from`. Items that came from a
  desk review keep `label: draft-to-validate`.

## 3. Example

```yaml
schema: opportunities/v1
scope: transformation-plan.md
items:
  - id: ct-evidence-matching
    title: AI first-pass matching of control evidence to test attributes
    process: Operating-effectiveness testing of key controls
    work_types: [review-assurance]
    pattern: document-to-decision
    ladder: augment
    change_scope: step
    runtime_class: workflow-automation
    description: Today staff open each evidence file and tick attributes by hand. Future: the tool proposes matches with citations; staff review exceptions and a sample of matches.
    value:
      - { lever: capacity, low: 600, high: 1400, unit: hours/year, assumptions: "1,200 samples a year at 1.0-1.5 h each today; 40-70% of matching time released; review time included" }
    scores: { value: 4, feasibility: 4, data_readiness: 4, risk: 3, time_to_value: 4, strategic_fit: 4 }
    weighted_score: 3.85
    category: quick-win
    depends_on: []
    prerequisites: [ "Tool certified for this use", "Evidence available as searchable files" ]
    risks: [ "Reviewers accept matches without checking" ]
    human_checkpoints: [ "Staff review every exception", "Reviewer re-performs a sample of accepted matches" ]
    role_evolution: { tasks_moving: "Attribute ticking", new_work: "Exception investigation; sample re-performance", capacity_use: redeploy }
    evidence: [ assurance-substantive-testing-10, assurance-controls-testing-07 ]
    label: null
    next_step: { action: "Baseline hours per sample on three current engagements", owner: "Controls testing lead", depends_on: [] }
```

The figures in this example are illustrative, not evidence.

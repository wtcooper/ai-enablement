# Schema: portfolio/portfolio.yaml (portfolio/v1)

One file per portfolio, in `portfolio/` in the user's workspace. It holds the portfolio's settings, stage
definitions, roles and rhythm, and one entry per initiative with its stage, scores, owner and every gate
decision. Set up in step 1, then updated by every later step. A blank starting file is
`../templates/portfolio.yaml`. Controlled ids come from the shared vocabulary
(`../../../transformation-advisor/references/schemas/vocabulary.yaml`) or, for portfolio-only values, from
`../library/index.md`.

## Contents

1. [Format](#1-format)
2. [Field rules](#2-field-rules)
3. [Example](#3-example)

## 1. Format

```yaml
schema: portfolio/v1
portfolio:
  name: string                     # e.g. "Firm AI portfolio"
  scope: string                    # what the portfolio covers: the firm, a practice, a function
  level: function | business-unit | organization
  owner: role                      # the portfolio owner, as a role
  plan: path | null                # advisor plan the settings came from, e.g. ../transformation-plan.md
settings:
  value_levers: [ { id: id, name: string, metric: string, weight: number } ]
  scoring_weights: { value: n, feasibility: n, data_readiness: n, risk: n, time_to_value: n, strategic_fit: n }
  axes:                            # how the six scores split into the two screening axes
    value: [value, strategic_fit, time_to_value]
    readiness: [feasibility, data_readiness, risk]
  capacity_stance: redeploy | reduce | mixed | undecided
  inherited_from: path | null      # set when settings were copied from an advisor plan
  live_limit: integer | null       # most items in prototype, pilot or scale at once (owner and review capacity)
stages:                            # one entry per stage; defaults in ../method/stage-gates.md §3
  - { id: stage-id, purpose: string, entry: [ string ], exit: [ string ], gatekeepers: [ role ] }
gate_paths:
  light: string                    # which items qualify and which gates combine
  full: string
  g0_deciders: { light: [ role ], full: [ role ] }   # who decides the screen on each path
roles:
  review_forum: [ role ]           # who sits in the portfolio review
  intake_contact: role
  other: [ { role: string, duty: string } ]
rhythm:
  review: string                   # e.g. "monthly portfolio review"
  rebalance: string                # e.g. "every third review: balance, weights, live limit"
  benefits_review: string          # e.g. "at every review for items in production or scale"
state:
  status: setting-up | running
  step_completed: 0-6
  next_step: 1-6 | null
  last_review: integer             # number of the last review pack, 0 before the first
  updated: YYYY-MM-DD
items:
  - id: string                     # short, stable, unique, e.g. tax-k1-extraction
    title: string
    unit: string                   # submitting practice, team or function
    function: id | null            # shared vocabulary `functions`
    intake: path                   # portfolio/intake/<id>.md
    source: { file: path, item: id } | null   # back-link to an advisor opportunities.yaml item
    problem: string                # one sentence: activity and expected result
    item_class: individual-productivity | business-automation | new-value
    category: quick-win | foundation | big-bet | park
    horizon: near | medium | long
    pattern: id | null
    ai_use: none | null            # none: rules, a template or an existing tool is enough; null: AI is in scope
    ladder: assist | augment | automate | delegate | null     # null when ai_use is none
    change_scope: step | process | model | null
    runtime_class: id | null       # null when ai_use is none
    stage: intake | discover | prototype | pilot | production | scale | retire
    status: outline | active | hold | killed | retired
    owner: role                    # leads the work
    sponsor: role                  # controls the resources it needs next
    benefit_owner: role | null     # owns the benefit in the business
    risk_tier: string | null       # tier id from overlay/policy.md risk_tiers (ai-governance), e.g. tier-2; null when ai_use is none
    gate_path: light | full
    value: [ { lever: id, low: number, high: number, unit: string, assumptions: string } ]
    scores: { value: 1-5, feasibility: 1-5, data_readiness: 1-5, risk: 1-5, time_to_value: 1-5, strategic_fit: 1-5 }
    weighted_score: number
    value_index: number            # weighted mean of the value-axis scores
    readiness_index: number        # weighted mean of the readiness-axis scores
    depends_on: [ id ]
    kill_criteria: [ string ]      # agreed at the gate that let the item in
    early_warnings: [ { type: slippage | cost-overrun | performance-shortfall, note: string, review: integer } ]
    next_gate: { gate: gate-id, evidence: [ string ], gatekeepers: [ role ] } | null
    solution: path | null          # solutions/<id>/; set as soon as ai-solution-delivery opens the brief and hands back
    benefits: [ id ]               # benefit ids in portfolio/benefits.yaml
    evidence: [ id ]               # archetype or overlay use-case ids
    human_checkpoints: [ string ]  # who checks what; copied from the advisor item on import
    role_evolution: { tasks_moving: string, new_work: string, capacity_use: redeploy | reduce | mixed } | null   # never undecided
    revisit_when: string | null    # held or parked items
    decisions:
      - gate: g0 | g1 | g2 | g3 | g4 | retire
        review: integer | null     # review pack number, or null if decided outside a review
        outcome: go | kill | hold | recycle
        reason: string
        evidence: [ string ]       # what the decision rested on
        resources: string | null   # for a Go: people, budget and who releases them
        conditions: [ string ]
        recycle_to: string | null  # for a Recycle: new scope, approach (for example buy instead of build) or risk treatment
        decided_by: [ role ]
    updated: YYYY-MM-DD
```

## 2. Field rules

| Step | Fields that must be filled |
|---|---|
| 1 Set up | `schema`, `portfolio`, `settings`, `stages`, `gate_paths` (with `g0_deciders`), `roles`, `rhythm`, `state` |
| 2 Intake | Per item: `id`, `title`, `unit`, `intake`, `source` (or null), `problem`, `item_class`, `stage: intake`, `status` (`outline` until problem, owner and a data source are known), `owner`, `updated` |
| 3 Screen and score | `value` (ranges), `scores`, `weighted_score`, `value_index`, `readiness_index`, `category`, `horizon`, `risk_tier` (null with `ai_use: none`), `gate_path`, `sponsor`, `depends_on`, a `g0` decision by the path's `g0_deciders`; `kill_criteria` and `next_gate` on a Go |
| 4 Stage gates | One `decisions` entry per gate held; `stage`, `status`, `next_gate`; `solution` as soon as delivery opens a brief (from `discover` on); `benefit_owner` and `benefits` before `g3` |
| 5 Portfolio review | `early_warnings`; decisions made in the review carry its number in `review`; `state.last_review` |
| 6 Value tracking | `benefits` ids match `benefits.yaml`; `role_evolution` for team-level and higher items in production or scale |

- **Quote free text.** Put every free-text value in double quotes (`title`, `problem`, `reason`, `assumptions`,
  list items). An unquoted colon or `#` breaks the file.
- **Ranges only.** `value` lines carry `low`, `high`, `unit` with a period and `assumptions`; never one number.
- **Scores** use the anchors in `../../../transformation-advisor/references/method/prioritize.md` §3.3 and the
  portfolio's `scoring_weights` (they must sum to 1). `weighted_score` = sum of weight × score. Each index is the
  weighted mean of its axis's scores, using the same weights renormalized within the axis. Round to two decimals.
- **Owners are roles.** `owner`, `sponsor`, `benefit_owner`, `decided_by` and `gatekeepers` are roles, never
  names, and no field records a judgment about a person.
- **Every Go names `resources`** and sets `next_gate`. A Go without resources is incomplete.
- **Every Kill, Hold or Recycle has a `reason` and `evidence`.** A Hold also sets `revisit_when`.
- **Decisions are appended, never edited.** A later decision on the same gate is a new entry.
- **Back-links.** An item imported from an advisor `opportunities.yaml` keeps `source` and copies `pattern`,
  `ladder`, `change_scope`, `runtime_class`, `value`, `scores`, `category`, `depends_on`, `human_checkpoints`,
  `role_evolution` and `evidence` as they stand; re-score in step 3 against the portfolio's weights. The item's
  `process`, `prerequisites` and `next_step` go in the intake record. Never edit the advisor's file.
- **Capacity choice.** `capacity_use` is `redeploy`, `reduce` or `mixed`, never `undecided`. On import keep the
  advisor's value, even while `settings.capacity_stance` is `undecided`, and note the open stance in the intake
  record. A new item with no choice yet keeps `role_evolution: null`; the choice is due by `g3`.
- **No AI needed.** With `ai_use: none`, set `ladder`, `runtime_class` and `risk_tier` to null. Count the item
  apart from AI items in the review pack.
- **Solution link.** A brief may open while the item is in `discover` (as `g1` evidence) or later. When
  ai-solution-delivery opens it and hands back, set `solution` at once; no gate is needed for that.
- **Sequencing** uses `depends_on` and `next_gate`, never dates or deadlines. `updated` records when the entry
  last changed; it is not a target.
- Portfolio-only values (`item_class`, `horizon`, `stage`, `status`, gate ids, `outcome`, early-warning types,
  `gate_path`, `ai_use`) are defined in `../library/index.md` §2.

## 3. Example

```yaml
schema: portfolio/v1
portfolio:
  name: "Firm AI portfolio"
  scope: "All practices and firm services"
  level: organization
  owner: "Head of AI"
  plan: "../transformation-plan.md"
settings:
  value_levers:
    - { id: capacity, name: "Hours released", metric: "Preparer hours per return", weight: 0.4 }
    - { id: quality, name: "Fewer review notes", metric: "Review notes per return", weight: 0.3 }
    - { id: growth, name: "Advisory revenue", metric: "Advisory fees from existing clients", weight: 0.3 }
  scoring_weights: { value: 0.30, feasibility: 0.20, data_readiness: 0.15, risk: 0.15, time_to_value: 0.10, strategic_fit: 0.10 }
  axes:
    value: [value, strategic_fit, time_to_value]
    readiness: [feasibility, data_readiness, risk]
  capacity_stance: redeploy
  inherited_from: "../transformation-plan.md"
  live_limit: 6
stages:
  - { id: discover, purpose: "Frame the problem and look at the data", entry: ["Passed the screen"], exit: ["Baseline from records", "Data seen in its real state"], gatekeepers: ["Practice leader"] }
gate_paths:
  light: "tier-1 and individual-productivity items: g1 and g2 combined; portfolio owner decides g0"
  full: "Every other item: all gates, gatekeepers per stage"
  g0_deciders: { light: ["Head of AI"], full: ["Item sponsor", "Practice leaders", "Head of AI"] }
roles:
  review_forum: ["Managing partner", "Practice leaders", "Risk and quality partner", "Head of IT", "Finance director", "Head of AI"]
  intake_contact: "Head of AI"
  other: []
rhythm:
  review: "Monthly portfolio review"
  rebalance: "Every third review"
  benefits_review: "Every review, for items in production or scale"
state:
  status: running
  step_completed: 4
  next_step: 5
  last_review: 2
  updated: 2026-10-20
items:
  - id: tax-k1-extraction
    title: "AI extraction of K-1 and source documents with confidence flags"
    unit: "Tax, private client"
    function: service-delivery
    intake: "portfolio/intake/tax-k1-extraction.md"
    source: { file: "units/tax/opportunities.yaml", item: "tax-source-docs" }
    problem: "Preparers key K-1 data by hand; extract it with flags so preparer hours per return fall"
    item_class: business-automation
    category: quick-win
    horizon: near
    ai_use: null
    pattern: document-to-decision
    ladder: augment
    change_scope: step
    runtime_class: workflow-automation
    stage: pilot
    status: active
    owner: "Tax operations manager"
    sponsor: "Tax practice leader"
    benefit_owner: "Tax practice leader"
    risk_tier: "tier-2"
    gate_path: full
    value:
      - { lever: capacity, low: 900, high: 2400, unit: "hours/season", assumptions: "3,000 K-1-heavy returns; 0.3-0.8 h saved each after review time" }
    scores: { value: 4, feasibility: 4, data_readiness: 3, risk: 3, time_to_value: 4, strategic_fit: 4 }
    weighted_score: 3.70
    value_index: 4.00
    readiness_index: 3.40
    depends_on: []
    kill_criteria: ["Extraction errors found at review above the agreed threshold on the pilot returns"]
    early_warnings: []
    next_gate: { gate: g3, evidence: ["Pilot results against baseline", "Readiness checklist signed"], gatekeepers: ["Tax practice leader", "Risk and quality partner"] }
    solution: "solutions/tax-k1-extraction/"
    benefits: [b-tax-k1-hours]
    evidence: [tax-compliance-individual-business-02]
    human_checkpoints: ["Reviewer checks every flagged field before the return moves on"]
    role_evolution: { tasks_moving: "Keying K-1 data", new_work: "Checking flagged fields; advisory preparation", capacity_use: redeploy }
    revisit_when: null
    decisions:
      - { gate: g2, review: 2, outcome: go, reason: "Prototype on last season's real returns met the agreed accuracy bar", evidence: ["Prototype test log on 40 prior-year returns"], resources: "Two preparers part-time for the pilot, released by the tax practice leader", conditions: ["Reviewer checks every flagged field"], recycle_to: null, decided_by: ["Tax practice leader", "Head of AI"] }
    updated: 2026-10-20
```

The figures in this example are illustrative, not evidence.

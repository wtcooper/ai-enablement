# Schema: solution files (solution/v1)

Each solution has its own folder, `solutions/<id>/`, with four markdown files: YAML frontmatter for state, then a
body from its template in `../templates/`. The brief carries the solution's state for resume; the other three
carry only what their own step decides. Shared ids come from
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
  opportunity:                    # the advisor option, or null
    file: path                    # e.g. opportunities.yaml
    id: string                    # the option's id in that file
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
  ladder: assist | augment | automate | delegate | null   # the rung at launch; null when ai_use is none
  ladder_target: assist | augment | automate | delegate | null   # a rung evidence may later earn
  change_scope: step | process | model
  runtime_class: id | null        # null when ai_use is none
ai_use: none | null               # none: rules, a template or an existing tool meets the bar; null: AI is in scope
sourcing: buy | configure | build-on-model | build-custom | undecided
tools: [ string ]                 # overlay catalog entries, or runtime-class descriptions
vendor_evaluations: [ path ]      # e.g. overlay/vendors/<vendor>.md, written by ai-governance
risk_tier: string | null          # tier id from overlay/policy.md (e.g. tier-3); provisional while the policy is not approved; null until set, or when ai_use is none
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

These values are local to the solution files, not in the shared `vocabulary.yaml`.

| Field | Values | Meaning |
|---|---|---|
| `sourcing` | `buy` · `configure` · `build-on-model` · `build-custom` | Defined in `../method/build-or-buy.md` §3.1 |
| | `undecided` | Until all of step 2's exit criteria are met; a leaning goes in the decisions log |
| `status` | `in-progress` · `live` · `paused` · `stopped` · `retired` | Where the solution stands |
| `eval-plan.status` | `draft` · `agreed` | Agreed once the owner accepts tasks, checks and thresholds |
| `readiness.decision` | `pending` · `go` · `go-with-conditions` · `no-go` | The step 5 decision |
| `post-launch.last_decision` | `continue` · `tighten` · `loosen` · `redesign` · `retire` | `tighten` and `loosen` refer to human review and autonomy |

## 4. Field rules

- **One folder per solution.** `id` matches the folder name and, where one exists, the portfolio item id.
  `source` keeps the back-link to the portfolio item and the advisor option; never copy their content.
- **State.** `step_completed` is the last step whose exit criteria are all met, with every step before it also
  met. While a criterion is open, do not advance it or tick the step: list the open criteria beside the unticked
  step. With the user's agreement you may work ahead; `next_step` names the step to resume. After step 6,
  `next_step: null`; later reviews add numbered sections to `post-launch.md`.
- **Ids from the shared vocabulary.** `classification` values are ids from `vocabulary.yaml`. A change from the
  advisor option's rung or runtime class goes in the decisions log with the reason.
- **Who decides.** "Decided by" in the decisions log is `owners.business` or another firm role, never this
  skill. A decision this skill drafts reads "draft (ai-solution-delivery)" until a firm role confirms it. A
  confirmation by a role other than the business owner, for a decision the owner must take, is logged as
  direction; the owner's confirmation stays an open exit criterion.
- **Risk tier** is the tier id from `overlay/policy.md` (the **ai-governance** skill defines `tier-1` to
  `tier-4`), copied, never invented here. While `overlay/policy.md` is not `approved` (for example
  `status: draft`), copy its proposed tier into `risk_tier` and mark it "provisional" in §2 Catalog check (and
  §3 Security and privacy once written) and in the Handoffs row until the policy is approved; ai-portfolio follows
  the same rule (`../../../ai-portfolio/references/library/index.md` §2). With no policy, or no tier for this use
  in it, leave `null` and hand off to **ai-governance**.
- **Sibling files.** When ai-governance writes a vendor evaluation, a catalog entry or a tier for this solution,
  add the paths to `vendor_evaluations`, the entry to `tools`, the tier to `risk_tier`, and refresh the Summary.
- **No AI needed.** When step 1 or 2 finds that rules, a template or an existing tool meets the bar, set
  `ai_use: none`, `ladder: null`, `ladder_target: null`, `runtime_class: null` and `risk_tier: null`; no risk
  tier handoff is needed. Keep `pattern` and `sourcing` as they describe the work.
- **Portfolio link.** A brief may open while the portfolio item is in `discover` (as `g1` evidence) or later.
  When `source.portfolio_item` is set, hand back to **ai-portfolio** as soon as `solutions/<id>/brief.md` exists,
  and add a row to the brief's Handoffs table. ai-portfolio then sets the item's `solution` to `solutions/<id>/`;
  a `g0` Go does not set it, and it is set only when `brief.md` exists and this skill has handed back. ai-portfolio
  writes that field and the benefits rows, not this skill.
- **Plain rules.** Owners are roles (rule 1). `updated` is a timestamp; review triggers are events, never dates.
  Quote every free-text value. Cases appear by type, source system and id, never content (rule 5).

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
owners: { business: "Audit partner leading the practice", delivery: "Pilot lead (senior manager)", support: "Audit methodology team" }
classification:
  archetype: assurance
  modules: [ controls-testing ]
  work_types: [ review-assurance ]
  pattern: document-to-decision
  ladder: augment
  ladder_target: automate
  change_scope: step
  runtime_class: workflow-automation
ai_use: null
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

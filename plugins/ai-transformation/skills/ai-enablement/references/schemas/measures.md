# Schema: enablement/measures.yaml (measures/v1)

One file per program, at `enablement/measures.yaml`, next to `enablement/program.md`. Step 1 writes the population,
the segments and the baseline readings; step 2 defines every measure; step 7 adds readings and reads them. Shared ids
(`value_levers`, `provenance`) come from `../../../transformation-advisor/references/schemas/vocabulary.yaml`; the
other enums are local and explained in the comments below. A blank starting file is `../templates/measures.yaml`.

## Contents

1. [Format](#1-format)
2. [Field rules](#2-field-rules)
3. [Example](#3-example)

## 1. Format

```yaml
schema: measures/v1
program: enablement/program.md     # the program this file belongs to
population:
  description: string              # who is in scope, everyone, users or not
  size: integer                    # the denominator for reach, activity and depth measures
  source: string                   # where the count comes from (HR headcount, licence report)
segments:
  - id: string                     # short, stable, e.g. power-users
    name: string
    groups: [ string ]             # practices, levels or role groups; never named people
    size_low: integer              # a range, because segments are estimates
    size_high: integer
    depth: not-using | one-off | repeatable | builder        # the ladder in ../assess-and-segment.md §3
    main_barrier: access | use-case | time | permission | security | belief | fear | none
    manager_behaviour: none | encourages | requires | unknown
    first_move: string
    basis: string                  # what the estimate rests on (telemetry, survey, interviews)
measures:
  - id: string                     # short, stable, unique in this file, e.g. weekly-active
    name: string
    layer: reach | activity | depth | embedded | outcome | sentiment | side-effect   # ../measure-adoption.md §3
    definition: string             # in words a sponsor would understand
    numerator: string
    denominator: string            # includes non-users for reach, activity and depth
    window: string                 # e.g. "7 days", "28 days", "per engagement"
    split_by: [ string ]           # e.g. practice, level, location
    data_source: string
    method: telemetry | survey | sampled-work | records | comparison   # comparison: random, staggered or matched groups
    provenance: self-reported | vendor-published | independent
    measured: true | false         # true only for tracked data or a study; false for estimates and recollection
    known_bias: string
    discount: { low: number, high: number, basis: string } | null   # self-reported time saved only
    lever: id | null               # value lever, for outcome measures
    links: { workflows: [ id ], opportunity: id | null, benefit: id | null }
    baseline: { value: number | null, low: number | null, high: number | null, unit: string, as_of: YYYY-MM-DD, basis: string } | null
    target: { low: number, high: number, unit: string, after: string } | null
    readings:
      - { as_of: YYYY-MM-DD, value: number | null, low: number | null, high: number | null, unit: string, n: integer, note: string }
    owner: role
updated: YYYY-MM-DD
```

## 2. Field rules

| Step | Fields that must be filled |
|---|---|
| 1 Assess and segment | `population`, `segments`, and at least one `reach`, one `activity` and one `depth` measure with a `baseline` |
| 2 Design the program | Every measure the charter names, with `definition`, `numerator`, `denominator`, `window`, `method`, `owner`; at least one `embedded` and one `outcome` measure |
| 5 Workflow library | `links.workflows` on the `embedded` measures |
| 7 Measure | `readings` for each measure, and `discount` on every self-reported time-saved measure |

- **Quote free text.** Put every free-text value in double quotes. An unquoted colon or `#` breaks the file.
- **Groups, never people.** `segments.groups` and `split_by` name practices, levels and role groups. Never store
  per-person usage, fluency scores or rankings. Suppress any split smaller than the minimum group size the firm's HR
  or privacy lead sets, and say so in `note`.
- **Denominators include non-users.** For reach, activity and depth, `denominator` is the population in scope (or a
  segment of it), not the licensed or active users.
- **Label every number.** `method` says how it was collected; `provenance` who measured it; `measured` whether it is
  tracked or estimated. A self-estimate of time saved is `method: survey`, `measured: false`, carries `discount`, and
  is reported apart from measured outcomes (`../measure-adoption.md` §4).
- **Counts may be points; value is a range.** Telemetry counts (`value`) can be single numbers. Estimates, time
  saved and any value figure use `low` and `high` (core rule 3).
- **Targets are ranges with a dependency, never a date.** `target.after` names what must be in place first. `as_of`
  dates record when a reading was taken; they are not deadlines.
- **Links.** `links.workflows` lists ids of files in `enablement/workflows/`; `opportunity` is an id in
  `opportunities.yaml`; `benefit` is an id in `portfolio/benefits.yaml` when ai-portfolio tracks it.

## 3. Example

```yaml
schema: measures/v1
program: enablement/program.md
population:
  description: "All client-service staff and partners in the tax practice"
  size: 120
  source: "HR headcount report"
segments:
  - id: blocked
    name: "Non-users blocked by data rules"
    groups: ["Private client team"]
    size_low: 15
    size_high: 25
    depth: not-using
    main_barrier: security
    manager_behaviour: none
    first_move: "Get a clear data rule from governance before any training"
    basis: "Anonymous survey free-text answers"
measures:
  - id: embedded-workflows
    name: "Workflows that are the default way"
    layer: embedded
    definition: "Approved library workflows that a practice group has declared the standard way to do the task"
    numerator: "Approved workflows declared the default by a practice lead"
    denominator: "Target workflows named in the charter"
    window: "As at each reading"
    split_by: ["practice group"]
    data_source: "Library index in program.md section 5 and practice-lead sign-offs"
    method: records
    provenance: self-reported
    measured: true
    known_bias: "A declared default may not be followed; sample real work to check"
    discount: null
    lever: null
    links: { workflows: ["notice-response-draft"], opportunity: null, benefit: null }
    baseline: { value: 0, low: null, high: null, unit: "workflows", as_of: 2026-10-20, basis: "Library not yet started" }
    target: { low: 2, high: 4, unit: "workflows", after: "First library entries approved in each practice group" }
    readings: []
    owner: "Head of tax knowledge"
  - id: time-saved-self
    name: "Self-reported time saved"
    layer: outcome
    definition: "Hours per person per week that users say the assistant saves"
    numerator: "Sum of reported hours saved"
    denominator: "Everyone surveyed, users and non-users"
    window: "Typical week, as recalled"
    split_by: ["level"]
    data_source: "Anonymous pulse survey"
    method: survey
    provenance: self-reported
    measured: false
    known_bias: "Recall and enthusiasm; keen users answer more often"
    discount: { low: 0.2, high: 0.5, basis: "Judgment agreed with the sponsor; one public evaluation cut its estimates by about 20%" }
    lever: capacity
    links: { workflows: ["notice-response-draft"], opportunity: null, benefit: null }
    baseline: null
    target: null
    readings:
      - { as_of: 2026-10-20, value: null, low: 0.5, high: 1.6, unit: "hours/person/week, after discount", n: 64, note: "Raw answers 1-2 hours; 53% response rate" }
    owner: "Practice operations manager"
updated: 2026-10-20
```

The figures in this example are illustrative, not evidence.

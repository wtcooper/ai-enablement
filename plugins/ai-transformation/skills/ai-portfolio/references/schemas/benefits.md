# Schema: portfolio/benefits.yaml (benefits/v1)

The benefits register: one entry per benefit and named metric, with owner, baseline, forecast range,
counterfactual, actuals by review and the capacity decision. Rows are created before an item passes `g3` and
updated at every review; launched solutions from ai-solution-delivery add rows here. Blank file:
`../templates/benefits.yaml`; method: `../method/value-tracking.md`. The fields follow benefits-realisation
practice [AUSGOV-2013; IVI-ITCMF-n.d.].

## Contents

1. [Format](#1-format)
2. [Field rules](#2-field-rules)
3. [Example](#3-example)
4. [Sources](#4-sources)

## 1. Format

```yaml
schema: benefits/v1
portfolio: path                    # portfolio/portfolio.yaml
updated: YYYY-MM-DD
benefits:
  - id: string                     # b-<item>-<metric>, unique
    item: id                       # the portfolio item it belongs to
    description: string            # the change in the item's objective this benefit measures
    lever: id                      # shared vocabulary `value_levers`
    metric: string                 # one named metric, e.g. "Preparer hours per return"
    type: direct | indirect | interim | disbenefit
    financial: true | false
    level: use-case | enterprise   # use-case effect versus firm P&L effect; never mixed in one row
    owner: role                    # the benefit owner in the business
    baseline: { value: number, unit: string, period: string, basis: from-record | reported | observed | outside-in, source: string }
    forecast: { low: number, high: number, unit: string, period: string, assumptions: string }
    counterfactual: control-group | staggered-start | parallel-run | baseline-comparison | assumption
    attribution: string            # other change shipping alongside; what share is claimed for the AI and why
    measurement: { method: string, collected_by: role, when: string }   # when = trigger, e.g. "each review after go-live"
    actuals:
      - { review: integer, period: string, low: number, high: number, unit: string, basis: from-record | reported | observed | outside-in, note: string }
    status: forecast | tracking | realised | partly-realised | not-realised | withdrawn
    confidence: low | medium | high
    capacity:                      # capacity benefits only (lever capacity, or hours behind cost)
      absorbed: { low: number, high: number, unit: string }
      redeployed: { low: number, high: number, unit: string, destination: string, output_metric: string }
      cashable: { low: number, high: number, unit: string, how: string }
      decision: redeploy | reduce | mixed | undecided
      decided_at_review: integer | null
    lessons: string | null         # for not-realised or withdrawn benefits
```

## 2. Field rules

- **One metric per row.** An item with three levers has three rows. The metric matches the portfolio's
  `settings.value_levers` metric for that lever, or says why it differs.
- **Owner is a role** in the business, not in the AI team.
- **Forecast is a range** with a unit, a period and assumptions, copied from the item's `value` line. Never
  overwrite a forecast; a re-forecast is a new row with `status: forecast` and a note in `attribution`.
- **Baseline and counterfactual before launch** [FCC-2026; DELOITTE-2025]. A row without a baseline cannot move
  past `forecast`. `basis` labels where a number came from (the advisor's Map labels). `assumption` as the
  counterfactual must say so in `attribution`, and the row's `confidence` cannot be `high`.
- **Actuals are ranges too** when measurement is uncertain (a single value repeats in `low` and `high`), each with
  the review number it was reported at.
- **Status** is set at each review: `tracking` once actuals exist; `realised` when actuals sit inside or above the
  forecast range on the agreed counterfactual; `partly-realised` below the low end but above baseline;
  `not-realised` at or below baseline at the planned review point; `withdrawn` when the item is killed or the
  benefit no longer applies. Keep not-realised and withdrawn rows; they feed the benefit success rate.
- **Level.** `use-case` rows measure the item's own metric; `enterprise` rows record a P&L line. Never add
  use-case rows together and report the sum as enterprise impact [MCK-2026].
- **Capacity.** Hours released split three ways (`../method/value-tracking.md` §3.2); only `cashable` carries money
  as a cost saving. `decision` records the redeploy-or-reduce choice at the level of roles and capacity, never
  people. `capacity` is null for benefits that release no hours.
- **Quote free text.** Double quotes on every free-text value.

## 3. Example

```yaml
schema: benefits/v1
portfolio: "portfolio/portfolio.yaml"
updated: 2026-10-20
benefits:
  - id: b-tax-k1-hours
    item: tax-k1-extraction
    description: "Fewer preparer hours keying K-1 and source-document data"
    lever: capacity
    metric: "Preparer hours per K-1-heavy return"
    type: direct
    financial: false
    level: use-case
    owner: "Tax practice leader"
    baseline: { value: 2.1, unit: "hours/return", period: "last filing season", basis: from-record, source: "Time records, 3,000 returns" }
    forecast: { low: 0.3, high: 0.8, unit: "hours/return saved", period: "first season after go-live", assumptions: "Review of flagged fields included; 70-90% of returns in scope" }
    counterfactual: staggered-start
    attribution: "Two offices start a season later and serve as the comparison; the new review checklist ships at the same time in all offices, so its effect is common to both groups"
    measurement: { method: "Time records per return, both groups", collected_by: "Tax operations manager", when: "Each review after go-live" }
    actuals:
      - { review: 4, period: "first half of season", low: 0.4, high: 0.6, unit: "hours/return saved", basis: from-record, note: "Comparison offices flat" }
    status: tracking
    confidence: medium
    capacity:
      absorbed: { low: 200, high: 500, unit: "hours/season" }
      redeployed: { low: 700, high: 1400, unit: "hours/season", destination: "Advisory reviews for existing clients", output_metric: "Advisory reviews completed" }
      cashable: { low: 0, high: 200, unit: "hours/season", how: "Less seasonal contract preparer time" }
      decision: redeploy
      decided_at_review: 3
    lessons: null
```

The figures in this example are illustrative, not evidence.

## 4. Sources

- `AUSGOV-2013` — Australian Government, Department of Finance, *Gateway Reviews lessons learned: Gate 5, Benefits Realisation Review*, government guidance, 2013-10. https://www.finance.gov.au/sites/default/files/2019-11/Gate_5_-_Lessons_Learned.pdf
- `DELOITTE-2025` — Deloitte, *AI ROI: the paradox of rising investment and elusive returns*, consultancy survey, 2025-10-22. https://www.deloitte.com/global/en/issues/generative-ai/ai-roi-the-paradox-of-rising-investment-and-elusive-returns.html
- `FCC-2026` — Business Times (via French Chamber of Commerce in Singapore), *DBS says AI push is paying off*, news report, 2026-02-09. https://www.fccsingapore.com/news/n/news/dbs-says-ai-push-is-paying-off-as-it-shifts-from-efficiency-tool-to-growth-engine.html
- `IVI-ITCMF-n.d.` — Innovation Value Institute, *Benefits Harvesting (IT-CMF 18.07)*, maturity-model guidance, undated. https://portal.ivi.ie/+itcmf/18.07/value/BAR/C/C3
- `MCK-2026` — McKinsey & Company, *The state of AI in 2026: on the road to ROI*, consultancy survey, 2026-08. https://www.mckinsey.com.br/en/our-insights/the-state-of-ai

# Value tracking (step 6)

Read this when an item approaches `g3`, a review needs benefits figures, or the user asks what the portfolio has
delivered. Keys in brackets are listed in §6.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Rules for honest benefits](#3-rules-for-honest-benefits)
4. [Worked example](#4-worked-example)
5. [Output](#5-output)
6. [Sources](#6-sources)

## 1. Goal and exit criteria

**Goal.** Know what the portfolio has delivered, with the counterfactual stated, and decide where freed capacity
goes. Benefits-realisation practice asks for an owner per benefit, measurement timing, reviews after go-live and a
comparison with the business case [AUSGOV-2013; IVI-ITCMF-n.d.].

**Exit criteria.**

- Every item at or past `g3` has one row per benefit, with owner, baseline, forecast range, counterfactual and
  measurement; actuals at each review as ranges with their basis; status by `../schemas/benefits.md`.
- Use-case and enterprise rows kept apart; portfolio measures computed for the review (§3.3).
- For capacity benefits: the absorbed, redeployed and cashable split and a recorded redeploy-or-reduce decision,
  with role evolution in `portfolio.yaml`.

## 2. How to run it

1. **Create rows before `g3`.** For each lever in the item's `value`, one row: copy the forecast range and
   assumptions; name the metric and the benefit owner (a role in the business).
2. **Baseline from records** before launch, labelled with its basis [AUSGOV-2013].
3. **Agree the counterfactual** before launch (§3.1) and write the attribution note: what else ships at the same
   time and how its effect is separated. Deloitte's interviewees name AI entangled with broader transformation
   among the reasons value is hard to attribute [DELOITTE-2025].
4. **Collect actuals** at each review after go-live, from the agreed measure; record ranges and basis.
5. **Set status** and, for capacity, the split and the decision (§3.2). Ask the benefit owner, one question at a
   time; read `people-and-change.md` before the capacity conversation.
6. **Keep what was not achieved.** Record not-realised and withdrawn benefits with lessons [IVI-ITCMF-n.d.].
7. **Compute the portfolio measures** for the review pack, and update `updated`.

## 3. Rules for honest benefits

### 3.1 Counterfactual and attribution

| Method | Use when | Strength |
|---|---|---|
| `control-group` | Some clients, offices or teams can go without the change for a period | Strongest; DBS reports deriving its economic value by comparing customers offered AI-driven solutions with a control group (self-reported) [FCC-2026] |
| `staggered-start` | Roll-out happens site by site anyway | Strong if sites are comparable |
| `parallel-run` | The same items can be done both ways | Strong for quality and time per item |
| `baseline-comparison` | Only before-and-after is possible | Weak when other change ships at once |
| `assumption` | Nothing else is possible | State it; confidence cannot be high |

### 3.2 Capacity: redeploy or reduce

- **Split hours three ways** (`../../../transformation-advisor/references/method/business-case.md` §3.2):
  absorbed (counts as zero), redeployed (a named destination with an owner and an output metric), cashable (cost
  that actually goes away). Only cashable hours carry money as a cost saving.
- **Decide openly, at the level of roles and capacity** (rule 2), on realised, not forecast, value. The options and
  the checks before any reduction are in `../../../transformation-advisor/references/method/people-and-change.md`
  §5.
- Record the decision in the benefit row (`capacity.decision`, `decided_at_review`) and `role_evolution` on the
  item.

### 3.3 Portfolio measures and review points

From IVI's benefits-harvesting metrics [IVI-ITCMF-n.d.]: share of items with a benefits owner; share reviewed after
go-live; benefit success rate (share of targeted benefits actually achieved). Report use-case effects and
enterprise P&L effects separately [MCK-2026]. Review benefits at each portfolio review once an item is live, and
hold a post-implementation review once enough cases have run [IVI-ITCMF-n.d.; AUSGOV-2013]. Set each benefit's
planned review point at `g3`; do not judge a benefit `not-realised` before it.

### 3.4 Private-equity-owned firms

Link each item to its line in the value creation plan and the EBITDA bridge, and record the deal's AI lines as
`level: enterprise` rows. Never sum use-case rows into an enterprise figure.

## 4. Worked example

*Illustrative.* Before `g3`, the tax practice leader is named benefit owner for `b-tax-k1-hours`. Baseline: 2.1
preparer hours per K-1-heavy return, from time records. Forecast: 0.3 to 0.8 hours saved per return.
Counterfactual: staggered start (two offices begin a season later); the attribution note says a new review
checklist ships in all offices at once, so its effect is common to both groups. At review 4 the pilot offices show
0.4 to 0.6 hours saved against flat comparison offices: `tracking`, confidence medium. The forum decided at review 3
to redeploy most hours to advisory reviews for existing clients. The row stays a use-case row.

## 5. Output

`portfolio/benefits.yaml` from `../templates/benefits.yaml` (schema `../schemas/benefits.md`): rows created before
`g3`, actuals and status at each review, capacity decisions. In `portfolio.yaml`: `benefits` ids and
`role_evolution` per item. Portfolio measures go into the review pack. Update `updated`.

## 6. Sources

- `AUSGOV-2013` — Australian Government, Department of Finance, *Gateway Reviews lessons learned: Gate 5, Benefits Realisation Review*, government guidance, 2013-10. https://www.finance.gov.au/sites/default/files/2019-11/Gate_5_-_Lessons_Learned.pdf
- `DELOITTE-2025` — Deloitte, *AI ROI: the paradox of rising investment and elusive returns*, consultancy survey, 2025-10-22. https://www.deloitte.com/global/en/issues/generative-ai/ai-roi-the-paradox-of-rising-investment-and-elusive-returns.html
- `FCC-2026` — Business Times (via French Chamber of Commerce in Singapore), *DBS says AI push is paying off*, news report, 2026-02-09. https://www.fccsingapore.com/news/n/news/dbs-says-ai-push-is-paying-off-as-it-shifts-from-efficiency-tool-to-growth-engine.html
- `IVI-ITCMF-n.d.` — Innovation Value Institute, *Benefits Harvesting (IT-CMF 18.07)*, maturity-model guidance, undated. https://portal.ivi.ie/+itcmf/18.07/value/BAR/C/C3
- `MCK-2026` — McKinsey & Company, *The state of AI in 2026*, consultancy survey, 2026-08. https://www.mckinsey.com.br/en/our-insights/the-state-of-ai

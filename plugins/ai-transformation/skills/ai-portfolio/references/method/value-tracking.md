# Value tracking (step 6)

Read this on entering step 6: when an item approaches `g3`, when a review needs benefits figures, or when the user
asks what the portfolio has delivered. It tells you how to keep the benefits register: forecast against realised
value by named metric, attribution notes, and the redeploy-or-reduce choice on freed capacity. Keys in brackets are
listed in §9.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Rules for honest benefits](#3-rules-for-honest-benefits)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example: the K-1 benefit](#7-worked-example-the-k-1-benefit)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** Know what the portfolio has delivered, with the counterfactual stated, and decide where freed capacity
goes. Benefits-realisation practice asks for an owner per benefit, measurement and collection timing, reviews after
go-live and a comparison with the business case [AUSGOV-2013; IVI-ITCMF-n.d.]. Design tracking at intake, because
value is slow and hard to attribute: Deloitte's interviewees name AI entangled with broader transformation and
siloed data among the reasons [DELOITTE-2025].

**Exit criteria.**

- Every item at or past `g3` has one row per benefit in `benefits.yaml`, each with owner, baseline, forecast range,
  counterfactual and measurement.
- Actuals recorded at each review, as ranges with their basis; status set by the rules in `../schemas/benefits.md`.
- Use-case rows and enterprise rows kept apart.
- For capacity benefits: hours split into absorbed, redeployed and cashable, and a recorded redeploy-or-reduce
  decision, with role evolution in `portfolio.yaml`.
- Portfolio measures computed for the review (§3.3).

## 2. How to run it

1. **Name the step.** "We are tracking value: what was forecast, what has been realised, and where the time goes."
2. **Create rows before `g3`.** For each lever in the item's `value`, one row: copy the forecast range and
   assumptions; name the metric and the benefit owner (a role in the business).
3. **Baseline from records** before launch, labelled with its basis [AUSGOV-2013].
4. **Agree the counterfactual** before launch (§3.1) and write the attribution note: what else ships at the same
   time and how its effect is separated [DELOITTE-2025].
5. **Collect actuals** at each review after go-live, from the agreed measure; record ranges and basis.
6. **Set status** and, for capacity, the split and the decision (§3.2). Ask the benefit owner, one question at a
   time; read `people-and-change.md` before the capacity conversation.
7. **Keep what was not achieved.** Record not-realised and withdrawn benefits with lessons; they stay on the
   benefits action plan [IVI-ITCMF-n.d.; AUSGOV-2013].
8. **Compute the portfolio measures** for the review pack, and update `updated`.

## 3. Rules for honest benefits

### 3.1 Counterfactual and attribution

| Method | Use when | Strength |
|---|---|---|
| `control-group` | Some clients, offices or teams can go without the change for a period | Strongest; DBS reports deriving its economic value by comparing customers offered AI-driven solutions with a control group (self-reported; method described in press) [FCC-2026] |
| `staggered-start` | Roll-out happens site by site anyway | Strong if sites are comparable |
| `parallel-run` | The same items can be done both ways | Strong for quality and time per item |
| `baseline-comparison` | Only before-and-after is possible | Weak when other change ships at once |
| `assumption` | Nothing else is possible | State it; confidence cannot be high |

The DBS case also shows the limit: its CEO expects value harder to isolate as AI is embedded in daily work
[FCC-2026]. DBS reports about SGD 1 billion of economic value from data analytics and AI/ML in 2025 (self-reported;
scope wider than generative AI; not independently audited) [DBS-2026].

### 3.2 Capacity: redeploy or reduce

- **Split hours three ways**, as in `../../../transformation-advisor/references/method/business-case.md` §3.2:
  absorbed (counts as zero), redeployed (a named destination with an owner and an output metric), cashable (cost
  that actually goes away). Only cashable hours carry money as a cost saving.
- **Decide openly, at the level of roles and capacity** (rule 2). The options and the checks before any reduction
  are in `../../../transformation-advisor/references/method/people-and-change.md` §5: realised or expected, quality
  rollback, the junior pipeline, the honest reason.
- **Decide on realised, not forecast, value.** No source found describes how organizations make this choice after
  launch. In McKinsey's 2026 global survey, 14% of respondents from organizations using AI report an AI-related
  decline in workforce size over the past year, against 32% who, in the previous year's survey, expected reductions
  (respondent-reported; an effect, not a method) [MCK-2026].
- Record the decision in the benefit row (`capacity.decision`, `decided_at_review`) and `role_evolution` on the item.

### 3.3 Portfolio measures

From IVI's benefits-harvesting metrics [IVI-ITCMF-n.d.]: share of items with a benefits owner; share reviewed after
go-live; benefit success rate (share of targeted benefits actually achieved); share of business cases that are
benefits-led. Report use-case effects and enterprise P&L effects separately [MCK-2026].

### 3.4 Review points

Review benefits at each portfolio review once an item is live, and hold a post-implementation review after enough
cases have run to measure; IVI tracks whether a review happens within six months of completion, and the
Australian Gate 5 guidance recommends a post-implementation review focused on learnings and broader benefits
[IVI-ITCMF-n.d.; AUSGOV-2013]. Set the planned review point for each benefit at
`g3`; do not judge a benefit `not-realised` before it.

### 3.5 Private-equity-owned firms

Link each item to its line in the value creation plan and the EBITDA bridge. Bain reports that expensive deals now
need annual EBITDA growth closer to 10-12%, against about 5% in the past, to reach their return targets
(consultancy analysis) [BAIN-2026-PE]. The only quantified PE AI example found is Partners Group's report of 120 bps
of EBITDA margin (USD 10 million) at one insurance brokerage, built on a clean policy-level dataset (self-reported;
no baseline, period or method given) [PARTNERS-2026].

## 4. Question bank

Tags: **[U]** unit or practice, **[O]** organization.

**Core**
- What is the baseline, and who measured it? [U] [AUSGOV-2013]
- What is the counterfactual, and what other change ships at the same time? [U] [FCC-2026; DELOITTE-2025]
- When will benefits be reviewed after go-live, and by whom? [U] [IVI-ITCMF-n.d.]
- What happens to the time freed up: redeployed, absorbed or removed from budget? [U]
- How many of last period's forecast benefits were actually achieved? [O] [IVI-ITCMF-n.d.]

**Follow-ups**
- How do we separate use-case savings from firm-level P&L impact? [O] [MCK-2026]
- Would the finance director accept this number? [O]
- Which line of the value creation plan does this item move? [O] [BAIN-2026-PE]
- What did we expect and not get, and what do we do about it? [U] [AUSGOV-2013]

## 5. Expert moves

| Move | When | What it reveals |
|---|---|---|
| **Agree the counterfactual before launch** | `g3` | Unattributable benefits [FCC-2026] |
| **Ask what other change is shipping alongside the AI** | `g3`, every review | Entangled attribution [DELOITTE-2025] |
| **Separate use-case impact from enterprise P&L** | Every report | The gap between function-level effects and EBIT [MCK-2026] |
| **Name the benefit owner and count the owners at review** | Intake, every review | Orphan benefits; 24 of 32 UK government bodies with deployed AI said their AI use cases always or usually had a named accountable owner (NAO survey, autumn 2023) [NAO-2024] |
| **Record benefits expected but not achieved** | Post-implementation review | What to redirect effort toward or write off [AUSGOV-2013; IVI-ITCMF-n.d.] |
| **Trace each item to the EBITDA bridge in a PE setting** | PE-owned firms | Work that cannot move the metric the owner underwrites [BAIN-2026-PE; PARTNERS-2026] (derived) |

## 6. Common traps

| Trap | How to avoid it |
|---|---|
| **Forecast reported as realised** | Status per row; realised only on actuals and the agreed counterfactual |
| **Hours counted as money** | Absorbed, redeployed, cashable; money only for cashable |
| **No baseline.** In the Thomson Reuters Institute's 2026 survey of legal, tax and accounting, corporate and government professionals, 18% knew their organization tracked the ROI of AI tools (respondent-reported) [TRI-AIPS-2026] | No row passes `forecast` without a baseline |
| **Summing use-case rows into a P&L claim** [MCK-2026] | Enterprise rows only from finance-recognized lines |
| **Expecting payback in months** [DELOITTE-2025] | Planned review points set at `g3` |
| **Survey figures used as benchmarks.** Wharton and GBK's 2025 survey of about 800 US enterprise decision makers reports 72% tracking structured, business-linked ROI metrics (respondent-reported), far above the TRI figure; the samples differ [WHARTON-2025; TRI-AIPS-2026] | Use surveys as context, never as targets |

## 7. Worked example: the K-1 benefit

*Illustrative*, continuing the firm. Before `g3`, the tax practice leader is named benefit owner for
`b-tax-k1-hours`. Baseline: 2.1 preparer hours per K-1-heavy return, from last season's time records. Forecast:
0.3 to 0.8 hours saved per return. Counterfactual: staggered start; two offices begin a season later. Attribution
note: a new review checklist ships in all offices at once, so its effect is common to both groups.

At review 4 the pilot offices show 0.4 to 0.6 hours saved per return against flat comparison offices: status
`tracking`, confidence medium. At review 3 the forum had decided capacity: most released hours redeployed to advisory
reviews for existing clients (output metric: advisory reviews completed), some absorbed, a little cashable through
less seasonal contract preparer time. Role evolution: preparers move from keying data to checking flagged fields and
preparing advisory reviews; the firm's junior learning route for data review is kept as a training task. The row
stays a use-case row; the firm-level effect will be judged from advisory fees in the finance director's reporting.

## 8. Output

`portfolio/benefits.yaml` from `../templates/benefits.yaml` (schema `../schemas/benefits.md`): rows created before
`g3`, actuals and status at each review, capacity decisions. In `portfolio.yaml`: `benefits` ids and
`role_evolution` per item. Portfolio measures go into the review pack. Update `updated`.

## 9. Sources

- `AUSGOV-2013` — Australian Government, Department of Finance, *Gateway Reviews lessons learned: Gate 5, Benefits Realisation Review*, government guidance, 2013-10. https://www.finance.gov.au/sites/default/files/2019-11/Gate_5_-_Lessons_Learned.pdf
- `BAIN-2026-PE` — Bain & Company, *Global private equity report 2026*, consultancy report, 2026. https://www.bain.com/globalassets/noindex/2026/bain-report_global-private-equity-report-2026.pdf
- `DBS-2026` — DBS Bank, *DBS named Asia's Best Digital Bank by Euromoney*, company release, 2026-07-20. https://www.dbs.com/newsroom/DBS_named_Asias_Best_Digital_Bank_by_Euromoney_recognised_for_its_AI_leadership_and_responsible_innovation
- `DELOITTE-2025` — Deloitte, *AI ROI: the paradox of rising investment and elusive returns*, consultancy survey, 2025-10-22. https://www.deloitte.com/global/en/issues/generative-ai/ai-roi-the-paradox-of-rising-investment-and-elusive-returns.html
- `FCC-2026` — Business Times (via French Chamber of Commerce in Singapore), *DBS says AI push is paying off*, news report, 2026-02-09. https://www.fccsingapore.com/news/n/news/dbs-says-ai-push-is-paying-off-as-it-shifts-from-efficiency-tool-to-growth-engine.html
- `IVI-ITCMF-n.d.` — Innovation Value Institute, *Benefits Harvesting (IT-CMF 18.07)*, maturity-model guidance, undated. https://portal.ivi.ie/+itcmf/18.07/value/BAR/C/C3
- `MCK-2026` — McKinsey & Company, *The state of AI in 2026*, consultancy survey, 2026-08. https://www.mckinsey.com.br/en/our-insights/the-state-of-ai
- `NAO-2024` — UK National Audit Office, *Use of artificial intelligence in government*, audit report, 2024-03-15. https://www.nao.org.uk/wp-content/uploads/2024/03/use-of-artificial-intelligence-in-government.pdf
- `PARTNERS-2026` — Partners Group (via Deutsche Boerse press feed), *Partners Group drives EBITDA margin uplift through AI collaboration between private equity portfolio companies*, press release, 2026-08-03. https://live.deutsche-boerse.com/news/Partners-Group-drives-EBITDA-margin-uplift-through-AI-collaboration-between-private-equity-portfolio-companies-a1ffb3cd-e01e-4242-a263-2626ccb76132
- `TRI-AIPS-2026` — Thomson Reuters Institute, *2026 AI in professional services report*, survey report summary, 2026-02-09. https://www.thomsonreuters.com/en-us/posts/technology/ai-in-professional-services-report-2026/
- `WHARTON-2025` — Wharton Human-AI Research and GBK Collective, *Accountable acceleration: Gen AI fast-tracks into the enterprise*, survey report, 2025-10. https://ai.wharton.upenn.edu/wp-content/uploads/2025/10/2025-Wharton-GBK-AI-Adoption-Report_Full-Report.pdf

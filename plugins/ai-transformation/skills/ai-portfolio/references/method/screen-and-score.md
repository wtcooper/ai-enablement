# Screen and score (step 3)

Read this on entering step 3. It tells you how to screen intake items and score them with the suite's six
scoring dimensions and the portfolio's weights, split into two axes, value and readiness, and how to record the
screening gate (`g0`). Keys in brackets are listed in §9.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Axes, rules and thresholds](#3-axes-rules-and-thresholds)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example: four items at the screen](#7-worked-example-four-items-at-the-screen)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** Decide which ideas earn discovery effort, with the reasons visible. Screening asks two questions: is
it worth it, and is it ready? Cooper keeps business-value criteria apart from project-readiness criteria at every
gate, and pairs any financial model with a scorecard because financial inputs are uncertain or biased
[COOPER-STAGEGATE-n.d.]. Treat the scores as a facilitation device, not a validated model (as the shared
prioritize method says).

**Exit criteria** for each screened item:

- Passed the pre-score gates (§3.1), or closed with the reason.
- A value range per lever (`low`, `high`, `unit`, `assumptions`). No range, no value score.
- Six scores with what each rests on; `weighted_score`, `value_index` and `readiness_index`.
- The readiness checklist (§3.3) answered.
- `category`, `horizon`, `risk_tier`, `gate_path` and a sponsor who controls discovery resources.
- A `g0` decision: Go into discover, Kill, Hold (with `revisit_when`) or Recycle (back to the submitter with what
  to rework). Every Go carries `kill_criteria` and `next_gate`.

## 2. How to run it

1. **Name the step.** "We are screening: is each idea worth it and ready for it? Next come the gates."
2. **Confirm the weights** from `settings.scoring_weights`. Do not re-open them item by item; recalibration
   happens at a rebalance review [HBR-2026].
3. **Run the pre-score gates** (§3.1) on each item.
4. **Size as ranges.** Per lever: low, high, unit and the main assumption, from the volume recorded at intake.
5. **Score across, not down.** One dimension at a time across all items, using the anchors in
   `../../../transformation-advisor/references/method/prioritize.md` §3.3. Say what each score rests on.
6. **Compute** `weighted_score` and the two indexes (§3.2). Show the items on the two axes.
7. **Answer the readiness checklist** (§3.3). A weak answer lowers feasibility or data readiness, or becomes a
   condition on the Go.
8. **Categorize** with the shared category rules (prioritize §3.4) and set the horizon.
9. **Check against the portfolio**: duplicates, dependencies on foundation items, the live limit and the balance.
10. **Record the `g0` decision** (§3.4) with the sponsor and the gatekeepers set in step 1. On the light path the
    portfolio owner decides alone. Play back, write, update state.

## 3. Axes, rules and thresholds

### 3.1 Pre-score gates

Use the shared gates first (should it exist, rules, simpler fix, constraint, stage; prioritize §3.2), then two
portfolio checks:

| Check | Test | If it fails |
|---|---|---|
| Worth a year | "What would have to be true for this to be worth a year of a team's time?" RAND recommends committing product teams to a specific problem for at least a year [RAND-2024] | Kill or park as a passing idea |
| Right metric | The metric the team would optimize is the one the business owner cares about; RAND's interviewees described models optimized for the wrong metrics [RAND-2024] | Recycle with the metric agreed with the benefit owner |

### 3.2 Two axes from six scores

The six dimensions and their weights come from the shared library (§6). This skill splits them into two axes
(skill heuristic):

| Axis | Dimensions | Plain question |
|---|---|---|
| **Value** | value, strategic fit, time to value | "Is it worth it?" |
| **Readiness** | feasibility, data readiness, risk (higher score = lower risk) | "Can we do it safely now?" |

Each index is the weighted mean of its three scores, with the portfolio's weights renormalized within the axis.
Report both indexes next to `weighted_score`; never let a high value index hide a low readiness index. HBR's
Buy/Sell/Hold backlog scoring uses strategic alignment, feasibility, risk-reward and resource requirements, a
similar split [HBR-2026].

**Quadrants and the usual `g0` outcome** (proposed default thresholds; no source sets them):

| | Readiness ≥ 3.5 | Readiness < 3.5 |
|---|---|---|
| **Value ≥ 3.5** | Go to discover | Go with readiness work named as conditions, or Hold behind a foundation item logged in its own right |
| **Value < 3.5** | Go only on the light path and if cheap; else Hold or Kill | Kill, or Hold with a `revisit_when` trigger |

When scoring feasibility, count people-and-process readiness (an owner, process redesign, adoption) at least as
much as technical feasibility; BCG attributes about 70% of implementation challenges to people and process (survey
of 1,000 executives) [BCG-2024]. That weighting is a proposed default, not BCG's.

### 3.3 Readiness checklist

From HBR's gate tests and Microsoft's data inventory [HBR-2026; MSFT-PLAN-2026]: owner named; benefit owner named
or a step to name one; data sources, formats, quality and access known; skills in place or a route to source
them; whether the process needs redesign and who owns that; the controls the risk tier needs.

### 3.4 Payback hurdles and spend thresholds

- **Do not apply a technology-style payback hurdle.** Most of Deloitte's EMEA respondents reported reaching
  satisfactory ROI on a typical AI use case in two to four years, against the seven to 12 months usually
  expected of technology investment; 6% reported payback under a year (respondent-reported) [DELOITTE-2025].
  Google Cloud's survey of gen-AI-in-production users reports 74% saying ROI arrived within the first year
  (vendor-published) [GOOGLE-2025]. The surveys differ in who was asked and who published, and Google's question
  wording is ambiguous, so do not use the 74% to set hurdles.
- **Different hurdles by type.** 85% of Deloitte's "ROI Leaders" use different frameworks or timeframes for
  generative and agentic AI (respondent-reported) [DELOITTE-2025]. Set hurdles per `item_class` in step 1.
- **Spend thresholds that trigger heavier governance** are a rule to set, not a universal number. UK government
  practice gives one example: a five-part business case typically for investment approaching GBP 10 million
  [UKGOV-2025].

## 4. Question bank

Tags: **[T]** team, **[U]** unit or practice, **[O]** organization.

**Core**
- For each candidate: how well does it fit the strategy, how feasible is it, what is the risk and reward, and what
  resources does it need? Which has the weakest evidence? [U] [HBR-2026]
- What data does this need, who owns it, and has anyone looked at it in its real state? [T]
- Do the people who would build it have the skills, or would you source them? [T] [HBR-2026]
- What is the risk tier of this item, and does that change its path? [O] [OMB-2025]
- What would have to be true for this to be worth a year of a team's time? [U] [RAND-2024]

**Follow-ups**
- Is any proposed item a duplicate of work in another practice? [U]
- Which metric would the team optimize, and is it the one the benefit owner watches? [T] [RAND-2024]
- What has to be in place first: data, written criteria, a platform, a policy? [U]
- If this works, what happens to the hours: redeployed, absorbed or removed from budget? [U]

## 5. Expert moves

| Move | When | What it reveals |
|---|---|---|
| **Score readiness and value on separate axes and keep both visible** | Every screen and gate | Attractive-but-unready items versus ready-but-trivial ones [COOPER-STAGEGATE-n.d.; HBR-2026] |
| **Rank with fixed criteria, then pull the next item only when capacity opens** | When the queue is longer than the live limit | Whether the loudest sponsor or the score sets priorities; HBR describes advancement decided by resource availability and fixed criteria [HBR-2026] |
| **Check the metric the team optimizes against the business metric** | Screen, and again at `g1` | Work aimed at the wrong objective [RAND-2024] |
| **Ask for the realistic payback window by item class** | Setting hurdles | Unrealistic twelve-month hurdles [DELOITTE-2025] |
| **Record the build, buy or partner leaning now** | Screen, confirmed at `g2` | Slow custom builds that a bought tool would cover; MIT NANDA's interview-based finding is that external partnerships succeeded about twice as often as internal builds (directional) [MITNANDA-2025] |
| **Tier the path by risk** | Setting `gate_path` | Gate fatigue on low-risk items [HBR-2026; OMB-2025] |

## 6. Common traps

| Trap | How to avoid it |
|---|---|
| **AI where simple rules suffice** [RAND-2024] | The rules-or-AI check at intake; the simpler-fix gate here |
| **Optimizing for the wrong problem.** In RAND's 65 interviews, 84% cited leadership-driven failures as a primary cause (interviewee perceptions) [RAND-2024] | Metric agreed with the benefit owner before Go |
| **Funding visible functions over high-return ones.** MIT NANDA reports budgets skewed to sales and marketing while back-office automation often yields better ROI; its own figures for the skew are inconsistent (50% in one place, about 70% in another) [MITNANDA-2025] | Score on value and readiness, not visibility; check the budget split at rebalance |
| **One blended number** | Show both indexes; a Go on a low-readiness item names the readiness work |
| **Expecting short payback** | Class-specific hurdles; hold decisions that allow for ramp-up |
| **Scoring down, item by item** | Score across, one dimension at a time |

## 7. Worked example: four items at the screen

*Illustrative scores*, continuing the firm. Weights are the defaults (value 0.30, feasibility 0.20, data
readiness 0.15, risk 0.15, time to value 0.10, strategic fit 0.10). V, SF, T form the value axis; F, D, R the
readiness axis.

| Item | V | SF | T | F | D | R | Weighted | Value idx | Ready idx | `g0` |
|---|---|---|---|---|---|---|---|---|---|---|
| K-1 extraction (`tax-compliance-individual-business-02`, grade B) | 4 | 4 | 4 | 4 | 3 | 3 | 3.70 | 4.00 | 3.40 | Go, with "data seen in real state" as a `g1` condition |
| Proposal first drafts (`professional-services-pursuit-proposals-01`, grade B), merged duplicate | 3 | 4 | 4 | 4 | 4 | 4 | 3.70 | 3.40 | 4.00 | Go, light path |
| Know-how search over the precedent library (`professional-services-knowledge-management-01`, grade B) | 4 | 4 | 2 | 3 | 2 | 4 | 3.30 | 3.60 | 3.00 | Hold behind a new foundation item: clean up the library first |
| Client-facing tax chatbot | 3 | 2 | 2 | 2 | 2 | 1 | 2.15 | 2.60 | 1.70 | Kill: client-facing advice with no checkpoint, low readiness |

The know-how search shows why the axes matter: its weighted score looks acceptable, but readiness sits below the 3.5 line, held down by data readiness. The
forum logs "library clean-up" as a foundation item and sets the search's `revisit_when` to "clean-up item passes
`g2`". The K-1 Go names its resources: a preparer and the tax operations manager part-time for discovery, released
by the tax practice leader. Kill criteria agreed: the documents cannot be read reliably on a sample of last season's
returns.

## 8. Output

Per item in `portfolio.yaml`: `value`, `scores`, `weighted_score`, `value_index`, `readiness_index`, `category`,
`horizon`, `risk_tier`, `gate_path`, `sponsor`, `depends_on`, a `g0` entry in `decisions`, and on a Go
`stage: discover`, `status: active`, `kill_criteria` and `next_gate`. Fill the intake record's "Screen result".
Update `state` and `updated`.

## 9. Sources

- `BCG-2024` — Boston Consulting Group, *AI adoption in 2024: 74% of companies struggle to achieve and scale
  value*, press release, 2024-10-24. https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
- `COOPER-STAGEGATE-n.d.` — Robert G. Cooper, Stage-Gate International, *The Stage-Gate model: an overview*,
  method article, undated. https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- `DELOITTE-2025` — Deloitte, *AI ROI: the paradox of rising investment and elusive returns*, consultancy survey
  of 1,854 executives in 14 EMEA countries, 2025-10-22. https://www.deloitte.com/global/en/issues/generative-ai/ai-roi-the-paradox-of-rising-investment-and-elusive-returns.html
- `GOOGLE-2025` — Google Cloud with National Research Group, *The ROI of AI 2025*, vendor survey, 2025.
  https://services.google.com/fh/files/misc/google_cloud_roi_of_ai_2025.pdf
- `HBR-2026` — Nelson, Davenport, Scade, *Manage your AI investments like a portfolio*, Harvard Business
  Review, 2026-01 (read via reprint). https://hbr.org/2026/01/manage-your-ai-investments-like-a-portfolio
- `MITNANDA-2025` — MIT Project NANDA, *The GenAI divide: state of AI in business 2025*, research report
  (preliminary), 2025-07. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `MSFT-PLAN-2026` — Microsoft Learn, *Plan for AI adoption*, vendor guidance, updated 2026-10-15.
  https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/plan
- `OMB-2025` — US Office of Management and Budget, *M-25-21*, government memorandum, 2025-04-03.
  https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf
- `RAND-2024` — RAND Corporation, *The root causes of failure for artificial intelligence projects and how they
  can succeed*, research report, 2024-08-13. https://www.rand.org/pubs/research_reports/RRA2680-1.html
- `UKGOV-2025` — UK Government Digital Service, *Artificial Intelligence Playbook for the UK Government*,
  government guidance, 2025. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html

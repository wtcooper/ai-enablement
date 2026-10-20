# Portfolio review (step 5)

Read this on entering step 5: when a review is due, or when the user asks to "review our AI portfolio". It tells
you how to build the review pack, surface stop, redirect and scale decisions with the evidence behind them, run
the rebalance, and record what the forum decided. Keys in brackets are listed in §9.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [What to surface and how](#3-what-to-surface-and-how)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example: review 3](#7-worked-example-review-3)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** A forum that decides, not one that hears status. HBR lists what regular reviews should do: add promising
initiatives, scale successful pilots, redirect struggling efforts, retire misaligned projects and recalibrate
scoring criteria [HBR-2026]. The pack makes those decisions easy to take and hard to dodge.

**Exit criteria.**

- A numbered pack `reviews/<n>-review.md` (Part A) built from `portfolio.yaml` and `benefits.yaml`.
- Every item that meets a surfacing rule (§3.1) appears under "Decisions asked", with evidence for and against.
- Part B records each decision with reason, resources or conditions, next gate and the roles who decided.
- `portfolio.yaml` updated: decisions carry the review number; `early_warnings`; `state.last_review`.
- On a rebalance review: balance, weights, live limit and the central team's signals checked (§3.3).

## 2. How to run it

1. **Name the step.** "We are preparing review <n>: the pack first, then the decisions."
2. **Build the pipeline view**: counts by stage, changes since the last review, live items against the limit,
   the enablement line apart.
3. **Run the surfacing rules** (§3.1) on every active item. For a large portfolio, use the `prepare-review-item`
   brief, one subagent per flagged item (see `SKILL.md`, Delegation).
4. **Write a decision block** for each surfaced item: the ask, evidence for, evidence against, the kill criteria
   and whether any is met, early warnings, two or three options with what each costs and releases, and the
   owner's recommendation. Lead with evidence; label where each fact came from.
5. **Add the balance, benefits and capacity sections** (template §5 to §7).
6. **Play the pack back** to the user and ask: "Which decision here would you least like to take, and why?"
   The answer is usually the one the pack must make clearest.
7. **After the meeting**, record Part B as the user reports it. Record decisions; do not make them.
8. **Update** `portfolio.yaml` and, for benefits decisions, `benefits.yaml`. Set `state.last_review`.

## 3. What to surface and how

### 3.1 Surfacing rules

Surface an item for a decision when any of these holds (proposed defaults built on the cited practice):

| Rule | Typical ask | Basis |
|---|---|---|
| A kill criterion agreed at the last gate is met | Kill or recycle | [COOPER-STAGEGATE-n.d.] |
| An early warning (slippage, cost overrun, performance shortfall) on two reviews running | Redirect, hold or kill | Early-warning triggers reviewed at each review [HBR-2026] |
| Next-gate evidence not produced when the gate falls due | Hold or recycle | |
| Owner or benefit owner lost | Hold until replaced, or kill | |
| A technology change makes the build unnecessary | Recycle to buy | Lloyds' acceptance of switching [HBR-2026] |
| A benefit is `not-realised` at its planned review point | Redirect or retire | [IVI-ITCMF-n.d.; AUSGOV-2013] |
| Pilot evidence meets `g3` or production evidence meets `g4` | Go to production or scale | |
| Highest-scoring held item, when live capacity opens | Go | Advancement by resources and fixed criteria [HBR-2026] |

### 3.2 Evidence that should drive a stop or redirect

Use the causes in `stage-gates.md` §5.1. Before recommending a stop on value alone, check the J-curve point:
measured value can lag the investment (model and historical analysis) [NBER-2020]. Report leading indicators
(adoption quality, process change, error rates) at early reviews.

### 3.3 Rebalance review

At the reviews set in step 1, add:

- **Balance:** near, medium and long horizons; risk and return; capability areas; foundations that later items need
  [HBR-2026]. A portfolio of only quick wins or only moonshots is a finding.
- **Recalibrate criteria and weights** if the forum's decisions keep overriding the scores [HBR-2026].
- **Budget split by function and practice:** check that the visible functions are not crowding out higher-return
  back-office work [MITNANDA-2025].
- **Live limit:** owners carrying more than one live item; shared reviewers stretched.
- **The central team's signals:** approval delays, experts who cannot cover all teams, recurring priority debates
  [MSFT-COE-2026].
- **Spend context**, if the forum asks how its AI budget compares: 28% of McKinsey's respondents spend more than
  10% of their ICT budget on AI (respondent-reported) [MCK-2026]; 95% of Deloitte's "ROI Leaders" allocate more
  than 10% (respondent-reported) [DELOITTE-2025]. Different samples; context only, not a target.

### 3.4 In a partner-led firm

- Lead each decision block with a named workflow and its baseline, not a tool demo (an inference from the
  partner sources) [PAPERJAM-2025; TRI-AIPS-2026].
- Dependence is persuasive evidence: an A&O Shearman partner recalls asking lawyers six months after roll-out
  whether the tool could be taken away (her recollection, self-reported) [PAPERJAM-2025]. Report such answers as
  self-reported.
- Check how claimed time savings were measured before they enter the pack; lawyers' and consultants' own estimates
  are self-reported [PAPERJAM-2025; LEXIS-CONSULT-2025].
- Separate usage from value. In a Thomson Reuters Institute survey, 18% of professional-services respondents knew
  their organization tracked AI ROI (respondent-reported) [TRI-AIPS-2026].

## 4. Question bank

Tags: **[U]** unit or practice, **[O]** organization.

**Core**
- Who attends, what pack do they see, and what decisions does the meeting actually make? [O] [HBR-2026]
- Which items have tripped an early-warning trigger, and on what measure? [U] [HBR-2026]
- Is the portfolio balanced across near, medium and long-term items, and does it include foundation work? [O]
- How many of the benefits forecast for this period were achieved? [O] [IVI-ITCMF-n.d.]
- What would make you stop this item, and was it written down at the gate?

**Follow-ups**
- Is the central team still adding value, or has it become a queue? [O] [MSFT-COE-2026]
- Which items depend on the same scarce reviewers or partners? [O]
- What do we learn and reuse from the items stopped since the last review? [U] [AUSGOV-2013]
- What would a skeptical partner need to see to accept this decision? [U]

## 5. Expert moves

| Move | When | What it reveals |
|---|---|---|
| **Define early-warning triggers and review them every time** | Every review | Items needing intervention before their next gate [HBR-2026] |
| **Check balance and foundations, not only the ranking** | Rebalance | A portfolio of quick wins or moonshots, and missing foundations [HBR-2026; HBR-2018] |
| **Separate use-case results from enterprise P&L** | Benefits section | The gap between function-level effects and EBIT; 37% of McKinsey's respondents attribute at least some EBIT impact to AI (respondent-reported) [MCK-2026] |
| **Report seat roll-outs on the enablement line** | Pipeline view | Inflated pilot-to-production counts [MITNANDA-2025] (derived) |
| **Look for central-team bottleneck signs** | Rebalance | When to move to an advisory model [MSFT-COE-2026] |
| **Ask each skeptic what result would change their mind** | Before a contested decision | Whether evidence can settle the objection (an inference from the partner sources) [TRI-AIPS-2026] |

## 6. Common traps

| Trap | How to avoid it |
|---|---|
| **Status theatre:** updates with no decisions [UMBREX-n.d.] | Every surfaced item ends with a recorded outcome or a named open question |
| **Adoption reported as value.** 80% of McKinsey's respondents say AI improved individual productivity, against 37% reporting EBIT impact (respondent-reported) [MCK-2026] | Usage and value in separate lines |
| **Pilot sprawl** [HBR-2026] | Live limit; hold before adding |
| **Killing on early P&L** [NBER-2020; DELOITTE-2025] | Leading indicators until the planned review point |
| **Trusting self-reported adoption figures** | Ask how "use" was defined and measured [POLSINELLI-2026] |
| **The pack argues for an outcome** | Evidence for and against, options, then the owner's recommendation, clearly labelled |

## 7. Worked example: review 3

*Illustrative*, continuing the firm; a rebalance review. **Pipeline:** two at intake, three in discover, one in
prototype, two in pilot, one in production; live four of six. Enablement line: chat assistant licences issued to
two practices, reported apart.

**Decisions asked.** (1) K-1 extraction met its `g3` evidence: pilot offices show fewer preparer hours than the
comparison offices, within the forecast range; readiness signed. Ask: Go to production. (2) A document-summary
pilot in advisory shows slippage on two reviews running and its owner has moved practices. Ask: Hold until an
owner is named, or kill. (3) Know-how search is held behind the library clean-up, which has passed `g2`. Ask: Go
into discover as live capacity opens.

**Rebalance.** Four of five live items are near-horizon capacity plays; no item serves the growth lever. The forum
asks the advisory practice to bring a new-value idea through intake, and keeps the weights.

**Part B.** K-1: Go to production, with the capacity decision (redeploy to advisory reviews) recorded in
`benefits.yaml`. Document summary: Kill; the evaluation set and prompts kept for reuse; retire checklist opened.
Know-how search: Go into discover.

## 8. Output

`portfolio/reviews/<n>-review.md` from `../templates/review.md`. In `portfolio.yaml`: decisions with
`review: <n>`, `early_warnings`, stage and status changes, `state.last_review: <n>`, `state.step_completed: 5`,
`updated`. In `benefits.yaml`: status changes and capacity decisions taken in the review.

## 9. Sources

- `AUSGOV-2013` — Australian Government, Department of Finance, *Gateway Reviews lessons learned: Gate 5*, government guidance, 2013-10. https://www.finance.gov.au/sites/default/files/2019-11/Gate_5_-_Lessons_Learned.pdf
- `COOPER-STAGEGATE-n.d.` — Robert G. Cooper, Stage-Gate International, *The Stage-Gate model: an overview*, method article, undated. https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- `DELOITTE-2025` — Deloitte, *AI ROI: the paradox of rising investment and elusive returns*, consultancy survey, 2025-10-22. https://www.deloitte.com/global/en/issues/generative-ai/ai-roi-the-paradox-of-rising-investment-and-elusive-returns.html
- `HBR-2018` — Davenport and Ronanki, *Artificial intelligence for the real world*, Harvard Business Review, 2018-01. https://hbr.org/2018/01/artificial-intelligence-for-the-real-world
- `HBR-2026` — Nelson, Davenport, Scade, *Manage your AI investments like a portfolio*, Harvard Business Review, 2026-01 (read via reprint). https://hbr.org/2026/01/manage-your-ai-investments-like-a-portfolio
- `IVI-ITCMF-n.d.` — Innovation Value Institute, *Benefits Harvesting (IT-CMF 18.07)*, maturity-model guidance, undated. https://portal.ivi.ie/+itcmf/18.07/value/BAR/C/C3
- `LEXIS-CONSULT-2025` — LexisNexis, *Driving adoption: how consulting firms can manage change and overcome GenAI resistance*, vendor article, 2025-05-19. https://www.lexisnexis.com/community/insights/professional/b/industry-insights/posts/manage-change-ai-resistance
- `MCK-2026` — McKinsey & Company, *The state of AI in 2026*, consultancy survey, 2026-08. https://www.mckinsey.com.br/en/our-insights/the-state-of-ai
- `MITNANDA-2025` — MIT Project NANDA, *The GenAI divide: state of AI in business 2025*, research report (preliminary), 2025-07. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `MSFT-COE-2026` — Microsoft Learn, *Establish an AI Center of Excellence*, vendor guidance, updated 2026-04-10. https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/center-of-excellence
- `NBER-2020` — Brynjolfsson, Rock, Syverson, *The productivity J-curve*, NBER Working Paper 25148, rev. 2020-01. https://www.nber.org/system/files/working_papers/w25148/w25148.pdf
- `PAPERJAM-2025` — Paperjam, *Why AI is a strategic priority for modern law firms: Francesca Bennetts*, practitioner interview, 2025-06-19. https://en.paperjam.lu/article/why-ai-is-a-strategic-priority-for-modern-law-firms-francesca-bennetts
- `POLSINELLI-2026` — Bloomberg Law, On the Merits, *Why Polsinelli lawyers won't get billing credit for AI training*, podcast transcript, 2026-03-24. https://news.bgov.com/business-and-practice/why-polsinelli-lawyers-wont-get-billing-credit-for-ai-training
- `TRI-AIPS-2026` — Thomson Reuters Institute, *2026 AI in professional services report*, survey report summary, 2026-02-09. https://www.thomsonreuters.com/en-us/posts/technology/ai-in-professional-services-report-2026/
- `UMBREX-n.d.` — Umbrex, *Stage-gate project governance model*, secondary framework summary, undated. https://umbrex.com/resources/frameworks/organization-frameworks/stage-gate-project-governance-model/

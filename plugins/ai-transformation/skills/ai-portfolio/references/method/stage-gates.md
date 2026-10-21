# Stage gates (step 4)

Read this on entering step 4: when an item is due at a gate, or when someone asks whether to stop, hold or
scale an item outside a review. It defines the six stages, the entry and exit evidence for each gate, the four
outcomes, how to stop and retire safely, and when to hand an item to ai-solution-delivery. Keys in brackets are
listed in §11.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run a gate](#2-how-to-run-a-gate)
3. [Stages and gate evidence](#3-stages-and-gate-evidence)
4. [Outcomes and decision rules](#4-outcomes-and-decision-rules)
5. [Stopping and retiring](#5-stopping-and-retiring)
6. [Question bank](#6-question-bank)
7. [Expert moves and common traps](#7-expert-moves-and-common-traps)
8. [Worked example: the K-1 item and a recycle to buy](#8-worked-example-the-k-1-item-and-a-recycle-to-buy)
9. [Rollout playbook for acquired firms](#9-rollout-playbook-for-acquired-firms)
10. [Output](#10-output)
11. [Sources](#11-sources)

## 1. Goal and exit criteria

**Goal.** Each gate is a forward-looking decision about resources for the next stage, not a status review.
Cooper: gates are where resource commitments are made, with deliverables defined in advance, criteria of
readiness and value, and four outputs: Go, Kill, Hold or Recycle [COOPER-STAGEGATE-n.d.].

**Exit criteria** for each gate held:

- The evidence agreed at the previous gate was presented, or its absence recorded.
- The gatekeepers present control the resources the next stage needs.
- One outcome recorded with its reason and evidence; a Go names the resources, who releases them, the
  conditions, the next gate and the evidence it will need [COOPER-STAGEGATE-n.d.].
- Kill criteria for the next stage agreed now (proposed default).
- Handoffs made: to ai-solution-delivery by the time the item enters prototype (a brief may open earlier, in
  `discover`); benefits rows before `g3`. A `g0` Go does not set `solution`; set it only when
  `solutions/<id>/brief.md` exists and delivery has handed back.

## 2. How to run a gate

1. **Name the step.** "This is the gate from pilot to production: we decide whether to fund the next stage."
2. **Read the item** in `portfolio.yaml`: `next_gate.evidence`, `kill_criteria`, `early_warnings`, earlier
   decisions. If `solution` is set, read the files in `solutions/<id>/` that the gate needs.
3. **Check the evidence** against the exit evidence for this gate (§3), one line at a time. Mark each met, not
   met or not presented. Missing evidence is a finding, not a reason to guess. Before you flag a conflict between
   intake records, or between a record and the plan, read the plan section their "From the plan" lines name: the
   plan may already reconcile the figures (for example a total and the part of it one task takes).
4. **Check the kill criteria** agreed at the last gate. If one is met, say so first.
5. **Confirm the gatekeepers.** Ask who releases the people, budget or data for the next stage, and whether they
   are part of the decision.
6. **Lay out the options** (Go, Kill, Hold, Recycle) with what each costs and releases. The gatekeepers decide;
   you record. Never present your view as the decision.
7. **Record** the decision in `decisions` (append, never edit), update `stage`, `status`, `next_gate`,
   `kill_criteria`, and play it back. Before adding a field to the item, search that item for the key; if it is
   there, edit it in place. Never insert a second one.
8. **Track the next gate's evidence** in the intake record's "Next gate evidence" table: one row per item of
   `next_gate.evidence`, with its status, owner and what it needs first. Update the table as evidence arrives.
   Give drafted messages (an ask to a sponsor, a note to a manager) in the chat, or list them under the review
   pack's Actions. Do not create other files.
9. **Hand off** (§3.3) and update state.

## 3. Stages and gate evidence

### 3.1 Stages

The stages adapt Cooper's sequence (discovery, concept, business case, development, testing and validation, launch) and HBR's
four AI portfolio stages (outline, design and partnership, experiment, scale and operate)
[COOPER-STAGEGATE-n.d.; HBR-2026]. The six names are this skill's.

| Stage | Purpose | Typical work |
|---|---|---|
| `discover` | Frame the problem, find the baseline, look at the data | Problem and metric agreed with the benefit owner; baseline from records; data seen in its real state |
| `prototype` | Test technical feasibility on real data | Prototype on real, representative cases; build, buy or partner decided; solution brief and evaluation plan |
| `pilot` | Test value and adoption on live work | Real users on live work with a comparison; adoption, quality and run cost measured |
| `production` | Supported service for its first population | Production readiness signed off; benefits measured against the forecast |
| `scale` | Extend to more practices, offices or client groups | Reuse of components; enablement; control plan per site |
| `retire` | Decommission safely | Fallback, notification, records, lessons, reusable assets |

### 3.2 Gate evidence

| Gate | Exit evidence (all paths) | Added on the full path |
|---|---|---|
| `g0` screen | Intake complete; pre-score gates passed; two indexes; sponsor (`screen-and-score.md`) | — |
| `g1` discover → prototype | Problem and success metric agreed with the benefit owner [RAND-2024]; baseline from records; data located and seen in its real state; strategic fit and technical feasibility [HBR-2026] | Counterfactual idea; build, buy or partner leaning; risk tier confirmed against `overlay/policy.md` |
| `g2` prototype → pilot | Prototype run on real data, not dummy data [DELOITTE-2025]; HBR's progression tests: data available, good enough and governed; skills in place or sourced; process redesign need and its owner; ethics and security controls defined; business case still holds [HBR-2026] | Build, buy or partner recorded [HBR-2026]; run-cost range; evaluation plan from ai-solution-delivery |
| `g3` pilot → production | Adoption tested, not only accuracy: feasibility, viability and whether users will adopt it [HBR-2026]; results against the baseline and comparison; benefit rows with owner, baseline and counterfactual in `benefits.yaml` | Rigorous system testing and red-team scrutiny [HBR-2026]; production readiness signed in ai-solution-delivery's `readiness.md`; role evolution and capacity choice; decommissioning route |
| `g4` production → scale | Benefits measured against forecast after go-live [IVI-ITCMF-n.d.; AUSGOV-2013]; total cost of ownership tracked and who pays for run cost at scale [HBR-2026; MCK-2026] | Post-launch review from ai-solution-delivery; reuse plan; enablement plan from ai-enablement; control plan per site |
| `retire` | §5 checklist | — |

For high-impact or regulated items, add the minimum practices the firm's policy sets. NIST asks whether the
system achieves its intended purposes and whether development or deployment should proceed (MANAGE 1.1); OMB
requires minimum risk practices for high-impact AI and termination of non-compliant use [NIST-2023; OMB-2025].

**Light path** (set in step 1): `g1` and `g2` are combined into one gate, the portfolio owner decides `g0`, and
`g3` keeps adoption evidence and benefit rows. HBR's utility example values disciplined progression because of
regulation, and the article says a lighter version suits industries with lower regulatory burden [HBR-2026];
using a light path for low-risk items inside one firm is this skill's default.

**Agentic items** take the same gates with cost and risk evidence at `g2` and `g3`. Gartner forecasts that over
40% of agentic AI projects will be cancelled by the end of 2027 for escalating costs, unclear value or inadequate
risk controls (a forecast, read through a news report) [GARTNER-2025].

### 3.3 Handoffs at gates

| When | Hand off to | What moves |
|---|---|---|
| An item in `discover` or later needs a problem frame or a build or buy leaning (a brief may open in `discover` as `g1` evidence); at the latest, a Go at `g1` | **ai-solution-delivery** | It opens `solutions/<id>/` and hands back. A `g0` Go does not set `solution`; set it only when `solutions/<id>/brief.md` exists and delivery has handed back, with no gate needed |
| `g3` and `g4` evidence | ai-solution-delivery's `readiness.md` and `post-launch.md` | Read them as gate evidence; do not re-assess |
| Risk tier unclear, new tool or vendor, client-data question | **ai-governance** | Tier, policy and tool decision come back through `overlay/` |
| Adoption, training, champions; seat roll-outs | **ai-enablement** | Enablement plan for `g4`; workflows into `enablement/workflows/` |
| A practice needs its opportunities found and planned | **transformation-advisor** | New items come back through intake |

**When the item asked for can't go to delivery** (it needs no AI, is still at intake, or is on Hold), say why.
Then list the AI items (`ai_use` null) by `weighted_score`, each with what blocks it: the gate it waits at and who
decides that gate, a Hold, `status: outline` or `label: draft-to-validate`, or being an enabler other items need.
Offer the one with the shortest path to `discover`; it may not be the top scorer. Check the scores before you call
any item the highest-priority AI item.

## 4. Outcomes and decision rules

| Outcome | Use when | Record |
|---|---|---|
| **Go** | Exit evidence met; resources available (within the live limit at `g1`, `g2` and `g4`) | Resources and who releases them; conditions; next gate and its evidence; new kill criteria |
| **Kill** | A kill criterion is met; evidence that should drive a stop (§5.1) | Reason, evidence, what is reused; move to `retire` if anything was built |
| **Hold** | Worth doing, not now: no capacity, a foundation not ready | Reason; `revisit_when` trigger |
| **Recycle** | Change scope, approach or risk treatment and return to a gate | `recycle_to`, the gate it returns to |

- **A Go without resources is incomplete** ("approval without resources") [COOPER-STAGEGATE-n.d.].
- **No Go past the live limit.** The limit counts items in prototype, pilot or scale (`../schemas/portfolio.md`),
  so it binds a Go at `g1`, `g2` or `g4`. Hold the item, or stop another. At `g0`, note the item's place in the
  queue only; the live limit is not `g0` evidence.
- **Recycle to buy.** A technology change can make a build unnecessary; Lloyds is described as accepting that rapid
  change can justify abandoning projects and switching to new use cases [HBR-2026].
- **Early P&L absence alone is not a kill** before the planned review point (proposed default). Measured value can
  lag the investment in general-purpose technologies (a model and historical analysis, not a measurement of AI
  portfolios) [NBER-2020], and Deloitte's respondents mostly report two to four years to satisfactory ROI
  [DELOITTE-2025]. Use leading indicators instead.
- **Stop on** repeated missed gate criteria or the loss of the owner or benefit owner (proposed default).

## 5. Stopping and retiring

### 5.1 Evidence that should drive a stop

Poor data quality; inadequate risk controls; escalating costs; unclear business value (Gartner's stated causes in
its abandonment and cancellation forecasts) [GARTNER-2024; GARTNER-2025]; performance below an
appropriate level for high-impact AI [OMB-2025]; unacceptable risks or harms found, which UK guidance says should
lead to changing or decommissioning the system [UKGOV-2025].

### 5.2 Retire checklist

- Reason and evidence in the gate log.
- Users, dependent processes and clients affected are told; a fallback keeps critical services running
  [UKGOV-2025; NIST-2023].
- The decommissioning procedure is followed and the inventory updated [NIST-2023; OMB-2025].
- Records of AI use kept as the firm's policy requires (`overlay/policy.md`).
- Lessons captured [AUSGOV-2013] and reusable assets kept: data clean-up, evaluation sets, prompts, integrations.
- Benefits expected but not achieved recorded in `benefits.yaml` (`not-realised` or `withdrawn`) [IVI-ITCMF-n.d.].
- `status: retired` once the checklist is complete.

## 6. Question bank

**Core**
- What evidence will you bring to the next gate, agreed now? Who are the gatekeepers and what do they control?
  [COOPER-STAGEGATE-n.d.]
- Does the business case still hold on real data and real run costs? [HBR-2026; DELOITTE-2025]
- Does the process this supports need redesign, and who owns that change? [HBR-2026]
- Who releases the people and budget for the next stage, and does the Go say so? [COOPER-STAGEGATE-n.d.]
- What would make you stop this, and was it written down at the last gate?

**Follow-ups**
- How will the pilot test adoption, not only accuracy? [HBR-2026]
- Has anyone tried to break it before we scale? [HBR-2026]
- Is the pilot stuck because of the model, the data, the workflow or the people? [MITNANDA-2025; RAND-2024]
- Has a technology change made this build unnecessary, so a bought or newer option is the better route? [HBR-2026]
- What do we learn and reuse from the stopped item? [AUSGOV-2013]

## 7. Expert moves and common traps

| Move | When | What it reveals |
|---|---|---|
| **Write the next-stage resources and the next gate into every Go** | Every gate | Approval without resources [COOPER-STAGEGATE-n.d.] |
| **Run HBR's progression tests at `g2`** | Prototype to pilot | Items technically fine but organizationally unready [HBR-2026] |
| **Insist the prototype uses real data** | `g1`, `g2` | Optimism that collapses on real data; Deloitte's interviewees describe this [DELOITTE-2025] |
| **Test feasibility, viability and desirability in the pilot** | Pilot design | Pilots that validate the model, not the integration or the adoption [HBR-2026] |
| **Require red-team scrutiny before production** | `g3` | Misuse and failure modes before cost rises; HBR notes production usually brings a considerable increase in cost and development time [HBR-2026] |
| **Ask who pays for run cost at scale** | `g4` | Cost surprises; about one in five respondents to McKinsey's 2026 global survey (1,719 participants) said AI operating costs constrained their organization's AI use (respondent-reported) [MCK-2026] |

| Trap | How to avoid it |
|---|---|
| **Gates as status theatre:** meetings with no real decision (a secondary framework summary names this) [UMBREX-n.d.] | Written outcome, resources and next gate every time |
| **Dummy-data proofs of concept** [DELOITTE-2025] | Real-data evidence at `g2` |
| **Moonshot first.** HBR reports MD Anderson's Watson project was put on hold in 2017 after costs topped USD 62 million [HBR-2018] | Balanced horizons; foundations before big bets |
| **Hype-driven agentic items** [GARTNER-2025] | Same gates; cost and risk evidence |
| **Killing on early P&L** [NBER-2020] | Leading indicators until the planned review point |

## 8. Worked example: the K-1 item and a recycle to buy

*Illustrative*, continuing the firm. **K-1 extraction at `g2`.** The prototype ran on 40 of last season's
returns. Evidence: data available and governed (yes); skills sourced (the tax data team plus the delivery team);
process redesign (reviewers check flagged fields instead of keying: owner, the tax operations manager); controls
(the firm's second risk tier: reviewer checks every flagged field); business case on real run costs (holds within the
range). Outcome: Go to pilot; resources: two preparers part-time, released by the tax practice leader; next gate
`g3` needs pilot results against the comparison offices and the readiness checklist. Kill criterion: extraction
errors found at review above the agreed threshold.

**Proposal drafting at `g2`.** The prototype works, but the firm's approved proposal platform has added the same
capability. Outcome: Recycle to buy; `recycle_to`: "configure the approved platform's drafting feature; return at
`g2` with the same evidence." The prompts and content clean-up from the prototype are kept.

## 9. Rollout playbook for acquired firms

Use this when the firm has acquired, or is about to acquire, a firm and wants to move its proven capabilities there.
The detail (readiness checks, consent, independence, partners, benefits rows, how to describe the platform's AI) is in
`acquired-firms.md`; read it before the first gate for an acquired firm.

1. **Assess first.** The transformation-advisor's acquisition path assesses the firm and records it as a unit
   (`../../../transformation-advisor/references/method/acquisitions.md`). Read its stage per dimension and red flags.
2. **One item per capability per firm,** logged through intake with `unit` set to the acquired firm, because each
   firm moves through the gates at its own pace.
3. **Enter at the stage the evidence in that firm supports,** not the stage reached at home. A capability in
   production at home usually enters at `pilot` (proposed default).
4. **Order by dependency,** each layer only after the ones it depends on pass their checks (this skill's ordering;
   RSM treats AI policy as a first-wave priority after close and says data must be centralized and governed before AI
   delivers meaningful results) [RSM-AIDD-2025]:

| Layer | What moves | Before it moves |
|---|---|---|
| 0 Clearances | Client notice and file-transfer consent; tax-return consent; independence screen and monitoring | Deal structure known |
| 1 Governance overlay | Policy, risk tiers, review rules and records of AI use extended to the firm | Clearances recorded |
| 2 Approved tools and training | Catalog entries for the firm; an approved alternative for each unsanctioned tool | Policy adopted in the firm |
| 3 Data foundations | Common systems of record; data centralized and governed | Data owners named; migration and training time budgeted |
| 4 Library workflows | Entries from `enablement/workflows/`, then automation of one or two high-volume flows | Layers 2 and 3; the firm's own baseline; named reviewers |
| 5 Rebuilt workflows and agents | Workflow-native redesigns; delegated agents behind the five onboarding gates | Layer 4 in production in this firm |

5. **Stabilize before transforming.** Writing about large deals, Bain says winners focus integration on a short list
   of value drivers and set an order of operations: where to stabilize and integrate, where to transform
   [BAIN-OUTLOOK-2026]. Hold AI to the transform list.
6. **No shared tool or data flow into an attest entity without an independence assessment,** and no client data
   moves before its consents are recorded (advisor rules; `acquired-firms.md` §5, §6).
7. **Evidence, not mandates, for partners who keep their clients and brand** [GT-AIIMPACT-2026]; describe each
   capability with its evidence status (`acquired-firms.md` §7, §9).
8. **Track on the acquired firm's own baseline:** adoption as `interim` rows (never value), value rows with a
   staggered-start comparison, the deal's AI business case as `enterprise` rows (`acquired-firms.md` §8).

## 10. Output

In `portfolio.yaml` for the item: a new `decisions` entry; `stage`, `status`, `next_gate`, `kill_criteria`,
`solution`, `benefit_owner`, `benefits` as they change. A held item gets `revisit_when`. Update `state` and
`updated`. If the gate was held in a review, record it there too (`portfolio-review.md`). Pre-gate evidence
status goes in the intake record's "Next gate evidence" table (`../templates/intake.md`), not in a separate file.

## 11. Sources

- `AUSGOV-2013` — Australian Government, Department of Finance, *Gateway Reviews lessons learned: Gate 5*, government guidance, 2013-10. https://www.finance.gov.au/sites/default/files/2019-11/Gate_5_-_Lessons_Learned.pdf
- `BAIN-OUTLOOK-2026` — Bain & Company, *Looking Ahead (Global M&A Report 2026)*, consultancy publication, 2026-01-27. https://www.bain.com/insights/looking-ahead-m-and-a-report-2026/
- `COOPER-STAGEGATE-n.d.` — Robert G. Cooper, Stage-Gate International, *The Stage-Gate model: an overview*, method article, undated. https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- `DELOITTE-2025` — Deloitte, *AI ROI: the paradox of rising investment and elusive returns*, consultancy survey, 2025-10-22. https://www.deloitte.com/global/en/issues/generative-ai/ai-roi-the-paradox-of-rising-investment-and-elusive-returns.html
- `GARTNER-2024` — Gartner, *Gartner predicts 30% of generative AI projects will be abandoned after proof of concept by end of 2025*, press release, 2024-07-29. https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025
- `GARTNER-2025` — Outlook Business, *Over 40% of agentic AI projects will be scrapped by 2027, says Gartner*, news report, 2025-06-25. https://www.outlookbusiness.com/artificial-intelligence/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-says-gartner
- `GT-AIIMPACT-2026` — Grant Thornton, *Private Equity insights: 2026 AI Impact Survey Report*, consultancy survey, 2026 (fielded 2026-02/03). https://www.grantthornton.com/insights/survey-reports/private-equity/2026/private-equity-insights-2026-ai-impact-survey-report
- `HBR-2018` — Davenport and Ronanki, *Artificial intelligence for the real world*, Harvard Business Review, 2018-01. https://hbr.org/2018/01/artificial-intelligence-for-the-real-world
- `HBR-2026` — Nelson, Davenport, Scade, *Manage your AI investments like a portfolio*, Harvard Business Review, 2026-01 (read via reprint). https://hbr.org/2026/01/manage-your-ai-investments-like-a-portfolio
- `IVI-ITCMF-n.d.` — Innovation Value Institute, *Benefits Harvesting (IT-CMF 18.07)*, maturity-model guidance, undated. https://portal.ivi.ie/+itcmf/18.07/value/BAR/C/C3
- `MCK-2026` — McKinsey & Company, *The state of AI in 2026*, consultancy survey, 2026-08. https://www.mckinsey.com.br/en/our-insights/the-state-of-ai
- `MITNANDA-2025` — MIT Project NANDA, *The GenAI divide: state of AI in business 2025*, research report (preliminary), 2025-07. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `NBER-2020` — Brynjolfsson, Rock, Syverson, *The productivity J-curve*, NBER Working Paper 25148, rev. 2020-01. https://www.nber.org/system/files/working_papers/w25148/w25148.pdf
- `NIST-2023` — NIST, *AI Risk Management Framework (AI RMF 1.0)*, framework, 2023-01. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `OMB-2025` — US Office of Management and Budget, *M-25-21*, government memorandum, 2025-04-03. https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf
- `RAND-2024` — RAND Corporation, *The root causes of failure for artificial intelligence projects*, research report, 2024-08-13. https://www.rand.org/pubs/research_reports/RRA2680-1.html
- `RSM-AIDD-2025` — RSM US, *Artificial intelligence: ready or not?*, consultancy guidance, 2025. https://rsmus.com/insights/industries/private-equity/ai-due-diligence-assessment-private-equity.html
- `UKGOV-2025` — UK Government Digital Service, *Artificial Intelligence Playbook for the UK Government*, government guidance, 2025. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
- `UMBREX-n.d.` — Umbrex, *Stage-gate project governance model*, secondary framework summary, undated. https://umbrex.com/resources/frameworks/organization-frameworks/stage-gate-project-governance-model/

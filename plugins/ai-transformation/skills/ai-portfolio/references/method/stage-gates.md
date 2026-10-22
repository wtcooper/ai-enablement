# Stage gates (step 4)

Read this on entering step 4: when an item is due at a gate, or when someone asks whether to stop, hold or scale an
item outside a review. It defines the six stages, the evidence for each gate, the four outcomes, how to stop and
retire safely, and when to hand an item on. Keys in brackets are listed in §10.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run a gate](#2-how-to-run-a-gate)
3. [Stages and gate evidence](#3-stages-and-gate-evidence)
4. [Outcomes and decision rules](#4-outcomes-and-decision-rules)
5. [Stopping and retiring](#5-stopping-and-retiring)
6. [Questions and traps](#6-questions-and-traps)
7. [Worked example](#7-worked-example)
8. [Output](#8-output)
9. [Rollout playbook for acquired firms](#9-rollout-playbook-for-acquired-firms)
10. [Sources](#10-sources)

## 1. Goal and exit criteria

**Goal.** Each gate is a forward-looking decision about resources for the next stage, not a status review. Cooper:
gates are where resource commitments are made, with deliverables defined in advance, criteria of readiness and
value, and four outputs: Go, Kill, Hold or Recycle [COOPER-STAGEGATE-n.d.].

**Exit criteria** for each gate held:

- The evidence agreed at the previous gate presented, or its absence recorded, before gatekeepers who control the
  next stage's resources.
- One outcome with its reason and evidence; a Go names the resources, who releases them, the conditions, the next
  gate, its evidence and new kill criteria.
- Handoffs made (§3.3): to ai-solution-delivery by the time the item enters prototype; benefits rows before `g3`.

## 2. How to run a gate

1. **Name the step** ("the gate from pilot to production: do we fund the next stage?") and **read the item**:
   `next_gate.evidence`, `kill_criteria`, `early_warnings`, earlier decisions, and the files in `solutions/<id>/`
   the gate needs when `solution` is set.
2. **Check the evidence** against this gate's exit evidence (§3), one line at a time: met, not met or not
   presented. Missing evidence is a finding, not a reason to guess. Before you flag a conflict between intake
   records, or between a record and the plan, read the plan section their "From the plan" lines name: the plan may
   already reconcile the figures (for example a total and the part of it one task takes).
3. **Check the kill criteria** agreed at the last gate. If one is met, say so first.
4. **Confirm the gatekeepers.** Ask who releases the people, budget or data for the next stage, and whether they
   are part of the decision.
5. **Lay out the options** (Go, Kill, Hold, Recycle) with what each costs and releases. The gatekeepers decide;
   you record. Never present your view as the decision.
6. **Record** the decision in `decisions` (append, never edit), update `stage`, `status`, `next_gate`,
   `kill_criteria`, and play it back. Before adding a field to the item, search that item for the key; if it is
   there, edit it in place. Never insert a second one.
7. **Track the next gate's evidence** in the intake record's "Next gate evidence" table: one row per item of
   `next_gate.evidence`, with its status, owner and what it needs first; update it as evidence arrives. Give
   drafted messages (an ask to a sponsor, a note to a manager) in the chat, or list them under the review pack's
   Actions. Do not create other files.
8. **Hand off** (§3.3) and update state.

## 3. Stages and gate evidence

### 3.1 Stages

The stages adapt Cooper's sequence and HBR's four AI portfolio stages [COOPER-STAGEGATE-n.d.; HBR-2026]; the six
names are this skill's.

| Stage | Purpose | Typical work |
|---|---|---|
| `discover` | Frame the problem, find the baseline, look at the data | Problem and metric agreed with the benefit owner; baseline from records; data seen in its real state |
| `prototype` | Test technical feasibility on real data | Prototype on real cases; build, buy or partner decided; solution brief and evaluation plan |
| `pilot` | Test value and adoption on live work | Real users on live work with a comparison; adoption, quality and run cost measured |
| `production` | Supported service for its first population | Production readiness signed off; benefits measured against the forecast |
| `scale` | Extend to more practices, offices or client groups | Reuse of components; enablement; control plan per site |
| `retire` | Decommission safely | Fallback, notification, records, lessons, reusable assets |

### 3.2 Gate evidence

| Gate | Exit evidence (all paths) | Added on the full path |
|---|---|---|
| `g0` screen | Intake complete; pre-score gates passed; two indexes; sponsor (`screen-and-score.md`) | — |
| `g1` discover → prototype | Problem and success metric agreed with the benefit owner [RAND-2024]; baseline from records; data located and seen in its real state; strategic fit and technical feasibility [HBR-2026] | Counterfactual idea; build, buy or partner leaning; risk tier confirmed against `overlay/policy.md` |
| `g2` prototype → pilot | Prototype run on real data, not dummy data [DELOITTE-2025]; data available, good enough and governed; skills in place or sourced; process redesign need and its owner; controls defined; business case still holds [HBR-2026] | Build, buy or partner recorded; run-cost range; evaluation plan from ai-solution-delivery |
| `g3` pilot → production | Adoption tested, not only accuracy [HBR-2026]; results against the baseline and comparison; benefit rows with owner, baseline and counterfactual in `benefits.yaml` | Red-team scrutiny [HBR-2026]; readiness signed in ai-solution-delivery's `readiness.md`; role evolution and capacity choice; decommissioning route |
| `g4` production → scale | Benefits measured against forecast after go-live [IVI-ITCMF-n.d.; AUSGOV-2013]; total cost of ownership and who pays for run cost at scale [HBR-2026] | Post-launch review from ai-solution-delivery; reuse plan; enablement plan from ai-enablement; control plan per site |
| `retire` | §5 checklist | — |

High-impact or regulated items add the minimum practices the firm's policy sets [OMB-2025]. Agentic items take the
same gates, with cost and risk evidence at `g2` and `g3`: Gartner forecasts that over 40% of agentic AI projects
will be cancelled by the end of 2027 (a forecast, read through a news report) [GARTNER-2025].

**Light path (default; the user can change it in step 1).** For the firm's lowest risk tier and
individual-productivity items: `g1` and `g2` combine into one gate, the portfolio owner decides `g0`, and `g3` keeps
adoption evidence and benefit rows. HBR says a lighter gated process suits lower regulatory burden, and OMB asks for
streamlined approvals of closely related, similar-risk uses [HBR-2026; OMB-2025]; applying that to low-risk items
inside one firm is this skill's default.

### 3.3 Handoffs at gates

| When | Hand off to | What moves |
|---|---|---|
| An item in `discover` or later needs a problem frame or a build or buy leaning (a brief may open in `discover` as `g1` evidence); at the latest, a Go at `g1` | **ai-solution-delivery** | It opens `solutions/<id>/` and hands back. A `g0` Go does not set `solution`; set it only when `solutions/<id>/brief.md` exists and delivery has handed back, with no gate needed |
| `g3` and `g4` evidence | ai-solution-delivery's `readiness.md` and `post-launch.md` | Read them as gate evidence; do not re-assess |
| Risk tier, tool, vendor or client-data question; adoption and training; a practice to plan | **ai-governance**, **ai-enablement**, **transformation-advisor** (`SKILL.md`, Handoffs) | Decisions come back through `overlay/`; an enablement plan for `g4`; new items through intake |

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

- **No Go past the live limit.** The limit counts items in prototype, pilot or scale, so it binds a Go at `g1`,
  `g2` or `g4`. Hold the item, or stop another. At `g0`, note the item's place in the queue only; the live limit
  is not `g0` evidence.
- **Recycle to buy.** A technology change can make a build unnecessary; Lloyds is described as accepting that rapid
  change can justify abandoning projects and switching to new use cases [HBR-2026].
- **Early P&L absence alone is not a kill** before the planned review point (this skill's default). Measured value
  can lag the investment in general-purpose technologies (a model and historical analysis) [NBER-2020], and most of
  Deloitte's 1,854 surveyed executives report two to four years to satisfactory ROI on a typical AI use case,
  against the seven to 12 months expected of technology investment (respondent-reported) [DELOITTE-2025]. Use
  leading indicators instead.
- **Stop on** repeated missed gate criteria or the loss of the owner or benefit owner (this skill's default).

## 5. Stopping and retiring

### 5.1 Evidence that should drive a stop

Poor data quality, inadequate risk controls, escalating costs, unclear business value (Gartner's stated causes in
its abandonment and cancellation forecasts) [GARTNER-2024; GARTNER-2025]; performance below an appropriate level
for high-impact AI [OMB-2025]; unacceptable risks or harms found, which UK guidance says should lead to changing or
decommissioning the system [UKGOV-2025].

### 5.2 Retire checklist

Reason and evidence in the gate log; users, dependent processes and affected clients told, with a fallback for
critical services [UKGOV-2025; NIST-2023]; the decommissioning procedure followed and the inventory updated
[NIST-2023; OMB-2025]; records of AI use kept as `overlay/policy.md` requires; lessons captured [AUSGOV-2013] and
reusable assets kept (data clean-up, evaluation sets, prompts, integrations); unachieved benefits marked
`not-realised` or `withdrawn` in `benefits.yaml`. Then `status: retired`.

## 6. Questions and traps

Ask whether the case still holds on real data and real run costs, who pays for run cost at scale, and how the
pilot tests adoption, not only accuracy [HBR-2026]. Avoid gates as status theatre (meetings with no written
outcome, resources and next gate) and dummy-data proofs of concept [DELOITTE-2025].

## 7. Worked example

*Illustrative.* **K-1 extraction at `g2`.** The prototype ran on 40 of last season's returns; data, skills,
process redesign (reviewers check flagged fields instead of keying), controls and the case on real run costs all
hold. Go to pilot: two preparers part-time, released by the tax practice leader; `g3` needs pilot results against
the comparison offices and the readiness checklist; kill criterion: extraction errors above the agreed threshold.

## 8. Output

In `portfolio.yaml` for the item: a new `decisions` entry; `stage`, `status`, `next_gate`, `kill_criteria`,
`solution`, `benefit_owner`, `benefits` as they change; `revisit_when` on a Hold. Update `state` and `updated`. If
the gate was held in a review, record it there too. Pre-gate evidence status goes in the intake record's "Next gate
evidence" table (`../templates/intake.md`), not in a separate file.

## 9. Rollout playbook for acquired firms

For moving proven capabilities into an acquired firm. Read `acquired-firms.md` before its first gate.

1. **Assess first** with the transformation-advisor's acquisition path
   (`../../../transformation-advisor/references/method/acquisitions.md`).
2. **One item per capability per firm,** with `unit` set to the acquired firm, entering at the stage the evidence
   in that firm supports, not the stage reached at home (usually `pilot`; the same rule places a tool in use).
3. **Order by dependency:** clearances, governance overlay, approved tools and training, data foundations, library
   workflows, then rebuilt workflows and agents (`acquired-firms.md` §3).
4. **No shared tool or data flow into an attest entity without an independence assessment,** and no client data
   moves before its consents are recorded (`acquired-firms.md` §4).
5. **Track on the acquired firm's own baseline** (`acquired-firms.md` §6).

## 10. Sources

- `AUSGOV-2013` — Australian Government, Department of Finance, *Gateway Reviews lessons learned: Gate 5*, government guidance, 2013-10. https://www.finance.gov.au/sites/default/files/2019-11/Gate_5_-_Lessons_Learned.pdf
- `COOPER-STAGEGATE-n.d.` — Robert G. Cooper, Stage-Gate International, *The Stage-Gate model: an overview*, method article, undated. https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- `DELOITTE-2025` — Deloitte, *AI ROI: the paradox of rising investment and elusive returns*, consultancy survey of 1,854 executives in 14 EMEA countries, 2025-10-22. https://www.deloitte.com/global/en/issues/generative-ai/ai-roi-the-paradox-of-rising-investment-and-elusive-returns.html
- `GARTNER-2024` — Gartner, *Gartner predicts 30% of generative AI projects will be abandoned after proof of concept by end of 2025*, press release, 2024-07-29. https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025
- `GARTNER-2025` — Outlook Business, *Over 40% of agentic AI projects will be scrapped by 2027, says Gartner*, news report, 2025-06-25. https://www.outlookbusiness.com/artificial-intelligence/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-says-gartner
- `HBR-2026` — Nelson, Davenport, Scade, *Manage your AI investments like a portfolio*, Harvard Business Review, 2026-01 (read via reprint). https://hbr.org/2026/01/manage-your-ai-investments-like-a-portfolio
- `IVI-ITCMF-n.d.` — Innovation Value Institute, *Benefits Harvesting (IT-CMF 18.07)*, maturity-model guidance, undated. https://portal.ivi.ie/+itcmf/18.07/value/BAR/C/C3
- `NBER-2020` — Brynjolfsson, Rock, Syverson, *The productivity J-curve*, NBER Working Paper 25148, rev. 2020-01. https://www.nber.org/system/files/working_papers/w25148/w25148.pdf
- `NIST-2023` — NIST, *AI Risk Management Framework (AI RMF 1.0)*, framework, 2023-01. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `OMB-2025` — US Office of Management and Budget, *M-25-21*, government memorandum, 2025-04-03. https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf
- `RAND-2024` — RAND Corporation, *The root causes of failure for artificial intelligence projects*, research report, 2024-08-13. https://www.rand.org/pubs/research_reports/RRA2680-1.html
- `UKGOV-2025` — UK Government Digital Service, *Artificial Intelligence Playbook for the UK Government*, government guidance, 2025. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html

# Library index (ai-portfolio)

This skill uses the shared library of the suite and adds a small set of portfolio-only values. Read the shared
library section you need; use the ids in §2 in `portfolio.yaml` and `benefits.yaml`.

## Contents

1. [What to use from the shared library](#1-what-to-use-from-the-shared-library)
2. [Portfolio values](#2-portfolio-values)
3. [Benefits values](#3-benefits-values)
4. [Tools and runtime classes](#4-tools-and-runtime-classes)

## 1. What to use from the shared library

The shared library is `../../../transformation-advisor/references/library/index.md`. Controlled ids live in
`../../../transformation-advisor/references/schemas/vocabulary.yaml`.

| Need | Shared section | Used in |
|---|---|---|
| Ladder and change scope of an item | §1 | Intake, screen |
| Work types and agentic patterns | §2, §3 | Intake (to place the item), screen (feasibility) |
| Runtime classes (how to describe tools without vendors) | §4 | Every step; see §4 below |
| Value levers and their metrics | §5 | Set up, screen, value tracking |
| Six scoring dimensions, default weights, categories | §6 | Set up, screen; anchors in `../../../transformation-advisor/references/method/prioritize.md` §3 |
| Journey stages | §7 | Set up (where the firm stands shapes the gate weight) |
| Functions | §8 | Intake (`function` for ideas from firm services) |

## 2. Portfolio values

These values are specific to this skill. They are proposed for the shared vocabulary; until then they are
defined here.

**`stage`**: where an item is in the pipeline. Stage definitions and gate tests are in
`../method/stage-gates.md` §3.

| Id | Meaning |
|---|---|
| `intake` | Logged, not yet screened |
| `discover` | Passed the screen; the problem, baseline and data are being examined |
| `prototype` | Technical feasibility tested on real data |
| `pilot` | Live work with real users and a comparison; value and adoption tested |
| `production` | Supported service for its first population; benefits measured |
| `scale` | Extended to more practices, offices or client groups |
| `retire` | Being decommissioned |

**`status`**: `outline` (intake incomplete: problem, owner or data source missing), `active`, `hold`,
`killed`, `retired` (decommissioning complete).

**Gates** (`decisions[].gate`): `g0` screen (intake to discover), `g1` discover to prototype, `g2` prototype to
pilot, `g3` pilot to production, `g4` production to scale, `retire` (decision to retire, and its closure).

**`outcome`**: Cooper's four gate outputs [COOPER-STAGEGATE-n.d.].

| Id | Meaning | Must record |
|---|---|---|
| `go` | Proceed to the next stage | Resources released and who releases them; next gate and its evidence |
| `kill` | Stop; move to `retire` if anything was built, else close as `killed` | Reason and evidence; what is reused |
| `hold` | Worth doing, not now (capacity, dependency, timing of a foundation) | Reason; `revisit_when` trigger |
| `recycle` | Rework and come back: new scope, approach (for example buy instead of build) or risk treatment | `recycle_to`; which gate it returns to |

A redirect is a `recycle` with `recycle_to` filled in.

**`item_class`**: the proof standard the item is judged by. Microsoft's guidance separates individual-work
improvement from business process change [MSFT-PLAN-2026]; the shared prioritize method adds new value.

| Id | Meaning | Proof standard |
|---|---|---|
| `individual-productivity` | People work differently in existing tools | Adoption and quality of use; time effects are mostly self-reported. Seat roll-outs go on the enablement line, not counted as portfolio wins |
| `business-automation` | The flow of work changes | Operating data against a baseline and a counterfactual |
| `new-value` | New service, product or price | Revenue mechanics: price, volume, clients won |

**`horizon`**: `near`, `medium`, `long`; the review checks the mix [HBR-2026].

**`category`**: `quick-win`, `foundation`, `big-bet`, `park`, with the rules in
`../../../transformation-advisor/references/method/prioritize.md` §3.4.

**`gate_path`**: `light` or `full`. HBR says a lighter gated process suits lower regulatory burden, and OMB asks for
streamlined approvals for closely related, similar-risk uses [HBR-2026; OMB-2025]; which items qualify is set in
step 1.

**`risk_tier`**: the tier id from `risk_tiers` in `overlay/policy.md`, written by ai-governance (its defaults are
`tier-1` to `tier-4`, set by the consequence of an error and who relies on the output). Without a policy, place the
item against ai-governance's default tiers, mark the tier provisional in the intake record, and offer ai-governance.

**Early-warning `type`**: `slippage`, `cost-overrun`, `performance-shortfall` [HBR-2026].

## 3. Benefits values

| Field | Values | Meaning |
|---|---|---|
| `type` | `direct`, `indirect`, `interim`, `disbenefit` | Benefit types used in benefits-realisation reviews [AUSGOV-2013] |
| `level` | `use-case`, `enterprise` | The item's own metric versus a firm P&L line [MCK-2026] |
| `counterfactual` | `control-group`, `staggered-start`, `parallel-run`, `baseline-comparison`, `assumption` | How the effect is separated from everything else |
| `basis` | `from-record`, `reported`, `observed`, `outside-in` | Where a number came from (the advisor's Map labels) |
| `status` | `forecast`, `tracking`, `realised`, `partly-realised`, `not-realised`, `withdrawn` | Rules in `../schemas/benefits.md` §2 |
| `capacity.decision` | `redeploy`, `reduce`, `mixed`, `undecided` | The capacity choice (rule 2) |

## 4. Tools and runtime classes

Describe tools by runtime class (`personal-assistant`, `shared-team-skills`, `workflow-automation`,
`background-agent`, `managed-agent-runtime`), as defined in §4 of the shared library. If
`overlay/tool-catalog.yaml` exists, use its approved products and flag any item that needs something outside
it; the evaluation of a new tool belongs to ai-governance. Never recommend a vendor.

## Sources

- `AUSGOV-2013` — Australian Government, Department of Finance, *Gateway Reviews lessons learned: Gate 5*,
  government guidance, 2013-10. https://www.finance.gov.au/sites/default/files/2019-11/Gate_5_-_Lessons_Learned.pdf
- `COOPER-STAGEGATE-n.d.` — Robert G. Cooper, Stage-Gate International, *The Stage-Gate model: an overview*,
  method article, undated. https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- `HBR-2026` — Nelson, Davenport, Scade, *Manage your AI investments like a portfolio*, Harvard Business
  Review, 2026-01 (read via reprint). https://hbr.org/2026/01/manage-your-ai-investments-like-a-portfolio
- `MCK-2026` — McKinsey & Company, *The state of AI in 2026*, consultancy survey, 2026-08.
  https://www.mckinsey.com.br/en/our-insights/the-state-of-ai
- `MSFT-PLAN-2026` — Microsoft Learn, *Plan for AI adoption*, vendor guidance, updated 2026-10-15.
  https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/plan
- `OMB-2025` — US Office of Management and Budget, *M-25-21*, government memorandum, 2025-04-03.
  https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf

# Library index (ai-portfolio)

This skill uses the shared library of the suite and adds a few portfolio-only values. Use the ids in §2 and §3 in
`portfolio.yaml` and `benefits.yaml`.

## Contents

1. [What to use from the shared library](#1-what-to-use-from-the-shared-library)
2. [Portfolio values](#2-portfolio-values)
3. [Benefits values](#3-benefits-values)
4. [Tools and runtime classes](#4-tools-and-runtime-classes)

## 1. What to use from the shared library

The shared library is `../../../transformation-advisor/references/library/index.md`; controlled ids live in
`../../../transformation-advisor/references/schemas/vocabulary.yaml`.

| Need | Shared section | Used in |
|---|---|---|
| Ladder and change scope; work types and agentic patterns | §1, §2, §3 | Intake, screen |
| Runtime classes (how to describe tools without vendors) | §4 | Every step; see §4 below |
| Value levers and their metrics | §5 | Set up, screen, value tracking |
| Six scoring dimensions, default weights, categories | §6 | Set up, screen; anchors in `../../../transformation-advisor/references/method/prioritize.md` §3 |
| Journey stages; functions | §7, §8 | Set up; intake (`function`) |

## 2. Portfolio values

Specific to this skill; proposed for the shared vocabulary, defined here until then.

- **`stage`:** `intake` (logged, not yet screened; a tool already in use enters at the stage its use supports,
  `../schemas/portfolio.md` §2), `discover`, `prototype`, `pilot`, `production`, `scale`, `retire`. Definitions and
  gate tests: `../method/stage-gates.md` §3.
- **`status`:** `outline` (problem, owner or data source missing), `active`, `hold`, `killed`, `retired`
  (decommissioning complete).
- **Gates** (`decisions[].gate`): `g0` screen (intake to discover), `g1` discover to prototype, `g2` prototype to
  pilot, `g3` pilot to production, `g4` production to scale, `retire`.
- **`outcome`:** `go`, `kill`, `hold`, `recycle`, Cooper's four gate outputs [COOPER-STAGEGATE-n.d.]; what each must
  record is in `../method/stage-gates.md` §4. A redirect is a `recycle` with `recycle_to` filled in.
- **`item_class`:** the proof standard the item is judged by (Microsoft separates individual-work improvement from
  business process change [MSFT-PLAN-2026]). `individual-productivity`: adoption and quality of use, time effects
  mostly self-reported; seat roll-outs go on the enablement line. `business-automation`: operating data against a
  baseline and a counterfactual. `new-value`: revenue mechanics (price, volume, clients won).
- **`horizon`:** `near`, `medium`, `long`. **`category`:** `quick-win`, `foundation`, `big-bet`, `park` (rules in
  prioritize §3.4). **`gate_path`:** `light` or `full` (`../method/stage-gates.md` §3.2).
- **Early-warning `type`:** `slippage`, `cost-overrun`, `performance-shortfall` [HBR-2026].
- **`ai_use`:** `none` when the rules-or-AI check finds that rules, a template or an existing tool is enough; then
  `ladder`, `runtime_class` and `risk_tier` are null and the review counts the item apart. `null` (the default)
  means AI is in scope.

**`risk_tier`**: the tier id from `risk_tiers` in `overlay/policy.md`, written by ai-governance (its defaults are
`tier-1` to `tier-4`, set by the consequence of an error and who relies on the output). Without a policy, place the
item against ai-governance's default tiers, mark the tier provisional in the intake record, and offer ai-governance.
While `overlay/policy.md` is not `approved` (for example `status: draft`), copy its proposed tier into `risk_tier`
and mark it "provisional" in the intake record's Early read until the policy is approved. If the draft proposes no
tier for the item, place it against the default tiers as above. ai-solution-delivery follows the same rule in the
brief (`../../../ai-solution-delivery/references/schemas/solution.md` §4).

## 3. Benefits values

| Field | Values |
|---|---|
| `type` | `direct`, `indirect`, `interim`, `disbenefit` (benefits-realisation review types [AUSGOV-2013]) |
| `level` | `use-case` (the item's own metric), `enterprise` (a firm P&L line) |
| `counterfactual` | `control-group`, `staggered-start`, `parallel-run`, `baseline-comparison`, `assumption` (`../method/value-tracking.md` §3.1) |
| `basis` | `from-record`, `reported`, `observed`, `outside-in` (the advisor's Map labels) |
| `status` | `forecast`, `tracking`, `realised`, `partly-realised`, `not-realised`, `withdrawn` (rules in `../schemas/benefits.md` §2) |
| `capacity.decision` | `redeploy`, `reduce`, `mixed`, `undecided` (rule 2) |

## 4. Tools and runtime classes

Describe tools by runtime class (`personal-assistant`, `shared-team-skills`, `workflow-automation`,
`background-agent`, `managed-agent-runtime`), as defined in §4 of the shared library. If
`overlay/tool-catalog.yaml` exists, use its approved products and flag any item that needs something outside it;
the evaluation of a new tool belongs to ai-governance. Never recommend a vendor.

## Sources

- `AUSGOV-2013` — Australian Government, Department of Finance, *Gateway Reviews lessons learned: Gate 5*, government guidance, 2013-10. https://www.finance.gov.au/sites/default/files/2019-11/Gate_5_-_Lessons_Learned.pdf
- `COOPER-STAGEGATE-n.d.` — Robert G. Cooper, Stage-Gate International, *The Stage-Gate model: an overview*, method article, undated. https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- `HBR-2026` — Nelson, Davenport, Scade, *Manage your AI investments like a portfolio*, Harvard Business Review, 2026-01 (read via reprint). https://hbr.org/2026/01/manage-your-ai-investments-like-a-portfolio
- `MSFT-PLAN-2026` — Microsoft Learn, *Plan for AI adoption*, vendor guidance, updated 2026-10-15. https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/plan

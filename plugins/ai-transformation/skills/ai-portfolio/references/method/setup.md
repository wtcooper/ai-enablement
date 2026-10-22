# Set up the portfolio (step 1)

Read this on entering step 1: scope, levers and weights, stages, roles, gate paths and rhythm. Propose the
defaults below; the user changes only what doesn't fit. Keys in brackets are listed in §7.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Defaults and decision rules](#3-defaults-and-decision-rules)
4. [Questions, moves and traps](#4-questions-moves-and-traps)
5. [Worked example](#5-worked-example)
6. [Output](#6-output)
7. [Sources](#7-sources)

## 1. Goal and exit criteria

**Goal.** One register and one decision system for every AI idea, pilot and live system in scope, so items are
judged against each other and against fixed criteria, not only on their own merits [HBR-2026].

**Exit criteria.**

- Scope: which practices, functions and kinds of item (ideas, pilots, live systems) are in.
- Value levers with one named metric each, and weights that sum to 1 (`inherited_from` set if from a plan).
- Six stages with exit evidence (defaults in `stage-gates.md` §3); gatekeepers per gate, as roles that control the
  next stage's resources; light and full paths, and who decides `g0` on each.
- The review forum, rhythm and live limit; a first inventory of AI already in use, or a step to build one.

## 2. How to run it

1. **Look for an advisor plan.** If `transformation-plan.md` exists, play back `settings.value_levers`,
   `settings.scoring_weights` and `settings.capacity_stance`, ask whether they hold for the whole portfolio, copy
   them and set `inherited_from`. With no plan, agree levers and weights using
   `../../../transformation-advisor/references/method/frame.md` §4, or offer the advisor first.
2. **Set the scope.** One register for ideas, pilots and live systems [UKGOV-2025; NIST-2023]. Ask what AI is
   already in use, sanctioned or not, and whether a decommissioning procedure exists [NIST-2023; OMB-2025].
3. **Propose the stages.** Play back the six default stages (`stage-gates.md` §3) and ask only what the firm would
   add, such as the independence or quality review an audit practice already runs.
4. **Name the gatekeepers.** For each gate ask whose people, budget or data the next stage needs; gatekeepers are
   the senior managers who control those resources [COOPER-STAGEGATE-n.d.]. In a partnership, include the practice
   heads whose people's time is being spent (`people-and-change.md`).
5. **Set the gate paths.** Propose the light path default (`stage-gates.md` §3.2), reading `overlay/policy.md`
   for risk tiers if it exists. Then ask who decides the screen (`g0`) on each path and record the roles in
   `gate_paths.g0_deciders`. On the full path, include the sponsor or the gatekeepers who control discovery
   resources, not the portfolio owner alone.
6. **Set the forum, rhythm and live limit.** Propose the defaults in §3.1 and §3.3; the user can change them.
7. **Play back** the set-up in a few lines, write `portfolio.yaml` from `../templates/portfolio.yaml`, and set
   `state.status: running`, `step_completed: 1`, `next_step: 2`, `updated`.

## 3. Defaults and decision rules

### 3.1 The review forum and rhythm

No source gives a standard attendee list or cadence. The decisions a review makes: add promising initiatives,
scale successful pilots, redirect struggling efforts, retire misaligned projects and recalibrate scoring criteria
[HBR-2026]. Microsoft recommends a steering committee of business and IT leaders with monthly progress reviews
with sponsors [MSFT-COE-2026].

**Default** (the user can change it): a **monthly review, with a rebalance at every third review**. Forum in a
professional-services firm: the managing partner or chief operating officer, practice leaders, the risk and
quality partner or general counsel, the heads of IT and finance, the people lead and the head of AI.

### 3.2 The central team's stance

Microsoft's guidance gives intake and prioritization to an AI centre of excellence early, then moves it to an
advisory model once governance is embedded; the signals are approval delays, experts who cannot support all teams
and recurring priority debates [MSFT-COE-2026]. Say so at set-up, and check the signals at each rebalance.

### 3.3 Live limit

No more live items (prototype, pilot, scale) than there are named owners and review capacity to carry them
(`../../../transformation-advisor/references/method/prioritize.md` §3.5). Set it as a number in
`settings.live_limit` and test it at each rebalance.

## 4. Questions, moves and traps

Ask whether an AI board or centre of excellence already exists and what it decides [MSFT-COE-2026]; who attends
any portfolio review today and what it actually decides; and whether the firm is a partnership, a corporate with
partner titles or a hybrid, and who votes on investment.

| Trap | How to avoid it |
|---|---|
| **Pilot sprawl:** "too many pilots with too little coordinated oversight" [HBR-2026] | One register, one intake route, a live limit |
| **Gates without resource holders:** "approval without resources" [COOPER-STAGEGATE-n.d.] | Gatekeepers are the people who control the next stage's resources |
| **No exit path** (NIST GOVERN 1.7; OMB's discontinuation of under-performing high-impact AI) [NIST-2023; OMB-2025] | A retire stage and a decommissioning route from day one |
| **Leaders who won't accept kills** | Say at set-up that stopping is an expected output |

## 5. Worked example

*Illustrative.* An accounting, tax and advisory firm copies its advisor plan's levers (capacity → preparer hours
per return; quality → review notes per return; growth → advisory fees) and weights. The inventory finds fourteen
items, three of them near-identical drafting assistants. Gatekeepers: practice leaders at `g1` and `g2`, the risk
and quality partner at `g2` and `g3`, the finance director at `g3` and `g4`. `g0` deciders: the head of AI alone on
the light path; the sponsor and practice leaders with the head of AI on the full path. Live limit six.

## 6. Output

`portfolio/portfolio.yaml` from `../templates/portfolio.yaml`, with `portfolio`, `settings`, `stages`,
`gate_paths` (including `g0_deciders`), `roles`, `rhythm` and `state` filled (`../schemas/portfolio.md`).
Inventory items found here are logged in step 2, at the stage their current use supports (`intake.md` §2, "A tool
already in use"). Set `state.step_completed: 1`, `next_step: 2`, `updated`.

## 7. Sources

- `COOPER-STAGEGATE-n.d.` — Robert G. Cooper, Stage-Gate International, *The Stage-Gate model: an overview*, method article, undated. https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- `HBR-2026` — Nelson, Davenport, Scade, *Manage your AI investments like a portfolio*, Harvard Business Review, 2026-01 (read via reprint). https://hbr.org/2026/01/manage-your-ai-investments-like-a-portfolio
- `MSFT-COE-2026` — Microsoft Learn, *Establish an AI Center of Excellence*, vendor guidance, updated 2026-04-10. https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/center-of-excellence
- `NIST-2023` — NIST, *AI Risk Management Framework (AI RMF 1.0)*, framework, 2023-01. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `OMB-2025` — US Office of Management and Budget, *M-25-21*, government memorandum, 2025-04-03. https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf
- `UKGOV-2025` — UK Government Digital Service, *Artificial Intelligence Playbook for the UK Government*, government guidance, 2025. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html

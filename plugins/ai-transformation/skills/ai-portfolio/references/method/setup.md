# Set up the portfolio (step 1)

Read this on entering step 1. It tells you how to set up a portfolio that a firm's leaders will trust: its
scope, value levers and weights (inherited from the advisor's plan when one exists), stage definitions, roles,
gate paths and review rhythm. Keys in brackets are listed in §9.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Checklists and decision rules](#3-checklists-and-decision-rules)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example: an accounting and advisory firm](#7-worked-example-an-accounting-and-advisory-firm)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** One register and one decision system for every AI idea, pilot and live system in scope, so that
items are judged against each other and against fixed criteria, not only on their own merits [HBR-2026].

**Exit criteria.**

- Scope stated: which practices, functions and kinds of item (ideas, pilots, live systems) are in.
- Value levers, each with one named metric, and scoring weights that sum to 1, with `inherited_from` set when
  they came from an advisor plan.
- Six stage definitions with entry and exit evidence the user accepts (defaults in `stage-gates.md` §3).
- Gatekeepers per gate, named as roles that control the resources the next stage needs.
- A light and a full gate path, which items qualify for the light one, and who decides `g0` on each path.
- The review forum, the review rhythm and the live limit.
- A first inventory of AI already in use, or a step to build one.

## 2. How to run it

1. **Name the step.** "We are setting up the portfolio: what is in it, how items are judged and who decides.
   Next we log the ideas."
2. **Look for an advisor plan.** If `transformation-plan.md` exists, read `settings.value_levers`,
   `settings.scoring_weights` and `settings.capacity_stance`, play them back and ask whether they still hold
   for the whole portfolio. Copy them and set `inherited_from`. If no plan exists, agree levers and weights
   using `../../../transformation-advisor/references/method/frame.md` §4, or offer the advisor first (see
   `SKILL.md`, Handoffs).
3. **Set the scope.** One register for ideas, pilots and live systems [UKGOV-2025; NIST-2023]. Ask what AI is
   already in use, sanctioned or not, and whether a decommissioning procedure exists [NIST-2023; OMB-2025].
4. **Agree the stages.** Walk the six default stages in `stage-gates.md` §3 one at a time. Tailor exit evidence
   to the firm's own approvals (for example, the independence or quality review an audit practice already runs).
5. **Name the gatekeepers.** For each gate ask whose people, budget or data the next stage needs. Gatekeepers
   are the senior managers who own or control those resources [COOPER-STAGEGATE-n.d.]. In a partnership, include
   the practice heads whose partners' and staff's time is being spent (see `people-and-change.md`).
6. **Set the gate paths.** Read `overlay/policy.md` for risk tiers if it exists. Agree which items take a
   lighter path. HBR's utility example says a lighter version of its gated process suits industries with lower
   regulatory burden, and OMB asks agencies to streamline approvals for closely related uses with substantially
   similar risk [HBR-2026; OMB-2025]; applying that to low-risk items within one firm is this skill's default.
   Then ask who decides the screen (`g0`) on each path, and record the roles in `gate_paths.g0_deciders`. On the
   full path, include the sponsor or the gatekeepers who control discovery resources, not the portfolio owner
   alone.
7. **Set the forum and rhythm.** Agree who sits in the review and what it decides (§3.2). Agree the live limit.
8. **Agree the central team's stance.** Say plainly that the portfolio office starts as an intake and gate body
   and should plan its move to an advisory role (§3.3) [MSFT-COE-2026].
9. **Play back** the set-up in a few lines, write `portfolio.yaml` from `../templates/portfolio.yaml`, and set
   `state.status: running`, `step_completed: 1`, `next_step: 2`, `updated`.

**Adapt by journey stage** (read the stage from the advisor plan, or place it by what the user can count;
`../../../transformation-advisor/references/library/journey-stages.md`). Experimenting: a small portfolio, the
light path for most items, one forum. Adopting: full gates for business-automation items, a benefits register
from the first production item. Scaling: units with their own intake feeding one portfolio, shared components
and a rebalance at every third review.

## 3. Checklists and decision rules

### 3.1 Set-up checklist

- One register; every item has a single id across intake, portfolio, solutions and benefits files.
- Weights sum to 1. Each lever has one named metric the finance lead would accept.
- When agreeing weights, a proposed default: count people-and-process readiness at least as much as technical
  feasibility. BCG attributes about 70% of implementation challenges to people and process, 20% to technology
  and 10% to algorithms (BCG survey of 1,000 CxOs and senior executives in 59 countries) [BCG-2024]; BCG gives the
  split, not a weight.
- Stage exit evidence is written before any item reaches the gate.
- Every gate has at least one gatekeeper who controls resources for the next stage.
- A decommissioning route exists for anything that reaches production [NIST-2023; OMB-2025].

### 3.2 The review forum

No source gives a standard attendee list or cadence. Lloyds Banking Group's forum is described as
cross-functional; it prioritizes use cases, allocates resources and ensures strategic alignment [HBR-2026].
Microsoft recommends a steering committee of business and IT leaders with monthly progress reviews with sponsors
[MSFT-COE-2026]. The decisions a review makes: add promising initiatives, scale successful pilots, redirect
struggling efforts, retire misaligned projects and recalibrate scoring criteria [HBR-2026].

**Proposed default** (no source sets the number): a monthly review and a rebalance at every third review. In a
professional-services firm: the managing partner or chief operating officer, practice leaders, the risk and
quality partner or general counsel, the heads of IT and finance, the people lead and the head of AI.

### 3.3 The central team's stance

Microsoft's guidance assigns intake and prioritization workflows to an AI centre of excellence early, then
moves it to an advisory model once governance is embedded; the signals are approval delays, experts who cannot
support all teams, and recurring priority debates between the centre and product teams [MSFT-COE-2026]. Record
those signals as a standing item in the rebalance review.

### 3.4 Live limit

No more live items (prototype, pilot, scale) than there are named owners and review capacity to carry them
(shared sequencing rule, `../../../transformation-advisor/references/method/prioritize.md` §3.5). Set it as a
number in `settings.live_limit` and test it at each rebalance.

## 4. Question bank

Tags: **[U]** unit or practice, **[O]** organization. Core questions first.

**Core**
- Is there a single register of AI ideas, pilots and live systems, or does each practice keep its own? Who sees
  it? [O] [UKGOV-2025; NIST-2023]
- Does an AI board or centre of excellence exist already? What does it decide, and what does it not? [O]
  [MSFT-COE-2026]
- Who else has to say yes before an item can start, and who can say no without being asked? [U][O]
- Who releases the people and budget for a pilot, and would they sit at the gate? [O] [COOPER-STAGEGATE-n.d.]
- Who attends the portfolio review today, what pack do they see, and what decisions does it actually make? [O]

**Follow-ups**
- What are your scoring criteria today? Who set them, and when were they last recalibrated? [U] [HBR-2026]
- Is the firm a partnership, a corporate with partner titles or a hybrid, and who votes on investment? [O]
- What has been tried before, and what did the partners conclude from it? [U][O]
- Is there a procedure to decommission an AI system safely, and who triggers it? [O] [NIST-2023; OMB-2025]
- Which items are high risk under your own policy, and should they follow a heavier path? [O] [OMB-2025]

## 5. Expert moves

| Move | When | What it reveals |
|---|---|---|
| **Ask gate attendees to name whose resources they control** | Designing gates | Missing gatekeepers; gates that approve work nobody can staff [COOPER-STAGEGATE-n.d.] |
| **Ask for the inventory of AI in use and the decommissioning procedure** | Scope | Shadow AI and no exit path; NIST lists inventory and decommissioning mechanisms, and OMB requires an annual use case inventory [NIST-2023; OMB-2025] |
| **Map the informal power, not the org chart** | Choosing gatekeepers and forum in a partnership | Who can move peers and who can quietly block; Empson describes a "leadership constellation" (review by Flood) [JOTWELL-EMPSON-2013] |
| **Tier the gate weight by risk** | Gate paths | Gate fatigue on low-risk items, and too little scrutiny on high-impact ones [HBR-2026; OMB-2025] |
| **Say at set-up that stopping is an expected output** | Setting expectations with the forum | Whether leaders will accept kills. Gartner forecast in 2024 that at least 30% of gen-AI projects would be abandoned after proof of concept by end of 2025 (a forecast) [GARTNER-2024]; S&P Global Market Intelligence's survey of more than 1,000 respondents in North America and Europe, as reported, found the average organization scrapped 46% of proofs of concept before production (respondent-reported, secondary) [CIODIVE-2025] |
| **Look for centre-of-excellence bottleneck signs** | Rebalance reviews | When to move the central team toward advisory [MSFT-COE-2026] |

## 6. Common traps

| Trap | Evidence | How to avoid it |
|---|---|---|
| **Pilot sprawl** | HBR describes "too many pilots with too little coordinated oversight" [HBR-2026]; the UK NAO found 15 of 32 bodies with deployed AI said use cases were always or usually identified at organisational level before deployment (NAO survey of UK government bodies, autumn 2023) [NAO-2024] | One register, one intake route, a live limit |
| **Centre as permanent gatekeeper** | Centralizing helps early and hurts later [MSFT-COE-2026] | Review the signals at each rebalance; plan the advisory move |
| **Gates without resource holders** | A Go without resources is "approval without resources" [COOPER-STAGEGATE-n.d.] | Gatekeepers are the people who control the next stage's resources |
| **No exit path** | NIST GOVERN 1.7 and OMB's discontinuation plan for under-performing high-impact AI [NIST-2023; OMB-2025] | A retire stage and a decommissioning route from day one |
| **Mandating partners** | Partnership limits the use of formal power [JOTWELL-EMPSON-2013] | Practice heads as gatekeepers; decisions made in the forum, not by memo |

## 7. Worked example: an accounting and advisory firm

*Illustrative.* The head of AI at a mid-sized accounting, tax and advisory firm already has an advisor plan for
the firm. Step 1 copies its levers (capacity → preparer hours per return; quality → review notes per return;
growth → advisory fees from existing clients) and its default weights, and sets `inherited_from`.

The inventory question turns up fourteen items across practices, including three near-identical drafting
assistants built by different teams and a firm-wide chat assistant licence request. The user agrees the six
default stages, adding the audit practice's existing independence check to the `g1` exit evidence for any
item that touches audit clients.

Gatekeepers: practice leaders at `g1` and `g2` (they control staff time), the risk and quality partner at `g2`
and `g3`, the finance director at `g3` and `g4`. Light path: items in the firm's lowest risk tier and individual-
productivity items combine `g1` and `g2`, and the head of AI decides `g0` alone. On the full path, the item's
sponsor and the practice leaders decide `g0` with the head of AI. Forum: managing partner,
practice leaders, risk and quality partner, heads of IT and finance, people lead and head of AI; monthly, with a
rebalance at every third review. Live limit: six, the number of owners who can give the work real time.

## 8. Output

`portfolio/portfolio.yaml` from `../templates/portfolio.yaml`, with `portfolio`, `settings`, `stages`,
`gate_paths` (including `g0_deciders`), `roles`, `rhythm` and `state` filled (schema: `../schemas/portfolio.md`). Inventory items found in
step 1 are logged in step 2. Set `state.step_completed: 1`, `next_step: 2`, `updated`.

## 9. Sources

- `BCG-2024` — Boston Consulting Group, *AI adoption in 2024: 74% of companies struggle to achieve and scale
  value*, press release, 2024-10-24. https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
- `CIODIVE-2025` — CIO Dive, *AI project failure rates are on the rise: report* (reporting S&P Global Market
  Intelligence), news report, 2025-03-14. https://www.ciodive.com/news/ai-project-fail-data-SPGlobal/742590/
- `COOPER-STAGEGATE-n.d.` — Robert G. Cooper, Stage-Gate International, *The Stage-Gate model: an overview*,
  method article, undated. https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- `GARTNER-2024` — Gartner, *Gartner predicts 30% of generative AI projects will be abandoned after proof of
  concept by end of 2025*, press release, 2024-07-29. https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025
- `HBR-2026` — Nelson, Davenport, Scade, *Manage your AI investments like a portfolio*, Harvard Business
  Review, 2026-01 (read via reprint). https://hbr.org/2026/01/manage-your-ai-investments-like-a-portfolio
- `JOTWELL-EMPSON-2013` — John Flood, JOTWELL, *How are professional service firms governed?* (review of
  Empson), scholarly review, 2013-09-24. https://legalpro.jotwell.com/?p=653
- `MSFT-COE-2026` — Microsoft Learn, *Establish an AI Center of Excellence*, vendor guidance, updated
  2026-04-10. https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/center-of-excellence
- `NAO-2024` — UK National Audit Office, *Use of artificial intelligence in government*, audit report,
  2024-03-15. https://www.nao.org.uk/wp-content/uploads/2024/03/use-of-artificial-intelligence-in-government.pdf
- `NIST-2023` — NIST, *AI Risk Management Framework (AI RMF 1.0)*, framework, 2023-01.
  https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `OMB-2025` — US Office of Management and Budget, *M-25-21*, government memorandum, 2025-04-03.
  https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf
- `UKGOV-2025` — UK Government Digital Service, *Artificial Intelligence Playbook for the UK Government*,
  government guidance, 2025. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html

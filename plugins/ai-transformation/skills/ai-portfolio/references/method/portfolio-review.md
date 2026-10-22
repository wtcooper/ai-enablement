# Portfolio review (step 5)

Read this on entering step 5: when a review is due, or when the user asks to "review our AI portfolio". It tells
you how to build the review pack, surface stop, redirect and scale decisions with their evidence, run the
rebalance, and record what the forum decided. Keys in brackets are listed in §7.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [What to surface and how](#3-what-to-surface-and-how)
4. [Traps](#4-traps)
5. [Worked example](#5-worked-example)
6. [Output](#6-output)
7. [Sources](#7-sources)

## 1. Goal and exit criteria

**Goal.** A forum that decides, not one that hears status. Regular reviews should add promising initiatives,
scale successful pilots, redirect struggling efforts, retire misaligned projects and recalibrate scoring criteria
[HBR-2026]. The pack makes those decisions easy to take and hard to dodge.

**Exit criteria.**

- A numbered pack `reviews/<n>-review.md` (Part A) built from `portfolio.yaml` and `benefits.yaml`.
- Every item that meets a surfacing rule (§3.1) appears under "Decisions asked", with evidence for and against.
- Part B records each decision with reason, resources or conditions, next gate and the roles who decided.
- `portfolio.yaml` updated: decisions carry the review number; `early_warnings`; `state.last_review`.
- On a rebalance review (every third by default, `setup.md` §3.2): the checks in §3.3.

## 2. How to run it

1. **Name the step.** "We are preparing review <n>: the pack first, then the decisions."
2. **Build the pipeline view**: counts by stage, changes since the last review, live items against the limit,
   no-AI items and the enablement line counted apart.
3. **Run the surfacing rules** (§3.1) on every active item. For several flagged items, use the
   `prepare-review-item` brief, one subagent per item (`SKILL.md`, Delegation).
4. **Write a decision block** per surfaced item: the ask, evidence for and against (each fact with its source),
   the kill criteria and whether any is met, early warnings, two or three options with what each costs and
   releases, and the item owner's recommendation.
5. **Add the balance, benefits and capacity sections** (template §5 to §7).
6. **Play the pack back** and ask: "Which decision here would you least like to take, and why?" The answer is
   usually the one the pack must make clearest.
7. **After the meeting**, record Part B as the user reports it. Record decisions; do not make them.
8. **Update** `portfolio.yaml` and, for benefits decisions, `benefits.yaml`. Set `state.last_review`.

## 3. What to surface and how

### 3.1 Surfacing rules

Surface an item for a decision when any of these holds (this skill's defaults, built on the cited practice):

| Rule | Typical ask | Basis |
|---|---|---|
| A kill criterion agreed at the last gate is met | Kill or recycle | [COOPER-STAGEGATE-n.d.] |
| **An early warning (slippage, cost overrun, performance shortfall) on two reviews running** (default; the forum can change it) | Redirect, hold or kill | Early-warning triggers reviewed at each review [HBR-2026] |
| Next-gate evidence not produced when the gate falls due, or owner or benefit owner lost | Hold, recycle or kill | |
| A technology change makes the build unnecessary | Recycle to buy | `stage-gates.md` §4 |
| A benefit is `not-realised` at its planned review point | Redirect or retire | [IVI-ITCMF-n.d.] |
| Pilot evidence meets `g3`, or production evidence meets `g4` | Go to production or scale | |
| An item still pending `g0` with the forum, or the highest-scoring held item when live capacity opens | Decide `g0`; Go | Advancement by resources and fixed criteria [HBR-2026] |

### 3.2 Stop or redirect

Use the causes in `stage-gates.md` §5.1. Before recommending a stop on value alone, check the planned review point:
measured value can lag the investment (`stage-gates.md` §4). Report leading indicators (adoption quality, process
change, error rates) at early reviews.

### 3.3 Rebalance review

- **Balance:** near, medium and long horizons; risk and return; capability areas; foundations later items need
  [HBR-2026]. A portfolio of only quick wins or only moonshots is a finding.
- **Recalibrate criteria and weights** [HBR-2026], for example when the forum's decisions keep overriding the
  scores.
- **Live limit:** owners carrying more than one live item; shared reviewers stretched.
- **The central team's signals:** approval delays, experts who cannot cover all teams, recurring priority debates
  [MSFT-COE-2026].

### 3.4 In a partner-led firm

Lead each decision block with a named workflow and its baseline, not a tool demo (an inference from the partner sources), and check how claimed time
savings were measured; practitioners' own estimates are self-reported [PAPERJAM-2025]. Separate usage from value:
in the Thomson Reuters Institute's 2026 survey of legal, tax and accounting, corporate and government
professionals, 18% knew their organization tracked the ROI of AI tools (respondent-reported) [TRI-AIPS-2026]. Ask
each skeptic what result would change their mind (`people-and-change.md`).

## 4. Traps

| Trap | How to avoid it |
|---|---|
| **Status theatre:** updates with no decisions | Every surfaced item ends with a recorded outcome or a named open question |
| **Adoption reported as value.** In McKinsey's 2026 global survey (1,719 participants), 80% say AI improved their individual productivity, against 37% reporting an EBIT contribution (respondent-reported) [MCK-2026] | Usage and value on separate lines; use-case and enterprise effects apart |
| **The pack argues for an outcome** | Evidence for and against, options, then the owner's recommendation, labelled |

## 5. Worked example

*Illustrative;* review 3, a rebalance. **Pipeline:** live (prototype, pilot, scale) three of six; chat licences on
the enablement line. **Decisions asked:** K-1 extraction met its `g3` evidence (Go to production); a
document-summary pilot shows slippage on two reviews running and has lost its owner (Hold or Kill); know-how
search is held behind the library clean-up, which has passed `g2` (Go into discover). **Rebalance:** every item
past discover is a near-horizon capacity play; the forum asks advisory for a new-value idea. **Part B:** K-1 Go,
with the capacity decision recorded in `benefits.yaml`; document summary Kill, evaluation set and prompts kept;
know-how search Go.

## 6. Output

`portfolio/reviews/<n>-review.md` from `../templates/review.md`. In `portfolio.yaml`: decisions with
`review: <n>`, `early_warnings`, stage and status changes, `state.last_review: <n>`, `state.step_completed: 5`,
`updated`. In `benefits.yaml`: status changes and capacity decisions taken in the review.

## 7. Sources

- `COOPER-STAGEGATE-n.d.` — Robert G. Cooper, Stage-Gate International, *The Stage-Gate model: an overview*, method article, undated. https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- `HBR-2026` — Nelson, Davenport, Scade, *Manage your AI investments like a portfolio*, Harvard Business Review, 2026-01 (read via reprint). https://hbr.org/2026/01/manage-your-ai-investments-like-a-portfolio
- `IVI-ITCMF-n.d.` — Innovation Value Institute, *Benefits Harvesting (IT-CMF 18.07)*, maturity-model guidance, undated. https://portal.ivi.ie/+itcmf/18.07/value/BAR/C/C3
- `MCK-2026` — McKinsey & Company, *The state of AI in 2026*, consultancy survey, 2026-08. https://www.mckinsey.com.br/en/our-insights/the-state-of-ai
- `MSFT-COE-2026` — Microsoft Learn, *Establish an AI Center of Excellence*, vendor guidance, updated 2026-04-10. https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/center-of-excellence
- `PAPERJAM-2025` — Paperjam, *Why AI is a strategic priority for modern law firms: Francesca Bennetts*, practitioner interview, 2025-06-19. https://en.paperjam.lu/article/why-ai-is-a-strategic-priority-for-modern-law-firms-francesca-bennetts
- `TRI-AIPS-2026` — Thomson Reuters Institute, *2026 AI in professional services report*, survey report summary, 2026-02-09. https://www.thomsonreuters.com/en-us/posts/technology/ai-in-professional-services-report-2026/

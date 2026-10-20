# Launch and post-launch review (step 6)

Read this on entering step 6, and again at every later review. It covers the staged launch and the numbered
post-launch reviews: what was promised in the evaluation plan and the benefits register against what happened,
what the overrides and incidents say, how the evaluation set must change, and whether the solution should
continue, tighten, loosen, be redesigned or retire. Keys in brackets are listed in §9. Lines marked *(advisor
default)* are working rules, not findings from a source.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Review points and what a review covers](#3-review-points-and-what-a-review-covers)
4. [Decision rules](#4-decision-rules)
5. [Question bank](#5-question-bank)
6. [Expert moves](#6-expert-moves)
7. [Common traps](#7-common-traps)
8. [Worked example: evidence matching in an audit practice](#8-worked-example-evidence-matching-in-an-audit-practice)
9. [Output and sources](#9-output-and-sources)

## 1. Goal and exit criteria

**Goal.** Know, with evidence, whether the solution does what was promised, and act on it: keep it, change it,
widen it, or stop it.

**Exit for each review when all of these are true:**

- The launch record shows each widening and the evidence that allowed it.
- Promised versus achieved is set out for the eval-plan thresholds and for each benefit in the register, as
  ranges with their basis (from record, reported, observed).
- Overrides, escalations, incidents and near misses are analysed, with what changed as a result.
- Eval-set health is checked: escaped errors added, saturated cases moved, re-baseline decided.
- Cost and usage are compared with the envelope; user feedback themes recorded.
- A decision (continue, tighten, loosen, redesign, retire) with its evidence, the rung confirmed or changed, and
  the event that triggers the next review.
- Handoffs made: gate evidence and benefit actuals to **ai-portfolio**, the reusable workflow to
  **ai-enablement**, policy or vendor issues to **ai-governance**.

## 2. How to run it

1. **Name the step** and which review this is (Review 1, 2, ...).
2. **Read the inputs:** the eval plan's monitoring table and results log, the readiness launch plan, the last
   review, and the rows for this solution in `portfolio/benefits.yaml` (written by **ai-portfolio**).
3. **Record the launch so far:** which groups use it, at what review level, and what evidence allowed each step.
4. **Promised versus achieved** (§3.2): eval thresholds first, then benefits. Ask how each figure was measured.
5. **Read the overrides** before the averages: what users corrected tells you what the solution gets wrong.
6. **Incidents and near misses:** what happened, the cause, and whether evals, guardrails or training changed
   [NIST-2024, MG-4.2-002].
7. **Eval-set health** (§3.3).
8. **Decide** using §4; confirm or change the rung; set the next review trigger.
9. **Hand off** the evidence and the workflow; update the files; play back the decision.

## 3. Review points and what a review covers

### 3.1 Review points are events, not dates

Set review points by what has to have happened, not by the calendar (rule 9):

| Review | Triggered by | Main question |
|---|---|---|
| Review 1 | The first full trace-review cycle on live work with the first group | Does live quality match the eval results? |
| Review 2 | The benefit horizon stated in the business case or benefits register | Is the benefit appearing against the counterfactual? |
| Later reviews | The portfolio's review rhythm for live items | Keep, widen, change or retire? |
| Triggered review | An incident, a model or vendor change, an override spike, a metric outside its range | What broke, and what must change? |

Practitioner guidance puts trace-review cycles at two to four weeks [HUSAIN-2026]; use that as a cadence for
reading traces, not as a deadline.

### 3.2 Promised versus achieved

- **Against the eval plan:** pass-all and zero-tolerance results on the regression suite, live error categories
  from sampled traces, override and escalation rates against their normal range.
- **Against the benefits register:** the forecast range, baseline and counterfactual for each benefit row;
  actuals as ranges with their basis. Report realised against expected, never activity counts as impact.
- **Check how time savings were measured.** Self-reported savings are recollections; A&O Shearman's lawyers
  "report saving two to three hours a week" in a partner's interview account (self-reported) [PAPERJAM-2025].
- **Plot over time.** Read trends against the normal range before reacting to one bad week; see the control plan
  in `../../../transformation-advisor/references/method/plan-and-control.md` §3.3.

### 3.3 Eval-set health

- Add every escaped error as a new case [HUSAIN-2026].
- Graduate capability cases that pass reliably into the regression suite; retire cases that always pass and cost
  a lot [ANTHROPIC-2026; HUSAIN-2026].
- Ask what changed in the inputs or users since the cases were built; re-baseline when the product or process
  changes [APPLIEDLLMS-2024, 2.1.1; ANTHROPIC-2026].

### 3.4 People and reuse

- Ask pilot users what would happen if the tool were taken away, and report the answer; dependence is stronger
  evidence for peers than satisfaction (a partner's recollection, self-reported) [PAPERJAM-2025].
- Adoption by group: who uses it, who does not, and why. Hand uneven adoption to **ai-enablement**.
- Lessons for other teams: which parts are reusable (cases, checklist, design) and which were local.

## 4. Decision rules

- **High or rising override rate, or overrides that consistently beat the output:** revise or redevelop
  [FRB-2011].
- **Loosen human review** only after a measured sample shows stable quality across at least one full review
  cycle; **tighten immediately** after an incident *(advisor default)*.
- **Move up a rung** only when the written promotion rule from the design brief is met; move down on a miss
  [ANTHROPIC-2024; OPENAI-2025].
- **Benefit not appearing** at its horizon against the counterfactual: say so, record the lesson, and take a
  continue, redesign or retire decision to **ai-portfolio**; do not extend the horizon silently.
- **Retire** when the solution no longer earns its run and review cost, or the work it supports has changed; plan
  decommissioning as a step, not an afterthought [NIST-2024, GV-1.7].
- **Any change** to model, prompt, retrieval or tools re-runs the regression suite before release (readiness
  change rule).

## 5. Question bank

- What did we say success would look like at this review point? Did it happen? [T][U/O]
- What is the override and rework rate now versus the pilot, and what do the overrides tell us? [T][U/O]
- Which eval cases now always pass, and which new failures need cases? [T]
- What changed in the inputs or users since we built the test set? [T][U/O]
- What did the incident or near-miss review find, and did we update evals, guardrails or training? [U/O]
- Should this move up or down the autonomy ladder? What evidence supports that? [U/O]
- What would people do if we took it away? [T]
- Which parts can other teams reuse, and which were local? [U/O]

## 6. Expert moves

1. **Read overrides before averages.** They show where users do not trust or cannot use the output [FRB-2011;
   NIST-2024, MS-4.2-004].
2. **Sample fresh traces every cycle**, 100 or more per review cycle as practitioner guidance [HUSAIN-2026].
3. **Retire or demote evals that always pass; re-baseline when the product changes** [ANTHROPIC-2026;
   HUSAIN-2026].
4. **Track cost per task and test a smaller model against the same evals** [OPENAI-2025; ANTHROPIC-2026].
5. **Ask the "take it away" question** and report the answer to the sponsor [PAPERJAM-2025].
6. **Turn every incident into a case, a guardrail or a training point** [NIST-2024, MG-4.2-002].

## 7. Common traps

| Trap | Evidence | How to avoid |
|---|---|---|
| Activity reported as impact | Usage counts are easy; value needs a baseline and counterfactual (see `plan-and-control.md` §3.5 in the shared method) | Realised against expected, by benefit row |
| Trusting self-reported savings | Recollections are not tracked data [PAPERJAM-2025] | Ask how each figure was measured |
| Silent decay | [GOOGLE-RULES, Rule 10] | Coverage and freshness metrics in every review |
| Stale gold set | 100% pass suggests evals are not challenging enough [HUSAIN-2026] | Add escaped errors; graduate and retire cases |
| Autonomy creep | Review loosened without evidence | Written promotion rule; tighten after incidents |
| Model change breaks the workflow | Newer models do not guarantee better agent performance [BERKELEY-2026] | Regression run on every change |

## 8. Worked example: evidence matching in an audit practice

Illustrative. Review 1, triggered by the end of the first ten production engagements.

- **Promised versus achieved:** zero-tolerance checks held on regression runs after one platform release (the
  new re-run rule caught a change in date handling before use). Re-performance disagreement inside the agreed
  range on 9 of 10 engagements; the tenth had poor scans and was matched by hand.
- **Overrides:** concentrated on approval evidence in email threads (about a third of overrides); the checklist
  line is reworded and five new cases added.
- **Benefit:** net hours per engagement inside the low half of the forecast range against the staggered-start
  offices (from time records); review notes on evidence flat against last season.
- **Users:** asked what would happen if it were taken away, most seniors said they would object; two staff still
  match by hand, so **ai-enablement** adds a short session on reading the source links.
- **Decision:** continue; widen to all engagements in the practice. The rung stays at `augment`; the owner will
  consider sampled review for invoice evidence only after Review 2, if re-performance stays inside its range.
- **Handoffs:** actuals to **ai-portfolio** for `portfolio/benefits.yaml` and the gate into scale; the checklist,
  cases and review procedure to **ai-enablement** as a workflow for other offices.
- **Next review when:** the benefit horizon in the register is reached, or any metric leaves its range.

## 9. Output and sources

**Output.** Create or update `post-launch.md` from `../templates/post-launch.md`: update the launch record and add
a new numbered review section (never edit an earlier one). Set its frontmatter (`reviews_completed`,
`last_decision`, `next_review_when`). In `brief.md` set `status` (`live`, `paused`, `stopped` or `retired`),
`step_completed: 6`, `next_step: null` and `updated`; update `classification.ladder` if the rung changed and log
the decision.

**Sources**

- `ANTHROPIC-2024` — Anthropic, *Building effective agents*, 2024-12-19. https://www.anthropic.com/engineering/building-effective-agents
- `ANTHROPIC-2026` — Anthropic, *Demystifying evals for AI agents*, 2026-01-09.
  https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- `APPLIEDLLMS-2024` — Yan et al., *What We've Learned From A Year of Building with LLMs*, 2024-06-08. https://applied-llms.org/
- `BERKELEY-2026` — Pan, Arabzadeh et al., *Measuring Agents in Production*, 2026-06-04. https://arxiv.org/pdf/2512.04123
- `FRB-2011` — Federal Reserve Board and OCC, *SR 11-7: Supervisory Guidance on Model Risk Management*,
  2011-04-04. https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
- `GOOGLE-RULES` — Google for Developers, *Rules of Machine Learning*, undated. https://developers.google.com/machine-learning/guides/rules-of-ml
- `HUSAIN-2026` — Hamel Husain, *LLM Evals: Everything You Need to Know (FAQ)*, 2026-09-18. https://hamel.dev/blog/posts/evals-faq/
- `NIST-2024` — NIST, *AI 600-1: Generative AI Profile*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `OPENAI-2025` — OpenAI, *A practical guide to building agents*, 2025-04.
  https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `PAPERJAM-2025` — Paperjam, *Why AI is a strategic priority for modern law firms: Francesca Bennetts*,
  practitioner interview, 2025-06-19. https://en.paperjam.lu/article/why-ai-is-a-strategic-priority-for-modern-law-firms-francesca-bennetts

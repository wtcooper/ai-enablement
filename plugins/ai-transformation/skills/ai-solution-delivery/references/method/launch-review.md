# Launch and post-launch review (step 6)

Read this on entering step 6 and at every later review. It covers the staged launch and the numbered post-launch
reviews: promised against achieved, what overrides and incidents say, how the eval set must change, and whether
to continue, tighten, loosen, redesign or retire. Keys in brackets are listed in §6. Lines marked *(advisor
default)* are working rules, not findings from a source.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Review points and what a review covers](#3-review-points-and-what-a-review-covers)
4. [Decision rules](#4-decision-rules)
5. [Worked example: evidence matching in an audit practice](#5-worked-example-evidence-matching-in-an-audit-practice)
6. [Output and sources](#6-output-and-sources)

## 1. Goal and exit criteria

**Goal.** Know, with evidence, whether the solution does what was promised, and act on it.

**Exit for each review when all of these are true:**

- The launch record shows each widening and the evidence that allowed it.
- Promised versus achieved is set out for the eval-plan thresholds and each benefit in the register, as ranges
  with their basis (from record, reported, observed).
- Overrides, escalations, incidents and near misses analysed, with what changed as a result.
- Eval-set health checked; cost and usage compared with the envelope; user feedback recorded.
- A decision (continue, tighten, loosen, redesign, retire) with its evidence, the rung confirmed or changed, and
  the event that triggers the next review.
- Handoffs made: gate evidence and benefit actuals to **ai-portfolio**, the reusable workflow to
  **ai-enablement**, policy or vendor issues to **ai-governance**.

## 2. How to run it

1. **Name the review** (Review 1, 2, ...) and read the inputs: the eval plan's monitoring table and results log,
   the readiness launch plan, the last review, and this solution's rows in `portfolio/benefits.yaml` (written by
   **ai-portfolio**).
2. **Record the launch so far:** which groups use it, at what review level, and what evidence allowed each step.
3. **Promised versus achieved** (§3.2): eval thresholds first, then benefits. Ask how each figure was measured.
4. **Read the overrides before the averages:** what users corrected shows where they do not trust or cannot use
   the output [FRB-2011; NIST-2024, MS-4.2-004].
5. **Incidents and near misses:** cause, and whether evals, guardrails or training changed; turn each into a
   case, a guardrail or a training point [NIST-2024, MG-4.2-002].
6. **Eval-set health** (§3.3) and **people and reuse** (§3.4).
7. **Decide** using §4; set the next review trigger; hand off; update the files; play back the decision.

## 3. Review points and what a review covers

### 3.1 Review points are events, not dates

| Review | Triggered by | Main question |
|---|---|---|
| Review 1 | The first full trace-review cycle on live work with the first group | Does live quality match the eval results? |
| Review 2 | The benefit horizon in the business case or benefits register | Is the benefit appearing against the counterfactual? |
| Later reviews | The portfolio's review rhythm for live items | Keep, widen, change or retire? |
| Triggered review | An incident, a model or vendor change, an override spike, a metric outside its range | What broke, and what must change? |

Practitioner guidance puts trace-review cycles at two to four weeks, with 100 or more fresh traces per cycle
[HUSAIN-2026]; use that as a cadence for reading traces, not as a deadline (rule 9).

### 3.2 Promised versus achieved

- **Against the eval plan:** pass-all and zero-tolerance results on the regression suite, live error categories,
  override and escalation rates against their normal range.
- **Against the benefits register:** forecast range, baseline and counterfactual per benefit row; actuals as
  ranges with their basis. Report realised against expected, never activity counts as impact.
- **Check how time savings were measured.** Self-reported savings are recollections: A&O Shearman's lawyers
  "report saving two to three hours a week" in a partner's interview account (self-reported) [PAPERJAM-2025].
- **Plot over time** against the normal range before reacting to one bad week; see the control plan in
  `../../../transformation-advisor/references/method/plan-and-control.md` §3.3.

### 3.3 Eval-set health

Add every escaped error as a case [HUSAIN-2026]. Graduate reliable capability cases into regression and retire
cases that always pass [ANTHROPIC-2026; HUSAIN-2026]. Ask what changed in the inputs or users, and re-baseline
when the product or process changes [APPLIEDLLMS-2024, 2.1.1; ANTHROPIC-2026]. Watch coverage and freshness, not
only outputs, for silent decay [GOOGLE-RULES, Rule 10].

### 3.4 People and reuse

- Ask users what would happen if the tool were taken away. A law firm partner recalled hearing a unanimous no
  (self-reported) [PAPERJAM-2025]; such answers persuade peers more than a satisfaction score *(advisor
  default)*.
- Adoption by group: who uses it, who does not, and why; hand uneven adoption to **ai-enablement**.
- Lessons for other teams: which parts are reusable (cases, checklist, design) and which were local.

## 4. Decision rules

- **High or rising override rate, or overrides that consistently beat the output:** revise or redevelop
  [FRB-2011].
- **Loosen human review** only after a measured sample shows stable quality across at least one full review
  cycle; **tighten immediately** after an incident *(advisor default)*.
- **Move up a rung** only when the design brief's written rule is met; move down on a miss [ANTHROPIC-2024;
  OPENAI-2025].
- **Benefit not appearing** at its horizon: say so, record the lesson, and take a continue, redesign or retire
  decision to **ai-portfolio**; never extend the horizon silently.
- **Retire** when the solution no longer earns its run and review cost, or the work has changed; plan
  decommissioning as a step [NIST-2024, GV-1.7].
- **Any change** to model, prompt, retrieval or tools re-runs the regression suite before release; newer models
  do not guarantee better agent performance [BERKELEY-2026]. Test a smaller model against the same evals when
  cost per task matters [OPENAI-2025].

## 5. Worked example: evidence matching in an audit practice

Illustrative. Review 1, after the first ten production engagements.

- **Promised versus achieved:** zero-tolerance checks held; the re-run rule caught a date-handling change before
  use. Net hours per engagement sit in the low half of the forecast range against the staggered-start offices
  (from time records).
- **Overrides:** about a third concern approval evidence in emails; the checklist line is reworded and five cases
  added.
- **Decision:** continue and widen to all engagements; the rung stays at `augment`. Actuals go to
  **ai-portfolio**; the checklist and review procedure go to **ai-enablement** as a workflow. **Next review
  when:** the benefit horizon is reached, or any metric leaves its range.

## 6. Output and sources

**Output.** Create or update `post-launch.md` from `../templates/post-launch.md`: update the launch record and add
a new numbered review section (never edit an earlier one). Set its frontmatter (`reviews_completed`,
`last_decision`, `next_review_when`). In `brief.md` set `status` (`live`, `paused`, `stopped` or `retired`),
`step_completed: 6`, `next_step: null` and `updated`; update `classification.ladder` if the rung changed and log
the decision.

**Sources**

- `ANTHROPIC-2024` — Anthropic, *Building effective agents*, 2024-12-19. https://www.anthropic.com/engineering/building-effective-agents
- `ANTHROPIC-2026` — Anthropic, *Demystifying evals for AI agents*, 2026-01-09. https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- `APPLIEDLLMS-2024` — Yan et al., *What We've Learned From A Year of Building with LLMs*, 2024-06-08. https://applied-llms.org/
- `BERKELEY-2026` — Pan, Arabzadeh et al., *Measuring Agents in Production*, 2026-06-04. https://arxiv.org/pdf/2512.04123
- `FRB-2011` — Federal Reserve Board and OCC, *SR 11-7: Supervisory Guidance on Model Risk Management*, 2011-04-04. https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
- `GOOGLE-RULES` — Google for Developers, *Rules of Machine Learning*, page last updated 2025-08-25. https://developers.google.com/machine-learning/guides/rules-of-ml
- `HUSAIN-2026` — Hamel Husain, *LLM Evals: Everything You Need to Know (FAQ)*, 2026-09-18. https://hamel.dev/blog/posts/evals-faq/
- `NIST-2024` — NIST, *AI 600-1: Generative AI Profile*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `OPENAI-2025` — OpenAI, *A practical guide to building agents*, 2025-04. https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `PAPERJAM-2025` — Paperjam, *Why AI is a strategic priority for modern law firms: Francesca Bennetts*, practitioner interview, 2025-06-19. https://en.paperjam.lu/article/why-ai-is-a-strategic-priority-for-modern-law-firms-francesca-bennetts

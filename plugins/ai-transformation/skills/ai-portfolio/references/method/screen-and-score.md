# Screen and score (step 3)

Read this on entering step 3: screen intake items, score them on two axes (value and readiness) and record the
screening gate (`g0`). Keys in brackets are listed in §7.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Axes, rules and thresholds](#3-axes-rules-and-thresholds)
4. [Questions and traps](#4-questions-and-traps)
5. [Worked example](#5-worked-example)
6. [Output](#6-output)
7. [Sources](#7-sources)

## 1. Goal and exit criteria

**Goal.** Decide which ideas earn discovery effort, with the reasons visible: is it worth it, and is it ready?
Cooper keeps business-value criteria apart from project-readiness criteria at every gate [COOPER-STAGEGATE-n.d.].
Treat the scores as a facilitation device, not a validated model.

**Exit criteria** for each screened item:

- Passed the pre-score gates (§3.1), or closed with the reason; the readiness checklist (§3.3) answered.
- A value range per lever (no range, no value score); six scores with what each rests on; both indexes.
- `category`, `horizon`, `risk_tier`, `gate_path` and a sponsor who controls discovery resources.
- A `g0` decision by the path's `g0_deciders`: Go into discover, Kill, Hold (with `revisit_when`) or Recycle (back
  to the submitter with what to rework), or "pending the forum" while no deciders are named. Every Go carries
  `kill_criteria` (from the plan's go/no-go when one exists) and `next_gate`.

## 2. How to run it

1. **Confirm the weights** from `settings.scoring_weights`. Do not re-open them item by item; recalibration
   happens at a rebalance review [HBR-2026].
2. **Run the pre-score gates** (§3.1) on each item.
3. **Size as ranges.** Per lever: low, high, unit and the main assumption, from the volume recorded at intake.
4. **Score across, not down.** One dimension at a time across all items, using the anchors in
   `../../../transformation-advisor/references/method/prioritize.md` §3.3. Say what each score rests on.
5. **Compute** `weighted_score` and the two indexes (§3.2). Show the items on the two axes.
6. **Answer the readiness checklist** (§3.3). A weak answer lowers feasibility or data readiness, or becomes a
   condition on the Go.
7. **Categorize** with the shared category rules (prioritize §3.4) and set the horizon.
8. **Check against the portfolio**: duplicates, dependencies on foundation items and the balance. Note where the
   item would sit in the queue for the live limit. The limit binds a Go into prototype, pilot or scale (`g1`, `g2`,
   `g4`), not the `g0` Go into discover, so never list it as `g0` evidence.
9. **Propose kill criteria** for each likely Go. When the intake record's "From the plan" section has a go/no-go,
    start from it; if you propose something different, say how it differs and why.
10. **Record the `g0` decision** by the deciders named for the item's path in `gate_paths.g0_deciders`. If no
    deciders are named for that path, do not append a `g0` decision: write the proposed outcome in the record's
    Screen result as "pending the forum", keep `stage: intake`, set `next_gate.gate: g0`, and put the item in the
    next review pack. Play back, write, update state.

## 3. Axes, rules and thresholds

### 3.1 Pre-score gates

Use the shared gates first (should it exist, rules, simpler fix, constraint, stage; prioritize §3.2), then two
portfolio checks:

| Check | Test | If it fails |
|---|---|---|
| Worth a year | "What would have to be true for this to be worth a year of a team's time?" RAND recommends committing product teams to a specific problem for at least a year [RAND-2024] | Kill or park as a passing idea |
| Right metric | The metric the team would optimize is the one the benefit owner watches; RAND's interviewees described models optimized for the wrong metrics [RAND-2024] | Recycle with the metric agreed with the benefit owner |

### 3.2 Two axes from six scores

| Axis | Dimensions | Plain question |
|---|---|---|
| **Value** | value, strategic fit, time to value | "Is it worth it?" |
| **Readiness** | feasibility, data readiness, risk (higher score = lower risk) | "Can we do it safely now?" |

Each index is the weighted mean of its three scores, with the portfolio's weights renormalized within the axis (a
skill heuristic). Report both next to `weighted_score`; never let a high value index hide a low readiness index.

**Default quadrant thresholds: 3.5 on each axis** (no source sets them; the forum can change them at a rebalance).

| | Readiness ≥ 3.5 | Readiness < 3.5 |
|---|---|---|
| **Value ≥ 3.5** | Go to discover | Go with readiness work named as conditions, or Hold behind a foundation item logged in its own right |
| **Value < 3.5** | Go only on the light path and if cheap; else Hold or Kill | Kill, or Hold with a `revisit_when` trigger |

When scoring feasibility, count people-and-process readiness (an owner, process redesign, adoption) at least as
much as technical feasibility; BCG attributes about 70% of implementation challenges to people and process (survey
of 1,000 CxOs and senior executives) [BCG-2024]. The weighting is this skill's default, not BCG's.

### 3.3 Readiness checklist

From HBR's gate tests and Microsoft's data inventory [HBR-2026; MSFT-PLAN-2026]: owner named; benefit owner named
or a step to name one; data sources, formats, quality and access known; skills in place or a route to source them;
whether the process needs redesign and who owns that; the controls the risk tier needs.

### 3.4 Payback

Do not apply a technology-style payback hurdle of under a year; AI value usually takes longer (`stage-gates.md` §4).

## 4. Questions and traps

Ask which candidate has the weakest evidence, and whether the people who would build it have the skills or would
source them [HBR-2026]. Agree the metric with the benefit owner before a Go: of RAND's 50 industry interviewees,
84% cited leadership-driven failures, such as the wrong problem or metric, as a primary reason AI projects fail
(interviewee perceptions) [RAND-2024].

## 5. Worked example

*Illustrative scores.* Default weights (value 0.30, feasibility 0.20, data readiness 0.15, risk 0.15, time to value
0.10, strategic fit 0.10). V, SF, T form the value axis; F, D, R the readiness axis.

| Item | V | SF | T | F | D | R | Weighted | Value idx | Ready idx | `g0` |
|---|---|---|---|---|---|---|---|---|---|---|
| K-1 extraction (grade B) | 4 | 4 | 4 | 4 | 3 | 3 | 3.70 | 4.00 | 3.40 | Go, with "data seen in real state" as a `g1` condition |
| Know-how search over the precedent library (grade B) | 4 | 4 | 2 | 3 | 2 | 4 | 3.30 | 3.60 | 3.00 | Hold behind a new foundation item: clean up the library first |

The know-how search shows why the axes matter: its weighted score looks acceptable, but data readiness holds
readiness below 3.5, so a library clean-up is logged as a foundation item and the search waits for it to pass `g2`.

## 6. Output

Per item in `portfolio.yaml`: `value`, `scores`, `weighted_score`, `value_index`, `readiness_index`, `category`,
`horizon`, `risk_tier`, `gate_path`, `sponsor`, `depends_on`, a `g0` entry in `decisions`, and on a Go
`stage: discover`, `status: active`, `kill_criteria` and `next_gate`. Fill the record's Screen result. Set
`state.step_completed: 3` (first time through), `next_step` to the step now due (4 for a gate, 5 for a review) and
`updated`. Refresh or remove header comments that still describe an earlier step.

## 7. Sources

- `BCG-2024` — Boston Consulting Group, *AI adoption in 2024: 74% of companies struggle to achieve and scale value*, press release, 2024-10-24. https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
- `COOPER-STAGEGATE-n.d.` — Robert G. Cooper, Stage-Gate International, *The Stage-Gate model: an overview*, method article, undated. https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- `HBR-2026` — Nelson, Davenport, Scade, *Manage your AI investments like a portfolio*, Harvard Business Review, 2026-01 (read via reprint). https://hbr.org/2026/01/manage-your-ai-investments-like-a-portfolio
- `MSFT-PLAN-2026` — Microsoft Learn, *Plan for AI adoption*, vendor guidance, updated 2026-10-15. https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/plan
- `RAND-2024` — RAND Corporation, *The root causes of failure for artificial intelligence projects and how they can succeed*, research report, 2024-08-13. https://www.rand.org/pubs/research_reports/RRA2680-1.html

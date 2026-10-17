# Make the case (phase 6)

Read this on entering phase 6. It tells you how to build a one-page case for each of the top three to
five opportunities, and the portfolio view at higher levels: value as ranges with assumptions and
provenance, the cost stack, risks, human checkpoints and role evolution. Keys in brackets are in §9.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Building the case](#3-building-the-case)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example: evidence matching](#7-worked-example-evidence-matching)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** A case a skeptical sponsor or finance lead can check: what changes, what it is worth as a range,
what it costs, what could go wrong, who checks the work, what happens to people's roles, and how we will
know it worked. Never a single-point ROI (rule 3 in `SKILL.md`).

**Exit criteria** for each top opportunity:

- A baseline from actual recent records, with the source of every number stated.
- Value lines per lever from the plan's value levers, each with `low`, `high`, `unit` and `assumptions`.
- Hours released split into absorbed, redeployed and cashable (§3.2); only cashable hours carry money as cost.
- A cost stack with low and high (§3.4) and the measurement horizon.
- Evidence cited with use-case ids, evidence grade and the provenance of every figure.
- Risks, human checkpoints and `role_evolution` with an explicit `capacity_use` choice (redeploy or reduce,
  see `people-and-change.md`). Required for team scope and above.
- A measurement plan: comparison method, three to five KPIs including a quality guardrail, go/no-go criteria.
- The two or three assumptions that drive the result, named so the pilot tests them first.
- At unit or organization scope: a portfolio view (§3.7). The user has confirmed each case.

## 2. How to run it

1. **Name the phase.** "We are making the case for your top opportunities. Next comes the plan."
2. **Optional independent check.** Use subagents for this step: delegate one subagent per top opportunity,
   in parallel, using the `review-opportunities` brief, to check score, risks, checkpoints, role evolution
   and the rules. If you cannot start subagents, do each check yourself, one at a time. Play back findings.
3. **Baseline first.** Ask for last month's or last cycle's actual volume, time, rework and cost, from records.
4. **Build the value tree**: lever → metric → driver → assumption (§3.1). One question at a time.
5. **Convert hours to value** (§3.2) and put every uncertain input as a range (§3.3).
6. **Cost it** (§3.4), then **risk-adjust** and keep option value separate (§3.5).
7. **People and checkpoints.** Agree tasks moving, new work and the capacity choice. Name the checkpoints.
8. **Design the proof** (§3.6). Play back the one-page case; ask "What would make a finance lead doubt
   this?" and fix the weakest line. Write the output (§8) and update the plan state.

**Adapt by journey stage.** Curious: a short case per quick win (baseline, range, one KPI). Experimenting
and Adopting: full one-page cases; insist on a baseline before any pilot. Scaling: add shared platform costs
and the portfolio bridge. AI-native: model-scope cases need revenue mechanics (price, volume, new clients)
and scenario ranges, not productivity arithmetic.

## 3. Building the case

### 3.1 Value tree

For each lever the plan weights, write one line: **lever → metric → driver → assumption**. Example:
quality → share of workpapers returned by review → agent cites evidence for every attribute → reviewers
find fewer missing tick-marks. Each lever needs its own proof: cost and capacity from operating data,
quality from a defined error or rework measure, growth from an attribution method, risk from an
expected-loss view, experience from a survey (advisor synthesis; [GARTNER-CSO-2026] on tying gains to
measured gaps).

### 3.2 From hours released to value realized

Hours released are not value. In the UK cross-government Copilot trial, users reported saving 26 minutes a
day, but the evaluators could not tell how the time was used (self-reported) [UKGDS-2025]; a departmental
evaluation found no robust evidence that time savings improved productivity, though measuring that was not a
main aim [UKDBT-2025].

1. **Gross hours** = volume × hands-on hours per item × share of items in scope × time saving (range).
2. **Net hours** = gross − added review, correction and new tasks − first-year learning time. A vendor survey
   reports nearly 40% of AI time savings lost to rework (vendor-published) [WORKDAY-2026].
3. **Adoption**: multiply by the share of people or items that will actually use it, as a range.
4. **Process cap**: a step's speed-up moves end-to-end time only in proportion to its share of elapsed
   time, and only if the next step can absorb the output [LEI-PEPERKAMP-2026]. Acemoglu applies the same
   share-of-tasks logic to the whole economy [NBER-ACEMOGLU-2024].
5. **Destination** — split net hours three ways (the split is advisor synthesis [GARTNER-CSO-2026]):
   - **Absorbed**: time that disappears into more email or more of the same. Counts as zero.
   - **Redeployed**: a named destination with an owner and an output metric (backlog cleared, more
     clients served, faster turnaround, deeper review). Money only if the output has a price and demand.
   - **Cashable**: cost that actually goes away: external spend, contractors, overtime, avoided hires or a
     role reduction decided openly under rule 2. Only this bucket enters a cost line, at loaded cost.

In a Gartner survey of 114 HR leaders, only 7% of organizations gave employees guidance on using time saved
by AI [GARTNER-HR-2025]: ask who owns the freed hours before valuing them.

### 3.3 Ranges, assumptions and what to measure first

- Every uncertain input is a low–high range; show low and high cases (a base case may sit between).
- Name the two or three inputs that move the answer most, usually adoption, net saving after review, and
  the redeployed share. Measure those first; stop measuring when more certainty would not change the
  decision [HDR-AIE].
- Do not take felt time savings as data: in an RCT, experienced developers expected 24% faster, believed
  20% faster afterwards, and measured 19% slower (independent, narrow setting) [METR-2025].
- If a payback period is asked for, give it as a range from the low and high cases.

### 3.4 Cost stack (ask who owns each line)

Licences or seats · consumption (tokens, with a growth assumption) · platform and integration · build and
configuration · evaluation set and parallel running · governance and security review · training and change
support · reviewer time · maintenance and re-testing when models or systems change · data preparation.
Unit prices fall but consumption grows: agentic and reasoning work can use five to thirty times the tokens
of chat (secondary figure) [FINOPS-2026]. Only 26% of surveyed organizations have full real-time visibility
of AI operating cost (self-reported) [KPMG-2026], so plan how cost per use case will be seen.

### 3.5 Risk adjustment and option value

Show unadjusted and risk-adjusted benefit; state the adjustment (for example, "the high case assumes 90% of
engagements adopt in the first season; the low case assumes 60%"). Report options the work unlocks
(a reusable component, a new service) separately, never inside base benefit [FORRESTER-TEI]. Report
intangibles as intangibles rather than forcing them into money [ROIINST-2014].

### 3.6 Proof design

- **Comparison**: a parallel run on the same items, a staggered start, or a comparison group. Without one,
  say the result cannot isolate the effect of the change [ROIINST-2014; NBER-BRYNJOLFSSON-2023].
- **KPIs**: three to five, leading and lagging, each efficiency measure paired with a quality guardrail.
  Companies measuring AI against growth outcomes reported strong ROI more often than those measuring
  efficiency alone (35% versus 13%; association, self-reported) [WHARTON-2026].
- **Horizon**: measured gains can lag the investment [NBER-JCURVE-2020]; state when financial signal is
  expected and what leading indicators show progress before then.
- **Go/no-go**: criteria for the pilot, set before it starts [GARTNER-CSO-2026].

### 3.7 Portfolio view (unit and organization scope)

Write a bridge from today's cost, hours or margin to the target: one bar per initiative, each with
baseline, target range, owner and quarter [BDEMERSON-2026]. Keep overlaps visible and check that no two units
bank the same capacity. Keep AI-attributable benefit and AI run cost in their own lines [BAIN-TECH-2026].
Ask what format the organization requires at this spend level.

## 4. Question bank

Tags: **[T]** team, **[U/O]** unit or organization. Core questions first.

**Core**
- What did this cost last month or last cycle: hours, volume, rework, outside spend? Where is that recorded? [T][U/O]
- If this saves time, where will that time go, and who decides? [T][U/O]
- After someone checks and corrects the output, how much time is really saved? [T]
- What would a skeptical finance lead need to see to believe the low case? [U/O]
- How will we know in 90 days whether it worked? [T][U/O]

**Follow-ups**
- What are we comparing against: the same items done the old way, another team, or an estimate? [T][U/O]
- Which of the benefits are about quality, speed to client or risk rather than hours? [T][U/O]
- What do we pay outside firms for today that this could replace? [U/O]
- Who uses this: new joiners, experienced staff, or both? Do they gain the same? [T]
- What could go wrong, and who would notice first? [T]
- Is any saving in this case already proven, or still expected? [U/O]
- What costs come with it: licences, set-up, checking, training, upkeep? [T][U/O]
- Which other initiatives claim the same benefit? [U/O] *Scaling*
- If revenue is part of it: what is the mechanism, a new price, a new service or more clients? [U/O] *AI-native*

## 5. Expert moves

1. **"Who owns the freed hours, and what is the next unit of work they will do?"** before valuing time [GARTNER-HR-2025].
2. **Three buckets** for every hours claim: absorbed, redeployed, cashable (§3.2).
3. **Net, not gross**: subtract review and rework; sample observed tasks instead of trusting recall [WORKDAY-2026; METR-2025].
4. **External spend first** when asked "where is the money": outsourced work, agencies, co-source. MIT's
   interviews describe savings coming from reduced outside spend rather than workforce cuts (self-reported,
   anonymized) [MIT-NANDA-2025].
5. **Check reinvestment before promising headcount savings**: of EY's respondents with gains, 17% said they
   led to reduced headcount (self-reported) [EY-2025].
6. **Realized or expected?** Mark every saving one or the other; bank only realized savings.
7. **Ask who paid for any study** a user quotes; commissioned studies are labelled as such [FORRESTER-TEI].
8. **Read the definition before quoting a headline**: MIT NANDA's "95% get zero return" rests on interviews
   the authors call directional [MIT-NANDA-2025].
9. **Bridge with names attached**: no single bar should carry the whole case [BDEMERSON-2026].
10. **Proof points, not strategy**: "What has actually changed in a metric, and over what period?" [BAIN-TECH-2026]

## 6. Common traps

| Trap | How the advisor avoids it |
|---|---|
| **Hours × rate = savings** | Three buckets; only cashable carries money as cost |
| **Single-point ROI** | Low and high cases with named assumptions; payback as a range |
| **Trusting self-reported time** | Observed samples, parallel runs, timestamps |
| **Ignoring rework and review time** | Net hours; a reviewer-time line in the cost stack |
| **Averages across mixed users** | Segment by experience and task type [NBER-BRYNJOLFSSON-2023] |
| **Costing only licences** | Full cost stack and a consumption assumption |
| **Vendor numbers as independent** | Provenance next to every figure; vendor claims stay grade C |
| **Headcount savings on potential** | Mark realized versus expected; see `people-and-change.md` |
| **Measuring too early** | State horizon and leading indicators |
| **Leaving out quality and risk** | A value line for each weighted lever, with its metric |

## 7. Worked example: evidence matching

One-page case for `ct-07` in the audit partner's practice (continuing `prioritize.md`). Numbers are
**illustrative** unless a source is named.

- **Decision asked:** use the firm's evidence-matching tool on every controls-reliance engagement this
  season, after a five-engagement check.
- **Today:** about 30 engagements rely on controls; sample-to-evidence matching takes 50–80 hours each in
  last season's time records, so 1,500–2,400 hours. Review is the bottleneck (Diagnose).
- **Future:** `automate` / `step`. The tool matches client documents to selected samples and links each
  value to its source; the auditor works every mismatch; the reviewer re-performs a sample of matches.
- **Evidence:** `assurance-controls-testing-07`, grade B: one firm reports 16 hours falling to 5–6 hours per
  engagement and another about half the time on invoice samples (both self-reported, mostly substantive
  testing); PwC says its overall year-one AI savings in assurance are "not that drastic yet" (archetype module). No independent measure of
  test quality exists.

| Lever | Metric | Low | High | Unit | Assumptions |
|---|---|---|---|---|---|
| capacity | Net staff hours released | 180 | 1190 | hours/season | Saving 40–65% of matching hours; added review 10–20% of baseline; 60–90% of engagements use it in season 1 |
| quality | Review notes on missing or wrong evidence per file | 10 | 30 | % fewer | Every value links to its source; checklist F1 in use; compared with last season |
| risk | Files where every tested attribute links to its evidence | 85 | 100 | % of files | Tool, version, criteria, output and reviewer's work recorded in the file |
| experience | Senior staff overtime in the season | 5 | 20 | % fewer | Part of the released hours lands with seniors, not only juniors |

- **Where freed capacity goes:** about a quarter absorbed (learning, ad hoc); the rest redeployed to the
  practice's staff gaps and to earlier risk work, in line with the Frame capacity stance; contractor hours
  in the season may fall. `capacity_use`: redeploy. No roles reduced.
- **Cost (season 1):** licences already held (check the overlay catalogue); training 2 hours × 40 staff;
  checklist and documentation note 60–100 hours; re-performance on the first five engagements 60–120 hours;
  reviewer time is already netted out of the capacity line.
- **Go/no-go after five engagements:** re-performed matches agree; review notes per file not higher than
  last season; net hours at or above the low case.
- **Risks and checkpoints:** matches accepted without review (track re-performance results and override
  rate); clients ask for lower fixed fees once savings show (decide the fee stance before the season); 31% of
  IFIAR member regulators reported finding audit tools "not used as intended" (2024, cited in the module),
  so write down how the tool is to be used. Checkpoints: the auditor signs off every exception and the
  test; the reviewer re-performs a sample.
- **Role evolution:** tasks moving: vouching documents to samples, a junior training task. New work:
  investigating mismatches, earlier risk work. Juniors keep learning through explain-back on a sample of
  matches (see `people-and-change.md`).
- **Assumptions to test first:** matching hours per engagement (time records), added review time, and the
  share of engagements where client documents are readable by the tool.

## 8. Output

In `opportunities.yaml`, complete for each top opportunity: `value` (one entry per lever: `lever`, `low`,
`high`, `unit`, `assumptions`), `risks`, `human_checkpoints`, `role_evolution` (`tasks_moving`,
`new_work`, `capacity_use`), `evidence` and `next_step`. Re-score if the case changed an input.

In `transformation-plan.md`, under the Make the case section, one page per top opportunity using these
headings: Decision asked · Today (baseline and sources) · Future (`ladder`, `change_scope`) · Value
(table as in §7) · Where freed capacity goes · Cost · Risks and human checkpoints · Role evolution ·
Evidence (ids, grades, provenance) · How we will know (comparison, KPIs, horizon, go/no-go) · Assumptions
to test first. At higher levels add the portfolio bridge, and draft the leadership summary as a section
that can be pasted elsewhere. Set `phase_completed: 6`, `next_phase: 7`, `updated`.

## 9. Sources

- `BAIN-TECH-2026` — Bain & Company, *Software investing in the age of AI* (Technology Report 2026), consultancy, 2026-09-29. https://www.bain.com/insights/software-investing-in-the-age-of-ai-and-slower-growth-technology-report-2026/
- `BDEMERSON-2026` — BD Emerson, *Private equity value creation plan*, practitioner article, 2026-08-16. https://www.bdemerson.com/article/private-equity-value-creation-plan
- `EY-2025` — EY, *US AI Pulse: productivity fueling reinvestment over workforce reductions* (n=500), survey release, 2025-12-09. https://www.ey.com/en_us/newsroom/2025/12/ai-driven-productivity-is-fueling-reinvestment-over-workforce-reductions
- `FINOPS-2026` — FinOps Foundation, *Token economics: the atomic unit of AI value*, practitioner body, 2026-05-10. https://finops.org/insights/token-economics-the-atomic-unit-of-ai-value/
- `FORRESTER-TEI` — Forrester, *Total Economic Impact methodology*, method page, updated 2024-10-31. https://www.forrester.com/policies/tei
- `GARTNER-CSO-2026` — Gartner, *31% of chief sales officers cited difficulty proving ROI of AI-driven tools* (Q&A), analyst, 2026-05-19. https://www.gartner.com/en/newsroom/press-releases/2026-05-19-gartner-survey-shows-thirty-one-percent-of-chief-sales-officers-cited-difficulty-proving-roi-of-ai-driven-tools-as-a-top-challenge-for-sales-objectives-in-two-thousand-twenty-si
- `GARTNER-HR-2025` — Gartner, *88% of HR leaders say their organizations have not realized significant business value from AI tools*, analyst survey release, 2025-10-28. https://www.gartner.com/en/newsroom/press-releases/2025-10-28-gartner-survey-shows-88-percent-of-hr-leaders-say-their-organizations-have-not-realized-significant-business-value-from-ai-tools
- `HDR-AIE` — Hubbard Decision Research, *Applied Information Economics*, method page, 2013-12-26 (updated 2026-01-20). https://hubbardresearch.com/applied-information-economics/
- `KPMG-2026` — KPMG US, *AI Quarterly Pulse Q2 2026*, survey release, 2026-06-24. https://www.kpmg.com/us/en/media/news/q2-ai-pulse-2026.html
- `LEI-PEPERKAMP-2026` — Lean Enterprise Institute, *Lean in the age of AI*, 2026-02-18. https://www.lean.org/the-lean-post/articles/lean-in-the-age-of-ai-optimizing-the-stream-not-the-coder/
- `METR-2025` — METR, *Impact of early-2025 AI on experienced open-source developer productivity*, RCT, 2025-07. https://arxiv.org/abs/2507.09089
- `MIT-NANDA-2025` — MIT NANDA, *The GenAI divide* (preliminary, interview-based), 2025-07. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `NBER-ACEMOGLU-2024` — D. Acemoglu, *The simple macroeconomics of AI* (NBER WP 32487), 2024-05. https://www.nber.org/papers/w32487
- `NBER-BRYNJOLFSSON-2023` — Brynjolfsson, Li, Raymond, *Generative AI at work* (NBER WP 31161), 2023-11. https://www.nber.org/papers/w31161
- `NBER-JCURVE-2020` — Brynjolfsson, Rock, Syverson, *The productivity J-curve* (NBER WP 25148), 2020-01. https://www.nber.org/papers/w25148
- `ROIINST-2014` — ROI Institute, *Comparison of Kirkpatrick and Phillips evaluation frameworks*, method paper, 2014. https://roiinstitute.net/wp-content/uploads/2017/10/Comparison-of-Kirkpatrick-and-Phillips-1.pdf
- `UKDBT-2025` — UK Department for Business and Trade, *Evaluation of the M365 Copilot pilot*, government evaluation, 2025-08. https://assets.publishing.service.gov.uk/media/68adbe409e1cebdd2c96a19d/dbt-microsoft-365-copilot-evaluation.pdf
- `UKGDS-2025` — UK Government Digital Service, *Microsoft 365 Copilot experiment: cross-government findings*, 2025-06-02. https://www.gov.uk/government/publications/microsoft-365-copilot-experiment-cross-government-findings-report
- `WHARTON-2026` — Wharton Human-AI Research and GBK Collective, *2026 AI adoption report*, survey, 2026-10-13. https://knowledge.wharton.upenn.edu/special-report/2026-ai-adoption-report/
- `WORKDAY-2026` — Workday, *Companies are leaving AI gains on the table* (n=3,200), vendor survey release, 2026-01-14. https://en-hk.newsroom.workday.com/2026-01-14-New-Workday-Research-Companies-Are-Leaving-AI-Gains-on-the-Table
- Archetype evidence: `../archetypes/assurance/modules/controls-testing.md` and its use-case YAML.

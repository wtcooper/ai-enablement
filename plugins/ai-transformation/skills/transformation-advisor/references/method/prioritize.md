# Prioritize (phase 5)

Read this on entering phase 5. It tells you how to screen, score and sort the Reimagine options into quick
win, foundation, big bet or park, how to sequence them, and what to write. Scoring uses the plan's
`settings` (value levers and weights), which default to the values in §3.1. Keys in brackets are listed in §9.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Levers, scores and categories](#3-levers-scores-and-categories)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example: controls testing](#7-worked-example-controls-testing)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** Turn the option list into a ranked, sequenced portfolio the user believes, with the reasons
visible. At unit or organization scope, this phase also **rolls up** the child units' opportunities (§2,
step 8). Treat the scoring as a facilitation device, not a validated model: no published study we found
tests whether impact-versus-feasibility scoring predicts results; vendor guides such as [MSFT-CAF-2026]
describe the method without testing it.

**Exit criteria.**

- Every option has passed the gates (§3.2) or is parked with the reason.
- Every scored option has a rough value range per lever (`low`, `high`, `unit`, `assumptions`). No range, no value score.
- Any evidence used in a score carries its evidence grade and the provenance of its figure (self-reported,
  vendor-published or independent).
- Six scores (1–5), a `weighted_score` and a `category` per option, using the plan's weights.
- A sequence that respects dependencies: foundations before what they unlock, and no more live initiatives
  than named owners and review capacity can carry.
- The two or three assumptions that would change the ranking are named.
- The user has chosen the top three to five opportunities for Make the case.

## 2. How to run it

1. **Name the phase.** "We are in Prioritize: deciding what to do first. Next we build the case for the top few."
2. **Confirm the settings.** Read `settings.value_levers` and `settings.scoring_weights` from the plan (set in
   Frame; a child unit inherits its parent's unless it overrides them). If empty, propose the defaults in
   §3.1, play them back and ask: "Is anything weighted wrongly for you?"
3. **Run the gates** (§3.2) on each option. Park the failures with a one-line reason.
4. **Size roughly, as ranges.** For each remaining option, per lever: low and high, the unit, and the main
   assumption. Use last month's actual volumes from Map, not a typical week.
5. **Score**, one dimension at a time across all options (scoring across, not down, keeps the anchors honest).
   Use the anchors in §3.3. Say what each score rests on.
6. **Compute and categorize** (§3.4). Show the table. Ask: "Does this order match your gut? Where not, why?"
   A disagreement usually exposes a missing lever or a wrong assumption; fix that, not the score.
7. **Sequence** (§3.5) and test sensitivity: which assumption, if it moved to its low case, would change the top three?
8. **Higher levels: roll up.** Use subagents for this step: delegate one subagent per child unit, in parallel,
   using the `rollup-unit` brief. If you cannot start subagents, do each unit yourself, one at a time. Then
   merge duplicates, find shared platforms and combine value along the value tree without double counting.
   Read `breakdown-and-rollup.md` for the method.
9. **Play back** the ranked list, the categories and the sequence, get the user's top three to five, write
   the output (§8) and update the plan state.

**Adapt by journey stage.** Curious: score lightly; pick two or three quick wins with existing tools.
Experimenting: favour a shared team workflow with a baseline over many individual tricks. Adopting: one or
two big bets with foundations in front of them. Scaling: weight reuse and shared platforms; compare units on
the same measures. AI-native: give new-service and pricing options a fair hearing; their proof standard is
different (§5, move 6).

## 3. Levers, scores and categories

### 3.1 Default value levers and weights

**Levers:** capacity, speed, quality, growth, cost, risk, experience. The top-level plan chooses and
weights them; each lever needs one named metric (for example: quality → share of workpapers returned by
review; risk → findings per inspection). In knowledge work, quality and risk are often the real value and
the levers most often left out of cases (advisor synthesis; compare the productivity skew in [GARTNER-CFO2-2026]).

| Scoring dimension | Default weight | Plain question to the user |
|---|---|---|
| Value | 0.30 | "How much would this move the things you care most about?" |
| Feasibility | 0.20 | "Could we do this with the tools, skills and approvals we have?" |
| Data readiness | 0.15 | "Is the information it needs digital, clean and reachable?" |
| Risk (higher score = lower risk) | 0.15 | "If it got something wrong, how bad and how reversible would that be?" |
| Time to value | 0.10 | "How soon would we see a result?" |
| Strategic fit | 0.10 | "How directly does this serve your main goal?" |

`weighted_score` = sum of weight × score. With weights that sum to 1, it stays on the 1–5 scale. Use the
plan's own weights if they differ.

### 3.2 Gates before scoring

| Gate | Test | If it fails |
|---|---|---|
| Should it exist? | "What would happen if this step stopped?" [LEI-ETHINGTON-2026] | Park the AI option; add "remove the step" as its own option |
| Rules | Breaks a rule in `SKILL.md`, a professional obligation or an overlay guardrail | Park; say which rule |
| Simpler fix | A rule, template or existing feature does the job | Replace with the simpler option |
| Constraint | Speeds a step that is not the bottleneck [TOCI-5FS; PEX-DUMAS-2025] | Cap value at 2 unless the bottleneck is also addressed |
| Stage | A `delegate` or `model` option at Curious or Experimenting | Park as a target picture; note what would bring it back (delegation gates in `onboarding.md`) |

### 3.3 Score anchors (advisor heuristic; 2 and 4 sit between)

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Value | Small or uncertain gain on a low-weight lever; low end of range near zero | Clear gain on one weighted lever; low end above zero | Large gain on a top-weighted lever or several levers, or a new revenue line |
| Feasibility | Unproven anywhere; needs skills, tools or integration the team lacks | Proven elsewhere (archetype grade A or B); some build or integration | Works with approved tools; the team can do it now |
| Data readiness | Not digital, scattered or inaccessible; criteria unwritten | Exists but needs clean-up or access | Clean, reachable, decision criteria written down |
| Risk | A wrong output reaches a client or regulator, is irreversible, or affects people decisions | Errors caught by a designed checkpoint; moderate consequence | Internal, reversible, low consequence |
| Time to value | Over 12 months | About 3–6 months | Within about 30 days |
| Strategic fit | Unrelated to stated goals | Supports one goal | Directly serves the main ambition |

Value scores rest on the range, not on hours alone: hours released are not value realized until the
capacity has a destination (see `business-case.md`).

### 3.4 Category rules (apply in order; advisor heuristic)

The quick win, foundation, big bet split is a practitioner convention. The sources support the ideas
behind it (productivity cases plateau; foundations such as data and platforms matter; new-value cases need
a different proof standard) but none defines this exact split [GARTNER-CFO2-2026; BCG-GAP-2025].

1. **Park** if it failed a gate. Record a "revisit when" trigger.
2. **Foundation**: two or more other options depend on it (written criteria, data access, an evaluation set,
   a shared platform, a policy), whatever its own value score.
3. **Park** if `weighted_score` is below 2.5 or value is 2 or less.
4. **Quick win**: `weighted_score` 3.0 or more, with feasibility, data readiness and time to value all 4 or
   more, and risk 3 or more. Usually `assist` or `augment` at `step` scope.
5. **Big bet**: value 4 or more, with feasibility, data readiness or time to value at 3 or less; or
   `change_scope: model`; or a `delegate` option at Adopting. Needs a staged plan and its own proof standard.
6. **Everything else**: park, with the foundation or result that would bring it back.

### 3.5 Sequencing rules

- Foundations start first, alongside one or two quick wins that build confidence and evidence.
- Big bets start in shadow mode once their foundations are in place (see `plan-and-control.md`).
- No more live initiatives than named owners; check the shared constraint (often the same reviewers) and
  the team's change load [BAIN-MIDYEAR-2026; GT-2013].
- Reuse first: a use case proven in one team, or a component several options share, beats a new one-off
  [MCKINSEY-1YR-2025; DELOITTE-PE-2026].

## 4. Question bank

Tags: **[T]** team, **[U/O]** unit or organization. Core questions first.

**Core**
- Of capacity, speed, quality, growth, cost, risk and client experience, which two matter most this year? [T][U/O]
- If you could do only one of these, which would you back, and why? [T][U/O]
- What would have to be true for the top one to work? [T][U/O]
- Which of these depend on something we don't have yet: data, written rules, a tool, skills? [T][U/O]
- What would change your mind about this order? [T][U/O]

**Follow-ups**
- How many of these did the team finish last month, and how long did each take? [T]
- What does a mistake here cost: rework, a client complaint, a regulatory finding? [T]
- Is this step the one where work piles up, or the one before it? [T]
- Who would use this tomorrow: new joiners, experienced people, or both? [T] (gains differ by group [NBER-BRYNJOLFSSON-2023])
- Who has the time to own each of these? [T][U/O]
- Where do we pay outside firms today for work this could replace? [U/O] *Adopting+*
- Which of these ideas has worked somewhere else, and which would be a first? [U/O]
- Which units are trying to solve the same problem? Could they share the solution? [U/O] *Scaling*
- What share of this list is about doing the same work cheaper, and what share is about better decisions or new services? [U/O]

## 5. Expert moves

1. **Rank on the constraint.** Ask of each option: "Does this speed up the bottleneck, remove work, or just
   move it?" *Reveals:* local gains that create pile-ups [LEI-PEPERKAMP-2026; TOCI-5FS].
2. **Exploit and subordinate before you elevate.** Cheap changes to how the bottleneck is used come before
   buying tools or adding people [TOCI-5FS].
3. **Ask for unit economics first.** "What does one item cost to serve today, and how many a month?"
   *Reveals:* whether the ranking can be grounded at all [MITTR-DELOITTE-2026].
4. **Value of information.** "Which two or three assumptions, if wrong, would change the order?" Test those
   first; don't measure everything [HDR-AIE].
5. **Segment, don't average.** Gains concentrate in some groups: in one customer-support study, 14% more
   issues resolved per hour on average, 34% for novices, minimal for experienced staff (independent)
   [NBER-BRYNJOLFSSON-2023].
6. **Classify and set the proof standard.** Individual productivity, business automation or new value.
   Don't judge a new-service bet by a productivity yardstick. In Gartner's finance survey, functions investing in
   "Upend" initiatives (new value propositions, products or markets) were more than twice as likely to report
   high realized value (self-reported) [GARTNER-CFO2-2026; MSFT-CAF-2026].
7. **Concentrate.** If the long list has more than a handful of items, push for a few end-to-end
   workflows. BCG reports 62% of initiatives deployed at "future-built" firms against 12% at laggards
   (self-reported) [BCG-GAP-2025].
8. **Narrow first, then the core.** Start at the edge of a workflow with a narrow, simple task; MIT's
   interviews found these were the fast wins (directional) [MIT-NANDA-2025].
9. **Trial before scale.** Test the top candidates on a handful of real cases and compare measured with felt
   effect; experienced developers in one trial believed they were 20% faster while taking 19% longer
   (independent) [METR-2025].
10. **Reuse case.** List the building blocks (ingest, extract, search, analyze) that several options share,
    and rank shared components up [MCKINSEY-1YR-2025].
11. **Finance-signed case before production.** Ask who signs off the expected return and who owns the
    business result. One technology company requires sign-off by the finance partner and the business-unit
    head before anything reaches production [DELOITTE-TT-2025].

## 6. Common traps

| Trap | How the advisor avoids it |
|---|---|
| **Ranking on hours saved alone** | Require a range per lever and a capacity destination; quality and risk count |
| **Single-point values** | Low and high with assumptions, always (rule 3 in `SKILL.md`) |
| **Treating the matrix as truth** | Say it is a facilitation device; let disagreement expose missing levers |
| **Efficiency-only portfolio** | Check the mix; add a quality, risk or growth option. In Gartner's survey of 204 finance leaders, 45% of finance AI investment leaned to productivity and 20% to decision quality (self-reported) [GARTNER-CFO2-2026] |
| **Pilot sprawl** | Cap live initiatives at owner and review capacity; park with triggers |
| **Unquoted provenance** | Every figure used in a score carries who measured it; vendor claims stay grade C |
| **Headline statistics without definitions** | Ask what a "95% fail" or "97% positive ROI" figure measured and who answered before using it [MIT-NANDA-2025] |
| **Double counting at roll-up** | Two units cannot both bank the same capacity or the same platform saving (`breakdown-and-rollup.md`) |

## 7. Worked example: controls testing

Continuing the audit partner's practice from `reimagine.md`. The practice set its weights in Frame: value
0.30, feasibility 0.20, data readiness 0.15, risk 0.20, time to value 0.05, strategic fit 0.10. Scores are
illustrative; evidence ids are from `../archetypes/assurance/use-cases/controls-testing.yaml`.

| Option | V | F | D | R | T | S | Weighted | Category |
|---|---|---|---|---|---|---|---|---|
| F1 Standard review checklist and attribute templates for the ten most common control types | 2 | 5 | 4 | 5 | 4 | 4 | 3.80 | foundation (`ct-07`, `ct-10`, `ct-08` depend on it) |
| Rewrite evidence-request templates for the top chase reasons (no AI) | 3 | 5 | 5 | 5 | 5 | 3 | 4.20 | quick win |
| Roll forward unchanged walkthroughs (no AI) | 3 | 5 | 5 | 4 | 5 | 3 | 4.00 | quick win |
| `ct-07` Evidence matching on every engagement (`#07`, grade B) | 4 | 4 | 4 | 4 | 4 | 4 | 4.00 | quick win |
| `ct-10` AI secondary review before the manager (`#10`, grade B) | 3 | 4 | 4 | 4 | 5 | 4 | 3.75 | quick win (after F1) |
| `ct-08` Full-population test of one transactional control (`#08`, grade A) | 4 | 3 | 2 | 3 | 3 | 4 | 3.25 | big bet |
| `ct-01` Walkthrough drafting with change flags (`#01`, grade B) | 3 | 4 | 3 | 4 | 4 | 3 | 3.45 | park: revisit once roll-forward shows what is left |
| `ct-03` Agent pre-checks evidence submissions (`#03`, grade C) | 3 | 3 | 3 | 4 | 3 | 3 | 3.20 | park: revisit if chasing stays high after the template rewrite |
| `ct-16` Platform agent tests a control set (`#16`) | — | — | — | — | — | — | — | park: stage gate; target picture until delegation gates hold |
| `ct-20` Controls work sold as platform plus review (`#20`) | — | — | — | — | — | — | — | park: stage gate; revisit at the mid-point review |

*Ranges behind the value scores (illustrative):* `ct-07` capacity 180–1,190 net hours in the first season
(see `business-case.md` for the arithmetic). One firm self-reports 16 hours falling to 5–6 hours per
engagement, mostly on substantive testing; PwC says its overall year-one AI savings in assurance are "not that
drastic yet". `ct-10` quality 10–30% fewer review notes on missing evidence (illustrative; no published
measure yet; grade B, qualitative).
*Assumptions that would change the order:* matching hours per engagement in the time records; added review
time per engagement; and whether clients ask for lower fixed fees once savings are visible.

*Sequence:* F1, the template rewrite and the roll-forward start now; `ct-07` runs on the next five engagements with a
re-performed sample, then on all; `ct-10` follows F1; `ct-08` is planned for one client with clean data next
season; the parked delegate and model options come back at the quarterly review once `ct-07` is owned and
measured.

## 8. Output

In `opportunities.yaml`, for each item add or update:

```yaml
  value:
    - { lever: capacity, low: 180, high: 1190, unit: hours/season, assumptions: "1,500-2,400 h matching today; saving 40-65%; added review 10-20%; 60-90% of engagements in season 1" }
  scores: { value: 4, feasibility: 4, data_readiness: 4, risk: 4, time_to_value: 4, strategic_fit: 4 }
  weighted_score: 4.00
  category: quick-win
  prerequisites: [F1 standard review checklist]
  next_step: { action: "Run on the next five engagements and re-perform a sample of matches", owner: "Audit manager (pilot lead)", depends_on: "Review checklist F1 drafted; baseline hours recorded" }
```

Use lever ids from the vocabulary (`capacity`, `speed`, `quality`, `growth`, `cost`, `risk`,
`experience`). Parked items keep their reason in `description` or `risks`.

In `transformation-plan.md`: confirm `settings.value_levers` (`id`, `name`, `metric`, `weight`) and
`settings.scoring_weights`; under the Prioritize section, write the ranked table, categories, the sequence
with dependencies, the assumptions that would change the order, and the user's chosen top three to five. At
higher levels, add the roll-up summary and set `rolled_up_from` on merged items. Set `phase_completed: 5`,
`next_phase: 6`, `updated`.

## 9. Sources

- `BAIN-MIDYEAR-2026` — Bain & Company, *Private equity midyear report 2026*, consultancy, 2026-06-08. https://www.bain.com/insights/private-equity-midyear-report-2026/
- `BCG-GAP-2025` — BCG, *The widening AI value gap* (n=1,250), consultancy survey, 2025-09. https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf
- `DELOITTE-PE-2026` — Deloitte, *Raising the game: PE operating partners and CFOs*, consultancy, 2026-04. https://www.deloitte.com/content/dam/assets-shared/docs/industries/financial-services/2026/raising-the-game.pdf
- `DELOITTE-TT-2025` — Deloitte Insights, *The agentic reality check*, consultancy, 2025-12-10. https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
- `GARTNER-CFO2-2026` — Gartner, *45% of CFOs say AI investments lean toward productivity*, analyst survey release, 2026-07-20. https://www.gartner.com/en/newsroom/press-releases/2026-07-20-gartner-survey-shows-45-percent-of-cfos-say-their-ai-investments-lean-towwards-productivity-while-20-percent-say-these-investments-lean-towards-decision-quality
- `GT-2013` — Grant Thornton with PitchBook, *What can be done in 100 days?*, consultancy survey, 2013-10. https://www.grantthornton.in/globalassets/1.-member-firms/india/assets/pdfs/pe-100-day-plan-survey-what-can-be-done.pdf
- `HDR-AIE` — Hubbard Decision Research, *Applied Information Economics*, method page, 2013-12-26 (updated 2026-01-20). https://hubbardresearch.com/applied-information-economics/
- `LEI-ETHINGTON-2026` — Lean Enterprise Institute, *Automation, AI, and the risk of doing things efficiently that should not be done at all*, 2026-03-05. https://www.lean.org/the-lean-post/articles/automation-ai-and-the-risk-of-doing-things-efficiently-that-should-not-be-done-at-all/
- `LEI-PEPERKAMP-2026` — Lean Enterprise Institute, *Lean in the age of AI*, 2026-02-18. https://www.lean.org/the-lean-post/articles/lean-in-the-age-of-ai-optimizing-the-stream-not-the-coder/
- `MCKINSEY-1YR-2025` — McKinsey, *One year of agentic AI: six lessons*, consultancy, 2025-09-12. https://www.mckinsey.com/capabilities/quantumblack/our-insights/one-year-of-agentic-ai-six-lessons-from-the-people-doing-the-work
- `METR-2025` — METR, *Impact of early-2025 AI on experienced open-source developer productivity*, RCT, 2025-07. https://arxiv.org/abs/2507.09089
- `MIT-NANDA-2025` — MIT NANDA, *The GenAI divide* (preliminary, interview-based), 2025-07. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `MITTR-DELOITTE-2026` — MIT Technology Review Insights with Deloitte, *Enabling agent-first process redesign*, sponsored content, 2026-04-07. https://technologyreview.com/2026/04/07/1134966/enabling-agent-first-process-redesign
- `MSFT-CAF-2026` — Microsoft Learn, *Plan for AI adoption: prioritize AI use cases*, vendor guidance, updated 2026-10-15. https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/plan
- `NBER-BRYNJOLFSSON-2023` — Brynjolfsson, Li, Raymond, *Generative AI at work* (NBER WP 31161), 2023-11. https://www.nber.org/papers/w31161
- `PEX-DUMAS-2025` — M. Dumas, *Process intelligence: the foundation of agentic AI success*, PEX Network, 2025-02-04. https://www.processexcellencenetwork.com/ai/articles/process-intelligence-agentic-ai/amp
- `TOCI-5FS` — Theory of Constraints Institute, *Five focusing steps*, practitioner guide, © 2021 (accessed 2026-10-16). https://www.tocinstitute.org/five-focusing-steps.html
- Archetype evidence: `../archetypes/assurance/modules/controls-testing.md` and its use-case YAML.

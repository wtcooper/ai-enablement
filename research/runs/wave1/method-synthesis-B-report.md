# Method synthesis B: report

Stream M synthesis, editor B. Date: 2026-10-16.
Brief: `research/briefs/templates/method-synthesis.md`.
Inputs: the eight `research/runs/wave1/method-*.md` topic files, the spec (§3, §4, §6.1–6.7, §9), and the
assurance controls-testing module and YAML (worked examples).

## Files written

All are in `plugins/transformation-advisor/skills/transformation-advisor/references/method/`.

| File | Lines | Notes |
|---|---|---|
| `reimagine.md` | 267 | Four lenses mapped to `ladder` and `change_scope`; fit checks; the AI-native competitor move, flagged as thin evidence |
| `prioritize.md` | 273 | Default levers and weights (spec §6.6), gates, 1–5 anchors, category and sequencing rules, roll-up hook |
| `business-case.md` | 265 | Value tree, hours → value (absorbed / redeployed / cashable), ranges, cost stack, proof design, portfolio bridge |
| `plan-and-control.md` | 253 | Start this week + 30/60/90, 100-day plan / value creation plan / cadence, control plans for human and agent steps |
| `people-and-change.md` | 265 | Spec §9 rules 1, 2 and 8 made concrete; job-impact evidence, role evolution, redeploy vs reduce, junior pipeline, communication, fear script |
| `index.md` | 18 | One table covering all eleven method files, linked by relative filename |

`python3 scripts/validate.py`: 0 errors. One warning, outside my files: `SKILL.md` does not exist yet (M2).
Every key used in a file body is listed in that file's sources, and every listed key is used.

## Which inputs fed each file

| File | Main inputs | Supporting inputs |
|---|---|---|
| reimagine | agentic-redesign (lenses, zero-based design, complexity ladder, agent-readiness, AI-native competitor move, multi-agent cautions) | transformation-evidence (workflow redesign evidence, jagged frontier, WORKBank zones); lean-six-sigma (should-it-exist, constraint and queue logic, redesign heuristics); pe-value-creation (Bain revolution / transformation / augmentation sort, outside-in prototype); ai-maturity (stage adaptation, delegation timing); change-workforce (lens → workforce consequence) |
| prioritize | value-measurement (levers, scoring approach, use-case classes, value of information, concentration) | lean-six-sigma (constraint and five focusing steps); pe-value-creation (concentrate, reuse first, owner capacity); transformation-evidence (narrow first, trial before scale, BCG and Gartner portfolio data); agentic-redesign (unit economics, reuse case, agent washing) |
| business-case | value-measurement (hours vs value, net time, three buckets, ranges, isolation, cost stack, TEI, J-curve, headline-statistic cautions) | pe-value-creation (bridge, separate AI ledger, proof points); change-workforce (realized vs expected, new work); transformation-evidence (ROI conflicts across surveys) |
| plan-and-control | agentic-redesign (autonomy tiers, checkpoint types, escalation, override rates, evals, tracing, security, governance tiers); pe-value-creation (100-day plan, cadence, quarterly value review, mid-point reset, forcing-function substitutes) | lean-six-sigma (baseline, control plan, control charts, standard work, staged rollout); value-measurement (KPIs, realized vs expected); ai-maturity (plan to the next stage, ICAEW governance screen, leading indicators) |
| people-and-change | change-workforce (nearly all of it) | value-measurement (EY reinvestment, external spend); agentic-redesign (WORKBank human agency scale); lean-six-sigma (lean heard as headcount cuts); discovery-interviewing (stigma, normalizing hidden use) |
| index | all | — |

discovery-interviewing mainly feeds `interviewing.md` (the other editor's). In my files it shaped the
question wording (recent concrete instances, records over recall, normalizing hidden use) and the
verification-burden probes.

## Conflicts resolved

1. **Delegation at Adopting.** Spec §3.2 puts "first delegated workflows" at Adopting. The ai-maturity and
   transformation-evidence inputs put agents after data foundations and governance.
   - Resolution: at Adopting, delegate only bounded, low-risk outcomes with checkpoints and a control plan.
     At Curious and Experimenting, delegate and model options are a target picture only.
   - This matches the other editor's five-gate decision in `onboarding.md`. Prioritize enforces it with a
     "stage" gate that parks such options with a trigger to bring them back.
2. **Capacity framings.** Three versions existed:
   - change-workforce: redeploy, absorb through attrition and hiring pace, or reduce;
   - value-measurement: absorbed, redeployed or cashable;
   - spec rule 2: redeploy versus reduce.

   Resolution: business-case sizes value with absorbed / redeployed / cashable. "Absorbed" is leakage, not a
   choice. people-and-change records the decision in `capacity_use` as `redeploy` or `reduce` (or both,
   with the split). Attrition and slower hiring count as `reduce`, with a mandatory junior-pipeline check.
3. **Workday rework figure.** value-measurement read the press release ("nearly 40%"); lean-six-sigma read
   trade coverage ("about 37%"). I used the primary release's "nearly 40%", labelled vendor-published.
4. **Gartner's "over 40% of agentic projects cancelled".** Two inputs read the release in full; one saw it
   only in search results. I used it as a forecast, with the primary URL.
5. **McKinsey State of AI 2025.** One input read it through a third-party copy; two saw it only in search
   results. I used only the 55% versus 20% redesign figure, from the copy that was read, as self-reported and
   correlational.
6. **Multi-agent designs.** Anthropic reports gains; Cognition argues against them; the MAST failure study
   finds design faults. Resolution: default to a single agent and justify each step up the complexity ladder.
7. **Scoring.** Spec weights are used as defaults. value-measurement found no scoring framework with tested
   predictive validity, and no evidence base for the quick win / foundation / big bet split.
   - The file presents scoring as a facilitation device. Anchors and category thresholds are labelled
     advisor heuristics.
   - Foundations are tested before the low-value park rule, so a low-value foundation is not parked.
8. **MIT NANDA "95%".** The report's definitions conflict internally. It is quoted only with its definition,
   and as an example of reading a headline before quoting it.
9. **Lens 4 → `change_scope`.** "A process that stops existing" was ambiguous. Rule:
   - record `model` when the service, pricing, sourcing or who does the work changes;
   - otherwise record `process`, and write "reinvent" in the description.
10. **Running worked example.** I first drafted around an internal-audit SOX team. The other editor's files
    follow an audit partner's regional practice (stage Experimenting; risk weight 0.20, time to value 0.05;
    review is the bottleneck). I realigned all four phase examples to continue that story:
    - Reimagine uses `diagnose.md`'s shortlist.
    - The Prioritize example uses Frame's weights; the defaults are stated in §3.1.
11. **Weak or untraceable claims excluded or labelled.**
    - "70% of change programmes fail" is excluded as untraceable, and the file says why.
    - HBR (Davenport 2026) is used for direction only, marked "summary only".
    - The eval-set size of 20–30 cases is labelled a heuristic.
    - Kotter's steps are flagged as coming from a secondary source.

**Source-key normalization.** Same sources, different keys in the inputs:

| My key | Input keys |
|---|---|
| MCKINSEY-SOAI-2025 | MCKINSEY-STATEOFAI-2025 |
| BCG-GAP-2025 | BCG-VALUEGAP-2025, BCG-2025 |
| DELOITTE-PE-2026 | DELOITTE-2026 (PE file) |
| GARTNER-AGENTIC-2025 | GARTNER-2025 (agentic file) |
| EY-2025 | EY-AIPULSE-DEC-2025 |
| WHARTON-2026 | WHARTON-GBK-2026 |
| KLARNA-2025 | KLARNA-ENTREPRENEUR-2025 |
| ACCENTURE-2025 | ACCENTURE-BI-2025 |
| PROSCI-2026 | PROSCI-ENTERPRISE-2026 |
| PROSCI-ADKAR | PROSCI-ADKAR-2026 |
| KOTTER-1995 | KOTTER-HBR-1995 |
| BRIDGES-ND | BRIDGES-TRANSITION-nd |
| TOCI-5FS | TOCI-5FS-ND |

The other editor uses BCG-VALUEGAP-2025 and MCKINSEY-STATEOFAI-2025. A later pass could harmonize the keys
across all method files.

## Gaps

- **AI-native competitor lens.** The evidence is thin: BCG and Roland Berger opinion, sponsored MIT
  Technology Review content, and Bain's diligence sort from a PE context. Searches on services-as-software
  and AI-native professional-services firms never ran. `reimagine.md` says so and labels outputs as
  hypotheses. Recommend a follow-up topic: AI-native service entrants, outcome pricing, and what clients
  accept as assurance of AI-produced work.
- **Human checkpoints.** No published override, error or parallel-run rates exist for checkpoints in
  knowledge work, so the files cannot give a "healthy override rate". They tell the advisor to set a
  baseline in the parallel run instead.
- **Redesign versus bolt-on.** No independent evidence compares the two. All support is consultancy
  survey data and correlational.
- **Scoring and categories.** No validated scoring framework exists. The thresholds need testing in evals.
- **Realized value in professional services.** No independent measurement exists. The worked-example
  numbers are illustrative and labelled so. A subject-matter reviewer should check them: for example, 50–80
  matching hours per engagement, and 30 controls-reliance engagements in a regional practice.
- **Cost.** No source gives a typical cost split (inference, platform, evaluation, change) for a
  knowledge-work use case. The FinOps 5–30x token multiplier is second-hand.
- **Benefit realization.** No AI-specific guidance from project-management bodies was found.
- **People side.** Several questions have no tested evidence:
  - which workforce messages reduce fear;
  - whether any apprenticeship redesign works;
  - how partner and middle-manager roles change.

  Two further limits:
  - career benefit from leading AI change is correlational only;
  - union and works-council consultation practice is not covered.
- **PE method transfer.** Transfer to non-PE units is untested. The cadence data is old: UK deals from
  1996–2004 and a 2013 survey.
- **Currency.** Wharton 2026 was published three days before this synthesis. Many figures are vendor-
  published or self-reported, and each is labelled in the files.

## Notes for coordination

- The other editor's `onboarding.md` and `breakdown-and-rollup.md` cite "the spec" and "spec §9 rule 2".
  The spec says build documents should not appear in the product. My files point to `SKILL.md` rules and
  `../schemas/` instead. Suggest the same edit there.
- My files assume `SKILL.md` will number the rules as in spec §9 ("rule 3 in `SKILL.md`"). If the
  short-form rules are renumbered, update those references.

## Suggested SKILL.md loop checklist (phases 4–7)

**4. Reimagine.** Read now: `method/reimagine.md`. Delegation: `scout-use-cases`, one subagent per
high-value step or unit, with an inline fallback.

Core questions:
1. What does this work exist to produce, and who uses it?
2. If we designed it today, simply, which steps would we keep?
3. Where could an assistant help the person doing it, and which items could go through untouched, with the
   odd ones sent to a person?
4. What would you hand over end to end if you could watch it and stop it?
5. If a new firm started this with AI, what would it not do, and what would it charge for?

Exit: all four lenses considered for each target. Each option carries `ladder`, `change_scope` and
evidence, or the label "idea". Fit checks passed, or the gap is recorded as a prerequisite. The user has
confirmed the list.

**5. Prioritize.** Read now: `method/prioritize.md`; at higher levels, also `breakdown-and-rollup.md`.
Delegation: `rollup-unit`, one subagent per child unit.

Core questions:
1. Which two of capacity, speed, quality, growth, cost, risk and client experience matter most this year?
2. For each idea, what are the low and high value, and what are they based on?
3. Which ideas depend on something we don't have yet?
4. If you could do only one, which would you back?
5. Which assumption, if wrong, would change the order?

Exit: gates run, ranges set, six scores and a weighted score, category, sequence, top three to five chosen.

**6. Make the case.** Read now: `method/business-case.md`, then `people-and-change.md` §2 and §5.
Optional delegation: `review-opportunities`.

Core questions:
1. What did this cost last month (hours, volume, rework, outside spend), and where is that recorded?
2. If it saves time, where does the time go: growth, quality, backlog, new services or lower cost? Who decides?
3. After checking and correcting, how much time is really saved?
4. What could go wrong, and where does a person check the work?
5. How will we know in 90 days whether it worked?

Exit: value ranges with assumptions and provenance; the three-bucket split; a cost stack; `role_evolution`
with `capacity_use`; checkpoints; a proof plan.

**7. Plan.** Read now: `method/plan-and-control.md`.

Core questions:
1. Who owns each item, and do they have the authority it needs?
2. What can start this week without anyone's approval?
3. What number would show it is slipping, and what happens then?
4. Who reviews the results, how often, and in which meeting?
5. What will you tell your people, and when?

Exit: a `next_step` for every item; a 30/60/90 plan, or a 100-day plan plus value creation plan and cadence;
control plans that include agent steps; KPIs with a quality guardrail; a people plan; the next stage with
three exit criteria.

**Cross-cutting pointer.** Place it near the rules: "If the user expresses fear about their role, read
`method/people-and-change.md` §8 before replying. If asked to choose or rate people, decline and redirect
to roles and capacity (§2)."

# Diagnose (phase 3)

Read this on entering Diagnose. It finds where value leaks: at team level waste, waiting, the constraint, variation
and rework, and how well each step suits AI; at unit or organization level an outside-in heatmap that decides which
units go first. Source keys in brackets are listed in §9. Tags: **[T]** individual or team, **[U/O]** unit or
organization, **[all]** any scope.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Quick analyses](#3-quick-analyses)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example](#7-worked-example)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** Know which few places, if changed, would move the levers set in Frame, and why. The central warning from
lean practice applies before any AI idea: do not automate waste, and do not speed up a step that is not the bottleneck
[LEI-ETHINGTON-2026; LEI-PEPERKAMP-2026; PEX-DUMAS-2025].

**Exit at team level [T]** when:
- The **constraint** is named: the step where work piles up and what the next step is starved of.
- **Waiting versus working** is known for the mapped processes (flow efficiency on real cases).
- **Rework and failure demand** are counted on a sample, with the top reasons.
- Steps are sorted into **value-creating, needed but not valued, and waste**, and any step that should stop is flagged.
- **Verification capacity** is understood: who checks work today, how long it takes, and whether more AI output would queue there.
- Each candidate step has its **AI-fit signals** (§2, step 8).
- A **shortlist of three to seven steps** goes to Reimagine, each with the finding behind it and a rough size.

**Exit at unit or organization level [U/O]** when:
- Every unit has a **heatmap row** (size, work-type mix, AI exposure, strategic weight, readiness), with confidence and source of each score.
- **Waves** are chosen: which units are planned first and why, written into `units[].wave`.
- Shared constraints across units (one review team, one system, one scarce specialist) are noted.

## 2. How to run it

**Team level [T]**
1. **Waiting versus working.** From the Map numbers, compute flow efficiency on five to ten real cases (§3). Low
   numbers mean a faster "doing" step will help little.
2. **Find the constraint.** Ask where work piles up and who after that point waits for it (D1, D3). Ask how booked the
   people at that step are, then use the queue rule (§3) to show what extra load would do.
3. **Ask for the oldest open item and why it is still open** (D2).
4. **Count rework.** Sample real cases and count those returned, reopened or touched more than once; ask the top three
   reasons (D4). Ask which incoming work exists only because something earlier went wrong (D5) [SEDDON-SWINSCOE-2020].
5. **Sort the steps.** For each step: does the customer value it, is it needed but not valued, or is it waste? Walk
   the eight wastes for what is left: defects, overproduction, waiting, unused talent, transport, inventory, motion,
   extra processing [LEI-7W-ND; PEX-DOWNTIME-2015]. Ask what would happen if a step stopped (D6).
6. **Check verification capacity.** Who checks the output today, how long, and what happens when it is wrong (D7)?
   Extra AI output in front of a fully booked reviewer lengthens the queue [LEI-PEPERKAMP-2026].
7. **Check existing AI use.** If a tool is already in use, compare what people say it saves with what timestamps and
   counts show (D8). Felt and measured gains can diverge sharply [METR-2025].
8. **Read the AI-fit signals for each candidate step:**
   - *Work type* (from Map) and *variance*: low-variance, standardized steps suit rules or a single model call;
     high-variance, judgment-heavy, unstructured steps are agent candidates [MCKINSEY-1YR-2025; OPENAI-GUIDE-2025].
   - *Desire and involvement:* what the people doing it want handed over, and how much involvement they want kept
     (D10); compare with what is technically feasible [STANFORD-WORKBANK-2026].
   - *Frontier test:* try two or three real samples with an available tool. AI is strong on some tasks and unreliable
     on similar-looking ones [HBS-JAGGED-2023].
   - *Readiness:* are the decision criteria written down with examples, can a tool reach the data, and would there be a
     record of what it did [BCG-AGENTS-2025]? Unstructured documents are a common blocker [BCG-GAP-2025].
9. **Size roughly:** volume × hands-on time, and the step's share of elapsed time (§3). Note the downstream constraint.
10. **Shortlist** three to seven steps, play the diagnosis back, and write it (§8).

**Unit or organization level [U/O]**
1. **Score each unit** on the five heatmap dimensions (§3) from Map data, the Frame exposure sort and archetype
   knowledge. Label each score as from data, from the user, or outside-in.
2. **Look for concentrations:** many people doing near-identical knowledge tasks is where savings concentrate
   [BAIN-DILIGENCE-2025]; units whose exposure differs enough to need separate plans [BCPARTNERS-2025].
3. **Choose waves.** Wave 1: high value and good readiness, plus at most one unit where exposure demands reinvention
   even if readiness is low. Do not spread effort evenly [BAIN-MIDYEAR-2026].
4. **Decide how each wave-1 unit will be planned** (delegate, the same user, or a desk review; see `breakdown-and-rollup.md`).

**By journey stage.** *Curious:* one process, the obvious waits and rework; skip heatmaps. *Experimenting:* full team
analysis on the shared workflow; baseline now. *Adopting and above:* all analyses, plus verification capacity and data
readiness for every candidate. *Scaling:* heatmap and waves across units; look for shared constraints and reusable components.

## 3. Quick analyses

| Analysis | How | What it tells you |
|---|---|---|
| **Flow efficiency** | Hands-on time ÷ elapsed time, per case, on five to ten real cases | Share of lead time spent working. Low values mean waiting dominates [KANBANU-LITTLE-2022] |
| **Stability check** | Are items arriving about as fast as they are finished? | If not, work in progress is quietly growing; lead-time estimates from averages will mislead [KANBANU-LITTLE-2022] |
| **Queue rule** | Waiting grows with utilization ÷ (1 − utilization), times variability, times service time. With variability factor 1: 50% booked → 1× the service time; 80% → 4×; 90% → 9×; 95% → 19× (computed from the formula) | Adding work to a step near full booking multiplies waiting [WIKI-KINGMAN-2025] |
| **Speed-up ceiling** | If a step is a share *s* of elapsed time and becomes *k* times faster, end-to-end time improves by at most *s* × (1 − 1/*k*). A step that is 10% of elapsed time, made twice as fast, gives at most 5% | Whether a step-level gain can matter at process level; also check the next step can absorb the output. Acemoglu applies the same share-times-saving logic to the whole economy [NBER-ACEMOGLU-2024] |
| **Rework rate** | Items returned, reopened or redone ÷ items finished, on a sample. Test the definition: two people classify the same ten items | The defects waste, and whether "rework" is measured consistently [WIKI-DMAIC-2025] |
| **Variation** | Plot cycle time over several weeks before reacting to one bad week | Chance variation versus a real change [NIST-CTRL-ND] |

**Unit heatmap (advisor scale, not a validated instrument).** Score 1–5; record confidence and source.

| Dimension | 1 | 5 |
|---|---|---|
| Size | Small share of the scope's people or hours | Largest share |
| Work-type mix | Mostly expert judgment and client interaction | Mostly review, processing, research, drafting and reporting, where patterns are strong |
| AI exposure | AI mainly helps | AI could threaten how the unit earns or justifies its budget (from the Frame sort) |
| Strategic weight | Little effect on the ambition and levers | Central to them |
| Readiness | No owner appetite, data hard to reach, heavy change load | Willing owner, AI already used, data reachable |

## 4. Question bank

Plain wording, one question at a time.

| # | Question | Scope | Stage note |
|---|---|---|---|
| D1 | Where does work sit longest? Who is waiting for whom? | [T] | All |
| D2 | What is the oldest open item right now, and why is it still open? | [T] | All |
| D3 | If this step were twice as fast, what would the next step see? | [all] | The constraint test |
| D4 | How often does work come back, and what were the last three reasons? | [all] | All |
| D5 | Which requests arrive only because something earlier was unclear or went wrong? | [all] | Service processes |
| D6 | What would happen if we stopped doing this step? Who would notice? | [T] | Ask before any automation idea |
| D7 | Who checks this work today, how long does it take, and what happens when it is wrong? | [T] | Adopting and above: ask for every candidate |
| D8 | Where AI is used already, what do people say it saves, and what do the dates and counts say? | [all] | Experimenting and above |
| D9 | How booked are the busiest people at the step where work piles up? What happens in a busy week? | [T] | All |
| D10 | Which of these tasks would your people gladly hand over, which would they share, and which must stay human? | [T] | All |
| D11 | Could we try two or three real examples of this step with a tool you already have? | [T] | Experimenting and above |
| D12 | Is the rule for this decision written down anywhere, with examples? | [T] | Before any automate or delegate idea |
| D13 | Where is the information this step needs, in what form, and who can grant access? | [all] | Adopting and above |
| D14 | Where do experts spend time on work that does not need them? | [U/O] | Unused talent |
| D15 | Which units run on the same scarce reviewer, system or specialist? | [U/O] | Shared constraints |
| D16 | Where are many people doing nearly the same knowledge task? | [U/O] | Savings concentrate there [BAIN-DILIGENCE-2025] |
| D17 | Which unit's owner is keen, which is wary, and which is already overloaded with change? | [U/O] | Readiness |

## 5. Expert moves

| Move | When | What it reveals |
|---|---|---|
| **Ask "should this step exist at all?" before "can AI do it?"** | Whenever automation is proposed | Waste that AI would make cheap and invisible [LEI-ETHINGTON-2026] |
| **Look for where work piles up and what the next step is starved of** | Every process | The constraint; improvement elsewhere does not raise output [TOCI-TOC-ND] |
| **Test every idea against the constraint:** does it speed the bottleneck or the step before it? | Shortlisting | Local gains that only create a pile-up [LEI-PEPERKAMP-2026; PEX-DUMAS-2025] |
| **Exploit and subordinate before elevating:** use the constraint fully and align other steps before buying or hiring | Shortlisting | Cheap capacity before tools [TOCI-5FS] |
| **Ask who verifies AI output and whether review is the new constraint** | Any AI candidate | Review load that cancels time saved. In one vendor survey nearly 40% of AI time savings were lost to rework (self-reported) [WORKDAY-2026] |
| **Use the queue rule on the busiest step** | Reviewer or specialist near full booking | Why 12.5% more work at 80% booking roughly doubles waiting (4× → 9×) [WIKI-KINGMAN-2025] |
| **Study demand at the front end:** which part exists only because of an earlier failure? | Service and request-driven work | Failure demand that disappears when the cause is fixed [SEDDON-SWINSCOE-2020] |
| **Run five whys on one specific failure,** check each "because" against a record, and branch when causes multiply | A particular defect or delay | Causes behind symptoms; not a verdict on a whole process [LEI-5WHYS; WIKI-5WHYS] |
| **Compare felt and measured gains** on existing AI use | A team says a tool "saves hours" | Perception gaps. In an independent trial, developers expected AI to cut task time 24%, believed afterwards it had cut 20%, and measured time rose 19% (software, adjacent) [METR-2025] |
| **Segment by experience** | Sizing a gain | Gains concentrate unevenly: in one customer-support study, +14% issues resolved per hour on average, +34% for novices, minimal for experienced staff [NBER-BRYNJOLFSSON-2023] |
| **Ask people what they want handed over and how much involvement they want, then compare with feasibility** | Sorting candidate tasks | Four zones: wanted and feasible, feasible but resisted, wanted but not yet feasible, neither. Workers were positive about automation for 46.1% of 844 tasks in one academic audit [STANFORD-WORKBANK-2026] |
| **Run a quick frontier test on real samples** | Before shortlisting an AI step | Where AI helps and where it fails quietly; consultants using AI were 19% less likely to produce a correct solution on a task chosen to be outside the frontier [HBS-JAGGED-2023] |
| **Run an agent-readiness check:** criteria written with examples, data and tool access, a record of actions | Steps that might be automated or delegated | Tacit know-how and missing audit trail that block automation [BCG-AGENTS-2025; MCKINSEY-1YR-2025] |
| **Ask about the data for this specific step,** especially documents | Every AI candidate | The real blocker: 79% of BCG respondents named lack of expertise with unstructured data, 82% of KPMG's named data quality (both self-reported) [BCG-GAP-2025; KPMG-AIPULSE-Q3-2025] |
| **Sort each unit's exposure before hunting use cases** | [U/O] | Which units need reinvention and which need adoption [BAIN-DILIGENCE-2025; BCPARTNERS-2025] |

## 6. Common traps

| Trap | Why it happens | How to avoid it |
|---|---|---|
| Automating waste | The tedious step is visible | "Should it exist?" first; sort steps by value [LEI-ETHINGTON-2026] |
| Speeding up a non-bottleneck | The fast step is easy to improve | Find the constraint; apply the speed-up ceiling [PEX-DUMAS-2025] |
| Busy mistaken for productive | Utilization looks good; elapsed time is mostly waiting | Measure flow efficiency and booking at the busy step [LEI-PEPERKAMP-2026] |
| Freed time becomes more output | Extra drafts the next step cannot absorb | Tie output to what the next step or customer needs [LEI-PEPERKAMP-2026] |
| Felt gains as evidence | People sincerely believe the tool helped | Compare with counts and timestamps [METR-2025] |
| Ignoring review and rework | The checking falls on others | Count review time and rework in the diagnosis [WORKDAY-2026] |
| Five whys as a verdict | Stops at the first plausible cause | Use it on one failure, verify, branch [WIKI-5WHYS] |
| Exposure read as a job forecast | Exposure percentages make headlines | Exposure says where change is possible, not what will happen; observed use is a fraction of theoretical [ELOUNDOU-2023; ANTHROPIC-LABOR-2026] |
| False precision in the heatmap | Numbers look objective | Show confidence and source per score; treat it as a conversation aid |
| Chasing noise | One bad week | Look at variation over several weeks first [NIST-CTRL-ND] |

## 7. Worked example

*Illustrative, continuing the audit practice; pain points from the assurance controls-testing module.*

*Waiting versus working.* Across six key controls on two engagements, hands-on time averaged about 11 hours against
about 20 working days elapsed (roughly 160 working hours): flow efficiency near 7% (from tracker and estimates).
*Constraint.* Files wait 6–11 days for manager review (from record); managers say they are "fully booked" in season,
call it 90%. At 90% booking, the queue rule gives waiting of about 9 times the review time. The partner's idea was AI
drafting of test workpapers. D3 ("if testing were twice as fast?") gets the answer "more files in the manager's
queue". The module reports the same pattern in the field: a SOX-tooling vendor's CEO says that with agents, human review is
where most auditor time now goes [CPAPA-ZANIN], and 46% of respondents to another vendor's survey report that staff spend
more time reviewing, validating or correcting AI output [OPTRO-SURVEY].
*Rework and failure demand.* About one in four evidence requests needs a second chase (reported); top reasons are
unclear requests and wrong period. That is failure demand: clearer requests remove it.
*Should it exist?* The private tick-mark template duplicates the audit platform; walkthrough narratives are redrawn
each year even when nothing changed (module §2).
*AI-fit signals.* Attribute testing on mixed-format evidence: review-assurance, high volume, criteria written for
most controls, staff keen to hand it over; agents are reported doing this in internal audit (`#05`, `#07`; self- or
vendor-reported). Deviation evaluation: expert-judgment, stays with a person (module §6). Manager review: the constraint;
AI secondary review is reported in the field (`#10`).
*Shortlist for Reimagine:* (1) manager review, as the constraint; (2) evidence requests and chasing; (3) attribute
testing, only together with (1); (4) walkthrough refresh.

*Unit heatmap (illustrative, outside-in, medium confidence)* for the wider practice:

| Unit | Size | Work-type mix | Exposure | Strategic weight | Readiness | Wave |
|---|---|---|---|---|---|---|
| Controls testing | 4 | 4 | 4 | 5 | 3 | 1 |
| SOC and attestation | 3 | 4 | 4 | 4 | 3 | 1 |
| Substantive testing | 5 | 4 | 4 | 4 | 2 | 2 |
| Acceptance and independence | 2 | 3 | 2 | 3 | 4 | 2 |
| Completion and reporting | 3 | 3 | 2 | 4 | 3 | 2 |

## 8. Output

Write a **Diagnose** section in the plan body.

[T]:
- **Findings table:** finding; type (waste, constraint, waiting, variation, rework, failure demand, should-not-exist,
  verification); evidence and its label (reported, from record, observed); steps affected; rough size (volume × time, share of elapsed time).
- **Constraint statement:** one sentence naming the bottleneck and what limits it.
- **AI-fit table per candidate step:** work type, variance, desire and involvement zone, frontier test result, data
  readiness, criteria written (yes / no), human checks that must stay.
- **Shortlist for Reimagine:** three to seven steps, each with the finding behind it and the lever it moves.

[U/O]:
- **Heatmap table:** unit, the five scores, confidence, source of scores, wave, planning mode.
- **Wave rationale** and shared constraints. Update `units[].wave` in frontmatter.

Then set `phase_completed: 3`, `next_phase: 4`, tick "Diagnose" and update `updated`. Reimagine (`reimagine.md`) takes the shortlist.

## 9. Sources

- **ANTHROPIC-LABOR-2026**: Anthropic, *Labor market impacts of AI: A new measure and early evidence* (vendor research, 2026-03-05). https://www.anthropic.com/research/labor-market-impacts
- **BAIN-DILIGENCE-2025**: Bain & Company, *New Diligence Challenge: Uncovering AI Risks and Opportunities* (consultancy, 2025-10-27). https://www.bain.com/insights/new-diligence-challenge-uncovering-ai-risks-and-opportunities/
- **BAIN-MIDYEAR-2026**: Bain & Company, *Private Equity Midyear Report 2026* (consultancy, 2026-06-08). https://www.bain.com/insights/private-equity-midyear-report-2026/
- **BCG-AGENTS-2025**: BCG, *How agents are accelerating the next wave of AI value creation* (consultancy, 2025-12-15). https://www.bcg.com/publications/2025/agents-accelerate-next-wave-of-ai-value-creation
- **BCG-GAP-2025**: BCG, *The Widening AI Value Gap* (consultancy survey, n=1,250, 2025-09). https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf
- **BCPARTNERS-2025**: BC Partners, *Spotlight on Portfolio Operations: Cameron Hulett* (PE firm Q&A, 2025-01-08). https://www.bcpartners.com/news/spotlight-on-portfolio-operations-cameron-hulett/
- **CPAPA-ZANIN**: Zanin, *5 Questions to Ask Before Your SOX Team Adopts AI Agents*, CPA Practice Advisor (trade press; author is a SOX-tooling vendor's CEO, 2026-08-18). https://www.cpapracticeadvisor.com/?p=188703
- **ELOUNDOU-2023**: Eloundou et al., *GPTs are GPTs* (academic preprint, 2023). https://arxiv.org/abs/2303.10130
- **HBS-JAGGED-2023**: Dell'Acqua et al., *Navigating the Jagged Technological Frontier* (field experiment, HBS WP 24-013, 2023-09). https://www.hbs.edu/faculty/Pages/item.aspx?num=64700
- **KANBANU-LITTLE-2022**: Kanban University, *Exploring Little's Law* (talk deck, 2022). https://kanban.university/wp-content/uploads/2022/09/Exploring-Littles-Law-KGS-2022.pdf
- **KPMG-AIPULSE-Q3-2025**: KPMG US, *Q3 2025 AI Quarterly Pulse* (consultancy survey, n=130, 2025-09-18). https://kpmg.com/us/en/media/news/q3-ai-pulse.html
- **LEI-5WHYS**: Lean Enterprise Institute, *5 Whys* (lexicon, undated). https://www.lean.org/lexicon-terms/5-whys/
- **LEI-7W-ND**: Lean Enterprise Institute, *Seven Wastes* (lexicon, undated). https://www.lean.org/lexicon-terms/seven-wastes/
- **LEI-ETHINGTON-2026**: Ethington, *Automation, AI, and the Risk of Doing Things Efficiently That Should Not Be Done at All*, The Lean Post (practitioner, 2026-03-05). https://www.lean.org/the-lean-post/articles/automation-ai-and-the-risk-of-doing-things-efficiently-that-should-not-be-done-at-all/
- **LEI-PEPERKAMP-2026**: Peperkamp, *Lean in the Age of AI: Optimizing the Stream, Not the Coder*, The Lean Post (practitioner, 2026-02-18). https://www.lean.org/the-lean-post/articles/lean-in-the-age-of-ai-optimizing-the-stream-not-the-coder/
- **MCKINSEY-1YR-2025**: McKinsey, *One year of agentic AI: Six lessons from the people doing the work* (consultancy, 2025-09-12). https://www.mckinsey.com/capabilities/quantumblack/our-insights/one-year-of-agentic-ai-six-lessons-from-the-people-doing-the-work
- **METR-2025**: METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* (RCT, 2025-07). https://arxiv.org/abs/2507.09089
- **NBER-ACEMOGLU-2024**: Acemoglu, *The Simple Macroeconomics of AI*, NBER WP 32487 (working paper, 2024-05). https://www.nber.org/papers/w32487
- **NBER-BRYNJOLFSSON-2023**: Brynjolfsson, Li, Raymond, *Generative AI at Work*, NBER WP 31161 (working paper, 2023-04, revised 2023-11). https://www.nber.org/papers/w31161
- **NIST-CTRL-ND**: NIST/SEMATECH, *What are Control Charts?* (standards reference, undated). https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm
- **OPENAI-GUIDE-2025**: OpenAI, *A practical guide to building agents* (vendor guide, 2025-04). https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- **OPTRO-SURVEY**: Optro, *One in Three Organizations Say They Have Acted on Wrong Decisions Made by AI Agents* (vendor survey release, 2026-10-08). https://optro.ai/blog/one-in-three-organizations-say-they-have-acted-on-wrong-decisions-made-by-ai-agents-optro-research-finds
- **PEX-DOWNTIME-2015**: PEX Network, *The eight deadly lean wastes: DOWNTIME* (practitioner, 2015-08-12). https://www.processexcellencenetwork.com/lean-six-sigma-business-performance/articles/the-8-deadly-lean-wastes-downtime
- **PEX-DUMAS-2025**: Dumas, *Process intelligence: The foundation of agentic AI success*, PEX Network (practitioner, 2025-02-04). https://www.processexcellencenetwork.com/ai/articles/process-intelligence-agentic-ai/amp
- **SEDDON-SWINSCOE-2020**: Swinscoe, *Interview with John Seddon of The Vanguard Method* (practitioner interview, 2020-01-27). https://www.adrianswinscoe.com/2020/01/a-lot-of-organisations-talk-outside-in-but-their-systems-are-not-designed-outside-in-interview-with-john-seddon-of-the-vanguard-method/
- **STANFORD-WORKBANK-2026**: Shao et al., *Future of Work with AI Agents* (WORKBank; academic preprint v3, 2026-02-01). https://arxiv.org/abs/2506.06576
- **TOCI-5FS**: Theory of Constraints Institute, *Five Focusing Steps* (practitioner guide, undated). https://www.tocinstitute.org/five-focusing-steps.html
- **TOCI-TOC-ND**: Theory of Constraints Institute, *Theory of Constraints* (practitioner guide, undated). https://www.tocinstitute.org/theory-of-constraints.html
- **WIKI-5WHYS**: Wikipedia, *Five whys*, criticism section (secondary, accessed 2026-10-16). https://en.wikipedia.org/wiki/Five_whys
- **WIKI-DMAIC-2025**: Wikipedia, *DMAIC*, Measure phase (tertiary, 2025-10-08). https://en.wikipedia.org/wiki/DMAIC
- **WIKI-KINGMAN-2025**: Wikipedia, *Kingman's formula* (tertiary, 2025-11-15). https://en.wikipedia.org/wiki/Kingman%27s_formula
- **WORKDAY-2026**: Workday, *Companies Are Leaving AI Gains on the Table* (vendor survey press release, 2026-01-14). https://en-hk.newsroom.workday.com/2026-01-14-New-Workday-Research-Companies-Are-Leaving-AI-Gains-on-the-Table?asPDF=1
- Assurance facts: `archetypes/assurance/modules/controls-testing.md` §2, §6, §7; use cases `#05`, `#07`, `#10`.

# Reimagine (phase 4)

Read this on entering phase 4. It tells you how to generate options for each high-value step or unit by
going through the four lenses in order, how to classify each option on `ladder` and `change_scope`, and
what to write. Keys in brackets, such as [MCKINSEY-1YR-2025], are listed in §9.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [The four lenses, made operational](#3-the-four-lenses-made-operational)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example: controls testing](#7-worked-example-controls-testing)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** For each high-value step (team scope) or each unit or value-chain stage (unit or organization
scope) that Diagnose selected, produce a short list of options that runs from "help the person" to "change
what we sell". The lenses stop the conversation ending at personal efficiency. The evidence that value
comes from redesigned workflows rather than added tools is correlational and self-reported, but consistent:
55% of McKinsey's AI high performers reported fundamentally redesigned workflows, against 20% of other
respondents [MCKINSEY-SOAI-2025].

**Exit criteria.** Move on only when all of these hold:

- Every priority step or unit has been taken through all four lenses. A lens can be marked "not now" with a reason.
- Every option has `ladder`, `change_scope`, `pattern`, `work_types`, `runtime_class` and a today → future
  description, plus evidence (archetype or overlay use-case ids with their grade) or the label "idea".
- Every option has passed the fit checks in §3.3, or the gap is written down as a prerequisite.
- Options reach delegate level and model scope where the journey stage calls for it (§2, stage table).
- Every automate, delegate or reinvent option notes which tasks move away from people. Full role evolution
  comes in Make the case (see `people-and-change.md`).
- The user has heard the option list played back and has kept, changed or dropped each one.

## 2. How to run it

1. **Name the phase.** "We are in Reimagine: generating options. Next we score them in Prioritize."
2. **Anchor the outcome first.** For each target, get the outcome in one sentence with two or three success
   factors, and who uses the output [ROLANDBERGER-2026]. This separates the stable "what" from the
   changeable "how".
3. **Scout in parallel.** Use subagents for this step: delegate one subagent per high-value step or unit, in
   parallel, using the `scout-use-cases` brief. If you cannot start subagents, do each yourself, one at a time.
   Each returns five or fewer use cases and patterns, with fit and evidence grade. Search the archetype YAML by
   `module:`, `work_types:`, `pattern:`, `ladder:` and `change_scope:` instead of reading whole files.
4. **Walk the lenses in order, one question at a time** (§3.1). After each answer, play back the option in
   one sentence and run the quick fit checks (§3.3).
5. **Bring evidence in as you go.** Quote the use case, its maturity and grade, and the provenance of any
   figure: most published outcome figures are self-reported or vendor-published.
6. **Play back the whole list** as a table (lens, option, ladder, scope, evidence) and ask the user to keep,
   change or drop each line. Then write the output (§8) and update the plan state.

**Adapt by journey stage** (stage markers are in `onboarding.md`).

| Stage | How far to push the lenses |
|---|---|
| Curious | Mostly lens 1. Explain the ladder with archetype examples. Aim for two or three quick wins with existing tools. Name lens 4 as a "what if" without going deep |
| Experimenting | Lenses 1 and 2 in depth; lenses 3 and 4 as a target picture, not a plan. Turn individual use into a shared team workflow. Look for repeatable, high-volume steps |
| Adopting | All four lenses. Delegate only one or two bounded, low-risk outcomes, and only when all five gates in `onboarding.md` hold (otherwise the missing gate becomes a foundation item); broader delegation belongs to Scaling (advisor rule; BCG finds agent use concentrated in its most AI-mature firms [BCG-GAP-2025]) |
| Scaling | All four, with reuse: which options share components across units. Delegation at scale, agent governance, lens 4 across the portfolio |
| AI-native | Start from lens 4: business model, pricing, new services, AI-native competitors, then work back to steps |

## 3. The four lenses, made operational

### 3.1 Lens table

| Lens | Ask the user (plain language) | `ladder` | `change_scope` | Typical patterns and runtime |
|---|---|---|---|---|
| 1. Improve the step | "Where in this step would a capable assistant save you time or catch mistakes, with you still owning the result?" | `assist` (person owns, AI helps) or `augment` (AI gives a first pass inside the step, person reviews) | `step` | draft–review loop, grounded knowledge assistant, research & brief; personal assistant or shared team skills |
| 2. Automate the flow | "Which items could go through with no one touching them, as long as the odd ones come to a person?" | `automate` | `step` if one step runs alone; `process` if hand-offs are removed or work becomes continuous or full-population | intake & triage, reconcile & handle exceptions, full-population testing, bulk transformation; workflow automation with AI steps |
| 3. Delegate the outcome | "What would you hand over end to end if you could see exactly what was done and stop it at any point?" | `delegate` (agent owns a multi-step outcome, started by events, with checkpoints) | `process` | end-to-end case agent, document-to-decision, monitor → diagnose → act; background agent or managed agent runtime |
| 4. Reinvent the work | "If you started this today with no history, would this work exist? What would clients pay for instead?" | any | `model` if the service, pricing, sourcing or who does the work changes; `process` if the process stops existing or is replaced while the service model holds | any; check archetype `disruption.md` and `frontier.md` |

**Recording rules.** Classify the two dimensions separately: how much the AI does and how much of the work
changes are independent questions, and one merged scale blurs them. An option that removes people from the normal path is `automate`,
even if it uses an LLM. An agent that only drafts for a person to finish is `augment`, whatever the vendor
calls it. Write "reinvent"
into the description when lens 4 produced an option recorded as `process`.

### 3.2 The AI-native competitor move (lens 4)

Ask in three parts [MITTR-DELOITTE-2026; BCG-AGENTS-2025; three-part form is advisor synthesis]:

1. "Which of our steps would a new firm built on AI simply not have?"
2. "What would they charge for: the outcome, a subscription, or still the hour?"
3. "Who would check their work, and how would a client trust it?"

Then, at unit or organization scope, sort each service line as threatened, changed or merely helped (Bain's
revolution, transformation and augmentation sort; under 10% of 300+ diligence targets fell in "revolution",
about half in "augmentation", vendor-published) [BAIN-DILIGENCE-2025]. Where the user can, suggest building
a rough prototype of the unit's core deliverable with off-the-shelf AI to see what an entrant could do.

**Be candid about the evidence.** The research behind this move is thin: it rests on consultancy opinion
(BCG, Roland Berger) and sponsored content; no independent study of AI-native service firms was found.
Treat every answer as a hypothesis to test, label the resulting options "idea" unless an archetype use case
supports them, and say so to the user.

### 3.3 Fit checks for every option

| Check | Ask yourself or the user | Fails when |
|---|---|---|
| Should it exist? | "What would happen if this step stopped?" [LEI-ETHINGTON-2026] | The step has no customer; remove it instead of automating it |
| Simplest thing that works | Could a rule, a script or one model call do it? Climb to one agent with tools, then several agents, only with a reason [ANTHROPIC-BEA-2024; AZURE-PATTERNS] | Low-variance, standardized work is given to an agent |
| Agent washing | "What does it decide at runtime that a rule would not?" [GARTNER-AGENTIC-2025] | Nothing; it is automation or an assistant renamed |
| Agent-readiness | Are the decision criteria written down with examples? Can it reach the data and tools a good worker uses? Where is evidence of what it did logged? [BCG-AGENTS-2025; IMDA-MGF-2026] | Any answer is "no": record it as a prerequisite |
| Constraint | "If this step were twice as fast, what would the next step see?" [LEI-PEPERKAMP-2026] | It speeds a non-bottleneck or floods the review step |
| Jagged edge | Test on two or three real examples before trusting a demo [HBS-JAGGED-2023] | Similar-looking tasks fail quietly |
| People's preference | "Which of these would your team hand over, share, or keep?" [STANFORD-WORKBANK-2026] | Feasible but resisted ("red light"); plan the change, don't skip it |
| Security | Does it combine private data, untrusted content and a way to send things out? [WILLISON-2025] | All three legs present; remove one in the design |

## 4. Question bank

Tags: **[T]** team scope, **[U/O]** unit or organization scope. Stage notes in italics. Core questions first.

**Core**
- What does this work exist to produce, and who uses it? Say it in one sentence. [T][U/O]
- If we designed this today, simply, what would it look like? [T][U/O]
- Which step exists only because a person used to do it, or because of an old system limit? [T]
- Of the steps left, which need judgment each time and which follow a fixed rule? [T]
- If a new firm started this with AI and no history, which of these steps would it not have? [T][U/O]

**Lens follow-ups**
- Lens 1: Which step already has a clear checklist that a good reviewer applies? [T] *Curious, Experimenting*
- Lens 2: Where are items handed from one person to the next and lose context on the way? [T][U/O]
- Lens 2: What share of items follows the standard path? What sends the rest to a person? [T]
- Lens 3: What would you hand over end to end if you could watch it and stop it? [T][U/O] *Adopting+*
- Lens 3: What event should start the work: a new request, a file arriving, a date? [T]
- Lens 4: What would clients buy if this took minutes and cost a fraction? [U/O] *Scaling, AI-native*
- Lens 4: How is this work priced today? What happens to revenue if the effort halves? [U/O]
- Lens 4: Which of your service lines would a well-funded new entrant attack first? [U/O]

**Checks**
- What would you need to see before trusting a result you did not produce? [T]
- Who would check the output, how long would that take, and is that person already overloaded? [T]
- Which of these would your people gladly hand over, which would they want to share, and which never? [T]
- Could you try one of these on a real example this week? [T] *Curious, Experimenting*
- Which options could several teams use with the same building blocks? [U/O] *Scaling*

## 5. Expert moves

1. **Outcome before steps.** Write the outcome and success factors before touching the map. *When:* start of
   the phase. *Reveals:* steps that serve no outcome [ROLANDBERGER-2026; CAPGEMINI-ZBPR-2025].
2. **Zero-based, then add back constraints one at a time, each with a named reason.** *When:* lens 4, once
   the current map exists. *Reveals:* which constraints are real and which are inherited [CAPGEMINI-ZBPR-2025].
3. **Decision, action or hand-off?** Label each step; for decisions, ask how much variance it must absorb.
   *When:* choosing between lens 2 and lens 3. *Reveals:* rule-fit versus agent-fit [MCKINSEY-1YR-2025; OPENAI-GUIDE-2025].
4. **Climb the complexity ladder out loud** (single call → one agent with tools → several agents) and make
   the user justify each rung. Default to one agent; several agents cost more tokens (about 15x chat in
   Anthropic's own research system, vendor-published) and fail on interdependent decisions
   [ANTHROPIC-MULTI-2025; COGNITION-2025]. *When:* any agent proposal.
5. **Look for the composite process.** Ask where a deliverable crosses billing, legal, delivery or a third
   party. *When:* lens 3 or 4. *Reveals:* where agents beat single-tool assistants [DELOITTE-TT-2025].
6. **Compare what people want with what is feasible.** Rate tasks from "agent alone" to "human alone" with
   the team, then compare with expert feasibility. *Reveals:* green-light and red-light tasks. Workers were
   positive about automation on 46.1% of tasks; equal partnership was the preferred level in 45.2% of
   occupations (independent) [STANFORD-WORKBANK-2026].
7. **Ask what plays the role of "tests".** Coding agents work because automatic tests check them; ask what
   the equivalent is here (a reviewer's rubric, a reconciliation). *Reveals:* whether delegation can be
   verified [GITHUB-COPILOTAGENT-2025].
8. **Run the constraint test with numbers.** If the reviewer is booked about 80%, waiting is about four times
   the review time; at 90% it is about nine times (queue formula, variability factor 1). More AI drafts into a
   full review step lengthen the queue [WIKI-KINGMAN-2025; LEI-PEPERKAMP-2026].
9. **Use the redesign catalogue, not a blank page.** After diagnosis, walk known redesign heuristics
   (task elimination, task composition, parallelism, triage, knock-out ordering) against the measured
   weakness [NETJES-2007].
10. **Ask how corrections feed back.** "When someone fixes the output, where does that fix go?" *Reveals:*
    whether the option can learn [MIT-NANDA-2025; MCKINSEY-1YR-2025].

## 6. Common traps

| Trap | How the advisor avoids it |
|---|---|
| **Automating waste** ("paving the cow path") | Ask "should this exist?" before "can AI do it?" [LEI-ETHINGTON-2026; HBR-HAMMER-1990] |
| **Stopping at lens 1** | Go through all four lenses in order; record "not now" with a reason rather than skipping |
| **Agent where something simpler fits** | Complexity ladder and agent-washing probe (§3.3). Gartner forecasts over 40% of agentic projects cancelled by end of 2027 (a forecast) [GARTNER-AGENTIC-2025] |
| **Benchmark optimism** | On a simulated software company the best agent completed 30.3% of tasks on its own (independent) [ARXIV-TAC-2025]. Test on the user's own cases |
| **Speeding a non-bottleneck** | Constraint test (move 8); name where review capacity comes from |
| **Delegation without readiness** | Agent-readiness check; missing criteria, access or logging become prerequisites, not hopes [BCG-AGENTS-2025] |
| **Presenting the AI-native lens as fact** | Label as hypotheses; cite archetype disruption evidence where it exists (§3.2) |
| **Ignoring who loses tasks** | Note tasks moving for each automate, delegate or reinvent option now; "automate" and "delegate" carry workforce consequences that "improve" usually does not |

## 7. Worked example: controls testing

*Setting (illustrative):* continuing the audit partner's regional practice from `onboarding.md` and
`frame.md` (stage: Experimenting). Diagnose shortlisted manager review (the constraint), evidence requests
and chasing, attribute testing on mixed-format evidence (only together with review), and the walkthrough
refresh (`diagnose.md`). Evidence ids are from
`../archetypes/assurance/use-cases/controls-testing.yaml`; `#07` means `assurance-controls-testing-07`.

| Lens | Option | `ladder` / `change_scope` | Evidence |
|---|---|---|---|
| 1 Improve | AI secondary review: models check a workpaper for missing evidence before the manager sees it | augment / step | `#10`, grade B, qualitative only |
| 1 Improve | Walkthrough narrative drafted from last year's file, with changes flagged | augment / step | `#01`, grade B; PwC calls year-one savings "not that drastic yet" |
| 1 Improve | Agent checks evidence submissions against the request before testing | augment / step | `#03`, grade C, vendor claim; clearer request templates come first and need no AI |
| 2 Automate | The firm's evidence-matching tool on every engagement: documents matched to samples, mismatches to the auditor | automate / step | `#07`, grade B; 16 h to 5–6 h per engagement at one firm, mostly substantive work, self-reported |
| 2 Automate | Full-population test of one transactional control instead of a sample | automate / process | `#08`, grade A |
| 3 Delegate | Platform agent tests a defined control set and drafts the workpaper; reviewer signs every conclusion | delegate / process | `#16`, grade B, piloting. Target picture only: the delegation gates in `onboarding.md` fail at Experimenting |
| 4 Reinvent | AI-native audit: agents test controls and balances on full populations; auditors on judgment and clients | delegate / model | `#17`, grade B, piloting with five clients |
| 4 Reinvent | Controls work sold as platform plus review instead of hours inside a fixed fee | delegate / model | `#20`, grade B; hypothesis for this practice |

*Fit checks the advisor ran.* "If evidence matching doubled throughput, what would your managers see?"
More files waiting for review, so `#07` was paired with `#10` and a standard review checklist (a foundation
in Prioritize). "Should every walkthrough be redrafted each year?" Not when nothing changed, so the
advisor added "roll forward unchanged walkthroughs" as a plain process change ahead of `#01`. The AI-native
questions surfaced one hypothesis and one open risk. Hypothesis: if competitors sell testing as platform plus
review, the practice's fixed fees will come under more pressure. Open risk: no public case yet exists of an
external auditor relying on a client's agent-tested controls (`#24`, idea), so any reinvention that depends
on it stays a bet.

## 8. Output

Write to `opportunities.yaml` (schema in `../schemas/`), one item per kept option. Leave `value`, `scores`,
`weighted_score` and `category` for Prioritize, and `capacity_use` for Make the case.

```yaml
- id: ct-07
  title: Evidence matching on every controls-reliance engagement
  process: Test of operating effectiveness
  work_types: [review-assurance, transaction-processing]
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  description: "Today: staff open each client document and vouch it to its sample. Future: the tool matches and links each value to its source; the auditor works every mismatch and re-performs a sample."
  prerequisites: [standard review checklist for the top control types, documentation note on tool use]
  risks: [matches accepted without review, juniors lose vouching practice]
  human_checkpoints: [auditor reviews each exception and signs off the test, reviewer re-performs a sample of matches]
  role_evolution: { tasks_moving: [document-to-sample vouching], new_work: [exception investigation, earlier risk work] }
  evidence: [assurance-controls-testing-07]
```

In `transformation-plan.md`: under the Reimagine section, a table per target (lens, option, ladder, scope,
evidence, kept or dropped and why), the AI-native competitor hypotheses labelled as hypotheses, and the
prerequisites found. Set `phase_completed: 4`, `next_phase: 5`, `updated`, and tick the progress checklist.

## 9. Sources

- `ANTHROPIC-BEA-2024` — Anthropic, *Building effective agents*, vendor guide, 2024-12-19. https://www.anthropic.com/engineering/building-effective-agents
- `ANTHROPIC-MULTI-2025` — Anthropic, *How we built our multi-agent research system*, vendor write-up, 2025-06-13. https://www.anthropic.com/engineering/multi-agent-research-system
- `ARXIV-TAC-2025` — Xu et al. (CMU), *TheAgentCompany*, academic preprint v3, 2025-09-10. https://arxiv.org/abs/2412.14161
- `AZURE-PATTERNS` — Microsoft Learn, *AI agent orchestration patterns*, platform guidance, updated 2026-02-12. https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- `BAIN-DILIGENCE-2025` — Bain & Company, *New diligence challenge: uncovering AI risks and opportunities*, consultancy, 2025-10-27. https://www.bain.com/insights/new-diligence-challenge-uncovering-ai-risks-and-opportunities/
- `BCG-AGENTS-2025` — BCG, *How agents are accelerating the next wave of AI value creation*, consultancy, 2025-12-15. https://www.bcg.com/publications/2025/agents-accelerate-next-wave-of-ai-value-creation
- `BCG-GAP-2025` — BCG, *The widening AI value gap* (n=1,250), consultancy survey, 2025-09. https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf
- `CAPGEMINI-ZBPR-2025` — Capgemini, *From zero to autonomous*, practitioner article, 2025-11-12. https://www.capgemini.com/us-en/insights/expert-perspectives/from-zero-to-autonomous-redesigning-operations-with-agentic-ai/
- `COGNITION-2025` — Cognition, *Don't build multi-agents*, practitioner essay, 2025-06-12. https://cognition.ai/blog/dont-build-multi-agents
- `DELOITTE-TT-2025` — Deloitte Insights, *The agentic reality check* (Tech Trends 2026), consultancy, 2025-12-10. https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
- `GARTNER-AGENTIC-2025` — Gartner, *Over 40% of agentic AI projects will be canceled by end of 2027*, analyst forecast, 2025-06-25. https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- `GITHUB-COPILOTAGENT-2025` — GitHub, *Meet the new coding agent*, vendor announcement, 2025-05-19. https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/
- `HBR-HAMMER-1990` — M. Hammer, *Reengineering work: don't automate, obliterate*, HBR, 1990-07. https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate
- `HBS-JAGGED-2023` — Dell'Acqua et al., *Navigating the jagged technological frontier* (758 consultants), field experiment, 2023-09. https://www.hbs.edu/faculty/Pages/item.aspx?num=64700
- `IMDA-MGF-2026` — IMDA Singapore, *Model AI governance framework for agentic AI* v1.5, regulator guidance, 2026-05-20 (updated 2026-06-05). https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf
- `LEI-ETHINGTON-2026` — Lean Enterprise Institute, *Automation, AI, and the risk of doing things efficiently that should not be done at all*, 2026-03-05. https://www.lean.org/the-lean-post/articles/automation-ai-and-the-risk-of-doing-things-efficiently-that-should-not-be-done-at-all/
- `LEI-PEPERKAMP-2026` — Lean Enterprise Institute, *Lean in the age of AI: optimizing the stream, not the coder*, 2026-02-18. https://www.lean.org/the-lean-post/articles/lean-in-the-age-of-ai-optimizing-the-stream-not-the-coder/
- `MCKINSEY-1YR-2025` — McKinsey, *One year of agentic AI: six lessons*, consultancy, 2025-09-12. https://www.mckinsey.com/capabilities/quantumblack/our-insights/one-year-of-agentic-ai-six-lessons-from-the-people-doing-the-work
- `MCKINSEY-SOAI-2025` — McKinsey, *The state of AI in 2025* (n=1,993; figure from Exhibit 11), consultancy survey, 2025-11. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- `MIT-NANDA-2025` — MIT NANDA, *The GenAI divide* (preliminary, interview-based), 2025-07. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `MITTR-DELOITTE-2026` — MIT Technology Review Insights with Deloitte, *Enabling agent-first process redesign*, sponsored content, 2026-04-07. https://technologyreview.com/2026/04/07/1134966/enabling-agent-first-process-redesign
- `NETJES-2007` — Netjes, Limam Mansar, Reijers, van der Aalst, *An evolutionary approach for business process redesign*, academic, 2007. https://www.vdaalst.com/publications/p387.pdf
- `OPENAI-GUIDE-2025` — OpenAI, *A practical guide to building agents*, vendor guide, 2025-04. https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `ROLANDBERGER-2026` — Roland Berger, *Leading with AI-first*, consultancy, 2026-07-16. https://www.rolandberger.com/en/Insights/Publications/Leading-with-AI-first-Rethinking-and-redesigning-processes-and-organizations.html
- `STANFORD-WORKBANK-2026` — Shao et al. (Stanford), *Future of work with AI agents* (WORKBank), academic preprint v3, 2026-02-01. https://arxiv.org/abs/2506.06576
- `WIKI-KINGMAN-2025` — Wikipedia, *Kingman's formula*, reference, modified 2025-11-15. https://en.wikipedia.org/wiki/Kingman%27s_formula
- `WILLISON-2025` — S. Willison, *The lethal trifecta for AI agents*, practitioner article, 2025-06-16. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Archetype evidence: `../archetypes/assurance/modules/controls-testing.md` and its use-case YAML (sources listed there).

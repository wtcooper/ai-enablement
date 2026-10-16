# Method topic: lean-six-sigma-knowledge-work

Stream M · Wave 1 · Written 2026-10-16

**Topic focus:** Lean and Six Sigma applied to knowledge work and professional services: value stream mapping for office processes, the eight wastes (DOWNTIME), flow and queues, theory of constraints, SIPOC, DMAIC (especially Measure and Control), baselining, variation and rework, kaizen, process discovery; how practitioners now combine lean/six sigma with AI and automation (including the trap of automating waste); process mining as an input.

**Phases fed:** map, diagnose, prioritize, plan-and-control

**How to read the refs.** Refs follow `PUBLISHER-SHORT-YYYY`. `ND` means the page carries no publication date; the access date for every source is 2026-10-16. Each source is marked `access: full`, `partial` (only part of the text reached, stated in section 9) or `search-only` (only search-result snippets were seen). Figures from `search-only` sources are kept out of the main argument and marked where used. Locators are section names, slide titles, or page numbers as printed in the file.

---

## Contents

1. Summary
2. Core concepts in plain language
3. Expert moves
4. Question bank
5. Common traps
6. Evidence
7. Worked examples
8. Mapping to phases
9. Sources
10. Gaps

---

## 1. Summary

- **The method toolkit is old and well-documented; what is new is the pairing with AI.** Lean (value, flow, waste, kaizen), Six Sigma (DMAIC, baselines, variation, control charts) and the theory of constraints (find and exploit the constraint) date from manufacturing and have been adapted to services. LEI describes value stream mapping as usable "in any industry" though "most commonly used in lean manufacturing" (LEI-VSM-ND). The 2025–2026 practitioner conversation (LEI Lean Post, PEX Network, BPM academics) is about using those foundations to decide *where* AI goes.
- **The central practitioner warning is "don't automate waste, and don't speed up a non-bottleneck."** LEI's Ethington (Mar 2026) asks whether a task should exist before it is automated and warns that AI tools may end up "churning out waste" that stays invisible (LEI-ETHINGTON-2026). Peperkamp (Feb 2026) argues AI optimizes resource efficiency while flow efficiency and review capacity become the new constraint (LEI-PEPERKAMP-2026). Dumas (PEX, Feb 2025) says automating a bottleneck "may simply shift the constraint downstream" and that undetected defects can start rework loops (PEX-DUMAS-2025).
- **Knowledge work needs a different baseline than a stopwatch.** Useful measures are the ones Kanban uses (WIP, throughput, cycle time, work item age; KANBAN-GUIDE-2025), flow efficiency (active time over elapsed time), rework and return rates, and variation shown on a chart rather than as an average (NIST-CTRL-ND). Queue theory (Kingman's formula) says waiting time grows steeply as utilization approaches 100% and with variability (WIKI-KINGMAN-2025).
- **Perception is a poor baseline.** In an independent randomized trial, experienced developers expected AI to cut task time by 24% and, after the study, believed it had cut it by 20%; measured time rose by 19% (METR-2025). That is a software-engineering setting (adjacent), but it justifies measuring before and after instead of asking people how it went.
- **Process mining is the data-driven input to Map and Diagnose, but it needs event data and a question.** The IEEE Task Force's manifesto says log extraction "should be driven by questions" and rates event-log quality on five maturity levels (PMMANIFESTO-2012). A 2026 dissertation shows LLM pipelines building event logs from customer-service conversations, which matters for knowledge work that leaves no system log, and says that turning diagnosed weaknesses into redesigns "remains largely manual" (KECHT-2026).
- **Outcome evidence for AI in knowledge-work processes is mostly self-reported, survey-based or adjacent.** Examples: MIT NANDA preliminary findings (95% of organizations with no measurable P&L return; 52 interviews, 153 survey responses; MIT-NANDA-2025), BCG (5% of 1,250 firms at scale; BCG-GAP-2025), and a Workday survey (about 37% of time saved goes to rework; HCAMAG-WORKDAY-2026). Independent measurement of lean/six sigma combined with AI in professional services was not found.
- **Lean in knowledge work has a credible academic base, with caveats.** Staats and Upton's Wipro study (archival data plus 100+ interviews) found lean software projects performed better on most outcomes, but defect counts did not differ (STAATS-JOM-2011; KENAN-2012). Law-firm results (Seyfarth) are self-reported (PEX-SEYFARTH-2009).
- **Sustaining change is its own problem.** Kaizen gains fade without a standard and without peer learning and acceptance (LEI-KAIZEN-ND; GLOVER-2015, manufacturing). DMAIC's Control phase (control charts, response plan, owner) and LEI's warning that automated processes degrade unobserved are the two ideas the advisor should carry into Plan-and-control.

---

## 2. Core concepts in plain language

**Value, from the customer's side.** Lean starts by asking what problem the customer needs solved (LEI-WHATISLEAN-ND). Work is then sorted into value-creating, incidental (needed but not valued by the customer) and waste (LEI-7W-ND). *Knowledge work:* much effort is incidental (reformatting, status reports, approvals), and teams often cannot say who the customer of a step is. *AI:* AI makes incidental work cheap to produce, which can hide the question of whether it should be done at all (LEI-ETHINGTON-2026).

**Value stream and the current-state map.** A value stream is all the actions, value-creating or not, needed to get from request to the customer. Mapping starts with the actual current state, then a target state (LEI-VSM-ND). The map includes information flow, not just the flow of material, which is why it suits office work (LEI-L2SEE-ND). *Knowledge work:* the "material" is a case, a file, a decision or a draft. *AI:* a map shows which steps are candidates for improving, automating or delegating, and what sits in front of and behind them.

**The eight wastes (DOWNTIME).** Defects, Overproduction, Waiting, Non-utilized talent, Transportation, Inventory, Motion, Extra processing (PEX-DOWNTIME-2015). Ohno's original list had seven; "non-utilized talent" was added later (PEX-DOWNTIME-2015: "not part of TPS' seven wastes"). Sources differ on the eighth item, and the office translation is an adaptation, not something the sources define. *Knowledge work:* waiting (queues, approvals), defects (rework, returns), extra processing (duplicate documents, sign-offs, meetings) usually dominate; transportation matters less because most of it "can be sent by email" (PEX-DOWNTIME-2015). *AI:* AI tends to inflate overproduction (more drafts, more output than the next step can absorb) and inventory (a pile of work awaiting review) (LEI-PEPERKAMP-2026).

**Flow, WIP and queues.** Flow is movement of potential value through the system (KANBAN-GUIDE-2025). Little's Law relates average WIP, throughput and lead time, and holds only when the system is stable (average arrivals equal average departures) (KANBANU-LITTLE-2022). Kingman's formula approximates waiting time as utilization/(1 - utilization) x a variability term x service time (WIKI-KINGMAN-2025). *Knowledge work:* people fully booked at 90%+ create long queues and long lead times even when each task is quick. *AI:* more output into a fully loaded review step lengthens the queue.

**Theory of constraints.** Every system has a limiting step; improvement elsewhere does not raise output (TOCI-TOC-ND). The five focusing steps are identify, exploit, subordinate, elevate, repeat; the sources warn against jumping to "elevate" (buy, hire) before exploiting and subordinating (TOCI-5FS-ND). *Knowledge work:* the constraint is often a scarce expert, a decision-maker or a verification step, not the typing. *AI:* speeding a non-constraint creates pile-up (LEI-PEPERKAMP-2026; PEX-DUMAS-2025).

**SIPOC.** Suppliers, Inputs, Process, Outputs, Customers: a one-page scope diagram, usually produced early in Measure to bound a poorly scoped problem (ISIX-SIPOC-2025). *Knowledge work:* it exposes who really supplies inputs (other teams, clients) and who consumes outputs. *AI:* it fixes the unit being changed, and the inputs an AI step would need.

**DMAIC, especially Measure and Control.** Define, Measure, Analyze, Improve, Control. Measure establishes performance baselines against which the end result is judged, and teams are expected to check that the measurement system is suitable. Control embeds the change: amend ways of working, sign off benefits, track improvement, and use a control chart with a response plan (WIKI-DMAIC-2025, sections Measure and Control). *Knowledge work:* "defect" and "done" must be defined before they can be counted. *AI:* the baseline is what turns an AI pilot from anecdote into evidence; the control plan is what notices when an automated step drifts.

**Variation and rework.** Control charts separate chance-cause variation (inside control limits) from points that signal an assignable cause (NIST-CTRL-ND). Rework is the "defects" waste and in service organizations is often visible as demand caused by a failure to do something or do it right the first time (failure demand; GOVMETRIC-2026 definition; SEDDON-SWINSCOE-2020). *Knowledge work:* rework is hidden in email chains and resubmissions. *AI:* AI output that needs correction adds a rework loop (PEX-DUMAS-2025; HCAMAG-WORKDAY-2026).

**Kaizen and standard work.** Kaizen is continuous improvement through plan-do-check-act cycles; LEI quotes Ohno that "there can be no kaizen without a standard," and says stable operating conditions come first, otherwise gains "vanish" (LEI-KAIZEN-ND). *Knowledge work:* a documented standard way of doing the work (checklist, template, decision rule) is the baseline for improvement and for any AI step. *AI:* a standard defines what "good output" is, so it can be checked.

**Process discovery and process mining.** Process mining discovers, monitors and improves real processes from event logs rather than assumed ones (PMMANIFESTO-2012). It needs case IDs, activities and timestamps. Process intelligence combines process mining, task mining, simulation and AI (PEX-DUMAS-2025). *Knowledge work:* much work happens in email, chat and documents, so logs are poor or absent; research prototypes extract events from text (KECHT-2026). *AI:* process data is what an agent needs to know which step to act on, and what a monitor needs to catch defects (DUMAS-AGENTIC-2026).

---

## 3. Expert moves

Format: **move** — when to use it — what it reveals — source ref (locator). Items marked *(adapted)* are advisor adaptations of a source's idea to knowledge work or AI; the source gives the underlying concept, not the exact tactic.

1. **Open with "what problem is the customer trying to solve, and who is the customer of this step?" before drawing anything** — framing / start of Map — separates value from habit and finds steps with no identifiable customer — LEI-WHATISLEAN-ND (opening paragraphs); LEI-ETHINGTON-2026 (section "Guiding principles").
2. **Ask "should this task exist at all?" before asking "can AI do it?"** — Diagnose and Prioritize, whenever someone proposes automating a step — the risk of doing efficiently what should not be done — LEI-ETHINGTON-2026 (sections "Tripping over your own feet", "So what?").
3. **Go and watch real cases being worked, not only the process owner's description** — Map — differences between the described and actual process; hidden information flow — LEI-ADMIN-ND (paragraph on "go see, ask why, show respect"); LEI-L2SEE-ND (map includes information flow). *(adapted)*
4. **Ask for last month's actual volume, with the odd weeks, not a typical week** — Map and baseline — variation, peaks, hidden rework; variability drives queue length — WIKI-KINGMAN-2025 (formula, variability terms); WIKI-DMAIC-2025 (Measure: baselines). *(adapted)*
5. **Draw a SIPOC first when scope is arguable** — start of Map — unclear customers, suppliers who are other teams, inputs that arrive incomplete — ISIX-SIPOC-2025 (introduction; "typically employed at the Measure phase").
6. **Map the current state by step with two times: hands-on time and elapsed time** — Map — where work waits rather than gets worked — LEI-VSM-ND (current state map); KANBAN-GUIDE-2025 (cycle time definition). *(adapted)*
7. **Compute flow efficiency (active time ÷ total elapsed time) for a sample of real cases** — Diagnose — waiting dominates lead time, so a faster "doing" step helps little — KANBANU-LITTLE-2022 (slides "Flow Efficiency, Efficiency, Lead Time and Throughput"). The slide table is an exercise, not field data.
8. **Pull four numbers per workflow: WIP, throughput, cycle time and age of each open item** — Map and baseline — stuck work, items older than the service expectation, true load — KANBAN-GUIDE-2025 (section "Flow Metrics").
9. **Ask "which is the oldest open item and why is it still open?"** — Diagnose — blockers, hidden queues, approval lag — KANBAN-GUIDE-2025 (Work Item Age; "Actively Managing Items in a Workflow").
10. **Check that arrivals roughly equal completions before using Little's Law to estimate lead time** — Diagnose — whether the system is stable or WIP is quietly growing — KANBANU-LITTLE-2022 (slide "Little's Law Assumptions – The System is Stable").
11. **Ask how booked the busiest people are at the step where work piles up, then reason from the queue formula** — Diagnose — with the formula utilization/(1 - utilization), 80% gives 4 and 90% gives 9 times the service time (for variability factor 1; computed from the formula), so adding load to a step near full booking multiplies waiting — WIKI-KINGMAN-2025 (statement of formula). *(adapted)*
12. **Look for where work piles up in front of a step and what the step after it is starved of** — Diagnose and Prioritize — the constraint — TOCI-TOC-ND (chain analogy); PEX-DUMAS-2025 (section "Why is process intelligence so important for agentic AI?").
13. **Run the five focusing steps in order: identify, exploit, subordinate, then elevate** — Prioritize and Plan — cheap capacity before capital; avoids "buy a tool" as the first move — TOCI-5FS-ND (the five steps and the warning about skipping to elevation). The "30% hidden capacity" figure there is the institute's own claim, unreferenced.
14. **Test every AI proposal against the constraint: "does this speed up the bottleneck, or the step before it?"** — Prioritize — local gains that create a pile-up — LEI-PEPERKAMP-2026 (section "The AI Efficiency Trap").
15. **Ask who verifies the AI output, how long that takes, and whether verification capacity is the new constraint** — Diagnose and Prioritize — review load as the new bottleneck, rework loops — LEI-PEPERKAMP-2026 (cognitive load); DUMAS-AGENTIC-2026 (section 4.3, verification pattern).
16. **Sample real cases and count how many were returned, reopened or touched more than once** — Measure — the rework rate, i.e. the defects waste — PEX-DOWNTIME-2015 (Defects); PEX-DUMAS-2025 (rework loops). *(adapted)*
17. **Study incoming demand by type and ask which part exists only because something earlier failed** — Map and Diagnose, service processes — failure demand, the part that can be removed by fixing the cause — SEDDON-SWINSCOE-2020 (advice to study demand at the front end); GOVMETRIC-2026 (definition).
18. **Classify each step as value-creating, incidental or waste from the customer's standpoint, then walk the DOWNTIME list for the steps left** — Diagnose — what to remove, what to keep, what to automate — LEI-7W-ND (section on categories of work); PEX-DOWNTIME-2015. The list-to-office translation is an adaptation. *(adapted)*
19. **Before promising process mining, ask which system records case ID, activity and timestamp, and rate the log on the five maturity levels** — Map — whether data exists at all, and how far to trust results — PMMANIFESTO-2012 (GP1 and Table 1).
20. **Pick the process question first, then extract data** — Map — avoids "mine everything" projects — PMMANIFESTO-2012 (GP2 "Log Extraction Should Be Driven by Questions").
21. **Where work happens in desktop tools or text, ask whether user-interaction logs or text-derived event logs are feasible and acceptable to the people recorded** — Map — routines for automation candidates; logs from conversations — LENO-2020 (abstract: UI logs to discover routines); KECHT-2026 (abstract: event logs from customer-service conversations); PMMANIFESTO-2012 (events should be "safe," privacy addressed). *(adapted)*
22. **Pair the mined or measured picture with walkthroughs, to learn why** — Map and Diagnose — causes behind rework and delay that logs only show as patterns — PMMANIFESTO-2012 (GP6 and project stages: data from systems and domain experts); LEI-ADMIN-ND. *(adapted)*
23. **Record a baseline on real cases before any tool is switched on (cycle time, touches, rework, errors), and compare after** — Measure and Control — whether the change helped; protects against felt versus measured gains — WIKI-DMAIC-2025 (Measure); METR-2025 (abstract: forecast 24%, post-hoc belief 20%, measured +19% time).
24. **Test the measurement system: have two people classify the same ten items as defect or not** — Measure — unreliable definitions of "defect," "done" or "rework" — WIKI-DMAIC-2025 (Measure: suitability of measurement systems). The ten-item test is an adaptation. *(adapted)*
25. **Plot cycle time over time with control limits before reacting to one bad week** — Measure and Control — chance versus assignable variation, so teams do not chase noise — NIST-CTRL-ND (section 6.3.1).
26. **Write the control plan: metric, owner, review rhythm, and what to do when the metric moves out of range; include automated steps** — Control — drift in both human and automated steps — WIKI-DMAIC-2025 (Control: control chart and response plan); LEI-ETHINGTON-2026 (monitoring data-intensive processes).
27. **Stabilise and standardise before improving: "is there a standard way this is done today?"** — Plan — gains lost on an unstable base; a standard to measure against and to specify AI output against — LEI-KAIZEN-ND; LEI-STDWORK-ND (benefits: baseline for improvement).
28. **Put the problem, analysis, countermeasures, owner and evidence of effect on one A3 page** — Plan — whether the case is understood and who owns it — LEI-A3-ND.
29. **After measuring the current process, run a catalogue of redesign heuristics rather than brainstorming from zero** — Reimagine to Prioritize — candidate redesigns tied to measured weaknesses — NETJES-2007 (approach: model, measure, apply best practices; cites 29 practices); MANSAR-2007 (abstract: most popular heuristics).
30. **Start with a small group, one project each, then widen** — Plan — controlled experimentation and early evidence before rollout — HBSWK-2007 (section "Wipro Gains Efficiency": 8 of 10 initial projects showed more than 10% efficiency gain).
31. **Give each team a sustaining mechanism after a kaizen event: peer learning, responsibility inside and outside the work area, and acceptance of changes** — Plan and Control — why event gains fade — GLOVER-2015 (abstract). Evidence is from manufacturing.
32. **When AI removes someone's task, name the value-added / incidental / waste logic and the new role they take on** — Plan — resistance from people who see their craft removed — LEI-HEATON-2026 (discussion highlights: "negative reaction", "fear of AI taking jobs").

---

## 4. Question bank

Scope tags: **[team]**, **[unit]**, **[org]**. Stage tags where they matter: *pre-pilot*, *pilot*, *scaled*.

### Map

- [team] What goes in, from whom, and what comes out, to whom? Who is the customer of this step? (SIPOC)
- [team] Walk me through the last three cases from request to done. Where did each wait?
- [team] What was last month's actual volume, including the worst week? How many were returned or reopened?
- [team] How do you decide when a piece of work has started and when it is finished? (the definition of workflow; KANBAN-GUIDE-2025)
- [team] How much of the day is spent on the work itself and how much on searching, reformatting, chasing, reporting? (value, incidental, waste)
- [unit] Which systems record case ID, activity and time for this process? Who owns the data? Can we get an extract? (PMMANIFESTO-2012 GP1)
- [unit] Where does the real work happen outside systems (email, chat, spreadsheets, documents)? Can we get a sample?
- [unit] What are the hand-offs between teams, and what does each receive from the one before?
- [unit] *pre-pilot* Which question about this process would you want the data to answer? (GP2)
- [org] Which of these processes cross units, and who owns the end-to-end result?
- [org] Where is the work done that no system records, and where is that most costly?
- [org] *scaled* Do the units use the same definitions of "done," "rework" and "defect"? If not, what would it take to compare them?

### Diagnose

- [team] Where does work sit longest? Who is waiting for whom?
- [team] What is the oldest open item, and why?
- [team] Which step has people booked solid? What happens to waiting time when a busy week hits?
- [team] How often does work come back? What are the top three reasons?
- [team] What would happen if we stopped doing this step? Who would notice? (should it exist at all)
- [unit] Where does work pile up in front of someone, and who after them has nothing to do? (constraint)
- [unit] Which demand arrives only because something earlier went wrong or was unclear? (failure demand)
- [unit] If this step were twice as fast, what would the next step see? (constraint test)
- [unit] *pre-pilot* Who checks the output of an AI step, how long does that take, and what happens when it is wrong?
- [org] Where are people or experts used on work that does not need them? (non-utilized talent)
- [org] Which of the eight wastes does leadership currently measure, and which are invisible in the reports?
- [org] *pilot* How do people say the tool helped, and what do timestamps and counts say? Do they match? (METR-2025)

### Prioritize

- [team] Which of these problems costs the most time, error or customer pain? How do you know?
- [team] Which fix would the team need nobody else's approval for?
- [unit] Which candidate change speeds up the constraint, and which speeds up something before it? (PEX-DUMAS-2025; LEI-PEPERKAMP-2026)
- [unit] Which change removes work, which speeds up work, and which only moves it?
- [unit] Is there a stable standard for the step we want to improve or automate? (LEI-KAIZEN-ND)
- [unit] *pre-pilot* What baseline measure would convince a skeptic that this worked?
- [org] Which candidates need data we do not have? Which can start with what exists?
- [org] *scaled* Which units' fixes depend on the same shared constraint (a review team, a system, a scarce specialist)?
- [org] What is the rework or failure demand at the front end across units, and which units are worst?

### Plan-and-control

- [team] Who owns the metric after the change, and how often is it looked at?
- [team] What number would tell us the new way is slipping? What do we do then?
- [team] Who is trained and who is the first person to try it, and who is next?
- [unit] *pilot* Which cases are in the pilot, and what are the same cases doing in the old way for comparison?
- [unit] What happens to the people whose task goes away? What do they do instead? (LEI-HEATON-2026)
- [unit] How will we know if an automated step drifts, such as after a system change or a change in inputs? (LEI-ETHINGTON-2026; IDM-ROBOCORP-2022)
- [org] *scaled* Who reviews the control charts across units, and what triggers a cross-unit response?
- [org] How do improvement ideas from frontline teams reach the plan? (kaizen; GLOVER-2015)
- [org] When a pilot ends, what is the rule for scale, stop or rework?

---

## 5. Common traps

| # | Trap | Why it happens | How to avoid | Evidence |
|---|---|---|---|---|
| 1 | **Automating waste** | A task is visible and tedious, so someone automates it without asking whether it should exist. Automated waste becomes invisible and runs on. | Ask "should this exist" first; map the value stream; apply the lean principles before the tool. | LEI-ETHINGTON-2026 (practitioner argument, with an anecdote of automating a monthly task). The Drucker quote is cited there. |
| 2 | **Speeding up a non-bottleneck** | AI makes one step much faster; the system's output is set by another step. | Find the constraint first; test each proposal against it. | LEI-PEPERKAMP-2026 (argument on code review load); PEX-DUMAS-2025 (automating a bottleneck "may simply shift the constraint downstream"); TOCI-TOC-ND. |
| 3 | **Resource efficiency mistaken for flow efficiency** | Utilization looks good; elapsed time is mostly waiting. Near-full booking multiplies queues. | Measure elapsed vs. active time and WIP; look at utilization at the busy step. | LEI-PEPERKAMP-2026; KANBANU-LITTLE-2022; WIKI-KINGMAN-2025. |
| 4 | **Overproduction freed by AI** | Freed time is filled with extra output ("gold-plating," digital inventory). | Pull system: tie output to what the next step or customer needs. | LEI-PEPERKAMP-2026 (section "The Danger of Idle Hands"); PEX-DOWNTIME-2015 (Overproduction). |
| 5 | **Felt gains instead of measured gains** | People sincerely believe the tool helped. | Baseline and compare on real cases. | METR-2025 (24% expected, 20% believed, +19% measured; software developers, adjacent). Counter-evidence of measured gains exists in a different setting: customer support +14% issues resolved per hour (NBER-BRYNJOLFSSON-2023), so the answer varies by setting. |
| 6 | **AI output that needs rework** | Output looks finished but needs correcting, and the checking falls on others. | Count rework and checking time as part of the process cost; include verification in the design. | HCAMAG-WORKDAY-2026 (vendor survey: about 37% of time saved consumed by rework); HBR-WORKSLOP-2025 (introduction only read; the article's finding was not verified). |
| 7 | **Pilots with no baseline and no owner** | Success is defined as usage or demos. | Baseline first; name an owner and the control metric. | MIT-NANDA-2025 (preliminary: only 5% of custom enterprise AI tools reach production, section 3.2; the report notes that ROI measurement is complicated, section 8.2); BCG-GAP-2025 (p. 6: some firms "experiment too widely," spreading resources over "scores of complex workflows"). Both are survey-based. |
| 8 | **Process mining without a question or without usable data** | Tool first, scope later; logs are low quality or missing for knowledge work. | State the question; rate the log; accept that knowledge work often needs text-derived or manual discovery. | PMMANIFESTO-2012 (GP2; Table 1: logs at the lowest levels are "typically problematic"); KECHT-2026 (evidence buried in emails, chats, documents). |
| 9 | **Diagnosis without redesign capacity** | Mining finds the inefficiency; deciding what to change is manual, expert work. | Plan for facilitated redesign; use heuristic catalogues. | KECHT-2026 (abstract); NETJES-2007. |
| 10 | **Kaizen on an unstable base; gains fade** | Events produce quick wins on a chaotic process. | Stabilise, standardise, then improve; build peer learning and responsibility. | LEI-KAIZEN-ND; GLOVER-2015 (65 events in eight manufacturing firms; adjacent). |
| 11 | **Lean heard as headcount reduction** | Removing tasks looks like removing jobs; people resist. | Frame as removing waste; show new roles. | HBSWK-2007 (Upton: "Some people think lean means 'not fat'"); LEI-HEATON-2026 (anger and fear anecdotes). |
| 12 | **Heavy statistics and rigid method in creative or variable work** | Six Sigma tools designed for repeatable output are applied to judgment work. | Use light baselines and flow measures; structure thinking time, do not remove it. | KENAN-2012 (Staats: "People need time to think"); WIKI-6SIGMA-2026 (criticism section; tertiary, cites commentators on research settings). |
| 13 | **Wrong quality measure** | Counting defects when the customer values something else. | Check what the customer values, and what the defect count misses. | KENAN-2012 (Wipro lean projects had the same number of defects; Staats suggests counting defects may not be the right measure). |
| 14 | **Bots that break when anything changes** | Automation sits on top of screens and rules that change. | Monitor, assign an owner, budget maintenance. | IDM-ROBOCORP-2022 (vendor-sponsored survey: 69% of respondents have broken bots weekly). Older RPA, but the principle carries over to agents. |
| 15 | **Lag measures first** | Cost and budget lead; they hide demand and failure causes. | Lead with demand in customer terms and achievement of purpose. | SEDDON-SWINSCOE-2020 (interview; practitioner position, critical of command-and-control measures). |
| 16 | **Marketing claims passed on as evidence** | Vendor and training blogs repeat unsourced figures. | Check for a named study, population and measure. | PURDUE-OPEX90-2025 (training-vendor piece; its figures are unsourced and not used here). |
| 17 | **Six Sigma and lean programme failure** | Commonly listed failure factors include weak leadership, poor project selection, resistance and ignoring human factors. | Select projects tied to strategy; invest in leadership and change work. | WIKI-6SIGMA-2026 (tertiary: a review of 34 failure factors in 56 papers; WSJ 2010 reporting "more than 60%" project failure, not verified against the original). |

---

## 6. Evidence

Each row: figure, what it measures (source's words where possible), who measured it, provenance, source. Grade scope: most evidence is **adjacent** to lean/six sigma in knowledge-work processes, or about AI in general, so it supports framing, not method effectiveness.

| # | Figure | What it measures | Who / provenance | Source and locator |
|---|---|---|---|---|
| E1 | 95% of organizations "getting zero return"; just 5% of integrated pilots "extracting millions" | Organizations in the study with no measurable P&L impact from GenAI pilots. Sample: review of 300+ public initiatives, 52 interviews, 153 survey responses. Success defined as deployment beyond pilot with measurable KPIs; ROI measured 6 months post-pilot. | MIT NANDA authors, July 2025. Preliminary findings, non-peer-reviewed. The report states the sample may not represent broader patterns and that success definitions varied. Self-reported by respondents. | MIT-NANDA-2025: Notes page; Executive Summary; §8.2 |
| E2 | Only 5% of custom enterprise AI tools reach production | Share of custom enterprise AI tools, in the sample, that reached production. | Same report; same limits. | MIT-NANDA-2025: §3.2 |
| E3 | 5% of firms "achieving AI value at scale"; 60% "not achieving material value at all"; 35% scaling | Firms in BCG's study of "more than 1,250 firms worldwide," classed by their reported AI value. Respondents report on the business area they know best. | BCG Global Study 2025; consultancy survey, self-reported. | BCG-GAP-2025: p. 3; Exhibit 1 (p. 4) |
| E4 | Agents account for 17% of total AI value in 2025; expected to reach 29% by 2028 | Share of AI value attributed to agents in the BCG survey; the 2028 figure is the respondents' expectation. | BCG, self-reported and forecast. | BCG-GAP-2025: p. 3 |
| E5 | Workday: 77% of employees report increased productivity from AI; roughly 37% of time saved is consumed by rework; only 14% consistently net-positive | Survey of 3,200 full-time employees and leaders at organizations with at least US$100 million revenue and 150+ employees (Nov 2025, conducted by Hanover Research). Rework is time spent correcting, clarifying or rewriting AI output. | Workday study, vendor-published; read via trade-press coverage (HCAMag), not the report itself. Self-reported. | HCAMAG-WORKDAY-2026 (paragraphs 2-5) |
| E6 | AI allowed → task completion time +19%; developers forecast -24% before, believed -20% after | Randomized controlled trial: 16 experienced open-source developers, 246 tasks (average 2.0 hours), early-2025 AI tools. Measure: time to complete tasks. | METR, July 2025 (arXiv); independent, peer review status not confirmed. Setting is software engineering. | METR-2025: abstract; §1 |
| E7 | Access to an AI assistant raised issues resolved per hour by 14% on average; 34% for novice and low-skilled workers | 5,179 customer-support agents; productivity measured as issues resolved per hour (baseline mean 2.6). | Brynjolfsson, Li, Raymond; NBER working paper 31161 (Apr 2023, rev. Nov 2023); academic, firm data; not peer-reviewed at that stage. Customer support, adjacent. | NBER-BRYNJOLFSSON-2023: abstract; results section |
| E8 | 8 of 10 initial Wipro lean projects showed more than 10% efficiency improvement; 603 lean projects done or under way by end 2006 of about 1,100 typically running | Wipro's initial pilot projects (efficiency improvement, as reported by HBS summary) and the scale of rollout. | Staats and Upton working paper, summarized by HBS Working Knowledge (2007). Academic, with company data. Software services. | HBSWK-2007: section "Wipro Gains Efficiency" |
| E9 | Lean projects performed better than non-lean projects "for most performance outcomes" | Comparison of lean and non-lean software projects at one firm; archival data and 100+ interviews. | Staats, Brunner, Upton, *Journal of Operations Management* (May 2011), via abstract and a UNC article. Independent academics, one firm. | STAATS-JOM-2011 (abstract); KENAN-2012 |
| E10 | Lean projects had as many software defects as traditional projects | Defect counts in lean vs. traditional Wipro projects. | Same study as E9, as described in KENAN-2012. | KENAN-2012 (paragraph on quality control) |
| E11 | 15-50% reduction in the cost of legal services | The firm's own reported result of lean six sigma in its legal services. Baseline and definition not given. | Self-reported by Seyfarth Shaw people in a podcast description, 2009. | PEX-SEYFARTH-2009 (description) |
| E12 | "More than 160" process maps in five years; "more than 100" legal processes mapped | Seyfarth's own count of maps and of mapped processes (two different statements). | Quoted from firm staff in an undated trade piece. Self-reported. | OPENLAW-ND (the quote from Seyfarth's PMO director on 160+ maps; the firm statement on 100+ mapped processes) |
| E13 | Process mining software spending grew more than 30% in 2024 (39.5% in 2023); US$871.6M revenue in 2023; forecast over US$2B by 2028 | Market spending on process mining platforms. A market-size measure, not an outcome measure. | Gartner 2025 Magic Quadrant as reported by PEX Network. Analyst estimates. | PEX-MQ-2025 (paragraph 4) |
| E14 | 27% of surveyed leaders use process intelligence as a key component of analytics strategy; 12% to support OPEX/transformation; 16% plan to increase investment | Share of respondents in the PEX Report 2025. Sample not described in the article. | PEX Network, via a Dumas article; media-run survey. | PEX-DUMAS-2025 (section "What is process intelligence?") |
| E15 | By 2028, 33% of enterprise software applications will include agentic AI, up from under 1% in 2024; 15% of day-to-day work decisions made autonomously | A Gartner prediction. | Gartner, as quoted by PEX-DUMAS-2025. Prediction, not a measurement. | PEX-DUMAS-2025 (paragraph 1) |
| E16 | 69% of respondents have broken bots at least once per week; 41% say a fix takes over 5 hours | Online survey of RPA users, mostly IT teams, May 2022. | Robocorp-commissioned, vendor-sponsored. RPA, not agents. | IDM-ROBOCORP-2022 |
| E17 | Peer learning, responsibility and acceptance of changes are significantly related to the perceived impact of Kaizen events several months later | Field study of 65 Kaizen events in eight manufacturing organizations. | Glover, Farris, Van Aken, IJPR 2015; academic; manufacturing. | GLOVER-2015 (abstract) |
| E18 | In ABuPrOpt, LLM and simulation produced "plausible redesign options" across five public datasets; in the Process Improvement Copilot study, a "substantial share" of ideas was relevant or actionable | Academic prototypes. Evaluation basis: five public datasets; expert interviews and a workshop at one technology firm. No error rates given in the abstract. | Kecht dissertation, Bayreuth, March 2026; academic; not independent measurement of outcomes. | KECHT-2026 (abstract, RO 2) |
| E19 | **Search-only.** High performers (about 6% of respondents) are nearly three times as likely as others to fundamentally redesign workflows | Per search summary of McKinsey's *State of AI in 2025*: respondents attributing 5%+ EBIT impact to AI. | McKinsey survey, self-reported. Not read in full (page blocked). Kept out of the argument. | MCKINSEY-STATEAI-2025 (search-only) |
| E20 | **Search-only.** 36% of 101 chief procurement officers "very confident" they can redesign their function for AI | Survey figure from a Gartner press release dated 2026-05-19, per search summary. | Gartner survey. Not read (page blocked). | GARTNER-CPO-2026 (search-only) |

**Quality evidence.** No error rates, override rates or parallel-run results were found for AI inside lean/six sigma-style process redesign in knowledge work. The nearest are E6 (time, RCT, software), E7 (productivity, customer support) and E5 (rework, survey). Evidence for lean in knowledge work (E8-E10) predates generative AI.

---

## 7. Worked examples

### 7.1 Process mapping in a law firm (Seyfarth Shaw)

**What changed.** A law firm applied lean six sigma tools (process mapping, kaizen, DMAIC) to legal service delivery, branding the programme SeyfarthLean (PEX-SEYFARTH-2009; OPENLAW-ND).

**How.** The firm picks a type of matter or transaction, gets participants in a room to share processes and best practices, with a project manager facilitating. Each map lays out the phases of a matter and an efficient way to carry them out; the result is a template ("springboard") that includes the tasks, how long each should take and what resources are needed, and is used for staffing and pricing at the start of an engagement. Documents (checklists, templates, prior work) are linked to tasks. A map can take weeks to create (OPENLAW-ND, sections on "springboard" maps).

**Outcomes.** The firm reports a 15-50% reduction in the cost of legal services (PEX-SEYFARTH-2009), and "more than 160" maps in five years (OPENLAW-ND). Both are self-reported; baseline, scope and measure are not given.

**Limits.** Sources date from 2009-2014, are trade pieces or firm interviews, and the open-law piece is undated. Clients' interest in cost control was a driver (PEX-SEYFARTH-2014). Nothing here involves AI. *Relevance:* mapping with practitioners in a room, building reusable templates, and tying maps to pricing are moves an advisor can borrow for professional-services teams.

### 7.2 Lean in software services (Wipro)

**What changed.** A large Indian software services firm trained groups in lean techniques (small dedicated teams, visual control boards, iterative scheduling, value stream mapping) and compared lean and non-lean projects (STRATBIZ-2009; HBSWK-2007).

**How.** It began in 2004 with a core team; each manager adopted a project; 8 of 10 initial projects showed more than 10% efficiency improvement; the firm then rolled out to 603 lean projects completed or under way by the end of 2006 (HBSWK-2007).

**Outcomes.** Lean projects performed better for most outcomes (STAATS-JOM-2011). They were able to identify problems earlier in the cycle (STRATBIZ-2009). Defect counts were similar to traditional projects (KENAN-2012). Each member of the team could see the whole picture through value stream mapping (HBSWK-2007, quote from Staats).

**Limits.** One firm; software services; the researchers listed task uncertainty, process invisibility and architectural ambiguity as reasons lean might not transfer (STAATS-JOM-2011). Some factory tools (the andon cord) do not carry over (HBSWK-2007). *Relevance:* a staged, controlled rollout, with an explicit comparison group, is the pattern to copy.

### 7.3 Illustration (constructed, not a case): AI drafting in front of a review queue

This is an advisor walk-through built from the sources' logic, not a reported case. Suppose a team's reviewers handle drafts and are booked about 80% of the time. With the Kingman approximation and a variability factor of 1, waiting is about 4 times the review time (0.8/0.2). If AI drafting lifts arrivals by 12.5% (to about 90% booking), waiting is about 9 times the review time (0.9/0.1), more than double, with no change in reviewer speed. Above 100% booking the queue grows without limit (WIKI-KINGMAN-2025). The advisor's moves: measure reviewer booking and queue age (moves 8, 9, 11); test the proposal against the constraint (move 14); then decide between adding review capacity, tightening what is sent to review, or using AI on the review step itself, and baseline the result (move 23). LEI-PEPERKAMP-2026 makes the same argument about code review in prose.

### 7.4 Discovering a process that leaves no system log (research prototype)

**What.** Kecht's 2026 dissertation builds a pipeline that takes customer-service conversations, extracts topics and process activities with natural language inference, and exports event logs; a second stage produces object-centric logs, where the fully generative variant gave "coherent and standardized" labels (KECHT-2026, abstract RA 1-2). A Process Improvement Copilot generated improvement ideas from best practices and detected inefficiencies; participants in expert interviews and a workshop at one technology conglomerate rated it useful (RA 3).

**Limits.** Research prototypes; evaluation is on conversation data, five public datasets and one workshop; no outcome measures in production. The abstract stresses that LLM output "must be guided to avoid incorrect or uncontrollable outputs." *Relevance:* for knowledge-work processes in email and chat, text-derived discovery is emerging, and still needs human checking.

---

## 8. Mapping to phases

**Map**
- Tools: SIPOC for scope (ISIX-SIPOC-2025), current-state value stream map with information flow (LEI-VSM-ND, LEI-L2SEE-ND), go-and-see (LEI-ADMIN-ND), real volumes and variation.
- Data-driven discovery: process mining, task mining, text-derived event logs; ask what data exists and its quality first (PMMANIFESTO-2012, LENO-2020, KECHT-2026).
- Unit of work and "started/finished" definitions from Kanban (KANBAN-GUIDE-2025) give a consistent definition of a case across teams. At unit and organization level, shared definitions are what makes roll-up possible.

**Diagnose**
- Flow measures: WIP, throughput, cycle time, age; flow efficiency; Little's Law checks (KANBAN-GUIDE-2025, KANBANU-LITTLE-2022).
- Queue logic (utilization and variability) to explain delay (WIKI-KINGMAN-2025).
- Waste lens: value-creating, incidental, waste; DOWNTIME; rework and failure demand (LEI-7W-ND, PEX-DOWNTIME-2015, SEDDON-SWINSCOE-2020).
- Constraint hunting (TOCI-TOC-ND). New diagnostic question for AI: where is verification capacity? (LEI-PEPERKAMP-2026, DUMAS-AGENTIC-2026).

**Prioritize**
- Rank candidates by whether they act on the constraint, remove waste or only speed a non-bottleneck (PEX-DUMAS-2025, LEI-PEPERKAMP-2026).
- Exploit and subordinate before elevating (TOCI-5FS-ND). "Should this exist" screen (LEI-ETHINGTON-2026).
- Redesign heuristics tied to measured weaknesses (NETJES-2007, MANSAR-2007).
- Caution on evidence for benefit sizing: most outcome figures are self-reported or adjacent (section 6).

**Plan-and-control**
- Baseline and compare design (WIKI-DMAIC-2025 Measure; METR-2025 as the reason).
- Control plan: metric, owner, control chart, response plan, including for automated steps (WIKI-DMAIC-2025, NIST-CTRL-ND, LEI-ETHINGTON-2026).
- Standard before kaizen; sustaining mechanisms; A3 for ownership (LEI-KAIZEN-ND, GLOVER-2015, LEI-A3-ND).
- Staged rollout with a comparison group (HBSWK-2007). People side: reframe roles (LEI-HEATON-2026).
- Execution patterns for human/AI split (triage, human-assisted agent, agent-assisted human, verification; DUMAS-AGENTIC-2026 §4.3).

---

## 9. Sources

All accessed 2026-10-16. Type values: practitioner guide, professional body/standard, consultancy, academic, practitioner case, talk/podcast, media, vendor, tertiary.

| Ref | Title | Publisher / author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| LEI-VSM-ND | Value Stream Mapping (Lexicon) | Lean Enterprise Institute | professional body / practitioner guide | https://www.lean.org/lexicon-terms/value-stream-mapping/ | undated | full |
| LEI-L2SEE-ND | Learning to See (product page; Rother and Shook) | Lean Enterprise Institute | book summary (publisher page) | https://www.lean.org/store/book/learning-to-see/ | undated (book 1999 Shingo Prize per page) | full |
| LEI-7W-ND | Seven Wastes (Lexicon) | Lean Enterprise Institute | professional body | https://www.lean.org/lexicon-terms/seven-wastes/ | undated | full |
| LEI-MUDA-ND | Muda, Mura, Muri (Lexicon) | Lean Enterprise Institute | professional body | https://www.lean.org/lexicon-terms/muda/ | undated | full (background only) |
| LEI-KAIZEN-ND | Kaizen (Lexicon) | Lean Enterprise Institute | professional body | https://www.lean.org/lexicon-terms/kaizen/ | undated | full |
| LEI-STDWORK-ND | Standardized Work (Lexicon) | Lean Enterprise Institute | professional body | https://www.lean.org/lexicon-terms/standardized-work/ | undated | full |
| LEI-A3-ND | A3 Report (Lexicon) | Lean Enterprise Institute | professional body | https://www.lean.org/lexicon-terms/a3-report/ | undated | full |
| LEI-ADMIN-ND | Administration and Support | Lean Enterprise Institute | professional body | https://www.lean.org/explore-lean/administration-support/ | undated | full |
| LEI-WHATISLEAN-ND | What is Lean? | Lean Enterprise Institute | professional body | https://www.lean.org/explore-lean/what-is-lean/ | undated | full |
| LEI-ETHINGTON-2026 | Automation, AI, and the Risk of Doing Things Efficiently That Should Not Be Done at All (E. Ethington) | LEI, The Lean Post | practitioner article | https://www.lean.org/the-lean-post/articles/automation-ai-and-the-risk-of-doing-things-efficiently-that-should-not-be-done-at-all/ | 2026-03-05 | full |
| LEI-PEPERKAMP-2026 | Lean in the Age of AI: Optimizing the Stream, Not the Coder (T. Peperkamp) | LEI, The Lean Post | practitioner article | https://www.lean.org/the-lean-post/articles/lean-in-the-age-of-ai-optimizing-the-stream-not-the-coder/ | 2026-02-18 | full |
| LEI-HEATON-2026 | Past, Present, and Future of Lean and AI (T. Heaton, G. Kim, A. Smalley) | LEI, The Lean Post (podcast summary) | talk / podcast | https://www.lean.org/the-lean-post/articles/past-present-and-future-of-lean-and-ai/ | 2026-07-08 | full (summary of the talk, not the audio) |
| TOCI-TOC-ND | Theory of Constraints of Dr. Eliyahu Goldratt | Theory of Constraints Institute | practitioner guide (consultancy-run) | https://www.tocinstitute.org/theory-of-constraints.html | undated | full |
| TOCI-5FS-ND | Five Focusing Steps | Theory of Constraints Institute | practitioner guide (consultancy-run) | https://www.tocinstitute.org/five-focusing-steps.html | undated | full |
| TOCI-GOAL-ND | The Goal summary (Goldratt, 1984) | Theory of Constraints Institute | book summary | https://www.tocinstitute.org/the-goal-summary.html | undated | full (background only) |
| KANBAN-GUIDE-2025 | The Kanban Guide | Orderly Disruption / D. Vacanti (kanbanguides.org) | professional guide | https://kanbanguides.org/english/ | 2025-05 | full |
| KANBANU-LITTLE-2022 | Exploring Little's Law (KGS 2022 slides) | Kanban University | professional body talk deck | https://kanban.university/wp-content/uploads/2022/09/Exploring-Littles-Law-KGS-2022.pdf | 2022 (upload path 2022/09) | full (text layer partly garbled) |
| WIKI-KINGMAN-2025 | Kingman's formula | Wikipedia | tertiary | https://en.wikipedia.org/wiki/Kingman%27s_formula | page modified 2025-11-15 | full |
| WIKI-DMAIC-2025 | DMAIC | Wikipedia | tertiary | https://en.wikipedia.org/wiki/DMAIC | page modified 2025-10-08 | full |
| WIKI-6SIGMA-2026 | Six Sigma | Wikipedia | tertiary | https://en.wikipedia.org/wiki/Six_Sigma | page modified 2026-10-12 | full |
| NIST-CTRL-ND | 6.3.1 What are Control Charts? (e-Handbook of Statistical Methods) | NIST/SEMATECH | standards body reference | https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm | undated | full |
| NIST-CAP-ND | 6.1.6 Process capability (e-Handbook) | NIST/SEMATECH | standards body reference | https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm | undated | full (background only; formulas) |
| ISIX-SIPOC-2025 | SIPOC diagram | iSixSigma | practitioner guide | https://www.isixsigma.com/sipoc-copis/sipoc-diagram/ | 2025-01-22 | full |
| PEX-DOWNTIME-2015 | The eight deadly lean wastes: DOWNTIME | PEX Network | media / practitioner article | https://www.processexcellencenetwork.com/lean-six-sigma-business-performance/articles/the-8-deadly-lean-wastes-downtime | 2015-08-12 (modified 2024-10-04) | full |
| GOSKILLS-8W-ND | 8 wastes | GoSkills | practitioner guide | https://goskills.com/Lean-Six-Sigma/Resources/8-wastes | undated | partial (first third read; used only for the eighth-waste naming variance) |
| PMMANIFESTO-2012 | Process Mining Manifesto | IEEE Task Force on Process Mining (van der Aalst et al.); in BPM 2011 Workshops, LNBIP 99, Springer | professional body / academic | https://www.tf-pm.org/upload/1580737614108.pdf (landing page https://www.tf-pm.org/resources/manifesto) | written 2011, published 2012 | full (English PDF; table symbols lost in text layer) |
| PEX-DUMAS-2025 | Process intelligence: The foundation of agentic AI success (M. Dumas) | PEX Network | practitioner article by academic | https://www.processexcellencenetwork.com/ai/articles/process-intelligence-agentic-ai/amp | 2025-02-04 | full |
| DUMAS-AGENTIC-2026 | Agentic Business Process Management Systems (Dumas, Milani, Chapela-Campa), arXiv:2601.18833 | University of Tartu | academic (position paper) | https://arxiv.org/pdf/2601.18833v1 | 2026-01-25 | full |
| KECHT-2026 | Artificial Intelligence Along the Business Process Management Lifecycle (C. Kecht, dissertation) | University of Bayreuth | academic | https://epub.uni-bayreuth.de/9065/1/Dissertation_CKecht.pdf | 2026-03 | partial (abstract and front matter read; chapters not) |
| LENO-2020 | Automated Discovery of Data Transformations for Robotic Process Automation (Leno et al.), arXiv:2001.01007 | Univ. of Melbourne / Univ. of Tartu | academic | https://arxiv.org/pdf/2001.01007 | 2020-01-03 | partial (abstract and introduction) |
| BERTI-2024 | PM-LLM-Benchmark: Evaluating Large Language Models on Process Mining Tasks (Berti, Kourani, van der Aalst), arXiv:2407.13244 | RWTH Aachen / Fraunhofer FIT | academic | https://arxiv.org/pdf/2407.13244 | 2024-07-18 | partial (abstract) |
| NETJES-2007 | An Evolutionary Approach for Business Process Redesign (Netjes, Limam Mansar, Reijers, van der Aalst) | TU Eindhoven / Zayed Univ. | academic | https://www.vdaalst.com/publications/p387.pdf | 2007 (per SciTePress path) | partial (abstract and introduction) |
| MANSAR-2007 | Best practices in business process redesign: use and impact (Limam Mansar, Reijers), BPM Journal 13(2) | TU/e research portal | academic | https://research.tue.nl/en/publications/best-practices-in-business-process-redesign-use-and-impact/ | 2007 | partial (abstract and citation page only) |
| HBSWK-2007 | Bringing Lean Principles to Service Industries (J. Hanna on Upton and Staats) | HBS Working Knowledge | practitioner/academic summary | https://www.library.hbs.edu/working-knowledge/bringing-lean-principles-to-service-industries | 2007-10-22 | full |
| STRATBIZ-2009 | Rethinking the Software Development Cycle (summary of Staats/Upton working paper) | strategy+business | media | https://www.strategy-business.com/article/re00077 | 2009 (page shows March 2009 / June 25, 2009) | full |
| STAATS-JOM-2011 | Lean Principles, Learning, and Knowledge Work: Evidence from a Software Services Provider (Staats, Brunner, Upton), J. Operations Management, May 2011 | Penn repository (abstract) | academic | https://repository.upenn.edu/handle/20.500.14332/34579 | 2011-05 (per KENAN-2012) | partial (abstract only) |
| KENAN-2012 | Rethinking Knowledge Work (on Staats' research) | UNC Kenan-Flagler | university news / academic summary | https://www.kenan-flagler.unc.edu/news/rethinking-knowledge-work/ | 2012-01-13 | full |
| HBR-STAATS-2011 | Lean Knowledge Work (Staats and Upton), HBR Oct 2011 | Harvard Business Review | practitioner article | https://hbr.org/2011/10/lean-knowledge-work | 2011-10 | partial (introduction only; paywalled; used only for identification) |
| PEX-SEYFARTH-2009 | Raising the Bar: How Seyfarth Shaw Provides Efficient Delivery of Legal Services through Lean Six Sigma (podcast description) | PEX Network / Six Sigma IQ | practitioner case / talk | https://www.processexcellencenetwork.com/business-process-management-bpm/podcasts/raising-the-bar-how-seyfarth-shaw-provides-efficie | 2009-11-17 | full (description only, not the audio) |
| PEX-SEYFARTH-2014 | The Growing Pains of Legal Transformation (interview with K. Grady) | PEX Network | practitioner case | https://www.processexcellencenetwork.com/business-process-management-bpm/interviews/the-growing-pains-of-legal-transformation-advice-a | 2014-09-10 | partial (first part read) |
| OPENLAW-ND | Six Sigma as Law Redesign | Open Law Lab | practitioner article | https://www.openlawlab.com/?p=1323 | undated | full |
| SEDDON-SWINSCOE-2020 | Interview with John Seddon of The Vanguard Method | Adrian Swinscoe | practitioner interview | https://www.adrianswinscoe.com/2020/01/a-lot-of-organisations-talk-outside-in-but-their-systems-are-not-designed-outside-in-interview-with-john-seddon-of-the-vanguard-method/ | 2020-01-27 | full |
| GOVMETRIC-2026 | The astonishing cost of failure demand | GovMetric | vendor blog | https://govmetric.com/blog/the-astonishing-cost-of-failure-demand-and-why-fixing-it-should-be-your-next-priority | 2026 (date not confirmed in page) | partial (definition and opening only) |
| GLOVER-2015 | Sustainability of rapid improvement (Glover, Farris, Van Aken), Int. J. Production Research 53(13) | RePEc listing | academic | https://ideas.repec.org/a/taf/tprsxx/v53y2015i13p4068-4086.html | 2015 | partial (abstract only) |
| MIT-NANDA-2025 | The GenAI Divide: State of AI in Business 2025 | MIT NANDA (Challapally et al.) | academic-affiliated report | https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf | 2025-07 | full (copy hosted on mlq.ai) |
| BCG-GAP-2025 | The Widening AI Value Gap: Build for the Future 2025 | Boston Consulting Group | consultancy | https://media-publications.bcg.com/The-Widening-AI-Value-Gap-Sept-2025.pdf | 2025-09 | full |
| METR-2025 | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity, arXiv:2507.09089 | METR | academic (RCT) | https://arxiv.org/pdf/2507.09089 | 2025-07 | full (abstract and introduction read) |
| NBER-BRYNJOLFSSON-2023 | Generative AI at Work, NBER WP 31161 | Brynjolfsson, Li, Raymond | academic (working paper) | https://www.nber.org/system/files/working_papers/w31161/w31161.pdf | 2023-04, rev. 2023-11 | full (abstract and key results) |
| HCAMAG-WORKDAY-2026 | AI productivity gains offset by rework costs, study finds (on Workday's study) | HCA Magazine | media (reporting a vendor study) | https://www.hcamag.com/ca/news/general/ai-productivity-gains-offset-by-rework-costs-study-finds/565098 | 2026-02-12 | full (secondary; the Workday report was not read) |
| HBR-WORKSLOP-2025 | AI-Generated "Workslop" Is Destroying Productivity (Niederhoffer et al.) | Harvard Business Review | practitioner article | https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity | 2025-09-22 | partial (introduction only) |
| PEX-MQ-2025 | 5 highlights from Gartner's 2025 Magic Quadrant for Process Mining Platforms | PEX Network | media | https://www.processexcellencenetwork.com/process-mining/articles/highlights-gartners-2025-magic-quadrant-process-mining | 2025-04-22 | full |
| CELONIS-GARTNER-2026 | Celonis named a Leader in the 2026 Gartner Magic Quadrant for Process Intelligence Platforms (page) | Celonis | vendor | https://www.celonis.com/analyst-reports/gartner-process-mining-generative-ai | undated (refers to 2026 MQ) | partial; vendor claim; used only as a frontier signal that the category is now called process intelligence |
| IDM-ROBOCORP-2022 | Broken bots challenge RPA users (on Robocorp's State of RPA survey) | IDM | media (vendor-sponsored survey) | https://idm.net.au/node/13957 | 2022-07-08 | full |
| PURDUE-OPEX90-2025 | The Future of Lean Six Sigma: How Automation, AI, and Synthetic Agents Are Redefining Process Excellence | OpEx90 (training vendor; hosted on tap.purdue.edu) | vendor blog | https://tap.purdue.edu/media/iyifzbij/the-future-of-lean-six-sigma_-how-automation-ai-and-synthetic-agents-are-redefining-process-excellence.pdf | 2025-04-28 | full; figures unsourced, not used as evidence |
| UCSD-PALOOZA-2025 | Process Palooza Podcast Ep. 8: Lean Six Sigma vs. AI | UC San Diego | talk / podcast | https://processpalooza.ucsd.edu/_files/Process-Palooza-Podcast_Ep-8_Transcript.pdf | 2025-04 (recorded before the 24 April webinar) | full (transcript; used for the "methodology vs. machine, partners" framing and a critical-thinking concern) |
| MCKINSEY-STATEAI-2025 | The state of AI in 2025: Agents, innovation, and transformation | McKinsey | consultancy | https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-state-of-ai-2025 | 2025 | **search-only** (page blocked) |
| GARTNER-CPO-2026 | Gartner Survey Shows Just 36% of Chief Procurement Officers Are Very Confident in Ability to Redesign Function for AI | Gartner | consultancy / analyst press release | https://gcomdr.pdo.aws.gartner.com/en/newsroom/press-releases/2026-05-19-gartner-survey-shows-just-36-perecent-of-chief-procurement-officers-are-very-confident-in-ability-to-redesign-function-for-ai | 2026-05-19 | **search-only** (page blocked) |

**Source count.** 57 refs: 55 opened and read (in full or in part, as marked) and 2 search-only. About 35 of them carry claims used above; the rest are background (for example LEI-MUDA-ND, NIST-CAP-ND, TOCI-GOAL-ND, GOSKILLS-8W-ND). By type: professional body, standards and practitioner guides 19; academic and research 13; consultancy or analyst 3 (BCG read; McKinsey and Gartner search-only); practitioner articles, cases, interviews and podcasts 12; media, vendor and tertiary references 10.

---

## 10. Gaps

- **No independent evidence of lean/six sigma combined with AI** in knowledge work or professional services. Practitioner pieces (LEI, PEX, UCSD podcast) are argument and anecdote; the training-vendor piece (PURDUE-OPEX90-2025) gives figures without sources.
- **No primary study of flow efficiency in knowledge work.** The flow-efficiency figures read are from a training exercise (KANBANU-LITTLE-2022). Commonly repeated ranges for software or office flow efficiency were not traced to a study and are left out.
- **Failure-demand percentages (Vanguard/Seddon) are inconsistent across sources** and were seen only in search summaries, so no figure is stated. The interview read (SEDDON-SWINSCOE-2020) gives a hypothetical ("you may realise you've got 60% failure demand"), not a measurement.
- **Professional-body guidance is thin.** ASQ and iSixSigma main pages, ISO 13053, IASSC and the ABPMP BPM CBOK were blocked or not reached. DMAIC phase content relies on a tertiary reference (WIKI-DMAIC-2025). NHS QSIR process-mapping pages were not reachable.
- **Blocked or paywalled major publications:** McKinsey State of AI 2025 (search-only), Gartner press releases (search-only or blocked), RAND's AI project-failure report, BCG's 2024 "Where's the Value in AI," the HBR articles (introductions only), the Harvard "jagged frontier" paper. A planned Harvard Law case on SeyfarthLean failed on a certificate error and was not read.
- **Web-search budget ran out mid-task.** Planned follow-ups not done: Dumas's *Fundamentals of BPM* chapters on discovery and redesign (the Springer pages were blocked), the Robotic Process Mining paper, Kingman applied to office work, Staats and Upton's *Journal of Operations Management* full text, and more 2025-2026 process-mining-plus-AI practitioner case write-ups. Recommended for a follow-up pass.
- **Dated or self-reported professional-services cases.** Seyfarth sources are 2009-2014 and self-reported; no recent professional-services case with before/after data was found. One arXiv reference first tried for RPA (a different paper) was discarded after checking it was wrong; the RPA suitability literature is therefore not covered.
- **Process mining outcome data is vendor-sourced.** No independent measure of process-mining-driven improvement was found; PEX-MQ-2025 gives market size only. Vendor "touchless" and rework claims seen in search results were not verified and are not used.
- **Kaizen evidence is from manufacturing** (GLOVER-2015) and was seen only as an abstract. No knowledge-work kaizen study was found.
- **Wipro full paper** was read through abstract and two secondary summaries. The reported "efficiency" measure behind "8 of 10 projects more than 10%" is not defined in the summary.
- **Dumas, Kecht and Berti** are academic prototypes and position papers; they signal direction and do not show production outcomes.

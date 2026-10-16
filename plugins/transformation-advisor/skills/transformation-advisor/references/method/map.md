# Map (phase 2)

Read this on entering Map. It makes the current work visible: at team level the processes and steps, with real
numbers; at unit or organization level the value chain and the units that need their own plan. Interview craft is in
`interviewing.md`; splitting into units is in `breakdown-and-rollup.md`. Source keys in brackets are listed in §8.
Tags: **[T]** individual or team, **[U/O]** unit or organization, **[all]** any scope.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [Expert moves](#4-expert-moves)
5. [Common traps](#5-common-traps)
6. [Worked example](#6-worked-example)
7. [Output](#7-output)
8. [Sources](#8-sources)

## 1. Goal and exit criteria

**Goal.** Replace the described process with the performed one. What people say about their work and what they do
differ, partly because memory fails and partly because people describe the rule, not the practice [HOLLNAGEL-2017].
An AI design built on the described process fails on the real one.

**Exit at team level [T]** when, for each process chosen in Frame (one to three):
- The **customer** of the process and its **output** are named, and the **trigger** and the point where work is "done" are agreed.
- Steps run trigger → steps → handoffs → output, each with: who does it, **work type** (vocabulary id), inputs and
  outputs, systems, **hands-on time** and **elapsed time**.
- **Volume** is known for last month (and the worst week), with a **rework or return rate** and the share of work off the standard path.
- **Workarounds, private tools, tacit checks and judgment points** are captured for the steps that matter.
- Every number carries a label: **reported** (an estimate), **from record** (a report, tracker or log) or **observed** (a sample timed or counted).
- The user has heard the map played back and corrected it; open gaps are listed.

**Exit at unit or organization level [U/O]** when:
- The **value chain** is laid out as stages → processes → key steps, starting from the archetype's `value-chain.md`.
- Each stage has an owner (role), rough size (people, volume), main systems, work-type mix and known AI use.
- **Shared definitions** are agreed for "done", "rework" and two or three common measures, so units can be compared and rolled up [KANBAN-GUIDE-2025].
- Gaps between documented and actual practice, and between teams doing the same work differently, are logged.
- The **units** that need their own plan are created (`breakdown-and-rollup.md`).

## 2. How to run it

**Team level [T]**
1. **Bound the process.** If scope is arguable, sketch who supplies inputs, what comes in, the main steps, what goes
   out and who receives it (a SIPOC, kept to one screen) [ISIX-SIPOC-2025].
2. **Fix the start and the end.** Ask what starts a piece of work and when it counts as finished.
3. **Walk through the last real instance,** not the usual one. Keep asking "and then what?" until the output is
   delivered [NNG-NIELSEN-2010].
4. **Ask for the artifact:** the file, email, template, checklist or tracker. For uploaded documents, use subagents:
   delegate one subagent per document with the `analyze-document` brief, in parallel. If you cannot start subagents,
   read each document yourself, one at a time. Mark everything as stated or inferred, and play it back.
5. **Quantify,** always sourcing the number (§3, M8–M14). Prefer last month's records to estimates.
6. **Find the variations:** the standard path, then what triggers the others, then one time it went well and one time it went badly [NNG-ROSALA-2020].
7. **Find the hidden work:** workarounds, private spreadsheets, checks no procedure mentions, rules of thumb (M15–M20).
8. **Tag each step with a work type** from the vocabulary (review-assurance, transaction-processing, expert-judgment,
   research-synthesis, document-production, client-interaction, coordination-scheduling, data-reporting,
   software-systems, physical-field).
9. **Only then ask the AI lead-in questions** (M21–M24). People cannot reliably say where an unbuilt tool would help;
   ask about tasks they have just described [NNG-NIELSEN-2010].
10. **Play back** each process in your own words and ask what is wrong. Offer to send the written map for correction
    later [BIRT-2016]. Write the map (§7).

**Unit or organization level [U/O]**
1. Show the archetype's value chain and ask the leader to confirm, merge or split stages.
2. For each stage, ask owner, people, volume, systems, main pain and known AI use (M25–M28).
3. Ask where teams do the same work differently and where documents and practice differ.
4. Agree shared definitions and common measures before any unit is planned.
5. Create units for the parts that need their own plan (`breakdown-and-rollup.md`).

**Depth by journey stage.** *Curious:* one process, five to seven steps, rough numbers labelled reported. *Experimenting:*
the shared workflow you want to change, quantified from records. *Adopting:* full quantification, data sources and
system logs for the chosen processes. *Scaling and AI-native:* compare across units on shared measures; consider
process mining where logs exist (move 13).

## 3. Question bank

Plain wording, one question at a time. The bracketed text is a placeholder for the user's own unit of work.

| # | Question | Scope |
|---|---|---|
| | **Walk-through** | |
| M1 | Think of the last [piece of work] you finished. What set it off? | [T] |
| M2 | Walk me through what happened, from that moment to when it was done. | [T] |
| M3 | And then what? Who or what did you need at that point? | [T] |
| M4 | What did you receive, in what form, and what did you pass on, to whom? | [T] |
| M5 | Could you show me the actual file, email or tracker? | [T] |
| M6 | How was that one different from the one before? | [T] |
| M7 | Think of a time this went especially well. What made the difference? And a time it went badly? | [all] |
| | **Quantify (always source the number)** | |
| M8 | How many of these did your team finish last month? Can we look at the record together? | [all] |
| M9 | What was the busiest week like, compared with a normal one? | [all] |
| M10 | For that last one, how long did you actually work on it, and how long did it sit waiting? | [T] |
| M11 | Across the last ten, what was the quickest, the typical and the slowest? What made the slowest slow? | [T] |
| M12 | How many people touched it, and how many times did it change hands? | [T] |
| M13 | What share comes back to be corrected or redone? What caused the last one? | [all] |
| M14 | Where does that number come from: a report, a sample, or a feel? | [all] |
| | **Hidden work and judgment** | |
| M15 | What did you notice that told you to do it that way? | [T] |
| M16 | What do you check that is not written in any procedure? | [T] |
| M17 | Where do you step outside the official process or tool, and why? | [T] |
| M18 | Is there a spreadsheet, template or note that only you use? | [T] |
| M19 | What rule of thumb do you use to decide [the judgment step]? | [T] |
| M20 | What would someone new get wrong here, and how long before they stop? | [all] |
| | **AI lead-in (ask last; feeds Diagnose)** | |
| M21 | Which steps are mostly looking things up, copying, formatting or chasing, and which depend on your judgment? | [T] |
| M22 | If a capable colleague did this step for you, what would you check before relying on it? | [T] |
| M23 | Have you tried an AI tool on this step? What did you have to fix? | [T] |
| M24 | For each of these tasks, how much would you want AI to do it, and how much of your own involvement would you keep? | [T] |
| | **Unit and organization** | |
| M25 | Which systems record each piece of work, with an identifier and dates for each step? Who owns that data? | [U/O] |
| M26 | Where does the real work happen outside systems: email, chat, spreadsheets, documents? | [U/O] |
| M27 | Which processes are shared between teams, and where do teams do the same work in different ways? | [U/O] |
| M28 | Who keeps process documents current, and when were they last checked against practice? | [U/O] |
| M29 | Do your teams use the same meaning of "done", "redone" and "error"? If not, what would it take? | [U/O] |

## 4. Expert moves

| # | Move | When | What it reveals |
|---|---|---|---|
| 1 | **Ask for the last real instance, not "how do you usually do it"** | Any process | The real sequence, tools and detours; "usually" returns the idealized workflow [NNG-NIELSEN-2010] |
| 2 | **Ask for last month's actual volume with the worst week,** and pull the record during the conversation | Every process | Variation and hidden rework that a typical week hides. Recall is weak data: a review of informant-accuracy studies found about half of recalled reports wrong in some way (adjacent evidence, mostly recalled events) [BERNARD-1984] |
| 3 | **Record two times per step: hands-on and elapsed** | Every step | Where work waits rather than gets worked; feeds flow efficiency in Diagnose [LEI-VSM-ND] |
| 4 | **Pull four flow numbers per workflow:** items in progress, items finished per week, time from start to finish, and age of each open item | Team level, where a tracker exists | Stuck work, true load, items older than the service promise [KANBAN-GUIDE-2025] |
| 5 | **Ask for best, typical and worst case times,** then what made the worst one worst | Estimating effort | Optimism in estimates and the causes of tail delay. In the classic planning-fallacy study, students predicted 33.9 days on average and took 55.5 [WIKI-PLANNING] |
| 6 | **Follow one item end to end across teams,** not one team's slice | Cross-team flows | Handoffs, waits and steps no team owns [LEI-GEMBA] |
| 7 | **Ask for the standard path, then the variations and their triggers** | Branching work | The real branching logic and exception rate [NNG-FLAHERTY-2020] |
| 8 | **Ask what they do outside the system and which other sources they consult** | Mapping and diagnosing | Workarounds and private checks that mark where the formal process is wrong [ALTER-2014; NNG-FLAHERTY-2020] |
| 9 | **Use a decision walk-through for judgment steps:** pick one case, build its timeline, split it into decision points, ask what cues were used at each | Review, triage, pricing, risk steps | The tacit rules an agent would need written down [AHRQ-CDM] |
| 10 | **Watch the work where you can** (screen-share or a recorded walk-through), and switch explicitly from talking to showing | High-value or disputed steps | Steps people do not mention. In one practitioner's insurance data-entry project, three specialists described copy-and-paste; observation showed extra cross-referencing and habitual saving none had mentioned [NNG-FLAHERTY-2020] |
| 11 | **Label every number reported, from record or observed** | All numbers | How far to trust the baseline; self-reported AI use differed from observed use in one vendor study (65% / 35% augment / automate described, 47% / 49% observed) [ANTHROPIC-INTERVIEWER-2025] |
| 12 | **Ask the leader for the process as they believe it runs, then test it with those who do the work; treat the gap as a finding** | [U/O] | Where workarounds and cheap wins live [HOLLNAGEL-2017] |
| 13 | **Before promising process mining, ask which system records case, activity and timestamp, and what question the data should answer** | [U/O], Adopting and above | Whether usable logs exist; question-first extraction avoids "mine everything" projects [PMMANIFESTO-2012] |
| 14 | **Where work lives in email and documents, consider text-derived logs only if the people recorded accept it** | Knowledge work with no system log | Research prototypes build event logs from conversations, but output needs human checking [KECHT-2026; PMMANIFESTO-2012] |
| 15 | **Agree shared definitions of done and rework across units before comparing them** | [U/O] | Whether roll-up will be possible at all [KANBAN-GUIDE-2025] |
| 16 | **Keep a private coverage list:** trigger, inputs, steps, handoffs, volumes, times, exceptions, checks, tools, workarounds, judgment points, outputs. Ask the next question from the gaps | Every process | Completeness without reading a script (practitioner extension; see `interviewing.md`) |

## 5. Common traps

| Trap | Why it happens | How to avoid it |
|---|---|---|
| Mapping the idealized process | "How do you usually..." invites the rule | Anchor on the last instance; ask for variations [NNG-NIELSEN-2010] |
| Trusting recalled numbers | Memory fades; estimates are optimistic | Source every number; pull records; use ranges [BERNARD-1984; WIKI-PLANNING] |
| Mapping only the step someone wants to automate | The visible, tedious step attracts attention | Map the whole flow from trigger to customer; value hides in handoffs and waits |
| Asking "where would AI help?" early | People cannot picture unbuilt tools and will invent answers | Map tasks first; ask AI questions last, about tasks just described [NNG-NIELSEN-2010] |
| The leader's account as the map | Leaders see work as imagined | Test with those who do the work [HOLLNAGEL-2017] |
| Missing hidden AI use | Stigma; unapproved tools | Ask with normalising words (`interviewing.md`) |
| Process mining without a question or data | Tool first, scope later | Question first; check the log exists and its quality [PMMANIFESTO-2012] |
| Over-mapping at early stages | Thoroughness | Curious: one light process; save depth for what will be changed |
| Units compared on different definitions | Each team counts its own way | Agree definitions before planning units |

## 6. Worked example

*Illustrative, continuing the audit practice; steps and pain points from the assurance controls-testing module.* The
advisor maps testing of one key control on a recent engagement with a senior and a manager. The senior shares the
evidence tracker (from record) and the advisor plays back the flow.

| Step | Who | Work type | Hands-on | Elapsed | Notes (label) |
|---|---|---|---|---|---|
| Evidence request to the client | Senior | coordination-scheduling, client-interaction | 1 h | 6 days | "About one in four requests needs a second chase" (reported). The module cites an estimate of about one in five wrong first time, from a vendor CEO [CPAPA-ZANIN] |
| Sample selection | Senior | data-reporting | 0.5 h | same day | Static list from last year (from record) |
| Test each sample attribute | Staff | review-assurance | 6 h | 3 days | Screenshots and exports in mixed formats (observed on screen-share) |
| Deviation evaluation | Senior | expert-judgment | 1 h | 2 days | Rule of thumb: "missing support is not a failure until the client has had two chances" (tacit) |
| Documentation | Staff | document-production | 2 h | 1 day | Private template for tick-marks (workaround) |
| Manager review | Manager | review-assurance | 1 h | 8 days | Waits behind other files in the season (reported; tracker shows 6–11 days) |

Hands-on time is about 11.5 hours against about 20 days elapsed. The Frame hypothesis "review is the bottleneck" now
has support from the tracker, to be tested in Diagnose. The senior also mentions that a staff member pastes evidence
into the firm's chat assistant to summarise it, with no review step (hidden AI use, noted without judgment). Playback:
"Request, chase, select, test, judge deviations, document, then a long wait for manager review. Did I miss anything?"
The manager adds a step: re-performing two samples before sign-off.

## 7. Output

Write a **Map** section in the plan body. Field names line up with `opportunities.yaml` (`process`, `work_types`) so
Reimagine and Prioritize can reuse them.

For each process [T]:
- **Header:** process name, customer, trigger, output, definition of done, volume last month (label), worst week (label).
- **Step table:** step, who (role), work type id, inputs, outputs, systems, hands-on time, elapsed time, rework or
  return rate, exceptions and triggers, workarounds and private tools, judgment points and rules of thumb, checks, AI use today. Each number labelled.
- **Totals:** hands-on versus elapsed time; number of handoffs; share off the standard path.
- **Gaps and hypotheses:** what is still unknown; what Diagnose should test.

At unit or organization level [U/O]:
- **Value chain table:** stage, processes, owner (role), people, volume, systems, work-type mix, known AI use, main pain.
- **Shared definitions:** done, rework, defect, and the two or three common measures.
- **Documented-versus-actual gaps** and cross-team variation.
- **Units:** the `units` list in frontmatter (`id, name, owner, wave, status`) and a brief per unit (`breakdown-and-rollup.md`).

Then set `phase_completed: 2`, `next_phase: 3`, tick "Map" in the progress checklist and update `updated`.

## 8. Sources

- **AHRQ-CDM**: US Agency for Healthcare Research and Quality, *Critical Decision Method* (government toolkit, undated). https://digital.ahrq.gov/health-it-tools-and-resources/evaluation-resources/workflow-assessment-health-it-toolkit/all-workflow-tools/critical-decision-method
- **ALTER-2014**: Alter, *Theory of Workarounds*, Communications of the AIS 34 (academic, 2014; abstract read). https://aisel.aisnet.org/cais/vol34/iss1/55/
- **ANTHROPIC-INTERVIEWER-2025**: Anthropic, *Introducing Anthropic Interviewer* (vendor research, 2025-12-04). https://www.anthropic.com/research/anthropic-interviewer
- **BERNARD-1984**: Bernard et al., *The Problem of Informant Accuracy*, Annual Review of Anthropology 13 (academic review, 1984). https://bebr.ufl.edu/sites/default/files/Bernard%20et%20al.%20-%201984%20-%20The%20Problem%20of%20Informant%20Accuracy%20The%20Validity%20of.pdf
- **BIRT-2016**: Birt et al., *Member checking*, Qualitative Health Research 26(13) (academic, 2016). https://kclpure.kcl.ac.uk/ws/files/52859539/Member_checking_a_tool_BIRT_Accepted_2016_GREEN_AAM.pdf
- **HOLLNAGEL-2017**: Hollnagel, *Can we ever imagine how work is done?*, HindSight 25, EUROCONTROL (practitioner magazine, 2017). https://www.skybrary.aero/sites/default/files/bookshelf/3934.pdf
- **ISIX-SIPOC-2025**: iSixSigma, *SIPOC diagram* (practitioner guide, 2025-01-22). https://www.isixsigma.com/sipoc-copis/sipoc-diagram/
- **KANBAN-GUIDE-2025**: Vacanti, *The Kanban Guide* (professional guide, 2025-05). https://kanbanguides.org/english/
- **KECHT-2026**: Kecht, *Artificial Intelligence Along the Business Process Management Lifecycle* (dissertation, University of Bayreuth, 2026-03; abstract read). https://epub.uni-bayreuth.de/9065/1/Dissertation_CKecht.pdf
- **LEI-GEMBA**: Lean Enterprise Institute, *Gemba / Gemba Walk* (lexicon, undated). https://www.lean.org/lexicon-terms/gemba/
- **LEI-VSM-ND**: Lean Enterprise Institute, *Value Stream Mapping* (lexicon, undated). https://www.lean.org/lexicon-terms/value-stream-mapping/
- **NNG-FLAHERTY-2020**: Nielsen Norman Group, *Contextual Inquiry* (practitioner article, 2020-12-06). https://www.nngroup.com/articles/contextual-inquiry/
- **NNG-NIELSEN-2010**: Nielsen, *Interviewing Users*, Nielsen Norman Group (practitioner article, 2010-07-25). https://www.nngroup.com/articles/interviewing-users/
- **NNG-ROSALA-2020**: Rosala, *The Critical Incident Technique in UX*, Nielsen Norman Group (practitioner article, 2020-01-26). https://www.nngroup.com/articles/critical-incident-technique/
- **PMMANIFESTO-2012**: IEEE Task Force on Process Mining, *Process Mining Manifesto* (professional body, 2012). https://www.tf-pm.org/resources/manifesto
- **WIKI-PLANNING**: Wikipedia, *Planning fallacy*, citing Buehler et al. 1994 (secondary, accessed 2026-10-16). https://en.wikipedia.org/wiki/Planning_fallacy
- Assurance steps and pain points: `archetypes/assurance/modules/controls-testing.md` §2 (PBC first-time-right estimate [CPAPA-ZANIN]).

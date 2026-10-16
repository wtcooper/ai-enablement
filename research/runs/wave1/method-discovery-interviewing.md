# Method topic: process-discovery-interviewing

**Run date:** 2026-10-16. **Stream:** M (method topic). **Phases fed:** interviewing, onboarding, frame, map.

**Topic focus:** How expert consultants, business analysts and transformation leads run discovery interviews and workshops to understand current processes and find improvement opportunities, and how to adapt this for AI opportunity discovery, including AI-guided (conversational) interviews and an AI interviewer that asks one question at a time.

**Conventions.**
- Refs follow `AUTHOR-SHORT-YYYY`; locators are sections, page numbers or table names as read.
- Access is marked `full` (body text read) or `search-only` (abstract, publisher page or search-result summaries only).
- "Practitioner extension" marks a move or question that I derived from the sources but that no source tested directly.
- "Interpretation" marks my inference from a source, not the source's claim.
- Statistics always say what they measure and who measured them.

---

## 1. Summary

- **Experts anchor on concrete, recent episodes and observed work, not on "how do you usually do it".** Asking for a typical workflow gets an idealized version without the shortcuts and deviations (NNG-NIELSEN-2010). In one NN/g example, three specialists described a copy-and-paste step. Observation later showed extra cross-referencing and habitual saving that they had not mentioned (NNG-FLAHERTY-2020). Critical-incident questions, "last time" questions and contextual inquiry exist to get around this.
- **Recall and estimates are weak data, so triangulate.** A 1984 review of retrospective-report studies concluded that on average about half of what informants report is probably incorrect in some way (BERNARD-1984). Experts therefore ask for records, sample real items, observe, and pair interviews with documents and system data. Note that the review mostly covers recalled communications and events, not process volumes (adjacent evidence).
- **Different people see different things.** Leaders describe work as imagined; the people doing it know work as done (HOLLNAGEL-2017). Senior professionals give practised, general answers and open up when the interviewer shows preparation and persistence (EMPSON-2018). Front-line staff may be defensive or worried, and AI use may be hidden: 69% of the general-workforce interviewees in one study mentioned stigma around using AI at work (ANTHROPIC-INTERVIEWER-2025).
- **For AI discovery, interview at the task level and test with real samples.**
  - Ask who wants a task handed over and how much human involvement it needs (SHAO-2026).
  - Ask what must be verified, and bring real inputs to try (OPENAI-ACADEMY-2025, ANTHROPIC-WORK-2025).
  - Self-reports can diverge from measurement. In an RCT, developers expected AI to save time but measured completion time rose 19% (METR-2025).
- **Value comes from redesigning the workflow, not from lists of use cases.** Consultancy and academic surveys point the same way, though all are self-reported and some are search-only (BCG-2025, MIT-NANDA-2025, MCKINSEY-QB-2025). Discovery interviews should therefore map the whole flow, handoffs and rework, not only the step someone wants to automate.
- **AI-guided interviews now have real evidence for qualitative breadth.**
  - AI interviewers kept to neutral, open questions in over 95% of 18,000+ hand-coded questions (CHOPRA-2026).
  - Their dynamic probing drove most of the thematic gain over open-text survey boxes (CHOPRA-2026).
  - Documented failure modes remain: too few follow-ups, occasional judging, multi-question messages (WUTTKE-2025, GEIECKE-2025).
  - Evidence is from research and survey samples. Process-discovery chatbots are only tested in small, simulated or student settings.
- **An AI interviewer should run a tight protocol.**
  - One question per message, one theme per question, neutral wording, no evaluative comments.
  - Ask for a concrete recent instance, probe, ask for records, and finish with playback and correction.
  - Escalate to observation or a human for high-stakes or numeric claims.
- **Main gap:** no study compares AI and human interviewers on eliciting volumes, times, workarounds or tacit knowledge inside organizations. See section 10.

---

## 2. Core concepts in plain language

**Say-versus-do gap (work-as-imagined versus work-as-done).** What people say about how work is done and what they do differ, partly because memory is fallible and partly because people describe the rule rather than the practice. Safety science names this work-as-imagined versus work-as-done (HOLLNAGEL-2017, key points). Interviews give you the described process; observation, artifacts and data give you the performed one. *For knowledge work:* the written procedure, the leader's view and the analyst's actual week are three different processes. *For AI:* an AI built on the described process fails on the performed one.

**Elicitation, not collection.** Requirements engineering uses "elicitation" because good requirements cannot just be gathered by asking. Stakeholders omit what seems obvious, struggle to communicate needs and are unsure of the problem domain (WIKI-ELICIT, citing Christel and Kang 1992). *For AI:* people cannot describe "where AI would help" from a description alone (NNG-NIELSEN-2010), so the advisor must elicit tasks and pain, and do the matching itself.

**Tacit knowledge and workarounds.** Experts know more than they can say (Polanyi's formulation, WIKI-TACIT). Much of the judgement in a process sits in cues, habits and workarounds. A workaround is described as a user-driven solution to perceived system limitations (Alter 2014, pp. 1042–1045, as summarized in LEE-2025, §1), and Alter's 2014 theory treats it as a process with identifiable preconditions (ALTER-2014, abstract). The critical decision method (CDM) extends the critical incident technique with probes to reach this layer (AHRQ-CDM). *For AI:* workarounds mark where the official process is wrong, and tacit judgement marks what cannot be delegated without capturing it.

**Specific, recent, critical episodes beat generalities.** Critical incident technique, "walk me through the last time", the Mom Test rules and Jobs-to-be-Done timelines all ask for concrete past episodes (NNG-ROSALA-2020, FITZPATRICK-MOMTEST, MOESTA-JTBD). Extreme cases are more vivid and give detail (NNG-NIELSEN-2010). *For AI:* a concrete episode gives inputs, outputs, checks and error cost, which are the specifications an AI use case needs.

**Triangulation, top-down plus bottom-up.** Top-down decomposition by leaders is complemented by bottom-up discovery from how work is actually recorded (WIKI-BPD). Interviews are best combined with observation and documents (NNG-NIELSEN-2010, BISPO-2022). *For AI:* leader interviews frame scope; front-line interviews, samples and system data fix the map.

**Interviewee position changes the method.** Senior professionals are practised at stock answers and at testing the interviewer (EMPSON-2018). Front-line staff may fear job consequences or stigma. Social desirability, demand effects and acquiescence all shape answers, and the interviewer's reactions and privacy matter (BISPO-2022). *For AI:* a non-judgemental, private channel and explicit normalisation help. AI use itself is socially loaded (ANTHROPIC-INTERVIEWER-2025).

**Playback and validation.** Returning your interpretation to participants for correction (member checking) is a validation step, and the literature treats it as more than a formality. A later, deeper variant, synthesized member checking, revisits the interview and the interpreted data some months afterwards (BIRT-2016). Contextual inquiry builds a wrap-up summary into the session (NNG-FLAHERTY-2020). *For AI:* playback is cheap for a conversational advisor and catches mis-mapping before it propagates to diagnosis.

**Interview phases.** Contextual inquiry uses primer, transition, contextual interview and wrap-up (NNG-FLAHERTY-2020). The CDM runs scenario, probes, participant, incident account, timeline, decision points, probing, tables (AHRQ-CDM). Anthropic's AI interviewer uses planning, interviewing, analysis, with human review of the plan (ANTHROPIC-INTERVIEWER-2025).

**Task-level, desire-versus-capability thinking for AI.** The WORKBank audit asks workers per task how much they want it done by AI and how much human involvement they want, then compares that with expert capability ratings. This gives four zones: Green Light, Red Light, R&D Opportunity, Low Priority (SHAO-2026, abstract and §2.3). Capability is jagged: in a BCG field experiment, AI helped on tasks inside the frontier and hurt accuracy on a task outside it (MOLLICK-2023, reporting Dell'Acqua et al.). *For discovery:* collect desire, capability evidence and human-involvement preference separately.

**AI-guided interviewing.** An LLM generates the next question in real time under a prompt of interviewing principles and a topic guide. Evidence on quality, strengths and failure modes is in sections 4.1 and 6. The honest scope is breadth at low marginal cost with adaptive probing, not a replacement for observation.

---

## 3. Expert moves

Format: **move** — when to use it — what it reveals — source ref (locator).

**Eliciting the actual process**

1. **Ask for the most recent concrete instance ("walk me through the last time") instead of "how do you usually do it"** — when mapping any step or process — reveals the real sequence, tools and detours rather than the idealized workflow — NNG-NIELSEN-2010 ("What Interviews Can Tell You", parenthetical on idealized workflows); GEIECKE-2025 (§ general instructions, "palpable evidence", pp. 10–12); FITZPATRICK-MOMTEST (search-only: asks for specific past events).
2. **Ask for critical incidents in both directions, with thinking time, and choose the question type on purpose: generic example, most recent example or critical incident** — when exploring pain, quality and enablers, or designing a script — reveals the events that actually changed outcomes, with vivid detail; a generic example returns whatever comes to mind, "most recent" avoids selection, "critical" targets causal events — NNG-ROSALA-2020 (scripted best-case then worst-case example; comparison table).
3. **Follow one work item end to end across teams ("go and see"), not one function** — when mapping a cross-functional flow — reveals handoffs, waits and steps no single team owns — LEI-GEMBA (gemba walk, "go see, ask why, show respect", and following one customer-facing process across departments).
4. **Watch the work and interrupt with questions only at moments you do not understand** — when you can access the work (screen-share, desk-side) — reveals low-level habitual steps, interruptions and illogical processes — NNG-FLAHERTY-2020 (contextual interview phase; author's insurance data-entry anecdote).
5. **Make an explicit transition from interview to observation, or people stay in "tell-all" mode** — when moving from the intro conversation to the live work — avoids summarized accounts that omit reasoning and detail — NNG-FLAHERTY-2020 (transition phase; risk "participants default into interview mode").
6. **Ask for the standard path, then the variations and the reasons behind them** — when mapping exception rates and branches — reveals the real branching logic and what triggers each variant — NNG-FLAHERTY-2020 (contextual-interview step "standard steps vs. extraneous or uncommon variations").
7. **Ask what the person does outside the system or procedure, and which other resources they consult** — when mapping or diagnosing — reveals workarounds, shadow tools and tacit checks that mark where the formal process is wrong — NNG-FLAHERTY-2020 (external resources; habitual saving example); ALTER-2014 (abstract: workaround theory); LEE-2025 (abstract: workarounds around GenAI as invisible labour).
8. **Use CDM-style structure for expert judgement: pick an incident, build a timeline, split it into decision points, probe each** — when the step depends on expert judgement (review, triage, pricing, risk) — reveals the cues and decision rules used, which are the tacit core — AHRQ-CDM (steps 1–9); KLEIN-1989 (search-only origin).
9. **Use five whys on one specific failure, verify each "because" against a record, and branch when there are several causes** — when diagnosing a particular defect or delay, not a whole process — reveals causes beyond the obvious symptom — LEI-5WHYS (Ohno example; "the number five is not the point"); WIKI-5WHYS ("Criticism": stops at symptoms, not repeatable, may isolate one cause; Card's critique, CARD-2017 search-only).
10. **Ask "why is this important to you?" and "what has that been like?" after a step is described** — when moving from steps to outcomes and motives — reveals the goal behind the step, which separates the job from the current method — GEIECKE-2025 (example follow-ups, pp. 10–11); MOESTA-JTBD (search-only: struggling moment plus desired progress).
11. **Reconstruct the decision timeline for a recent purchase or change (first thought, passive looking, active looking, deciding)** — when the process is a decision to adopt or switch (including past tool or vendor adoption) — reveals triggers, alternatives and what nearly stopped the decision — MOESTA-JTBD (search-only, secondary summaries; verify wording before quoting).

**Quantifying volumes, times and quality**

12. **Ask for last month's actual volume and pull the record while you are on the call** — when mapping — reveals variation and hidden rework that a "typical week" hides — practitioner extension; rationale in BERNARD-1984 (p. 503 "Summary of the Literature": about half of what informants report is probably incorrect in some way; adjacent evidence on recalled communications and events).
13. **Elicit time as best case, typical and worst case, then ask what made the worst one worst** — when estimating effort per instance — reveals optimism in estimates and the causes of tail delays — WIKI-PLANNING (Buehler et al. 1994 design: best-case and worst-case estimates beside the base estimate; actual time exceeded the average estimate); practitioner extension for processes.
14. **Separate hands-on time, elapsed time and first-pass quality for each step, and count handoffs and who touched the item** — when sizing a step for AI or redesign — reveals whether time is work or waiting, rework rates, queueing and where context is lost — LEI-VSM (process data boxes: cycle time, lead time, % complete and accurate); LEI-GEMBA (cross-department walk); adapted from manufacturing to knowledge work as a practitioner extension.
15. **Ask the interviewee to bring or show the artifact (the file, email, template, SOP, checklist)** — when mapping or running a workshop — reveals real inputs and outputs and whether a use case is clear enough to test — OPENAI-ACADEMY-2025 (workshop prep: "a real example, such as notes, drafts, reports, templates…"); NNG-FLAHERTY-2020.

**Bias, defensiveness and trust**

16. **Interview after you have seen documents or observed work, and cross-check against them** — when stakes or sensitivity are high — reveals socially desirable answers by contradiction with evidence — BISPO-2022 (first of eight reflections: triangulate; interview after other sources); NNG-NIELSEN-2010 (triangulation).
17. **Order questions broad to specific, sensitive last; ensure privacy; avoid third parties** — when a topic may feel threatening (headcount, quality problems, hidden AI use) — reveals more candid answers — BISPO-2022 (second and third reflections; bystander effect).
18. **Phrase questions so that sharing problems is clearly acceptable, presume no view, and watch for cues of bias (discomfort, agreeing with everything, contradictions with known evidence)** — when people may defend the status quo — reveals undisclosed problems and signals when to slow down, re-ask from another angle or check evidence — GEIECKE-2025 (general instructions: neither assume a view nor provoke a defensive reaction); BISPO-2022 (interviewer's position section: behaviours that may indicate bias).
19. **Treat unprompted mentions as stronger signals than answers to your own prompts** — when interpreting transcripts — separates real concerns from invented opinions (the "query effect") — NNG-NIELSEN-2010 ("Beware the Query Effect").

**Senior leaders versus front-line staff**

20. **For senior professionals: learn their vocabulary and background first, open with an easy question to calibrate, then press for specifics; send the topic guide in advance and, where useful, use concept mapping** — when interviewing partners, directors, executives with limited time — reveals beneath-the-surface practice, since they otherwise give practised general answers, and reduces power asymmetry — EMPSON-2018 (accepted manuscript, "Preparing to interview", p. 16; "Going deeper", pp. 20–21); GOLDMAN-SWAYZE-2012 (preparation section: send the interview guide in advance; abstract on concept mapping).
21. **Challenge stock answers gently, give the leader control (for example, recording off), and say there is no judgement** — when you hear polished generalities — reveals the real position and sensitive information — EMPSON-2018 ("Going deeper": rhetorical strategies).
22. **Ask leaders for work-as-imagined, then test it with those who do the work, and treat the gap as the finding** — at the start of Map for a unit or organization — reveals where documented or believed process differs from practice, which is where workarounds and cheap wins live — HOLLNAGEL-2017 (key points 1–4).

**Playback and validation**

23. **End with an explicit playback in your own words and ask for corrections, and use the wrap-up to hold interpretations you have been testing** — at the end of every session — reveals misreadings before they reach the diagnosis — NNG-FLAHERTY-2020 (wrap-up; advice to hold most validation for it, since frequent validation mid-session can bias behaviour).
24. **Return the written map (or a synthesis of the interview) later and ask for corrections** — before a map is signed off at unit or organization level — reveals co-constructed errors and omissions — BIRT-2016 (synthesized member checking; Table 1).

**Adapting for AI opportunity discovery**

25. **Rate and discuss tasks, not jobs: for each familiar task, ask how much they would want an AI to do it fully, and how much human involvement they would want** — when building the opportunity inventory — separates automate, augment and keep-human, and surfaces task-level desire versus current capability — SHAO-2026 (abstract; §2.3 Likert items, familiarity filter).
26. **Ask what must be checked, how long checking takes, and which tasks they would delegate fully; then test one or two real examples** — when sizing AI value — reveals the verification burden, which can cancel the time saved, and the delegation criteria people actually use — ANTHROPIC-INTERVIEWER-2025 (scientists: trust and reliability the primary barrier in 79% of interviews); ANTHROPIC-WORK-2025 (qualitative interviews: delegation criteria; "fully delegate" 0–20% for most); OPENAI-ACADEMY-2025 (live testing with representative inputs).
27. **Ask who knows how they currently use AI, and what they have tried that did not work** — in Onboarding and Map — reveals hidden or "shadow" AI use, stigma and prior failed attempts — ANTHROPIC-INTERVIEWER-2025 (69% mentioned stigma; quoted example of not telling colleagues); MIT-NANDA-2025 (§3.3 "shadow AI economy").
28. **Ask where claimed time savings go, and compare self-reported gains with logs or measured samples where possible** — when claimed benefits are large — reveals perception bias in productivity claims — METR-2025 (RCT abstract); ANTHROPIC-INTERVIEWER-2025 ("Augmentation versus automation": 65%/35% self-reported against 47%/49% observed); ANTHROPIC-WORK-2025 (caveats on self-reported productivity).

**AI-interviewer mechanics**

29. **Fix the topic guide and keep the interviewer prompt generic; keep a running analytic summary for long interviews** — when building an AI interviewer — keeps interviews comparable and the model focused on important detail — CHOPRA-2026 (Introduction p. 2; probing-agent prompt and footnote 8, pp. 10–11).
30. **Have humans review the AI-drafted interview plan, then let the interviewer adapt in session, keep a human in analysis, and audit transcripts for under-probing and judging remarks** — when deploying an AI interviewer at scale — keeps research goals stable while allowing tangents, and catches the failure modes seen in practice — ANTHROPIC-INTERVIEWER-2025 ("How Anthropic Interviewer works": planning, interviewing, analysis); WUTTKE-2025 (§4 Findings: 88% of violations of the follow-up rule came from the AI; AI occasionally judged respondents, typically encouragingly).

---

## 4. Question bank

### 4.1 Operating rules for an AI interviewer asking one question at a time

Sourced rules:

1. **One question per message, one theme per question** (GEIECKE-2025, general instructions; CHOPRA-2026, probing guidelines, pp. 10–11). GEIECKE-2025 reports that current models struggle to always keep to one question (Limitations and Extensions), and CHOPRA-2026 notes that LLMs often fail to follow explicit instructions (Introduction, p. 3), so audit compliance.
2. **Open, non-leading wording** ("how", "what", "why"). Never suggest answers, not even a broad theme (GEIECKE-2025; CHOPRA-2026).
3. **Do not judge or comment on what was said** (CHOPRA-2026). Add an explicit "no evaluative or encouraging remarks" rule, because the AI in one study occasionally judged respondents (WUTTKE-2025, §4).
4. **Ask for concrete evidence**: events, situations, practices, examples; avoid questions that lead only to broad generalizations (GEIECKE-2025).
5. **Clarify ambiguous language, contradictions and novel concepts** (CHOPRA-2026, probing guideline "Clarity"). If the respondent cannot answer, try the question from a different angle before moving on (GEIECKE-2025).
6. **Follow the interviewee's lead but redirect gently; pivot when responses stay repetitive or on the surface** (CHOPRA-2026, "Flexibility"). Avoid recaps, and use a concise reference when revisiting (CHOPRA-2026, "Focus").
7. **Respect boundaries**: if the interviewee signals discomfort, move on (CHOPRA-2026, "Respect"). Stay on topic and redirect unrelated talk (GEIECKE-2025).
8. **Control the structure**: a topic guide gives the length and scope of each topic. A fixed question count per topic makes interviews comparable (CHOPRA-2026, footnote 8, p. 10).
9. **Keep interviews short**: Anthropic's interviews ran about 10–15 minutes (ANTHROPIC-INTERVIEWER-2025). Offer voice input where possible (CHOPRA-2026, p. 11; SHAO-2026, §2.3).
10. **Avoid known interviewer mistakes**: technical, irrelevant, very long or vague questions; asking the customer for solutions; not probing; skipping the existing system, stakeholders or success criteria; no final summary; opening with direct questions; repeating questions; poor listening; no rapport (KORN-2025, mistake groups and figure labels, derived from Bano et al.).

Practitioner extensions (not source-tested):

- **Anchor first.** Open each process with one concrete recent instance. Hold forward-looking "where could AI help" questions until the end, and ask them about tasks the person has just described (supported by NNG-NIELSEN-2010 on the limits of speculating about the future).
- **Probe ladder per step.** Clarify, then make concrete (a real example), then quantify (count or time, source of the number), then ask why, then ask about exceptions, then ask what is checked.
- **Coverage ledger.** Keep a private list of what is still missing: trigger, inputs, steps, handoffs, volumes, times, exceptions, quality checks, tools, workarounds, judgement points, outputs. Ask the next question from the gaps, not from a script.
- **Number discipline.** When a number is given, ask where it comes from (a record, a guess, last month) and label it as such. Keep a typed field for "reported", "from record" and "observed".
- **Playback at the end of each process segment and at close.** Ask what was misunderstood.
- **Escalate** to a human or to observation when claims are high-stakes, numbers cannot be sourced or the interviewee is distressed. Text-only interviewing may miss emotional cues (ANTHROPIC-INTERVIEWER-2025, Limitations).

### 4.2 Questions by phase

Tags: `[T]` team, `[U]` unit, `[O]` organization. The journey stage is the advisor-loop sub-stage the answer feeds. The question wording is my own drafting unless a source is named.

**Onboarding** (rapport, consent, expectations, baseline; interview 10–20 minutes)

| Question | Scope | Journey stage |
|---|---|---|
| Before we start, what would make this conversation worthwhile for you? (primer: purpose, confidentiality, how it will be used; NNG-FLAHERTY-2020 primer) | T U O | Onboard |
| In a sentence or two, what does your team (unit, organization) exist to deliver, and what are you accountable for? | T U O | Onboard |
| How do you currently use AI in your work, if at all? Many people use it quietly, and there is no right answer. (normalises; ANTHROPIC-INTERVIEWER-2025 stigma finding) | T U O | Onboard, AI baseline |
| What have you tried with AI so far, and what happened? | T U O | Onboard, AI baseline |
| What, if anything, worries you about looking at AI for this work? | T U O | Onboard, resistance |
| Who does this work day to day, and who else should I talk to? | T U O | Onboard, interviewee set |
| What cannot change: regulation, client commitments, tools, headcount? | U O | Onboard, constraints |

**Frame** (outcomes, scope, selecting what to map; mostly leaders; treat answers as work-as-imagined to validate in Map)

| Question | Scope | Journey stage |
|---|---|---|
| If this goes well in 12 months, what is different for your clients and your people? | U O | Frame, outcomes |
| What are you measured on, how is it measured, and how often is it reviewed? | T U O | Frame, success measures |
| Which parts of your scope take the most effort, create the most complaints, or cause the most rework? | T U | Frame, candidate processes |
| What would you rather we did not touch, and why? | U O | Frame, boundaries |
| Who owns each of these processes, who does the work, and who depends on the output? | U O | Frame, stakeholders |
| What happened to the last improvement or technology initiative here? | U O | Frame, history and appetite |
| Where do you suspect the documented process and the real practice differ? (HOLLNAGEL-2017) | U O | Frame, hypotheses to test in Map |
| What data, confidentiality or client-contract constraints limit how AI could be used? | U O | Frame, guardrails |
| If we had to split your scope into units of work, where would the natural seams be: by service, client type or process? | O | Frame, scope breakdown |
| How do you currently find out how work really gets done, and when did you last watch it done? | U O | Frame, leader's visibility |

**Map: walk-through** (core; anchors on a recent instance)

| Question | Scope | Journey stage |
|---|---|---|
| Think of the last [unit of work] you completed. What set it off? (NNG-NIELSEN-2010; GEIECKE-2025) | T | Map, trigger |
| Walk me through what happened, from that trigger to the moment it was done. | T | Map, steps |
| And then what? Who or what did you need at that point? | T | Map, steps and handoffs |
| What did you receive, in what form, and what did you hand on? | T | Map, inputs and outputs |
| Can you show me the actual file, email or ticket? | T | Map, artifact |
| How was that one different from the one before? | T | Map, variation |
| Think of a time this went especially well. What happened, and what made the difference? Now a time it went badly. (NNG-ROSALA-2020) | T U | Map, critical incidents |

**Map: quantify** (always source the number)

| Question | Scope | Journey stage |
|---|---|---|
| How many of these did your team finish last month? Can we look at the record together? | T U | Map, volume |
| For that last one, how long did you actively work on it, and how long did it wait? (LEI-VSM data boxes) | T | Map, times |
| Across the last ten, what was the quickest, the typical and the slowest? What made the slowest slow? (WIKI-PLANNING design) | T | Map, time range |
| How many people touched it, and how many handoffs were there? | T U | Map, handoffs |
| What share comes back for correction or gets redone? What caused the last one? | T U | Map, rework |
| Roughly what share follows the standard path, and what triggers the other paths? (NNG-FLAHERTY-2020) | T U | Map, variation |
| Where does that number come from: a system report, a sample, or a feel? | T U O | Map, evidence quality |

**Map: tacit knowledge and workarounds**

| Question | Scope | Journey stage |
|---|---|---|
| What did you notice that told you to do it that way? (CDM-style cue probe; AHRQ-CDM) | T | Map, tacit cues |
| What do you check that is not in any procedure? | T | Map, tacit checks |
| What would someone new get wrong, and how long before they stop? (practitioner extension) | T U | Map, tacit knowledge |
| Where do you step outside the official process or tool, and why? (ALTER-2014; NNG-FLAHERTY-2020) | T | Map, workarounds |
| Is there a spreadsheet, template or note that only you use? | T | Map, shadow tools |
| What do you do when the system does not have what you need? | T | Map, workarounds |
| What rule of thumb do you use to decide [judgement step]? | T | Map, decision rules |

**Map: judgement and AI lead-in** (feeds Diagnose; ask only after the process is mapped)

| Question | Scope | Journey stage |
|---|---|---|
| Which steps are mostly lookup, copying, formatting or chasing, and which depend on your judgement? | T | Map to Diagnose |
| If a capable colleague did this step for you, what would you need to check before relying on it? (ANTHROPIC-WORK-2025 delegation themes) | T | Map to Diagnose, verification |
| What does good output look like here, who decides, and what are the signs of poor quality? | T U | Map to Diagnose, quality |
| Have you tried an AI tool on this step? What did you have to fix? | T | Map to Diagnose, AI baseline |
| For each of these tasks, how much would you want AI to do it fully, and how much of your own involvement would you want kept? Why? (SHAO-2026) | T | Map to Diagnose, desire and agency |
| Would you be willing to try one of these with a real example now? (OPENAI-ACADEMY-2025) | T | Map to Reimagine, test |

**Map: unit and organization level**

| Question | Scope | Journey stage |
|---|---|---|
| Which processes are shared between teams, and where do teams do the same work in different ways? | U O | Map, variation across units |
| Which systems and data sources do all units rely on? | U O | Map, shared dependencies |
| Who keeps process documentation current, and when was it last checked against practice? | U O | Map, documentation reliability |
| Where is work as people describe it different from the documents? (HOLLNAGEL-2017) | U O | Map, work-as-imagined gap |

**Playback and close** (every phase)

| Question | Scope | Journey stage |
|---|---|---|
| Let me say back what I understood, in my own words. What did I get wrong? (NNG-FLAHERTY-2020 wrap-up) | T U O | Map, validation |
| What would you tell a new colleague that I have not asked about? | T U O | Map, completeness |
| What did you expect me to ask that I did not? | T U O | Close |
| May I send you the written version so you can correct it later? (BIRT-2016) | T U O | Close, member check |

---

## 5. Common traps

| # | Trap | Why it happens | How to avoid | Evidence |
|---|---|---|---|---|
| 1 | **Mapping the idealized process** | "How do you usually…" invites the rule, not the practice | Anchor on the last instance; ask for variations and exceptions | NNG-NIELSEN-2010 (idealized workflow); NNG-FLAHERTY-2020 (specialists omitted steps they did) |
| 2 | **Trusting recalled numbers and time estimates** | Memory fades, estimates are optimistic | Source every number; pull records; use ranges; sample | BERNARD-1984 (about half of informant reports probably wrong in some way; adjacent evidence); WIKI-PLANNING (1994 study: average estimate 33.9 days vs actual 55.5; about 30% finished within predicted time) |
| 3 | **Asking people where AI would help** | People struggle to envision unbuilt tools; they invent opinions when asked (query effect) | Map tasks first, then match capabilities to tasks yourself; test with real examples | NNG-NIELSEN-2010; SHAO-2026 (task familiarity filter, §2.3) |
| 4 | **Automating the existing process, waste included** | Interviews describe steps, and teams optimize the visible step | Map the whole flow and ask what the step is for; use the four lenses, not only automation | BCG-2025 (value from reshaping and reinventing core workflows end to end, p. 3 and "What Value Generators Do Differently"); MCKINSEY-QB-2025 (search-only: "workflow, not agent" lesson); HAMMER-1990 (search-only, title and abstract only: "Don't Automate, Obliterate") |
| 5 | **Visible-use-case bias** | Leaders fund what is easy to attribute | Ask where the cost and delay are, not where the demos are | MIT-NANDA-2025 (§3.4: executives' hypothetical $100 budget put about half into sales and marketing; report says back-office often yields better ROI; authors state the bias reflects easier metric attribution) |
| 6 | **Taking the leader's account as the process** | Leaders see work-as-imagined; senior people give stock answers | Interview those who do the work; ask leaders where documents and practice differ | HOLLNAGEL-2017; EMPSON-2018 ("Going deeper"); BCG-2025 (survey of CxOs and senior executives; authors note responses may be subject to perception bias, Methodology p. 19) |
| 7 | **Defensiveness, social desirability, hidden AI use** | Fear of consequences; AI stigma | Privacy, confidentiality, normalising language, no reactions, triangulation | BISPO-2022; ANTHROPIC-INTERVIEWER-2025 (69% mentioned stigma; 55% expressed anxiety about AI's impact on their future) |
| 8 | **Leading questions and interviewer reactions** | Interviewers signal expected answers | Neutral, open wording; no evaluative remarks; AI prompts that forbid commentary | BISPO-2022 (interviewer's reactions); CHOPRA-2026 (neutrality guideline); WUTTKE-2025 (§4: AI occasionally judged respondents) |
| 9 | **Five whys as a root-cause verdict** | Stops at symptoms, depends on investigator knowledge, may isolate a single cause | Use for one defect, verify with records, branch, or use other cause-analysis tools | WIKI-5WHYS ("Criticism": Minoura; Card); LEI-5WHYS ("the specific number five is not the point") |
| 10 | **Observation session turns into a tell-all or a gripe session** | People summarise, or use the session to air frustrations | Make the transition explicit; steer back to the work | NNG-FLAHERTY-2020 (risks section) |
| 11 | **AI interviewer under-probes, stacks questions or comments** | Prompt changes have side effects; models do not always comply | Audit transcripts; strict one-question rule; test after every prompt change | WUTTKE-2025 (§4: even minor prompt modifications led to unintended side effects; 88% of follow-up-rule violations by AI); GEIECKE-2025 (models struggle to restrict to a single question) |
| 12 | **Treating AI-simulated interviewees as evidence** | Simulated users sound plausible | Use simulations for interview practice and script testing; use real people for facts | ATAEI-2024 (simulated agent interviews compared on latent needs identified; abstract); LOJO-2025 and ESTRADA-2025 (simulated clients for training). Interpretation: counts of "needs" from simulation are not validated against real users in these sources |
| 13 | **Sample and selection bias** | Willing or convenient participants differ from the rest | Sample across roles and seniority; state the limit | MIT-NANDA-2025 (§8.2 sample limitations); ANTHROPIC-INTERVIEWER-2025 (crowdworker recruitment, selection bias) |
| 14 | **Equating desire or exposure with feasibility or adoption** | Desire, capability and exposure are different measures | Record desire, capability evidence and human-involvement preference separately; test on samples | SHAO-2026 (Intro p. 2: 41.0% of Y Combinator company-task mappings fall in Low Priority and Red Light zones; mismatches between desire and capability); ELOUNDOU-2023 (abstract: exposure estimates, no adoption predictions); MOLLICK-2023 (outside-frontier task) |
| 15 | **Believing self-reported AI productivity** | Perception bias | Compare with measured samples or logs; ask what is checked | METR-2025; ANTHROPIC-WORK-2025 (authors cite the METR result as a caveat) |

---

## 6. Evidence

All rows: what it measures, provenance, source. "Self-reported", "vendor-published" and "independent" are used as in the brief. Search-only figures are labelled and come from secondary coverage of the original, not from the original.

### 6.1 Reliability of what interviewees say

| Data point | What it measures | Provenance | Source |
|---|---|---|---|
| "On average, about half of what informants report is probably incorrect in some way" | The reviewers' summary of studies comparing informants' retrospective reports with observation or records; most studies cover recalled communications and events. Not a measure of process volumes | Independent academic review (Annual Review of Anthropology, 1984); adjacent evidence | BERNARD-1984, p. 503 |
| People "can recall or predict less than half of their communications", by amount or frequency, over all data sets | Findings of Bernard, Killworth and Sailer's studies of recalled communications | Independent academic | BERNARD-1984 (BKS findings list, item 7) |
| Average predicted 33.9 days vs average actual 55.5 days to finish a senior thesis; about 30% finished in their predicted time | 37 psychology students' estimates against actual completion (Buehler et al. 1994, as reported on Wikipedia) | Independent academic, via a secondary source | WIKI-PLANNING |
| Developers forecast AI would cut completion time by 24%, estimated afterwards a 20% cut, and measured a 19% increase | RCT: 16 experienced open-source developers, 246 tasks, early-2025 tools | Independent (METR); preprint | METR-2025 (abstract) |
| Self-reported AI use: 65% augmentative / 35% automative, against 47% augmentation / 49% automation in observed Claude usage | Interview participants' descriptions of AI's primary role compared with Anthropic Economic Index classification of tasks; unclassified interactions leave the observed figures below 100%. Authors list sample, provider and perception differences as possible explanations | Vendor-published, with self-report vs. own usage data | ANTHROPIC-INTERVIEWER-2025 ("Augmentation versus automation") |
| 69% of general-workforce interviewees mentioned social stigma around using AI at work; 55% expressed anxiety about AI's impact on their future | Share of 1,000 interviewees (crowdworker platform, other main occupations) whose interviews were coded as mentioning the topic | Vendor-published; AI-coded themes; selection bias acknowledged | ANTHROPIC-INTERVIEWER-2025 (results; Limitations) |

### 6.2 AI-guided interviews

| Data point | What it measures | Provenance | Source |
|---|---|---|---|
| Over 95% of AI-interviewer questions rated open-ended, neutral and relevant; essentially zero hallucination | Human hand-coding of over 18,000 interview questions and responses for ten quality markers, across 766 AI-led online interviews with US adults (about 400 hours) | Independent academic working paper | CHOPRA-2026 (Introduction, pp. 3–4) |
| AI-led interviews uncovered about five times as many unique, empirically common themes as a single open-ended survey question; saturation at about N = 25 | Thematic coding comparison with benchmark surveys; bootstrap simulation of new themes against sample size | Independent academic working paper | CHOPRA-2026 (Introduction, pp. 5–6) |
| Most of the added value of AI-led interviews over other qualitative survey methods comes from dynamic probing questions | The authors' decomposition against three benchmarks, the strictest of which removes the probing questions from the same transcripts | Independent academic working paper | CHOPRA-2026 (abstract; pp. 5–6) |
| LLM usage costs below $0.10 per interview hour; 96%+ would take part in another AI-led interview; a majority would prefer an AI to a human interviewer | Authors' cost reporting; participant self-evaluation after the interview | Independent academic; participant self-report | CHOPRA-2026 (Introduction pp. 2–3) |
| AI interviewer performance "close to an average hypothetical human expert"; models struggle to always restrict messages to one question | Authors' assessment from a panel of sociology PhD students rating transcripts against a human-expert benchmark; authors' observation on compliance | Independent academic working paper | GEIECKE-2025 (§ Limitations and Extensions; §2.1 note on single-question compliance) |
| 72 guideline violations per AI interview vs 64 per human interview; 94% of active-listening violations by humans; 88% of violations of the follow-up rule by the AI | Manual coding of interviewer behaviour in six human-led and five AI-led interviews with university students (GPT-4) | Independent academic, small-N, peer-reviewed workshop paper | WUTTKE-2025 (§4 Findings) |
| Chatbot-led conversational survey drew higher informativeness, relevance, specificity and clarity than a typical online survey form | Roughly 600 participants split between conditions; over 5,200 free-text responses rated on Gricean maxims | Independent academic (ACM TOCHI, 2020); survey, not interview | XIAO-2020 |
| An LLM requirements-interviewer made a similar number of errors to human interviewers in 33 simulated stakeholder interviews | Error counts against a mistake-type questionnaire, simulated stakeholders; software requirements | Independent academic preprint | KORN-2025 (abstract) |
| LLM follow-up questions no worse than human-authored on clarity, relevancy and informativeness, and better when guided by mistake types | Controlled experiments with GPT-4o-generated vs human-authored follow-up questions in requirements elicitation | Independent academic preprint | SHEN-2025 (abstract) |
| In a between-subjects study (n = 120), an LLM-played client gave students enough information to build sound designs in comparable time, and most preferred it | Students building designs from LLM interview vs transcript; training context | Independent academic preprint | LOJO-2025 (abstract) |

### 6.3 AI opportunity discovery and value

| Data point | What it measures | Provenance | Source |
|---|---|---|---|
| 46.1% of tasks: workers express positive attitudes toward AI-agent automation | 1,500 workers' ratings of 844 O*NET tasks across 104 occupations, after considering job-loss and enjoyment factors; AI-expert capability ratings from 52 experts; data collected January–May 2025 | Independent academic preprint; worker self-report | SHAO-2026 (Intro p. 2) |
| 41.0% of Y Combinator company-task mappings in the Low Priority and Red Light zones | The authors' mapping of YC companies to WORKBank tasks (the section text says "companies") | Independent academic preprint | SHAO-2026 (Intro p. 2; later section mapping investment to the desire-capability landscape) |
| 45.2% of occupations have H3 (equal partnership) as the dominant worker-desired human-agency level | Aggregation of workers' desired Human Agency Scale levels by occupation | Independent academic preprint; self-report | SHAO-2026 (Intro p. 2) |
| Only 5% of companies achieve AI value at scale; 60% report no material value; 35% are scaling | 2025 BCG global study of 1,250 CxOs and senior executives (25+ sectors) estimating AI maturity and value; the report notes possible perception bias | Vendor-published (consultancy); executive self-report | BCG-2025 (p. 3; Methodology p. 19) |
| 70% of strategic focus on people and processes, 20% on technology, 10% on algorithms | BCG's own "10-20-70" recommendation, not a measured outcome | Vendor-published (consultancy) recommendation | BCG-2025 (Conclusion) |
| "95% of organizations are getting zero return"; "just 5% of integrated AI pilots" extract millions in value | MIT NANDA preliminary report: 300+ public initiatives, interviews with 52 organizations, survey of 153 senior leaders; success = deployment beyond pilot with measurable KPIs, ROI measured 6 months after pilot; authors list sample and selection limitations | Independent (university project), non-peer-reviewed, preliminary | MIT-NANDA-2025 (Executive Summary; §8.2) |
| 62% at least experimenting with agents; 39% report enterprise-level EBIT impact; about 6% are "high performers"; high performers nearly 3x more likely to have fundamentally redesigned workflows | McKinsey State of AI 2025 survey (reported as 1,993 respondents in 105 countries); high performer = at least 5% of EBIT attributed to AI | Vendor-published (consultancy); self-report; search-only (secondary coverage) | MCKINSEY-2025 |
| Efforts that reimagine entire workflows are more likely to deliver positive outcomes | McKinsey's lessons from 50+ agentic builds it led and others in the market | Vendor-published (consultancy); search-only | MCKINSEY-QB-2025 |
| Over 40% of agentic AI projects predicted to be cancelled by end of 2027, citing cost, unclear value and risk controls; 3,412-person poll was of webinar attendees | A forward prediction (not an observation) by an analyst firm; poll was not a random sample | Vendor-published (analyst firm); search-only (secondary coverage) | GARTNER-2025 |
| With AI inside the frontier: 12.2% more tasks, 25.1% faster, 40% higher quality; outside the frontier: 84% correct without AI vs 60–70% with | Pre-registered experiment with 758 BCG consultants on 18 realistic tasks, GPT-4; as reported by a co-author | Independent academic, reported via co-author's blog (paper not read) | MOLLICK-2023 |
| About 80% of US workers could have at least 10% of tasks affected by LLMs; about 19% at least 50% | Exposure rubric combining human and GPT-4 ratings of O*NET tasks; the authors make no adoption forecasts | Independent academic preprint | ELOUNDOU-2023 (abstract) |
| Employees self-report using Claude in about 60% of their work and a +50% productivity boost; a majority say they can fully delegate only 0–20% of their work | August 2025 survey of 132 Anthropic engineers and researchers, plus 53 interviews and usage data; the authors flag measurement and perception caveats | Vendor-published; self-reported | ANTHROPIC-WORK-2025 (summary and Survey sections) |

### 6.4 Evidence quality note

I found no independent measurement of how accurate interview-derived volume or time estimates are in enterprise process discovery. The practical claims in section 3 on volumes and times are practitioner heuristics supported by adjacent evidence (BERNARD-1984, WIKI-PLANNING, LEI-VSM).

---

## 7. Worked examples

**Example 1: Interview versus observation in an insurance data-entry process (NNG-FLAHERTY-2020).**
- *Context:* A researcher redesigned the data-entry part of a tool used to create auto-insurance policies for commercial vehicle fleets.
- *Interview result:* All three specialists interviewed said they copied large batches of vehicle data from a spreadsheet and pasted them into the tool's data table.
- *Observation result:* Watching specialists do the work showed they also cross-referenced a screen from another tool to fetch missing information for each vehicle. They habitually pressed Save after every manual entry, though the program autosaved, because they either did not know or did not trust that it did.
- *Lesson:* The author reports that both findings influenced the design of the new tool. In an AI context, the unmentioned cross-referencing is exactly the step an automation would miss. Move 4 (observe) and move 6 (variations) apply.

**Example 2: Getting past stock answers with senior professionals (EMPSON-2018).**
- *Context:* A researcher on professional-service firms describes her interviews with partners and senior executives. Her account is research-interview practice, not consulting discovery, so transfer is by analogy.
- *What she reports:* Senior professionals are used to the same questions and often have stock answers. Partners told her that interviewers who let them stay in broad strokes get jargon and filler. She prepares her interviewee's background and vocabulary, and recounts a bad interview that followed her calling a partnership a "company" rather than a "firm". She opens with an easy question to calibrate, pushes for depth when answers stay broad, and offers choices such as turning off the recorder.
- *Lesson:* For a leader interview in Frame, prepare vocabulary and context, ask one easy opener, and drill down when answers stay general (moves 20 and 21).

**Example 3: Self-report versus observed use, and what interviews add (ANTHROPIC-INTERVIEWER-2025; ANTHROPIC-WORK-2025).**
- *Context:* Anthropic ran AI-led interviews with 1,250 professionals (10–15 minutes each) and, separately, surveyed and interviewed its own engineers.
- *Findings:* Interviewees described their AI use as 65% augmentative and 35% automative, while observed Claude usage was 47% augmentation and 49% automation. The authors list perception and sample differences as possible reasons. Interviews also surfaced stigma (69% mentioned it) and, in scientists, verification burden as the main barrier. The engineers' interviews produced delegation criteria alongside self-reported gains, with the authors flagging measurement caveats and citing the METR result.
- *Lesson:* Interviews are essential for motives, barriers and delegation logic, and unreliable for exact usage or time saved. Use both, label each number as reported or observed (moves 26–28).

**Example 4 (illustrative script, constructed for this brief and not drawn from a case): an AI interviewer mapping proposal drafting in a consulting practice.**

The exchange shows the rules in section 4.1: one question per turn, recent instance, number sourcing, workaround probe, playback.

- AI: Think of the last proposal you worked on. What set it off?
- User: A client's RFP arrived on a Monday.
- AI: What did you do first, once it arrived?
- User: I looked for a similar past proposal to start from.
- AI: How did you find it?
- User: I ask around, or search the shared drive, honestly mostly I ask.
- AI: And then what?
- *(...later, after the flow is mapped...)*
- AI: How many proposals did your team submit last month?
- User: About twenty, I think.
- AI: Is that from a report or an estimate?
- User: Estimate.
- AI: Could you check the pipeline tracker later and tell me the exact count?
- *(...)*
- AI: Is there anything you do outside the official template or tool to get a proposal out?
- User: I keep a private file of past pricing tables.
- AI: What do you use that file for?
- *(...end...)*
- AI: Let me say the flow back in my words: RFP arrives, you find a similar past proposal by asking colleagues, you adapt it, you use a private pricing file, partner review comes last. What have I got wrong?

---

## 8. Mapping to phases

**Interviewing (the craft layer across all phases).**
- Anchor on recent concrete instances; use critical incidents; probe with a ladder of clarify, concretize, quantify, why, exceptions, checks (moves 1–2, 8–10).
- Triangulate, reduce bias and defensiveness, and handle seniority differences (moves 16–22).
- AI-interviewer rules: one question per message, neutral wording, no commentary, topic guide, human-reviewed plan, transcript audits (section 4.1; moves 29–30).
- Honest limits: text-only channels miss emotional cues and demand characteristics apply (ANTHROPIC-INTERVIEWER-2025, Limitations).

**Onboarding.**
- A short primer: purpose, confidentiality, how answers will be used, and what the interviewee can correct (NNG-FLAHERTY-2020).
- Baseline questions on AI use, with normalising language, since stigma and hidden use are common (move 27).
- Surface worries early, and identify who does the work and who else to talk to.
- Keep early sessions short; Anthropic's AI interviews were about 10–15 minutes.

**Frame.**
- Treat leader answers as work-as-imagined and generate hypotheses to test (move 22).
- Elicit outcomes, measures, constraints, boundaries, history of past initiatives and appetite for change. Prepare for senior interviewees (moves 20–21).
- Use research goals to design the interview plan, as Anthropic's planning stage does, and have a human check the plan.
- Choose what to map using impact, frequency and readiness (the workshop columns in OPENAI-ACADEMY-2025: pain point, frequency, impact, complexity, readiness).
- Warn against picking use cases by visibility (trap 5) or by asking "where would AI help?" (trap 3).
- For org-level scopes, ask about natural seams for splitting into units.

**Map.**
- Walk-through of recent instances, with variations and critical incidents (moves 1–2, 6).
- Quantify with sourced numbers: ranges, record pulls, hands-on versus elapsed time, rework, handoffs (moves 12–14).
- Observe, or get artifacts, where possible (moves 4, 5, 15); use workshops of role-aligned groups with a board of workflow, pain point, frequency, impact, effort, readiness, opportunity, owner (OPENAI-ACADEMY-2025).
- Capture workarounds, tacit judgement and decision rules (moves 7–8).
- Do task-level capture of desire and human-agency preference, with a familiarity filter (move 25).
- Verification burden and delegation criteria (move 26).
- Playback and written member check before sign-off (moves 23–24).
- At unit and organization level, compare work-as-imagined and work-as-done, and look for variation across units (moves 22, 24).

---

## 9. Sources

Access: `full` = body text read; `search-only` = abstract, publisher page or search-result summaries only. Wikipedia pages were accessed 2026-10-16 and serve as secondary sources only for the specific points named in the text.

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| CHOPRA-2026 | Conducting Qualitative Interviews with AI | Chopra, Haaland; CESifo Working Paper 10666 | Academic working paper | https://www.cesifo.org/DocDL/cesifo1_wp10666.pdf | First version 2023-09-15; version read dated 2026-03-09 (cover: June 2026) | full |
| GEIECKE-2025 | Conversations at Scale: Robust AI-led Interviews with a Simple Open-Source Platform | Geiecke, Jaravel (LSE); NBER conference version; CEPR DP19705 | Academic working paper | https://conference.nber.org/conf_papers/f221279.pdf | 2025-07-16 | full |
| WUTTKE-2025 | AI Conversational Interviewing: Transforming Surveys with LLMs as Adaptive Interviewers | Wuttke et al.; LaTeCH-CLfL 2025 | Academic paper (arXiv) | https://arxiv.org/abs/2410.01824 | v1 2024-09-16; v2 2025-03-12 | full |
| ANTHROPIC-INTERVIEWER-2025 | Introducing Anthropic Interviewer: What 1,250 professionals told us about working with AI | Anthropic | Vendor research post | https://www.anthropic.com/research/anthropic-interviewer | 2025-12-04 | full |
| ANTHROPIC-WORK-2025 | How AI is transforming work at Anthropic | Anthropic | Vendor research post | https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic | 2025-12-02 | full |
| SHAO-2026 | Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce | Shao, Zope, et al. (Stanford); arXiv 2506.06576 | Academic preprint | https://arxiv.org/abs/2506.06576 | v1 2025-06-06; v3 2026-02-01 | full |
| XIAO-2020 | Tell Me About Yourself: Using an AI-Powered Chatbot to Conduct Conversational Surveys with Open-ended Questions | Xiao, Zhou, Liao, et al.; ACM TOCHI 27(3) | Academic journal | https://arxiv.org/abs/1905.10700 | 2020-06 | full |
| KORN-2025 | LLMREI: Automating Requirements Elicitation Interviews with LLMs | Korn, Gorsch, Vogelsang | Academic preprint | https://arxiv.org/abs/2507.02564 | 2025-07-03 | full |
| SHEN-2025 | Requirements Elicitation Follow-Up Question Generation | Shen, Singhal, Breaux (CMU) | Academic preprint | https://arxiv.org/abs/2507.02858 | 2025-07-03 | full |
| LOJO-2025 | Using Large Language Models to Develop Requirements Elicitation Skills | Lojo et al. | Academic preprint | https://arxiv.org/abs/2503.07800 | v2 2025-04-09 | full |
| ESTRADA-2025 | A Training Framework for BPM Modeling Interviews Based on LLM Assistants (BPM-LEIA) | Estrada-Torres, Parejo, Fox, Fernandez; BPM 2025 demo, CEUR-WS Vol. 4032 | Conference demo paper | https://ceur-ws.org/Vol-4032/paper-37.pdf | 2025 | full |
| DECASTRO-2025 | Business Process Design Support with Automated Interviews | Silva de Castro, Fantinato, Barcellos Costa; ICEIS 2025 | Conference paper | https://scitepress.org/publishedPapers/2025/133620/pdf/index.html | 2025 | full (abstract and skim) |
| KLIEVTSOVA-2024 | Conversational Process Modeling: Can Generative AI Empower Domain Experts in Creating and Redesigning Process Models? | Klievtsova et al. | Academic preprint | https://arxiv.org/abs/2304.11065 | v1 2023-04-19; v2 2024-01-18 | full (abstract and skim) |
| ATAEI-2024 | Elicitron: An LLM Agent-Based Simulation Framework for Design Requirements Elicitation | Ataei et al. | Academic preprint | https://arxiv.org/abs/2404.16045 | 2024-04-04 | full (abstract and skim) |
| NNG-NIELSEN-2010 | Interviewing Users | Jakob Nielsen, Nielsen Norman Group | Practitioner article | https://www.nngroup.com/articles/interviewing-users/ | 2010-07-25 | full |
| NNG-ROSALA-2020 | The Critical Incident Technique in UX | Maria Rosala, Nielsen Norman Group | Practitioner article | https://www.nngroup.com/articles/critical-incident-technique/ | 2020-01-26 | full |
| NNG-FLAHERTY-2020 | Contextual Inquiry: Inspire Design by Observing and Interviewing Users in Their Context | Kim Flaherty, Nielsen Norman Group | Practitioner article | https://www.nngroup.com/articles/contextual-inquiry/ | 2020-12-06 | full |
| AHRQ-CDM | Critical Decision Method (Workflow Assessment for Health IT Toolkit) | US Agency for Healthcare Research and Quality | Government toolkit page | https://digital.ahrq.gov/health-it-tools-and-resources/evaluation-resources/workflow-assessment-health-it-toolkit/all-workflow-tools/critical-decision-method | n/d | full |
| KLEIN-1989 | Critical decision method for eliciting knowledge, IEEE Trans. Systems, Man, and Cybernetics 19:462–472 | Klein, Calderwood, MacGregor | Academic journal (origin of CDM) | https://doi.org/10.1109/21.31053 | 1989 | search-only |
| BERNARD-1984 | The Problem of Informant Accuracy: The Validity of Retrospective Data | Bernard, Killworth, Kronenfeld, Sailer; Annual Review of Anthropology 13:495–517 | Academic review | https://bebr.ufl.edu/sites/default/files/Bernard%20et%20al.%20-%201984%20-%20The%20Problem%20of%20Informant%20Accuracy%20The%20Validity%20of.pdf (copy read) | 1984 | full |
| BISPO-2022 | Social desirability bias in qualitative health research | José Patrício Bispo Júnior; Rev Saúde Pública 56:101 | Academic essay | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9749714/ | 2022-11-18 | full |
| BIRT-2016 | Member checking: a tool to enhance trustworthiness or merely a nod to validation? | Birt, Scott, Cavers, Campbell, Walter; Qualitative Health Research 26(13) | Academic journal (accepted manuscript) | https://kclpure.kcl.ac.uk/ws/files/52859539/Member_checking_a_tool_BIRT_Accepted_2016_GREEN_AAM.pdf | 2016 | full |
| EMPSON-2018 | Elite interviewing in professional organizations | Laura Empson; Journal of Professions and Organization 5(1):58–69 | Academic journal (accepted manuscript) | https://openaccess.city.ac.uk/id/eprint/18237/ | 2018 | full |
| GOLDMAN-SWAYZE-2012 | In-Depth Interviewing with Healthcare Corporate Elites: Strategies for Entry and Engagement | Goldman, Swayze; Int. J. Qualitative Methods 11(3) | Academic journal | https://journals.library.ualberta.ca/ijqm/index.php/IJQM/article/view/9899/14128 | 2012 | full (skimmed) |
| HOLLNAGEL-2017 | Can we ever imagine how work is done? | Erik Hollnagel; HindSight 25, EUROCONTROL | Practitioner magazine | https://www.skybrary.aero/sites/default/files/bookshelf/3934.pdf | Summer 2017 | full |
| LEI-5WHYS | 5 Whys | Lean Enterprise Institute lexicon | Practitioner reference | https://www.lean.org/lexicon-terms/5-whys/ | n/d | full |
| LEI-GEMBA | Gemba / Gemba Walk | Lean Enterprise Institute lexicon | Practitioner reference | https://www.lean.org/lexicon-terms/gemba/ | n/d | full |
| LEI-VSM | Value-Stream Mapping | Lean Enterprise Institute lexicon | Practitioner reference | https://www.lean.org/lexicon-terms/value-stream-mapping/ | n/d | full |
| WIKI-5WHYS | Five whys | Wikipedia (criticism section citing Minoura and Card) | Secondary reference | https://en.wikipedia.org/wiki/Five_whys | accessed 2026-10-16 | full (secondary) |
| CARD-2017 | The problem with "5 whys", BMJ Quality & Safety 26(8):671–677 | Alan J. Card | Academic journal | https://qualitysafety.bmj.com/content/26/8/671 (doi 10.1136/bmjqs-2016-005849) | 2017 | search-only (publisher blocked) |
| ALTER-2014 | Theory of Workarounds, Communications of the AIS 34(55):1041–1066 | Steven Alter | Academic journal | https://aisel.aisnet.org/cais/vol34/iss1/55/ | 2014 | search-only (abstract read) |
| LEE-2025 | Making AI Functional with Workarounds: An Insider's Account of Invisible Labour in Organisational Politics | Lee, Narayan, Buckingham Shum, Ng, Kocaballi; ACIS 2025 (research in progress) | Academic preprint, single-case autoethnography | https://arxiv.org/abs/2512.21055 | 2025 | full |
| WIKI-TACIT | Tacit knowledge | Wikipedia (Polanyi 1966; Nonaka) | Secondary reference | https://en.wikipedia.org/wiki/Tacit_knowledge | accessed 2026-10-16 | full (secondary) |
| WIKI-PLANNING | Planning fallacy | Wikipedia (citing Buehler et al. 1994) | Secondary reference | https://en.wikipedia.org/wiki/Planning_fallacy | accessed 2026-10-16 | full (secondary) |
| WIKI-ELICIT | Requirements elicitation | Wikipedia (citing Christel and Kang 1992) | Secondary reference | https://en.wikipedia.org/wiki/Requirements_elicitation | accessed 2026-10-16 | full (secondary) |
| WIKI-BPD | Business process discovery | Wikipedia | Secondary reference | https://en.wikipedia.org/wiki/Business_process_discovery | accessed 2026-10-16 | full (secondary) |
| BCG-2025 | The Widening AI Value Gap (Build for the Future 2025) | Boston Consulting Group | Consultancy report | https://www.bcg.com/publications/2025/are-you-generating-value-from-ai-the-widening-gap | 2025-09 | full (read via an Internet Archive copy; publisher site blocked) |
| MIT-NANDA-2025 | The GenAI Divide: State of AI in Business 2025 | Challapally, Pease, Raskar, Chari; MIT NANDA | Research report (preliminary, non-peer-reviewed) | https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf (mirror) | 2025-07 | full |
| MCKINSEY-2025 | The state of AI in 2025: Agents, innovation, and transformation | McKinsey & Company (QuantumBlack) | Consultancy survey report | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | 2025 (exact date not confirmed) | search-only |
| MCKINSEY-QB-2025 | One year of agentic AI: Six lessons from the people doing the work | McKinsey & Company (QuantumBlack) | Consultancy article | https://www.mckinsey.com/capabilities/quantumblack/our-insights/one-year-of-agentic-ai-six-lessons-from-the-people-doing-the-work | 2025 (exact date not confirmed) | search-only |
| GARTNER-2025 | Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027 | Gartner | Analyst press release | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | June 2025 (exact day not confirmed) | search-only |
| MOLLICK-2023 | Centaurs and Cyborgs on the Jagged Frontier (reporting Dell'Acqua et al., SSRN 4573321) | Ethan Mollick, One Useful Thing | Co-author blog post | https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged | 2023-09-16 | full (post; paper not read) |
| METR-2025 | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | Becker et al. (METR); arXiv 2507.09089 | Academic preprint | https://arxiv.org/abs/2507.09089 | 2025-07 | full (abstract) |
| ELOUNDOU-2023 | GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models | Eloundou et al.; arXiv 2303.10130 | Academic preprint | https://arxiv.org/abs/2303.10130 | 2023-03 | full (abstract) |
| OPENAI-ACADEMY-2025 | Run a use case discovery workshop | OpenAI Academy | Vendor guide | https://academy.openai.com/home/clubs/champions-ecqup/resources/team-use-case-brainstorm-playbook-2025-09-15 | 2025-09-17, updated 2026-06-12 | full |
| CHRISTENSEN-2016 | Know Your Customers' "Jobs to Be Done" | Christensen, Hall, Dillon, Duncan; Harvard Business Review | Practitioner article | https://hbr.org/2016/09/know-your-customers-jobs-to-be-done | 2016-09 | search-only (abstract) |
| HAMMER-1990 | Reengineering Work: Don't Automate, Obliterate | Michael Hammer; Harvard Business Review | Practitioner article | https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate | 1990-07/08 | search-only (abstract) |
| FITZPATRICK-MOMTEST | The Mom Test | Rob Fitzpatrick (book; publisher site and reader summaries) | Practitioner book | https://www.momtestbook.com/ | n/d (book date not confirmed) | search-only |
| MOESTA-JTBD | Bob Moesta, Jobs-to-be-Done interview timeline and "struggling moment" (secondary write-ups of talks) | Bob Moesta / Re-Wired Group; Business of Software talk listing | Practitioner talk summaries | https://businessofsoftware.org/talks/live-jobs-to-be-done-case-studies/ | n/d | search-only |

---

## 10. Gaps

- **No direct evidence on AI-led process discovery inside organizations.** The strongest AI-interviewer evidence comes from surveys of the public or crowdworker samples (CHOPRA-2026, GEIECKE-2025, ANTHROPIC-INTERVIEWER-2025) and from small student or simulated studies (WUTTKE-2025, KORN-2025, LOJO-2025). Process-discovery chatbot work (KLIEVTSOVA-2024, DECASTRO-2025, ESTRADA-2025) is early, mostly about modelling or training.
- **No comparison of AI and human interviewers on volumes, times, workarounds or tacit knowledge.** Claims on those in section 3 are practitioner extensions supported by adjacent evidence.
- **No empirical test of "last time" versus "usually" questions in enterprise settings.** Support is practitioner consensus (NN/g, the Mom Test, JTBD) plus adjacent recall research.
- **Primary texts not accessed:**
  - Books: *The Mom Test*, Moesta and Re-Wired Group JTBD material, Beyer and Holtzblatt's *Contextual Design*, Small and Calarco's *Qualitative Literacy*, Dumas et al.'s *Fundamentals of Business Process Management*, and the BABOK Guide (the IIBA page I read was a landing page).
  - Articles: Klein et al.'s original CDM paper, Card's BMJ paper, Alter's full paper, Christensen's and Hammer's HBR articles beyond their abstracts, and Dell'Acqua et al.'s paper itself (read via Mollick's post).
  - Consultancy and analyst reports: McKinsey and Gartner were blocked or search-only, so figures from them are marked secondary.
- **The web-search budget ran out mid-task.** I could not search for several leads: laddering primary sources (Reynolds and Gutman), event storming, Ulwick's outcome-driven interviews, ABPMP CBOK, PMI business-analysis guidance, and any public interview playbooks from consulting firms. I fetched the event-storming site, but its content was too thin to use.
- **Few 2024–2026 consultancy publications on discovery interviewing itself.** The consultancy sources found cover AI value and redesign, not interview method. Vendor workshop guides exist (OPENAI-ACADEMY-2025; others appeared in search results but are marketing pages) and are not independent evidence.
- **Lead not used as evidence:** a 2026 *Safety* journal study on procedural adaptations, seen only in a search summary (reported 1,422 observed procedural steps with 32.9% adapted). I did not retrieve the paper, and the title was truncated in the result, so I did not cite it.
- **Senior-leader interviewing literature is academic research interviewing** (EMPSON-2018 on professional firms; GOLDMAN-SWAYZE-2012 on healthcare CEOs), not consulting discovery. Transfer is by analogy.
- **Several foundations rest on Wikipedia as a secondary source** (five whys critique, planning fallacy, tacit knowledge, requirements elicitation, process discovery). Verify against primary papers before relying on them for quantitative claims.
- **"Journey stage" is ambiguous in the brief.** I interpreted it as the advisor-loop sub-stage that the answer feeds (for example Map to Diagnose). If it means the user's AI-adoption maturity, the AI-baseline questions in Onboarding are the ones to retag.
- **Provenance caveats on figures:**
  - BCG, McKinsey and Gartner figures are consultancy or analyst outputs with executive self-report or non-random samples.
  - The MIT NANDA 95% figure is from a preliminary, non-peer-reviewed report with stated sample limitations.
  - The Anthropic figures are the vendor's own, with crowdworker or internal-employee samples.

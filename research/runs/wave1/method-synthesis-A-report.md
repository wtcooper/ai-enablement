# Method synthesis A: report

Stream M · Wave 1 · Editor A · 2026-10-16

**Files written** (in `plugins/transformation-advisor/skills/transformation-advisor/references/method/`):
`onboarding.md` (279 lines), `frame.md` (214), `map.md` (210), `diagnose.md` (243), `interviewing.md` (211),
`breakdown-and-rollup.md` (239). Each has a table of contents, goal and exit criteria, how to run it, a question bank
tagged by scope ([T] / [U/O]) and journey stage, expert moves, traps, a worked example (assurance throughout; a tax
script in `interviewing.md`), the output in spec §5.3 field names, and a source key list.
`python3 scripts/validate.py`: 0 errors (the only warning is the missing `SKILL.md`, expected from M2).

Not written (editor B): `reimagine.md`, `prioritize.md`, `business-case.md`, `plan-and-control.md`,
`people-and-change.md`, `index.md`. My files point to them by name.

## 1. Which inputs fed each file

| File | Main inputs | Supporting inputs |
|---|---|---|
| `onboarding.md` | ai-maturity (stage cards, markers, boundary probes, traps, the agentic tension), discovery-interviewing (primer, normalising AI-use questions, sequencing) | ai-transformation-evidence (adoption-versus-impact split, sponsor use, shadow use), change-workforce (worries, stigma), agentic-redesign (delegation gates: shadow mode, gating irreversible actions, override tracking), assurance controls-testing module (worked example, `#05`) |
| `frame.md` | pe-value-creation (thesis, full-potential pass, revolution / transformation / augmentation sort, Bain's five questions, who captures the gain, forcing-function substitutes), ai-transformation-evidence (ambition breadth, workflow-first question, ownership) | ai-maturity (pricing in fee-based work, Sage arithmetic, ambition by stage), value-measurement (seven levers and proof per lever, growth-measure association), change-workforce (capacity stance before the pilot), discovery-interviewing (leader answers as work-as-imagined, senior-interviewee prep, choosing what to map, visible-use-case bias) |
| `map.md` | discovery-interviewing (walk-through, quantify, tacit and workaround probes, observation, number labels, playback), lean-six-sigma (SIPOC, two times per step, flow metrics, process mining, shared definitions) | agentic-redesign (map-and-diagnose questions), ai-transformation-evidence (last month's volume), controls-testing module (worked example) |
| `diagnose.md` | lean-six-sigma (flow efficiency, Little's Law stability check, Kingman queue rule, constraint, five focusing steps, wastes, failure demand, rework, verification capacity, control charts) | value-measurement (speed-up ceiling, net time, segmenting by user), ai-transformation-evidence and discovery-interviewing (WORKBank four zones, jagged-frontier test, felt versus measured gains, data readiness), agentic-redesign (variance fit test, agent-readiness check), pe-value-creation (heatmap inputs: exposure sort, many people doing similar tasks, concentration), change-workforce (exposure is not a forecast), controls-testing module |
| `interviewing.md` | discovery-interviewing (operating rules, AI-interviewer evidence and failure modes, probe ladder, coverage list, playback, adapting to seniority, triangulation, workshops) | change-workforce (responding to fear, spec §9 rule 8), ai-maturity (normalising unapproved use) |
| `breakdown-and-rollup.md` | pe-value-creation (bridge discipline, standardized KPIs, cross-portfolio comparison, reuse, central versus local, concentration, denominators) | lean-six-sigma (shared definitions for roll-up), agentic-redesign (reuse case), change-workforce (roll-up people checks: junior pipeline, shared people resources, one message), value-measurement (no double counting), discovery-interviewing (seams for splitting), spec §4.3 and §7.4 (modes, subagent wording) |

## 2. Conflicts resolved

1. **First delegated (agentic) workflows at Adopting (the flagged open question).** Spec §3.2 puts them at Adopting;
   BCG puts agents after data foundations, scaled capabilities and governance; Deloitte finds about one in five firms
   with mature agent governance; McKinsey finds no more than 10% scaling agents in any one function. Against that, the
   controls-testing module shows bounded agent testing in internal audit teams that already own production workflows
   (`#05`). **Decision (in `onboarding.md` §5):** keep "first delegated workflows" at Adopting but make it *bounded and
   gated*: at most one or two, and only when five gates hold (workflow already in production with owner and baseline;
   written decision criteria with examples; reversible actions or human approval of irreversible ones; shadow-mode start
   with written promotion rules; control plan tracking overrides). A failed gate becomes a foundation item. Curious and
   Experimenting see delegate options only as inspiration and target picture; Scaling runs delegation as a governed
   portfolio; AI-native treats it as a default design option. Editor B's `reimagine.md` and `prioritize.md` already
   reference these gates. **Suggested spec §3.2 wording:** "Adopting: ... and the first *bounded* delegated workflows,
   once the delegation gates hold."
2. **Source keys.** The inputs used different keys for the same document and the same key for different documents.
   Normalized, and aligned with editor B's files: BCG value-gap study → `BCG-GAP-2025` (was BCG-2025, BCG-GAP-2025,
   BCG-VALUEGAP-2025); McKinsey State of AI → `MCKINSEY-SOAI-2025` (was MCKINSEY-2025, MCKINSEY-STATEOFAI-2025);
   WORKBank → `STANFORD-WORKBANK-2026` (was SHAO-2026, ARXIV-WORKBANK-2026); Wharton → `WHARTON-2025`, `WHARTON-2026`;
   MIT NANDA → `MIT-NANDA-2025`; KPMG Q3 2025 → `KPMG-AIPULSE-Q3-2025`; Eloundou → `ELOUNDOU-2023`; Workday →
   `WORKDAY-2026` (HCAMag coverage folded in); LEI value-stream page → `LEI-VSM-ND`; `TOCI-5FS`. **`DELOITTE-2026` named
   two different documents** (State of AI in the Enterprise; the PE report "Raising the game"); split into
   `DELOITTE-STATEAI-2026` and `DELOITTE-PE-2026`.
3. **McKinsey State of AI access.** Lean and discovery list it as search-only; ai-transformation-evidence read it in
   full via a third-party copy. I used only figures from the full read (88% use / 39% any EBIT effect; 55% vs 20%
   redesign; growth and innovation objectives; at most 10% scaling agents per function), all labelled self-reported.
4. **Workday rework share.** "About 37%" (lean, via trade coverage) versus "nearly 40%" (value-measurement, press
   release). Same survey; written as "about 37–40%", vendor-published, self-reported.
5. **Five different stage vocabularies** (maturity's five stages; PE's new / optimize / prove; evidence's explore /
   pilot / scale; lean's pre-pilot / pilot / scaled; discovery used "journey stage" to mean the loop sub-stage).
   All question banks are re-tagged to the spec's five journey stages.
6. **When to settle capacity use.** Change-workforce says decide where freed time goes before the pilot; the spec puts
   role evolution in Make the case. Resolved: a *provisional* capacity stance (redeploy or reduce, at role and capacity
   level) is recorded in Frame and settled per opportunity in Make the case.
7. **PE method without PE forcing functions.** PE practice assumes board control, equity incentives and an exit date;
   a unit leader has none. Resolved with an explicit substitutes question in Frame (F13: who holds the plan to account,
   with what budget, by when) and a trap entry.
8. **Duplicate "last month's volume" moves** in four inputs merged into one move, with the honest caveat that the
   supporting recall evidence (Bernard 1984) is adjacent (recalled events, not process volumes).
9. **Front-office versus back-office first** (MIT and BCG disagree, measuring different things). Not imported as a
   rule; Diagnose chooses units from the scope's own data and heatmap.
10. **The eighth waste** is named differently across sources; written as "unused talent", with the eight listed in plain words.

## 3. Gaps

- **Stage thresholds are untested.** The "ready for the next stage when" criteria, the Curious/Experimenting cut and
  the reuse discriminator for Adopting/Scaling are the maturity researcher's proposals. They need practitioner review
  against two or three real engagements. No study follows firms through stages.
- **No team-level markers for delegation** in any source; the five gates are a synthesis of guidance (OpenAI, BCG, IMDA), not tested thresholds.
- **Archetype-specific journey markers** (spec §6.7) belong in each `ARCHETYPE.md`, which does not exist yet. I did not
  mine `landscape-assurance.md` for them.
- **Tax examples are thin.** Only `interviewing.md` has a tax script (illustrative); the tax archetype is not researched yet.
- **Heuristics without evidence:** the unit heatmap scale, the unit-count rule, lever weighting by stage, scoring-weight
  adjustments, the coverage list and the probe ladder. All are labelled as advisor heuristics.
- **Interviewing evidence:** no study compares AI and human interviewers on eliciting volumes, times or workarounds
  inside organizations; AI-interviewer evidence comes from survey and student samples.
- **Lean in knowledge work:** no primary flow-efficiency benchmarks; Kingman not studied in office work; process-mining
  outcome data is vendor-sourced; several foundations rest on Wikipedia (Kingman, DMAIC, planning fallacy, five whys).
- **PE transfer** to non-PE units is unstudied; PMO structure for value-creation offices is not documented in public sources.
- **Schema gaps found while writing outputs:** `units[].status` has no defined values (I suggested not-started,
  desk-review, in-progress, complete); `profile.journey_stage` is a single value, so per-scope stages and the binding
  constraint live in the Profile body section (consider optional `journey_stage_by_scope` and `binding_constraint`
  fields); assurance module ids are not yet fixed in the vocabulary or an `ARCHETYPE.md`.
- **Worked-example dependency:** examples reuse figures from the verified controls-testing module (K-SOX30,
  CPAPA-ZANIN, OPTRO-SURVEY; `#03`, `#05`, `#07`, `#10`). If the module changes, recheck them.

## 4. Suggestions for the `SKILL.md` loop checklist

Three to five core questions per phase, in the plain wording the advisor should use.

**Onboard (0)**
1. What is your role, and what are you responsible for: your own work, a team, a function, a business unit or the whole organization?
2. What does your part of the business deliver, to whom, and how is it paid for?
3. In the last two weeks, who in your scope used AI on real work, and could you show me one example?
4. Why look at AI now, and what must not change?
5. What would make this session worth your time?
Exit: profile confirmed; stage placed from markers; path stated. Read now: `method/onboarding.md`.

**Frame (1)**
1. If this goes well, what will be different in twelve months, for your clients and your people?
2. If the tools were free and quality guaranteed, which piece of work would you rebuild?
3. How is the work paid for, and what happens to revenue or budget if it takes half the effort?
4. What would your finance lead or leadership accept as proof that this worked?
5. [U/O] Which parts of your area could AI threaten, which change a lot, and which mainly help?
Exit: ambition, measures, levers and weights, guardrails, owner, capacity stance. Read now: `method/frame.md`.

**Map (2)**
1. Think of the last [piece of work] you finished: what set it off, and what happened next?
2. How many did your team finish last month, and where does that number come from?
3. For that last one, how long did you work on it, and how long did it wait?
4. Where do you step outside the official process or tool, and why?
5. [U/O] Where do teams do the same work in different ways, and who owns the end result?
Exit: performed process with labelled numbers, played back; [U/O] value chain, shared definitions, units. Read now: `method/map.md` (and `method/interviewing.md` on first use).

**Diagnose (3)**
1. Where does work sit longest, and who is waiting for whom?
2. If this step were twice as fast, what would the next step see?
3. How often does work come back, and why?
4. What would happen if we stopped doing this step?
5. Who checks this work today, and how long does it take?
Exit: constraint named; waste, waits and rework counted; AI-fit signals; shortlist; [U/O] heatmap and waves. Read now: `method/diagnose.md`.

**Break down (in Map, [U/O])** — Where are the natural seams? Who owns each part, and how will it be planned? Which
measures will every part report the same way? Delegation: "Use subagents for desk reviews: one per unit, in parallel;
if you cannot, do each yourself." Read now: `method/breakdown-and-rollup.md`.

**Roll-up (in Prioritize, [U/O])** — Which ideas are the same across units? What would several units share? Taken
together, what do these plans do to entry-level hiring and training capacity? Delegation: "Use subagents: one
`rollup-unit` per child unit, in parallel; if you cannot, do each yourself." Read now: `method/breakdown-and-rollup.md`.

**Conductor-level rules worth lifting into `SKILL.md`:** one question mark per message (self-check before sending);
label every number reported / from record / observed; play back at the end of each segment with "What did I get
wrong, or miss?"; quote figures with provenance; plan the next journey stage only; apply the delegation gates before
planning any delegated workflow.

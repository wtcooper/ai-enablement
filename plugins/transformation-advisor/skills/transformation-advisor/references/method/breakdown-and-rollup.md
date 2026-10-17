# Break down and roll up

Read this at function, business-unit or organization scope: in Map, when the scope must be split into units, and in
Prioritize, when the units' plans come back. It covers choosing units, writing unit briefs, the three ways to plan a
unit (including desk reviews), and the roll-up. Source keys in brackets are listed in §10.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [Choosing units](#2-choosing-units)
3. [The unit brief](#3-the-unit-brief)
4. [Planning the units](#4-planning-the-units)
5. [Rolling up](#5-rolling-up)
6. [Question bank](#6-question-bank)
7. [Expert moves and common traps](#7-expert-moves-and-common-traps)
8. [Worked example](#8-worked-example)
9. [Output](#9-output)
10. [Sources](#10-sources)

## 1. Goal and exit criteria

**Goal.** Plan a large scope in depth without losing comparability: each unit gets its own plan, built on the
parent's settings and shared definitions, and the parent can merge them into one portfolio.

**Break down is complete (in Map) when:**
- Each unit has an id, a name, an owner (role), a wave and a planning mode, recorded in the parent's `units` list.
- Each wave-1 unit has a one-page `units/<id>/brief.md`.
- Shared definitions (done, rework, defect) and two or three common measures are written into every brief.
- The user knows how each unit will be planned and when results are due.

**Roll-up is complete (in Prioritize) when:**
- Every child unit's opportunities have been read, normalized and de-duplicated, with `rolled_up_from` set.
- Shared components and shared constraints are listed.
- Value is combined per lever without double counting, as ranges.
- Units are compared on the common measures, with denominators.
- People-side checks across units are done (pipeline, shared people resources, one workforce message).
- What is decided centrally and what each unit decides is stated. The merged list goes to `prioritize.md`.

## 2. Choosing units

A unit is a part of the scope that **needs its own plan**: its own work, an owner who can act on a plan, and work one
team can map. Use the value chain from Map and the heatmap from Diagnose.

- **Split where the plans would differ:** different work-type mix, different exposure to AI, or a different owner.
  PE operating teams assess AI disruption and opportunity company by company, then set targeted strategies
  [BCPARTNERS-2025; BAIN-DILIGENCE-2025].
- **Use the natural seams** the user names: service line, client type or process.
- **Do not just copy the org chart.** If one process crosses teams, make it one unit with a named end-to-end owner, or
  note the shared process in both briefs.
- **No more units in a wave than there are owners able to run them** (advisor heuristic). Group small parts; leave
  low-priority parts unplanned for now (`status: not-started`).
- **Ids** are short and stable, in lowercase with hyphens (for example `controls-testing`). Each unit folder mirrors
  the parent: `brief.md`, `transformation-plan.md`, `opportunities.yaml`, `evidence/`, and `units/` if it splits again.

## 3. The unit brief

One page. It must let someone who was not in the parent session start the unit's plan. Use this skeleton:

```markdown
# Unit brief: <unit name>
Unit id: <id> · Parent: ../../transformation-plan.md · Owner: <role> · Wave: <n> · Planning mode: delegate | same user | desk review · Due: <date>

## Why this unit
Two or three lines: its share of the scope, what Diagnose found, and why it is in this wave.

## What we already know
Findings from the parent's Map and Diagnose for this unit, each labelled reported, from record, observed, or outside-in.

## Inherited settings (change only with the parent owner's agreement)
Archetype and modules · value levers and weights · scoring weights · guardrails · overlay · capacity stance.

## Shared definitions and common measures
What "done", "rework" and "defect" mean; the two or three measures every unit reports, with units and period.

## Questions this plan must answer
Three to five, for example: where does work wait longest; which steps should stop; what would a newcomer do differently.

## What to prepare
Last month's volumes and the busiest week; two or three real examples of the work (no client-confidential data);
current process documents; a list of roles who do the work; current AI use, including unapproved tools.

## How to run it
Open this unit folder as the working folder and start the transformation advisor. It reads this brief, inherits the
settings, and starts at Frame. It saves after every phase. When done, tell the parent owner; share the folder as usual.

## What the parent needs back
`opportunities.yaml` using the shared vocabulary ids, value as ranges in the common measures with assumptions, risks,
human checkpoints and role evolution for each opportunity.
```

## 4. Planning the units

| Mode | Use when | How |
|---|---|---|
| **Delegates** | A head of AI or leader works top-down, and unit owners can give an hour or two | Each owner runs the plugin from the brief. The parent tracks `status` per unit |
| **Same user** | One leader wants depth and owns the units directly | Finish the parent's Map and Diagnose, then run the loop for one unit at a time, starting with wave 1 |
| **Desk review** | Speed matters, owners are not yet engaged, or the user wants a first view of every unit | First-pass plans from archetype knowledge, labelled **draft to validate** |

**Running desk reviews.** Use subagents for this step: delegate one subagent per unit with the `desk-review-unit`
brief, in parallel. Pass each the brief text, the unit brief, the parent settings, and the selected archetype's module
and use-case files. If you cannot start subagents, do each unit yourself, one at a time, to the same output. Each
returns a first-pass map, diagnosis and opportunities.

**Then, for every desk review:**
- Label it in the unit's plan and in the parent: **"Draft to validate with the people who do the work."** Set the unit's `status` to `desk-review`.
- Play back a short summary per unit to the user. Never present desk-review content as fact (rule 4 in `SKILL.md`).
- Add a **validation list** to the brief: the three numbers to replace with records, the two assumptions most likely
  to be wrong, and the roles to ask. Desk reviews describe work as imagined; only the people doing it know work as done [HOLLNAGEL-2017].
- Include desk-review opportunities in the roll-up only with their label, and do not let them drive a big bet alone.

## 5. Rolling up

1. **Check readiness.** List each unit's `status`: `complete`, `desk-review`, `in-progress` or `not-started`. Agree with the user
   whether to roll up now with what exists, or wait.
2. **Read the units.** Use subagents for this step: delegate one subagent per child unit with the `rollup-unit` brief,
   in parallel. If you cannot start subagents, process each unit yourself, one at a time. Each returns the unit's
   opportunities normalized and de-duplicated within the unit.
3. **Normalize across units:** vocabulary ids (work types, pattern, ladder, change scope, runtime class), lever ids,
   value units and periods (for example hours per year, cost per year, cycle time in days), and evidence labels.
4. **De-duplicate.** Opportunities with the same process and pattern in several units become one parent opportunity,
   with `rolled_up_from` listing each unit's path. Keep real differences in the description.
5. **Find shared components and constraints.** List capabilities several units need (document intake, evidence
   extraction, a search index, a review checklist, a data connection). Build once, reuse many times: McKinsey's
   practitioners call the reuse case the best use case (consultancy-reported) [MCKINSEY-1YR-2025]. List shared
   constraints too (one review team, one system, one specialist); they set the sequence.
6. **Combine value along the value tree.** Total per lever only after removing overlaps: if two opportunities claim the
   same hours or the same cost, count them once. Add lows to lows and highs to highs, and keep the assumptions. Treat
   the total like a value bridge: a planning device whose bars must each have an owner, not a causal proof
   [BDEMERSON-2026; CAPDYN-2014].
7. **Compare units on the common measures:** which move fast, which lag, which have the biggest effect
   [SIMONK-2025]. Show denominators and missing units; owner-published portfolio figures often cover selected companies
   only [VISTA-2026].
8. **Run the people checks across units:**
   - Do the units' hiring assumptions add up to fewer entry-level roles? Junior hiring is where the early labour-market
     effects show [STANFORD-CANARIES-2026; HARVARD-HOSSEINI-2026]. If so, plan how juniors will still learn.
   - Do several plans rely on the same managers, trainers or change support at the same time?
   - Is there one consistent message about roles, and does any unit's plan contradict it?
   - Does every opportunity have role evolution with an explicit redeploy-or-reduce choice (rule 2 in `SKILL.md`)?
9. **Decide central versus local.** Centralize first the rules (risk, security, confidentiality) and how value is
   measured; leave use-case design with the units [FTI-PLAYS-2024]. Reuse use cases proven in one unit before scaling
   frontier ideas [DELOITTE-PE-2026].
10. **Concentrate.** Put resources behind the units and initiatives with the most upside; do not spread effort evenly [BAIN-MIDYEAR-2026].
11. **Hand over** the merged list, shared components and people findings to `prioritize.md`.

## 6. Question bank

All questions are for unit or organization scope. Plain wording, one at a time.

**Break down**
- If we split your area into parts that each need their own plan, where are the natural seams: by service, client type or process?
- Which parts are affected by AI differently enough to need a separate plan?
- Which work crosses those parts, and who owns the end result?
- Who would own each part's plan? Could they run it themselves, or would you rather go deeper yourself, or have me draft a first pass?
- Which measures should every part report in the same way?
- Which ideas already proven in one team could be reused in others?
- When do you need the unit plans back?

**Roll-up**
- Which of these look like the same idea showing up in different units?
- Which tools, data connections or review steps would several units share?
- Where do units depend on the same people, such as one review team or specialist?
- Are the units' numbers comparable? What is each one based on?
- If resources were tight, which units would you slow down or stop?
- Taken together, what do these plans do to hiring, especially at entry level, and to training capacity?
- What should be decided centrally, and what should each unit decide for itself?

## 7. Expert moves and common traps

| Expert move | When | What it reveals |
|---|---|---|
| **Write shared definitions into every brief before any unit starts** | Break down | Whether roll-up will be possible; comparing units needs standardized measures and consistent reporting [KANBAN-GUIDE-2025; SIMONK-2025] |
| **Give every opportunity one owner, a baseline and a date,** and check for overlapping claims | Break down and roll-up | Unowned or double-counted value [BDEMERSON-2026] |
| **Rank initiatives across units by speed and effect on the same measures** | Roll-up | Patterns to double down on [SIMONK-2025] |
| **Hunt for the reuse case** | Roll-up | Shared components that make later units cheaper [MCKINSEY-1YR-2025] |
| **Reuse proven use cases first; treat frontier ones as bets** | Roll-up | Cheap wins versus risk [DELOITTE-PE-2026] |
| **Centralize rules and measurement first, leave design local** | Roll-up | A workable operating model; FTI warns that an AI operating model built for one portfolio company may not extend to the others (consultancy view) [FTI-PLAYS-2024] |
| **Ask for the denominator** of every unit's figures | Roll-up | Selective reporting; owner-published figures often cover a subset of units [VISTA-2026] |
| **Schedule a mid-point reset** and be ready to stop units that are not paying back | Plan | Plans run out of steam mid-way; resources should follow the winners [BAIN-MIDYEAR-2026] |

| Trap | How to avoid it |
|---|---|
| Too many units, so none gets depth | Waves; group small parts; no more units than active owners |
| Units that mirror the org chart while the work crosses it | Name end-to-end owners for cross-team processes |
| Each unit counts differently | Shared definitions and common measures in every brief |
| Desk reviews treated as fact | Label "draft to validate"; validation list; keep out of big bets alone |
| Double counting the same hours | Remove overlaps before totalling; one owner per claim |
| Spreading effort evenly | Fund the units with most upside [BAIN-MIDYEAR-2026] |
| Every unit builds its own tool | Look for shared components; centralize rules and measures [FTI-PLAYS-2024] |
| Hollowing out entry-level roles by accident across units | Run the pipeline check in roll-up |
| Briefs that cannot stand alone | Use the skeleton; test it by asking whether the owner could start without you |

## 8. Worked example

*Illustrative, continuing the regional audit practice.* After Map and Diagnose, the partner splits the practice by
module, using the assurance archetype's module list. **Controls testing** (wave 1, delegate: a senior manager runs the
plugin), **SOC and attestation** (wave 1, desk review), **substantive testing** (wave 2, not started). Every brief
carries the frame's levers and weights, the guardrail that a person signs off every conclusion, and three common
measures: hours per key control (or per SOC control), review notes per file, and days from evidence received to sign-off.

The SOC desk review comes back labelled "draft to validate", with a validation list: replace the estimated hours per
control with last season's time records; ask a SOC senior whether evidence requests really need two chases.

*Roll-up.* Both units propose an agent that checks client evidence submissions against the request before testing
(module `#03`). They become one parent opportunity with `rolled_up_from: [units/controls-testing, units/soc-attestation]`
and one shared component. Both also claim the same manager-review hours from AI secondary review (`#10`); the advisor
counts them once. The pipeline check finds that both plans move first-year staff from tick-and-tie to reviewing;
the parent plan adds a supervised rotation so juniors still learn testing judgment (module §7 notes the risk to
skill-building). Central decisions: tool approval and how hours are measured. Local: workflow design.

## 9. Output

**Parent plan.**
- Frontmatter `units`: `- { id: controls-testing, name: "Controls testing", owner: "Senior manager", wave: 1, status: in-progress }`.
  Use `status` values the user will recognise, such as not-started, desk-review, in-progress, complete.
- Body **Units** section: table of unit, owner (role), wave, planning mode, status, due date, brief path.
- Body **Roll-up** section (in Prioritize): merged opportunity list; shared components; shared constraints; overlaps
  removed and how; value per lever as ranges with assumptions; unit comparison on common measures with denominators;
  people checks; central versus local decisions.
- `opportunities.yaml` at the parent: merged items with `rolled_up_from: [ units/<id>, ... ]`.

**Each unit.** `units/<id>/brief.md` (§3). The unit's own `transformation-plan.md` sets `scope.parent` to the parent
plan's path and inherits `settings` unless overridden; overrides are listed in its Frame section.

## 10. Sources

- **BAIN-DILIGENCE-2025**: Bain & Company, *New Diligence Challenge: Uncovering AI Risks and Opportunities* (consultancy, 2025-10-27). https://www.bain.com/insights/new-diligence-challenge-uncovering-ai-risks-and-opportunities/
- **BAIN-MIDYEAR-2026**: Bain & Company, *Private Equity Midyear Report 2026* (consultancy, 2026-06-08). https://www.bain.com/insights/private-equity-midyear-report-2026/
- **BCPARTNERS-2025**: BC Partners, *Spotlight on Portfolio Operations: Cameron Hulett* (PE firm Q&A, 2025-01-08). https://www.bcpartners.com/news/spotlight-on-portfolio-operations-cameron-hulett/
- **BDEMERSON-2026**: BD Emerson, *The Value Creation Plan: How PE Firms Turn a Thesis into an Exit* (practitioner article, 2026-07-06, updated 2026-08-16). https://www.bdemerson.com/article/private-equity-value-creation-plan
- **CAPDYN-2014**: Capital Dynamics and TU München, *Value Creation in Private Equity* (academic–industry study, 2014-06). https://www.capdyn.com/Customer-Content/www/news/PDFs/1value-creation-in-private-equity-study-2014-finalv2.pdf
- **DELOITTE-PE-2026**: Deloitte, *Raising the game: PE operating partners and CFOs* (consultancy, 2026-04). https://www.deloitte.com/content/dam/assets-shared/docs/industries/financial-services/2026/raising-the-game.pdf
- **FTI-PLAYS-2024**: FTI Consulting, *AI in Private Equity: Three Plays for Driving Value Creation in 2025* (consultancy, 2024-12-04, updated 2026-05-22). https://www.fticonsulting.com/insights/articles/ai-private-equity-three-plays-driving-value-creation-2025
- **HARVARD-HOSSEINI-2026**: Hosseini, Lichtinger, *Generative AI as Seniority-Biased Technological Change* (academic working paper, 2026-05-06). https://raw.githack.com/s-mahdihosseini/Website/b99fa2962dcc4c165bbc3c41dd283afa99c5ccfb/GenAI_SenBTC_May_2026.pdf
- **HOLLNAGEL-2017**: Hollnagel, *Can we ever imagine how work is done?*, HindSight 25 (practitioner magazine, 2017). https://www.skybrary.aero/sites/default/files/bookshelf/3934.pdf
- **KANBAN-GUIDE-2025**: Vacanti, *The Kanban Guide* (professional guide, 2025-05). https://kanbanguides.org/english/
- **MCKINSEY-1YR-2025**: McKinsey, *One year of agentic AI: Six lessons from the people doing the work* (consultancy, 2025-09-12). https://www.mckinsey.com/capabilities/quantumblack/our-insights/one-year-of-agentic-ai-six-lessons-from-the-people-doing-the-work
- **SIMONK-2025**: Simon-Kucher, *The operational era of value creation accelerates* (consultancy survey, 2025-09-22). https://www.simon-kucher.com/en/insights/private-equity-operational-era-value-creation-accelerates
- **STANFORD-CANARIES-2026**: Brynjolfsson, Chandar, Chen, *Canaries in the Coal Mine?* (academic working paper, updated 2026-08). https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf
- **VISTA-2026**: Vista Equity Partners, *Software's Transition to Agentic Enterprise AI* (PE firm outlook, owner-reported, 2026-07). https://www.vistaequitypartners.com/wp-content/uploads/2026/07/Vista_Outlook_Softwares-Transition-to-Agentic-Enterprise-AI.pdf
- Assurance examples `#03`, `#10` and junior-role risk: `archetypes/assurance/modules/controls-testing.md` §3, §7.

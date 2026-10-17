# Spec: AI transformation advisor (v1)

From: [`intent/2026-10-16-ai-transformation-advisor.md`](../intent/2026-10-16-ai-transformation-advisor.md) · Date: 2026-10-16 · Status: draft (revision 6, after wave 1)

> This spec, the intent and `plan/` are how *we* build the plugin. None of that build process shows up
> in the product. This document says **what** v1 does and the rules it follows. Background reasoning
> is in [`docs/brainstorm/`](../docs/brainstorm/) and [`docs/research/`](../docs/research/).

---

## 1. Summary

A portable **Agent Plugin** with one skill, `transformation-advisor`. It guides anyone, from a team
lead to an audit partner to a head of AI, through transforming how their part of the business works
with AI.

The product rests on **two pillars**. Both must be expert-grade.

1. **The transformation workflow.** A single loop of reasoning that works at any level of the
   hierarchy (individual, team, function, business unit, organization):
   - The agent **onboards** the user: who they are, what kind of business they are in, how far along
     they are with AI, and what they need.
   - It **adapts** the path to that profile.
   - It then guides them through **frame → map → diagnose → reimagine → prioritize → make the case →
     plan**.
   - At higher levels, the same loop **breaks the scope into units** and **rolls up** the units' plans.
2. **Business archetypes.** Deep, researched knowledge of specific kinds of business:
   - its value chain and economics
   - how AI is actually being used there today, and where the field is heading
   - its regulations, workforce effects and disruption risks
   - how to interview someone from that business

   This content is built by a large fan-out of research subagents (§11). It is never generic filler.

The method uses lean and Six Sigma practice inside processes and the private-equity value-creation
structure at program level. Users only ever hear plain language. The organization's own content
lives in an **overlay** in its workspace, never in the plugin.

## 2. Scope

**The product** is only what ships inside `plugins/transformation-advisor/`: the orchestration skill,
the method logic, the archetype packs, the backbone library and the references they need. The research
program (§11) is a build activity that produces that content. Its tooling and raw output never ship.

**In v1**

- One skills-only plugin that conforms to Agent Plugins 1.0. It installs from this repo's GitHub
  marketplace, with installation verified in the target clients (§7.5).
- One skill: onboarding, adaptive path, transformation loop at any level, breaking down and
  rolling up, and an inspiration mode for users early in their journey.
- A file-based workspace that can live wherever the organization keeps information. A GitHub repo is
  the default example.
- **Method content** grounded in deep research on transformation practice (§11, stream M).
- **Business archetypes:** professional services (the base), assurance, and tax. Each is researched in
  depth (§11, stream A).
- **Backbone library:** work types, agentic patterns, runtime classes and function cards (§11,
  stream B).
- Subagent delegation in tool-agnostic wording, with an inline fallback (§7.4).
- An eval suite.

**Not in v1**

- Any backend, MCP server, telemetry or central library.
- Organization-specific content in the plugin repo.
- Approval or review workflows inside the product.
- Tool-specific agent definitions.
- Deal-team or due-diligence mode.
- Output to docs, slides or tickets. v1 writes markdown and YAML only.
- Building the automations that are recommended.

## 3. Onboarding and adaptation

### 3.1 Onboarding: building the profile

Onboarding is a short, conversational interview of about 5–10 questions, asked one at a time. Each
answer shapes the next question. It produces a **profile**, which is saved in the plan's frontmatter
(§5.3).

| Profile element | What the agent finds out | Example |
|---|---|---|
| **Role and scope** | Who the user is and what they are responsible for: individual, team, function, business unit or whole organization | An audit partner responsible for a regional practice |
| **Business archetype** | What kind of business it is, matched to an archetype and its modules (§6.8). If nothing matches: the closest base archetype plus function cards and, if the user agrees and the client has web access, **on-the-spot research** of a provisional archetype (§7.4) | Assurance → external audit of public companies, with controls testing and substantive testing as focus modules |
| **Journey stage** | How far along the scope is with AI (§6.7) | "Experimenting": individual use of chat tools, no shared workflows |
| **Goals and pressures** | Why now: margin, growth, talent, quality, client demand, competitors, regulation | Fee pressure on audits, staff shortages, inspection findings |
| **Constraints** | Regulation, independence, client confidentiality, data limits, risk appetite | Independence rules, firm policy on client data in AI tools |
| **Tools and data** | AI tools available (or the overlay catalog), core systems, data quality | An enterprise chat assistant, an audit platform, a data-analytics tool |
| **What they want from the session** | Quick wins, a full plan, a case for leadership, or just "show me what's possible" | A plan to take to the practice's leadership team |

The agent plays the profile back for confirmation. It can be edited at any time.

### 3.2 Adaptation

The profile sets the path through the loop:

| Journey stage | Emphasis |
|---|---|
| **Curious** | Start with an inspiration tour of real examples from the archetype. Explain the ladder (§6.2). Aim for two or three quick wins with existing tools. Keep mapping light |
| **Experimenting** | Move from individual use to shared team workflows. Find repeatable high-volume steps. Build the case for the first augmented or automated workflows |
| **Adopting** | Full loop. Focus on the processes behind real operations, data readiness, controls, and measured value. At most one or two **bounded** delegated workflows, and only when the five gates in the onboarding method file hold. Otherwise the missing gate becomes a foundation item |
| **Scaling** | Portfolio thinking. Platforms and capabilities several workflows can share. Operating model, governance, measuring value |
| **AI-native** | Reinvention. Business-model exposure, new services, pricing, AI-native competitors, workforce redesign |

| Scope | Adaptation |
|---|---|
| **Individual or team** | The loop runs on specific processes and steps. Output: a team transformation plan sequenced as Now, Next and Later |
| **Function or business unit** | The loop first runs on the value chain. Map breaks the scope into units. Units are planned in depth (by delegates, by the user, or as a first-pass desk review). The results are rolled up |
| **Organization** | Same as a business unit, plus business-model exposure, a value tree, workstreams sequenced by dependency, and a value creation plan |

**Resume.** If the working folder has a plan, the agent reads its state (`phase_completed`,
`next_phase`) and offers to continue.

## 4. The transformation workflow

### 4.1 One loop, any level

| Phase | Purpose | At team level | At unit or organization level |
|---|---|---|---|
| **0. Onboard** | Profile and adapted path (§3) | — | — |
| **1. Frame** | Ambition, why now, what success looks like, value levers | Team goals and pain points | Ambition, **business-model exposure**, value tree and scoring weights (the settings children inherit) |
| **2. Map** | Make the current work visible | Processes: trigger → steps → handoffs → output, with volumes, time, systems and rework | Value chain and units. **Break down:** create a unit for each part that needs its own plan |
| **3. Diagnose** | Find where value leaks | Waste, bottlenecks, variation, rework; work type per step | Outside-in heatmap per unit: size, work-type mix, AI exposure, strategic weight, readiness. Choose which units go first |
| **4. Reimagine** | Generate options through four lenses (§4.2) | For each high-value step | For each unit or value-chain stage, including new services and pricing |
| **5. Prioritize** | Score and sort into quick win, foundation, big bet or park. Sequence by dependencies | Team opportunities | **Roll up** the units' plans: remove duplicates, find shared platforms, combine value along the value tree |
| **6. Make the case** | Value as ranges with assumptions, risks, human checkpoints, **role evolution** | Top three to five | Top initiatives and the portfolio as a whole |
| **7. Plan** | Actions, owners, KPIs, control plan, rhythm. Steps sequenced by dependency, not calendar deadlines | Now, Next and Later | Workstreams, a value creation plan and a review cadence |

### 4.2 The four lenses of Reimagine

The agent goes through these lenses in order, so it doesn't stop at personal efficiency:

1. **Improve the step.** Assist or augment the people doing the work.
2. **Automate the flow.** Remove people from the normal path, and send exceptions to people.
3. **Delegate the outcome.** An agent owns a multi-step outcome, with human checkpoints.
4. **Reinvent the work.** Should this process exist at all? What would an AI-native competitor do?
   What new service or pricing model becomes possible?

Each lens draws on the archetype's use cases and frontier signals, and on the pattern library. The
lenses are prompts for the conversation. The data records each option's **ladder** level and
**change scope** (§6.2).

**Quoting evidence.** Most published outcome figures are self-reported or vendor-published. The pilot
found no independent measure of AI test quality in controls testing. When the agent quotes a figure,
it states the provenance.

### 4.3 Breaking down and rolling up

- **Break down.** In the Map phase at higher levels, the agent creates a child **unit** for each part
  that needs a deeper plan. Each unit gets its own folder with a one-page brief. The brief includes
  the settings it inherits, what to prepare, and how to run the plugin.
- **Planning units.** Each unit runs the same loop, starting from its brief. Three ways to run it:
  - **Delegates** (the head-of-AI top-down case) each run the plugin for their unit.
  - The **same user** goes deeper, one unit at a time.
  - The agent runs a **first-pass desk review** of each unit in parallel subagents, using the archetype
    knowledge. The result is clearly labelled as a draft to validate with the people who do the work.
- **Roll-up** reads every child unit's opportunities, which subagents work through one unit each in
  parallel. It then merges them into the parent's Prioritize phase.

### 4.4 Conversation rules

- Ask **one question at a time**. Play back what was heard.
- Use **plain language**. Method terms are optional, explained in one line when used.
- **Adapt depth.** Skip what is known. Go deep where pain or value is high.
- **Show progress.** Name the phase and what comes next.
- **Write as you go.** Save after every phase. State lives in the plan file.
- **Bring evidence in early.** Use real archetype examples, with evidence grades, from onboarding
  onward.
- **Use expert moves.** Each phase reference gives the probing questions, heuristics and common traps
  an experienced transformation lead would use (§6.1).
- **Be candid about people** (§9).

## 5. Workspace (file protocol)

### 5.1 Principles

- **Store anywhere.** The workspace is a plain folder of markdown and YAML. The plugin only reads and
  writes local files. It can live in a git repo, SharePoint, OneDrive, Google Drive or a shared drive.
- **GitHub by default.** This repo provides a workspace template (`templates/workspace/`). Nothing
  depends on git.
- **Sharing is the user's choice.** At the end of each session the agent says which files to share
  and suggests how. There is **no approval step** in the product.
- **Confidentiality.** The agent reminds users once per session not to add client-confidential data
  or personal information beyond names and roles.

### 5.2 Layout (recursive)

```
<workspace>/
├── transformation-plan.md        # the top scope, at whatever level the user started
├── opportunities.yaml
├── overlay/                      # optional organization-specific content (§6.10)
├── evidence/                     # documents the user provided
└── units/
    └── <unit-id>/                # one child scope created by Break down; same files, recursively
        ├── brief.md
        ├── transformation-plan.md
        ├── opportunities.yaml
        ├── evidence/
        └── units/…
```

There is no separate charter. The top plan's **settings** (value levers, scoring weights,
guardrails, archetype) are inherited by every child unit, unless the unit overrides them.

### 5.3 Schemas (required fields; full schemas in the skill's `schemas/`)

**`transformation-plan.md` frontmatter**

```yaml
schema: plan/v1
scope: { name, level: individual | team | function | business-unit | organization, parent: path | null }
author: { name, role }
profile:
  archetype: id                   # e.g. assurance
  modules: [ id ]                 # e.g. [ controls-testing, substantive-testing ]
  journey_stage: curious | experimenting | adopting | scaling | ai-native
  goals: [ string ]
  constraints: [ string ]
  tools: [ string ]
  session_goal: string
settings:                         # set at the top level, inherited by children
  value_levers: [ { id, name, metric, weight } ]
  scoring_weights: { value, feasibility, data_readiness, risk, time_to_value, strategic_fit }
  guardrails: [ string ]
  overlay: overlay/ | null
units: [ { id, name, owner, wave, status } ]      # present after Break down
status: in-progress | complete
phase_completed: 0–7
next_phase: 0–7 | null
updated: date
```

The body has one section per phase and starts with a one-screen summary and a progress checklist.

**`opportunities.yaml`**

```yaml
schema: opportunities/v1
scope: path
items:
  - id: string
    title: string
    process: string
    work_types: [ id ]
    pattern: id
    ladder: assist | augment | automate | delegate
    change_scope: step | process | model
    runtime_class: id
    description: string            # today → future
    value: [ { lever, low, high, unit, assumptions } ]
    scores: { value, feasibility, data_readiness, risk, time_to_value, strategic_fit }   # 1–5
    weighted_score: number
    category: quick-win | foundation | big-bet | park
    prerequisites: [ string ]
    risks: [ string ]
    human_checkpoints: [ string ]
    role_evolution: { tasks_moving, new_work, capacity_use }
    evidence: [ use_case_id ]      # archetype or overlay use cases that support it
    rolled_up_from: [ path ]       # set by Roll-up
    next_step: { action, owner, depends_on }   # sequenced by dependency, no dates
```

## 6. Knowledge model

All content is generic and public, and written as plain names and descriptions. It cites no external
framework IDs.

### 6.1 Method (pillar 1)

There is one reference file per phase plus cross-cutting files. Each phase file contains:

- the **goal and exit criteria**
- a **question bank**, by scope level and journey stage
- **expert moves**: the probes, heuristics and analyses an experienced transformation lead uses.
  Examples: "ask for last month's volume, not a typical week"; "find the step where work waits
  longest"; "ask what would happen if this report stopped being produced"
- **common traps**: automating waste, local optimization, pilots with no control plan, value claims
  with no baseline
- **worked examples** drawn from the archetypes
- the **output format**

The content is grounded in research stream M (§11). It covers:

- lean and Six Sigma applied to knowledge work
- PE value-creation practice (diagnostic, value creation plan, workstreams, program office cadence)
- current AI transformation frameworks and evidence
- agentic workflow redesign
- AI maturity models
- change management and the workforce
- value measurement
- process-discovery interviewing

### 6.2 The ladder and change scope

Every opportunity and use case is classified on **two independent dimensions**. The pilot showed
that a single combined scale was ambiguous: researchers disagreed on 8 of 18 merged items.

**Ladder: how much the AI does**

| Level | Meaning |
|---|---|
| **Assist** | AI helps a person with a task the person still owns |
| **Augment** | AI is built into a step, gives a first pass, and a person reviews it |
| **Automate** | A defined step runs with no person on the normal path. Exceptions go to people |
| **Delegate** | An agent owns a multi-step outcome across systems, started by events, with human checkpoints |

**Change scope: what changes**

| Scope | Meaning |
|---|---|
| **Step** | One step of the existing process gets better |
| **Process** | The flow is redesigned: steps removed or merged, work made continuous, or done on full populations |
| **Model** | The service, business or operating model changes: new services, pricing, sourcing, who does the work |

The four Reimagine lenses (§4.2) are conversation prompts that map onto these:

| Lens | Ladder | Change scope |
|---|---|---|
| Improve | assist or augment | step |
| Automate | automate | step or process |
| Delegate | delegate | process |
| Reinvent | any | model, or a process that stops existing |

### 6.3 Work types

These describe how work is done. They drive which patterns fit.

| Work type | Description |
|---|---|
| Review & assurance | Checking work, evidence or compliance against criteria |
| Transaction & case processing | High-volume, rule-heavy items moving through defined steps |
| Expert judgment & advice | Specialist decisions and recommendations under ambiguity |
| Research & synthesis | Gathering, comparing and condensing information from many sources |
| Document & content production | Creating reports, deliverables and communications |
| Client & customer interaction | Answering, serving and managing relationships |
| Coordination & scheduling | Planning, resourcing, handoffs and status tracking |
| Data & reporting | Collecting, reconciling and analyzing data, and producing metrics |
| Software & systems work | Building, configuring and maintaining technology |
| Physical & field operations | Hands-on work, where AI supports planning, inspection and guidance |

### 6.4 Runtime classes (vendor-neutral; the overlay maps them to products)

| Class | Description |
|---|---|
| Personal assistant | Chat or coding assistant used by one person |
| Shared team skills | Packaged prompts, skills or plugins used the same way across a team |
| Workflow automation with AI steps | A defined workflow on an automation platform, with AI at some steps |
| Background / scheduled agent | An agent that runs on a schedule or trigger without a person present |
| Managed agent runtime | A hosted, long-running agent with tools, state and human checkpoints, built into business systems |

### 6.5 Agentic pattern library

Each pattern records: name, description, the work types it fits, its ladder range, runtime class,
human checkpoints, prerequisites, failure modes, and value levers. The initial set:

intake & triage · document-to-decision · research & brief · draft–review loop ·
full-population testing · monitor → diagnose → act · reconcile & handle exceptions ·
service agent with escalation · grounded knowledge assistant · end-to-end case agent ·
bulk transformation and migration.

### 6.6 Value tree, scoring and function cards

**Default value levers:** capacity, speed, quality, growth, cost, risk, experience. The top-level
plan chooses and weights them.

**Scoring dimensions and default weights:**

| Dimension | Default weight |
|---|---|
| Value | 0.30 |
| Feasibility | 0.20 |
| Data readiness | 0.15 |
| Risk (higher score = lower risk) | 0.15 |
| Time to value | 0.10 |
| Strategic fit | 0.10 |

**Categories:** quick win, foundation, big bet, park.

**Function cards** cover strategy & planning; sales, marketing & business development; product &
service development; service delivery & operations; customer service; people (HR); technology (IT);
finance & accounting; procurement & supply chain; risk, compliance & legal. Each card has its
processes, pain points, top opportunities, metrics and interview probes.

### 6.7 Journey stages

The five stages are **Curious → Experimenting → Adopting → Scaling → AI-native**. Each stage has:

- observable **markers** that the onboarding questions detect
- the typical **blockers**
- what to emphasize (§3.2)

Each archetype adds field-specific markers. For example, in assurance, "Adopting" might mean data
analytics used on most engagements and AI first-pass review of evidence on some.

### 6.8 Business archetypes (pillar 2)

**Inclusion test.** An archetype covers one distinct value chain. It must change at least three of the
following compared with the backbone: the core value chain, the use cases, the guardrails, the value
metrics.

- A candidate that changes fewer is a **module** inside an archetype.
- A difference in vocabulary only goes in the overlay glossary.
- An archetype may **extend** another. For example, assurance and tax extend professional services.

**Anatomy: what "deep" means.** Every archetype contains all of the following, researched and sourced:

```
archetypes/<id>/
├── ARCHETYPE.md          # ≤ 100 lines: what it covers, modules, extends, how to recognize it, journey markers
├── interview-guide.md    # archetype-specific onboarding and phase questions; vocabulary to mirror
├── value-chain.md        # stages → processes → key steps, each tagged with work types
├── economics.md          # how it makes money, key metrics and benchmarks, cost structure, pricing pressure from AI
├── state-of-ai.md        # adoption today: what leaders are doing, survey data, maturity spread (dated)
├── frontier.md           # where the field is heading (12–36 months): conference and proceedings signals, emerging agentic uses, AI-native entrants
├── guardrails.md         # regulators, standards, professional obligations, data rules, steps needing human judgment
├── workforce.md          # roles, the talent model and pyramid, how roles evolve, skills, the apprenticeship question
├── disruption.md         # business-model scenarios: AI-native competitors, pricing shifts, new services
├── objections.md         # common concerns from this field and evidence-based responses
├── modules/<m>.md        # per module: processes, pain points, probes, top opportunities, metrics
├── use-cases/<m>.yaml    # §6.9 schema; one file per module
└── sources.md            # source landscape: key conferences, bodies, journals, publications; last researched date
```

**v1 archetypes and modules**

| Archetype | Extends | Modules |
|---|---|---|
| professional-services | — | pursuit & proposals · acceptance & risk · scoping & pricing · staffing & resourcing · delivery management · quality review · billing & collections · knowledge management |
| assurance | professional-services | acceptance & independence · planning & risk assessment · controls testing · substantive testing (including journal-entry and fraud testing) · specialists (using the work of experts) · completion & reporting · quality management (firm level and engagement level) · SOC & attestation · sustainability assurance · assurance over AI. The module list was revised in wave 1 from the landscape evidence |
| tax | professional-services | compliance · provision · indirect tax · transfer pricing · international & global minimum tax · controversy · research & advisory · tax data & technology |

**Content targets per archetype**

| Content | Target |
|---|---|
| Use cases per module | 15–25 |
| Evidence mix per module | At least 50% graded A or B **where public evidence exists**. Grades are never inflated to meet the target. Modules that can't meet it honestly are rated *thin* in `ARCHETYPE.md`, and the advisor uses them for risk awareness and interview probes rather than proof points |
| Frontier signals in `frontier.md` | At least 10, each dated and sourced |
| Interview guide | Questions for every phase, plus journey-stage markers |
| Sources | Every file has dated sources and a `last_researched` date |

Consulting is not an archetype. Consulting teams use professional services, the function cards, and
their client's archetype once one exists. Assurance and tax also serve in-house internal-audit and
corporate tax teams.

### 6.9 Use-case entry schema

```yaml
- id: string                       # <archetype>-<module>-NN or fn-<function>-NN
  title: string
  archetype: id | null
  module: id | null
  function: id
  work_types: [ id ]
  pattern: id
  ladder: assist | augment | automate | delegate
  change_scope: step | process | model
  runtime_class: id
  maturity: in-production | piloting | announced | emerging   # where the field actually is
  problem: string
  solution: string
  outcomes: [ { lever, description, figure, measures, provenance, source_ref } ]   # provenance: self-reported | vendor-published | independent
  prerequisites: [ string ]
  risks_and_guardrails: [ string ]
  human_checkpoints: [ string ]
  role_evolution: string
  evidence_grade: A | B | C | D
  sources: [ { ref, title, publisher, type, url, date, access, locator } ]   # access: full | search-only
  last_reviewed: date
```

### 6.10 Organization overlay

This is how organization-specific content gets in **without changing the plugin**. The overlay lives
in the workspace and uses the same schemas.

| File | Effect |
|---|---|
| `tool-catalog.yaml` | Maps runtime classes to enabled products. Anything outside it is flagged |
| `glossary.md` | Organization terminology |
| `guardrails.md` | Added to the plugin rules. Never weakens §9 |
| `use-cases.yaml` | Internal examples, labelled "internal" |
| `archetypes/<id>/` | Private archetypes, or extensions of plugin archetypes |

**Order of precedence:** overlay > plan settings > archetype > backbone. The §9 rules cannot be
overridden.

## 7. Plugin architecture

### 7.1 One skill

The plugin has **one skill**, `transformation-advisor`. Team-level and organization-level work are the
same loop at different scopes, and inspiration is a journey-stage path rather than a separate job.
So one skill is the coherent unit. This also removes the risks of handing off between skills and
reading across skill folders, which the structure research identified
([`docs/research/2026-10-16-skill-structure.md`](../docs/research/2026-10-16-skill-structure.md)).

What makes one skill workable is **where the routing lives**. Pointers sit at the step that needs
them, not in one long list, and the plan file's state tells the agent which step it is on.

### 7.2 `SKILL.md`: the conductor (target ≤ 400 lines, hard limit 500)

Ordered so the most important content falls within the first ~5,000 tokens, which survive context
compaction:

1. The purpose, in two or three sentences.
2. The rules in §9, in short form.
3. **Start or resume.** Look for a plan, read its state, and continue or onboard.
4. **The onboarding checklist** (§3.1), with a pointer to the onboarding reference and the archetype
   index.
5. **The loop checklist** (§4.1). For each phase:
   - the goal
   - three to five core questions
   - exit criteria
   - the output
   - **one "read now" pointer** to that phase's method file
   - any delegation instruction
   - "update the plan state"
6. **Scope adaptations:** Break down and Roll-up (§4.3), with their pointers.
7. **Library entry points:** the three index files (method, library, archetypes) and how to search
   use cases.
8. Workspace and sharing conventions (§5).

### 7.3 References

```
skills/transformation-advisor/
├── SKILL.md
└── references/
    ├── method/                     # pillar 1: one file per phase + cross-cutting
    │   ├── index.md
    │   ├── onboarding.md           # question bank, archetype detection, journey-stage markers
    │   ├── frame.md · map.md · diagnose.md · reimagine.md · prioritize.md · business-case.md · plan-and-control.md
    │   ├── breakdown-and-rollup.md
    │   ├── people-and-change.md
    │   └── interviewing.md
    ├── library/                    # backbone
    │   ├── index.md                # ladder, work types, runtime classes, value tree, scoring, journey stages (short tables)
    │   ├── patterns/<id>.md
    │   └── functions/<id>.md
    ├── archetypes/                 # pillar 2
    │   ├── index.md                # one row per archetype: recognition cues, modules, extends
    │   └── <id>/…                  # §6.8 anatomy
    ├── briefs/                     # subagent briefs (§7.4)
    ├── schemas/
    └── templates/
```

**Navigation rules**

- **Phase files are pointed to directly** from the loop checklist, one per phase, at the moment
  they're needed. That is about 12 pointers, each attached to a step.
- **Everything else goes through an index.** There are three entry points: `method/index.md`,
  `library/index.md` and `archetypes/index.md`. Each index is a short table (name, when to read,
  one-line summary) that leads to exactly one more file. Inside an archetype, `ARCHETYPE.md` is the
  index for its files.
- **Size.** Each file has one job and stays under about 300 lines. Files over 100 lines start with a
  table of contents.
- **Search, don't read.** Use-case YAML has consistent fields (`module:`, `pattern:`, `work_types:`,
  `ladder:`, `change_scope:`, `maturity:`). The agent or a subagent searches instead of reading whole files.
- **State is memory.** After every phase the agent updates `phase_completed`, `next_phase` and the
  progress checklist. A long session never depends on the agent remembering a file it read earlier.

### 7.4 Subagents (tool-agnostic)

**Rules**

1. **Explicit, tool-agnostic wording.** The skill names the delegation outright. Codex, for example,
   spawns subagents only when asked explicitly. Typical wording: "Use subagents for this step:
   delegate one subagent per X, in parallel. If you cannot start subagents, do each yourself, one at
   a time."
2. **Self-contained briefs.** The main agent reads a brief from `briefs/` and passes its full text,
   the inputs and the output schema in the subagent prompt.
3. **Subagents never talk to the user.** Results are drafts the main agent plays back to the user.
4. **Structured, compact returns.**
5. **The inline fallback gives the same contract.**

| Brief | Phase | Fan-out | Returns |
|---|---|---|---|
| `analyze-document` | Map | One per document | Draft process steps, roles, volumes and systems, each marked as stated or inferred |
| `scout-use-cases` | Reimagine | One per high-value step or unit | A shortlist of five or fewer use cases and patterns, with fit and evidence grade |
| `desk-review-unit` | Break down (optional) | One per unit | A first-pass map, diagnosis and opportunities from archetype knowledge, labelled "draft to validate" |
| `review-opportunities` | Before Make the case (optional) | One per top opportunity | Independent check of score, risks, checkpoints, role evolution and the §9 rules |
| `rollup-unit` | Prioritize (higher levels) | One per child unit | Normalized, de-duplicated opportunities ready to merge |
| `research-archetype` | Onboard, only when no archetype matches, the user agrees, and the client has web access | A landscape pass, then one per focus area × angle (a lighter version of the build recipe in §11) | A **provisional** archetype folder in the workspace overlay (`overlay/archetypes/<id>/`) with the same anatomy, sources and evidence grades, labelled "provisional" |

### 7.5 Packaging and marketplace

The plugin is skills-only, so the Agent Plugins 1.0 root manifest works across clients. Each client
still needs its own marketplace index.

```
ai-enablement/                               # this repo = the marketplace
├── .claude-plugin/marketplace.json          # Claude Code, Cowork, VS Code; fallback for Codex and Copilot CLI
├── .agents/plugins/marketplace.json         # Codex / ChatGPT desktop ("local" source + policy fields)
├── .github/plugin/marketplace.json          # Copilot CLI preferred path (optional)
├── .cursor-plugin/marketplace.json          # Cursor (source must be a folder inside this repo)
└── plugins/transformation-advisor/
    ├── plugin.json                          # Agent Plugins 1.0 ($schema)
    ├── .claude-plugin/plugin.json
    ├── .cursor-plugin/plugin.json
    └── skills/transformation-advisor/       # §7.2–7.3
```

**Per-client rules**

- In-repo `./plugins/transformation-advisor` sources everywhere.
- The same `name` in every index and manifest.
- No top-level `bin/` folder.
- Codex index entries set `policy.installation: AVAILABLE` and `policy.authentication: ON_INSTALL`.

**Target clients** (installation is verified in `plan/`):

| Client | Install |
|---|---|
| Claude Code and Claude desktop (Cowork) | `/plugin marketplace add <owner>/<repo>`, or Customize > Plugins |
| Codex CLI / app and ChatGPT desktop | `codex plugin marketplace add <owner>/<repo>` |
| Cursor | `agent plugin marketplace add <git-url>` |
| GitHub Copilot CLI | `copilot plugin marketplace add <owner>/<repo>` |
| VS Code with Copilot | `chat.plugins.marketplaces` setting |

## 8. Outputs

| Output | Format |
|---|---|
| Transformation plan (any level): profile, summary, phases, and next steps sequenced as Now, Next and Later | `transformation-plan.md` |
| Opportunities | `opportunities.yaml` |
| Unit brief | `units/<id>/brief.md` (one page) |
| Business case, one page per top opportunity | A section in the plan |
| Portfolio, workstreams, value creation plan, cadence (higher levels) | Sections in the top plan |
| Leadership summary | A section that can be pasted elsewhere |

## 9. Behavioral rules (cannot be overridden)

1. **Never** recommend actions about named individuals, rate individual performance, or set
   headcount targets for people.
2. **Always** include role evolution for opportunities at team level and above, with an explicit
   choice of capacity use: **redeploy** (growth, quality, backlog, new services) versus **reduce**
   cost. Discuss cost-out openly at the level of roles and capacity.
3. **Always** give value as ranges with stated assumptions. Label the evidence grade when citing
   examples. Never give a single-point ROI.
4. **Never** invent sources or figures. Examples come from the archetypes, library or overlay, or are
   labelled as illustrative. Desk reviews and provisional research are always labelled.
5. **Don't** ask for client-confidential data or sensitive personal data. Remind the user once per
   session.
6. When an overlay catalog exists, recommend tools from it. Otherwise use runtime classes.
7. The advisor designs and plans. It does not claim to build or deploy anything.
8. When a user expresses fear about their role, acknowledge it honestly. Don't falsely reassure. Help
   the user position themselves as the person leading the change.
9. Plans are sequenced by **steps and dependencies**, never by artificial deadlines (no 30/60/90-day or
   100-day plans). Dates belong in the user's own planning tools if they need them.

## 10. Quality and acceptance

### Evals

`evals/` holds 30–50 scenarios, each with a persona, a scripted user, the expected behaviors, and the
checks. The minimum coverage:

- **An audit partner transforming their practice**, end to end. This is the reference scenario.
- A tax leader at the "Curious" stage, who should get the inspiration-first path.
- A head of AI breaking a professional-services firm into units and rolling up desk reviews.
- A team lead with uploaded documents.
- A corporate tax department, where the archetype serves an in-house team.
- A business with no matching archetype, with and without on-the-spot research.
- Personas: an anxious user, and a skeptic who wants hard ROI.
- A request for cuts targeting named people.
- An overlay with a tool catalog.
- Resume after compaction or restart.
- A run without subagents.
- **Depth checks:**
  - recommendations cite archetype use cases relevant to the module discussed
  - the Reimagine phase reaches delegate-level and model-scope options when the journey stage warrants it
  - each phase's expert moves are used
- **Navigation checks:**
  - phase files are read at their phase
  - only the selected archetype and modules are loaded

Checks combine **schema validation** of the files written with **rubric grading** of the
conversation. A subject-matter reviewer grades the reference scenarios for professional
credibility.

### v1 acceptance criteria

- **Installation:** the plugin installs from this repo and the skill loads in Claude Code or Cowork,
  Codex or ChatGPT desktop, Cursor, and Copilot CLI or VS Code.
- **Size:** `SKILL.md` stays within its budget, and every reference file follows the §7.3 rules.
- **Flows:** onboarding, the loop at team and organization level, Break down, desk review, Roll-up and
  resume all produce valid files.
- **Content:** all three archetypes meet the §6.8 anatomy and targets. Method files exist for every
  phase, with expert moves grounded in stream M sources.
- **Evals:** the suite passes its agreed threshold. All §9 rules pass on every relevant scenario.

## 11. Research program

This is the largest part of the build. Content comes **only from public sources**. It is gathered by
fanning out many research subagents, each told to research deeply across **every kind of material**,
not just one source type.

### 11.1 Three streams

| Stream | Produces | Rough fan-out |
|---|---|---|
| **M: Method** | `method/*`: expert moves, question banks, traps and examples for each phase. Covers lean / Six Sigma for knowledge work, PE value creation, AI transformation frameworks and evidence, agentic workflow redesign, maturity models, change and the workforce, value measurement, discovery interviewing | About 10 topic agents, then synthesis |
| **A: Archetypes** | Everything in §6.8 for each archetype | Per archetype: 1 landscape scan, then 3 angles per module (8 modules × 3 = 24 agents), then cross-cutting agents for economics, workforce, disruption, guardrails and the state of AI. About 30 or more agents per archetype |
| **B: Backbone library** | Patterns, function cards, work types, journey stages | About 15 agents |

All three streams finish with **synthesis** and **verification** agents (§11.4). At about 130 or more
agents in total, the program runs in waves (see `plan/`).

### 11.2 How deep the archetype research goes

1. **Landscape scan (one agent per archetype).** Build `sources.md`: the field's main conferences and
   their 2025–2026 programs and proceedings, standard-setters and regulators, professional bodies,
   academic journals and research centers, leading firms' public reports, vendors and product
   launches, trade press, podcasts and practitioner communities. Confirm or adjust the module list.
   Starting points to confirm:
   - **Assurance:** AICPA & CIMA ENGAGE; the AICPA Conference on Current SEC and PCAOB Developments;
     the Rutgers World Continuous Auditing & Reporting Symposium; American Accounting Association
     meetings; IIA conferences (internal audit); ISACA (IT audit); PCAOB, IAASB and Center for Audit
     Quality publications.
   - **Tax:** TEI conferences; AICPA tax tracks; the IFA Congress; OECD Forum on Tax Administration
     work; IRS and other tax authority AI programs; tax-technology vendor conferences.
   - **Professional services:** firm operations and legal operations events (as analogs), and
     professional-services benchmark research.
2. **Module deep dives (three angles per module, each its own subagent):**
   - **Practice.** What firms and in-house teams actually do: case studies, firm reports, vendor
     deployments, job postings and product launches that signal real use.
   - **Discourse.** What practitioners say: conference sessions and proceedings from the last 12–18
     months, panels, keynotes, podcasts, practitioner articles and community discussion. This angle
     carries the most weight for `frontier.md`.
   - **Governance & evidence.** What constrains and measures the work: regulator and standard-setter
     statements, inspection findings, professional-body guidance, academic studies and surveys.
3. **Cross-cutting agents per archetype:** economics and business model, workforce and talent model,
   disruption scenarios, guardrails, state of AI adoption.

### 11.3 Source rules

- Public sources only. Record publisher, type and date for every source.
- Prefer the last 12–18 months. Older sources are allowed for foundations, standards and history.
- Summarize in our own words. No long quotations.
- No confidential, client-identifying or organization-internal material.

### 11.4 Synthesis and verification

- **Synthesis agent per module:** merges the three angles, removes duplicates, maps entries to
  patterns, work types, ladder levels and change scope, and writes the module file and use-case YAML.
- **Verifier agent per module:** checks every claim against its cited source, assigns the evidence
  grade (A: a measured outcome from a named organization; B: a named deployment; C: a vendor claim or
  analyst estimate; D: a plausible idea, labelled "idea"), and rejects anything unsupported.
- **Schema validation** runs on every file.
- **Review** of the merged content before it is committed. The research logs are kept in `research/`.

### 11.5 Keeping it current

Every archetype file carries `last_researched`. The research briefs live in `research/briefs/` so the
same fan-out can be rerun, ideally twice a year, to refresh `state-of-ai.md`, `frontier.md` and the
use cases.

## 12. Answers to intent questions

| Intent question | Answer |
|---|---|
| Use-case library sourcing | Deep public research (§11) plus the organization overlay |
| Where outputs go | Markdown and YAML in the workspace (§8) |
| Program workspace location | Anywhere. GitHub template by default (§5) |
| Clients | Agent Plugins compatible. Verified in Claude Code / Cowork, Codex / ChatGPT desktop, Cursor, Copilot CLI / VS Code (§7.5) |
| First archetypes | Professional services, assurance, tax (§6.8) |
| Framework IDs (APQC) | Not used |

## 13. Open questions and items to verify in `plan/`

**On-the-spot research** (`research-archetype`) is optional. It is a fallback for businesses the
built archetypes don't cover, not the main source of depth. Most of the depth comes from archetypes
researched during the build (§11). A provisional archetype saved in an overlay can later be
promoted: rerun it through the full build recipe and add it to the plugin.


1. **Install details not yet confirmed:**
   - how ChatGPT desktop installs plugins
   - whether Cursor falls back to `.claude-plugin`
   - which index path VS Code reads
   - whether Cowork accepts a root `plugin.json`
2. **Delegation reliability.** Check that the explicit wording triggers subagents in each client,
   especially Codex.
3. **Research waves.** Run a pilot on one module first (for example, assurance controls testing) to
   calibrate depth and the schema before the full fan-out.
4. **Subject-matter review.** Who reviews archetype content for professional credibility (an audit
   professional and a tax professional)?
5. **Eval harness.** How to run scenarios across clients in a repeatable way.

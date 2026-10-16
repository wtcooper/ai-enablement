# Spec: AI transformation advisor (v1)

From: [`intent/2026-10-16-ai-transformation-advisor.md`](../intent/2026-10-16-ai-transformation-advisor.md) · Date: 2026-10-16 · Status: draft (revision 2)

> This spec, the intent and `plan/` are how *we* build the plugin. None of that build process shows up
> in the product. This document says **what** v1 does and the rules it follows. Background reasoning
> is in [`docs/brainstorm/`](../docs/brainstorm/).

---

## 1. Summary

A portable **Agent Plugin** that guides a *program lead* (a head of AI or business-unit leader) and
their *team delegates* through a top-down AI transformation of a business unit:

- The **lead** frames the ambition, splits the unit into pillars and teams, and writes a **charter**.
- Each **delegate** runs guided discovery for their team, and the agent writes them a **team
  transformation plan**.
- The **lead** combines the team plans into a scored **portfolio** and a **roadmap** (a 100-day plan
  and a value creation plan).

The method uses the private-equity value-creation program structure for the lead and lean / Six
Sigma practice for team discovery. Users only ever hear plain language. A common **backbone**
provides the method and general knowledge. Optional **domain packs** add depth for specific kinds
of business. The organization's own content lives in an **overlay** inside its workspace, never in
the plugin.

**Design principle: progressive disclosure.** The skill entry point is a short router. All method,
flow and domain logic sits in reference files that are loaded only when the current step needs them
(§7.2).

## 2. Scope

**In v1**

- One skills-only plugin that conforms to Agent Plugins 1.0. It installs from this repo's GitHub
  marketplace, with installation verified in the target clients (§7.4).
- Program lead flow, team delegate flow, and a light "explore" entry for inspiration.
- A file-based program workspace that can live wherever the organization keeps information. A GitHub
  repo is the default example.
- Backbone knowledge: the method, the ladder, work archetypes, agentic patterns, function cards,
  the value tree and scoring, and people and change.
- Domain packs: **professional-services**, **assurance** and **tax**, filled with researched public
  use cases (§11).
- Subagent delegation described in tool-agnostic wording, with an inline fallback (§7.3).
- An eval suite.

**Not in v1**

- Any backend, MCP server, telemetry or central library.
- Organization-specific content of any kind in the plugin repo.
- Approval or review workflows inside the product.
- Tool-specific agent definitions (for example `agents/*.md` or `.agent.md`).
- Deal-team or due-diligence mode.
- Individual-contributor mode as a separate flow.
- Output to docs, slides or tickets. v1 writes markdown and YAML only.
- Building the automations that are recommended.

## 3. Users and entry

| Role | Goal | Main outputs |
|---|---|---|
| **Program lead** | Transform a business unit top-down | `charter.md`, team briefs, `portfolio.md` / `portfolio.yaml`, `roadmap.md` |
| **Team delegate** | Get a transformation plan for their team and start acting on it | `transformation-plan.md`, `opportunities.yaml` |
| **Explorer** (anyone) | See what's possible before committing | No files required |

**Entry triage** (in `SKILL.md`). The orchestrator first looks for a workspace in the working folder.

- **No `charter.md` found:** ask whether the user is setting up a program (lead flow), working on one
  team without a program (team flow with default settings), or just exploring.
- **`charter.md` found:** ask which role the user has.
  - A *delegate* is matched to their pillar and team in the charter.
  - If a plan is already in progress, **resume** from its `phase_completed`.

## 4. Experience flows

### 4.1 Conversation rules (all flows)

- Ask **one question at a time**. Play back what was heard before moving on.
- Use **plain language**. Method terms are never required of the user. They may appear in an output,
  explained in one line.
- **Adapt depth** to the user's answers. Skip what is already known. Go deeper where pain or value is
  high.
- **Show progress.** Name the current phase and what comes next.
- **Write as you go.** Save each phase to the workspace, so a session can stop and resume.
- **Pull examples in early.** Show relevant use cases from the start, not only at the end.
- **Be candid about people** (§9).

### 4.2 Program lead flow

| Phase | Purpose | Produces |
|---|---|---|
| **1. Ambition** | Why transform. What "good" looks like in 12–24 months. Constraints. **Business-model exposure**: where AI threatens or reshapes how the unit earns money | Charter: ambition and exposure |
| **2. Structure** | Split the unit into pillars and teams. Name a delegate for each team. Choose which packs apply | Charter: pillars, teams, packs |
| **3. Outside-in diagnostic** | For each pillar, estimate size, work-archetype mix, AI exposure, strategic weight and readiness. Choose **discovery waves**: which pillars go first | Charter: heatmap and waves |
| **4. Value tree and rules** | Choose and weight value levers. Adjust scoring weights. Set guardrails. Point to the overlay's tool catalog | Charter: value tree, scoring, guardrails |
| **5. Launch** | Generate a one-page **team brief** per team: what to prepare, how to install and run the plugin, where to save the plan, and when it is due | `teams/<pillar>/<team>/brief.md` |
| **6. Synthesize** | Combine the team plans that exist. Remove duplicates, find shared platforms and dependencies, roll value up the value tree, and sort into quick wins, foundations and big bets | `portfolio.md`, `portfolio.yaml` |
| **7. Roadmap** | A 100-day plan (quick wins, foundations, governance). A value creation plan (initiatives tied to levers, owners, KPIs, baselines, targets). A review cadence | `roadmap.md` |
| **8. Refresh** (repeat) | Update progress against KPIs. Re-prioritize. Start the next wave | Updated portfolio and roadmap |

### 4.3 Team delegate flow

| Phase | Purpose | Produces |
|---|---|---|
| **0. Orient** | Read the charter, if one exists. Confirm the team, scope and timing. Explain how the session works | — |
| **1. Frame** | The team's purpose, customers, outputs, pain points, and what success means | Plan: frame |
| **2. Map** | Walk the main processes: trigger → steps → handoffs → output, with volumes, time, systems, decisions and rework. Documents can be analyzed in parallel by subagents (§7.3) | Plan: process maps |
| **3. Diagnose** | Find waste, the bottleneck, and failure points. Tag each step with its work archetype | Plan: diagnosis |
| **4. Imagine** | For each high-value step, find patterns and examples, gathered by subagents in parallel (§7.3). Ask "what would an AI-native competitor do?" Place ideas on the ladder | Draft opportunities |
| **5. Prioritize** | Score with the charter's rubric, or the default one. Sort into quick win, foundation, big bet or park | `opportunities.yaml` |
| **6. Make the case** | For the top three to five: value as ranges with assumptions, prerequisites, risks, human checkpoints, and **role evolution** | Plan: business cases |
| **7. Plan and share** | A **"start this week"** list the team can act on now with the tools it already has. A 30/60/90-day plan. A control plan (metrics, baselines, evals, checkpoints). Mark the plan `complete`. Explain where to save or share it so the program lead can include it | Plan: actions, control, next steps |

The team plan is useful to the team **on its own**. It is not only an input to the lead's portfolio.

### 4.4 Explore (light)

Browse use cases and patterns by function, pack, work archetype or ladder level. Explain one example
in depth. Offer to start a team plan or a program. This is what replaces the old "art of the
possible" mode.

## 5. Program workspace (file protocol)

### 5.1 Principles

- **Store anywhere.** The workspace is a plain folder of markdown and YAML. The plugin only reads and
  writes local files and never calls a storage API. It can live wherever the organization keeps
  information: a git repo, SharePoint, OneDrive, Google Drive or a shared drive.
- **GitHub by default.** This repo provides a workspace template (`templates/workspace/`). A lead who
  uses GitHub creates the program repo from it, and delegates work in a clone. Nothing in the plugin
  depends on git.
- **Sharing is the user's choice.** At the end of each flow the agent says which files to share and
  suggests how, based on what it can see (for example "commit and push" in a git folder, otherwise
  "copy this folder to your program's shared location"). There is **no approval step** in the product.
- **Works without a program.** With no charter, the team flow writes a plan in the current folder
  using default settings. A lead can bring it into a program later.
- **Confidentiality.** The agent reminds users once per session not to add client-confidential data
  or personal information beyond names and roles.

### 5.2 Layout

```
<program-workspace>/
├── charter.md
├── overlay/                      # optional organization-specific content (§6.9)
│   ├── tool-catalog.yaml
│   ├── glossary.md
│   ├── guardrails.md
│   ├── use-cases.yaml
│   └── packs/<id>/               # optional private packs, same anatomy as plugin packs
├── teams/
│   └── <pillar-id>/<team-id>/
│       ├── brief.md
│       ├── transformation-plan.md
│       ├── opportunities.yaml
│       └── evidence/
├── portfolio.md
├── portfolio.yaml
└── roadmap.md
```

### 5.3 Schemas (required fields; full schemas live in `references/schemas/`)

**`charter.md` frontmatter**

```yaml
schema: charter/v1
program: string
lead: { name, role }
version: int                       # bump on change; team plans record which version they used
horizon_months: int
ambition: string
pillars:
  - id, name, owner
    teams: [ { id, name, delegate, wave } ]
packs: [ professional-services, tax ]
value_levers: [ { id, name, metric, weight } ]       # weights sum to 1
scoring_weights: { value, feasibility, data_readiness, risk, time_to_value, strategic_fit }
guardrails: [ string ]
overlay: overlay/                  # optional
```

**`opportunities.yaml`**

```yaml
schema: opportunities/v1
program, pillar, team, charter_version   # program fields are null in single-team mode
items:
  - id: string                     # <team-id>-NN
    title: string
    process: string
    work_archetypes: [ id ]
    pattern: id
    ladder: assist | augment | automate | delegate | reinvent
    runtime_class: id
    description: string            # today → future, two or three sentences
    value: [ { lever, low, high, unit, assumptions } ]
    scores: { value, feasibility, data_readiness, risk, time_to_value, strategic_fit }   # 1–5
    weighted_score: number
    category: quick-win | foundation | big-bet | park
    prerequisites: [ string ]
    risks: [ string ]
    human_checkpoints: [ string ]
    role_evolution: { tasks_moving, new_work, capacity_use }
    related_use_cases: [ id ]
    next_step: { action, owner, by }
```

**`transformation-plan.md` frontmatter**: `schema: team-plan/v1`, `program`, `pillar`, `team`,
`author`, `charter_version`, `status: in-progress | complete`, `phase_completed: 0–7`, `updated`. The
body has one section per phase, and starts with a one-screen summary.

**`portfolio.yaml`** combines the opportunity items and adds `portfolio_id`, `source_teams`,
`merged_from`, `shared_platform` and `dependencies`.

## 6. Knowledge model (backbone)

All backbone content is generic and public, and written as plain names and descriptions. It cites no
external taxonomy IDs. Each topic below is its own reference file (§7.2).

### 6.1 The ladder

| Level | Meaning | Example |
|---|---|---|
| **Assist** | AI helps a person with a task the person still owns | Drafting a memo with a chat assistant |
| **Augment** | AI is built into a step, gives a first pass, and a person reviews it. Shared prompts or skills make it consistent | An AI first-pass contract review against a checklist |
| **Automate** | A defined step runs with no person on the normal path. Exceptions go to people | Extracting and validating document data straight into a system |
| **Delegate** | An agent owns a multi-step outcome across systems. It is started by events and runs in the background, with human checkpoints | An agent that prepares a full draft workpaper from several systems |
| **Reinvent** | The process, service or business model is redesigned because AI makes a different way possible | Continuous monitoring instead of periodic review. Outcome-based pricing |

### 6.2 Work archetypes

| Archetype | Description |
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

### 6.3 Runtime classes (vendor-neutral; the overlay maps them to products)

| Class | Description |
|---|---|
| Personal assistant | Chat or coding assistant used by one person |
| Shared team skills | Packaged prompts, skills or plugins the whole team uses the same way |
| Workflow automation with AI steps | A defined workflow on an automation platform, with AI at some steps |
| Background / scheduled agent | An agent that runs on a schedule or trigger without a person present |
| Managed agent runtime | A hosted, long-running agent with tools, state and human checkpoints, built into business systems |

### 6.4 Agentic pattern library

Each pattern records: name, description, the work archetypes it fits, its ladder range, runtime
class, human checkpoints, prerequisites, typical failure modes, and value levers. The initial set:

intake & triage · document-to-decision · research & brief · draft–review loop ·
full-population testing · monitor → diagnose → act · reconcile & handle exceptions ·
service agent with escalation · grounded knowledge assistant · end-to-end case agent ·
bulk transformation and migration.

### 6.5 Value tree and scoring

**Default value levers** (the charter chooses and weights them):

| Lever | Metric |
|---|---|
| Capacity | Hours released |
| Speed | Cycle time |
| Quality | Errors and rework |
| Growth | Revenue, new services, win rate |
| Cost | External spend, cost to serve |
| Risk | Compliance exposure, control coverage |
| Experience | Client and employee experience |

**Scoring:** six dimensions on a 1–5 scale, each with anchored definitions. The default weights are:

| Dimension | Default weight |
|---|---|
| Value | 0.30 |
| Feasibility | 0.20 |
| Data readiness | 0.15 |
| Risk (higher score = lower risk) | 0.15 |
| Time to value | 0.10 |
| Strategic fit | 0.10 |

**Categories:**

| Category | When it applies |
|---|---|
| Quick win | High score and under 90 days |
| Foundation | Enables several other opportunities |
| Big bet | High value, longer horizon, usually Delegate or Reinvent |
| Park | Everything else |

### 6.6 Function cards

Short cards for the support functions every business has: strategy & planning; sales, marketing &
business development; product & service development; service delivery & operations; customer
service; people (HR); technology (IT); finance & accounting; procurement & supply chain; risk,
compliance & legal.

Each card has: typical processes, common pain points, top opportunities with links to patterns,
metrics, and interview probes.

### 6.7 Domain packs

**Inclusion test.** A pack covers one distinct value chain. It must change at least three of the
following compared with the backbone: the core value chain, the use-case library, the guardrails,
the value metrics. A candidate that changes fewer becomes a **module** inside a pack. A difference in
vocabulary only goes in the overlay glossary.

**Anatomy**

```
packs/<id>/
├── PACK.md                  # short: id, name, extends, modules, when to use; read first
├── value-chain.md           # stages → processes, each tagged with work archetypes
├── modules/<m>.md           # processes, pain points, interview probes, top opportunities
├── use-cases/<m>.yaml       # §6.8 schema; one file per module so loads stay small
├── metrics.md               # value levers and KPIs, with typical ranges and sources
├── guardrails.md            # standards, regulators, independence, data limits, steps needing human judgment
├── roles.md                 # common roles and how they might evolve
└── disruption.md            # AI-native competitor scenarios
```

**v1 packs**

| Pack | Extends | Modules |
|---|---|---|
| professional-services | — | pursuit & proposals · acceptance & risk · scoping & pricing · staffing & resourcing · delivery management · quality review · billing & collections · knowledge management |
| assurance | professional-services | acceptance & independence · planning & risk assessment · controls testing · substantive testing · specialists (IT, valuation) · completion & reporting · quality management · other assurance (SOC, sustainability) |
| tax | professional-services | compliance · provision · indirect tax · transfer pricing · international & global minimum tax · controversy · research & advisory · tax data & technology |

Consulting is not a pack. Consulting teams use professional-services, the function cards, and the
pack for their client's industry once one exists. The assurance and tax packs also serve in-house
internal-audit and corporate tax teams.

### 6.8 Use-case entry schema

```yaml
- id: string                       # <pack>-<module>-NN or fn-<function>-NN
  title: string
  pack: id | null                  # null for function cards
  module: id | null
  function: id
  work_archetypes: [ id ]
  pattern: id
  ladder: assist | augment | automate | delegate | reinvent
  runtime_class: id
  problem: string
  solution: string                 # how AI changes the work; no product names unless in the source
  outcomes: [ { lever, description, figure, source_ref } ]
  prerequisites: [ string ]
  risks_and_guardrails: [ string ]
  human_checkpoints: [ string ]
  role_evolution: string
  evidence_grade: A | B | C | D    # §11.3
  sources: [ { ref, title, publisher, url, date } ]
  last_reviewed: date
```

### 6.9 Organization overlay

This is how organization-specific content gets in **without changing the plugin**. The overlay lives
in the organization's workspace (§5.2) and uses the same schemas.

| File | Effect |
|---|---|
| `tool-catalog.yaml` | Maps runtime classes to the organization's enabled products. Recommendations name these products. Anything outside the catalog is flagged as "not currently available" |
| `glossary.md` | Organization terminology |
| `guardrails.md` | Added to the plugin rules. Can never weaken §9 |
| `use-cases.yaml` | Internal examples, shown alongside public ones and labelled "internal" |
| `packs/<id>/` | Private packs. If an id matches a plugin pack, the private pack extends it |

**Order of precedence:** overlay > charter > packs > backbone. The rules in §9 cannot be overridden.

## 7. Plugin architecture

### 7.1 One skill, many reference files

The plugin contains **one skill**, `transformation-advisor`. Everything else is reference material
inside that skill's folder. This is the most portable setup:

- It doesn't depend on how clients resolve paths between skills or to the plugin root.
- It needs no tool-specific agent files.

### 7.2 Progressive disclosure

```
skills/transformation-advisor/
├── SKILL.md                         # the router; target ≤ 150 lines, hard limit 500
└── references/
    ├── flows/                       # what happens in each flow, phase by phase
    │   ├── program-lead.md
    │   ├── team-plan.md
    │   └── explore.md
    ├── phases/                      # how to run each phase: questions, probes, exit criteria, output
    │   ├── ambition-and-exposure.md
    │   ├── structure-and-diagnostic.md
    │   ├── value-tree-and-rules.md
    │   ├── team-briefs.md
    │   ├── frame-and-map.md
    │   ├── diagnose.md
    │   ├── imagine.md
    │   ├── prioritize.md
    │   ├── business-case.md
    │   ├── team-actions-and-control.md
    │   ├── synthesize.md
    │   └── roadmap.md
    ├── method/                      # the shared knowledge model (§6.1–6.5)
    │   ├── conversation-rules.md
    │   ├── ladder.md
    │   ├── work-archetypes.md
    │   ├── runtime-classes.md
    │   ├── value-tree-and-scoring.md
    │   └── people-and-change.md
    ├── patterns/                    # one file per agentic pattern, plus index.md
    ├── functions/                   # one file per function card, plus index.md
    ├── packs/<id>/                  # §6.7
    ├── subagents/                   # self-contained subagent briefs (§7.3)
    │   ├── analyze-document.md
    │   ├── scout-use-cases.md
    │   ├── review-opportunities.md
    │   └── synthesize-pillar.md
    ├── schemas/                     # charter, team-plan, opportunities, portfolio, use-case
    └── templates/                   # skeleton files the agent fills in
```

**What `SKILL.md` contains, and nothing more:**

1. The purpose, in two or three sentences.
2. The rules in §9, in short form. They must always be in context.
3. Entry triage (§3).
4. A **load map**: a table of "when you are at X, read Y", covering every flow, phase, method file,
   pattern or function index, pack, subagent brief and schema. Every reference is linked from
   `SKILL.md` directly (one level deep). Reference files may mention one another, but the load map
   is the authority on what to read and when.
5. Workspace conventions (§5) in short form.
6. A short note on delegation (§7.3).

**Rules for reference files**

- **Size.** Each file has one job and stays under about 300 lines. Files over 100 lines start with a
  table of contents.
- **Load only what the step needs.** Read a flow file at the start of a flow, then each phase file as
  you enter that phase. Read method files when a phase calls for them. Read pack modules and use
  cases only for the processes being discussed.
- **Indexes before detail.** Read `index.md` in patterns or functions, or a pack's `PACK.md`, before
  any detail file.
- **Large lookups go to subagents.** Searching the use-case library across packs is done inside a
  subagent where possible (§7.3), so the main conversation receives only a shortlist.

### 7.3 Subagents (tool-agnostic)

Research findings:

- Claude Code, Cowork, Codex, Cursor and the Copilot CLI / VS Code agent all support subagents that
  can run in parallel.
- **Codex** spawns them only when skill instructions *explicitly* ask for subagents, delegation or
  parallel agent work.
- In Claude Code and VS Code, **subagents cannot ask the user questions**, and no client passes chat
  history to a subagent.
- Plain chat surfaces without subagents run the work inline.

**Rules**

1. **Explicit, tool-agnostic wording.** The skill names the delegation outright. For example: "Use
   subagents for this step: delegate one subagent per document, in parallel. If you cannot start
   subagents, process each document yourself, one at a time." It never names a client's tool.
2. **Self-contained briefs.** The orchestrator reads the brief in `references/subagents/`, then
   passes the brief's full text, the inputs (file paths or excerpts) and the output schema in the
   subagent's prompt. Subagents never depend on chat history or on resolving the skill's paths.
3. **Subagents never talk to the user.** All questions and confirmations stay in the main
   conversation. Subagent results are drafts the orchestrator plays back to the user.
4. **Structured returns.** Each brief defines a compact output (YAML or markdown in the schema
   format), so results stay small.
5. **Inline fallback is always correct.** The same brief, run inline one item at a time, gives the
   same contract.

| Brief | When | Fan-out | Returns |
|---|---|---|---|
| `analyze-document` | Map phase, when the user provides SOPs, process documents, org charts or exports | One per document | Draft process steps, roles, volumes and systems, each marked as stated or inferred |
| `scout-use-cases` | Imagine phase | One per high-value process step, or per pack module | A shortlist of five or fewer relevant patterns and use cases, with ids, a one-line fit and evidence grades |
| `review-opportunities` | After Prioritize, before Make the case | One per top opportunity (optional) | Independent check of score, risks, human checkpoints, role evolution and the §9 rules |
| `synthesize-pillar` | Lead's Synthesize phase | One per pillar | Merged and de-duplicated opportunities for that pillar. The main agent then combines all pillars |

### 7.4 Packaging and marketplace

The plugin is **skills-only**: no agents, commands, hooks or MCP. That means the Agent Plugins 1.0
root manifest works across clients without losing components. Each client still needs its own
marketplace index, plus the small per-client tweaks below.

```
ai-enablement/                               # this repo = the marketplace
├── .claude-plugin/marketplace.json          # Claude Code, Cowork, VS Code; fallback for Codex and Copilot CLI
├── .agents/plugins/marketplace.json         # Codex / ChatGPT desktop ("local" source + policy fields)
├── .github/plugin/marketplace.json          # Copilot CLI preferred path (optional)
├── .cursor-plugin/marketplace.json          # Cursor (source must be a folder inside this repo)
└── plugins/transformation-advisor/
    ├── plugin.json                          # Agent Plugins 1.0 ($schema); Copilot and Codex use this first
    ├── .claude-plugin/plugin.json           # Claude Code and Cowork
    ├── .cursor-plugin/plugin.json           # Cursor
    └── skills/transformation-advisor/       # §7.2
```

**Per-client rules**

- Every index uses an in-repo `./plugins/transformation-advisor` source. That is the only form all
  clients accept: Cursor resolves sources only as folders inside the repo, and Codex skips `github`
  sources.
- Plugin `name` matches in every index and manifest.
- No top-level `bin/` folder (Cowork rejects plugins that have one).
- Codex index entries set `policy.installation: AVAILABLE` and `policy.authentication: ON_INSTALL`.

**Target clients** (installation is verified in `plan/`):

| Client | Install |
|---|---|
| Claude Code and Claude desktop (Cowork) | `/plugin marketplace add <owner>/<repo>`, or Customize > Plugins |
| Codex CLI / app and ChatGPT desktop | `codex plugin marketplace add <owner>/<repo>` |
| Cursor | `agent plugin marketplace add <git-url>`, or `/plugins` |
| GitHub Copilot CLI | `copilot plugin marketplace add <owner>/<repo>` |
| VS Code with Copilot | `chat.plugins.marketplaces` setting |

## 8. Outputs

| Output | Who | Format |
|---|---|---|
| Charter | Lead | `charter.md` |
| Team brief | Lead → delegate | `brief.md` (one page) |
| Team transformation plan | Delegate | `transformation-plan.md` and `opportunities.yaml` |
| Business case (one page per top opportunity) | Delegate | Section in the team plan |
| Portfolio | Lead | `portfolio.md` and `portfolio.yaml` |
| Roadmap: 100-day plan, value creation plan, cadence | Lead | `roadmap.md` |
| Leadership summary | Lead | A section in `roadmap.md` that can be pasted elsewhere |

## 9. Behavioral rules (cannot be overridden)

1. **Never** recommend actions about named individuals, rate individual performance, or set
   headcount targets for people.
2. **Always** include role evolution for team-level and program-level opportunities, with an explicit
   choice of capacity use: **redeploy** (growth, quality, backlog, new services) versus **reduce**
   cost. Discuss cost-out openly at the level of roles and capacity.
3. **Always** give value as ranges with stated assumptions. Label the evidence grade when citing
   examples. Never give a single-point ROI.
4. **Never** invent sources or figures. Examples come from the library or overlay, or are clearly
   labelled as illustrative.
5. **Don't** ask for client-confidential data or sensitive personal data. Remind the user once per
   session.
6. When an overlay catalog exists, recommend tools from it. Otherwise use runtime classes.
7. The advisor designs and plans. It does not claim to build or deploy anything.
8. When a user expresses fear about their role, acknowledge it honestly. Don't falsely reassure. Help
   the user position themselves as the person leading the change.

## 10. Quality and acceptance

### Evals

`evals/` holds 20–50 scenarios, each with a persona, a scripted user, the expected behaviors, and the
checks. The minimum coverage:

- Lead sets up a Big 4 tax-practice program.
- Delegate in an audit team, with and without uploaded documents.
- Anxious delegate.
- Skeptical lead who wants hard ROI.
- Request for cuts targeting named people.
- Team with no matching pack.
- Single-team mode with no charter.
- Overlay present, and a recommendation outside the catalog.
- Resume mid-plan.
- Synthesis of five or more team plans with duplicates and conflicts.
- A run with no subagents (the inline fallback).
- **Progressive-disclosure check:** the files read match the load map, and no pack or library file is
  loaded when it isn't needed.

Checks combine **schema validation** of the files written with **rubric grading** of the
conversation.

### v1 acceptance criteria

- **Installation:** the plugin installs from this repo and the skill loads in Claude Code or Cowork,
  Codex or ChatGPT desktop, Cursor, and Copilot CLI or VS Code.
- **Size:** `SKILL.md` is 150 lines or fewer. Every reference file follows the §7.2 size rule.
- **Lead:** can produce a valid charter and team briefs in one session.
- **Delegate:** can produce a valid team plan and `opportunities.yaml` in one session of about 60–90
  minutes, and can resume.
- **Synthesis:** five or more team plans become a valid portfolio and roadmap.
- **Packs:** professional-services, assurance and tax meet the content targets in §11.4.
- **Evals:** the suite passes its agreed threshold. All §9 rules pass on every relevant scenario.

## 11. Content research program

The pack and backbone content is built by a **fan-out research effort** during the build phase, using
**only public sources**.

### 11.1 Process

1. **Briefs.** One research brief per pack module and per function card, in `research/briefs/`.
   Each brief gives the scope, the questions to answer, the schema to return, and the source rules.
2. **Fan-out.** One research subagent per brief. Each returns candidate use-case entries (§6.8),
   value-chain notes, metrics, guardrails and pain points, all with citations.
3. **Verify.** A separate verifier subagent checks each claim against its cited source, assigns the
   evidence grade, and rejects unsupported entries.
4. **Merge.** Remove duplicates across modules, map entries to patterns and archetypes, and run
   schema validation.
5. **Review** the merged content before it is committed. Source logs are kept in `research/sources/`.

### 11.2 Source rules

- Public sources only: regulator and standard-setter publications, professional-body reports, firms'
  public case studies and reports, vendor case studies (graded accordingly), academic work, and
  reputable press.
- Prefer 2025–2026. Record a date for every source.
- Summarize in our own words. No long quotations.
- No confidential, client-identifying or organization-internal material.

### 11.3 Evidence grades

| Grade | Meaning |
|---|---|
| **A** | A measured outcome from a named organization |
| **B** | A named real deployment, without published measurements |
| **C** | A vendor claim or analyst estimate |
| **D** | A plausible pattern with no public deployment found. Labelled "idea" |

### 11.4 Content targets (v1)

| Content | Target |
|---|---|
| Agentic patterns | 11 |
| Function cards | 10, each with 5–8 use cases |
| Pack modules | 8–15 use cases each (roughly 200–300 entries across the three packs) |
| Evidence mix | At least 50% grade A or B |

## 12. Answers to intent questions

| Intent question | Answer |
|---|---|
| Use-case library sourcing | Researched public content (§11) plus the organization's own overlay |
| Where outputs go | Markdown and YAML in the workspace (§8) |
| Program workspace location | Anywhere the organization stores information. GitHub repo template by default (§5) |
| Clients for v0 | Agent Plugins compatible. Verified in Claude Code / Cowork, Codex / ChatGPT desktop, Cursor, Copilot CLI / VS Code (§7.4) |
| First packs | professional-services, assurance, tax (§6.7). Content from public research, nothing organization-specific |
| Framework IDs (APQC) | Not used. Plain names and descriptions only |

## 13. Open questions and items to verify in `plan/`

1. **Install details not yet confirmed:**
   - how ChatGPT desktop installs plugins
   - whether Cursor falls back to `.claude-plugin`
   - which index path VS Code reads
   - whether Cowork accepts a root `plugin.json` next to `.claude-plugin/plugin.json`
2. **Delegation reliability.** Check that the explicit wording in §7.3 actually triggers subagents in
   each target client, especially Codex. Record the results in the eval report.
3. **Eval harness.** How we run the scenarios across clients in a repeatable way. For example, run the
   main harness in one client and do install smoke tests in the others.

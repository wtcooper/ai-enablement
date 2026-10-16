# Spec: AI transformation advisor (v1)

From: [`intent/2026-10-16-ai-transformation-advisor.md`](../intent/2026-10-16-ai-transformation-advisor.md) · Date: 2026-10-16 · Status: draft

> Stage 2 (Design) artifact. It says **what** v1 does and the rules it follows. The build order,
> the files that change, and how we prove it works belong in `plan/`. Background reasoning is in
> [`docs/brainstorm/`](../docs/brainstorm/).

---

## 1. Summary

A portable **Agent Plugin** that guides a *program lead* (a head of AI or business-unit leader) and
their *team delegates* through a top-down AI transformation of a business unit:

- The **lead** frames the ambition, splits the unit into pillars and teams, and writes a **charter**.
- Each **delegate** runs guided discovery for their team against that charter and produces a
  standard **team assessment**.
- The **lead** combines the assessments into a scored **portfolio** and a **roadmap** (a 100-day plan
  and a value creation plan).

The method uses the private-equity value-creation program structure for the lead and lean / Six
Sigma practice for team discovery. Users only ever hear plain language. A common **backbone**
provides the method and general knowledge. Optional **domain packs** add depth for specific kinds
of business. The organization's own content lives in an **overlay** inside its workspace, never in
the plugin.

## 2. Scope

**In v1**

- One plugin that conforms to Agent Plugins 1.0 and installs from a GitHub-hosted marketplace in any
  compatible client.
- Program lead flow, team delegate flow, and a light "explore" entry for inspiration.
- A file-based program workspace, with a GitHub repo as the reference setup.
- Backbone knowledge: the method, the ladder, work archetypes, agentic patterns, function cards,
  the value tree and scoring, and people and change.
- Domain packs: **professional-services**, **assurance** and **tax**, filled with researched public
  use cases (§11).
- Subagents for document analysis and portfolio synthesis in clients that support them, with an
  inline fallback everywhere else.
- An eval suite.

**Not in v1**

- Any backend, MCP server, telemetry or central library.
- Organization-specific content of any kind in the plugin repo.
- Deal-team or due-diligence mode.
- Individual-contributor mode as a separate flow. Delegates may involve their team members, but the
  delegate runs the session.
- Output to docs, slides or tickets. v1 writes markdown and YAML only.
- Building the automations that are recommended.

## 3. Users and entry

| Role | Goal | Main outputs |
|---|---|---|
| **Program lead** | Transform a business unit top-down | `charter.md`, `portfolio.md` / `portfolio.yaml`, `roadmap.md` |
| **Team delegate** | Find and make the case for AI opportunities in their team | `assessment.md`, `opportunities.yaml` |
| **Explorer** (anyone) | See what's possible before committing | No files required |

**Entry triage.** On activation, the orchestrator checks the working folder for a workspace:

- **No `charter.md` found:** ask whether the user is setting up a program (lead flow), working
  without a program (single-team discovery with default settings), or just exploring.
- **`charter.md` found:** ask which role the user has, or infer it from git identity or the folder.
  - A *delegate* is matched to their pillar and team in the charter.
  - If an assessment is already in progress, **resume** from its `status` and its last completed
    phase.

## 4. Experience flows

### 4.1 Conversation rules (all flows)

- Ask **one question at a time**. Play back what was heard before moving on.
- Use **plain language**. Method terms (value stream, DMAIC, value bridge) are never required of the
  user. They may appear in an output, explained in one line.
- **Adapt depth** to the user's answers. Skip what is already known. Go deeper where pain or value is
  high.
- **Show progress.** Name the current phase and what comes next.
- **Write as you go.** After each phase, save it to the workspace, so a session can stop and resume.
- **Pull examples in early.** Show relevant use cases and patterns from the start, not only at the end.
- **Be candid about people** (§9).

### 4.2 Program lead flow

| Phase | Purpose | Produces |
|---|---|---|
| **1. Ambition** | Why transform. What "good" looks like in 12–24 months. Constraints. **Business-model exposure**: where AI threatens or reshapes how the unit earns money | Charter: ambition and exposure sections |
| **2. Structure** | Split the unit into pillars and teams. Name a delegate for each team. Choose which packs apply | Charter: pillars, teams, packs |
| **3. Outside-in diagnostic** | For each pillar, estimate size, work-archetype mix, AI exposure, strategic weight and readiness. Choose **discovery waves**: which pillars go first | Charter: heatmap and waves |
| **4. Value tree and rules** | Choose and weight value levers. Adjust scoring weights. Set guardrails. Point to the overlay's tool catalog | Charter: value tree, scoring, guardrails |
| **5. Launch** | Generate a one-page **delegate brief** per team: what to prepare, how to run the plugin, and the deadline | `pillars/<p>/<t>/brief.md` |
| **6. Synthesize** | Combine the submitted assessments. Remove duplicates, find shared platforms and dependencies, roll value up the value tree, and sort into quick wins, foundations and big bets | `portfolio.md`, `portfolio.yaml` |
| **7. Roadmap** | A 100-day plan (quick wins, foundations, governance). A value creation plan (initiatives tied to levers, owners, KPIs, baselines, targets). A review cadence | `roadmap.md` |
| **8. Review** (repeat) | Update status against KPIs. Refresh priorities. Start the next wave | Updated portfolio and roadmap |

### 4.3 Team delegate flow

| Phase | Purpose | Produces |
|---|---|---|
| **0. Orient** | Read the charter. Confirm the team, scope and deadline. Explain how the session works and what happens to the output | — |
| **1. Frame** | The team's purpose, customers, outputs, pain points, and what success means for them | Assessment: frame |
| **2. Map** | Walk the main processes: trigger → steps → handoffs → output, with volumes, time, systems, decisions, and where rework happens. Optionally hand SOPs or exports to `artifact-analyst` | Assessment: process maps |
| **3. Diagnose** | Find waste, the bottleneck, and failure points. Tag each step with its work archetype | Assessment: diagnosis |
| **4. Imagine** | For each high-value step, show patterns and examples from the backbone, packs and overlay. Ask "what would an AI-native competitor do?" Place ideas on the ladder | Draft opportunities |
| **5. Prioritize** | Score each opportunity with the charter's rubric. Sort into quick win, foundation, big bet or park | `opportunities.yaml` |
| **6. Make the case** | For the top three to five: value as ranges with assumptions, prerequisites, risks and human checkpoints, and **role evolution** | Assessment: business cases |
| **7. Hand off** | A control plan (metrics, baselines, evals, checkpoints). Next steps and owners. Set the assessment status to `ready-for-review` | Assessment: control and next steps |

### 4.4 Explore (light)

Browse use cases and patterns by function, pack, work archetype or ladder level. Explain one example
in depth. Offer to start discovery or a program. This is what replaces the old "art of the possible"
mode.

## 5. Program workspace (file protocol)

### 5.1 Principles

- **Storage-agnostic.** The workspace is a plain folder of markdown and YAML. The plugin only reads
  and writes local files and never calls a storage API. Any synced location works: a git repo,
  SharePoint, OneDrive, Google Drive.
- **GitHub as the reference setup.** The repo provides a **workspace template** (`templates/workspace/`).
  The lead creates the program repo from it. Delegates clone it and commit to their team folder,
  ideally through a pull request. **The lead's merge is the acceptance**, the same pattern as the
  AI-native SDLC. Delegates who don't use git can return files any way they like, and the lead
  commits them.
- **Single-team mode.** With no charter, the plugin writes an assessment in the current folder using
  default settings. A lead can bring it into a program later.
- **Confidentiality.** Workspaces should be private. The plugin reminds users not to add
  client-confidential data or personal information beyond names and roles.

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
├── pillars/
│   └── <pillar-id>/<team-id>/
│       ├── brief.md
│       ├── assessment.md
│       ├── opportunities.yaml
│       └── evidence/
├── portfolio.md
├── portfolio.yaml
└── roadmap.md
```

### 5.3 Schemas (required fields; full JSON Schemas live in the plugin)

**`charter.md` frontmatter**

```yaml
schema: charter/v1
program: string
lead: { name, role }
version: int                       # bump on change; assessments record which version they used
status: draft | active | closed
horizon_months: int
ambition: string                   # one paragraph
pillars:
  - id, name, owner
    teams: [ { id, name, delegate, wave } ]
packs: [ professional-services, tax ]
value_levers:                      # chosen from the default value tree (§6.5), weights sum to 1
  - { id, name, metric, weight }
scoring_weights: { value, feasibility, data_readiness, risk, time_to_value, strategic_fit }
guardrails: [ string ]             # in addition to the plugin's fixed rules
overlay: overlay/                  # path, optional
```

**`opportunities.yaml` (one item per opportunity)**

```yaml
schema: opportunities/v1
program, pillar, team, charter_version
items:
  - id: string                     # <team-id>-NN
    title: string
    process: string                # process and step it changes
    work_archetypes: [ id ]
    pattern: id                    # from the pattern library
    ladder: assist | augment | automate | delegate | reinvent
    runtime_class: id              # §6.3
    description: string            # today → future, two or three sentences
    value:
      - { lever, low, high, unit, assumptions }
    scores: { value, feasibility, data_readiness, risk, time_to_value, strategic_fit }   # 1–5
    weighted_score: number
    category: quick-win | foundation | big-bet | park
    prerequisites: [ string ]
    risks: [ string ]
    human_checkpoints: [ string ]
    role_evolution: { tasks_moving, new_work, capacity_use }
    related_use_cases: [ id ]      # from library or overlay
    next_step: { action, owner, by }
```

**`assessment.md` frontmatter**: `schema: assessment/v1`, `program`, `pillar`, `team`,
`delegate`, `charter_version`, `status: in-progress | ready-for-review | accepted`,
`phase_completed: 0–7`, `updated`. The body has one section per phase.

**`portfolio.yaml`** combines the opportunity items and adds `portfolio_id`, `source_teams`,
`merged_from`, `shared_platform` and `dependencies`.

## 6. Knowledge model (backbone)

All backbone content is generic, public and written as plain names and descriptions. It cites no
external taxonomy IDs.

### 6.1 The ladder

| Level | Meaning | Example |
|---|---|---|
| **Assist** | AI helps a person with a task the person still owns | Drafting an email or memo with a chat assistant |
| **Augment** | AI is built into a step, gives a first pass, and a person reviews it. Shared prompts or skills make it consistent across the team | An AI first-pass review of contracts against a checklist |
| **Automate** | A defined step runs with no person on the normal path. Exceptions go to people | Extracting and validating data from documents straight into a system |
| **Delegate** | An agent owns a multi-step outcome across systems. It is started by events and runs in the background, with human checkpoints | An agent that prepares a full draft workpaper, gathering evidence from several systems |
| **Reinvent** | The process, service or business model is redesigned because AI makes a different way possible | Continuous monitoring instead of periodic review. Outcome-based pricing instead of hours |

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

### 6.3 Runtime classes (vendor-neutral; the overlay maps them to real products)

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

**Scoring:** six dimensions on a 1–5 scale. Each has anchored definitions in
`method/scoring.md`. The defaults are:

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

These are short cards for the support functions every business has: strategy & planning;
sales, marketing & business development; product & service development; service delivery &
operations; customer service; people (HR); technology (IT); finance & accounting; procurement &
supply chain; risk, compliance & legal.

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
├── PACK.md          # frontmatter: id, name, version, extends, modules, when_to_use
├── value-chain.md   # stages → processes, each tagged with work archetypes
├── modules/<m>.md   # processes, pain points, interview probes, top opportunities
├── use-cases.yaml   # §6.8 schema
├── metrics.md       # value levers and KPIs, with typical ranges and sources
├── guardrails.md    # standards, regulators, independence, data limits, steps needing human judgment
├── roles.md         # common roles and how they might evolve
└── disruption.md    # AI-native competitor scenarios
```

**Loading.** The orchestrator reads only the `PACK.md` frontmatter at the start. It loads modules and
use cases when the charter or the conversation calls for them.

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
  pack: id | null                  # null for backbone (function cards)
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
in the organization's own workspace (§5.2) and uses the same schemas.

| File | Effect |
|---|---|
| `tool-catalog.yaml` | Maps runtime classes to the organization's enabled products. Recommendations name these products. Anything outside the catalog is flagged as "not currently available" |
| `glossary.md` | Organization terminology |
| `guardrails.md` | Added to the plugin rules. Can never weaken §9 |
| `use-cases.yaml` | Internal examples, shown alongside public ones and labelled "internal" |
| `packs/<id>/` | Private packs. If an id matches a plugin pack, the private pack extends it |

**Order of precedence:** overlay > charter > packs > backbone. The rules in §9 cannot be overridden.

## 7. Plugin architecture

### 7.1 Repository and packaging

```
ai-enablement/                          # this repo = the GitHub marketplace
├── <per-client marketplace index files>  # one index per client that needs it (verify in plan)
├── plugins/ai-transformation-advisor/
│   ├── plugin.json                     # Agent Plugins 1.0 manifest
│   ├── skills/
│   │   ├── transformation-advisor/     # orchestrator and all shared knowledge (progressive disclosure)
│   │   │   ├── SKILL.md
│   │   │   ├── flows/                  # program-lead, team-discovery, synthesis-roadmap, explore
│   │   │   ├── method/                 # ladder, archetypes, runtime classes, value tree, scoring,
│   │   │   │                           # people-and-change, interviewing, diagnostic
│   │   │   ├── patterns/
│   │   │   ├── functions/
│   │   │   ├── packs/
│   │   │   ├── schemas/
│   │   │   └── templates/              # workspace files and deliverables
│   │   ├── analyze-artifacts/SKILL.md  # self-contained
│   │   └── synthesize-portfolio/SKILL.md
│   └── agents/                         # client-specific subagent wrappers (Claude Code first)
│       ├── artifact-analyst.md         # preloads analyze-artifacts
│       └── portfolio-synthesizer.md    # preloads synthesize-portfolio
├── templates/workspace/                # GitHub template for a program workspace
├── evals/
├── research/                           # research briefs and source logs behind the pack content
├── intent/ · spec/ · plan/ · docs/
```

**Why one large orchestrator skill:** shared knowledge lives inside a single skill folder. That
avoids depending on how each client resolves paths between skills or to the plugin root. The
smaller skills are self-contained and receive their inputs from the orchestrator.

### 7.2 Subagents and fallback

- **Rule:** every subagent is a thin wrapper that preloads one self-contained skill. If subagents
  aren't available, the orchestrator runs that skill inline with the same inputs and output contract.
- **Subagents never talk to the user.** All questions go through the orchestrator.

| Subagent | Input | Output |
|---|---|---|
| `artifact-analyst` | Paths to the delegate's evidence files | A draft process map in the assessment's map format, with each extracted fact marked as stated or inferred |
| `portfolio-synthesizer` | Paths to every `opportunities.yaml`, plus the charter | `portfolio.yaml` and a draft `portfolio.md` |

Large programs are processed in parallel by pillar.

## 8. Outputs

| Output | Who | Format |
|---|---|---|
| Charter | Lead | `charter.md` |
| Delegate brief | Lead → delegate | `brief.md` (one page) |
| Team assessment | Delegate | `assessment.md` and `opportunities.yaml` |
| Business case (one page per top opportunity) | Delegate | Section in the assessment |
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
7. The advisor designs and hands off. It does not claim to build or deploy anything.
8. When a user expresses fear about their role, acknowledge it honestly. Don't falsely reassure. Help
   the user position themselves as the person leading the change.

## 10. Quality and acceptance

### Evals

`evals/` holds 20–50 scenarios, each with a persona, a scripted user, the expected behaviors, and the
checks. The minimum coverage:

- Lead sets up a Big 4 tax-practice program.
- Delegate in an audit team, with and without uploaded SOPs.
- Anxious delegate.
- Skeptical lead who wants hard ROI.
- Request for cuts targeting named people.
- Team with no matching pack.
- Overlay present, and a recommendation outside the catalog.
- Resume mid-discovery.
- Synthesis of five or more assessments with duplicates and conflicts.
- A client without subagents (the inline fallback).

Checks combine **schema validation** of the files written with **rubric grading** of the
conversation.

### v1 acceptance criteria

- The plugin conforms to Agent Plugins 1.0 and installs from this repo's marketplace in Claude Code
  and at least two other compatible clients.
- A lead can produce a valid charter and delegate briefs in one session.
- A delegate can produce a valid assessment and `opportunities.yaml` in one session of about 60–90
  minutes, and can resume.
- Synthesis turns five or more assessments into a valid portfolio and roadmap.
- The professional-services, assurance and tax packs meet the content targets in §11.4.
- The eval suite passes its agreed threshold. All §9 rules pass on every relevant scenario.

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
5. **Human review** through a pull request. Logs are kept in `research/sources/`.

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
| Program workspace location | Storage-agnostic folder. GitHub repo as the reference setup (§5) |
| Clients for v0 | Any client compatible with Agent Plugins 1.0. Subagents where supported, with fallback (§7) |
| First packs | professional-services, assurance, tax (§6.7). Content from public research, nothing organization-specific |
| APQC licensing | Not used. Plain names and descriptions only |

## 13. Open questions

1. **Non-technical delegates.** Assurance and tax team leads may not use Codex, Cursor or Copilot. Is
   Claude (Cowork or desktop) or ChatGPT plugin support enough for them, or do we need a "send me
   your answers" path?
2. **Client differences** to verify in `plan/`: marketplace index files for each client, the Cursor
   marketplace limitation, and how each client resolves paths to reference files inside a skill.
3. **Subagent formats** for clients other than Claude Code (Copilot custom agents, Codex, Cursor).
   Add them in v1, or rely on the inline fallback?
4. **The lead's review step.** Should pull-request review be the recommended acceptance step, or just
   an option?

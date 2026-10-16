# Brainstorm: archetype packs, subagent architecture, and the PE value-creation frame

Date: 2026-10-16 · Status: working notes · Follows: [`2026-10-16-delivery-and-scope.md`](2026-10-16-delivery-and-scope.md)

> **Partly superseded.** The spec has since changed several things discussed here: there is now a single skill
> using progressive disclosure, subagents are described in tool-agnostic wording (no `agents/` folder), the
> product has no review step, and delegates produce a "team transformation plan". See
> [`spec/2026-10-16-ai-transformation-advisor.md`](../../spec/2026-10-16-ai-transformation-advisor.md).

Decisions from the owner in this round:

- **First audience:** a *program lead*, such as a head of AI or a business-unit leader asked to transform
  a business. They work **top-down**: they split the business into pillars and team functions, then
  hand discovery to delegates who map their own processes.
- **Delivery:** an Agent Plugin that runs entirely inside the user's AI client. **No shared backend in
  v1.** An orchestrator skill launches specialized subagents.
- **Specialization:** a common backbone plus **optional archetype packs** for different kinds of
  business.

---

## 1. Two roles, one shared program

The top-down shape means the plugin serves two roles that work on the **same program**:

| Role | Who | What they do with the plugin |
|---|---|---|
| **Program lead** | Head of AI, business-unit leader, transformation lead | Set the ambition and the *charter*. Define pillars and teams. Launch discovery. Combine the results into a portfolio. Build the roadmap and value creation plan. Run review cadences |
| **Team delegate** | Function or team lead (later, individual contributors) | Run guided discovery for their team against the charter. Produce a standard *team assessment* |

### Shared state without a backend: files

With no backend, **files are the shared state**. A program workspace is a folder the lead shares with
delegates (a git repo, SharePoint or OneDrive, a Cowork folder, anything synced):

```
transformation/
├── charter.md                  # lead: ambition, pillars, value tree, scoring weights, guardrails, tool catalog, timeline
├── pillars/
│   └── <pillar>/<team>/
│       ├── assessment.md       # delegate: process map, diagnosis, opportunities (fixed frontmatter schema)
│       └── evidence/           # optional SOPs, exports, volumes the delegate added
├── portfolio.md                # lead: combined, scored, de-duplicated opportunities
└── roadmap.md                  # lead: 100-day plan and value creation plan, owners, KPIs, cadence
```

The charter is what makes a top-down program consistent. Every delegate session reads it, so all teams
are scored on the same value tree and weights, use the same pillars and terms, and work within the
same guardrails and tool catalog. A schema for `assessment.md` lets the lead's synthesis step combine
twenty teams mechanically. This is a PE-style program office (PMO) run through files. A backend (MCP)
can replace the folder later without changing the method.

## 2. Orchestrator and subagents

### What the research says

- **Agent Plugins 1.0 standardizes only skills and MCP servers.** The spec lists agents, commands and
  hooks as "too client-specific" for v1. Subagents are therefore **not portable**. Claude Code loads
  them from a plugin's `agents/` folder, and other clients ignore that folder.
  ([spec 1.0.0](https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md))
- **Subagents cannot ask the user questions.** In Claude Code, `AskUserQuestion` is removed from every
  subagent. They start with a blank context and return only a final report.
  ([Claude Code subagents docs](https://code.claude.com/docs/en/sub-agents))
- **When to use the main conversation:** frequent back-and-forth, context shared across phases,
  latency-sensitive steps.
- **When to use subagents:** verbose input or output you don't want in the main context,
  self-contained work that returns a summary, enforced tool limits, and work that can run in parallel.
- A subagent can **preload skills** (`skills:` frontmatter), so an agent can be a thin wrapper around
  a portable skill.
- Multi-agent setups use many times more tokens. Use them where context isolation or parallel work
  pays for itself, not by default.

### Design consequences

1. **The interview stays in the orchestrator.** Discovery is a conversation, and subagents can't hold
   one. The orchestrator skill owns the dialogue, the phase flow and the program files.
2. **The portable unit is the skill. Agents are a Claude Code enhancement layer.** Each subagent
   preloads a skill that holds its real instructions. In a client without subagents, the orchestrator
   runs the same skill inline. Same behavior, just less context isolation.
3. **Subagents do bounded work.** Analyze documents, find analogues, score independently, red-team,
   and fan out over many team files.

### Proposed subagents

| Subagent | Job | Why it is a subagent |
|---|---|---|
| `artifact-analyst` | Read SOPs, process documents, org charts, ticket or time exports. Return a draft process map with steps, roles, volumes and systems | Verbose input, short structured output |
| `use-case-scout` | For a mapped step or work archetype, search the pattern library and packs for analogues, and the web if allowed. Return a shortlist with evidence | Breadth search. Keeps noise out of the interview |
| `opportunity-assessor` | Score candidates against the charter's rubric. Place each on the ladder (assist → augment → automate → delegate → reinvent) | Independent scoring is less swayed by the user's favorite ideas |
| `risk-and-people-reviewer` | Red-team each opportunity for regulatory and data risk, missing human checkpoints, and the role-evolution story | A separate critic catches what the advocate misses |
| `portfolio-synthesizer` | Lead only. Fan out over every `assessment.md` (parallel by pillar). Remove duplicates, find shared platforms, roll value up into the value tree | Parallel and verbose. A natural fan-out |

Start with **two of these: `artifact-analyst` and `portfolio-synthesizer`.** Their value is clearest.
Add the others when evals show the orchestrator scoring generously or missing risks.

### Proposed plugin layout

```
ai-transformation-advisor/
├── plugin.json                      # Agent Plugins 1.0 manifest (portable)
├── .claude-plugin/plugin.json       # Claude Code manifest, if still needed alongside
├── skills/
│   ├── transformation-advisor/      # orchestrator: role triage, phase flow, program file I/O
│   │   ├── SKILL.md
│   │   └── references/              # method, value tree, ladder, interview guides, schemas
│   ├── program-charter/             # lead: top-down framing and charter
│   ├── team-discovery/              # delegate: map → diagnose → imagine → prioritize
│   ├── portfolio-and-roadmap/       # lead: synthesis, value creation plan, 100-day plan
│   ├── analyze-artifacts/           # preloaded by artifact-analyst
│   └── synthesize-portfolio/        # preloaded by portfolio-synthesizer
├── agents/                          # Claude Code only; ignored elsewhere
│   ├── artifact-analyst.md
│   └── portfolio-synthesizer.md
└── packs/                           # backbone function cards + optional archetype packs (§3)
```

## 3. Archetype packs

### Are there industry standards to use?

| Taxonomy | Level of detail | Fit as a pack boundary |
|---|---|---|
| **GICS / NAICS** (industry classification) | 11 sectors → 25 industry groups → 74 industries → 163 sub-industries | Good for *labels*. Bad for *packs*: audit and tax both fall under "professional services" |
| **APQC Process Classification Framework (PCF)** | Cross-industry, 13 level-1 categories down to activities, plus industry versions (banking, utilities, consumer products, petroleum, insurance, healthcare and others) | **Best backbone for functions.** Gives process IDs and vocabulary. No professional-services version: that work sits under "5.0 Deliver Services" |
| **Domain reference models** (SCOR supply chain, BIAN banking, TM Forum eTOM telecom, ACORD insurance, ITIL IT services) | Deep, one domain each | Good *sources* for a pack's value chain, not boundaries in themselves |
| **O\*NET** (occupations → tasks) | About 1,000 occupations and their task statements | Good for *task-level* breakdown and AI-exposure prompts inside discovery |
| **Professional standards** (ISA and PCAOB audit standards, ISQM 1, ASC 740, OECD Pillar Two) | The regulated workflow of a service line | Defines a regulated pack's process map and its guardrails |

None of these alone gives the right cut. Industry codes are too coarse and process frameworks are
too generic. **I recommend defining a pack by its value chain and borrowing the taxonomies for IDs and
vocabulary.**

### Recommended level of detail: a pack is a distinct value chain

A pack earns its place when it changes **at least three** of these four things compared with the
backbone and other packs:

1. **Core value chain:** the end-to-end flow of the work that creates the product (not support
   functions).
2. **Use-case library:** the top AI opportunities are different.
3. **Guardrails:** different regulators, professional standards or data obligations.
4. **Value metrics:** the business measures value differently (realization and utilization versus
   inventory turns versus combined ratio).

If a candidate changes only one or two of these, it is a **module** inside a pack. If it changes only
the vocabulary, it is a **glossary entry in the organization overlay**. In practice this puts packs at
about the level of a **service line or industry group**, with modules at the sub-service level.

### Three layers, plus work archetypes in the backbone

```
Backbone (always installed)
├── Method: charter → discovery → diagnose → imagine → prioritize → case → roadmap
├── Work archetypes (how work is done, which drives which AI pattern fits)
│     review & assurance · high-volume transaction processing · expert judgment & advice ·
│     research & synthesis · content & document production · customer-facing service ·
│     coordination & scheduling · software & data engineering · physical & field operations
├── Agentic pattern library, keyed to work archetypes
└── Function cards (APQC level-1 categories, light): strategy, sales & marketing, service delivery,
      customer service, HR, IT, finance, procurement & supply chain, risk & compliance, legal

Domain packs (optional; one value chain each; may extend another pack)
└── e.g. professional-services ← assurance, tax

Organization overlay (configuration, never committed upstream)
└── tool catalog, terminology, pillars, governance, intake destination
```

**Work archetypes** are probably the most useful idea here. They let the backbone suggest the right
agentic patterns for *any* team, before any pack is installed. Audit work is mostly *review &
assurance* plus *transaction processing*. Tax compliance is *transaction processing* plus *document
production*. Tax advisory is *expert judgment* plus *research & synthesis*. Packs then add domain
depth on top.

### Worked example: a Big 4 firm

| Pack | Extends | Modules | What makes it a pack |
|---|---|---|---|
| **professional-services** | (backbone) | Pursuit and proposal, acceptance and risk, scoping and pricing, staffing and resourcing, delivery management, quality review, billing and collections, knowledge management | Engagement-based value chain. Utilization, realization and margin metrics. Business-model risk to billable hours |
| **assurance** | professional-services | Acceptance and independence, planning and risk assessment, controls testing (SOX and ICFR), substantive testing, specialists (IT audit, valuation), completion and reporting, quality management (ISQM 1), other assurance (SOC, sustainability) | Standards-driven workflow. Independence and skepticism guardrails. Full-population testing changes the method itself |
| **tax** | professional-services | Compliance (corporate, partnership, individual), provision (ASC 740 and IAS 12), indirect tax, transfer pricing, international and Pillar Two, controversy, research and advisory, tax data and technology | Deadline-driven, data-heavy flow. Distinct regulators. Strong reinvention potential (compliance shifting from hours to outcomes) |
| *consulting* | — | **Not a pack.** Uses professional-services plus the **client's** industry pack and function cards | Its value chain *is* the professional-services chain. Its domain content is the client's |

These packs **also serve corporate in-house teams**. A corporate tax department uses the tax pack, and
internal audit uses most of the assurance pack. That makes them reusable well beyond Big 4.

**Possible later packs**, using the same test: financial services (banking, insurance, asset and
wealth management as modules), healthcare provider and payer, life sciences, manufacturing and
industrial, retail and consumer goods, software and technology, public sector, energy and utilities.

### Pack anatomy (all markdown and YAML; read only when needed)

```
packs/<id>/
├── PACK.md          # frontmatter: id, version, extends, taxonomy refs (APQC, NAICS), modules, when to load
├── value-chain.md   # level 1–3 process map, each step tagged with a work archetype and APQC ID where one exists
├── modules/<m>.md   # per sub-domain: processes, common pain points, interview probes, top opportunities
├── use-cases.yaml   # problem → pattern → ladder level → value → prerequisites → risks → evidence and source
├── metrics.md       # value levers and KPIs, with typical ranges and sources
├── guardrails.md    # standards, regulators, independence, data limits, steps that require human judgment
├── roles.md         # common roles and how each could evolve
└── disruption.md    # "what would an AI-native competitor do here?" scenarios
```

**Packaging:** Agent Plugins 1.0 has **no dependency mechanism**, so a pack can't declare that it
needs the core plugin. Recommendation: **one monorepo, with packs as folders inside a single plugin**.
The orchestrator reads `PACK.md` files and loads modules on demand, so packs that aren't in use cost
almost nothing in context. If packs grow large or need restricted distribution, a build script can
produce bundles (core alone, or core with selected packs) as separate plugins from the same source.

## 4. The PE frame, and how it relates to lean and Six Sigma

### The three disciplines in plain terms

| | **Lean** | **Six Sigma** | **PE value creation** |
|---|---|---|---|
| Origin | Toyota | Motorola, then GE | Private equity operating partners and consultancies |
| Core question | Where is the waste, and how does work *flow*? | Where is the *variation and defects*, and what causes them? | *Where is the value*, what is it worth, and how fast can we capture it? |
| Altitude | Process and team (bottom-up) | Process (bottom-up, data-heavy) | Whole business (top-down, financially anchored) |
| Signature tools | Value stream map, 8 wastes, flow and pull, kaizen, "go and see" | DMAIC (Define, Measure, Analyze, Improve, Control), baselines, root cause, control plans | Investment thesis, diagnostic, value bridge, value creation plan, 100-day plan, PMO with KPI cadence, exit story |
| Time frame | Continuous | Project by project | Fixed hold period (3–7 years). Front-loaded first 100 days |

They are layers, not rivals. **PE decides where to look and what it's worth. Lean and Six Sigma are
the tools operating partners use inside a business to fix the processes the plan targets.** All three
share *baseline → prioritize → improve → control*.

### Recommendation

The persona you described, a head of AI arriving to transform a business top-down, is almost exactly
a **PE operating partner arriving at a newly acquired company**. So:

1. **Use the PE program structure as the program-lead layer.**
   - *Thesis / ambition:* why transform and what "good" looks like. This includes **business-model
     exposure**: where AI threatens or reshapes how the unit earns money, for example billable hours.
   - *Outside-in diagnostic* across pillars, to choose where to send delegates first.
   - *Value tree:* the unit's equivalent of an EBITDA bridge. For a Big 4 unit that means
     capacity, margin, realization, cycle time, quality and growth.
   - *Value creation plan and 100-day plan:* quick wins, foundations (data, tools, governance), and
     larger structural bets.
   - *Program office cadence:* track initiatives against KPIs and roll results back into the charter.
2. **Use lean and Six Sigma as the method inside team discovery.** Map the value stream, find waste and
   the bottleneck, set a baseline, and finish with a *control* plan (metrics, evals, human
   checkpoints). The user never needs to learn the vocabulary.
3. **The value tree joins the two layers.** Every team opportunity rolls up to a lever in the charter.
   That gives the lead a sized portfolio instead of a list of ideas.
4. **Defer a deal-team mode** (AI due diligence on an acquisition target, or AI-adjusted investment
   theses). It's a different user and a different job. It could become a later "deals" pack once the
   program-lead flow works.
5. **Be honest about cost-out.** PE programs are open about cost reduction. The advisor should be
   too, at the level of capacity and roles. It should always show the choice between redeploying
   capacity (growth, quality, backlog, new services) and reducing cost. It never sets targets for
   named people.

## 5. Generic or organization-specific (previous open question)

**Recommendation:** an open, generic core (backbone, method, patterns and packs) with a **private
organization overlay** for the tool catalog, terminology, pillars and governance. Use it inside your
firm first with the professional-services, assurance and tax packs. Firm-specific content (internal
tool names, policies, real use cases) stays in the overlay or a private fork, never in a public repo.

## 6. New open questions

1. **Program workspace:** where will leads and delegates actually share files? This decides how the
   charter and assessment protocol is described.
2. **Clients for v0:** Claude Code and Cowork with subagents, plus one or more clients without
   subagents (ChatGPT, Copilot, Cursor) to prove the fallback works?
3. **APQC licensing:** the cross-industry PCF requires attribution, and some industry versions have
   their own terms. Should we reference IDs and short names only, rather than copying the frameworks?
4. **Seed content:** who can supply real (sanitized) assurance and tax use cases and pain points to
   check the first packs?

## Sources

- [Agent Plugins spec 1.0.0](https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md)
- [Agent plugins in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-plugins)
- [Claude Code: create custom subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Agent SDK subagents](https://docs.anthropic.com/en/docs/claude-code/sdk/subagents)
- [APQC industry-specific PCFs](https://www.apqc.org/process-frameworks/industry-specific-process-frameworks)
- [APQC cross-industry and industry PCF collection](https://www.apqc.org/node/245395)

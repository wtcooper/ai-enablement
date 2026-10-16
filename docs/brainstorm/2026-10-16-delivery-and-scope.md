# Brainstorm: delivery mechanism and scope

Date: 2026-10-16 · Status: working notes · Feeds: [`intent/2026-10-16-ai-transformation-advisor.md`](../../intent/2026-10-16-ai-transformation-advisor.md)

These are notes for the move from intent to spec. Nothing here is decided yet.

---

## 1. The landscape as of October 2026

- **Agent Plugins 1.0** (August 2026) is a vendor-neutral package format. A plugin is a folder with a
  `plugin.json` manifest, `skills/<name>/SKILL.md` and optional MCP server configuration. Its
  maintainers come from OpenAI, Microsoft/GitHub, Cursor, Amazon, Vercel and (reportedly) Google.
  Clients include ChatGPT, Codex, Cursor, Copilot, VS Code and Kiro. Claude Code loads plugins of the
  same shape through its own marketplaces. The spec deliberately leaves out installation, permissions
  and marketplaces, so each client does those differently.
- **Agent Skills** is the separate open standard for `SKILL.md` (frontmatter plus instructions plus
  reference files). Skills are the portable unit. A plugin is the wrapper that bundles them.
- **Managed agent runtimes** (for example Claude Managed Agents, and hosted agents on the other
  platforms) let an organization run long-lived agents with tools, sandboxes and state behind a
  web app, Slack or Teams. This is the "hosted agentic workflow" category users struggle to picture.
- **The gap the intent names is real.** Coding and chat tools have trained people to think "my
  assistant". The value now moving into the business core (pricing, sales ops, finance, service,
  supply chain) needs people to think "our workflow, redesigned around agents".

## 2. Delivery options

| # | Option | Who it reaches | Strengths | Weaknesses |
|---|---|---|---|---|
| A | **Agent Plugin** (skills + optional MCP) in a marketplace | Users already in Claude, Cursor, Codex, Copilot or ChatGPT | Cheap to build. Portable. Versioned in git. Meets users where they work. Fits the open standard | Skews technical. Ephemeral: no shared memory between sessions. Client behavior varies. Weak for multi-person team engagements |
| B | **MCP server** (library, tool catalog, intake, benchmarks) | Any MCP client, including plugin users | Central, updatable "brain". Makes the data flywheel possible. Intake goes straight to a backlog | Needs hosting, authentication and privacy controls. Has to be run as a service |
| C | **Hosted advisor** (managed agent runtime behind web, Slack or Teams) | Leaders, non-technical staff, deal and transformation teams | No setup for users. Can hold state across multi-session, multi-person engagements. Can produce polished deliverables | The most build and operations work. Platform choice is a commitment |
| D | **Chat-native packaging** (Claude Project, custom GPT, Copilot agent) | Broad enterprise chat users | Fastest to ship. Familiar | Copied content drifts across platforms. Limited tools. No flywheel |
| E | **Facilitator kit** (agent as co-pilot to a human transformation lead running workshops) | Transformation or enablement teams | Uses human facilitation where it matters most: trust, politics, fear | Doesn't scale without facilitators. Needs Option A or C underneath |
| F | **Use-case gallery** (browsable, shared web page or dashboard) | Everyone, especially "show me what's possible" users | Directly addresses the inspiration gap. Can be shared | It is a view onto the library, not an advisor on its own |

### Recommendation: one brain, many front doors

The plugin is a **wrapper**. The lasting asset is the **content**: the methodology, the interview flows,
the scoring rubrics and the use-case library. So:

1. **Build the content as code, independent of any runtime.** Skills plus reference markdown and a
   structured use-case library (YAML or JSON) in this repo. Everything else packages it.
2. **First front door: an Agent Plugin (Option A).** It is the cheapest way to test whether the
   method and content work. It reaches the "already in AI tools" group named in the intent, and it
   follows the standard the user already identified. Publish it to a Claude Code marketplace and to
   standard-compatible clients from the same source.
3. **Second step: an MCP server (Option B)**, bundled into the same plugin. Add it when we need a
   shared library, an organization tool catalog or direct intake. This is what turns a smart prompt
   into a system that learns.
4. **Third step: a hosted advisor (Option C) plus a gallery (Option F)**, aimed at leaders and team
   engagements, reusing the same skills on a managed runtime. The facilitator kit (Option E) is a
   *mode* of the advisor, not a separate product.

The plugin is the right *first* step. On its own it is probably not enough for the leadership and
organization zoom level, which is where the reinvention-level ideas sit.

## 3. How it might work

### 3.1 Entry: meet users where they are

A short triage (two or three questions) sets two dials:

- **Zoom:** individual · team · organization
- **Experience:** explorer (show me what's possible) · practitioner (redesign my work) · leader
  (build the case)

### 3.2 Core flow (lean, DMAIC and value creation, in plain language)

| Phase | What the advisor does | Borrowed from |
|---|---|---|
| **Frame** | Goals, pain points, what success looks like, constraints, the user's role in the change | DMAIC Define, investment thesis |
| **Map** | Walk the current process: SIPOC, steps, handoffs, volumes, cycle times, systems, decisions | Value stream mapping, gemba |
| **Diagnose** | Find waste (DOWNTIME), the bottleneck, rework and failure points. Break work into tasks and judge how exposed each is to AI | Lean wastes, theory of constraints, task decomposition |
| **Imagine** | Show patterns and peer examples from the library. Ask "what would an AI-native competitor do?" Place ideas on the ladder: assist → augment → automate → delegate to agents → reinvent | Inspiration library, zero-based redesign |
| **Prioritize** | Score value, feasibility, data readiness, risk and time to value. Separate quick wins from structural bets | PE value lever sizing, impact/effort matrix |
| **Make the case** | Directional value with assumptions (hours released, cycle time, quality, revenue). A role-evolution view. Risks and controls | EBITDA bridge, business case |
| **Plan and hand off** | 30/60/90 or 100-day plan. Owners. The *control* plan (metrics, evals, human checkpoints). Structured intake submission | 100-day plan, DMAIC Control, PMO |

### 3.3 Knowledge modules (skills and reference files)

- **Transformation methods:** lean, Six Sigma (DMAIC), theory of constraints, jobs-to-be-done, change
  management (ADKAR and Kotter, kept light).
- **Value-creation playbook:** outside-in diagnostic, value levers (revenue, margin, capital,
  multiple), spans and layers, cost-to-serve, benchmarking functional cost as a percentage of
  revenue, 100-day plan, value creation plan tracking, a playbook reused across the portfolio, and AI
  as part of the exit story.
- **Agentic pattern library:** reusable *shapes* such as event-triggered triage, document-to-decision,
  research and synthesis, monitor → diagnose → act, reconciliation, customer-facing agent with
  escalation, and code or content migration. Each comes with when to use it, a maturity level, the
  human checkpoints it needs, and which runtime class fits (personal assistant, scheduled or
  background agent, managed runtime).
- **Use-case library:** examples by function and industry, with problem → pattern → outcome →
  lessons learned. Sources: curated public cases, internal cases, and opt-in anonymized sessions.
- **Organization catalog (overlay):** enabled tools and platforms, approved data sources, governance
  rules, intake destination. Loaded from config so each organization can customize it.
- **People and change:** a role-evolution template, the "proposer as leader" framing, and capacity
  redeployment options (growth, quality, backlog, new services) versus cost reduction.

### 3.4 Candidate skills (if it starts as a plugin)

- `transformation-advisor`: the orchestrator. Triage, then route to the flow.
- `art-of-the-possible`: inspiration by role, function and industry from the library.
- `process-discovery`: interview and mapping (SIPOC, value stream, task breakdown).
- `opportunity-assessment`: diagnosis, ladder placement, scoring.
- `business-case`: value sizing with assumptions, plus role evolution.
- `transformation-roadmap`: a 100-day or value-creation-plan view for team and organization zoom.
- `submit-use-case`: structured intake (markdown, issue or ticket through MCP).

That could start as **one skill with reference files** and split up only when the evals show routing or
context problems.

## 4. Out of scope (initial view)

- Building the automations themselves. The advisor designs and hands off; build teams or agents build.
- Detailed financial models, deal valuation or legal and HR advice on workforce actions.
- Assessing named individuals' performance, or targeting specific people.
- Vendor selection outside the organization's catalog. The advisor can say a capability is missing.
- Real-time process mining or system integration in v1.

## 5. Risks

- **Generic advice.** Without a strong library and an organization catalog the output looks like any
  chat answer. *Mitigation:* the library and catalog are first-class, and the evals check for specifics.
- **Methodology overload.** Lean and value-creation vocabulary scares people off. *Mitigation:* use the
  methods under the hood and plain language in the conversation.
- **Fear backfire.** Handling the workforce topic badly loses trust. *Mitigation:* an explicit,
  tested people-and-change behavior, and eval scenarios for anxious users.
- **Client fragmentation.** Plugins behave differently in each client. *Mitigation:* keep skills
  simple and self-contained, and test in the top two or three clients.

## 6. Next steps

1. Answer the open questions in the intent, especially audience, backend and PE depth.
2. Collect five to ten real interview transcripts or use cases (sanitized) to seed the library and evals.
3. Draft `spec/` (behaviors, modes, output formats, knowledge modules) from the accepted intent.
4. Draft `plan/` for the v0 plugin build.

## Sources

- [The AI-native SDLC playbook (Anthropic)](https://claude.com/blog/the-ai-native-sdlc-playbook)
- [Agent Plugins spec repository](https://github.com/agentplugins/agent-plugins-spec)
- [Agent Plugins announcement (Google Developers Blog)](https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/)
- [Deploying AI across PE portfolio companies (WorkWise)](https://workwisesolutions.org/guides/deploying-ai-pe-portfolio-companies-playbook.html)
- [How AI is reshaping the PE operating model (Brightwave)](https://www.brightwave.io/blog/how-ai-is-reshaping-the-private-equity-operating-model)

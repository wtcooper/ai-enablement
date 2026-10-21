# AI Transformation

A set of AI skills for the people who lead AI change in a business: team leads, practice leaders,
heads of AI, and knowledge, learning and operations leaders. They go beyond personal productivity to
redesigned workflows, AI agents and new ways of working, and then help run the program that follows.

The plugin runs inside the AI tool you already use: Claude, ChatGPT / Codex, Cursor or GitHub Copilot.
Each skill interviews you the way an experienced practitioner would, draws on deep, researched knowledge
of your field, and writes plain files you can act on and share.

> **Status: in development (pre-release).** The method, five business archetypes and five skills are built.
> The plugin installs and runs in Claude Code; the other tools are still being checked. See [Status](#status).

## Why

- Most people use AI for **personal tasks**, like drafting or summarizing. Few know how to redesign a
  **team's or a firm's** work around it.
- Good ideas need a **method**: where to look, how to size value, what to do first. They also need
  **real examples from your own field**, not generic ones.
- People worry that AI will replace them. The advisor is **honest** about how roles change, and it
  helps the person proposing the change lead it.

## The skills

| Skill | Use it when you want to | It writes |
|---|---|---|
| **transformation-advisor** | Find where AI could change your team's, practice's or firm's work and plan it; assess an acquired firm's AI maturity | `transformation-plan.md`, `opportunities.yaml`, unit briefs |
| **ai-portfolio** | Log, screen and score AI ideas; decide whether to stop, redirect or scale a pilot; run portfolio reviews; track benefits; roll capabilities into an acquired firm | `portfolio/` |
| **ai-solution-delivery** | Take one opportunity to production: frame the problem, build or buy, design brief, evaluation plan, readiness check, post-launch review | `solutions/<id>/` |
| **ai-enablement** | Raise fluency and sustained use: segment users, role-based curriculum, champions and office hours, a workflow library, adoption measures, bringing partners along | `enablement/` |
| **ai-governance** | Set practical governance: acceptable use, client-data rules, risk tiers and human review, records of AI use, professional duties, vendor evaluation, an approved-tool catalog | `overlay/` |

The skills share one knowledge base and hand work to each other through files. Opportunities from a
transformation plan enter the portfolio; a portfolio item ready to build opens a solution folder; launched
solutions add benefits and reusable workflows; and the governance files constrain every skill.

## How the advisor works

![How the advisor works](docs/images/advisor-flow.svg)

1. **It gets to know you.** It asks about your role, what kind of business you're in, how far along
   you are with AI, and what you need from the session. Then it adapts. Someone new to AI starts
   with real examples from their field. A seasoned leader goes straight to redesign and the business
   case.
2. **It walks you through one loop**, asking one question at a time. Frame the goal, map the real
   work, find where value leaks, then reimagine it through four lenses:
   - **improve** the step
   - **automate** the flow
   - **delegate** the outcome to an AI agent
   - **reinvent** the work
3. **It works at any level.** For a team, the loop looks at specific processes. For a practice or a
   firm, it splits the work into units (such as service lines). Each unit runs the same loop, and
   the advisor rolls the results up into one roadmap.
4. **It writes things down.** Your plan is saved as you go, so you can stop, share and pick it up
   later.

More detail: [How the advisor works](docs/how-it-works.md).

## What's inside

![What's inside](docs/images/whats-inside.svg)

- **Method:** how an expert runs a transformation. It draws on lean and Six Sigma,
  private-equity value-creation practice, and current evidence on what makes AI efforts succeed.
- **Business archetypes:** deep knowledge of a field. That includes how the work is done, where AI
  is really being used (with sourced, graded examples), the regulations, workforce effects and
  where the field is heading.
- **Your organization (optional):** your approved tools, terminology and internal examples. These
  stay in your own folder and never go into the plugin.

| Archetype | Status |
|---|---|
| **Assurance**: audit, SOC and attestation, sustainability assurance, assurance over AI, and the mid-market: private-company audits, employee benefit plan audits, nonprofit and government (single audit) | Ready: 13 focus areas, 265 sourced examples, all fact-checked |
| **Tax**: individual and corporate compliance, provision and Pillar Two, indirect tax, transfer pricing, controversy, research and advisory, tax data and technology, and multistate tax for private companies | Ready: 9 focus areas, 206 sourced examples, all fact-checked. Public evidence is thinner than in audit, and the advisor says so |
| **Advisory**: the advisory and outsourced side of accounting firms serving private and middle-market companies: client accounting services, risk and controls, transactions, valuation, forensic and disputes, FP&A, private client | Ready: 7 focus areas, 124 sourced examples, all fact-checked. Strongest in client accounting services and risk; thin in valuation and FP&A |
| **Security**: governance and risk, security operations, threat intelligence, incident response, vulnerability and exposure, application security, cloud, identity, data security and privacy, human risk, AI security | Ready: 11 focus areas, 245 sourced examples, all fact-checked |
| **Professional services**: the base for law, consulting, accounting and advisory firms and in-house legal teams: pursuit and proposals, client development, acceptance and risk, scoping and pricing, staffing, delivery, work production, quality review, billing, knowledge management, talent and learning, firm finance | Ready: 12 focus areas, 240 sourced examples, all fact-checked. Few firms publish measured results, and the advisor says so |
| Other fields | The advisor uses its general method, and can optionally research a field on the spot |

## Getting started

### 1. Install

The plugin installs from this repository's marketplace. Pick your tool. Installation is confirmed in Claude
Code; the other tools are being checked ([checklist](docs/install-testing.md)).

| Tool | Install |
|---|---|
| Claude Code or Claude desktop (Cowork) | `/plugin marketplace add wtcooper/ai-enablement`, then install **ai-transformation**. In Cowork, use Customize > Plugins |
| Codex CLI / app or ChatGPT desktop | `codex plugin marketplace add wtcooper/ai-enablement`, then `codex plugin add ai-transformation@ai-enablement` |
| Cursor | `agent plugin marketplace add https://github.com/wtcooper/ai-enablement`, then install from `/plugins` |
| GitHub Copilot CLI | `copilot plugin marketplace add wtcooper/ai-enablement`, then `copilot plugin install ai-transformation@ai-enablement` |
| VS Code with Copilot | Add `wtcooper/ai-enablement` to the `chat.plugins.marketplaces` setting |

### 2. Start in a folder for your work

Open your AI tool in an empty folder, or in a shared folder or repo your team uses. The skills save
their files there, so the advisor's plan, the portfolio and the policy sit side by side. A [starter folder](templates/workspace/) is available if you want one, with examples of
the optional organization content.

### 3. Ask for help in your own words

> *"Help me figure out how AI could transform my audit practice."*
>
> *"I lead a tax compliance team. Where should we use AI?"*
>
> *"I'm new to AI. Show me what teams like mine are doing."*
>
> *"We have 30 AI ideas and no way to compare them or stop the weak pilots."* (ai-portfolio)
>
> *"We want to build a tool that drafts responses to tax notices. Build or buy, and how do we test it?"*
> (ai-solution-delivery)
>
> *"Adoption is uneven and the partners ignore the assistant."* (ai-enablement)
>
> *"IT says no. Can our staff use AI on client returns?"* (ai-governance)

The right skill takes it from there. A first session usually takes 60–90 minutes. Ask it to pause at
any time, and it picks up where you left off next time.

### Tips

- **Don't paste client-confidential or personal data.** Describe the work instead.
- **Share the plan.** It's plain text, so you can commit it to a repo or copy it to a shared drive.
  For a firm-wide effort, give each unit leader their brief and collect their plans.
- **Add your organization's context** (optional) in an `overlay/` folder next to your plan. It can
  hold your tool list, terms and internal examples. See
  [How the advisor works](docs/how-it-works.md#your-organizations-content).

## Status

| Done | Next |
|---|---|
| Method: 11 step-by-step guides, plus guides for leading partners and for acquisitions, fact-checked | Confirm installation in Codex, Cursor and Copilot |
| Five archetypes, fact-checked: professional services (12 focus areas), assurance (13), tax (9), advisory (7) and security (11) | Test runs with real practice leaders, and an eval suite |
| Five skills (advisor, portfolio, solution delivery, enablement, governance): install, trigger and hand off in Claude Code | |
| Shared library: 11 pattern guides, 10 function cards and journey stages, fact-checked | |
| Research program and quality checks | |

## Learn more

- [How the advisor works](docs/how-it-works.md): onboarding, the loop, outputs, evidence grades and
  ground rules
- [How this project is built](docs/development.md): design documents, the research program and
  repo layout

## License

[MIT](LICENSE)

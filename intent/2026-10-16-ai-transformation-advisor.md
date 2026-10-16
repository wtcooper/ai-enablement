# Intent: AI transformation advisor

Author: Wade Cooper · Drafted with Claude · Date: 2026-10-16 · Status: draft

> Stage 1 (Plan) artifact in the [AI-native SDLC](https://claude.com/blog/the-ai-native-sdlc-playbook)
> chain: `intent` → `spec` → `plan`. This file says what we want, why, and under
> which constraints. It says nothing yet about how it is built. The open delivery
> and scope options live in
> [`docs/brainstorm/2026-10-16-delivery-and-scope.md`](../docs/brainstorm/2026-10-16-delivery-and-scope.md).

## Problem

AI tools are now everywhere. People use Claude, ChatGPT, Cursor, Codex and Copilot every day, but almost
all of that use is **personal productivity**. One person drafts, summarizes or codes faster. Very few
individuals, teams or leaders can see the next step: redesigning **how a team or business works** with
hosted agentic workflows and managed agent runtimes. In that world agents run in the background, start on
events, cross systems and hand off to humans at checkpoints. The step is from "AI helps me do my tasks"
to "the work is designed around agents".

Four things get in the way:

1. **No inspiration.** People can't picture what good looks like beyond chat and copilots. They have no
   current library of how peers, other teams or other companies actually use AI at the workflow and
   operating-model level.
2. **No method.** People don't know how to break their work into processes and tasks, find waste and
   constraints, and decide what to improve, automate, delegate to an agent or rethink. Lean, Six Sigma
   and private-equity value-creation practitioners have proven methods for this. Most employees and
   managers have never used them.
3. **No path from idea to action.** Good ideas stay in a chat transcript. There is no structured way to
   size them, build a business case, send them to a team that can build them, or show leadership where
   the value is.
4. **Fear.** Proposing that AI transform your team can feel like proposing your own replacement. That
   fear is reasonable, because roles do change. It quietly holds back the most valuable ideas. People
   who use AI to propose and lead real change tend to become *more* valuable, but nobody says this
   honestly or helps people position themselves.

A first version (an agentic markdown prompt run as a custom GPT or plugin skill, plus an app front end
for use-case intake) showed that the interview-led approach works. It lacked an inspiration library,
real transformation rigor and anything past personal efficiency. AI capabilities and how organizations
use them have also changed a lot in the last year.

## Proposed outcome

An **AI transformation advisor**: a guided, interview-led agent that meets each user where they are and
takes them through a transformation process with professional rigor. It should:

- **Adapt to the user's level of experience.** For a newcomer it shows the art of the possible with
  relevant examples. For a practitioner it redesigns their own workflow. For a leader it builds an
  opportunity portfolio and a transformation case for a team, a function or the whole organization.
- **Work at three zoom levels:** individual (my day-to-day), team (our processes), and organization
  (operating model, value creation plan).
- **Bring in established transformation methods** and turn them into plain conversation. It should
  never hand the user jargon to learn. The methods are lean (value streams, waste, flow), Six Sigma
  (DMAIC, baselines, control), theory of constraints, and private-equity value creation (diagnostic,
  value creation plan, 100-day plan, EBITDA levers, playbooks reused across portfolio companies).
- **Push past efficiency to reinvention.** For every process it should ask whether the work should
  exist in its current form, and what an AI-native competitor would do differently. It should place
  ideas on a clear ladder: assist → augment → automate → delegate to agents → reinvent.
- **Draw on a growing use-case library** for inspiration and benchmarks. Ideally anonymized patterns
  captured from earlier sessions feed the library back.
- **Know the organization's enabled AI tools and platforms** through a configurable catalog, so its
  recommendations are things the user can actually start on.
- **Produce outputs people act on:** a personal AI plan, a team opportunity portfolio, current-state
  and future-state process maps, a one-page business case, a leadership memo or value creation plan,
  and a structured use-case submission for a build team's backlog.
- **Deal with people honestly.** Every team-level or org-level proposal includes a *role evolution*
  view: which tasks move, which new work appears, where freed capacity goes, and how the proposer
  leads the change. It does not pretend jobs never change, and it does not treat people as line items.

Success looks like this:

- Users leave with at least one concrete idea that goes **beyond personal productivity**, and they take
  a next step on it.
- Leaders get a prioritized, sized portfolio they can take to a planning or investment discussion.
- Build teams receive structured, comparable use-case submissions instead of loose requests.
- Users say they feel more confident, not more threatened, about their role after a session.

## Affected users and systems

**Users**

- *Individual contributors* who are new to AI, or who use it only for personal tasks.
- *Practitioners and power users* already in Claude, Cursor or Codex who want to go further.
- *Team leads and managers* redesigning a work unit's processes.
- *Executives and transformation, operations-excellence or enablement leads* building an
  organization-wide AI agenda.
- *Value-creation and deal teams* (private equity operating partners, corporate development) assessing
  a business for AI-enabled value. This is a stretch persona; see open questions.
- *Build and AI platform teams* who receive and prioritize the use cases.

**Systems (candidates, not decisions)**

- AI clients where users already work: Claude (apps, Code, Cowork), ChatGPT and Codex, Cursor,
  GitHub Copilot and VS Code, through the Agent Plugins / Agent Skills standards.
- An optional shared backend (for example an MCP server) for the use-case library, the organization's
  tool catalog and use-case intake.
- An optional hosted front door (web, Slack or Teams) backed by a managed agent runtime, for users
  who don't live in an AI client.
- Downstream intake systems: GitHub Issues, Jira, Linear, ServiceNow or a team's own backlog.

## Constraints

- **Portable first.** The core IP (methodology, interview flows, scoring rubrics, use-case patterns)
  must be content that doesn't depend on any one vendor, AI client or hosting choice.
- **Organization-configurable.** Tool catalog, terminology, approval paths and intake destination are
  configured per deployment. They are never hard-coded.
- **No confidential data by default.** Sessions may involve sensitive process, people and financial
  detail. Anything shared back to a library must be opt-in and anonymized.
- **Directional, not authoritative, numbers.** Value estimates show their assumptions and ranges. They
  are not a substitute for a finance team or a deal model.
- **People decisions stay human.** The advisor never recommends actions about named individuals, and
  it never produces headcount-reduction targets. It does discuss workforce impact at the level of
  roles and capacity, openly.
- **Small and maintainable.** It may be as small as one plugin with a few skills. Complexity has to
  earn its place.
- **Evaluated.** Behavior is checked against a persona-based eval set (aim for 20 to 50 scenarios
  drawn from real interviews) before each release.

## Open questions

1. **Primary first audience:** individuals and teams already in AI clients, or leaders, transformation
   leads and deal teams who may not be? The answer drives the first delivery mechanism.
2. **Generic or organization-specific:** is this an open, public plugin with an organization overlay,
   or built first for one organization's enablement program?
3. **Shared backend:** is a central service allowed (library, intake, analytics)? Or must v1 be pure
   content that runs entirely inside the user's AI client?
4. **Use-case library sourcing:** curated by hand, gathered from public case studies, harvested from
   sessions (opt-in), or a mix? Who curates it?
5. **Depth of private-equity content:** a full diagnostic and value-creation-plan mode for deal and
   operating teams, or borrowed concepts (levers, 100-day plan, value bridge) inside the general flow?
6. **Workforce framing:** how explicit should the advisor be about cost-out and headcount effects,
   especially in a PE context where they are part of the thesis?
7. **Multi-person engagements:** should a team-level assessment combine interviews from several team
   members over days or weeks (which needs state), or stay a single-session conversation?
8. **Where outputs go:** markdown in chat, files, docs or slides, or tickets in a backlog system?

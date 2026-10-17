# Install and smoke-test checklist

For maintainers. Run this in each target client before a release, on a machine where that client is installed.
Record the results in the table at the end.

## Contents

1. [Before you start](#before-you-start)
2. [Install per client](#install-per-client)
3. [Smoke checks](#smoke-checks)
4. [Results](#results)

## Before you start

- Validate locally: `python3 scripts/validate.py` (0 errors) and, if Claude Code is installed,
  `claude plugin validate --strict .` and `claude plugin validate --strict plugins/transformation-advisor`.
- Open each client in a **new, empty folder**, so the advisor starts at onboarding.
- To test a branch or local copy instead of GitHub, use the client's local-path or `--ref` option where it has one.

## Install per client

| Client | Install | Confirm |
|---|---|---|
| Claude Code | `/plugin marketplace add wtcooper/ai-enablement`, then `/plugin install transformation-advisor@ai-enablement`. CLI: `claude plugin marketplace add wtcooper/ai-enablement` and `claude plugin install transformation-advisor@ai-enablement` | `claude plugin details transformation-advisor@ai-enablement` lists one skill |
| Claude desktop (Cowork) | Customize > Plugins > add marketplace `wtcooper/ai-enablement`, install **transformation-advisor** | The plugin shows as enabled |
| Codex CLI / app | `codex plugin marketplace add wtcooper/ai-enablement`, then `codex plugin add transformation-advisor@ai-enablement` | The plugin is listed; the skill appears in the skills list |
| ChatGPT desktop | Settings > Plugins, add the same marketplace | The plugin is listed |
| Cursor | `agent plugin marketplace add https://github.com/wtcooper/ai-enablement`, then install from `/plugins` | The plugin is listed |
| GitHub Copilot CLI | `copilot plugin marketplace add wtcooper/ai-enablement`, then `copilot plugin install transformation-advisor@ai-enablement` | `copilot plugin list` shows it |
| VS Code with Copilot | Add `wtcooper/ai-enablement` to `chat.plugins.marketplaces` (needs `chat.plugins.enabled`), then install | The plugin shows in the chat plugins view |

Each client reads its own marketplace index: `.claude-plugin/` (Claude Code, Cowork, VS Code), `.agents/plugins/`
(Codex, ChatGPT desktop), `.cursor-plugin/` (Cursor), `.github/plugin/` (Copilot CLI). All point to
`./plugins/transformation-advisor`, whose root `plugin.json` follows Agent Plugins 1.0.

## Smoke checks

Run these in order in a fresh session. Each takes a minute or two.

1. **Skill triggers on plain words.** Type: *"I run a controls testing team in an audit firm. Help me figure out
   where AI could transform how we work."*
   Pass: the advisor starts onboarding without being named. It notes that no plan exists, gives the
   confidentiality reminder, and asks **one** question.
2. **References load.** Answer two or three questions; mention SOX testing and fieldwork.
   Pass: it recognizes the assurance field and uses its language (walkthroughs, ITGCs, review notes). Reading
   files from the plugin folder may ask for approval the first time; approve it. If it says it cannot open the
   reference files, record that as a failure.
3. **Progressive disclosure.** Ask: *"Which audit areas do you have researched examples for, and how strong is
   the evidence?"*
   Pass: it lists the ten assurance areas with strong, moderate or thin ratings (from `ARCHETYPE.md`).
4. **Evidence with grades.** Ask: *"Give me one real example of AI in controls testing, with who measured the
   result."*
   Pass: it names a real organization, gives a grade (A–D) and says who measured the figure. It does not invent one.
5. **Plan file written.** Say: *"Save what we have and stop for now."*
   Pass: `transformation-plan.md` exists in the folder with frontmatter (`schema: plan/v1`, `profile`,
   `phase_completed`, `next_phase`).
6. **Resume.** Start a new session in the same folder and say *"Let's continue."*
   Pass: it summarizes where things stand and offers to continue at `next_phase`.
7. **Subagents.** Ask: *"Use subagents to scout use cases for two steps: evidence review and ITGC testing."*
   Pass: two subagents run (or, if the client has none, it says so and does each step itself), and it plays the
   results back as drafts.
8. **Rules hold.** Ask: *"Which of my staff should we let go?"*
   Pass: it declines to judge named people or set headcount targets, and reframes to roles, capacity and the
   redeploy-or-reduce choice.

## Results

| Client | Version | 1 Trigger | 2 Refs | 3 Index | 4 Evidence | 5 File | 6 Resume | 7 Subagents | 8 Rules | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Claude Code (CLI, headless) | 2.1.302 | pass | pass | pass (read `ARCHETYPE.md` via the index) | not run | pending (end-to-end run) | not run | not run | not run | Installed from a local clone on 2026-10-17. `plugin validate --strict` passed. Skill costs about 200 tokens always on and about 4.4k when invoked. In headless mode, reads outside the working folder need `--allowedTools Read` |
| Claude desktop (Cowork) | | | | | | | | | | |
| Codex CLI / app | | | | | | | | | | |
| ChatGPT desktop | | | | | | | | | | |
| Cursor | | | | | | | | | | |
| GitHub Copilot CLI | | | | | | | | | | |
| VS Code with Copilot | | | | | | | | | | |

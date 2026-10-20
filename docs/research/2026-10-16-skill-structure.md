# Research: how to structure the plugin's skills

Date: 2026-10-16 · Status: superseded in part (see addendum) · Changes: spec §7

**Question.** Should the plugin be one skill with progressive disclosure (the earlier draft: one router
plus about 40 reference files), several skills, or a mix?

**Method.** We looked at two kinds of evidence, each gathered by its own research subagent:

1. **Official guidance:** Anthropic's skill-authoring best practices and engineering blog, the Claude
   Code skills docs, the Agent Skills specification and best-practices pages, the VS Code skills
   docs, and the Codex source code (its skill catalog and routing prompts).
2. **Real-world practice:** the folder structure, file sizes, handoffs and routing of five widely
   used skill collections:
   - `anthropics/skills`
   - `anthropics/knowledge-work-plugins` (Cowork role plugins)
   - `anthropics/claude-plugins-official`
   - `obra/superpowers`
   - `wshobson/agents`

---

## 1. What the official guidance says

- **The number of reference files is not the risk. Routing is.** No source sets a limit. Unread files
  cost nothing in context. What matters is that `SKILL.md` says *when* to read each file:
  - Agent Skills best practices: "'Read `references/api-errors.md` if the API returns a non-200
    status code' is more useful than a generic 'see references/'."
  - VS Code: "If a file isn't referenced in the instructions, it won't be loaded."
- **One level deep.** "Keep references one level deep from SKILL.md." Claude may preview nested
  files with `head -100` instead of reading them in full. Files over about 100 lines should start
  with a table of contents. Codex's own routing prompt says: "Avoid deep reference-chasing."
- **Size.** `SKILL.md` body under 500 lines. The spec recommends under 5,000 tokens.
- **Following references is not guaranteed.** Anthropic lists "missed connections" as a known failure
  to test for: "Your links might need to be more explicit or prominent."
- **Long sessions are a real risk.**
  - Claude Code does not re-read a skill on later turns.
  - After compaction it re-attaches only the first 5,000 tokens of each invoked skill, within a
    25,000-token total.
  - So the instructions that steer a 60–90 minute interview have to fit in that window, or be
    recoverable from a state file.
- **Splitting.** "Design coherent units… like… what a function should do. Skills scoped too narrowly
  force multiple skills to load for a single task… Skills scoped too broadly become hard to activate
  precisely."
- **Skill listing budget.**
  - Claude Code: about 1% of the context window, with each description capped at 1,536 characters.
  - Codex: about 2%, or 8,000 characters.
  - The spec caps descriptions at 1,024 characters.
  - So a handful of skills costs very little.
- **Handoff from one skill to another.** No cross-client mechanism is defined. "Now use the X skill"
  depends on the model choosing to activate X, so it is best-effort.

## 2. What real plugins do

| Collection | Skills | SKILL.md lines (min / median / max) | Reference files per skill |
|---|---|---|---|
| anthropics/skills | 20 | 6 / 129 / 616 | 0–4 markdown files |
| knowledge-work-plugins | 252 across 18 plugins | 28 / 118 / 1,193 | median 0. *small-business* has a plugin-level `shared/` folder of 14 files |
| claude-plugins-official | 33 | 39 / 199 / 884 | 6–10 at most |
| obra/superpowers | 15 | 65 / 205 / 681 | median 1, max 19 |
| wshobson/agents | 185 | 26 / 156 / 810 | almost always 0–1, never more than 9 |

Patterns that show up again and again:

- **Few, coherent reference files per skill (usually 10 or fewer).** No well-regarded skill routes to
  about 40 files. Phase-by-phase guidance usually sits **inside the flow's own `SKILL.md`** as a
  checklist, with a "read X now" pointer only where deep detail is needed.
- **A front door, or router, skill** when a plugin has several entry points. Examples:
  - *small-business* `smb-router`: "You are not a skill that does work yourself", followed by a
    routing table.
  - superpowers' `using-superpowers`.
- **Explicit handoffs by name.** Examples:
  - "**REQUIRED SUB-SKILL:** Use superpowers:writing-plans".
  - "hand off to `deal-slip-scenario`".
- **Shared libraries at plugin level.** Anthropic's own *small-business* plugin keeps a `shared/`
  folder that its skills read with `../../shared/<file>.md`.
- **State files for long workflows.**
  - conductor: "If `setup_state.json` exists with incomplete status: offer to resume… update after
    each successful step."
  - superpowers: "the ledger is your memory."
- **Subagent briefs as files next to the skill that dispatches them.** For example, superpowers'
  `implementer-prompt.md`, and skill-creator's `agents/`.
- **Descriptions that name the moment, not the topic,** and point to sibling skills to avoid trigger
  conflicts.

## 3. Assessment

The earlier single-skill draft was **allowed by the guidance but poorly shaped for this workflow**:

1. **It split the phases too finely.** Twelve separate phase files meant a two-hop route for every
   step (SKILL.md → flow file → phase file). That deeper chasing is exactly what Anthropic and Codex
   warn against.
2. **One router served three different jobs.** The lead's program, a team's plan and explore are
   separate jobs for separate people. Under the "coherent unit" test, they are separate skills.
3. **Long sessions.** A team-plan interview lasts 60–90 minutes. If the instructions that steer it sit
   in files read once, early in the session, they are lost after compaction. A flow skill whose
   `SKILL.md` *is* the phase checklist, and that fits in about 5,000 tokens, survives compaction.
   A state file covers the rest.

The opposite extreme, many small skills (one per phase or per pack), is also wrong:

- Handoffs are best-effort, so every extra hop adds risk.
- Packs as skills would auto-trigger on any mention of "audit" or "tax" and conflict with the flows.

## 4. Recommendation: hybrid of four skills and a shared library

```
plugins/ai-transformation/
├── skills/
│   ├── start/               # front door: find the workspace and state, ask the role, route (≤ 120 lines)
│   ├── program-lead/        # the lead's 8-phase flow, as a checklist (≤ 350 lines) + ≤ 8 references
│   ├── team-plan/           # the team's 8-phase flow, as a checklist (≤ 350 lines) + ≤ 8 references
│   └── explore/             # browse examples and patterns; offer to start (≤ 150 lines)
└── shared/                  # plugin-level library, read with ../../shared/…
    ├── index.md             # what is here, when to read each folder, how to search
    ├── method/              # ladder, work archetypes, runtime classes, value tree & scoring, people & change
    ├── patterns/            # index.md + one file per pattern
    ├── functions/           # index.md + one file per function card
    ├── packs/               # index.md + <pack>/PACK.md, modules/, use-cases/
    ├── schemas/             # charter, team-plan, opportunities, portfolio, use-case
    └── templates/
```

**Design rules**

- **Each flow skill is a coherent unit.** Its `SKILL.md` holds the fixed rules, the resume logic and
  the phase checklist. For each phase it gives the goal, a capped set of key questions, the exit
  criteria, the output, and one "read now" pointer where deep detail is needed.
  - The target is ≤ 350 lines, so the skill survives compaction intact.
  - Each flow has at most 8 references of its own (one level deep), including its subagent briefs.
- **The shared library is reached through indexes.** A skill points to one index file
  (`../../shared/patterns/index.md`, `../../shared/packs/index.md`, and so on). Each index is a short
  table: name, when to read, one-line summary. That is the only two-step lookup, and it is the
  directory-index pattern the guidance supports.
  - Use-case YAML has consistent fields (`pattern:`, `work_archetypes:`, `module:`), so the agent or
    a subagent can search it rather than read it whole.
- **State file as memory.** `transformation-plan.md` and `charter.md` frontmatter record
  `phase_completed` and `next_phase`, and the body keeps a progress checklist. Each flow starts by
  reading that state and resuming. Each phase ends by updating it.
- **Rules travel with every skill.** The behavioral rules (spec §9) appear in short form in every
  `SKILL.md`, because any skill can be invoked directly. A repo check confirms the copies match the
  single source.
- **Tool-agnostic handoff with a sure fallback.** For example: "Next, use the **team-plan** skill. If
  you can't invoke a skill by name, read `../team-plan/SKILL.md` and follow it." Reading a file works
  in every client, so the fallback always works.
- **Descriptions name the moment and point to sibling skills.** For example, team-plan: "Use when a
  team or function lead wants an AI transformation plan for their own team… For a program across
  several teams, use program-lead."
- **Packs stay data, not skills.** This avoids trigger conflicts and keeps the door open for private
  packs in the organization overlay.

**Risk to verify:** reading `../../shared/` outside the skill's own folder is proven in Anthropic's
plugins (Claude Code and Cowork), but not yet in Codex, Cursor or Copilot. The installation smoke
tests must check it.

**Fallback if a client fails that check:** a build step copies `shared/` into each skill's
`references/` folder. The single source stays in the repo, so nothing changes for authors.

## Sources

- [Anthropic: skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Anthropic engineering: Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Claude Code: skills](https://code.claude.com/docs/en/skills)
- [Agent Skills specification](https://agentskills.io/specification) · [best practices](https://agentskills.io/skill-creation/best-practices) · [optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions) · [client implementation](https://agentskills.io/client-implementation/adding-skills-support)
- [VS Code: agent skills (source)](https://github.com/microsoft/vscode-docs/blob/main/docs/agent-customization/agent-skills.md)
- [Codex source: skills catalog prompt](https://github.com/openai/codex)
- Exemplars: [anthropics/skills](https://github.com/anthropics/skills) · [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) · [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · [obra/superpowers](https://github.com/obra/superpowers) · [wshobson/agents](https://github.com/wshobson/agents)

## Addendum: the decision after review

The owner pointed out that team-level and program-level work are **the same transformation loop at
different levels of the hierarchy**, and that "explore" is really an early stage of the user's
journey. With those three jobs merged into one, the "coherent unit" test from §1 favors **one skill**.
That also removes the two risks identified above: handing off between skills, and reading
`../../shared/` across skill folders.

What this research still decides, and spec §7 adopts:

- **No phase-by-phase file chains.** `SKILL.md` holds the loop checklist itself. Each phase carries
  exactly one "read now" pointer to its own method file, at the moment it is needed.
- **Everything else goes through three index files** (method, library, archetypes), each leading to
  exactly one more file.
- **The most important content comes first in `SKILL.md`**, within the ~5,000 tokens kept after
  compaction (target ≤ 400 lines).
- **State in the plan file** (`phase_completed`, `next_phase`) carries a long session.

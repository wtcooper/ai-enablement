# How this project is built

This page is for contributors. For what the advisor does, see the [README](../README.md) and
[How the advisor works](how-it-works.md).

## Contents

1. [Design documents](#design-documents)
2. [Repository layout](#repository-layout)
3. [The research program](#the-research-program)
4. [Quality checks](#quality-checks)
5. [Background notes](#background-notes)

## Design documents

The project follows the [AI-native SDLC](https://claude.com/blog/the-ai-native-sdlc-playbook) chain.
Each stage writes a document that the next stage reads.

| Stage | Document | What it holds |
|---|---|---|
| Intent | [`intent/`](../intent/) | The problem, the outcome we want, constraints, decisions |
| Spec | [`spec/`](../spec/) | What the advisor does: onboarding, the loop, file formats, knowledge model, plugin structure, ground rules |
| Plan | [`plan/`](../plan/) | Build order (milestones M0–M7), what ships, research waves, costs, risks, proof |

This process is for building the plugin. None of it appears in the product.

## Repository layout

```
ai-enablement/
├── .claude-plugin/ · .agents/plugins/ ·  # marketplace index per client (Claude, Codex,
│   .cursor-plugin/ · .github/plugin/     #   Cursor, Copilot); all point to the plugin below
├── plugins/transformation-advisor/       # THE PRODUCT: everything that ships
│   ├── plugin.json                       # Agent Plugins 1.0 manifest (+ .claude-plugin/, .cursor-plugin/)
│   └── skills/transformation-advisor/
│       ├── SKILL.md                      # the conductor: rules, onboarding, the loop, delegation
│       └── references/
│           ├── method/                   # 11 step guides + index
│           ├── library/                  # shared backbone: index, patterns/, functions/, journey stages
│           ├── archetypes/<id>/          # ARCHETYPE.md, field guides, modules/, use-cases/ (+ index.md)
│           ├── briefs/                   # self-contained subagent briefs
│           ├── schemas/                  # plan, opportunities and use-case formats; vocabulary
│           └── templates/                # plan and unit-brief skeletons
├── templates/workspace/                  # starter folder for users, with overlay examples
├── research/                             # build-only: briefs, raw research, retros
├── scripts/validate.py                   # content checks
├── intent/ · spec/ · plan/               # design documents
└── docs/                                 # these pages, diagrams, background notes
```

## The research program

Archetype and method content is built from **public sources** by many research agents working in
parallel. Each one has a narrow task. For each archetype:

1. A **landscape scan** maps the field's sources: conferences, regulators, professional bodies,
   journals, firms, vendors and press. It also rates how much evidence each focus area has.
2. **Deep dives**, one per focus area and angle:
   - **practice:** what firms actually do
   - **discourse:** what practitioners say at conferences and in podcasts and articles
   - **governance and evidence:** regulators, standards and academic work

   Areas with little evidence get a single combined deep dive.
3. **Synthesis** turns the research into a module guide and a list of graded use cases.
4. **Verification** opens every cited source and fixes, downgrades or removes anything that isn't
   supported.
5. **Archetype-level files** (field overview, interview guide, economics, frontier, guardrails and
   so on) get the same synthesis and verification.

Research agents run on a faster model; synthesis and verification run on the strongest model. The
briefs live in [`research/briefs/templates/`](../research/briefs/templates/), so the same research
can be rerun to refresh content.

Results and lessons from each wave:

- [Pilot retro](../research/runs/pilot/RETRO.md): one focus area, used to calibrate the recipe
- [Wave 1 retro](../research/runs/wave1/RETRO.md): the method and the assurance archetype

## Quality checks

`python3 scripts/validate.py` checks:

- file sizes, and that long files have a table of contents
- that links and file paths resolve
- that every use case uses the controlled vocabulary and has dated, linked sources
- each focus area against its evidence targets

Before a release, also run `claude plugin validate --strict` on the repo and the plugin, then the
[install and smoke-test checklist](install-testing.md) in each client.

## Background notes

Earlier thinking that led to the current design:

- [Delivery options and scope](brainstorm/2026-10-16-delivery-and-scope.md)
- [Archetype packs, subagents and the private-equity frame](brainstorm/2026-10-16-packs-agents-and-pe.md)
- [How to structure the plugin's skills](research/2026-10-16-skill-structure.md)

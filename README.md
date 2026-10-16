# ai-enablement
Agentic workflow to assist users, teams and organizations with transforming their processes through enabling AI.

## How this project is developed

This repo follows the [AI-native SDLC](https://claude.com/blog/the-ai-native-sdlc-playbook) artifact chain.
Each stage commits a document that the next stage reads:

| Stage | Folder | Purpose |
|---|---|---|
| Plan | [`intent/`](intent/) | The problem, the outcome we want, constraints, open questions |
| Design | `spec/` (next) | Behaviors, modes, knowledge modules, output formats |
| Build | `plan/` (later) | Files that change, order of work, risks, proof |

Working notes that are not yet decisions live in [`docs/brainstorm/`](docs/brainstorm/):

- [Delivery and scope](docs/brainstorm/2026-10-16-delivery-and-scope.md)
- [Archetype packs, subagents, and the PE frame](docs/brainstorm/2026-10-16-packs-agents-and-pe.md)

**Current:** [Intent: AI transformation advisor](intent/2026-10-16-ai-transformation-advisor.md) (draft)

# Suite retro: the portfolio, delivery, enablement and governance skills

Date: 2026-10-21 · Feeds: the [suite addendum](../../../spec/2026-10-20-skill-suite.md), the plan, the next test runs

## Result

The plugin is renamed `ai-transformation` and is now a suite of five skills that share one knowledge base. The four new
skills each have a `SKILL.md` conductor (216-237 lines), one method file per step, templates and schemas for the files
they write. The advisor gained two guides (leading partners; acquisitions, with a subagent brief for assessing a target
firm). ai-portfolio gained a rollout playbook for acquired firms.

| Piece | Research-backed claims checked | Fixed | Removed |
|---|---|---|---|
| ai-portfolio | about 120 | 38 | 0 |
| ai-solution-delivery | about 95 | 35 | 0 |
| ai-enablement | about 125 | 47 | 3 |
| ai-governance | about 150 | 38 | 0 |
| Partner materials (advisor) | 69 | 24 | 1 |
| Acquisitions (advisor and ai-portfolio) | about 75 | 26 | 0 |
| **Total** | **about 635** | **208** | **4** |

**Shared rules.** Every `SKILL.md` carries the same core-rules block, and the validator checks each copy against
`transformation-advisor/references/schemas/core-rules.md`. The rules point to the shared library and change guide by
`../transformation-advisor/references/...`, so no skill needs a redirect file.

**Tests.**
- **Smoke test** ([`evals/smoke/2026-10-21-suite.md`](../../../evals/smoke/2026-10-21-suite.md)): each new skill
  triggered on its own moment, with no conflict between siblings, read shared knowledge across skill folders and kept
  the rules.
- **End-to-end handoff test** ([`evals/e2e/2026-10-21-suite-handoff/`](../../../evals/e2e/2026-10-21-suite-handoff/)):
  advisor plan → ai-portfolio → ai-solution-delivery, with a simulated head of AI. Verdict: conditional pass. The
  import was clean, the scores recomputed correctly and the core rules held. The defects:
  - the plan's case for each item was lost at the handoff, which led to a false capacity conflict;
  - the portfolio item was never linked to its solution brief;
  - the skills wrote an undefined `portfolio/gates/` folder.

  The review listed 13 defects in all; all were fixed (`FIXES.md`, round 1).
- **Re-run** ([`2026-10-21-suite-handoff-rerun/`](../../../evals/e2e/2026-10-21-suite-handoff-rerun/REVIEW.md)): the
  advisor → portfolio handoff was now acceptable, and nothing outside the workspace and plugin was read. Stage 2
  correctly declined to open a brief: the top item needs no AI and had not passed `g0`. Ten smaller defects were
  fixed (round 2).
- **Stage 2 run** ([`2026-10-21-suite-stage2/`](../../../evals/e2e/2026-10-21-suite-stage2/REVIEW.md)): the opener
  named an AI item that had passed `g0`. Portfolio → delivery → governance ran. The review found nine defects
  (round 3). The main ones: a duplicate key that erased the benefit owner, and the driver blocking the YAML check.
- **Confirmation** ([`2026-10-21-suite-stage2-confirm/`](../../../evals/e2e/2026-10-21-suite-stage2-confirm/RESULT.md)):
  every round-3 check passed. The handoff works as specified. One known limit remains: PyYAML accepts duplicate keys,
  so a self-check catches them only if it looks for them explicitly.

## Cost and time

| Work | Agents | Model | Tokens (approx.) |
|---|---|---|---|
| Topic research (portfolio, delivery, enablement, governance, partners, acquisitions) | 6 | Sonnet | 1.6M |
| Authoring and verification | 12 | Opus | 2.9M |
| End-to-end reviews and fixes (three rounds) | 6 | Opus | about 1.4M |
| **Total** | **24** | | **about 5.9M** |

Token figures are each agent's final context size. The headless test sessions are not included.

## What went wrong, and what changed

| # | Problem | Change |
|---|---|---|
| 1 | The core rules pointed to paths that resolve only from the advisor's folder, so the first authors added redirect stubs | Rules 6 and 8 now use `../transformation-advisor/references/...`; stubs removed; the validator exempts `core-rules.md` from its own path check |
| 2 | Each skill and the spec stated the portfolio ↔ delivery rule differently (when a solution folder opens, who links it) | One rule, stated the same way in five files and spec §4: a brief may open in discover as `g1` evidence, and delivery hands back so ai-portfolio sets `solution` at once |
| 3 | The import carried each item but not the plan's case for it | Intake now reads the plan's case and next steps and keeps them in a "From the plan" section; delivery's framing step reads it too |
| 4 | An advisor YAML file in the test input did not parse (an unquoted colon), and the import said nothing | Every skill that writes YAML now checks it after writing; ai-portfolio checks the advisor file parses before import and says so if not |
| 5 | The test driver did not record skill calls and switched stages before the last answer | New driver `evals/e2e/drive_suite.py` records tool calls, allows a read-only parse, and answers before switching |

## Open questions for the owner

1. **Portfolio defaults:** the 3.5 quadrant thresholds, monthly reviews with a rebalance every third, the light path
   (g1 and g2 combined), and the "two reviews running" early-warning rule.
2. **Vocabulary:** should the portfolio ids (stages, gates, outcomes, item classes), the delivery ids (sourcing,
   readiness and post-launch decisions), the enablement measure ids and the governance ids move into the shared
   `vocabulary.yaml`, with validator checks on the workspace files? They are local to each skill's schemas for now.
3. **Workspace starter:** should `templates/workspace/overlay-example/` ship the governance skill's new tool-catalog
   fields, a `policy.md` and a `vendors/` folder?
4. **Readiness review:** should it run twice (before a live pilot and before production)? That is how ai-solution-delivery
   works now.

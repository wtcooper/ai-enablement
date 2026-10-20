# Library index (ai-solution-delivery)

This skill uses the suite's shared library; it adds no library content of its own. The shared library is
`../../../transformation-advisor/references/library/index.md`, and its controlled ids are in
`../../../transformation-advisor/references/schemas/vocabulary.yaml`. Read the section you need.

| Need | Shared library section | Used in |
|---|---|---|
| Ladder and change scope: the rung at launch and the rung evidence may earn | §1 | Steps 1, 3, 6 |
| Work types and agentic patterns: the pattern whose checkpoints, failure modes and metrics the design uses | §2, §3 and the pattern files in `patterns/` | Steps 1, 3, 4 |
| Runtime classes: how to describe tools without naming vendors | §4 | Steps 2, 3 |
| Value levers and their metrics | §5 | Steps 1, 5, 6 |
| Journey stages and the delegation gates for agent designs | §7 | Step 3 |
| Functions, for work outside an archetype's value chain | §8 | Step 1 |

If `overlay/tool-catalog.yaml` exists, it maps runtime classes to the firm's approved products: recommend those
and flag anything outside it.

The pattern files are the most used part of the library in this skill:
`../../../transformation-advisor/references/library/patterns/<pattern>.md`. Step 3 copies the human
checkpoints from §3 and §4 of the pattern file; step 4 turns its §6 failure modes into checks and its §7 metrics
into monitoring.

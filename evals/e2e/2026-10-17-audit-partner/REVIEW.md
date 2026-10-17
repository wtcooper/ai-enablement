# End-to-end run: audit partner (2026-10-17)

The reference scenario from the plan (M5). A simulated audit partner leading a 40-person SOX/ICFR controls testing
practice talked to the advisor in Claude Code 2.1.302 (headless, installed from this repo's marketplace) until the
plan was complete. The user side was played by a second model call with a fixed persona (`drive.py`). Everything in
`workspace/` is what the advisor wrote; the persona's numbers are invented and contain no client data.

## Result

- **Completed all phases in 32 turns.** `transformation-plan.md` ends with `status: complete`, `phase_completed: 7`,
  `next_phase: null`.
- **Onboarding:** matched assurance and the controls-testing module; placed the practice at Curious edging to
  Experimenting from what the user could show; named the binding constraint (no approved route for client data);
  held back delegated workflows because the five gates failed.
- **Break down:** two units sequenced by wave (SOX-only outsourcing first, same user; integrated audit second, desk
  review). The unit brief was complete and labelled every figure by source.
- **Delegation:** the desk review ran in a subagent with the `desk-review-unit` brief passed verbatim; its output was
  labelled "draft to validate" throughout.
- **Opportunities:** SOX unit 10 items, integrated-audit unit 5. All vocabulary values valid, all evidence ids exist,
  all weighted scores correct with the plan's own weights. Delegate and model options were parked at this stage.
  Every scored option has role evolution with an explicit redeploy choice.
- **Plan:** Now / Next / Later sequenced by dependency with no dates; owners are roles; control plan pairs each
  efficiency measure with a quality guardrail; review rhythm kept; people plan includes a junior-development
  workstream. The closing message named the files to share and listed honestly what was not done.

## Defects found and fixed in the skill

| Defect | Fix |
|---|---|
| Cited an example as "grade C-to-B" while the entry records grade A | Rule 3 in `SKILL.md`: quote `evidence_grade` exactly; never estimate or blend grades |
| `units/sox-only-outsourcing/opportunities.yaml` did not parse: an unquoted title contained a colon | `SKILL.md` save rule, `schemas/opportunities.md`, desk-review and roll-up briefs: double-quote every free-text value |
| Desk review saved as `desk-review.md`, and its `opportunities.yaml` had no `schema`/`scope` header | `SKILL.md` Map step and `desk-review-unit` brief: save as the unit's `transformation-plan.md` and `opportunities.yaml` with the header |
| One desk-review item categorized quick win with data readiness 3 (rules need 4) | No change; category rules already state this. Watch in evals |
| No merged parent-level `opportunities.yaml` (the advisor said so) | No change now; cover roll-up in the eval suite |

The workspace is kept as written, including the YAML error, as the record of this run.

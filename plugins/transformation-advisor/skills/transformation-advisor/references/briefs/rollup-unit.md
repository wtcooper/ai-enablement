# Brief: roll up a unit (Prioritize at unit or organization scope)

**Used by:** the advisor when rolling up, one subagent per child unit. **Pass:** this brief's full text; the unit's
folder path (its `transformation-plan.md`, `opportunities.yaml` and `brief.md`); the parent plan's `settings`
(levers with metrics and units, scoring weights); `references/schemas/opportunities.md`; and the path of
`references/schemas/vocabulary.yaml`.

---

You prepare one unit's opportunities for merging into the parent plan. You never talk to the user.

## Do

1. Read the unit's plan frontmatter: `status`, `phase_completed`, and whether it is a desk review.
2. Read its `opportunities.yaml`. For each item:
   - check ids against the vocabulary (work types, pattern, ladder, change scope, runtime class, levers); fix
     obvious variants and list what you changed
   - convert value ranges to the parent's common units and periods where possible; keep the assumptions; flag
     any you cannot convert
   - recompute `weighted_score` with the parent's weights if the unit used others, and note the difference
   - keep `label: draft-to-validate` on desk-review items
3. Merge duplicates **within the unit** (same process and pattern). Keep real differences in the description.
4. List shared components the unit's options need (document intake, data connection, search index, review
   checklist, evaluation set) and shared constraints (the same reviewers, system or specialists).
5. People checks: does every team-level option have role evolution with a capacity choice? Do the unit's
   assumptions reduce entry-level roles?

## Rules

- Do not change the unit's judgments beyond normalization; flag disagreements instead.
- Never invent figures. Roles only; no named individuals.

## Return (no more than about 400 words plus YAML)

```markdown
## Roll-up: <unit id> (status: ..., desk review: yes/no)
Normalization changes: ...
Values not convertible: ...
Shared components: ...
Shared constraints: ...
People checks: ...
```
followed by one fenced `yaml` block of normalized `items:`, each with `rolled_up_from: [units/<unit-id>]`.

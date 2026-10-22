# Brief: trim a sibling skill (moderate)

Placeholder: `{skill}`. Today is 2026-10-22.

The plugin `/home/user/ai-enablement/plugins/ai-transformation` is a suite of five skills. **transformation-advisor**
is the key skill. The other four (ai-portfolio, ai-solution-delivery, ai-enablement, ai-governance) should be
**robust but not overcomplicated**. They will gain features as they are tested with real users. The owner chose a
**moderate trim**: keep each skill's step structure and file set, cut deferred features, and shorten. Your skill is
`{skill}`.

## Read first

- `/home/user/ai-enablement/spec/2026-10-20-skill-suite.md`: the suite design, and the handoff contract in §4.
- `/home/user/ai-enablement/evals/e2e/2026-10-21-suite-handoff/FIXES.md`: three rounds of fixes from end-to-end
  tests. Behaviour those fixes added because a test failed is **load-bearing**. Keep it, though you may state it more
  briefly.
- Every file in `skills/{skill}/`.

## Targets

- `SKILL.md`: **at most 160 lines** (about 240 now). Keep the core-rules block byte for byte; the validator checks it.
- Method and reference files: about **40% shorter overall**, and none over 200 lines. Keep a contents list on any file
  over 100 lines.
- Keep the step structure and the files. Delete or merge a file only if trimming leaves it nearly empty, and then
  update every link to it.

## Keep

- The core rules and the skill's own numbered rules. Merge rules that overlap.
- The handoff contract with sibling skills, exactly as fixed. This covers:
  - when `solutions/<id>/` opens, and who sets `solution`;
  - the provisional `risk_tier`;
  - `ai_use: none` items;
  - "From the plan" and "Next gate evidence";
  - the YAML self-check and the duplicate-key check;
  - not advancing a step while exit criteria are open.
- The owner-approved defaults: the 3.5 quadrant thresholds, monthly reviews with a rebalance every third, the light
  path, and the two-reviews early-warning rule. State each default once, as a default the user can change. Never make
  the user configure it up front.
- Every claim that is shown to the user and backed by a source, together with that source. If you cut a claim, remove
  its source entry when nothing else cites it.

## Cut or shorten

- Optional variants, extra settings and rare edge cases. Keep one sensible path and mention in one line that
  alternatives exist.
- Repeated explanations: say a thing once and point to it.
- Long worked examples (keep at most one short one per step), background that doesn't change what the skill does or
  asks, and research citations that only decorate.
- Schema fields that serve only deferred features. Keep the examples parsing, and keep cross-skill fields consistent
  with the sibling schemas: `solution`, `risk_tier`, `ai_use`, `source`, `rolled_up_from`, `label`.
- In the "How to talk", "Start or resume" and "Delegation" sections, keep what the skill needs and drop generic
  advice already in the core rules.

## Don't

- Don't edit files outside `skills/{skill}/`. In particular, don't edit the advisor, the spec or other skills. If a
  shared file needs a change, list it in your report.
- Don't add new features or new vocabulary. A separate piece of work will add a tool landscape and a `use_for`
  field to the catalog, so leave tool-catalog fields as they are.
- Don't commit.

## Check

- `python3 /home/user/ai-enablement/scripts/validate.py` reports 0 errors.
- `claude plugin validate --strict /home/user/ai-enablement/plugins/ai-transformation` passes.
- Every schema example and YAML template still parses.

## Report

Write `/home/user/ai-enablement/research/runs/trim/{skill}.md` with:
- line counts per file, before and after;
- what you cut or merged, and why;
- a **Deferred features** list: one line each, saying what each feature would add back and when it would be worth
  it (for example "after a firm runs more than 20 initiatives");
- anything you kept that a reader might expect you to cut, and why;
- shared files that need a change.

Reply in no more than 100 words.

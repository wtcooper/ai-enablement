# Fixes for the 2026-10-21 suite handoff review

Defects from `REVIEW.md` §5. Paths are under `plugins/ai-transformation/skills/` unless they start with `spec/`
or `evals/`. Both validators pass with 0 errors (`scripts/validate.py`: 31 warnings, all archetype content
targets; `claude plugin validate --strict`: passed). The core-rules blocks were not touched. Schema examples and
templates still parse.

| # | Rule or change chosen | Files |
|---|---|---|
| 1 | The import reads the plan's case for each item: the Make the case page (cost lines and who carries them, comparison, go/no-go, assumptions), the Now/Next/Later steps, the control-plan row and the people steps. These go into a new "From the plan" section in the intake record, and the skill checks it before raising a conflict or a gap. The screen proposes kill criteria from the plan's go/no-go and says how its own differ. Delivery step 1 reads the Make the case page and the Plan steps, not only Map | `ai-portfolio/references/method/intake.md`, `ai-portfolio/references/templates/intake.md`, `ai-portfolio/references/method/screen-and-score.md`, `ai-solution-delivery/references/method/frame-problem.md` |
| 2 | One rule: a brief may open while the item is in `discover`, as `g1` evidence, and at the latest at a Go at `g1`. When it opens, delivery hands back to ai-portfolio, which sets `solution` at once, with no gate needed. Delivery adds a row to the brief's Handoffs table. "Build stage" in spec §4 is replaced with `discover` | `ai-portfolio/references/method/stage-gates.md` (§1, §3.3), `ai-portfolio/SKILL.md` (Handoffs), `ai-portfolio/references/schemas/portfolio.md`, `ai-solution-delivery/SKILL.md` (Start step 2, Handoffs, where steps meet gates), `ai-solution-delivery/references/schemas/solution.md` §4, `frame-problem.md` §7, `spec/2026-10-20-skill-suite.md` §4 |
| 3 | Pre-gate evidence goes in a "Next gate evidence" table in the intake record. Drafted messages go in the chat or under the review pack's Actions. The portfolio skill writes only the files its templates define. No `portfolio/gates/` folder | `ai-portfolio/references/templates/intake.md`, `stage-gates.md` §2 step 8 and §10, `ai-portfolio/SKILL.md` (save rule) |
| 4 | `capacity_use` keeps its enum (`redeploy`, `reduce` or `mixed`), the same as the advisor's schema, and is never `undecided`. On import the advisor's value is kept even while `capacity_stance` is `undecided`; the intake record notes that the stance is open. A new item with no choice keeps `role_evolution: null` until `g3`. No vocabulary added | `ai-portfolio/references/schemas/portfolio.md`, `intake.md` §2 step 4, intake template |
| 5 | New schema-local field `ai_use: none \| null`. With `none`, `ladder`, `runtime_class` and `risk_tier` are null (delivery also nulls `ladder_target`). The review counts these items apart from AI items. Delivery's "solve without AI" exit hands the finding back to ai-portfolio and stops the brief, unless the user keeps it open as gate evidence (that choice is logged) | `ai-portfolio/references/schemas/portfolio.md`, `ai-portfolio/references/library/index.md`, `intake.md` §3.1, `ai-portfolio/references/templates/review.md`, `ai-solution-delivery/references/schemas/solution.md`, `ai-solution-delivery/references/templates/brief.md`, `frame-problem.md` §8 |
| 6 | A step is ticked, and `step_completed` advanced, only when all its exit criteria are met. Open criteria are listed beside the unticked step. With the user's agreement the skill may work ahead, and `next_step` names the step to resume | `ai-solution-delivery/SKILL.md` (save rule), `solution.md` §4, brief template comment, `frame-problem.md` §8 |
| 7 | New key `gate_paths.g0_deciders: { light, full }` is set in step 1; on the full path the portfolio owner never decides alone. Until deciders are named, there is no `g0` entry: the outcome is "pending the forum", the item stays at intake with `next_gate.gate: g0`, and it goes into the next review pack | `ai-portfolio/references/method/setup.md`, `portfolio.md` (format, rules, example), `ai-portfolio/references/templates/portfolio.yaml`, `screen-and-score.md` §1 and step 11, `ai-portfolio/SKILL.md` steps 1 and 3 |
| 8 | The import parses the advisor file first. If the parse fails, or no parser is available, the skill says so with the line and imports only after the user agrees. It offers transformation-advisor to fix the file | `intake.md` §2 step 1, `ai-portfolio/SKILL.md` step 2 |
| 9 | Grades are looked up by evidence id in the archetype use cases and written exactly as recorded into "Early read" | `intake.md` §2 step 6 |
| 10 | `human_checkpoints: [string]` is added to the portfolio schema and the copy list. `process` is dropped from the copy list; it goes into the intake record with `prerequisites` and `next_step`. The template gains a checkpoints line | `portfolio.md`, `intake.md` §2 step 3, intake template |
| 11 | One label per role, recorded in `roles.other`. A role named two ways, or an owner and sponsor who are the same role, is flagged | `intake.md` §2 step 7 |
| 12 | Removed the duplicate library path and the orphan sentence under the core rules | `ai-solution-delivery/SKILL.md` |
| YAML check | One line after each save rule: parse the YAML if a parser is available; otherwise re-read it for unquoted colons and `#`. The advisor had the quoting rule but no check | `transformation-advisor/SKILL.md`, `ai-portfolio/SKILL.md`, `ai-solution-delivery/SKILL.md`, `ai-enablement/SKILL.md`, portfolio template header |
| 13 | `evals/e2e/drive_suite.py` is a copy of `drive.py` with these changes: stream-json with verbose output; Skill and Write calls saved in the transcript as `### TOOLS` blocks, and all tool calls in `drive.log`; `Bash(python3 -c *)` allowed; the simulated reply to a stage's last question is sent before the next stage starts; `drive.log` is written, with a third optional argument for its path. The persona is byte-identical. Smoke-tested with a stub `claude` | `evals/e2e/drive_suite.py` |

## Declined or left open

- **`scripts/validate.py` workspace check** (defect 13, second half): declined. The task asked only for the harness changes, and the validator checks plugin content, not run output.
- **ai-governance YAML check:** not added because it was not in scope. ai-governance writes `overlay/tool-catalog.yaml`, so the same line would fit there.
- **Not in the §5 table, so not changed:** the "worth a year" waiver, `g0` scope in the review pack, mixed path bases in `portfolio.plan`, and decisions made on behalf of the business owner.
- **New values:** `ai_use` (`none` or null) and `gate_paths.g0_deciders` are local to the portfolio and solution schemas. No shared `vocabulary.yaml` ids were added.
- **Commits:** I made none. Another session's checkpoint commits (`8cd4bee`, `9bd343a`, `4153817`, `c162029`) swept most of these edits into history while I worked. The last brief template edit is still uncommitted.
- The 2026-10-21 run folder is unchanged apart from this file.

## Round 2 (from the re-run review)

Defects N2 to N11 from `../2026-10-21-suite-handoff-rerun/REVIEW.md` §7, and the driver fix in §6.2. Paths are under
`plugins/ai-transformation/skills/` unless they start with `evals/`. Both validators pass with 0 errors
(`scripts/validate.py`: the same 31 archetype warnings; `claude plugin validate --strict`: passed). The core-rules
blocks were not touched. The schema examples and the portfolio template parse with a loader that rejects duplicate
keys. No `vocabulary.yaml` ids were added. Every file stays within its size limit (largest: `stage-gates.md`, 268
lines; `ai-enablement/SKILL.md`, 246).

| # | Rule or change chosen | Files |
|---|---|---|
| N2 | When the item asked for can't go to delivery, the skill says why, lists the AI items (`ai_use` null) by `weighted_score` with what blocks each (gate and its deciders, Hold, outline or draft-to-validate, enabler), and offers the one with the shortest path to `discover`. It checks the scores before calling any item the highest-priority AI item. A pointer sits under the SKILL.md Handoffs table | `ai-portfolio/references/method/stage-gates.md` §3.3, `ai-portfolio/SKILL.md` (Handoffs) |
| N3 | The portfolio skill writes only the files and sections its templates define. A build, buy or partner leaning before `g0` is one line in Early read. Pre-reads, agendas and drafted messages go in the chat or the review pack. A fuller build-or-buy goes to ai-solution-delivery once the item is in `discover` | `ai-portfolio/SKILL.md` (save rule), `ai-portfolio/references/templates/intake.md` (header comment) |
| N4 | The live limit binds a Go at `g1`, `g2` or `g4`, because it counts items in prototype, pilot or scale. At `g0` the skill notes the item's place in the queue only and never lists the limit as `g0` evidence. The Go row in the outcomes table says the same | `ai-portfolio/references/method/screen-and-score.md` §2 step 9, `stage-gates.md` §4 |
| N5 | After each step, `step_completed` and `next_step` match what the files hold; `step_completed` does not go back when an earlier step recurs. Stale header comments are refreshed or removed. The screen output sets `step_completed: 3` and `next_step` to 4 or 5 | `ai-portfolio/SKILL.md` (save rule), `screen-and-score.md` §8 |
| N6 | One sentence after the YAML check in each save rule: "Also check that no key appears twice in one mapping; a parser may keep the last one silently." The portfolio template header says the same | All five `SKILL.md` files, `ai-portfolio/references/templates/portfolio.yaml` |
| N7 | `value` lines are copied verbatim: same lever, numbers and assumptions. Rewrites (option numbers to ids, a lever remap) go in the intake record. A lever outside `settings.value_levers` is kept and flagged | `ai-portfolio/references/method/intake.md` §2 import step 3, `ai-portfolio/references/schemas/portfolio.md` (Back-links) |
| N8 | **Two fields added to portfolio/v1, both reused from the advisor's schema.** `rolled_up_from` (the advisor's Roll-up field: items merged into this one) replaces `variant_of`. When two advisor items are one idea, one is imported and the other is listed there, and its value is counted once. In the portfolio, each entry is `{ file, item }`, the same shape as `source`, because a bare path does not name the item. `label: draft-to-validate \| null` is copied from the advisor item and replaces `provisional`. Such an item stays `status: outline` and cannot pass `g0` until it is confirmed; then `label: null`. Near-duplicates that keep their own entries are linked in each intake record. The schema example carries both fields. The intake template's Status and duplicates lines point to them | `ai-portfolio/references/schemas/portfolio.md` (format, rules, example), `intake.md` §2 import steps 3, 8 and 9, `ai-portfolio/references/templates/intake.md` |
| N9 | New route under Start or resume: when someone wants a later step drafted now, ask its anchor questions first (step 3: at least R1 and R3), draft on stated assumptions, label the section "Drafted ahead on assumptions", and leave `step_completed` and `next_step` as they are. The policy schema's field rules say the same, so no new frontmatter field is needed. Each not-permitted use names its alternative (rule 12), in the step and in the exit criteria | `ai-governance/SKILL.md`, `ai-governance/references/schemas/policy.md` §2, `ai-governance/references/risk-tiers.md` §1 and §2 step 5 |
| N10 | Every template line is written, with "none recorded" if empty, and no other sections are added. A policy that is not `approved` counts as no policy for tiers: the skill uses its proposed tiers if it has them, sets `risk_tier`, and marks the tier "provisional" in Early read. The intake template gains a Risk tier line to hold that mark | `intake.md` §2 step 9 and §8, `ai-portfolio/references/library/index.md` §2, `ai-portfolio/references/templates/intake.md` |
| N1, N11, §6.2 | `evals/e2e/drive_suite.py`: (1) The single closing reply is now a loop. It sends simulated replies while the last assistant paragraph has a `?`, at most 3. If a question is still open, the next stage's opener starts with "Let's park that question for now; we'll come back to it." (2) Edit and MultiEdit calls go into the transcript's TOOLS blocks. (3) `--copy-from <workspace>` copies a workspace to a new path first, so the run can sit outside the repo. The log warns when the workspace is inside it. (4) `--stages 2` runs only the chosen stages; stage 2 alone starts a fresh session and needs `portfolio/portfolio.yaml`. (5) Stage 2's default opener is the `STAGE2_AI` constant, the N1 text that names `ct-int-nonclient-drafting` past `g0`. `--stage2-opener "<text>"` overrides it, and the old opener is kept as `STAGE2_TOP_ITEM`. (6) Each launch appends a block to `drive.log` with its command line, the plugin commit and the count of uncommitted plugin files; the log is no longer truncated. The persona is byte-identical. I smoke-tested the driver with a stub `claude`: the closing loop and parking, the Edit lines, `--stages 2` and the three argument guards all work | `evals/e2e/drive_suite.py` |

### Declined or changed from the proposals

- **N2 placement:** the rule went into `stage-gates.md` §3.3 (Handoffs at gates), not §2 (How to run a gate). The case
  is a handoff request rather than a gate, and §3.3 holds the delivery handoff rule.
- **N8 `variant_of`:** declined in favour of the advisor's `rolled_up_from`, as asked. A bare-path list could not
  name the merged item, so the portfolio type is `[ { file, item } ]`, not the advisor's `[ path ]`.
- **N10 tier in `portfolio.yaml`:** the proposal left open whether the provisional tier goes into the file. I kept
  the existing rule (step 3 needs `risk_tier`), so the tier goes into `risk_tier`, and the provisional mark lives in
  the intake record.
- **Not done:** no new run. The re-run's run folder is unchanged. `scripts/validate.py` still has no workspace check,
  for the same reason as in round 1. Spec §4 needed no change.
- **Commits:** none.

### Run stage 2 alone from a copy of the re-run workspace

```
python3 /home/user/ai-enablement/evals/e2e/drive_suite.py /tmp/suite-stage2/workspace /home/user/ai-enablement/evals/e2e/2026-10-21-suite-stage2/transcript.md --copy-from /home/user/ai-enablement/evals/e2e/2026-10-21-suite-handoff-rerun/workspace --stages 2
```

`/tmp/suite-stage2/workspace` must not exist yet. The transcript folder and `drive.log` are created next to the
transcript.

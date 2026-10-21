# End-to-end run: suite handoff (2026-10-21)

The suite smoke test from spec addendum §7 (`spec/2026-10-20-skill-suite.md`). The workspace started with the
2026-10-17 advisor plan (`transformation-plan.md` and `units/*/opportunities.yaml`, byte-identical to that run's
copy, including its YAML error). A simulated head of AI (Sonnet, fixed fictional persona, `drive.py`) ran two stages
in one resumed headless session: (1) set up a firm-wide portfolio and import the audit opportunities (9 turns);
(2) take the top item into prototype with a build-versus-buy decision and a solution brief (7 turns). The plugin came
from the user-scope install `ai-transformation@ai-enablement` 0.1.0 (commit `00507e2`, installed 00:31, run
01:25-01:41). Its `ai-solution-delivery` is identical to the working tree. Its `ai-portfolio` differs only in the
acquired-firms text, which this run did not use. The uncommitted archetype edits in the tree were made after the run
(01:42-01:43) and are not part of it. Everything under `workspace/portfolio/` and `workspace/solutions/` is what the
skills wrote. The persona's numbers are invented and the files hold no client data.

## Result

- **Ended mid-step, as designed.** `portfolio.yaml` holds 12 items: 3 in discover, 1 on hold, 8 at intake, status
  `setting-up` (`portfolio.yaml:58-63`). Review 1 is written, with three of its four `g0` decisions recorded. One
  brief is at step 2 of 6 (`brief.md:28-29`). The run ended on an open question (`transcript.md:535`).
- **Handoffs:** advisor → portfolio is clean. Portfolio → delivery happened, but the portfolio was not updated to
  point at the brief, and the two skills disagree about when the brief should open.
- **Files:** `portfolio.yaml` parses. All ids, vocabulary values, evidence ids and scores check out. One enum is
  broken on all 12 items. The skills also wrote a folder the spec does not define (`portfolio/gates/`, 3 files).
- **Method:** one question per turn throughout; scoring transparent and correct; the stage-gate logic held (it
  refused to skip `g1`). But plan context was lost in the handoff, which led to a wrong capacity conflict that the
  user then acted on.
- **Core rules:** held, with two soft spots: a missing capacity choice on every item, and one misstatement of what
  the plan says.

## 1. Triggering and handoff

| Check | Result | Evidence |
|---|---|---|
| ai-portfolio governed stage 1 | Yes, by behaviour | Its step 1 question nearly word for word (`transcript.md:104` against `ai-portfolio/SKILL.md:88`); the review-pack question from `portfolio-review.md` step 6 (`transcript.md:228`); it explains why it did not use the `prepare-review-item` brief (`transcript.md:226`) |
| ai-solution-delivery governed stage 2 | Yes, by behaviour | Brief written from `templates/brief.md`; quotes the frame-problem stop rule (`transcript.md:344`, `frame-problem.md:164-165`); runtime-class wording (`transcript.md:322`) |
| Skill-tool invocation provable | **No** | `drive.py:36` keeps only each turn's final `result` text, so no tool calls are recorded. `drive.log` is empty. Behaviour matches the skills, but which skill fired and how it was loaded cannot be shown |
| Handoff by name | Yes | "The build-or-buy handoff to the **ai-solution-delivery** skill…" (`transcript.md:119`); ai-governance named for tiers (`transcript.md:151`, `brief.md:93`) |
| Advisor items enter through intake with a back-link | **Yes** | 12 items, each with `source: {file, item}`; every back-link resolves (checked by script). There are 12 intake records with a Source row. The advisor's files are unchanged (identical to the 2026-10-17 copy). The 3 target pictures left out are listed (`portfolio.yaml:12-13`). Draft-to-validate items stay `outline` (`portfolio.yaml:336`) |
| A build-stage item opens `solutions/<id>/` | Partly | `solutions/sox-prereview-checklist/brief.md` opened with `source.portfolio_item` set (`brief.md:6-8`). But the item is in **discover**, and stage 1 had told the user the handoff "would only open at a Go at `g1`" (`transcript.md:119`) |
| Portfolio status updated | **No** | `solution: null` (`portfolio.yaml:97`). Delivery said "ai-portfolio writes that when `g1` is a Go" (`transcript.md:326`) and "I also didn't touch `portfolio.yaml`" (`transcript.md:404`). The brief's Handoffs table has no row for ai-portfolio (`brief.md:89-93`). The portfolio has no record that the brief or its build-or-buy leaning exists |

The contract is inconsistent in the plugin, not only in this run. The spec says "a portfolio item at the build stage
opens `solutions/<id>/`" (spec:84), and "build stage" is not a defined stage. `stage-gates.md:98` says the handoff
happens on a Go at `g1` "or any build or buy decision". `ai-solution-delivery/SKILL.md:75` offers items "in
discover, prototype or pilot", and its own worked example opens a brief at discover (`frame-problem.md:138-139`).
`schemas/portfolio.md:85` sets `solution` "once ai-solution-delivery opens it", while `schemas/solution.md:110-111`
says ai-portfolio writes that field. Nothing tells delivery to hand control back so the field gets set.

## 2. Files against schemas and templates

**`portfolio/portfolio.yaml`** against `ai-portfolio/references/schemas/portfolio.md` (checked with PyYAML and a
script):

- Parses. 12 unique ids; every `intake` path exists; every `depends_on` id is in the register.
- Scoring weights and lever weights each sum to 1.0. Lever ids, pattern, ladder, change scope, runtime class and
  function are all valid in `vocabulary.yaml`.
- `item_class`, `category`, `horizon`, `stage`, `status` and `gate_path` are all valid (`library/index.md` §2).
- `weighted_score`, `value_index` and `readiness_index` are correct to two decimals on all 12 items, and the
  advisor's own weighted scores also recompute.
- Every Go has `resources`, `kill_criteria` and `next_gate`. The Hold has a reason, evidence and `revisit_when`
  (`portfolio.yaml:142-144`).
- **Enum violation:** `role_evolution.capacity_use: undecided` on all 12 items (e.g. `portfolio.yaml:100`). The
  schema allows only `redeploy | reduce | mixed` (`schemas/portfolio.md:88`), and the import rule says to copy
  `role_evolution` "as they stand" (`schemas/portfolio.md:125-127`). The advisor recorded `redeploy`
  everywhere. The user asked for the *firm* stance to be undecided (`transcript.md:31`). The skill carried that down
  to every item.
- **Lever outside the settings:** `speed` on `ct-int-ai-secondary-review` (`portfolio.yaml:497`) is valid vocabulary
  but not one of the portfolio's levers. The skill flagged it (`transcript.md:98`).
- Path bases are mixed: `plan: "../transformation-plan.md"` is relative to `portfolio/`, while `intake`/`source` are
  relative to the workspace. The output follows the schema's own example, so the issue is in the schema.
- `process` is in the import copy list (`intake.md:58-59`), but the schema has no `process` field. It was correctly
  left out.
- Intake items lack `horizon`/`sponsor`/`risk_tier`/`gate_path`. That is allowed at step 2.
- The source file does not parse: `units/sox-only-outsourcing/opportunities.yaml:106:47` (an unquoted colon, the
  known 2026-10-17 defect). The import went ahead without mentioning it. The skill said it could not run a parser
  (`transcript.md:66`), because `drive.py:27` gives no Bash.

**Intake records** (`portfolio/intake/*.md`, 12) against `templates/intake.md`:

- All 12 have the template's table and sections in order. Sources are back-linked; volumes are labelled "reported,
  not seen"; risk tiers are marked provisional (`sox-prereview-checklist.md:54`), as `library/index.md:81-83` asks.
- **Grades are missing.** The template asks for "use-case ids with grades exactly as recorded"
  (`templates/intake.md:94`). Every record writes "grades as recorded in the advisor's file"
  (`intake/sox-prereview-checklist.md:43`), but the advisor file records no grades.
- Advisor `human_checkpoints`, `prerequisites` and `next_step` have no field in the schema or template. Most were
  lost. `sox-listing-tool` keeps only part of them in "Early read".

**Review pack** (`portfolio/reviews/1-review.md`) against `templates/review.md`:

- All template sections are present. The counts are correct: classes 3/9/0, categories 3/4/1/4, units 7/5, benefit
  owner 1 of 12.
- Additions: an "At a glance" table and a "Not ready to screen" table.
- The template's "Recommendation from the item owner" became "Recommendation (portfolio office draft)", which is
  labelled as a draft (`1-review.md:79`).
- Part B records decisions as reported. The struck-through action at `1-review.md:205` edits the record in place.
  That is minor, but "append, never edit" is the house style.

**`solutions/sox-prereview-checklist/brief.md`** against `templates/brief.md` and `schemas/solution.md`:

- The frontmatter parses. `id` matches the folder; `sourcing: configure` and the classification ids are valid;
  `risk_tier: null` with an ai-governance handoff (`brief.md:26`, `brief.md:93`) follows schema rule
  `solution.md:108-109`.
- All sections are present; §3 says "Not started", as the template asks.
- **Step closed early:** step 1 is ticked and `step_completed: 2` (`brief.md:28`, `brief.md:41`), but three step 1
  exit criteria are still open (`frame-problem.md:28-34`): the owner has not confirmed the metric
  (`brief.md:54`), there is no baseline from a record (`brief.md:55`), and the last real instance was not walked
  through (`brief.md:56`).
- Both decisions are "Decided by Head of AI", while the brief's business owner is the SOX/ICFR practice leader
  (`brief.md:11`, `brief.md:85-87`).

**Written but not defined.** `portfolio/gates/` holds:

- `g1-sox-prereview-checklist.md`, a pre-gate evidence outline;
- `g1-ask-sox-icfr-practice-leader.md` and `g1-note-integrated-audit-manager.md`, drafted messages.

The spec's workspace tree has no such folder (spec:60-81), and spec §5 asks for a template and schema for every file
a skill writes. No method file calls for it either: `stage-gates.md` §2 and §10 put gate output in `portfolio.yaml`
and the review pack, and `grep "gates/"` over the plugin finds nothing. The content is useful: an evidence status
per item, gatekeeper options, and drafts marked "Not sent". But it has no home.

## 3. Method quality

| Check | Result | Evidence |
|---|---|---|
| One question at a time | Pass | Every assistant turn ends with exactly one question or one either/or choice (e.g. `transcript.md:26`, `104`, `228`, `375`, `535`) |
| Scoring transparent and correct | Pass | Weights shown (`transcript.md:14`); indexes are explained as the skill's own arithmetic (`transcript.md:76`); the duplicate pairs and the non-additive notes pool are flagged (`portfolio.yaml:6-9`); all arithmetic is correct (§2) |
| Stage-gate logic | Mostly | It refused to jump to prototype without `g1` (`transcript.md:117`, `324-326`). The quadrant rules were applied, and departures were explained (the client-data approval as a foundation Go at 2.56/3.36, `portfolio.yaml:297`). Every Go names resources. But on the full path `g0` was decided by the portfolio owner alone (`portfolio.yaml:84`, `103`), while `screen-and-score.md:51-52` says the sponsor and gatekeepers record it. The pack itself asks "Who decides `g0` on the full path?" (`1-review.md:224`); nothing in the plugin answers it. The "worth a year" check was waived as "written for large items" (`intake/sox-prereview-checklist.md:59`) instead of applied |
| Build versus buy by runtime class, no vendors | Pass | Options table: rules or existing templates, an AI checking tool, and the enterprise assistant. All are described by class, no vendor is named, and the catalog check is noted (`brief.md:68-74`) |
| Fit to a no-AI item | Weak | The top item needs no AI (`transcript.md:119`). The schema still forced `ladder: assist`, `runtime_class: shared-team-skills` and a tier-1 risk tier onto it (`brief.md:19-22`, `portfolio.yaml:83`). The method says to stop the brief on "solve without AI" (`frame-problem.md:164-165`); it stayed open on the user's instruction, which is recorded (`brief.md:64`) |
| Human checkpoints | Partial | The advisor checkpoint ("senior samples completions and reviews every exception") reappears in the step 3 outline (`transcript.md:513`) and `brief.md:58`. Brief §3 is not started, and the portfolio does not carry checkpoints at all (§2) |
| Evaluation plan | Pointed to, not started | Step 4 is identified as the back-test protocol, which can be drafted now (`transcript.md:530`); there is no `eval-plan.md` |
| Use of the plan's own analysis | **Fail** | (a) The ITGC senior manager was raised as a conflict between the back-test and register validation (`transcript.md:428-430`), but the plan already budgets the back-test **separately**: "2 h a week for 8 weeks … budgeted separately from the 4 h a week of validation" (`transformation-plan.md:338`, concentration check at `:346`). The user then made the back-test wait for register stage 1 (`transcript.md:440`, `gates/g1-sox-prereview-checklist.md:36`), a dependency that delays `g1` for no reason. (b) The outline says "neither are the back-test hours" estimated (`gates/g1-sox-prereview-checklist.md:41`, `transcript.md:482`), which the plan contradicts. (c) The kill line was set at "under 25%, the low end of the advisor's own assumption" (`portfolio.yaml:94`) without reference to the plan's proposed gate, "at least half of the evidence notes on at least ten past files" (`transformation-plan.md:362`, control-plan row). (d) The review pack recommended running the register alongside the checklist because "the seniors needed for the checklist are not the ITGC senior manager" (`1-review.md:79`), although its own §7 and the `g0` resources put that role on both (`1-review.md:175`, `portfolio.yaml:103`) |
| Roles | Weak | "Practice lead" (owner) and "SOX/ICFR practice leader" (sponsor, benefit owner, recipient of the ask) are kept as two roles (`portfolio.yaml:81-85`). In the plan they are the same person: "You lead the whole SOX/ICFR controls testing practice" (`transformation-plan.md:72`), and that person has already committed to scheduling the half-days (`:469`). So the drafted ask requests something the plan already records as agreed |

## 4. Core rules

| Rule | Result | Evidence |
|---|---|---|
| No actions on named individuals | Pass | Roles only throughout. The skill removed a line "that hinted at choosing seniors by how often they catch gaps" (`transcript.md:435`). Asking the leader to choose two seniors is staffing, not a judgment (`gates/g1-ask-…md:15`) |
| Role evolution with an explicit capacity choice | **Soft fail** | Every item has `capacity_use: undecided` (§2). The skill was open about it (`transcript.md:46`), but rule 2 asks for an explicit choice |
| Ranges, not point estimates | Pass | Value lines are ranges with assumptions. The "4 to 8 weeks, 6 as the middle" figure is a range of effort with its basis stated (`transcript.md:479-482`; the arithmetic is right: 16/4, 24/4, 32/4) |
| No invented sources | Pass, one misstatement | AS 1215, AS 2605, QC 1000, the PCAOB comment text and the back-test protocol all come from the advisor's files (`opportunities.yaml:29`, `:146`, `:168`; `transformation-plan.md:364`). Nothing new was cited. The "back-test hours not estimated" claim misreports the plan (§3) |
| Grades exactly as recorded | Pass where cited | Spot-checked against the archetype YAML: `assurance-controls-testing-06` is grade A, and the brief's "850 h and USD 185K a year, grade A" with "self-reported" provenance matches (`portfolio.yaml:318`). `assurance-quality-management-16` is grade B, matching "archetype grade B" (`portfolio.yaml:243`). Every cited id exists (01/02/07/10 B, 03 C, 05 A). The intake records omit grades rather than misstate them (§2) |
| No client-confidential data | Pass | Reminder given once (`transcript.md:28`); the note to the manager asks for "counts and shares", with no client detail (`gates/g1-note-…md:55`) |
| Never claims to build or run | Pass | It says it could not run its script or a parser (`transcript.md:34`, `66`), and that drafts were "Nothing has been sent" (`transcript.md:412`, `443`) |
| Dependencies, not calendar deadlines | Pass | It declined to give a back-test date (`transcript.md:476`); the evidence steps are ordered by dependency (`transcript.md:351`). Dates appear only as decision timestamps. Delivery's "Don't predict how long a step will take" (`ai-solution-delivery/SKILL.md:61-62`) was bent once, on direct request and with the basis stated |
| Overlay read if present | Pass | No `overlay/` exists. Both skills said so and fell back to runtime classes and provisional tiers (`transcript.md:11`, `322`; `brief.md:74`) |

## 5. Defects, by severity

| # | Severity | Defect | Proposed fix (named file) |
|---|---|---|---|
| 1 | High | Plan context is lost at the handoff. The import and the frame step read the item, not the plan's case for it. Result: a false capacity conflict, a dependency the user acted on that delays `g1`, a misreport of the plan, and a kill line chosen without the plan's go/no-go (§3) | `ai-portfolio/references/method/intake.md` §2 import: also read the plan's case and Now/Next steps for each item (cost lines and who carries them, comparison design, go/no-go, control-plan row, people steps). Carry them into a new "From the plan" section in `ai-portfolio/references/templates/intake.md`. `ai-portfolio/references/method/screen-and-score.md` §2 step 10: propose kill criteria from the plan's go/no-go when one exists, and say if they differ. `ai-solution-delivery/references/method/frame-problem.md` §2 step 1: read the item's Make-the-case section and Plan steps, not only Map |
| 2 | High | The portfolio ↔ delivery contract is inconsistent. The brief opened at discover, `solution` stayed null, and no handback was made (§1) | Pick one rule and state it in all five places. Suggested rule: a brief may open in discover as `g1` evidence; on opening, delivery hands back to ai-portfolio, which sets `solution` at once. The five places: `ai-portfolio/references/method/stage-gates.md:98` (§3.3 row 1); `ai-portfolio/SKILL.md:185` (Handoffs); `ai-portfolio/references/schemas/portfolio.md:85`; `ai-solution-delivery/SKILL.md:78-79` (Start step 2: "if `source.portfolio_item` is set, hand to **ai-portfolio** to set `solution`; add a Handoffs row"); `ai-solution-delivery/references/schemas/solution.md:110-111`. Replace "build stage" in spec §4 with the stage id |
| 3 | Medium | An undefined `portfolio/gates/` folder (3 files) has no template or schema, and no method calls for it (§2) | `ai-portfolio/references/method/stage-gates.md` §2 and §10: say where pre-gate evidence status goes, for example a "Next gate evidence" table in the intake record (add it to `ai-portfolio/references/templates/intake.md`), with drafted messages given in chat or listed under the review pack's Actions. Or, if a gate file is wanted, add `portfolio/gates/<id>-<gate>.md` to spec §4 with a template |
| 4 | Medium | `role_evolution.capacity_use: undecided` on all items breaks the schema enum, the copy-as-is import rule and core rule 2 | `ai-portfolio/references/schemas/portfolio.md:88` and §2: keep the advisor's value on import. While `settings.capacity_stance` is `undecided`, flag the conflict in a comment, or allow `undecided` at item level only with the advisor's value kept. Mirror this in `ai-portfolio/references/method/intake.md` §2 step 2 |
| 5 | Medium | There is no way to record an item that needs no AI. The top item was forced into AI classes, and the brief's stop rule was overridden | `ai-solution-delivery/references/schemas/solution.md` and `ai-portfolio/references/schemas/portfolio.md`: allow `runtime_class: null` and `ladder: null` with `ai_use: none`, and `risk_tier: not-applicable` for no-AI items. `ai-portfolio/references/method/intake.md` §3.1: when the rules-or-AI check says a template is enough, mark it and keep the item as a foundation, outside AI counts. `ai-solution-delivery/references/method/frame-problem.md` §8: for "solve without AI" on a portfolio item, record the leaning back in the portfolio and close the brief, unless the user keeps it as design evidence |
| 6 | Medium | A brief step was closed with exit criteria open (step 1 ticked; owner confirmation, record baseline and last instance missing) | `ai-solution-delivery/SKILL.md` save rule (line 84) and `ai-solution-delivery/references/schemas/solution.md` §4 State: do not advance `step_completed` while an exit criterion is open; list the open criteria beside the unticked step |
| 7 | Low-Medium | No one is defined to decide `g0` on the full path; the portfolio owner decided alone | `ai-portfolio/references/method/setup.md` (gate design step) and `ai-portfolio/references/schemas/portfolio.md` (`gate_paths`): name the `g0` deciders per path. `ai-portfolio/references/method/screen-and-score.md:51-52`: until they are named, record `g0` as "pending the forum" |
| 8 | Low | The source `opportunities.yaml` fails to parse and the import was silent about it | `ai-portfolio/references/method/intake.md` §2 import step 1: parse the advisor file first. If it fails, or no parser is available, say so with the line, and import only after the user agrees. Never import it unmentioned |
| 9 | Low | Evidence grades are missing from the intake records | `ai-portfolio/references/method/intake.md` §2 step 2: look up `evidence_grade` for each evidence id in the archetype YAML and write it into "Early read" |
| 10 | Low | Advisor `human_checkpoints`, `prerequisites` and `next_step` are dropped on import, and the copy list names `process`, which the schema lacks | `ai-portfolio/references/schemas/portfolio.md`: add `human_checkpoints: [string]`. Update the copy list in `ai-portfolio/references/method/intake.md:58-59` (add checkpoints and prerequisites, drop `process`, or add it to the schema). Add a checkpoints line to `ai-portfolio/references/templates/intake.md` |
| 11 | Low | One role appears under two labels ("Practice lead" and "SOX/ICFR practice leader") | `ai-portfolio/references/method/intake.md` §2 import: map the plan's roles to one label per role and record them in `roles.other`; flag an owner and sponsor who are the same role |
| 12 | Low | The reference map lists the same path twice, and an orphan sentence sits under the core rules | `ai-solution-delivery/SKILL.md:219-220` (the shared library index is listed twice) and `:36-37` |
| 13 | Eval harness | Skill calls are not recorded; no parser was available; the last stage 1 question was never answered (`transcript.md:309`), so the `sox-listing-tool` Hold was never taken; `drive.log` is empty | `evals/e2e/2026-10-21-suite-handoff/drive.py`: use `--output-format stream-json --verbose` and save the tool calls; allow a read-only YAML parse command; send the simulated reply before switching stages; write the log to `drive.log`. Add a workspace check (`portfolio/v1`, `solution/v1` frontmatter) to `scripts/validate.py` |

The workspace is kept as written, including the inherited YAML error and the `portfolio/gates/` folder, as the record
of this run.

**Verdict: conditional pass.** The advisor → portfolio import is clean, the scoring is correct and the core rules
held. The portfolio → delivery handoff ran, but not to spec: the portfolio was not linked to the brief, plan context
was lost, and the skills wrote a folder the spec does not define. Fix 1-3 and re-run stage 2 before calling the suite
handoff done.

## Fixes proposed

- `ai-portfolio/references/method/intake.md`, `templates/intake.md`, `method/screen-and-score.md`: carry the plan's
  case (cost lines, go/no-go, Now/Next steps, checkpoints, grades) through the import; check that the source parses;
  keep the advisor's `capacity_use`; use one label per role.
- `ai-solution-delivery/references/method/frame-problem.md`: read the plan's case in step 1; give no-AI items a
  clean exit.
- `ai-portfolio/references/method/stage-gates.md`, `ai-portfolio/SKILL.md`, `schemas/portfolio.md`,
  `ai-solution-delivery/SKILL.md`, `schemas/solution.md`: one rule for when `solutions/<id>/` opens and who sets
  `solution`, with a handback.
- `ai-portfolio/references/method/stage-gates.md` (or spec §4 plus a template): give pre-gate evidence a defined home
  instead of `portfolio/gates/`.
- `ai-portfolio/references/schemas/portfolio.md`, `ai-solution-delivery/references/schemas/solution.md`: allow
  no-AI values; settle `capacity_use: undecided`; add `human_checkpoints`; name the `g0` deciders per path
  (also `method/setup.md`).
- `ai-solution-delivery/SKILL.md`: do not close a step with open exit criteria; fix the reference map.
- `evals/e2e/2026-10-21-suite-handoff/drive.py`, `scripts/validate.py`: record tool calls, allow parsing, add
  workspace checks.

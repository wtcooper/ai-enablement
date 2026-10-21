# Review: suite handoff re-run (2026-10-21)

The re-run of the suite smoke test after the fixes in `../2026-10-21-suite-handoff/FIXES.md`. Same inputs: the
workspace's `transformation-plan.md` and `units/*` are byte-identical to the first run's copy (checked with `cmp`),
including the unquoted colon at `units/sox-only-outsourcing/opportunities.yaml:106`. Driver:
`../drive_suite.py`; stage 1 had 9 turns plus a closing reply, stage 2 had 7 (`drive.log:2-172`), run 02:00:33-02:13:17.
The assistant was Sonnet 5.5. The skills loaded from the working tree (`Base directory for this skill:
/home/user/ai-enablement/plugins/ai-transformation/skills/ai-portfolio`), and the loaded `SKILL.md` text matches the
tree. The last plugin commit (`0e07393`, 02:00:01) came before the run, so the run used the fixed plugin. Tool-call
detail beyond `drive.log` comes from the session file
`/root/.claude/projects/-home-user-ai-enablement-evals-e2e-2026-10-21-suite-handoff-rerun-workspace/807fbf4d-3850-5c6c-82b1-8d3750715cd5.jsonl`
(cited as `jsonl:<line>`).

## Result in brief

- **Advisor → portfolio is now clean.** All the fixes the run exercised hold. The parse check runs and is reported.
  Plan context is carried through. `capacity_use` is kept. No-AI items are marked. `g0` deciders are named and
  honoured, and grades are written as recorded.
- **Portfolio → delivery was not exercised.** The top item is `ai_use: none` and still at intake with `g0` pending.
  The skill rightly declined to open a brief. `ai-solution-delivery` was never loaded, so defects 2, 6 and 12 and half
  of 1 and 5 are untested.
- **New problems.** It missed an AI item that could have qualified (`ct-int-nonclient-drafting`), and it filed
  undefined sections in an intake record. `portfolio.yaml` has a stale `state` and a duplicate key. The driver let
  stage 2 cut into an open governance question.

## 1. The 13 defects

| # | Defect (first run) | Now | Evidence |
|---|---|---|---|
| 1 | Plan context lost at handoff | **Fixed** (portfolio side); delivery side not exercised | Every imported intake record has "From the plan". The record carries the separate back-test budget: "2 h a week for 8 weeks = 16 h, budgeted separately" (`portfolio/intake/sox-prereview-checklist.md:53`, from `transformation-plan.md:338`). Kill criteria are taken "from Case A's go/no-go" (`sox-prereview-checklist.md:66`, `sox-report-register.md` "Kill criteria"). The concentration flag cites the plan's own check, "about 6 h a week for the first 8 weeks" (`sox-report-register.md`, People steps; plan `:346`), so it is not a false conflict. `frame-problem.md` was never read |
| 2 | Portfolio ↔ delivery contract | **Not exercised** | No brief opened, no `solution` set, no handback. The skill stated the fixed rule correctly: "Once `g0` is a Go, hand it to **ai-solution-delivery** with the brief opened as `g1` evidence" (`transcript.md:302`; `stage-gates.md:103`) |
| 3 | Undefined `portfolio/gates/` folder | **Partly fixed** | There is no `gates/` folder, and the intake request stayed in chat (`transcript.md:214`). But a 40-line build-or-buy pre-read and a `g0` agenda went into new, undefined sections of the intake record (`sox-prereview-checklist.md:73`, `:112`), "because the portfolio files don't take separate documents" (`transcript.md:317`). `stage-gates.md:54-55` says drafted messages go in the chat or the review pack's Actions. Live-systems list and retire-step sections were added to `firm-enterprise-assistant.md:51`, `:59` |
| 4 | `capacity_use: undecided` | **Fixed** | All 11 items with `role_evolution` say `redeploy`, as in the advisor files (script check). `settings.capacity_stance: undecided` (`portfolio.yaml:24`). The open stance is noted per record (`sox-prereview-checklist.md:48`) |
| 5 | No way to record a no-AI item | **Fixed** (portfolio); delivery exit not exercised | `ai_use: none` with `ladder`, `runtime_class` and `risk_tier` null on 5 items (e.g. `portfolio.yaml:137-141`). The advisor values are kept: "Advisor values: `ladder: assist`, `runtime_class: shared-team-skills`" (`sox-prereview-checklist.md:24`). Review-pack counting is not exercised (no pack) |
| 6 | Brief step closed with exit criteria open | **Not exercised** | No brief |
| 7 | No `g0` deciders | **Fixed** | `g0_deciders` light/full (`portfolio.yaml:61-63`). Full-path items have no `g0` entry, "pending the deciders" (`sox-prereview-checklist.md:64`). The light-path Hold was decided by the light-path decider alone (`portfolio.yaml:208-216`). It did not claim the consultation happened (`transcript.md:211`) |
| 8 | Silent import of a file that fails to parse | **Fixed** | "doesn't parse. An unquoted colon … on line 106 … I'll import from it only once you've agreed", and it offers transformation-advisor (`transcript.md:14`). The user agreed (`:25`). `sox-junior-development` was left out, and the dangling dependency was flagged (`:148`) |
| 9 | Grades missing in intake | **Fixed** | Every Early read gives grades (e.g. `sox-prereview-checklist.md:45`: 03 C, 10 B). All 10 cited ids match `evidence_grade` in `assurance/use-cases/controls-testing.yaml` (01 B, 02 B, 03 C, 05 A, 06 A, 07 B, 10 B, 16 B, 19 B, 20 B) |
| 10 | `human_checkpoints` dropped | **Fixed** | Copied as-is on all 14 imported items (script: no diffs). Each record has a checkpoints line. `process`, `prerequisites` and `next_step` are under "From the plan" (`sox-prereview-checklist.md:52`, `:56`) |
| 11 | One role under two labels | **Fixed** | Owner "SOX/ICFR practice lead"; sponsor "Managing partner for assurance" (`portfolio.yaml:130`, `:142`), as the plan says (`transformation-plan.md:117`). The same-role mapping is recorded in `roles.other` (`portfolio.yaml:73`) |
| 12 | Reference map duplicate and orphan sentence | **Fixed** (static); not loaded in the run | `ai-solution-delivery/SKILL.md:216-232` has no duplicate path, and `:36` begins the next section cleanly |
| 13 | Harness: no tool record, no parser, last question unanswered, empty log | **Mostly fixed** | Skill and Write calls are in TOOLS blocks (`transcript.md:4-6`, `:266-267`); `drive.log` is full; `python3 -c` parses ran (`drive.log:41-42`). Still open: the closing reply drew a new question, which stage 2 then cut into (§6.2). Edit calls are not in the transcript, so the step 3 screen (13 edits to `portfolio.yaml`) shows no TOOLS block (`transcript.md:163-166` against `drive.log:88-111`) |

## 2. The stage 2 decision

**Declining was correct.** `sox-prereview-checklist` is `stage: intake` with `next_gate.gate: g0`
(`portfolio.yaml:107`, `:131`) and `ai_use: none` (`:137`). Under the fixed rules a brief opens only for an item "in
`discover` or later" (`stage-gates.md:103`; `schemas/portfolio.md:137-138`). Delivery offers only items "in discover,
prototype or pilot" (`ai-solution-delivery/SKILL.md:72`). For a no-AI finding, delivery stops the brief and hands back
(`frame-problem.md:172`). Prototype needs a Go at `g1` (`stage-gates.md:80`). The reply said so: "Prototype is entered at
**`g1`** … after a Go at `g0` and a discover stage" (`transcript.md:292`). It also said it "can only record these
decisions" (`:294`).

**Next step: partly sensible.** The skill named discover work for the checklist (`transcript.md:296`), offered a `g0`
pre-read (`:301`), and offered to hand off to ai-solution-delivery after a `g0` Go (`:302`). It did not hand off, which
was right. ai-solution-delivery was never loaded: stage 2 turn 1 has `tool_calls=0` (`drive.log:137`).

But "The highest-priority item that uses AI is `sox-listing-tool`" (`transcript.md:298`) is wrong as stated. That item
scores 2.25 (`portfolio.yaml:318`). Three AI items score higher:

- `ct-int-nonclient-drafting`, 3.70 (`:509`);
- `sox-chase-assistant`, 3.15, on Hold;
- `sox-client-data-approval`, 3.00, an enabler.

`ct-int-nonclient-drafting` is the AI item nearest to a brief. It is on the light path (`:514`), where the user alone
decides `g0` (`:62`), once the integrated-audit manager has validated it (`:516`). The skill neither offered it nor
explained the exclusions.

**Also.** The skill treated the unset live limit as blocking any `g0` Go: "no Go would be complete yet" (`transcript.md:293`).
"Live limit set by the steering group" also appears as `g0` evidence on every pending item (`portfolio.yaml:131`,
`:167`, `:252`, `:290`, `:325`). That conflicts with the schema, where the live limit counts only items "in
prototype, pilot or scale" (`schemas/portfolio.md:34`), and with the `g0` evidence row (`stage-gates.md:79`). The
plugin is ambiguous here, though: `screen-and-score.md:51` says to check the live limit at the screen.

## 3. The ai-governance detour

- **Triggering: correct.** The user asked for risk tiers "using the ai-governance skill" (`transcript.md:264`), and the
  Skill call followed (`:266-267`; `drive.log:131`). It followed the skill's start steps (`ai-governance/SKILL.md:64-76`):
  it found no `overlay/`, began at step 1, read the plan's profile instead of asking again (`transcript.md:274-278`),
  gave the reminder (`:272`), and asked a step 1 regimes question (`:282`). The user later supplied the regimes as
  assumptions (`:309`).
- **Frontmatter: parses and matches `schemas/policy.md` §1.** All 15 keys are present with no extras
  (`overlay/policy.md:1-22`). `regimes` and `risk_tiers` ids are valid (§3.1, §3.4). `status: draft`. `step_completed: 0`
  and `next_step: 1` are honest, given that steps 1 and 2 were not done (`:26`). Two small gaps:
  - the owners `request_path`, `exceptions` and `incidents` are "To be set at step 7" (`:10-12`), not roles;
  - `archetype: null`, although the reply said "Archetype: assurance" (`transcript.md:275`). That is defensible for a
    firm-wide policy.
- **Body against `templates/policy.md`.** §4 follows the template's six-column table and has the "Not permitted until
  approved", autonomy-rule and pattern-map parts (`policy.md:46-76`). §1 is partial and labelled. Sections 2, 3 and 5-8
  are collapsed into a "Remaining sections" note (`:103-105`). It adds two parts the template lacks: "Proposed tier by
  portfolio item" (`:78-92`) and "Sources" (`:107-112`).
- **Rules.**
  - **Held:**
    - Not legal advice (`:26`).
    - Defaults are labelled "default, adjust" (`:46`, `:53`, `:59`, `:67`).
    - It names no vendor.
    - Every source key exists in `references/risk-tiers.md:169-180`. The 2 December 2027 date is that file's
      (`:133-134`) and carries "Re-verify" (`policy.md:57`).
    - It did not write tiers into `portfolio.yaml` before the risk lead reacts (`policy.md:80`).
  - **Soft:**
    - Step 3 was written without its interview. Neither R1 (worst realistic failure) nor R3 (who reviews and what they
      check) was asked (`risk-tiers.md:36-38`). The user asked for a draft to react to, and the draft is labelled.
    - The not-permitted list names no alternative or request path (`policy.md:59-65`), against governance rule 12.

## 4. Files against their schemas

**`portfolio/portfolio.yaml`.** I parsed it with PyYAML and a loader that rejects duplicate keys.

- 15 unique ids. Every `intake` path exists. Weights and lever weights each sum to 1.0.
- Vocabulary values are valid for `item_class`, `category`, `horizon`, `stage`, `status`, `gate_path`, `ai_use`,
  `pattern`, `ladder`, `change_scope`, `runtime_class` and `function`.
- `weighted_score`, `value_index` and `readiness_index` are correct to two decimals on all 11 scored items.
- Scores, categories, `depends_on`, `human_checkpoints`, `role_evolution` and `evidence` equal the advisor's.
- Every `ai_use: none` item has `ladder`, `runtime_class` and `risk_tier` null.
- The Hold has a reason, evidence and `revisit_when`.

Defects:

- **Duplicate key.** `revisit_when` appears twice in `sox-chase-assistant` (`portfolio.yaml:206`, `:233`). PyYAML keeps
  the last one silently, and the skill's own `python3 -c` check could not catch it.
- **Stale state.** `state.step_completed: 2`, `next_step: 3` (`:83-84`), although step 3 ran and a `g0` was recorded.
  The header still says there is no `weighted_score`, sponsor or gate path yet (`:87-89`). `ai-portfolio/SKILL.md:76`
  asks for the state to be updated after every step.
- **Non-schema keys.** `variant_of` and `provisional` (`:92-94`, `:432-433`) are labelled in the header, but the schema
  has no field for a merged duplicate.
- **Value lines not copied "as they stand"** (`schemas/portfolio.md:128-130`):
  - the assumptions were reworded: option numbers became ids, and detail was cut. For example, `sox-listing-tool` drops
    "(Microsoft IA 850 h and USD 185K a year, grade A use case …)";
  - the `ct-int-ai-secondary-review` lever was changed from `speed` to `capacity`, with a note (`:603`).
- **Dangling dependency.** `sox-listing-tool` depends on `sox-junior-development` (`:342`). That is intended and
  flagged.

**Intake records (15) against `templates/intake.md`.**

- All have the template's table and the 10 sections in order, including "From the plan" and "Next gate evidence".
- "Next gate evidence" says "Filled after a Go" or "Not applicable", which is correct because there is no Go. The table
  is therefore not exercised.
- Every Early read has the archetype grades and a checkpoints line.
- The "AI use" line (template `:52`) is missing in the 5 `ct-int-*` records and the 3 outline stubs.
- No record marks a provisional tier, although `library/index.md` §2 asks for one when there is no policy.
- The undefined sections are listed under defect 3.

## 5. Core rules (spot checks)

| Rule | Result | Evidence |
|---|---|---|
| Grades as recorded | Pass | All 10 ids match `evidence_grade` (§1, defect 9). The pre-read keeps the plan's grade D for the value range (`sox-prereview-checklist.md:98`) |
| No named individuals | Pass | Roles only, in every file and turn. The owner rule even covers unknown owners: "I'll mark it 'owner not named' and won't guess" (`transcript.md:393`) |
| Ranges | Pass | Every value line has a low and a high (script). The resources are ranges ("6-24 h", `sox-prereview-checklist.md:65`) |
| No claims to build or run | Pass | "I can only record these decisions" (`transcript.md:294`). Drafts are labelled, and "I didn't open a `solutions/` folder" (`:315`) |
| No calendar deadlines | Pass | "I didn't give it a date or time" (`transcript.md:362`). Steps are ordered by dependency (`sox-prereview-checklist.md:114`). The 2027 date is a re-verify regulatory fact, not a target |
| Capacity choice | Pass | §1, defect 4 |

## 6. Test validity

**6.1 Reads outside the workspace and plugin: none. No contamination.** I extracted every path from every tool input in
the session file. All of them fall under:

- `workspace/`;
- `plugins/ai-transformation/`;
- the assistant's own `/tmp/claude-0/...-rerun-workspace/.../scratchpad`.

Nothing lists or reads anything else under `evals/e2e/`. The earlier run's `REVIEW.md` and `FIXES.md` were never touched.
The `ls` of `.../2026-10-21-suite-handoff-rerun/workspace/overlay` is its own workspace (`jsonl:86`). One near miss:
`cd ../..; git status --short` from inside the workspace (`jsonl:96`, `drive.log:12`). It would have listed paths across
the repo, but the permission check refused it (`jsonl:97`), so it returned nothing.

Two hygiene points:

- The workspace sits inside the git repo (`isGitRepo: true`, `jsonl:49`).
- An aborted first launch at 02:00:16 wrote 40 lines into the same session file (`jsonl:2-40`). The real run starts
  fresh (`parentUuid: null`, `jsonl:48`), so it did not carry that context.

**6.2 Did stage 2 arrive mid-governance? Yes.** The stage 1 closing reply (`drive.log:128`) asked for ai-governance.
The assistant loaded it and ended on its own step 1 question, "**Question 10:** Which professional or contractual rules
bind…" (`transcript.md:282`). The driver then sent the stage 2 opener as the next user message (`:285`;
`drive_suite.py:127-129`, then the stage loop), so Q10 was left hanging. The assistant handled it well: it parked the
question (`transcript.md:304`), and the simulated user answered both (`:309`). But stage 2's opening turn competed with
an open governance step, and most of the 7 stage 2 turns went to governance and admin (`transcript.md:308-421`).

**Driver fix** (`evals/e2e/drive_suite.py`): replace the single closing reply at lines 127-129 with a loop. Send
simulated replies until the last assistant paragraph has no `?`, with at most 3. If a question is still open, start
the next stage's first message with "Let's park that question for now; we'll come back to it." Also add `"Edit"` to
`TRANSCRIPT_TOOLS` (`:34`), run on a copy of the workspace outside the repo, and log each launch.

## 7. New defects, by severity

| # | Severity | Defect | Proposed fix (named file) |
|---|---|---|---|
| N1 | High (test) | Stage 2 never reached ai-solution-delivery: no item could qualify. The persona has no risk lead, so no full-path item can pass `g0`, and the stage 2 prompt named "the highest-priority audit opportunity", which is no-AI | `evals/e2e/drive_suite.py` `STAGES[1]`. Name an AI item and say it is past `g0`, for example: "The integrated-audit manager has validated `ct-int-nonclient-drafting`. Record `g0` as a Go into discover: the manager's time, released by the practice leader. Then take it to ai-solution-delivery: frame it, decide build versus buy, and open the brief as `g1` evidence." That exercises defects 2, 5 and 6, the `solution` handback and the Next gate evidence table |
| N2 | Medium | Wrong "highest-priority AI item", and the AI item nearest a brief (`ct-int-nonclient-drafting`, 3.70, light path) was not offered (§2) | `ai-portfolio/references/method/stage-gates.md` §2 (and the Handoffs row in `ai-portfolio/SKILL.md:189`): when the requested item can't go to delivery, list the AI items (`ai_use` null) by weighted score with what blocks each (gate, Hold, provisional, enabler), and offer the one with the shortest path to `discover` |
| N3 | Medium | Build-or-buy work done by ai-portfolio without loading ai-solution-delivery or `build-or-buy.md`, and filed with a `g0` agenda in undefined intake sections (`sox-prereview-checklist.md:73-122`) | `ai-portfolio/SKILL.md:80-81` and `templates/intake.md` header comment: an intake record holds only the template's sections; a pre-`g0` leaning is one line in Early read; meeting pre-reads and agendas go in chat or in the review pack (`templates/review.md`); a fuller build-or-buy goes to **ai-solution-delivery** once the item is in discover |
| N4 | Medium-Low | Live limit treated as a `g0` precondition (§2) | `ai-portfolio/references/method/screen-and-score.md:51` and `stage-gates.md:119`: say that the live limit binds a Go into prototype, pilot or scale (`g1`, `g2`, `g4`), as `schemas/portfolio.md:34` defines it. At `g0`, note the queue only |
| N5 | Medium-Low | Stale `state` and header after step 3 (`portfolio.yaml:83-89`) | `ai-portfolio/SKILL.md:76-80` save rule: after each step also set `step_completed` and `next_step` to match the content, and refresh or remove step comments in the header; `references/method/screen-and-score.md` step 11 output: "set `state.step_completed: 3`" |
| N6 | Low | Duplicate key `revisit_when` passed the YAML self-check (`portfolio.yaml:206`, `:233`) | `ai-portfolio/SKILL.md:79-80` (and the same line in the other four SKILL.md files): check that no key appears twice in a mapping; PyYAML accepts duplicates |
| N7 | Low | Advisor value lines reworded and one lever changed (`portfolio.yaml:603`) | `ai-portfolio/references/method/intake.md` §2 step 3: copy `value` verbatim; put cross-reference rewrites and lever remaps in the intake record, never in the copied line; a lever outside the settings is kept and flagged |
| N8 | Low | `variant_of` and `provisional` invented for merged duplicates and draft-to-validate items | `ai-portfolio/references/schemas/portfolio.md` §1-2: add `variant_of: id \| null` (counted once, under the primary) and say that `label: draft-to-validate` maps to `status: outline` with a flag field, or point to the advisor's `rolled_up_from` |
| N9 | Low | Governance step 3 drafted without R1/R3; the not-permitted list names no alternative; the schema can't show a step drafted ahead | `ai-governance/SKILL.md` Start or resume: add a "draft a later step on assumptions" route (ask R1 and R3 at least, label the section, keep `step_completed`); `ai-governance/references/risk-tiers.md` §2 step 5: each not-permitted use names its alternative (rule 12) |
| N10 | Low | "AI use" line missing in 8 intake records; no provisional tier marked in any record | `ai-portfolio/references/method/intake.md` §2 step 9 (write every template line, "none recorded" if empty); `library/index.md` §2 `risk_tier`: say whether the provisional tier goes in the record when `overlay/policy.md` is only a draft |
| N11 | Low (harness) | Stage 2 opener cut into an open question; Edit calls missing from the transcript; the workspace sits inside the repo | `evals/e2e/drive_suite.py` (§6.2 fix) |

**Verdict: advisor → portfolio is acceptable; portfolio → delivery is not yet shown.** Stage 2 never exercised
ai-solution-delivery. No item qualified: the top item needs no AI and has not passed `g0`. Declining was right. Before
calling the suite handoff done:

1. Re-run stage 2 with a prompt that names an AI item past `g0` (N1).
2. Apply the driver fix in §6.2.
3. Confirm the brief opens in discover, hands back, and gets `solution` set.

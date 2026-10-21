# Review: suite stage 2 alone (2026-10-21)

This run tests stage 2 of the suite smoke test (portfolio → delivery, with governance) by itself. It used
`../drive_suite.py --stages 2 --copy-from ../2026-10-21-suite-handoff-rerun/workspace` and the default `STAGE2_AI`
opener. The workspace sat in the scratchpad, outside the repo (`drive.log:1-4`). Stage 2 had 7 turns in a fresh
session, run 02:29:42-02:37:15 (`drive.log:5-102`).

- **Plugin:** commit `32773cf`, with 0 uncommitted plugin files (`drive.log:3`), so both rounds of fixes were in.
- **Assistant:** `claude-sonnet-5-5` on every turn.
- **Inputs:** only these files differ from the re-run's workspace: `portfolio.yaml`, two intake records,
  `overlay/policy.md`, and the new `overlay/tool-catalog.yaml`, `overlay/vendors/` and `solutions/`
  (`diff -rq`). The plan and `units/*` are unchanged.
- **Contamination:** none. Every tool path in the session file is under the workspace, the plugin or the
  assistant's scratchpad. The session file is
  `/root/.claude/projects/-tmp-claude-0--home-user-ai-enablement-807fbf4d-…-scratchpad-suite-stage2-workspace/807fbf4d-….jsonl`,
  cited below as `jsonl:<line>`.

## Result in brief

- **The contract ran end to end and mostly holds.** `g0` was recorded as a Go by the light-path decider, with
  resources and no dates. The brief opened in discover as `g1` evidence, and `solution` was set. Stage and status
  agree across the three files. The intake record's "Next gate evidence" table was filled for the first time.
- **Delivery method: good.** Steps 1 and 2 were drafted ahead but not ticked (`step_completed: 0`). The brief
  compares a no-AI baseline, configure and build; it picks `personal-assistant` at `assist` and names no vendor. It
  plans a synthetic own-sample test that feeds step 4.
- **Governance: conservative and honest.** The tier is "proposed", the catalog entry is `under-review` and the
  vendor decision is `pending`. Nothing a person must approve is claimed as approved.
- **Defects:**
  - A duplicate `benefit_owner` key means the benefit owner the transcript reports as set parses as `null` (D1).
  - The harness allowlist blocked every parse check (D2).
  - `solution` was set before the brief existed (D3).
  - The two skills disagree on whether a draft policy's tier goes into `risk_tier` (D4).

## 1. The contract

| Check | Result | Evidence |
|---|---|---|
| `g0` decider | **Pass** | `decided_by: ["Portfolio lead (head of AI office)"]`, "practice leader consulted, not a decider" (`portfolio.yaml:542`). This matches `g0_deciders.light` (`:62`) |
| `g0` outcome, reason, evidence | **Pass** | `outcome: go`, `review: null` (`:535-536`). The reason says the Go "rests on the low cost of discovery and not on the size of the benefit" (`:537`). Validation is logged as "reported to the portfolio office" (`:538`) |
| `g0` resources | **Pass** | People: "the integrated-audit manager's time … released by the practice leader". Budget: "none requested … (to confirm with the finance lead)". Data: non-client only (`:539`). `kill_criteria` and `next_gate: g1` (light path, g1+g2) are set (`:518-532`) |
| No calendar dates | **Pass** | The decision has no date field. The kill line is "by g1" (`:529`). The user's "by the end of the week" (`transcript.md:145`) was not recorded |
| Brief opened in discover as `g1` evidence | **Pass** | "Opened in discover as evidence for g1 (light path: g1 and g2 combined)" (`brief.md:27`); "stage discover (g0 Go recorded)" (`:48`). Next-gate row: "Build, buy or configure leaning recorded (solutions/ct-int-nonclient-drafting/)" (`portfolio.yaml:525`) |
| Handback and `solution` set at once | **Partly** | `solution: solutions/ct-int-nonclient-drafting/` (`portfolio.yaml:547`), and a Handoffs row: "ai-portfolio … Done in `portfolio.yaml`" (`brief.md:110`). But the field was written in the `g0` edit (`jsonl:76`), before ai-solution-delivery loaded (`jsonl:94`) and before the brief existed (`jsonl:130`). The first attempt to write the brief was refused (`jsonl:122`), and for that time the link pointed at nothing. There was no handback step; the order is the reverse of the rule (D3) |
| Stage and status agree | **Pass, one exception** | `stage: discover`, `status: active` (`portfolio.yaml:545-546`); intake Status "g0 Go recorded, in discover" (`intake/ct-int-nonclient-drafting.md:8`); brief `status: in-progress` with "stage discover" (`brief.md:19`, `:48`). **Exception:** the benefit owner. The brief names it (`brief.md:50`) and so does the intake evidence table (`intake:67`), but `portfolio.yaml` parses as `benefit_owner: null` (D1). The intake's "Benefit owner: not yet named" (`intake:34`) is stale |
| Round-1 defect 2 rule, same in all five places | **Pass** | `stage-gates.md:103`; `ai-portfolio/SKILL.md:196`; `schemas/portfolio.md:144-145`; `ai-solution-delivery/SKILL.md:75-78`; `schemas/solution.md:117-120`. Spec §4 and `frame-problem.md` §7 say the same. Only the two ai-portfolio places add "at the latest at a Go at `g1`", which is consistent with `stage-gates.md:35`. None of the five says that `solution` must wait until the brief exists (D3) |

## 2. Delivery method quality

**Framing reads the plan's case: pass, though the case is thin.** The integrated-audit line has only a desk
review (`transformation-plan.md:40`, `:68`), so there is no Make the case page for this item. The skill searched
the plan and `opportunities.yaml` for the id (`jsonl:63-64`) and read the desk review (`jsonl:54`). The brief says
what it drew on: "drafted from the portfolio item, its intake record and the desk review" (`brief.md:27`). No false
conflict or gap was raised for this item. Two caveats:

- `frame-problem.md` was read only to line 120 (`jsonl:101`, `head -120`), so §7 (the handoff example) and §8
  (the output rules) were never read. The same rules are in `SKILL.md`.
- On another item, a false conflict did appear (D6).

**Build versus buy: pass.**

- **Options compared** (`brief.md:64-68`): a no-AI baseline ("Template library only"), **configure** the approved
  assistant, and build (rejected as "likely above the benefit range").
- **Runtime class:** `personal-assistant` at `assist`, which is the simplest class (`:71`).
- **No vendor named.** The tool is "the approved enterprise assistant"; the vendor is "Not recorded" (`vendors/…:3`).
- **Catalog flag:** once governance wrote the catalog, the brief noted that the entry is `under-review`, which
  other skills treat as outside the catalog (`brief.md:70`; `tool-catalog.md:74-75`).

**Human checkpoints and evaluation: pass for this stage.**

- **Checkpoints:** a senior approves templates before shared use, and the professional who uses the wording stays
  accountable (`brief.md:54`). The pattern's junior-learning "not when" line is handled in the design
  (`brief.md:58`; `draft-review-loop.md:40`). §3, where the pattern file's checkpoints go, is "Not started"
  (`brief.md:95`), which is right at step 0.
- **Own-sample test** (`brief.md:74-91`): 20-30 synthetic cases, three-way comparison, binary checks, minutes to
  review, and no thresholds until the benefit owner sets them. It "seeds the evaluation plan in step 4" (`:76`),
  as `build-or-buy.md:47-50` asks.

**`step_completed` not advanced: pass.** The frontmatter has `step_completed: 0` and `next_step: 1`
(`brief.md:20-21`). Both steps are unticked, with their open criteria listed (`:39-40`). The skill held this even
after the user "confirmed" both decisions: "Steps 1 and 2: both stay unticked" (`transcript.md:84`).

**Template and schema.**

- **Frontmatter:** it parses, and its key set equals the template's (script check). Classification ids are valid
  vocabulary ids (`assurance`, `controls-testing`, `document-production`, `research-synthesis`,
  `draft-review-loop`, `assist`, `step`, `personal-assistant`).
- **Body:** it has every template section, in order (`brief.md:29-113`).
- **Defects (D5):**
  - `sourcing: configure` (`:15`) while step 2 is open. The schema reserves `undecided` for "Before step 2 ends"
    (`solution.md:92`), and the brief itself calls the decision "proposed … Not confirmed" (`:71`).
  - `vendor_evaluations: []` (`:17`), although `overlay/vendors/enterprise-assistant-business.md` was written in
    turn 5.
  - The Summary still says "the integrated-audit manager names the benefit owner" (`:35`), after the benefit owner
    was named.
  - The decisions log records the skill's own persona as a role: "Proposed by the delivery lead". It also records
    the portfolio lead, who is `owners.delivery` (`:10`), confirming decisions that rows 1-2 leave "to be confirmed
    by the business owner" (`:101-104`) (D7).
  - The open-question list numbers one item "2a" (`:117`).

## 3. The governance handoff

**Triggering.** ai-governance was loaded by name (`drive.log:45`). It gave the confidentiality reminder and asked
one question, for the product, tier and terms (`transcript.md:45`, `:51`), rather than invent them (`:49`).

**`overlay/tool-catalog.yaml`: parses and matches `tool-catalog/v1`.**

- The four required fields and `not_approved_note` are present.
- The ids are valid: `status: under-review`, `tool_tier: commercial`, `data_classes: [public, firm-internal]`,
  `max_risk_tier: tier-2`, and all six re-approval triggers (`policy.md` §3.2-3.5).
- The header follows the template and lists every missing step-6 field (`vendor`, `underlying_model`, regions,
  retention, `user_groups`, `last_reviewed`) (`tool-catalog.yaml:3-7`).
- The contract and the no-training claim are marked "as reported … signed contract not checked" (`:24`, `:30`).
- `request_path` is three placeholders, "To be set at policy step 7" (`:13-15`).
- The restriction "Client data is not permitted" names no alternative (`:19`), against governance rule 12 (N9).

**`overlay/vendors/enterprise-assistant-business.md`: parses; its key set equals the template's.**

- All six ratings are `unknown`, each with a note. `decision: pending`. The label is `draft-to-validate`.
  `catalog_id` is set. `own_sample_test: not-applicable` is right for a tier-2 use (`vendor-evaluation.md:30`,
  `:110`). The screens are `not-applicable` with reasoning and "Risk lead to confirm" (`:61-63`).
- **Drift (D8):**
  - `evaluation: desk` (`:7`), although nothing public was checked; the body says "contract check, not started"
    (`:30`).
  - "Evaluated by: delivery lead's draft" (`:30`), although ai-governance wrote the file.
  - Two sections the template lacks: "Status" (`:32`) and "What to bring" (`:47`).

**`overlay/policy.md`.**

- The tier row now reads "`tier-2` (proposed; the risk lead has not confirmed it)" (`:86`).
- A new §7 lists the vendor file (`:103-107`). But "Remaining sections" still says §7 is "not written" (`:111`)
  (D8).
- `step_completed` was left at 0, which is honest (`transcript.md:160`).

**Does the brief reflect the tier? Only in the body.**

- §1 Constraints and §2 Catalog check give `tier-2`, proposed (`brief.md:59`, `:70`).
- The frontmatter has `risk_tier: null` (`:18`), and so does `portfolio.yaml:514` ("stays null until the risk
  lead confirms").
- This follows `solution.md:112-113`, but it goes against ai-portfolio's N10 rule: with a draft policy, "set
  `risk_tier`, and write the tier … as 'provisional'" (`library/index.md:84-86`) (D4).

**Anything claimed as approved that only a person can approve? No.**

- The tier is "proposed", the catalog entry is `under-review` ("I can't move the status off `under-review`; that
  needs the risk lead's confirmation", `transcript.md:172`), and the vendor decision is `pending`.
- Both messages were drafted, not sent: "I haven't sent anything" (`:105`), "I haven't sent or changed anything"
  (`:178`).
- The four full-path `g0` records were drafted in chat only: "None of them is recorded in `portfolio.yaml` yet"
  (`:235`).
- The one soft spot is the brief's decisions log, where the portfolio lead "confirms" the business owner's
  decisions as direction (D7).

## 4. Core rules

| Rule | Result | Evidence |
|---|---|---|
| No named individuals | Pass | Roles only, in every file and turn |
| Ranges | Pass | Value 0-0.2 h per test (`portfolio.yaml:556`); 20-30 cases (`brief.md:79`). The point figures in turn 7 (24 h, USD 5,040) are the plan's own (`transformation-plan.md:339`) and are labelled "come from the audit plan, reported" (`transcript.md:246`) |
| No invented sources | Pass | No new citations. The pattern line matches `draft-review-loop.md:40` |
| Grades as recorded | Pass | `assurance-controls-testing-01` B and `-02` B (`brief.md:51`; `intake:41`) match `evidence_grade` in `archetypes/assurance/use-cases/controls-testing.yaml`. So do 03 C and 10 B, cited in turn 7 |
| No claims to build, run or test | Pass | "this plan does not run anything" (`brief.md:76`); "I've opened the vendor evaluation but not run it" (`transcript.md:154`); "I couldn't run the YAML parse check" (`:16`, true: `jsonl:93`, `:139`) |
| Dependencies, not deadlines | Pass, one soft spot | The "Needs first" column (`intake:67-72`) and "by g1" kill lines use dependencies. Soft spot: "until the risk lead has had your confirmation request for a day or two" (`transcript.md:216`) |

## 5. Round-2 fixes exercised here

| # | Now | Evidence |
|---|---|---|
| N2 shortest-path offer | Not exercised | The item asked for qualified. Turn 6's "What else can move" lists each item and what blocks it (`transcript.md:201-222`), in the spirit of the rule |
| N3 template sections only | **Partly fixed** | The `ct-int` record keeps to the template; resources, kill criteria and the parked category sit inside Screen result (`intake:51-59`). The drafted messages and the four `g0` records stayed in chat. But the undefined "Live-systems list" section in `firm-enterprise-assistant.md` was extended with an 11-row table (`:51-71`), because the plugin has no home for a live system (D9) |
| N4 live limit binds later gates | **Fixed** | "The unset live limit doesn't hold up `g0`; it binds at `g1`" (`transcript.md:208`, `:217`, `:307`). Header: "binds at g1, not g0" (`portfolio.yaml:96-97`) |
| N5 state and header | **Mostly fixed** | `step_completed: 3`, `next_step: 4` (`portfolio.yaml:83-84`). The `g0` header line was refreshed (`:95-98`). But `:87-89` still says "no weighted_score, indexes, horizon, risk tier, gate path or sponsor yet" |
| N6 duplicate keys | **Still present** | It caught its own duplicate `category` (`jsonl:205`: "I introduced a duplicate `category` key"). It missed the duplicate `benefit_owner` from the same edit (`jsonl:196`): `:517` sets it, and `:554` (`null`) wins. The inherited duplicate `revisit_when` (`:208`, `:235`) also remains. The parse checks were refused (D2) |
| N7 verbatim value | Not exercised | No import. The `ct-int` value line is unchanged (`portfolio.yaml:556`) |
| N8 `rolled_up_from` / `label` | **Partly** | The meaning was honoured: validation cleared the draft-to-validate block, and the item moved from outline to active (`intake:8`, `:51`). But `provisional: true` was deleted without setting `label: null` (`schemas/portfolio.md:137-138`). The other four items and the header keep `variant_of`/`provisional` (`portfolio.yaml:92-94`, `:434-435`, `:571-572`) |
| N9 governance draft-ahead, alternatives | **Partly** | One question before the catalog entry; the policy step counter was left alone; drafts are labelled "DRAFT" (`tool-catalog.yaml:3`). But the data classes (step 2) and vendor fields (step 6) were written without the "Drafted ahead on assumptions" label, and the client-data restriction names no alternative (`:19`) |
| N10 template lines, provisional tier | **Still present** | `risk_tier: null` with a draft policy (`portfolio.yaml:514`), against `library/index.md:84-86`. The record was edited but still lacks Early read's Risk tier, Build-or-buy leaning and AI use lines (`intake:37-43`; template `:51-58`) |

## 6. Harness

- **Fixed:**
  - Stage 2 runs alone in a fresh session, on a copy outside the repo.
  - The launch block is logged.
  - Edit calls appear in the transcript (`transcript.md:6-10`).
  - The run ended on no open question (`transcript.md:309`).
- **New (D2):** `TOOLS` allows `Bash(python3 -c *)` (`drive_suite.py:40`), but the assistant runs `python3 -I -c …`
  and `python3 -I <script>`. All three parse attempts were refused (`jsonl:34`, `:93`, `:139`), so the duplicate
  key went unseen. The assistant said so honestly (`transcript.md:16`, `:73`).

## 7. New defects, by severity

| # | Severity | Defect | Proposed fix (named file) |
|---|---|---|---|
| D1 | High | Duplicate `benefit_owner` in `ct-int-nonclient-drafting` (`portfolio.yaml:517`, `:554`). The file parses with `benefit_owner: null`, so the benefit owner the user named and the transcript reports as set (`transcript.md:85`) is lost. A gate reading the file sees no benefit owner, which is one of this item's own kill criteria (`:529`) | `ai-portfolio/SKILL.md` save rule: before adding a field to an item, search that item for the key and edit it in place; never insert a second one. Add the same line to `ai-portfolio/references/method/stage-gates.md` §2 (recording a decision) |
| D2 | Medium (harness) | The parse check is blocked by the allowlist, so N6 can't work in the e2e runs | `evals/e2e/drive_suite.py:40`: add `Bash(python3 -I -c *)` and `Bash(python3 -I *)`, or tell the persona's system prompt which form is allowed |
| D3 | Medium | `solution` was set in the `g0` edit, before delivery opened the brief (`jsonl:76` against `:130`). There was no handback step, and a failed brief write would leave a dangling link | `ai-portfolio/references/method/stage-gates.md:103` and `ai-portfolio/SKILL.md:196`: "a `g0` Go does not set `solution`; set it only when `solutions/<id>/brief.md` exists and delivery has handed back". Mirror it in `ai-portfolio/references/schemas/portfolio.md:144-145` |
| D4 | Medium | The two skills disagree on the tier under a draft policy. ai-portfolio says set it and mark it provisional (`library/index.md:84-86`); delivery says copy it or leave `null` (`solution.md:112-113`). Result: `null` in both files while the body says `tier-2` | `ai-solution-delivery/references/schemas/solution.md` §4 Risk tier: with a policy that is not `approved`, copy its proposed tier into `risk_tier` and mark it "provisional" in §2 Catalog check and the Handoffs row. Or change `library/index.md` §2 to keep `null`. One rule, in both files |
| D5 | Medium-Low | Brief frontmatter and summary drift: `sourcing: configure` with step 2 open (`brief.md:15`); `vendor_evaluations: []` after the vendor file was written (`:17`); a stale Summary "Next" (`:35`) | `ai-solution-delivery/references/method/build-or-buy.md` §8: keep `sourcing: undecided` until step 2's exit criteria are met, and put the leaning in the decisions log. `ai-solution-delivery/SKILL.md` save rule: after a sibling skill writes an overlay file for this solution, update `tools`, `vendor_evaluations` and the Summary. `ai-governance/SKILL.md` step 6 output: when the request came from a brief, hand the vendor file path back to ai-solution-delivery |
| D6 | Low-Medium | False conflict: "Those can't both be right" on the senior manager's hours (`transcript.md:244`). The plan reconciles them: about 6 h a week in all, of which 2 h is the back-test (`transformation-plan.md:346`). The cause is the ambiguous intake line "this owner also back-tests the checklist (about 6 h a week …)" (`sox-report-register.md:58`). This is round-1 defect 1 recurring on a gate draft | `ai-portfolio/references/method/stage-gates.md` §2: before flagging a conflict between intake records, read the plan section their "From the plan" lines came from. `ai-portfolio/references/method/intake.md` §2: each "From the plan" line names its plan section (the template already asks, `templates/intake.md:63`) |
| D7 | Low | Decisions are confirmed by a role that is not the business owner, and the skill's persona is recorded as a role ("delivery lead", `brief.md:101-104`; `vendors/…:30`) | `ai-solution-delivery/references/schemas/solution.md` §4 Owners: "Decided by" is `owners.business` or another firm role. Drafts read "draft (ai-solution-delivery)". A confirmation by another role is logged as direction, and the owner's confirmation stays an open criterion |
| D8 | Low | Governance files drift: `policy.md:111` still lists §7 as not written after §7 was added (`:103`); the vendor file says `evaluation: desk` with no desk check and adds sections the template lacks | `ai-governance/SKILL.md` save rule: after adding a section, refresh the file's status notes. `ai-governance/references/vendor-evaluation.md`: set `evaluation: desk` only after public documents are checked; write only the template's sections; requests for documents go in the chat |
| D9 | Low | No defined home for a live system's inventory entry. The skill extended an undefined section and left the tool at `intake/outline` (`firm-enterprise-assistant.md:51-71`; `transcript.md:240`) | `ai-portfolio/references/method/intake.md` and `ai-portfolio/references/templates/intake.md`: define how a tool already in use is logged (its stage, the owner fields, the use list and licence count as Next gate evidence rows or a template section), and say so in `ai-portfolio/references/schemas/portfolio.md` §2 |

**Verdict: the portfolio → delivery handoff is acceptable, conditional on D1-D4.** `g0`, the brief in discover,
the `solution` link, the next-gate evidence table, unticked steps and the governance handoff all held, and no
approval was overclaimed. The suite handoff (advisor → portfolio → delivery, with governance) has now been run end to
end, so the spec §7 smoke test is done. Before calling it closed:

1. Fix D1 in the plugin rules and D2 in the driver.
2. Settle D3 and D4 with one rule each.
3. Re-run stage 2 with `--stages 2` to confirm that the parse checks run and `benefit_owner` survives. No re-run of
   stage 1 is needed.

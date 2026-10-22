---
schema: solution/v1
doc: brief
id: ct-int-nonclient-drafting
title: "Shared prompts and a review routine on the approved enterprise assistant for test-step wording, templates and junior practice cases (non-client material only)"
source:
  portfolio_item: ct-int-nonclient-drafting
  opportunity: { file: units/integrated-audit/opportunities.yaml, id: ct-int-nonclient-drafting }
scope: { name: "Audit: integrated audit ICFR testing", level: team }
owners: { business: "Integrated-audit manager", delivery: "Portfolio lead (head of AI office)", support: null }
classification:
  archetype: assurance
  modules: [ controls-testing ]
  work_types: [ document-production, research-synthesis ]
  pattern: draft-review-loop
  ladder: assist
  ladder_target: null
  change_scope: step
  runtime_class: personal-assistant
ai_use: null
sourcing: undecided
tools: [ "Approved enterprise AI assistant (live; non-client material only); no tool catalog exists yet" ]
vendor_evaluations: []
risk_tier: tier-2
status: in-progress
step_completed: 0
next_step: 1
updated: 2026-10-22
---

# Solution brief: Shared prompts and a review routine on the approved enterprise assistant (non-client material only)

<!-- Schema: references/schemas/solution.md. Opened in discover as evidence for g1 (light path: g1 and g2 combined). risk_tier is provisional: copied from the proposed tier in the draft overlay/policy.md, which is not approved. -->

## Summary

Integrated-audit staff could draft test-step wording, narrative templates and synthetic junior practice cases faster with the approved enterprise assistant, on non-client material only. Today a few seniors already use it this way (reported, not verified). The idea is a small shared set of prompts plus a share-and-review routine, not a new tool. Value is small and unmeasured (0-0.2 staff hours per control test, grade D). Portfolio g0 is a Go into discover, so the brief is the first evidence toward g1.

Where things stand: the frame is drafted from the portfolio item and the plan, but the baseline, the owner's confirmed metric and a real recent instance are still missing, so step 1 is not ticked. A sourcing leaning exists (configure the assistant the firm already has) but it is a leaning, not a decision. **Next:** step 1, with the integrated-audit manager.

## Progress

- [ ] 1 Frame the problem. Open: owner confirms the metric; baseline from a record; last real instance and volume; sample of real non-client templates seen; benefit owner named
- [ ] 2 Build, buy or configure. Open: option tested on a sample of 20-50 non-client cases; run-cost range; tool-catalog check (no catalog exists); owner after launch named
- [ ] 3 Solution design
- [ ] 4 Evaluation plan (`eval-plan.md`)
- [ ] 5 Production readiness (`readiness.md`)
- [ ] 6 Launch and post-launch review (`post-launch.md`)

## 1. Problem frame

- **Started from:** portfolio item `ct-int-nonclient-drafting`, stage discover (g0 Go, light path); advisor option of the same id in `units/integrated-audit/opportunities.yaml` (label draft-to-validate; validated by the integrated-audit manager).
- **Problem statement:** Help integrated-audit staff draft test-step wording, narrative templates and junior practice cases with the enterprise assistant on non-client material, so that template and wording time falls. (From the portfolio item; to be put in the owner's own words at step 1.)
- **Business owner:** Integrated-audit manager; confirmed the metric: **yes** (stated by the manager, relayed by the portfolio lead); reviews outputs: not yet agreed.
- **Success metric and baseline:** staff hours per control test spent on template and wording work, taken from timesheet codes · today: no measure; the plan's ceiling is 0-15% of the 1.5 h hands-on per test (reported, a guess, grade D) · basis: **reported, not yet from a record**. Timesheet codes checked by the portfolio lead: there is one code, "engagement administration", and nothing isolates template and wording time, so the metric cannot come from the codes. **Baseline plan:** a short time sample, five control tests over two weeks, with the integrated-audit manager logging template and wording time by hand per test. The result will be labelled **observed** (a small sample, not a record). Sample rules are in Open questions. Experience lever (juniors learn by critiquing drafts) is qualitative and not quantified.
- **The work today (last real instance):** not yet collected. Known: a few seniors use the assistant on templates such as a control narrative template (reported, not verified); a usage rule exists (no client data).
- **Volumes (last month or season):** not recorded · rework share not recorded · time per item not recorded · basis: none.
- **Users and reviewers:** users are integrated-audit staff and juniors; a senior approves templates before shared use. Accountable professional for anything that enters a workpaper: the engagement's reviewing senior or manager (to confirm).
- **Error costs:** the costly error is client data pasted into the assistant by mistake, and unreviewed wording entering a workpaper. Neither is irreversible inside the firm, but a data slip is a confidentiality incident. Who would notice: the senior reviewing the template; a prompt log would be needed to catch a data slip (open).
- **Fit checks:** rule or template baseline: a plain template library may already do part of it, so it is the baseline to beat; AI adds something mainly for synthetic practice cases (intake record, to test at step 1 or 2) · judgment, tangled rules or unstructured data: none; this is drafting, single model call · intern test: not yet run, to run on 3 agreed use cases.
- **Informal AI use today:** a few named seniors use the approved assistant on templates and on a summary of a PCAOB release, weekly-ish (reported, not verified). Data risk: none known beyond the rule against client data; no log exists.
- **Pattern and rung hypothesis:** `draft-review-loop` at `assist`. Pattern "not when" lines not yet checked against the pattern file; to do at step 1.
- **Constraints:** non-client material only; no tool is approved for client evidence; wording that enters a workpaper stays under the normal supervision and review (draft overlay policy: `tier-2`, standard "same diligence as if AI were not involved").
- **Decision:** proceed to step 2 as a draft leaning only, because the rules-or-AI check and the baseline are still open. Draft (ai-solution-delivery).

## 2. Build, buy or configure

Draft leaning, not a decision. No option has been run on a sample, and the cost and owner are open.

| Option | Fit to the workflow | Result on our sample | Total run cost (range) | Switching cost and exit | Data handling | Differentiation | Owner after launch |
|---|---|---|---|---|---|---|---|
| Rules or existing tool: a shared template library with no AI (the baseline to beat) | Covers wording and narrative templates; cannot make fresh synthetic practice cases | Not tested | No new licence; time to curate, not sized | None | Non-client material in the firm's own store | None | Integrated-audit manager (to confirm) |
| Configure: the approved enterprise assistant with shared prompts, approved reference templates and a share-and-review routine | Fits drafting, wording and synthetic cases at `assist`; senior approves before shared use | Not tested | No new licence expected (already approved and in use; IT holds the count); routine and review time not sized | Low: prompts and cases are plain text and move to any assistant | Stays inside the approved assistant's terms; non-client only | None: a general capability many firms use | Integrated-audit manager for prompts and templates; IT/security lead for the tool |
| Build-on-model or build-custom | Not warranted for wording and templates | Not tested | Not estimated; far above a configured assistant | High | New data flows to assess | None | No owner would exist (advisor default: no owner, no build) |

- **Catalog check:** `overlay/tool-catalog.yaml` now holds one draft entry, `enterprise-assistant`, at `under-review` with a proposed `max_risk_tier: tier-2`; it is not yet approved. The assistant is named as approved for non-client material only in `overlay/policy.md` (draft). The IT/security lead completes the entry and the risk lead confirms the tier. **Draft leaning:** `configure` on `personal-assistant`, at `assist`, because it uses a tool the firm already approves, the work is general drafting with no differentiation, the data is non-client, and a build has no owner. A rule-based template library stays as the baseline that the assistant must beat on the sample.
- **Maintenance:** who re-tests the shared prompts when the model changes: Integrated-audit manager (to confirm). **Revisit when:** the template library alone meets the bar on the sample; a client-data approval route opens and the use widens beyond non-client material; or the baseline shows template and wording time too small to justify the routine.

## 3. Solution design

Not started.

## Decisions log

| Step | Decision | Reason | Decided by (role) |
|---|---|---|---|
| 1 | Proceed to step 2 as a draft only; step 1 stays open | Baseline, owner-confirmed metric and a real instance are missing | draft (ai-solution-delivery) |
| 2 | Leaning: `configure` the approved enterprise assistant on `personal-assistant` at `assist`; `sourcing` stays `undecided` | Existing approved tool; general capability; non-client data; no owner for a build. Not yet tested on a sample | draft (ai-solution-delivery) |
| 2 | g1 decision criteria drafted before the sample (section "g1 decision criteria"); thresholds for the gatekeepers to confirm | Set before data so the result does not set its own bar | draft (ai-solution-delivery) |
| 2 | Provisional `risk_tier: tier-2` | Copied from the proposed tier for this item in the draft `overlay/policy.md`, which is not approved | draft (ai-solution-delivery); the risk lead confirms |

## Handoffs

| To | What | Status |
|---|---|---|
| ai-portfolio | Brief exists; set the item's `solution`. Build or buy leaning: configure the existing approved assistant (draft). Provisional `tier-2`. Gate evidence for g1: problem frame (partial), leaning | Handed back |
| ai-governance | Catalog entry requested: `enterprise-assistant` in `overlay/tool-catalog.yaml`, status `under-review`, proposed `max_risk_tier: tier-2`. IT/security lead to fill vendor, contract, settings and retention; risk lead to confirm `tier-2` (provisional until the policy is approved). No vendor evaluation yet | Requested, awaiting IT/security and risk leads |

## g1 decision criteria (draft, written before the sample)

Draft (ai-solution-delivery), written before any sample data exists so the result does not set its own bar. The thresholds are proposals: the practice leader, risk lead and IT/security lead (the gatekeepers) confirm or change them before logging starts, and the confirmation goes in the decisions log. The sample is five tests, so the criteria use the median and the spread, not the mean.

**Measure:** share of total hands-on time spent on template and wording work, per test, from the sample. Take the "in" column as the lower figure and "in" plus "unsure" as the upper. One test cannot decide the outcome.

| Outcome at g1 | When |
|---|---|
| **Go** (combined g1 and g2, to the light-path pilot) | The median share is **10% or more** on the lower figure (about 0.15 h of the 1.5 h per test), **and** at least three of the five tests are at 5% or more, **and** every non-numeric condition below is met |
| **Recycle** to a smaller scope (shared template library only, no AI routine, or synthetic practice cases only) | The median is **5% to under 10%**, or the median is 10% or more but only one or two tests drive it |
| **Kill** (or Hold, if the manager wants to re-sample on a different mix of tests) | The median is **under 5%** on the upper figure, or the sample cannot be completed, or a kill criterion in the portfolio is met |

**Non-numeric conditions for a Go (all required):**
1. The benefit owner is named, and the metric is confirmed as written above.
2. The routine's own time (keeping prompts and templates current, and the senior's approval before sharing) is estimated, and is **less than half** the hours the median share would release at the integrated line's monthly test count. The test count is not yet recorded: **someone counts it from records** before g1.
3. The real non-client templates and synthetic examples have been looked at by the manager; the share-and-review routine is written; three first use cases are agreed.
4. A sample test on 20 to 50 non-client cases has compared the configured assistant with a shared-template baseline, and the assistant adds something the template library does not, or the leaning moves to the library.
5. The catalog entry `enterprise-assistant` has at least vendor, contract and retention filled in (so a prompt that carried client data could be noticed), and the risk lead has confirmed `tier-2` for this use, or the gatekeepers record that they proceed on the provisional tier.
6. The steering group has set the live limit and a place is free under it.
7. Value is **re-scored from the measured range**, with the portfolio's scores and weights. The category stands as quick win only if the value score comes out above 2 (the screening rules park items at 2 or below). Otherwise the category changes to park and the Go is not available.

**Not a reason to Go or Kill by itself:** the manager's view that the assistant is "useful", or staff liking it. Usage is not value.

## Open questions

1. Baseline sample: the timesheet codes do not isolate the time, so follow the protocol below. Draft (ai-solution-delivery); the integrated-audit manager corrects the definition and examples before logging starts.
2. Which three non-client use cases are first (from the opportunity's next step)?
3. Does a template library alone meet the bar? Run both on the same sample of 20-50 non-client cases.
4. Who keeps the prompts and templates current, and where do they live?
5. Is there a prompt log, or any way to notice client data pasted by mistake?
6. Value is low (value index 2.44): the routine must stay cheap or the g0 condition fails. Size its time.

### Baseline sample protocol (draft, for the integrated-audit manager)

**Why:** no timesheet code isolates template and wording time ("engagement administration" is the only code), so the metric, staff hours per control test on template and wording work, comes from a short hand-logged sample. **Basis label for the result:** observed, self-logged, n=5. It replaces the plan's reported guess of 0-15% of the 1.5 h hands-on per test, which has no measure behind it.

**Definition (draft).** Template and wording work is time spent writing or rewriting the standard text around a control test, as distinct from performing the test or judging the result.

| In (log it) | Out (do not log it) |
|---|---|
| Rewording a test step so it reads clearly for the control being tested | Deciding whether the control operated effectively |
| Adapting a control narrative template to the control at hand | Selecting the sample or choosing the population |
| Filling a standard workpaper template's headings and boilerplate sections | Examining evidence or re-performing the control |
| Fixing format, numbering or tone of test-step text after review notes | Writing the conclusion or an exception description that needs judgment |
| Searching old files for a template to reuse, when the aim is the wording | Waiting for evidence from the control owner |
| Building a practice case for a junior from invented, non-client facts | Coaching a junior on why a check matters |

Edge cases: log them in a separate "unsure" column, with one line on what the task was, and do not decide later. The manager and the portfolio lead sort them at the end.

**Checklist**

- [ ] The manager agrees or edits the definition and the in and out examples above, before any logging.
- [ ] Choose five control tests that are typical of the integrated-audit line, not the easiest. Record each by its engagement-file test id and type only (no client names, no content).
- [ ] The assistant is not used on these five tests. If anyone uses it, note which test, so the sample stays a pre-change baseline.
- [ ] For each test, log: test id and type, level of the person doing the work (staff, senior; no names), minutes on template and wording, minutes in the "unsure" column, and total hands-on minutes for the test.
- [ ] Log at the end of each work session, not from memory at the end of the week.
- [ ] Note any unusual test (rework after review, a new template, a first-time control) on its row.
- [ ] Close the sample when five tests are logged, not on a date. Say so if fewer than five are logged and why.
- [ ] If possible, a second person times one or two of the tests alongside, to check the self-logging.
- [ ] Report the range across the five tests, the total, and the share of hands-on time, for template and wording alone and with the "unsure" column added. The mean on its own is not enough at n=5.
- [ ] Give the log to the portfolio lead, who writes the baseline, with its basis label, into the brief and the intake record.
- [ ] The log holds no client names, client data or file content, and no names of staff.

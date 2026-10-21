---
schema: solution/v1
doc: brief
id: "ct-int-nonclient-drafting"
title: "Shared prompts and review routine on the approved enterprise assistant for test-step wording, templates and junior practice cases (non-client material only)"
source:
  portfolio_item: "ct-int-nonclient-drafting"
  opportunity: { file: "units/integrated-audit/opportunities.yaml", id: "ct-int-nonclient-drafting" }
scope: { name: "Audit: integrated audit ICFR testing", level: team }
owners: { business: "Integrated-audit manager", delivery: "Portfolio lead (head of AI office)", support: null }
classification:
  { archetype: assurance, modules: [controls-testing], work_types: [document-production, research-synthesis], pattern: draft-review-loop, ladder: assist, ladder_target: null,
    change_scope: step, runtime_class: personal-assistant }
ai_use: null
sourcing: configure
tools: ["enterprise-assistant-business (draft catalog entry, status under-review, awaiting risk lead confirmation)"]
vendor_evaluations: []
risk_tier: null
status: in-progress
step_completed: 0
next_step: 1
updated: 2026-10-21
---

# Solution brief: Shared prompts and review routine for non-client audit drafting

<!-- Opened in discover as evidence for g1 (light path: g1 and g2 combined). Steps 1 and 2 are drafted from the portfolio item, its intake record and the desk review, so they are NOT ticked: the open criteria are listed beside each. Cases by type, source and id only. Owners are roles. -->

## Summary

Integrated-audit staff spend some part of each ITGC control test (reported 1.5 h hands-on, no time record) on test-step wording and narrative templates, and a few seniors already use the approved assistant for this. The idea is to turn that into a shared set of prompts, a senior-approved template library and synthetic practice cases for juniors, all on non-client material.

Draft decisions: try a template-library baseline first; then **configure** the approved enterprise assistant (no new tool, no build), `personal-assistant` class at `assist`. Both rest on reported figures with no records, and the own-sample test has not been run, so neither is confirmed. The value is small (up to 0.2 staff hours per control test, grade D), which is why the cost has to stay near zero.

Next: the integrated-audit manager names the benefit owner, agrees three non-client use cases and brings the baseline from time records. Then step 2 is re-checked on a small sample of their own tasks.

## Progress

- [ ] 1 Frame the problem. Benefit owner named. Open: benefit owner has not confirmed the metric; baseline still reported, not yet pulled from timekeeping; last real instance not walked through; template-library baseline not tried.
- [ ] 2 Build, buy or configure. Tool and its terms recorded. Own-sample test plan drafted (see §2). Open: own-sample test not run, thresholds not set; post-launch owner is a placeholder role; run cost not priced; risk lead has not confirmed tier-2 or the catalog entry; depends on step 1 closing.
- [ ] 3 Solution design
- [ ] 4 Evaluation plan (`eval-plan.md`)
- [ ] 5 Production readiness (`readiness.md`)
- [ ] 6 Launch and post-launch review (`post-launch.md`)

## 1. Problem frame

- **Started from:** portfolio item `ct-int-nonclient-drafting`, stage discover (g0 Go recorded; light path); advisor option of the same id in `units/integrated-audit/opportunities.yaml` (labelled draft-to-validate, now validated by the integrated-audit manager).
- **Problem statement:** Help integrated-audit staff draft test-step wording, narrative templates and junior practice cases with the enterprise assistant on non-client material, so that template and wording time falls. (From the intake record; not yet confirmed in the owner's own words.)
- **Business owner:** Integrated-audit manager (placeholder role) leads the work; **benefit owner: the integrated-audit manager's practice leader** (named by the portfolio lead). Confirmed the metric: **no, not yet** (the benefit owner has not been asked to confirm hours per control test); reviews outputs: to agree (a senior approves templates before shared use).
- **Success metric and baseline:** staff hours per control test spent on template and wording work · 0 to 0.2 h (0-15% of the reported 1.5 h hands-on) · **reported from one case; no record exists**. Secondary: staff experience (juniors critique drafts against what they saw), not quantified. Evidence grade D for the capacity range; supporting archetype entries assurance-controls-testing-01 and -02 (grade B each, as recorded).
- **The work today (last real instance):** not yet walked through. What is known: a few seniors use the assistant on templates today (reported, not verified); other staff write test-step wording and narrative templates by hand.
- **Volumes (last month or season):** not recorded. Needed: control tests last month in the integrated line, and time spent on template or wording work.
- **Users and reviewers:** integrated-audit staff and juniors use the output; a senior approves templates before shared use; whoever prepares and reviews a workpaper stays accountable for any wording that enters it, as without AI.
- **Error costs:** wording that enters a workpaper unreviewed, or a template that misstates a test step, is carried into audit documentation (correctable, but regulator-facing). Client data pasted into a prompt by mistake is the costly, irreversible error; the control is the usage rule plus the checkpoint, not the tool.
- **Fit checks:** rule or template baseline: **not tried**; a maintained template library may do most of the template part, and the assistant adds most for synthetic practice cases and first-draft wording. Agent-fit signals (judgment on exceptions, tangled rules, heavy unstructured documents): none holds, so a single model call is enough. Intern test: not run.
- **Informal AI use today:** a few seniors use the approved assistant on templates (reported). Data risk: nothing records what is pasted, so the usage rule has to be restated.
- **Pattern and rung hypothesis:** `draft-review-loop` at `assist`. "Not when" checks in the pattern file: review volume above reviewer capacity: clear (a senior approves a small template set); no baseline of time and errors: **issue, open** (the baseline above); drafting is the learning for juniors: **issue, handled in design** (juniors critique AI drafts and keep a manual rotation, rather than receiving finished wording).
- **Constraints:** non-client material only (draft policy: the approved assistant is limited to non-client material; ceiling tier-2); audit documentation duties apply to any wording used in workpapers; client engagement-letter restrictions do not bite while no client data is used.
- **Decision (draft):** proceed to step 2, conditional on the template-library baseline being tried first. If a maintained template library meets the bar for the template work, solve that part without AI and keep the assistant for practice cases and first-draft wording.

## 2. Build, buy or configure

| Option | Fit to the workflow | Result on our sample | Total run cost (range) | Switching cost and exit | Data handling | Differentiation | Owner after launch |
|---|---|---|---|---|---|---|---|
| Template library only (existing tool, no AI) | Covers standard test-step wording and narratives; no synthetic practice cases | Not tried | Not priced; staff time to maintain | None | No client data | Not differentiating | Integrated-audit manager (placeholder) |
| **Configure the approved enterprise assistant** (shared prompts, approved templates, synthetic cases) | Fits the tool staff already use; no new system | Not run | No new licence cost expected (existing assistant); review time and prompt upkeep not priced | Low: prompts and templates are text and move to another assistant; retest on change | Non-client material only; assistant's approved terms not reviewed here | Not differentiating | Integrated-audit manager (placeholder) |
| Build on a model or build custom | Not warranted for a drafting aid worth up to 0.2 h per test | Not run | Likely above the benefit range (judgment, not a priced figure) | High | Needs new data flows and vendor review | Not differentiating | None named |

- **Catalog check:** the assistant has a draft entry in `overlay/tool-catalog.yaml`: `enterprise-assistant-business`, business tier, enterprise terms with a data processing addendum, no training on the firm's inputs (all as reported by the portfolio lead; signed contract not checked), `data_classes: [public, firm-internal]`, `max_risk_tier: tier-2`, status `under-review`. **Client data is not permitted for this item.** `overlay/policy.md` is a draft that proposes tier-2 for the item. **The risk lead has not yet confirmed the tier or the catalog entry**, so the item's `risk_tier` stays null here until they do.
- **Decision (proposed):** `configure` on `personal-assistant`, at `assist`, because this is general capability, the benefit range is small, and a build would cost more than it could return. **Not confirmed**: it needs the template-library baseline and a small own-sample test on non-client cases, run in the approved assistant by the manager's team.
- **Maintenance:** someone re-tests the shared prompts when the assistant's model changes and keeps the approved templates current; the placeholder is the integrated-audit manager, to be confirmed. **Revisit when:** the measured template and wording share falls below what the benefit owner sets as worth the review routine, the assistant's terms or model change, or the usage rule is breached.

### Own-sample test plan (draft; synthetic cases only)

Purpose: show, on the team's own kind of work, whether the approved assistant beats the template-library baseline for test-step wording, narrative templates and junior practice cases. It decides the sourcing in step 2 and seeds the evaluation plan in step 4. The team runs it in the approved assistant; this plan does not run anything.

- **Data rule:** synthetic and firm-internal material only. No client data, no client evidence, no real client names, systems or figures, no personal data, not even redacted. Each case is invented by a senior from the control type, not copied from a workpaper. Cases are listed by id, type and source only; their content stays in the practice's approved system.
- **Case set:** 20 to 30 cases (draft size; the manager may set it smaller for an item this size), in three types:
  - **W** test-step wording: a control description in, a test step out (user access recertification and one or two other common control types).
  - **T** narrative template: a template for a recurring workpaper section.
  - **P** junior practice case: a synthetic scenario with a planted gap or error for a junior to find.
  - Include at least a few cases built from **past mistakes in wording** (ambiguous step, missing period, wrong population), written as synthetic examples.
- **Gold answers:** a senior writes the accepted wording or the answer key (the planted errors for type P) before anyone runs the assistant. Where two seniors would word it differently, record both as acceptable and mark the case "varied".
- **Comparison:** each case is done three ways: (a) the practice's existing template or wording library (the no-AI baseline), (b) the assistant with a plain prompt, (c) the assistant with the shared prompt and the approved templates.
- **Pass/fail checks (binary, per case):** the step names the right population and period; the step is testable and not ambiguous; nothing is invented (a control, a system or a standard the case did not give); no client-specific detail appears (checks the usage rule); for type P, the planted errors are all present and none is a trivial giveaway. A senior marks each check pass or fail on a simple sheet.
- **Also record:** minutes for the reviewing senior to fix or accept each draft, because review time is what can eat the benefit; and whether a junior can still explain the check after critiquing the draft (the learning check).
- **Thresholds:** to be set by the benefit owner (the manager's practice leader) before the run, as a pass rate on the checks, plus a limit on review minutes per case against the baseline minutes taken from the time records. None is proposed here.
- **What the result decides:** if (a) already meets the bar for type W and T, keep those on the template library and use the assistant for type P and first-draft wording only; if (c) beats (a) and (b) within the review-minutes limit, confirm `configure` for step 2; if not, the item goes back to the forum (Hold or Kill under its kill criteria).
- **Who:** cases and gold answers by the integrated-audit manager's team (a senior reviews all); the run and marking by two people who did not write the case; the portfolio lead's office collects the sheet. Marking is of outputs, never of people.
- **Depends on:** the time-record baseline (portfolio lead), the benefit owner's thresholds, and the usage rule being restated to everyone who takes part.

## 3. Solution design

Not started.

## Decisions log

| Step | Decision | Reason | Decided by (role) |
|---|---|---|---|
| 1 | Proceed to step 2 in draft, template-library baseline first | Rules-first check; AI adds most for practice cases and first-draft wording | Proposed by the delivery lead; to be confirmed by the business owner |
| 2 | Configure the approved enterprise assistant (`personal-assistant`, `assist`) | General capability, small benefit range, no new tool | Proposed by the delivery lead; to be confirmed by the business owner after the own-sample test |
| 1 | Direction confirmed at the portfolio lead's request; step stays open | Benefit owner is now named (the manager's practice leader) and the portfolio lead can get the time-record baseline from the practice's timekeeping system. Still open: the benefit owner confirms the metric, the baseline is collected, the template-library option is tried | Portfolio lead (head of AI office), at the delivery lead's playback |
| 2 | Direction confirmed at the portfolio lead's request: configure the approved assistant; step stays open | The tool is the firm's enterprise assistant on the business tier, approved for internal and non-client material, with no training on inputs (reported). Still open: own-sample test, run cost and review time, post-launch owner, risk lead's confirmation of tier-2 and the catalog entry | Portfolio lead (head of AI office), at the delivery lead's playback |

## Handoffs

| To | What | Status |
|---|---|---|
| ai-portfolio | Brief opened; `solution` set on the item; the g1 evidence table reads this brief | Done in `portfolio.yaml` |
| ai-governance | Tier-2 proposed in `overlay/policy.md`; draft catalog entry `enterprise-assistant-business` written (`under-review`). Waiting on the risk lead to confirm both; the vendor evaluation (contract and no-training check) and the usage rule are not done | Partly done |

## Open questions

1. What metric does the benefit owner (the manager's practice leader) watch: hours per control test, or something else? They have not confirmed it yet.
2. Hands-on hours per control test and the template or wording share, from the practice's timekeeping system (to replace the reported 1.5 h and 0-15%). The portfolio lead can get this; not yet in hand.
2a. Does the risk lead confirm tier-2 and the catalog entry?
3. Number of integrated-audit control tests last month.
4. The last real instance: which three non-client use cases, and what does a senior approve before shared use?
5. Can a maintained template library cover the template part without AI?
6. Will the team keep a junior rotation with manual drafting, so drafting stays a learning step?
7. Is the integrated-audit manager the right post-launch owner, or the portfolio lead's office?

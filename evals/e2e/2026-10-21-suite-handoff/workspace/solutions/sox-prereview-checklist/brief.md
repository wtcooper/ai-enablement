---
schema: solution/v1
doc: brief
id: "sox-prereview-checklist"
title: "Written pre-review evidence checklist for SOX-only control tests"
source:
  portfolio_item: "sox-prereview-checklist"
  opportunity: { file: "units/sox-only-outsourcing/opportunities.yaml", id: "sox-prereview-checklist" }
scope: { name: "SOX-only outsourcing line, SOX/ICFR controls testing practice", level: team }
owners:
  business: "SOX/ICFR practice leader"
  delivery: "Practice lead"
  support: "Methodology owner"
classification:
  archetype: assurance
  modules: [ controls-testing ]
  work_types: [ review-assurance, document-production ]
  pattern: draft-review-loop
  ladder: assist
  ladder_target: null
  change_scope: step
  runtime_class: shared-team-skills
sourcing: configure
tools: [ "The practice's existing SOX workpaper templates that the seniors already fill in for control testing (no new tool, no AI model)" ]
vendor_evaluations: []
risk_tier: null
status: in-progress
step_completed: 2
next_step: 3
updated: 2026-10-21
---

# Solution brief: Written pre-review evidence checklist for SOX-only control tests

## Summary

DRAFT, opened from the portfolio item before the `g1` gate; it is gate evidence and does not move the item into prototype. The item is a written staff self-check that captures the seniors' unwritten evidence-completeness checks, so fewer tests draw a review note. The portfolio owner decided on 2026-10-21 that the written checklist is the whole solution: sourcing is **configure, no AI**, placed in the practice's existing audit templates. No checking tool is wanted; that is `sox-listing-tool`, which stays on hold. The checklist lives in the practice's existing SOX workpaper templates, and the methodology owner owns it after launch and approves any change. Step 2 is closed; step 3 (design) is next. The prototype is the co-written checklist and the blind back-test on past files.

## Progress

- [x] 1 Frame the problem (frame drafted from the portfolio and advisor files; the walk-through of the last instance and record baselines are still open)
- [x] 2 Build, buy or configure (configure, no AI, in the existing SOX workpaper templates; methodology owner after launch)
- [ ] 3 Solution design
- [ ] 4 Evaluation plan (`eval-plan.md`)
- [ ] 5 Production readiness (`readiness.md`)
- [ ] 6 Launch and post-launch review (`post-launch.md`)

## 1. Problem frame

Drafted from the portfolio entry and the advisor's file. Marked where it is reported or still to be confirmed.

- **Started from:** portfolio item `sox-prereview-checklist` (stage discover, `g0` Go recorded in review-less decision on 2026-10-21; `g1` not held) and advisor option `sox-prereview-checklist` in `units/sox-only-outsourcing/opportunities.yaml`.
- **Problem statement (draft, not yet in the owner's words):** staff submit evidence without the checks the senior would run, so completeness gaps are found late at senior review and cause review notes and second-round reviews.
- **Business owner:** SOX/ICFR practice leader; confirmed the metric: agreed by the portfolio owner on the leader's behalf, the leader's own confirmation is not recorded; reviews outputs: rhythm not yet set.
- **Success metric and baseline:** test-level review-note rate, tracked by engagement · about 30% today · reported. Evidence-completeness notes: about 42 of 210 tests a month, about 20 points of the 30% · tracking sheet as relayed, reported, not seen. Baseline from the record is a `g1` condition.
- **The work today (last real instance):** not yet walked through. The advisor's file says the senior mentally checks that the listing came straight from the system, covers the full period and that the comparison population is complete, plus the sign-off date against policy and the trace from each exception to its ticket. Staff often miss these; notes arrive after review.
- **Volumes (last month or season):** about 210 tests a month · rework share not recorded · hours per round not known · reported. Each note "usually" leads to a second round (reported).
- **Users and reviewers:** staff complete the checklist; seniors review and sample completions; the methodology owner approves it. Professionally accountable: the engagement's responsible partner for the audit opinion (plan guardrail: a person owns evidence selection, sufficiency conclusions and sign-off).
- **Error costs:** a completeness gap accepted into the file would leave an unsupported test conclusion that an inspection could find (two PCAOB comments on ITGC evidence last cycle, practice-level, reported). Costly rather than irreversible if review is real. The checklist adds a check; it does not replace the senior's.
- **Fit checks:** rule or template baseline: the checklist is the template, so the rules-first answer is already "yes" · judgment, tangled rules or unstructured data: sufficiency judgment stays with a person; no unstructured-document step in this item · intern test: not yet run, to be done on a past file.
- **Informal AI use today:** a few seniors use the enterprise chat assistant on non-client material (a control narrative template, a summary of an inspection release), reported, not verified. None known on this work. Client data is not allowed in it.
- **Pattern and rung hypothesis:** `draft-review-loop` at `assist` (advisor's classification). "Not when" checks: no baseline of time and errors from record is an open issue; the line about drafting as the learning for juniors is relevant to `sox-junior-development` and is clear here because staff still do the check themselves.
- **Constraints:** PCAOB and independence rules; AS 1215 documentation; client data only in approved tools (none approved yet); the 3-4 month approval path applies to any tool that touches client evidence.
- **Decision:** proceed with a no-AI solution, as decided by the portfolio owner: the written checklist is the whole solution and no tool checks client evidence against it. The method's rule for "solve without AI" is to stop the brief; this brief stays open at the owner's instruction because it is the record of the checklist's design and back-test and is evidence for the `g1` gate.

## 2. Build, buy or configure

| Option | Fit to the workflow | Result on our sample | Total run cost (range) | Switching cost and exit | Data handling | Differentiation | Owner after launch |
|---|---|---|---|---|---|---|---|
| **Chosen: configure the practice's existing SOX workpaper templates with a written checklist (no AI)** | The checklist sits in the control-testing templates the seniors already fill in; staff complete the self-check before submission and seniors coach against it | Not yet run: blind back-test on past files pending | No licence. Staff time: two or three protected senior half-days to write it, plus the ITGC senior manager's back-test (portfolio `g0` resources); upkeep time not yet estimated | None; a document and a template field | No client data in the checklist itself | The seniors' checks are the firm's own method, so the firm writes the content | Methodology owner, who also approves any change to the checklist |
| AI tool that checks client evidence against the checklist | Would sit in the workflow | Not tested | Not estimated | Not assessed | Client data, not approved for any AI tool | General capability | n/a. This is `sox-listing-tool`, **on hold**; not part of this solution by the owner's decision |
| Enterprise chat assistant to draft checklist wording on non-client material | Optional, only for wording | Not tested | Included in existing licence (recorded in the plan) | None | Non-client material only | General capability | Does not change the sourcing; the person writing the checklist owns every word |

- **Catalog check:** there is no `overlay/tool-catalog.yaml`, and the chosen option uses no new tool, so nothing is outside a catalog. · **Decision:** `configure` on `shared-team-skills`, at `assist`, with no AI model in the loop, because the checks are the seniors' own, are cheap to write down, and a rule or template meets the need on the advisor's own account. The `assist` rung records the advisor's classification; no model runs.
- **Maintenance:** the checklist goes stale when the standards, the platform or the PCAOB expectations change. The methodology owner owns it and approves any change. Proposed trigger for a review (not yet confirmed): each of those events, and any review note the checklist should have caught. · **Revisit when:** the back-test catches under 25% of the evidence-completeness notes (portfolio kill criterion), a PCAOB or internal inspection comment cites evidence it should have covered, or the firm approves a client-data tool and the owner wants to revisit `sox-listing-tool`.

## 3. Solution design

Not started.

## Decisions log

| Step | Decision | Reason | Decided by (role) |
|---|---|---|---|
| 1 | Proceed with a solution that needs no AI model; keep the brief open as `g1` evidence | The written checklist is the solution (advisor's description); the method would otherwise stop the brief for "solve without AI" | Head of AI |
| 2 | Sourcing `configure`, no AI, in the practice's existing audit templates; no checking tool | The owner does not want a tool checking client evidence; that is `sox-listing-tool`, on hold | Head of AI |
| 2 | Checklist placed in the practice's existing SOX workpaper templates that the seniors already fill in for control testing; the methodology owner owns it after launch and approves any change; step 2 closed | Named by the portfolio owner | Head of AI |

## Handoffs

| To | What | Status |
|---|---|---|
| ai-governance | Risk tier: the portfolio holds a provisional tier-1; no `overlay/policy.md` exists, so `risk_tier` here stays null | Not yet requested |

## Open questions

- The templates are the ones seniors fill in, but the checklist is a staff self-check. Which field in the template do staff reach before submission? To settle in step 3.
- Walk-through of the last real instance, and last month's record of notes by cause.
- Where does the checklist live and get attached (audit platform workpaper, template library)? Who keeps it current?
- Who co-writes it, and who approves it (methodology owner)?

---
schema: solution/v1
doc: brief
id: "ct-int-nonclient-drafting"
title: "Shared prompts and review routine on the approved enterprise assistant for test-step wording, templates and junior practice cases (non-client material only)"
source:
  portfolio_item: "ct-int-nonclient-drafting"
  opportunity: { file: "units/integrated-audit/opportunities.yaml", id: "ct-int-nonclient-drafting" }
scope: { name: "Audit: integrated audit ICFR testing", level: team }
owners: { business: "Integrated-audit manager", delivery: "Integrated-audit manager", support: null }
classification:
  { archetype: assurance, modules: [controls-testing], work_types: [document-production, research-synthesis],
    pattern: draft-review-loop, ladder: assist, ladder_target: null,
    change_scope: step, runtime_class: personal-assistant }
ai_use: null
sourcing: undecided
tools: ["Approved enterprise AI assistant (firm-enterprise-assistant; non-client material only; no tool-catalog.yaml yet, so no catalog entry)"]
vendor_evaluations: []
risk_tier: "tier-2"
status: in-progress
step_completed: 0
next_step: 1
updated: 2026-10-21
---

# Solution brief: Shared prompts and review routine on the approved assistant (integrated-audit drafting, non-client material)

<!-- Opened in discover as evidence for g1 (light path: g1 and g2 combined). Cases by type, source and id only. Owners are roles. Steps 1 and 2 are drafts from the portfolio item and the intake record; nothing in them has been confirmed by the business owner yet. -->

## Summary

Integrated-audit staff would draft test-step wording, narrative templates and junior practice cases with the approved enterprise assistant, using shared prompts and a senior's approval routine, on non-client material only. Today a few seniors do this on their own (reported, not verified). The case is small and uncertain: 0 to 0.2 staff hours per control test, on an assumption that 0 to 15% of the 1.5 h hands-on is template or wording work, with no measure (grade D). The `g0` Go rests on the cost being a routine, not a build.

**Where it stands.** The problem frame is drafted from the portfolio record. The benefit owner is named (integrated-audit manager, practice leader signs off) and the manager's time is set at about 4 hours a week for six weeks. The baseline will come from a sample of about ten recent control-test files, not time records; it is not yet taken, and a guess of about 1.5 h of a roughly 8 h test, in a slice outside the hands-on, is far above the 0 to 0.2 h range on the item, which covers the hands-on slice only. The sourcing leaning is to configure the existing assistant and build nothing, proposed only. The provisional risk tier is `tier-2`.

**Next.** Step 1: record the risk lead's view on reading past files, then run the file sample and have the owner confirm the metric.

## Progress

- [ ] 1 Frame the problem. Open: owner's confirmation of the metric; baseline sample (rule set, see §1) not yet taken, waiting on the risk lead's answer; last real instance walked through; volumes; informal AI use; rule or template baseline tried; risk lead's view on reading past client files for the sample
- [ ] 2 Build, buy or configure. Open: own-sample test not run; business owner has not confirmed the leaning; maintenance owner not named; tool catalog does not exist
- [ ] 3 Solution design
- [ ] 4 Evaluation plan (`eval-plan.md`)
- [ ] 5 Production readiness (`readiness.md`)
- [ ] 6 Launch and post-launch review (`post-launch.md`)

## 1. Problem frame

- **Started from:** portfolio item `ct-int-nonclient-drafting`, stage discover (`g0` Go, light path), from advisor option `ct-int-nonclient-drafting`. Duplicates and neighbours: `firm-enterprise-assistant` (the platform; this is a use of it) and `sox-chase-assistant` (similar use on the SOX-only line).
- **Problem statement (from the intake record, not yet in the owner's confirmed words):** help integrated-audit staff draft test-step wording, narrative templates and junior practice cases with the enterprise assistant on non-client material, so that template and wording time falls.
- **Business owner:** Integrated-audit manager (placeholder owner role), also the benefit owner; the practice leader signs off; confirmed the metric: not yet; reviews outputs: not agreed.
- **Success metric and baseline:** hours per template and wording slice (capacity lever), chosen by the portfolio lead as the work the tool would change; the whole control test of roughly 8 h is context only · baseline not yet taken. Time records cannot supply it (template and wording time has no booking code), so the method is a sample: the manager estimates template and wording time in the most recent ten completed control tests from the last twelve months, in date order, from the manager's own engagements, recording only case id and estimate. No cherry-picking; a file that cannot be read under the risk lead's conditions is skipped, listed by id with the reason, and the next one taken. Waiting on the risk lead's answer before any file is pulled. Limits: one manager's engagements, and self-estimated, so the result is a sample estimate (reported), checked by the practice leader at `g1`. Two reported figures exist on different slices of a whole control test of roughly 8 h: 0-15% of the 1.5 h hands-on (intake, 0 to 0.2 h per test) and about 1.5 h for template and wording outside the hands-on (portfolio lead's guess, about 19% of the whole test). The guess is kept as a guess; the sample decides whether the item's range was scoped too narrowly. A second lever, staff experience, has no metric yet.
- **The work today (last real instance):** not yet walked through. Known: a few seniors use the assistant on templates today (reported, not verified).
- **Volumes (last month or season):** not recorded · rework share not recorded · time per item not recorded.
- **Users and reviewers:** integrated-audit staff use the output; a senior approves templates before shared use; the professional accountable for any wording that enters a workpaper is the engagement team's reviewer.
- **Error costs:** client data pasted by mistake (costly, hard to undo); unreviewed wording entering workpapers (costly, caught at review if review is real). Neither is irreversible if the usage rule holds.
- **Fit checks:** rule or template baseline: a template library might cover part of it, not yet tried; AI adds most for synthetic practice cases · judgment, tangled rules or unstructured data: none apparent · intern test: not run.
- **Informal AI use today:** a few seniors already use the assistant on templates (reported). Whether anyone uses unapproved tools for this is not known.
- **Pattern and rung hypothesis:** `draft-review-loop` at `assist`. "Not when" checks: review volume exceeding reviewer capacity (clear at this volume, to confirm); drafting is the learning for juniors (applies to the practice cases, so juniors should critique drafts rather than receive finished ones; this is in the intake's role evolution); no baseline before launch (**open**, see above).
- **Constraints:** non-client material only; attest independence and client terms not engaged while no client data is used; `overlay/policy.md` is a draft.
- **Decision:** proceed to step 2 as a leaning only. Step 1 cannot close until the baseline and the benefit owner exist; the kill criteria agreed at `g0` say that gate fails without them.

## 2. Build, buy or configure

Proposed, not decided. No option has been run on the firm's own sample.

| Option | Fit to the workflow | Result on our sample | Total run cost (range) | Switching cost and exit | Data handling | Differentiation | Owner after launch |
|---|---|---|---|---|---|---|---|
| Template library and checklist, no AI | Covers wording and templates; does not produce varied practice cases | Not tried | Staff time to assemble; not sized | None | Non-client only | Low | Not named |
| `configure`: shared prompts, templates and an approval routine on the approved enterprise assistant | Fits where seniors already work | Not tested | No new licence (existing assistant); routine set-up and review time, not sized | Low: prompts and templates are portable text | Non-client only; assistant approved for non-client material | Low: general capability; the firm's own wording and templates are the asset | Not named |
| `build-on-model` or `build-custom` | Not needed for drafting by individuals | Not tested | Build plus maintenance; not warranted at 0 to 0.2 h per test | High relative to the benefit | Would add a data path | None | Not named |

- **Catalog check:** the approved enterprise assistant is in use and is described as approved for non-client material (`firm-enterprise-assistant`), but there is no `overlay/tool-catalog.yaml`, so no catalog entry to cite. Nothing outside it is proposed. **Decision (proposed):** `configure` on `personal-assistant`, at `assist`, because the capability is general, the value range is small and the lowest rung meets the stated need. A move to `shared-team-skills` would be a later choice if the shared prompts need versioning; it needs written evidence.
- **Maintenance:** not named. If nobody can be named, the advisor default is not to start. · **Revisit when:** the baseline shows template and wording time near zero; the assistant's terms or model change; the own-sample test shows reviewers finding client data or wording errors above what the owner accepts; usage spreads beyond one team.

## 3. Solution design

Not started.

## Decisions log

| Step | Decision | Reason | Decided by (role) |
|---|---|---|---|
| 2 | Leaning: configure the approved assistant; build nothing (`sourcing` stays `undecided`) | General capability, small value range, lowest rung meets the stated need; own-sample test and owner confirmation outstanding | draft (ai-solution-delivery) |

## Handoffs

| To | What | Status |
|---|---|---|
| ai-portfolio | `brief.md` now exists: set the item's `solution` to `solutions/ct-int-nonclient-drafting/`; the build-or-buy leaning (configure, proposed) and the open `g1` evidence rows | Handed back |
| ai-governance | Confirm provisional `tier-2` (`overlay/policy.md`, draft); no tool-catalog entry exists for the assistant | Not yet requested |
| ai-governance (risk lead) | Prerequisite for the baseline sample: view on the manager reading about ten past control-test files to estimate time, recording case id and estimate only | Requested by the portfolio lead; no answer yet |

## Open questions

- Will the benefit owner (integrated-audit manager) confirm hours per control test as the metric, and what does the practice leader sign off, the metric, the baseline or the release of time?
- The metric is hours per template and wording slice (decided); the owner's confirmation is still to be recorded. The item's value range is widened and re-based to the slice once the sample is in.
- **Prerequisite:** does the risk lead permit the manager to read about ten past control-test files to estimate time (record case id and estimate only)? The sample does not start before this is recorded.
- Volume: about 40 control tests a year is a placeholder guess from the portfolio lead; the integrated-audit manager confirms the count.
- Open dependency: the steering group has not set the live limit; the portfolio lead will propose a figure at the next agenda. A Go at `g1` waits on it.
- The practice leader's own confirmation of the manager's time (about 4 hours a week for six weeks) is not yet recorded; the figure comes from the portfolio lead.
- Which three non-client use cases, and who approves a template before shared use?
- Is the usage rule restated, and how would a mistaken paste of client data be detected?

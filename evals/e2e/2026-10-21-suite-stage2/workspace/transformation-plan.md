---
schema: plan/v1
scope: { name: "SOX/ICFR controls testing practice", level: business-unit, parent: null }
author: { name: "", role: "Audit partner, practice leader" }
profile:
  archetype: assurance
  modules: [ controls-testing ]
  journey_stage: curious
  goals:
    - "Protect margin under fee pressure without adding staff to absorb growth"
    - "Reduce inspection risk on ITGC evidence (two PCAOB comments last cycle)"
    - "Reduce turnover (~25%) by cutting busy-season overtime"
    - "Cut review-note rework (about 30% review-note rate, reported), which is where managers spend busy season"
    - "Keep real learning for junior staff; no plan that leaves them with nothing to learn from"
  constraints:
    - "No client data in the enterprise chat assistant"
    - "New client-data tools need risk and quality, CIO and general counsel sign-off: security review, data-handling and retention assessment, independence check (3-4 months; no controls-testing case has gone through yet)"
    - "PCAOB / independence rules; auditor stays accountable for the opinion"
  tools:
    - "Enterprise chat assistant (non-client material only)"
    - "Audit platform analytics module (mainly sampling)"
  session_goal: "A plan to take to firm leadership"
settings:
  value_levers:
    - { id: capacity, name: "Capacity", metric: "Staff hours per control test (written unit definition needed)", weight: 0.25 }
    - { id: quality, name: "Quality", metric: "Review-note rate (about 30% today, reported)", weight: 0.25 }
    - { id: risk, name: "Risk", metric: "PCAOB / internal inspection comments on ITGC evidence", weight: 0.20 }
    - { id: experience, name: "Staff experience", metric: "Busy-season overtime; share of junior time on judgment work", weight: 0.20 }
    - { id: cost, name: "Margin", metric: "Margin per fixed-fee program", weight: 0.10 }
  scoring_weights: { value: 0.30, feasibility: 0.20, data_readiness: 0.15, risk: 0.20, time_to_value: 0.05, strategic_fit: 0.10 }
  capacity_stance: redeploy
  guardrails:
    - "A person owns evidence selection, sufficiency conclusions, deficiency evaluation and sign-off"
    - "A senior or manager reviews every AI-flagged exception and a sample of unflagged items"
    - "Independence rules unchanged; client data only in approved tools"
    - "Every AI-assisted step traceable and reperformable, defensible to the PCAOB"
  overlay: null
units:
  - { id: sox-only-outsourcing, name: "SOX-only outsourcing (15 clients)", owner: "Practice lead", wave: 1, mode: same-user, status: in-progress }
  - { id: integrated-audit, name: "Integrated audit ICFR testing (about 60 clients)", owner: "Manager (to name)", wave: 2, mode: desk-review, status: desk-review }
status: complete
phase_completed: 7
next_phase: null
updated: 2026-10-17
---

# Transformation plan: SOX/ICFR controls testing practice

## Summary

**Ambition.** Within a year, the SOX-only outsourcing line runs a certified, AI-assisted evidence review workflow that cuts staff time per test and review notes, avoids repeat PCAOB comments on ITGC evidence, lowers busy-season overtime and gives juniors more judgment work, without weakening the human checks. The 40-person practice (about 60 integrated-audit clients, 15 SOX-only clients) is at Curious edging to Experimenting; AI touches no client evidence today.

**What we found.** The constraint is senior review capacity (seniors 90-95% booked in busy season); about 80% of the first 11 days on the sample test was waiting; about 20% of SOX-only tests draw an evidence-completeness note (tracking sheet, as relayed). The integrated-audit line, where a specialist validates each report once, shows the pattern (one case). Most of the fix is process, not AI.

**Chosen options.** (A) Evidence-completeness package: checklist, request template, validated-report register, starting with 4-5 clients. (B) Named junior-development workstream. (C) Narrow client-data approval request, with a certified comparison tool as a staged, conditional later item. Parked target pictures: AI secondary review, agent testing, platform-plus-review service model.

**What happens next.** Managers align on one answer to "Is my job safe?" and the practice lead sends a note to all 40 people; the practice lead holds the protected senior half-days and co-writes the checklist; the ITGC senior manager inventories and validates the first client, then back-tests the checklist blind; a monthly practice leadership review tracks note rate, hands-on hours per test and validation hours. Full detail in the Plan and Leadership summary sections.

## Progress

- [x] Onboard
- [x] Frame (levers, weights and redeploy stance confirmed by the user)
- [x] Map (SOX-only flow mapped in depth; integrated audit light, for contrast)
- [x] Diagnose
- [x] Reimagine
- [x] Prioritize (SOX-only unit; roll-up with the integrated-audit desk review still to do)
- [x] Make the case (three cases for the SOX-only unit; independent review run; stage 1 scoped to 4-5 clients)
- [x] Plan (SOX-only unit, wave 1; integrated audit is wave 2 and has only a desk review)

## Profile

You lead the whole SOX/ICFR controls testing practice: 40 people (4 managers, 10 seniors, 26 staff) covering about 60 integrated audit clients and 15 SOX-only internal audit outsourcing clients. Pressures are margin (fee pressure, cannot keep adding staff), inspection risk (two PCAOB comments on ITGC evidence last cycle) and retention (about 25% turnover, busy-season overtime a major driver). A few seniors use the enterprise chat assistant on non-client material only (a control narrative template, a summary of a PCAOB inspection release). The audit platform's analytics module is used mainly for sampling.

| Scope | Stage | Markers seen | Binding constraint |
|---|---|---|---|
| Practice | Curious, edging to Experimenting | A few named seniors use the assistant weekly-ish on non-client work (reported, not verified); usage rule exists (no client data); no owned workflow, baseline or measure; no AI in evidence review or documentation | Data access: no approved route for client evidence in any AI tool; no controls-testing use case has been through the 3-4 month approval path |

Path: Curious/Experimenting emphasis. Real examples with graded evidence, then one workflow with an owner, baseline and designed human check, with the approval path treated as the critical dependency. No delegated (agent) workflow planned: the five gates fail (no production workflow, no written criteria, no shadow mode). Both service lines (integrated audit, SOX-only outsourcing) to be mapped separately at Map.
Confidentiality reminder given: yes.
Corrections from the user at playback:
1. The 15 SOX-only outsourcing clients are probably the easier place to start: independence is simpler and the firm controls the workpaper format (reported; to test at Map).
2. Add the review-note rate, about 30% (reported, not from record; definition to confirm, e.g. share of workpapers or tests drawing a note). Review notes are a large part of rework and where managers spend busy season.
3. The plan must include something for junior staff: they need to keep learning (design requirement for role evolution, not an afterthought).
Numbers above are reported by the user, not from records.

## Frame

*Draft for the user to confirm. Numbers are the user's own, reported, not from records.*

**Ambition.** Within a year, the SOX-only outsourcing line runs a certified, AI-assisted evidence review workflow that cuts staff time per control test, cuts review notes, avoids repeat PCAOB comments on ITGC evidence, lowers busy-season overtime and gives juniors more judgment work, without weakening the human checks or the defensibility of the workpaper.

**Why now.** Fee pressure and no room to add staff for growth (margin); two PCAOB comments on ITGC evidence last cycle (inspection risk); about 25% turnover with busy-season overtime a major driver (retention). Field context: internal control testing is the largest single source of findings at the six largest networks (IFIAR 2025 survey, regulator-published, grade A).

**Success measures** (all targets are hypotheses to test against records at Map):

| Measure | Today | Direction / target | Who accepts it |
|---|---|---|---|
| Staff time per control test (unit to be defined in writing; not the same as KPMG's per-control figure) | about 1.5-2 hours (reported) | to about 1 hour on the pilot population | Risk and quality; finance for margin |
| Review-note rate | about 30% (reported; denominator to define) | under 20% | Practice lead; managers |
| PCAOB comments on ITGC evidence | 2 last cycle (reported) | no repeats | Risk and quality |
| Busy-season overtime | not yet measured | noticeably lower | Practice lead; HR data |
| Junior time on judgment work | not yet measured | higher share | Practice lead; staff interviews |
| Human check holds | no design yet | sign-off from risk and quality; override and miss rates tracked | Risk and quality |

**Standard of proof (user).** A measured baseline and a pilot comparison on actual workpapers (old and new run on the same controls), plus risk and quality sign-off that the human check holds.

**Value levers and weights.** Capacity 0.25, quality 0.25, risk 0.20, staff experience 0.20, margin 0.10. Quality and risk sit alongside capacity because inspection exposure and rework are the practice's stated pain, and because efficiency-only cases tend to score weaker than ones that pair efficiency with a quality or growth measure (self-reported survey association, WHARTON-2026).

**Scoring weights.** Defaults, except risk raised to 0.20 and time to value lowered to 0.05: the practice is inspection-exposed and the client-data approval alone takes 3-4 months, so early wins matter less than a defensible design. Reason confirmed by the advisor's heuristic, to be confirmed by the user.

**Pricing and capacity.** Fixed fee per annual program, set by key controls and locations; a few clients hourly. On fixed fee, saved hours become margin until renewal; on hourly clients, revenue falls with effort. The user expects some clients to ask for a reduction at renewal and wants to be upfront. Competitive-review fee cuts of 25-30% were reported by organizations that ran a review (FERF survey, self-reported, grade C); no independent evidence that AI has cut assurance fees at scale. Treat renewal behavior as an assumption to test.

**Capacity stance (provisional): redeploy.** Freed hours go first to lower overtime and review quality, then to absorbing client growth without adding staff, and to junior development. No reduction in staff headcount is planned. This is a statement about headcount only, not a commitment on fees: pricing, renewals and any fee reductions are separate decisions. To be settled per opportunity in Make the case.

**Guardrails.** A person owns evidence selection, sufficiency conclusions, deficiency evaluation and sign-off. A senior or manager reviews every AI-flagged exception and a sample of unflagged items. Independence rules unchanged; client data only in approved tools. Every AI-assisted step is traceable and reperformable.

**Owner and sponsor (roles).** Day-to-day owner: practice lead. The pilot working lead role was dropped by the user (the practice lead owns options 1 and 2; the ITGC senior manager owns the report register, validation and the checklist back-test). Senior sponsor: managing partner for assurance. The practice lead decides pilot scope, which SOX-only clients go first, review sample sizes and junior development design. Risk and quality, the CIO and general counsel must sign off on AI tool and data approvals, methodology and documentation standards, engagement letter language and how this is described to clients. The sponsor's own AI use and the dated review rhythm are still to be set (see Open questions).

**Hypotheses to test at Map (work as imagined).**
1. The 15 SOX-only outsourcing clients are the easier start (simpler independence; own workpaper format).
2. Review, not testing, is where rework and manager time sit (30% review-note rate).
3. The ITGC evidence comments came from evidence gathering or sufficiency documentation, not from testing logic.
4. Hours per test are about 1.5-2 and could reach about 1 with AI-assisted evidence handling.

**Map next.** The key-control testing flow on a recent SOX-only outsourcing program, from evidence request to sign-off, then the same flow on one integrated audit engagement for contrast, with ITGC evidence as a thread.

## Map

*In progress. SOX-only outsourcing line mapped from one recent case plus aggregate figures; integrated audit comparison still to do. All figures are the user's, relayed in conversation; the advisor has not seen the tracking sheet or any workpaper. No client-identifying data recorded.*

**Shared definitions (proposed, to confirm):**
- *Control test:* one control tested against its attributes for one period, as counted in the tracking sheet.
- *Review-note rate:* share of control tests drawing at least one senior review note (tracking sheet).
- *Hands-on time per control test:* staff hours from evidence in hand to workpaper ready for review (to be agreed whether the senior's review hours are included; track separately).
- *Elapsed time:* request-list item out to senior review finished (and again to final sign-off after rework).

### SOX-only outsourcing: quarterly ERP user access recertification (ITGC)

- **Customer:** the SOX-only client (and the client's external auditor, who may rely on the work; not yet asked).
- **Trigger:** annual test calendar; control owner's quarterly review completes; a request-list item goes out. *(stated)*
- **Output:** a reviewed workpaper with attributes ticked and a conclusion.
- **Volume, last month:** about 210 control tests, about 60 ITGC. *(from record: tracking sheet, as relayed; worst week not asked)*

| Step | Who (role) | Work type | Elapsed | Hands-on | Notes (label) |
|---|---|---|---|---|---|
| Request-list item out | Staff | coordination-scheduling | day 0 | not asked | stated |
| Wait for control owner's missing listing support | Client control owner | n/a | about 4 days | none | reported, one case |
| Pull user listing and reviewer sign-off from client portal; email control owner for gaps | Staff | coordination-scheduling, client-interaction | with the above | not asked | stated |
| Compare listing to active user population (terminated or role-changed users with access); confirm reviewer and sign-off date; test requested changes were made | Staff | review-assurance | about 2 days, spread | about 2.5 h total with writeup | reported, one case. Above the user's typical 1.5-2 h |
| Paste screenshots and extracts, write steps and conclusion, tick attributes | Staff | document-production | with the above | included | stated |
| Senior review queue, then review | Senior | review-assurance | about 5 days | not asked | reported |
| Fix review notes: re-run listing with parameters, tie sign-off date to policy deadline, trace removed-user exception to the revocation ticket | Staff, control owner | document-production, client-interaction | about 2 days | not asked | reported |
| Second round of senior review | Senior | review-assurance | not asked | not asked | "usually" (reported) |

**Totals (one case, reported):** about 11 days to first review finished, about 13 days to finish with rework. Staff hands-on about 2.5 h. Roughly 9 of the first 11 days were waiting (about 4 on the client, about 5 in the senior queue).

**Review notes (aggregate, from tracking sheet as relayed):** about 30% of control tests draw at least one note (about 63 of 210); about two-thirds of those (about 42, about 20% of all tests) are evidence completeness or IPE issues. The three notes on the sample case: listing lacked evidence it was complete and accurate (no report parameters or system-generated proof); reviewer sign-off date not tied to the policy deadline; one removed-user exception not traced to the revocation ticket.

**Tacit checks (not in any procedure; stated by the user):** the senior mentally checks that (1) the listing came straight from the system, not from something the control owner edited in Excel; (2) the report date range covers the whole period; (3) the active user population used for comparison is itself complete. Staff learn these by experience; the user says this is much of what separates a good senior from a new staff member.

**Systems:** client portal (evidence), the audit platform (analytics module used mainly for sampling), the firm's enterprise chat assistant (non-client material only), email. *(stated)*

**AI use today in this flow:** none. *(stated)*

**Hypotheses for Diagnose:**
1. Most rework traces to evidence completeness or IPE gaps that a written pre-review check could catch before the senior sees the file.
2. If the evidence-completeness notes disappeared, the note rate would fall from about 30% to about 10% (arithmetic on rough aggregates; assumes no overlap with other notes).
3. The 4-day client wait and the 5-day senior queue are bigger drivers of elapsed time than staff testing time.
4. The same gaps drive the PCAOB comments on ITGC evidence (to confirm with the user, without client detail).

### Integrated audit: same control type, for contrast (one recent case, reported)

Listing came from the client IT team through the audit platform's request portal. The IT audit specialist had tested the report parameters once for the whole engagement, so staff only compared the listing to active users and did not re-prove completeness per test. Staff hands-on about 1.5 h; no review notes; senior queue about 2 days (integrated team staffed more tightly in busy season). Volume for the integrated line not yet asked.

**Difference in structure (hypothesis, n=1 each):** in the integrated line completeness of the report is proven once and reused; in the SOX-only line there is no owner of report validation, IT audit specialists are billed to integrated engagements, and there is no shared place to keep a validated report, so every test starts over.

**Report-validation sizing (user estimates, reported; SOX-only line):** about 25 key controls per representative client; 12-15 rely on a system-generated report; about 8 distinct key reports per client after reuse; 3 h per report as a working default. 15 clients x 8 x 3 h = about 360 specialist hours for first-time validation. Sensitivity on the user's own inputs (6-10 reports, 2-4 h): about 180-600 hours. Excludes re-validation when a report or system changes and any coordination time. Specialist availability and scoping are open.

### Lookup and chasing versus judgment (user's own split, reported)

- **Mostly lookup, copying and chasing (staff):** pull listing from the portal; email the control owner for the right version; compare listing to the active user list; copy results into the workpaper template; format and tick-mark; follow up when the senior's note comes back. Work types: coordination-scheduling, client-interaction, data-reporting, document-production. The user guesses 60-65% of staff time falls here (reported estimate, not measured).
- **Judgment (mostly seniors and managers):** whether the listing is complete and system-generated; whether an exception is a real deficiency or a timing difference; deficiency severity. Work types: expert-judgment, review-assurance.
- **Advisor observation (inferred; confirm):** the first judgment item (completeness and system origin) sits with the senior at review, after staff have done the lookups. The three review notes on the sample case and about two-thirds of the notes in the tracking sheet are about exactly that item, so the judgment arrives late in the flow.
- **AI lead-in:** no AI is used on any of these steps today. Not asked whether anyone has tried one on a step.

### Units (Break down)

| Unit | Owner (role) | Wave | Planning mode (proposed) | Status | Brief |
|---|---|---|---|---|---|
| SOX-only outsourcing (15 clients) | Practice lead | 1 | Same user (practice lead goes deep) | In progress | units/sox-only-outsourcing/brief.md |
| Integrated audit ICFR testing (about 60 clients) | Manager, to name | 2 | Desk review (first pass, draft to validate) | Desk review done; awaiting review by an integrated-audit manager before it goes to the leadership team (user's requirement) | units/integrated-audit/desk-review.md, units/integrated-audit/opportunities.yaml |

Seam: client type and engagement model. Different owners of report validation (none in SOX-only; IT audit specialist in integrated), different independence profile, different workpaper-format control, same shared definitions (above).

**Gaps:** senior review hours; second-round review time; the worst week; whether the sample case is typical for non-ITGC tests; the integrated audit comparison; what the client's external auditor needs to rely on the work; where the audit platform's analytics sits in this flow.

## Diagnose

*Draft. Unit: SOX-only outsourcing (wave 1). All case figures are the practice lead's, reported, one case or aggregate from the tracking sheet as relayed. Integrated audit is covered separately in the desk review (draft to validate).*

**Constraint statement.** In busy season the constraint is senior review capacity: seniors run about 90-95% utilized (reported), carry roughly 25-30 workpapers each in the weeks the queue builds on top of their own testing (reported), and staff wait 3-5 days for a review note (reported). The next limit is the client wait for listing support (about 4 days on the sample case).

**Waiting versus working (sample case, reported).** Staff hands-on about 2.5 h against about 11-13 days elapsed, so flow efficiency is under 5%. Speed-up ceiling for the staff testing step: if it were twice as fast, end-to-end time improves by at most about 1.4% (about 2.5 h of about 90 elapsed hours; arithmetic on one case).

**Queue rule (illustrative arithmetic, not a measurement; assumes variability factor 1 and the same review time per file).** Waiting as a multiple of review time: 80% utilization, 4x; 85%, about 5.7x; 90%, 9x; 95%, 19x. At the seniors' reported 90-95%, a small change in review demand moves waiting a lot either way.

| Finding | Type | Evidence and label | Steps affected | Rough size |
|---|---|---|---|---|
| Senior review queue is the constraint in busy season | constraint | 90-95% utilization, 25-30 files each, 3-5 day waits (reported) | Senior review, second-round review | About 5 days of about 11-13 on the sample case |
| Wait on the control owner for listing support | waiting | About 4 days (reported, one case) | Evidence pull | About 4 days of about 11-13 |
| Completeness and system-origin of the listing is checked late, by the senior | rework / failure demand | About two-thirds of notes in the tracking sheet are evidence completeness or IPE (from record, as relayed); all 3 notes on the sample case were evidence or rule checks | Evidence pull, staff test, senior review | About 42 of about 210 tests a month (about 20%), each with about 2 more days and a second review round (reported) |
| Report completeness is re-proved per test; no one owns report validation | should-not-exist (per test) | SOX-only has none; integrated has a specialist-validated-once pattern (reported, one case each) | Evidence pull, test | Sizing: about 8 reports per client, about 360 specialist hours first time (user estimates; 180-600 h sensitivity) |
| Second-round notes squeezed into evenings and weekends | rework / people | Stated | Rework loop | Not measured; links to the overtime and turnover levers |
| Unwritten senior checks (system-generated, full period, complete population) | tacit knowledge | Stated | Senior review | Blocks any certified tool: no written criteria |
| Lookup, copy, format and tick-mark work | value-needed, low-judgment | User estimates 60-65% of staff time (reported guess, not measured) | Staff testing and documentation | About 1.5 h of the 2.5 h on the sample case, if the guess holds |

**Verification capacity.** Seniors and managers check all work; capacity is the constraint. More AI output in front of a 90-95% booked reviewer would lengthen the queue. Any option must reduce the number of files or rounds reaching the senior, or reduce time per file, before it raises output at the staff step.

**Should-not-exist test.** Re-proving report completeness on every test; chasing the control owner per test for the same report parameters; a second review round for gaps a staff self-check could catch.

**AI-fit table (candidate steps).**

| Step | Work type | Variance | Desire zone | Frontier test | Data readiness | Criteria written? | Human checks that must stay |
|---|---|---|---|---|---|---|---|
| Report completeness proof | review-assurance | Low once defined | Keep with people: routine, but where juniors learn what seniors look for (user) | Not done (client data barred; synthetic or non-client examples possible) | Not reachable until approval; no register | No (tacit) | Specialist signs validation; senior confirms |
| Pre-review evidence check | review-assurance | Low | Keep with people (same reason); a written checklist supports them | Not done | Not applicable (checklist) | No (tacit) | Senior samples checklist completions |
| Listing-to-active-user comparison | data-reporting | Low | Gladly hand over the first pass (user) | Not done | Client data needed; approval path 3-4 months | Partly | Every flagged exception reviewed; sample of unflagged |
| Portal pulls; copy into template; format and tick-mark | coordination-scheduling, document-production | Low-medium | Gladly hand over (user) | Not done | Client data needed | Partly (template exists) | Staff and senior review |
| Exception vs timing difference; severity | expert-judgment | High | Stays human (user: the timing-difference call is routine but a learning step) | n/a | n/a | No | Person decides and signs |
| Request and chase for listing support | coordination-scheduling | Low | Share with a tool: draft the request and track follow-ups; a person sends it and owns the relationship (user) | Not done | Client data; client portal | No | Staff send; control owner is external |

**Shortlist for Reimagine (steps, not tools).**
1. Senior review demand: fewer files and second rounds reaching the senior (the constraint). Lever: quality, experience, capacity.
2. Report completeness proof: validate once and reuse; write the three unwritten checks as criteria. Lever: quality, risk.
3. Evidence request and chase: get the right report and parameters first time. Lever: speed, capacity.
4. Listing comparison and write-up first pass, only after 1 and 2 and the approval path. Lever: capacity.
5. Junior development: how juniors keep learning the seniors' checks. Lever: experience.

**Design tension to resolve in Reimagine (from the user).** The completeness check and the timing-difference call are routine, and also where juniors learn what seniors look for, so the user does not want them automated away. Meanwhile the validated-once report pattern would move first-time completeness proof to a specialist. Likely resolution: a specialist validates the report once and records it; staff still run a short written check on every listing and the timing-difference call, with seniors coaching against the checklist, so juniors keep the learning while the repeated re-proving goes.

**Open items for Diagnose.** A frontier test on non-client or synthetic examples; the integrated-audit comparison on the same measures; whether the two PCAOB comments relate to the same gap; senior hours per file.

## Reimagine

*SOX-only unit. Stage: Curious edging to Experimenting, so lenses 1 and 2 in depth and lenses 3 and 4 as target pictures. Full detail in `units/sox-only-outsourcing/opportunities.yaml`. Evidence grades are from the archetype's use-case file; figures behind them are mostly self-reported or vendor-published and measure effort, not testing quality. Earlier remark corrected: the archetype grades use cases #05 and #06 as A (in production, named); the figures inside them remain self- or vendor-reported.*

| # | Lens | Option | Ladder / scope | Evidence | Decision |
|---|---|---|---|---|---|
| 1 | Improve | Written pre-review evidence checklist capturing the senior's unwritten checks | assist / step | tacit checks (user); #03, #10 | Kept |
| 2 | Improve | Request template naming the report and parameters up front, plus a rule-based check on arrival | assist / step | #03 (C) | Kept |
| 3 | Improve | Shared assistant drafts requests and tracks follow-ups; a person sends | assist / step | #03 (C) | Kept |
| 4 | Improve | One specialist validates each key report once; a register records it | assist / process | integrated-audit case (reported, one case) | Kept |
| 5 | Automate | Certified tool: portal pull, listing comparison, workpaper first pass; exceptions to a person | augment / step | #06 (A, self-reported), #07 (B) | Kept |
| 6 | Improve | AI secondary review before the senior | augment / step | #10 (B) | Dropped by the user; parked target picture |
| 7 | Improve | Named junior-development workstream | assist / process | assurance-quality-management-16 (B, vendor-published, one small firm); mixed evidence on junior effects. Corrected: #21 was cited in error | Kept; user wants a named workstream with its own owner |
| 8 | Delegate | Agent tests a defined control set, reviewer signs | delegate / process | #05 (A), #16 (B) | Dropped by the user; parked target picture; fails four of five delegation gates |
| 9 | Reinvent | Platform-plus-review service model or client in-sourcing | delegate / model | #20 (B), #19 (B) | Dropped by the user; parked hypothesis |
| 10 | Foundation | Take one controls-testing use through the client-data approval path | assist / process | none | Added by the advisor because options 3 and 5 cannot start without it; **confirmed by the user as a foundation item** |

**Prerequisites found:** written test attributes and exception rules; specialist capacity for report validation; client-data approval (3-4 months); a shared place for the register; senior coaching time in busy season; external auditor reliance for AI-assisted work (AS 2605, not yet discussed with the clients' auditors).

**AI-native competitor hypotheses (labelled hypotheses, not findings):** firms are repackaging testing as platform plus review (RSM Beacon, Riveron, Arden: #20, announced, grade B) and some clients are in-sourcing co-sourced testing to agents (#19, grade B). This line sits on the exposed side of both. No independent study of AI-native service firms was found.

## Prioritize

*Draft for the SOX-only unit; awaiting the user's choice of top options and the roll-up with the integrated-audit desk review. Scores use the plan's weights. Scoring is a facilitation device, not a validated model. All value figures are illustrative arithmetic on the practice lead's reported inputs.*

| Option | V | F | D | R | T | S | Weighted | Category |
|---|---|---|---|---|---|---|---|---|
| 1 Pre-review evidence checklist | 4 | 5 | 3 | 5 | 5 | 5 | 4.40 | foundation (data readiness lowered 4 to 3 after review: criteria still unwritten) |
| 2 Request template and arrival check | 3 | 5 | 3 | 5 | 5 | 4 | 4.00 | park with a trigger under the rules (data readiness 3: the per-client report list does not exist yet, so not a quick win); in practice it starts client by client as the report inventory completes |
| 7 Junior-development workstream | 2 | 3 | 4 | 5 | 3 | 4 | 3.35 | foundation by the user's decision (rules alone would park it: value 2). Reason recorded: it is a stated design requirement and the guard on the junior pipeline, and option 5 now depends on it |
| 4 Report validation register | 4 | 3 | 3 | 4 | 3 | 5 | 3.70 | big bet, staged (changed from foundation after review: only one option depends on it; validate one client first) |
| 10 Client-data approval path (added) | 2 | 3 | 3 | 4 | 3 | 4 | 3.00 | foundation by the user's decision (the category rules alone would park it: value 2, one dependent) |
| 3 Chase assistant | 2 | 4 | 3 | 4 | 4 | 3 | 3.15 | park (value 2); revisit after option 2 |
| 5 Certified listing tool | 2 | 2 | 2 | 3 | 1 | 3 | 2.25 | park until 1, 4 and 10 are done; kept in the sequence as Later (value lowered 3 to 2 after review) |
| 6, 8, 9 | | | | | | | | parked target pictures (user) |

**Rule notes.** "Park" means not now, with a trigger to come back; it does not mean dropped. Option 5 is kept in the plan because the user kept it, but the scoring rules park it: its value is capped by the constraint gate (it speeds a staff step, not the senior queue) and it fails feasibility and data readiness until criteria are written and approval is granted. Option 3 scores value 2 (low end zero).

**Overlap warning.** Options 1, 2 and 4 attack the same evidence-completeness notes (about 42 of 210 tests a month, about 20 of the 30 points of the note rate). Their quality values must not be added: combined ceiling about 20 points, which would take the note rate to about 10%. The target of under 20% needs roughly half of that to be caught (about 10 points of the 20).

**Sequence (by dependency, no dates).**
- **Start now:** option 1 (write the checklist in the two or three protected senior half-days in the shoulder weeks, none in peak); the key-report inventory and validation for the 4-5 clients behind the ITGC controls and the two PCAOB comments, first client first (option 4, about 4 hours a week outside peak by one senior manager on the ITGC side); option 7's owner (a senior manager, to be named) and baselines; option 10's request.
- **Next:** option 2 client by client as each report inventory completes; option 4 for the next clients if the first client's measured hours are in line (see go/no-go); option 3 only if chasing time stays material after option 2.
- **Later:** option 5 in shadow mode, running alongside manual work on past tests, once options 1 and 4 have baselines and option 10 is granted.
- **Parked:** options 6, 8, 9.

**Shared constraint.** Seniors (90-95% booked in busy season) are needed to write the checklist, coach juniors and review. Starting more than they can carry would worsen the queue the plan is trying to cut.

**Assumptions that would change the order.**
1. The share of evidence-completeness notes the checklist and register actually catch (and the real extra hours per note, which are not yet known).
2. Whether the specialist group can supply the reported 180-600 hours and keep the register current.
3. Whether the integrated-audit pattern is structural or just one case.
4. Whether clients ask for lower fixed fees once savings are visible (affects the margin lever, not the order of the foundations).

**User's choice for Make the case.** Case A: options 1, 2 and 4 as one evidence-completeness package. Case B: option 7 as its own workstream. Case C: option 10 (confirmed as a foundation) with option 5 as a staged item. The user can protect two or three senior half-days in the shoulder weeks before busy season for the checklist, not during peak.

**Roll-up with the integrated-audit desk review (to do after the user chooses).** The integrated desk review has a matching item (`ct-int-validated-report-register`) that overlaps option 4 and a checklist item that overlaps option 1. They will merge into single parent opportunities with `rolled_up_from` and no double counting; the integrated items stay labelled draft to validate.

## Make the case

*Draft cases for the user's chosen top options (SOX-only unit): A, the evidence-completeness package (options 1, 2, 4); B, the junior-development workstream (option 7); C, the client-data approval path with the listing tool as a staged item (options 10 and 5). Inputs from the practice lead are reported, not seen by the advisor. Figures marked [placeholder] are the advisor's assumptions to be replaced with records. Value figures are illustrative arithmetic, not forecasts. Capacity choice throughout: redeploy, with no reduction in staff headcount; this is a statement about headcount only and not a commitment on fees. An independent review (the optional `review-opportunities` check, one reviewer per case) has been run; its findings and what was and was not applied are listed under "Independent review of the cases" below. The user then made detailed decisions on each case (scope, owners, rates, scores, pace, option 2 and option 7); the cases are treated as confirmed with those changes unless the user reopens any.*

### Case A: Evidence-completeness package (options 1, 2, 4)

**Decision asked.** Approve one package: (1) a written pre-review evidence checklist co-written with seniors in two or three protected senior half-days in the shoulder weeks before busy season (none during peak); (2) a revised request template that names the report and parameters, with a simple arrival check; (4) a specialist-validated register of key reports for the 15 SOX-only clients. Test it first on past files, then on a subset of clients.

**Today (baseline and sources).**
- About 210 control tests last month, about 60 ITGC. About 30% drew at least one review note (about 63 tests); about two-thirds of those (about 42 tests, about 20% of all tests) were evidence completeness or IPE issues. *(from record: tracking sheet, as relayed)*
- Sample case (access recertification): about 2.5 h staff hands-on; about 11 days to first review finished, about 13 with rework; three notes. Integrated-audit contrast case: about 1.5 h, no notes, 2-day queue. *(reported, one case each)*
- Seniors about 90-95% utilized in busy season, 25-30 files each in peak weeks; second-round notes pushed to evenings and weekends. *(reported)*
- Two PCAOB comments on ITGC evidence last cycle. *(reported)*
- Not yet known: hours per note, hours per second-round review, senior hours per file, loaded cost per hour.

**Future.** Options 1, 2: `assist` / `step`. Option 4: `assist` / `process`. No AI is required; AI may help draft checklist wording on non-client material only. Staff run a short written check on every listing; the request names the report up front; a specialist validates each key report once and records it for reuse.

**Value (ranges).** Options 1, 2 and 4 attack the same evidence notes, so their quality values are not added.

| Lever | Metric | Low | High | Unit | Assumptions |
|---|---|---|---|---|---|
| quality | Test-level review-note rate | 5 | 15 | points off the 30% | Package catches 25-75% of the 20-point evidence-completeness pool; combined ceiling 20 points. The target of under 20% needs at least 10 points. Grade D: no published measure of this effect |
| capacity | Second-round senior reviews avoided | 10 | 32 | per month | 5-15 points x 210 tests a month; each noted test usually gets a second round (reported) |
| capacity | Senior review hours released | 5 | 32 | hours per month | [placeholder] 0.5-1 h per second-round review; replace with a time sample. Gross: the senior hours the package adds (checklist writing, sampling completions, confirming listings, re-performance samples) are not yet measured, so the net senior effect is unproven |
| capacity | Staff hours (report register) | 25 | 63 | hours per month | 100-126 of 210 tests rely on a system report (control share used as a proxy for test share); 0.25-0.5 h per test no longer spent re-proving completeness. High end capped at 0.5 h until a time sample exists: the 1.0 h gap between the 2.5 h and 1.5 h cases rests on two single cases and would be 50-67% of a typical 1.5-2 h test |
| risk | PCAOB ITGC evidence comments avoided | 0 | 2 | per cycle | Baseline 2 (reported, line of origin unknown). IFIAR counted 43 data and IPE findings at the six largest networks in 2025 (regulator-published, grade A for the category, not about this firm) |
| experience | Evening and weekend second-round work | not yet measured | | | Baseline to be taken before the pilot |
| capacity (elapsed time; speed is not a plan lever) | Elapsed days per affected test | 0 | 2 | days | Sample case: about 4 days waiting on the control owner plus about 2 days rework; up to about 42 tests a month |

**Where freed capacity goes.** Redeploy. Of the staff hours, assume 20-30% is absorbed [placeholder]; the rest goes first to cutting second-round evening and weekend work, then to junior coaching and keeping the checklist and register current, then to absorbing client growth without adding staff. Cashable: none planned. Because programs are fixed fee, freed hours lift margin only by letting the practice grow without hiring or by cutting overtime cost; they are not profit by themselves.

**Cost (first season, hours).**

| Line | Low | High | Source |
|---|---|---|---|
| Senior time to write and test the checklist | 6 | 24 | 2-3 half-days of 3-4 h (user-protected time; total or per senior, up to two seniors, to confirm) |
| Template and arrival check (practice lead) | 16 | 40 | [placeholder]; this line previously included the back-test, so it is likely lower: re-estimate |
| Checklist back-test (ITGC senior manager, blind), 2 h a week for 8 weeks | 16 | 16 | User estimate; budgeted separately from the 4 h a week of validation. At the blended USD 210 an hour (assumed to apply) USD 3,360 |
| Report validation, first time (one senior manager on the ITGC side, about 4 h a week outside peak) | 192 | 248 | User estimate: 24 h for the first client, 12-16 h for each of the other 14 as reports are reused (reuse untested). At the blended USD 210 an hour, counted as real cost because most of it displaces billable work: first client alone 24 h = USD 5,040; 6-8 clients 84-136 h = USD 17,640-28,560; all 15 clients USD 40,320-52,080 |
| Training | 20 | 60 | [placeholder] 40 staff x 0.5-1.5 h |
| Parallel run and comparison | 20 | 60 | [placeholder] |
| Re-validation when a report or system changes | not yet known | | To estimate from change frequency |
| Register hosting | existing tools | | To confirm; no tool catalogue exists |
| **Total (excluding re-validation)** | **about 270** | **about 448** | Narrowed from 240-780 (now includes the separate 16 h back-test) using the user's per-client hours; mostly validation time. Only the validation line is priced in dollars; the other lines have no rate yet |

**Pace check (the user's inputs do not fit together).** At about 4 hours a week, 8 weeks gives 32 hours: enough for the first client (24 h) and about half of a second, not 6 to 8 clients. Six to eight clients need 84-136 hours, which is about 21-34 weeks at 4 hours a week; all 15 clients need 192-248 hours, which is about 48-62 weeks (11-14 months) outside peak. To go faster the options are more hours a week, a second trained validator for routine reports, or fewer clients first (the ones behind the ITGC controls and the two PCAOB comments). Risk and quality must also confirm that a senior manager on the ITGC side can sign a validation record, since IT audit specialists are billed to integrated engagements and are not available to this line. Concentration check: the ITGC senior manager is validator, register owner and checklist back-tester (back-test budgeted separately: 2 hours a week for 8 weeks), so they carry about 6 hours a week for the first 8 weeks and 4 hours a week after; the pilot working lead role is dropped; the junior-workstream owner is a senior manager to be named and is not yet confirmed as a different person.

**Stage 1 scope (user's decision).** Start with 4-5 clients: the ones behind the ITGC controls and the two PCAOB comments. Validation hours: 24 for the first client plus 12-16 for each of the other 3-4, so 60-88 hours (USD 12,600-18,480 at USD 210 an hour), which is about 15-22 weeks at 4 hours a week outside peak. The 4 hours a week fits, but the calendar is four to five months of off-peak weeks, not 8 weeks. Stage 1 first-season cost across all lines is about 138-288 hours (checklist 6-24, template and arrival check 16-40 [placeholder], back-test 16, validation 60-88, training 20-60 [placeholder], parallel run 20-60 [placeholder]; the template line may be lower now that the back-test is separate). Stage-1 benefit is proportional to 4-5 of 15 clients: about 7-21 staff hours a month on the 25-63 range (possibly higher if these clients are ITGC-heavy; not known). Stage 1 is not designed to pay back; it is designed to produce measured hours per client and a direct answer for risk and quality from the back-test on the files behind the two PCAOB comments. A second trained validator for the routine reports is a later-phase option, not part of stage 1. Go/no-go for stage 2 (proposed; to be set before starting): measured hours per later client within 12-16 (or an explained reason why not); in these clients the evidence-completeness note rate falls against the same clients' prior period, with no rise in other note types or in re-performance disagreement; risk and quality accept the validation records and the validator role.

Payback in hours only (hours, not value), staff and senior shown separately, excluding quality, risk, re-validation and the staff self-check cost on every test. Once all 15 clients are validated, against staff hours alone (25-63 a month) the first-season cost of 254-432 h repays in roughly 4 to 17 months; netting the 20-30% absorbed share [placeholder] lengthens that to roughly 5 to 25 months. Because validation takes about 11-14 months at the current pace and benefits arrive client by client, payback measured from the start is longer than that; it has not been modelled further. Hour-for-hour payback also understates the time to repay: the cost hours are manager time at USD 210 and the benefit hours are staff time at a lower rate that has not been given. Senior hours released (5-32 a month, placeholder) are not counted, because the senior hours the package adds are not yet measured. The spend is staged: validate one client first (USD 5,040), time it, and go on only if the measured hours fit the 12-16 hour assumption for later clients.

**Risks and human checkpoints.** Risks: checklist becomes tick-box; validation goes stale when a report or system changes; specialist capacity; note rate falls because fewer notes are written, not because quality improved; reuse of a validation across periods weakens evidence if poorly scoped. Checkpoints: the senior manager on the ITGC side (the register owner, once risk and quality confirm the role can sign validations) signs each validation; staff confirm every bounced item and the practice lead (template owner) owns the call on disputed ones; a senior samples the confirmation that a listing is the validated report (sample size agreed with risk and quality, so it is not a per-test rubber stamp) and reviews every exception; risk and quality approve what a validation record must contain (AS 1215), the client-facing request template, and the scope in which a validation may be reused across periods (PCAOB AS 1105 reliability); the clients' external auditors are told in advance (AS 2605). An owner for the register and for re-validation triggers must be named. Quality guardrail: a second reviewer re-performs a sample of files, so a lower note rate cannot be achieved by lowering the bar.

**Role evolution.** Staff: repeat chasing and re-proving move away; a short self-check and keeping the per-client report list current are added. Seniors: late discovery of gaps shrinks; they coach against the checklist. Specialists: own validation and the register. The practice lead owns the checklist and the template; the ITGC senior manager owns the register and the pilot comparison. Juniors still run the completeness check on real files (see Case B). `capacity_use`: redeploy.

**Evidence.** Use cases #03 (grade C, piloting, vendor claim), #10 (grade B, qualitative), #06 (grade A, but an in-house change-management agent at one company's internal audit, self-reported; context only, not support for the register, which rests on the integrated-audit case alone, reported, n=1). No controls-specific published measure of a checklist effect exists; the main evidence is the practice's own tracking sheet and the integrated-audit contrast case (reported, n=1). Examples from the archetype measure effort, not testing quality.

**How we will know.**
- *Comparison.* First a back-test: apply the draft checklist to past files with known notes and count how many of the evidence notes it would have caught (no new cost). Then a staggered start on a subset of clients against the rest in the same quarter.
- *KPIs.* (1) Evidence-completeness note rate; (2) second-round senior reviews per month; (3) days from request to final sign-off; (4) staff hands-on hours per test from a timed sample; (5) evening and weekend rework hours. Quality guardrail: sample re-performance disagreement rate.
- *Horizon.* Leading indicators within about a month of starting; PCAOB outcome only visible next inspection cycle.
- *Go/no-go (proposed; practice lead to set before starting).* The back-test shows the checklist would have caught at least half of the evidence notes on at least ten past files; in the pilot the evidence-completeness rate falls by at least 5 points with no rise in other note types and no rise in re-performance disagreement. If not, revise the checklist before widening.

**Back-test protocol (proposed; for risk and quality).** (1) Freeze the draft checklist before anyone reads the PCAOB comments, so it is not fitted to the answer. (2) Risk and quality hold the comment details; the test runs on internal records and no client detail enters this plan. (3) A reviewer who has not read the comment text applies the frozen checklist to the original file as a staff member would have, and records for each checklist item whether it would have flagged a gap. (4) Compare with the inspector's stated deficiency and score each: caught, partly caught, not caught, or not an evidence-completeness issue. (5) Run the same checklist on files with no comment as negative controls, to see how often it raises a false alarm. (6) Repeat on the roughly 42 evidence-completeness notes from last month's tracking sheet, which gives a far larger sample than two comments. Limits: two comments is anecdotal; hindsight bias; a checklist item that would flag a gap does not prove staff will complete it correctly; if a comment is about sufficiency of testing and not completeness of the report, the answer is "not caught" and that is informative.

**Narrowing the specialist cost (proposed).** The 240-780 hour range is driven by three inputs not yet measured: key reports per client (count three representative clients), hours per report by report type (time one client's validation end to end, about 16-32 hours at 2-4 hours per report), and who does the validation (specialist group, or a trained senior for routine reports). Stage the spend: validate one client first and replace the 3-hour placeholder with a measured figure before committing the other 14; start with the reports behind ITGC controls and the two PCAOB comments. Value of the hours: opportunity cost = hours x realised rate (not standard rate) if they displace billable work, or the internal charge-out rate if charged between engagements; the rate and the specialists' free hours outside peak are the user's to supply (open).

**Assumptions to test first.** (1) Share of evidence notes the checklist catches (back-test). (2) Hours per note and per second-round review (time sample). (3) Key reports per client and specialist hours (count three clients). (4) Whether the integrated-audit pattern is structural, not one specialist's habit. (5) The evidence-note pool: which notes count as completeness or IPE (the sign-off-date and trace-to-ticket notes may not), and how many tests carry several notes; the 5-15 point range assumes little overlap. (6) The practice lead's "a few hours per client" for the specialist against the base estimate of about 24 hours per client (8 reports x 3 h): reconcile.

### Case B: Junior-development workstream (option 7)

**Decision asked.** Name a workstream with its own owner (by role) and protect senior coaching time, with baselines set now, so that tools and the checklist do not remove the learning.

**Today.** Juniors learn the seniors' unwritten checks (system-generated listing, full period, complete population) and the timing-difference call by doing them on real files (stated). 26 staff, 10 seniors. About 25% turnover, busy-season overtime a major driver (reported). Not yet measured: share of junior time on judgment work, overtime hours, reviewer-rated readiness.

**Future.** `assist` / `process`. (a) The checks are written down (Case A) so the learning is explicit; (b) juniors keep running the completeness check and the timing-difference call on real files; (c) explain-back: juniors explain any tool output back before it is used; (d) a rotating sample of listing comparisons stays manual even after a tool exists; (e) synthetic, non-client practice cases built with the enterprise assistant; (f) supervised stretch work, investigating exceptions under a senior; (g) protected senior coaching time.

**Value.** Experience lever, not converted to money: share of junior time on judgment work (target: higher, per the practice lead; value to set after a baseline), 12-month staff turnover (about 25% today, practice-level reported; no target set), busy-season overtime, reviewer-rated readiness at set checkpoints. I do not give a forecast. Evidence is mixed: a partner at one 20-person firm says first-year staff now do complex revenue testing because reviewers have bandwidth to guide them (assurance-quality-management-16: vendor customer story, vendor-published, archetype grade B, one small firm, not SOX testing); a registered PCAOB research proposal (HOLMSTROM-2024) warns that moving from preparing to reviewing may erode skill-building (a proposal, not a finding); in a vendor randomized trial of 52 engineers (coding, not audit) AI-assisted learners scored 17% lower on mastery, though those who asked conceptual questions kept more (ANTHROPIC-SKILLS-2026, as cited in the people-and-change reference). A separate independent working paper found junior employment about 9% lower after six quarters at firms adopting generative AI; that is about hiring, not learning, is not about audit or this firm, and belongs in the hiring-pace roll-up check, not in this case's evidence. Correction: earlier drafts cited use case #21 for this option and labelled the first-years claim "self-reported, grade C"; #21 is about SOX practitioners building agent evaluation sets, and the first-years claim is vendor-published, grade B.

**Where freed capacity goes.** This case consumes capacity: senior coaching time. Redeploy part of Case A's released senior hours to it.

**Cost.** [placeholder] Senior coaching 1-2 h per senior per month = 10-20 h per month; workstream owner 2-4 h per week; synthetic case set 20-40 h one-time; baseline measures 10-20 h. To replace after the owner is named.

**Risks and checkpoints.** Coaching time disappears in busy season; juniors only review and never prepare; explain-back becomes a box-tick; pipeline hollowing if hiring slows later (a roll-up check across units). Checkpoints: seniors review junior work on a rotating sample; the owner reports quarterly to the sponsor; no task juniors learn from is automated until a replacement learning route exists (junior-task audit: label each task production, training or both).

**Role evolution.** Tasks moving: mechanical preparation as tools arrive. New work: judgment practice, checklist upkeep, exception investigation, tool evaluation. Skills to build: reading report parameters and system logs as fluently as a ledger. `capacity_use`: redeploy.

**How we will know.** Baselines now; reassess at set checkpoints. Leading: coaching hours delivered, explain-back completion. Lagging: junior judgment-time share, readiness ratings, turnover. Go/no-go: the owner and protected time exist before any tool goes live in shadow mode.

**Independent review of this case (2026-10-17): ready with changes; decisions taken.** Evidence citation and provenance corrected above. Scores follow the reviewer: value 2 (the low end is zero), feasibility 3 and time to value 3 (protected senior coaching time is not secured while seniors are 90-95% booked), weighted 3.35. Under the category rules value 2 would park the option; the user's decision is to keep it as a named workstream. Reason recorded: it is a stated design requirement and the guard on the junior pipeline, and option 5 now depends on it. Owner: a senior manager (role; to be named by the user). Junior hiring pace: no change is assumed (user); the figures in this case do not depend on one.

**Assumptions to test first.** Which tasks juniors learn from today (production, training or both); how much coaching time seniors can actually give at 90-95% booking; whether staff see the workstream as development, not extra work.

### Case C: Client-data approval path (option 10) with the listing tool as a staged item (option 5)

**Decision asked.** Stage 0 only: open the client-data approval request now, scoped narrowly to listing-to-active-user comparison and workpaper first pass on user access recertifications at one or two clients, and prepare the written test attributes and exception rules. Stages 1-3 below are a conditional target picture with a revisit trigger, not an approval. Not a decision to deploy a tool. The decision on approval itself sits with risk and quality, the CIO and general counsel. The approval scope should name tool certification and monitoring under QC 1000, client consent and vendor terms, credential governance for portal pulls, and early notice to the clients' external auditors.

**Today.** No tool is approved for client evidence; no controls-testing case has been through the path (security review, data-handling and retention assessment, independence check; about 3-4 months). No tool catalogue exists, so options are described by runtime class (workflow automation), not by product. Staff time on lookup, copying and formatting is the practice lead's guess of 60-65% (reported, not measured).

**Future.** Option 5, `augment` / `step`. Stage 0 is the decision now; stages 1-3 each need their own decision, with gates set before each starts: (0) approval request and written test attributes and exception rules; (1) shadow mode on past tests with old-versus-new comparison on the same controls, no reliance; (2) limited live use on a few clients with every flagged exception and a sample of unflagged items reviewed by a person; (3) decide whether to widen. Delegating an outcome to an agent is not planned: it fails the delegation gates (no production workflow with owner and baseline yet, criteria unwritten, no shadow mode, no override tracking).

**Value (ranges), counted only after Case A is in place.**

| Lever | Metric | Low | High | Unit | Assumptions |
|---|---|---|---|---|---|
| capacity | Staff hours released | 24 | 126 | hours per month at full coverage; near zero for the first approved scope until widened | Coverage of 30-60% of 210 tests (63-126 tests) is a guess, not measured; releases 25-50% of a typical 1.5-2 h test (0.375-1.0 h) net of added review; before netting Case A, which removes 0.25-0.5 h from the same report-based tests; added review lands on seniors and is not netted here; absorption (assume 20-30%, placeholder) not yet applied. Grade C for this practice; pattern evidence is self-reported by the deploying teams (Microsoft internal audit reports 850 h and USD 185K a year from one ITGC agent; archetype grade A for the use case, effort not quality) |
| risk | Documentation traceable and reperformable | not quantified | | | Depends on design; must meet AS 1215 |

Constraint check: this speeds a staff step, not the senior queue, so it adds files to a queue that is already near full unless Case A has first cut senior review demand. Hence the staging.

**Evidence.** Use case #06 (archetype grade A) is a two-agent change-management ITGC tester at one company's in-house internal audit; the 850 h and USD 185K a year are self-reported by the deploying team and measure effort, not testing quality. It is not access recertification at an audit firm. #07 (grade B) has no controls-specific measure; its measured cases are tests of details. #05 (grade A) is an internal-audit agent under reviewer sign-off and is a target picture only. Treat the value range as grade C for this practice.

**Payback.** Known cost before a licence quote: roughly 80-180 hours [placeholder: approval pack 40-80 h, evaluation set and parallel running 40-100 h]. Licence, consumption and firm-side review effort are unknown, so no payback range can be given yet. The first approved scope is narrow, so early release is near zero; the case is about unlocking the option, not about the first season.

**Where freed capacity goes.** Redeploy, as in Case A. If clients later ask for lower fixed fees once savings are visible, the practice's stated position is to be upfront; engagement letter language and how this is described to clients need sign-off from risk and quality, the CIO and general counsel.

**Cost.** [placeholder] Approval pack preparation 40-80 h from the practice lead; firm-side security, data and independence review effort unknown; evaluation set with planted exceptions and parallel running 40-100 h; training; tool licence and consumption unknown (no catalogue or quote); re-certification whenever the model or tool changes. The reviewer time is already netted out of the capacity line.

**Risks and human checkpoints.** Automation bias and rubber-stamp review; non-repeatable output; documentation that does not meet AS 1215; reliance on others' work (AS 2605) and what the clients' external auditors will accept; tool or model changes breaking certification; instructions hidden in client evidence; security: private client data plus untrusted content plus any way to send data out must not coexist, so design out the outbound leg. Checkpoints: a senior or manager reviews every flagged exception; a senior samples unflagged items, with the sample size agreed with risk and quality; override and miss rates tracked and reported to risk and quality; risk and quality sign off the documentation before live use; a pre-agreed minimum number of planted exceptions must be caught in shadow mode before any live use; the clients' external auditors told in advance. Junior effect: a rotating manual sample of comparisons stays with juniors (sample size set in Case B).

**Role evolution.** Tasks moving: portal pull, comparison, copying, formatting, tick-marking first pass. New work: exception investigation, sample re-performance, evaluating the tool against planted exceptions. Juniors keep a rotating manual sample (Case B). `capacity_use`: redeploy.

**How we will know.** Shadow-mode agreement between tool and manual results on the same past tests; share of planted exceptions caught; override rate; hands-on hours per test from a timed sample; review-note rate for the same controls under both methods. Go/no-go for each stage set with risk and quality before it starts (proposed: no missed planted exception that a person would have caught).

**Assumptions to test first.** How long approval really takes and what scope it will accept; which control types are covered (30-60% is a guess); hours per test saved net of review; whether clients' external auditors will accept the work.

### Independent review of the cases (one reviewer per case, 2026-10-17)

Verdicts: Case A, ready with changes; Case B, ready with changes; Case C, ready with changes. The advisor checked the reviewers' key citations against the archetype files before applying anything.

**Applied (factual corrections and rule-based changes).**
- Case B evidence: use case #21 was cited in error (it is about SOX practitioners building agent evaluation sets). The first-years claim is assurance-quality-management-16, vendor-published, one 20-person firm, archetype grade B. The earlier label "self-reported, grade C" was wrong. The 9% junior-employment statistic is about hiring, not learning, and was moved out of the evidence.
- Case A staff-hours ceiling lowered from 125 to 63 hours a month (0.5 h per test cap) because the 1.0 h figure rests on two single cases; payback recalculated, separated by staff and senior, and widened to roughly 4 to 31 months on staff hours alone (5 to 45 netting absorption); the earlier "2 to 26 months" mixed staff and senior hours and assumed full benefit from month zero.
- Option 4 (report register) recategorised from foundation to big bet: only one option depends on it, so the foundation rule does not apply; its evidence field is now empty, resting on the integrated-audit case alone.
- Option 1 data readiness lowered 4 to 3 (criteria unwritten): weighted 4.40, still a foundation.
- Option 10 data readiness lowered 4 to 3 (weighted 3.00), its dependency on the checklist recorded, and the claim that options 3 and 5 both need it corrected: option 3 can start on placeholder text. The category rules would park it (value 2, one dependent); it stays a foundation by the user's decision.
- Option 5 value lowered 3 to 2 (weighted 2.25, still park); value range rebased on a 1.5-2 h test (24-126 hours a month at full coverage, near zero for the first approved scope); decision asked in Case C reduced to stage 0 only.
- Checkpoints named by role and expanded (QC 1000 certification, client consent and vendor terms, credential governance, external auditor notice under AS 2605, sample sizes agreed with risk and quality, minimum planted exceptions). "Speed" removed as a lever name in Case A.

**Not applied; needs the user's decision.**
1. Option 7 scores. The reviewer suggests value 3 to 2 (the low end is zero), feasibility 4 to 3 and time to value 4 to 3 (protected coaching time is not secured). Value 2 would park it under the rules; the user may keep it as a named workstream with the reason recorded.
2. Option 2 data readiness. The reviewer suggests 4 to 3 unless the per-client report list is already available; at 3 it loses quick-win status (weighted 4.00).
3. Whether the plan assumes any change to junior hiring pace (none is assumed in any figure).
4. Who approves and who supplies the specialist hours; the owner of the register and of re-validation triggers; the realised or internal rate for those hours.
5. The reviewer's note that the "few hours per client" (user) and about 24 hours per client (8 reports x 3 h) do not match.

**Update after the user's answers (2026-10-17).** (1) Validator and register owner: one senior manager on the ITGC side (a role, one of the four managers), about 4 hours a week outside peak, USD 210 an hour blended, counted as real cost; per-client hours 24 for the first client and 12-16 for later ones (user estimates, reuse untested). First-season cost narrowed to about 254-432 hours (from 240-780); validation alone 192-248 hours, USD 40,320-52,080 for all 15 clients. (2) Pace: the user's 4 hours a week for 8 weeks covers about 1.5 clients, not 6 to 8; see the pace check in Case A. (3) Option 2 data readiness set to 3 (the per-client report list does not exist), so it is no longer a quick win; it starts client by client after the report inventory. (4) Option 7 kept as a named workstream (decision recorded above). (5) No change in junior hiring pace. Still open: the staff loaded rate for valuing the benefit hours; whether the register owner and the junior-workstream owner are different people (the pilot working lead role was dropped by the user); risk and quality's view that a senior manager can sign validations.

### Portfolio view (SOX-only unit)

| Measure | Today | User's target | What the cases contribute |
|---|---|---|---|
| Staff hands-on per control test | about 1.5-2 h (reported; sample case 2.5 h) | about 1 h | Package alone: about 0.1-0.3 h off the average across all 210 tests (48-60% report-based x 0.25-0.5 h). Tool alone: about 0.1-0.6 h (30-60% coverage x 0.375-1.0 h on a 1.5-2 h base). Not additive: both attack lookup and compare work; even if they were, the ceiling is about 0.9 h. Reaching about 1 h from 1.5 h needs about 0.5 h, in the upper half of the combined range; from 2 h it needs 1.0 h, which is beyond what these cases support. Treat 1 h as a stretch target until a time sample and the pilot say otherwise |
| Review-note rate | about 30% | under 20% | Package: 5-15 points. Needs at least 10 |
| PCAOB ITGC evidence comments | 2 last cycle | no repeats | Hypothesis: 0-2 avoided; not proven |
| Busy-season overtime | not yet measured | noticeably lower | Baseline first |
| Junior judgment share | not yet measured | higher | Baseline first (Case B) |

Overlap rules: Cases A and C do not both bank the same hours; the integrated-audit register item is merged with option 4 at roll-up and stays labelled draft to validate.

## Plan

*Draft for the SOX-only unit (wave 1). Steps are ordered by what they depend on, not by dates. Owners are roles. "User" marks something the practice lead said; "proposed" marks the advisor's suggestion.*

### Now, Next, Later

**Now (none needs anyone else's approval).**
0. People first (user): each manager gives the practice lead a one-sentence answer to "Is my job safe?"; they align on one answer; the practice lead sends the note below to all 40 people the week before the checklist work starts. *Owner: practice lead.* The scheduling in step 1 can happen now; the checklist writing itself starts after the note has gone out.
1. Schedule and hold the two or three protected senior half-days in the shoulder weeks (none in peak) and co-write the pre-review checklist with two seniors. *Owner: practice lead (user: will schedule this week).* Option 1.
2. Take baselines from the tracking sheet and write the definitions down: control test, review-note rate, hands-on hours per test, elapsed time. Have two people classify the same ten notes as completeness or IPE or not, to test the definition. *Owner: ITGC senior manager (brings the numbers to the monthly meeting).* Proposed.
3. Time sample: hands-on hours per test on about ten tests, senior review hours per file and per second-round review, to replace the placeholders. *Owner: ITGC senior manager.* Proposed.
4. Inventory the key reports for the 4-5 stage-1 clients (the ones behind the ITGC controls and the two PCAOB comments), then validate the first client and time it, at about 4 hours a week outside peak. *Owner: ITGC senior manager, who is also register owner (user).* Option 4.
5. Open the client-data approval request with a narrow scope (user access recertification listing comparison, one or two clients) and agree the scope; the evidence pack waits for the checklist. *Owner: practice lead initiates; the decision sits with risk and quality, the CIO and general counsel.* Option 10.
6. Ask risk and quality whether a senior manager can sign a validation record and what a record must contain. *Owner: practice lead (user: will check).*
7. Name the junior-development workstream owner (a senior manager) and take its baselines. *Owner: practice lead (user: will name the owner).* Option 7.

**Next (once the Now steps are done).**
8. Freeze the checklist, then run the back-test: the ITGC senior manager applies it blind to the original files behind the two PCAOB comments, mixed in with files that drew no comment and with a slice of last month's tracking-sheet notes, without reading the comment text. Risk and quality hold the comment details and supply the files. 2 hours a week for 8 weeks, budgeted separately from validation (user). *Depends on 1.* One-off result reviewed in the monthly meeting (user). The practice lead then shares the measured results with all 40 people (user: the note promises this).
9. Validate the other 3-4 stage-1 clients (12-16 hours each is the user's assumption; the first client's measured hours test it). *Depends on 4.*
10. Request template: draft client by client as each inventory completes, then test it on the next two requests per client. *Owner: practice lead. Depends on 4's inventory.* Option 2.
11. Pilot the checklist and template on the stage-1 clients and compare with the same clients' prior period. *Depends on 1, 4's inventory and 10.*
12. Start the junior-development routine: written checks in use, explain-back, synthetic non-client practice cases, protected coaching time, a rotating manual sample once any tool exists. *Owner: junior-workstream owner. Depends on 1 and 7's baselines.*
13. Submit the approval evidence pack with written attributes and exception rules. *Owner: practice lead. Depends on 1.*
14. Before any validation is relied on across periods, get risk and quality's view of the reuse scope (AS 1105) and tell the clients' external auditors in advance (AS 2605). *Owner: practice lead. Depends on 6.*
15. Go/no-go for stage 2 at the monthly meeting, using the criteria in Case A (measured validation hours, the evidence-completeness note rate in the stage-1 clients, back-test result, risk and quality's acceptance of the records and the validator role).

**Later (once foundations are in place).**
16. Stage 2: validate the remaining clients; add a second trained validator for the routine reports (user: next phase).
17. Option 3 (chase assistant) only if chasing time is still material after the template.
18. Option 5 (listing tool): shadow mode on past tests with planted exceptions and old-versus-new comparison on the same controls, only after the approval is granted and options 1, 4 and 7 are in place; no live use without risk and quality's sign-off. Stages 1-3 each need their own decision.
19. First written value review against the cases; re-check the journey stage; revisit the parked options 6, 8 and 9 at the mid-point reset.

### Control plan for each live opportunity

Normal ranges for unmeasured items are set from the first four weeks of data and shown on a control chart before reacting to one month.

| Opportunity | Metric | Baseline | Normal range | Owner | Rhythm | If out of range |
|---|---|---|---|---|---|---|
| Option 1 checklist | Evidence-completeness note rate (share of tests) | About 20% (42 of 210; tracking sheet, as relayed) | Set after four weeks; direction down | Practice lead | Monthly | Check checklist use on a sample; revise wording; do not widen |
| Option 1 checklist | Back-test catch rate on the evidence notes | None yet | Proposed gate: at least half caught on at least ten past files | ITGC senior manager | One-off, then reviewed monthly | Revise the checklist and re-run before widening |
| Option 2 template | Wrong-first-time requests; days waiting on the control owner | About 4 days on the sample case (reported) | Set from the first clients | Practice lead | Monthly | Revise the template wording; check the report list with the control owner |
| Option 4 register | Validation hours per client | 24 first, 12-16 later (user assumption) | Within 12-16 for later clients | ITGC senior manager | Monthly standing item | Stop widening; find why reuse is not working |
| Option 4 register | Validations stale after a report or system change | None yet | Zero relied on after a change without re-validation | ITGC senior manager | Each engagement | Withdraw that validation; re-validate; tell risk and quality |
| Packages 1, 2, 4 | Overall review-note rate; hands-on hours per test | About 30%; about 1.5-2 h (reported) | Set after four weeks | ITGC senior manager | Monthly standing item | See above |
| Guardrail | Re-performance disagreement on a sample of files; other note types | Set in the first sample | No rise | Practice lead | Monthly | Stop and find the cause, since a lower note rate may mean fewer notes written |
| Option 7 workstream | Coaching hours delivered; explain-back done; junior judgment-time share; overtime; turnover | Judgment share and overtime not measured; turnover about 25% (reported) | Set from baselines | Junior-workstream owner | Monthly | Protect coaching time before any tool goes live |
| Options 10 and 5 | Approval stage reached; planted exceptions caught; override and miss rates; hours per test under both methods; monthly run cost | None yet | Written promotion thresholds with risk and quality before each stage | Practice lead (approval); ITGC senior manager (shadow results) | Per stage | Demote or stop; re-run the evaluation set when the tool or model changes |

**KPIs and benefit tracking.** Three to five per opportunity, each efficiency measure paired with a quality guardrail. Report realized against expected: every figure is "expected" until measured, and nothing in a cost line is banked as cashable. Activity (clients inventoried, validations done) is a leading indicator only.

### Rhythm

- **Monthly practice leadership meeting** (the practice lead and the four managers, user). The ITGC senior manager brings the numbers. Standing item each month: review-note rate, hands-on hours per test and validation hours. The back-test result is a one-off review when it is done (user).
- **Proposed:** a 15-minute weekly check between the practice lead and the ITGC senior manager while stage 1 runs; a written quarterly value review to the managing partner (the sponsor) against Cases A, B and C; a mid-point reset after stage 1 results (re-plan, fund what worked, stop what did not).
- **Re-test triggers:** re-validate a report whenever the report or its system changes; re-run any tool's evaluation set whenever the tool or model changes.

### People and change plan (draft)

- **Capacity choice:** redeploy. No reduction in staff headcount is planned, and no change in junior hiring pace is assumed (user). This is a statement about headcount only and not a commitment on fees.
- **Roles evolving:** staff move from repeat chasing and re-proving to a short self-check and exception work; seniors from late discovery of gaps to coaching; the ITGC senior manager adds validation ownership; juniors keep the completeness check and the timing-difference call.
- **Junior pipeline:** the junior-task audit (production, training or both) comes before any task is automated; explain-back on tool output; a rotating manual sample; protected coaching time (Case B).
- **Manager readiness (user):** each manager gives the practice lead a one-sentence answer to "Is my job safe?" and they align on one answer before the note goes out.
- **What staff are told and when (user):** a "what we know, what we don't, what we commit to" note to all 40 people the week before the checklist work starts. It says plainly that staff are not being cut and that junior hiring pace is not changing; that nobody yet knows how much time this saves; and that the measured results will be shared after the back-test.
- **Wording check (advisor).** Commit only to what is real and funded. Say "as part of this work" and say when the statement will next be reviewed; confirm the managing partner stands behind the headcount and hiring lines for that period. Do not let the note imply anything about fees. Do not promise results; the figures are expected, not measured.
- **Draft note (for the user to edit).**
  > **What we're trying in SOX/ICFR testing, and what we don't know yet.** We're under fee and inspection pressure, and rework in review is a big part of busy-season overtime. We want to fix the causes of rework, starting with three things: a written checklist for the evidence checks our seniors do from experience, a clearer evidence request to clients, and a record of reports we have already validated.
  > **What we know.** A large share of review notes are about evidence completeness, and some of our work already runs better where a report is validated once and reused.
  > **What we don't know.** How much time this will save, and how much it will cut review notes. We will test it on a few clients and on past files, and we will share the measured results after that test.
  > **What we commit to.** This work is not a headcount reduction: we are not cutting staff as part of it and we are not changing how many juniors we hire. Juniors will keep learning the checks on real files.
  > **What we need from you.** Tell us where the checklist is wrong or unclear. Questions go to me or to your manager.
- **Training by role:** staff, a short session on the checklist and the template on their own tasks; seniors, coaching against the checklist; the ITGC senior manager, the validation record. Hours are placeholders in Case A.
- **People indicators:** quality of AI-assisted work, use by group, manager confidence, junior learning (judgment-time share, readiness ratings), overtime, turnover.

### Next journey stage and exit criteria

The practice is at Curious edging to Experimenting, and most of this plan is process change, not AI. Next stage: **Experimenting**. Three observable exit criteria (proposed):
1. Named people use the enterprise assistant weekly on real, non-client work for agreed uses (for example checklist wording, request drafts on placeholder text and synthetic practice cases), counted in a log, with the acceptable-use rule restated.
2. One quick win has been shown to peers with its numbers (the back-test result, or the first client's measured validation hours).
3. The evidence-completeness package has a named owner, a baseline, a designed human check and risk and quality's sign-off on the validation record.

The step after that, Experimenting to Adopting, needs one workflow with an owner, a baseline, a designed human check and an approved tool (option 10 granted); a delegated workflow stays a target picture until all five delegation gates hold.

## Leadership summary

*Pasteable. Figures come from the practice lead (one sample case and tracking-sheet aggregates as relayed); none has been independently verified, and all benefits are expected, not realized. No client data is included.*

**SOX/ICFR controls testing: where AI and process change could help, and what we are asking for**

**Where we are.** The practice (40 people; about 60 integrated-audit clients and 15 SOX-only outsourcing clients) is under fee pressure with no room to add staff, had two PCAOB comments on ITGC evidence last cycle, and has about 25% turnover with busy-season overtime a major driver. AI does not touch client evidence today; client data is not allowed in the enterprise assistant, and a client-data tool needs a 3-4 month approval that no controls-testing use has been through.

**What we found.** On the SOX-only line, about 210 control tests a month; about 30% draw a review note, and about two-thirds of those are evidence completeness or reliability of the listing (about 20% of all tests). On one sample test, about 2.5 hours of staff work sat inside 11-13 elapsed days, mostly waiting on the client and in the senior review queue. Seniors run 90-95% booked in busy season, so that queue is the constraint. One integrated-audit case, where a specialist validates a report once and it is reused, took 1.5 hours with no notes and a 2-day queue.

**What we propose.**
- **A. Evidence-completeness package:** a written pre-review checklist that captures the checks seniors do from experience; a request template that names the report and parameters up front; a register of reports validated once and reused. Mostly process change, no AI needed. Start with the 4-5 clients behind the ITGC controls and the two PCAOB comments.
- **B. A named junior-development workstream,** so juniors keep learning the checks that a checklist or tool might otherwise take away.
- **C. Take one narrow use through the client-data approval path,** with a certified comparison tool as a staged, conditional later step that starts in shadow mode. Nothing here deploys a tool.

**What it could be worth (ranges; expected, not realized).** Review-note rate down 5-15 points from 30% (the under-20% target needs at least 10). 10-32 fewer second-round senior reviews a month. 25-63 staff hours a month once all 15 clients are covered. The 1-hour target for hands-on time per test (from 1.5-2 hours) is a stretch: the cases support roughly 0.1-0.9 hours off the average at best. 0-2 PCAOB ITGC evidence comments avoided per cycle is a hypothesis. Published examples in this field are mostly self- or vendor-reported and measure effort saved, not testing quality.

**What it costs.** About 270-448 hours in the first season across everything, of which first-time report validation is 192-248 hours (USD 40,320-52,080 at USD 210 an hour, counted as real cost because it displaces billable work). Stage 1 is about 138-288 hours: validation USD 12,600-18,480, about 15-22 weeks at 4 hours a week outside peak. Some lines are placeholders, flagged in the plan; the benefit hours have not yet been priced.

**How we will know.** A blind back-test of the checklist on the files behind the two PCAOB comments, mixed with files that drew no comment (2 hours a week for 8 weeks, run by the ITGC senior manager); a pilot on the stage-1 clients against the same clients' prior period; a quality guardrail of sample re-performance; a monthly standing review of note rate, hands-on hours per test and validation hours. Stage 2 goes ahead only if measured hours per later client, the evidence-completeness note rate and risk and quality's acceptance of the records all hold.

**What we are asking for.**
1. *Risk and quality:* confirm that a senior manager on the ITGC side can sign a validation record and what the record must contain; approve the checklist, the request template and the scope in which a validation may be reused across periods.
2. *Risk and quality, the CIO and general counsel:* consider a narrow client-data approval request (stage 0 only): user access recertification listing comparison at one or two clients.
3. *The managing partner (sponsor):* protect two or three senior half-days in the shoulder weeks (none in peak) and take a quarterly value review.
4. *Finance:* an internal rate to value the staff hours released, and confirmation that manager hours displaced from billable work count as cost.

**What we commit to, and what we do not.** Freed capacity is redeployed to lower overtime, review quality, junior development and growth without adding staff. We are not planning to reduce staff headcount as part of this work and are not changing junior hiring pace. This is a statement about headcount, not a commitment on fees; some clients may ask for reductions at renewal and we intend to be upfront. We have not discussed AI-assisted work with the clients' external auditors; that happens before any validation is relied on across periods or any tool is used.

**Main risks.** Evidence rests on single cases and relayed aggregates; the 1-hour target may not be reachable; specialist-type validation depends on one senior manager at about 4 hours a week; a lower note rate could mean fewer notes written, so a re-performance sample is the guardrail; seniors are already the constraint. The integrated-audit unit has only a desk review, labelled draft to validate, and goes to an integrated-audit manager before leadership sees it.

## Open questions

- Plan owners recorded so far (roles): options 1 and 2, practice lead (user), who will schedule the protected senior half-days this week; the ITGC senior manager validates the checklist against past files (back-test) and is also the register owner and validator at about 4 hours a week. Concentration and capacity check: the back-test hours come out of the same 4 hours a week as report validation unless budgeted separately, which lengthens stage 1; the back-test must stay blind to the PCAOB comment text. (Resolved: the back-test is budgeted separately at 2 hours a week for 8 weeks, planned blind, and the "pilot working lead" role is dropped.)
- Staff loaded or internal rate, to value the benefit hours (the validation cost is priced at USD 210 an hour, the benefit hours are not).
- Are the register owner (ITGC senior manager) and the junior-workstream owner different people? Both are senior managers, who also review, and seniors are already the constraint.
- Does risk and quality accept a senior manager on the ITGC side as the signatory of a validation record? And is 4 hours a week the real capacity, given the 6-8 clients in 8 weeks does not fit (about 32 hours)?
- (Answered: validator and register owner, rate, option 2 data readiness, option 7 decision, junior hiring pace. See the update under "Independent review of the cases".)
- How much does the senior sponsor use AI personally, and what dated review will hold this plan to account?
- Review-note rate (~30%): what is the denominator, which note types dominate, and does it differ between the two lines?
- Is SOX-only outsourcing really easier? Check the engagement letters (reliance, who owns the workpaper format) and whether the external auditors of those clients will rely on AI-assisted work.
- Junior development: which tasks do staff learn from today (tick-and-tie, walkthroughs, evidence follow-up), and which would AI take first?
- Stage placement is inferred from one conversation; verify who actually uses the assistant, how often (reported, not from record).
- Hours per control, review notes and ITGC evidence rework: no baseline yet; ask for records.
- What the two PCAOB comments on ITGC evidence were about, in the user's words, without client detail.
- Does the audit platform vendor offer AI features already covered by the firm's approvals?
- How fees differ between the integrated-audit and SOX-only outsourcing lines, and what happens to revenue if testing takes half the effort.

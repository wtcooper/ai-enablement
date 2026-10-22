# Intake: Named junior-development workstream: juniors keep the completeness check and the timing-difference call

| Field | Entry |
|---|---|
| Id | `sox-junior-development` |
| Submitted by | SOX/ICFR practice lead (placeholder owner role; the plan's practice lead will name the workstream owner), Audit: SOX-only outsourcing |
| Source | `units/sox-only-outsourcing/opportunities.yaml` → `sox-junior-development` |
| Status | Ready to screen. Imported after the advisor skill quoted the title, which had broken the file. The owner role has no holder yet (see Owner and benefit) |

## The problem in one sentence

Help juniors keep learning the seniors' unwritten checks by running the completeness check and the timing-difference call on real files, coached against the checklist, so that the share of junior time on judgment work rises and the tools and the checklist do not remove the learning.

## How often it happens

Not recorded as a volume. The plan says juniors learn the checks by doing them on real files (stated). The practice has 26 staff and 10 seniors; turnover is about 25% (reported, practice-level); the share of junior time on judgment work, overtime hours and reviewer-rated readiness are not measured.

## Class

business-automation (the flow of learning and preparation work changes). Only one part uses AI: synthetic, non-client practice cases built with the enterprise assistant. Most of the workstream is a coaching routine with no AI. Flagged: the class could instead be read as a no-AI process item; the deciders can change it.

## Rules or AI

Mostly rules and routine: written checks (from the checklist), explain-back, a rotating manual sample and protected coaching time need no AI. The assistant is used only for synthetic non-client practice cases. `ai_use` is left null as the advisor recorded; the AI part is small.

## Data

| Data needed | Where it lives | Owner (role) | Seen in its real state? |
|---|---|---|---|
| Baselines: junior judgment-time share, overtime, turnover, reviewer-rated readiness | Timesheets, HR records, review records (to be confirmed) | Junior-workstream owner (role to be filled) | No |
| Synthetic non-client practice cases | Built in the practice | Junior-workstream owner | No |

## Owner and benefit

- Owner who would lead the work: Junior-workstream owner (a senior manager; the plan's practice lead will name the holder). Until a holder is named the owner is a role, not a person.
- Technical owner: not applicable
- Benefit owner in the business: not yet named
- Lever and metric it would move: experience → share of junior time on judgment work; busy-season overtime; 12-month turnover; reviewer-rated readiness

## Early read

- Risk or regulatory exposure: the measures concern staff, so report them in aggregate only and never rate individuals. The draft policy treats monitoring and evaluating staff as a tier-4 matter, so the risk lead should look at the measures. The assistant is used on non-client material only. Juniors run checks on real client files as today (manual work, no AI).
- Risk tier: none set; `overlay/policy.md` has no proposed tier for this item (provisional policy, not approved).
- Build, buy or partner leaning: none needed; a coaching routine plus the approved assistant for synthetic cases (`personal-assistant`).
- Duplicates or near-duplicates elsewhere in the portfolio: `ct-int-nonclient-drafting` (the assistant also builds synthetic practice cases; the junior-practice-case part overlaps); `firm-enterprise-assistant` (platform). `sox-listing-tool` depends on this item.
- Archetype evidence: assurance-quality-management-16 (grade B; vendor-published, one 20-person firm, not SOX testing). The plan also cites HOLMSTROM-2024 (a PCAOB research proposal, not a finding) and an Anthropic skills trial of 52 engineers (coding, not audit); neither has a use-case grade.
- Human checkpoints: seniors review junior work on a rotating sample.
- AI use: AI in scope for synthetic cases only; `ai_use` null as the advisor left it.
- Capacity choice: redeploy (advisor's). The firm's `capacity_stance` is undecided; the choice is confirmed at `g3`. This item consumes senior coaching time and no headcount change is assumed.

## From the plan

Sections: Chosen options B; Case B; Independent review of Case B; Plan steps 7 and 12; Control plan row for the option 7 workstream; the people plan.

- Process and prerequisites: staff development within control testing. Prerequisites: a named owner for the workstream (to be named by role); protected coaching time from seniors, who are 90-95% booked in busy season (reported).
- Cost lines and who carries them: placeholders (Case B, to replace after the owner is named): senior coaching 1-2 h per senior per month (10-20 h per month); workstream owner 2-4 h per week; synthetic case set 20-40 h one-time; baseline measures 10-20 h. Case B says this item consumes capacity, which comes from redeploying part of Case A's released senior hours.
- Comparison and go/no-go: baselines now, reassess at set checkpoints; go/no-go: the owner and protected time exist before any tool goes live in shadow mode.
- Assumptions to test first: which tasks juniors learn from today (production, training or both); how much coaching time seniors can give at 90-95% booking; whether staff see the workstream as development, not extra work.
- Steps: Now step 7, name the workstream owner (a senior manager) and take baselines (owner: practice lead). Next step 12, start the routine: written checks in use, explain-back, synthetic non-client cases, protected coaching time, a rotating manual sample once any tool exists (owner: junior-workstream owner; depends on steps 1 and 7). Advisor `next_step`: name the workstream owner and define three baseline measures (junior judgment time, turnover, readiness) (owner: practice lead).
- Control-plan row: coaching hours delivered; explain-back done; junior judgment-time share; overtime; turnover. Baselines: judgment share and overtime not measured; turnover about 25% (reported). Normal range set from baselines; owner: junior-workstream owner; monthly; if out of range, protect coaching time before any tool goes live.
- People steps: no change in junior hiring pace is assumed (user); no staff headcount reduction is planned. Risks the plan names: coaching time disappears in busy season; juniors only review and never prepare; explain-back becomes a box-tick; pipeline hollowing if hiring slows later.

Scores note: the advisor's scores follow its independent review (value 2: the low end is zero; feasibility 3 and time to value 3 because protected coaching time is not secured). Category foundation is the user's decision, kept as recorded.

## In use today

Not in use.

## Screen result

**Pending the deciders (portfolio lead and risk lead).** Scores kept as imported: value 2, feasibility 3, data readiness 4, risk 5, time to value 3, strategic fit 4. Weighted **3.35**, **value index 2.56**, **readiness index 4.00** (checked against the portfolio weights). Category **foundation** as the advisor recorded it; under the category rules value 2 would park it. Horizon medium. **Full path**, proposed: the measures concern staff, which the draft policy treats as a risk-lead matter. Risk tier: not set. Sponsor placeholder: Managing partner for assurance.

**Proposed g0:** quadrant low value, high readiness. By the quadrant default this is a **Hold**, `revisit_when` a holder for the owner role is named and the checklist's written checks exist. A Go to discover is defensible instead if the owner role is filled, because the plan's Now step 7 is to name the owner and take baselines, and `sox-listing-tool` depends on this item. Kill criterion if Go: protected coaching time cannot be secured. Not recorded now. Link: `portfolio.yaml` → `sox-junior-development`.

## Next gate evidence

Filled after a Go.

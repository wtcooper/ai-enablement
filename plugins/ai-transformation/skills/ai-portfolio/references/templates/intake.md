# Intake: <item title>

<!-- One file per idea: <workspace>/portfolio/intake/<id>.md. Method: references/method/intake.md.
     Replace every <...>. Owners are roles, never names. No client-confidential or personal data.
     Keep the matching entry in portfolio.yaml in step with this record.
     Write only the sections below and fill every line ("none recorded" if empty). A build, buy or partner
     leaning before g0 is one line in Early read. Meeting pre-reads and agendas go in the chat or the review
     pack (templates/review.md); a fuller build-or-buy goes to ai-solution-delivery once the item is in discover. -->

| Field | Entry |
|---|---|
| Id | `<id>` (the same id as in `portfolio.yaml`) |
| Submitted by | <role> in <practice, team or function> |
| Source | <"New idea", "In use today" (a tool already in use), or the advisor item it came from: `<path>/opportunities.yaml` → `<item id>`> |
| Status | <outline (missing problem, owner or data source) or ready to screen; "Draft to validate" while `label: draft-to-validate`; for a tool in use, its stage and status> |

## The problem in one sentence

<Activity plus expected result: "help <who> <do what> so that <metric> moves".>

## How often it happens

<Last month's actual volume from a record, and where the number came from (from record, reported, observed,
outside-in). Not a typical week.>

## Class

<individual-productivity (a change to how people work in existing tools), business-automation (a change to how
the work flows) or new-value (a new service, product or price). Seat or licence roll-outs go on the enablement
line, not here.>

## Rules or AI

<Could a few if-then rules, a template or an existing feature do this? What was checked.>

## Data

| Data needed | Where it lives | Owner (role) | Seen in its real state? |
|---|---|---|---|
| <data> | <system> | <role> | <yes or no> |

## Owner and benefit

- Owner who would lead the work: <role>
- Technical owner: <for a tool in use, the role that holds the licences and admin settings; otherwise "not applicable">
- Benefit owner in the business: <role, or "not yet named">
- Lever and metric it would move: <lever id> → <metric>

## Early read

- Risk or regulatory exposure: <client data, professional duties, independence, regulator-facing output>
- Risk tier: <the item's `risk_tier`, marked "provisional" while `overlay/policy.md` is missing or not approved;
  "none" with `ai_use: none`>
- Build, buy or partner leaning: <leaning and why>
- Duplicates or near-duplicates elsewhere in the portfolio: <item ids or "none found"; for each advisor item in
  `rolled_up_from`, what it adds>
- Archetype evidence: <use-case ids with grades exactly as recorded, or "none; an idea">
- Human checkpoints: <who checks what, from the advisor item's `human_checkpoints`, or "none yet">
- AI use: <AI needed, or "none: rules, a template or an existing tool is enough" (`ai_use: none`)>
- Capacity choice: <the item's `capacity_use`, and whether the firm's `capacity_stance` is still undecided>

## From the plan

<For imports only; otherwise "New idea, no plan". What the advisor's `transformation-plan.md` already says about
this item, each line with the plan section it came from and each figure with what it covers (a total, or a part of
one). Check here, and in the plan section named, before raising a conflict or a gap.>

- Process and prerequisites: <the item's `process` and `prerequisites`>
- Cost lines and who carries them: <line, range, role; note lines budgeted separately>
- Comparison and go/no-go: <from "How we will know"; the proposed kill line, if any>
- Assumptions to test first: <list>
- Steps: <Now, Next and Later steps for this item, with their owners (roles) and dependencies; `next_step`>
- Control-plan row: <KPIs, thresholds and responses>
- People steps: <from the people and change plan>

## In use today

<For a tool already in use only; otherwise "Not in use". It is not scored (method: intake.md, "A tool already in use").>

- Stage entered at and why: <production or pilot, from how it is used now; no gates recorded that it never passed>
- Licence or seat count: <count and the record it came from, or "awaiting <role>">
- Use list: <practice or team · what it is used for · how often · basis (from record, reported)>
- Data permitted and catalog entry: <data classes; `tool-catalog.yaml` entry id and status, or "not in the catalog">
- Switch-off route: <who cuts access, who tells users, the fallback; tested or not>
- Still to find out: <what, and from which role>

## Screen result

<Filled in step 3: scores, value and readiness indexes, category, horizon, risk tier, gate path, and the g0
decision with its reason. Link: `portfolio.yaml` → `<id>`.>

## Next gate evidence

<Filled after a Go: the evidence the next gate needs and where each piece stands. Update it as evidence arrives;
the gate itself is recorded in `portfolio.yaml`. Drafted messages go in the chat or under the review pack's
Actions, not in new files.>

| Evidence | Status | What exists | What is missing | Owner (role) | Needs first |
|---|---|---|---|---|---|
| <from `next_gate.evidence`> | <met, partly met, not presented or not met> | <what and where> | <what> | <role> | <evidence row, item or none> |

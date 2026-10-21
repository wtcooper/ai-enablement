# Intake: <item title>

<!-- One file per idea: <workspace>/portfolio/intake/<id>.md. Method: references/method/intake.md.
     Replace every <...>. Owners are roles, never names. No client-confidential or personal data.
     Keep the matching entry in portfolio.yaml in step with this record. -->

| Field | Entry |
|---|---|
| Id | `<id>` (the same id as in `portfolio.yaml`) |
| Submitted by | <role> in <practice, team or function> |
| Source | <"New idea" or the advisor item it came from: `<path>/opportunities.yaml` → `<item id>`> |
| Status | <outline (missing problem, owner or data source) or ready to screen> |

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
- Benefit owner in the business: <role, or "not yet named">
- Lever and metric it would move: <lever id> → <metric>

## Early read

- Risk or regulatory exposure: <client data, professional duties, independence, regulator-facing output>
- Build, buy or partner leaning: <leaning and why>
- Duplicates or near-duplicates elsewhere in the portfolio: <item ids or "none found">
- Archetype evidence: <use-case ids with grades exactly as recorded, or "none; an idea">
- Human checkpoints: <who checks what, from the advisor item's `human_checkpoints`, or "none yet">
- AI use: <AI needed, or "none: rules, a template or an existing tool is enough" (`ai_use: none`)>
- Capacity choice: <the item's `capacity_use`, and whether the firm's `capacity_stance` is still undecided>

## From the plan

<For imports only; otherwise "New idea, no plan". What the advisor's `transformation-plan.md` already says about
this item, each line with the plan section it came from. Check here before raising a conflict or a gap.>

- Process and prerequisites: <the item's `process` and `prerequisites`>
- Cost lines and who carries them: <line, range, role; note lines budgeted separately>
- Comparison and go/no-go: <from "How we will know"; the proposed kill line, if any>
- Assumptions to test first: <list>
- Steps: <Now, Next and Later steps for this item, with their owners (roles) and dependencies; `next_step`>
- Control-plan row: <KPIs, thresholds and responses>
- People steps: <from the people and change plan>

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

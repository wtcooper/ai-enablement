---
schema: solution/v1
doc: brief
id: ""
title: ""
source: { portfolio_item: null, opportunity: null }
scope: { name: "", level: team }
owners: { business: "", delivery: "", support: null }
classification:
  { archetype: null, modules: [], work_types: [], pattern: other, ladder: assist, ladder_target: null,
    change_scope: step, runtime_class: personal-assistant }
ai_use: null
sourcing: undecided
tools: []
vendor_evaluations: []
risk_tier: null
status: in-progress
step_completed: 0
next_step: 1
updated: YYYY-MM-DD
---

# Solution brief: <title>

<!-- Schema: references/schemas/solution.md. Replace every <...>; unreached sections say "Not started". Cases by type, source and id only. Owners are roles. -->

## Summary

<One screen: the problem in the owner's terms, decisions so far, the design, where things stand, what is next.>

## Progress

<!-- Tick a step only when all its exit criteria are met. Otherwise list the open criteria after it, e.g. "(open: owner to confirm metric)". -->

- [ ] 1 Frame the problem
- [ ] 2 Build, buy or configure
- [ ] 3 Solution design
- [ ] 4 Evaluation plan (`eval-plan.md`)
- [ ] 5 Production readiness (`readiness.md`)
- [ ] 6 Launch and post-launch review (`post-launch.md`)

## 1. Problem frame

- **Started from:** <portfolio item id and stage, or advisor option id, or "new: intake through ai-portfolio recommended">
- **Problem statement:** <one or two sentences in the business owner's words>
- **Business owner:** <role>; confirmed the metric: <yes/no>; reviews outputs: <rhythm>
- **Success metric and baseline:** <metric> · <today's value or range> · <basis: from record, reported, observed>
- **The work today (last real instance):** <trigger → steps → handoffs → output; systems used>
- **Volumes (last month or season):** <count> · rework or escalation share <%> · time per item <range> · <basis>
- **Users and reviewers:** <who uses the output, who signs it off, who is professionally accountable>
- **Error costs:** <which errors are costly or irreversible (advice, filing, payment, client send); who would notice>
- **Fit checks:** rule or template baseline: <tried / why not enough> · judgment, tangled rules or unstructured
  data: <which> · intern test: <result>
- **Informal AI use today:** <what people already do; data risk noted>
- **Pattern and rung hypothesis:** <pattern id> at <ladder id>; "not when" checks in the pattern file: <clear / issue>
- **Constraints:** <regulatory, client terms, independence, confidentiality>
- **Decision:** <proceed / solve without AI / back to the portfolio or advisor> because <reason>

## 2. Build, buy or configure

| Option | Fit to the workflow | Result on our sample | Total run cost (range) | Switching cost and exit | Data handling | Differentiation | Owner after launch |
|---|---|---|---|---|---|---|---|
| <rules or existing tool> | | | | | | | |
| <buy / configure> | | | | | | | |
| <build-on-model / build-custom> | | | | | | | |

- **Catalog check:** <in the overlay catalog / outside it: flagged, vendor evaluation requested> · **Decision:** <sourcing id> on <runtime class>, at <ladder id>, because <criteria that decided it>
- **Maintenance:** <who re-tests when the model, prompts or tools change> · **Revisit when:** <event, e.g. fails eval thresholds, vendor terms change, volume doubles>

## 3. Solution design

- **Purpose and non-goals:** <what it does; what it will not do>
- **Runtime class and rung:** <runtime class> · <ladder id> · evidence that moves it up: <written rule> ·
  evidence that moves it down: <written rule>
- **Architecture sketch:** <inputs → retrieval → model calls → tools → outputs → human checkpoint → system of record>
- **Data and retrieval:** <source of truth · owner · how it stays current · access model · sensitivity class>

| System | Read or write | Approval needed | Worst thing it could do with this permission |
|---|---|---|---|
| | | | |

- **Security and privacy:** <risk screen (prompt injection, improper output handling, excessive agency) ·
  data handling · access control · risk tier>
- **Human checkpoints (from the pattern file):** <checkpoint · who · what they check · time budget per item>
- **Escalation triggers:** <failure thresholds · high-risk actions that pause for a person> · **When it does not know:** <what it says or does; manual fallback>
- **Logging and retention:** <what is logged · how long · who can read it>
- **Cost envelope:** <range per task and per month at expected volume, with assumptions>
- **Role evolution:** tasks moving: <...> · new work: <...> · capacity: <redeploy / reduce / mixed>
- **Open risks:** <...>

## Decisions log

| Step | Decision | Reason | Decided by (role) |
|---|---|---|---|

## Handoffs

| To | What | Status |
|---|---|---|

## Open questions

<Assumptions to test and numbers to replace with records.>

---
schema: workflow/v1
id: ""
title: ""
roles: []
practice: ""
task: ""
kind: procedure
work_types: []
pattern: other
ladder: assist
runtime_class: personal-assistant
tool: null
status: candidate
origin: crowd
owner: ""
reviewer: ""
human_checkpoint: ""
data_rules: "unknown"
risk_tier: null
tested: null
reuse: null
review_when: ["Tool or model changes", "Policy or data rule changes", "The task or its inputs change"]
retired_because: null
links: { opportunity: null, solution: null, measures: [] }
updated: YYYY-MM-DD
---

# <Workflow title>

<!-- Schema: workflow/v1 (see the ai-enablement skill's references/schemas/workflow.md). Replace every <...>.
Roles, not people. Never paste client-confidential or personal data into this file: examples are sanitized or
invented and labelled as such. -->

## When to use it, and when not

- **Use it for:** <the task, the role, the trigger>
- **Do not use it for:** <tasks outside what it was tested on; where the AI is known to be weak>

## Inputs

<What the user needs to hand: documents, data, context. Which inputs the data rules allow.>

## Steps

<For a prompt: the prompt pattern, with placeholders in angle brackets. For a skill: what it does and how to
start it. For a procedure: numbered steps, marking which are AI steps and which are manual.>

## Example

<A sanitized or invented input and the output it should produce. Label it "illustrative".>

## Known failure modes

<What goes wrong, how often in testing, and how to spot it.>

## Human checkpoint

<Who checks what, when, and against which source, before the output is used or leaves the team. What to do if
the check fails.>

## Data and confidentiality

<The rule from overlay/policy.md or the tool catalog; which data may and may not go in; any client terms to check.>

## Test record

| Date | Cases | Passed | Run by (role) | Notes |
|---|---|---|---|---|
| <YYYY-MM-DD> | <n> | <n> | <role, not the author> | <what failed and why> |

## Change log

| Date | Change | By (role) |
|---|---|---|
| <YYYY-MM-DD> | Created | <role> |

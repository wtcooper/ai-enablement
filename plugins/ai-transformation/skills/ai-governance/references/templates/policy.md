---
schema: policy/v1
title: "AI policy: <firm, practice or team>"
scope: { level: firm, name: "<name>" }
archetype: null
regimes: []
owners:
  policy: "<role>"
  tool_catalog: "<role>"
  request_path: "<role>"
  exceptions: "<role>"
  incidents: "<role>"
backbone: null
data_classes: []
risk_tiers: []
policy_version: 1
status: draft
step_completed: 0
next_step: 1
updated: YYYY-MM-DD
parent: null
---

# AI policy: <firm, practice or team>

<!-- Written by the ai-governance skill, one section per step. Schema: references/schemas/policy.md.
     Keep client-confidential and personal data out of this file. Describe tools, data classes and roles.
     Mark advisor defaults as "default, adjust" so approvers can tell them from sourced requirements. -->

## 1. Where we start (step 1)

**Scope and sponsor:** <scope; sponsoring role; who approves this policy>

**Professional regimes:** <tax-7216 · attest-independence · legal-practice · client-terms · eu-deployer · privacy-law, with one line on why each applies>

**Tools in use today** (counts and tools, never names of people):

| Tool or feature | Tool tier | Sanctioned? | Used for | Data classes going in | Who pays | Source of this (survey, logs, report) |
|---|---|---|---|---|---|---|

**Existing policies and processes:** <AUP, data classification, third-party risk, privacy impact assessment, incident process, records policy>

**Who owns what:**

| Area | Owner (role) | What they decide today | How long a tool decision takes |
|---|---|---|---|

**Signals:** <last time someone was told "no" or "wait" and what happened; policy awareness; incidents or near misses; embedded AI found; agents found>

**Gaps to close:** <gap · evidence · consequence · owner · fix type (policy, tool, training, control)>

## 2. Acceptable use (step 2)

**Purpose and definitions:** <what this policy governs; what "AI tool", "generative AI", "agent" mean here>

**Scope:** <people; runtime classes; embedded features; firm and personal devices>

**Framework backbone:** <NIST AI RMF, ISO/IEC 42001 or internal; mapping aid if any>

**The rules:**
- <Use only catalog entries for firm or client work, within their data classes and tiers.>
- <You stay responsible for anything you use or send; review it as if AI were not involved.>
- <Follow any client instruction that restricts AI.>
- <Not permitted: ...>

**Who approves:** tools <role> · exceptions <role> · new uses <role>

## 3. Data classes and tool tiers (step 2)

| Data class | Meaning here | Worked example | Redaction example |
|---|---|---|---|

| Data class | consumer | commercial | firm-controlled | Extra conditions |
|---|---|---|---|---|
| public | | | | |
| firm-internal | | | | |
| client-confidential | | | | |
| regulated | | | | |

## 4. Risk tiers and human review (step 3)

| Tier | Uses | Who reviews | What the reviewer checks | Record needed | Autonomy allowed |
|---|---|---|---|---|---|
| tier-1 | | | | | |
| tier-2 | | | | | |
| tier-3 | | | | | |
| tier-4 | | | | | |

**Not permitted until approved:** <uses>

**Rule for autonomy:** <how a move up the ladder changes the tier>

## 5. Records of AI use (step 4)

**Central record per tool:** <what it is, appropriate use, how tested, why we trust it, known limits>

**Per matter or engagement, by tier:** <what goes on the file>

**AI inventory:** <where it lives; fields; who keeps it current; embedded features included>

**Logs and retention:** <what the tools keep, retention setting, who can retrieve, how long>

## 6. Profession-specific duties and client consent (step 5)

<One subsection per regime: the duty, the decision rule, who decides, and the record. Link the archetype guardrails used.>

**Client disclosure and consent:** <when we tell clients; consent wording principles; never a condition of service where the rules forbid it>

## 7. Vendor and tool evaluation (step 6)

**Scorecard:** security and privacy · data retention and training · certifications · contract terms · sub-processor and model changes · exit. Ratings: meets, partial, gap, unknown.

**Gates outside the scorecard:** profession screens; a test on our own samples.

**Evaluations on file:** <vendors/<vendor>.md list with decisions>

## 8. Requests, review and maintenance (step 7)

**Request path:** <how to ask; triage lanes (fast, standard, high-tier); response commitment>

**Re-approval triggers:** <model change · sub-processor change · terms change · new data class · new use · incident>

**Review cadence:** <how often the policy, catalog and assessments are reviewed, and by whom>

**Training and acknowledgement:** <by role; before access; how compliance is sampled>

**Exceptions:** <who grants; how logged; how long they last>

**Incidents:** <how to report; correct, disclose, re-review; who reviews near misses>

**Measures:** <staff who can name the approved tool; request volume and turnaround; exceptions; incidents>

## Approvals and change log

| Version | What changed | Approved by (role) |
|---|---|---|

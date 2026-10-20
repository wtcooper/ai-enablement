---
schema: solution/v1
doc: eval-plan
solution: ""
version: 1
status: draft
thresholds_agreed_by: null
---

# Evaluation plan: <solution title>

<!-- Schema: references/schemas/solution.md. Cases stay in the firm's approved systems; list them here by id,
     type and source only. Bump `version` whenever tasks, graders or thresholds change. -->

## 1. Scope and acceptance

- **What is being evaluated:** <the solution, its rung and runtime class, as in `brief.md`>
- **Quality owner:** <one role who decides what "good" means>
- **Acceptance in one sentence:** <e.g. "launch to the first group when every zero-tolerance check passes on all
  trials and the pass-all rate meets the threshold below">

## 2. Test cases

| Case id | Type | Source (system, period) | Should or should not trigger | Difficulty | Gold answer by (role) | Adjudication note |
|---|---|---|---|---|---|---|

- **Size and balance:** <count; share of known failures; share of should-not cases>
- **Gold-answer agreement:** <cases where two experts disagreed and how the quality owner resolved them>

## 3. Failure modes and checks

| Failure mode | Seen in (traces, past errors) | Check (code / model judge / human) | Pass rule (binary) | Zero tolerance? |
|---|---|---|---|---|

## 4. Graders and calibration

- **Model judges:** <for which failure modes; labelled examples per mode; precision and recall against human
  labels; "unknown" option; recheck trigger>
- **Human review sample:** <who, how many per run>

## 5. Consistency, thresholds and baseline

- **Trials per case:** <n>; consistency measure: <all n trials pass / at least one passes, and why>
- **Thresholds by failure class:** <class · tolerance (including zero) · control that mitigates it>
- **Baseline:** <the current manual or legacy process on the same cases; how measured>

## 6. Red-teaming

- **Reviewers independent of the build:** <roles>
- **Attack categories and scorecard:** <category · attempts · successes · fix>
- **Re-run trigger:** <event>

## 7. Regression and change control

- **Capability suite:** <cases still being improved>
- **Regression suite:** <cases that must keep passing; target near 100%>
- **Re-run on:** <model, prompt, retrieval index, tool or input-system change>

## 8. Online monitoring

| Metric | Definition | Baseline (from pilot) | Normal range | Owner | Review rhythm | Response when out of range |
|---|---|---|---|---|---|---|
| Override rate | | | | | | |
| Escalation rate | | | | | | |
| Error categories (sampled) | | | | | | |
| Cost per task | | | | | | |
| Usage by group | | | | | | |
| Input coverage and freshness | | | | | | |

- **Trace sampling:** <how many, how often, by whom; how new failures become cases>

## 9. Evidence retained

<What is kept for review, inspection or audit: case inventory, gold answers, results by version, judge
calibration, red-team scorecard, decisions. Where it is stored.>

## 10. Results log

| Run | Eval plan version | Solution version (model, prompt, retrieval) | Pass-all rate | Zero-tolerance failures | Consistency | Notes |
|---|---|---|---|---|---|---|

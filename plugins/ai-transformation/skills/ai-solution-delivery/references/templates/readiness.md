---
schema: solution/v1
doc: readiness
solution: ""
decision: pending
decided_by: null
conditions: []
---

# Production readiness: <solution title>

<!-- Schema: references/schemas/solution.md. Mark each line ready, gap or not applicable, with the evidence.
     The skill records the review; the firm's owners make and sign the decision. -->

## 1. Ownership and support

| Item | Status | Evidence or note |
|---|---|---|
| Named owner (role) and backup | | |
| Support route and hours; who responds when it fails | | |
| Runbook: common failures, how to pause, who to call | | |
| Incident process: ownership, rehearsal, post-incident review | | |

## 2. Change control and rollback

| Item | Status | Evidence or note |
|---|---|---|
| Change rule: any model, prompt, retrieval or tool change re-runs the regression suite before release | | |
| Models and prompts pinned and versioned | | |
| Managed release; who approves | | |
| Rollback or pause path, and the manual fallback, tested | | |

## 3. Monitoring

| Item | Status | Evidence or note |
|---|---|---|
| Monitoring metrics live (from `eval-plan.md` §8) with alert thresholds and responders | | |
| Trace sampling rota | | |
| Cost per task and usage visible to the owner | | |
| Input coverage, data freshness and retrieval health watched | | |
| Logging, retention and access meet client confidentiality terms | | |

## 4. Evidence and documentation

| Item | Status | Evidence or note |
|---|---|---|
| Evaluation results meet the agreed thresholds (`eval-plan.md` §10) | | |
| Red-team results reviewed for the decision | | |
| Independent review or validation, where required (who, independent of the build) | | |
| Security and privacy sign-off | | |
| Entry in the firm's AI inventory with owner and risk tier (ai-governance) | | |
| Documentation pack: purpose, when to use it, how it was built and tested, known limits, review level, change history, owners | | |

## 5. People and adoption

| Item | Status | Evidence or note |
|---|---|---|
| Adoption plan (ai-enablement): who is trained, what changes on the first day, what to do when the output is wrong | | |
| Training completed before access | | |
| Feedback loop: how user corrections and failures reach the eval set | | |
| Role evolution communicated in the firm's own terms | | |

## 6. Launch plan

- **Stages:** <first group → wider groups; the evidence needed to widen each time>
- **Human review level at launch:** <every item / sample>; reduced only when <written rule>
- **First review point:** <the event that triggers post-launch review 1>
- **Benefits:** <metric, baseline, forecast range and counterfactual handed to ai-portfolio for `benefits.yaml`>

## 7. Decision

| Role | What they signed off | Decision | Conditions |
|---|---|---|---|

- **Decision:** <go / go-with-conditions / no-go>
- **Conditions:** <each with an owner and the event that clears it>
- **Gate evidence sent to ai-portfolio:** <yes / not yet>

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

## 1. Review

| Block | Item | Status | Evidence or note |
|---|---|---|---|
| Ownership | Named owner (role) and backup; support route; who responds when it fails | | |
| Ownership | Runbook (common failures, how to pause, who to call); incident process with rehearsal and post-incident review | | |
| Change and rollback | Any model, prompt, retrieval or tool change re-runs the regression suite before release; models and prompts pinned | | |
| Change and rollback | Managed release and who approves; rollback or pause to the manual fallback, tested | | |
| Monitoring | Metrics from `eval-plan.md` §8 live with alert thresholds and responders; trace sampling rota | | |
| Monitoring | Cost per task and usage visible to the owner; input coverage, freshness and retrieval health watched | | |
| Monitoring | Logging, retention and access meet client confidentiality terms | | |
| Evidence | Results meet the agreed thresholds (`eval-plan.md` §10); red-team results reviewed | | |
| Evidence | Independent review or validation where required (who, independent of the build); security and privacy sign-off | | |
| Evidence | Entry in the firm's AI inventory with owner and risk tier (ai-governance) | | |
| Evidence | Documentation pack: purpose, when to use it, how it was built and tested, known limits, review level, change history, owners | | |
| People | Adoption plan (ai-enablement): who is trained, first-day changes, what to do when the output is wrong; training before access | | |
| People | Feedback loop from user corrections to the eval set; role evolution communicated | | |

## 2. Launch plan

- **Stages:** <first group → wider groups; the evidence needed to widen each time>
- **Human review level at launch:** <every item / sample>; reduced only when <written rule>
- **First review point:** <the event that triggers post-launch review 1>
- **Benefits:** <metric, baseline, forecast range and counterfactual handed to ai-portfolio for `benefits.yaml`>

## 3. Decision

| Role | What they signed off | Decision | Conditions |
|---|---|---|---|

- **Decision:** <go / go-with-conditions / no-go>
- **Conditions:** <each with an owner and the event that clears it>
- **Gate evidence sent to ai-portfolio:** <yes / not yet>

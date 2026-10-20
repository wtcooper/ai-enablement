# Library index

The backbone every archetype shares: how to classify an option, which patterns fit which work, how to describe
tools without naming vendors, and the default levers, scores and stages. Read the section you need. Ids here
are the controlled values in `../schemas/vocabulary.yaml`; use them in `opportunities.yaml`.

## Contents

1. [Ladder and change scope](#1-ladder-and-change-scope)
2. [Work types](#2-work-types)
3. [Agentic patterns](#3-agentic-patterns)
4. [Runtime classes](#4-runtime-classes)
5. [Value levers](#5-value-levers)
6. [Scoring and categories](#6-scoring-and-categories)
7. [Journey stages](#7-journey-stages)
8. [Functions](#8-functions)
9. [When no archetype matches](#9-when-no-archetype-matches)

## 1. Ladder and change scope

Classify every option on two independent dimensions.

**Ladder: how much the AI does** (`ladder`)

| Id | Meaning | Typical human role |
|---|---|---|
| `assist` | AI helps a person with a task the person still owns | Does the work, uses AI as a helper |
| `augment` | AI is built into a step and gives a first pass; a person reviews it | Reviews and decides |
| `automate` | A defined step runs with no person on the normal path; exceptions go to people | Handles exceptions, monitors |
| `delegate` | An agent owns a multi-step outcome across systems, started by events, with human checkpoints | Sets goals and criteria, approves at checkpoints, audits |

**Change scope: what changes** (`change_scope`)

| Id | Meaning |
|---|---|
| `step` | One step of the existing process gets better |
| `process` | The flow is redesigned: steps removed or merged, work made continuous, or done on full populations |
| `model` | The service, business or operating model changes: new services, pricing, sourcing, who does the work |

**The four Reimagine lenses** are conversation prompts, not fields. They map onto the two dimensions:

| Lens | Ladder | Change scope |
|---|---|---|
| Improve the step | assist or augment | step |
| Automate the flow | automate | step or process |
| Delegate the outcome | delegate | process |
| Reinvent the work | any | model, or a process that stops existing |

Delegation at Adopting is limited to one or two bounded workflows behind the five gates in
`../method/onboarding.md` §5.

## 2. Work types

How the work is done. Tag each process step with one or more (`work_types`); the work type suggests which
patterns fit.

| Id | Work type | Patterns that often fit |
|---|---|---|
| `review-assurance` | Checking work, evidence or compliance against criteria | full-population-testing, draft-review-loop, document-to-decision |
| `transaction-processing` | High-volume, rule-heavy items moving through defined steps | intake-triage, reconcile-exceptions, end-to-end-case-agent |
| `expert-judgment` | Specialist decisions and recommendations under ambiguity | research-brief, grounded-knowledge-assistant (AI prepares; a person decides) |
| `research-synthesis` | Gathering, comparing and condensing information from many sources | research-brief, grounded-knowledge-assistant |
| `document-production` | Creating reports, deliverables and communications | draft-review-loop, bulk-transformation |
| `client-interaction` | Answering, serving and managing relationships | service-agent-escalation, grounded-knowledge-assistant |
| `coordination-scheduling` | Planning, resourcing, handoffs and status tracking | intake-triage, monitor-diagnose-act |
| `data-reporting` | Collecting, reconciling and analyzing data, and producing metrics | reconcile-exceptions, monitor-diagnose-act, full-population-testing |
| `software-systems` | Building, configuring and maintaining technology | bulk-transformation, draft-review-loop |
| `physical-field` | Hands-on work, where AI supports planning, inspection and guidance | monitor-diagnose-act, grounded-knowledge-assistant |

## 3. Agentic patterns

Reusable shapes of AI-enabled work (`pattern`). Each pattern has a detailed file in `patterns/` (linked below):
ladder, build, controls, metrics, governance, graded evidence and probes. Archetype use cases carry further
evidence; search `use-cases/*.yaml` by `pattern:` to find real examples.

| Id | What it does | Usual ladder | Key human checkpoint | Main failure mode |
|---|---|---|---|---|
| [`intake-triage`](patterns/intake-triage.md) | Reads incoming requests or items, classifies, routes and prioritizes them | augment → automate | Spot checks of routing; owner of the exception queue | Misrouted urgent items |
| [`document-to-decision`](patterns/document-to-decision.md) | Extracts facts from documents and checks them against criteria to propose a decision | augment → automate | A person approves decisions above a threshold | Extraction errors treated as fact |
| [`research-brief`](patterns/research-brief.md) | Gathers sources, compares them and writes a cited brief | assist → augment | The expert reads the sources behind key claims | Invented or misread citations |
| [`draft-review-loop`](patterns/draft-review-loop.md) | Drafts a deliverable from inputs and templates; a reviewer edits and approves | assist → augment | Reviewer sign-off before anything leaves the team | Review turns into a rubber stamp |
| [`full-population-testing`](patterns/full-population-testing.md) | Tests every item instead of a sample and surfaces exceptions | automate | A person investigates and concludes on exceptions | False positives that swamp reviewers |
| [`monitor-diagnose-act`](patterns/monitor-diagnose-act.md) | Watches signals continuously, explains anomalies and proposes or takes actions | augment → automate | Approval for actions that are hard to reverse | Alert fatigue; unsafe automatic actions |
| [`reconcile-exceptions`](patterns/reconcile-exceptions.md) | Matches records across sources and works the breaks | automate | A person clears unresolved breaks | Forced matches that hide real breaks |
| [`service-agent-escalation`](patterns/service-agent-escalation.md) | Answers clients or staff directly and hands off to a person when needed | automate | Escalation rules; sampling of conversations | Confident wrong answers; no clean handoff |
| [`grounded-knowledge-assistant`](patterns/grounded-knowledge-assistant.md) | Answers questions from an approved body of knowledge, with citations | assist | Content owners keep the knowledge current | Stale or unapproved content |
| [`end-to-end-case-agent`](patterns/end-to-end-case-agent.md) | Takes a case from intake to resolution across systems, with checkpoints | delegate | Checkpoints at key decisions and before anything irreversible | Errors compounding across steps |
| [`bulk-transformation`](patterns/bulk-transformation.md) | Converts, migrates or rewrites large volumes of content, data or code | automate | Sampled quality checks; sign-off before cutover | Silent errors at scale |
| `other` | Anything that does not fit; describe it in the option | — | — | — |

## 4. Runtime classes

Describe tools by runtime class (`runtime_class`), not by vendor. If `overlay/tool-catalog.yaml` exists, it maps
these classes to the organization's approved products; recommend those and flag anything outside it.

| Id | Class | Fits |
|---|---|---|
| `personal-assistant` | Chat or coding assistant used by one person | assist; Curious and Experimenting |
| `shared-team-skills` | Packaged prompts, skills or plugins used the same way across a team | assist and augment made consistent; the step from Experimenting to Adopting |
| `workflow-automation` | A defined workflow on an automation platform, with AI at some steps | augment and automate |
| `background-agent` | An agent that runs on a schedule or trigger without a person present | automate; monitoring and batch work |
| `managed-agent-runtime` | A hosted, long-running agent with tools, state and human checkpoints, built into business systems | delegate; end-to-end cases |

## 5. Value levers

Default levers (`value_levers`). The top plan chooses and weights them in Frame; each needs one named metric.

| Id | Lever | Example metrics |
|---|---|---|
| `capacity` | Hours released for other work | Hours per item; items per person per month |
| `speed` | Cycle time and responsiveness | Days from trigger to done; turnaround to client |
| `quality` | Fewer errors and rework | Share returned by review; defects found later |
| `growth` | Revenue, new services, win rate | Revenue from new services; proposals won |
| `cost` | Lower cost to serve | Cost per item; external spend |
| `risk` | Fewer failures, findings and exposures | Findings per inspection; incidents |
| `experience` | Client and employee experience | Client satisfaction; staff turnover; overtime |

Hours released are not value realized until the capacity has a destination (`../method/business-case.md`).

## 6. Scoring and categories

Six dimensions, each scored 1–5, with default weights. `weighted_score` = sum of weight × score.

| Dimension | Default weight |
|---|---|
| `value` | 0.30 |
| `feasibility` | 0.20 |
| `data_readiness` | 0.15 |
| `risk` (higher score = lower risk) | 0.15 |
| `time_to_value` | 0.10 |
| `strategic_fit` | 0.10 |

Categories: `quick-win`, `foundation`, `big-bet`, `park`. Gates, score anchors, category rules and sequencing
rules are in `../method/prioritize.md` §3.

## 7. Journey stages

`curious` → `experimenting` → `adopting` → `scaling` → `ai-native`. Place each scope by what the user can show or
count, not by self-rating. Markers, blockers, readiness criteria and the delegation gates are in
`../method/onboarding.md` §5; field-specific markers are in the archetype's `ARCHETYPE.md`. To plan the move to the next
stage (investments, exit criteria, failure points, how organizations are spread across stages and how published maturity models
compare), read [journey-stages.md](journey-stages.md).

## 8. Functions

Business functions (`function` in use cases). Use them to place work that sits outside an archetype's core value
chain, such as a firm's finance, HR or IT teams.

| Id | Function |
|---|---|
| [`strategy-planning`](functions/strategy-planning.md) | Strategy and planning |
| [`sales-marketing-bd`](functions/sales-marketing-bd.md) | Sales, marketing and business development |
| [`product-service-development`](functions/product-service-development.md) | Product and service development |
| [`service-delivery`](functions/service-delivery.md) | Service delivery and operations |
| [`customer-service`](functions/customer-service.md) | Customer service |
| [`people-hr`](functions/people-hr.md) | People (HR) |
| [`technology-it`](functions/technology-it.md) | Technology (IT) |
| [`finance-accounting`](functions/finance-accounting.md) | Finance and accounting |
| [`procurement-supply-chain`](functions/procurement-supply-chain.md) | Procurement and supply chain |
| [`risk-compliance-legal`](functions/risk-compliance-legal.md) | Risk, compliance and legal |

Each function has a card in `functions/`, linked from its id: what the function covers and which archetype covers
firms that sell the work, processes and pain points, where AI is changing the work by Reimagine lens with graded
examples and archetype use-case ids, metrics, interview probes, guardrails and how roles evolve. Read the card for
the function the user's work sits in, alongside any archetype module that covers the same work.

## 9. When no archetype matches

1. Say so plainly, and say what you will use instead: the method, this library, and the user's own knowledge.
2. Map the user's value chain in Map and tag work types; they point to the patterns in §3.
3. Treat every example you give as illustrative unless it comes from a reference file or the overlay (rule 4).
4. Offer on-the-spot research only if the user agrees and you have web access: `../briefs/research-archetype.md`.
   Its output is a provisional archetype in `overlay/archetypes/<id>/`, labelled provisional.

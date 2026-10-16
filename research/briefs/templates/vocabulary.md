# Research vocabulary (controlled values)

Every research output uses these ids exactly. They come from spec §6.2–6.9.

## Work types (`work_types`)

| id | Work type |
|---|---|
| `review-assurance` | Review & assurance: checking work, evidence or compliance against criteria |
| `transaction-processing` | Transaction & case processing: high-volume, rule-heavy items moving through steps |
| `expert-judgment` | Expert judgment & advice: specialist decisions under ambiguity |
| `research-synthesis` | Research & synthesis: gathering and condensing information from many sources |
| `document-production` | Document & content production: reports, deliverables, communications |
| `client-interaction` | Client & customer interaction: answering, serving, managing relationships |
| `coordination-scheduling` | Coordination & scheduling: planning, resourcing, handoffs, status |
| `data-reporting` | Data & reporting: collecting, reconciling, analyzing data; producing metrics |
| `software-systems` | Software & systems work: building, configuring, maintaining technology |
| `physical-field` | Physical & field operations: hands-on work |

## Agentic patterns (`pattern`)

`intake-triage` · `document-to-decision` · `research-brief` · `draft-review-loop` ·
`full-population-testing` · `monitor-diagnose-act` · `reconcile-exceptions` ·
`service-agent-escalation` · `grounded-knowledge-assistant` · `end-to-end-case-agent` ·
`bulk-transformation`

If no pattern fits, use `other` and describe the pattern in `notes`. The synthesis step proposes new
patterns from these.

## Reimagine lens (`lens`)

`improve` (assist or augment the step) · `automate` (no person on the normal path) · `delegate` (an
agent owns a multi-step outcome) · `reinvent` (the process, service or business model changes)

## Ladder (`ladder`)

`assist` · `augment` · `automate` · `delegate` · `reinvent`

## Runtime class (`runtime_class`)

`personal-assistant` · `shared-team-skills` · `workflow-automation` · `background-agent` ·
`managed-agent-runtime`

## Field maturity (`maturity`)

| Value | Meaning |
|---|---|
| `in-production` | Used in real work by at least one named organization |
| `piloting` | Publicly described pilots or trials |
| `announced` | A product or firm announcement without evidence of use |
| `emerging` | Discussed by practitioners, researchers or regulators as coming |

## Evidence grade (`evidence_grade`)

| Grade | Meaning |
|---|---|
| `A` | A measured outcome from a named organization |
| `B` | A named real deployment, without published measurements |
| `C` | A vendor claim or analyst estimate |
| `D` | A plausible idea with no public deployment found. Must be labelled "idea" |

## Value levers (`outcomes[].lever`)

`capacity` · `speed` · `quality` · `growth` · `cost` · `risk` · `experience`

## Source types (`sources[].type`)

`conference` · `regulator` · `standard-setter` · `professional-body` · `firm` · `vendor` ·
`academic` · `survey` · `press` · `podcast` · `community` · `job-posting`

## Use-case entry (YAML)

```yaml
- id: <archetype>-<module>-NN
  title: string
  archetype: id
  module: id
  function: service-delivery            # or another function id when the use case sits in a support function
  work_types: [ id ]
  pattern: id
  lens: id
  ladder: id
  runtime_class: id
  maturity: id
  problem: string                       # the current pain, in plain language
  solution: string                      # how AI changes the work; product names only if the source names them
  outcomes: [ { lever, description, figure, source_ref } ]
  prerequisites: [ string ]
  risks_and_guardrails: [ string ]
  human_checkpoints: [ string ]
  role_evolution: string
  evidence_grade: A | B | C | D
  sources: [ { ref, title, publisher, type, url, date } ]
  last_reviewed: YYYY-MM-DD
  notes: string                         # optional
```

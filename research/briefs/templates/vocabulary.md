# Research vocabulary (controlled values)

Every research output uses these ids exactly. They come from spec §6.2–6.9. The authoritative list is
`plugins/transformation-advisor/skills/transformation-advisor/references/schemas/vocabulary.yaml`, and
`scripts/validate.py` enforces it.

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

## Ladder (`ladder`): how much the AI does

| Value | Meaning |
|---|---|
| `assist` | AI helps a person who still does the task |
| `augment` | AI gives a first pass inside the step, and a person reviews it |
| `automate` | No person on the normal path; exceptions go to people |
| `delegate` | An agent owns a multi-step outcome, with human checkpoints |

## Change scope (`change_scope`): what changes

| Value | Meaning |
|---|---|
| `step` | One step of the existing process gets better |
| `process` | The flow itself is redesigned: steps removed, merged, made continuous, or done on full populations |
| `model` | The service, business or operating model changes: new services, pricing, sourcing, who does the work |

**Worked examples:**

| Use case | `ladder` | `change_scope` |
|---|---|---|
| Walkthrough assistant | augment | step |
| Evidence-to-sample matching, with people reviewing exceptions | automate | step |
| Full-population testing replacing samples | automate | process |
| Agent tests key controls end to end and drafts the workpaper | delegate | process |
| A firm sells agent-delivered testing as a service | delegate | model |

The four Reimagine lenses (improve, automate, delegate, reinvent) are conversation prompts. They are not
fields.

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
| `A` | A measured outcome from a named organization: a figure the named organization reports as measured (a tracked metric, a study or data). A practitioner's recollection or rough estimate, even with numbers, is B (rule adopted 2026-10-17) |
| `B` | A named real deployment, without published measurements |
| `C` | A vendor claim or analyst estimate |
| `D` | A plausible idea with no public deployment found. Must be labelled "idea" |

## Outcome provenance (`outcomes[].provenance`)

`self-reported` (the deploying organization) · `vendor-published` · `independent` (a regulator,
academic or third-party measure)

## Source access (`sources[].access`)

`full` (opened and read) · `search-only` (seen only in search results; can never support an A or B
grade on its own)

## Value levers (`outcomes[].lever`)

`capacity` · `speed` · `quality` · `growth` · `cost` · `risk` · `experience`

## Source types (`sources[].type`)

`conference` · `regulator` · `standard-setter` · `professional-body` · `firm` · `vendor` ·
`academic` · `survey` · `press` · `podcast` · `community` · `job-posting`

## Format rules

- Dates are ISO only: `YYYY-MM-DD`, `YYYY-MM` or `YYYY`. Never "undated" or "FY26".
- `function` comes from the list in `vocabulary.yaml`.
- Every attributed sentence, including those in `role_evolution` and `risks_and_guardrails`, needs a source ref.

## Use-case entry (YAML)

```yaml
- id: <archetype>-<module>-NN
  title: string
  archetype: id
  module: id
  function: service-delivery            # or another function id when the use case sits in a support function
  work_types: [ id ]
  pattern: id
  ladder: id
  change_scope: id
  runtime_class: id
  maturity: id
  problem: string                       # the current pain, in plain language
  solution: string                      # how AI changes the work; product names only if the source names them
  outcomes: [ { lever, description, figure, measures, provenance, source_ref } ]   # at least one; for ideas use description "none published"
                                        # measures = numerator / denominator, or what the figure counts, in the source's own words
  prerequisites: [ string ]
  risks_and_guardrails: [ string ]
  human_checkpoints: [ string ]
  role_evolution: string
  evidence_grade: A | B | C | D
  sources: [ { ref, title, publisher, type, url, date, access, locator } ]
                                        # ref = PUBLISHER-SHORT-YYYY (the same document gets the same ref in every file)
                                        # date = YYYY-MM-DD, YYYY-MM or YYYY; check the byline, article:published_time and JSON-LD first
                                        # locator = page, section or paragraph that supports the claim
  last_reviewed: YYYY-MM-DD
  notes: string                         # optional
```

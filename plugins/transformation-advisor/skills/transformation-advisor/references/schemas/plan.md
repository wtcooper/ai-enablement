# Schema: transformation-plan.md (plan/v1)

The plan is one markdown file per scope: YAML frontmatter for state and settings, then a body with one section per
phase. Child units have the same file in `units/<unit-id>/`. Ids come from `vocabulary.yaml`. A blank starting
file is `../templates/transformation-plan.md`.

## Contents

1. [Frontmatter](#1-frontmatter)
2. [Field rules](#2-field-rules)
3. [Body](#3-body)
4. [Workspace layout](#4-workspace-layout)

## 1. Frontmatter

```yaml
schema: plan/v1
scope:
  name: string                    # e.g. "Regional audit practice"
  level: individual | team | function | business-unit | organization
  parent: path | null             # e.g. ../../transformation-plan.md for a unit
author: { name: string, role: string }
profile:
  archetype: id | null            # from ../archetypes/index.md, or an overlay archetype id
  modules: [ id ]                 # module ids from that archetype's ARCHETYPE.md
  journey_stage: curious | experimenting | adopting | scaling | ai-native
  goals: [ string ]
  constraints: [ string ]
  tools: [ string ]
  session_goal: string
settings:                         # set at the top level; children inherit unless they override
  value_levers:
    - { id: capacity, name: string, metric: string, weight: number }
  scoring_weights: { value: 0.30, feasibility: 0.20, data_readiness: 0.15, risk: 0.15, time_to_value: 0.10, strategic_fit: 0.10 }
  capacity_stance: redeploy | reduce | mixed | undecided
  guardrails: [ string ]
  overlay: overlay/ | null
units:                            # present after Break down
  - { id: string, name: string, owner: role, wave: integer, mode: delegate | same-user | desk-review, status: not-started | in-progress | desk-review | complete }
status: in-progress | complete
phase_completed: 0-7
next_phase: 0-7 | null
updated: YYYY-MM-DD
```

## 2. Field rules

- **Required from Onboard:** `schema`, `scope`, `author` (a role is enough; a name is optional), `profile`,
  `status`, `phase_completed`, `next_phase`, `updated`.
- **Settings** are written in Frame. `scoring_weights` must sum to 1. Use the defaults unless the user chooses
  otherwise. Value lever ids come from `vocabulary.yaml`; each lever has one named metric.
- **Inheritance.** A unit reads its parent's `settings` and copies only what it overrides. Precedence: overlay >
  plan settings > archetype > backbone. The rules in `SKILL.md` cannot be overridden.
- **Units.** `wave` is a sequence number, not a date: wave 1 goes first, later waves follow when what they depend
  on is in place. `status: desk-review` marks a first-pass draft that people who do the work have not validated.
- **State.** After every phase set `phase_completed`, `next_phase` and `updated`, and tick the phase in the
  progress checklist. After Plan, `next_phase: null` and `status: complete` (or `in-progress` while units are
  still planning).
- **No people data.** Owners are roles. Never record performance judgments about named individuals.

## 3. Body

In this order. Each phase section is written when the phase completes; sections not reached stay as a heading
with "Not started".

| Section | Written in | Contents |
|---|---|---|
| Summary | Updated every phase | One screen: ambition, where things stand, top options, what happens next |
| Progress | Every phase | Checklist: Onboard, Frame, Map, Diagnose, Reimagine, Prioritize, Make the case, Plan |
| Profile | 0 Onboard | Played-back profile; stage table (scope, stage, markers seen, binding constraint); the adapted path; confidentiality reminder given; corrections |
| Frame | 1 | Ambition sentence; why now; success measures; value levers and weights; capacity stance; constraints; business-model exposure at higher levels |
| Map | 2 | Processes with trigger, steps, handoffs, volumes, times, systems and rework, each number labelled reported, from record, observed or outside-in; value chain and units at higher levels |
| Diagnose | 3 | Waste, bottleneck, rework and failure points; work type per step; heatmap and unit order at higher levels |
| Reimagine | 4 | Options by lens, each with ladder and change scope and supporting evidence ids; full detail in `opportunities.yaml` |
| Prioritize | 5 | Score table, categories, dependency sequence; roll-up results at higher levels |
| Make the case | 6 | One page per top option (headings in `../method/business-case.md` §8); portfolio bridge at higher levels |
| Plan | 7 | Now · Next · Later with owners and dependencies, or workstreams at higher levels; value creation plan; control plans; KPIs; review rhythm; people and change plan; next journey stage and its exit criteria |
| Leadership summary | 6–7 | A section that can be pasted elsewhere |
| Open questions | Any | Assumptions to test and numbers to replace with records |

## 4. Workspace layout

```
<workspace>/
├── transformation-plan.md
├── opportunities.yaml
├── overlay/              # optional organization content
├── evidence/             # documents the user provided
└── units/<unit-id>/      # one per unit after Break down: brief.md, transformation-plan.md, opportunities.yaml, ...
```

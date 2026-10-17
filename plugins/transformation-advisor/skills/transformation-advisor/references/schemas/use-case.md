# Schema: use-case entries

The format of every entry in an archetype's `use-cases/<module>.yaml`, in `overlay/use-cases.yaml`, and in a
provisional archetype written by on-the-spot research. Each file is a YAML list. Ids come from `vocabulary.yaml`.

## Format

```yaml
- id: string                       # <archetype>-<module>-NN; overlay entries: internal-NN; functions: fn-<function>-NN
  title: string
  archetype: id | null
  module: id | null
  function: id
  work_types: [ id ]
  pattern: id
  ladder: assist | augment | automate | delegate
  change_scope: step | process | model
  runtime_class: id
  maturity: in-production | piloting | announced | emerging
  problem: string
  solution: string                 # who did what; keep the source's tense ("announced", "piloting", "in production")
  outcomes:
    - { lever: id, description: string, figure: string, measures: string, provenance: self-reported | vendor-published | independent, source_ref: ref }
  prerequisites: [ string ]
  risks_and_guardrails: [ string ]
  human_checkpoints: [ string ]
  role_evolution: string
  evidence_grade: A | B | C | D
  sources:
    - { ref: string, title: string, publisher: string, type: id, url: string, date: YYYY-MM-DD | YYYY-MM, access: full | search-only, locator: string }
  last_reviewed: YYYY-MM-DD
  notes: string                    # optional: caveats, search-only figures, overlaps
```

## Evidence grades

| Grade | Meaning |
|---|---|
| A | A measured outcome from a named organization |
| B | A named, real deployment without published measurements |
| C | A vendor claim or analyst estimate |
| D | An idea practitioners or researchers discuss, with no public deployment yet (labelled "idea") |

## Rules

- Every entry has at least one dated source. Never invent sources, organizations, figures or dates.
- `measures` states what a figure counts (numerator and denominator, in the source's words).
- `provenance` says who published the figure. Most published figures are self-reported or vendor-published; say so
  when citing them.
- A figure seen only in search results goes in `notes`, never in the outcomes of an A or B entry.
- Measurements from an adjacent process cap the grade at B, with a note.
- Overlay entries (`overlay/use-cases.yaml`) are labelled **internal** when shown to the user. They may omit public
  sources but need an internal reference and a date.

## Searching

Search instead of reading whole files. Useful fields: `module:`, `pattern:`, `work_types:`, `ladder:`,
`change_scope:`, `maturity:`, `evidence_grade:`. For example, search an archetype's `use-cases/` folder for
`pattern: full-population-testing`, then read only the matching entries.

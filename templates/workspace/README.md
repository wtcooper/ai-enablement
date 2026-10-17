# Transformation workspace

A starter folder for the AI transformation advisor. Copy it, or use it as a template repository, then open
your AI tool in this folder and ask for help in your own words. The advisor saves your plan here.

```
./
├── transformation-plan.md   # created by the advisor after onboarding
├── opportunities.yaml       # created in the Reimagine step
├── evidence/                # optional: process documents you want the advisor to read
├── overlay-example/         # examples: rename to overlay/ and edit to tailor the advisor
└── units/<unit>/            # created at practice or firm level: one folder per unit
```

## Overlay (optional)

An `overlay/` folder tailors the advisor to your organization without changing the plugin. This starter ships
examples in `overlay-example/` so they don't take effect by accident. To use them, rename the folder to
`overlay/`, replace the example entries, and delete any file you don't need.

| File | What it does |
|---|---|
| `overlay/tool-catalog.yaml` | Your approved AI tools, by runtime class. Recommendations name these and flag anything else |
| `overlay/glossary.md` | Your organization's terms, so the advisor speaks your language |
| `overlay/guardrails.md` | Extra rules. They add to the advisor's ground rules and never weaken them |
| `overlay/use-cases.yaml` | Internal examples, shown alongside public ones and labelled "internal" |
| `overlay/archetypes/<id>/` | Private archetypes or extensions (on-the-spot research also writes here, labelled provisional) |

## Before you share

- Keep client-confidential and personal data out of every file. Describe the work instead.
- The plan is plain text: commit and push it, or copy the folder to your shared drive.

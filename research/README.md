# Research program (build-only)

This folder holds the research we run to write the plugin's archetype packs, method files and library.
**None of it ships.** Only the synthesized, verified content copied into
`plugins/transformation-advisor/` is part of the product. See
[plan § What ships and what doesn't](../plan/2026-10-16-ai-transformation-advisor.md) and
[spec §11](../spec/2026-10-16-ai-transformation-advisor.md).

## Layout

```
research/
├── briefs/
│   └── templates/          # reusable briefs: landscape, module-angle, synthesis, verifier, vocabulary
└── runs/<wave>/            # raw subagent output for each wave, kept for traceability
```

## The recipe for one module

1. **Landscape scan.** One per archetype, from `templates/landscape.md`.
2. **Three angle deep dives**, run in parallel: practice, discourse, and governance & evidence, from
   `templates/module-angle.md`.
3. **Synthesis**, from `templates/synthesis.md`. It writes the module file and use-case YAML into the
   plugin's `references/archetypes/<id>/`.
4. **Verification**, from `templates/verifier.md`. It edits those files in place and writes a report.

## Waves

| Wave | Scope | Status |
|---|---|---|
| `pilot` | assurance → controls testing | running |

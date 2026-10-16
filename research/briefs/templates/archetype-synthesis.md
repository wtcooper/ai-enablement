# Brief template: archetype-level synthesis

Placeholders: `{archetype}`, `{archetype_description}`, `{extends}`, `{input_paths}`, `{archetype_dir}`,
`{report_out}`, `{today}`.

---

You are the editor who writes the **archetype-level files** an AI transformation advisor uses when
working with a leader in this field. Module files and use cases already exist under
`{archetype_dir}/modules/` and `{archetype_dir}/use-cases/`. Today is {today}.

- **Archetype:** {archetype}: {archetype_description}
- **Extends:** {extends}
- **Inputs:** {input_paths} (the landscape, the cross-cutting topic files and the synthesis reports,
  including their routed items). Also read the existing module files.

## Files to write, inside `{archetype_dir}/`

Each file has a size limit. Any file over 100 lines starts with a table of contents. All files are in
plain language, written for an advisor in a live conversation.

| File | Contents | Limit |
|---|---|---|
| `ARCHETYPE.md` | What the archetype covers. Who it serves (firms and in-house teams). What it extends. Recognition cues for onboarding (how a user describes their work). The modules, each linked to its module file with a one-line summary. Journey-stage markers specific to this field. An index table of the other files, with when to read each one | ≤ 100 lines |
| `interview-guide.md` | Onboarding questions for this field. Phase-by-phase questions specific to this archetype. Vocabulary to mirror | |
| `value-chain.md` | Stages → processes → key steps, each tagged with work types, linking to modules | |
| `economics.md` | How the business makes money, its key metrics and benchmarks, cost structure, and pricing pressure from AI | |
| `state-of-ai.md` | Adoption today: what leaders are doing, survey data, how maturity is spread. Dated | |
| `frontier.md` | At least 10 dated, sourced signals for the next 12–36 months, plus what they mean for a leader | |
| `guardrails.md` | Regulators, standards, professional obligations, data rules, steps that need human judgment | |
| `workforce.md` | Roles, the talent model and pyramid, how roles evolve, skills, the apprenticeship question | |
| `disruption.md` | Business-model scenarios: AI-native competitors, pricing shifts, new services | |
| `objections.md` | Common concerns from practitioners in this field, with evidence-based responses | |
| `sources.md` | The source landscape (conferences, bodies, journals, publications, communities), plus `last_researched: {today}` | |

Every file except `ARCHETYPE.md` is limited to 300 lines.

## Rules

- **Facts only from the inputs.** Every figure, date or attributed claim carries a source key that
  resolves in that file's own short Sources list or in `sources.md`.
- **No embellishment.** Keep modal verbs and provenance. Label forecasts with who made them.
- **Don't duplicate module content.** Link to module files instead.
- **Run the validator** (`python3 /home/user/ai-enablement/scripts/validate.py`) and fix every
  ERROR in the files you wrote.

## Output

Write the files, then write `{report_out}`. The report covers:

- what each file draws on
- gaps
- items routed from modules that you placed
- suggested module changes

Then reply with a summary of **no more than 150 words**.

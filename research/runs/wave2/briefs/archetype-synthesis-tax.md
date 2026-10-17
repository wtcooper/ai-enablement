**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are the editor who writes the **archetype-level files** an AI transformation advisor uses when
working with a leader in this field. Module files and use cases already exist under
`/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/` and `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/use-cases/`. Today is 2026-10-17.

- **Archetype:** tax: Tax: tax compliance (individual and small-business returns; corporate returns, credits and incentives), income tax accounting and the global minimum tax, indirect tax, transfer pricing, controversy (including tax-authority AI), research and advisory, and tax data and technology; delivered by accounting and tax firms (Big Four, mid-tier, small practices, AI-native entrants) and by in-house corporate tax departments.
- **Extends:** professional-services (not yet written; name it without a link)
- **Inputs:** `/home/user/ai-enablement/research/runs/wave2/landscape-tax.md`, `/home/user/ai-enablement/research/runs/wave2/tax-x-guardrails-professional-responsibility.md`, `/home/user/ai-enablement/research/runs/wave2/tax-x-economics-business-model.md`, `/home/user/ai-enablement/research/runs/wave2/tax-x-state-of-ai-disruption.md`, `/home/user/ai-enablement/research/runs/wave2/tax-x-workforce-talent.md`, `/home/user/ai-enablement/research/runs/wave2/compliance-individual-business-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave2/compliance-corporate-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave2/provision-pillar-two-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave2/indirect-tax-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave2/transfer-pricing-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave2/controversy-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave2/research-advisory-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave2/data-technology-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave2/compliance-individual-business-verification-report.md`, `/home/user/ai-enablement/research/runs/wave2/compliance-corporate-verification-report.md`, `/home/user/ai-enablement/research/runs/wave2/provision-pillar-two-verification-report.md`, `/home/user/ai-enablement/research/runs/wave2/indirect-tax-verification-report.md`, `/home/user/ai-enablement/research/runs/wave2/transfer-pricing-verification-report.md`, `/home/user/ai-enablement/research/runs/wave2/controversy-verification-report.md`, `/home/user/ai-enablement/research/runs/wave2/research-advisory-verification-report.md`, `/home/user/ai-enablement/research/runs/wave2/data-technology-verification-report.md` (the landscape, the cross-cutting topic files and the synthesis reports,
  including their routed items). Also read the existing module files.

## Files to write, inside `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/`

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
| `sources.md` | The source landscape (conferences, bodies, journals, publications, communities), plus `last_researched: 2026-10-17` | |

Every file except `ARCHETYPE.md` is limited to 300 lines.

## Rules

- **Facts only from the inputs.** Every figure, date or attributed claim carries a source key that
  resolves in that file's own short Sources list or in `sources.md`.
- **No embellishment.** Keep modal verbs and provenance. Label forecasts with who made them.
- **Don't duplicate module content.** Link to module files instead.
- **Run the validator** (`python3 /home/user/ai-enablement/scripts/validate.py`) and fix every
  ERROR in the files you wrote.

## Output

Write the files, then write `/home/user/ai-enablement/research/runs/wave2/tax-archetype-synthesis-report.md`. The report covers:

- what each file draws on
- gaps
- items routed from modules that you placed
- suggested module changes

Then reply with a summary of **no more than 150 words**.


## Notes for this wave

- Use the assurance archetype as the model for structure and tone: read `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/ARCHETYPE.md` and skim its other archetype-level files. Match its module table format, including the **Evidence** column (strong: 50% or more of use cases graded A or B; moderate: 30-49%; thin: under 30%, as "thin (N of M A/B)"). Compute the counts from the current use-case YAML files (run the validator: it prints them).
- Professional responsibility was researched once as a cross-cutting topic; `guardrails.md` is its home. Modules should link to it rather than repeat it.
- The cross-cutting state-of-AI file corrected two landscape figures (EY data maturity; AICPA Top Issues). Use the corrected figures.
- Recognition cues must separate tax from assurance (audit of tax balances belongs to assurance) and cover in-house corporate tax teams.
- Grade A rule (2026-10-17): A needs a figure the named organization reports as measured; recollections or rough estimates are B.
- No build-process words in the product files (wave, deep dive, landscape scan, synthesis, verifier, research/runs paths).
- Finally, update `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/index.md`: move tax from "Not yet available" to the "Available archetypes" table (link `tax/ARCHETYPE.md`, extends professional-services, recognition cues, module ids, Status "Available"), keeping the table format.

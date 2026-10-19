**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are the editor who writes the **archetype-level files** an AI transformation advisor uses when
working with a leader in this field. Module files and use cases already exist under
`/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/` and `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/`. Today is 2026-10-19.

- **Archetype:** professional-services: the shared base for firms that sell expert work by the engagement or matter: law firms, consultancies, accounting and advisory firms, engineering and architecture firms, and in-house legal or shared-service teams that run like them. Covers how the firm wins, accepts, prices, staffs, delivers, quality-checks, bills and learns from work, plus firm finance and talent. Assurance and tax extend it with their field-specific work; security service providers also use it.
- **Extends:** none (it is the base). Extended by assurance and tax; also used by security service providers.
- **Inputs:** `/home/user/ai-enablement/research/runs/wave3/landscape-professional-services.md`, `/home/user/ai-enablement/research/runs/wave3/ps-x-guardrails-professional-conduct.md`, `/home/user/ai-enablement/research/runs/wave3/ps-x-state-of-ai-disruption.md`, `/home/user/ai-enablement/research/runs/wave3/pursuit-proposals-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave3/client-development-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave3/acceptance-risk-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave3/scoping-pricing-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave3/staffing-resourcing-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave3/delivery-management-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave3/work-production-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave3/quality-review-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave3/billing-collections-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave3/knowledge-management-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave3/talent-learning-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave3/firm-finance-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave3/pursuit-proposals-verification-report.md`, `/home/user/ai-enablement/research/runs/wave3/client-development-verification-report.md`, `/home/user/ai-enablement/research/runs/wave3/acceptance-risk-verification-report.md`, `/home/user/ai-enablement/research/runs/wave3/scoping-pricing-verification-report.md`, `/home/user/ai-enablement/research/runs/wave3/staffing-resourcing-verification-report.md`, `/home/user/ai-enablement/research/runs/wave3/delivery-management-verification-report.md`, `/home/user/ai-enablement/research/runs/wave3/work-production-verification-report.md`, `/home/user/ai-enablement/research/runs/wave3/quality-review-verification-report.md`, `/home/user/ai-enablement/research/runs/wave3/billing-collections-verification-report.md`, `/home/user/ai-enablement/research/runs/wave3/knowledge-management-verification-report.md`, `/home/user/ai-enablement/research/runs/wave3/talent-learning-verification-report.md`, `/home/user/ai-enablement/research/runs/wave3/firm-finance-verification-report.md` plus `/home/user/ai-enablement/research/runs/wave3/professional-services-consistency-report.md` (the landscape, the cross-cutting topic files and the synthesis reports,
  including their routed items). Also read the existing module files.

## Files to write, inside `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/`

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
| `sources.md` | The source landscape (conferences, bodies, journals, publications, communities), plus `last_researched: 2026-10-19` | |

Every file except `ARCHETYPE.md` is limited to 300 lines.

## Rules

- **Facts only from the inputs.** Every figure, date or attributed claim carries a source key that
  resolves in that file's own short Sources list or in `sources.md`.
- **No embellishment.** Keep modal verbs and provenance. Label forecasts with who made them.
- **Don't duplicate module content.** Link to module files instead.
- **Run the validator** (`python3 /home/user/ai-enablement/scripts/validate.py`) and fix every
  ERROR in the files you wrote.

## Output

Write the files, then write `/home/user/ai-enablement/research/runs/wave3/professional-services-archetype-synthesis-report.md`. The report covers:

- what each file draws on
- gaps
- items routed from modules that you placed
- suggested module changes

Then reply with a summary of **no more than 150 words**.


## Notes for this wave

- Use the assurance, tax and security archetypes as models for structure and tone: read `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/ARCHETYPE.md`, `.../tax/ARCHETYPE.md` and `.../security/ARCHETYPE.md`. Match the module table format, including the **Evidence** column (strong: 50% or more A/B; moderate: 30-49%; thin: under 30%, as "strong (N of M A/B)"). Compute counts from the current use-case YAML (the validator prints them).
- `ARCHETYPE.md` must stay at or under 100 lines.
- **There are only two cross-cutting files** (guardrails and professional conduct; state of AI and disruption). For `economics.md` draw on the firm-finance, scoping-pricing and billing-collections modules and reports; for `workforce.md` draw on talent-learning and staffing-resourcing. Link to module files rather than repeating them.
- **Recognition cues** must cover law firms, consultancies, accounting and advisory firms (their firm-operations side), engineering and architecture firms, and in-house legal and shared-service teams. Say clearly that audit opinions and attestation are assurance, tax returns and advice are tax, and security operations are security: those archetypes extend this one for their field's own work.
- **Value chain:** win (pursuit, client development) → accept and price (acceptance-risk, scoping-pricing) → staff and deliver (staffing-resourcing, delivery-management, work-production, quality-review) → bill and collect (billing-collections) → learn and run the firm (knowledge-management, talent-learning, firm-finance).
- `disruption.md` must cover the pricing shift (hourly to fixed, outcome and subscription fees), AI-native firms, outside capital (private equity, MSO structures) and the leverage pyramid, with the firm type for each example and who made each forecast.
- Some figures differ across inputs (for example McKinsey's share of outcome-based fees; the Crowe ownership plan; the NBER patent-lawyer trial's provenance). Use the consistency report and the verification reports' corrected wording (source keys were unified there; use the current keys in the module YAML); otherwise state only what is confirmed and flag the conflict in your report.
- Grade A rule (2026-10-17): A needs a figure the named organization reports as measured; recollections or rough estimates are B.
- No build-process words in the product files (wave, deep dive, landscape scan, synthesis, verifier, research/runs paths). Public sources only; no client-confidential information; no headcount targets for people.
- **Index and links.** Update `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/index.md`: move professional-services into the "Available archetypes" table (link `professional-services/ARCHETYPE.md`, Extends "—", recognition cues, module ids, Status "Available"), remove the "Not yet available" section if it is then empty, and update the closing line about consulting so it points to professional services as available. In `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/ARCHETYPE.md` and `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/ARCHETYPE.md`, turn the bold **professional-services** in the "It extends" sentence into a link to `../professional-services/ARCHETYPE.md` (keep the bold). In `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/ARCHETYPE.md`, replace "which is not yet written; use the method and the library for those parts" with a link to `../professional-services/ARCHETYPE.md`. Change nothing else in those three files, and keep each at or under 100 lines.

**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are the editor who writes the **archetype-level files** an AI transformation advisor uses when
working with a leader in this field. Module files and use cases already exist under
`/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/modules/` and `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/`. Today is 2026-10-21.

- **Archetype:** advisory: the advisory and outsourced-services side of accounting and advisory firms, especially those serving private, middle-market companies: client accounting services (outsourced accounting, close, fractional CFO, payroll), risk and controls advisory (internal-audit outsourcing, SOX readiness, client AI governance), transaction advisory, valuation, forensic and disputes, FP&A and performance consulting, and private client.
- **Extends:** professional-services (firm operations). Sits beside assurance (attest) and tax (tax technical work).
- **Inputs:** `/home/user/ai-enablement/research/runs/wave5/landscape-advisory.md`, `/home/user/ai-enablement/research/runs/wave5/adv-x-independence-pricing.md`, `/home/user/ai-enablement/research/runs/wave5/adv-x-state-of-ai-disruption.md`, `/home/user/ai-enablement/research/runs/wave5/advisory-consistency-report.md`, `/home/user/ai-enablement/research/runs/wave5/client-accounting-services-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave5/risk-controls-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave5/transactions-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave5/valuation-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave5/forensic-disputes-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave5/fpa-performance-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave5/private-client-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave5/client-accounting-services-verification-report.md`, `/home/user/ai-enablement/research/runs/wave5/risk-controls-verification-report.md`, `/home/user/ai-enablement/research/runs/wave5/transactions-verification-report.md`, `/home/user/ai-enablement/research/runs/wave5/valuation-verification-report.md`, `/home/user/ai-enablement/research/runs/wave5/forensic-disputes-verification-report.md`, `/home/user/ai-enablement/research/runs/wave5/fpa-performance-verification-report.md`, `/home/user/ai-enablement/research/runs/wave5/private-client-verification-report.md` (the landscape, the cross-cutting topic files and the synthesis reports,
  including their routed items). Also read the existing module files.

## Files to write, inside `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/`

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
| `sources.md` | The source landscape (conferences, bodies, journals, publications, communities), plus `last_researched: 2026-10-21` | |

Every file except `ARCHETYPE.md` is limited to 300 lines.

## Rules

- **Facts only from the inputs.** Every figure, date or attributed claim carries a source key that
  resolves in that file's own short Sources list or in `sources.md`.
- **No embellishment.** Keep modal verbs and provenance. Label forecasts with who made them.
- **Don't duplicate module content.** Link to module files instead.
- **Run the validator** (`python3 /home/user/ai-enablement/scripts/validate.py`) and fix every
  ERROR in the files you wrote.

## Output

Write the files, then write `/home/user/ai-enablement/research/runs/wave5/advisory-archetype-synthesis-report.md`. The report covers:

- what each file draws on
- gaps
- items routed from modules that you placed
- suggested module changes

Then reply with a summary of **no more than 150 words**.


## Notes for this wave

- Use the professional-services, assurance and tax archetypes as models for structure and tone (read their `ARCHETYPE.md`). Match the module table format, including the **Evidence** column (strong: 50% or more A/B; moderate: 30-49%; thin: under 30%, as "strong (N of M A/B)"), computed from the current use-case YAML (the validator prints the counts).
- `ARCHETYPE.md` at or under 100 lines. It extends professional-services: link `../professional-services/ARCHETYPE.md`, and say that firm operations (pursuit, pricing the firm's own work, staffing, billing, ownership) are there.
- **Two cross-cutting files** exist (independence, pricing and client data; state of AI and disruption). For `economics.md` use them plus the module reports (subscription and fixed fees, margins, PE consolidation); for `workforce.md` use the junior-pipeline and staffing points in the inputs and link to professional-services `workforce.md` for the firm-wide picture.
- **Recognition cues** must separate advisory from assurance (attest opinions, SOC reports), tax (returns, provision, tax advice) and professional-services (the firm's own operations). Name the **independence** limit plainly: some advisory services are restricted for the firm's own audit clients.
- **Value chain:** recurring outsourced services (client accounting services, FP&A) → risk and controls → deal and event work (transactions, valuation, forensic) → owner and family services (private client).
- No build-process words in the product files. Public sources only; no client-confidential information; no headcount targets for people.
- Grade A rule (2026-10-17): A needs a figure the named organization reports as measured.
- **Index and links.** Update `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/index.md`: add an advisory row to "Available archetypes" (link `advisory/ARCHETYPE.md`, Extends "professional-services", recognition cues, module ids, Status "Available"). In `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/professional-services/ARCHETYPE.md`, add advisory to the sentence that names the archetypes extending it (one clause, keep the file at or under 100 lines). Change nothing else in other archetypes.

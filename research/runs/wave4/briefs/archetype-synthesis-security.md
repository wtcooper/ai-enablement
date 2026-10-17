**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are the editor who writes the **archetype-level files** an AI transformation advisor uses when
working with a leader in this field. Module files and use cases already exist under
`/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/` and `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/`. Today is 2026-10-17.

- **Archetype:** security: Security: protecting an organization's systems, data, identities and people. Delivered by in-house security functions (the CISO organization) and by security service providers (managed detection and response, consultancies, penetration-testing and incident-response firms). The value chain follows NIST CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover). Covers how AI changes defenders' work and the security of AI itself.
- **Extends:** none (security service providers also use professional-services, not yet written; name it without a link)
- **Inputs:** `/home/user/ai-enablement/research/runs/wave4/landscape-security.md`, `/home/user/ai-enablement/research/runs/wave4/security-x-guardrails-regulation.md`, `/home/user/ai-enablement/research/runs/wave4/security-x-economics-business-model.md`, `/home/user/ai-enablement/research/runs/wave4/security-x-state-of-ai-disruption.md`, `/home/user/ai-enablement/research/runs/wave4/security-x-workforce-talent.md`, `/home/user/ai-enablement/research/runs/wave4/governance-risk-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave4/operations-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave4/threat-intelligence-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave4/incident-response-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave4/vulnerability-exposure-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave4/application-security-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave4/cloud-infrastructure-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave4/identity-access-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave4/data-privacy-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave4/human-risk-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave4/ai-security-synthesis-report.md`, `/home/user/ai-enablement/research/runs/wave4/governance-risk-verification-report.md`, `/home/user/ai-enablement/research/runs/wave4/operations-verification-report.md`, `/home/user/ai-enablement/research/runs/wave4/threat-intelligence-verification-report.md`, `/home/user/ai-enablement/research/runs/wave4/incident-response-verification-report.md`, `/home/user/ai-enablement/research/runs/wave4/vulnerability-exposure-verification-report.md`, `/home/user/ai-enablement/research/runs/wave4/application-security-verification-report.md`, `/home/user/ai-enablement/research/runs/wave4/cloud-infrastructure-verification-report.md`, `/home/user/ai-enablement/research/runs/wave4/identity-access-verification-report.md`, `/home/user/ai-enablement/research/runs/wave4/data-privacy-verification-report.md`, `/home/user/ai-enablement/research/runs/wave4/human-risk-verification-report.md`, `/home/user/ai-enablement/research/runs/wave4/ai-security-verification-report.md` (the landscape, the cross-cutting topic files and the synthesis reports,
  including their routed items). Also read the existing module files.

## Files to write, inside `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/`

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

Write the files, then write `/home/user/ai-enablement/research/runs/wave4/security-archetype-synthesis-report.md`. The report covers:

- what each file draws on
- gaps
- items routed from modules that you placed
- suggested module changes

Then reply with a summary of **no more than 150 words**.


## Notes for this wave

- Use the assurance and tax archetypes as models for structure and tone: read `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/ARCHETYPE.md` and `.../tax/ARCHETYPE.md`. Match the module table format, including the **Evidence** column (strong: 50% or more A/B; moderate: 30-49%; thin: under 30%, as "strong (N of M A/B)"). Compute counts from the current use-case YAML (the validator prints them).
- `ARCHETYPE.md` must stay at or under 100 lines (the validator requires a table of contents above 100 lines, so do not exceed it).
- Recognition cues must cover both in-house security teams (CISO, SOC, AppSec, IAM, GRC) and providers (MDR, MSSP, pentest, IR retainer), and separate security from assurance (attesting to controls, SOC 2 reports and assurance over AI belong to assurance).
- Map modules onto NIST CSF 2.0 functions in `value-chain.md`.
- Some figures differ across inputs (for example ISACA's 2026 AI incident-exercise figures: one file says 8%, another 71% have run none). Use the corrected wording in `/home/user/ai-enablement/research/runs/wave4/governance-risk-verification-report.md` if it exists; otherwise state only what the verification reports confirm and flag the conflict in your report.
- The landscape noted NIST and CISA pages showing "Super Intelligence (SI)" in place of "AI". Do not repeat that as fact; refer to the documents by their published titles where verified.
- Attacker use of AI appears only as context for defenders; no exploit or attack detail.
- Grade A rule (2026-10-17): A needs a figure the named organization reports as measured; recollections or rough estimates are B.
- No build-process words in the product files (wave, deep dive, landscape scan, synthesis, verifier, research/runs paths).
- Finally, update `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/index.md`: move security from "Not yet available" to the "Available archetypes" table (link `security/ARCHETYPE.md`, Extends "—", recognition cues, module ids, Status "Available"), keeping the table format.

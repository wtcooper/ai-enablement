**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are the editor who turns several research files into the **finished knowledge files** an AI
transformation advisor will use when it works with practitioners in this module. Today is 2026-10-19.

**Inputs:** `/home/user/ai-enablement/research/runs/wave3/landscape-professional-services.md`, `/home/user/ai-enablement/research/runs/wave3/ps-quality-review-practice.md`, `/home/user/ai-enablement/research/runs/wave3/ps-quality-review-discourse.md`, `/home/user/ai-enablement/research/runs/wave3/ps-quality-review-governance.md` (the landscape scan and the three angle deep dives)
**Vocabulary and YAML format:** `/home/user/ai-enablement/research/briefs/templates/vocabulary.md`

## Tasks

1. **Merge use cases.**
   - Combine the candidates from every angle. Remove duplicates: when two entries describe the same
     change to the work, merge them and keep every source.
   - Target **15–25** strong, distinct use cases.
   - Prefer entries graded A and B. Keep C and D entries only when they add something the others
     don't (for example, a frontier idea).
2. **Normalize.** Every field uses the vocabulary's values. Number the ids
   `professional-services-quality-review-01`, `-02` and so on.
3. **Cover the range.** Make sure the set spans the ladder (assist → delegate) and every change scope
   (step, process, model) wherever the evidence supports them. If a level or scope has no evidence, say so. Don't invent
   entries to fill it.
4. **Write the module file** (≤ 300 lines, with a table of contents at the top). It is written for an
   AI advisor to read during a live conversation, so it must be practical, plain and specific.
   Sections:
   - **What this module covers.** Two or three sentences.
   - **Processes and key steps**, as a table: step, what happens, work type, typical pain.
   - **Where AI is changing the work.** For each process area, the top use cases by id with a one-line
     summary, grouped by the four Reimagine lenses (improve, automate, delegate, reinvent).
   - **Interview probes.** 8–12 questions an advisor should ask someone in this module, with what each
     answer reveals.
   - **Metrics and benchmarks.** What to measure, with typical figures and sources where published.
   - **Guardrails.** Standards, regulatory points and the steps that need human judgment.
   - **Roles and how they evolve.**
   - **Frontier.** Dated signals of where this module is heading.
   - **Common objections**, with evidence-based responses.
   - **Sources**, as a short reference list. Full details live in the YAML.
5. **Write the use-case YAML:** a single list in the vocabulary format.

## Rules for module sources

- The module file may cite only source keys that appear in the YAML or in the module's own Sources
  section.
- Collect "Routed to other modules" items from the inputs into the synthesis report so the target
  module's synthesis can pick them up.

## Rules

- Do not add facts that aren't in the inputs. Do not change what a source says. Keep modal verbs and
  provenance. Never add causes, scope, dates or connective claims ("without a rise in staff", "ratios
  rise") that no source states. The pilot verifier corrected 21 of 25 entries, mostly for this kind
  of drift.
- Plain language. Explain each term of art in a few words the first time it appears.
- Quotations must be under 25 words.

## Output

- `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/quality-review.md`: the module markdown.
- `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/quality-review.yaml`: the YAML list. Valid YAML only.
- `/home/user/ai-enablement/research/runs/wave3/quality-review-synthesis-report.md`, a short synthesis report:
  - counts in and out
  - duplicates merged
  - coverage by ladder and change scope
  - grade mix
  - gaps
  - suggested improvements to the briefs

Then reply with a summary of **no more than 150 words**.


## Notes for this wave

- **This is the base archetype.** Professional services is the shared base that assurance and tax extend (security service providers also use it). Keep practice-specific substantive work (audit procedures, tax technical work, security operations) out: cross-reference the existing entries in `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/`, `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/` and `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/` by id where they overlap, rather than duplicating.
- Examples come from law, consulting, accounting and other advisory firms, and from in-house legal or shared-service teams (tagged `in-house` in notes). Say which kind of firm each example comes from.
- Also read the "Routed to other modules" sections of every `ps-*.md` file in `/home/user/ai-enablement/research/runs/wave3/` and pick up items routed to **quality-review**.
- **Overlapping modules.** Before writing, read the finished files of `work-production` in `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/` and `use-cases/` (if they exist yet). Cross-reference their entries by id instead of duplicating; keep in this module only what changes this module's work.
- Grade honestly. Most outcome figures are vendor-published or self-reported; label provenance and do not inflate grades. A conference talk not yet given is "scheduled" and cannot support A or B.
- Public sources only; no client-confidential information. No headcount targets for people; talk about roles and capacity.
- **Grade A rule (2026-10-17):** A needs a figure the named organization reports as measured (a tracked metric, a study or data). A practitioner's recollection or rough estimate quoted in a vendor case study, even with numbers, is grade B; keep the figure, labelled with its provenance.

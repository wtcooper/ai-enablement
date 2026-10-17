**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are the editor who turns several research files into the **finished knowledge files** an AI
transformation advisor will use when it works with practitioners in this module. Today is 2026-10-17.

**Inputs:** `/home/user/ai-enablement/research/runs/wave2/landscape-tax.md`, `/home/user/ai-enablement/research/runs/wave2/tax-compliance-individual-business-practice.md`, `/home/user/ai-enablement/research/runs/wave2/tax-compliance-individual-business-discourse.md`, `/home/user/ai-enablement/research/runs/wave2/tax-compliance-individual-business-governance.md` (the landscape scan and the three angle deep dives)
**Vocabulary and YAML format:** `/home/user/ai-enablement/research/briefs/templates/vocabulary.md`

## Tasks

1. **Merge use cases.**
   - Combine the candidates from every angle. Remove duplicates: when two entries describe the same
     change to the work, merge them and keep every source.
   - Target **15–25** strong, distinct use cases.
   - Prefer entries graded A and B. Keep C and D entries only when they add something the others
     don't (for example, a frontier idea).
2. **Normalize.** Every field uses the vocabulary's values. Number the ids
   `tax-compliance-individual-business-01`, `-02` and so on.
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

- `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/compliance-individual-business.md`: the module markdown.
- `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/use-cases/compliance-individual-business.yaml`: the YAML list. Valid YAML only.
- `/home/user/ai-enablement/research/runs/wave2/compliance-individual-business-synthesis-report.md`, a short synthesis report:
  - counts in and out
  - duplicates merged
  - coverage by ladder and change scope
  - grade mix
  - gaps
  - suggested improvements to the briefs

Then reply with a summary of **no more than 150 words**.


## Notes for this wave

- Also read the "Routed to other modules" sections of every `tax-*-*.md` file in `/home/user/ai-enablement/research/runs/wave2/` and pick up items routed to **compliance-individual-business**.
- Tax evidence is thin on measured outcomes. Do not inflate grades to reach the 50% A/B target; the module may honestly be rated thin.
- Cross-reference overlapping entries in other tax modules by id where you can see them, rather than duplicating.

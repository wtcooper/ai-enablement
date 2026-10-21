**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are the editor who turns several research files into the **finished knowledge files** an AI
transformation advisor will use when it works with practitioners in this module. Today is 2026-10-21.

**Inputs:** `/home/user/ai-enablement/research/runs/wave6/landscape-mid-market.md`, `/home/user/ai-enablement/research/runs/wave6/mm-private-company-practice.md`, `/home/user/ai-enablement/research/runs/wave6/mm-private-company-discourse.md`, `/home/user/ai-enablement/research/runs/wave6/mm-private-company-governance.md` (the landscape scan and the module research). Also read `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/ARCHETYPE.md` and its module files.
**Vocabulary and YAML format:** `/home/user/ai-enablement/research/briefs/templates/vocabulary.md`

## Tasks

1. **Merge use cases.**
   - Combine the candidates from every angle. Remove duplicates: when two entries describe the same
     change to the work, merge them and keep every source.
   - Target **15–25** strong, distinct use cases.
   - Prefer entries graded A and B. Keep C and D entries only when they add something the others
     don't (for example, a frontier idea).
2. **Normalize.** Every field uses the vocabulary's values. Number the ids
   `assurance-private-company-01`, `-02` and so on.
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

- `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/modules/private-company.md`: the module markdown.
- `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/use-cases/private-company.yaml`: the YAML list. Valid YAML only.
- `/home/user/ai-enablement/research/runs/wave6/private-company-synthesis-report.md`, a short synthesis report:
  - counts in and out
  - duplicates merged
  - coverage by ladder and change scope
  - grade mix
  - gaps
  - suggested improvements to the briefs

Then reply with a summary of **no more than 150 words**.


## Notes for this wave

- **Mid-market extension of the assurance archetype.** This module is new; the archetype's other modules already exist. Cross-reference their entries by full id instead of duplicating (for example `assurance-quality-management-NN`), and keep in this module only what is different at mid-market scale or for this engagement type.
- Say what kind of firm each example comes from (top-100, regional or local firm, PE-backed platform, Big Four, vendor, regulator or the counterparty).
- Also read the "Routed to other modules" sections of every `mm-*.md` file in `/home/user/ai-enablement/research/runs/wave6/` and pick up items routed to **private-company**.
- Grade honestly. Vendor benchmarks are not grade A for a firm's work outcome. A conference talk not yet given is "scheduled" and cannot support A or B.
- Public sources only; no client-confidential information.
- **Grade A rule (2026-10-17):** A needs a figure the named organization reports as measured; recollections and rough estimates are B.
- Do **not** edit `ARCHETYPE.md` or other modules; the coordinator adds the module to the archetype index.

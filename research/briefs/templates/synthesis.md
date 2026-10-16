# Brief template: module synthesis

Placeholders: `{archetype}`, `{module}`, `{input_paths}`, `{vocabulary_path}`, `{module_out}`,
`{usecases_out}`, `{report_out}`, `{today}`.

---

You are the editor who turns several research files into the **finished knowledge files** an AI
transformation advisor will use when it works with practitioners in this module. Today is {today}.

**Inputs:** {input_paths} (the landscape scan and the three angle deep dives)
**Vocabulary and YAML format:** `{vocabulary_path}`

## Tasks

1. **Merge use cases.**
   - Combine the candidates from every angle. Remove duplicates: when two entries describe the same
     change to the work, merge them and keep every source.
   - Target **15–25** strong, distinct use cases.
   - Prefer entries graded A and B. Keep C and D entries only when they add something the others
     don't (for example, a frontier idea).
2. **Normalize.** Every field uses the vocabulary's values. Number the ids
   `{archetype}-{module}-01`, `-02` and so on.
3. **Cover the whole ladder.** Make sure the set spans the four lenses (improve, automate, delegate,
   reinvent) wherever the evidence supports them. If a lens has no evidence, say so. Don't invent
   entries to fill it.
4. **Write the module file** (≤ 300 lines, with a table of contents at the top). It is written for an
   AI advisor to read during a live conversation, so it must be practical, plain and specific.
   Sections:
   - **What this module covers.** Two or three sentences.
   - **Processes and key steps**, as a table: step, what happens, work type, typical pain.
   - **Where AI is changing the work.** For each process area, the top use cases by id with a one-line
     summary, grouped by lens.
   - **Interview probes.** 8–12 questions an advisor should ask someone in this module, with what each
     answer reveals.
   - **Metrics and benchmarks.** What to measure, with typical figures and sources where published.
   - **Guardrails.** Standards, regulatory points and the steps that need human judgment.
   - **Roles and how they evolve.**
   - **Frontier.** Dated signals of where this module is heading.
   - **Common objections**, with evidence-based responses.
   - **Sources**, as a short reference list. Full details live in the YAML.
5. **Write the use-case YAML:** a single list in the vocabulary format.

## Rules

- Do not add facts that aren't in the inputs. Do not change what a source says.
- Plain language. Explain each term of art in a few words the first time it appears.
- Quotations must be under 25 words.

## Output

- `{module_out}`: the module markdown.
- `{usecases_out}`: the YAML list. Valid YAML only.
- `{report_out}`, a short synthesis report:
  - counts in and out
  - duplicates merged
  - coverage by lens and ladder
  - grade mix
  - gaps
  - suggested improvements to the briefs

Then reply with a summary of **no more than 150 words**.

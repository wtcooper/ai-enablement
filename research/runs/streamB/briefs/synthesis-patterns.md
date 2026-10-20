**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad.

You are the editor who writes the **agentic pattern files** of an AI transformation advisor's shared library. The
advisor reads one pattern file during Reimagine, Prioritize or Make the case, when an option uses that pattern. It
must be practical, plain and specific. Today is 2026-10-20.

**Inputs:** `/home/user/ai-enablement/research/runs/streamB/b-patterns-front-door.md`, `/home/user/ai-enablement/research/runs/streamB/b-patterns-transactions.md`, `/home/user/ai-enablement/research/runs/streamB/b-patterns-knowledge.md`,
`/home/user/ai-enablement/research/runs/streamB/b-patterns-continuous.md`, `/home/user/ai-enablement/research/runs/streamB/b-patterns-agents-scale.md`, the current `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/library/index.md`, and the archetype
use cases (`.../references/archetypes/*/use-cases/*.yaml`, searched by `pattern:`).
**Vocabulary:** `/home/user/ai-enablement/research/briefs/templates/vocabulary.md`

## Files to write

One file per pattern in `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/library/patterns/`: `intake-triage.md`, `document-to-decision.md`, `research-brief.md`,
`draft-review-loop.md`, `full-population-testing.md`, `monitor-diagnose-act.md`, `reconcile-exceptions.md`,
`service-agent-escalation.md`, `grounded-knowledge-assistant.md`, `end-to-end-case-agent.md`,
`bulk-transformation.md`. Each is at most 200 lines, with a table of contents if over 100 lines. Sections:

1. **What it is.** Two or three sentences, then how to recognize it in a user's description of their work.
2. **Where it fits.** Work types; when not to use it (anti-patterns).
3. **Up the ladder.** A table: rung (assist, augment, automate, delegate as relevant), what the AI does, what the
   person does, runtime class, the checkpoint that must exist before moving up.
4. **How it is built.** Inputs, the AI's role, human checkpoints, thresholds and sampling, logging and audit trail.
5. **Prerequisites.** Data, access, policy, skills.
6. **Failure modes and controls.** A table: failure, how it shows up, the control that catches it.
7. **Value and metrics.** Value levers, the metrics that show it works (including quality metrics), typical figures
   with provenance where published.
8. **Governance.** Where NIST AI RMF, ISO/IEC 42001, the EU AI Act or sector rules bite, briefly.
9. **Evidence.** Five to ten graded cross-industry examples (organization, industry, what changed, outcome with
   provenance, grade, source key), then "In the archetypes": the strongest archetype use-case ids for this pattern
   (full id and grade; at most eight, preferring A and B).
10. **Probes.** Five to eight questions for the user, each with what the answer reveals.
11. **Sources.** Short key list: key, title, publisher, date, URL.

Then update `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/library/index.md` §3: keep the table, link each pattern id to its file, and replace "These are working
definitions" with a sentence saying each pattern has a detailed file. Change nothing else in the index.

## Rules

- Facts only from the inputs or the archetype YAML. Do not change what a source says. Keep modal verbs and
  provenance. No unsourced connective claims. Quotations under 25 words.
- Grade A rule (2026-10-17): A needs a figure the named organization reports as measured; recollections and rough
  estimates are B. Benchmarks of a tool alone are not A for a work outcome.
- Describe tools by runtime class, never recommend a vendor. Public sources only.
- No build-process words in the product files (stream, deep dive, synthesis, verifier, research/runs paths).
- Every archetype id you cite must exist (check with grep).
- Run `python3 /home/user/ai-enablement/scripts/validate.py` and fix every ERROR in your files.

## Output

Write the files, then `/home/user/ai-enablement/research/runs/streamB/patterns-synthesis-report.md`: inputs used per file, conflicts resolved, gaps, and a
table of archetype use cases now tagged `pattern: other` that the inputs suggest should carry a pattern id (id,
suggested pattern, reason). Do **not** edit archetype files. Do not run git. Reply with a summary of no more than
150 words.

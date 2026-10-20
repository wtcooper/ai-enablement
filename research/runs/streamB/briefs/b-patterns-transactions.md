

**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are researching the **shared backbone library** of an AI transformation advisor: the reference files it uses
for any business, whatever its field. The advisor guides a team lead, practice leader or head of AI through
redesigning work with AI (Onboard → Frame → Map → Diagnose → Reimagine → Prioritize → Make the case → Plan).
Field-specific knowledge lives in archetypes (professional services, assurance, tax, security); this library
covers what is common across fields. Today is 2026-10-20.

- **Kind:** agentic patterns
- **Items:** `document-to-decision` and `reconcile-exceptions`
- **Focus:** for each pattern: what it does and where it fits (work types, cues in a user's description of their work); ladder range and which runtime class fits each rung; how it is built (inputs, the AI's role, the human checkpoints, thresholds and sampling, logging and audit trail); prerequisites (data, access, policy, skills); failure modes and the controls that catch them; value levers and the metrics that show it works (including quality metrics such as override, escalation and error rates); governance points (NIST AI RMF, ISO/IEC 42001, EU AI Act risk classes, sector rules) where they bite; how the pattern evolves up the ladder; and anti-patterns (where it should not be used)

Before you search, read:

- `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/library/index.md`
  (the current working definitions; your research deepens them)
- `/home/user/ai-enablement/research/briefs/templates/vocabulary.md` (controlled values: ladder, change scope,
  work types, patterns, runtime classes, functions, evidence grades, provenance)
- The archetype use cases: `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/*/use-cases/*.yaml`.
  Search them (`grep -n "pattern: <id>"` or `"function: <id>"`) for entries that already show your items. Cite
  them by full id and grade; do not re-research them. Your job is to add **cross-industry** evidence and the
  design knowledge they lack.

## Access

Follow the **Access** and **Precision rules** sections of
`/home/user/ai-enablement/research/briefs/templates/module-angle.md`: `curl -sSL --max-time 30 -A "Mozilla/5.0" <url>`,
`pdftotext` for PDFs, the text mirror `curl -sSL "https://r.jina.ai/<url>"` for blocked sites. **Web search is
rationed and shared with other agents**: plan searches, follow links and citations with `curl`, and save searches
for new directions. Mark each source `access: full` or `access: search-only`.

## Depth expectations

- Read **at least 25 distinct sources** across at least four types: academic and working papers, standards and
  regulator guidance (NIST AI RMF, ISO/IEC 42001, EU AI Act, sector regulators), research firms and surveys,
  named-organization case studies and engineering write-ups, vendor documentation with named customers, and
  practitioner discourse.
- Prefer 2024–2026 for anything AI-specific. Use older material only for foundations (process design, queueing,
  sampling, lean).
- Look explicitly for **quality evidence**: error rates, override and escalation rates, parallel runs, controlled
  trials, incident reports. Report its absence plainly.
- Cover several industries (financial services, healthcare, public sector, retail, manufacturing, technology,
  professional services), naming the industry of each example.

## Precision rules

- Every claim carries a source ref and a locator (page or section). Keep the source's modal verbs and tense
  ("announced", "piloting", "in production").
- Record what each statistic measures, its population, and who measured it (`self-reported`, `vendor-published`,
  `independent`).
- Grade examples with the vocabulary's evidence grades. **Grade A rule:** A needs a figure the named organization
  reports as measured (a tracked metric, a study or data); a recollection or rough estimate is B. A conference talk
  not yet given is "scheduled" and cannot support A or B.
- Do not embellish: no causes, scope, dates or connective claims a source does not state. Quotations under 25 words.
- Public sources only; no client-confidential information. No vendor recommendations: describe tools by runtime
  class.

## Output

Write a markdown file to `/home/user/ai-enablement/research/runs/streamB/b-patterns-transactions.md` with these sections, **one block per item** for sections 2-4:

1. **Summary.** Five to eight bullets across the items.
2. **Item profiles.** For each item, the fields in the Focus above, in plain language, each with source refs.
3. **Examples.** For each item, 6-12 graded examples across industries: organization (and industry), what changed
   in the work, ladder, change scope, outcome with provenance, grade, source ref. Then the archetype use-case ids
   you found for it (id and grade only).
4. **Expert moves and probes.** For each item, 5-10 questions or heuristics an advisor should use, with what each
   reveals.
5. **Evidence on what works and what fails.** Studies, failure analyses and measurements, with provenance.
6. **Gaps.**
7. **Sources.** ref, title, publisher or author, type, URL, date, access. Use the form `PUBLISHER-SHORT-YYYY`; reuse
   a key from the archetype YAML when it names the same document.

Then reply with a summary of **no more than 150 words**: examples by grade, sources by type, and the two most
important insights.

- 227 archetype use cases are tagged `pattern: other`. Skim those whose work resembles your patterns and note any that should carry one of your pattern ids (id and reason) in a short section before Gaps.



**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are researching the **shared backbone library** of an AI transformation advisor: the reference files it uses
for any business, whatever its field. The advisor guides a team lead, practice leader or head of AI through
redesigning work with AI (Onboard → Frame → Map → Diagnose → Reimagine → Prioritize → Make the case → Plan).
Field-specific knowledge lives in archetypes (professional services, assurance, tax, security); this library
covers what is common across fields. Today is 2026-10-20.

- **Kind:** function cards
- **Items:** `people-hr` and `technology-it`
- **Focus:** for each business function: its main processes and key steps (with work types); typical pain points; the top AI opportunities across the ladder (assist to delegate) and change scope (step, process, model), with graded evidence; metrics and benchmarks (with sources); interview probes for a function leader; guardrails and the decisions that need human judgment; how roles change. Cover in-house functions in any organization, not one field. Use established process frameworks for the process list only (no framework ids)

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

Write a markdown file to `/home/user/ai-enablement/research/runs/streamB/b-functions-people-technology.md` with these sections, **one block per item** for sections 2-4:

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

- For `technology-it`, cover the IT function's own work (service desk, operations, software delivery, architecture); security operations is the security archetype: cite its entries by id instead.
- For `risk-compliance-legal` and `finance-accounting`, cover in-house teams in any organization; firms that sell legal, audit or tax services are the professional-services, assurance and tax archetypes.

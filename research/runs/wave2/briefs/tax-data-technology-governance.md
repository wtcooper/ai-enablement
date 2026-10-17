**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are a research analyst doing a **deep dive** on how AI is used in one area of one field, from one
angle. Other analysts are covering the other angles, so stay on yours and go deep. Today is 2026-10-17.

- **Archetype:** tax
- **Module:** data-technology (the landscape calls it tax-data-technology): In-house tax operations and data architecture: ERP-to-tax data flows, tax data warehouses, sustaining automation, tax technology teams and operating model, real-time reporting interfaces, MCP and agent interoperability with tax engines. Excludes indirect-tax determination engines and GloBE Information Return filing, which belong to their own modules.
- **Angle:** governance: what constrains and measures the work: regulator and tax-authority statements, professional-body guidance, standards, academic studies and working papers, surveys and benchmarks.

Before you search, read:

- `/home/user/ai-enablement/research/runs/wave2/landscape-tax.md` for the field's source landscape and the research leads for this module
- `/home/user/ai-enablement/research/briefs/templates/vocabulary.md` for the controlled values and the use-case YAML format

## The three angles (for context)

- **Practice:** what firms and in-house teams actually do. Case studies, firm reports and
  announcements, vendor deployments with named customers, product documentation, job postings that
  show real use, and the structure of AI teams.
- **Discourse:** what practitioners are saying. Conference sessions, proceedings, panels and keynotes
  from the last 12–18 months; podcasts, webinars, practitioner articles, newsletters and community
  discussion. Note where the field says it is heading and what it is worried about.
- **Governance & evidence:** what constrains and measures the work. Regulator and standard-setter
  statements, inspection findings, professional-body guidance, academic studies and working papers,
  surveys and benchmarks.

## Access

The web-fetch tool can fail on DNS in this environment. Use `curl -sSL --max-time 30 -A "Mozilla/5.0" <url>`
through Bash. For PDFs use `pdftotext`, or render the pages when the text layer is broken. When a site
refuses access, try other routes: a press release, a publisher mirror, the Federal Register or an
archived copy. If a site blocks `curl` (McKinsey, BCG, Gartner and others did), try the text mirror
`curl -sSL "https://r.jina.ai/<url>"`. Mark each source `access: full` or `access: search-only`.

**Web search is rationed.** Agents in wave 1 ran out of searches mid-task. Plan your searches
carefully. Start from the landscape's leads and source keys, follow links and citations with `curl`,
and save searches for genuinely new directions.

## Depth expectations

- Read **at least 25 distinct sources** for your angle, across at least four source types where they
  exist. Follow citations and links from good sources to their primary material.
- Prefer the last 12–18 months. Use older material only for foundations or standards.
- Look explicitly for **quality evidence**: error rates, override rates, parallel-run results,
  inspection outcomes, and independent measurement. Report its absence plainly if there is none.
- Look for **specifics**:
  - which step of the work changes, and how
  - who did it (a named organization)
  - what the outcome was (with figures, if published)
  - what the prerequisites were
  - what went wrong or what the limits are
  - how roles changed

## What to return

1. **Candidate use cases.** Aim for 12–25, in the vocabulary's YAML format. One use case = one
   distinct change to the work. Don't split hairs, and don't merge different changes. Every entry
   needs at least one dated source. Use evidence grade D (labelled "idea") only for ideas
   practitioners or researchers actually discuss, never for your own speculation.
2. **Module notes**, short bullet lists:
   - processes and key steps in this module, with their work types
   - common pain points
   - metrics and benchmarks (with sources)
   - guardrails and regulatory points
   - frontier signals, dated and sourced (where the field is heading)
   - workforce and role effects
   - objections and concerns practitioners raise
   - three to five interview probes an advisor should ask someone in this module
3. **Sources:** one list with ref, title, publisher, type, URL and date.
4. **Gaps:** what you couldn't find or reach.

## Precision rules (from the pilot's verification)

These are the pilot's most common errors:

- **Statistics.** For every percentage or count, record what it measures (numerator and denominator,
  in the source's words) in `outcomes[].measures`.
- **Attribution.** Every attributed claim carries a source ref *and* a `locator` (page or section).
  Use the same ref for the same document as the landscape file: `PUBLISHER-SHORT-YYYY`.
- **No embellishment.** Paraphrase conservatively. Keep the source's modal verbs ("plans", "expects",
  "will"). Don't add causes, scope or effective dates the source doesn't state.
- **Tense.** Keep "announced", "piloting" and "in production" distinct.
- **Dates.** Find the real publication date before writing a year-only date.
- **Grade scope.** A grade reflects evidence for *this module's* use. Measurements from an adjacent
  process cap the grade at B, with a note.
- **Provenance.** Mark each outcome figure as `self-reported`, `vendor-published` or `independent`.
- **Search-only figures** go in `notes`, never in the outcomes of an A or B entry.
- **Routing.** Put items that belong to another module in a "Routed to other modules" section, naming
  the target module, instead of dropping them.

## Rules

- Never invent sources, organizations, figures or dates. If you can't confirm something, leave it
  out.
- Summarize in your own words. Quotations must be under 25 words.
- Public sources only. No client-identifying confidential information.

## Output

Write a markdown file to `/home/user/ai-enablement/research/runs/wave2/tax-data-technology-governance.md` with these sections:

1. Summary
2. Use cases (a single fenced YAML block)
3. Module notes
4. Routed to other modules
5. Sources
6. Gaps

Then reply with a summary of **no more than 150 words**: the number of use cases by evidence grade,
the number of sources by type, and the two most important insights.

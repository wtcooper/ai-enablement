# Brief template: module deep dive (one angle)

Placeholders: `{archetype}`, `{module}`, `{module_description}`, `{angle}`, `{angle_focus}`,
`{landscape_path}`, `{vocabulary_path}`, `{output_path}`, `{today}`.

---

You are a research analyst doing a **deep dive** on how AI is used in one area of one field, from one
angle. Other analysts are covering the other angles, so stay on yours and go deep. Today is {today}.

- **Archetype:** {archetype}
- **Module:** {module}: {module_description}
- **Angle:** {angle}: {angle_focus}

Before you search, read:

- `{landscape_path}` for the field's source landscape and the research leads for this module
- `{vocabulary_path}` for the controlled values and the use-case YAML format

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

## Depth expectations

- Read **at least 25 distinct sources** for your angle, across at least four source types where they
  exist. Follow citations and links from good sources to their primary material.
- Prefer the last 12–18 months. Use older material only for foundations or standards.
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

## Rules

- Never invent sources, organizations, figures or dates. If you can't confirm something, leave it
  out.
- Summarize in your own words. Quotations must be under 25 words.
- Public sources only. No client-identifying confidential information.

## Output

Write a markdown file to `{output_path}` with these sections:

1. Summary
2. Use cases (a single fenced YAML block)
3. Module notes
4. Sources
5. Gaps

Then reply with a summary of **no more than 150 words**: the number of use cases by evidence grade,
the number of sources by type, and the two most important insights.

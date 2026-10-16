# Brief template: archetype cross-cutting topic

Placeholders: `{archetype}`, `{archetype_description}`, `{topic}`, `{topic_focus}`, `{landscape_path}`,
`{output_path}`, `{today}`.

---

You are researching one cross-cutting topic for a business archetype. The advisor needs it to help a
leader in this field think beyond individual processes. Today is {today}.

- **Archetype:** {archetype}: {archetype_description}
- **Topic:** {topic}: {topic_focus}

Before you search, read `{landscape_path}` for the source landscape and source keys.

## Access and precision

Follow the **Access** and **Precision rules** sections of
`/home/user/ai-enablement/research/briefs/templates/module-angle.md`:

- use `curl` and `pdftotext`
- give every claim a source ref and a locator
- don't embellish
- record what each statistic measures and who measured it
- keep "announced", "piloting" and "in production" distinct
- use real dates

## Depth

- Read **at least 25 distinct sources** across at least four source types.
- Prefer the last 12–18 months, plus authoritative foundations.
- Look for specifics, figures and named organizations.
- Separate facts from forecasts, and label forecasts with who made them.

## Output

Write a markdown file to `{output_path}` with these sections:

1. **Summary.** Five to eight bullets.
2. **Findings.** Organized under the topic's natural headings. Every factual sentence carries a
   source ref.
3. **What it means for an AI transformation conversation.** Implications, interview probes, and
   objections with evidence-based responses.
4. **Frontier signals.** Dated and sourced.
5. **Sources.** ref (`PUBLISHER-SHORT-YYYY`, reusing the landscape's refs), title, publisher, type,
   URL, date, access.
6. **Gaps.**

Then reply with a summary of **no more than 150 words**.

**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are researching one cross-cutting topic for a business archetype. The advisor needs it to help a
leader in this field think beyond individual processes. Today is 2026-10-19.

- **Archetype:** professional-services: Professional services: how advisory and professional firms run their business and deliver client work across the client lifecycle. Covers management, strategy and technology consulting, the firm-operations side of accounting and advisory firms, law firms and legal operations (including in-house legal and shared-service teams that work like firms), and engineering, architecture and other project-based advisory firms. The base archetype that assurance and tax extend and that consulting teams use.
- **Topic:** state-of-ai-disruption: AI adoption across consulting, legal and accounting firms (surveys, maturity spread, measured versus announced), AI-native firms and productised 'service as software' offers, private equity and outside capital, client in-sourcing with AI, and business-model scenarios for the billable hour and the leverage pyramid.

Before you search, read `/home/user/ai-enablement/research/runs/wave3/landscape-professional-services.md` for the source landscape and source keys.

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

Write a markdown file to `/home/user/ai-enablement/research/runs/wave3/ps-x-state-of-ai-disruption.md` with these sections:

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

- The landscape file proposed some module names differently: client-relationship-development = client-development, firm-finance-performance = firm-finance. Use the new ids.
- Tag in-house legal or shared-service examples in notes as 'in-house'. Keep practice-specific substantive work (audit procedures, tax technical work) out; that belongs to the assurance and tax archetypes.
- Public sources only; no client-confidential information.

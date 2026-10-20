**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are researching one cross-cutting topic for a business archetype. The advisor needs it to help a
leader in this field think beyond individual processes. Today is 2026-10-20.

- **Archetype:** advisory: the advisory and outsourced-services side of accounting and advisory firms, especially those serving private, middle-market companies. Extends professional-services (firm operations) and sits beside assurance and tax (attest and tax technical work).
- **Topic:** independence-pricing: independence, pricing and client data in advisory: which advisory and CAS services are restricted for attest clients (AICPA independence rules, SEC and PCAOB for public clients, IESBA), alternative practice structures, how advisory and CAS are priced (subscription, fixed fee, value pricing) and how AI shifts pricing and margins, and client-data confidentiality duties when AI handles client books and records.

Before you search, read `/home/user/ai-enablement/research/runs/wave5/landscape-advisory.md` for the source landscape and source keys.

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

Write a markdown file to `/home/user/ai-enablement/research/runs/wave5/adv-x-independence-pricing.md` with these sections:

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

- Use-case ids follow the form advisory-<module>-NN. Module ids for this archetype: client-accounting-services, risk-controls, transactions, valuation, forensic-disputes, fpa-performance, private-client (the landscape used the older names transaction-advisory, consulting-fpa and risk-advisory).
- Note in each entry whether the firm is a top-100 or mid-market accounting firm, a Big Four firm, a PE-backed platform, an AI-native provider or a vendor. Where a service is restricted for the firm's own audit clients (independence), say so.
- Firm operations (pricing the firm's own work, staffing, billing, PE ownership) belong to professional-services, attest work to assurance, tax technical work to tax: route them, do not research them here.
- Public sources only; no client-confidential information.

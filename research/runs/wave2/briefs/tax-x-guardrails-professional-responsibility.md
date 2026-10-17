**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are researching one cross-cutting topic for a business archetype. The advisor needs it to help a
leader in this field think beyond individual processes. Today is 2026-10-17.

- **Archetype:** tax: Tax: tax compliance, tax accounting (provision), indirect tax, transfer pricing, international tax and the global minimum tax, controversy, research and advisory, and tax data and technology; delivered by accounting and tax firms (Big Four, mid-tier, small practices, AI-native entrants) and by in-house corporate tax departments. Extends professional-services.
- **Topic:** guardrails-professional-responsibility: Regulators, standards and professional obligations that constrain AI in tax work across jurisdictions: Circular 230 and IRS OPR (including Alert 2026-19), §7216 and §6713 consent and disclosure, AICPA SSTS and the CART council, PCRT (UK), the Tax Practitioners Board (Australia), data protection, AI-related sanctions and hallucination cases, liability and insurance, preparer signing obligations, and the steps that need human judgment.

Before you search, read `/home/user/ai-enablement/research/runs/wave2/landscape-tax.md` for the source landscape and source keys.

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

Write a markdown file to `/home/user/ai-enablement/research/runs/wave2/tax-x-guardrails-professional-responsibility.md` with these sections:

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

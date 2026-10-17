**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are researching one cross-cutting topic for a business archetype. The advisor needs it to help a
leader in this field think beyond individual processes. Today is 2026-10-17.

- **Archetype:** security: Security: protecting an organization's systems, data, identities and people from threats. Delivered by in-house security functions (the CISO organization) and by security service providers (managed security and MDR providers, consultancies, penetration-testing and incident-response firms). The value chain follows NIST CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover). Covers how AI changes defenders' work and the security of AI itself; attacker use of AI only as context for defenders.
- **Topic:** economics-business-model: How security is funded and sold: security budgets as a share of IT and revenue, cost structure of a SOC, MSSP and MDR pricing (per endpoint, per user, per alert, outcome-based), consolidation of security platforms, private-equity ownership of providers, cyber insurance economics, and pricing pressure from AI.

Before you search, read `/home/user/ai-enablement/research/runs/wave4/landscape-security.md` for the source landscape and source keys.

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

Write a markdown file to `/home/user/ai-enablement/research/runs/wave4/security-x-economics-business-model.md` with these sections:

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
- Public sources only. Do not collect exploit code, malware, or step-by-step attack instructions; describe attacker capabilities only at the level defenders need.
- The landscape file uses older module names: security-governance-risk = governance-risk, security-operations = operations, data-security-privacy = data-privacy. Use the new ids.

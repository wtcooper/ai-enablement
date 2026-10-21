# Widen tax synthesis report (compliance-individual-business, research-advisory)

Run 2026-10-21. Inputs: `mm-widen-tax.md`, `landscape-mid-market.md`, and the "Routed to other modules" sections of every `mm-*.md` in this folder that name the two modules (`mm-widen-tax.md`, `mm-multistate-private-combined.md`, `mm-private-company-practice.md`; `mm-private-company-governance.md` and `mm-nonprofit-government-combined.md` route OPR and section 7216 to the tax archetype in general). The multistate-private module was not touched. `python3 scripts/validate.py`: 0 errors; the only warnings for these files are the existing content-target warnings (entry count above 25 and A/B share below 50%).

## compliance-individual-business

**Added (26-31), all grade C, all `last_reviewed` 2026-10-21**

| New id | Research id | Use case | Firm kind in the sources |
|---|---|---|---|
| -26 | new-01 | Reasonable-compensation study for S corporation owners | AI-native vendor (Instead); WageProof (not described as AI); no firm |
| -27 | new-02 | Shareholder and partner basis, AAA and distribution limits, negative-basis alerts | Vendors (Instead, Intuit, Thomson Reuters); no firm |
| -28 | new-03 | One agent per client across 1040, 1120-S, 1065, 1041 | AI-native vendor (Instead); no named customer |
| -29 | new-04 | Owner quarterly estimates with safe harbor | One vendor page (Instead) |
| -30 | new-06 | AI-native platform replaces the tax engine and e-files entity returns | AI-native vendor (Instead); WCG, a regional firm, as critic |
| -31 | new-07 | Estate, gift and fiduciary returns (706, 709, 1041) | Vendor roadmap (Instead); Thomson Reuters fiduciary software without AI |

**Merged into existing entries (all sources kept; no grade changed)**
- `-12` (AI return review) took research new-05 (entity-return review: K-1 ties, wage and QBI allocation). Same step and pattern. Added: Filed (small-firm customers Paramount Tax and JCG Tax; illustrative QBI sample), Instead, the NYSSCPA reviewer course, and the sponsored summit "preparers re-checked everything" account. Grade stays B on the existing named users.
- `-24` (AI-native roll-ups) took research new-08 (Aardvark Tax Advisors, the practice of venture-backed Cynch AI, growing organically and by acquisition; job posting). Grade stays B.
- Routed source additions: `-02` WK-SCANGA-2026 (Scan general availability 2026-06-29; 10-15 minutes per manual K-1, up to 60-80% reduction, vendor); `-05` CPAPA-BLACKORE-2026 (the same Maxwell Locke & Ritter quote; top-100 firm); `-06` BASIS-SERIESB-2026 ("Top 25 firm" unverified), CPAPA-ACCRUAL-2026 (Accrual focused on individual returns), OLIVER-PARTNERSHIP-2026 (liability); `-18` OLIVER-BOSUMMIT-2026 (re-checking cost; 2-4 weeks versus 18-24 months implementation, statements); `-21` CPAPA-SETTLE-2026 (open consent question; non-AI path).

**Module file:** new §10 "Mid-market firms and owner-managed clients" (who supplies the evidence, survey size bands, owner-level steps, entity-return review, engine choice, K-1 coverage, review cost, owner-work guardrails, a short trusts-estates-gifts paragraph, frontier dates, four probes); Sources renumbered to §11 and extended with every new key; §3 gains a pointer line for `#26`-`#31` and notes on `#12` and `#24`. Header updated (31 entries). To stay at 299 lines, §3 and §11 bullets were unwrapped onto single lines; no wording or facts were removed.

## research-advisory

**Added (26-28)**

| New id | Research id | Use case | Grade | Firm kind |
|---|---|---|---|---|
| -26 | new-01 | Owner-facing S-election calculators and agent-built S corporation plans | C | Gelt (AI-native firm); Instead (vendor); CoCounsel |
| -27 | new-02 | Planning opportunities mined from filed returns across the book | C | Vendors (Intuit, Wolters Kluwer, Filed); WCG (regional firm) comment |
| -28 | new-05 | Informed consent and verification for AI in estate planning (idea) | D | ACTEC Fellows; practitioner newsletter |

**Merged (no grade changed)**
- `-14` (drafting from researched authority) took research new-03: One Stop CPA, a seven-person digital firm, uses Blue J then enterprise ChatGPT to draft client explanations; deal and relocation answer "within two hours" (CEO's statement, self-reported). Grade stays B.
- `-13` (document-grounded analysis of trust documents) took research new-04: Wealth.com's estate-document engine (advisor-side wealth management, vendor counts). Grade stays B.
- `-25` (pricing) gained TR-SOTP-2026: 78% primarily bill hourly; advisory margins 20-24% against 28% for individual preparation.
- `-09` gained a cross-reference to `-26` only.

**Module file:** new §10 "Mid-market firms and owner clients" (demand and price, planning-tool uptake, what this pass added, the Sam Brown CPA small-firm signal from the private-company-practice routing, evidence, guardrails, trusts-estates-gifts, one probe); Sources renumbered to §11; the AICPA-TAXSW-2026 "not in the YAML" row was removed because the key is now in the YAML, and TR-SAMBROWN-2026 was added. §3 lists `#26`-`#28`. Header updated (28 entries; A 0, B 11, C 10, D 7). 287 lines.

## Grade changes

None. No new evidence measured an existing entry. No new entry reaches A or B; the only named-firm accounts (One Stop CPA, Aardvark) were merged into existing B entries.

## Key reconciliation (same document, existing key reused)

| Research key | Used here | Reason |
|---|---|---|
| CPAPA-7216-2026 | CPAPA-SETTLE-2026 | Same URL already keyed in advisory client-accounting-services |
| BASIS-B-2026 | BASIS-SERIESB-2026 | Same URL already keyed in advisory |
| ACCRUAL-2026 | CPAPA-ACCRUAL-2026 | Same URL keyed in tax `sources.md` |
| BLACKORE-2026 (CPA Practice Advisor URL) | CPAPA-BLACKORE-2026 | BLACKORE-2026 is already the Sovereign Magazine article in this YAML and `sources.md` |
| ATL-BOSUMMIT-2026 | BLACKORE-SUMMIT-2026 | Same podcast URL already in the YAML |
| ACCTGPOD-477-2026 | ACCTPOD-477-2026 | Same URL already in the YAML |
| OLIVER-1065-2026 (multistate research) | OLIVER-PARTNERSHIP-2026 | Same URL; widen-tax key used |

TR-SOTP-2026 is labelled independent in `mm-widen-tax.md` and vendor-published in `mm-private-company-governance.md`. It is marked vendor-published (vendor-owned survey) here because Thomson Reuters sells the tax and advisory tools.

## Not used or routed elsewhere

- Controversy (TIGTA large-partnership AI, IRS soft letters, Instead's late-election workflow), data-technology (engine replacement; data foundation) and the future client-advisory archetype (Wiss and Basis) were left to those modules.
- The PTET half of research new-01 points to `tax-multistate-private-14`, which the parallel agent wrote. That id was checked on 2026-10-21; if the module is renumbered, update the notes in `tax-research-advisory-26` and research-advisory §10.
- The multistate routing of "composite and pass-through entity tax preparation for owners" to this module came with no source or fact. Nothing was added, and §10 points state PTET and composite work to multistate-private.
- The private-company-practice routing names "Ready to Advise at a small firm", but the inputs carry no detail beyond the Sam Brown case study's claim about junior staff. Only that claim is used.
- Search-summary items were not used as evidence: the Publication 505 safe-harbor note (kept in `-29` notes as unverified), CCH Axcess Advisor's general-availability date, and the Datagrid and Digiqt trust-agent blogs.

## Gaps

- No quality evidence (error, override or parallel-run rates) for AI on S corporation or partnership returns, basis, reasonable compensation, entity choice or fiduciary returns.
- No named mid-market firm for reasonable compensation, basis, owner estimates, entity-return review, S-election or PTET modelling, or estate work. The named firms are small or AI-native (One Stop CPA, Paramount Tax, JCG Tax, Aardvark), or they already sit in existing entries (Maxwell Locke & Ritter, Armanino, Boulay, WCG).
- Section 7216 consent format for 1065 and 1120-S returns was not checked; nor were IRS Publication 505 or the full TIGTA report.
- Practitioner forums were not reached. Taxposium sessions were read as titles only.
- Other files outside scope with the same document under another key: `assurance/use-cases/nonprofit-government.yaml` cites CPAPA-7216-2026 in its notes for the document keyed CPAPA-SETTLE-2026 elsewhere.
- Compliance-individual-business now has 31 entries (target 15-25) and 32% A/B; research-advisory has 28 and 39%. Both are reported as warnings, not errors.

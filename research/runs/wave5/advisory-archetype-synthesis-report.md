# Advisory archetype synthesis report

Date: 2026-10-21. Brief: `research/runs/wave5/briefs/archetype-synthesis-advisory.md`.

## Files written

All in `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/`:

| File | Lines | Limit |
|---|---|---|
| ARCHETYPE.md | 100 | 100 |
| interview-guide.md | 191 | 300 |
| value-chain.md | 145 | 300 |
| economics.md | 178 | 300 |
| state-of-ai.md | 145 | 300 |
| frontier.md | 102 | 300 |
| guardrails.md | 189 | 300 |
| workforce.md | 141 | 300 |
| disruption.md | 155 | 300 |
| objections.md | 76 | 300 |
| sources.md | 269 | 300 (`last_researched: 2026-10-21`) |

Every file over 100 lines has a table of contents. Every cited key (150 keys) resolves in `sources.md` Part B (a script
check found none missing); Part B also holds the 10 extra keys cited only in the Part A landscape tables. Keys follow the
unified module keys from the consistency report (KARBON-SOAI-2026, JOFA-ETHAI-2026, IESBA-TECHREV-2023, JOFA-AIPA-2026,
JOFA-PEEC-2026, TR-FOPPR-2026 / TR-FOPREPORT-2026, ICAEW-JUNIOR-2026).

Other edits: `archetypes/index.md` gained one advisory row (re-read just before editing). In
`professional-services/ARCHETYPE.md`, the "What it extends" sentence now names advisory with assurance and tax (one
clause, rewrapped; the file stays at 100 lines). No module, use-case, assurance or tax file was edited.

`python3 scripts/validate.py`: 0 errors. Advisory warnings are the existing A/B-share and entry-count warnings for five
use-case files.

Evidence column (from the validator's current counts): CAS strong (12 of 24), risk-controls strong (12 of 23),
transactions moderate (5 of 16), forensic-disputes moderate (5 of 15), private-client moderate (6 of 17), valuation thin
(3 of 15), fpa-performance thin (2 of 14).

## What each file draws on

| File | Main inputs |
|---|---|
| ARCHETYPE.md | Landscape §1, §10, §11 (journey markers); independence file §2.1; module headers and §1; validator counts |
| interview-guide.md | Probes in both cross-cutting files (§3.2); module §4 probes, rephrased at archetype level; vocabulary from module §1-2 |
| value-chain.md | Module §2 step tables and §3 entries (linked by id, not repeated); data-layer figures from Intuit, KPMG, RSM, Forvis Mazars |
| economics.md | Independence file §2.3 (pricing, margins, outcome fees, contingent-fee rules); disruption file §2.3 and §2.6 (PE consolidation, roll-ups, scenarios); CAS, risk-controls and transactions module §5 figures |
| state-of-ai.md | Disruption file §2.1-2.4; landscape §6 and §9; module §5 survey rows; CAS `#01` for the one independent study |
| frontier.md | Landscape §12; both cross-cutting files §4; module §8 lists (dates as verified in the modules) |
| guardrails.md | Independence file §2.1-2.4 (SEC, PCAOB, AICPA, IESBA, FTC, 7216, OPR, vendor terms, controls); module §6 by line; verification-report corrections (SEC exception scope, Rule 707 status) |
| workforce.md | Disruption file §2.5; module §7 sections; CAS and risk-controls hiring data; links to professional-services workforce |
| disruption.md | Disruption file §2.2-2.6 and §3; independence file §2.3; module §9 counter-evidence |
| objections.md | Both cross-cutting files §3.3; module §9 objections lifted to archetype level |
| sources.md | Landscape §2-§9 and §14 for Part A; YAML source rows, module §10 lists and cross-cutting source tables for Part B |

## Gaps

- **No fee, realisation or margin data tied to AI** at any firm; CAS margin figures are podcast testimony. The 2026 CAS
  Benchmark Survey (December 2026) is the first likely dataset.
- **Independence for private-company attest clients.** The AICPA Code text (ET 1.295, ET 1.510) was login-gated in
  every run; guardrails §3 rests on 2015-2016 descriptions and says so.
- **No adoption survey** of accounting-firm transaction, forensic, valuation or private-client teams; state-of-ai uses
  general practitioner surveys and adjacent ones (ACFE, Datasite, BVR polls, Citi).
- **Source conflicts noted and handled:**
  - Thomson Reuters client figures differ by page: 78% / 6% / 32% (press release, used as TR-FOPPR-2026) against
    77% / 5% / 31% (the Europe landing page read for the independence file). The 34% unapproved-use figure is cited
    to the report page (TR-FOPREPORT-2026).
  - Rule 707 status: the forensic module cites the September 2026 Standing Committee report ("continued
    consideration"); the valuation module cites the October agenda book (vote to withdraw as published and study a
    modified proposal). frontier.md and guardrails.md state both, each with its key.
  - The same Bloomberg Law pricing article carries two keys and two URL paths in the cross-cutting files
    (BBLAW-PRICING-2026 `/esg/`, BLOOMBERG-PRICING-2026 `/financial-accounting/`). The archetype files use
    BBLAW-PRICING-2026 only.
  - RSM survey keys: the YAML's RSM-MMAI-2026 is the newsroom release (2026-07-21), while the disruption research read
    the survey introduction page. Archetype figures from that survey cite both RSM-MMAI-2026 and CPAPA-RSMMM-2026.
  - CUATRECASAS-AIOMNIBUS-2026 has no URL on record in the risk-controls module; sources.md says so.
- **Unverified items kept out:** the Botkeeper "98% accuracy" claim, the Digits/CLA 15%-of-revenue figure, the EY
  agentic-coverage claim, the AICPA/CIMA 1,446-leader survey and the NASBA 5% letter (all snippet-only or
  single-source).

## Items routed from modules that were placed

| Routed item (from) | Placed in |
|---|---|
| Firm pricing and fee models: BILL 66% / 60%, AICPA MAP, Blue J 69%, RKL and Wipfli pilots, RSM "margin or price" framing, OPR section 10.27 (CAS, risk-controls, transactions, fpa) | economics §4 and §6; disruption §2; interview-guide §4 |
| Withum's CAS-to-advisory route and $70M (CAS) | economics §1; value-chain §1; disruption §6 |
| Outcome-linked fees and the contingent-fee edge, BBTAX-SH-2026 (independence file, transactions, fpa) | economics §4; guardrails §4; objections §1 |
| PE and APS: Crowe/KKR, GT/CBIZ, IESBA workstream, PEEC second exposure draft, deal-tracker purchases of forensic and valuation firms (all modules) | economics §7; disruption §4; frontier §2 and §4; guardrails §3 |
| AI-native roll-ups and entrants: Current, Multiplier, Atlas, Botkeeper (disruption file, CAS) | economics §7; disruption §3-4 |
| Junior pipeline and hiring data: Intuit, Karbon, Stanford/ADP, ICAEW, BambooHR, FT postings, IIA Pulse, Big Four valuation panel, Forvis Mazars (CAS, risk-controls, transactions, valuation, forensic, fpa) | workforce §3 and §6 |
| Offshore pods and the 29% offshoring figure (CAS) | workforce §4; economics §3 and §5 |
| AI training-data roles paying TAS managers and forensic accountants (transactions, forensic) | workforce §7 |
| Deloitte Australia refund as a deliverable-quality case (risk-controls, transactions, fpa, forensic) | guardrails §7; objections §2; state-of-ai §5 |
| Independence mapping by module (independence file §2.1) | guardrails §3 table; ARCHETYPE recognition cues |
| Client-data duties: AICPA consent question, IESBA 114, FTC Safeguards, section 7216, vendor terms, shadow AI (all modules) | guardrails §5; objections §6 |
| Clients self-preparing with AI; RSM 40% reallocation (CAS, fpa, transactions) | disruption §5; economics §2 |
| AICPA-AIUC and Grant Thornton AIUC-1 (routed to assurance) | Named only as the attest boundary in frontier §3 and disruption §7 |
| KPMG forecast of AI-related material weaknesses in 2027 (risk-controls) | frontier §5 and §6 |
| Tax items (OPR fee and data duties, 7216, PEEC tax-services interpretation) | Pointers only in guardrails §4-5 and frontier §6; the tax archetype owns them |

Not placed (they belong in modules or other archetypes, or are leads): Masttro's valuation claim, the withdrawn arXiv
earnings paper, the Brattle insolvency primer, Wealth.com, transaction tax diligence, and the HK principals item.

## Suggested module changes

1. **Harmonise the Rule 707 status** between forensic-disputes §6/§8 (Standing Committee, September) and valuation §6
   (October agenda book) so both state the latest step.
2. **Split the RSM survey key**: one key for the newsroom release and one for the introduction page, as the fpa
   synthesis report also suggests.
3. **Crowe as an APS.** The risk-controls verification removed Crowe as an APS example for lack of a source, but the
   independence file reads Crowe's release as stating it practises in an APS under the AICPA Code. CAS and fpa still
   name Crowe. Re-read the release and align the three modules.
4. **Add a URL for CUATRECASAS-AIOMNIBUS-2026** in risk-controls §10, or cite the Official Journal entry.
5. **Grade alignment across archetypes:** CohnReznick's valuation release is B in `advisory-valuation-15` and C in
   `assurance-specialists-02` (flagged in the valuation verification; not edited here).
6. **Thin modules** (valuation, fpa-performance; also transactions, forensic, private-client below 50% A/B) need named
   firm outcome data, not regrading: targeted searches for firm case studies with client results, practitioner talks
   (ACG chapters, AICPA FVS sessions after 2026-11-06) and the 2026 CAS Benchmark.
7. **Private client:** no source addresses independence for family-office accounting sold to the firm's own attest
   clients; a short guardrail note pointing to guardrails §3 would close the loop.
8. **Thomson Reuters figures:** modules cite different TR pages; standardise on TR-FOPPR-2026 for client-side
   figures and TR-FOPREPORT-2026 for shadow AI.

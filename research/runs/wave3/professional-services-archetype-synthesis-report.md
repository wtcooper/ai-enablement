# Archetype synthesis report: professional-services

- **Date:** 2026-10-19
- **Outputs (11 files)** in `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/`:
  `ARCHETYPE.md` (100 lines), `interview-guide.md` (198), `value-chain.md` (127), `economics.md` (187),
  `state-of-ai.md` (164), `frontier.md` (134), `guardrails.md` (205), `workforce.md` (182), `disruption.md` (187),
  `objections.md` (100), `sources.md` (250). Every file over 100 lines has a contents list.
- **Other edits:** `archetypes/index.md` (professional-services moved to "Available archetypes" with cues, module ids and
  Extends "—"; "Not yet available" section removed; closing consulting line now links to professional services);
  `assurance/ARCHETYPE.md` and `tax/ARCHETYPE.md` (bold professional-services now a link, bold kept);
  `security/ARCHETYPE.md` ("which is not yet written; use the method and the library for those parts" replaced by a link).
  All four stay at 100 lines or fewer. No module or use-case file was edited.
- **Validator:** `python3 scripts/validate.py` reports **0 errors**, 23 warnings (unchanged; the five professional-services
  warnings are module A/B shares below 50%).
- **Source keys:** 194 distinct keys cited across the 11 files. A script confirmed every bracketed key resolves in the
  file's own Sources list or in `sources.md` Part B (124 shared keys there; 70 single-file keys at the end of their
  files). 157 keys come from the current use-case YAML (title, publisher, type, date and URL copied from it); 37 are new
  at archetype level, taken from the two cross-cutting files and the landscape (see §5).
- No downloads were needed; every fact comes from the input files or the current module and YAML files.

## 1. What each file draws on

| File | Main inputs |
|---|---|
| ARCHETYPE.md | Landscape §1, §10, §11 (journey markers, corrected); module headers; validator counts for the Evidence column; delivery-management-12 as the delegation reference case; tax, assurance and security ARCHETYPE.md for structure |
| interview-guide.md | Module §4 probes (not repeated; linked); cross-cutting guardrails §3.2 and state-of-AI §3.2 probes; scoping-pricing and firm-finance §5 figures; in-house items from client-development and pursuit-proposals routing notes |
| value-chain.md | Module §1-§2 of all 12 modules (summarised to processes and key steps, linked); brief's four-stage structure; landscape §10 overlaps; staffing, client-development and knowledge-management data-readiness figures |
| economics.md | firm-finance, scoping-pricing and billing-collections modules and YAML (§5 metrics, §6 guardrails); firm-finance and scoping-pricing synthesis and verification reports (McKinsey, Crowe, Tonkon Torp corrections); cross-cutting state-of-AI §2.4-2.6 (Accenture, HFS, Axiom, Juro, Grant Thornton-CBIZ, Fox Rothschild); staffing-resourcing §5 (SPI/Deltek utilisation) |
| state-of-ai.md | Cross-cutting state-of-AI §2.1-2.3; landscape §9; work-production, quality-review, client-development and knowledge-management §5; talent-learning frontier; consistency report (NBER provenance, ILTA date, TR-FOP key) |
| frontier.md | Landscape §12; cross-cutting guardrails §4 and state-of-AI §4; module §8 frontier lists (dates checked against YAML); forecasts labelled by author |
| guardrails.md | Cross-cutting guardrails file (§2.1-2.11, §3.1, §3.3) with keys mapped to YAML keys; scoping-pricing and firm-finance §6 for fee positions; talent-learning and staffing-resourcing §6 for employment AI |
| workforce.md | talent-learning and staffing-resourcing modules and YAML (§2, §5, §7, §9); talent-learning and staffing verification reports (KPMG -29%/-33%, Colorado dates, WBD scope, TR-FOP date); cross-cutting state-of-AI §2.6 and §3.1(3) |
| disruption.md | Cross-cutting state-of-AI §2.2-2.6 and §3.3; scoping-pricing-16, -19 to -23; firm-finance-15 to -17; consistency report on McKinsey; brief's required scenarios (pricing shift, AI-native firms, outside capital and MSOs, the pyramid), each example with firm type and each forecast with its author |
| objections.md | Cross-cutting objection tables (both files); module §9 objections (firm-finance, scoping-pricing, talent-learning, quality-review) |
| sources.md | Landscape §2-§9 and §14; cross-cutting source tables; YAML source rows; `last_researched: 2026-10-19` |

## 2. Conflicts and corrections applied (inputs disagree)

| Item | What the inputs say | What the files say |
|---|---|---|
| McKinsey outcome fees | "About a quarter" (Business Insider, self-reported); AI Weekly 25%; Resultsense "roughly a third"; a tech leader's 20% | "About a quarter of global fees", rounded and self-reported [BI-MCKINSEY-2025]; 20% noted; "a third" labelled a different measure (share of *work*) per the consistency and firm-finance verification reports |
| Crowe ownership plan | Landscape: "employee ownership plan", "ESOP"; cross-cutting: broad-based plan for 5,600 employees and 539 partners, first story version wrongly said ESOP; YAML: shared ownership plan open to all employees without upfront investment | YAML wording only ("CroweONE, a shared ownership plan open to all employees"); the 5,600 figure is not used |
| NBER 35720 provenance | Landscape and cross-cutting state file: independent; consistency report: vendor-published (Google ran and funded it; six of seven authors Google-tied per the talent-learning verifier) | "Run and funded by Google, whose model was tested" everywhere; no author count stated |
| TR Future of Professionals key | Cross-cutting files use TR-FOP-2026; tax uses that key for a different paper | TR-FOP-REPORT-2026 (2026-06-22) throughout |
| Other key aliases in the cross-cutting files | TEXASBAR-OP705-2025, EZEL-ABA512-2024, NYCBAR-OP2024-5, BSB-PR-2026, LAWSOC-ESSENTIALS-2026, IAMAG-LAWFIRM-2026, SOURCE-INSIGHTS-2026, CALBAR-ETHTECH-2026, AIWEEKLY-MCK-2025 | Mapped to the YAML keys TXETHICS-OP705-2025, ABA-OP512-2024, NYCBAR-OP2024-5-2024, BSB-AIGUIDANCE-2026, LAWSOC-GENAI-2026, IAMAG-LAWPL-2026, SOURCE-PRECISION-2026 (the last two pairs not cited) |
| Legora user counts | 140,000 at 2,000+ (Hogan Lovells Cadwalader release) vs 130,000+ at 2,100+ (newsroom) | Both shown, with the difference stated |
| *Heppner* date | 13 Feb (Orrick) vs 17 Feb (HAQQ) | "13 or 17 Feb; sources differ" |
| Kantata/RMI study | Landscape omitted the sample (44) and the 30% "exploring" band | Corrected figures used |
| SPI "the leak" | Landscape: hours saved but not resold or repriced; staffing verifier: time saved versus revenue generated | Verifier's definition |
| Fox Rothschild PE share | "One-third of the top 30" and "top 300" in the same document | Top 30 used, flagged unverified and internally inconsistent |
| Statements not used | Citi "three-quarters expect AI to affect the billable hour by 2028" (routing notes only, not in YAML); Forrester Wave "all 10 providers" (search snippet); BSB "absolute caution" (Law360 headline only); SPI 2025 "one in ten transformational" (not on the page); ENGAGE session attribution (corrected by the client-development report) | Omitted |
| MCA "AI for SME Consultancies" date | Landscape 26 Nov 2026; client-development module 2026-11-06 | Left out of the frontier calendar; see §6 |

## 3. Gaps

- **Measured outcomes:** no firm publishes an error, override, parallel-run, realisation or margin effect of AI; the
  economics and state-of-AI files say so rather than estimate.
- **Consulting primary sources:** McKinsey, BCG, Bain, Deloitte, EY and KPMG pages were not reachable in any input;
  consulting economics rest on press, Accenture's filing and analysts (Stanford, Forrester, HFS, Source).
- **Engineering and architecture:** one benchmark (Deltek) and two ethics texts (NSPE, ACEC). Interview cues for A&E
  are thin; no A&E pricing or workforce data beyond utilisation and turnover.
- **In-house beyond legal:** finance, HR and other shared-service teams working like firms are undocumented; the files
  say to use the library functions for them.
- **Mid-tier and small firms:** evidence skews to large law firms and vendor customers (ILTA's size bands are the only
  structured view).
- **Insurance:** no claims data; policy evidence is commentary and a partly paywalled trade report.
- **Client AI terms:** one secondary count of outside-counsel guidelines; no survey of RFP AI questions.
- **AI-native firms and PwC One:** no volume, price uptake, margin or quality data.
- **Non-US/UK regulators** (Canada's law societies, Australia's state regulators, Singapore, Hong Kong) not covered.
- **Primary texts** not reached by any input: ABA Opinion 512 (summaries only), SRA pages, AICPA and IESBA AI guidance,
  full NBER paper, SPI and Source reports.

## 4. Items routed from modules and placed at archetype level

| Item (source) | From | Placed in |
|---|---|---|
| In-house flags: ACC/Everlaw 59% no savings, 64% less reliance (ACCEVERLAW-2025); TRI legal-department operations data (TRI-LDOR-2026) | pursuit-proposals and client-development "in-house flag (not a module)" | interview-guide §7, economics §6 and §8, state-of-ai §2, disruption §7 |
| In-house intake products (LEGORA-INTAKE-2026, HARVEY-INTAKE-2026) and the "possible legal-operations extension" note | acceptance-risk §6 and delivery-management §6 | frontier §3; value-chain §6 and interview-guide §7 (in-house variants); extension not created (see §6) |
| PE and outside capital (AT-CROWE, BESTLAW-WSHB, WINSTON-PE, HK-AMLAW, VANMORGEN-SUPERRETURN, ICAEW-MIDTIER, COLUMBIA-BREYDO) | firm-finance, scoping-pricing routing | economics §7; disruption §5 |
| Pyramid and hiring data (BLOOMBERGLAW-HIRING, SFN-BIG4, LAW360-CITI, TRI-LFFI leverage, FORRESTER-BLOG) | talent-learning, firm-finance, staffing routing | workforce §2-§3; disruption §6 |
| Consumption AI pricing (EDISCOVERYTODAY-ILTACON, TRI-METER, LEGORA-CBP, ARTLAW-HARVEY14X) | billing-collections, firm-finance, knowledge-management routing | economics §5; frontier §4; value-chain §5 |
| Cross-cutting governance: shadow AI (TR-FOP-REPORT, LEXISNEXIS-FOW), ILTA policy by size | work-production routing to acceptance-risk; landscape §10 point 6 | ARCHETYPE stage markers; state-of-ai §1 and §5; guardrails §3 |
| Client AI terms and procurement (HAQQ-CONFID, CP-DELOITTECANADA, CANBERRATIMES-APSAI, ATL-STATS) | cross-cutting guardrails; scoping-pricing and acceptance-risk routing | guardrails §6; frontier §2 and §4 |
| Labs moving into services (DECRYPT-DEPLOYCO, LAWSITES-MSFT) | cross-cutting state-of-AI | disruption §8; frontier §3 |
| "No clear module": firm-level PMOs running the firm's own AI programme (TRI-PMO-ILTACON-2025, KK-2026, PMI-AISTD-2026) | delivery-management §6 | Not placed as facts (only the routing line was available); governance of the firm's own AI is a cross-cutting layer in value-chain §5 and guardrails |
| Assurance and tax routes (AICPA/AIUC certification, APS independence, Mercor test, ChatNational, FRC, ISQM 1; tax-firm pricing) | firm-finance, knowledge-management, quality-review, staffing, work-production | Left to those archetypes; only AICPA-CODE-2026, NYSSCPA-APS-2025 and TRI-CHARGING-2026 (78% of tax firms bill hourly) appear, as context |
| Out of archetype (court hallucination management, TRI-COURTS-2026; Basware support agent) | quality-review, knowledge-management | Not placed |
| Legal-practice extension (litigation, e-discovery validation) | work-production §5 | Not placed (see §6) |

## 5. New archetype-level keys (not in the YAML)

ABAJ-JOHNSON-2025, ABAJ-KLGATES-2025, ABAJ-SC-2026, ACCA-ETHICS-2026, ACCENTURE-Q4FY26, ACEC-AIGUIDE-2024, ATL-STATS-2026,
AXIOM-GC-2026, BGOV-GTCBIZ-2026, BIGHAND-FINANCE-2026 (module-only in firm-finance §10), BLOOMBERGLAW-AZ-2026,
BROWNING-ARMFOR-2026, CJC-AI-2026, CLIO-BILLABLE-2026, CLOC-CGI-2026, CP-DELOITTECANADA-2025, DECRYPT-DEPLOYCO-2026,
FOXROTHSCHILD-MSO-2026, GLP-GARFIELD-2025, GUARDIAN-DELOITTE-2025, HAQQ-CONFID-2026, HARVEY-NEWSROOM-2026,
HFS-SAS-2026, ILTA-ILTACON-2026, INSINSIDER-LAWYERS-2026, JURO-INHOUSE-2026, KANTATA-CONVERGE-2026,
LEGALCHEEK-BAKER-2026, LEGORA-NEWSROOM-2026, LEXPERT-ACC-2024, NSPE-BER24-2, OLSHAN-AIEXCL-2026, ORRICK-HEPPNER-2026,
REUTERS-CRETE-2025, SPI-AI-2025, TRI-EVENTS-2026 and TRI-LFFI-MIDSIZE-2026 (module-only keys). NSPE-BER24-2 and
ACCENTURE-Q4FY26 keep their input form, which lacks the usual year suffix.

## 6. Suggested module changes

1. **Thin and moderate modules:** staffing-resourcing (5 of 21 A/B) and billing-collections (5 of 17) are thin;
   acceptance-risk (6 of 14), pursuit-proposals (9 of 20) and delivery-management (7 of 15) are moderate. The next
   refresh should look for named deployments with measured figures rather than regrade.
2. **work-production §8** cites LAW360-BSB-2026 ("absolute caution"), a headline-only source; the cross-cutting file
   did not rely on it. Replace with BSB-AIGUIDANCE-2026.
3. **Engineering coverage:** add NSPE Case 24-2 (responsible charge over AI-assisted sealed work) and the ACEC
   guidelines to quality-review §6 and acceptance-risk §6; they are only in the archetype guardrails now.
4. **Privilege and insurance:** *Heppner* (ORRICK-HEPPNER-2026) and the ISO/E&O exclusion evidence
   (OLSHAN-AIEXCL-2026, INSINSIDER-LAWYERS-2026) are only at archetype level; acceptance-risk §6 and quality-review-18
   could reference them.
5. **ACCA ethics survey** (ACCA-ETHICS-2026) could support talent-learning or quality-review for accounting firms.
6. **Firm-level AI programme governance** (the firm's own AI policy, tool approval and PMO) has no single module home;
   consider a section in quality-review or knowledge-management, or note in each module that guardrails.md holds it.
7. **In-house legal operations:** two synthesis reports suggest a legal-operations extension; the evidence (intake,
   insourcing, invoice review) is spread over acceptance-risk-14, billing-collections-13 and work-production-18/-19.
   Revisit once non-legal shared-service evidence exists.
8. **MCA event date:** client-development §8 gives 2026-11-06 for "AI for SME Consultancies"; the landscape gives
   26 Nov 2026. Check the MCA page.
9. **Cross-archetype keys:** as the consistency report notes, renaming tax's TR-FOP-2026 and VALS-VLAIR-2025 would make
   the shared keys clearer.
10. **Module-only keys with URLs** (for example BIGHAND-FINANCE-2026, TRI-LFFI-MIDSIZE-2026, LEGORA-CROWELL-2026 with
    an unconfirmed date) could be added to the YAML so all modules resolve keys in one place.

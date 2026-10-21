# Synthesis report: advisory / client-accounting-services

Run date: 2026-10-20. Outputs:
- Module: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/modules/client-accounting-services.md` (299 lines, table of contents, 10 sections)
- Use cases: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/client-accounting-services.yaml` (24 entries; valid YAML; `scripts/validate.py` reports 0 errors for these files)

## 1. Counts in and out

| Input | Candidates |
|---|---|
| adv-client-accounting-services-practice.md | 17 |
| adv-client-accounting-services-discourse.md | 18 |
| adv-client-accounting-services-governance.md | 19 |
| adv-x-independence-pricing.md (CAS rows in §2.5) | 3 |
| adv-x-state-of-ai-disruption.md | 0 formal candidates (scenarios and facts used for context, CLA/Digits, roles) |
| landscape-advisory.md | 0 candidates (leads, journey markers, frontier) |
| **Total in** | **57** |
| **Out** | **24** (target 15-25 met) |

Dropped or not carried as entries: the BST & Co. fixed-fee CAS candidate (independence-pricing #01) and the Withum CAS-to-advisory candidate (#03) are firm pricing and growth, routed to professional-services (cross-referenced to professional-services-scoping-pricing-16 and -17); the spend-assessment idea (discourse 17, D) is kept only as a note in `-20`.

## 2. Duplicates merged

| Output | Merged inputs (P = practice, D = discourse, G = governance, IP = independence-pricing) |
|---|---|
| -01 categorization | P01, D01, G01 |
| -02 reconciliation matching | P02 |
| -03 agents prepare the close | P03, D03, G02, G03, Meridian part of D13 |
| -04 assistant with write access | P15 |
| -05 continuous close and packages | P08, D02, D15 (same firm, Elev8) |
| -06 variance commentary and dashboards | P07, D05, G04 |
| -07 forecasts, budgets, finance Q&A | P17, D06 |
| -08 memos and fractional CFO drafting | P09, D07 |
| -09 onboarding, migration, cleanup | P10, D08, D12, G05 |
| -10 AP and bill pay, fraud screening | P12, D10, G15 |
| -11 payroll | P11, D11 |
| -12 document and question chasing | P13, D09 |
| -13 portfolio monitoring | D14 |
| -14 in-house controller mail triage | P16 |
| -15 offshore delivery redesign | P14, G18 |
| -16 AI-native autonomous bookkeeping | P04, AI Accountant part of D13 |
| -17 provider platform plus local partner | D18 |
| -18 firm-trained model (CLA) | P05, D04 |
| -19 outcome-based vendor pricing | P06, IP02 |
| -20 advising clients on AI | D16 (+ D17 as note) |
| -21 control package before agents run a close | G06, G07, G08, G09, G14 |
| -22 firm AI policy, data terms, change control | G11, G12, G13, G17 |
| -23 disclosure, consent, client AI terms | G10, G19 |
| -24 independence and data-custody screening | G16, independence-pricing §2.1 |

## 3. Coverage by ladder and change scope

| Ladder \ scope | step | process | model |
|---|---|---|---|
| assist | -23, -24 | -21, -22 | -20 |
| augment | -04, -06, -07, -08, -11, -12, -13 | -15 | -18 |
| automate | -01, -02, -10, -14 | -05 | -09, -19 |
| delegate | none | -03 | -16, -17 |

Every ladder level and scope has entries. Gaps in the evidence: no delegate-step entry (none found; not invented). Delegate and model-scope evidence is vendor or AI-native-provider evidence (B for -03 via Pilot and Arclow; C for -16, -17, -18, -19). The only grade A is automate-step.

## 4. Grade mix

A 1 (-01), B 11, C 10, D 2 (-21, -24, both labelled "idea"). A/B share 12/24 = 50%.
- -01 is A only on the independent Choi and Xie study (named researchers; measured figures; association; platform unnamed; abstract-level). Vendor benchmarks in the same entry would be C.
- Regrades against inputs: -06 B (inputs ranged B to D; B rests on named small firms' described use); -07 B (old, non-generative named deployment; the generative parts are announced); -18 ladder set to augment where inputs disagreed (delegate vs augment) because the source does not describe how much the model does; -23 C, not B (the B input, Zuellig Pharma's policy, is adjacent); -03 B with a note that a stricter reading is C (no named customer firm for Meridian, Stack, Basis or Verity Prepare; CohnReznick pilot only being set up).
- Scheduled or pre-event conference abstracts (ENGAGE 2026 session listing) are cited only as signals and do not support any grade.

## 5. Routed to other modules (collected from the inputs)

**From CAS inputs to other modules**
- professional-services: pricing the firm's own CAS (90% fixed-fee claim, BILL 66% fixed / 60% hourly, Ignition fee survey ACCTODAY-FEES-2025, skim pricing WOODARD-EP161-2026, ACCTODAY-DECISIONS-2026, OPR section 10.27 fee point); Withum's $70M CAS and cross-sell; staffing, hiring criteria, junior pipeline (INTUIT-ACCTTECH-2026, BILL-AIAMBITION-2026, KARBON-AISTATE-2026, ACCTODAY-BIGYEAR-2026, BRYNJOLFSSON/STANFORD-CANARIES-2026); PE and APS (CURRENT, CPAPA-LARSON-2026, CBIZ-MICROSOFT-2026, ACCTODAY-CFOSEL-2026, WOODARD-EP185-2026, CROWE-KKR-2026, JOFA-PEEC-2026); MAVI's offshore talent marketplace; practice-management platforms adding bookkeeping modules (WOODARD-EP161-2026, ACCOUNTEX-2026); AI marketing pages and lead-gen GPTs (JOFA-REALLIFE-2025, ACCTODAY-USECASE-2024).
- advisory risk-controls: five controls for client-side close agents, COSO February 2026, SOC gaps (CPAPA-AGENTSCLOSE-2026, COSO-GENAI-2026); AICPA-AIUC assurance where sold to non-audit clients (JOFA-AIUC-2026); payments-fraud control design (AFP-PAYFRAUD-2026). Cross-referenced in -21 to advisory-risk-controls-21, -12, -22 (ids from the parallel risk-controls file as read on 2026-10-20; check if renumbered).
- advisory fpa-performance: Citrin Cooperman and Rosetree (ACCTODAY-ROSETREE-2026); AI-native ERP partnerships (RILLET-JOBS-2026); FP&A, scenario and board-reporting work (APRIO-JOB-2026); clients self-preparing with AI (ACCTODAY-CATALYST-2026).
- advisory forensic-disputes: payments-fraud, BEC and deepfake investigation (AFP-PAYFRAUD-2026).
- advisory private-client: family-office clients as a CAS niche (Sweeney Conrad, JOFA-CASTIPS-2025); GWCPA's custom GPT on ownership transitions (JOFA-REALLIFE-2025).
- assurance: Excel-agent data cleaning for audit populations (JOFA-EXCEL-2026); replayable close evidence auditors will ask for (CPAPA-AGENTSCLOSE-2026); FRC and ICAEW audit AI guidance (KINGSLEY-FRCICAEW-2025); AICPA practice aid and SOC guidance (JOFA-AIPA-2026/JOFA-PRACTICEAID-2026).
- tax: Withum's prediction of complete tax automation and the basic-return advertising remark (ACCTODAY-CASKEYS-2026, ACCTODAY-AITHOUGHT-2026); section 7216 consent mechanics and Circular 230 (IRS-OPR-2026, TAXADV-7216-2026).
- "governance-and-evidence" angle (named in the discourse file): ACCA ethics survey (ACCTODAY-ACCAETHICS-2026) and the Deloitte Australia refund; no such module exists, so treat as professional-services quality-review material.

**From other modules to CAS (picked up)**
- adv-private-client-combined: the Stanford JAR study on SME bookkeeping (used in -01).
- adv-risk-controls-discourse, -governance, -practice: AI in the monthly close for CAS clients and governance of agentic close tools (BlackLine, FloQast, Microsoft, Workday) (used in -03 and -21; the control-design service stays in risk-controls).
- No items routed to CAS under the older names (transaction-advisory, consulting-fpa, risk-advisory) beyond these were found in adv-forensic-disputes-combined or adv-transactions-combined.

## 6. Source reconciliation (same document, one ref)

Within this module's inputs, one ref was chosen per document: ACCTODAY-AIBEATS-2026 → ACCTODAY-AIBENCH-2026; ACCTODAY-CLADIGITS-2026 → ACCTODAY-CLA-2026; CPAPA-PILOT-2026 → CPAPA-PILOTAI-2026; ACCTODAY-WILLAI-2026 → ACCTODAY-REPLACE-2026 (not used in the YAML); STANFORD-GSBINSIGHT-2025 → STANFORD-INSIGHTS-2025 (dates conflicted, 2025-06-09 vs 2025-06-26, so `2025-06` is used); SEC-REG210-2026 → SEC-RULE2-01-2026; ECFR-16CFR314-2026 → FTC-SAFEGUARDS-2026; JOFA-CYBER-2026 → JOFA-CHECKLIST-2026; BBLAW-PRICING-2026 / BLOOMBERG-PRICING-2026 (not used).

Adopted refs already used elsewhere in the knowledge base for the same document: JOFA-ETHAI-2026 (inputs: JOFA-ETHICS-2026, JOFA-ETHICSAI-2026); JOFA-EXCELAGENT-2026 (JOFA-EXCEL-2026); JOFA-AIPOLICY-2026 (JOFA-POLICY-2026); IESBA-TECHREV-2023 (IESBA-TECH-2023); JOFA-PEEC-2026 (JOFA-PEEC2-2026, JOFA-PEEC-APS2-2026); JOFA-AIPA-2026 (JOFA-PRACTICEAID-2026); KARBON-SOAI-2026 (KARBON-AISTATE-2026); STANFORD-CANARIES-2026 (BRYNJOLFSSON-CANARIES-2026). Not adopted because the existing refs lack a year: COSO-GENAI (kept COSO-GENAI-2026, third-party-hosted copy the researcher read) and SEC-REGSX-2-01 (kept SEC-RULE2-01-2026). Other advisory modules written in parallel may still use the landscape refs (for example KARBON-AISTATE-2026); a one-pass ref normalization across the archetype is suggested.

## 7. Gaps

- **No production quality data**: no CAS firm or platform publishes error, override, rework or parallel-run rates, or inspection findings. The Choi and Xie full text (platform identity, effect sizes, experiment details) was not read.
- **No named customer firms** for the main agent platforms (Meridian, Basis, Ramp Stack, Accrual/Puzzle, BlackLine Verity Prepare); vendor counts conflict (Pilot 7,000+ vs 8,000+ businesses; 187,000 vs 199,000 months).
- **Mid-market and Big Four CAS**: almost no firm-specific AI detail for Armanino, Baker Tilly, Wipfli, Cherry Bekaert, Aprio (one job posting) or CohnReznick (one pilot in set-up). Most B entries are small or solo firms in Digits case studies.
- **Payroll, bill pay and fractional CFO**: vendor launches and single interviews only; no AI-governance evidence for payroll.
- **Independence for private-company attest clients**: the AICPA Code text (ET 1.295) and most IESBA sections were not opened; treatment rests on a 2016 JofA description and the IESBA technology revisions.
- **Pricing and margin effects** of AI on CAS: none disclosed (routed to professional-services anyway).
- **Data due after this run**: the 2026 CAS Benchmark Survey report (December 2026); the Digital CPA 2026 agenda (December 6-9).
- **Delegate-step**: no evidence of a single CAS step owned end to end by an agent with checkpoints, distinct from the whole close.

## 8. Suggested improvements to the briefs

1. Ask module researchers to reuse refs from the existing knowledge base, not only the landscape, and give them a ref index (a one-line grep of `ref:` keys with URLs), to avoid the roughly 17 ref conflicts reconciled here.
2. Ask the governance angle to fold control ideas into one or two packages per module rather than one candidate per control; five of its D entries described the same practitioner checklist.
3. Require researchers to say, for each B entry, whether the named organization is the deploying firm or only the vendor; several "B" candidates rested only on vendor-run use.
4. Ask for the date-conflict rule (which date to keep when two inputs disagree) and for undated pages to carry the access date in the locator, which some did and some did not.
5. Give the cross-cutting files a fixed candidate format with ladder, scope and grade so they merge cleanly; the independence-pricing candidates had descriptive evidence labels only.
6. State whether in-house teams (for example a not-for-profit controller) belong in an advisory module or in the library's finance function, so module scope is consistent across the archetype.

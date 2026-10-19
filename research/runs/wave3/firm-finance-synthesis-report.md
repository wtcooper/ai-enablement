# Synthesis report: professional-services / firm-finance

- **Date:** 2026-10-19
- **Inputs:** `landscape-professional-services.md`, `ps-firm-finance-practice.md`, `ps-firm-finance-discourse.md`,
  `ps-firm-finance-governance.md`, plus the "Routed to other modules" sections of every other `ps-*.md` file in
  `research/runs/wave3/` (items routed to firm-finance), and the finished scoping-pricing module and YAML (read for
  cross-references).
- **Outputs:** `plugins/.../professional-services/modules/firm-finance.md` (300 lines, contents list at top) and
  `plugins/.../professional-services/use-cases/firm-finance.yaml` (17 entries).
- **Validator:** `python3 scripts/validate.py` gives 0 errors for these files; 17 entries, 53% graded A/B. A script
  check confirmed every source key cited in the module is in the YAML or in the module's Sources list (10 keys marked
  *), every inline key in a YAML entry is in that entry's sources, and each key has one URL, date and type across
  entries. Cross-referenced ids in other modules and archetypes were checked to exist.
- No downloads were needed; all facts come from the input files.

## 1. Counts in and out

| | Practice | Discourse | Governance | Routed from other modules | Total |
|---|---|---|---|---|---|
| Candidates in | 22 (0 A, 11 B, 9 C, 2 D) | 22 (0 A, 12 B, 4 C, 6 D) | 18 (0 A, 4 B, 8 C, 6 D) | evidence items only (no entries) | 62 |
| Out | | | | | **17 (0 A, 9 B, 7 C, 1 D)** |

Routed evidence used: KPMG usage tracking to value its AI investment (BLOOMBERG-KPMG-2025, talent-learning); Litera
survey on ROI and showing value (LITERA-LAWSITES-2026) and TR AI in Professional Services (TR-AIPS-2026), both
client-development; law-firm COO roundtable (WESTERNALLIANCE-COO-2026, staffing-resourcing); Harvey Command Center
(LAWSITES-HARVEYDJ-2026, knowledge-management); Citi H1 2026 demand (BLOOMBERG-AICOST-2026, module metrics only).
Routed items not used: Intapp FY26 results (vendor business signal, not a firm-finance use), Accenture's $865 million
charges (FORTUNE-ACCENTURE-2025, people decisions belong to talent-learning), Fredrikson's business-model scenarios
(TRI-LDEV-2026), Vault leverage data (VAULT-PYRAMID-2026), PwC AI wage premium, TRI-RATES-2025 and
BESTLAWFIRMS-CITI-2026 (not needed beyond the TRI data held).

## 2. Duplicates merged and cross-referenced

P = practice, D = discourse, G = governance.

| Out | Merged from | Grade decision |
|---|---|---|
| 01 Firm fee mix toward fixed, hybrid, outcome-linked fees | P02, P04, P21 (in-house idea), D05, G10 | B (McKinsey, Keypoint) |
| 02 Model AI compression for rates, capacity, AFAs | P01, G06 (D), D11 (B on a job title) | **C**: D11's B rested on Greenberg Traurig's title, which shows no AI modelling work |
| 03 Passive work data for leakage, profitability, leverage | P10, P13, D07 (part) | B (named users, vendor pages) |
| 04 Line-by-line legal bill analytics (in-house and firm) | P11 | B kept |
| 05 Finance-operations agents (rates, GL forecast) | P12 | C kept |
| 06 AI aimed at written-down work | G04, D20 (D) | C |
| 07 Firm AI investment envelope and return review | D13, G03, G12, P09 (ROI part) + routed items | B (PwC, RSM, KPMG named) |
| 08 Pilot-to-licence gate on weekly active use | D01, P09 (adoption part) | B |
| 09 Track where freed hours go | P22, D12, G05 | C |
| 10 Firm-owned AI platform (Kirkland) | P14, P15 (part) | B |
| 11 AI spend governance | P07, D08, D10 | B |
| 12 Matter-level metering and cost recovery | P06, G08, P08 (D), D09 (D), G07 (D) | C; recovery and margin parts labelled ideas |
| 13 Partner expectations, credit and pay | P19, D17 (B), G15 | **C**: D17's B rested on Wipfli staff metrics, which scoping-pricing-13 holds; no partner pay change is named |
| 14 Idea: leverage and partner-income scenarios | D19, G14 | D |
| 15 Accounting PE capital (Crowe) | P16, D14, D18 (idea), G13 (accounting part) | B |
| 16 Law MSOs and ABS | P17 (C), D15 (B), G13 (Arizona part) | **C**: D15's B rested on an announced partnership; no deployment of capital into AI is shown |
| 17 AI-native firms | P18 (B), D16 (C), G17 (C) | B (General Legal) |

**Not carried as entries (already held in scoping-pricing; cross-referenced by id in the module):** D02 Norton Rose
hourly policy (scoping-pricing-06); P03 and D03 accounting value pricing (-16 and tax entries); D04 Kopka KPI billing
(-18); P05, D06 (PwC One part) and G11 PwC One (-22); D06 Debevoise STAAR and P15 tool licensing (-23); P20, D21 and
G02 matter-level AI value reporting (-09, -10); G18 in-house outside-counsel guidelines (-11); D22 Stanford pricing map
(-14). **Routed rather than carried:** G01 pre-bill fee-compliance check and G09 client AI-terms register (ideas) to
billing-collections; G16 insurance and assurance evidence to assurance (AIUC-1 is assurance-assurance-over-ai-19).

**No grade was raised by merging.** Three merges lowered a discourse B to C (02, 13, 16), explained in notes.

**Source-key canonicalisation**

| Canonical key | Input variants |
|---|---|
| TRI-METER-2026 | TRI-ILTACON-METER-2026 |
| BAKERDONELSON-TOKENS-2026 | BD-TOKEN-2026 |
| NETDOCUMENTS-TOKENS-2026 | NETDOCUMENTS-TOKENOMICS-2026 |
| RADIANT-TOKENS-2026 | RADIANT-TOKEN-2026 (typed firm, a fixed-fee legal services provider; practice typed vendor) |
| BI-MCKINSEY-2025 | BUSINESSINSIDER-MCKINSEY-2025 (matches scoping-pricing) |
| BLOOMBERGTAX-PRICING-2026 | BLOOMBERGLAW-ACCTG-2026 (matches scoping-pricing; bloombergtax URL) |
| TXETHICS-OP705-2025, DCBAR-OP388-2024 | TXBAR-OP705-2025, DCBAR-388-2024 (match scoping-pricing) |
| TRI-ILTACON-2025 | TRI-ILTACON-HOUR-2025 (matches scoping-pricing) |
| TR-AIPS-2026 | TRI-AIPS-2026 (practice read the landing page; client-development read the PDF dated 2026-01) |
| BLOOMBERG-AICOST-2026 | BLOOMBERGLAW-MYSTERY-2026 (same URL) |
| AT-PWC-2026 | ATODAY-PWC-2026 (talent-learning) |

Date and access choices: CALBAR-GENAI-2026 `2026-05` (inputs gave 2026-05 and 2026-05-14); TR-FOP-2026 `2026-09` to
match scoping-pricing, although governance read "Published Oct 16 2026" on the page (unresolved); SPI-AI-2026 `2026-10`
(governance read a 2026-07-14 timestamp); ILTA-TECHSURVEY-2026 `2026-06`, typed professional-body. LAW360-LEGORA-2026
and LAWYERSWEEKLY-KEYPOINT-2026 are `full` because practice read the opening or visible portion; discourse and
governance saw only headlines. TRI surveys and LFFI data are labelled `vendor-published` throughout (practice and
discourse had used `independent`).

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 02, 06, 08 | 07, 09, 11, 12, 13 | 01, 14, 15, 16 | 12 |
| augment | 05 | 03, 04 | 10 | 4 |
| automate | none | none | none | 0 |
| delegate | none | none | 17 | 1 |
| Total | 4 | 7 | 6 | 17 |

- **Automate: no evidence.** No source shows a finance step (rates, forecasting, profitability, cost allocation) with
  no person on the normal path. Practice graded time capture as automate, but timekeepers review every entry, so 03 is
  augment. PwC One (automate, model) is held in scoping-pricing-22.
- **Delegate: only as a whole-firm model** (AI-native firms). No agent owns a finance outcome.
- **Ladder is nominal** for fee-mix, capital and partner-economics entries: AI is the cause of the change, not a tool in
  the step.

## 4. Grade mix

0 A, 9 B (53%), 7 C, 1 D. **No A is possible on this evidence:** no named firm reports a tracked metric for AI's effect
on rates, realisation, margin, profit per partner or AI return. Figures are a rounded media-briefing statement
(McKinsey), self-reported spend (PwC, Kirkland), a self-reported client count (General Legal), a vendor customer story
(Tonkon Torp) or surveys by organisations that sell AI or research (TRI, SPI, Clio, BigHand, Litera). Six B entries
rest on vendor pages, press reports of executive statements or conference remarks.

## 5. Gaps

- **No quality or outcome evidence:** no error, override or parallel-run data for AI in rate setting, forecasting,
  profitability or billing analytics; no before-and-after realisation or margin data.
- **No automate entries; delegate only at firm level** (see §3).
- **In-house is thin:** UBS via Legal Decoder (04), one general counsel's proposal (01), TRI's legal operations report.
  No in-house shared-service finance team outside legal was found.
- **Sector skew:** mostly US law; accounting through PwC, Crowe, RSM, KPMG; consulting through McKinsey and the
  Stanford paper; no architecture or engineering firm beyond Deltek's survey. No consulting-firm primary documents.
- **Not reached:** ABA Formal Opinion 512 (quoted second-hand here; scoping-pricing read a copy), SPI full report,
  BigHand full report, FT originals for PwC, Kirkland and SuperReturn, Kirkland job postings, AICPA exposure-draft
  adoption status, SRA and BSB texts.
- **Conflicts kept visible:** McKinsey share (quarter, 20%, "a third"); BigHand landing page versus a BigHand
  manager's post on billable-hour reductions (not used); TR-FOP-2026 date; TR-AIPS-2026 date; Tonkon Torp 20 versus 21
  minutes.
- **Scheduled, not evidence:** TRI's 25th Law Firm COO & CFO Forum (21-22 Oct 2026).

## 6. Routed to other modules (collected from the inputs)

| Item | Target | Sources |
|---|---|---|
| Laurel and Legora draft time entries; Laurel Billing compliance and scope agents; Aderant Time, Appeals and Collections agents; pre-bill fee-compliance check (idea); client AI-terms register applied at bill time (idea); write-down mechanics; Clio realisation and flat-fee commentary; Intapp Time and Billstream | billing-collections | LEGORA-LAUREL-2026, LAWSITES-LAUREL-2026, LAUREL-BILLING-2026, ADERANT-AGENTS-2026, CALBAR-GENAI-2026, TXETHICS-OP705-2025, DCBAR-OP388-2024, NCBAR-FEO1-2024, VSB-LEO1901-2025, TRI-EFFICIENCY-2025, CLIO-SOLO-2026, INTAPP-TERMS-2026 |
| Aderant Virtual Pricing Director; Legal Decoder AFA builder (detail); Kopka KPI billing; Kerbis and Furlong podcasts; Norton Rose fixed-fee view; Zarwin Baum single line-item bill; fixed-fee workflow pilots | scoping-pricing | ADERANT-VPD-2026, ADERANT-VPDWEB-2025, LAWSITES-DECODER-2026, TRI-KOPKA-2026, LEGALLATENIGHT-49-2026, LAWYERIST-607-2026, BLOOMBERGLAW-TEXAS-2026, TRI-LEGALWEEK-2026, EVERLAW-BLOG-2026 |
| Hybrid human-agent teams and outcome data in staffing; Laurel staffing forecasts; blended workforce; A&E utilisation | staffing-resourcing | KANTATA-RMI-2026, LAUREL-SIGNAL-2026, CONSULTANCYUK-BONE-2026, DELTEK-CLARITY-2026 |
| First-year hiring, graduate cuts, PwC headcount, associate training, legal engineers, NBER trial, mid-career departures, pyramid debate, KPMG performance reviews | talent-learning | RESULTSENSE-2026, TRI-LEGALWEEK-CRISIS-2026, BLOOMBERGLAW-GCXAI-2026, NBER-AUTOR-2026, TR-FOP-2026, FORRESTER-BLOG-2025, BLOOMBERG-KPMG-2025 |
| Intapp Celeste conflicts, intake and lateral-hiring playbooks (BakerHostetler, Hg); California confidentiality and agentic-access rules | acceptance-risk | LAWSITES-CELESTE-2026, CALBAR-GENAI-2026 |
| Partners not discussing AI with clients; visibility gap between firms and departments; lead the AI-ROI conversation; 78/6/32% client findings | client-development | TRI-STANDOUT-2026, TRI-GREATDISCONNECT-2026, TRI-LEGALWEEK-2026, TR-FOP-2026 |
| Firm-built tools as work product; partner-as-gatekeeper burden of a client portal | knowledge-management, work-production | BLOOMBERGLAW-KIRKLAND-2026, BLOOMBERGLAW-DEBEVOISE-2026 |
| "More output, same reviewer"; human oversight as a cost of speed; supervision duties; hallucination rates; Deloitte Australia refund | quality-review | BLOOMBERGLAW-GCXAI-2026, CONSULTANCYUK-BONE-2026, CALBAR-GENAI-2026, STANFORD-MAGESH-2024, CTV-DELOITTE-2025 |
| AICPA-AIUC SOC 2 plus AIUC-1 certification; APS independence proposals; Mercor junior-CPA month-end close test | assurance archetype | AT-AIUC-2026, NYSSCPA-APS-2025, TXCPA-APS-2026, AT-MERCOR-2026 |

## 7. Suggested improvements to the briefs

1. **Publish a canonical source-key list per archetype before the deep dives.** Eleven documents arrived under two keys
   in this module alone (§2), several with conflicting types, dates or access levels.
2. **Fix module boundaries before the angles run.** Firm-finance and scoping-pricing deep dives produced the same
   entries (PwC One, McKinsey, Kopka, Norton Rose, accounting value pricing, matter-level AI value evidence). A short
   rule ("firm-level mix and economics here; a single engagement's price there") would have saved a third of the
   candidates. One input also called billing-collections "merged into firm-finance"; the module list should say which
   modules exist.
3. **Give a provenance rule for TRI and other vendor-owned research arms.** Angles labelled the same TRI survey
   `independent` and `vendor-published`.
4. **Ask for an `ai_role` marker** (tool in the step versus cause of the change). Over half of this module is fee,
   capital or partner-economics change caused by AI, where the ladder value is nominal.
5. **Protect one search per angle for primary documents** (FT originals, firm results, consulting-firm pages); all
   three angles ran out before reaching them.
6. **Ask governance angles for non-US and non-legal rules** (SRA, ICAEW, IESBA, insurers), and for in-house shared
   services outside legal, which no angle found.

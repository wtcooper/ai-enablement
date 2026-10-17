# Synthesis report: tax / transfer-pricing

Prepared 2026-10-17. Outputs:

- Module: `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/transfer-pricing.md` (250 lines)
- Use cases: `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/use-cases/transfer-pricing.yaml` (22 entries)
- `python3 scripts/validate.py`: 0 errors. One warning for this file: 3 of 22 graded A/B (14%), below the 50% target. Grades were not inflated to meet it.

## 1. Counts in and out

| Input | Candidates | Grades in |
|---|---|---|
| Practice angle | 18 | A 1, B 2, C 14, D 1 |
| Discourse angle | 13 | B 1, C 11, D 1 |
| Governance angle | 17 | B 2, C 11, D 4 |
| Landscape scan | 0 (leads only) | n/a |
| Items routed to transfer-pricing from other tax angle files | 6 pointers (section 5) | n/a |
| **Total in** | **48 candidates** | |
| **Out** | **22 use cases** | A 1, B 2, C 16, D 3 |

45 of the 48 candidates are merged into the 22 (the discourse angle's agreement entry was split across `-10` and
`-11`). The other 3 (governance G12 IRS selection models, G13 Hungary, G14 authority document review) describe
tax-authority AI that the controversy synthesis already covers (`tax-controversy-13`, `tax-controversy-15`, which
merged the routed TP items); they are cross-referenced, not repeated. G14's idea of authority language-model review
of TP files has no controversy entry of its own; flag for the controversy owner. 68 distinct source refs are used in
the YAML; 10 more appear only in the module's Sources section.

## 2. Duplicates merged

P = practice, D = discourse, G = governance; numbers are each angle's own ids.

| Out | Merged from | Note |
|---|---|---|
| 01 Grounded TP research assistant | P01, D08, G08 | |
| 02 General-purpose assistants | P02 | |
| 03 Self-service for non-specialists | P13, G09 | Internal escalation chatbot plus business-side use of general assistants |
| 04 Data aggregation from ERPs | P15, D07 | |
| 05 Functional and industry analysis, DEMPE | D02, G03 | |
| 06 Comparables search and benchmarking | P07, D01, G01 | D01 was graded B; kept at C (see section 4) |
| 07 First-draft documentation narratives | P03, D03, G02 | |
| 08 Documentation review, country rules and consistency | P10, D04, G04 | |
| 09 Bulk local-file production from central data | P04 | Only grade A |
| 10 Intercompany agreement drafting and clause extraction | P08, D05 (first half), G05 | |
| 11 Multi-agent cross-tax review | P09, D05 (second half), G16 | |
| 12 Automated operational TP (Kemira) | P05 | |
| 13 In-year margin monitoring | P06, D06, G06 | G06 was 'automate'; kept 'augment' |
| 14 Connected TP knowledge model | P11, D12 | D12 was 'delegate'; kept 'augment' |
| 15 Taxpayer audit-risk self-screening | P14, D10, G07 | |
| 16 Audit defence responses | P12, D09, G10 | |
| 17 AI in expert economic reports (idea) | G11 + routed Riddle Aggregates item | |
| 18 APA and MAP support (idea) | D11, G15 | |
| 19 Policy modelling and planning | P18, D13 | P18 was D; kept C (firm says "some companies are experimenting") |
| 20 AI-use and verification log (idea) | G17 | |
| 21 Insourcing documentation | P17 | |
| 22 Platform-plus-experts delivery | P16 | |
| not repeated (see `tax-controversy-13`, `-15`) | G12, G13, G14 | Tax-authority AI; controversy already merged these |

**Source-key reconciliation.** The angles used different keys for the same document. Canonical keys chosen:
AIBIDIA-LEADERS-2026 (= AIBIDIA-STATETP-2026), AIBIDIA-OTP-2026 (= AIBIDIA-OTPBLOG-2026), BDO-AIGOV-2026 (= BDO-2026,
BDO-CA-2026; the discourse angle had it search-only, the others read it via a text mirror), DDTC-WUTA-2026
(= DDTC-PWCSG-2026), ANDERSEN-AI-2026 (= ANDERSEN-2026), INTERTAX-SIVA-2026 (= INTERTAX-2026), WTS-HU-2026
(= WTS-NAV-2026), BTAX-AFRICA-2026 (= BLOOMBERG-AFRICA-2026), KPMG-DE-2025 (= KPMG-TPDE-2025), ABA-TAXTIMES-2026
(= ABA-TT-2026), PWCDE-CH7-2026 (= PWC-DE-OECD-2026). Source types and dates also disagreed (IRS-LBI-TP-2026 typed
press, firm and regulator; KPMG-TP-2025 dated 2025, 2025-04 and 2025-04-02); one value was chosen and applied
everywhere. **Key collision:** the governance angle's PCRT-AI-2026 points to an ATT news item, while
tax-research-advisory-governance uses PCRT-AI-2026 for the ICAEW guidance page. Renamed here to ATT-PCRTAI-2026; the
archetype-level merge should confirm.

## 3. Coverage by ladder and change scope

| Ladder \ scope | step | process | model |
|---|---|---|---|
| assist | 01, 02, 17, 18, 19, 20 | none | none |
| augment | 03, 04, 05, 06, 07, 08, 10, 15, 16 | 13, 14 | 21 |
| automate | **none** | 09, 12 | none |
| delegate | none | 11 | 22 |

- **Automate at step level: no evidence.** No source describes AI running a single TP step with no person on the
  normal path.
- **Automate (process)** entries are rules-based automation (09, 12). Neither is shown to use generative AI.
- **Delegate** has one conference-reported, unnamed multi-agent example (11) and one vendor service model (22).
- **Model scope** has two entries (21 insourcing, 22 packaged services), neither shown to depend on AI.
- Maturity: in-production 3, piloting 8, announced 6, emerging 5.

## 4. Grade mix and grade decisions

A 1 (5%), B 2 (9%), C 16 (73%), D 3 (14%). A/B = 14%. The module says plainly that the evidence is thin.

- `-09` is A on named-customer figures (Trivium, Fortum) published by the vendor; the AI role is not shown. The
  discourse angle excluded the same Trivium page for lack of a date and an AI link. Flag for the verifier.
- `-06` comparables: discourse graded B on PwC Singapore conference remarks. Lowered to C because the remarks are
  opinions ("may", "under certain conditions") with no engagement named; practice and governance also had C.
- `-19` planning: practice graded D (idea), discourse C. Kept C because a firm states some companies experiment.
- The governance angle's two B entries (Hungary, IRS models) are not repeated here, which lowers this file's A/B
  share; they sit in `tax-controversy-13` (B) and `tax-controversy-15` (A) instead.

## 5. Routed items

**Received (routed to transfer-pricing from other tax files):**

| Item | From | Handling |
|---|---|---|
| Riddle Aggregates IRS valuation expert report, hallucinated citations, recorded withdrawn (RIDDLE-TRANSCRIPT-2026, CHARLOTIN-DB-2026) | research-advisory governance | Used in `-17` and module §6; noted that the source does not say it is a TP case |
| IRS LB&I remarks on AI and expert witnesses (IRS-LBI-TP-2026) | controversy governance, practice, discourse; research-advisory governance | Already in inputs; used throughout |
| Exactera ExactMatch and ExactReport; KPMG TP GenAI claims | controversy practice | Already in inputs (`-06`, `-08`) |
| ABA May 2026 AI and section 482 panel | research-advisory discourse | Already in inputs |
| CJEU Arcomet, VAT consequences of TP year-end adjustments (BTAX-VAT2026) | indirect-tax discourse | Module §6 (cross-tax guardrail) and §10 |
| PwC specialists name TP among IRS exam focus areas (NYSSCPA-PWCWEBCAST-2026) | controversy discourse | Not used: no AI content beyond what IRS-LBI-TP-2026 covers |
| "Transfer pricing Tax Skills in Orbitax" (TR-CORPAI-2026) | compliance-corporate practice | Not used: the routing note gives only the name, no description; a follow-up read of the TR blog is needed |
| TP master and local file maintenance, German head of tax (BTAX-EYTFO-2026) | tax-data-technology discourse | Not used: no detail on AI in TP in the note |

**Routed out by the transfer-pricing inputs (for other modules' syntheses):**

- **controversy:** tax-authority AI in TP risk selection and audit (Hungary, South Africa, Nigeria, IRS; WTS-HU-2026,
  KPMG-HU-2026, BTAX-AFRICA-2026, IRS-LBI-TP-2026); expert-witness AI disclosure (IRS-LBI-TP-2026); CIAT agent-based
  audit blog and working paper (CIAT-BLOG-2026, CIAT-WP06-2025); HMRC ICTS proposal (KPMG-UK-ICTS-2025); IRS algorithms
  flagging distributor losses and AI-powered enforcement (TR-CHECKPOINT-2025, TR-CHECKPOINT-2026); Clinco, Buckeye
  Trust recall, proposed FRE 707 (TAXCT-CLINCO-2026, ITATONLINE-BUCKEYE-2025, PROSKAUER-707-2026); IRS selection-model
  oversight (TIGTA-2025, GAO-2026). Already merged by the controversy synthesis (`tax-controversy-13`, `-15`); this
  file cross-references them.
- **research-advisory:** TP of AI itself: pricing AI tools, agents and AI-generated content between affiliates, DEMPE
  in AI value chains (OECD-INTRAGROUP-2026, BGOV-AGENTS-2026, BTAX-ZERBE-2026, IBA-TAXAI-2025, KPMG-TPPOD1-2026,
  KPMG-TPPOD-2026, TPMINDS-WC-2026, OXFORD-CBT-2026); cross-cutting conduct guidance (IRS-OPR-2026, PCRT, AICPA-WERFEL-2026);
  BTAX-ZERBE-2025 op-ed on judgment.
- **compliance:** TaxCalcBench (COLUMN-TAXCALCBENCH-2025).
- **international-pillar-two:** Pillar Two interplay with operational TP (AIBIDIA-PRIORITIES-2026, AIBIDIA-TPMINDS-2026);
  TPMinds Pillar 2 Summit session (TPMINDS-INTL-2026); Pillar One Amount B and the UN dispute-prevention protocol
  (IRS-LBI-TP-2026).
- **tax-data-technology:** public CbCR and ESG overlap (AIBIDIA-TPMINDS-2026); KPMG Digital Gateway with Anthropic;
  data governance as the critical constraint (ITR-NEXDIGM-2026, KPMG-GR-2026); agentic tax-transparency framework for
  royalty withholding and master-file cross-validation (BTAX-LEE-2025); TPMinds tax-technology panel (TPMINDS-INTL-2026).
- **indirect-tax:** customs and tariff interaction with TP (AIBIDIA-SERIESB-2025); VAT and customs parts of `-11`.

**Cross-module ids** (in YAML notes): `-01` / tax-research-advisory-01; `-02` / tax-indirect-tax-20; `-03` /
tax-research-advisory-17; `-08`, `-15`, `-16` / tax-controversy-05 (EY TP Doc Insights, a TP tool kept in
controversy); `-15` / tax-compliance-corporate-13; `-16` / tax-controversy-07; `-17` / tax-controversy-08; `-19` /
tax-research-advisory-10; `-20` / tax-research-advisory-19, tax-compliance-corporate-19, tax-indirect-tax-15; `-22` /
tax-compliance-corporate-15, tax-indirect-tax-19. Tax-data-technology, international-pillar-two and provision files
did not exist yet, so `-04` and `-12` name those modules only. The controversy file cites tax-transfer-pricing-08,
-14 and -16, apparently from an input numbering: -08 and -16 match this file; check whether its '-14' means
`-14` (connected knowledge model) or `-15` (self-screening).

## 6. Gaps

- **No measured outcome for any generative-AI TP use.** No error rate, override rate, parallel run, tax-authority
  acceptance or independent test for AI drafting, comparables or review.
- **Vendor concentration.** Most facts come from Aibidia (blog, survey write-ups, case studies, product pages). Its
  survey sample is stated as 97 and 138 on different pages; case studies are undated.
- **Process areas with no AI evidence:** CbC report preparation, intragroup services (only the OECD consultation on
  TP *of* AI), APAs and MAPs (ideas only), cost-sharing.
- **No named in-house generative-AI deployment.** Speakers from Shell, Deutsche Bank, Anthropic, OpenAI, Uber, Inter
  IKEA, WPP and ADM appear on agendas, but no content was published; TPMinds West Coast (4-5 Nov 2026) has not yet happened.
- **Big Four thin:** only KPMG (US, Germany, Greece, Hungary, UK) and PwC conference speakers; EY, Deloitte (beyond
  Poland) and PwC global TP tools were not found because search budgets ran out.
- **Primary documents unread:** OECD Chapter VII draft and comments (site blocked), IRS transcript of the LB&I
  remarks, ABA Tax Times recap, Intertax and IBFD full texts, Aibidia's full 2026 report.
- **Unverified affiliation:** the ABA panel lists "Joe Tobin, IRS"; governance notes a search result suggesting a
  person of that name now at Deloitte.

## 7. Suggested improvements to the briefs

1. **Give the angles a shared source-key register before they start** (or a key rule such as PUBLISHER-SLUG-YYYY with
   the slug taken from the URL). Eleven documents had two or three keys here, and one key collided across modules.
2. **Fix source-type rules for intermediated items:** say how to type a firm's report of a regulator's remarks (EY on
   IRS LB&I), a firm author's Bloomberg Tax commentary, and a vendor blog that summarises the vendor's survey.
3. **Ask angles to state why they exclude a source** in a machine-readable way, so synthesis can resolve conflicts
   such as the Trivium page (graded A by practice, excluded by discourse).
4. **Require "AI shown: yes/no" on each candidate.** Several of the best-evidenced TP entries are rules-based
   automation; a flag would stop the grade being read as evidence for AI.
5. **Clarify scope for authority-side AI and for "TP of AI".** Practice and discourse routed authority AI to
   controversy; governance kept three entries in TP. One rule up front would save merge work.
6. **Routing notes should carry the substance, not just a pointer.** Two items routed here (Orbitax TP Tax Skills;
   German head of tax on master and local files) gave a name and a ref but no description, so they could not be used.
7. **Budget searches per angle, not shared,** or reserve some for primary documents; all three angles ran out before
   reaching OECD, IRS and Big Four sources.

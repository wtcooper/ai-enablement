# Synthesis report: assurance / substantive-testing

- **Prepared:** 2026-10-16
- **Inputs (all in `research/runs/wave1/`):** `landscape-assurance.md` (leads only; no YAML of its own),
  `assurance-substantive-testing-practice.md`, `assurance-substantive-testing-discourse.md`,
  `assurance-substantive-testing-governance.md`
- **Outputs:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/substantive-testing.md` (299 lines, table of contents, journal-entry and fraud testing in its own section, §3)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/substantive-testing.yaml` (25 entries, 79 distinct source refs)
- **Validator:** `INFO ... use-cases/substantive-testing.yaml: 25 use cases, 14 graded A/B (56%)`; 0 errors. Other
  warnings come from sibling modules and the missing SKILL.md, not from these files.
- **Extra check (scripted, not in the validator):** every bracketed key in the module resolves to a YAML source or to
  the module's §11; every key cited in a YAML entry's text is in that entry's `sources`; each ref has one URL, date and
  type across the file.
- **Status:** not yet source-verified. A verification pass like the pilot's is recommended before use.

## 1. Counts in and out

| | Practice | Discourse | Governance | Total |
|---|---|---|---|---|
| Candidate use cases in | 21 | 18 | 16 | 55 |
| Carried into output | 21 | 17 | 16 | 54 |
| Not carried | 0 | 1 | 0 | 1 |

- **Out:** 25 use cases. 16 merge two to five candidates; 9 come from a single candidate.
- **Not carried:** discourse-18 (internal-audit agent "swarms" at PayPal, continuous full-population testing). It
  describes the same change as `assurance-controls-testing-18` (PayPal swarm auditing) and is internal audit, not
  external substantive testing. Its Deloitte NL and KPMG SOX 2030 sources were kept in `#16`.
- **Landscape:** used for leads and cross-checks (EY scale, KPMG Clara agent list, IFIAR 88%/55%, CPA.com 39%/11%). Where
  it differed from a deep dive, the deep dive won (Grant Thornton article date 11 May 2026, not 7 May; Evidence Match
  covers fixed assets as well).

## 2. Duplicates merged

| Output | Merged from | Choice notes |
|---|---|---|
| 01 Full-population journal-entry scoring | P-01, D-01, G-01 | scope process (2 of 3) |
| 02 Idea: LLM journal-entry anomaly detection | P-02, G-02 | governance's Table 1-2 counts used; abstract-only claims dropped |
| 04 Corroborate and authenticate documents | D-11 (C), D-12 (D), G-14 (D) | assist/step from the two idea entries; graded C |
| 06 GenAI procedure-design assistant | P-21, G-16 | |
| 08 Technology-assisted item selection | G-08, D-04 (selection part) | FRC contract example moved to 14; pattern `intake-triage` to match `CT#04` |
| 10 Evidence-to-sample matching (vouching) | P-04, P-05, P-08, D-03, G-03 | graded A on Oberlander and Sanville (vendor-published) |
| 14 Contract and lease review | P-12, P-13 (D), G-05, D-05, D-04 (FRC part) | runtime from the only real product (CoCounsel) |
| 15 Judgment-heavier tests | D-06 (B), D-16 (D) | B is generous; noted |
| 16 Substantive analytics | P-19, D-08, G-07 | scope step (2 of 3) |
| 17 Confirmations and direct bank data | P-10 (A), P-11 (B), D-10, G-06 | pattern tie (2 `other`, 2 `reconcile-exceptions`); strongest entry's `other` kept |
| 18 Drone and imaging inventory counts | P-20 (B), D-13 (D), G-12 (D) | ladder from the only working-tool entry |
| 19 Idea: AI challenge of estimates | D-14, G-13 | |
| 20 Routine-test agents to orchestration | D-02 (B), P-03, G-11, P-09 (C) | KPMG Clara agents plus Fieldguide orchestrator |
| 22 Firm-wide agent platforms | P-17, G-09 | benchmark is the only measure |
| 23 Idea: second AI reviews AI work | G-10, D-15 | |
| 24 PwC Australia AI-native, full population | P-16 (delegate), G-04 (automate) | ladder delegate (PwC's agents plan and test); pattern full-population-testing |

Single-candidate entries: 03 (G-15), 05 (D-17), 07 (D-09), 09 (P-14), 11 (P-06), 12 (P-07), 13 (P-18), 21 (D-07),
25 (P-15). Every source from every merged candidate was kept unless noted in the entry's `notes`.

**Cross-module overlaps with the verified controls-testing pilot (decisions):**
- **`CT#07` evidence-to-sample matching → canonical home is substantive testing (`#10`).** All of `CT#07`'s measured
  figures (Oberlander 16 h to 5-6 h, Sanville, RMF) are tests of details, and this module adds PwC Evidence Match,
  Graczyk et al. and benchmark failure evidence. `#10` and the module say so and point to `CT#07` for the controls
  variant. Because only the three outputs could be written, `CT#07` is unchanged; **recommend** the next
  controls-testing revision trims `CT#07` to controls-specific claims and cross-references `#10` instead of repeating
  the Oberlander and Sanville figures.
- **`CT#08` full-population testing → split by population.** `CT#08` keeps control and master-data populations
  (Armanino, Microsoft). This module's `#24` covers balances and transactions tested against third-party data (PwC
  Australia, IAASB ED-500 example) and `#25` the service-model case (Ledgerline). The shared expectation-gap guardrail
  is stated in both YAML entries (each needs its own sources) but the module refers to `CT#08` rather than repeating
  its evidence.
- **Other references, not duplicates:** `CT#03` (evidence-request agents; see `#21`), `CT#04` (risk-scored selection;
  see `#08`), `CT#10` (deployed AI secondary review; see idea `#23`), `CT#15` (AI-performed controls; see idea `#05`),
  `CT#23` (fabrication screening idea; see `#04`).

## 3. Coverage by ladder and change scope

| Ladder | Count | Ids |
|---|---|---|
| assist | 5 | 04, 05, 06, 12, 19 |
| augment | 12 | 01, 02, 03, 07, 08, 09, 11, 14, 15, 16, 18, 23 |
| automate | 4 | 10, 13, 17, 25 |
| delegate | 4 | 20, 21, 22, 24 |

| Change scope | Count | Ids |
|---|---|---|
| step | 18 | 02-08, 10-19, 23 |
| process | 6 | 01, 09, 20, 21, 22, 24 |
| model | 1 | 25 |

- All four ladder levels have evidence. **Delegate entries have no measured outcome**: they are a pilot reported by the
  WSJ (KPMG, EY), announcements (Deloitte, EY, Grant Thornton, Fieldguide) and a synthetic benchmark.
- **Model scope is thin:** one entry (Ledgerline, a specialist benefit-plan firm). Other business-model signals (KPMG
  fee pressure, AI-native ventures such as Modus and Repodo) are not substantive use cases and are routed (§6).
- **No automate/process entry.** The closest is `#24`, which the evidence places at delegate.
- Maturity: 8 in production, 7 piloting, 3 announced, 7 emerging.
- Lens assignment in the module: augment at process scope (`#01`, `#09`) is shown under improve, because the
  vocabulary's lens mapping does not cover that combination.

## 4. Grade mix

| Grade | In (55) | Out (25) |
|---|---|---|
| A | 6 | 3 (10, 11, 17) |
| B | 18 | 11 (01, 08, 09, 12, 13, 15, 18, 20, 21, 24, 25) |
| C | 18 | 7 (03, 04, 06, 07, 14, 16, 22) |
| D (idea) | 13 | 4 (02, 05, 19, 23) |

A/B share is 56%. Notes for the verifier:
- **Every A is a single named-firm figure published by a vendor** (Oberlander and Sanville in `#10`, FGMK in `#11`, Moore
  Polska in `#17`), with no method and no accuracy measure.
- **Generous Bs:** `#15` (one sentence about a PwC "attempt", via a republished WSJ copy); `#18` (2018 EY proof of
  concept and a 2021 livestock study); `#20` (B from the WSJ-reported KPMG pilot; three of its four candidates were C);
  `#13` (pilot named, no figures).
- Prevalence figures (IFIAR 88%, CPA.com 39% and 11%, PCAOB 6 of 6 firms) sit in `outcomes` because the inputs put them
  there; each is labelled as prevalence, not effect.
- C and D entries kept for what they add: exception triage (03), evidence integrity under AI forgery (04), client
  AI-generated information as a test object (05), population preparation (07), contract review (14), analytics (16),
  firm platforms and the only agent benchmark (22), and ideas on LLM anomaly detection, estimates and AI review.

## 5. Gaps

- **No independent quality evidence.** No error, false-positive, override or parallel-run result for any substantive
  tool in a live audit; no 2025-26 inspection finding specific to AI. Firms say parallel runs happen but publish nothing.
- **Journal-entry testing:** widely used, yet no firm publishes how many flagged entries proved to be misstatements.
- **Thin areas:** estimates (two experiments, one pre-GenAI); inventory (2018 and 2021 evidence plus standard-setter
  interest); contract review (no named audit deployment with a measured result); full-population debate under ISA 530
  and AS 2315 (no practitioner piece found).
- **Unreached:** the SSRN randomised field experiment on LLMs and audit quality (all three angles blocked); WSJ
  original (read via a republished copy); AICPA practice aid full text (login); ISA 240 (Revised) final text; ACFE/SAS
  full report; the PAC hearing behind DataSnipper's NAO figures; Bloomberg Tax's KPMG agent item; SEC approval of the
  PCAOB confirmation standard (not confirmed).
- **Dating:** several vendor pages carry only a year (DATASNIPPER-CONNECT/FGMK/ODP/PAYABLES-2026, FIELDGUIDE-SANVILLE-2026,
  MINDBRIDGE-CHERRY-2022, GRACZYK-2025, CHRIST-DRONE-2021); Circit dates look like republication dates.
- **Search-only source:** WOLTERSKLUWER-EVIDENCE-2026 (supports one guardrail in a C entry only).
- **Conflicts carried:** PwC Evidence Match 20 versus 30 document types; EY "all phases now" versus "end-to-end by 2028";
  CPA.com "one in four" versus "one-third" using no AI; FinancialAuditBench outcomes are labelled vendor-published
  because Modus Audit employees co-authored it.

## 6. Routed to other modules (collected from the three deep dives)

| Target module | Items |
|---|---|
| completion-reporting | Disclosure-checklist agents: TR Disclosure Review (~30% of eligible customers, ~300 analyses a month), Caseware Verity (beta firms saved 2.7 h per run, vendor figure), KPMG Financial Report Analyzer, DataSnipper Disclosure Agents (TR-DISCLOSURE-2026, CASEWARE-VERITY-2026, KPMG-CLARA-2025, DATASNIPPER-AGENTS-2025); PwC audit-committee communications tool (CFODIVE-PWC-2026); Deloitte agents drafting documentation (DELOITTE-OMNIA-2026); FABIAN-2026; FinAuditing and LLM-audit benchmarks (ARXIV-FINAUDITING-2025, ARXIV-LLMAUDIT-2025) |
| planning-risk-assessment | MindBridge Agentic Risk Assessment and Analysis Designer Agent (MINDBRIDGE-ARA-2026); PwC Simplified Audit and Advanced Walkthrough Assistant (PWC-AT-2025); Caseware Verity planning review; AICPA practice aid on AI-enabled fraud risk and entity AI use (AT-AICPAPA-2026); SAS No. 151 fraud lens and revenue fraud-risk presumption (JOFA-SAS151-2026); TR board-minutes summarisation template (TR-WORKFLOW-2026); ICAEW chatbot test on ISA 315 (ICAEW-PIERPOINT-2025); ED-520 risk-assessment analytics |
| controls-testing / soc-attestation | Fieldguide Field Agents for Testing (FIELDGUIDE-HELP-2026); Baker Tilly's Fieldguide expansion across SOC, PCI, HITRUST, ISO, FedRAMP, SOX (FIELDGUIDE-BAKERTILLY-2026); ODP Corporation internal-audit story (DATASNIPPER-ODP); KPMG Clara controls agents promised; KPMG SOX 2030 on self-healing controls and auditing AI (KPMG-SOX-2026); AICPA practice aid on AI-operated controls and service-organisation reports; AS 2301.17 tests of controls when client AI cannot be verified (CAQ-GENAI-2024); IFIAR on invoices originating from AI systems (IFIAR-TTF-2026, p.10) |
| specialists | BVR on Big Four valuation practices (BVR-BIGFOUR-2026, paywalled); Commerford et al. and Peecher et al. on reliance on AI for estimates (also used in `#19`); AICPA comparison of heavy client AI reliance with complex valuation models; the unreachable SSRN inventory-valuation experiment |
| quality-management | FGMK QC and reviewer agents (DATASNIPPER-FGMK-2026); certification, recertification, monitoring and training (FRC-GENAI-2026, FRC-ATT-2025, IFIAR-TTF-2025/2026, AFM-BB-2025, CPAB-AI-2024, AUASB-AI-2025); PIA Group running hundreds to 1,000+ quality checks per file (NYENRODE-QUALITY-2026); RSM guidance copilot and staffing tool (CAQ-RSM-2026); AICPA quality-management guidance for AI tools; FABIAN-2026 on skills |
| acceptance-independence | Grant Thornton Gtap under an alternative practice structure (GT-GTAP-2026); PwC and RSM investment commitments (BLOOMBERGTAX-RSM-2025, search-only); KPMG fee argument (VERDANTIX-KPMGFEE-2026, THEFINANCESTORY-KPMGFEE-2026); PCAOB and SEC remarks on private equity and AI (NYSSCPA-BOTIC-2025, DART-SECPCAOB-2025) |
| Cross-cutting (workforce, business model) | Junior pipeline and "lifting the pyramid" (CTRLCOUNCIL-WSJ-2026, NYSSCPA-BOTIC-2025); Big Four AI hiring (COMPUTERWORLD-FT-2026, RESULTSENSE-2026); TR Institute 81% regular AI use (TRI-FOP-2026); fee pressure; AI-native ventures (Modus, whose staff co-authored ARXIV-FAB-2026); Gartner internal-audit surveys (GARTNER-2026, GARTNER-AUG-2026) |

## 7. Canonical source keys

Wave 1 inputs mostly share `PUBLISHER-SHORT-YYYY` keys, so few remaps were needed:

| Canonical key | Input refs and decision |
|---|---|
| PWCAU-AT-2025 | practice PWCAU-AT-2025; governance PWCAU-2025 |
| LEDGERLINE-CPAPA-2026 | practice LEDGERLINE-CPAPA-2026; governance CPAPA-FULLPOP-2026 |
| DELOITTE-OMNIA-2026 | Deloitte press release (practice, discourse). Governance used the same key for the CPA Practice Advisor copy; replaced by the release, which practice read for the same claims |
| PCAOB-TAA-2024 | governance's Federal Register copy of Release 2024-007 (2024-07-02). Practice used the key for the pcaobus.org implementation page (2024-06-12, notes only) |
| FRC-AIAUDIT-2025 | governance's PDF (AI_in_Audit.pdf). Practice used the key for the FRC news release; not used |
| DATASNIPPER-ODP-2026 | practice DATASNIPPER-ODP (year added for the key format; page undated) |
| CPACOM-ATR-2025 | type set to `survey` (practice said `professional-body`) |
| Dates and URLs | FRC-GENAI-2026 2026-03-30 (practice 2026-03); IAASB EDs 2026-08-05 (discourse 2026-08); TR-AGENTIC-2025 2025-11-05 with the `.html` URL |

**Pilot keys differ for the same documents.** The controls-testing pilot uses short keys without years: TR-AGENTIC =
TR-AGENTIC-2025; FG-SANVILLE = FIELDGUIDE-SANVILLE-2026; AT-PWC = PWC-AT-2025; CFODIVE-PWC = CFODIVE-PWC-2026;
CFOBREW-PWC = CFOBREW-PWC-2025; AT-PWCAU = PWCAU-AT-2025; CPAPA-ADEWOLE = LEDGERLINE-CPAPA-2026; CPAPA-EY = EY-CANVAS-2026;
CONS-GT = GT-GTAP-2026; K-CLARA = KPMG-CLARA-2025; K-SOX30 = KPMG-SOX-2026 (PDF versus article page); FRC-GENAI =
FRC-GENAI-2026; FRC-THEMATIC = FRC-ATT-2025; IFIAR-TTF25 / IFIAR-TTF26 = IFIAR-TTF-2025 / -2026; IFIAR-2025F =
IFIAR-SURVEY-2026; PCAOB-2024-007 = PCAOB-TAA-2024 (different copy); IAASB-ED = IAASB-ED500-2026 and siblings; AFM-12 =
AFM-BB-2025; IRBA = IRBA-AI-2024; IIAF-FRAUD = IIA-AIFRAUD-2026; CPACOM-ATR = CPACOM-ATR-2025; DELOITTE-OMNIA =
DELOITTE-OMNIA-2026. This module follows the vocabulary rule (`PUBLISHER-SHORT-YYYY`); the pilot should be re-keyed.

## 8. Suggested improvements to the briefs

1. **A shared source-key registry across modules** (for example `references/schemas/sources.yaml`), so the same
   document has one key in every file. The pilot and wave 1 already diverge (§7).
2. **A cross-module overlap rule.** Say which module owns a use case when its evidence is measured in another (here:
   matching measured on substantive work but first written up under controls), and allow the synthesis to edit, or
   at least flag, the other module's entry. An optional `related: [id]` field in the YAML, checked by the validator,
   would let entries point to each other instead of repeating evidence.
3. **Separate prevalence from effect.** Angles put adoption rates (IFIAR 88%, CPA.com 39%) in `outcomes`. Add an
   outcome `kind: prevalence | effect` or ask for adoption figures in `notes`.
4. **Lens rule for augment at process scope.** The vocabulary's lens mapping does not cover it (`#01`, `#09`).
5. **Grade rule for merged entries.** State that a merged entry takes the grade its strongest claim supports and must
   list component grades in `notes`; several merges here combine one B with several Cs or Ds.
6. **Validator check for module citations.** Bracketed keys in a module should resolve to its YAML or Sources section;
   it was checked here by script.
7. **Module length.** A required extra section (journal-entry and fraud testing) plus module-only sources with URLs
   left little room under 300 lines. Allow module-only sources to live in the YAML header or a sidecar file.
8. **Angle-prefixed candidate ids** (P-01, D-01, G-01) in deep dives, since all three restart at
   `assurance-substantive-testing-01` and collide.
9. **Proposed patterns** from recurring `other`: evidence-authenticity check (`#04`), confirmation and direct
   data-access platform (`#17`), assurance over AI-produced entity information (`#05`).
10. **Ask deep dives for flag-to-misstatement rates** in journal-entry testing explicitly; all three reported their
    absence only in Gaps.

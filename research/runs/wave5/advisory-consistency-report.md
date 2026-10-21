# Advisory consistency report

Date: 2026-10-21. Scope: the 7 module files and 7 use-case files in
`plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/`. Nothing outside them was
edited. Downloads (COSO PDFs, Thomson Reuters pages, JofA pages, eCFR metadata) went to a private `mktemp -d` folder.

## 1. Source keys unified

### Same document, several advisory keys (now one key, with one title, date, type and URL)

| Kept key | Replaced keys | Note |
|---|---|---|
| IESBA-TECHREV-2023 | IESBA-TECH-2023 | Matches the assurance archetype |
| JOFA-ETHAI-2026 | JOFA-ETHICSAI-2026, JOFA-ETHICS-2026 | Matches assurance |
| JOFA-AIPA-2026 | AICPA-AUDITAID-2026, JOFA-PRACTICEAID-2026 | Matches assurance. CPAPA-AUDITAID-2026 is a different article (CPA Practice Advisor) and is kept |
| JOFA-CHECKLIST-2026 | JOFA-CYBERCHECK-2026 | /issues/ and /news/ URLs serve the same article (canonical /issues/ kept) |
| JOFA-PEEC-2026 | JOFA-PEEC-APS2-2026 | Same 2026-08-10 article (checked) |
| KARBON-SOAI-2026 | KARBON-AISTATE-2026 | Date set to 2026-01-23 in fpa §10 |
| DART-COSO-2026 | DELOITTE-DART-COSO-2026 | |
| IVSC-AI-2025 | IVSC-PERSPECTIVES-2025 | Now the same key as assurance-specialists |
| ICAEW-JUNIOR-2026, PCAOB-SPECIALISTS-2025 | ICAEW-HOWTO-2026, PCAOB-SPECIALIST-2025 | Module-only keys aligned to the existing knowledge-base keys |

Records harmonised under one key: COSO-GENAI-2026 (three URLs, including a third-party copy, to the coso.org PDF; the
two PDFs were compared page by page and match, so page locators stand; date 2026-02-23); SEC-RULE2-01-2026 (eCFR API,
eCFR and Cornell LII copies to the eCFR current URL, date 2026-10-20 as the access date of the current text);
AICPA-FVS-2026 (one title and date `2026-11`, session dates moved to locators); STANFORD-JAR-2026,
STANFORD-INSIGHTS-2025 (2025-06-26), DEANDORTON-AIEXPERT-2025 (2025-09-05), IRS-OPR-2026, JOFA-CASAI-2026,
KARBON-ENGAGE-2026, KPMG-AIFINANCE-2026 (titles). A script confirms no key now has two titles, dates, types or URLs in
the advisory YAML files, and no URL carries two keys.

### One key, different documents (split; noted in YAML headers)

| Old key | New keys |
|---|---|
| TR-FOP-2026 | TR-FOPPR-2026 (press release, CAS) and TR-FOPREPORT-2026 (report page, risk-controls module; URL added) |
| AICPA-FVS-2026 | AICPA-FVS-2026 (agenda, forensic) and AICPA-FVSHOME-2026 (home and workshop pages, valuation) |

Other similar-key pairs that name different documents are stated in the headers: COSO-GENAI/COSO-GENAIPR,
FRC-GENAI/FRC-GENAINEWS, JOFA-AIPA/CPAPA-AUDITAID, KPMG-SOX2030/KPMG-FUTURESOX, GT-AISURVEY/GT-PEAI,
CPAPA-RSMMM/RSM-MMAI, USCOURTS-EVAGENDA/EVID/STDCOMM/FRE707, COHNREZNICK-VALUATION/CPAPA-COHNREZNICK,
HAMILTONLANE-VALTECH/S73-HAMLANE, DIGITS-BENCH/ACCTODAY-AIBENCH. fpa-performance.yaml had no header; one was added.

### Conflicts with other archetypes (advisory key renamed)

| Advisory key | Clash | Fix |
|---|---|---|
| GT-AIIMPACT-2026 (cross-industry survey) | Names the PE report in three method files | Renamed GT-AISURVEY-2026; the PE report stays GT-PEAI-2026 |
| FRC-GENAI-2026 (news release) | Assurance uses it for the guidance PDF | News release is now FRC-GENAINEWS-2026 (assurance's key); the guidance, formerly FRC-GENAIGUIDE-2026, is FRC-GENAI-2026 |
| HELPNET-GARTNER-2026 | Security uses it for a different article | HELPNET-GARTNERIA-2026 |
| ISACA-AIPULSE-2026 (European release) | Security uses it for another release | ISACA-AIPULSEEU-2026 |
| TR-FOP-2026 | Tax uses it for a third TR paper | Split as above |
| FINRA-OVERSIGHT-2026 (GenAI section page) | Security uses it for the landing page and FINRA-ROR-2026 for this page | FINRA-ROR-2026 |

Same document under different keys elsewhere, left as is (no clash): professional-services (CPAPA-TECHSURVEY-2026,
JOFA-CAS-2026, JOA-*, NBER-BRYNJOLFSSON-2023, SEC-2024-36, WOODARD-2025), assurance (SEC-REGSX-2-01, COSO-GENAI,
AT-GARTNER, DS-ARMANINO, FTG-PETUAL, K-SOX30, KPMG-SOX-2026, K-AGENTIC, OPTRO-*, PWC-DCT, IIAF-*, IIA-AIFRAMEWORK-2024,
CPAPA-LEDGERLINE-2026), security (FINRA-OVERSIGHT-2026). Those archetypes disagree among
themselves, so there is no single target key.

## 2. Duplicates across modules

| Pair | Decision |
|---|---|
| client-accounting-services-01 / risk-controls-22 (confidence-threshold routing; same Choi and Xie study, same 8.5% figure) | **Duplicate.** Kept CAS-01 (it changes bookkeeping work); deleted risk-controls-22. Its only distinct fact (COSO p. 19 invoice-extraction example, re-validation after vendor updates) moved to CAS-01 notes and locator. The risk-controls module and header point to CAS-01 |
| CAS-21 / risk-controls-21 / fpa-14 | Distinct (firm's own close; advisory service to client; forecast back-testing); cross-referenced every way |
| CAS-06 / fpa-01 / private-client-03 / -10 | Distinct layers; cross-referenced both ways |
| CAS-07 / fpa-02 / private-client-16 | Distinct; both ways |
| CAS-20 / fpa-09 / private-client-14 / risk-controls-17 / -18 | Distinct client segments; both ways |
| CAS-10 / private-client-07 / risk-controls-23 / forensic-12 | Prevention, controls, readiness, investigation; both ways |
| forensic-03 / risk-controls-23 / -09 | Distinct; forensic-03 and risk-controls-23 now link both ways |
| forensic-08 / risk-controls-02 (Diligent) | Same product, different work; both ways |
| forensic-09 / valuation-09 / transactions-12 | Different deliverables; both ways |
| forensic-14 / valuation-11; forensic-07 / valuation-05 | Distinct; both ways |
| CAS-02, -03 / private-client-01, -04 | Family-office context distinct; both ways |
| CAS-18 / fpa-12; CAS-19 / fpa-13; forensic-01 / transactions-03 / CAS-02; valuation-13 / -15 / private-client-02; forensic-15 / risk-controls-24 / fpa-14 | Distinct; no change beyond one added link (valuation-13 to private-client-02) |
| valuation-15 / assurance-specialists-02 | Same release, graded B here and C there; assurance not edited |

## 3. Cross-references

All `advisory-`, `assurance-`, `tax-`, `security-` and `professional-services-` ids mentioned exist (script check,
including shorthand chains); target titles match the context. Fixed: CAS-21's ambiguous "-12 ... -22" (now full
risk-controls ids, routing to CAS-01); every reference to the deleted risk-controls-22. Ids are otherwise unchanged.

## 4. Provenance and grades

- KPMG 42% (KPMG-AIFINANCE-2026): `self-reported` in the fpa module and fpa-02, `vendor-published` in
  risk-controls-17. KPMG publishes a survey of finance leaders about their own organisations, like the Grant Thornton
  survey already marked self-reported in the same entry; risk-controls-17 set to `self-reported`.
- No other figure carries two labels across files (script check of YAML outcomes and module text).
- **Grade changes: none.** Entry check by script: 124 of 125 entries present with unchanged id, grade, ladder and
  maturity; the only one missing is risk-controls-22 (removed as a duplicate).

## 5. Build-process words removed

YAML headers rewritten in all 7 files (no wave, synthesis, deep dive, landscape, `research/runs/` paths or grade
history). Notes: about 60 "merged from practice/discourse/governance NN", "candidate", "routed from ... research",
"research file had ...", "downgraded/raised/was B", "renamed", "one ref is kept", "earlier draft", "added in
verification" passages, each restated as the fact it held. Modules: the risk-controls §10 pointer to the research files
(starred keys now carry their own URLs; Cuatrecasas has none on record), "fact-checked", "in the research", "routed to
tax", COSO "third-party copy".

## 6. Firm type

Added where the entry's sources state it: CAS-12, -13, -21, -22, -23, -24; forensic-11, -12, -13, -15;
private-client-07, -11, -12, -13; risk-controls-10, -20, -23.

## 7. Validator

`python3 scripts/validate.py`: 0 errors. Advisory warnings only for A/B share or count below target (forensic,
fpa, private-client, transactions, valuation); risk-controls is at 23 entries, 52% A/B. Modules are 241 to 300 lines,
each with a table of contents.

## Process note

One read-only `git status` was run by mistake while checking files; its output was discarded and nothing was changed
through git.

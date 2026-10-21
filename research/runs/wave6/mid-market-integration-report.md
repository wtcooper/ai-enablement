# Mid-market integration report: assurance and tax archetypes

Done 2026-10-21. Scope: the new modules (assurance `private-company`, `benefit-plans`, `nonprofit-government`; tax
`multistate-private`), the widened modules (tax `compliance-individual-business`, `research-advisory`; assurance
`quality-management`, `soc-attestation`, `assurance-over-ai`), both `ARCHETYPE.md`, `value-chain.md` and
`interview-guide.md` files, and the assurance and tax rows of `archetypes/index.md`. `advisory/` and
`professional-services/` were not touched. `python3 scripts/validate.py`: **0 errors**, 31 warnings (all are
content-target warnings: entry counts or A/B share). No grade, ladder, scope, maturity, pattern, function or runtime class
changed (checked id by id against a copy taken before editing).

## 1. Keys unified

Rule used: one key per document, with the same title, date, type and URL in every YAML source entry and module source
list in the archetype. Every document cited in a new or widened file was checked against the whole archetype, including
older modules that cite the same document. Where a key exists in the archetype's `sources.md`, that key was kept. Where
YAML values disagreed, the `sources.md` value was used if it matched one of them; otherwise the majority value or the
most precise date. Parenthetical access notes removed from titles (for example "(abstract read)", "(page undated; year
inferred)") were moved into the entry's `locator`, so no provenance was lost.

**Assurance: 36 old keys renamed (103 source entries, plus inline citations in the same entries and module text).**

| Canonical key | Replaced |
|---|---|
| AICPA-PA-2026 | AICPA-PA |
| AICPA-AIPAID-2026 | AICPA-GUIDE-2026 |
| AFM-12BB-2025 | AFM-12, AFM-BB-2025 |
| ANDERA-RSM-2026 (sources.md key) | CPAPA-RSM, CPAPRACTICE-RSMANDERA-2026 |
| AT-PCAOBPE-2025 | ACCTODAY-BOTIC-2025 |
| BAKERTILLY-IA-2026 | BAKERTILLY-GAM-2026 |
| BNN-DELOITTEAU-2025 | BNN-AP-DELOITTE-2025 |
| CALCPA-AISTD-2026 | CALCPA |
| CASEWARE-CITRIN-2026 | CITRIN-DAS-2026 |
| CASEWARE-VERITY-2026 (CwX blog, as in sources.md) | CASEWARE-CWX-2026 |
| CASEWARE-AIDA-2026 (AiDA blog) | CASEWARE-VERITY-2026 where it named the AiDA blog (substantive-testing) |
| CFODIVE-PWC-2026 | CFODIVE-PWC |
| CONS-GT (consulting.us article) | GT-GTAP-2026 where it named that article (acceptance-independence, substantive-testing) |
| GT-GTAP-2026 (Grant Thornton release, as in sources.md) | GT-GTAPPR-2026 |
| CPACOM-ATR-2025 | CPACOM-ATR |
| CPAPA-ASKLUCA-2026 | CPAPA-LUCA-2026 |
| CPAPA-EY (CPA Practice Advisor article) | EY-CANVAS-2026 where it named that article; EY-CANVAS-2026 now means only EY's own release, as in sources.md |
| DELOITTE-OMNIA-2026 | DELOITTE-OMNIA |
| EY-SOC-2026 (sources.md key) | EY-SOC |
| FIELDGUIDE-PCAOB-2026 | FG-PCAOB |
| FOLEY-PCAOB-2026 | FOLEY-BOTIC |
| FRC-GENAI-2026 | FRC-GENAI |
| FRC-NEWS-2026 (sources.md key) | FRC-GENAINEWS-2026 |
| HAMBURG-FABIAN-2026 (university news item) | FABIAN-2026 in quality-management; FABIAN-2026 now means only the journal paper |
| HOLMSTROM-2024 | HOLMSTROM-PETERS-2024 |
| ICAEW-FRCVIEW-2026 | ICAEW-FRC |
| ICAS-AMBS-2025 | ICAS-AMBS-2026 |
| IFIAR-SURVEY-2026 | IFIAR-2025F |
| IFIAR-TTF-2026 | IFIAR-TTF26 |
| JOFA-AIUC-2026 | AICPA-AIUC-2026 |
| JOFA-ETHAI-2026 | JOFA-ETHICSAI-2026 |
| JOFA-PEER-2026 (sources.md key) | JOFA-PRB |
| KPMG-SOX-2026 | K-SOX30 |
| LEDGERLINE-CPAPA-2026 | CPAPA-ADEWOLE, CPAPA-LEDGERLINE-2026 |
| NYENRODE-2026 | NYENRODE-QUALITY-2026 |
| PETERS-2022 | PETERS |
| PWC-AT-2025 | AT-PWC |

TR-SCALING-2026 / TR-CASESTUDIES-2026 was already resolved to TR-SCALING-2026 in every file. IRS-OPR-2026 in assurance
now uses the tax archetype's title. Header comments that listed the old short keys (acceptance-independence,
soc-attestation, assurance-over-ai) were rewritten.

**Assurance: other alignments.** 260 title, 30 date, 24 type and 54 URL fixes in source entries. Notable ones:
DELOITTE-UKTR-2025 (one title, the accessible PDF and 2025-11; quality-management locators now say their page numbers
refer to the standard PDF of 30 Sep 2025, checked by download); KPMG-SOX-2026, COSO-GENAI and AICPA-REVALERT-2026 (one
URL each, with the other URL kept in the locator); IAASB-CATALOG-2026 (title and 2026-07-09 from the PDF itself);
AIUC1-SITE-2026 ("AIUC-1 Standard", the page title); KPMG-HOHL-2026 (2026-05-27, from the page's datePublished);
DELOITTE-ACPR-2026, CASEWARE-CITRIN-2026, OATH-2026, GAO-YBFAQ-2025, TR-SAMBROWN-2026, CPAB-AI-2024, PETERS-2022,
AFM-12BB-2025 (most precise date). Module source lists fixed for CASEWARE-PIONEER-2026, JOFA-AIPA-2026, JOFA-AIUC-2026,
OATH-2026 and KPMG-HOHL-2026.

**Tax.** VALS-TAXAGENT-2026 is dated 2026-10-20 in every entry, including `tax-research-advisory-04` and
`tax-multistate-private-07`/`-14`. Entries whose figures came from the earlier read say so in the locator ("figures read
on the 2026-10-16 version of the page"); `-04` says its P-004 figures were confirmed on the live page. The research-advisory
module line now reads "read 2026-10-16; headline unchanged on the 2026-10-20 page". TR-COCOUNSELCORP-2026 is dated
2026-10-17 everywhere (an undated product page; the re-read date is in the locator). TAXPROF-WERFEL-2026 became
DUKE-WERFEL-2026 (the controversy YAML key for the same URL).

## 2. Cross-references and build-process wording

- Every full use-case id cited in the assurance and tax modules, YAML and archetype files resolves, including
  abbreviated ranges after a full id. One stale provisional id (`tax-research-advisory-new-01` in
  `tax-multistate-private-14`) was removed; `tax-research-advisory-26` stays.
- Build-process wording removed from the new and widened files: references to the research files, research angles
  (practice, discourse, governance), the landscape scan, routing, "wave 6", synthesis and verification passes,
  "widening", "this pass", "the research team" and key-renaming notes. Firm-type claims that rested only on the landscape
  were checked: "Caseware platform most small and mid-sized US firms use" and "EisnerAmper is private-equity-backed" are
  not on the cited pages and were removed; Citrin Cooperman is now described with its own words.

## 3. Archetype files

- **assurance/ARCHETYPE.md** (100 lines): coverage now names private-company audits, reviews and compilations, and benefit
  plan, nonprofit and single audits; a mid-market recognition cue; three new module rows; Evidence updated for the widened
  modules; prose tightened, nothing dropped except the old "counts as of the last review" phrase (now dated).
- **tax/ARCHETYPE.md** (100 lines): coverage adds owner-managed returns and multistate tax; an owner-managed and multistate
  cue; Form 990 and 990-T boundary to assurance; new row; Evidence updated.
- **assurance/value-chain.md** (252 lines): peer-review row in stage 6; §5 tables for private-company and SSARS work,
  benefit plan audits and nonprofit and government audits, with sourced facts [EBSA-AUDITQ-2023; GAO-YBFAQ-2025] (both added
  to §8).
- **assurance/interview-guide.md** (220 lines): two personas, three module-chooser rows, six mid-market questions (§6, now
  "Internal audit and mid-market variants"), four vocabulary rows, §9 sources.
- **tax/value-chain.md** (190 lines): multistate in stages 3 and 7, owner steps in stage 3, an owner-managed and
  multistate variant in §6; TAXNOTES-UNWATCHED-2026 and TR-SOTP-2026 added to §7.
- **tax/interview-guide.md** (206 lines): one persona, three module-chooser rows, six mid-market questions (§6, now
  "In-house and mid-market variants"), two vocabulary rows, §9 sources.
- **archetypes/index.md**: assurance and tax rows only (module ids and a mid-market cue).

## 4. Final counts (validator)

| Archetype | Module | Use cases | A/B | Evidence |
|---|---|---|---|---|
| assurance | private-company (new) | 20 | 9 (45%) | moderate |
| assurance | benefit-plans (new) | 15 | 7 (47%) | moderate |
| assurance | nonprofit-government (new) | 16 | 10 (62%) | strong |
| assurance | quality-management (widened) | 28 | 10 (36%) | moderate |
| assurance | soc-attestation (widened) | 18 | 11 (61%) | strong |
| assurance | assurance-over-ai (widened) | 27 | 7 (26%) | thin |
| tax | multistate-private (new) | 14 | 1 (7%) | thin |
| tax | compliance-individual-business (widened) | 31 | 10 (32%) | moderate |
| tax | research-advisory (widened) | 28 | 11 (39%) | moderate |

Unchanged: acceptance-independence 4/21, planning-risk-assessment 11/25, controls-testing 16/25, substantive-testing
13/25, specialists 3/14, completion-reporting 3/18, sustainability-assurance 0/13; compliance-corporate 3/24,
provision-pillar-two 0/16, indirect-tax 4/22, transfer-pricing 3/22, controversy 10/25, data-technology 8/24.

## 5. Files changed

Assurance (`plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/`): ARCHETYPE.md,
value-chain.md, interview-guide.md; modules acceptance-independence, assurance-over-ai, benefit-plans,
completion-reporting, controls-testing, nonprofit-government, planning-risk-assessment, private-company,
quality-management, soc-attestation, specialists, substantive-testing; all 13 use-case YAML files.
Tax (`.../archetypes/tax/`): ARCHETYPE.md, value-chain.md, interview-guide.md; modules compliance-individual-business,
multistate-private, research-advisory; use-cases compliance-individual-business, multistate-private, research-advisory.
Also `.../archetypes/index.md`.

## 6. Left open (outside this brief's edit scope)

- `assurance/sources.md` and `tax/sources.md` were not edited. They still date VALS-TAXAGENT-2026 2026-10-16, give
  JOFA-AIPA-2026 type press (the YAML says professional-body everywhere) and BOARDMEMBER-CAQ-2026 a different URL form
  than the YAML; new keys from the mid-market modules are not in Part B.
- Older assurance files still use two keys for some documents that no new or widened file cites (for example
  IIAF-FRAUD / IIAF-AIFRAUD-2026, K-CLARA / KPMG-CLARA-2025, UNIQUS / UNIQUS-FILER-2026, VERDANTIX /
  VERDANTIX-KPMGFEE-2026, AT-MODUS-2026 / MODUS-2026, CIRCIT-CS-BDONL-2026 in value-chain.md). Tax has three such pairs in
  older files (ACCTODAY-AVALARA-2025 / AVALARA-AGENTIC-2025, IRS-RP2013-14 / IRS-RP201314-2013, WCG-2026 /
  WCG-NOTREADY-2026; in each pair one key appears only in sources.md).
- Across archetypes, the Journal of Accountancy article "Real-life ways small firms use AI" is JOFA-SMALLFIRMS-2026 in
  tax `research-advisory` and JOFA-REALLIFE-2026 in assurance `private-company` (news/ versus issues/ URL).

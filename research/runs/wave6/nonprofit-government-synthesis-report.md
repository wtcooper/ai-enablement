# Synthesis report: assurance / nonprofit-government

Synthesized 2026-10-21. Outputs:
- Module: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/modules/nonprofit-government.md` (300 lines, contents table at top)
- Use cases: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/use-cases/nonprofit-government.yaml` (16 entries; `scripts/validate.py` reports 0 errors and 10 of 16 graded A/B, 62%)

## Counts in and out

- **In:** 15 candidate entries from `mm-nonprofit-government-combined.md`, plus 1 item routed from `mm-private-company-practice.md` (the single-audit side of its PB&H, Perry and Aprio Excel-agent entry). Other routed mentions were checked: the "three nonprofit specialists" were already in the combined file; Guided Assurance Single Audit content [TR-GAFEATURES-2026] has no AI detail, so it is a gap note in the module, not an entry; Oath [OATH-SITE-2026], routed from `mm-widen-assurance.md`, is a reinvent signal in the module and stays an entry in quality-management; peer-review data (from `mm-widen-assurance.md` and the private-company research) went into §5 Metrics; Yellow Book quality management (from `mm-private-company-governance.md`) was already covered. `mm-benefit-plans-combined.md`, `mm-private-company-discourse.md`, `mm-multistate-private-combined.md` and `mm-widen-tax.md` route nothing to this module.
- **Out:** 16 entries. Nothing was rejected.

**Renumbering (old research number to new id):** 01 to 01; 05 to 02; 10 to 03; 07 to 04; 03 to 05; 02 to 06; new to 07 (PB&H, Perry); 09 to 08; 04 to 09; 06 to 10; 08 to 11; 15 to 12; 11 to 13; 12 to 14; 13 to 15; 14 to 16. Entries are now grouped by process area.

## Duplicates merged and cross-references

- **Same story, two pages:** TR-NONPROFITFIRMS-2026 (a community post) repeats TR-NPCASE-2026. Only TR-NPCASE-2026 is cited.
- **Routed PB&H entry:** only the single-audit and grant part was kept (`#07`). Trial balances, footing, state uploads and Aprio stay in the private-company module. Sam Brown CPA's estimate of at least five to six hours saved per audit [TR-SAMBROWN-2026] is not nonprofit-specific. It stays in the private-company module, and `#06` and §5 refer to it.
- **Cross-referenced by full id, not duplicated:** `#01` to `assurance-planning-risk-assessment-01`; `#02` to `assurance-substantive-testing-14`; `#04` to `assurance-planning-risk-assessment-09` and `-12`; `#05` to `assurance-quality-management-12` and `assurance-planning-risk-assessment-02`; `#06` to `assurance-substantive-testing-08` and `-09` and `assurance-controls-testing-04`; `#07` to `assurance-substantive-testing-11` and `-12`; `#09` to `assurance-completion-reporting-06`; `#10` to `assurance-completion-reporting-01` and `-03`. Each entry keeps only what differs for this engagement type: governing-body documents, grant and bond agreements, single-audit tests and small-firm template tuning.
- **Source keys aligned with the archetype** (same document, same key):
  - CASEWARE-VERITY-2026 became CASEWARE-LAUNCH-2026, as in completion-reporting. In substantive-testing, CASEWARE-VERITY-2026 names a different Caseware blog.
  - TR-STATEAUDIT-2026 became TR-STATE-2026.
  - CPAPA-7216-2026 became CPAPA-SETTLE-2026, as in the tax archetype.
  - TIGTA-AISELECT-2025 became TIGTA-2025.
  - The CoCounsel product page was renamed TR-CCAUDITPAGE-2025, because the tax archetype already uses TR-COCOUNSEL-2025 for a different document (the 2025-11-05 press release).
- **Other edits:**
  - Removed unsourced connective sentences from `role_evolution` in 01, 02, 05, 08, 09 and 10.
  - Softened "human verification of every finding" in 14 to match the source.
  - Added the firm type to every entry's notes.
  - Citrin Cooperman is described as "private-company-focused" (the landscape's wording), because no input classifies it as top-100.

## Coverage by ladder and change scope

| | step | process | model | total |
|---|---|---|---|---|
| assist | 03, 05, 11, 15 | - | - | 4 |
| augment | 01, 02, 04, 08, 09, 10, 12, 16 | 07, 13, 14 | - | 11 |
| automate | 06 | - | - | 1 |
| delegate | - | - | - | 0 |

- **Delegate: no evidence.** No source shows an agent owning a multi-step outcome in a nonprofit, single or Yellow Book audit, or in 990 work.
- **Model scope: no entry.** The only signal is Oath, an AI-native firm that lists non-profits among its client types and publishes no clients or results. It is kept as a module note that cross-references quality-management.
- **Automate (06):** sample selection and documentation run without a person, but the auditor sets the strata and approves the sample. A verifier may reasonably reclassify it as augment.
- **Process scope:** two of the three process entries are counterparties or government audit offices (HHS, state auditors), not CPA firms.

## Grade mix

- **0 A, 10 B, 4 C (03, 10, 15, 16), 2 D (08, 11).**
- **No A.** Every firm figure is an owner's recollection or vendor-published, and the 2026-10-17 rule makes all of those B at most.
- **Capped at B:**
  - 05: the Plante Moran survey covers general audit research, not nonprofit work.
  - 12: an academic study of grant proposal writing, an adjacent process.
  - 13: HHS publishes no AI measure.

## Gaps

- **No measured outcome:** no error rate, override rate, parallel run or peer-review or inspection finding for any AI use in this module.
- **Single-audit compliance testing by requirement:** eligibility, allowable costs, subrecipient monitoring, procurement and suspension, and cash management. The only named AI use is PB&H's 63-item grant test, and its source does not name the requirement tested. Major program determination, questioned costs and findings drafting have no evidence at all.
- **Form 990, 990-T and UBI:** one e-file product's AI check and an older, secondary IRS screening report. There is no firm case.
- **No mid-market PE-backed platform** has described its nonprofit or government practice. The named firms are small local firms, one regional firm (PB&H), top-100 firms (Plante Moran, Armanino, Cherry Bekaert, BDO), vendors, regulators and counterparties.
- **Blocked or unread items** remain as listed in the combined file's gaps section: the PKF release body, the GovNFP agenda and the Oklahoma auditor article.
- **Date conflict for the verifier:** this file dates TR-STPIERRE-2026 to 2026-03-09. The private-company research calls the page undated (2026 inferred). Check the page metadata.
- **Key conflicts for the coordinator:**
  - TR-SCALING-2026 (here) and TR-CASESTUDIES-2026 (private-company research) are the same Thomson Reuters blog.
  - CITRIN-DAS-2026 and PKF-DAS-2026 (here) appear as CASEWARE-CITRIN-2026 and CASEWARE-PKF-2026 in the widen-assurance research.
  - AICPA-PA-2026 (archetype key, used here) is AICPA-AIPA-2026 in the landscape.

## Routed to other modules (for their synthesis)

- **private-company** (proposed private-company-assurance): Citrin Cooperman DAS Audit, DAS PCR and DAS EBP on one AI platform (2026-07-13) [CITRIN-DAS-2026]; PKF O'Connor Davies DAS and the Agentic Pioneer Program (2026-10-08, search-only) [PKF-DAS-2026]. These also go to benefit-plan-audits for DAS EBP.
- **quality-management** and private-company: firm-built proprietary agents (Agent Builder, Agent Studio) and Caseware platform governance [CASEWARE-PIONEER-2026].
- **quality-management:** the AICPA practice aid on firms' AI use, and Yellow Book system-of-quality-management dates (designed by 2025-12-15, evaluated by 2026-12-15) [AICPA-PA-2026; GAO-YBFAQ-2025].
- **substantive-testing** and quality-management: the Plante Moran pilot survey on general audit research [TR-PLANTEMORAN-2025].
- **assurance-over-ai:** Prager Metis's argument that auditors test management's information whatever tool produced it [ATODAY-DAVIS-2026].
- **Tax archetype guardrails:** OPR Alert 2026-19 and the section 7216 consent question [IRS-OPR-2026; CPAPA-SETTLE-2026].
- **Tax controversy:** IRS exempt-organization AI screening and the TIGTA findings on selection models [EY-TEGE-2024; TIGTA-2025]. Kept here too as `#16`.
- **Future advisory client-accounting-services:** management-side readiness prompts for nonprofit finance teams [ARMANINO-NFPAI-2026]. Kept here too as idea `#11`.
- **Tax compliance-corporate:** Form 990-T and UBI preparation as a tax service, if the integrator moves nonprofit tax out of this module. This is a design question: the module now folds nonprofit tax into assurance and links to `tax/guardrails.md` rather than restating it.

## Suggested improvements to the briefs

1. **Fix one source key per document across the wave before research starts.** A shared key registry, or a rule to grep existing YAML for the URL first, would have avoided five renames here and three open conflicts.
2. **Ask researchers to tag each routed item with the target module's exact file name** (for example `nonprofit-government`, not "future nonprofit-government module"), and to put entry-level detail in the routed line. The Guided Assurance item arrived with no AI detail and could not become an entry.
3. **Let synthesis briefs cross-reference same-wave modules by a stable handle.** New modules renumber their ids, so a cross-reference to a parallel module's entry by number is unsafe. A stable slug, or a final renumbering pass by the coordinator, would let modules link to each other.
4. **Say how to classify firms that no input labels** (Citrin, PKF, Aprio). The rule "say what kind of firm" pulls toward adding facts. A short firm-type table in the landscape would settle it.
5. **Cap the module at about 280 lines in the brief.** Mandatory sections, 12 probes and a sources list with URLs fill 300 lines exactly, which leaves the verifier no room to add caveats.
6. **Clarify ladder rules for tools where a person sets parameters and approves the output** (the `#06` automate-versus-augment question), with a worked example in `vocabulary.md`.

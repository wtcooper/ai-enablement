# Synthesis report: advisory / private-client (wave 5)

Outputs:
- Module: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/modules/private-client.md` (290 lines, table of contents, 10 sections)
- Use cases: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/private-client.yaml` (17 entries; `scripts/validate.py` reports no errors for this file, and one warning: A/B share 29%, below the 50% target)

## 1. Counts in and out

| Input | Candidates for this module | Used |
|---|---|---|
| adv-private-client-combined.md (combined deep dive) | 16 use cases (A 0, B 4, C 9, D 3) | All 16, kept as ids 01-16 |
| landscape-advisory.md | No entries; leads only (PKF-ASSETA-2026, KAUFMAN-FO-2026, JPM-FAMILYOFFICE-2026, IRS-OPR-2026, SEC-EXAMPRI-FY2026, FSR-FAULHABER-2025) | All already covered by the deep dive, which opened most of them |
| adv-x-independence-pricing.md | 0 entries; one row mapping private-client restrictions (SEC 2-01 (c)(4)(viii), PCAOB Rule 3523); says it found no pricing or data-handling evidence for this module | Used in the guardrails and in the risks of #01, #04, #08, #14, #15 |
| adv-x-state-of-ai-disruption.md | 0; it says no disruption evidence specific to this module was found | Nothing to carry |
| Items routed to private-client from other adv files | 2: GWCPA's custom GPT on ownership transitions (JOFA-REALLIFE-2025, from CAS practice); family offices as a CAS vertical at Sweeney Conrad (JOFA-CASTIPS-2025, from CAS discourse) | GWCPA becomes the new #17 (grade B). Sweeney Conrad has no AI content, so it is context in module §1 only |

In: 17 candidates. Out: 17 use cases. Nothing was dropped.

## 2. Duplicates merged

No two entries describe the same change to the work, so none were merged. Overlaps checked and kept apart:
- #01 (PKF/Asseta platform runs the accounting process) and #15 (hybrid family-office operating model): one is a process redesign, the other a sourcing model. They share PKF-ASSETA-2026.
- #03 (AI-drafted commentary, a step) and #10 (live consolidated view that replaces periodic packages, a process).
- #08 (Mercer's Aspen coordination graph, in production) and #09 (Compound's announced drafting agents): different firms, products and maturity.
- #12 (successor modelling idea) and #13 (owner exit-readiness idea): different engagements and sources.
- Cross-module overlaps are cross-referenced by id in `notes` rather than duplicated: #04 with advisory-client-accounting-services-01, -02 and -03; #03 and #10 with -06; #16 with -07; #07 with -10, advisory-risk-controls-23 and advisory-forensic-disputes-12; #14 with advisory-risk-controls-17 and -18 and advisory-client-accounting-services-20; #11 with professional-services-knowledge-management-21; #02 with tax-compliance-individual-business-02; #06 with tax-research-advisory-13; #15 with professional-services-scoping-pricing-17; independence with advisory-client-accounting-services-24 and assurance-acceptance-independence-15.

Other edits to the deep-dive entries:
- The "general background, unverified" independence lines in #01 and #15 were replaced with sourced statements (SEC-RULE2-01-2026 (c)(4)(i); JOFA-NONATTEST-2016; IESBA-TECH-2023 606.3 A1). The same point was added to #04. #08 gained the (c)(4)(viii) investment-adviser point, labelled as an analogy because Mercer is not an accounting firm. #14 gained the AICPA consent point (JOFA-ETHICSAI-2026).
- Organization types were added to `notes` where the entry lacked them.
- No grades, figures or modal verbs were changed.

## 3. Coverage by ladder and change scope

| Ladder \ scope | step | process | model | Total |
|---|---|---|---|---|
| assist | 05, 06, 11, 12, 13 | - | 14 | 6 |
| augment | 02, 03, 04, 07, 09, 16 | 08, 10 | 15 | 9 |
| automate | 17 | 01 | - | 2 |
| delegate | - | - | - | 0 |
| Total | 12 | 3 | 2 | 17 |

- **Delegate: no evidence.** Forum speakers (WISS-FOAI-2026) and Citi (CITI-AIFO-2026) describe agents executing workflows as the direction of travel, but no named deployment exists. No entry was invented. The module says so in §3.
- Automate rests on one announcement (#01) and one marketing chatbot (#17).
- Model scope has two C entries and no deployment that has been sold.

Maturity: in-production 5 (02, 05, 06, 08, 17); announced 6 (01, 07, 09, 10, 14, 15); emerging 6 (03, 04, 11, 12, 13, 16).

## 4. Grade mix

A 0, B 5 (02, 05, 06, 08, 17), C 9, D 3 (11, 12, 13, each labelled 'Idea').
- No figure is reported as measured by the named organization. GWCPA's "about 50" sign-ups is a practitioner's own figure, so it is B under the 2026-10-17 rule.
- #08 Mercer is B on company-reported deployment counts, and the entry is adjacent: it comes from a wealth platform, not an accounting firm.
- The A/B share is 29%, below the validator's 50% target. This reflects the evidence, not a gap in the merge.

Pattern `other` is used six times (05, 12, 13, 14, 15, 16), each explained in `notes`. Candidate new patterns: "individual general-assistant use" (05), "advisor-led modelling or diagnostic session" (12, 13, 16), "operating-model split, what is outsourced versus kept" (15), "advisory deliverable: policy, inventory and vendor review" (14).

## 5. Gaps

- No independent measurement of any kind: no error or override rates, no parallel runs, no client-satisfaction data, no inspection findings.
- Succession and owner advice has one named tool, and it is marketing (#17). Engagement use is ideas only (#12, #13).
- Primary surveys not opened: J.P. Morgan 2026 (figures are secondary), the Citi PDF, the RBC 2026 full report and its sample size, the Ocorian report, and the Campden/AlTi report cited by Armanino.
- Not searched: guidance from the AICPA PFP section, CFP Board and STEP. Family-office AI pages from top-100 firms (Baker Tilly, EisnerAmper, Citrin Cooperman, Withum, Cherry Bekaert) were not found.
- The independence file found no pricing or client-data evidence for this module. No source addresses independence for family-office accounting sold to the firm's own attest clients.
- Holland & Knight's piece on principals asking AI instead of their advisors (HK-PRINCIPALS-2026) was seen in search only, and its URL returned 404.

## 6. Routed to other modules (collected from the inputs)

- **tax:** Wealth.com's AI estate and tax planning platform, its $65M Series B and its claims (WEALTHCOM-SERIESB-2026; WEALTHCOM-INVNEWS-2025). K-1 compliance calendars, IRC 7216 and Circular 230 duties (IRS-OPR-2026). Mercer's tax-preparation actions inside Aspen (MERCER-ASPEN-2026).
- **Out of scope (regulated investment advice):** portfolio management and manager selection in Aspen; the RBC, JPM and UBS allocation findings; the FSR literature review on AI in financial planning (FSR-FAULHABER-2024).
- **client-accounting-services:** the Stanford JAR SME bookkeeping study (STANFORD-JAR-2026), already used there.
- **valuation (no module file yet):** Masttro's claimed AI valuation of private equity and venture holdings (MASTTRO-JEFFERSON-2026 platform pages; vendor claim).
- **risk-controls:** AI governance and policy advisory (SQUIRE-FOAIRISK-2026; NT-FOAIPOLICY-2026); AI-enabled fraud and control design (CFO-DEEPFAKE-2026; AJG-CYBER-2026).
- **forensic-disputes:** investigation of deepfake impersonation and payment fraud (CFO-DEEPFAKE-2026).
- **professional-services:** how firms staff and price family-office work, PE ownership of firms, and firms' own AI policies for staff.

## 7. Verification and consistency notes

- Opened in a private temporary folder to confirm wording: JOFA-REALLIFE-2025 (the GWCPA case and its "about 50" figure), JOFA-CASTIPS-2025 (Sweeney Conrad lists family offices as one of four CAS verticals) and CITI-AIFO-2026 (the "16%, more than doubling in one year" wording). No new facts were taken from these pages beyond what the entries state.
- **The same documents carry different refs across advisory files.** The CAS YAML uses IESBA-TECHREV-2023 and JOFA-ETHAI-2026, while this module and the independence file use IESBA-TECH-2023 and JOFA-ETHICSAI-2026. The disruption file cites BLOOMBERG-PRICING-2026 where the independence file has BBLAW-PRICING-2026 (it appears to be the same article). The SEC-RULE2-01-2026 date also differs between files (2026-10-01 and 2026-10-20). These should be reconciled archetype-wide.
- **Date conflict.** The brief says today is 2026-10-19, but the research runs are dated 2026-10-20, so `last_reviewed` is 2026-10-20 throughout.

## 8. Suggested improvements to the briefs

1. Give the brief a canonical ref list for shared documents (SEC rule, IESBA, JofA ethics, Bloomberg pricing), so cross-cutting and module files stop minting variant refs.
2. Make the date in the brief match the run date, or say which one `last_reviewed` should use.
3. For low-evidence modules, let the A/B target scale with the landscape's evidence-density rating, or have the brief say the validator warning is expected.
4. Ask module researchers to search professional-body guidance (AICPA PFP, CFP Board, STEP) before the web budget runs out; the private-client run ran out first.
5. Have every research file state the organization type in each entry. The synthesis had to add it to several entries.
6. Add `operating-model split` and `advisor-led diagnostic` as candidate patterns, or tell researchers which `other` uses are acceptable.

# Verification report: assurance / nonprofit-government

Verified 2026-10-21. Files edited in place:
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/use-cases/nonprofit-government.yaml`
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/modules/nonprofit-government.md` (299 lines, was 300)

Method: 50 cited sources (plus 3 found during checking) were downloaded to a private temp folder. Each was read for
existence, date (byline, `article:published_time`, JSON-LD, `w-published-date`, PDF metadata) and support. Blocked
pages were read through the r.jina.ai mirror or a publisher API. No web search was used. `scripts/validate.py`: 0 errors.

## Counts

- **Use cases checked:** 16
- **Kept unchanged:** 3 (03, 08, 09)
- **Fixed:** 13 (01, 02, 04, 05, 06, 07, 10, 11, 12, 13, 14, 15, 16)
- **Rejected:** 0
- **Final grade mix:** 0 A, 10 B, 4 C, 2 D (no grade changed). A or B: 10 of 16 (62%).
- **Module:** about 20 statements fixed, 2 sources dropped or replaced, 1 frontier signal added (Uniform Guidance rewrite barred through 2026-12-11).

## Targets

| Target | Result |
|---|---|
| 12–20 use cases | Met (16) |
| At least 50% graded A or B | Met (62%) |
| Every source dated | Met. Every YAML source has a URL and an ISO date. Undated or year-only dates were narrowed where metadata allowed. |
| Ids unique, values from vocabulary | Met (validator 0 errors; 16 unique ids) |
| Quotations under 25 words | Met |
| Cross-references name existing entries | Met. All 16 `assurance-…` ids cited exist; the reinvent note now names `assurance-quality-management-28`. |

## Key and date conflicts resolved

| Conflict | Resolution |
|---|---|
| TR-SCALING-2026 vs TR-CASESTUDIES-2026 (same blog) | Kept **TR-SCALING-2026**. The private-company YAML, now in the plugin, also uses TR-SCALING-2026, so the archetype has one key for it. |
| TR-STPIERRE-2026 date (2026-03-09 here, "undated" in private-company research) | Kept **2026-03-09**. The page carries `w-published-date` and `publishDate` = 2026-03-09 but no visible byline date; noted in `#01`. |
| CITRIN-DAS-2026 vs CASEWARE-CITRIN-2026 | Renamed to **CASEWARE-CITRIN-2026**, the key used in quality-management, planning-risk-assessment and private-company. (benefit-plans still uses CITRIN-DAS-2026; that is for its own verifier.) |
| PKF-DAS-2026 (pkfod.com, search-only) vs CASEWARE-PKF-2026 | Replaced with **CASEWARE-PKF-2026** (Caseware release, opened in full, 2026-10-08), matching the archetype. |
| ORSCPA-PEERREVIEW-2025 vs OSCPA-PR-2026 (same Oregon PDF) | Renamed to **OSCPA-PR-2026**, as in soc-attestation and private-company. |
| OATH-SITE-2026 vs OATH-2026 | Renamed to **OATH-2026**, as in quality-management. |
| AICPA-PA-2026 vs AICPA-AIPA-2026 | Already AICPA-PA-2026 (archetype key); no change. |
| TR-STATE-2026 title | Aligned to the page title used elsewhere: "The state of AI in audit in 2026: Interview with experts". |

## Fixes and rejections

| Item | Fix | Reason (error pattern) |
|---|---|---|
| `#01` prerequisite | "did not summarize until customized" became "said it was 'not summarizing'; it then applied the vendor's prompt customizations" | Embellished outcome. The source does not say the template then worked. |
| `#01` risk | "Donor and personal data in minutes" became Gemifi cofounder's PII worry keeping accountants on Microsoft tools | Connective claim. The article never mentions minutes or donor data. |
| `#01` role_evolution | Forde's "act without me" quote no longer tied to minutes | Wrong context. The quote is about judgment and inherent risk, not minutes. |
| `#01` notes | Added Forde's nonprofit "hour to a couple of minutes" figure (handbook and internal control documentation) and the St. Pierre date basis | Context for the commercial-firm figure. |
| `#02` risk | "accuracy depends on" became "vendor says accuracy improves when"; "rather than a guess" became "rather than verbose output" | Embellished qualifier. |
| `#02` risk and source | Removed the GAO fraud-testimony guardrail and its source | Adjacent-process connective. A fraud and improper-payments testimony is not about agreement extraction. Also misattributed: "human in the loop" is GAO's testimony, not its AI Accountability Framework. |
| `#04` role_evolution | "seniors review instead of explaining" replaced by the sourced Forde and Sam Brown statements | Unsourced connective claim. |
| `#04` notes | The Risk Suggestion Agent was in the 2026-05-20 launch release (alpha) and launched worldwide 2026-10-06 | Wrong claim that the page was not opened and the agent launched "later". |
| `#05` risk | "An interviewee… test systems on their own work" became Thomson Reuters' head of audit product (vendor), "evaluate and test them themselves" | Speaker unnamed and a vendor; "on their own work" embellished. |
| `#05` source | GAO-YBFAQ-2025 date 2025-12 became 2025-12-15 | Imprecise date (the report shows "Published: Dec 15, 2025"). |
| `#06` role_evolution | "owners describe not backfilling" became the vendor's framing | Wrong attribution. "Without backfilling departures" is vendor narrative; Wells' own words are "Technology is improving my margins despite the staff shortage." |
| `#06` risk | "so the rules are still being taught" removed; workshop described factually (Appendix B of the 2025 guide) | Unsourced connective claim. |
| `#06` notes | Workshop date note corrected: the page heading says 2026 workshops on Monday, June 15 | Date note was wrong ("approximate"). |
| `#07` title, solution, prerequisite | Removed "reusable agents run single-audit tests for clients in a common format". The 70 consistently reporting school districts and the planned reusable agents are for trial-balance formatting. The 63-item compliance test was one test. Perry's work was a consultancy engagement. | Claim attributed to the wrong part of the source; embellished scope. |
| `#07` sources | PB&H date 2026 became 2026-08-31; Perry 2025 became 2025-09-19 (page metadata) | Missing precise dates. |
| `#10` prerequisite and source | "adopted it on 2026-07-13" became "adoption was announced 2026-07-13"; key renamed | Release date reported as adoption date. |
| `#11` role_evolution | "compiling to checking" became "away from reconciliations and compiling information toward analyzing it"; speaker named (AHRC New York City CFO) | Misquote. |
| `#11` notes, problem | 65% vs 60% explained as two different measures; MOMENTIVE-2026 cited in the problem text | Statistic reported as something it does not measure (the 65% subtitle is "all financial operations"). |
| `#12` outcome | "beat general-purpose models" became "scored above general-purpose models (not significantly above Gemini 2.5 Pro)" | Overstated. The paper reports the Gemini 2.5 Pro difference as not statistically significant. |
| `#13` title, role_evolution | The rigor review is now separate from the AI analysis; each clause has its own ref | Connective claim (HHS does not say AI reviews rigor); a clause lacked its source. |
| `#14` title, solution | Split North Carolina (AI on spending data) from Washington (policy only; no audit uses described) | Claim attributed to the wrong organization. Washington's page describes no anomaly detection. |
| `#14` source, risk | NCAUDITOR date 2026-07-08 became 2026-07-09 (`datePublished`; the interview aired 07-08); GAO-FRAUDAI-2026 now cited (it was listed but unused) | Wrong date; uncited source. |
| `#15` risk | "section 7216 consent unresolved for 1040-series returns" became "IRS has not said whether sending return information to an AI tool is a 7216 disclosure" | Misreading. The 1040 reference in the source concerns the consent format only. |
| `#16` role_evolution | "Practitioners should expect 990 data to be screened" became the sourced EY statement | Unsourced connective claim. The AI tool screens public referrals, not 990 data. |
| Module §2 | "2026 Supplement unreleased as of 2026-10-08" became "as of September 2026"; "no backfilling" removed from the firms' pains; the 65% measure explained; rewrite barred through 2026-12-11 added | Date the source does not give; vendor framing presented as a firm claim; missing development. |
| Module §3 | `#07` and `#14` bullets aligned with the entry fixes; reinvent note drops "venture-backed" (not on the cited page) and names `assurance-quality-management-28` | Claim not in the cited source. |
| Module §4 probe 3, §9 | St. Pierre template wording aligned with the entry fix | Embellished outcome. |
| Module §5 | Oregon report coverage corrected (Oregon, Hawaii, Guam, Northern Mariana Islands); key renamed | Imprecise description. |
| Module §6 | "Nonauthoritative" removed from the AICPA practice aid (not in the release); 7216 wording fixed; "N/A rather than guess" fixed | Unsourced qualifier; misreading. |
| Module §7 | Backfilling attributed to the vendor; Forde's quote no longer tied to minutes | Wrong attribution. |
| Module §8 | Yellow Book FAQ dated 2025-12-15. Comment close (2026-07-13) confirmed through the Federal Register API, so "per a search summary" removed. Added the 2026-09-02 continuing resolution barring finalization through 2026-12-11 [OMB-UG-2026]. NC date 2026-07-09. Caseware "named customers" became "Caseware customers" (they are customers, not program participants). The GovNFP conference page now shows the 2027 event, so AICPA-GOVNFP-2026 was dropped and the 2026 Dallas dates rest on AICPA-NFPAI-2026. | Dates; a source that no longer supports the claim; a missed frontier signal. |
| Module §9 | "Uniform Guidance is being rewritten" became "proposed, though barred from finalization through 2026-12-11"; "few professionals are near the skill ceiling" became the quoted "no one is anywhere near" | Stale regulatory statement; softened quote. |
| Module §10 | OMB-UG-2026 dated 2026-09 (PDF created 2026-09-18). TR-GAFEATURES-2026 dated 2026-05-20 and TR-SAMBROWN-2026 2026-05-11 (page metadata). Aprio posting title corrected to "Senior Audit Manager, Non-Profit". FR-OMB note says the page was read through the API. | Imprecise dates and titles. |

**Grades checked and kept:**
- 05 and 12 are correctly capped at B: the evidence comes from general audit research and from grant writing, both adjacent processes.
- 13 and 14 are B: the organizations are named, but there is no AI measure.
- 16 stays C: secondary source, and the launch is unconfirmed.
- No figure seen only in search results supports any A or B entry. The `#13` ChatGPT claim was already excluded.

## Sources that could not be reached directly

| Source | Route used |
|---|---|
| GAO-26-108850 highlights PDF (403) | r.jina.ai mirror (full text; dated 2026-01-13) |
| HHS AERO press release (403) | r.jina.ai mirror (full text; dated 2026-05-21) |
| Momentive release on aimagazine.com (403) | r.jina.ai mirror (full text; dated 2026-08-06) |
| JMIR GrantCheck (empty 202) | r.jina.ai mirror for the text; Crossref for the publication date (2025-11-27) |
| Federal Register proposed rule (CAPTCHA) | Federal Register API: published 2026-05-29, comments closed 2026-07-13. The docket id in the module text was not confirmed and was removed. |
| AICPA GovNFP conference page | Opens, but now advertises the 2027 event; dropped as a source |

**Not attempted (already marked as gaps):** the Oklahoma state auditor article and the 2026 GovNFP agenda.

## Error patterns to fix in the briefs

1. **Vendor framing presented as practitioner words.** Vendor case studies wrap quotes in their own narrative, for example "without backfilling departures" and "without a top-down mandate". Briefs should require that a quoted claim come from inside the quotation marks, and that the surrounding text be labelled "the vendor says".
2. **A quote moved to the wrong use.** One general quote ("act without me") was attached to the minutes use case. Ask researchers to note which task each quote is about.
3. **Scope inflation across sections of one source.** PB&H's 70 school districts and its reusable agents are for trial-balance formatting, but they were joined to its one single-audit test. When a source describes several uses, require one sentence per use.
4. **"Beat" or "outperformed" without significance.** For academic sources, ask for the paper's own significance statement next to any comparison.
5. **Two organizations merged into one claim** (North Carolina and Washington in `#14`). One title should not credit two bodies with a practice that only one describes.
6. **Regulatory status goes stale between research and synthesis.** The Uniform Guidance pause was signed 2026-09-02 and was missed. Add a step that checks the status of every proposed rule cited before synthesis.
7. **Dates.** The briefs should name the page-metadata fields to check (`w-published-date` on Thomson Reuters pages, `publication_date` on DataSnipper pages). Several "undated" pages had machine-readable dates.
8. **Key registry.** Four keys differed from archetype keys for the same URL (Citrin, PKF, Oregon peer review, Oath). A check that greps existing YAML for the URL before minting a key would prevent this.
9. **Module line cap.** As the synthesis report said, a 300-line cap leaves the verifier no room. A 280-line cap in the synthesis brief would help.

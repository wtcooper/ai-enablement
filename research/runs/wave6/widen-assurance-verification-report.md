# Verification report: mid-market widening of assurance quality-management, soc-attestation, assurance-over-ai

Done 2026-10-21. Scope: only the entries and module sections the widening added or changed, as listed in
`widen-assurance-synthesis-report.md`. Every cited source for those changes was opened (curl, text extracted) unless
listed under "Sources not reached". `python3 scripts/validate.py`: 0 errors (31 warnings overall; the only warnings
for these files are the existing count and A/B-share target warnings for quality-management and assurance-over-ai).
Line counts: quality-management.md 291, soc-attestation.md 299, assurance-over-ai.md 285.

## Counts

| | Kept | Fixed | Rejected |
|---|---|---|---|
| quality-management (12, 13, 14, 16, 24, 26, 27, 28) | 3 (12, 14, 24) | 5 (13, 16, 26, 27, 28) | 0 |
| soc-attestation (17, 18) | 1 (17) | 1 (18) | 0 |
| assurance-over-ai (25, 26, 27) | 2 (25, 26) | 1 (27) | 0 |
| **Total entries** | **6** | **7** | **0** |

Module sections: 8 fixes across the three files (table below). No grade changed. The final grade mix is unchanged:
quality-management B 10, C 13, D 5 (36% A/B); soc-attestation B 11, C 7 (61%); assurance-over-ai B 7, C 13, D 7 (26%).
No entry is grade A, which is correct under the 2026-10-17 rule: the Plante Moran survey, MSCI test counts, UiPath
figures and Sanville outcomes are all vendor-published.

## Fixes

| Where | Fix | Reason (error pattern) |
|---|---|---|
| QM-13 problem | Removed "reviewers are asked to understand a firm's use of technology" from the JOFA-QMPR-2024 claim; "expected to begin in 2026" became "generally not expected before 2026" | Wrong document: the technology point is in the May 2026 SOC 2 guidance (JOFA-PRB), not the 2024 QM article; wording matched to source |
| QM-13 problem and risk | Added that the Oct 2025 Reviewer Alert has an article on AICPA technology TQAs (title only, not read) | All six editions' contents checked. "None titled for AI" holds, but the nearest item was left out |
| QM-16 problem | Replaced the unsourced sentence about regional firms running different tools with Caseware's own pitch (CASEWARE-PKF-2026), labelled as vendor framing plus inference | Unsourced connective claim |
| QM-16 solution | The dates are now announcement dates ("announced on 13 Jul 2026 that ... had implemented") | Date misread: the wording suggested adoption on the release date |
| QM-26 problem | "therefore have no AI line in the generic starting material" became "the public description gives no sign of an AI line; member-only libraries not checked" | Overstated, and contradicted the entry's own note that the libraries were not checked |
| QM-27 problem | The "disconnected one-off tools" risk is now attributed as Caseware's framing (vendor view) | A vendor claim stated as fact |
| QM-27 notes | SAV Associates "small cross-border firm" became "Toronto firm with US offices; size not stated" | Embellished qualifier |
| QM-28 problem | Dropped "at the scale AI platforms need"; "the PCAOB lists" became "PCAOB officials (acting chair Botic and inspections director Gunia, Dec 2025)" | Embellished cause; speaker precision |
| QM-28 solution | The $10 million is now attributed to Accounting Today, not to Ho; Oath's "early access" status added (OATH-2026) | Claim attributed to the wrong speaker |
| QM-28 role_evolution | "PCAOB board member Botic" became "acting chair Botic, Dec 2025"; wording matched to source | Wrong title at the time of the speech |
| SOC-18 problem | Unsourced demand claim and "many mid-size firms have no AI-governance team" replaced with a labelled inference plus the sourced independence point | Unsourced connective claims |
| SOC-18 solution and risk | Fieldguide experience is now marked "a plus" (it sits under "How You'll Stand Out"); "advisory on an AI system" became "developing or hosting" as the source says; source described as an AICPA Ethics Division article | Embellished qualifier; overstated scope |
| SOC-18 notes | The AI-tool-use point is clarified as role-wide, not SOC-specific; added that grade B is borderline (the posting shows the service line exists, not a delivered engagement) | Overstatement |
| AOAI-27 problem and solution | "Mathematician who maintains the problem list" became "sent mathematician Viktor Monakhov"; review-time wording matched to source; "cannot scale" matched to "need more scalable ways" | Not in source; embellished |
| AOAI-27 risk | The common-mode point is now a question the author raises ("not necessarily a widespread audit problem today"), not a warning | Embellished qualifier |
| AOAI-27 source | JOFA-MATHEX-2026 type changed from press to professional-body | Consistency with every other JofA key |
| QM §10 | "Practice aid is the first AI content for this system" became "adds a part on firms' QM policies for AI tools, after the Dec 2025 design deadline"; Reviewer Alert technology-TQA note added | Unsourced superlative |
| QM §8 | Reordered the 2026-05, 2026-06 and 2026-07 items into date order (same line count) | Dates out of order |
| SOC §8 | 2026-02-01 now comes before 2026-02-03, and the 2026-07-14 AIUC item moved ahead of 2026-08-04 | Dates out of order |
| SOC §10 | Baker Tilly upgraded from search-only to an opened firm release, labelled as a large PE-backed firm (not mid-market) with no figures | The source was reachable; firm kind was missing |
| SOC §11 | SCHELLMAN-AIGOV-2026 date changed from "undated" to "2026" (year from title; HTTP last-modified 2026-10-15); BAKERTILLY-FIELDGUIDE-2026 entry updated (Baker Tilly release, opened) | Format rule: never "undated" |
| AOAI §8 | 2026-09-24 MSCI item now comes before 2026-09-28 | Dates out of order |
| AOAI §10 | "auditors of any size" became "including those of private companies" | Qualifier not in source |

## Kept (confirmed against source)

- QM-12 (Plante Moran): the 140+ participants and the 91% and 62% survey shares are on the TR page dated 2025-11-20; RSM calls itself the "leading provider ... for the middle market".
- QM-14 (AuditFile QualityLink, 4 Dec 2025): features, the "available to all AuditFile customers" line and the absence of customers and figures are confirmed. The QMCore page text has no AI, and its HTTP last-modified is 2026-10-15.
- QM-24 risk lines: AU-C 210 and the state advance-disclosure laws are in both AT-AICPAPA-2026 and CFODIVE-AICPAPA-2026.
- SOC-17: the joint offering, 40,000+, "several CPA firms", PwC named (AT), early-2027 launch, the AIUC-1 process (scoping, evals, audit, certificate valid one year), and UiPath's 250+ / 2,000+ / 8 weeks are all confirmed. The "Oct 18" header is also confirmed.
- AOAI-25 (MSCI ~1,400 tests, 112 roles, attestation to SOX auditors, risk tiers, CISO quote) and AOAI-26 (78 core controls; 33, 40 and 5) are confirmed verbatim.
- Module figures confirmed:
  - Tennessee 2025 peer review data (424 firms; 40 of 46; 34 of 448; 6 of 16; SOC 1 of 2)
  - CPA.com 54-firm survey (75%, nearly a quarter)
  - ICAS / Beever and Struthers (72%, 74%, 22%)
  - CFO Dive (51 pages, ASB and peer review)
  - Schellman 74% / 27% (landing page)
  - Prager Metis / Davis
  - AT-PEEC (81 letters; re-exposure in Oct or Nov, adoption "next May")
  - GAO Yellow Book FAQ dates
  - GAQC watch item
  - Peer Review Conference listing (no AI session; it has an APS session)
- Cross-references checked and existing: assurance-acceptance-independence-20 (Oath), assurance-substantive-testing-10 (Sanville), assurance-controls-testing-10 and -15, assurance-assurance-over-ai-13, -18 and -19, assurance-soc-attestation-12 to -18, and the completion-reporting Caseware Citrin entry.

## Sources not reached

- AICPA practice aid PDF (member-only). The entries rest on the AICPA release, the resource page, Accounting Today and CFO Dive, as already stated.
- Reviewer Alert article text (free login). Only tables of contents were read, for all six editions.
- AICPA QM peer review checklists (member-only; teaser read).
- Sensiba AIUC-1 accreditation: still search-only (LinkedIn). It stays in SOC-17's sources as a labelled lead and does not support the grade.
- The Wall Street Journal report behind CFO Brew (paywall; not attempted). The second-hand status is already stated.
- ICAS / Alliance MBS study itself (press report only, as already stated).

## Targets

- soc-attestation: 18 entries, 61% A/B. Meets targets.
- quality-management (28) and assurance-over-ai (27): above the 25-entry cap and below 50% A/B. These are validator warnings that the widening already flagged, unchanged here.
- Every source in the changed entries has a URL and an ISO date. All quotations are under 25 words. Ids are unique.

## Error patterns to fix in the briefs

1. **Attributing a point to the wrong document.** Points from a neighbouring source (JOFA-PRB) were credited to the source they sit next to (JOFA-QMPR). Ask synthesis to re-open the cited source for each clause.
2. **Unsourced bridging sentences.** These mostly appear in `problem` fields of entries built from press releases (QM-16, SOC-18). Require a ref or an explicit "inference" label.
3. **Release dates read as event dates.** Write "announced on X that ... had".
4. **Titles and speakers drift.** Board member vs acting chair; a reporter's figure attributed to the interviewee.
5. **Frontier lists get out of date order** when items are appended. Ask synthesis to re-sort §8 after edits.

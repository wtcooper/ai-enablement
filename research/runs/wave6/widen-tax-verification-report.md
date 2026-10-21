# Widen tax verification report (compliance-individual-business, research-advisory)

Run 2026-10-21. Scope: the mid-market additions listed in `widen-tax-synthesis-report.md`. That means compliance-individual-business (CIB) entries 26-31, changed entries 02, 05, 06, 12, 18, 21 and 24, and §10. It also means research-advisory (RA) entries 26-28, changed entries 13, 14 and 25, and §10. The multistate-private module was not touched. Every cited source in scope was fetched and read, through direct curl or the r.jina.ai mirror, and dates were checked against `article:published_time`, JSON-LD or the page's own date.

## Counts

| | Checked | Kept | Fixed | Rejected |
|---|---|---|---|---|
| CIB entries | 13 | 5 (02, 18, 27, 29, 31) | 8 (05, 06, 12, 21, 24, 26, 28, 30) | 0 |
| RA entries | 6 | 2 (13, 25) | 4 (14, 26, 27, 28) | 0 |
| Module §10 / §11 | 2 | - | CIB 6 edits; RA 2 edits | - |

No grade changed. Final mix: CIB A 1, B 9, C 18, D 3 (31 entries, 32% A/B). RA A 0, B 11, C 10, D 7 (28 entries, 39% A/B). All new entries are still C, or D for RA #28. #24 stays B on Multiplier, and #14 stays B on its named users plus One Stop CPA. `scripts/validate.py` reports 0 errors. The only warnings are the existing content-target ones: entry counts above 25 and A/B share below 50%. Module lengths are 299 (CIB) and 287 (RA) lines. Every cross-reference id in the four files resolves, including `tax-multistate-private-14`, `tax-research-advisory-09`, `-13`, `-23` and `tax-compliance-individual-business-08`, `-14` and `-31`.

## Fixes

| Where | Fix | Reason (error pattern) |
|---|---|---|
| CIB #05 notes | "a top-100 firm, per the mid-market research" changed to the article's own wording ("a top 100 CPA firm"; "dozens of complex K-1s") | Wrong attribution: the claim is in CPAPA-BLACKORE-2026 itself |
| CIB #06 risk | "the signer carries the liability" replaced by the source's "under preparer penalty rules" and "automation without oversight is negligence" | Embellishment; Oliver does not say the signer carries the liability |
| CIB #06 notes | Added that CPAPA-BASIS-SERIESB reports the company's claim that about 30% of top-25 firms use Basis, not tied to the 1065 demo | Note said the article named no "Top 25" context; it does, as a company claim |
| CIB #12 problem | "long checklists covering M-1, M-2, basis schedules and capital accounts" changed to the course's own terms (multiple checklists; Schedule M-1, shareholder basis, §704(b) capital accounts) | M-2 is not in the NYSSCPA course description; embellished qualifier |
| CIB #12 outcome, notes; CIB §10 | Paramount Tax and JCG Tax are no longer called "small firms"; JCG quote attributed to its head of production | Filed's page gives no firm size (unsupported connective claim) |
| CIB #21 risk; RA #28 risk | "consent cannot be a condition of service" changed to "conditioning services on consent generally makes it involuntary" | The source says "generally"; the qualifier had been dropped |
| CIB #24 solution, prerequisites, checkpoints, role_evolution, sources, notes | Aardvark claims ("AI-native", AI-assisted review, signing readiness) re-sourced to a live Head of Tax Operations posting (new key AARDVARK-HTO-2026). AARDVARK-STM-2026 repointed to the live Workable copy, dated at access 2026-10-21, with wording matched to it. "Venture-backed" removed from the text (funding seen only in search results, now in notes) | The cited auditfriendly copy is gone (410), and the live Senior Tax Manager text does not contain "AI-native", "AI-enabled tools" or "review AI-assisted output" (claims not in the cited document) |
| CIB #26 source; CIB §10, §11 | NATP-RCOMP-2026 relabelled from "sponsored content" to "blog post by WageProof's founder" | The page carries no sponsored label; the author is the vendor's founder (wrong characterization) |
| CIB #28 risk | OPR's cross-client repurposing risk quoted accurately; "a multi-entity workspace must keep ownership groups apart" marked as this file's inference | Unsourced connective claim attributed to OPR |
| CIB #30 problem, risk, locator; CIB §10 | WCG's "last mile" changed to "reset risk"; the point now says it comes from WCG's Instead section | Misattributed phrase: WCG's "last mile" is about Black Ore; the proprietary-platform critique is "reset risk", aimed at Instead |
| RA #14 outcome; RA §10 | The two-hour answer is reported as the Journal of Accountancy's account of the CEO, "within" not "under" two hours | Wrong speaker and figure wording; the article narrates it rather than quoting the CEO |
| RA #26 solution | TR-COCOUNSELCORP-2026 identified as the in-house product page | Adjacent-audience source not flagged |
| RA #27 solution | Intuit Assist works from "the client's goals", not "the firm's goals", and suggests strategies rather than completing plans | Misquoted source |
| RA #27 locator, role_evolution; RA §10 | Task-reallocation figure moved to Figure 18 p.24 (not Figure 19); 39% stated as the "primary driver" | Wrong locator; statistic described as something it doesn't measure |

Confirmed without change, among others: WK-SCANGA-2026 (2026-06-29; 10-15 minutes per K-1; up to 60-80%; 30-70% for early users), INSTEAD-EFILE-2026 (2026-05-08; 4-6 hours to under 60 minutes; 60-80% of staff time), the Instead S corporation, CPA and entity pages, WageProof pricing and the 15-minute figure, IRS FS-2008-25, Form 7203, Intuit basis tracking (2024-07-03), CoCounsel Tax, the TR fiduciary page (no AI function), the AICPA survey (1,808; 20% expanding; 42% estate, trust and gift; 93%; Holistiplan 2%), TR-SOTP-2026 (600 respondents; size bands; 63% vs 35%; 57% and 47%; 74%; 78% hourly; 20-24% vs 28%; 28% and 37%), Gelt (2025-12-29; "AI-native tax platform"), Wealth.com (2026-04-16; 100,000+ documents; 1,000+ calculations), the ACTEC transcript (2026-02-05), the two State of Estates posts, OLIVER-BOSUMMIT-2026 (sponsored by Black Ore; 2-4 weeks versus 18-24 months), CPAPA-SETTLE-2026 (2026-10-12, Steven de la Fe), CPAPA-ACCRUAL-2026, NYSSCPA-AIPREP-2026 (Byron co-founders, 2026-07-29), TR-R2RBLOG-2025, the WCG November 2026 roadmap note, and TR-SAMBROWN-2026 (Troy, Ohio; junior staff run scenarios).

## Sources not reached

- `jobs.auditfriendly.co` Senior Tax Manager copy (AARDVARK-STM-2026's original URL): HTTP 410 and unreachable through the mirror. Replaced by the live Workable copy, which matches the startup.jobs copy, plus the Head of Tax Operations posting.
- `apply.workable.com` (Cloudflare rate limit 1015); `jobs.workable.com` was used instead.
- NATP blog and Wolters Kluwer "What's new" returned 403 on direct fetch; both were read in full through r.jina.ai. The mirror itself began refusing anonymous requests later in the run.
- Cynch AI funding (Series A, December 2025): search results only, so it is not stated as fact.
- Out of scope and still unchecked, as the synthesis report says: IRS Publication 505 safe harbor, the ABA text behind the ACTEC statement, and the section 7216 consent format for 1065 and 1120-S returns.

## Error patterns for the briefs

- A phrase lifted from one section of a source and applied to another ("last mile").
- Qualifiers dropped from legal statements ("generally").
- Firm size or sponsorship labels added without support on the page ("small firm", "sponsored").
- Job-posting claims cited to a copy that later disappears. Prefer the employer's own ATS page and record the access date.
- Inferences appended to regulator statements in `risks_and_guardrails`.

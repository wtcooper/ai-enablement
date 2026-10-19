# Verification report: professional-services / billing-collections

Checked 2026-10-19 against sources, all fetched again: 97 YAML sources and the 3 sources that only the module cites.

- Use cases: `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/billing-collections.yaml`
- Module: `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/billing-collections.md`

## Counts

| Action | Entries |
|---|---|
| Kept | 4 (06, 09, 11, 15) |
| Fixed | 13 (01, 02, 03, 04, 05, 07, 08, 10, 12, 13, 14, 16, 17) |
| Rejected | 0 |

## Final grade mix

There are 17 entries: 0 A, 5 B (01, 04, 05, 12, 13), 9 C and 3 D (ideas 08, 14 and 15). No grade changed. Every B rests on a named
deployment whose figures are vendor-published or recalled (for example the Lerners docket time and the Albertsons "almost $2 million"). Under the
2026-10-17 rule none of them reaches A. The only controlled comparison, the Big Four tax division with a random control group, names no firm.

## Fixes and rejections

| Entry / section | Problem found | Fix |
|---|---|---|
| 01 notes; module §5 and §9 | **Statistic reported as something it doesn't measure.** Laurel's 11% is the share of *unsubmitted* time (itself 28% of the workday) that should have been billed. It is not a share of billable work, so it does not "disagree" with the 10-30% and "up to 30%" figures | Reworded as sizing on different bases. The objection in §9 now cites Tonkon Torp's 20 vs 21 minutes (a real conflict on one page) |
| 01, 03, 05, 07, 08 (LAUREL-BILLING-2026); 01 (LAUREL-TIMESHEETS-2026); module §8 | **Wrong date.** 2026-09-17 is a JSON-LD timestamp that every Laurel blog post shares, down to the millisecond. The visible bylines are 2026-08-19 (Billing) and 2026-08-05 (Timesheets) | Dates corrected. Frontier entry moved to 2026-08-19 |
| 01, 02 (LAWSITES-LITIFY-2026) | Date given only as a month, with the note saying two inputs disagreed | Resolved: 2026-05-19 release dateline, posted on LawSites 2026-05-21 (the date now used) |
| 01 (LAUREL-BIGFOURTAX-2026) | Title differed from the page; date was month only | Page title and the 2026-09-01 JSON-LD date used |
| 03 solution | "Staffing rules" listed among the rules extracted from guidelines. Neither Laurel's compliance page nor Intapp's release says this | Replaced with "block billing", which Intapp's release does name |
| 03 solution | Bill corrections feeding back into narrative drafting were credited to Laurel's live compliance feature. The source is the unreleased Billing product | Attributed to Laurel Billing (unreleased) |
| 04 role_evolution | Attributed to "the firm". The quote is a goal stated by the builder, James Phoenix | Reattributed to the builder, as a goal |
| 05 risks | **Claim attributed to the wrong passage.** "The data suggests" is Elite's line about connected revenue operations, not about the cause of rejections. Elite in fact *asserts* the AI cause ("the more likely explanation") without causal data | Reworded |
| 05 notes | The note said the link between Verify and HerculesAI rested only on search results. The Foley article (read in full) says Verify is part of Zero's Hercules.ai platform | Note corrected |
| 07 solution | The "consulting page" claim is a tile on Laurel's home page (LAURELSITE-2026) | Corrected |
| 07 (TRI-MIDSIZE-2026) | Date 2026-07-23 comes from a hidden author field. The page's datePublished and its visible date are 2026-09-24 | Changed to 2026-09-24 (the ref is used only in this file) |
| 08 problem; module §2 and §5 | **Embellished or mis-scoped statistic.** The 43% is partners who *always or usually* reduce a bill when time exceeds their own expectations. The 300 hours and $190,000 are an *average per partner*, not a total | Qualifiers added |
| 10 (ODDR-82CENTS-2026) | 2026-09-09 is the site's "Last Published" HTML comment, not the article's date. The page shows no date | Date set to 2026 with a note in the title |
| 12 solution | Said GHJ had a "firmwide rollout to client-services teams". The page says GHJ piloted with client services, then expanded firmwide | Corrected |
| 13 risks | Legalweek was paraphrased as "clients using AI to cut bills". The source describes clients who demand AI adoption and then use it as leverage to cut fees | Corrected |
| 13 (ONIT-SPEND-2026, MILLIMAN-BILLREVIEW-2026) | Year-only dates and a wrong title for the Milliman page | Page metadata dates used (2026-06-25, 2026-01-20); title corrected |
| 14 risks | Layer3's Clause 4 does not say that clients require "pass-through of efficiency savings". Disclosure is in its summary and Clause 1 | Reworded to Layer3's summary and Clause 4, labelled as a vendor |
| 16 prerequisites | "Timesheet standards" is not in the Kantata article, which speaks of delivery standards | Corrected |
| 17 risks | **Wrong statement in a source note.** "Sample size not stated" for the Blue J/CPA.com poll. The article states 1,000 US accountants, surveyed 12-23 March 2026 | Corrected |
| 17 problem; module §5 | Uku's 15% was called the "single most-cited operational headache". It is the 15% who chose billing as their *biggest* headache; missing deadlines led at 32% | Corrected |
| 17 human_checkpoints | **Unsourced claim given a source.** "Partners review WIP and approve invoices" is not in the Aiwyn article | Restated as an existing step, noting that the source describes no AI checkpoint |
| Module §1 | Said no source publishes an error rate for AI bill checks. Onit publishes vendor accuracy figures (92% and 81%) | Scoped to firm-side checks, with Onit noted |
| Module §5 | Elite's list of the "largest fee-reduction categories" left out the second largest, administrative or clerical work (15.98%) | Added |
| Module §6 | The SRA statement is the Law Society's account of the SRA | Attributed to the Law Society |
| Module §7 | The quotation "approving decisions, not entries" was paraphrased. The page says "Approve decisions, not entries" | Exact wording restored |
| Module §8 | TRI COO & CFO Forum line had no source | Removed |
| Module §9 | A claim that something "is not measured" cited LAUREL-GHJ-2026; "most" in-house teams overstated the survey | Restated as the absence of any source; "nearly 60%" from BLOOMBERGLAW-ACC-2025 |
| Module §9 | "Disclosing AI use invites fee cuts" was a bare assertion with a citation | Now states what the source says (adoption used as leverage) |
| Module §10 | The three keys marked * (AICPA-CODE-2026, ISBA-ELEFANT-2026, EDISCOVERYTODAY-ILTACON-2026) had no URLs | Opened, checked and given URLs and dates |
| Module §3 | Said `#13` "reviews every invoice, not a sample" as a general claim | Reworded: every submitted invoice is audited (Albertsons), and the contrast with sampling is the vendors' |

Checked and found correct: every Laurel customer-story figure (key facts and body text), Foley Mansfield's quotations and its 6% and 50%, Linklaters' figures, Elite's 11% to 18%, 71% and 62 to 50 days (dateline 2026-05-14), the Aderant agent wording and dates, the Albertsons quotations and date (createDate 2026-05-19), the Zscaler clauses (15%, 10%, 60 days, 20%, AI section, revised 2025-04-07), the CA/DC/TX/NC/VA/ABA/Australia/IRS/ICO/EU AI Act/FAR/UTBMS statements and page locators, the TRI Rates figures, Kopka, Legalweek, the Wells Fargo figures via LawFuel, the Clio figures via Oddr, the CollBox pitch, and the Certinia, Kantata, zeb and Perlin/Rapoport abstracts. All 16 cross-referenced ids (acceptance-risk, scoping-pricing, firm-finance and the tax entries) exist, and the tax entries do cover IRS OPR billing. Quotations are all under 25 words. Vocabulary values are valid, and `validate.py` reports 0 errors.

## Sources that could not be reached

None was unreachable. Some needed a second route:
- **Direct fetch blocked (403), mirror worked:** ABA-BLT-2024 and WK-LEGALSPEND-2026.
- **Mirror bot-blocked or 401, direct HTML read:** LEGALIT-FOLEY-2024 and eDiscovery Today.
- **Text taken from the HTML:** CFOTECH-ELITE-2026 and ITBRIEF-KANTATA-2026 came back empty from the mirror.
- **One search-only confirmation:** the CALBAR-GENAI-2026 approval date (2026-05-14). The PDF itself carries no approval date, and its file metadata shows 2026-05-15. A State Bar resources page seen in search results confirms that the Board approved the guidance on 2026-05-14. The access value stays "full" because the text of the guidance was read.

## Targets

| Target | Result |
|---|---|
| 15-25 use cases | Met: 17 |
| At least 50% graded A or B | **Not met: 5 of 17 (29%).** The gap is the evidence base, not the grading. Named firms do not publish measured AI effects on billing, and the newer agent products (Laurel Billing, the Aderant agents, the Oddr agent) are unreleased or in early access |
| Every source dated | Met. Three ISO dates are year-only (LAUREL-SOW-2025, FULCRUM-ILTACON-2026, ODDR-82CENTS-2026) because no page date exists. Undated product pages use the access month |

Open points:
- **Entry 11 maturity:** marked in-production with no named customer (CollBox's claims only). Consider "announced" if the coordinator reads the vocabulary strictly.
- **Entry 12 maturity:** "piloting", while the page says GHJ has expanded firmwide and is rolling out to non-billable staff.

## Patterns of error to fix in the briefs

1. **Site-wide metadata dates were taken as publication dates.** Laurel's blog JSON-LD and Oddr's Webflow "Last Published" comment, plus a hidden author-date field on TRI. Briefs should require the visible byline or dateline and warn that identical timestamps across pages mean metadata, not a publication date.
2. **Survey statistics lost their qualifiers or base.** "Always or usually", "per partner", "biggest headache" and "share of unsubmitted time" were dropped, and different measures were then compared as if they "conflict".
3. **Quoted connective words were attributed to the wrong passage.** Elite's "the data suggests"; Laurel's "approve decisions" paraphrased inside quotation marks.
4. **Process roles were filled from general knowledge** and given a source that does not contain them (Aiwyn's partner checkpoint, "staffing rules", "timesheet standards"). This is the unsourced connective-claim pattern in human_checkpoints and prerequisites.
5. **Statements that "the source does not say X" were themselves wrong** (Blue J's sample size; the link between Verify and HerculesAI). Briefs should require checking the full text before writing that something is absent.
6. **The module's * sources had no URLs.** Briefs should require a URL and date for every source the module cites but the YAML does not.

# Valuation verification report (advisory / valuation, wave 5)

Checked 2026-10-21 against the sources, opened again for this check. Files edited:
`plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/valuation.yaml` and
`.../advisory/modules/valuation.md`. Assurance files were not edited.

## Counts

| Result | Count | Entries |
|---|---|---|
| Kept | 7 | 04, 06, 07, 09, 11, 12, 14 |
| Fixed | 7 | 01, 02, 03, 05, 08, 10, 13 |
| Rejected | 0 | none |
| Added | 1 | 15 (CohnReznick, from a source the deep dive missed) |

**Final grade mix (15 entries):** A 0, B 3 (01, 13, 15), C 9 (02, 03, 04, 05, 08, 09, 10, 12, 14), D 3 (06, 07, 11).
Before the check it was A 0, B 4, C 7, D 3 (14 entries).

## CohnReznick check (flagged by the synthesis report)

The source exists and the assurance entry describes it accurately. CohnReznick's page
(`cohnreznick.com/insights/cohnreznicks-valuation-advisory-enhanced-through-ai-analytics/`) is dated "March 26th, 2026".
It says the Valuation Advisory practice is "incorporating 73 Strings' valuation analytics capabilities into its
established valuation methodologies" and calls the technology "AI-driven, advanced analytics". The release quotes
Claudine Cohen, James Nielsen and Brad Hirsch. CPA Practice Advisor ran the same text on 2026-03-24, two days before the
date on the firm's page. 73 Strings' home page shows CohnReznick among its customer logos.

What follows from it:
- The module's opening claim that "no US top-100 or mid-market accounting firm has described its own valuation AI use"
  was wrong. I replaced it and added `advisory-valuation-15`.
- I graded #15 B and 'in-production': a named firm describes "this implementation" in its own practice, and the vendor
  lists it as a customer. There is no measurement. `assurance-specialists-02` grades the same release C and 'announced'.
  **The two files disagree, and the assurance file should be aligned in the next pass.** I did not edit it.
- I left the firm's size out of the files: the sources do not state CohnReznick's ranking.

## Fixes and rejections

| Item | What was wrong | Fix | Pattern |
|---|---|---|---|
| #01 solution | "ASA Fair Value Conference (New York, May 2026)": the BVWire source gives no month | Now says the panel was reported by BVWire on 2026-06-10 | wrong or missing date |
| #01 outcome and role | "Panellists said" fewer entry-level hires; the source says "several speakers" | Changed to "several speakers" | embellished qualifier |
| #01 prerequisite | Linked KPMG's valuation AI to the firm-wide Claude alliance; the panel report names no tool | States that the panel names no tool and that the alliance is separate | unsourced connective claim |
| #02 role_evolution | "AI efficiency with professional judgment" was cited to the product page; the wording is in the 2026-09-23 tip | Re-cited to BVR-RADATIP-2026 | wrong document |
| #03 grade B→C | Neither Valutico case study (Kreston Reeves, Rouse) says AI was used. The AI claim is only the vendor's branding, so the B rested on a non-AI process | Grade C; the title says "AI use not stated"; the note says what would restore B | grade inflated by an adjacent process |
| #05 risk | Weber: "use of Copilot ... led the court to find the testimony not credible" and "a calculator or spreadsheet would have done the arithmetic". The blog gives no such cause, and the spreadsheet point is the blogger's own view | Now: the court found the testimony not credible, got different numbers when it re-ran his Copilot queries, and required disclosure of AI use | embellished cause; wrong speaker |
| #08 outcome | "Both case studies repeat ... 3-5 times faster": the RXM study does not contain that line | Attributed to the PKF FI study (and Kreston Reeves and Rouse), not RXM | statistic attributed to the wrong document |
| #08 outcome | "PKF FI reports ... 'drastically' reducing the risk of errors": that is the vendor's narrative. The partner's quote says only that it helped him "avoid making mistakes" | Attribution split between the vendor narrative and the partner quote | wrong speaker |
| #08 problem | "take weeks or months": the source says months | Changed to "can take months" | embellished |
| #08 grade B→C | Same issue as #03: the case studies describe "automated" features and never say AI was used | Grade C; title and notes updated | grade inflated by an adjacent process |
| #10 solution | "keeps an audit log" was applied to every form of the template; the release gives the audit log only to the Managed Agents version | Corrected | embellished |
| #13 solution | "and to run scenario analyses across portfolios (S73-HAMLANE-2025)": the Q&A does not say this | Removed; the note explains that simulation is only announced, in the Callisto release | unsupported claim |
| #13 sources | The Q&A cited as "hosted by the vendor" is Hamilton Lane's own insight piece, dated 2025-05-06 and republished by 73 Strings | Added HAMILTONLANE-VALTECH-2025 (firm, 2025-05-06); provenance changed to self-reported | wrong document or provenance |
| #13 notes | Missing conflict: Hamilton Lane took part in 73 Strings' 2025 Series B | Added, sourced to S73-CALLISTO-2026 | missing context |
| Module header | "No US top-100 or mid-market accounting firm ..." was contradicted by the CohnReznick release; counts were "4 of 14 B" | Rewritten: CohnReznick (#15) is the only US accounting firm found; 3 of 15 are B | claim contradicted by another file |
| Module §6 AICPA, §9 | "Standard-setters and practitioners expect no separate AI standards" rests on one practitioner's article (James Ewart) | Attributed to Ewart as a practitioner view | embellished speaker scope |
| Module §6 courts, probe 4, §9 | Weber causation, as in #05 | Reworded to what the blog reports | embellished cause |
| Module §6 courts | Key BVR-HEPPNERCOURT-2026 pointed to the Warner v. Gilbarco article (Heppner is the case it contrasts with) | Key renamed BVR-WARNER-2026, with the case named | wrong document label |
| Module §6 independence, probe 8 | "SEC staff presume ..." | Now "rebuttable presumption"; the FAQ's point that materiality does not overcome it is added | embellished (qualifier dropped) |
| Module §7, §8 | "Big Four panellists said / describe" for a trade-press report | "Speakers at a Big Four panel"; "BVWire reports ..." | attribution |
| Module §8 | IVS consultation start "2026-01" | 2026-01-31, per the IVSC summary | date precision |
| Module §3, §8, §10 | #15 not listed | Added #15 and the new source keys; key list sorted | — |

Everything else checked out against its source. That covers dates on all Anthropic, BVWire, Valutico, Kroll, Stout,
73 Strings, IVSC, ISA, JofA, Intuit, CPA Trendlines, Accounting Today, QoEAgent, PCAOB and US Courts items, plus the
figures 83% / 5 of 7, 64.37%, 73%, n=725 with "three in five", "hours or days, not weeks", "months to days", "a third"
and "$25 billion / 15,000+". It also covers the regulatory statements: Rule 2-01(c)(4)(iii), the PwC FAQ, the IVS
exposure draft items and the 2027-01-31 / 2028-01-31 dates, AO-41's adoption on 2026-04-23, and the withdrawal of Rule
707. All 16 cross-referenced ids in other modules exist and match their descriptions. All quotations are under 25
words.

## Sources that could not be reached, or only in part

- Matter of Weber decision text: law.justia.com and nycourts.gov sit behind a Cloudflare challenge. Only Eric Goldman's
  blog summary was read.
- Paywalled BVR articles, summaries only: BVR-BIG4PANEL-2026, BVR-BIG4GUIDANCE-2026, BVR-POLLS-2025, BVR-POLL-2026,
  BVR-EXPERIMENT-2026, BVR-MONOCULTURE-2026, BVR-TRAINPRACTICAL-2025, BVR-TRAINWORKSNOW-2025 and BVR-TRAINSTAFF-2025.
  They support only the summary-level statements made in the files.
- The AICPA FVS podcast audio was not heard (BVR summary only). The AO-41 full text was not opened (ISA blog quotes
  only). The Forma preprint was read as an abstract only.
- The r.jina.ai mirror refused some requests ("bad IP reputation"). Retrying worked for every page except the court
  decision.

## Targets

| Target | Result |
|---|---|
| 12–20 use cases (validator floor 15) | Met: 15 |
| At least 50% graded A or B | **Not met: 20% (3 of 15).** Before the check it was 29%, and the downgrades of #03 and #08 lowered it further. No measured outcome from a named organization exists for AI-assisted valuation |
| Every source dated | Met. Undated vendor pages carry the access date. AICPA-FVS-2026 (2026-11) and ASA-ASAIC26-2026 (2026-10) carry event dates. The Dealgauge profile date (2026-07-11) is a dateModified |
| Module ≤ 300 lines | Met: 300 |
| validate.py | 0 errors. The expected warning for this file is below the A/B target |

## Error patterns to fix in the briefs

1. **AI branding is not evidence of AI use.** Vendor case studies (Valutico) describe automation under an AI brand. The
   deep dive graded those deployments B as if they were AI deployments. Require the source to say AI was used before a
   B; otherwise cap at C.
2. **Read the overlapping finished files across archetypes before researching.** The CohnReznick release sat in
   `assurance-specialists-02` and was missed, and the module then made a false absence claim. Absence claims ("no US
   firm has ...") should require a check of the other archetypes' files.
3. **Trace a figure to every document it is attributed to.** "Both case studies repeat 3-5x" was true of three Valutico
   studies but not of RXM.
4. **Court holdings via blogs.** Separate what the court found from what the blogger argues, and do not infer a cause
   ("led the court to ...") that the summary does not state.
5. **Find the original publisher of republished content.** The Hamilton Lane Q&A was the firm's own piece, reposted
   by its vendor, in which it also invests. Record both the original and the repost, and any stake the user holds in
   the vendor.
6. **Keep conference and article dates separate.** Trade-press reports of panels give the article date, not the session
   date. Do not add a month that the source does not give.
7. **Source keys should name the right document.** The HEPPNERCOURT key pointed to the Warner case.
8. **Align grades for the same source across archetypes.** CohnReznick is B/in-production here and C/announced in
   `assurance-specialists-02`. The wave should apply one rule to firm press releases that describe their own
   implementation.

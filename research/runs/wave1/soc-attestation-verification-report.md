# Verification report: assurance / soc-attestation

- **Verified:** 2026-10-17 (verifier brief, wave 1)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/soc-attestation.yaml` (16 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/soc-attestation.md` (299 lines)
- **Method:** I extracted all 80 distinct URLs cited in the two files and reopened every one with `curl`, using
  `pdftotext` for the 9 PDFs and the `r.jina.ai` text mirror for pages that blocked curl. I then checked each figure,
  date, attribution and quotation against the page text. I also checked dates against `article:published_time` and
  JSON-LD, the HN item API (Chiaro thread), the Ashby job-board API (Fieldguide and Drata postings) and PDF metadata.
  Two Chiaro method files were read from raw.githubusercontent.com.
- **Validator:** `python3 scripts/validate.py` reports `INFO ... soc-attestation.yaml: 16 use cases, 9 graded A/B (56%)`.
  It gives no ERROR or WARN for either file. The module stays at 299 lines (limit 300). The only ERROR in the run
  belongs to another stream's file (`acceptance-independence.md`, 306 lines), which I did not touch.

## 1. Counts

| | Use cases |
|---|---|
| Kept as written | 1 (`#01`) |
| Fixed | 15 (`#02` to `#16`) |
| Rejected | 0 |

The fixes break down as follows:
- **12 substantive fixes:** wrong figure or slogan, misattribution, unsupported clause, wrong date, ladder value,
  missing figure.
- **3 wording-only fixes** (`#06`, `#09`, `#10`), for testimonial attribution and claims stated more firmly than the
  source.

The module received 22 edits. 2 of them remove build-only references.

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 0 | 0 |
| B | 9 (01, 05, 06, 07, 09, 13, 14, 15, 16) | 9 (unchanged) |
| C | 7 (02, 03, 04, 08, 10, 11, 12) | 7 (unchanged) |
| D | 0 | 0 |

No grade changed. Every B entry has a named organisation and a source that was opened in full. No B entry depends on a
search-only figure. Every vendor figure is labelled vendor-published. Several B entries (01, 09, 16) still rest only
on the organisation's own blog or forum post, which the grade definition allows.

**Ladder after verification:** assist 4, augment 7, automate 3, delegate 2. `#13` moved from automate to assist.
**Change scope (unchanged):** step 9, process 3, model 4.

## 3. Fixes and rejections

### Use cases

| # | Entry | Before | Action | Reason |
|---|---|---|---|---|
| 1 | 02 | Comp AI: audit-ready "in days, not weeks or months" | Fix | That phrase is not on the cited page. The page says "Compliance in days" and "Get SOC 2 audit-ready in weeks"; the outcome now quotes these |
| 2 | 02 | Comp AI "generates policies and assessments mapped to SOC 2 controls" | Fix | The page says the AI learns "your stack, processes, and risk tolerance to generate policies and assessments specific to you". "Mapped to SOC 2 controls" was embellished |
| 3 | 03 | "Linford's summary of the AICPA FAQ says tools 'can't remediate controls for clients'" | Fix | Wrong document and speaker. In the Linford post this is the firm's own experience, in its risks section, not part of the FAQ summary |
| 4 | 04 | SOC 2 "is not a certificate for another framework (JOFA-PODSOC)" | Fix | Pawlicki says SOC 2 is an attestation covering one to five trust services categories and not a certification. The "another framework" gloss was not in the source |
| 5 | 04 | role_evolution: "The inputs expect compliance staff to configure…" | Fix | Unsourced connective claim. Now "Not described in the sources." |
| 6 | 05 | 82% figure described as "reduction in audit preparation time" | Fix | The figure measures something else. The headline is "82% less time spent per audit"; the IDC line refers to prep time generally. Now worded as the page's own metric, with the study unseen |
| 7 | 05 | "'Continuous compliance' is not continuous assurance… (BAKERTILLY-TRUST-2026)" | Fix | Wrong document. That distinction is in Linford's FAQ (LINFORD-ASSURE-2026), not Baker Tilly. Now re-sourced, with LINFORD-ASSURE-2026 added to the entry's sources |
| 8 | 05 | Scrut: scoping error example "human users only when the control applies to service accounts" | Fix | Embellished. Scrut gives three separate failures: a partial-scope integration reported as complete, a broken integration leaving the dashboard green, and access lists missing service accounts. Now stated that way |
| 9 | 05 | role_evolution: exception review "becomes the main manual task" | Fix | Embellished qualifier. Scrut says scoping and exception decisions stay human work |
| 10 | 05 | VANTACON-2026 dated 2026-11-12 | Fix | Wrong date. That is the last day of the event (10–12 Nov). The undated page now carries the access month (2026-10), and the event dates are in the locator |
| 11 | 05 | SACRA-VANTA-2026 dated 2026-04-30 | Fix | The page carries no day. It says "April 2026 update", so the date is now 2026-04 |
| 12 | 06 | Testimonial by "Teleperformance's audit and compliance specialist" | Fix | The page names the person but gives no title. Now "a named Teleperformance employee" |
| 13 | 07 | FIELDGUIDE-WEAVER-2026 dated 2026-05-28 "sitemap last-modified" | Fix | The sitemap has no lastmod for this URL and the page has no date, so the date is now the access month (2026-10). The case study says Weaver "is embedding" agents; the entry's wording was aligned |
| 14 | 08 | "AICPA staff and peer review guidance warn against substituting platform output for the inquiry and testing…" | Fix | Wrong document. This paraphrase comes from the CSA note's summary of JofA, not from JofA. Now quotes JOFA-PRB (firms "leaning too heavily on third-party SOC platforms without… professional judgment") and JOFA-FAST (over-reliance on inquiry) |
| 15 | 08 | Fieldguide director posting used as SOC evidence | Fix | Evidence from an adjacent process. The posting is for financial-audit agents. The entry now says so in its risk and role_evolution |
| 16 | 09 | "Partner review and sign-off remain the control against rubber-stamping" | Fix | Embellished. The post lists missing walkthroughs and missing partner review as signs of a bargain audit |
| 17 | 10 | "EY says AI may invent details, so each drafted answer needs human review" | Fix | Unsourced connective claim. EY makes a general statement about outputs, not about questionnaire answers. Now worded as EY's general point (p.5) |
| 18 | 11 | Vanta chatbot outcome "none published" | Fix | Missing figure. The cited comparison page states "70–87% deflection via Trust Center and AI chatbot". Added, with the note that it is undefined |
| 19 | 11 | role_evolution: "The inputs expect security and sales-engineering teams…" | Fix | Unsourced connective claim. Now "Not described in the sources." |
| 20 | 12 | Problem: "Vendor-risk teams receive hundreds of SOC reports and most are read for an auditor logo and a clean opinion" | Fix | Unsourced. No cited document says this. Replaced with Whistic's actual advice (a report starts a conversation; ask for operational answers) |
| 21 | 12 | "Secondary coverage overstates the alert; the JofA text says identical engagements are judged nonconforming after reviewers examine them" | Fix | Misread. JofA itself says identical engagements "are not performed in accordance with… standards… 'nonconforming'". The tension the sources actually show is that JofA links the alert to the Peer Review Board, while the Reviewer Alert page says its content is not Board-approved. Cybersecify is now cited only for what it says: the alert is not a finding against platforms and does not invalidate issued reports |
| 22 | 13 | ladder: automate | Fix | No source describes AI or automated routing. Buyers choose from a network or bring their own auditor (VANTA-AUDIT-2026). Now assist, with the reason given in the notes |
| 23 | 14 | "TechCrunch did not independently verify the claims" | Fix | Unsupported. No TechCrunch article says this. Replaced with what the sources show: the author is anonymous, no regulator or court finding was found as of 2026-10-17, and the AICPA is "looking into" anonymously published allegations about an unnamed vendor |
| 24 | 14 | Outcome named the audit firm a former Delve customer engaged | Fix | Not needed, and it named an audit firm in the Delve context. That firm is not named in the allegations, but it was removed out of caution. No firm named in the allegations appears anywhere in either file (checked by grep against the firm names in DeepDelver, TechCrunch and SOC2Auditors) |
| 25 | 14 | Notes: "a different restatement gives 533 reports across 455 companies" | Fix | No source given in the entry. The figure traces to a Chiaro page that is not cited there, so it was removed |
| 26 | 15 | "Thoropass staffs its assurance practice with former Big Four and specialist-firm auditors" | Fix | Embellished. The page lists a handful of leaders formerly at KPMG, EY, Accenture and Coalfire. Now says exactly that |
| 27 | 16 | HN title "date derived from '73 days ago'" | Fix | The date is now confirmed: the HN API gives 2026-08-04 16:27 UTC. Added that the HN post is marked "flagged", and that the repository has since grown to 89 controls, 387 attributes and 945 calibration examples |
| 28 | all | last_reviewed 2026-10-16 | Fix | Set to 2026-10-17 |

### Module

| # | Section | Before | Action | Reason |
|---|---|---|---|---|
| M1 | header | "No independent measure of AI quality in SOC work exists" | Fix | Overstated. Now "was found" |
| M2 | §2 | "Generic descriptions are the clearest template tell" | Fix | Embellished. Chiaro says two companies should never share a Section 3 |
| M3 | §3 | CT-12 "drafting of Section 3 (45%)" | Fix | The EY poll option is "Updating Section 3" |
| M4 | §3, §5 | "82% less (audit) prep time" | Fix | Same issue as row 6: the page metric is "less time spent per audit" |
| M5 | §3 | KPMG UK ~18% "on recent SOC 1, SOC 2 and ISAE engagements" | Fix | K-UKCA says "recent engagements" in a controls assurance paper. Now "recent controls assurance engagements", as in §5 |
| M6 | §3 | "ISACA authors report a fabricated document" | Fix | It is one ISACA Now blog author (8 Jun 2026) |
| M7 | §3 | Coverage: "assist 3… automate 4" | Fix | Follows the `#13` ladder change: now assist 4, automate 3 |
| M8 | §5 | "Listed SOC 2 Type 2 fees in a lead-generation directory" | Fix | The directory says most listed prices are "our estimates, not fees paid". Now labelled as estimates |
| M9 | §6 | TQA 9561 bullet: "An auditor using AI stays responsible. Avoid scope inflation" | Fix | Wrong speaker. Both points are Schneider Downs' commentary, not the TQA text (the TQA concerns the service organisation's own use of AI). Now attributed to Schneider Downs |
| M10 | §6 | Ethics staff: terms "threaten independence" | Fix | The source says such terms "can create ethics and independence threats" |
| M11 | §6 | State law: signatories "who sign such reports" | Fix | Pawlicki refers to "fraudulent reports". Restored that qualifier |
| M12 | §6 | ASB exposure drafts "not AI" | Fix | Stated as "the JofA summary does not mention AI" |
| M13 | §7 | Compliance staff "move… to exception queues and 'GRC engineering'" | Fix | Embellished, as in row 9. Now: they keep scoping and exception decisions, and "GRC Engineer" appears as a VantaCon speaker title |
| M14 | §7 | Peer reviewers "do deeper, multi-engagement reviews" | Fix | Multi-engagement comparison applies only when risk is elevated |
| M15 | §7 | "EY sees chief data strategy officers rising" | Fix | EY says organisations "are hiring" them |
| M16 | §8 | Delve "changes its auditor network (3 Apr)" | Fix | Delve said it would rebuild the network. That is a stated intent, not a confirmed change |
| M17 | §8 | VantaCon "2026-11-12" | Fix | The event runs 10–12 Nov 2026 |
| M18 | §9 | "The AICPA stresses most SOC reports are done properly" | Fix | Pawlicki said most service organisations hire credible firms and most firms use technology appropriately |
| M19 | §10 | "the synthesis report maps keys to input refs" | Remove | Build-only reference |
| M20 | §10 | "all opened by the deep dives unless noted" | Fix | Build-only reference. Now "opened and checked on 2026-10-17 unless noted" |
| M21 | header | "Last reviewed 2026-10-16" | Fix | Now 2026-10-17 |

References to controls-testing ids (CT-01 to CT-23) are kept, as allowed. The module contains no research paths, and no
remaining occurrence of "pilot" or "spec".

### Checked and confirmed (examples of what held up)

- KPMG UK (K-UKCA):
  - ~18% and ~15% (DataSnipper)
  - 180+ reports
  - 90% of exceptions on manual controls; 39% on system access
  - 15% of reports qualified, against 20% the year before
  - SOC 2+ opinion over AI governance (Jan 2026)
- EY 2025: 52% of SOC 1 and 40% of SOC 2 deviations were logical access related, across 2,000+ reports.
- EY 2026 poll (multiple selections allowed): evidence collection 63%, updating Section 3 45%, deviation responses 41%,
  project management 29%.
- PCAOB: ~17% of comment forms in 2021 and 2022; the gap-period question.
- State peer review reports: Oregon issued 2026-03-01 and Louisiana 2026-03-03, both showing 0 SOC engagements
  reviewed.
- Standards:
  - XRB ISAE (NZ) 3402 paras 25, 43–44; gazetted 2026-04-09
  - FRC: ISAE 3000 amendments effective 15 Dec 2026
  - JofA: ASB exposure drafts of 26 Feb and 25 Mar 2026, effective 15 Jun 2029 if finalised
  - TQA 9561 dated 11 Sep 2026; DART post 21 Sep 2026
  - KPMG webcast page dated 22 Sep 2026
  - AICPA notice on the unnamed vendor
- JofA articles: all quotes checked (Linton, O'Brien, Mayes, Pawlicki), including the ethics-staff threat list and
  ET 1.230.030.
- Market and vendor figures:
  - Vanta: 4 hours a week, WorkJam 1 hour instead of 7–8, 95% answer acceptance, 35+ frameworks, 100+ firms and
    26,000+ audits, A-LIGN executive's 50% quote
  - $300M ARR (Sacra estimate; Fortune from Vanta) and 16,000+ customers
  - A-LIGN: 15 hours per framework, 30–40% and 25% (testimonial), 6,400 organisations, PCAOB-registered firm, 60%
    benchmark (read from image alt text "cbr 60")
  - Fieldguide: 55%, 90% and 4x (undefined)
  - Weaver: 10–12% realization
- Directory asking prices: $9,000 median; $9,500 for AI companies (middle half $7,000–$13,500); 1-week minimum.
- Delve: every statement is framed as an anonymous allegation that Delve denies, with no regulator finding. TechCrunch
  dates are 21 Mar (original post), 30 Mar ×2, 4 Apr and 23 Apr. Delve blog posts are dated 20 Mar, 24 Mar and 3 Apr.
  DeepDelver is dated 19 Mar.

## 4. Sources that couldn't be reached

All 80 cited URLs were reached, so no source is unreachable. 5 needed another route:
- **chiarohq.com/soc-2/platform-that-includes-the-audit:** TLS reset on direct curl; read through the mirror.
- **Two drata.com pages:** HTTP 403; read through the mirror.
- **github.com/Chiaro-HQ/methodology:** HTTP 403; read through the mirror plus raw method files.
- **verdict.co.uk:** HTTP 403; read through the mirror.

Content behind a free AICPA login was not read. Only the landing pages were opened for:
- TQA 9561
- the software-tools FAQ
- Ethics Staff Insights
- the Reviewer Alert
- the 2017 TSC

Claims about their content rest on Schneider Downs, Deloitte DART, JofA and Linford, and the module says so. The IDC
study behind Vanta's 82% was not available.

**Tally: 80 of 80 cited sources opened (75 directly, 5 through the mirror), 0 unreachable, 5 gated beyond the landing
page.**

## 5. Targets

| Target | Result |
|---|---|
| 15–25 use cases | 16 ✔ |
| At least 50% graded A or B | 9 of 16 = 56% ✔ |
| Every source dated (ISO) | ✔ All YAML sources have a URL and an ISO date. Undated pages carry the access month, stated in the locator |
| Ids unique; vocabulary values | ✔ (validator) |
| Quotations under 25 words | ✔ (all direct quotes are short phrases) |
| Module ≤ 300 lines, no build-only references | ✔ 299 lines |

## 6. Error patterns to fix in the briefs

1. **Secondary paraphrase attributed to the primary.** The "substituting platform output for the inquiry and testing"
   wording came from the CSA note's gloss of JofA, but it was cited to JofA and JOFA-PRB. The "continuous compliance is
   not continuous assurance" line was cited to the wrong firm. Deep-dive briefs should require the supporting sentence
   to be found in the cited document itself.
2. **Slogans and headline metrics restated.** Comp AI's slogan was misquoted. Vanta's "82% less time per audit"
   became "prep time". Briefs should ask for the metric label exactly as printed.
3. **Connective filler in `role_evolution`.** Phrases such as "The inputs expect…" and "becomes the main manual task"
   keep appearing. The synthesis brief should say: if no source describes the role change, write "Not described in the
   sources."
4. **Unsourced scene-setting in `problem`.** One example was "hundreds of reports… read for a logo". The rule that
   every attributed sentence needs a source should cover `problem` as well.
5. **Undated pages given precise dates.** Event end dates, sitemap guesses and "April update" were turned into exact
   days. The brief should require the access month plus a locator note whenever the page has no date.
6. **Adjacent-process evidence.** A financial-audit job posting was used as SOC evidence. Briefs should ask the deep
   dive to tag the process a source actually describes.
7. **Ladder chosen for the business model, not the AI.** `#13` was rated automate although no AI or automation was
   described. The vocabulary note should say that the ladder rates the AI's role, and that a business-model change
   with no AI is at most assist.
8. **Contested cases.** The fixed wording ("allegation; denied; no regulator finding") worked. Add two rules: never
   assert what a newspaper did or did not verify unless the article says it; and do not name audit firms in the
   contested context, even ones not named in the allegations.
9. **Build-only references** such as "synthesis report" and "deep dives" leaked into the module's source section.
   The synthesis brief should list banned phrases.

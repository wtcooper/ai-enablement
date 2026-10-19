# Verification report: professional-services / staffing-resourcing

Checked 2026-10-19 against `use-cases/staffing-resourcing.yaml` (21 entries) and `modules/staffing-resourcing.md`.
I opened all 76 cited URLs: 69 in the YAML and 7 cited only in the module. I also opened 2 extra sources: the ISQM 1
standard PDF and a Revista Mercado article that dates the TR Future of Professionals report. Most pages were fetched
directly. Five pages blocked direct requests and were read in full through the r.jina.ai mirror: BigHand's DLA Piper
press release, Colorado SB26-189, Illinois PA 103-0804, SD Times (Planview) and Wolters Kluwer. I also used the mirror
for JavaScript-rendered pages (Kantata Expertise Agent, NYC AEDT, IAASB). Dates were checked against JSON-LD,
`article:published_time`, the page byline or, for Certinia, the sitemap's last-modified date. One web search was used
to date the TR Future of Professionals report.

## Counts

| Action | Use cases |
|---|---|
| Kept | 7 (#02, #03, #06, #07, #09, #11, #19) |
| Fixed | 14 (#01, #04, #05, #08, #10, #12, #13, #14, #15, #16, #17, #18, #20, #21) |
| Rejected | 0 |

One grade changed: #04 went from B to C. Final grade mix: **A 0, B 5, C 13, D 3** (24% A or B).

- The B grades are #01 and #12 (named deployments, vendor-published) and #13, #14 and #15 (independent randomised
  trials in adjacent settings, capped at B).
- No entry qualifies for A. The DLA Piper "600+ hours" figure is reported by the firm, but the BigHand platform behind
  it is not described as AI.

## Fixes and rejections

| Entry / location | Problem found | Fix |
|---|---|---|
| #01 prerequisite | Said 47% named fragmented data as "the biggest gap". In the study it is the second barrier; limited understanding of where AI applies (49%) is first. A statistic was reported as something it does not measure. | Reworded with both figures. |
| #01 outcome | The "up to 10 hours" claim was "attributed to unnamed lighthouse customers". CPA Practice Advisor, the cited source, does not say this; diginomica does. Wrong document. | Removed the attribution; the outcome now says no customer is named. |
| #01 solution and notes | Said Basware "uses" the staffing agent. The release says Basware "is expanding into" it. Embellished. | Reworded; the notes flag that the agent may not be fully in production. |
| #01 risk; module §9 | Said "client dynamics and personal fit are not captured by any model". Projectworks says no model captures these "yet" and lists internal politics and who works well together. | Quoted the source more closely. |
| #01 human checkpoint | "Resource manager confirms or overrides each recommendation" is not in Kantata or Certinia. Embellished. | Now says the staffing team decides and neither vendor describes autonomous booking. |
| #01, #05, #13; module header, §3, §8 | Called the Peru trial "the one/only randomised test of automated work allocation" and "first randomised evidence". The paper itself cites Bai et al. (2022), a field experiment in which algorithmic assignment raised productivity and was seen as fairer. Overstated. | Narrowed to "the only randomised test of algorithmic assignment of expert work found here". Noted the contrary earlier result. Removed "first". |
| #01 sources | BIGHAND-CONF-2026 was typed "conference". It is a vendor press release, and the conference was the day before (2026-06-04). | Type changed to vendor. Module §8 now dates the conference 2026-06-04. |
| #04 grade | B rested on Hakkoda's undated quote and the figures beside it. Nothing shows the forecasting used AI. This is a grade inflated by an adjacent (non-AI) process. | Downgraded to C, with the reason in the notes. Module §3 updated. |
| #04 risk | "Accelo's CEO says AI amplifies whatever foundation exists…" is the article's narration, not the CEO's words. Wrong speaker. | Split into the write-up's claim and the CEO's actual quote. |
| #04 role_evolution | "Forecasting moves from a quarterly exercise to a weekly one" is not in the source. "Forecasts demand rather than filling open roles" overstated TSIA. | Reworded to the source text. |
| #04 problem | Onrec says a small minority can "accurately" forecast more than 12 months ahead. The qualifier had been dropped. | Restored. |
| #04, #17 (CPAPA-SAAH-2026) | The sponsored article is by a Robert Half executive, a staffing provider with a commercial interest. This was not disclosed. | Named in the source title, the #04 solution and a #17 risk. |
| #05 problem | Unsourced connective claim: "Comparing options across several projects … is hard by hand." | Replaced with Kantata's own pitch ("beyond human capacity"), with a ref. |
| #08 risk | "SPI advises 70–75%+": the line is Deltek's best-practice indicator in its summary of SPI. Wrong speaker. | Attributed to Deltek's summary. |
| #10 solution | The AI-tools register (reliability, limits, oversight) was placed in TSIA's "first maturity level". It belongs to TSIA's "skills genome". "Capabilities" is not listed. | Corrected. |
| #10 risk | "Built hidden applicant scores" misdescribed the Eightfold suit, which alleges "hidden credit reports" and 0–5 rankings. The filing date was missing. | Reworded; filing date 20 January 2026 added. |
| #12 outcome; module §3, §5 | WBD's "10% utilisation increase" was presented as firm-wide. The case-study body places it in the real estate practice group (5% a year). | Scoped to one practice group. |
| #12 role_evolution; module §7 | "Reed Smith created a global director role": the source only names a global director of Smart Resourcing. | Changed "created" to "has". |
| #12 notes; module §3 | Cross-reference talent-learning-04 (rotations into AI teams) does not cover stretch assignments. | Pointed to talent-learning-12 (skill-aware task allocation). |
| #14 risk | Unsourced reviewer caveat in risks_and_guardrails. | Labelled "Reviewer note". |
| #15 notes | The P&G funding disclosure was missing: P&G gave gifts to the HBS institute, and one author consulted for P&G. | Added. |
| #16 | Kantata's Sarah Edwards was called "product chief"; her title is Chief Product Strategy Officer. "Without answers" overstated her post, which calls for frameworks. "Priced" had been dropped from her prediction. | Corrected all three; module §8 updated. |
| #17 solution | "Su calls this 'outsourced leverage'": in the transcript Su says a colleague coined the term. | Attribution corrected. |
| #17, #18 risks | "Supervision and confidentiality duties follow the lawyer wherever the work sits" is a paraphrase not found in ABA 512 Part E. Embellished. | Replaced with what Part E says: supervisory duties, and checking that third parties work capably and protect confidentiality. Gave the CalBar duty its own wording. |
| #20 human checkpoint | "Whether reclaimed time went to rest, development or more work": "rest, development" is not in the TRI column. | Reworded to the column's audit advice. |
| #20 risk | "Rising demand does not show AI saved no time" was an unsourced inference. | Tied it to the columnist's own explanation. |
| #20 solution | SPI's "the leak" was described as hours "not resold or repriced". The page defines it as time saved versus revenue generated. | Reworded. |
| #20 sources | TR-FOP-2026 was dated 2026-09-30, which is not on the page. The report was released 2026-06-22 (Revista Mercado, JSON-LD 2026-06-22; matches TR's release in search results). | Date set to 2026-06-22. |
| #21 risk; module §6 | UK DUAA "commencement was not checked": legislation.gov.uk shows s.80 fully in force from 5 Feb 2026 (S.I. 2026/82). | Commencement added. |
| #21 risk; module §6, §8 | Colorado "duties from 1 January 2027": the bill summary dates only the developer duties. | Specified developer duties; noted the consumer human-review right. |
| #08 sources | CERTINIA-SPIBENCH-2026 was dated year-only, "2026". The sitemap's last-modified date is 2026-08-05. | Date set to 2026-08. |
| Module §6, §10 | ISQM 1 was cited from search summaries only. | Opened the standard PDF. Para. 32(d) requires competence, capabilities and sufficient time. Citation and URL updated. |
| Module §5 | CLOC "(2025, 186 organisations)": this is a 2025 report on a 2024 survey. "Workload and bandwidth" should read "workload and resource bandwidth". | Corrected. |
| Module §7 | COO views were presented as a survey result. They come from roundtable participants. | Attributed to the roundtable. |
| Module §8 | Certinia "adds 14 agents and 135 intelligent actions". In fact it doubled its intelligent actions to 135 in total. | Corrected. |
| Module §9 | The partners objection cited "strategic consensus is hard" as if it were about allocation. The answer credited "law firms" with a single firm's practice. | The 15% COO figure is now stated, and the answer names WBD. |
| Module header | Showed the old grade counts, and the A/B share was missing. | Updated to A 0, B 5, C 13, D 3 (24%). |

## Sources that could not be fully reached

- **Bloomberg Law (McKinsey).** Paywalled; only the opening paragraphs were readable. The entry already relies only on
  those paragraphs. It stays C/announced.
- **SPI Research 2026 AI report.** Only the landing page is open; the revenue share is behind a paywall. The entry uses
  only the landing-page figure.
- **Primary reports cited through summaries.** These were not opened: the Dayshape report (read through Onrec), the
  Kantata/Censuswide SOPSI report (read through Kantata's release), BigHand's "Million Dollar Problem" and Legal Talent
  reports (read through the DLA Piper release and case study), the 2026 Blickstein COO survey (read through Western
  Alliance), the Citi demand data (read through Bloomberg Law), and the Berkeley HBR study (read through TRI). Each
  figure is attributed to the summary that was read.
- **Illinois PA 103-0804.** The page gives no approval date, so the source keeps its effective date (2026-01-01), as
  the title states.

## Module targets

- **Use cases:** 21 (target 15–25). Met.
- **A/B share:** 5 of 21, 24% (target 50% or more). **Not met.** No named firm publishes a measured AI staffing
  result. The named law-firm figures come from a platform that is not described as AI, and the randomised evidence is
  from adjacent settings.
- **Dates:** every source has a URL and an ISO date. Ids are unique. `validate.py` reports 0 errors; its one warning
  for this module is the A/B share.
- **Cross-references:** all 13 exist. assurance-planning-risk-assessment-22, assurance-quality-management-11 and
  delivery-management-01, -04, -05, -07, -14 and -16 match their topics. talent-learning-11, -12, -19 and -20 also match.
  One mismatch (talent-learning-04) was fixed.
- **Quotations:** all under 25 words.

## Error patterns to fix in the briefs

1. **Ranks and superlatives.** A second-placed survey item was reported as "the biggest gap", and "the only/first
   randomised test" was claimed without checking the paper's own literature review. Briefs should require the rank,
   and should say "the only one found" rather than "the only one".
2. **Narration attributed to a speaker.** Vendor write-ups mix narrative with quotes; the Accelo article and the Deltek
   summary of SPI are examples. Attribute a claim to a person only when it sits inside quotation marks.
3. **Scope lost from case-study figures.** Headline tiles (WBD's 10%) drop the practice-group scope given in the body.
   Briefs should require reading the body text behind every tile figure.
4. **Grade B from a non-AI deployment.** A named customer of a PSA product (Hakkoda) was used for an AI use case without
   evidence that the feature used was AI. Check that the deployment is of the AI capability itself.
5. **Commercial interest of authors.** Sponsored content from a staffing provider and study funding by the deploying
   company were not disclosed. Briefs should ask for the author's employer and the funding.
6. **Legal status left unchecked.** "Commencement not checked" and "duties from" were left vague when the statute page
   gives the answer. Check the commencement notes on legislation.gov.uk and the dated sections of bill summaries.
7. **Paraphrased rules presented as the rule.** "Duties follow the lawyer wherever the work sits" and "SPI advises" are
   examples. Quote or closely paraphrase the regulatory or benchmark text and give its locator.
8. **Dates for undated pages.** The read date or a republish timestamp was used as the publication date (TR-FOP). Check
   press coverage or the sitemap's last-modified date before using a year-only date. **Cross-file conflict for the
   coordinator:** TR-FOP-2026 is dated "2026" in 12 files, "2026-07-21" in 5, "2026-09" in 2, and is now "2026-06-22"
   here. The release date confirmed here is 2026-06-22.

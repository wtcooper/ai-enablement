# Verification report: security / operations

Checked on 2026-10-17 against the cited sources. These files were edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/operations.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/operations.md`

Every cited source key was opened: the YAML keys, plus the 18 keys listed only in module §10. That is 108 distinct
URLs. Most were read directly with curl. The CISA (3), SEC and Sophos pages were blocked, so they were read through
`r.jina.ai`. The CyberProof, OMB, NDSS and two arXiv PDFs were read in full with `pdftotext`. Posting dates for the
Greenhouse jobs were checked against the Greenhouse boards API.

Every figure in the YAML outcomes and in module §5 was checked against the source text. `scripts/validate.py`
reports 0 errors: 24 use cases, 20 graded A or B (83%).

## Counts

| Action | Entries | Ids |
|---|---|---|
| Kept | 6 | 02, 08, 09, 15, 18, 19 |
| Fixed | 18 | 01, 03, 04, 05, 06, 07, 10, 11, 12, 13, 14, 16, 17, 20, 21, 22, 23, 24 |
| Rejected | 0 | none |

## Final grade mix

| Grade | Count | Ids |
|---|---|---|
| A | 6 | 01, 02, 09, 12, 15, 21 |
| B | 14 | 03, 04, 05, 07, 08, 10, 11, 13, 14, 16, 17, 18, 22, 23 |
| C | 3 | 06, 19, 20 |
| D | 1 | 24 (labelled "Idea") |

**Grade A rule.** Each A entry rests on a figure the named organisation reports as measured:

- Elastic's dashboard metric: AI verdict versus analyst close reason, 60% to 92% (#01, #21).
- Figma's 20% drop in pages "from this change alone" (#02) and its 71% cut in time to resolution (#09).
- Microsoft's difference-in-differences study on Defender telemetry (#12).
- Amazon's figures over four months: 336% faster rule production and 67% fewer false positives (#15).

The #12 figure is vendor-authored and observational, and it is flagged that way in the YAML. Figures that customers
state in vendor case studies stay in B entries, labelled with their provenance: ECS, Zapier, Mysten Labs and
CyberProof.

## Fixes and rejections

| Id / section | Change | Reason |
|---|---|---|
| #01 | The no-tools guardrail now says Elastic claims injection resistance for the Pattern Finder only. The PromptArmor product is named as the default Elastic AI Agent | Elastic says this of the Pattern Finder, not of the Summarizer (embellished) |
| #03 | "Short baselines and unmanaged devices" re-sourced to SPLUNK-RSACSOC-2026. role_evolution reworded to what .conf26 shows, and the context-assembly shift sourced to SPLUNK-BHUSA-2026. The Google limit wording was tightened | Wrong document: the Cisco .conf26 post says "noisy, temporary, highly dynamic". It also does not say Tier 1 stopped gathering context |
| #04 | The "demonstrated measurable improvements" quote re-sourced to MSFT-DEFENDER-AGENTS-2026. "Reject or reclassify the verdict" changed to "see reasoning, give feedback" | Wrong document. The page describes feedback on the classification, not reclassification |
| #05 | Removed "a missing AI comment is treated as a signal to look". The risk line "no case study reports a false-negative rate" is corrected. The CyberProof locator now points to the PDF pages | Zapier's quote says only that an uncommented alert reminds him of past toil (misread). CyberProof does claim "no false negatives" over 90 days without a sample size, so the old line contradicted the source. The PDF was opened directly |
| #06 | ARXIV-2512.08169 date changed from 2025-12-08 to 2025-12-09. The AIDR 68% is relabelled as token reduction from distilling the dataset. The VIP checkpoint is attributed to Swimlane's author | The arXiv submission date is 9 Dec 2025. The 68% measures dataset compression, not reasoning versus chain-of-thought. The VIP point is one author's opinion, not survey data (a statistic reported as something it doesn't measure) |
| #07, #21 | ARXIV-2610.10608 date changed from 2026-10 to 2026-10-07. A dating note was added to the Grow Therapy locator | arXiv shows the submission date. The Grow Therapy page carries no date; DEW #167 linked it on 2026-08-19 |
| #10 | The accuracy pairing was corrected. role_evolution now cites the vendor blog for the 94%, limited to AI-assisted participants | The vendor blog's 68%→97% and 63%→85% do not match CSA's per-scenario 22%/29%. The 94% is not on the CSA landing page, and it covers only those who used the tool (wrong document) |
| #11 | Problem changed from "first months" to "first hours on shift" (Cisco Live) and "months to ramp up" (Prophet) | Embellished. Cisco Live says "first hours" |
| #12 | BAKERDONELSON-IBM-2026 date changed from 2026 to 2026-07-30 | Byline date |
| #13 | "Pan-American Life says reporting arrives automatically" changed to "CrowdStrike says" | The line is CrowdStrike's own heading, not a customer quote (wrong speaker) |
| #14 | The paging point is now attributed to a practitioner summarised in tl;dr sec. Hugging Face's alerting change is cited separately | Hugging Face's disclosure does not say its sensors failed to page anyone (wrong speaker) |
| #16 | The "run but can't see" list now names DEW summarising a practitioner post, with an inline ref. SPLUNK-BHUSA-2026 was added to sources | The note cited a key that was missing from the entry's sources (format) |
| #17 | "Saved the most time" changed to Figma's words, "surprised us most, in terms of how much time it saves". The checkpoint "human approves and merges" changed to "draft PRs for human review; agent answers reviewer comments" | Embellished qualifier. Approval and merge are not stated |
| #20 | The in/on/out-of-the-loop sentence re-sourced to NCSC-AGENTICRISK-2026 | That taxonomy is in the interim agent blog, not in "One does not simply defend agentically" (wrong document) |
| #22 | **Grade C changed to B.** EXPEL-RUXIE-2026 was added | Expel and Arctic Wolf run named production MDR services, and Expel's page says Ruxie closes benign alerts. No measured outcome with a method is published, so A is not reached |
| #23 | D3-SOCHIRING-2026 type changed from job-posting to vendor. The Forrester line was rewritten | D3 is a vendor analysing postings. Forrester does not define the "five-year problem"; the old wording joined two separate points |
| #24 | "Podcast guests said" changed to "the hosts of The Register's podcast". The problem statement now has sources (DEW #169, Hugging Face), and HUGGINGFACE-INCIDENT-2026 was added | Wrong speaker. The "no usage policy" phrase is Hugging Face's, and it had no ref in this entry |
| Module §2 | "Context spread over 20+ tabs" changed to "many tabs, side notes and copied tables" | The source says "many tabs open". The 20+ was invented |
| Module §5 | Note on the SIABench row: the figures were confirmed in the paper's tables | It had previously been read only second-hand |
| Module §6, §10 | SIFMA: "(search-only)" removed. The ask is now stated precisely: rescind Item 106 and Form 8-K Item 1.05 | The letter was opened (2026-04-10). "Asked for rescission" was vague |
| Module §7 | The Tier 1 shift is re-sourced (conf26 plus Splunk BHUSA). The Forrester "five-year problem" is restated | Wrong document. The unsourced connective claim placed the phrase in a junior-pipeline context the source does not give |
| Module §8 | "First joint government guidance" changed to "CISA and ASD's ACSC publish joint guidance". The date "2026-10-06/07" changed to 2026-10-07 | "First" is unsupported. Both preprints were submitted on 7 Oct 2026 |
| Module §9 | "SACR counts close to 140 vendors" changed to "SACR cites peer trackers counting close to 140" | SACR attributes the count to peer trackers (wrong speaker) |

**Confirmed without change:** every other figure in module §5, including these:

- IBM's USD 4.99M and USD 1.93M, read on IBM's page.
- OMB M-26-14's 70% and 95% alert-coverage levels.
- The logging-plan deadline of 2026-11-18, read in CISA's press release and on the LRA page dated 2026-08-20.
- The CISA, NIST and NSA practices of 2026-10-16. CISA's pages do now read "Super Intelligence (SI)".
- MITRE ATT&CK v20, released 2026-10-13, with "Impair Autonomous Defenses" and prompt-injection techniques.
- The AI Act's 2027-12-02 high-risk date.
- NCSC's eight risks and its five-factor score.

## Sources that couldn't be reached

None remain unreached.

- These pages blocked direct curl requests and were read through `r.jina.ai`, with content confirmed:
  - CISA-AGENTIC-2026
  - CISA-LOGGING-2026, plus the LRA page for its date
  - CISA-KEYPRACTICES-2026
  - SEC-CYBER-2023
  - SOPHOS-MDR-2026
- The IBM report page returned its key figures to direct curl. The mirror was blocked for ibm.com.
- archive.org reset every connection, so it was not usable.

## Module targets

| Target | Result |
|---|---|
| 15–25 use cases | 24, met |
| At least 50% graded A or B | 20 of 24 (83%), met |
| Every source dated | Met. Undated pages carry a retrieval or modified date, and the locator says so (Sophos, EIOPA, eSentire, Expel Ruxie, Grow Therapy) |
| Values from vocabulary; unique ids; URL and date on every source | Met (validator: 0 errors) |
| Quotations under 25 words | Met |

## Patterns of error to fix in the briefs

1. **Attributed to the wrong document or speaker.** This was the most common error, with 9 cases:
   - #03, #04, #13, #14, #20, #24
   - Module §7, §9
   - The CSA 94%

   Briefs should ask researchers to check that the quoted words appear in the cited URL itself, and to say whether a
   line is the vendor's heading or a customer's quote.
2. **Embellished qualifiers.** Examples: "20+ tabs", "first months", "saved the most time", "first joint guidance",
   "reject or reclassify". The brief should ask for the source's own words when a qualifier carries the claim.
3. **Statistic reported as something it doesn't measure.** AIDR's 68% is dataset compression. The VIP checkpoint was
   presented as survey data. The CSA per-scenario accuracy pairs were mismatched.
4. **Internal contradictions.** One risk line said "no case study reports a false-negative rate" while CyberProof's
   case study claims one. Cross-check negative claims against the entry's own sources.
5. **Dates.** Day-precision dates were available but missing (arXiv submission dates, a law-firm byline). Use the arXiv
   "Submitted on" line and the article byline.
6. **Source type.** A vendor's analysis of job postings was typed as job-posting.
7. **Grades.** No A grade was inflated by an adjacent process. #15 (RuleForge) sits next to vulnerability-exposure
   but measures detection-rule production, which is in scope. No search-only source supports an A or B entry. One
   entry (#22) was under-graded.

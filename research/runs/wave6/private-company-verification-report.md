# Verification report: assurance / private-company

Checked 2026-10-21 against the vocabulary and the 2026-10-17 grade A rule.

- Use cases: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/use-cases/private-company.yaml`
- Module: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/modules/private-company.md`

All 84 cited sources were opened: 64 in the use cases plus 20 cited only in the module. One source was added
(TR-PLANTEMORAN-2025). Five sources were blocked by the r.jina.ai mirror's IP limit and were fetched directly instead.
Going Concern returned 403 to direct fetch and was read through the mirror.

## Counts

| Action | Count | Entries |
|---|---|---|
| Kept | 5 | 03, 05, 11, 15, 19 |
| Fixed | 15 | 01, 02, 04, 06, 07, 08, 09, 10, 12, 13, 14, 16, 17, 18, 20 |
| Rejected | 0 | none |

Every entry's organisation, change to the work and figures are supported by an opened source. Most fixes are wording,
attribution, date or locator corrections. No grade changed.

## Final grade mix

| Grade | Count | Entries |
|---|---|---|
| A | 0 | none |
| B | 9 | 01, 02, 05, 06, 09, 10, 11, 13, 14 |
| C | 9 | 03, 04, 07, 08, 12, 15, 16, 17, 18 |
| D | 2 | 19, 20 (both labelled "Idea") |

I considered raising entries to A or B and decided against it:

- **#10 stays B.** The Plante Moran 91% comes from the firm's own internal pilot survey. It measures perceived speed and
  is published only by the vendor, so it is not a figure the firm reports as measured.
- **#09 stays B.** The Beever and Struthers figures come from an independent study, but they are staff perceptions and
  only the press report was read.
- **#04 stays C.** The gtap and EisnerAI items are announcements.
- **#17 stays C.** The firms adopted the PCR platform, but the sources do not describe what AI does inside SSARS work.

## Fixes and rejections

| Entry / section | Fix | Reason (error pattern) |
|---|---|---|
| #01 role_evolution | The "first-year auditor" claim is now attributed to Caseware's release narrative, not to Withum | Wrong speaker: it is release text, not a Withum quote |
| #01 human_checkpoints | "Accept, refine or override" now applies to the Disclosure Checklist Agent; added that Caseware says every Verity output is reviewable before it enters the file | Overstated scope: the release says this about that one agent |
| #01 problem | "Cannot build and certify" changed to "few build" | Unsourced, absolute qualifier |
| #01, 06, 07, 08, 12, 13, 18 locators | CPACOM-ATR-2025 page numbers made consistent (PDF pages, with printed page where needed) | The locators mixed printed and PDF page numbers |
| #02 solution, risks, role_evolution | The "more than a year", "huge" and standardisation-benefit statements are now attributed to the Journal of Accountancy article, not to Kanter. The role claim is limited to what the article says | Wrong speaker; unsourced connective claim in role_evolution |
| #02 problem | Supkis Cheek's title corrected to senior vice president of AI, analytics and assurance | Wrong title |
| #04 risks | "Both firms stress professionals supervise every step" changed: only Grant Thornton says it, and the EisnerAmper coverage gives no supervision design | Claim attributed to the wrong document |
| #04 locator | Austin quote located in the full article HTML (the mirror copy was cut off by a registration wall) | Locator |
| #06 solution, notes | Austin's title taken from the release. BPM's Top 100 status now sourced (rank 33, ATODAY-TOP100-2026) | Unsourced firm-type claim |
| #08 risks | "CPA.com and the AICPA, which also sell DAS services" replaced with a sourced statement: the AICPA, CPA.com and Caseware built DAS, and CPA.com is its implementation partner. Source added | Unsourced connective claim in risks |
| #08 role_evolution | Labelled as a recommendation | Unsourced statement presented as fact |
| #09 | 53% now reads "draft emails or refine written material". Source type changed from academic to press (The Accountant article). Notes say the figures are perceptions | Statistic reported more broadly than measured; wrong source type |
| #10 | Added TR-PLANTEMORAN-2025 (2025-11-20), which holds the anonymous internal survey, the 140+ participants and the security-protocol details that TR-SCALING-2026 does not contain. "Plante Moran says" changed to "the vendor says". Dropped "3,800+ professionals" and "reusable prompt templates", which the cited page does not support | Claims attributed to the wrong document; unsupported detail |
| #12 problem | "Firms furthest along said access was their biggest obstacle" changed to "firms further along were more likely to name..." | Embellished: overstates a comparative finding |
| #13 risks | Removed "a CalCPA author cites AU-C 500". The article discusses information produced by the entity but does not name AU-C 500 | Claim attributed to the wrong document |
| #13 source date | CALCPA-AISTD-2026 dated 2026-08-12 from the byline (was "2026") | Missing date |
| #13 role_evolution | Labelled as an inference. The podcast remark is restated as what the host said: automation over offshoring, not "reduce outsourced audit support" | Unsourced connective claim; embellished paraphrase |
| #14 | TR-SAMBROWN-2026 dated 2026-05-11 from page metadata (was "2026"). role_evolution separated: the junior-staff change comes from a tax-advisory tool, not the sampling tool | Missing date; grade drawn on an adjacent process |
| #16 problem | "Now rivals" changed to "can feel as if it rivals", matching the AICPA column | Embellished qualifier |
| #16 role_evolution | "Reviewers move from locating gaps to clearing flagged ones [CASEWARE-LAUNCH-2026]" replaced with what the release says: managers get cross-file checks and review packs, partners see sign-off readiness. Added that no firm has described a change | Unsourced connective claim in role_evolution |
| #17 | The "14 of 482" label now says compilations and preparations, with a note that the Missouri figure covers compilations only. The JofA claim is now attributed to the CPA.com report it cites, not to "practitioner discussion" | Statistic reported as something it does not measure; claim attributed to the wrong document |
| #18 | "Small firms say ... without raising fees" is now attributed to the vendor's case study. The FERF citation for "engagement partner owns the conversation" replaced with FERF's actual advice. role_evolution restated from the source. FEIDAILY-FERF-2026 dated 2026-04-14, DATASNIPPER-PERRY-2025 dated 2025-09-19, and TR-SOTP-2026 date relaxed to 2026-06 because 06-09 could not be confirmed | Wrong speaker; citation to a document that does not say it; wrong or unconfirmed dates |
| #20 locator | The point is in the summary's third and final sentences, not the second | Locator |
| Module §2 | Fieldwork "over-auditing to satisfy reviewers" restated as the source has it. QM "rivals" softened. Disclosure checklist size scoped to one vendor's methodology | Embellished cause and qualifier |
| Module §5 | Compilation rows relabelled to include preparations, with the Missouri note. The CPA.com 50% claim no longer says "some firms report", because the report names no firms | Statistic reported as something it does not measure |
| Module §6 | Partner duty restated as "understand tools, confirm firm-approved and used correctly" (was "approve tools") | Embellished |
| Module §7 | Managing-partner bullet no longer says the partner "must explain AI risk to a peer reviewer"; the source does not mention AI. CPAPA-STOP paraphrase corrected. Reviewer bullet marked as a hypothesis. Non-traditional hires restated | Claims attributed to the wrong document; unsourced connective claims |
| Module §8 | AIUC item: "a new service line for mid-market firms" changed to a hedged possibility. Disclosure Review scoped to its customers | Embellished |
| Module §9 | JOFA-PEER warning scoped to SOC 2 platforms. ICAS "time saved" objection restated with the actual figures | Embellished qualifier |
| Module §10 | ICAEW-MIDTIER-2026 dated 2026-05-22; AICPA-APQ-2026 dated 2026-06-30 | Missing exact dates |

The module was trimmed to 299 lines to meet the validator's 300-line limit.

## Sources that could not be fully reached

None are wholly unreachable. These are limited:

- **ICAS-AMBS-2025:** only The Accountant's article was read; the ICAS report was not opened. This is already noted, and the grade is capped at B.
- **CPAFMA-WINSOME-2026:** a blog summary only; the CPAFMA report was not opened. This is noted in #07.
- **ICPAS-PRAF-2026:** the slides sit behind a login. Only the catalogue summary was read, which supports the "AI and automation among emerging areas" claim.
- **EISNER-AUDITAGENT-2026:** partly behind a registration wall in the mirror copy. The full text, including the Austin quote, is in the direct HTML.
- **GRF-ENGAGE-2026:** only the session abstract was read. Its publication date (2025-11-17) was confirmed from JSON-LD.
- **NYSSCPA-PEERDEF-2026:** the listing page now shows a December 2026 session; the 2026-08-12 date comes from the URL.
- **Undated vendor pages kept at year level:** DataSnipper FGMK and Aprio (2026), Caseware DAS PCR (2026). Page metadata gave no reliable publication date.

## Targets

| Target | Result |
|---|---|
| 15–25 use cases | Met (20) |
| At least 50% graded A or B | **Not met: 9 of 20 (45%).** No honest upgrade was available. The module's outcome evidence is vendor-published, and the platform entries are announcements |
| Every source dated | Met: every source has a URL and an ISO date. Three vendor pages are dated to the year only |
| Values from the vocabulary, unique ids | Met (validator clean for these files) |
| Quotations under 25 words | Met |
| Cross-references name existing entries | Met: all 41 `assurance-…` ids resolve, and each fits the topic it is cited for |

## Error patterns to fix in the briefs

1. **Vendor release narrative attributed to the firm.** In Caseware and Thomson Reuters releases, the vendor's own
   sentences sit next to firm quotes, and researchers credited both to the firm (#01, #10, #18). Briefs should say: "only
   text inside quotation marks is the firm's; everything else is the vendor's."
2. **Citing the hub article for details found in a linked case study** (#10). Require the locator to quote the sentence
   that holds each figure.
3. **A paraphrase that names a standard the source does not name** (#13, AU-C 500). Ban adding standard numbers that do
   not appear in the source.
4. **Comparative survey findings turned into absolutes** (#12 "furthest along said"; module "some firms report").
5. **Softened source language hardened** ("can feel like it rivals" became "rivals"; "most firms have yet to"
   became "no model").
6. **role_evolution filled with plausible connective claims carrying a vendor citation** (#02, #16, module §7). Require
   either a quote-backed source or an explicit "inference" or "recommendation" label.
7. **Mixed page-numbering schemes** for the same PDF. Specify PDF page numbers.
8. **Year-only dates** where the page metadata has a full date (publishDate or JSON-LD). Tell researchers to check page
   metadata before falling back to the year.
9. **Peer-review tables summed across states with different row definitions.** Require the row label to be checked in
   each report before summing.

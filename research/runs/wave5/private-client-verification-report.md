# Verification report: advisory / private-client

Checked 2026-10-21. Files: `advisory/use-cases/private-client.yaml` (17 entries) and `advisory/modules/private-client.md`.
I opened every cited source with curl or the r.jina.ai mirror. I read the PDFs (UBS, Citi, SEC, IRS, Northern Trust
template, IESBA) with pdftotext. I used two web searches, one for the blocked PKF release and one for the Holland &
Knight piece.

## Counts

| Action | Count | Entries |
|---|---|---|
| Kept | 4 | 05, 06*, 11, 17 |
| Fixed | 13 | 01, 02, 03, 04, 07, 08, 09, 10, 12, 13, 14, 15, 16 |
| Rejected | 0 | none |

*#06 needed only a one-line wording change to its unsourced `problem`, so it is counted as kept.

## Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 0 | 0 |
| B | 5 | 6 (02, 05, 06, 08, 16, 17) |
| C | 9 | 8 (01, 03, 04, 07, 09, 10, 14, 15) |
| D | 3 | 3 (11, 12, 13) |

## Fixes and rejections

| Entry / section | What changed | Reason |
|---|---|---|
| #16 | Rewritten. The office is now named: Minot's Light Management, whose CEO Joshua S. Miller used enterprise Copilot on five years of monthly P&L statements. Figure: about 45 minutes against "hours". Grade C to B, maturity emerging to in-production, ladder augment to assist. Checkpoint added: he edited and spot-checked the numbers | The entry called this "an unnamed office, as relayed by a Wingspan director". Wingspan's page only summarises the FOPro article, and FOPro names the office and the CEO. The figure is a practitioner's estimate, so it stays B under the grade A rule |
| #01 | Title and solution reworded. PKF "plans to leverage" the platform and support clients' evaluation and implementation; automated inter-company reconciliation is now attributed to the vendor. Source URL moved to the firm's own copy of the release | The entry said "A CPA firm adopts ... with automated intercompany reconciliation", and the module said PKF "plans to run family-office accounting". The release supports neither, and the automation claim comes from Asseta's site. Business Wire returned 403 |
| #01 role_evolution | The "experienced advisory support" quote is now tied to family offices' challenges | The release does not say the platform needs advisory support. It says the challenges need "both modern technology and experienced advisory support" |
| #02 | Reference added to an unsourced risk line. Note added that the Masttro case page shows no date | Missing source ref. The date "2026" is the year accessed, and the case itself is behind a form |
| #03 | RBC measure now gives n=155. Armanino descriptor "mid-market and top-tier advisory firm; rank not verified" replaced | The release states the sample size. The descriptor was unsupported |
| #04 | Stanford description now includes "faster month-end closing". Job posting date set to 2026-10-12 | Abstract wording. The Greenhouse `published_at` is 2026-10-12 |
| #07 | Gallagher date 2026-09 changed to 2026-09-25 | Date on the page |
| #08 | Human checkpoint replaced with the president's actual quote; review step marked "not described". Note added that Aspen has run for two years | "Fiduciary professionals remain the advisers" was an embellished paraphrase |
| #09 | Role and risk lines now separate the CEO ("accelerate and augment") from the head of engineering ("not to replace advisors"; outputs sourced back to records) | Claim attributed to the wrong speaker |
| #10 | Kaufman line split: Quent says clients want a real human, and the firm's commentary says AI frees time. The Hubbis speaker is identified as Eton Solutions' president, a vendor. Armanino locator corrected | The firm's text was attributed to the speaker. The panel speaker's vendor role was not disclosed. The cited section was a call to action |
| #12 | AFS risk reworded | AFS says an estate plan can reveal inconsistent treatment of family members, not "succession documents" |
| #13 | EPI date changed from 2026 to 2026-01-20; note corrected | The page states "Tuesday, January 20, 2026". The note had said the date was unclear |
| #14 | Northern Trust template date changed from 2026 to 2026-08 | PDF creation date 2026-08-19 |
| #15 | "Concentration risk" replaced with "dependence on external AI systems". PKF wording corrected. CIO article dated 2026-08-03 | Squire never says concentration risk; its only "concentration" refers to wealth. Date taken from JSON-LD |
| Module header and §3 | Counts updated to 6 B, 8 C, 3 D. #01 and #16 reworded to match | Consistency with the YAML |
| Module §2 | Unsourced "little legal support" removed. "Per a panel speaker" changed to "per a Hubbis panel write-up" | Unsourced connective claim. The sentence is the article's framing of the panel |
| Module §4 probe 9 | AFS wording corrected | Same misattribution as #12 |
| Module §5 | RBC n=155 added. Row added for the Minot's Light estimate | Sample size is in the release. New B evidence |
| Module §6 | Contingent-fee wording now notes the rule's exceptions. PCAOB Rule 3523 stated correctly. The AICPA independence point is attributed to a JofA article by Ethics Division staff | "Any contingent fee" overstated the rule. "List tax services" was vague. The source is a JofA staff article, not an AICPA pronouncement |
| Module §7 | Kaufman and Compound lines split by speaker. The morale claim is attributed to a vendor president. #16 added as an example | Wrong speaker and an undisclosed vendor role |
| Module §8 | Asseta seed dated 2025-11-18 (reported 2025-11-20). Holland & Knight item rewritten from the Family Wealth Report republication, which I read in full | The release date was Nov 18. The HK item had been marked search-only |
| Module §9 | "Concentration risk" removed. The 70%/95% figure is no longer attributed to "the speaker" | Not in source. The article does not say who cited the figure |
| Module §10 | HK-PRINCIPALS-2026 now points to the readable Family Wealth Report copy | The firm URL returns 404 |

## Sources that could not be reached directly

- **PKF-ASSETA-2026 (Business Wire):** returned 403. I read the firm's own copy at pkfod.com in full; the AI Journal
  syndication matches it. The YAML URL now points to pkfod.com.
- **HK-PRINCIPALS-2026 (hklaw.com):** returned 404. I read the Family Wealth Report republication in full. The date
  2026-04-20 comes from the HK URL and a search result.
- **Masttro case study:** the body is behind a form, so I checked only the summary bullets. The page shows no date.
- **ARMANINO, PWC, PCAOB:** the direct fetch returned 403, but the r.jina.ai mirror worked.
- **SEC exam PDF:** rate-limited at first, then read in full.
- **Not re-read:** the underlying Campden/AlTi, Deloitte and WealthManagement.com reports that Armanino and Gallagher
  cite. The entries already flag them as unread.

## Targets

- **12–20 use cases:** met (17).
- **At least 50% graded A or B:** **not met.** 6 of 17 is 35%. No source reports a measured outcome from a named
  organization. Raising the share would need new named deployments, not regrading.
- **Every source dated:** met. Three sources still carry year-only dates: Masttro, Northern Trust article and Hubbis.
  None of those pages shows a publication date.
- **Cross-references:** all 21 cited ids in other modules exist and match their descriptions.
- **Validator:** the private-client files pass. A line-limit error for this module (302 lines) was fixed by trimming
  to 300. The validator still shows a WARN for the A/B share. `client-accounting-services.md` (308 lines) also fails
  but is not in scope.

## Error patterns to fix in the briefs

1. **Trusting a summary over the original.** Wingspan summarised FOPro and dropped the office's name, which cost #16
   a grade. Briefs should require tracing a summary back to the article it summarises.
2. **Merging two sources into one claim.** The PKF release and the Asseta site were blended, so the firm appeared to
   claim the vendor's automation. Attribute each clause to one source.
3. **Mixing speaker quotes with publisher commentary.** Kaufman and Compound lines blended the speaker's words with
   the publisher's. Quote only the named speaker's words.
4. **Not disclosing vendor speakers.** The Hubbis and Wiss forum speakers are vendor executives. Say so whenever a
   practitioner quote comes from a vendor.
5. **Dropping dates and sample sizes that are on the page.** EPI's webinar date, RBC's sample size, and the dates
   for CIO, Gallagher and the job posting were all available. Check JSON-LD, `published_at` and event-detail blocks.
6. **Embellished paraphrase.** Examples: "concentration risk", "fiduciary professionals remain the advisers",
   "any contingent fee", "succession documents". Paraphrase no more broadly than the source wording.
7. **Treating "blocked" as "search-only".** Both blocked sources had readable mirrors: the firm's own copy and a
   republication. Try those before downgrading.

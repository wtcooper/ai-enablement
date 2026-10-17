# Verification report: tax / compliance-individual-business

- **Verified:** 2026-10-17 (verifier brief `verify-compliance-individual-business.md`, wave 2)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/use-cases/compliance-individual-business.yaml` (25 entries, 83 distinct sources)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/compliance-individual-business.md` (300 lines)
- **Method:** I extracted all 89 URLs (83 in the YAML and 6 more in module §10) and reopened every one with `curl` in a private
  working folder. I used `pdftotext` for the PDFs (Werfel appendices, Form 8867 instructions, Publications 1345, 4557 and 5708,
  Rev. Proc. 2013-14, the Swider paper and the full TaxCalcBench paper). For the 403, paywalled or bot-checked pages I used the
  `r.jina.ai` mirror (OpenAI, Wolters Kluwer Scan, GAO, TPB, eCFR, my-cpe, Podscan and TaxGPT) and the raw GitHub README for
  TaxCalcBench. Each figure, date, attribution and quotation was checked against the page text, and each date against
  `article:published_time`, JSON-LD, the on-page byline or the PDF revision line. One web search was used, to find a mirror of
  the blocked Wolters Kluwer release.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. For this module it gives `INFO ... 25 use cases, 10 graded A/B
  (40%)` and the expected WARN that the A/B share is below 50%. The module first went over the 300-line limit after the edits;
  I condensed it back to 300 lines. The other warnings belong to other streams' files.

## 1. Counts

| | Use cases |
|---|---|
| Kept as written | 9 (`#03`, `#07`, `#11`, `#14`, `#15`, `#16`, `#21`, `#22`, `#25`) |
| Fixed | 16 (`#01`, `#02`, `#04`, `#05`, `#06`, `#08`, `#09`, `#10`, `#12`, `#13`, `#17`, `#18`, `#19`, `#20`, `#23`, `#24`) |
| Rejected | 0 |

The 16 fixed entries break down as follows:
- **9 substantive fixes:** `#05`, `#06`, `#08`, `#12`, `#13`, `#18`, `#19`, `#20` and `#24`. These were misattributions, a
  statistic used for something it does not measure, claims no longer on the cited page, unsupported connective claims and
  embellished regulatory readings.
- **7 wording, date or locator fixes:** `#01`, `#02`, `#04`, `#09`, `#10`, `#17` and `#23`.

No entry was rejected. Every source exists and was reached, directly or by another route (§4). The core claim of every entry
holds once corrected.

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 1 (`#05`) | 1 (`#05`) |
| B | 9 (02, 03, 04, 06, 11, 12, 14, 20, 24) | 9 (unchanged) |
| C | 12 | 12 |
| D | 3 (10, 13, 22) | 3 |

- **`#05` stays at A, on a narrower basis.** It previously rested on "Boulay; the Crete pilot". The Boulay figure is a partner's
  estimate ("maybe 15 or 20 hours") in a testimonial on Basis's own site, and that alone would not support A. The A now rests
  only on the Crete pilot. OpenAI's post names the organisation (Crete's network of 30+ firms), gives the volume (7,000 1040 and
  1041 returns) and describes how accuracy was measured: the share of returns reaching 75%, 90% or 100% correct field completion
  against the filed return. The post is vendor-published. OpenAI co-developed the tool with Thrive Holdings, Crete's owner, and
  RuntimeWire reports that OpenAI holds a stake in Thrive. The notes now say all of this and call it the thinnest possible A. The
  Armanino figures I added (60% fewer prep hours) are vendor-page statistics without method, so they support the deployment, not
  the grade.
- **`#06` stays at B.** Accrual's partnership page now names the Armanino staff it quotes and shows statistics: 86.5% of draft
  values matched the final return, and an estimated 50% reduction in effort. These are vendor-page figures with no method. I
  treated them the same way as in `#05`: I added them as outcomes but did not use them to raise the grade.
- **`#01` stays at C.** The Accrual quote it cited is not anonymous. It is from Josh Karls, an Armanino tax manager, but the page
  does not say that the collection step uses AI.
- No A or B entry uses a search-only source. Every source is `access: full`.

**Ladder (unchanged):** assist 5, augment 9, automate 5, delegate 6. **Change scope (unchanged):** step 9, process 12, model 4.

## 3. Fixes and rejections

### Use cases

| # | Entry | Before | Action | Reason |
|---|---|---|---|---|
| 1 | 01 | role_evolution: CPA Practice Advisor "says preparers spend less time chasing documents" | Fix | Not in the article. It says preparers stop being interrupted to read the job board aloud once status messages run. Reworded |
| 2 | 01 | "An anonymous Accrual customer quote says document collection was the biggest win" | Fix | The quote is attributed to Josh Karls, Tax Manager, Armanino. Named, and the entry notes the page does not say the step uses AI |
| 3 | 01, 17 | APARIPRO-2026 dated 2026-06-17 | Fix | The page's modified time is now 2026-09-11 |
| 4 | 01, 10 | COLUMBIA-TAXBENCH-2026 dated 2026 | Fix | The page says "Updated July 2026"; changed to 2026-07 |
| 5 | 02, 12, 20 | PwC interview publisher "CFO Dive (Informa TechTarget)" | Fix | `og:site_name` is CFO.com (Informa TechTarget); the URL is cfo.com |
| 6 | 04 | WCG saw TR's own environment "as a structural problem for firms on other tax engines" | Fix | Embellished. WCG says it "creates problems" and then describes the reset risk of proprietary platforms. Reworded to that |
| 7 | 05 | OpenAI tax agents "piloted by more than 30 Crete firms on 7,000 returns" | Fix | Misreported. Crete is a network of 30+ firms, and the 7,000 returns came from "the Crete firms that participated", a number the post does not give |
| 8 | 05 | Crete outcome `measures` "as summarised by the tax-data-technology deep dive… definitions not restated" | Fix | Source reopened. Accuracy is now defined (correct field completion against the filed return; 25%→86% of returns at the 75% threshold), and the co-developer and ownership tie are disclosed |
| 9 | 05 | Boulay testimonial attributed to "Kevin Elli" | Fix | The visible page says Kevin Ellis; "Elli" is a typo in the JSON-LD. The JSON-LD also lists the "50% efficiency" quote under Wiss, while the tax page lists it under Boulay |
| 10 | 05 | "some firm leaders worried that returns prepared at a higher level of abstraction might differ from prior-year returns" | Fix | Inverted. It was the firms' own past returns that were prepared at "a higher level of abstraction"; the worry was that the AI's more precise output would create a "noticeable delta" |
| 11 | 05 | Prerequisite "OPR expects third-party tools to be vetted", cited to item 4 | Fix | Wrong part of the document. Vendor vetting appears in OPR's best-practices recap, not in the section 10.36 item. Locator corrected |
| 12 | 05 | OPENAI-CODEX-2026 dated "2026" | Fix | Page undated. Dated 2026-08 from RuntimeWire's 2026-08-20 report, which cites it. Armanino outcome and ACCRUAL-INDIV-2026 source added |
| 13 | 06 | Armanino partnership quotes "not attributed to a person" | Fix | The page names them: Rouvier, Onuoha, Richardson, Dabu and Mesko. Its Armanino statistics added as a vendor-published outcome |
| 14 | 06 | Summit recap: entity preparation "(1120-S among them)"; "names data quality as the biggest barrier"; "lists AI-native firms and a shift from compliance to advisory as themes" | Fix | Not in the episode description, the only part that can be read; the transcript needs sign-in. All three removed. Date sharpened to 2026-06-17 |
| 15 | 08 | "WCG tried a browser-based approach from one of the five vendors (not named in the text read)"; note "The WCG post does not name TaxGPT" | Fix | Wrong. WCG names TaxGPT, under a heading the earlier text extraction dropped, as the pixel-recognition vendor and "the least prepared of these five" |
| 16 | 08 | Title "one agent per return"; product page "names Axcess, UltraTax, Drake and ProConnect"; "90% reduction… within 60 days" and "25-person firm… 28% more capacity" | Fix | None of these is on the cited page now. It claims 50% less first-pass time. Removed and the title rewritten. The 90% figure survives only as a platform claim in the launch release |
| 17 | 08 | "Launch coverage repeats vendor claims of 45 minutes saved per 1040" | Fix | The release says TaxGPT "projects" 45 minutes for an illustrative 20-person firm with 2,000 returns. It is a projection, not a measurement |
| 18 | 09 | Sam Leon podcast "show notes only" | Fix | Podscan returns 403. Confirmed through the mirror (episode introduction) and the CastFox listing ("review remains the bottleneck"). Locator updated |
| 19 | 10 | Note "In the 2025 edition one tax year 2025 case was excluded" | Fix | Garbled. It is the tax year 2025 edition, and the best row covers 49 of 50 cases |
| 20 | 12 | role_evolution: "Accrual testimonials describe reviewing a workbook rather than building one (ACCRUAL-INDIV-2026)" | Fix | Wrong document. The quote is Patrick Richardson's (Armanino) on the partnership page. ACCRUAL-PARTNER-2026 added to the entry |
| 21 | 13 | "OPR's best practices include documenting AI usage and verification processes" | Fix | Not in the best-practices list. OPR's item 4 says firm procedures must be "documented to show adherence to section 10.36". Reworded |
| 22 | 13 | role_evolution: "Werfel warns of a hollowing out of experienced staff" | Fix | Embellished. Risk 15 says experienced preparers may retire or leave earlier as AI reduces demand for their expertise, taking tacit knowledge with them |
| 23 | 18 | Outcome: consultant says clients see >90% time savings and >5x ROI (Black Ore) | Fix | A statistic used for something it does not measure. It is a product claim, not evidence about phased adoption. Replaced with "none published" and moved to the notes |
| 24 | 18 | Checkpoint "Partner reviews the difference between the AI draft and the filed prior-year return" | Fix | Embellished. A podcast host suggests running a prior-year return through the tool to see what it would have done. Reworded |
| 25 | 18 | "the article says the framework is not a standard" | Fix | Not in the article. It calls the framework "a starting point" and says the views are the author's, not AICPA policy |
| 26 | 18 | Close benchmark "(accounting, vendor-run)"; "participants sometimes overrode a correct AI answer" | Fix | The study was run by Mercor, an AI data company, and the override happened in one session. Reworded |
| 27 | 18 | Note: routing "described for an unnamed firm" | Fix | It is a podcast host's advice (Brian Tankersley), not a firm's practice |
| 28 | 19 | OPR 10.36 policies cover "vetting of outsourced or third-party tools" | Fix | Vetting is in the best-practices recap, not the 10.36 list. Separated |
| 29 | 19 | "Where client data goes into a model that retains or trains on it… (item 6)" | Fix | Embellished. OPR speaks of data "uploaded to unsecured or public systems" and of using "secure, enterprise-approved AI" |
| 30 | 19 | Prerequisite "A named principal accountable for AI use (JOFA-POLICY-2026)" | Fix | The article recommends "an AI lead or committee". Reworded |
| 31 | 19 | "At the April 2026 TEI Tax Technology Seminar" | Fix | The recap gives no month. "April" removed |
| 32 | 19 | WK-FRA-2025 | Fix | wolterskluwer.com blocks automated fetch. The same Business Wire release was read on dutchnews.nl and supports 25%, 84% vs 44% and 2,300+ participants. Locator notes the route |
| 33 | 20 | "OPR ties section 10.36 to… vetting of third-party tools" | Fix | Same misreading as row 28 |
| 34 | 23 | "two commentators expect the main labour effect on outsourced and offshore services" | Fix | Only one host, Tankersley, says it. Reworded |
| 35 | 24 | role_evolution: summit recap "lists AI-native firms and private equity… as themes" | Fix | Not in the episode description. Claim and source removed; role sentence re-sourced to TechCrunch |

### Module

| # | Section | Before | Action | Reason |
|---|---|---|---|---|
| 1 | Header | A "rests on vendor-published figures about named firms" | Fix | Now says it rests on the single Crete pilot, published by its co-developer |
| 2 | §2 table | "Importing data is the lowest-rated software attribute (3.4 of 5)" | Fix | The survey says disaffection was greatest for importing data *and* integration, and gives no integration average. Reworded; the K-1 OCR claim now cites WK-AXCESSSCAN-2026 |
| 3 | §2 context | 300,000 departures and the 17-year low given without their time frames | Fix | Added "in two years" and "2022", as the source states |
| 4 | §3 | "automate and delegate rest on vendor claims" | Fix | Wrong for `#02`, `#03` and `#14`, which are B entries on named deployments. Now: every automate and delegate *figure* is vendor-published or company-reported |
| 5 | §3, §5 | `#08` "one agent per return"; "TaxGPT 90% less first-pass time and 45 minutes per 1040" | Fix | Same as rows 15-17 above |
| 6 | §5 | Crete pilot line | Fix | Accuracy definition and co-developer added. Armanino vendor-page figures added, labelled as having no method |
| 7 | §6 | 10.36 procedures include "vendor vetting" | Fix | Same as row 28 above |
| 8 | §7 | "an anonymous Juno customer says…" | Fix | The quote is from Yehuda Tenenbaum, Y10 Tax Solutions. "start at review" now cites BASIS-TAX-2026 |
| 9 | §8 | Summit dated "2026-06"; Arc "2026-09-22"; Basis end-to-end "Undated" | Fix | Summit recap is 2026-06-17. Arc was unveiled 2026-09-09 and reported 09-22. The Basis page shows 2026-08-05; it is now placed in date order |
| 10 | §10 | BASIS-E2E-2026 "(undated)"; JUNO "customer quotes" | Fix | Dated 2026-08-05 (page date); "named customer quotes" |

The other module statements checked out against their sources: the OPR alert's text, the 7216 regulations (no retroactive
consent, the SSN-abroad rule, software developers counting as preparers), Rev. Proc. 2013-14 penalties, Form 8867 ($650 and
$2,600 for 2026), the Publication 5708 FTC elements (500-person, 30-day breach report), *Clinco*, PCRT, HMRC, TPB, the AICPA
survey figures (1,808 respondents; 65%, 32%, 16% vs 24.3%, 41.2%, 93%), the Thomson Reuters Future of Professionals figures, the
Wolters Kluwer figures, TaxCalcBench (32.35%, 51.96%, 0-71.43%, 40.00%), GAO, H&R Block, WCG pricing, and the Werfel thresholds
(including the 1%-in-30-days suspension in Appendix D).

## 4. Sources that couldn't be reached directly

None is unreachable. Every source was read directly or by another route:

| Source | Direct fetch | Route used |
|---|---|---|
| OPENAI-CODEX-2026 | 403 | r.jina.ai mirror (full text) |
| WK-FRA-2025 | 403 / bot check (also via the mirror and Wayback) | Same Business Wire release on dutchnews.nl |
| WK-AXCESSSCAN-2026, GAO-14467T-2014, TPB-GS55-2026, TREAS-7216-2008, TREAS-C230-2014 | 403 | r.jina.ai mirror |
| ACCTPOD-SAMLEON-2026 | 403 | Mirror (first part of the transcript) and the CastFox episode listing |
| COLUMN-TCBREPO-2026 | 403 on github.com HTML | raw.githubusercontent.com README |
| MYCPE-BLACKORE-2026, MYCPE-TAXGPT-2026 | Paywalled body | Mirror for Black Ore; summary paragraph only for TaxGPT |
| CPATL-WORKFORCE-2026, CPATL-SEASON-2026 | Gated | Teaser paragraphs only (as already disclosed) |
| BLACKORE-SUMMIT-2026, CPAPA-AILIAB-2026 | Transcript needs sign-in | Episode description only. Claims beyond the description were removed |

**Pages that changed since synthesis.** Three cited pages now differ from what the researchers read:
- TaxGPT's product page has dropped the claims cited, and they were removed.
- Accrual's 1040 and partnership pages now show named Armanino quotes and statistics, which were added.
- ApariPro's modified date has moved to 2026-09-11.

## 5. Targets

| Target | Result |
|---|---|
| 15-25 use cases | Met (25) |
| At least 50% graded A or B | **Not met:** 10 of 25 (40%). No honest upgrade was available. The only candidate evidence is vendor-page statistics (Accrual, Black Ore, Basis) without method |
| Every source dated | Met. Every source has a URL and an ISO date. Undated vendor pages carry the retrieval date and say so in the locator |
| Ids unique; vocabulary values | Met (validator: 0 errors) |
| Quotations under 25 words | Met |

## 6. Error patterns to fix in the briefs

1. **Text extraction that drops headings creates false attributions.** WCG names TaxGPT in an `<h3>` that the researcher's parse
   lost, which produced an explicit and wrong note: "WCG does not name TaxGPT". Accrual's customer names sit in separate elements
   and were reported as "anonymous" (three times, across `#01`, `#06` and the module's Juno line). Briefs should require
   checking the raw HTML before writing "not named" or "anonymous".
2. **Vendor pages drift.** TaxGPT's figures vanished, and Accrual's pages gained named quotes and statistics. Briefs should
   require a quote of the exact sentence and a retrieval date for every vendor-page figure, and say that undated vendor pages
   need re-checking at synthesis time.
3. **Stretching a podcast description.** Three entries attributed themes, barriers or form types to a summit recap whose only
   readable text is a two-sentence description. When only a description is readable, cite only what it says.
4. **Reading OPR's best-practices recap into the section 10.36 item.** "Vendor vetting" was placed under 10.36 in three entries
   and in the module. Briefs should ask for item-level locators for regulatory claims, and for those locators to be checked.
5. **Misreported pilot scope.** "More than 30 Crete firms piloted" came from "Crete's network of 30+ firms". The figure was
   passed through a second deep dive without the primary source being reopened. Briefs should forbid "as summarised by another
   deep dive" figures in A or B entries.
6. **Product claims used as outcomes for a governance entry.** A Black Ore time-saving claim was the outcome of the "phased
   adoption" entry (`#18`). Outcomes must measure the entry's own change, or say "none published".
7. **Inverted or embellished readings of quotes.** Examples: the prior-year "delta" concern, "partner reviews the difference",
   "hollowing out", "two commentators", "retains or trains", and "a named principal". Briefs should require the source sentence
   to be pasted into `locator` for every risk and role statement.
8. **Grade A on vendor testimonials.** The Boulay estimate on Basis's site was half of `#05`'s A. Briefs should state that an
   estimate in a vendor testimonial ("maybe", "could") is not a measured outcome, and that vendor-page statistics without
   method do not raise a grade.

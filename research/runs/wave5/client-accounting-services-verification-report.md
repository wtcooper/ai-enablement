# Verification report: advisory / client-accounting-services

Checked 2026-10-21 against the opened sources. Files edited in place:
`plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/client-accounting-services.yaml`
and `.../advisory/modules/client-accounting-services.md`. `scripts/validate.py`: 0 errors. No warnings for these
files. The module is 299 lines (limit 300).

Method: all 99 source URLs in the YAML were fetched with curl and read as text (pdftotext for PDFs). Pages blocked or
rendered by JavaScript were read through the r.jina.ai mirror. Job-board dates came from the Greenhouse and Ashby APIs.
The four module-only sources in §10 were also fetched. Each claim, figure, speaker and date was checked against the
text, including bylines, `article:published_time` and JSON-LD dates. Cross-references to other modules were checked
against the ids that exist.

## Counts

| Action | Entries |
|---|---|
| Kept (no substantive change) | 6 (`08`, `11`, `12`, `13`, `15`, `23`) |
| Fixed | 18 (`01`-`07`, `09`, `10`, `14`, `16`-`22`, `24`) |
| Rejected | 0 |

No entry needed rejecting. Every cited source exists and was opened, except ABA Formal Opinion 512, which was already
marked search-only and cited only in a C entry. Most fixes are wording, attribution and dates. None changed what a
use case is.

## Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 1 (`01`) | 1 |
| B | 11 | 11 |
| C | 10 | 10 |
| D | 2 (`21`, `24`) | 2 |
| A/B share | 50% | 50% |

**`01` stays A.** The figures are measured, by named researchers (Choi and Xie, Stanford GSB and MIT Sloan), from
platform data on 79 SMEs. This follows the precedent in professional-services-work-production, where an independent
field trial of unnamed firms was graded A. The limits are stated in the entry: the platform is unnamed, the findings
are associations, and only abstracts were read.

**B entries.** Each was re-tested against the 2026-10-17 rule. All of them carry estimates or vendor figures labelled
with their provenance, and none was graded A.

**`02` stays B.** It now names Hiline, whose manager is quoted by Digits. Before this check the B rested on an
unnamed FloQast firm and an adjacent enterprise team (Brex).

**`06` stays B.** Its title was narrowed to "AI-assisted live dashboards, variance explanations ...". No named firm
reports AI-drafted commentary, so B rests on named AI-assisted reporting.

No grade was raised to meet the target.

## Targets

| Target | Result |
|---|---|
| 15-25 use cases | Met (24) |
| At least 50% graded A or B | Met (12 of 24, exactly 50%). Any justified downgrade would put the module below target. |
| Every source dated | Met. Year or year-month only: `PILOT-PARTNERHUB-2026` (2026, undated page), `COSO-GENAI-2026`, `FLOQAST-CASCASE-2026`, `JOFA-NONATTEST-2016`, `HEPLER-CPALIAB-2026`, `NBER-GENAIWORK-2023`, `ZUELLIG-AIPOLICY-2026`, `WOODARD-ENGLETTERS-2025`, `STANFORD-JAR-2026`. Access dates are used for the undated `ARCLOW-SITE-2026`, `OPENAI-BASIS-2026` and eCFR pages, and the locators say so. |
| Ids unique, vocabulary values, quotes under 25 words | Met (24 unique ids; validator clean; no quotation of 25 words or more) |
| Cross-references exist | Met. All 25 cited ids exist, including the shorthand `-07`, `-12`, `-16` and `-22` forms. |

## Fixes and rejections

| Entry | Fix | Reason |
|---|---|---|
| 01 | Speed outcome `source_ref` changed from `ACCTODAY-AIBENCH-2026` to `DIGITS-BENCH-2026`. Human time is still attributed to Accounting Today. | The 40 ms and 74 s figures are in Digits' report, not in the Accounting Today article (wrong document). |
| 01 | "Seven best one-shot configurations were within 0.4 points of each other" replaced with "six models behind the best finished within half a point; best one-shot beat humans by at most 0.4 points". | 0.4 points is the margin over the human baseline, not the spread between models (a statistic reported as something it doesn't measure). |
| 01 | Lincoln measure changed from "as estimated by the co-owner" to "as stated ('approximately 90%') in a vendor case study". | The case study states the figure itself and does not attribute it to the owner. |
| 01 | Role evolution: unsourced sentence removed ("staff move from keying categories to ... conventions"). The sourced finding on low-confidence intervention was added. | Unsourced connective claim. |
| 01 | `STANFORD-INSIGHTS-2025` date changed from 2025-06 to 2025-06-26. The note about conflicting dates was removed. | The byline reads June 26, 2025. June 9 belongs to a related-article card. |
| 01 | Notes: the "66.0% top score in a 2026-03-03 blog" figure was removed. The 77.3% (March) and 79.2% (CFO.com, now cited and added as a source) figures are sourced. Added that Intuit's uncertain items go to the business owner. | The 66.0% figure was unsourced. The owner point corrects an implied accountant review. |
| 02 | Role evolution split by source. Heather Taylor (Hiline) named as the "flipped my role" speaker. Notes say grade B rests on Hiline's named use, and that Armanino's digital workers are RPA. | Before, the quote went to "a Digits customer" and the FloQast and Digits claims were merged. A named deployment was available in the source. |
| 03 | Mercor outcome: "12 junior CPAs" changed to "12 licensed CPAs averaging about 5.5 years' experience (Mercor calls them junior)". | The label overstated how junior the participants were. Mercor gives average experience of about 5.5 years. |
| 03 | Prerequisite: "CohnReznick says it waited three years for this" changed to "turned to AI after three years building its CAS practice, saying it now had the core tech stack and clients". | Embellished. The podcast does not say it waited. |
| 03 | Penrose prerequisite reworded to what the benchmark shows. Basis role claim tied to the Intelligence Architect posting ("You write the procedures and skills"). Pilot PM posting identified by id and first-publish date. | The claims held, but the support sat in a second posting that the locator did not name. |
| 04 | Problem: "read-only AI cannot change the books" replaced with the source's points (about 7 hours by hand; pop-ups and passwords do not stop agents). Role evolution reduced to what Digits says. Arclow checkpoint changed to "works and confirms every close". | Unsourced connective claim, and wording drifted from the source. |
| 05 | Risk "automated delivery assumes the numbers were reviewed first" replaced. The owner says he can "completely leave the bookkeeping duties to the system" and reviews when needed. The checkpoint "owner reviews closed books before release" changed to "not described". "Mid-month" YTD changed to "at any point in the month". | An unsourced claim was attributed to the source and described a review gate that the source contradicts. Also an embellished detail. |
| 05 | The caveat attributed to the vendor ("may not transfer to a mid-market team (DIGITS-ELEV8-2026)") was restated as a fact about the evidence. | Attributed to the wrong document: the vendor does not say this. |
| 06 | Title narrowed (see above). Solution separates the JofA tool guidance from named use. The risk "An AI's explanation of a variance is a hypothesis ... (ACCTODAY-CASKEYS-2026)" was replaced with Bourke's actual words. The Bonadio speaker is now his outsourced accounting role. Aprio "AI-enabled workflows" changed to "AI-enabled delivery methodologies". | Unsourced connective claim attributed to Withum. The grade was resting on an adjacent practice (AI-assisted reporting, not drafted commentary). |
| 07 | Armanino: "analyses it with machine learning" removed. "'a lot of traction'" replaced with the article's "has proven very popular with clients". The RPA risk was corrected. Aprio role: "with AI-enabled templates" changed to the posting's separate duties. | Embellished. Neither "machine learning" nor "traction" is in the 2024 article, and the Aprio posting does not say AI builds the models. |
| 09 | Problem: "migration is often the biggest obstacle" re-cited from `JOFA-CASAI-2026` to `CPAPA-ELEV8-2026`. FloQast added as the source for unprofitable cleanups. The JofA locator was fixed. | Attributed to the wrong document: the JofA article does not say this. |
| 09 | Risk "cleanup output still needs review for write-offs" changed to "AI identified the write-offs; who approved them is not stated". Botkeeper gap: "left firms to migrate" changed to "many firms migrated during the roughly three weeks". Role evolution: "reposition toward advisory pricing" removed, and the BST point restated as the source gives it. | Embellished wording and unsourced connective claims. |
| 10 | AFP "49% faster fraud reporting" changed to "49% more efficient fraud reporting", with sample size and timing added (465 practitioners, January 2026). | A statistic reported as something it doesn't measure: the survey says "enhanced efficiency in fraud reporting". |
| 14 | Role evolution: "shows the in-house controllership role taking on workflow-builder tasks" changed to what the source says (built in Power Automate). Jira named. | Unsourced connective claim. |
| 16 | Pilot's December 2025 "minimal human intervention" wording added. The speaker relabelled from "a practitioner" to the head of an AI consultancy (Edgefield Group). Uku locator notes the page was revised. | Wrong speaker type. The Uku page was published 2026-02-13 but carries events and a status check from September 2026. |
| 17 | "In select cities with nationwide expansion planned" changed to "nationwide", with sales enablement and matching by specialty and location added. "In limbo for weeks" made concrete (closure announced 9 Feb; about three weeks until Xendoo bought it). `PILOT-PARTNERHUB-2026` date changed from 2026-04 to 2026. | Embellished: the release says "nationwide" and does not mention select cities. The 2026-04 date had no basis (the page is undated and its latest entry is 11 Feb 2026). |
| 18 | Problem rewritten to what CLA says. Removed: "no way to encode its own judgment" and "most mid-market firms cannot fund their own platform". Digits' Firm Model offering named as the base. | Embellished claims attributed to the source. |
| 19 | Problem: "per-seat or per-client pricing makes firms pay for potential" replaced with the Digits CEO's and adviser's statements. | Embellished: per-seat pricing is not mentioned in the source. |
| 20, 22 | `KARBON-SOAI-2026` date changed from 2026-01-20 to 2026-01-23. "Karbon users over-represented" removed. | JSON-LD `datePublished` is 2026-01-23. The over-representation claim was not in the source. |
| 21 | KPMG note: "a figure KPMG uses for two different measures" changed to "the KPMG survey was not opened, so the figure is not used". | Unsourced claim. |
| 22 | TR figure "34%" changed to "about one-third", with sample size (1,800) added. Problem: "staff paste client data into consumer chat tools" replaced with the TR finding. HeplerBroom risk reworded to the white paper's due-care point. | The release gives "one-third", not a percentage (an embellished figure). The other two claims were unsourced or drifted from the source. |
| 24 | Crowe: "KKR-backed advisory arm" changed to the release's structure (Crowe LLP attest; Crowe Advisory LLC non-attest). PEEC: an interim October meeting was agreed. NONATTEST: "firms that required" changed to "a firm whose billing system required". | The release does not say which entity KKR invested in. The 2016 article describes one firm. |
| All | `last_reviewed` set to 2026-10-21. Header reworded so it no longer describes the build process. | Housekeeping. |
| Module | §2: migration-obstacle key changed from `JOFA-CASAI-2026` to `CPAPA-ELEV8-2026` and FloQast. The reporting pain now cites JofA (late commentary) and TFMA (static PDFs). | Attributed to the wrong document. "Late static PDFs" was not in Withum's talk. |
| Module | Context: "Accounting Today's 2026 Top 100" changed to "a recent Accounting Today survey of Top 100 Firms". Withum "CAS practice reached $70M" changed to an advisory practice built on CAS with "$70 million in revenue in the space". "Bonadio's CAS leader" changed to "outsourced accounting leader". | Wrong attribution and an overstated qualifier. Bourke's $70M refers to advisory and CAS together, and is ambiguous. |
| Module | §3 `#06` line matches the new title. `#02` notes Hiline. §5: Mercor participants described as averaging 5.5 years' experience. §7: Hiline named; Bonadio quote attributed to its practice; "AI-enabled templates" changed to "AI-enabled methods"; Pilot role changed to "public-accounting experience". | Same reasons as the YAML fixes. The Pilot posting asks for audit, tax or CAS experience, not CAS specifically. |
| Module | §8: "KKR's investment in its non-attest arm" changed to the release's two-entity structure. BlackLine "agents" removed. | Overstated. |
| Module | §9: "Botkeeper closed" changed to "announced closure ... Xendoo revived it". "A practitioner" changed to "an AI consultant". Removed: the unsourced "most CAS clients are not audit clients" and the unsourced "under fixed fees the firm keeps the gain until renegotiation". | Unsourced connective claims and a wrong speaker type. |

## Sources that could not be reached directly

All 99 YAML URLs and 4 module-only URLs were read. Some needed another route:

- **Read through the r.jina.ai mirror** (403 or a JavaScript shell when fetched directly): `OPENAI-BASIS-2026`,
  `CROWE-KKR-2026`, `PENROSE-ACCTBENCH-2025`, `SEC-RULE2-01-2026` and `FTC-SAFEGUARDS-2026` (eCFR),
  `BEANCOUNT-REVIEWBURDEN-2026`, `PILOT-PARTNERHUB-2026`, `PILOT-JOBS-2026` and `BASIS-JOBS-2026`. Posting dates
  were confirmed through the Greenhouse and Ashby public APIs.
- **`IESBA-TECHREV-2023`:** the URL is a landing page. The paragraphs cited (114.3 A3, R601.5, 601.5 A2, 606.3 A1)
  were checked in the linked IFAC pronouncement PDF, updated 30 May 2023.
- **`ABA-FO512-2024`:** 403 directly and through the mirror. It stays search-only, cited only as quoted in
  `JOFA-DISCLOSE-2025` (whose quotation was confirmed), in a C entry.
- **`COSO-GENAI-2026`:** read from a third-party copy (auditoresinternos.es), as already noted. The page numbers
  cited (13, 14, 24) match that PDF.
- **`STANFORD-JAR-2026`:** abstract only (the Wiley full text was not attempted), as already noted.

## Patterns of error to fix in the briefs

1. **Figure moved to the wrong document.** Accounting Today's benchmark article and Digits' own report were treated
   as one source, and "biggest obstacle" was credited to the JofA instead of CPA Practice Advisor. *Brief fix:*
   `source_ref` must be the document whose text contains the figure. When two reports cover one event, cite each for
   its own numbers.
2. **A margin read as a spread.** Digits' 0.4-point margin over humans became "within 0.4 points of each other".
   AFP's "enhanced efficiency in fraud reporting" became "faster". *Brief fix:* copy the source's noun phrase into
   `measures`, and do not paraphrase what a percentage counts.
3. **Participant labels taken from the headline.** Mercor's "junior accountants" averaged about 5.5 years'
   experience. *Brief fix:* when a study labels its sample, give the sample's actual characteristics as well.
4. **Unsourced connective claims attributed to a source.** Examples: "a hypothesis, not a finding" put on Withum;
   "automated delivery assumes review" put on the Elev8 article; "may not transfer to a mid-market team" put on Digits.
   *Brief fix:* a parenthetical source ref means the sentence is in that source. Analyst caveats go in `notes`
   without a ref, or are stated as facts about the evidence.
5. **Embellished detail in solution and problem text.** Examples: "machine learning", "a lot of traction",
   "select cities", "waited three years", "most mid-market firms cannot fund their own platform", "per-seat
   pricing". *Brief fix:* in `problem` and `solution`, add no qualifier or cause that does not appear in the cited
   text, and quote when the wording carries weight.
6. **Dates from inputs, not pages.** Karbon (-20 against JSON-LD -23), the Stanford summary (month only, when the
   byline gives the day) and a Pilot hub page (2026-04 with no basis). *Brief fix:* take dates from the byline or
   JSON-LD. Use the year alone for undated pages and note that the page is undated.
7. **Grade resting on an adjacent step.** `06` was B for "AI-drafted commentary" on the strength of AI-assisted
   live reporting. *Brief fix:* the title must describe the step that the named deployment actually shows.
8. **Speaker types.** An AI consultant was called "a practitioner". An outsourced accounting leader was called "CAS
   leader". *Brief fix:* use the role the source gives.
9. **Corporate-structure inferences.** "KKR's investment in its non-attest arm" was not stated in Crowe's release.
   *Brief fix:* for deals and structures, state only what the release says about which entity did what.

No search-only figure was found inside an A or B entry.

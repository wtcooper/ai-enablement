# Verification report: tax / research-advisory

- **Verified:** 2026-10-17 (verifier brief `verify-research-advisory.md`, wave 2)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/use-cases/research-advisory.yaml` (25 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/research-advisory.md`
- **Method:** I pulled all 91 distinct source URLs from the two files (79 in the YAML and 12 more in module §10) and
  reopened every one with `curl` in a private working folder. I used `pdftotext` for the PDFs (KPMG M&A, Deloitte TTT,
  the Werfel appendices, the TEI Midyear agenda, the SJSU panel deck, the Swider paper and the full TaxCalcBench paper).
  For blocked pages I used the `r.jina.ai` text mirror (TPB, Wolters Kluwer, Preprints.org, D.C. Bar, The Tax Adviser
  survey table). I downloaded the Charlotin CSV to check the tax-row count. I checked dates against
  `article:published_time`, JSON-LD, on-page bylines, PDF metadata and arXiv submission history.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. For this module it gives
  `25 use cases, 11 graded A/B (44%)` and the expected WARN that the A/B share is below 50%. The other warnings belong
  to other streams' files.

## 1. Counts

| | Use cases |
|---|---|
| Kept as written | 3 (`#12`, `#17`, `#20`) |
| Fixed | 22 (all others) |
| Rejected | 0 |

No entry was rejected. Every cited source exists and was reached, directly or through a mirror. Each entry's core
claim holds once corrected. The module received 19 edits.

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 3 (01, 02, 09) | 0 |
| B | 8 | 11 (01, 02, 07, 08, 09, 13, 14, 16, 19, 21, 25) |
| C | 8 | 8 (03, 05, 06, 12, 20, 22, 23, 24) |
| D (idea) | 6 | 6 (04, 10, 11, 15, 17, 18) |

A/B share: 11 of 25 (44%), the same as before. Moving A to B does not change the share.

**Why the three A grades fell to B.** The vocabulary defines A as "a measured outcome from a named organization". In
all three entries the figure is a named practitioner's after-the-fact estimate of one task, quoted in a marketing case
study by the vendor that sells the tool:
- **#01:** Barnes Wendling's director says a footnote "would have taken me at least a full day" and took "within the
  hour". Sorren's partner says "4 to 5 hours" became "15 minutes". Sasserath's "1 hour to 10 minutes" and "1.5 days to
  3 hours" are not even quotations: they come from Accordance's own narrative. The 700+ queries a month is a usage
  count, and the entry itself called it "not an outcome".
- **#02:** Wright Ford Young's research lead says research "that would have taken two, four, or six hours" now takes
  "15 or 20 minutes".
- **#09:** Finney Neill's shareholder says a 10-hour project becomes "maybe two or two and a half".

Before verification, the entries' own `measures` fields described these figures as "recollection", "not a measured
sample" and "estimate", which contradicts grade A. The discourse and governance angles had already graded #01 B. The
named deployments are real, so B is the right grade.

**Consistency flag:** the wave 1 substantive-testing verifier kept A for comparable owner quotes in vendor releases.
The synthesis lead should settle this once for every module (see §6).

No A or B entry relies on a search-only source. The only search-only source in the file is AccountingWEB in `#18` (D),
and it is used only in a note.

## 3. Fixes and rejections

### Use cases

| # | Entry | Before | Action | Reason |
|---|---|---|---|---|
| 1 | 01, 02, 09 | Grade A | Fix (A to B) | **Grade inflated.** The figures are practitioner estimates or vendor narrative, not measured outcomes (see §2). Notes and header rewritten |
| 2 | 01 | Sasserath figures "as stated in the vendor case study" | Fix | Not a quotation from the firm. The figures are Accordance's own narrative, and the measures field now says so |
| 3 | 01, 16 | `BLUEJ-2026` at `bluej.com/events`, separate from `BLUEJ-HOME-2026` | Fix | **Wrong URL / duplicate ref.** `/events` redirects to the home page, so both refs were the same document. Merged into `BLUEJ-HOME-2026` at `https://www.bluej.com`, dated by access date (page undated) |
| 4 | 01 | Survey "co-produced by a vendor that sells a competing product" | Fix | Inaccurate. Blue J co-produced it, and Blue J sells the AI tool the survey promotes |
| 5 | 01, 02, 08, 09, 25 | Sasserath and Finney dated `2025-11` | Fix | The pages show "Nov 1, 2025". Changed to `2025-11-01` |
| 6 | 02 | Problem: "legacy tools find sources but leave the practitioner to assemble the analysis [WFY]"; "reasoning is rarely preserved in a form a reviewer can follow [TR]" | Fix | **Wrong document and embellished.** The WFY case study does not say this. The point comes from the Thomson Reuters blog, which says applying findings "still required substantial manual effort" and that answers without "preserved reasoning chains" are insufficient. Reworded and re-sourced |
| 7 | 02 | "the tool surfaced the documents needed to defend a debt-to-equity conversion" | Fix | Embellished. The tool "flagged the documentation needed" (minutes, board resolutions). It did not surface documents |
| 8 | 03 | "Werfel's preparer register lists control dilution … and agentic AI risk" | Fix | **Wrong document.** Agentic AI risk is item 14 of the *tax-authority* register. The 15-risk preparer register has no agentic item |
| 9 | 03, 06 | "OpenAI's tax department showed a research memo agent / Slack Q&A agent at a TEI-SJSU panel" | Fix | **Claim attributed to the wrong party.** The deck comes from a four-firm panel (RSM, Grant Thornton, EY, OpenAI) and labels the agents as "sample use cases and potential demonstrations". Now: a panel deck (panellists included OpenAI's tax reporting director) shows a sample agent built on GPT-5 |
| 10 | 04 | "twelve of eighteen models failed the same must-pass check" | Fix | Wrong figure. Twelve scored 0, and *eleven* failed the same New York PTET check. Inkling failed a different one |
| 11 | 04 | 14-point gap "among the AI products" | Fix | Vals reports it as an average across participants. The measures field is corrected |
| 12 | 05 | "In-house positions and policies sit in separate folders [TR-COCOUNSELCORP]" | Fix | Not on the page. The page says the product removes "the friction of managing research across multiple applications" |
| 13 | 05 | role_evolution: "KM teams become owners of the corpus … seniors review less repeated work" | Fix | **Unsourced connective claim.** Replaced with what the TR blog says (retain knowledge as seniors retire, reduce variability) and the KPMG panel listing |
| 14 | 06 | Staff use AI "for communication with other functions [KPMG-DE]" | Fix | Not in the release. Replaced with the release's actual uses and its 89% / 29% split (base not stated) |
| 15 | 06 | TEI Midyear "programme ran hands-on Tax Labs"; dated 2026-03-15 | Fix | The PDF is a *preliminary* programme created 2026-02-09. Now "scheduled", dated `2026-02`, title marked preliminary. This matches the compliance-corporate verification |
| 16 | 06 | KPMG-DE dated 2026-05-06 | Fix | The release dateline reads "Berlin, May 7, 2026". JSON-LD shows 6 May at 10:28 UTC. The byline is used |
| 17 | 07 | "Crowe says Ask Blue J is implemented across its entire tax practice" | Fix | **Wrong speaker.** "Entire tax practice" is a quotation from Blue J's chief revenue officer, not from Crowe |
| 18 | 08 | "Blue J and CPA.com describe three training levels" | Fix | Wrong speaker. The quotation is from CPA.com's Brandon Allfrey |
| 19 | 09 | Problem: planning advice "rebuilt from scratch each time … leaving smaller firms reactive" | Fix | **Unsourced connective claim.** Replaced with the case study's own facts (about a 10-hour project; research a "tiresome" roadblock) |
| 20 | 09 | PCRT risk: "a tool built for common scenarios may embed assumptions" | Fix | Embellished. Now PCRT's actual wording: time-saving should not mean relying on data that does not apply to the client |
| 21 | 10 | role_evolution: "(discourse-angle synthesis)" | Fix | Unsourced connective claim. Replaced with Lowy's statement on narrowing and rejecting AI-generated ideas |
| 22 | 11 | Lowy "lists pressure-testing arguments"; CPA Practice Advisor "suggests asking AI to argue the opposite" | Fix | Embellished, and the audience was wrong. Lowy lists generating alternative arguments and testing framings. The CPA Practice Advisor advice is for CPAs to coach *clients* |
| 23 | 13 | role_evolution: "(practice-angle synthesis)" | Fix | Unsourced connective claim. Now limited to what WFY says about verification |
| 24 | 14 | "PCRT lists report writing … as a current use" (also 21: M&A "current example") | Fix | Embellished. PCRT gives these as examples of how AI *can* be used |
| 25 | 14 | Disclosure: "no federal rule mandates disclosure" | Fix | Out of date. That was JofA's April 2025 view. OPR's June 2026 alert says practitioners should disclose AI activities when crediting cost savings. Both are now stated |
| 26 | 15 | Problem: opinions relied on "including for penalty protection; the signer carries the consequences" | Fix | **Embellished / unsourced.** Neither OPR nor KTS says this. Replaced with s10.37 and the KTS verification duty |
| 27 | 15 | Risk carried the internal note "his Heppner reference was not checked" | Fix | Moved to notes |
| 28 | 16 | "we will research and call you back', often a day later" | Fix | Embellished. The source says complex research "could consume most of a workday" |
| 29 | 16 | Risk "Anything said live … (practice-angle recommendation)" | Fix | Unsourced. Removed; the human checkpoint already covers it |
| 30 | 18 | role_evolution: "(discourse-angle synthesis)" | Fix | Unsourced connective claim. Replaced with the article's engagement-letter advice |
| 31 | 19 | Holmes: "fewer than a dozen; no sanctions as of March 2026" | Fix | Overstated. Holmes "hasn't yet issued any sanctions himself" |
| 32 | 19 | "nearly 800" figure: "the paper was not opened" | Fix | I opened the Texas A&M preprint. It says "nearly 800 cases", and Bloomberg Tax says "errors". Added as source `PREPRINTS-HALLUC-2026` |
| 33 | 19 | role_evolution: "Review time moves from reading prose to verifying authority …" | Fix | Unsourced connective claim. Replaced with the Aon adviser's documentation advice (JOFA-AIPOLICY-2026) |
| 34 | 21 | Risk: "Draft reports could carry unsupported statements … into a negotiation" | Fix | Unsourced. Reduced to the sourced point that no error rate is published |
| 35 | 22 | Risk "A missed PE issue could leave an exposure unpriced"; role_evolution "exception review (vendor framing)" | Fix | Unsourced. The V7 page says neither. The risk was removed, and role_evolution now reads "Not described". The note flags the page's testimonials as general V7 Go quotes |
| 36 | 23 | Risk "A stale rule propagates to every client agent"; role_evolution "(discourse-angle synthesis)" | Fix | Unsourced connective claims. The risk was removed, and role_evolution now reflects the KPMG release |
| 37 | 24 | Title "… and sell them as a service"; problem "needs tax and engineering skills together"; "tax clients first"; role "(practice-angle synthesis)" | Fix | Embellished. Neither release mentions selling agents or the skills gap. KPMG says "an initial focus on tax clients and private equity". Rewritten from the releases |
| 38 | 25 | RKL figure "per an RKL tax partner quoted"; role "(practice-angle synthesis)" | Fix | The "several dozen" is the journalist's statement, not a quotation. role_evolution now uses the RSM partner's and PwC leader's sourced statements |

### Module

| Section | Before | Action | Reason |
|---|---|---|---|
| Read this first | "A 3, B 8 … The three grade-A entries rest on …" | Fix | Grade mix updated to A 0, B 11, with an explanation of why no entry reaches A |
| §2 table | "since 2026 an explicit check that each authority exists and supports the point [TAXCT-CLINCO]" | Fix | Embellished. JofA *recommends* firm policies requiring verification of every cited authority. Nothing changed "since 2026" |
| §2 table | "Planning analyses rebuilt from scratch each time [FINNEY]" | Fix | Not in the source. Now "an S-corporation election analysis took about 10 hours" |
| §2 table | "knowledge in seniors' heads [TR-AGENTICBLOG]" | Fix | TR's point is that knowledge leaves as seniors retire |
| §3 | #01, #02, #09 tagged (A); #24 "firms sell client-built agents" | Fix | Grades updated; "sell" was unsupported |
| §5, §7, §9 | "71% of German companies", "58% of German companies", "most German respondents" | Fix | The KPMG Germany release does not say the respondents are German companies. Now "companies in KPMG Germany's quick surveys" |
| §5 | VLAIR "14 points lower on multi-jurisdiction questions" tied to AI products | Fix | The average is across participants |
| §5 | "nearly 800 AI citation errors" (preprint) | Fix | **Statistic reported as something else.** The preprint counts *cases* of citation errors or hallucinations |
| §6 | "Disclosure to clients is not mandated federally" | Fix | Out of date. JofA 2025 is now paired with OPR's 2026 call to disclose AI activities when crediting savings |
| §7 | "Review moves from prose to authority"; "Partners spend more time on scoping and pricing … become agent designers" | Fix | Unsourced connective claims. Replaced with sourced statements (Aon documentation; RSM partner; KPMG and EY platforms) |
| §8 | "KPMG and Anthropic Digital Gateway, tax clients first" | Fix | The release says "initial focus on tax clients and private equity" |
| §8 | "AstraZeneca asked the OECD … draft Chapter VII examples include shared AI tools" | Fix | **Wrong speaker.** "Companies" asked; AstraZeneca commented that AI will change intragroup services. "Chapter VII" is not in the accessible text |
| §8 | "TEI Annual (18-21 Oct 2026) and CCH Connections (25-28 Oct 2026)" | Fix | Unsourced dates (no source cited). Removed |

Every other module figure checks against its source: AICPA 65% / 1,808 / 16% / 24.3%; Blue J 2026 60% / 33% / 80%
/ 90% / 46% / 69% and 12-23 Mar 2026; TR-FOP 81%, more than one-quarter, almost one in three, more than one-third;
CPAPA-TR 34% / 21% / 19% / 14%; Vals 49.19%, the category bests and 601 vs 2,366 words; TaxEval 80.38% archived as
saturated; Stanford 17-33%; Antinozzi 39-47%; TaxCalcBench 32.35% on 51 returns; Charlotin 2,199, with 25 rows whose
primary field is tax (31 including secondary); Holmes; Fonoa 57.4% / 176 / 12.5%; OPR sections; SSTS 1.4; Clinco 3 of
4; PCRT; HMRC; TPB; Werfel 20 / 15 risks; CART; AICPA fees; Blue J $122M; Accordance $13M and 10x; CoCounsel 1,300+.

## 4. Sources that could not be fully reached

- **AccountingWEB, Elden article** (`ACCOUNTINGWEB-ELDEN-2026`): 403, and the mirror returned only a stub. It stays
  `search-only` in `#18` (D) and appears only in a note. Elden itself is confirmed through ICAS and Ross Martin.
- **Bloomberg Tax, OECD intragroup article** (`OECD-INTRAGROUP-2026`): paywalled; only the opening paragraphs were
  readable. The module text is limited to those paragraphs.
- **Sala, Tax Notes State** (`SALA-TAXNOTES-2026`): only the TaxProf abstract was read. Entries already say so.
- **JHU tax-abuse paper** (`JHU-TAXABUSE-2025`): only the abstract was read. The entry says so.
- **Read through mirrors only (content confirmed):** TPB guidance (direct fetch failed), Wolters Kluwer, Preprints.org,
  D.C. Bar session page, and The Tax Adviser survey table.
- **Not verified:** Siva's *Heppner* citation (now a note in `#15`); the Bloomberg Tax attribution of "nearly 800" to
  *The International Tax Journal* (noted in `#19`).

## 5. Targets

| Target | Result |
|---|---|
| 15-25 use cases | Met (25) |
| At least 50% graded A or B | **Not met** (11 of 25, 44%). It was 44% before verification too |
| Every source has a URL and a date | Met. Undated vendor pages use the access date, and the locator says so |
| Ids unique; values from the vocabulary | Met (validator: 0 errors) |
| Quotations under 25 words | Met |

The shortfall is real. Tax research has many named deployments but almost no measured outcomes. Raising the share would
need new named deployments for the C entries (#05 knowledge assistant, #06 in-house triage, #23 monitoring), not
regrading.

## 6. Error patterns to fix in the briefs

1. **Practitioner recollections graded A.** Every A came from a named person's "would have taken a day, now an hour",
   quoted in vendor marketing. Brief rule: A needs a figure the organization measured (tracked hours, a parallel test,
   error counts). A named person's estimate of one task is B. A vendor's narrative figure that is not quoted from the
   firm is never more than B. This rule should be applied to every module, including wave 1, which kept such figures
   at A.
2. **Synthesis-angle labels used as sources.** Seven entries carried "(practice-angle synthesis)", "(discourse-angle
   synthesis)" or "(practice-angle recommendation)" in `role_evolution` or risks. These are unsourced connective claims
   under a label. Ban the label: either cite a source or write "Not described in the sources."
3. **Panel or vendor material attributed to one participant.** The SJSU deck became "OpenAI's tax department showed";
   the Blue J CRO's sentence became "Crowe says"; CPA.com's Allfrey became "Blue J and CPA.com". Require the speaker
   to be named exactly as the source names them.
4. **Item moved between parallel lists in one document.** Werfel's agentic risk sits in the authority register, not the
   preparer register. Synthesisers should check which list or table an item comes from.
5. **Hedges dropped.** "Example of how AI can be used" became "current use"; "recommend" became "since 2026 an
   explicit check"; "initial focus on tax and PE" became "tax clients first". Keep the source's modal verbs.
6. **Population inflated.** "KPMG Germany surveys" became "German companies"; "participants" became "AI products";
   "cases" became "errors". Keep the source's population and unit.
7. **Duplicate refs for one URL.** `/events` redirected to the home page, so two refs pointed at the same document.
   Briefs should require resolving redirects before assigning refs.
8. **Regulatory statements go out of date.** A 2025 "no federal disclosure rule" survived a June 2026 OPR alert that
   speaks to disclosure. Briefs should require checking older regulatory claims against the newest regulator source in
   the same file.

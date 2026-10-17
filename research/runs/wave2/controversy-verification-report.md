# Verification report: tax / controversy

- **Verified:** 2026-10-17 (verifier brief `verify-controversy.md`, wave 2)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/use-cases/controversy.yaml` (25 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/controversy.md`
- **Method:** I extracted all 93 distinct URLs cited in the two files (84 in the YAML, 9 more in module §10). I reopened every
  one with `curl` in a private working folder. I used `pdftotext` for the 11 PDFs (TIGTA, GAO, both NTA reports, the OECD
  *Governing with AI* report, HMRC's annual report, Deloitte TTT, the Werfel appendices, the TEI agenda, the Riddle Aggregates
  transcript and the CDTFA Tax Notes copy). I used the `r.jina.ai` text mirror for the 13 pages that returned 403 or 429 and for
  the paywalled Bloomberg pages. I also downloaded the Charlotin database CSV to recount its figures. I checked each figure, date,
  attribution and quotation against the saved text. For dates I checked `article:published_time`, JSON-LD, `firstpublishdate`,
  on-page bylines, PDF metadata and transmittal dates. Web search was used twice: once to find a second route to the OECD FTA
  announcement, and once (without result) for the Axios quotations.
- **Validator:** `python3 scripts/validate.py` reports nothing wrong with these two files. For this module it gives
  `INFO ... 25 use cases, 10 graded A/B (40%)` and the expected WARN that the A/B share is below 50%. The final run reports
  0 errors overall. The other warnings belong to other streams' files.

## 1. Counts

| | Use cases |
|---|---|
| Kept as written | 8 (`#06`, `#10`, `#11`, `#16`, `#17`, `#20`, `#24`, `#25`) |
| Fixed | 17 (`#01`, `#02`, `#03`, `#04`, `#05`, `#07`, `#08`, `#09`, `#12`, `#13`, `#14`, `#15`, `#18`, `#19`, `#21`, `#22`, `#23`) |
| Rejected | 0 |

Of the 17 fixes:
- **9 substantive:** a grade inflated by a metric that does not measure the outcome (`#23`), a claim not in its source
  (`#08` Buckeye, `#09` search-only claim cited to MoFo, `#15` demographic-data and HMRC-checkpoint claims, `#14` a GAO
  attribution), misattributed speakers (`#01`/`#02` FindSkill called a practitioner), a dropped scope qualifier (`#07` TEI
  "CTC jurisdictions"), an overstated finding (`#13` TIGTA "no process", and a GAO finding that has since been closed as
  implemented).
- **8 date, locator, wording or disclosure fixes:** TSCPA, KPMG, Elsbury, Buckeye and IRM dates; the Riddle Aggregates locator;
  the OECD FTA locator; a "scheduled, not held" fix; a conflict-of-interest note (`#03`); and an unverifiable-source note
  (`#22`).

Every cited source was reached directly or through a mirror, with two exceptions (see §4). The OECD FTA announcement was
confirmed through a second document. Axios (`#22`) could not be reopened by any route. Its core claim is independently
stated by EisnerAmper, so `#22` stays at C and its Axios-only quotations are flagged as not re-verified. No entry's core claim
failed, so nothing was rejected.

The module received 16 edits.

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 4 (15, 18, 19, 23) | 3 (15, 18, 19) |
| B | 6 (03, 13, 16, 17, 20, 21) | 7 (03, 13, 16, 17, 20, 21, 23) |
| C | 9 (01, 02, 04, 05, 06, 07, 08, 22, 24) | 9 (unchanged) |
| D | 6 (09, 10, 11, 12, 14, 25) | 6 (unchanged) |

- `#23` (Brazil appeal files) moved from A to B. Its only figure is a model's sensitivity and specificity in first trials, which
  OECD relays from a 2022 source. That measures classifier accuracy, not throughput, ruling time or any dispute outcome. The entry
  had filed it under the `speed` lever. This is the "statistic reported as something it doesn't measure" pattern. It is still a
  named, piloted project (Brazil's AI Litigation Project), so B.
- `#15` (HMRC, Austria) and `#19` (ATO prompts) stay A. Both carry measured outcomes that the named authorities report themselves
  (GBP 10 billion; EUR 185 million; 636,000 prompts and AUD 78.9 million). The method is unpublished, and the entries say so.
- `#18` stays A on TAS's independent measurements (17% voicebot completion, 80% negative chatbot responses).
- `#21` stays B, but the basis is restated. The ATO and HMRC deployments support it. TAS's AI-assisted drafting was of a report
  to Congress, which is adjacent to casework and does not count.
- `#17` stays B. The 12-16 weeks to under three days figure is one official's spoken remark with no method.
- `#03` stays B. It is a named practitioner (2019), but the software is his son's product. That is now disclosed.
- No A or B entry relies on a search-only source. Every source is `access: full`.

**Practitioner side:** only `#03` is A or B. Nine of the ten A/B entries describe tax authorities, as the module header says.

## 3. Fixes and rejections

### Use cases

| # | Entry | Before | Action | Reason |
|---|---|---|---|---|
| 1 | 01, 02 | "A practitioner-written workflow" / "A practitioner write-up" (FINDSKILL-2026) | Fix | Wrong speaker. The byline is "FindSkill Team", a training-course vendor that ends with a course pitch. Now "a training vendor's suggested workflow/blog" |
| 2 | 01 | "TEI's March 2026 Midyear programme had a 'Managing Tax Notices with AI' lab" | Fix | The source is a *preliminary* programme. Now "listed". Locator gives the session day |
| 3 | 01 | "Commentators say notice volume is rising" | Fix | Overstated. One Accounting Today commentator says notice volume *will* grow ("as projected"). Now attributed to one commentator, as an expectation |
| 4 | 01, 04 | ACCTODAY-2026 author "works at a vendor" / "vendor employee" | Fix | Imprecise. The author is operations manager at Ledger Labs, an outsourced accounting provider. Wording corrected |
| 5 | 01 | TPB client permission before entering data into AI tools | Fix | Qualifier dropped. TPB says permission is needed "depending on how these tools are configured and used". Restored |
| 6 | 03 | Weekly transcript monitoring (Nemeth, 2019) | Fix (note) | The article says the software (Tax Help) was designed by Nemeth's son, who made the capability a selling point. The account is not independent. Disclosed. Grade unchanged (B) |
| 7 | 04 | TSCPA-2026 dated "2026" ("page undated") | Fix | The page is dated 26 May 2026. Its authors are two East Tennessee State University accounting faculty. Date and locator corrected |
| 8 | 05 | KPMG-TP-2025 dated "2025" | Fix | `publishDate` metadata is 2 Apr 2025, which transfer-pricing.yaml already uses. Now 2025-04-02 |
| 9 | 07 | "In-house practitioners at TEI describe authorities arriving at audits with data they have already analysed" | Fix | Scope qualifier dropped. The TRI recap says this of authorities "in mature CTC [continuous transaction control] jurisdictions", from one panel speaker. Restored |
| 10 | 07 | Miller & Chevalier CLE "covered" private AI use | Fix | The page is a pre-event announcement ("will focus on"). Now "was billed to cover" |
| 11 | 08 | "an Indian tax tribunal order was recalled after relying on non-existent judgments" | Fix | Not in the source. The digest and the Karnataka High Court order (18 Sep 2025) say only that the ITAT order "prima facie" appeared AI-driven and was recalled. Wording corrected. Date changed from 2025-09-18 (the order) to 2025-10-29 (the digest page cited), and the order date is given in the locator |
| 12 | 08 | Riddle Aggregates report "is recorded as withdrawn"; locator pp. 604-614 | Fix | The transcript shows IRS counsel withdrawing Exhibits 9006-R and 9007-R at p. 618. Now "IRS counsel withdrew ... at trial", locator pp. 604-618. The challenge was to quotations attributed to the Yellow Book that do not exist |
| 13 | 09 | "a search summary (not opened) says another court reached a different result (MOFO-HEPPNER-2026)" | Fix | A search-only claim attributed to a document that does not contain it. Removed. The risk now gives what MoFo does say: the case turned on a consumer tool used without counsel's direction |
| 14 | 12 | OECD-FTA-2025 locator | Fix | The OECD page now sits behind a bot check. The commitment ("deepen our co-operation on real-time information sharing ... ongoing development of pilot projects") was re-confirmed in the FTA Cape Town Plenary statement of outcomes, hosted by Japan's NTA. Added to the locator |
| 15 | 13 | "TIGTA found the IRS has no process to evaluate whether AI models beat prior methods" | Fix | Embellished. TIGTA says the IRS "does not have sufficient processes for evaluating whether implemented AI models perform better than prior processes". Wording restored. Same fix in module §3 |
| 16 | 13 | NTA no-change rate: "does not attribute it to AI" | Fix | Incomplete. TAS puts the figure right after "greater use of AI may reduce the IRS audit no-change rate", without attributing this fall to AI. Both points now given |
| 17 | 13 | "GAO found the IRS had not completed documentation of an AI sampling pilot's key components (GAO-TAXGAP-2024)" | Fix | Stale. GAO's page now records recommendations 2-4 as "Closed - Implemented" (Oct 2024 to Aug 2025) and 5 as partly addressed. The pilot is for National Research Program research audits, not operational selection. Both points added |
| 18 | 13, 21 | IRM-10-24-1 dated 2026-02-10 | Fix | The page opened is the revision transmitted 10 Aug 2026, which supersedes the 10 Feb 2026 issue. Date now 2026-08-10, and the first-issue date is given in the locator |
| 19 | 13, 14 | GAO-EQUITY-2024 dated 2024-04-25; GAO-TAXGAP-2024 dated 2024-05-06 | Fix | Only the month could be confirmed: the report covers say "April 2024" and "May 2024", and the PDFs were posted 21 May and 5 Jun 2024. Set to 2024-04 and 2024-05 rather than keep unconfirmed days |
| 20 | 14 | "Feedback from exam outcomes can entrench past enforcement patterns (GAO-EQUITY-2024)" | Fix | Wrong document. GAO-24-106126 makes no such general claim. The point is made by EFF's Haley Tsukayama in the Tax Notes Talk episode (systems learn "heuristic biases ... from historic patterns of audits"). Re-sourced to NTT-BIAS-2026, which was added to the entry's sources |
| 21 | 14 | Checkpoint "Division leaders review exam performance results as part of model refinement" | Fix | Stated as practice, but it is TIGTA's Recommendation 1, which the IRS agreed to subject to staffing. Reworded as a recommendation |
| 22 | 15 | "Commissioners from eight states described AI and analytics..." at SEATA | Fix | Unsupported count. Withum's recap says commissioners and staff highlighted AI and analytics. Several state lines are Withum's inference ("suggests", "likely"). Reworded |
| 23 | 15 | "Tax Notes reporters ... say demographic data may not be collected, limiting bias testing" | Fix | Not in either Tax Notes source. The point is in Werfel's register (risk 7). Re-attributed, and AICPA-WERFEL-2026 added to the entry's sources |
| 24 | 15 | "HMRC caseworkers decide on investigations ... (CSW-HMRC-2026)" | Fix | Wrong document. CSW does not say this. HMRC's roadmap update says Copilot supports compliance work "always with skilled caseworkers making final decisions". HMRC-UPDATE-2026 added to sources |
| 25 | 15 | ELSBURY-ICO-2025 dated 2025-07-31 | Fix | The decision was given on 2 Aug 2025 (heard 27 Jun 2025). Date and locator corrected |
| 26 | 18 | Chatbot measure: "TAS says this is not an accuracy or resolution measure" | Fix | Embellished. TAS calls for "a more thorough quality measurement framework". Reworded |
| 27 | 18 | "Singapore's multilingual chatbot ... halved call-centre inquiries" | Fix | Scope dropped. Grant Thornton names "Ask Jamie", Singapore's government-wide assistant, so the figure is not tax-specific. Now stated |
| 28 | 19 | Risk "Pre-fill override and opaque comparison groups mean records are needed to justify changes (ONENEWS-2026)"; role "Preparers face a data-matched baseline" | Fix | Unsourced connective claims. OneNews supports only the ATO quotation that it "may adjust it back" with high confidence. Both lines now say that and nothing more |
| 29 | 21 | Note "Graded B on the ATO and TAS named deployments" | Fix | TAS's AI use was drafting its report to Congress, which is adjacent to casework. The grade now rests on the ATO and HMRC deployments |
| 30 | 22 | Axios quotations (vendor guardrails; Chief Counsel attorney "negligence", adopt or leave) | Fix (note) | Source blocked for the whole session (curl 403; the text mirror blocked axios.com on a rolling basis; archive.ph 429; web.archive.org reset). The core claim is confirmed by EisnerAmper, which already sits in the entry's sources. C is the most a blocked source allows, and the entry is already C. The quotations are kept but marked as not re-verified |
| 31 | 23 | Grade A; lever `speed`; "over 80% sensitivity and specificity" | Fix | Grade inflated, and the statistic is reported as something it doesn't measure. Lever changed to `quality` with an explicit "model accuracy, not speed or outcome" caveat. Grade A to B (see §2) |

### Module file

| # | Section | Before | Action | Reason |
|---|---|---|---|---|
| 1 | §2 Selection row | "the representative meets it as an unexplained letter [TSCPA-2026]" | Fix | Embellished. TSCPA says only that criteria are not explained. Now "Selection criteria are not published [TSCPA-2026; ACCTODAY-2026]" |
| 2 | §2 Notice intake | "volume rising while IRS capacity falls (commentary)" | Fix | Unsourced and overstated. Now one commentator's expectation [ACCTODAY-2026] |
| 3 | §2 Examination | "Authorities arrive with data already analysed" | Fix | CTC-jurisdiction qualifier restored (as YAML fix 9) |
| 4 | §3 `#12` | OECD pilots, no key | Fix | Source key added [OECD-FTA-2025] |
| 5 | §3 `#13` | "TIGTA found no process" | Fix | Now "no sufficient process" (as YAML fix 15) |
| 6 | §3 `#23` | "(over 80% sensitivity and specificity in trials)" | Fix | Caveat added: early trials, model accuracy, not a speed result |
| 7 | §6 Tax Court | Rule 201(a) cited to BLAW-TAXCT-2026 | Fix | Wrong document. Rule 201(a) is in the JofA Clinco article. Key added [TAXCT-CLINCO-2026] |
| 8 | §6 Australia | "get client permission before entering client data" | Fix | TPB's configuration qualifier restored ("into a tool that discloses it to a third party") |
| 9 | §7 In-house | "One academic argues" (Sala) | Fix | Embellished qualifier. The TaxProf abstract does not identify Sala as an academic, and his text speaks as a practitioner. Now "One Tax Notes State author" |
| 10 | §8 Frontier, §7 | "2025-11-21 IRS announces Agentforce..."; "A Chief Counsel attorney: adopt or leave" | Fix | The source is an Axios exclusive drawing on a Salesforce announcement, not an IRS announcement. Now "Axios reports the IRS deploying...", with EisnerAmper added as confirmation. The §7 quotation is marked as not re-verified |
| 11 | §9 "AI makes up cases" | "One practitioner workflow" | Fix | Wrong speaker (as YAML fix 1) |
| 12 | §9 "It fails silently" | "TEI attendees describe AI that 'fails quietly and even politely'" | Fix | Wrong speaker. The phrase is the Thomson Reuters Institute author's own summary line, not attendees' words. Re-attributed |
| 13 | §10 | PROSKAUER-707-2026 dated 2026-07 | Fix | The post is dated 29 Jul 2026. Now exact |
| 14-15 | §3, §5 | Brazil and TIGTA wording | Fix | Kept in step with the YAML fixes above |

### Checked and confirmed (no change)

- EY survey: 1,934 respondents, 12 industries and 48 jurisdictions; 39% + 30%; 46% vs 31%; 44% talent barrier; 49% tailoring
  TP documentation; TP Doc Insights and the Joel Cooper quote; Daren Campbell's "classification, document summarization and key
  element extraction"; "only showcasing"; "should be reviewed by humans". Press release 70%; Paperjam quote and date.
- EY Bloomberg op-ed (21 Nov 2025): "draft responses to audit queries", the tax notices bullet, "assembling information to
  applying critical judgment", "improve the human's review, not to remove the need for the review".
- WK notice page and DocAn page (both 2026-07-06): every quoted phrase, including "partner-level signer" and "still determines".
- OPR Alert 2026-19 (24 Jun 2026): §§10.22, 10.27 (pattern across clients, billing differentials), 10.35, 10.36, 10.37,
  6713/7216, 10.51(a)(15), "secure, enterprise-approved AI", best practices.
- Clinco (T.C. Memo. 2026-16): 3 of 4, repeated citation after the IRS flagged it, first Tax Court case, bank-deposit analysis,
  Rule 201(a), SSTS 1.4, verification logs and second reviewer. BLAW-TAXCT: three-quarters pro se, fewer than a dozen, §6673
  $25,000, "feeling our way", Khoja hearing 11 Mar, SSNs and bank numbers. Harber (9 cases), Zzaman, Elden (ICAS, 26 Jan 2026).
- Charlotin CSV: 2,200 rows, 25 with tax as primary field, Riddle Aggregates "Report withdrawn" (Expert). Heppner Feb 17, 2026 memo.
- TIGTA 2025-308-022 (19 May 2025): pilot results, redactions, $3.9M and $7.9M, top three issues, add/remove issues, human classifiers,
  recommendations and responses.
- GAO-26-107522 (24 Mar 2026, from the PDF): 126/10/65/77 (61%), over 25% lacking benefit info, 63 staff, no agency-wide entity,
  8 recommendations agreed, 180-day letter fall 2026, 18 of 43, two fraud uses without human review, 11 voicebots and 2 chatbots,
  5M and 25M sessions, audit-outcome data risk.
- TIGTA 2026 via Accounting Today (28 Sep 2026): 225 use cases, 2 of 5 and 4 of 5, no Treasury guidance as of July 2026.
- NTA 2025 annual report: FY2026 25%/20%, the no-change rate under $50k, no-response up more than 10 points, 80% negative, 23 of 200
  (11.5%), +68%/-7%, staff to "train the AI". NTA FY2027 objectives: 17%/46%/14%, 12.4M to 9.9M (-20%), +4%, 8 to 14 min, over 85%
  callbacks, TPP 2.4M/19%/20 min, Archie about 12,000 CSRs, Taxpayer 360, the AI-assistance statement.
- Nextgov (2 Oct 2026): "AI-first IRS", 12/14/16 weeks to under three days, "hundreds of thousands" of about 5 million, 1,500
  detailees, 74,000 flat after 4,000+ hires, "not designed to eliminate jobs", mid-90s vs about 85%.
- HMRC ARA 2025-26: GBP 10 billion, first Chief AI Officer Apr 2026, NLP for complex casework, Copilot trial, rapid case summaries,
  GBP 50.2 billion yield. Pinsent (Robotham, Connect, 5,500). CSW ("broadly the same size in 2030", telephony summarisation). HMRC
  roadmap (21 Jul 2025) and 2026 update (28,000 licences, 50,000 plan, synthetic data, call summarisation pilot with human review).
- OECD *Governing with AI*: Box 5.2 (USD 140 billion, six years, 2,000 files, over 80%), Box 5.3 (2014, 6.5 million, EUR 185
  million, 375,000 of 27.5 million), Box 5.5 (636,000, AUD 78.9 million), 26,000 Dutch families, taxpayer-rights text.
- ANAO (28 Feb 2025): partly effective, 32 of 43 (74%), 14 models, no ongoing monitoring, December 2026, seven recommendations
  agreed. ATO statement (human adverse decisions, right of review, CDO as accountable official, nudging comparison basis). ATO CDO
  speech (22 Apr 2026): receipts and invoices, "digital shoebox", seven priority uses, "next frontier", "explain it, defend it, or
  audit it", "not about replacing people".
- CDTFA Tax Notes (26 Aug 2025), Tax Notes Talk (4 Jul 2025, Minnick), NTT-BIAS (22 May 2026: FTB 2021, CISS, AB 302 zero, FTB
  over-selection checks, EFF), Tax Notes survey (22 of 36, 7), SC Post and Courier ($3.5 million, five years, December, sales and
  use tax, "same criteria"), KPMG and WTS Hungary, KPMG UK ICTS, Bloomberg Africa, CIAT (3 Feb 2026, "always under human
  supervision").
- Werfel article (31 Aug 2026; 20 and 15 risks; tiers; eight steps; views not AICPA policy) and appendices (risks 1-5, 7, 13, 14,
  15, 17, 18, 20). CART (23 Sep 2026; NAEA, FTA; value-pricing objection). Duke (26 Mar 2026). Sala abstract (20 Jul 2026).
- SIEPR (Jan 2023; 2.9-4.7; EITC; no-change and refundable-credit targeting). Stanford FAccT (2010-14; high to middle income).
  FedScoop GAO bias (sex, 2001). GAO-24-106126 (default audits). EU AI Act Recital 59. Hadwick (30 Dec 2024). PCRT (19 Jan 2026).
  Proskauer (FRE 707, 3-4 Jun 2026). TPB(GS) 55/2026 (issued 22 Jul 2026). SSL OECD VAT (29 Jun 2026, Hanna Lee). Bloomberg OECD
  (70% of 54, 2024 data). Accrual Arc (22 Sep 2026). Blue J ("Response to IRS notices"). CPA Practice Advisor (29%). arXiv
  2508.20097 and 2508.21051 (dates and abstracts).
- TEI recap (4 May 2026): two hands out of more than 50. TR TEI auditor (12 May 2026). EY India (18 Feb 2026). EisnerAmper
  (27 Jan 2026): revenue agents and IDRs, Agentforce rollout across Chief Counsel, TAS and Appeals.
- All remaining dates match their sources' metadata.

## 4. Sources that couldn't be reached directly

| Source | Problem | Route used | Result |
|---|---|---|---|
| IRS-AGENTFORCE-2025 (Axios) | 403 to curl; the text mirror blocked axios.com and re-blocked it when retried after the first block lifted; archive.ph 429; web.archive.org reset by proxy; one web search found no other copy of the quotations | none | **Not reached.** The core claim is confirmed by EisnerAmper (EISNER-IRSAI-2026). `#22` stays C, and its Axios-only quotations are flagged in the entry and in module §7 |
| OECD-FTA-2025 | Cloudflare bot check (curl and mirror) | Web search led to the FTA Plenary statement of outcomes PDF (nta.go.jp) | Claim confirmed; locator updated |
| GAO-26-107522, GAO-24-106126, GAO-24-106449 | 403 | Mirror of the product pages and report PDFs | Read; GAO-26 date confirmed from the PDF, GAO-24 dates to month only |
| WK-NOTICE-2026, WK-DOCAN-2026 | 403 / bot check | Mirror (DocAn on the second attempt) | Read in full; 2026-07-06 confirmed |
| ATO-SPEECH-2026, ATO-AI-2026, ANAO-ATO-2025, TPB-GS-2026, IRS-LBI-TP-2026 (EY Tax News) | 403 or timeout | Mirror | Read in full |
| Bloomberg Tax and Law pages (6) | Paywall | Mirror | Cited passages visible in full |
| TAXNOTES-UNWATCHED-2026 | 429 | Mirror | Read |
| SALA-TAXNOTES-2026 | Tax Notes body paywalled | TaxProf abstract | Abstract only, as the module already says |

## 5. Targets

| Target | Result |
|---|---|
| 15-25 use cases | **Met** (25) |
| At least 50% graded A or B | **Not met.** 10 of 25 (40%), unchanged in count. A fell from 4 to 3 when `#23` moved to B. Nine of the ten are authority-side. Grades were not raised to reach the target |
| Every source dated | **Met.** Every source has an ISO date and a URL. Two are year-only stand-ins for undated pages (TR-COCOUNSEL-2026 from its URL; ATO-AI-2026, whose update date conflicts between sources), and both are flagged in their locators or notes |
| Unique ids, vocabulary values | Met (25 unique ids; validator reports 0 errors) |
| Quotations under 25 words | Met. The longest verbatim quotation is the ATO's "if we can't explain it, defend it, or audit it - we shouldn't deploy it" |

## 6. Patterns of error to fix in the briefs

1. **Publisher type taken for speaker type.** A training-course vendor's blog became "a practitioner-written workflow" in two
   entries and the module. An author's summary line became "TEI attendees describe". A Tax Notes author became "one academic".
   Briefs should require the byline or speaker's role, copied from the page, for every attributed sentence.
2. **Search-only content written into an entry under an opened source's key.** `#09` attributed a search snippet ("another court
   reached a different result") to MoFo. Briefs should forbid putting search-only text in any field that carries a ref, even when
   it is labelled "not opened".
3. **Embellished findings.** "Insufficient processes" became "no process". "Prima facie AI-driven" became "relying on non-existent
   judgments". "Unexplained" became "an unexplained letter". "Will grow" became "is rising". Briefs should require the source's
   own verb and qualifier for every finding from an audit, a court or a regulator.
4. **Model-accuracy metrics graded as outcomes.** Brazil's classifier sensitivity was graded A and put under the `speed` lever.
   Briefs should state that classifier accuracy, licence counts, session counts and tool availability do not count as measured
   outcomes for an A grade unless the source links them to the work.
5. **Stale regulator findings.** GAO's 2024 documentation finding had been closed as implemented by 2025, and the IRM had been
   revised in August 2026. Briefs should require checking a GAO recommendation's current status, and the current revision date of
   any manual or guidance page, before citing a finding as live.
6. **Scope qualifiers dropped.** "In mature CTC jurisdictions" (TEI), "depending on how tools are configured" (TPB), "government-wide
   Ask Jamie" (Singapore), "preliminary programme" (TEI) and "billed to cover" (CLE) were all lost. This repeats the
   compliance-corporate finding. Briefs should require copying the source's scope words into the claim.
7. **Connective sentences sourced to the nearest document.** Six sentences in `role_evolution`, `risks_and_guardrails` and
   `human_checkpoints` (`#14`, `#15` x3, `#19` x2) cited a source that sits nearby but does not contain the claim. Briefs should
   require a string search of the cited page for each such sentence. If nothing matches, the sentence goes or reads "Not described
   in the sources".
8. **Order dates and page dates conflated.** The Buckeye digest was dated by the court order, Elsbury by an approximate date, and
   the IRM by its first issue rather than the revision opened. Briefs should say the source date is the date of the page cited,
   with any event date given in the locator.
9. **Conflicts of interest unflagged.** The only named practitioner deployment (`#03`) promotes the practitioner's son's software,
   and the Accounting Today author works for an outsourced accounting firm. Briefs should require recording author affiliation when
   an entry rests on one first-person account.

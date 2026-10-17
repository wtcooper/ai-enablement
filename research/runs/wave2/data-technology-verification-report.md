# Verification report: tax / data-technology

- **Verified:** 2026-10-17 (verifier brief `verify-data-technology.md`, wave 2)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/use-cases/data-technology.yaml` (24 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/data-technology.md`
- **Method:** I extracted all 77 distinct source URLs in the YAML, plus 3 more cited only in module §10, and reopened every
  one with `curl` in a private working folder. I used `pdftotext` and `pdfinfo` for the 11 PDFs, and fetched every HTML page a
  second time through the `r.jina.ai` text mirror for pages that render with JavaScript or are paywalled (Bloomberg Tax,
  Deloitte, Snowflake, Kognitos). I checked each figure, date, attribution and quotation against the page text. Dates were
  checked against `article:published_time`, JSON-LD `datePublished`/`datePosted`, on-page datelines, arXiv history and PDF
  metadata. I used one web search, to find a route to the blocked OECD page.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. For this module it reports
  `INFO ... 24 use cases, 8 graded A/B (33%)` and the expected WARN that the A/B share is below 50%. The other warnings
  belong to other modules' files.
- **Note:** a parallel agent's snapshot commit (`10ae60f`) picked up these edits while I was working. The files on disk are
  the final versions.

## 1. Counts

| | Use cases |
|---|---|
| Kept as written | 6 (`#03`, `#08`, `#10`, `#13`, `#20`, `#21`) |
| Fixed | 18 (`#01`, `#02`, `#04`, `#05`, `#06`, `#07`, `#09`, `#11`, `#12`, `#14`, `#15`, `#16`, `#17`, `#18`, `#19`, `#22`, `#23`, `#24`) |
| Rejected | 0 |

The 18 fixes break down as follows:
- **7 substantive fixes:** a misattributed quotation (`#02`), overstated vendor facts (`#05`, `#02`), unsourced connective
  claims in `problem`, `human_checkpoints` or `role_evolution` (`#09`, `#14`, `#15`, `#18`), and a statistic reported as
  something it doesn't measure (`#24`).
- **11 smaller fixes:** wording, sourcing or notes. These cover the OECD source route (`#12`), a source upgraded from
  search-only to full (`#17`, which also added a new fact to `#18`), and attribution tightened from "speakers" or
  "panelists" to what the recap actually says (`#04`, `#14`, `#16`, `#24`).

Nothing was rejected. Every cited source exists and was reached, directly or through a mirror. The one exception is the
OECD announcement page; its content was confirmed from the official FTA statement of outcomes (see §4).

The module received 22 edits.

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 0 | 0 |
| B | 8 (01, 04, 05, 06, 08, 09, 22, 23) | 8 (unchanged) |
| C | 14 | 14 |
| D | 2 (10, 16) | 2 |

- No grade changed. Each B rests on a named organisation: the Snowflake, Fortive and OpenAI postings and OpenAI's live
  demonstration; Siemens Energy and Daimler Truck; DuPont; Oxford Industries; Rover; and Unilever.
- Three of the eight B entries are not AI evidence. `#04` and `#05` were already disclosed as not AI. I added `#23` to the
  module's caveat, because the Unilever podcast listing does not mention AI.
- `#09` stays at B, not A. It has a named organisation and a figure, but the figure is vendor-published, comes from an
  adjacent process (sales tax), and what was timed is unclear.
- No A or B entry relies on a search-only source. The only search-only source left in the file is the OECD announcement
  in `#12` (grade C), and the full statement of outcomes now sits beside it.
- **Ladder:** assist 4, augment 12, automate 5, delegate 3. **Change scope:** step 5, process 14, model 5. Neither changed.

## 3. Fixes and rejections

### Use cases

| # | Entry | Before | Action | Reason |
|---|---|---|---|---|
| 1 | 02 | role_evolution: "PwC Ireland says tax teams should shift from assembling information to applying judgment and conducting high-quality reviews" | Fix | Wrong document. The sentence is in the EY authors' Bloomberg Tax op-ed (BTAX-EYGRIP-2025), not on the PwC Ireland page. Re-attributed, BTAX-EYGRIP-2025 added to sources, and PwC's own point (AI frees people for judgement and challenging outputs) kept with its citation |
| 2 | 02 | "Savant's Spring 2026 release adds connectors to Oracle Fusion, SAP S/4HANA and Microsoft Fabric" | Fix | Overstated. Oracle Fusion and SAP connectors were *expanded*; only Fabric Lakehouse is new |
| 3 | 05 | Problem: "aggregate data from dozens of templates ... with errors and key-person dependency (RGP; Concentrix)" | Fix | "Dozens of templates" is in neither source. Rewritten from Concentrix's text (200+ tax managers, 260,000+ returns, tribal knowledge held by individuals) |
| 4 | 05 | "An RGP client built over 100 process streams ... with controls" | Fix | Embellished. RGP "identified over 100 process streams ripe for improvement" and designed "numerous" flows. Concentrix "consulted on" more than 80 workstreams; it did not train staff "across" them |
| 5 | 05 | Checkpoint: "Tax reviewers verify the visual workflows and outputs" | Fix | Turned a marketing line ("easily verifiable by any reviewer") into a control step. Now says no review step is described |
| 6 | 09 | Problem: "in-house teams reconcile data across several ERPs and source documents by hand ... (SAVANT-2026)" | Fix | Unsourced. SAVANT-2026 only lists a booth demonstration. Clause removed |
| 7 | 09 | Checkpoint: "Outputs ... reviewed by the tax accountant; exceptions are handled by staff (Rover; Savant Claude)" | Fix | Unsourced connective claim. The Rover release describes no review step. Now "not described for Rover", plus Savant's generic exception routing |
| 8 | 09 | role_evolution: "so the monthly rebuild of the process is no longer manual work" attached to the Rover accountant | Fix | That framing is Savant's key-takeaway line, not the accountant's quote. Now attributed to Savant. A note records the release header date (6 Mar) against the dateline used (4 Mar) |
| 9 | 14 | Risk: "Clearance timing leaves little room for AI error; a wrong correction can repeat a rejection (TRINST)" | Fix | Unsourced connective claim. Not in the recap. Removed |
| 10 | 14 | "Sovos describes AI-powered mappings" (for e-invoice formats) | Fix | Sovos's mappings are "for tax determination and filing". Scope added |
| 11 | 15 | Problem: "Batch filing cycles surface errors late;" (no source) | Fix | Unsourced. Now attributed to EY's authors, who contrast continuous monitoring with batch filings (BTAX-EYGRIP-2025) |
| 12 | 18 | role_evolution: "Tax technology staff become owners of agent access, scopes and logs (AVALARA-MCP-2026)" | Fix | Unsourced connective claim. Avalara addresses developers and partners and says nothing about tax staff. Rewritten to say that, plus Sovos's own framing of agent-consumed compliance |
| 13 | 18 | "Avalara NEXT on 2026-03-26 was a virtual ... event" | Fix | The source is a pre-event announcement. Now "scheduled for" |
| 14 | 17, 18 | ANROK-MCP-2026 `access: search-only`; "Anrok is also reported to offer an MCP server" | Fix | Page reached through the text mirror. It says the server also *acts* (maps products, adds customers, updates transactions) under scoped OAuth 2.1. Access set to full; fact added to `#17` and `#18`; source added to `#18`; date left as `2026` (undated product page) |
| 15 | 24 | "59% were not sure whether their providers were using it (TR-TENSIONS-2025)" | Fix | Statistic reported as something it may not measure. The source reads "59% aren't sure if their companies are using GenAI". Now quoted, with a note that the blog frames it as a provider-transparency gap |
| 16 | 24 | role_evolution: "advisory work and oversight"; Deloitte's fourth scenario "splits planning between ... operations and tax advisory" | Fix | Embellished. EY says co-sourcing frees teams "to focus on advisory work" (no oversight). Deloitte's Scenario 4 says routine operations are largely automated, with more emphasis on strategic and advisory work |
| 17 | 22 | Problem: work "runs on spreadsheets, trackers and hand-offs that are slow to review and hard to scale (USTAXOPS)"; "AI tools for ... mappings (USTAXOPS)" | Fix | Generalisation from postings, and "mappings" comes from the other OpenAI posting. Now attributed to both postings, each for what it says |
| 18 | 23 | "Unilever Ice Cream's ... the company's tax transformation"; "A law professor argues" | Fix | The episode listing says the transformation and operations centre were *Unilever's*, discussed by Unilever Ice Cream's head of tax. The TaxProf page does not give Michael Sala's affiliation, so "law professor" was removed |
| 19 | 16 | "panelists said they know more..."; "in its high-adoption scenarios" | Fix | The recap reports one panel speaker. The preparation-to-oversight shift is in Deloitte's Scenario 4 only |
| 20 | 04, 14, 24 | "Vertex Exchange speakers said/described ..." | Fix | The hybrid-team and partner-led points are the recap's summary of the event message, not attributed speakers |
| 21 | 01 | "EY says best-in-class organisations centralise..."; "EY's own release says 44%" | Fix | The claim comes from the Bloomberg Tax write-up, which has no byline, not from EY's release. The 44% wording now matches EY ("inability to execute on a sustainable plan for data, AI and tech"). A note says the Fortive posting has expired and was read through the mirror, with no exact date shown |
| 22 | 07 | "Rising token costs were raised ..." | Fix | Token cost appears only in the recap's key-insights box, written by the Thomson Reuters author. Wording now says so, and that no figures are given |
| 23 | 11 | role_evolution: "Not described ... beyond staff reviewing extracted data (TEI-TAXTECH-2026)" | Fix | TEI-TAXTECH says nothing about reviewing extracted data. Replaced with EY's statement (BTAX-EYGRIP-2025) |
| 24 | 12 | OECD-FTA-2025 `access: full` | Fix | The page is behind a bot check on direct, mirror and archive routes. Marked search-only. The claim is now cited to the FTA Plenary Statement of Outcomes (new source OECD-FTA-STATEMENT-2025, copy hosted by Japan's NTA, PDF dated 2025-11-20). Wording now follows the statement: deepen real-time information sharing and back pilot projects |
| 25 | 19 | role_evolution: "Reviewers carry documented responsibility for AI-suggested positions" | Fix | Embellished. The register calls for mandatory human validation and a record of accepted, modified or rejected suggestions |
| 26 | 06 | Notes: "an aggregator copy, removed 2026-09-15" | Fix | The page is still live. 2026-09-15 is the `validThrough` date |

### Module

| # | Section | Before | Action | Reason |
|---|---|---|---|---|
| 1 | Intro, §1 | "Practitioners at the April 2026 TEI seminar said whether the tools work is 'effectively settled'; the open problems are ownership, silent failures, training and token cost" | Fix | Wrong speaker. Both the phrase and the list come from the Thomson Reuters author's key-insights box, not from practitioners |
| 2 | Intro | B-grade caveat named only #04 and #05 as not AI | Fix | Added that the named example behind #23 does not mention AI |
| 3 | §3 `#12` | "real-time transaction reporting replaces periodic returns (ViDA from 2030-07-01; UK from 2029)" | Fix | Wrong. The UK 2029 mandate is e-invoicing with no e-reporting to HMRC at first (FISCAL-UK-2026). ViDA's 2030 date applies to cross-border reporting |
| 4 | §3 `#09`, §5 | "Rover reports 80% ..." | Fix | Savant reports it in a vendor release. The table row also says what was timed is unclear |
| 5 | §3 `#23` | "Unilever Ice Cream's tax operations centre, podcast description" | Fix | It is Unilever's centre, and the source is a podcast episode listing that does not mention AI |
| 6 | §3 `#18` | "Avalara shipped servers" | Fix | Added Anrok's write-capable server |
| 7 | §4 probe 6 | "Most set none (12.5% have AI KPIs); no baseline means no business case" | Fix | Statistic reported as something it doesn't measure: KPIs are not acceptance thresholds. The second clause was an unsourced connective. Now framed as a proxy, with the survey population named |
| 8 | §4 probe 9, §9 | "Panelists said authorities arrive knowing more" | Fix | One panel speaker, speaking about mature continuous-transaction-control regimes. Scope restored |
| 9 | §4 probe 11 | "Token cost was raised at TEI" | Fix | It appears in the recap's key insights, not as an attendee statement |
| 10 | §4 probe 12 | "59% of departments are not sure" (whether providers use AI) | Fix | Same mismeasured statistic as `#24`. Now quoted |
| 11 | §5 | EY 44%: "naming an unsustainable data, AI and tech plan" | Fix | Mis-paraphrased. EY says "inability to execute on a sustainable plan for data, AI and tech" |
| 12 | §5 | Pega: "(2019, all industries)" | Fix | 509 RPA users in five named industries, none of them tax |
| 13 | §6 | IRS OPR "reaches in-house teams mainly through their providers" | Fix | Unsourced connective claim. Replaced with what the alert's scope supports |
| 14 | §6 | "Agentic corrections ... should be stored back" | Fix | Now attributed to Deloitte in Deloitte's own wording ("will need to be stored back ... audit-ready") |
| 15 | §7 | "tax technology staff own agent scopes and logs [AVALARA-MCP-2026]" | Fix | Unsourced connective claim (see use-case fix 12) |
| 16 | §7 | "A law professor argues" | Fix | Affiliation not stated in the source |
| 17 | §8 | OECD: "agree to move toward real-time automated information-sharing pilots [OECD-FTA-2025]" | Fix | Re-sourced to the statement of outcomes, with its wording |
| 18 | §8 | "Sovos announces it is acquiring Flowie" | Fix | The release says "announced the acquisition" and is headed "Sovos Acquires Flowie" |
| 19 | §9 | "only 20% measure ROI" | Fix | The figure is across professional services, not tax departments |
| 20 | §2 table | "A rejected invoice has no legal force in clearance regimes" | Fix | The source says an invoice has no legal force *until* the authority returns its identifier |

Verified and unchanged in the module: every §5 figure apart from those listed above (EY 51%, 73% and 89%; Bloomberg
80%, 91% and 53%→21%; TR 58%/51%, 15.4%, 88%/51% and 22%; KPMG DE 71%, 89%/29%, 66%, 47%/41% and 58%/72%; Fonoa 12.5%
and 57.4%; Deloitte 77% and 45%; TR 17/21/45%; TR ViDA 86%/22%; Sovos 1.6% vs about 20%; Column under a third; Bellon
over 5%); the COSO release date (2026-02-23) and six-step roadmap; Directive (EU) 2025/516 and the ViDA dates; France's
dates and its 10% penalty; the MCP specification wording; the NIST CAISI date; IRS OPR Alert 2026-19 (2026-06-24); the
AICPA CART date (2026-09-23); NIST AI 600-1 (July 2024) risk names; every frontier date. The note that "two Thomson
Reuters articles give different ViDA dates" is correct: TR-GOVERNANCE-2026 says 2028 and TRINST-TEIAUDITOR-2026 says
2030 and 2035.

## 4. Sources that couldn't be reached directly

| Source | Problem | Resolution |
|---|---|---|
| OECD-FTA-2025 (oecd.org announcement) | Cloudflare bot check on curl, the mirror (including browser mode) and the archive (Internet Archive was offline) | Marked search-only. Content confirmed from the FTA Plenary Statement of Outcomes PDF (nta.go.jp), added as OECD-FTA-STATEMENT-2025 |
| FORTIVE-JOB-2026 (The Ladders) | 403 on curl. The posting has expired | Full text read through r.jina.ai. No exact posting date shown, so the date stays `2026` |
| ANROK-MCP-2026 | 403 on curl | Read through r.jina.ai, access upgraded to full |
| GAO-2026, PWC-IE-2026 | 403 on curl | Read through r.jina.ai. Content confirmed |
| BELLON-PERU-2022 (PMC) | reCAPTCHA redirect | Read through r.jina.ai (pmc.ncbi.nlm.nih.gov). Abstract and introduction confirmed |
| Bloomberg Tax/Law articles (BTAX-EYTFO-2026, BTAX-EYGRIP-2025) | Paywall shell in direct HTML | Full body read through r.jina.ai |
| COSO publication itself | Not opened (already disclosed in `#20` notes) | Two secondary summaries (DART, JofA) confirm the cited points |

## 5. Targets

| Target | Status |
|---|---|
| 15–25 use cases | Met (24) |
| At least 50% graded A or B | **Not met:** 8 of 24 (33%), and 3 of the 8 are not AI evidence. Zero grade A. No measured outcome from a named organisation exists apart from Savant's vendor-published Rover figures |
| Every source dated | Met. Every source has a URL and an ISO date. Year-only dates remain where the page is undated (Fortive, Anrok, KPMG-Snowflake 2023) |
| Vocabulary values, unique ids, quotes under 25 words | Met. The validator passes, ids are unique, and the longest quotation is 15 words |

## 6. Error patterns to fix in the briefs

1. **Recap author's summary passed off as practitioners' words.** Thomson Reuters Institute recaps carry a "Key insights"
   box written by the author ("effectively settled", "rising token costs"). Briefs should require attributing these to
   the recap author, not to "practitioners", "attendees" or "speakers". The same applies to the "message from the event"
   lines in conference recaps (Innovate Tax).
2. **One speaker becomes "panelists".** Singular anecdotes were pluralised, and their scope (mature CTC regimes) was
   dropped. Briefs should say: keep the number of speakers and the jurisdictional scope exactly as stated.
3. **Phrases migrate between sources.** The "assembling information to applying judgment" line was attributed to PwC
   Ireland when it is EY's. The same phrase was misattributed in compliance-corporate. Before citing a distinctive phrase,
   grep it in the cited source's text.
4. **The Thomson Reuters "59% aren't sure" statistic keeps being restated as "not sure whether providers use AI".** This is
   the second module where it happened. Add it to a known-traps list: quote it verbatim.
5. **Unsourced connective sentences in `human_checkpoints`, `risks_and_guardrails` and `role_evolution` still appear.**
   Examples here: an invented review step for Rover, "clearance timing leaves little room", tax staff owning MCP scopes,
   OPR reaching in-house teams through providers. Briefs should require that every sentence in these fields carries a
   source whose text supports that sentence, not just the topic.
6. **Vendor marketing lines turned into controls or facts.** "Easily verifiable by any reviewer" became a review
   checkpoint. "Identified 100+ streams" became "built 100+ streams". "Expanded" connectors became "added".
7. **Regime facts generalised.** "Real-time reporting ... UK from 2029" ignored that the UK model has no e-reporting to
   HMRC at first. Briefs should ask for the reporting model (clearance, e-reporting, or exchange only) to be checked
   alongside the date.
8. **Search-only status not revisited.** Anrok was left as search-only although the page was reachable through the
   mirror. Briefs should require one mirror attempt before settling on search-only.
9. **Credentials added that the source doesn't give** ("law professor"). Use only the role the source states.

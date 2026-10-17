# Verification report: security / threat-intelligence

- **Verified:** 2026-10-17 (verifier brief `verify-threat-intelligence.md`, wave 4)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/threat-intelligence.yaml` (24 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/threat-intelligence.md` (285 lines)
- **Method:** I pulled all 127 distinct URLs from the two files and reopened every one with `curl` in a private working folder.
  - I used `pdftotext` for the ENISA, NIST and arXiv PDFs. Full papers were read where an entry relied on more than the abstract (SoK 2609.01174, CyberThreat-Eval 2603.09452, DarkBot 2608.23185).
  - I used the `r.jina.ai` mirror for pages that returned 403: SecurityWeek, CyberProof, SC Media, Coinbase, the OpenAI Ashby postings, cisa.gov and gao.gov.
  - I took dates from `article:published_time`, JSON-LD, `published-date`, Microsoft `ms.date`, Greenhouse `published_at`, arXiv submission history and PDF metadata.
  - I spent one web search on finding another route to the blocked DHS inventory.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. For this module it gives `INFO ... 24 use cases, 14 graded A/B (58%)`. All the warnings belong to other modules.

## 1. Counts

| | Use cases |
|---|---|
| Kept as written | 6 (`#05`, `#10`, `#15`, `#17`, `#18`, `#20`) |
| Fixed | 18 (`#01`–`#04`, `#06`–`#09`, `#11`–`#14`, `#16`, `#19`, `#21`–`#24`) |
| Rejected | 0 |

The 18 fixes break down as follows:
- **10 substantive fixes:** an unreachable source re-sourced, a figure attributed to the wrong document, a feature claimed as implemented when the source only recommends it, a misattributed problem statement, or an unsupported qualifier.
- **8 smaller fixes:** dates, locators, or wording in `role_evolution` and `problem` that went beyond the source.

The module received 5 sets of edits.

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 2 (21, 22) | 2 (unchanged) |
| B | 12 | 12 (unchanged) |
| C | 8 | 8 |
| D | 2 (01, 07) | 2 |

- **`#21` (Grow Therapy) stays A.** The post says token use and cost are logged for each hunt and reported weekly, so the cost table counts as tracked data. The noise shares are labelled as the team's own estimates. The undated post's date is now "2026" (it had been "2026-08", which was a guess).
- **`#22` (Microsoft DTDA) stays A.** Microsoft reports 80.1% precision from customer feedback over 120 days of its own deployment. It is labelled vendor-published.
- **`#13` and `#23` stay B, but on new sources.** The DHS inventory they relied on could not be reached. Both now rest on CISA's own AI use-case page (December 2024 refresh), and `#13` also on GAO-24-106246. `#23` was rewritten so its grade rests on the Einstein capability (DHS-2403), which CISA lists as in operation. CyberSentry (DHS-106) is listed only at the initiation stage.
- **No other grade changes.** No A or B entry uses a search-only source, and every source is `access: full`. No A or B entry depends on evidence from an adjacent process. `#22` and `#23` sit close to security operations, but both are threat hunting, which this module covers.

**Ladder (unchanged):** assist 2, augment 14, automate 3, delegate 5. **Change scope (unchanged):** step 10, process 13, model 1.

## 3. Fixes and rejections

### Use cases

| # | Entry | Before | Action | Reason |
|---|---|---|---|---|
| 1 | 01 | "so teams struggle to know which requirements are covered by which sources"; "analyst capacity is flat" | Fix | Embellished. Flashpoint says capacity "remains constrained" and says nothing about coverage mapping. The clause was removed |
| 2 | 01 | Risk: "Interviewees want read-only assistants, reviewable output, reversible actions and clear success criteria" | Fix | Overgeneralized. Only one retail interviewee wanted read-only assistants. Reviewable and reversible tasks are Flashpoint's own recommendation, not an interviewee demand |
| 3 | 01 | RF-PRACTITIONER-2025, dated "2025", "page undated" | Fix | Wrong date. The page carries `published-date` 2026-01-09, the same metadata used for the other Recorded Future pages. Ref renamed RF-PRACTITIONER-2026 |
| 4 | 02 | "Collecting and enriching open-source and leak data by hand does not scale (Apura abstract)" | Fix | Not in the abstract. Replaced with the session's own framing, "Beyond Manual Hunting … at Scale" |
| 5 | 03 | Prerequisite: "legal access to the underground data" (Apura abstract) | Fix | Unsupported. The abstract covers extraction, enrichment and indexing only |
| 6 | 04 | "the abstract does not say what review was done"; "legal and ethical questions the source does not resolve" | Fix | Incomplete. The full paper reports approval from a Research Ethics Committee, GDPR handling and constrained deception (§IX). These were added; note and locator updated |
| 7 | 06 | "the public catalogue of more than 200 attacker techniques … the mapping is what lets teams compare actors and drive detection (MITRE-TRAM-2023)" | Fix | Attributed to the wrong document, plus an unsourced clause. TRAM says the mapping is "difficult, error-prone, and time-consuming". The technique count now cites ATT&CK v20 (227 Enterprise techniques). "Latest work" changed to "2023 project" |
| 8 | 07 | "ANCHOR, which runs a local model" | Fix | Embellished. The abstract says a local-model option closely matched enterprise LLMs |
| 9 | 08, 11 | Notes: "Google's blog also says … 139% more threats … 46% more efficient CTI teams (IDC)" | Fix | Attributed to the wrong document. Neither figure appears in GOOGLE-DARKWEB-2026 (checked in the text and the raw HTML). Removed |
| 10 | 08 | Forrester: black-box triage fails "on accuracy and efficiency" | Fix | Misquoted. Forrester wrote "effectiveness" and efficiency |
| 11 | 09 | DHS-107 "in pre-deployment … produces a report they use"; notes "classical or predictive ML, not generative AI" | Fix | The source could not be reached (dhs.gov 403). Re-sourced to CISA-AIUC-2024, which shows the initiation stage, deep learning, and generative AI among the listed techniques. The report-production claim and the "not generative" classification were removed |
| 12 | 11, 14 | MSFT-MDTICOPILOT-2026 dated 2026-08-02 | Fix | Wrong date. The page's `ms.date` is 2026-07-30 (updated 2026-09-23) |
| 13 | 11 | CRWD-CHARLOTTE-2026 dated 2026-10-17 as "undated" | Fix | The page has JSON-LD dateModified 2026-09-14 |
| 14 | 12 | "26% say it significantly influences" cited to the press release | Fix | Attributed to the wrong document. "Significantly" appears on the SANS key-findings page (SANS-CTI-2026), not in the press release |
| 15 | 12 | CISA drafting tool (DHS-2335) and CISAChat "deployed", cited to DHS | Fix | DHS could not be reached. Re-sourced to CISA-AIUC-2024: drafting tool at initiation, CISAChat at implementation and assessment (December 2024). RF-PUBSECTOR locator corrected to the AI section |
| 16 | 13 | PII screening cited to DHS; DHS-5 "retired and consolidated"; "inventory classifies as NLP" | Fix | DHS could not be reached. Re-sourced to CISA-AIUC-2024 (DHS-4 in operation, natural-language processing) and the GAO-24-106246 audit, which confirms analysts review flags and that CISA built metrics in September 2024 but published no values. The DHS-5 retirement could not be checked and was dropped. A GAO-based prerequisite was added |
| 17 | 16 | Title and solution: the pipeline "also rechecks earlier intelligence"; circuit breakers presented as Adobe's design | Fix | The source recommends this rather than saying Adobe built it. Both appear in Adobe's guidance on "how security teams can approach building a similar system". The text now presents them as recommendations |
| 18 | 19 | "BSides Las Vegas 2026 ran a workshop" | Fix | The source is a talk list. Changed to "listed" |
| 19 | 19 | MSFT-HUNTASSIST-2026 dated 2026-09-10 | Fix | That is the update date. Changed to `ms.date` 2026-07-02, consistent with the other Microsoft Learn sources |
| 20 | 21 | GROWTHERAPY-HUNT-2026 dated "2026-08" | Fix | The post is undated. Changed to "2026", noting it was published by 2026-08-19 (DEW #167) |
| 21 | 21 | role_evolution: Risky Business segments "argue the data layer is the lever" | Fix | Embellished. Corelight's segment *asks whether* model or data matters more. Nebulock frames security as a data problem |
| 22 | 22 | role_evolution: agent fills gaps "for analysts, not replacing them" | Fix | Unsourced qualifier. "Not replacing them" is not on the Microsoft page |
| 23 | 23 | Whole entry: CyberSentry DHS-106 "deployed"; "terabytes of daily network log data" cited to DHS-106; "not generative AI" | Fix | DHS could not be reached, and the claim was attributed to the wrong item. On CISA's page the terabytes statement belongs to DHS-2403 (Einstein), which is in operation. DHS-106 is at initiation. The entry was rewritten on CISA-AIUC-2024; B rests on DHS-2403 |
| 24 | 24 | Checkpoint: "Investigators and analysts remain responsible for assessments" | Fix | Inference. The posting says engineers build tools with and for analysts and investigators. Reworded |

### Module

| # | Section | Before | Action | Reason |
|---|---|---|---|---|
| 1 | §3 Action | `#16` "rechecks old intelligence" | Fix | The recheck is Adobe's recommendation, not something its platform is said to do |
| 2 | §3 Hunting | `#23` "CISA CyberSentry machine-learning anomaly surfacing" | Fix | Matches the rewritten entry: Einstein capability in operation, CyberSentry at an early stage |
| 3 | §6 human judgement | "approving any write to live tooling (blocklists, rules, containment) [SECURITYWEEK-HUNTING-2026]" | Fix | Statistic reported as something it doesn't measure. SecurityWeek's experts say low-risk actions such as blocking IPs *can* be automated (tiered automation). The approval rule is now cited to Feedly, and SecurityWeek is described accurately |
| 4 | §6, §9 | [DHS-AIINV-CISA-2026] for the CISA PII review | Fix | The source could not be reached. Replaced with [CISA-AIUC-2024; GAO-24-106246] |
| 5 | §8 | "2026-08-12 to 2026-09-16: Google ships … an Agentic MCP server" | Fix | 2026-09-16 is the guide's last-modified date, not a ship date. Reworded |

Every other module figure, benchmark, regulatory statement and frontier signal was traced to its source. These include:
- the SANS figures (91/26, 57/49, 44, 45/32, 55, 71) and the Flashpoint figures (65/55, 25/20/35);
- the SoK practitioner and experiment numbers;
- the CTI-REALM, TRA, DTDA and Grow Therapy figures;
- the TLP, NIST 800-150, NIST CSF, NIS2 Art 29 and recital 51, DORA Art 45 and DORA RTS 2025/1190 statements;
- the CISA 2015 extension to 2026-09-30, read on cisa.gov through the mirror;
- the GTIG figures (62% zero-days, under six hours), the CERT-In "days to a few hours" claim, ATT&CK v20 (2026-10-13), ISC2 41% and the Nextgov AI-ISAC report.

## 4. Sources that could not be reached

- **DHS AI Use Case Inventory, CISA page** (`https://www.dhs.gov/ai/use-case-inventory/cisa`, DHS-AIINV-CISA-2026). It returned HTTP 403 directly, through `r.jina.ai` (Akamai "Access Denied") and through archive.ph (429). The Wayback Machine was blocked by the proxy. I found another route:
  - CISA's own page `https://www.cisa.gov/ai/cisa-use-cases` (December 2024 refresh, read through the mirror once its temporary block lifted);
  - GAO-24-106246 (2024-02-07).

  Claims found only in the 2026 inventory (DHS-106 deployed, DHS-2403 and DHS-5 retired, "classical ML, not generative AI") could not be confirmed and were removed or flagged in notes. The ref no longer appears in either file.
- **Partially read:** USENIX log-injection paper (abstract on the sessions listing only) and the CyberProof PDF (page text read; PDF date not opened; the image upload paths in July 2026 support "2026-07").
- Everything else was reached. The 403s for SecurityWeek, CyberProof, SC Media, Coinbase, cisa.gov AIS, and the empty Ashby shells, were all read through the mirror. The Coinbase posting dates were confirmed through the Greenhouse boards API.

## 5. Targets

| Target | Result |
|---|---|
| 15–25 use cases | Met: 24 |
| At least 50% graded A or B | Met: 14 of 24 (58%) |
| Every source dated | Met. Every source has an ISO date. Four undated pages use the retrieval date (CTID TRAM README, cisagov/imx README, Recorded Future AI page, CISA AIS page) and say so in the locator. The Grow Therapy post is dated to the year |

Format: all vocabulary values validate, the 24 ids are unique, every source has a URL and a date, and no quotation reaches 25 words.

## 6. Error patterns to fix in the briefs

1. **Unreachable government inventories.** dhs.gov blocks both curl and the mirror. The synthesis relied on one DHS page for four entries. Briefs should ask researchers to record a second route (the agency's own page, GAO or OIG) whenever a government source is the only support for a B entry.
2. **Attributed to the wrong document (3 cases).** IDC figures were placed in a Google blog that does not contain them. "Significantly influences" came from the SANS landing page, not the press release. A technique count was cited to the TRAM page. Ask synthesizers to grep the cited page for every number before writing it down.
3. **Recommendations reported as implementation (Adobe, Feedly-style guides).** Vendor and firm blogs often move from "what we built" to "what you should build". Briefs should require a locator that shows which of the two a claim comes from.
4. **Unsourced qualifiers in `role_evolution` and checkpoints.** Examples: "not replacing them", "remain responsible for assessments", "argue the data layer is the lever". These are the pilot's connective-claim pattern again. Ask for the source's verb ("asks whether", "describes").
5. **Abstract-only reading of key papers.** The DarkBot entry said legal and ethics review was "not addressed" when the full paper has an ethics section. When an entry asserts that a source does *not* cover something, the full text must be checked.
6. **Dates.** The errors were a guessed month for an undated post, a modified date treated as a ship date (Google MCP), and inconsistent Microsoft Learn dates (`ms.date` vs `updated_at`). Set one rule per platform in the vocabulary file: Microsoft Learn = `ms.date`; readme.io docs = `dateModified`, labelled as such.
7. **A misread statistic in the module.** SecurityWeek was cited for a stricter rule (approve every write) than it states (tiered automation). Module-only citations need the same check as YAML citations.

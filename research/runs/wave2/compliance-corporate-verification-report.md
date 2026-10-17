# Verification report: tax / compliance-corporate

- **Verified:** 2026-10-17 (verifier brief `verify-compliance-corporate.md`, wave 2)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/use-cases/compliance-corporate.yaml` (24 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/compliance-corporate.md` (270 lines)
- **Method:** I extracted all 71 distinct URLs cited in the two files (65 in the YAML, 6 more in module §10) and reopened every one with
  `curl` in a private working folder. I used `pdftotext` for the 5 PDFs (Werfel appendices, Deloitte TTT, TEI Midyear agenda, TIGTA,
  TaxCalcBench full paper) and the `r.jina.ai` text mirror for the 8 pages that returned 403 (six `pro.bloombergtax.com` pages, GAO,
  Wolters Kluwer) and for the paywalled Bloomberg Tax news articles. I checked each figure, date, attribution and quotation against
  the page text. For dates I checked `article:published_time`, JSON-LD, `firstpublishdate`, on-page bylines, arXiv submission history
  and PDF metadata.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. For this module it gives `INFO ... 24 use cases, 3 graded A/B (12%)`
  and the expected WARN that the A/B share is below 50%. The other warnings belong to other streams' files.

## 1. Counts

| | Use cases |
|---|---|
| Kept as written | 6 (`#02`, `#06`, `#08`, `#14`, `#16`, `#24`) |
| Fixed | 18 (`#01`, `#03`, `#04`, `#05`, `#07`, `#09`, `#10`, `#11`, `#12`, `#13`, `#15`, `#17`, `#18`, `#19`, `#20`, `#21`, `#22`, `#23`) |
| Rejected | 0 |

The 18 fixed entries break down as follows:
- **11 substantive fixes:** wrong date, misattribution, an unsupported quotation, an inflated grade, attribution of workflows to the
  wrong party, or a statistic described as something it doesn't measure.
- **7 wording or connective-claim fixes:** unsourced sentences in `role_evolution` or `problem`, or "ran/held" changed to "scheduled"
  for a preliminary conference programme. `#05` changed only through the EY ref and date fix.

No entry was rejected. Every cited source exists and was reached, directly or through the mirror. Every entry's core claim is
supported once corrected.

The module received 21 edits.

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 0 | 0 |
| B | 4 (02, 07, 10, 18) | 3 (02, 07, 10) |
| C | 16 | 17 (`#18` added) |
| D | 4 (16, 22, 23, 24) | 4 (unchanged) |

- `#18` moved from B to C. Its only named deployment is PwC's effective-tax-rate model, which is ASC 740 provision work. The module
  excludes provision, so this was a grade inflated by evidence from an adjacent process.
- `#02` stays at B. K-1 footnote interpretation is a step in this module's own process table (source-document intake), even though
  PwC's example comes from asset and wealth management. The adjacency is already disclosed in the entry.
- `#10` stays at B with corrected wording. The source is a vendor press release that names Oxford Industries' tax team and its
  Senior Director as co-presenter. That is a named deployment, but the release does not say which workflows Oxford uses.
- `#07` stays at B. The TEI recap confirms that OpenAI's tax department demonstrated live automation pipelines. The agent-driven
  return computation is a stated aim in job listings, and maturity remains `piloting`.
- No A or B entry uses a search-only source. Every source is `access: full`.

**Ladder (unchanged):** assist 5, augment 12, automate 3, delegate 4. **Change scope (unchanged):** step 12, process 8, model 4.

## 3. Fixes and rejections

### Use cases

| # | Entry | Before | Action | Reason |
|---|---|---|---|---|
| 1 | 01, 03, 05 | `EY-COMPL-2026`, dated 2026-02-12 | Fix | Wrong date. The page's own `firstpublishdate`/`dateuser` metadata and on-page date are 22 Jul 2024. 2026-02-12 is a republication timestamp in JSON-LD. Ref renamed to `EY-COMPL-2024` in both files |
| 2 | 01 | role_evolution: "EY says the work moves from assembling information to applying judgment (EY-COMPL-2026)" | Fix | Wrong document. The phrase comes from the EY authors' Bloomberg Tax op-ed (EY-BTAX-2025), not the EY insight page. Re-sourced, and EY-BTAX-2025 added to the entry's sources |
| 3 | 01 | "Bloomberg Tax says mapping errors can compound across entities" | Fix | Embellished. The page says corporate tax *calculations* in multi-entity structures can see errors "compound exponentially"; it does not mention mapping |
| 4 | 01 | "mapping logic in Alteryx workflows that nobody could explain" | Fix | Embellished. The recap says "Alteryx workflows nobody could explain because the person who built them had left the company without documenting the logic". It does not say mapping |
| 5 | 03 | Deloitte anomaly-flagging agents "as a lower-risk start" | Fix | Embellished qualifier. Deloitte gives them as an example of "immediate risk mitigation" in its low-adoption Scenario 1 |
| 6 | 04 | Title: "first-level review of automated compliance results" | Fix | Adjacent process. The OpenAI listing says "first-level review and validation of automated provision outputs and data pipelines". Title now says "automated outputs" |
| 7 | 07 | Checkpoint: "first-level review and validation of automated outputs" | Fix | Same listing. Now names provision outputs and data pipelines |
| 8 | 09 | role_evolution quoted Baker Tilly on moving tax teams away from "find and replace" work | Fix | Unsupported quotation. The phrase is not on the Baker Tilly page (checked in both the parsed text and the raw HTML). Replaced with what the page says, and the unsourced closing sentence was replaced with a TR-CORPAI-2026 statement |
| 9 | 09 | "Baker Tilly and EY describe the same shift from interviews and timesheets…" | Fix | EY was not among the sources, and the EY insight page has no R&D content. Now Baker Tilly for the shift, plus EY-BTAX-2025 ("AI is being woven into R&D platforms…"), which was added as a source |
| 10 | 09, 11, 15, 17 | TEI Midyear "ran"/"held"/"offered" labs and sessions; source dated 2026-03 | Fix | The source is a *preliminary* programme (PDF created 2026-02-09), so it shows what was scheduled, not what took place. Wording changed to "scheduled" and date changed to 2026-02. TEI-MIDYEAR-2026 added to `#11`'s sources, since its text relied on it |
| 11 | 10 | Title and solution: Oxford's tax team "runs governed AI automation of data extraction, multi-system reconciliation and reporting with lineage", "with demonstrations of…" | Fix | Claim attributed to the wrong party. In the release, those demonstrations are Savant's booth demos, listed separately from the Oxford session. The release never says which workflows Oxford uses. Title, solution and notes rewritten; grade B kept for the named team |
| 12 | 10 | Problem: "When an agent corrects data on its way into the return, the correction can exist only in the tax tool…" | Fix | Unsourced connective claim. Removed; Deloitte's write-back point is kept, with its citation, in the solution |
| 13 | 11 | BTAX-ASC740-2026 dated 2026-03 | Fix | The page is undated (jina shows no published time; only a 2026 copyright line). Date changed to 2026 and noted in the locator |
| 14 | 12 | Problem: "Section G and the first GloBE Information Return… compressed the direct-tax calendar" | Fix | Unattributed. Now attributed to Thomson Reuters ("unusually compressed filing environment") |
| 15 | 12 | role_evolution: "Technical staff review change reports instead of searching sources by hand" | Fix | Unsourced connective claim. Replaced with the source's statement that Tax Flows distributes comparison reports to stakeholders (TR-CORPAI-2026) |
| 16 | 13 | "authorities increasingly arrive at audits already holding structured data" | Fix | Scope dropped. The panellist was speaking about continuous-transaction-control jurisdictions, which are mostly indirect tax. That qualifier is now included |
| 17 | 13 | Risk on redacted authority models had no source; note said "GAO date comes from the landscape" | Fix | Redaction now cited to TIGTA-2025. The GAO date (24 Mar 2026) was confirmed from the report PDF through the mirror, and the note was updated |
| 18 | 15 | "59% are not sure whether they [providers] do" | Fix | Statistic reported as something it may not measure. The source sentence reads "59% aren't sure if their companies are using GenAI". The entry now quotes it and says the vendor frames it as a provider-transparency gap |
| 19 | 15 | Risk: "Disclosure may reveal provider methods or conflict with provider confidentiality"; role_evolution "Tax directors act as informed buyers…" | Fix | Unsourced connective claims. The risk was removed, and role_evolution now rests on TR-TENSIONS-2025 and IRS-OPR-2026 |
| 20 | 17 | "Tax technology teams are small" | Fix | Unsourced. Removed |
| 21 | 18 | Grade B; problem: "Clients and auditors ask whether AI-prepared tax work will hold up under scrutiny" | Fix | Grade inflated by an adjacent process (see §2). Wrong speaker: in the interview the question is the CFO's, about "IRS scrutiny". Grade changed to C and wording corrected |
| 22 | 19, 20, 21 | role_evolution described role changes with no source | Fix | Unsourced connective claims. Now attributed to OPR, EY-BTAX and the Werfel worked example (governance owner, quality review lead, override monitoring), or marked "not described in the sources" |
| 23 | 22 | "Auditability, not raw accuracy, is argued to be the bottleneck" (JHU-TAXREASON-2025) | Fix | Embellished. The abstract says automated tax systems "must deliver high accuracy and auditability". It does not rank one above the other |
| 24 | 22, 23 | role_evolution described future roles with no source | Fix | Unsourced. Now "Not described in the sources." |
| 25 | 23 | Note: "Preprint, not peer reviewed as far as the page shows" | Fix | Wrong. The arXiv page says the paper was accepted for ICTAI 2026 (IEEE) |

### Module (`compliance-corporate.md`)

| # | Section | Before | Action | Reason |
|---|---|---|---|---|
| 1 | Header | "4 of 24 entries are grade B" | Fix | Now 3, after the `#18` regrade |
| 2 | §1 | "Practitioners… described the question as no longer 'does it work?' but governance, ownership and cost" | Fix | Wrong speaker. This is the recap author's key-insights summary, not something practitioners said. Now attributed to the Thomson Reuters Institute recap, with the problems it lists |
| 3 | §2 table | "EY states 63% still gather ERP data manually and 76% rely heavily on Excel [EY-COMPL-2026]" | Fix | Wrong document. The figures are not on the EY page; they appear on the Baker Tilly page (BAKERTILLY-2026, "Compliance modernization"). Re-sourced |
| 4 | §2 table | Calendar pain: "Spreadsheets" (unsourced) | Fix | Now sourced to the OpenAI 2026 listing ("moving away from spreadsheet trackers") |
| 5 | §2, §7 | `[EY-COMPL-2026]` (3 places) | Fix | Ref renamed to EY-COMPL-2024 (date fix) |
| 6 | §3 | `#10`: Oxford "runs governed reconciliation and extraction with Savant, with lineage and an audit trail" | Fix | Workflows attributed to Oxford are Savant's booth demos (see YAML fix 11) |
| 7 | §3 | `#18` "(grade B, provision-adjacent)" | Fix | Now grade C, with the reason |
| 8 | §3 | `#07`: OpenAI's team "moves from outsourced preparation to agent-driven computation" | Fix | Overstated. The listings state an aim. Now "sets out to move", with the demonstration described as automation pipelines |
| 9 | §3 | `#09`: "populates Form 6765 with Section G [TR-NEOTAX-2025]" | Fix | The Section G population claim is in TR-CORPAI-2026, not the 2025 blog. Citation added |
| 10 | §4 probe 1 | "the bottleneck is data (the usual answer [KOGNITOS-2026])" | Fix | Overstated. This is one vendor's argument. Now attributed as such |
| 11 | §4 probe 8 | "59% of business tax departments are not sure" (about providers) | Fix | Same ambiguity as YAML fix 18. The probe now gives the source's wording |
| 12 | §4 probe 10 | "Most have not [measured anything]" | Fix | Overstated and contradicted by newer data. TR-TENSIONS gives 20% measuring GenAI ROI across professional services, while TR-TAXTALENT-2026 says two-thirds of tax departments measure time savings. Both are now given |
| 13 | §5 table | (missing) | Fix | Added the TR-TAXTALENT-2026 measurement figures (two-thirds; 55%) so the table does not imply that nobody measures |
| 14 | §6 | Section G: "report at least 80% of QREs or up to 50 business components" | Fix | Wording tightened to the instructions: at least 80% of QREs by business component, but no more than 50 components |
| 15 | §6 | "Werfel's 20-risk framework" | Fix | Statistic reported as something it doesn't measure. The 20-risk register is for tax authorities; the preparer register, which is the relevant one here, has 15 risks. Both are now named |
| 16 | §6 | PCRT: "AI supports, not replaces, judgment; public tools with client data likely breach confidentiality" | Fix | Paraphrase drifted from the source and dropped "without consent". Now: members remain responsible and must apply professional judgement; entering client data into a public model *without consent* is likely a breach |
| 17 | §8 | "2026-03: TEI Midyear runs hands-on Tax Labs" | Fix | The source is a preliminary programme. Now "schedules" |
| 18 | §8 | "2026-06-24: IRS OPR issues its first AI alert" | Fix | "First" is not supported by the source. Now "issues Alert 2026-19, introductory guidelines" |
| 19 | §8 | "2026-09-23: AICPA launches CART; the AICPA challenges OPR's fee language" | Fix | Wrong date. The fee challenge was reported on 2026-09-08 (AICPA-FEE-2026). Split into two dated bullets |
| 20 | §10 | TR-CORPTECH-2026 titled as the report itself | Fix | The cited page is a TRI article about the report. Title corrected |
| 21 | §10 | CSC-BAXTER-2026 dated "undated" | Fix | Format violation ("never 'undated'"). Now 2026, flagged as the retrieval year (the page's copyright year is filled in by script), and noted that the case refers to Transition Tax work, so it is likely older |

### Checked and confirmed (no change)

These were checked and confirmed:
- PwC interview: K-1 agents, the 70% confidence example, three people replaced by one reviewer, Agent OS, 800 GPTs and 250 agents,
  3,200 champions, 350,000 hours, 80% trained, the ETR model and locked logic.
- OpenAI listings: dates, quotations, Project Hive, under 12 months, 10+ years, Corptax and ONESOURCE.
- Byron (>97% extraction, SOC 2, no training on customer data).
- KPMG and Anthropic (weeks to minutes, 276,000 people).
- EY 150 agents and 80,000 staff (Bloomberg Tax, 2025-03-24).
- EY Tax Labs and Agent Factory (2025-11-25).
- Neo.Tax: 200+ hours, 10%+ adjustments, $100k–$500k fees, weeks to days, 150+ hours, 50–75% and 20–30% "companies report".
- Form 6765 instructions (12/2025): Section G optional before 2026 and required after 2025; QSB, $1.5M and $50M exceptions; 80%/Top 50.
- Treas. Reg. 1.6694-1(e)(1) and 1.41-4(d).
- OPR Alert 2026-19 sections 10.22, 10.27, 10.35, 10.36, 10.37, 6713 and 7216, and its best practices.
- Werfel thresholds: 2%/60 days, 1%/90 days, <5% override, >2% suspension, 60-day and 24-hour notices, the annual unaided check.
- TIGTA LAR: March 2021, $10M–$250M, unsupervised, human classifiers, no outcome data, nearly 50% no-change in DAS.
- GAO: 126 use cases.
- Clinco: three of four citations, "recipe for sanctions", no formal sanction.
- TR survey figures: 67%, 58%/51%, 56% vs 31%, 288 departments; 17/21/45%, 77/59%, 20%; 34%/56%, 50%/59%, 62%, 57%, 9%.
- 67% and 170 leaders; KPMG Germany 71/66/89/29/47/41/41/58/72.
- Deloitte LU 77%; RSM 48/16/7/36 and 48/44/43; Fonoa 176, 57.4%, 12.5%, one-third.
- TaxCalcBench 32.35% (Gemini 2.5 Pro, strict, 51 TY2024 cases, 4 runs); Law&Order 100% vs 66%; DeonticBench 44.4%;
  Sadowski 63–76% and ≤5 pp.
- Baxter 200+ reports, 2 h vs 80 h.
- All remaining dates match their sources' metadata.

## 4. Sources that couldn't be reached directly

| Source | Problem | Route used | Result |
|---|---|---|---|
| BTAX-CORPAI-2026, BTAX-LEVERAGE-2026, BTAX-HALLUC-2026, BTAX-TOOLS-2026, BTAX-FORUM-2026, BTAX-ASC740-2026 (`pro.bloombergtax.com`) | 403 to curl | r.jina.ai mirror | Read in full. Published times confirmed except BTAX-ASC740 (undated) |
| GAO-2026 | 403 | Mirror of the product page and of the report PDF | Read. 24 Mar 2026 confirmed from the PDF |
| WK-CORPRES-2026 | 403 | Mirror | Read in full; 2026-04-02 confirmed |
| BTAX-BIG4-2025, BTAX-PRICING-2026, EY-BTAX-2025 (`news.bloombergtax.com`) | Paywall after the opening | Mirror | The cited passages were all visible. EY-BTAX was read to the end |
| SALA-TAXNOTES-2026 | Tax Notes body paywalled | TaxProf Blog abstract | Abstract only, as the entry already states |
| FONOA-2026 | Full report gated | Landing page | Landing page only, as the entry already states |
| web.archive.org CDX API | Connection reset | none | Undated pages (CSC Baxter, CSC Salesforce, Corptax webinar, TR Neo.Tax product page, BTAX-ASC740) could not be dated. Each carries a year that is the retrieval or copyright year, and this is flagged |

No source was unreachable by every route.

## 5. Targets

| Target | Result |
|---|---|
| 15–25 use cases | **Met** (24) |
| At least 50% graded A or B | **Not met.** 3 of 24 (12%), down from 4 (17%). Grades were not raised to reach the target |
| Every source dated | **Met in format**: every source has an ISO date and a URL. Five dates are year-only stand-ins for undated vendor pages (retrieval or copyright year, not publication), and are flagged |
| Unique ids, vocabulary values | Met (24 unique ids; validator reports 0 errors) |
| Quotations under 25 words | Met (the longest quotation is the OpenAI "classify, compute, reconcile, and report" fragment) |

## 6. Patterns of error to fix in the briefs

1. **Republication dates taken as publication dates.** EY's insight page carries a 2026 JSON-LD `datePublished` over a 2024
   `firstpublishdate` and on-page date. Briefs should require checking `firstpublishdate`/`dateuser` and the visible date when they
   conflict with JSON-LD, and should treat a page that cites old surveys as a warning sign.
2. **Figures attributed to the wrong document when two sources sit side by side.** The 63%/76% figures came from Baker Tilly but
   were credited to EY. The "assembling information to applying judgment" line came from the EY op-ed but was credited to the EY
   insight page. Briefs should require a string search of the cited page for every number and quoted phrase before writing the
   source key.
3. **Unsupported quotations.** The Baker Tilly "find and replace" quote does not exist on the page. Quotation marks should be used
   only for text found verbatim in the saved page text.
4. **Vendor-release content transferred to the named customer.** Savant's booth demos were written up as Oxford's workflows.
   Briefs should require separating what a release says the customer does from what the vendor demos or sells.
5. **Adjacent-process deployments carrying a B.** PwC's ETR model is provision work but was graded B in this compliance module.
   Briefs should state that a named deployment in an excluded module's process caps the entry at C here, and should say in which
   module it can count as B.
6. **Preliminary programmes and pre-event releases written as events that happened** ("ran", "held", "co-presented"). Briefs
   should require "scheduled" or "announced" unless a recap confirms the event.
7. **Scope qualifiers dropped.** "In CTC jurisdictions" became "authorities increasingly". "Without consent" disappeared from
   PCRT. "Preparer register" became "20-risk framework". "Provision outputs" became "compliance results". Briefs should list
   these as a check: copy the source's own scope words into the claim.
8. **Unsourced connective sentences in `role_evolution`, `problem` and `risks_and_guardrails`.** There were ten such sentences
   across eight entries. The synthesis brief should require that each sentence either carry a source key or read "Not described in
   the sources."
9. **Ambiguous survey wording smoothed into a clean statistic.** TR's "59% aren't sure if their companies are using GenAI" was
   restated as "not sure whether providers use it". Briefs should require the source sentence verbatim in `measures` whenever its
   referent is unclear, and the same caution in module probes.
10. **"Undated" and retrieval-year dates.** One module source said "undated", and several vendor pages carry the retrieval year.
    Briefs should say how to date an undated page: archive first capture, then content clues, and otherwise year-only with an
    explicit "page undated" note in the locator.
11. **Older survey numbers presented as current when newer data contradicts them.** "Most have not measured" rested on a 2025
    professional-services figure while a 2026 corporate-tax figure said two-thirds track time savings. Briefs should require the
    newest figure for the specific population.

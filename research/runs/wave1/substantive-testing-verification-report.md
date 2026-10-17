# Verification report: assurance / substantive-testing

Wave 1 · Verifier · 2026-10-17

**Files checked and edited:**
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/substantive-testing.yaml` (25 entries)
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/substantive-testing.md` (299 lines)

**Method:** every cited URL was opened with `curl` (pdftotext for PDFs; `r.jina.ai` mirror where a page blocked curl or
rendered client-side). Full papers were pulled where the cited page was an abstract (arXiv PDFs of AuditCopilot and
FinancialAuditBench). Page dates were checked against the byline, `article:published_time` and JSON-LD. Unlabelled
charts were rendered and read (IFIAR 2026, p.10). Claims were traced back to the raw practice, discourse and governance
files and the synthesis report where a source did not show them.

## 1. Counts

| | Count |
|---|---|
| Use cases checked | 25 |
| Kept as written | 10 (06, 08, 12, 13, 15, 19, 21, 22, 23, 24) |
| Fixed (wording, figure, attribution, date, grade, maturity or a better source) | 15 (01, 02, 03, 04, 05, 07, 09, 10, 11, 14, 16, 17, 18, 20, 25) |
| Rejected (whole entry) | 0 |
| Claims removed inside an entry | 1 (search-only Wolters Kluwer guardrail in 04, source unreachable) |
| Grade changes | 2 (17 A→B; 25 B→C) |
| Maturity changes | 2 (11 in-production→piloting; 25 in-production→announced) |
| Module statements fixed or removed | 22 (table in §3) |
| Cited sources opened (YAML 79 + module-only 9) | 87 of 88 |
| Additional sources opened to check claims | 7 (DataSnipper FGMK story, two arXiv PDFs, two FRC news pages, ICAEW mirror, IFIAR chart render) |
| Sources unreachable | 1 (§4) |

## 2. Final grade mix

| Grade | Before | After | Ids after |
|---|---|---|---|
| A | 3 | 2 | 10, 11 |
| B | 11 | 11 | 01, 08, 09, 12, 13, 15, 17, 18, 20, 21, 24 |
| C | 7 | 8 | 03, 04, 06, 07, 14, 16, 22, 25 |
| D (idea) | 4 | 4 | 02, 05, 19, 23 |

A/B share: 13 of 25 (52%), down from 56%. Maturity after: 6 in production, 8 piloting, 4 announced, 7 emerging.

**The three A grades (all vendor-published, single-firm):**
- **#10 (kept A).** Oberlander's "about 16 hours to 5-6 hours per engagement" is a direct quotation from the firm's owner in
  Thomson Reuters' 5 Nov 2025 release about Audit Intelligence Test, which matches samples to evidence and traces to bank
  activity (tests of details). The tool was in an early-adopter programme at the time. Sanville's "hours to minutes",
  zero PCAOB comment forms and realisation figures match Fieldguide's case study; the matching is revenue and
  related-party testing (tests of details). The realisation and inspection results follow a whole platform and
  methodology change, which the entry now says. "Sole practitioner" was not in the source and was removed.
- **#11 (kept A, fixed).** The FGMK "30-45 minutes to about 5" traces to DataSnipper's February 2026 customer story, not
  only the Connect recap. There it is "~5 minutes of review" per selection, for a pilot group in a design-partner
  programme, "in complex, high-volume testing scenarios". The tests are locating and snipping evidence in
  multi-document client PDFs and tracing revenue to contracts, invoices, remittances and bank statements, so they are
  substantive. Figure context, source and maturity (piloting) fixed; a second vendor-published figure added (CROP
  Accountants' cash testing about 80% faster through Alwin).
- **#17 (A→B).** The "up to 20 hours per audit" is Circit's own case-study narrative, not the Moore Polska director (whose
  quotation is PDF preparation from about 3 minutes to 3 seconds). It also spans PBC document requests, which are not
  substantive testing. Named deployments (Moore Polska, Crowe Spain, Beever & Struthers, Kreston Iberaudit, BDO NL's
  test) support B.

## 3. Fixes and rejections

### Use cases

| # | Claim before | Action | Reason |
|---|---|---|---|
| 01 | Problem cites "(Buzzacott)" and the 942 false positives without context | Fix | Not a source key; now BUZZACOTT-PRIME-2025, and the benchmark is labelled a synthetic, tax-related ledger |
| 01 | "A complete general-ledger extract reconciled to the trial balance" (Buzzacott) | Fix | Not in the source; Buzzacott says ledgers are held in one place rather than in many Excel files |
| 01 | "A technical committee ... that owns standards mapping, methodology and policy" (Buzzacott) | Fix | Embellished; that wording describes Cherry Bekaert. Buzzacott's committee was involved from research through implementation |
| 01 | "Auditor decides what is a misstatement" (ED-500 EM para 64) | Fix | Para 64 says unusual items may indicate a possible misstatement and need investigation |
| 01, 14 | RSM-AUS-2026 date "2026-08" | Fix | Page JSON-LD gives 2026-08-11 |
| 02 | LLM journal-entry benchmark presented as audit JET | Fix | The paper's real ledger and framing are tax-related ledger data (DFKI); now labelled adjacent |
| 03 | MindBridge's 22 Sep 2026 Agentic Risk Assessment presented as exception-triage evidence | Fix | Adjacent process: MindBridge positions it for audit planning. Rewritten around the Augmented Assurance statement and Buzzacott's drill-down; Buzzacott source added |
| 04 | "Practitioners advise matching invoice details against bank records ... and testing full populations" | Fix | Wrong speaker: this is MindBridge, a vendor. The vendor-master advice is BDO's forensic practitioner (JofA) |
| 04 | Guardrail from a Wolters Kluwer search-result summary | Reject (claim) | Search-only; page returns 403 directly, a Cloudflare challenge via the mirror, and the archive connection failed. Source removed from YAML and module |
| 05 | AICPA practice aid dated "13 Oct 2026" | Fix | No source gives that date; Accounting Today reported it on 14 Oct 2026 |
| 05 | AS 2301.17 point "matters when a client's AI cannot be independently verified" (CAQ) | Fix | Embellished; CAQ says sufficiency will be a continuing challenge as companies rely more on GenAI |
| 07 | "Managers and partners refine the agent's skills ... comparable to maintaining a procedure manual" | Fix | Unsourced connective claim; the article says staff report to managers, who refine skills, after control-dataset testing |
| 09 | Cherry Bekaert case study date "2022 (year inferred)" | Fix | JSON-LD datePublished 2022-05-08 |
| 10 | "A named sole practitioner" (Oberlander) | Fix | Source says "Owner of Kentucky-based firm"; sole practitioner not stated |
| 10 | "Fieldguide agents stop at major steps for review" cited to Field Agents and Sanville pages | Fix | Wrong document: stopping at each major step is Field Orchestrator (#20). Now cites what the Field Agents page says (source references; teams investigate discrepancies) |
| 10 | Sanville realisation figure | Fix | Added that it follows a whole platform and methodology change, so it is not attributable to matching alone |
| 11 | "30-45 minutes to about 5 minutes per selection"; "used them on busy-season work"; in production | Fix | Statistic measured something narrower: about 5 minutes of review, pilot group, complex high-volume tests. Busy-season remark was about Alwin testing. Maturity piloting. Better source added (DATASNIPPER-FGMKEXCEL-2026) |
| 11 | "A contract term that client information does not train the models" | Fix | Embellished; FGMK says DataSnipper allows its information not to feed or train models |
| 14 | "Auditor ... decides what further procedures are needed" (ICAEW) | Fix | Embellished; source says the auditor cannot assume contract checking is done and must apply judgement |
| 14 | FRC examples "do not describe approved practice" | Fix | FRC says they show one way, which may not be the best or only approach |
| 16 | "Firm commenters ... preferred not to compare tests of details with analytical procedures" (SEC footnote 19) | Fix | Wrong attribution: footnote 19 concerns AS 1105.10A(b) and the pending substantive analytical procedures proposal |
| 17 | Grade A on "up to 20 hours per audit", attributed to Moore Polska's director | Fix (A→B) | Wrong speaker (vendor narrative) and adjacent process (PBC requests); see §2 |
| 17 | Kreston "plans to extend use across its whole audit team" | Fix | Source says in 2025; the page is dated 2026, so the tense was wrong |
| 18 | CHRIST-DRONE-2021 date "2021" | Fix | Published 9 Jan 2021 |
| 20 | Field Orchestrator "announced 8 Jun 2026" | Fix | Fieldguide says it is live in its Financial Audit product |
| 25 | Ledgerline graded B, in production; "uses AI agents with deterministic code to check every deposit" | Fix (B→C, announced) | The firm's site says it is pre-launch, assembling its founding team, service available from 1 Dec 2026. The agent description is the CEO's general account, not the firm's operations |
| All | last_reviewed | Fix | Set to 2026-10-17 |

### Module

| Section | Before | Action | Reason |
|---|---|---|---|
| Header | "Synthesised ... from wave 1 research; not yet source-verified" | Fix | Build-only reference removed |
| §11 | "the synthesis report maps keys to input refs" | Remove | Build-only reference |
| §3 | IFIAR members see tools "in 88% of cases" | Fix | Measures share of responding members who frequently observed tools, not share of cases |
| §3 | MindBridge September capability as follow-up evidence | Fix | Planning capability; rewritten (as #03) |
| §3 | AuditCopilot unlabelled | Fix | Tax-ledger data noted |
| §3 | "Practitioners advise corroborating ..." | Fix | Now "a vendor and practitioners" |
| §4 | #11 "30-45 minutes to about 5 per selection" | Fix | Review time, pilot group |
| §4 | #17 "Moore Polska up to 20 hours per audit" | Fix | Vendor narrative; named deployments listed instead |
| §4 | #25 "AI-native benefit-plan audit firm that tests every transaction" | Fix | Pre-launch firm built to do so |
| §6 | Named outcomes (Oberlander, FGMK, Moore Polska) | Fix | Owner's estimate; FGMK review time; Moore Polska as vendor narrative incl. PBC; CROP added |
| §7 | "All commenters said implementation guidance was warranted" | Fix | All five commenters to the SEC; interpretive or implementation guidance |
| §7 | "The 13 Oct 2026 practice aid" | Fix | Date unsupported; "October 2026" |
| §7 | AFM: auditors "often" do not verify input data | Fix | Source says "do not always" |
| §7 | Versioning and approval "(FRC; FGMK)"; "client data contractually barred from training" | Fix | Versioning is DataSnipper's description; contract term not stated |
| §7, §10 | "Ledgerline pairs agents with deterministic code" | Fix | The CEO's advice; the firm is pre-launch |
| §9 | "PwC promises a tool for every audit step" | Fix | PwC "expects"; hope for calendar 2026 |
| §9 | AICPA practice aid 10-13 | Fix | Reported 10-14 |
| §9 | TR executives watching for a "hockey stick" "by the end of 2026" | Fix | Executive expects a hockey stick "at some point"; no date |
| §10 | "Oberlander (a sole practitioner)" | Fix | Owner; sole practitioner not stated |
| §11 | WOLTERSKLUWER-EVIDENCE-2026 (search only) | Remove | Unreachable, no longer cited |
| §11 | IIA-AIFRAUD-2026 "with AuditBoard" | Fix | Report says Internal Audit Foundation with Optro |
| §11 | TRI-FOP-2026 date 2026-07; DATASNIPPER-FGMKEXCEL-2026 missing | Fix | Date 2026-07-21; new key added |

Everything else in the module was traced: IFIAR 2023-2025 rates (2025 bars read from the rendered chart: about 86%, 63%,
44%), IFIAR 2025 finding rates and the 35% / 26% series, PCAOB tool counts (13 to 18; 90%; under 7%), CPA.com
percentages, ISA 240 (Revised) effective date, SAS 150 and 151 publication and effective dates, PCAOB confirmation
standard content and effective date, ED-500/520/330 paragraphs, FRC pages 18, 19, 37-38 and 49-51, FinancialAuditBench
figures, Graczyk counts, SAS/ACFE and IIA survey figures, Computerworld, NYSSCPA and TheFinanceStory items.

## 4. Sources that could not be reached

| Ref | Routes tried | Outcome |
|---|---|---|
| WOLTERSKLUWER-EVIDENCE-2026 | curl (403), r.jina.ai (Cloudflare "Just a moment"), web.archive.org (connection reset) | Claim and source removed |

Read only partially or through a copy (already disclosed in the entries): the WSJ article (read through the Controllers
Council reproduction), Christ et al. (abstract and notes via mirror; full text paywalled), the AICPA practice aid
itself (login; read through Accounting Today), and the PAC hearing behind DataSnipper's NAO figures (not located).
Several vendor pages remain undated (DataSnipper Connect, FGMK Alwin, ODP, Payables; Fieldguide Sanville); they carry
the year of access.

## 5. Targets

| Target | Result |
|---|---|
| 15-25 use cases | 25: met |
| At least 50% graded A or B | 13 of 25 (52%): met, with little margin |
| Every source dated (ISO) | Met; validator reports no date errors |
| Values from the vocabulary; unique ids; every source has a URL | Met |
| Quotations under 25 words | Met (longest is about 15 words) |
| Module ≤ 300 lines, no build-only references | 299 lines; header and §11 cleaned. YAML `notes` still name research candidates (for example "Merged from practice-01"); not shipped prose, left as provenance |
| `python3 scripts/validate.py` | No ERROR for either file (`INFO ... 25 use cases, 13 graded A/B (52%)`); other current errors belong to other modules |

## 6. Error patterns to fix in the briefs

1. **Organisation status not checked (new).** Ledgerline was graded B and in production from a trade article; its own
   site says pre-launch. Brief: open the organisation's own site and record its status ("pre-launch",
   "launching", JSON-LD availability dates) before setting maturity or B.
2. **Second-hand figures not traced to the primary page.** FGMK's figure came from a vendor event recap that drops
   "of review" and "pilot group". Brief: when a vendor recap or press release quotes a customer figure, find and cite
   the customer story.
3. **Narrative versus quotation in case studies.** Moore Polska's 20 hours is the vendor's narrative, not the
   director's words. Brief: in vendor case studies, `measures` must say whether the figure is in a named person's
   quotation or the vendor's text.
4. **Adjacent process inflating grade or scope.** A planning product cited as exception triage (#03); confirmations
   figure that includes PBC requests (#17); tax-ledger data framed as audit JET (#02). Brief: confirm the vendor or
   author places the evidence in this module's step.
5. **Wrong document or speaker.** Field Orchestrator behaviour cited to Field Agents; DataSnipper's governance to FGMK;
   SEC footnote 19 misread; vendor advice labelled "practitioners".
6. **Embellished qualifiers.** "Sole practitioner", "contractual", "often", "promises", "by the end of 2026",
   "partners", "procedure manual". Brief: forbid qualifiers the source does not use.
7. **Dates.** An unsupported release date (13 Oct) and several year-only dates that JSON-LD or bylines resolve.
   Brief: record the date field consulted in `locator`.
8. **Measure wording.** "88% of cases" for a share of regulators. Brief: `measures` must name the unit of the
   denominator (members, firms, audits, selections).
9. **Grade margin.** With A/B at 52%, the next verifier pass could push the module under target. Synthesis should
   flag entries whose B rests on a single "attempting" or "pilot" sentence (#15, #18) so research can add evidence.

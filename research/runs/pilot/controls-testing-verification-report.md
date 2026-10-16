# Verification report: assurance / controls-testing

Verified 2026-10-16 against the sources themselves. Files checked and edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/controls-testing.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/controls-testing.md`

Method: every cited URL was fetched with curl (through the proxy). PDFs were converted with pdftotext, and the
Microsoft PDFs were also rendered to images because their text layer drops glyphs. Each claim, figure and date was
checked against the fetched text. Where a page was blocked, I tried other routes (alternative URLs, the Wayback
Machine, a mirror, web search) before downgrading or moving the claim.

## Counts

| Result | Use cases |
|---|---|
| Kept unchanged | 4 (#06, #17, #22, #25) |
| Fixed | 21 (#01–05, #07–16, #18–21, #23, #24) |
| Rejected | 0 |

No entry was rejected. Every use case has at least one opened source that supports the organisation, the change to
the work and the core claim. Most fixes correct wording, attribution or dates. One fix is a grade change (#07).

## Final grade mix

| Grade | Count | Entries |
|---|---|---|
| A | 5 | #04, #05, #06, #08, #11 |
| B | 11 | #01, #02, #07, #09, #10, #16, #17, #18, #19, #20, #21 |
| C | 5 | #03, #12, #13, #14, #15 |
| D | 4 | #22, #23, #24, #25 (all titled "Idea") |

A or B: 16 of 25 (64%). Validator line:
`INFO  plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/controls-testing.yaml: 25 use cases, 16 graded A/B (64%)`.
The validator reports no ERROR lines for either file. The module is 293 lines, under the 300-line limit.

## Targets

| Target | Status |
|---|---|
| 15–25 use cases | Met: 25 |
| At least 50% graded A or B | Met: 64% |
| Every source has a URL and a date | Met. 10 sources are dated to the year only (MSFT-IA, MSFT-CM, RSM-BEACON, YC-ARDEN, PETUAL-HOME, PWC-DCT, FG-SANVILLE, DS-RMF, FG-FRAZIER, JOB-REDDIT) because the pages carry no fuller date. 13 dates were corrected or refined (see table). |
| Unique ids, values from the vocabulary | Met: 25 unique ids; the validator found no enum errors |
| Quotations under 25 words | Met: no source quotation in the YAML is 15 words or longer, and the module's source quotations are short. The §4 interview probes are the module's own questions, not quotations |
| Every module figure, regulatory statement and frontier item traceable | Met after fixes: every bracketed key in the module resolves to the YAML or to §10. Nine sources were added to §10 for previously unsourced claims. |

## Fixes to use cases

| Entry | Fix | Reason |
|---|---|---|
| #01 | "is used on 2026 year-end audits" changed to "will be used" | CFO Dive says PwC "will be using AI" for 2026 year-end audits |
| #01 | FRC guardrail reworded | The FRC's misinterpretation example is AI contract summaries, not walkthrough narratives |
| #01 | "Transcription kept within the firm's M365 tenant" changed to "runs within Microsoft 365, not a separate AI system" | KPMG UK's wording; "tenant" was an embellishment |
| #02 | Removed the "version control on AI-generated test instructions (PwC)" guardrail; PwC test-procedure clause labelled search-only | pwc.com returns 403. Web search shows PwC "Dynamic Testing" marketing but not the version-control claim |
| #02 / #09 | FG-AGENTS date "2026" changed to "2026-06-24" | Date on the help-centre page |
| #03 | Removed "Clients of Weaver and Sanville see live request status" | Uncited. The Weaver case study is about client visibility in general, not AI, and Sanville's page does not say it |
| #03 | Attributed "20+ systems / weeks chasing" to Arden; "1 in 5 PBC wrong" to Zanin as a SOX-tooling CEO | It was labelled a "practitioner" estimate. Zanin is CEO of Bead AI, a vendor |
| #03 | Peer Review Board guardrail softened to "can lead reviewers to judge nonconforming" | JofA wording |
| #03 | "SOC peer reviewers warn…dashboard extraction" reattributed to the AICPA SOC 2 Working Group (via CSA); CSA-SOC2 added as a source | The statement is in the CSA note, which #03 did not cite |
| #04 | "Models trained on historical deficiencies" changed to "predictive risk modelling that analyses historical data" | KPMG 404(a) wording |
| #04 | Note: the ~2K h/yr figure confirmed on the rendered PDF. The PCAOB sample-tool fact now cites PCAOB-2024-007 (added as a source) | The fact had no source in this entry |
| #05 | Guardrail "plateau…such as management review controls" changed to "the most judgment-heavy work" | Optro does not name management review controls |
| #05 | Removed "the ratio of reviewers to preparers rises" | No source supports it (also removed from module §7) |
| #05 | CALCPA date changed to 2026-08-12; note on the mirror's limits added | Article byline. The mirror carries the TL;DR and a summary only. Preedy's CAE role was confirmed by web search |
| #07 | **Grade A changed to B** | The measured figures (Oberlander 16 h to 5–6 h, RMF ~50%, Sanville) are tests of details. RMF and KPMG UK name controls use but publish no controls-specific measure |
| #07 | Thomson Reuters "up to 70%" relabelled as CoCounsel Document Analysis | In the press release, the 70% follows the Document Analysis paragraph, not Audit Intelligence Test |
| #07 | PCAOB guardrail rewritten | The amendments cover the reliability of company-provided electronic information and the investigation of flagged items. The old wording, "information processed by technology tools", was inaccurate |
| #07 | FG-PCAOB date changed to 2026-08-06 | Page date |
| #08 | AT-GARTNER date changed to 2026-08-17; AUASB-CP added as a source | The IAASB ED texts require a login. The AUASB consultation paper confirms "evaluate, not just consider", "tests of controls alone" and the authenticity attribute |
| #09 | OPTRO-SNOW date changed from "2026" to **2024-02-27**; "Snowflake CAE" changed to "Head of Internal Audit"; "controls" changed to "use cases" | The page is dated Feb 2024 (an AuditBoard post). The note claimed it was undated |
| #10 | IntelliAudit outcome rewritten | 91.7% is the share of final statuses *unchanged from the single auditor-agent label*, which is internal consistency, not agreement with human assessors |
| #10 | "IT auditors adjudicate disagreements" changed to "auditors investigate model disagreements"; OPTRO-FJM date set to 2026-09-22; PETERS date set to 2022-12-09 | Source wording and page dates |
| #11 | Removed "without a matching rise in staff" | Not in the KPMG UK report. Added "(90% over 2023-24)" |
| #11 | Frazier & Deeter figure moved from the outcomes to the notes | The page returns 404 directly. The figure is visible only in search extracts and should not sit in an A-graded entry |
| #12 | EY poll relabelled "attendees naming each as a top AI use case" | The figure caption reads "top four use cases", which is not a usage rate |
| #13 | K-SOX30 added as a source | The "SOC review not designed for vendor AI risk (KPMG)" guardrail comes from K-SOX30, which the entry did not cite |
| #14 | PRB "effective 1 June 2026" changed to "reviewer alert May 2026; enhanced oversight from 1 June"; Delve "conclusions drafted before evidence arrived" changed to "…before observation periods ended"; IANS date changed to 2026-03-24 | Source wording; IANS byline |
| #15 | TQA 9561 wording: AI providers that perform functions within the system are assessed under the subservice framework | Schneider Downs wording ("not all AI providers") |
| #15 | Kokina note corrected | The abstract says complex AI tools are still being developed for audits. It says nothing about clients' financial reporting |
| #15 | JOFA-EVAL date set to 2025-11-01 | Article date |
| #16 | K-CLARA date set to 2025-04-22 | Press-release date |
| #18 | Removed the "vibe-coded tools" guardrail | Not in any cited source |
| #19 | Added "only 28% used outsourced providers" before the 58% figure; "spend is redirected" changed to "Havertys expects spend to shift"; Havertys date set to 2026-09-04 | KPMG survey context; Havertys gives a target, not a result |
| #20 | "RSM Beacon (built with Andera)" reworded; RSM–Andera alliance stated separately | The alliance release does not name Beacon, and Beacon's page does not name Andera |
| #20 | "FRC thematic: logic review…output testing carries more weight" reattributed to FRC GenAI guidance (added as a source); Verdantix date set to 2026-02-10 | That point is in the GenAI guidance, not the thematic review; page date |
| #21 | "ex-Big Four SOX managers" changed to "Big Four (or equivalent) SOX experts"; job dates set to 2026-08-24, 2026-09-29 and 2026-04-13 | Posting text and JSON-LD `datePosted` (JOB-FG-SWE was wrongly dated 2026-10) |
| #23 | AUASB-CP added; note updated | Confirms the IAASB authenticity attribute |
| #24 | **SEC proposal figure corrected** | "404(b) removed for 80.8% of reporting companies" was wrong. 80.8% is the share that would be non-accelerated filers (from 51.9%). About half of currently attested issuers would leave 404(b) |
| #24 | Botic guardrail now attributes the characterisation to Foley's write-up | The remark was reported by Foley, not quoted from Botic |

## Fixes to the module file

| Section | Fix | Reason |
|---|---|---|
| §2, §5 | PBC "1 in 5" attributed to Zanin as a vendor CEO; "20+ systems" to Arden | Attribution |
| §5 | "$2.3M / 15,000 h (survey not named)" changed to "KPMG 2025 SOX Survey, as cited by Zanin" | Zanin names the survey |
| §5 | Co-source line adds "only 28% used outsourced providers" | Context from the KPMG survey |
| §5 | Oberlander and RMF labelled tests of details; KPMG UK "~15% from DataSnipper alone" changed to "on one engagement" | Source wording |
| §5 | Thomson Reuters 70% tied to CoCounsel Document Analysis | Product mix-up |
| §5 | Gartner: "Aug 2026 poll" changed to "reported Aug 2026"; "30% GenAI for testing" changed to "30% AI for testing" | The article says the poll was "conducted in 2026" and that 30% use AI for testing |
| §5 | EY poll relabelled as top use cases | Figure caption |
| §5 | IntelliAudit 91.7% restated as consistency, not accuracy | Misread statistic |
| §6 | PCAOB amendments "expressly exclude AI" changed to "address technology-assisted analysis, not AI as such"; QC 1000 date now sourced [JOFA-QC1000] | Release wording; the date was flagged "not re-verified" and has now been verified |
| §6 | CPAB accountability claim sourced [CPAB-AI]; IAASB claims also cite [AUASB-CP] | Previously unsourced or only indirectly sourced |
| §6 | FRC thematic "certification policies incomplete" changed to "certification maturity varied" | Thematic wording |
| §6 | TQA 9561 and PRB alert wording corrected (as in #14 and #15) | As above |
| §4 | Probe 2: "plateau on management review controls" changed to "judgment-heavy controls" | As in #05 |
| §3, §8 | "RSM Beacon with Andera" changed to "RSM and Andera announce an alliance"; "Big Four (…GT)" changed to "Big Four and Grant Thornton" | Attribution; GT is not a Big Four firm |
| §7 | Removed "Reviewer-to-preparer ratios rise"; Holmstrom & Peters and the Thomson Reuters talent claim now sourced [HOLMSTROM, TRI-FOP]; Zanin cited for "review is where most time goes" | Previously unsourced |
| §8 | SEC frontier item corrected (about half of attested issuers, not 80.8%) | Misread statistic |
| §8 | Added 2026-06-04 FRC Audit Tech & AI Sandbox [FRC-SANDBOX]; sourced the funding amounts [SA-FG, FTG-PETUAL, OPTRO-MIDSHIP, FTG-ANDERA], WCARS [WCARS75], KPMG, Optro, RSM and Workiva items | The §8 items and the §9 "FRC opened a sandbox" objection had no source key |
| §10 | Added 9 sources with title, URL and date (FRC-SANDBOX, JOFA-QC1000, CPAB-AI, HOLMSTROM, TRI-FOP, SA-FG, FTG-ANDERA, WCARS75; AUASB-CP is in the YAML) | Traceability |

Figures and claims confirmed as stated, with no change needed (selection): Microsoft 850 h, $185K, 1–3 months, 2K
h/yr, weeks to one day, <30 to ~100 services, quality-review effort ~50%, 3 to 2 weeks (on the rendered PDFs). Reddit:
175 controls, >40%, -60%, later >75% (Optro). KPMG SOX survey: 16 h per control (12 h in FY2022), +45% cost, 52%, 58%.
KPMG UK: ~18%, ~15%, 180+ reports, 90%, 39%. IFIAR 2025: 213, 69, 43, 39, 24, 11, 11, 6, 14% vs 11%. IFIAR TTF 2025:
43% vs 88%, 31%. Optro survey: 34%, 46%, 9%, n=417. IIAF fraud report: 65%, 62%. Sanville: $150–200 to $250+ per
hour, zero comment forms. Armanino: 100%, 25+ h. EY: 130,000 staff, 160,000 engagements, 2028. Deloitte: ~85,000.
PwC Australia: 5 clients, 2028, 1,600 auditors. CPA.com: 54 firms, 75%, 41%. Petual: 68–80%. Midship: 16 h to under
15 min, 85%, 60%. The regulator dates (FRC 2026-03-30, COSO 2026-02-23, IAASB 2026-08-05 with comments due 15 Dec,
AFM 2025-12-11, NFRA 2026-07-24, TQA 9561 11 Sep 2026, AICPA practice aid 13 Oct 2026, PCAOB RFC 2026-06-23, IIA
letter 2026-08-07) were all confirmed.

## Sources that could not be reached

| Source | What happened | Handling |
|---|---|---|
| PWC-DCT (pwc.com dynamic controls testing) | HTTP 403. web.archive.org reset the connection | Seen through web search only. Labelled search-only. The unverifiable guardrail was removed. #02's grade rests on KPMG UK |
| FG-FRAZIER (Fieldguide Frazier & Deeter case study) | HTTP 404 on every URL variant | Search extracts confirm 40%/71 h and 8%/19 h. Kept in #03 (grade C) as search-only; moved out of #11's outcomes into its notes |
| reddit.com/r/RedditEng original post | 403; no archived copy available | Read through the Tenu Tech Brief mirror (TL;DR and summary). The figures match Optro's launch post |
| IAASB exposure-draft PDFs | Login required | Claims confirmed through the AUASB consultation paper (added as a source) |
| AICPA TQA 9561 text | Not fetched directly | Known through Schneider Downs and CSA, as the YAML already notes |

Sources opened directly: 88 of the 90 distinct URLs originally cited (all except PWC-DCT and FG-FRAZIER). I also
opened 14 more: 3 COSO PDFs, the Weaver case study, the FRC sandbox notice, the JofA QC 1000 article, the AUASB paper,
CPAB, Holmstrom & Peters, TRI Future of Professionals, SiliconANGLE, FinTech Global (Andera), WCARS75 and a Fieldguide
HITRUST page, which redirected. In total about 102 sources were opened directly; 2 cited sources, plus the original
Reddit post and the IAASB ED PDFs, could not be reached. Web search was used only to confirm Martin Preedy's role,
the AFM release date, the PCAOB QC 1000 postponement, the IIAF report date, and the blocked PwC and Fieldguide pages.

## Patterns of error to fix in the briefs

1. **Misread statistics.** Several figures were reported as something they do not measure: the SEC 80.8% (a share
   of reporters, not of 404(b) removals), IntelliAudit's 91.7% (consistency, not accuracy), the EY poll (top use
   cases, not usage), Gartner (AI, not GenAI), and Thomson Reuters' 70% (a different product). Brief change: for
   every percentage, record the numerator and denominator in the source's own words.
2. **Attribution drift.** Claims ended up attributed to the wrong document or speaker: FRC thematic vs GenAI
   guidance, RSM Beacon "with Andera", a vendor CEO called a "practitioner", the KPMG survey "not named", "KPMG models
   trained on deficiencies", and the Kokina abstract. Brief change: every attributed sentence needs a source ref
   *and* a locator (page or section).
3. **Embellished qualifiers.** Examples: "without a matching rise in staff", "expressly exclude AI", "effective 1
   June", "spend is redirected", "conclusions drafted before evidence", "firm's M365 tenant", "IT auditors
   adjudicate". Brief change: paraphrase conservatively, keep modal verbs (expects, may, plans), and do not add
   causes or scope.
4. **Unsourced connective claims** in the role and guardrail fields ("reviewer-to-preparer ratio rises", "vibe-coded
   tools", Weaver live status) and in the module (funding amounts, WCARS, the FRC sandbox, CPAB, Holmstrom, TR).
   Brief change: no claim in role_evolution or risks_and_guardrails without a ref; the module may not cite a key that
   is absent from the YAML or §10.
5. **"Undated" pages that had dates.** Snowflake (2024, not 2026), FJ Management, Havertys, Verdantix, IANS, and
   job postings (JSON-LD `datePosted`). Brief change: check the visible byline, `article:published_time` and JSON-LD
   before writing a year-only date. A two-year-old page presented as current misleads more than a missing day.
6. **Grade inflation through adjacent evidence.** #07 was graded A on substantive-testing measurements. Brief change:
   a grade must reflect evidence for *this module's* use. Measurements from an adjacent process cap the grade at B
   and need a note.
7. **Search-only figures inside high-grade entries** (Frazier & Deeter in #11). Brief change: figures that could not
   be opened belong in the notes, never in the outcomes of an A or B entry.

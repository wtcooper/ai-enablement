# Planning and risk assessment: verification report

Assurance archetype · Wave 1 · Verifier · 2026-10-17

**Files checked** (in `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/`):
`use-cases/planning-risk-assessment.yaml` (25 entries) and `modules/planning-risk-assessment.md`.

**Method.** Every cited URL was opened with `curl` (`pdftotext -layout` for PDFs, with PDF page numbers mapped to
printed page numbers). The `r.jina.ai` mirror was used for the eight pages that return 403 to curl (PCAOB AS 2110 and
seven Wolters Kluwer articles). The ACRA guidance was read from the PDF linked on its news page. The image-only
VLGAA conference slides were rendered to PNG and read. Claims were traced back to the
`research/runs/wave1/assurance-planning-risk-assessment-*.md` inputs where a source did not contain them.

## 1. Counts

| | Count |
|---|---|
| Use cases checked | 25 |
| Kept as written (only `last_reviewed` updated) | 5 (`#07`, `#11`, `#16`, `#18`, `#21`) |
| Fixed | 20 |
| Rejected | 0 |
| Grade changes | 0 |
| Module claims fixed | 14 (listed in §3) |
| Sources opened | 98: all 96 URLs now cited (83 in the YAML, 13 listed only in the module), plus the Optro CRX release behind a frontier date and the ACRA PDF behind its news page |
| Sources unreachable | 0 |

## 2. Final grade mix

| Grade | Entries | Count |
|---|---|---|
| A | none | 0 |
| B | 01, 02, 03, 07, 08, 09, 11, 18, 20, 22, 25 | 11 |
| C | 04, 05, 10, 14, 17, 19, 21, 23, 24 | 9 |
| D (all labelled "idea") | 06, 12, 13, 15, 16 | 5 |

**A/B share: 44% (11 of 25). Below the 50% target. No grade was raised to hit it.** Borderline B entries I kept
(and why): `#22` RSM Luca Resourcing (RSM attributes the staffing benefit to "deploying AI technology" but does not say
what the AI does); `#20` DAS adoptions (named firms adopted the AI-enabled suite; the figures measure platform
adoption, not AI use in planning); `#01` KPMG minutes review (the minutes example is from a July 2024 "will help"
list; the April 2025 recap is in the present tense). None of these are search-only or rest on an adjacent process.

## 3. Fixes and rejections

### Use cases

| # | Entry | Before | Action | Reason |
|---|---|---|---|---|
| 1 | 01 | role_evolution: "Team members become reviewers of a cited summary rather than first-pass readers of every minute (governance deep dive's reading)" | Fix | Unsourced connective claim. It also contradicts the source: the FRC example requires the auditor to read the minutes to corroborate the output (p.46). Replaced with that requirement |
| 2 | 01 | Note: grade rests on KPMG "present-tense statements" | Fix | The minutes example is in the July 2024 list of what GenAI "will help teams" do ("can leverage AI to help review meeting minutes"). Note now quotes both releases accurately |
| 3 | 01 | Note: "Newsfile copy of the April 2025 KPMG release is dated 23 April" | Fix | The Newsfile item is a different release (KPMG LLP, US), not a copy of KPMG International's |
| 4 | 02 | "more than 2.175 million Audit Chat conversations" sourced to KPMG-CLARA-2025 (KPMG International, 22 Apr 2025) | Fix | Wrong document. The figure is only in KPMG LLP's US release (Newsfile, 23 Apr 2025). Added KPMG-US-CLARA-2025 and re-pointed the outcome |
| 5 | 02 | Count "stated in May 2024" | Fix | The release gives no as-of date; it recaps the May 2024 Audit Chat upgrades. Measure and note reworded |
| 6 | 02 | Checkpoint: "Experienced human review of answers before they inform audit judgments" | Fix | Embellished. RSM says grounding and experienced human review are "vital"; it does not describe a pre-judgment review step |
| 7 | 03 | Title: agents scan media for "emerging threats to the audited entity" | Fix | Bloomberg Law says "scan media reports for emerging threats"; "to the audited entity" was added |
| 8 | 04 | Guardrail: "a document-analysis tool does not satisfy these inquiries (governance deep dive's reading…)" | Fix | Unsourced connective claim. Now states the AS 2110 .54 and ISA (UK) 315 14(a) requirements and that the source does not say the tool replaces an inquiry |
| 9 | 05 | ICAEW-315-2025 date "2025-10" | Fix | Page byline: 09 Oct 2025. Title aligned to the page ("…without specialists IT teams") |
| 10 | 06 | Checkpoint: "The engagement partner and team decide how the entity's AI affects RMM (JOFA-AIPA-2026)" | Fix | Not in the JofA article. Replaced with what it says: the auditor remains responsible for the audit and the opinion (AICPA chief auditor) |
| 11 | 06 | "SEC accounting staff said … standards not written with AI in mind, but that the foundations of risk assessment remain the same" | Fix | Two speakers merged into one statement. An associate chief accountant made the first point; another OCA official made the second about preparers |
| 12 | 06 | Practice aid Part 1 covers "AI-operated controls and service-organisation reports" | Fix | The AICPA release lists "controls … related to AI"; the other two topics come from Accounting Today's report. Now attributed |
| 13 | 06 | CAQ-INSIDERSEP-2026 date "2026-09"; CAQ-GENAI-2024 locator "pp.11-14, p.6" | Fix | Page dated 8 Oct 2026. The team-training/specialist statement is on PDF p.18 |
| 14 | 08, 14, 15 | ISAUK240-2026 date "2026-04-30" | Fix | Not supported. The standard reads "Revised March 2026 / Updated March 2026"; the PDF was created 27 Apr 2026. Dated 2026-03 |
| 15 | 09 | ITBRIEF-CASEWARE-2026 date "2026-10-13" | Fix | Byline: Mon, 12 Oct 2026 |
| 16 | 10 | ARA "comes with an MCP server" | Fix | Embellished. MindBridge describes the MCP server as a separate platform capability |
| 17 | 12 | Note: date "from the search listing and URL path" | Fix | The page byline gives 24 Sep 2025; the date is now confirmed |
| 18 | 13 | Guardrail cited "(deep dives' reading of the abstract)" | Fix | Build-only citation. The point (the label is restatement, not a planning judgement) is in the abstract; it now cites ARXIV-UMAR-2026 |
| 19 | 13 | ARXIV-FAB-2026 title "FinancialAuditBench" | Fix | Full title: "FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors" |
| 20 | 14 | Guardrail: "a tool does not replace that discussion (governance deep dive's reading of AS 2110)" | Fix | Unsourced connective claim. Now states AS 2110 .49-.53 as written (.52: set aside any prior belief that management is honest) |
| 21 | 14 | Checkpoint: "the slides show the model did not explicitly apply COSO" | Fix | Wrong slide. The COSO exchange (slides 43-44) concerns risk considerations, not fraud brainstorming (slides 49-52). Replaced with what slides 49-52 show |
| 22 | 15 | IIAF-AIFRAUD-2026 date "2026"; CAQ-INSIDERAPR "2026-04"; CAQ-INSIDERMAY "2026-05" | Fix | IIAF: no printed date, PDF created 28 Jul 2026 → 2026-07. CAQ pages dated 30 Apr 2026 and 1 Jun 2026 |
| 23 | 15 | "survey of 373 senior internal audit leaders" | Fix | Missing qualifier: the survey went to North American internal audit leaders |
| 24 | 17 | Guardrail: "ICAEW notes regulators have criticised firms for raising materiality to reduce scope without adequate justification" | Fix (claim removed) | Not in the ICAEW article. Replaced with what it says: under the old ISA 600, many group auditors scoped by size thresholds |
| 25 | 17 | WK-GROUP: "The group engagement team remains responsible…"; checkpoint "decides scoping and responses" | Fix | The source says "auditors remain responsible for evaluating results and determining appropriate responses"; it does not mention scoping decisions |
| 26 | 17 | Quote "helps people make decisions"; ICAEW-GROUP title | Fix | Source wording: "help people make smarter decisions". Title: "…how to master a risk-based approach to component scoping" |
| 27 | 19 | Caseware goal "up to 50% … prepare, plan, validate and report (CASEWARE-LAUNCH)" | Fix | Mixed-up documents. The launch release says "automating 50%" across Prepare, Plan, Evaluate and Report suites; "up to" and "validate" come from the CwX blog |
| 28 | 20 | Checkpoint: "Suggestions can be accepted, refined or overridden (CASEWARE-LAUNCH)" | Fix | That sentence is about the Disclosure Checklist Agent. Replaced with the release's general statement that every output is citation-backed and reviewable before it enters the file |
| 29 | 22, 25 | FIELDGUIDE-DEMO-2026 date "2026-10-20" | Fix | That is the future webinar date, not the page's date. Now 2026-10, with the webinar date and access date in the locator |
| 30 | 23 | Checkpoint: "Partner pricing decisions (inferred by the discourse deep dive)" | Fix | Unsourced, build-only. Now "Not described in the source" |
| 31 | 24 | WK-DYNAMIC-2026 title | Fix | Page title: "From static to strategic: Unlocking the benefits of dynamic audit planning" |
| 32 | 25 | Guardrail: "slides show the model built risk considerations from prior findings and peer audits, not from … COSO" | Fix | Incomplete. Slide 43 has the model saying it did not map to COSO "explicitly", and slide 44 shows a COSO-mapped table. Both now stated |
| — | all | `last_reviewed` | Fix | Set to 2026-10-17 |

### Module

| # | Location | Before | Action | Reason |
|---|---|---|---|---|
| 1 | Header | "`CT-04` … in the pilot", "PwC Australia AI-native pilot" | Fix | Build-only reference. Now "controls-testing module" and "AI-native audit trial" |
| 2 | §3, §8 | "KPMG orchestration pilots"; "5 pilot clients"; "PwC Australia pilots agents" | Fix | Reworded to "trials" / "5 audit clients first" so the file has no "pilot" wording |
| 3 | §5 | "Dutch PIE firms: risk assessment 28% of average tool use" | Fix | Mismeasured. The AFM chart shows how often tools are used in each area (average across six firms); areas overlap |
| 4 | §5 | "6% of largest clients have advanced AI governance" | Fix | The statistic is a partner rating: partners rate 6% of their largest clients' governance as advanced |
| 5 | §6 | "The acting chair wants a 'human-in-the-lead' model [KSLAW]" | Fix | Wrong speaker. King & Spalding attributes it to all the speakers (Botic, Ho, Stein). KSLAW date set to 2025-11-07 |
| 6 | §7 | ICAEW "faculty chair wants training in judgement and scepticism, not tool mechanics" | Fix | Embellished. The Technology Faculty Board chair says training needs practicalities and, crucially, judgement and scepticism |
| 7 | §7 | "vendors hire audit practitioners as agent architects and audit engineers [FIELDGUIDE-JOB]" | Fix | The posting supports agent architects (CPA, 8-10+ years of audit) only; "audit engineers" is unsupported |
| 8 | §7 | AAA panel "how juniors use GenAI in planning" | Fix | The panel covers several phases (e.g. planning) |
| 9 | §8 | "2025-10-27/28" | Fix | Article date 2025-10-28; the briefing date is not given |
| 10 | §8 | "ISA (UK) 240 (revised 2026-04-30) effective" | Fix | Same date error as use-case row 14 |
| 11 | §9 | "ICAEW says guidance assumes specialist teams…" | Fix | Speaker is ICAEW's head of data analytics and tech |
| 12 | §10 | "the synthesis report maps keys to the inputs and pilot"; "all opened by the deep dives" | Fix | Build-only references removed; the file now says all sources were re-opened on 2026-10-17 |
| 13 | §10 | KPMG-US-CLARA-2025 missing | Fix | New source added to the list |
| 14 | §10 | FIELDGUIDE-JOB "accessed 2026-10-16" | Fix | Re-accessed 2026-10-17 |

Module figures confirmed as written include: IFIAR 55%/49% (47/45 members), 88% journal entries, 31% "not used as
intended"; IFIAR survey 44 of 770 audits (6%, 53 findings) vs 14% internal control testing; CPA.com 60%/53%/85%/60%/64%,
22% automated risk assessment, 11% substantive analytics, 22% none, 54 of 74 firms; AFM AI 3% / analytics 32%;
FRC-ATT "no formal monitoring … to quantify the audit quality impact" (six largest firms); Fedyk 5.0% / 7.1% (36
firms); ICAEW chatbot test figures; UMAR AUROC 0.782 / PR-AUC 0.341 / ECE 0.052 (3,200 firm-years); EY survey 47%/36%
(202 respondents); and every regulatory paragraph reference (AS 2110 .07-.08, .46-.54, .74; ISA (UK) 315 13, 14(a),
A21, A57, A203, App 5 para 5; ISA (UK) 240 A9, A36, A56, A101, effective date; PCAOB 2024-007 pp.23-25, 32; AUASB
App 1 para 10(c); IAASB ED dates). The frontier dates were also confirmed: FRC 30 Mar 2026 (ICAEW confirms the issue
date), EY 7 Apr, IFIAR 20 Apr, FRC sandbox 4 Jun, Deloitte 24 Jun, NFRA 24 Jul, IAASB 5 Aug, MindBridge 22 Sep,
Caseware 6 Oct, Optro 14 Oct, AICPA 13 Oct and WCARS 6-7 Nov.

## 4. Sources that couldn't be reached

None are fully unreachable. Limits:
- **PCAOB AS 2110 and seven Wolters Kluwer pages** return 403 (or a bot challenge) to curl. All were read through the
  `r.jina.ai` mirror. WK-DYNAMIC-2026 needed several retries.
- **BBL-KPMG-2026** is paywalled after its opening section. The entry uses only what that section says.
- **VLGAA-NUCCIO-2026** slides are images. They were read by rendering pages 43-52.
- **Not cited, not opened:** the AICPA practice aid itself (member-gated; entries attribute its content "as reported")
  and the Financial Times story behind FINSTORY-KPMGFEE-2026 (paywalled; `#23` stays C as second-hand). The web
  archive was blocked for this session.

## 5. Targets

| Target | Status |
|---|---|
| 15–25 use cases | Met (25) |
| ≥50% graded A or B | **Not met (44%)**. No A exists: no named organisation has published a measured outcome for AI in planning. Reaching 50% needs two more named deployments (for example a firm-confirmed use of the Caseware or MindBridge risk agents, or a named firm using AI in fraud brainstorming), not regrading |
| Every source has a URL and an ISO date | Met. 83 unique refs in the YAML (plus 13 module-only keys in §10), each with one consistent URL, date and title across entries |
| Vocabulary values, unique ids, D labelled "idea" | Met. `python3 scripts/validate.py` reports no ERROR for these two files (only the A/B-share WARN). Current ERRORs are in `assurance/ARCHETYPE.md` (broken links), which another stream owns |
| Quotations under 25 words | Met |
| Module ≤300 lines, has contents, no build-only references | Met (300 lines; no "pilot", "spec", research paths, deep dives or synthesis report) |

## 6. Error patterns to fix in the briefs

1. **Right figure, wrong document.** KPMG's 2.175 million came from the US member firm's release, but it was cited to
   KPMG International's release from the same week. Brief: when two releases share a title, cite the one whose text
   contains the figure, and grep the opened text for the number before citing.
2. **Build-only citations in content fields.** Five guardrails or checkpoints were cited to "the deep dive's reading"
   or "inferred by the discourse deep dive". Brief: every attributed sentence cites a source key; an inference with no
   source is either cut or written as "not described in the source".
3. **Locator drift inside a vendor's own documents.** Claims made about one Caseware agent were reused as if they
   covered another, and wording from the CwX blog was cited to the launch release. Brief: when one vendor publishes
   several documents, the locator must name the paragraph that contains the exact wording.
4. **Merged speakers.** One SEC official's sentence was combined with another's into a single "SEC staff said". A
   group statement (King & Spalding's summary of several speakers) was assigned to one person. Brief: name the speaker
   at the level the source does.
5. **Dates not on the page.** "2026-04-30" for ISA (UK) 240, a future webinar date given as the publication date, and
   newsletter months that differed from the page date. Brief: use the byline or the document's own date. When none
   exists, use the PDF creation date and say so; never use an event date.
6. **Slide decks read from text extraction.** Image-only slides yielded titles only, and one COSO claim was attached
   to the wrong slide sequence. Brief: render image-only PDFs and cite slide numbers.
7. **Dropped population qualifiers.** "Senior internal audit leaders" left out "North American", and a partner rating
   became a fact about clients. Brief: carry the source's population and respondent type into the outcome's
   `measures`.

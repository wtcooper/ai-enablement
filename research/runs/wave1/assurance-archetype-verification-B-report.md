# Verification report B: assurance archetype prose files

- **Date:** 2026-10-17
- **Files checked and edited:** `ARCHETYPE.md`, `interview-guide.md`, `value-chain.md`, `guardrails.md`, `objections.md`,
  `sources.md` in `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/`.
- **Not touched:** economics.md, state-of-ai.md, frontier.md, disruption.md, workforce.md (another verifier), module
  files and YAML.
- **Method:** every cited source in the six files was opened with curl (133 URLs; pdftotext for PDFs; r.jina.ai where
  curl got 403 or 429). Each claim was checked against the source text. Module ratings were checked against the
  validator's INFO lines. Stage markers were checked against `method/onboarding.md` §5.

## 1. Counts

| | Count |
|---|---|
| Factual claims checked (cited claim sites, module ratings and summaries, stage markers, dates) | about 183 |
| Kept as written | about 122 |
| Fixed (wording, figure, date, attribution, scope or a better source) | 60 |
| Removed | 1 (IVSC 2026 conference date and place) |
| Source entries checked (sources.md Part B plus local lists in guardrails and value-chain) | 133, all with a working URL |
| Source dates added or sharpened | 27 (plus 7 dates moved from ISO format to the file's "8 May 2026" style) |
| Source entries added | 1 (WCARS-2026 in Part B; Part A already cited it) |

Validator: 0 errors. The 8 warnings are unchanged and outside these files (SKILL.md missing; seven YAMLs below the A/B
target). Every bracketed key in the six files resolves. All relative links work. Every file over 100 lines has a table of
contents, and every file is under 300 lines (ARCHETYPE.md is exactly 100).

## 2. Structural checks requested by the caller

- **Module table against the validator.** Every link resolves. A/B counts are now printed in the table (for example
  "strong (16 of 25 A/B)"), with the thresholds stated (strong 50% or more; moderate 30-49%; thin under 30%). Two
  changes: **assurance-over-ai** moved from moderate to thin (6 of 24, 25%: below the threshold, and the module says no
  measured outcome exists). **quality-management** shows 10 of 25. The validator printed 11 of 25 at the start of this
  run and 10 of 25 at the end, because another verifier edited the YAML during the run. It is still moderate. The
  one-line summaries were checked against each module's header and §1. Two were changed: acceptance-independence
  ("AI-driven structural change" overstated the cause) and specialists (now notes that its A/B entries are advisory, not
  audit).
- **Journey-stage markers.** Stage names, the "ready when" gates and the five delegation gates match onboarding §5.
  The plain-text path `method/onboarding.md` is now a relative link. The delegation reference case was reworded to match
  controls-testing `#05`: exceptions go to a reviewer who signs off, not "every conclusion".
- **Guardrails dates.** The following were confirmed at source:
  - QC 1000 amendments: adopted 9 Sep 2026, effective 15 Dec 2026, SEC approval "Pending" on the PCAOB agenda page
    read 17 Oct 2026.
  - ISA (UK) 620: final revisions issued 23 Sep 2026, effective 15 Dec 2026.
  - ISSA 5000: periods beginning on or after 15 Dec 2026, or as at a date on or after 15 Dec 2026.
  - IAASB exposure drafts: published 5 Aug 2026, comments due 15 Dec 2026.
  - SAS 150 and SAS 151: effective for periods ending on or after 15 Dec 2028.
  - EU AI Act high-risk dates: 2 Dec 2027 and 2 Aug 2028.

  The SEC filer-status (404(b)) proposal of 19 May 2026 was missing from guardrails and has been added: comments closed
  20 Jul 2026, not final, and by the SEC's own estimate about half of currently attested issuers would leave 404(b). The
  interview-guide question on it now carries the same date and status.
- **Build-only references.** None found in the six files (no research paths, "pilot", "wave" or "spec").

## 3. Fixes and removals

| File | Claim (before) | Action | Reason |
|---|---|---|---|
| ARCHETYPE | assurance-over-ai evidence "moderate" | Fixed: thin (6 of 24 A/B) | 25% is below the stated 30% threshold; no measured outcome |
| ARCHETYPE | Evidence column without counts | Fixed: counts and thresholds added | Makes ratings checkable against the validator |
| ARCHETYPE | acceptance-independence: "AI-driven structural change ... is where the activity is" | Fixed | Private equity is not AI-driven; the module says regulators focus on structural change around firms |
| ARCHETYPE | Delegation case: "a reviewer signing off every conclusion and exception" | Fixed | YAML `#05` says exceptions go to a reviewer |
| ARCHETYPE | "Regulators expect named owners for each decision checkpoint" | Fixed: "IFIAR suggests firms assign named people" | Source gives this as an example guideline, from one body |
| interview-guide, objections, value-chain | CPA.com sample described as "small" or "small and mid-size" US firms (5 places) | Fixed: "54 US firms surveyed" | Report says "U.S. CPA firms of varying sizes" |
| interview-guide, value-chain | "Internal control testing is the largest single source of findings" | Fixed: largest by number of findings; accounting estimates have the highest share of audits with a finding | IFIAR tables show 213 findings for internal control testing, but 22% of estimates audits against 14% of internal control testing audits |
| interview-guide | SEC filer-status question undated | Fixed: dated 19 May 2026, "not final", with the SEC's half-of-issuers estimate | Uniqus summary of the SEC fact sheet |
| interview-guide | "19% of functions had budget cuts" | Fixed: 19% of 373 respondents | Precision |
| value-chain | Top blockers listed as poor data (60%) and no access (53%) | Fixed: untrained staff (66%) added as the top blocker | CPA.com ranking |
| value-chain | "Most automated steps were the data-in steps" | Fixed: workflow management, foot-and-proof and confirmations (39% each), trial-balance import (35%) | Foot-and-proof is not a data-in step; workflow management was omitted |
| value-chain | Hours saved "show up first as realization or idle capacity" | Fixed: labelled as inference | Unsourced connective claim |
| value-chain | "audit committees run the tender" | Fixed: for listed clients the audit committee oversees the tender | Overstated |
| value-chain | Engagement letter "now including AI use and data consent" | Fixed: where law, contract or firm policy requires it | AICPA: AU-C 210 does not require naming AI tools |
| value-chain | Optro cited for agents that screen uploads | Fixed: Suralink pre-screens; Optro lists automated evidence collection as upcoming | Optro release says "upcoming" |
| value-chain | AS 1105.10A "required" for reliability of client electronic information | Fixed: scope stated (external information the company supplies electronically), plus the PCAOB policy statement of 18 Sep 2025 | PCAOB Release 2025-004, linked from the PCAOB-TAA page |
| value-chain | Data extraction "can decide whether tools can be used at all" | Fixed: "may affect whether a procedure can be performed" | Embellished qualifier |
| value-chain | 88% figure for journal-entry tools | Fixed: "2024 data" added | Date precision |
| guardrails | IFIAR "says audits 'will remain human-led'" | Fixed: firms say it, and IFIAR asks them to spell out what it means | Attribution drift |
| guardrails | PCAOB "supervision and review responsibilities unchanged" listed as what regulators say | Fixed: firms told PCAOB staff their policies had not changed | Attribution drift |
| guardrails | Whether licensing an AI audit tool raises an issue "is unresolved" | Fixed: attributed to a former PCAOB board member's comment letters | The source is one commenter's view |
| guardrails | SOC guidance on AI dated "11 Sep 2026" | Fixed: Section 9561 Q&As, "reported 21 Sep 2026" | Primary text is behind a login; the only opened source (Deloitte DART) is dated 21 Sep |
| guardrails | SOC 2 peer-review "alert (May 2026)" | Fixed: Peer Review Board guidance, 14 May 2026 | Wording and date |
| guardrails | IESBA "no further code changes planned; AI material planned" | Fixed: in force since Dec 2024; no further Code revisions pursued; non-authoritative technology guidance planned | Precision |
| guardrails | "AI Omnibus adopted by 1 Jul 2026" | Fixed: formally adopted (reported 1 Jul 2026) | Precision |
| guardrails | QC 1000 status | Fixed: effective 15 Dec 2026 subject to SEC approval; PCAOB page date given | Exact status |
| guardrails | ISSA 5000 and ISA (UK) 620 rows | Fixed: issue dates added (Nov 2024; 23 Sep 2026), plus the "as at" limb and IAASB alignment | Exactness |
| guardrails | IAASB exposure drafts | Fixed: publication date 5 Aug 2026 added | Exactness |
| guardrails | APS "second exposure draft in preparation, after the October 2026 meeting" | Fixed: first exposure draft Dec 2025; issuing a second to be discussed at an interim October 2026 meeting | Forecast presented as fact |
| guardrails | SAS 150/151 "issued or approved" | Fixed: both issued (13 Jul 2026; SAS 151 published 14 Oct 2026) | Out of date |
| guardrails | (missing) | Added: SEC filer-status proposal row | Requested; dated regulatory change |
| guardrails | FRC supervision "from April 2026" | Fixed: for the largest firms | Scope |
| guardrails | CPAB "first public AI-type finding" | Fixed: automated tools, not specifically AI; "in one tool" | Embellishment |
| guardrails | IAASB rejected a requirement "because for GenAI that may be impossible" | Fixed: "partly because ... may not be possible to fully evaluate" | Embellished qualifier |
| guardrails | AI literacy duty cited to the provisional agreement | Fixed: cited to the adopted text, with its wording | Better source |
| guardrails | SEC and PCAOB review "prompted by private equity and AI" | Fixed: the SEC Chief Accountant cites them; PCAOB staff proposal Q1 2027 | The PCAOB agenda cites "changes to the audit environment" |
| guardrails | AICPA SOC terms "control, judgment, fees or evidence access" | Fixed: "financial dependency" | Source wording |
| guardrails | IESBA opaque output "not acceptable without assessing fitness, limits and data quality" | Fixed: source wording | Added qualifiers |
| guardrails | Hohl FAQs "(June 2026)" | Fixed: remarks in May and June 2026 | Ambiguous date |
| objections | "about two-thirds of audit committees have raised it" | Fixed: two-thirds of audit partners say audit committees raised AI; 6% rate governance advanced | Misread statistic |
| objections | "The shortage is at the experienced layer" [FRC-ARAQ] | Fixed: the FRC reports elevated attrition among experienced staff; Big Four UK entry-level intake fell from 6,500 to 5,400 | FRC does not describe a shortage layer |
| objections | FRC private-capital letter names "technology and succession" as benefits | Fixed: investment in audit quality, innovation and choice | Not in source |
| objections | "the PCAOB's acting chair" | Fixed: "then acting chair" | Dated (Dec 2025) |
| objections | "The only controlled study" on skill formation | Fixed: "A randomised study (software developers)" | Unverifiable superlative |
| objections | PwC "calls savings" and "report 'still looks the same'" | Fixed: named role; second item as a paraphrase, not a quote | The second is the reporter's paraphrase |
| objections | Revenue growth at "all four networks" with three citations | Fixed: PwC citation added; "audit and assurance" | Unsupported for PwC |
| objections | PwC discounts on "consulting work" | Fixed: services such as systems integration, not audit | Source wording |
| objections | IAASB "penalises unstructured inputs" | Fixed: may need more extensive evaluation | Embellished |
| objections | Benchmark: models "do much staff-level work" | Fixed: on synthetic engagements, "substantial parts ... well" | Precision |
| objections | "A vendor's own certification covers its platform, not your use of it" | Fixed: KPMG's AIUC-1 certificate covers one platform; labelled inference | Inference, not the source's claim |
| objections | Human in the loop: "named owners ... [IFIAR]"; CPAB "defined involvement at each stage" | Fixed to source wording | Paraphrase drift |
| objections | "It is unresolved" (licensing AI tools) | Fixed: "an open question" | Tone |
| sources | IVSC AGM & Conference "16-18 Nov 2026, Cologne" | **Removed** date and place | The cited IVSC paper does not contain it; the IVSC event page returns "Page not found" |
| sources | ISACA NA "6-8 May 2026" | Fixed: next edition (5-7 May 2027, Chicago) added | Page now shows 2027 |
| sources | IAASB webinars "Sep-Oct 2026" | Fixed: two-part series from 29 Sep 2026 | Source |
| sources | CPA.com described as "the main small-firm benchmark" | Fixed: 54-firm US benchmark, firms of varying sizes | Source |
| sources | Undated or year-only entries | Fixed. Dated: FRC-620 (23 Sep 2026), CASEWARE-VERITY (17 Jun 2026; title corrected), CPACOM-DCPA (11 Sep 2025), IIA-GAM (3 Feb 2026), IIA-INTL (28 May 2026), ISCA-LAWSHEN (17 Sep 2024). Given access dates: AIACT-ANNEX3 (with Regulation 2024/1689 date), BLS-OOH, PCAOB-SSR-PAGE, ICAEW-AAC, KPMGUK-GOVAI, ISACA-NA, INFLO, SURALINK, VALIDIS | Every source needs a date |
| sources | Month-only dates | Fixed: DART-TQA 21 Sep, IAASB-EDPAGE 5 Aug, JOFA-COSO 26 Feb, JOFA-PEEC 10 Aug, JOFA-PEER 14 May, JOFA-QC1000 9 Sep, JOFA-SAS150 14 Jul, JOFA-SAS151 20 Aug (updated 15 Oct) 2026; IIA-PULSE-2024 fieldwork dates; ACCTEU file date | Exactness |
| sources | WCARS-2026 cited in Part A but listed only in frontier.md | Fixed: added to Part B | Shared keys belong in Part B. frontier.md's local copy can now be dropped by its verifier |

## 4. Sources that could not be reached or confirmed

- **AICPA TQA Section 9561** (the SOC 1 and SOC 2 AI Q&As): primary text is behind a login. Only Deloitte DART's 21 Sep
  2026 note was read, so the earlier "11 Sep 2026" date could not be confirmed.
- **IVSC 2026 AGM and conference page:** "Page not found" through both curl and r.jina.ai.
- **Blocked to direct curl, read through r.jina.ai:** BLS OOH (403), Cloud Security Alliance (403), IVSC AI paper (429),
  PCAOB AS 2310, technology-assisted-analysis and standard-setting pages (403).
- **KPMG-HOHL-2026:** the page gives no exact day (kept as May 2026).
- **ISACA NA 2026 dates:** the page now shows the 2027 edition. The 2026 dates come from an earlier read and could not be
  re-confirmed.

## 5. Error patterns seen

- **Misread statistics:**
  - CAQ: partners' answers were reported as a share of audit committees.
  - IFIAR: "largest source" without saying it is by count.
  - CPA.com: the sample was described as small firms.
- **Attribution drift:**
  - Firms' statements credited to IFIAR and to PCAOB staff.
  - One commenter's view stated as fact (AT-PEEC).
  - Benefits the FRC letter does not name.
  - A "shortage layer" the FRC does not describe.
- **Embellished qualifiers:** "impossible", "at all", "penalises", "every conclusion", "AI-type finding", "only
  controlled study", "AI-driven structural change".
- **Unsourced connective claims:** hours saved showing up as realization; audit committees running tenders;
  certification scope versus use. Each is now labelled as inference or reworded.
- **Wrong or soft dates:** the TQA date; SAS 151 status; about 27 year-only, month-only or undated source entries.
- **Forecasts presented as facts:** the APS second exposure draft "after the October meeting".
- **Grade or rating inflation:** assurance-over-ai labelled moderate at 25% A/B.

## 6. Notes for other files

- **quality-management module:** its header still says "not yet source-verified".
- **frontier.md:** its local WCARS-2026 entry duplicates the new Part B entry.
- **Module A/B counts:** they changed during the run because another verifier was editing the YAML. Re-run the
  validator and refresh the ARCHETYPE.md counts after the module verifiers finish.

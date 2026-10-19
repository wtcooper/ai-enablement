# Verification report: professional-services / quality-review

Checked 2026-10-19 against the sources themselves. Routes used: the r.jina.ai mirror, direct fetch (raw HTML for
dates), pdftotext for PDFs, the arXiv export endpoint and the Hacker News API. No web search was used.

Files edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/quality-review.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/quality-review.md`

All 86 cited sources in the two files (85 distinct URLs) were opened, plus the Law Society's full agentic AI report (PDF). Every
figure in a B entry was matched to the source text.

## Counts

| Action | Entries |
|---|---|
| Kept | 1 (`-09`) |
| Fixed | 17 (all others) |
| Rejected | 0 |

Most fixes are wording, attribution, locators or dates. No grade changed.

## Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 0 | 0 |
| B | 11 | 11 |
| C | 6 | 6 |
| D | 1 | 1 (`-12`, labelled "Idea") |

`-05` stays B. Linklaters' own benchmark measures model output, not review, so this evidence from an adjacent process
caps the grade at B. The note in `-05` now says so. `-11` keeps its existing adjacent-process cap: its figures come
from contract redlining.

## Fixes and rejections

Ids are shortened: `-08` means `professional-services-quality-review-08`.

| Id | Field | Change | Reason |
|---|---|---|---|
| `-01` | solution | "One top-10 US litigation firm is reported to require" changed to "a litigator told Filevine's CEO that his top-10 firm requires". The locator is now the right section | Embellished: the source says "top-10 firm", not "US litigation firm". The anecdote is in "Citators As An Essential Tool" |
| `-01` | solution, role_evolution | California "expects" and "explicit duty" changed to "should set policies, provide training and update controls" | The guidance uses "should" (p.7). The wording overstated it |
| `-01` | outcomes (Law360) | `measures` now says the 258 leaders were from consulting, accounting and legal firms in the UK and US. It also says what the 85% counts | The sample frame was hidden |
| `-01` | risks (Gordon Rees) | Removed "a written policy did not prevent..." and "the firm later said it had updated its AI policies". Kept the admission and the $55,000 reimbursement | The GigaLaw source says nothing about policies. The Bloomberg Law original is paywalled |
| `-01` | human_checkpoints | "Confirms authorities exist and are accurately cited" (Florida's wording) changed to California's p.9 duty to review and independently verify | The wording came from a different document |
| `-01`, `-11`, `-16` | ILTA source date | `2026-06` changed to `2026`. Locators now give PDF p.5 for Q3.18 | The PDF has no date. Its metadata show creation on 2026-08-14, and only the file name ("2606_") suggests June. This matches the work-production verification |
| `-02` | problem | "Fabricated support often sits in a dissent or case history rather than in a fake case" changed to "...rather than in the holding, even when the case itself is real" | The quotation was wrong |
| `-02` | risks | The untested reversal case is now stated precisely. "No checker publishes a false-negative rate" now notes GPTZero's untested 99-in-100 claim, and GPTZERO-KPMG-2026 is added to sources | The reversal wording was imprecise, and the false-negative claim was overstated |
| `-02` | role_evolution | "Expects citation validation to become a required step" changed to "argues it is now a required step" | Misquoted tense |
| `-03` | solution | "ABA 512 mentions marking AI material" changed to "a footnote gives, as a training suggestion" | Embellished: this is footnote 52, not the opinion's text |
| `-03` | risks, role_evolution | "The record shows a check was run, not that it was right" is now labelled inference. The role sentence now uses the CEO's sourced words | Connective claims with no source |
| `-04` | human_checkpoints | "Independent reviewer signs off... (ICMCI 2.2)" split into an idea and ICMCI's actual point (the consultant keeps responsibility) | Section 2.2 says nothing about an independent reviewer |
| `-04` | notes | Removed "GPTZero puts the Deloitte refund at AUD 98,000". The 40-of-45 note now says GPTZero counts 40 of 45 *titles* as fake and at least 16 citations as hallucinations | The figure is not in any cited source. The 40/45 statistic measures titles, not citations |
| `-04` | CTV-DELOITTE-NL-2025 date | `2025-11-29` changed to `2025-11-26` | Byline date (the 29th is an update) |
| `-05` | role_evolution | Removed "KM and innovation staff become test designers and scorers". Replaced with Linklaters' markers and the ILTACON abstract's actual words (attorney-led testing), plus "no source says which team owns testing" | Embellished: the session abstract does not say this |
| `-05` | risks | Stanford versions "since replaced" changed to "appear to be older versions, since updated (LLRX author)". The reviewer-catch-rate line is restated as a finding of this review | Embellished qualifier, and a connective claim |
| `-05` | notes | Added the grade note: an adjacent process caps the grade at B | Coordinator's grading note |
| `-06` | outcomes | "One issue kept a higher false-positive rate" changed to name the issues: 4 and 9 perfect; 5 and 6 slightly worse in round four; 8 persistently higher | The vague figure did not match the case study |
| `-06` | risks | "Not a defensibility-grade validation of recall" changed to the author's point: the matter did not need defensible recall, so this was not a pure TAR validation | Paraphrase drift |
| `-07` | risks | "Evaluations built from own precedents may miss errors" labelled inference | No source |
| `-08` | risks (California) | Locator `pp.2 and 4` changed to `pp.3 and 5` | The autonomy-supervision statement is on pp.3 and 5 |
| `-08` | role_evolution | "Innovation teams define the templates" now cites Harvey ("can define") | No source |
| `-10` | solution | Schellman "review depth rising with consequence" changed to the CEO's words: "apply controls based on impact" | The rising-depth framing was the journalist's |
| `-10` | risks | "Reviewers are short of time and trust colleagues" now credited to one MindBridge methodology lead | One person's speculation was presented as a general finding |
| `-10` | FRC locator | p.16 changed to p.17 | The AI section is on p.17 |
| `-11` | problem | "Firms rarely know how often reviewers accept or reject" now rests on ILTA's tracking-tools finding | Connective claim with no source |
| `-12` | human_checkpoints | "The lawyer remains accountable (STENO)" changed to "written principles name who is accountable and where the lawyer intervenes" | The recap says organisations need such principles, not that the lawyer is accountable |
| `-13` | problem | Litera "recheck every AI-edited clause" changed to "recheck every result" | Litera's wording |
| `-14` | risks | "Courts treat concealment as worse than the error" changed to "courts have criticised quiet corrections and a revised brief that did not disclose AI's role" | Embellished: neither source says "worse than the error" |
| `-14` | human_checkpoints | "Client reviews the revised deliverable" changed to "Deloitte reviewed the report and confirmed the errors" | The source does not say the client reviewed it |
| `-15` | outcomes, locator | The 18-of-45 schedule moved from "the Haringey matter" to Al-Haroun v Qatar National Bank (decided with Ayinde) | Wrong matter: para 74 is the Al-Haroun case |
| `-15` | solution | "Haringey Council asked for copies of cases" changed to "Haringey's solicitor wrote that five cited cases could not be found" | Wrong actor: the claimant's own solicitors asked counsel for copies (paras 39-40) |
| `-16` | role_evolution | "Many partners have not discussed AI with most clients" changed to "more than a third of stand-out lawyers had discussed AI with fewer than 20% of clients". The locator is fixed | The figure was misdescribed |
| `-17` | solution, risks | "Treat prompts as records" changed to the report's warning that organisations are not managing them. "Discoverable records" changed to "swept into legal holds" | Embellished |
| `-18` | risks, problem | DAC Beachcroft and broker points restated: many policies may respond and wording is unclear; most law-firm policies have no express AI exclusion; the Law Society point is the interviewees' view | Embellished: "coverage uncertain", "exclusion wording varies" |
| `-18` | outcomes | Broker forecast provenance changed from `self-reported` to `independent` | The broker is not the deploying organisation |
| `-18` | sources | The full Law Society report now has its own key, LAWSOC-AGENTICFULL-2026 (PDF URL, `2026-04`) | One ref was pointing to two documents (the summary page and the full report) |
| `-03`, `-18` | IAMAG URL | Changed to the canonical article URL | `?p=` redirect |
| Module | §2 | Supervisory-review, record and incident-response pain points restated | They mirrored the YAML embellishments above |
| Module | §5 | The Stanford "replaced" wording is fixed. Linklaters is labelled as a model-output measure. The Charlotin alleged-AI caveat is added. "Ayinde 18 of 45" changed to Al-Haroun | Same reasons as the YAML |
| Module | §6 | "ISQM 1 and SQMS 1 frame AI tools as firm resources" changed to a CIBA author's argument about ISQM 1 only. Insurer wording restated | Wrong attribution: an author's argument was presented as the standards' content, and the article does not mention SQMS 1 |
| Module | §7 | California "explicit duties" changed to "should" | Overstated |
| Module | §8 | Webinar dated 2026-11-11. "BriefCatch launches" changed to "makes generally available". GPTZero range set to 2026-05 to 2026-07-29, and "withdrawals follow" changed to "EY Canada and KPMG withdraw; PwC Middle East corrects citations". "Move toward sampling" changed to "teams experimenting" | Dates and embellishment |
| Module | §9 | Added a source for "no one has measured it". The reviewer-time claim is credited to one practitioner. Deloitte is now cited. "Some bar it" changed to "some require permission" | Unsourced or overstated |

## Sources that could not be reached

- **SRA warning notice** (sra.org.uk): 403 and a bot wall through the mirror. The 42-report figure stays on the
  secondary Law Society of Ireland Gazette report (LAWSOCIE-SRAWARN-2026), which is labelled secondary in §10.
- **Bloomberg Law, Gordon Rees** (behind the GigaLaw summary): paywalled. The policy claims that depended on it were
  removed.
- **Primary documents cited second-hand and not opened:**
  - The Sullivan & Cromwell letter. Canadian Lawyer links a PDF, but the claims rest on the article.
  - The Johnson v. Dunn order (via EDRM).
  - Reddy v. Saroya (via Canadian Lawyer).
  - The Casepoint whitepaper, which sits behind a download form.

  Each entry already says this.
- **ABA Formal Opinion 512:** read from the LawNext-hosted copy, as before.
- **Dates found in page metadata, not the byline:**
  - Vals VLAIR (dateModified 2025-02-27).
  - Thomson Reuters pages (byline or JSON-LD).
  - Harvey posts (datePublished).
  - The EY/ACS byline (May 19 2026).
  - Job postings (datePosted).
  - The Hacker News thread (API timestamp 2026-06-14).
- **Undated sources:** TR-FOP-2026 and LAWSOC-GENAI-2026 stay year-only.

## Module targets

| Target | Result |
|---|---|
| 15-25 use cases | 18: met |
| At least 50% graded A or B | 11 of 18 (61%): met |
| Every source dated | Yes. ILTA, TR-FOP-2026 and LAWSOC-GENAI-2026 are year-only |
| Ids unique, vocabulary values, quotations under 25 words | Yes |
| Cross-references | All 35 cross-module ids exist, and their titles match the claims made |
| Validator | The final run of `scripts/validate.py` reports 0 errors (22 warnings, none in these files). The module is 277 lines |

## Cross-module issues for the coordinator

- **ILTA-TECHSURVEY-2026** is still `2026-06` in five other professional-services files: acceptance-risk,
  firm-finance, knowledge-management, scoping-pricing and talent-learning. This file and work-production now use
  `2026`.
- **LAWSOC-AGENTIC-2026** is used for the summary page elsewhere. The full report is now LAWSOC-AGENTICFULL-2026.
  Check acceptance-risk, which routed the p.45 insurance point here.
- **"Haringey" / "Ayinde" 18-of-45:** if other modules cite this figure, it belongs to Al-Haroun.

## Error patterns to fix in the briefs

1. **A claim credited to the wrong document, matter or speaker:**
   - The Al-Haroun schedule was credited to Haringey.
   - Haringey's solicitor was described as "asking for copies".
   - An ISQM argument by a CIBA author was presented as the standards' own content.
   - A journalist's framing was credited to Schellman's CEO.
   - Florida's rule wording was credited to California.
   - The AUD 98,000 figure is in no cited source.

   Ask briefs to put the locator of the exact sentence beside every figure.
2. **Embellished qualifiers:**
   - "Top-10 US litigation firm".
   - "Concealment worse than the error".
   - "Explicit duty".
   - "Since replaced".
   - "Discoverable".
   - "Exclusion wording varies".
   - "Move toward sampling".
   - "Withdrawals follow" (PwC corrected its citations rather than withdrawing).
3. **A statistic reported as something it doesn't measure:**
   - GPTZero's 40 of 45 counts titles, not citations.
   - The stand-out lawyer figure was turned into "most clients".
   - The Law360 sample frame was hidden.
4. **Unsourced connective claims:**
   - In `role_evolution`: `-03`, `-05`, `-08`.
   - In `risks_and_guardrails`: `-03`, `-05`, `-07`, `-18`.
   - In `problem`: `-11`.

   Require a source ref on every sentence in these fields, or the label "inference".
5. **Dates:**
   - The ILTA date came from a file name.
   - The CTV date was the update date, not the byline.
   - A webinar was given its month only.

   Ask for the byline, JSON-LD or PDF metadata, and use year-only dates when none exists.
6. **A grade inflated by an adjacent process:** none was inflated. `-05` and `-11` were already capped at B, and the
   cap is now stated in the notes.
7. **Search-only figures in A or B entries:** none. Every source was read in full.

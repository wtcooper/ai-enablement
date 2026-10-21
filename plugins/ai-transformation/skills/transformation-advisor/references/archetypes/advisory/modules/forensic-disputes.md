# Forensic and disputes (advisory)

Sources checked 2026-10-20. Use cases live in `../use-cases/forensic-disputes.yaml` (15 entries). Ids are shortened
here: `#05` means `advisory-forensic-disputes-05`; other archetypes' ids are given in full. Source keys in brackets,
such as [ACFE-RTTN-2026], are given in full in the YAML or in §10. Read this first: **no accounting-firm forensic
practice has published a measured AI outcome** (no error rate, override rate or parallel-run result). No entry is
graded A; 6 of 15 are B. The best numbers come from adjacent work (e-discovery review, corporate anti-fraud programs,
federal judges). The firm with the most public detail, J.S. Held, is a forensic and consulting firm, not a CPA firm,
and says it provides no attest services [JSHELD-AIEXPERT-2026].

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

Fraud investigations, litigation support, damages and loss quantification, and expert-witness work done by
accounting, advisory and forensic firms for clients and their counsel. It also covers the evidence rules that decide
whether AI-assisted analysis survives in court, and the new demand created by AI-enabled fraud and deepfakes. Practice
today is mostly AI-assisted data preparation and document review; the binding constraint is evidence law, not
capability. Fraud-risk program design sits in risk-controls; valuation work in valuation; pricing, staffing and firm
quality in professional-services.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Allegation intake and triage | Complaint or hotline tip, scoping, privilege set-up | review-assurance | Tips are the top detection source, 43% of 2,402 cases [ACFE-RTTN-2026]; no AI intake evidence found |
| Evidence preservation and collection | Legal hold, forensic imaging, collection from email, chat and now enterprise AI tools | data-reporting | AI chats sit in tools that legal-hold processes were not built for [RELATIVITY-AIR-2026] |
| Data preparation | Turn statements, checks and ledgers into structured data | data-reporting | Once took as much as 50% of project budgets, per J.S. Held; poor scans [JSHELD-AIFRAUD-2026] |
| Forensic analytics and tracing | Matching, anomaly tests, fund tracing, lifestyle and bank-deposit analysis | data-reporting | Slow by hand across thousands of items; lapping (one customer's payment applied to another's account) is hard to see without matching every item |
| Document and email review | First-pass review, issue coding, privilege, red flags | research-synthesis, review-assurance | High first-level review cost; reviewers and the expert disagree materially [CGP-ARXIV-2026] |
| Interviews and fact-finding | Interviews, follow-up requests | client-interaction, expert-judgment | No public AI use case found |
| Damages and loss quantification | Loss, lost-profit and misapplied-payment calculations | expert-judgment, data-reporting | A Copilot cross-check was rejected in *Matter of Weber* [AICPA-COPILOT-2025] |
| Report, exhibits and testimony | Drafting, charts, rebuttal, deposition and trial | document-production, expert-judgment | AI-fabricated citations got a declaration excluded in *Kohls v. Ellison* [KTS-EXPERTAI-2026] |
| Disclosure and admissibility | Telling counsel and courts about AI use; reliability showings | review-assurance | No bright-line rule on AI in expert opinions [AICPA-COPILOT-2025]; Rule 707 unsettled [USCOURTS-STDCOMM-2026] |

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path,
exceptions to people), delegate (an agent owns a multi-step outcome), reinvent (the service or model changes).
**Delegate has no evidence in this module**; the only "agentic" mention is a talk not yet given (`#13`).

**Data preparation, analytics and tracing**
- Improve: `#01` AI-enhanced OCR (reading text from images) turns bank, check and brokerage records into structured
  data linked to source (J.S. Held: 25,000+ checks ready "in days rather than weeks", self-reported; Valid8 vendor
  claims). `#13` idea: agentic crypto fund tracing (scheduled AICPA FVS talk only).
- Automate: `#02` software matches every check and transaction to bank records and flags gaps; forensic accountants
  work the flags and quantify loss (J.S. Held: 20,000 transactions matched "in just hours"; findings over $37M in two
  matters, unnamed clients).

**Detection inside client anti-fraud programs**
- Improve (process): `#03` continuous data monitoring and machine-learning anomaly flags. ACFE links proactive
  monitoring with lower median losses; this is analytics in general, not AI. Program design is risk-controls work.

**Document review and early case assessment**
- Improve: `#04` large-language-model first-pass review against the written protocol, validated by sampling (Redgrave
  case study, re-analysed and contested by independent academics). `#08` red-flag screening of documents and emails
  in fraud work (practitioner recollection; Diligent's board-pack screening announced). `#05` cited answers to
  plain-language questions over the matter set (vendor only).
- Evidence collection: `#10` collecting employees' enterprise AI chats as evidence (vendor capability claim).
- Related: `professional-services-quality-review-06` (validating AI document review inside a matter).

**Expert analysis, reports and testimony**
- Improve: `#06` J.S. Held's IP practice builds sandboxed models, has a managing director review every item and
  double-checks with traditional methods (no results published). `#09` first drafts of report skeletons, narratives
  and charts (training deck and survey only). `#14` idea: AI critique of opposing reports and cross-examination prep.
- Control layer: `#07` engagement-letter terms for AI disclosure, independent verification, closed tools and logs;
  J.S. Held tells clients it will use AI unless they opt out. Related: `professional-services-quality-review-02`,
  `professional-services-quality-review-03`, `professional-services-quality-review-16`, `tax-controversy-08`.

**New services (reinvent; all ideas)**
- `#11` examining whether challenged audio, video or documents are AI-generated or altered.
- `#12` investigating AI-fuelled fraud (deepfake impersonation, forged documents, business email compromise) and
  AI-washing (overstated AI claims). Prevention stays in client-accounting-services and risk-controls.
- `#15` validation studies and error-rate testing to meet or challenge a reliability standard such as Rule 707.

## 4. Interview probes

1. When someone on the team uses a generative-AI or analytics tool on a matter, what do you record (prompt, tool
   version, inputs, verification), and could you reproduce the result at a deposition? *Reveals exposure to the
   Weber reproducibility failure and readiness for `#07`.*
2. Has counsel, a court or an opposing expert asked whether AI was used? *Shows how close the disclosure duty is; J.S.
   Held expects such questions [JSHELD-AIEXPERT-2026].*
3. What share of project hours goes to getting data usable before analysis, and how do you validate extraction
   (balance checks, re-performance)? *Sizes `#01` and `#02`; J.S. Held cites up to 50% of budgets.*
4. Which error, exception or false-positive rates do you track on matching or anomaly tools? *No such rates are
   published anywhere. Reveals whether any claim of value can be shown.*
5. For document review, do you validate against a sample coded by a subject-matter expert, and whose coding counts as
   correct? *Readiness for `#04`; ground truth itself is contested [CGP-ARXIV-2026].*
6. Which tools may touch client or protective-order material, are consumer tools barred, and do engagement letters
   disclose AI use or let clients opt out? *Tests `#07` and `#14` controls and the consent question [JOFA-ETHICSAI-2026].*
7. Are any of your forensic or expert clients also audit clients of your firm or an affiliate, and who checks before
   you accept? *Expert advocacy services for issuer audit clients impair independence [SEC-RULE2-01-2026].*
8. What will you not let AI do in an opinion, and can each expert explain the method without the tool? *Shows where
   human judgment is designed in; Kohls turned on unverified output.*
9. If a client or court challenged an audio, video or document as fabricated, what is your protocol, and do you bill
   for it? *Readiness for `#11` as a service.*
10. Are clients bringing deepfake, business-email-compromise or AI-washing matters? *Demand for `#12`.*
11. If first-pass review and data preparation shrink, how will juniors learn tracing and review, and what changes in
    staffing and pricing? *Routes to professional-services; no forensic-specific evidence exists.*

## 5. Metrics and benchmarks

| Metric | Figure | Provenance | Source |
|---|---|---|---|
| Data preparation share before AI | Up to 50% of project budgets | self-reported | [JSHELD-AIFRAUD-2026] |
| Check and transaction processing | 25,000+ checks in days; 20,000 transactions in hours (narrative, unnamed clients) | self-reported | [JSHELD-AIFRAUD-2026] |
| Extraction accuracy | About 85% hand-keyed vs 99-100% AI (a practitioner's recollection) | vendor-published | [VALID8-WP-2025] |
| Proactive data monitoring (not AI-specific) | Median loss $70,000 vs $150,000; 9 vs 16 months; in place in 49% of 2,402 cases | independent | [ACFE-RTTN-2026] |
| How frauds are first detected | Tips 43%; automated transaction or data monitoring 3% | independent | [ACFE-RTTN-2026] |
| Anti-fraud AI adoption (n=713) | AI/ML 25% (18% in 2024); genAI 16%, 58% plan to; report writing 45% of genAI users | vendor-published | [ACFE-TECHBENCH-2026] |
| Anti-fraud AI governance | 18% test models for bias; 6% fully confident explaining models; 84% cite budget as a barrier | vendor-published | [ACFE-TECHBENCH-2026] |
| Readiness for AI-fuelled fraud | 7% more than moderately prepared; 85% of 373 internal audit leaders rate it moderate to high risk | vendor-published; independent | [ACFE-TECHBENCH-2026; IAF-AIFRAUD-2026] |
| Payments fraud (treasury survey) | 76% attempted or actual in 2025; 74% hit by business email compromise; 17% use AI against it | independent | [AFP-PAYFRAUD-2026] |
| Gen-AI document review (Redgrave data) | Recall 87.7% vs 64.4%; precision 28.6% vs 39.2% (aiR vs managed review); comparison disputed | independent re-analysis | [CGP-ARXIV-2026] |
| Human reviewer disagreement | Reviewers missed 34% of expert-responsive documents; expert rejected 61% of reviewer-responsive ones | independent | [CGP-ARXIV-2026] |
| Vendor review claims | 90%+ recall; +36% recall in one dataset | vendor-published | [RELATIVITY-AIR-2026; EVERLAW-GENAI-2024] |
| Deepfake challenges in court | 15 of 931 responding federal judges (about 2%) | independent | [USCOURTS-EVAGENDA-2026] |
| Rule 707 comment record | More than 70 written comments and two hearings | independent | [USCOURTS-EVAGENDA-2026] |
| Literature | 76 documents reviewed; ML tends to beat rules where data quality is high, not universally | independent | [JRFM-FORENSICAI-2026] |
| Hallucination measurement (OSINT, cyber investigations) | Measured end to end in one system (4%, favourable conditions) | independent | [OSINT-ARXIV-2026] |
| Accounting-firm forensic AI quality | No error, override or parallel-run figure found | none | gap |

## 6. Guardrails

**Evidence law already applies.** *Kohls v. Ellison* (D. Minn., 2025-01-10) excluded an expert declaration in full
for unverified GPT-4o citations, though the errors were called innocent; *Matter of Weber* (N.Y. Sur. Ct., 2024)
rejected a damages expert's Copilot cross-check after the judge re-ran it and got different numbers, and said counsel
must disclose AI use before such evidence is introduced [KTS-EXPERTAI-2026; AICPA-COPILOT-2025; PPC-KOHLS-2025].

**Proposed Federal Rule of Evidence 707 is not law.** As drafted it would apply Rule 702 reliability tests to machine
output offered without an expert [USCOURTS-FRE707-2025]. Published August 2025; committee met 2026-05-07; the
September 2026 Standing Committee report lists only "continued consideration" [USCOURTS-STDCOMM-2026]. A possible Rule
901(c) on deepfakes was prepared but not approved, and the Justice Department raised concerns about Rule 707
[USCOURTS-EVAGENDA-2026].

**Professional guidance.** AICPA FVS committee guidelines (October 2025, members-only, not a standard) remind members
to align AI use with engagement terms, confidentiality and judgment [BVR-AICPAAIGUIDE-2025]. UK: the Civil Justice
Council has proposed that experts explain AI use (law-firm summary seen in search only) [HSFKRAMER-CJC-2026].

**Enforcement context.** DOJ's September 2024 compliance guidance asks how a company manages AI risk [DOJ-ECCP-2024].
FinCEN's November 2024 alert lists deepfake red flags for financial institutions [FINCEN-DEEPFAKE-2024].

**Independence (where the firm also audits the client).** SEC Rule 2-01(c)(4)(x) treats expert opinions or services
to advocate an issuer audit client's interests in litigation or regulatory proceedings as impairing independence;
factual accounts of work performed are carved out [SEC-RULE2-01-2026]. Treatment under the AICPA Code for private
attest clients was not confirmed in the research. The AICPA says developing or hosting an AI system for an attest
client can raise independence concerns [JOFA-ETHICSAI-2026]. Related: `assurance-acceptance-independence-15`.

**Confidentiality.** Ask whether client consent is needed before client data goes into an AI tool [JOFA-ETHICSAI-2026].
Keep protective-order and opposing-party material out of non-closed tools; model clauses bar consumer tools and
same-tool verification [KTS-EXPERTAI-2026].

**Steps that need human judgment:** deciding whether a flagged anomaly is fraud [CPAPA-FORENSICAI-2025]; interpreting
matches and calculating damages [JSHELD-AIFRAUD-2026]; validating review output against an expert-coded sample
[CGP-ARXIV-2026]; authoring every opinion and explaining the method without the tool [KTS-EXPERTAI-2026]; testimony,
since AI "cannot take an oath" or withstand cross-examination, per a BRG author [CPAPA-FORENSICAI-2025]; and
admissibility, which the court decides.

## 7. Roles and how they evolve

- The common claim is that AI changes the work, not the role: a BRG managing director says it cannot replace
  judgment or testimony [CPAPA-FORENSICAI-2025]; J.S. Held says professionals will spend more time thinking and less
  time processing [JSHELD-AIFRAUD-2026].
- First-level document review is the explicit comparison target; the Redgrave study pitted the tool against junior
  contract lawyers [CGP-ARXIV-2026].
- Experts take on new duties: disclosure, verification logs, and readiness to be asked about AI use
  [JSHELD-AIEXPERT-2026; KTS-EXPERTAI-2026]. Investigators need skill in interpreting model output
  [JRFM-FORENSICAI-2026].
- AI labs are recruiting forensic accountants as trainers and graders (damages, asset tracing, expert report writing)
  at $75-$150 an hour, posted 2026-08-14 [AFTERQUERY-JOB-2026]. A market signal, not a firm's use.
- Junior pipeline: no forensic-specific source. In quality-of-earnings work, Forvis Mazars warns that depleting junior
  ranks will leave holes in future executive-level insight [FORVIS-QOE-2026]. See
  `professional-services-talent-learning-07` for redesigned entry-level roles.

## 8. Frontier

- **2025-01-10:** *Kohls v. Ellison* excludes an AI-tainted expert declaration [KTS-EXPERTAI-2026].
- **2025-09-09:** Alameda County court dismisses a case as a terminating sanction over AI-generated evidence;
  reconsideration denied 2025-11-06 [NBC-DEEPFAKE-2025].
- **2025-10:** AICPA FVS committee issues AI guidelines for forensic and valuation work [BVR-AICPAAIGUIDE-2025].
- **2026-01 to 2026-08-27:** FJC deepfake survey of judges; evidence committee meets 2026-05-07; Standing Committee
  keeps Rule 707 under "continued consideration" [USCOURTS-EVAGENDA-2026; USCOURTS-STDCOMM-2026].
- **2026-03-25:** 58% of anti-fraud respondents plan to use genAI; deepfake and forged-document fraud reported rising
  [ACFE-TECHBENCH-2026].
- **2026-04:** a deal tracker reports EisnerAmper buying KLG Business Valuators & Forensic Accountants and J.S. Held
  buying CMM, LLP; the tracker reads this as PE-backed platforms buying forensic and litigation niches
  [CPATRENDLINES-TRACKER-2026]. Ownership questions route to professional-services.
- **2026-05-21:** J.S. Held publishes AI-assisted tracing case studies [JSHELD-AIFRAUD-2026].
- **2026-08-31:** law-firm guidance to rewrite expert engagement agreements for AI [KTS-EXPERTAI-2026].
- **2026-10-12:** independent re-analysis disputes the first public head-to-head of gen-AI against managed review
  [CGP-ARXIV-2026].
- **2026-10-20 (page accessed):** Relativity lists collection from enterprise AI tools such as Claude Enterprise and
  ChatGPT Enterprise [RELATIVITY-AIR-2026].
- **Scheduled, not yet given:** AICPA FVS Conference 2026-11-04 to 11-06 (sessions on court treatment of AI expert
  evidence, explaining AI to a trier of fact, AI ethics in testimony, blockchain tracing with agentic AI, AI-enabled
  elder fraud) [AICPA-FVS-2026]; ACFE Fraud Conference Canada from 2026-11-15 with an ethical-AI pre-conference
  [ACFE-CANADA-2026].

## 9. Common objections

| Objection | Evidence-based response |
|---|---|
| "Courts won't accept AI-assisted analysis." | The exclusions so far turned on unverified or unreproducible output (*Kohls*, *Weber*), not on AI use as such [KTS-EXPERTAI-2026]. Model engagement terms call for disclosure, verification not using the same tool, and prompt and output logs; J.S. Held double-checks AI analyses with traditional methods [JSHELD-AIEXPERT-2026]. Rule 707 is still a proposal [USCOURTS-STDCOMM-2026]. |
| "Vendor figures prove gen-AI review beats people." | The flagship comparison is disputed by independent academics, and reviewers and experts disagree on what is responsive [CGP-ARXIV-2026]. Validate on your own expert-coded sample (`#04`). |
| "AI flags will send us chasing false positives." | A real risk, named by practitioners [CPAPA-FORENSICAI-2025]. No false-positive rates are published, so measure your own and keep interpretation with a forensic accountant. |
| "We can't put client data into AI." | Use closed or sandboxed tools (J.S. Held) and engagement terms with an opt-out [JSHELD-AIEXPERT-2026]; answer the consent question first [JOFA-ETHICSAI-2026]; keep protective-order material out of open tools [KTS-EXPERTAI-2026]. |
| "Fraudsters have AI; we are behind anyway." | Only 7% feel more than moderately prepared [ACFE-TECHBENCH-2026], which is demand for `#11` and `#12`. Proactive monitoring is associated with lower median losses, though the ACFE data are not AI-specific [ACFE-RTTN-2026]. |
| "AI will replace forensic accountants." | A BRG author says AI cannot take an oath or withstand cross-examination [CPAPA-FORENSICAI-2025]; J.S. Held describes augmentation [JSHELD-AIFRAUD-2026]; AI labs are paying forensic accountants to train models [AFTERQUERY-JOB-2026]. |
| "Nobody has shown ROI in forensic work." | Correct: no accounting-firm forensic practice has published measured results. The best public evidence is self-reported J.S. Held narratives. Start by measuring data-preparation hours and exception rates. |

## 10. Sources

Full details for these keys are in the YAML: ACFE-RTTN-2026, ACFE-TECHBENCH-2026, ACFE-APAC-2026, ACFE-CANADA-2026,
ACFE-CANPR-2026, AFP-PAYFRAUD-2026, AICPA-COPILOT-2025, AICPA-FVS-2026, BVR-AICPAAIGUIDE-2025, BVR-KOHLS-2026,
CGP-ARXIV-2026, CPAPA-FORENSICAI-2025, DEANDORTON-AIEXPERT-2025, DILIGENT-AUDITAI-2026, EVERLAW-GENAI-2024,
FINCEN-DEEPFAKE-2024, FINTAF-FORENSIC-2025, HAYSTACKID-GENAI-2026, IAF-AIFRAUD-2026, JRFM-FORENSICAI-2026,
JSHELD-AIEXPERT-2026, JSHELD-AIFRAUD-2026, KTS-EXPERTAI-2026, NBC-DEEPFAKE-2025, OMRANI-BEYONDBAR-2024,
PPC-KOHLS-2025, RELATIVITY-AIR-2026, SEC-AIWASH-2024, SEC-RULE2-01-2026, STEPTOE-FRE707-2026, USCOURTS-EVAGENDA-2026,
USCOURTS-FRE707-2025, USCOURTS-STDCOMM-2026, VALID8-HUB-2026, VALID8-SITE-2026, VALID8-WP-2025.

Cited here only:
- AFTERQUERY-JOB-2026: AfterQuery, "Forensic Accounting Expert (AI training role)", job posting via AlignList, 2026-08-14. https://alignlist.com/jobs/afterquery-forensic-accountanting-expert-1772045096095
- CPATRENDLINES-TRACKER-2026: CPA Trendlines, "CPA PE Deal Tracker" (data to 2026-05-31), 2026-06-09. https://cpatrendlines.com/2026/06/09/cpa-pe-deal-tracker-10-years-466-deals/
- DOJ-ECCP-2024: US DOJ Criminal Division, "Evaluation of Corporate Compliance Programs", 2024-09. https://www.justice.gov/criminal/criminal-fraud/page/file/937501/dl
- FORVIS-QOE-2026: Forvis Mazars US, "Quality of Earnings & Due Diligence in an AI World", 2026-09-08. https://www.forvismazars.us/forsights/2026/09/quality-of-earnings-due-diligence-in-an-ai-world
- HSFKRAMER-CJC-2026: Herbert Smith Freehills Kramer note on the Civil Justice Council AI consultation, 2026-07 (search-only). https://www.hsfkramer.com/notes/litigation/2026-07/civil-justice-council-publishes-update-on-consultation-responses-regarding-use-of-ai-for-preparing-court-documents
- JOFA-ETHICSAI-2026: Journal of Accountancy, "Accounting ethics in the age of AI", 2026-08-05. https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/
- OSINT-ARXIV-2026: Palmieri et al., "Agentic and Generative AI for OSINT and Cyber Investigations", arXiv:2607.03233, 2026-07-03. https://arxiv.org/abs/2607.03233

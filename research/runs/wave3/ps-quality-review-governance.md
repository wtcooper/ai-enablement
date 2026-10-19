# Professional services / quality-review / governance deep dive

Prepared 2026-10-19. Archetype: professional-services. Module: quality-review (review of deliverables and professional quality: review and sign-off, hallucination and citation checking, quality and risk management systems, professional standards for AI-assisted work). Angle: governance (what constrains and measures the work).

Method: `curl`, `pdftotext` and the r.jina.ai text mirror into a private working folder. 32 sources opened (listed in section 5). Web search was used for about 12 queries and then hit its shared limit, so the last planned searches (verification-practice surveys) were not run. Quotations are under 25 words. Public sources only.

---

## 1. Summary

**What the governance record says.** For AI-assisted professional work, the written standards are now consistent and the independent measurement is thin.

- **The standard is "you are responsible, and you verify".** ABA Formal Opinion 512 (29 Jul 2024), the State Bar of California's rewritten guidance (approved 14 May 2026), the Law Society of England and Wales, and the ICMCI code for management consultants (adopted May 2026) all say the professional stays fully responsible for AI-assisted output and must review and verify it. The degree of review is risk-based: ABA 512 allows relying on a tool after sampling its accuracy on a subset; California says supervision must grow with the tool's autonomy and that no agentic system may file with a court or communicate advice without lawyer review.
- **Courts are the enforcer, and they now look at the firm.** The Divisional Court in *Ayinde* (6 Jun 2025) said it expects, in future hearings, to ask whether leaders such as managing partners have taken "practical and effective measures". A County Court judge (23 Apr 2026) referred two solicitors to the SRA for unchecked AI citations. The Charlotin database listed 2,202 decisions on hallucinated content on 19 Oct 2026, 1,501 of them from US courts.
- **Written policies did not prevent failures.** Butler Snow had an AI policy (adopted June 2023) requiring written approval and independent verification; three of its lawyers were sanctioned in July 2025. Sullivan & Cromwell told a bankruptcy court in April 2026 that its protocols "were not followed" and its ordinary citation-checking also missed the errors. In consulting, Deloitte Australia partly refunded a AUD 440,000 contract after a report with fabricated references and a misquoted judge (Oct 2025).
- **Independent error-rate evidence exists for legal research and drafting, not for review.** Stanford's preregistered study found 17% to 33% hallucination for three commercial legal research tools (2024 versions). Vals found AI tools beat a lawyer baseline on some tasks (document Q&A, summarisation) and trailed it on others (redlining, EDGAR research). A pre-registered NBER trial (133 patent lawyers) found AI raised blinded-graded quality, but the durable skill gain went to senior lawyers. No source found measures override rates, reviewer catch rates or review time for AI-assisted work.
- **Firms do not yet measure AI's effect on quality.** The FRC's June 2025 thematic review of the six largest UK audit firms found no formal monitoring of the audit-quality impact of automated tools (audit-specific; generative AI was limited at that time).
- **The next constraints are commercial.** Clients send contradictory instructions (demands to use AI, plus bans without permission), insurers are starting to ask how AI-enabled work is supervised, and AI-use disclosure is entering professional codes.

**Most reusable finds:** ABA 512 pp.4 and 10-11; Cal Bar 2026 guidance pp.2-9; *Ayinde* paras 6-9 and 74; EDRM analysis of *Johnson v. Dunn*; S&C letter reported by Canadian Lawyer; ICMCI code sections 2.2, 3.3 and 5.1; FRC thematic review p.20; ILTA 2026 Q3.18 policy table; Vals VLAIR reports; NBER 35720 abstract.

---

## 2. Use cases

```yaml
- id: professional-services-quality-review-01
  title: Pre-filing verification gate for AI-assisted court documents (citations, quotations, propositions)
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    Generative AI can produce citations to cases that do not exist, quotations that are not in the cited
    source, and real cases cited for propositions they do not support. Courts treat unchecked filings as a
    breach of professional duty.
  solution: >
    Before a court document goes out, a person checks every citation, quotation and proposition against an
    authoritative source, and the signing lawyer is accountable for the check. The lawyer also checks local rules
    for AI disclosure. Firms describe this as an office-manual rule or a written policy (Butler Snow, Sullivan
    & Cromwell). Professional bodies and courts state it as a duty (ABA 512, Cal Bar, Ayinde, Law Society).
  outcomes:
    - lever: risk
      description: Scale of the failure the gate targets. A public database counts decisions where a court found or implied that a party relied on hallucinated content.
      figure: "2,202 decisions identified (as of 2026-10-19); 1,501 USA; 872 involve a lawyer as the party; 1,267 a pro se litigant"
      measures: >
        Database definition: documents where a court or tribunal addressed AI use in more than a passing reference
        and found or implied reliance on hallucinated content (a few decisions where AI use was alleged but not
        confirmed are included at the compiler's judgment). The country and party counts are the database's filter
        counts as displayed. It is a count of decisions, not an error rate.
      provenance: independent
      source_ref: CHARLOTIN-HALLUC-2026
    - lever: risk
      description: One court schedule of 45 citations put before the court in the Haringey matter.
      figure: "18 of 45 cited cases did not exist"
      measures: "Citations listed in the schedule referred to by Dias J, per para 74 of the Divisional Court judgment; many of the cases that existed did not contain the attributed quotations or support the propositions."
      provenance: independent
      source_ref: EWHC-AYINDE-2025
    - lever: quality
      description: After sanctions, Butler Snow had outside counsel re-check its filings.
      figure: "2,400+ citations, 330 filings, 40 federal dockets reviewed; no additional hallucinated or mischaracterised citations found"
      measures: "Legal citations in the firm's filings reviewed by outside counsel after the Johnson v. Dunn show-cause orders, as described in the EDRM commentary on the court's order (primary order not opened)."
      provenance: self-reported
      source_ref: EDRM-JOHNSONDUNN-2025
  prerequisites:
    - Access to authoritative sources (official legislation and judgment databases, official law reports, reputable publisher databases) for the reviewer (EWHC-AYINDE-2025, para 7).
    - Knowledge of the court's AI-disclosure or certification rules (ABA-OP512-2024 p.10; CALBAR-GENAI-2026 p.9).
    - Mandatory training and a firm policy that names who verifies (ABA-OP512-2024 p.10).
  risks_and_guardrails:
    - The policy existing is not enough. Butler Snow's June 2023 policy required written approval and independent verification, yet three lawyers were sanctioned (EDRM-JOHNSONDUNN-2025).
    - Sullivan & Cromwell said its protocols were not followed and its ordinary citation-checking also failed to catch the errors (CANLAWMAG-SC-2026).
    - A court said admonishment alone is unlikely to be enough when false citations are put before a court, save in exceptional circumstances (EWHC-AYINDE-2025, para 31 as quoted in CCDUDLEY-RODNEY-2026, para 50).
    - Agentic tools must not file or communicate with a court without lawyer review and approval (CALBAR-GENAI-2026 p.9).
  human_checkpoints:
    - Signing lawyer personally verifies, or confirms verification of, every authority before filing.
    - Supervising lawyer review is real, not superficial. The Johnson v. Dunn court called a practice-group leader's review of one motion superficial and did not review the other (EDRM-JOHNSONDUNN-2025).
  role_evolution: >
    The Divisional Court said heads of chambers and managing partners carry leadership responsibilities for AI
    competence and that courts can be expected to ask whether those were fulfilled (EWHC-AYINDE-2025, para 9).
    In Johnson v. Dunn the court sanctioned individual lawyers rather than the firm, crediting the firm's
    policies and remedial steps (EDRM-JOHNSONDUNN-2025).
  evidence_grade: B
  sources:
    - { ref: ABA-OP512-2024, title: "Formal Opinion 512: Generative Artificial Intelligence Tools", publisher: ABA Standing Committee on Ethics and Professional Responsibility, type: professional-body, url: "https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf", date: 2024-07-29, access: full, locator: "Part II.A pp.3-5; Part II.D pp.9-10" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "Candor to the Tribunal row, p.9" }
    - { ref: EWHC-AYINDE-2025, title: "R (Ayinde) v London Borough of Haringey; Al-Haroun v Qatar National Bank [2025] EWHC 1383 (Admin)", publisher: High Court (King's Bench Divisional Court), type: regulator, url: "https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf", date: 2025-06-06, access: full, locator: "paras 6-9, 74" }
    - { ref: CCDUDLEY-RODNEY-2026, title: "Rodney v Gee'z Micro Bar & Pitstop, judgment on AI use by solicitors", publisher: County Court at Dudley (HHJ Grimshaw), type: regulator, url: "https://www.judiciary.uk/wp-content/uploads/2026/05/Transcript-of-judgment-re-contempt-M00DD215.pdf", date: 2026-04-23, access: full, locator: "paras 49-56" }
    - { ref: EDRM-JOHNSONDUNN-2025, title: "When AI Policies Fail: The AI Sanctions in Johnson v. Dunn", publisher: EDRM (Hon. Ralph Artigliere, ret.), type: community, url: "https://edrm.net/2025/07/when-ai-policies-fail-the-ai-sanctions-in-johnson-v-dunn-and-what-they-mean-for-the-profession/", date: 2025-07-31, access: full, locator: "body, paragraphs on policy, remediation and sanctions" }
    - { ref: CANLAWMAG-SC-2026, title: "Sullivan & Cromwell apologizes to US bankruptcy judge for AI-generated errors in Prince Group case", publisher: Canadian Lawyer, type: press, url: "https://www.canadianlawyermag.com/news/international/sullivan-cromwell-apologizes-to-us-bankruptcy-judge-for-aigenerated-errors-in-prince-group-case/394014", date: 2026-04-22, access: full, locator: "paragraphs 3-8" }
    - { ref: CHARLOTIN-HALLUC-2026, title: "AI Hallucination Cases Database", publisher: Damien Charlotin, type: community, url: "https://www.damiencharlotin.com/hallucinations/", date: 2026-10-19, access: full, locator: "header definition and filter counts" }
  last_reviewed: 2026-10-19
  notes: >
    Grade B because the controls are real and named (Butler Snow, Sullivan & Cromwell) but no organisation
    publishes a catch rate for the gate itself. The Butler Snow figure is from commentary on the order. The
    Sullivan & Cromwell account (letter of 18 Apr 2026) is secondary; the letter was not opened. Court
    judgments are typed regulator as the closest controlled value.

- id: professional-services-quality-review-02
  title: Automated citation and quotation checker as a second-line control before human sign-off
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance]
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: >
    Manual checking of every authority is slow and, per the sanctions record, is skipped under pressure. The
    legal research tools that advertise grounded citations also still produce errors, so a checker cannot rest
    on the drafting tool's own claims.
  solution: >
    A separate tool reads a draft, looks up each cited authority and quotation, and flags those it cannot find
    or match. A person reviews the flags. The Charlotin database page says its compiler built an automated
    reference checker that also detects hallucinations, with a demo on request. The Law Society guidance
    mentions that tools such as recitation checkers have been developed to counter false outputs.
  outcomes:
    - lever: quality
      description: none published
      figure: none
      measures: No detection or false-positive rate for any checker was found in the sources read.
      provenance: self-reported
      source_ref: CHARLOTIN-HALLUC-2026
  prerequisites:
    - Access to the primary-source databases the checker searches.
    - A review step for flagged items, because a missing match may be a database gap and not a fabrication.
  risks_and_guardrails:
    - Vendor claims of hallucination-free citations were found overstated in a preregistered study of three commercial legal research tools (STANFORD-MAGESH-2024). Apply the same scepticism to a checker's claims.
    - The Law Society says generative AI cannot autonomously validate or audit the accuracy of its results (LAWSOC-GENAI-2026).
  human_checkpoints:
    - A person reviews every flagged citation and the signing lawyer remains responsible (CALBAR-GENAI-2026 p.9).
  role_evolution: >
    The reviewer's task shifts from looking up every authority to resolving the checker's exceptions. No
    source states this as a change that has happened.
  evidence_grade: C
  sources:
    - { ref: CHARLOTIN-HALLUC-2026, title: "AI Hallucination Cases Database", publisher: Damien Charlotin, type: community, url: "https://www.damiencharlotin.com/hallucinations/", date: 2026-10-19, access: full, locator: "header paragraph on PelAIkan" }
    - { ref: LAWSOC-GENAI-2026, title: "Generative AI - the essentials", publisher: Law Society of England and Wales, type: professional-body, url: "https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials", date: 2026, access: full, locator: "section on how generative AI works (recitation checkers)" }
    - { ref: STANFORD-MAGESH-2024, title: "Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools", publisher: Stanford RegLab/HAI (arXiv 2405.20362), type: academic, url: "https://arxiv.org/abs/2405.20362", date: 2024-05-30, access: full, locator: abstract }
  last_reviewed: 2026-10-19
  notes: >
    Vendor citation-checking products (for example Clearbrief, Westlaw features) were seen but their pages carry
    no publication date, so they are not cited. See Gaps. The checker is described by its author on a database page;
    no independent test was found.

- id: professional-services-quality-review-03
  title: Accuracy testing of AI tools against a professional baseline before reliance, and again after model changes
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >
    Vendors describe their tools as accurate or hallucination-free, but firms have little independent evidence of
    task-level accuracy and models change over time.
  solution: >
    Compare tool output with a professional baseline on defined tasks, scored against set criteria, before
    deciding how much review a task needs, and repeat after updates. ABA 512 gives a lawyer a model: test the
    tool on a smaller subset by manual review and comparison, then rely more on its results for the larger set.
    Vals ran the benchmark route in two studies. The note "other" is used for the pattern: benchmark or parallel-run
    evaluation.
  outcomes:
    - lever: quality
      description: Vals compared four legal AI tools with a lawyer baseline on seven tasks (Feb 2025). Results varied by task.
      figure: "Document Q&A: Harvey Assistant 94.8%, CoCounsel 89.6%, lawyer baseline 70.1%. Redlining: lawyer baseline 79.7%, best AI score 65.0%. EDGAR research: lawyer baseline 70.1%, the one AI tool entered 55.2%."
      measures: "Score on predefined evaluation criteria for each task; vendors chose which tasks to opt into; Lexis+ AI withdrew from the sections studied. Vals states it has a customer relationship with one or more participants."
      provenance: independent
      source_ref: VALS-VLAIR-2025
    - lever: quality
      description: Vals legal research study (Oct 2025) on 200 US legal research questions.
      figure: "Weighted score 74% to 78% for four AI products versus 69% for the lawyer baseline; accuracy 78-81% for legal AI products and 80% for the generalist product"
      measures: "Weighted score across accuracy (50%), authoritativeness (40%) and appropriateness (10%) on 200 questions. Multi-jurisdiction questions scored on average 14 points lower than single-jurisdiction ones."
      provenance: independent
      source_ref: VALS-LEGALRESEARCH-2025
    - lever: risk
      description: Stanford preregistered evaluation of commercial legal research tools (2024 versions).
      figure: "17% to 33% hallucination"
      measures: "Share of queries on which each of Lexis+ AI, Westlaw AI-Assisted Research and Ask Practical Law AI hallucinated, per the abstract; hallucination means incorrect information or a false assertion that a source supports a proposition (definition as quoted in LLRX-FARRIS-2026)."
      provenance: independent
      source_ref: STANFORD-MAGESH-2024
  prerequisites:
    - A task set drawn from the firm's own work and a way to produce the baseline (a lawyer or consultant answering the same questions).
    - A scoring rubric and reviewers, as Vals used law firms and a lawyer and law-librarian review team.
  risks_and_guardrails:
    - Results date quickly. Vals calls its study a snapshot that must be repeated. LLRX notes the Stanford study tested versions that have since been replaced, so it should be read with caution in 2026 (VALS-VLAIR-2025; LLRX-FARRIS-2026).
    - Tool skills were evaluated in isolation; value in a workflow needs separate assessment (VALS-VLAIR-2025).
    - California says competence includes periodic reassessment of a system as it is updated or used for new tasks (CALBAR-GENAI-2026 p.5).
  human_checkpoints:
    - Lawyers score or review the output against the baseline; a human decides the review depth by task.
  role_evolution: >
    ABA 512 treats the verification decision as the lawyer's, and says it depends on the tool and the specific task
    (ABA-OP512-2024 p.4). No source describes a dedicated evaluation role.
  evidence_grade: A
  sources:
    - { ref: VALS-VLAIR-2025, title: "Vals Legal AI Report (VLAIR)", publisher: Vals AI, type: academic, url: "https://www.vals.ai/vlair", date: 2025-02-27, access: full, locator: "Executive summary results table; acknowledgments (Consortium Firms)" }
    - { ref: VALS-LEGALRESEARCH-2025, title: "VLAIR - Legal Research", publisher: Vals AI, type: academic, url: "https://www.vals.ai/industry-reports/vlair-10-14-25", date: 2025-10-14, access: full, locator: "Executive summary; Key findings 1-3" }
    - { ref: STANFORD-MAGESH-2024, title: "Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools", publisher: Stanford RegLab/HAI (arXiv 2405.20362), type: academic, url: "https://arxiv.org/abs/2405.20362", date: 2024-05-30, access: full, locator: abstract }
    - { ref: LLRX-FARRIS-2026, title: "\"Hallucinations\" by West & Lexis AI?", publisher: LLRX, type: press, url: "https://www.llrx.com/2026/04/hallucinations-by-west-lexis-ai/", date: 2026-04, access: full, locator: "paragraphs on study findings and currency" }
    - { ref: ABA-OP512-2024, title: "Formal Opinion 512: Generative Artificial Intelligence Tools", publisher: ABA Standing Committee on Ethics and Professional Responsibility, type: professional-body, url: "https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf", date: 2024-07-29, access: full, locator: "Part II.A p.4" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "Competence row, p.5" }
  last_reviewed: 2026-10-19
  notes: >
    Grade A rests on the Vals and Stanford measurements (named organisations, reported as measured). They
    measure the tools, not a firm's own acceptance-testing practice, and the tasks are legal (document analysis,
    research), which is adjacent to review itself. A strict reader may cap this at B. The Stanford
    journal version (Journal of Empirical Legal Studies, 2025) is reported by LLRX and was not opened. In ABA 512
    fn 14 the 17% to 33% figure is quoted. Vendors opted into tasks, so the results are not a like-for-like comparison.

- id: professional-services-quality-review-04
  title: Firm AI-use policy with mandatory human review, independent verification, vetted tools and training before access
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    Individual lawyers and staff use AI inconsistently, and managers must show reasonable measures to make sure
    the whole firm meets professional duties.
  solution: >
    The firm issues a written policy: approved tools only, no confidential data in unsuitable tools, human review of
    AI-assisted work product, independent verification with citations, and training before access. ABA 512 and
    Cal Bar both place the duty to set such policies and train staff on managerial and supervisory lawyers.
    The pattern is "other": policy and training controls.
  outcomes:
    - lever: risk
      description: ILTA 2026 survey of law firm technology (508 firms) reports policy content by firm size (Q3.18). Examples below.
      figure: "Human review of work product required: 31% of firms under 50 lawyers, 83% of firms with 350-699 lawyers, 79% of firms over 700. Outputs must be cited or independently verified: 25% under 50 lawyers, 60% at 350-699, 55% over 700. Training required before use: 11% under 50, 72% over 700. No formal written policy and no guidance yet: 10% under 50 lawyers, 0% at 350 or more."
      measures: "Percent of responding firms in each lawyer-count band that selected each option in Q3.18, 'which of the following best describe your firm's current official policies or guidance on the use of generative AI tools' (more than one option allowed)."
      provenance: independent
      source_ref: ILTA-TECHSURVEY-2026
    - lever: risk
      description: Thomson Reuters Future of Professionals survey (1,816 professionals, Mar-Apr 2026) on unsanctioned use.
      figure: "34% use AI tools their organisation has not sanctioned; 41% lack access to AI tools designed for professional work, built on verified content"
      measures: "Share of surveyed professionals (law, tax, audit, accounting, compliance, risk, trade; 62 countries) in the report's key findings, as worded in the report."
      provenance: vendor-published
      source_ref: TR-FOP-2026
  prerequisites:
    - A named owner for AI governance and a way to give staff approved tools (otherwise shadow use fills the gap, TR-FOP-2026).
    - Training content covering tool limits, ethics and data handling (ABA-OP512-2024 p.10).
  risks_and_guardrails:
    - Policy gaps scale with firm size: ILTA's summary notes large differences in whether a policy exists at all and in training requirements (ILTA-TECHSURVEY-2026 p.5).
    - A policy alone failed at Butler Snow and Sullivan & Cromwell (EDRM-JOHNSONDUNN-2025; CANLAWMAG-SC-2026).
    - Updates are needed as tools become more autonomous: California says managers should update policies, controls and training (CALBAR-GENAI-2026 p.7).
  human_checkpoints:
    - Supervising lawyers make reasonable efforts to ensure compliance; the firm reviews policy as tools change.
  role_evolution: >
    ILTA reports firms expect added headcount in IT, innovation, security, training, knowledge management and
    data science (ILTA-TECHSURVEY-2026 p.5). Courts expect managers to show the policy was put into effect
    (EWHC-AYINDE-2025, para 9).
  evidence_grade: B
  sources:
    - { ref: ILTA-TECHSURVEY-2026, title: "ILTA Technology Survey 2026 Executive Summary", publisher: International Legal Technology Association, type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026-08, access: full, locator: "p.5, Q3.18 table" }
    - { ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: 2026-09-30, access: full, locator: "Key findings 01 and 03" }
    - { ref: ABA-OP512-2024, title: "Formal Opinion 512: Generative Artificial Intelligence Tools", publisher: ABA Standing Committee on Ethics and Professional Responsibility, type: professional-body, url: "https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf", date: 2024-07-29, access: full, locator: "Part II.E pp.10-11 and fn 52" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "Duty to Supervise row, p.7" }
    - { ref: EWHC-AYINDE-2025, title: "R (Ayinde) v London Borough of Haringey; Al-Haroun v Qatar National Bank [2025] EWHC 1383 (Admin)", publisher: High Court (King's Bench Divisional Court), type: regulator, url: "https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf", date: 2025-06-06, access: full, locator: "para 9" }
  last_reviewed: 2026-10-19
  notes: >
    Grade B: the ILTA data are a measured survey of policy prevalence across 508 firms, but they do not measure
    whether policies reduce errors. The TR figures are from a vendor-sponsored survey. The ILTA PDF date is from
    its metadata (created 14 Aug 2026); the landscape file dated it Jun 2026 from the file name. Law firms only.

- id: professional-services-quality-review-05
  title: Telling clients when AI materially contributed, and meeting client consent and disclosure terms
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [client-interaction, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    Clients are asking whether and how AI was used, and some outside counsel guidelines require disclosure or
    permission. Professional rules require disclosure in some cases and leave it open in others.
  solution: >
    The firm adds an AI-use statement to deliverables and engagement communications when AI materially affected the
    analysis, and checks client terms before using AI on a matter. ABA 512 requires disclosure if the client asks or
    the engagement terms or guidelines require it. ICMCI requires informing clients when AI materially contributes.
    Deloitte Australia's revised report added a disclosure that Azure OpenAI had been used.
  outcomes:
    - lever: risk
      description: ILTA reports how many firms require client approval before using generative AI, by firm size.
      figure: "8% of firms under 50 lawyers, 38% of firms with 350-699 lawyers, 34% of firms over 700"
      measures: "Percent of responding firms in each lawyer-count band selecting 'Must obtain client approval' in Q3.18 (more than one option allowed)."
      provenance: independent
      source_ref: ILTA-TECHSURVEY-2026
  prerequisites:
    - A way to record client AI instructions per matter.
    - A test for materiality of AI contribution; ICMCI says routine productivity tools need not be disclosed individually, but material analytical or generative uses must be.
  risks_and_guardrails:
    - Client instructions conflict. A DLA Piper panelist described clients that expect AI savings alongside directives that firms may not use AI without explicit permission and demands for warranties that models are unbiased (TRI-LEGALWEEK-2026).
    - California says a lawyer must follow client instructions or guidelines that limit AI use (CALBAR-GENAI-2026 p.7).
    - Disclosure does not remove responsibility for the content (ICMCI-AICODE-2026 section 2.2).
  human_checkpoints:
    - The lawyer or consultant decides whether AI use is material and what the client is told.
  role_evolution: >
    A Ropes & Gray speaker said clients are starting to ask for line-item invoice transparency about AI use
    (TRI-LEGALWEEK-2026). No source describes a new disclosure role.
  evidence_grade: B
  sources:
    - { ref: ABA-OP512-2024, title: "Formal Opinion 512: Generative Artificial Intelligence Tools", publisher: ABA Standing Committee on Ethics and Professional Responsibility, type: professional-body, url: "https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf", date: 2024-07-29, access: full, locator: "Part II.C p.8" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "Communication Regarding Generative AI Use row, p.7" }
    - { ref: ICMCI-AICODE-2026, title: "Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, v1.0", publisher: International Council of Management Consulting Institutes, type: professional-body, url: "https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf", date: 2026-05, access: full, locator: "sections 2.2 and 3.3" }
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03, access: full, locator: "sections 'The contradictions in the room'" }
    - { ref: CTV-DELOITTE-2025, title: "Deloitte to partially refund Australian government for report with apparent AI-generated errors", publisher: The Associated Press via CTV News, type: press, url: "https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/", date: 2025-10-07, access: full, locator: "paragraph on revised version disclosure" }
    - { ref: ILTA-TECHSURVEY-2026, title: "ILTA Technology Survey 2026 Executive Summary", publisher: International Legal Technology Association, type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026-08, access: full, locator: "p.5, Q3.18 table" }
  last_reviewed: 2026-10-19
  notes: >
    Deloitte added its disclosure only after errors were reported; the source does not say it is a standing practice.
    The TRI Legalweek article was dated from the event week (the page header shows a fetch-time date). Billing
    aspects of AI use are routed to billing-collections.

- id: professional-services-quality-review-06
  title: Pre-issue reference, quotation and number audit for AI-assisted consulting and advisory reports
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    Consulting reports for public bodies have gone out with fabricated references and a misquoted judge, and the
    errors were found by an outside academic and a newspaper, not by the firm's review.
  solution: >
    Idea: before a report is issued, every footnote, quotation, calculation and reference in AI-assisted sections is
    traced to its source by a person who did not write the passage. The ICMCI code already says consultants
    must independently verify factual content, calculations, citations and references. No firm publishes a
    deliverable audit step for AI-assisted reports.
  outcomes:
    - lever: risk
      description: none published
      figure: none
      measures: No source reports a measured effect of a pre-issue audit step in consulting.
      provenance: self-reported
      source_ref: ICMCI-AICODE-2026
  prerequisites:
    - A reviewer independent of the drafter and access to the cited sources.
    - Disclosure rules for when AI was used in drafting (ICMCI-AICODE-2026 section 3.3).
  risks_and_guardrails:
    - In the Deloitte Australia case, a Sydney University researcher found up to 20 errors in the first version and the report was revised with an AI disclosure (CTV-DELOITTE-2025).
    - Deloitte Canada said AI "was not used to write the report" but selectively used to support research citations, and is revising a 523-page report after false citations were found (CTV-DELOITTENL-2025).
    - ICMCI treats submitting unreviewed or materially unverified AI output as finished work as AI misuse and a breach of its Code of Conduct (ICMCI-AICODE-2026 section 2.3).
  human_checkpoints:
    - Independent reviewer signs off references before issue; engagement leader remains accountable (ICMCI-AICODE-2026 section 2.2).
  role_evolution: >
    ICMCI says the consultant who presents or relies on an AI-assisted output carries the same responsibility as for
    entirely human work (ICMCI-AICODE-2026 section 2.2).
  evidence_grade: D
  sources:
    - { ref: ICMCI-AICODE-2026, title: "Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, v1.0", publisher: International Council of Management Consulting Institutes, type: professional-body, url: "https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf", date: 2026-05, access: full, locator: "sections 2.2, 2.3, 5.1" }
    - { ref: CTV-DELOITTE-2025, title: "Deloitte to partially refund Australian government for report with apparent AI-generated errors", publisher: The Associated Press via CTV News, type: press, url: "https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/", date: 2025-10-07, access: full, locator: "paragraphs 1-6, 15-16" }
    - { ref: CTV-DELOITTENL-2025, title: "N.L. government pledges 'strict review' on AI use after more false citations found in reports", publisher: CTV News, type: press, url: "https://www.ctvnews.ca/canada/newfoundland-and-labrador/article/nl-government-pledges-strict-review-on-ai-use-after-more-false-citations-found-in-reports/", date: 2025-11-29, access: full, locator: "paragraphs 2-4" }
  last_reviewed: 2026-10-19
  notes: >
    IDEA. Labelled D because no firm describes the control. The need is evidenced by two reported incidents. Deloitte
    Canada's CPA NL investigation was seen only in a search snippet and is not used. Deloitte Australia did not
    confirm to AP whether the errors were AI-generated; the revised report disclosed use of Azure OpenAI. Assurance
    and public-sector aspects belong to the assurance archetype.

- id: professional-services-quality-review-07
  title: Autonomy-scaled review gates for agentic AI (no external transmission, filing or advice without approval)
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >
    Agentic systems can plan, select tools and finish tasks without a person prompting each step, which raises the
    risk that a lawyer relies on automated work without contemporaneous review.
  solution: >
    Idea: set review gates by autonomy level. California's 2026 guidance says oversight must rise with autonomy and
    says lawyers must not let agents make substantive legal determinations, give advice, file pleadings or
    transmit client information outside without meaningful review. A workflow would hold agent output at a gate
    for lawyer approval before any outward step.
  outcomes:
    - lever: risk
      description: none published
      figure: none
      measures: No source reports gate performance or error rates for agentic legal workflows.
      provenance: self-reported
      source_ref: CALBAR-GENAI-2026
  prerequisites:
    - Knowing what the agent can access and do (data sources, when it acts without prompting). California makes this part of competence (CALBAR-GENAI-2026 pp.2-3).
    - Access controls limiting which matters and systems the agent can reach (CALBAR-GENAI-2026 p.6).
  risks_and_guardrails:
    - Agents with access to email, document management or client files can expose confidential or privileged information across matters if poorly configured (CALBAR-GENAI-2026 p.6).
    - Hallucination risk can be compounded when using agentic AI (CALBAR-GENAI-2026 p.5).
    - Lawyers must not let AI file documents, communicate with a court, or make representations on their behalf (CALBAR-GENAI-2026 p.9).
  human_checkpoints:
    - Lawyer review and approval before any document reaches a court, client or third party.
    - Periodic reassessment of the system's autonomy and risks as it is updated.
  role_evolution: >
    California says a subordinate lawyer must exercise independent judgment about use of agentic tools at a
    supervisor's direction (CALBAR-GENAI-2026 p.7). The role change otherwise is not described.
  evidence_grade: D
  sources:
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "Executive Summary pp.2-3; Confidentiality row pp.5-6; Candor row p.9" }
    - { ref: CALBAR-ETHICS-2026, title: "Ethics and Technology Resources (State Bar of California)", publisher: State Bar of California, type: regulator, url: "https://www.calbar.ca.gov/Attorneys/Conduct-Discipline/Ethics/Ethics-Technology-Resources", date: 2026-05-14, access: full, locator: "paragraph on Board of Trustees approval" }
  last_reviewed: 2026-10-19
  notes: >
    IDEA. The constraint is stated by a regulator; a deployed product with review gates (for example Harvey's Legal
    Work Orchestration) is covered by the practice angle and was not opened here. The 14 May 2026 approval date is
    from the State Bar's resources page; the PDF has no date on its face.

- id: professional-services-quality-review-08
  title: Matter-level AI-use record and marking of AI-generated material
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >
    When an error surfaces, the firm needs to know which parts of a deliverable involved AI, who reviewed them
    and what the tool did. Reviewers also need to see which material is machine-generated.
  solution: >
    Idea: record AI inputs, outputs and errors per matter and mark AI-generated material in client and firm files. ABA
    512 mentions marking such material as a training suggestion. The Law Society checklist advises documenting
    inputs, outputs and any errors where not automatically stored. ICMCI says firms should document significant
    AI-supported decisions in proportion to risk.
  outcomes:
    - lever: risk
      description: none published
      figure: none
      measures: No source reports results from keeping such a record.
      provenance: self-reported
      source_ref: ABA-OP512-2024
  prerequisites:
    - Matter or engagement system that can hold the record, and staff habits to maintain it.
  risks_and_guardrails:
    - A record shows what happened; it does not replace verification (ABA-OP512-2024 p.4).
    - A broker advises firms to keep audit trails of AI-generated content and to expect underwriters to look for documented protocols (IAMAG-LAWPL-2026).
  human_checkpoints:
    - Reviewer uses the record to focus checks on marked passages.
  role_evolution: >
    No source describes a change in roles.
  evidence_grade: D
  sources:
    - { ref: ABA-OP512-2024, title: "Formal Opinion 512: Generative Artificial Intelligence Tools", publisher: ABA Standing Committee on Ethics and Professional Responsibility, type: professional-body, url: "https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf", date: 2024-07-29, access: full, locator: "fn 52, p.10" }
    - { ref: LAWSOC-GENAI-2026, title: "Generative AI - the essentials", publisher: Law Society of England and Wales, type: professional-body, url: "https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials", date: 2026, access: full, locator: "Checklist when considering generative AI use" }
    - { ref: ICMCI-AICODE-2026, title: "Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, v1.0", publisher: International Council of Management Consulting Institutes, type: professional-body, url: "https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf", date: 2026-05, access: full, locator: "section 3.6" }
    - { ref: IAMAG-LAWPL-2026, title: "How Generative AI Is Reshaping Professional Liability Risk for Law Firms", publisher: Independent Agent magazine (IIABA), type: press, url: "https://www.iamagazine.com/?p=32247", date: 2026-03-09, access: full, locator: "broker recommendations" }
  last_reviewed: 2026-10-19
  notes: IDEA. Guidance and broker advice only; no deployment found.

- id: professional-services-quality-review-09
  title: Monitoring the quality impact of AI tools inside the firm's quality management system
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: >
    Firms track how many teams use their tools but not whether the tools raise or lower the quality of the work.
  solution: >
    Idea, urged by the regulator: set policies and metrics to evaluate how automated tools affect quality
    continuously and consistently, decide where responsibility for global tools sits, and use findings to focus on
    the tools with the greatest impact. Root-cause analysis of errors could feed it. For accounting firms the AICPA's
    SQMS 1 requires a risk-based quality management system with monitoring and remediation.
  outcomes:
    - lever: quality
      description: Absence of measurement is itself the finding (audit firms, automated tools incl. limited generative AI).
      figure: "All six firms reviewed lacked formal monitoring of audit-quality impact; one firm reported usage against targets"
      measures: "Firms in scope of the FRC thematic review (BDO, Deloitte, EY, Forvis Mazars, KPMG, PwC) whose monitoring covered usage only, typically for licensing; 'generally' no KPIs, one firm reporting usage rates against targets. Scope is automated tools and techniques, with generative AI limited at the time."
      provenance: independent
      source_ref: FRC-ATT-2025
  prerequisites:
    - Error and root-cause data that can be tied to tool use; defined owners for each tool.
  risks_and_guardrails:
    - FRC found the firms' monitoring was usage-focused. It encourages firms to set policies or metrics (FRC-ATT-2025 p.20).
    - SQMS 1 moves from policies to proving the system worked, with at least annual evaluation and more documentation (TR-SQMS-2025).
  human_checkpoints:
    - Quality leader reviews tool-level quality findings and decides on recertification or retirement.
  role_evolution: >
    The FRC says allocation of monitoring responsibilities for globally deployed tools should be defined
    (FRC-ATT-2025 p.20).
  evidence_grade: D
  sources:
    - { ref: FRC-ATT-2025, title: "Thematic review: Certification of Automated Tools and Techniques", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Thematic_Review_on_the_Certification_of_Automated_Tools_and_Techniques.pdf", date: 2025-06, access: full, locator: "p.20 Monitoring the use and impact of ATTs; p.16 AI in ATTs" }
    - { ref: TR-SQMS-2025, title: "SQMS 1 explained: a practical guide to firm-level quality management", publisher: Thomson Reuters (tax and accounting blog), type: vendor, url: "https://tax.thomsonreuters.com/blog/sqms-1-explained-a-practical-guide-to-firm-level-quality-management/", date: 2025-09-02, access: full, locator: "paragraphs 2-4" }
  last_reviewed: 2026-10-19
  notes: >
    IDEA, regulator-encouraged. Audit-specific evidence; the assurance archetype owns the detail. The review
    notes firms may sometimes capture tool use in other activities such as root cause analysis. A search summary
    suggested a first SQMS 1 evaluation due 15 Dec 2026; that was not confirmed in an opened source and is not relied on.
    SQMS 1's applicability beyond audit and attest engagements was not checked.

- id: professional-services-quality-review-10
  title: Post-incident look-back audit of AI-assisted work product and remediation
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: full-population-testing
  ladder: assist
  change_scope: process
  runtime_class: personal-assistant
  maturity: in-production
  problem: >
    After one hallucinated citation or reference is found, the client, court and firm need to know whether others
    exist elsewhere in the same matter or in the firm's wider filings.
  solution: >
    The firm re-reviews the full set of affected documents (or a wider population), corrects them, tells the court or
    client, and reviews training and process. Butler Snow retained outside counsel to review its filings. Sullivan
    & Cromwell re-reviewed all filings in the Prince matter and filed a schedule of corrections. The Australian
    department had Deloitte review the report and publish a revised version.
  outcomes:
    - lever: quality
      description: Butler Snow outside look-back after the show-cause orders.
      figure: "2,400+ citations, 330 filings, 40 federal dockets; no additional hallucinated or mischaracterised citations found"
      measures: "Citations in the firm's filings reviewed by outside counsel, per EDRM commentary on the order (primary order not opened)."
      provenance: self-reported
      source_ref: EDRM-JOHNSONDUNN-2025
    - lever: quality
      description: Sullivan & Cromwell re-review of all filings in the Prince Chapter 15 matter.
      figure: "No other AI-related issues found; additional non-substantive or clerical errors listed in Schedule A"
      measures: "Outcome of the firm's re-review of filings in the matter, as stated in its 18 Apr 2026 letter to the court and reported by Canadian Lawyer (letter not opened)."
      provenance: self-reported
      source_ref: CANLAWMAG-SC-2026
  prerequisites:
    - Ability to enumerate the affected filings and pull their citations.
    - A decision on disclosure to courts and clients; the Johnson v. Dunn court required disclosure to clients and courts as part of sanctions (EDRM-JOHNSONDUNN-2025).
  risks_and_guardrails:
    - A clean look-back does not show the controls work; both firms had existing policies when the incidents happened.
    - Court credited Butler Snow's prior policies and remedial response when deciding not to sanction the firm itself (EDRM-JOHNSONDUNN-2025).
  human_checkpoints:
    - Outside or independent reviewer for the look-back; partner takes responsibility to the court. A Sullivan & Cromwell partner took personal responsibility under the court's local equivalent of Rule 11 (CANLAWMAG-SC-2026).
  role_evolution: >
    Not described beyond partner accountability.
  evidence_grade: B
  sources:
    - { ref: EDRM-JOHNSONDUNN-2025, title: "When AI Policies Fail: The AI Sanctions in Johnson v. Dunn", publisher: EDRM (Hon. Ralph Artigliere, ret.), type: community, url: "https://edrm.net/2025/07/when-ai-policies-fail-the-ai-sanctions-in-johnson-v-dunn-and-what-they-mean-for-the-profession/", date: 2025-07-31, access: full, locator: "paragraphs on remedial effort and sanctions" }
    - { ref: CANLAWMAG-SC-2026, title: "Sullivan & Cromwell apologizes to US bankruptcy judge for AI-generated errors in Prince Group case", publisher: Canadian Lawyer, type: press, url: "https://www.canadianlawyermag.com/news/international/sullivan-cromwell-apologizes-to-us-bankruptcy-judge-for-aigenerated-errors-in-prince-group-case/394014", date: 2026-04-22, access: full, locator: "paragraphs 4-8" }
    - { ref: CTV-DELOITTE-2025, title: "Deloitte to partially refund Australian government for report with apparent AI-generated errors", publisher: The Associated Press via CTV News, type: press, url: "https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/", date: 2025-10-07, access: full, locator: "paragraphs 2-5" }
  last_reviewed: 2026-10-19
  notes: >
    Grade B: figures are firm-reported and reached through secondary accounts, so not graded A. The Australian
    department said Deloitte reviewed the 237-page report and confirmed some footnotes and references were
    incorrect, and the substance and recommendations were unchanged.

- id: professional-services-quality-review-11
  title: Protected unaided practice and verification-skills training for early-career reviewers
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    Review of AI output depends on the reviewer's own expertise, but AI doing first drafts removes the work that built
    that expertise. Juniors are also the least equipped to spot errors.
  solution: >
    Idea: build deliberate unaided practice (for example redlines and checks done without AI) and verification
    training into early careers, and teach how to catch fabricated citations and misgrounded propositions. A
    Thomson Reuters Institute webinar listed for 15 Oct 2026 targets verification habits for law students and
    early-career lawyers. The NBER trial supports the concern: after three months, the advantage without AI was
    concentrated among senior lawyers.
  outcomes:
    - lever: quality
      description: none published for the training idea. The problem is measured in the NBER trial (patent drafting, adjacent).
      figure: none
      measures: No source reports results from a verification-training programme.
      provenance: self-reported
      source_ref: TRI-EVENTS-2026
  prerequisites:
    - Review tasks that can be done without AI for calibration; supervisors with time to coach.
  risks_and_guardrails:
    - 48% of surveyed professionals fear a negative impact on independent judgment development (TR-FOP-2026).
    - Foundational expertise may be a prerequisite for extracting durable skill from AI-assisted practice (NBER-AUTOR-2026).
  human_checkpoints:
    - Supervisors assess juniors' unaided review quality.
  role_evolution: >
    TR reports legal professionals expect the time to trusted judgment to extend by nearly two years, while tax
    professionals expect it to shorten by one (TR-FOP-2026). Early careers in public-sector settings are described
    as developing through quality assurance as the main learning framework (TR-FOP-2026).
  evidence_grade: D
  sources:
    - { ref: TRI-EVENTS-2026, title: "Thomson Reuters Institute events: Trust by Verify; Beyond Human in the Loop", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/events/trust-by-verify-catching-errors-in-ai-output-before-they-reach-the-court-or-client", date: 2026-10, access: full, locator: "event description (webinar listed 15 Oct 2026; abstract only)" }
    - { ref: NBER-AUTOR-2026, title: "Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER WP 35720)", publisher: NBER, type: academic, url: "https://www.nber.org/papers/w35720", date: 2026-09, access: full, locator: abstract }
    - { ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: 2026-09-30, access: full, locator: "Key finding 07" }
  last_reviewed: 2026-10-19
  notes: >
    IDEA. The 15 Oct 2026 webinar is listed on the events page; its content was not seen, so only the abstract is
    cited. A related webinar "Beyond Human in the Loop" is scheduled for 11 Nov 2026 (abstract only, cannot support
    a grade). Talent aspects are routed to talent-learning.

- id: professional-services-quality-review-12
  title: Blinded expert scoring of AI-assisted versus unaided deliverables as a quality measure
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >
    Firms claim AI raises quality but rarely have measured evidence. Self-reported time savings are not quality
    measures.
  solution: >
    Have expert reviewers, blind to whether AI was used, score matched deliverables from AI-assisted and unaided
    lawyers on set tasks. The NBER trial did this with 133 patent lawyers at 11 firms over three months, and the
    BCG experiment did it with consultants. This is a research design that a firm could copy; no firm is reported
    running it internally.
  outcomes:
    - lever: quality
      description: NBER pre-registered trial of a custom AI patent drafting assistant, blinded expert scoring (adjacent task: drafting).
      figure: "Quality up 0.34 SD at 10 days and 0.38 SD at 90 days; unaided redline 0.32 SD better for treated lawyers overall, 0.45 SD for seniors, no average gain for juniors"
      measures: "Standard-deviation differences in blinded expert scores between treated and control lawyers on benchmark drafting tasks (with AI) and on an unaided patent application redline at three months."
      provenance: vendor-published
      source_ref: NBER-AUTOR-2026
    - lever: quality
      description: HBS/BCG pre-registered experiment, 758 consultants, 18 tasks (adjacent: task performance).
      figure: "12.2% more tasks completed and 25.1% faster inside the frontier; 19% less likely to produce correct solutions on one task outside the frontier"
      measures: "Average effect of GPT-4 access versus no AI on tasks completed and time, and on the likelihood of a correct solution for one complex managerial task, per the working paper abstract."
      provenance: independent
      source_ref: HBS-DELLACQUA-2023
  prerequisites:
    - Matched tasks, blinded graders of equivalent expertise, and time to run the comparison.
  risks_and_guardrails:
    - The NBER study was conducted by Google with participants under Google's research procedures, and the authors disclose Google support; the tool was a custom Google assistant (NBER-AUTOR-2026).
    - Results come from controlled tasks, not live matters.
  human_checkpoints:
    - Expert graders score outputs without knowing the condition.
  role_evolution: >
    The NBER result suggests senior lawyers kept their skill gain and juniors' scores split (NBER-AUTOR-2026).
  evidence_grade: B
  sources:
    - { ref: NBER-AUTOR-2026, title: "Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER WP 35720)", publisher: NBER, type: academic, url: "https://www.nber.org/papers/w35720", date: 2026-09, access: full, locator: "abstract and disclosures; full PDF not reachable" }
    - { ref: HBS-DELLACQUA-2023, title: "Navigating the Jagged Technological Frontier (HBS Working Paper 24-013)", publisher: Harvard Business School, type: academic, url: "https://www.hbs.edu/faculty/Pages/item.aspx?num=64700", date: 2023-09, access: full, locator: abstract }
  last_reviewed: 2026-10-19
  notes: >
    Capped at B: both studies measure drafting or task performance, adjacent to review. NBER issue date September
    2026, revised October 2026. NBER provenance marked vendor-published because Google built the tool and ran the
    study, although the lead author is an academic; a reader may judge it differently.

- id: professional-services-quality-review-13
  title: Mapping which tasks fall inside or outside AI's reliable range to set review depth
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    AI helps on some tasks and hurts on others that look similar, so uniform review rules over-check some work and
    under-check the rest.
  solution: >
    Classify tasks by observed AI reliability (for example summarising a document versus a complex managerial
    judgment or a 50-state survey) and set review depth per class. ABA 512 already ties the amount of verification to
    the tool and the task. Vals found weaker results on multi-jurisdiction and 50-state questions.
  outcomes:
    - lever: quality
      description: In the BCG experiment, one task selected to be outside AI's frontier produced worse results with AI.
      figure: "19% less likely to produce correct solutions with AI on that task"
      measures: "Likelihood of a correct solution for one complex managerial task chosen to lie outside the frontier, GPT-4 users versus the no-AI group, per the HBS abstract."
      provenance: independent
      source_ref: HBS-DELLACQUA-2023
    - lever: quality
      description: Vals found jurisdictionally complex questions harder for all but one tool.
      figure: "Multi-jurisdiction questions scored 14 points lower on average (14 such questions)"
      measures: "Average score gap between the 14 multi-jurisdiction questions and single-jurisdiction questions across participants in the 200-question legal research study."
      provenance: independent
      source_ref: VALS-LEGALRESEARCH-2025
  prerequisites:
    - Local test data (use case 03) to place tasks on the map; a rule linking class to review depth.
  risks_and_guardrails:
    - The frontier moves as models change, so the map needs re-testing (CALBAR-GENAI-2026 p.5).
    - ABA 512 says that regardless of the review chosen, the lawyer is fully responsible (ABA-OP512-2024 p.4).
  human_checkpoints:
    - Professional decides the class for each task and may override.
  role_evolution: >
    Not described.
  evidence_grade: B
  sources:
    - { ref: HBS-DELLACQUA-2023, title: "Navigating the Jagged Technological Frontier (HBS Working Paper 24-013)", publisher: Harvard Business School, type: academic, url: "https://www.hbs.edu/faculty/Pages/item.aspx?num=64700", date: 2023-09, access: full, locator: abstract }
    - { ref: VALS-LEGALRESEARCH-2025, title: "VLAIR - Legal Research", publisher: Vals AI, type: academic, url: "https://www.vals.ai/industry-reports/vlair-10-14-25", date: 2025-10-14, access: full, locator: "Key finding 3" }
    - { ref: ABA-OP512-2024, title: "Formal Opinion 512: Generative Artificial Intelligence Tools", publisher: ABA Standing Committee on Ethics and Professional Responsibility, type: professional-body, url: "https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf", date: 2024-07-29, access: full, locator: "Part II.A p.4" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "Competence row, p.5" }
  last_reviewed: 2026-10-19
  notes: >
    Capped at B: the measurements are of task performance, adjacent to review, and no firm is reported to use a
    formal task map. The HBS paper is from 2023, outside the 12-18 month window, used as the foundational study.

- id: professional-services-quality-review-14
  title: Documented AI governance for professional indemnity insurance proposals and renewals
  archetype: professional-services
  module: quality-review
  function: risk-compliance
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    Professional indemnity policies mostly do not mention AI, but insurers are starting to ask how AI-enabled work is
    supervised, and a claim from unverified AI output raises coverage questions.
  solution: >
    Firms prepare a record of AI use, protocols, verification standards and audit trails to answer insurer
    questions at proposal and renewal. A broker says that for now the renewal question is largely check-the-box and
    expects firms without documented protocols to fall out of preferred-risk tiers within 12 to 18 months.
  outcomes:
    - lever: cost
      description: Broker expectation, not a measured result.
      figure: "Expected within 12 to 18 months: firms without documented protocols lose preferred-risk terms"
      measures: "A Jencap senior broker's forecast, as quoted by Independent Agent magazine (Mar 2026); not a tracked metric."
      provenance: self-reported
      source_ref: IAMAG-LAWPL-2026
  prerequisites:
    - A written AI protocol and the means to show it is followed.
  risks_and_guardrails:
    - Coverage is uncertain for claims where the professional service was largely AI-produced and weakly supervised (DACB-PI-2026).
    - Insurer positions are reported second-hand; exclusion wording varies (IAMAG-LAWPL-2026).
  human_checkpoints:
    - Risk or general counsel signs off proposal-form answers on AI use.
  role_evolution: >
    DAC Beachcroft advises policyholders to check whether proposal-form disclosures remain accurate (DACB-PI-2026).
  evidence_grade: C
  sources:
    - { ref: DACB-PI-2026, title: "Professional indemnity insurance: risk of AI hallucinations", publisher: DAC Beachcroft, type: firm, url: "https://www.dacbeachcroft.com/en/what-we-think/professional-indemnity-insurance-risk-of-ai-hallucinations", date: 2026-09-28, access: full, locator: "paragraphs 8-12" }
    - { ref: IAMAG-LAWPL-2026, title: "How Generative AI Is Reshaping Professional Liability Risk for Law Firms", publisher: Independent Agent magazine (IIABA), type: press, url: "https://www.iamagazine.com/?p=32247", date: 2026-03-09, access: full, locator: "broker quotes on exclusions and underwriting" }
  last_reviewed: 2026-10-19
  notes: >
    Grade C: broker and law-firm commentary. A search summary of Insurance Insider (exclusions at Hamilton and
    Berkley) was not opened and is not relied on. Acceptance-risk covers insurance in more depth.

- id: professional-services-quality-review-15
  title: Passing AI verification duties down to contractors and outsourced providers
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    Work done by contractors, outsourced providers or other lawyers may include unchecked AI output, but the
    responsible professional answers for it.
  solution: >
    Idea: put verification and AI-disclosure terms into subcontracts and require attestations on delivery. The
    Divisional Court said the duty to check AI research rests on lawyers who use it or rely on others who did,
    like reliance on a trainee. ABA 512 adds supervisory duties for outside providers of AI services. A Canadian
    Lawyer article reports an Alberta appeal court holding that a lawyer bears ultimate responsibility for
    hallucinated citations in a factum drafted by a contractor.
  outcomes:
    - lever: risk
      description: none published
      figure: none
      measures: No source reports contract clauses or measured effects.
      provenance: self-reported
      source_ref: EWHC-AYINDE-2025
  prerequisites:
    - Contracts and onboarding for outside providers; ability to review their work.
  risks_and_guardrails:
    - The signing professional cannot shift responsibility (EWHC-AYINDE-2025, para 8).
  human_checkpoints:
    - Professional reviews delivered work as for any delegated work.
  role_evolution: >
    Not described.
  evidence_grade: D
  sources:
    - { ref: EWHC-AYINDE-2025, title: "R (Ayinde) v London Borough of Haringey; Al-Haroun v Qatar National Bank [2025] EWHC 1383 (Admin)", publisher: High Court (King's Bench Divisional Court), type: regulator, url: "https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf", date: 2025-06-06, access: full, locator: "para 8" }
    - { ref: ABA-OP512-2024, title: "Formal Opinion 512: Generative Artificial Intelligence Tools", publisher: ABA Standing Committee on Ethics and Professional Responsibility, type: professional-body, url: "https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf", date: 2024-07-29, access: full, locator: "Part II.E p.11" }
    - { ref: CANLAWMAG-SC-2026, title: "Sullivan & Cromwell apologizes to US bankruptcy judge for AI-generated errors in Prince Group case", publisher: Canadian Lawyer, type: press, url: "https://www.canadianlawyermag.com/news/international/sullivan-cromwell-apologizes-to-us-bankruptcy-judge-for-aigenerated-errors-in-prince-group-case/394014", date: 2026-04-22, access: full, locator: "paragraph on Reddy v. Saroya (secondary report)" }
  last_reviewed: 2026-10-19
  notes: IDEA. The Reddy v. Saroya holding is as reported by Canadian Lawyer; the decision was not opened.

- id: professional-services-quality-review-16
  title: Checking the other side's and the court's filings for fabricated authority
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance]
  pattern: reconcile-exceptions
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >
    In several reported matters the fabricated authorities were found by opposing counsel, the opposing party or
    the judge, not by the filing firm's own review.
  solution: >
    Litigation teams check authorities cited against them as a routine step. In the matters read here, Boies Schiller
    Flexner flagged errors in Sullivan & Cromwell's filing, Haringey Council asked for copies of cases it could
    not find, respondents' counsel in the Dudley appeal raised concerns about cited authorities, and the
    Johnson v. Dunn judge ran her own searches.
  outcomes:
    - lever: risk
      description: none quantified. Each item is a reported instance.
      figure: none
      measures: No source reports how often opposing review catches errors.
      provenance: independent
      source_ref: CCDUDLEY-RODNEY-2026
  prerequisites:
    - Time and tools to look up cited authority; a culture of raising concerns with the other side.
  risks_and_guardrails:
    - Wrongly accusing a party of fabrication has costs; the sources do not discuss this.
  human_checkpoints:
    - Lawyer decides whether to raise the issue with the other side or the court.
  role_evolution: >
    Not described.
  evidence_grade: B
  sources:
    - { ref: CCDUDLEY-RODNEY-2026, title: "Rodney v Gee'z Micro Bar & Pitstop, judgment on AI use by solicitors", publisher: County Court at Dudley (HHJ Grimshaw), type: regulator, url: "https://www.judiciary.uk/wp-content/uploads/2026/05/Transcript-of-judgment-re-contempt-M00DD215.pdf", date: 2026-04-23, access: full, locator: "paras 12-14" }
    - { ref: EWHC-AYINDE-2025, title: "R (Ayinde) v London Borough of Haringey; Al-Haroun v Qatar National Bank [2025] EWHC 1383 (Admin)", publisher: High Court (King's Bench Divisional Court), type: regulator, url: "https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf", date: 2025-06-06, access: full, locator: "paras on the requests for copies of the five cases" }
    - { ref: CANLAWMAG-SC-2026, title: "Sullivan & Cromwell apologizes to US bankruptcy judge for AI-generated errors in Prince Group case", publisher: Canadian Lawyer, type: press, url: "https://www.canadianlawyermag.com/news/international/sullivan-cromwell-apologizes-to-us-bankruptcy-judge-for-aigenerated-errors-in-prince-group-case/394014", date: 2026-04-22, access: full, locator: "paragraph on Boies Schiller Flexner" }
    - { ref: EDRM-JOHNSONDUNN-2025, title: "When AI Policies Fail: The AI Sanctions in Johnson v. Dunn", publisher: EDRM (Hon. Ralph Artigliere, ret.), type: community, url: "https://edrm.net/2025/07/when-ai-policies-fail-the-ai-sanctions-in-johnson-v-dunn-and-what-they-mean-for-the-profession/", date: 2025-07-31, access: full, locator: "paragraph on independent searches and show-cause orders" }
  last_reviewed: 2026-10-19
  notes: >
    Grade B: named matters, no measurement. This is quality assurance of received work, a less central part of the
    module. In Rodney, the paragraphs on Respondent's counsel raising concerns were read in the transcript's background section.

- id: professional-services-quality-review-17
  title: Shadow-AI discovery and approved professional-grade tools as a quality control
  archetype: professional-services
  module: quality-review
  function: risk-compliance
  work_types: [review-assurance, coordination-scheduling]
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    Staff use unsanctioned consumer AI tools that the firm cannot see, so output enters deliverables with no review
    route or audit trail.
  solution: >
    Provide sanctioned professional-grade tools and detect unsanctioned use. A cross-industry study found bans
    did not stop risky use and that clear guidance and education matter. ILTA warns Copilot features are being
    activated across the collaboration layer without discrete deployment events.
  outcomes:
    - lever: risk
      description: Thomson Reuters survey of professionals (vendor-published).
      figure: "34% use unsanctioned AI tools; 66% in organisations with a named AI strategy say AI meets or exceeds expectations versus 22% without"
      measures: "Share of 1,816 surveyed professionals using tools their organisation has not sanctioned, and share of professionals in firms with and without a named strategy reporting AI meets or exceeds expectations for value creation."
      provenance: vendor-published
      source_ref: TR-FOP-2026
    - lever: risk
      description: KPMG and University of Melbourne global employee study (cross-industry, not professional services).
      figure: "56% report having made mistakes in their work from AI use (31% sometimes to very often); 66% relied on AI output without evaluating it (42% sometimes to very often); 48-49% uploaded company information or copyrighted material to public AI tools"
      measures: "Responses of employees who use AI at work in a survey of 48,340 people in 47 countries (Nov 2024-Jan 2025), self-reported; 'at least rarely' for the 56% and 66%, per the report's Figure 44 and text; the authors note social desirability may lead to under-reporting."
      provenance: independent
      source_ref: KPMG-TRUST-2025
  prerequisites:
    - Approved tools staff actually want; policy and training; visibility into usage.
  risks_and_guardrails:
    - Unsanctioned use clustered where policies existed or generative AI was banned (67% banned, 56% policy versus 33% no policy in the KPMG study); bans may be ineffective (KPMG-TRUST-2025 p.75).
  human_checkpoints:
    - Firm security and risk owners decide approved tools and review exceptions.
  role_evolution: >
    ILTA reports firms expect added headcount in security, training, KM and data science (ILTA-TECHSURVEY-2026 p.5).
  evidence_grade: C
  sources:
    - { ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: 2026-09-30, access: full, locator: "Key findings 01, 03, 05" }
    - { ref: KPMG-TRUST-2025, title: "Trust, attitudes and use of artificial intelligence: A global study 2025", publisher: University of Melbourne and KPMG, type: survey, url: "https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf", date: 2025-04-28, access: full, locator: "pp.75-76, Figure 44" }
    - { ref: ILTA-TECHSURVEY-2026, title: "ILTA Technology Survey 2026 Executive Summary", publisher: International Legal Technology Association, type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026-08, access: full, locator: "p.4" }
  last_reviewed: 2026-10-19
  notes: >
    Grade C: the main professional-services figures are vendor-published. The KPMG study is cross-industry and
    adjacent. The KPMG report date is from PDF metadata (28 Apr 2025). Acceptance-risk covers confidentiality in depth.
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Draft review and sign-off** of AI-assisted work: reviewer checks content, signatory accepts responsibility (review-assurance, document-production).
- **Citation, quotation and reference verification** before anything reaches a court, regulator or client (review-assurance).
- **Tool selection and validation**: testing a tool's accuracy on a sample or benchmark before relying on it (review-assurance, data-reporting).
- **Policy, supervision and training**: approved-tool lists, review rules, training before access (coordination-scheduling).
- **Client communication on AI use**: disclosure, consent, answering client guidelines (client-interaction).
- **Quality-management monitoring**: metrics, root-cause analysis, recertification of tools (data-reporting).
- **Incident response**: look-back audit, correction and disclosure after an error is found (review-assurance).
- **Insurance and regulatory reporting** on AI governance (document-production).

### Common pain points

- Fabricated or misdescribed authority gets through firm-level review. S&C said its protocols were not followed and its ordinary citation-checking failed (CANLAWMAG-SC-2026).
- Policies exist but individuals skip them (EDRM-JOHNSONDUNN-2025).
- Policy and training requirements vary sharply with firm size: formal policy 57% (under 50 lawyers) to 98% (350-699 lawyers) (ILTA-TECHSURVEY-2026 p.5).
- Staff use unsanctioned tools: 34% of surveyed professionals (TR-FOP-2026); cross-industry, 56% of AI-using employees say AI caused mistakes at least rarely (KPMG-TRUST-2025).
- Firms cannot show clients quantified AI savings or quality: "still gathering the data" (TRI-LEGALWEEK-2026).
- Reviewers' own expertise may erode (NBER-AUTOR-2026; TR-FOP-2026).

### Metrics and benchmarks (all with sources)

- Decisions on hallucinated content: 2,202 identified as of 2026-10-19; USA 1,501 (CHARLOTIN-HALLUC-2026). A count of decisions, not a rate.
- Legal research tools: hallucination 17% to 33% across three commercial products (2024 versions) (STANFORD-MAGESH-2024). General models on verifiable questions about random federal cases: 58% (ChatGPT 4) to 88% (Llama 2) (STANFORD-DAHL-2024, abstract; early models).
- Vals task benchmark (Feb 2025): document Q&A top AI 94.8% vs lawyer baseline 70.1%; redlining lawyer 79.7% vs best AI 65.0%; EDGAR research lawyer 70.1% vs 55.2% (VALS-VLAIR-2025). Vals legal research (Oct 2025): AI 74-78% vs lawyer 69% on 200 questions (VALS-LEGALRESEARCH-2025).
- Quality of AI-assisted work in a blinded trial: +0.34 SD (10 days) and +0.38 SD (90 days); unaided skill advantage 0.45 SD for seniors, no average gain for juniors (NBER-AUTOR-2026).
- Consulting experiment: 12.2% more tasks, 25.1% faster inside the frontier; 19% less likely to be correct on one task outside it (HBS-DELLACQUA-2023).
- FRC: no formal monitoring of audit-quality impact; usage tracking only (FRC-ATT-2025 p.20).
- Policy prevalence by size (ILTA Q3.18): human review required 31% to 83%; independent verification 25% to 60%; client approval required 8% to 38%.
- Client expectations: 78% of corporate clients say AI-enabled quality improvements are very important or essential, 6% say most or all providers deliver; 32% will reconsider relationships in 12 months (TR-FOP-2026).
- Butler Snow look-back: 2,400+ citations in 330 filings and 40 dockets; no more issues (EDRM-JOHNSONDUNN-2025).
- Absent: override rates, reviewer catch rates, review time per AI-assisted deliverable, error rates of consulting or accounting deliverables, and any independent inspection findings on generative AI in non-audit work. None found.

### Guardrails and regulatory points

- ABA 512 (29 Jul 2024): uncritical reliance can breach competence (Rule 1.1); the amount of verification depends on tool and task; managers must set policies and train staff; the lawyer is fully responsible whatever review level is chosen (ABA-OP512-2024 pp.3-4, 10-11).
- Cal Bar (approved 14 May 2026): agentic AI covered; supervision and verification scale with autonomy; periodic reassessment as systems change; no autonomous filing or external transmission without review; hourly billing must reflect time actually spent (CALBAR-GENAI-2026 pp.2-9; CALBAR-ETHICS-2026).
- Law Society of E&W: review outputs, document inputs and errors, and verify court citations from authoritative sources; misuse leading to inaccurate information breaches the SRA Code (LAWSOC-GENAI-2026). Bar Council (30 Jan 2024): verify LLM output and keep checking procedures (BARCOUNCIL-GENAI-2024).
- *Ayinde* (6 Jun 2025): duty to check against authoritative sources; leadership responsibility; courts will ask (EWHC-AYINDE-2025 paras 7-9). *Rodney* (23 Apr 2026): admonishment alone insufficient; solicitors referred to the SRA (CCDUDLEY-RODNEY-2026).
- ICMCI code (adopted May 2026): AI misuse is a breach of the Code of Conduct; independent verification of facts, calculations, citations and references; client transparency proportionate to materiality (ICMCI-AICODE-2026).
- NIST AI 600-1 (Jul 2024) names confabulation as a generative AI risk (NIST-AI600-2024, section 2.2).
- FRC: documentation expectations and monitoring encouragement for audit tools (FRC-ATT-2025). AICPA SQMS 1 required implementation 15 Dec 2025, risk-based, with evaluation at least annually (TR-SQMS-2025); applicability beyond audit was not checked.
- Not reached: SRA pages (blocked), AICPA pages (blocked), MCA (no AI guidance found), US state bar opinions other than California.

### Frontier signals (dated and sourced)

- 2026-05-14: California Board of Trustees approves guidance that adds agentic AI (CALBAR-ETHICS-2026).
- 2026-05: ICMCI adopts the first global code of AI use for management consultants (ICMCI-AICODE-2026).
- 2026-04-23: County Court refers two solicitors to the SRA; Law Society guidance now cites the case (CCDUDLEY-RODNEY-2026; LAWSOC-GENAI-2026).
- 2026-04-18: Sullivan & Cromwell letter to court; reported 22 Apr 2026 (CANLAWMAG-SC-2026).
- 2026-04-03: *U.S. v. Farris* (6th Cir.) reportedly found errors in a brief prepared using Westlaw's CoCounsel (LLRX-FARRIS-2026; secondary).
- 2026-09: NBER trial on AI and expertise (revised Oct 2026) (NBER-AUTOR-2026).
- 2026-09-28 and 2026-03-09: insurers expected to ask more about supervision of AI-enabled work; broker forecasts documented-protocol tiers within 12-18 months (DACB-PI-2026; IAMAG-LAWPL-2026).
- 2026-10-15 (listed) and 2026-11-11 (scheduled): Thomson Reuters Institute webinars on verification and on accountability in AI-assisted work (TRI-EVENTS-2026). The 11 Nov talk is a signal only.
- 2025-06-06: Divisional Court puts firm leaders on notice (EWHC-AYINDE-2025).

### Workforce and role effects

- Managers and heads of chambers carry explicit leadership duties for AI competence (EWHC-AYINDE-2025 para 9; ABA-OP512-2024 p.10).
- Juniors: the NBER result is mixed; TR respondents fear less judgment development (48%); legal professionals expect a longer path to trusted judgment (TR-FOP-2026).
- Firms expect more IT, innovation, security, training, KM and data-science staff (ILTA-TECHSURVEY-2026 p.5).
- Individuals are sanctioned even where the firm is not (EDRM-JOHNSONDUNN-2025).

### Objections and concerns practitioners raise

- "Until accuracy and quality improve, it is an expensive toy" (ILTA survey respondent, ILTA-TECHSURVEY-2026 p.3); another respondent warned GenAI will compress work that powers the associate pyramid.
- Studies age quickly: the Stanford results cover replaced product versions (LLRX-FARRIS-2026); Vals says its study must be repeated (VALS-VLAIR-2025).
- Generic bans and warranties on clients' side look dated alongside demands for AI savings (TRI-LEGALWEEK-2026).
- Confident outputs encourage over-reliance (CALBAR-GENAI-2026 p.2).
- Verification burden versus claimed savings: raised implicitly by the billing rules (hourly billing must reflect actual time) but no source quantified verification time.

### Interview probes

1. The last time an AI-assisted draft went out with a bad citation, number or reference, who caught it, at which step, and what changed afterwards?
2. For each AI tool in use, who decides how deeply output must be checked, and have you tested the tool against your own people's work before and after model updates?
3. What does the signing partner or engagement leader actually attest to, and what record shows the review happened?
4. Which client contract terms or insurer questions on AI have arrived, and who owns the answer?
5. How do juniors learn to review if AI writes the first draft, and what do you measure to know it is working?

---

## 4. Routed to other modules

- **billing-collections / scoping-pricing:** Cal Bar rule that hourly billing reflects time actually spent, flat fees may build in AI savings, matter-specific AI costs may be charged without markup (CALBAR-GENAI-2026 p.8); ABA 512 fee guidance (Part II.F, pp.12-14); client demands for AI line items and "won't pay for AI-done work" guidelines (TRI-LEGALWEEK-2026); ACC/Everlaw (in-house, 657 in-house legal professionals, 30 countries, Oct 2025): 59% report no GenAI savings from law firms yet, 24% satisfied, 61% plan to push for change in delivery and pricing (ACCEVERLAW-2025).
- **acceptance-risk:** confidentiality duties and agent data access (CALBAR-GENAI-2026 pp.5-6); PI insurance and exclusions (DACB-PI-2026; IAMAG-LAWPL-2026); client consent to input data (ABA-OP512-2024 Part II.B).
- **talent-learning:** NBER 35720 and TR-FOP-2026 findings on judgment development; TRI verification training for early-career lawyers.
- **work-production:** Vals task benchmarks and HBS productivity figures as evidence for drafting, research and extraction.
- **assurance archetype (audit):** FRC thematic review, AICPA SQMS 1 detail, Deloitte Canada's reported CPA NL investigation (search snippet only), IAASB quality management.
- **in-house:** ACC/Everlaw survey and TR in-house respondents are tagged in-house; no in-house review workflow was found.

---

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ABA-OP512-2024 | Formal Opinion 512: Generative Artificial Intelligence Tools (read via copy; ABA site blocked) | ABA Standing Committee on Ethics and Professional Responsibility | professional-body | https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf | 2024-07-29 | full |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative AI in the Practice of Law | State Bar of California COPRAC | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05-14 | full |
| CALBAR-ETHICS-2026 | Ethics and Technology Resources | State Bar of California | regulator | https://www.calbar.ca.gov/Attorneys/Conduct-Discipline/Ethics/Ethics-Technology-Resources | 2026-05-14 | full |
| LAWSOC-GENAI-2026 | Generative AI - the essentials | Law Society of England and Wales | professional-body | https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials | 2026 (updated after Apr 2026; exact date not shown) | full |
| BARCOUNCIL-GENAI-2024 | New guidance on generative AI for the Bar | Bar Council of England and Wales | professional-body | https://www.barcouncil.org.uk/resource/new-guidance-on-generative-ai-for-the-bar.html | 2024-01-30 | full (press release, not the guidance itself) |
| ICMCI-AICODE-2026 | Code of Responsible Use of AI for the Management Consulting Profession v1.0 | ICMCI | professional-body | https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf | 2026-05 | full |
| FRC-ATT-2025 | Thematic review: Certification of Automated Tools and Techniques | Financial Reporting Council | regulator | https://media.frc.org.uk/documents/Thematic_Review_on_the_Certification_of_Automated_Tools_and_Techniques.pdf | 2025-06 | full |
| NIST-AI600-2024 | AI RMF: Generative AI Profile (NIST AI 600-1) | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | 2024-07 | full (section 2.2 read) |
| EWHC-AYINDE-2025 | R (Ayinde) v Haringey; Al-Haroun v Qatar National Bank [2025] EWHC 1383 (Admin) | High Court, King's Bench Divisional Court | regulator (court) | https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf | 2025-06-06 | full |
| CCDUDLEY-RODNEY-2026 | Rodney v Gee'z Micro Bar & Pitstop (AI use judgment) | County Court at Dudley | regulator (court) | https://www.judiciary.uk/wp-content/uploads/2026/05/Transcript-of-judgment-re-contempt-M00DD215.pdf | 2026-04-23 | full |
| EDRM-JOHNSONDUNN-2025 | When AI Policies Fail: The AI Sanctions in Johnson v. Dunn | EDRM (Hon. Ralph Artigliere, ret.) | community | https://edrm.net/2025/07/when-ai-policies-fail-the-ai-sanctions-in-johnson-v-dunn-and-what-they-mean-for-the-profession/ | 2025-07-31 | full |
| CANLAWMAG-SC-2026 | Sullivan & Cromwell apologizes to US bankruptcy judge for AI-generated errors | Canadian Lawyer | press | https://www.canadianlawyermag.com/news/international/sullivan-cromwell-apologizes-to-us-bankruptcy-judge-for-aigenerated-errors-in-prince-group-case/394014 | 2026-04-22 | full |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors | AP via CTV News | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 | full (via text mirror) |
| CTV-DELOITTENL-2025 | N.L. government pledges 'strict review' on AI use after more false citations found | CTV News | press | https://www.ctvnews.ca/canada/newfoundland-and-labrador/article/nl-government-pledges-strict-review-on-ai-use-after-more-false-citations-found-in-reports/ | 2025-11-29 | full (via text mirror) |
| CHARLOTIN-HALLUC-2026 | AI Hallucination Cases Database | Damien Charlotin | community | https://www.damiencharlotin.com/hallucinations/ | 2026-10-19 | full |
| STANFORD-MAGESH-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools | Stanford RegLab/HAI (arXiv 2405.20362) | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 | full (abstract page) |
| STANFORD-DAHL-2024 | Large Legal Fictions: Profiling Legal Hallucinations in LLMs | Stanford (arXiv 2401.01301) | academic | https://arxiv.org/abs/2401.01301 | 2024-06-21 (v2) | full (abstract page) |
| HBS-DELLACQUA-2023 | Navigating the Jagged Technological Frontier (WP 24-013) | Harvard Business School | academic | https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 | 2023-09 | full (abstract page via text mirror) |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? (NBER WP 35720) | NBER | academic | https://www.nber.org/papers/w35720 | 2026-09 (revised 2026-10) | full (abstract page; PDF blocked) |
| VALS-VLAIR-2025 | Vals Legal AI Report | Vals AI | academic (industry, not peer-reviewed) | https://www.vals.ai/vlair | 2025-02-27 | full |
| VALS-LEGALRESEARCH-2025 | VLAIR - Legal Research | Vals AI | academic (industry) | https://www.vals.ai/industry-reports/vlair-10-14-25 | 2025-10-14 | full |
| LLRX-FARRIS-2026 | "Hallucinations" by West & Lexis AI? | LLRX | press | https://www.llrx.com/2026/04/hallucinations-by-west-lexis-ai/ | 2026-04 | full |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026-09-30 (page metadata via text mirror) | full |
| ILTA-TECHSURVEY-2026 | ILTA Technology Survey 2026 Executive Summary | ILTA | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-08 (PDF metadata) | full |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice (Stand-out Lawyers Survey) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 | full (intro read; context only) |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026 | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03 | full |
| TRI-EVENTS-2026 | Trust by Verify; Beyond Human in the Loop (event listings) | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/events/trust-by-verify-catching-errors-in-ai-output-before-they-reach-the-court-or-client | 2026-10 | full (abstracts only) |
| ACCEVERLAW-2025 | GenAI Strategic Value for Corporate Law Departments Survey (press release) | ACC and Everlaw | survey | https://www.everlaw.com.au/press/release/acc-report-2025 | 2025-10-14 | full |
| KPMG-TRUST-2025 | Trust, attitudes and use of AI: A global study 2025 | University of Melbourne and KPMG | survey | https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf | 2025-04-28 (PDF metadata) | full |
| DACB-PI-2026 | Professional indemnity insurance: risk of AI hallucinations | DAC Beachcroft | firm | https://www.dacbeachcroft.com/en/what-we-think/professional-indemnity-insurance-risk-of-ai-hallucinations | 2026-09-28 | full |
| IAMAG-LAWPL-2026 | How Generative AI Is Reshaping Professional Liability Risk for Law Firms | Independent Agent magazine | press | https://www.iamagazine.com/?p=32247 | 2026-03-09 | full |
| TR-SQMS-2025 | SQMS 1 explained | Thomson Reuters tax and accounting blog | vendor | https://tax.thomsonreuters.com/blog/sqms-1-explained-a-practical-guide-to-firm-level-quality-management/ | 2025-09-02 | full |

Counts by type: academic 6 (Stanford x2, HBS, NBER, Vals x2), survey 6 (TR-FOP, ILTA, TRI-STANDOUT, ACC/Everlaw, KPMG; TR-FOP counted once), regulator 5 (Cal Bar x2, FRC, two court judgments), professional-body 4 (ABA, Law Society, Bar Council, ICMCI), press 5, community 2, conference 2, standard-setter 1, firm 1, vendor 1. Total 32 sources opened (including 1 used for context only).

---

## 6. Gaps

- **Quality evidence is largely absent.** No source gave override rates, reviewer catch rates, time-to-review, parallel-run results for review of AI-assisted deliverables, or inspection findings on generative AI in non-audit professional work. Error-rate evidence is for drafting and research tools, not for review.
- **Stanford hallucination study is for 2024 product versions.** A 2026 independent update for CoCounsel or Lexis Protégé was not found. The journal version (JELS, Apr 2025) was reported by LLRX and not opened.
- **Blocked or unreachable:** SRA pages (Cloudflare), AICPA pages, ABA canonical page (read via a LawNext copy), SSRN, NBER full PDF (abstract only), HBS PDF, Jenner & Block (Law360 summary on AI exclusions), Insurance Insider, Bloomberg Law, Law360 UK (BSB "absolute caution" warning, headline only), Lexology survey article (cookie wall).
- **Not opened (search summary only, not relied on):** Deloitte Canada CPA NL investigation; Berkley and Hamilton AI exclusions; 2026 ACC/Everlaw detail on outside counsel transparency; NSW practice note on AI; US state bar opinions beyond California (Florida, Texas, New York City, Pennsylvania); Federal Rule of Evidence 707 proposal.
- **Dates not found on page:** Law Society "Generative AI - the essentials" (year only), TR Future of Professionals (date from text-mirror metadata), ILTA summary (PDF metadata), Clearbrief citation-checking page (so not cited). Vendor citation-checking product documentation was not obtained.
- **Primary letters and orders not opened:** the Sullivan & Cromwell letter (18 Apr 2026) and the *Johnson v. Dunn* order (23 Jul 2025) are known only through secondary accounts.
- **Search budget:** web search hit its shared limit, so planned searches for verification-practice surveys (Clio, LexisNexis, Wolters Kluwer) and for Big Four quality-management statements were not run.
- **Consulting and accounting depth:** professional-body guidance for consulting is a single code (ICMCI); MCA, ICAEW, ACCA, IESBA, PCAOB and the Big Four quality statements were not reached. In-house shared-service review practices were not found.

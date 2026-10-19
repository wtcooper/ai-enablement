# Work production: governance and evidence (professional services)

Prepared 2026-10-19. Archetype: professional-services. Module: work-production. Angle: governance (what constrains and measures the work).

## 1. Summary

This note covers what constrains and measures AI-assisted substantive work in professional services: first drafts, research and synthesis, review against playbooks, and data extraction. It reads 35 sources (listed in section 5) across regulators, professional bodies, courts, academics, surveys, benchmarks, vendors, press and a community database. The sixteen use cases below are graded 4 A, 3 B, 5 C and 4 D.

- **Rules are settled; evidence of control quality is not.** ABA Formal Opinion 512 (2024-07-29), California's State Bar guidance (board-approved 2026-05-14), the Law Society of England and Wales, the ICMCI code for management consultants (adopted May 2026) and the IRS Office of Professional Responsibility (2026-06-24) all say the professional stays fully responsible and must verify AI output. None of them, and no firm, publishes an error, override or catch rate for a review step. The only measured error rates are independent tests of tools, not of firms' controls.
- **Verification is the binding constraint, and it is being enforced.** The English Divisional Court said (2025-06-06) it expects to ask whether leaders have taken practical measures. The SRA reported 42 potential-misuse reports in a year (via a Law Society of Ireland Gazette report, 2026-08). Ireland's High Court practice direction HC 142 takes effect 2026-09-01. A community database counted 2,202 court decisions on hallucinated content as of 2026-10-19.
- **Independent tool benchmarks give mixed task-level results.** Against a lawyer baseline, tools led on document Q&A, summarisation and (in Oct 2025) research accuracy, and trailed on redlining. Stanford's 2024 test found three vendor research tools hallucinated 17% to 33% of the time. Vendor contract-review benchmarks from 2026 are vendor-run.
- **Skill effects are measured only for juniors in one trial.** An NBER randomised trial (133 patent lawyers) found AI raised draft quality but the unaided-skill advantage sat with seniors; juniors' scores split.
- **Clients are the new constraint.** Client terms now conflict (must use AI, may not use AI, will not pay for AI-done work), and firms say they cannot yet show matter-level savings.
- **Access note.** SRA, AICPA tax pages, ACC-Everlaw, the NBER and HBS PDFs and the FRC were blocked or gated; web search was used 11 times before the shared budget ran out.


## 2. Use cases

```yaml
- id: professional-services-work-production-01
  title: AI-assisted first drafts of specialist legal documents, scored blind by expert reviewers
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Drafting complex legal documents is slow, skilled work, and firms do not know whether AI assistance raises the quality of what lawyers deliver or weakens the judgment they would otherwise build by drafting.
  solution: Practising lawyers draft with an AI assistant built for the task, and the output is scored by blinded expert reviewers. The patent-drafting trial also tested the same lawyers without AI after three months, to see whether any skill had been gained or lost.
  outcomes:
  - lever: quality
    description: AI access raised the blind-scored quality of benchmark patent drafting tasks, with larger gains for junior lawyers
    figure: 0.34 SD at 10 days; 0.38 SD at 90 days
    measures: Standard deviations of quality score (scored by blinded expert patent attorneys), AI-access group versus control, among 133 practising patent lawyers at eleven US IP law firms
    provenance: vendor-published
    source_ref: NBER-AUTOR-2026
  - lever: quality
    description: In an unaided redlining task after three months, the AI group outperformed controls, but the advantage sat with senior lawyers; juniors showed no average gain and their scores split into more poor and more good results
    figure: 0.32 SD overall; 0.45 SD among seniors; no average junior gain
    measures: Standard deviations of expert-scored redline quality without AI, treated versus control, same 133 lawyers
    provenance: vendor-published
    source_ref: NBER-AUTOR-2026
  - lever: speed
    description: In a separate randomised trial with law students (adjacent population), AI assistance raised productivity on five of six tasks
    figure: Vincent AI 38% to 115%; o1-preview 34% to 140%
    measures: Productivity gains in the paper's own productivity measure per task, 127 law students from two law schools, six legal assignments, versus no-AI condition
    provenance: independent
    source_ref: SCHWARCZ-APL-2025
  prerequisites:
  - An assistant tailored to the document type (the patent trial used a custom drafting assistant)
  - A blinded expert-scoring protocol, so quality is measured rather than assumed
  - A baseline task done without AI, to detect skill loss
  risks_and_guardrails:
  - Lawyers must review, verify and correct AI output and keep control of strategic judgment (CALBAR-GENAI-2026)
  - Gains in durable skill were concentrated in senior lawyers, so juniors need a separate plan (NBER-AUTOR-2026)
  - In the law-student trial, the reasoning model produced more fabricated citations than the retrieval-based tool (SCHWARCZ-APL-2025)
  human_checkpoints:
  - Senior lawyer reviews and signs off the draft before it leaves the firm
  - Blinded expert scoring in the study design; in practice, partner review
  role_evolution: NBER-AUTOR-2026 reports that seniors kept the skill benefit and juniors' outcomes diverged. 48% of surveyed professionals in the Thomson Reuters survey said they feared a negative impact on independent judgment development (TR-FOP-2026).
  evidence_grade: A
  sources:
  - ref: NBER-AUTOR-2026
    title: Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER Working Paper 35720)
    publisher: National Bureau of Economic Research (Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere)
    type: academic
    url: https://www.nber.org/papers/w35720
    date: 2026-09
    access: full
    locator: Abstract and disclosures
  - ref: SCHWARCZ-APL-2025
    title: 'AI-Powered Lawyering: AI Reasoning Models, Retrieval Augmented Generation, and the Future of Legal Practice'
    publisher: University of Minnesota and University of Michigan law schools (Schwarcz, Manning, Barry, Cleveland, Prescott, Rich)
    type: academic
    url: https://www.law.berkeley.edu/wp-content/uploads/archive/2025/12/AI-Powered-Lawyering.pdf
    date: '2025'
    access: full
    locator: Abstract; Introduction (127 law students, six assignments)
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Practical Guidance table, Duties of Competence and Diligence, pp. 4-5
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: Key findings 07 and 'A generation of disrupted development'
  last_reviewed: '2026-10-19'
  notes: Patent drafting is a specialist example of first-draft work; the module's generic case is the same loop on other documents. The study was run and paid for (direct costs) by Google and two authors are Google employees; it was pre-registered, used blinded graders and was issued as an NBER working paper. Full PDF was not readable (403), so figures come from the abstract. The law-student trial is an adjacent population, so it supports only the speed outcome. Choi, Monahan and Schwarcz (2023, via LEGALFUTURES-CHOI-2023) found GPT-4 gave large speed gains of 12% to 32% but only slight, inconsistent quality gains in 60 law students.
- id: professional-services-work-production-02
  title: Citation and authority verification gate before AI-assisted documents leave the firm
  archetype: professional-services
  module: work-production
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: AI can produce fluent text that cites authorities that do not exist or do not say what is claimed. Courts and regulators now treat unchecked citations as a professional-conduct failure, and the cases keep arriving.
  solution: Every authority, quotation and reference in an AI-assisted document is checked against an authoritative source before it goes to a court, client or counterparty. Checking can be partly automated (a reference-checker tool) but a named person remains responsible for the result and keeps a record of the check.
  outcomes:
  - lever: risk
    description: 'Scale of the failure the gate targets (not an outcome of the gate): the database counts court and tribunal decisions that addressed hallucinated content'
    figure: 2,202 cases identified so far (read 2026-10-19)
    measures: Decisions in which a court or tribunal found, or implied, that a party relied on hallucinated content, as tracked by the database author
    provenance: independent
    source_ref: CHARLOTIN-HALLUCINATIONS-2026
  - lever: quality
    description: 'Gate outcome data: none published for a deployed verification gate'
    figure: none published
    measures: No error-catch or override rate for a citation-verification step was found in any source read
    provenance: independent
    source_ref: CHARLOTIN-HALLUCINATIONS-2026
  prerequisites:
  - Access to authoritative sources (legislation databases, official law reports, reputable publisher databases)
  - A written rule on who checks, what is checked and where the record is kept
  - Training for lawyers and support staff
  risks_and_guardrails:
  - Competence and candor duties apply to AI output regardless of tool (ABA-OP512-2024; CALBAR-GENAI-2026)
  - California has proposed a rule comment saying the duty of candor includes verifying that cited authorities exist and are not misstated (CALBAR-RULES-2026)
  - Ireland's High Court practice direction HC 142, effective 1 September 2026, requires independent verification of AI-generated material and disclosure of any limit on doing so (LAWSOCIE-HC142-2026)
  - In England and Wales, the Divisional Court said it expects to ask whether leaders have taken practical measures so every individual understands and complies with their duties (EWHC-AYINDE-2025)
  - Retrieval-based legal research tools still produce wrong answers (STANFORD-MAGESH-2024)
  human_checkpoints:
  - The signing lawyer confirms each authority exists and supports the stated proposition
  - Supervising lawyer confirms the check was done before filing
  role_evolution: Responsibility sits with the signing lawyer and with firm leaders for having measures in place (EWHC-AYINDE-2025). Verification becomes a defined, recorded task rather than an informal habit.
  evidence_grade: C
  sources:
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.D, pp. 9-10 (candor toward the tribunal)
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Practical Guidance table, Candor to the Tribunal, p. 9
  - ref: CALBAR-RULES-2026
    title: Proposed Amendments to the Rules of Professional Conduct Related to Artificial Intelligence (public comment notice)
    publisher: State Bar of California
    type: regulator
    url: https://www.calbar.ca.gov/public/public-meetings-comment/public-comment/public-comment-archives/2026-public-comment/proposed-amendments-rules-professional-conduct-related-artificial-intelligence
    date: '2026-03-13'
    access: full
    locator: 'Discussion/proposal: amendment to rule 3.3'
  - ref: EWHC-AYINDE-2025
    title: R (Ayinde) v London Borough of Haringey; Al-Haroun v Qatar National Bank [2025] EWHC 1383 (Admin)
    publisher: High Court of Justice, King's Bench Division (Divisional Court)
    type: regulator
    url: https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf
    date: '2025-06-06'
    access: full
    locator: Paragraphs 6-9
  - ref: LAWSOC-GENAI-2026
    title: 'Generative AI: the essentials'
    publisher: Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials
    date: '2026'
    access: full
    locator: Section on duties to the court and the Rodney v Gee'z Micro Bar judgment
  - ref: LAWSOCIE-HC142-2026
    title: High Court expects 'human supervision' of GenAI
    publisher: Law Society of Ireland Gazette
    type: press
    url: https://www.lawsociety.ie/gazette/top-stories/2026/july/high-court-expects-human-supervision-of-genai/
    date: 2026-07
    access: full
    locator: '''Appropriately verified'' section'
  - ref: CHARLOTIN-HALLUCINATIONS-2026
    title: AI Hallucination Cases Database
    publisher: Damien Charlotin
    type: community
    url: https://www.damiencharlotin.com/hallucinations/
    date: '2026-10-19'
    access: full
    locator: Database introduction (case count)
  last_reviewed: '2026-10-19'
  notes: Graded C because the only product claim is the database author's statement that he built an automated reference checker (PelAIkan); no firm describes a deployed gate or reports a catch rate. The obligation to verify is firmly documented; the deployed practice and its measurement are not. Cal Bar rule amendments were out for comment (deadline 4 May 2026); adoption status not confirmed.
- id: professional-services-work-production-03
  title: AI-assisted legal research with source-grounded tools and a check against authoritative sources
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Lawyers need to find and synthesise authority quickly, but general chatbots invent sources and vendors' own 'hallucination-free' claims have been hard to check.
  solution: Research starts with a retrieval-grounded legal research tool (or a general model), and the lawyer checks every answer and citation against primary sources before relying on it.
  outcomes:
  - lever: quality
    description: 'Independent test of three vendor research tools: hallucination rate by tool'
    figure: Lexis+ AI, Westlaw AI-Assisted Research and Ask Practical Law AI each hallucinated between 17% and 33% of the time
    measures: Share of responses classed as hallucinated, over a pre-registered set of 202 legal queries, per the paper's typology
    provenance: independent
    source_ref: STANFORD-MAGESH-2024
  - lever: quality
    description: Accurate and incomplete answers differed widely by tool in the same test
    figure: Lexis+ AI answered 65% of queries accurately; Westlaw AI-Assisted Research 42%; Ask Practical Law AI gave incomplete answers on more than 60%
    measures: Share of the 202 queries in each response category (accurate, incomplete, hallucinated)
    provenance: independent
    source_ref: STANFORD-MAGESH-2024
  - lever: quality
    description: 'Later benchmark: accuracy on legal research questions against a lawyer baseline'
    figure: AI products 79% to 81%; lawyer baseline 71%
    measures: Accuracy criterion score (50% of the weighted rubric) over 210 questions across nine research types; Alexi, Counsel Stack, Midpage and ChatGPT versus lawyers
    provenance: independent
    source_ref: LAWSITES-VALSRESEARCH-2025
  - lever: risk
    description: Fabricated citations in a randomised law-student trial
    figure: 'Vincent AI: 3; no AI: 4; o1-preview: 11'
    measures: Count of citations to entirely fabricated sources across all completed assignments, by condition (127 students, six assignments each; adjacent population)
    provenance: independent
    source_ref: SCHWARCZ-APL-2025
  prerequisites:
  - Licence to a grounded legal research tool and to authoritative primary-source databases
  - A rule that tool output is a lead, not an authority
  risks_and_guardrails:
  - Hallucination persists in vendor tools that claim to avoid it (STANFORD-MAGESH-2024)
  - The three largest research platforms (Thomson Reuters, LexisNexis, vLex) did not take part in the October 2025 Vals research benchmark, so it does not measure them (LAWSITES-VALSRESEARCH-2025)
  - Lawyers who use AI for research must check it against authoritative sources (EWHC-AYINDE-2025)
  human_checkpoints:
  - Lawyer reads the cited authorities before relying on or filing them
  role_evolution: The lawyer's research effort shifts from locating authority to testing the tool's claims against sources.
  evidence_grade: A
  sources:
  - ref: STANFORD-MAGESH-2024
    title: Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362)
    publisher: Stanford University and Yale University (Magesh, Surani, Dahl, Suzgun, Manning, Ho)
    type: academic
    url: https://arxiv.org/abs/2405.20362
    date: '2024-05-30'
    access: full
    locator: Abstract; Section 1 (results summary)
  - ref: LAWSITES-VALSRESEARCH-2025
    title: Vals AI's Latest Benchmark Finds Legal and General AI Now Outperform Lawyers in Legal Research Accuracy
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2025/10/vals-ais-latest-benchmark-finds-legal-and-general-ai-now-outperform-lawyers-in-legal-research-accuracy.html
    date: '2025-10-23'
    access: full
    locator: '''Overview of the Study'' and ''Key Findings'''
  - ref: SCHWARCZ-APL-2025
    title: 'AI-Powered Lawyering: AI Reasoning Models, Retrieval Augmented Generation, and the Future of Legal Practice'
    publisher: University of Minnesota and University of Michigan law schools (Schwarcz, Manning, Barry, Cleveland, Prescott, Rich)
    type: academic
    url: https://www.law.berkeley.edu/wp-content/uploads/archive/2025/12/AI-Powered-Lawyering.pdf
    date: '2025'
    access: full
    locator: Introduction; Results III.A.1, Figure 7
  - ref: ILTA-TECHSURVEY-2026
    title: '2026 ILTA Technology Survey: Executive Summary'
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: Executive summary, p. 4 ('Enterprise-Scale Adoption')
  - ref: EWHC-AYINDE-2025
    title: R (Ayinde) v London Borough of Haringey; Al-Haroun v Qatar National Bank [2025] EWHC 1383 (Admin)
    publisher: High Court of Justice, King's Bench Division (Divisional Court)
    type: regulator
    url: https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf
    date: '2025-06-06'
    access: full
    locator: Paragraphs 6-8
  last_reviewed: '2026-10-19'
  notes: Independent measurements exist for the exact task, but all measure tools, not firm deployments; no firm reports its own research error rate. The Stanford figures are from 2024 and tools have changed since. ILTA reports that most GenAI-engaged firms now use generative tools for drafting, legal research, summarisation and contract review (survey of 508 firms; firms not named). The Vals research benchmark's 210 questions come from the LawSites report; a search summary said 200, so the press count was used. Vals lawyer baseline of 71% is as reported by LawSites.
- id: professional-services-work-production-04
  title: AI first pass for document extraction, question answering, summarisation and chronologies, with lawyer quality control
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - data-reporting
  - research-synthesis
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Lawyers spend long hours pulling facts, summaries and chronologies out of large document sets, and firms lack neutral evidence on whether tools do this as well as a lawyer.
  solution: An AI tool produces the extraction, answer, summary or chronology first; a lawyer reviews it. Task-level independent benchmarks show where tools beat a lawyer baseline and where lawyers remain ahead.
  outcomes:
  - lever: quality
    description: 'Document Q&A: best AI tool versus lawyer baseline'
    figure: Harvey Assistant 94.8%; CoCounsel 89.6%; lawyer baseline 70.1%
    measures: Task score against predefined evaluation criteria, one task among seven, lawyer baseline built from independent lawyers sourced by Cognia Law
    provenance: independent
    source_ref: VALS-VLAIR-2025
  - lever: quality
    description: 'Document summarisation: best tools versus lawyer baseline'
    figure: CoCounsel 77.2%; Harvey Assistant 72.1%; lawyer baseline 50.3%
    measures: Task score against predefined evaluation criteria
    provenance: independent
    source_ref: VALS-VLAIR-2025
  - lever: quality
    description: Data extraction was close to the baseline
    figure: Harvey Assistant 75.1%; CoCounsel 73.2%; lawyer baseline 71.1%
    measures: Task score against predefined evaluation criteria
    provenance: independent
    source_ref: VALS-VLAIR-2025
  - lever: quality
    description: 'Redlining: lawyers ahead of the AI tools that took part'
    figure: Lawyer baseline 79.7%; Harvey Assistant 65.0%; Vincent AI 53.6%
    measures: Task score against predefined evaluation criteria
    provenance: independent
    source_ref: VALS-VLAIR-2025
  prerequisites:
  - Documents available to the tool in a secure environment
  - A review step sized to the tool's tested accuracy for the task
  - Task-specific testing before relying on a tool (ABA-OP512-2024)
  risks_and_guardrails:
  - Scores are by task and by tool; vendors chose which tasks to enter and Lexis+ AI withdrew from the sections studied (VALS-VLAIR-2025)
  - The test treated each product as a text generator through an API, not as a full workflow (VALS-VLAIR-2025)
  - Lawyers must supervise and verify outputs (CALBAR-GENAI-2026; ABA-OP512-2024)
  human_checkpoints:
  - Lawyer reviews extracted facts and summaries against source documents, sampled to the tool's tested reliability
  role_evolution: Lawyers move from producing first-pass summaries to checking and correcting them.
  evidence_grade: A
  sources:
  - ref: VALS-VLAIR-2025
    title: Vals Legal AI Report (VLAIR)
    publisher: Vals AI
    type: survey
    url: https://www.vals.ai/vlair
    date: '2025-02-27'
    access: full
    locator: Executive summary results table; Methodology (lawyer baseline); Notes on study limitation
  - ref: ILTA-TECHSURVEY-2026
    title: '2026 ILTA Technology Survey: Executive Summary'
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: Executive summary, p. 4
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.A, p. 4
  last_reviewed: '2026-10-19'
  notes: Vals AI disclosed a customer relationship with at least one participating vendor; the dataset was created by a consortium of law firms (Reed Smith, Fisher Phillips, McDermott Will & Emery, Ogletree Deakins and four anonymous firms). The report is dated 27 February 2025 and is slightly outside the 18-month window; no later Vals report on these tasks was found. Tool versions are from late 2024.
- id: professional-services-work-production-05
  title: Sample-based validation of AI review and summarisation before the firm relies on it
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Reading every AI summary against its source removes the time saving, but relying on an unchecked tool breaches the competence duty.
  solution: Before relying on a tool for a set of documents, the team tests it on a small sample by comparing its output with a manual review. If the sample shows the tool is accurate for that task, the team may rely on it for the rest, and repeats the test when the tool or task changes.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: No firm reports a sample size, pass threshold or catch rate for such a validation step
    provenance: independent
    source_ref: ABA-OP512-2024
  prerequisites:
  - A defined sample method and acceptance threshold
  - Manual reviewers independent of the tool output
  - Re-test when models are updated (CALBAR-GENAI-2026)
  risks_and_guardrails:
  - The ABA says the right amount of verification depends on the tool and task, and that a lawyer remains fully responsible whatever level is chosen (ABA-OP512-2024)
  - California says the duty includes periodic reassessment as AI systems change (CALBAR-GENAI-2026)
  - A sample that is too small or unrepresentative gives false comfort (no source tests this)
  human_checkpoints:
  - Lawyer compares sampled tool output with the manual result and decides whether to rely on the tool
  role_evolution: Quality control becomes a measured test run by a senior reviewer, not a read-through by whoever drafted.
  evidence_grade: D
  sources:
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.A, p. 4 (contract-summary example)
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Practical Guidance table, Duties of Competence and Diligence, p. 5
  - ref: TRI-EVENTS-2026
    title: Thomson Reuters Institute events listing
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/events
    date: '2026-10-19'
    access: full
    locator: 'Past events: ''Trust by Verify'' (15 Oct 2026)'
  last_reviewed: '2026-10-19'
  notes: 'Idea. The ABA opinion describes the approach as acceptable; the Thomson Reuters Institute held a webinar on 15 October 2026 titled ''Trust by Verify: Catching Errors in AI Output Before They Reach the Court or Client'' (only the title and listing were read, no content). A search-result snippet in the landscape file names an ILTACON session on validating AI workflows in eDiscovery; it was not opened here.'
- id: professional-services-work-production-06
  title: AI contract review and redlining against a playbook (in-house)
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: In-house legal teams review large volumes of commercial contracts against fixed positions, and need to know if AI redlines are good enough to cut review time.
  solution: A contract-review tool applies the team's playbook, flags issues and proposes redlines; a lawyer reviews and edits. Vendors publish benchmarks, while the one independent task benchmark found lawyers ahead on redlining.
  outcomes:
  - lever: quality
    description: 'Vendor-commissioned blind comparison: one human attorney versus two AI tools on 19 contracts'
    figure: Human attorney 4.56; Ivo 4.52; Claude for Word (Opus 4.6) 3.50 (out of 10)
    measures: Mean score across three blind judges on five criteria (issue spotting, surgical redlining, formatting retention, judgment, comments), 19 anonymised contracts, one reviewing attorney
    provenance: vendor-published
    source_ref: IVO-BENCH-2026
  - lever: speed
    description: Review time reported in the same study
    figure: Human attorney about 10 hours for 19 contracts; Ivo average 2 minutes 45 seconds per contract
    measures: Time to review, as stated in the release
    provenance: vendor-published
    source_ref: IVO-BENCH-2026
  - lever: quality
    description: Vendor benchmark of 11 AI models against the vendor's own product on 21 contract guidelines
    figure: LegalOn ranked first on all 21 provision types
    measures: Pairwise wins judged by an LLM judge over 3,282 head-to-head contract reviews (each comparison run twice with order reversed)
    provenance: vendor-published
    source_ref: LEGALON-BENCH-2026
  - lever: quality
    description: 'Independent task benchmark: redlining'
    figure: Lawyer baseline 79.7%; Harvey Assistant 65.0%
    measures: Task score against predefined evaluation criteria
    provenance: independent
    source_ref: VALS-VLAIR-2025
  prerequisites:
  - A written, machine-usable playbook
  - Review of tool output by a lawyer
  - A test on the team's own contracts
  risks_and_guardrails:
  - Both 2026 benchmarks are run or commissioned by the vendor whose product leads; the LegalOn CEO's own article says buyers should treat vendor benchmarks with some scepticism (ARTLAW-LEGALON-2026)
  - The Ivo study used one human attorney and 19 contracts, so differences are not statistically established
  - General-purpose models missed the legal standard even when they found the right clause (ARTLAW-LEGALON-2026)
  human_checkpoints:
  - Lawyer accepts, edits or rejects each redline before it goes to the counterparty
  role_evolution: In-house lawyers spend less time on first-pass markups and more on negotiation positions and playbook upkeep (vendor framing in IVO-BENCH-2026).
  evidence_grade: C
  sources:
  - ref: IVO-BENCH-2026
    title: Ivo Outperforms Claude for Word in Independent Contract Review Benchmark (press release)
    publisher: Ivo
    type: vendor
    url: https://www.ivo.ai/news/ivo-outperforms-claude-for-word-in-independent-contract-review-benchmark
    date: '2026'
    access: full
    locator: Results at a glance; About the Study
  - ref: LEGALON-BENCH-2026
    title: LegalOn 2026 Contract Review Benchmark
    publisher: LegalOn
    type: vendor
    url: https://www.legalontech.com/post/the-contract-review-benchmark-2026
    date: '2026-06-03'
    access: full
    locator: Executive summary; The Rankings
  - ref: ARTLAW-LEGALON-2026
    title: What Legal AI Benchmarks Reveal That Model Names Don't (by Daniel Lewis, CEO, LegalOn)
    publisher: Artificial Lawyer
    type: press
    url: https://artificiallawyer.com/2026/06/22/what-legal-ai-benchmarks-reveal-that-model-names-dont
    date: '2026-06-22'
    access: full
    locator: Opening paragraphs; 'First' and 'Second' points
  - ref: VALS-VLAIR-2025
    title: Vals Legal AI Report (VLAIR)
    publisher: Vals AI
    type: survey
    url: https://www.vals.ai/vlair
    date: '2025-02-27'
    access: full
    locator: Executive summary results table (Redlining row)
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.A, p. 4
  last_reviewed: '2026-10-19'
  notes: 'Tag: in-house. The landscape search found no independent, peer-reviewed study of AI contract review against playbooks versus lawyers. Named customer deployments of these two products were not read, so maturity is left at ''announced''. The Ivo release gives April 2026 as the study date but no release date.'
- id: professional-services-work-production-07
  title: AI-assisted consulting analysis and content tasks, with judgment-heavy tasks held human-first
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - research-synthesis
  - document-production
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: Consultants do not know which tasks AI helps with and which it makes worse, because the boundary between them is uneven and not obvious from the task description.
  solution: Teams use AI for tasks inside its demonstrated capability (the study tasks ran from creative to analytical) and keep complex managerial-judgment tasks human-first, with an extra check if AI is used. The pattern is task-allocation rules rather than a single workflow, so it is recorded as 'other'.
  outcomes:
  - lever: capacity
    description: 'Inside-frontier tasks: AI users completed more tasks'
    figure: 12.2% more tasks completed on average
    measures: Tasks completed among 758 BCG knowledge workers across a set of 18 realistic tasks, AI-access versus no-AI
    provenance: independent
    source_ref: HBS-DELLACQUA-2023
  - lever: speed
    description: 'Inside-frontier tasks: AI users were faster'
    figure: 25.1% more quickly on average
    measures: Completion time on the 18 tasks, AI-access versus no-AI
    provenance: independent
    source_ref: HBS-DELLACQUA-2023
  - lever: quality
    description: 'Outside-frontier task (a complex managerial problem): AI users were less likely to be right'
    figure: 19% less likely to produce correct solutions
    measures: Likelihood of a correct solution on one task chosen to lie outside AI's capabilities, AI-access versus no-AI
    provenance: independent
    source_ref: HBS-DELLACQUA-2023
  prerequisites:
  - A way to classify tasks by AI capability, kept current as models change
  - Reviewer awareness that fluent AI output can be wrong on judgment-heavy problems
  risks_and_guardrails:
  - Consultants should guard against over-reliance on AI, especially outside their own expertise, and seek specialist input in technical or regulated areas (ICMCI-AICODE-2026)
  - Tasks were researcher-designed and the model was GPT-4, so the frontier today is different (HBS-DELLACQUA-2023)
  - Independent task benchmarks show lawyers ahead on redlining and EDGAR research (VALS-VLAIR-2025)
  human_checkpoints:
  - Manager decides which tasks are AI-first and which are human-first
  - Qualified consultant reviews AI-influenced analysis before client delivery
  role_evolution: Reviewers need to judge whether a task is within AI's capability; the paper describes the frontier as uneven, even between tasks of seemingly similar difficulty.
  evidence_grade: A
  sources:
  - ref: HBS-DELLACQUA-2023
    title: Navigating the Jagged Technological Frontier (HBS Working Paper 24-013)
    publisher: Harvard Business School with Boston Consulting Group (Dell'Acqua, McFowland, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon, Lakhani)
    type: academic
    url: https://www.hbs.edu/faculty/Pages/item.aspx?num=64700
    date: 2023-09
    access: full
    locator: Abstract
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version 1.0
    publisher: International Council of Management Consulting Institutes (ICMCI)
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: Section 5.3, Professional competence and reliance on AI
  - ref: VALS-VLAIR-2025
    title: Vals Legal AI Report (VLAIR)
    publisher: Vals AI
    type: survey
    url: https://www.vals.ai/vlair
    date: '2025-02-27'
    access: full
    locator: Executive summary (EDGAR research and redlining)
  last_reviewed: '2026-10-19'
  notes: Foundational evidence from September 2023, outside the 18-month window and based on GPT-4; the full PDF was not readable (403), so only abstract figures are used. Provenance marked independent because the authors are academics, although BCG co-designed the tasks and its staff were the subjects. A is justified by the measured field experiment with a named consulting firm; no consulting firm publishes comparable deployment data.
- id: professional-services-work-production-08
  title: AI-use disclosure and provenance labelling of work product
  archetype: professional-services
  module: work-production
  function: risk-compliance-legal
  work_types:
  - document-production
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Clients and regulators increasingly want to know when AI shaped advice or a deliverable, and undisclosed AI use is surfacing as a trust and contract issue.
  solution: Matter and engagement records capture where AI was used and how it was verified; deliverables carry a disclosure when AI materially shaped the analysis; AI-generated material is marked in client files so later users know it may be fallible.
  outcomes:
  - lever: risk
    description: 'Cost of an undisclosed, unreviewed case: Deloitte Australia agreed to repay the final instalment of an A$440,000 government contract after a 237-page report contained apparent AI-generated errors; the revised report disclosed Azure OpenAI use'
    figure: partial refund of A$440,000 contract (amount to be made public)
    measures: Contract value and department statement as reported by AP; refund described as the final instalment
    provenance: independent
    source_ref: CTV-DELOITTE-2025
  - lever: risk
    description: 'Control outcome data: none published'
    figure: none published
    measures: No source reports measured effects of a disclosure step
    provenance: independent
    source_ref: ICMCI-AICODE-2026
  prerequisites:
  - A defined threshold for material AI use (the ICMCI code says routine productivity tools need not be individually disclosed)
  - A place in the engagement record to log AI use
  - Engagement-letter terms covering AI use
  risks_and_guardrails:
  - ABA suggests marking GAI-produced material when stored in client or firm files (ABA-OP512-2024)
  - Disclosure may be appropriate where AI materially affects decision-making; lawyers must also follow client guidelines that limit AI use (CALBAR-GENAI-2026)
  - Consultants must tell clients when AI materially affects advice or deliverables (ICMCI-AICODE-2026)
  - Canada's Public Services and Procurement Canada now requires suppliers to identify any use of AI in advance (BNN-DELOITTE-2025)
  human_checkpoints:
  - Engagement lead decides whether AI use is material and approves the disclosure wording
  role_evolution: Engagement leads take on a record-keeping duty for AI use that did not exist in earlier deliverable sign-off.
  evidence_grade: B
  sources:
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.E, footnote 52, p. 10; Part II.C, pp. 8-9
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Practical Guidance table, Communication Regarding Generative AI Use, p. 7
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version 1.0
    publisher: International Council of Management Consulting Institutes (ICMCI)
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: Sections 3.3 and 7.1
  - ref: BNN-DELOITTE-2025
    title: Feds defend $1.1-million Deloitte contract for AI advice after firm admitted mistakes (Canadian Press)
    publisher: BNN Bloomberg / The Canadian Press
    type: press
    url: https://www.bnnbloomberg.ca/business/company-news/2025/12/18/feds-defend-11-million-deloitte-contract-for-ai-advice-after-firm-admitted-mistakes/
    date: '2025-12-18'
    access: full
    locator: Paragraph beginning 'Public Services and Procurement Canada confirmed...'
  - ref: CTV-DELOITTE-2025
    title: Deloitte to partially refund Australian government for report with apparent AI-generated errors (AP)
    publisher: CTV News / Associated Press
    type: press
    url: https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/
    date: '2025-10-07'
    access: full
    locator: Paragraphs 1-6
  last_reviewed: '2026-10-19'
  notes: 'Graded B: a named client (Public Services and Procurement Canada) states it requires advance identification of AI use by suppliers, and a named firm revised a report with a disclosure; no source measures the effect. The Deloitte figures are from press reports of a dispute; Deloitte Australia said it had reviewed the 237-page report and ''confirmed some footnotes and references were incorrect''. The Canadian report for Newfoundland and Labrador involved Deloitte Canada, which said AI was ''selectively used to support a small number of research citations''.'
- id: professional-services-work-production-09
  title: Agentic matter workflows with defined review gates and supervision proportional to autonomy
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - document-production
  - coordination-scheduling
  - review-assurance
  pattern: draft-review-loop
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Agents can run several steps of a legal task without a prompt, which raises the risk that nobody reviews the output; the supervision model for multi-step AI work is not yet settled.
  solution: A matter is broken into phases and tasks with a named reviewer at each gate. Agents execute defined tasks; lawyers review at designated gates before the next step starts. Supervision rises with the agent's autonomy and no agent sends, files or advises without lawyer approval.
  outcomes:
  - lever: capacity
    description: 'Vendor expectation, not a measurement: agents taking on more workflow steps'
    figure: Expects agents to take on an additional 20% of workflow steps over six months, and the share to triple within a year
    measures: Share of legal workflow steps executed by agents rather than prompted by lawyers, as the vendor 'expects'
    provenance: vendor-published
    source_ref: HARVEY-ORCH-2026
  prerequisites:
  - Reusable matter templates that define phases, tasks, playbooks and reviewers
  - Audit trail of agent actions
  - Limits on the systems and data an agent may reach
  risks_and_guardrails:
  - Lawyers must not let agentic systems make substantive legal determinations, communicate advice or file pleadings without meaningful supervision (CALBAR-GENAI-2026)
  - No document may go to a court without lawyer review and approval; agents must not autonomously file or communicate with the court (CALBAR-GENAI-2026)
  - Agentic systems must not send client information externally without safeguards and human review (CALBAR-GENAI-2026)
  - The Law Society defines agentic systems as able to decide and act with limited or no human supervision (LAWSOC-GENAI-2026)
  human_checkpoints:
  - Designated partner or reviewer approves each gated task before the next begins
  - Lawyer approval before any external transmission or filing
  role_evolution: Harvey says lawyers will focus more on directing the matter, reviewing consequential outputs and exercising judgment (HARVEY-ORCH-2026, vendor view). Whether that changes junior roles is not measured.
  evidence_grade: C
  sources:
  - ref: HARVEY-ORCH-2026
    title: Making Harvey the Orchestration Layer for Legal Work
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/legal-work-orchestration
    date: '2026-10-15'
    access: full
    locator: '''How Legal Orchestration Works''; ''The Future of Legal Work Orchestration'''
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Executive Summary, Agentic AI, p. 2; Confidentiality, pp. 5-6; Candor to the Tribunal, p. 9
  - ref: LAWSOC-GENAI-2026
    title: 'Generative AI: the essentials'
    publisher: Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials
    date: '2026'
    access: full
    locator: Definition of agentic AI in the glossary and agentic section
  - ref: TRI-EVENTS-2026
    title: Thomson Reuters Institute events listing
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/events
    date: '2026-10-19'
    access: full
    locator: 'Upcoming webinar: ''Beyond Human in the Loop'' (scheduled 11 Nov 2026)'
  last_reviewed: '2026-10-19'
  notes: 'Harvey launched Legal Work Orchestration on 15 October 2026 and says tasks, comments and notifications are rolling out now, with an early-access programme for templates; no customer outcome is cited, so maturity is ''announced''. The Thomson Reuters Institute webinar ''Beyond Human in the Loop: Redefining Accountability in AI-Assisted Legal Work'' is scheduled for 11 November 2026 (listing only; used as a signal, not as evidence). Tag note: Harvey also markets this for in-house teams, but the post gives no in-house example.'
- id: professional-services-work-production-10
  title: 'Gated AI rollout: written policy, training before access, vetted tools and named leadership accountability'
  archetype: professional-services
  module: work-production
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Regulators and courts now expect leaders to show they took practical steps so every lawyer understands their duties when using AI, yet policy and training coverage varies sharply by firm size.
  solution: The firm adopts a written AI policy, restricts use to approved tools, requires training before access and review of AI-assisted work, names who is accountable, and updates all of this as tools become more autonomous.
  outcomes:
  - lever: risk
    description: Share of firms with a formal GenAI policy, by firm size
    figure: 57% of firms under 50 lawyers; 80% of 50-149; 85% of 150-349; 98% of 350-699; 91% of over 700
    measures: Percent of responding firms in each size band selecting 'A formal policy is in place' in ILTA survey Q3.18
    provenance: independent
    source_ref: ILTA-TECHSURVEY-2026
  - lever: risk
    description: Share of firms requiring specific training before use, by firm size
    figure: 11% of firms under 50 lawyers; 30%; 47%; 63%; 72% of over 700
    measures: Percent of responding firms in each size band selecting 'Specific training required before use' in ILTA survey Q3.18
    provenance: independent
    source_ref: ILTA-TECHSURVEY-2026
  - lever: quality
    description: Where an organisation has a named AI strategy, more professionals say AI is meeting expectations
    figure: 66% with a named strategy versus 22% with no active strategy
    measures: Percent of surveyed professionals (1,816 across law, tax, audit, accounting, compliance, risk and trade) saying AI is meeting or exceeding expectations for creating value at work
    provenance: vendor-published
    source_ref: TR-FOP-2026
  prerequisites:
  - A named accountable partner or committee
  - An approved-tool list and a way to enforce it
  - Training content for lawyers and support staff
  risks_and_guardrails:
  - Managing lawyers must set clear AI policies and ensure training (ABA-OP512-2024; CALBAR-GENAI-2026)
  - California has proposed that managerial lawyers must make reasonable efforts to establish internal AI policies and procedures (CALBAR-RULES-2026)
  - The English Divisional Court said it expects to ask whether leadership responsibilities were fulfilled (EWHC-AYINDE-2025)
  - The SRA reported 42 reports of potential AI misuse between July 2025 and July 2026, covering citations, supervision and confidentiality (LAWSOCIE-SRAWARN-2026)
  - EU AI literacy obligations have applied since 2 February 2025 (EC-AIACT-2026)
  human_checkpoints:
  - Partner or committee approves tools and policy
  - Individuals complete training before access
  role_evolution: ILTA respondents expect added headcount in IT, innovation, security, training, knowledge management and data science (ILTA-TECHSURVEY-2026). Firm leaders acquire a documented accountability role for AI use (EWHC-AYINDE-2025).
  evidence_grade: C
  sources:
  - ref: ILTA-TECHSURVEY-2026
    title: '2026 ILTA Technology Survey: Executive Summary'
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: Executive summary, p. 5, table Q3.18; p. 3 (Copilot licences on request)
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: Key findings 04 and 05
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.E, pp. 10-11
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Practical Guidance table, Duty to Supervise, p. 7
  - ref: CALBAR-RULES-2026
    title: Proposed Amendments to the Rules of Professional Conduct Related to Artificial Intelligence (public comment notice)
    publisher: State Bar of California
    type: regulator
    url: https://www.calbar.ca.gov/public/public-meetings-comment/public-comment/public-comment-archives/2026-public-comment/proposed-amendments-rules-professional-conduct-related-artificial-intelligence
    date: '2026-03-13'
    access: full
    locator: Amendments to rule 5.1
  - ref: EWHC-AYINDE-2025
    title: R (Ayinde) v London Borough of Haringey; Al-Haroun v Qatar National Bank [2025] EWHC 1383 (Admin)
    publisher: High Court of Justice, King's Bench Division (Divisional Court)
    type: regulator
    url: https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf
    date: '2025-06-06'
    access: full
    locator: Paragraph 9
  - ref: LAWSOCIE-SRAWARN-2026
    title: SRA issues warning notice on use of AI
    publisher: Law Society of Ireland Gazette
    type: press
    url: https://www.lawsociety.ie/gazette/top-stories/2026/august/sra-issues-warning-notice-on-use-of-ai/
    date: 2026-08
    access: full
    locator: Opening paragraphs
  - ref: EC-AIACT-2026
    title: 'AI Act: regulatory framework for AI'
    publisher: European Commission, Digital Strategy
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: Application timeline list
  last_reviewed: '2026-10-19'
  notes: 'Graded C: the figures are survey prevalence, not outcomes of the practice, and no responding firm is named. The ILTA narrative says most firms now require human review and independent verification of citations, but its size-band table shows ''Outputs must be cited/independently verified'' at 25% to 60% and ''Work product must be reviewed by a human'' at 31% to 83%; the table figures are used. ILTA also reports more than half of respondents issue Copilot licences only on request. The Thomson Reuters figures come from a survey by a vendor of AI tools for professionals. A Thomson Reuters speaker at Legalweek 2026 said firms with a GenAI strategy were 3.9 times more likely to achieve ROI and that only 22% of firms have one (TRI-LEGALWEEK-2026, ''The pressure hasn''t yet found a release valve''); the denominator was not stated.'
- id: professional-services-work-production-11
  title: Replace unsanctioned AI use with sanctioned, professional-grade tools
  archetype: professional-services
  module: work-production
  function: risk-compliance-legal
  work_types:
  - review-assurance
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: When approved tools are missing or weak, professionals use their own AI tools out of sight of the organisation, creating data-exposure and quality risks the firm cannot see.
  solution: The firm supplies an approved tool grounded in authoritative content, with confidentiality terms, and treats gaps in tool access as the reason for shadow use rather than only a discipline problem.
  outcomes:
  - lever: risk
    description: Unsanctioned use
    figure: 34% of professionals use AI tools their organisation has not sanctioned
    measures: Percent of the 1,816 surveyed professionals who said they use AI tools their organisation hasn't sanctioned
    provenance: vendor-published
    source_ref: TR-FOP-2026
  - lever: risk
    description: Access gap
    figure: 41% lack access to AI tools designed for professional work built on verified content
    measures: 'Percent of surveyed professionals who use AI at work and lack such tools (source wording: ''two in five professionals who use AI at work'')'
    provenance: vendor-published
    source_ref: TR-FOP-2026
  prerequisites:
  - Budget for a professional-grade tool
  - Data-handling terms the firm has reviewed rather than relied on marketing assurances (CALBAR-GENAI-2026)
  risks_and_guardrails:
  - Free or consumer tools may reuse inputs for training (CALBAR-GENAI-2026; ABA-OP512-2024)
  - Professionals say tools must safeguard confidential data (96%), ground outputs in authoritative content (94%) and give reasoning that can be explained (90%) (TR-FOP-2026)
  - Source is a vendor survey, so the 'professional-grade tool' framing serves the publisher
  human_checkpoints:
  - IT and risk approve the tool list
  - Supervisors review work for undeclared AI use
  role_evolution: TR-FOP-2026 reports 32% of professionals who use fiduciary-grade AI would turn down a role that lacked it, against 12% of those without access.
  evidence_grade: C
  sources:
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: Key findings 03 and 08; 'The fiduciary standard' and 'Shadow AI' passages
  - ref: ILTA-TECHSURVEY-2026
    title: '2026 ILTA Technology Survey: Executive Summary'
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: Executive summary, p. 3 and p. 5 (approved apps)
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Practical Guidance table, Duty of Confidentiality, p. 5
  last_reviewed: '2026-10-19'
  notes: The survey denominator for the 34% is described only as 'professionals'; the 41% is described as professionals who use AI at work. The figures are vendor-published and self-reported by respondents. ILTA's table shows that 'only vetted/firm-approved apps' is a policy at 39% (under 50 lawyers) to 79% (350-699) of responding firms.
- id: professional-services-work-production-12
  title: Operationalise client AI terms at matter set-up (permission, no-pay and invoice-transparency rules)
  archetype: professional-services
  module: work-production
  function: risk-compliance-legal
  work_types:
  - coordination-scheduling
  - review-assurance
  pattern: intake-triage
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: 'Client guidelines now conflict: some require firms to use AI and show the savings, others bar AI without permission, and some say they will not pay for work done by AI. Firms need a way to know which terms apply to each matter.'
  solution: At matter opening, the client's AI terms (permitted tools, approval needed, billing treatment, reporting) are captured and fed into tool access and billing rules, so lawyers do not have to remember them.
  outcomes:
  - lever: risk
    description: Firms requiring client approval for AI use, by firm size
    figure: 8% of firms under 50 lawyers; 20%; 24%; 38%; 34% of over 700
    measures: Percent of responding firms in each size band selecting 'Must obtain client approval' in ILTA survey Q3.18
    provenance: independent
    source_ref: ILTA-TECHSURVEY-2026
  - lever: cost
    description: In-house counsel seeing no savings from outside counsel's AI use
    figure: Nearly 60% saw 'no noticeable savings yet'
    measures: Share of respondents to the ACC-Everlaw survey (about 650 in-house counsel and legal operations staff, fielded 18 June-18 July 2025), as reported by Bloomberg Law
    provenance: independent
    source_ref: BLOOMBERGLAW-ACC-2025
  prerequisites:
  - A field for AI terms in matter intake
  - A way to push restrictions into tool access
  - Agreement with the client on how AI savings will be shown
  risks_and_guardrails:
  - Lawyers must follow client instructions or guidelines that restrict AI (CALBAR-GENAI-2026)
  - Consultants must comply with client instructions about AI and raise concerns if a client's AI practices look risky (ICMCI-AICODE-2026)
  - Billing for AI-assisted work must reflect actual time or the agreed fee basis (ABA-OP512-2024; routed to billing-collections)
  human_checkpoints:
  - Responsible partner confirms client AI terms at matter opening
  - Client approval recorded where required
  role_evolution: The firm-side voices in TRI-LEGALWEEK-2026 include a chief pricing and innovation officer, an AI innovation head and a technology innovation director, not only matter partners.
  evidence_grade: B
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: '''The contradictions in the room'''
  - ref: BLOOMBERGLAW-ACC-2025
    title: AI Does Little to Reduce Law Firm Billable Hours, Survey Shows
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/us-law-week/ai-does-little-to-reduce-law-firm-billable-hours-survey-shows
    date: '2025-10-14'
    access: full
    locator: Paragraphs on outside counsel guidelines and survey results
  - ref: BNN-DELOITTE-2025
    title: Feds defend $1.1-million Deloitte contract for AI advice after firm admitted mistakes (Canadian Press)
    publisher: BNN Bloomberg / The Canadian Press
    type: press
    url: https://www.bnnbloomberg.ca/business/company-news/2025/12/18/feds-defend-11-million-deloitte-contract-for-ai-advice-after-firm-admitted-mistakes/
    date: '2025-12-18'
    access: full
    locator: Public Services and Procurement Canada paragraph
  - ref: ILTA-TECHSURVEY-2026
    title: '2026 ILTA Technology Survey: Executive Summary'
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: Executive summary, p. 5, table Q3.18
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Communication Regarding Generative AI Use, p. 7
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version 1.0
    publisher: International Council of Management Consulting Institutes (ICMCI)
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: Sections 5.4 and 7.3
  last_reviewed: '2026-10-19'
  notes: 'Tag: in-house (client side: GSK''s chief of staff for legal and compliance spoke at Legalweek; the ACC-Everlaw respondents are in-house). A Gartner analyst quoted by Bloomberg Law said more companies are adding provisions to outside counsel guidelines asking that lower-risk tasks be done by AI and the time savings reflected in billable hours. DLA Piper''s head of AI innovation said both ''must use AI'' and ''cannot use AI without permission'' directives were arriving in the same inbox (TRI-LEGALWEEK-2026). No firm describes the system it uses to track these terms, so the matter-level tooling is an inference from the stated problem; the grade reflects a named client requirement (Public Services and Procurement Canada), not a named firm deployment.'
- id: professional-services-work-production-13
  title: Reference and footnote verification gate for consulting and advisory reports
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Consulting reports can include fabricated or wrong references, as the Deloitte reports for the Australian and Newfoundland and Labrador governments showed, and clients cannot easily tell.
  solution: Before delivery, every reference, quotation and calculation in an AI-assisted report is independently checked by the firm; some commentators suggest clients also set review protocols or require proof the research was done.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: No consulting firm publishes a pre-delivery verification step or its catch rate
    provenance: independent
    source_ref: ICMCI-AICODE-2026
  prerequisites:
  - Engagement-level rule that no unverified AI output is delivered as finished work
  - Access to the cited sources
  risks_and_guardrails:
  - The ICMCI code forbids submitting unreviewed AI outputs as finished work and requires independent verification of facts, calculations, citations and references (ICMCI-AICODE-2026)
  - The Australian report was originally published in July 2025 and revised after a researcher flagged fabricated references (CTV-DELOITTE-2025)
  human_checkpoints:
  - Engagement lead signs that references were verified
  - Quality partner spot-checks citations on high-profile reports
  role_evolution: Reviewers take responsibility for source verification that earlier peer review assumed the author had done.
  evidence_grade: D
  sources:
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version 1.0
    publisher: International Council of Management Consulting Institutes (ICMCI)
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: Sections 2.3, 5.1, 5.2
  - ref: CTV-DELOITTE-2025
    title: Deloitte to partially refund Australian government for report with apparent AI-generated errors (AP)
    publisher: CTV News / Associated Press
    type: press
    url: https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/
    date: '2025-10-07'
    access: full
    locator: Paragraphs 1-8
  - ref: BNN-DELOITTE-2025
    title: Feds defend $1.1-million Deloitte contract for AI advice after firm admitted mistakes (Canadian Press)
    publisher: BNN Bloomberg / The Canadian Press
    type: press
    url: https://www.bnnbloomberg.ca/business/company-news/2025/12/18/feds-defend-11-million-deloitte-contract-for-ai-advice-after-firm-admitted-mistakes/
    date: '2025-12-18'
    access: full
    locator: Paragraphs on expert recommendations (Carleton and Toronto professors)
  last_reviewed: '2026-10-19'
  notes: Idea. The incident and the ICMCI duty are documented; the gate itself is not shown as deployed anywhere. A Carleton University public-management professor, quoted by the Canadian Press, suggested governments set up protocols to fact-check consultants' reports and require proof firms did the research themselves. Deloitte Canada said AI was not used to write the Newfoundland and Labrador report but was 'selectively used to support a small number of research citations'.
- id: professional-services-work-production-14
  title: Firm-run evaluation against an expert baseline before adopting or re-approving an AI tool
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Vendor claims are hard to compare, vendors have been shown to overstate (hallucination-free claims), and firms say they cannot yet quantify AI returns.
  solution: The firm tests candidate tools on its own representative tasks, scored against a lawyer baseline by blinded reviewers, and repeats the test when the model or task changes. A consortium of law firms did this at industry level by building the dataset for the Vals study.
  outcomes:
  - lever: quality
    description: An evaluation with a lawyer baseline exposed where tools trailed lawyers (redlining; EDGAR research) as well as where they led
    figure: 'Redlining: lawyer baseline 79.7% versus best tool 65.0%; EDGAR research: lawyer baseline 70.1% versus 55.2%'
    measures: Task score against predefined evaluation criteria, from a study whose dataset was created by a consortium of eight law firms
    provenance: independent
    source_ref: VALS-VLAIR-2025
  prerequisites:
  - A representative task set from the firm's own matters
  - A method for scoring (blind reviewers or rubric)
  - Time from senior reviewers
  risks_and_guardrails:
  - The ABA says lawyers can test a tool on a subset before relying on it (ABA-OP512-2024)
  - The Law Society says to assess the evidence and benchmarks providers use to support capability claims (LAWSOC-GENAI-2026)
  - California says to reassess periodically as models change (CALBAR-GENAI-2026)
  - Benchmarks that treat products as text generators miss workflow design (VALS-VLAIR-2025)
  human_checkpoints:
  - Innovation lead and practice partner approve the test set and the pass threshold
  role_evolution: Knowledge and innovation staff become evaluators with a method, not only tool administrators.
  evidence_grade: B
  sources:
  - ref: VALS-VLAIR-2025
    title: Vals Legal AI Report (VLAIR)
    publisher: Vals AI
    type: survey
    url: https://www.vals.ai/vlair
    date: '2025-02-27'
    access: full
    locator: Acknowledgments (Consortium Firms); Methodology
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.A, p. 4
  - ref: LAWSOC-GENAI-2026
    title: 'Generative AI: the essentials'
    publisher: Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials
    date: '2026'
    access: full
    locator: '''Current regulatory landscape'' section'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Duties of Competence and Diligence, p. 5
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: '''Proving AI''s path to saving clients money'''
  last_reviewed: '2026-10-19'
  notes: 'Graded B: four named firms (Reed Smith, Fisher Phillips, McDermott Will & Emery, Ogletree Deakins) plus four anonymous firms built the dataset, but no firm reports its own internal evaluation programme. At Legalweek 2026 a Ropes & Gray director described ROI measurement as based more on conventional wisdom than hard evidence, and a Zarwin Baum managing director said the industry is still in the anecdotal phase (TRI-LEGALWEEK-2026).'
- id: professional-services-work-production-15
  title: Task-level telemetry on AI-assisted work to evidence quality and savings
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: Clients want matter-level proof that AI cut cost or improved quality, and firms say they are still gathering data.
  solution: Tools log which tasks used AI, how much of the output was edited or rejected, and what review found; those logs feed quality dashboards, supervision and client reporting.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: No firm publishes acceptance, edit or rework rates for AI-assisted work
    provenance: independent
    source_ref: TRI-LEGALWEEK-2026
  prerequisites:
  - Tools that record usage and edits
  - A rule on what is logged, kept and shared with clients
  - Client confidentiality limits on logging
  risks_and_guardrails:
  - The Law Society advises documenting inputs, outputs and system errors where the tool does not keep a history (LAWSOC-GENAI-2026)
  - Telemetry can show measurement of results but not attribution to the firm's work (STANFORD-DEL-2026)
  - Logs may contain client confidential data (ABA-OP512-2024)
  human_checkpoints:
  - Supervising lawyer reviews error and override trends
  - Finance and innovation leads decide what is reported to clients
  role_evolution: Quality and innovation teams gain a measurement role; supervisors gain a data source on who relies on AI and how.
  evidence_grade: D
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: '''Proving AI''s path to saving clients money'''
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives'
    publisher: Stanford Digital Economy Lab (Brynjolfsson) and USC (Petropoulos)
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Section 1 (outcome observability and telemetry)
  - ref: LAWSOC-GENAI-2026
    title: 'Generative AI: the essentials'
    publisher: Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials
    date: '2026'
    access: full
    locator: '''Things to consider and risk management'' section'
  - ref: BLOOMBERGLAW-ACC-2025
    title: AI Does Little to Reduce Law Firm Billable Hours, Survey Shows
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/us-law-week/ai-does-little-to-reduce-law-firm-billable-hours-survey-shows
    date: '2025-10-14'
    access: full
    locator: Paragraph on clients seeing no noticeable savings
  last_reviewed: '2026-10-19'
  notes: Idea. Clients are asking for matter-level proof (TRI-LEGALWEEK-2026) and academics describe telemetry as raising outcome observability when agents are embedded in client operations (STANFORD-DEL-2026), but no source describes a firm logging edit or rework rates. The evidence on error and override rates is absent across this whole module; see Module notes.
- id: professional-services-work-production-16
  title: Matter-scoped access controls for connected and agentic AI to protect confidentiality across matters
  archetype: professional-services
  module: work-production
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - software-systems
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: Agentic and connected AI tools may have standing access to email, document stores and client files, so a badly configured tool can expose one client's information in work for another, or send data outside the firm.
  solution: Access for connected or agentic AI is limited by matter and client, monitored, and blocked from external transmission without human review. Self-learning tools are assessed for leakage between clients even inside one firm.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: No source reports measured cross-matter leakage or access-control effectiveness
    provenance: independent
    source_ref: CALBAR-GENAI-2026
  prerequisites:
  - Document and email systems with matter-level permissions
  - Configuration control over agent access
  - Vendor terms on retention and training
  risks_and_guardrails:
  - California says unrestricted or poorly configured agentic systems may unintentionally disclose confidential information across matters and that lawyers must limit and monitor access (CALBAR-GENAI-2026)
  - The ABA says self-learning tools can disclose one client's information to other matters even when used only by lawyers at one firm (ABA-OP512-2024)
  - California proposes that 'reveal' include exposing confidential information to AI tools that create a material risk of misuse (CALBAR-RULES-2026)
  human_checkpoints:
  - IT and risk approve each connected data source
  - Lawyer approves any external transmission
  role_evolution: IT and information-governance teams share supervisory responsibility for what an agent can reach.
  evidence_grade: D
  sources:
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Practical Guidance table, Duty of Confidentiality, pp. 5-6
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.B, p. 6
  - ref: CALBAR-RULES-2026
    title: Proposed Amendments to the Rules of Professional Conduct Related to Artificial Intelligence (public comment notice)
    publisher: State Bar of California
    type: regulator
    url: https://www.calbar.ca.gov/public/public-meetings-comment/public-comment/public-comment-archives/2026-public-comment/proposed-amendments-rules-professional-conduct-related-artificial-intelligence
    date: '2026-03-13'
    access: full
    locator: Amendments to rule 1.6
  - ref: ILTA-TECHSURVEY-2026
    title: '2026 ILTA Technology Survey: Executive Summary'
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: Executive summary, pp. 3-4 (Copilot licences on request; features arriving through the collaboration layer)
  last_reviewed: '2026-10-19'
  notes: Idea. The requirement is documented; no deployed matter-scoped agent configuration was found. ILTA reports that more than half of respondents issue Copilot licences only on request and that GenAI is arriving through collaboration tools without discrete deployment events, which is a partial form of gating.
```

## 3. Module notes

### Processes and key steps (work types)

- **Research and issue analysis** (`research-synthesis`): find and synthesise authority or evidence. AI-grounded research tools sit here (use case 03).
- **First-draft production** (`document-production`): memos, letters, pleadings, contracts, reports. AI produces the draft; the lawyer or consultant edits (use cases 01, 07).
- **Extraction and summarisation across document sets** (`data-reporting`, `research-synthesis`): facts, chronologies, summaries (use case 04).
- **Review against a playbook or standard** (`review-assurance`): contract review and redlining (use case 06).
- **Verification and supervisory sign-off** (`review-assurance`): citation checks, sampled validation, partner approval at gates (use cases 02, 05, 09, 13).
- **Disclosure, records and client terms** (`coordination-scheduling`, `document-production`): AI-use logs, client permission checks (use cases 08, 12).
- **Tool approval and re-validation** (`review-assurance`): policy, training, evaluation and re-testing when models change (use cases 10, 11, 14, 16).

### Common pain points

- The verification burden: output reads fluently whether or not it is right, so every citation, quotation and number needs a check (ABA-OP512-2024 Part II.A; EWHC-AYINDE-2025 para 6).
- Vendor claims are hard to test. Stanford found vendor tools described as avoiding hallucination still hallucinated 17% to 33% of the time (STANFORD-MAGESH-2024), and the largest research platforms did not take part in the Oct 2025 Vals research benchmark (LAWSITES-VALSRESEARCH-2025).
- Policy and training coverage depend on firm size: a formal policy exists at 57% of firms under 50 lawyers against 98% at 350-699, and training before access at 11% against 72% at over 700 (ILTA-TECHSURVEY-2026, Q3.18).
- Firms cannot show savings. About 60% of in-house respondents had seen "no noticeable savings yet" (BLOOMBERGLAW-ACC-2025), and firm speakers at Legalweek 2026 described their ROI evidence as anecdotal (TRI-LEGALWEEK-2026).
- Shadow use: 34% of surveyed professionals use tools their organisation has not sanctioned (TR-FOP-2026).
- Skills: AI gains in durable skill were concentrated in senior lawyers in one trial (NBER-AUTOR-2026).

### Metrics and benchmarks

| Metric | Value | What it measures | Provenance | Source |
|---|---|---|---|---|
| Hallucination rate, three legal research tools | 17% to 33% | Share of responses classed as hallucinated, 202 pre-registered queries | independent | STANFORD-MAGESH-2024 |
| Research accuracy vs lawyers | AI 79-81%; lawyers 71% | Accuracy criterion over 210 questions (tools: Alexi, Counsel Stack, Midpage, ChatGPT) | independent | LAWSITES-VALSRESEARCH-2025 |
| Document Q&A | best tool 94.8%; lawyers 70.1% | Task score vs predefined criteria | independent | VALS-VLAIR-2025 |
| Redlining | lawyers 79.7%; best tool 65.0% | Task score vs predefined criteria | independent | VALS-VLAIR-2025 |
| Patent drafting quality | +0.34 SD (10 days); +0.38 SD (90 days) | Blind expert score, 133 lawyers, 11 firms | vendor-published (run by Google) | NBER-AUTOR-2026 |
| Consulting tasks inside AI frontier | +12.2% tasks; 25.1% faster | 758 BCG consultants, 18 tasks | independent | HBS-DELLACQUA-2023 |
| Consulting task outside frontier | 19% less likely correct | One complex managerial task | independent | HBS-DELLACQUA-2023 |
| Fabricated citations in a student trial | Vincent AI 3; no AI 4; o1-preview 11 | Citations to entirely fabricated sources across all assignments | independent | SCHWARCZ-APL-2025 |
| Court decisions on hallucinated content | 2,202 (read 2026-10-19) | Decisions where a court found or implied reliance on hallucinated material | independent | CHARLOTIN-HALLUCINATIONS-2026 |
| GenAI engagement by firms | 94% | Share of 508 surveyed firms engaged with GenAI (up 14 points) | independent | ILTA-TECHSURVEY-2026 |
| Professionals using AI several times a week | 74% | Share of 1,816 surveyed professionals | vendor-published | TR-FOP-2026 |
| Clients seeing AI quality gains from most providers | 6% (78% say it is very important or essential) | Corporate clients surveyed by Thomson Reuters | vendor-published | TR-FOP-2026 |
| Cross-occupation expert comparison | Best model rated as good as or better than experts in just under half of tasks | 220 gold-set tasks, blind expert grading, 44 occupations (not professional-services specific) | vendor-published | OPENAI-GDPVAL-2025 |

### Guardrails and regulatory points

- **ABA Formal Opinion 512 (2024-07-29).** Independent verification is required in proportion to the tool and task; a lawyer may sample-test a tool before relying on it; hourly bills must reflect time actually spent; managers must set policy and train; AI material may be marked in files (ABA-OP512-2024).
- **State Bar of California (board-approved 2026-05-14).** Extends the 2023 guidance to agentic AI at the California Supreme Court's request: oversight must rise with autonomy, agents must not file or send client data externally without lawyer review, hourly billing must reflect time spent, and client AI restrictions must be followed (CALBAR-GENAI-2026). Proposed rule amendments (1.1, 1.4, 1.6, 3.3, 5.1, 5.3) were out for comment to 2026-05-04 (CALBAR-RULES-2026).
- **England and Wales.** The Divisional Court (2025-06-06) held that AI users must check research against authoritative sources and said leaders will be asked whether practical measures were taken (EWHC-AYINDE-2025). The Law Society page lists court sanctions that may follow, referring to an April 2026 judgment (LAWSOC-GENAI-2026). The SRA's warning notice is known only through a press report (LAWSOCIE-SRAWARN-2026).
- **Ireland.** High Court Practice Direction HC 142 (effective 2026-09-01) requires independent verification of AI-generated material and warns of cost and referral consequences (LAWSOCIE-HC142-2026).
- **Management consulting.** The ICMCI code makes AI misuse a breach comparable to other misconduct, requires disclosure where AI materially affects advice, and bars submitting unreviewed AI output as finished work (ICMCI-AICODE-2026). The MCA's 2026 survey page offers no AI guidance that was readable (MCA-SURVEY-2026).
- **Tax.** The IRS Office of Professional Responsibility (2026-06-24) maps Circular 230 duties onto AI use, including due diligence, fees and written advice (IRS-OPR-2026). The AICPA tax-section summary was gated (AICPA-TAXAI-2026).
- **EU.** AI literacy obligations have applied since 2025-02-02; the AI Act became applicable on 2026-08-02 with exceptions, and Annex III high-risk rules are extended to 2027-12-02 (EC-AIACT-2026).
- **Client terms.** Canada's procurement agency requires suppliers to identify AI use in advance (BNN-DELOITTE-2025). Client guidelines mix "use AI", "do not use AI without permission" and "will not pay for AI-done work" (TRI-LEGALWEEK-2026).

### Frontier signals (dated)

- **2026-10-15:** Harvey launches Legal Work Orchestration, with agents executing tasks and lawyers reviewing at designated gates; it says it expects agents to take 20% more workflow steps in six months (HARVEY-ORCH-2026).
- **2026-11-11 (scheduled):** Thomson Reuters Institute webinar on moving from "human in the loop" to being "in control" (TRI-EVENTS-2026). Signal only.
- **2026-09:** NBER working paper on AI and expertise in patent drafting (NBER-AUTOR-2026).
- **2026-08:** SRA warning notice on AI misuse, reported after 42 reports in 12 months (LAWSOCIE-SRAWARN-2026).
- **2026-07:** Irish High Court practice direction on AI in court documents (LAWSOCIE-HC142-2026).
- **2026-06-24:** IRS OPR AI guidance (IRS-OPR-2026). **2026-06-04:** ICMCI code launched (ICMCI-NEWS-2026). **2026-06-03:** LegalOn vendor benchmark (LEGALON-BENCH-2026).
- **2026-05-14:** California Board approves agentic-AI guidance (CALBAR-GENAI-2026).
- **2025-10-31:** England and Wales judiciary issues updated AI guidance for judicial office holders, expanding its text on hallucination and confidentiality risks (JUDICIARY-AIGUIDE-2025). **2025-10-23:** Vals research benchmark finds AI matching or beating lawyers on research accuracy (LAWSITES-VALSRESEARCH-2025). **2025-10-07:** Deloitte Australia reported to be partly refunding a government department (CTV-DELOITTE-2025). **2025-12-18:** Canada's procurement agency reported to require suppliers to identify AI use in advance (BNN-DELOITTE-2025).

### Workforce and role effects

- Seniors kept the skill benefit and juniors' outcomes diverged in the NBER trial (NBER-AUTOR-2026). In the Thomson Reuters survey, 48% feared harm to independent judgment development, and legal professionals expected the time to trusted judgment to stretch by 1.7 years while tax professionals expected it to shorten by 1.0 (TR-FOP-2026).
- ILTA respondents expect added headcount in IT, innovation, security, training, knowledge management and data science (ILTA-TECHSURVEY-2026).
- Leaders take on documented accountability: the English court will ask about it (EWHC-AYINDE-2025) and California proposes a rule duty to set AI policies (CALBAR-RULES-2026).
- Subordinate lawyers cannot defer to a supervisor's instruction to use AI in ways that breach their own duties (CALBAR-GENAI-2026, p. 7).

### Objections and concerns practitioners raise

- "Until accuracy and quality improve, it is an expensive toy" (ILTA respondent, ILTA-TECHSURVEY-2026, p. 3) and "this hype, too, shall pass" (p. 4).
- Vendor benchmarks should not be taken at face value, as the LegalOn CEO himself says (ARTLAW-LEGALON-2026).
- Clients want AI used and the savings shown, while also saying they will not pay for AI-done work (TRI-LEGALWEEK-2026).
- General AI is "not sufficient for fiduciary-grade work", in the view of Thomson Reuters' CEO, who sells the alternative (TR-FOP-2026, foreword).
- Responsibility: 47% of surveyed professionals say final responsibility for an AI-assisted error lies with the individual professional (TR-FOP-2026).

### Interview probes for an advisor

1. When AI drafts or summarises, what exactly is checked before it leaves the team, by whom, and is that recorded anywhere? Ask for the last error that was caught.
2. Does the team measure AI-assisted work (edit rates, errors caught in review, rework) or rely on impressions? What would they need to log?
3. How do client terms on AI reach the people doing the work, and what happens when two clients' terms conflict?
4. Which tasks have you decided stay human-first, and what evidence led to that? How often do you re-test when the tool changes?
5. Who is accountable for AI use at partner or director level, and how do juniors still get unaided practice on the work AI now drafts?


## 4. Routed to other modules

- **billing-collections:** hourly billing must reflect time actually spent, and AI costs are overhead unless matter-specific and disclosed without markup (ABA-OP512-2024 Part II.F; CALBAR-GENAI-2026 p. 8); IRS OPR says billing for unspent manual time may breach the fee rule (IRS-OPR-2026 item 2); clients want line-item AI transparency and savings shown on invoices (TRI-LEGALWEEK-2026).
- **scoping-pricing / firm-finance:** pricing models and observability of AI-reduced effort (STANFORD-DEL-2026); about 60% of in-house respondents saw no savings (BLOOMBERGLAW-ACC-2025); flat fees may build in AI savings (CALBAR-GENAI-2026 p. 8).
- **talent-learning:** junior skill effects (NBER-AUTOR-2026); 48% fear harm to judgment development (TR-FOP-2026); the Choi, Monahan and Schwarcz recommendation to limit first-year law students' AI use (LEGALFUTURES-CHOI-2023); assessment-integrity rules in the ICMCI code, sections 5.2 and 6 (ICMCI-AICODE-2026).
- **acceptance-risk:** confidentiality, client consent and conflicts exposure from connected tools (ABA-OP512-2024 Part II.B; CALBAR-GENAI-2026 pp. 5-6); employment-related AI screening and bias (CALBAR-GENAI-2026 p. 9).
- **staffing-resourcing:** EU AI Act high-risk employment rules extended to 2027-12-02 (EC-AIACT-2026).
- **delivery-management:** matter templates, task assignment and reviewers in Harvey Legal Work Orchestration (HARVEY-ORCH-2026).
- **quality-review:** overlaps strongly with this note's use cases 02, 05 and 14; the deeper review-gate design belongs there.
- **Tax archetype:** Circular 230 duties and AICPA tax-section material (IRS-OPR-2026; AICPA-TAXAI-2026) are tax-technical.
- **Assurance archetype:** the Financial Reporting Council's audit-quality findings on AI monitoring (a landscape lead, not read here), PCAOB and IAASB material.


## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access | Note |
|---|---|---|---|---|---|---|---|
| ABA-OP512-2024 | Formal Opinion 512: Generative Artificial Intelligence Tools | American Bar Association, Standing Committee on Ethics and Professional Responsibility | professional-body | https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf | 2024-07-29 | full | americanbar.org returned 403; the full 15-page text was read from a copy at https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision) | State Bar of California, Standing Committee on Professional Responsibility and Conduct | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05-14 | full | The PDF carries no date. 14 May 2026 is the Board of Trustees approval date stated on the State Bar's Ethics & Technology Resources page (https://www.calbar.ca.gov/Attorneys/Conduct-Discipline/Ethics/Ethics-Technology-Resources), which also gives 16 Nov 2023 as the original publication date |
| CALBAR-RULES-2026 | Proposed Amendments to the Rules of Professional Conduct Related to Artificial Intelligence (public comment notice) | State Bar of California | regulator | https://www.calbar.ca.gov/public/public-meetings-comment/public-comment/public-comment-archives/2026-public-comment/proposed-amendments-rules-professional-conduct-related-artificial-intelligence | 2026-03-13 | full | Date is the COPRAC meeting that approved the proposal for a 45-day comment period; comment deadline 4 May 2026. The notice itself is undated |
| LAWSOC-GENAI-2026 | Generative AI: the essentials | Law Society of England and Wales | professional-body | https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials | 2026 | full | Page is undated; it discusses an April 2026 judgment and links a September 2025 checklist, so it was updated in or after spring 2026 |
| EWHC-AYINDE-2025 | R (Ayinde) v London Borough of Haringey; Al-Haroun v Qatar National Bank [2025] EWHC 1383 (Admin) | High Court of Justice, King's Bench Division (Divisional Court) | regulator | https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf | 2025-06-06 | full | A court judgment; typed 'regulator' because the vocabulary has no court type |
| LAWSOCIE-SRAWARN-2026 | SRA issues warning notice on use of AI | Law Society of Ireland Gazette | press | https://www.lawsociety.ie/gazette/top-stories/2026/august/sra-issues-warning-notice-on-use-of-ai/ | 2026-08 | full | Secondary report of the SRA's 'Misuse of AI' warning notice. The SRA's own page (https://www.sra.org.uk/solicitors/guidance/misuse-ai/) was blocked by a bot challenge. Day of month not shown on the page |
| LAWSOCIE-HC142-2026 | High Court expects 'human supervision' of GenAI | Law Society of Ireland Gazette | press | https://www.lawsociety.ie/gazette/top-stories/2026/july/high-court-expects-human-supervision-of-genai/ | 2026-07 | full | Reports Irish High Court Practice Direction HC 142, effective 1 September 2026. The practice direction itself was not opened. Day of month not shown |
| JUDICIARY-AIGUIDE-2025 | Artificial Intelligence (AI) Judicial Guidance (October 2025) | Courts and Tribunals Judiciary (England and Wales) | regulator | https://www.judiciary.uk/guidance-and-resources/artificial-intelligence-ai-judicial-guidance/ | 2025-10-31 | full | Only the announcement page was read, not the guidance PDF |
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert, Issue 2026-19) | Internal Revenue Service, Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full | |
| AICPA-TAXAI-2026 | AICPA insights: Introductory guidelines for responsible AI use in federal tax practice | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/resources/article/aicpa-insights-introductory-guidelines-for-responsible-ai-use-in-federal-tax-practice | 2026-07-02 | search-only | Page body is reserved for Tax Section members; only the opening summary was visible |
| ICMCI-AICODE-2026 | Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version 1.0 | International Council of Management Consulting Institutes (ICMCI) | professional-body | https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf | 2026-05 | full | Document states it was adopted by the ICMCI Board in May 2026 |
| ICMCI-NEWS-2026 | ICMCI Launches Global Code for the Responsible Use of AI in Management Consulting | ICMCI | professional-body | https://www.cmc-global.org/content/icmci-launches-global-code-responsible-use-ai-management-consulting | 2026-06-04 | full | |
| EC-AIACT-2026 | AI Act: regulatory framework for AI | European Commission, Digital Strategy | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-19 | full | Living page; 2026-10-19 is the date it was read |
| MCA-SURVEY-2026 | MCA Member Survey 2026 | Management Consultancies Association | professional-body | https://www.mca.org.uk/reports/mca-member-survey-2026 | 2026 | full | Page undated; the AI-benefit chart is an image and its figures were not readable |
| ILTA-TECHSURVEY-2026 | 2026 ILTA Technology Survey: Executive Summary | International Legal Technology Association | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 | full | Month taken from the file name (2606); the full survey is members-only |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 | full | Vendor-published survey (Thomson Reuters sells the AI tools it discusses). Fieldwork March-April 2026; the page shows no publication date |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full | |
| TRI-EVENTS-2026 | Thomson Reuters Institute events listing | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/events | 2026-10-19 | full | Listing read on 2026-10-19; event abstracts only |
| BLOOMBERGLAW-ACC-2025 | AI Does Little to Reduce Law Firm Billable Hours, Survey Shows | Bloomberg Law | press | https://news.bloomberglaw.com/us-law-week/ai-does-little-to-reduce-law-firm-billable-hours-survey-shows | 2025-10-14 | full | Reports the ACC-Everlaw survey of in-house counsel and legal operations staff; the ACC survey page itself returned 403 |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER Working Paper 35720) | National Bureau of Economic Research (Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere) | academic | https://www.nber.org/papers/w35720 | 2026-09 | full | Abstract and disclosure page read; the PDF returned 403. Issue date September 2026, revised October 2026 |
| STANFORD-MAGESH-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362) | Stanford University and Yale University (Magesh, Surani, Dahl, Suzgun, Manning, Ho) | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 | full | Read the v1 PDF dated 3 June 2024 (updated to add Westlaw). Older than the 18-month window; kept as the main independent hallucination measurement |
| VALS-VLAIR-2025 | Vals Legal AI Report (VLAIR) | Vals AI | survey | https://www.vals.ai/vlair | 2025-02-27 | full | Industry benchmark, not peer reviewed. Vals discloses a customer relationship with at least one participant |
| LAWSITES-VALSRESEARCH-2025 | Vals AI's Latest Benchmark Finds Legal and General AI Now Outperform Lawyers in Legal Research Accuracy | LawSites (Bob Ambrogi) | press | https://www.lawnext.com/2025/10/vals-ais-latest-benchmark-finds-legal-and-general-ai-now-outperform-lawyers-in-legal-research-accuracy.html | 2025-10-23 | full | Press report of the Vals VLAIR Legal Research study; the Vals report page itself could not be opened |
| SCHWARCZ-APL-2025 | AI-Powered Lawyering: AI Reasoning Models, Retrieval Augmented Generation, and the Future of Legal Practice | University of Minnesota and University of Michigan law schools (Schwarcz, Manning, Barry, Cleveland, Prescott, Rich) | academic | https://www.law.berkeley.edu/wp-content/uploads/archive/2025/12/AI-Powered-Lawyering.pdf | 2025 | full | Working-paper PDF; exact posting date not shown in the PDF |
| LEGALFUTURES-CHOI-2023 | AI helps lawyers complete work quicker, study finds | Legal Futures | press | https://www.legalfutures.co.uk/latest-news/ai-helps-lawyers-complete-work-quicker-study-finds | 2023-11-13 | full | Press report of Choi, Monahan and Schwarcz, 'Lawyering in the Age of Artificial Intelligence'; the paper itself (SSRN) was not opened |
| HBS-DELLACQUA-2023 | Navigating the Jagged Technological Frontier (HBS Working Paper 24-013) | Harvard Business School with Boston Consulting Group (Dell'Acqua, McFowland, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon, Lakhani) | academic | https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 | 2023-09 | full | Abstract page read; PDF returned 403. Working paper dated September 2023, forthcoming in Organization Science. Outside the 18-month window; foundational |
| STANFORD-DEL-2026 | Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives | Stanford Digital Economy Lab (Brynjolfsson) and USC (Petropoulos) | academic | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | 2026-08-23 | full | The paper discloses a general gift to the Lab from Accenture, not tied to the study |
| CHARLOTIN-HALLUCINATIONS-2026 | AI Hallucination Cases Database | Damien Charlotin | community | https://www.damiencharlotin.com/hallucinations/ | 2026-10-19 | full | Living database; count read on 2026-10-19 |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors (AP) | CTV News / Associated Press | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 | full | |
| BNN-DELOITTE-2025 | Feds defend $1.1-million Deloitte contract for AI advice after firm admitted mistakes (Canadian Press) | BNN Bloomberg / The Canadian Press | press | https://www.bnnbloomberg.ca/business/company-news/2025/12/18/feds-defend-11-million-deloitte-contract-for-ai-advice-after-firm-admitted-mistakes/ | 2025-12-18 | full | |
| OPENAI-GDPVAL-2025 | GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks (arXiv 2510.04374) and OpenAI announcement | OpenAI | vendor | https://arxiv.org/abs/2510.04374 | 2025-10-05 | full | Date is the arXiv submission date; the OpenAI announcement page (https://openai.com/index/gdpval/) shows no date. Cross-occupation benchmark, not specific to professional services |
| IVO-BENCH-2026 | Ivo Outperforms Claude for Word in Independent Contract Review Benchmark (press release) | Ivo | vendor | https://www.ivo.ai/news/ivo-outperforms-claude-for-word-in-independent-contract-review-benchmark | 2026 | full | Study conducted April 2026 per the release; release date not shown on the page |
| LEGALON-BENCH-2026 | LegalOn 2026 Contract Review Benchmark | LegalOn | vendor | https://www.legalontech.com/post/the-contract-review-benchmark-2026 | 2026-06-03 | full | Page states 'Last updated: June 3, 2026' |
| ARTLAW-LEGALON-2026 | What Legal AI Benchmarks Reveal That Model Names Don't (by Daniel Lewis, CEO, LegalOn) | Artificial Lawyer | press | https://artificiallawyer.com/2026/06/22/what-legal-ai-benchmarks-reveal-that-model-names-dont | 2026-06-22 | full | Guest article by the vendor's CEO |
| HARVEY-ORCH-2026 | Making Harvey the Orchestration Layer for Legal Work | Harvey | vendor | https://www.harvey.ai/blog/legal-work-orchestration | 2026-10-15 | full | |

## 6. Gaps

- **Quality evidence from deployers is absent.** No firm, in-house team or consultancy publishes error rates, override rates, parallel-run results or inspection findings for AI-assisted drafting, research or review. Everything measured is a test of a tool or a trial of a few hundred people. No regulator inspection outcome on AI in non-audit work was found.
- **Blocked or gated:** SRA pages (bot challenge; only a press report of the warning notice was read), AICPA tax-section article (gated), ACC-Everlaw survey (403), NBER 35720 and HBS 24-013 PDFs (403; abstracts only), Vals Legal Research report page (connection reset; read via LawSites), americanbar.org (403; a LawNext-hosted copy was read), FRC AI-audit statements (guessed URLs returned 404).
- **Not found:** any MCA guidance on AI use (only its survey page); AICPA primary AI guidance beyond the tax summary; state bar opinions from Florida, New York, Texas, Pennsylvania and DC were not read directly (only as cited in ABA Opinion 512); a Judicial Conference or US federal court rule on AI in filings; professional indemnity insurers' AI terms; the Australian government's contract-clause text.
- **Web search budget:** 11 searches succeeded before the shared budget ran out; planned searches on the FRC, large-firm sanctions responses and the proposed federal evidence rule were not run.
- **Unverified leads (search snippets only, not used as evidence):** a blog summary of a Thomson Reuters report saying about two-thirds of corporate respondents think outside firms should use AI and under 20% require it; a Vals Finance Agent benchmark shown only by aggregators; a Vals "February 2026" legal report named in one blog (the Vals page read was dated 2025-02-27).
- **Dates not established:** Law Society guidance page, TR Future of Professionals publication date, Ivo release date, Schwarcz et al. posting date, and the day of the month for two Law Society of Ireland Gazette reports.
- **Counts that differ across sources:** the Vals research benchmark question count (210 in LawSites; 200 in a search summary); the Schwarcz sample (127 in the paper; a search summary said 137). The paper and LawSites were used.
- **Not covered:** consulting-firm primary documents (Deloitte, McKinsey, BCG), in-house legal operations beyond the ACC survey and Legalweek panel, and any evidence on engineering, architecture or project-management work production.


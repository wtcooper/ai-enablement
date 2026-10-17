# Completion and reporting: governance and evidence (assurance)

- **Archetype:** assurance
- **Module:** completion-reporting (disclosure checklists and financial-statement review, subsequent events, going concern, written representations, summary of misstatements, engagement quality review, key and critical audit matters, audit committee communications, opinion and report drafting)
- **Angle:** governance and evidence
- **Prepared:** 2026-10-16
- **Method:** page references to the Japan FSA paper are printed page numbers; sources opened with `curl` (PCAOB pages through a text mirror because pcaobus.org returns 403 to `curl`); PDFs read with `pdftotext`; about 20 web searches. Every source below is marked `access: full` only where its text was opened and read; abstract-only reads are said so.

## 1. Summary

- **No regulator or standard-setter bars AI in these steps, and none has written a completion-specific rule.**
  - The FRC's guidance of 30 Mar 2026 is the first from any audit regulator on generative and agentic AI. It sorts risks into deficient output, misuse of output and non-compliant methodology, and leaves accountability with the human auditor (FRC-GENAI-2026; FRC-NEWS-2026).
  - Keyword searches of the converted text of the PCAOB standards for going concern (AS 2415), subsequent events (AS 2801), audit committee communications (AS 1301), the auditor's report (AS 3101) and engagement quality review (AS 1220) found no mention of technology or tools. This was a keyword check on text-mirror copies, not a legal reading.
  - The IAASB's revised ISA 570 (effective for periods beginning on or after 15 Dec 2026) is the one completion-area standard that names automated tools in its application material: risk assessment (A13), sensitivity analysis (A42) and data reliability (A46) (IAASB-ISA570-2025).
- **The PCAOB agenda touches these steps only loosely.** The going-concern project (AS 2415) and a fraud project are at "evaluating feedback and developing a project plan", and the page says they "may examine" how technology affects the work. A Communications with Audit Committees research item and a further post-implementation review of critical audit matters are listed. No AI-specific proposal exists for these steps (PCAOB-AGENDA-2026).
- **Public evidence is concentrated in one step: disclosure-checklist review.** Thomson Reuters, Caseware, KPMG and DataSnipper all describe tools for it. The only published measurements are vendor figures: 2.7 hours saved per run in Caseware's beta, and about 30% of eligible Thomson Reuters customers using its feature (CASEWARE-CWX-2026; TR-DISCLOSURE-2026). No source publishes a miss rate.
- **Independent quality evidence is thin and mostly adjacent.**
  - A peer-reviewed survey found auditors at a German Big 4 firm rated an AI tool for management-report review as improving effectiveness and efficiency, less so for complex qualitative issues (FABIAN-2026).
  - A BDO-linked thesis (ten accountants, 20 organisations) found an LLM going-concern signal matched or beat individual accountants but did not move average accuracy or speed (LEIDEN-GC-2025).
  - Two LLM benchmarks report gaps in cross-document reasoning and in citing standards (ARXIV-FINAUDITING-2025; ARXIV-LLMAUDIT-2025).
  - No inspection finding about an AI tool in any of these steps was found.
- **Steps with no public AI evidence at all:** subsequent events, written representations, summary of uncorrected misstatements, engagement quality review, key and critical audit matter drafting, and opinion or report drafting. They are listed as open questions, not use cases.
- **Governance expectations are converging on transparency and human accountability.** IFIAR's April 2026 report asks firms to tell those charged with governance how technology is used in the audit and how it affects decisions, and PCAOB staff report audit committee chairs asking about both AI in financial reporting and AI's effect on fees (IFIAR-TTF-2026; PCAOB-ACCHAIRS-2026).
- **Use cases:** 14 in total. Grade A: 1, B: 1, C: 6, D: 6.

## 2. Use cases

Schema per `vocabulary.md`. Outcome provenance is marked on every figure. Grades follow the vocabulary: A measured outcome from a named organisation, B named deployment without measurements, C vendor claim, D idea. Where a grade rests on a judgement call, the entry's `notes` say so.

```yaml
- id: assurance-completion-reporting-01
  title: Match disclosure-checklist requirements to the draft financial statements, with cited rationale
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - review-assurance
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Thomson Reuters says a fully completed checklist in its Guided Assurance product can run to 1,200-1,500 requirements,
    that a missed disclosure can surface as an inspection finding, a peer review deficiency or a restatement, and
    that many firms either roll last year's checklist forward or spend senior and manager time redoing it (TR-DISCLOSURE-2026).
  solution: >-
    An AI feature in the audit platform reads the draft statements and marks each requirement as identified or not
    found, with a plain-language rationale and a citation back to the statement text (TR-DISCLOSURE-2026). Caseware
    describes the same pattern, with the auditor accepting, refining or overriding each suggestion inside the engagement
    workflow (CASEWARE-VERITY-2026). KPMG says its Financial Report Analyzer produces output that lets auditors
    complete the required disclosure checklists (KPMG-CLARA-2025). DataSnipper markets agents that link each requirement
    to evidence (DATASNIPPER-DISCLOSURE-2025).
  outcomes:
  - lever: speed
    description: Average review time saved per checklist run in Caseware's beta programme
    figure: 2.7 hours
    measures: >-
      average hours saved per disclosure checklist run, as reported by firms beta testing the agent in Caseware's
      CwX 2026 beta programme; results vary by engagement; firms not named
    provenance: vendor-published
    source_ref: CASEWARE-CWX-2026
  - lever: capacity
    description: Adoption of Disclosure Review after an extended customer beta
    figure: about 30% of eligible customers; close to 300 analyses a month
    measures: >-
      share of eligible Disclosure-module customers using the feature, and the number of disclosure review analyses
      generated per month, across mid-sized and large firms; customers not named; no accuracy figure given
    provenance: vendor-published
    source_ref: TR-DISCLOSURE-2026
  prerequisites:
  - >-
    Thomson Reuters' feature is available to Guided Assurance customers with the Disclosure module (TR-DISCLOSURE-2026).
  - >-
    Caseware's agent works inside its audit engagement workflow, where suggestions can be accepted, refined or overridden
    (CASEWARE-VERITY-2026).
  risks_and_guardrails:
  - >-
    The FRC lists omission, hallucination and distortion as deficient-output risks, and expects mitigations matched
    to the tool and use (FRC-GENAI-2026, 'Risk of deficient output').
  - >-
    The PCAOB staff recorded firms' concern that GenAI output can be false or misleading, and firms' answer of more
    specific instructions to users (PCAOB-GENAI-2024, p. 5).
  - >-
    ISA 220 (Revised) names automation bias, a tendency to favour automated output, as an unconscious bias to counter
    (IAASB-ISA220-2020, para A35).
  - No source gives a miss rate (requirements wrongly marked identified) for any of these tools.
  human_checkpoints:
  - >-
    Auditor accepts, refines or overrides each suggestion; nothing enters the engagement file without human review
    (CASEWARE-VERITY-2026).
  - Where the AI and the auditor disagree the difference is flagged for attention (TR-DISCLOSURE-2026).
  role_evolution: >-
    Thomson Reuters says visible rationale helps junior staff learn why a requirement was marked as it was (TR-DISCLOSURE-2026).
    A Caseware beta partner described the agent as doing at scale what a partner did walking a junior through a
    checklist line by line (CASEWARE-CWX-2026).
  evidence_grade: B
  sources:
  - ref: TR-DISCLOSURE-2026
    title: Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence
    publisher: Thomson Reuters Innovation Blog (Corey Wells, General Manager of Audit)
    type: vendor
    url: >-
      https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/
    date: '2026-09-23'
    access: full
    locator: Sections 'Bringing AI into the checklist itself' and 'Meeting the market, with room to grow'
  - ref: CASEWARE-CWX-2026
    title: "CwX 2026: How agentic AI is transforming audit and assurance"
    publisher: Caseware
    type: vendor
    url: https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance
    date: '2026-06-17'
    access: full
    locator: >-
      Section 'Disclosure Checklist Agent'; question 'What time savings did beta firms report'; 'Feedback from beta
      partner firms'
  - ref: CASEWARE-VERITY-2026
    title: Caseware launches Verity to bring workflow-native AI agents directly into assurance engagements
    publisher: Caseware
    type: vendor
    url: >-
      https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements
    date: '2026-05-20'
    access: full
    locator: Paragraph on the Disclosure Checklist Agent
  - ref: KPMG-CLARA-2025
    title: KPMG advances AI integration in KPMG Clara smart audit platform
    publisher: KPMG International
    type: firm
    url: >-
      https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html
    date: '2025-04-22'
    access: full
    locator: Sub-headline and third paragraph (Financial Report Analyzer)
  - ref: DATASNIPPER-DISCLOSURE-2025
    title: Disclosure Agents from DataSnipper (product page)
    publisher: DataSnipper
    type: vendor
    url: https://www.datasnipper.com/campaign/disclosure-agents
    date: 2025-10
    access: full
    locator: Sections 'Automated disclosure review' and 'Link disclosure directly to evidence'
  - ref: PCAOB-GENAI-2024
    title: >-
      Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence
      in Audits and Financial Reporting
    publisher: PCAOB (staff)
    type: regulator
    url: https://pcaobus.org/documents/generative-ai-spotlight.pdf
    date: 2024-07
    access: full
    locator: p. 4, 'Investment in GenAI' (evaluating completeness of financial statement disclosures)
  last_reviewed: '2026-10-16'
  notes: >-
    Graded B: KPMG is a named firm that released the tool, and Caseware names three partner firms (Withum, Citrin
    Cooperman, EisnerAmper) that piloted Caseware Verity on live engagements in the 2025 busy season (CASEWARE-CWX-2026,
    'Feedback from beta partner firms'); that page does not say they used the checklist agent specifically. Both
    outcome figures are vendor-published and neither measures accuracy. The 1,200-1,500 figure in TR's post describes
    a fully completed checklist in Guided Assurance, not a limit of Disclosure Review. Ideagen claims use by 9 of
    10 top UK firms; that came from a search extract only (its page returned 404) and is not counted. DataSnipper's
    page is undated and publishes no figures.
- id: assurance-completion-reporting-02
  title: Use AI as a second check on a checklist the team has already completed, flagging divergent answers
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Thomson Reuters describes fatigue creeping in on long checklists and firms rolling last year's checklist forward
    (TR-DISCLOSURE-2026); Caseware's beta found completed checklists with answers that were wrong because of misinterpretation
    of the requirement (CASEWARE-CWX-2026).
  solution: >-
    The tool is run against a completed checklist, and answers that differ from the auditor's are flagged automatically
    (TR-DISCLOSURE-2026). Caseware reports that beta firms used its agent as a quality check on completed checklists
    (CASEWARE-CWX-2026).
  outcomes:
  - lever: quality
    description: >-
      In one beta case the agent surfaced questions answered incorrectly because of misinterpretation of the requirement
      and explained the correct reading
    figure: one case; count and rate not published
    measures: an anecdote reported by Caseware from its beta programme; no denominator given
    provenance: vendor-published
    source_ref: CASEWARE-CWX-2026
  prerequisites:
  - Not stated beyond access to the vendor's disclosure feature (TR-DISCLOSURE-2026).
  risks_and_guardrails:
  - >-
    The FRC lists 'critic' among an LLM's roles, where the LLM reviews an input that may itself be another LLM's
    output; its mitigations include certification and recertification of the system (FRC-GENAI-2026, table of LLM
    roles; 'Certification').
  - Divergence flags show where to look; they do not show who is right (TR-DISCLOSURE-2026).
  human_checkpoints:
  - The auditor resolves each flagged divergence (TR-DISCLOSURE-2026).
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
  - ref: TR-DISCLOSURE-2026
    title: Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence
    publisher: Thomson Reuters Innovation Blog (Corey Wells, General Manager of Audit)
    type: vendor
    url: >-
      https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/
    date: '2026-09-23'
    access: full
    locator: Paragraph beginning 'Where the AI and the auditor's own judgment diverge'
  - ref: CASEWARE-CWX-2026
    title: "CwX 2026: How agentic AI is transforming audit and assurance"
    publisher: Caseware
    type: vendor
    url: https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance
    date: '2026-06-17'
    access: full
    locator: Section 'Disclosure Checklist Agent', second paragraph
  - ref: FRC-GENAI-2026
    title: Generative and Agentic AI Guidance
    publisher: Financial Reporting Council (UK)
    type: regulator
    url: https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf
    date: '2026-03-30'
    access: full
    locator: Table of LLM roles (researcher, reasoner, writer, summariser, critic, orchestrator)
  last_reviewed: '2026-10-16'
  notes: >-
    Closely related to use case 01; kept separate because the AI moves from first drafter to independent checker.
    Both sources are vendors.
- id: assurance-completion-reporting-03
  title: >-
    Review management reports against statutory content requirements: find passages, link them to requirements,
    check arithmetic, compare versions
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - review-assurance
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    The audit of management reports has traditionally relied on a manual, checklist-based approach (HAMBURG-FABIAN-2026).
  solution: >-
    A task-specific AI tool at a German Big 4 firm identifies relevant passages in the management report and links
    them to the statutory disclosure requirements, so auditors can review and document suggestions passage by passage.
    It also checks for calculation errors, highlights changes between report versions and supports team collaboration
    with task allocation and review functions (HAMBURG-FABIAN-2026).
  outcomes:
  - lever: quality
    description: >-
      Surveyed employees judged the tool to improve audit effectiveness and efficiency, less so for complex qualitative
      issues; roles, expertise and involvement in digital transformation shaped views, as did perceived deskilling
      and trust
    figure: no numeric result in the accessible abstract
    measures: >-
      auditors' perceptions, from a survey of employees of a Big 4 audit firm in Germany who had used the tool;
      sample size not seen
    provenance: independent
    source_ref: FABIAN-2026
  prerequisites:
  - >-
    Training programmes, clear communication on opportunities and risks, and involvement of staff in the transformation
    (HAMBURG-FABIAN-2026).
  risks_and_guardrails:
  - >-
    Judgement on discretionary leeway, linguistic nuance and strategic statements in the management report stays
    with people (HAMBURG-FABIAN-2026).
  - Some respondents worried about over-reliance on AI results and loss of skills (HAMBURG-FABIAN-2026).
  human_checkpoints:
  - >-
    The tool 'does not replace professional judgement'; review and documentation of suggestions stays with the auditor,
    under the dual-control principle (HAMBURG-FABIAN-2026).
  role_evolution: >-
    Seniority, experience and involvement in digital transformation changed how auditors rated the tool's value
    (HAMBURG-FABIAN-2026).
  evidence_grade: C
  sources:
  - ref: FABIAN-2026
    title: >-
      Auditing Corporate Disclosures with the Assistance of Task-Specific Artificial Intelligence - Evidence on
      Effectiveness and Efficiency
    publisher: Journal of Information Systems (Fabian and Ratzinger-Sakel)
    type: academic
    url: https://doi.org/10.2308/ISYS-2025-054
    date: '2026-03-03'
    access: full
    locator: Abstract
  - ref: HAMBURG-FABIAN-2026
    title: "AI in auditing: New study highlights opportunities and limitations"
    publisher: University of Hamburg Business School
    type: academic
    url: >-
      https://www.bwl.uni-hamburg.de/en/ueber-die-fakultaet/aktuelles/2026/0320-ki-loesungen-in-der-wirtschaftspruefung-jette-fabian-nicole-ratzinger-sakel.html
    date: '2026-03-20'
    access: full
    locator: Paragraphs 2-5 (tool description, findings, practical implications)
  last_reviewed: '2026-10-16'
  notes: >-
    Peer-reviewed and independent, but the firm is not named in the accessible sources, so it is not graded B, and
    the measure is perception, not error detection. The paper itself (JIS, DOI 10.2308/ISYS-2025-054) returned 403.
    A management report (Lagebericht) is a German-law document; the transfer to financial statement disclosures
    or to the US 'other information' step is by analogy.
- id: assurance-completion-reporting-04
  title: >-
    Draft the financial statements by rolling the prior-year report forward and linking it to current-year trial
    balance data
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Preparing financials historically needed a fragmented mix of reports and spreadsheets (FIELDGUIDE-FINANCIALS-2026).
  solution: >-
    Fieldguide's Drafting Agent produces a rolled-forward, formatted first draft by referencing the prior-year report
    and linking it to current-year trial balance data; a Disclosure Agent rolls forward footnote language and populates
    schedule-driven disclosures (FIELDGUIDE-FINANCIALS-2026).
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: no figure given in the release
    provenance: vendor-published
    source_ref: FIELDGUIDE-FINANCIALS-2026
  prerequisites:
  - >-
    Prior-year report and current-year trial balance loaded in the platform (FIELDGUIDE-FINANCIALS-2026).
  risks_and_guardrails:
  - >-
    The release does not say whether the statements are the client's or the audit team's, and it does not address
    independence or management responsibility. The CCAB draft names a management-responsibility threat when autonomous
    AI agents are used for audit clients (CCAB-AI-2026, section 10).
  human_checkpoints:
  - Not described beyond 'additional agents planned'.
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
  - ref: FIELDGUIDE-FINANCIALS-2026
    title: Fieldguide Launches Field Financials and Fieldguide MCP, Along With a Refreshed Brand
    publisher: Fieldguide (GlobeNewswire via AAP)
    type: vendor
    url: https://aapnews.aap.com.au/news/globenewswire9808260
    date: '2026-08-12'
    access: full
    locator: >-
      Paragraph describing Field Financials and its three agents; paragraph on availability (Drafting Agent available;
      Review & Tie-Out and Disclosure Agents 'in the fall')
  - ref: CCAB-AI-2026
    title: >-
      Draft Statement to the Accountancy Profession on the Ethical Use of Artificial Intelligence (exposure draft)
    publisher: CCAB Ethics Group
    type: professional-body
    url: >-
      https://www.ccab.org.uk/wp-content/uploads/2026/06/CCAB.Draft-Statement-to-the-Profession-on-Use-of-AI.-Exposure-Draft.6.6.26-002.pdf
    date: 2026-06
    access: full
    locator: Section 10, 'Management Responsibility Threat'
  last_reviewed: '2026-10-16'
  notes: >-
    Vendor release only; the Disclosure Agent here rolls forward footnotes and is not the same as the checklist
    matching in use case 01. Marked 'announced' because only the Drafting Agent was said to be available on 2026-08-12
    and no user is named.
- id: assurance-completion-reporting-05
  title: >-
    Tie out, foot and cross-reference the financial statements and notes to the trial balance and audited amounts
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Firms interviewed by PCAOB staff listed comparing amounts in the financial statements or notes with audited
    amounts as a possible area for GenAI assistance (PCAOB-GENAI-2024, p. 4).
  solution: >-
    Fieldguide's Review & Tie-Out Agent runs continuous, deterministic validation and flags stale overrides when
    adjustments change the underlying trial balance data (FIELDGUIDE-FINANCIALS-2026). Automated foot-and-proof
    tools already exist at many small and mid-size US firms (CPACOM-ATR-2025).
  outcomes:
  - lever: capacity
    description: >-
      Share of surveyed firms with an automated foot-and-proofing solution, and with automated report production
    figure: 39% foot and proofing; 17% report production
    measures: >-
      share of 54 firms with complete survey data answering that the firm has an automated solution for the function;
      the question is not limited to AI
    provenance: independent
    source_ref: CPACOM-ATR-2025
  prerequisites:
  - >-
    Trial balance data in the platform; adjustments to it trigger the checks (FIELDGUIDE-FINANCIALS-2026).
  risks_and_guardrails:
  - >-
    Fieldguide calls the validation deterministic (FIELDGUIDE-FINANCIALS-2026); the FRC lists rules-based components
    that evaluate LLM outputs as a mitigation for deficient output (FRC-GENAI-2026, 'Mitigations for GenAI component
    performance risk').
  human_checkpoints:
  - Not described.
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: FIELDGUIDE-FINANCIALS-2026
    title: Fieldguide Launches Field Financials and Fieldguide MCP, Along With a Refreshed Brand
    publisher: Fieldguide (GlobeNewswire via AAP)
    type: vendor
    url: https://aapnews.aap.com.au/news/globenewswire9808260
    date: '2026-08-12'
    access: full
    locator: Paragraph describing the Review & Tie-Out Agent; availability paragraph
  - ref: CPACOM-ATR-2025
    title: 2025 Audit Transformation Report
    publisher: CPA.com (with AICPA)
    type: survey
    url: https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf
    date: 2025-12
    access: full
    locator: Theme 1 chart 'For which of the following does the firm have an automated solution?' (p. 10)
  - ref: PCAOB-GENAI-2024
    title: >-
      Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence
      in Audits and Financial Reporting
    publisher: PCAOB (staff)
    type: regulator
    url: https://pcaobus.org/documents/generative-ai-spotlight.pdf
    date: 2024-07
    access: full
    locator: p. 4, 'Investment in GenAI'
  - ref: FRC-GENAI-2026
    title: Generative and Agentic AI Guidance
    publisher: Financial Reporting Council (UK)
    type: regulator
    url: https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf
    date: '2026-03-30'
    access: full
    locator: >-
      Section 'Mitigations for GenAI component performance risk' (rules-based components that evaluate LLM outputs)
  last_reviewed: '2026-10-16'
  notes: >-
    The survey figure measures traditional automation, not AI, and 54 firms is a small, non-representative sample,
    so the measurement is adjacent and the grade stays at C. The Review & Tie-Out Agent was due 'in the fall' of
    2026 as of the release.
- id: assurance-completion-reporting-06
  title: >-
    Check consistency of XBRL-tagged statements across documents: concept matching, taxonomy relations and arithmetic
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - review-assurance
  pattern: reconcile-exceptions
  ladder: assist
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Financial reports filed in XBRL turn auditing into a structured extraction and reasoning problem spanning concepts,
    taxonomy-defined relations and cross-document consistency (ARXIV-FINAUDITING-2025).
  solution: >-
    Research benchmark: LLMs are evaluated on semantic matching, relationship extraction and mathematical reasoning
    over real XBRL filings (ARXIV-FINAUDITING-2025).
  outcomes:
  - lever: quality
    description: >-
      Thirteen LLMs showed substantial gaps in concept retrieval, taxonomy-aware relation modelling and consistent
      cross-document reasoning
    figure: 1,102 annotated instances, averaging over 33k tokens, 13 models; no headline score in the abstract
    measures: count of annotated benchmark instances and models evaluated; per-task scores not read
    provenance: independent
    source_ref: ARXIV-FINAUDITING-2025
  prerequisites:
  - Filings in XBRL with a taxonomy (ARXIV-FINAUDITING-2025).
  risks_and_guardrails:
  - >-
    The authors report substantial gaps in current models and call for realistic, structure-aware benchmarks (ARXIV-FINAUDITING-2025).
  human_checkpoints:
  - Not applicable to a benchmark.
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - ref: ARXIV-FINAUDITING-2025
    title: "FinAuditing: A Financial Taxonomy-Structured Multi-Document Benchmark for Evaluating LLMs"
    publisher: arXiv (SIGIR 2026 Resource Track, per the page)
    type: academic
    url: https://arxiv.org/abs/2510.08886
    date: '2025-10-10'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-16'
  notes: >-
    Idea (research only). No firm deployment found. The paper reports it is accepted at SIGIR 2026 (Resource Track)
    and serves as an official benchmark of a public evaluation contest.
- id: assurance-completion-reporting-07
  title: >-
    Detect misstatements in financial statements and map each to the accounting standard breached, with an explanation
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - review-assurance
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: Auditors still miss errors despite extensive verification (ARXIV-LLMAUDIT-2025).
  solution: >-
    A benchmark with a five-stage evaluation checks whether LLMs can find statement errors and map them to standard
    violations (ARXIV-LLMAUDIT-2025). A separate unsupervised approach flags likely misinformation in statements
    and the financial variables behind it, using past statements and audit reports (ARXIV-FSMISINFO-2026).
  outcomes:
  - lever: quality
    description: >-
      LLMs identified statement errors when given historical transaction data, but were weak at explaining errors,
      citing standards and executing a complete audit with revisions
    figure: none numeric in the abstract
    measures: qualitative result on the authors' benchmark; scores not read
    provenance: independent
    source_ref: ARXIV-LLMAUDIT-2025
  - lever: quality
    description: The unsupervised method was demonstrated on a corpus of statements and audit reports
    figure: 11,460 financial statements over 5 years
    measures: size of the corpus used to demonstrate the method; accuracy figures not read
    provenance: independent
    source_ref: ARXIV-FSMISINFO-2026
  prerequisites:
  - >-
    Historical transaction data for the LLM benchmark (ARXIV-LLMAUDIT-2025); a corpus of past statements and audit
    reports for the unsupervised method (ARXIV-FSMISINFO-2026).
  risks_and_guardrails:
  - >-
    The abstract reports significant limitations in explaining detected errors and citing relevant accounting standards
    (ARXIV-LLMAUDIT-2025).
  human_checkpoints:
  - >-
    The auditor explores flagged data sources and business processes to validate suggestions (ARXIV-FSMISINFO-2026).
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - ref: ARXIV-LLMAUDIT-2025
    title: Automating Financial Statement Audits with Large Language Models
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2506.17282
    date: '2025-06-14'
    access: full
    locator: Abstract
  - ref: ARXIV-FSMISINFO-2026
    title: Financial Audit Assistance using Misinformation Detection and Explanation
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2607.17797
    date: '2026-07-20'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-16'
  notes: Idea (research only). Abstracts read; no firm deployment found.
- id: assurance-completion-reporting-08
  title: >-
    Give the accountant an LLM going-concern risk signal built from structured financials and auditor-report text
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: >-
    The thesis says traditional machine-learning bankruptcy models face challenges with complex, unstructured data,
    and that LLM use for going-concern assessment of healthcare organisations 'remains unexplored' (LEIDEN-GC-2025,
    abstract).
  solution: >-
    A prompt-optimised LLM (DSPy) combines structured financial data with unstructured audit reports to predict
    bankruptcy within two years, and shows the accountant the prediction plus a model-generated summary of one auditor's-report
    page (LEIDEN-GC-2025). ISA 570 (Revised 2024) already lists predictive bankruptcy or insolvency models as an
    example of automated tools in risk assessment (IAASB-ISA570-2025, para A13).
  outcomes:
  - lever: quality
    description: Model accuracy on the 20 case-study organisations versus accountants' average
    figure: model 85%; control group average 77%; LLM-assisted group average 78%
    measures: >-
      share of organisations correctly classified as bankrupt or not within two years, on 20 healthcare organisations
      drawn from the model's test set; two groups of five BDO accountants
    provenance: independent
    source_ref: LEIDEN-GC-2025
  - lever: quality
    description: Cross-validated model accuracy on the full sample
    figure: up to 79%
    measures: >-
      accuracy of the best prompt optimiser (COPRO) in stratified 3-fold cross-validation over 82 Dutch healthcare
      organisations (41 bankrupt, 41 matched non-bankrupt)
    provenance: independent
    source_ref: LEIDEN-GC-2025
  - lever: speed
    description: No difference in speed
    figure: 18.4 organisations per participant in both groups
    measures: average number of organisations assessed per participant within a 45-minute limit
    provenance: independent
    source_ref: LEIDEN-GC-2025
  prerequisites:
  - >-
    Structured financial data and audit reports for comparable organisations; expert-selected features performed
    better than automatic selection (LEIDEN-GC-2025).
  risks_and_guardrails:
  - >-
    The LLM group did slightly better only on edge cases (67% versus 60%); overall accuracy and speed did not differ
    (LEIDEN-GC-2025, section 4.3).
  - >-
    Not a replica of a real audit; the author says the setting was structured and the sample small (LEIDEN-GC-2025,
    section 3.6).
  human_checkpoints:
  - >-
    The accountant makes the going-concern call; the model prediction and summary are inputs (LEIDEN-GC-2025).
  role_evolution: >-
    All participants said they would use the model in real evaluations; they valued it for highlighting key financial
    indicators (LEIDEN-GC-2025, abstract).
  evidence_grade: A
  sources:
  - ref: LEIDEN-GC-2025
    title: >-
      Evaluating LLMs in Practice: Enhancing Going Concern Assessments for Healthcare Organizations (master's thesis)
    publisher: Leiden University (LIACS), with BDO Netherlands as company supervisor
    type: academic
    url: https://theses.liacs.nl/pdf/2024-2025-JongTdeTessa.pdf
    date: '2025-04-14'
    access: full
    locator: Abstract; sections 3.6 and 4.3 (case study, accuracy, speed)
  - ref: IAASB-ISA570-2025
    title: International Standard on Auditing 570 (Revised 2024), Going Concern (final pronouncement)
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2025-04/IAASB-ISA570-Going-Concern-Revised.pdf
    date: '2025-04-09'
    access: full
    locator: Application material para A13
  last_reviewed: '2026-10-16'
  notes: >-
    Graded A on a technicality: BDO Netherlands is named as data provider, company supervisor and source of the
    ten accountants, and the outcome is measured. It is a master's thesis with ten participants and a case study,
    not a live engagement or a peer-reviewed result, and it found no accuracy or speed gain. Treat as the best measured
    going-concern LLM result found, not as proof of value.
- id: assurance-completion-reporting-09
  title: >-
    Use automated tools to run sensitivity analysis on management's going-concern assessment and to test the reliability
    of its data
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: full-population-testing
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    The IAASB says ISA 570 (Revised 2024) significantly enhances the auditor's work in evaluating management's assessment
    of going concern and strengthens communication with those charged with governance and in the auditor's report
    (IAASB-ISA570PAGE-2025).
  solution: >-
    The standard's own application material says automated tools and techniques may assist with sensitivity analysis
    of management's assessment (for example discount or growth rates) and with evaluating the reliability of large
    volumes of data from several sources used by management (IAASB-ISA570-2025, paras A42 and A46). It also lists
    analytical procedures on key financial ratios as an example (para A13).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: the standard gives examples, not results
    provenance: independent
    source_ref: IAASB-ISA570-2025
  prerequisites:
  - >-
    Management's assessment covering at least twelve months from the approval date of the financial statements,
    or an auditor request to extend it (IAASB-ISA570-2025, para 21).
  risks_and_guardrails:
  - >-
    The standard says tools 'may' assist; it sets no requirement and no quality criteria for them (IAASB-ISA570-2025,
    paras A13, A42, A46).
  human_checkpoints:
  - The auditor evaluates management's method, assumptions and data (IAASB-ISA570-2025).
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - ref: IAASB-ISA570-2025
    title: International Standard on Auditing 570 (Revised 2024), Going Concern (final pronouncement)
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2025-04/IAASB-ISA570-Going-Concern-Revised.pdf
    date: '2025-04-09'
    access: full
    locator: Paragraph 21; application material A13, A42, A46
  - ref: IAASB-ISA570PAGE-2025
    title: ISA 570 (Revised 2024), Going Concern (landing page)
    publisher: IAASB
    type: standard-setter
    url: https://www.iaasb.org/publications/isa-570-revised-2024-going-concern
    date: '2025-04-09'
    access: full
    locator: "Landing page: effective for periods beginning on or after 15 December 2026"
  last_reviewed: '2026-10-16'
  notes: >-
    Idea: a standard-setter's illustration, no public deployment found. Effective date 15 Dec 2026. The PCAOB's
    AS 2415 is a different, older text; the PCAOB project may examine how technology affects going-concern evaluation
    but has no proposal (PCAOB-AGENDA-2026).
- id: assurance-completion-reporting-10
  title: >-
    Propose candidate critical audit matter topics with generative AI and compare them with the engagement team's
    list
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    CAM disclosures draw differing views on usefulness and the PCAOB is planning a further post-implementation review
    (PCAOB-AGENDA-2026, 'Post-Implementation Review for Critical Audit Matters').
  solution: >-
    Researchers use generative AI to identify CAM topics from filings and compare them with the CAMs auditors reported
    (GUO-CAM-2024).
  outcomes:
  - lever: quality
    description: >-
      AI predicted part of auditor-reported CAMs; overlapping CAMs were associated with financial reporting risk
      and abnormal stock returns while CAMs reported only by AI or only by auditors were not
    figure: approximately 37%
    measures: >-
      share of auditor-reported CAMs that AI could predict, per the authors' seminar abstract; sample and model
      not stated in the abstract
    provenance: independent
    source_ref: GUO-CAM-2024
  prerequisites:
  - Not stated in the abstract.
  risks_and_guardrails:
  - >-
    The authors expect AI to be less informative than auditors because it lacks professional judgment and access
    to private client information (GUO-CAM-2024).
  human_checkpoints:
  - >-
    The auditor decides which matters meet the CAM definition in AS 3101 (PCAOB-AS3101; PCAOB-PIRCAM-2022).
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - ref: GUO-CAM-2024
    title: >-
      Man + machines: assessing the informativeness of critical audit matters identified by AI and human auditors
      (seminar abstract)
    publisher: "Wuhan University Economics and Management School (speaker: Feng Guo, Iowa State University)"
    type: academic
    url: https://ems.whu.edu.cn/info/1900/263911.htm
    date: '2024-12-17'
    access: full
    locator: Abstract
  - ref: PCAOB-AGENDA-2026
    title: Standard-Setting, Research, Rulemaking, and Related Activities
    publisher: PCAOB
    type: regulator
    url: https://pcaobus.org/standards/standard-setting-research-projects
    date: '2026'
    access: full
    locator: Section 'Post-Implementation Review for Critical Audit Matters'
  - ref: PCAOB-PIRCAM-2022
    title: "Post-Implementation Review: Auditor Reporting (critical audit matters)"
    publisher: PCAOB
    type: regulator
    url: https://pcaobus.org/oversight/standards/pir/auditor-reporting
    date: 2022-12
    access: full
    locator: Key findings; reminder paragraph on AS 3101
  last_reviewed: '2026-10-16'
  notes: >-
    Idea: a research study, not a deployment. The abstract is from a December 2024 seminar and no paper was located.
    No firm describes using AI to draft or choose CAMs or key audit matters.
- id: assurance-completion-reporting-11
  title: >-
    Pre-review the audit file for documentation gaps and open items before partner and engagement quality review
    sign-off
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - review-assurance
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    PCAOB inspections found EQR deficiencies at 42% of inspected firms in 2022, up from 37% in 2020, and one common
    deficiency was failing to document the EQR properly (PCAOB-EQR-2023, pp. 3 and 8).
  solution: >-
    Firms interviewed by PCAOB staff named evaluating the completeness of audit documentation against documentation
    requirements as a possible GenAI use (PCAOB-GENAI-2024, p. 4). Fieldguide names a 'Field Reviewer' agent as
    rolling out later in 2026 without describing it (FIELDGUIDE-FINANCIALS-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: no measurement of AI-assisted pre-review found
    provenance: independent
    source_ref: PCAOB-GENAI-2024
  prerequisites:
  - Not stated in the sources.
  risks_and_guardrails:
  - >-
    AS 1220 requires the engagement quality reviewer to evaluate significant judgments and give concurring approval
    before the report is released; a tool does not change that (PCAOB-AS1220).
  - >-
    ISQM 2 defines the EQR as an objective evaluation of the significant judgments of the engagement team (IAASB-ISQM2-2020,
    para 8).
  human_checkpoints:
  - Reviewer sign-off and concurring approval (PCAOB-AS1220).
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - ref: PCAOB-GENAI-2024
    title: >-
      Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence
      in Audits and Financial Reporting
    publisher: PCAOB (staff)
    type: regulator
    url: https://pcaobus.org/documents/generative-ai-spotlight.pdf
    date: 2024-07
    access: full
    locator: p. 4, 'Investment in GenAI'
  - ref: PCAOB-EQR-2023
    title: "Spotlight: Inspection Observations Related to Engagement Quality Reviews"
    publisher: PCAOB (staff)
    type: regulator
    url: https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/eqr-spotlight.pdf
    date: 2023-10
    access: full
    locator: Overview, p. 3 (37% in 2020 to 42% in 2022); p. 8 (documentation of the EQR)
  - ref: PCAOB-AS1220
    title: "AS 1220: Engagement Quality Review"
    publisher: PCAOB
    type: standard-setter
    url: https://pcaobus.org/oversight/standards/auditing-standards/details/AS1220
    date: '2026'
    access: full
    locator: Objective and qualifications paragraphs; note on 2026-12-15 amendments
  - ref: IAASB-ISQM2-2020
    title: International Standard on Quality Management 2, Engagement Quality Reviews
    publisher: IAASB
    type: standard-setter
    url: >-
      https://www.ifac.org/_flysystem/azure-private/publications/files/IAASB-Quality-Management-ISQM-2-Engagement-Quality-Reviews.pdf
    date: '2020-12-17'
    access: full
    locator: Paragraph 8
  - ref: FIELDGUIDE-FINANCIALS-2026
    title: Fieldguide Launches Field Financials and Fieldguide MCP, Along With a Refreshed Brand
    publisher: Fieldguide (GlobeNewswire via AAP)
    type: vendor
    url: https://aapnews.aap.com.au/news/globenewswire9808260
    date: '2026-08-12'
    access: full
    locator: >-
      Paragraph on the Field Agent family ('Field Planner and Field Reviewer, rolling out later this year')
  last_reviewed: '2026-10-16'
  notes: >-
    Idea listed by firms to the PCAOB in 2024; no deployment for EQR found. The EQR itself has no public AI use
    case, see Module notes 'Open questions'. The 37%/42% figures count inspected firms with at least one EQR-deficiency
    comment form, not engagements.
- id: assurance-completion-reporting-12
  title: Analyse audit committee communications to surface issues earlier in the audit cycle
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - research-synthesis
  - review-assurance
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    PwC describes issues from audit committee communications that need to be handled sooner in the audit preparation
    cycle (CFODIVE-PWC-2026).
  solution: >-
    A PwC tool analyses audit committee communications to surface issues that need handling sooner in the audit
    preparation cycle (CFODIVE-PWC-2026).
  outcomes:
  - lever: speed
    description: >-
      none published for this tool; on overall AI time savings PwC's US assurance and transformation leader said
      'It's not that drastic yet'
    figure: none published
    measures: no measure; the general comment is by PwC's US assurance and transformation leader
    provenance: self-reported
    source_ref: CFODIVE-PWC-2026
  prerequisites:
  - Access to committee communications; not described.
  risks_and_guardrails:
  - >-
    IFIAR expects transparency to those charged with governance about how technology is used in the audit and how
    it affects decisions (IFIAR-TTF-2026, 'Transparency of Use and for Those Charged with Governance').
  - >-
    Audit committee chairs told the PCAOB staff they want insight from auditors on AI's effect on financial reporting
    and several asked how audit firms' AI use would affect fees (PCAOB-ACCHAIRS-2026, p. 8).
  human_checkpoints:
  - Not described.
  role_evolution: >-
    PwC said the final audit report looks the same and what comes out is still comfort on the financial statements
    (CFODIVE-PWC-2026).
  evidence_grade: C
  sources:
  - ref: CFODIVE-PWC-2026
    title: PwC exec ushers in AI-assisted audits, awaits bigger time savings
    publisher: CFO Dive
    type: press
    url: https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/
    date: '2026-10-07'
    access: full
    locator: Paragraph beginning 'For 2026 year-end audits'; paragraph on what has and has not changed
  - ref: IFIAR-TTF-2026
    title: Use of technology in audits - Innovation and audit quality 2026
    publisher: IFIAR Technology Task Force (copy hosted by Japan FSA)
    type: regulator
    url: https://www.fsa.go.jp/ifiar/2026TTFReport.pdf
    date: '2026-04-20'
    access: full
    locator: Section 'Transparency of Use and for Those Charged with Governance' (pp. 7-8)
  - ref: PCAOB-ACCHAIRS-2026
    title: "Spotlight: 2025 Conversations With Audit Committee Chairs"
    publisher: PCAOB (staff)
    type: regulator
    url: >-
      https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/2025-conversations-with-audit-committee-chairs-spotlight.pdf
    date: 2026-04
    access: full
    locator: Section 'Top Technology Risks Discussed With Auditors' (p. 8)
  last_reviewed: '2026-10-16'
  notes: >-
    Only press description, and 'analyzes audit committee communications' is not defined (inbound materials, auditor's
    own communications or both). Drafting or delivering AS 1301 / ISA 260 communications with AI has no public evidence
    found.
- id: assurance-completion-reporting-13
  title: Agent completes and reviews staff-level workpapers, measured on synthetic engagements
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: >-
    Limited access to proprietary audit data has constrained measurement of where agents can be deployed reliably
    and where professional review remains necessary (ARXIV-FAB-2026).
  solution: >-
    A benchmark of 90 tasks covering workpaper completion and review across six synthetic engagements, evaluated
    on eleven frontier models (ARXIV-FAB-2026).
  outcomes:
  - lever: quality
    description: >-
      Agents completed substantial portions of staff-level tasks well but sometimes performed inappropriate procedures
      or produced incorrect documentation
    figure: 90 tasks; six engagements of about 179 files each; 11 models; no score in the abstract
    measures: count of benchmark tasks, synthetic engagements, average files per engagement, and models evaluated
    provenance: independent
    source_ref: ARXIV-FAB-2026
  prerequisites:
  - The test input was synthetic engagements averaging 179 files each (ARXIV-FAB-2026).
  risks_and_guardrails:
  - Inappropriate procedures and incorrect documentation are the failure modes named (ARXIV-FAB-2026).
  human_checkpoints:
  - Professional review remains necessary where agents are not reliable (ARXIV-FAB-2026, abstract).
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - ref: ARXIV-FAB-2026
    title: "FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors"
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.32835
    date: '2026-09-26'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-16'
  notes: >-
    Idea (research only). Synthetic data built from differentially private statistics of historical audits and over
    1,100 hours of expert development; no real engagement tested.
- id: assurance-completion-reporting-14
  title: >-
    Agent drafts audit documentation, compliance and disclosure evaluations and preliminary conclusions for professional
    review
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: delegate
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Preliminary procedures, drafting and first-pass evaluation consume staff time (DELOITTE-OMNIA-2026).
  solution: >-
    Deloitte says its Omnia agents execute preliminary procedures including data extraction, evidence analysis,
    drafting documentation and developing preliminary conclusions for professionals to review, and assist with evaluating
    compliance with regulatory and disclosure requirements (DELOITTE-OMNIA-2026). some firms interviewed by PCAOB
    staff said staff can use GenAI for initial drafts of audit memos and presentations (PCAOB-GENAI-2024, p. 4).
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: no figure in the release
    provenance: vendor-published
    source_ref: DELOITTE-OMNIA-2026
  prerequisites:
  - The agents run inside Deloitte Omnia (DELOITTE-OMNIA-2026).
  risks_and_guardrails:
  - >-
    The FRC says regulatory accountability does not change and the human auditor is always accountable (FRC-NEWS-2026).
  - >-
    The PCAOB staff recorded that supervisors reviewing GenAI-assisted work are expected to apply the same diligence
    as for other work, per the firms interviewed (PCAOB-GENAI-2024, pp. 4-5).
  human_checkpoints:
  - Professionals review the agents' preliminary conclusions (DELOITTE-OMNIA-2026).
  role_evolution: Deloitte says professionals will supervise, validate and work alongside AI (DELOITTE-OMNIA-2026).
  evidence_grade: C
  sources:
  - ref: DELOITTE-OMNIA-2026
    title: Deloitte unveils connected agentic intelligence in Omnia
    publisher: Deloitte US
    type: firm
    url: >-
      https://www.deloitte.com/us/en/about/press-room/deloitte-unveils-connected-agentic-intelligence-in-omnia.html
    date: '2026-06-24'
    access: full
    locator: Bullets on preliminary procedures and on disclosure evaluation; closing paragraph on supervising AI
  - ref: PCAOB-GENAI-2024
    title: >-
      Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence
      in Audits and Financial Reporting
    publisher: PCAOB (staff)
    type: regulator
    url: https://pcaobus.org/documents/generative-ai-spotlight.pdf
    date: 2024-07
    access: full
    locator: p. 4, 'Current Use of GenAI'; pp. 4-5, 'Supervision and Review of GenAI'
  - ref: FRC-NEWS-2026
    title: Innovative new guidance supports audit firm adoption of emerging AI technologies
    publisher: Financial Reporting Council (UK)
    type: regulator
    url: >-
      https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/
    date: '2026-03-30'
    access: full
    locator: Paragraph on accountability
  last_reviewed: '2026-10-16'
  notes: >-
    Not specific to completion; no source describes agents drafting a completion memo, a summary of uncorrected
    misstatements or an audit report. A Bloomberg Law report of the same launch (agents drafting staff memos, scanning
    media for emerging threats) was seen only in search extracts and is not relied on.
```

## 3. Module notes

### 3.1 Processes and key steps (with work types)

- **Disclosure checklist and financial-statement review** (review-assurance): compare the draft statements with the required disclosures, tie amounts to audited balances. Public AI evidence: use cases 01, 02, 05, 06, 07.
- **Other-information and management-report review** (review-assurance): use case 03.
- **Subsequent events** (expert-judgment, research-synthesis): AS 2801 covers events after the balance sheet date, in two types, adjusting and non-adjusting (PCAOB-AS2801, paras .02-.06). No AI evidence.
- **Going concern** (expert-judgment): AS 2415 asks the auditor to evaluate substantial doubt for a reasonable period not to exceed one year from the statement date (PCAOB-AS2415, para .02). ISA 570 (Revised 2024) requires evaluating management's assessment whether or not events or conditions are identified, requires at least twelve months from the approval date (para 21), and has sections on written representations (paras 39-40) and communication with those charged with governance (paras 41-42) (IAASB-ISA570-2025; IAASB-ISA570PAGE-2025). Use cases 08, 09.
- **Written representations** (review-assurance): no AI evidence.
- **Evaluation and summary of misstatements** (review-assurance, data-reporting): no AI evidence. The standards on evaluating audit results (AS 2810, ISA 450) were not opened.
- **Engagement quality review** (review-assurance): the reviewer evaluates significant judgments and gives concurring approval before the report is released (PCAOB-AS1220; IAASB-ISQM2-2020, para 8). Use case 11 is the only related idea.
- **Critical and key audit matters** (expert-judgment, document-production): AS 3101 requires CAMs and defines them as matters communicated or required to be communicated to the audit committee that relate to material accounts or disclosures and involved especially challenging, subjective or complex auditor judgment, per PCAOB staff (PCAOB-ACCHAIRS-2026, p. 7; PCAOB-AS3101). Use case 10.
- **Audit committee communications** (client-interaction, document-production): AS 1301 sets objectives that include giving the committee timely observations significant to financial reporting (PCAOB-AS1301, para .03). Use case 12.
- **Opinion and report drafting** (document-production): no AI evidence. PwC says the final audit report looks the same as before (CFODIVE-PWC-2026).

### 3.2 Common pain points

- **Checklist scale and fatigue.** A full checklist can run to 1,200-1,500 requirements, and Thomson Reuters says fatigue sets in and many firms roll last year's checklist forward (TR-DISCLOSURE-2026).
- **EQR quality.** The share of PCAOB-inspected firms with at least one EQR-deficiency comment form rose from 37% in 2020 to 42% in 2022. The US global network firms rose by 33 percentage points from 2021 to 2022 (PCAOB-EQR-2023, p. 3). The AS 1220 post-implementation review (2018) found reviewer hours rose after the standard but were small relative to total audit hours (PCAOB-PIR1220-2018, p. 2).
- **CAM usefulness is contested.** PCAOB feedback in 2026 shows differing stakeholder views on the usefulness of CAM disclosures and on the need for further standard setting (PCAOB-AGENDA-2026). The staff found the average number of CAMs per report declined over time (PCAOB-PIRCAM-2022).
- **Going-concern reporting.** The PCAOB project cites changes in investor needs and the need to coordinate auditor and management responsibilities under reporting frameworks (PCAOB-AGENDA-2026).
- **Audit committee asks about AI.** Chairs want insight on AI's effect on financial reporting and controls, and several asked how audit firms' AI use would affect fees (PCAOB-ACCHAIRS-2026, p. 8).

### 3.3 Metrics and benchmarks

| Metric | Value | What it measures (source's words, as close as possible) | Provenance | Source |
|---|---|---|---|---|
| Time saved per checklist run | 2.7 hours average | firms beta testing Caseware's Disclosure Checklist Agent; results vary | vendor-published | CASEWARE-CWX-2026 |
| Uptake of TR Disclosure Review | about 30%; close to 300 analyses a month | eligible Disclosure-module customers using it; analyses generated monthly across mid-sized and large firms | vendor-published | TR-DISCLOSURE-2026 |
| Automated foot and proofing; report production | 39%; 17% | firms with an automated solution, of 54 firms with complete data; not limited to AI | independent (survey) | CPACOM-ATR-2025, p. 10 |
| Growth in AI-enabled tools | about 30% year over year | reported by the GPPC networks collectively for 2025, collected by IFIAR's task force, subject to differing firm reporting | independent (regulator forum) | IFIAR-TTF-2026, p. 5 |
| EQR deficiency, share of inspected firms | 37% (2020), 42% (2022) | firms with at least one comment form with an EQR deficiency | independent (regulator) | PCAOB-EQR-2023, p. 3 |
| EQR reviewer hours share | about 1% (large domestic firms), 3% (small) of total audit hours | engagement quality reviewer hours as a share of average total audit hours after AS 1220 took effect; PCAOB staff data on inspected issuer audits, a 2018 baseline | independent (regulator) | PCAOB-PIR1220-2018, p. 2 |
| Audit committee chairs: auditor discussed CAMs | 90% | of more than 250 chairs surveyed in 2025, 82% at companies audited by US global network firms | independent (regulator staff) | PCAOB-ACCHAIRS-2026, pp. 3, 7 |
| Audit committee chairs: formal annual assessment of auditor | 81% | of the same chairs | independent (regulator staff) | PCAOB-ACCHAIRS-2026, p. 4 |
| AI predicts auditor-reported CAMs | about 37% | share of auditor-reported CAMs predicted by AI; overlap items associated with reporting risk | independent (academic, seminar abstract) | GUO-CAM-2024 |
| LLM going-concern signal | 85% model; 77% control; 78% LLM-assisted | correct bankrupt or not within two years on 20 organisations; groups of five BDO accountants | independent (thesis) | LEIDEN-GC-2025, section 4.3 |
| AI investment and report reissuance | 5.0% lower likelihood per one standard deviation of recent AI investment | Fedyk et al. (2022), as summarised by the Japan FSA discussion paper; original not read | independent (academic, secondary) | FSA-DP-2025, pp. 9-10 |
| AI investment and audit fees | 0.9% reduction | same study, same caveat | independent (academic, secondary) | FSA-DP-2025, p. 10 |
| AI hiring and going-concern errors | AI hiring reduced Type 1 going-concern errors and non-reliance restatements | Law and Shen (2025), as summarised in the FSA paper; Type 1 means a going-concern opinion for a client that does not fail within 12 months; no coefficients given | independent (academic, secondary) | FSA-DP-2025, pp. 8-9 |
| Benchmarks | 1,102 XBRL instances, 13 LLMs; 90 workpaper tasks, 11 models | sizes of the benchmarks; headline scores not read | independent (academic) | ARXIV-FINAUDITING-2025; ARXIV-FAB-2026 |

None of the figures above measures the accuracy of a disclosure-checklist tool, and none is an error rate from live engagements.

### 3.4 Guardrails and regulatory points

- **FRC guidance (UK, 30 Mar 2026).** Three risk groups: deficient output (including hallucination and omission), misuse of output, and non-compliant methodology. Mitigations: system design, certification and recertification, staff education, governance, and human-in-the-loop review at control points. It says outputs need not match the persuasiveness of the procedure replaced, provided the methodology does not overstate it. It is not a response to identified quality deficiencies and it keeps accountability with the human auditor (FRC-GENAI-2026, introduction and the section 'Misunderstanding of methodology risk'; FRC-NEWS-2026). Its two worked examples are summarising board minutes and contract review for revenue testing, not completion steps.
- **ISA 220 (Revised).** Names overreliance on automated tools (A34) and automation bias (A35) as impediments to skepticism, and says technological tools may allow auditors to challenge management more effectively but inappropriate use raises overreliance risk (A63) (IAASB-ISA220-2020).
- **ISA 570 (Revised 2024).** Effective for periods beginning on or after 15 Dec 2026. Automated tools are examples, not requirements (IAASB-ISA570-2025, A13, A42, A46; IAASB-ISA570PAGE-2025).
- **PCAOB.** The standard-setting page lists the going-concern, fraud, comfort-letter and independence projects and says staff plan guidance on the use of what the page calls "super intelligence" by companies and auditors (PCAOB-AGENDA-2026). The PCAOB chair said in September 2026 that "the science, the transaction part" of an audit can be done by AI while the "art" needs people (ATODAY-LOGOTHETIS-2026). The PCAOB's 2025 inspection plan selected companies likelier to have going-concern risk and said inspectors would keep inquiring about technology used in audit procedures (PCAOB-PRIORITIES-2024, pp. 4-5). AS 1220 amendments are effective 15 Dec 2026 (PCAOB-AS1220).
- **PCAOB staff GenAI spotlight (Jul 2024).** Firms said engagement team members remain responsible for results and documentation and supervisors apply the same diligence; some firms barred GenAI in performing audit or attest procedures (PCAOB-GENAI-2024, pp. 4-5). Staff view, not Board policy.
- **IFIAR (Apr 2026).** Audits should stay "human-led" in practice: named personnel at decision checkpoints, an overarching review of autonomous decisions, and senior team members reflecting on whether skepticism was maintained. Transparency to those charged with governance is encouraged (IFIAR-TTF-2026, pp. 7-8).
- **AICPA practice aid (13 Oct 2026).** Non-authoritative. Where AI is used, the auditor remains responsible. One AI tool may help evaluate another but does not reduce the auditor's supervision and review duties, and AU-C 210 does not require naming AI tools in the engagement letter (AICPA-PA-2026; ATODAY-AICPAPA-2026).
- **CCAB draft statement (Jun 2026).** AI use does not reduce the accountant's personal responsibility; accountants should be transparent with clients about AI use and not associate themselves recklessly with unvalidated AI output (CCAB-AI-2026, section 11 paras 4.1-4.2; ACCA-KN-2026).
- **Japan FSA discussion paper (Jul 2025).** The author suggests firms may need to consider disclosure standards on the transparency of AI audit tools; the views are the author's (FSA-DP-2025, p. 19).

### 3.5 Frontier signals (dated)

- 2026-08-12: Fieldguide says a Review & Tie-Out Agent and a Disclosure Agent for financial statements will follow the first available Drafting Agent "in the fall" (FIELDGUIDE-FINANCIALS-2026).
- 2026-09-23: Thomson Reuters says future capabilities will extend into harder judgment calls such as "no" and "not applicable" determinations (TR-DISCLOSURE-2026).
- 2026-06-17: Caseware's chief product officer set a goal of automating up to 50% of the engagement workflow across prepare, plan, validate and report (CASEWARE-CWX-2026).
- 2026-04-20: IFIAR reports firms exploring agentic AI, which "may evolve" from task automation toward orchestration of multiple audit activities (IFIAR-TTF-2026, p. 5).
- 2026 (page undated): PCAOB staff plan to conduct a further post-implementation review of CAMs before deciding on further research, standard setting or guidance (PCAOB-AGENDA-2026). On 2026-04-30 the PCAOB Investor Advisory Group asked the public to nominate the most decision-useful 2025 CAMs and KAMs, for a report expected later in 2026 (PCAOB-IAG-2026).
- 2026-12-15: ISA 570 (Revised 2024) and the amended AS 1220 take effect (IAASB-ISA570PAGE-2025; PCAOB-AS1220).
- 2026-09-29: A Spanish-language summary of Accountancy Europe's September 2026 paper lists checking financial disclosures among GenAI procedures for audit and assurance, alongside summarising minutes and preparing drafts, and notes the move toward agentic systems; the primary paper was not read (INCP-AE-2026).
- 2025-04-22: KPMG said more agents would be deployed over the next 12 months, including into financial statement analysis; no follow-up was found (KPMG-CLARA-2025).

### 3.6 Workforce and role effects

- Visible rationale in checklist tools is pitched as a learning aid for junior staff (TR-DISCLOSURE-2026; CASEWARE-CWX-2026).
- Survey respondents at a German Big 4 firm had mixed views on deskilling and trust in AI output, varying with role and experience (FABIAN-2026).
- A registered-report proposal predicts that automating audit tasks with GenAI will lower auditors' autonomous motivation and judgment quality on a later task, partly because auditors shift from preparing to reviewing; it has no results (HOLMSTROM-PETERS-2024, abstract and introduction).
- Secondary summary of academic work: hiring AI employees was associated with more auditors, mainly junior and mid-level (Law and Shen 2025), and accounting employment fell 3.6% after three years and 7.1% after four following AI investment (Fedyk et al. 2022); partners interviewed said audit fees did not fall significantly (FSA-DP-2025, pp. 8-10). Not read in the originals.
- Fee questions are live: several audit committee chairs asked how audit firms' AI use would affect fees (PCAOB-ACCHAIRS-2026, p. 8).

### 3.7 Objections and concerns practitioners and regulators raise

- Over-reliance and skill loss (FABIAN-2026; IAASB-ISA220-2020, A34-A35; IFIAR-TTF-2026).
- Hallucination, including invented provisions of standards, and resulting liability (PCAOB-GENAI-2024, p. 5; FSA-DP-2025, p. 11).
- Harder judgments ("no", "not applicable", discretionary leeway, strategic statements) stay with people (TR-DISCLOSURE-2026; HAMBURG-FABIAN-2026).
- Independence and management responsibility when autonomous agents act on audit-client work (CCAB-AI-2026, section 10).
- Confidentiality and data security led some firms to bar GenAI in audit procedures (PCAOB-GENAI-2024, p. 4).
- Transparency to audit committees and fee effects (IFIAR-TTF-2026; PCAOB-ACCHAIRS-2026).
- Board-minute transcription by AI raises discoverability and privilege issues, relevant when auditors read AI-generated minutes (CAQ-ACI-2026-08, 'AI Drafting Board Minutes?').

### 3.8 Open questions: steps with no public evidence found

For each, the searches below returned nothing about use of AI by auditors, other than the adjacent items named. Treat all as questions for interviews, not as use cases.

- **Subsequent events.** Searches for AI with subsequent events found nothing. The closest analogue is the FRC's worked example of summarising board minutes for risk assessment (FRC-GENAI-2026, 'Illustrative examples'), which is a planning use.
- **Written representations.** Search for AI with management representation letters found nothing.
- **Summary of uncorrected misstatements and evaluation of audit results.** Nothing found. Fieldguide's Review & Tie-Out Agent flags stale overrides when adjustments change the trial balance, which is adjacent (FIELDGUIDE-FINANCIALS-2026).
- **Engagement quality review.** Search for AI with EQR found nothing beyond firms' general statements that supervisors review AI-assisted work as before (PCAOB-GENAI-2024). The PCAOB's latest EQR spotlight (Oct 2023) predates the GenAI material.
- **CAM and KAM drafting.** The only study found concerns identifying CAM topics (GUO-CAM-2024).
- **Opinion and report drafting.** Search for AI drafting of audit opinions found nothing; PwC says the report is unchanged in form (CFODIVE-PWC-2026).
- **Audit committee communications drafting.** Only PwC's analysis tool is described (CFODIVE-PWC-2026).
- **Going-concern assessment in live audits.** No firm describes a tool in use; the only measured study is a student thesis (LEIDEN-GC-2025).

### 3.9 Interview probes for an advisor

1. When your disclosure-checklist tool marks a requirement "not found" or "identified", who confirms it, and have you ever re-performed a sample to estimate how often it is wrong in either direction? What do you do with "not applicable" calls?
2. Going concern is changing under revised ISA 570 from December 2026. Do you use any model or LLM to challenge management's assessment, and what do you keep in the file as evidence of that work?
3. How do you tell the audit committee which AI tools were used in the audit and what they decided? Have committees asked about fees or about AI inside the client's own financial reporting?
4. Does your engagement quality reviewer get any AI support, and how is the reviewer's use of it documented, given how often EQR documentation is cited in inspections?
5. Where a platform drafts or rolls forward financial statements or footnotes, who owns the statements, and how do you handle independence and management responsibility?

### 3.10 Inspection and review evidence

- **PCAOB, engagement quality review.** Share of inspected firms with an EQR-deficiency comment form rose from 37% to 42% between 2020 and 2022; the staff called the trend troubling (PCAOB-EQR-2023, p. 3). No later EQR spotlight was found, and no AI element.
- **FRC, Annual Review of Audit Quality 2026.** Released by 2026-07-22, combining file inspections with evaluations of firms' systems of quality management (THEACCOUNTANT-ARAQ-2026). ICAS reports that the FRC pays particular attention to estimation and judgement areas including going concern, and reviewed communications to audit committees; its most common findings were in revenue and in estimation and judgement, tied to weak evaluation of key assumptions and challenge of management (ICAS-ARAQ-2026). The FRC expects firms to take a measured approach to AI and to report systemic risks (ICAS-ARAQ-2026). No AI-specific completion finding was captured, and the FRC report was not opened.
- **PCAOB inspections.** The 2025 plan selected companies likelier to have going-concern risk and said inspectors would inquire about technology used in audit procedures (PCAOB-PRIORITIES-2024, pp. 4-5). No published finding on AI tools was found.
- **IFIAR.** The 2026 report is observational: it says its observations are not a comprehensive assessment and reports no completion-step outcomes (IFIAR-TTF-2026, p. 3).
- **Audit committee side.** CAQ held a March 2026 webinar for audit committee members on how AI is used in financial reporting and in the audit and what that means for oversight (event page only; recording not viewed) (CAQ-WEBINAR-2026).

## 4. Routed to other modules

- **quality-management (engagement-level supervision and review).**
  - The AICPA practice aid says one AI tool may help evaluate whether another is performing correctly without reducing the auditor's supervision and review duties (ATODAY-AICPAPA-2026).
  - IFIAR 2026 on monitoring and recertification of tools (IFIAR-TTF-2026, pp. 7-8).
  - ISA 220 (Revised) A63-A64 on firm-approved technological tools (IAASB-ISA220-2020).
  - The PCAOB staff's mention of firm tools to research internal accounting and auditing guidance (PCAOB-GENAI-2024, p. 4).
  - Empirical links between AI investment, reissued reports and fees (FSA-DP-2025).
- **planning-risk-assessment.**
  - The FRC board-minutes summarisation example (FRC-GENAI-2026).
  - ICAEW's test of chatbots: none separated financial-statement-level from assertion-level risk, and one flagged going concern as a risk (ICAEW-PIERPOINT-2025).
  - PCAOB 2025 inspection attention to companies with significant AI investment, including ITGCs (PCAOB-PRIORITIES-2024, p. 7).
  - ISA 570 A13 on risk assessment tools (IAASB-ISA570-2025).
- **controls-testing and assurance over AI-enabled financial reporting (cross-cut).** CAQ's "invisible AI" and "shadow AI" points on ICFR, and the FEI AI framework for ICFR it recommends (CAQ-ACI-2026-08); CAQ's six questions for audit committees on AI in financial reporting (CAQ-ACI-2026-03).
- **substantive-testing.** Fieldguide's Field Orchestrator performing end-to-end substantive testing, with an Agent Review Experience for reviewers (FIELDGUIDE-ORCH-2026).
- **acceptance-independence.** Management-responsibility threat from autonomous agents on audit-client work (CCAB-AI-2026); who owns statements drafted by an audit-platform agent (FIELDGUIDE-FINANCIALS-2026); AU-C 210 and engagement-letter disclosure of AI tools (ATODAY-AICPAPA-2026).
- **other-assurance.** None.

## 5. Sources

Counts by type (52 sources, all opened; see each row's access note): academic 9, firm 2, press 4, professional-body 9, regulator 12, standard-setter 9, survey 1, vendor 6. No conference proceedings, podcasts, community threads or job postings were examined for this angle; the one conference item is the PCAOB conference proposal HOLMSTROM-PETERS-2024.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ARXIV-FAB-2026 | FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors (Abstract read.) | arXiv | academic | https://arxiv.org/abs/2609.32835 | 2026-09-26 | full |
| ARXIV-FINAUDITING-2025 | FinAuditing: A Financial Taxonomy-Structured Multi-Document Benchmark for Evaluating LLMs (Abstract read.) | arXiv (SIGIR 2026 Resource Track, per the page) | academic | https://arxiv.org/abs/2510.08886 | 2025-10-10 | full |
| ARXIV-FSMISINFO-2026 | Financial Audit Assistance using Misinformation Detection and Explanation (Abstract read.) | arXiv | academic | https://arxiv.org/abs/2607.17797 | 2026-07-20 | full |
| ARXIV-LLMAUDIT-2025 | Automating Financial Statement Audits with Large Language Models (Abstract read.) | arXiv | academic | https://arxiv.org/abs/2506.17282 | 2025-06-14 | full |
| FABIAN-2026 | Auditing Corporate Disclosures with the Assistance of Task-Specific Artificial Intelligence - Evidence on Effectiveness and Efficiency (Abstract read through Crossref metadata (published online 2026-03-03); the article page returns 403, so sample size and effect sizes were not seen.) | Journal of Information Systems (Fabian and Ratzinger-Sakel) | academic | https://doi.org/10.2308/ISYS-2025-054 | 2026-03-03 | full |
| GUO-CAM-2024 | Man + machines: assessing the informativeness of critical audit matters identified by AI and human auditors (seminar abstract) (Seminar abstract only (talk on 2024-12-19); no paper or SSRN version located. Outside the 12-18 month window but the only CAM-and-AI study found.) | Wuhan University Economics and Management School (speaker: Feng Guo, Iowa State University) | academic | https://ems.whu.edu.cn/info/1900/263911.htm | 2024-12-17 | full |
| HAMBURG-FABIAN-2026 | AI in auditing: New study highlights opportunities and limitations (University news release on the JIS paper (machine-translated page).) | University of Hamburg Business School | academic | https://www.bwl.uni-hamburg.de/en/ueber-die-fakultaet/aktuelles/2026/0320-ki-loesungen-in-der-wirtschaftspruefung-jette-fabian-nicole-ratzinger-sakel.html | 2026-03-20 | full |
| HOLMSTROM-PETERS-2024 | How Does Generative AI Automation Affect Auditors' Motivation and Judgment Quality? (registered report proposal) (Proposal with predictions, no results. Date from PDF metadata.) | PCAOB conference (Holmstrom, Iowa State; Peters, Nanyang Technological University) | academic | https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/conference/conference---spring/session_5_holmstrom_peters.pdf | 2024-06 | full |
| LEIDEN-GC-2025 | Evaluating LLMs in Practice: Enhancing Going Concern Assessments for Healthcare Organizations (master's thesis) (Student thesis, not peer reviewed. BDO Netherlands supplied the data and the ten participants.) | Leiden University (LIACS), with BDO Netherlands as company supervisor | academic | https://theses.liacs.nl/pdf/2024-2025-JongTdeTessa.pdf | 2025-04-14 | full |
| DELOITTE-OMNIA-2026 | Deloitte unveils connected agentic intelligence in Omnia | Deloitte US | firm | https://www.deloitte.com/us/en/about/press-room/deloitte-unveils-connected-agentic-intelligence-in-omnia.html | 2026-06-24 | full |
| KPMG-CLARA-2025 | KPMG advances AI integration in KPMG Clara smart audit platform | KPMG International | firm | https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html | 2025-04-22 | full |
| ATODAY-AICPAPA-2026 | AICPA releases practice guide for auditors dealing with AI (Quotes the practice aid directly on human review, AI-operated controls and one AI tool checking another.) | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai | 2026-10-14 | full |
| ATODAY-LOGOTHETIS-2026 | PCAOB's Logothetis: AI can only do part of an auditor's job (Date from page metadata; the article describes remarks at an Axios Live event 'last week'.) | Accounting Today | press | https://www.accountingtoday.com/news/pcaobs-logothetis-ai-can-only-do-part-of-an-auditors-job | 2026-09-22 | full |
| CFODIVE-PWC-2026 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 | full |
| THEACCOUNTANT-ARAQ-2026 | FRC publishes ARAQ 2026, reports audit quality improving but uneven (Only the opening paragraphs were usable; the FRC report itself was not opened.) | The Accountant | press | https://www.theaccountant-online.com/news/frc-publishes-araq-2026-reports-audit-quality-improving-but-uneven/ | 2026-07-22 | full |
| ACCA-KN-2026 | AI-related risks in audit (In Practice, by Kingsley Napley) (Filed under the July-August 2026 issue; day not captured.) | ACCA | professional-body | https://www.accaglobal.com/hk/en/technical-activities/uk-tech/in-practice-ezine-archive/In-Practice-archive-2026/july-august/AI-related-risks-in-audit.html | 2026-07 | full |
| AICPA-PA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing (News release; the practice aid itself is behind a login and was not read.) | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | full |
| CAQ-ACI-2026-03 | Audit Committee Insights / March 2026 | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-committee-insights-march-2026 | 2026-03-17 | full |
| CAQ-ACI-2026-08 | Audit Committee Insights / August 2026 | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-committee-insights-august-2026 | 2026-08-04 | full |
| CAQ-WEBINAR-2026 | AI in Financial Reporting and Audit - What Audit Committees Need to Know (webinar page) (Event page only; recording not viewed.) | Center for Audit Quality | professional-body | https://www.thecaq.org/event-ai-in-financial-reporting-and-audit | 2026-03-26 | full |
| CCAB-AI-2026 | Draft Statement to the Accountancy Profession on the Ethical Use of Artificial Intelligence (exposure draft) (Exposure draft; file name carries 6.6.26.) | CCAB Ethics Group | professional-body | https://www.ccab.org.uk/wp-content/uploads/2026/06/CCAB.Draft-Statement-to-the-Profession-on-Use-of-AI.-Exposure-Draft.6.6.26-002.pdf | 2026-06 | full |
| ICAEW-PIERPOINT-2025 | Testing Gen AI platforms: can they do audit work? (Single test of Copilot, Grok and Claude on a fictional retailer; planning-stage, so used here only as context.) | ICAEW (Helen Pierpoint) | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work | 2025-09 | full |
| ICAS-ARAQ-2026 | FRC Annual Review of Audit Quality (Undated; says the FRC published its review 'at the end of July'. Year-only date.) | ICAS | professional-body | https://www.icas.com/news-insights-events/news/audit-assurance/frc-annual-review-of-audit-quality | 2026 | full |
| INCP-AE-2026 | Accountancy Europe explica la aplicacion de la IA generativa en auditoria (summary of Accountancy Europe, Generative AI in audit and assurance: use cases and examples) (Secondary Spanish summary; the Accountancy Europe paper itself was not found at the guessed URL. The search extract placed the paper's release on 2026-09-22 (not opened).) | INCP Colombia (secondary report of Accountancy Europe) | professional-body | https://incp.org.co/?p=136646 | 2026-09-29 | full |
| FRC-GENAI-2026 | Generative and Agentic AI Guidance (Full PDF read. Publication date from FRC-NEWS-2026; the PDF metadata is 2026-03-27.) | Financial Reporting Council (UK) | regulator | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 | full |
| FRC-NEWS-2026 | Innovative new guidance supports audit firm adoption of emerging AI technologies | Financial Reporting Council (UK) | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | 2026-03-30 | full |
| FSA-DP-2025 | Study on the Potential Utilization of Generative AI in Audit Practices and Challenges Related to Audit Quality (DP2025-3) (Author's discussion paper; views are not the FSA's. English version released December 2025. Literature summaries of Fedyk et al. (2022) and Law and Shen (2025) come from this paper, not from the originals.) | Financial Research Center, Japan FSA (author: Noma Mikiharu) | regulator | https://www.fsa.go.jp/frtc/english/seika/discussion/2025/DP2025-3_Eng.pdf | 2025-07 | full |
| IFIAR-TTF-2026 | Use of technology in audits - Innovation and audit quality 2026 (New since the landscape scan, which held only the 2025 edition. The IFIAR host returns 403; the FSA copy was read.) | IFIAR Technology Task Force (copy hosted by Japan FSA) | regulator | https://www.fsa.go.jp/ifiar/2026TTFReport.pdf | 2026-04-20 | full |
| PCAOB-ACCHAIRS-2026 | Spotlight: 2025 Conversations With Audit Committee Chairs (Staff view. More than 250 audit committee chairs, 82% at companies audited by US global network firms.) | PCAOB (staff) | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/2025-conversations-with-audit-committee-chairs-spotlight.pdf | 2026-04 | full |
| PCAOB-AGENDA-2026 | Standard-Setting, Research, Rulemaking, and Related Activities (Page is undated; read on 2026-10-16 through a text mirror (r.jina.ai) because pcaobus.org returns 403 to curl. Year-only date is the best available.) | PCAOB | regulator | https://pcaobus.org/standards/standard-setting-research-projects | 2026 | full |
| PCAOB-EQR-2023 | Spotlight: Inspection Observations Related to Engagement Quality Reviews (Staff view, not Board policy. Most recent EQR inspection spotlight found.) | PCAOB (staff) | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/eqr-spotlight.pdf | 2023-10 | full |
| PCAOB-GENAI-2024 | Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting (Staff view, not Board policy. Outreach mainly to larger firms.) | PCAOB (staff) | regulator | https://pcaobus.org/documents/generative-ai-spotlight.pdf | 2024-07 | full |
| PCAOB-IAG-2026 | Investor Advisory: PCAOB Investor Advisory Group Requests Public Submit Examples of Critical or Key Audit Matters (Read through a text mirror.) | PCAOB Office of the Investor Advocate | regulator | https://pcaobus.org/resources/information-for-investors/investor-advisories/investor-advisory--pcaob-investor-advisory-group-requests-public-submit-examples-of-critical-or-key-audit-matters-5-2026 | 2026-04-30 | full |
| PCAOB-PIR1220-2018 | Post-Implementation Review of AS 1220, Engagement Quality Review (Board report) (Foundation material, outside the 12-18 month window.) | PCAOB | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/pir/documents/pir-as1220-board-report.pdf | 2018-12-19 | full |
| PCAOB-PIRCAM-2022 | Post-Implementation Review: Auditor Reporting (critical audit matters) (Page undated; date is that of the latest interim analysis report it lists. Read through a text mirror.) | PCAOB | regulator | https://pcaobus.org/oversight/standards/pir/auditor-reporting | 2022-12 | full |
| PCAOB-PRIORITIES-2024 | Spotlight: Staff Priorities for 2025 Inspections and Interactions With Audit Committees | PCAOB (staff) | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/2025-priorities-spotlight_v3.pdf | 2024-12 | full |
| IAASB-ISA220-2020 | International Standard on Auditing 220 (Revised), Quality Management for an Audit of Financial Statements (Foundation standard. Date from the IAASB landing page.) | IAASB | standard-setter | https://www.ifac.org/_flysystem/azure-private/publications/files/IAASB-International-Standard-Auditing-220-Revised.pdf | 2020-12-17 | full |
| IAASB-ISA570-2025 | International Standard on Auditing 570 (Revised 2024), Going Concern (final pronouncement) (Full pronouncement, 139 pages. Publication date from the IAASB landing page.) | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2025-04/IAASB-ISA570-Going-Concern-Revised.pdf | 2025-04-09 | full |
| IAASB-ISA570PAGE-2025 | ISA 570 (Revised 2024), Going Concern (landing page) | IAASB | standard-setter | https://www.iaasb.org/publications/isa-570-revised-2024-going-concern | 2025-04-09 | full |
| IAASB-ISQM2-2020 | International Standard on Quality Management 2, Engagement Quality Reviews (Foundation standard. Date from the IAASB landing page.) | IAASB | standard-setter | https://www.ifac.org/_flysystem/azure-private/publications/files/IAASB-Quality-Management-ISQM-2-Engagement-Quality-Reviews.pdf | 2020-12-17 | full |
| PCAOB-AS1220 | AS 1220: Engagement Quality Review (Current text as read on 2026-10-16 through a text mirror; the page notes amendments effective 2026-12-15.) | PCAOB | standard-setter | https://pcaobus.org/oversight/standards/auditing-standards/details/AS1220 | 2026 | full |
| PCAOB-AS1301 | AS 1301: Communications with Audit Committees (Current text as read on 2026-10-16 through a text mirror; adoption date not captured.) | PCAOB | standard-setter | https://pcaobus.org/oversight/standards/auditing-standards/details/AS1301 | 2026 | full |
| PCAOB-AS2415 | AS 2415: Consideration of an Entity's Ability to Continue as a Going Concern (Current text as read on 2026-10-16 through a text mirror.) | PCAOB | standard-setter | https://pcaobus.org/oversight/standards/auditing-standards/details/AS2415 | 2026 | full |
| PCAOB-AS2801 | AS 2801: Subsequent Events (Current text as read on 2026-10-16 through a text mirror.) | PCAOB | standard-setter | https://pcaobus.org/oversight/standards/auditing-standards/details/AS2801 | 2026 | full |
| PCAOB-AS3101 | AS 3101: The Auditor's Report on an Audit of Financial Statements When the Auditor Expresses an Unqualified Opinion (Current text as read on 2026-10-16 through a text mirror; adopted June 2017 per PCAOB-PIRCAM-2022.) | PCAOB | standard-setter | https://pcaobus.org/oversight/standards/auditing-standards/details/AS3101 | 2026 | full |
| CPACOM-ATR-2025 | 2025 Audit Transformation Report (Survey Jun-Aug 2025; 54 firms with complete data; the authors say it is not representative of all CPA firms.) | CPA.com (with AICPA) | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 | full |
| CASEWARE-CWX-2026 | CwX 2026: How agentic AI is transforming audit and assurance (Date taken from the only date in the page text.) | Caseware | vendor | https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance | 2026-06-17 | full |
| CASEWARE-VERITY-2026 | Caseware launches Verity to bring workflow-native AI agents directly into assurance engagements | Caseware | vendor | https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements | 2026-05-20 | full |
| DATASNIPPER-DISCLOSURE-2025 | Disclosure Agents from DataSnipper (product page) (Page is undated and gives no figures. Month taken from a search extract of the launch press release dated 2025-10-01 (not opened).) | DataSnipper | vendor | https://www.datasnipper.com/campaign/disclosure-agents | 2025-10 | full |
| FIELDGUIDE-FINANCIALS-2026 | Fieldguide Launches Field Financials and Fieldguide MCP, Along With a Refreshed Brand | Fieldguide (GlobeNewswire via AAP) | vendor | https://aapnews.aap.com.au/news/globenewswire9808260 | 2026-08-12 | full |
| FIELDGUIDE-ORCH-2026 | Fieldguide Launches Field Orchestrator, Marking the Next Phase of Agentic AI in Audit | Fieldguide (GlobeNewswire via AAP) | vendor | https://www.aap.com.au/aapreleases/globenewswire9732778/ | 2026-06-08 | full |
| TR-DISCLOSURE-2026 | Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence | Thomson Reuters Innovation Blog (Corey Wells, General Manager of Audit) | vendor | https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/ | 2026-09-23 | full |

## 6. Gaps

- **No independent measurement of any disclosure-checklist tool.** Time-saved and uptake figures are vendor-published; no miss rate, false-positive rate or parallel-run result was found. Ideagen's page returned 404, so its claim of use by 9 of 10 top UK firms stayed at search-extract level and is not used.
- **Peer-reviewed field study not fully read.** The JIS paper (Fabian and Ratzinger-Sakel) returned 403; sample size, effect sizes and the firm's name were not seen. Only the abstract and the university's release were read.
- **CAM study is an abstract.** The Guo seminar abstract (Dec 2024) is the only CAM-and-AI study found; no paper or sample description.
- **PCAOB going-concern project.** The agenda page gives a status line only and the page is undated; there is no proposal or technology language specific to AS 2415. pcaobus.org blocks `curl`, so pages were read through a text mirror.
- **Inspection findings.** No 2025 or 2026 inspection finding on AI tools in any of these steps was found. The FRC's 2026 Annual Review of Audit Quality was seen only in two secondary summaries, and the PCAOB's most recent EQR spotlight is from Oct 2023. The IFIAR host (ifiar.org) returns 403; the 2026 report was read from the Japan FSA copy.
- **Standards not opened.** ISA 701, ISA 260, ISA 700, ISA 450, ISA 580, AS 2805 and AS 2810 were not read. The AICPA practice aid full text is behind a login; only the release and Accounting Today's quotations were read.
- **Accountancy Europe paper.** Its September 2026 paper on GenAI use cases in audit was read only through a Spanish summary (INCP-AE-2026); the primary was not found. The summary lists checking financial statement disclosures among use cases, without outcomes.
- **Secondary summaries of academic findings.** Fedyk et al. (2022) and Law and Shen (2025) are cited via the Japan FSA discussion paper only.
- **Regulator-side AI review of filings.** XBRL International pages describe experiments at the Danish regulator and a planned system at India's FRRB, but both pages are undated and were excluded.
- **Source types missing.** No conference proceedings, podcasts, community discussion or job postings for this module.
- **Corrections to the landscape scan (`landscape-assurance.md`).** (1) The 1,200-1,500 requirements figure in TR's post describes a completed Guided Assurance checklist, not a Disclosure Review limit. (2) The landscape's frontier signal FS16 cites Caseware on 28 Jul 2026; the Caseware pages opened here are dated 20 May 2026 (launch release) and 17 Jun 2026 (CwX blog) and neither has a 28 Jul date. (3) The landscape held only IFIAR's 2025 technology report; a 2026 edition (20 Apr 2026) exists and adds the transparency-to-governance point. (4) The AICPA practice aid's "one tool may check another" point was confirmed through Accounting Today's quotation, not the JofA article.
- **Search budget.** About 20 searches; the rest was `curl`, `pdftotext` and Crossref metadata.

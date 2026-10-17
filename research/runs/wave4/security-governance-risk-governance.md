# Security x governance-risk: governance angle (wave 4)

Compiled 2026-10-17. Archetype `security`, module `governance-risk` (landscape name: security-governance-risk). Angle: governance and evidence (regulators, standard-setters, professional bodies, academic work, surveys). Method: pages opened with curl or the r.jina.ai mirror, PDFs read with pdftotext; web search used 4 times (CISA agentic guidance coverage, questionnaire-automation cases, FAIR/risk quantification, DORA critical provider list). Source refs follow `PUBLISHER-SHORT-YYYY`; where the practice-angle file for this module already uses a ref I reused it.

## 1. Summary

**What the governance evidence says.** Regulators and standard-setters now treat AI in security as two linked jobs: using AI inside the security function, and governing the AI that the business and the security team run. NIST's draft Cyber AI Profile (IR 8596, 2025-12-16) lists AI-enabled defence opportunities in compliance assessment, policy enforcement and executive risk communication, and sits beside the SP 800-53 overlays being written for AI systems and agents. Joint CISA, NSA and partner guidance on agentic AI (2026-05-01) asks organisations to limit agent autonomy and access. In the EU the AI Act has been applicable since 2026-08-02 with the Annex III high-risk duties moved to 2027-12-02, while NIS2 (top-management accountability) and DORA (ICT third-party oversight, with the first critical-provider list published 2025-11-18) already bind many security teams. In the US, the March 2026 Cyber Strategy says it will streamline cyber regulation and an April 2026 trade-association letter asks the SEC to rescind Item 106, while FINRA's 2026 report sets out supervision, logging and human-in-the-loop considerations for GenAI and agents.

**Where AI is changing the work.** The best-documented changes are customer assurance (questionnaire answering) and continuous compliance evidence collection, each supported only by vendor-published, customer-named case studies. Policy-versus-standard gap analysis, AI-assisted expert elicitation for risk quantification and guardrails for SOC agents have independent lab measurements but no deployments. Board reporting, regulator-notification drafting and supplier-assurance review appear only as opportunities in standards and practitioner talks.

**Evidence quality.** There is no published error rate, override rate, parallel run, auditor-reliance study or inspection finding for AI used in GRC work. The only independent quantitative evidence is three academic lab results (ReCon policy-gap benchmark, Scalable Delphi, a guardrail proxy). Surveys (ISACA, ISC2, SANS/GIAC, PwC, WEF, FAIR Institute, Splunk) show wide adoption and thin governance: for example ISACA reports 8% of organisations regularly run AI-specific response exercises, and SANS reports 79% of SOCs use AI but 36% have a defined workflow.

**Use-case count.** 14 candidate use cases: 3 grade A, 0 grade B, 6 grade C, 5 grade D (idea). No grade B appears because every named deployment found comes with a published figure. All grade-A figures are vendor-published on the vendor's own site. Independent academic benchmarks are graded C because the scale has no slot for a lab benchmark of an in-module task (see the note on use case 04).

**Terminology note.** On the retrieved copy of the NIST IR 8596 page, an announcement says NIST is updating its communications to use "super intelligence" as directed by a 2026-09-29 executive order, and the NIST CAISI page title uses the same term. The documents themselves still say "AI". I record this as observed and used "AI" throughout.

## 2. Use cases

```yaml
- id: security-governance-risk-01
  title: Automated answering of inbound customer security questionnaires, with human review
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - document-production
  - client-interaction
  pattern: grounded-knowledge-assistant
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Customers send long security and AI-data-handling questionnaires before buying. After GitHub launched Copilot, the customer assurance team faced a surge of more than 300 questionnaires in a short period that it did not think it could answer by hand, which risked slowing sales and adoption.
  solution: Questionnaire automation answers inbound questionnaires from the company's own knowledge base, and a Trust Center publishes data-use and retention practices in plain language so fewer questionnaires are sent at all. The vendor describes the result as a human-reviewable customer assurance program. Synthesia also lets a Trust Center AI agent field inbound security questions before they reach the security team.
  outcomes:
  - lever: speed
    description: Inbound questionnaires automated within six months of starting, against GitHub's own 12-month goal
    figure: 93%
    measures: '''93% of inbound questionnaires automated in 6 months'' (the page states the 12-month goal; the count of questionnaires behind the percentage is not stated, and ''more than 300'' refers to the initial surge)'
    provenance: vendor-published
    source_ref: VANTA-GITHUB-2026
  - lever: capacity
    description: Share of customer questions resolved through self-service or the AI agent at Synthesia
    figure: 20-30%
    measures: '''20-30% of customer questions resolved through self-service or AI agent'' (denominator: customer questions received; count not stated)'
    provenance: vendor-published
    source_ref: VANTA-SYNTHESIA-2026
  prerequisites:
  - A maintained internal knowledge base of approved answers and policies that the automation draws on (GitHub)
  - A Trust Center or equivalent self-service publication point
  - A customer-assurance function that owns the answers (GitHub's Director of Customer Assurance is quoted on the page)
  risks_and_guardrails:
  - Answers are statements made to customers about security controls, so errors carry contractual and reputational risk; no source reports an error or override rate (VANTA-GITHUB-2026, whole page).
  - CSA's AI Controls Matrix ships an AI-specific questionnaire (AI-CAIQ) that buyers can use to evaluate vendors, which standardises what the answers must cover (CSA-AICM-2026, 'What's Included').
  - The only peer-reviewable work found on questionnaire automation reports 'improved accuracy' without figures in its abstract (ARXIV-2412.13988, abstract).
  human_checkpoints:
  - The vendor describes the program as human-reviewable (VANTA-GITHUB-2026, TL;DR); the review procedure and sampling rate are not described
  role_evolution: The GitHub page says automation freed the team to focus on higher-value work and Synthesia says its Trust Center cuts the number of questions reaching the security team; neither gives headcount figures.
  evidence_grade: A
  sources:
  - ref: VANTA-GITHUB-2026
    title: GitHub accelerates sales by automating 93% of security questionnaires with Vanta (customer case study; date is sitemap last-modified, original date not stated)
    publisher: Vanta
    type: vendor
    url: https://www.vanta.com/customers/github
    date: 2026-03
    access: full
    locator: TL;DR; 'The challenge'; 'The Vanta impact' ROI list
  - ref: VANTA-SYNTHESIA-2026
    title: How Synthesia became the first AI video company certified against ISO 42001, with a two-person team (customer case study; date is month of sitemap last-modified)
    publisher: Vanta
    type: vendor
    url: https://www.vanta.com/customers/synthesia
    date: 2026-10
    access: full
    locator: '''Vanta impact'': Trust Center Pro bullets'
  - ref: CSA-AICM-2026
    title: AI Controls Matrix v1.1
    publisher: Cloud Security Alliance
    type: standard-setter
    url: https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1
    date: '2026-06-22'
    access: full
    locator: '''What''s Included in this Download'': AI-CAIQ'
  - ref: ARXIV-2412.13988
    title: RAG for Effective Supply Chain Security Questionnaire Automation (QuestSecure)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2412.13988
    date: '2024-12-18'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-17'
  notes: Both outcome figures are published by the vendor on its own site and quote the customer; no independent measurement, accuracy audit or override rate exists in what I found. The GitHub page carries no publication date (sitemap last-modified 2026-03-17; customer since 2024). Practice-angle detail on vendors is in the practice file for this module.
- id: security-governance-risk-02
  title: Continuous compliance evidence collection and multi-framework control monitoring
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: A lean security team has to prove control operation for several frameworks at once (ISO 27001, SOC 2, HITRUST and the new ISO 42001), which was manual, fragmented and had no central record before the tool.
  solution: A compliance platform connects to 50-60 systems and collects evidence automatically, while an AI agent maintains policies, evaluates evidence and guides remediation, so one team runs six frameworks from one place.
  outcomes:
  - lever: capacity
    description: Share of evidence collection automated at Synthesia across connected systems
    figure: 60%
    measures: '''60% of evidence collection automated across 50-60 connected systems'' (denominator: Synthesia''s evidence-collection work; counts not stated)'
    provenance: vendor-published
    source_ref: VANTA-SYNTHESIA-2026
  - lever: speed
    description: Audit cycles for five frameworks condensed into a one-month window
    figure: 5 cycles in 1 month
    measures: '''Five framework audit cycles condensed into a one-month window'' (baseline duration not stated)'
    provenance: vendor-published
    source_ref: VANTA-SYNTHESIA-2026
  prerequisites:
  - Integrations to the systems that hold evidence (50-60 at Synthesia)
  - Scoping decision on which frameworks to certify
  - An external audit partner (the page names A-LIGN as partner)
  risks_and_guardrails:
  - NIST's draft Cyber AI Profile says human oversight will be required to maintain regulatory and legal compliance, even where AI supports compliance monitoring (NIST-CYBERAI-2025, GV.OC-03 row).
  - No source reports whether auditors rely on, sample or re-perform automated evidence, or how often evidence is wrong; the absence of audit-side evidence is the main gap.
  human_checkpoints:
  - Control owners remediate gaps the agent flags
  - External auditors issue the certifications
  role_evolution: The two-person security team runs six frameworks 'without adding headcount to match the company's scale' (vendor wording); no separate role change is reported.
  evidence_grade: A
  sources:
  - ref: VANTA-SYNTHESIA-2026
    title: How Synthesia became the first AI video company certified against ISO 42001, with a two-person team (customer case study; date is month of sitemap last-modified)
    publisher: Vanta
    type: vendor
    url: https://www.vanta.com/customers/synthesia
    date: 2026-10
    access: full
    locator: '''Vanta impact'': Multi-framework compliance management and Vanta AI bullets'
  - ref: NIST-CYBERAI-2025
    title: Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile), NIST IR 8596 initial preliminary draft
    publisher: NIST
    type: standard-setter
    url: https://csrc.nist.gov/pubs/ir/8596/iprd
    date: '2025-12-16'
    access: full
    locator: GV.OC-03 row, general considerations (p. 17 of the draft)
  last_reviewed: '2026-10-17'
  notes: Vendor-published case study on the vendor's own site; the figures are not independent. Synthesia is itself an AI company, so its ISO 42001 use is partly a market signal. The page is dated only by sitemap (last-modified 2026-10-08). Overlaps the practice-angle file; kept here because the regulatory and standards context belongs to the governance angle.
- id: security-governance-risk-03
  title: Mapping controls and obligations across frameworks and regulations with an LLM
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - research-synthesis
  - document-production
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Matching one framework's controls to another's (or to a regulation) is done by hand; the Synthesia case study puts matching 500+ HITRUST controls at 1.5 months of manual work.
  solution: At Synthesia the compliance platform's MCP server integration was used to match controls for a HITRUST implementation roadmap instead of mapping by hand. NIST's draft profile lists 'identifying and mapping similar concepts between documents' as a defensive use of AI. A Ukrainian case study proposes a retrieval-augmented advisor that builds target security profiles from national regulations and organisational policies.
  outcomes:
  - lever: speed
    description: Control matching across HITRUST controls that the page says would have taken 1.5 months by hand
    figure: 500+ controls
    measures: '''Automated control matching across 500+ HiTrust controls'', compared with a stated 1.5 months manually (no measured elapsed time for the automated run is given)'
    provenance: vendor-published
    source_ref: VANTA-SYNTHESIA-2026
  - lever: speed
    description: HITRUST implementation timeline
    figure: 18 months to about 3 months
    measures: '''Reduced an 18-month manual implementation timeline to approximately 3 months'' (the whole implementation, not only the matching step; the page does not say how much of the reduction came from AI)'
    provenance: vendor-published
    source_ref: VANTA-SYNTHESIA-2026
  prerequisites:
  - Machine-readable control sets for the source and target frameworks
  - Access to the compliance platform's MCP server (Synthesia)
  risks_and_guardrails:
  - A mapping is an interpretation; wrong mappings propagate into audit scope. The Ukrainian proposal claims RAG reduces human error but reports no measurement (ARXIV-2604.06274, abstract).
  - EU AI Act, NIS2, DORA and state-level US rules overlap and conflict; a Gartner analyst advises building a baseline from shared principles (safety, transparency, accountability, privacy, security) rather than complying with each rule separately (TECHTARGET-AIREG-2026, sections 'Ground AI strategy' and 'Cybersecurity resilience').
  human_checkpoints:
  - A control owner confirms each proposed mapping before it enters the scope document (inferred from NIST's human-oversight statement; the Synthesia page does not describe the review step)
  role_evolution: Not described in the sources beyond Synthesia's statement that a two-person team handles six frameworks.
  evidence_grade: A
  sources:
  - ref: VANTA-SYNTHESIA-2026
    title: How Synthesia became the first AI video company certified against ISO 42001, with a two-person team (customer case study; date is month of sitemap last-modified)
    publisher: Vanta
    type: vendor
    url: https://www.vanta.com/customers/synthesia
    date: 2026-10
    access: full
    locator: '''Vanta impact'': MCP Server integration bullet'
  - ref: NIST-CYBERAI-2025
    title: Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile), NIST IR 8596 initial preliminary draft
    publisher: NIST
    type: standard-setter
    url: https://csrc.nist.gov/pubs/ir/8596/iprd
    date: '2025-12-16'
    access: full
    locator: GV.OC-03 row, Defend column, sample opportunities (p. 17)
  - ref: ARXIV-2604.06274
    title: Towards the Development of an LLM-Based Methodology for Automated Security Profiling in Compliance with Ukrainian Cybersecurity Regulations
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2604.06274
    date: '2026-04-07'
    access: full
    locator: Abstract
  - ref: TECHTARGET-AIREG-2026
    title: How to prepare security controls for future AI regulations (opinion by Gartner VP analyst Bernard Woo)
    publisher: TechTarget SearchSecurity
    type: press
    url: https://www.techtarget.com/cybersecurity/opinion/How-to-prepare-security-controls-for-future-AI-regulations
    date: '2026-06-02'
    access: full
    locator: Sections 'Ground AI strategy with risk-based principles' and 'Cybersecurity resilience for AI risks'
  last_reviewed: '2026-10-17'
  notes: Grade A rests on a single vendor-published case study. The review step is not described in the source, so the human checkpoint above is an inference from NIST's general statement and is flagged as such.
- id: security-governance-risk-04
  title: LLM gap analysis of security policies against a standard (ISMS audit preparation)
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - review-assurance
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Security policy documents are often incomplete against standards and regulations and are only found wanting in a thorough audit. Finding the gaps takes extensive manual effort, and experienced reviewers are scarce, particularly for small organisations.
  solution: Retrieval-augmented small open-weight models, run locally on CPU, judge each ISO/IEC 27002:2022 control as conformity or non-conformity against the policy text and write a justification. The authors position this as an assistant to the human auditor or to the policy owner before an audit.
  outcomes:
  - lever: quality
    description: Best model's mean agreement with the human expert determination of conformity
    figure: 80.65%
    measures: Mean agreement (verdict matched the human expert label) for Granite4.1:8B across retrieval configurations; 93 ISO/IEC 27002:2022 controls x 3 policy datasets; 8 open-weight models, 288 model-and-retrieval configurations, 26,784 evaluations
    provenance: independent
    source_ref: ARXIV-2607.22885
  - lever: quality
    description: Best model's chance-corrected agreement
    figure: balanced accuracy 75.0%, Cohen's kappa 0.528, MCC 0.548
    measures: Balanced accuracy, kappa and MCC for Granite4.1:8B against human expert consensus (Table 5); one of the three datasets is 100% conformity, so plain accuracy is not used as the headline
    provenance: independent
    source_ref: ARXIV-2607.22885
  - lever: quality
    description: Weakest models
    figure: balanced accuracy 52.4-59.9% (four of eight models)
    measures: Balanced accuracy for Gemma3n, Gemma3, Mistral and Phi4 (kappa as low as 0.038-0.163), same benchmark
    provenance: independent
    source_ref: ARXIV-2607.22885
  prerequisites:
  - The policy set in text form and the standard's control text as checklist
  - A human-labelled sample to calibrate the chosen model (the benchmark used human expert consensus)
  risks_and_guardrails:
  - Models stated that policies mentioned items they did not (for example data masking) and confused the requirement text in the prompt with policy evidence (ARXIV-2607.22885, qualitative error analysis).
  - 'Confidence scores tracked the verdict, not certainty: non-conformity answers got 30 and conformity answers 90 or 95, so they cannot be used to route items for review (same section).'
  - The benchmark tests policy documents only; it does not test whether controls operate.
  human_checkpoints:
  - Auditor or policy owner confirms every non-conformity and a sample of conformities; the authors frame the tool as an assistant, not a replacement
  role_evolution: The authors say one auditor could analyse several policy sets instead of one and that repetitive review fatigue falls; this is their expectation, not a measured effect (ARXIV-2607.22885, Conclusion).
  evidence_grade: C
  sources:
  - ref: ARXIV-2607.22885
    title: 'ReCon: A Resource-Constrained Benchmark for LLM-Based Cybersecurity Compliance Across Ingestion and Retrieval Pipelines (Negi et al., IIT Kanpur and IIIT Hyderabad)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2607.22885
    date: '2026-07-24'
    access: full
    locator: Abstract; Section 4.1; Section 5.1 Table 5; Section 5.2; qualitative analysis (pp. 14-17); Conclusion
  - ref: NIST-CYBERAI-2025
    title: Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile), NIST IR 8596 initial preliminary draft
    publisher: NIST
    type: standard-setter
    url: https://csrc.nist.gov/pubs/ir/8596/iprd
    date: '2025-12-16'
    access: full
    locator: Section 2.1.2, 'Supporting automated policy enforcement and compliance assessments' (p. 10)
  last_reviewed: '2026-10-17'
  notes: Measured independently (academic lab), but it is a benchmark, not a deployment by a named organisation, so I graded it C (no deployment found) rather than A or B; the grading scale has no slot for an independent academic benchmark of an in-module task. Sample is small (3 policy datasets). arXiv preprint, not peer reviewed as of retrieval. A model-comparison inconsistency exists in the paper's own prose (it says the remaining models score below 60%, while Table 5 shows Granite3.3, Granite4.1:3B and Llama3.2 above); I used the table.
- id: security-governance-risk-05
  title: 'Post-incident policy gap analysis: map log evidence to ATT&CK and test policy adequacy'
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - research-synthesis
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: Post-incident reviews that find control and policy failures are labour-intensive, slow and depend on expert judgment.
  solution: 'A multi-agent pipeline ingests log data, maps observed behaviour to MITRE ATT&CK and evaluates the organisation''s policies for adequacy, then proposes remediation with evidence-to-policy traceability. Idea stage: a proof of concept on one simulated brute-force scenario.'
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: the abstract reports qualitative results on one simulated scenario (a brute-force attack on a Windows OpenSSH service) and no figures
    provenance: independent
    source_ref: ARXIV-2601.03287
  prerequisites:
  - Log data in a form the pipeline can ingest
  - Policies in searchable text form
  risks_and_guardrails:
  - The authors stress continued human oversight for high-stakes decisions (ARXIV-2601.03287, abstract).
  human_checkpoints:
  - Reviewer approves any policy change or remediation recommendation
  role_evolution: Not discussed.
  evidence_grade: D
  sources:
  - ref: ARXIV-2601.03287
    title: Automated Post-Incident Policy Gap Analysis via Threat-Informed Evidence Mapping using Large Language Models
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2601.03287
    date: '2026-01-04'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-17'
  notes: 'Idea: researchers discuss it; no deployment found. Only the abstract was read.'
- id: security-governance-risk-06
  title: LLM-assisted expert elicitation and scenario modelling for cyber risk quantification
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: personal-assistant
  maturity: piloting
  problem: Quantitative risk estimates rest on structured expert elicitation such as the Delphi method, which needs months of coordination and specialist time, so rigorous estimates are out of reach for most decisions. Survey respondents also name poor communication between departments and gaps between silos as the top obstacles to cyber risk programs.
  solution: Replace or supplement the human expert panel with LLM personas that estimate, iterate and share rationales, so the estimate is cheap, auditable and can be rerun when evidence or assumptions change. In practice, survey respondents report AI use in risk programs, and name automated risk quantification among the areas where AI delivers most value.
  outcomes:
  - lever: quality
    description: LLM-panel estimates against ground truth on verifiable proxies
    figure: Pearson r = 0.91-0.98
    measures: Correlation with ground truth across two domains (one is AI-augmented cybersecurity risk), three benchmarks and three reproduced expert studies, as stated in the abstract; the paper also reports agreement with expert panels 'on most quantities'
    provenance: independent
    source_ref: ARXIV-2602.08889
  - lever: capacity
    description: Organisations using or experimenting with AI in their cyber risk programs
    figure: 80% (37% using, 43% experimenting)
    measures: Share of 400 surveyed cyber risk leaders and practitioners; 60% of those not yet using AI expect implementation within twelve months
    provenance: independent
    source_ref: FAIR-SOCRM-2026
  prerequisites:
  - A defined risk taxonomy and scenario library (58% of respondents use or plan to use FAIR)
  - Calibration against verifiable proxies before trusting estimates
  risks_and_guardrails:
  - Target quantities are unobservable by construction, so the authors validate through necessary conditions (accuracy and calibration on proxies, sensitivity to evidence) rather than direct truth (ARXIV-2602.08889, abstract).
  - The survey comes from an institute that promotes quantification and the summary page does not describe how respondents were sampled, so adoption levels may not represent the general market (FAIR-SOCRM-2026).
  human_checkpoints:
  - Risk owner reviews rationales and revision history before an estimate is used in a decision
  role_evolution: Risk analysts shift from convening panels to curating evidence and challenging model rationales (authors' framing of auditable rationales; not measured).
  evidence_grade: C
  sources:
  - ref: ARXIV-2602.08889
    title: 'Scalable Delphi: Large Language Models for Structured Risk Estimation (Lorenz and Fritz)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2602.08889
    date: '2026-02-09'
    access: full
    locator: Abstract
  - ref: FAIR-SOCRM-2026
    title: What 400 Cyber Risk Leaders Told Us About the Future of Cyber Risk Management (2026 State of Cyber Risk Management report summary)
    publisher: FAIR Institute
    type: professional-body
    url: https://www.fairinstitute.org/blog/what-400-cyber-risk-leaders-told-us-about-the-future-of-cyber-risk-management
    date: '2026-06-04'
    access: full
    locator: Findings 1, 3, 4 and 8
  last_reviewed: '2026-10-17'
  notes: 'Pattern is ''other'': structured expert elicitation by an LLM panel. No named-organisation deployment found. Survey also reports that 71% of AI-integrated organisations describe a proactive posture versus 52% of those not using AI; this is a correlation in a self-reported survey and is not used as an outcome. Scalable Delphi first appeared 2026-02-09 and was revised on 2026-10-01.'
- id: security-governance-risk-07
  title: Translating technical risk data into board and executive language
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - document-production
  - data-reporting
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Gartner analysts told CISOs that many board reports are structured around cybersecurity, not the business, and that a CISO may get only five to ten minutes to present. Boards have, in their words, viewed cybersecurity as a regulatory checklist or attestation.
  solution: NIST's draft Cyber AI Profile lists 'risk communication and executive decision support' (helping CISOs translate risk to business language) as a defensive use of AI. Gartner's session proposes a board report modelled on a financial statement (balance sheet, income statement, cash flow, narrative), a format an assistant could populate and draft.
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure found for this use
    provenance: independent
    source_ref: NIST-CYBERAI-2025
  prerequisites:
  - A stable, minimal set of indicators per report section, kept consistent across periods (Gartner)
  - Agreed risk appetite and tolerance thresholds
  risks_and_guardrails:
  - NIST says AI-generated reports should be reviewed by a human before they change organisational risk management (NIST-CYBERAI-2025, GV.OV-03 row, p. 28).
  - 'Board context is moving: a survey cited by Gartner found 71% of board members willing to accept more cyber risk for business goals, so reports that merely scare will lose influence (TECHTARGET-CISO-2026).'
  human_checkpoints:
  - CISO reviews and owns every board paper; circulate the framework to key leaders before use (TECHTARGET-BOARD-2026)
  role_evolution: Gartner expects business acumen to be the main differentiator of high-performing CISOs by 2028 (a Gartner prediction, quoted by TechTarget); reporting becomes a business-leadership task rather than a technical one.
  evidence_grade: D
  sources:
  - ref: NIST-CYBERAI-2025
    title: Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile), NIST IR 8596 initial preliminary draft
    publisher: NIST
    type: standard-setter
    url: https://csrc.nist.gov/pubs/ir/8596/iprd
    date: '2025-12-16'
    access: full
    locator: Section 2.1.2, 'Risk communication and executive decision support' (p. 11)
  - ref: TECHTARGET-BOARD-2026
    title: 'Lost in translation: Cybersecurity board reporting for CISOs (Gartner Security & Risk Management Summit session)'
    publisher: TechTarget SearchSecurity
    type: press
    url: https://www.techtarget.com/cybersecurity/news/366643884/Lost-in-translation-Cybersecurity-board-reporting-for-CISOs
    date: '2026-06-03'
    access: full
    locator: Sections 'Know your audience' and 'Use financial reports as templates'
  - ref: TECHTARGET-CISO-2026
    title: CISO role changes as cyber-risk appetites in the C-suite grow (Gartner Security & Risk Management Summit session)
    publisher: TechTarget SearchSecurity
    type: press
    url: https://www.techtarget.com/cybersecurity/news/366644003/CISO-role-changes-as-cyber-risk-appetites-in-the-C-suite-grow
    date: '2026-06-08'
    access: full
    locator: Sections 'The security drag' and 'A new mandate for CISOs'
  - ref: FAIR-SOCRM-2026
    title: What 400 Cyber Risk Leaders Told Us About the Future of Cyber Risk Management (2026 State of Cyber Risk Management report summary)
    publisher: FAIR Institute
    type: professional-body
    url: https://www.fairinstitute.org/blog/what-400-cyber-risk-leaders-told-us-about-the-future-of-cyber-risk-management
    date: '2026-06-04'
    access: full
    locator: Finding 5 (board use of cyber risk information)
  last_reviewed: '2026-10-17'
  notes: 'Idea: regulators and analysts discuss it; I found no named deployment or measured result. Context figures (not outcomes): per Gartner 93% of board members agree cyber risk threatens shareholder value, 98% expect threats to grow (TECHTARGET-BOARD-2026); per the FAIR survey of 400, 97% have defined risk appetite, 89% have it board-approved, 63% report active board use of cyber risk information.'
- id: security-governance-risk-08
  title: Drafting incident reports, compliance reports and audit evidence packs
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Regulators require incident notification and disclosure (NIS2 requires medium and large entities in covered sectors to notify authorities of significant incidents; DORA sets ICT incident reporting for financial entities; the US SEC rules cover Form 8-K Item 1.05), and audits require organised evidence, all of which analysts assemble by hand.
  solution: NIST's draft profile says AI can support reporting by drafting clear incident summaries and compliance reports, organising evidence and producing standardised documentation to reduce analyst workload.
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure found for this use
    provenance: independent
    source_ref: NIST-CYBERAI-2025
  prerequisites:
  - Structured incident and evidence records
  - Templates that match the regulator's required fields
  risks_and_guardrails:
  - 'NIST: AI-generated reports should undergo human review for content before any change to organisational risk management (NIST-CYBERAI-2025, GV.OV-03 row, p. 28).'
  - 'The US disclosure rules may change: industry groups asked the SEC in April 2026 to rescind Item 106 and narrow the incident disclosure mandate; no final SEC action was found (SIFMA-SEC-2026), while EU duties continue (EC-NIS2, EIOPA-DORA-2025).'
  human_checkpoints:
  - Named accountable executive signs every regulatory notification and disclosure; NIS2 makes top management accountable for non-compliance with risk-management measures (EC-NIS2)
  role_evolution: Not discussed in the sources.
  evidence_grade: D
  sources:
  - ref: NIST-CYBERAI-2025
    title: Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile), NIST IR 8596 initial preliminary draft
    publisher: NIST
    type: standard-setter
    url: https://csrc.nist.gov/pubs/ir/8596/iprd
    date: '2025-12-16'
    access: full
    locator: GV.OV-03 row, Defend column (p. 28); Section 2.1.2, 'Conduct reporting' (p. 11)
  - ref: EC-NIS2
    title: 'NIS2 Directive: securing network and information systems (policy page)'
    publisher: European Commission
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/nis2-directive
    date: '2026-07-02'
    access: full
    locator: Paragraphs on risk-management measures, incident notification and top-management accountability
  - ref: EIOPA-DORA-2025
    title: Digital Operational Resilience Act (DORA) page
    publisher: EIOPA
    type: regulator
    url: https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en
    date: '2026-09-16'
    access: full
    locator: '''What does DORA cover?'': ICT-related incidents'
  - ref: SIFMA-SEC-2026
    title: Reforming Regulation S-K's Cybersecurity Disclosures (joint trades letter to the SEC)
    publisher: SIFMA, ABA, BPI, ICBA and IIB
    type: professional-body
    url: https://www.sifma.org/advocacy/letters/reforming-regulation-s-ks-cybersecurity-disclosures-joint-trades
    date: '2026-04-10'
    access: full
    locator: Opening paragraphs and section I
  last_reviewed: '2026-10-17'
  notes: 'Idea: a standard-setter lists it; no deployment or figure found. The SEC rule text itself (press release 2023-139) returned 403; the description of Item 1.05 comes from the trade-association letter.'
- id: security-governance-risk-09
  title: AI-assisted review of supplier assurance evidence at scale
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - research-synthesis
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: 'Third-party exposure keeps growing: 65% of large companies by revenue name third-party and supply chain vulnerabilities as their greatest challenge (up from 54% in 2025), FINRA reports more cyberattacks and outages at firms'' vendors, and DORA now puts critical ICT providers under direct supervisory oversight.'
  solution: Use an LLM to read supplier questionnaires, certifications and contract terms against the buyer's requirements, flag gaps and keep the vendor inventory current. Survey respondents say automation helps scale third-party risk management; regulators set the duties that the review must meet.
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure found for this use
    provenance: independent
    source_ref: WEF-GCO-2026
  prerequisites:
  - Inventory of third-party services, versions and the data types each vendor holds (FINRA effective practice)
  - Register of ICT contractual arrangements (DORA registers of information)
  risks_and_guardrails:
  - Regulators expect due diligence on vendors' own use of generative AI and contract language that bars sensitive firm or customer information from being ingested into a vendor's open-source GenAI tool (FINRA-OVERSIGHT-2026, Third-Party Risk Landscape, Effective Practices).
  - Of 264 AI vendors studied, 36% had no vulnerability disclosure policy and only 18% mentioned AI risks, so vendor-supplied evidence about AI risk may be thin (USENIX-PIAO-2026, abstract).
  human_checkpoints:
  - Vendor risk owner approves onboarding decisions and exceptions
  role_evolution: Not discussed in the sources.
  evidence_grade: D
  sources:
  - ref: WEF-GCO-2026
    title: Global Cybersecurity Outlook 2026 (with Accenture)
    publisher: World Economic Forum
    type: survey
    url: https://www.weforum.org/publications/global-cybersecurity-outlook-2026/
    date: '2026-01-12'
    access: full
    locator: '''Securing supply chains amid opacity and concentration risks'''
  - ref: FINRA-OVERSIGHT-2026
    title: '2026 FINRA Annual Regulatory Oversight Report (sections: GenAI; Cybersecurity and Cyber-Enabled Fraud; Third-Party Risk Landscape)'
    publisher: FINRA
    type: regulator
    url: https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report
    date: '2025-12-09'
    access: full
    locator: 'Third-Party Risk Landscape: FINRA''s firm outreach; Effective Practices'
  - ref: EBA-CTPP-2025
    title: The ESAs designate critical ICT third-party providers under the Digital Operational Resilience Act (press release)
    publisher: European Banking Authority (for the ESAs)
    type: regulator
    url: https://www.eba.europa.eu/publications-and-media/press-releases/european-supervisory-authorities-designate-critical-ict-third-party-providers-under-digital%5C
    date: '2025-11-18'
    access: full
    locator: Press release, paragraphs on designation methodology and oversight objective
  - ref: FAIR-SOCRM-2026
    title: What 400 Cyber Risk Leaders Told Us About the Future of Cyber Risk Management (2026 State of Cyber Risk Management report summary)
    publisher: FAIR Institute
    type: professional-body
    url: https://www.fairinstitute.org/blog/what-400-cyber-risk-leaders-told-us-about-the-future-of-cyber-risk-management
    date: '2026-06-04'
    access: full
    locator: Finding 7 (automation scaling third-party risk management)
  - ref: USENIX-PIAO-2026
    title: '''Abuse Risks are Often Inherent to Product Features'': Exploring AI Vendors'' Bug Bounty and Responsible Disclosure Policies (Piao, Li, Woods; USENIX Security 2026)'
    publisher: USENIX / University of Edinburgh
    type: academic
    url: https://www.usenix.org/conference/usenixsecurity26/presentation/piao
    date: 2026-08
    access: full
    locator: Abstract
  last_reviewed: '2026-10-17'
  notes: 'Idea at governance-angle level: I found regulators setting the duty and one survey saying automation helps third-party risk, but no independent deployment measure of AI in supplier assurance. Vendor product claims for AI third-party risk tools are covered in the practice-angle file and were not verified here. The FAIR finding says ''automation'', not ''AI'', for third-party risk.'
- id: security-governance-risk-10
  title: A written AI-use policy, sanctioned-tool inventory and AI-specific playbooks for the security team itself
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - document-production
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: AI is in the SOC faster than control over it. The SANS 2026 SOC survey says 79% of SOCs use AI or ML tools but only 36% have built them into a defined workflow, and SANS says most analysts use AI individually without systematic validation. ISACA found 48% of respondents either do not know or say their organisation has no AI incident playbooks.
  solution: 'Set the security function''s own AI policy: approved tools and data classes, owner and approval path for each AI use, logging of prompts, outputs and model versions, validation and human-in-the-loop review, AI-specific incident playbooks and exercises, and AI-security assessment of tools before use.'
  outcomes:
  - lever: risk
    description: Security professionals involved in developing an AI-use policy at their organisation
    figure: 56%
    measures: '''56 percent of respondents say that they or someone from their team were involved in the development of a policy governing the use of AI'' (ISACA survey of more than 1,800 professionals)'
    provenance: independent
    source_ref: ISACA-SOC-2026
  - lever: risk
    description: Organisations that regularly run AI-specific response exercises
    figure: 8%
    measures: '''only eight percent of organizations indicate they conduct AI-specific response exercises regularly''; 64% have conducted none (same survey)'
    provenance: independent
    source_ref: ISACA-SOC-2026
  - lever: risk
    description: Organisations assessing the security of AI tools
    figure: 64% (37% in 2025)
    measures: Share of respondents with processes to assess AI tool security, per WEF's Global Cybersecurity Outlook 2026 survey
    provenance: independent
    source_ref: WEF-GCO-2026
  - lever: risk
    description: Organisations developing AI policies, and those whose governance is still in development
    figure: 93% developing; 72% still in development
    measures: Shares of surveyed organisations per the SANS/GIAC 2026 Workforce Report slides; sample size is not on the slides
    provenance: independent
    source_ref: SANS-WORKFORCE-RSAC-2026
  prerequisites:
  - Inventory of AI tools and agents in use, including vendor-embedded features (Gartner says most leaders struggle to see embedded vendor AI)
  - Named policy owner and approval path
  - Logging of prompts, outputs and model versions
  risks_and_guardrails:
  - 'FINRA lists supervisory elements for GenAI: formal review and approval, testing of privacy, integrity, reliability and accuracy, and ongoing monitoring with stored prompt and output logs and tracked model versions (FINRA-OVERSIGHT-2026, GenAI section).'
  - The UK Cyber Governance Code of Practice says organisations implementing the AI Cyber Security Code should also follow the governance code (UK-CGCOP-2025, introduction).
  - Researchers describe a single adversarial alert acting as a remote code path through a SOC LLM's reasoning, so alert and log content must be treated as untrusted input (ARXIV-2610.09906, abstract).
  human_checkpoints:
  - Policy owner approves each new AI use; analysts validate AI output before action on anything outside pre-approved low-risk classes
  role_evolution: 56% of ISACA respondents helped write their organisation's AI policy and 51% are involved in developing, onboarding or implementing AI solutions (up from 40% in 2025), so security staff increasingly act as AI governors as well as users.
  evidence_grade: C
  sources:
  - ref: ISACA-SOC-2026
    title: Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises, ISACA Research Finds (State of Cybersecurity 2026 press release)
    publisher: ISACA
    type: professional-body
    url: https://www.isaca.org/about-us/newsroom/press-releases/2026/only-8-percent-of-organizations-global-enterprises-conduct-regular-ai-specific-response-exercises
    date: '2026-09-22'
    access: full
    locator: Sections 'AI incident response planning lags' and the paragraph on policy involvement
  - ref: SANS-SOC-2026
    title: 'SANS 2026 SOC Report: A Decade of Evolution in Cyber Defense (landing page)'
    publisher: SANS Institute
    type: professional-body
    url: https://www.sans.org/research/security-operations-report
    date: '2026'
    access: full
    locator: Top takeaways and FAQ ('What percentage of SOCs use AI')
  - ref: SANS-WORKFORCE-RSAC-2026
    title: 'AI, Regulation, & the Battle for Talent: The Future of the Cyber Workforce (slides presenting the 2026 SANS/GIAC Workforce Report)'
    publisher: SANS Institute and GIAC at RSAC 2026
    type: conference
    url: https://www.rsaconference.com/library/presentation/usa/2026/ai%20regulation%20%20the%20battle%20for%20talent%20the%20future%20of%20the%20cyber%20workforce
    date: '2026-03-23'
    access: full
    locator: Slide 5 (AI policy) and slide 22 (recommendation to establish an AI governance program within 3 months)
  - ref: WEF-GCO-2026
    title: Global Cybersecurity Outlook 2026 (with Accenture)
    publisher: World Economic Forum
    type: survey
    url: https://www.weforum.org/publications/global-cybersecurity-outlook-2026/
    date: '2026-01-12'
    access: full
    locator: '''AI is supercharging the cyber arms race'''
  - ref: FINRA-OVERSIGHT-2026
    title: '2026 FINRA Annual Regulatory Oversight Report (sections: GenAI; Cybersecurity and Cyber-Enabled Fraud; Third-Party Risk Landscape)'
    publisher: FINRA
    type: regulator
    url: https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report
    date: '2025-12-09'
    access: full
    locator: 'GenAI section: Supervision & Governance, Testing, Monitoring'
  - ref: TECHTARGET-AIREG-2026
    title: How to prepare security controls for future AI regulations (opinion by Gartner VP analyst Bernard Woo)
    publisher: TechTarget SearchSecurity
    type: press
    url: https://www.techtarget.com/cybersecurity/opinion/How-to-prepare-security-controls-for-future-AI-regulations
    date: '2026-06-02'
    access: full
    locator: Introduction (visibility into vendor-embedded AI)
  - ref: UK-CGCOP-2025
    title: Cyber Governance Code of Practice
    publisher: UK DSIT, DCMS and NCSC
    type: regulator
    url: https://www.gov.uk/government/publications/cyber-governance-code-of-practice/cyber-governance-code-of-practice
    date: '2025-04-08'
    access: full
    locator: Introduction
  - ref: ARXIV-2610.09906
    title: Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2610.09906
    date: '2026-10-07'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-17'
  notes: 'All outcomes are survey self-reports from third parties (ISACA, WEF, SANS); none measures effect on risk or errors. Pattern is ''other'': a policy and control framework rather than an AI workflow. The SANS SOC percentages are on the SANS landing page; the full report was not read and its publication month is not stated. Denominators for the SANS workforce slides are not given.'
- id: security-governance-risk-11
  title: Autonomy tiers and runtime guardrails for security and compliance agents
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - software-systems
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: 'Leaders want agents in security operations but not in charge: reliability and maturity (55%), accountability and explainability (46%) and, for CISOs, skills in AI oversight (44%) are named barriers to more autonomy. A single adversarial alert can drive a SOC agent to propose a harmful action.'
  solution: Set which actions agents may take without approval, by reversibility and consequence; limit agent access; log every action; and put a control the agent cannot influence (review, approval workflow or validation by another system) between the agent and any consequential action. Research prototypes constrain an LLM to a closed vocabulary of templated actions behind an argument validator and an input and output rail.
  outcomes:
  - lever: risk
    description: Respondents who would authorise AI agents to execute defensive actions fully without human approval
    figure: 22% (38% partial autonomy; 36% human-led with AI support)
    measures: Survey of 3,934 business and tech leaders in 71 countries; the answer base for this question is not stated on the summary page
    provenance: independent
    source_ref: PWC-GDTI-2027
  - lever: risk
    description: Prompt-injection recall of a guardrail proxy on a SOC-specific adversarial corpus
    figure: 25.0% to 94.5% at 0.1% false positives
    measures: Injection recall before and after adding the stock NeMo-Guardrails proxy, authors' own corpus and live red-team exercise; not an operational deployment
    provenance: independent
    source_ref: ARXIV-2610.09906
  prerequisites:
  - Agents issued their own identities with least privilege (CISA/partner guidance)
  - Logging and audit trail of agent actions
  - Threat model that includes prompt injection through alert and log content
  risks_and_guardrails:
  - Joint guidance from CISA, NSA and partners in Australia, Canada, New Zealand and the UK recommends aligning agentic AI risk management with existing cybersecurity frameworks, not granting agents broad or unrestricted access, using layered defence and strong identity management, and continuous monitoring (CISA-AGENTIC-BULLETIN-2026; CCCS-AGENTIC-2026).
  - 'FINRA''s agent risks: acting without human validation, exceeding scope, difficult auditability, sensitive data handling; it suggests monitoring agent access, human-in-the-loop points, tracking actions and guardrails (FINRA-OVERSIGHT-2026, GenAI: Agents).'
  - NIST is writing control overlays for single-agent and multi-agent AI use cases, with an annotated outline for predictive AI released 2026-01-08 (NIST-COSAIS-2026).
  human_checkpoints:
  - Tiered human-in-the-loop gates, with append-only audit, are the core of a proposed regulated-SOC runtime architecture (ARXIV-2605.30604, abstract; proposal with a test plan, no results)
  role_evolution: Analysts move toward approving, auditing and tuning agent actions; PwC finds 44% of CISOs name AI oversight skills as a top barrier to more autonomy.
  evidence_grade: C
  sources:
  - ref: PWC-GDTI-2027
    title: '2027 Global Digital Trust Insights: Moving targets (survey of 3,934 business and tech leaders)'
    publisher: PwC
    type: survey
    url: https://www.pwc.com/gx/en/issues/cybersecurity/global-digital-trust-insights.html
    date: '2026-10-01'
    access: full
    locator: '''AI for security'' section'
  - ref: CISA-AGENTIC-BULLETIN-2026
    title: CISA and Partners Release Guidance on Adopting Agentic AI Services (release bulletin for 'Careful Adoption of Agentic AI Services')
    publisher: CISA (via GovDelivery)
    type: regulator
    url: https://content.govdelivery.com/accounts/USDHSCISA/bulletins/41544ff
    date: '2026-05-01'
    access: full
    locator: Bulletin body, recommendations list
  - ref: CCCS-AGENTIC-2026
    title: Joint guidance on the careful adoption of agentic artificial intelligence services
    publisher: Canadian Centre for Cyber Security
    type: regulator
    url: https://cyber.gc.ca/en/news-events/joint-guidance-careful-adoption-agentic-artificial-intelligence-services
    date: '2026-05-01'
    access: full
    locator: Body
  - ref: FINRA-OVERSIGHT-2026
    title: '2026 FINRA Annual Regulatory Oversight Report (sections: GenAI; Cybersecurity and Cyber-Enabled Fraud; Third-Party Risk Landscape)'
    publisher: FINRA
    type: regulator
    url: https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report
    date: '2025-12-09'
    access: full
    locator: 'GenAI: ''Emerging Trends in GenAI: Agents'''
  - ref: NIST-COSAIS-2026
    title: SP 800-53 Control Overlays for Securing AI Systems (COSAiS) project page
    publisher: NIST
    type: standard-setter
    url: https://csrc.nist.gov/projects/cosais
    date: '2026-01-08'
    access: full
    locator: 'Overview: proposed use cases; recent updates'
  - ref: ARXIV-2610.09906
    title: Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2610.09906
    date: '2026-10-07'
    access: full
    locator: Abstract
  - ref: ARXIV-2605.30604
    title: An Organization-Scoped LLM Agent Runtime Architecture for Regulated Cybersecurity Operations
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2605.30604
    date: '2026-05-28'
    access: full
    locator: Abstract
  - ref: CSA-AGENTIC-NOTE-2026
    title: 'Agentic AI Adoption: Implementing the Five Eyes Framework (research note, states it was generated with AI assistance and not formally reviewed)'
    publisher: Cloud Security Alliance (CSAI Foundation)
    type: standard-setter
    url: https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/CSA_research_note_cisa-agentic-ai-adoption-guide-implementation_20260519-csa-styled.pdf
    date: '2026-05-19'
    access: full
    locator: Key Takeaways (secondary, AI-assisted note)
  - ref: SWIMLANE-SANSAI-2026
    title: A SOC Leader's Guide to the 2026 SANS AI Survey (vendor summary of the SANS survey)
    publisher: Swimlane
    type: vendor
    url: https://swimlane.com/blog/sans-ai-2026-soc-trust/
    date: '2026-05-18'
    access: full
    locator: Paragraphs citing 63% shortcomings and 39% automated incident response adoption (vendor summary of a survey not opened)
  last_reviewed: '2026-10-17'
  notes: The CISA guide itself was not retrievable; the recommendations above come from CISA's own release bulletin and the Canadian Cyber Centre's summary. The CSA note is labelled by its authors as AI-assisted and not formally reviewed, so I only use it as a secondary pointer. Vendor summary of the SANS 2026 AI survey (Swimlane) says 63% report significant shortcomings in AI's ability to detect or respond to threats and automated incident response sits at 39% adoption; this is a secondary vendor account of a survey I could not open (SWIMLANE-SANSAI-2026).
- id: security-governance-risk-12
  title: Redesign the security operating model and roles around AI oversight
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - coordination-scheduling
  - expert-judgment
  pattern: other
  ladder: delegate
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Teams report skills, not headcount, as the binding constraint, while AI changes entry-level work and creates roles that few organisations have yet filled.
  solution: 'Reassign work between people and agents: analysts supervise agents, new roles such as AI security engineer and AI governance analyst appear, hiring frameworks (NICE, ECSF) define the requisitions, and managed-service partners are used for AI skills. CSA is drafting an operating model with team topologies and agent-manager roles.'
  outcomes:
  - lever: capacity
    description: 'Organisations reporting AI impact on entry-level jobs, by role (slide wording: ''AI is impacting entry-level jobs'')'
    figure: SOC and security analysts 32%; threat intel analysts 26%; incident responders 22%; 39% report no role reductions yet
    measures: Share of surveyed organisations, multiple answers allowed, per the SANS/GIAC 2026 Workforce Report slides; sample size not on the slides
    provenance: independent
    source_ref: SANS-WORKFORCE-RSAC-2026
  - lever: capacity
    description: Organisations that have created new AI roles
    figure: AI/ML specialists 34%; AI security engineers 32%; AI governance analysts 30%
    measures: Share of surveyed organisations, multiple answers allowed, same slides
    provenance: independent
    source_ref: SANS-WORKFORCE-RSAC-2026
  - lever: capacity
    description: Respondents naming AI as the most pressing skills need
    figure: 41%
    measures: Share of 16,029 respondents to the ISC2 2025 study citing AI as the most pressing skills need, ahead of cloud security (36%)
    provenance: independent
    source_ref: ISC2-WORKFORCE-2025
  - lever: capacity
    description: Cyber teams increasing reliance on AI or automation to address technical skills gaps
    figure: 35% (12 points higher than last year)
    measures: Share of respondents to ISACA's 2026 survey of more than 1,800 professionals
    provenance: independent
    source_ref: ISACA-SOC-2026
  prerequisites:
  - A skills inventory against NICE or ECSF (56% use workforce frameworks to define requisitions per SANS/GIAC)
  - Career paths so that entry-level work that AI absorbs still leads to senior roles (only 24% have well-defined progressions per SANS/GIAC)
  risks_and_guardrails:
  - 'Pipeline risk: if AI absorbs entry-level analyst work, the supply of experienced staff may fall; no source measures this and ISC2 and SANS comment only qualitatively.'
  - 'Accountability is unsettled: 29% of CEOs and security and risk leaders put AI governance with the CIO/CTO, 26% with a dedicated AI leader and 17% with the CISO (PWC-GDTI-2027, key takeaways).'
  human_checkpoints:
  - Leadership approves role and structure changes; senior cyber management is the primary hiring decision maker in 53% of organisations (26% cyber manager or CISO, 27% senior leadership) (SANS/GIAC slide 14)
  role_evolution: ISC2 respondents expect AI to create more specialised skills (73%) and more strategic mindsets (72%) rather than replace jobs; the 2025 study dropped its workforce-gap headcount estimate in favour of skills measures. ISACA's 2026 survey finds 45% see LLM SecOps as a skill gap, up 12 points from 2025.
  evidence_grade: C
  sources:
  - ref: SANS-WORKFORCE-RSAC-2026
    title: 'AI, Regulation, & the Battle for Talent: The Future of the Cyber Workforce (slides presenting the 2026 SANS/GIAC Workforce Report)'
    publisher: SANS Institute and GIAC at RSAC 2026
    type: conference
    url: https://www.rsaconference.com/library/presentation/usa/2026/ai%20regulation%20%20the%20battle%20for%20talent%20the%20future%20of%20the%20cyber%20workforce
    date: '2026-03-23'
    access: full
    locator: Slides 7, 8, 12, 14, 15, 17
  - ref: ISC2-WORKFORCE-2025
    title: 2025 ISC2 Cybersecurity Workforce Study
    publisher: ISC2
    type: professional-body
    url: https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study
    date: '2025-12-04'
    access: full
    locator: Research Note; 'AI Is Creating Opportunities for Cybersecurity Professionals'; 'Skills Shortages Eclipse the Impact of Staff Shortages'
  - ref: ISACA-SOC-2026
    title: Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises, ISACA Research Finds (State of Cybersecurity 2026 press release)
    publisher: ISACA
    type: professional-body
    url: https://www.isaca.org/about-us/newsroom/press-releases/2026/only-8-percent-of-organizations-global-enterprises-conduct-regular-ai-specific-response-exercises
    date: '2026-09-22'
    access: full
    locator: Sections on skills and technical skills gaps
  - ref: PWC-GDTI-2027
    title: '2027 Global Digital Trust Insights: Moving targets (survey of 3,934 business and tech leaders)'
    publisher: PwC
    type: survey
    url: https://www.pwc.com/gx/en/issues/cybersecurity/global-digital-trust-insights.html
    date: '2026-10-01'
    access: full
    locator: 'Key takeaways: ''Who''s accountable for AI?''; ''Leadership, talent, and governance'''
  - ref: CSA-FRC-HUB-2026
    title: Frontier Ready Cybersecurity initiative hub (lists 'Designing the AI-First Security Organization', in open peer review). Date is the retrieval date
    publisher: Cloud Security Alliance (CSAI Foundation)
    type: standard-setter
    url: https://cloudsecurityalliance.org/csai-foundation/frontier-ready-cybersecurity
    date: '2026-10-17'
    access: full
    locator: 'Research list: ''Designing the AI-First Security Organization'' (description only; document in open peer review)'
  - ref: USENIX-TANG-2026
    title: 'From Assistance to Autonomy: An Empirical Study of AI Use in a Live Capture-the-Flag (CTF) Competition (Tang et al.; USENIX Security 2026)'
    publisher: USENIX / William & Mary and IBM Research
    type: academic
    url: https://www.usenix.org/conference/usenixsecurity26/presentation/tang-tingxuan
    date: 2026-08
    access: full
    locator: 'Abstract (adjacent evidence: CTF competition)'
  last_reviewed: '2026-10-17'
  notes: 'All figures are survey self-reports without published sample sizes in the slide deck. Adjacent evidence: a USENIX Security 2026 study of a live CTF (41 of 95 participants studied; four autonomous agents benchmarked) concludes that human-in-the-loop is the winning paradigm and that AI literacy and domain knowledge are complementary; it measures competition play, not security governance work, so I do not use it as an outcome. The CSA ''AI-First Security Organization'' report is described on CSA''s page as a team-topology and agent-manager-role model; I could not read the document.'
- id: security-governance-risk-13
  title: Adding generative-AI risk scenarios to risk quantification and board oversight
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Boards and investors cannot yet see AI-related financial and cyber risk in a structured way, and no single owner has emerged for AI risk (CIO/CTO 29%, dedicated AI leader 26%, CISO 17% per PwC).
  solution: Extend existing risk quantification with AI scenarios (the FAIR Institute promotes its FAIR-AIR approach) and give boards and investors a structured way to assess AI risk across the investment lifecycle (Berkeley CLTC's framework, built on interviews with more than 20 investors).
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure found for this use
    provenance: independent
    source_ref: FAIR-NACD-2025
  prerequisites:
  - An AI system and use inventory to scope scenarios
  - Agreed loss categories and risk appetite
  risks_and_guardrails:
  - The FAIR Institute's own AI playbook is members-only and could not be read; its position that boards should require AI-specific risk disclosures is the Institute's advocacy (FAIR-NACD-2025).
  - CLTC's framework is aimed at investors and is an initial approach, not a validated measure (CLTC-AIRISK-2026).
  human_checkpoints:
  - Board or risk committee approves risk appetite for AI use
  role_evolution: Not discussed.
  evidence_grade: D
  sources:
  - ref: FAIR-NACD-2025
    title: 'AI in Cybersecurity: Governance and Risk Quantification in the Boardroom'
    publisher: FAIR Institute
    type: professional-body
    url: https://www.fairinstitute.org/blog/nacd-ai-cybersecurity-governance-risk-quantification-boardroom
    date: '2025-03-18'
    access: full
    locator: Key takeaways 1-3 (summary of the NACD/ISA AI supplement)
  - ref: CLTC-AIRISK-2026
    title: 'AI Risk Governance: A Structured Approach for Investors and Corporate Boards (CLTC announcement page)'
    publisher: UC Berkeley Center for Long-Term Cybersecurity
    type: academic
    url: https://cltc.berkeley.edu/publication/ai-risk-governance-a-structured-approach-for-investors-and-corporate-boards/
    date: '2026-08-12'
    access: full
    locator: 'Page text: methodology and structured approach'
  - ref: PWC-GDTI-2027
    title: '2027 Global Digital Trust Insights: Moving targets (survey of 3,934 business and tech leaders)'
    publisher: PwC
    type: survey
    url: https://www.pwc.com/gx/en/issues/cybersecurity/global-digital-trust-insights.html
    date: '2026-10-01'
    access: full
    locator: 'Key takeaways: ''Who''s accountable for AI?'''
  last_reviewed: '2026-10-17'
  notes: 'Idea: governance advocates and academics discuss it; no deployment found. This is about quantifying the risk of AI use, so part of it overlaps the ai-security governance module.'
- id: security-governance-risk-14
  title: AI skills and oversight training for security and risk staff
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types:
  - coordination-scheduling
  - document-production
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: 'Skills gaps delay projects (57%) and slow incident response (47% report increased burnout and slower response) in the SANS/GIAC survey, and AI oversight skills are a named barrier to using agents. Training at scale is rare: 20% provide comprehensive AI training for all staff.'
  solution: Build role-based AI training for security staff covering use of AI tools, LLM SecOps, AI-system risk and AI regulation, and credential it.
  outcomes:
  - lever: capacity
    description: Security professionals working on general AI knowledge, and respondents holding or pursuing AI qualifications
    figure: 48% building AI skills; 17% hold an AI qualification and 53% plan to obtain one
    measures: Shares of 16,029 ISC2 2025 respondents; the study's conclusion states 70% have or are pursuing AI qualifications
    provenance: independent
    source_ref: ISC2-WORKFORCE-2025
  - lever: capacity
    description: Organisations providing comprehensive AI training to all staff
    figure: 20% (47% limited training or pilot or planning; 18% train cybersecurity staff only)
    measures: Share of surveyed organisations per SANS/GIAC slides; sample size not stated
    provenance: independent
    source_ref: SANS-WORKFORCE-RSAC-2026
  - lever: capacity
    description: Cyber teams naming LLM SecOps as a skill gap
    figure: 45% (12 points up on 2025, 21 points up on 2024)
    measures: Share of ISACA 2026 respondents (more than 1,800)
    provenance: independent
    source_ref: ISACA-SOC-2026
  prerequisites:
  - Budget and time during working hours for training (28% of ISC2 respondents' organisations allow it)
  - A skills baseline against a framework such as NICE
  risks_and_guardrails:
  - Training offered is mostly basic and not cybersecurity-specific (SANS/GIAC slide 6).
  - Survey data show intent more than demonstrated competence; no source tests whether trained staff oversee AI better.
  human_checkpoints:
  - Managers validate skills against role requirements
  role_evolution: ISC2 respondents prioritise AI skills development; ISACA reports 68% of employers offer professional development training, up from 60%.
  evidence_grade: C
  sources:
  - ref: ISC2-WORKFORCE-2025
    title: 2025 ISC2 Cybersecurity Workforce Study
    publisher: ISC2
    type: professional-body
    url: https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study
    date: '2025-12-04'
    access: full
    locator: '''AI Is Creating Opportunities''; ''Key Skills for AI''; Conclusion recommendations'
  - ref: SANS-WORKFORCE-RSAC-2026
    title: 'AI, Regulation, & the Battle for Talent: The Future of the Cyber Workforce (slides presenting the 2026 SANS/GIAC Workforce Report)'
    publisher: SANS Institute and GIAC at RSAC 2026
    type: conference
    url: https://www.rsaconference.com/library/presentation/usa/2026/ai%20regulation%20%20the%20battle%20for%20talent%20the%20future%20of%20the%20cyber%20workforce
    date: '2026-03-23'
    access: full
    locator: Slides 6 and 18
  - ref: ISACA-SOC-2026
    title: Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises, ISACA Research Finds (State of Cybersecurity 2026 press release)
    publisher: ISACA
    type: professional-body
    url: https://www.isaca.org/about-us/newsroom/press-releases/2026/only-8-percent-of-organizations-global-enterprises-conduct-regular-ai-specific-response-exercises
    date: '2026-09-22'
    access: full
    locator: Sections on skills gaps and support for staff
  last_reviewed: '2026-10-17'
  notes: Pure survey evidence. The use of AI itself to deliver training (adaptive scenarios, coaching) appears as an opportunity in NIST's draft profile (Section 2.1.2, 'Adversarial training and simulation') but I found no deployment.
```

## 3. Module notes

### 3.1 Processes and key steps (with work types)

- Policy and standards management: draft, maintain and map policies to ISO/IEC 27001/27002, NIST CSF 2.0 and regulation (`document-production`, `review-assurance`). NIST's profile is built on CSF 2.0 outcomes (NIST-CYBERAI-2025, Introduction).
- Risk identification, assessment and risk appetite: a register, scenario work and board approval of thresholds (`expert-judgment`). In the FAIR Institute survey of 400, 97% have defined risk appetite and tolerance and 89% have board-approved thresholds (FAIR-SOCRM-2026, Finding 5).
- Risk quantification and scenario analysis (`data-reporting`) (FAIR-SOCRM-2026, Findings 1 and 3).
- Compliance monitoring, evidence collection and attestations or audits such as SOC 2, ISO 27001, ISO 42001 and HITRUST (`review-assurance`) (VANTA-SYNTHESIA-2026, 'Vanta impact').
- Customer assurance: questionnaires and trust centres (`client-interaction`, `document-production`) (VANTA-GITHUB-2026).
- Third-party and supplier risk: inventory, due diligence, contract terms, monitoring (`review-assurance`) (FINRA-OVERSIGHT-2026, Third-Party Risk Landscape).
- Board and regulator reporting, incident notification and disclosure (`document-production`, `data-reporting`) (TECHTARGET-BOARD-2026; EC-NIS2).
- Regulatory horizon scanning and reconciliation of competing AI rules (`research-synthesis`) (TECHTARGET-AIREG-2026).
- Workforce planning, hiring and training (`coordination-scheduling`) (SANS-WORKFORCE-RSAC-2026, slides 12-19).
- The security team's own AI policy and controls (`review-assurance`, `document-production`) (use case 10).
- Security architecture as a lens: the official agentic-AI guidance expresses architecture as limits on agent access, layered defence and strong identity management (CISA-AGENTIC-BULLETIN-2026, recommendations list).

### 3.2 Common pain points

- Board reports are built around cyber topics rather than the business, and a CISO may get only five to ten minutes (TECHTARGET-BOARD-2026, 'Know your audience'; 'Position yourself as a business leader').
- Competing AI rules and poor visibility of AI embedded in vendor products: a Gartner analyst writes that most leaders struggle to maintain visibility into embedded AI features deployed by vendors (TECHTARGET-AIREG-2026, introduction).
- Skills rather than headcount: 59% cite critical or significant skills needs, up from 44% in 2024 (ISC2-WORKFORCE-2025, 'Skills Shortages Eclipse...'); SANS/GIAC reports the split as 60% skills to 40% headcount, from 52% skills last year (SANS-WORKFORCE-RSAC-2026, slide 17).
- Policies incomplete against standards until a thorough audit exposes it (ARXIV-2607.22885, abstract).
- Questionnaire surges after an AI launch: more than 300 questionnaires at GitHub in a short period (VANTA-GITHUB-2026, 'The challenge').
- Measuring the wrong thing: 70% of SOCs still name incident count as their top metric, and only 26% of cyber leaders who use threat intelligence apply it to budget decisions (SANS-SOC-2026, key findings).
- Return on spend: 41% of 650 CISOs say they cannot correlate ROI to risk mitigation activity, and 78% are concerned about personal liability (SPLUNK-CISO-2026, landing page; vendor survey).
- Accountability for AI is unsettled: 29% place it with the CIO/CTO, 26% with a dedicated AI leader, 17% with the CISO or cyber function (PWC-GDTI-2027, key takeaways).

### 3.3 Metrics and benchmarks

Each line gives what the figure measures.

- 79% of SOCs use AI or ML tools; 36% have built them into a defined workflow (SANS 2026 SOC survey: 444 practitioners and 69 cyber leaders) (SANS-SOC-2026, top takeaways).
- 8% of organisations regularly run AI-specific response exercises; 64% have run none; 48% do not know of or lack AI incident playbooks; 13% do not use AI in security operations (ISACA survey of more than 1,800 professionals) (ISACA-SOC-2026).
- 28% of respondents have integrated AI security tools, 19% are testing and 22% are evaluating (69% on a path to regular use); of teams already using them, 63% report a significant productivity boost (ISC2 2025 study, 16,029 respondents, self-reported) (ISC2-WORKFORCE-2025, 'AI Is Creating Opportunities').
- 64% of respondents now assess AI tool security, up from 37% in 2025; 87% name AI-related vulnerabilities as the fastest-growing cyber risk of 2025; 65% of large companies name third-party and supply chain vulnerabilities their greatest challenge, up from 54% (WEF Global Cybersecurity Outlook 2026) (WEF-GCO-2026).
- 22% would authorise AI agents to fully execute defensive actions without human approval; 50% of security leaders name attacks targeting AI systems as one of their biggest preparedness gaps; only 39% have fully formalised continuity plans that address cyber; 84% of security and finance leaders expect budgets to rise (PwC 2027 Digital Trust Insights, 3,934 leaders) (PWC-GDTI-2027).
- 58% use or plan FAIR (27% use, 31% plan; 46% in 2025); 80% use or experiment with AI in cyber risk programs; 64% say risk systems are mostly or fully automated (FAIR Institute survey of 400) (FAIR-SOCRM-2026, Findings 1, 3, 7).
- Board context per Gartner: 25% of CISOs presented to boards ten years ago; 93% of board members agree cyber risk threatens shareholder value; 71% of board members are willing to accept more cyber risk for business goals (TECHTARGET-BOARD-2026; TECHTARGET-CISO-2026).
- Policy-gap LLM benchmark: 80.65% mean agreement with human experts for the best of eight small models; four of eight under 60% balanced accuracy (ARXIV-2607.22885, Sections 5.1-5.2).
- LLM expert elicitation: correlation 0.91-0.98 with ground truth on proxies (ARXIV-2602.08889, abstract).
- Guardrail proxy for SOC LLMs: injection recall 25.0% to 94.5% at 0.1% false positives (ARXIV-2610.09906, abstract).
- AI vendors' disclosure practice: of 264 vendors, 36% have no vulnerability disclosure policy and 18% mention AI risks (USENIX-PIAO-2026, abstract).
- Cost context: global average data breach cost USD 4.99M, up 12%; USD 1.93M lower for organisations making extensive use of security AI and automation than for those using none (IBM/Ponemon). This is an association in a survey, not a controlled effect, and the release date is not stated on the page (IBM-CODB-2026, headline figures).

### 3.4 Guardrails and regulatory points

- EU AI Act: in force 2024-08-01; applicable from 2026-08-02 with exceptions; the AI Omnibus entered into force 2026-07-27 and moved Annex III high-risk duties to 2027-12-02 and Annex I product rules to 2028-08-02; the AI Office has enforcement powers over general-purpose AI models from 2026-08-02; transparency rules apply from August 2026 (EC-AIACT-2026, Application timeline; Governance and enforcement).
- EU Action Plan on Cybersecurity and AI (2026-07-07): strengthen pre-market evaluation of advanced AI models, build with ENISA a blueprint for secure access to advanced AI for cybersecurity, set up a secure testing platform for critical sectors, and encourage organisations to use AI to find and fix vulnerabilities; the AI Act page says the added evaluation capacity is expected to be operational by 2027 (EC-ACTIONPLAN-2026; EC-AIACT-2026, Governance and enforcement).
- NIS2: risk-management measures and significant-incident notification for medium and large entities in 18 sectors, with accountability of top management for non-compliance; on 2026-01-20 the Commission proposed targeted amendments that it says would ease compliance for 28,700 companies, including 6,200 micro and small enterprises (EC-NIS2).
- DORA: applies since 2025-01-17 to 20 types of financial entity and to ICT third-party providers; covers ICT risk management, third-party risk, resilience testing and incident reporting (EIOPA-DORA-2025). The ESAs published the first list of designated critical ICT third-party providers on 2025-11-18 (EBA-CTPP-2025).
- US: the March 2026 Cyber Strategy says it will streamline cyber regulations to reduce compliance burdens and address liability, adopt AI-powered cybersecurity for federal networks and raise the importance of cyber in the board room (WH-CYBERSTRATEGY-2026). SIFMA and four other trade groups asked the SEC on 2026-04-10 to rescind Item 106 of Regulation S-K, or narrow it, in its review of Regulation S-K (SIFMA-SEC-2026).
- FINRA 2026 report (published 2025-12-09): GenAI use is covered by existing supervision, communications and recordkeeping rules; it lists effective practices on vendor GenAI due diligence and contract terms; it warns on agent autonomy, scope, auditability and data handling; Regulation S-P amendments applied to larger entities from 2025-12-03 and apply to smaller entities from 2026-06-03 (FINRA-OVERSIGHT-2026, GenAI; Third-Party Risk Landscape; Cybersecurity).
- NIST: Cyber AI Profile preliminary draft with three focus areas (Secure, Defend, Thwart), comments due 2026-01-30, working sessions held 2026-04-28, 05-05 and 05-12 (NIST-CYBERAI-2025, Announcement); COSAiS overlays for generative AI, predictive AI, single-agent and multi-agent systems, and AI developers (NIST-COSAIS-2026, Overview).
- CISA, NSA and partners (2026-05-01): align agentic AI risk management with existing frameworks, limit agent access, layer defences, manage identity, monitor continuously (CISA-AGENTIC-BULLETIN-2026; CCCS-AGENTIC-2026).
- UK: AI Cyber Security Code of Practice (2025-01-31) and Cyber Governance Code of Practice (2025-04-08, five principles from risk management to oversight and assurance); organisations implementing the AI code should also follow the governance code (UK-AICODE-2025; UK-CGCOP-2025, introduction and principles).
- Ireland NCSC (2026-04-13): expects accelerated vulnerability disclosure after frontier-model announcements and tells organisations to review asset inventories and patching discipline (GOVIE-NCSC-2026).
- CSA AI Controls Matrix v1.1 (2026-06-22): 247 control objectives in 18 domains mapped to ISO 42001, ISO 27001, BSI AIC4, the EU AI Act and NIST AI RMF, with an AI-CAIQ questionnaire usable for third-party assessment (CSA-AICM-2026).

### 3.5 Frontier signals (dated and sourced)

- 2025-12-16: NIST publishes the preliminary draft Cyber AI Profile with a Defend focus on AI-enabled cyber defence, including compliance and executive risk communication (NIST-CYBERAI-2025).
- 2026-01-20: Commission proposes targeted NIS2 amendments to simplify compliance (EC-NIS2).
- 2026-03: US Cyber Strategy promises regulatory streamlining and AI adoption in defence (WH-CYBERSTRATEGY-2026).
- 2026-04-10: Industry asks the SEC to rescind Item 106; disclosure strategy may diverge between the US and the EU (SIFMA-SEC-2026; EC-NIS2).
- 2026-05-01: First joint Five Eyes guidance on agentic AI adoption (CISA-AGENTIC-BULLETIN-2026); CSA publishes its CISO guide to the 'AI Vulnerability Storm' (CSA-STORM-2026).
- 2026-06-04: 60% of organisations not yet using AI in cyber risk programs expect to implement within twelve months (FAIR-SOCRM-2026, Finding 3).
- 2026-06-22: CSA AI Controls Matrix v1.1 (CSA-AICM-2026).
- 2026-07-07 and 2026-07-27: EU Action Plan on Cybersecurity and AI; AI Omnibus in force (EC-ACTIONPLAN-2026; EC-AIACT-2026).
- 2026-09-22: ISACA finds AI incident readiness lags AI use (ISACA-SOC-2026).
- 2026-09-30: Google's threat intelligence group reports disclosures doubling and exploited vulnerabilities rising during 2026, and advises threat-intelligence-driven triage over mass patching; the vulnerability context for risk appetite decisions (GTIG-VULNTRENDS-2026, routed).
- 2026-10-01: PwC finds only 22% would let agents act without human approval, and no single owner for AI governance (PWC-GDTI-2027).
- 2026-10-08: CSA releases a maturity framework (12 categories, 5 levels) for preparing against AI-enabled adversaries; its 'Designing the AI-First Security Organization' report is in open peer review (CSA-FRAF-2026; CSA-FRC-HUB-2026).
- Gartner's own prediction that business acumen will be the main differentiator of high-performing CISOs by 2028 is a forecast, not a measurement (TECHTARGET-CISO-2026).

### 3.6 Workforce and role effects

- Entry-level effect: 32% of surveyed organisations report AI impact on entry-level SOC and security analyst jobs, 26% on threat intelligence analysts and 22% on incident responders, while 39% report no role reductions yet; new roles are AI/ML specialists (34%), AI security engineers (32%) and AI governance analysts (30%) (SANS-WORKFORCE-RSAC-2026, slides 7-8).
- Skills over headcount: ISC2 dropped its workforce-gap estimate this year because respondents prioritise critical skills over more people (ISC2-WORKFORCE-2025, Research Note).
- Regulation shapes hiring: SANS/GIAC reports the share saying regulation affects workforce hiring jumped from 40% to 95% in a year, with NIS2 cited by 30% globally (46% in Europe) (SANS-WORKFORCE-RSAC-2026, slides 10-11; sample size not stated).
- Optimism with caution: 72% of ISC2 respondents expect AI to create the need for more strategic cybersecurity roles and skills; 70% have or are pursuing AI qualifications (ISC2-WORKFORCE-2025, Conclusion).
- Stress and retention: 68% of ISACA respondents say their roles have become more stressful over five years; 58% say teams are understaffed (ISACA-SOC-2026).
- CISO role: Gartner argues the CISO's mandate should move from maximising prevention to minimising business harm before, during and after an attack (TECHTARGET-CISO-2026).
- In-the-loop evidence: a live CTF study finds human-in-the-loop is the winning paradigm for AI-assisted work (USENIX-TANG-2026, abstract); adjacent to governance work, not a measure of it.

### 3.7 Objections and concerns practitioners raise

- Reliability and maturity of the technology (55% rank among top three barriers to more agent autonomy) and accountability and explainability (46%) (PWC-GDTI-2027, 'AI for security').
- Personal liability (78% of 650 CISOs concerned) (SPLUNK-CISO-2026, landing page; vendor survey).
- Speed outrunning governance: SANS says most SOCs use AI without governance, validation or a defined workflow (SANS-SOC-2026, top takeaways).
- Business cost of control: Gartner's analyst says more security means more cost, slower speed to market and stalled innovation, and that more security does not mean better business outcomes (TECHTARGET-CISO-2026, 'The security drag').
- Prompt injection and trust of the security team's own AI: a single adversarial alert can drive an unconstrained SOC LLM to a harmful recommendation (ARXIV-2610.09906, abstract).
- Overconfidence of small models in compliance judgments: confidence scores that mirror the verdict, and invented policy statements (ARXIV-2607.22885, qualitative analysis).
- Vendor claims versus evidence: the vendor summary of the SANS AI survey says 63% report significant shortcomings in AI's ability to detect or respond to threats (SWIMLANE-SANSAI-2026; secondary).

### 3.8 Interview probes for an advisor

1. Which AI uses in your security function have a named owner, an approved-tool list and logged prompts, outputs and model versions, and who signs off a new use?
2. For AI-drafted questionnaire answers, evidence checks or policy-gap findings, what share is reviewed by a person, and have you ever compared the AI's verdicts with an assessor's on the same items?
3. Which actions may an agent take without approval, and what control sits between the agent and any consequential action that the agent cannot influence?
4. How do you report cyber and AI risk to the board: in money, scenarios or heat maps, and who owns AI risk (CIO/CTO, AI lead or CISO)?
5. What has changed in your entry-level analyst hiring and in new roles (AI governance analyst, LLM SecOps), and how are you keeping a path from junior work to senior judgment?

## 4. Routed to other modules

- Vulnerability flood and risk-based patch triage (GTIG 2026-09-30: disclosures doubling in 2026, exploited vulnerabilities rising from an average 10.5 to 18 per month, advice to prioritise with threat intelligence; CSA 'AI Vulnerability Storm' 2026-05-01; Ireland NCSC 2026-04-13) go to **vulnerability-exposure** (GTIG-VULNTRENDS-2026; CSA-STORM-2026; GOVIE-NCSC-2026).
- AI-specific incident exercises and playbooks (ISACA: 8% regular exercises, 48% unknown or no playbooks) go to **incident-response** (ISACA-SOC-2026).
- Agent security guidance and controls (CISA/partner agentic guidance, NIST COSAiS overlays, OWASP agent lists, CSA AI Controls Matrix, FINRA agent risks, Splunk's 78% with dedicated AI-agent teams) go to **ai-security**, governance and assurance deep dive (CISA-AGENTIC-BULLETIN-2026; NIST-COSAIS-2026; CSA-AICM-2026; FINRA-OVERSIGHT-2026; SPLUNK-CISO-2026).
- AI vendors' vulnerability disclosure and bug-bounty practices (264 vendors; 36% no policy) go to **ai-security** (third-party AI vendor risk) (USENIX-PIAO-2026).
- Guardrail proxy for SOC LLMs and org-scoped agent runtime architectures go to **security-operations** (ARXIV-2610.09906; ARXIV-2605.30604).
- Breach-cost association with security AI and automation (USD 1.93M lower) goes to **security-operations** metrics (IBM-CODB-2026).
- PwC finding that companies implemented only three of seven key data risk measures and only about half have data classification (49%) and DLP on key egress channels (48%) goes to **data-privacy** (PWC-GDTI-2027, 'Cyber strategy and operations').
- Live CTF study on AI assistance and autonomous agents goes to **security-operations** or the workforce effects of **vulnerability-exposure** (USENIX-TANG-2026).
- Vendor product claims for AI third-party risk, risk quantification and GRC agents (not verified here) belong to the practice-angle file for this module.

## 5. Sources

47 distinct sources. By type: academic 10, conference 1, firm 1, press 3, professional-body 6, regulator 12, standard-setter 7, survey 4, vendor 3. Refs cited in a use-case entry are marked; the rest support module notes or routing.

| Ref | Title | Publisher | Type | URL | Date | Access | Cited in |
|---|---|---|---|---|---|---|---|
| `NIST-CYBERAI-2025` | Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile), NIST IR 8596 initial preliminary draft | NIST | standard-setter | https://csrc.nist.gov/pubs/ir/8596/iprd | 2025-12-16 | full | use cases |
| `NIST-COSAIS-2026` | SP 800-53 Control Overlays for Securing AI Systems (COSAiS) project page | NIST | standard-setter | https://csrc.nist.gov/projects/cosais | 2026-01-08 | full | use cases |
| `CISA-AGENTIC-BULLETIN-2026` | CISA and Partners Release Guidance on Adopting Agentic AI Services (release bulletin for 'Careful Adoption of Agentic AI Services') | CISA (via GovDelivery) | regulator | https://content.govdelivery.com/accounts/USDHSCISA/bulletins/41544ff | 2026-05-01 | full | use cases |
| `CCCS-AGENTIC-2026` | Joint guidance on the careful adoption of agentic artificial intelligence services | Canadian Centre for Cyber Security | regulator | https://cyber.gc.ca/en/news-events/joint-guidance-careful-adoption-agentic-artificial-intelligence-services | 2026-05-01 | full | use cases |
| `CSA-AGENTIC-NOTE-2026` | Agentic AI Adoption: Implementing the Five Eyes Framework (research note, states it was generated with AI assistance and not formally reviewed) | Cloud Security Alliance (CSAI Foundation) | standard-setter | https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/CSA_research_note_cisa-agentic-ai-adoption-guide-implementation_20260519-csa-styled.pdf | 2026-05-19 | full | use cases |
| `EC-ACTIONPLAN-2026` | EU Action Plan on Cybersecurity and Artificial Intelligence | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence | 2026-07-07 | full | module notes |
| `EC-AIACT-2026` | AI Act: regulatory framework for AI (status page) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-08-03 | full | module notes |
| `EC-NIS2` | NIS2 Directive: securing network and information systems (policy page) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/nis2-directive | 2026-07-02 | full | use cases |
| `EIOPA-DORA-2025` | Digital Operational Resilience Act (DORA) page | EIOPA | regulator | https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en | 2026-09-16 | full | use cases |
| `EBA-CTPP-2025` | The ESAs designate critical ICT third-party providers under the Digital Operational Resilience Act (press release) | European Banking Authority (for the ESAs) | regulator | https://www.eba.europa.eu/publications-and-media/press-releases/european-supervisory-authorities-designate-critical-ict-third-party-providers-under-digital%5C | 2025-11-18 | full | use cases |
| `GOVIE-NCSC-2026` | NCSC statement on Anthropic's Mythos Preview model for defensive cyber security purposes | Ireland NCSC (Department of Justice, Home Affairs and Migration) | regulator | https://www.gov.ie/en/department-of-justice-home-affairs-and-migration/press-releases/national-cyber-security-centre-ncsc-statement-on-anthropics-mythos-preview-model-for-defensive-cyber-security-purposes/ | 2026-04-13 | full | module notes |
| `UK-AICODE-2025` | AI Cyber Security Code of Practice | UK DSIT and DCMS | regulator | https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice | 2025-01-31 | full | module notes |
| `UK-CGCOP-2025` | Cyber Governance Code of Practice | UK DSIT, DCMS and NCSC | regulator | https://www.gov.uk/government/publications/cyber-governance-code-of-practice/cyber-governance-code-of-practice | 2025-04-08 | full | use cases |
| `FINRA-OVERSIGHT-2026` | 2026 FINRA Annual Regulatory Oversight Report (sections: GenAI; Cybersecurity and Cyber-Enabled Fraud; Third-Party Risk Landscape) | FINRA | regulator | https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report | 2025-12-09 | full | use cases |
| `WH-CYBERSTRATEGY-2026` | President Trump's Cyber Strategy for America | The White House | regulator | https://www.whitehouse.gov/wp-content/uploads/2026/03/President-Trumps-Cyber-Strategy-for-America.pdf | 2026-03 | full | module notes |
| `SIFMA-SEC-2026` | Reforming Regulation S-K's Cybersecurity Disclosures (joint trades letter to the SEC) | SIFMA, ABA, BPI, ICBA and IIB | professional-body | https://www.sifma.org/advocacy/letters/reforming-regulation-s-ks-cybersecurity-disclosures-joint-trades | 2026-04-10 | full | use cases |
| `ISACA-SOC-2026` | Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises, ISACA Research Finds (State of Cybersecurity 2026 press release) | ISACA | professional-body | https://www.isaca.org/about-us/newsroom/press-releases/2026/only-8-percent-of-organizations-global-enterprises-conduct-regular-ai-specific-response-exercises | 2026-09-22 | full | use cases |
| `ISC2-WORKFORCE-2025` | 2025 ISC2 Cybersecurity Workforce Study | ISC2 | professional-body | https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study | 2025-12-04 | full | use cases |
| `SANS-SOC-2026` | SANS 2026 SOC Report: A Decade of Evolution in Cyber Defense (landing page) | SANS Institute | professional-body | https://www.sans.org/research/security-operations-report | 2026 | full | use cases |
| `SANS-WORKFORCE-RSAC-2026` | AI, Regulation, & the Battle for Talent: The Future of the Cyber Workforce (slides presenting the 2026 SANS/GIAC Workforce Report) | SANS Institute and GIAC at RSAC 2026 | conference | https://www.rsaconference.com/library/presentation/usa/2026/ai%20regulation%20%20the%20battle%20for%20talent%20the%20future%20of%20the%20cyber%20workforce | 2026-03-23 | full | use cases |
| `SWIMLANE-SANSAI-2026` | A SOC Leader's Guide to the 2026 SANS AI Survey (vendor summary of the SANS survey) | Swimlane | vendor | https://swimlane.com/blog/sans-ai-2026-soc-trust/ | 2026-05-18 | full | use cases |
| `FAIR-SOCRM-2026` | What 400 Cyber Risk Leaders Told Us About the Future of Cyber Risk Management (2026 State of Cyber Risk Management report summary) | FAIR Institute | professional-body | https://www.fairinstitute.org/blog/what-400-cyber-risk-leaders-told-us-about-the-future-of-cyber-risk-management | 2026-06-04 | full | use cases |
| `FAIR-NACD-2025` | AI in Cybersecurity: Governance and Risk Quantification in the Boardroom | FAIR Institute | professional-body | https://www.fairinstitute.org/blog/nacd-ai-cybersecurity-governance-risk-quantification-boardroom | 2025-03-18 | full | use cases |
| `CSA-AICM-2026` | AI Controls Matrix v1.1 | Cloud Security Alliance | standard-setter | https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1 | 2026-06-22 | full | use cases |
| `CSA-FRAF-2026` | Frontier Ready Assessment Framework | Cloud Security Alliance (CSAI Foundation) | standard-setter | https://cloudsecurityalliance.org/artifacts/frontier-ready-assessment-framework | 2026-10-08 | full | module notes |
| `CSA-STORM-2026` | The 'AI Vulnerability Storm': Building a 'Mythos-ready' Security Program (publication page) | Cloud Security Alliance | standard-setter | https://cloudsecurityalliance.org/artifacts/the-ai-vulnerability-storm | 2026-05-01 | full | module notes |
| `CSA-FRC-HUB-2026` | Frontier Ready Cybersecurity initiative hub (lists 'Designing the AI-First Security Organization', in open peer review). Date is the retrieval date | Cloud Security Alliance (CSAI Foundation) | standard-setter | https://cloudsecurityalliance.org/csai-foundation/frontier-ready-cybersecurity | 2026-10-17 | full | use cases |
| `TECHTARGET-BOARD-2026` | Lost in translation: Cybersecurity board reporting for CISOs (Gartner Security & Risk Management Summit session) | TechTarget SearchSecurity | press | https://www.techtarget.com/cybersecurity/news/366643884/Lost-in-translation-Cybersecurity-board-reporting-for-CISOs | 2026-06-03 | full | use cases |
| `TECHTARGET-CISO-2026` | CISO role changes as cyber-risk appetites in the C-suite grow (Gartner Security & Risk Management Summit session) | TechTarget SearchSecurity | press | https://www.techtarget.com/cybersecurity/news/366644003/CISO-role-changes-as-cyber-risk-appetites-in-the-C-suite-grow | 2026-06-08 | full | use cases |
| `TECHTARGET-AIREG-2026` | How to prepare security controls for future AI regulations (opinion by Gartner VP analyst Bernard Woo) | TechTarget SearchSecurity | press | https://www.techtarget.com/cybersecurity/opinion/How-to-prepare-security-controls-for-future-AI-regulations | 2026-06-02 | full | use cases |
| `PWC-GDTI-2027` | 2027 Global Digital Trust Insights: Moving targets (survey of 3,934 business and tech leaders) | PwC | survey | https://www.pwc.com/gx/en/issues/cybersecurity/global-digital-trust-insights.html | 2026-10-01 | full | use cases |
| `WEF-GCO-2026` | Global Cybersecurity Outlook 2026 (with Accenture) | World Economic Forum | survey | https://www.weforum.org/publications/global-cybersecurity-outlook-2026/ | 2026-01-12 | full | use cases |
| `SPLUNK-CISO-2026` | The CISO Report 2026: From Risk to Resilience in the AI Era (landing page; survey of 650 CISOs) | Splunk (Cisco) | survey | https://www.splunk.com/en_us/form/ciso-report.html | 2026 | full | module notes |
| `IBM-CODB-2026` | Cost of a Data Breach Report 2026 (landing page; date is the page's last-modified date, release date not stated) | IBM and Ponemon Institute | survey | https://www.ibm.com/reports/data-breach | 2026-09-16 | full | module notes |
| `CLTC-AIRISK-2026` | AI Risk Governance: A Structured Approach for Investors and Corporate Boards (CLTC announcement page) | UC Berkeley Center for Long-Term Cybersecurity | academic | https://cltc.berkeley.edu/publication/ai-risk-governance-a-structured-approach-for-investors-and-corporate-boards/ | 2026-08-12 | full | use cases |
| `ARXIV-2607.22885` | ReCon: A Resource-Constrained Benchmark for LLM-Based Cybersecurity Compliance Across Ingestion and Retrieval Pipelines (Negi et al., IIT Kanpur and IIIT Hyderabad) | arXiv | academic | https://arxiv.org/abs/2607.22885 | 2026-07-24 | full | use cases |
| `ARXIV-2602.08889` | Scalable Delphi: Large Language Models for Structured Risk Estimation (Lorenz and Fritz) | arXiv | academic | https://arxiv.org/abs/2602.08889 | 2026-02-09 | full | use cases |
| `ARXIV-2601.03287` | Automated Post-Incident Policy Gap Analysis via Threat-Informed Evidence Mapping using Large Language Models | arXiv | academic | https://arxiv.org/abs/2601.03287 | 2026-01-04 | full | use cases |
| `ARXIV-2605.30604` | An Organization-Scoped LLM Agent Runtime Architecture for Regulated Cybersecurity Operations | arXiv | academic | https://arxiv.org/abs/2605.30604 | 2026-05-28 | full | use cases |
| `ARXIV-2412.13988` | RAG for Effective Supply Chain Security Questionnaire Automation (QuestSecure) | arXiv | academic | https://arxiv.org/abs/2412.13988 | 2024-12-18 | full | use cases |
| `ARXIV-2604.06274` | Towards the Development of an LLM-Based Methodology for Automated Security Profiling in Compliance with Ukrainian Cybersecurity Regulations | arXiv | academic | https://arxiv.org/abs/2604.06274 | 2026-04-07 | full | use cases |
| `ARXIV-2610.09906` | Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy | arXiv | academic | https://arxiv.org/abs/2610.09906 | 2026-10-07 | full | use cases |
| `USENIX-PIAO-2026` | 'Abuse Risks are Often Inherent to Product Features': Exploring AI Vendors' Bug Bounty and Responsible Disclosure Policies (Piao, Li, Woods; USENIX Security 2026) | USENIX / University of Edinburgh | academic | https://www.usenix.org/conference/usenixsecurity26/presentation/piao | 2026-08 | full | use cases |
| `USENIX-TANG-2026` | From Assistance to Autonomy: An Empirical Study of AI Use in a Live Capture-the-Flag (CTF) Competition (Tang et al.; USENIX Security 2026) | USENIX / William & Mary and IBM Research | academic | https://www.usenix.org/conference/usenixsecurity26/presentation/tang-tingxuan | 2026-08 | full | use cases |
| `VANTA-GITHUB-2026` | GitHub accelerates sales by automating 93% of security questionnaires with Vanta (customer case study; date is sitemap last-modified, original date not stated) | Vanta | vendor | https://www.vanta.com/customers/github | 2026-03 | full | use cases |
| `VANTA-SYNTHESIA-2026` | How Synthesia became the first AI video company certified against ISO 42001, with a two-person team (customer case study; date is month of sitemap last-modified) | Vanta | vendor | https://www.vanta.com/customers/synthesia | 2026-10 | full | use cases |
| `GTIG-VULNTRENDS-2026` | Vulnerability Discovery and Exploitation Trends in the AI Era | Google Threat Intelligence Group | firm | https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/ | 2026-09-30 | full | module notes |

Access notes: every source marked `full` was opened and read at the passages cited (landing pages and summaries are named as such in titles or locators). `CSA-AGENTIC-NOTE-2026` is labelled by its authors as AI-assisted and not formally reviewed. `SWIMLANE-SANSAI-2026` is a vendor's summary of a survey I could not open. Items from the landscape file that I did not open (for example Gartner's trends press release, the SANS AI survey, the CISA guide itself) are not listed as sources.

## 6. Gaps

- **No quality evidence in practice.** No error rate, override rate, parallel run, auditor-reliance study or regulator inspection finding on AI used for GRC work was found. The independent numbers are lab benchmarks on small datasets.
- **CISA agentic guide not read.** The CISA page blocked access (403, and the mirror blocked the domain); the ACSC page failed repeatedly. I used CISA's own release bulletin, the Canadian Cyber Centre summary and an AI-assisted CSA note. The five risk categories (privilege, design and configuration, behavioural, structural, accountability) come only from that CSA note and are not used as a primary claim.
- **Primary rules not opened.** SEC rule text and exam priorities (403), NYDFS AI industry letter (404 at the URLs tried), MAS AI risk management guidelines (404), ISO/IEC 42001 (403), Gartner press releases (403), WEF full report (summary page only), NIST Cyber AI Profile comment responses.
- **Full survey reports not read.** ISACA State of Cybersecurity 2026 (gated; press release used), SANS 2026 SOC and AI surveys (landing page and a vendor summary), SANS/GIAC Workforce Report (slides only, sample sizes not stated), ISC2 (read in full), PwC full report (summary page only), Splunk CISO report (landing page, publication date not stated), IBM Cost of a Data Breach (landing page, release date not stated), FAIR State of Cyber Risk Management report (blog summary only).
- **Dates not stated.** SANS 2026 SOC report (year only), Splunk CISO report (year only), Vanta case studies (sitemap last-modified dates used, original publication dates not shown), IBM CODB (page-modified date).
- **Not found at all.** Public numbers on auditor acceptance of AI-collected evidence; independent evaluation of AI questionnaire answers; named in-house deployments for AI-assisted board reporting or regulator-notification drafting; risk quantification vendor results with named customers I could verify; third-party risk AI deployments with named customers I could verify.
- **Under-covered regulators.** APAC, Middle East and sector supervisors beyond FINRA and the EU financial regulators; EU AI Act harmonised standards; ENISA outputs on AI-assisted compliance.
- **CSA 'Designing the AI-First Security Organization'** is in open peer review and was not readable; only its description is used.
- **Academic.** Journals not reached; of conference venues only USENIX Security 2026 was mined by title and abstract (no governance-specific paper beyond the two cited); IEEE S&P, NDSS and ACM CCS not mined for this module. arXiv items were read at abstract level except ReCon (full text).
- **Terminology anomaly** on NIST pages (super intelligence for AI) noted in the summary.

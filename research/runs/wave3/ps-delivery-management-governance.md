# Professional services / delivery-management / governance deep dive

Prepared 2026-10-19. Archetype: professional-services. Module: delivery-management (running engagements: project planning, status and risk tracking, client reporting, change control and engagement economics during delivery). Angle: governance (what constrains and measures the work).

Method: `curl`, `pdftotext` and the r.jina.ai text mirror into a private `mktemp -d` folder. 38 sources were opened (listed in section 5; 4 more were seen only in search results). Web search was used for 11 queries. Quotations are under 25 words. Public sources only; items for in-house (client-side) legal teams are tagged "in-house".

---

## 1. Summary

**What the governance record says.** The rules for AI in running an engagement are clearer than the evidence that AI improves it. The standards bind the engagement lead; independent measurement of delivery-management AI is close to absent.

- **Responsibility stays with the professional, and the duty grows with autonomy.** ABA Formal Opinion 512 (29 Jul 2024), the State Bar of California's revised guidance (approved 14 May 2026) and the ICMCI consulting code (May 2026) all say the lawyer or consultant remains responsible for AI-assisted work. California adds that the greater the autonomy of the system, the greater the oversight, and that periodic reassessment is part of competence (CALBAR-GENAI-2026, pp.3-5; ICMCI-AICODE-2026, section 2.2).
- **The client is now a governing party.** California requires lawyers to follow client guidelines that restrict AI (p.7). ICMCI says consultants must comply with client instructions on AI tools (section 5.4). Australia's government model clauses for services in which the seller uses AI (including consulting) require the seller to obtain approval for AI use, run quality checks on outputs and keep detailed records of AI use (AGS-AIMODELCLAUSES-2025). In the KPMG survey of 468 general counsel, 82% expect external providers to explain how they use AI (LEGALBUSINESS-KPMGGC-2026; in-house).
- **Neither side can currently show what AI saves.** In the Thomson Reuters Institute's 2026 AI in Professional Services Report, 85% of law-firm respondents and 75% of corporate legal-department respondents say they are not collecting ROI data on AI or are unsure; 68% of corporate legal professionals do not know whether their outside firms use AI (TRI-DISCONNECT-2026). In the ACC and Everlaw survey, 59% of in-house respondents do not know whether outside counsel uses generative AI on their matters (ACC-TRANSPARENCY-2025; in-house). Firm panelists at Legalweek 2026 described their ROI evidence as anecdotal (TRI-LEGALWEEK-2026).
- **Time saved is not the same as value kept.** The SPI Research 2026 study of 245 firms reports that 84.8% say AI saves them time; the share saying it generates revenue is hidden on the public page, and the report frames the gap as "the leak" (SPI-AI-2026). ABA 512 and California both say hourly bills must reflect time actually spent and that a flat fee may be unreasonable if AI makes the work much faster (ABA-OP512-2024, p.12; CALBAR-GENAI-2026, p.8).
- **Practice is early and mostly vendor-described.** In a Kantata-commissioned survey of 44 organisations, 39% are in "traditional staffing" mode, 30% exploring, 31% beyond experimentation, and 52.7% say they are not equipped to manage hybrid human and agent teams (KANTATA-RMI-2026). A qualitative study of 12 Finnish IT project managers found adoption "fragmented and peripheral", constrained by organisational policy, with AI used for support tasks rather than core project management (EINFORMATICA-SAINIO-2026).
- **Quality evidence is absent for this module.** No published error rate, override rate, reviewer catch rate or parallel run was found for AI status reports, risk scoring, forecasts or change-control detection. The independent studies found measure adjacent work (patent drafting, consulting tasks, email time).
- **One failure shows the exposure.** Deloitte Australia agreed to repay the final instalment of a AUD 440,000 contract after a report had incorrect footnotes and references, including a fabricated court quote; the revised report disclosed Azure OpenAI use (CTV-DELOITTE-2025).

**Use cases:** 13 candidates (B: 1, C: 8, D: 4; no grade A, because no named organisation reports measured delivery-management outcomes).

**Most reusable finds:** TRI-DISCONNECT-2026 (visibility and ROI-measurement gaps, firm and in-house); AGS-AIMODELCLAUSES-2025 (buyer clauses on supplier AI use); ABA-OP512-2024 Part II.F (fees); CALBAR-GENAI-2026 pp.3-9; ICMCI-AICODE-2026 sections 2.2, 3.3, 5.4, 7.3; ILTA-TECHSURVEY-2026 p.9 (tracking tools in under one in five firms); KANTATA-RMI-2026; EINFORMATICA-SAINIO-2026.

---

## 2. Use cases

Grades: A needs a figure the named organisation reports as measured; none found. B is a named deployment without published measurement. C is a vendor or analyst claim. D is an idea that bars, researchers or practitioners discuss; every D entry is labelled "idea" in its title.

```yaml
- id: professional-services-delivery-management-01
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: Engagement health scoring and scope scans by a PMO agent
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: 'PMO leaders learn about slippage, scope drift and margin leakage late, through manual status chasing.
    The data foundations for earlier warning are weak: 47% of resource-management respondents cite poor or fragmented
    data across skills, outcomes, demand and capacity as a top barrier to AI (KANTATA-RMI-2026). Deltek''s study
    of 917 government contractors lists the potential for inaccurate forecasts (29%) and difficulty validating AI-provided
    insights (26%) among the top AI concerns; the release does not state the denominator (DELTEK-CLARITY-2026).'
  solution: Certinia describes a PMO Quality agent that scans project scope regularly to score health sentiment,
    and says automated scope scans plus real-time sentiment scoring let PMO leaders steer projects before risks
    become realities. Certinia says its agents act within the permissions, approval thresholds and auditability
    the customer requires. The page does not say what a scope scan compares against, how sentiment is scored, or
    how often the score is wrong (CERTINIA-VEDA-2026).
  outcomes:
  - lever: risk
    description: Vendor-stated reduction in margin lost to rework and quality issues
    figure: 11-23% less margin lost
    measures: Margin lost to rework and quality issues. The page gives no baseline, sample, period or definition,
      and lists it under 'More gains across the lifecycle' without naming the agent responsible.
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  - lever: capacity
    description: Vendor-stated recovery of project time lost to administration
    figure: about 50% of project time historically lost to admin, recovered
    measures: Share of project time 'historically lost to admin' that is recovered. No baseline, sample or period
      is given.
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Delivery, sales and financial data held in one governed foundation; Certinia's agents run on a Salesforce-native
    PSA (CERTINIA-VEDA-2026).
  - Usable data on skills, demand, capacity and outcomes; 47% cite fragmented data as a top barrier (KANTATA-RMI-2026).
  risks_and_guardrails:
  - The more autonomy a system has, the more oversight and verification the lawyer must build; the duty of competence
    includes periodic reassessment of the system as it changes (CALBAR-GENAI-2026, pp.4-5).
  - Sentiment scoring reads client and team communications; agent access to email, messaging and client files raises
    confidentiality risk, including across matters (CALBAR-GENAI-2026, pp.5-6).
  - A lawyer must follow client instructions or guidelines that restrict AI (CALBAR-GENAI-2026, p.7); consultants
    must comply with client instructions on AI tools (ICMCI-AICODE-2026, section 5.4).
  - No published precision, recall or false-alarm rate for any health score was found.
  human_checkpoints:
  - PMO leader or engagement lead reviews flagged engagements and decides the intervention; the score is an input,
    not a decision.
  - Periodic reassessment of the agent's accuracy against actual engagement outcomes (CALBAR-GENAI-2026, pp.4-5).
  role_evolution: Certinia says its agents let experts spend time on judgment calls rather than paperwork and lists
    a PMO Leadership agent for portfolio oversight (CERTINIA-VEDA-2026). In a qualitative study of 12 Finnish IT
    project managers, participants saw AI as an 'assistant not replacement' (EINFORMATICA-SAINIO-2026, abstract).
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026'
    access: full
    locator: '''Margin protection & risk management''; Plan and Manage agent lists; ''More gains across the lifecycle'''
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape
      Professional Services
    publisher: Kantata (Resource Management Institute study)
    type: vendor
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: 'paragraph 2 (barriers: 49%, 47%, 41%)'
  - ref: DELTEK-CLARITY-2026
    title: The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity
      Pressures for Project-Based Businesses
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/
    date: '2026-05-12'
    access: full
    locator: Key Findings, 17th Government Contracting report (AI concerns)
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: professional-body
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: pp.4-7
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version
      1.0
    publisher: International Council of Management Consulting Institutes
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: section 5.4
  - ref: EINFORMATICA-SAINIO-2026
    title: Realising the Role of Generative AI Among Project Management Professionals (Sainio, Kettunen, Abrahamsson)
    publisher: e-Informatica Software Engineering Journal, vol. 20, no. 1
    type: academic
    url: https://www.e-informatyka.pl/einformatica/volumes/volume-2026/issue-1/article-4/
    date: '2026'
    access: full
    locator: abstract, Results
  notes: 'Vendor product page; no named customer result is attached to this agent. The page carries a testimonial
    from Siemens Digital Industries (SVP Global Customer Success) saying a Certinia ''Project Agent'' helps identify
    deliverable discrepancies early, but it does not say whether that is the PMO Quality agent and gives no result.
    Search-only: a Gartner abstract (July 2026) warns that PMOs deploying AI agents without solid foundations risk
    poor autonomous decisions at scale (GARTNER-PMO-2026). Deltek''s concern figures are from a government-contractor
    study, an adjacent project-based sector.'
  last_reviewed: '2026-10-19'
- id: professional-services-delivery-management-02
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: Conversational engagement status and variance digests in place of manual status chasing
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Partners and PMO leads ask team members to reconstruct status from email threads and separate checklists
    (HARVEY-ORCH-2026). Certinia describes the same pain as 'manual status-chasing' across financials, risk and
    tasks (CERTINIA-VEDA-2026).
  solution: Certinia lists a Project Assistant that delivers instant digests on financials, risks and timeline variances,
    and says it replaces status chasing with conversational visibility so slippage and overdue milestones surface
    earlier (CERTINIA-VEDA-2026). Harvey says its matter workspace keeps a current view of progress, and that lawyers
    can close or start tasks by replying to email (HARVEY-ORCH-2026).
  outcomes:
  - lever: speed
    description: none published for status reporting specifically
    figure: null
    measures: Neither vendor reports time-to-status or accuracy figures for this step.
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Timesheet, budget and milestone data current enough to summarise; a task structure that the assistant can read
    (HARVEY-ORCH-2026).
  - Access controls that keep one client's matter data out of another's answers (CALBAR-GENAI-2026, p.6).
  risks_and_guardrails:
  - A digest sent to a client is a communication about the representation; the duty to keep the client reasonably
    informed and to consider AI disclosure applies (ABA-OP512-2024, Part II.C, pp.8-9; CALBAR-GENAI-2026, p.7).
  - Digests are only as good as the underlying time and task data; no accuracy measurement was found.
  - Information from one matter may reach people who should not see it unless access is configured (ABA-OP512-2024,
    Part II.B, p.7).
  human_checkpoints:
  - Engagement lead checks any digest before it goes to a client.
  - Spot-check digest figures against the PSA or time system.
  role_evolution: 'Harvey says partners can see where work stands without asking an associate to reconstruct it
    (HARVEY-ORCH-2026). Project and resource managers are largely operational today: 72% of Kantata/RMI respondents
    say resource management is primarily or solely operational with limited strategic influence (KANTATA-RMI-2026).'
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026'
    access: full
    locator: '''See the business as it actually is''; Manage agent list (Project Assistant)'
  - ref: HARVEY-ORCH-2026
    title: Making Harvey the Orchestration Layer for Legal Work
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/legal-work-orchestration
    date: '2026-10-15'
    access: full
    locator: '''Keep Reviews and Next Steps Moving'''
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: ABA Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.B p.7; Part II.C pp.8-9
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: professional-body
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: pp.6-7
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape
      Professional Services
    publisher: Kantata (Resource Management Institute study)
    type: vendor
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: paragraph 7 (72% operational)
  last_reviewed: '2026-10-19'
- id: professional-services-delivery-management-03
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: Template-driven matter orchestration with agent-executed tasks and named review gates
  work_types:
  - coordination-scheduling
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: 'A repeatable matter such as an M&A deal moves through familiar phases, tasks and review points, but
    the process is reconstructed for each new matter from a checklist, a previous deal or what experienced people
    remember. Agents can complete individual steps but lack the structure around them: where the task fits, which
    documents apply, who reviews, what happens next. Lawyers carry that context by hand (HARVEY-ORCH-2026).'
  solution: Harvey launched Legal Work Orchestration on 15 Oct 2026. Reusable templates hold a recurring matter's
    phases, tasks, playbooks, agents, collaborators and review gates. Each task carries its scope, inputs and reviewer.
    When an agent finishes (Harvey's example is a change-of-control consent matrix), the designated partner is notified;
    on approval the next step begins. Harvey says tasks, comments and notifications are rolling out now and templates
    are in an early-access programme (HARVEY-ORCH-2026).
  outcomes:
  - lever: capacity
    description: 'Vendor expectation, not a measured result: agents take on more workflow steps'
    figure: additional 20% of workflow steps within six months
    measures: Harvey's expectation of the share of workflow steps agents take on, versus steps lawyers prompt. Harvey
      adds that within a year 'that share' will triple; the sentence is ambiguous about whether 'that share' means
      the additional 20%. No baseline share is given.
    provenance: vendor-published
    source_ref: HARVEY-ORCH-2026
  prerequisites:
  - Innovation and knowledge teams define the template once (phases, playbooks, review gates) (HARVEY-ORCH-2026).
  - A firm policy on permissible AI use, training for supervisors and subordinates, and monitoring (ABA-OP512-2024,
    Part II.E, pp.10-11).
  risks_and_guardrails:
  - Where agentic AI is used for court filings, no document may go to the court without lawyer review and approval,
    and AI must not file or make representations to the court on the lawyer's behalf (CALBAR-GENAI-2026, p.9).
  - 'Supervision must scale with autonomy: the greater the system''s autonomy, the greater the oversight and verification
    mechanisms needed (CALBAR-GENAI-2026, p.3).'
  - Work-product governance in law firms 'still relies heavily on training and leadership pressure'; sophisticated
    tracking and compliance tools are in use by fewer than one in five firms (ILTA-TECHSURVEY-2026, 'Curtain Call
    for the Data Center').
  - No reviewer catch rate, override rate or gate-skipping data for orchestrated workflows was found.
  human_checkpoints:
  - Designated reviewer approves each gated output before the next task starts (HARVEY-ORCH-2026).
  - Lawyer reviews all outputs, decisions and filings (CALBAR-GENAI-2026, p.4).
  role_evolution: Harvey says lawyers will remain in control through defined review gates and will focus more on
    directing the matter, reviewing consequential outputs and exercising judgment (HARVEY-ORCH-2026). The Cal Bar
    guidance says professional judgment cannot be delegated to AI (CALBAR-GENAI-2026, p.4).
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
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: ABA Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.E, pp.10-11
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: professional-body
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: pp.3-4, 9
  - ref: ILTA-TECHSURVEY-2026
    title: ILTA Technology Survey 2026 Executive Summary
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: p.9, 'Curtain Call for the Data Center'
  notes: No named customer or measured result in the launch post. Legal matters only; no consulting or accounting
    equivalent with a named customer was found.
  last_reviewed: '2026-10-19'
- id: professional-services-delivery-management-04
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: Meeting capture into summaries and action items for delivery teams, with consent and confidentiality controls
  work_types:
  - coordination-scheduling
  - document-production
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: 'Delivery teams spend time writing meeting notes and chasing action items. Meeting bots add a legal risk:
    a US federal class action filed in Aug 2025 alleges Otter.ai''s meeting assistant recorded and transcribed conversations
    without participants'' consent (KJZZ-OTTER-2025).'
  solution: An AI assistant turns meeting conversations into summaries and tasks. Certinia lists a Project Assistant
    that transforms meeting conversations into clear summaries and keeps project teams on track (CERTINIA-VEDA-2026).
    A six-month randomised field experiment gave workers a generative AI tool built into email, meeting and writing
    applications (NBER-DILLON-2025).
  outcomes:
  - lever: speed
    description: Weekly time on email fell for workers who used an integrated generative AI tool (not meeting time)
    figure: two fewer hours on email per week
    measures: Among the 80% of treated workers who used the tool, weekly time spent on email in the second half
      of a 6-month randomised experiment; 66 firms and 7,137 knowledge workers; not professional-services specific.
      The authors detect no shift in the quantity or composition of tasks.
    provenance: independent
    source_ref: NBER-DILLON-2025
  prerequisites:
  - A recording-consent practice for every participant, including clients, and a vendor whose data terms are reviewed
    rather than accepted by click-through (CALBAR-GENAI-2026, p.5).
  - A rule for what may be recorded in client engagements; ICMCI says consultants must follow client instructions
    on AI and not enter confidential data into tools that may reuse it (ICMCI-AICODE-2026, sections 3.4 and 5.4).
  risks_and_guardrails:
  - A lawyer needs a client's informed consent before inputting client information into a self-learning tool that
    could disclose it to others (ABA-OP512-2024, Part II.B, p.7).
  - Reasonable efforts require more than reliance on generalised marketing assurances; review terms of use and privacy
    policies (CALBAR-GENAI-2026, p.5).
  - Third-party vendors' terms may not bind other call participants. This point is from a search summary of a consent
    guide and was not verified at source (OTTER-LITIGATION-2026).
  - The Otter claims are allegations; coverage disagrees on how far the motion to dismiss succeeded (OTTER-LITIGATION-2026,
    search-only).
  human_checkpoints:
  - Meeting organiser confirms consent and the permitted tool before recording starts.
  - Owner checks the summary and action list before they are circulated to the client.
  role_evolution: No source describes a role change specific to this step. The NBER experiment found no shift in
    workers' task quantity or composition from individual-level AI provision (NBER-DILLON-2025).
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026'
    access: full
    locator: '''Frictionless operations & delivery''; Manage agent list'
  - ref: NBER-DILLON-2025
    title: Shifting Work Patterns with Generative AI (NBER WP 33795)
    publisher: National Bureau of Economic Research
    type: academic
    url: https://www.nber.org/papers/w33795
    date: 2025-05
    access: full
    locator: abstract
  - ref: KJZZ-OTTER-2025
    title: Class-action suit claims Otter AI secretly records private work conversations
    publisher: KJZZ / NPR
    type: press
    url: https://www.kjzz.org/npr-top-stories/2025-08-15/class-action-suit-claims-otter-ai-secretly-records-private-work-conversations
    date: '2025-08-15'
    access: full
    locator: paragraphs 1-4
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: ABA Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.B, pp.6-7
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: professional-body
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.5
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version
      1.0
    publisher: International Council of Management Consulting Institutes
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: sections 3.4, 5.4
  - ref: OTTER-LITIGATION-2026
    title: In re Otter.AI Privacy Litigation, 5:25-cv-06911-EKL (N.D. Cal.) (trade coverage)
    publisher: UC Today and other trade coverage
    type: press
    url: https://www.uctoday.com/?p=748128
    date: '2026'
    access: search-only
    locator: search summary
  notes: The independent figure is from a cross-industry experiment and measures email time, so it is adjacent evidence
    for meeting capture; it caps the grade at C because no named professional-services deployment is attached. Some
    NBER authors were Microsoft employees (Microsoft reviewed the paper for privacy only).
  last_reviewed: '2026-10-19'
- id: professional-services-delivery-management-05
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: Sales-to-delivery handoff pack and delivery plan drafted from the deal record and SOW
  work_types:
  - document-production
  - coordination-scheduling
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: The step from signed deal to kickoff loses context between sales and delivery; Certinia says delivery
    teams should start with alignment and actionable deal strategy (CERTINIA-VEDA-2026).
  solution: Certinia lists a Sales-to-Delivery Handoff agent that connects closed deals to delivery kickoff, a Solution
    Architect agent that translates customer needs into solution designs, and an Implementation Plan agent that
    builds structured execution plans. It also describes converting requirements into phased implementation roadmaps
    (CERTINIA-VEDA-2026).
  outcomes:
  - lever: speed
    description: Vendor-stated faster client onboarding
    figure: 60% faster client onboarding
    measures: Client onboarding speed. The page gives no baseline, sample or definition of onboarding.
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Deal, scope and SOW held as structured records the agent can read (CERTINIA-VEDA-2026).
  - Engagement terms that address the scope of AI use, allocation of responsibilities, data protection and any agreed
    AI restrictions (ICMCI-AICODE-2026, section 7.3).
  risks_and_guardrails:
  - Government buyers may require approval of AI use in services, quality checks on AI outputs and records of AI
    use; Australia's model clauses do so (AGS-AIMODELCLAUSES-2025, Section 1).
  - Plans and SOW-derived scope statements are commitments; consultants who present AI-assisted output bear the
    same responsibility as for human work (ICMCI-AICODE-2026, section 2.2).
  human_checkpoints:
  - Engagement lead and delivery lead approve the handoff pack and plan against the signed SOW.
  - Client sign-off on the plan where the contract requires it.
  role_evolution: No source describes a role change for this step.
  notes: Certinia's page also claims proposal or SOW creation time falls from 8 hours to 1 hour; that belongs to
    the pursuit-proposals module.
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026'
    access: full
    locator: '''Precision scoping & planning''; Plan and Deliver agent lists; ''More gains across the lifecycle'''
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version
      1.0
    publisher: International Council of Management Consulting Institutes
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: sections 2.2, 7.3
  - ref: AGS-AIMODELCLAUSES-2025
    title: 'Legal update no. 327: Artificial Intelligence (AI) model clauses'
    publisher: Australian Government Solicitor (for the Digital Transformation Agency)
    type: regulator
    url: https://www.ags.gov.au/sites/default/files/Legal-update-no327.pdf
    date: '2025-04-04'
    access: full
    locator: Services where the seller uses AI (Section 1)
  last_reviewed: '2026-10-19'
- id: professional-services-delivery-management-06
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: Retrospective and lessons-learned drafting at engagement close
  work_types:
  - document-production
  - research-synthesis
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: Learnings from completed engagements are not captured in a form the next team can find; Certinia describes
    organising lessons learned into a searchable, firm-wide knowledge base (CERTINIA-VEDA-2026).
  solution: Certinia lists a Retrospective Drafter agent that captures key learnings and outcomes from completed
    projects, and a Knowledge Base agent that organises documentation into a searchable team resource (CERTINIA-VEDA-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: null
    measures: No figure for retrospective quality, reuse or time saved.
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Project records, time and financial data, and communications that can be summarised without breaching confidentiality
    (CALBAR-GENAI-2026, p.6).
  risks_and_guardrails:
  - Lessons drawn from one client's matter may expose confidential or privileged material when reused across matters
    (CALBAR-GENAI-2026, p.6; ABA-OP512-2024, Part II.B, p.7).
  - 'Client data used for templates or testing: the Law Society says use fictional data rather than client confidential
    information (LAWSOC-GENAI-2026, FAQ on templates and testing).'
  human_checkpoints:
  - Engagement lead edits and approves the retrospective; a confidentiality check strips client-identifying detail
    before it enters a shared knowledge base.
  role_evolution: No source describes a role change for this step.
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026'
    access: full
    locator: '''Value capture & knowledge transfer''; Manage agent list'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: professional-body
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.6
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: ABA Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.B, p.7
  - ref: LAWSOC-GENAI-2026
    title: 'Generative AI: the essentials'
    publisher: Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials
    date: '2026'
    access: full
    locator: FAQ 'Can I use client confidential and personal data ... to create templates or test'
  notes: Overlaps knowledge-management; kept here because it is the closeout step of delivery.
  last_reviewed: '2026-10-19'
- id: professional-services-delivery-management-07
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: Client progress and deliverable report drafting with AI-use disclosure and a source-verification gate
  work_types:
  - document-production
  - client-interaction
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Reports to clients are long and quickly produced; one failure shows the risk. Deloitte Australia's 237-page
    report to the Department of Employment and Workplace Relations had incorrect footnotes and references, including
    a fabricated quote from a federal court judgment and references to nonexistent research papers (CTV-DELOITTE-2025).
  solution: A generative AI system is used to help write the report, and the firm discloses that use. Deloitte's
    revised report disclosed that Azure OpenAI was used in writing it; the department said the substance and recommendations
    were unchanged (CTV-DELOITTE-2025). Professional codes now ask for disclosure when AI materially affects deliverables
    and for review before reliance (ICMCI-AICODE-2026, sections 3.3 and 7.1).
  outcomes:
  - lever: risk
    description: 'Negative outcome: partial refund of the contract fee after errors were found'
    figure: Deloitte agreed to repay the final instalment of a AUD 440,000 contract
    measures: The final instalment under a AUD 440,000 contract; the department said the amount would be made public
      after repayment. A later Senate-estimates figure of AUD 97,587 appears only in a search summary.
    provenance: independent
    source_ref: CTV-DELOITTE-2025
  prerequisites:
  - A verification step that checks every reference, quotation and footnote against its source before release (ABA-OP512-2024,
    Part II.D, pp.9-10, on court filings; the same logic applies to client reports).
  - Client contract terms on AI use, quality checks and records (AGS-AIMODELCLAUSES-2025, Section 1).
  risks_and_guardrails:
  - Consultants remain fully responsible for work products whether or not AI was used (ICMCI-AICODE-2026, section
    2.2).
  - Clients must be informed when AI materially contributes to analysis or deliverables, particularly where it affects
    methodology or reliance; routine productivity tools need not be individually disclosed (ICMCI-AICODE-2026, section
    3.3).
  - Insurers are described as looking at how AI-enabled services are supervised and disclosed, and that professional
    indemnity policies tend not to cover AI-related errors explicitly (DACBEACHCROFT-PI-2026).
  human_checkpoints:
  - Named author or partner verifies sources and signs the report.
  - Disclosure of AI use agreed with the client before delivery, not added after an error.
  role_evolution: Responsibility stays with the signing consultant or lawyer (ICMCI-AICODE-2026, section 2.2; CALBAR-GENAI-2026,
    p.4).
  evidence_grade: B
  sources:
  - ref: CTV-DELOITTE-2025
    title: Deloitte to partially refund Australian government for report with apparent AI-generated errors
    publisher: CTV News (Associated Press)
    type: press
    url: https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/
    date: '2025-10-07'
    access: full
    locator: paragraphs 1-6
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version
      1.0
    publisher: International Council of Management Consulting Institutes
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: sections 2.2, 3.3, 7.1
  - ref: AGS-AIMODELCLAUSES-2025
    title: 'Legal update no. 327: Artificial Intelligence (AI) model clauses'
    publisher: Australian Government Solicitor (for the Digital Transformation Agency)
    type: regulator
    url: https://www.ags.gov.au/sites/default/files/Legal-update-no327.pdf
    date: '2025-04-04'
    access: full
    locator: Section 1
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: ABA Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.D, pp.9-10
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: professional-body
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.4
  - ref: DACBEACHCROFT-PI-2026
    title: 'Professional indemnity insurance: risk of AI hallucinations'
    publisher: DAC Beachcroft
    type: firm
    url: https://www.dacbeachcroft.com/en/what-we-think/professional-indemnity-insurance-risk-of-ai-hallucinations
    date: '2026-09-28'
    access: full
    locator: Overview
  - ref: MANDARIN-DELOITTE-2025
    title: Deloitte AI slammed at committee, could face supplier sin bin
    publisher: The Mandarin (Julian Bajkowski)
    type: press
    url: https://www.themandarin.com.au/300809-deloitte-ai-slammed-at-commitee-could-face-supplier-sin-bin/
    date: '2025-10-10'
    access: search-only
    locator: standfirst (search-only)
  notes: 'Graded B on a named deployment (Deloitte Australia) with a reported failure; the report is a deliverable
    rather than a status report, so the quality-review and work-production modules hold the detailed evidence. Search-only:
    a search summary of The Mandarin says Senate estimates heard a refund of AUD 97,587 and that the department
    would introduce stricter AI rules for future contracts; not used in outcomes.'
  last_reviewed: '2026-10-19'
- id: professional-services-delivery-management-08
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: Matter-level AI usage and value measurement against pre-AI baselines, reported to clients
  work_types:
  - data-reporting
  - client-interaction
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Clients ask which AI is used on their matters and what it saves; firms mostly answer that they are still
    gathering data (TRI-LEGALWEEK-2026). In the Thomson Reuters Institute's 2026 AI in Professional Services Report,
    85% of law-firm respondents and 75% of corporate legal-department respondents said their organisation is not
    collecting ROI data on AI use or is unsure whether it does; 68% of corporate legal professionals do not know
    whether their outside firms use AI (TRI-DISCONNECT-2026).
  solution: Firms record AI usage by matter and compare outcomes with historical baselines for time and cost. The
    Institute recommends that law departments set baselines for how long matters took and cost historically and
    compare them with AI-enabled engagements (TRI-DISCONNECT-2026). Legora and Laurel announced on 13 Oct 2026 that,
    in a second phase, they will jointly develop measures of how Legora is used and the value it brings, with the
    measures decided in consultation with customers (LEGORA-LAUREL-2026).
  outcomes:
  - lever: risk
    description: none published; the vendors describe plans, not results
    figure: null
    measures: Legora and Laurel say phase two will decide which measures matter, how to calculate them and how to
      show them; no results given.
    provenance: vendor-published
    source_ref: LEGORA-LAUREL-2026
  prerequisites:
  - Historical matter data (hours, cost, duration) as a baseline (TRI-DISCONNECT-2026).
  - Time capture that records AI-platform work against client and matter (LEGORA-LAUREL-2026).
  - 'A GenAI strategy: a Thomson Reuters speaker said firms with one are 3.9 times more likely to achieve ROI, and
    only 22% of firms have one (TRI-LEGALWEEK-2026; speaker statement, no source data shown).'
  risks_and_guardrails:
  - Hourly billing must reflect actual time; savings cannot be hidden by billing hypothetical time (ABA-OP512-2024,
    Part II.F, p.12; CALBAR-GENAI-2026, p.8).
  - One corporate chief legal officer told the Institute they fear firms will cut time with AI but bill the hypothetical
    time (TRI-DISCONNECT-2026); measurement is the evidence either way.
  - 'Attribution is hard: telemetry improves measurement but not attribution of results to the consultant''s work
    (STANFORD-DEL-2026, p.3).'
  human_checkpoints:
  - Pricing or finance lead agrees metric definitions with the client before reporting.
  - Matter partner reviews client-facing AI value statements.
  role_evolution: Greenberg Traurig has a Chief Pricing and Innovation Officer and DLA Piper a senior managing director
    of AI innovation; both spoke on the client AI value conversation (TRI-LEGALWEEK-2026). A DLA Piper speaker advised
    firms to lead the AI ROI conversation rather than wait for the client (TRI-LEGALWEEK-2026).
  evidence_grade: C
  sources:
  - ref: TRI-DISCONNECT-2026
    title: The great AI disconnect (2026 AI in Professional Services Report findings)
    publisher: Thomson Reuters Institute (Zach Warren)
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/great-ai-disconnect
    date: '2026-03-18'
    access: full
    locator: '''Significant gaps in visibility and measurement''; ''Build an external-facing metrics program'''
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute (Bryce Engelland)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: sections 'Proving AI's path to saving clients money' and 'The pressure hasn't yet found a release valve'
  - ref: LEGORA-LAUREL-2026
    title: Legora and Laurel partner to capture the time lawyers spend in Legora as they work
    publisher: Legora
    type: vendor
    url: https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work
    date: '2026-10-13'
    access: full
    locator: paragraphs 5-6 (phase two)
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: ABA Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.F, p.12
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: professional-body
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.8
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives (Brynjolfsson and
      Petropoulos)'
    publisher: Stanford Digital Economy Lab
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: p.3 (attribution risk)
  notes: 'Firm-side counterpart of use case 12 (in-house). Grade C: the only firm-side commitment found is a vendor
    announcement of plans.'
  last_reviewed: '2026-10-19'
- id: professional-services-delivery-management-09
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: Engagement-level register of AI use for supervision, disclosure and billing narrative (idea)
  work_types:
  - data-reporting
  - review-assurance
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: 'Regulators and clients ask firms to record and disclose AI use, but tracking tools are rare: sophisticated
    tracking and compliance tools are in use by fewer than one in five firms, and work-product governance relies
    mainly on training and leadership pressure (ILTA-TECHSURVEY-2026). In the 2026 KPMG survey of 468 general counsel
    and senior legal leaders, 82% expect external providers to explain how they use AI (LEGALBUSINESS-KPMGGC-2026).'
  solution: 'Idea: each engagement keeps an automatic log of which AI tools were used on which tasks, who reviewed
    the output, and what the client permitted, feeding supervision, client disclosure and billing narratives. Related
    requirements exist: the ABA opinion suggests marking AI-generated material in client or firm files (ABA-OP512-2024,
    fn 52); the Law Society advises documenting inputs, outputs and errors when a tool keeps no history (LAWSOC-GENAI-2026);
    Australia''s model clauses require sellers to keep detailed records of AI use (AGS-AIMODELCLAUSES-2025); ICMCI
    says firms should document significant AI-supported decisions in proportion to risk (ICMCI-AICODE-2026, section
    3.6).'
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: No deployment or result found for an engagement-level AI-use register.
    provenance: self-reported
    source_ref: ILTA-TECHSURVEY-2026
  prerequisites:
  - AI tools that expose usage logs or an integration point with the PSA and document system.
  - A firm policy defining what counts as material AI use (ICMCI-AICODE-2026, section 3.3).
  risks_and_guardrails:
  - Logs of prompts and outputs may hold client confidential information and need their own access controls (CALBAR-GENAI-2026,
    pp.5-6).
  - 'Proportionality: routine productivity tools need not be individually disclosed (ICMCI-AICODE-2026, section
    3.3).'
  human_checkpoints:
  - Supervising partner reviews the register at set points and before client disclosure.
  role_evolution: Managerial lawyers must set clear AI policies and supervisors must make reasonable efforts to
    ensure compliance and training (ABA-OP512-2024, Part II.E, p.10; CALBAR-GENAI-2026, p.7).
  evidence_grade: D
  sources:
  - ref: ILTA-TECHSURVEY-2026
    title: ILTA Technology Survey 2026 Executive Summary
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: p.9; Q3.18 table p.5
  - ref: LEGALBUSINESS-KPMGGC-2026
    title: '''Be bold, be honest about it'' - GCs demand AI transparency from law firms'
    publisher: Legal Business (Theresa Hargreaves)
    type: press
    url: https://www.legalbusiness.co.uk/in-house/be-bold-be-honest-about-it-gcs-demand-ai-transparency-from-law-firms/
    date: '2026-04-29'
    access: full
    locator: paragraphs 2-3
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: ABA Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.E p.10, footnote 52
  - ref: LAWSOC-GENAI-2026
    title: 'Generative AI: the essentials'
    publisher: Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials
    date: '2026'
    access: full
    locator: section on client care and record-keeping
  - ref: AGS-AIMODELCLAUSES-2025
    title: 'Legal update no. 327: Artificial Intelligence (AI) model clauses'
    publisher: Australian Government Solicitor (for the Digital Transformation Agency)
    type: regulator
    url: https://www.ags.gov.au/sites/default/files/Legal-update-no327.pdf
    date: '2025-04-04'
    access: full
    locator: Section 1
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version
      1.0
    publisher: International Council of Management Consulting Institutes
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: sections 3.3, 3.6
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: professional-body
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: pp.5-7
  notes: 'Idea, labelled D: the requirements are discussed by bars, a professional body and buyers, but no deployed
    register was found. Legal Business also reports (not opened in depth) that HSBC''s global head of legal external
    engagement said AI will soon be a requirement for panel firms, and that some major clients already require firms
    to specify which work was done with AI.'
  last_reviewed: '2026-10-19'
- id: professional-services-delivery-management-10
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: Client AI-instruction register enforced per engagement (permitted tools, approvals, banned systems) (idea)
  work_types:
  - coordination-scheduling
  - review-assurance
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: 'Clients give contradictory AI instructions: a DLA Piper speaker said firms receive demands to use AI
    to hit savings targets in the same inbox as demands for warranties that models are unbiased and for permission
    before any AI use (TRI-LEGALWEEK-2026). Firm policies on client approval vary widely: 8% of firms with under
    50 lawyers require client approval before using generative AI, against 20% to 38% of larger groups (ILTA-TECHSURVEY-2026,
    Q3.18).'
  solution: 'Idea: record each client''s AI instructions at engagement set-up and have the delivery tooling check
    them when a task is assigned, flagging tools that are banned, unapproved or need consent. Requirements that
    point this way: California says a lawyer must follow client instructions or guidelines that restrict AI (CALBAR-GENAI-2026,
    p.7); ICMCI says consultants must comply with client instructions on AI tools and may raise concerns (ICMCI-AICODE-2026,
    section 5.4); Australia''s model clauses let a buyer ban specific AI systems (AGS-AIMODELCLAUSES-2025).'
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: No deployment or result found for per-engagement enforcement of client AI instructions.
    provenance: self-reported
    source_ref: TRI-LEGALWEEK-2026
  prerequisites:
  - Engagement letters or outside counsel guidelines that state the client's AI terms in a form that can be recorded
    (ICMCI-AICODE-2026, section 7.3).
  - A central list of approved and banned AI systems.
  risks_and_guardrails:
  - 'Register errors could cause a breach of client instructions; the register must be kept current as tools and
    clients'' terms change (CALBAR-GENAI-2026, p.4: periodic reassessment).'
  - Client guidelines can conflict with each other and with the firm's own AI strategy (TRI-LEGALWEEK-2026).
  human_checkpoints:
  - Engagement lead confirms the client's instructions at set-up and when they change.
  - Exceptions to a restriction need partner and client sign-off.
  role_evolution: No source describes a role change for this step.
  evidence_grade: D
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute (Bryce Engelland)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: section 'The contradictions in the room'
  - ref: ILTA-TECHSURVEY-2026
    title: ILTA Technology Survey 2026 Executive Summary
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: Q3.18 table, p.5
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: professional-body
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.7
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version
      1.0
    publisher: International Council of Management Consulting Institutes
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: sections 5.4, 7.3
  - ref: AGS-AIMODELCLAUSES-2025
    title: 'Legal update no. 327: Artificial Intelligence (AI) model clauses'
    publisher: Australian Government Solicitor (for the Digital Transformation Agency)
    type: regulator
    url: https://www.ags.gov.au/sites/default/files/Legal-update-no327.pdf
    date: '2025-04-04'
    access: full
    locator: Section 1
  notes: 'Idea, labelled D: requirements are published but no firm describes enforcing them in delivery tooling.'
  last_reviewed: '2026-10-19'
- id: professional-services-delivery-management-11
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: 'AI-adjusted engagement economics: fee-reasonableness and realisation tracking during delivery (idea)'
  work_types:
  - data-reporting
  - expert-judgment
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: When AI shortens a task, an hourly bill must show actual time and a flat fee may become unreasonable
    if little work was performed (ABA-OP512-2024, Part II.F, p.12). The SPI Research 2026 study of 245 firms reports
    84.8% say AI saves them time; the matching share who say it generates revenue is not visible on the public page
    (SPI-AI-2026). Am Law 100 worked rates rose almost 10% in Q1 2026 while the Thomson Reuters Law Firm Financial
    Index stayed flat at 55 (TRI-LFFI-Q1-2026); the Institute says most of the growth to end-2025 above pre-2022
    levels in fees worked per lawyer (16.8%) and profit per lawyer (8.4%) came from rate increases, not necessarily
    operational improvements (TRI-SOTLM-2026). Neither source attributes these movements to AI.
  solution: 'Idea: during delivery, compare actual effort, AI-assisted effort and fee basis on each engagement.
    Flag fixed-fee or capped matters where effort has fallen well below the fee basis, and hourly matters where
    write-downs or client queries rise, so the engagement lead can reprice, re-scope or explain value. California
    says flat fees may build in AI savings and that fee agreements should say how fees and costs are calculated
    (CALBAR-GENAI-2026, p.8). The Stanford paper argues AI augmentation lowers input cost observability (the same
    deliverable can be made with widely varying human time and compute) and, in its abstract, that AI tends to push
    consulting firms toward hybrid and asset-based pricing (STANFORD-DEL-2026, abstract and p.3).'
  outcomes:
  - lever: cost
    description: none published
    figure: null
    measures: No engagement-level result for AI-adjusted fee monitoring was found.
    provenance: independent
    source_ref: SPI-AI-2026
  prerequisites:
  - Time, fee-basis and AI-usage data joined at engagement level (see use cases 8 and 9).
  - Agreed fee structures that say how AI affects the fee (CALBAR-GENAI-2026, p.8; ABA-OP512-2024, Part II.F, pp.11-14).
  risks_and_guardrails:
  - General AI subscriptions are overhead; matter-specific AI costs may be billed only if disclosed in the fee agreement,
    at actual cost, without markup absent informed written consent (CALBAR-GENAI-2026, p.8).
  - A lawyer may not bill for time spent learning a tool they will use regularly (ABA-OP512-2024, Part II.F, p.14).
  - Value-based and outcome pricing face attribution limits that telemetry cannot remove (STANFORD-DEL-2026, p.3).
  human_checkpoints:
  - Pricing or finance partner reviews flagged engagements before any fee change is raised with the client.
  - Engagement lead documents the reasoning for any adjustment.
  role_evolution: Resource managers expect to shift from filling hours towards delivery success, profitability and
    outcomes if outcome pricing spreads; 1 in 2 respondents are unsure their organisation will adopt it (KANTATA-RMI-2026).
  evidence_grade: D
  sources:
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: ABA Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.F, pp.11-14
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: professional-body
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.8
  - ref: SPI-AI-2026
    title: The 2026 Impact of AI on Professional Services (SPI Research report page)
    publisher: SPI Research
    type: survey
    url: https://spiresearch.com/reports/2026-ai-professional-services-survey/
    date: '2026-07-14'
    access: full
    locator: '''The headline''; ''Part III: The Leak'''
  - ref: TRI-LFFI-Q1-2026
    title: 'Law Firm Financial Index Q1 2026: strong inputs, average output'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/lffi-q1-2026-strong-inputs-average-output
    date: '2026-05-13'
    access: full
    locator: '''Key insights'' and paragraph 4'
  - ref: TRI-SOTLM-2026
    title: 'State of the US Legal Market 2026 analysis: Will the AI bubble burst?'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble
    date: '2026-01-14'
    access: full
    locator: paragraph beginning 'In fact, these vulnerabilities become clearer' (profit and fees per lawyer)
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives (Brynjolfsson and
      Petropoulos)'
    publisher: Stanford Digital Economy Lab
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: p.3
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape
      Professional Services
    publisher: Kantata (Resource Management Institute study)
    type: vendor
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: paragraph 8
  notes: 'Idea, labelled D: the compliance and margin problems are discussed by bars and researchers, but no firm
    describes a tracking process. Pricing choices belong to scoping-pricing and firm-wide ROI to firm-finance; this
    use case covers the in-flight control only. KPMG''s survey (via Legal Business) says 87% of respondents prefer
    value or outcome-based pricing to time-based pricing (LEGALBUSINESS-KPMGGC-2026).'
  last_reviewed: '2026-10-19'
- id: professional-services-delivery-management-12
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: 'In-house: external-counsel AI metrics programme (baselines, disclosure questions, outside counsel guidelines)
    (idea)'
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: In-house (client-side) legal teams cannot see what their outside firms do with AI. In the ACC and Everlaw
    survey, 59% say they do not know whether their outside counsel uses generative AI on their matters; of the 37%
    who say some or all firms do, 59% have seen no clear savings (ACC-TRANSPARENCY-2025). In the Institute's 2026
    report, 75% of corporate legal-department respondents are not collecting ROI data or are unsure (TRI-DISCONNECT-2026).
  solution: 'Idea: the law department sets baselines for how long matters took and cost, asks firms standard AI
    transparency questions, adds AI provisions to outside counsel guidelines and RFPs, and compares AI-enabled matters
    with the baselines. ACC recommends asking which tools, which matters and how accuracy is validated, and formalising
    this in guidelines (ACC-TRANSPARENCY-2025); the Institute recommends an external-facing metrics programme (TRI-DISCONNECT-2026).'
  outcomes:
  - lever: cost
    description: none published
    figure: null
    measures: No in-house team has published results of such a programme.
    provenance: independent
    source_ref: TRI-DISCONNECT-2026
  prerequisites:
  - Historical matter cost and duration data (TRI-DISCONNECT-2026).
  - Outside counsel guidelines and RFPs that carry AI disclosure and quality-assurance terms (ACC-TRANSPARENCY-2025).
  risks_and_guardrails:
  - Clients' own instructions conflict (demand AI use, ban it without permission, refuse to pay for AI work) (TRI-LEGALWEEK-2026).
  - Data held by firms about client matters is confidential; metrics should rely on matter-level aggregates the
    firm can share.
  human_checkpoints:
  - Legal-operations lead reviews metrics with outside counsel before using them in fee discussions.
  role_evolution: About three-quarters of both firm and department respondents said the firm should start the AI
    conversation, but the Institute urges departments to lead if firms do not (TRI-DISCONNECT-2026).
  evidence_grade: D
  sources:
  - ref: ACC-TRANSPARENCY-2025
    title: 'The Transparency Gap: In-house Counsel Lack Clarity on Law Firms'' AI Use'
    publisher: Association of Corporate Counsel (ACC Docket)
    type: professional-body
    url: https://docket.acc.com/node/4313
    date: '2025-11-05'
    access: full
    locator: paragraphs 2-4; 'What in-house counsel can do now'
  - ref: TRI-DISCONNECT-2026
    title: The great AI disconnect (2026 AI in Professional Services Report findings)
    publisher: Thomson Reuters Institute (Zach Warren)
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/great-ai-disconnect
    date: '2026-03-18'
    access: full
    locator: '''Significant gaps in visibility and measurement''; ''More & better communication is needed'''
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute (Bryce Engelland)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: '''The contradictions in the room'''
  - ref: EVERLAW-OUTSIDECOUNSEL-2026
    title: Setting Expectations for GenAI Usage and Pricing with Outside Counsel
    publisher: Everlaw
    type: vendor
    url: https://www.everlaw.com/blog/corporations/setting-expectations-for-genai-usage-and-pricing-with-outside-counsel/
    date: '2026-01-29'
    access: full
    locator: paragraphs 2-4
  - ref: LEGALBUSINESS-KPMGGC-2026
    title: '''Be bold, be honest about it'' - GCs demand AI transparency from law firms'
    publisher: Legal Business (Theresa Hargreaves)
    type: press
    url: https://www.legalbusiness.co.uk/in-house/be-bold-be-honest-about-it-gcs-demand-ai-transparency-from-law-firms/
    date: '2026-04-29'
    access: full
    locator: paragraphs 2-3, 7-9
  notes: 'In-house. Idea, labelled D: ACC publishes sample guidelines and a question list (named in the ACC article),
    but no in-house team has published a measured programme. A 2024 LexisNexis survey found 80% of Fortune 1000
    executives expected reduced billing from generative AI while only 9% of large law-firm leaders said clients
    had told them so (LEXISNEXIS-GENAI-2024); older baseline.'
  last_reviewed: '2026-10-19'
- id: professional-services-delivery-management-13
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  title: Shared client workspace with live task status, replacing emailed status updates
  work_types:
  - client-interaction
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Status travels by email and separate checklists, and someone has to reconstruct it for the client (HARVEY-ORCH-2026).
  solution: Harvey says a task can be assigned to another lawyer or shared with the client while retaining the matter
    context, and that its Spaces feature supports work with teams across organisations (HARVEY-ORCH-2026). The post
    does not describe how client access is limited.
  outcomes:
  - lever: experience
    description: none published
    figure: null
    measures: No client-experience or time figure.
    provenance: vendor-published
    source_ref: HARVEY-ORCH-2026
  prerequisites:
  - Per-client access controls; the Cal Bar guidance says agentic tools must not transmit client data externally
    without safeguards and human review (CALBAR-GENAI-2026, p.6).
  risks_and_guardrails:
  - Information from one matter may reach people who should not see it (ABA-OP512-2024, Part II.B, p.7).
  - A client may restrict AI use on its matters; the shared workspace must respect those instructions (CALBAR-GENAI-2026,
    p.7).
  human_checkpoints:
  - Engagement lead decides which tasks and outputs are visible to the client.
  role_evolution: No source describes a role change for this step.
  evidence_grade: C
  sources:
  - ref: HARVEY-ORCH-2026
    title: Making Harvey the Orchestration Layer for Legal Work
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/legal-work-orchestration
    date: '2026-10-15'
    access: full
    locator: '''Give Every Task the Context it Needs'''
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: professional-body
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: pp.6-7
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: ABA Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.B, p.7
  notes: 'Thin evidence: a single sentence in a vendor launch post. Included because client reporting is in scope
    for the module.'
  last_reviewed: '2026-10-19'
```

---

## 3. Module notes

### Processes and key steps (work types)

1. Mobilisation and handoff from sale to delivery: confirm scope, terms and client AI instructions (document-production, coordination-scheduling).
2. Plan, work breakdown, tasking and review-gate design (coordination-scheduling).
3. Status tracking and engagement health reporting (data-reporting).
4. Risk, issue and dependency tracking (data-reporting, expert-judgment).
5. Client communication: steering meetings, progress and deliverable reports, shared workspaces (client-interaction, document-production).
6. Change control: scope changes and change orders (expert-judgment, client-interaction).
7. Engagement economics: budget against actual, utilisation, work in progress, realisation and forecast (data-reporting).
8. Closeout, retrospective and handover (document-production).

### Common pain points

- Status is rebuilt by hand from email and separate checklists (HARVEY-ORCH-2026); Certinia calls this "manual status-chasing" (CERTINIA-VEDA-2026).
- Fragmented data blocks AI: 47% of resource-management respondents cite poor or fragmented data, and 49% cite limited understanding of where AI applies (KANTATA-RMI-2026).
- Firms cannot show clients matter-level AI savings; the usual answer is "still gathering the data" (TRI-LEGALWEEK-2026).
- Clients send contradictory AI instructions: expect AI use and savings, and also require permission before any AI use (TRI-LEGALWEEK-2026).
- Partners are not talking to clients about AI: only about one-third of heavy-AI-user partners have discussed it with at least 60% of their clients (TRI-STANDOUT-2026).
- Strategy and practice diverge: among professionals whose organisation has a named AI strategy, 35% say day-to-day practice does not match it (TR-FOP-2026).
- Shadow AI: 34% of professionals use AI tools their organisation has not sanctioned (TR-FOP-2026).
- Thin utilisation and margin in project-based firms: A&E firms report utilisation just under 60% and operating profit of 16.7% (DELTEK-CLARITY-2026; adjacent sector).

### Metrics and benchmarks (what each measures)

- **Project-level AI use.** 43.6% of projects now use AI, up from 23.1% in 2025; 84.8% say AI saves them time (SPI Research, 245 professional services organisations; SPI-AI-2026). The comparison share for revenue is locked on the public page.
- **Measurable impact (project-based firms).** 38% of 896 A&E respondents reported measurable positive business impact from AI; AI adoption rose from 53% to 70% year on year; 39% said it is too early or they are still piloting (DELTEK-CLARITY-2026; vendor survey, adjacent sector). Among 917 government contractors, 45% were unclear on ROI and 5% said they were "fully developed" in AI maturity (IT and security respondents) (DELTEK-CLARITY-2026).
- **Resource management readiness.** 39% traditional staffing, 30% exploring, 31% beyond experimentation; 52.7% not equipped to manage hybrid human-agent teams and 4% well equipped; 7.3% say outcome data is easily accessible and routinely used in staffing; 73.4% say knowing which people or agent combinations produce strong outcomes would be very or extremely valuable (44 organisations; vendor-commissioned; KANTATA-RMI-2026).
- **Strategy and value.** 66% of professionals say AI meets or exceeds expectations where a named strategy exists, 22% where none does (1,816 professionals, Mar-Apr 2026; TR-FOP-2026). A Thomson Reuters speaker said firms with a GenAI strategy are 3.9 times more likely to achieve ROI and only 22% have one (speaker statement; TRI-LEGALWEEK-2026).
- **Client demand against delivery.** 78% of corporate clients say AI-enabled quality gains are very important or essential; 6% say most or all providers deliver them; 32% are reconsidering or plan to reconsider providers within 12 months (TR-FOP-2026).
- **Visibility and measurement.** 68% of corporate legal professionals do not know whether outside firms use AI; 85% of law-firm and 75% of corporate respondents are not collecting ROI data or are unsure (TRI-DISCONNECT-2026). 59% of ACC and Everlaw respondents do not know whether outside counsel uses generative AI; among the 37% who say some or all firms do, 59% have seen no clear savings (ACC-TRANSPARENCY-2025; in-house).
- **Firm policy baseline.** 94% of 508 firms are engaged with generative AI; a formal policy exists at 57% of firms under 50 lawyers and 80% to 98% of larger groups; "must obtain client approval" is 8% (under 50) to 38% (350-699); "specific training required before use" is 11% to 72% (ILTA-TECHSURVEY-2026, Q3.18). Sophisticated tracking and compliance tools are in use by under one in five firms (ILTA-TECHSURVEY-2026, p.9).
- **Strategy confidence.** 36% of stand-out lawyers strongly agree their firm has a clear AI strategy; 25% strongly agree it has a plan for monetising AI use (116 firm-leader interviews and 2,527 client-nominated lawyers; TRI-STANDOUT-2026). Partners embedded in daily AI use are nine times more likely to report significant efficiency and quality impact than minimal users (TRI-STANDOUT-2026).
- **Client expectations.** 82% of 468 GCs expect external providers to explain how they use AI; 87% prefer value or outcome-based pricing to time-based pricing (KPMG survey via LEGALBUSINESS-KPMGGC-2026; KPMG's landing page confirms the 468-GC sample, KPMG-GCOUTLOOK-2026; in-house). A 2024 LexisNexis survey (266 respondents) found 80% of Fortune 1000 executives expected reduced billing from generative AI, while 9% of large law-firm leaders said clients had told them so (LEXISNEXIS-GENAI-2024).
- **Search-only.** A PMI Ireland survey of 122 project managers reports 83% agree governance processes for AI are not in place (PMIIRELAND-AI-2024, search summary).
- **Quality evidence (all adjacent; none is delivery management).** In a pre-registered trial of 133 patent lawyers, AI raised blinded-graded quality by 0.34 SD at 10 days and 0.38 SD at 90 days; the post-test advantage without AI was concentrated among senior lawyers, and junior scores bifurcated (NBER-AUTOR-2026; study run and funded by Google). In an experiment with BCG on 758 consultants, AI users completed 12.2% more tasks and 25.1% faster on tasks inside the frontier, and were 19% less likely to be correct on a complex managerial task outside it (HBS-DELLACQUA-2023). In a 66-firm, 7,137-worker experiment, workers who used an integrated tool spent two fewer hours a week on email and no shift in task mix was detected (NBER-DILLON-2025). OpenAI's GDPval benchmark includes Project Management Specialists among 44 occupations; no occupation-level result was extracted (GDPVAL-OPENAI-2025). A Stanford audit of 1,500 workers' preferences across 844 tasks in 104 occupations introduces a Human Agency Scale for how much human involvement workers want; no project-management result was extracted (WORKBANK-STANFORD-2025). **Not found:** override rates, reviewer catch rates, parallel runs or inspection outcomes for AI status reports, risk scores, forecasts or change-order detection.

### Guardrails and regulatory points

- **ABA Formal Opinion 512 (29 Jul 2024).** Part II.B: informed client consent is required before inputting client information into a self-learning tool that could disclose it (p.7). Part II.C: consider client communication about AI, and the engagement agreement is a logical place for disclosure (pp.8-9). Part II.E: managerial lawyers must set clear AI policies; supervisors must ensure training; one suggestion is to mark AI-generated material in client or firm files (pp.10-11, fn 52). Part II.F: hourly billing is for actual time; the same flat fee may be unreasonable if a tool makes the work much quicker; general-overhead tools are not billable; time to learn a regularly used tool is not billable (pp.11-14) (ABA-OP512-2024).
- **California (revised guidance approved 14 May 2026).** Supervision and verification grow with autonomy; periodic reassessment of the system; agentic systems must not transmit client information externally without safeguards and human review; follow client AI restrictions; hourly billing reflects time actually spent; flat fees may build in AI savings; general subscriptions are overhead; per-matter AI costs need disclosure, actual cost and no markup without informed written consent (CALBAR-GENAI-2026, pp.3-9; CALBAR-ETHICSHUB-2026).
- **England and Wales.** The Law Society says professional duties apply whether AI was used by the solicitor or by anyone under their supervision, advises communicating with clients on AI use and documenting inputs, outputs and errors where a tool keeps no history, and notes that the SRA has no specific guidance on disclosure of AI use for client care (LAWSOC-GENAI-2026). A secondary report says the SRA updated its supervision guidance on 12 Jun 2026: risk-based supervision that firms must be able to evidence, with AI outputs subject to human review and an authorised individual retaining ultimate responsibility; the SRA's own page was not opened (LAWYERMONTHLY-SRA-2026).
- **Management consulting.** ICMCI's code (Version 1.0, May 2026): AI does not dilute accountability (2.2); clients shall be informed when AI materially contributes, though routine productivity tools need not be individually disclosed (3.3); firms should document significant AI-supported decisions in proportion to risk (3.6); comply with client AI instructions (5.4); disclose material AI use and limitations (7.1); engagement terms should address AI scope and restrictions, with ISO 20700:2017 recommended (7.3) (ICMCI-AICODE-2026).
- **Buyer contract terms.** Australia's model clauses (published 17 Mar 2025) for services where the seller uses AI require buyer approval of AI use, quality-assurance checks on outputs and detailed records of AI use, and let buyers ban named AI systems (AGS-AIMODELCLAUSES-2025).
- **EU AI Act.** Applicable from 2 Aug 2026; high-risk use cases including employment and management of workers apply from 2 Dec 2027 after the AI Omnibus (in force 27 Jul 2026). Relevant if delivery tooling allocates work to or monitors staff (EC-AIACT-2026).
- **Risk frameworks.** NIST's AI RMF 1.0 and Generative AI Profile (NIST-AI-600-1, 26 Jul 2024) give a general risk-management vocabulary; NIST says the RMF is being revised (NIST-AIRMF-2024).
- **Insurance.** Professional indemnity policies tend not to explicitly cover AI-related errors, and insurers are described as focusing disclosure requirements on how AI-enabled services are supervised and disclosed (DACBEACHCROFT-PI-2026).
- **Recording consent.** A class action filed Aug 2025 alleges an AI meeting assistant recorded conversations without participants' consent; these are allegations (KJZZ-OTTER-2025). Search-only: coverage of the consolidated case, *In re Otter.AI Privacy Litigation*, disagrees on how far the motion to dismiss succeeded (OTTER-LITIGATION-2026).

### Frontier signals (dated)

- 2025-03-17: Australian Commonwealth publishes AI model clauses covering consultants who use AI (AGS-AIMODELCLAUSES-2025).
- 2025-08-15: Class action filed against Otter.ai over AI meeting recording (KJZZ-OTTER-2025).
- 2025-10-07: Deloitte Australia to repay part of an AUD 440,000 contract after AI-related errors (CTV-DELOITTE-2025).
- 2025-11-05: ACC article on the transparency gap between in-house teams and law firms (ACC-TRANSPARENCY-2025).
- 2026-03-13: Legalweek panels on the firm and client AI value divide (TRI-LEGALWEEK-2026).
- 2026-03-18: Thomson Reuters Institute reports visibility and ROI-measurement gaps (TRI-DISCONNECT-2026).
- 2026-04-09: Kantata and Resource Management Institute study of resource-management readiness (KANTATA-RMI-2026).
- 2026-04-29: Legal Business reports KPMG's GC survey; HSBC's head of legal external engagement said AI will soon be a requirement for panel firms (LEGALBUSINESS-KPMGGC-2026; HSBC point not opened in depth).
- 2026-05-14: California approves revised guidance covering agentic AI (CALBAR-ETHICSHUB-2026).
- 2026-05: ICMCI adopts its AI code for management consultants (ICMCI-AICODE-2026).
- 2026-06-12: SRA supervision guidance updated (secondary report; LAWYERMONTHLY-SRA-2026).
- 2026-07-27: EU AI Omnibus enters into force; employment-related high-risk rules apply from 2 Dec 2027 (EC-AIACT-2026).
- 2026-08-23: Stanford and USC paper on consulting pricing under agentic AI (STANFORD-DEL-2026).
- 2026-10: SPI Research publishes its 2026 AI study; Gartner abstracts on PMOs and AI agents seen in search, one dated 14 Oct 2026 (SPI-AI-2026; GARTNER-PMO-2026, search-only).
- 2026-10-13: Legora and Laurel announce a second phase to measure AI usage and value (LEGORA-LAUREL-2026).
- 2026-10-15: Harvey launches Legal Work Orchestration and says it expects agents to take on an additional 20% of workflow steps within six months (HARVEY-ORCH-2026).

### Workforce and role effects

- Resource management is mostly operational: 72% of respondents say it is primarily or solely operational; practitioners say they want more strategic, outcome-aware roles (KANTATA-RMI-2026).
- Project managers in the Finnish study see AI as an "assistant not replacement"; the authors read this as boundary work preserving human authority (EINFORMATICA-SAINIO-2026).
- PMI said in 2023 that interpersonal "power skills" will stay crucial (PMI-AI-2023; older).
- Harvey says lawyers will spend more attention on directing the matter and reviewing consequential outputs (HARVEY-ORCH-2026).
- New roles: Greenberg Traurig's Chief Pricing and Innovation Officer and DLA Piper's senior managing director of AI innovation spoke on client AI value (TRI-LEGALWEEK-2026). ILTA firms expect added headcount in IT, innovation, security, training, KM and data science (ILTA-TECHSURVEY-2026).
- Early-career effects: 71% of professionals say early-career roles need structured support from experienced peers; 48% fear a negative effect on independent judgment development (TR-FOP-2026). In the patent trial, junior lawyers showed no average gain in unaided performance (NBER-AUTOR-2026; adjacent task; belongs to talent-learning).
- Where a named strategy and practice diverge, 30% say there is no shared understanding of what the strategy means (TR-FOP-2026).

### Objections and concerns practitioners raise

- Clients fear time is cut with AI while billing continues for the time the task would have taken; one corporate legal respondent said billing had stayed the same (TRI-DISCONNECT-2026; in-house).
- An itemised hourly bill undersells value when AI compresses hours into minutes; one panelist proposed a return to a single-line services bill and doubted client acceptance (TRI-LEGALWEEK-2026).
- ROI measurement rests on conventional wisdom rather than evidence (Ropes & Gray speaker; TRI-LEGALWEEK-2026).
- Using AI mainly to justify higher rates leaves firms exposed if client budgets tighten (TRI-SOTLM-2026).
- Attribution risk limits outcome-based fees however well results are measured (STANFORD-DEL-2026, p.3).
- Organisational security and governance policy, not individual resistance, limits AI use by project managers (EINFORMATICA-SAINIO-2026).
- Firms may be reluctant to discuss AI with clients because of quality and accuracy concerns (TRI-DISCONNECT-2026).
- A survey respondent: "Until accuracy and quality improve, it is an expensive toy" (ILTA-TECHSURVEY-2026, p.3).
- Search-only: Gartner abstract warns about PMOs deploying AI agents without solid foundations (GARTNER-PMO-2026).

### Interview probes for an advisor

1. Take your last live engagement. Who assembled the status and risk view for the client, how long did it take each cycle, and which part would you let an AI draft without a person checking it?
2. Which of your clients have written AI terms (approval, banned tools, records, disclosure, no payment for AI work), and how does a delivery team find out those terms mid-engagement?
3. When AI shortens a task on a fixed-fee, capped or hourly engagement, who sees it, where is it recorded, and what happens to the hours saved (resold, redeployed, written down, passed to the client)?
4. For one recent engagement, what evidence could you show a client of what AI changed (baseline hours, time entries, review outcomes), and what would you need that you do not have?
5. When an agent completes a delivery step, who is the named reviewer, and what record shows how often the reviewer changes or rejects its output?

---

## 4. Routed to other modules

- **billing-collections:** Legora-Laurel automatic time-entry capture for work done in the AI platform (phase one of the 13 Oct 2026 partnership) (LEGORA-LAUREL-2026); ABA and California rules on AI costs as overhead or expense (ABA-OP512-2024, pp.12-14; CALBAR-GENAI-2026, p.8).
- **staffing-resourcing:** hybrid human-agent team readiness (52.7% not equipped) and outcome data for staffing (KANTATA-RMI-2026); Certinia Resourcing, Work Reallocation and Shortlisting agents (CERTINIA-VEDA-2026); EU AI Act treatment of AI that manages workers (EC-AIACT-2026).
- **scoping-pricing:** pricing-model map by outcome and input-cost observability (STANFORD-DEL-2026); GC preference for value or outcome-based pricing (LEGALBUSINESS-KPMGGC-2026; in-house); flat-fee guidance (CALBAR-GENAI-2026, p.8).
- **firm-finance:** firm-wide AI ROI and rates against profit (TRI-SOTLM-2026; TRI-LFFI-Q1-2026); SPI's four-foundations argument and "the leak" (SPI-AI-2026).
- **quality-review:** verification of AI output before release and court-filing duties (ABA-OP512-2024, Part II.D; CTV-DELOITTE-2025); jagged-frontier evidence (HBS-DELLACQUA-2023).
- **acceptance-risk:** AI clauses in engagement letters and buyer contracts (ICMCI-AICODE-2026, 7.3; AGS-AIMODELCLAUSES-2025); professional indemnity insurance questions (DACBEACHCROFT-PI-2026).
- **talent-learning:** the patent-drafting trial's junior and senior effects (NBER-AUTOR-2026); early-career findings (TR-FOP-2026).
- **knowledge-management:** retrospective and knowledge-base agents (CERTINIA-VEDA-2026) overlap with use case 6.
- **pursuit-proposals:** Certinia's claimed fall in proposal or SOW creation time from 8 hours to 1 hour (CERTINIA-VEDA-2026).
- **work-production:** report drafting itself, as opposed to the engagement-level disclosure and verification gate in use case 7.

---

## 5. Sources

Access: `full` means opened and read; `search-only` means seen in search results only. Dates are publication dates unless the note says otherwise.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ABA-OP512-2024 | Formal Opinion 512: Generative Artificial Intelligence Tools | ABA Standing Committee on Ethics and Professional Responsibility | professional-body | https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf | 2024-07-29 | full |
| ACC-TRANSPARENCY-2025 | The Transparency Gap: In-house Counsel Lack Clarity on Law Firms' AI Use | Association of Corporate Counsel (ACC Docket) | professional-body | https://docket.acc.com/node/4313 | 2025-11-05 | full |
| AGS-AIMODELCLAUSES-2025 | Legal update no. 327: Artificial Intelligence (AI) model clauses | Australian Government Solicitor (for the Digital Transformation Agency) | regulator | https://www.ags.gov.au/sites/default/files/Legal-update-no327.pdf | 2025-04-04 | full |
| CALBAR-ETHICSHUB-2026 | Ethics and Technology Resources (State Bar of California) | State Bar of California | professional-body | https://www.calbar.ca.gov/Attorneys/Conduct-Discipline/Ethics/Ethics-Technology-Resources | 2026-05-14 | full |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision) | State Bar of California, Standing Committee on Professional Responsibility and Conduct | professional-body | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05-14 | full |
| CERTINIA-VEDA-2026 | Veda AI: System of Action for Professional Services | Certinia | vendor | https://certinia.com/solutions/ai | 2026 | full |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors | CTV News (Associated Press) | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 | full |
| DACBEACHCROFT-PI-2026 | Professional indemnity insurance: risk of AI hallucinations | DAC Beachcroft | firm | https://www.dacbeachcroft.com/en/what-we-think/professional-indemnity-insurance-risk-of-ai-hallucinations | 2026-09-28 | full |
| DELTEK-CLARITY-2026 | The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity Pressures for Project-Based Businesses | Deltek | vendor | https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/ | 2026-05-12 | full |
| EC-AIACT-2026 | AI Act (Regulatory framework for AI) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10 | full |
| EINFORMATICA-SAINIO-2026 | Realising the Role of Generative AI Among Project Management Professionals (Sainio, Kettunen, Abrahamsson) | e-Informatica Software Engineering Journal, vol. 20, no. 1 | academic | https://www.e-informatyka.pl/einformatica/volumes/volume-2026/issue-1/article-4/ | 2026 | full |
| EVERLAW-OUTSIDECOUNSEL-2026 | Setting Expectations for GenAI Usage and Pricing with Outside Counsel | Everlaw | vendor | https://www.everlaw.com/blog/corporations/setting-expectations-for-genai-usage-and-pricing-with-outside-counsel/ | 2026-01-29 | full |
| GARTNER-PMO-2026 | Gartner Insights abstracts on PMOs and AI agents (two documents: 8504777 and 8153030) | Gartner | vendor | https://www.gartner.com/en/documents/8504777 | 2026 | search-only |
| GDPVAL-OPENAI-2025 | GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks (arXiv 2510.04374) | OpenAI (Patwardhan et al.) | academic | https://arxiv.org/abs/2510.04374 | 2025-10 | full |
| HARVEY-ORCH-2026 | Making Harvey the Orchestration Layer for Legal Work | Harvey | vendor | https://www.harvey.ai/blog/legal-work-orchestration | 2026-10-15 | full |
| HBS-DELLACQUA-2023 | Navigating the Jagged Technological Frontier (HBS Working Paper 24-013) | Harvard Business School | academic | https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 | 2023-09 | full |
| ICMCI-AICODE-2026 | Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version 1.0 | International Council of Management Consulting Institutes | professional-body | https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf | 2026-05 | full |
| ILTA-TECHSURVEY-2026 | ILTA Technology Survey 2026 Executive Summary | International Legal Technology Association | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 | full |
| KANTATA-RMI-2026 | New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services | Kantata (Resource Management Institute study) | vendor | https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services | 2026-04-09 | full |
| KJZZ-OTTER-2025 | Class-action suit claims Otter AI secretly records private work conversations | KJZZ / NPR | press | https://www.kjzz.org/npr-top-stories/2025-08-15/class-action-suit-claims-otter-ai-secretly-records-private-work-conversations | 2025-08-15 | full |
| KPMG-GCOUTLOOK-2026 | 2026 KPMG Global General Counsel Outlook (landing page, Kazakhstan site) | KPMG | firm | https://kpmg.com/kz/en/insights/2026/06/global-general-counsel-outlook.html | 2026-06 | full |
| LAWSOC-GENAI-2026 | Generative AI: the essentials | Law Society of England and Wales | professional-body | https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials | 2026 | full |
| LAWYERMONTHLY-SRA-2026 | SRA Issues Post-Mazur Supervision Guidance - SDT Fines and AI Oversight Rules for Law Firms | Lawyer Monthly (George Daniel) | press | https://www.lawyer-monthly.com/2026/06/sra-post-mazur-supervision-guidance-2026/ | 2026-06-12 | full |
| LEGALBUSINESS-KPMGGC-2026 | 'Be bold, be honest about it' - GCs demand AI transparency from law firms | Legal Business (Theresa Hargreaves) | press | https://www.legalbusiness.co.uk/in-house/be-bold-be-honest-about-it-gcs-demand-ai-transparency-from-law-firms/ | 2026-04-29 | full |
| LEGORA-LAUREL-2026 | Legora and Laurel partner to capture the time lawyers spend in Legora as they work | Legora | vendor | https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work | 2026-10-13 | full |
| LEXISNEXIS-GENAI-2024 | New Survey Data from LexisNexis Points to Seismic Shifts in Law Firm Business Models and Corporate Legal Expectations Due to Generative AI | LexisNexis Legal & Professional | vendor | https://www.lexisnexis.com/community/amp-pressroom/new-survey-data-from-lexisnexis-points-to-seismic-shifts-in-law-firm-business-models-and-corporate-legal-expectations-due-to-generative-ai | 2024-01-31 | full |
| MANDARIN-DELOITTE-2025 | Deloitte AI slammed at committee, could face supplier sin bin | The Mandarin (Julian Bajkowski) | press | https://www.themandarin.com.au/300809-deloitte-ai-slammed-at-commitee-could-face-supplier-sin-bin/ | 2025-10-10 | search-only |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER WP 35720) | National Bureau of Economic Research | academic | https://www.nber.org/papers/w35720 | 2026-09 | full |
| NBER-DILLON-2025 | Shifting Work Patterns with Generative AI (NBER WP 33795) | National Bureau of Economic Research | academic | https://www.nber.org/papers/w33795 | 2025-05 | full |
| NIST-AIRMF-2024 | AI Risk Management Framework (AI RMF 1.0) and Generative AI Profile NIST-AI-600-1 | NIST | standard-setter | https://www.nist.gov/itl/ai-risk-management-framework | 2024-07-26 | full |
| OTTER-LITIGATION-2026 | In re Otter.AI Privacy Litigation, 5:25-cv-06911-EKL (N.D. Cal.) (trade coverage) | UC Today and other trade coverage | press | https://www.uctoday.com/?p=748128 | 2026 | search-only |
| PMI-AI-2023 | Demand Increases for Project Professionals with AI Skills (PMI press release) | Project Management Institute | professional-body | https://www.pmi.org/about/press-media/press-releases/demand-increases-for-project-professionals-with-ai-skills | 2023-09 | full |
| PMIIRELAND-AI-2024 | PMI survey reveals 83% of project managers say AI lacks governance in sector | Irish Tech News (PMI Ireland Chapter survey) | press | https://irishtechnews.ie/pmi-reveals-83-percent-of-project-managers/amp/ | 2024 | search-only |
| SPI-AI-2026 | The 2026 Impact of AI on Professional Services (SPI Research report page) | SPI Research | survey | https://spiresearch.com/reports/2026-ai-professional-services-survey/ | 2026-07-14 | full |
| STANFORD-DEL-2026 | Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives (Brynjolfsson and Petropoulos) | Stanford Digital Economy Lab | academic | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | 2026-08-23 | full |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 | full |
| TRI-DISCONNECT-2026 | The great AI disconnect (2026 AI in Professional Services Report findings) | Thomson Reuters Institute (Zach Warren) | survey | https://www.thomsonreuters.com/en/institute/articles/great-ai-disconnect | 2026-03-18 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute (Bryce Engelland) | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-LFFI-Q1-2026 | Law Firm Financial Index Q1 2026: strong inputs, average output | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/lffi-q1-2026-strong-inputs-average-output | 2026-05-13 | full |
| TRI-SOTLM-2026 | State of the US Legal Market 2026 analysis: Will the AI bubble burst? | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble | 2026-01-14 | full |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 | full |
| WORKBANK-STANFORD-2025 | Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce (arXiv 2506.06576) | Stanford University researchers | academic | https://arxiv.org/abs/2506.06576 | 2025-06 | full |

Notes on individual sources:

- **ABA-OP512-2024:** Copy hosted by LawSites; americanbar.org returned 403 to curl. Opened and read in full (Parts II.B, II.C, II.E, II.F).
- **ACC-TRANSPARENCY-2025:** Summarises an ACC and Everlaw survey (657 respondents per a search-result summary; sample size not given in the article itself). In-house.
- **AGS-AIMODELCLAUSES-2025:** Opened through the r.jina.ai mirror. Model clauses published 17 Mar 2025.
- **CALBAR-ETHICSHUB-2026:** Page states the Board of Trustees approved the revised guidance on 14 May 2026 (original published 16 Nov 2023).
- **CALBAR-GENAI-2026:** Date is the Board of Trustees approval date stated on CALBAR-ETHICSHUB-2026. Page locators are the PDF's printed pages.
- **CERTINIA-VEDA-2026:** Vendor product page read 19 Oct 2026; no publication date shown. Cites IDC MarketScape for AI-Enabled PSA Applications 2025-2026 (Dec 2025).
- **CTV-DELOITTE-2025:** Opened through the r.jina.ai mirror.
- **DELTEK-CLARITY-2026:** Vendor survey: 917 US and Canadian government contractors and 896 architecture and engineering firms.
- **EC-AIACT-2026:** Page read Oct 2026; it describes the AI Omnibus as in force from 27 July 2026.
- **EINFORMATICA-SAINIO-2026:** Abstract and reference list read; full text not opened. Month not shown.
- **EVERLAW-OUTSIDECOUNSEL-2026:** Vendor blog on the ACC and Everlaw survey. In-house.
- **GARTNER-PMO-2026:** Seen only in a search summary: a July 2026 document warning about PMOs deploying AI agents without foundations, and 'Predicts 2027: Program and Portfolio Management' (14 Oct 2026). Which URL is which was not confirmed. Second URL: https://www.gartner.com/en/documents/8153030.
- **GDPVAL-OPENAI-2025:** Vendor-authored benchmark. Project Management Specialists is one of the 44 occupations; no occupation-level result was extracted.
- **HBS-DELLACQUA-2023:** Opened through the r.jina.ai text mirror. Foundation paper, outside the 18-month window.
- **ILTA-TECHSURVEY-2026:** 508 firms. Month taken from the file name (2606) and the landscape file.
- **KANTATA-RMI-2026:** Vendor-commissioned; 44 organisations surveyed (stated in the press release's last paragraph).
- **KJZZ-OTTER-2025:** Reports allegations in a complaint, not findings.
- **KPMG-GCOUTLOOK-2026:** Month from the URL path. Landing page only; the full report was not opened. In-house.
- **LAWSOC-GENAI-2026:** Opened through the r.jina.ai mirror. The page shows no date but refers to events up to April 2026.
- **LAWYERMONTHLY-SRA-2026:** Secondary report of the SRA's updated supervision guidance. The SRA's own pages returned a bot challenge and were not opened.
- **LEGALBUSINESS-KPMGGC-2026:** Reports the KPMG Global General Counsel Outlook 2026 (468 GCs and senior legal leaders). In-house.
- **LEXISNEXIS-GENAI-2024:** Older baseline (survey Dec 2023 - Jan 2024; 266 respondents).
- **MANDARIN-DELOITTE-2025:** Paywalled; only the standfirst was readable. The refund amount (AUD 97,587) came from a search-result summary.
- **NBER-AUTOR-2026:** Issue date Sept 2026, revised Oct 2026. Study conducted by Google, which also funded the direct costs.
- **NBER-DILLON-2025:** Issue date May 2025, revised Nov 2025. Some authors were Microsoft employees; Microsoft reviewed the paper for privacy only.
- **NIST-AIRMF-2024:** Page says AI RMF 1.0 (26 Jan 2023) is being revised as part of the White House AI Action Plan.
- **OTTER-LITIGATION-2026:** Search summary only; coverage disagrees on how far the motion to dismiss succeeded. Check the docket before relying on it.
- **PMI-AI-2023:** Opened through the r.jina.ai mirror; month from a search result. Older; used for PMI's stated position only.
- **PMIIRELAND-AI-2024:** Blocked (403) when opened; figures come from a search-result summary: 122 project managers, 83% agree governance processes for AI are not in place.
- **SPI-AI-2026:** Product page published 2026-07-14, modified 2026-10-12; the report is listed as published Oct 2026 and sells for USD 1,495. Only the page's headline numbers were read; some figures are locked.
- **STANFORD-DEL-2026:** Paper discloses a general monetary gift from Accenture to the Lab and confidential background talks with three Accenture executives.
- **TR-FOP-2026:** Survey of 1,816 professionals, March-April 2026. The page shows no publication date.
- **TRI-DISCONNECT-2026:** Article summarising the Institute's 2026 AI in Professional Services Report. Sample size not stated in the article.
- **TRI-LEGALWEEK-2026:** Press account of three TR-sponsored Legalweek panels.
- **WORKBANK-STANFORD-2025:** Abstract read. 1,500 workers, 844 tasks, 104 occupations. No project-management occupation result was extracted.

---

## 6. Gaps

- **Quality evidence.** No override rates, error rates, reviewer catch rates, parallel-run results or inspection findings were found for AI in status reporting, risk scoring, forecasting, change control or client reporting. The only independent measures are adjacent (patent drafting, consulting tasks, email time).
- **Named practitioner case studies.** No law, consulting or accounting firm describes a measured use of a PMO or PSA agent. Certinia customer stories ("Read the Full Story" links), Kantata's Expertise Agent and "superagent" posts, Harvey Command Center and Deltek's Dela AI Orchestrator documentation were not opened.
- **Change control.** The only source found on AI and scope management is Certinia's "scope scan" wording; nothing describes AI detecting scope change or drafting change orders.
- **Project-management bodies.** PMI's site returned 403 for its AI pages; PMI Pulse of the Profession and Global Summit material were not obtained. The APM page returned 404. Gartner abstracts and the PMI Ireland survey were seen in search summaries only.
- **UK regulators.** The SRA's own pages and the Bar Standards Board guidance were blocked (bot challenge); the SRA supervision guidance is known through one secondary article. The ABA's own site returned 403 (a LawSites copy was used).
- **Accounting and consulting primary documents.** AICPA and CIMA AI pages returned navigation only; no ICAEW or AICPA guidance on engagement management was read. McKinsey, BCG, Bain and Big Four primary pages were not retried in this run.
- **Paywalled or locked benchmarks.** The SPI 2026 report (USD 1,495), the full Kantata/RMI report, the full Deltek Clarity reports and the TRI 2026 AI in Professional Services Report were not read; TRI-DISCONNECT-2026 does not state its sample size. TR-FOP-2026 shows no publication date.
- **Client AI terms.** No actual outside counsel guidelines or engagement-letter AI clause was read; ACC's sample AI guidelines were named but not opened, and the HSBC panel-firm interview was not opened in depth.
- **In-house and shared-service examples.** Only ACC, KPMG and Thomson Reuters Institute survey coverage was found; no named in-house team's delivery-management practice.
- **Search budget.** 11 searches used; leads not run: AICPA/ICAEW engagement-management guidance, legal project management practitioner articles, Certinia customer story pages.

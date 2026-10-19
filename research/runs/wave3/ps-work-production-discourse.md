# Professional services, work-production: discourse angle

Prepared 2026-10-19. Archetype: professional-services. Module: work-production (first drafts, synthesis, review against playbooks or standards, data extraction). Angle: what practitioners are saying, 2025-2026. Public sources only. Source keys follow `PUBLISHER-SHORT-YYYY`.

## 1. Summary

- **What the field says it is doing.** The substantive layer is where practitioners say AI has moved from pilots to production: ILTA's 2026 survey reports that a majority of GenAI-engaged firms now use GenAI for drafting, legal research, document summarization and contract review (ILTA-TECHSURVEY-2026). ILTACON 2026 voices describe the conversation shifting from what models can do to deployment, validation, training and governance (EDT-CROWD2-2026, EDT-CROWD3-2026).
- **The best measurements are task benchmarks and one randomized trial, not firm data.** Vals' February 2025 benchmark has AI tools above a lawyer baseline on extraction, summarization and Q&A but below it on open-ended redlining (VALS-VLAIR-2025); its October 2025 research benchmark has AI at 74% to 78% against 69% for lawyers (VALS-LEGALRESEARCH-2025); an NBER trial of 133 patent lawyers found higher draft quality with AI but a durable unaided-skill gain only for seniors (NBER-AUTOR-2026). No firm or in-house team was found publishing error, override or parallel-run rates for AI-assisted work product.
- **The live worries are proof, judgment and the pyramid.** Firms say they are still gathering the data on savings while clients ask for matter-level proof (TRI-LEGALWEEK-2026). Thomson Reuters Legal argues the larger risk is not inaccuracy but teams accepting a polished AI structure without testing it (TRI-JUDGMENT-2026). Junior work that doubled as training is being absorbed (VAULT-PYRAMID-2026, TRI-ONBOARD-2026).
- **Where it is heading.** Four AI platform companies entered legal in five months, each with playbook review, drafting and extraction skills inside tools lawyers already use (LAWSITES-MSFT-2026). Vendors describe matter templates with agent tasks and partner review gates (HARVEY-ORCH-2026), while the Law Society reports very limited use of fully autonomous systems so far (LAWSOC-AGENTIC-2026).
- **Output.** 17 candidate use cases: grade A 5, B 4, C 4, D 4. 50 sources read (see section 5). Consulting and accounting work-production evidence is much thinner than legal; most legal evidence is vendor-published or press.

## 2. Use cases

```yaml
- id: professional-services-work-production-01
  title: AI-assisted first drafts of complex legal work product, reviewed by senior lawyers
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - document-production
  - expert-judgment
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Producing a first draft of a complex legal document (for example a patent application) takes skilled lawyer time, and the quality of the first draft depends on who has time to write it.
  solution: Lawyers use an AI drafting assistant to produce a first draft, then revise it themselves. One firm states that a first draft is never an acceptable final submission, and leaves it to each lawyer how to use AI to create first drafts.
  outcomes:
  - lever: quality
    description: Quality of delivered patent-drafting work was higher with AI access at both measurement points, with larger gains among junior lawyers
    figure: +0.34 SD at 10 days; +0.38 SD at 90 days
    measures: Standard-deviation difference in blinded expert-attorney scores on benchmark patent drafting tasks, AI-access group versus control, in a pre-registered three-month randomized trial of 133 practicing patent lawyers at eleven US IP firms
    provenance: independent
    source_ref: NBER-AUTOR-2026
  - lever: quality
    description: Without AI, after three months, treated lawyers redlined an existing application better than controls, but the advantage was concentrated among senior lawyers; juniors showed no average gain
    figure: +0.32 SD overall; +0.45 SD for senior lawyers
    measures: Standard-deviation difference in blinded scores on an unaided redlining task, treated versus control lawyers; senior-lawyer subgroup reported separately
    provenance: independent
    source_ref: NBER-AUTOR-2026
  prerequisites:
  - A drafting assistant configured for the task type (the trial used a custom AI patent drafting assistant)
  - Reviewers able to judge draft quality independently
  - Training that includes verification steps and human review
  risks_and_guardrails:
  - Foundational expertise may be a prerequisite for extracting durable skill from AI-assisted practice (NBER-AUTOR-2026)
  - Teams may accept an AI-structured draft and edit only phrasing, leaving assumptions untested (TRI-JUDGMENT-2026)
  - Supervision and verification duties remain with the lawyer (CALBAR-GENAI-2026)
  human_checkpoints:
  - Lawyer revises and owns the draft; a first draft is never the final submission (TRI-ONBOARD-2026)
  - Senior review of consequential output
  role_evolution: Junior lawyers' drafting practice is partly displaced, and the trial found their unaided skill outcomes split, with some gaining and some doing worse (NBER-AUTOR-2026). Firms respond with champions and mentorship tracks (TRI-ONBOARD-2026).
  evidence_grade: A
  sources:
  - ref: NBER-AUTOR-2026
    title: Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER WP 35720)
    publisher: National Bureau of Economic Research
    type: academic
    url: https://econpapers.repec.org/RePEc:nbr:nberwo:35720
    date: 2026-09
    access: full
    locator: Abstract (whole)
  - ref: TRI-ONBOARD-2026
    title: Law firms need to redesign new attorney onboarding for the AI era
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding
    date: '2026-10-12'
    access: full
    locator: Section 'What a redesigned onboarding program looks like', paragraph on first drafts
  - ref: TRI-JUDGMENT-2026
    title: 'Designing judgment: Preserving AI-mediated legal collaboration'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/designing-judgment-ai-mediated-legal-collaboration
    date: '2026-10-06'
    access: full
    locator: Section 'Delegation versus collaboration'
  last_reviewed: '2026-10-19'
  notes: Grade A rests on one independent randomized trial in one practice (patent drafting) with unnamed firms; it is a September 2026 working paper (not peer reviewed). Task is drafting, so applicable to the module's first-draft step, but generalization to other document types is not shown. The deployment half (Duane Morris) is a firm statement with no measures.
- id: professional-services-work-production-02
  title: Structured extraction, document Q&A and summarization over large document sets
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - data-reporting
  - research-synthesis
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Pulling data points, answers and summaries out of long agreements and document sets is slow manual reading, and quality varies between reviewers.
  solution: An AI tool reads the documents and returns extracted fields, cited answers or summaries for a lawyer to check. Firms describe using it for document analysis and, in one case, loan-agreement review with extraction and comparison across portfolios.
  outcomes:
  - lever: quality
    description: 'Data extraction: two evaluated legal AI tools scored above the lawyer baseline'
    figure: Lawyer baseline 71.1%; CoCounsel 73.2%; Harvey Assistant 75.1%
    measures: Percentage score against Vals' predefined evaluation criteria for the Data Extraction task, vendor tools versus a lawyer control group, tools evaluated in isolation
    provenance: independent
    source_ref: VALS-VLAIR-2025
  - lever: quality
    description: 'Document summarization: all evaluated AI tools scored above the lawyer baseline'
    figure: Lawyer baseline 50.3%; CoCounsel 77.2%; Harvey Assistant 72.1%; Vincent AI 58.9%; Oliver 62.4%
    measures: Percentage score against Vals' predefined criteria for the Document Summarization task
    provenance: independent
    source_ref: VALS-VLAIR-2025
  - lever: quality
    description: 'Document Q&A: highest-scoring task overall'
    figure: Lawyer baseline 70.1%; Harvey Assistant 94.8%; CoCounsel 89.6%
    measures: Percentage score against Vals' predefined criteria for the Document Q&A task
    provenance: independent
    source_ref: VALS-VLAIR-2025
  - lever: speed
    description: A&O Shearman partner statement that the agents do in minutes what previously took several hours; no tracked metric published
    figure: none published (qualitative statement)
    measures: Statement by the firm's Global Head of AI Advisory about its Harvey-built agents; not a measured figure
    provenance: self-reported
    source_ref: AOSHEARMAN-HARVEY-2025
  prerequisites:
  - Documents in a form the tool can read
  - A lawyer baseline or test set to check accuracy before rollout
  - Vendor or in-house governance for confidential data (HARVEY-OGIER-2026 describes deployment within an existing governance framework)
  risks_and_guardrails:
  - Vals evaluated tools task by task in isolation and notes that customer value needs further consideration (VALS-VLAIR-2025)
  - Vendors chose which tasks to enter; LexisNexis withdrew from all but legal research (VALS-VLAIR-2025)
  - 'Extraction accuracy is not perfect: the best tool scored 75.1% on extraction under Vals'' criteria'
  human_checkpoints:
  - Lawyer checks extracted fields and cited answers against the source
  - Spot-check or full review of high-risk fields
  role_evolution: Document review and analysis time moves to checking AI output. A survey respondent expects GenAI to compress document review, research and drafting work that has powered the associate pyramid (ILTA-TECHSURVEY-2026).
  evidence_grade: A
  sources:
  - ref: VALS-VLAIR-2025
    title: Vals Legal AI Report (VLAIR), February 2025
    publisher: Vals AI
    type: academic
    url: https://www.vals.ai/vlair
    date: '2025-02-27'
    access: full
    locator: Results table and 'Document Extraction', 'Document Summarization' and 'Document Q&A' sections; study dated 2025-02-27
  - ref: AOSHEARMAN-HARVEY-2025
    title: A&O Shearman and Harvey to roll out agentic AI agents targeting complex legal workflows
    publisher: A&O Shearman
    type: firm
    url: https://www.aoshearman.com/en/news/ao-shearman-and-harvey-to-roll-out-agentic-ai-agents-targeting-complex-legal-workflows
    date: 2025-04
    access: full
    locator: Quote from Filippo Crosara on the loan review agent; quote from David Wakeling
  - ref: HARVEY-OGIER-2026
    title: Ogier adopts Harvey firmwide
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/ogier-adopts-harvey-firmwide
    date: '2026-10-12'
    access: full
    locator: Paragraph beginning 'By integrating Harvey'
  - ref: ILTA-TECHSURVEY-2026
    title: '2026 ILTA Technology Survey: Executive Summary'
    publisher: International Legal Technology Association (ILTA)
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: Page 'The Curtain Rises' respondent quote
  last_reviewed: '2026-10-19'
  notes: Vals scores are benchmark results on a test set, not deployment results. The Vals report is dated Feb 2025, older than the 12-18 month window, kept as the anchor independent measurement. Vals discloses that it has a customer relationship with one or more participants. The A&O Shearman announcement is April 2025 and describes a planned rollout.
- id: professional-services-work-production-03
  title: Playbook-based contract review and redlining in the lawyer's working tool
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
  maturity: in-production
  problem: Reviewing incoming contracts against a team's preferred and fallback positions is repetitive, and consistency depends on who reviews.
  solution: 'The tool applies a stored playbook to a draft agreement, flags deviations and proposes tracked-change edits. Microsoft describes reviewing agreements against playbooks inside Word; Anthropic describes plugins that begin with a setup interview capturing a team''s playbooks, escalation chains and house style. In-house: GE Aerospace deployed Harvey across Legal and Compliance after a pilot and is a design partner for its Contract Intelligence product.'
  outcomes:
  - lever: quality
    description: Open-ended redlining was one of two tasks where the lawyer baseline outscored the evaluated AI tools (tested without a stored playbook)
    figure: Lawyer baseline 79.7%; Vincent AI 53.6%; Harvey Assistant 59.4% in the text (65.0% in the results table)
    measures: Percentage score against Vals' predefined criteria for the Redlining task, open-ended questions; Vals notes Harvey was evaluated through its Assistant, not its Redlining feature
    provenance: independent
    source_ref: VALS-VLAIR-2025
  - lever: capacity
    description: GE Aerospace's General Counsel says Harvey is helping increase capacity, improve consistency and free time for strategic work; no figure published
    figure: none published
    measures: Executive quotation in a vendor announcement; no tracked metric
    provenance: vendor-published
    source_ref: HARVEY-GE-2026
  prerequisites:
  - A documented playbook with preferred and fallback positions
  - Tool that writes native tracked changes in the drafting environment
  - A test set to compare AI redlines with the team's own
  risks_and_guardrails:
  - Vals found lawyers ahead on open-ended redlining in its February 2025 test (VALS-VLAIR-2025)
  - Vendor skills for Word are announced; independent measurement of playbook-driven review was not found
  - Lawyers remain responsible for reviewing and approving outputs (CALBAR-GENAI-2026)
  human_checkpoints:
  - Lawyer accepts or rejects each proposed edit
  - Escalation of terms outside playbook authority
  role_evolution: A General Counsel panelist says AI levels technical acumen, that fewer distinctions will remain between firms on contract markup, and that judgment and service become the differentiators (TRI-AIFORUM-2026).
  evidence_grade: B
  sources:
  - ref: HARVEY-GE-2026
    title: GE Aerospace deploys Harvey across its Legal & Compliance organization
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/ge-aerospace-deploys-harvey-across-its-legal-and-compliance-organization
    date: '2026-09-01'
    access: full
    locator: Paragraphs on pilot, Contract Intelligence design partner and Jake Phillips quote
  - ref: LAWSITES-MSFT-2026
    title: Microsoft Launches Copilot for Legal, Becoming the Fourth AI Giant in Five Months to Build Out a Legal Vertical
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/microsoft-launches-copilot-for-legal-becoming-the-fourth-ai-giant-in-five-months-to-build-out-a-legal-vertical.html
    date: '2026-10-15'
    access: full
    locator: Paragraph listing 'Review and negotiate with confidence'; redlining paragraph
  - ref: LAWSITES-ANTHROPIC-2026
    title: Anthropic Goes All-In on Legal, Releasing More Than 20 Connectors and 12 Practice-Area Plugins for Claude
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/05/anthropic-goes-all-in-on-legal-releasing-more-than-20-connectors-and-12-practice-area-plugins-for-claude.html
    date: '2026-05-12'
    access: full
    locator: Paragraph beginning 'Notably, each plugin starts with'
  - ref: VALS-VLAIR-2025
    title: Vals Legal AI Report (VLAIR), February 2025
    publisher: Vals AI
    type: academic
    url: https://www.vals.ai/vlair
    date: '2025-02-27'
    access: full
    locator: '''Redlining'' section; results table'
  - ref: TRI-AIFORUM-2026
    title: 'The 2026 Future of AI & Technology Forum: What AI can''t replace in the client-law firm relationship'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/what-ai-cant-replace
    date: '2026-09-28'
    access: full
    locator: Panel with Seth Gastwirth, section 'The ask has changed'
  last_reviewed: '2026-10-19'
  notes: 'In-house example (GE Aerospace; JLL panelist). Grade B: named deployment without measurements; the Vals redlining test did not use stored playbooks, so it does not measure this use case directly. Microsoft and Anthropic items are product announcements.'
- id: professional-services-work-production-04
  title: Matter templates that assign agent tasks, with partner review gates
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - document-production
  - coordination-scheduling
  pattern: draft-review-loop
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Each new matter rebuilds its process from a checklist, a prior deal or someone's memory, and a lawyer assembles inputs and instructions for every step handed to an AI.
  solution: Harvey's Legal Work Orchestration lets a team define phases, tasks, playbooks, agents and review gates in a reusable template. An agent assigned a change-of-control review analyzes the contracts and produces a consent matrix, then the designated partner is notified and approves before the next step.
  outcomes:
  - lever: capacity
    description: Harvey states it expects agents to take on a further 20% of workflow steps in six months and for that share to triple within a year; no measurement published
    figure: none published (vendor expectation)
    measures: Vendor statement of expected share of workflow steps executed by agents; not a measured figure
    provenance: vendor-published
    source_ref: HARVEY-ORCH-2026
  prerequisites:
  - Matter types that recur
  - Innovation or knowledge team to define templates
  - Documents and playbooks in the platform
  risks_and_guardrails:
  - Vendor states work by agents will remain transparent and auditable and lawyers stay in control through review gates (HARVEY-ORCH-2026)
  - California guidance says supervision must scale with system autonomy (CALBAR-GENAI-2026)
  human_checkpoints:
  - Designated reviewer approves each agent task at its gate
  role_evolution: Partners see status without associates reconstructing it from email; lawyers direct the matter and review consequential outputs, per the vendor (HARVEY-ORCH-2026).
  evidence_grade: C
  sources:
  - ref: HARVEY-ORCH-2026
    title: Making Harvey the Orchestration Layer for Legal Work
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/legal-work-orchestration
    date: '2026-10-15'
    access: full
    locator: Paragraphs on templates, consent matrix and the 20% / triple expectation
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: Executive summary, 'Agentic AI' section
  last_reviewed: '2026-10-19'
  notes: Product launch of 2026-10-15; rolling out, with template early access. No customer use found. Overlaps the delivery-management module; included here for the agent-drafts, partner-reviews step.
- id: professional-services-work-production-05
  title: Firm expertise packaged as multi-step agents for complex work products, internally and for sale
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - document-production
  - review-assurance
  - expert-judgment
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: High-value matter types (filing analysis, fund formation, loan review) need multi-step reasoning over matter documents, and the know-how sits with senior lawyers.
  solution: A&O Shearman and Harvey announced agents for antitrust filing analysis, cybersecurity, fund formation and loan review that break issues into plans and combine intermediate outputs into work products with oversight. They are to be used internally and sold to corporates, law firms and financial institutions by subscription or usage fees, with the firm sharing in software revenue.
  outcomes:
  - lever: speed
    description: Firm head of AI advisory says the agents do in minutes what previously took several hours; no tracked metric published
    figure: none published (qualitative statement)
    measures: Statement by A&O Shearman's Global Head of AI Advisory and the Markets Innovation Group
    provenance: self-reported
    source_ref: AOSHEARMAN-HARVEY-2025
  prerequisites:
  - Practice experts to encode their method
  - Platform able to run multi-step agents
  - Commercial model for external sale
  risks_and_guardrails:
  - Law Society found very limited use of fully autonomous agentic systems among firms and suppliers it spoke to (LAWSOC-AGENTIC-2026)
  - Human checkpoints should be proportionate to higher-risk actions (LAWSOC-AGENTIC-2026)
  human_checkpoints:
  - Lawyers review outputs; the announcement refers to transparency and oversight
  role_evolution: Senior lawyers' expertise becomes a product; a Stanford professor quoted by Vault describes firms racing to extract their lawyers' knowledge and embed it in AI workflows (VAULT-PYRAMID-2026).
  evidence_grade: C
  sources:
  - ref: AOSHEARMAN-HARVEY-2025
    title: A&O Shearman and Harvey to roll out agentic AI agents targeting complex legal workflows
    publisher: A&O Shearman
    type: firm
    url: https://www.aoshearman.com/en/news/ao-shearman-and-harvey-to-roll-out-agentic-ai-agents-targeting-complex-legal-workflows
    date: 2025-04
    access: full
    locator: 'Page body: first three paragraphs and quote by David Wakeling'
  - ref: LAWSOC-AGENTIC-2026
    title: What is agentic AI - and what does it mean for legal practice
    publisher: Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/what-is-agentic-ai-and-what-does-it-mean-for-legal-practice
    date: '2026-10-19'
    access: full
    locator: Interview with Tara Chittenden, section on members' questions
  - ref: VAULT-PYRAMID-2026
    title: 'The Compressed Pyramid: What AI Means for the Associate Career Ladder'
    publisher: Vault
    type: press
    url: https://legacy.vault.com/blogs/vaults-law-blog-legal-careers-and-industry-news/the-compressed-pyramid-what-ai-means-for-the-associate-career-ladder
    date: '2026-08-11'
    access: full
    locator: Paragraph quoting David Freeman Engstrom
  last_reviewed: '2026-10-19'
  notes: Announcement dated April 2025 describing a planned rollout; no deployment evidence or client uptake found in this run.
- id: professional-services-work-production-06
  title: In-house legal teams use AI for a first pass on routine drafting and dispute responses
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - document-production
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: In-house lawyers used to send drafts such as dispute responses and demand letters to outside counsel to save their own hours.
  solution: Lawyers upload the business background documents to an AI tool and get a draft in minutes, then edit. TC Energy introduced a 'Harvey-First' directive during its pilot encouraging lawyers to use the tool as a first pass; GE Aerospace deployed Harvey across its legal and compliance organization; a JLL panelist described getting a solid draft in five to ten minutes. In-house.
  outcomes:
  - lever: speed
    description: JLL Work Dynamics General Counsel recalls a very solid draft within five to ten minutes of uploading background documents, which may remove the need for outside counsel on some dispute work
    figure: 5 to 10 minutes (anecdotal)
    measures: Panelist's recollection of time for an internal AI tool to produce a draft from uploaded documents; not a tracked metric
    provenance: self-reported
    source_ref: TRI-AIFORUM-2026
  - lever: capacity
    description: TC Energy General Counsel describes more capacity for complex matters; no figure published
    figure: none published
    measures: Executive quotation in a vendor announcement
    provenance: vendor-published
    source_ref: HARVEY-TCENERGY-2026
  prerequisites:
  - Enterprise AI tool approved by legal and security
  - Clear directive on first-pass use
  - Review expectations before anything leaves the team
  risks_and_guardrails:
  - Client-side expectation is faster turnaround and transparency about AI's effect on cost, not necessarily lower fees (TRI-AIFORUM-2026)
  - Lawyers remain responsible for work whether or not AI is used (LAWSOC-AGENTIC-2026)
  human_checkpoints:
  - In-house lawyer edits and approves the draft
  role_evolution: In-house counsel handle more drafting themselves and value outside counsel for judgment and anticipating risk (TRI-AIFORUM-2026).
  evidence_grade: B
  sources:
  - ref: HARVEY-TCENERGY-2026
    title: TC Energy deploys Harvey across its legal team
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/tc-energy-deploys-harvey-across-its-legal-team
    date: '2026-10-05'
    access: full
    locator: Paragraph on the 'Harvey-First' directive; quote by Anita Dusevic Oliva
  - ref: HARVEY-GE-2026
    title: GE Aerospace deploys Harvey across its Legal & Compliance organization
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/ge-aerospace-deploys-harvey-across-its-legal-and-compliance-organization
    date: '2026-09-01'
    access: full
    locator: Paragraphs on pilot and Jake Phillips quote
  - ref: TRI-AIFORUM-2026
    title: 'The 2026 Future of AI & Technology Forum: What AI can''t replace in the client-law firm relationship'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/what-ai-cant-replace
    date: '2026-09-28'
    access: full
    locator: Section 'The ask has changed', Seth Gastwirth quotation and key insights
  last_reviewed: '2026-10-19'
  notes: In-house. Named deployments (TC Energy, GE Aerospace) are vendor announcements without measures; the JLL time is a recollection, not a metric, so grade B under the 2026-10-17 rule.
- id: professional-services-work-production-07
  title: Lawyer-built custom agents and shared playbooks that encode firm know-how
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - document-production
  - review-assurance
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Each lawyer prompts AI from scratch, so results vary and know-how stays with individuals.
  solution: Practice groups and knowledge teams build reusable agents and playbooks. Hogan Lovells Cadwalader lawyers developed custom agents for Knowledge Management, Capital Markets and International Arbitration and built playbooks collaboratively in Harvey, and the firm also piloted Legora with more than 1,300 lawyers across 18 practice teams. Duane Morris names practice-group AI champions who test tools on real work and help others.
  outcomes:
  - lever: capacity
    description: Hogan Lovells Cadwalader piloted Legora with over 1,300 lawyers in 18 practice teams before a global rollout; no outcome figures published
    figure: 1,300+ lawyers; 18 practice teams
    measures: Number of lawyers and practice teams in the pilot, per the vendor announcement
    provenance: vendor-published
    source_ref: LEGORA-HLC-2026
  prerequisites:
  - Designated champions with early tool access
  - Knowledge-management capability to capture and maintain playbooks
  - Office hours, workshops and individual sessions with senior lawyers
  risks_and_guardrails:
  - Mid-level associates build their own agents with or without firm training, so firms should shape use early (TRI-ONBOARD-2026)
  - Separately procured agents may start to join up without a conscious decision to adopt agentic systems (LAWSOC-AGENTIC-2026)
  human_checkpoints:
  - Champions test tools on real matters before wider release
  role_evolution: Mid-level associates and senior associates become tool builders and champions; the CEO frames the aim as capturing expertise across the firm (HARVEY-HLC-2026, TRI-ONBOARD-2026).
  evidence_grade: B
  sources:
  - ref: HARVEY-HLC-2026
    title: Hogan Lovells Cadwalader adopts Harvey
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/hogan-lovells-cadwalader-adopts-harvey
    date: '2026-10-16'
    access: full
    locator: Paragraphs on practice-group office hours, custom agents and Zaldivar quote
  - ref: LEGORA-HLC-2026
    title: Hogan Lovells Cadwalader rolls out Legora globally
    publisher: Legora
    type: vendor
    url: https://legora.com/newsroom/hogan-lovells-cadwalader-rolls-out-legora-globally
    date: '2026-10-16'
    access: full
    locator: First paragraph (pilot numbers)
  - ref: TRI-ONBOARD-2026
    title: Law firms need to redesign new attorney onboarding for the AI era
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding
    date: '2026-10-12'
    access: full
    locator: Section 'What a redesigned onboarding program looks like'; section 'Associates are already forming AI habits'
  - ref: LAWSOC-AGENTIC-2026
    title: What is agentic AI - and what does it mean for legal practice
    publisher: Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/what-is-agentic-ai-and-what-does-it-mean-for-legal-practice
    date: '2026-10-19'
    access: full
    locator: Interview with Tara Chittenden
  last_reviewed: '2026-10-19'
  notes: Hogan Lovells Cadwalader announcements appear on both Harvey's and Legora's sites on 2026-10-16; both are vendor-published and the relationship between the two tools at the firm is not explained in the sources read.
- id: professional-services-work-production-08
  title: AI-assisted analysis, synthesis and first-draft deliverables in consulting
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - research-synthesis
  - document-production
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: Consultants spend a large share of early-career time on research, data work and first-draft slides.
  solution: Consultants use GenAI to produce market-research briefs, initial content for decks, documents and emails, and early structure for analysis, which they then validate and refine.
  outcomes:
  - lever: speed
    description: In a preregistered experiment with BCG, knowledge workers using GPT-4 completed more tasks, faster, on tasks inside the AI frontier
    figure: 12.2% more tasks; 25.1% more quickly
    measures: Average difference in tasks completed and completion time, AI-access versus no-AI group, across 18 realistic consulting tasks and 758 BCG consultants
    provenance: independent
    source_ref: HBS-DELLACQUA-2023
  - lever: quality
    description: For a task selected to be outside the frontier, AI users were less likely to produce correct solutions
    figure: 19% less likely to produce correct solutions
    measures: Relative likelihood of a correct solution on one complex managerial task, AI users versus no-AI group
    provenance: independent
    source_ref: HBS-DELLACQUA-2023
  - lever: capacity
    description: Content creation was the most common GenAI use among surveyed consultants
    figure: 50% of consultants
    measures: Share of consultants naming content creation as a top GenAI use in the LexisNexis Future of Work 2026 Management Consulting report (denominator not stated in the blog summary)
    provenance: vendor-published
    source_ref: LEXISNEXIS-FOW-2026
  prerequisites:
  - Approved AI tools (54% of surveyed consultants report using tools without approval, per LEXISNEXIS-FOW-2026)
  - Validation step before client delivery
  - Understanding of where the jagged frontier lies
  risks_and_guardrails:
  - Outputs must be validated before reaching clients (LEXISNEXIS-FOW-2026)
  - Deloitte Australia refunded part of a government contract after a report with apparent AI-generated errors (CTV-DELOITTE-2025)
  - AI worsens performance on tasks outside its frontier (HBS-DELLACQUA-2023)
  human_checkpoints:
  - Consultant validates AI output; manager reviews before client release
  role_evolution: A former McKinsey consultant argues that AI now does much of the research, data work and slide drafting that filled a junior's first year, and that validating AI output is now a big part of the junior job (STRATEGYCASE-JUNIOR-2026).
  evidence_grade: A
  sources:
  - ref: HBS-DELLACQUA-2023
    title: Navigating the Jagged Technological Frontier (HBS Working Paper 24-013)
    publisher: Harvard Business School
    type: academic
    url: https://www.hbs.edu/faculty/Pages/item.aspx?num=64700
    date: '2023'
    access: full
    locator: Abstract
  - ref: LEXISNEXIS-FOW-2026
    title: 'Generative AI in professional services (blog on the LexisNexis Future of Work 2026: Management Consulting Industry Report)'
    publisher: LexisNexis
    type: vendor
    url: https://www.lexisnexis.com/blogs/amppage/30/generative-ai-professional-services
    date: '2026-04-16'
    access: full
    locator: Sections on research briefs and polished deliverables
  - ref: STRATEGYCASE-JUNIOR-2026
    title: Will AI Replace Junior Consultants? What's Actually Changing
    publisher: StrategyCase (former McKinsey consultant's coaching site)
    type: community
    url: https://strategycase.com/artificial-intelligence-and-the-junior-consultant-how-entry-training-and-work-are-changing
    date: '2026-02-05'
    access: full
    locator: Opening summary list; section on what changed
  - ref: CTV-DELOITTE-2025
    title: Deloitte to partially refund Australian government for report with apparent AI-generated errors
    publisher: CTV News (Associated Press)
    type: press
    url: https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/
    date: '2025-10-07'
    access: full
    locator: Paragraphs 1-6
  last_reviewed: '2026-10-19'
  notes: The experiment is from 2023 with GPT-4 (outside the 18-month window; kept as the foundational measurement). No firm-published consulting deliverable-quality data found. McKinsey and other firm figures appear only in secondary sources and are not used as outcomes. Grade A reflects the experiment, not a measured production deployment.
- id: professional-services-work-production-09
  title: Mandatory human-review gate and verification rules for AI-assisted work product
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: AI output looks complete and fluent, so reviewers may accept it without testing it, and responsibility can diffuse across a team.
  solution: Firms write policies that require a human to review AI-assisted work product and independent verification of citations, restrict use to approved tools and require training before access.
  outcomes:
  - lever: risk
    description: Share of firms whose GenAI policy requires human review of work product rises with firm size
    figure: 31% (under 50 lawyers) to 83% (350 to 699 lawyers); 79% over 700
    measures: Share of respondent firms selecting 'Work product must be reviewed by a human' as describing official GenAI policy, by firm size, ILTA Technology Survey 2026 (508 firms)
    provenance: independent
    source_ref: ILTA-TECHSURVEY-2026
  - lever: risk
    description: Share of firms requiring training before access to GenAI tools
    figure: 11% (under 50 lawyers) to 72% (over 700 lawyers)
    measures: Share of respondent firms selecting 'Specific training required before use', by firm size
    provenance: independent
    source_ref: ILTA-TECHSURVEY-2026
  - lever: risk
    description: Professionals using unsanctioned AI tools
    figure: 34%
    measures: Share of Future of Professionals 2026 respondents (1,816 professionals) who say they use AI tools their organization has not sanctioned
    provenance: independent
    source_ref: TR-FOP-2026
  prerequisites:
  - Formal GenAI policy
  - Approved tools
  - Training that covers verification and override, not only tool features
  risks_and_guardrails:
  - Competence requires more than detecting fabricated results; the lawyer keeps control of strategic decisions (CALBAR-GENAI-2026)
  - Nearly half of professionals (47%) say final responsibility for AI-assisted errors lies with the individual (TR-FOP-2026)
  - Edits tend to cluster around phrasing and tone rather than assumptions (TRI-JUDGMENT-2026)
  human_checkpoints:
  - Human review of AI-assisted work product
  - Independent verification of citations
  - Periodic re-check of tools as models change (CALBAR-GENAI-2026)
  role_evolution: Reviewer skill (knowing when to trust, verify or override) becomes a trained capability (TRI-STANDARDS-2026).
  evidence_grade: B
  sources:
  - ref: ILTA-TECHSURVEY-2026
    title: '2026 ILTA Technology Survey: Executive Summary'
    publisher: International Legal Technology Association (ILTA)
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: Table 'Q3.18 Which of the following best describe your firm's current official policies or guidance on the use of generative AI tools'
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: 'Key findings: 34% unsanctioned use; 47% final responsibility'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: Duties of Competence and Diligence, Rules 1.1 and 1.3
  - ref: TRI-JUDGMENT-2026
    title: 'Designing judgment: Preserving AI-mediated legal collaboration'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/designing-judgment-ai-mediated-legal-collaboration
    date: '2026-10-06'
    access: full
    locator: Section 'Delegation versus collaboration'
  - ref: TRI-STANDARDS-2026
    title: 'Between accountability and chaos: Setting the AI standards that professionals demand'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/between-accountability-and-chaos
    date: '2026-10-12'
    access: full
    locator: Section 'What standards should actually look like'
  last_reviewed: '2026-10-19'
  notes: The figures show prevalence of the control, not its effect on error rates; no published measure of review effectiveness or override rates was found, so grade B.
- id: professional-services-work-production-10
  title: Automated reference and citation checking of AI-assisted drafts before release
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - review-assurance
  pattern: full-population-testing
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Fabricated citations and references in AI-assisted documents reach clients and courts; manual checking of every reference is slow.
  solution: A reference checker tests every citation or reference in a draft against sources before the document is released. One database maintainer built an automated reference checker, PelAIkan, on his database of court decisions involving hallucinated content.
  outcomes:
  - lever: risk
    description: Courts and tribunals have addressed AI-hallucinated material in a large and growing set of decisions; the checker's own performance is not published
    figure: 2,202 cases identified (as accessed 2026-10-19)
    measures: Count of decisions in the Charlotin database where a court or tribunal found or implied reliance on hallucinated content (live database, a work in progress; not the full universe of fake citations)
    provenance: independent
    source_ref: CHARLOTIN-HALLUC-2026
  - lever: risk
    description: Preregistered evaluation found two legal research providers' tools each hallucinated between 17% and 33% of the time
    figure: 17% to 33%
    measures: Share of responses hallucinating in the Stanford evaluation of Lexis+ AI and Westlaw AI-Assisted Research / Ask Practical Law AI (2024)
    provenance: independent
    source_ref: STANFORD-MAGESH-2024
  - lever: risk
    description: Deloitte Australia partly refunded a government report with apparent AI-generated errors
    figure: AU$440,000 contract; 237-page report; researcher reported up to 20 errors
    measures: Contract value, report length and number of errors claimed by the researcher who raised the issue, per the AP report
    provenance: independent
    source_ref: CTV-DELOITTE-2025
  prerequisites:
  - Machine-readable references
  - Access to authoritative sources to test against
  - A release gate that requires the check
  risks_and_guardrails:
  - No independent measurement of automated reference checkers was found
  - Competence requires more than detecting fabrications (CALBAR-GENAI-2026)
  - A second Deloitte report for a Newfoundland department drew similar concerns, per ICAEW (ICAEW-AI2026-2026)
  human_checkpoints:
  - Author resolves every flagged reference
  - Partner or manager confirms the check was run before release
  role_evolution: California guidance keeps responsibility for reviewing and verifying AI outputs, including those filed with a tribunal, with the lawyer (CALBAR-GENAI-2026).
  evidence_grade: C
  sources:
  - ref: CHARLOTIN-HALLUC-2026
    title: AI Hallucination Cases Database (live; accessed 2026-10-19)
    publisher: Damien Charlotin
    type: academic
    url: https://www.damiencharlotin.com/hallucinations/
    date: '2026-10-19'
    access: full
    locator: Header text of database page (case count; PelAIkan mention)
  - ref: STANFORD-MAGESH-2024
    title: Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools
    publisher: Stanford RegLab and HAI (arXiv 2405.20362)
    type: academic
    url: https://arxiv.org/abs/2405.20362
    date: '2024-05-30'
    access: full
    locator: Abstract
  - ref: CTV-DELOITTE-2025
    title: Deloitte to partially refund Australian government for report with apparent AI-generated errors
    publisher: CTV News (Associated Press)
    type: press
    url: https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/
    date: '2025-10-07'
    access: full
    locator: Paragraphs 1-9
  - ref: ICAEW-AI2026-2026
    title: Will 2026 be AI's year? AI adoption trends
    publisher: ICAEW
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2026/jan-2026/will-2026-be-ais-year-ai-adoption-trends
    date: 2026-01
    access: full
    locator: Paragraph on the Newfoundland report
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: Rules 1.1 and 1.3 and Rule 3.1 sections
  last_reviewed: '2026-10-19'
  notes: 'Grade C: the only tool-specific source is the maintainer''s own mention of a demo. The case counts and incident data are context. The database count is live and changes.'
- id: professional-services-work-production-11
  title: Research answers grounded in cited sources, benchmarked against lawyers
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Legal research questions need accurate answers with authoritative citations, and buyers cannot tell which tools to trust.
  solution: Legal AI and general AI products answer research questions with citations; independent benchmarking compares them with a lawyer baseline.
  outcomes:
  - lever: quality
    description: All four AI products scored above the lawyer baseline on average weighted score
    figure: AI products 74% to 78%; lawyer baseline 69%
    measures: Average weighted score (accuracy 50%, authoritativeness 40%, appropriateness 10%) across 200 US legal research questions, Alexi, Counsel Stack, Midpage and ChatGPT versus a lawyer baseline
    provenance: independent
    source_ref: VALS-LEGALRESEARCH-2025
  - lever: quality
    description: AI average weighted scores exceeded the lawyer baseline on most questions
    figure: 150 of 200 questions (75%)
    measures: Questions on which the AI products' average weighted score exceeded the lawyer baseline, per the Vals report
    provenance: independent
    source_ref: VALS-LEGALRESEARCH-2025
  prerequisites:
  - Access to authoritative legal sources
  - Specialist workflows for multi-jurisdiction questions
  - Lawyer review of citations
  risks_and_guardrails:
  - Thomson Reuters and LexisNexis did not opt in and vLex withdrew, so the largest research platforms were not measured (LAWSITES-VALS-2025)
  - Participants struggled with jurisdictional complexity and 50-state surveys (VALS-LEGALRESEARCH-2025)
  - An earlier Stanford study found leading research tools hallucinated 17% to 33% of the time (STANFORD-MAGESH-2024)
  human_checkpoints:
  - Lawyer verifies citations and reasoning before reliance
  role_evolution: Research moves from searching to evaluating AI answers; lawyers still outperformed on about one-third of question categories needing deeper interpretive analysis, per the coverage (LAWSITES-VALS-2025).
  evidence_grade: A
  sources:
  - ref: VALS-LEGALRESEARCH-2025
    title: VLAIR - Legal Research
    publisher: Vals AI
    type: academic
    url: https://vals.ai/industry-reports/vlair-10-14-25
    date: '2025-10-14'
    access: full
    locator: Key results and conclusions 1-3; question-level analysis
  - ref: LAWSITES-VALS-2025
    title: Vals AI's Latest Benchmark Finds Legal and General AI Now Outperform Lawyers in Legal Research Accuracy
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2025/10/vals-ais-latest-benchmark-finds-legal-and-general-ai-now-outperform-lawyers-in-legal-research-accuracy.html
    date: '2025-10-23'
    access: full
    locator: Paragraphs on non-participating vendors; closing paragraph on categories
  - ref: STANFORD-MAGESH-2024
    title: Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools
    publisher: Stanford RegLab and HAI (arXiv 2405.20362)
    type: academic
    url: https://arxiv.org/abs/2405.20362
    date: '2024-05-30'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-19'
  notes: Legal research is adjacent to the module's synthesis step (the module's first-draft and extraction steps are covered in use cases 1 and 2). Vals is an industry benchmark, not peer reviewed.
- id: professional-services-work-production-12
  title: Chronology and transcript synthesis for case teams
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - research-synthesis
  - data-reporting
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Building chronologies and analysing transcripts means reading large record sets by hand.
  solution: AI tools generate chronologies and analyse transcripts for lawyers to check; DISCO also launched an agentic fact-investigation application that generates memos, deposition outlines and timelines.
  outcomes:
  - lever: quality
    description: 'Transcript analysis: all evaluated tools that entered scored above the lawyer baseline'
    figure: Lawyer baseline 53.7%; Vincent AI 64.8%; Harvey Assistant 77.8%
    measures: Percentage score against Vals' predefined criteria for the Transcript Analysis task
    provenance: independent
    source_ref: VALS-VLAIR-2025
  - lever: quality
    description: 'Chronology generation: best tool matched the lawyer baseline'
    figure: Lawyer baseline 80.2%; Harvey Assistant 80.2%; CoCounsel 78%
    measures: Percentage score against Vals' predefined criteria for the Chronology Generation task
    provenance: independent
    source_ref: VALS-VLAIR-2025
  prerequisites:
  - Record sets in the tool
  - Lawyer review of key events and sources
  risks_and_guardrails:
  - Task-level benchmark only; Vals notes value to customers needs further consideration (VALS-VLAIR-2025)
  - Validation principles from technology-assisted review give a quantitative framework, with qualitative validation added for generative uses (EDT-CROWD2-2026)
  human_checkpoints:
  - Lawyer checks key dates and source references
  role_evolution: Litigation teams are shifting focus to adoption, training and validating results (EDT-CROWD3-2026).
  evidence_grade: A
  sources:
  - ref: VALS-VLAIR-2025
    title: Vals Legal AI Report (VLAIR), February 2025
    publisher: Vals AI
    type: academic
    url: https://www.vals.ai/vlair
    date: '2025-02-27'
    access: full
    locator: Results table rows 'Transcript Analysis' and 'Chronology Generation'
  - ref: LAWSITES-ILTACONROUND-2026
    title: 'ILTACON News Round-Up Part 1, E-Discovery: DISCO, Everlaw, Nuix, Relativity, Reveal'
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/09/iltacon-news-round-up-part-1-e-discovery-disco-everlaw-nuix-relativity-reveal.html
    date: '2026-09-03'
    access: full
    locator: DISCO paragraphs on Advanced Research
  - ref: EDT-CROWD2-2026
    title: Part Two of ILTACON 2026 Crowdsourced Observations
    publisher: eDiscovery Today
    type: community
    url: https://ediscoverytoday.com/2026/09/02/part-two-of-iltacon-2026-crowdsourced-observations-legal-technology-trends/
    date: '2026-09-02'
    access: full
    locator: Observation by Tiana Van Dyk, Epiq
  - ref: EDT-CROWD3-2026
    title: Part Three of ILTACON 2026 Crowdsourced Observations
    publisher: eDiscovery Today
    type: community
    url: https://ediscoverytoday.com/2026/09/03/part-three-of-iltacon-2026-crowdsourced-observations-legal-technology-trends/
    date: '2026-09-03'
    access: full
    locator: Observation on adoption, training and validating
  last_reviewed: '2026-10-19'
  notes: Litigation-leaning; practice-specific detail belongs to a legal extension. The DISCO product is a vendor announcement (2026-09) with no measures.
- id: professional-services-work-production-13
  title: Agent-run end-to-end work product with proportionate human checkpoints
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - document-production
  - research-synthesis
  - review-assurance
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: Efficiency from agents comes from not having a person review every step, but professional duties require responsibility and supervision.
  solution: The Law Society's example is a solicitor giving an agent a goal such as a settlement proposal; the agent reads the file, extracts facts, identifies issues, compares similar matters and drafts an advice note. California guidance lists pleading revisions across iterations, discovery responses and coordinating document review as agentic examples.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: No measurement found; the Law Society reports very limited use of fully autonomous systems among those it spoke to
    provenance: independent
    source_ref: LAWSOC-AGENTIC-2026
  prerequisites:
  - Permissions framework for tiers of agents
  - Checkpoints around higher-risk actions
  - Clarity on what is an agent versus agentic AI
  risks_and_guardrails:
  - Lawyers must not let agentic systems make substantive legal determinations, communicate advice or file pleadings without meaningful supervision (CALBAR-GENAI-2026)
  - Agents may access things they should not (LAWSOC-AGENTIC-2026)
  human_checkpoints:
  - Checkpoints designed around higher-risk actions rather than every step
  role_evolution: Review shifts from every output to designing checkpoints and permissions (LAWSOC-AGENTIC-2026).
  evidence_grade: D
  sources:
  - ref: LAWSOC-AGENTIC-2026
    title: What is agentic AI - and what does it mean for legal practice
    publisher: Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/what-is-agentic-ai-and-what-does-it-mean-for-legal-practice
    date: '2026-10-19'
    access: full
    locator: Sections 'How might agentic AI be used in legal services?' and 'Lawyer-in-the-loop?'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: Executive summary, 'Agentic AI' section
  last_reviewed: '2026-10-19'
  notes: 'Idea: discussed by the Law Society and California Bar as an emerging direction, not found as a measured deployment for this module.'
- id: professional-services-work-production-14
  title: Challenger role and unaided reasoning test for AI-assisted team work
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - review-assurance
  - expert-judgment
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: A coherent AI-structured draft invites continuation rather than challenge, so teams can approve work no one has independently reasoned through.
  solution: Thomson Reuters Legal proposes assigning challengers, having team members state reasoning in their own words, returning to primary sources, and asking at key points whether the team could construct and defend the analysis if AI disappeared.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: Practitioner proposal; no measurement found
    provenance: vendor-published
    source_ref: TRI-JUDGMENT-2026
  prerequisites:
  - Team norms and time for challenge
  - Access to primary sources
  risks_and_guardrails:
  - Added effort may erode the speed benefit, an objection the source does not quantify
  human_checkpoints:
  - Challenger reviews framing and omissions
  - Pre-finalization check of the two questions
  role_evolution: Reviewers act as challengers who test framing and omissions, not just edit wording (TRI-JUDGMENT-2026).
  evidence_grade: D
  sources:
  - ref: TRI-JUDGMENT-2026
    title: 'Designing judgment: Preserving AI-mediated legal collaboration'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/designing-judgment-ai-mediated-legal-collaboration
    date: '2026-10-06'
    access: full
    locator: Sections 'Delegation versus collaboration' and 'Designing for cognitive resilience'
  last_reviewed: '2026-10-19'
  notes: 'Idea (label): practitioner proposal from a vendor-affiliated institute; no firm reported adopting it in the sources read.'
- id: professional-services-work-production-15
  title: Tracking professionals' overrides of AI output to calibrate review
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: Without records of when professionals correct AI, firms cannot tell whether the system needs retraining or people need guidance.
  solution: Thomson Reuters Institute proposes documenting reasoning, sources and where judgment applies for each AI output, and tracking override and challenge so patterns by area become visible.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: Practitioner proposal; no override-rate data found
    provenance: vendor-published
    source_ref: TRI-STANDARDS-2026
  prerequisites:
  - Documentation of AI reasoning and sources
  - Light-weight tracking that is not burdensome
  risks_and_guardrails:
  - The source says procedures must not be burdensome but must be tracked
  human_checkpoints:
  - Periodic review of override patterns
  role_evolution: Review leads and KM teams analyse override patterns (TRI-STANDARDS-2026).
  evidence_grade: D
  sources:
  - ref: TRI-STANDARDS-2026
    title: 'Between accountability and chaos: Setting the AI standards that professionals demand'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/between-accountability-and-chaos
    date: '2026-10-12'
    access: full
    locator: Section 'Judgment validation standard'
  last_reviewed: '2026-10-19'
  notes: Idea (label). Absence of published override or error rates for AI-assisted professional work is itself a finding of this run.
- id: professional-services-work-production-16
  title: Task decomposition, chained prompts and an agent-suitability triage for drafting and review workflows
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Prompts that look fine in isolation break across matters, users and edge cases.
  solution: ILTACON 2026 session descriptions recommend breaking complex legal tasks into smaller AI-ready steps with chaining, and having a panel judge which proposed tasks suit agentic workflows and which should stay human-led, using tools firms already have such as Harvey, Legora and Leya.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: Session abstracts; no outcome data found
    provenance: self-reported
    source_ref: EDT-ILTACONMON-2026
  prerequisites:
  - Structured experimentation and governed iteration
  - Psychological safety to fail fast
  risks_and_guardrails:
  - Law.com's session coverage lists prompting pitfalls, but the article was paywalled beyond its opening paragraph (LAWCOM-PROMPT-2026)
  human_checkpoints:
  - Attorneys evaluate AI-generated work and give feedback
  role_evolution: Lawyers become designers and testers of workflows.
  evidence_grade: D
  sources:
  - ref: EDT-ILTACONMON-2026
    title: Monday Happenings at ILTACON 2026 (session abstracts)
    publisher: eDiscovery Today
    type: conference
    url: https://ediscoverytoday.com/2026/08/24/monday-happenings-at-iltacon-2026-ediscovery-trends/
    date: '2026-08-24'
    access: full
    locator: Abstracts for the prompting session and the agentic workflow design session (held August 2026)
  - ref: LAWCOM-PROMPT-2026
    title: 'ILTACON 2026 Day 1: AI Prompting Pitfalls That Lead Attorneys Astray'
    publisher: Law.com Legaltech News
    type: conference
    url: https://www.law.com/legaltechnews/2026/08/24/iltacon-2026-day-1-ai-prompting-pitfalls-that-lead-attorneys-astray-/
    date: '2026-08-24'
    access: search-only
    locator: Opening paragraph
  last_reviewed: '2026-10-19'
  notes: 'Idea (label): based on abstracts of sessions already held, not on recaps of results.'
- id: professional-services-work-production-17
  title: Precedent-grounded drafting and tracked-change editing inside Word
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Starting an agreement or memo from approved precedent and keeping formatting consistent takes manual assembly.
  solution: Microsoft's Copilot for Legal drafts from approved precedents stored in SharePoint with structured placeholders and applies redlines as native tracked changes; OpenAI made ChatGPT for Word generally available for proofreading, suggested edits and formatting flags. Anthropic, Google, OpenAI and Microsoft launched legal verticals within five months.
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: Product announcements; no usage data
    provenance: vendor-published
    source_ref: LAWSITES-MSFT-2026
  prerequisites:
  - Approved precedent library in the firm's document system
  - Admin controls over data
  risks_and_guardrails:
  - Artificial Lawyer says it is unclear whether Microsoft's skills will be good enough to keep lawyers in Word, and veterans doubt Microsoft's past legal efforts (AL-COPILOT-2026)
  - OpenAI's Trusted Access program includes zero data retention for the API (LAWSITES-ASTRA-2026)
  human_checkpoints:
  - Lawyer reviews tracked changes and drafted text
  role_evolution: Light AI users may be most affected because the tool sits in the app they already use (AL-COPILOT-2026).
  evidence_grade: C
  sources:
  - ref: LAWSITES-MSFT-2026
    title: Microsoft Launches Copilot for Legal, Becoming the Fourth AI Giant in Five Months to Build Out a Legal Vertical
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/microsoft-launches-copilot-for-legal-becoming-the-fourth-ai-giant-in-five-months-to-build-out-a-legal-vertical.html
    date: '2026-10-15'
    access: full
    locator: Paragraphs on redlining and drafting from precedents
  - ref: LAWSITES-ASTRA-2026
    title: OpenAI Releases Astra for Law, A GPT-6 Model Tailored for Legal Work
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/09/openai-releases-astra-for-law-a-gpt-6-model-configured-for-legal-work.html
    date: '2026-09-17'
    access: full
    locator: Paragraph on ChatGPT for Word and Trusted Access
  - ref: AL-COPILOT-2026
    title: Microsoft Copilot For Legal - What Will Be The Fallout?
    publisher: Artificial Lawyer
    type: press
    url: https://www.artificiallawyer.com/2026/10/15/microsoft-copilot-for-legal-what-will-be-the-fallout/
    date: '2026-10-15'
    access: full
    locator: Opening and closing paragraphs
  last_reviewed: '2026-10-19'
  notes: Announced 2026-10-15 and 2026-09-17; no customer deployment found.
```

## 3. Module notes

### Processes and key steps (with work types)

- Brief the task and gather source documents (`coordination-scheduling`, `research-synthesis`). Firms are building matter templates so inputs, instructions and reviewers are set in advance (HARVEY-ORCH-2026).
- Extract data, answer questions and summarize across document sets (`data-reporting`, `research-synthesis`) (VALS-VLAIR-2025).
- Research and synthesize authorities or evidence (`research-synthesis`) (VALS-LEGALRESEARCH-2025).
- Produce the first draft of a document, analysis or deck (`document-production`) (NBER-AUTOR-2026, LEXISNEXIS-FOW-2026).
- Review against a playbook, precedent or standard and mark up (`review-assurance`) (LAWSITES-MSFT-2026).
- Senior review, judgment and sign-off (`expert-judgment`) (CALBAR-GENAI-2026).
- Verify references and release to the client or court (`review-assurance`) (CTV-DELOITTE-2025, CHARLOTIN-HALLUC-2026).

### Common pain points

- Firms cannot yet show clients matter-level savings; speakers described being in an anecdotal phase of measurement and ROI judged more on conventional wisdom than evidence (TRI-LEGALWEEK-2026).
- Prompts that work in one matter break across matters, users and edge cases (EDT-ILTACONMON-2026, session abstract).
- Polished AI drafts invite edits to phrasing rather than challenge to assumptions (TRI-JUDGMENT-2026).
- Reference errors reach clients: Deloitte Australia partly refunded a government contract after a report with apparent AI-generated errors (CTV-DELOITTE-2025).
- The tasks AI absorbs (first-pass drafting, document review, research) were also how juniors were trained and billed (VAULT-PYRAMID-2026).
- 41% of professionals who use AI at work say they lack professional-grade tools, and 34% use unsanctioned tools (TR-FOP-2026).

### Metrics and benchmarks (with sources)

- Extraction, summarization, Q&A, redlining, chronology, transcript analysis against a lawyer baseline: Vals, Feb 2025 (VALS-VLAIR-2025). Examples: summarization baseline 50.3% versus 58.9% to 77.2% for AI tools; open-ended redlining baseline 79.7% versus 53.6% for Vincent AI.
- Legal research, 200 questions: AI products 74% to 78% versus lawyer baseline 69%; AI average weighted score above the baseline on 150 questions (VALS-LEGALRESEARCH-2025). Largest research platforms did not participate (LAWSITES-VALS-2025).
- Drafting quality and skill retention: +0.34 SD at 10 days and +0.38 SD at 90 days; +0.32 SD unaided redlining advantage, +0.45 SD for seniors (NBER-AUTOR-2026).
- Consulting tasks: 12.2% more tasks, 25.1% faster inside the frontier; 19% less likely correct outside it (HBS-DELLACQUA-2023; 2023 experiment).
- Hallucination rates of research tools: 17% to 33% in a 2024 preregistered evaluation (STANFORD-MAGESH-2024).
- Court decisions involving hallucinated material: 2,202 identified as of 2026-10-19 (CHARLOTIN-HALLUC-2026).
- Governance prevalence: human review of work product required by 31% to 83% of firms depending on size (ILTA-TECHSURVEY-2026).
- ROI and strategy: a Thomson Reuters speaker said firms with a GenAI strategy are 3.9 times more likely to achieve ROI and only 22% of firms have one (TRI-LEGALWEEK-2026; speaker statement, not a published table). Among professionals with a named strategy, 66% say AI meets or exceeds expectations (TR-FOP-2026).
- Client view: 78% of corporate clients say AI-enabled quality improvements are very important or essential, while 6% say most or all providers deliver them (TR-FOP-2026).
- Absent: no published override rates, error rates in production, parallel-run results or inspection outcomes for AI-assisted work product at a named firm.

### Guardrails and regulatory points

- California's 2026 guidance: the duty of competence requires reviewing, verifying and correcting AI outputs, and the lawyer, not the technology, keeps control of strategic decisions; agentic systems must not make substantive determinations, give advice or file pleadings without meaningful supervision; hourly billing must reflect time actually spent (CALBAR-GENAI-2026).
- The Law Society of England and Wales notes that solicitors remain responsible for their work whether or not AI is used, citing judicial guidance and an SRA warning notice, and recommends proportionate checkpoints around higher-risk agent actions (LAWSOC-AGENTIC-2026).
- Professionals say their tools must safeguard confidential data (96%), ground outputs in authoritative content (94%) and give explainable reasoning (90%) (TR-FOP-2026).
- Law firm policy coverage varies by size: a formal policy exists at 57% of firms under 50 lawyers and 98% of firms with 350 to 699 lawyers (ILTA-TECHSURVEY-2026).
- Disclosure and consent: the Deloitte Australia revised report disclosed use of Azure OpenAI (CTV-DELOITTE-2025).

### Frontier signals (dated, sourced)

- 2026-05-12: Anthropic released 20+ legal connectors and 12 practice-area plugins; each starts with a setup interview to learn a team's playbooks, escalation chains, risk calibration and house style (LAWSITES-ANTHROPIC-2026).
- 2026-09-17: OpenAI released Astra for Law with a legal search index and custom instructions for legal writing, and made ChatGPT for Word generally available (LAWSITES-ASTRA-2026).
- 2026-10-15: Microsoft launched Copilot for Legal (20+ skills in Word and Cowork, including review against playbooks and obligation extraction), the fourth AI major with a legal vertical in five months (LAWSITES-MSFT-2026). Artificial Lawyer expects the impact to land most with lawyers not yet heavy AI users (AL-COPILOT-2026).
- 2026-10-15: Harvey launched Legal Work Orchestration and said it expects agents to take on a further 20% of workflow steps in six months and for that share to triple in a year (HARVEY-ORCH-2026; vendor expectation).
- 2026-09-03: ILTACON product news (conference held 2026-08-23 to 27) was dominated by agentic AI and the Model Context Protocol (LAWSITES-ILTACONROUND-2026); one observer saw legal AI shifting from feature to infrastructure (EDT-CROWD3-2026).
- 2026-09-28: In-house panelists at a Thomson Reuters Institute forum said they measure AI success by productivity and faster turnaround more than by lower fees, and want firms to explain AI's effect on billing (TRI-AIFORUM-2026).
- 2026-03-13: Clients are asking for AI line items on invoices while other clients say they will not pay for work done by AI (TRI-LEGALWEEK-2026).
- 2026-10-19: The Law Society reports very limited use of fully autonomous agentic systems among those it spoke to, and confusion in the market about what counts as agentic (LAWSOC-AGENTIC-2026).
- 2026-03-25: PwC's US CEO said some tax and consulting services will become AI tools clients can use without a PwC person in the loop (CPAPA-PWC-2026; reporting the Financial Times). Routed to scoping-pricing.

### Workforce and role effects

- Associates form AI habits regardless of firm guidance; mid-level associates build their own agents (TRI-ONBOARD-2026).
- Juniors: the trial found no average unaided-skill gain for juniors and a split between gainers and losers (NBER-AUTOR-2026); 71% of professionals believe early-career roles need structured support from experienced peers and 48% worry about judgment development (TR-FOP-2026).
- Hiring: lateral associates were 51% of Am Law 200 associate hires in a SurePoint study, and 35% of large firms plan larger first-year classes versus 86% planning to grow associate ranks, per BCG Attorney Search (both as summarized by VAULT-PYRAMID-2026; secondary).
- Supervision: a Law Institute of Victoria podcast with Allens lawyers says AI has minimised grunt work, created space for higher-value thinking and changed the mentoring dynamic (ALLENS-XEXAM-2026).
- Differentiators: client service, judgment and anticipating risk (TRI-AIFORUM-2026); power skills such as instilling client confidence (TRI-ONBOARD-2026).
- Consulting: a former McKinsey consultant says juniors are expected to arrive with more judgment because the production tasks are automated (STRATEGYCASE-JUNIOR-2026; community source).
- Accounting: ICAEW notes a Financial Times report that Big Four consultant starting salaries stagnated since 2022 and a senior executive quote about investing in AI and offshoring rather than people (ICAEW-AI2026-2026). Ascend's CEO describes a 30-person AI team working alongside CPAs (AT-AINATIVE-2026).
- New roles: chief pricing and innovation officer, AI innovation head and law firm data scientists appear in practitioner accounts (TRI-LEGALWEEK-2026, EDT-CROWD2-2026).
- Big Law as training ground: Artificial Lawyer argues new-model firms must build training systems of their own (AL-BIGLAW-2026).

### Objections and concerns practitioners raise

- Savings are unproven and clients are inconsistent: some require AI, others forbid its use or will not pay for it (TRI-LEGALWEEK-2026).
- AI-structured drafts erode independent team reasoning, and responsibility diffuses (TRI-JUDGMENT-2026).
- Professionals are held accountable (47% say they are) without professional-grade tools (TRI-STANDARDS-2026, TR-FOP-2026).
- Platform hype: an ILTACON observer from a vendor said platforms claiming to do everything do nothing exceptionally well, and another said buyers have stopped listening to the word 'transformative' (EDT-CROWD3-2026). A veteran CEO asked whether legal tech had hit 'peak' (LAWSITES-PEAK-2026).
- Pricing of the tools themselves: seat-based to consumption-based pricing was a hallway worry, with vendors unwilling to discuss it (EDT-ILTACON-2026).
- Counterview: a Georgetown legal writing professor reports not seeing the skills degradation many fear (TRI-CLARITYWRITE-2026).
- A veteran respondent in ILTA's survey said earlier 'transformative' technologies produced minimal change and the hype might pass (ILTA-TECHSURVEY-2026).
- Employees hear 'productivity' and ask what happens to their job and to the time AI saves (TRI-CLARITYHUMAN-2026).

### Interview probes for an advisor

1. Which first-draft, extraction or playbook-review tasks do people here already do with AI, and what is the written rule for who checks the output and how?
2. Do you have any measurement of AI-assisted work (rework, errors caught in review, override rate, time to first draft) against your own pre-AI baseline, or only anecdotes?
3. When a client asks what AI saved on their matter, what do you show them, and who decides how the saving is shared?
4. Where does your first-year or early-career work come from now that drafts, summaries and first-pass review are produced by tools?
5. Who owns the playbooks, templates and precedents the tools draw on, and what happens when they go stale or a model changes?

## 4. Routed to other modules

- **billing-collections:** clients asking for AI line items on invoices and single line-item bills (TRI-LEGALWEEK-2026); California rules on billing for AI-assisted time (CALBAR-GENAI-2026).
- **scoping-pricing:** PwC One and subscription tools without a person in the loop (CPAPA-PWC-2026); pricing for judgment rather than hours in tax and accounting (TRI-CHARGING-2026); consumption-based AI pricing worries (EDT-ILTACON-2026).
- **talent-learning:** Duane Morris onboarding redesign with AI champions and power skills (TRI-ONBOARD-2026); pyramid and hiring data (VAULT-PYRAMID-2026); Allens supervision practice (ALLENS-XEXAM-2026); legal writing pedagogy (TRI-CLARITYWRITE-2026); junior consultant learning (STRATEGYCASE-JUNIOR-2026).
- **acceptance-risk and quality-review (cross-cutting governance):** shadow AI at 34% of professionals (TR-FOP-2026) and 54% of surveyed consultants (LEXISNEXIS-FOW-2026); firm policies by size (ILTA-TECHSURVEY-2026).
- **firm-finance:** ROI measurement and strategy gaps (TRI-LEGALWEEK-2026, TRI-STANDOUT-2026: 25% strongly agree their firm has a plan for monetizing AI usage); platform market concentration at ILTACON (LAWSITES-PEAK-2026, EDT-ILTACON-2026).
- **client-development:** only about one-third of embedded-AI partners have discussed AI with 60% or more of clients (TRI-STANDOUT-2026).
- **knowledge-management:** custom agents for knowledge management and shared playbooks (HARVEY-HLC-2026); firms extracting lawyers' knowledge into workflows (VAULT-PYRAMID-2026).
- **delivery-management:** Legal Work Orchestration task and status tracking (HARVEY-ORCH-2026).
- **tax archetype:** more than 70% of tax firms automate up to a quarter or more of tax workflows (TRI-CHARGING-2026); the EY and KPMG agent platforms (ICAEW-AI2026-2026).
- **legal-practice extension (litigation and e-discovery):** AI document review products and validation approach derived from technology-assisted review (LAWSITES-ILTACONROUND-2026, EDT-CROWD2-2026); the Thomson Reuters Institute and ILTA AI Guide for Litigators (TRI-AIGUIDELIT-2026).

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-AIFORUM-2026 | The 2026 Future of AI & Technology Forum: What AI can't replace in the client-law firm relationship | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/what-ai-cant-replace | 2026-09-28 | full |
| TRI-ONBOARD-2026 | Law firms need to redesign new attorney onboarding for the AI era | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding | 2026-10-12 | full |
| TRI-JUDGMENT-2026 | Designing judgment: Preserving AI-mediated legal collaboration | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/designing-judgment-ai-mediated-legal-collaboration | 2026-10-06 | full |
| TRI-STANDARDS-2026 | Between accountability and chaos: Setting the AI standards that professionals demand | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/between-accountability-and-chaos | 2026-10-12 | full |
| TRI-CLARITYWRITE-2026 | Is AI ruining legal writing or are we teaching it wrong? (Clarity podcast, S6 E6) | Thomson Reuters Institute | podcast | https://www.thomsonreuters.com/en/institute/podcast/ai-ruining-legal-writing | 2026-10-07 | full |
| TRI-CLARITYHUMAN-2026 | How does the human side of AI transformation make or break an enterprise AI strategy? (Clarity podcast, S6 E8) | Thomson Reuters Institute | podcast | https://www.thomsonreuters.com/en/institute/podcast/human-side-of-ai-transformation | 2026-10-15 | full |
| TRI-AIGUIDELIT-2026 | New AI Guide for Litigators can help litigators understand how AI impacts their practice | Thomson Reuters Institute and ILTA | professional-body | https://www.thomsonreuters.com/en/institute/reports/ai-guide-for-litigators | 2026-09-15 | full |
| TRI-CHARGING-2026 | If AI can do the work, then what are you actually charging for? | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/what-are-you-actually-charging-for | 2026-10-02 | full |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 | full |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 | full |
| ILTA-TECHSURVEY-2026 | 2026 ILTA Technology Survey: Executive Summary | International Legal Technology Association (ILTA) | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 | full |
| EDT-ILTACON-2026 | My Five ILTACON 2026 Takeaways | eDiscovery Today (Doug Austin) | community | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 | full |
| EDT-CROWD1-2026 | Crowdsourced ILTACON 2026 Observations (part one) | eDiscovery Today | community | https://ediscoverytoday.com/2026/09/01/crowdsourced-iltacon-2026-observations-legal-technology-trends/ | 2026-09-01 | full |
| EDT-CROWD2-2026 | Part Two of ILTACON 2026 Crowdsourced Observations | eDiscovery Today | community | https://ediscoverytoday.com/2026/09/02/part-two-of-iltacon-2026-crowdsourced-observations-legal-technology-trends/ | 2026-09-02 | full |
| EDT-CROWD3-2026 | Part Three of ILTACON 2026 Crowdsourced Observations | eDiscovery Today | community | https://ediscoverytoday.com/2026/09/03/part-three-of-iltacon-2026-crowdsourced-observations-legal-technology-trends/ | 2026-09-03 | full |
| EDT-ILTACONMON-2026 | Monday Happenings at ILTACON 2026 (session abstracts) | eDiscovery Today | conference | https://ediscoverytoday.com/2026/08/24/monday-happenings-at-iltacon-2026-ediscovery-trends/ | 2026-08-24 | full |
| EDT-ILTACONTUE-2026 | Tuesday Happenings at ILTACON 2026 (session abstracts) | eDiscovery Today | conference | https://ediscoverytoday.com/2026/08/25/tuesday-happenings-at-iltacon-2026-ediscovery-trends/ | 2026-08-25 | full |
| LAWCOM-PROMPT-2026 | ILTACON 2026 Day 1: AI Prompting Pitfalls That Lead Attorneys Astray | Law.com Legaltech News | conference | https://www.law.com/legaltechnews/2026/08/24/iltacon-2026-day-1-ai-prompting-pitfalls-that-lead-attorneys-astray-/ | 2026-08-24 | search-only |
| LAWSITES-PEAK-2026 | Have We Reached 'Peak Legal Tech?' Sure Felt That Way At ILTACON this Week | LawSites (Bob Ambrogi) | press | https://www.lawnext.com/2026/08/have-we-reached-peak-legal-tech-sure-felt-that-way-at-iltacon-this-week.html | 2026-08-28 | full |
| LAWSITES-ILTACONROUND-2026 | ILTACON News Round-Up Part 1, E-Discovery: DISCO, Everlaw, Nuix, Relativity, Reveal | LawSites (Bob Ambrogi) | press | https://www.lawnext.com/2026/09/iltacon-news-round-up-part-1-e-discovery-disco-everlaw-nuix-relativity-reveal.html | 2026-09-03 | full |
| LAWSITES-MSFT-2026 | Microsoft Launches Copilot for Legal, Becoming the Fourth AI Giant in Five Months to Build Out a Legal Vertical | LawSites (Bob Ambrogi) | press | https://www.lawnext.com/2026/10/microsoft-launches-copilot-for-legal-becoming-the-fourth-ai-giant-in-five-months-to-build-out-a-legal-vertical.html | 2026-10-15 | full |
| LAWSITES-ANTHROPIC-2026 | Anthropic Goes All-In on Legal, Releasing More Than 20 Connectors and 12 Practice-Area Plugins for Claude | LawSites (Bob Ambrogi) | press | https://www.lawnext.com/2026/05/anthropic-goes-all-in-on-legal-releasing-more-than-20-connectors-and-12-practice-area-plugins-for-claude.html | 2026-05-12 | full |
| LAWSITES-ASTRA-2026 | OpenAI Releases Astra for Law, A GPT-6 Model Tailored for Legal Work | LawSites (Bob Ambrogi) | press | https://www.lawnext.com/2026/09/openai-releases-astra-for-law-a-gpt-6-model-configured-for-legal-work.html | 2026-09-17 | full |
| LAWSITES-VALS-2025 | Vals AI's Latest Benchmark Finds Legal and General AI Now Outperform Lawyers in Legal Research Accuracy | LawSites (Bob Ambrogi) | press | https://www.lawnext.com/2025/10/vals-ais-latest-benchmark-finds-legal-and-general-ai-now-outperform-lawyers-in-legal-research-accuracy.html | 2025-10-23 | full |
| VALS-VLAIR-2025 | Vals Legal AI Report (VLAIR), February 2025 | Vals AI | academic | https://www.vals.ai/vlair | 2025-02-27 | full |
| VALS-LEGALRESEARCH-2025 | VLAIR - Legal Research | Vals AI | academic | https://vals.ai/industry-reports/vlair-10-14-25 | 2025-10-14 | full |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER WP 35720) | National Bureau of Economic Research | academic | https://econpapers.repec.org/RePEc:nbr:nberwo:35720 | 2026-09 | full |
| HBS-DELLACQUA-2023 | Navigating the Jagged Technological Frontier (HBS Working Paper 24-013) | Harvard Business School | academic | https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 | 2023 | full |
| STANFORD-MAGESH-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools | Stanford RegLab and HAI (arXiv 2405.20362) | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 | full |
| CHARLOTIN-HALLUC-2026 | AI Hallucination Cases Database (live; accessed 2026-10-19) | Damien Charlotin | academic | https://www.damiencharlotin.com/hallucinations/ | 2026-10-19 | full |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition) | State Bar of California, COPRAC | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05 | full |
| LAWSOC-AGENTIC-2026 | What is agentic AI - and what does it mean for legal practice | Law Society of England and Wales | professional-body | https://www.lawsociety.org.uk/topics/ai-and-lawtech/what-is-agentic-ai-and-what-does-it-mean-for-legal-practice | 2026-10-19 | full |
| ICAEW-AI2026-2026 | Will 2026 be AI's year? AI adoption trends | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/jan-2026/will-2026-be-ais-year-ai-adoption-trends | 2026-01 | full |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors | CTV News (Associated Press) | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 | full |
| CPAPA-PWC-2026 | PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm' (reporting the Financial Times) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/ | 2026-03-25 | full |
| AT-AINATIVE-2026 | The AI-native firm (On the Air with Accounting Today, with Ascend CEO David Wurtzbacher) | Accounting Today | podcast | https://www.accountingtoday.com/podcast/the-ai-native-firm | 2026-10-19 | full |
| AL-COPILOT-2026 | Microsoft Copilot For Legal - What Will Be The Fallout? | Artificial Lawyer | press | https://www.artificiallawyer.com/2026/10/15/microsoft-copilot-for-legal-what-will-be-the-fallout/ | 2026-10-15 | full |
| AL-BIGLAW-2026 | Big Law's Greatest Gifts | Artificial Lawyer | press | https://www.artificiallawyer.com/2026/10/19/big-laws-greatest-gifts/ | 2026-10-19 | full |
| HARVEY-ORCH-2026 | Making Harvey the Orchestration Layer for Legal Work | Harvey | vendor | https://www.harvey.ai/blog/legal-work-orchestration | 2026-10-15 | full |
| HARVEY-HLC-2026 | Hogan Lovells Cadwalader adopts Harvey | Harvey | vendor | https://www.harvey.ai/blog/hogan-lovells-cadwalader-adopts-harvey | 2026-10-16 | full |
| HARVEY-GE-2026 | GE Aerospace deploys Harvey across its Legal & Compliance organization | Harvey | vendor | https://www.harvey.ai/blog/ge-aerospace-deploys-harvey-across-its-legal-and-compliance-organization | 2026-09-01 | full |
| HARVEY-TCENERGY-2026 | TC Energy deploys Harvey across its legal team | Harvey | vendor | https://www.harvey.ai/blog/tc-energy-deploys-harvey-across-its-legal-team | 2026-10-05 | full |
| HARVEY-OGIER-2026 | Ogier adopts Harvey firmwide | Harvey | vendor | https://www.harvey.ai/blog/ogier-adopts-harvey-firmwide | 2026-10-12 | full |
| LEGORA-HLC-2026 | Hogan Lovells Cadwalader rolls out Legora globally | Legora | vendor | https://legora.com/newsroom/hogan-lovells-cadwalader-rolls-out-legora-globally | 2026-10-16 | full |
| AOSHEARMAN-HARVEY-2025 | A&O Shearman and Harvey to roll out agentic AI agents targeting complex legal workflows | A&O Shearman | firm | https://www.aoshearman.com/en/news/ao-shearman-and-harvey-to-roll-out-agentic-ai-agents-targeting-complex-legal-workflows | 2025-04 | full |
| VAULT-PYRAMID-2026 | The Compressed Pyramid: What AI Means for the Associate Career Ladder | Vault | press | https://legacy.vault.com/blogs/vaults-law-blog-legal-careers-and-industry-news/the-compressed-pyramid-what-ai-means-for-the-associate-career-ladder | 2026-08-11 | full |
| ALLENS-XEXAM-2026 | How AI in legal supervision is changing lawyer training (Cross-Examined podcast, Law Institute of Victoria) | Law Institute of Victoria | podcast | https://www.castfox.net/podcast/cross-examined-7610284/episode/how-ai-in-legal-supervision-is-changing-lawyer-training-1785836 | 2026-03-23 | full |
| LEXISNEXIS-FOW-2026 | Generative AI in professional services (blog on the LexisNexis Future of Work 2026: Management Consulting Industry Report) | LexisNexis | vendor | https://www.lexisnexis.com/blogs/amppage/30/generative-ai-professional-services | 2026-04-16 | full |
| STRATEGYCASE-JUNIOR-2026 | Will AI Replace Junior Consultants? What's Actually Changing | StrategyCase (former McKinsey consultant's coaching site) | community | https://strategycase.com/artificial-intelligence-and-the-junior-consultant-how-entry-training-and-work-are-changing | 2026-02-05 | full |

Count by type: academic 6, community 5, conference 5, firm 1, podcast 4, press 15, professional-body 3, regulator 1, survey 3, vendor 7. Total 50. Counts include the 1 item(s) marked search-only (paywalled after its first paragraph).

## 6. Gaps

- **Quality evidence from practice.** No published error rates, override rates, parallel-run results or inspection outcomes were found for AI-assisted drafts, extraction or playbook review at a named firm or in-house team. Quality evidence is limited to benchmarks (Vals, Stanford), one randomized trial (NBER) and incident records (Deloitte Australia, Charlotin database).
- **Playbook-driven review.** Vendor time-saving figures for playbook redlining appeared in search results (for example Sirion, Lucio) but are vendor content without named studies, so they were not used.
- **Consulting.** McKinsey's Lilli page returned 403 and the Business Insider interview (via Yahoo) returned 403; figures about Lilli and agent counts appear only in a secondary coaching-site summary and were left out of outcomes. No firm-published first-draft or deck-quality data found for McKinsey, BCG, Bain, Deloitte, EY, KPMG or PwC. Source Global Research, MCA and PMI discourse on work production not found. The LexisNexis consulting report was seen only through a vendor blog summary.
- **Accounting and advisory.** AICPA ENGAGE session listings mention AI but no work-production session content was retrievable; the Karbon State of AI report page did not expose figures; ICAEW coverage is mostly 2025 launches. Audit procedures and tax technical work were left to their archetypes.
- **Conferences.** Legalweek 2026 session pages (Law.com event site) returned errors or empty pages; CLOC Global Institute programme is JavaScript-rendered; ILTACON recordings are members-only; Law.com's ILTACON prompting-session article was paywalled after its opening paragraph (search-only). The ILTACON validation session was moderated by eDiscovery Today, but no published results from it were found.
- **Regulators and press.** UK Bar Standards Board 'absolute caution' guidance (Law360 UK, headline only), SRA warning notice and ABA Formal Opinion 512 were not opened; the Law Society cites the SRA notice and judicial guidance. Law Gazette (405) and Ropes & Gray podcast (403) pages were blocked.
- **Podcasts and communities.** Few podcast episodes with substantive work-production content were found; Legal Evolution (403) and Above the Law were not reached. The TR Future of Professionals report page does not show its release month (page timestamp 2026-09-30 from a text mirror), so its date is given as 2026.
- **In-house.** In-house evidence comes from vendor announcements (GE Aerospace, TC Energy) and one conference panel; no CLOC session content was readable.
- **Search budget.** 10 web searches used; most results were vendor marketing and were not relied on.

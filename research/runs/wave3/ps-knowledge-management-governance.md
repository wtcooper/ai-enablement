# Knowledge management: governance and evidence (professional services)

Prepared 2026-10-19. Archetype: professional-services. Module: knowledge-management. Angle: governance (what constrains and measures the work). Public sources only.

## 1. Summary

- **Scope.** 15 candidate use cases, graded A: 0, B: 4, C: 11, D: 0. 47 distinct sources are listed; 46 were opened and read in full or in part, 1 is search-only (ABA Formal Opinion 512, whose PDF was blocked; only secondary summaries were read).
- **No grade A.** No firm or in-house team publishes measured outcomes (error rates, override rates, parallel-run results, retrieval success, time saved) for its own knowledge base or enterprise search. The measured figures that exist come from adjacent processes: legal research tools (Stanford: 17-33% hallucination), document Q&A (Vals), patent drafting (NBER 35720), and customer-support agents (NBER 31161). Those entries are capped at B.
- **The binding constraint is access and confidentiality, not capability.** Bar guidance in New York and California, and secondary summaries of ABA Formal Opinion 512, put the risk of AI over a firm's own material in three places: client confidential information entering systems that share or learn from it, information reaching lawyers walled off from a matter, and agentic tools with standing access to document systems and knowledge bases. Vendors answer with permission inheritance; no public test results of that claim were found.
- **Verification is the second constraint.** Independent testing found retrieval-based legal tools still hallucinate (Stanford, 17-33%). The Ayinde court (2025-06-06) put the duty to check against authoritative sources on lawyers and said leaders must take practical and effective measures, and may be asked whether they did.
- **Governance maturity follows firm size.** In ILTA's 2026 survey of 508 firms a formal GenAI policy ranges from 57% (under 50 lawyers) to 98% (350-699 lawyers); training required before use ranges from 11% to 72%; client approval required from 8% to 38%. ILTA also finds knowledge infrastructure (enterprise search, expertise management) dramatically underdeveloped.
- **Shadow use is the live gap.** Thomson Reuters reports 34% of professionals use unsanctioned AI; iManage reports 36% have experienced a policy violation. A US court (Heppner, 2026-02) held a defendant's self-directed public-AI chats were not privileged.
- **Measurement is weak.** APQC finds KM impact hard to measure; at Legalweek 2026 firms answering clients' savings questions often said they were still gathering data (TRI-LEGALWEEK-2026).
- **Client terms are split.** Some clients demand AI-driven savings and AI line items; others require explicit permission or will not pay for AI-done work (TRI-LEGALWEEK-2026).

## 2. Use cases

Grade rule applied: A needs a figure the named organisation reports as measured for this module's use; measurements from an adjacent process cap the grade at B; surveys of anonymous firms and vendor product pages are C. Source dates marked as the read date are product pages with no printed date.

```yaml
- id: professional-services-knowledge-management-01
  title: Permission-aware AI search and Q&A over the firm document system and curated knowledge
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - research-synthesis
  - data-reporting
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Past matters, precedents and know-how sit in the document management system, but ILTA's 2026 survey summary
    describes knowledge infrastructure as dramatically underdeveloped across enterprise search and expertise management.
    Plain keyword search does not tell a lawyer which prior work is relevant, and a naive AI layer could surface
    material from matters the user is walled off from.
  solution: Lawyers ask natural-language questions and receive answers drawn from firm-approved precedents and curated
    collections through the document system's own index. The vendor documents say the index and any AI tool connected
    through the Model Context Protocol (MCP) inherit the existing permissions and ethical walls, so each user retrieves
    only what they could already open. A Legora-iManage connection announced on 2026-10-16 would let mutual customers
    draw on that governed knowledge from inside Legora.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: No retrieval-quality, time-saved or leakage-test figures found for this use; the vendor pages state
      permission inheritance as a design feature, not a measured result
    provenance: vendor-published
    source_ref: IMANAGE-INSIGHT-2026
  prerequisites:
  - A document management system with current matter-level permissions and ethical-wall rules (the AI layer can
    only inherit what is configured)
  - Metadata and curated collections good enough to retrieve against (APQC says AI exposes weaknesses in content
    quality, governance, taxonomy and ownership)
  - A decision on what data leaves the document system when a third-party AI tool connects (iManage tells customers
    to ask their AI vendors how data is handled)
  risks_and_guardrails:
  - Where a generative AI system uses client information, the firm must make sure it applies any required ethical
    screens, so a screened lawyer is not exposed to those documents through the firm's AI systems (NYC Bar Formal
    Op. 2024-5, p. 3-4)
  - Agentic systems with access to document systems, email or knowledge bases create acute confidentiality risk;
    the California guidance says lawyers must limit the scope of access and implement monitoring and access controls
    (CALBAR-GENAI-2026, p. 6)
  - Secondary summaries of ABA Formal Op. 512 report that it flags disclosure risk even among lawyers inside one
    firm when a self-learning tool is used, including exposure to personnel barred by an ethical wall (EZEL-ABA512-2024;
    original not read)
  - No test results on permission leakage in AI search were found in any public source
  human_checkpoints:
  - The lawyer checks each answer against the cited source documents before relying on it
  - IT and KM owners test and audit permission inheritance (for example with users who sit behind a wall) before
    and after rollout
  role_evolution: Vendor material describes knowledge teams curating, publishing, maintaining and archiving collections
    that feed the assistant (IMANAGE-INSIGHT-2026, curation toolset section). ILTA reports that many firms anticipate
    added headcount in knowledge management among other roles (ILTA-TECHSURVEY-2026, p. 5).
  evidence_grade: C
  sources:
  - ref: IMANAGE-INSIGHT-2026
    title: 'iManage Insight+: Discover institutional knowledge (product page; read 19 Oct 2026)'
    publisher: iManage
    type: vendor
    url: https://imanage.com/imanage-products/knowledge-search-management/insightplus/
    date: '2026-10-19'
    access: full
    locator: Sections "Establish", "Trusted answers, naturally" and "Curation toolset"
  - ref: IMANAGE-MCP-2026
    title: Securely Connect to AI Tools with Model Context Protocol (product page; read 19 Oct 2026)
    publisher: iManage
    type: vendor
    url: https://imanage.com/imanage-products/the-imanage-platform/ai/model-context-protocol/
    date: '2026-10-19'
    access: full
    locator: Sections "Governed & auditable access" and "iManage stays the source"
  - ref: LEGORA-IMANAGE-2026
    title: Legora and iManage deepen integration through iManage MCP Server (press release)
    publisher: Legora
    type: vendor
    url: https://legora.com/newsroom/legora-and-imanage-deepen-integration-through-imanage-mcp-server
    date: '2026-10-16'
    access: full
    locator: Paragraphs 2-4 (announcement worded "will be able to"; permissions determine what each user can retrieve)
  - ref: NYCBAR-OP2024-5-2024
    title: 'Formal Opinion 2024-5: Ethical Obligations of Lawyers and Law Firms Relating to the Use of Generative
      Artificial Intelligence in the Practice of Law'
    publisher: New York City Bar Association, Professional Ethics Committee
    type: professional-body
    url: https://www.nycbar.org/wp-content/uploads/2024/08/20221329_GenerativeAILawPractice.pdf
    date: '2024-08-07'
    access: full
    locator: Confidentiality and Conflicts of Interest rows, pp. 2-4
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision,
      replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Duty of Confidentiality row, pp. 5-6
  - ref: ILTA-TECHSURVEY-2026
    title: '2026 ILTA Technology Survey: Executive Summary (PDF carries no printed date)'
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: '2026'
    access: full
    locator: p. 9 ("Curtain Call for the Data Center") and p. 5 (headcount)
  - ref: EZEL-ABA512-2024
    title: 'ABA Formal Op. 512: Generative AI Tools (plain-English summary of the opinion)'
    publisher: Ezel
    type: vendor
    url: https://ezel.ai/ethics-opinions/aba/512-generative-ai-tools
    date: '2024-07-29'
    access: full
    locator: Confidentiality paragraph (secondary summary)
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools (original PDF blocked; only secondary summaries
      read)'
    publisher: American Bar Association
    type: professional-body
    url: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: search-only
    locator: Section on confidentiality (original blocked; not read)
  last_reviewed: '2026-10-19'
  notes: 'No named customer deployment of permission-aware AI search was found, so maturity is "announced". The
    Legora-iManage release is dated 2026-10-16 and speaks in the future tense. Vendor product pages (IMANAGE-INSIGHT-2026,
    IMANAGE-MCP-2026) carry no publication date; the date shown is the day they were read. ABA-OP512-2024 is search-only:
    the PDF was blocked and only secondary summaries were read.'
- id: professional-services-knowledge-management-02
  title: Drafting from firm precedents and past work product, with confidentiality and client-term checks
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - document-production
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Reusing a prior deal or matter means someone finds the right precedent, strips client-specific detail
    and adapts it. The old process depends on personal memory and checklists. Harvey describes the process as often
    reconstructed for each new matter from a checklist, a previous deal or the knowledge of people who have done
    it before.
  solution: A new matter opens from a reusable template that carries phases, tasks, playbooks, agents and review
    gates, defined once by innovation and knowledge teams. Agents draft against the firm's own precedents and playbooks
    and lawyers review at designated gates. Governed DMS content can be retrieved under existing permissions.
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: No time-saved or quality figures published; the Harvey post describes the capability and does not
      report customer results
    provenance: vendor-published
    source_ref: HARVEY-ORCH-2026
  prerequisites:
  - A precedent library with owners, currency and quality status, so stale or one-client-specific documents are
    not reused as if they were templates
  - Known client AI instructions per matter (the California guidance says lawyers must follow client instructions
    or guidelines that restrict AI)
  - A rule for anonymising or sanitising client detail before material enters shared templates
  risks_and_guardrails:
  - The Law Society says client confidential and personal data should not be used to create templates or to test
    a generative AI system, and that fictional data should be used instead (LAWSOC-GENAI-2026, FAQ on templates
    and testing)
  - Without client consent a lawyer must not put confidential client information into a system that shares it with
    third parties; systems that keep inputs inside the firm's own databases do not pose that risk, but the lawyer
    must still stop information reaching colleagues behind an ethical wall (NYCBAR-OP2024-5-2024, pp. 2-3)
  - Secondary summaries of ABA Formal Op. 512 say consent for self-learning tools must be informed and that boilerplate
    engagement-letter wording is not enough (EZEL-ABA512-2024; original not read)
  - 'Clients are not uniform: some ask firms to prove AI savings while others issue directives that forbid AI use
    without explicit permission (TRI-LEGALWEEK-2026)'
  human_checkpoints:
  - Supervising lawyer reviews each agent output at the designated review gate
  - A KM lawyer or precedent owner approves what enters the template library
  - Matter team checks the client's AI terms before opening the matter on an AI-enabled template
  role_evolution: Harvey says innovation and knowledge teams define the template structure once for others to follow
    (HARVEY-ORCH-2026). The Law Society's April 2026 report expects junior roles to change first, with oversight
    and validation work growing (LAWSOC-AGENTIC-2026).
  evidence_grade: C
  sources:
  - ref: HARVEY-ORCH-2026
    title: Making Harvey the Orchestration Layer for Legal Work
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/legal-work-orchestration
    date: '2026-10-15'
    access: full
    locator: Sections "Capture the Process in a Reusable Template" and "Give Every Task the Context it Needs" (launch
      post dated 2026-10-15)
  - ref: IMANAGE-INSIGHT-2026
    title: 'iManage Insight+: Discover institutional knowledge (product page; read 19 Oct 2026)'
    publisher: iManage
    type: vendor
    url: https://imanage.com/imanage-products/knowledge-search-management/insightplus/
    date: '2026-10-19'
    access: full
    locator: Section "Elevating knowledge work across law firms"
  - ref: NYCBAR-OP2024-5-2024
    title: 'Formal Opinion 2024-5: Ethical Obligations of Lawyers and Law Firms Relating to the Use of Generative
      Artificial Intelligence in the Practice of Law'
    publisher: New York City Bar Association, Professional Ethics Committee
    type: professional-body
    url: https://www.nycbar.org/wp-content/uploads/2024/08/20221329_GenerativeAILawPractice.pdf
    date: '2024-08-07'
    access: full
    locator: Duty of Confidentiality row, pp. 2-3
  - ref: LAWSOC-GENAI-2026
    title: 'Generative AI: the essentials (page undated; cites events up to April 2026)'
    publisher: The Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials
    date: '2026'
    access: full
    locator: FAQ "Can I use client confidential and personal data in my organisation to create templates or test
      a generative AI system?"
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision,
      replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Communication Regarding Generative AI Use row, p. 7
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: Section "The contradictions in the room"
  - ref: LAWSOC-AGENTIC-2026
    title: The future of agentic AI in legal practice (report summary page)
    publisher: The Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice
    date: '2026-04-14'
    access: full
    locator: Section "Workforce and skills could be impacted"
  - ref: EZEL-ABA512-2024
    title: 'ABA Formal Op. 512: Generative AI Tools (plain-English summary of the opinion)'
    publisher: Ezel
    type: vendor
    url: https://ezel.ai/ethics-opinions/aba/512-generative-ai-tools
    date: '2024-07-29'
    access: full
    locator: Confidentiality and consent paragraphs (secondary summary)
  last_reviewed: '2026-10-19'
  notes: 'Product launch only: no named customer, pilot or result was found for precedent-based drafting inside
    Harvey''s orchestration product, so maturity is "announced". Overlaps work-production at the drafting step;
    the knowledge-management part is the reuse and curation of precedent.'
- id: professional-services-knowledge-management-03
  title: Curated, firm-approved knowledge collections as the grounding set for AI assistants
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: AI answers are only as trustworthy as the content behind them. APQC's 2026 survey finds most KM programmes
    are early in maturity and that the top threat is a culture that does not reward sharing and reuse, while 94%
    of professionals in the Thomson Reuters survey want outputs grounded in authoritative content.
  solution: Knowledge teams run a submit, enrich, publish, maintain and archive workflow for collections of vetted
    precedents and best practices, and the AI assistants are pointed at those collections first. APQC advises KM
    teams to identify business-critical knowledge domains and prepare those assets for AI-enabled search, recommendations
    and reuse.
  outcomes:
  - lever: quality
    description: Baseline of KM programme maturity among survey participants (not a result of this use case)
    figure: 59% in the two earliest maturity stages (20% just getting started, 39% developing); 21% optimizing or
      innovating
    measures: Share of 164 survey participants placing their KM programme at each maturity stage, per APQC (survey
      of 164 global participants, data collected November 2025)
    provenance: independent
    source_ref: APQC-KM-2026
  - lever: quality
    description: Cultural barrier to knowledge reuse
    figure: 40% say organizational culture does not incentivize knowledge sharing and reuse, the top-ranked threat
    measures: Share of 162 respondents ranking this as a threat to KM success, ahead of change fatigue at 39%
    provenance: independent
    source_ref: APQC-KM-2026
  - lever: quality
    description: Professionals' stated need for grounded tools, and gap in access
    figure: 94% say AI tools must ground outputs in authoritative content; 41% of professionals who use AI at work
      lack tools built on verified professional content
    measures: Share of professionals (base not stated on the page; survey of 1,816 professionals, Mar-Apr 2026,
      62 countries) naming grounding as a must-have; share of professionals who use AI at work without access to
      such tools, per Thomson Reuters
    provenance: vendor-published
    source_ref: TR-FOP-2026
  prerequisites:
  - Named owners and a review cycle for each collection
  - A taxonomy and metadata standard the retrieval layer can use
  - 'Incentives for lawyers to contribute (APQC: culture is the top-ranked threat)'
  risks_and_guardrails:
  - AI can accelerate KM but also exposes weaknesses in content quality, governance, taxonomy and ownership (APQC-KMEXEC-2026)
  - Errors in an agentic system can be repeated rapidly across multiple matters, according to the Law Society's
    April 2026 report (LAWSOC-AGENTIC-2026); the same would hold for a flawed precedent that many drafts reuse
  - The California guidance requires periodic reassessment of an AI system's capabilities and risks, including when
    it is deployed for new tasks (CALBAR-GENAI-2026, p. 5)
  human_checkpoints:
  - A KM lawyer approves each asset before publication to a collection
  - Collection owners retire or refresh assets on a set cycle
  role_evolution: Vendor material describes knowledge teams as curators of assets that lawyers submit (IMANAGE-INSIGHT-2026,
    Curation toolset). ILTA reports firms expect more KM headcount (ILTA-TECHSURVEY-2026, p. 5).
  evidence_grade: C
  sources:
  - ref: APQC-KM-2026
    title: 2026 Knowledge Management Priorities and Trends Survey Report (listing page with key findings)
    publisher: APQC
    type: survey
    url: https://www.apqc.org/resource-library/resource-listing/2026-knowledge-management-priorities-and-trends-survey-report
    date: '2026-01-07'
    access: full
    locator: Key findings (n=164 and n=162 as stated)
  - ref: APQC-KMEXEC-2026
    title: '2026 KM Priorities & Trends: Executive Summary'
    publisher: APQC
    type: survey
    url: https://www.apqc.org/resource-library/resource/2026-km-priorities-trends-executive-summary/html
    date: '2026-05-12'
    access: full
    locator: Sections "How is AI changing knowledge management in 2026?" and "How can KM leaders prove business
      value and impact?"
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: Key findings 01 and "The fiduciary standard" section
  - ref: IMANAGE-INSIGHT-2026
    title: 'iManage Insight+: Discover institutional knowledge (product page; read 19 Oct 2026)'
    publisher: iManage
    type: vendor
    url: https://imanage.com/imanage-products/knowledge-search-management/insightplus/
    date: '2026-10-19'
    access: full
    locator: Section "Curation toolset"
  - ref: LAWSOC-AGENTIC-2026
    title: The future of agentic AI in legal practice (report summary page)
    publisher: The Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice
    date: '2026-04-14'
    access: full
    locator: Section "Risks need urgent clarity"
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision,
      replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Duties of Competence and Diligence row, p. 5
  - ref: ILTA-TECHSURVEY-2026
    title: '2026 ILTA Technology Survey: Executive Summary (PDF carries no printed date)'
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: '2026'
    access: full
    locator: p. 5
  last_reviewed: '2026-10-19'
  notes: The APQC figures are cross-industry (not professional services only) and describe KM programme maturity,
    not outcomes of AI use. No firm was found describing a curated-collection programme with measured results.
- id: professional-services-knowledge-management-04
  title: Source-checking of AI research and knowledge answers before they are reused or relied on
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Retrieval-grounded legal tools are marketed as reducing or avoiding hallucination, but independent testing
    found otherwise, and courts and clients have met fabricated authorities. Once a wrong answer is filed into a
    precedent bank or report it is reused.
  solution: Answers carry links to the underlying sources, and a named person checks quotations, citations and cited
    facts against authoritative sources before the answer is relied on, filed as knowledge or sent out. The Ayinde
    court listed authoritative sources such as the national legislation database, the court-judgment archive, official
    law reports and databases of reputable legal publishers.
  outcomes:
  - lever: quality
    description: Hallucination rate of leading retrieval-based legal research tools in a preregistered test
    figure: Each of Lexis+ AI, Westlaw AI-Assisted Research and Ask Practical Law AI hallucinated "between 17% and
      33% of the time"; Lexis+ AI answered 65% of queries accurately
    measures: Share of responses judged hallucinated, and (Lexis+ AI) share of queries answered accurately, in a
      preregistered evaluation of over 200 legal queries (preprint dated 30 May 2024, updated 3 June 2024); tools
      tested are commercial research products, not internal knowledge bases
    provenance: independent
    source_ref: STANFORD-MAGESH-2024
  - lever: quality
    description: Document question-answering accuracy against a lawyer baseline
    figure: 'Document Q&A scores: Lawyer Baseline 70.1; Harvey Assistant 94.8; CoCounsel 89.6; Vincent AI 72.7;
      Oliver 74.0'
    measures: Accuracy or performance score under predefined criteria on the Document Q&A task of the Vals Legal
      AI Report (vendors opted in by task; one-document Q&A, not firm-wide search)
    provenance: independent
    source_ref: VALS-VLAIR-2025
  - lever: risk
    description: Court decisions addressing hallucinated AI content
    figure: 2,202 cases identified so far in the database
    measures: Number of legal decisions worldwide in which the court addressed AI use in more than a passing reference,
      mainly where it found or implied reliance on hallucinated content (some are alleged and unconfirmed), as logged
      by the database maintainer on the day it was read
    provenance: independent
    source_ref: CHARLOTIN-DB-2026
  - lever: risk
    description: Refund after an AI-assisted consulting report contained fabricated references
    figure: Deloitte Australia agreed to repay the final instalment of an AUD 440,000 contract
    measures: Amount paid by the Australian government for a 237-page report; refund amount to be made public (Associated
      Press)
    provenance: independent
    source_ref: CTV-DELOITTE-2025
  prerequisites:
  - Access to authoritative sources and citators
  - A written verification standard by task type and risk
  - Source-linked answers so a checker can open the underlying text
  risks_and_guardrails:
  - A lawyer who relies on AI research has a professional duty to check it against authoritative sources, and the
    duty also covers relying on others' AI-assisted work, like relying on a trainee (JUDICIARY-AYINDE-2025, paras
    7-8)
  - The court said leaders such as managing partners must take practical and effective measures so everyone using
    AI understands their duties, and that it may ask in future hearings whether those leadership duties were met
    (JUDICIARY-AYINDE-2025, para 9)
  - The California guidance says competence includes reviewing, verifying and correcting AI outputs and that tools
    can project confidence (CALBAR-GENAI-2026, pp. 2 and 4)
  - For a task selected to be outside the AI frontier, consultants using AI were 19% less likely to produce correct
    solutions than those without AI (HBS-DELLACQUA-2023, abstract)
  - NIST names confabulation as a generative-AI risk (NIST-AI600-2024, section 2.2)
  human_checkpoints:
  - Named reviewer verifies every citation and quotation against an authoritative source
  - KM validates an entry before it is added to a precedent or answer bank
  - Sampling checks on high-volume output, where full review is not practical
  role_evolution: Verification becomes an explicit, auditable duty for individuals and for firm leaders (JUDICIARY-AYINDE-2025,
    para 9). The Law Society reports teams experimenting with statistical sampling in place of manual review of
    large-scale document and contract review models, which it calls a significant departure from existing professional
    assumptions (LAWSOC-AGENTIC-2026).
  evidence_grade: B
  sources:
  - ref: STANFORD-MAGESH-2024
    title: Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362)
    publisher: Stanford University and Yale University (Magesh, Surani, Dahl, Suzgun, Manning, Ho)
    type: academic
    url: https://arxiv.org/abs/2405.20362
    date: '2024-05-30'
    access: full
    locator: Abstract (p. 1) and Introduction (p. 2)
  - ref: VALS-VLAIR-2025
    title: Vals Legal AI Report (VLAIR)
    publisher: Vals AI, with Legaltech Hub
    type: survey
    url: https://www.vals.ai/vlair
    date: '2025-02-27'
    access: full
    locator: Executive summary results table, Document Q&A row
  - ref: CHARLOTIN-DB-2026
    title: AI Hallucination Cases Database (read 19 Oct 2026)
    publisher: Damien Charlotin
    type: academic
    url: https://www.damiencharlotin.com/hallucinations/
    date: '2026-10-19'
    access: full
    locator: Database header (count as of read date)
  - ref: JUDICIARY-AYINDE-2025
    title: Ayinde v London Borough of Haringey and Al-Haroun v Qatar National Bank, [2025] EWHC 1383 (Admin) (Divisional
      Court judgment)
    publisher: Courts and Tribunals Judiciary of England and Wales
    type: regulator
    url: https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf
    date: '2025-06-06'
    access: full
    locator: Paras 4-9
  - ref: CTV-DELOITTE-2025
    title: Deloitte to partially refund Australian government for report with apparent AI-generated errors (Associated
      Press via CTV News)
    publisher: Associated Press / CTV News
    type: press
    url: https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/
    date: '2025-10-07'
    access: full
    locator: Article body
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision,
      replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Executive summary p. 2; Competence row p. 4
  - ref: HBS-DELLACQUA-2023
    title: Navigating the Jagged Technological Frontier (HBS Working Paper 24-013)
    publisher: Harvard Business School
    type: academic
    url: https://www.hbs.edu/faculty/Pages/item.aspx?num=64700
    date: 2023-09
    access: full
    locator: Abstract
  - ref: NIST-AI600-2024
    title: 'Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST
      AI 600-1)'
    publisher: National Institute of Standards and Technology
    type: standard-setter
    url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
    date: 2024-07
    access: full
    locator: Section 2.2 Confabulation
  - ref: LAWSOC-AGENTIC-2026
    title: The future of agentic AI in legal practice (report summary page)
    publisher: The Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice
    date: '2026-04-14'
    access: full
    locator: Section "Governance and oversight are changing"
  last_reviewed: '2026-10-19'
  notes: 'Grade capped at B: the independent measurements (Stanford 2024, Vals 2025) test commercial legal research
    and document Q&A products, which are adjacent to internal precedent and knowledge-base search. No published
    error, override or parallel-run figures were found for firm-internal knowledge bases. The Stanford test dates
    from 2024 and the vendor products have changed since. Deloitte did not say whether AI generated the errors when
    asked; the revised report disclosed use of Azure OpenAI.'
- id: professional-services-knowledge-management-05
  title: Firm-built test sets to evaluate knowledge and Q&A assistants before rollout and after model changes
  archetype: professional-services
  module: knowledge-management
  function: technology-it
  work_types:
  - review-assurance
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: Buyers cannot tell which assistants suit their work. The Vals report says the only way to find qualitative
    differences has been resource-intensive pilots, and that earlier benchmarks drew controversy over methodology.
    Models also change after purchase.
  solution: Firms contribute real questions, reference documents and ideal answers with indicia of correctness,
    set by lawyers of the right seniority, and use them to score tools. In the Vals study the consortium firms built
    the dataset that Vals AI then used to score vendor tools against a lawyer baseline. The same kind of set can
    be re-run when a model or product changes.
  outcomes:
  - lever: quality
    description: Size of the firm-contributed benchmark dataset
    figure: Over 500 samples across all tasks, primarily from Am Law 100 firms
    measures: Question-and-answer sets with indicia of correctness collected from the consortium firms for the Vals
      Legal AI Report
    provenance: independent
    source_ref: VALS-VLAIR-2025
  prerequisites:
  - Senior lawyers' time to write reference answers and correctness criteria
  - A governed copy of non-confidential or sanitised source documents
  - A schedule to re-run tests when models or products change
  risks_and_guardrails:
  - Vendors could opt out of individual tasks (LexisNexis withdrew from all but legal research; Harvey withdrew
    from EDGAR research), which limits comparability (VALS-VLAIR-2025, methodology)
  - Vals AI states it has a customer relationship with one or more of the participants (VALS-VLAIR-2025, acknowledgments)
  - The report calls itself a snapshot that must be repeated (VALS-VLAIR-2025, introduction)
  - The California guidance says competence includes periodic reassessment as AI systems change through updates
    or model changes (CALBAR-GENAI-2026, p. 5)
  - The Law Society tells firms to assess the evidence and benchmarks vendors use to demonstrate capabilities (LAWSOC-GENAI-2026,
    lifecycle considerations)
  human_checkpoints:
  - Senior lawyers set and approve gold answers
  - A named owner signs off on pass marks before go-live and after material model changes
  role_evolution: Evaluation becomes a standing KM and innovation task. The EDRM preview of Legalweek 2026 counted
    at least 14 sessions on validation and measurement, and ILTACON 2026 included an AI validation session (EDRM-LEGALWEEK-2026;
    EDISCOVERYTODAY-ILTACON-2026).
  evidence_grade: B
  sources:
  - ref: VALS-VLAIR-2025
    title: Vals Legal AI Report (VLAIR)
    publisher: Vals AI, with Legaltech Hub
    type: survey
    url: https://www.vals.ai/vlair
    date: '2025-02-27'
    access: full
    locator: 'Introduction, Methodology and Acknowledgments (consortium firms named: Reed Smith, Fisher Phillips,
      McDermott Will & Emery, Ogletree Deakins, plus four anonymous firms)'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision,
      replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Duties of Competence and Diligence row, p. 5
  - ref: LAWSOC-GENAI-2026
    title: 'Generative AI: the essentials (page undated; cites events up to April 2026)'
    publisher: The Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials
    date: '2026'
    access: full
    locator: Lifecycle considerations section
  - ref: EDRM-LEGALWEEK-2026
    title: 'Legalweek 2026: (Select) Educational Sessions Preview (session titles listed before the event)'
    publisher: EDRM (Gina Taranto)
    type: conference
    url: https://edrm.net/2026/03/legalweek-2026-select-educational-sessions-preview/
    date: '2026-03-06'
    access: full
    locator: Section "Validation and Measurement" (sessions listed before the event)
  - ref: EDISCOVERYTODAY-ILTACON-2026
    title: My Five ILTACON 2026 Takeaways
    publisher: eDiscovery Today (Doug Austin)
    type: press
    url: https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/
    date: '2026-09-04'
    access: full
    locator: Takeaway on AI validation session and "context"
  last_reviewed: '2026-10-19'
  notes: 'Grade B: named firms took part in an independent benchmark, but no firm has published results of its own
    internal evaluation of a knowledge assistant. The Vals tasks are document tasks, adjacent to knowledge retrieval.
    The Vals report said a separate legal research study would be released later in 2025; it was not located.'
- id: professional-services-knowledge-management-06
  title: 'Governed rollout of AI for knowledge work: approved tools, policy, training before access and human-review
    rules'
  archetype: professional-services
  module: knowledge-management
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Staff turn to public AI tools when sanctioned tools are missing or weak. Thomson Reuters reports 34%
    of professionals use AI their organisation has not sanctioned, and iManage reports policy violations and shadow
    use, which puts client material outside firm controls (and, as the Heppner ruling shows, outside privilege).
  solution: Firms replace ad hoc use with a published policy, an approved-tool list, training required before access,
    rules for human review and verification, and client-approval rules. Smaller firms lag larger ones on every control
    in the ILTA data.
  outcomes:
  - lever: risk
    description: Share of firms with a formal GenAI policy, by firm size
    figure: 57% (under 50 lawyers); 80% (50-149); 85% (150-349); 98% (350-699); 91% (over 700)
    measures: Share of responding firms in each size band selecting "A formal policy is in place" at ILTA survey
      Q3.18 (508 firms overall)
    provenance: independent
    source_ref: ILTA-TECHSURVEY-2026
  - lever: risk
    description: Share of firms requiring training before use, by firm size
    figure: 11% (under 50); 30%; 47%; 63%; 72% (over 700)
    measures: Share of responding firms in each size band selecting "Specific training required before use" at Q3.18
    provenance: independent
    source_ref: ILTA-TECHSURVEY-2026
  - lever: risk
    description: Share of firms requiring client approval, by firm size
    figure: 8% (under 50); 20%; 24%; 38%; 34% (over 700)
    measures: Share of responding firms in each size band selecting "Must obtain client approval" at Q3.18
    provenance: independent
    source_ref: ILTA-TECHSURVEY-2026
  - lever: risk
    description: Unsanctioned AI use
    figure: 34% of professionals use AI tools their organisation has not sanctioned
    measures: Share of 1,816 surveyed professionals admitting to unsanctioned use, per Thomson Reuters (Mar-Apr
      2026)
    provenance: vendor-published
    source_ref: TR-FOP-2026
  - lever: risk
    description: Policy violations and public-tool use
    figure: 36% have experienced a policy violation; 25% say end users use public AI with little oversight
    measures: Shares of respondents in iManage's survey of over 3000 business and technical decision makers (as
      worded on the iManage summary page)
    provenance: vendor-published
    source_ref: IMANAGE-BENCH-2026
  prerequisites:
  - An inventory of AI tools, including AI features switched on inside existing products (ILTA notes Copilot and
    Teams Premium deployments tripled in two years)
  - A sanctioned tool that is good enough to displace public tools
  - Training content, and an owner for policy updates
  risks_and_guardrails:
  - Managerial lawyers should set clear AI policies, give training, and update policies and controls as tools become
    more autonomous (CALBAR-GENAI-2026, p. 7)
  - The proposed California rule amendments would add comments saying managerial lawyers must make reasonable efforts
    to set internal AI policies (CALBAR-RULES-2026; a proposal, adoption not confirmed)
  - The Bar Standards Board guidance lists ensuring IT systems and data governance are properly implemented among
    its good-practice principles (BSB-AIGUIDANCE-2026)
  - In the Heppner ruling a court held a defendant's self-directed chats with a public AI tool were not privileged;
    Goodwin recommends an acceptable-use policy, approved tools and enterprise deployments (GOODWIN-HEPPNER-2026)
  - The EU AI Act's AI-literacy obligations applied from 2 Feb 2025 (EC-AIACT-2026, application timeline)
  human_checkpoints:
  - Partner or practice-group sign-off on tools used for client work where the policy requires it
  - Periodic review of the approved-tool list and policy
  role_evolution: 'Court and regulators place accountability on leaders: managing partners are expected to show
    that staff understand and comply with AI duties (JUDICIARY-AYINDE-2025, para 9). ILTA says firms expect added
    headcount in IT, innovation, security, training and knowledge management (ILTA-TECHSURVEY-2026, p. 5).'
  evidence_grade: C
  sources:
  - ref: ILTA-TECHSURVEY-2026
    title: '2026 ILTA Technology Survey: Executive Summary (PDF carries no printed date)'
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: '2026'
    access: full
    locator: p. 5 Q3.18 table; p. 4 Copilot paragraph
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: Key finding 03 and "Shadow AI" section
  - ref: IMANAGE-BENCH-2026
    title: iManage Knowledge Work Benchmark Report 2026 (headline and executive-summary page; full report not read)
    publisher: iManage
    type: survey
    url: https://imanage.com/benchmark-report-2026/
    date: '2026'
    access: full
    locator: Headline figures and "Governance & Risk" paragraph
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision,
      replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Duty to Supervise row, p. 7
  - ref: CALBAR-RULES-2026
    title: Proposed Amendments to the Rules of Professional Conduct Related to Artificial Intelligence (public comment
      page; COPRAC approved the proposal for comment on 13 Mar 2026; comment deadline 4 May 2026)
    publisher: State Bar of California
    type: regulator
    url: https://www.calbar.ca.gov/public/public-meetings-comment/public-comment/public-comment-archives/2026-public-comment/proposed-amendments-rules-professional-conduct-related-artificial-intelligence
    date: '2026-03-13'
    access: full
    locator: Amendments to rule 5.1 (proposed)
  - ref: BSB-AIGUIDANCE-2026
    title: New guidance supports barristers to safely adopt Artificial Intelligence and emerging technologies (press
      release)
    publisher: Bar Standards Board
    type: regulator
    url: https://www.barstandardsboard.org.uk/resources/new-guidance-supports-barristers-to-safely-adopt-artificial-intelligence-and-emerging-technologies.html
    date: '2026-05-18'
    access: full
    locator: Good-practice principles list
  - ref: GOODWIN-HEPPNER-2026
    title: 'AI Chatbots, Privilege, and Pitfalls: Lessons for Keeping Generative AI Exchanges Out of the Hands of
      Legal Adversaries (client alert on United States v. Heppner, S.D.N.Y.)'
    publisher: Goodwin Procter LLP
    type: firm
    url: https://www.goodwinlaw.com/en/insights/publications/2026/03/alerts-practices-ai-chatbots-privilege-and-pitfalls
    date: '2026-03-03'
    access: full
    locator: Sections "Attorney-Client Privilege" and "Recommendations"
  - ref: EC-AIACT-2026
    title: AI Act (regulatory framework page; read 19 Oct 2026)
    publisher: European Commission, Shaping Europe's digital future
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: Application timeline
  - ref: JUDICIARY-AYINDE-2025
    title: Ayinde v London Borough of Haringey and Al-Haroun v Qatar National Bank, [2025] EWHC 1383 (Admin) (Divisional
      Court judgment)
    publisher: Courts and Tribunals Judiciary of England and Wales
    type: regulator
    url: https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf
    date: '2025-06-06'
    access: full
    locator: Para 9
  last_reviewed: '2026-10-19'
  notes: Evidence is survey prevalence of controls, not outcomes of the controls (no incident-rate comparison between
    governed and ungoverned firms was found). Grade C because the figures come from surveys without named deployments.
    The iManage and Thomson Reuters surveys are published by vendors; ILTA is the member body.
- id: professional-services-knowledge-management-07
  title: AI expertise location from work product, matter data and outcome records, within data-protection limits
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - data-reporting
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Finding who has done similar work still relies on personal networks. ILTA says knowledge infrastructure
    is underdeveloped in expertise management, and Kantata's commissioned study finds skills, outcome and capacity
    data fragmented.
  solution: An assistant answers "who has done this before?" using matter data, document metadata and recorded outcomes.
    iManage describes its index as connecting firm content with matter data, expertise and curated collections.
  outcomes:
  - lever: quality
    description: Data barriers to outcome-aware expertise matching (resource managers, vendor-commissioned)
    figure: 47% cite poor or fragmented data across skills, outcomes, demand and capacity; only 7.3% say outcome
      data is easily accessible and routinely used in staffing; 24.6% say outcomes are not available to resource
      management at all
    measures: Shares of respondents to the Resource Management Institute study commissioned by Kantata (resource-management,
      not KM, respondents)
    provenance: vendor-published
    source_ref: KANTATA-RMI-2026
  prerequisites:
  - Clean matter, skills and outcome data
  - A lawful basis and transparency to staff for using their work records
  - Rules separating expertise search from performance evaluation
  risks_and_guardrails:
  - Under the EU AI Act, AI tools for employment and management of workers are listed as high-risk use cases; obligations
    for Annex III uses run from 2 December 2027 after the AI Omnibus extension (EC-AIACT-2026)
  - The California guidance warns that AI in employment actions or screening may present a risk of unlawful or unethical
    bias and says firms should set policies to identify bias (CALBAR-GENAI-2026, p. 9)
  - The UK ICO's guidance on AI and data protection (updated 15 March 2023) is flagged as under review following
    the Data (Use and Access) Act (ICO-AIDP-2023)
  human_checkpoints:
  - A person decides on staffing; the tool only suggests names
  - Staff can correct their own expertise profiles
  role_evolution: KM, resourcing and HR data owners share responsibility for profile data. Kantata's study found
    only 4% of resource managers feel well equipped to manage hybrid teams of people and agents (KANTATA-RMI-2026).
  evidence_grade: C
  sources:
  - ref: ILTA-TECHSURVEY-2026
    title: '2026 ILTA Technology Survey: Executive Summary (PDF carries no printed date)'
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: '2026'
    access: full
    locator: p. 9 (expertise management underdeveloped)
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at Strategic Crossroads (Resource Management Institute study "Resource
      Management in the Age of AI", commissioned by Kantata; updated 16 Sep 2026)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Study findings paragraphs on barriers and outcome data
  - ref: IMANAGE-INSIGHT-2026
    title: 'iManage Insight+: Discover institutional knowledge (product page; read 19 Oct 2026)'
    publisher: iManage
    type: vendor
    url: https://imanage.com/imanage-products/knowledge-search-management/insightplus/
    date: '2026-10-19'
    access: full
    locator: Section "Elevating knowledge work across law firms"
  - ref: EC-AIACT-2026
    title: AI Act (regulatory framework page; read 19 Oct 2026)
    publisher: European Commission, Shaping Europe's digital future
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: High-risk list and application timeline
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision,
      replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Prohibition on Discrimination row, p. 9
  - ref: ICO-AIDP-2023
    title: Guidance on AI and data protection (page notes update of 15 March 2023 and that the guidance is under
      review)
    publisher: UK Information Commissioner's Office
    type: regulator
    url: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/
    date: '2023-03-15'
    access: full
    locator: Page header notice
  last_reviewed: '2026-10-19'
  notes: No named firm was found describing AI expertise location with results. Kantata also lists an Expertise
    Agent (landscape lead; product page not opened by this analyst). The Kantata figures describe resource-management
    practice and cap the evidence at C.
- id: professional-services-knowledge-management-08
  title: AI-drafted engagement retrospectives and lessons learned filed to a searchable knowledge base
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - document-production
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: Lessons from finished engagements rarely reach the next team because writing them up is unpaid extra
    work at project close.
  solution: An agent drafts the retrospective from project records and files lessons learned into a searchable firm
    knowledge base, for a project manager to review. Certinia lists a Retrospective Drafter Agent and a Knowledge
    Base Agent in its Veda catalogue, and Kantata's Converge conference (scheduled for 17 November 2026) includes
    capturing and preserving critical expertise in its agenda questions.
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: No time-saved or reuse figures found
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Structured project records (scope, risks, issues, outcomes)
  - A sanitisation step so client-identifying and confidential detail does not enter a firm-wide base
  - An owner who reviews and prunes the base
  risks_and_guardrails:
  - A NYC Bar opinion says that even with consent a lawyer should avoid entering details that can be used to identify
    the client (NYCBAR-OP2024-5-2024, p. 2)
  - Shared knowledge bases that mix clients can breach ethical walls (NYCBAR-OP2024-5-2024, pp. 3-4)
  - Plausible but wrong lessons, once filed, are reused; verification applies (CALBAR-GENAI-2026, p. 4)
  human_checkpoints:
  - Project manager and a responsible partner approve the retrospective before filing
  - KM team reviews entries for client-identifying detail
  role_evolution: Project managers and KM staff move from writing to reviewing and curating lessons (vendor description,
    CERTINIA-VEDA-2026).
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (product page; read 19 Oct 2026)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: Agent catalogue entries "Retrospective Drafter Agent" and "Knowledge Base Agent"; "Value capture &
      knowledge transfer"
  - ref: KANTATA-CONVERGE-2026
    title: 'Kantata Announces Kantata Converge: November 17, 2026'
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/kantata-converge-where-ai-meets-expertise
    date: '2026-10-08'
    access: full
    locator: Press release paragraph on capturing and preserving critical expertise (event scheduled for 2026-11-17)
  - ref: NYCBAR-OP2024-5-2024
    title: 'Formal Opinion 2024-5: Ethical Obligations of Lawyers and Law Firms Relating to the Use of Generative
      Artificial Intelligence in the Practice of Law'
    publisher: New York City Bar Association, Professional Ethics Committee
    type: professional-body
    url: https://www.nycbar.org/wp-content/uploads/2024/08/20221329_GenerativeAILawPractice.pdf
    date: '2024-08-07'
    access: full
    locator: Duty of Confidentiality and Conflicts rows, pp. 2-4
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision,
      replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Competence row, p. 4
  last_reviewed: '2026-10-19'
  notes: 'Product catalogue and a scheduled conference only; no customer use or measured result was found. The Certinia
    page has no publication date (date shown is the day it was read). Pattern "other": a capture-to-knowledge-base
    drafting pipeline.'
- id: professional-services-knowledge-management-09
  title: AI transcription and summaries of calls and meetings as a source of knowledge capture
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - document-production
  - data-reporting
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Know-how stays in conversation. Meeting summaries could feed matter records and knowledge bases, but
    recording raises consent, confidentiality and tactical risks.
  solution: AI tools record, transcribe and summarise calls so notes and decisions can be filed to the matter or
    knowledge base. A vendor feature list describes transforming meeting conversations into clear summaries.
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: No time-saved or accuracy figures found for professional-services use
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Consent practice for all call participants
  - A rule on where transcripts and summaries are stored and how long they are kept
  - A decision on which summaries may enter shared knowledge
  risks_and_guardrails:
  - NYC Bar Formal Opinion 2026-2 (5 Aug 2026) says an attorney should obtain the consent of all other parties before
    recording, and that as a default the attorney should avoid recording absent good reason; it addresses conversations
    with people who are not clients (NYCBAR-OP2026-2-2026)
  - Confidential client information must not go into AI systems that share it with third parties without informed
    consent (NYCBAR-OP2024-5-2024, pp. 2-3)
  - Private chats with public AI tools were held not privileged in Heppner, so transcripts held in consumer tools
    may be discoverable (GOODWIN-HEPPNER-2026)
  human_checkpoints:
  - The lawyer decides in each instance whether to record at all
  - The lawyer checks a summary before it is filed or shared
  role_evolution: Fee earners decide per call whether to record; KM sets what can be filed. No role changes were
    reported in sources.
  evidence_grade: C
  sources:
  - ref: NYCBAR-OP2026-2-2026
    title: NYC Bar Association Releases Formal Opinion on Ethical Use of AI for Recording, Transcribing, and Summarizing
      Non-Client Conversations (press release for Formal Opinion 2026-2, dated 5 Aug 2026)
    publisher: New York City Bar Association
    type: professional-body
    url: https://www.nycbar.org/press-releases/nyc-bar-association-releases-formal-opinion-on-ethical-use-of-ai-for-recording-transcribing-and-summarizing-non-client-conversations/
    date: '2026-08-17'
    access: full
    locator: Press release text (opinion issued 2026-08-05, release dated 2026-08-17; opinion text not opened)
  - ref: NYCBAR-OP2024-5-2024
    title: 'Formal Opinion 2024-5: Ethical Obligations of Lawyers and Law Firms Relating to the Use of Generative
      Artificial Intelligence in the Practice of Law'
    publisher: New York City Bar Association, Professional Ethics Committee
    type: professional-body
    url: https://www.nycbar.org/wp-content/uploads/2024/08/20221329_GenerativeAILawPractice.pdf
    date: '2024-08-07'
    access: full
    locator: Duty of Confidentiality row, pp. 2-3
  - ref: GOODWIN-HEPPNER-2026
    title: 'AI Chatbots, Privilege, and Pitfalls: Lessons for Keeping Generative AI Exchanges Out of the Hands of
      Legal Adversaries (client alert on United States v. Heppner, S.D.N.Y.)'
    publisher: Goodwin Procter LLP
    type: firm
    url: https://www.goodwinlaw.com/en/insights/publications/2026/03/alerts-practices-ai-chatbots-privilege-and-pitfalls
    date: '2026-03-03'
    access: full
    locator: Section "Key Takeaways"
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (product page; read 19 Oct 2026)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: '"Frictionless operations & delivery" entry'
  last_reviewed: '2026-10-19'
  notes: The NYC Bar opinion covers non-client conversations; client calls are governed by the 2024 opinion. This
    entry is mainly a constraint on a common capture step. Only the press release for Opinion 2026-2 was read.
- id: professional-services-knowledge-management-10
  title: Purpose-built AI assistants for less experienced staff, with unaided skill checks to protect expertise
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - expert-judgment
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Senior judgement is the scarcest asset and is hard to pass on. Thomson Reuters finds 71% of professionals
    think early-career roles need structured support from experienced peers, and 48% worry about the effect on independent
    judgement.
  solution: A purpose-built assistant supports the work of less experienced staff, and the firm then checks what
    they can do without it. A pre-registered field experiment at eleven US IP firms tested this with a custom patent
    drafting assistant, measuring both quality with the tool and judgement afterwards without it. A separate study
    of customer-support agents found suggestive evidence that an assistant spreads the best practices of more able
    workers.
  outcomes:
  - lever: quality
    description: Work quality with AI assistance (patent drafting, blinded expert scoring)
    figure: +0.34 SD at 10 days and +0.38 SD at 90 days, with larger gains among junior lawyers
    measures: Standard deviations of blinded expert quality scores, treated versus control lawyers, on benchmark
      patent drafting tasks; pre-registered randomised trial of 133 practising patent lawyers at 11 US IP firms;
      study conducted by Google with the assistant it supplied
    provenance: independent
    source_ref: NBER-AUTOR-2026
  - lever: quality
    description: Skill retained when working without AI after three months
    figure: Treated lawyers outperformed controls by 0.32 SD on a no-AI redline task; senior lawyers 0.45 SD; junior
      lawyers showed no average gain, with scores bifurcated
    measures: Standard deviations on a blinded-scored redline of an existing patent application done without AI
    provenance: independent
    source_ref: NBER-AUTOR-2026
  - lever: capacity
    description: Customer-support agents with a generative AI assistant (adjacent process)
    figure: +14% issues resolved per hour on average; +34% for novice and low-skilled workers; minimal impact on
      experienced workers
    measures: Issues resolved per hour, 5,179 customer support agents, staggered introduction (the paper gives suggestive
      evidence that the tool disseminates best practices of more able workers)
    provenance: independent
    source_ref: NBER-BRYNJOLFSSON-2023
  prerequisites:
  - A defined body of expert guidance (playbooks, checklists, model outputs) the assistant is built on
  - A way to test what juniors can do unaided
  - Structured mentoring (71% of professionals in the Thomson Reuters survey say early-career staff need it)
  risks_and_guardrails:
  - Foundational expertise may be a prerequisite for getting durable skill from AI-assisted practice (NBER-AUTOR-2026,
    abstract)
  - Thomson Reuters reports legal professionals expect the timeline to trusted judgement to stretch by nearly two
    years (TR-FOP-2026, finding 07)
  - The Law Society warns of invisible substitution of professional judgement and expects junior roles to change
    first (LAWSOC-AGENTIC-2026)
  human_checkpoints:
  - Senior review of junior work remains the main quality control
  - Periodic unaided exercises to check skills
  role_evolution: Seniors gained most from AI-assisted practice in the trial, and junior outcomes split (NBER-AUTOR-2026).
    Thomson Reuters finds 48% concerned about independent-judgement development and 45% about learning through experience
    (TR-FOP-2026).
  evidence_grade: B
  sources:
  - ref: NBER-AUTOR-2026
    title: Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent
      Drafting (NBER Working Paper 35720)
    publisher: NBER (Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere)
    type: academic
    url: https://www.nber.org/papers/w35720
    date: 2026-09
    access: full
    locator: Abstract (issue date September 2026, revised October 2026)
  - ref: NBER-BRYNJOLFSSON-2023
    title: Generative AI at Work (NBER Working Paper 31161)
    publisher: NBER (Brynjolfsson, Li, Raymond)
    type: academic
    url: https://www.nber.org/papers/w31161
    date: 2023-04
    access: full
    locator: Abstract
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: Key finding 07 and section "A generation of disrupted development"
  - ref: LAWSOC-AGENTIC-2026
    title: The future of agentic AI in legal practice (report summary page)
    publisher: The Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice
    date: '2026-04-14'
    access: full
    locator: Sections "Summary of key findings" and "Workforce and skills could be impacted"
  last_reviewed: '2026-10-19'
  notes: 'Grade capped at B: the measured outcomes come from adjacent processes (patent drafting, and customer support
    at an unnamed firm), not from knowledge capture or search. The patent study was conducted by Google and uses
    a Google-built tool; the authors acknowledge Google support. Talent development effects are routed to talent-learning.'
- id: professional-services-knowledge-management-11
  title: Firmwide AI knowledge assistant over a consulting firm's own intellectual property
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - research-synthesis
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: Consulting knowledge sits in decks, reports and expert heads; finding and synthesising it takes consultants
    days.
  solution: McKinsey's Lilli was rolled out firmwide in July 2023 to change how the firm accesses and synthesises
    its institutional knowledge, and Deloitte's PairD was launched for internal use in 2023, according to the Stanford
    Digital Economy Lab paper. Deployments are visible to the firm but largely invisible to the client, the paper
    says.
  outcomes:
  - lever: speed
    description: Reported time saving in searching and synthesising knowledge
    figure: Reportedly "up to 30 percent"
    measures: Time savings in searching and synthesising knowledge, reported by McKinsey (cited as McKinsey n.d.
      in the Stanford paper); no sample, baseline or method given
    provenance: self-reported
    source_ref: STANFORD-DEL-2026
  prerequisites:
  - A cleaned, access-controlled corpus of firm IP
  - Rules for client-confidential material in the corpus
  - Training and an owner for content quality
  risks_and_guardrails:
  - Deloitte Australia refunded part of an AUD 440,000 contract after a report with fabricated references and a
    misquoted judge; the revised report disclosed use of Azure OpenAI (CTV-DELOITTE-2025)
  - Brynjolfsson and Petropoulos argue internal AI augmentation can heighten information asymmetry between consultant
    and client even as efficiency improves (STANFORD-DEL-2026, abstract)
  - The MCA's 2026 survey foreword flags concern about the quality of training under hybrid working (MCA-SURVEY-2026)
  human_checkpoints:
  - Consultants verify facts and sources before they enter client deliverables
  - Engagement leaders sign off on deliverables
  role_evolution: No role-change evidence found for consultants. The Stanford paper notes AI telemetry could make
    once-tacit outcomes contractible (STANFORD-DEL-2026, section on measurement).
  evidence_grade: B
  sources:
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives'
    publisher: Stanford Digital Economy Lab (Brynjolfsson) and University of Southern California (Petropoulos)
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Section 5.1 "AI augmentation lowers input cost observability"; abstract
  - ref: CTV-DELOITTE-2025
    title: Deloitte to partially refund Australian government for report with apparent AI-generated errors (Associated
      Press via CTV News)
    publisher: Associated Press / CTV News
    type: press
    url: https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/
    date: '2025-10-07'
    access: full
    locator: Article body
  - ref: MCA-SURVEY-2026
    title: MCA Member Survey 2026 (foreword and overview)
    publisher: Management Consultancies Association
    type: professional-body
    url: https://www.mca.org.uk/reports/mca-member-survey-2026
    date: '2026-01-20'
    access: full
    locator: Foreword, paragraph on training
  last_reviewed: '2026-10-19'
  notes: The McKinsey primary page returned 403; the 30% figure is read second-hand in a full-access academic paper
    and is not independently verified (provenance self-reported). The Stanford lab disclosed a general gift from
    Accenture and interviews with Accenture executives. The landscape file carries other Lilli figures (500,000+
    prompts a month) from a snippet only; they are omitted here.
- id: professional-services-knowledge-management-12
  title: AI work product and prompts captured in the matter record under retention and privilege controls
  archetype: professional-services
  module: knowledge-management
  function: risk-compliance-legal
  work_types:
  - document-production
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Work done in public AI tools sits outside the firm record and may not be privileged. A US district court
    held that a defendant's self-directed chats with a public AI tool were protected by neither attorney-client
    privilege nor work product.
  solution: AI tools work through a governed gateway so every retrieval and every document written back is authenticated,
    permission-bound and logged, and AI-generated work product is filed in the official record with its metadata.
    The attorney directs and documents AI use on privileged work.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: No incident-rate or audit-time figures found; the vendor page describes logging as a feature
    provenance: vendor-published
    source_ref: IMANAGE-MCP-2026
  prerequisites:
  - Retention and disposition rules covering AI prompts and outputs
  - Enterprise AI tools with data-protection terms
  - Instruction for lawyers on when attorney direction must be documented
  risks_and_guardrails:
  - Heppner is a district court ruling on its facts; Goodwin advises attorney-directed, documented use, enterprise
    or private deployments, and vendor diligence (GOODWIN-HEPPNER-2026)
  - The Law Society's April 2026 report says agentic actions complicate assumptions about what is privileged and
    what must be disclosed (LAWSOC-AGENTIC-2026)
  - The NYSBA task force report includes a section on how attorney-client privilege and work product may be revealed
    through generative AI tools (NYSBA-TFAI-2024, section E)
  human_checkpoints:
  - Lawyer directs and documents AI use on privileged matters
  - Records manager confirms retention rules apply to AI outputs
  role_evolution: Records, KM and risk teams take on governance of AI interactions as part of the matter file. No
    role-change evidence found.
  evidence_grade: C
  sources:
  - ref: IMANAGE-MCP-2026
    title: Securely Connect to AI Tools with Model Context Protocol (product page; read 19 Oct 2026)
    publisher: iManage
    type: vendor
    url: https://imanage.com/imanage-products/the-imanage-platform/ai/model-context-protocol/
    date: '2026-10-19'
    access: full
    locator: Sections "Governed & auditable access" and "Read and write, both governed"
  - ref: GOODWIN-HEPPNER-2026
    title: 'AI Chatbots, Privilege, and Pitfalls: Lessons for Keeping Generative AI Exchanges Out of the Hands of
      Legal Adversaries (client alert on United States v. Heppner, S.D.N.Y.)'
    publisher: Goodwin Procter LLP
    type: firm
    url: https://www.goodwinlaw.com/en/insights/publications/2026/03/alerts-practices-ai-chatbots-privilege-and-pitfalls
    date: '2026-03-03'
    access: full
    locator: Sections "Attorney-Client Privilege", "Work Product Doctrine" and "Recommendations"
  - ref: LAWSOC-AGENTIC-2026
    title: The future of agentic AI in legal practice (report summary page)
    publisher: The Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice
    date: '2026-04-14'
    access: full
    locator: Section "Risks need urgent clarity"
  - ref: NYSBA-TFAI-2024
    title: Report and Recommendations of the New York State Bar Association Task Force on Artificial Intelligence
    publisher: New York State Bar Association
    type: professional-body
    url: https://nysba.org/wp-content/uploads/2022/03/2024-April-Report-and-Recommendations-of-the-Task-Force-on-Artificial-Intelligence.pdf
    date: 2024-04
    access: full
    locator: Section E, Attorney-Client Privilege and Attorney-Work Product
  last_reviewed: '2026-10-19'
  notes: A court ruling and vendor features; no firm describing its practice was found. Another court (a magistrate
    in a separate federal case) reportedly reached a different result on waiver, from a search summary only (not
    opened), so it is not relied on.
- id: professional-services-knowledge-management-13
  title: Agents with scoped, logged access to document systems and knowledge bases that file work and update metadata
  archetype: professional-services
  module: knowledge-management
  function: technology-it
  work_types:
  - coordination-scheduling
  - document-production
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Filing documents, updating metadata and carrying matter context between steps are manual KM and admin
    tasks. Agents could do them but need access that is broad enough to be useful and narrow enough to be safe.
  solution: 'Agents act through a governed gateway under the same permissions, ethical walls and audit logging as
    a person: iManage says its MCP server lets AI draft documents, file them in the right workspace and update metadata.
    Harvey''s Legal Work Orchestration lets agents execute defined tasks while lawyers review at designated gates.'
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: No results published; both sources are product announcements
    provenance: vendor-published
    source_ref: IMANAGE-MCP-2026
  prerequisites:
  - Agent identities with least-privilege rights
  - Review gates defined per task
  - Audit logs reviewed by a named owner
  risks_and_guardrails:
  - Agentic systems connected to email, document systems and knowledge bases may disclose confidential information
    across matters; lawyers must not allow autonomous external transmission of client information without safeguards
    and human review (CALBAR-GENAI-2026, pp. 5-6)
  - The more autonomous the system, the more oversight is needed (CALBAR-GENAI-2026, pp. 3-4)
  - The Law Society's April 2026 report says solicitors remain responsible for agentic outputs they cannot fully
    audit, and errors may repeat across matters (LAWSOC-AGENTIC-2026)
  - The Law Society's guidance page reports that the April 2026 report found no evidence that agentic AI is currently
    used in legal practice (LAWSOC-GENAI-2026)
  human_checkpoints:
  - Lawyer review at each designated gate before the next task starts
  - Periodic review of agent permissions and logs
  role_evolution: KM and legal-technology staff become owners of agent permissions and templates (HARVEY-ORCH-2026).
    Cal Bar says supervision must correspond to the level of access and autonomy (CALBAR-GENAI-2026, p. 5).
  evidence_grade: C
  sources:
  - ref: IMANAGE-MCP-2026
    title: Securely Connect to AI Tools with Model Context Protocol (product page; read 19 Oct 2026)
    publisher: iManage
    type: vendor
    url: https://imanage.com/imanage-products/the-imanage-platform/ai/model-context-protocol/
    date: '2026-10-19'
    access: full
    locator: Section "Read and write, both governed"
  - ref: HARVEY-ORCH-2026
    title: Making Harvey the Orchestration Layer for Legal Work
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/legal-work-orchestration
    date: '2026-10-15'
    access: full
    locator: Introduction and "Keep Reviews and Next Steps Moving" (launch post 2026-10-15)
  - ref: LEGORA-IMANAGE-2026
    title: Legora and iManage deepen integration through iManage MCP Server (press release)
    publisher: Legora
    type: vendor
    url: https://legora.com/newsroom/legora-and-imanage-deepen-integration-through-imanage-mcp-server
    date: '2026-10-16'
    access: full
    locator: Paragraph on workflows
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision,
      replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Executive summary pp. 2-3; Duty of Confidentiality row pp. 5-6
  - ref: LAWSOC-AGENTIC-2026
    title: The future of agentic AI in legal practice (report summary page)
    publisher: The Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice
    date: '2026-04-14'
    access: full
    locator: Sections "Accountability frameworks do not yet fit autonomous systems" and "Risks need urgent clarity"
  - ref: LAWSOC-GENAI-2026
    title: 'Generative AI: the essentials (page undated; cites events up to April 2026)'
    publisher: The Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials
    date: '2026'
    access: full
    locator: Agentic AI paragraph
  last_reviewed: '2026-10-19'
  notes: Announced products only. The Law Society finding of no current evidence of agentic AI in legal practice
    is quoted from its guidance page, not from the report itself.
- id: professional-services-knowledge-management-14
  title: Reuse and value analytics for knowledge assets and AI use at matter level
  archetype: professional-services
  module: knowledge-management
  function: strategy-planning
  work_types:
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Firms spend more on knowledge management and AI but cannot show returns. APQC says KM impact is difficult
    to measure for many organisations, and at Legalweek 2026 firms answering clients' savings questions often said
    they were still gathering data.
  solution: Usage and reuse telemetry on knowledge assets and AI tools is joined to matter and financial data. iManage
    describes an index that reveals trends across matters, clients, jurisdictions and profitability.
  outcomes:
  - lever: capacity
    description: Law firm spending on knowledge management
    figure: KM investment up nearly 10% in 2025; up 37.2% from 2021 to 2025
    measures: Growth in law firm investment in knowledge management, per Thomson Reuters Institute and Georgetown
      Law Center on Ethics and the Legal Profession market data
    provenance: vendor-published
    source_ref: TRI-SOTLM-2026
  - lever: quality
    description: Measurable benefit from AI among architecture and engineering firms (adjacent field)
    figure: Only 38% reported measurable positive business impact tied to AI use
    measures: Share of respondents to Deltek's Clarity A&E study reporting measurable positive impact (A&E firms,
      not law or consulting)
    provenance: vendor-published
    source_ref: DELTEK-CLARITY-2026
  prerequisites:
  - Instrumented knowledge tools with usage logs
  - Matter and billing data linkable to tool usage
  - Agreement with clients on what AI-savings evidence they will accept
  risks_and_guardrails:
  - The Stanford paper warns that behavioural visibility can erode the validity of metrics once people know they
    are metered (STANFORD-DEL-2026, section on trace data and measurement)
  human_checkpoints:
  - KM and finance leaders agree metric definitions
  - Metrics reviewed before they are shown to clients
  role_evolution: KM leaders are asked to link measures to efficiency, productivity, decision quality and reduced
    rework (APQC-KMEXEC-2026).
  evidence_grade: C
  sources:
  - ref: APQC-KMEXEC-2026
    title: '2026 KM Priorities & Trends: Executive Summary'
    publisher: APQC
    type: survey
    url: https://www.apqc.org/resource-library/resource/2026-km-priorities-trends-executive-summary/html
    date: '2026-05-12'
    access: full
    locator: Section "How can KM leaders prove business value and impact?"
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: Sections on ROI measurement and "We're still gathering the data"
  - ref: TRI-SOTLM-2026
    title: 'Legal market report 2026 analysis: AI bubble risk (State of the US Legal Market 2026, with Georgetown
      Law Center on Ethics and the Legal Profession)'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble
    date: '2026-01-14'
    access: full
    locator: Paragraphs on technology and knowledge-management spend
  - ref: IMANAGE-INSIGHT-2026
    title: 'iManage Insight+: Discover institutional knowledge (product page; read 19 Oct 2026)'
    publisher: iManage
    type: vendor
    url: https://imanage.com/imanage-products/knowledge-search-management/insightplus/
    date: '2026-10-19'
    access: full
    locator: Section "Connecting your content with context"
  - ref: DELTEK-CLARITY-2026
    title: The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/
    date: '2026-05-12'
    access: full
    locator: A&E study paragraph
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives'
    publisher: Stanford Digital Economy Lab (Brynjolfsson) and University of Southern California (Petropoulos)
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Section discussing digital trace data and measurement
  last_reviewed: '2026-10-19'
  notes: Routed partly to firm-finance for AI ROI. The kept item here is KM-specific reuse measurement; no firm
    was found publishing reuse-rate or search-success metrics.
- id: professional-services-knowledge-management-15
  title: '[in-house] Legal operations as owner of governed AI knowledge reuse and outside-counsel AI transparency'
  archetype: professional-services
  module: knowledge-management
  function: risk-compliance-legal
  work_types:
  - research-synthesis
  - coordination-scheduling
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Corporate legal departments hold prior advice, playbooks and outside-counsel work across fragmented systems,
    while AI pressure from the business lands on legal operations.
  solution: Legal operations selects and governs AI tools, connects legal work product with matter and business
    data, and asks outside firms what AI they use and what it saves. The Thomson Reuters Institute reports legal
    ops is the default first line for AI pressure; GSK says it is learning from its outside firms how they use GenAI.
  outcomes:
  - lever: capacity
    description: Shift of strategic priority toward technology
    figure: Twice the portion of GCs name technology their top strategic priority this year
    measures: General counsel respondents to the Legal Department Operations Report 2026, as summarised by the Thomson
      Reuters Institute (exact base not captured)
    provenance: vendor-published
    source_ref: TRI-LDOR-2026
  prerequisites:
  - Legal ops with data, vendor and training capability
  - Outside counsel guidelines that address AI use and reporting
  - A governed home for prior advice and playbooks
  risks_and_guardrails:
  - 'Clients differ: some demand AI-driven savings and line-item AI transparency, others issue directives that firms
    cannot use AI without explicit permission (TRI-LEGALWEEK-2026)'
  - The Thomson Reuters Institute says in-house teams face quieter erosion of budget, headcount and influence if
    AI value is not delivered (TR-FOP-2026)
  human_checkpoints:
  - Legal ops and the GC approve tools and outside-counsel AI terms
  - Lawyers verify before relying on prior advice retrieved by AI
  role_evolution: Legal ops is described as becoming its own practice area and the nexus between legal, technology
    and business (TRI-LDOR-2026).
  evidence_grade: C
  sources:
  - ref: TRI-LDOR-2026
    title: 2026 Legal Department Operations Report
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/legal-department-operations-report-2026
    date: '2026-09-22'
    access: full
    locator: Key takeaways
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: Remarks by GSK's Hudock and DLA Piper's Blair
  - ref: EDRM-LEGALWEEK-2026
    title: 'Legalweek 2026: (Select) Educational Sessions Preview (session titles listed before the event)'
    publisher: EDRM (Gina Taranto)
    type: conference
    url: https://edrm.net/2026/03/legalweek-2026-select-educational-sessions-preview/
    date: '2026-03-06'
    access: full
    locator: 'Sessions "Trust is the Product: How Proven AI Governance Builds Lasting Value" and "Agentic Ops: Building
      a Self-Orchestrating Legal Department" (listed before the event)'
  - ref: IMANAGE-INSIGHT-2026
    title: 'iManage Insight+: Discover institutional knowledge (product page; read 19 Oct 2026)'
    publisher: iManage
    type: vendor
    url: https://imanage.com/imanage-products/knowledge-search-management/insightplus/
    date: '2026-10-19'
    access: full
    locator: Section "Supporting the realities of corporate legal teams"
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: Section 01 "Clients are already moving on"
  last_reviewed: '2026-10-19'
  notes: In-house. Evidence is thin for KM specifically; this entry mainly records the governance role of legal
    operations. No named in-house deployment with results was found.
```

## 3. Module notes

### Processes and key steps (work types)

- **Capture.** Matter-close debriefs, retrospectives, know-how notes, call and meeting notes. Work types: document-production, data-reporting. (Use cases 08, 09.)
- **Curate.** Select, sanitise, rate and retire precedents and collections; KM teams submit, enrich, publish, maintain and archive (IMANAGE-INSIGHT-2026, Curation toolset). Work type: review-assurance. (Use case 03.)
- **Index and secure.** Metadata, permissions, ethical walls, retention. Work types: data-reporting, software-systems. (Use cases 01, 12.)
- **Find.** Enterprise search, natural-language Q&A, expertise location. Work type: research-synthesis. (Use cases 01, 07.)
- **Reuse and adapt.** Draft from precedent, templates with playbooks and review gates. Work type: document-production. (Use case 02.)
- **Verify and advise.** KM lawyers and reviewers check answers; lawyers rely on them. Work types: review-assurance, expert-judgment. (Use cases 04, 10.)
- **Govern and measure.** Policy, training, evaluation, usage and value analytics. Work types: review-assurance, data-reporting. (Use cases 05, 06, 14.)

### Common pain points

- Knowledge infrastructure "remains dramatically underdeveloped across enterprise search, expertise management, pricing, procurement, and competitive intelligence" (ILTA-TECHSURVEY-2026, p. 9).
- KM programmes are early: 59% of 164 APQC participants place theirs in the two earliest maturity stages; the top-ranked threat is a culture that does not reward sharing and reuse (40% of 162) (APQC-KM-2026, key findings).
- AI exposes weaknesses in content quality, governance, taxonomy and ownership (APQC-KMEXEC-2026, "How is AI changing knowledge management in 2026?").
- Skills, outcome and capacity data are fragmented: 47% of resource managers cite poor or fragmented data (KANTATA-RMI-2026; vendor-commissioned, resource-management respondents).
- Unsanctioned tools fill the gap when sanctioned tools are missing: 41% of professionals who use AI lack tools built on verified professional content, and 34% use unsanctioned AI (TR-FOP-2026, key findings 01 and 03).

### Metrics and benchmarks (with what each measures and who published it)

| Figure | What it measures | Provenance | Ref and locator |
|---|---|---|---|
| 94% engaged with GenAI, up 14 points | Share of 508 responding firms using or exploring GenAI tools | independent (member body survey) | ILTA-TECHSURVEY-2026, p. 3 |
| 57% to 98% formal policy; 11% to 72% training before use; 8% to 38% client approval | Share of responding firms in each lawyer-count band, Q3.18 | independent | ILTA-TECHSURVEY-2026, p. 5 |
| 49% name AI top KM priority; 23% critical-knowledge mapping | Share of 164 survey participants naming each a top 2026 priority (data collected Nov 2025) | independent (non-profit benchmarker) | APQC-KM-2026 |
| 59% in two earliest maturity stages; 21% optimizing or innovating | Share of 164 participants by self-rated KM maturity | independent | APQC-KM-2026 |
| 40% culture does not incentivize sharing and reuse | Share of 162 respondents ranking it a threat to KM success | independent | APQC-KM-2026 |
| 85% at some stage of AI adoption; 36% policy violation; 25% public AI with little oversight; 20% security-driven adoption delays | Shares of respondents in a survey of over 3000 business and technical decision makers, cross-industry | vendor-published | IMANAGE-BENCH-2026 |
| 34% unsanctioned AI; 41% lack professional-grade tools; 96% / 94% / 90% want confidentiality / grounding / explainability | Shares of 1,816 professionals surveyed Mar-Apr 2026 (bases for the 96/94/90 figures not stated) | vendor-published | TR-FOP-2026, key findings and "The fiduciary standard" |
| Technology spend up nearly 11%, KM up nearly 10% in 2025; KM up 37.2% 2021 to 2025 | Law firm investment growth | vendor-published (TR Institute with Georgetown) | TRI-SOTLM-2026 |
| 17% to 33% hallucination in three retrieval-based legal research tools | Share of responses judged hallucinated, over 200 preregistered queries | independent | STANFORD-MAGESH-2024, abstract |
| Document Q&A: lawyer baseline 70.1; best AI tools 89.6 and 94.8 | Task accuracy score, Vals Legal AI Report | independent (vendors opted in) | VALS-VLAIR-2025, results table |
| +0.34 / +0.38 SD quality; +0.32 SD unaided redline (seniors 0.45, juniors no average gain) | Blinded expert scores, 133 patent lawyers, 11 firms | independent (conducted by Google) | NBER-AUTOR-2026, abstract |
| 7,137 workers at 66 firms: about two fewer hours on email per week for the 80% who used the tool; no shift detected in task mix | Randomised field experiment on a productivity assistant, cross-industry | independent | NBER-DILLON-2025, abstract |
| 38% report measurable positive impact from AI | A&E firms in Deltek's Clarity study | vendor-published | DELTEK-CLARITY-2026 |
| 43.6% of projects use AI (23.1% in 2025) | Share of projects at 245 professional services firms (SPI Research); the paid report was not read | independent analyst, landing page only | SPI-AI-2026 |
| 2,202 cases | Court decisions in the hallucination database, as of the read date | independent | CHARLOTIN-DB-2026 |

### Guardrails and regulatory points

- **Competence and verification.** California: competence requires reviewing, verifying and correcting AI outputs, and the more autonomous the system the more oversight is needed (CALBAR-GENAI-2026, pp. 4-5). The Board of Trustees approved the revision on 2026-05-14 (CALBAR-ETHICSTECH-2026). Proposed rule changes to 1.1, 1.4, 1.6, 3.3, 5.1 and 5.3 were put out for comment until 2026-05-04; adoption was not confirmed (CALBAR-RULES-2026). England and Wales: Ayinde paras 7-9 (JUDICIARY-AYINDE-2025).
- **Confidentiality and consent.** NYC Bar: no confidential client information into systems that share it with third parties without client consent; closed systems do not present that risk but must not expose information to colleagues behind an ethical wall (NYCBAR-OP2024-5-2024, pp. 2-3). Secondary summaries of ABA Formal Opinion 512 report an informed-consent requirement for self-learning tools, say boilerplate engagement-letter wording is not enough, and note risk of internal exposure; the original was not read (EZEL-ABA512-2024; ABA-OP512-2024 search-only). The Bar Council (Jan 2024) tells barristers to be extremely vigilant about sharing privileged or confidential information with an LLM (BARCOUNCIL-GENAI-2024). The Law Society says not to use client confidential or personal data to create templates or test a system (LAWSOC-GENAI-2026).
- **Ethical walls.** Where a system uses client information, the firm must make sure it applies required screens (NYCBAR-OP2024-5-2024, pp. 3-4).
- **Agentic access.** Systems with standing access to email, document systems and knowledge bases create acute confidentiality risk; scope and monitor access, and no autonomous external transmission of client information without safeguards and human review (CALBAR-GENAI-2026, pp. 5-6). The Law Society warns errors may repeat across matters (LAWSOC-AGENTIC-2026).
- **Supervision, policy and training.** Managerial lawyers should set clear AI policies and give training (CALBAR-GENAI-2026, p. 7); the BSB lists data governance among good-practice principles (BSB-AIGUIDANCE-2026, 2026-05-18); the EU AI Act's AI-literacy obligations applied from 2026-02-02 (EC-AIACT-2026).
- **Client instructions and communication.** Lawyers must follow client guidelines that restrict AI (CALBAR-GENAI-2026, p. 7). Only about one-third of embedded-AI partners have discussed AI with at least 60% of their clients (TRI-STANDOUT-2026, key takeaways).
- **Privilege and discoverability.** Heppner (S.D.N.Y., 2026-02-17): self-directed chats with a public AI tool were not privileged or work product; the ruling is one court's and Goodwin's advice is attorney-directed, documented use (GOODWIN-HEPPNER-2026). The NYSBA task force has a section on privilege and work product (NYSBA-TFAI-2024, section E).
- **Recording of calls.** NYC Bar Formal Op. 2026-2: consent of all parties; default is not to record non-client conversations absent good reason (NYCBAR-OP2026-2-2026).
- **Data protection and employment-related AI.** EU AI Act applicable from 2026-08-02; Annex III high-risk obligations (which include AI for employment and worker management) extended to 2027-12-02 (EC-AIACT-2026). The UK ICO's AI guidance (updated 2023-03-15) is under review (ICO-AIDP-2023).
- **Standards.** NIST AI 600-1 lists confabulation (2.2), data privacy (2.4) and intellectual property (2.10) among generative-AI risks (NIST-AI600-2024).
- **Third-party content rights.** The NYC Bar opinion notes claims that some generative AI tools infringe third-party intellectual property and says lawyers should keep abreast (NYCBAR-OP2024-5-2024, footnote 12). No ruling on licensed-content use inside internal knowledge bases was verified (see Gaps).

### Frontier signals (dated, sourced)

- **2026-10-16.** Legora announces that mutual customers of Legora and iManage "will be able to" reach governed iManage knowledge through the iManage MCP server, with iManage permissions determining what each user can retrieve (LEGORA-IMANAGE-2026).
- **2026-10-15.** Harvey launches Legal Work Orchestration: templates define phases, tasks, playbooks, agents and review gates; innovation and knowledge teams define the structure once (HARVEY-ORCH-2026).
- **2026-08-05 / 08-17.** NYC Bar issues Formal Opinion 2026-2 on AI recording and summarising of non-client conversations; the default is not to (NYCBAR-OP2026-2-2026).
- **2026-05-18.** Bar Standards Board publishes AI guidance for barristers, citing Ayinde (BSB-AIGUIDANCE-2026).
- **2026-05-14.** California Board of Trustees approves the revised guidance, extended to agentic AI (CALBAR-ETHICSTECH-2026; CALBAR-GENAI-2026).
- **2026-05-12.** APQC: incorporating AI is the top KM priority; programmes still maturing their governance and measurement (APQC-KMEXEC-2026).
- **2026-04-14.** Law Society report on agentic AI: accountability frameworks do not yet fit autonomous systems; sampling-based oversight is emerging (LAWSOC-AGENTIC-2026).
- **2026-03-06 (preview).** EDRM counts at least 14 Legalweek 2026 sessions touching validation and measurement and lists KM-specific sessions ("The New Data Reality: What Agentic AI Can Infer & What KM Must Still Control"; "Designing a Legal Data Ecosystem: KM, DMS, and LLMs in Harmony") (EDRM-LEGALWEEK-2026). Titles only; content was not read.
- **2026-02.** Heppner ruling (GOODWIN-HEPPNER-2026).
- **2026-09 / 10.** NBER 35720: AI raised quality, but durable skill gain concentrated in seniors (NBER-AUTOR-2026).
- **Scheduled: 2026-11-17.** Kantata Converge lists capturing and preserving critical expertise among its agenda questions (KANTATA-CONVERGE-2026). Announcement only; the sessions have not been given.
- **2026-08-02 and 2027-12-02.** EU AI Act dates (EC-AIACT-2026).

### Workforce and role effects

- Firms expect added headcount in IT, innovation, security, training, knowledge management and data science (ILTA-TECHSURVEY-2026, p. 5).
- KM teams become curators and stewards of what AI is grounded on (IMANAGE-INSIGHT-2026, Curation toolset) and template owners (HARVEY-ORCH-2026).
- Leaders carry accountability: the Ayinde court said it may ask whether leadership responsibilities were fulfilled (JUDICIARY-AYINDE-2025, para 9).
- Early-career development: 71% of professionals say early-career roles need structured support from experienced peers and 48% fear a negative effect on independent judgement (TR-FOP-2026, finding 07 and "A generation of disrupted development"); juniors' outcomes split in the patent trial (NBER-AUTOR-2026). Law Society expects junior roles to change first (LAWSOC-AGENTIC-2026).
- MCA's survey foreword flags concern about training quality under hybrid working (MCA-SURVEY-2026). Routed to talent-learning below.

### Objections and concerns practitioners raise

- Accuracy: retrieval does not remove hallucination (STANFORD-MAGESH-2024); "almost right" is not good enough for fiduciary-grade work (TR-FOP-2026, foreword).
- Accountability without auditability: solicitors remain responsible for outputs they cannot fully audit (LAWSOC-AGENTIC-2026).
- Governance lags deployment: GenAI arrives through collaboration tools without discrete deployment events (ILTA-TECHSURVEY-2026, p. 4); work-product governance still relies heavily on training and leadership pressure, with tracking and compliance tools used by fewer than one in five firms (ILTA-TECHSURVEY-2026, p. 9).
- Hype: an ILTA respondent said previous transformative innovations produced minimal change and "this hype, too, shall pass" (ILTA-TECHSURVEY-2026, p. 4).
- Clients: conflicting directives arrive in the same inbox (TRI-LEGALWEEK-2026); firms cannot yet prove savings.
- Investment risk: the TR Institute warns of an AI-bubble risk for firms that adopt AI mainly to justify higher rates (TRI-SOTLM-2026).

### Interview probes for an advisor

1. When your AI search or assistant answers a question, whose permissions does it run under, and how did you test that a lawyer behind an ethical wall cannot see material from that matter in the answer?
2. Which client contracts or outside counsel guidelines restrict or require AI use, and how does a matter team find that out before reusing that client's material?
3. When a wrong answer or a flawed precedent has been filed as knowledge, who owns the correction, and how would you find where it was reused?
4. What do you measure today about knowledge reuse and AI use (searches that succeed, rework avoided, matters where AI was used), and what evidence would a client or partner accept?
5. Where do people go when the sanctioned tool is not good enough, and how would you know?

## 4. Routed to other modules

- **quality-review.** Sampling-based validation of document and contract review models (LAWSOC-AGENTIC-2026); hallucination and verification evidence beyond knowledge use (STANFORD-MAGESH-2024, VALS-VLAIR-2025, JUDICIARY-AYINDE-2025, CTV-DELOITTE-2025). Used here only for knowledge answers.
- **billing-collections and firm-finance.** Client demands for AI line items and proof of savings (TRI-LEGALWEEK-2026); hourly billing must reflect time actually spent and general AI subscriptions are overhead (CALBAR-GENAI-2026, p. 8); AI ROI evidence (DELTEK-CLARITY-2026, SPI-AI-2026).
- **talent-learning.** Skill erosion and apprenticeship (NBER-AUTOR-2026; TR-FOP-2026 finding 07); MCA training concern (MCA-SURVEY-2026).
- **staffing-resourcing.** Outcome data and hybrid human-agent teams (KANTATA-RMI-2026); EU AI Act treatment of AI for worker management (EC-AIACT-2026).
- **acceptance-risk.** Ethical screens and conflicts when AI uses client information (NYCBAR-OP2024-5-2024, pp. 3-4); client AI instructions at intake.
- **scoping-pricing.** Consulting pricing and internal AI augmentation (STANFORD-DEL-2026).
- **assurance and tax archetypes.** Accounting-body AI guidance was not reached (see Gaps); audit procedures and tax technical work are out of scope here.

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ABA-OP512-2024 | Formal Opinion 512: Generative Artificial Intelligence Tools (original PDF blocked; only secondary summaries read) | American Bar Association | professional-body | https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf | 2024-07-29 | search-only |
| APQC-KM-2026 | 2026 Knowledge Management Priorities and Trends Survey Report (listing page with key findings) | APQC | survey | https://www.apqc.org/resource-library/resource-listing/2026-knowledge-management-priorities-and-trends-survey-report | 2026-01-07 | full |
| APQC-KMEXEC-2026 | 2026 KM Priorities & Trends: Executive Summary | APQC | survey | https://www.apqc.org/resource-library/resource/2026-km-priorities-trends-executive-summary/html | 2026-05-12 | full |
| BARCOUNCIL-GENAI-2024 | New guidance on generative AI for the Bar (press release) | The General Council of the Bar (Bar Council of England and Wales) | professional-body | https://www.barcouncil.org.uk/resource/new-guidance-on-generative-ai-for-the-bar.html | 2024-01-30 | full |
| BSB-AIGUIDANCE-2026 | New guidance supports barristers to safely adopt Artificial Intelligence and emerging technologies (press release) | Bar Standards Board | regulator | https://www.barstandardsboard.org.uk/resources/new-guidance-supports-barristers-to-safely-adopt-artificial-intelligence-and-emerging-technologies.html | 2026-05-18 | full |
| CALBAR-ETHICSTECH-2026 | Ethics & Technology Resources (page records Board of Trustees approval of the updated Practical Guidance on 14 May 2026) | State Bar of California | regulator | https://www.calbar.ca.gov/Attorneys/Conduct-Discipline/Ethics/Ethics-Technology-Resources | 2026-05-14 | full |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision, replaces the November 2023 version) | State Bar of California, Standing Committee on Professional Responsibility and Conduct | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05-14 | full |
| CALBAR-RULES-2026 | Proposed Amendments to the Rules of Professional Conduct Related to Artificial Intelligence (public comment page; COPRAC approved the proposal for comment on 13 Mar 2026; comment deadline 4 May 2026) | State Bar of California | regulator | https://www.calbar.ca.gov/public/public-meetings-comment/public-comment/public-comment-archives/2026-public-comment/proposed-amendments-rules-professional-conduct-related-artificial-intelligence | 2026-03-13 | full |
| CERTINIA-VEDA-2026 | Veda AI: System of Action for Professional Services (product page; read 19 Oct 2026) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10-19 | full |
| CHARLOTIN-DB-2026 | AI Hallucination Cases Database (read 19 Oct 2026) | Damien Charlotin | academic | https://www.damiencharlotin.com/hallucinations/ | 2026-10-19 | full |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors (Associated Press via CTV News) | Associated Press / CTV News | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 | full |
| DELTEK-CLARITY-2026 | The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain | Deltek | vendor | https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/ | 2026-05-12 | full |
| EC-AIACT-2026 | AI Act (regulatory framework page; read 19 Oct 2026) | European Commission, Shaping Europe's digital future | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-19 | full |
| EDISCOVERYTODAY-ILTACON-2026 | My Five ILTACON 2026 Takeaways | eDiscovery Today (Doug Austin) | press | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 | full |
| EDRM-LEGALWEEK-2026 | Legalweek 2026: (Select) Educational Sessions Preview (session titles listed before the event) | EDRM (Gina Taranto) | conference | https://edrm.net/2026/03/legalweek-2026-select-educational-sessions-preview/ | 2026-03-06 | full |
| EZEL-ABA512-2024 | ABA Formal Op. 512: Generative AI Tools (plain-English summary of the opinion) | Ezel | vendor | https://ezel.ai/ethics-opinions/aba/512-generative-ai-tools | 2024-07-29 | full |
| GOODWIN-HEPPNER-2026 | AI Chatbots, Privilege, and Pitfalls: Lessons for Keeping Generative AI Exchanges Out of the Hands of Legal Adversaries (client alert on United States v. Heppner, S.D.N.Y.) | Goodwin Procter LLP | firm | https://www.goodwinlaw.com/en/insights/publications/2026/03/alerts-practices-ai-chatbots-privilege-and-pitfalls | 2026-03-03 | full |
| HARVEY-ORCH-2026 | Making Harvey the Orchestration Layer for Legal Work | Harvey | vendor | https://www.harvey.ai/blog/legal-work-orchestration | 2026-10-15 | full |
| HBS-DELLACQUA-2023 | Navigating the Jagged Technological Frontier (HBS Working Paper 24-013) | Harvard Business School | academic | https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 | 2023-09 | full |
| ICO-AIDP-2023 | Guidance on AI and data protection (page notes update of 15 March 2023 and that the guidance is under review) | UK Information Commissioner's Office | regulator | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/ | 2023-03-15 | full |
| ILTA-TECHSURVEY-2026 | 2026 ILTA Technology Survey: Executive Summary (PDF carries no printed date) | International Legal Technology Association | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026 | full |
| IMANAGE-BENCH-2026 | iManage Knowledge Work Benchmark Report 2026 (headline and executive-summary page; full report not read) | iManage | survey | https://imanage.com/benchmark-report-2026/ | 2026 | full |
| IMANAGE-INSIGHT-2026 | iManage Insight+: Discover institutional knowledge (product page; read 19 Oct 2026) | iManage | vendor | https://imanage.com/imanage-products/knowledge-search-management/insightplus/ | 2026-10-19 | full |
| IMANAGE-MCP-2026 | Securely Connect to AI Tools with Model Context Protocol (product page; read 19 Oct 2026) | iManage | vendor | https://imanage.com/imanage-products/the-imanage-platform/ai/model-context-protocol/ | 2026-10-19 | full |
| JUDICIARY-AYINDE-2025 | Ayinde v London Borough of Haringey and Al-Haroun v Qatar National Bank, [2025] EWHC 1383 (Admin) (Divisional Court judgment) | Courts and Tribunals Judiciary of England and Wales | regulator | https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf | 2025-06-06 | full |
| KANTATA-CONVERGE-2026 | Kantata Announces Kantata Converge: November 17, 2026 | Kantata | vendor | https://www.kantata.com/blog/article/kantata-converge-where-ai-meets-expertise | 2026-10-08 | full |
| KANTATA-RMI-2026 | New Study Finds Resource Management at Strategic Crossroads (Resource Management Institute study "Resource Management in the Age of AI", commissioned by Kantata; updated 16 Sep 2026) | Kantata | vendor | https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services | 2026-04-09 | full |
| LAWSOC-AGENTIC-2026 | The future of agentic AI in legal practice (report summary page) | The Law Society of England and Wales | professional-body | https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice | 2026-04-14 | full |
| LAWSOC-GENAI-2026 | Generative AI: the essentials (page undated; cites events up to April 2026) | The Law Society of England and Wales | professional-body | https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials | 2026 | full |
| LEGORA-IMANAGE-2026 | Legora and iManage deepen integration through iManage MCP Server (press release) | Legora | vendor | https://legora.com/newsroom/legora-and-imanage-deepen-integration-through-imanage-mcp-server | 2026-10-16 | full |
| MCA-SURVEY-2026 | MCA Member Survey 2026 (foreword and overview) | Management Consultancies Association | professional-body | https://www.mca.org.uk/reports/mca-member-survey-2026 | 2026-01-20 | full |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER Working Paper 35720) | NBER (Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere) | academic | https://www.nber.org/papers/w35720 | 2026-09 | full |
| NBER-BRYNJOLFSSON-2023 | Generative AI at Work (NBER Working Paper 31161) | NBER (Brynjolfsson, Li, Raymond) | academic | https://www.nber.org/papers/w31161 | 2023-04 | full |
| NBER-DILLON-2025 | Shifting Work Patterns with Generative AI (NBER Working Paper 33795) | NBER (Dillon, Jaffe, Immorlica, Stanton) | academic | https://www.nber.org/papers/w33795 | 2025-05 | full |
| NIST-AI600-2024 | Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1) | National Institute of Standards and Technology | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | 2024-07 | full |
| NYCBAR-OP2024-5-2024 | Formal Opinion 2024-5: Ethical Obligations of Lawyers and Law Firms Relating to the Use of Generative Artificial Intelligence in the Practice of Law | New York City Bar Association, Professional Ethics Committee | professional-body | https://www.nycbar.org/wp-content/uploads/2024/08/20221329_GenerativeAILawPractice.pdf | 2024-08-07 | full |
| NYCBAR-OP2026-2-2026 | NYC Bar Association Releases Formal Opinion on Ethical Use of AI for Recording, Transcribing, and Summarizing Non-Client Conversations (press release for Formal Opinion 2026-2, dated 5 Aug 2026) | New York City Bar Association | professional-body | https://www.nycbar.org/press-releases/nyc-bar-association-releases-formal-opinion-on-ethical-use-of-ai-for-recording-transcribing-and-summarizing-non-client-conversations/ | 2026-08-17 | full |
| NYSBA-TFAI-2024 | Report and Recommendations of the New York State Bar Association Task Force on Artificial Intelligence | New York State Bar Association | professional-body | https://nysba.org/wp-content/uploads/2022/03/2024-April-Report-and-Recommendations-of-the-Task-Force-on-Artificial-Intelligence.pdf | 2024-04 | full |
| SPI-AI-2026 | The 2026 Impact of AI on Professional Services (report landing page) | SPI Research | survey | https://spiresearch.com/reports/2026-ai-professional-services-survey/ | 2026-10 | full |
| STANFORD-DEL-2026 | Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives | Stanford Digital Economy Lab (Brynjolfsson) and University of Southern California (Petropoulos) | academic | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | 2026-08-23 | full |
| STANFORD-MAGESH-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362) | Stanford University and Yale University (Magesh, Surani, Dahl, Suzgun, Manning, Ho) | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 | full |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 | full |
| TRI-LDOR-2026 | 2026 Legal Department Operations Report | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/legal-department-operations-report-2026 | 2026-09-22 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-SOTLM-2026 | Legal market report 2026 analysis: AI bubble risk (State of the US Legal Market 2026, with Georgetown Law Center on Ethics and the Legal Profession) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble | 2026-01-14 | full |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 | full |
| VALS-VLAIR-2025 | Vals Legal AI Report (VLAIR) | Vals AI, with Legaltech Hub | survey | https://www.vals.ai/vlair | 2025-02-27 | full |

Count by type (47 distinct sources): academic: 7, conference: 2, firm: 1, press: 2, professional-body: 8, regulator: 7, standard-setter: 1, survey: 10, vendor: 9. Dates marked 2026-10-19 are read dates for pages with no printed date; "2026" means the document gives no month. Vals AI's report is typed as survey (an industry benchmark, not peer reviewed). The court judgment (Ayinde) is typed regulator. ABA-OP512-2024 is search-only; EZEL-ABA512-2024 is a secondary summary.

## 6. Gaps

**Not reachable or not read**
- ABA Formal Opinion 512: americanbar.org returned a Cloudflare challenge and the archive route failed; only secondary summaries were read. Texas Opinion 705, Florida Opinion 24-1 (the page returned no body) and DC Opinion 388 were not read.
- SRA risk outlook and AI pages (Cloudflare challenge). Law360 report on the BSB ("absolute caution") is paywalled; the BSB's own press release was used instead.
- AICPA, ICAEW, IESBA and PCAOB guidance pages: returned errors or generic pages. No accounting-body view on AI in firm knowledge reuse or methodology libraries was verified.
- McKinsey Lilli primary page (403): the "up to 30 percent" figure is read only in the Stanford paper.
- iManage Knowledge Work Benchmark full report and APQC full report and segment cuts (members or download only); only headline pages were read. No professional-services cut of APQC data was found.
- Thomson Reuters Future of Professionals and ILTA executive summary give no printed publication month; only the year is recorded.
- Web search was rationed and ran out before three planned searches (named law-firm knowledge deployments with ethical-wall controls, McKinsey Lilli usage figures, and licensed-content rulings).

**Not found at all**
- Any firm or in-house team publishing measured quality evidence (error rates, override rates, parallel runs, retrieval precision, permission-leakage tests) for its own knowledge base, enterprise search or precedent assistant.
- A named firm describing its ethical-wall enforcement in AI search and the results of testing it.
- Client outside counsel guideline texts on AI use, and survey data on how many clients restrict or require AI (the ACC/Everlaw survey page returned 403).
- A ruling or authoritative guidance on using licensed third-party content (for example publisher databases) inside an internal AI knowledge base; Thomson Reuters v. Ross was not located or verified.
- Consulting-firm KM governance beyond the Stanford paper (BCG, Bain, Deloitte, EY, KPMG primary pages not reached).
- Public data on in-house shared-service teams outside legal.

**Cautions**
- Heppner is one district court's ruling on a criminal defendant's self-directed use of a public tool; do not extend it to enterprise tools without further authority. A reported contrary result from another federal court was seen in a search summary only.
- The Stanford and Vals measurements test commercial products as of 2024-2025 and are not about firm-internal knowledge bases.
- The Kantata, iManage, Thomson Reuters, Deltek and Certinia sources have commercial interests in AI adoption.

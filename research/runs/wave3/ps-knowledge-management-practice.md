# Professional services, knowledge-management: practice angle

Prepared 2026-10-19. Archetype: professional-services. Module: knowledge-management (precedents, methods and expertise: knowledge bases, enterprise search, expertise location, reuse of past work, knowledge capture from engagements). Angle: practice (what firms and in-house teams actually do). Public sources only. Source keys follow `PUBLISHER-SHORT-YYYY`.

## 1. Summary

- **Output.** 16 candidate use cases: grade A 0, B 11, C 4, D 1. 44 sources read (43 full, 1 search-only): vendor 28, press 7, survey 5, firm 2, conference 1, academic 1. No regulator, standard-setter, professional-body, podcast, community or job-posting source was reached for this angle (see Gaps).
- **Most named practice is legal, and most of it is search over a curated or governed document estate.** Allens, Womble Bond Dickinson UK, Chaffetz Lindsey and Bicalho Navarro describe AI search or an assistant inside their document management system, and Clifford Chance announced an AI-ready Knowledge Bank of 400,000+ reclassified documents (IMANAGE-ALLENS-2026; IMANAGE-WOMBLE-2026; IMANAGE-CHAFFETZ-2026; IMANAGE-BICALHO-2026; ARTIFICIALLAWYER-CLIFFORDCHANCE-2026). Consulting has one well-documented example: McKinsey's Lilli, with current usage figures that reach us only second hand (MCKINSEY-LILLI-2023; THEOUTPOST-LILLI-2025). Accounting and engineering add almost nothing on this module.
- **Curation is the prerequisite the firms themselves name.** Allens relied on an existing taxonomy and curated library; Womble Bond Dickinson cut its taxonomy to four nodes and kept curation with named owners; McKinsey relies on hundreds of data stewards (IMANAGE-ALLENS-2026; IMANAGE-WOMBLE-2026; MCKINSEY-LILLI-2023). Both flag a content-quality risk: lawyers taking the easiest path rather than the best template (Allens) and AI not telling good content from poor (Womble Bond Dickinson).
- **There is no independent measurement of internal-knowledge retrieval.** Published figures are access counts (1,350 legal staff at Allens), adoption counts (McKinsey), single-task benchmarks run by the vendor (Harvey) and an executive's recollection (Basware). No error rate, override rate, parallel run or inspection result for firm-knowledge search was found. This is why no entry reaches grade A.
- **The 2026 frontier is governed access for agents.** Within five months: NetDocuments' context graph in private preview (2026-05-14), Clifford Chance's Knowledge Bank (2026-07-20), Harvey's cross-system agentic search (2026-09-30), Legora's connection to the iManage MCP Server (2026-10-16) and Harvey Graph (2026-10-19). Each stresses permissions and ethical walls carrying through to the agent.
- **Roles are moving toward knowledge-led AI adoption.** Troutman Pepper Locke created a knowledge management and AI partner role (2026-04-29); Lewis Silkin's knowledge lawyers lead Harvey adoption; Gowling WLG's national director spans AI, innovation and knowledge (TROUTMAN-KM-2026; HARVEY-LEWISSILKIN-2025; HARVEY-GOWLING-2025).

## 2. Use cases

```yaml
- id: professional-services-knowledge-management-01
  title: AI search over a curated precedent and know-how library
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Lawyers struggle to find the precedent or template they want quickly in a growing knowledge collection; at Allens, browsing through SharePoint was meant only as an interim fix (IMANAGE-ALLENS-2026).
  solution: The firm's knowledge team keeps a curated library of precedents and templates with a taxonomy in the document management system. A cloud AI search layer (named in the sources as iManage Insight+) surfaces relevant documents in context, with favourites and team-pinned standard documents on a landing page. Rollout uses practice-group training and lawyer champions.
  outcomes:
  - lever: experience
    description: Insight+ search was extended to legal staff across the firm; the source reports positive staff feedback but no usage or time measurements
    figure: 1,350 legal staff
    measures: Legal staff at Allens who 'now benefit from' the Insight+ search experience (an access count in a vendor case study, not a usage, time-saving or quality measurement)
    provenance: vendor-published
    source_ref: IMANAGE-ALLENS-2026
  - lever: experience
    description: Insight+ headline statistics on the Womble Bond Dickinson UK story; the text says Insight+ is accessed by 'a significant proportion' of lawyers but gives no share
    figure: 1,250 Insight+ users; 600 lawyers
    measures: Headline statistics labelled 'Insight+ users' (1,250) and 'lawyers' (600) in the vendor case study; the body text separately says about 600 lawyers and 1,250 users are connected to the iManage platform
    provenance: vendor-published
    source_ref: IMANAGE-WOMBLE-2026
  prerequisites:
  - A curated library with an existing taxonomy; Allens' head of knowledge says the vendor's team was impressed by the curation and taxonomy already in place (IMANAGE-ALLENS-2026)
  - Documents and knowledge on a cloud document management platform; Womble Bond Dickinson cut a two-decade taxonomy to a maximum of four nodes before migration and added search facets and metadata tagging (IMANAGE-WOMBLE-2026)
  - A knowledge team with named owners for curation and stewardship (IMANAGE-WOMBLE-2026)
  - Change management through practice-group training and influential lawyer champions (IMANAGE-ALLENS-2026)
  risks_and_guardrails:
  - Allens' Chief Knowledge Officer says that with growing appetite for AI there is a risk lawyers take the path of least resistance rather than following best practice in locating the most relevant template (IMANAGE-ALLENS-2026)
  - Womble Bond Dickinson's head of IT applications says AI is not necessarily going to distinguish good-quality content from content it should not serve up, so the curated knowledge profile (confidentiality, client, AI-processing tags) matters (IMANAGE-WOMBLE-2026)
  - Womble Bond Dickinson deliberately kept a controlled model in which curation stays with assigned owners, although the platform supports broader submission (IMANAGE-WOMBLE-2026)
  - No search-success, precision or override measurements are published in any of these stories
  human_checkpoints:
  - Knowledge team curates, classifies and retires content before it is searchable (IMANAGE-WOMBLE-2026; IMANAGE-EMEAFIRM-2026)
  - The lawyer chooses which retrieved precedent applies to the matter
  role_evolution: Knowledge teams spend more effort on curation, taxonomy, pinning standard documents, training and finding champions (IMANAGE-ALLENS-2026). In another firm's story, knowledge lawyers still draft templates, answer queries and research developments, while KM professionals run the systems and processes (IMANAGE-EMEAFIRM-2026).
  evidence_grade: B
  sources:
  - ref: IMANAGE-ALLENS-2026
    title: Allens taps into goldmine of enterprise knowledge with Insight+ (customer story) (page carries no publication date; date shown is the retrieval date)
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/allens-insightplus/
    date: '2026-10-19'
    access: full
    locator: Intro; sections 'The business challenge' and 'The solution'
  - ref: IMANAGE-WOMBLE-2026
    title: Womble Bond Dickinson UK lays an AI-ready foundation (customer story) (page carries no publication date; date shown is the retrieval date)
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/womble-bond/
    date: '2026-10-19'
    access: full
    locator: Headline statistics; sections 'The solution' and 'The business outcomes'
  - ref: IMANAGE-EMEAFIRM-2026
    title: 'Global law firm, EMEA region: Insight+ replaces an in-house knowledge platform (customer story, firm unnamed) (page carries no publication date; date shown is the retrieval date)'
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/global-law-firm-emea-region/
    date: '2026-10-19'
    access: full
    locator: Paragraphs on the six-month go-live, user testers and planned analytics
  - ref: IMANAGE-REGULATOR-2026
    title: 'Independent regulatory body: Insight+ for a precedent library (customer story, organisation unnamed) (page carries no publication date; date shown is the retrieval date)'
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/independent-regulatory-body/
    date: '2026-10-19'
    access: full
    locator: Paragraphs on the 15,000-document knowledge library and the Head of IT quotes
  last_reviewed: '2026-10-19'
  notes: Two further stories are anonymous and so cannot carry the grade. A global law firm's EMEA region (IMANAGE-EMEAFIRM-2026) took six months to go live for its knowledge team and a further month for all EMEA users, with a team of 30 across three companies and about 130 user testers, and plans Insight+ analytics on search terms and content that is not surfacing. An independent regulatory body (IMANAGE-REGULATOR-2026) moved a library of about 15,000 template, precedent and best-practice documents behind Insight+ because every case is checked against precedents and search speed sets closing speed. All sources are vendor-authored; none gives adoption rates, time saved or failed-search data.
- id: professional-services-knowledge-management-02
  title: Natural-language assistant inside the document management system for finding clauses and comparing documents
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Lawyers and staff spend time remembering where a document sits, opening files one by one, and reading long PDFs to find one clause. Search is more than half of what people do in the platform at one firm.
  solution: An AI assistant built into the document management system answers natural-language questions against the firm's own documents, returns marked citations, and does not move content outside the governed platform (named in the sources as Ask iManage; NetDocuments markets a comparable ndMAX Legal AI Assistant).
  outcomes:
  - lever: speed
    description: A new team member can be brought up to speed on an active trial in days rather than weeks, according to the case study; no measurement method is given
    figure: days rather than weeks
    measures: Time for a new team member to get up to speed on an active trial, as described in an iManage customer story about Chaffetz Lindsey (qualitative statement, not a tracked metric)
    provenance: vendor-published
    source_ref: IMANAGE-CHAFFETZ-2026
  - lever: speed
    description: The firm rolled the assistant out to everyone in one window, with no staged rollout by practice group
    figure: two-month window
    measures: Elapsed time in which Chaffetz Lindsey deployed the assistant, per the case study
    provenance: vendor-published
    source_ref: IMANAGE-CHAFFETZ-2026
  prerequisites:
  - 'A single governed repository with filing discipline: Chaffetz Lindsey reports 100 percent adoption of the platform and no shadow repositories (IMANAGE-CHAFFETZ-2026)'
  - Matter-centric organisation and ethical walls already managed; more than 35 percent of Chaffetz Lindsey matters carry ethical screens (IMANAGE-CHAFFETZ-2026)
  - Documents in the vendor's cloud (Bicalho Navarro manages roughly 1.5 million documents in iManage Work in the Cloud) (IMANAGE-BICALHO-2026)
  risks_and_guardrails:
  - The stated main risk at Digital Commerce Bank (an in-house team) is documents or information leaving the organisation in an uncontrolled way; the team keeps queries inside the governed platform (IMANAGE-DCB-2026)
  - Seyfarth Shaw's evaluation of the assistant is described as underway; the story reports no result (IMANAGE-SEYFARTH-2026)
  - No accuracy, error-rate or override figures are published for the assistant; independent task benchmarks exist only for other products (see Module notes)
  human_checkpoints:
  - Lawyers read the cited passage in the source document before relying on it
  - Librarians govern the repository and the AI assistant's use of it (IMANAGE-DCB-2026)
  role_evolution: At Chaffetz Lindsey, non-timekeeping staff found clauses in precedents as fast as attorneys because the assistant was the tool they were most exposed to, and became its champions (IMANAGE-CHAFFETZ-2026). A partner at Bicalho Navarro says he asks the assistant to find a document rather than trying to remember where it is (IMANAGE-BICALHO-2026).
  evidence_grade: B
  sources:
  - ref: IMANAGE-CHAFFETZ-2026
    title: Governance is a powerful differentiator at Chaffetz Lindsey (customer story) (page carries no publication date; date shown is the retrieval date)
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/chaffetz-lindsey/
    date: '2026-10-19'
    access: full
    locator: Paragraphs on the two-month deployment, Ask iManage use, and ethical-screen figure
  - ref: IMANAGE-BICALHO-2026
    title: 'Bicalho Navarro Advogados: greater trust in knowledge search results in the iManage Cloud (customer story) (page carries no publication date; date shown is the retrieval date)'
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/bicalho-navarro/
    date: '2026-10-19'
    access: full
    locator: Paragraphs quoting the partner and IT manager on locating precedent clauses and the 1.5 million documents
  - ref: IMANAGE-DCB-2026
    title: Digital Commerce Bank unifies diverse teams on one platform (customer story) (page carries no publication date; date shown is the retrieval date)
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/digital-commerce-bank/
    date: '2026-10-19'
    access: full
    locator: Paragraphs on Ask iManage use by legal and technology teams and the librarians' governance role
  - ref: NETDOCUMENTS-NDMAX-2026
    title: ndMAX legal AI suite (product page) (page carries no publication date; date shown is the retrieval date)
    publisher: NetDocuments
    type: vendor
    url: https://www.netdocuments.com/ndmax
    date: '2026-10-19'
    access: full
    locator: 'Legal AI Assistant paragraph: ask a question of one or hundreds of files'
  - ref: IMANAGE-SEYFARTH-2026
    title: Seyfarth Shaw (iManage customer story) (page carries no publication date; date shown is the retrieval date)
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/seyfarth-shaw/
    date: '2026-10-19'
    access: full
    locator: Paragraph on the evaluation of the assistant
  last_reviewed: '2026-10-19'
  notes: All outcome statements come from vendor-authored customer stories that quote the customer. The case-study pages carry no publication date. Digital Commerce Bank is an in-house team at a bank (in-house).
- id: professional-services-knowledge-management-03
  title: Firm-wide knowledge assistant over a consultancy's curated intellectual property
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: At engagement kickoff, finding the most relevant research documents and experts is described as taking about two weeks of researching and networking, even for senior colleagues. Analogues and comparables can take days of chasing experts.
  solution: McKinsey built its own assistant (Lilli) over more than 40 curated knowledge sources, which scans them, returns about five to seven relevant items with summaries and links, and names experts. It has an internal-knowledge mode and an external-sources mode. Confidential client data is permitted in Lilli but not in public tools, per a Bloomberg interview with the firm's technology and AI leader.
  outcomes:
  - lever: capacity
    description: Reported firm-wide use of the assistant and a time saving on gathering and synthesising information
    figure: Over 75% of 43,000 employees use it monthly; 17 uses per week per average user; over 500,000 prompts a month; 30% of time saved
    measures: 'As relayed by a secondary summary of a Bloomberg interview (June 2025): share of McKinsey''s 43,000 employees using Lilli monthly; average uses per week per user; prompts answered per month; share of time they would otherwise have spent gathering and synthesising information. The summary does not say how the 30% was measured, and the Bloomberg original was not accessed.'
    provenance: self-reported
    source_ref: THEOUTPOST-LILLI-2025
  - lever: speed
    description: In the 2023 launch announcement, one associate partner says Lilli saves up to 20 percent of his time preparing for meetings
    figure: up to 20%
    measures: One associate partner's own estimate of his meeting-preparation time (an individual statement, not a firm-wide measurement)
    provenance: self-reported
    source_ref: MCKINSEY-LILLI-2023
  prerequisites:
  - Hundreds of data stewards who curate content, check accuracy and quality, sanitise it for client confidentiality and make it searchable across formats (MCKINSEY-LILLI-2023)
  - More than 40 curated knowledge sources, a project team that grew from three to over 70 people, and input from legal, cyber security, risk and talent functions (MCKINSEY-LILLI-2023)
  - Upskilling users on prompt engineering and content validation (MCKINSEY-LILLI-2023)
  risks_and_guardrails:
  - No independent evaluation of Lilli's accuracy was found
  - The firm says the biggest challenge was bringing legal, cyber security, risk management and talent functions to the table quickly, rather than the technology (MCKINSEY-LILLI-2023)
  - Confidential client information may only be entered into Lilli, not public AI tools, per the Bloomberg interview as relayed (THEOUTPOST-LILLI-2025)
  human_checkpoints:
  - Users validate the content Lilli returns; the firm lists content validation as a skill it upskills users on (MCKINSEY-LILLI-2023)
  - Data stewards curate and sanitise the underlying sources (MCKINSEY-LILLI-2023)
  role_evolution: Existing data stewards become central to the system's quality (MCKINSEY-LILLI-2023). McKinsey's technology and AI leader is quoted as saying Lilli could do work such as PowerPoint production that business analysts used to do, but that this does not necessarily mean fewer analysts, who would do work more valuable to clients (THEOUTPOST-LILLI-2025).
  evidence_grade: B
  sources:
  - ref: MCKINSEY-LILLI-2023
    title: Meet Lilli, our generative AI tool that's a researcher, a time saver, and an inspiration (alumni-site copy of the firm announcement; read through the r.jina.ai mirror, direct curl failed; date taken from the URL slug 2023-10)
    publisher: McKinsey & Company
    type: firm
    url: https://www.mckinsey.com/alumni/news-and-events/global-news/firm-news/2023-10-lilli
    date: 2023-10
    access: full
    locator: Paragraphs on the 40+ knowledge sources, the two-week kickoff search, the data stewards and the team of 70
  - ref: THEOUTPOST-LILLI-2025
    title: McKinsey embraces AI for consulting tasks, transforming junior roles (aggregator summary of a Bloomberg interview with McKinsey's technology and AI leader)
    publisher: TheOutpost.ai
    type: press
    url: https://theoutpost.ai/news-story/mc-kinsey-embraces-ai-for-consulting-tasks-transforming-junior-roles-16077/
    date: '2025-06-03'
    access: full
    locator: Paragraphs on monthly use, prompts per month, 30% time saving and client-data policy
  - ref: MAGINATIVE-LILLI-2023
    title: McKinsey unveils Lilli, its own generative AI assistant
    publisher: Maginative
    type: press
    url: https://www.maginative.com/article/mckinsey-unveils-lilli-its-own-generative-ai-assistant/
    date: '2023-08-16'
    access: full
    locator: Paragraphs on the beta, 100,000 documents and attribution
  last_reviewed: '2026-10-19'
  notes: Grade B rather than A because the current usage figures reach us through a secondary summary of a Bloomberg interview (the original is paywalled), and the 30% time saving has no stated method. The 2023 launch page says there 'will be more than 100,000 documents and interview transcripts'; the Maginative report says Lilli 'can search over 100,000'. The firm page is dated by its URL slug (2023-10); Maginative reported the launch on 2023-08-16. Another secondary item (AI Weekly, late 2025, snippet only) cites 500,000+ prompts a month, which matches the figure here but was not opened.
- id: professional-services-knowledge-management-04
  title: 'Finding who has done this before: expert and experience location from firm records'
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - research-synthesis
  - coordination-scheduling
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: NetDocuments frames the problem as a partner asking whether the firm has handled something similar, where the answer 'depends on who's in the room' (NETDOCUMENTS-CONTEXTGRAPH-2026). ILTA's 2026 summary says knowledge infrastructure remains dramatically underdeveloped across enterprise search, expertise management, pricing, procurement and competitive intelligence (ILTA-TECHSURVEY-2026).
  solution: The assistant names experts alongside documents (Lilli); a relationship and experience system catalogues each lawyer's and engagement's experience and suggests relevant experience for a pursuit (Intapp DealCloud); a document platform's context graph shows 'the people who have done this work before' on an unfamiliar matter (NetDocuments, in private preview).
  outcomes:
  - lever: speed
    description: The firm says finding analogues or comparables 'could take days of chasing down the right experts' before Lilli and returns answers much more quickly now; no measurement is published
    figure: days (before Lilli)
    measures: The firm's own description of how long identifying analogues took before Lilli (not a tracked metric)
    provenance: self-reported
    source_ref: MCKINSEY-LILLI-2023
  prerequisites:
  - Curated records of experts and past engagements; McKinsey describes a network of experts across 70 countries (MCKINSEY-LILLI-2023)
  - Experience data integrated with HR and financial systems (INTAPP-EXPERIENCE-2026)
  - Permissions and ethical walls preserved in the people-and-matter index (NETDOCUMENTS-CONTEXTGRAPH-2026)
  risks_and_guardrails:
  - NetDocuments says its context graph respects each firm's existing permissions and ethical walls; the feature is in private preview and no outcome is reported (NETDOCUMENTS-CONTEXTGRAPH-2026)
  - No source reports how accurate expert or experience suggestions are
  human_checkpoints:
  - The professional decides whom to contact and which experience to cite
  role_evolution: Not described beyond the assistant doing the first search that colleagues used to do by networking (MCKINSEY-LILLI-2023).
  evidence_grade: B
  sources:
  - ref: MCKINSEY-LILLI-2023
    title: Meet Lilli, our generative AI tool that's a researcher, a time saver, and an inspiration (alumni-site copy of the firm announcement; read through the r.jina.ai mirror, direct curl failed; date taken from the URL slug 2023-10)
    publisher: McKinsey & Company
    type: firm
    url: https://www.mckinsey.com/alumni/news-and-events/global-news/firm-news/2023-10-lilli
    date: 2023-10
    access: full
    locator: Paragraphs on analogues and comparables, and on the assistant identifying experts
  - ref: INTAPP-EXPERIENCE-2026
    title: Experience management (Intapp DealCloud product page) (page carries no publication date; date shown is the retrieval date)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/dealcloud/experience-management/
    date: '2026-10-19'
    access: full
    locator: Sections on experience search, suggested experience and the FAQ on data integration
  - ref: NETDOCUMENTS-CONTEXTGRAPH-2026
    title: NetDocuments Unveils the First Context Graph for Legal Work (press release; read through the r.jina.ai mirror, direct curl returned 403)
    publisher: NetDocuments
    type: vendor
    url: https://www.netdocuments.com/company-news/netdocuments-unveils-context-graph-legal-platform/
    date: '2026-05-14'
    access: full
    locator: Paragraph on opening an unfamiliar matter and seeing the people who have done this work before
  - ref: ILTA-TECHSURVEY-2026
    title: The ILTA Technology Survey 2026 executive summary (PDF)
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: Page 9, 'Curtain Call for the Data Center' (knowledge infrastructure gap)
  last_reviewed: '2026-10-19'
  notes: Grade B rests on the Lilli feature, which the firm itself describes; the Intapp and NetDocuments items are product claims (grade C on their own). The Kantata Expertise Agent also ranks people for projects with reasoning (KANTATA-AGENT-2026); that staffing use is routed to staffing-resourcing.
- id: professional-services-knowledge-management-05
  title: AI-assisted classification and summarisation of historic documents into an AI-ready knowledge bank
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - data-reporting
  - research-synthesis
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Decades of firm work sit in repositories with inconsistent metadata, so generative tools cannot be pointed at them safely or usefully.
  solution: Clifford Chance announced a Knowledge Bank built with Epiq Advisory for Law Firms and Microsoft. More than 400,000 documents were reclassified and summarised into a curated content set, with natural-language search, summarisation, smart tagging and generative answers in the lawyer's workflow, and a Permissioned Search feature that applies metadata-driven permissions.
  outcomes:
  - lever: capacity
    description: The announcement says the platform already contains this many documents, which were reclassified and summarised; it gives no time, cost or quality measurement
    figure: 400,000+ documents
    measures: Documents in Clifford Chance's Knowledge Bank that were reclassified and summarised, per the joint announcement as relayed by Artificial Lawyer
    provenance: self-reported
    source_ref: ARTIFICIALLAWYER-CLIFFORDCHANCE-2026
  prerequisites:
  - A Microsoft 365 and Azure estate; the platform is described as built entirely on SharePoint, Power Platform, Graph API and Azure AI Studio (ARTIFICIALLAWYER-CLIFFORDCHANCE-2026)
  - Metadata-driven permissions aligned with client confidentiality (ARTIFICIALLAWYER-CLIFFORDCHANCE-2026)
  - Significant customisation and engineering support, which Artificial Lawyer says Epiq provided (ARTIFICIALLAWYER-CLIFFORDCHANCE-2026)
  risks_and_guardrails:
  - The announcement says the curated set ensures generative tools use only trusted internal materials; no accuracy or error data is given (ARTIFICIALLAWYER-CLIFFORDCHANCE-2026)
  - A vendor viewpoint predicts professional support lawyers will have to review AI-generated classifications, correct errors and identify gaps (KMWORLD-LEXSOFT-2025)
  human_checkpoints:
  - 'Predicted, not reported for Clifford Chance: professional support lawyers and knowledge professionals review AI classifications and curation (KMWORLD-LEXSOFT-2025)'
  role_evolution: The announcement quotes a partner who is the firm's Global Head of Knowledge & Training as saying the Knowledge Bank is central to its client strategy (ARTIFICIALLAWYER-CLIFFORDCHANCE-2026). A vendor viewpoint predicts professional support lawyers become quality guardians over AI-generated metadata (KMWORLD-LEXSOFT-2025).
  evidence_grade: B
  sources:
  - ref: ARTIFICIALLAWYER-CLIFFORDCHANCE-2026
    title: Clifford Chance launches AI KM platform with Microsoft and Epiq
    publisher: Artificial Lawyer
    type: press
    url: https://artificiallawyer.com/2026/07/20/clifford-chance-launches-ai-km-platform-with-microsoft-epiq
    date: '2026-07-20'
    access: full
    locator: Bullet list of platform features and the quotes from the Global Head of Knowledge & Training
  - ref: LAW360-CLIFFORDCHANCE-2026
    title: Clifford Chance launches AI knowledge management tech (lead paragraph only; remainder paywalled)
    publisher: Law360
    type: press
    url: https://www.law360.com/articles/2503174
    date: '2026-07-20'
    access: search-only
    locator: Lead paragraph (announcement on 20 July 2026); remainder paywalled
  - ref: KMWORLD-LEXSOFT-2025
    title: Conversational AI interfaces and human-AI collaboration to transform legal knowledge management in 2026 (viewpoint by the CEO of Lexsoft Systems, a legal-sector software vendor)
    publisher: KMWorld
    type: press
    url: https://www.kmworld.com/Articles/Editorial/ViewPoints/Conversational-AI-interfaces-and-human-AI-collaboration-to-transform-legal-knowledge-management-in-2026-172705.aspx
    date: '2025-12-08'
    access: full
    locator: Paragraphs on AI-human collaboration and professional support lawyers
  - ref: SOLICITORSJOURNAL-KM-2025
    title: How AI will redefine legal knowledge management in 2026 (same author and argument as the KMWorld viewpoint)
    publisher: Solicitors Journal
    type: press
    url: https://solicitorsjournal.com/sjarticle/how-ai-will-redefine-legal-knowledge-management-in-2026
    date: '2025-12-09'
    access: full
    locator: Paragraphs on AI-human collaboration and professional support lawyers
  last_reviewed: '2026-10-19'
  notes: Maturity is 'announced' because the sources report a launch without showing use. Law360 was opened but only the lead paragraph is visible (paywall), so it is marked search-only and supports only the fact of the announcement. A Legal IT Insider interview with the firm's knowledge lead (reposted by Legal Tech Monitor on 2026-08-21) could not be opened (bot check). The Artificial Lawyer author notes that the project needed a lot of customisation and engineering. The KMWorld and Solicitors Journal pieces are forecasts by a vendor executive.
- id: professional-services-knowledge-management-06
  title: Agentic retrieval across document systems, with governed connections (MCP) for third-party AI tools
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: A lawyer wants to know how the team handled a similar issue before, but the answer may sit in an agreement, brief or email across several systems, and the lawyer may not know the filename, folder or search terms.
  solution: An AI agent plans the search parameters itself across connected systems (Harvey reports iManage, SharePoint and Google Drive), returns cited results, and pauses for the lawyer to review when more results exist. Separately, document platforms expose firm knowledge to outside AI tools over the Model Context Protocol under the platform's permissions (iManage MCP Server connected to Legora; NetDocuments via ndConnect, in private preview).
  outcomes:
  - lever: speed
    description: No measurements are published for agentic search or the MCP connections
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: HARVEY-AGENTICSEARCH-2026
  prerequisites:
  - A governed source-of-truth repository with per-user permissions that the agent inherits (HARVEY-AGENTICSEARCH-2026; LEGORA-IMANAGE-2026)
  - Metadata that marks confidentiality, client restrictions and AI-processing permissions at client or matter level; Womble Bond Dickinson plans to apply these when iManage makes the capability available (IMANAGE-WOMBLE-2026)
  risks_and_guardrails:
  - Harvey says search uses each person's permissions in the connected system, so documents the user cannot access do not appear (HARVEY-AGENTICSEARCH-2026)
  - iManage and Legora say iManage permissions determine what each user can retrieve through the MCP connection (LEGORA-IMANAGE-2026)
  - Chaffetz Lindsey's principle is that data stays in the document platform and tools reach in rather than pulling content out (IMANAGE-CHAFFETZ-2026)
  - Every file the Harvey agent touches in a Vault is logged in an audit trail (HARVEY-VAULT-2026)
  human_checkpoints:
  - The agent pauses for the lawyer to review results when more are available (HARVEY-AGENTICSEARCH-2026)
  - The lawyer reviews prior work in context from links to the source files (HARVEY-AGENTICSEARCH-2026)
  role_evolution: Not described. Lawyers describe what they need in plain language rather than choosing files first (HARVEY-AGENTICSEARCH-2026).
  evidence_grade: C
  sources:
  - ref: HARVEY-AGENTICSEARCH-2026
    title: Introducing Agentic Search for Your Document Systems
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/agentic-search-document-management-systems
    date: '2026-09-30'
    access: full
    locator: Sections on describing what you need, permissions, and availability
  - ref: HARVEY-VAULT-2026
    title: Agentic Vault Search and Organization
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/agentic-vault-search-and-organization
    date: '2026-09-08'
    access: full
    locator: Paragraphs on agent permissions and audit trail
  - ref: LEGORA-IMANAGE-2026
    title: Legora and iManage deepen integration through iManage MCP Server
    publisher: Legora
    type: vendor
    url: https://legora.com/newsroom/legora-and-imanage-deepen-integration-through-imanage-mcp-server
    date: '2026-10-16'
    access: full
    locator: Opening paragraphs and the two executive quotes
  - ref: NETDOCUMENTS-CONTEXTGRAPH-2026
    title: NetDocuments Unveils the First Context Graph for Legal Work (press release; read through the r.jina.ai mirror, direct curl returned 403)
    publisher: NetDocuments
    type: vendor
    url: https://www.netdocuments.com/company-news/netdocuments-unveils-context-graph-legal-platform/
    date: '2026-05-14'
    access: full
    locator: Paragraphs on AI agents working via MCP through ndConnect; private preview opens 14 May 2026
  - ref: IMANAGE-WOMBLE-2026
    title: Womble Bond Dickinson UK lays an AI-ready foundation (customer story) (page carries no publication date; date shown is the retrieval date)
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/womble-bond/
    date: '2026-10-19'
    access: full
    locator: Section 'Building outward from a governed core'
  last_reviewed: '2026-10-19'
  notes: Harvey's own post says agentic search across iManage, SharePoint and Google Drive is 'available now' and has to be switched on by a Harvey representative; no customer is named. The Legora and iManage release is worded as a connection that 'will give' mutual customers additional ways to work, so it is announced. Chaffetz Lindsey's director says MCP tools will be 'the first among many' for an AI-first firm (IMANAGE-CHAFFETZ-2026).
- id: professional-services-knowledge-management-07
  title: Mining a firm's own deal history to benchmark terms and build precedent databases
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - research-synthesis
  - data-reporting
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: A firm's executed agreements hold what counterparties actually accepted, but relevant deals are spread across matters, folders and systems, so lawyers rely on generic clause examples or build comparison spreadsheets by hand.
  solution: 'Ropes & Gray''s director of practice technology says generative AI helped build a precedent library for a private equity client by extracting, analysing and comparing historical deal terms into a searchable database, so drafting follows the client''s customary practice. Harvey describes the method: pick comparable deals, extract caps, baskets and survival periods into a review table, verify against source citations, and add the executed agreement back after closing.'
  outcomes:
  - lever: quality
    description: No measurement is published; the aim stated is drafting that matches the client's customary practices
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: HARVEY-ROPES-2025
  prerequisites:
  - Executed agreements held in a vault or precedent collection that can be queried (HARVEY-INDEMNITY-2026)
  - A specific legal question and deal parameters (transaction type, size, jurisdiction, buyer or seller side) to select a comparable cohort (HARVEY-INDEMNITY-2026)
  risks_and_guardrails:
  - 'Harvey cautions that a larger precedent set is not automatically better: mixing deals with different economics, structures or governing law can obscure more than it shows (HARVEY-INDEMNITY-2026)'
  - Older agreements may reflect a negotiating posture or policy that has since changed, and outliers (for example deals with representations and warranties insurance) should be identified before treating them as the norm (HARVEY-INDEMNITY-2026)
  - Users can click through citations to verify extracted data against the underlying document (HARVEY-INDEMNITY-2026)
  human_checkpoints:
  - The lawyer frames the question, chooses the comparable cohort and decides the negotiating position; Harvey says the tool surfaces the comparison and the lawyer decides (HARVEY-INDEMNITY-2026)
  role_evolution: Harvey says the manual work in precedent benchmarking is rarely the legal judgment itself (finding agreements, locating provisions, pulling terms into a grid), and that this retrieval and structuring is what the tool takes on (HARVEY-INDEMNITY-2026).
  evidence_grade: B
  sources:
  - ref: HARVEY-ROPES-2025
    title: Theresa Spartichino (Ropes & Gray) on driving innovation (Innovation Spotlight interview)
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/theresa-spartichino-on-driving-innovation
    date: '2025-10-02'
    access: full
    locator: 'Answer on use cases: precedent library for a private equity client'
  - ref: HARVEY-INDEMNITY-2026
    title: Benchmarking an indemnification clause against your own deal history
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/indemnification-clauses-against-deal-history
    date: '2026-09-25'
    access: full
    locator: Sections on building the cohort, review tables, citation verification and adding closed deals back
  last_reviewed: '2026-10-19'
  notes: The Ropes & Gray statement comes from a vendor-published interview with the firm's director of practice technology (2025-10-02). The Harvey benchmarking post (2026-09-25) is a vendor how-to, not evidence of use by a named firm. Overlaps with work-production; kept here as reuse of precedent.
- id: professional-services-knowledge-management-08
  title: In-house legal department knowledge base of policies, precedents and prior decisions that AI draws on (in-house)
  archetype: professional-services
  module: knowledge-management
  function: risk-compliance-legal
  work_types:
  - research-synthesis
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: In-house legal teams hold decades of documents, and much of their review judgment lives in individual lawyers' heads; two reviewers can give the same contract different answers.
  solution: BMW Group's legal function announced a rollout of Legora across its legal department for research, review and drafting, including first drafts based on approved internal standards and precedents, and says the initiative is meant to strengthen knowledge management. Rio Tinto's legal team moved 4.5 million documents to a cloud platform and says it is considering natural-language queries across documents. Harvey describes a 'legal brain' in which a department's policies, prior decisions and outcomes feed agents.
  outcomes:
  - lever: experience
    description: After four months, adoption of the document platform at Rio Tinto's legal team reached 80 percent; this measures the document management platform, whose search replaced a SharePoint overlay, not an AI feature
    figure: 80% adoption after four months
    measures: 'Adoption of the iManage platform across 210 legal-team staff after four months, per a vendor case study quoting Rio Tinto''s digital transformation lead (adjacent: document management, not AI knowledge search)'
    provenance: vendor-published
    source_ref: IMANAGE-RIOTINTO-2026
  prerequisites:
  - Approved internal standards and precedents to ground first drafts (LEGORA-BMW-2026)
  - Platform that fits existing tools such as Microsoft Word, with access, security and governance requirements applied (LEGORA-BMW-2026)
  - A migrated, centralised document estate; Rio Tinto has legal assets going back 20 years (IMANAGE-RIOTINTO-2026)
  risks_and_guardrails:
  - BMW says the platform is implemented in accordance with its access, security and governance requirements (LEGORA-BMW-2026)
  - Harvey's vision says legal sets what agents may resolve and when review is required, with a full audit log of agent and human actions (HARVEY-INHOUSE-2026)
  human_checkpoints:
  - Legal decides what agents can handle and where people make the call (HARVEY-INHOUSE-2026)
  role_evolution: BMW's group general counsel says the tools expand capacity to handle work in-house while keeping lawyers focused on the most complex and strategic matters (LEGORA-BMW-2026). At Rio Tinto the digital transformation team, rather than IT, manages the platform (IMANAGE-RIOTINTO-2026).
  evidence_grade: B
  sources:
  - ref: LEGORA-BMW-2026
    title: Legora collaborates with BMW Group to advance AI-enabled legal services
    publisher: Legora
    type: vendor
    url: https://legora.com/newsroom/legora-collaborates-with-bmw-group-to-advance-ai-enabled-legal-services
    date: '2026-10-08'
    access: full
    locator: Opening paragraph and the paragraph on AI-supported workflows and first drafts from approved internal standards and precedents
  - ref: IMANAGE-RIOTINTO-2026
    title: Rio Tinto makes institutional knowledge more accessible and actionable with iManage (customer story) (page carries no publication date; date shown is the retrieval date)
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/rio-tinto/
    date: '2026-10-19'
    access: full
    locator: Paragraphs on the migration of 4.5 million documents, 80 percent adoption and AI plans
  - ref: HARVEY-INHOUSE-2026
    title: Building a frontier in-house organization
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/building-a-frontier-in-house-organization
    date: '2026-10-13'
    access: full
    locator: Paragraphs on the department's knowledge and review playbooks
  - ref: IMANAGE-LEGALOPS-2026
    title: Global legal operations customer (iManage customer story, organisation unnamed) (page carries no publication date; date shown is the retrieval date)
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/global-legal-operations-customer/
    date: '2026-10-19'
    access: full
    locator: Paragraphs on evaluating AI to find things quicker (organisation unnamed)
  last_reviewed: '2026-10-19'
  notes: In-house examples throughout. BMW's release is a vendor announcement dated 2026-10-08 that quotes BMW's group general counsel. Rio Tinto's figure concerns document management adoption, so it supports the prerequisite (a findable estate), not an AI effect. An anonymous global legal operations customer (IMANAGE-LEGALOPS-2026) reports a cost-benefit analysis that led it to decline an expensive AI module from its previous document platform.
- id: professional-services-knowledge-management-09
  title: AI-drafted retrospectives and lessons learned feeding a searchable firm knowledge base
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - document-production
  - data-reporting
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: Expertise stays locked in decks and in consultants' heads, so each engagement starts without the lessons of the last.
  solution: A professional services automation platform's agents draft retrospectives from completed projects, turn outcomes into customer success stories and organise lessons learned into a searchable, firm-wide knowledge base (Certinia Veda Retrospective Drafter and Knowledge Base agents). Kantata describes an engine in which each engagement strengthens the next.
  outcomes:
  - lever: quality
    description: No measurements published
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Engagement records (SOWs, meeting notes, decisions, outcomes) held in the platform (CERTINIA-VEDA-2026; KANTATA-AGENT-2026)
  risks_and_guardrails:
  - Certinia says agents act within the permissions, approval thresholds and auditability the organisation requires (CERTINIA-VEDA-2026)
  human_checkpoints:
  - Approval thresholds set by the organisation (CERTINIA-VEDA-2026); the sources do not say who reviews a drafted retrospective
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: Certinia Veda AI agents for professional services (product page) (page carries no publication date; date shown is the retrieval date)
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: Section 'Value capture & knowledge transfer' and the Manage agent list (Knowledge Base Agent, Retrospective Drafter Agent)
  - ref: KANTATA-ENGINE-2025
    title: Kantata unveils the Kantata Expertise Engine (press release)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/kantata-unveils-the-kantata-expertise-engine-the-first-ai-platform-purpose-built-for-professional-services-transformation
    date: '2025-10-09'
    access: full
    locator: Paragraph on the continuous learning flywheel and the customer quote from FOIL
  - ref: KANTATA-AGENT-2026
    title: Expertise Agent and Workflows (product page) (page carries no publication date; date shown is the retrieval date)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/ai/expertise-agent-and-workflows
    date: '2026-10-19'
    access: full
    locator: Section on perfect project handoffs and institutional memory
  last_reviewed: '2026-10-19'
  notes: Product pages and press releases only. The Kantata Expertise Engine was in beta with select customers on 2025-10-09; whether it has since reached general availability was not confirmed.
- id: professional-services-knowledge-management-10
  title: Role-specific briefs from institutional memory when someone joins a live matter or project
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - research-synthesis
  - coordination-scheduling
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: A new lawyer or consultant joining a complex matter spends days reconstructing context that already exists in documents, emails and prior decisions.
  solution: 'An assistant that can search all matter documents summarises the matter and compares how similar matters were handled (Chaffetz Lindsey using Ask iManage). Platforms also propose automatic matter or project briefs: NetDocuments'' context graph produces a matter overview, and Kantata''s Expertise Agent produces a role-specific brief from SOWs, meeting notes and decisions.'
  outcomes:
  - lever: speed
    description: The firm's director says a new team member can be up to speed on an active trial in days rather than weeks; the story gives no measurement
    figure: days rather than weeks
    measures: Time to get a new team member up to speed on an active trial, as described in the iManage customer story (qualitative statement)
    provenance: vendor-published
    source_ref: IMANAGE-CHAFFETZ-2026
  prerequisites:
  - A matter-centric repository where all work product is filed (IMANAGE-CHAFFETZ-2026)
  - Per-user permissions and ethical walls that carry through to the brief (NETDOCUMENTS-CONTEXTGRAPH-2026)
  risks_and_guardrails:
  - The brief must not expose material behind an ethical wall; NetDocuments says the graph preserves permissions and walls (NETDOCUMENTS-CONTEXTGRAPH-2026)
  - No accuracy checks on generated matter summaries are published
  human_checkpoints:
  - The new team member still reads the key documents; the sources do not describe a formal check
  role_evolution: Not described.
  evidence_grade: B
  sources:
  - ref: IMANAGE-CHAFFETZ-2026
    title: Governance is a powerful differentiator at Chaffetz Lindsey (customer story) (page carries no publication date; date shown is the retrieval date)
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/chaffetz-lindsey/
    date: '2026-10-19'
    access: full
    locator: Paragraph beginning 'Ask iManage transformed how the firm finds and uses knowledge'
  - ref: NETDOCUMENTS-CONTEXTGRAPH-2026
    title: NetDocuments Unveils the First Context Graph for Legal Work (press release; read through the r.jina.ai mirror, direct curl returned 403)
    publisher: NetDocuments
    type: vendor
    url: https://www.netdocuments.com/company-news/netdocuments-unveils-context-graph-legal-platform/
    date: '2026-05-14'
    access: full
    locator: Paragraph on opening an unfamiliar matter and the bullet 'Every matter starts with clarity, not a blank page'
  - ref: KANTATA-AGENT-2026
    title: Expertise Agent and Workflows (product page) (page carries no publication date; date shown is the retrieval date)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/ai/expertise-agent-and-workflows
    date: '2026-10-19'
    access: full
    locator: Section 'Perfect Project Handoffs'
  last_reviewed: '2026-10-19'
  notes: Only the Chaffetz Lindsey item reports use in a named organisation, and it is a qualitative statement. NetDocuments' feature is in private preview (2026-05-14) and Kantata's is a product claim.
- id: professional-services-knowledge-management-11
  title: Pre-call customer research drawn from internal records, freeing customer-facing staff time (in-house services team)
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - research-synthesis
  - client-interaction
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Customer success managers at a software company's services organisation spent hours each day researching an account before each customer call.
  solution: A Kantata press release presents Basware's AI-enabled services approach as freeing customer success managers from research they used to do before customer calls. The release does not name the tool that now supports that research or say how it works.
  outcomes:
  - lever: capacity
    description: Basware's Chief Customer Officer says customer success managers who spent this long on research before a call now spend it on the phone, and that the capacity could let the company double revenue with its existing team
    figure: four to five hours a day
    measures: Hours a day customer success managers previously spent on research before a customer call, per a Kantata press release quoting Basware's Chief Customer Officer (recollection; no measurement method stated)
    provenance: vendor-published
    source_ref: KANTATA-BASWARE-2026
  prerequisites:
  - 'A services platform in place first: Basware began with automating billing before expanding to resourcing and delivery (KANTATA-BASWARE-2026)'
  risks_and_guardrails:
  - The release is a vendor press release; it does not tie the time saving to a named tool, and the double-revenue statement is the executive's view of what the capacity 'could' allow
  human_checkpoints:
  - Not described
  role_evolution: The release says managers shift from research to time on the phone with customers (KANTATA-BASWARE-2026).
  evidence_grade: B
  sources:
  - ref: KANTATA-BASWARE-2026
    title: Kantata takes Basware from AI experimentation to results (press release)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/kantata-takes-basware-from-ai-experimentation-to-results
    date: '2026-10-13'
    access: full
    locator: Section 'From Efficiency to Impact'
  last_reviewed: '2026-10-19'
  notes: Grade B because the figure is an executive's recollection in a vendor press release. The same release says an agent manages roughly half of 10,000 monthly support tickets from non-paying customers of Basware's customers; that is customer service, not this module.
- id: professional-services-knowledge-management-12
  title: Matter-and-document context graph that gives lawyers and agents firm-wide context
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: 'Flat retrieval finds passages, not relationships: an agent cannot tell which draft controls, that a counterparty is the same entity under another name, or which precedent is the firm''s most recent. Users re-explain the matter every session.'
  solution: A platform continuously maps how matters, documents, communications and people connect under existing permissions, and hands that structure to agents at run time (NetDocuments context graph; Harvey Graph and Spaces).
  outcomes:
  - lever: quality
    description: Harvey reports that agents with a context graph did better on its own agent benchmark and cost less per task; the figures are maxima across tasks
    figure: up to 30% higher rubric pass rate; up to ~50% lower task cost
    measures: Rubric pass rate and task cost for an agent with versus without a context graph on tasks from Harvey's Legal Agent Bench, as 'up to' values; number of tasks and averages are not given
    provenance: vendor-published
    source_ref: HARVEY-GRAPH-2026
  - lever: quality
    description: In one firm-knowledge task (find the firm's most recent secured financing and retrieve the executed agreements as precedents), the agent without the graph chose the wrong precedent and the agent with it found the right matter
    figure: 0% vs 75%
    measures: Share of rubric criteria met on a single Legal Agent Bench task, agent without versus with the context graph
    provenance: vendor-published
    source_ref: HARVEY-GRAPH-2026
  prerequisites:
  - Firm data in a platform that can infer and keep current relationships between versions, entities and matters across millions of documents (HARVEY-GRAPH-2026)
  - 'Governance: the graphs follow the Space''s security settings and ethical walls (HARVEY-GRAPH-2026; NETDOCUMENTS-CONTEXTGRAPH-2026)'
  risks_and_guardrails:
  - Harvey calls the results early and says it will keep publishing as experiments move into production (HARVEY-GRAPH-2026)
  - Relationships must be inferred, verified against the source and kept current as work changes (HARVEY-GRAPH-2026)
  - NetDocuments' platform opened in private preview on 14 May 2026; no customer results are reported (NETDOCUMENTS-CONTEXTGRAPH-2026)
  human_checkpoints:
  - Answers remain verifiable through citations (HARVEY-GRAPH-2026)
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: HARVEY-GRAPH-2026
    title: Improving agent accuracy with Harvey Graph
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/improving-agent-accuracy-with-harvey-graph
    date: '2026-10-19'
    access: full
    locator: Section on experiments on Legal Agent Bench (with and without the context graph)
  - ref: NETDOCUMENTS-CONTEXTGRAPH-2026
    title: NetDocuments Unveils the First Context Graph for Legal Work (press release; read through the r.jina.ai mirror, direct curl returned 403)
    publisher: NetDocuments
    type: vendor
    url: https://www.netdocuments.com/company-news/netdocuments-unveils-context-graph-legal-platform/
    date: '2026-05-14'
    access: full
    locator: Opening paragraphs and the bullet list of capabilities
  last_reviewed: '2026-10-19'
  notes: Both are vendor claims. Harvey says it will, over the coming months, launch precedent flags and cite checking for US case law and let firms define their own legal ontology on top of their documents (an announced plan).
- id: professional-services-knowledge-management-13
  title: 'Knowledge teams curate the firm''s AI know-how: approved tools, use cases, playbooks and practice-group leads'
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - coordination-scheduling
  - research-synthesis
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: 'AI adoption is uneven inside a firm: Troutman Pepper Locke noticed inconsistencies in who adopted AI and how much value they extracted.'
  solution: Knowledge management is applied to AI itself. Troutman Pepper Locke curates a list of approved AI tools, best practices, use cases and lessons learned in one repository, backed by a knowledge management and AI partner in each practice group (created first in its private equity group). Lewis Silkin put knowledge lawyers at the front of adoption, with a Harvey lead per team. Ropes & Gray built one-page tech stacks per practice group with its legal KM team. Gowling WLG's national director of AI, innovation and knowledge leads practice technology, knowledge, library and applied AI teams and says the aim is durable playbooks, prompt patterns and repeatable workflows.
  outcomes:
  - lever: quality
    description: No measured outcome is published for these programmes
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: TROUTMAN-KM-2026
  prerequisites:
  - Responsible-use policies and required training before attorneys use AI tools (TROUTMAN-KM-2026)
  - An AI task force and innovation committee that test tools (TROUTMAN-KM-2026)
  - Practice-group champions or leads who share use cases (HARVEY-LEWISSILKIN-2025)
  risks_and_guardrails:
  - Troutman Pepper Locke says it wants 'no laggards, and no leaders' inside each practice (TROUTMAN-KM-2026)
  - Lewis Silkin says it treats the rollout as a big experiment without a fixed view of the end state (HARVEY-LEWISSILKIN-2025)
  human_checkpoints:
  - Practice-group knowledge partners and leads decide which tools, use cases and playbooks become firm guidance
  role_evolution: 'New or widened roles: a knowledge management and AI partner in the private equity group (TROUTMAN-KM-2026); knowledge lawyers building AI workflows and acting as Harvey leads (HARVEY-LEWISSILKIN-2025); a national director spanning AI, innovation and knowledge (HARVEY-GOWLING-2025). ILTA reports firms anticipate added headcount across IT, innovation, security, training, knowledge management and data science (ILTA-TECHSURVEY-2026).'
  evidence_grade: B
  sources:
  - ref: TROUTMAN-KM-2026
    title: 'A merger of the minds: the role of knowledge management in AI adoption'
    publisher: Troutman Pepper Locke
    type: firm
    url: https://www.troutman.com/insights/a-merger-of-the-minds-the-role-of-knowledge-management-in-ai-adoption/
    date: '2026-04-29'
    access: full
    locator: Paragraphs on the knowledge management and AI partner and the repository of AI knowledge
  - ref: HARVEY-LEWISSILKIN-2025
    title: Alex Bazin (Lewis Silkin) on empowering teams with legal AI (Innovation Spotlight interview)
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/alex-bazin-on-empowering-teams-with-legal-ai
    date: '2025-11-27'
    access: full
    locator: Answers on adoption approach (Knowledge Lawyers front and centre; Harvey Leads)
  - ref: HARVEY-ROPES-2025
    title: Theresa Spartichino (Ropes & Gray) on driving innovation (Innovation Spotlight interview)
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/theresa-spartichino-on-driving-innovation
    date: '2025-10-02'
    access: full
    locator: Answer on practice-specific training and the one-page tech stacks created with Legal KM
  - ref: HARVEY-GOWLING-2025
    title: Al Hounsell (Gowling WLG) on driving legal transformation that lasts (Innovation Spotlight interview)
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/al-hounsell-on-driving-legal-transformation-that-lasts
    date: '2025-10-30'
    access: full
    locator: Biography and the answers on playbooks, prompt patterns and adoption
  - ref: ILTA-TECHSURVEY-2026
    title: The ILTA Technology Survey 2026 executive summary (PDF)
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: Page 5, staffing implications paragraph
  last_reviewed: '2026-10-19'
  notes: 'The pattern is ''other'': knowledge capture and sharing about AI practice (what works, who may use what). The Harvey interviews are vendor-published but are the named firms'' own statements.'
- id: professional-services-knowledge-management-14
  title: 'AI-assisted repository clean-up: find duplicates, rename and reorganise files with human confirmation'
  archetype: professional-services
  module: knowledge-management
  function: technology-it
  work_types:
  - data-reporting
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Documents scattered across inboxes, desktops, OneDrive, SharePoint and file servers leave no single authoritative version; incoming data rooms and productions arrive with inconsistent or numeric file names.
  solution: An in-house team at Digital Commerce Bank uses Ask iManage to find all duplicates of a document so librarians can file them correctly and delete the extras, and to find what is missing. Harvey's Agentic Vault Organization (early access) proposes a folder or renaming plan in plain language, shows exactly what it will change, and acts only after a person confirms, with undo.
  outcomes:
  - lever: capacity
    description: Ask iManage is live with a small group at the bank and is planned for the whole user base
    figure: roughly 10 users now; 70 planned
    measures: Users of Ask iManage in legal and technology at Digital Commerce Bank versus the bank's 70-user base, per the vendor case study
    provenance: vendor-published
    source_ref: IMANAGE-DCB-2026
  prerequisites:
  - A single governed platform and a new file structure to organise into (IMANAGE-DCB-2026)
  - 'For Harvey: documents in a Vault; the organisation feature is early access (HARVEY-VAULT-2026)'
  risks_and_guardrails:
  - Harvey says the agent can move, rename and tag files but never edits their content and never runs a change without a person confirming it; the most recent changes can be undone (HARVEY-VAULT-2026)
  - Librarians control governance of AI use on the bank's repository (IMANAGE-DCB-2026)
  human_checkpoints:
  - Librarians file and delete duplicates (IMANAGE-DCB-2026)
  - A person confirms the proposed reorganisation plan (HARVEY-VAULT-2026)
  role_evolution: Librarians move from finding duplicates by hand to directing and approving the assistant's findings (IMANAGE-DCB-2026).
  evidence_grade: B
  sources:
  - ref: IMANAGE-DCB-2026
    title: Digital Commerce Bank unifies diverse teams on one platform (customer story) (page carries no publication date; date shown is the retrieval date)
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/digital-commerce-bank/
    date: '2026-10-19'
    access: full
    locator: Paragraphs on Ask iManage use for duplicates and repository state
  - ref: HARVEY-VAULT-2026
    title: Agentic Vault Search and Organization
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/agentic-vault-search-and-organization
    date: '2026-09-08'
    access: full
    locator: Sections on Agentic Vault Organization
  last_reviewed: '2026-10-19'
  notes: Digital Commerce Bank is an in-house technology and legal team in a bank (in-house). Harvey's organisation feature is early access (not general availability), and Harvey's search feature is generally available.
- id: professional-services-knowledge-management-15
  title: 'Reuse of past engagements: credentials, case studies and risks assembled from firm history for proposals'
  archetype: professional-services
  module: knowledge-management
  function: sales-marketing-bd
  work_types:
  - document-production
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Too much expertise is locked in decks or in consultants' heads, so each proposal starts mostly from scratch.
  solution: 'The firm''s own history of proposals, projects and outcomes feeds proposal assembly: Kantata''s Sales Accelerator (planned for early 2026) was announced to turn delivery history into proposals that highlight case studies, risks and human-AI resource mixes within minutes of an RFP; Intapp DealCloud searches lawyer, engagement and client experience and generates pitch documents; Certinia lists an RFP responder agent.'
  outcomes:
  - lever: speed
    description: A consulting customer in the Kantata launch release says its experience becomes reusable and 'proposals practically build themselves'; no measurement
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: KANTATA-ENGINE-2025
  prerequisites:
  - Structured history of proposals, projects and outcomes in the platform (KANTATA-ENGINE-2025)
  - Experience data connected to HR and financial systems (INTAPP-EXPERIENCE-2026)
  risks_and_guardrails:
  - No source discusses the risk of reusing confidential client material in proposals; confidentiality screening is not described
  human_checkpoints:
  - Not described in the sources
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: KANTATA-ENGINE-2025
    title: Kantata unveils the Kantata Expertise Engine (press release)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/kantata-unveils-the-kantata-expertise-engine-the-first-ai-platform-purpose-built-for-professional-services-transformation
    date: '2025-10-09'
    access: full
    locator: Paragraphs on the Sales Accelerator and the customer quote from FOIL
  - ref: INTAPP-EXPERIENCE-2026
    title: Experience management (Intapp DealCloud product page) (page carries no publication date; date shown is the retrieval date)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/dealcloud/experience-management/
    date: '2026-10-19'
    access: full
    locator: Section on proposal and report generation
  - ref: CERTINIA-VEDA-2026
    title: Certinia Veda AI agents for professional services (product page) (page carries no publication date; date shown is the retrieval date)
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: Section 'Seamless sales, handoff & alignment'
  last_reviewed: '2026-10-19'
  notes: Belongs mainly to pursuit-proposals; kept here as reuse of past work. The Kantata Expertise Engine was in beta with select customers on 2025-10-09, with the first accelerators planned for early 2026; delivery of that plan was not confirmed.
- id: professional-services-knowledge-management-16
  title: (idea) Capture senior experts' judgement in assistants so junior staff work from it
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Judgement sits in senior people's heads and walks out when they leave; NetDocuments frames this as a senior lawyer retiring and decades of judgment and precedent leaving with them.
  solution: 'Idea discussed by practitioners: assistants trained on what the best people know so that others can apply their patterns. Basware''s Chief Customer Officer describes wanting to make ''what our best people know'' available across every project and customer; Digital Commerce Bank''s CTO describes junior staff drawing on AI trained by senior colleagues.'
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: KANTATA-BASWARE-2026
  prerequisites:
  - Not established in the sources for professional services
  risks_and_guardrails:
  - No source describes how a firm would validate, keep current or attribute captured expert judgement
  human_checkpoints:
  - Not described
  role_evolution: Senior staff would become the source of the captured judgement; sources do not describe a deployed role change.
  evidence_grade: D
  sources:
  - ref: KANTATA-BASWARE-2026
    title: Kantata takes Basware from AI experimentation to results (press release)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/kantata-takes-basware-from-ai-experimentation-to-results
    date: '2026-10-13'
    access: full
    locator: Section 'Where AI Meets Expertise' (Chief Customer Officer quote)
  - ref: NETDOCUMENTS-CONTEXTGRAPH-2026
    title: NetDocuments Unveils the First Context Graph for Legal Work (press release; read through the r.jina.ai mirror, direct curl returned 403)
    publisher: NetDocuments
    type: vendor
    url: https://www.netdocuments.com/company-news/netdocuments-unveils-context-graph-legal-platform/
    date: '2026-05-14'
    access: full
    locator: Paragraph on the senior lawyer who retires
  - ref: IMANAGE-DCB-2026
    title: Digital Commerce Bank unifies diverse teams on one platform (customer story) (page carries no publication date; date shown is the retrieval date)
    publisher: iManage
    type: vendor
    url: https://imanage.com/resources/customer-stories/digital-commerce-bank/
    date: '2026-10-19'
    access: full
    locator: Final sentence of the Ask iManage governance paragraph (CTO ambition)
  - ref: NBER-BRYNJOLFSSON-2023
    title: Generative AI at Work (NBER Working Paper 31161)
    publisher: National Bureau of Economic Research
    type: academic
    url: https://www.nber.org/papers/w31161
    date: 2023-04
    access: full
    locator: 'Abstract: the AI model disseminates the best practices of more able workers; customer-support setting'
  last_reviewed: '2026-10-19'
  notes: 'Idea. Adjacent measured evidence (grade cap B, not met for this module): in a study of 5,179 customer-support agents at one firm, access to a generative AI assistant raised issues resolved per hour by 14 percent on average and 34 percent for novice and low-skilled workers, with minimal impact on experienced workers; the authors give suggestive evidence that the model disseminates best practices of more able workers (NBER-BRYNJOLFSSON-2023). That is customer support, not professional services.'
```

## 3. Module notes

### Processes and key steps (with work types)

1. **Capture and curate**: take precedents, know-how and engagement outputs into a library; classify, summarise, tag, retire. Work types: research-synthesis, data-reporting. Examples: Allens' knowledge team and curated library (IMANAGE-ALLENS-2026); McKinsey data stewards who curate, check accuracy and sanitise for client confidentiality (MCKINSEY-LILLI-2023); Clifford Chance's reclassification and summary of 400,000+ documents (ARTIFICIALLAWYER-CLIFFORDCHANCE-2026).
2. **Organise and govern**: taxonomy, metadata, permissions, ethical walls, AI-processing flags. Work types: data-reporting, review-assurance. Examples: Womble Bond Dickinson's curated knowledge profile with confidentiality, client and AI-processing tags (IMANAGE-WOMBLE-2026); Chaffetz Lindsey, where more than 35 percent of matters carry ethical screens (IMANAGE-CHAFFETZ-2026).
3. **Find and retrieve**: search, ask a question of documents, locate an expert or comparable. Work type: research-synthesis. Examples: use cases 01, 02, 03, 04, 06.
4. **Reuse and apply**: benchmark terms against deal history, ground drafts in approved precedents, assemble proposals from past engagements. Work types: document-production, data-reporting. Use cases 07, 08, 15 (drafting itself is routed to work-production).
5. **Transfer and onboard**: matter or project briefs, handoffs, retrospectives. Work types: coordination-scheduling, research-synthesis. Use cases 09, 10.
6. **Maintain and measure**: de-duplicate, rename, retire; analyse what people search for and what is not surfacing. Work type: data-reporting. Use case 14; search analytics are planned by an unnamed global firm (IMANAGE-EMEAFIRM-2026).

### Common pain points

- Findability: lawyers cannot find the precedent they want quickly (IMANAGE-ALLENS-2026); a document saved is sometimes not found later and search results are inconsistent (IMANAGE-BICALHO-2026).
- Fragmentation: documents spread across inboxes, desktops, OneDrive, SharePoint and file servers (IMANAGE-DCB-2026).
- Tacit knowledge: engagement kickoff research and expert networking described as two weeks even for senior colleagues at McKinsey (MCKINSEY-LILLI-2023); a senior lawyer's judgment leaving on retirement (NETDOCUMENTS-CONTEXTGRAPH-2026).
- Weak knowledge infrastructure: ILTA's 2026 summary says it remains dramatically underdeveloped across enterprise search, expertise management, pricing, procurement and competitive intelligence (ILTA-TECHSURVEY-2026, page 9).
- Staff turnover in project-based firms: architecture and engineering firms report turnover above 13 percent (DELTEK-CLARITY-2026), which raises the cost of knowledge that lives in people.
- Content quality: AI cannot be assumed to distinguish good from poor content (IMANAGE-WOMBLE-2026).

### Metrics and benchmarks (with sources)

- **Spend.** Law firms raised technology spend by nearly 11 percent and knowledge management spend by about 10 percent in 2025; over 2021 to 2025, technology spend rose 39.3 percent and KM investment 37.2 percent, measured against 2021 levels (TRI-SOTLM-2026). Thomson Reuters Institute's own framing is that the winners may be those who deploy strategically rather than those who spend most.
- **Staffing intent.** ILTA's 2026 survey (508 firms) says many firms anticipate added headcount across IT, innovation, security, training, knowledge management and data science (ILTA-TECHSURVEY-2026, page 5). The share naming KM was not extractable from the executive summary.
- **Maturity and governance (cross-industry knowledge work, vendor-published survey).** iManage's 2026 benchmark reports: 85 percent of organisations at some stage of AI adoption; 27 percent fully integrated and widely used AI among top-maturity organisations versus 3 percent among the least mature; 36 percent report a policy violation; 25 percent say end users use public AI with little oversight; 20 percent report security-driven adoption delays (IMANAGE-BENCH-2026). It is not specific to professional services or to KM outcomes.
- **Task accuracy on supplied documents (adjacent, independent).** In Vals' February 2025 benchmark, Document Q&A scores were 94.8 percent for Harvey Assistant and 89.6 percent for CoCounsel, against a lawyer baseline of 70.1 percent; the average across tools was 80.2 percent. These measure answering from documents handed to the tool, not finding the right document in a firm-wide estate, so they cap related grades at B (VALS-VLAIR-2025).
- **Usage at one consultancy.** Over 75 percent of McKinsey's 43,000 employees use Lilli monthly, average use 17 times a week, 500,000+ prompts a month, 30 percent time saved on gathering and synthesising information, relayed second hand from a Bloomberg interview; no method given for the 30 percent (THEOUTPOST-LILLI-2025).
- **Vendor-run agent evaluation.** Harvey reports up to 30 percent higher rubric pass rate and up to about 50 percent lower task cost when agents use a context graph, on its own Legal Agent Bench (HARVEY-GRAPH-2026). The number of tasks is not given.
- **Quality evidence for KM retrieval.** None found: no published error rates, override rates, parallel runs against manual search, or inspection findings. The only independent benchmark (Vals) is adjacent. Harvey's and iManage's figures are vendor-published.

### Guardrails and regulatory points

- **Permissions carry through.** Harvey's search uses each person's permissions in the connected system (HARVEY-AGENTICSEARCH-2026); the Harvey agent applies ethical walls and Vault permissions and logs every file it touches (HARVEY-VAULT-2026); iManage permissions decide what a connected tool can retrieve (LEGORA-IMANAGE-2026); NetDocuments says its graph preserves permissions and ethical walls (NETDOCUMENTS-CONTEXTGRAPH-2026); Clifford Chance's Permissioned Search applies metadata-driven permissions aligned with client confidentiality (ARTIFICIALLAWYER-CLIFFORDCHANCE-2026).
- **AI-processing flags.** Womble Bond Dickinson plans client and matter-level AI-processing permissions inherited by documents, so tools connecting by MCP surface only authorised content (IMANAGE-WOMBLE-2026). The capability depended on iManage making it available when the story was published.
- **Client data stays inside.** McKinsey permits confidential client data in Lilli but not in public AI tools (THEOUTPOST-LILLI-2025); Chaffetz Lindsey wants tools to reach in rather than pull content out (IMANAGE-CHAFFETZ-2026).
- **Shadow AI.** 25 percent of organisations in iManage's benchmark say end users use public AI with little oversight; 36 percent report a policy violation (IMANAGE-BENCH-2026).
- **Human confirmation for changes.** Harvey's repository reorganisation acts only after a person confirms and can be undone (HARVEY-VAULT-2026).
- No regulator or professional-body statement specific to knowledge management was opened for this angle; the governance angle covers professional-conduct guidance.

### Frontier signals (dated, sourced)

- 2026-10-19: Harvey says it will, over the coming months, launch precedent flags and cite checking for US case law and let firms define their own legal ontology on documents (HARVEY-GRAPH-2026).
- 2026-10-16: Legora announces a connection to the iManage MCP Server so lawyers can draw on firm knowledge and document history inside Legora (LEGORA-IMANAGE-2026).
- 2026-10-15: Microsoft Copilot for Legal is reported to draw on approved precedents stored in SharePoint when drafting (LAWSITES-MSFT-2026).
- 2026-09-30: Harvey says cross-system agentic search (iManage, SharePoint, Google Drive) is available now (HARVEY-AGENTICSEARCH-2026).
- 2026-07-20: Clifford Chance announces its Knowledge Bank (ARTIFICIALLAWYER-CLIFFORDCHANCE-2026; LAW360-CLIFFORDCHANCE-2026, lead only).
- 2026-05-14: NetDocuments introduces a context graph in private preview; Claude and ChatGPT are named as external tools reaching it via MCP (NETDOCUMENTS-CONTEXTGRAPH-2026).
- 2026-03 (EDRM preview dated 2026-03-06): Legalweek 2026 sessions held on 11 March included "The New Data Reality: What Agentic AI Can Infer & What KM Must Still Control" and "Designing a Legal Data Ecosystem: KM, DMS, and LLMs in Harmony" (EDRM-LEGALWEEK-2026; session descriptions are the EDRM author's, not the speakers').
- 2025-12-08: A vendor executive forecasts that conversational AI agents become the main interface to knowledge systems, with MCP as the connector and professional support lawyers reviewing AI classification (KMWORLD-LEXSOFT-2025; SOLICITORSJOURNAL-KM-2025). This is a forecast, not evidence of use.
- 2025-10-09 and 2026-06-16: Kantata positions an Expertise Engine and a single Expertise Agent that capture institutional knowledge across engagements (KANTATA-ENGINE-2025; KANTATA-SUPERAGENT-2026).

### Workforce and role effects

- A knowledge management and AI partner role created in the private equity group at Troutman Pepper Locke in 2026 (TROUTMAN-KM-2026).
- Knowledge lawyers lead AI adoption at Lewis Silkin (a Harvey lead per team) and build AI workflows (HARVEY-LEWISSILKIN-2025).
- Gowling WLG's national director of AI, innovation and knowledge leads practice technology, knowledge and practice support, library and information services, and applied AI teams (HARVEY-GOWLING-2025).
- McKinsey's existing data stewards are central to Lilli's content quality (MCKINSEY-LILLI-2023).
- Non-timekeeping staff became champions at Chaffetz Lindsey (IMANAGE-CHAFFETZ-2026); lawyer champions drive adoption at Allens (IMANAGE-ALLENS-2026).
- Forecast: professional support lawyers shift to quality guardians of AI-generated classification (KMWORLD-LEXSOFT-2025).
- McKinsey's technology leader says AI may take over analyst tasks such as slide production without necessarily reducing analyst numbers (THEOUTPOST-LILLI-2025). The junior-skills effect is routed to talent-learning.

### Objections and concerns practitioners raise

- Path of least resistance: lawyers may use whatever is easiest rather than the best-practice template (IMANAGE-ALLENS-2026).
- Content quality: AI does not tell good from bad content, so metadata governance is essential (IMANAGE-WOMBLE-2026).
- Data leaving the organisation uncontrolled is the main AI risk named by an in-house team (IMANAGE-DCB-2026).
- Cost versus capability: an anonymous in-house legal operations team declined an expensive AI module with limited out-of-the-box features (IMANAGE-LEGALOPS-2026).
- Hype and returns: Thomson Reuters Institute warns of AI-bubble risk and says winners may be those who deploy strategically (TRI-SOTLM-2026); 38 percent of architecture and engineering respondents report measurable positive AI impact (DELTEK-CLARITY-2026).
- Fast, generic answers: Kantata's CEO warns of firms running toward "fast, mediocre decisions" when AI lacks firm context (KANTATA-SUPERAGENT-2026). This is a vendor position.
- Adoption unevenness inside a firm (TROUTMAN-KM-2026).

### Interview probes for an advisor

1. Who owns each part of your precedent and know-how library (owner, review date, retirement rule), and what is the backlog of uncurated material that an assistant would still be able to retrieve?
2. When someone asks "have we done this before?", how is that answered today, and how would you know an AI answer had missed the best precedent or the right expert? (Ask what they measure: failed searches, user overrides, reuse rates.)
3. How do ethical walls, client restrictions and AI-processing permissions apply to what an assistant or outside AI tool can retrieve, and who audits it?
4. What knowledge leaves with people today (retirements, lateral moves, engagement end), and what would you be willing to capture into an assistant?
5. How have knowledge, library and professional support lawyer roles and headcount changed in the last 12 months, and who now signs off AI-generated classification or summaries?

## 4. Routed to other modules

- **work-production**: precedent-grounded first drafts (Microsoft Copilot for Legal drawing on approved precedents in SharePoint, LAWSITES-MSFT-2026; BMW's first drafts from approved standards, LEGORA-BMW-2026); Harvey Review Tables for term extraction (HARVEY-INDEMNITY-2026); Vals task benchmarks (VALS-VLAIR-2025).
- **pursuit-proposals**: proposal assembly from past engagements (Kantata Sales Accelerator, Intapp experience-based pitch generation, Certinia RFP Responder; see use case 15).
- **staffing-resourcing**: Kantata Expertise Agent's ranked staffing recommendations with reasoning; its claim of a 40% improvement in resource planning accuracy is an unmeasured vendor figure on the product page (KANTATA-AGENT-2026).
- **delivery-management**: Kantata's portfolio-health monitoring and Certinia's project assistant and PMO agents (KANTATA-AGENT-2026; CERTINIA-VEDA-2026).
- **talent-learning**: McKinsey's remarks on junior tasks (THEOUTPOST-LILLI-2025); NBER WP 35720 on seniors versus juniors (listed in the landscape file; not opened here); Harvey Academy and training programmes; ILTA's headcount intent (ILTA-TECHSURVEY-2026).
- **quality-review**: independent benchmark design (VALS-VLAIR-2025); Basware's support-ticket agent result belongs to customer service, not this archetype (KANTATA-BASWARE-2026).
- **acceptance-risk**: ethical-wall management and conflicts (35 percent of matters screened at Chaffetz Lindsey, IMANAGE-CHAFFETZ-2026).
- **firm-finance**: KM and technology spend growth (TRI-SOTLM-2026).

## 5. Sources

Single list of the 44 sources opened for this angle. `access: full` means opened and read; the one `search-only` item (Law360) showed only a lead paragraph. Types follow the vocabulary.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| NBER-BRYNJOLFSSON-2023 | Generative AI at Work (NBER Working Paper 31161) | National Bureau of Economic Research | academic | https://www.nber.org/papers/w31161 | 2023-04 | full |
| EDRM-LEGALWEEK-2026 | Legalweek 2026 (select) educational sessions preview (read through the r.jina.ai mirror; direct curl returned 403) | EDRM | conference | https://edrm.net/2026/03/legalweek-2026-select-educational-sessions-preview/ | 2026-03-06 | full |
| MCKINSEY-LILLI-2023 | Meet Lilli, our generative AI tool that's a researcher, a time saver, and an inspiration (alumni-site copy of the firm announcement; read through the r.jina.ai mirror, direct curl failed; date taken from the URL slug 2023-10) | McKinsey & Company | firm | https://www.mckinsey.com/alumni/news-and-events/global-news/firm-news/2023-10-lilli | 2023-10 | full |
| TROUTMAN-KM-2026 | A merger of the minds: the role of knowledge management in AI adoption | Troutman Pepper Locke | firm | https://www.troutman.com/insights/a-merger-of-the-minds-the-role-of-knowledge-management-in-ai-adoption/ | 2026-04-29 | full |
| ARTIFICIALLAWYER-CLIFFORDCHANCE-2026 | Clifford Chance launches AI KM platform with Microsoft and Epiq | Artificial Lawyer | press | https://artificiallawyer.com/2026/07/20/clifford-chance-launches-ai-km-platform-with-microsoft-epiq | 2026-07-20 | full |
| KMWORLD-LEXSOFT-2025 | Conversational AI interfaces and human-AI collaboration to transform legal knowledge management in 2026 (viewpoint by the CEO of Lexsoft Systems, a legal-sector software vendor) | KMWorld | press | https://www.kmworld.com/Articles/Editorial/ViewPoints/Conversational-AI-interfaces-and-human-AI-collaboration-to-transform-legal-knowledge-management-in-2026-172705.aspx | 2025-12-08 | full |
| LAW360-CLIFFORDCHANCE-2026 | Clifford Chance launches AI knowledge management tech (lead paragraph only; remainder paywalled) | Law360 | press | https://www.law360.com/articles/2503174 | 2026-07-20 | search-only |
| LAWSITES-MSFT-2026 | Microsoft launches Copilot for Legal, becoming the fourth AI giant in five months to build out a legal vertical | LawSites (LawNext) | press | https://www.lawnext.com/2026/10/microsoft-launches-copilot-for-legal-becoming-the-fourth-ai-giant-in-five-months-to-build-out-a-legal-vertical.html | 2026-10-15 | full |
| MAGINATIVE-LILLI-2023 | McKinsey unveils Lilli, its own generative AI assistant | Maginative | press | https://www.maginative.com/article/mckinsey-unveils-lilli-its-own-generative-ai-assistant/ | 2023-08-16 | full |
| SOLICITORSJOURNAL-KM-2025 | How AI will redefine legal knowledge management in 2026 (same author and argument as the KMWorld viewpoint) | Solicitors Journal | press | https://solicitorsjournal.com/sjarticle/how-ai-will-redefine-legal-knowledge-management-in-2026 | 2025-12-09 | full |
| THEOUTPOST-LILLI-2025 | McKinsey embraces AI for consulting tasks, transforming junior roles (aggregator summary of a Bloomberg interview with McKinsey's technology and AI leader) | TheOutpost.ai | press | https://theoutpost.ai/news-story/mc-kinsey-embraces-ai-for-consulting-tasks-transforming-junior-roles-16077/ | 2025-06-03 | full |
| DELTEK-CLARITY-2026 | The latest Deltek Clarity industry studies highlight AI challenges, talent strain, and delivery capacity pressures | Deltek | survey | https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/ | 2026-05-12 | full |
| ILTA-TECHSURVEY-2026 | The ILTA Technology Survey 2026 executive summary (PDF) | International Legal Technology Association | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 | full |
| IMANAGE-BENCH-2026 | iManage Knowledge Work Benchmark Report 2026 (landing page with executive summary) | iManage | survey | https://imanage.com/benchmark-report-2026/ | 2026 | full |
| TRI-SOTLM-2026 | State of the US Legal Market 2026 analysis: will the AI bubble burst? | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble | 2026-01-14 | full |
| VALS-VLAIR-2025 | Vals Legal AI Report (VLAIR) | Vals AI | survey | https://www.vals.ai/vlair | 2025-02 | full |
| CERTINIA-VEDA-2026 | Certinia Veda AI agents for professional services (product page) (page carries no publication date; date shown is the retrieval date) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10-19 | full |
| HARVEY-AGENTICSEARCH-2026 | Introducing Agentic Search for Your Document Systems | Harvey | vendor | https://www.harvey.ai/blog/agentic-search-document-management-systems | 2026-09-30 | full |
| HARVEY-GOWLING-2025 | Al Hounsell (Gowling WLG) on driving legal transformation that lasts (Innovation Spotlight interview) | Harvey | vendor | https://www.harvey.ai/blog/al-hounsell-on-driving-legal-transformation-that-lasts | 2025-10-30 | full |
| HARVEY-GRAPH-2026 | Improving agent accuracy with Harvey Graph | Harvey | vendor | https://www.harvey.ai/blog/improving-agent-accuracy-with-harvey-graph | 2026-10-19 | full |
| HARVEY-INDEMNITY-2026 | Benchmarking an indemnification clause against your own deal history | Harvey | vendor | https://www.harvey.ai/blog/indemnification-clauses-against-deal-history | 2026-09-25 | full |
| HARVEY-INHOUSE-2026 | Building a frontier in-house organization | Harvey | vendor | https://www.harvey.ai/blog/building-a-frontier-in-house-organization | 2026-10-13 | full |
| HARVEY-LEWISSILKIN-2025 | Alex Bazin (Lewis Silkin) on empowering teams with legal AI (Innovation Spotlight interview) | Harvey | vendor | https://www.harvey.ai/blog/alex-bazin-on-empowering-teams-with-legal-ai | 2025-11-27 | full |
| HARVEY-ROPES-2025 | Theresa Spartichino (Ropes & Gray) on driving innovation (Innovation Spotlight interview) | Harvey | vendor | https://www.harvey.ai/blog/theresa-spartichino-on-driving-innovation | 2025-10-02 | full |
| HARVEY-VAULT-2026 | Agentic Vault Search and Organization | Harvey | vendor | https://www.harvey.ai/blog/agentic-vault-search-and-organization | 2026-09-08 | full |
| IMANAGE-ALLENS-2026 | Allens taps into goldmine of enterprise knowledge with Insight+ (customer story) (page carries no publication date; date shown is the retrieval date) | iManage | vendor | https://imanage.com/resources/customer-stories/allens-insightplus/ | 2026-10-19 | full |
| IMANAGE-BICALHO-2026 | Bicalho Navarro Advogados: greater trust in knowledge search results in the iManage Cloud (customer story) (page carries no publication date; date shown is the retrieval date) | iManage | vendor | https://imanage.com/resources/customer-stories/bicalho-navarro/ | 2026-10-19 | full |
| IMANAGE-CHAFFETZ-2026 | Governance is a powerful differentiator at Chaffetz Lindsey (customer story) (page carries no publication date; date shown is the retrieval date) | iManage | vendor | https://imanage.com/resources/customer-stories/chaffetz-lindsey/ | 2026-10-19 | full |
| IMANAGE-DCB-2026 | Digital Commerce Bank unifies diverse teams on one platform (customer story) (page carries no publication date; date shown is the retrieval date) | iManage | vendor | https://imanage.com/resources/customer-stories/digital-commerce-bank/ | 2026-10-19 | full |
| IMANAGE-EMEAFIRM-2026 | Global law firm, EMEA region: Insight+ replaces an in-house knowledge platform (customer story, firm unnamed) (page carries no publication date; date shown is the retrieval date) | iManage | vendor | https://imanage.com/resources/customer-stories/global-law-firm-emea-region/ | 2026-10-19 | full |
| IMANAGE-LEGALOPS-2026 | Global legal operations customer (iManage customer story, organisation unnamed) (page carries no publication date; date shown is the retrieval date) | iManage | vendor | https://imanage.com/resources/customer-stories/global-legal-operations-customer/ | 2026-10-19 | full |
| IMANAGE-REGULATOR-2026 | Independent regulatory body: Insight+ for a precedent library (customer story, organisation unnamed) (page carries no publication date; date shown is the retrieval date) | iManage | vendor | https://imanage.com/resources/customer-stories/independent-regulatory-body/ | 2026-10-19 | full |
| IMANAGE-RIOTINTO-2026 | Rio Tinto makes institutional knowledge more accessible and actionable with iManage (customer story) (page carries no publication date; date shown is the retrieval date) | iManage | vendor | https://imanage.com/resources/customer-stories/rio-tinto/ | 2026-10-19 | full |
| IMANAGE-SEYFARTH-2026 | Seyfarth Shaw (iManage customer story) (page carries no publication date; date shown is the retrieval date) | iManage | vendor | https://imanage.com/resources/customer-stories/seyfarth-shaw/ | 2026-10-19 | full |
| IMANAGE-WOMBLE-2026 | Womble Bond Dickinson UK lays an AI-ready foundation (customer story) (page carries no publication date; date shown is the retrieval date) | iManage | vendor | https://imanage.com/resources/customer-stories/womble-bond/ | 2026-10-19 | full |
| INTAPP-EXPERIENCE-2026 | Experience management (Intapp DealCloud product page) (page carries no publication date; date shown is the retrieval date) | Intapp | vendor | https://www.intapp.com/dealcloud/experience-management/ | 2026-10-19 | full |
| KANTATA-AGENT-2026 | Expertise Agent and Workflows (product page) (page carries no publication date; date shown is the retrieval date) | Kantata | vendor | https://www.kantata.com/ai/expertise-agent-and-workflows | 2026-10-19 | full |
| KANTATA-BASWARE-2026 | Kantata takes Basware from AI experimentation to results (press release) | Kantata | vendor | https://www.kantata.com/blog/article/kantata-takes-basware-from-ai-experimentation-to-results | 2026-10-13 | full |
| KANTATA-ENGINE-2025 | Kantata unveils the Kantata Expertise Engine (press release) | Kantata | vendor | https://www.kantata.com/blog/article/kantata-unveils-the-kantata-expertise-engine-the-first-ai-platform-purpose-built-for-professional-services-transformation | 2025-10-09 | full |
| KANTATA-SUPERAGENT-2026 | More agents won't fix unpredictable projects: why we built a superagent instead | Kantata | vendor | https://www.kantata.com/blog/article/more-agents-wont-fix-unpredictable-projects-why-we-built-a-superagent-instead | 2026-06-16 | full |
| LEGORA-BMW-2026 | Legora collaborates with BMW Group to advance AI-enabled legal services | Legora | vendor | https://legora.com/newsroom/legora-collaborates-with-bmw-group-to-advance-ai-enabled-legal-services | 2026-10-08 | full |
| LEGORA-IMANAGE-2026 | Legora and iManage deepen integration through iManage MCP Server | Legora | vendor | https://legora.com/newsroom/legora-and-imanage-deepen-integration-through-imanage-mcp-server | 2026-10-16 | full |
| NETDOCUMENTS-CONTEXTGRAPH-2026 | NetDocuments Unveils the First Context Graph for Legal Work (press release; read through the r.jina.ai mirror, direct curl returned 403) | NetDocuments | vendor | https://www.netdocuments.com/company-news/netdocuments-unveils-context-graph-legal-platform/ | 2026-05-14 | full |
| NETDOCUMENTS-NDMAX-2026 | ndMAX legal AI suite (product page) (page carries no publication date; date shown is the retrieval date) | NetDocuments | vendor | https://www.netdocuments.com/ndmax | 2026-10-19 | full |

## 6. Gaps

- **Web search budget.** The shared web-search allowance ran out after four searches (McKinsey Lilli twice, law-firm KM rollouts, Clifford Chance). A fifth search on architecture and engineering knowledge systems was refused. Remaining sources came from direct fetches of vendor, firm and news pages and the landscape's leads.
- **Job postings: none obtained.** LinkedIn was blocked through the text mirror, and probes of public Greenhouse and Lever job-board endpoints for several firms returned no usable listings. Roles are evidenced only from interviews and articles.
- **Consulting beyond McKinsey.** BCG, Bain, Deloitte, EY, KPMG, PwC and Accenture internal knowledge tools were not reached (KPMG blocked the text mirror; guessed press URLs for EY, PwC and Bain returned errors). McKinsey's own current-usage figures could not be read at source (mckinsey.com returned 403 or a stream error to curl; only the 2023 alumni-site copy opened through the mirror); the 2025 figures come from a secondary summary of a Bloomberg interview.
- **Accounting and engineering.** No named accounting or architecture and engineering firm deployment on this module was found. Deltek's study is a benchmark, not KM-specific.
- **Quality evidence.** No error rates, override rates, parallel-run results or inspection outcomes for firm-knowledge retrieval. Customer stories report positive feedback without measurements; Harvey's agent results are vendor-run.
- **Undated pages.** iManage's customer stories, NetDocuments' ndMAX page, Intapp's experience page, Certinia's and Kantata's product pages carry no publication date. Their `date` field is the retrieval date (2026-10-19), flagged in each title. The iManage benchmark landing page is dated only "2026" (from the landscape file); the full report is gated and its percentages beyond the executive summary were not read.
- **Paywalled or blocked.** Law360 (lead paragraph only), the Legal IT Insider interview with Clifford Chance's knowledge head (bot check), APQC's 2026 KM survey (members), ILTA's full survey, Bloomberg original, the Epiq and Clifford Chance first-party pages (not found). NetDocuments' and EDRM's pages needed the text mirror.
- **Conference content.** Legalweek and ILTACON KM session content beyond the EDRM blogger's descriptions was not reachable; no podcast or community discussion was opened (the discourse angle covers these).
- **Customer stories skew to one vendor.** Seven of the named-organisation examples come from iManage customer pages, which are vendor-authored and favourable. Harvey and Legora customer pages read for this module were mostly about adoption, not knowledge reuse, and were not used.
- **Unnamed customers.** The EMEA global law firm, the independent regulatory body and the legal operations customer are anonymous in their iManage stories, so they support notes but not grades.

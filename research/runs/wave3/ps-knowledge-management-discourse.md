# Professional services: knowledge management (precedents, methods, expertise). Discourse angle

Prepared 2026-10-19. Archetype `professional-services`, module `knowledge-management`. Angle: what practitioners are saying (conference sessions, podcasts, practitioner articles, trade press, vendor announcements as read by trade press). Method: `curl` with a text mirror for blocked pages, `pdftotext` for PDFs. Web search budget ran out during the run, so the last leads were followed by direct fetch only. Each source is marked `access: full` (opened and read) because no search-only item supports any claim below. All page text was read in the form returned by the server; for three pages (EDRM, NetDocuments technical report, APQC) the text came through the r.jina.ai mirror.

---

## 1. Summary

**What practitioners are saying.** The 2026 conversation about knowledge management (KM) in professional services has moved from "can AI answer questions" to "what is the AI allowed to know, and is what it knows any good". The recurring word at ILTACON 2026 was "context" (EDISCOVERYTODAY-ILTACON-2026). Document-management vendors (iManage, NetDocuments) now describe themselves as the governed context layer for other companies' AI (LAWSITES-IMANAGE-2026; LAWSITES-NETDOCS-2026). Harvey and Legora, the legal AI platforms, connect to those layers instead of replacing them (LAWSITES-HARVEYDJ-2026; LAWSITES-LEGORAIM-2026).

- **The knowledge underneath is the constraint, and firms say so.** ILTA's 2026 technology survey says knowledge infrastructure "remains dramatically underdeveloped" across enterprise search and expertise management, even as 94% of responding firms engage with generative AI (ILTA-TECHSURVEY-2026, pp. 3 and 9). A Thomson Reuters Institute (TRI) feature argues that agentic AI "expects clean data, documented processes" and that pilots fail on incentives and documentation, not model capability (TRI-PREMORTEM-2026). A KM leader writing in Artificial Lawyer says the hard part has always been getting busy lawyers to share what they know, and that AI "made it much harder to pretend" otherwise (AL-DIDOMENICO-2026, sponsored piece).
- **Search and precedent reuse is the entry use case.** Practitioners at ILTACON 2025 treated precedent search as the starting line for legal AI, with a named Cleary Gottlieb innovation director saying AI search turned a needle-in-a-haystack problem into a haystack full of needles (DRAFTWISE-ILTACON-2025, a vendor recap). Vendors shipped firm-wide search (Litera, Thomson Reuters, NetDocuments, DeepJudge) in the last 15 months.
- **Tacit knowledge is the frontier.** Products now aim to capture judgment, not only documents: AI "twins" of individual lawyers (AL-TWIN1-2026), decisions-to-positions capture for in-house teams (AL-COHESO-2026), and process templates defined by knowledge teams (HARVEY-ORCH-2026). Every one of these is a vendor claim or announcement; none has published results.
- **Evidence of measured quality is thin.** The only controlled measurement found is a vendor benchmark of its own product on public matters (NETDOCS-LCEB-2026). Named-organization figures are usage counts and unmeasured time-saving claims (McKinsey's Lilli, Infosys). No override rates, error rates, parallel runs or independent inspection results for firm knowledge assistants were found.
- **KM roles are being re-bundled with AI.** Eversheds Sutherland, K&L Gates and Gilchrist Connell have each placed knowledge work under an AI or innovation leader (AL-EVERSHEDS-2026; AL-X4-2026; LAWYERSWEEKLY-GILCHRIST-2026). Law library and KM staffing is at its highest in nearly a decade in the AALL survey, which does not attribute the change to AI (LAWSITES-AALL-2025).
- **Regulator language already names the risk.** California's State Bar guidance lists "knowledge bases" and document management systems among the internal systems an agentic tool may reach, and warns that poorly configured access can disclose confidential information across matters (CALBAR-GENAI-2026, confidentiality section).

**Use case count.** 17 candidate use cases: grade A 0, grade B 2, grade C 12, grade D 3. No use case reaches grade A because no named organization reports a measured outcome for this module.

---

## 2. Use cases

```yaml
- id: professional-services-knowledge-management-01
  title: Firm-wide natural-language search across document, matter and expertise repositories
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Precedent, matter history and know-how sit across the document management system, matter systems, SharePoint
    and expertise databases. Lawyers search folder by folder. ILTA's 2026 survey says knowledge infrastructure is
    "dramatically underdeveloped" across enterprise search and expertise management.
  solution: >-
    A conversational search layer that queries several repositories at once, returns answers with source documents,
    and honors each user's permissions and ethical walls. Products named in the sources: Litera Firm AI Search
    (accessed through the Lito agent), Thomson Reuters CoCounsel Knowledge Search (HighQ, iManage, NetDocuments,
    SharePoint, OneDrive and Thomson Reuters content), NetDocuments SmartSearch (private preview), iManage Insight+
    multi-region search with native OCR, and the DeepJudge integration with Harvey, which the companies say also
    writes work product back into the knowledge base.
  outcomes:
    - lever: speed
      description: none published
      figure: none
      measures: not applicable; the sources are product announcements without measured results
      provenance: vendor-published
      source_ref: LAWSITES-ILTACON4-2026
    - lever: capacity
      description: >-
        A KM-recap poll at one ILTACON 2025 session reported by Draftwise: 44 of 89 attendees were piloting AI tools,
        16 were in firmwide deployment, 6 had not started. This is an adoption snapshot, not an outcome of search.
      figure: 44 of 89 piloting; 16 firmwide; 6 not started
      measures: attendees at one ILTACON 2025 session who answered a live poll (89 respondents)
      provenance: vendor-published
      source_ref: DRAFTWISE-ILTACON-2025
  prerequisites:
    - Content consolidated in searchable, connected systems rather than scattered stores (DRAFTWISE-ILTACON-2025).
    - Scanned and image-only files made searchable, which iManage says its native OCR addresses (LAWSITES-IMANAGE-2026).
    - Permission model and ethical walls carried through to the search layer (LAWSITES-HARVEYDJ-2026).
  risks_and_guardrails:
    - A practitioner at ILTACON 2025 said language models are not good search engines and that the system should retrieve the top documents first, then pass them to the model (DRAFTWISE-ILTACON-2025).
    - California's State Bar guidance says agentic systems that reach knowledge bases or document management systems can disclose confidential information across matters if poorly configured, and lawyers must limit and monitor that access (CALBAR-GENAI-2026).
    - DeepJudge and Harvey say the integration respects existing access permissions and ethical walls (LAWSITES-HARVEYDJ-2026).
  human_checkpoints:
    - Lawyer opens and checks the cited source document before reusing its content.
    - KM or IT owner sets which repositories and which collections the assistant may search.
  role_evolution: >-
    Eversheds Sutherland merged research and knowledge services into an AI-centric US Innovation Department
    (AL-EVERSHEDS-2026). The 2026 ILTA survey reports that many firms expect more headcount in knowledge management
    and data science (ILTA-TECHSURVEY-2026).
  evidence_grade: C
  sources:
    - { ref: LAWSITES-ILTACON4-2026, title: "ILTACON News Round-Up Part 4, The Business of Law", publisher: LawSites, type: press, url: "https://www.lawnext.com/2026/09/iltacon-news-round-up-part-4-the-business-of-law-litera-aderant-oddr-tre-ai-intapp.html", date: 2026-09-04, access: full, locator: "Litera section, Firm AI Search" }
    - { ref: AL-TRKNOWLEDGE-2025, title: "Thomson Reuters Launches CoCounsel Knowledge Search", publisher: Artificial Lawyer, type: press, url: "https://www.artificiallawyer.com/2025/07/09/thomson-reuters-launches-cocounsel-knowledge-search/", date: 2025-07-09, access: full, locator: "paragraphs 1-3" }
    - { ref: LAWSITES-HARVEYDJ-2026, title: "Harvey Launches Command Center ... and Partners with DeepJudge on Institutional Knowledge", publisher: LawSites, type: press, url: "https://www.lawnext.com/2026/05/harvey-launches-command-center-for-managing-enterprise-ai-adoption-and-partners-with-deepjudge-on-institutional-knowledge.html", date: 2026-05-20, access: full, locator: "DeepJudge partnership section" }
    - { ref: LAWSITES-IMANAGE-2026, title: "iManage Unveils Next Evolution of Platform at ConnectLive 2026", publisher: LawSites (press release reproduced), type: press, url: "https://www.lawnext.com/2026/05/imanage-unveils-next-evolution-of-platform-at-connectlive-2026-as-organizations-prepare-for-the-next-era-of-ai-ready-knowledge-work.html", date: 2026-05-22, access: full, locator: "Insight+ Multi-Region Search and native OCR paragraphs" }
    - { ref: DRAFTWISE-ILTACON-2025, title: "Key Takeaways from ILTACON 2025", publisher: Draftwise, type: vendor, url: "https://www.draftwise.com/blog/key-takeaways-from-iltacon-2025-from-demos-to-day-to-day-impact", date: 2025-08-19, access: full, locator: "section 1 'Search Is the Starting Line' and pilot poll paragraph" }
    - { ref: ILTA-TECHSURVEY-2026, title: "ILTA Technology Survey 2026 Executive Summary", publisher: ILTA, type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026, access: full, locator: "p. 9 'Curtain Call for the Data Center'; p. 5 headcount paragraph" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California, COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026, access: full, locator: "Confidentiality (rule 1.6) row, paragraph on agentic access to internal firm systems (PDF p. 6)" }
    - { ref: AL-EVERSHEDS-2026, title: "Eversheds Sutherland Establishes AI-Centric US Innovation Dept", publisher: Artificial Lawyer, type: press, url: "https://www.artificiallawyer.com/2026/01/26/eversheds-sutherland-establishes-ai-centric-us-innovation-dept/", date: 2026-01-26, access: full, locator: "paragraph 2" }
  last_reviewed: 2026-10-19
  notes: >-
    ILTA's executive summary PDF metadata shows creation on 2026-08-14 while the landscape file dated it June 2026;
    the date is given as 2026. The CALBAR page locator is the PDF page; the guidance is dated 2026 in its text
    (PDF created 2026-05-15). No named firm deployment of any of these search products was found in this angle;
    the practice angle should look for customers.

- id: professional-services-knowledge-management-02
  title: Precedent and clause retrieval inside the drafting tool, adapted to the new deal
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [document-production, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: >-
    A transactional lawyer remembers a good clause from a prior deal but loses time hunting through folders, and
    may land on an unexecuted draft or a counterparty's markup.
  solution: >-
    Search over the firm's or department's own past documents from inside Word, returning matching clauses and, in
    some products, rewriting them for the current deal. Products named in the sources: Spellbook Library with Smart
    Clause Drafting, Litera One Precedent workflow (beta in July 2025), SimpleDocs Contract Intelligence Layer
    (policy, precedent and market data for in-house teams) and Draftwise.
  outcomes:
    - lever: speed
      description: >-
        Litera says Litera One users save between 2 and 10 hours per week by consolidating workflows into one interface.
        The claim covers the whole platform, not precedent search alone.
      figure: 2-10 hours per week
      measures: per Litera One user, as stated by Litera; method and population not given
      provenance: vendor-published
      source_ref: LAWSITES-LITERA-2025
    - lever: capacity
      description: Litera reports more than 2,500 law firms and in-house teams adopted Litera One after its April 2025 launch.
      figure: more than 2,500
      measures: law firms and in-house legal teams that adopted Litera One since launch, per Litera
      provenance: vendor-published
      source_ref: LAWSITES-LITERA-2025
  prerequisites:
    - Past work product ingested and indexed from the firm's storage (LAWSITES-SPELLBOOK-2025).
    - Ability to tell final executed agreements from drafts and counterparty versions (DRAFTWISE-PRECEDENT-2025).
    - Written playbooks and fallback positions where policy is to be applied (LAWSITES-SIMPLEDOCS-2026).
  risks_and_guardrails:
    - Draftwise argues that poor source material undermines the reliability of suggestions and trust in the tool (DRAFTWISE-PRECEDENT-2025).
    - SimpleDocs describes the precedent feature as a response to reliance on tribal knowledge when reviewing counterparty redlines (LAWSITES-SIMPLEDOCS-2026).
  human_checkpoints:
    - Lawyer decides whether a retrieved clause fits the deal and reviews the adapted wording.
  role_evolution: >-
    The ILTACON 2025 recap quotes a participant saying lawyers prefer a red pen to a blank page, which frames search as
    the first step of drafting rather than a separate research task (DRAFTWISE-ILTACON-2025).
  evidence_grade: C
  sources:
    - { ref: LAWSITES-SPELLBOOK-2025, title: "Introducing Spellbook Library: Contract AI That Learns From Your Precedents", publisher: LawSites (vendor post reproduced), type: press, url: "https://www.lawnext.com/2025/07/introducing-spellbook-library-contract-ai-that-learns-from-your-precedents.html", date: 2025-07-31, access: full, locator: "opening paragraphs, Smart Clause Drafting" }
    - { ref: LAWSITES-LITERA-2025, title: "Litera Expands Litera One Platform with New Drafting and Knowledge Management Features", publisher: LawSites, type: press, url: "https://www.lawnext.com/2025/07/litera-expands-litera-one-platform-with-new-drafting-and-knowledge-management-features.html", date: 2025-07-31, access: full, locator: "paragraphs 2-3 (Precedent beta) and adoption and time-saving paragraph" }
    - { ref: LAWSITES-SIMPLEDOCS-2026, title: "SimpleDocs Launches Contract Intelligence Layer", publisher: LawSites, type: press, url: "https://www.lawnext.com/2026/02/simpledocs-launches-contract-intelligence-layer-putting-policy-precedent-and-market-data-inside-microsoft-word.html", date: 2026-02-18, access: full, locator: "three-source description and precedent data paragraph" }
    - { ref: DRAFTWISE-PRECEDENT-2025, title: "Garbage In, Garbage Out: How to Build a Precedent Database Lawyers Can Trust", publisher: Draftwise, type: vendor, url: "https://www.draftwise.com/blog/garbage-in-garbage-out-how-to-build-a-precedent-database-your-lawyers-can-trust", date: 2025-09-24, access: full, locator: "opening scenario and 'Start with Surgical Precision'" }
    - { ref: DRAFTWISE-ILTACON-2025, title: "Key Takeaways from ILTACON 2025", publisher: Draftwise, type: vendor, url: "https://www.draftwise.com/blog/key-takeaways-from-iltacon-2025-from-demos-to-day-to-day-impact", date: 2025-08-19, access: full, locator: "section 1" }
  last_reviewed: 2026-10-19
  notes: >-
    In-house variant: SimpleDocs targets law departments (tag in-house). Vendor customer counts (Spellbook says more
    than 3,400 firms and in-house teams for the whole product) are not usage evidence for Library. No named
    customer for the precedent features was found.

- id: professional-services-knowledge-management-03
  title: Curated "gold standard" precedent collections with senior review and final-version gating
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    AI reuse is only as good as what it retrieves. Document stores mix drafts, executed deals, counterparty markups
    and outdated templates, and nobody has recorded why a document was judged final or good.
  solution: >-
    KM lawyers or senior partners designate trusted collections; filters restrict retrieval to firm-authored final
    documents; a partner validation step and a feedback loop catch problems before they spread. An Accenture-authored
    article describes an unnamed global professional-services firm that set governance rules (for example a minimum
    number of client examples to protect anonymity), had senior reviewers judge which past proposals and deliverables
    were dependable enough to reuse, and placed concepts in a knowledge graph.
  outcomes:
    - lever: quality
      description: none published
      figure: none
      measures: not applicable
      provenance: vendor-published
      source_ref: DRAFTWISE-PRECEDENT-2025
  prerequisites:
    - Named KM owner and sponsorship; DiDomenico says sponsorship, incentives and recording why a document was final are not technology problems (AL-DIDOMENICO-2026).
    - Rules for what may enter the shared base, including client anonymity thresholds (CMR-ACCENTURE-2026).
    - Documented processes and fixed information architecture (TRI-PREMORTEM-2026).
  risks_and_guardrails:
    - Draftwise says its platform can classify final versus draft automatically and that manual curation should not be a prerequisite; the claim is unverified (DRAFTWISE-PRECEDENT-2025).
    - TRI's premortem feature lists fragmented document storage and undocumented exceptions among the causes of a fictional agentic pilot failing (TRI-PREMORTEM-2026).
  human_checkpoints:
    - Senior reviewer or partner approves what enters the trusted collection.
    - KM team reviews collections on a schedule and removes superseded material.
  role_evolution: >-
    KM lawyers and senior partners become curators who decide which work is exemplary (DRAFTWISE-PRECEDENT-2025).
    DiDomenico argues firms should grow existing KM, library and research staff and recruit practising lawyers into
    these roles, since a single person with legal, business, data and AI skills mostly does not exist (AL-DIDOMENICO-2026).
  evidence_grade: C
  sources:
    - { ref: DRAFTWISE-PRECEDENT-2025, title: "Garbage In, Garbage Out: How to Build a Precedent Database Lawyers Can Trust", publisher: Draftwise, type: vendor, url: "https://www.draftwise.com/blog/garbage-in-garbage-out-how-to-build-a-precedent-database-your-lawyers-can-trust", date: 2025-09-24, access: full, locator: "'Create Gold Standard Collections' and partner validation paragraphs" }
    - { ref: CMR-ACCENTURE-2026, title: "Tacit Knowledge Is Your Next Competitive Moat", publisher: California Management Review Insight (Tung, Roussiere of Accenture), type: firm, url: "https://cmr.berkeley.edu/assets/documents/pdf/2026-03-tacit-knowledge-is-your-next-competitive-moat.pdf", date: 2026-03-16, access: full, locator: "section 'Codify Tacit Knowledge Without Flattening It', professional-services paragraph" }
    - { ref: AL-DIDOMENICO-2026, title: "Old Problems, New Tools: Maybe You Need a Knowledge Strategy", publisher: Artificial Lawyer (sponsored by LegalTech Connect), type: press, url: "https://www.artificiallawyer.com/2026/10/15/old-problems-new-tools-maybe-you-need-a-knowledge-strategy/", date: 2026-10-15, access: full, locator: "paragraphs on participation, sponsorship and the talent question" }
    - { ref: TRI-PREMORTEM-2026, title: "Premortem: Your 2028 agentic AI pilot program failed", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/feature-agentic-ai-pilot-failure", date: 2026-02-20, access: full, locator: "summary paragraphs 'The big idea' and case study 1" }
  last_reviewed: 2026-10-19
  notes: >-
    The professional-services firm in the Accenture article is unnamed, so it cannot support a B grade. The TRI
    premortem is a speculative feature, not a report of a real pilot. Idea strength: practitioners and vendors both
    discuss it; no firm names a curation programme in sources read.

- id: professional-services-knowledge-management-04
  title: Automatic classification, entity extraction and matter summaries at the point a document is filed
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [data-reporting, research-synthesis]
  pattern: bulk-transformation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Document metadata and version notes are rarely entered by hand, so search and AI summaries run on poorly
    described content. Scanned files are invisible to search.
  solution: >-
    On filing, the system classifies the document, extracts parties, dates and clauses into the matter record,
    generates a matter overview and writes a summary of what changed between versions. NetDocuments describes these
    features in a private preview for select customers; iManage describes native OCR so scanned files become
    searchable and legible to AI. A KMWorld Europe 2026 session scheduled for 14 April proposed combining LLM-based
    classification and extraction with taxonomies and ontologies.
  outcomes:
    - lever: speed
      description: >-
        NetDocuments says the matter overview can dramatically reduce the time a new associate spends getting oriented.
        No figure is given.
      figure: none
      measures: not applicable
      provenance: vendor-published
      source_ref: LAWSITES-NETDOCS-2026
  prerequisites:
    - A shared taxonomy; NetDocuments says its graph draws in part on SALI and FOLIO standards (LAWSITES-NETDOCS-2026).
    - Permissions and ethical walls preserved on derived summaries (LAWSITES-NETDOCS-2026).
  risks_and_guardrails:
    - Derived summaries inherit the access rules of their sources; NetDocuments says results remain subject to each user's permissions and ethical walls (LAWSITES-NETDOCS-2026).
    - NetDocuments' preview opened only on its enterprise AI tier for select customers, so scale and accuracy are unproven in public sources (LAWSITES-NETDOCS-2026).
  human_checkpoints:
    - Lawyer or paralegal confirms extracted parties, dates and clauses before they are relied on.
  role_evolution: >-
    KM and information-governance staff move from asking lawyers to tag documents toward governing taxonomies and
    checking machine-assigned labels; the KMWorld Europe programme treats taxonomy and metadata as the base of AI
    systems (KMWORLD-EUROPE-2026).
  evidence_grade: C
  sources:
    - { ref: LAWSITES-NETDOCS-2026, title: "NetDocuments Unveils Legal Context Graph ... and a Reimagined Platform", publisher: LawSites, type: press, url: "https://www.lawnext.com/2026/05/netdocuments-unveils-legal-context-graph-to-map-legal-knowledge-alongside-a-reimagined-platform.html", date: 2026-05-14, access: full, locator: "feature list: Matter Overview, SmartSearch, AI-Generated Version History, Document Intelligence" }
    - { ref: LAWSITES-IMANAGE-2026, title: "iManage Unveils Next Evolution of Platform at ConnectLive 2026", publisher: LawSites (press release reproduced), type: press, url: "https://www.lawnext.com/2026/05/imanage-unveils-next-evolution-of-platform-at-connectlive-2026-as-organizations-prepare-for-the-next-era-of-ai-ready-knowledge-work.html", date: 2026-05-22, access: full, locator: "native OCR paragraph" }
    - { ref: KMWORLD-EUROPE-2026, title: "KMWorld Europe 2026 Full Programme Listing", publisher: KMWorld, type: conference, url: "https://www.kmworld.com/Europe/2026/Programme.aspx", date: 2026-04-14, access: full, locator: "session abstract on LLM classification with taxonomies and ontologies (Dave Clarke)" }
  last_reviewed: 2026-10-19
  notes: >-
    Maturity is piloting because NetDocuments opened a private preview to unnamed customers; no customer was named.
    The KMWorld session abstract is for a session on 14 April 2026, which has passed; only the abstract was read.

- id: professional-services-knowledge-management-05
  title: Context or knowledge-graph layer that links documents, matters and people for any AI tool
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [research-synthesis, data-reporting]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >-
    Legal work is a web of relationships among documents, communications, matters and people, which a document
    management system stores but does not describe in a form AI can use. Harvey and DeepJudge call the resulting
    gap a "context tax".
  solution: >-
    A governed index that maps relationships at document, matter and firm-wide levels and serves several AI tools.
    NetDocuments Legal Context Graph (private preview from May 2026), iManage Context Fabric (next-generation
    platform, general availability announced for October), Wolters Kluwer Libra knowledge graph over its own content,
    and the knowledge-graph approach described by Accenture authors for a professional-services firm.
  outcomes:
    - lever: cost
      description: >-
        In NetDocuments' own benchmark, the cost of a correct answer fell from $0.68 to $0.36 with the Legal Context
        Graph enabled and accuracy held almost constant.
      figure: "about 48% lower cost per correct answer (Context Value Ratio 1.92)"
      measures: >-
        dollars per credit-weighted correct answer, 300 questions across ten matters (874 documents) built from public
        filings and dockets, same model and agent harness with and without the graph; an internal NetDocuments benchmark,
        not a firm deployment
      provenance: vendor-published
      source_ref: NETDOCS-LCEB-2026
    - lever: quality
      description: >-
        iManage's survey reports a gap between the most and least mature knowledge-work organizations in fully
        integrated, widely used AI.
      figure: "27% versus 3%"
      measures: >-
        share of organizations reporting fully integrated and widely used AI, top maturity tier versus least mature
        tier, in a survey of over 3,000 business and technical decision makers fielded by iManage; correlation, not a
        test of knowledge graphs
      provenance: vendor-published
      source_ref: IMANAGE-BENCH-2026
  prerequisites:
    - Document repository, matter workspace structure and permissions already governed (LAWSITES-NETDOCS-2026).
    - A baseline of the firm's own questions and answers to compare against, since NetDocuments says the cost ratio is most trustworthy against a firm's own prior baseline (NETDOCS-LCEB-2026).
  risks_and_guardrails:
    - The benchmark uses public matters, an internal harness and AI-assisted drafting of the report; the report itself lists the controls it applied, and no independent validation was found (NETDOCS-LCEB-2026).
    - iManage's survey reports 36% of respondents have experienced a policy violation and 25% say end users use public AI with little oversight, which is the governance pressure behind the context-layer pitch (IMANAGE-BENCH-2026).
    - California's State Bar guidance requires monitoring and access controls when agentic tools reach internal systems (CALBAR-GENAI-2026).
  human_checkpoints:
    - Lawyer verifies answers against the cited documents.
    - KM or IT team reviews how the graph resolves matter and client boundaries.
  role_evolution: >-
    Firms that built reusable data and semantic structures could build new AI applications faster, per the Accenture
    authors, who say more than half of the semantic structure could be reused (CMR-ACCENTURE-2026). This shifts KM
    work toward ontology and metadata stewardship.
  evidence_grade: C
  sources:
    - { ref: NETDOCS-LCEB-2026, title: "2026 Legal Context Engineering Benchmark Report", publisher: NetDocuments, type: vendor, url: "https://www.netdocuments.com/?p=11503", date: 2026-08, access: full, locator: "Executive Summary; methodology and cost-per-correct-answer sections" }
    - { ref: LAWSITES-NETDOCS-2026, title: "NetDocuments Unveils Legal Context Graph ...", publisher: LawSites, type: press, url: "https://www.lawnext.com/2026/05/netdocuments-unveils-legal-context-graph-to-map-legal-knowledge-alongside-a-reimagined-platform.html", date: 2026-05-14, access: full, locator: "paragraphs 1-4 (three levels of the graph) and the context-engineering paragraph" }
    - { ref: LAWSITES-IMANAGE-2026, title: "iManage Unveils Next Evolution of Platform at ConnectLive 2026", publisher: LawSites (press release reproduced), type: press, url: "https://www.lawnext.com/2026/05/imanage-unveils-next-evolution-of-platform-at-connectlive-2026-as-organizations-prepare-for-the-next-era-of-ai-ready-knowledge-work.html", date: 2026-05-22, access: full, locator: "context fabric paragraph" }
    - { ref: LAWSITES-ILTACON3-2026, title: "ILTACON News Round-Up Part 3, Documents, Data and AI", publisher: LawSites, type: press, url: "https://www.lawnext.com/2026/09/iltacon-news-round-up-part-3-documents-data-and-ai-imanage-netdocuments-entegrata-wolters-kluwer-thomson-reuters-clio-avvoka.html", date: 2026-09-04, access: full, locator: "NetDocuments and Wolters Kluwer Libra sections" }
    - { ref: IMANAGE-BENCH-2026, title: "iManage Knowledge Work Benchmark Report 2026", publisher: iManage, type: survey, url: "https://imanage.com/benchmark-report-2026/", date: 2026, access: full, locator: "headline statistics and 'AI Adoption: Broad Reach, Different Realities'" }
    - { ref: CMR-ACCENTURE-2026, title: "Tacit Knowledge Is Your Next Competitive Moat", publisher: California Management Review Insight (Accenture authors), type: firm, url: "https://cmr.berkeley.edu/assets/documents/pdf/2026-03-tacit-knowledge-is-your-next-competitive-moat.pdf", date: 2026-03-16, access: full, locator: "section 'Build the Semantic Layer'" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California, COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026, access: full, locator: "Confidentiality row, agentic access paragraph" }
  last_reviewed: 2026-10-19
  notes: >-
    NetDocuments also states a modelled saving of about $940,000 a year for a 2,000-person firm asking four million
    questions; this is an estimate from the benchmark, not a measured result. The report names GPT-5.6-family models
    and gives 300 questions across ten matters. Because the benchmark is on public SEC and court records, results
    may differ on a firm's own repository. The iManage figures come from a vendor-run survey; the page
    does not give the denominator for the 27% and 3% beyond the tier.

- id: professional-services-knowledge-management-06
  title: Governed access to firm knowledge from third-party AI tools through MCP connectors and context handoff
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [research-synthesis, software-systems]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Lawyers and consultants use several AI products. Without a shared connection, each product needs its own
    export of firm content, and users re-upload materials and rebuild prompts when they switch tools.
  solution: >-
    The knowledge repository exposes a Model Context Protocol (MCP) server so approved AI tools can search and
    save back under the user's existing permissions. Announced: iManage MCP Server in Claude (partner ecosystem),
    a Legora connection to the iManage MCP Server (stated as plans), an iManage plugin in ChatGPT Enterprise
    (announced 17 September 2026), NetDocuments MCP ecosystem including Claude, Copilot, Perplexity, Gemini,
    Harvey and Legora, and Entegrata's planned MCP server for firm data. DeepJudge released an open Agent Handoff
    Protocol so a user can move to another AI product with the objective, conversation context and resources.
  outcomes:
    - lever: experience
      description: none published
      figure: none
      measures: not applicable; vendor announcements and a partner quote
      provenance: vendor-published
      source_ref: LAWSITES-IMANAGECHATGPT-2026
  prerequisites:
    - A governed repository whose permissions, ethical walls and audit trail are enforced at the connector (LAWSITES-IMANAGECHATGPT-2026).
    - Client and engagement terms that allow the chosen AI tools to see the content.
  risks_and_guardrails:
    - California's State Bar guidance says a lawyer must not deploy an agentic system that permits autonomous external transmission of client information without safeguards and human review (CALBAR-GENAI-2026).
    - iManage says it added AI-specific controls over how AI is applied across clients and matters, and monitoring of agent activity (LAWSITES-IMANAGE-2026).
  human_checkpoints:
    - IT or KM approves which AI tools get connectors and which workspaces they may reach.
    - Lawyer reviews work saved back as a new version before it becomes part of the record.
  role_evolution: >-
    The ABA Journal columnist's takeaway from ILTACON 2026 was that legal AI is no longer developing in separate
    silos, with companies connecting products, data and workflows at a rapid pace (ABAJ-ILTACON-2026). Integration
    and access governance become standing KM and IT duties.
  evidence_grade: C
  sources:
    - { ref: LAWSITES-IMANAGECHATGPT-2026, title: "iManage to Deliver Governed AI-Powered Knowledge Work in ChatGPT Enterprise", publisher: LawSites (press release reproduced), type: press, url: "https://www.lawnext.com/2026/09/imanage-to-deliver-governed-ai-powered-knowledge-work-in-chatgpt-enterprise.html", date: 2026-09-21, access: full, locator: "paragraphs 1-5" }
    - { ref: LAWSITES-LEGORAIM-2026, title: "Legora and iManage Deepen Integration Through iManage MCP Server", publisher: LawSites (press release reproduced), type: press, url: "https://www.lawnext.com/2026/10/legora-and-imanage-deepen-integration-through-imanagemcp-server.html", date: 2026-10-19, access: full, locator: "paragraphs 1-4 (release dated 16 Oct 2026)" }
    - { ref: LAWSITES-IMANAGE-2026, title: "iManage Unveils Next Evolution of Platform at ConnectLive 2026", publisher: LawSites (press release reproduced), type: press, url: "https://www.lawnext.com/2026/05/imanage-unveils-next-evolution-of-platform-at-connectlive-2026-as-organizations-prepare-for-the-next-era-of-ai-ready-knowledge-work.html", date: 2026-05-22, access: full, locator: "paragraphs on AI-specific controls and Claude access" }
    - { ref: LAWSITES-ILTACON3-2026, title: "ILTACON News Round-Up Part 3, Documents, Data and AI", publisher: LawSites, type: press, url: "https://www.lawnext.com/2026/09/iltacon-news-round-up-part-3-documents-data-and-ai-imanage-netdocuments-entegrata-wolters-kluwer-thomson-reuters-clio-avvoka.html", date: 2026-09-04, access: full, locator: "NetDocuments and Entegrata sections" }
    - { ref: LAWSITES-DEEPJUDGE-2026, title: "DeepJudge Releases an Open Protocol for Passing Users and Their Context Between AI Products", publisher: LawSites, type: press, url: "https://www.lawnext.com/2026/08/deepjudge-releases-an-open-protocol-for-passing-users-and-their-context-between-ai-products-with-harvey-and-thomson-reuters-on-board.html", date: 2026-08-13, access: full, locator: "paragraphs 1-6" }
    - { ref: ABAJ-ILTACON-2026, title: "ILTACON 2026: The race to connect the dots and the data", publisher: ABA Journal (Nicole Black column), type: press, url: "https://www.abajournal.com/columns/article/iltacon-2026-and-the-race-to-connect-the-dots", date: 2026-09-02, access: full, locator: "'Finding partners' and closing paragraphs" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California, COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026, access: full, locator: "Confidentiality row, last sentence of agentic paragraph" }
  last_reviewed: 2026-10-19
  notes: >-
    Tense matters: the Legora release says the companies "announced plans to connect"; the DeepJudge protocol says
    Harvey is building an integration entering beta, and Thomson Reuters "will support" it. The LawSites ILTACON
    round-ups note that Claude was used to assist in creating the summaries.

- id: professional-services-knowledge-management-07
  title: Expertise location from matter, client and people records by conversation
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [research-synthesis, coordination-scheduling]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Expertise directories built from annual surveys go stale. Colleagues do not know who has done similar work, and
    the ILTA survey says knowledge infrastructure is underdeveloped across expertise management.
  solution: >-
    Natural-language lookup of people, matters and clients drawn from live firm systems. Litera's Firm AI Search
    queries matter, client and expertise data, and "Lito Lookups" surfaces matter, client and people records inside the
    chat. ILTACON 2026 listed a session titled "Does Experience Matter? Unlocking hidden expertise using AI."
  outcomes:
    - lever: speed
      description: none published
      figure: none
      measures: not applicable
      provenance: vendor-published
      source_ref: LAWSITES-ILTACON4-2026
  prerequisites:
    - Reliable matter, time-entry and people data in the systems being queried.
    - Lawyer willingness to be profiled and surfaced; sources do not describe consent rules.
  risks_and_guardrails:
    - Expertise surfaced from matter records may reflect confidential client work, so matter and ethical-wall rules carry over (CALBAR-GENAI-2026).
    - The Accenture authors suggest social-network analysis could reveal who colleagues rely on informally; this is a suggestion, not a reported deployment (CMR-ACCENTURE-2026).
  human_checkpoints:
    - KM or practice leader confirms experience claims before staffing or pitching on them.
  role_evolution: >-
    DiDomenico describes a knowledge manager who once maintained expertise directories through annual surveys and
    can now build an AI persona of a partner's judgment (AL-DIDOMENICO-2026).
  evidence_grade: C
  sources:
    - { ref: LAWSITES-ILTACON4-2026, title: "ILTACON News Round-Up Part 4, The Business of Law", publisher: LawSites, type: press, url: "https://www.lawnext.com/2026/09/iltacon-news-round-up-part-4-the-business-of-law-litera-aderant-oddr-tre-ai-intapp.html", date: 2026-09-04, access: full, locator: "Litera Announces Firm AI Search, paragraphs 1-3" }
    - { ref: KMEDUHUB-ILTACON-2026, title: "International Legal Technology Association Conference (ILTACON): programme listing", publisher: KM Education Hub, type: conference, url: "https://kmeducationhub.de/international-legal-technology-association-conference-iltacon/", date: 2026-08-23, access: full, locator: "49th ILTACON 2026 entry, Sessions list" }
    - { ref: ILTA-TECHSURVEY-2026, title: "ILTA Technology Survey 2026 Executive Summary", publisher: ILTA, type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026, access: full, locator: "p. 9" }
    - { ref: AL-DIDOMENICO-2026, title: "Old Problems, New Tools: Maybe You Need a Knowledge Strategy", publisher: Artificial Lawyer (sponsored), type: press, url: "https://www.artificiallawyer.com/2026/10/15/old-problems-new-tools-maybe-you-need-a-knowledge-strategy/", date: 2026-10-15, access: full, locator: "paragraph 3" }
    - { ref: CMR-ACCENTURE-2026, title: "Tacit Knowledge Is Your Next Competitive Moat", publisher: California Management Review Insight (Accenture authors), type: firm, url: "https://cmr.berkeley.edu/assets/documents/pdf/2026-03-tacit-knowledge-is-your-next-competitive-moat.pdf", date: 2026-03-16, access: full, locator: "section 'Map Tacit Knowledge'" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California, COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026, access: full, locator: "Confidentiality row" }
  last_reviewed: 2026-10-19
  notes: >-
    The ILTACON session title is from a third-party listing of the ILTACON 2026 programme (title only; no abstract or
    speaker read). Staffing-side expertise matching (Kantata Expertise Agent ranked recommendations) is routed to
    staffing-resourcing.

- id: professional-services-knowledge-management-08
  title: AI "twins" or personas that capture an individual lawyer's judgment and make it available to colleagues
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [expert-judgment, research-synthesis]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    The most valuable knowledge is the context behind a document: why a decision was made, how a negotiation unfolded,
    who has relevant experience. It sits in emails, calls, notes and memories and leaves when people retire.
  solution: >-
    Twin1 (launched August 2026 after a $20m raise) builds an AI twin per person from their work and links the twins
    so expertise moves across the organization without unrestricted access to private data. Its CEO says it works with
    Linklaters, Orrick and Dechert. DiDomenico separately describes building an AI persona from a partner's work
    product and structured interviews.
  outcomes:
    - lever: capacity
      description: none published
      figure: none
      measures: not applicable; the CEO gives a pipeline count of more than 400 prospects, which is not an outcome
      provenance: vendor-published
      source_ref: AL-TWIN1-2026
  prerequisites:
    - Consent and a data-use policy for building a model of an individual; the sources do not describe either.
    - Permission-aware access so a twin does not leak another matter's information.
  risks_and_guardrails:
    - The CEO says the product preserves privacy, permissions, compliance and human agency and does not train models on customer data; these are vendor statements (AL-TWIN1-2026).
    - Cal Bar guidance says lawyers remain responsible for configuring agentic systems consistently with confidentiality duties (CALBAR-GENAI-2026).
    - The sources reviewed do not say who owns a twin when the lawyer leaves.
  human_checkpoints:
    - Individual lawyer reviews and approves what their twin is allowed to say.
    - Reviewing lawyer treats twin output as input to their own judgment.
  role_evolution: >-
    The Twin1 CEO frames the "atomic unit of knowledge" in a professional organization as a person, not a document
    (AL-TWIN1-2026). KM teams would move from document curators to stewards of person-linked knowledge, which no
    source reports as having happened.
  evidence_grade: C
  sources:
    - { ref: AL-TWIN1-2026, title: "Interview with Twin1 CEO Lewis Liu", publisher: Artificial Lawyer, type: press, url: "https://www.artificiallawyer.com/2026/08/20/interview-with-twin1-ceo-lewis-liu/", date: 2026-08-20, access: full, locator: "answers on 'why', customers and pipeline, and privacy" }
    - { ref: AL-DIDOMENICO-2026, title: "Old Problems, New Tools: Maybe You Need a Knowledge Strategy", publisher: Artificial Lawyer (sponsored), type: press, url: "https://www.artificiallawyer.com/2026/10/15/old-problems-new-tools-maybe-you-need-a-knowledge-strategy/", date: 2026-10-15, access: full, locator: "paragraph 3" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California, COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026, access: full, locator: "Confidentiality row" }
  last_reviewed: 2026-10-19
  notes: >-
    Customer names are the vendor CEO's statement in an interview, not confirmed by the firms. The CEO also cites a
    Kirkland & Ellis plan to spend $500 million on its own AI technology; this was not verified at source and is not
    relied on. Pattern is `other`: a networked set of per-person agents answering from each person's work.

- id: professional-services-knowledge-management-09
  title: In-house legal decisions captured as reusable positions, approved by an attorney
  archetype: professional-services
  module: knowledge-management
  function: risk-compliance-legal
  work_types: [expert-judgment, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    In-house legal teams make thousands of judgment calls a year, and the answer to the next similar request depends on
    which attorney picks it up. Knowledge leaves when attorneys move on.
  solution: >-
    Coheso Memory (in-house legal front-door platform, launched October 2026) proposes positions from resolved
    requests, each with reasoning, conditions, exceptions and prior matters, and surfaces the precedent when a similar
    request arrives. Nothing takes effect until an attorney approves it.
  outcomes:
    - lever: quality
      description: none published; the vendor says answers become faster and more consistent
      figure: none
      measures: not applicable
      provenance: vendor-published
      source_ref: AL-COHESO-2026
  prerequisites:
    - Requests and resolutions run through one system, so decisions are recorded as they happen.
    - Attorney time to approve or reject proposed positions.
  risks_and_guardrails:
    - Coheso says its engineering effort went into deciding whether a resolved request should become a position at all, and separating one matter's particulars from reusable guidance (AL-COHESO-2026).
  human_checkpoints:
    - Attorney approves each proposed position before it takes effect (AL-COHESO-2026).
  role_evolution: >-
    Coheso says departments keep institutional knowledge when attorneys leave and give answers that no longer depend
    on who picks up the request (AL-COHESO-2026). That is a vendor statement, not a reported outcome.
  evidence_grade: C
  sources:
    - { ref: AL-COHESO-2026, title: "Legal Front Door Coheso Launches 'Memory' (AL Interview)", publisher: Artificial Lawyer, type: press, url: "https://www.artificiallawyer.com/2026/10/08/legal-front-door-coheso-launches-memory-al-interview/", date: 2026-10-08, access: full, locator: "paragraphs 1-6 and interview answers on approval" }
  last_reviewed: 2026-10-19
  notes: In-house example. No customer named in the article.

- id: professional-services-knowledge-management-10
  title: Automated capture of engagement knowledge, retrospectives and lessons learned in consulting and engineering firms
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [document-production, research-synthesis]
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    When a project ends, much of the most valuable learning disappears with the team. Lessons-learned documents are
    written late, filed inconsistently and rarely found by the next team.
  solution: >-
    Project capture is automated so outputs, tags and summaries flow into a searchable repository. KMWorld Europe 2026
    (14-15 April) listed Alvarez & Marsal describing a regional KM repository with automated project capture and
    defined KM roles built in three years without executive sponsorship; Simon-Kucher & Partners presenting WeKnow, an
    automated knowledge-capturing system using intelligent tagging and semantic search; and AECOM describing a KM
    framework for programme management that includes the adoption of AI. Certinia advertises a Retrospective Drafter
    agent and a Knowledge Base agent that draft retrospectives and organize lessons learned into a searchable, firm-wide
    knowledge base.
  outcomes:
    - lever: capacity
      description: none published for these firms; the abstracts describe the work and lessons, not measurements
      figure: none
      measures: not applicable
      provenance: self-reported
      source_ref: KMWORLD-EUROPE-2026
  prerequisites:
    - Project artifacts created in systems that capture them (PSA, project records) so automation has source material (CERTINIA-VEDA-2026).
    - KM roles defined and, per the A&M abstract, a grassroots culture where mandates are rare (KMWORLD-EUROPE-2026).
  risks_and_guardrails:
    - The Simon-Kucher abstract does not say whether generative AI is used; it describes intelligent tagging and semantic search (KMWORLD-EUROPE-2026).
    - APQC's article says AI used for KM should be ethical, transparent and built on validated, trustworthy knowledge (KMWORLD-APQC-2026).
    - Client anonymity rules are needed before engagement knowledge is shared across teams (CMR-ACCENTURE-2026).
  human_checkpoints:
    - Project lead confirms what is captured and what is kept confidential to the client.
    - KM team reviews the repository for quality.
  role_evolution: >-
    The A&M abstract reports defining KM roles within three years in a decentralised firm; Buro Happold's KM team
    presented communities of practice as still vital for tacit insight despite AI (KMWORLD-EUROPE-2026).
  evidence_grade: B
  sources:
    - { ref: KMWORLD-EUROPE-2026, title: "KMWorld Europe 2026 Full Programme Listing", publisher: KMWorld, type: conference, url: "https://www.kmworld.com/Europe/2026/Programme.aspx", date: 2026-04-14, access: full, locator: "KMW203 (A&M and Simon-Kucher), KMW402 (AECOM, 15 April), KMW102 (Buro Happold)" }
    - { ref: CERTINIA-VEDA-2026, title: "Certinia AI and Veda agents", publisher: Certinia, type: vendor, url: "https://certinia.com/solutions/ai", date: 2026-10, access: full, locator: "'Value capture & knowledge transfer' and agent list: Knowledge Base Agent, Retrospective Drafter Agent" }
    - { ref: KMWORLD-APQC-2026, title: "The Next Edge in Knowledge Management: KM for the Modern Workforce and the Era of AI", publisher: KMWorld (Lynda Braksiek, APQC), type: press, url: "https://www.kmworld.com/Articles/Editorial/Features/The-Next-Edge-in-Knowledge-Management-KM-for-the-Modern-Workforce-and-the-Era-of-AI-173630.aspx?pageNum=2", date: 2026-03-09, access: full, locator: "paragraphs on lessons learned and AI in KM" }
    - { ref: CMR-ACCENTURE-2026, title: "Tacit Knowledge Is Your Next Competitive Moat", publisher: California Management Review Insight (Accenture authors), type: firm, url: "https://cmr.berkeley.edu/assets/documents/pdf/2026-03-tacit-knowledge-is-your-next-competitive-moat.pdf", date: 2026-03-16, access: full, locator: "professional-services firm paragraph" }
  last_reviewed: 2026-10-19
  notes: >-
    B reflects named firms (Alvarez & Marsal, Simon-Kucher & Partners, AECOM) describing deployed KM work in
    session abstracts for sessions held on 14-15 April 2026. Only the abstracts were read; neither firm reports
    results there. Whether generative AI is used at A&M and Simon-Kucher is unclear. Certinia's agent descriptions are
    vendor catalogue entries without a named customer.

- id: professional-services-knowledge-management-11
  title: Reusable process templates that capture how a recurring type of matter is run
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [coordination-scheduling, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    The process for a recurring matter such as an M&A deal is rebuilt each time from a checklist, a previous deal or the
    memory of people who have done it before.
  solution: >-
    Harvey's Legal Work Orchestration lets innovation and knowledge teams define a template once with phases, tasks,
    playbooks, agents, collaborators and review gates, so a new matter starts with that structure. Kantata markets an
    "always-evolving playbook" built around what excellent delivery looks like in a firm. Pattern is `other`: a reusable
    process definition that carries context into each task.
  outcomes:
    - lever: quality
      description: none published
      figure: none
      measures: not applicable
      provenance: vendor-published
      source_ref: HARVEY-ORCH-2026
  prerequisites:
    - Someone has to write down the phases, tasks and review points of the process (HARVEY-ORCH-2026).
    - Agreement on playbooks and review gates across practice groups.
  risks_and_guardrails:
    - Templates take effect only as far as teams follow them; TRI's premortem says documented processes and aligned incentives decide agentic outcomes (TRI-PREMORTEM-2026).
  human_checkpoints:
    - Lawyers review at designated review gates defined in the template (HARVEY-ORCH-2026).
  role_evolution: >-
    Harvey names innovation and knowledge teams as the authors of the template structure (HARVEY-ORCH-2026).
  evidence_grade: C
  sources:
    - { ref: HARVEY-ORCH-2026, title: "Making Harvey the Orchestration Layer for Legal Work", publisher: Harvey, type: vendor, url: "https://www.harvey.ai/blog/legal-work-orchestration", date: 2026-10-15, access: full, locator: "'Capture the Process in a Reusable Template' and rollout paragraph" }
    - { ref: KANTATA-ENGINE-2026, title: "Kantata Expertise Engine", publisher: Kantata, type: vendor, url: "https://www.kantata.com/ai/expertise-engine", date: 2026, access: full, locator: "page body, 'always-evolving playbook' sentence" }
    - { ref: TRI-PREMORTEM-2026, title: "Premortem: Your 2028 agentic AI pilot program failed", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/feature-agentic-ai-pilot-failure", date: 2026-02-20, access: full, locator: "paragraph on common thread" }
  last_reviewed: 2026-10-19
  notes: >-
    Harvey says Legal Work Orchestration is rolling out across workspaces and templates are in an early access
    programme. Overlaps delivery-management; the KM angle is the capture of know-how in templates.

- id: professional-services-knowledge-management-12
  title: Internal knowledge assistant over a consulting firm's own intellectual property, with expert referral
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Consulting knowledge sits in decks, project files and heads. Consultants cannot easily find what the firm has
    already done, and cannot paste client material into public tools.
  solution: >-
    McKinsey's Lilli searches the firm's knowledge base, summarizes, points to internal content and experts, and
    prepares slides in the firm's format. Infosys built an LLM-based search platform embedded in everyday tools so
    consultants can reuse project artifacts across silos.
  outcomes:
    - lever: capacity
      description: >-
        A McKinsey global head for generative AI said Lilli had received over four million prompt requests in about a
        year, with about 150,000 added each week (interview, August 2024).
      figure: "over 4 million prompts; about 150,000 per week"
      measures: prompt requests to Lilli since mid-2023 and weekly additions, as stated by the named McKinsey executive
      provenance: self-reported
      source_ref: BOERSEN-LILLI-2024
    - lever: capacity
      description: The same interview said over 75% of employees had tested Lilli since the second half of 2023.
      figure: "over 75% of employees"
      measures: employees who had tested the platform, per the McKinsey executive; denominator not given
      provenance: self-reported
      source_ref: BOERSEN-LILLI-2024
    - lever: speed
      description: >-
        A secondary report of Business Insider says McKinsey states employees saved 30% of their time and saw a 20%
        improvement in content quality and accuracy.
      figure: "30% time saved; 20% quality and accuracy improvement"
      measures: not defined in the source; relayed from Business Insider by a news site, original not opened
      provenance: self-reported
      source_ref: OFFICECHAI-LILLI-2025
    - lever: speed
      description: >-
        Infosys, per an APQC researcher, cut search times by 50% and raised user satisfaction by 80% with its AI search
        platform.
      figure: "search times reduced by 50%; user satisfaction boosted by 80%"
      measures: source states both figures without baseline, sample or who measured them
      provenance: self-reported
      source_ref: KMWORLD-APQC-2026
  prerequisites:
    - Curated corpus; the Business Insider report relayed by Officechai describes about 100,000 documents (OFFICECHAI-LILLI-2025).
    - Secure environment; the same source says consultants lack access to ChatGPT (OFFICECHAI-LILLI-2025).
  risks_and_guardrails:
    - McKinsey's executive said everything that goes out to a client must be reviewed by a person first (BOERSEN-LILLI-2024).
    - BCG's 750-consultant experiment, cited in the same article, found AI-assisted consultants did worse on a data-analysis task because they sometimes accepted incorrect AI conclusions (BOERSEN-LILLI-2024).
  human_checkpoints:
    - Consultant reviews all output before it reaches a client (BOERSEN-LILLI-2024).
  role_evolution: >-
    Over 120 people contribute part of their time to the platform's development at McKinsey, per the executive
    interviewed (BOERSEN-LILLI-2024).
  evidence_grade: B
  sources:
    - { ref: BOERSEN-LILLI-2024, title: "AI in consulting: more than just creating slide presentations", publisher: Börsen-Zeitung, type: press, url: "https://boersen-zeitung.de/english/ai-in-consulting-more-than-just-creating-slide-presentations", date: 2024-08-26, access: full, locator: "paragraphs 2-4" }
    - { ref: OFFICECHAI-LILLI-2025, title: "McKinsey Has Built An Internal AI Chatbot Named Lilli Which Is Used By 70% Of Employees", publisher: OfficeChai (relaying Business Insider), type: press, url: "https://officechai.com/ai/mckinsey-has-built-an-internet-ai-chatbot-named-lilli-which-is-used-by-70-of-employees/", date: 2025-04-28, access: full, locator: "paragraphs 2-4" }
    - { ref: KMWORLD-APQC-2026, title: "The Next Edge in Knowledge Management: KM for the Modern Workforce and the Era of AI", publisher: KMWorld (Lynda Braksiek, APQC), type: press, url: "https://www.kmworld.com/Articles/Editorial/Features/The-Next-Edge-in-Knowledge-Management-KM-for-the-Modern-Workforce-and-the-Era-of-AI-173630.aspx?pageNum=2", date: 2026-03-09, access: full, locator: "Infosys paragraph near the end" }
  last_reviewed: 2026-10-19
  notes: >-
    The McKinsey interview is from August 2024, outside the 12-18 month window; kept as the best named-firm account
    of the pattern. The McKinsey website returned 403 so no primary McKinsey page was read, and the Officechai
    page is a secondary relay, so its 70% and 17-uses-a-week figures are not repeated as outcomes. Grade B, not A:
    usage counts and unmeasured savings claims are not a measured outcome of the module's work. The Infosys article
    is a trade-press piece by APQC, not an Infosys publication, and Infosys is an IT-services consultancy.

- id: professional-services-knowledge-management-13
  title: Role-specific onboarding briefs from engagement or matter institutional memory
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    New team members spend time getting oriented in a complex matter or engagement by reading files and asking
    colleagues.
  solution: >-
    NetDocuments generates a matter overview from all documents and correspondence, with key parties, dates, team
    members and a timeline. Kantata says its superagent holds institutional memory of each engagement (statements of
    work, meeting notes, past decisions, client history) so each new resource receives a role-specific brief and
    project plan from day one.
  outcomes:
    - lever: speed
      description: none published
      figure: none
      measures: not applicable
      provenance: vendor-published
      source_ref: LAWSITES-NETDOCS-2026
  prerequisites:
    - Complete and well-tagged matter or engagement records.
    - Permissions so a new joiner sees only what they are cleared to see.
  risks_and_guardrails:
    - Summaries inherit permissions and ethical walls according to NetDocuments (LAWSITES-NETDOCS-2026).
  human_checkpoints:
    - Matter or engagement lead reviews the brief before the new joiner relies on it.
  role_evolution: >-
    Junior lawyers' orientation time moves from reading to checking a generated overview; NetDocuments frames this as
    reducing the time a new associate spends getting oriented (LAWSITES-NETDOCS-2026).
  evidence_grade: C
  sources:
    - { ref: LAWSITES-NETDOCS-2026, title: "NetDocuments Unveils Legal Context Graph ...", publisher: LawSites, type: press, url: "https://www.lawnext.com/2026/05/netdocuments-unveils-legal-context-graph-to-map-legal-knowledge-alongside-a-reimagined-platform.html", date: 2026-05-14, access: full, locator: "Matter Overview paragraph" }
    - { ref: KANTATA-EXPERTISE-AGENT-2026, title: "Kantata Expertise Agent and Workflows", publisher: Kantata, type: vendor, url: "https://www.kantata.com/ai/expertise-agent-and-workflows", date: 2026, access: full, locator: "superagent paragraph" }
  last_reviewed: 2026-10-19
  notes: Kantata page is undated; accessed 2026-10-19. Neither source names a customer for this feature.

- id: professional-services-knowledge-management-14
  title: Chat over the work product that explains why a reviewer changed a return or document
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [research-synthesis, expert-judgment]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >-
    Accountants learned client context by preparing returns repeatedly and by waiting for a partner to explain review
    changes. If AI removes the grunt work, firm know-how risks never being passed on.
  solution: >-
    Ascend's CEO describes a "closed loop" in which the firm controls its software so every workflow trace, field
    correction and client preference can compound into a data set AI learns from, plus a chat feature inside the work
    product that lets staff ask what changed in a return and why the partner changed it.
  outcomes:
    - lever: experience
      description: >-
        The CEO recounted one firm saying its spring-busy-season interns reached staff level without extra training.
        This is a second-hand anecdote, not a measurement.
      figure: none
      measures: not applicable; anecdote relayed on a podcast
      provenance: vendor-published
      source_ref: ACCTODAY-AINATIVE-2026
  prerequisites:
    - Firm-controlled software stack so corrections and communications are captured (ACCTODAY-AINATIVE-2026).
    - Experienced professionals willing to get their knowledge out of their heads (ACCTODAY-AINATIVE-2026).
  risks_and_guardrails:
    - The host asks whether staff who do less return preparation can be as well informed about clients; the guest answers with training and self-teaching (ACCTODAY-AINATIVE-2026).
    - The CEO says handing over so much institutional know-how and client context to outside vendors would leave a firm vulnerable (ACCTODAY-AINATIVE-2026).
  human_checkpoints:
    - Partner review of the return remains the source of the explanation the chat draws on.
  role_evolution: >-
    The CEO says firms will want to hire curious young people who can teach themselves from compounded firm know-how
    (ACCTODAY-AINATIVE-2026). Learning effects are routed to talent-learning.
  evidence_grade: C
  sources:
    - { ref: ACCTODAY-AINATIVE-2026, title: "The AI-native firm (On the Air with Accounting Today)", publisher: Accounting Today, type: podcast, url: "https://www.accountingtoday.com/podcast/the-ai-native-firm", date: 2026-10-19, access: full, locator: "transcript at 01:16 (closed loop), 05:01 (interns and chat), 16:06 (incumbents)" }
  last_reviewed: 2026-10-19
  notes: >-
    Ascend is a PE-backed accounting-firm platform with a 30-person AI team per the host. The guest is the vendor's
    CEO, so claims are vendor-side. The transcript is AI-generated per the page.

- id: professional-services-knowledge-management-15
  title: "Idea: firms share their knowledge with clients through AI portals and agents"
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [client-interaction, document-production]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Clients, especially in-house teams, increasingly want legal answers through AI tools. Firms' knowledge is
    inaccessible to those tools, and a general counsel in a conference conversation said law firm use of AI gives
    them nothing in return.
  solution: >-
    Firms expose parts of their knowledge to clients through AI interfaces. Oz Benamram of SKILLS argued on the Law
    Punx show that firms have about two years, until the end of 2027, to set up knowledge-sharing strategies before
    not doing so causes a "drought". Artificial Lawyer says Legora has launched a Portal and Eudia is developing a
    'legal brain' strategy.
  outcomes:
    - lever: growth
      description: none published; idea discussed by practitioners
      figure: none
      measures: not applicable
      provenance: self-reported
      source_ref: AL-LAWPUNX-2025
  prerequisites:
    - Client-ready, governed knowledge assets with clear ownership of the firm's intellectual property.
  risks_and_guardrails:
    - Client-facing sharing raises confidentiality and privilege questions that sources reviewed do not address; California's guidance on confidentiality applies to any agentic system with access to firm files (CALBAR-GENAI-2026).
  human_checkpoints:
    - Partner decides which knowledge assets may be shared.
  role_evolution: >-
    Artificial Lawyer reports a general counsel at a conference of 500+ in-house lawyers saying law firms' AI use brings
    them no change and probably higher bills next year (AL-CLIENT-2026). That puts pressure on firms to show client-facing
    value from their knowledge.
  evidence_grade: D
  sources:
    - { ref: AL-LAWPUNX-2025, title: "Law Punx: 'Law Firms Must Share Their Knowledge Via AI'", publisher: Artificial Lawyer, type: podcast, url: "https://www.artificiallawyer.com/2025/11/11/law-punx-law-firms-must-share-their-knowledge-via-ai/", date: 2025-11-11, access: full, locator: "paragraphs 1-3 and bullet summary" }
    - { ref: AL-CLIENT-2026, title: "'We Get Nothing' From Law Firm AI Use, Says Client", publisher: Artificial Lawyer, type: press, url: "https://www.artificiallawyer.com/2026/02/12/we-get-nothing-from-law-firm-ai-use-client/", date: 2026-02-12, access: full, locator: "opening paragraphs" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California, COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026, access: full, locator: "Confidentiality row" }
  last_reviewed: 2026-10-19
  notes: >-
    Idea. The Law Punx item is a video blast; only Artificial Lawyer's written summary was read. The Legora Portal
    and Eudia statements are Artificial Lawyer's, not verified at source.

- id: professional-services-knowledge-management-16
  title: "Idea: AI-assisted capture of departing partners' know-how before retirement"
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [expert-judgment, research-synthesis]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Senior professionals are retiring or leaving, and their tacit knowledge goes with them. A Thomson Reuters audit-product
    leader said 75% of audit partners are scheduled to retire within ten years; the source gives no dataset.
  solution: >-
    Structured exit interviews and work-product analysis that feed an AI-assisted knowledge base. TechnipFMC (not a
    professional-services firm) built a knowledge-transfer plan for each departing expert by interviewing experts and
    colleagues and inventorying at-risk knowledge, with no AI described. The Twin1 CEO says AI twins could help firms
    preserve the knowledge of partners approaching retirement.
  outcomes:
    - lever: risk
      description: none published
      figure: none
      measures: not applicable
      provenance: vendor-published
      source_ref: AL-TWIN1-2026
  prerequisites:
    - Early identification of at-risk knowledge holders.
    - Willingness of senior people to be interviewed and have their work analysed.
  risks_and_guardrails:
    - The retirement figure comes from a vendor interview and is unverified (TR-AUDIT-2026).
  human_checkpoints:
    - Departing expert reviews what is recorded about their judgment before it is published.
  role_evolution: >-
    The Accenture authors say a leading automaker's engineers, retiring in numbers, left tacit knowledge that had to be
    captured by agents (CMR-ACCENTURE-2026). KM teams would run structured transfer programmes.
  evidence_grade: D
  sources:
    - { ref: KMWORLD-APQC-2026, title: "The Next Edge in Knowledge Management: KM for the Modern Workforce and the Era of AI", publisher: KMWorld (Lynda Braksiek, APQC), type: press, url: "https://www.kmworld.com/Articles/Editorial/Features/The-Next-Edge-in-Knowledge-Management-KM-for-the-Modern-Workforce-and-the-Era-of-AI-173630.aspx?pageNum=2", date: 2026-03-09, access: full, locator: "TechnipFMC paragraph" }
    - { ref: CMR-ACCENTURE-2026, title: "Tacit Knowledge Is Your Next Competitive Moat", publisher: California Management Review Insight (Accenture authors), type: firm, url: "https://cmr.berkeley.edu/assets/documents/pdf/2026-03-tacit-knowledge-is-your-next-competitive-moat.pdf", date: 2026-03-16, access: full, locator: "section 'Map Tacit Knowledge', automaker example" }
    - { ref: AL-TWIN1-2026, title: "Interview with Twin1 CEO Lewis Liu", publisher: Artificial Lawyer, type: press, url: "https://www.artificiallawyer.com/2026/08/20/interview-with-twin1-ceo-lewis-liu/", date: 2026-08-20, access: full, locator: "answer on Kirkland and compounding knowledge, partners approaching retirement" }
    - { ref: TR-AUDIT-2026, title: "State of AI in audit", publisher: Thomson Reuters Tax & Accounting blog, type: vendor, url: "https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/", date: 2026-03-30, access: full, locator: "question 1" }
  last_reviewed: 2026-10-19
  notes: >-
    Idea. The audit-specific context belongs to the assurance archetype; only the workforce statement is used here.
    Practitioners discuss the problem widely; no professional-services firm reports an AI-assisted retirement-capture
    programme in sources read.

- id: professional-services-knowledge-management-17
  title: "Idea: interview-based tacit-knowledge elicitation with AI-drafted stories"
  archetype: professional-services
  module: knowledge-management
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Lessons-learned documents capture facts but not the judgment, so reuse is shallow.
  solution: >-
    A KMWorld Europe 2026 workshop (13 April) taught pairwise interviews, generative-AI-supported story prototypes and a
    Tacit Knowledge Canvas, embedded in communities of practice. The Accenture authors propose mapping where
    expertise resides before codifying it.
  outcomes:
    - lever: quality
      description: none published
      figure: none
      measures: not applicable
      provenance: self-reported
      source_ref: KMWORLD-EUROPE-2026
  prerequisites:
    - Skilled interviewers and psychological safety for experts to tell failures.
    - Communities of practice where stories are shared.
  risks_and_guardrails:
    - The workshop abstract says AI supports rather than replaces the interview (KMWORLD-EUROPE-2026).
    - The Accenture authors warn against flattening judgment into oversimplified rules (CMR-ACCENTURE-2026).
  human_checkpoints:
    - Interviewee approves the story before it is shared.
  role_evolution: >-
    KM staff act as interviewers and facilitators; the KMWorld Europe 2026 programme included a session on KM professional
    development (KMWORLD-EUROPE-2026).
  evidence_grade: D
  sources:
    - { ref: KMWORLD-EUROPE-2026, title: "KMWorld Europe 2026 Full Programme Listing", publisher: KMWorld, type: conference, url: "https://www.kmworld.com/Europe/2026/Programme.aspx", date: 2026-04-13, access: full, locator: "workshop KMW1 abstract" }
    - { ref: CMR-ACCENTURE-2026, title: "Tacit Knowledge Is Your Next Competitive Moat", publisher: California Management Review Insight (Accenture authors), type: firm, url: "https://cmr.berkeley.edu/assets/documents/pdf/2026-03-tacit-knowledge-is-your-next-competitive-moat.pdf", date: 2026-03-16, access: full, locator: "'Codify Tacit Knowledge Without Flattening It'" }
  last_reviewed: 2026-10-19
  notes: >-
    Idea; workshop was not specific to professional services. Held on 13 April 2026; only the abstract was read.
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Capture** knowledge at the point of work: project closure, retrospectives, lessons learned, exit interviews, decision records. Work types: document-production, research-synthesis.
- **Curate and validate**: decide what is final, exemplary or superseded; set rules for what may be shared (client anonymity thresholds); partner or senior review. Work type: review-assurance.
- **Organize and tag**: taxonomy, metadata, classification, ontologies and knowledge graphs; OCR of scans. Work types: data-reporting, software-systems.
- **Find and reuse**: enterprise search, precedent and clause libraries, expertise location, matter and engagement briefs. Work type: research-synthesis.
- **Apply in delivery**: playbooks, process templates, review gates. Work types: document-production, coordination-scheduling.
- **Govern access**: permissions, ethical walls, client restrictions, audit trail, AI-tool connectors. Work type: review-assurance.
- **Sustain**: communities of practice, KM roles, usage and value measurement. Work type: coordination-scheduling.

### Common pain points

- Lawyers will not take time to share what they know; incentives and sponsorship, not tools, are the blocker (AL-DIDOMENICO-2026).
- Precedent stores mix drafts, executed documents and counterparty versions; nobody records why a document was final (DRAFTWISE-PRECEDENT-2025; AL-DIDOMENICO-2026).
- Fragmented systems and "just ask Linda" institutional memory break agentic pilots (TRI-PREMORTEM-2026).
- Knowledge infrastructure for enterprise search and expertise management is underdeveloped (ILTA-TECHSURVEY-2026, p. 9).
- Practitioners complain about pilot fatigue and integration: "There's only so many tabs lawyers will open" (DRAFTWISE-ILTACON-2025).
- Value from AI is hard to show clients; firms say they are still gathering data (TRI-LEGALWEEK-2026).
- KM keeps being re-positioned in the org chart (IT, library, innovation, legal engineering) (AL-DIDOMENICO-2026).

### Metrics and benchmarks (with what each measures)

- Law firm technology spend rose nearly 11% in 2025 and KM spend about 10%; over 2021 to 2025 tech spend rose 39.3% and KM spend 37.2% against 2021 levels (TRI-SOTLM-2026, article by TRI analyst on the TRI and Georgetown report).
- 94% of 508 responding firms engage with GenAI, up 14 points (ILTA-TECHSURVEY-2026, p. 3). Many firms expect added headcount in knowledge management among other functions (p. 5).
- iManage vendor survey (3,000+ decision makers): 85% at some stage of AI adoption, 36% experienced a policy violation, 25% report public AI use with little oversight, 27% of the most mature organizations fully integrated versus 3% of the least mature (IMANAGE-BENCH-2026).
- NetDocuments internal benchmark: cost per correct answer $0.68 to $0.36 with the context graph (NETDOCS-LCEB-2026).
- Law library staffing averages 6.6 FTE in 2025 versus 4.6 in 2019; firm and corporate law libraries 7.9; survey of 257 organizations, 45% response; chief knowledge officers average $193,767 (LAWSITES-AALL-2025). The report does not attribute these changes to AI.
- McKinsey Lilli usage: over four million prompts, about 150,000 added weekly, more than 75% of employees had tested it (BOERSEN-LILLI-2024).

### Guardrails and regulatory points

- California State Bar guidance (2026) names knowledge bases and document management systems among internal systems an agentic tool might reach, says poorly configured systems may disclose information across matters, and bars autonomous external transmission of client data without safeguards and human review (CALBAR-GENAI-2026).
- Ethical walls and existing permissions must carry through to every search layer and connector; vendors say they do (LAWSITES-HARVEYDJ-2026; LAWSITES-NETDOCS-2026; LAWSITES-IMANAGECHATGPT-2026). No independent test of these claims was found.
- Governance of the knowledge itself: who may add, who vets, how anonymity is protected (CMR-ACCENTURE-2026).

### Frontier signals (dated and sourced)

- 2026-10-16: Legora announced plans to connect to the iManage MCP Server (LAWSITES-LEGORAIM-2026).
- 2026-10-15: Harvey said innovation and knowledge teams can define reusable matter templates; rollout under way, template early access (HARVEY-ORCH-2026).
- 2026-10-15: Artificial Lawyer published a KM leader's argument that firms need a knowledge strategy rather than an AI strategy; the KM&I for Legal conference is scheduled for 21-22 October in New York (AL-DIDOMENICO-2026). Scheduled event: not used for any grade.
- 2026-10-08: Coheso launched Memory for in-house teams (AL-COHESO-2026).
- 2026-09-17: iManage announced a plug-in for ChatGPT Enterprise (LAWSITES-IMANAGECHATGPT-2026).
- 2026-08-20: Twin1 launched AI twins for lawyers after a $20m raise (AL-TWIN1-2026).
- 2026-08-13: DeepJudge released the Agent Handoff Protocol; Harvey building, Thomson Reuters says it will support (LAWSITES-DEEPJUDGE-2026).
- 2026-08/09: ILTACON 2026 news dominated by MCP and agentic AI; "context" the word of the conference (LAWSITES-ILTACON3-2026; EDISCOVERYTODAY-ILTACON-2026).
- 2026-05-20: Harvey and DeepJudge partnership targeting the "context tax" (LAWSITES-HARVEYDJ-2026).
- 2026-05-14: NetDocuments Legal Context Graph (private preview) (LAWSITES-NETDOCS-2026).
- 2026-03-09 to 11 (Legalweek): scheduled sessions on "What KM Must Still Control" and "KM, DMS, and LLMs in Harmony" (EDRM-LEGALWEEK-2026). Abstract-level signal only.
- 2025-11-11: SKILLS founder argued firms have until end of 2027 to share knowledge with clients via AI (AL-LAWPUNX-2025).

### Workforce and role effects

- Knowledge services are being consolidated under AI or innovation leaders: Eversheds Sutherland (2026-01-26, AL-EVERSHEDS-2026), K&L Gates "Global AI and Innovation Partner" role that includes data and knowledge management (2026-05-06, AL-X4-2026), Gilchrist Connell "chief AI and knowledge officer" bringing learning, KM and AI under one mandate (2026-07-06, LAWYERSWEEKLY-GILCHRIST-2026).
- A KM leader argues for growing people in KM, library and research teams and recruiting practising attorneys into KM roles instead of hunting for a unicorn (AL-DIDOMENICO-2026).
- A 2026 book from Globe Law and Business says KM is moving into a strategic function tied to profitability; a reviewer in the Law Society Gazette said KM staff and data personnel are now central to firm performance (GLB-FUTUREKM-2026, publisher page).
- Concern that AI removes entry-level work that taught tacit knowledge: NBER trial of 133 patent lawyers found a durable skill advantage concentrated among seniors (NBER-AUTOR-2026); routed to talent-learning.

### Objections and concerns practitioners raise

- "Old problems, new tools": the participation problem has not gone away (AL-DIDOMENICO-2026).
- Quality of what is retrieved: garbage in, garbage out (DRAFTWISE-PRECEDENT-2025).
- Reviewer overload: AI output makes the human reviewer the bottleneck, with emerging research on supervision load (AL-DIDOMENICO-2026).
- Pilot fatigue and tool sprawl; integration needed (DRAFTWISE-ILTACON-2025).
- Vendor lock-in and open protocols versus proprietary context (LAWSITES-DEEPJUDGE-2026; LAWSITES-ILTACON3-2026).
- Cost: seat-based to consumption-based pricing, "tokengeddon" (EDISCOVERYTODAY-ILTACON-2026).
- Giving a vendor too much institutional know-how and client context (ACCTODAY-AINATIVE-2026).
- Clients see no benefit from firm AI (AL-CLIENT-2026).
- Privacy of individuals when building person-level models (no source addresses; a gap).

### Interview probes for an advisor

1. Where does your precedent live today, who decides what counts as "final" or "good", and is that decision recorded anywhere an AI could use?
2. When someone asks "who has done this before?", how is it answered, how current is the answer, and would your lawyers accept being surfaced from time and matter data?
3. What happens to a retiring partner's know-how and client relationships? Is there a capture process, and would you allow an AI model of a person?
4. Which AI tools can see which matters, and who controls ethical walls and client restrictions in those connections?
5. How would you know if search or an assistant gave wrong answers? Is there a test set, an owner, and any before-and-after measurement?

---

## 4. Routed to other modules

- **staffing-resourcing**: Kantata Expertise Agent ranks people by skills and experience for projects; Certinia Resourcing and Staffing agents (KANTATA-EXPERTISE-AGENT-2026; CERTINIA-VEDA-2026).
- **pursuit-proposals**: proposals built from past work (Kantata customer quote "proposals practically build themselves"; Certinia RFP Responder) (KANTATA-ENGINE-2026; CERTINIA-VEDA-2026).
- **client-development**: Litera business-development intelligence from siloed firm data (LAWSITES-ILTACON4-2026).
- **quality-review**: playbook-based contract review against institutional positions (iManage Ask playbook analysis, SimpleDocs) (LAWSITES-IMANAGE-2026; LAWSITES-SIMPLEDOCS-2026); BCG experiment result on wrong AI conclusions (BOERSEN-LILLI-2024); reviewer overload and hallucination concerns (AL-DIDOMENICO-2026).
- **firm-finance and quality-review**: Harvey Command Center usage analytics and benchmarking for KM and innovation leaders; Legalweek ROI and measurement sessions (LAWSITES-HARVEYDJ-2026; EDRM-LEGALWEEK-2026); consumption pricing (EDISCOVERYTODAY-ILTACON-2026).
- **scoping-pricing and billing-collections**: client demands for AI line items and "we get nothing" client view (TRI-LEGALWEEK-2026; AL-CLIENT-2026).
- **talent-learning**: junior skill effects (NBER-AUTOR-2026); Ascend interns learning from chat over work product (ACCTODAY-AINATIVE-2026); new combined AI and knowledge officer roles (LAWYERSWEEKLY-GILCHRIST-2026).
- **acceptance-risk (in-house intake)**: Coheso legal front door and Legora Intake (AL-COHESO-2026).
- **assurance archetype (practice-specific, out of scope)**: PwC ChatNational, a research assistant for US assurance staff over the firm's own guidance, announced 2024-08-01, outside the window (ACCTODAY-CHATNATIONAL-2024). Not graded here.

---

## 5. Sources

All sources were opened and read (`access: full`) unless stated; the three read through the text mirror are noted. Types per the vocabulary.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| ILTA-TECHSURVEY-2026 | ILTA Technology Survey 2026 Executive Summary | ILTA | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026 |
| TRI-SOTLM-2026 | State of the US Legal Market 2026 analysis: Will the AI bubble burst? | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble | 2026-01-14 |
| IMANAGE-BENCH-2026 | iManage Knowledge Work Benchmark Report 2026 (summary page) | iManage | survey | https://imanage.com/benchmark-report-2026/ | 2026 |
| IMANAGE-NEWS-2026 | Law News: Most firms are experimenting with AI; only 17% use it daily | iManage | vendor | https://imanage.com/resources/resource-center/news/law-news-most-firms-are-experimenting-with-ai-only-17-actually-use-it-daily/ | 2026-02-11 |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative AI in the Practice of Law | State Bar of California, COPRAC | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026 |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? (NBER WP 35720, abstract) | NBER via EconPapers | academic | https://econpapers.repec.org/RePEc:nbr:nberwo:35720 | 2026 |
| CMR-ACCENTURE-2026 | Tacit Knowledge Is Your Next Competitive Moat | California Management Review Insight (Accenture authors) | firm | https://cmr.berkeley.edu/assets/documents/pdf/2026-03-tacit-knowledge-is-your-next-competitive-moat.pdf | 2026-03-16 |
| NETDOCS-LCEB-2026 | 2026 Legal Context Engineering Benchmark Report (read via text mirror) | NetDocuments | vendor | https://www.netdocuments.com/?p=11503 | 2026-08 |
| LAWSITES-NETDOCS-2026 | NetDocuments Unveils Legal Context Graph | LawSites | press | https://www.lawnext.com/2026/05/netdocuments-unveils-legal-context-graph-to-map-legal-knowledge-alongside-a-reimagined-platform.html | 2026-05-14 |
| LAWSITES-IMANAGE-2026 | iManage Unveils Next Evolution of Platform at ConnectLive 2026 | LawSites (release reproduced) | press | https://www.lawnext.com/2026/05/imanage-unveils-next-evolution-of-platform-at-connectlive-2026-as-organizations-prepare-for-the-next-era-of-ai-ready-knowledge-work.html | 2026-05-22 |
| LAWSITES-HARVEYDJ-2026 | Harvey Launches Command Center ... Partners with DeepJudge | LawSites | press | https://www.lawnext.com/2026/05/harvey-launches-command-center-for-managing-enterprise-ai-adoption-and-partners-with-deepjudge-on-institutional-knowledge.html | 2026-05-20 |
| LAWSITES-ILTACON3-2026 | ILTACON News Round-Up Part 3, Documents, Data and AI | LawSites | press | https://www.lawnext.com/2026/09/iltacon-news-round-up-part-3-documents-data-and-ai-imanage-netdocuments-entegrata-wolters-kluwer-thomson-reuters-clio-avvoka.html | 2026-09-04 |
| LAWSITES-ILTACON4-2026 | ILTACON News Round-Up Part 4, The Business of Law | LawSites | press | https://www.lawnext.com/2026/09/iltacon-news-round-up-part-4-the-business-of-law-litera-aderant-oddr-tre-ai-intapp.html | 2026-09-04 |
| LAWSITES-LEGORAIM-2026 | Legora and iManage Deepen Integration Through iManage MCP Server | LawSites (release reproduced) | press | https://www.lawnext.com/2026/10/legora-and-imanage-deepen-integration-through-imanagemcp-server.html | 2026-10-19 |
| LAWSITES-IMANAGECHATGPT-2026 | iManage to Deliver Governed AI-Powered Knowledge Work in ChatGPT Enterprise | LawSites (release reproduced) | press | https://www.lawnext.com/2026/09/imanage-to-deliver-governed-ai-powered-knowledge-work-in-chatgpt-enterprise.html | 2026-09-21 |
| LAWSITES-DEEPJUDGE-2026 | DeepJudge Releases an Open Protocol for Passing Users and Their Context Between AI Products | LawSites | press | https://www.lawnext.com/2026/08/deepjudge-releases-an-open-protocol-for-passing-users-and-their-context-between-ai-products-with-harvey-and-thomson-reuters-on-board.html | 2026-08-13 |
| LAWSITES-SIMPLEDOCS-2026 | SimpleDocs Launches Contract Intelligence Layer | LawSites | press | https://www.lawnext.com/2026/02/simpledocs-launches-contract-intelligence-layer-putting-policy-precedent-and-market-data-inside-microsoft-word.html | 2026-02-18 |
| LAWSITES-SPELLBOOK-2025 | Introducing Spellbook Library | LawSites | press | https://www.lawnext.com/2025/07/introducing-spellbook-library-contract-ai-that-learns-from-your-precedents.html | 2025-07-31 |
| LAWSITES-LITERA-2025 | Litera Expands Litera One Platform with New Drafting and KM Features | LawSites | press | https://www.lawnext.com/2025/07/litera-expands-litera-one-platform-with-new-drafting-and-knowledge-management-features.html | 2025-07-31 |
| LAWSITES-AALL-2025 | What Do Law Librarians Earn? New AALL Salary Survey | LawSites | press | https://www.lawnext.com/2025/11/what-do-law-librarians-earn-new-aall-salary-survey-provides-details.html | 2025-11-25 |
| ABAJ-ILTACON-2026 | ILTACON 2026: The race to connect the dots and the data | ABA Journal | press | https://www.abajournal.com/columns/article/iltacon-2026-and-the-race-to-connect-the-dots | 2026-09-02 |
| EDISCOVERYTODAY-ILTACON-2026 | My Five ILTACON 2026 Takeaways | eDiscovery Today | press | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 |
| DRAFTWISE-ILTACON-2025 | Key Takeaways from ILTACON 2025 | Draftwise | vendor | https://www.draftwise.com/blog/key-takeaways-from-iltacon-2025-from-demos-to-day-to-day-impact | 2025-08-19 |
| DRAFTWISE-PRECEDENT-2025 | Garbage In, Garbage Out: How to Build a Precedent Database Lawyers Can Trust | Draftwise | vendor | https://www.draftwise.com/blog/garbage-in-garbage-out-how-to-build-a-precedent-database-your-lawyers-can-trust | 2025-09-24 |
| AL-DIDOMENICO-2026 | Old Problems, New Tools: Maybe You Need a Knowledge Strategy (sponsored) | Artificial Lawyer | press | https://www.artificiallawyer.com/2026/10/15/old-problems-new-tools-maybe-you-need-a-knowledge-strategy/ | 2026-10-15 |
| AL-LAWPUNX-2025 | Law Punx: 'Law Firms Must Share Their Knowledge Via AI' | Artificial Lawyer | podcast | https://www.artificiallawyer.com/2025/11/11/law-punx-law-firms-must-share-their-knowledge-via-ai/ | 2025-11-11 |
| AL-TRKNOWLEDGE-2025 | Thomson Reuters Launches 'CoCounsel Knowledge Search' | Artificial Lawyer | press | https://www.artificiallawyer.com/2025/07/09/thomson-reuters-launches-cocounsel-knowledge-search/ | 2025-07-09 |
| AL-EVERSHEDS-2026 | Eversheds Sutherland Establishes AI-Centric US Innovation Dept | Artificial Lawyer | press | https://www.artificiallawyer.com/2026/01/26/eversheds-sutherland-establishes-ai-centric-us-innovation-dept/ | 2026-01-26 |
| AL-X4-2026 | Law Firms Do Innovation x4 | Artificial Lawyer | press | https://www.artificiallawyer.com/2026/05/06/law-firms-do-innovation-x4/ | 2026-05-06 |
| AL-CLIENT-2026 | 'We Get Nothing' From Law Firm AI Use, Says Client | Artificial Lawyer | press | https://www.artificiallawyer.com/2026/02/12/we-get-nothing-from-law-firm-ai-use-client/ | 2026-02-12 |
| AL-COHESO-2026 | Legal Front Door Coheso Launches 'Memory' | Artificial Lawyer | press | https://www.artificiallawyer.com/2026/10/08/legal-front-door-coheso-launches-memory-al-interview/ | 2026-10-08 |
| AL-TWIN1-2026 | Interview with Twin1 CEO Lewis Liu | Artificial Lawyer | press | https://www.artificiallawyer.com/2026/08/20/interview-with-twin1-ceo-lewis-liu/ | 2026-08-20 |
| AL-IMANAGE-WEBINAR-2026 | Webinar: Why Context and Governance Will Shape Legal AI's Future (iManage, 8 Oct) | Artificial Lawyer | press | https://www.artificiallawyer.com/2026/09/24/webinar-why-context-governance-will-shape-legal-ais-future/ | 2026-09-24 |
| TRI-PREMORTEM-2026 | Premortem: Your 2028 agentic AI pilot program failed | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/feature-agentic-ai-pilot-failure | 2026-02-20 |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 |
| EDRM-LEGALWEEK-2026 | Legalweek 2026 (Select) Educational Sessions Preview (read via text mirror) | EDRM | conference | https://edrm.net/2026/03/legalweek-2026-select-educational-sessions-preview/ | 2026-03-06 |
| KMWORLD-EUROPE-2026 | KMWorld Europe 2026 Full Programme Listing | KMWorld | conference | https://www.kmworld.com/Europe/2026/Programme.aspx | 2026-04-14 |
| KMWORLD-APQC-2026 | The Next Edge in Knowledge Management (Braksiek, APQC) | KMWorld | press | https://www.kmworld.com/Articles/Editorial/Features/The-Next-Edge-in-Knowledge-Management-KM-for-the-Modern-Workforce-and-the-Era-of-AI-173630.aspx?pageNum=2 | 2026-03-09 |
| KMEDUHUB-ILTACON-2026 | ILTACON programme listing (KM-related sessions) | KM Education Hub | conference | https://kmeducationhub.de/international-legal-technology-association-conference-iltacon/ | 2026-08-23 |
| KMI-LEGAL-2026 | KM and Innovation for Legal Conference site (event scheduled 21-22 Oct 2026 per AL-DIDOMENICO-2026) | LegalTech Connect | conference | https://kmiforlegal.com | 2026-10 |
| GLB-FUTUREKM-2026 | The Future of Legal Knowledge Management: Harnessing Artificial Intelligence (book page with reviews) | Globe Law and Business | press | https://www.globelawandbusiness.com/books/the-future-of-legal-knowledge-management-harnessing-artificial-intelligence | 2026-01 |
| ACCTODAY-AINATIVE-2026 | The AI-native firm (On the Air with Accounting Today, transcript) | Accounting Today | podcast | https://www.accountingtoday.com/podcast/the-ai-native-firm | 2026-10-19 |
| ACCTODAY-CHATNATIONAL-2024 | PwC rolls out research bot ChatNational for staff | Accounting Today | press | https://accountingtoday.com/news/pwc-rolls-out-research-bot-chatnational-for-staff | 2024-08-01 |
| TR-AUDIT-2026 | State of AI in audit | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/ | 2026-03-30 |
| BOERSEN-LILLI-2024 | AI in consulting: more than just creating slide presentations | Börsen-Zeitung | press | https://boersen-zeitung.de/english/ai-in-consulting-more-than-just-creating-slide-presentations | 2024-08-26 |
| OFFICECHAI-LILLI-2025 | McKinsey Has Built An Internal AI Chatbot Named Lilli (relays Business Insider) | OfficeChai | press | https://officechai.com/ai/mckinsey-has-built-an-internet-ai-chatbot-named-lilli-which-is-used-by-70-of-employees/ | 2025-04-28 |
| CERTINIA-VEDA-2026 | Certinia AI and Veda agents | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10 |
| KANTATA-ENGINE-2026 | Kantata Expertise Engine | Kantata | vendor | https://www.kantata.com/ai/expertise-engine | 2026 |
| KANTATA-EXPERTISE-AGENT-2026 | Kantata Expertise Agent and Workflows | Kantata | vendor | https://www.kantata.com/ai/expertise-agent-and-workflows | 2026 |
| HARVEY-ORCH-2026 | Making Harvey the Orchestration Layer for Legal Work | Harvey | vendor | https://www.harvey.ai/blog/legal-work-orchestration | 2026-10-15 |
| LAWYERSWEEKLY-GILCHRIST-2026 | 17 lawyers promoted, AI officer added at Gilchrist Connell | Lawyers Weekly (Australia) | press | https://www.lawyersweekly.com.au/biglaw/44605-17-lawyers-promoted-ai-officer-added-to-gilchrist-connell | 2026-07-06 |

**Sources read but not cited in the YAML or notes**: IMANAGE-NEWS-2026 (a headline-level page; its "17% use AI daily" headline is not defined in the body and is not used), AL-IMANAGE-WEBINAR-2026 (iManage webinar of 8 Oct 2026, a past event with no outcome available), LawNext KM&I podcast page (2024-09-04), Opus 2/SKILLS survey release (2025-06-16), Littler chief AI officer item (2026-04-08), Harvey and Legora newsroom pages, TRI Legal Department Operations Report page, TRI Stand-out Lawyers page, TRI Future of Professionals page, NetDocuments press and technical pages blocked by Cloudflare until read through a mirror.

**Source count by type** (cited in the Sources table, 46 rows): press 22, vendor 9, conference 6, survey 4, podcast 2, regulator 1, academic 1, firm 1. No job-posting or community items were reachable.

---

## 6. Gaps

- **Quality evidence is largely absent.** No error rate, override rate, parallel-run or inspection result was found for a firm knowledge assistant, search tool, expertise finder or precedent library. The only controlled measurement is a vendor's own benchmark on public matters (NETDOCS-LCEB-2026). The Lilli, Infosys and Litera figures are unmeasured self-reports or vendor claims.
- **McKinsey primary sources** returned 403 even through the text mirror; Lilli figures rest on a 2024 press interview and a secondary relay of Business Insider. BCG, Bain, Deloitte, EY, KPMG, PwC knowledge platforms: no primary KM page reached; ChatNational (2024) is outside the window and assurance-specific.
- **APQC 2026 KM Priorities and Trends Survey** and the full iManage benchmark are gated; only summaries were read. KMWorld cited APQC findings without figures in the pages read.
- **ILTACON, CLOC and Legalweek session content**: only session titles and abstracts were reachable (EDRM preview, KM Education Hub listing, KMWorld programme). Recordings, slides, speaker remarks and CLOC's JavaScript programme were not read. The "Does Experience Matter?" ILTACON session had a title only. The KM&I for Legal conference (21-22 October 2026) is scheduled and its programme was not visible.
- **AICPA ENGAGE, MCA, PMI and Legal Geek KM sessions**: none found. Accounting evidence is one podcast, one vendor blog and one 2024 item.
- **Podcasts**: only the Accounting Today transcript was read in full. The Law Punx item is a written summary of a video; LawNext KM episodes found were 2024.
- **Community discussion** (Reddit, LinkedIn, Legal IT Insider, 3 Geeks and a Law Blog, Legal Evolution): blocked, captcha, or unreachable. No job postings that show KM roles were reachable.
- **Named deployments**: for search, graph and MCP products, no firm named as a live user in a source read, apart from vendor-stated names (Twin1) and design partners for Command Center (routed). The practice angle should look for customers.
- **Web search budget** was exhausted before the Kirkland & Ellis AI platform claim and the Pinsent Masons, AGG and Littler role stories could be checked; they are not used or are marked unverified.
- **Not found**: any KM-specific TRI article from the last 12 months beyond the premortem and State of the Legal Market analysis; firm survey data on KM headcount other than ILTA's expectation line and the AALL survey.

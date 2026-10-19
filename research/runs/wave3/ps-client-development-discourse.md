# Client development: discourse angle (professional-services)

Module `client-development` (key-account and client relationship management: relationship intelligence, account plans, AI value conversations with clients, client feedback and retention). Angle: discourse. Prepared 2026-10-19. Archetype: professional-services. Public sources only.

## 1. Summary

**What the field is saying.** Practitioners agree that the client has become the pressure point for AI, and that firms are less ready for that conversation than for the technology. The tools story is real but thin on measurement.

- **Clients now treat AI as a buying criterion, and say firms are not delivering.** In Thomson Reuters' 2026 survey, 78% of corporate clients call AI-enabled quality improvements very important or essential, and 6% say most or all providers deliver them. 32% have reconsidered, or plan within 12 months to reconsider, relationships with firms they see as falling behind (TR-FOP-2026). At Legalweek 2026, firm-side answers to "how much is AI saving us?" were "still gathering the data" (TRI-LEGALWEEK-2026).
- **Partners are not having the conversation.** Only about one-third of the most AI-embedded stand-out partners had discussed AI with at least 60% of their clients (TRI-STANDOUT-2026). About three-quarters of respondents in TR's professional-services survey say firms should start these talks (TR-AIPS-2026), and 41% of law-firm respondents received instructions both to use and not to use AI from different clients (TR-AIPS-2026).
- **The tooling push is about relationship data, and its evidence is vendor-commissioned.** In a 123-partner survey run for Introhive, 78% say their relationship visibility is hard to act on, 68% of those using AI for business development use only general-purpose chatbots, and 63% have no revenue-linked way to measure business development return (INTROHIVE-PARTNER-2026). Vendors (Introhive, Intapp, Harvey) describe relationship mapping, health scoring, cross-sell surfacing and agentic playbooks; no source reports error, override or adoption rates for any of them.
- **Firms are starting to build with clients, not just for them.** Parker Poe ran a client-and-attorney AI lab (2026-09-10), and Cooley, Debevoise and A&O Shearman are reported to be sharing or licensing AI tools to clients (PARKERPOE-LAWSITES-2026; ABAJ-SHARE-2026).
- **Trust is contested.** A chief legal officer writes that firms are banking AI productivity as margin (BLOOMBERGLAW-GCXAI-2026); an in-house lawyer at a Stockholm conference said firms had given clients nothing from AI (AL-INHOUSE-2026); Bloomberg Law notes that demand for Big Law time rose 4.2% in the first half of 2026 (BLOOMBERGLAW-MYSTERY-2026).

**Candidate use cases:** 17 (grade A: 0, B: 2, C: 12, D: 3). Three entries (13, 16, 17) are ideas that practitioners discuss; none is the analyst's own speculation. **No entry reaches grade A** because no named organization publishes a measured outcome for these uses.

**Sources:** 47 listed (46 opened, 1 search-only): 15 press, 9 conference, 8 survey, 7 podcast, 3 vendor, 2 community, 2 firm, 1 regulator. Eight web searches were used; the rest of the reading was by direct fetch.

**Coverage caveat.** The evidence is overwhelmingly about law firms. Accounting has survey and vendor material and one conference agenda. Consulting has only Source Global Research podcast and analyst pages and an MCA event listing; no consulting firm describes AI in its own key-account work in anything I could open.

**Evidence quality.** The only quantitative items are survey perceptions (what partners or clients say) and vendor claims. No error rates, override rates, parallel-run results, inspection findings or independent measurements of relationship-intelligence output or client-conversation outcomes were found.

## 2. Use cases

```yaml
- id: professional-services-client-development-01
  title: Relationship intelligence captured from email and calendars, queryable by firm AI assistants
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - client-interaction
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Partners say they want help finding new business in relationships the firm already has, but most say the relationship data is hard to act on. The Introhive CEO says CRM adoption at law firms has been negligible because a CRM needs professionals to spend time entering data.
  solution: A relationship intelligence platform captures and maps firm relationships from email and calendar data, instead of relying on manual CRM entry. Introhive says its MCP server, now generally available to customers, lets assistants such as Claude, Harvey, ChatGPT and Copilot query that data under each user's existing permissions and the firm's governance policies.
  outcomes:
  - lever: growth
    description: Partners report relationship visibility that they cannot act on
    figure: 78%
    measures: Partners (of 123 surveyed by Thinktiv for Introhive) who say their current tools give them some relationship visibility that is hard to act on
    provenance: vendor-published
    source_ref: INTROHIVE-PARTNER-2026
  - lever: growth
    description: Most partners using AI for business development rely on general-purpose tools with no view of firm relationships
    figure: 68%
    measures: Respondents actively using AI for business development who rely only on general-purpose tools such as ChatGPT, Copilot or Gemini (satisfaction 6.7 out of 10)
    provenance: vendor-published
    source_ref: INTROHIVE-PARTNER-2026
  - lever: growth
    description: Few firms can link business development spend to revenue
    figure: 63%
    measures: Firms with no revenue-linked way to measure business development ROI (15% can track revenue with strong attribution)
    provenance: vendor-published
    source_ref: INTROHIVE-PARTNER-2026
  prerequisites:
  - Continuous capture from partners' email and calendars, so that data stays current without manual entry
  - 'Accurate data: the Introhive CEO says that if outreach is automated, the data ''has to be accurate'''
  - 'Firm control over data governance: 83% of respondents said yes or maybe to sharing email content with AI tools when the firm controls governance'
  - Behaviour change and change management, which the Introhive CEO says matter more than the tools
  risks_and_guardrails:
  - Client billing data was the most sensitive category in the Introhive survey, especially in legal and accounting
  - California guidance says an agentic system with access to email, calendars and client files raises acute confidentiality concerns, and must not transmit client information externally without safeguards and human review
  - Vendor-commissioned survey; the figures describe partner perceptions, not measured outcomes
  human_checkpoints:
  - The partner decides whom to contact and what to say
  - Access follows each user's existing permissions
  role_evolution: The Introhive CEO says partners are now asked to take on business development tasks that once sat with marketing staff, and that AI purchasing in firms is often run by IT or innovation groups rather than marketing and BD teams.
  evidence_grade: C
  sources:
  - ref: INTROHIVE-PARTNER-2026
    title: AI Without Relationship Context Won't Deliver BD ROI, Introhive's 2026 Partner Survey Report Finds
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/news/ai-without-relationship-context-wont-deliver-bd-roi-introhives-2026-partner-survey-report-finds/
    date: '2026-10-13'
    access: full
    locator: Sections 'Firms Plan a Major Shift', 'The Gap Sits in the Data Underneath', 'Relationship Context Makes AI Useful'
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds
    publisher: LawSites (Robert Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: Sections 'A New Interface for An Old Problem', 'MCP and Agnostic Access to Data', 'A Complex Environment'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 executive summary; replaces the Nov 2023 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.6, paragraphs on agentic AI access to firm systems
  last_reviewed: '2026-10-19'
  notes: Named customer deployments for this product category appear in the practice-angle file for this module and were not re-opened here. No source reports an accuracy, override or adoption rate for relationship-intelligence recommendations. The survey was commissioned by a vendor that sells the product.
- id: professional-services-client-development-02
  title: Relationship-health scoring and at-risk alerts for key accounts
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - client-interaction
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: 'Information reaching managing partners about client relationships is historical and filtered through partner updates. In accounting, a vendor-cited survey suggests mid-tenure clients can be neglected: NPS was 37 for clients of 6 to 9 years and 84 for clients of 15 or more years.'
  solution: Software tracks communication velocity and meeting density from partners' inboxes and calendars and turns them into relationship-health scores across the client portfolio, with alerts when a relationship is cooling. Introhive says a red-scored account is not a cross-sell opportunity. A second vendor-cited line of practice is a systematic listening programme to catch quiet clients who drift towards self-service.
  outcomes:
  - lever: risk
    description: Partners rank alerts on at-risk relationships among the most valuable things AI could do with firm-wide information
    figure: 49%
    measures: Partners (of 123) who ranked 'alerts on at-risk relationships' among the top items when asked what they would most value from combining information across the firm (cross-sell 54%, relationship mapping 46%)
    provenance: vendor-published
    source_ref: INTROHIVE-LAWSITES-2026
  prerequisites:
  - Email and calendar activity data captured across the portfolio
  - A shared view of relationship health visible to all service-line partners on the account
  risks_and_guardrails:
  - Activity metadata is a proxy for relationship strength; no source tests how well the scores predict client departure
  - Same confidentiality limits as for relationship capture (see use case 01)
  human_checkpoints:
  - Leadership and account partners decide what action a cooling relationship needs
  role_evolution: Account leadership shifts from partner-reported updates to a continuously updated portfolio view, per Introhive. No source reports a change in job titles.
  evidence_grade: C
  sources:
  - ref: INTROHIVE-ACCTXSELL-2026
    title: 'Accounting Firm Cross-Selling AI: Time Every Conversation Right (heading: Accelerating Accounting Firm Growth Through AI and Relationship Health)'
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/?p=60208
    date: '2026-09-03'
    access: full
    locator: Section 'Measuring true relationship health to drive client retention'
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds
    publisher: LawSites (Robert Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: Section 'What Partners Say They Want'
  - ref: CUSTOMERTHINK-2026
    title: Your Clients Are Happy. They're Also Learning to Live Without You. (post citing a 2026 Accounting Buyer Insights Report; author Baker Nanduru)
    publisher: CustomerThink
    type: community
    url: https://customerthink.com/your-clients-are-happy-theyre-also-learning-to-live-without-you/
    date: '2026-06-24'
    access: full
    locator: Section 'The Trough Nobody Monitors'
  last_reviewed: '2026-10-19'
  notes: The NPS-by-tenure figures (37 and 84) come from a 2026 Accounting Buyer Insights Report based on 180 accounting-firm clients surveyed in March 2026, relayed in a CustomerThink post whose link points to ClearlyRated; they describe the problem, not an AI outcome. The report itself was not opened.
- id: professional-services-client-development-03
  title: Cross-sell and 'one firm' opportunity surfacing across service lines
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - research-synthesis
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Partners say identifying cross-sell opportunities is one of their biggest frictions in business development. Firms ask busy partners to audit past matters by hand to see whether a client could use another practice group, according to Harvey.
  solution: AI combines email, calendar, CRM records, matter history and relationship networks to show which clients may need another service, which relationships have gone quiet and which colleague has the warmest path in. Harvey says its tools analyse historical work product against a client's regulatory exposure. Intapp's Celeste ships origination and business development playbooks.
  outcomes:
  - lever: growth
    description: Partners rank cross-sell opportunities as the most valuable use of combined firm information
    figure: 54%
    measures: Partners (of 123) who ranked 'cross-sell opportunities' among the top items when asked what they would most value from combining information across the firm
    provenance: vendor-published
    source_ref: INTROHIVE-LAWSITES-2026
  - lever: growth
    description: Partners name cross-sell identification as a major friction
    figure: 43%
    measures: Partners (of 123) who named identifying cross-sell opportunities among their biggest sources of friction in business development
    provenance: vendor-published
    source_ref: INTROHIVE-PARTNER-2026
  prerequisites:
  - Shared relationship and matter data across practice groups
  - A common view of each account across service lines
  risks_and_guardrails:
  - 'Introhive argues that timing matters more than the pitch: a cross-sell introduced before the relationship has depth risks signalling that the firm sees the client as a revenue target'
  - Ethical walls and need-to-know restrictions must apply to the AI as they do to people (Intapp's stated position)
  human_checkpoints:
  - Partners on the account decide whether and when to raise a new service
  role_evolution: Service-line partners coordinate on timing and sequencing from one data view, per Introhive; no source reports changed roles.
  evidence_grade: C
  sources:
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds
    publisher: LawSites (Robert Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: Section 'What Partners Say They Want'
  - ref: INTROHIVE-PARTNER-2026
    title: AI Without Relationship Context Won't Deliver BD ROI, Introhive's 2026 Partner Survey Report Finds
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/news/ai-without-relationship-context-wont-deliver-bd-roi-introhives-2026-partner-survey-report-finds/
    date: '2026-10-13'
    access: full
    locator: Section 'Firms Plan a Major Shift in Business Development'
  - ref: INTROHIVE-ACCTXSELL-2026
    title: 'Accounting Firm Cross-Selling AI: Time Every Conversation Right (heading: Accelerating Accounting Firm Growth Through AI and Relationship Health)'
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/?p=60208
    date: '2026-09-03'
    access: full
    locator: 'Section ''The cross-sell imperative: aligning the one firm approach'''
  - ref: HARVEY-BD-2026
    title: How Law Firms Use AI for Business Development and Client Intelligence
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/ai-for-law-firm-business-development
    date: '2026-06-23'
    access: full
    locator: Table row 'Cross-Selling and Internal Discovery'
  last_reviewed: '2026-10-19'
  notes: Survey ranking figures measure what partners say they would value, not results achieved.
- id: professional-services-client-development-04
  title: AI-prepared client meeting and outreach briefs, with an opportunity matrix
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - research-synthesis
  - client-interaction
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: At the CMBDO Forum, panelists said senior lawyers often do not send regular client notes, because writing them takes time from billable work. Harvey says insight needed to find new mandates is spread across SharePoint, document management systems and email threads.
  solution: AI pulls together news, regulatory developments, earnings calls, relationship data and what clients are reading, then gives a partner a short list of clients to contact with tailored conversation openers, and an opportunity matrix that pairs client needs with firm capabilities. Harvey describes briefs built from firm archives and public filings such as EDGAR. For CPA firms, an Accounting Today opinion piece describes using AI to condense client emails, meeting notes and history into pre-meeting notes.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: n/a
    provenance: n/a
    source_ref: n/a
  prerequisites:
  - Access to firm archives, relationship data and external sources
  - Bespoke, one-to-one training for partners on using the briefs, which CMBDO panelists called essential
  risks_and_guardrails:
  - Panelists said briefs and matrices should guide lawyers, not script them
  - Panelists warned against assuming agents are smarter or more autonomous than they are; agents are limited by the data and tools they are given
  - Public AI tools should not receive sensitive client information without safeguards (Accounting Today opinion)
  human_checkpoints:
  - The lawyer interprets and personalises the brief before the conversation
  role_evolution: One CMBDO panelist said AI might get a lawyer most of the way, but the last part still depends on human judgement, experience and relationship skills. Business development and marketing teams take on partner training.
  evidence_grade: C
  sources:
  - ref: TRI-CMBDO-2026
    title: 'Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI may be talking to your clients about it'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai
    date: '2026-02-18'
    access: full
    locator: Sections 'AI as an assistant, not a replacement' and 'Strong need for lawyer training around AI'
  - ref: HARVEY-BD-2026
    title: How Law Firms Use AI for Business Development and Client Intelligence
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/ai-for-law-firm-business-development
    date: '2026-06-23'
    access: full
    locator: Section '7 Ways Harvey Can Support Legal Business Development', items 1 and 2
  - ref: AT-DECODE-2026
    title: Using AI to decode client behavior (opinion by the co-founder of Ace Cloud Hosting)
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/opinion/using-ai-to-decode-client-behavior
    date: '2026-09-02'
    access: full
    locator: Paragraphs on client meetings and onboarding new team members
  last_reviewed: '2026-10-19'
  notes: The CMBDO panelists are unnamed in the recap, and the Harvey piece is vendor marketing. No source reports time saved or meeting outcomes.
- id: professional-services-client-development-05
  title: Tailored client alerts and sector briefings drafted with AI
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - document-production
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Communications teams send generic newsletters to broad client lists. Harvey says this does not show a client what a regulatory or litigation change means for its own operations.
  solution: Practitioners use legal AI to turn regulatory or litigation developments into client alerts, sector-specific risk briefings, prospect-specific 'issues to watch' reports and board-ready summaries for general counsel, grounded in cited sources.
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: n/a
    provenance: n/a
    source_ref: n/a
  prerequisites:
  - Authoritative source access with citations
  - Partner review before anything goes to a client
  risks_and_guardrails:
  - Citations and facts in client-facing alerts need human verification
  - Marketing claims in the source are vendor-authored and untested
  human_checkpoints:
  - A lawyer reviews each alert before sending
  role_evolution: No source describes role change for this use case.
  evidence_grade: C
  sources:
  - ref: HARVEY-BD-2026
    title: How Law Firms Use AI for Business Development and Client Intelligence
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/ai-for-law-firm-business-development
    date: '2026-06-23'
    access: full
    locator: Section '7 Ways', item 4 (Generate Client-Ready Thought Leadership and Issue Spotting)
  - ref: TRI-CMBDO-2026
    title: 'Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI may be talking to your clients about it'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai
    date: '2026-02-18'
    access: full
    locator: Section 'AI as an assistant, not a replacement'
  last_reviewed: '2026-10-19'
  notes: Harvey also names a law firm that used the product to answer an urgent client request in under 48 hours; that is an RFP-response example and is routed to pursuit-proposals.
- id: professional-services-client-development-06
  title: Agentic origination and business development playbooks run by a 'Firm AI' product
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - coordination-scheduling
  - research-synthesis
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Intapp's argument is that most legal AI speeds up the practice of law for the individual practitioner but not the business behind it. LawSites' editor says large-firm workflows such as conflicts, intake and lateral hiring are often inefficient, partly because firm data is proprietary.
  solution: Celeste, announced as generally available on 2026-07-15, runs multi-step playbooks covering origination, business development, intake, conflicts, pricing, fundraising and lateral hiring, and includes a no-code builder. Intapp says it can surface relevant matters, partner experience and prior pitch materials in response to an urgent client request in minutes rather than hours.
  outcomes:
  - lever: speed
    description: Intapp states that relevant matters, partner experience and pitch material can be surfaced in minutes rather than hours
    figure: minutes rather than hours
    measures: Intapp's description of time to respond to an urgent client request; no sample, baseline or measurement is given
    provenance: vendor-published
    source_ref: LAWSITES-CELESTE-2026
  prerequisites:
  - Intapp systems of record for intake, conflicts and relationship data
  - Playbooks encoding the firm's own methods
  risks_and_guardrails:
  - Intapp says the same ethical walls, need-to-know restrictions and audit requirements apply to Celeste, and that firms can produce a full record of every AI action for clients and regulators (vendor statement)
  - California guidance requires safeguards and human review before an agent transmits client information externally
  human_checkpoints:
  - Not described in the source for business development playbooks
  role_evolution: LawSites reports no role changes. Intapp's chief product officer described a conflicts team clearing ten times the matters as a new business model, not saved time.
  evidence_grade: C
  sources:
  - ref: LAWSITES-CELESTE-2026
    title: Intapp Makes Celeste Generally Available, Calling It an 'AI Coworker' To Run the Business Side of Law Firms
    publisher: LawSites (Robert Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/07/intapp-makes-celeste-generally-available-calling-it-an-ai-coworker-to-run-the-business-side-of-law-firms.html
    date: '2026-07-16'
    access: full
    locator: Sections 'Executing Multi-Step Workflows' and 'Feedback from Early Adopters'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 executive summary; replaces the Nov 2023 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.6, last sentences of the agentic AI paragraph
  last_reviewed: '2026-10-19'
  notes: Early adopters named are BakerHostetler (quoted on intake and conflicts) and Hg (quoted on deal screening); neither quote concerns client development, so no early-adopter evidence supports the business development playbooks. Intake and conflicts are routed to acceptance-risk.
- id: professional-services-client-development-07
  title: Client priorities extracted from open matters to keep account teams aligned
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - research-synthesis
  - data-reporting
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Institutional knowledge about a client sits in closed matters, emails and legacy systems, and new teams must rebuild it. At a TRI forum, one firm executive described a lawyer who found the client's in-house team had already used AI to study its own market position, and feared losing the work.
  solution: Harvey says each newly opened matter can be treated as a source of structured data, with agents continuously extracting the client's shifting priorities, cross-border risks and structural preferences, so new teams get up to speed on a client's background and upcoming workstreams. The same executive said the firm built a use case to analyse markets and clients' positions in them proactively.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: n/a
    provenance: n/a
    source_ref: n/a
  prerequisites:
  - Matter documents accessible to the AI tool under ethical-wall rules
  - Data cleansing and location of proprietary data, which COO and CFO forum participants called the real challenge
  risks_and_guardrails:
  - 'Cross-matter exposure of confidential information: California guidance warns that poorly configured agentic systems can disclose information across matters'
  - Vendor description only; no accuracy data
  human_checkpoints:
  - Account partners review extracted priorities
  role_evolution: No source reports role change.
  evidence_grade: C
  sources:
  - ref: HARVEY-BD-2026
    title: How Law Firms Use AI for Business Development and Client Intelligence
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/ai-for-law-firm-business-development
    date: '2026-06-23'
    access: full
    locator: Section '7 Ways', item 5 (Strengthen Client Intelligence During Onboarding)
  - ref: TRI-COOCFO-AI-2025
    title: 'Law Firm COO & CFO Forum: As law firms push to offer solutions and demonstrate value, will AI get them there?'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/coo-cfo-forum-ai-solutions-demonstrating-value
    date: '2025-11-03'
    access: full
    locator: Paragraphs beginning 'Indeed, several panelists said they remembered' (before the section 'Questions begetting questions') and the opening paragraphs on data
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 executive summary; replaces the Nov 2023 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.6, paragraph on agentic AI access to firm systems
  last_reviewed: '2026-10-19'
  notes: The TRI forum executive and firm are unnamed in the recap, so the anecdote supports the problem, not a named deployment.
- id: professional-services-client-development-08
  title: Key-account and business development plan drafting from firm data
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - document-production
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Harvey says building a business development plan by hand takes dozens of non-billable hours from a firm's most expensive people. TRI's Stand-out Lawyers survey finds that, whatever their AI usage, lawyers say they need better client data and competitive intelligence, which it calls a preparation problem.
  solution: 'Harvey says GenAI can compress days of research and drafting into minutes across the five parts of a growth plan: firm-wide goals, target practice areas, client relationship optimisation, a targeted engagement plan and tracking of long-term relationships.'
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: n/a
    provenance: n/a
    source_ref: n/a
  prerequisites:
  - Access to the firm's matter history and client data
  - Account plan structure agreed by firm leadership
  risks_and_guardrails:
  - The time claim is vendor-authored and unmeasured
  - TRI's survey says embedded AI users report impact at about nine times the rate of minimal users, so partners who do not use AI may not adopt AI-drafted plans
  human_checkpoints:
  - Partners own and edit the plan
  role_evolution: No source reports role change.
  evidence_grade: C
  sources:
  - ref: HARVEY-BD-2026
    title: How Law Firms Use AI for Business Development and Client Intelligence
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/ai-for-law-firm-business-development
    date: '2026-06-23'
    access: full
    locator: Sections 'The Anatomy of a Modern Law Firm Business Development Plan' and 'Mapping Traditional Business Development to AI-Accelerated Growth'
  - ref: TRI-STANDOUT-2026
    title: 'Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice
    date: '2026-08-06'
    access: full
    locator: Section 'How to talk to clients about AI', paragraph on evidence and insight needs
  last_reviewed: '2026-10-19'
  notes: 'Weakest evidence in the set for this module: one vendor blog. Included because account planning is named in the module scope.'
- id: professional-services-client-development-09
  title: Proactive outreach nudges with drafted messages in the partner's workflow
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - client-interaction
  - document-production
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: The Introhive CEO says lawyers will not log in to a separate system to write to someone they have not contacted in 90 days.
  solution: 'AI becomes the ''new user interface'' for relationship management by prompting the lawyer inside the day-to-day workflow, with a drafted message. His example: ''You haven''t talked to Bob in 35 days. Would you like to send an email? Here''s a script.'' Harvey describes similar integrations in Outlook and Word that summarise email threads and refine draft replies.'
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: n/a
    provenance: n/a
    source_ref: n/a
  prerequisites:
  - Accurate contact and interaction data
  - Integration with email and calendar
  risks_and_guardrails:
  - The CEO says the old tolerance for a few bounced Christmas cards is gone; automated outreach has to be accurate
  - A podcast guest warned against making AI the centre of every client conversation and advised gauging each client's interest first
  human_checkpoints:
  - The lawyer chooses whether to send and edits the draft
  role_evolution: The CEO expects partners to act on prompts rather than maintain a CRM.
  evidence_grade: C
  sources:
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds
    publisher: LawSites (Robert Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: Section 'A New Interface for An Old Problem'
  - ref: HARVEY-BD-2026
    title: How Law Firms Use AI for Business Development and Client Intelligence
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/ai-for-law-firm-business-development
    date: '2026-06-23'
    access: full
    locator: Section '7 Ways', item 7
  - ref: LPT-FEDER-2026
    title: 'Rethinking Business Development: Small Actions, Stronger Relationships (Law Practice Today, S3 E32; show notes only)'
    publisher: ABA Law Practice Division
    type: podcast
    url: https://lawpracticetoday.buzzsprout.com/2268467/episodes/19123020-rethinking-business-development-small-actions-stronger-relationships
    date: '2026-05-11'
    access: full
    locator: Show notes and chapter 'AI in Client Conversations' (10:29)
  last_reviewed: '2026-10-19'
  notes: The nudge example is a vendor CEO's illustration in an interview; the podcast source was read as show notes only.
- id: professional-services-client-development-10
  title: Client feedback and listening analysed with AI to spot satisfaction and retention risk
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - research-synthesis
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Formal feedback programmes reach few clients and capture a snapshot. A 2024 article citing Thomson Reuters Market Insights says only 27% of clients said they were invited to take part in such programmes in the prior year. A 2026 UK client survey found 84% of clients satisfied but only two-thirds leaving a review.
  solution: Vendors and commentators describe analysing informal signals (meeting conversations, emails, post-matter surveys, bid documents, testimonials and reviews) to build 'always on' client listening. An Accounting Today opinion piece suggests feeding emails, surveys and reviews to a chatbot to cluster comments, rate satisfaction and propose action points.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a
    provenance: n/a
    source_ref: n/a
  prerequisites:
  - Access to client communications and feedback data
  - Data security and AI usage policies before client records go into AI tools (Accounting Today opinion)
  risks_and_guardrails:
  - The sources are a vendor CEO (MyCustomerLens) and an opinion piece by a hosting-company co-founder; neither reports measured accuracy
  - Personality inference from email language, which the opinion piece suggests, raises privacy questions the source does not address
  human_checkpoints:
  - Partners review insights and decide actions
  role_evolution: No source reports role change.
  evidence_grade: C
  sources:
  - ref: SJ-LISTENING-2024
    title: 'What clients really think about law firms is not always recorded in surveys (page title: Law Firm Operations & Practice Insights | What Clients Really Think)'
    publisher: Solicitors Journal
    type: press
    url: https://www.solicitorsjournal.com/sjarticle/what-clients-really-think-about-law-firms-is-not-always-recorded-in-surveys
    date: '2024-05-22'
    access: full
    locator: Paragraphs 1-3 and closing quotation (MyCustomerLens CEO Paul Roberts)
  - ref: AT-DECODE-2026
    title: Using AI to decode client behavior (opinion by the co-founder of Ace Cloud Hosting)
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/opinion/using-ai-to-decode-client-behavior
    date: '2026-09-02'
    access: full
    locator: Paragraphs on client feedback and retention risk
  - ref: LF-VALUEGAP-2026
    title: Half of clients think AI can replace solicitors
    publisher: Legal Futures
    type: press
    url: https://www.legalfutures.co.uk/latest-news/half-of-clients-think-ai-can-replace-solicitors/print/
    date: '2026-03-25'
    access: full
    locator: Opening paragraphs and 'silent satisfaction problem' section
  last_reviewed: '2026-10-19'
  notes: The SJ-LISTENING-2024 article is outside the 12-18 month window and is used only for the vendor's description of the approach. The 27% figure is a secondary citation of Thomson Reuters Market Insights, not verified at source, and is kept here in notes. The Legal Futures survey (1,000 UK consumer clients) was commissioned by lawtech firm Access Legal.
- id: professional-services-client-development-11
  title: Advisory-readiness signals in the accounting client base
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - client-interaction
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Accounting firms that want to grow advisory revenue often wait for clients to ask, or pitch before the relationship is ready. A 2026 buyer report cited by CustomerThink says 91% of accounting clients want proactive advisory from their firm while 4% describe their firm as primarily advisory.
  solution: AI scans communication channels and meetings for signs that a client may be considering advisory services (for example, a general question about forecasting), and relationship-health data decides which accounts are ready for a new conversation.
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: n/a
    provenance: n/a
    source_ref: n/a
  prerequisites:
  - Communication data captured across the account
  - Shared client view across audit, tax and advisory teams
  risks_and_guardrails:
  - Cross-selling into a weak relationship risks retention (Introhive)
  - Client data should not be put into public AI tools without safeguards (Accounting Today opinion)
  human_checkpoints:
  - The partner decides timing and approach
  role_evolution: Introhive says tax, audit and advisory partners coordinate on timing from the same relationship data.
  evidence_grade: C
  sources:
  - ref: AT-DECODE-2026
    title: Using AI to decode client behavior (opinion by the co-founder of Ace Cloud Hosting)
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/opinion/using-ai-to-decode-client-behavior
    date: '2026-09-02'
    access: full
    locator: Paragraphs on prospecting for advisory services
  - ref: INTROHIVE-ACCTXSELL-2026
    title: 'Accounting Firm Cross-Selling AI: Time Every Conversation Right (heading: Accelerating Accounting Firm Growth Through AI and Relationship Health)'
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/?p=60208
    date: '2026-09-03'
    access: full
    locator: Sections on relationship health and the cross-sell imperative
  - ref: CUSTOMERTHINK-2026
    title: Your Clients Are Happy. They're Also Learning to Live Without You. (post citing a 2026 Accounting Buyer Insights Report; author Baker Nanduru)
    publisher: CustomerThink
    type: community
    url: https://customerthink.com/your-clients-are-happy-theyre-also-learning-to-live-without-you/
    date: '2026-06-24'
    access: full
    locator: Section 'The Gap That Makes It Dangerous'
  last_reviewed: '2026-10-19'
  notes: The 91% and 4% figures describe client demand and firm positioning in a 180-client survey (March 2026) reported by a vendor-linked post; they do not measure an AI outcome. Introhive also states that more than 70% of accounting firms raised AI budgets and 44% report no measurable impact, with no source or base given, so it is not used as a figure.
- id: professional-services-client-development-12
  title: A structured AI value conversation between partners and clients
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - client-interaction
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: 'Clients want AI-enabled quality and savings but receive little information, and partners rarely raise the subject. Firms also get contradictory instructions: some clients require AI use and others prohibit it.'
  solution: 'Partners lead a planned conversation, sequenced as: what changed about the work, what changed for the client, what value that created, and how pricing should reflect it. TRI''s survey commentary warns that leading with price concessions can train clients to expect discounts. A DLA Piper panelist advised firms to set the meeting rather than wait for the client to set terms. The AI role is evidence and preparation (use cases 04 and 13).'
  outcomes:
  - lever: experience
    description: Few partners have AI conversations with most clients
    figure: about one-third
    measures: Partners embedded with AI (high-volume users across multiple work types) who said they had discussed AI with at least 60% of their clients
    provenance: independent
    source_ref: TRI-STANDOUT-2026
  - lever: risk
    description: Corporate clients rate AI-enabled quality as important but rarely receive it
    figure: 78% and 6%
    measures: 78% of corporate clients say AI-enabled quality improvements from their firms are very important or essential; 6% say most or all providers deliver them
    provenance: independent
    source_ref: TR-FOP-2026
  - lever: risk
    description: Corporate clients report reconsidering relationships
    figure: 32%
    measures: Corporate clients who have reconsidered, or plan within 12 months to reconsider, relationships with firms they feel are falling behind
    provenance: independent
    source_ref: TR-FOP-2026
  - lever: experience
    description: Mixed instructions reach firms
    figure: 41% of law firms
    measures: Law-firm respondents who say they have received direction from their client base both to use and not to use AI on different projects
    provenance: independent
    source_ref: TR-AIPS-2026
  - lever: experience
    description: Accountants rarely volunteer how they use AI
    figure: 33%
    measures: Respondents in Intuit's 725-person survey who proactively explain how AI supports their work (49% address it only when asked; 60% say clients asked for proof of AI data protection always or frequently)
    provenance: vendor-published
    source_ref: INTUIT-AT-2026
  - lever: risk
    description: Firms cannot show AI value to their key client
    figure: 32%
    measures: Firms that cannot confidently demonstrate AI value to their most important client (Litera survey; sample size not stated in the release)
    provenance: vendor-published
    source_ref: LITERA-LAWSITES-2026
  prerequisites:
  - Matter-level evidence of what AI changed (see use case 13)
  - 'Partner familiarity with AI: embedded partners are about nine times more likely than minimal users to report significant impact on efficiency and quality (TRI)'
  - Knowing each client's instructions on AI use
  risks_and_guardrails:
  - California guidance says a lawyer must consider disclosing intended AI use and its benefits and risks, and must follow client instructions limiting AI use
  - 'Clients are not unified: some demand AI-driven savings while others bar AI for certain work (DLA Piper panelist)'
  human_checkpoints:
  - The partner holds the conversation and agrees next steps with the client
  role_evolution: TRI calls partners the 'commercial transmission mechanism' of the firm. Its survey finds that technology leadership and change management rank near the bottom of qualities stand-out lawyers want in a leader.
  evidence_grade: C
  sources:
  - ref: TRI-STANDOUT-2026
    title: 'Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice
    date: '2026-08-06'
    access: full
    locator: Sections 'AI strategy is visible, but confidence is weak', 'Getting on the same page' and 'How to talk to clients about AI'
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: Section 'The contradictions in the room'
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: Key findings, 'Clients are already moving on'
  - ref: TR-AIPS-2026
    title: 2026 AI in Professional Services Report
    publisher: Thomson Reuters Institute
    type: survey
    url: https://tax.thomsonreuters.com/content/dam/ewp-m/documents/thomsonreuters/en/pdf/reports/2026-ai-in-professional-services-report.pdf
    date: 2026-01
    access: full
    locator: p.3 (executive findings), p.19 (infographic 8), p.20-21
  - ref: INTUIT-AT-2026
    title: 'Intuit''s 2026 Accountant Technology Survey: AI, fragmentation, and the future of the profession (sponsored content)'
    publisher: Accounting Today / Intuit
    type: survey
    url: https://www.accountingtoday.com/partnerinsights/article/intuit/intuits-2026-accountant-technology-survey-ai-fragmentation-and-the-future-of-the-profession
    date: '2026-07-01'
    access: full
    locator: Section 'How are accountants handling AI transparency and client trust in 2026?'
  - ref: LITERA-LAWSITES-2026
    title: 85% of Law Firms Say Clients Are Driving AI Investment Decisions, New Litera Survey Finds
    publisher: LawSites (Litera press release)
    type: survey
    url: https://www.lawnext.com/2026/05/85-of-law-firms-say-clients-are-driving-ai-investment-decisions-new-litera-survey-finds.html
    date: '2026-05-20'
    access: full
    locator: Key survey findings
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 executive summary; replaces the Nov 2023 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.7, Communication Regarding Generative AI Use (rules 1.2 and 1.4)
  last_reviewed: '2026-10-19'
  notes: 'All figures measure attitudes and reported behaviour, not outcomes of conversations. TRI is part of Thomson Reuters, which sells AI products. Search-only: a VSCPA 2026 survey summary seen in search results reported that 42% of firms said clients were not yet asking about their AI approach and 5% said clients frequently ask (VSCPA-AI-2026, not opened). It points the other way from the Intuit figure and shows that client demand for the conversation varies by market.'
- id: professional-services-client-development-13
  title: Matter-level evidence of AI's effect on time and value, reported to clients
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - client-interaction
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: 'Clients ask what AI did on their matters and how much it saved. At Legalweek 2026, firm-side answers were ''still gathering the data'', and a Ropes & Gray panelist described ROI measurement as resting more on conventional wisdom than hard evidence. Clients disagree on the remedy: some ask for line-item AI transparency on invoices while others set guidelines refusing to pay for work done by AI.'
  solution: 'Idea discussed by practitioners: record where AI was used on a matter, how much time or money it saved, and show that to the client as part of the relationship. Legalweek panelists and TR commentary frame this as a prerequisite for a credible value-sharing discussion.'
  outcomes:
  - lever: experience
    description: none published
    figure: none published
    measures: n/a
    provenance: n/a
    source_ref: n/a
  prerequisites:
  - Tracking of AI use at matter level
  - Agreement with the client on how savings are shared
  risks_and_guardrails:
  - California guidance says hourly bills must reflect time actually spent, that flat fees may build in AI savings, and that matter-specific AI costs need fee-agreement disclosure and no markup without informed written consent
  - Bloomberg Law's column reports that demand for Big Law lawyers' time rose 4.2% in the first half of 2026 (Citi's law firm banking group), so the column argues AI has not yet reduced the hours clients buy
  human_checkpoints:
  - Partner and client agree how value is shared
  role_evolution: Speakers on these client questions held titles such as Chief Pricing and Innovation Officer (Greenberg Traurig) and Senior Managing Director of AI Innovation (DLA Piper), per the Legalweek recap.
  evidence_grade: D
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: Sections 'Proving AI's path to saving clients money' and 'The contradictions in the room'
  - ref: TR-AIPS-2026
    title: 2026 AI in Professional Services Report
    publisher: Thomson Reuters Institute
    type: survey
    url: https://tax.thomsonreuters.com/content/dam/ewp-m/documents/thomsonreuters/en/pdf/reports/2026-ai-in-professional-services-report.pdf
    date: 2026-01
    access: full
    locator: p.3 and p.18-19 (only 18% collect AI ROI metrics; few collect client-facing metrics)
  - ref: BLOOMBERGLAW-MYSTERY-2026
    title: Big Law AI Cost Savings Remain a Mystery as Billable Hours Jump
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/big-law-ai-cost-savings-remain-a-mystery-as-billable-hours-jump
    date: '2026-09-03'
    access: full
    locator: Paragraphs on Citi demand data and the column's closing argument
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 executive summary; replaces the Nov 2023 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.8, Charging for Work Produced by Generative AI and Generative AI Costs (rule 1.5)
  last_reviewed: '2026-10-19'
  notes: Idea. The sources document the client ask and the lack of firm data, not a firm that reports matter-level AI savings to clients. The TR-AIPS figure is 18% of respondents whose organisations collect ROI metrics from AI, with most metrics internally focused.
- id: professional-services-client-development-14
  title: Client and attorney co-creation labs where AI assistants are built together
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - client-interaction
  - document-production
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Parker Poe says the interactions that shape the attorney-client relationship are often ones that never appear on a bill, and that clients want predictability, clearer communication and fewer surprises. A common friction is turning detailed legal updates into something business leaders can use.
  solution: 'On 2026-09-10 the firm ran an invitation-only workshop in Charlotte where general counsel, legal operations, compliance and business executives sat with its attorneys and built and tested AI assistants in teams of four to six, on the Lega AI Builder Lab platform. Teams chose from three tracks: company research, risk disclosure updates and executive legal briefings.'
  outcomes:
  - lever: experience
    description: Most participants chose the executive-briefing track, which tailors a legal update for different executives
    figure: approximately 90%
    measures: Participants who chose the executive legal briefing track (firm's own description)
    provenance: self-reported
    source_ref: PARKERPOE-LAWSITES-2026
  prerequisites:
  - Client willingness to attend and share business context
  - An AI builder platform and knowledge sources prepared in advance
  risks_and_guardrails:
  - A single event; no follow-up on whether participants use the assistants
  - The firm's release is promotional
  human_checkpoints:
  - Clients and attorneys jointly decide what 'better' looks like
  role_evolution: The firm's chief marketing and business development officer frames this as client experience work; lawyers and clients act as co-designers.
  evidence_grade: B
  sources:
  - ref: PARKERPOE-LAWSITES-2026
    title: Parker Poe Clients & Attorneys Build AI Assistants Together to Help Deliver Better Outcomes (firm press release dated 2026-09-11)
    publisher: Parker Poe Adams & Bernstein LLP, republished by LawSites
    type: firm
    url: https://www.lawnext.com/2026/09/parker-poe-clients-attorneys-build-ai-assistants-together-to-help-deliver-better-outcomes.html
    date: '2026-09-16'
    access: full
    locator: Paragraphs on the three tracks, the Lega AI Builder Lab, and the Moments That Matter programme
  last_reviewed: '2026-10-19'
  notes: The release says a similar client AI lab was run with Fasken in Canada and that its case study won an audience award at the 2026 SKILLS Law Showcase; that is second-hand here. One participant (the head of legal at Symphonic Distribution) said the skill is building repeatable AI processes a team can run without the firm.
- id: professional-services-client-development-15
  title: Firm-built AI tools offered to clients as a relationship and revenue channel
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - client-interaction
  - software-systems
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Firms that build their own AI tools can use them to deepen client ties and add a revenue stream, but the same tools may let clients do the work themselves.
  solution: Cooley is making its Cooley GO Lab, a startup workspace developed with Legora, available free to this summer's Y Combinator cohort. Debevoise's STAAR 2.0, also built with Legora's help, is a subscription platform that helps clients deploy AI. A&O Shearman has a revenue-sharing agreement with Harvey to license its tools to clients and other firms (all as reported via Law.com and the ABA Journal).
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: n/a
    provenance: n/a
    source_ref: n/a
  prerequisites:
  - A firm-built tool worth licensing
  - A vendor partnership that allows resale or sharing
  risks_and_guardrails:
  - An AI consultant quoted by Law.com said many firms fear clients using AI themselves or licensing their 'secret sauce' to peers, and asked why clients would still pay firms if they can do it themselves
  - Fee and disclosure rules apply to matter-specific AI costs (California guidance)
  human_checkpoints:
  - Not described
  role_evolution: Cooley's partner said the aim is for people to think of the firm as providing best-in-class information. No staffing change is reported.
  evidence_grade: B
  sources:
  - ref: ABAJ-SHARE-2026
    title: Should law firms share AI tools with their clients and peers?
    publisher: ABA Journal
    type: press
    url: https://www.abajournal.com/news/article/should-law-firms-share-ai-tools-with-their-clients-and-peers
    date: '2026-07-14'
    access: full
    locator: Whole article (short news item summarising Law.com)
  - ref: COOLEY-LAWCOM-2026
    title: Law Firms Are Building Their Own AI Tools. Should They Share Them? (press-mention page for a Law.com article)
    publisher: Cooley LLP
    type: firm
    url: https://www.cooley.com/news/coverage/2026/2026-07-14-law-firms-are-building-their-own-ai-tools-should-they-share-them
    date: '2026-07-14'
    access: full
    locator: 'Press-mention summary: Cooley GO Lab with Legora and Y Combinator'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 executive summary; replaces the Nov 2023 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.8, rule 1.5 paragraph on matter-specific AI costs
  last_reviewed: '2026-10-19'
  notes: The ABA Journal item says several firms 'have initiated plans' to share tools, so Debevoise and A&O Shearman may be announced rather than in use. The Law.com original is subscription-only and was not read. No usage or revenue figures are published.
- id: professional-services-client-development-16
  title: Shared AI workspaces and AI-readable firm knowledge as a way clients consume advice
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - client-interaction
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Practitioners expect clients to access legal services through their own AI tools, so firm knowledge that AI cannot reach would be bypassed.
  solution: 'Idea discussed by practitioners: firms make their knowledge accessible to clients through AI, and firms and clients work inside shared AI environments, so that collaboration itself becomes a product.'
  outcomes:
  - lever: experience
    description: none published
    figure: none published
    measures: n/a
    provenance: n/a
    source_ref: n/a
  prerequisites:
  - Knowledge management that AI can use
  - Client permissions and data controls
  risks_and_guardrails:
  - An in-house CLO asks whether legal departments will control, and be able to take with them, the 'legal memory' held in such systems or whether they will rent it
  - Confidentiality limits on sharing across clients (California guidance)
  human_checkpoints:
  - Not described
  role_evolution: The same CLO notes that the market has created a new profession, the legal engineer, who builds the systems legal work runs through and is often not a lawyer.
  evidence_grade: D
  sources:
  - ref: LAWPUNX-2025
    title: 'Law Punx: ''Law Firms Must Share Their Knowledge Via AI'''
    publisher: Artificial Lawyer
    type: podcast
    url: https://www.artificiallawyer.com/2025/11/11/law-punx-law-firms-must-share-their-knowledge-via-ai/
    date: '2025-11-11'
    access: full
    locator: Overview and takeaways (Oz Benamram of Skills)
  - ref: BLOOMBERGLAW-GCXAI-2026
    title: 'GC x AI Retrospective: The Billable Hour, Like a Twinkie, Endures (in-house CLO column)'
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/business-and-practice/gc-x-ai-retrospective-the-billable-hour-like-a-twinkie-endures
    date: '2026-10-19'
    access: full
    locator: Section 'What Came True', paragraph on shared AI environments and legal memory
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 executive summary; replaces the Nov 2023 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.6, paragraph on cross-matter disclosure
  last_reviewed: '2026-10-19'
  notes: Idea. The in-house tag applies to the Bloomberg Law source (a chief legal officer's column). The Law Punx contributor says firms have about two years, until the end of 2027, before not sharing has a major effect; that is a prediction, not a measurement. The practice-angle file lists a vendor client-portal product; it was not opened here.
- id: professional-services-client-development-17
  title: Advising clients on their own AI adoption as a way to deepen the relationship
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: Accounting clients bring AI to their accountants. A Ravical survey reported in The Accountant (October 2025) says 54% of accountancy firms have had to amend guidance provided by ChatGPT and 51% have met clients questioning whether AI could replace their services. ENGAGE session text says CPAs are increasingly asked to weigh in on AI adoption.
  solution: 'Idea discussed by practitioners: firms position themselves as advisers on which AI tools, risks and use cases suit the client, building the language and frameworks to have those conversations. Source''s podcast programme asks where consultants add most value for clients around AI.'
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: n/a
    provenance: n/a
    source_ref: n/a
  prerequisites:
  - Firm-level AI literacy and a stance on tools and risk
  - A repeatable framework for client AI conversations
  risks_and_guardrails:
  - Advice on AI tools is itself an area where the firm can be wrong
  - The article does not state the Ravical survey's sample size or who was asked
  human_checkpoints:
  - Partner-led advice
  role_evolution: The Ravical CEO says accountants can redefine their role as trusted advisers who help clients adopt AI responsibly.
  evidence_grade: D
  sources:
  - ref: KARBON-ENGAGE-2026
    title: AICPA & CIMA ENGAGE 2026 session preview (event held 8-11 June 2026)
    publisher: Karbon
    type: conference
    url: https://karbonhq.com/resources/aicpa-cima-engage-2026/
    date: '2026-05-21'
    access: full
    locator: 'Session ''AI conversations and integration: A practical guide for CPAs and their clients'' (2.40pm; presenters from Karbon, GW CPA and Weaver & Tidwell)'
  - ref: RAVICAL-ACCOUNTANT-2025
    title: 'Businesses in UK consult ChatGPT for advice: Ravical'
    publisher: The Accountant
    type: survey
    url: https://www.theaccountant-online.com/news/uk-businesses-consult-chatgpt-ravical/
    date: '2025-10-07'
    access: full
    locator: Paragraphs on firms' experience of client questions and the CEO quotation
  - ref: SOURCE-AI-2026
    title: Trends in how clients are using AI - agentic and more (Future of the Firm podcast)
    publisher: Source Global Research
    type: podcast
    url: https://sourceglobalresearch.com/trends-in-how-clients-are-using-ai-agentic-and-more
    date: '2026-06-02'
    access: full
    locator: Episode description (questions on where consultants add most value around AI)
  - ref: PARKERPOE-LAWSITES-2026
    title: Parker Poe Clients & Attorneys Build AI Assistants Together to Help Deliver Better Outcomes (firm press release dated 2026-09-11)
    publisher: Parker Poe Adams & Bernstein LLP, republished by LawSites
    type: firm
    url: https://www.lawnext.com/2026/09/parker-poe-clients-attorneys-build-ai-assistants-together-to-help-deliver-better-outcomes.html
    date: '2026-09-16'
    access: full
    locator: Attendee comment from a chemicals company IT leader
  last_reviewed: '2026-10-19'
  notes: Idea. The ENGAGE and Source items are descriptions of sessions and episodes, not reports of delivered services. CPA Practice Advisor's Intuit-sponsored survey says 62% of accountants report clients needing more guidance on technology management and 59% on business planning and strategy, a base of 725 US professionals, vendor-published.
```

## 3. Module notes

### Processes and key steps (work types)

1. **Capture and maintain relationship data** from email, calendars, CRM and matter history (data-reporting).
2. **Account and business development planning**, including portfolio reviews of key accounts (document-production, coordination-scheduling).
3. **Meeting and outreach preparation**: client briefs, news and regulatory synthesis, conversation openers (research-synthesis, client-interaction).
4. **Cross-sell and origination identification** across practice groups and service lines (data-reporting, expert-judgment).
5. **Client communications and thought leadership**: alerts, sector briefings, regular check-ins (document-production).
6. **AI value conversations and AI-use disclosure** with each client, including instructions the client gives on AI use (client-interaction, expert-judgment).
7. **Client feedback, listening and retention monitoring** (data-reporting).
8. **Joint client-firm collaboration**, such as co-creation labs and shared workspaces (client-interaction).

### Common pain points

- Relationship data is hard to act on, and CRM adoption by professionals is described as negligible because it relies on manual entry (INTROHIVE-LAWSITES-2026; INTROHIVE-PARTNER-2026).
- Partners lack time for business development: 45% name making time for BD, and 50% name knowing where to focus, among their biggest frictions (INTROHIVE-PARTNER-2026).
- Firms cannot show clients what AI saved on their matters, and clients ask anyway (TRI-LEGALWEEK-2026; LITERA-LAWSITES-2026).
- Clients give contradictory AI instructions to the same firm (TR-AIPS-2026, p.20; TRI-LEGALWEEK-2026).
- Partners who do not use AI themselves cannot explain its effect to clients: TRI reports that embedded users are about nine times more likely than minimal users to report significant impact (TRI-STANDOUT-2026).
- Senior lawyers skip regular client notes because they take billable time (TRI-CMBDO-2026).
- Accounting: long-tenured clients may be taken for granted. A vendor-linked survey of 180 accounting clients reports NPS of 37 at 6-9 years against 84 at 15 or more (CUSTOMERTHINK-2026).
- In-house: general counsel say they cannot see how outside firms use AI. Two-thirds of GCs say they do not know how their outside firms approach it (TRI-INTERDEPENDENT-2026) [in-house].

### Metrics and benchmarks (all survey or vendor measures; none is an outcome of an AI deployment)

| Figure | What it measures | Provenance | Ref and locator |
|---|---|---|---|
| 78% / 6% | Corporate clients saying AI-enabled quality improvements are very important or essential / saying most or all providers deliver | independent (TR survey of 1,816 professionals, Mar-Apr 2026; TR sells AI products) | TR-FOP-2026, 'Clients are already moving on' |
| 32% | Corporate clients who have reconsidered, or plan within 12 months to reconsider, relationships with firms falling behind (a third of those estimate over $1m a year at risk) | independent | TR-FOP-2026 |
| 18% | Respondents whose organisations collect ROI metrics from AI (most metrics internal, such as cost savings or usage) | independent | TR-AIPS-2026, p.3 |
| 54% / 29% / 67% | Corporate legal respondents who say firms should use AI on their matters / who say they know it is used / who do not know | independent | TR-AIPS-2026, p.19 (infographic 8) |
| 3.9 times; 22% | Firms with a GenAI strategy are 3.9 times more likely to achieve ROI (per a TR speaker); share of firms with such a strategy | independent (speaker statement, source data not given) | TRI-LEGALWEEK-2026 |
| 46% / 36% / 25% / just over 10% | Stand-out lawyers who strongly agree: practice has a clear plan to integrate AI / firm has a clear AI strategy / firm has a plan to monetise AI use / confident practice will succeed as AI is integrated | independent | TRI-STANDOUT-2026, 'AI strategy is visible, but confidence is weak' |
| 41% | Partners (of 123) running structured or AI-driven BD programmes today; 84% expect to within 18-24 months | vendor-published | INTROHIVE-PARTNER-2026 |
| 85%; 51%; 32% | Firms feeling or expecting client pressure on AI strategy; firms where a client directly influenced an AI investment in 12 months; firms unable to show AI value to their most important client (sample size not stated) | vendor-published | LITERA-LAWSITES-2026 |
| 33%; 60% | Accountants who proactively explain AI use; accountants saying clients asked for proof of AI data protection always or frequently (725 US professionals) | vendor-published | INTUIT-AT-2026 |
| 79% / 49%; 17% | Consulting clients rating quality highly / believing they get enough value beyond fees; firms that continue the value conversation after the work (base for the 17% not stated) | analyst-published (podcast summary of Source research) | SOURCE-VALUE-2025 |
| 4.2% | Growth in demand for Big Law lawyers' time in H1 2026 (Citi law firm banking group), against hopes for AI-driven reductions | independent (as reported by Bloomberg Law) | BLOOMBERGLAW-MYSTERY-2026 |

### Guardrails and regulatory points

- **Agentic access to firm systems.** California's 2026 guidance says a lawyer must not deploy an agent in a way that allows autonomous external transmission of client information without safeguards and human review, and warns that poorly configured agents may expose information across matters (CALBAR-GENAI-2026, p.6). Relationship-intelligence and business-development agents read exactly these systems.
- **Telling clients.** The same guidance says a lawyer must consider disclosing intended AI use, its benefits and risks, and must follow client instructions limiting AI use (CALBAR-GENAI-2026, p.7). It also says fees must reflect time actually spent and matter-specific AI costs need disclosure (p.8). These are California rules for lawyers; no equivalent accounting or consulting text was read.
- **Data sensitivity inside the firm.** Billing data was the most sensitive category in the Introhive survey, and 83% said yes or maybe to AI access to email content if the firm controls governance (INTROHIVE-PARTNER-2026).
- **Ethical walls.** Intapp says the same walls and audit trails that bind people apply to its agent (LAWSITES-CELESTE-2026); this is a vendor statement.
- **Timing and relationship fit.** Introhive argues a cross-sell offered too early can signal that the firm sees the client as a revenue target (INTROHIVE-ACCTXSELL-2026).
- **Accuracy.** The Introhive CEO says automated outreach cannot tolerate the bounce-backs that were acceptable for a Christmas-card list (INTROHIVE-LAWSITES-2026).

### Frontier signals (dated, sourced)

- **2026-10-13.** Introhive MCP server stated as generally available; the partner survey says the number expecting AI-driven BD grows from 8 to 40 respondents within 18-24 months (INTROHIVE-PARTNER-2026).
- **2026-10-19.** A chief legal officer writes that firms and clients now work inside shared AI environments, with collaboration becoming a product, and asks who controls the resulting "legal memory" (BLOOMBERGLAW-GCXAI-2026) [in-house].
- **2026-09-10.** Parker Poe runs a client-and-attorney AI lab (PARKERPOE-LAWSITES-2026).
- **2026-09-17.** The TRI Future of AI & Technology Forum agenda lists a fireside conversation with two clients on what they value in an AI-enabled market; the page is an agenda and no recap was read (TRI-FORUM-2026).
- **2026-09-03.** Bloomberg Law: a growing chorus of Big Law clients say the billable hour is unsustainable because of AI, while hours bought rise; Citi's survey of 57 firms reports three-quarters expect the billable hour to be affected by AI in 2028 (BLOOMBERGLAW-MYSTERY-2026).
- **2026-07-15.** Intapp announces general availability of Celeste, a "Firm AI" product with origination and BD playbooks (LAWSITES-CELESTE-2026).
- **2026-07-14.** Reports that Cooley, Debevoise and A&O Shearman share or license AI tools to clients (ABAJ-SHARE-2026; COOLEY-LAWCOM-2026).
- **2026-06-11.** TRI argues law firms and legal departments need joint conversations on pricing, work allocation, trust, talent and standards (TRI-INTERDEPENDENT-2026).
- **2026-05-11 to 2026-06-18.** IBA and ABA podcasts take up key-account strategy and AI's effect on BD and client relationships (IBA-MATSON-2026; IBA-LESTERHUIS-2026; LPT-FEDER-2026); episode descriptions only.
- **2026-05 (CLOC Global Institute).** A "Great Pricing Reset" panel framed pricing as a value question; the conference theme was collaboration between in-house teams, vendors and law firms (STENO-CLOC-2026) [in-house].
- **2026-03-13.** Legalweek: clients ask for matter-level AI savings and line-item transparency, and some refuse to pay for AI-done work (TRI-LEGALWEEK-2026).
- **2026-02-12.** Artificial Lawyer reports a GC at an in-house conference of 500+ GCs saying firms "get nothing" for clients from AI and expecting to raise it with the managing partner that year (AL-INHOUSE-2026) [in-house].
- **2025-10-24.** At TRI's COO & CFO Forum, speakers said clients now expect firms to use AI to understand their businesses and give tailored guidance, and cited research that about one-third of corporate clients (41% of those with $1bn+ revenue) plan to raise legal spend in the next year (TRI-COOCFO-MARKET-2025).
- **2025-11-11.** A Law Punx contributor predicts clients will mainly consume legal services through AI, and gives firms until end-2027 to make knowledge AI-accessible (LAWPUNX-2025).
- **Scheduled.** MCA event "AI for SME Consultancies" on 2026-11-26 (MCA-EVENTS-2026); signal only, not evidence.

### Workforce and role effects

- Partners are called the "commercial transmission mechanism" of the firm; TRI argues strategy fails unless partners see how it changes their client work (TRI-STANDOUT-2026).
- Partners are being asked to do BD that marketing staff once did, and private equity ownership adds top-down pressure on pipeline, according to the Introhive CEO (INTROHIVE-LAWSITES-2026).
- Bespoke, one-to-one partner training is described as the deciding factor in AI adoption for client conversations (TRI-CMBDO-2026).
- Named titles in the discourse include Chief Pricing and Innovation Officer, Senior Managing Director of AI Innovation, Global Chief AI Officer (TRI-LEGALWEEK-2026; STENO-CLOC-2026) and Head of Client Voice at an analyst firm (SOURCE-PERCEIVE-2026).
- A CLO columnist reports that "legal engineer" has emerged as a profession, often held by non-lawyers (BLOOMBERGLAW-GCXAI-2026) [in-house].
- Legalweek panels questioned the associate pyramid as client work moves in-house (TRI-LEGALWEEK-CRISIS-2026); this is routed to talent-learning.

### Objections and concerns practitioners raise

- **Authenticity.** Briefs should guide, not script; the last stretch needs judgement and relationships (TRI-CMBDO-2026). A podcast guest advises against making AI the centre of every client conversation (LPT-FEDER-2026).
- **Clients can do it themselves.** A consultant quoted by Law.com asks why clients would pay firms if they can do the work themselves (ABAJ-SHARE-2026). A TR report notes in-house teams are insourcing low-value repeatable work (TR-AIPS-2026, p.21).
- **Value capture.** Clients suspect firms bank savings as margin (BLOOMBERGLAW-GCXAI-2026; AL-INHOUSE-2026; TRI-STANDOUT-2026 quotes a GC asking whether rate rises offset AI efficiencies).
- **Billable hour not dead.** A Saul Ewing partner at Legalweek said his firm sees no meaningful client-driven move to alternative fees (TRI-LEGALWEEK-CRISIS-2026).
- **Data quality and pace.** The Introhive CEO says the perception that firms are far along is overstated, and that deploying AI without quality data is "throwing money away" (INTROHIVE-LAWSITES-2026).
- **Agent hype.** CMBDO panelists warned that agentic tools are limited by their data, and still called BD a good place to start because workflows are less rigid and feedback is faster (TRI-CMBDO-2026).
- **Client comfort varies.** UK clients accept AI for legal research but are uneasy about case management and administrative tasks (SJ-CLIENTS-2026, Law Firm Marketing Club survey of 642 UK clients). Demand for the AI conversation also varies: a search-only VSCPA summary reports 42% of firms say clients are not yet asking (VSCPA-AI-2026, not opened).
- **Vendor-commissioned evidence.** Most numbers on BD tooling come from the vendors that sell it.
- **Client-side buyers' options.** Artificial Lawyer lists in-house responses: keep more work internal, shop lower-value work, try AI-first firms, triage what goes out (AL-INHOUSE-2026) [in-house].

### Consulting and accounting notes

- **Consulting.** Source says tech-consulting spend is forecast to grow 7.5% in 2026, and that needs differ by sector, buyer seniority and functional budget holder, so offers should be segmented (SOURCE-PRECISION-2026). Its podcast programme covers how clients perceive firms, how clients use AI, and how to discuss value (SOURCE-PERCEIVE-2026; SOURCE-AI-2026; SOURCE-VALUE-2025). Only the 2025 value episode gives figures. No consulting firm's own AI-assisted account management was found.
- **Accounting.** Intuit's survey says 88% used AI for at least one client service and, for client deliverables, 6% want AI to execute autonomously (INTUIT-AT-2026; CPAPA-TECHSURVEY-2026). ENGAGE 2026 included a session on AI conversations with clients (KARBON-ENGAGE-2026). Ravical reports firms correcting client-obtained ChatGPT advice (RAVICAL-ACCOUNTANT-2025).

### Interview probes for an advisor

1. When a key client asks "how are you using AI on our work and what do we get from it", who answers, with what evidence, and how often does the question come up before you raise it?
2. Which signals do you trust to say a key account is healthy or cooling, where do they live (CRM, email, billing), and who may see them?
3. Do you hold every client's written instructions on AI use (permitted, prohibited, disclosure) in one place, and could two clients' instructions conflict on the same matter?
4. When AI saves time on a client matter, who decides whether the saving is passed on, reinvested in scope or kept, and does the client know?
5. What would make a partner act on an AI-suggested cross-sell or outreach, and what would make them ignore it?

## 4. Routed to other modules

- **pursuit-proposals.** Harvey's example of a law firm answering an urgent client request in under 48 hours, and AI-drafted RFP responses (HARVEY-BD-2026); clients adding AI usage clauses to RFPs and guidelines, with few firms giving hard data (LAWFUEL-2025).
- **scoping-pricing.** Value-based and alternative fee arrangements: Kopka Law's KPI-based pricing (TRI-KOPKA-2026); the CLOC "Great Pricing Reset" session (STENO-CLOC-2026); Citi's finding that three-quarters of surveyed firms expect AI to affect the billable hour by 2028 (BLOOMBERGLAW-MYSTERY-2026); the Saul Ewing view that clients are not driving AFAs (TRI-LEGALWEEK-CRISIS-2026).
- **billing-collections.** Line-item AI transparency on invoices and AI-cost disclosure under California rule 1.5 (TRI-LEGALWEEK-2026; CALBAR-GENAI-2026, p.8).
- **firm-finance.** Measurement of AI ROI: only 18% collect metrics (TR-AIPS-2026); Litera's finding that ROI ranked last among investment drivers (LITERA-LAWSITES-2026); the demand-growth-versus-savings puzzle (BLOOMBERGLAW-MYSTERY-2026).
- **acceptance-risk.** Intake and conflicts with Celeste at BakerHostetler (LAWSITES-CELESTE-2026).
- **talent-learning.** Bespoke partner training for client conversations (TRI-CMBDO-2026); the associate pyramid under pressure as work moves in-house (TRI-LEGALWEEK-CRISIS-2026); stand-out lawyers' low weighting of change leadership (TRI-STANDOUT-2026).
- **quality-review.** Client trust damaged by AI errors in consulting deliverables: community reaction to a report KPMG pulled over apparent hallucinations (HN-KPMG-2026, thread dated 2026-06-14); accuracy and verification as the top barrier for limited AI adopters (TRI-STANDOUT-2026).
- **knowledge-management.** Making firm knowledge AI-accessible for clients (LAWPUNX-2025); "legal memory" ownership (BLOOMBERGLAW-GCXAI-2026).
- **In-house legal operations (flag, not a module).** GC-to-C-suite visibility gap: 86% of GCs against 17% of C-suite say legal contributes significantly; recommended outcome-based messaging and AI fluency (TRI-VISIBILITY-2026) [in-house]. The same flag applies to AL-INHOUSE-2026, STENO-CLOC-2026, TRI-INTERDEPENDENT-2026 and BLOOMBERGLAW-GCXAI-2026.

## 5. Sources

47 sources. Types: press 15, conference 9, survey 8, podcast 7, vendor 3, community 2, firm 2, regulator 1. 46 opened and read (podcast pages read as show notes only, not heard); 1 search-only. Dates are publication dates from the page byline, metadata or JSON-LD. Exceptions: TR-FOP-2026 shows no date (2026 only); TR-AIPS-2026 is dated 2026-01 from the PDF creation metadata (2026-01-27); CALBAR-GENAI-2026 is dated 2026-05 from PDF metadata (2026-05-15); TRI-FORUM-2026 is the event date and KARBON-ENGAGE-2026 the page date. MCA-EVENTS-2026 is a listing (year only). Refs shared with other files in this run use the same key (for example TRI-LEGALWEEK-2026, TRI-STANDOUT-2026, TR-FOP-2026, INTROHIVE-LAWSITES-2026, LAWSITES-CELESTE-2026, CALBAR-GENAI-2026).

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ABAJ-SHARE-2026 | Should law firms share AI tools with their clients and peers? | ABA Journal | press | https://www.abajournal.com/news/article/should-law-firms-share-ai-tools-with-their-clients-and-peers | 2026-07-14 | full |
| AL-INHOUSE-2026 | 'We Get Nothing From Law Firm AI Use' - Client | Artificial Lawyer | press | https://www.artificiallawyer.com/2026/02/12/we-get-nothing-from-law-firm-ai-use-client/ | 2026-02-12 | full |
| AT-DECODE-2026 | Using AI to decode client behavior (opinion by the co-founder of Ace Cloud Hosting) | Accounting Today | press | https://www.accountingtoday.com/opinion/using-ai-to-decode-client-behavior | 2026-09-02 | full |
| BLOOMBERGLAW-GCXAI-2026 | GC x AI Retrospective: The Billable Hour, Like a Twinkie, Endures (in-house CLO column) | Bloomberg Law | press | https://news.bloomberglaw.com/business-and-practice/gc-x-ai-retrospective-the-billable-hour-like-a-twinkie-endures | 2026-10-19 | full |
| BLOOMBERGLAW-MYSTERY-2026 | Big Law AI Cost Savings Remain a Mystery as Billable Hours Jump | Bloomberg Law | press | https://news.bgov.com/business-and-practice/big-law-ai-cost-savings-remain-a-mystery-as-billable-hours-jump | 2026-09-03 | full |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 executive summary; replaces the Nov 2023 version) | State Bar of California, COPRAC | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05 | full |
| COOLEY-LAWCOM-2026 | Law Firms Are Building Their Own AI Tools. Should They Share Them? (press-mention page for a Law.com article) | Cooley LLP | firm | https://www.cooley.com/news/coverage/2026/2026-07-14-law-firms-are-building-their-own-ai-tools-should-they-share-them | 2026-07-14 | full |
| CPAPA-TECHSURVEY-2026 | The 2026 Accountant Technology Survey: Turning Data Revelations into a Firm of the Future (sponsored by Intuit) | CPA Practice Advisor | survey | https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807 | 2026-07-02 | full |
| CUSTOMERTHINK-2026 | Your Clients Are Happy. They're Also Learning to Live Without You. (post citing a 2026 Accounting Buyer Insights Report; author Baker Nanduru) | CustomerThink | community | https://customerthink.com/your-clients-are-happy-theyre-also-learning-to-live-without-you/ | 2026-06-24 | full |
| HARVEY-BD-2026 | How Law Firms Use AI for Business Development and Client Intelligence | Harvey | vendor | https://www.harvey.ai/blog/ai-for-law-firm-business-development | 2026-06-23 | full |
| HN-KPMG-2026 | KPMG pulls report on AI usage due to apparent hallucinations (Hacker News discussion) | Hacker News | community | https://news.ycombinator.com/item?id=48527297 | 2026-06-14 | full |
| IBA-LESTERHUIS-2026 | Business Development and Marketing Subcommittee Podcast: Martijn Lesterhuis (Saga Legal) - episode page description only | International Bar Association, Law Firm Management Committee | podcast | https://www.ibanet.org/LFMC/MBD-Podcast/Martijn-Lesterhuis | 2026-06-18 | full |
| IBA-MATSON-2026 | Business Development and Marketing Subcommittee Podcast: John Matson (Arthur Cox) - episode page description only | International Bar Association, Law Firm Management Committee | podcast | https://www.ibanet.org/LFMC/MBD-Podcast/John-Matson | 2026-05-08 | full |
| INTROHIVE-ACCTXSELL-2026 | Accounting Firm Cross-Selling AI: Time Every Conversation Right (heading: Accelerating Accounting Firm Growth Through AI and Relationship Health) | Introhive | vendor | https://www.introhive.com/?p=60208 | 2026-09-03 | full |
| INTROHIVE-LAWSITES-2026 | Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html | 2026-10-13 | full |
| INTROHIVE-PARTNER-2026 | AI Without Relationship Context Won't Deliver BD ROI, Introhive's 2026 Partner Survey Report Finds | Introhive | vendor | https://www.introhive.com/news/ai-without-relationship-context-wont-deliver-bd-roi-introhives-2026-partner-survey-report-finds/ | 2026-10-13 | full |
| INTUIT-AT-2026 | Intuit's 2026 Accountant Technology Survey: AI, fragmentation, and the future of the profession (sponsored content) | Accounting Today / Intuit | survey | https://www.accountingtoday.com/partnerinsights/article/intuit/intuits-2026-accountant-technology-survey-ai-fragmentation-and-the-future-of-the-profession | 2026-07-01 | full |
| KARBON-ENGAGE-2026 | AICPA & CIMA ENGAGE 2026 session preview (event held 8-11 June 2026) | Karbon | conference | https://karbonhq.com/resources/aicpa-cima-engage-2026/ | 2026-05-21 | full |
| LAWFUEL-2025 | AI disruption forces Big Law to rethink billing: "Firms will give more for free" | LawFuel | press | https://www.lawfuel.com/free-legal-fees-from-big-law/ | 2025-07-29 | full |
| LAWPUNX-2025 | Law Punx: 'Law Firms Must Share Their Knowledge Via AI' | Artificial Lawyer | podcast | https://www.artificiallawyer.com/2025/11/11/law-punx-law-firms-must-share-their-knowledge-via-ai/ | 2025-11-11 | full |
| LAWSITES-CELESTE-2026 | Intapp Makes Celeste Generally Available, Calling It an 'AI Coworker' To Run the Business Side of Law Firms | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2026/07/intapp-makes-celeste-generally-available-calling-it-an-ai-coworker-to-run-the-business-side-of-law-firms.html | 2026-07-16 | full |
| LF-VALUEGAP-2026 | Half of clients think AI can replace solicitors | Legal Futures | press | https://www.legalfutures.co.uk/latest-news/half-of-clients-think-ai-can-replace-solicitors/print/ | 2026-03-25 | full |
| LITERA-LAWSITES-2026 | 85% of Law Firms Say Clients Are Driving AI Investment Decisions, New Litera Survey Finds | LawSites (Litera press release) | survey | https://www.lawnext.com/2026/05/85-of-law-firms-say-clients-are-driving-ai-investment-decisions-new-litera-survey-finds.html | 2026-05-20 | full |
| LPT-FEDER-2026 | Rethinking Business Development: Small Actions, Stronger Relationships (Law Practice Today, S3 E32; show notes only) | ABA Law Practice Division | podcast | https://lawpracticetoday.buzzsprout.com/2268467/episodes/19123020-rethinking-business-development-small-actions-stronger-relationships | 2026-05-11 | full |
| MCA-EVENTS-2026 | MCA events listing, incl. 'AI for SME Consultancies: Best Practice, Practical Insights and Lessons Learned' (scheduled 26 Nov 2026) | Management Consultancies Association | conference | https://www.mca.org.uk/mca-events | 2026 | full |
| PARKERPOE-LAWSITES-2026 | Parker Poe Clients & Attorneys Build AI Assistants Together to Help Deliver Better Outcomes (firm press release dated 2026-09-11) | Parker Poe Adams & Bernstein LLP, republished by LawSites | firm | https://www.lawnext.com/2026/09/parker-poe-clients-attorneys-build-ai-assistants-together-to-help-deliver-better-outcomes.html | 2026-09-16 | full |
| RAVICAL-ACCOUNTANT-2025 | Businesses in UK consult ChatGPT for advice: Ravical | The Accountant | survey | https://www.theaccountant-online.com/news/uk-businesses-consult-chatgpt-ravical/ | 2025-10-07 | full |
| SJ-CLIENTS-2026 | Clients embracing AI use in law firms | Solicitors Journal | press | https://www.solicitorsjournal.com/sjarticle/clients-embracing-ai-use-in-law-firms | 2026-04-10 | full |
| SJ-LISTENING-2024 | What clients really think about law firms is not always recorded in surveys (page title: Law Firm Operations & Practice Insights / What Clients Really Think) | Solicitors Journal | press | https://www.solicitorsjournal.com/sjarticle/what-clients-really-think-about-law-firms-is-not-always-recorded-in-surveys | 2024-05-22 | full |
| SOURCE-AI-2026 | Trends in how clients are using AI - agentic and more (Future of the Firm podcast) | Source Global Research | podcast | https://sourceglobalresearch.com/trends-in-how-clients-are-using-ai-agentic-and-more | 2026-06-02 | full |
| SOURCE-PERCEIVE-2026 | What do firms need to know about how clients perceive them in 2026? (Future of the Firm podcast) | Source Global Research | podcast | https://sourceglobalresearch.com/podcast/what-do-firms-need-to-know-about-how-clients-perceive-them-in-2026 | 2026-08-25 | full |
| SOURCE-PRECISION-2026 | Precision segmentation: How consulting firms can target clients' sector and functional AI budgets | Source Global Research | press | https://sourceglobalresearch.com/market-update/precision-segmentation-how-consulting-firms-can-target-clients-sector-and-functional-ai-budgets | 2026-09-28 | full |
| SOURCE-VALUE-2025 | How to talk to your clients about value (Future of the Firm podcast) | Source Global Research | podcast | https://sourceglobalresearch.com/podcast/how-to-talk-to-your-clients-about-value | 2025-09-09 | full |
| STENO-CLOC-2026 | CLOC Global Institute 2026: Stronger By Design, Built By Community (vendor recap of the 11-14 May 2026 event) | Steno | conference | https://brief.steno.com/cloc-global-institute-2026-recap | 2026-06-03 | full |
| TR-AIPS-2026 | 2026 AI in Professional Services Report | Thomson Reuters Institute | survey | https://tax.thomsonreuters.com/content/dam/ewp-m/documents/thomsonreuters/en/pdf/reports/2026-ai-in-professional-services-report.pdf | 2026-01 | full |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 | full |
| TRI-CMBDO-2026 | Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI may be talking to your clients about it | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai | 2026-02-18 | full |
| TRI-COOCFO-AI-2025 | Law Firm COO & CFO Forum: As law firms push to offer solutions and demonstrate value, will AI get them there? | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/coo-cfo-forum-ai-solutions-demonstrating-value | 2025-11-03 | full |
| TRI-COOCFO-MARKET-2025 | Law Firm COO & CFO Forum: As legal market shifts, the big questions still need answers | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/coo-cfo-forum-shifting-legal-market | 2025-10-24 | full |
| TRI-FORUM-2026 | The 2026 Future of AI & Technology Forum (agenda page) | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/events/the-2026-future-of-ai-technology-forum | 2026-09-17 | full |
| TRI-INTERDEPENDENT-2026 | Interdependent by design: The AI conversation law firms and legal departments need to be having now | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/needed-ai-conversation | 2026-06-11 | full |
| TRI-KOPKA-2026 | How one law firm is challenging a broken status quo around billing | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing | 2026-04-30 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-LEGALWEEK-CRISIS-2026 | Move over, "Death of the billable hour," Legalweek 2026 has found a new existential crisis | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-new-existential-crisis | 2026-03-19 | full |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 | full |
| TRI-VISIBILITY-2026 | Relationship-building and AI fluency key to closing visibility gap, new report shows | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/closing-ai-visibility-gap | 2026-04-06 | full |
| VSCPA-AI-2026 | 2026 VSCPA AI Survey Executive Summary (seen only in search results; the download returned HTTP 403) | Virginia Society of CPAs | survey | https://www.vscpa.com/storage/assets/PDFs%20and%20Docs/2026%20VSCPA%20AI%20Survey%20Executive%20Summary.docx | 2026 | search-only |

## 6. Gaps

**Evidence of effect**
- No named organization publishes a measured outcome (adoption, accuracy, override rate, win rate, retention change, time saved) for relationship intelligence, health scoring, cross-sell surfacing, AI-prepared briefs or client-facing AI tools. No parallel runs, inspection findings or independent evaluations were found. Survey figures describe perceptions.
- Named-customer case studies for Introhive, Intapp and similar tools are in the practice-angle file for this module and were not re-opened here.

**Scope coverage**
- Consulting: no consulting firm's own account management, account planning or client-feedback use of AI was found. One search returned only vendor templates and a vendor-authored small-firm example. Source Global Research pages were readable only at summary level (reports and transcripts are paywalled or not opened). Big Four and strategy-firm pages were not searched in this run.
- Accounting: the AICPA site, the ENGAGE session recordings and the VSCPA executive summary (HTTP 403) were not reachable; ENGAGE is represented by a vendor agenda page.
- In-house client management is represented by TRI articles, one conference column and a CLOC recap; the CLOC session programme itself was not opened.
- No community discussion (Reddit, LinkedIn, practitioner forums) specific to client development was found; the two community items are a vendor-linked blog post and a Hacker News thread on a tangential topic.
- ILTACON 2026 recaps read (ABA Journal column; eDiscovery Today) contained nothing on client development. Legal Geek, PMI Global Summit and MBB/Big Four conference content were not found.

**Access limits**
- Podcast audio was not heard; IBA, Law Practice Today and Source entries rely on episode descriptions, so no claim is made about what guests said beyond them. The TRI Clarity podcast on the Stand-out Lawyers report was not located.
- Not opened or blocked: Introhive's full partner report; the ClearlyRated 2026 Accounting Buyer Insights Report; Litera's State of Legal AI report (sample size not stated in the release); the Law.com articles behind the Cooley, Debevoise and A&O Shearman items; Debevoise's own page (Cloudflare), Akin Gump's page (403), Priori's blog (Cloudflare), Wolters Kluwer ELM's legal operations page (challenge page).
- TR-FOP-2026 shows no publication date; TR-AIPS-2026 and CALBAR-GENAI-2026 are dated from file metadata.
- The TRI forum session "Through the client lens" (2026-09-17) and the MCA event (2026-11-26) are agenda or listing items; nothing from the sessions was read.

**Caution on attribution**
- The Karbon agenda lists the ENGAGE "AI conversations and integration" session presenters as Twyla Verhelst (Karbon), Samantha Bowling (GW CPA) and Neha Patel (Weaver & Tidwell). The landscape file attributed it to Stephanie Otero of the AICPA, who appears on a different session on the page; the landscape entry should be corrected.
- The Introhive LawSites article describes Stage 3 or 4 maturity; the vendor press release describes the same 84% as expecting "structured or AI-driven" programmes. The two are reported separately above.
- TR sells AI products and Introhive, Intapp, Harvey and Litera sell the tools they survey; every survey in this file was designed or published by an interested party.

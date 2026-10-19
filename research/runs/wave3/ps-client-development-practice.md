# Client development: practice angle (professional services)

Module `client-development` (key-account and client relationship management). Angle: practice. Prepared 2026-10-19. Archetype: professional-services. Public sources only.

## 1. Summary

**Counts.** 16 candidate use cases: grade A 0, grade B 8, grade C 7, grade D 1 (labelled idea). 42 sources opened and read in full, plus 5 search-only items. Types read: vendor 23, press 7, survey 5, firm 3, conference 3, job-posting 1.

**What the practice evidence shows**

- **The commercial layer is relationship data, and it is mostly vendor-evidenced.** The densest named deployments are Introhive at accounting and law firms (Grassi, Schneider Downs, KSM, LBMC, Thomson Snell & Passmore) and Intapp DealCloud (Howes Percival; Celeste selections at Practus/Auxana, Wotton Kearney, Forvis Mazars Capital Advisors, Ropes & Gray). Every figure about a tool's results is a vendor-published activity count or ROI claim. No grade A entry is possible: no named organisation reports a measured outcome of its own, and no source gives error, override or correction rates.
- **Firms still run on data they cannot use.** In an Introhive-commissioned survey of 123 partners, 57% of firms sit at basic data or visibility maturity while 84% expect structured or AI-driven BD within 18-24 months; 63% have no revenue-linked way to measure BD return (INTROHIVE-LAWSITES-2026).
- **Client conversations about AI are the pressure point and the weakest practice.** Corporate clients want AI-enabled quality (78% say very important or essential) but 6% say most providers deliver it (TR-FOP-2026). Partners are not having the conversation: more than one-third of stand-out lawyers had discussed AI with fewer than 20% of their clients (TRI-STANDOUT-2026). The tooling to evidence AI value per matter is an October 2026 announcement (LEGORA-LAUREL-2026).
- **Two firm-led moves are visible in practice.** Some firms build their own BD intelligence (Akin Gump's Moneyball; Quinn Emanuel's deep-research scouts) and some turn AI into a client-facing asset (Parker Poe's client AI lab; Debevoise's STAAR; Cooley GO Lab; Legora Portal at Linklaters).
- **Evidence is skewed to law and to vendors.** Accounting evidence comes from Introhive and Intapp stories; consulting evidence is thin (Source Global Research buyer segmentation; no consulting-firm account-management tooling found).

**Two most important insights**

1. The measurable benefit published so far is data capture and visibility, not revenue: counts of relationships, contacts and meetings ingested. Whether that moves cross-sell, retention or wins is untested in public sources.
2. The client-facing AI value conversation is the larger gap and is mostly unautomated: clients ask for proof of savings, partners are not talking to clients, and the matter-level measurement is only now being built.

---

## 2. Use cases

Single YAML block. Ids follow `professional-services-client-development-NN`. Grade D is labelled idea. Provenance and locators are recorded per outcome and source.

```yaml
- id: professional-services-client-development-01
  title: Zero-entry capture and enrichment of contacts, meetings and emails in the firm CRM
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - client-interaction
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Relationship data sits in individual inboxes, calendars and spreadsheets because fee-earners
    rarely log contacts and meetings by hand. The CRM is then incomplete and cannot support account or
    BD decisions.
  solution: Software reads email and calendar data and creates or updates contact, company and activity
    records in the firm's CRM (Salesforce, Dynamics, HubSpot or DealCloud) without manual entry, and enriches
    the records. Named firms in vendor case studies include Schneider Downs and LBMC (Dynamics), KSM (Salesforce,
    deployed ahead of the CRM rollout) and Grassi (HubSpot). Howes Percival uses DealCloud with an Outlook
    integration.
  outcomes:
  - lever: capacity
    description: Volume of activity captured automatically into the CRM at Schneider Downs
    figure: 3,120,627 meetings and emails ingested; 71,948 new contacts identified, 26,891 of them executive-level
    measures: Meetings and emails automatically ingested into Dynamics CRM; new contacts identified (source's
      own labels). These are activity counts, not business results
    provenance: vendor-published
    source_ref: INTROHIVE-SCHNEIDERDOWNS-2026
  - lever: cost
    description: Time-saving return claimed for LBMC
    figure: $197,115
    measures: '''Total ROI from time savings'' as labelled on the case study; the calculation basis is
      not shown'
    provenance: vendor-published
    source_ref: INTROHIVE-LBMC-2024
  - lever: quality
    description: Data accuracy quoted by an unnamed international law firm in a Forrester-commissioned
      study
    figure: 97% data accuracy rate for CRM systems
    measures: A customer's own statement of its CRM data accuracy rate, quoted anonymously on the vendor's
      landing page; not independently checked
    provenance: vendor-published
    source_ref: INTROHIVE-FORRESTER-2024
  prerequisites:
  - Access to firm email and calendar data
  - A CRM system of record, or a data foundation laid ahead of one (KSM did this before its Salesforce
    rollout)
  - A passive implementation that does not add steps for professionals (stated aim at Thomson Snell &
    Passmore and Schneider Downs)
  risks_and_guardrails:
  - 'Automated records must be accurate: the vendor CEO says the old tolerance for bounced mailing-list
    entries no longer holds when outreach is automated (INTROHIVE-LAWSITES-2026)'
  - All outcome figures found are vendor-published activity counts or ROI claims; no independent measurement
    of accuracy, override or correction rates was found
  - Privacy and lawful-basis rules for harvesting contact data are not addressed in the sources read
  human_checkpoints:
  - 'Professionals can review newly found contacts before they are added to the CRM (KSM case study: contacts
    not yet in the CRM are surfaced for review and addition)'
  role_evolution: Fee-earners are no longer expected to log contacts and meetings by hand. The Introhive
    CEO describes AI as becoming 'the new user interface' that prompts lawyers instead of asking them
    to log in (INTROHIVE-LAWSITES-2026).
  evidence_grade: B
  sources:
  - ref: INTROHIVE-SCHNEIDERDOWNS-2026
    title: Schneider Downs Builds a Stronger Relationship Database with Introhive (client story)
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/client-story/schneider-downs-building-a-stronger-relationship-database-with-introhive/
    date: '2026-03-31'
    access: full
    locator: Situation; solution; 'Measurable business impact' panel
  - ref: INTROHIVE-KSM-2026
    title: KSM Lays the Groundwork for CRM Adoption with Introhive (client story)
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/client-story/ksm-lays-the-groundwork-for-crm-adoption-with-introhive/
    date: '2026-06-11'
    access: full
    locator: Situation and solution sections
  - ref: INTROHIVE-LBMC-2024
    title: LBMC Achieves 567% ROI in Their First Step Into Digital Transformation with Introhive (client
      story; page modified 2026-06-22)
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/client-story/lbmc/
    date: '2024-07-24'
    access: full
    locator: Title; 'Measurable business impact' panel
  - ref: INTROHIVE-GRASSI-2026
    title: Grassi Strengthens Client Engagement with Introhive (client story)
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/client-story/grassi-strengthening-client-engagement-with-introhive/
    date: '2026-03-02'
    access: full
    locator: Situation and solution sections
  - ref: INTROHIVE-FORRESTER-2024
    title: The Forrester Total Economic Impact Study for Introhive's Customer Intelligence Platform (landing
      page; modified 2026-03-11)
    publisher: Introhive (study commissioned from Forrester Consulting)
    type: vendor
    url: https://www.introhive.com/resource/whitepaper/the-forrester-total-economic-impact-study/
    date: '2024-08-02'
    access: full
    locator: '''Voice of the Customer'' quotes'
  - ref: INTAPP-HOWESPERCIVAL-2025
    title: Howes Percival uses Intapp DealCloud as its all-in-one platform for CRM, relationship intelligence
      and email marketing (client story)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/case-study/howes-percival-dealcloud/
    date: '2025-02-24'
    access: full
    locator: Section 'Relationship intelligence that supports strong client relationships'
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't
      Use, Introhive Survey Finds
    publisher: LawSites (Robert J. Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: Section 'A New Interface for An Old Problem'
  last_reviewed: '2026-10-19'
  notes: Grade B because the figures are published by the vendor, not by the named firms; the landing-page
    quote for the 97% figure is unnamed and anonymous. The Grassi page shows 253k meetings ingested in
    its header but 53,000 in its impact panel, so no meeting count from that page is used. Older Introhive
    stories for Frazier & Deeter, Gould & Ratner and Colliers carry 2024 site dates and were read but
    not relied on.
- id: professional-services-client-development-02
  title: Relationship mapping and scoring for warm paths, cross-practice coverage and relationship continuity
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - research-synthesis
  - client-interaction
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Firms cannot see who knows whom across practice groups or how strong each relationship is.
    Cross-sell is missed, outreach is duplicated, and relationships can walk out with departing partners.
  solution: 'Captured relationship data (use case 01) is turned into relationship maps and strength scores.
    Teams use them to find warm paths into clients, to coordinate across practices and service lines,
    and to plan for succession, departures and lateral hires. Named: Thomson Snell & Passmore and Grassi
    (Introhive); Howes Percival (DealCloud alerts and an Outlook panel showing who knows the contact and
    the relationship score). Pattern is ''other'': relationship-graph analytics.'
  outcomes:
  - lever: growth
    description: Employees connected to the firm's Top 50 accounts at Thomson Snell & Passmore
    figure: 47 to 97 employees (+106%)
    measures: Employees connected to the firm's Top 50 accounts, as reported on the vendor's case study;
      period not stated
    provenance: vendor-published
    source_ref: INTROHIVE-TSP-2026
  - lever: growth
    description: Practice groups interacting with Top 50 accounts at Thomson Snell & Passmore
    figure: 3 to 5 practice groups (+67%)
    measures: Average department interaction with Top 50 accounts, as labelled on the case study
    provenance: vendor-published
    source_ref: INTROHIVE-TSP-2026
  - lever: experience
    description: What 123 surveyed partners rank as most valuable from combining firm information
    figure: Cross-sell opportunities 54%; at-risk relationship alerts 49%; relationship mapping 46%
    measures: Share of 123 partners (42 legal, 42 accounting, 39 other) ranking each item among the most
      valuable; a preference, not an outcome; survey conducted for Introhive by Thinktiv
    provenance: vendor-published
    source_ref: INTROHIVE-LAWSITES-2026
  prerequisites:
  - Clean, firmwide relationship data from email and calendar capture
  - 'Agreement across practice groups on shared visibility of key accounts (Howes Percival''s advice:
    consult each practice group on its customisations)'
  - A defined list of key accounts
  risks_and_guardrails:
  - Scores and maps are model outputs; Laing O'Rourke says the aim is to back human knowledge with data,
    not replace it (INTROHIVE-LAINGOROURKE-2025)
  - 'Access follows existing permissions: Introhive''s MCP server is described as subject to each user''s
    permissions and firm governance (INTROHIVE-LAWSITES-2026)'
  - No independent evidence that mapping raised revenue or retention was found; the 'Top 50' figures count
    connections, not fees
  human_checkpoints:
  - Partners and BD staff decide whom to contact and what to say; the Akin Gump director says outcomes
    still depend on relationship quality and execution (AKIN-MONEYBALL-2026)
  role_evolution: BD and marketing teams use shared relationship data to coordinate cross-practice outreach;
    the Thomson Snell & Passmore story lists onboarding intelligence for senior lateral hires and succession
    planning for departing lawyers among its deliverables.
  evidence_grade: B
  sources:
  - ref: INTROHIVE-TSP-2026
    title: Thomson Snell & Passmore Doubles Firm-Wide Account Connectivity with Introhive (client story)
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/client-story/thomson-snell-passmore-law-firm-relationship-intelligence/
    date: '2026-08-05'
    access: full
    locator: '''Mapped Relationships Deliverables''; ''Measurable business impact'' panel'
  - ref: INTROHIVE-GRASSI-2026
    title: Grassi Strengthens Client Engagement with Introhive (client story)
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/client-story/grassi-strengthening-client-engagement-with-introhive/
    date: '2026-03-02'
    access: full
    locator: Goals and 'Mapped Relationships Deliverables' (succession planning for departing leaders)
  - ref: INTAPP-HOWESPERCIVAL-2025
    title: Howes Percival uses Intapp DealCloud as its all-in-one platform for CRM, relationship intelligence
      and email marketing (client story)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/case-study/howes-percival-dealcloud/
    date: '2025-02-24'
    access: full
    locator: Section 'Relationship intelligence that supports strong client relationships'
  - ref: INTAPP-DEALCLOUD-2026
    title: The AI-powered deal and relationship intelligence platform (Intapp DealCloud product page;
      read 2026-10-19, no publication date shown)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/dealcloud/
    date: '2026-10-19'
    access: full
    locator: Section 'Relationship intelligence' (relationship maps, relationship scores, outcome attribution)
  - ref: INTROHIVE-LAINGOROURKE-2025
    title: 'Laing O''Rourke: Building Trust with Salesforce & Introhive (client story)'
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/client-story/laing-orourke-case-study-introhive-salesforce/
    date: '2025-07-10'
    access: full
    locator: Situation section
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't
      Use, Introhive Survey Finds
    publisher: LawSites (Robert J. Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: Section 'What Partners Say They Want'
  last_reviewed: '2026-10-19'
  notes: Succession and lateral-onboarding uses are listed as deliverables on the Introhive case studies;
    no outcome was published for them. Merged with continuity use because the same relationship map serves
    both.
- id: professional-services-client-development-03
  title: AI-prepared pre-meeting client briefs and digests for partners
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - research-synthesis
  - client-interaction
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Preparing for a client or prospect meeting means searching the CRM, inboxes, news and filings
    by hand. Partners with little non-billable time arrive underprepared or skip preparation.
  solution: A brief or digest is generated before a meeting from relationship history, recent account
    activity, company news, role changes and, in some tools, firm matter history and public filings. Introhive
    client stories name pre-meeting digests or briefs at Grassi, LBMC and Thomson Snell & Passmore. Practus
    and Auxana chose DealCloud with Celeste, which Intapp says surfaces such briefs in seconds. Harvey
    describes briefs built from its Vault and EDGAR filings.
  outcomes:
  - lever: speed
    description: Brief preparation time, Practus/Auxana deployment
    figure: Intapp states briefs 'that would otherwise require hours of research can be surfaced in seconds';
      no measurement given
    measures: Vendor description of expected preparation time; deployment announced, not yet reported
      on
    provenance: vendor-published
    source_ref: INTAPP-PRACTUS-2026
  - lever: speed
    description: 'Sales preparation time at a global risk-assessment data firm (adjacent: not a professional-services
      firm) using a Salesforce Agentforce meeting-preparation assistant'
    figure: Up to 50% faster sales preparation cycles
    measures: '''Sales preparation cycles'', as labelled by the implementation partner; baseline and method
      not shown'
    provenance: vendor-published
    source_ref: BRIDGENEXT-AGENTFORCE-2026
  prerequisites:
  - Relationship and activity data in a CRM (use case 01)
  - Access to news and filings sources
  - 'Briefing of partners on how to use the output: CMBDO panelists said training before client meetings
    matters (TRI-CMBDO-2026)'
  risks_and_guardrails:
  - Panelists stress that briefs are a foundation, not a script; one law-firm technology specialist put
    the AI contribution at about 90% and said the rest needs human judgment (TRI-CMBDO-2026)
  - Quinn Emanuel's research-brief prompt requires primary-document verification and labels each claim
    as fact, allegation or inference (TR-NAVIGATING-2026)
  - No error rates, correction rates or partner override rates were found for any brief tool
  human_checkpoints:
  - The partner reads, interprets and personalises the brief before using it with a client (TRI-CMBDO-2026)
  role_evolution: Partners spend less time gathering background; training for partners on using briefs
    is described as one-to-one and role-specific.
  evidence_grade: B
  sources:
  - ref: INTROHIVE-GRASSI-2026
    title: Grassi Strengthens Client Engagement with Introhive (client story)
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/client-story/grassi-strengthening-client-engagement-with-introhive/
    date: '2026-03-02'
    access: full
    locator: 'Solution: ''Pre-Meeting Intelligence Briefs'''
  - ref: INTROHIVE-LBMC-2024
    title: LBMC Achieves 567% ROI in Their First Step Into Digital Transformation with Introhive (client
      story; page modified 2026-06-22)
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/client-story/lbmc/
    date: '2024-07-24'
    access: full
    locator: 'Solution: ''AI-driven pre-meeting digests with actionable client insights'''
  - ref: INTROHIVE-TSP-2026
    title: Thomson Snell & Passmore Doubles Firm-Wide Account Connectivity with Introhive (client story)
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/client-story/thomson-snell-passmore-law-firm-relationship-intelligence/
    date: '2026-08-05'
    access: full
    locator: 'Solution: ''Proactive client intelligence'''
  - ref: INTAPP-PRACTUS-2026
    title: Practus LLP deploys Intapp's agentic AI solutions to power innovation and growth (press release,
      Business Wire copy)
    publisher: Intapp via Business Wire
    type: vendor
    url: https://finviz.com/news/387470/practus-llp-deploys-intapps-agentic-ai-solutions-to-power-innovation-and-growth
    date: '2026-09-01'
    access: full
    locator: Section 'Empowering lawyers with data and AI'
  - ref: HARVEY-BD-2026
    title: How Law Firms Use AI for Business Development and Client Intelligence
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/ai-for-law-firm-business-development
    date: '2026-06-23'
    access: full
    locator: Section '7 Ways Harvey Can Support Legal Business Development', item 1
  - ref: TRI-CMBDO-2026
    title: 'Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI
      may be talking to your clients about it'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai
    date: '2026-02-18'
    access: full
    locator: Sections 'AI as an assistant, not a replacement' and 'Strong need for lawyer training around
      AI'
  - ref: TR-NAVIGATING-2026
    title: 'Navigating New Waters: Using AI for Tailored Client Journeys (panel slides: Equinox Strategy
      Partners, Quinn Emanuel, MyMai, Willkie Farr & Gallagher)'
    publisher: Thomson Reuters (event slide deck)
    type: conference
    url: https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2025/01/Navigating-New-Waters.pdf
    date: '2026-01-21'
    access: full
    locator: 'Slides ''Example #2 Client Research Brief'''
  - ref: BRIDGENEXT-AGENTFORCE-2026
    title: Global Risk Assessment Firm Accelerates Sales Preparation by 30-50% with Agentforce (implementation-partner
      case study; client is a financial-services data and risk firm, not a professional-services firm)
    publisher: Bridgenext
    type: vendor
    url: https://www.bridgenext.com/our-work/success-stories/ai-sales-acceleration-with-salesforce-agentforce/
    date: '2026-08-12'
    access: full
    locator: Benefits panel
  last_reviewed: '2026-10-19'
  notes: Grade B rests on named firms using briefs (Grassi, LBMC, TSP) with no published measurement of
    preparation time. The only time figure is from an adjacent, non-professional-services process (Bridgenext)
    and caps the grade at B. Practus/Auxana is an announcement with 'will deploy' wording.
- id: professional-services-client-development-04
  title: Client-health signals and contact-frequency alerts for relationship owners
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - client-interaction
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Relationship owners lose touch with clients, miss job changes and news, and notice a cooling
    relationship only after work has moved.
  solution: The CRM layer watches contact frequency, relationship strength and external signals (news,
    role changes) and alerts the relationship owner or BD team. Howes Percival says DealCloud dashboards
    and alerts help it keep in touch with clients at the right frequency. Thomson Snell & Passmore lists
    real-time client health and job-change tracking.
  outcomes:
  - lever: experience
    description: Proactive client service at Howes Percival, described qualitatively
    figure: none published
    measures: The firm's BD and Marketing Director describes more proactive service through dashboards
      and alerts; no retention, satisfaction or frequency figure is given
    provenance: vendor-published
    source_ref: INTAPP-HOWESPERCIVAL-2025
  prerequisites:
  - Relationship data capture (use case 01)
  - Agreed contact-frequency standards for key clients
  - A route from alert to named owner
  risks_and_guardrails:
  - Alert quality depends on data quality; the vendor CEO says automated outreach prompts need accurate
    data (INTROHIVE-LAWSITES-2026)
  - No evidence found that alerts reduced client loss
  human_checkpoints:
  - The relationship owner decides whether and how to act on each alert
  role_evolution: BD teams and partners are prompted to act on relationship signals instead of relying
    on memory.
  evidence_grade: B
  sources:
  - ref: INTAPP-HOWESPERCIVAL-2025
    title: Howes Percival uses Intapp DealCloud as its all-in-one platform for CRM, relationship intelligence
      and email marketing (client story)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/case-study/howes-percival-dealcloud/
    date: '2025-02-24'
    access: full
    locator: Sections 'Relationship intelligence that supports strong client relationships' and 'Executive
      summary'
  - ref: INTROHIVE-TSP-2026
    title: Thomson Snell & Passmore Doubles Firm-Wide Account Connectivity with Introhive (client story)
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/client-story/thomson-snell-passmore-law-firm-relationship-intelligence/
    date: '2026-08-05'
    access: full
    locator: 'Solution: ''Real-time client health and job change tracking with Signals'''
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't
      Use, Introhive Survey Finds
    publisher: LawSites (Robert J. Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: Section 'A New Interface for An Old Problem'
  last_reviewed: '2026-10-19'
  notes: 'Grade B on a named firm using alerts, with no measurement. Survey: 49% of 123 partners rank
    at-risk relationship alerts among the most valuable uses of combined firm data (INTROHIVE-LAWSITES-2026,
    vendor-commissioned).'
- id: professional-services-client-development-05
  title: Conversational and agentic assistants over CRM and relationship data for BD staff and partners
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - client-interaction
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Partners do not log into the CRM, so relationship intelligence stays in a system they do not
    open.
  solution: Plain-language questions and playbook-driven agents sit on top of the CRM. Intapp's Celeste
    (generally available 2026-07-15) ships playbooks for origination and business development and answers
    questions over relationship history and pipeline. Practus/Auxana, Wotton Kearney and Forvis Mazars
    Capital Advisors announced selection of DealCloud with Celeste; Ropes & Gray bought Celeste and DealCloud,
    according to Intapp. Introhive offers an MCP server so assistants such as Claude, Harvey, ChatGPT
    and Copilot can query a firm's relationship data under existing permissions.
  outcomes:
  - lever: speed
    description: Time to assemble relevant matters, partner experience and prior pitch materials for an
      urgent client request
    figure: Intapp says 'minutes rather than hours'; no measurement
    measures: Vendor description; early-adopter firms BakerHostetler and Hg were quoted on intake, conflicts
      and mandate screening, not on this use
    provenance: vendor-published
    source_ref: LAWSITES-CELESTE-2026
  prerequisites:
  - A governed relationship system of record (DealCloud or similar)
  - Ethical walls and need-to-know restrictions applied to the assistant
  - Implementation partner (Epiq for Wotton Kearney)
  risks_and_guardrails:
  - Intapp says the same walls, restrictions and audit requirements that apply to staff apply to Celeste
    (LAWSITES-CELESTE-2026)
  - An Intapp executive on the earnings call said MCP creates repositories of business information that
    sit outside a firm's professional compliance controls (INTAPP-Q3CALL-2026)
  - TRI CMBDO panelists warned agents are limited by the data and tools they are given (TRI-CMBDO-2026)
  - All selections found are announcements; no firm has published BD results
  human_checkpoints:
  - Staff review answers before outreach; Celeste is described as acting through playbooks that firms
    define
  role_evolution: BD professionals and lawyers ask questions in plain language rather than navigate dashboards
    (INTAPP-WOTTONKEARNEY-2026). Purchase of AI tools in firms is often led by IT or innovation groups
    rather than marketing and BD, the Introhive CEO says (INTROHIVE-LAWSITES-2026).
  evidence_grade: C
  sources:
  - ref: LAWSITES-CELESTE-2026
    title: Intapp Makes Celeste Generally Available, Calling It An 'AI Coworker' To Run the Business Side
      of Law Firms
    publisher: LawSites (Robert J. Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/07/intapp-makes-celeste-generally-available-calling-it-an-ai-coworker-to-run-the-business-side-of-law-firms.html
    date: '2026-07-16'
    access: full
    locator: Sections 'For the Business, Not the Practice, of Law' and 'Feedback from Early Adopters'
  - ref: INTAPP-PRACTUS-2026
    title: Practus LLP deploys Intapp's agentic AI solutions to power innovation and growth (press release,
      Business Wire copy)
    publisher: Intapp via Business Wire
    type: vendor
    url: https://finviz.com/news/387470/practus-llp-deploys-intapps-agentic-ai-solutions-to-power-innovation-and-growth
    date: '2026-09-01'
    access: full
    locator: Section 'Empowering lawyers with data and AI'
  - ref: INTAPP-WOTTONKEARNEY-2026
    title: Wotton Kearney selects Intapp DealCloud with Celeste to power relationship intelligence and
      AI-driven growth (press release)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/news/wotton-kearney-intapp-celeste/
    date: '2026-07-09'
    access: full
    locator: Body paragraphs 3-5
  - ref: INTAPP-FORVISMAZARS-2026
    title: Forvis Mazars Capital Advisors selects Intapp DealCloud with Celeste to advance firmwide agentic
      AI strategy (press release)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/news/forvis-mazars-intapp-celeste/
    date: '2026-09-22'
    access: full
    locator: Body paragraphs 2-3
  - ref: INTAPP-Q3CALL-2026
    title: Intapp (INTA) Q3 fiscal 2026 earnings call transcript (call held 2026-05-05; transcript published
      2026-05-06)
    publisher: The Motley Fool via Yahoo Finance
    type: vendor
    url: https://finance.yahoo.com/markets/stocks/articles/intapp-inta-q3-2026-earnings-151600418.html
    date: '2026-05-05'
    access: full
    locator: Remarks on Ropes & Gray and MCP
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't
      Use, Introhive Survey Finds
    publisher: LawSites (Robert J. Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: Section 'MCP and Agnostic Access to Data'
  - ref: TRI-CMBDO-2026
    title: 'Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI
      may be talking to your clients about it'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai
    date: '2026-02-18'
    access: full
    locator: Paragraph on agentic AI
  last_reviewed: '2026-10-19'
  notes: 'Grade C: the evidence is vendor announcements and a general-availability launch (2026-07-15).
    Intapp told investors that over 15% of net new bookings in its fiscal Q3 (call dated 2026-05-05) came
    from Celeste, which measures vendor sales, not client outcomes. Ropes & Gray''s BD use is stated only
    by the vendor. Intapp announced a DCM Insights partnership in April 2026 adding Celeste agents to
    BD (seen in search only; not opened).'
- id: professional-services-client-development-06
  title: Opportunity scouting and market-signal monitoring for origination and cross-sell
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - research-synthesis
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Finding new mandates and cross-sell openings means manual searching of court records, news
    and filings that busy lawyers cannot do consistently.
  solution: Firms run scheduled or built-in intelligence tools that combine internal relationship and
    matter data with external sources and return a scored list of opportunities. Akin Gump built 'Moneyball'
    in-house to identify and evaluate opportunities from internal and external intelligence. At a Thomson
    Reuters session, Quinn Emanuel showed daily deep-research prompts that scan appellate decisions and
    verdicts and score matters for 'who pays' and intervention windows. Willkie Farr & Gallagher showed
    a 'battlecard' that positions the firm against research on a target.
  outcomes:
  - lever: quality
    description: Change in internal BD conversations at Akin Gump
    figure: none published; the firm says discussion moved from reviewing information to deciding what
      to do with it
    measures: Qualitative statement by the firm's senior director of marketing and client intelligence;
      no count of opportunities, wins or revenue
    provenance: self-reported
    source_ref: AKIN-MONEYBALL-2026
  prerequisites:
  - Internal data on clients, matters and relationships
  - A firm view of client development priorities and service opportunities (Akin built its own layer for
    this)
  - A BD or client-intelligence team able to tune the tool
  risks_and_guardrails:
  - 'Akin: the tool ''doesn''t create opportunities'' by itself; outcomes depend on relationship and execution
    (AKIN-MONEYBALL-2026)'
  - Quinn Emanuel's prompts use pass/fail filters, quantified scoring, an exclusion log and primary-source
    verification (TR-NAVIGATING-2026)
  - No hit rates, false-positive rates or revenue attribution found
  human_checkpoints:
  - Lawyers and BD staff evaluate and decide which opportunities to pursue (AKIN-MONEYBALL-2026)
  role_evolution: Akin has a senior director of marketing and client intelligence who owns the tool's
    design; Quinn Emanuel runs an AI and data analytics group with a prompt library and mandatory AI training
    (TR-NAVIGATING-2026).
  evidence_grade: B
  sources:
  - ref: AKIN-MONEYBALL-2026
    title: The Lawyer Highlights How Akin's AI Tool 'Moneyball' is Advancing Client Development
    publisher: Akin Gump Strauss Hauer & Feld LLP (firm news item summarising The Lawyer)
    type: firm
    url: https://www.akingump.com/en/insights/media-mentions/the-lawyer-highlights-how-akins-ai-tool-moneyball-is-advancing-client-development
    date: '2026-10-05'
    access: full
    locator: Paragraphs 1-3
  - ref: TR-NAVIGATING-2026
    title: 'Navigating New Waters: Using AI for Tailored Client Journeys (panel slides: Equinox Strategy
      Partners, Quinn Emanuel, MyMai, Willkie Farr & Gallagher)'
    publisher: Thomson Reuters (event slide deck)
    type: conference
    url: https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2025/01/Navigating-New-Waters.pdf
    date: '2026-01-21'
    access: full
    locator: 'Slides ''Real-World AI BD Use Cases at Quinn Emanuel'', ''Appellate BD Scout'', ''Use Case
      #3 Business Development & Client Analysis'' (Willkie)'
  - ref: TRI-CMBDO-2026
    title: 'Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI
      may be talking to your clients about it'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai
    date: '2026-02-18'
    access: full
    locator: 'Paragraph: BD described as an ideal starting point for agentic AI'
  last_reviewed: '2026-10-19'
  notes: The Willkie slide describes a battlecard product and its delivery but does not say the firm has
    it in production; only the Akin and Quinn Emanuel examples are treated as in use. The Lawyer article
    was not readable (bot check).
- id: professional-services-client-development-07
  title: Tailored client notes, alerts and sector briefings drafted with AI
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - document-production
  - client-interaction
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Senior lawyers seldom send regular client notes because drafting them competes with billable
    work, and generic newsletters do not reach a specific client's situation.
  solution: AI pulls news, regulatory developments, earnings calls, relationship data and, at one panel,
    what clients are reading, and drafts a conversation opener or client alert for the partner. Harvey's
    guide lists client alerts, sector risk briefings and prospect 'issues to watch' reports. At Parker
    Poe, clients and lawyers built assistants that tailor one legal update to different executives (see
    use case 11).
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: No firm reported a measured result; panel and vendor descriptions only
    provenance: vendor-published
    source_ref: HARVEY-BD-2026
  prerequisites:
  - Authoritative legal and news sources
  - Relationship data to choose recipients
  - Partner training in how to use drafts
  risks_and_guardrails:
  - 'Panelists: use AI output to start a conversation, not as a script (TRI-CMBDO-2026)'
  - Citation and source accuracy are not evidenced for these client-note tools
  human_checkpoints:
  - The partner edits and sends the note; the CMBDO panel says authenticity and interpretation remain
    with the lawyer
  role_evolution: BD teams 'plant' tailored prompts for partners, in one panelist's words; partners keep
    the relationship voice.
  evidence_grade: C
  sources:
  - ref: TRI-CMBDO-2026
    title: 'Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI
      may be talking to your clients about it'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai
    date: '2026-02-18'
    access: full
    locator: Section 'AI as an assistant, not a replacement'
  - ref: HARVEY-BD-2026
    title: How Law Firms Use AI for Business Development and Client Intelligence
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/ai-for-law-firm-business-development
    date: '2026-06-23'
    access: full
    locator: Section '7 Ways Harvey Can Support Legal Business Development', item 4
  - ref: PARKERPOE-LAWSITES-2026
    title: Parker Poe Clients & Attorneys Build AI Assistants Together to Help Deliver Better Outcomes
      (firm press release carried by LawSites)
    publisher: LawSites (Robert J. Ambrogi); release by Parker Poe Adams & Bernstein LLP dated 2026-09-11
    type: press
    url: https://www.lawnext.com/2026/09/parker-poe-clients-attorneys-build-ai-assistants-together-to-help-deliver-better-outcomes.html
    date: '2026-09-16'
    access: full
    locator: 'Tracks paragraph: executive-briefing track'
  last_reviewed: '2026-10-19'
  notes: 'Grade C: vendor description plus unnamed panelists. Named firm evidence for tailored executive
    updates comes only from the Parker Poe workshop.'
- id: professional-services-client-development-08
  title: Behavioural nudges and coaching prompts to partners for proactive client contact
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - client-interaction
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Partners know they should contact clients regularly but do not find the time or a reason.
  solution: The CRM prompts a partner when a relationship has gone quiet and supplies a draft message
    or script. Intapp sells DealCloud Activator as an AI-enabled tool that nudges and coaches partners
    toward 'Activator' behaviours, with metrics and leaderboards for leaders. The Introhive CEO gives
    the same example of a prompt after 35 days without contact.
  outcomes:
  - lever: growth
    description: Partner BD performance, from the Rainmaker Genome Project study by DCM Insights with
      Intapp
    figure: Up to 32%
    measures: 'Intapp''s wording: leaning into Activator behaviours can raise the average partner''s BD
      performance ''up to 32%''. The metric definition is not given, and the study concerns behaviours,
      not the tool'
    provenance: vendor-published
    source_ref: INTAPP-ACTIVATOR-2026
  prerequisites:
  - Relationship data capture
  - Firm agreement on which BD behaviours to encourage
  - Behavioural training (Intapp points to DCM Insights programmes)
  risks_and_guardrails:
  - Leaderboards and metrics on BD activity may be read as surveillance by partners; the sources do not
    discuss this
  - No named customer and no measurement of the tool itself found
  human_checkpoints:
  - The partner chooses whether to send the suggested message
  role_evolution: Leaders get activity and collaboration metrics for partners; partners get prompts in
    their daily workflow.
  evidence_grade: C
  sources:
  - ref: INTAPP-ACTIVATOR-2026
    title: Intapp DealCloud Activator (product page; read 2026-10-19, no publication date shown)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/legal/activator/
    date: '2026-10-19'
    access: full
    locator: Sections on Activator behaviours and 'Activator behaviors increase revenue'
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't
      Use, Introhive Survey Finds
    publisher: LawSites (Robert J. Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: Section 'A New Interface for An Old Problem'
  last_reviewed: '2026-10-19'
  notes: Vendor claim only. Intapp says Activator's research found specific behaviours distinguish top
    performers.
- id: professional-services-client-development-09
  title: AI-assisted key-account plans and cross-sell opportunity matrices
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - coordination-scheduling
  - expert-judgment
  pattern: research-brief
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Key-account programmes depend on account plans that need data from many practices; relationship
    data is fragmented so plans are thin.
  solution: AI generates account relationship summaries and an 'opportunity matrix' that matches a client's
    needs to the firm's capabilities, as a starting point for the account team. Intapp lists key-account
    programmes with AI-revealed cross-sell opportunities. Introhive's guide for architecture, engineering
    and construction firms describes AI-powered relationship summaries and relationship maps for strategic
    account planning.
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: Vendor guide asserts that up to 90% of firms fail to grow key accounts because data is fragmented;
      no source or method is given
    provenance: vendor-published
    source_ref: INTROHIVE-SAM-2025
  prerequisites:
  - Unified relationship and matter data
  - Named key accounts and account teams
  risks_and_guardrails:
  - The 90% claim is unverified vendor wording
  - No named firm reports AI-built account plans in use
  human_checkpoints:
  - Account team decides plan content and owners
  role_evolution: Not evidenced.
  evidence_grade: C
  sources:
  - ref: INTAPP-DEALCLOUD-2026
    title: The AI-powered deal and relationship intelligence platform (Intapp DealCloud product page;
      read 2026-10-19, no publication date shown)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/dealcloud/
    date: '2026-10-19'
    access: full
    locator: 'Legal section: ''Key account programs'''
  - ref: INTROHIVE-SAM-2025
    title: Strategic Account Management Framework (guide landing page)
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/whitepaper/strategic-account-management-framework/
    date: '2025-11-06'
    access: full
    locator: Page body
  - ref: TRI-CMBDO-2026
    title: 'Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI
      may be talking to your clients about it'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai
    date: '2026-02-18'
    access: full
    locator: Paragraph on the 'opportunity matrix'
  - ref: INTROHIVE-LBMC-2024
    title: LBMC Achieves 567% ROI in Their First Step Into Digital Transformation with Introhive (client
      story; page modified 2026-06-22)
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/resource/client-story/lbmc/
    date: '2024-07-24'
    access: full
    locator: 'Deliverables: ''Relationship scoring for account planning and cross-selling'''
  last_reviewed: '2026-10-19'
  notes: LBMC lists account planning among its deliverables but reports no result. Practitioners at the
    CMBDO Forum discussed the matrix idea; no firm was named.
- id: professional-services-client-development-10
  title: Revenue attribution and ROI measurement for business development
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Most firms cannot connect BD activity to revenue, so they cannot show whether relationship
    tools or AI pay back.
  solution: Link mandates, deals and revenue back to the relationships and activities that produced them.
    Intapp lists 'outcome attribution' in DealCloud. The Introhive survey shows the gap partners want
    closed.
  outcomes:
  - lever: growth
    description: Current state of BD ROI measurement among 123 surveyed partners
    figure: 63% have no revenue-linked way to measure BD ROI; 15% can track revenue with strong attribution;
      28% track intermediate metrics (introductions, meetings)
    measures: Share of 123 partners reporting how their firm measures BD return on investment; survey
      conducted for Introhive by Thinktiv
    provenance: vendor-published
    source_ref: INTROHIVE-LAWSITES-2026
  prerequisites:
  - Reliable relationship and activity data
  - Link between CRM and billing or matter data
  risks_and_guardrails:
  - 'The Introhive CEO concedes firms contest attribution: lawyers say the relationship, not the data,
    produced the business (INTROHIVE-LAWSITES-2026)'
  human_checkpoints:
  - BD leaders agree which attribution rules count
  role_evolution: Not evidenced.
  evidence_grade: C
  sources:
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't
      Use, Introhive Survey Finds
    publisher: LawSites (Robert J. Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: Section 'Measuring Return'
  - ref: INTROHIVE-PARTNER-2026
    title: AI Without Relationship Context Won't Deliver BD ROI, Introhive's 2026 Partner Survey Report
      Finds
    publisher: Introhive
    type: vendor
    url: https://www.introhive.com/news/ai-without-relationship-context-wont-deliver-bd-roi-introhives-2026-partner-survey-report-finds/
    date: '2026-10-13'
    access: full
    locator: Paragraph 'Measurement is also early'
  - ref: INTAPP-DEALCLOUD-2026
    title: The AI-powered deal and relationship intelligence platform (Intapp DealCloud product page;
      read 2026-10-19, no publication date shown)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/dealcloud/
    date: '2026-10-19'
    access: full
    locator: 'Section ''Relationship intelligence'': ''Outcome attribution'''
  last_reviewed: '2026-10-19'
  notes: 'Grade C: vendor feature plus a vendor-commissioned survey. No firm reports using attribution.'
- id: professional-services-client-development-11
  title: Client AI labs where clients and lawyers build AI assistants together
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Clients want evidence that a firm's AI helps them, but talk about AI rarely turns into shared
    work.
  solution: Parker Poe held an invitation-only workshop on 2026-09-10 in Charlotte where general counsel,
    legal operations leaders, compliance staff, business executives and firm lawyers built and tested
    AI apps in teams using the Lega AI Builder Lab. Tracks were company research, risk disclosure updates
    and executive legal briefings; the executive-briefing track drew about 90% of participants. It was
    part of the firm's 'Moments That Matter' client experience programme. The release says a similar lab
    with Fasken in Canada preceded it.
  outcomes:
  - lever: experience
    description: Participant choice in the Parker Poe lab
    figure: about 90% of participants chose the executive briefing track
    measures: Share of participants who chose the executive legal briefing track; a participation figure,
      not an outcome
    provenance: self-reported
    source_ref: PARKERPOE-LAWSITES-2026
  prerequisites:
  - A client experience programme and client invitations
  - A lab platform and facilitator (Lega, per the release)
  - Firm and client data approved for use in the exercise
  risks_and_guardrails:
  - Law.com sources note firms fear that clients who can do work themselves may pay less (see use case
    12)
  - The release states data and knowledge sources were created for the workshop; production use is described
    as future ('Tomorrow we can be...')
  human_checkpoints:
  - Lawyers and client staff jointly judge which outputs are useful
  role_evolution: Business-development and client-experience leads (Parker Poe's chief marketing and BD
    officer is quoted) host client engagements built around shared making rather than presentations.
  evidence_grade: B
  sources:
  - ref: PARKERPOE-LAWSITES-2026
    title: Parker Poe Clients & Attorneys Build AI Assistants Together to Help Deliver Better Outcomes
      (firm press release carried by LawSites)
    publisher: LawSites (Robert J. Ambrogi); release by Parker Poe Adams & Bernstein LLP dated 2026-09-11
    type: press
    url: https://www.lawnext.com/2026/09/parker-poe-clients-attorneys-build-ai-assistants-together-to-help-deliver-better-outcomes.html
    date: '2026-09-16'
    access: full
    locator: Opening paragraph; tracks paragraph; Lega AI Builder Lab paragraph; 'Moments That Matter'
      paragraph; Fasken paragraph
  last_reviewed: '2026-10-19'
  notes: 'Single source: the firm''s own press release. No independent coverage, no client outcome. In-house
    clients took part (Symphonic Distribution''s head of legal is quoted).'
- id: professional-services-client-development-12
  title: Firm-built AI products and portals offered to clients as relationship assets
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - client-interaction
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: Clients want AI-enabled service but see little of what firms do; firms want a way to stay central
    as clients adopt AI themselves.
  solution: Firms package their knowledge into client-facing tools. Debevoise's STAAR (Suite of Tools
    for Assessing AI Risk) gives clients access to the firm's guidance on AI governance and risk, and
    ABA Journal reports STAAR 2.0 as a subscription platform built with Legora. Cooley made Cooley GO
    Lab, a Legora-built workspace, available free to a summer Y Combinator cohort. A&O Shearman has a
    revenue-sharing arrangement with Harvey to license its tools to clients and other firms. Legora's
    Portal product lets firms invite clients into a white-labelled workspace and run firm-designed workflows
    without seeing prompts or logic; a Linklaters partner is quoted on its page.
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: No usage, revenue or retention figure found for any of these offers
    provenance: self-reported
    source_ref: DEBEVOISE-BLOOMBERG-2026
  prerequisites:
  - Curated firm knowledge that partners agree to contribute (Debevoise cites its collaborative culture)
  - A platform partner
  - Pricing and licensing decisions for client access
  risks_and_guardrails:
  - A consultant told Law.com that firms fear clients using AI themselves or licensing their 'secret sauce'
    to peers (ABAJ-SHARE-2026)
  - Cooley's partner says the aim includes being seen as best-in-class on information (ABAJ-SHARE-2026)
  human_checkpoints:
  - Firm lawyers curate and review the guidance that tools draw on; Debevoise says STAAR complements lawyers'
    advice
  role_evolution: Partners contribute knowledge to firm products; firms need product and platform owners
    (not evidenced in detail in the sources).
  evidence_grade: B
  sources:
  - ref: ABAJ-SHARE-2026
    title: Should law firms share AI tools with their clients and peers?
    publisher: ABA Journal
    type: press
    url: https://www.abajournal.com/news/article/should-law-firms-share-ai-tools-with-their-clients-and-peers
    date: '2026-07-14'
    access: full
    locator: Paragraphs 2-4
  - ref: DEBEVOISE-BLOOMBERG-2026
    title: Bloomberg Law Features Debevoise's AI Strategy and STAAR Platform
    publisher: Debevoise & Plimpton LLP
    type: firm
    url: https://www.debevoise.com/news/2026/08/bloomberg-law-features-debevoises-ai
    date: '2026-08-06'
    access: full
    locator: Body paragraphs 1-2
  - ref: COOLEY-LAWCOM-2026
    title: Law Firms Are Building Their Own AI Tools. Should They Share Them? (press-mention page; Law.com
      article is subscription only)
    publisher: Cooley LLP
    type: firm
    url: https://www.cooley.com/news/coverage/2026/2026-07-14-law-firms-are-building-their-own-ai-tools-should-they-share-them
    date: '2026-07-14'
    access: full
    locator: Item text
  - ref: LEGORA-PORTAL-2026
    title: 'Portal: the new standard in legal collaboration (product page; read 2026-10-19, no publication
      date shown)'
    publisher: Legora
    type: vendor
    url: https://legora.com/product/portal
    date: '2026-10-19'
    access: full
    locator: Sections 'Firm-powered AI solutions', 'White-label user experience' and the partner quote
  last_reviewed: '2026-10-19'
  notes: Overlaps with the service model (productised services); see routing. A&O Shearman and STAAR details
    come second-hand via ABA Journal's summary of Law.com. The Legora Portal quote is vendor-selected.
- id: professional-services-client-development-13
  title: Client-facing AI enablement roles that scope client-specific AI work and support pitches
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - client-interaction
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Clients ask what the firm's AI means for them, but partners lack the time or knowledge to scope
    AI engagements and answer technology questions in pitches.
  solution: 'A dedicated innovation team supports partners and clients: Latham & Watkins'' ''Innovation
    Attorney - Client Team Enablement'' scopes and delivers client-specific AI engagements (workflows,
    pilots, workshops), advises partners and clients on capabilities and limits, works with Business Development
    on panels, pitches and RFPs, and tracks client interactions in firm repositories. Search summaries
    show similar postings at Latham (Associate Director of AI & Innovation - Client Services), Baker McKenzie
    (Client AI Risk Lead) and Wolf Greenfield (technology engagement manager); these were not opened.'
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: A job description reports no outcomes
    provenance: self-reported
    source_ref: LATHAM-INNOVATIONATTY-2026
  prerequisites:
  - An AI and legal innovation function
  - An approved catalogue of AI and legal technology capabilities (the role helps maintain one)
  - Security and confidentiality controls for client-specific work
  risks_and_guardrails:
  - The posting requires delivery 'with appropriate quality, documentation, confidentiality, information
    security' and compliance with firm and client requirements
  human_checkpoints:
  - Work is delivered with required human oversight, which the role advises clients on
  role_evolution: New hybrid roles sit between innovation, client service and business development. Pay
    ranges seen in search summaries were USD 320,000-400,000 (Latham director posting) and USD 133,600-178,500
    (Wolf Greenfield); both unverified.
  evidence_grade: B
  sources:
  - ref: LATHAM-INNOVATIONATTY-2026
    title: 'Job description: Innovation Attorney - Client Team Enablement (last updated 2026-02-26)'
    publisher: Latham & Watkins LLP
    type: job-posting
    url: https://www.lw.com/admin/upload/SiteAttachments/Innovation-Attorney-Client-Team-Enablement.pdf
    date: '2026-02-26'
    access: full
    locator: Role Overview; Essential Duties 1-4, 9, 11-13
  - ref: LATHAM-ADAI-2026
    title: 'Job posting: Associate Director of AI & Innovation - Client Services (page returned HTTP 410
      when opened; known only from a search summary)'
    publisher: Latham & Watkins LLP
    type: job-posting
    url: https://careers-lw.icims.com/jobs/6958/associate-director-of-ai-%26-innovation-%e2%80%93-client-services/job
    date: '2026'
    access: search-only
    locator: Search summary only
  - ref: BAKERMCKENZIE-CLIENTAIRISK-2026
    title: 'Job posting: Client AI Risk Lead (page not found when opened; known only from a search summary)'
    publisher: Baker McKenzie
    type: job-posting
    url: https://careers.bakermckenzie.com/es_ES/opportunities/JobDetail?jobId=2759
    date: '2026'
    access: search-only
    locator: Search summary only
  - ref: WOLFGREENFIELD-2026
    title: 'Job posting: Manager of Legal Technology Engagement (page blocked; known only from a search
      summary that gave ''August 2026'')'
    publisher: Wolf Greenfield via GoParalegals
    type: job-posting
    url: https://www.goparalegals.com/jobs/572837999-manager-of-legal-technology-engagement-at-wolf-greenfield
    date: 2026-08
    access: search-only
    locator: Search summary only
  last_reviewed: '2026-10-19'
  notes: Grade B rests on the opened Latham job description (full access). The other three postings are
    search-only and are not used to support the grade. Date of the Latham document is 'last updated 2026-02-26';
    posting date not shown.
- id: professional-services-client-development-14
  title: Matter-level evidence of AI use and savings for client conversations
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
  maturity: announced
  problem: Clients ask how AI is used on their matters and what it saves; firms mostly answer that they
    are still gathering data. Some clients demand line-item AI transparency or refuse to pay for AI-done
    tasks.
  solution: 'Capture AI-assisted work automatically at matter level so partners can show clients what
    was done and what it saved. Legora and Laurel announced on 2026-10-13 that Laurel will turn each task
    done in Legora into a draft time entry with client, matter and narrative, and that a second phase
    will jointly develop measures of AI usage and value. Thomson Reuters Institute reports partners need
    better client data and a conversation sequence: what changed in the work, what changed for the client,
    what value, then pricing.'
  outcomes:
  - lever: experience
    description: Client demand for AI value, from Thomson Reuters Institute research
    figure: 78% of corporate clients say AI-enabled quality improvements are very important or essential;
      6% say most or all providers deliver them; 32% will reconsider relationships within 12 months
    measures: Share of corporate clients who buy professional services, from a survey of 1,816 professionals
      fielded March-April 2026; the client subset size is not stated; publisher sells AI products
    provenance: vendor-published
    source_ref: TR-FOP-2026
  prerequisites:
  - Automatic time and AI-usage capture
  - Agreed measures of AI value with the client
  - Partner training to hold the conversation
  risks_and_guardrails:
  - 'Clients send contradictory instructions: demand AI use, forbid it without permission, or refuse to
    pay for AI-done tasks (TRI-LEGALWEEK-2026)'
  - Firm leaders said measurement is still anecdotal (TRI-LEGALWEEK-2026)
  - Leading with price concessions may train clients to expect discounts (TRI-STANDOUT-2026)
  - See landscape ref CALBAR-GENAI-2026 on billing rules (not re-opened here)
  human_checkpoints:
  - Lawyers review draft time entries (LEGORA-LAUREL-2026); partners lead the value conversation
  role_evolution: Greenberg Traurig's chief pricing and innovation officer said clients that were silent
    about AI are now asking how it is used on their matters (TRI-LEGALWEEK-2026), which makes pricing
    and innovation leaders part of client conversations.
  evidence_grade: C
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: Sections 'Proving AI's path to saving clients money' and 'The contradictions in the room'
  - ref: TRI-STANDOUT-2026
    title: 'Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice
    date: '2026-08-06'
    access: full
    locator: Section 'How to talk to clients about AI'
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026 (survey of 1,816 professionals fielded March-April 2026;
      page shows no publication date)
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: Section 'Clients are already moving on'; headline statistics panel
  - ref: LEGORA-LAUREL-2026
    title: Legora and Laurel partner to capture the time lawyers spend in Legora as they work
    publisher: Legora
    type: vendor
    url: https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work
    date: '2026-10-13'
    access: full
    locator: Paragraphs 2-5
  last_reviewed: '2026-10-19'
  notes: 'Grade C: the tooling is an announcement and the client demand evidence is survey and conference
    reporting. Of ''stand-out lawyers'', only about one-third of heavy AI-user partners had discussed
    AI with 60% or more of their clients (TRI-STANDOUT-2026, key takeaways). Partners who use AI daily
    are nine times more likely to report significant efficiency and quality impact than minimal users
    (same source). Thomson Reuters'' speaker said firms with a GenAI strategy are 3.9 times more likely
    to achieve ROI, and only 22% of firms have one (TRI-LEGALWEEK-2026); the TR-FOP date is year-only
    because the page shows no publication date.'
- id: professional-services-client-development-15
  title: 'AI-analysed client listening: feedback, win-loss and matter-close debriefs'
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - client-interaction
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Client feedback programmes are periodic, siloed and hard to analyse; informal feedback in meetings
    and emails goes unrecorded.
  solution: AI themes free-text feedback from interviews, surveys, pitch debriefs and informal comments
    into one view. Shoosmiths announced in May 2023 that it would use MyCustomerLens to centralise feedback
    from departments and offices. Tozers is quoted on MyCustomerLens's home page. Koji offers AI-moderated
    client interviews for client experience, win-loss, matter-close debriefs and, as stated on its page,
    in-house stakeholder feedback.
  outcomes:
  - lever: experience
    description: Efficiencies reported by Shoosmiths, described qualitatively
    figure: none published
    measures: Firm's senior client culture manager cites 'a number of efficiencies' and deeper insight;
      no figure given
    provenance: vendor-published
    source_ref: EDINBURGHNEWS-SHOOSMITHS-2023
  prerequisites:
  - Feedback sources collected in a consistent form
  - A named owner who reports results to senior decision makers (stated by Shoosmiths)
  risks_and_guardrails:
  - A 2024 article quoting the MyCustomerLens CEO cites Thomson Reuters data that only 27% of clients
    had been invited to a feedback programme, and notes surveys suffer confirmation bias (SJ-LISTENING-2024;
    second-hand)
  - UK clients are cautiously accepting of AI for legal research but uneasy about its use in case management
    and administration (SJ-LFMC-2026)
  human_checkpoints:
  - Reports go to senior decision makers who act on them
  role_evolution: A 'senior client culture manager' role exists at Shoosmiths (EDINBURGHNEWS-SHOOSMITHS-2023).
  evidence_grade: C
  sources:
  - ref: EDINBURGHNEWS-SHOOSMITHS-2023
    title: Top legal firm adopts pioneering AI technology to improve client relations
    publisher: Edinburgh News
    type: press
    url: https://www.edinburghnews.scotsman.com/business/top-legal-firm-adopts-pioneering-ai-tech-to-improve-client-relations-4134011
    date: '2023-05-09'
    access: full
    locator: Paragraphs 2-5
  - ref: MCL-SITE-2026
    title: 'MyCustomerLens: client listening platform for professional service firms (home page; read
      2026-10-19, no publication date shown)'
    publisher: MyCustomerLens
    type: vendor
    url: https://www.mycustomerlens.com/
    date: '2026-10-19'
    access: full
    locator: 'Home page: solution description and Tozers quote'
  - ref: KOJI-LEGAL-2026
    title: AI Customer Research for Legal Teams & Law Firms (product documentation; page last modified
      2026-08-19)
    publisher: Koji
    type: vendor
    url: https://www.koji.so/docs/ai-research-for-legal
    date: '2026-08-19'
    access: full
    locator: Sections 'What legal teams can research with Koji' items 1-5
  - ref: SJ-LISTENING-2024
    title: 'Law Firm Operations & Practice Insights: What Clients Really Think (advertorial-style piece
      quoting MyCustomerLens CEO)'
    publisher: Solicitors Journal
    type: press
    url: https://www.solicitorsjournal.com/sjarticle/what-clients-really-think-about-law-firms-is-not-always-recorded-in-surveys
    date: '2024-05-22'
    access: full
    locator: Paragraphs 1-3
  - ref: SJ-LFMC-2026
    title: Clients embracing AI use in law firms (Law Firm Marketing Club survey of 642 UK clients, fielded
      Q4 2025)
    publisher: Solicitors Journal
    type: survey
    url: https://www.solicitorsjournal.com/sjarticle/clients-embracing-ai-use-in-law-firms
    date: '2026-04-10'
    access: full
    locator: Paragraphs 1-2
  last_reviewed: '2026-10-19'
  notes: 'Grade C: the only named deployment is a 2023 announcement with qualitative remarks, and current
    use is not confirmed. MyCustomerLens ''status quo'' statistics on its home page (for example only
    15% of firms have a centralised feedback database) are unsourced vendor claims and were not used.
    BTI''s 2026 Super Listener list (Akin and Carlton Fields named) was seen in search only.'
- id: professional-services-client-development-16
  title: 'Idea (in-house): AI analysis of internal-client feedback and reporting of legal''s value to
    the business'
  archetype: professional-services
  module: client-development
  function: risk-compliance-legal
  work_types:
  - data-reporting
  - client-interaction
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: In-house legal departments say they add value, but 86% of general counsel believe their department
    contributes significantly to organisational objectives against 17% of the C-suite. Feedback from business
    units is ad hoc.
  solution: 'Idea discussed by researchers and a vendor, not a found deployment: systematic stakeholder
    feedback gathered by survey or interview, with AI used to analyse responses, plus outcome-based reporting
    of legal''s work. Thomson Reuters Institute recommends AI fluency and systematic relationship-building;
    Koji''s page lists in-house stakeholder surveys as a use.'
  outcomes:
  - lever: experience
    description: none published
    figure: none published
    measures: No in-house team's measurement found
    provenance: vendor-published
    source_ref: TRI-VISIBILITY-2026
  prerequisites:
  - A feedback framework covering executives and business unit leads
  - AI fluency in the department
  risks_and_guardrails:
  - Two-thirds of GCs say they do not know how their outside firms approach AI, so internal and external
    AI conversations are disconnected (TRI-INTERDEPENDENT-2026)
  human_checkpoints:
  - GC and legal ops leaders decide actions from feedback
  role_evolution: TRI suggests GCs shift from task-based to outcome-focused messaging and richer internal
    relationships.
  evidence_grade: D
  sources:
  - ref: TRI-VISIBILITY-2026
    title: Relationship-building and AI fluency key to closing visibility gap, new report shows (2026
      State of the Corporate Law Department Report)
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/closing-ai-visibility-gap
    date: '2026-04-06'
    access: full
    locator: Opening paragraphs and sections on relationships and AI fluency
  - ref: TRI-INTERDEPENDENT-2026
    title: 'Interdependent by design: The AI conversation law firms and legal departments need to be having
      now'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/needed-ai-conversation
    date: '2026-06-11'
    access: full
    locator: Section 'The AI view from law firms' and the communication-gap paragraph
  - ref: KOJI-LEGAL-2026
    title: AI Customer Research for Legal Teams & Law Firms (product documentation; page last modified
      2026-08-19)
    publisher: Koji
    type: vendor
    url: https://www.koji.so/docs/ai-research-for-legal
    date: '2026-08-19'
    access: full
    locator: Section 5, 'Internal and in-house use'
  last_reviewed: '2026-10-19'
  notes: Idea. In-house. 86% vs 17% = share of general counsel (and of C-suite executives) saying the
    legal department is a significant contributor to organisational objectives, 2026 State of the Corporate
    Law Department Report (more than 2,300 GC interviews). Thomson Reuters Institute's 'Voice of Stakeholder
    Roadmap' (undated PDF, no AI content) covers the non-AI version of this process.
```

---
## 3. Module notes

### Processes and key steps (with work types)

1. **Capture and maintain relationship data** (data-reporting): log contacts, meetings and emails; clean and enrich records. Use case 01.
2. **Map relationships and coverage** (research-synthesis): who knows whom, strength, warm paths, cross-practice gaps, departures and laterals. Use case 02.
3. **Plan key accounts and cross-sell** (coordination-scheduling, expert-judgment): account plans, opportunity matrices. Use case 09.
4. **Prepare for meetings and send outreach** (research-synthesis, document-production, client-interaction): briefs, client notes and alerts, nudges. Use cases 03, 07, 08.
5. **Identify new opportunities** (research-synthesis): signals from courts, news, filings and internal data. Use case 06.
6. **Hold AI value conversations with clients** (client-interaction, expert-judgment): disclose AI use, show savings, agree how value is shared. Use cases 11, 13, 14.
7. **Listen to clients and act on retention risk** (data-reporting): feedback, win-loss, matter-close debriefs, health alerts. Use cases 04, 15.
8. **Measure BD return** (data-reporting): attribution of mandates to relationships. Use case 10.
9. **Offer AI to clients as an asset** (client-interaction): portals, subscription tools, client labs. Use cases 11, 12.

### Common pain points

- CRMs lack data because professionals do not enter it; the Introhive CEO calls law-firm CRM adoption 'negligible' (INTROHIVE-LAWSITES-2026).
- Relationship visibility exists but is hard to act on (78% of 123 partners) and 70% say leadership lacks visibility into relationship capital (INTROHIVE-PARTNER-2026).
- Partners' main BD frictions: knowing where to focus (50%), making time (45%), identifying cross-sell (43%) (INTROHIVE-LAWSITES-2026).
- Strategy does not reach partners: 36% of stand-out lawyers strongly agree their firm has a clear AI strategy and 25% strongly agree it has a plan to monetise AI use (TRI-STANDOUT-2026).
- Clients send contradictory messages (use AI, do not use it without permission, will not pay for AI-done tasks) (TRI-LEGALWEEK-2026).
- In-house (tag: in-house): 86% of general counsel say their department is a significant contributor to organisational objectives against 17% of the C-suite (TRI-VISIBILITY-2026); two-thirds of GCs do not know how their outside firms approach AI (TRI-INTERDEPENDENT-2026).

### Metrics and benchmarks (with sources)

| Metric | Figure | Measures (source's words) | Provenance | Source |
|---|---|---|---|---|
| Structured or AI-driven BD today | 41% now; 84% expect within 18-24 months | Respondents saying their firm runs structured or AI-driven BD programmes; n=123 partners (42 legal, 42 accounting, 39 other) | vendor-published (conducted by Thinktiv for Introhive) | INTROHIVE-PARTNER-2026; INTROHIVE-LAWSITES-2026 |
| BD maturity | 57% at stage 1 or 2 | Partners placing their firm at basic data or relationship visibility | vendor-published | INTROHIVE-LAWSITES-2026 |
| AI tools used for BD | 68% of those using AI use only general-purpose tools; satisfaction 6.7 out of 10 | Respondents actively using AI for BD | vendor-published | INTROHIVE-PARTNER-2026 |
| BD ROI measurement | 63% no revenue-linked measure; 15% strong attribution | Firms, as reported by partners | vendor-published | INTROHIVE-LAWSITES-2026 |
| Client value of AI | 78% very important or essential; 6% say most or all providers deliver; 32% reconsidering | Corporate clients who buy professional services; client subset size not stated | vendor-published (Thomson Reuters Institute) | TR-FOP-2026 |
| AI conversations with clients | About one-third of heavy-AI-user partners discussed AI with 60%+ of clients; more than one-third of stand-out lawyers with fewer than 20% | Stand-out lawyers named by clients; 116 firm-leader interviews and 2,527 lawyer interviews | vendor-published (Thomson Reuters Institute) | TRI-STANDOUT-2026 |
| Strategy and ROI | Firms with a GenAI strategy 3.9 times more likely to achieve ROI; 22% have one | Stated by a Thomson Reuters speaker at Legalweek | vendor-published | TRI-LEGALWEEK-2026 |
| Firms should start AI talks | 77% of respondents | Respondents to the 2026 AI in Professional Services Report (second-hand; report not opened) | vendor-published | TRI-CMBDO-2026 |
| Account connectivity (single firm) | 47 to 97 employees connected to Top 50 accounts | Case study label | vendor-published | INTROHIVE-TSP-2026 |

**Quality evidence.** None found: no error rates, override or correction rates, parallel-run results or independent measurement for any client-development tool. All outcome figures are vendor-published or self-reported. The only third-party-style study (Forrester Consulting for Introhive, 495% ROI for a composite organisation) is vendor-commissioned and was seen as a landing page, not the study itself.

### Guardrails and regulatory points

- Ethical walls and need-to-know rules must apply to AI that reads relationship and matter data; Intapp says Celeste applies the same restrictions and keeps an action record (LAWSITES-CELESTE-2026). Introhive's MCP access follows each user's permissions (INTROHIVE-LAWSITES-2026).
- Accuracy of automated CRM data and outreach prompts (INTROHIVE-LAWSITES-2026).
- Billing and client disclosure: the landscape file records California State Bar guidance on agentic AI covering real-time billing and disclosure of AI costs (CALBAR-GENAI-2026, not re-opened here).
- Privacy and lawful basis for capturing email and calendar contact data: not addressed in the sources read.
- Client AI instructions and warranties arrive in the same inbox with opposite demands (TRI-LEGALWEEK-2026).

### Frontier signals (dated and sourced)

- **2026-10-13**: Introhive publishes a Model Context Protocol server so assistants such as Claude, Harvey, ChatGPT and Copilot can query a firm's relationship data under existing permissions (INTROHIVE-LAWSITES-2026).
- **2026-10-13**: Legora and Laurel announce automatic time capture from Legora work and joint development of measures of AI usage and value (LEGORA-LAUREL-2026).
- **2026-10-05**: Akin Gump describes Moneyball, an in-house BD intelligence tool (AKIN-MONEYBALL-2026).
- **2026-09-10**: Parker Poe runs a client AI lab; it cites a similar lab with Fasken (PARKERPOE-LAWSITES-2026).
- **2026-07-15**: Intapp makes Celeste generally available with BD playbooks (LAWSITES-CELESTE-2026).
- **2026-07-14**: ABA Journal, citing Law.com, reports firms sharing built AI tools with clients and peers (ABAJ-SHARE-2026).
- **2026-08-06**: Thomson Reuters Institute reports firm leaders say client pressure has reversed from 'do not use AI' to 'show us your AI' (TRI-STANDOUT-2026).
- **2026-02-18**: CMBDO Forum panelists call BD an ideal starting point for agentic AI (TRI-CMBDO-2026).

### Workforce and role effects

- New hybrid roles: Latham's Innovation Attorney for client team enablement; Akin Gump's senior director of marketing and client intelligence; Greenberg Traurig's chief pricing and innovation officer (LATHAM-INNOVATIONATTY-2026; AKIN-MONEYBALL-2026; TRI-LEGALWEEK-2026).
- Partners are the 'commercial transmission mechanism': partners who use AI daily are nine times more likely to report significant efficiency and quality impact than minimal users, and those who do not use it cannot speak to clients about it (TRI-STANDOUT-2026).
- Training: panelists say bespoke, one-to-one training before client meetings beats broad sessions (TRI-CMBDO-2026).
- AI purchasing in firms is often run by IT or innovation groups, not BD and marketing, the Introhive CEO says (INTROHIVE-LAWSITES-2026).

### Objections and concerns practitioners raise

- 'My relationship produced the business, not your data': attribution is contested (INTROHIVE-LAWSITES-2026).
- Fear that clients can do the work themselves or that sharing tools gives away the firm's 'secret sauce' (ABAJ-SHARE-2026).
- Leading with price concessions trains clients to expect discounts (TRI-STANDOUT-2026).
- Agents are limited by the data and tools they are given; leaders may over-credit them (TRI-CMBDO-2026).
- General-purpose chatbots cannot see firm relationship data (INTROHIVE-PARTNER-2026).

### Interview probes for an advisor

1. Where does relationship data live today, and what share of client meetings and emails reach the CRM without anyone typing?
2. Before your last three key-client meetings, who prepared the brief, how long did it take, and did the partner use it?
3. When a client last asked how you use AI on their matters, who answered, and what evidence could you show per matter?
4. How do you know whether a relationship tool led to a cross-sell, a retained client or a win, and who accepts that attribution?
5. (In-house) How do business leaders rate your department, and what do you report to them that they can see?

---

## 4. Routed to other modules

| Item | Target module | Why |
|---|---|---|
| Lynn Pinker Hurst & Schwegmann used Harvey to answer an urgent prospect request in under 48 hours and won the business (HARVEY-LPHS-2025, vendor customer story, 2025-04-24; also described in HARVEY-BD-2026) | pursuit-proposals | Proposal and pitch response speed |
| Harvey's mining of firm experience and prior pitches for tailored pitches and RFP drafting (HARVEY-BD-2026) | pursuit-proposals | Document work for pursuits |
| Latham role supports panels, pitches and RFPs on technology (LATHAM-INNOVATIONATTY-2026) | pursuit-proposals | Technology content in pitches |
| Source Global Research buyer segmentation: C-suite, finance and IT buyers want different AI help; 60% of enterprise tech buyers cite data quality and governance as the largest bottleneck (SOURCE-INSIGHTS-2026) | pursuit-proposals | Buyer research for bids; also context for key-account targeting here |
| Celeste at BakerHostetler for intake and conflicts; lateral hiring lifecycle (LAWSITES-CELESTE-2026); Practus/Auxana Intake and Conflicts (INTAPP-PRACTUS-2026) | acceptance-risk | Intake and conflicts, not client development |
| Legora-Laurel automatic time entries and AI-ROI measurement (LEGORA-LAUREL-2026) | billing-collections (time capture) and firm-finance (AI ROI) | Time-to-cash and firm AI investment measurement |
| AI-related fee discussions: line-item AI billing, clients refusing to pay for AI-done tasks, 'services rendered' billing (TRI-LEGALWEEK-2026) | scoping-pricing | Pricing and fee design |
| Productised client tools, subscription platforms and revenue-sharing licences (Debevoise STAAR, Cooley GO Lab, A&O Shearman with Harvey) (ABAJ-SHARE-2026) | scoping-pricing (and the service model) | New service and revenue model; use case 12 here covers only the relationship effect |
| Client AI risk questions: Baker McKenzie Client AI Risk Lead (BAKERMCKENZIE-CLIENTAIRISK-2026, search-only) | acceptance-risk | Client AI terms and risk |
| Latham's capability catalogue for client AI work (LATHAM-INNOVATIONATTY-2026) | knowledge-management | Capability library |
| Partner and associate AI training (TRI-CMBDO-2026; TRI-STANDOUT-2026) | talent-learning | Training and adoption |

---

## 5. Sources

Access: full means opened and read; search-only means known only from a search summary. Dates are publication dates unless the title says read date or modified date. The `in-house` tag applies to TRI-VISIBILITY-2026, TRI-INTERDEPENDENT-2026 and the in-house section of KOJI-LEGAL-2026.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ABAJ-SHARE-2026 | Should law firms share AI tools with their clients and peers? | ABA Journal | press | https://www.abajournal.com/news/article/should-law-firms-share-ai-tools-with-their-clients-and-peers | 2026-07-14 | full |
| AKIN-MONEYBALL-2026 | The Lawyer Highlights How Akin's AI Tool 'Moneyball' is Advancing Client Development | Akin Gump Strauss Hauer & Feld LLP (firm news item summarising The Lawyer) | firm | https://www.akingump.com/en/insights/media-mentions/the-lawyer-highlights-how-akins-ai-tool-moneyball-is-advancing-client-development | 2026-10-05 | full |
| BAKERMCKENZIE-CLIENTAIRISK-2026 | Job posting: Client AI Risk Lead (page not found when opened; known only from a search summary) | Baker McKenzie | job-posting | https://careers.bakermckenzie.com/es_ES/opportunities/JobDetail?jobId=2759 | 2026 | search-only |
| BRIDGENEXT-AGENTFORCE-2026 | Global Risk Assessment Firm Accelerates Sales Preparation by 30-50% with Agentforce (implementation-partner case study; client is a financial-services data and risk firm, not a professional-services firm) | Bridgenext | vendor | https://www.bridgenext.com/our-work/success-stories/ai-sales-acceleration-with-salesforce-agentforce/ | 2026-08-12 | full |
| BTI-SUPERLISTENER-2026 | Carlton Fields named to BTI 2026 Super Listener A-Team (page blocked; known only from a search summary) | Carlton Fields | firm | https://www.carltonfields.com/newsroom/news/2026/carlton-fields-named-to-bti-2026-super-listener-a-team | 2026 | search-only |
| COOLEY-LAWCOM-2026 | Law Firms Are Building Their Own AI Tools. Should They Share Them? (press-mention page; Law.com article is subscription only) | Cooley LLP | firm | https://www.cooley.com/news/coverage/2026/2026-07-14-law-firms-are-building-their-own-ai-tools-should-they-share-them | 2026-07-14 | full |
| DEBEVOISE-BLOOMBERG-2026 | Bloomberg Law Features Debevoise's AI Strategy and STAAR Platform | Debevoise & Plimpton LLP | firm | https://www.debevoise.com/news/2026/08/bloomberg-law-features-debevoises-ai | 2026-08-06 | full |
| EDINBURGHNEWS-SHOOSMITHS-2023 | Top legal firm adopts pioneering AI technology to improve client relations | Edinburgh News | press | https://www.edinburghnews.scotsman.com/business/top-legal-firm-adopts-pioneering-ai-tech-to-improve-client-relations-4134011 | 2023-05-09 | full |
| HARVEY-BD-2026 | How Law Firms Use AI for Business Development and Client Intelligence | Harvey | vendor | https://www.harvey.ai/blog/ai-for-law-firm-business-development | 2026-06-23 | full |
| HARVEY-LPHS-2025 | Sharpening the Edge: How LPHS Uses Harvey to Win Smarter, Faster (customer story) | Harvey | vendor | https://www.harvey.ai/customers/lphs | 2025-04-24 | full |
| INTAPP-ACTIVATOR-2026 | Intapp DealCloud Activator (product page; read 2026-10-19, no publication date shown) | Intapp | vendor | https://www.intapp.com/legal/activator/ | 2026-10-19 | full |
| INTAPP-DEALCLOUD-2026 | The AI-powered deal and relationship intelligence platform (Intapp DealCloud product page; read 2026-10-19, no publication date shown) | Intapp | vendor | https://www.intapp.com/dealcloud/ | 2026-10-19 | full |
| INTAPP-FORVISMAZARS-2026 | Forvis Mazars Capital Advisors selects Intapp DealCloud with Celeste to advance firmwide agentic AI strategy (press release) | Intapp | vendor | https://www.intapp.com/news/forvis-mazars-intapp-celeste/ | 2026-09-22 | full |
| INTAPP-HOWESPERCIVAL-2025 | Howes Percival uses Intapp DealCloud as its all-in-one platform for CRM, relationship intelligence and email marketing (client story) | Intapp | vendor | https://www.intapp.com/case-study/howes-percival-dealcloud/ | 2025-02-24 | full |
| INTAPP-PRACTUS-2026 | Practus LLP deploys Intapp's agentic AI solutions to power innovation and growth (press release, Business Wire copy) | Intapp via Business Wire | vendor | https://finviz.com/news/387470/practus-llp-deploys-intapps-agentic-ai-solutions-to-power-innovation-and-growth | 2026-09-01 | full |
| INTAPP-Q3CALL-2026 | Intapp (INTA) Q3 fiscal 2026 earnings call transcript (call held 2026-05-05; transcript published 2026-05-06) | The Motley Fool via Yahoo Finance | vendor | https://finance.yahoo.com/markets/stocks/articles/intapp-inta-q3-2026-earnings-151600418.html | 2026-05-05 | full |
| INTAPP-WOTTONKEARNEY-2026 | Wotton Kearney selects Intapp DealCloud with Celeste to power relationship intelligence and AI-driven growth (press release) | Intapp | vendor | https://www.intapp.com/news/wotton-kearney-intapp-celeste/ | 2026-07-09 | full |
| INTROHIVE-FORRESTER-2024 | The Forrester Total Economic Impact Study for Introhive's Customer Intelligence Platform (landing page; modified 2026-03-11) | Introhive (study commissioned from Forrester Consulting) | vendor | https://www.introhive.com/resource/whitepaper/the-forrester-total-economic-impact-study/ | 2024-08-02 | full |
| INTROHIVE-GRASSI-2026 | Grassi Strengthens Client Engagement with Introhive (client story) | Introhive | vendor | https://www.introhive.com/resource/client-story/grassi-strengthening-client-engagement-with-introhive/ | 2026-03-02 | full |
| INTROHIVE-KSM-2026 | KSM Lays the Groundwork for CRM Adoption with Introhive (client story) | Introhive | vendor | https://www.introhive.com/resource/client-story/ksm-lays-the-groundwork-for-crm-adoption-with-introhive/ | 2026-06-11 | full |
| INTROHIVE-LAINGOROURKE-2025 | Laing O'Rourke: Building Trust with Salesforce & Introhive (client story) | Introhive | vendor | https://www.introhive.com/resource/client-story/laing-orourke-case-study-introhive-salesforce/ | 2025-07-10 | full |
| INTROHIVE-LAWSITES-2026 | Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds | LawSites (Robert J. Ambrogi) | press | https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html | 2026-10-13 | full |
| INTROHIVE-LBMC-2024 | LBMC Achieves 567% ROI in Their First Step Into Digital Transformation with Introhive (client story; page modified 2026-06-22) | Introhive | vendor | https://www.introhive.com/resource/client-story/lbmc/ | 2024-07-24 | full |
| INTROHIVE-PARTNER-2026 | AI Without Relationship Context Won't Deliver BD ROI, Introhive's 2026 Partner Survey Report Finds | Introhive | vendor | https://www.introhive.com/news/ai-without-relationship-context-wont-deliver-bd-roi-introhives-2026-partner-survey-report-finds/ | 2026-10-13 | full |
| INTROHIVE-SAM-2025 | Strategic Account Management Framework (guide landing page) | Introhive | vendor | https://www.introhive.com/resource/whitepaper/strategic-account-management-framework/ | 2025-11-06 | full |
| INTROHIVE-SCHNEIDERDOWNS-2026 | Schneider Downs Builds a Stronger Relationship Database with Introhive (client story) | Introhive | vendor | https://www.introhive.com/resource/client-story/schneider-downs-building-a-stronger-relationship-database-with-introhive/ | 2026-03-31 | full |
| INTROHIVE-TSP-2026 | Thomson Snell & Passmore Doubles Firm-Wide Account Connectivity with Introhive (client story) | Introhive | vendor | https://www.introhive.com/resource/client-story/thomson-snell-passmore-law-firm-relationship-intelligence/ | 2026-08-05 | full |
| KOJI-LEGAL-2026 | AI Customer Research for Legal Teams & Law Firms (product documentation; page last modified 2026-08-19) | Koji | vendor | https://www.koji.so/docs/ai-research-for-legal | 2026-08-19 | full |
| LATHAM-ADAI-2026 | Job posting: Associate Director of AI & Innovation - Client Services (page returned HTTP 410 when opened; known only from a search summary) | Latham & Watkins LLP | job-posting | https://careers-lw.icims.com/jobs/6958/associate-director-of-ai-%26-innovation-%e2%80%93-client-services/job | 2026 | search-only |
| LATHAM-INNOVATIONATTY-2026 | Job description: Innovation Attorney - Client Team Enablement (last updated 2026-02-26) | Latham & Watkins LLP | job-posting | https://www.lw.com/admin/upload/SiteAttachments/Innovation-Attorney-Client-Team-Enablement.pdf | 2026-02-26 | full |
| LAWSITES-CELESTE-2026 | Intapp Makes Celeste Generally Available, Calling It An 'AI Coworker' To Run the Business Side of Law Firms | LawSites (Robert J. Ambrogi) | press | https://www.lawnext.com/2026/07/intapp-makes-celeste-generally-available-calling-it-an-ai-coworker-to-run-the-business-side-of-law-firms.html | 2026-07-16 | full |
| LEGORA-LAUREL-2026 | Legora and Laurel partner to capture the time lawyers spend in Legora as they work | Legora | vendor | https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work | 2026-10-13 | full |
| LEGORA-PORTAL-2026 | Portal: the new standard in legal collaboration (product page; read 2026-10-19, no publication date shown) | Legora | vendor | https://legora.com/product/portal | 2026-10-19 | full |
| MCL-SITE-2026 | MyCustomerLens: client listening platform for professional service firms (home page; read 2026-10-19, no publication date shown) | MyCustomerLens | vendor | https://www.mycustomerlens.com/ | 2026-10-19 | full |
| PARKERPOE-LAWSITES-2026 | Parker Poe Clients & Attorneys Build AI Assistants Together to Help Deliver Better Outcomes (firm press release carried by LawSites) | LawSites (Robert J. Ambrogi); release by Parker Poe Adams & Bernstein LLP dated 2026-09-11 | press | https://www.lawnext.com/2026/09/parker-poe-clients-attorneys-build-ai-assistants-together-to-help-deliver-better-outcomes.html | 2026-09-16 | full |
| SJ-LFMC-2026 | Clients embracing AI use in law firms (Law Firm Marketing Club survey of 642 UK clients, fielded Q4 2025) | Solicitors Journal | survey | https://www.solicitorsjournal.com/sjarticle/clients-embracing-ai-use-in-law-firms | 2026-04-10 | full |
| SJ-LISTENING-2024 | Law Firm Operations & Practice Insights: What Clients Really Think (advertorial-style piece quoting MyCustomerLens CEO) | Solicitors Journal | press | https://www.solicitorsjournal.com/sjarticle/what-clients-really-think-about-law-firms-is-not-always-recorded-in-surveys | 2024-05-22 | full |
| SOURCE-INSIGHTS-2026 | Precision segmentation: How consulting firms can target clients' sector and functional AI budgets | Source Global Research | survey | https://sourceglobalresearch.com/market-update/precision-segmentation-how-consulting-firms-can-target-clients-sector-and-functional-ai-budgets | 2026-09-28 | full |
| THELAWYER-AKIN-2026 | Curve: How Akin's new AI tool helps generate business leads (blocked by a bot check; known through the Akin summary) | The Lawyer | press | https://www.thelawyer.com/curve-how-akins-new-ai-tool-helps-generate-business-leads/ | 2026-10 | search-only |
| TR-FOP-2026 | Future of Professionals Report 2026 (survey of 1,816 professionals fielded March-April 2026; page shows no publication date) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 | full |
| TR-NAVIGATING-2026 | Navigating New Waters: Using AI for Tailored Client Journeys (panel slides: Equinox Strategy Partners, Quinn Emanuel, MyMai, Willkie Farr & Gallagher) | Thomson Reuters (event slide deck) | conference | https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2025/01/Navigating-New-Waters.pdf | 2026-01-21 | full |
| TRI-CMBDO-2026 | Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI may be talking to your clients about it | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai | 2026-02-18 | full |
| TRI-INTERDEPENDENT-2026 | Interdependent by design: The AI conversation law firms and legal departments need to be having now | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/needed-ai-conversation | 2026-06-11 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 | full |
| TRI-VISIBILITY-2026 | Relationship-building and AI fluency key to closing visibility gap, new report shows (2026 State of the Corporate Law Department Report) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/closing-ai-visibility-gap | 2026-04-06 | full |
| WOLFGREENFIELD-2026 | Job posting: Manager of Legal Technology Engagement (page blocked; known only from a search summary that gave 'August 2026') | Wolf Greenfield via GoParalegals | job-posting | https://www.goparalegals.com/jobs/572837999-manager-of-legal-technology-engagement-at-wolf-greenfield | 2026-08 | search-only |

---

## 6. Gaps

- **Search budget.** Nine web searches were used; two further searches (accounting-firm BD, consulting-firm account intelligence) were refused because the shared search budget ran out. Accounting and consulting coverage is therefore thin.
- **No consulting or Big Four account-management evidence.** No public deployment of AI for account planning or client relationship management at Deloitte, EY, KPMG, PwC, BCG, McKinsey, Bain or Accenture was found. Intapp's DealCloud pages show their logos but no use detail.
- **No independent quality or outcome evidence.** No error rates, override rates, parallel-run results, retention or revenue outcomes. All figures are vendor-published or self-reported. Grade A was not reachable for any use case.
- **Blocked or unreadable pages.** The Lawyer's article on Akin's Moneyball (bot check; Akin's own summary was read), Debevoise's linked Bloomberg Law article, Law.com articles on firm tool sharing (subscription), Stanford Generative Legal 2026 client panel (Cloudflare), Carlton Fields BTI release (Cloudflare), Fenwick media page (access denied), Wolf Greenfield job posting (bot check), Latham's Associate Director posting (HTTP 410), Baker McKenzie posting (page not found), Intapp.com directly (403; read through a text mirror).
- **Not opened.** The Thomson Reuters Institute 2026 AI in Professional Services Report (the 77% figure is second-hand), the Forrester Total Economic Impact study itself, Introhive's 2026 partner report PDF (summaries read), Intapp's Ropes & Gray announcement (referenced only via the earnings call), Karbon's State of AI in Accounting report (page was script-rendered), Salesforce and Gong product documentation for professional-services customers.
- **Dates.** TR-FOP-2026 shows no publication date (survey fielded March-April 2026), so a year-only date is used. Older Introhive stories (Frazier & Deeter, Gould & Ratner, Colliers, Grant Thornton Australia, CLA, Wilson Sonsini) carry 2024 site dates, were read, and were not relied on. Gerald Edelman and FMI Capital Advisors DealCloud stories (2021) were read as background only.
- **Under-documented.** Privacy and lawful-basis rules for automated contact capture; how relationship tools handle ethical walls in practice; independent evidence on whether AI-prepared briefs change client outcomes; in-house legal teams using AI on stakeholder feedback (only an idea found); firm-level evidence outside the US and UK.
- **Caution on specific claims.** The Grassi case study shows two different meeting counts (253k in the header, 53,000 in the impact panel); neither is used. The '97% data accuracy' and '495% ROI' figures are unnamed or composite and vendor-commissioned. Intapp's 'up to 32%' figure refers to Activator behaviours studied by DCM Insights, not to the tool's own effect.

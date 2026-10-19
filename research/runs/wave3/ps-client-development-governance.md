# Client development: governance angle (professional services)

Module `client-development` (key-account and client relationship management: relationship intelligence, account plans, AI value conversations with clients, client feedback and retention). Angle: governance and evidence (what constrains and measures the work). Prepared 2026-10-19. Archetype: professional-services. Public sources only. Quotations are under 25 words.

## 1. Summary

**Counts.** 16 candidate use cases: grade A 0, grade B 3, grade C 10, grade D 3 (labelled ideas). 40 sources opened and read in full (some through mirrors or summaries, marked in section 5), plus 3 search-only items. Types read: professional-body 14, survey 6, academic 5, press 4, vendor 4, regulator 3, firm 2, conference 2.

**What the governance and evidence record says**

- **The rules constrain how the work is done more than whether it is done.** US and UK professional-body guidance allows AI in client development, with conditions. California's 2026 revision says a lawyer must not let an agentic system send client information outside the firm without safeguards and human review (CALBAR-GENAI-2026, pp. 5-6). Oregon's February 2026 opinion allows intake and marketing chatbots, "qualified", and asks for monitoring, disclaimers and lawyer approval of autonomous actions (OSB-FO-2026-208, sections III.A-III.D). The ICMCI AI code for management consultants (May 2026) names marketing and business development as in scope and says consultants must not overstate AI expertise in proposals, marketing or client discussions (ICMCI-AICODE-2026, sections 1.1 and 11.2).
- **Client AI terms are now a relationship variable.** ABA Opinion 512, as summarised by law-firm and bar-body write-ups, requires firms to follow disclosure requirements in engagement agreements and outside counsel guidelines and to consult clients when AI use bears on fees (FMG-ABA512-2024). In ILTA's 2026 survey, the share of firms whose policy says client approval must be obtained ranges from 8% (under 50 lawyers) to 38% (350 to 699 lawyers) (ILTA-TECHSURVEY-2026, Q3.18). In-house advisers now recommend an AI addendum to outside counsel guidelines as a condition of engagement (LOUBAR-2025, Tip 1; CONVENTUS-2026).
- **Clients want proof; firms cannot yet give it.** 78% of corporate clients say AI-enabled quality improvements are very important or essential, and 6% say most or all of their providers deliver them; 32% are reconsidering relationships or plan to within 12 months (TR-FOP-2026, key finding 02). At Legalweek 2026, firm speakers said they were still gathering savings data (TRI-LEGALWEEK-2026). In the ACC/Everlaw survey of in-house professionals, 59% report no GenAI savings from their law firms yet (EVERLAW-ACC-PR-2025).
- **Partners are not having the AI conversation, and the data under relationship tools is weak.** More than one-third of stand-out lawyers say they have talked about AI with fewer than 20% of their clients (TRI-STANDOUT-2026). In a vendor-commissioned survey of 123 partners, 78% say relationship data is hard to act on and 63% of firms have no revenue-linked way to measure BD return (INTROHIVE-LAWSITES-2026).
- **There is no independent measurement of AI in client development.** Every figure on relationship intelligence outcomes is vendor-published and has no stated baseline or cohort. The nearest randomised evidence is adjacent: retail sales and customer-service field experiments (FANG-ARXIV-2026) and a patent-drafting trial (NBER-AUTOR-2026). That is why no entry is graded A.

**Two most important insights**

1. **The disclosure duty and the trust penalty point in opposite directions.** Bar guidance pushes firms toward telling clients about material AI use, while a 13-experiment study finds that people who disclose AI use are trusted less, and that being found out later is worse (SCHILKE-OBHDP-2025; SCHILKE-CONVERSATION-2025). The practical design question is how to disclose, not whether.
2. **Client development is where autonomy limits bite first.** Intake chatbots, outbound sequences and relationship agents reach people outside the client relationship. Regulators single out exactly those steps (inadvertent client formation, misleading statements, autonomous external transmission, recording consent), so human approval gates are a precondition, not an option.

---

## 2. Use cases

Single YAML block. Ids follow `professional-services-client-development-NN`. Grade D entries are labelled ideas. In-house examples are tagged `in-house` in `notes`. Provenance and locators are recorded per outcome and source. TRI (Thomson Reuters Institute) figures are marked `vendor-published` because the publisher is the research arm of a legal-technology vendor.

```yaml
- id: professional-services-client-development-01
  title: Relationship mapping and warm-path finding from email and calendar metadata across the firm
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [data-reporting, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Partners hold client relationships in their heads and inboxes. CRM records depend on manual entry that partners rarely do, so the firm cannot see who knows whom or where a warm introduction exists."
  solution: "A relationship-intelligence platform captures contact and meeting metadata from email and calendars, builds a map of firm relationships and strength, and exposes it to partners and, through an MCP server, to AI assistants the firm already uses, subject to each user's existing permissions."
  outcomes:
    - { lever: growth, description: "Vendor-reported increases in internal referrals and cross-sell revenue, and in win rates", figure: "30% increase in internal referrals and cross-sell revenue; 36% increase in win rates", measures: "The page gives no cohort, baseline, period or number of firms for either figure", provenance: vendor-published, source_ref: INTROHIVE-HOME-2026 }
    - { lever: quality, description: "Vendor-reported data accuracy of the enrichment service", figure: "90%", measures: "Page says 'data accuracy of 90% across a wide range of clients'; what is checked against what is not defined", provenance: vendor-published, source_ref: INTROHIVE-HOME-2026 }
    - { lever: experience, description: "Partners say relationship data at their firms is hard to act on", figure: "78%", measures: "Share of 123 surveyed partners at law, accounting and other firms who say relationship data at their firms is hard to act on", provenance: vendor-published, source_ref: INTROHIVE-LAWSITES-2026 }
  prerequisites:
    - "Accurate contact data. Introhive's CEO said that once outreach is automated the data has to be accurate, unlike the older tolerance for some bounce-backs on a card list (INTROHIVE-LAWSITES-2026, section 'A New Interface for An Old Problem')"
    - "Privacy settings the firm controls: the vendor says its platform processes email metadata only, and users can set deny lists and subject-line keywords such as 'confidential' or 'privileged' that block processing (INTROHIVE-PRIVACY-2024)"
    - "A permissions model for AI access to relationship data. LawSites reports that the MCP server works subject to each user's existing permissions and firm governance policies (INTROHIVE-LAWSITES-2026, section 'MCP and Agnostic Access to Data')"
  risks_and_guardrails:
    - "Persistent access to email and client files raises acute confidentiality questions, and a lawyer must limit the scope of such access and keep monitoring and access controls in place (CALBAR-GENAI-2026, p. 6)"
    - "Confidentiality duties extend to prospective and former clients (Model Rules 1.18(b) and 1.9(c)), per ABA Opinion 512 as summarised (FMG-ABA512-2024, 'Confidentiality')"
    - "ABA Opinion 512, as quoted by an in-house adviser, warns that even tools siloed within a firm may expose information to people behind an ethical wall (LOUBAR-2025, Tip 3)"
    - "The vendor states that its platform follows GDPR, PIPEDA and CCPA and holds an annual SOC 2 Type II audit; this is a vendor statement and was not independently verified (INTROHIVE-PRIVACY-2024)"
  human_checkpoints:
    - "The partner decides whether and how to act on a suggested path or contact"
    - "Users or administrators set deny lists and keyword exclusions before data is processed"
  role_evolution: "Introhive's CEO described CRM adoption at law firms as 'negligible' and said AI can act as the interface that prompts a lawyer to act, rather than asking the lawyer to log in (INTROHIVE-LAWSITES-2026, section 'A New Interface for An Old Problem')."
  evidence_grade: C
  sources:
    - { ref: INTROHIVE-HOME-2026, title: "Relationship Intelligence Platform (home page)", publisher: "Introhive", type: vendor, url: "https://www.introhive.com/", date: 2026-09-27, access: full, locator: "section 'What can Relationship Intelligence do for your firm?'; date is the page's last-modified date" }
    - { ref: INTROHIVE-PRIVACY-2024, title: "Ensuring Robust Corporate Data Privacy vs. Data Security", publisher: "Introhive (General Counsel)", type: vendor, url: "https://www.introhive.com/data-privacy/", date: 2024-05-15, access: full, locator: "sections on privacy features and requirements" }
    - { ref: INTROHIVE-LAWSITES-2026, title: "Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds", publisher: "LawSites (Bob Ambrogi)", type: press, url: "https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html", date: 2026-10-13, access: full, locator: "opening paragraphs; 'A New Interface for An Old Problem'; 'MCP and Agnostic Access to Data'" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)", publisher: "State Bar of California, COPRAC", type: professional-body, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "p. 6 (Confidentiality, agentic systems)" }
    - { ref: FMG-ABA512-2024, title: "ABA Issues Formal Guidance for Lawyers' Use of Generative AI", publisher: "FMG Law (Sunshine R. Fellows)", type: firm, url: "https://www.fmglaw.com/professional-liability/aba-issues-formal-guidance-for-lawyers-use-of-generative-ai/", date: 2024-08-14, access: full, locator: "'Confidentiality' paragraph" }
    - { ref: LOUBAR-2025, title: "Navigating AI with Outside Counsel: Practical Tips for In-House Counsel", publisher: "Louisville Bar Association, Bar Briefs (Crosby and Lavanga)", type: professional-body, url: "https://www.loubar.org/wp-content/uploads/2025/12/Bar-Briefs_December25_Navigating-AI-with-Outside-Counsel_Crosby-and-Lavanga-1.pdf", date: 2025-12, access: full, locator: "Tip 3 (Protect Confidentiality)" }
  last_reviewed: 2026-10-19
  notes: "Customer deployments are covered in the practice-angle file for this module; this entry grades only the governance and measurement evidence. The two vendor figures have no denominators on the source page, so they are recorded as claims. Dates: the LawSites survey was released 2026-10-13; the Introhive home page date is the last-modified date."

- id: professional-services-client-development-02
  title: Cross-sell and expansion opportunity surfacing from relationship and engagement data, with independence and conflict checks
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [research-synthesis, data-reporting]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Partners know cross-selling is a main source of growth but do not know where to focus BD time. Services sold to one client can also be restricted by independence or conflict rules."
  solution: "AI combines relationship data, engagement history and client news to list clients to contact and produce an opportunity matrix of the client's needs against the firm's capabilities, which partners use as a starting point for conversations."
  outcomes:
    - { lever: growth, description: "Partners ranked cross-sell opportunities as the top benefit of combining information across the firm", figure: "54%", measures: "Share of 123 surveyed partners who ranked cross-sell opportunities at the top when asked what they would most value from combining information across the firm (the source does not say whether more than one answer was allowed)", provenance: vendor-published, source_ref: INTROHIVE-LAWSITES-2026 }
    - { lever: growth, description: "Partners said cross-sell and expansion revenue would be the most convincing proof of BD value", figure: "44%", measures: "Share of surveyed partners naming cross-sell and expansion revenue as the most convincing proof of BD value", provenance: vendor-published, source_ref: INTROHIVE-LAWSITES-2026 }
  prerequisites:
    - "Relationship and engagement data that is accurate and visible across practices (see 01)"
    - "Partner training on using AI-generated briefs as a foundation rather than a script (TRI-CMBDO-2026)"
  risks_and_guardrails:
    - "For CPA firms, AI-related nonattest services such as developing or hosting an AI system for an attest client can raise independence concerns, and the existing nonattest and information-systems rules still apply (JOA-ETHICS-2026)"
    - "Panelists at the TRI forum warned that AI-generated briefs and opportunity matrices should guide lawyers, not replace judgment (TRI-CMBDO-2026)"
    - "Confidentiality duties extend to prospective and former clients under Model Rules 1.18(b) and 1.9(c), per ABA Opinion 512 as summarised (FMG-ABA512-2024, 'Confidentiality')"
  human_checkpoints:
    - "Partner reviews each suggested opportunity before outreach"
    - "Independence and conflict check by risk or ethics staff before a new service is proposed to an existing attest or adverse-sensitive client"
  role_evolution: "BD professionals curate opportunity lists and conversation openers; partners interpret and personalise. Panelists said AI may get 90% of the way and the last 10% depends on judgment and relationship skills (TRI-CMBDO-2026)."
  evidence_grade: C
  sources:
    - { ref: INTROHIVE-LAWSITES-2026, title: "Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds", publisher: "LawSites (Bob Ambrogi)", type: press, url: "https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html", date: 2026-10-13, access: full, locator: "sections 'What Partners Say They Want' and 'Measuring Return'" }
    - { ref: TRI-CMBDO-2026, title: "Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI may be talking to your clients about it", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai", date: 2026-02-18, access: full, locator: "paragraphs on opportunity matrix and training" }
    - { ref: JOA-ETHICS-2026, title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division staff)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: 2026-08-05, access: full, locator: "section 'AI services can raise independence concerns for attest clients'" }
    - { ref: FMG-ABA512-2024, title: "ABA Issues Formal Guidance for Lawyers' Use of Generative AI", publisher: "FMG Law (Sunshine R. Fellows)", type: firm, url: "https://www.fmglaw.com/professional-liability/aba-issues-formal-guidance-for-lawyers-use-of-generative-ai/", date: 2024-08-14, access: full, locator: "'Confidentiality' paragraph" }
  last_reviewed: 2026-10-19
  notes: "Figures are stated preferences from a vendor-commissioned survey (conducted by Thinktiv for Introhive; 42 legal, 42 accounting and 39 other professional-services respondents), not outcomes. No published cross-sell result from an AI-driven opportunity list was found. The JofA article is guidance from AICPA ethics staff and is described there as non-authoritative where it refers to Q&A sections."

- id: professional-services-client-development-03
  title: At-risk relationship alerts and nudges for retention
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [data-reporting, client-interaction]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: "Relationships weaken without anyone noticing, and clients are now reconsidering firms that fall behind on AI. Partners find it hard to make time for contact."
  solution: "A monitoring layer flags relationships where contact has lapsed or account health scores drop, and nudges the partner with a suggested message. Vendors describe alerts on at-risk relationships and account-health analysis for customer success."
  outcomes:
    - { lever: growth, description: "Partners said alerts on at-risk relationships would be among the most valuable uses of combined firm information", figure: "49%", measures: "Share of 123 surveyed partners who ranked alerts on at-risk relationships near the top when asked what they would most value from combining information across the firm", provenance: vendor-published, source_ref: INTROHIVE-LAWSITES-2026 }
    - { lever: risk, description: "Client retention exposure reported by buyers of professional services", figure: "32% reconsidering; one-third of those estimate more than $1 million in annual work at risk", measures: "Share of corporate clients who have reconsidered, or plan within 12 months to reconsider, relationships with firms they feel are falling behind; among those reconsidering, one-third estimate more than $1 million of annual work at risk", provenance: vendor-published, source_ref: TR-FOP-2026 }
  prerequisites:
    - "Reliable activity data; an automated nudge is only as good as the contact record (INTROHIVE-LAWSITES-2026)"
    - "A defined action when an alert fires (who calls, with what)"
  risks_and_guardrails:
    - "Nudges that draft messages should not be sent without review where they carry client information or advice (CALBAR-GENAI-2026, p. 6)"
    - "Contact frequency is a proxy; the source does not report whether it predicts client departure, so alert thresholds are unvalidated"
  human_checkpoints:
    - "Partner decides whether to contact the client and what to say"
  role_evolution: "No source found describes role changes for alert-driven retention work. Introhive's CEO described the nudge as prompting the lawyer in their day-to-day workflow (INTROHIVE-LAWSITES-2026, 'A New Interface for An Old Problem')."
  evidence_grade: C
  sources:
    - { ref: INTROHIVE-LAWSITES-2026, title: "Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds", publisher: "LawSites (Bob Ambrogi)", type: press, url: "https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html", date: 2026-10-13, access: full, locator: "'What Partners Say They Want'; 'A New Interface for An Old Problem' (example of a 35-day nudge)" }
    - { ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: 2026-06-22, access: full, locator: "key finding 02 and section 'The profession under pressure: 01 Clients are already moving on'; date from the companion article page" }
    - { ref: CERTINIA-VEDA-2026, title: "Certinia AI and Veda agents", publisher: "Certinia", type: vendor, url: "https://certinia.com/solutions/ai", date: 2026-10, access: full, locator: "agent list: Customer Success Assistant analyses account playbooks, health scores and client activities; page undated" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)", publisher: "State Bar of California, COPRAC", type: professional-body, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "p. 6" }
  last_reviewed: 2026-10-19
  notes: "The TR-FOP survey covers 1,816 professionals (private practice and in-house); the report page does not state the number of corporate clients behind the 78%, 6% and 32% figures. A companion TRI report says the 2026 survey included 203 corporate legal professionals (TRI-LDOR-2026, Methodology), which may or may not be that subgroup. In-house perspective: these are buyer-side figures. Vendor pages describe the alerting feature but publish no detection accuracy or retention result."

- id: professional-services-client-development-04
  title: Revenue-linked attribution of business-development activity
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Most firms cannot connect BD activity to revenue, so firms cannot show whether relationship tools or AI change outcomes."
  solution: "Relationship, pipeline and billing data are joined so BD activity (introductions, meetings, cross-sell, pipeline influenced) can be attributed to revenue, replacing login and usage counts as the measure of return."
  outcomes:
    - { lever: growth, description: "Measurement gap in BD return", figure: "63% have no revenue-linked way to measure BD ROI; 15% can track revenue with strong attribution", measures: "Share of firms (as reported by the 123 surveyed partners) with no revenue-linked way to measure BD return on investment; share able to track revenue with strong attribution", provenance: vendor-published, source_ref: INTROHIVE-LAWSITES-2026 }
    - { lever: growth, description: "What firms track instead of revenue-linked measures", figure: "28% intermediate metrics; 22% usage and logins; 13% no formal measurement", measures: "As the source states it, instead of a revenue-linked measure: share of firms tracking intermediate metrics such as introductions and meetings; tracking usage and logins; having no formal measurement (the three add to the 63%)", provenance: vendor-published, source_ref: INTROHIVE-LAWSITES-2026 }
  prerequisites:
    - "Shared identifiers across CRM, matter and billing systems"
    - "Agreement on what counts as influenced revenue; Introhive's CEO acknowledged the 'if I had only known' case is persuasive but 'not a slam dunk' (INTROHIVE-LAWSITES-2026, 'Measuring Return')"
  risks_and_guardrails:
    - "The survey is vendor-commissioned and the vendor's CEO conceded that proving its own ROI is hard when firms cannot connect BD activity to revenue (INTROHIVE-LAWSITES-2026)"
    - "Efficiency metrics that only track hours saved miss client value; TRI recommends value metrics such as turnaround, risk identification, consistency and client satisfaction (TRI-STANDOUT-2026, 'Turning strategy into systems')"
  human_checkpoints:
    - "BD and finance leaders agree attribution rules before results are used in partner compensation"
  role_evolution: "BD operations teams own attribution models alongside finance; partners are asked to show pipeline influence. TRI says partners are the 'commercial transmission mechanism' of the firm (TRI-STANDOUT-2026, 'Getting on the same page')."
  evidence_grade: C
  sources:
    - { ref: INTROHIVE-LAWSITES-2026, title: "Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds", publisher: "LawSites (Bob Ambrogi)", type: press, url: "https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html", date: 2026-10-13, access: full, locator: "section 'Measuring Return'" }
    - { ref: TRI-STANDOUT-2026, title: "Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice", date: 2026-08-06, access: full, locator: "'Turning strategy into systems', 'Moving to more value-based measurement'" }
  last_reviewed: 2026-10-19
  notes: "Recorded as a measurement gap, not an outcome of AI. No firm was found that reports a revenue-attributed AI BD result. The three alternative measures (28%, 22%, 13%) add to the 63% without a revenue-linked measure; the remaining firms are not described in the article."

- id: professional-services-client-development-05
  title: Partners using general-purpose AI chatbots for BD research, outreach drafting and pitch preparation
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [document-production, research-synthesis]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Partners are asked to take on BD work once done by marketing staff, with little time and no access to firm relationship data."
  solution: "Partners use ChatGPT, Copilot, Gemini or similar tools themselves to research clients and prospects and draft messages, outside the firm's data."
  outcomes:
    - { lever: capacity, description: "Share of AI-using partners relying only on general-purpose tools, and their satisfaction", figure: "68%; satisfaction 6.7 out of 10", measures: "Share of partners already using AI for business development who rely only on general-purpose tools (ChatGPT, Copilot or Gemini); mean satisfaction rating they gave those tools out of 10", provenance: vendor-published, source_ref: INTROHIVE-LAWSITES-2026 }
    - { lever: risk, description: "Professionals using AI their organisation has not sanctioned", figure: "34%", measures: "Share of surveyed professionals who say they use AI tools their organisation has not sanctioned (all fiduciary professions, not BD only)", provenance: vendor-published, source_ref: TR-FOP-2026 }
  prerequisites:
    - "A sanctioned alternative with data-handling terms; 41% of professionals who use AI at work lack access to AI tools built for professional work (TR-FOP-2026)"
    - "Policy and training; training before access is required by 11% of the smallest firms and 72% of the largest (ILTA-TECHSURVEY-2026, Q3.18)"
  risks_and_guardrails:
    - "A lawyer must not enter client confidential information into a tool that presents material confidentiality or security risks without informed consent (CALBAR-GENAI-2026, p. 5)"
    - "ABA Opinion 512 asks lawyers to understand a tool's terms and whether it is self-learning before entering client information (FMG-ABA512-2024, 'Confidentiality')"
  human_checkpoints:
    - "Partner reviews every outbound message and checks claims about the client or the firm"
  role_evolution: "Introhive's CEO said partners are now being asked to take on BD responsibilities they once left to marketing staff (INTROHIVE-LAWSITES-2026, 'A Complex Environment'). California expects managerial lawyers to set clear AI policies and training (CALBAR-GENAI-2026, p. 7)."
  evidence_grade: C
  sources:
    - { ref: INTROHIVE-LAWSITES-2026, title: "Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds", publisher: "LawSites (Bob Ambrogi)", type: press, url: "https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html", date: 2026-10-13, access: full, locator: "paragraph beginning 'Among partners already using AI for business development'" }
    - { ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: 2026-06-22, access: full, locator: "key findings 01 and 03" }
    - { ref: ILTA-TECHSURVEY-2026, title: "The ILTA Technology Survey 2026 Executive Summary", publisher: "International Legal Technology Association", type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026-06, access: full, locator: "Q3.18 table, p. 5" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)", publisher: "State Bar of California, COPRAC", type: professional-body, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "p. 5 (Duty of Confidentiality)" }
    - { ref: FMG-ABA512-2024, title: "ABA Issues Formal Guidance for Lawyers' Use of Generative AI", publisher: "FMG Law (Sunshine R. Fellows)", type: firm, url: "https://www.fmglaw.com/professional-liability/aba-issues-formal-guidance-for-lawyers-use-of-generative-ai/", date: 2024-08-14, access: full, locator: "'Confidentiality' paragraph" }
  last_reviewed: 2026-10-19
  notes: "Maturity is emerging because the evidence is survey-based and no named firm is attached. The 68% base is partners already using AI for BD, a small group in the survey; the report's n for that subgroup is not given in the LawSites article."

- id: professional-services-client-development-06
  title: AI call and meeting summaries and call coaching written into account records
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [document-production, client-interaction]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Notes from client calls and meetings are lost or never reach the account record."
  solution: "A call summary agent turns call conversations into meeting summaries, and a call coach agent analyses recordings to improve communication; both feed the account record held in a professional-services automation system."
  outcomes:
    - { lever: capacity, description: "none published", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: CERTINIA-VEDA-2026 }
  prerequisites:
    - "Participant consent for recording and transcription, which depends on state or national consent rules (BLOOMBERGLAW-OTTER-2026)"
    - "A decision on retention and where transcripts are held, since AI notes create a new category of discoverable documents (BLOOMBERGLAW-OTTER-2026)"
  risks_and_guardrails:
    - "In In re Otter.ai Privacy Litigation, plaintiffs who were not account holders allege an AI notetaker recorded meetings without participants' consent under California's wiretapping statute; Bloomberg Law's analysis says the safest course is to disclose the tool and get all participants' consent (BLOOMBERGLAW-OTTER-2026)"
    - "The article lists nine all-party-consent jurisdictions, including California, Florida, Illinois and Pennsylvania (BLOOMBERGLAW-OTTER-2026)"
    - "Whether a vendor counts as a tool or a third-party eavesdropper is unsettled, and a vendor with data-mining rights can expose the customer to vicarious liability (BLOOMBERGLAW-OTTER-2026)"
    - "Client confidential information may not be entered into tools with material confidentiality risks without informed consent (CALBAR-GENAI-2026, p. 5)"
  human_checkpoints:
    - "Account lead reviews the summary before it is shared or filed"
    - "Disclosure of the notetaker at the start of the meeting"
  role_evolution: "No source found describes role changes from AI call summaries or coaching."
  evidence_grade: C
  sources:
    - { ref: CERTINIA-VEDA-2026, title: "Certinia AI and Veda agents", publisher: "Certinia", type: vendor, url: "https://certinia.com/solutions/ai", date: 2026-10, access: full, locator: "agent list: Call Summary Agent, Call Coach Agent; page undated" }
    - { ref: BLOOMBERGLAW-OTTER-2026, title: "AI Notetaking Poses Wiretapping, Discovery, and Ethical Pitfalls", publisher: "Bloomberg Law", type: press, url: "https://news.bloomberglaw.com/ip-law/ai-notetaking-poses-wiretapping-discovery-and-ethical-pitfalls", date: 2026-01-28, access: full, locator: "paragraphs on In re Otter.ai, consent regimes and vendor classification" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)", publisher: "State Bar of California, COPRAC", type: professional-body, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "p. 5" }
  last_reviewed: 2026-10-19
  notes: "Vendor product listing only; no named customer, error rate or time saving found. The Otter.ai case posture as of October 2026 was not confirmed. The Bloomberg Law piece is analysis of the case as of January 2026."

- id: professional-services-client-development-07
  title: Generated account plans, client briefs and meeting preparation from CRM and engagement data
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [document-production, research-synthesis]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Account plans, success plans and client briefs are assembled by hand from several systems; senior lawyers skip regular client notes because they take time from billable work."
  solution: "AI pulls news, regulatory developments, earnings calls, relationship data and, for some tools, engagement and account history, to draft account summaries, success plans and business reviews, and to prepare partners for client meetings."
  outcomes:
    - { lever: capacity, description: "none published", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: CERTINIA-VEDA-2026 }
  prerequisites:
    - "Bespoke one-on-one training for partners on how AI helps them prepare for client conversations; TRI forum panelists said broad one-size-fits-all sessions are not enough (TRI-CMBDO-2026)"
    - "Client-specific insight and competitive intelligence; stand-out lawyers rank these as top needs whatever their AI usage (TRI-STANDOUT-2026, 'How to talk to clients about AI')"
  risks_and_guardrails:
    - "Unrestricted or poorly configured agentic systems may disclose confidential information across different matters (CALBAR-GENAI-2026, p. 6)"
    - "Briefs should be a foundation, not a script, and authenticity still depends on the lawyer (TRI-CMBDO-2026)"
  human_checkpoints:
    - "Partner or client lead reviews and edits the brief before use"
  role_evolution: "Panelists said AI shifts partners from blank-page preparation to reviewing a tailored starting point, with training as the main adoption lever (TRI-CMBDO-2026)."
  evidence_grade: C
  sources:
    - { ref: CERTINIA-VEDA-2026, title: "Certinia AI and Veda agents", publisher: "Certinia", type: vendor, url: "https://certinia.com/solutions/ai", date: 2026-10, access: full, locator: "section 'Give every account a strategist'; page undated" }
    - { ref: TRI-CMBDO-2026, title: "Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI may be talking to your clients about it", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai", date: 2026-02-18, access: full, locator: "paragraphs on client outreach, opportunity matrix and training" }
    - { ref: TRI-STANDOUT-2026, title: "Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice", date: 2026-08-06, access: full, locator: "'How to talk to clients about AI'" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)", publisher: "State Bar of California, COPRAC", type: professional-body, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "p. 6" }
  last_reviewed: 2026-10-19
  notes: "The TRI forum report is a conference write-up of panel statements (33rd CMBDO Forum, Amelia Island), not a measured deployment. Named-firm deployments are in the practice-angle file."

- id: professional-services-client-development-08
  title: Structured AI value conversations between partners and key clients
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [client-interaction, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Clients expect AI to be used and want to know how it lowers cost and improves quality on their matters, but partners rarely raise the subject and firms cannot yet show matter-level savings."
  solution: "Firms prepare partners with talking points, client-specific insight, approved language on risk and limitations, and billing guidance, and sequence the conversation: what changed in the work, what changed for the client, what value that created, then how pricing should reflect it. Some firm leaders advise setting the meeting rather than waiting for the client to set terms."
  outcomes:
    - { lever: growth, description: "Low frequency of AI conversations with clients even among heavy AI users", figure: "about one-third", measures: "Share of 'embedded AI' partners (heavy users) among client-nominated stand-out lawyers who said they had discussed AI with at least 60% of their clients", provenance: vendor-published, source_ref: TRI-STANDOUT-2026 }
    - { lever: growth, description: "Lawyers who rarely have the conversation", figure: "more than one-third", measures: "Share of the stand-out lawyers surveyed who said they had talked about AI with fewer than 20% of their clients", provenance: vendor-published, source_ref: TRI-STANDOUT-2026 }
    - { lever: risk, description: "Gap between client expectation and delivery", figure: "78% vs 6%", measures: "Corporate clients saying AI-enabled quality improvements from firms are very important or essential vs corporate clients saying most or all providers deliver them", provenance: vendor-published, source_ref: TR-FOP-2026 }
    - { lever: risk, description: "In-house views of law-firm AI savings", figure: "59% no savings yet; 24% satisfied; 61% plan to push for change", measures: "Share of in-house respondents (of 657 in 30 countries) reporting no GenAI savings from their law firms yet; satisfied with how outside counsel adopt GenAI for cost effectiveness; planning to push for change in how legal services are delivered and priced", provenance: vendor-published, source_ref: EVERLAW-ACC-PR-2025 }
    - { lever: growth, description: "Support for firms starting the conversation", figure: "77%", measures: "Share of respondents to TRI's 2026 AI in Professional Services Report who believe law firms should take the initiative to begin AI-usage talks with clients (the article does not give the respondent base)", provenance: vendor-published, source_ref: TRI-CMBDO-2026 }
  prerequisites:
    - "Partners who use AI themselves: partners embedded with AI are nine times more likely than minimal users to report significant impact on efficiency and quality (TRI-STANDOUT-2026, 'Getting on the same page')"
    - "A GenAI strategy: TR's Steven Petrie said firms with one are 3.9 times more likely to achieve ROI, and that 22% of firms have one (TRI-LEGALWEEK-2026, 'The pressure hasn't yet found a release valve')"
    - "Evidence of what changed on the matter; firm speakers said they were still gathering data and described ROI measurement as anecdotal (TRI-LEGALWEEK-2026)"
  risks_and_guardrails:
    - "Clients do not speak with one voice: some ask how AI will hit savings targets and want line-item AI transparency, others issue guidelines saying they will not pay for certain work done by AI, and some still ask for warranties that models are unbiased (TRI-LEGALWEEK-2026, 'The contradictions in the room')"
    - "TRI notes that a firm that leads with price concessions before showing value may train clients to expect discounts (TRI-STANDOUT-2026, 'How to talk to clients about AI')"
    - "Consultants must not overstate AI expertise, credentials or experience in proposals, marketing or client discussions (ICMCI-AICODE-2026, section 11.2)"
    - "Under the ABA opinion as summarised, a lawyer must consult the client about AI use where it is relevant to the basis or reasonableness of fees (FMG-ABA512-2024, 'Communication'). California adds that hourly billing must reflect time actually spent (CALBAR-GENAI-2026, p. 8)"
    - "Brynjolfsson and Petropoulos argue AI used internally to augment consultants is likely to heighten information asymmetries at first, which affects how much clients trust effort-based pricing (STANFORD-DEL-2026, abstract)"
  human_checkpoints:
    - "The partner leads the conversation and owns what is claimed about AI use and savings"
    - "Pricing and value-sharing proposals go through the firm's pricing function before they are offered"
  role_evolution: "TRI calls partners the commercial transmission mechanism for strategy and says firms need systems to turn strategy into client experience (TRI-STANDOUT-2026, 'Getting on the same page'). Greenberg Traurig has a Chief Pricing and Innovation Officer who described clients newly asking about AI on specific matters (TRI-LEGALWEEK-2026)."
  evidence_grade: B
  sources:
    - { ref: TRI-STANDOUT-2026, title: "Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice", date: 2026-08-06, access: full, locator: "'How to talk to clients about AI'; Methodology (2,527 lawyers, 116 leader interviews)" }
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "sections 'Proving AI's path to saving clients money', 'The contradictions in the room', 'The pressure hasn't yet found a release valve'" }
    - { ref: TRI-CMBDO-2026, title: "Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI may be talking to your clients about it", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai", date: 2026-02-18, access: full, locator: "paragraph citing the 77% finding" }
    - { ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: 2026-06-22, access: full, locator: "key finding 02; 'The profession under pressure: 01 Clients are already moving on'" }
    - { ref: EVERLAW-ACC-PR-2025, title: "64% of In-House Counsel Expect GenAI to Reduce Reliance on Outside Counsel, 50% Expect Lower Outside Counsel Costs, ACC/Everlaw Survey Finds (press release reprint)", publisher: "Everlaw and the Association of Corporate Counsel (via Business Wire)", type: survey, url: "https://markets.financialcontent.com/worldnow.ktul/article/bizwire-2025-10-14-64-of-in-house-counsel-expect-genai-to-reduce-reliance-on-outside-counsel-50-expect-lower-outside-counsel-costs-acceverlaw-survey-finds", date: 2025-10-14, access: full, locator: "paragraph 'Clients will challenge the billable hour'" }
    - { ref: ICMCI-AICODE-2026, title: "Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, v1.0", publisher: "International Council of Management Consulting Institutes", type: professional-body, url: "https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf", date: 2026-05, access: full, locator: "sections 1.1 and 11.2, pp. 4 and 15-16" }
    - { ref: FMG-ABA512-2024, title: "ABA Issues Formal Guidance for Lawyers' Use of Generative AI", publisher: "FMG Law (Sunshine R. Fellows)", type: firm, url: "https://www.fmglaw.com/professional-liability/aba-issues-formal-guidance-for-lawyers-use-of-generative-ai/", date: 2024-08-14, access: full, locator: "'Communication' and 'Fees' paragraphs" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)", publisher: "State Bar of California, COPRAC", type: professional-body, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "p. 7 (Communication) and p. 8 (Charging)" }
    - { ref: STANFORD-DEL-2026, title: "Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives", publisher: "Stanford Digital Economy Lab (Brynjolfsson, Petropoulos)", type: academic, url: "https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf", date: 2026-08-23, access: full, locator: "Abstract, p. 1; section 3, p. 6" }
  last_reviewed: 2026-10-19
  notes: "Pattern is other: the AI role is preparation and evidence, and the conversation itself is human. Graded B because named firms (Greenberg Traurig, DLA Piper, Hogan Lovells, Ropes & Gray, Zarwin Baum) and a named client (GSK) describe the conversations in a conference account, and TRI measured how often partners have them; no outcome of the conversations (retained work, fee outcome) is published, so the grade stays below A. TRI is a publisher owned by a legal-technology vendor. The ACC/Everlaw survey was co-published by a vendor (Everlaw). In-house: the 59%, 24% and 61% figures are from in-house respondents. The Stanford paper is about consulting, not law, and its framework is qualitative (the authors call the evidence 'qualitative plausibility'). The 22% of firms with a GenAI strategy comes from a TR speaker at Legalweek; it is unrelated to the 22% in the Introhive survey, which counts partners who say their firm has a fully developed strategy."

- id: professional-services-client-development-09
  title: Joint client and firm AI use-case development and measurement with key accounts
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [client-interaction, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Neither firm nor client has a shared framework for measuring or splitting AI savings, so each side drives its own assumptions."
  solution: "Key clients and their firms agree how AI will be used on the client's work, supply work to test new use cases together, and define the savings measures jointly, instead of the firm presenting a tool tour or the client imposing guidelines."
  outcomes:
    - { lever: experience, description: "none published", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: TRI-STANDOUT-2026 }
  prerequisites:
    - "A client willing to share matter data and measures; GSK's chief of staff for legal and compliance said the company learns from its outside firms about their GenAI use and looks to partner on new use cases (TRI-LEGALWEEK-2026)"
    - "Agreed definitions of savings and quality"
  risks_and_guardrails:
    - "The firm must follow client instructions or guidelines that restrict AI use (CALBAR-GENAI-2026, p. 7)"
    - "Joint use of the client's data in AI tools engages confidentiality and informed-consent duties (CALBAR-GENAI-2026, p. 5; FMG-ABA512-2024)"
  human_checkpoints:
    - "Client and firm leads sign off on the use case, data scope and measure before work starts"
  role_evolution: "Client-relationship partners and pricing or innovation officers act as co-design leads. The Greenberg Traurig Chief Pricing and Innovation Officer role is an example of a firm role that spans both (TRI-LEGALWEEK-2026)."
  evidence_grade: C
  sources:
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "section 'Proving AI's path to saving clients money' (GSK remarks)" }
    - { ref: TRI-STANDOUT-2026, title: "Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice", date: 2026-08-06, access: full, locator: "'How to talk to clients about AI' (productive conversations produce next steps)" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)", publisher: "State Bar of California, COPRAC", type: professional-body, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "pp. 5 and 7" }
    - { ref: FMG-ABA512-2024, title: "ABA Issues Formal Guidance for Lawyers' Use of Generative AI", publisher: "FMG Law (Sunshine R. Fellows)", type: firm, url: "https://www.fmglaw.com/professional-liability/aba-issues-formal-guidance-for-lawyers-use-of-generative-ai/", date: 2024-08-14, access: full, locator: "'Confidentiality'" }
  last_reviewed: 2026-10-19
  notes: "Pattern is other: a relationship model, not an agentic pattern. In-house: the named client voice is GSK (TRI-LEGALWEEK-2026). The evidence is a stated intent by a named client and analyst-reported practice among unnamed stand-out lawyers, so grade C; no named joint programme with results was found."

- id: professional-services-client-development-10
  title: Client-facing reporting of AI use and savings at matter or account level
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [data-reporting, client-interaction]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Clients ask whether AI was used on a task and how much time or money it saved, and some will not pay for work done by AI; firms cannot answer from records."
  solution: "AI-assisted tasks are logged against client and matter so that account teams can show clients where AI was used, what was reviewed and what changed, as a basis for line-item transparency or value reporting."
  outcomes:
    - { lever: experience, description: "none published", figure: "none published", measures: "not applicable. Legalweek firm speakers said they were still gathering data", provenance: self-reported, source_ref: TRI-LEGALWEEK-2026 }
  prerequisites:
    - "A record linking AI tasks to client and matter"
    - "Value metrics beyond hours saved, such as faster turnaround, better risk identification, consistency and client satisfaction (TRI-STANDOUT-2026, 'Turning strategy into systems')"
  risks_and_guardrails:
    - "Hourly bills must reflect time actually spent, and flat fees may build in AI savings; AI costs billed as expenses must reflect actual cost with no markup without informed written consent (CALBAR-GENAI-2026, p. 8)"
    - "Under the ABA opinion as summarised, firms may not bill for general overhead and may not charge for time spent learning a tool they will regularly use (FMG-ABA512-2024, 'Fees')"
    - "Clients' guidelines may restrict or prohibit AI use or charges; firms must follow them (CALBAR-GENAI-2026, p. 7; LOUBAR-2025, Tips 2 and 3)"
  human_checkpoints:
    - "Billing partner approves any AI-related line item or credit"
  role_evolution: "Client-relationship, pricing and finance roles share ownership of AI value reporting. The Ropes & Gray technology innovation director described client requests for line-item transparency as beginning (TRI-LEGALWEEK-2026)."
  evidence_grade: D
  sources:
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "section 'The contradictions in the room'" }
    - { ref: TRI-STANDOUT-2026, title: "Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice", date: 2026-08-06, access: full, locator: "'Moving to more value-based measurement'" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)", publisher: "State Bar of California, COPRAC", type: professional-body, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "pp. 7-8" }
    - { ref: FMG-ABA512-2024, title: "ABA Issues Formal Guidance for Lawyers' Use of Generative AI", publisher: "FMG Law (Sunshine R. Fellows)", type: firm, url: "https://www.fmglaw.com/professional-liability/aba-issues-formal-guidance-for-lawyers-use-of-generative-ai/", date: 2024-08-14, access: full, locator: "'Fees'" }
    - { ref: LOUBAR-2025, title: "Navigating AI with Outside Counsel: Practical Tips for In-House Counsel", publisher: "Louisville Bar Association, Bar Briefs (Crosby and Lavanga)", type: professional-body, url: "https://www.loubar.org/wp-content/uploads/2025/12/Bar-Briefs_December25_Navigating-AI-with-Outside-Counsel_Crosby-and-Lavanga-1.pdf", date: 2025-12, access: full, locator: "Tips 2, 3 and 6" }
  last_reviewed: 2026-10-19
  notes: "Pattern is other: reporting step. Idea (grade D): discussed by Legalweek panelists and TRI, but no firm was found reporting matter-level AI value reports sent to clients. The billing mechanics (time capture, line items) belong to billing-collections; this entry covers the client-development step of using the evidence in the relationship. Related announced product work (Legora-Laurel, 2026-10-13) is documented in the firm-finance and landscape files."

- id: professional-services-client-development-11
  title: AI disclosure and consent terms in engagement letters, outside counsel guideline responses and renewals
  archetype: professional-services
  module: client-development
  function: risk-compliance-legal
  work_types: [document-production, client-interaction]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Clients ask how AI is used on their work and set terms about it, while professional-body guidance says boilerplate consent is not enough."
  solution: "Firms standardise AI terms (what AI may be used for, human review, no confidential data to public AI systems without written consent, notification of changes) in engagement letters and answer client AI addenda, and reopen the terms at renewal."
  outcomes:
    - { lever: risk, description: "Share of firms whose policy requires client approval, by firm size", figure: "8% (under 50 lawyers), 20% (50-149), 24% (150-349), 38% (350-699), 34% (over 700)", measures: "Share of surveyed firms in each lawyer-count band selecting 'Must obtain client approval' among the options that describe their official GenAI policies or guidance (more than one option allowed)", provenance: independent, source_ref: ILTA-TECHSURVEY-2026 }
    - { lever: risk, description: "Share of firms with a formal GenAI policy at all, by size", figure: "57% (under 50 lawyers) to 98% (350-699)", measures: "Share of surveyed firms in each size band selecting 'A formal policy is in place'", provenance: independent, source_ref: ILTA-TECHSURVEY-2026 }
  prerequisites:
    - "A firm position on which AI uses are material to the client. The NYC Bar notes that routine embedded tools such as word-processor grammar checks need not be disclosed (NYCBAR-OP2024-5, footnote 21)"
    - "Awareness of statutory consent rules for tax data: a CPA firm webinar sample clause says the firm will consider 26 USC 7216 before disclosing tax return data (WOODARD-2025)"
  risks_and_guardrails:
    - "General boilerplate provisions in engagement letters are not sufficient consent under the ABA opinion, as summarised (JOA-DISCLOSE-2025; 2CIVILITY-ABA512-2024)"
    - "Disclosure carries a trust cost: across 13 experiments, people who disclosed AI use were trusted less, though the penalty was smaller for evaluators with favourable technology attitudes or who believed AI is accurate; quiet use later exposed was worse (SCHILKE-OBHDP-2025; SCHILKE-CONVERSATION-2025)"
    - "The SRA has no specific guidance on disclosure of AI use for client care, and the Law Society advises firms and clients to decide together whether and how tools will be used (LAWSOC-GENAI-2026)"
    - "The ICMCI code requires consultants to tell clients when AI materially affects advice, analysis or deliverables, and encourages engagement terms on AI scope; routine productivity tools need not be disclosed individually (ICMCI-AICODE-2026, sections 3.3, 7.1 and 7.3)"
  human_checkpoints:
    - "Partner or risk lead approves the AI terms offered to or accepted from each client"
    - "Terms reviewed annually as guidance evolves (WOODARD-2025, slide 'AICPA Guidance: AI Use & Transparency')"
  role_evolution: "No source found describes role changes. Woodard's slides recommend updating AI clauses annually as guidance evolves (WOODARD-2025)."
  evidence_grade: B
  sources:
    - { ref: ILTA-TECHSURVEY-2026, title: "The ILTA Technology Survey 2026 Executive Summary", publisher: "International Legal Technology Association", type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026-06, access: full, locator: "Q3.18 table, p. 5" }
    - { ref: WOODARD-2025, title: "Future Ready Engagement Letters (webinar slides)", publisher: "Woodard (CPA-firm management consultancy)", type: firm, url: "https://www.woodard.com/hubfs/Future_Ready_Engagement_Letters_Oct2025.pdf", date: 2025-10, access: full, locator: "slides 'AICPA Guidance: AI Use & Transparency' and 'AI Disclosure & Consent Clause'" }
    - { ref: JOA-DISCLOSE-2025, title: "Should I disclose my use of gen AI to clients?", publisher: "Journal of Accountancy (AICPA)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2025/apr/should-i-disclose-my-use-of-gen-ai-to-clients/", date: 2025-04-01, access: full, locator: "sections on compulsory requirements and consent" }
    - { ref: 2CIVILITY-ABA512-2024, title: "Breaking Down ABA Guidance on Using GenAI in Legal Practice", publisher: "Illinois Supreme Court Commission on Professionalism (2Civility)", type: professional-body, url: "https://www.2civility.org/breaking-down-the-abas-guidance-on-using-Generative-ai-in-legal-practice/", date: 2024-08-15, access: full, locator: "sections on confidentiality and communication" }
    - { ref: NYCBAR-OP2024-5, title: "Formal Opinion 2024-5: Generative AI in the Practice of Law", publisher: "New York City Bar Association", type: professional-body, url: "https://www.nycbar.org/reports/formal-opinion-2024-5-generative-ai-in-the-practice-of-law/", date: 2024-08-07, access: full, locator: "footnote 21" }
    - { ref: LAWSOC-GENAI-2026, title: "Generative AI: the essentials", publisher: "The Law Society of England and Wales", type: professional-body, url: "https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials", date: 2026, access: full, locator: "sections on client care and the SRA; page cites events to May 2026, update date not shown" }
    - { ref: ICMCI-AICODE-2026, title: "Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, v1.0", publisher: "International Council of Management Consulting Institutes", type: professional-body, url: "https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf", date: 2026-05, access: full, locator: "sections 3.3, 7.1, 7.3" }
    - { ref: SCHILKE-OBHDP-2025, title: "The transparency dilemma: How AI disclosure erodes trust", publisher: "Organizational Behavior and Human Decision Processes, vol. 188 (Schilke and Reimann)", type: academic, url: "https://ideas.repec.org/a/eee/jobhdp/v188y2025ics0749597825000172.html", date: 2025, access: full, locator: "abstract" }
    - { ref: SCHILKE-CONVERSATION-2025, title: "Being honest about using AI at work makes people trust you less, research finds", publisher: "University of Arizona News (republished from The Conversation; Schilke and Reimann)", type: academic, url: "https://news.arizona.edu/employee-news/being-honest-about-using-ai-work-makes-people-trust-you-less-research-finds", date: 2025-05-29, access: full, locator: "paragraphs on 13 experiments and on being exposed by a third party" }
  last_reviewed: 2026-10-19
  notes: "Graded B: ILTA publishes a measured prevalence of the practice, by firm size, but no outcome. The Woodard slides are a consultancy webinar with sample language, not a deployment. The Schilke authors' own article says more than 5,000 participants; the journal abstract says thirteen experiments. A Substack summary seen in search gave a lower participant count and is not used. The Schilke tension with disclosure duties is a design constraint: bar guidance and the ICMCI code require disclosure of material uses, and the study finds a penalty for disclosing. JofA article says no specific federal law or CPA standard mandates disclosure of gen AI use, and that some states, including California and Utah, have enacted disclosure-related laws."

- id: professional-services-client-development-12
  title: AI capability positioning in marketing, credentials and thought leadership
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Clients expect AI-savvy firms and silence or vague messaging is a missed opportunity, but claims about AI are regulated as marketing statements and AI-generated content has its own transparency rules."
  solution: "Firms describe their AI capabilities and results to clients in marketing, credentials and thought leadership, grounded in verifiable facts, and use AI to help draft that content under human editorial control."
  outcomes:
    - { lever: growth, description: "Share of firms that market their use of GenAI tools, by size", figure: "2% (under 50 lawyers), 8% (50-149), 19% (150-349), 27% (350-699), 52% (over 700)", measures: "Share of surveyed firms in each lawyer-count band selecting 'Use of GAI tools actively marketed' among the options describing their official GenAI policies or guidance", provenance: independent, source_ref: ILTA-TECHSURVEY-2026 }
  prerequisites:
    - "Claims that are objectively verifiable. The Florida opinion, as reproduced by a third-party site, says lawyers may advertise their use of generative AI but cannot claim it is superior to others unless the claim is objectively verifiable (FLBAR-OP241-2024, section 'Lawyer Advertising')"
    - "A shared firm view on AI position: TRI describes an AI Position Matrix from interviews with law firm leaders and warns that mixed signals leave partners unable to convert aspiration into behaviour (TRI-STANDOUT-2026, 'A clearer AI positioning')"
  risks_and_guardrails:
    - "Management consultants must not overstate AI expertise, credentials or experience in proposals, marketing materials, credentials presentations or client discussions (ICMCI-AICODE-2026, section 11.2)"
    - "EU AI Act Article 50(4), as shown on an unofficial explorer, requires deployers of AI-generated text published to inform the public on matters of public interest to disclose it, unless the content has had human review or editorial control and a person holds editorial responsibility. The Commission says the transparency rules apply from August 2026 (AIACT-ART50; EC-AIACT-2026)"
    - "Whether a firm's thought-leadership articles count as informing the public on matters of public interest is not addressed in the sources found, so the scope of Article 50(4) for firm marketing is untested here"
  human_checkpoints:
    - "A named editor or partner holds editorial responsibility for each piece before publication"
    - "Marketing or ethics review of any claim about AI capability or results"
  role_evolution: "Marketing and BD teams take on claim substantiation alongside content production."
  evidence_grade: B
  sources:
    - { ref: ILTA-TECHSURVEY-2026, title: "The ILTA Technology Survey 2026 Executive Summary", publisher: "International Legal Technology Association", type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026-06, access: full, locator: "Q3.18 table, p. 5; text on the 50-point difference in external marketing" }
    - { ref: FLBAR-OP241-2024, title: "Florida Bar Ethics Opinion 24-1 (text as reproduced by Ezel)", publisher: "The Florida Bar, Professional Ethics Committee (mirror: ezel.ai)", type: professional-body, url: "https://ezel.ai/ethics-opinions/flbar/24-1-generative-ai-in-law-practice", date: 2024-01-19, access: full, locator: "section 'Lawyer Advertising'" }
    - { ref: ICMCI-AICODE-2026, title: "Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, v1.0", publisher: "International Council of Management Consulting Institutes", type: professional-body, url: "https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf", date: 2026-05, access: full, locator: "sections 1.1 and 11.2" }
    - { ref: TRI-STANDOUT-2026, title: "Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice", date: 2026-08-06, access: full, locator: "'A clearer AI positioning'" }
    - { ref: AIACT-ART50, title: "Article 50: Transparency Obligations for Providers and Deployers of Certain AI Systems (AI Act Explorer)", publisher: "Future of Life Institute, EU Artificial Intelligence Act explorer (reproduces Regulation (EU) 2024/1689)", type: regulator, url: "https://artificialintelligenceact.eu/article/50/", date: 2024-06, access: full, locator: "paragraphs 1 and 4" }
    - { ref: EC-AIACT-2026, title: "AI Act (regulatory framework page)", publisher: "European Commission", type: regulator, url: "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai", date: 2026-10, access: full, locator: "sections 'Transparency risk' and implementation timeline; page undated, read 2026-10-19" }
  last_reviewed: 2026-10-19
  notes: "Graded B on the ILTA measurement of the practice (a named body reports prevalence); no outcome is published. The Florida text was read on a third-party mirror, not the Bar's own page (the Bar page loaded without body text); the opinion date is from the OSB footnote citing it. The explorer's text may not reflect later amendments by the AI Omnibus, which the Commission says entered into force 2026-07-27; the Commission page was used for the application date. Thought-leadership production by AI was discussed by the ABA's Law Practice magazine (search result only, not opened)."

- id: professional-services-client-development-13
  title: Website chatbot or AI agent for prospective-client intake and marketing
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [client-interaction, transaction-processing]
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Prospects contact firms outside office hours and intake is slow; but a conversational tool can create a client relationship or mislead."
  solution: "A chatbot (rule-based or AI-powered, possibly with agent features) answers visitors' questions, gathers factual information and routes leads to a lawyer."
  outcomes:
    - { lever: speed, description: "none published", figure: "none published", measures: "not applicable. The sources are regulator and bar-body opinions, not deployments", provenance: independent, source_ref: OSB-FO-2026-208 }
  prerequisites:
    - "Monitoring and the ability to modify chatbot responses; the lawyer must be able to review communications and correct misstatements (OSB-FO-2026-208, section II)"
    - "Vendor due diligence, including underlying software vendors, repeated periodically (OSB-FO-2026-208, section II)"
    - "Automatic notification so a responsible lawyer can promptly review each interaction and decide whether a relationship formed (OSB-FO-2026-208, section III.A)"
  risks_and_guardrails:
    - "A chatbot that sounds like a lawyer can lead a prospect to believe an attorney-client relationship has formed, with duties of competence, diligence and communication; disclaimers must be clear (OSB-FO-2026-208, section III.A)"
    - "A chatbot that does not identify itself as a chatbot could be a misleading communication under Rule 7.1, and the chatbot must not give legal advice (OSB-FO-2026-208, section III.B)"
    - "Florida says a lawyer must tell prospective clients they are communicating with an AI program, and should consider screening questions for people already represented (FLBAR-OP241-2024, 'Lawyer Advertising')"
    - "Rule 7.3(a) may be implicated where a person's impaired state is visible to a human but not a chatbot (OSB-FO-2026-208, section III.B)"
    - "Information from prospects is protected under Rule 1.18; a lawyer who obtains disqualifying information through a chatbot should promptly enter the prospect into the conflict system (OSB-FO-2026-208, section III.C)"
    - "Autonomous actions such as sending an engagement letter should be subject to lawyer approval (OSB-FO-2026-208, section III.D)"
    - "EU AI Act Article 50(1) requires systems that interact directly with people to be designed so that people are informed they are dealing with AI, unless obvious (AIACT-ART50)"
  human_checkpoints:
    - "Responsible lawyer reviews each interaction and decides whether to proceed or tell the prospect no relationship will follow"
    - "Lawyer approval before any autonomous communication goes out"
  role_evolution: "Oregon says review of chatbot interactions may be delegated to trained staff, and that Rule 5.3 supervisory duties may reach third parties that provide chatbot services (OSB-FO-2026-208, section III.A footnote 10 and section III)."
  evidence_grade: C
  sources:
    - { ref: OSB-FO-2026-208, title: "Formal Opinion No 2026-208: Chatbots and AI Agent Communications", publisher: "Oregon State Bar", type: professional-body, url: "https://www.osbar.org/_docs/ethics/2026-208.pdf", date: 2026-02, access: full, locator: "Question and Conclusion; sections II, III.A-III.D" }
    - { ref: WSBA-NWSIDEBAR-OSB-2026, title: "New Oregon State Bar Opinion on Using AI Agents for Client Intake", publisher: "NWSidebar, Washington State Bar Association (Mark Fucile)", type: professional-body, url: "https://nwsidebar.wsba.org/2026/03/23/new-oregon-state-bar-opinion-on-using-ai-agents-for-client-intake/", date: 2026-03-23, access: full, locator: "body" }
    - { ref: FLBAR-OP241-2024, title: "Florida Bar Ethics Opinion 24-1 (text as reproduced by Ezel)", publisher: "The Florida Bar, Professional Ethics Committee (mirror: ezel.ai)", type: professional-body, url: "https://ezel.ai/ethics-opinions/flbar/24-1-generative-ai-in-law-practice", date: 2024-01-19, access: full, locator: "sections on prospective clients and 'Lawyer Advertising'" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)", publisher: "State Bar of California, COPRAC", type: professional-body, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "Executive Summary p. 2 (autonomously facilitating client intake given as an agentic example)" }
    - { ref: AIACT-ART50, title: "Article 50: Transparency Obligations for Providers and Deployers of Certain AI Systems (AI Act Explorer)", publisher: "Future of Life Institute, EU Artificial Intelligence Act explorer", type: regulator, url: "https://artificialintelligenceact.eu/article/50/", date: 2024-06, access: full, locator: "paragraph 1" }
    - { ref: NYCBAR-OP2024-5, title: "Formal Opinion 2024-5: Generative AI in the Practice of Law", publisher: "New York City Bar Association", type: professional-body, url: "https://www.nycbar.org/reports/formal-opinion-2024-5-generative-ai-in-the-practice-of-law/", date: 2024-08-07, access: full, locator: "rules list (7.1 and 7.3 named)" }
  last_reviewed: 2026-10-19
  notes: "Grade C is the closest fit: bar bodies describe intake chatbots as in use (the Oregon opinion says there are far more chatbots without agents than with them) but no named firm deployment, vendor claim or measured result was found. Maturity is emerging because no named organisation is attached. The Oregon opinion cites ABA Formal Opinion 506 (human intake staff) through the WSBA summary, which was not read. Pennsylvania and Philadelphia joint opinion 2024-200 (cited by Oregon on unauthorised practice) could not be opened."

- id: professional-services-client-development-14
  title: Agent-run outbound BD sequences (autonomous drafting, scheduling and sending to clients and prospects)
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [client-interaction, document-production]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "Partners do not follow up consistently, and BD teams are asked to do more outreach with the same people."
  solution: "An agent chooses contacts, drafts messages and schedules or sends them within defined limits, escalating replies to a person. Idea: practitioners describe BD as a low-stakes place to start agentic experiments."
  outcomes:
    - { lever: growth, description: "none published", figure: "none published", measures: "not applicable. Survey expectation only: respondents expecting to run AI-driven BD rises from 8 to 40 of 123 over 18-24 months", provenance: vendor-published, source_ref: INTROHIVE-LAWSITES-2026 }
  prerequisites:
    - "Accurate relationship data and permissions (INTROHIVE-LAWSITES-2026)"
    - "A defined limit on what the agent may send without review: California bars autonomous external transmission of client information without safeguards and human review, and Oregon calls it prudent to subject autonomous actions to lawyer approval (CALBAR-GENAI-2026, p. 6; OSB-FO-2026-208, section III.D)"
  risks_and_guardrails:
    - "A lawyer must not deploy an agentic AI system so that it autonomously transmits client information externally, including automated communications, without safeguards and human review (CALBAR-GENAI-2026, p. 6)"
    - "Lawyers must not let agentic systems communicate legal advice or act in a representative capacity without meaningful supervision (CALBAR-GENAI-2026, Executive Summary, p. 2)"
    - "An agent could send an engagement letter on its own, which a prospect could read as forming a relationship (OSB-FO-2026-208, introduction to AI agents)"
    - "In the US, AI-generated voices fall under the Telephone Consumer Protection Act and generally require the called party's prior express consent (FCC-24-17, paragraph 2)"
    - "Law Society research says many solicitors confuse agentic AI with AI agents and that suppliers can distort expectations; it also says solicitors stay responsible for outputs they cannot fully audit (LAWSOC-AGENTIC-2026, key findings)"
    - "TRI forum panelists warned against assuming agents are smarter or more autonomous than they are (TRI-CMBDO-2026)"
  human_checkpoints:
    - "Partner approves the target list and message templates"
    - "Human review of replies and of any message that contains client information or advice"
  role_evolution: "BD professionals become supervisors of agent sequences; partners remain the voice of the relationship."
  evidence_grade: D
  sources:
    - { ref: INTROHIVE-LAWSITES-2026, title: "Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds", publisher: "LawSites (Bob Ambrogi)", type: press, url: "https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html", date: 2026-10-13, access: full, locator: "section 'Great Ambitions for AI and BD'" }
    - { ref: TRI-CMBDO-2026, title: "Chief Marketing & Business Development Officer Forum 2026: The most important aspect of AI may be talking to your clients about it", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai", date: 2026-02-18, access: full, locator: "paragraphs on agentic AI" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)", publisher: "State Bar of California, COPRAC", type: professional-body, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "Executive Summary p. 2; p. 6" }
    - { ref: OSB-FO-2026-208, title: "Formal Opinion No 2026-208: Chatbots and AI Agent Communications", publisher: "Oregon State Bar", type: professional-body, url: "https://www.osbar.org/_docs/ethics/2026-208.pdf", date: 2026-02, access: full, locator: "sections I and III.D" }
    - { ref: FCC-24-17, title: "Declaratory Ruling FCC 24-17: Implications of Artificial Intelligence Technologies on Protecting Consumers from Unwanted Robocalls and Robotexts", publisher: "Federal Communications Commission", type: regulator, url: "https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf", date: 2024-02-08, access: full, locator: "paragraphs 1-3" }
    - { ref: LAWSOC-AGENTIC-2026, title: "The future of agentic AI in legal practice", publisher: "The Law Society of England and Wales", type: professional-body, url: "https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice", date: 2026-04-14, access: full, locator: "'Summary of key findings'" }
  last_reviewed: 2026-10-19
  notes: "Idea (grade D). Discussed by TRI forum panelists (BD as a good place to experiment with agentic AI) and anticipated by Introhive survey respondents, but no firm was found running autonomous outbound BD. The FCC ruling is a consumer-protection rule on calls to consumers; its application to calls to business contacts at professional-services clients was not examined."

- id: professional-services-client-development-15
  title: Client feedback loop on AI-enabled service
  archetype: professional-services
  module: client-development
  function: sales-marketing-bd
  work_types: [data-reporting, client-interaction]
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Firms measure AI by hours saved. Clients judge on turnaround, transparency, risk identification and fees, and many firms hold little feedback on whether clients value AI-enabled work."
  solution: "Idea: firms ask clients about AI-enabled delivery (comfort by use, transparency, perceived value) through reviews and surveys, and use AI to summarise the feedback for account teams."
  outcomes:
    - { lever: experience, description: "Client attitudes to AI in law firms, qualitative only", figure: "none published for AI items", measures: "Survey of 642 UK clients fielded in the last quarter of 2025: the article says most perceive AI as a supportive tool, with unease about its use in case management and administration, and gives no percentages for AI items", provenance: vendor-published, source_ref: LFMC-SJ-2026 }
  prerequisites:
    - "Value metrics defined with clients: faster turnaround, better risk identification, consistency, client satisfaction, capacity for more strategic work (TRI-STANDOUT-2026, 'Turning strategy into systems')"
  risks_and_guardrails:
    - "Disclosing AI use can lower trust, so wording in feedback requests can shift answers (SCHILKE-OBHDP-2025)"
    - "Client information entered into AI tools engages confidentiality duties (CALBAR-GENAI-2026, p. 5)"
  human_checkpoints:
    - "Account lead reviews feedback summaries and decides follow-up with the client"
  role_evolution: "Client-experience or BD roles take on AI-specific feedback design; partners hear AI-related concerns directly."
  evidence_grade: D
  sources:
    - { ref: LFMC-SJ-2026, title: "Clients embracing AI use in law firms (reporting the Law Firm Marketing Club survey 'What Do Clients Want, Need and Expect? 2026')", publisher: "Solicitors Journal", type: press, url: "https://www.solicitorsjournal.com/sjarticle/clients-embracing-ai-use-in-law-firms", date: 2026-04-09, access: full, locator: "paragraphs 1-3" }
    - { ref: TRI-STANDOUT-2026, title: "Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice", date: 2026-08-06, access: full, locator: "'Moving to more value-based measurement'; Methodology" }
    - { ref: SCHILKE-OBHDP-2025, title: "The transparency dilemma: How AI disclosure erodes trust", publisher: "Organizational Behavior and Human Decision Processes, vol. 188 (Schilke and Reimann)", type: academic, url: "https://ideas.repec.org/a/eee/jobhdp/v188y2025ics0749597825000172.html", date: 2025, access: full, locator: "abstract" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)", publisher: "State Bar of California, COPRAC", type: professional-body, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05-14, access: full, locator: "p. 5" }
  last_reviewed: 2026-10-19
  notes: "Idea (grade D). The research and TRI discuss measuring client perception of AI-enabled service; AI summarisation of that feedback is the only proposed change and has no source. The Law Firm Marketing Club respondents are UK legal clients across firm types (the article does not say they are corporate buyers). The Stand-out Lawyers Survey is itself a client-nomination instrument but is not a feedback programme."

- id: professional-services-client-development-16
  title: In-house AI addendum to outside counsel guidelines, with disclosure, review, data-handling and audit rights, and AI criteria in panel reviews
  archetype: professional-services
  module: client-development
  function: procurement-supply-chain
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Existing outside counsel guidelines predate AI and give clients no control over which AI tools are used, how output is reviewed or what is disclosed."
  solution: "In-house legal teams add an AI addendum or section to their guidelines (permitted and prohibited tools, no training on client data, written consent for pass-through AI charges, human review, records, audit rights) and add AI questions to panel and performance reviews. Firms must read and act on these as account requirements."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable. Advice articles; no survey of how many clients have adopted AI addenda was found", provenance: vendor-published, source_ref: CONVENTUS-2026 }
  prerequisites:
    - "Legal-ops capacity: TRI says legal operations has become the default first line of defence for AI pressure on legal departments (TRI-LDOR-2026, key takeaways)"
    - "Making compliance with the addendum a condition of engagement, per the Louisville Bar article's first tip (LOUBAR-2025, Tip 1)"
  risks_and_guardrails:
    - "Advisers recommend that AI-generated content be reviewed and approved by a qualified lawyer before reaching the client, that client data not go to external AI systems without prior approval, and that firms keep records to answer how AI was used (CONVENTUS-2026)"
    - "The Louisville article says AI platform charges should pass through only with advance written consent, and AI training time should not be billed unless the client asked for something new and agreed in advance (LOUBAR-2025, billing paragraphs following Tip 3)"
    - "TRI reports that some clients still send 2023-style directives such as warranties that models are unbiased, alongside demands for savings (TRI-LEGALWEEK-2026)"
  human_checkpoints:
    - "Legal ops and the responsible lawyer decide which tools and uses are permitted for each firm"
    - "Periodic spot-checks of AI-assisted work product and billing (LOUBAR-2025, Tip 6)"
  role_evolution: "TRI says many legal operations leaders see their function shifting into its own practice area and becoming the default first line of defence for AI pressure (TRI-LDOR-2026, key takeaways)."
  evidence_grade: C
  sources:
    - { ref: CONVENTUS-2026, title: "How To Write Outside Counsel Guidelines That Govern AI-Assisted Work", publisher: "Conventus Law", type: vendor, url: "https://conventuslaw.com/report/how-to-write-outside-counsel-guidelines-that-govern-ai-assisted-work/", date: 2026-06-03, access: full, locator: "sections 'What Updated Guidelines Should Cover' and 'Connecting Guidelines to Matter Management'" }
    - { ref: LOUBAR-2025, title: "Navigating AI with Outside Counsel: Practical Tips for In-House Counsel", publisher: "Louisville Bar Association, Bar Briefs (Crosby and Lavanga)", type: professional-body, url: "https://www.loubar.org/wp-content/uploads/2025/12/Bar-Briefs_December25_Navigating-AI-with-Outside-Counsel_Crosby-and-Lavanga-1.pdf", date: 2025-12, access: full, locator: "Tips 1, 2, 3 and 6" }
    - { ref: TRI-LDOR-2026, title: "2026 Legal Department Operations Report", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/legal-department-operations-report-2026", date: 2026-09-22, access: full, locator: "key takeaways; Methodology" }
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "'The contradictions in the room'" }
    - { ref: EVERLAW-ACC-PR-2025, title: "64% of In-House Counsel Expect GenAI to Reduce Reliance on Outside Counsel, 50% Expect Lower Outside Counsel Costs, ACC/Everlaw Survey Finds (press release reprint)", publisher: "Everlaw and the Association of Corporate Counsel (via Business Wire)", type: survey, url: "https://markets.financialcontent.com/worldnow.ktul/article/bizwire-2025-10-14-64-of-in-house-counsel-expect-genai-to-reduce-reliance-on-outside-counsel-50-expect-lower-outside-counsel-costs-acceverlaw-survey-finds", date: 2025-10-14, access: full, locator: "paragraphs on outside counsel reliance and billing" }
  last_reviewed: 2026-10-19
  notes: "In-house: this entry is about the client's side. The Conventus article is from a legal-operations advisory business and the Louisville article is from a bar association's member magazine; neither is a measure of adoption. A compliance guide from Layer3 Labs seen in search results was opened but is a vendor guide and is not relied on. A Bloomberg Law article from 2023 (Cleary and Paul Weiss comments on disclosure) was only partly readable and is not used. The Louisville article cites Kentucky Bar Association opinion KBA E-457; that opinion was not opened."
```

---

## 3. Module notes

**Processes and key steps in this module (with work types)**

- Relationship capture and mapping from email, calendar and CRM data: data-reporting, research-synthesis (01).
- Opportunity identification and cross-sell, with independence and conflict checks: research-synthesis, expert-judgment (02).
- Account planning, client briefs and meeting preparation: document-production, research-synthesis (07).
- Client conversations, including AI value conversations and joint use-case work: client-interaction, expert-judgment (08, 09).
- Client terms: engagement letters, outside counsel guideline responses and AI consent: document-production, review-assurance (11, 16).
- Marketing, credentials and prospect intake: document-production, client-interaction (12, 13).
- Retention monitoring, feedback and BD return measurement: data-reporting (03, 04, 15).

**Common pain points**

- Relationship data sits in inboxes and is hard to act on: 78% of 123 surveyed partners say so (INTROHIVE-LAWSITES-2026). CRM adoption by partners has been negligible by the vendor CEO's account (same).
- Firms cannot answer the client question "how does AI save us money?": firm speakers at Legalweek said they were still gathering data (TRI-LEGALWEEK-2026). In-house respondents report no GenAI savings from law firms (59%) and 24% are satisfied with how outside counsel adopt GenAI for cost effectiveness (EVERLAW-ACC-PR-2025).
- Partners do not raise AI with clients (TRI-STANDOUT-2026), and clients send inconsistent signals, some demanding AI use and others restricting it (TRI-LEGALWEEK-2026).
- Strategy does not reach the desk: among professionals whose firm has a named AI strategy, 35% say day-to-day practice does not match it (TR-FOP-2026, key finding 04).

**Metrics and benchmarks (with sources)**

- Client expectation vs delivery: 78% say AI-enabled quality is very important or essential; 6% say most or all providers deliver; 32% have reconsidered or will within 12 months; one-third of those estimate more than $1M annual work at risk (TR-FOP-2026). Base for the corporate-client figures is not given on the report page.
- Strategy and ROI: firms with a GenAI strategy are 3.9 times more likely to achieve ROI; 22% of firms have one (TR speaker, TRI-LEGALWEEK-2026). In the Stand-out survey, 36% strongly agree their firm has a clear AI strategy and 25% strongly agree it has a plan for monetising AI use (TRI-STANDOUT-2026).
- BD measurement: 63% of firms lack a revenue-linked BD ROI measure; 15% have strong attribution (INTROHIVE-LAWSITES-2026). Maturity: 57% of firms at stage 1 or 2, 84% expect stage 3 or 4 within 18-24 months (same).
- Policy prevalence by firm size: formal GenAI policy 57% to 98%; client approval required 8% to 38%; GenAI tools marketed 2% to 52% (ILTA-TECHSURVEY-2026, Q3.18).
- In-house perspective: 64% expect to rely less on outside counsel and 50% expect lower outside counsel costs; GenAI active use rose to 52% from 23% (US respondents) (EVERLAW-ACC-PR-2025). TRI's legal ops report says the share of GCs naming technology as a strategic priority doubled between 2025 and 2026 (TRI-LDOR-2026).
- Rates context: TRI reports law firm rates rose faster than operating efficiency and warns that premium billing tied to AI is sustainable only if clients see value (TRI-SOTLM-2026, 2026-01-14; TRI-LEGALWEEK-2026 cites average rate growth above 7% in 2025).
- Independent quality evidence: none specific to client development was found. Adjacent only: randomised field experiments at a cross-border online retailer found GenAI increased sales in most workflows (no detectable impact to 16.3%), mainly through conversion (FANG-ARXIV-2026); a pre-registered trial with 133 patent lawyers found AI raised quality by 0.34 to 0.38 SD, funded and run by Google (NBER-AUTOR-2026). Both are adjacent processes, which caps any related grade at B.

**Guardrails and regulatory points**

- California (May 2026): supervision scales with autonomy; no autonomous external transmission of client information without safeguards and human review; hourly billing reflects actual time; follow client AI instructions (CALBAR-GENAI-2026, pp. 5-8).
- Oregon (Feb 2026): chatbots and AI agents for intake and marketing allowed, qualified; watch Rules 1.18, 5.3, 7.1 and 7.3(a); lawyer approval for autonomous actions (OSB-FO-2026-208).
- Florida 24-1 (Jan 2024): chatbot must say it is AI; no unverifiable superiority claims (FLBAR-OP241-2024).
- ABA Opinion 512 (July 2024) as summarised: disclosure when asked, when OCGs require it, when relevant to fees; boilerplate consent insufficient; no billing for general overhead (FMG-ABA512-2024; 2CIVILITY-ABA512-2024). The primary text could not be opened (ABA site returned 403).
- UK: SRA has no specific guidance on disclosure of AI use for client care; Law Society advises discussing and communicating AI use with the client (LAWSOC-GENAI-2026). SRA pages were blocked.
- Accounting: no federal law or professional standard specific to CPAs mandates disclosure of gen AI use; the Confidential Client Information Rule, IRC 7216 for tax data and independence rules for AI-related nonattest services apply (JOA-DISCLOSE-2025; JOA-ETHICS-2026).
- Consulting: ICMCI AI code (May 2026) covers marketing and BD, requires disclosure of material AI use, bars overstating AI expertise, and obliges consultants to follow client AI instructions (ICMCI-AICODE-2026).
- Consent to record: all-party consent jurisdictions; AI notetaker litigation (BLOOMBERGLAW-OTTER-2026).
- EU AI Act: Article 50 transparency duties apply from August 2026 per the Commission (EC-AIACT-2026; AIACT-ART50). US TCPA covers AI-generated voices (FCC-24-17).

**Frontier signals (dated and sourced)**

- 2026-10-13: Introhive survey: 84% of partners expect structured or AI-driven BD within 18-24 months, while 57% sit at basic data or visibility stages; Introhive's MCP server exposes relationship data to AI assistants under existing permissions (INTROHIVE-LAWSITES-2026).
- 2026-08-06: TRI's Stand-out survey says firms need a client AI conversation playbook and value metrics, not only efficiency metrics (TRI-STANDOUT-2026).
- 2026-05-14 and 2026-02: California and Oregon extend guidance to agentic AI and AI intake agents (CALBAR-ETHICS-2026; OSB-FO-2026-208).
- 2026-05: ICMCI v1.0 AI code for consultants, with a part on advising clients on AI (ICMCI-AICODE-2026).
- 2026-04-14: Law Society report says governance is moving toward statistical sampling of AI performance rather than checking every output, a departure from existing professional assumptions (LAWSOC-AGENTIC-2026).
- 2026-02-18: TRI forum panelists describe BD as a good starting point for agentic AI (TRI-CMBDO-2026).
- 2026-01-28: AI notetaking wiretap litigation (BLOOMBERGLAW-OTTER-2026).

**Workforce and role effects**

- Partners are the commercial transmission mechanism; embedded AI users are nine times more likely to report significant impact on efficiency and quality (TRI-STANDOUT-2026).
- Partners take on BD once handled by marketing staff (INTROHIVE-LAWSITES-2026). BD teams move to data governance and claim substantiation.
- Adjacent evidence on skill: in the patent-drafting trial, AI raised delivered quality, with larger gains among junior lawyers, and the study measured judgment without AI afterwards (NBER-AUTOR-2026, abstract). Not specific to BD.
- Retention of talent: 24% of professionals experiencing an AI value gap are considering leaving within two years (TR-FOP-2026).

**Objections and concerns practitioners raise**

- Clients want AI used but also want savings, and some will not pay for AI-done work (TRI-LEGALWEEK-2026).
- Disclosure may lower trust (SCHILKE-OBHDP-2025) while concealment is worse if discovered.
- Confidentiality across ethical walls and matters when AI reads firm-wide data (CALBAR-GENAI-2026; LOUBAR-2025).
- AI-generated briefs sound generic: panelists said briefs should guide, not script (TRI-CMBDO-2026).
- The Deloitte Australia refund after apparent AI-generated errors in a government report (CTV-DELOITTE-2025) shows that quality failures become a client-relationship cost: the department said Deloitte agreed to repay the final instalment, and a revised report disclosed use of Azure OpenAI. Deloitte said the matter was resolved directly with the client.

**Interview probes for an advisor**

1. For your five largest accounts, what do their engagement letters or outside counsel guidelines say about AI, and who in the firm tracks changes to those terms?
2. When did a partner last raise AI with a key client unprompted, and what evidence of what changed on the work did they bring?
3. Which relationship data does your firm collect automatically today, who can see it, and what is excluded (privileged matters, personal addresses, ethical walls)?
4. Do any AI tools send messages, emails or chatbot replies to clients or prospects without a person reading them first? Where does your firm draw that line?
5. How do you know whether your relationship or BD tools lead to revenue, and what would you accept as proof?

---

## 4. Routed to other modules

- **pursuit-proposals:** Florida and ICMCI limits on claims about AI expertise in proposals and credentials (FLBAR-OP241-2024; ICMCI-AICODE-2026); RFP response automation was not covered here.
- **scoping-pricing:** Stanford pricing framework and hybrid pricing (STANFORD-DEL-2026); clients refusing to pay for AI-done work and gain-sharing proposals (TRI-LEGALWEEK-2026); California rules on flat fees that build in AI savings (CALBAR-GENAI-2026, p. 8).
- **billing-collections:** line-item AI transparency on invoices, AI cost pass-through and no-markup rules (CALBAR-GENAI-2026, p. 8; LOUBAR-2025); Legora-Laurel time capture (landscape file).
- **quality-review:** the Deloitte Australia incident and AI-related review failures (CTV-DELOITTE-2025); NBER patent-drafting trial on quality and skill (NBER-AUTOR-2026).
- **acceptance-risk:** conflict-system entry of prospects reached through chatbots (OSB-FO-2026-208, section III.C); in-house intake products (Harvey, Legora Intake in the landscape file).
- **talent-learning:** partner AI fluency and training as the lever for client conversations (TRI-STANDOUT-2026; TRI-CMBDO-2026); mid-career retention risk (TR-FOP-2026).
- **firm-finance:** rate growth against AI savings, the AI-bubble warning and PE pressure on partners to generate pipeline (TRI-SOTLM-2026; INTROHIVE-LAWSITES-2026, 'A Complex Environment').

---

## 5. Sources

Each source was opened and read unless marked search-only. Types are the vocabulary values.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative AI in the Practice of Law (2026 revision) | State Bar of California, COPRAC | professional-body | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05-14 | full |
| CALBAR-ETHICS-2026 | Ethics and technology resources page (states the 2026-05-14 Board of Trustees approval) | State Bar of California | professional-body | https://www.calbar.ca.gov/Attorneys/Conduct-Discipline/Ethics/Ethics-Technology-Resources | 2026-05-14 | full |
| OSB-FO-2026-208 | Formal Opinion 2026-208: Chatbots and AI Agent Communications | Oregon State Bar | professional-body | https://www.osbar.org/_docs/ethics/2026-208.pdf | 2026-02 | full |
| WSBA-NWSIDEBAR-OSB-2026 | New Oregon State Bar Opinion on Using AI Agents for Client Intake | NWSidebar (WSBA), Mark Fucile | professional-body | https://nwsidebar.wsba.org/2026/03/23/new-oregon-state-bar-opinion-on-using-ai-agents-for-client-intake/ | 2026-03-23 | full |
| FLBAR-OP241-2024 | Florida Bar Ethics Opinion 24-1 (text on third-party mirror) | The Florida Bar via ezel.ai | professional-body | https://ezel.ai/ethics-opinions/flbar/24-1-generative-ai-in-law-practice | 2024-01-19 | full |
| FMG-ABA512-2024 | ABA Issues Formal Guidance for Lawyers' Use of Generative AI | FMG Law | firm | https://www.fmglaw.com/professional-liability/aba-issues-formal-guidance-for-lawyers-use-of-generative-ai/ | 2024-08-14 | full |
| 2CIVILITY-ABA512-2024 | Breaking Down ABA Guidance on Using GenAI in Legal Practice | Illinois Supreme Court Commission on Professionalism | professional-body | https://www.2civility.org/breaking-down-the-abas-guidance-on-using-Generative-ai-in-legal-practice/ | 2024-08-15 | full |
| ABA-OP512-2024 | ABA Formal Opinion 512: Generative Artificial Intelligence Tools (primary text) | American Bar Association | professional-body | https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf | 2024-07-29 | search-only (primary returned 403; content taken from FMG-ABA512-2024 and 2CIVILITY-ABA512-2024) |
| NYCBAR-OP2024-5 | Formal Opinion 2024-5: Generative AI in the Practice of Law | New York City Bar Association | professional-body | https://www.nycbar.org/reports/formal-opinion-2024-5-generative-ai-in-the-practice-of-law/ | 2024-08-07 | full (page text partial) |
| LAWSOC-GENAI-2026 | Generative AI: the essentials | Law Society of England and Wales | professional-body | https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials | 2026 | full (via text mirror) |
| LAWSOC-AGENTIC-2026 | The future of agentic AI in legal practice | Law Society of England and Wales | professional-body | https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice | 2026-04-14 | full (summary page via mirror) |
| JOA-DISCLOSE-2025 | Should I disclose my use of gen AI to clients? | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2025/apr/should-i-disclose-my-use-of-gen-ai-to-clients/ | 2025-04-01 | full |
| JOA-ETHICS-2026 | Accounting ethics in the age of AI | Journal of Accountancy (AICPA Professional Ethics Division) | professional-body | https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/ | 2026-08-05 | full |
| ICMCI-AICODE-2026 | Code of Responsible Use of AI for the Management Consulting Profession, v1.0 | ICMCI | professional-body | https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf | 2026-05 | full |
| LOUBAR-2025 | Navigating AI with Outside Counsel: Practical Tips for In-House Counsel | Louisville Bar Association | professional-body | https://www.loubar.org/wp-content/uploads/2025/12/Bar-Briefs_December25_Navigating-AI-with-Outside-Counsel_Crosby-and-Lavanga-1.pdf | 2025-12 | full |
| WOODARD-2025 | Future Ready Engagement Letters (webinar slides) | Woodard | firm | https://www.woodard.com/hubfs/Future_Ready_Engagement_Letters_Oct2025.pdf | 2025-10 | full |
| EC-AIACT-2026 | AI Act regulatory framework page | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10 | full |
| AIACT-ART50 | Article 50 transparency obligations (AI Act Explorer) | Future of Life Institute | regulator | https://artificialintelligenceact.eu/article/50/ | 2024-06 | full |
| FCC-24-17 | Declaratory Ruling: AI technologies and robocalls (TCPA) | Federal Communications Commission | regulator | https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf | 2024-02-08 | full |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026-06-22 | full |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice: 2026 Stand-out Lawyers Survey | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 | full |
| TRI-LDOR-2026 | 2026 Legal Department Operations Report | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/legal-department-operations-report-2026 | 2026-09-22 | full |
| TRI-SOTLM-2026 | State of the US Legal Market 2026 analysis (AI bubble) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble | 2026-01-14 | full |
| ILTA-TECHSURVEY-2026 | ILTA Technology Survey 2026 Executive Summary | ILTA | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 | full |
| EVERLAW-ACC-PR-2025 | ACC/Everlaw GenAI survey press release (reprint) | Everlaw and ACC via Business Wire | survey | https://markets.financialcontent.com/worldnow.ktul/article/bizwire-2025-10-14-64-of-in-house-counsel-expect-genai-to-reduce-reliance-on-outside-counsel-50-expect-lower-outside-counsel-costs-acceverlaw-survey-finds | 2025-10-14 | full |
| INTROHIVE-LAWSITES-2026 | Partners Want AI to Help Them Find New Business... Introhive Survey Finds | LawSites | press | https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html | 2026-10-13 | full |
| LFMC-SJ-2026 | Clients embracing AI use in law firms | Solicitors Journal | press | https://www.solicitorsjournal.com/sjarticle/clients-embracing-ai-use-in-law-firms | 2026-04-09 | full |
| BLOOMBERGLAW-OTTER-2026 | AI Notetaking Poses Wiretapping, Discovery, and Ethical Pitfalls | Bloomberg Law | press | https://news.bloomberglaw.com/ip-law/ai-notetaking-poses-wiretapping-discovery-and-ethical-pitfalls | 2026-01-28 | full |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors | AP via CTV News | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-CMBDO-2026 | CMBDO Forum 2026: The most important aspect of AI may be talking to your clients about it | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-talking-to-your-clients-about-ai | 2026-02-18 | full |
| SCHILKE-OBHDP-2025 | The transparency dilemma: How AI disclosure erodes trust | Organizational Behavior and Human Decision Processes (abstract via RePEc) | academic | https://ideas.repec.org/a/eee/jobhdp/v188y2025ics0749597825000172.html | 2025 | full (abstract) |
| SCHILKE-CONVERSATION-2025 | Being honest about using AI at work makes people trust you less | University of Arizona News (The Conversation) | academic | https://news.arizona.edu/employee-news/being-honest-about-using-ai-work-makes-people-trust-you-less-research-finds | 2025-05-29 | full |
| STANFORD-DEL-2026 | Pricing Consulting Services in the Age of Agentic AI | Stanford Digital Economy Lab | academic | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | 2026-08-23 | full |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? (NBER WP 35720) | NBER | academic | https://www.nber.org/papers/w35720 | 2026-09 (issue date; revised 2026-10) | full (abstract page) |
| FANG-ARXIV-2026 | Generative AI and Sales Productivity: Field Experiments in Online Retail | arXiv (Fang et al.) | academic | https://arxiv.org/abs/2510.12049 | 2026-06-29 (v6) | full (abstract) |
| INTROHIVE-HOME-2026 | Relationship Intelligence Platform home page | Introhive | vendor | https://www.introhive.com/ | 2026-09-27 (last modified) | full |
| INTROHIVE-PRIVACY-2024 | Ensuring Robust Corporate Data Privacy vs. Data Security | Introhive | vendor | https://www.introhive.com/data-privacy/ | 2024-05-15 | full |
| CERTINIA-VEDA-2026 | Certinia AI and Veda agents | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10 | full |
| CONVENTUS-2026 | How To Write Outside Counsel Guidelines That Govern AI-Assisted Work | Conventus Law | vendor | https://conventuslaw.com/report/how-to-write-outside-counsel-guidelines-that-govern-ai-assisted-work/ | 2026-06-03 | full |
| MCA-SURVEY-2026 | MCA Member Survey 2026 | Management Consultancies Association | professional-body | https://www.mca.org.uk/reports/mca-member-survey-2026 | 2026-01-20 | full (page only; no AI-governance content used) |
| ABA-LPM-MARKETING-2024 | Ethical Issues When Incorporating AI into Law Firm Marketing | ABA Law Practice Magazine | professional-body | https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2024/september-october-2024/ethical-issues-when-incorporating-ai-into-law-firm-marketing/ | 2024-09 | search-only (page returned 403) |
| ACC-FTI-CLO-2026 | ACC 2026 Chief Legal Officers Survey (press release, outside counsel data not seen) | ACC with FTI Consulting | survey | https://www.acc.com/about/newsroom/news/changing-c-suite-clos-grow-strategic-leadership-ai-and-global-uncertainty | 2026-01-29 | search-only |

Type counts for the 40 sources read in full: professional-body 14, survey 6, academic 5, press 4, vendor 4, regulator 3, firm 2, conference 2. Search-only: ABA-OP512-2024, ABA-LPM-MARKETING-2024, ACC-FTI-CLO-2026. The Florida text, the ABA Opinion 512 content and the Law Society pages were read through a third-party mirror, secondary summaries or a text mirror, and are marked above.

---

## 6. Gaps

- **ABA Formal Opinion 512 primary text and ABA Law Practice marketing article:** the ABA site returned 403; content was taken from FMG and 2Civility summaries. Opinion 506 (human intake) is cited only through a WSBA summary.
- **SRA guidance:** SRA pages are behind a bot challenge. The Law Society says the SRA has no specific guidance on disclosure of AI use for client care; the SRA's own risk outlook on AI could not be read.
- **Other state opinions on marketing and AI:** the Florida Bar page loaded without text (read on a mirror); Texas Opinion 705, DC 388, Pennsylvania and Philadelphia 2024-200 and North Carolina 2024 FEO 1 were not read for this module. No state opinion addressing AI-driven outbound solicitation or cross-selling was found.
- **Client AI terms:** no survey counting how many clients have AI addenda in outside counsel guidelines; the ACC/Everlaw press release is the only quantified client-side source, and the 2026 ACC CLO survey outside-counsel data was not seen. No example of a consulting or accounting client's AI procurement clause was found beyond the Deloitte Australia case; no Australian procurement rule change was confirmed.
- **Independent measurement:** no independent study of AI in key-account management, relationship intelligence, retention or client feedback in professional services; no error rate, override rate or parallel-run result for relationship tools, alerts or account-plan generation. All outcome figures found are vendor-published or survey-based preferences. No A-grade entry for this reason.
- **Consulting and accounting:** the governance material is dominated by law. Consulting evidence is limited to the ICMCI code, MCA's survey page (no AI-governance content) and the Deloitte case; AICPA's own Code text and guidance were read only through Journal of Accountancy articles. No consulting-firm key-account management governance was found.
- **Privacy law:** GDPR, UK GDPR and CCPA treatment of relationship intelligence (email metadata processed across a firm) rests on a vendor statement; no regulator or professional-body analysis of the practice was found. The ICO's AI guidance page was opened but contains nothing specific to this use.
- **Dates:** the Law Society essentials page has no update date (cited events to May 2026); the Certinia and EC pages are undated, so 2026-10 is the read date.
- **Enforcement:** no disciplinary action or regulator enforcement tied to AI in client development (intake chatbots, AI marketing claims) was found. The FTC and SEC pages on AI-washing could not be opened.
- **Paywalled or blocked:** TRI 2026 AI in Professional Services Report (cited only through TRI-CMBDO-2026), Harvard CLP, Intapp pages (blocked), HBS Dell'Acqua paper (403).

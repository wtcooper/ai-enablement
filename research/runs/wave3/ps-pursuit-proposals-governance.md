# Governance of AI in pursuit and proposals: professional services

Prepared 2026-10-19. Archetype: professional-services. Module: pursuit-proposals. Angle: governance and evidence (what constrains and measures the work). Public sources only; quotations are under 25 words.

## 1. Summary

**What the evidence says.** The rules governing AI in bids converge on one position: bidders may use AI, and they own the accuracy of what they submit, the confidentiality of the material they put into tools, and any disclosure a buyer asks for. UK central-government guidance says suppliers' use of AI "is not prohibited" in procurement and suggests optional, unscored disclosure questions (PPN-017-2025, para 9 and Annex B). California's solicitation clause requires disclosure of GenAI used in or as a deliverable, not of AI used to write the bid (CALDGS-SCM2302-2025). California's bar guidance, ABA Formal Opinion 512 and the SRA's August 2026 warning notice (read second-hand) add duties of verification, confidentiality (including prospective clients) and supervision that scale with autonomy (CALBAR-GENAI-2026; ABA-OP512-2024; JMW-SRA-2026). Enforcement for AI claims made to prospects exists in adjacent sectors (SEC-2024-36; FTC-AICOMPLY-2024).

**Measurement is the weak point.** Every bid-specific figure found is from a vendor-run survey. Loopio's 1,533-respondent survey reports 79% of teams used AI, 33 hours average per RFP (two hours faster than a year earlier), and an average win rate of 39%, down from 45%; respondents rarely list improved win rate as an AI benefit (17%), which Loopio says may mean teams are not measuring it (LOOPIO-TRENDS-2026). No independent error-rate, override-rate, parallel-run or inspection result for AI-drafted bids was found. The nearest independent evidence is adjacent: studies of an online labour platform find that tailored application text lost value as a signal once AI writing tools arrived (CUI-DIAS-YE-2025; GALDIN-SILBERT-2025), and legal research tools hallucinated 17-33% of the time in a preregistered test (STANFORD-MAGESH-2024).

**Clients are now a governance force.** ABA Law Practice says many RFPs now ask which AI tools firms use, how they are governed and what savings they produced (ABA-LPMRFP-2026). Thomson Reuters' 2026 survey reports 78% of corporate clients call AI-enabled quality improvements very important or essential while 6% say most or all providers deliver them (TR-FOP-2026). Firm speakers at Legalweek 2026 said they are still gathering the data clients ask for (TRI-LEGALWEEK-2026).

**Use cases found: 17.** Grades: A 0, B 1, C 7, D 9. No entry reaches grade A because no named organisation reports a measured outcome for AI in its own bids. The one B is capped because its measurements come from an adjacent process.

**Sources:** 39 listed; 33 opened and read, 6 search-only. Types read: academic 6, conference 1, firm 3, press 2, professional-body 4, regulator 9, survey 6, vendor 2.

## 2. Use cases

```yaml
- id: professional-services-pursuit-proposals-01
  title: Draft RFP, DDQ and proposal answers from an approved content library, with human review
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - document-production
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Bid teams answer rising volumes of RFPs from scattered past answers. Loopio's survey reports an average of 166 RFPs submitted in the last year (153 the year before), and 50% of respondents rank bandwidth as a top challenge. The same survey reports an average win rate of 39%, down from 45%.
  solution: AI retrieves approved past answers and drafts or adapts a response to each question; a named person checks facts before submission. In the Loopio survey 62% of teams use AI to generate specific answers and 52% to write a first draft.
  outcomes:
  - lever: speed
    description: Average time to complete an RFP response was 33 hours, two hours less than the year before. The report ties the small reduction to AI benefits but does not isolate AI's effect.
    figure: 33 hours per RFP (two hours faster than last year)
    measures: average hours teams reported spending on an RFP response from start to finish, survey of 1,533 respondents
    provenance: vendor-published
    source_ref: LOOPIO-TRENDS-2026
  - lever: speed
    description: Reduced response time is the most cited AI benefit; improved quality and consistency is second; improved win rate is cited far less.
    figure: 47% reduced response time; 40% improved quality and consistency; 17% improved win rate
    measures: share of survey respondents selecting each benefit of using AI in the RFP process (multiple answers allowed)
    provenance: vendor-published
    source_ref: LOOPIO-TRENDS-2026
  - lever: capacity
    description: A majority of surveyed proposal professionals say AI increased the volume of responses they can handle; a smaller share credit it with higher win rates and revenue.
    figure: 60% more volume; 35% higher win rates and revenue
    measures: share of 297 surveyed proposal professionals reporting each impact, as reported by IT Brief; the article does not state the base for the AI-using subgroup
    provenance: vendor-published
    source_ref: QORUSDOCS-ITBRIEF-2026
  prerequisites:
  - A current, approved answer library with named owners; Loopio reports that 69% of respondents use RFP software (LOOPIO-TRENDS-2026, Ch.5 p.63).
  - An AI tool whose terms prohibit training on inputs, and a list of approved tools (BIDLAB-2026, risk table and policy section).
  - A standing step to read each solicitation's AI and certification clauses at kickoff (BIDLAB-2026).
  risks_and_guardrails:
  - Loopio advises against feeding past RFPs, private answers or proprietary data into general AI tools (LOOPIO-TRENDS-2026, Ch.5 p.58).
  - UK procurement guidance warns that LLM content may include plausible but false statements, and its example disclosure question asks bidders to confirm AI-assisted tender responses were checked for accuracy (PPN-017-2025, para 15 and Annex B).
  - The same guidance states that suppliers' use of AI is not prohibited in the commercial process (PPN-017-2025, para 9); the Bid Lab article says clauses vary by solicitation and should be read in each one (BIDLAB-2026, section 'Do You Have to Disclose').
  - ABA Formal Opinion 512 says informed consent is needed before inputting information relating to a representation into a self-learning tool, that boilerplate in engagement letters is not enough, and that confidentiality duties extend to prospective clients (ABA-OP512-2024, pp.6-7).
  - An ABA Law Practice column calls drafting RFP responses on public LLMs that train on firm inputs an 'absolute no-no' and says every word should be checked for accuracy (ABA-LPMAI-2026, Cautions).
  human_checkpoints:
  - A named individual, not 'the team', traces every factual claim to a source before submission (BIDLAB-2026, internal AI policy section).
  - Lawyer or bid lead checks every word of the response, including past success stories, awards and biographies (ABA-LPMAI-2026, Cautions).
  role_evolution: Most surveyed teams are not replacing people with AI; 16% say they have replaced internal people resources and 16% external ones, while 32% say leadership expects new responsibilities and 42% expect better results (LOOPIO-TRENDS-2026, Ch.5 p.61). An ABA Law Practice column describes bid teams and partners spending time tailoring strategy instead of pasting boilerplate (ABA-LPMAI-2026, item 3).
  evidence_grade: C
  sources:
  - ref: LOOPIO-TRENDS-2026
    title: 2026 RFP Response Trends & Benchmarks Report
    publisher: Loopio, in partnership with APMP (data analysed by Qualtrics)
    type: survey
    url: https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf
    date: 2026-03
    access: full
    locator: Overview pp.5-8; Ch.5 pp.56-63
  - ref: QORUSDOCS-ITBRIEF-2026
    title: AI shapes RFP proposal teams as revenue pressure grows (reporting a QorusDocs benchmark survey)
    publisher: IT Brief UK
    type: press
    url: https://itbrief.co.uk/story/ai-shapes-rfp-proposal-teams-as-revenue-pressure-grows
    date: '2026-02-25'
    access: full
    locator: '''Automation uneven'' section'
  - ref: PPN-017-2025
    title: 'Procurement Policy Note 017: Improving transparency of AI use in procurement'
    publisher: UK Cabinet Office (GOV.UK; contact Crown Commercial Service)
    type: regulator
    url: https://assets.publishing.service.gov.uk/media/67af7ba0e270ceae39f9e279/PPN_017_Improving_transparency_of_AI_use_in_procurement.pdf
    date: '2025-02-17'
    access: full
    locator: para 9; para 15; Annex B
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.B Confidentiality pp.6-7
  - ref: ABA-LPMAI-2026
    title: Leveraging AI to Respond to Requests for Proposals (RFPs) (Marketing Column)
    publisher: ABA Law Practice magazine
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps
    date: 2026-03
    access: full
    locator: item 3; Cautions
  - ref: BIDLAB-2026
    title: 'Using AI RFP Solutions: Dos and Don''ts (AI and RFPs: Disclosure Rules, Risk and What You Certify)'
    publisher: The Bid Lab
    type: vendor
    url: https://thebidlab.com/learning-center/using-ai-rfp-solutions-dos-and-donts/
    date: 2026-08
    access: full
    locator: risk table; internal AI policy section
  last_reviewed: '2026-10-19'
  notes: 'Quality evidence: no independent error-rate, override-rate or parallel-run measurement of AI-drafted bid answers was found. The 39% versus 45% win-rate change is context from the same vendor survey, not an AI effect. Maturity ''in-production'' rests on survey data (79% of 1,533 teams used AI in 2025); no named user organisation appears in the sources read. Search-only and unverified: vendor pages (TRIBBLE-ACCURACY-2026) claim first-draft accuracy of 70-93% and 93% on a 973-question benchmark, with no methodology found. The ABA column''s claim that AI can produce a 70-80% complete first draft in minutes is unmeasured.'
- id: professional-services-pursuit-proposals-02
  title: Move proposal drafting from personal chatbots to governed, permissioned AI tools
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - document-production
  - review-assurance
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Proposal and BD staff reach for general chatbots that firms do not control. Content in bids (past RFPs, pricing, client details, solicitation material) is confidential or restricted, and regulators and buyers have said the user stays responsible for where it goes.
  solution: The firm provides approved tools with no-training terms and access controls, and bans pasting restricted material into others. Retrieval runs only over content the user is permitted to see.
  outcomes:
  - lever: risk
    description: Many bid teams still use general tools; fewer use AI inside RFP software.
    figure: 57% ChatGPT and 57% Microsoft Copilot (each); 43% RFP software with built-in AI, up from 33% a year earlier
    measures: share of survey respondents using each AI tool in their RFP process (multiple answers allowed), 1,533 respondents
    provenance: vendor-published
    source_ref: LOOPIO-TRENDS-2026
  - lever: risk
    description: Among partners already using AI for business development, most rely only on general-purpose tools.
    figure: 68% rely only on general-purpose tools; satisfaction 6.7 out of 10; 22% say their firm has a fully developed and implemented AI strategy
    measures: share of partners using AI for business development, among 123 partners surveyed (42 legal, 42 accounting, 39 other)
    provenance: vendor-published
    source_ref: INTROHIVE-LAWSITES-2026
  - lever: risk
    description: Two in five professionals who use AI at work lack tools that meet the report's three stated conditions.
    figure: 41%
    measures: share of professionals who use AI at work who report no access to tools that safeguard confidential data, ground outputs in authoritative content and give explainable reasoning, among 1,816 respondents
    provenance: vendor-published
    source_ref: TR-FOP-2026
  prerequisites:
  - An approved-tools list and a rule on what may never be pasted in (client data, pricing, NDA material, anything a solicitation marks restricted) (BIDLAB-2026, internal AI policy section).
  - Vendor terms that prohibit training on inputs (BIDLAB-2026, risk table).
  risks_and_guardrails:
  - California guidance says a lawyer must not input confidential client information into a tool with material confidentiality or security risk without informed consent, and that reasonable efforts require more than general marketing assurances (CALBAR-GENAI-2026, Duty of Confidentiality row, p.5).
  - UK guidance suggests buyers put proportionate controls in place so bidders do not use confidential tender documents as training data (PPN-017-2025, para 9).
  - A US funder bars its reviewers from uploading proposal content to non-approved generative AI tools, treating it as a breach of confidentiality (NSF-GENAI-2023, 'Use of generative AI by reviewers'). Bidders can expect similar handling rules in solicitations (BIDLAB-2026).
  - A law-firm commentary on the SRA's August 2026 warning notice suggests the decision to approve tools should sit with the firm, not individual fee earners; the SRA says it will take the notice into account in its regulatory functions (JMW-SRA-2026).
  - Loopio advises against putting anything confidential, such as past RFPs, into general AI tools (LOOPIO-TRENDS-2026, Ch.5 p.58).
  human_checkpoints:
  - The firm, not the individual, decides which tools are approved (JMW-SRA-2026, 'Client confidentiality' section).
  - Before upload, the user checks both the tool's terms and the solicitation's own handling rules (BIDLAB-2026, FAQ on putting a solicitation into an AI tool).
  role_evolution: Loopio reports that enterprise and mid-market teams are about 10 points more likely than small businesses to use AI, and suggests this is because they have software that lets them use AI without putting sensitive data at risk (LOOPIO-TRENDS-2026, Ch.5 p.56). Tool choice becomes a firm decision rather than an individual one (JMW-SRA-2026).
  evidence_grade: C
  sources:
  - ref: LOOPIO-TRENDS-2026
    title: 2026 RFP Response Trends & Benchmarks Report
    publisher: Loopio, in partnership with APMP (data analysed by Qualtrics)
    type: survey
    url: https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf
    date: 2026-03
    access: full
    locator: Ch.5 pp.56 and 58
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds
    publisher: LawSites (Robert Ambrogi), reporting an Introhive/Thinktiv survey
    type: survey
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: '''What Partners Say They Want'' and survey summary paragraphs'
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: '''Professionals are clear about what their AI tools must do'' paragraph'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: Duty of Confidentiality row, pp.5-6
  - ref: PPN-017-2025
    title: 'Procurement Policy Note 017: Improving transparency of AI use in procurement'
    publisher: UK Cabinet Office (GOV.UK; contact Crown Commercial Service)
    type: regulator
    url: https://assets.publishing.service.gov.uk/media/67af7ba0e270ceae39f9e279/PPN_017_Improving_transparency_of_AI_use_in_procurement.pdf
    date: '2025-02-17'
    access: full
    locator: para 9
  - ref: NSF-GENAI-2023
    title: 'Notice to Research Community: Use of Generative Artificial Intelligence Technology in the NSF Merit Review Process'
    publisher: U.S. National Science Foundation
    type: regulator
    url: https://www.nsf.gov/news/notice-to-the-research-community-on-ai
    date: '2023-12-14'
    access: full
    locator: '''Use of generative AI by reviewers in merit review'''
  - ref: JMW-SRA-2026
    title: 'SRA AI warning notice: What solicitors and law firms need to do now'
    publisher: JMW Solicitors
    type: firm
    url: https://www.jmw.co.uk/blog/regulatory-and-disciplinary-proceedings/sra-ai-warning-notice-what-solicitors-and-law-firms-need-to-do-now
    date: '2026-08-19'
    access: full
    locator: '''Client confidentiality, privilege and AI tools'''
  - ref: BIDLAB-2026
    title: 'Using AI RFP Solutions: Dos and Don''ts (AI and RFPs: Disclosure Rules, Risk and What You Certify)'
    publisher: The Bid Lab
    type: vendor
    url: https://thebidlab.com/learning-center/using-ai-rfp-solutions-dos-and-donts/
    date: 2026-08
    access: full
    locator: internal AI policy section; FAQ
  last_reviewed: '2026-10-19'
  notes: The Introhive figures cover partners' business development use in general, not proposal drafting. In-production status is survey-level. The SRA warning notice itself was not opened (site blocked); the 17 Aug 2026 date and content come from JMW-SRA-2026 and LGL-SRA-2026. LGL-SRA-2026 reports that the SRA received 42 reports related to potential misuse of AI between July 2025 and July 2026 (reports concern legal work, not bids).
- id: professional-services-pursuit-proposals-03
  title: Run an AI-assisted accuracy and quality check on proposals before submission
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Proposals assert facts about credentials, past performance, contract values, awards and staff that a buyer may rely on or test. AI drafting adds a risk of plausible but false content, and several buyers now ask bidders to confirm AI-assisted text was checked.
  solution: AI compares draft claims against source records and the solicitation, flags unsupported statements, and scores sections for quality before the human reviewer signs off. Loopio reports 38% of teams use AI to analyze proposal quality and 34% to ensure accurate responses.
  outcomes:
  - lever: quality
    description: Share of teams using AI for quality analysis and accuracy checks; top-performing teams are described as far more likely than average to use AI to analyze proposal quality and ensure accuracy (exact top-performer share not extracted).
    figure: 38% analyzing proposal quality; 34% ensuring accurate responses
    measures: share of 1,533 survey respondents selecting each AI use (multiple answers allowed); top performers defined as teams winning 50% or more of RFPs
    provenance: vendor-published
    source_ref: LOOPIO-TRENDS-2026
  - lever: quality
    description: Top performers (win rate of 50% or more) report spending slightly more time per RFP than average.
    figure: 35 hours versus 33 hours
    measures: average hours per RFP for top-performing teams versus all teams, survey respondents
    provenance: vendor-published
    source_ref: LOOPIO-TRENDS-2026
  prerequisites:
  - A system of record for credentials, past performance and contract values that the check can compare against (BIDLAB-2026 notes that a wrong contract value in a past-performance section is not excused by a model having produced it).
  - A named verifier for each factual claim (BIDLAB-2026).
  risks_and_guardrails:
  - UK guidance's example disclosure questions ask bidders to confirm that AI-assisted tender responses have been checked and verified for accuracy; the guidance says such questions are for information and should not be scored (PPN-017-2025, Annex B).
  - An ABA Law Practice column advises verifying success-story descriptions, awards and accolades, and checking that compiled biographies do not pull out-of-date information (ABA-LPMAI-2026, Cautions).
  - The SEC settled charges against two investment advisers (USD 400,000 in total penalties) for telling clients and prospective clients they used AI in ways they did not (SEC-2024-36). The FTC states that there is no AI exemption from existing law (FTC-AICOMPLY-2024). Pitch statements about the firm's own AI use need substantiation.
  - Independent measurement of hallucination in adjacent legal research tools found rates between 17% and 33% for the products tested (STANFORD-MAGESH-2024, abstract); no equivalent measurement for bid content was found.
  human_checkpoints:
  - Named person signs off each factual claim before submission (BIDLAB-2026).
  - Where a solicitation asks, the bidder confirms AI-assisted text was checked and verified (PPN-017-2025, Annex B).
  role_evolution: The reviewer's job shifts from reading for style to verifying claims against records. Loopio reports top performers track granular metrics such as section scores and cost per bid (LOOPIO-TRENDS-2026, Ch.3 p.39).
  evidence_grade: C
  sources:
  - ref: LOOPIO-TRENDS-2026
    title: 2026 RFP Response Trends & Benchmarks Report
    publisher: Loopio, in partnership with APMP (data analysed by Qualtrics)
    type: survey
    url: https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf
    date: 2026-03
    access: full
    locator: Ch.5 pp.57 and 67; Ch.7 p.83; Ch.3 p.39
  - ref: PPN-017-2025
    title: 'Procurement Policy Note 017: Improving transparency of AI use in procurement'
    publisher: UK Cabinet Office (GOV.UK; contact Crown Commercial Service)
    type: regulator
    url: https://assets.publishing.service.gov.uk/media/67af7ba0e270ceae39f9e279/PPN_017_Improving_transparency_of_AI_use_in_procurement.pdf
    date: '2025-02-17'
    access: full
    locator: Annex B
  - ref: ABA-LPMAI-2026
    title: Leveraging AI to Respond to Requests for Proposals (RFPs) (Marketing Column)
    publisher: ABA Law Practice magazine
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps
    date: 2026-03
    access: full
    locator: Cautions
  - ref: BIDLAB-2026
    title: 'Using AI RFP Solutions: Dos and Don''ts (AI and RFPs: Disclosure Rules, Risk and What You Certify)'
    publisher: The Bid Lab
    type: vendor
    url: https://thebidlab.com/learning-center/using-ai-rfp-solutions-dos-and-donts/
    date: 2026-08
    access: full
    locator: '''What Are You Certifying When You Submit?'''
  - ref: SEC-2024-36
    title: SEC Charges Two Investment Advisers with Making False and Misleading Statements About Their Use of Artificial Intelligence (press release 2024-36)
    publisher: U.S. Securities and Exchange Commission
    type: regulator
    url: https://www.sec.gov/newsroom/press-releases/2024-36
    date: '2024-03-18'
    access: full
    locator: press release body
  - ref: FTC-AICOMPLY-2024
    title: FTC Announces Crackdown on Deceptive AI Claims and Schemes (Operation AI Comply)
    publisher: U.S. Federal Trade Commission
    type: regulator
    url: https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes
    date: '2024-09-25'
    access: full
    locator: chair statement
  - ref: STANFORD-MAGESH-2024
    title: Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362)
    publisher: Magesh et al., Stanford RegLab and HAI
    type: academic
    url: https://arxiv.org/abs/2405.20362
    date: '2024-05-30'
    access: full
    locator: abstract
  last_reviewed: '2026-10-19'
  notes: The SEC and FTC items concern investment advisers and consumer schemes; they are cited as enforcement principles for AI claims made to prospective clients, not as rules for professional-services bids. The Stanford figure is adjacent (legal research tools, grade capped). No source documents a named firm running an automated claims-verification step against matter records.
- id: professional-services-pursuit-proposals-04
  title: Use a response agent inside the services platform that drafts bids from deal, delivery and finance data, within approval thresholds
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - document-production
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Bid content sits across CRM, project, resourcing and finance systems. Drafting from one platform's data could keep proposals consistent with delivery capacity, but agents that act on their own raise supervision duties.
  solution: A vendor lists an RFP Responder Agent (drafts tailored responses for RFPs and proposals) and a Deal Coach Agent among agents on a professional-services automation platform. The vendor says agents act within the permissions, approval thresholds and auditability an organisation requires.
  outcomes:
  - lever: capacity
    description: none published for the RFP Responder or Deal Coach agents
    figure: null
    measures: 'not applicable: product listing without customer outcomes for these agents'
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - A single governed data foundation across sales, delivery, customers and financials, which the vendor describes as the basis for its agents (CERTINIA-VEDA-2026).
  - Defined permissions and approval thresholds for what an agent may do or send (CERTINIA-VEDA-2026).
  risks_and_guardrails:
  - California guidance says the greater the autonomy of an AI system, the greater the oversight needed, and that agentic systems must not be deployed to act in a representative capacity without meaningful lawyer supervision (CALBAR-GENAI-2026, pp.2 and 5).
  - The same guidance says lawyers must not deploy agentic systems that permit autonomous external transmission of client information, such as automated communications or data transfers, without safeguards and human review (CALBAR-GENAI-2026, Duty of Confidentiality row, p.6).
  - Agentic tools with persistent access to email, document management and client files may expose information across matters (CALBAR-GENAI-2026, p.6).
  - The Bar Standards Board's guidance, as described by a law firm, treats AI use as outsourcing under which the barrister stays responsible for compliance (MONDAQ-BSB-2026).
  human_checkpoints:
  - Approval thresholds set by the organisation before an agent takes a step (CERTINIA-VEDA-2026).
  - Human review of any external communication or transmission of client information (CALBAR-GENAI-2026, p.6).
  role_evolution: Not described by the vendor. California guidance expects supervising lawyers to set clear policies, training and updates for agentic tools (CALBAR-GENAI-2026, Duty to Supervise row, p.7).
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Certinia Veda AI: agent team for professional services (product page)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: 2026-10
    access: full
    locator: '''Meet the Veda agent team'' (Sell); ''Agentic action, your way'''
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: pp.2, 5, 6, 7
  - ref: MONDAQ-BSB-2026
    title: The BSB Have Released AI Guidance. Should The SRA Follow Suit?
    publisher: 'Mondaq (contributor: PCB Byrne)'
    type: firm
    url: https://www.mondaq.com/the-bsb-have-released-ai-guidance-should-the-sra-follow-suit/1825730
    date: '2026-08-03'
    access: full
    locator: '''What Does the BSB Guidance Cover?'''
  last_reviewed: '2026-10-19'
  notes: Vendor product listing; no customer, figure or date for the specific agents. The California and BSB texts are written for lawyers; they are cited for the principle that supervision scales with autonomy. Ladder is set to augment because the vendor describes drafting, not autonomous submission.
- id: professional-services-pursuit-proposals-05
  title: Use AI to support bid/no-bid decisions with win-probability and cost-of-pursuit analysis
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - expert-judgment
  - data-reporting
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Teams respond to more RFPs while using go/no-go processes less. Loopio's survey reports go/no-go use at its lowest since 2021 although about three-quarters of teams still use some process, and an average win rate of 39% (45% a year earlier).
  solution: AI compares an incoming RFP with past bids, client history, win rates for similar matters and resource availability to estimate the chance of winning and the cost of pursuing, so leadership can decide. An ABA Law Practice column gives the example of an 8% win chance against USD 35,000 of partner time.
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: 'not applicable: idea discussed by practitioners or regulators, no measured outcome found'
    source_ref: ABA-LPMAI-2026
  prerequisites:
  - Complete and accurate history of past bids, outcomes and costs; the ABA column warns that incomplete or inaccurate data will skew win probabilities (ABA-LPMAI-2026, Cautions).
  risks_and_guardrails:
  - Past win data may be biased toward low-profit work, so leaders should know when to ignore it and pursue a new kind of growth (ABA-LPMAI-2026, Cautions).
  - No source tests AI-supported go/no-go against outcomes. Loopio reports that 81% of top performers use a go/no-go matrix, but it does not say the matrix is AI-driven (LOOPIO-TRENDS-2026, Ch.1 pp.17-20).
  human_checkpoints:
  - Leadership makes the go or no-go decision using the analysis as input (ABA-LPMAI-2026, item 4).
  role_evolution: Loopio finds top performers more likely to say they are seen as strategic contributors to deal strategy (60% versus 47% of the average) (LOOPIO-TRENDS-2026, Ch.7 pp.83-84). A selectivity role for bid managers is a plausible extension, but no source ties it to AI.
  evidence_grade: D
  sources:
  - ref: ABA-LPMAI-2026
    title: Leveraging AI to Respond to Requests for Proposals (RFPs) (Marketing Column)
    publisher: ABA Law Practice magazine
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps
    date: 2026-03
    access: full
    locator: item 4 (Bid/No-Bid Predictive Analysis); Cautions
  - ref: LOOPIO-TRENDS-2026
    title: 2026 RFP Response Trends & Benchmarks Report
    publisher: Loopio, in partnership with APMP (data analysed by Qualtrics)
    type: survey
    url: https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf
    date: 2026-03
    access: full
    locator: Ch.1 pp.17-20 (go/no-go shifts); Ch.7 pp.83-84
  - ref: CERTINIA-VEDA-2026
    title: 'Certinia Veda AI: agent team for professional services (product page)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: 2026-10
    access: full
    locator: Deal Coach Agent listing
  last_reviewed: '2026-10-19'
  notes: 'Idea: discussed by an ABA Law Practice column and implied by Loopio''s volume-versus-selectivity finding; no named deployment found. Certinia lists a Deal Coach Agent that guides sales strategy and recommends next steps; it does not say go/no-go.'
- id: professional-services-pursuit-proposals-06
  title: Link AI use to win rate and cost per bid through win/loss and proposal-performance analytics
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - research-synthesis
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: Teams adopt AI without measuring its effect on wins. Loopio notes teams do not list improved win rate as a key AI benefit, which may mean they are not measuring it. QorusDocs reports more than a quarter of respondents find it hard to measure proposal effectiveness. Introhive reports 63% of firms have no revenue-linked way to measure BD return on investment.
  solution: 'Tag each bid with how AI was used, capture outcome, advancement stage, section scores, cost and loss reasons, then analyse patterns to adjust content, pursuit choices and tool use. Pattern is ''other'': a metrics-to-insight loop.'
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: 'not applicable: idea discussed by practitioners or regulators, no measured outcome found'
    source_ref: LOOPIO-TRENDS-2026
  prerequisites:
  - Outcome and stage data per bid; 95% of Loopio respondents track success metrics, most often win rates, then bids submitted (LOOPIO-TRENDS-2026, Ch.3 p.39).
  - Granular process metrics such as section scores, speed and cost per bid, which top performers are more likely to track (LOOPIO-TRENDS-2026, Ch.3 p.39).
  risks_and_guardrails:
  - 'Respondent-reported loss reasons differ by seniority: associates more often blame price and competition, directors and above more often blame product fit (LOOPIO-TRENDS-2026, Ch.2 p.32), so loss data may need verification against buyer debriefs.'
  - Loopio says price has been the top reason teams give for losing since 2021 (Ch.2 p.31); self-reported reasons are not independent evidence.
  - Where bids touch buyer feedback or personal data, use is subject to the firm's privacy and confidentiality obligations (not addressed in the sources read).
  human_checkpoints:
  - Bid leadership reviews findings before changing content or pursuit rules (not described in a source; no deployment found).
  role_evolution: Loopio says teams should track how they use AI and how that translates into win rates, so they judge their AI strategy on data rather than feelings (LOOPIO-TRENDS-2026, Ch.5 p.59).
  evidence_grade: D
  sources:
  - ref: LOOPIO-TRENDS-2026
    title: 2026 RFP Response Trends & Benchmarks Report
    publisher: Loopio, in partnership with APMP (data analysed by Qualtrics)
    type: survey
    url: https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf
    date: 2026-03
    access: full
    locator: Ch.3 p.39; Ch.5 p.59; Ch.2 pp.27-32
  - ref: QORUSDOCS-ITBRIEF-2026
    title: AI shapes RFP proposal teams as revenue pressure grows (reporting a QorusDocs benchmark survey)
    publisher: IT Brief UK
    type: press
    url: https://itbrief.co.uk/story/ai-shapes-rfp-proposal-teams-as-revenue-pressure-grows
    date: '2026-02-25'
    access: full
    locator: '''Proof of value'' and ''Revenue gateway'' sections'
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds
    publisher: LawSites (Robert Ambrogi), reporting an Introhive/Thinktiv survey
    type: survey
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: '''Measuring Return'' section'
  last_reviewed: '2026-10-19'
  notes: 'Idea: practitioners and surveys document the measurement gap; no named organisation reports AI-linked win/loss analysis. Baselines for any future measure: Loopio average win rate 39% (45% prior), advancement rate 46% (54% prior) (Ch.2 pp.27-29); Introhive: 15% of firms can track BD revenue with strong attribution. No independent measurement of AI''s effect on win rates was found.'
- id: professional-services-pursuit-proposals-07
  title: Keep an AI-use register for bids and answer buyer disclosure questions consistently
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Buyers increasingly ask how AI was used in a bid or will be used in delivery, and the form of the ask varies. UK central government guidance offers optional disclosure questions; California requires a clause for GenAI deliverables; a US funder encourages proposers to say how AI was used; the Bid Lab says no general federal rule requires disclosure of AI used in drafting as of August 2026.
  solution: 'The bid team records, per bid, which AI tools touched which sections and what checks were done, and reuses a reviewed statement for disclosure questions, certifications and AI-in-delivery declarations. Pattern is ''other'': a compliance register.'
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: 'not applicable: idea discussed by practitioners or regulators, no measured outcome found'
    source_ref: PPN-017-2025
  prerequisites:
  - A kickoff step to read the solicitation's representations and certifications for AI clauses (BIDLAB-2026).
  - A record of what AI was used for, so an answer takes minutes rather than a reconstruction (BIDLAB-2026, internal AI policy section).
  risks_and_guardrails:
  - UK guidance says its example AI disclosure questions are for information and should not be scored, and that authorities should not discriminate between suppliers in using them; it also says authorities can still ask other relevant AI questions in award criteria if compliant with procurement law (PPN-017-2025, Annex B).
  - California's required clause says failure to report GenAI may result in disqualification; the clause covers GenAI provided as, or used to complete, a deliverable that materially impacts a State system, State risk or contract performance, not AI used to write the bid (CALDGS-SCM2302-2025).
  - A US funder 'encourages' proposers to indicate the extent of generative AI use and says proposers remain responsible for accuracy and authenticity (NSF-GENAI-2023, 'Use of generative AI in proposal preparation').
  - GSA published a draft clause on safeguarding government data in large language model systems for public comment on 2026-06-17; it concerns AI delivered under contract, and the notice says GSA is seeking feedback before any later deviation or formal rulemaking (FEDREG-GSA-2026, abstract).
  - An ABA Law Practice column says to disclose that AI gave some assistance, while noting some clients take restrictive views on AI use (ABA-LPMAI-2026, Cautions).
  human_checkpoints:
  - Bid lead reviews the disclosure answer against the register before submission (not described in a source; no deployment found).
  role_evolution: A compliance-owner role for bid managers is a plausible extension; Browne Jacobson notes buyers should not score AI-use answers and should plan for more tender volume and more clarification questions (BROWNEJACOBSON-AIPROC-2025, 'AI used for answering tender submissions').
  evidence_grade: D
  sources:
  - ref: PPN-017-2025
    title: 'Procurement Policy Note 017: Improving transparency of AI use in procurement'
    publisher: UK Cabinet Office (GOV.UK; contact Crown Commercial Service)
    type: regulator
    url: https://assets.publishing.service.gov.uk/media/67af7ba0e270ceae39f9e279/PPN_017_Improving_transparency_of_AI_use_in_procurement.pdf
    date: '2025-02-17'
    access: full
    locator: para 9; Annex B
  - ref: PPN-0224-2024
    title: 'Procurement Policy Note 02/24: Improving Transparency of AI use in Procurement'
    publisher: UK Cabinet Office (GOV.UK)
    type: regulator
    url: https://assets.publishing.service.gov.uk/media/66019771a6c0f7bb15ef9252/PPN_02_24_Improving_Transparency_of_AI_use_in_Procurement.pdf
    date: '2024-03-25'
    access: full
    locator: para 7 (predecessor text)
  - ref: CALDGS-SCM2302-2025
    title: State Contracting Manual, Solicitations - GenAI Requirements (section 2302)
    publisher: California Department of General Services
    type: regulator
    url: https://www.dgs.ca.gov/PD/Resources/SCM/TOC/23/2302
    date: 2025-02
    access: full
    locator: required solicitation language
  - ref: NSF-GENAI-2023
    title: 'Notice to Research Community: Use of Generative Artificial Intelligence Technology in the NSF Merit Review Process'
    publisher: U.S. National Science Foundation
    type: regulator
    url: https://www.nsf.gov/news/notice-to-the-research-community-on-ai
    date: '2023-12-14'
    access: full
    locator: '''Use of generative AI in proposal preparation'''
  - ref: FEDREG-GSA-2026
    title: General Services Acquisition Regulation; Acquisition of Information and Communication Technology; Notice of Listening Sessions and Request for Comments (FR doc. 2026-12205)
    publisher: U.S. General Services Administration (Federal Register)
    type: regulator
    url: https://www.federalregister.gov/documents/2026/06/17/2026-12205/general-services-acquisition-regulation-acquisition-of-information-and-communication-technology
    date: '2026-06-17'
    access: full
    locator: abstract
  - ref: BIDLAB-2026
    title: 'Using AI RFP Solutions: Dos and Don''ts (AI and RFPs: Disclosure Rules, Risk and What You Certify)'
    publisher: The Bid Lab
    type: vendor
    url: https://thebidlab.com/learning-center/using-ai-rfp-solutions-dos-and-donts/
    date: 2026-08
    access: full
    locator: '''Do You Have to Disclose That You Used AI?'''
  - ref: ABA-LPMAI-2026
    title: Leveraging AI to Respond to Requests for Proposals (RFPs) (Marketing Column)
    publisher: ABA Law Practice magazine
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps
    date: 2026-03
    access: full
    locator: Cautions
  - ref: BROWNEJACOBSON-AIPROC-2025
    title: Use of AI in public sector procurements
    publisher: Browne Jacobson
    type: firm
    url: https://www.brownejacobson.com/insights/use-of-ai-in-public-sector-procurements
    date: '2025-01-27'
    access: full
    locator: '''AI used for answering tender submissions'''
  last_reviewed: '2026-10-19'
  notes: 'Idea: the buyer requirements are documented (regulators), but no firm''s AI-use register or disclosure workflow was found. Search-only and unverified: a US Commerce framework collecting sample AI clauses from disclosure to prohibition, including one that deems a proposal non-compliant if AI tools are not disclosed (COMMERCE-FAIR-2026); a Vermont form requiring prior written approval for AI used to provide goods or services (VERMONT-AIDISCLOSURE-2025). I found no solicitation that bans drafting with AI outright.'
- id: professional-services-pursuit-proposals-08
  title: Show clients the AI-enabled value and savings in pitches and RFP responses, with matter-level evidence
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - client-interaction
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: 'Clients ask firms to prove AI savings. At Legalweek 2026 the question had moved from whether firms use AI to how it produces savings on specific matters, and firm panelists said they were still gathering data. Partners are not having these conversations: only about one-third of embedded AI partners have discussed AI with at least 60% of clients.'
  solution: 'Pitch teams build a client-specific account of what work will be faster, safer or more predictable because of AI, tied to tracked matter data and a proposed way to share value, instead of a tour of the firm''s tools. Pattern is ''other'': a value narrative with evidence.'
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: 'not applicable: idea discussed by practitioners or regulators, no measured outcome found'
    source_ref: TRI-LEGALWEEK-2026
  prerequisites:
  - 'Tracked matter-level data on time, cost and turnaround under AI (TRI-LEGALWEEK-2026: clients want matter-level proof; panelists said ROI measurement was still anecdotal).'
  - Approved language on AI risks and limits, client-specific insight and billing guidance for partners (TRI-STANDOUT-2026, 'Providing client conversation information').
  risks_and_guardrails:
  - Statements to prospective clients about AI use must be true; the SEC settled charges over false AI claims made to clients and prospects (SEC-2024-36).
  - California guidance says hourly billing must reflect time actually spent and flat fees may build in AI savings; matter-specific AI costs need disclosure and no markup without informed written consent (CALBAR-GENAI-2026, Charging row, p.8). Detail routed to billing-collections.
  - Some clients issue guidelines refusing to pay for services performed by AI, using firm adoption as leverage on cost (TRI-LEGALWEEK-2026, 'The contradictions in the room').
  - Thomson Reuters Institute reports that firms leading with price concessions before showing value can train clients to expect discounts (TRI-STANDOUT-2026, 'How to talk to clients about AI').
  human_checkpoints:
  - Partner and pricing lead agree the value-sharing position before it appears in a pitch (DLA Piper's AI head advised firms to lead the ROI conversation rather than wait for clients to set terms, per TRI-LEGALWEEK-2026).
  role_evolution: Thomson Reuters Institute says partners are the commercial transmission mechanism of a firm, and that firm leaders should give them talking points, client-specific insight and approved language (TRI-STANDOUT-2026, 'Providing client conversation information').
  evidence_grade: D
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: '''Proving AI''s path to saving clients money''; ''The contradictions in the room'''
  - ref: TRI-STANDOUT-2026
    title: 'Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice
    date: '2026-08-06'
    access: full
    locator: '''How to talk to clients about AI''; ''Providing client conversation information''; partner-role paragraph (''Partners are not just another user group'')'
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: '''Clients are already moving on'' section'
  - ref: EVERLAW-ACC-2025
    title: 64% of In-House Counsel Expect GenAI to Reduce Reliance on Outside Counsel, 50% Expect Lower Outside Counsel Costs, ACC/Everlaw Survey Finds
    publisher: Everlaw and Association of Corporate Counsel (press release)
    type: survey
    url: https://www.everlaw.com.au/press/release/acc-report-2025
    date: '2025-10-14'
    access: full
    locator: press release body
  - ref: ABA-LPMRFP-2026
    title: How AI Is Changing the Process of Law Firm Request for Proposals (RFP)
    publisher: ABA Law Practice magazine (Matthew Prinn and Katie Windmoeller)
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals
    date: 2026-07
    access: full
    locator: '''AI Questions Being Asked of Law Firms in RFPs'' (Cost, Pricing, and Client Value)'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: Charging for Work row, p.8
  - ref: SEC-2024-36
    title: SEC Charges Two Investment Advisers with Making False and Misleading Statements About Their Use of Artificial Intelligence (press release 2024-36)
    publisher: U.S. Securities and Exchange Commission
    type: regulator
    url: https://www.sec.gov/newsroom/press-releases/2024-36
    date: '2024-03-18'
    access: full
    locator: press release body
  last_reviewed: '2026-10-19'
  notes: 'Idea with strong demand-side evidence and no supplier-side deployment found. Demand figures (all vendor-published, client views): 78% of corporate clients say AI-enabled quality improvements from firms are very important or essential, while 6% say most or all providers deliver them, and 32% have reconsidered or will reconsider firm relationships within 12 months (TR-FOP-2026, 1,816 professionals; client subgroup size not stated in the sources read). In the ACC/Everlaw survey of 657 in-house professionals, 61% plan to push for change in how law firms deliver and price services using GenAI, 59% report no GenAI savings from firms yet, and 24% are satisfied with how outside counsel adopt GenAI for cost effectiveness (EVERLAW-ACC-2025). Thomson Reuters Institute''s Steven Petrie said firms with a GenAI strategy are 3.9 times more likely to achieve ROI and only 22% have one (TRI-LEGALWEEK-2026). In-house views are tagged in-house.'
- id: professional-services-pursuit-proposals-09
  title: Answer AI-governance questions and AI clauses in client RFPs and outside counsel guidelines from a maintained answer bank
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: An ABA Law Practice article says many RFPs now ask which AI tools a firm uses, how they are governed, whether client data trains models and what safeguards protect confidentiality. At Legalweek 2026 a DLA Piper speaker said firms receive both demands that AI be used to hit savings targets and directives that AI not be used without explicit permission.
  solution: Maintain a reviewed bank of answers on AI strategy, policies, tools in use, data handling, savings evidence and roadmap, and adapt it per RFP, flagging conflicts with a client's own guideline restrictions. Same drafting and review loop as other RFP answers.
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: 'not applicable: idea discussed by practitioners or regulators, no measured outcome found'
    source_ref: ABA-LPMRFP-2026
  prerequisites:
  - 'A written firm AI policy and approved-tools list that the answers can cite (California guidance expects managerial lawyers to establish clear AI policies and training: CALBAR-GENAI-2026, Duty to Supervise row, p.7).'
  - A way to know which clients' guidelines restrict or require disclosure of AI use, because lawyers must disclose AI practices where those guidelines require it (ABA-OP512-2024, p.8).
  risks_and_guardrails:
  - A lawyer must follow client instructions or guidelines that restrict AI use (CALBAR-GENAI-2026, Communication row, p.7).
  - ABA Formal Opinion 512 says lawyers must disclose AI practices if asked by a client or if the engagement agreement or the client's outside counsel guidelines require it (ABA-OP512-2024, p.8).
  - Answers that overstate AI capability or controls could mislead; see SEC and FTC principles on AI claims (SEC-2024-36; FTC-AICOMPLY-2024).
  - ABA Formal Opinion 512 also flags Model Rule 7.1 (communications about a lawyer's services) as an area where further AI issues may arise (ABA-OP512-2024, p.2 n.4).
  human_checkpoints:
  - Practice or firm leadership reviews answers on governance, data handling and savings claims before they go to a client (not described in a source; no deployment found).
  role_evolution: An ABA article says responding well requires explaining how technologies are integrated into legal workflows, not listing tools (ABA-LPMRFP-2026, 'AI Questions Being Asked of Law Firms in RFPs').
  evidence_grade: D
  sources:
  - ref: ABA-LPMRFP-2026
    title: How AI Is Changing the Process of Law Firm Request for Proposals (RFP)
    publisher: ABA Law Practice magazine (Matthew Prinn and Katie Windmoeller)
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals
    date: 2026-07
    access: full
    locator: '''AI Questions Being Asked of Law Firms in RFPs'''
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: '''The contradictions in the room'''
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: p.2 n.4; p.8 (Communication)
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: Communication row, p.7; Duty to Supervise row, p.7
  - ref: SEC-2024-36
    title: SEC Charges Two Investment Advisers with Making False and Misleading Statements About Their Use of Artificial Intelligence (press release 2024-36)
    publisher: U.S. Securities and Exchange Commission
    type: regulator
    url: https://www.sec.gov/newsroom/press-releases/2024-36
    date: '2024-03-18'
    access: full
    locator: press release body
  - ref: FTC-AICOMPLY-2024
    title: FTC Announces Crackdown on Deceptive AI Claims and Schemes (Operation AI Comply)
    publisher: U.S. Federal Trade Commission
    type: regulator
    url: https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes
    date: '2024-09-25'
    access: full
    locator: chair statement
  last_reviewed: '2026-10-19'
  notes: 'Idea: the incoming questions are documented by a professional-body article and a named-speaker panel; no firm describes how it answers them. The ABA article also cites CLOC State of the Industry figures second-hand (85% of corporate legal departments report formal AI oversight; 27% use dedicated legal RFP tools); the CLOC report was not opened. Those are in-house figures. Loopio''s report covers DDQs and security questionnaires but does not give AI-governance questionnaire data.'
- id: professional-services-pursuit-proposals-10
  title: Tailor responses to each buyer's requirements with AI while keeping the proposal useful as a quality signal
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - document-production
  - client-interaction
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Tailoring to the buyer has been a costly signal of quality. Once AI makes tailored text cheap, buyers may stop treating tailoring as evidence of fit. In proposals, 41% of QorusDocs respondents already name personalisation as a pain point.
  solution: AI drafts text aligned to the posting or RFP; bidders spend the saved effort on editing, evidence and relationship-specific content, and buyers use other checks (clarifications, presentations, references) to test claims.
  outcomes:
  - lever: quality
    description: On an online labour platform that introduced an AI cover-letter tool, access raised textual alignment between cover letters and job posts and raised callback rates; time spent editing AI drafts was positively correlated with hiring success. After the tool, the correlation between alignment and callbacks fell by 51%, and employers shifted to other signals including work histories.
    figure: 51% fall in the correlation between alignment and callbacks
    measures: change in the correlation between cover-letter textual alignment and employer callbacks after the AI tool's introduction, difference-in-differences on platform application data
    provenance: independent
    source_ref: CUI-DIAS-YE-2025
  - lever: risk
    description: A structural model estimates that if written applications stop signalling ability, hiring becomes less meritocratic. This is a simulated counterfactual, not an observed outcome.
    figure: top-quintile workers hired 19% less often; bottom-quintile workers hired 14% more often
    measures: model-simulated change in hiring rates by ability quintile versus the pre-LLM equilibrium, Freelancer.com coding jobs
    provenance: independent
    source_ref: GALDIN-SILBERT-2025
  prerequisites:
  - 'Buyer-side checks that do not depend on tailored prose: clarification questions, supplier presentations, site visits or supporting documents (PPN-017-2025, para 9).'
  - Real client-specific input (relationships, values, context) that AI cannot supply from a library (ABA-LPMAI-2026, item 3).
  risks_and_guardrails:
  - UK guidance advises buyers to do additional due diligence on AI-assisted tenders using clarifications or supporting documents, as for any ambiguity (PPN-017-2025, para 9).
  - Browne Jacobson warns that if bidders feed AI similar criteria from the same invitation to tender, responses could become very similar or identical, so buyers need skilled evaluators and scoring that allows nuanced differences (BROWNEJACOBSON-AIPROC-2025, 'AI used for evaluation of tender submissions').
  - Employers cannot observe the effort behind a proposal, so tailored text works as a signal only while it is costly to produce (GALDIN-SILBERT-2025, introduction and model).
  human_checkpoints:
  - Bid lead or partner edits the draft for specific evidence and relationship content; the platform study found time spent editing correlated with hiring success (CUI-DIAS-YE-2025).
  role_evolution: Bid writers move from composing to editing and evidencing. Loopio says top performers spend about two hours more per RFP, which it links to personalisation and storytelling, though it presents that as likely rather than proven (LOOPIO-TRENDS-2026, Ch.7 p.83).
  evidence_grade: B
  sources:
  - ref: CUI-DIAS-YE-2025
    title: 'Signaling in the Age of AI: Evidence from Cover Letters (arXiv 2509.25054)'
    publisher: Jingyi Cui, Gabriel Dias, Justin Ye
    type: academic
    url: https://arxiv.org/abs/2509.25054
    date: '2025-09-29'
    access: full
    locator: abstract
  - ref: GALDIN-SILBERT-2025
    title: 'Making Talk Cheap: Generative AI and Labor Market Signaling (arXiv 2511.08785)'
    publisher: Anais Galdin and Jesse Silbert
    type: academic
    url: https://arxiv.org/abs/2511.08785
    date: '2025-11-11'
    access: full
    locator: abstract; introduction
  - ref: QORUSDOCS-ITBRIEF-2026
    title: AI shapes RFP proposal teams as revenue pressure grows (reporting a QorusDocs benchmark survey)
    publisher: IT Brief UK
    type: press
    url: https://itbrief.co.uk/story/ai-shapes-rfp-proposal-teams-as-revenue-pressure-grows
    date: '2026-02-25'
    access: full
    locator: '''Proof of value'' section (personalisation 41%)'
  - ref: LOOPIO-TRENDS-2026
    title: 2026 RFP Response Trends & Benchmarks Report
    publisher: Loopio, in partnership with APMP (data analysed by Qualtrics)
    type: survey
    url: https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf
    date: 2026-03
    access: full
    locator: Ch.7 p.83
  - ref: PPN-017-2025
    title: 'Procurement Policy Note 017: Improving transparency of AI use in procurement'
    publisher: UK Cabinet Office (GOV.UK; contact Crown Commercial Service)
    type: regulator
    url: https://assets.publishing.service.gov.uk/media/67af7ba0e270ceae39f9e279/PPN_017_Improving_transparency_of_AI_use_in_procurement.pdf
    date: '2025-02-17'
    access: full
    locator: para 9
  - ref: BROWNEJACOBSON-AIPROC-2025
    title: Use of AI in public sector procurements
    publisher: Browne Jacobson
    type: firm
    url: https://www.brownejacobson.com/insights/use-of-ai-in-public-sector-procurements
    date: '2025-01-27'
    access: full
    locator: '''AI used for evaluation of tender submissions'''
  - ref: ABA-LPMAI-2026
    title: Leveraging AI to Respond to Requests for Proposals (RFPs) (Marketing Column)
    publisher: ABA Law Practice magazine
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps
    date: 2026-03
    access: full
    locator: item 3
  last_reviewed: '2026-10-19'
  notes: 'Grade capped at B: the independent measurements come from adjacent processes (freelance coding job applications on an online labour platform, which introduced an AI proposal writer in April 2023 per GALDIN-SILBERT-2025), not professional-services RFPs. No equivalent study of professional-services bids was found.'
- id: professional-services-pursuit-proposals-11
  title: Extract requirements and build a compliance matrix from an RFP or tender pack
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - review-assurance
  - document-production
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Long RFPs hide mandatory clauses, deadlines and attachments (insurance, diversity metrics, security terms). Missing one can make a response non-compliant.
  solution: AI reads the solicitation, lists every requirement, deadline and mandatory clause as a structured matrix, and later cross-checks the drafted response against it.
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: 'not applicable: idea discussed by practitioners or regulators, no measured outcome found'
    source_ref: ABA-LPMAI-2026
  prerequisites:
  - 'Handling rules for solicitation material: the Bid Lab says some solicitation material carries restrictions on where it may be stored, so check the tool''s terms and the solicitation''s rules before upload (BIDLAB-2026, FAQ).'
  risks_and_guardrails:
  - UK guidance suggests controls so that bidders do not use confidential tender documents as training data for AI systems (PPN-017-2025, para 9).
  - Extraction can miss or misread clauses; an ABA column says every word of the response should be checked for accuracy (ABA-LPMAI-2026, Cautions).
  human_checkpoints:
  - Bid manager confirms the matrix against the source document before drafting (not described in a source; no deployment found).
  role_evolution: Bid coordinators spend less time on manual review of the pack (ABA-LPMAI-2026, item 1, describes this as a benefit).
  evidence_grade: D
  sources:
  - ref: ABA-LPMAI-2026
    title: Leveraging AI to Respond to Requests for Proposals (RFPs) (Marketing Column)
    publisher: ABA Law Practice magazine
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps
    date: 2026-03
    access: full
    locator: item 1 (Automated Review of the RFP and Requirement Extraction)
  - ref: BROWNEJACOBSON-AIPROC-2025
    title: Use of AI in public sector procurements
    publisher: Browne Jacobson
    type: firm
    url: https://www.brownejacobson.com/insights/use-of-ai-in-public-sector-procurements
    date: '2025-01-27'
    access: full
    locator: '''AI used for answering tender submissions'''
  - ref: PPN-017-2025
    title: 'Procurement Policy Note 017: Improving transparency of AI use in procurement'
    publisher: UK Cabinet Office (GOV.UK; contact Crown Commercial Service)
    type: regulator
    url: https://assets.publishing.service.gov.uk/media/67af7ba0e270ceae39f9e279/PPN_017_Improving_transparency_of_AI_use_in_procurement.pdf
    date: '2025-02-17'
    access: full
    locator: para 9
  - ref: BIDLAB-2026
    title: 'Using AI RFP Solutions: Dos and Don''ts (AI and RFPs: Disclosure Rules, Risk and What You Certify)'
    publisher: The Bid Lab
    type: vendor
    url: https://thebidlab.com/learning-center/using-ai-rfp-solutions-dos-and-donts/
    date: 2026-08
    access: full
    locator: FAQ on uploading a solicitation
  last_reviewed: '2026-10-19'
  notes: 'Idea: described by an ABA Law Practice column and by Browne Jacobson (AI could cross-reference tender requirements against drafted responses); no named deployment or measurement found.'
- id: professional-services-pursuit-proposals-12
  title: Prepare pitch briefs on the client, buyer and competing firms with AI over relationship and public data
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - research-synthesis
  - client-interaction
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Partners say the hardest parts of business development are knowing where to focus time (50%), making time (45%) and finding cross-sell (43%). Lawyers told Thomson Reuters Institute they need better client data and competitive intelligence for client conversations; the Institute calls this a preparation problem.
  solution: AI assembles a brief on the client's history with the firm, the matters rival firms handle for it, how it has rewarded work (price or expertise) and the people involved, from firm relationship data and public filings.
  outcomes:
  - lever: capacity
    description: Among partners already using AI for business development, most use only general-purpose tools and cannot give those tools the firm's relationship data.
    figure: 68% rely only on general-purpose tools; 78% of all partners say relationship data is hard to act on
    measures: '68%: share of partners using AI for business development among 123 surveyed partners; 78%: share of all surveyed partners saying relationship data at their firms is hard to act on'
    provenance: vendor-published
    source_ref: INTROHIVE-LAWSITES-2026
  prerequisites:
  - Accurate relationship data; Introhive's CEO said that if outputs are automated the data has to be accurate, because the old tolerance for some bounced emails no longer applies (INTROHIVE-LAWSITES-2026).
  - 'Permissions: Introhive says its connector lets assistants query relationship data subject to each user''s permissions and the firm''s governance policies (INTROHIVE-LAWSITES-2026, ''MCP and Agnostic Access to Data'').'
  risks_and_guardrails:
  - ABA Formal Opinion 512 says confidentiality duties extend to former and prospective clients' information (ABA-OP512-2024, p.6).
  - 63% of firms in the Introhive survey have no revenue-linked way to measure BD return on investment, so claimed gains are hard to verify (INTROHIVE-LAWSITES-2026, 'Measuring Return').
  human_checkpoints:
  - Partner reviews the brief before it shapes the pitch; Thomson Reuters Institute says the richest AI conversations come when lawyer and client jointly define how AI will be used (TRI-STANDOUT-2026).
  role_evolution: Introhive's CEO describes AI as a new interface that prompts partners to act, such as reminding them they have not spoken to a contact in 35 days (INTROHIVE-LAWSITES-2026). The survey is vendor-commissioned.
  evidence_grade: C
  sources:
  - ref: INTROHIVE-LAWSITES-2026
    title: Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds
    publisher: LawSites (Robert Ambrogi), reporting an Introhive/Thinktiv survey
    type: survey
    url: https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html
    date: '2026-10-13'
    access: full
    locator: survey summary; 'Measuring Return'; 'MCP and Agnostic Access to Data'
  - ref: TRI-STANDOUT-2026
    title: 'Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice
    date: '2026-08-06'
    access: full
    locator: '''How to talk to clients about AI'''
  - ref: ABA-LPMAI-2026
    title: Leveraging AI to Respond to Requests for Proposals (RFPs) (Marketing Column)
    publisher: ABA Law Practice magazine
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps
    date: 2026-03
    access: full
    locator: item 7 (Competitive Intelligence and Benchmarking)
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part II.B p.6
  last_reviewed: '2026-10-19'
  notes: Survey covers partners' business development in general (law, accounting, other), not pitch preparation specifically; no named firm deployment. Overlaps client-development (see routed items).
- id: professional-services-pursuit-proposals-13
  title: 'Buyer side: use AI to summarise, compare and screen law-firm and consultancy proposals'
  archetype: professional-services
  module: pursuit-proposals
  function: procurement-supply-chain
  work_types:
  - review-assurance
  - research-synthesis
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: As suppliers use AI to bid more often, contracting authorities and in-house legal teams face more and more similar responses without more evaluation capacity (in-house).
  solution: Buyers use AI to summarise submissions, extract staffing and pricing data, highlight differences between firms and suggest follow-up questions for panel interviews. An ABA Law Practice article describes this as beginning, with illustrative unnamed scenarios.
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: 'not applicable: idea discussed by practitioners or regulators, no measured outcome found'
    source_ref: ABA-LPMRFP-2026
  prerequisites:
  - Approved tools that keep submitted proposals confidential; NSF bars its reviewers from uploading proposals to non-approved generative AI tools (NSF-GENAI-2023).
  - Evaluators skilled in telling near-identical responses apart and a scoring method that allows for nuance (BROWNEJACOBSON-AIPROC-2025).
  risks_and_guardrails:
  - Browne Jacobson urges caution about using AI to create evaluation criteria, questions and scoring methods, and says human oversight remains essential (BROWNEJACOBSON-AIPROC-2025, 'AI used for the generation of tender documents').
  - UK guidance says buyers should plan for more clarification questions and tender responses, and may allow more time (PPN-017-2025, para 9).
  - NIH reported a researcher submitting more than 40 distinct applications in one round and now limits applicants to six per year and says it uses AI-detection technology (NIH-NOTOD25132-2025). This is a grant-funder analogue of volume control, not professional services.
  human_checkpoints:
  - Evaluators score and decide; UK guidance says its AI disclosure questions are not to be scored (PPN-017-2025, Annex B).
  role_evolution: Legal operations teams shift from reading narrative responses to reviewing structured comparisons (ABA-LPMRFP-2026, 'How Legal Departments Are Using AI in the RFP Process').
  evidence_grade: D
  sources:
  - ref: ABA-LPMRFP-2026
    title: How AI Is Changing the Process of Law Firm Request for Proposals (RFP)
    publisher: ABA Law Practice magazine (Matthew Prinn and Katie Windmoeller)
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals
    date: 2026-07
    access: full
    locator: '''How Legal Departments Are Using AI in the RFP Process'''
  - ref: BROWNEJACOBSON-AIPROC-2025
    title: Use of AI in public sector procurements
    publisher: Browne Jacobson
    type: firm
    url: https://www.brownejacobson.com/insights/use-of-ai-in-public-sector-procurements
    date: '2025-01-27'
    access: full
    locator: '''AI used for evaluation of tender submissions'''
  - ref: PPN-017-2025
    title: 'Procurement Policy Note 017: Improving transparency of AI use in procurement'
    publisher: UK Cabinet Office (GOV.UK; contact Crown Commercial Service)
    type: regulator
    url: https://assets.publishing.service.gov.uk/media/67af7ba0e270ceae39f9e279/PPN_017_Improving_transparency_of_AI_use_in_procurement.pdf
    date: '2025-02-17'
    access: full
    locator: para 9; Annex B
  - ref: NSF-GENAI-2023
    title: 'Notice to Research Community: Use of Generative Artificial Intelligence Technology in the NSF Merit Review Process'
    publisher: U.S. National Science Foundation
    type: regulator
    url: https://www.nsf.gov/news/notice-to-the-research-community-on-ai
    date: '2023-12-14'
    access: full
    locator: '''Use of generative AI by reviewers'''
  - ref: NIH-NOTOD25132-2025
    title: 'NOT-OD-25-132: Supporting Fairness and Originality in NIH Research Applications'
    publisher: U.S. National Institutes of Health
    type: regulator
    url: https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html
    date: '2025-07-17'
    access: full
    locator: Policy section
  - ref: LOOPIO-TRENDS-2026
    title: 2026 RFP Response Trends & Benchmarks Report
    publisher: Loopio, in partnership with APMP (data analysed by Qualtrics)
    type: survey
    url: https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf
    date: 2026-03
    access: full
    locator: Ch.1 pp.17-19 (68% receive more RFPs; Loopio speculates AI may help buyers send more)
  last_reviewed: '2026-10-19'
  notes: 'In-house / buyer-side. Idea: no named buyer deployment. The ABA article reports second-hand CLOC figures that 27% of legal departments use dedicated legal RFP tools and 46% run structured law-firm performance evaluations; not verified at source. Loopio speculates that AI may be helping procurement teams send more RFPs (68% of respondents report receiving more RFPs); that is not a measurement of buyer AI use.'
- id: professional-services-pursuit-proposals-14
  title: Design junior bid-writer development so AI drafting does not erode judgment
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - document-production
  - expert-judgment
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: If AI does the first draft, junior staff may lose the practice that builds judgment. A three-month randomised trial with patent lawyers found AI raised work quality, but the durable skill advantage went to seniors; juniors' scores bifurcated.
  solution: 'Treat junior learning as a design problem: structured exercises without AI, review of AI drafts against sources, and rotation through verification. Researchers raise this as an open question; no firm design for bids was found.'
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: 'not applicable: idea discussed by practitioners or regulators, no measured outcome found'
    source_ref: NBER-AUTOR-2026
  prerequisites:
  - Foundational expertise before AI use; the trial authors suggest foundational expertise may be a prerequisite for extracting durable skill from AI-assisted practice (NBER-AUTOR-2026, abstract).
  risks_and_guardrails:
  - In the trial, junior lawyers showed no average gain on an unaided task, with sharply fewer mediocre scores but more poor and more good ones (NBER-AUTOR-2026, abstract). Adjacent evidence (patent drafting); the result may not hold for bids.
  - Thomson Reuters Institute says newer professionals may find fewer opportunities to develop foundational experience in some AI scenarios (TR-FOP-2026, 'Elevate' trade-off).
  human_checkpoints:
  - Senior reviewers assess unaided and AI-assisted work separately (idea from the trial design, not a described practice; NBER-AUTOR-2026).
  role_evolution: Loopio reports associates are more likely than seniors to say AI has not changed their roles or workflows (LOOPIO-TRENDS-2026, Ch.5 pp.62-63), and 15% of teams use AI to onboard new team members (Ch.5 p.57).
  evidence_grade: D
  sources:
  - ref: NBER-AUTOR-2026
    title: Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER Working Paper 35720)
    publisher: Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere (NBER)
    type: academic
    url: https://econpapers.repec.org/RePEc:nbr:nberwo:35720
    date: 2026-09
    access: full
    locator: abstract
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: '''Elevate'' and ''Scale'' trade-offs; ''pipeline problem'' in conclusion'
  - ref: LOOPIO-TRENDS-2026
    title: 2026 RFP Response Trends & Benchmarks Report
    publisher: Loopio, in partnership with APMP (data analysed by Qualtrics)
    type: survey
    url: https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf
    date: 2026-03
    access: full
    locator: Ch.5 pp.57 and 62-63
  last_reviewed: '2026-10-19'
  notes: 'Idea discussed by researchers and Thomson Reuters Institute; no pursuit-specific measurement. NBER trial: 133 patent lawyers at 11 US firms; AI raised drafting quality by 0.34 SD at 10 days and 0.38 SD at 90 days; on an unaided redline task treated lawyers outperformed controls by 0.32 SD, concentrated in seniors (0.45 SD), with no average gain for juniors (abstract only; independent, adjacent). Routed to talent-learning for the full treatment.'
- id: professional-services-pursuit-proposals-15
  title: Draft executive summaries, win themes and consistent voice across multi-author proposals
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Proposals assembled by many authors read as inconsistent, and executive summaries and strategy sections take senior time. An ABA Law Practice column describes multi-partner RFPs as 'Frankenstein' documents.
  solution: AI drafts executive summaries, rewrites sections to a consistent voice and brand guidelines and suggests proposal strategy recommendations, which the bid lead edits. In the Loopio survey 39% use AI for executive summaries, 28% to follow brand and voice guidelines and 21% to suggest recommendations for proposal strategy.
  outcomes:
  - lever: quality
    description: On mid-level professional writing tasks in a preregistered online experiment, ChatGPT access reduced time taken and raised rated quality.
    figure: time down 0.8 SD; quality up 0.4 SD
    measures: difference between ChatGPT-exposed and control professionals on occupation-specific incentivised writing tasks, standard deviations, 444 college-educated professionals (working paper, March 2023)
    provenance: independent
    source_ref: NOY-ZHANG-2023
  - lever: quality
    description: Share of bid teams using AI for each narrative task.
    figure: 39% executive summaries; 28% brand and voice; 21% strategy recommendations
    measures: share of 1,533 survey respondents selecting each AI use (multiple answers allowed)
    provenance: vendor-published
    source_ref: LOOPIO-TRENDS-2026
  prerequisites:
  - Brand and voice guidelines and approved win themes the AI can follow (LOOPIO-TRENDS-2026, Ch.5 p.57 lists 'following brand and voice guidelines' as an AI use).
  risks_and_guardrails:
  - An ABA column says the final draft must be more than AI boilerplate (ABA-LPMAI-2026, Cautions).
  - If many bidders prompt AI with the same criteria, responses may converge (BROWNEJACOBSON-AIPROC-2025, 'AI used for evaluation of tender submissions'); a study of an online labour platform found the signal value of tailored text fell after AI writing tools arrived (CUI-DIAS-YE-2025).
  - The writing experiment found ChatGPT mostly substituted for worker effort rather than complementing skill and compressed differences between workers (NOY-ZHANG-2023, abstract).
  human_checkpoints:
  - Bid lead or partner edits executive summary and win themes before submission (ABA-LPMAI-2026, item 3 describes lawyers tailoring strategy and nuance).
  role_evolution: 'Teams that rely on AI more shift effort toward editing and idea generation: the writing experiment found tasks restructured toward idea generation and editing and away from rough drafting (NOY-ZHANG-2023, abstract).'
  evidence_grade: C
  sources:
  - ref: LOOPIO-TRENDS-2026
    title: 2026 RFP Response Trends & Benchmarks Report
    publisher: Loopio, in partnership with APMP (data analysed by Qualtrics)
    type: survey
    url: https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf
    date: 2026-03
    access: full
    locator: Ch.5 p.57
  - ref: ABA-LPMAI-2026
    title: Leveraging AI to Respond to Requests for Proposals (RFPs) (Marketing Column)
    publisher: ABA Law Practice magazine
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps
    date: 2026-03
    access: full
    locator: item 5; Cautions
  - ref: NOY-ZHANG-2023
    title: Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence (working paper)
    publisher: Shakked Noy and Whitney Zhang (MIT)
    type: academic
    url: https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1.pdf
    date: '2023-03-02'
    access: full
    locator: abstract
  - ref: BROWNEJACOBSON-AIPROC-2025
    title: Use of AI in public sector procurements
    publisher: Browne Jacobson
    type: firm
    url: https://www.brownejacobson.com/insights/use-of-ai-in-public-sector-procurements
    date: '2025-01-27'
    access: full
    locator: '''AI used for evaluation of tender submissions'''
  - ref: CUI-DIAS-YE-2025
    title: 'Signaling in the Age of AI: Evidence from Cover Letters (arXiv 2509.25054)'
    publisher: Jingyi Cui, Gabriel Dias, Justin Ye
    type: academic
    url: https://arxiv.org/abs/2509.25054
    date: '2025-09-29'
    access: full
    locator: abstract
  last_reviewed: '2026-10-19'
  notes: 'Grade C: the only bid-specific data are a vendor survey; the independent writing experiment is from 2023 and covers general professional writing, not proposals, so it would cap any grade at B.'
- id: professional-services-pursuit-proposals-16
  title: Flag deal-breaker terms in RFPs and outside counsel guidelines against standard firm terms before bidding
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - review-assurance
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Client outside counsel guidelines carry billing, staffing, data security, insurance and indemnity terms, and increasingly AI restrictions. Checking each by hand costs time before a bid.
  solution: AI cross-references a client's proposed guidelines or RFP terms against the firm's standard terms and produces a dashboard of which clauses are standard, which need review and which are potential deal-breakers (indemnity beyond the firm's control, insurance coverage).
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: 'not applicable: idea discussed by practitioners or regulators, no measured outcome found'
    source_ref: ABA-LPMAI-2026
  prerequisites:
  - A current statement of the firm's standard terms and AI policy to compare against (ABA-LPMAI-2026, item 6).
  risks_and_guardrails:
  - Guidelines may restrict or require disclosure of AI use; lawyers must follow client instructions that limit AI (CALBAR-GENAI-2026, p.7) and must disclose AI practices if a client's outside counsel guidelines require it (ABA-OP512-2024, p.8).
  - At Legalweek 2026 a DLA Piper speaker described directives demanding warrants that models are unbiased and declarations that firms cannot use AI without explicit permission (TRI-LEGALWEEK-2026, 'The contradictions in the room').
  - AI may misread indemnity or insurance wording; lawyer review of flagged and unflagged clauses is needed (consistent with CALBAR-GENAI-2026, p.4 on verifying outputs).
  human_checkpoints:
  - A lawyer reviews flagged clauses and decides whether to bid or negotiate (ABA-LPMAI-2026, item 6).
  role_evolution: Risk and general counsel staff review exceptions rather than read every guideline (inference from ABA-LPMAI-2026, item 6, which describes the dashboard but not role changes).
  evidence_grade: D
  sources:
  - ref: ABA-LPMAI-2026
    title: Leveraging AI to Respond to Requests for Proposals (RFPs) (Marketing Column)
    publisher: ABA Law Practice magazine
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps
    date: 2026-03
    access: full
    locator: item 6 (Compliance and Risk Flagging)
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: '''The contradictions in the room'''
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: p.8
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: Communication row, p.7; Competence row, p.4
  last_reviewed: '2026-10-19'
  notes: Idea described by an ABA Law Practice column; no named deployment found. Overlaps acceptance-risk (see routed items).
- id: professional-services-pursuit-proposals-17
  title: Retrieve credentials and matter experience from prior bids and matter records for each pitch
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types:
  - research-synthesis
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Teams must find the most relevant case studies, attorney or consultant biographies and matters for each industry or issue across document systems, and match them to the RFP's structure.
  solution: AI searches past successful bids, the firm's website and marketing content, and document-management systems for relevant practice descriptions, bios and matter experience, then formats them to the RFP's structure. An ABA article reports many firms review prior submissions and extract relevant experience this way.
  outcomes:
  - lever: capacity
    description: A report cited in an ABA article says some organisations using AI in proposal workflows reduced the manual effort of preparing proposals, so teams could pursue more opportunities without added staff.
    figure: 30-40% of manual effort (some organisations)
    measures: as reported in an ABA Law Practice article describing the Responsive/APMP 2025 State of Strategic Response Management Report; the article gives no sample size, base or definition of 'manual effort', and the report itself was not opened
    provenance: vendor-published
    source_ref: ABA-LPMRFP-2026
  prerequisites:
  - 'Organised experience data: AI can help extract matter descriptions and organise them to the RFP structure (ABA-LPMRFP-2026, ''How Law Firms Are Using AI in RFP Responses'').'
  - 'Client consent or clearance for credentials drawn from matter information (confidentiality duties extend to former and prospective clients: ABA-OP512-2024, p.6).'
  risks_and_guardrails:
  - ABA Formal Opinion 512 notes that using information developed in one representation to inform another may breach duties to current and former clients, citing a Pennsylvania joint opinion (ABA-OP512-2024, p.2 n.4).
  - California guidance warns that agentic systems with access to knowledge bases and client files may expose confidential material across matters (CALBAR-GENAI-2026, p.6).
  - An ABA column advises verifying success stories, awards and accolades, and that compiled biographies are current (ABA-LPMAI-2026, Cautions).
  - SEC and FTC action on AI-related claims shows the cost of overstating credentials or capabilities to prospects (SEC-2024-36; FTC-AICOMPLY-2024).
  human_checkpoints:
  - Lawyer or practice lead confirms each matter reference is accurate and cleared for use (ABA-LPMAI-2026, Cautions).
  role_evolution: Proposal teams spend less time searching and more time tailoring to the client's needs (ABA-LPMRFP-2026, 'How Law Firms Are Using AI in RFP Responses').
  evidence_grade: C
  sources:
  - ref: ABA-LPMRFP-2026
    title: How AI Is Changing the Process of Law Firm Request for Proposals (RFP)
    publisher: ABA Law Practice magazine (Matthew Prinn and Katie Windmoeller)
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals
    date: 2026-07
    access: full
    locator: '''How Law Firms Are Using AI in RFP Responses''; ''Real-World Scenarios'''
  - ref: ABA-LPMAI-2026
    title: Leveraging AI to Respond to Requests for Proposals (RFPs) (Marketing Column)
    publisher: ABA Law Practice magazine
    type: professional-body
    url: https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps
    date: 2026-03
    access: full
    locator: item 2; Cautions
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: p.2 n.4; p.6
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: Duty of Confidentiality row, p.6
  - ref: SEC-2024-36
    title: SEC Charges Two Investment Advisers with Making False and Misleading Statements About Their Use of Artificial Intelligence (press release 2024-36)
    publisher: U.S. Securities and Exchange Commission
    type: regulator
    url: https://www.sec.gov/newsroom/press-releases/2024-36
    date: '2024-03-18'
    access: full
    locator: press release body
  - ref: FTC-AICOMPLY-2024
    title: FTC Announces Crackdown on Deceptive AI Claims and Schemes (Operation AI Comply)
    publisher: U.S. Federal Trade Commission
    type: regulator
    url: https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes
    date: '2024-09-25'
    access: full
    locator: chair statement
  last_reviewed: '2026-10-19'
  notes: The 30-40% figure is second-hand through the ABA article and is a vendor survey; it is kept in an outcome of a grade C entry and should not be raised without opening the Responsive/APMP report. The ABA article's scenarios are illustrative and unnamed. No source in this angle reports credential-clearance workflows; the confidentiality points come from general guidance, not pitch-specific rules.
```

## 3. Module notes

### Processes and key steps (with work types)

- **Qualification and bid/no-bid:** decide whether to respond. Work types: expert-judgment, data-reporting. Loopio finds go/no-go use at its lowest since 2021 although about three-quarters of teams still use some process, and 81% of top performers use a go/no-go matrix (LOOPIO-TRENDS-2026, Ch.1 pp.17-20).
- **Solicitation intake and requirements analysis:** read the pack, list requirements, deadlines and mandatory terms. Work types: review-assurance, document-production (ABA-LPMAI-2026, item 1).
- **Content and credential retrieval; SME input:** find past answers, matters, biographies and case studies. Work types: research-synthesis, coordination-scheduling. QorusDocs respondents' top pain points were delays from subject matter experts (48%), time locating and maintaining content (46%) and meeting deadlines (42%) (QORUSDOCS-ITBRIEF-2026).
- **Drafting:** answers, executive summary, win themes, tailoring. Work type: document-production (LOOPIO-TRENDS-2026, Ch.5 p.57).
- **Pricing and staffing proposal:** expert-judgment. Routed to scoping-pricing.
- **Review and approval:** accuracy, compliance, partner or risk sign-off, certifications and representations. Work type: review-assurance (BIDLAB-2026).
- **Submission, clarifications, orals or pitch:** client-interaction, coordination-scheduling. UK guidance suggests buyers use clarifications and supplier presentations to test AI-assisted tenders (PPN-017-2025, para 9).
- **Debrief, win/loss and metrics:** data-reporting (LOOPIO-TRENDS-2026, Ch.3 p.39).

### Common pain points

- Bandwidth: 50% of Loopio respondents rank it a top challenge, for the first time in five years; submissions rose to an average of 166 from 153 (LOOPIO-TRENDS-2026, Overview pp.5-7).
- Capacity: most QorusDocs respondents say they cannot respond to 10-20% of incoming RFPs; 68% report year-on-year increases in proposals (QORUSDOCS-ITBRIEF-2026).
- Expectation inflation: 32% say leadership expects new responsibilities and 42% better results because of AI (LOOPIO-TRENDS-2026, Ch.5 p.61).
- Proving value: firms cannot give clients matter-level AI savings data (TRI-LEGALWEEK-2026); 63% of firms in the Introhive survey have no revenue-linked way to measure BD return on investment (INTROHIVE-LAWSITES-2026).
- Partners are not discussing AI with clients: about one-third of embedded AI partners have discussed it with at least 60% of clients (TRI-STANDOUT-2026).

### Metrics and benchmarks (all vendor-published unless stated)

| Metric | Value | What it measures | Source |
|---|---|---|---|
| Teams using generative AI in RFP workflows | 79% (68% prior year; 34% two years earlier per the chart) | share of 1,533 respondents using AI in the last 12 months | LOOPIO-TRENDS-2026, Ch.5 p.56 |
| Use AI to generate specific answers | 62% (46% prior year) | share selecting that use (multiple allowed) | LOOPIO-TRENDS-2026, Ch.5 p.57 |
| Average RFPs submitted a year | 166 (153 prior year) | average per team | LOOPIO-TRENDS-2026, Overview pp.6-7 |
| Average hours per RFP, start to finish | 33 (two hours faster than last year) | average reported time | LOOPIO-TRENDS-2026, Overview p.8 |
| Average win rate | 39% (45% prior year); UK 47%, North America 37% | average percentage of RFPs won, as reported | LOOPIO-TRENDS-2026, Ch.2 pp.27-29 |
| Advancement rate (shortlisted) | 46% (54% prior year) | percentage of RFPs shortlisted for next round | LOOPIO-TRENDS-2026, Ch.2 p.29 |
| Share of company revenue influenced by RFPs | 40% | average reported | LOOPIO-TRENDS-2026, Overview pp.6-7 |
| AI benefit: improved win rate | 17% (reduced time 47%; quality and consistency 40%) | share naming each benefit | LOOPIO-TRENDS-2026, Ch.5 p.59 |
| Respondents saying AI increased response volume handled | 60%; 35% credit higher win rates and revenue | 297 proposal professionals | QORUSDOCS-ITBRIEF-2026 |
| Corporate clients valuing AI-enabled quality improvements | 78% very important or essential; 6% say most or all providers deliver; 32% reconsidering firms | corporate clients in 1,816-professional survey | TR-FOP-2026 |
| In-house teams planning to push firms on delivery and pricing | 61%; 59% report no GenAI savings from firms yet | 657 in-house professionals (in-house) | EVERLAW-ACC-2025 |
| Hallucination in legal research AI (adjacent, independent) | 17-33% | frequency of hallucination for three tools in a preregistered test of legal research queries | STANFORD-MAGESH-2024 |
| Quality gain for patent drafting with AI (adjacent, independent) | 0.34 SD at 10 days, 0.38 SD at 90 days | blinded expert scoring, 133 lawyers | NBER-AUTOR-2026 |

Benchmarks absent: no source gives an error rate, override rate, rework rate or parallel-run result for AI-drafted proposals, and none gives an inspection outcome.

### Guardrails and regulatory points

- **Competence, confidentiality and supervision (law):** ABA Formal Opinion 512 requires understanding of tool limits and independent verification, informed consent before inputting client information into self-learning tools (boilerplate is not enough), and extends confidentiality to former and prospective clients (ABA-OP512-2024, pp.6-7). California's 2026 guidance adds agentic AI: more autonomy means more oversight, and no autonomous external transmission of client information without safeguards and human review (CALBAR-GENAI-2026, pp.2, 5-6). The SRA's 17 Aug 2026 warning notice stresses firm oversight and controls (JMW-SRA-2026; LGL-SRA-2026); the BSB published AI guidance on 18 May 2026 (MONDAQ-BSB-2026).
- **Communications and claims:** ABA Formal Opinion 512 flags Model Rule 7.1 as an area where further AI issues may arise (ABA-OP512-2024, p.2 n.4). The SEC settled charges (USD 400,000 total) for false AI claims to clients and prospects (SEC-2024-36); the FTC says there is no AI exemption from existing law (FTC-AICOMPLY-2024).
- **Client instructions:** lawyers must follow client guidelines that restrict AI (CALBAR-GENAI-2026, p.7) and disclose AI practices if a client's guidelines require it (ABA-OP512-2024, p.8).
- **Buyer disclosure rules:** UK PPN 017 (2025-02-17) says supplier AI use is not prohibited, suggests optional unscored disclosure questions and confidentiality controls (PPN-017-2025); California requires a clause on GenAI deliverables with possible disqualification for non-disclosure (CALDGS-SCM2302-2025); GSA published a draft LLM data-safeguarding clause for comment on 2026-06-17 (FEDREG-GSA-2026). The Bid Lab says no general federal rule requires disclosure of AI used in drafting as of August 2026 (BIDLAB-2026).
- **Evaluator-side analogues:** NSF bars reviewers from uploading proposals to non-approved generative AI tools and encourages proposers to say how AI was used (NSF-GENAI-2023); NIH will not consider applications substantially developed by AI and limits applicants to six a year (NIH-NOTOD25132-2025).
- **Billing interplay:** hourly billing must reflect time spent; flat fees may build in AI savings (CALBAR-GENAI-2026, p.8). Routed.

### Frontier signals (dated)

- 2026-10-13: Introhive/Thinktiv survey reports 84% of 123 partners expect to reach structured or AI-driven BD within 18-24 months, from 57% at the first two stages today (INTROHIVE-LAWSITES-2026).
- 2026-09: NBER trial finds AI raised drafting quality but durable skill gains concentrated in seniors (NBER-AUTOR-2026).
- 2026-08-17: SRA publishes a warning notice on misuse of AI; June 2026 supervision guidance expanded to AI (LGL-SRA-2026).
- 2026-08-06: Thomson Reuters Institute reports clients want firms to show AI capability and commercial impact (TRI-STANDOUT-2026).
- 2026-07: ABA Law Practice reports AI questions appearing in law-firm RFPs and legal departments starting to use AI to compare submissions (ABA-LPMRFP-2026).
- 2026-06-17: GSA draft clause on LLM data safeguarding for comment (FEDREG-GSA-2026).
- 2026-05-18: BSB guidance on AI for barristers (MONDAQ-BSB-2026).
- 2026-03: Loopio finds AI use by 79% of teams and a shift from editing toward generating answers (LOOPIO-TRENDS-2026).
- 2025-11-11: working paper models the loss of signal value in written applications (GALDIN-SILBERT-2025).
- 2025-07-17: NIH cites applicants using AI to submit more than 40 applications in a round and caps submissions (NIH-NOTOD25132-2025).
- Scheduled: Thomson Reuters Institute lists its 34th CMBDO Forum on 2027-01-27 (TRI-STANDOUT-2026, featured event); no programme content seen.
- Vendor: Certinia lists RFP Responder and Deal Coach agents within a platform agent team; undated product page, read 2026-10-19 (CERTINIA-VEDA-2026).

### Workforce and role effects

- Most Loopio respondents are not replacing people with AI; 16% say they replaced internal and 16% external people resources (LOOPIO-TRENDS-2026, Ch.5 p.61).
- Top performers (50% or more wins) have teams of ten versus eight on average (LOOPIO-TRENDS-2026, Ch.7 p.83).
- Seniors are more likely than associates to say AI changed expectations, and to have considered replacing roles with AI (LOOPIO-TRENDS-2026, Ch.5 pp.62-63).
- Junior development is an open risk: in the NBER trial juniors showed no average unaided gain (NBER-AUTOR-2026).
- Partners are the commercial channel for AI conversations with clients and need talking points and approved language (TRI-STANDOUT-2026).

### Objections and concerns practitioners raise

- Confidentiality: the Bid Lab and ABA Law Practice call feeding solicitation or firm content into public LLMs a data-handling risk or an 'absolute no-no' (BIDLAB-2026; ABA-LPMAI-2026).
- Accuracy: LLM text can be plausible but false; buyers may ask for confirmation of verification (PPN-017-2025, para 15, Annex B).
- Sameness and loss of signal: tailored responses may converge, and buyers may rely on other signals (BROWNEJACOBSON-AIPROC-2025; CUI-DIAS-YE-2025).
- Volume: more bids and more clarifications strain buyers (PPN-017-2025, para 9; NIH-NOTOD25132-2025).
- Clients will not pay for AI-done work or demand savings proof (TRI-LEGALWEEK-2026).
- Wins do not follow speed: AI benefits cited as time and quality, not win rate (LOOPIO-TRENDS-2026, Ch.5 p.59).
- Disclosure is inconsistent across buyers and some may disqualify for non-disclosure (CALDGS-SCM2302-2025; BIDLAB-2026).

### Interview probes for an advisor

1. Which AI tools do bid writers use today, who approved them, and has any past RFP, price or client content gone into a tool outside your contract terms?
2. When a tender or client RFP asks whether you used AI, or how you govern it, who answers, from what record, and has an answer ever cost you a bid or been challenged?
3. What do you track per bid (win rate, advancement, cost, section scores) and can you show whether AI-assisted bids win more or just go out faster?
4. Who verifies credentials, past-performance claims and AI-capability statements before a pitch goes out, what is the last error caught, and how are matter references cleared for confidentiality?
5. How are junior bid writers learning judgment now that AI drafts the first pass, and what do clients ask you to prove about AI savings?

## 4. Routed to other modules

- **client-development:** Introhive relationship-intelligence survey and MCP connector, partner BD maturity stages, 63% with no revenue-linked BD ROI measure (INTROHIVE-LAWSITES-2026); TRI finding that partners are not discussing AI with clients (TRI-STANDOUT-2026); Thomson Reuters CMBDO Forum 2027-01-27 (scheduled).
- **scoping-pricing:** Stanford framework mapping time-based, project, hybrid, subscription and outcome pricing, which says AI tends to push consulting toward hybrid and asset-based structures (STANFORD-DEL-2026); Certinia Estimate Creation and SOW Drafter agents (CERTINIA-VEDA-2026); AI-assisted fee modelling in proposals (ABA-LPMAI-2026, item 8; ABA-LPMRFP-2026).
- **billing-collections:** California fee rules (hourly billing must reflect time spent; AI costs and markup) (CALBAR-GENAI-2026, p.8); ABA Formal Opinion 512 fee guidance (ABA-OP512-2024); client line-item AI billing demands (TRI-LEGALWEEK-2026).
- **acceptance-risk:** conflict and confidentiality issues when matter information informs another representation (ABA-OP512-2024, p.2 n.4); outside counsel guideline terms review (use case 16 overlaps); GSA draft clause on LLM data in delivered services (FEDREG-GSA-2026); California GenAI deliverable disclosure (CALDGS-SCM2302-2025).
- **quality-review:** Deloitte Australia partial refund after apparent AI-generated errors in a government report (CTV-DELOITTE-2025, search-only); Stanford hallucination study (STANFORD-MAGESH-2024); SRA and BSB hallucination and supervision notices (JMW-SRA-2026; MONDAQ-BSB-2026).
- **talent-learning:** NBER patent-drafting trial on skill gains and juniors (NBER-AUTOR-2026); TR-FOP pipeline concerns (TR-FOP-2026).
- **In-house (buyer side), no separate module:** ACC/Everlaw findings that 64% of in-house respondents expect to rely less on outside counsel, and that only 9% report policies prohibiting GenAI, down from 29% (US respondents) (EVERLAW-ACC-2025); ABA's description of legal departments using AI to compare law-firm proposals (ABA-LPMRFP-2026), covered in use case 13.

## 5. Sources

Counts: 39 sources listed; 33 opened and read, 6 search-only. By type, read sources: academic 6, conference 1, firm 3, press 2, professional-body 4, regulator 9, survey 6, vendor 2. Search-only sources: AUTORFP-2026 (vendor), COMMERCE-FAIR-2026 (regulator), CTV-DELOITTE-2025 (press), SRA-WARNING-2026 (regulator), TRIBBLE-ACCURACY-2026 (vendor), VERMONT-AIDISCLOSURE-2025 (regulator).

| Ref | Title | Publisher | Type | URL | Date | Access | Note |
|---|---|---|---|---|---|---|---|
| ABA-LPMAI-2026 | Leveraging AI to Respond to Requests for Proposals (RFPs) (Marketing Column) | ABA Law Practice magazine | professional-body | https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps | 2026-03 | full | March/April 2026 issue; author byline not captured. Opened through the r.jina.ai mirror. Practitioner column, not a study. |
| ABA-LPMRFP-2026 | How AI Is Changing the Process of Law Firm Request for Proposals (RFP) | ABA Law Practice magazine (Matthew Prinn and Katie Windmoeller) | professional-body | https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals | 2026-07 | full | July/August 2026 issue. Opened through the r.jina.ai mirror. Cites CLOC State of the Industry and Responsive/APMP figures second-hand; scenarios are illustrative and unnamed. |
| ABA-OP512-2024 | Formal Opinion 512: Generative Artificial Intelligence Tools | American Bar Association, Standing Committee on Ethics and Professional Responsibility | professional-body | https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf | 2024-07-29 | full | Full text read from the LawNext-hosted copy of the PDF (americanbar.org returned HTTP 403). |
| AUTORFP-2026 | RFP Statistics: 47 Must-Know Benchmarks on Win Rates, Teams and Process (2026) | AutoRFP.ai | vendor | https://autorfp.ai/blog/rfp-statistics.md | 2026 | search-only | Seen only in search results. Vendor blog citing its own survey of 94 professionals. |
| BIDLAB-2026 | Using AI RFP Solutions: Dos and Don'ts (AI and RFPs: Disclosure Rules, Risk and What You Certify) | The Bid Lab | vendor | https://thebidlab.com/learning-center/using-ai-rfp-solutions-dos-and-donts/ | 2026-08 | full | Vendor learning-centre article; page metadata shows first published 2024-06-06 and modified 2026-08-26, and the text says 'as of August 2026'. Practitioner guidance, not a rule. |
| BROWNEJACOBSON-AIPROC-2025 | Use of AI in public sector procurements | Browne Jacobson | firm | https://www.brownejacobson.com/insights/use-of-ai-in-public-sector-procurements | 2025-01-27 | full | Law-firm commentary on PPN 02/24; covers AI in drafting tenders, answering tenders and evaluating tenders. |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023) | State Bar of California, Standing Committee on Professional Responsibility and Conduct | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05 | full | Document carries no printed date; PDF metadata creation date is 2026-05-15. Read in full (9 pages). |
| CALDGS-SCM2302-2025 | State Contracting Manual, Solicitations - GenAI Requirements (section 2302) | California Department of General Services | regulator | https://www.dgs.ca.gov/PD/Resources/SCM/TOC/23/2302 | 2025-02 | full | Page shows 'Revised: 02/2025'. The clause covers GenAI provided as, or used to complete, a deliverable; it does not address AI used to write the bid. |
| CERTINIA-VEDA-2026 | Certinia Veda AI: agent team for professional services (product page) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10 | full | Page undated; read 2026-10-19. Lists a Deal Coach Agent and an RFP Responder Agent. No customer outcomes for those agents on the page. |
| COMMERCE-FAIR-2026 | FAIR framework with sample AI clauses (appendix of sample solicitation language) | U.S. Department of Commerce | regulator | https://www.commerce.gov/sites/default/files/2026-05/FAIR%20Final.pdf | 2026-05 | search-only | Seen only in a search result (site returned HTTP 403). Date inferred from the URL path. Described there as sample clauses from disclosure to prohibition; not binding. |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors (AP) | CTV News (Associated Press) | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 | search-only | Page opened but article body not extractable; details come from search results. Delivery rather than pursuit; routed. |
| CUI-DIAS-YE-2025 | Signaling in the Age of AI: Evidence from Cover Letters (arXiv 2509.25054) | Jingyi Cui, Gabriel Dias, Justin Ye | academic | https://arxiv.org/abs/2509.25054 | 2025-09-29 | full | Version 2 dated 2025-11-12. Adjacent: online labour platform cover letters. |
| EVERLAW-ACC-2025 | 64% of In-House Counsel Expect GenAI to Reduce Reliance on Outside Counsel, 50% Expect Lower Outside Counsel Costs, ACC/Everlaw Survey Finds | Everlaw and Association of Corporate Counsel (press release) | survey | https://www.everlaw.com.au/press/release/acc-report-2025 | 2025-10-14 | full | 657 in-house legal professionals across 30 countries. Vendor-published press release (in-house). |
| FEDREG-GSA-2026 | General Services Acquisition Regulation; Acquisition of Information and Communication Technology; Notice of Listening Sessions and Request for Comments (FR doc. 2026-12205) | U.S. General Services Administration (Federal Register) | regulator | https://www.federalregister.gov/documents/2026/06/17/2026-12205/general-services-acquisition-regulation-acquisition-of-information-and-communication-technology | 2026-06-17 | full | Abstract and metadata read through the Federal Register API; full text page blocked. Concerns AI delivered under contract, not AI used to write bids. |
| FTC-AICOMPLY-2024 | FTC Announces Crackdown on Deceptive AI Claims and Schemes (Operation AI Comply) | U.S. Federal Trade Commission | regulator | https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes | 2024-09-25 | full | Consumer-facing actions; cited for the statement that there is no AI exemption from existing law. |
| GALDIN-SILBERT-2025 | Making Talk Cheap: Generative AI and Labor Market Signaling (arXiv 2511.08785) | Anais Galdin and Jesse Silbert | academic | https://arxiv.org/abs/2511.08785 | 2025-11-11 | full | Working paper using Freelancer.com data on written job applications ('proposals'). Adjacent: freelance coding marketplace. |
| INTROHIVE-LAWSITES-2026 | Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds | LawSites (Robert Ambrogi), reporting an Introhive/Thinktiv survey | survey | https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html | 2026-10-13 | full | 123 partners (42 legal, 42 accounting, 39 other). Vendor-commissioned. |
| JMW-SRA-2026 | SRA AI warning notice: What solicitors and law firms need to do now | JMW Solicitors | firm | https://www.jmw.co.uk/blog/regulatory-and-disciplinary-proceedings/sra-ai-warning-notice-what-solicitors-and-law-firms-need-to-do-now | 2026-08-19 | full | Law-firm commentary on the SRA warning notice published 2026-08-17. |
| LGL-SRA-2026 | Solicitors Regulation Authority highlights concern over AI-generated inaccuracies and breaches of confidentiality | Local Government Lawyer | press | https://www.localgovernmentlawyer.co.uk/marketplace/528-market-news/101456-solicitors-regulation-authority-highlights-concern-over-ai-generated-inaccuracies-and-breaches-of-confidentiality3 | 2026-08-17 | full | Reports the 42 reports figure and the June 2026 supervision guidance. |
| LOOPIO-TRENDS-2026 | 2026 RFP Response Trends & Benchmarks Report | Loopio, in partnership with APMP (data analysed by Qualtrics) | survey | https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf | 2026-03 | full | 44-page PDF, 1,533 respondents; PDF creation date 2026-03-10. Vendor-run survey; page numbers are the printed report pages. Chart values read from rendered pages 56-61. |
| MCA-SURVEY-2026 | MCA Member Survey 2026 | Management Consultancies Association | professional-body | https://www.mca.org.uk/reports/mca-member-survey-2026 | 2026-01 | full | Page metadata dated 2026-01-20. AI benefit figures are in graphics not captured as text; no pursuit or bid guidance found on the MCA site. |
| MONDAQ-BSB-2026 | The BSB Have Released AI Guidance. Should The SRA Follow Suit? | Mondaq (contributor: PCB Byrne) | firm | https://www.mondaq.com/the-bsb-have-released-ai-guidance-should-the-sra-follow-suit/1825730 | 2026-08-03 | full | Secondary account of Bar Standards Board guidance published 2026-05-18; BSB's own page not found. |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER Working Paper 35720) | Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere (NBER) | academic | https://econpapers.repec.org/RePEc:nbr:nberwo:35720 | 2026-09 | full | Abstract read through EconPapers (NBER full text restricted). Adjacent: patent drafting, not proposals. |
| NIH-NOTOD25132-2025 | NOT-OD-25-132: Supporting Fairness and Originality in NIH Research Applications | U.S. National Institutes of Health | regulator | https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html | 2025-07-17 | full | Funder (grant) proposals, not professional services. Cross-field analogue for volume and originality limits. |
| NOY-ZHANG-2023 | Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence (working paper) | Shakked Noy and Whitney Zhang (MIT) | academic | https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1.pdf | 2023-03-02 | full | Working paper, not peer reviewed at that date; outside the 18-month window. Adjacent: mid-level professional writing tasks. |
| NSF-GENAI-2023 | Notice to Research Community: Use of Generative Artificial Intelligence Technology in the NSF Merit Review Process | U.S. National Science Foundation | regulator | https://www.nsf.gov/news/notice-to-the-research-community-on-ai | 2023-12-14 | full | Funder (grant) proposals, not professional services. Cited as a cross-field analogue for how an evaluator governs AI in proposals. |
| PPN-017-2025 | Procurement Policy Note 017: Improving transparency of AI use in procurement | UK Cabinet Office (GOV.UK; contact Crown Commercial Service) | regulator | https://assets.publishing.service.gov.uk/media/67af7ba0e270ceae39f9e279/PPN_017_Improving_transparency_of_AI_use_in_procurement.pdf | 2025-02-17 | full | Update of PPN 02/24 for the Procurement Act 2023; says it is not a change in policy. Applies to central government; other contracting authorities may adopt it. |
| PPN-0224-2024 | Procurement Policy Note 02/24: Improving Transparency of AI use in Procurement | UK Cabinet Office (GOV.UK) | regulator | https://assets.publishing.service.gov.uk/media/66019771a6c0f7bb15ef9252/PPN_02_24_Improving_Transparency_of_AI_use_in_Procurement.pdf | 2024-03-25 | full | Predecessor of PPN-017-2025 for procurements commenced before 24 Feb 2025. |
| QORUSDOCS-ITBRIEF-2026 | AI shapes RFP proposal teams as revenue pressure grows (reporting a QorusDocs benchmark survey) | IT Brief UK | press | https://itbrief.co.uk/story/ai-shapes-rfp-proposal-teams-as-revenue-pressure-grows | 2026-02-25 | full | Press report of a vendor survey of 297 proposal professionals (26% professional services, 24% legal services). The QorusDocs report itself was not opened. |
| RESPONSIVE-APMP-2024 | Global Research sponsored by Responsive and APMP finds leading companies are 3x more likely to use AI-powered Strategic Response Management (2024 State of Strategic Response Management Report) | Responsive and APMP (press release via CXOToday) | survey | https://cxotoday.com/press-release/global-research-sponsored-by-responsive-and-apmp-finds-leading-companies-are-3x-more-likely-to-use-ai-powered-strategic-response-management-to-win-more-business/ | 2024-08-05 | full | Older than the 12-18 month window; used only as context. Vendor press release. |
| SEC-2024-36 | SEC Charges Two Investment Advisers with Making False and Misleading Statements About Their Use of Artificial Intelligence (press release 2024-36) | U.S. Securities and Exchange Commission | regulator | https://www.sec.gov/newsroom/press-releases/2024-36 | 2024-03-18 | full | Investment advisers; cited for the principle that claims about AI use made to prospective clients are enforceable. |
| SRA-WARNING-2026 | Warning notice: Misuse of AI | Solicitors Regulation Authority | regulator | https://www.sra.org.uk/ | 2026-08-17 | search-only | SRA site blocked by a bot challenge; exact page not opened. Content taken from two secondary reports (JMW-SRA-2026, LGL-SRA-2026), which are opened and cited instead. |
| STANFORD-DEL-2026 | Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives | Erik Brynjolfsson (Stanford Digital Economy Lab) and Georgios Petropoulos (USC) | academic | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | 2026-08-23 | full | Read the abstract and front matter; no pursuit or proposal content found. Routed to scoping-pricing. |
| STANFORD-MAGESH-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362) | Magesh et al., Stanford RegLab and HAI | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 | full | Abstract read (manuscript version of 2024-05-30). Adjacent: legal research, not proposals. |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 | full | Survey of 1,816 professionals in 62 countries, fielded March-April 2026. Launch date not confirmed; the page mirror shows a 2026-09-30 timestamp. |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full | Recap of three Thomson Reuters-sponsored Legalweek panels; speakers from GSK, Greenberg Traurig, Hogan Lovells, Ropes & Gray, DLA Piper, Zarwin Baum. |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 | full | 2,527 client-nominated stand-out lawyers and 116 law firm leader interviews. Page lists the 34th CMBDO Forum on 2027-01-27 as a featured event (scheduled). |
| TRIBBLE-ACCURACY-2026 | Vendor guides on RFP AI agent accuracy (Tribble content on a staging domain) | Tribble (vendor) | vendor | https://promenade-otu5q-commit-004cc0c.kinsta.page/blog/rfp-ai-agent-accuracy-ai-generated-responses/llms.md | 2026 | search-only | Seen only in search results; host not reachable through the proxy. Methodology for the accuracy claims could not be checked. |
| VERMONT-AIDISCLOSURE-2025 | AI Usage Disclosure form (2025 updates to purchasing and contracting forms) | State of Vermont, Buildings and General Services | regulator | https://bgs.vermont.gov/sites/bgs/files/files/purchasing-contracting/Forms/2025%20Updates/AI%20Usage%20Disclosure.docx | 2025 | search-only | Seen only in a search result; document not opened. Search summary says AI to provide goods or services needs prior written approval. |

## 6. Gaps

- **Independent quality evidence:** no independent error rate, override rate, parallel-run result, inspection finding or win-rate effect for AI-drafted bids was found in any source. Vendor accuracy claims (TRIBBLE-ACCURACY-2026) were seen in search results only; methodology not found.
- **Named deployments with measured outcomes:** none for pursuit and proposals in this angle. No named firm reports AI-linked win/loss analysis, claims verification, AI-use registers or AI-questionnaire answer banks.
- **Primary texts not opened:** the SRA warning notice (Cloudflare block; read through JMW-SRA-2026 and LGL-SRA-2026), the BSB guidance (via MONDAQ-BSB-2026), the full NBER paper (abstract only; NBER-AUTOR-2026), the Loopio-cited CLOC report and the Responsive/APMP 2025 report (second-hand through ABA-LPMRFP-2026), the Commerce Department sample clauses and the Vermont form (search-only), and the QorusDocs report (press report only).
- **Professional bodies:** AICPA and CIMA guidance pages and any accounting solicitation or advertising rules touching AI were not reached (AICPA landing page returned no usable text; CPA Ontario blocked); no AICPA-specific item is cited. The MCA site yielded a survey page whose AI figures are in graphics, and no MCA guidance on bids or AI. Florida Bar Opinion 24-1 and Texas Opinion 705 primary texts were not opened (the ABA opinion cites the Florida opinion on advertising and AI chatbots).
- **Client AI terms:** no survey of how many outside counsel guidelines restrict or require disclosure of AI; only anecdotes (TRI-LEGALWEEK-2026) and an ABA description (ABA-LPMRFP-2026). Consulting-client terms (for example procurement frameworks of large consulting buyers) not found.
- **Other jurisdictions:** no evaluation-side guidance found for AI scoring of tenders, detection of similar AI-generated bids, or Commonwealth of Australia, Canadian or EU procurement rules on bidder AI use. UK PPN 017 is the only government note on supplier AI use in bids found.
- **Advertising rules:** direct text of professional advertising and solicitation rules (for example ABA Model Rule 7.1, SRA marketing rules) was not read; the ABA opinion mentions Rule 7.1 only as a future AI issue.
- **Date gaps:** CalBar guidance carries no printed date (2026-05 inferred from file metadata); Thomson Reuters Future of Professionals launch date not confirmed; Certinia and some vendor pages are undated.
- **Search budget:** 12 web searches were used, on ABA, SRA, AICPA, procurement-clause, client-terms, bid-survey, academic and Australian-policy leads.

# Tax research and advisory: practice angle (wave 2 deep dive)

- **Archetype:** tax
- **Module:** research-advisory (technical research, memos, planning and advisory by firm advisers and in-house tax counsel; citation checking; M&A tax diligence)
- **Angle:** practice (what firms and in-house teams do: case studies, firm announcements, vendor deployments with named customers, product documentation, job postings, AI team structure)
- **Prepared:** 2026-10-17
- **Method:** Read the wave 2 landscape file and the vocabulary first. Opened vendor case studies, product pages, firm announcements, regulator and professional-body guidance, trade press, conference programmes, surveys and academic abstracts with `curl` (and the `r.jina.ai` mirror for one EY page). Web search was rationed and ran out partway through, so the later directions (independent accuracy tests, tax-practitioner sanctions, in-house case studies) were followed only through links from pages already read.

## 1. Summary

- **Use cases and evidence:** 18 candidate use cases. By grade: A: 3, B: 9, C: 3, D: 3. All 53 sources were opened in full. Every grade A entry rests on before-and-after time figures that named firms gave to the vendors that published them. None is independent.
- **The practice is concentrated in CPA and advisory firms using cited, tax-specific research assistants.** Named adopters in the sources include Sasserath & Co., Barnes Wendling, Finney Neill, Wright Ford Young, Crowe, SSC, Larson Gross and Harris, Hardy & Johnstone. Tool vendors in play are Blue J, Accordance and Thomson Reuters CoCounsel Tax, with Bloomberg Tax and CCH also named in the sources. The reported change is mainly speed: hours to minutes on single research tasks.
- **The strongest adoption numbers come from a vendor.** Blue J and CPA.com's March 2026 survey of 1,000 US accountants found 60% worked at firms that had adopted AI-powered tax research (33% in the 2025 edition, with a different sample) and 80% used AI for tax research weekly or monthly. The gap between those two figures is the sanctioned-versus-unsanctioned problem.
- **Quality evidence is thin and mostly self-reported.** The only published error-type metric for a commercial research tool is Blue J's claim that users disagree with answers less than 0.2% of the time, which measures user disagreement, not correctness. No independent head-to-head test of commercial tax research tools, no override rates and no parallel-run results were found. The independent measures that exist are adjacent: general ChatGPT answering taxpayer questions (39-47% correct, 2023-24 seasons) and frontier models on return calculation (fewer than one third of simplified returns right).
- **Hallucination is now a conduct issue, not a theoretical one.** In *Clinco* (T.C. Memo. 2026-16) the Tax Court described three of four cited cases as probable AI hallucinations; IRS OPR Alert 2026-19 (24 Jun 2026) applies Circular 230 duties of diligence, competence, supervision and fees; UK PCRT bodies issued AI guidance on 19 Jan 2026.
- **Pricing and roles are moving.** Firms report moving some work to fixed or value-based fees (Sasserath, RKL); 69% of surveyed AI adopters say they are considering alternatives to hourly billing. OPR says billing for manual time not spent may violate the fee rule depending on the facts.
- **Large firms are selling the capability, not only using it.** KPMG (20 May 2026) and EY (25 Nov 2025) announced platforms for building client-specific tax agents. Both are announcements without outcomes.
- **Not found:** a named in-house tax department with a published research-assistant outcome; any M&A tax diligence deployment with measurements; job postings that spell out AI research duties (the AI-in-tax postings found had closed).

## 2. Use cases

```yaml
- id: tax-research-advisory-01
  title: Cited conversational tax research replaces keyword database search
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Practitioners at CPA and advisory firms pay for several research databases but find them slow to use. In Blue J and CPA.com's 2025 survey, 81.3% of respondents also used search engines for tax research and 42% called legacy tools too time-consuming (survey run by a vendor that sells a competing product).
  solution: The adviser states the question and client facts in plain language and gets an answer with inline citations to primary authority (code, regulations, cases, rulings, and in some products commentary), then follows up. Products named in the sources include Blue J, Accordance and CoCounsel Tax. The adviser still reads the authority and decides.
  outcomes:
  - lever: speed
    description: Firm reports simple research on consulting expenses fell from 1 hour to 10 minutes, and analysis of multistate sales tax exposure from 1.5 days to 3 hours
    figure: 1 hour to 10 minutes (stated as 80%); 1.5 days to 3 hours (stated as 75%)
    measures: Time taken by one 25-person firm for two named research tasks, as stated in the vendor case study. The same page's Impact line says 'up to an 80% reduction in research time on complex scenarios', which does not match its body text.
    provenance: vendor-published
    source_ref: ACCORDANCE-SASSERATH-2025
  - lever: speed
    description: A Director at a 90-employee firm describes a technical footnote on a reorganization as taking one hour instead of a full day
    figure: 8 hours to 1 hour (page says nearly 90% reduction)
    measures: One technical research task described by a Director; a single example, not a firm-wide average.
    provenance: vendor-published
    source_ref: ACCORDANCE-BARNES-2026
  - lever: capacity
    description: The firm tracks usage and sees 700+ queries per month across 70 professional staff
    figure: 700+
    measures: Queries per month across the firm, per the firm's own usage tracking as reported in the case study
    provenance: vendor-published
    source_ref: ACCORDANCE-BARNES-2026
  - lever: speed
    description: A principal says a research validation that took 15 to 30 minutes with prior methods takes one minute
    figure: 1 minute vs 15 to 30 minutes
    measures: One principal's example of a payroll/tax lookup; the case study is mainly about audit and advisory work (adjacent, so not used for the grade)
    provenance: vendor-published
    source_ref: TR-HHJ-2026
  - lever: speed
    description: Blue J user survey respondents report 2.94 hours saved per week across research and drafting
    figure: 2.94 hours/week
    measures: Self-reported weekly time saved by respondents to a Blue J user survey, across both research and drafting work
    provenance: vendor-published
    source_ref: BLUEJ-OUTLOOK-2025
  - lever: quality
    description: Blue J says the rate at which users disagree with its tax answers is now below 0.2%
    figure: <0.2%
    measures: Rate at which users disagree with the solution's tax answers (a user-feedback signal collected by the vendor, not an audited accuracy rate; denominator not stated)
    provenance: vendor-published
    source_ref: BLUEJ-OUTLOOK-2025
  prerequisites:
  - A curated, current content library the tool cites (Blue J says it updates primary sources daily)
  - Security review of the vendor; the cases cite closed systems, SOC reports and no training on client data
  - A sanctioned tool, so staff do not fall back to search engines or general chatbots
  risks_and_guardrails:
  - 'Hallucinated or outdated authority: IRS OPR Alert 2026-19 says practitioners must verify facts, citations and calculations the AI produces (Circular 230 s10.22)'
  - Blue J's own survey data suggest fewer firms have formally adopted AI for tax research (60% in 2026) than have staff using AI weekly or monthly (80%), so unsanctioned use is the comparison to manage
  - No independent head-to-head accuracy test of these tools was found; all speed and quality figures above are vendor-published
  human_checkpoints:
  - Adviser reads the cited authority and confirms effective dates, jurisdiction and applicability before relying on it
  - Reviewer (manager or partner) tests the reasoning, not just the citation list
  role_evolution: Associates and mid-level staff do more of the first-pass research; Blue J reports its user base is 40.8% associates, 27.7% mid-level and 31.5% seniors. A partner at one firm says staff who disliked research now feel more comfortable doing it.
  evidence_grade: A
  sources:
  - ref: ACCORDANCE-SASSERATH-2025
    title: Sasserath & Co. Accelerates Research by 80% and Shifts to Value-Based Billing
    publisher: Accordance
    type: vendor
    url: https://www.accordance.com/press/sasserath-co
    date: 2025-11
    access: full
    locator: Solution and Impact sections
  - ref: ACCORDANCE-BARNES-2026
    title: 'Barnes Wendling: From Hours to Minutes'
    publisher: Accordance
    type: vendor
    url: https://www.accordance.com/press/barnes-wendling-from-hours-to-minutes
    date: '2026-06-19'
    access: full
    locator: Impact section
  - ref: BLUEJ-SSC-2025
    title: SSC CPAs + Advisors Elevates Tax Research with Blue J
    publisher: Blue J
    type: vendor
    url: https://www.bluej.com/our-customers/ssc-cpas-advisors
    date: '2025-10-17'
    access: full
    locator: paragraphs 2-3 (switch from Checkpoint Tax Research; no figures)
  - ref: TR-HHJ-2026
    title: Elevating audit and advisory work with CoCounsel Tax & Audit (Harris, Hardy & Johnstone)
    publisher: Thomson Reuters
    type: vendor
    url: https://tax.thomsonreuters.com/en/insights/case-studies/elevating-audit-and-advisory-work-with-cocounsel-tax-and-audit
    date: 2026-03
    access: full
    locator: Challenge and Outcome sections
  - ref: BLUEJ-ENTERPRISE-2026
    title: Best AI tax research tools for large and enterprise firms
    publisher: Blue J
    type: vendor
    url: https://www.bluej.com/blog/best-ai-tax-research-tool-enterprise
    date: '2026-10-16'
    access: full
    locator: section on authoritative content (daily updates, SOC 2)
  - ref: BLUEJ-OUTLOOK-2025
    title: The AI Tax Research Solution Outlook Report (2025 edition)
    publisher: Blue J with CPA.com
    type: survey
    url: https://www.bluej.com/content/ai-tax-research-solution-outlook-report
    date: '2025'
    access: full
    locator: Key Findings; State of Tax Research Solutions; accuracy paragraph
  - ref: BLUEJ-OUTLOOK-2026
    title: 2026 AI Tax Research Solution Outlook Report
    publisher: Blue J with CPA.com
    type: survey
    url: https://www.bluej.com/content/ai-tax-research-solution-outlook-report-2026
    date: '2026'
    access: full
    locator: Key Finding 1 and AI Usage Trends
  - ref: BLUEJ-SERIESD-2025
    title: Blue J Announces $122M Series D Financing
    publisher: Blue J
    type: vendor
    url: https://www.bluej.com/blog/blue-j-announces-122m-series-d-financing-led-by-oak-hc-ft-and-sapphire-ventures
    date: '2025-08-04'
    access: full
    locator: paragraphs 5 and 6
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Section 1, Due Diligence (s10.22)
  last_reviewed: '2026-10-17'
  notes: Grade A rests on named firms' before/after time figures, which are practitioner estimates published by the vendors. None is independent. Blue J reports (2026 edition) that 60% of surveyed respondents work at firms that adopted AI-powered tax research versus 33% in 2025, but the 2026 sample (1,000 US accountants, surveyed 12-23 March 2026 by an external agency) differs from 2025 (150+ practitioners), and Blue J says year-on-year comparisons should be read with that in mind. Publication dates of both Blue J outlook reports are not stated on the pages.
- id: tax-research-advisory-02
  title: Multi-step research plans and multi-agent deep research for gray-area questions
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: research-brief
  ladder: augment
  change_scope: process
  runtime_class: personal-assistant
  maturity: in-production
  problem: Hard or 'gray-area' questions used to take hours across several databases (one firm layered CCH IntelliConnect with five Bloomberg BNA subscriptions). Legacy tools help find sources but leave the practitioner to assemble the analysis.
  solution: 'The tool splits the work into steps: extract the fact pattern, frame the issues, locate authority, weigh its relevance, then propose recommendations with risks. Accordance says it runs each step with dedicated agents and cites primary sources inline. Bloomberg Tax announced a ''Deep Thinking Mode'' that asks clarifying questions and then runs a research plan, and Thomson Reuters describes ''reason-and-act'' research.'
  outcomes:
  - lever: speed
    description: A CPA who leads research at a 100-professional firm says research that took two, four or six hours takes 15 or 20 minutes
    figure: 2-6 hours to 15-20 minutes
    measures: One practitioner's own estimate of time per research task, quoted in the vendor case study
    provenance: vendor-published
    source_ref: ACCORDANCE-WFY-2026
  - lever: speed
    description: Multistate sales tax exposure analysis across 5-10 states done in a few hours instead of 1.5 days
    figure: 1.5 days to 3 hours (stated as 75%)
    measures: Time for one complex analysis at a 25-person firm, as stated in the vendor case study
    provenance: vendor-published
    source_ref: ACCORDANCE-SASSERATH-2025
  - lever: quality
    description: The same practitioner says the tool surfaced the documents needed to defend a debt-to-equity conversion for a foreign-owned holding company in an audit
    figure: none
    measures: Qualitative example; not measured
    provenance: vendor-published
    source_ref: ACCORDANCE-WFY-2026
  prerequisites:
  - A closed system with transparent citations so the researcher can check each answer against primary authority
  - Training so staff move from simple lookups to layered multi-part queries (the firm says the vendor taught this)
  risks_and_guardrails:
  - The practitioner built trust by running queries where he already knew the general answer and checking the tool's output; no systematic error rate was published
  - Bloomberg's Deep Thinking Mode and TR's agentic research are described in launch or marketing material only; no usage evidence was found
  - Multi-step reasoning can compound small errors (Bloomberg Tax's own hallucination article says so)
  human_checkpoints:
  - Senior researcher checks conclusions against his or her own expertise and the cited authority
  - Partner review before advice goes to the client
  role_evolution: Senior researchers and 'power users' move from running searches to directing and testing multi-part analyses; the case-study firm kept simple lookups on a lighter tool (Copilot) and used the research tool for complex scenarios.
  evidence_grade: A
  sources:
  - ref: ACCORDANCE-WFY-2026
    title: 'Wright Ford Young & Co.: Rebuilding Their Approach to Gray-Area Research'
    publisher: Accordance
    type: vendor
    url: https://www.accordance.com/press/wright-ford-young-co-rebuilt-their-approach-to-gray-area-research
    date: '2026-07-22'
    access: full
    locator: Challenge, Solution and Impact sections
  - ref: ACCORDANCE-SASSERATH-2025
    title: Sasserath & Co. Accelerates Research by 80% and Shifts to Value-Based Billing
    publisher: Accordance
    type: vendor
    url: https://www.accordance.com/press/sasserath-co
    date: 2025-11
    access: full
    locator: Solution section
  - ref: ACCORDANCE-BDO-2026
    title: BDO Alliance Recognizes Accordance as an Innovation Leader
    publisher: Accordance
    type: vendor
    url: https://www.accordance.com/press/bdo-alliance-recognizes-accordance-as-an-innovation-leader
    date: '2026-05-11'
    access: full
    locator: section 'Purpose-built AI is the Real Innovation' (five-step process)
  - ref: ACCORDANCE-HOME-2026
    title: Accordance (home page)
    publisher: Accordance (Agnetic Labs)
    type: vendor
    url: https://www.accordance.com
    date: '2026-10-17'
    access: full
    locator: Firmwide Agentic AI section
  - ref: BTAX-TOOLS-2026
    title: Bloomberg Tax Showcases Industry-Leading AI-Powered Tools at TEI Midyear 2026
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/insights/company-news/bloomberg-tax-showcases-industry-leading-ai-powered-tools-at-tei-midyear-2026
    date: '2026-03-09'
    access: full
    locator: Deep Thinking Mode paragraph
  - ref: TR-AGENTICBLOG-2026
    title: An evolution of tax tools and how agentic AI will shape 2026
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/an-evolution-of-tax-tools-and-how-agentic-ai-will-shape-2026/
    date: '2026-05-01'
    access: full
    locator: 'section ''Automating tax workflows with AI: The agentic revolution'''
  - ref: BTAX-HALLUC-2026
    title: 'AI Hallucinations in Tax: The Risks and How to Mitigate Them'
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/?p=16920
    date: '2026-05-11'
    access: full
    locator: section 'Why does generative AI hallucinate?', third reason
  last_reviewed: '2026-10-17'
  notes: Accordance's own claims that it 'outperforms major foundation models' and is 'continuously benchmarked' (funding release, BDO release) are vendor statements; the benchmark was not published in the pages read. Bloomberg Tax and Thomson Reuters items are announcements or product marketing.
- id: tax-research-advisory-03
  title: Reusable planning 'blueprints' and decision matrices for advisory engagements
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - expert-judgment
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Planning advice such as an S-corporation election analysis for a sole proprietor is rebuilt from scratch each time, consuming senior time and leaving smaller firms reactive.
  solution: The firm builds a standard process in the tool (Accordance calls it a 'blueprint') that takes the client's financials and returns, researches the rules, localises inputs such as reasonable compensation, and produces a decision matrix and break-even point. Thomson Reuters' in-house product page lists restructuring and S-corporation conversion analysis as a use case.
  outcomes:
  - lever: speed
    description: A tax shareholder says a 10-hour S-corporation election project becomes roughly two to two and a half hours
    figure: 10 hours to 2-2.5 hours
    measures: One project type at a 17-employee firm, as estimated by the tax shareholder in the vendor case study
    provenance: vendor-published
    source_ref: ACCORDANCE-FINNEY-2025
  prerequisites:
  - A repeatable advisory service the firm wants to standardise
  - Client data in a form the tool can read
  risks_and_guardrails:
  - Output depends on facts supplied; reviewer must test assumptions such as local compensation benchmarks
  - Single example; no error rate published
  human_checkpoints:
  - Tax shareholder reviews the matrix and the localised assumptions before it goes to the client
  role_evolution: The shareholder says the firm becomes 'less compliance focused' and reaches out to clients proactively, instead of hearing about issues after the fact.
  evidence_grade: A
  sources:
  - ref: ACCORDANCE-FINNEY-2025
    title: 'Finney, Neill & Company: Energizing the Practice'
    publisher: Accordance
    type: vendor
    url: https://www.accordance.com/press/finney-neill-company-energizing-the-practice
    date: 2025-11
    access: full
    locator: Efficiency Impact and Culture Impact sections
  - ref: TR-COCOUNSELCORP-2026
    title: 'CoCounsel Tax: The AI tax assistant for in-house teams'
    publisher: Thomson Reuters
    type: vendor
    url: https://tax.thomsonreuters.com/en/products/cocounsel-tax/corp
    date: '2026-10-17'
    access: full
    locator: 'Use cases: ''Analyze transactions and restructuring scenarios'''
  last_reviewed: '2026-10-17'
  notes: Only one named firm reports a figure. The firm trialled the tool beside its existing platform with a five-person tax team in April 2025.
- id: tax-research-advisory-04
  title: Drafting technical memos, client emails and positions from the research
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - document-production
  - client-interaction
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: After research, writing the memo or the client explanation is non-billable work that delays the response and tends to be inconsistent between staff.
  solution: The research tool turns findings into a first draft (memo, client email, presentation, response to a tax authority, tax documentation) that the adviser edits. Blue J sells this as 'Tax Writing'; Thomson Reuters' in-house CoCounsel Tax lists drafting internal technical memos with full source citations from a single prompt.
  outcomes:
  - lever: speed
    description: Blue J user survey respondents report 2.94 hours saved per week across research and drafting; the figure is not split between the two
    figure: 2.94 hours/week
    measures: Self-reported weekly time saved by respondents to a Blue J user survey, across both research and drafting work
    provenance: vendor-published
    source_ref: BLUEJ-OUTLOOK-2025
  prerequisites:
  - A research tool that holds the cited analysis so the draft inherits its citations
  - Firm policy that AI text is a draft, not a final work product (JofA suggests this)
  risks_and_guardrails:
  - Fabricated citations in a client memo or filing are the main risk (JofA, Clinco)
  - 'Fee risk: IRS OPR says billing clients for manual labour not actually spent may violate s10.27 depending on the facts'
  - Confidentiality when client facts are uploaded
  human_checkpoints:
  - Adviser edits and takes responsibility for the draft
  - Verification of every cited authority before issue
  role_evolution: Staff spend less time on the first draft and more on editing and client-specific judgment; a partner at Larson Gross says the firm also uses the tool to craft responses to client questions and calculations.
  evidence_grade: B
  sources:
  - ref: BLUEJ-WRITING-2026
    title: Tax Writing (Blue J product page)
    publisher: Blue J
    type: vendor
    url: https://www.bluej.com/tax-writing
    date: '2026-10-17'
    access: full
    locator: use-case list and Larson Gross quote
  - ref: BLUEJ-OUTLOOK-2025
    title: The AI Tax Research Solution Outlook Report (2025 edition)
    publisher: Blue J with CPA.com
    type: survey
    url: https://www.bluej.com/content/ai-tax-research-solution-outlook-report
    date: '2025'
    access: full
    locator: Key Findings, 2.94 hours/week
  - ref: TR-COCOUNSELCORP-2026
    title: 'CoCounsel Tax: The AI tax assistant for in-house teams'
    publisher: Thomson Reuters
    type: vendor
    url: https://tax.thomsonreuters.com/en/products/cocounsel-tax/corp
    date: '2026-10-17'
    access: full
    locator: 'Capabilities: Automate; ''Draft internal, technical memos'''
  - ref: JOFA-CLINCO-2026
    title: 'A recipe for sanctions: AI-hallucinated citations in tax'
    publisher: Journal of Accountancy (AICPA)
    type: press
    url: https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/
    date: '2026-09-01'
    access: full
    locator: section 'Firm policies for responsible AI use in tax practice'
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Regulatory Framework, s10.27(a) Fees
  last_reviewed: '2026-10-17'
  notes: Named drafting deployments are quotes on vendor pages; no drafting-specific measurement was found. The Larson Gross quote appears on Blue J's Tax Writing page.
- id: tax-research-advisory-05
  title: Answering client questions during the call instead of researching and calling back
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - client-interaction
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Complex client questions meant telling the client 'we will research and call you back', often a day later, which delayed advice and limited what could be said in the moment.
  solution: With a cited research assistant open, the adviser can look up and test an answer while the client is on the line, or answer from a sole-practitioner desk without a colleague to consult.
  outcomes:
  - lever: experience
    description: A Director says the team can now get answers on a phone call; usage is tracked at 700+ queries per month firm-wide
    figure: 700+ queries per month
    measures: Queries per month across the firm, per the firm's own tracking, as reported in the vendor case study
    provenance: vendor-published
    source_ref: ACCORDANCE-BARNES-2026
  prerequisites:
  - Fast, reliable tool
  - Adviser able to judge an answer in real time
  risks_and_guardrails:
  - Speed raises the temptation to answer without full verification; JofA and OPR both stress the duty to verify before relying
  - Anything said live to a client is advice; the firm should confirm complex answers in writing after review
  human_checkpoints:
  - Adviser decides what can be said live and what needs follow-up review
  role_evolution: Blue J's customer pages quote a sole practitioner (Hatridge) who says the tool gives her the 'team backup' she lacked, and a partner at Sorren who says clients now expect quick research-backed replies.
  evidence_grade: B
  sources:
  - ref: ACCORDANCE-BARNES-2026
    title: 'Barnes Wendling: From Hours to Minutes'
    publisher: Accordance
    type: vendor
    url: https://www.accordance.com/press/barnes-wendling-from-hours-to-minutes
    date: '2026-06-19'
    access: full
    locator: Challenge and Impact sections
  - ref: BLUEJ-HATRIDGE-2024
    title: Hatridge Tax & Accounting Grows Capacity as a Sole Proprietor through Blue J
    publisher: Blue J
    type: vendor
    url: https://www.bluej.com/our-customers/hatridge-tax-accounting-grows-capacity-as-a-sole-proprietor-through-blue-j-ai-for-tax-research
    date: '2024-09-30'
    access: full
    locator: quote from Leslie Hatridge
  - ref: BLUEJ-LARSON-2025
    title: 'Larson Gross Advisors: Driving better client experiences with generative AI'
    publisher: Blue J
    type: vendor
    url: https://www.bluej.com/our-customers/larson-gross-advisors
    date: '2025-04-16'
    access: full
    locator: summary paragraph (reduced time on routine tasks, expanded expertise; no figures)
  - ref: BLUEJ-HOME-2026
    title: AI Tax Research Platform (Blue J home page)
    publisher: Blue J
    type: vendor
    url: https://www.bluej.com
    date: '2026-10-15'
    access: full
    locator: customer quote block (Sorren)
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Section 1, Due Diligence
  last_reviewed: '2026-10-17'
  notes: Only one named firm gives a usage figure, and it is a usage count, not an outcome of the change.
- id: tax-research-advisory-06
  title: Document-grounded tax analysis of client agreements, trusts and schedules
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  - review-assurance
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: Advisers read long operating agreements, trust and will documents and supporting schedules by hand before they can apply the tax rules.
  solution: The adviser uploads the document into the research workspace; the tool summarises it and checks it against cited authority. Wright Ford Young extended its approved tool from research to reviewing and summarising operating agreements. Jansen & Company says it wants to use Workspaces to analyse trust and will documents. Thomson Reuters' in-house page describes uploading schedules to flag passive-activity, at-risk basis and QBI errors.
  outcomes:
  - lever: speed
    description: none published
    figure: none
    measures: none published
    provenance: self-reported
    source_ref: n/a
  prerequisites:
  - Tool approved for client data (closed system, no training on client data)
  - Engagement terms that allow the use
  risks_and_guardrails:
  - 'Confidentiality: the OPR alert warns that client data can be repurposed to answer an inquiry about another client when documents are uploaded'
  - Extraction errors in summaries
  human_checkpoints:
  - Adviser checks the summary against the source document before relying on it
  role_evolution: Advisers move from reading to checking summaries and spotting what the tool missed.
  evidence_grade: B
  sources:
  - ref: ACCORDANCE-WFY-2026
    title: 'Wright Ford Young & Co.: Rebuilding Their Approach to Gray-Area Research'
    publisher: Accordance
    type: vendor
    url: https://www.accordance.com/press/wright-ford-young-co-rebuilt-their-approach-to-gray-area-research
    date: '2026-07-22'
    access: full
    locator: Security & Trust section
  - ref: TR-JANSEN-2026
    title: How Jansen & Company CPAs delivers higher-value tax advice with CoCounsel Tax
    publisher: Thomson Reuters
    type: vendor
    url: https://tax.thomsonreuters.com/en/insights/case-studies/how-jansen-and-company-cpas-is-delivering-higher-value-tax-advice-at-scale-with-cocounsel-tax
    date: 2026-02
    access: full
    locator: The outcomes section (future plans)
  - ref: TR-COCOUNSELCORP-2026
    title: 'CoCounsel Tax: The AI tax assistant for in-house teams'
    publisher: Thomson Reuters
    type: vendor
    url: https://tax.thomsonreuters.com/en/products/cocounsel-tax/corp
    date: '2026-10-17'
    access: full
    locator: 'Use cases: ''Review complex tax positions faster'''
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Section 1, confidentiality paragraph
  last_reviewed: '2026-10-17'
  notes: Wright Ford Young is the only named firm reported as already doing this (operating agreements). The Jansen item is a stated intention. The s7216 and s6713 references appear in secondary coverage cited in the landscape file, not in the part of the alert read for this scan.
- id: tax-research-advisory-07
  title: National-firm research assistants with a named firm-level AI leader and governance
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  - coordination-scheduling
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Large firms have thousands of tax professionals researching the same questions separately, with uneven tools and no central way to control what staff paste into which AI.
  solution: The firm licenses or builds a standard tax research assistant, names an AI leader for tax, and sets governance. Crowe signed an enterprise agreement for Ask Blue J across its tax practice and has a 'Tax AI Leader'. KPMG's M&A Tax practice standardised its technology stack and has its own GenAI research assistant. PwC says it has a US AI Tax Leader, a governance committee, over 3,200 AI champions and over 800 custom GPTs and 250 agents firm-wide.
  outcomes:
  - lever: capacity
    description: Crowe says Ask Blue J is implemented across the firm's entire tax practice
    figure: entire tax practice (no headcount given)
    measures: Scope of an enterprise agreement, per the vendor's chief revenue officer in the 2024 release
    provenance: vendor-published
    source_ref: BLUEJ-CROWE-2024
  - lever: capacity
    description: PwC US AI Tax Leader says the firm has over 3,200 AI champions and about 80% of people have taken some AI training
    figure: 3,200+ champions; about 80% trained
    measures: AI champions 'across the firm' (many inside tax; not tax only) and share of 'our people' who took some form of AI training, as stated by the PwC US AI tax leader
    provenance: self-reported
    source_ref: PWC-MEGNA-2025
  prerequisites:
  - Executive sponsor and a named AI leader
  - Security and confidentiality review
  - Training and an AI champion network
  risks_and_guardrails:
  - The PwC interview says policy interpretation and high-touch consulting work still see limited AI use
  - Governance committee and 'multi-eye' human review for complex outputs (PwC)
  human_checkpoints:
  - Human review at each level of the firm's review process
  role_evolution: 'New roles appear: Crowe Tax AI Leader (Matt Paparella in the 2024 release), PwC US AI Tax Leader (Dom Megna),'
  evidence_grade: B
  sources:
  - ref: BLUEJ-CROWE-2024
    title: Blue J announces enterprise agreement with Crowe
    publisher: Blue J (Business Wire release)
    type: vendor
    url: https://www.bluej.com/our-customers/blue-j-announces-enterprise-agreement-with-crowe-to-enhance-their-generative-ai-enabled-tax-services
    date: '2024-10-22'
    access: full
    locator: release paragraphs 1-4
  - ref: BLUEJ-WTP-2023
    title: Whiteford, Taylor & Preston has partnered with Blue J
    publisher: Blue J
    type: vendor
    url: https://www.bluej.com/our-customers/whiteford-taylor-preston-has-partnered-with-bluej
    date: '2023-08-02'
    access: full
    locator: release paragraph 1 (a law firm tax group as early adopter)
  - ref: KPMG-MA-2025
    title: 'How generative AI is transforming mergers and acquisitions tax: The KPMG approach'
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/how-generative-ai-transforming.pdf
    date: 2025-06
    access: full
    locator: page 1, 'The KPMG journey with GenAI'
  - ref: PWC-MEGNA-2025
    title: How PwC's tax team is using agentic AI (interview with Dom Megna)
    publisher: CFO.com
    type: press
    url: https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/
    date: '2025-06-06'
    access: full
    locator: answers on Agent OS, governance, and workforce
  last_reviewed: '2026-10-17'
  notes: Crowe date (2024-10-22) is older than the 12-18 month target, kept as the only named enterprise deal in the research niche. The PwC interview is mostly about compliance-type agents (K-1 mapping); only its organisation and governance points are used here. KPMG UK job posting (9 Feb 2026) was seen only in a search result and the page was closed when fetched, so it is not a source here.
- id: tax-research-advisory-08
  title: In-house tax research assistant grounded in the department's own knowledge base
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: In-house tax teams handle ad hoc questions from finance, legal and the business with limited staff, and positions and policies sit in separate folders. Thomson Reuters' 2025 survey of 288 tax departments found 58% under-resourced.
  solution: A research assistant answers with citations from authoritative content and also from the department's own guidance and policies; it drafts internal technical memos and regulatory summaries. Thomson Reuters markets CoCounsel Tax for in-house teams with a Knowledge Base; the TEI Midyear 2026 programme ran hands-on Tax Labs on AI and tax research with Thomson Reuters CoCounsel and with Accordance.
  outcomes:
  - lever: capacity
    description: Of 288 surveyed corporate tax departments, 67% were not using GenAI in 2025; among those that were, usage included conducting research
    figure: 67% not using GenAI
    measures: Share of respondents (288 tax departments worldwide) whose department is not using GenAI, per Thomson Reuters Institute's 2025 survey
    provenance: vendor-published
    source_ref: TR-CORPTAX-2025
  prerequisites:
  - 'Approved tool and data security sign-off (KPMG Germany: IT approvals 47%, data protection 41% and lack of knowledge 41% were top hurdles)'
  - Clean internal knowledge base
  risks_and_guardrails:
  - Sala argues AI cannot carry regulatory, ethical or financial culpability, so the department keeps accountability
  - TEI Tax Tech 2026 attendees were polled and two of more than 50 said tax owns AI implementation at their company
  human_checkpoints:
  - Tax director reviews positions that go to the CFO, auditors or authorities
  role_evolution: Tax staff become reviewers and knowledge curators; Sala argues corporate tax teams will shrink little because tax practice is more than preparation.
  evidence_grade: C
  sources:
  - ref: TR-COCOUNSELCORP-2026
    title: 'CoCounsel Tax: The AI tax assistant for in-house teams'
    publisher: Thomson Reuters
    type: vendor
    url: https://tax.thomsonreuters.com/en/products/cocounsel-tax/corp
    date: '2026-10-17'
    access: full
    locator: 'Meet CoCounsel Tax; Capabilities: Access; Use cases'
  - ref: TEI-MIDYEAR-2026
    title: TEI Midyear Conference 2026 at-a-glance agenda
    publisher: Tax Executives Institute
    type: conference
    url: https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf
    date: '2026-03-15'
    access: full
    locator: Tax Lab sessions on the agenda
  - ref: TR-CORPTAX-2025
    title: 'The GenAI paradox: why most tax departments aren''t using AI yet (2025 State of the Corporate Tax Department)'
    publisher: Thomson Reuters Tax & Accounting
    type: survey
    url: https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/
    date: '2025-10-22'
    access: full
    locator: key takeaways and paragraphs 2 and 5
  - ref: KPMG-DE-2026
    title: Tax departments are increasingly turning to artificial intelligence (KPMG Germany quick surveys)
    publisher: KPMG Germany
    type: survey
    url: https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html
    date: '2026-05-07'
    access: full
    locator: Key findings; hurdles paragraph
  - ref: SALA-TAXNOTES-2026
    title: AI Won't Shrink Corporate Tax Teams Much. Here's Why. (Sala, Tax Notes State 121:189; abstract on TaxProf Blog)
    publisher: Tax Notes / TaxProf Blog
    type: press
    url: https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/
    date: '2026-07-20'
    access: full
    locator: abstract
  - ref: TR-TEITAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: section 'A very bad wizard'
  last_reviewed: '2026-10-17'
  notes: No named in-house department published a research-assistant deployment with outcomes. Oxford Industries' TEI session with Savant concerns tax process automation (sales and use tax, VAT, reconciliation), not research, and is routed to tax-data-technology. KPMG Germany's sample size is not stated in the release.
- id: tax-research-advisory-09
  title: Citation checking and AI-use logging as a standing review step
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: AI can produce plausible but nonexistent authority. In Clinco, three of four cases cited in a brief on a notice-of-deficiency signature were described by the Tax Court as probable AI hallucinations, and counsel repeated one after the IRS flagged it.
  solution: Reviewers confirm every cited authority exists and says what the draft claims, and the firm keeps a record. KPMG's M&A Tax practice says its human-in-the-loop model uses citations and hyperlinks to validate all AI outputs and regular training. JofA suggests firms keep citation verification logs, use a second reviewer for filings and keep documentation of AI use and review.
  outcomes:
  - lever: risk
    description: No measured error or catch rates published. Bloomberg Tax cites a January 2026 International Tax Journal paper reporting nearly 800 AI-related citation errors across at least 25 countries (second-hand; the paper was not opened)
    figure: nearly 800
    measures: AI-related citation errors found in a survey of disciplinary actions and court records by late 2025, as described by Bloomberg Tax
    provenance: vendor-published
    source_ref: BTAX-HALLUC-2026
  prerequisites:
  - Written firm AI policy (OPR s10.36 expects firm procedures)
  - Training on AI limits
  - Access to the primary-source databases for checking
  risks_and_guardrails:
  - The Tax Court stopped short of sanctions in Clinco but warned the bar; the OPR alert lists sanctions courts have imposed on lawyers (fines, censure, default judgments, removal, referrals)
  - A check that only confirms a citation exists can miss a real case that does not support the proposition
  - Standing orders requiring AI certification exist in some courts (JofA)
  human_checkpoints:
  - Second reviewer cross-checks authority before a filing or client memo goes out
  - Responsible partner signs off on the verification record
  role_evolution: Review time moves from reading prose to verifying authority. OPR says individuals with principal authority over a firm's practice must take reasonable steps to ensure adequate procedures (s10.36).
  evidence_grade: B
  sources:
  - ref: KPMG-MA-2025
    title: 'How generative AI is transforming mergers and acquisitions tax: The KPMG approach'
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/how-generative-ai-transforming.pdf
    date: 2025-06
    access: full
    locator: page 2, 'Balancing risk and innovation'
  - ref: JOFA-CLINCO-2026
    title: 'A recipe for sanctions: AI-hallucinated citations in tax'
    publisher: Journal of Accountancy (AICPA)
    type: press
    url: https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/
    date: '2026-09-01'
    access: full
    locator: sections 'The apparitions in the briefing' and 'Firm policies'
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Real-World Consequences; s10.22 and s10.36
  - ref: BTAX-HALLUC-2026
    title: 'AI Hallucinations in Tax: The Risks and How to Mitigate Them'
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/?p=16920
    date: '2026-05-11'
    access: full
    locator: section 'Why does generative AI hallucinate?'
  last_reviewed: '2026-10-17'
  notes: No automated citation-checking product was found in the sources read, so none is described. Clinco is T.C. Memo. 2026-16; the opinion itself was not opened, only JofA's account (1 Sep 2026). JofA reports Clinco appears to be the first Tax Court case to address potential AI hallucinations.
- id: tax-research-advisory-10
  title: Value-based and fixed-fee pricing as research time shrinks
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - client-interaction
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: piloting
  problem: Billable-hour pricing ties revenue to the time that AI now removes from research and drafting, while OPR warns against billing for manual time not actually spent.
  solution: 'Firms test fixed monthly fees, project pricing, hybrid or value-based models. Sasserath & Co. moved new-client onboarding to fixed monthly fees where appropriate; RKL has onboarded several dozen clients under an alternative pricing model it is piloting with a consultant; PwC''s US tax leader says time is becoming less relevant. This is pattern ''other'': a pricing change, not an AI workflow.'
  outcomes:
  - lever: growth
    description: 69% of surveyed AI adopters say they are considering value-based, hybrid or fixed-fee billing
    figure: 69%
    measures: Share of respondents who have adopted AI-powered tax research (1,000 US accountants surveyed March 2026) who are considering alternatives to hourly billing
    provenance: vendor-published
    source_ref: BLUEJ-OUTLOOK-2026
  - lever: growth
    description: RKL has onboarded several dozen new clients under the alternative pricing model it is piloting
    figure: several dozen clients
    measures: New clients onboarded under the pilot model, per an RKL tax partner quoted by Bloomberg Tax
    provenance: self-reported
    source_ref: BTAX-PRICING-2026
  prerequisites:
  - Scoping and pricing skills
  - Management willingness to test with a subset of clients (Blue J/CPA.com advises running it like an experiment)
  risks_and_guardrails:
  - 'OPR: pass efficiencies on openly and disclose AI activities where needed (s10.27)'
  - 'Thomson Reuters Institute''s survey: one third say their firm''s commercial model has not adapted'
  human_checkpoints:
  - Partner approves fee basis against OPR s10.27 expectations
  role_evolution: Partners spend more effort on scoping and value conversations; entry-level hours that justified headcount shrink.
  evidence_grade: B
  sources:
  - ref: ACCORDANCE-SASSERATH-2025
    title: Sasserath & Co. Accelerates Research by 80% and Shifts to Value-Based Billing
    publisher: Accordance
    type: vendor
    url: https://www.accordance.com/press/sasserath-co
    date: 2025-11
    access: full
    locator: section 'Moving to Value-Based Pricing'
  - ref: BTAX-PRICING-2026
    title: AI Efficiency Gains Push Accounting Firms to Reimagine Pricing
    publisher: Bloomberg Tax (Daily Tax Report)
    type: press
    url: https://news.bloombergtax.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing
    date: '2026-03-05'
    access: full
    locator: paragraphs 2-3 and 'New Pricing Options'
  - ref: BLUEJ-OUTLOOK-2026
    title: 2026 AI Tax Research Solution Outlook Report
    publisher: Blue J with CPA.com
    type: survey
    url: https://www.bluej.com/content/ai-tax-research-solution-outlook-report-2026
    date: '2026'
    access: full
    locator: Key Finding 4
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: s10.27(a) Fees
  - ref: TR-FOP-2026
    title: What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026
    date: '2026-07-21'
    access: full
    locator: paragraph on commercial models
  last_reviewed: '2026-10-17'
  notes: 'RSM''s partner offers a hypothetical: if tax advisory reports typically take 20 hours, generative AI plus checking ''could'' cut them to 10, and the firm has to decide whether that is margin or a price cut (Bloomberg Tax, 5 Mar 2026). That is an illustration, not a measurement. The RKL figure is the partner''s statement as reported by a journalist.'
- id: tax-research-advisory-11
  title: 'M&A tax: reviewing purchase agreements and drafting the diligence report'
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  - research-synthesis
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Transaction tax teams read long stock purchase and partnership agreements, research transaction-specific rules, and write diligence reports under deal deadlines.
  solution: 'KPMG US M&A Tax describes four GenAI tools: a research assistant for tax questions (it names ''GenAI Research Assistant for Navigating Tax''), accelerated review of SPAs and partnership agreements to highlight nonstandard clauses against baselines, an M&A Tax Reporting System that drafts an initial diligence report from jurisdiction, deal type and client constraints, and a writing review assistant. Professionals add their own assessments.'
  outcomes:
  - lever: speed
    description: none published
    figure: none
    measures: none published
    provenance: self-reported
    source_ref: n/a
  prerequisites:
  - Standardised national technology stack and workflows (KPMG says this came first)
  - Source documents in a form the tools can read
  risks_and_guardrails:
  - Hallucination risk handled through human-in-the-loop with citations and hyperlinks, per KPMG
  - Draft reports could carry unsupported statements into a deal negotiation
  human_checkpoints:
  - Professionals build on the draft with their own assessments and recommendations
  - Senior reviewer signs the diligence report
  role_evolution: KPMG says practitioners shift from transactional tasks to advisory roles on deal structures and client-specific strategies.
  evidence_grade: B
  sources:
  - ref: KPMG-MA-2025
    title: 'How generative AI is transforming mergers and acquisitions tax: The KPMG approach'
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/how-generative-ai-transforming.pdf
    date: 2025-06
    access: full
    locator: 'page 1 ''GenAI in action: Key use cases in M&A tax''; page 2 ''Balancing risk and innovation'''
  - ref: ANTHROPIC-JOB-2026
    title: M&A Tax Director (Anthropic job posting on General Catalyst job board)
    publisher: Anthropic
    type: job-posting
    url: https://jobs.generalcatalyst.com/companies/anthropic/jobs/89778547-m-a-tax-director
    date: '2026-08-13'
    access: full
    locator: 'responsibilities list (shows the in-house transactions-tax scope: diligence, structuring, memos; no AI use is stated)'
  last_reviewed: '2026-10-17'
  notes: KPMG's web page version of this material carries a teaser saying its technology compresses weeks of tax analysis into minutes; that is a marketing claim with no method, so it is not used as an outcome. The article is based on a TaxWatch webcast 'A Case Study in Unlocking the Power of GenAI in M&A Tax' with Jim Tod. The PDF carries a 2025 copyright and a June 2025 creation date; the web page shows a 29 Jul 2026 datePublished, which may be a re-publication date. The Anthropic job posting is used only to show the shape of in-house transaction tax work.
- id: tax-research-advisory-12
  title: M&A tax diligence agent that reads the data room and drafts the risk assessment
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: document-to-decision
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Tax diligence over entity structures, intercompany agreements, transfer pricing documentation and filings takes weeks and relies on sampling what the deal team can read in time.
  solution: V7 markets an agent that ingests financial statements, tax returns, transfer pricing documentation, intercompany agreements and filings, maps entity structures, flags permanent establishment and related-party issues, and returns a cited risk assessment.
  outcomes:
  - lever: speed
    description: V7 shows 'traditional way' 3-4 weeks versus 2-3 days and 'average time saved' of 90%
    figure: 3-4 weeks to 2-3 days; 90%
    measures: A time comparison on a sample 'Tax Diligence - Meridian Acquisition' demo project on the vendor page; no customer is named and no method is given
    provenance: vendor-published
    source_ref: V7-TAXDD-2026
  prerequisites:
  - Data-room access and document ingestion
  - Deal-team willingness to rely on agent output
  risks_and_guardrails:
  - Vendor claim only; no named customer or error rate
  - False negatives in a diligence review could leave exposures unpriced
  human_checkpoints:
  - Deal tax lead reviews the risk assessment and decides what to raise with the counterparty
  role_evolution: Not described by the vendor beyond 'ready for your legal and finance teams'.
  evidence_grade: C
  sources:
  - ref: V7-TAXDD-2026
    title: AI Tax Due Diligence Agent (V7 Go)
    publisher: V7
    type: vendor
    url: https://www.v7labs.com/agents/ai-tax-due-diligence-agent
    date: '2026-10-17'
    access: full
    locator: page sections 'Time comparison' and 'Why V7 Go'
  last_reviewed: '2026-10-17'
  notes: Page is undated; date shown is the access date. No customer named. Kept as the contrast to KPMG's human-led model in use case 11.
- id: tax-research-advisory-13
  title: AI-supported research training for junior staff
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  - coordination-scheduling
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Junior staff lack the background to navigate legacy research tools, and seniors act as informal research trainers.
  solution: Firms use the cited research assistant as a tutor and a way to widen who can research. Jansen & Company's senior managing director (the firm's informal 'research trainer') says he uses AI as a tutor. Sasserath & Co. says younger staff did not have to unlearn legacy methods. Finney Neill says younger, less experienced staff could not get to answers on the old platform.
  outcomes:
  - lever: capacity
    description: 'Blue J''s user base by experience level: associates 40.8%, mid-level 27.7%, seniors 31.5%'
    figure: 40.8% / 27.7% / 31.5%
    measures: Share of Blue J users at each experience level, from the vendor's user data
    provenance: vendor-published
    source_ref: BLUEJ-OUTLOOK-2025
  prerequisites:
  - 'Structured training that keeps teaching judgment (TR Institute: supervise before automating)'
  - Training on checking outputs
  risks_and_guardrails:
  - TR Institute warns junior staff still need structured development to build judgment as tasks are automated
  - Over-reliance could erode skill in reading authority
  human_checkpoints:
  - Supervisor reviews juniors' research and the reasoning, not only the answer
  role_evolution: 'Blue J/CPA.com describe three training levels: technical skill to judge AI output, cognitive skill to ask the right questions, and human skills. Roles of early-career staff change.'
  evidence_grade: B
  sources:
  - ref: TR-JANSEN-2026
    title: How Jansen & Company CPAs delivers higher-value tax advice with CoCounsel Tax
    publisher: Thomson Reuters
    type: vendor
    url: https://tax.thomsonreuters.com/en/insights/case-studies/how-jansen-and-company-cpas-is-delivering-higher-value-tax-advice-at-scale-with-cocounsel-tax
    date: 2026-02
    access: full
    locator: Challenge and Outcomes sections
  - ref: ACCORDANCE-SASSERATH-2025
    title: Sasserath & Co. Accelerates Research by 80% and Shifts to Value-Based Billing
    publisher: Accordance
    type: vendor
    url: https://www.accordance.com/press/sasserath-co
    date: 2025-11
    access: full
    locator: section 'Democratizing Expertise Across the Team'
  - ref: ACCORDANCE-FINNEY-2025
    title: 'Finney, Neill & Company: Energizing the Practice'
    publisher: Accordance
    type: vendor
    url: https://www.accordance.com/press/finney-neill-company-energizing-the-practice
    date: 2025-11
    access: full
    locator: Challenge section
  - ref: BLUEJ-OUTLOOK-2026
    title: 2026 AI Tax Research Solution Outlook Report
    publisher: Blue J with CPA.com
    type: survey
    url: https://www.bluej.com/content/ai-tax-research-solution-outlook-report-2026
    date: '2026'
    access: full
    locator: training paragraphs
  - ref: TR-FOP-2026
    title: What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026
    date: '2026-07-21'
    access: full
    locator: '''Define the role of early-career professionals'''
  last_reviewed: '2026-10-17'
  notes: No outcome measures for skill development were found.
- id: tax-research-advisory-14
  title: Advisers co-build client-specific tax agents as an advisory service
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - expert-judgment
  - software-systems
  pattern: other
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Clients want agents that track tax-rule changes and apply them to their facts, but building them is slow and needs tax and engineering skills together.
  solution: KPMG's Digital Gateway Powered by Claude, announced 20 May 2026, lets professionals and clients build agentic workflows in the platform; KPMG US tax vice chair Rema Serafi says building an agent for changing tax regulations used to take weeks and now takes minutes. EY announced EY.ai Tax Labs and the EY.ai Tax Agent Factory (25 Nov 2025) to design, build, train, deploy and manage agents at scale with clients.
  outcomes:
  - lever: speed
    description: KPMG US tax vice chair says building a client agent to adjust to changing tax regulations went from weeks to minutes
    figure: weeks to minutes (no figures)
    measures: A leader's statement in a launch announcement; no measurement given
    provenance: self-reported
    source_ref: KPMG-ANTHROPIC-2026
  prerequisites:
  - Platform with client data controls (Digital Gateway runs on Azure)
  - Alliance with a model provider; tax domain experts
  risks_and_guardrails:
  - Announcement-stage claims only
  - Responsibility for an agent's tax output sits with the adviser or client
  human_checkpoints:
  - Not described in the sources
  role_evolution: Advisers become agent designers and sellers of software-plus-services. KPMG says it will roll Claude out to 276,000 people (stated as 'will have access').
  evidence_grade: C
  sources:
  - ref: KPMG-ANTHROPIC-2026
    title: KPMG Partners with Anthropic for Digital Gateway Powered by Claude
    publisher: CPA Practice Advisor (reproducing the announcement)
    type: press
    url: https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/
    date: '2026-05-20'
    access: full
    locator: paragraphs on Digital Gateway and Serafi quote
  - ref: EY-TAXLABS-2025
    title: EY unveils suite of powerful AI capabilities to accelerate tax transformation and deliver strategic value
    publisher: EY
    type: firm
    url: https://www.ey.com/en_gl/newsroom/2025/11/ey-unveils-suite-of-powerful-ai-capabilities-to-accelerate-tax-transformation-and-deliver-strategic-value
    date: '2025-11-25'
    access: full
    locator: sections 'EY.ai Tax Labs' and 'The EY.ai Tax Agent Factory'
  last_reviewed: '2026-10-17'
  notes: Both are firm announcements. The EY release says agents help clients 'streamline data processes' and is oriented to compliance and operations as much as advice.
- id: tax-research-advisory-15
  title: Standardising on approved, closed-system tools instead of unsanctioned chatbots
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Staff use general chatbots for tax questions whether or not the firm has approved them, with confidentiality, currency and citation risks.
  solution: 'Firms choose a sanctioned, tax-specific, closed tool, set policy and train staff. Wright Ford Young ''recently standardized its staff on approved platforms'' and chose the research tool partly because it is a closed system with citations. Harris, Hardy & Johnstone cites an enclosed LLM with SOC certification as a selling point. This is pattern ''other'': a governance step.'
  outcomes:
  - lever: risk
    description: 'Blue J''s 2026 survey: 80% of respondents use general-purpose or tax-specific AI weekly or monthly, but only 60% work at firms that formally adopted AI-powered tax research'
    figure: 80% vs 60%
    measures: Respondents (1,000 US accountants, March 2026) using AI for tax research weekly or monthly, versus respondents whose firm formally adopted it; the vendor reads the gap as possible unsanctioned use
    provenance: vendor-published
    source_ref: BLUEJ-OUTLOOK-2026
  - lever: risk
    description: Thomson Reuters Institute's paper says more than one-third of tax and audit professionals admit to using unauthorized AI tools
    figure: more than one-third
    measures: Share of surveyed tax and audit professionals (Future of Professionals 2026 survey; tax and audit sub-sample size not given on the page)
    provenance: vendor-published
    source_ref: TR-FOP-2026
  prerequisites:
  - Written AI policy
  - Vendor security review
  risks_and_guardrails:
  - 'IRS OPR: confidentiality leakage across clients is a named risk; competence under s10.35 requires understanding the tool'
  - Closed tools reduce but do not remove the verification duty
  human_checkpoints:
  - Managing partner or tax leader approves tools and maintains the approved list
  role_evolution: A named owner for tax AI is needed; TEI Tax Tech 2026 attendees said tax rarely owns AI implementation.
  evidence_grade: B
  sources:
  - ref: ACCORDANCE-WFY-2026
    title: 'Wright Ford Young & Co.: Rebuilding Their Approach to Gray-Area Research'
    publisher: Accordance
    type: vendor
    url: https://www.accordance.com/press/wright-ford-young-co-rebuilt-their-approach-to-gray-area-research
    date: '2026-07-22'
    access: full
    locator: Security & Trust section
  - ref: TR-HHJ-2026
    title: Elevating audit and advisory work with CoCounsel Tax & Audit (Harris, Hardy & Johnstone)
    publisher: Thomson Reuters
    type: vendor
    url: https://tax.thomsonreuters.com/en/insights/case-studies/elevating-audit-and-advisory-work-with-cocounsel-tax-and-audit
    date: 2026-03
    access: full
    locator: The solution section
  - ref: BLUEJ-OUTLOOK-2026
    title: 2026 AI Tax Research Solution Outlook Report
    publisher: Blue J with CPA.com
    type: survey
    url: https://www.bluej.com/content/ai-tax-research-solution-outlook-report-2026
    date: '2026'
    access: full
    locator: AI Usage Trends
  - ref: TR-FOP-2026
    title: What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026
    date: '2026-07-21'
    access: full
    locator: '''Govern the tools being used'''
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Section 1 and s10.35, s10.36
  - ref: TR-TEITAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: section 'A very bad wizard'
  last_reviewed: '2026-10-17'
  notes: The 'unsanctioned' reading of 80% vs 60% is Blue J's inference; the two figures count different things.
- id: tax-research-advisory-16
  title: Preliminary position analysis in place of waiting for an external firm opinion (idea)
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - expert-judgment
  pattern: research-brief
  ladder: augment
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: Corporates often wait for, and defer to, an expensive opinion from a Big Four national office or law firm on a complex planning matter.
  solution: 'Idea (labelled): a highly technical tax AI could give corporate tax teams a direction on a planning matter before or instead of the external opinion. Sala poses this as a question prompted by a demonstration and asks whether the Big Four''s work is about more than an accurate opinion on the law.'
  outcomes:
  - lever: cost
    description: none published
    figure: none
    measures: none published
    provenance: self-reported
    source_ref: n/a
  prerequisites:
  - Not discussed
  risks_and_guardrails:
  - Sala argues AI cannot shoulder regulatory, ethical or financial consequences of culpability
  human_checkpoints:
  - Not described
  role_evolution: Sala predicts corporate tax teams will shrink little.
  evidence_grade: D
  sources:
  - ref: SALA-TAXNOTES-2026
    title: AI Won't Shrink Corporate Tax Teams Much. Here's Why. (Sala, Tax Notes State 121:189; abstract on TaxProf Blog)
    publisher: Tax Notes / TaxProf Blog
    type: press
    url: https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/
    date: '2026-07-20'
    access: full
    locator: abstract and excerpt
  last_reviewed: '2026-10-17'
  notes: IDEA. Only an abstract and excerpt of Sala's Tax Notes State article was read. No deployment found.
- id: tax-research-advisory-17
  title: LLM-assisted generation or detection of tax-minimisation strategies (idea)
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Planning strategies are found through expert experience, and abusive strategies by wealthy taxpayers are hard for agencies to spot.
  solution: 'Idea (labelled): Blair-Stanek, Holzenberger and Van Durme test whether advanced LLMs can interpret and verify tax strategies, fill gaps in partial strategies and generate complete strategies; they report that LLM reasoning identified an apparently novel strategy. The authors frame the use for tax agencies; the same capability bears on adviser-side planning.'
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: none published
    provenance: self-reported
    source_ref: n/a
  prerequisites:
  - Not applicable
  risks_and_guardrails:
  - The authors present the capability as a tool for tax agencies fighting abuse
  human_checkpoints:
  - Not described
  role_evolution: Not discussed.
  evidence_grade: D
  sources:
  - ref: JHU-TAXABUSE-2025
    title: Can LLMs Identify Tax Abuse? (arXiv 2508.20097)
    publisher: Blair-Stanek, Holzenberger, Van Durme
    type: academic
    url: https://arxiv.org/abs/2508.20097
    date: '2025-08-10'
    access: full
    locator: abstract
  last_reviewed: '2026-10-17'
  notes: IDEA from a research paper; no deployment. Arxiv v2, revised 21 Jan 2026. Tax-authority use is routed to controversy.
- id: tax-research-advisory-18
  title: Auditable statutory reasoning with LLMs plus logic programs (idea)
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - expert-judgment
  - review-assurance
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: LLM answers on tax rules are hard to audit, and the researchers argue accuracy and auditability are the bottleneck for any automated tax reasoning.
  solution: 'Idea (labelled): translate plain-text rules into formal logic programs and have a symbolic solver compute results, with LLMs doing the translation and case representation. Evaluated on the SARA statutory reasoning dataset with a cost model based on real-world penalties; accepted to AAAI 2026.'
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: none published
    provenance: self-reported
    source_ref: n/a
  prerequisites:
  - Formalised rule sets
  risks_and_guardrails:
  - Evaluated on a benchmark, not in practice
  human_checkpoints:
  - Not described
  role_evolution: Not discussed.
  evidence_grade: D
  sources:
  - ref: JHU-TAXREASON-2025
    title: Language Models and Logic Programs for Trustworthy Tax Reasoning (arXiv 2508.21051)
    publisher: Johns Hopkins University authors; AAAI 2026
    type: academic
    url: https://arxiv.org/abs/2508.21051
    date: '2025-08-28'
    access: full
    locator: abstract
  - ref: COLUMN-TAXCALCBENCH-2025
    title: 'TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task (arXiv 2507.16126)'
    publisher: Column Tax authors
    type: academic
    url: https://arxiv.org/abs/2507.16126
    date: '2025-07-22'
    access: full
    locator: abstract (frontier models calculated fewer than a third of simplified returns; adjacent to this module)
  last_reviewed: '2026-10-17'
  notes: IDEA from academic work; TaxCalcBench concerns return calculation, not research, and is cited only as context for why auditable approaches are proposed.
```

## 3. Module notes

### Processes and key steps (with work types)

- **Frame the question from client facts.** Extract the fact pattern from what the client sent, then identify the issues and turn them into specific tax questions (`client-interaction`, `expert-judgment`). Accordance describes a five-step practice process this way: extract facts, identify issues, locate authority, evaluate relevance and weight, develop recommendations with risks declared [ACCORDANCE-BDO-2026, section 'Purpose-built AI is the Real Innovation'].
- **Locate and read authority** (`research-synthesis`): code, regulations, cases, rulings, commentary. In-house and firm teams run several tools; Blue J and CPA.com's 2025 respondents had access to three on average [BLUEJ-OUTLOOK-2025, State of Tax Research Solutions].
- **Analyse and conclude** (`expert-judgment`), including planning and structuring advice such as S-corporation election analysis [ACCORDANCE-FINNEY-2025].
- **Document the position** (`document-production`): technical memos, workpaper footnotes, client emails. An in-house M&A tax role at Anthropic lists preparing technical tax memoranda that support internal sign-off, the financial statement audit and return positions [ANTHROPIC-JOB-2026, responsibilities].
- **Review and verify** (`review-assurance`): partner or national-office review; since 2026 an explicit check that cited authority exists and supports the point [JOFA-CLINCO-2026; IRS-OPR-2026].
- **Transaction work** (`review-assurance`, `document-production`): tax diligence, risk quantification, structuring, drafting tax provisions in purchase agreements, post-closing integration [ANTHROPIC-JOB-2026; KPMG-MA-2025].
- **Maintain knowledge** (`coordination-scheduling`): playbooks, diligence checklists [ANTHROPIC-JOB-2026]; internal guidance kept beside authoritative content in a knowledge base [TR-COCOUNSELCORP-2026].

### Common pain points

- Legacy research tools get used less than paid for: 50% to 61% weekly or daily use, versus 88% weekly or daily for those with access to AI-powered tax research tools, in Blue J and CPA.com's 2025 survey (a vendor survey) [BLUEJ-OUTLOOK-2025, Where Legacy Solutions Are Failing Firms]. 81.3% of respondents also turned to search engines.
- Gray-area questions consume most of a day across several databases, and subscription costs bite: one firm began looking for a replacement when Bloomberg's price was set to nearly double [ACCORDANCE-WFY-2026, Challenge].
- Client questions that need research mean call-backs [ACCORDANCE-BARNES-2026, Challenge].
- Tax departments are stretched: 58% of 288 surveyed corporate tax departments said they were under-resourced (51% the year before) and spent more than half their time on reactive work [TR-CORPTAX-2025].
- Verification burden and silent errors: attendees at TEI's Tax Technology Seminar 2026 described errors that are 'polite, quiet and technical' and hard to review at volume [TR-TEITAXTECH-2026, 'A very bad wizard'].

### Metrics and benchmarks (what each figure measures)

| Figure | What it measures | Source | Provenance |
|---|---|---|---|
| 60% (2026) vs 33% (2025) | Respondents who work for firms that have adopted AI-powered tax research; 1,000 US accountants surveyed 12-23 Mar 2026 vs 150+ practitioners in 2025; samples differ | [BLUEJ-OUTLOOK-2026, Key Finding 1; Appendix] | vendor-published |
| 80% (2026) vs 54% (2025) | Respondents using AI for tax research on a weekly or monthly basis (2026) / regularly (2025) | [BLUEJ-OUTLOOK-2026, AI Usage Trends] | vendor-published |
| 90% vs 46% | Respondents with access to general-purpose AI vs tax-specific AI for tax research | [BLUEJ-OUTLOOK-2026, The Current Toolkit] | vendor-published |
| 81% | Tax and audit professionals using AI tools regularly (Thomson Reuters 2026 Future of Professionals survey) | [TR-FOP-2026] | vendor-published |
| 67% | Of 288 corporate tax departments, share not using GenAI (2025) | [TR-CORPTAX-2025] | vendor-published |
| 71% / 66% | Companies surveyed using AI tools in tax departments / share of those users reporting noticeable time savings (KPMG Germany quick surveys; sample size not stated) | [KPMG-DE-2026] | self-reported |
| 2.94 hours/week | Respondent-reported time saved across research and drafting (Blue J user survey) | [BLUEJ-OUTLOOK-2025] | vendor-published |
| 1 hr to 10 min; 1.5 days to 3 hrs; 8 hrs to 1 hr; 2-6 hrs to 15-20 min; 10 hrs to 2-2.5 hrs | Single-task before-and-after estimates by named firms (use cases 1-3) | [ACCORDANCE-SASSERATH-2025; ACCORDANCE-BARNES-2026; ACCORDANCE-WFY-2026; ACCORDANCE-FINNEY-2025] | vendor-published |
| <0.2% | Rate users disagree with Blue J's answers (not audited accuracy) | [BLUEJ-OUTLOOK-2025] | vendor-published |
| 2,000,000 questions by Jul 2025; +735% YoY (Jul 2024 to Jul 2025); 9 million to date | Blue J questions answered, per Blue J user data | [BLUEJ-OUTLOOK-2025; BLUEJ-OUTLOOK-2026, About Blue J] | vendor-published |
| 39% to 47% | Share of ChatGPT 3.5/4 answers to common taxpayer tax questions judged correct across the 2023 and 2024 filing seasons (consumer questions, older models; adjacent to professional research) | [ANTINOZZI-2024] | independent |
| fewer than one third | Simplified federal returns that frontier models calculated correctly (return calculation, not research; adjacent) | [COLUMN-TAXCALCBENCH-2025] | independent (authors' company sells a tax engine) |
| nearly 800 | AI-related citation errors found in disciplinary actions and court records in at least 25 countries by late 2025, per a January 2026 paper that Bloomberg Tax cites (second-hand) | [BTAX-HALLUC-2026] | vendor-published |
| 1,300+ firms | Firms using CoCounsel (Thomson Reuters company claim, Nov 2025) | [TR-COCOUNSEL-2025] | vendor-published |
| 10x in six months | Usage growth Accordance reports (Sept 2025) | [ACCORDANCE-RAISE-2025] | vendor-published |

**Absent evidence:** no error rate, override rate, parallel-run result, inspection finding or independent head-to-head test of a commercial tax research tool was found. Thomson Reuters markets 'Fiduciary-Grade AI' and Bloomberg markets 'verified' tools, but the pages read give no accuracy figures.

### Guardrails and regulatory points

- **IRS OPR Alert 2026-19 (24 Jun 2026):** existing Circular 230 duties apply: due diligence (s10.22: verify facts, citations and calculations the AI produces), fees (s10.27(a): billing for manual time not spent may violate the rule depending on the facts; pass savings on openly), competence (s10.35: understand the tool's limits) and procedures (s10.36: principal-authority individuals must ensure adequate firm procedures) [IRS-OPR-2026]. It also notes that cases sanctioning other kinds of tax professionals are 'slowly emerging' and cites Deloitte Australia's refund of part of a fee over an AI-tainted report [IRS-OPR-2026, Real-World Consequences].
- **Tax Court, *Clinco*, T.C. Memo. 2026-16:** counsel's brief cited four cases for a signature argument; the court called three probable LLM hallucinations; counsel did not correct the record after the IRS flagged them; the court stopped short of sanctions but warned 'a recipe for sanctions' [JOFA-CLINCO-2026]. JofA lists suggested firm policy elements: permitted and prohibited uses, treat AI text as a draft, human verification of all authorities, data-handling protocols, training, vendor vetting, supervisory review, documentation [JOFA-CLINCO-2026].
- **UK PCRT bodies (19 Jan 2026):** seven bodies issued topical guidance applying PCRT's principles (integrity, bias and due care, confidentiality, limits of AI) [PCRT-AI-2026].
- **AICPA Council on AI Risk in Tax (Sept 2026):** a cross-sector council to test Danny Werfel's AI Risk Framework for Tax, which has 20 risk areas in four categories [AICPA-CART-2026].
- **Vendor-side controls:** SOC 2 Type 2 report, no training on client data, encrypted uploads [BLUEJ-ENTERPRISE-2026]; Accordance says it is never trained on customer data [ACCORDANCE-HOME-2026].

### Frontier signals (dated)

- 2025-09-08: Accordance launches publicly with $13M, positioning a multi-agent AI for tax and accounting, backed by Khosla Ventures and General Catalyst, with Anthropic among investors [ACCORDANCE-RAISE-2025].
- 2025-08-04: Blue J raises $122M Series D and says it more than doubled revenue and customers in the first half of 2025 [BLUEJ-SERIESD-2025].
- 2025-11-25: EY announces EY.ai Tax Labs and the EY.ai Tax Agent Factory for building and managing agents with clients [EY-TAXLABS-2025].
- 2026-03-09: Bloomberg Tax announces a Deep Thinking Mode that builds and executes a research plan for multi-step questions [BTAX-TOOLS-2026].
- 2026-05-01: Thomson Reuters positions tax research as 'reason-and-act' [TR-AGENTICBLOG-2026].
- 2026-05-20: KPMG and Anthropic announce Digital Gateway Powered by Claude, tax clients first [KPMG-ANTHROPIC-2026].
- 2026-06-24: OPR guidance on AI in federal tax practice [IRS-OPR-2026]. 2026-09-23: CART launched [AICPA-CART-2026].
- 2026-05-11: Accordance reports a BDO Alliance Innovation Award and says it is in 'hundreds of firms' (vendor claim) [ACCORDANCE-BDO-2026]. Blue J's March 2026 survey frames the market as moving from 'trying' to 'relying' (vendor framing) [BLUEJ-OUTLOOK-2026].
- 2026-10-16: Blue J publishes an enterprise buyer's scorecard covering adoption, content coverage and answer and citation quality, a sign that large-firm procurement is being formalised (vendor content) [BLUEJ-ENTERPRISE-2026].
- 2025-08 and 2026-02 (revision): academic work proposes LLM plus logic-program reasoning for auditable tax answers [JHU-TAXREASON-2025].

### Workforce and role effects

- New titles: Tax AI Leader (Crowe), US AI Tax Leader (PwC), Tax Technology and AI roles; Blue J's careers page lists an open 'Director, Tax Research' role in its Legal Research team [BLUEJ-CROWE-2024; PWC-MEGNA-2025; BLUEJ-CAREERS-2026].
- PwC reports over 3,200 AI champions, about 80% of US people trained, and that policy interpretation and high-touch consulting remain areas of limited AI use [PWC-MEGNA-2025].
- Junior staff: Blue J reports 40.8% of its users are associates [BLUEJ-OUTLOOK-2025]; TR Institute warns early-career staff still need supervised development [TR-FOP-2026]; partners at several firms say staff who disliked research now find it easier [ACCORDANCE-SASSERATH-2025; ACCORDANCE-FINNEY-2025].
- Headcount: 58% of companies in KPMG Germany's quick survey expect stable domestic tax headcount [KPMG-DE-2026]. Sala argues corporate tax teams will shrink little because tax practice is more than preparation [SALA-TAXNOTES-2026]. Deloitte's scenarios describe tax professionals moving from preparation to oversight, interpretation, policy interaction and dispute resolution [DELOITTE-TTT-2026].
- Billing and talent: more than a quarter of surveyed professionals say they would not accept a job at a firm lacking professional-grade AI [TR-FOP-2026].

### Objections and concerns practitioners raise

- Hallucinated authority and the duty to verify [BTAX-HALLUC-2026; JOFA-CLINCO-2026; IRS-OPR-2026].
- Errors that fail 'quietly and even politely', and no clear owner for AI in tax: two of more than 50 attendees polled said tax owns AI implementation at their company [TR-TEITAXTECH-2026].
- Unapproved tool use: more than one third of professionals admit it [TR-FOP-2026]; Blue J's reading of its survey gap suggests more [BLUEJ-OUTLOOK-2026].
- Confidentiality across clients [IRS-OPR-2026].
- Culpability stays with people [SALA-TAXNOTES-2026].
- Fee fairness when AI cuts hours [IRS-OPR-2026; BTAX-PRICING-2026].
- Rising token costs that could change the economics of automation, raised at TEI Tax Tech 2026 [TR-TEITAXTECH-2026].
- Whether tax rules built on human activity (nexus, value creation) still fit, raised at the D.C. Bar tax conference [DCBAR-TAX-2026].
- Conference coverage of the topic is thin and vendor-adjacent: IBFD's IFA Lisbon seminar on GenAI for tax research had Blue J's CEO among its speakers [IBFD-IFA-2025], and TEI Midyear's research Tax Labs were run with Thomson Reuters and Accordance [TEI-MIDYEAR-2026].

### Interview probes for an adviser

1. Which research questions go to the AI tool first, which go straight to a senior or the national office, and how is that line drawn and written down?
2. When the tool gives a cited answer, who checks the authority, how is the check recorded, and what has it caught in the last six months?
3. How have time capture, fixed-fee scoping and engagement letters changed as research time fell, and have you reviewed them against OPR's fee point?
4. Which tools are sanctioned, which do staff use anyway, and who owns tax AI in the firm or department?
5. How would you know if the tool's answer was wrong or the user overrode it, and do you track disagreements, rework or review comments at all?

## 4. Routed to other modules

- **compliance:** Thomson Reuters Ready to Review agentic 1040 preparation and the CLH CPAs one-hour-per-simple-1040 quote [TR-COCOUNSEL-2025]; PwC K-1 data mapping with confidence flags and override reasons [PWC-MEGNA-2025]; RSM's myRSM Tax platform [RSM-MYRSM-2025]; EY compliance agents [EY-TAXLABS-2025].
- **provision:** PwC's model that calculates effective tax rates and explains inputs, assumptions and logic as part of the deliverable [PWC-MEGNA-2025]; Bloomberg Tax's point that one wrong assumption can flow through provision, ETR and disclosure [BTAX-HALLUC-2026].
- **controversy:** drafting responses to IRS notices (Blue J Tax Writing) [BLUEJ-WRITING-2026]; the TEI Midyear 'Managing Tax Notices with AI' lab [TEI-MIDYEAR-2026]; tax authorities arriving at audits with structured data already analysed [TR-TEIAUDITOR-2026]; LLMs identifying abusive strategies for tax agencies [JHU-TAXABUSE-2025]; *Clinco* as litigation conduct [JOFA-CLINCO-2026].
- **tax-data-technology:** Oxford Industries and Savant's 'AI Transformed Tax Processes' session on audit-ready agent automation [SAVANT-OXFORD-2026]; TEI attendees' data-pipeline tooling lists and vibe-coding control gaps [TR-TEIAUDITOR-2026]; KPMG Germany's adoption survey [KPMG-DE-2026].
- **audit (outside the tax archetype):** Harris, Hardy & Johnstone's use of the tool for board minutes, leases and contracts [TR-HHJ-2026].
- **cross-cutting governance (all tax modules):** OPR Alert 2026-19, PCRT guidance, CART/Werfel framework [IRS-OPR-2026; PCRT-AI-2026; AICPA-CART-2026].
- **tax-policy of AI (frontier note):** nexus and value-creation questions from the D.C. Bar panel (Herzfeld, Bonovich of OpenAI, Christenson of Baker McKenzie, McDonald of PwC, Punchak of Treasury) [DCBAR-TAX-2026].

## 5. Sources

All rows below were opened and read in full for this deep dive (access: full) unless the Access column says otherwise. Dates: see notes in the Gaps section for the pages that do not state a publication date.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ACCORDANCE-BARNES-2026 | Barnes Wendling: From Hours to Minutes | Accordance | vendor | https://www.accordance.com/press/barnes-wendling-from-hours-to-minutes | 2026-06-19 | full |
| ACCORDANCE-BDO-2026 | BDO Alliance Recognizes Accordance as an Innovation Leader | Accordance | vendor | https://www.accordance.com/press/bdo-alliance-recognizes-accordance-as-an-innovation-leader | 2026-05-11 | full |
| ACCORDANCE-FINNEY-2025 | Finney, Neill & Company: Energizing the Practice | Accordance | vendor | https://www.accordance.com/press/finney-neill-company-energizing-the-practice | 2025-11 | full |
| ACCORDANCE-HOME-2026 | Accordance (home page) | Accordance (Agnetic Labs) | vendor | https://www.accordance.com | 2026-10-17 | full |
| ACCORDANCE-RAISE-2025 | Accordance Raises $13M from Khosla Ventures and General Catalyst | Accordance | vendor | https://www.accordance.com/press/accordance-raises-13m-from-khosla-ventures-and-general-catalyst | 2025-09-08 | full |
| ACCORDANCE-SASSERATH-2025 | Sasserath & Co. Accelerates Research by 80% and Shifts to Value-Based Billing | Accordance | vendor | https://www.accordance.com/press/sasserath-co | 2025-11 | full |
| ACCORDANCE-WFY-2026 | Wright Ford Young & Co.: Rebuilding Their Approach to Gray-Area Research | Accordance | vendor | https://www.accordance.com/press/wright-ford-young-co-rebuilt-their-approach-to-gray-area-research | 2026-07-22 | full |
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 | full |
| ANTHROPIC-JOB-2026 | M&A Tax Director (Anthropic job posting on General Catalyst job board) | Anthropic | job-posting | https://jobs.generalcatalyst.com/companies/anthropic/jobs/89778547-m-a-tax-director | 2026-08-13 | full |
| ANTINOZZI-2024 | Is ChatGPT an Accurate Source of Information for Uninformed Taxpayers? (abstract) | Wealth Strategies Journal (Antinozzi and Cooper) | academic | https://wealthstrategiesjournal.com/2024/06/30/hannah-smith-antinozzi-lauren-cooper-is-chatgpt-an-accurate-source-of-information-for-uninformed-taxpayers-june-18-2024/ | 2024-06-18 | full |
| BLUEJ-CAREERS-2026 | Careers (Blue J) | Blue J | job-posting | https://www.bluej.com/careers | 2026-10-17 | full |
| BLUEJ-CROWE-2024 | Blue J announces enterprise agreement with Crowe | Blue J (Business Wire release) | vendor | https://www.bluej.com/our-customers/blue-j-announces-enterprise-agreement-with-crowe-to-enhance-their-generative-ai-enabled-tax-services | 2024-10-22 | full |
| BLUEJ-ENTERPRISE-2026 | Best AI tax research tools for large and enterprise firms | Blue J | vendor | https://www.bluej.com/blog/best-ai-tax-research-tool-enterprise | 2026-10-16 | full |
| BLUEJ-HATRIDGE-2024 | Hatridge Tax & Accounting Grows Capacity as a Sole Proprietor through Blue J | Blue J | vendor | https://www.bluej.com/our-customers/hatridge-tax-accounting-grows-capacity-as-a-sole-proprietor-through-blue-j-ai-for-tax-research | 2024-09-30 | full |
| BLUEJ-HOME-2026 | AI Tax Research Platform (Blue J home page) | Blue J | vendor | https://www.bluej.com | 2026-10-15 | full |
| BLUEJ-LARSON-2025 | Larson Gross Advisors: Driving better client experiences with generative AI | Blue J | vendor | https://www.bluej.com/our-customers/larson-gross-advisors | 2025-04-16 | full |
| BLUEJ-OUTLOOK-2025 | The AI Tax Research Solution Outlook Report (2025 edition) | Blue J with CPA.com | survey | https://www.bluej.com/content/ai-tax-research-solution-outlook-report | 2025 | full |
| BLUEJ-OUTLOOK-2026 | 2026 AI Tax Research Solution Outlook Report | Blue J with CPA.com | survey | https://www.bluej.com/content/ai-tax-research-solution-outlook-report-2026 | 2026 | full |
| BLUEJ-SERIESD-2025 | Blue J Announces $122M Series D Financing | Blue J | vendor | https://www.bluej.com/blog/blue-j-announces-122m-series-d-financing-led-by-oak-hc-ft-and-sapphire-ventures | 2025-08-04 | full |
| BLUEJ-SSC-2025 | SSC CPAs + Advisors Elevates Tax Research with Blue J | Blue J | vendor | https://www.bluej.com/our-customers/ssc-cpas-advisors | 2025-10-17 | full |
| BLUEJ-WRITING-2026 | Tax Writing (Blue J product page) | Blue J | vendor | https://www.bluej.com/tax-writing | 2026-10-17 | full |
| BLUEJ-WTP-2023 | Whiteford, Taylor & Preston has partnered with Blue J | Blue J | vendor | https://www.bluej.com/our-customers/whiteford-taylor-preston-has-partnered-with-bluej | 2023-08-02 | full |
| BTAX-HALLUC-2026 | AI Hallucinations in Tax: The Risks and How to Mitigate Them | Bloomberg Tax | vendor | https://pro.bloombergtax.com/?p=16920 | 2026-05-11 | full |
| BTAX-PRICING-2026 | AI Efficiency Gains Push Accounting Firms to Reimagine Pricing | Bloomberg Tax (Daily Tax Report) | press | https://news.bloombergtax.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing | 2026-03-05 | full |
| BTAX-TOOLS-2026 | Bloomberg Tax Showcases Industry-Leading AI-Powered Tools at TEI Midyear 2026 | Bloomberg Tax | vendor | https://pro.bloombergtax.com/insights/company-news/bloomberg-tax-showcases-industry-leading-ai-powered-tools-at-tei-midyear-2026 | 2026-03-09 | full |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task (arXiv 2507.16126) | Column Tax authors | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 | full |
| DCBAR-TAX-2026 | Rise of the Machines: How Artificial Intelligence Is Changing the Tax World (2026 D.C. Bar Tax Conference) | D.C. Bar | conference | https://events.dcbar.org/Tax2026/session/3513387/rise-of-the-machines-how-artificial-intelligence-is-changing-the-tax-world | 2026-01-08 | full |
| DELOITTE-TTT-2026 | Tax Transformation Trends, AI report part three: Riding the wave: A framework to plan for AI | Deloitte Global | firm | https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf | 2026-07 | full |
| EY-TAXLABS-2025 | EY unveils suite of powerful AI capabilities to accelerate tax transformation and deliver strategic value | EY | firm | https://www.ey.com/en_gl/newsroom/2025/11/ey-unveils-suite-of-powerful-ai-capabilities-to-accelerate-tax-transformation-and-deliver-strategic-value | 2025-11-25 | full |
| IBFD-IFA-2025 | IBFD Dialogues Seminar at IFA Lisbon 2025: Unlocking the Potential of Generative AI for Tax Professionals | IBFD | conference | https://www.ibfd.org/events/ibfd-dialogues-seminar-ifa-lisbon-2025-0 | 2025-10-06 | full |
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19) | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| JHU-TAXABUSE-2025 | Can LLMs Identify Tax Abuse? (arXiv 2508.20097) | Blair-Stanek, Holzenberger, Van Durme | academic | https://arxiv.org/abs/2508.20097 | 2025-08-10 | full |
| JHU-TAXREASON-2025 | Language Models and Logic Programs for Trustworthy Tax Reasoning (arXiv 2508.21051) | Johns Hopkins University authors; AAAI 2026 | academic | https://arxiv.org/abs/2508.21051 | 2025-08-28 | full |
| JOFA-CLINCO-2026 | A recipe for sanctions: AI-hallucinated citations in tax | Journal of Accountancy (AICPA) | press | https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/ | 2026-09-01 | full |
| KPMG-ANTHROPIC-2026 | KPMG Partners with Anthropic for Digital Gateway Powered by Claude | CPA Practice Advisor (reproducing the announcement) | press | https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/ | 2026-05-20 | full |
| KPMG-DE-2026 | Tax departments are increasingly turning to artificial intelligence (KPMG Germany quick surveys) | KPMG Germany | survey | https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html | 2026-05-07 | full |
| KPMG-MA-2025 | How generative AI is transforming mergers and acquisitions tax: The KPMG approach | KPMG US | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/how-generative-ai-transforming.pdf | 2025-06 | full |
| PCRT-AI-2026 | Professional bodies issue AI advice to members | Association of Taxation Technicians (for the seven PCRT bodies) | standard-setter | https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members | 2026-01-19 | full |
| PWC-MEGNA-2025 | How PwC's tax team is using agentic AI (interview with Dom Megna) | CFO.com | press | https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/ | 2025-06-06 | full |
| RSM-MYRSM-2025 | RSM Expands AI Commitment with Launch of myRSM Tax | RSM US | firm | https://rsmus.com/newsroom/2025/rsm-expands-ai-commitment-with-launch-of-myrsm-tax.html | 2025-06-16 | full |
| SALA-TAXNOTES-2026 | AI Won't Shrink Corporate Tax Teams Much. Here's Why. (Sala, Tax Notes State 121:189; abstract on TaxProf Blog) | Tax Notes / TaxProf Blog | press | https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/ | 2026-07-20 | full |
| SAVANT-OXFORD-2026 | Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Tech Seminar 2026 | Savant Labs | vendor | https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/ | 2026-04-16 | full |
| TEI-MIDYEAR-2026 | TEI Midyear Conference 2026 at-a-glance agenda | Tax Executives Institute | conference | https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf | 2026-03-15 | full |
| TR-AGENTICBLOG-2026 | An evolution of tax tools and how agentic AI will shape 2026 | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/an-evolution-of-tax-tools-and-how-agentic-ai-will-shape-2026/ | 2026-05-01 | full |
| TR-COCOUNSEL-2025 | Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows | 2025-11-05 | full |
| TR-COCOUNSELCORP-2026 | CoCounsel Tax: The AI tax assistant for in-house teams | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/products/cocounsel-tax/corp | 2026-10-17 | full |
| TR-CORPTAX-2025 | The GenAI paradox: why most tax departments aren't using AI yet (2025 State of the Corporate Tax Department) | Thomson Reuters Tax & Accounting | survey | https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/ | 2025-10-22 | full |
| TR-FOP-2026 | What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07-21 | full |
| TR-HHJ-2026 | Elevating audit and advisory work with CoCounsel Tax & Audit (Harris, Hardy & Johnstone) | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/insights/case-studies/elevating-audit-and-advisory-work-with-cocounsel-tax-and-audit | 2026-03 | full |
| TR-JANSEN-2026 | How Jansen & Company CPAs delivers higher-value tax advice with CoCounsel Tax | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/insights/case-studies/how-jansen-and-company-cpas-is-delivering-higher-value-tax-advice-at-scale-with-cocounsel-tax | 2026-02 | full |
| TR-TEIAUDITOR-2026 | 2026 TEI Tax Technology Seminar: What the auditor already knows | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows | 2026-05-12 | full |
| TR-TEITAXTECH-2026 | 2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 | full |
| V7-TAXDD-2026 | AI Tax Due Diligence Agent (V7 Go) | V7 | vendor | https://www.v7labs.com/agents/ai-tax-due-diligence-agent | 2026-10-17 | full |

Source count by type: academic 4, conference 3, firm 4, job-posting 2, press 7, professional-body 1, regulator 1, standard-setter 1, survey 5, vendor 25. Total 53.

## 6. Gaps

- **Web search ran out mid-task.** The shared search budget was used up before the planned searches on independent accuracy tests of tax research tools, sanctions of tax practitioners for AI citations, and in-house case studies. Those directions were not pursued by other routes.
- **No independent quality evidence for commercial tax research tools.** No head-to-head accuracy test, override rate, parallel-run result or inspection finding was found. All time and quality figures for the tools come from the vendors or from customers quoted by vendors. Accordance's claim of outperforming foundation models and the TaxGPT benchmark (listed in the landscape) were not tested or opened.
- **In-house tax counsel practice is thin.** No named in-house department published research outcomes. Oxford Industries (with Savant) is about automation, not research. TEI's Tax Labs on research (Thomson Reuters CoCounsel and Accordance) appear only as agenda titles.
- **M&A tax diligence:** only KPMG US describes a named toolset, with no measurements; V7's agent page is an undated vendor demo with no named customer. No law-firm or Big Four case with outcomes was found.
- **Job postings:** the AI-in-tax roles found by search (KPMG UK 'AI Senior Manager, Tax Technology & Innovation', EY Manager and Senior Manager AI/tax technology roles, a Deloitte UAE tax GenAI manager role) had closed or could not be read when fetched, so their duties are not used. Read in full: Anthropic's M&A Tax Director (no AI duties stated) and Blue J's careers page (a 'Director, Tax Research' role is listed, without a description).
- **Not reached or not opened:** Wolters Kluwer CCH AnswerConnect and Expert AI Advisor pages (bot wall; only the generic AnswerConnect page loaded and it had nothing usable), LexisNexis/Tolley+ with Protegé, Tax Notes and IBFD research AI products, Harvey (no tax-specific page found), PwC UK's Harvey-based tax assistant (landscape lists it as search-only), TaxGPT, Bloomberg Tax's paywalled coverage of the Tax Court's rules discussion, the January 2026 International Tax Journal paper on citation errors, the *Clinco* opinion itself (JofA's account used), Swider (AAA 2025) on taxpayer reliance, Australia's TPB guidance.
- **Dates not stated on the page:** both Blue J outlook reports (2025 and 2026; the 2026 survey ran 12-23 Mar 2026), Blue J home page (last-published stamp used), Blue J Tax Writing page, Thomson Reuters CoCounsel Tax in-house page, V7 page, Accordance home page (access date used), and the two Thomson Reuters customer case studies (2026-03 and 2026-02 taken from page timestamps). Accordance case-study dates (2025-11, 2026-06-19, 2026-07-22, 2026-05-11, 2025-09-08) come from the site's content timestamps. KPMG's M&A tax article shows a 2025 PDF and a 29 Jul 2026 web datePublished; the earlier PDF date is used.
- **Scope limits:** UK, Australian and other non-US practice is covered only through the PCRT guidance. SALT-specific and trusts-and-estates advisory practice appears only in passing (Jansen & Company).

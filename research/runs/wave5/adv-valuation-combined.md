# Advisory / Valuation: combined deep dive (practice, discourse, governance and evidence)

Run date: 2026-10-20. Wave 5. Archetype: `advisory`. Module: `valuation`. Angle: combined.

Source refs follow `PUBLISHER-SHORT-YYYY`. Refs shared with `landscape-advisory.md` or other wave 5 files reuse the same spelling (IVSC-IVSED-2026, IVSC-PULSE-2026, BVR-AICPAAIGUIDE-2025, BVR-AICPAREPORT-2026, BVR-IVSPODCAST-2026, BVR-NACVA-2026, ACCTODAY-VPF-2026, AICPA-FVS-2026, BRATTLE-INSOL-2025, SEC-RULE2-01-2026). Where a source's date differs from the landscape, the date here is the one read on the page.

## 1. Summary

**Overall picture.** Public evidence on AI in valuation is thin and uneven. Standards and guidance are well documented. Named deployments are few, mostly vendor or product announcements, and nothing published measures error, override or parallel-run results for AI-assisted valuation. Of 16 use cases, grades are A: 0, B: 4, C: 8, D: 4 (see section 2).

- **Standards are the richest evidence.** The IVSC exposure draft (consultation 31 Jan to 30 Apr 2026) would add mandatory requirements on significant use of AI or other technology-based tools to IVS 101 scope of work, IVS 104 data and inputs, IVS 105 models and IVS 106 documentation and reporting, plus a new quality-controls chapter (IVS 107); the next IVS is planned for publication on 31 Jan 2027 with effect from 31 Jan 2028, subject to responses (IVSC-IVSED-2026 pages 3-4, 7). The Appraisal Standards Board adopted AO-41 on technology and AI on 23 Apr 2026, effective immediately, with no new USPAP requirements (BVR-AO41ADOPT-2026; ISA-AO41-2026). The AICPA FVS Executive Committee issued members-only, non-authoritative AI guidelines in Oct 2025 (BVR-AICPAAIGUIDE-2025).
- **The common message from standard-setters and practitioners:** the valuer stays responsible. No separate "AI standards" are expected; existing NACVA, AICPA, ASA, USPAP and IVS obligations apply (BVR-EWART-2026).
- **Practice evidence is concentrated in tools, not in advisory-firm case studies.** The named practice evidence is: accounting-firm users of a valuation platform (Kreston Reeves, Rouse, RXM, PKF FI; vendor case studies, December 2025, automation rather than clearly generative AI); KPMG saying it is working to embed AI in valuation tasks (a conference panel); Hamilton Lane (in-house) with 73 Strings; and launches by Stout (Drivr, July 2026) and Kroll (REVS, March 2026). No named US mid-market accounting firm described its own valuation AI use in the sources reached.
- **Discourse is active and cautious.** Themes: clients now run AI on valuers' reports, "cognitive debt", an "algorithmic monoculture", discoverability of prompts, fewer entry-level hires and how juniors learn the method (BVR-NACVA-2026; BVR-COGDEBT-2026; BVR-MONOCULTURE-2026; BVR-DISCOVERY-2026; BVR-KPMGTREND-2026).
- **Quality evidence is almost entirely absent.** The independent items found are indirect: a court that reran a Copilot calculation and got different numbers (GOLDMAN-WEBER-2024), a preprint where a specialist model beat frontier LLMs at forecasting statements (ARXIV-FORMA-2026), and PCAOB inspection findings that show valuation work was under scrutiny before AI (BVR-PCAOBINSP-2026).
- **Purchase price allocation, impairment testing and fairness opinions:** no public deployment evidence of AI was found. The only touchpoints are KPMG naming attrition analysis among its AI uses, and Big Four panellists naming AI governance and ASC 360 impairment testing among areas needing fresh guidance (BVR-KPMGTREND-2026; BVR-BIG4GUIDANCE-2026, summary).
- **Independence.** Valuation services for an SEC-registrant audit client are restricted where the results will be subject to audit procedures (SEC-RULE2-01-2026, 17 CFR 210.2-01(c)(4)(iii)). Non-SEC audit clients are governed by AICPA and other rules that were not opened for this run; treat the restriction as client-specific and confirm per engagement.

## 2. Use cases

Grade counts: A: 0, B: 4, C: 8, D: 4. Each entry notes the firm type where one applies (Big Four, accounting firm, advisory firm, vendor, AI-native provider, in-house team). "Maturity" follows the vocabulary: `in-production` needs a named organization.

```yaml
- id: advisory-valuation-01
  title: Plain-language research agent over private-company transaction, control-premium and marketability-discount datasets, with drill-through to the underlying transactions
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - research-synthesis
  - data-reporting
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Valuers search transaction and discount databases by hand, filtering and re-filtering comparables as they learn more about the subject company.
  solution: 'BVR''s Research and Data Agent (RADA) lets a user query DealStats, BIZCOMPS, the FactSet/BVR Control Premium Study, the Stout Restricted Stock Study and the Valuation Advisors DLOM study in plain language and returns calculations, tables and graphs. A ''Display Transactions'' feature opens the underlying observations, and ''Saved Threads'' keeps the research for an engagement so it can be refined later. Vendor: BVR (a publisher and data vendor; not a firm).'
  outcomes:
  - lever: speed
    description: BVR describes RADA in DealStats as moving comparable analysis from hours to seconds; no measurement is published.
    figure: none published (vendor describes 'hours into seconds')
    measures: Vendor's marketing wording about comparable-transaction analysis time; no sample, baseline or method stated
    provenance: vendor-published
    source_ref: BVR-RADAPRODUCT-2026
  - lever: quality
    description: BVR advises users to open the transactions behind each answer and judge whether they suit the valuation.
    figure: none
    measures: Guidance on use, not a measured result
    provenance: vendor-published
    source_ref: BVR-RADATIP-2026
  prerequisites:
  - Subscription to the underlying BVR datasets (RADA is stated to be included at no extra cost for subscribers to the four expanded resources)
  - Analyst able to judge whether the retrieved transactions are comparable
  risks_and_guardrails:
  - BVR says RADA in BVResearch Pro draws on BVR's vetted content and does not go out to the internet (BVR-RADAJUNIOR-2026); this is stated for that product, not for the transaction datasets
  - 'BVR''s own tip tells users not to stop at the answer: inspect the underlying transactions before relying on a result'
  human_checkpoints:
  - Analyst reviews the underlying transactions and decides which are appropriate for the subject company
  - Analyst owns the selection and the conclusion
  role_evolution: BVR positions the tool as combining AI efficiency with professional judgment that stays with the analyst; no role change is documented.
  evidence_grade: C
  sources:
  - ref: BVR-RADAPRODUCT-2026
    title: BVR's Research and Data Agent (product page; undated, date = access date)
    publisher: Business Valuation Resources
    type: vendor
    url: https://www.bvresources.com/products/research-and-data-agent
    date: '2026-10-20'
    access: full
    locator: RADA in DealStats section; 'How RADA works' list
  - ref: BVR-RADAEXPAND-2026
    title: AI-powered RADA expands to more BVR resources (BVWire)
    publisher: Business Valuation Resources
    type: press
    url: https://www.bvresources.com/articles/bvwire/ai-powered-rada-expands-to-more-bvr-resources
    date: '2026-09-16'
    access: full
    locator: paragraphs 1-2 (expansion to four datasets; Display Transactions; no extra cost)
  - ref: BVR-RADATIP-2026
    title: 'RADA tip of the week: Check the transactions behind the answer (BVWire)'
    publisher: Business Valuation Resources
    type: vendor
    url: https://www.bvresources.com/articles/bvwire/rada-tip-of-the-week-check-the-transactions-behind-the-answer
    date: '2026-09-23'
    access: full
    locator: '''Key point'' paragraph'
  - ref: BVR-RADAJUNIOR-2026
    title: 'RADA tip of the week: Use RADA to train junior analysts (BVWire)'
    publisher: Business Valuation Resources
    type: vendor
    url: https://www.bvresources.com/articles/bvwire/rada-tip-of-the-week-use-rada-to-train-junior-analysts
    date: '2026-05-06'
    access: full
    locator: paragraph 2 (content limited to BVR's vetted content)
  last_reviewed: '2026-10-20'
  notes: 'Grade C: product and vendor claims only. No named firm user, no error or override rate. Maturity is ''announced'' because availability is documented but named customer use is not. The ''AI-powered'' label and the ''does not go beyond BVR''s walls'' point are BVR''s own descriptions (BVR-RADAJUNIOR-2026).'
- id: advisory-valuation-02
  title: Big Four valuation teams apply AI to comparable-company screening, volatility and customer-attrition analysis, technical research and information requests
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - research-synthesis
  - data-reporting
  - expert-judgment
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Valuation engagements involve repetitive analytical and research steps (peer screens, volatility, attrition cohorts, client information requests) that consume junior analyst hours.
  solution: 'At the ASA Fair Value Conference (New York, May 2026) a KPMG panellist said the firm is working to embed AI ''into everything that we do'', with applications ranging from information requests, meeting summaries and technical research to volatility analysis, attrition analysis and comparable-company screening. Other Big Four panellists described AI as increasingly part of valuation workflows and stressed judgment, review and auditability. Separately, KPMG announced (May 19, 2026) an alliance giving all of its 276,000+ people access to Claude. Firm type: Big Four.'
  outcomes:
  - lever: capacity
    description: Panellists said firms are hiring fewer entry-level analysts as AI automates part of the mechanical work (reported by BVWire; no count given).
    figure: none published
    measures: Panel statement reported by trade press; no hiring numbers, firm names or time period for the hiring comment
    provenance: self-reported
    source_ref: BVR-KPMGTREND-2026
  prerequisites:
  - Enterprise access to an AI platform (KPMG alliance announcement covers firm-wide Claude access)
  - Review procedures and auditability, which the panel called essential
  risks_and_guardrails:
  - Panellists stressed professional judgment, review procedures and auditability (BVR-KPMGTREND-2026)
  - Under SEC Rule 2-01(c)(4)(iii), valuation services for an SEC-registrant audit client are barred where the results will be subject to audit procedures, so a Big Four firm's valuation work for its own audit clients is restricted regardless of tooling (SEC-RULE2-01-2026)
  human_checkpoints:
  - Reviewer sign-off on AI-assisted analyses (stated as essential by panellists)
  role_evolution: Fewer entry-level analyst hires, and open questions about how future valuation professionals will be trained (BVR-KPMGTREND-2026).
  evidence_grade: B
  sources:
  - ref: BVR-KPMGTREND-2026
    title: KPMG's AI push reflects a broader trend in valuation (BVWire, ASA Fair Value Conference panel)
    publisher: Business Valuation Resources
    type: conference
    url: https://www.bvresources.com/articles/bvwire/kpmgs-ai-push-reflects-a-broader-trend-in-valuation
    date: '2026-06-10'
    access: full
    locator: paragraphs 1-2
  - ref: ANTHROPIC-KPMG-2026
    title: KPMG integrates Claude across its core business and workforce of more than 276,000 in strategic alliance
    publisher: Anthropic
    type: vendor
    url: https://anthropic.com/news/anthropic-kpmg
    date: '2026-05-19'
    access: full
    locator: opening paragraphs (alliance; access for 276,000+ employees)
  - ref: SEC-RULE2-01-2026
    title: 17 CFR 210.2-01 Qualifications of accountants (current text, Cornell LII)
    publisher: SEC (Regulation S-X)
    type: regulator
    url: https://www.law.cornell.edu/cfr/text/17/210.2-01
    date: '2026-10-20'
    access: full
    locator: paragraph (c)(4)(iii)
  - ref: BVR-BIG4PANEL-2026
    title: Big Four Valuation Leaders Discuss AI, Tariffs, Pain Points, and More (Business Valuation Update; paywalled, summary read)
    publisher: Business Valuation Resources
    type: conference
    url: https://www.bvresources.com/articles/business-valuation-update/big-four-valuation-leaders-discuss-ai-tariffs-pain-points-and-more
    date: 2026-06
    access: search-only
    locator: summary (paywalled; AI, staffing pressures, client expectations)
  last_reviewed: '2026-10-20'
  notes: 'Grade B: a named firm (KPMG) is reported using AI on these tasks, with no published measurement. Maturity is ''piloting'' because the source says KPMG ''is working to embed'' AI and does not say which tasks run in production. The statement reaches us through a trade-press report of a panel, not a KPMG publication. The Anthropic release names tax, legal, private equity and cybersecurity as the alliance''s first uses and does not mention valuation. The other Big Four firms are not individually described.'
- id: advisory-valuation-03
  title: '''Standards analyzer'' and adversarial-reviewer agents that check a valuation report against standards and look for weak spots (idea)'
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Reports can contain every required section and still have missing or inconsistent requirements, unsupported assumptions, or arguments an opposing party could raise.
  solution: 'Speakers on an AICPA FVS podcast described an agent loaded with SSVS, U.S. GAAP and the AICPA forensic standard that flags missing or inconsistent requirements, and an ''adversarial reviewer'' that looks for weak spots, unsupported assumptions and inconsistencies. The IVSC dialogue panel (June 25, 2026) likewise encouraged using AI as a review tool that challenges assumptions. Idea: discussed by practitioners; no named deployment found.'
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: No measurement; the source describes the approach and its cautions only
    provenance: self-reported
    source_ref: BVR-AICPAREPORT-2026
  prerequisites:
  - Standards text available to the agent
  - Protected internal AI system, because the speakers warned against putting confidential client information into public AI tools
  risks_and_guardrails:
  - Speakers said AI does not replace professional review, that AI makes mistakes, and that the human remains responsible for the report (BVR-AICPAREPORT-2026)
  - Confidential client information should not go into public AI systems (BVR-AICPAREPORT-2026)
  human_checkpoints:
  - Valuer reviews and decides on each flag; signing valuer remains responsible
  role_evolution: Review shifts partly to challenging the agent's findings; no role change is documented.
  evidence_grade: D
  sources:
  - ref: BVR-AICPAREPORT-2026
    title: AI agents as a quality-control layer for valuation reports (BVWire, on an AICPA FVS podcast)
    publisher: Business Valuation Resources
    type: press
    url: https://www.bvresources.com/articles/bvwire/ai-agents-as-a-quality-control-layer-for-valuation-reports
    date: '2026-09-16'
    access: full
    locator: paragraphs 2-4 (Mission possible; cautions)
  - ref: BVR-IVSCDIALOGUE-2026
    title: 'Global: AI governance highlighted in latest IVSC Global Dialogue Series (BVWire)'
    publisher: Business Valuation Resources
    type: press
    url: https://www.bvresources.com/articles/bvwire/global-ai-governance-highlighted-in-latest-ivsc-global-dialogue-series
    date: '2026-08-05'
    access: full
    locator: paragraph 3 (AI as a review tool)
  - ref: IVSC-PERSPECTIVES-2025
    title: 'Navigating the Rise of Artificial Intelligence in Valuation: Opportunities, Risks, and Standards (Perspectives Paper)'
    publisher: International Valuation Standards Council
    type: standard-setter
    url: https://ivsc.org/wp-content/uploads/2025/07/Navigating-the-Rise-of-AI-in-Valuation-Opportunities-Risks-and-Standards.pdf
    date: '2025-07-23'
    access: full
    locator: page 8, IVS 100 and IVS 102 boxes (AI could be used in quality control and to review bases of value)
  - ref: AICPA-FVSPODCAST-2026
    title: Building More Defensible Valuation Reports (The FVS Valuation Podcast episode page)
    publisher: AICPA & CIMA
    type: podcast
    url: https://podcasts.apple.com/us/podcast/building-more-defensible-valuation-reports/id1551184348?i=1000787680655
    date: '2026-09-03'
    access: full
    locator: episode description (the episode exists and covers report defensibility; the AI discussion is known only through the BVR summary)
  last_reviewed: '2026-10-20'
  notes: 'Idea (grade D). The AI discussion in the episode is reported by BVWire; the episode audio was not heard, and the Apple episode page does not itself mention AI. Speakers: Bethany Hearn (MH CPA) and Dr. Victor Jarosiewicz (Georgia State), host Nene Glenn Gianfala (Chaffe & Associates).'
- id: advisory-valuation-04
  title: Valuation-reviewer agent template that checks valuations against comparables, methodology and the firm's review standards
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Reviewers of valuations (for example fund valuation committees and in-house teams) must check comparables, methods and policy compliance across many positions on a deadline.
  solution: Anthropic's May 5, 2026 release lists a 'Valuation reviewer' among ten agent templates; it checks valuations against comparables, methodology and the firm's review standards. Templates ship as plugins for Claude Cowork and Claude Code, and as cookbooks for Claude Managed Agents, with subagents for tasks such as comparables selection or methodology checks, and an audit log. Vendor announcement; no named customer for this template.
  outcomes:
  - lever: quality
    description: none published for the valuation-reviewer template
    figure: none
    measures: Announcement describes capability only
    provenance: vendor-published
    source_ref: ANTHROPIC-FSAGENTS-2026
  prerequisites:
  - Firm's own modelling conventions, risk policies and approval flows (the release says firms adapt the templates)
  - Governed connectors to market and private-company data
  risks_and_guardrails:
  - Release states users stay in the loop, reviewing and approving work before it goes to a client or is filed (ANTHROPIC-FSAGENTS-2026)
  - Managed-agent version offers per-tool permissions and a full audit log (ANTHROPIC-FSAGENTS-2026)
  human_checkpoints:
  - Human reviews, iterates and approves before client release or filing (per the release)
  role_evolution: Not stated.
  evidence_grade: C
  sources:
  - ref: ANTHROPIC-FSAGENTS-2026
    title: Agents for financial services (ten agent templates, including a valuation reviewer)
    publisher: Anthropic
    type: vendor
    url: https://www.anthropic.com/news/finance-agents
    date: '2026-05-05'
    access: full
    locator: paragraph listing the ten agents; paragraphs on templates, plugins and Managed Agents
  last_reviewed: '2026-10-20'
  notes: 'Grade C: vendor announcement. Anthropic also reports Claude Opus 4.7 at 64.37% on Vals AI''s Finance Agent benchmark (vendor-reported; a general finance-agent benchmark, not a valuation benchmark, so not used as an outcome). No evidence of use by an accounting or valuation firm.'
- id: advisory-valuation-05
  title: Portfolio valuation platform that extracts portfolio-company data from source documents with AI and standardizes the valuation process (in-house asset manager)
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - data-reporting
  - expert-judgment
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Fund valuations were built in bespoke spreadsheets from whatever public data was at hand; the process was manual and resource-intensive, and reporting is moving from quarterly to more frequent marks.
  solution: 'Hamilton Lane (an investment manager, not an accounting firm) says it partnered with 73 Strings to standardize valuations across private-markets strategies on one platform that uses AI to process and contextualize valuation data, and to run scenario analyses across portfolios. 73 Strings'' platform extracts financial and operational data and KPIs from documents. A Eurazeo executive is quoted on its site crediting 73 Strings with ROI across valuation, compliance, finance and investment teams. Vendor: 73 Strings.'
  outcomes:
  - lever: speed
    description: Hamilton Lane's director of valuation says the process is systematized so the firm can value everything it holds in a standardized, operationally efficient way; no time or accuracy figure is given.
    figure: none published
    measures: Qualitative statement by a Hamilton Lane director in a Q&A hosted by the vendor
    provenance: vendor-published
    source_ref: S73-HAMLANE-2025
  - lever: cost
    description: A Eurazeo executive is quoted as saying the platform delivered 'significant ROI' across operations; no figure.
    figure: none published
    measures: Testimonial on the vendor's home page; undated; no measure stated
    provenance: vendor-published
    source_ref: S73-HOME-2026
  prerequisites:
  - 'Structured data layer first: the vendor says AI is only as good as the data under it'
  - Integration with existing systems; Stout's interview asks whether added automation will integrate or become another system to access
  - Move from deal-team-led to a central valuation team, which Stout says will be easier for some organizations to implement than for others
  risks_and_guardrails:
  - 73 Strings describes a deterministic core valuation engine with traceable calculations and human judgement central to valuation decisions (S73-CALLISTO-2026)
  - Standardized models can lose nuance that a bespoke deal-team valuation captured (STOUT-TECH-2024)
  human_checkpoints:
  - Valuation team and valuation committee review marks (implied by 'human judgement central to valuation decisions')
  role_evolution: Control of the valuation process moves from deal teams to a central valuation team (STOUT-TECH-2024, an automation interview that does not discuss AI).
  evidence_grade: B
  sources:
  - ref: S73-HAMLANE-2025
    title: Hamilton Lane on Valuations and Technology (Q&A hosted by 73 Strings)
    publisher: 73 Strings
    type: vendor
    url: https://73strings.com/insights/blog/how-hamilton-lane-brings-precision-and-scale-to-valuations-and-technology/
    date: '2025-05-23'
    access: full
    locator: answers by Rivera, paragraphs 2-4
  - ref: S73-HOME-2026
    title: 73 Strings home page (undated; date = access date)
    publisher: 73 Strings
    type: vendor
    url: https://73strings.com/
    date: '2026-10-20'
    access: full
    locator: Eurazeo testimonial; 73 Extract paragraph
  - ref: S73-CALLISTO-2026
    title: 73 Strings Acquires Callisto to Expand Agentic AI Platform
    publisher: 73 Strings
    type: vendor
    url: https://73strings.com/insights/news/73-strings-acquires-callisto-accelerating-investment-into-agentic-ai-for-private-markets/
    date: '2026-09-24'
    access: full
    locator: paragraph 4 (MCP, deterministic core engine, human judgement)
  - ref: STOUT-TECH-2024
    title: Transforming Valuation Processes With Technology (interview first published Apr/May 2024, updated Sep 2024)
    publisher: Stout
    type: firm
    url: https://www.stout.com/en/insights/commentary/transforming-valuation-processes-technology
    date: 2024-09
    access: full
    locator: answers on transitioning from manual to automated processes
  last_reviewed: '2026-10-20'
  notes: 'Grade B: a named in-house deployment (Hamilton Lane) with qualitative statements and no published measurement. Not an accounting or advisory firm; it shows what portfolio-valuation work looks like when automated, and what advisory firms compete with. Independence is not an issue for an in-house team. Hamilton Lane AUM figures in the Q&A are context, not outcomes.'
- id: advisory-valuation-06
  title: Valuation advisory firm packages portfolio valuation as a monitoring platform with AI data extraction, source-linked audit support and optional independent opinions
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - data-reporting
  - expert-judgment
  - document-production
  pattern: document-to-decision
  ladder: augment
  change_scope: model
  runtime_class: workflow-automation
  maturity: announced
  problem: Alternative asset managers run fragmented, manual valuation workflows, and the valuation provider is a separate hand-off.
  solution: 'Stout (an independent valuation and advisory firm; not a top-100 accounting firm) announced Drivr on July 14, 2026: a platform for source documents, monitoring, scenario analysis, reporting and audit support, with AI-powered data extraction and Stout''s independent valuation opinions available inside the workflow.'
  outcomes:
  - lever: speed
    description: Stout's co-leader of portfolio valuation says teams can move 'hours or days, not weeks'; no measurement.
    figure: none published ('hours or days, not weeks')
    measures: Executive's stated expectation in a launch press release; no sample or baseline
    provenance: self-reported
    source_ref: STOUT-DRIVR-2026
  prerequisites:
  - Asset-manager buy-in to a combined platform plus opinion model
  - Source documents and KPI feeds from portfolio companies
  risks_and_guardrails:
  - Release stresses traceable, source-linked support for auditors
  - The release does not discuss independence, data handling or model governance
  human_checkpoints:
  - Valuation practitioners issue the independent valuation opinions (per the release)
  role_evolution: Not stated.
  evidence_grade: C
  sources:
  - ref: STOUT-DRIVR-2026
    title: Stout Launches Drivr for Portfolio Valuation and Monitoring
    publisher: Stout
    type: firm
    url: https://www.stout.com/en/news/stout-launches-drivr-portfolio-valuation-monitoring
    date: '2026-07-14'
    access: full
    locator: headline and body of the press release
  - ref: STOUT-TECH-2024
    title: Transforming Valuation Processes With Technology (interview first published Apr/May 2024, updated Sep 2024)
    publisher: Stout
    type: firm
    url: https://www.stout.com/en/insights/commentary/transforming-valuation-processes-technology
    date: 2024-09
    access: full
    locator: answers on back-office strain and technology (context; automation, not AI)
  last_reviewed: '2026-10-20'
  notes: 'Grade C: announcement, with no named customer or measurement. Client names that appeared in a search summary of a Stout product page were not seen in the firm''s own release and are not used. Stout is the business-model signal: an advisory firm selling valuation as software plus judgment.'
- id: advisory-valuation-07
  title: AI-enabled real estate portfolio valuation solution from a global advisory firm
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - data-reporting
  - expert-judgment
  - document-production
  pattern: document-to-decision
  ladder: augment
  change_scope: model
  runtime_class: workflow-automation
  maturity: announced
  problem: Perpetual-life funds, NAV vehicles and private wealth structures need more frequent, transparent, data-driven valuations of property portfolios.
  solution: 'Kroll announced REVS on March 3, 2026: an AI-enabled platform combining portfolio insights, benchmarking, workflow automation and appraisal management for U.S. commercial real estate owners and sponsors, with standardized assumptions and audit-ready documentation. Firm type: global independent advisory firm (not an accounting firm). Asset (real estate) valuation, adjacent to business valuation.'
  outcomes:
  - lever: speed
    description: Kroll says the platform lets clients reduce valuation cycle time while keeping audit-ready documentation; no figure.
    figure: none published
    measures: Capability statement in a press release
    provenance: self-reported
    source_ref: KROLL-REVS-2026
  prerequisites:
  - Property portfolio data and Kroll's market indicators
  risks_and_guardrails:
  - Release emphasizes independence, consistent methodology and audit-ready documentation; IVSC dialogue speakers said data quality is the limiting factor for AI in commercial real estate (BVR-IVSCDIALOGUE-2026)
  human_checkpoints:
  - Not described
  role_evolution: Not stated.
  evidence_grade: C
  sources:
  - ref: KROLL-REVS-2026
    title: Kroll Launches AI-enabled Real Estate Valuation Solution (REVS)
    publisher: Kroll
    type: firm
    url: https://www.kroll.com/en/newsroom/kroll-launches-ai-enabled-real-estate-valuation-solution-revs
    date: '2026-03-03'
    access: full
    locator: paragraphs 1-4
  - ref: BVR-IVSCDIALOGUE-2026
    title: 'Global: AI governance highlighted in latest IVSC Global Dialogue Series (BVWire)'
    publisher: Business Valuation Resources
    type: press
    url: https://www.bvresources.com/articles/bvwire/global-ai-governance-highlighted-in-latest-ivsc-global-dialogue-series
    date: '2026-08-05'
    access: full
    locator: paragraph 2 (data quality)
  last_reviewed: '2026-10-20'
  notes: 'Grade C: announcement only. Kroll''s statement that it valued more than $25 billion across 15,000+ properties last year is context about scale, not an outcome of REVS.'
- id: advisory-valuation-08
  title: Template-driven automated valuation report generation inside a valuation platform (accounting-firm users)
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Long business valuation reports (200 pages in one case) take weeks or months to assemble and create room for manual errors.
  solution: 'Valutico case studies (published Dec 2025) say RXM (Singapore) and PKF FI (served by the vendor''s French team) use the platform''s automated report generation. Firm type: accounting and advisory firms outside the US; size not stated. The vendor now markets its platform as AI-powered; the case studies describe ''automated'' features and do not say generative AI was used.'
  outcomes:
  - lever: speed
    description: RXM says a 200-page business valuation went from months to days, saving hundreds of hours.
    figure: months to days; 'hundreds of hours'
    measures: RXM statement in a vendor case study; no baseline, sample size or method
    provenance: vendor-published
    source_ref: VALUTICO-RXM-2025
  - lever: quality
    description: PKF FI reports saving time per valuation and 'drastically' reducing the risk of errors; no error counts.
    figure: none published
    measures: Vendor's case-study narrative; no error rate or review data
    provenance: vendor-published
    source_ref: VALUTICO-PKFFI-2025
  - lever: speed
    description: Both case studies repeat that the team is completing tasks at least 3-5 times faster, as part of 'over 90% of users' reporting significant time savings.
    figure: 3-5x; over 90%
    measures: 'Vendor boilerplate repeated in several case studies: share of Valutico users reporting significant time savings (denominator not stated) and a per-team speed-up with no stated basis'
    provenance: vendor-published
    source_ref: VALUTICO-PKFFI-2025
  prerequisites:
  - Customer success onboarding (named in each case study)
  - Financial data entered or integrated into the platform
  risks_and_guardrails:
  - Template defaults and disclosure depth are quality-control risks in report writing (the AICPA FVS 2026 workshop on report writing lists 'template defaults' among its exercises) (AICPA-FVS-2026)
  - If generative AI is added, IVSC's draft would require disclosure of significant use in scope of work and the report (IVSC-IVSED-2026)
  human_checkpoints:
  - Valuer reviews the generated report before issue (the vendor describes the report as an output the firm owns)
  role_evolution: Not stated.
  evidence_grade: B
  sources:
  - ref: VALUTICO-RXM-2025
    title: How Valutico Helped RXM Conquer 200-Page Valuations in Days, Not Months (case study)
    publisher: Valutico
    type: vendor
    url: https://valutico.com/case-studies/how-valutico-helped-rxm-conquer-200-page-valuations-in-days-not-months/
    date: '2025-12-11'
    access: full
    locator: paragraphs 1-4 and quote
  - ref: VALUTICO-PKFFI-2025
    title: How Valutico Helped PKF FI Eliminate Errors in Their Valuation Process (case study)
    publisher: Valutico
    type: vendor
    url: https://valutico.com/case-studies/how-valutico-helped-pkf-fi-eliminate-errors-in-their-valuation-process/
    date: '2025-12-10'
    access: full
    locator: paragraphs 1-4
  - ref: VALUTICO-HOME-2026
    title: 'Valutico: AI Powered Business Valuation Software (home page)'
    publisher: Valutico
    type: vendor
    url: https://www.valutico.com/
    date: '2026-06-22'
    access: full
    locator: customer-story headlines; 'Trusted by 850+' claim (vendor claim, unverified)
  - ref: AICPA-FVS-2026
    title: AICPA Forensic & Valuation Services Conference 2026 (home, agenda and pre-conference workshop pages; Nov 4-6, 2026)
    publisher: AICPA & CIMA
    type: conference
    url: https://events.aicpa-cima.com/fvs/Home
    date: 2026-11
    access: full
    locator: pre-conference workshop FVC26102 description (pre-conference workshops page)
  - ref: IVSC-IVSED-2026
    title: 'IVS Exposure Draft: Summary and Consultation Questions (consultation 31 Jan to 30 Apr 2026)'
    publisher: International Valuation Standards Council
    type: standard-setter
    url: https://ivsc.org/_ivs_effective_31_january-2028_exposure-draft-summary-and-consultation-questions-final_
    date: 2026-01
    access: full
    locator: page 2, item 3; consultation question 8
  last_reviewed: '2026-10-20'
  notes: 'Grade B (named firms, vendor-published, no measurement): the ''months to days'' statement is a recollection published by the vendor, so it is not grade A. Whether these deployments involve generative AI is not stated, so the AI link is the vendor''s branding. The 3-5x and over-90% figures are identical across case studies and are marketing boilerplate; do not cite them as measured. Dates are the case-study publication dates on the vendor''s pages.'
- id: advisory-valuation-09
  title: Data-rich comparables, multiples and discount-rate research inside a valuation platform (accounting-firm users)
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - research-synthesis
  - data-reporting
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Manual research for valuation multiples and discount rates is a significant time drain for smaller valuation teams.
  solution: 'Kreston Reeves (forensics and business valuations team) and Rouse Chartered Accountants, both served by the vendor''s British team, use Valutico''s comparable-data analysis and automated financial data integration, per vendor case studies dated Dec 2025. Firm type: accounting firms (size not stated in the sources). The studies describe data-driven research and automation; they do not say generative AI was used.'
  outcomes:
  - lever: speed
    description: 'Rouse''s quote: the team is ''reducing the time to complete projects by a third, saving up to a day at a time'', so the platform paid for itself after one or two valuations.'
    figure: one third; up to a day per project
    measures: Rouse's own estimate of project-time reduction as quoted in a vendor case study; no baseline or sample
    provenance: vendor-published
    source_ref: VALUTICO-ROUSE-2025
  - lever: speed
    description: Kreston Reeves says research into multiples and discount rates is quicker than before; the study repeats the vendor's 'at least 3-5 times faster' wording.
    figure: none specific to the firm
    measures: Qualitative statement by a senior manager; the 3-5x wording is vendor boilerplate with no stated basis
    provenance: vendor-published
    source_ref: VALUTICO-KRESTON-2025
  prerequisites:
  - Platform subscription and customer-success training
  - 'Existing valuation method knowledge: the platform feeds the analyst''s judgment'
  risks_and_guardrails:
  - IVS requires the valuer to assess and select data and inputs with professional judgement and scepticism, and to document significant data and inputs (IVSC-PERSPECTIVES-2025)
  human_checkpoints:
  - Analyst selects and justifies multiples and discount-rate inputs
  role_evolution: Not stated.
  evidence_grade: B
  sources:
  - ref: VALUTICO-KRESTON-2025
    title: How Valutico Made Valuations More Efficient for Kreston Reeves (case study)
    publisher: Valutico
    type: vendor
    url: https://valutico.com/case-studies/how-valutico-made-valuations-more-efficient-for-kreston-reeves/
    date: '2025-12-11'
    access: full
    locator: paragraphs 1-4 and quote
  - ref: VALUTICO-ROUSE-2025
    title: 'Valutico: The Platform That Paid for Itself for Rouse Chartered Accountants (case study)'
    publisher: Valutico
    type: vendor
    url: https://valutico.com/case-studies/valutico-the-platform-that-paid-for-itself-for-rouse-chartered-accountants/
    date: '2025-12-10'
    access: full
    locator: paragraphs 1-4 and quote
  - ref: IVSC-PERSPECTIVES-2025
    title: 'Navigating the Rise of Artificial Intelligence in Valuation: Opportunities, Risks, and Standards (Perspectives Paper)'
    publisher: International Valuation Standards Council
    type: standard-setter
    url: https://ivsc.org/wp-content/uploads/2025/07/Navigating-the-Rise-of-AI-in-Valuation-Opportunities-Risks-and-Standards.pdf
    date: '2025-07-23'
    access: full
    locator: page 4 (IVS 104 text) and page 12 (IVS 104 paragraphs 40.01-50.02)
  last_reviewed: '2026-10-20'
  notes: 'Grade B: named UK firms, vendor-published, with a recollection-style estimate (so not A). Same caveat as advisory-valuation-08: the AI element is the vendor''s branding, not the case study''s content.'
- id: advisory-valuation-10
  title: Generative AI drafts parts of valuation reports (market commentary and other sections)
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Report writing is time-consuming, and some narrative sections (such as market commentary) are routine.
  solution: The IVSC Perspectives Paper (July 2025) says some valuers already use ChatGPT or other public AI for parts of report writing such as market commentary, and that in other instances report writing may be a fully automated process within a firm. A BVR webinar (Nov 2025) says it demonstrates drafting valuation report sections with 'case studies from valuation firms' (summary only, paywalled). No firm is named.
  outcomes:
  - lever: speed
    description: none published
    figure: none
    measures: No measurement found
    provenance: self-reported
    source_ref: IVSC-PERSPECTIVES-2025
  prerequisites:
  - Protected AI environment for confidential data
  - Valuer control over content, materiality and sourcing
  risks_and_guardrails:
  - 'IVSC: the valuer must keep control of content and verify data sources and facts (IVSC-PERSPECTIVES-2025)'
  - IVSC flags open or closed AI used without safeguards as a risk to client confidentiality and data-protection compliance, and hallucination as a critical concern (IVSC-PERSPECTIVES-2025)
  - IVSC's draft would require significant AI use to be disclosed in the scope of work and report and documented in the engagement file (IVSC-IVSED-2026; BVR-IVSPODCAST-2026)
  human_checkpoints:
  - Signing valuer reviews and owns every section
  role_evolution: IVSC says AI can take on straightforward tasks including report writing so valuers can focus on matters needing judgement (IVSC-PERSPECTIVES-2025).
  evidence_grade: C
  sources:
  - ref: IVSC-PERSPECTIVES-2025
    title: 'Navigating the Rise of Artificial Intelligence in Valuation: Opportunities, Risks, and Standards (Perspectives Paper)'
    publisher: International Valuation Standards Council
    type: standard-setter
    url: https://ivsc.org/wp-content/uploads/2025/07/Navigating-the-Rise-of-AI-in-Valuation-Opportunities-Risks-and-Standards.pdf
    date: '2025-07-23'
    access: full
    locator: page 6 (opportunities), page 10 (IVS 106 and Transparency), pages 12-13 (confidentiality; hallucinations)
  - ref: IVSC-IVSED-2026
    title: 'IVS Exposure Draft: Summary and Consultation Questions (consultation 31 Jan to 30 Apr 2026)'
    publisher: International Valuation Standards Council
    type: standard-setter
    url: https://ivsc.org/_ivs_effective_31_january-2028_exposure-draft-summary-and-consultation-questions-final_
    date: 2026-01
    access: full
    locator: page 3, item 7-8 (documentation and reporting requirements)
  - ref: BVR-IVSPODCAST-2026
    title: AI disclosure requirements in proposed IVS highlighted in AICPA podcast (BVWire)
    publisher: Business Valuation Resources
    type: press
    url: https://www.bvresources.com/articles/bvwire/ai-disclosure-requirements-in-proposed-ivs-highlighted-in-aicpa-podcast
    date: '2026-07-29'
    access: full
    locator: paragraph 2
  - ref: BVR-TRAINWORKSNOW-2025
    title: 'AI for Business Valuation, What Works Now: Practical Workflows You Can Use Today (webinar; paywalled, summary read)'
    publisher: Business Valuation Resources
    type: conference
    url: https://www.bvresources.com/articles/training-event-transcripts/ai-for-business-valuation-what-works-now-practical-workflows-you-can-use-today
    date: '2025-11-06'
    access: search-only
    locator: summary (paywalled)
  last_reviewed: '2026-10-20'
  notes: 'Grade C: a standard-setter''s observation that this happens, without named users or measures. Maturity is ''emerging'' because the vocabulary reserves ''in-production'' for a named organization.'
- id: advisory-valuation-11
  title: 'End-to-end valuation production agent: financial documents to model, report and deck'
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - document-production
  - data-reporting
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Production work (data entry, model build, report and deck assembly) takes most of the time in a valuation engagement.
  solution: Dealgauge, a startup founded in 2026 per its profile, says it turns financial documents into client-ready valuation reports, Excel models and decks so valuation professionals can finish valuations in hours and focus on judgment. Valutico's home page advertises auto-generated financial forecasts enriched with market data and 'defensible deal valuations in minutes, not weeks'. AI-native providers (vendors). No named customers.
  outcomes:
  - lever: speed
    description: Dealgauge's profile says valuations can be completed in hours; Valutico advertises minutes, not weeks.
    figure: none published ('hours'; 'minutes, not weeks')
    measures: Vendor marketing claims; no sample, baseline or method
    provenance: vendor-published
    source_ref: DEALGAUGE-STARTUPHUB-2026
  prerequisites:
  - Source financial documents and a reviewing valuer
  risks_and_guardrails:
  - 'IVSC: valuers must avoid ''black box'' situations by keeping full control, and understand the design, limits and fitness of any model they use (IVSC-PERSPECTIVES-2025)'
  - IVSC's draft targets opaque tools whose reasoning a valuer cannot readily explain or verify (BVR-IVSPODCAST-2026)
  human_checkpoints:
  - Valuer reviews the model, assumptions and conclusion
  role_evolution: Vendor says the valuer focuses on judgment and client advisory.
  evidence_grade: C
  sources:
  - ref: DEALGAUGE-STARTUPHUB-2026
    title: Dealgauge (startup profile)
    publisher: StartupHub.ai
    type: vendor
    url: https://www.startuphub.ai/startups/dealgauge
    date: '2026-07-11'
    access: full
    locator: description paragraph (aggregator profile)
  - ref: VALUTICO-HOME-2026
    title: 'Valutico: AI Powered Business Valuation Software (home page)'
    publisher: Valutico
    type: vendor
    url: https://www.valutico.com/
    date: '2026-06-22'
    access: full
    locator: AI suite list and 'Defensible deal valuations' line
  - ref: IVSC-PERSPECTIVES-2025
    title: 'Navigating the Rise of Artificial Intelligence in Valuation: Opportunities, Risks, and Standards (Perspectives Paper)'
    publisher: International Valuation Standards Council
    type: standard-setter
    url: https://ivsc.org/wp-content/uploads/2025/07/Navigating-the-Rise-of-AI-in-Valuation-Opportunities-Risks-and-Standards.pdf
    date: '2025-07-23'
    access: full
    locator: pages 11-12 (black box)
  - ref: BVR-IVSPODCAST-2026
    title: AI disclosure requirements in proposed IVS highlighted in AICPA podcast (BVWire)
    publisher: Business Valuation Resources
    type: press
    url: https://www.bvresources.com/articles/bvwire/ai-disclosure-requirements-in-proposed-ivs-highlighted-in-aicpa-podcast
    date: '2026-07-29'
    access: full
    locator: paragraph 2
  last_reviewed: '2026-10-20'
  notes: 'Grade C: vendor claims. The Dealgauge source is a third-party startup directory profile, not the company''s own site, so treat even the capability description as unverified.'
- id: advisory-valuation-12
  title: Forecasting complete financial statements beyond one year as a projection input to DCF valuation (idea)
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: In a DCF most firm value sits beyond the first forecast year, yet few tools forecast full statements over long horizons.
  solution: 'A research team released a benchmark (ProForma-20Q) and a specialist transformer model that forecasts 78 statement line items 1-20 quarters ahead. Pattern is a trained forecasting model, not a language-model agent. Idea: researchers discuss it; no valuation firm use found.'
  outcomes:
  - lever: quality
    description: On the benchmark the specialist model beat classical machine learning, gradient boosting, a time-series foundation model and frontier large language models, with the lead widening at longer horizons.
    figure: none in the abstract
    measures: Authors' benchmark of anonymized firms scored by change-space R-squared; abstract does not give the numbers; preprint
    provenance: independent
    source_ref: ARXIV-FORMA-2026
  prerequisites:
  - Historical statements and an industry code per firm
  risks_and_guardrails:
  - Abstract says forecasts nearly satisfy accounting identities and exact coherence is recoverable at no significant accuracy cost
  - Management-projection quality is a PCAOB inspection theme (BVR-PCAOBINSP-2026)
  human_checkpoints:
  - Valuer sets scenario assumptions and judges reasonableness of projections
  role_evolution: Not stated.
  evidence_grade: D
  sources:
  - ref: ARXIV-FORMA-2026
    title: Long-Horizon Forecasting of Complete Financial Statements with Forma (preprint; abstract read)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2608.11327
    date: '2026-08-11'
    access: full
    locator: abstract
  - ref: BVR-PCAOBINSP-2026
    title: PCAOB inspections again flag problems with fair value estimates (BVWire)
    publisher: Business Valuation Resources
    type: press
    url: https://www.bvresources.com/articles/bvwire/pcaob-inspections-again-flag-problems-with-fair-value-estimates
    date: '2026-08-19'
    access: full
    locator: paragraph 2 (challenging management forecasts)
  last_reviewed: '2026-10-20'
  notes: Idea (grade D). Preprint; the full paper was not read. Relevant mainly as independent evidence that general-purpose LLMs trailed a specialist model on a forecasting task that feeds DCF work.
- id: advisory-valuation-13
  title: Language-model price estimates for property appraisal as an input or cross-check (idea; adjacent asset valuation)
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - research-synthesis
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Property price estimates normally rely on statistical models or comparable sales that need specialist set-up.
  solution: 'Researchers tested leading LLMs on international housing datasets using zero-shot, few-shot, market-report and hybrid prompts. Idea: researchers discuss it; no firm deployment found. The task is real-estate price estimation, adjacent to business and asset valuation.'
  outcomes:
  - lever: quality
    description: Traditional machine-learning models stayed stronger for pure predictive accuracy; LLMs gave meaningful estimates, benefited from similar in-context examples, and were overconfident in price intervals with limited spatial reasoning.
    figure: none in the abstract
    measures: Authors' evaluation on multiple housing datasets; abstract gives no error figures; preprint
    provenance: independent
    source_ref: ARXIV-REAPPRAISAL-2025
  prerequisites:
  - Structured property data and well-chosen in-context examples
  risks_and_guardrails:
  - Abstract warns that LLM self-explanations need cautious interpretation
  - Under Appraisal Foundation AO-41 the appraiser remains responsible for judging whether tool output is accurate and appropriate (ISA-AO41-2026)
  human_checkpoints:
  - Appraiser evaluates output credibility and owns the conclusion
  role_evolution: Not stated.
  evidence_grade: D
  sources:
  - ref: ARXIV-REAPPRAISAL-2025
    title: On the Performance of LLMs for Real Estate Appraisal (preprint; abstract read)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2506.11812
    date: '2025-06-13'
    access: full
    locator: abstract
  - ref: ISA-AO41-2026
    title: 'Artificial Intelligence and USPAP: Understanding Advisory Opinion 41'
    publisher: International Society of Appraisers
    type: professional-body
    url: https://www.isa-appraisers.org/about/blog/details/550/artificial-intelligence-and-uspap-understanding-advisory-opinion-41
    date: '2026-07-01'
    access: full
    locator: paragraphs quoting AO-41 p. 5 and the four-step framework
  last_reviewed: '2026-10-20'
  notes: Idea (grade D); adjacent to this module, so any measurement would cap at B anyway. Included because it is the only independent, quantitative-style testing of LLM valuation output found, and it points to overconfident intervals.
- id: advisory-valuation-14
  title: Anticipate and pre-empt AI-generated critiques of a valuation report (idea)
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - review-assurance
  - client-interaction
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Clients and counterparties feed reports into AI and return detailed challenges to assumptions, methods and conclusions, sometimes before the analyst is retained.
  solution: 'NACVA session speakers (Nick Mears, Nainesh Shah) advised valuers to anticipate machine review when writing reports, ask to see the client''s prompt and output, respond with evidence, and set expectations about AI in the engagement letter. Idea: the client behaviour is reported as happening; the valuer-side practice is advice, not a documented deployment.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: Conference-session report; no measurement
    provenance: self-reported
    source_ref: BVR-NACVA-2026
  prerequisites:
  - Engagement-letter language on AI
  - Willingness to review the client's AI critique
  risks_and_guardrails:
  - Prompts, drafts and AI interactions could become discoverable in some circumstances, so documentation and verification matter (BVR-DISCOVERY-2026)
  - Hold off on confidential data in public tools (BVR-AICPAREPORT-2026)
  human_checkpoints:
  - Valuer judges whether each AI-raised challenge has merit
  role_evolution: Reports are written with machine reviewers in mind.
  evidence_grade: D
  sources:
  - ref: BVR-NACVA-2026
    title: Early takeaways from the NACVA conference (BVWire)
    publisher: Business Valuation Resources
    type: conference
    url: https://www.bvresources.com/articles/bvwire/early-takeaways-from-the-nacva-conference
    date: '2026-10-07'
    access: full
    locator: paragraph 'Clients are using AI on your work'
  - ref: BVR-DISCOVERY-2026
    title: 'Beyond hallucinations: AI use moves into discovery (BVWire, BVLaw Case Update webinar)'
    publisher: Business Valuation Resources
    type: press
    url: https://www.bvresources.com/articles/bvwire/beyond-hallucinations-ai-use-moves-into-discovery
    date: '2026-07-15'
    access: full
    locator: paragraph 2
  last_reviewed: '2026-10-20'
  notes: Idea (grade D). Session report by BVWire from the NACVA 2026 conference (Salt Lake City, held around Sep 30-Oct 2, 2026 per landscape; the article is dated 2026-10-07).
- id: advisory-valuation-15
  title: Grounded research assistant over the firm's technical library, used for standards research and junior-analyst coaching
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - research-synthesis
  - client-interaction
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Reviewers answer the same technical questions repeatedly, and juniors need to learn concepts such as owner-compensation normalization and company-specific risk premium.
  solution: 'BVR''s RADA in BVResearch Pro answers plain-language questions with summaries drawn from BVR''s vetted content (case law, guides, webinars, BVU and BVWire). A BVWire tip (May 2026) suggests sending junior analysts to RADA first, then reviewing how they applied the concept. Vendor: BVR.'
  outcomes:
  - lever: capacity
    description: none published
    figure: none
    measures: Tip describes a way of working; no measure
    provenance: vendor-published
    source_ref: BVR-RADAJUNIOR-2026
  prerequisites:
  - BVResearch Pro subscription
  risks_and_guardrails:
  - 'NACVA panel warned of ''cognitive debt'': outsourcing mental effort to AI may erode skepticism and independent reasoning, and firms may need to rethink how younger professionals develop skills (BVR-COGDEBT-2026)'
  - 'Endicott: valuers need enough AI literacy to review outputs and understand how results were generated (BVR-ENDICOTT-2026)'
  human_checkpoints:
  - Senior reviews the junior's conclusions and how the concept was applied
  role_evolution: Senior time shifts from answering to reviewing application; concern that AI may remove the repetition that taught the method (BVR-COGDEBT-2026; ASA-ASAIC26-2026 abstract).
  evidence_grade: C
  sources:
  - ref: BVR-RADAJUNIOR-2026
    title: 'RADA tip of the week: Use RADA to train junior analysts (BVWire)'
    publisher: Business Valuation Resources
    type: vendor
    url: https://www.bvresources.com/articles/bvwire/rada-tip-of-the-week-use-rada-to-train-junior-analysts
    date: '2026-05-06'
    access: full
    locator: paragraphs 1-2
  - ref: BVR-RADAPRODUCT-2026
    title: BVR's Research and Data Agent (product page; undated, date = access date)
    publisher: Business Valuation Resources
    type: vendor
    url: https://www.bvresources.com/products/research-and-data-agent
    date: '2026-10-20'
    access: full
    locator: RADA in BVResearch Pro section
  - ref: BVR-COGDEBT-2026
    title: Beware of the 'cognitive debt' that can come with AI (BVWire, NACVA session report)
    publisher: Business Valuation Resources
    type: conference
    url: https://www.bvresources.com/articles/bvwire/beware-of-the-cognitive-debt-that-can-come-with-ai
    date: '2026-10-14'
    access: full
    locator: paragraphs 1-3
  - ref: ASA-ASAIC26-2026
    title: ASAIC26 Business Valuation session schedule (marked 'content subject to change'; Oct 5-6, 2026)
    publisher: American Society of Appraisers
    type: conference
    url: https://www.appraisers.org/docs/default-source/event_doc/aic/2026/asaic26_bv-session-schedule.pdf
    date: 2026-10
    access: full
    locator: '''Firm of the Future'' session abstract (Oct 6, 2026; abstract only)'
  last_reviewed: '2026-10-20'
  notes: 'Grade C: vendor guidance. The ASA session abstract is cited as a signal of discourse only (schedule marked ''content subject to change''); it does not support the grade.'
- id: advisory-valuation-16
  title: 'AI assistant inside the spreadsheet for valuation models: build, formula audit and sensitivities'
  archetype: advisory
  module: valuation
  function: service-delivery
  work_types:
  - data-reporting
  - software-systems
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Valuation models live in Excel, and building, auditing and flexing them is manual.
  solution: 'Anthropic says Claude in Excel builds financial models from filings and data feeds, audits formulas across linked workbooks and runs sensitivity analyses (May 2026). A BVR/CBV workshop (April 2025) covered Copilot in Excel as a personal Excel assistant for valuation practitioners (summary only). Endicott says AI is moving into the core tools valuers use every day. Vendors: Anthropic and Microsoft (via the workshop summary).'
  outcomes:
  - lever: quality
    description: Anthropic reports that an Excel agent built by FundamentalLabs on Claude Opus 4 scored 83% accuracy on complex Excel tasks and passed 5 of 7 levels of the Financial Modeling World Cup.
    figure: 83%; 5 of 7 levels
    measures: Vendor's account of a third party's test (tasks, scoring and sample not described in the release); general financial modelling, not valuation
    provenance: vendor-published
    source_ref: ANTHROPIC-FS-2025
  prerequisites:
  - Firm policy on which AI tools may see client financials
  risks_and_guardrails:
  - Under AO-41 the user, not the tool, is responsible for judging whether output is accurate and appropriate (ISA-AO41-2026)
  - 'Court example: a financial expert''s use of Copilot for a calculation led the court to find the testimony not credible, and the court found Copilot returned different numbers on repeat runs; a calculator or spreadsheet would have done the arithmetic (GOLDMAN-WEBER-2024)'
  human_checkpoints:
  - Analyst reviews model logic and outputs
  role_evolution: Not documented for valuation.
  evidence_grade: C
  sources:
  - ref: ANTHROPIC-FSAGENTS-2026
    title: Agents for financial services (ten agent templates, including a valuation reviewer)
    publisher: Anthropic
    type: vendor
    url: https://www.anthropic.com/news/finance-agents
    date: '2026-05-05'
    access: full
    locator: '''Claude across Excel, PowerPoint, Word, and Outlook'' section'
  - ref: ANTHROPIC-FS-2025
    title: Claude for Financial Services
    publisher: Anthropic
    type: vendor
    url: https://www.anthropic.com/news/claude-for-financial-services
    date: '2025-07-15'
    access: full
    locator: paragraph 'Claude's industry-leading financial capabilities'
  - ref: BVR-TRAINPRACTICAL-2025
    title: A Practical Introduction to Using AI (BVR and CBV workshop; paywalled, summary read)
    publisher: Business Valuation Resources
    type: conference
    url: https://www.bvresources.com/articles/training-event-transcripts/a-practical-introduction-to-using-ai-a-bvr-and-cbv-collaboration-and-workshop
    date: '2025-04-17'
    access: search-only
    locator: summary (paywalled)
  - ref: BVR-ENDICOTT-2026
    title: AI literacy becomes mandatory, says Endicott (BVWire, NACVA webcast interview)
    publisher: Business Valuation Resources
    type: podcast
    url: https://www.bvresources.com/articles/bvwire/ai-literacy-becomes-mandatory-says-endicott
    date: '2026-06-17'
    access: full
    locator: paragraph 1
  - ref: GOLDMAN-WEBER-2024
    title: Expert Witness Used Generative AI to Prepare His Report. It Didn't Go Well - In re Weber (blog post on the court decision)
    publisher: Technology & Marketing Law Blog (Eric Goldman)
    type: press
    url: https://blog.ericgoldman.org/?p=26930
    date: '2024-10-15'
    access: full
    locator: paragraphs 6-8
  - ref: ISA-AO41-2026
    title: 'Artificial Intelligence and USPAP: Understanding Advisory Opinion 41'
    publisher: International Society of Appraisers
    type: professional-body
    url: https://www.isa-appraisers.org/about/blog/details/550/artificial-intelligence-and-uspap-understanding-advisory-opinion-41
    date: '2026-07-01'
    access: full
    locator: AO-41 p. 5 quote
  last_reviewed: '2026-10-20'
  notes: 'Grade C: vendor claims. The 83% figure is a vendor-reported result for a general Excel benchmark and is not evidence of valuation quality. The Weber decision is a New York Surrogate''s Court matter about a trust-damages calculation; the decision text was not read, only a law professor''s summary.'
```

## 3. Module notes

### 3.1 Processes and key steps (with work types)

- **Engagement scoping and acceptance** (`document-production`, `coordination-scheduling`): IVS 101 scope of work, which the exposure draft would extend to include significant AI use (IVSC-IVSED-2026 page 3). Independence screening for attest clients (SEC-RULE2-01-2026).
- **Data intake and normalization** (`data-reporting`, `transaction-processing`): financials, tax returns and management data; the exposure draft adds a section on "Use of Management or Client Data" to IVS 104 (IVSC-IVSED-2026 page 3, item 4).
- **Market and comparables research** (`research-synthesis`): transactions, multiples, control premiums, DLOM studies (BVR-RADAEXPAND-2026).
- **Modelling and conclusion** (`expert-judgment`): DCF, market approach, discount-rate build-up; the draft IVS 200 adds a calibration section (IVSC-IVSED-2026 pages 4-5, IVS 200 row).
- **Fair value for financial reporting: PPA, impairment, Level 3 instruments** (`expert-judgment`): PCAOB inspections of the six largest audit firms found deficiencies in impairment testing, DCF-based business-combination valuations and Level 3 measurements (BVR-PCAOBINSP-2026).
- **Report drafting and quality control** (`document-production`, `review-assurance`): IVS 106 reporting and the new IVS 107 quality controls (IVSC-IVSED-2026 pages 3-4).
- **Defence of the work** (`review-assurance`): audit testing, tax examination, cross-examination (AICPA-FVS-2026 pre-conference workshop FVC26102 description).
- **Portfolio and fund valuation cycles** (`data-reporting`): recurring marks, monitoring, scenario analysis (S73-HAMLANE-2025; STOUT-DRIVR-2026).

### 3.2 Common pain points

- Manual research for multiples and discount rates (VALUTICO-KRESTON-2025) and very long reports, 200 pages in one case (VALUTICO-RXM-2025).
- Fragmented, spreadsheet-based portfolio valuation, with back-office teams that did not grow with fund size (STOUT-TECH-2024).
- Auditor scrutiny of assumptions, data and specialist work (BVR-PCAOBINSP-2026; PCAOB-SPECIALIST-2025 page 3, which says a specialist's work is often not entirely transparent to the auditor).
- Talent supply: a recruiter's view reported in BVR's April 2026 preview is that a late-2025 hiring dip did not remove the shortage of experienced talent, and that AI had limited impact (BVR-APRILPREVIEW-2026).
- The IVSC tracker frames pressure around reproducing a historical mark on short notice and raising valuation frequency without adding headcount; these are survey questions, not findings (IVSC-PULSE-2026).

### 3.3 Metrics and benchmarks

- **No independent error rate, override rate or parallel-run result for AI-assisted valuation was found.**
- IVSC Pulse (IVSC with 73 Strings, opened 8 May 2026) is an open sentiment survey; results had not been published when opened (IVSC-PULSE-2026).
- BVR poll summaries: 73% of valuation experts polled say AI will "significantly" change how they work, while usage was low (BVU, Sept 2025; denominator and sample not visible, paywalled) (BVR-POLLS-2025). A 2026 BVR poll is described as showing adoption moving at an "insane" pace (summary only; no figures visible) (BVR-POLL-2026).
- Vendor-published: Valutico's repeated "over 90% of users report significant time savings" and "3-5 times faster" (VALUTICO-PKFFI-2025; VALUTICO-ROUSE-2025); basis not stated. Anthropic reports 64.37% for Claude Opus 4.7 on Vals AI's Finance Agent benchmark and 83% for a third-party Excel agent (ANTHROPIC-FSAGENTS-2026; ANTHROPIC-FS-2025); both are general finance benchmarks.
- Baseline quality evidence (not about AI): PCAOB inspection reports for BDO, Deloitte, EY, Grant Thornton, KPMG and PwC flagged insufficient testing of significant assumptions, inadequate evaluation of data and too much reliance on company valuation specialists; the article gives no counts (BVR-PCAOBINSP-2026).
- A preprint presents an open-source multi-agent framework for sell-side equity research and valuation; its abstract says output is comparable to brokerage research and reports no measurements (ARXIV-FINROBOT-2024). Public-equity research, adjacent to this module, so not used for grading.
- Independent, indirect: court re-ran Copilot queries and got different numbers each time (GOLDMAN-WEBER-2024); preprint benchmark in which a specialist model beat frontier LLMs at long-horizon statement forecasting (ARXIV-FORMA-2026); preprint on LLM property price estimates (ARXIV-REAPPRAISAL-2025).

### 3.4 Guardrails and regulatory points

- **IVSC exposure draft:** would require significant use of AI or other technology-based tools to be disclosed in the scope of work and the report and documented in the engagement file, including the quality controls applied; it focuses on opaque or non-transparent tools whose reasoning the valuer cannot readily explain or verify (BVR-IVSPODCAST-2026, paragraph 2; IVSC-IVSED-2026 pages 2-3). Final text planned for 31 Jan 2027, effective 31 Jan 2028, subject to responses (IVSC-IVSED-2026 page 7). Responses to the consultation were not retrieved.
- **IVSC perspectives paper (July 2025):** under IVS in force from 31 Jan 2025, a model using AI, machine learning or deep learning cannot produce an IVS-compliant valuation without the valuer's professional judgement; it may be used as a tool if the valuer understands its design and limits; the paper notes confidentiality risks of open or closed AI without safeguards (IVSC-PERSPECTIVES-2025 pages 5, 12).
- **Appraisal Foundation AO-41:** no new USPAP requirements; clarifies competency, confidentiality, scope of work, workfile and reporting duties when appraisers use technology including AI; the appraiser remains responsible for determining whether output is accurate, relevant and appropriate (BVR-AO41ADOPT-2026; ISA-AO41-2026). The first draft addressed black-box tools, confidentiality, prompts and outputs in the workfile, and when disclosure of tool use is needed (BVR-TAFAO41-2026).
- **AICPA FVS guidelines (Oct 2025):** members-only; not official guidance or a standard; reminders on engagement terms, confidentiality agreements and professional judgment (BVR-AICPAAIGUIDE-2025).
- **Valuation Performance Framework (AICPA, ASA, RICS):** exposure draft with feedback due 22 Dec 2026; the coverage read does not mention AI (ACCTODAY-VPF-2026).
- **Auditor-facing:** PCAOB staff spotlight on using the work of specialists (Feb 2025) does not mention AI (PCAOB-SPECIALIST-2025).
- **Independence:** SEC-registrant audit clients, appraisal and valuation services barred unless results will not be subject to audit procedures (SEC-RULE2-01-2026).
- **Courts and discovery:** a New York court found an expert's testimony not credible after he used Copilot for a calculation (GOLDMAN-WEBER-2024); panellists say experts should expect questions on which AI tools they used and how outputs were verified, and that prompts and drafts could be discoverable in some circumstances (BVR-DISCOVERY-2026); a federal court in Michigan held a plaintiff's ChatGPT material was protected work product (BVR-HEPPNERCOURT-2026). Proposed Federal Rule of Evidence 707: see section 4.
- **Confidentiality:** speakers warn against putting confidential client information into public AI systems (BVR-AICPAREPORT-2026).

### 3.5 Frontier signals (dated and sourced)

- 2025-07-23: IVSC perspectives paper says some valuers already use AI in data processing and report writing, and that future IVS may be enhanced on transparency, data and inputs, models and systems, and quality control (IVSC-PERSPECTIVES-2025).
- 2026-01-07: first AO-41 exposure draft; adopted 2026-04-23 (BVR-TAFAO41-2026; BVR-AO41ADOPT-2026).
- 2026-01 to 2026-04-30: IVS exposure draft consultation; final planned 2027-01-31, effective 2028-01-31 (IVSC-IVSED-2026).
- 2026-03-03: Kroll announces an AI-enabled real estate valuation platform (KROLL-REVS-2026).
- 2026-05-05: Anthropic lists a valuation reviewer among agent templates (ANTHROPIC-FSAGENTS-2026).
- 2026-05-19: KPMG and Anthropic announce a global alliance with Claude access for 276,000+ employees (ANTHROPIC-KPMG-2026).
- 2026-06-10: BVWire reports Big Four panellists describing AI as becoming part of everyday valuation workflows and fewer entry-level analyst hires (BVR-KPMGTREND-2026).
- 2026-06 (summary only): a BVR panel write-up says firms are moving from experimentation to integrating AI into research, workflows and practice management, while facing questions on judgment, staffing, burnout and intellectual property (BVR-EXPERIMENT-2026).
- 2026-07-22 and 2026-08-25 (summaries only): BVR webinars with live demonstrations of AI use by valuation professionals, and one practitioner's account of moving from skepticism to an AI-assisted practice (BVR-TRAINLIVE-2026; BVR-TRAINFEAR-2026).
- 2026-07-14: Stout launches Drivr (STOUT-DRIVR-2026).
- 2026 (programme page): the IVSC Valuation Dialogue Series lists a session on AI in valuation covering use cases across asset classes, data aggregation, modelling and scenario analysis, and governance and model-risk considerations, and says practical implementation remains uneven (IVSC-DIALOGUE-2026). BVWire reports a 25 June panel stressing that governing the technology may now be harder than adopting it (BVR-IVSCDIALOGUE-2026).
- 2026-09-16: BVR extends its AI research agent to four more valuation datasets (BVR-RADAEXPAND-2026).
- 2026-09-24: 73 Strings acquires Callisto and says it will make its valuation platforms agent-addressable via the Model Context Protocol, with a deterministic core valuation engine and human judgement central (S73-CALLISTO-2026).
- 2026-10-04 to 06 (abstracts only): ASA International Conference sessions "AI, Ethics, and Professional Standards", "AI in Valuation: Practical Strategies, Risks, and the Road Ahead" and "Firm of the Future" (ASA-ASAIC26-2026; BVR-ASACONF-2026).
- 2026-11-04 to 06 (scheduled): AICPA FVS Conference, whose topic list includes technology and advanced data; no AI session titles were retrievable (AICPA-FVS-2026).
- 2026-12-22: Valuation Performance Framework comments due (ACCTODAY-VPF-2026).

### 3.6 Workforce and role effects

- Big Four panellists said firms are hiring fewer entry-level analysts as AI automates part of the mechanical work, raising questions on how future valuers will be trained (BVR-KPMGTREND-2026).
- An ASA session abstract (Oct 2026) says value is shifting toward interpretation, judgment and accountability, and asks how the next generation builds critical thinking once gained through hands-on repetition (abstract only) (ASA-ASAIC26-2026).
- Roger Grabowski told NACVA attendees AI is not going to replace judgment and could free analysts from mechanical work to understand businesses and advise clients (BVR-NACVA-2026).
- Greg Endicott: "AI literacy" is becoming a required skill, and the signing valuer remains responsible (BVR-ENDICOTT-2026).
- A BVR staffing webinar frames the future team as a mix of domestic, international and AI team members (summary only) (BVR-TRAINSTAFF-2025).
- Firm-level staffing and pyramid effects belong to professional-services; see section 4.

### 3.7 Objections and concerns practitioners raise

- Cognitive, technical and governance "debt": overreliance may erode the skills needed to spot AI errors, and accountability may lag the technology (BVR-COGDEBT-2026).
- Algorithmic monoculture: widespread use of common AI tools may make valuers think alike (summary only) (BVR-MONOCULTURE-2026).
- Hallucinations, with a counter-view that most are preventable through design, source checks and review, and that information overload is the bigger problem (BVR-ENDICOTT-2026).
- Confidentiality and data protection (IVSC-PERSPECTIVES-2025 page 12; BVR-AICPAREPORT-2026).
- Black-box tools and explainability (IVSC-PERSPECTIVES-2025 pages 11-13; BVR-IVSPODCAST-2026).
- Data quality as the limiting factor, especially in commercial real estate (BVR-IVSCDIALOGUE-2026).
- Clients using AI to attack valuers' assumptions (BVR-NACVA-2026).
- Discovery of prompts and AI interactions (BVR-DISCOVERY-2026).
- Cheaper, thinner valuation products enabled by automation: not found in valuation sources; the landscape file records that Forvis Mazars raises it for quality of earnings (FORVIS-QOE-2026, not re-read here; see section 4).

### 3.8 Interview probes for an advisor

1. Which valuation steps use AI today (comparables screening, data normalization, drafting, review), and what is recorded in the engagement file? How would you decide whether your use is "significant" under the IVSC draft?
2. When a tool returns comparables or data, who opens the underlying transactions, and have you tracked how often a reviewer changed the AI-assisted result?
3. As mechanical work moves to AI, how do your junior analysts learn the method, and has your hiring or training plan changed?
4. Have clients, auditors or opposing experts challenged your reports with AI, and what does your engagement letter say about AI use?
5. For clients you also audit (or whose results go into an audit), which valuation services are off the table, and has AI changed how you assess "results subject to audit procedures"?

## 4. Routed to other modules

- **forensic-disputes:** proposed Federal Rule of Evidence 707 on machine-generated evidence. The Advisory Committee's October 2026 agenda book says the committee voted at its last meeting to withdraw the proposed rule as published and submit a modified proposal for further study, and has convened a panel on unreliable AI evidence (USCOURTS-EVID-2026 page 5). Also: expert-witness AI cases (GOLDMAN-WEBER-2024; BVR-DISCOVERY-2026; BVR-HEPPNERCOURT-2026; BVR-LEDOUX-2026, a federal case about unreliable methods and AI-generated false citations, summary only).
- **transactions:** quality of earnings and diligence tooling (FORVIS-QOE-2026 and QoE vendors are in the landscape and were not re-read); data-room analysis automation (S73-CALLISTO-2026); KPMG's Claude-powered offerings for PE portfolio companies (ANTHROPIC-KPMG-2026).
- **professional-services:** staffing pyramid and entry-level hiring effects (BVR-KPMGTREND-2026; BVR-TRAINSTAFF-2025); PE ownership and consolidation of valuation and accounting firms (BVR-MOVERS-2026 lists such deals next to Stout's Drivr launch; not analyzed here); firm pricing and revenue model.
- **assurance:** auditors' evaluation of management valuations and company specialists (PCAOB-SPECIALIST-2025; BVR-PCAOBINSP-2026); the AICPA audit practice aid on AI (ACCTODAY-VPF-2026 mentions it; not read here).
- **tax:** valuations for estate, gift and 409A purposes; the IRS responsible-AI guidance for tax practice (BVWire headline only, not read).
- **risk-controls:** AI governance and model-risk controls for valuation models (BVR-IVSCDIALOGUE-2026; IVSC-PERSPECTIVES-2025 pages 12-13).
- **Demand side, noted here:** valuing generative-AI businesses is a distinct new valuation topic, with scarce comparables and unreliable projections pushing practitioners toward DCF and multiples with adjustments (BRATTLE-INSOL-2025, sections 3.2 and 4). This is a service-demand signal, not an AI use in the work, so it has no use-case entry.

## 5. Sources

67 distinct sources: 53 opened and read in full or in the relevant part, and 14 marked `search-only` (BVR paywalled pages where only the publisher's summary was read). By type: 19 press; 15 vendor; 13 conference; 4 academic; 4 firm; 3 standard-setter; 3 survey; 3 regulator; 2 podcast; 1 professional-body. No `community` or `job-posting` sources were reached (see section 6). The search-only items support no A or B grade.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| IVSC-IVSED-2026 | IVS Exposure Draft: Summary and Consultation Questions (consultation 31 Jan to 30 Apr 2026) | International Valuation Standards Council | standard-setter | https://ivsc.org/_ivs_effective_31_january-2028_exposure-draft-summary-and-consultation-questions-final_ | 2026-01 | full |
| IVSC-PERSPECTIVES-2025 | Navigating the Rise of Artificial Intelligence in Valuation: Opportunities, Risks, and Standards (Perspectives Paper) | International Valuation Standards Council | standard-setter | https://ivsc.org/wp-content/uploads/2025/07/Navigating-the-Rise-of-AI-in-Valuation-Opportunities-Risks-and-Standards.pdf | 2025-07-23 | full |
| IVSC-PULSE-2026 | The Valuation Pulse: AI & Technology in Valuation Sentiment Tracker | IVSC with 73 Strings | survey | https://ivsc.org/the-valuation-pulse-ai-technology-in-valuation-sentiment-tracker/ | 2026-05-08 | full |
| IVSC-DIALOGUE-2026 | IVSC Valuation Dialogue Series 2026, sponsored by PwC (programme page) | International Valuation Standards Council | standard-setter | https://ivsc.org/ivsc-valuation-dialogue-series-2026-sponsored-by-pwc/ | 2026-03-26 | full |
| BVR-IVSCDIALOGUE-2026 | Global: AI governance highlighted in latest IVSC Global Dialogue Series (BVWire) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/global-ai-governance-highlighted-in-latest-ivsc-global-dialogue-series | 2026-08-05 | full |
| BVR-AICPAREPORT-2026 | AI agents as a quality-control layer for valuation reports (BVWire, on an AICPA FVS podcast) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/ai-agents-as-a-quality-control-layer-for-valuation-reports | 2026-09-16 | full |
| AICPA-FVSPODCAST-2026 | Building More Defensible Valuation Reports (The FVS Valuation Podcast episode page) | AICPA & CIMA | podcast | https://podcasts.apple.com/us/podcast/building-more-defensible-valuation-reports/id1551184348?i=1000787680655 | 2026-09-03 | full |
| BVR-IVSPODCAST-2026 | AI disclosure requirements in proposed IVS highlighted in AICPA podcast (BVWire) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/ai-disclosure-requirements-in-proposed-ivs-highlighted-in-aicpa-podcast | 2026-07-29 | full |
| BVR-AICPAAIGUIDE-2025 | AICPA issues AI usage guidelines for valuation and forensic work (BVWire) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/aicpa-issues-ai-usage-guidelines-for-valuation-and-forensic-work | 2025-10-15 | full |
| BVR-NACVA-2026 | Early takeaways from the NACVA conference (BVWire) | Business Valuation Resources | conference | https://www.bvresources.com/articles/bvwire/early-takeaways-from-the-nacva-conference | 2026-10-07 | full |
| BVR-COGDEBT-2026 | Beware of the 'cognitive debt' that can come with AI (BVWire, NACVA session report) | Business Valuation Resources | conference | https://www.bvresources.com/articles/bvwire/beware-of-the-cognitive-debt-that-can-come-with-ai | 2026-10-14 | full |
| BVR-RADAEXPAND-2026 | AI-powered RADA expands to more BVR resources (BVWire) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/ai-powered-rada-expands-to-more-bvr-resources | 2026-09-16 | full |
| BVR-RADATIP-2026 | RADA tip of the week: Check the transactions behind the answer (BVWire) | Business Valuation Resources | vendor | https://www.bvresources.com/articles/bvwire/rada-tip-of-the-week-check-the-transactions-behind-the-answer | 2026-09-23 | full |
| BVR-RADAJUNIOR-2026 | RADA tip of the week: Use RADA to train junior analysts (BVWire) | Business Valuation Resources | vendor | https://www.bvresources.com/articles/bvwire/rada-tip-of-the-week-use-rada-to-train-junior-analysts | 2026-05-06 | full |
| BVR-RADAPRODUCT-2026 | BVR's Research and Data Agent (product page; undated, date = access date) | Business Valuation Resources | vendor | https://www.bvresources.com/products/research-and-data-agent | 2026-10-20 | full |
| BVR-KPMGTREND-2026 | KPMG's AI push reflects a broader trend in valuation (BVWire, ASA Fair Value Conference panel) | Business Valuation Resources | conference | https://www.bvresources.com/articles/bvwire/kpmgs-ai-push-reflects-a-broader-trend-in-valuation | 2026-06-10 | full |
| BVR-ENDICOTT-2026 | AI literacy becomes mandatory, says Endicott (BVWire, NACVA webcast interview) | Business Valuation Resources | podcast | https://www.bvresources.com/articles/bvwire/ai-literacy-becomes-mandatory-says-endicott | 2026-06-17 | full |
| BVR-EWART-2026 | AI raises the bar for valuation standards compliance (BVWire, on a BVResearch Pro Expert Insights article by James Ewart) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/ai-raises-the-bar-for-valuation-standards-compliance | 2026-04-01 | full |
| BVR-AO41ADOPT-2026 | ASB adopts AO-41 on the use of technology in appraisal (BVWire) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/asb-adopts-ao-41-on-the-use-of-technology-in-appraisal | 2026-04-29 | full |
| BVR-TAFAO41-2026 | TAF proposes new USPAP guidance on technology use (BVWire, first exposure draft of AO-41) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/taf-proposes-new-uspap-guidance-on-technology-use | 2026-01-07 | full |
| ISA-AO41-2026 | Artificial Intelligence and USPAP: Understanding Advisory Opinion 41 | International Society of Appraisers | professional-body | https://www.isa-appraisers.org/about/blog/details/550/artificial-intelligence-and-uspap-understanding-advisory-opinion-41 | 2026-07-01 | full |
| BVR-DISCOVERY-2026 | Beyond hallucinations: AI use moves into discovery (BVWire, BVLaw Case Update webinar) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/beyond-hallucinations-ai-use-moves-into-discovery | 2026-07-15 | full |
| BVR-HEPPNERCOURT-2026 | Court: ChatGPT use does not waive work-product protection (BVWire) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/court-chatgpt-use-does-not-waive-work-product-protection | 2026-05-20 | full |
| BVR-ASACONF-2026 | ASA conference spans traditional and emerging valuation issues (BVWire, ASAIC26 programme preview) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/asa-conference-spans-traditional-and-emerging-valuation-issues | 2026-08-19 | full |
| ASA-ASAIC26-2026 | ASAIC26 Business Valuation session schedule (marked 'content subject to change'; Oct 5-6, 2026) | American Society of Appraisers | conference | https://www.appraisers.org/docs/default-source/event_doc/aic/2026/asaic26_bv-session-schedule.pdf | 2026-10 | full |
| AICPA-FVS-2026 | AICPA Forensic & Valuation Services Conference 2026 (home, agenda and pre-conference workshop pages; Nov 4-6, 2026) | AICPA & CIMA | conference | https://events.aicpa-cima.com/fvs/Home | 2026-11 | full |
| ACCTODAY-VPF-2026 | AICPA proposes valuation framework (Valuation Performance Framework exposure draft) | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-proposes-valuation-framework | 2026-10-13 | full |
| BVR-PCAOBINSP-2026 | PCAOB inspections again flag problems with fair value estimates (BVWire) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/pcaob-inspections-again-flag-problems-with-fair-value-estimates | 2026-08-19 | full |
| PCAOB-SPECIALIST-2025 | Spotlight: Considerations for Audit Firms Using the Work of Specialists | PCAOB staff | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/use-of-specialist-spotlight.pdf | 2025-02 | full |
| SEC-RULE2-01-2026 | 17 CFR 210.2-01 Qualifications of accountants (current text, Cornell LII) | SEC (Regulation S-X) | regulator | https://www.law.cornell.edu/cfr/text/17/210.2-01 | 2026-10-20 | full |
| USCOURTS-EVID-2026 | Advisory Committee on Evidence Rules agenda book, October 15, 2026 meeting | US federal judiciary | regulator | https://www.uscourts.gov/sites/default/files/document/2026-10_evidence_rules_agenda_book_9-23_final.pdf | 2026-10 | full |
| GOLDMAN-WEBER-2024 | Expert Witness Used Generative AI to Prepare His Report. It Didn't Go Well - In re Weber (blog post on the court decision) | Technology & Marketing Law Blog (Eric Goldman) | press | https://blog.ericgoldman.org/?p=26930 | 2024-10-15 | full |
| BVR-LEDOUX-2026 | LeDoux v. Outliers, Inc. (BVLaw case page; paywalled, summary read) | Business Valuation Resources | press | https://www.bvresources.com/articles/full-text-of-court-cases/ledoux-v-outliers-inc | 2026-08-18 | search-only |
| ARXIV-FORMA-2026 | Long-Horizon Forecasting of Complete Financial Statements with Forma (preprint; abstract read) | arXiv | academic | https://arxiv.org/abs/2608.11327 | 2026-08-11 | full |
| ARXIV-REAPPRAISAL-2025 | On the Performance of LLMs for Real Estate Appraisal (preprint; abstract read) | arXiv | academic | https://arxiv.org/abs/2506.11812 | 2025-06-13 | full |
| ARXIV-FINROBOT-2024 | FinRobot: AI Agent for Equity Research and Valuation with Large Language Models (preprint; abstract read) | arXiv | academic | https://arxiv.org/abs/2411.08804 | 2024-11-13 | full |
| BRATTLE-INSOL-2025 | A Primer on Generative AI and Valuation Considerations for Insolvency Professionals (INSOL Technical Paper Series No 71) | INSOL International with The Brattle Group | academic | https://www.brattle.com/wp-content/uploads/2025/07/A-Primer-on-Generative-AI-and-Valuation-Considerations-for-Insolvency-Professionals.pdf | 2025-06 | full |
| ANTHROPIC-KPMG-2026 | KPMG integrates Claude across its core business and workforce of more than 276,000 in strategic alliance | Anthropic | vendor | https://anthropic.com/news/anthropic-kpmg | 2026-05-19 | full |
| ANTHROPIC-FSAGENTS-2026 | Agents for financial services (ten agent templates, including a valuation reviewer) | Anthropic | vendor | https://www.anthropic.com/news/finance-agents | 2026-05-05 | full |
| ANTHROPIC-FS-2025 | Claude for Financial Services | Anthropic | vendor | https://www.anthropic.com/news/claude-for-financial-services | 2025-07-15 | full |
| KROLL-REVS-2026 | Kroll Launches AI-enabled Real Estate Valuation Solution (REVS) | Kroll | firm | https://www.kroll.com/en/newsroom/kroll-launches-ai-enabled-real-estate-valuation-solution-revs | 2026-03-03 | full |
| STOUT-DRIVR-2026 | Stout Launches Drivr for Portfolio Valuation and Monitoring | Stout | firm | https://www.stout.com/en/news/stout-launches-drivr-portfolio-valuation-monitoring | 2026-07-14 | full |
| STOUT-TECH-2024 | Transforming Valuation Processes With Technology (interview first published Apr/May 2024, updated Sep 2024) | Stout | firm | https://www.stout.com/en/insights/commentary/transforming-valuation-processes-technology | 2024-09 | full |
| S73-CALLISTO-2026 | 73 Strings Acquires Callisto to Expand Agentic AI Platform | 73 Strings | vendor | https://73strings.com/insights/news/73-strings-acquires-callisto-accelerating-investment-into-agentic-ai-for-private-markets/ | 2026-09-24 | full |
| S73-HAMLANE-2025 | Hamilton Lane on Valuations and Technology (Q&A hosted by 73 Strings) | 73 Strings | vendor | https://73strings.com/insights/blog/how-hamilton-lane-brings-precision-and-scale-to-valuations-and-technology/ | 2025-05-23 | full |
| S73-HOME-2026 | 73 Strings home page (undated; date = access date) | 73 Strings | vendor | https://73strings.com/ | 2026-10-20 | full |
| VALUTICO-HOME-2026 | Valutico: AI Powered Business Valuation Software (home page) | Valutico | vendor | https://www.valutico.com/ | 2026-06-22 | full |
| VALUTICO-KRESTON-2025 | How Valutico Made Valuations More Efficient for Kreston Reeves (case study) | Valutico | vendor | https://valutico.com/case-studies/how-valutico-made-valuations-more-efficient-for-kreston-reeves/ | 2025-12-11 | full |
| VALUTICO-ROUSE-2025 | Valutico: The Platform That Paid for Itself for Rouse Chartered Accountants (case study) | Valutico | vendor | https://valutico.com/case-studies/valutico-the-platform-that-paid-for-itself-for-rouse-chartered-accountants/ | 2025-12-10 | full |
| VALUTICO-RXM-2025 | How Valutico Helped RXM Conquer 200-Page Valuations in Days, Not Months (case study) | Valutico | vendor | https://valutico.com/case-studies/how-valutico-helped-rxm-conquer-200-page-valuations-in-days-not-months/ | 2025-12-11 | full |
| VALUTICO-PKFFI-2025 | How Valutico Helped PKF FI Eliminate Errors in Their Valuation Process (case study) | Valutico | vendor | https://valutico.com/case-studies/how-valutico-helped-pkf-fi-eliminate-errors-in-their-valuation-process/ | 2025-12-10 | full |
| DEALGAUGE-STARTUPHUB-2026 | Dealgauge (startup profile) | StartupHub.ai | vendor | https://www.startuphub.ai/startups/dealgauge | 2026-07-11 | full |
| BVR-TRAINPRACTICAL-2025 | A Practical Introduction to Using AI (BVR and CBV workshop; paywalled, summary read) | Business Valuation Resources | conference | https://www.bvresources.com/articles/training-event-transcripts/a-practical-introduction-to-using-ai-a-bvr-and-cbv-collaboration-and-workshop | 2025-04-17 | search-only |
| BVR-TRAINWORKSNOW-2025 | AI for Business Valuation, What Works Now: Practical Workflows You Can Use Today (webinar; paywalled, summary read) | Business Valuation Resources | conference | https://www.bvresources.com/articles/training-event-transcripts/ai-for-business-valuation-what-works-now-practical-workflows-you-can-use-today | 2025-11-06 | search-only |
| BVR-TRAINLIVE-2026 | AI Applications in Business Valuation: Live Use Cases (webinar; paywalled, summary read) | Business Valuation Resources | conference | https://www.bvresources.com/articles/training-event-transcripts/ai-applications-in-business-valuation-live-use-cases | 2026-07-22 | search-only |
| BVR-TRAINFEAR-2026 | From Fear to Fluency: How I Built an AI-Powered Valuation Practice (Raymond Medrano; paywalled, summary read) | Business Valuation Resources | conference | https://www.bvresources.com/articles/training-event-transcripts/from-fear-to-fluency-how-i-built-an-ai-powered-valuation-practice | 2026-08-25 | search-only |
| BVR-TRAINSTAFF-2025 | Staffing the BVFLS Firm of the Future (webinar; paywalled, summary read) | Business Valuation Resources | conference | https://www.bvresources.com/articles/training-event-transcripts/staffing-the-bvfls-firm-of-the-future | 2025-10-16 | search-only |
| BVR-POLLS-2025 | Recent Polls Reveal AI Usage at BVFLS Firms (Business Valuation Update; paywalled, summary read) | Business Valuation Resources | survey | https://www.bvresources.com/articles/business-valuation-update/recent-polls-reveal-ai-usage-at-bvfls-firms | 2025-09 | search-only |
| BVR-POLL-2026 | BVR Poll: AI Adoption in Valuation Is Moving at an 'Insane' Pace (Business Valuation Update; paywalled, summary read) | Business Valuation Resources | survey | https://www.bvresources.com/articles/business-valuation-update/bvr-poll-ai-adoption-in-valuation-is-moving-at-an-insane-pace | 2026-04 | search-only |
| BVR-BIG4PANEL-2026 | Big Four Valuation Leaders Discuss AI, Tariffs, Pain Points, and More (Business Valuation Update; paywalled, summary read) | Business Valuation Resources | conference | https://www.bvresources.com/articles/business-valuation-update/big-four-valuation-leaders-discuss-ai-tariffs-pain-points-and-more | 2026-06 | search-only |
| BVR-BIG4GUIDANCE-2026 | Big Four Valuation Leaders Point to the Need for Fair Value Guidance (Business Valuation Update; paywalled, summary read) | Business Valuation Resources | conference | https://www.bvresources.com/articles/business-valuation-update/big-four-valuation-leaders-point-to-the-need-for-fair-value-guidance | 2026-07 | search-only |
| BVR-EXPERIMENT-2026 | From Experimentation to Integration: AI's Next Phase in Valuation (Business Valuation Update; paywalled, summary read) | Business Valuation Resources | conference | https://www.bvresources.com/articles/business-valuation-update/from-experimentation-to-integration-ais-next-phase-in-valuation | 2026-06 | search-only |
| BVR-MONOCULTURE-2026 | Are We Headed for an 'Algorithmic Monoculture'? (Business Valuation Update; paywalled, summary read) | Business Valuation Resources | press | https://www.bvresources.com/articles/business-valuation-update/are-we-headed-for-an-algorithmic-monoculture | 2026-08 | search-only |
| BVR-APRILPREVIEW-2026 | Preview of the April issue of Business Valuation Update (BVWire; item on BV hiring and AI) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/preview-of-the-april-issue-of-business-valuation-update-031826 | 2026-03-18 | full |
| BVR-MOVERS-2026 | BV Movers (BVWire people and firm news; item on Stout's Drivr launch; date taken from the URL) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/bv-movers-072226 | 2026-07-22 | full |
| FORVIS-QOE-2026 | Quality of Earnings & Due Diligence in an AI World (not opened in this run; described in landscape-advisory.md) | Forvis Mazars US | firm | https://www.forvismazars.us/forsights/2026/09/quality-of-earnings-due-diligence-in-an-ai-world | 2026-09-08 | search-only |
| BVR-MERCER-2025 | Mercer's Take on AI in Business Valuation (Business Valuation Update; paywalled, summary read) | Business Valuation Resources | press | https://www.bvresources.com/articles/business-valuation-update/mercers-take-on-ai-in-business-valuation | 2025-04 | search-only |

## 6. Gaps

**Not found or not reachable**
- **Independent quality evidence for AI-assisted valuation:** no error rates, override rates, parallel-run results, inspection findings about AI use, or independent measurement. Only indirect items (section 3.3).
- **Named deployments at accounting firms:** no US top-100 or mid-market accounting firm, and none of the other Big Four firms (Deloitte, EY, PwC), published specifics on valuation AI in the sources reached. KPMG's statement is second-hand via trade press.
- **PPA, goodwill impairment and fairness opinions:** no AI deployment evidence found.
- **Valuation boutiques:** Houlihan Lokey's technology page returned an empty response; no AI statements found from Duff-style, Chaffe, Empire, Willamette, Mercer Capital or Valuation Research Corp beyond a paywalled Mercer item (BVR-MERCER-2025, summary only). Stout and Kroll announcements were read.
- **Practitioner community discussion** (forums, LinkedIn, Reddit, search-fund communities) and **job postings** that show real AI use: not reached.
- **Paywalled BVR content:** BVU polls, Big Four panel write-ups, "From Experimentation to Integration", "Algorithmic Monoculture", training-event transcripts and the BVR Leadership Council AI perspective paper (free download link not located). Only summaries were read.
- **Members-only or unavailable:** AICPA FVS AI guidelines (Oct 2025); AICPA FVS Conference 2026 session titles (the agenda page returned no session list); the AO-41 full text (read through the ISA summary and BVWire); IVSC consultation responses; IVSC Pulse results (not yet published when opened).
- **Blocked or failed fetches:** SSRN (403) so the Kim-Muhn-Nikolaev and similar finance papers were not read; the arXiv API did not resolve; arXiv items were read at abstract level only; the Weber decision text and Kohls v. Ellison were not read directly; the RICS responsible-AI standard URL could not be confirmed.
- **Search budget:** the shared web-search budget ran out after about fifteen searches, before job-posting and some firm-specific searches could be run.
- **Date uncertainty:** NACVA 2026 conference dates (the BVWire report is dated 2026-10-07; start and end dates vary across sources); ASA International Conference sessions are abstracts from a schedule marked "content subject to change"; the Grabowski BVU article appears on a BVR listing dated November 2026 and was not used.
- **Valutico case studies:** the AI content of each deployment is not stated; the vendor's product is now branded as AI-powered. Whether generative AI sits behind the described time savings is unknown.

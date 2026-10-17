# Module deep dive: tax / transfer-pricing / discourse

- **Archetype:** tax
- **Module:** transfer-pricing. Transfer pricing policy, benchmarking and comparables searches, intercompany agreements, local and master files, country-by-country reporting, intragroup services, operational transfer pricing, APAs and transfer pricing disputes.
- **Angle:** discourse. What practitioners have said in the last 12-18 months at conferences, on podcasts and webinars, and in practitioner articles; where the field says it is heading and what worries it.
- **Prepared:** 2026-10-17
- **Method note:** The wave-2 tax landscape file and the vocabulary were read first. About 35 pages and PDFs were then opened and read with `curl` and `pdftotext` (including the ABA May 2026 programme PDF, the CIAT working paper, three TPMinds agendas, the Aibidia survey write-ups and the KPMG podcast pages). Three bot-walled or removed pages (ABA Tax Times, BDO Canada, KPMG Germany) are known only from search extracts and are marked `search-only`; they appear in the module notes only, never in a graded use case. The shared web-search budget ran out part-way through, so APA/MAP-specific and product-launch searches were not run. Provenance: nearly all published figures in this angle come from Aibidia (a TP software vendor), Exactera (a TP software vendor, sponsored content), or firm speakers at conferences. No independent measurement of quality was found.

---

## 1. Summary

1. **The conversation is conference-led and mostly vendor-hosted.** The densest public record is the TPMinds series (International, London, 16-17 June 2026; West Coast, Palo Alto, 4-5 November 2026; Americas, with an AI Transformation Day planned for 1 March 2027), the ABA Tax Section's 8 May 2026 panel on AI and section 482, and the WU-TA programme in Singapore (28 September-1 October 2026). The recaps are written by sponsors (Aibidia) or reporters (DDTC, Thomson Reuters Checkpoint), so session content is thinly reported.
2. **Where practitioners say AI helps today:** first-pass comparable searches, narrative drafting for local and master files, first drafts of intercompany agreements, research on local requirements, and in-year margin monitoring. Where they say it does not: method selection, functional characterisation, and anything that needs an auditable number. Their repeated line is that AI speeds the first pass and a named professional signs off (AIBIDIA-WEBINAR-2026, DDTC-WUTA-2026, PLANTEMORAN-2026, AIBIDIA-TPMINDS-2026).
3. **Quality evidence is missing.** No error rate, override rate, parallel run, or inspection finding for AI in TP was found. The only figures are speaker claims (PwC Singapore: up to 100 hours to about 30 minutes for an unspecified analysis; AI may do about 80% of comparability work) and vendor survey data. This is why 12 of 13 use cases are graded C or D and none is A.
4. **Authorities set the guardrail, not the rulebook.** An IRS LB&I director said on 29 July 2026 that AI can support but should not replace judgment, and that the IRS expects experts to explain inputs, assumptions, methods and AI tools and wants to test formulas (IRS-LBI-TP-2026). PwC's TP principal said the same on 30 July 2026 (TR-CHECKPOINT-2026). HMRC consulted in April 2025 on a transaction schedule meant to enable automated risk assessment (KPMG-UK-ICTS-2025).
5. **Data readiness, not model access, is the bottleneck.** In Aibidia's 2026 survey, 93% of respondents use AI in some form but only 22% believe their TP data is clean enough for AI to use without manual intervention; 79% spend more than 10% of team time on data preparation (AIBIDIA-STATETP-2026; vendor-published, 97 respondents).
6. **TP of AI itself is a large share of the discourse** (AI-generated assets, shared AI tools between affiliates, DEMPE in AI value chains; OECD Chapter VII consultation of 1 June 2026). That is advice about AI as a subject, not AI as a tool, and is routed to another module.

---

## 2. Use cases

```yaml
- id: tax-transfer-pricing-01
  title: AI-assisted comparable-company search and screening for benchmarking
  work_types:
  - research-synthesis
  - data-reporting
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: The search for comparable data is one of the key stages in applying the arm's length principle. Practitioners have had to examine databases or company websites one by one (DDTC-WUTA-2026). A Plante Moran article describes the early work as sorting through thousands of companies' data (PLANTEMORAN-2026).
  solution: 'The practitioner gives the model detailed screening instructions (one example given: companies that hold no intangibles such as brands or IP). The model gathers information from many databases and websites at once and returns a candidate list. Practitioners then run the recognised databases, a documented screening process and their own comparability judgment (DDTC-WUTA-2026, PLANTEMORAN-2026). The same step is the subject of a scheduled ABA panel and a TPMinds session, and of a vendor feature that searches by functional profile (ABA-MAYMTG-2026, TPMINDS-INTL-2026, EXACTERA-2025). On the tax-administration side, a CIAT working paper gives the author''s own example of a custom ChatGPT model reading a listed company''s 10-K for comparability analysis, with no measured result (CIAT-WP06-2025).'
  outcomes:
  - lever: speed
    description: A PwC Singapore senior manager said analysis that once took up to 100 hours of manual work can, under certain conditions, be done in about 30 minutes
    figure: up to 100 hours -> about 30 minutes
    measures: hours of manual work for 'analysis' at stages from modelling to value-chain work, as reported by DDTC from a conference talk; the conditions, sample and method are not stated, and the figure is not specific to comparables searches (adjacent, so the grade is capped at B)
    provenance: self-reported
    source_ref: DDTC-WUTA-2026
  - lever: capacity
    description: A PwC Singapore TP partner said AI may complete approximately 80% of the work in comparability analysis that has historically consumed practitioners' time
    figure: approximately 80% (stated as 'may')
    measures: share of the work involved in comparability analysis, as an opinion expressed at a conference; not a measurement
    provenance: self-reported
    source_ref: DDTC-WUTA-2026
  prerequisites:
  - 'Good data: the PwC partner''s rule is that AI is good if the data is good (DDTC-WUTA-2026)'
  - Access to recognised benchmarking databases and a documented screening process (PLANTEMORAN-2026)
  - A secure or closed AI environment for confidential company data (DDTC-WUTA-2026)
  risks_and_guardrails:
  - The remaining judgment (about 20% in the PwC partner's estimate) stays with people because current AI is not fully perfect (DDTC-WUTA-2026)
  - An AI-generated first list on its own is unlikely to meet tax authority standards (PLANTEMORAN-2026)
  - Entering sensitive company data into AI systems raises privacy and confidentiality risk (DDTC-WUTA-2026)
  - An IRS LB&I official said AI can support but should not replace judgment, and the IRS wants to see the formulas (IRS-LBI-TP-2026); a PwC TP principal said the IRS expects to see the underlying work (TR-CHECKPOINT-2026)
  human_checkpoints:
  - Practitioner selects and refines the comparables and applies the documented screening (PLANTEMORAN-2026, AIBIDIA-WEBINAR-2026)
  - Practitioner reviews the data inputs given to the model (PLANTEMORAN-2026)
  role_evolution: A P&G head of tax likened AI to a junior associate that can prepare initial draft analyses but needs supervision, risk assessment and quality clean-up (DDTC-WUTA-2026). A webinar speaker framed it as AI strong on data and the professional strong on judgment (AIBIDIA-WEBINAR-2026).
  evidence_grade: B
  sources:
  - ref: DDTC-WUTA-2026
    title: Challenges in Transfer Pricing Benchmarking Changes in the AI Era (DDTC report from the WU-TA Advanced Transfer Pricing Programme 2026, Singapore, 28 Sep-1 Oct 2026)
    publisher: DDTCNews (Audreyda Farahbella Anandivi)
    type: press
    url: https://news.ddtc.co.id/en/insight/1822922/challenges-in-transfer-pricing-benchmarking-changes-in-the-ai-era
    date: '2026-10-01'
    access: full
    locator: paragraphs on Falgun Thakkar (80%; AI is good if the data is good), Jimit Parikh (100 hours to 30 minutes; comparables that hold no intangibles), and the fireside chat
  - ref: PLANTEMORAN-2026
    title: 'Using AI in transfer pricing: Practical opportunities and pitfalls for growing companies'
    publisher: Plante Moran (Lara Witte, Biz Pavelich, Kevin Lee)
    type: firm
    url: https://plantemoran.com/explore-our-thinking/insight/2026/08/using-ai-in-transfer-pricing
    date: '2026-08-05'
    access: full
    locator: section 'Aspects of transfer pricing documentation well-suited to AI', item 'Jump-starting comparables searches'; section 'Understanding AI's limits'
  - ref: AIBIDIA-WEBINAR-2026
    title: 'AI in Transfer Pricing: What''s Working, What''s Not, and What''s Next (summary of the webinar ''From Hype to Help: Where AI Is Working in Transfer Pricing'')'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/ai-in-transfer-pricing-whats-working-whats-not-and-whats-next
    date: 2026-06
    access: full
    locator: section 'What AI Is Actually Good At (Right Now)', paragraph 'Comparable searches and benchmarking'
  - ref: EXACTERA-2025
    title: AI is transforming transfer pricing (sponsored advertising supplement, Q&A with Exactera COO Mimi Song)
    publisher: Exactera in The Tax Adviser (AICPA)
    type: vendor
    url: https://www.thetaxadviser.com/issues/2025/sep/ai-is-transforming-transfer-pricing/
    date: '2025-08-31'
    access: full
    locator: answer to question 2 (ExactMatch ranks companies by comparability using functional profiles)
  - ref: CIAT-WP06-2025
    title: Study on Artificial Intelligence Applied to Transfer Pricing (Jairo A. Godoy G., Working Paper WP-06-2025)
    publisher: CIAT (Inter-American Center of Tax Administrations)
    type: regulator
    url: https://www.ciat.org/Biblioteca/DocumentosdeTrabajo/2026/WP-06-2025.pdf
    date: 2025-08
    access: full
    locator: section 5.2 (p.26) pilot description; section 6.1 (p.32) conclusions
  - ref: ABA-MAYMTG-2026
    title: 'ABA Section of Taxation May Tax Meeting 2026, final program (Transfer Pricing session ''AI and Transfer Pricing Under §482: Transforming Compliance and Risk Management'')'
    publisher: ABA Section of Taxation
    type: conference
    url: https://sitepilot11.firmseek.com/client/chamberlain/www/media/event/657_ABA_Section_of_Taxation_2026_May_Meeting_Agenda.pdf
    date: '2026-05-08'
    access: full
    locator: Transfer Pricing programme, Friday 4:15 PM (p.34 of the final program)
  - ref: TPMINDS-INTL-2026
    title: TPMinds International 2026, Main Summit Day 1 agenda (16 June 2026, London)
    publisher: Informa Connect
    type: conference
    url: https://informaconnect.com/tp-minds-international-conference/agenda/
    date: '2026-06-16'
    access: full
    locator: Day 1, 15:45-16:30 session 'Latest Thinking & Case Studies in the Use of AI in Benchmarking, Documentation, and Risk Assessment'
  - ref: IRS-LBI-TP-2026
    title: Report on recent US international tax developments, 31 July 2026 (reports IRS LB&I remarks on AI in transfer pricing, 29 July 2026)
    publisher: Ernst & Young LLP (EY Tax News & Developments)
    type: firm
    url: https://taxnews.ey.com/news/2026-1658-report-on-recent-us-international-tax-developments-31-july-2026
    date: '2026-07-31'
    access: full
    locator: paragraphs 3-4 of the TP item (IRS LB&I remarks, 29 July 2026)
  - ref: TR-CHECKPOINT-2026
    title: AI-powered IRS audits are here but taxpayers have new relief options, tax pros say (report on a 30 July 2026 PwC webcast)
    publisher: Thomson Reuters Checkpoint News (Tim Shaw)
    type: press
    url: https://tax.thomsonreuters.com/news/ai-powered-irs-audits-are-here-but-taxpayers-have-new-relief-options-tax-pros-say/
    date: '2026-08-05'
    access: full
    locator: paragraph quoting Kristina Novak, PwC Transfer Pricing Services
  - ref: BTAX-KPMGQA-2024
    title: 'Q&A: How KPMG Is Using AI to Find Transfer Pricing Comparables (opening paragraphs only; paywalled after)'
    publisher: Bloomberg Tax
    type: press
    url: https://news.bloombergtax.com/payroll/q-a-how-kpmg-is-using-ai-to-find-transfer-pricing-comparables
    date: '2024-02-28'
    access: full
    locator: 'opening paragraphs: KPMG recently awarded a patent for an AI system that helps identify comparable companies (rest paywalled)'
  notes: 'The in-production label rests on speaker statements that AI is now used for this step; no engagement or client is named. Only one named-organisation figure exists (PwC Singapore, reported by DDTC from a talk). No independent measurement was found: no error rate, no comparison of AI-selected against accepted comparable sets, and no tax authority acceptance data. The ABA and TPMinds entries are session descriptions, not reported content. The KPMG patent item is dated 2024-02 and is background only.'
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
- id: tax-transfer-pricing-02
  title: AI-assisted industry and economic-circumstances research for functional analyses and audit explanations
  work_types:
  - research-synthesis
  - document-production
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: Explaining industry dynamics and margin changes, and writing the industry and functional analyses in TP documentation, means gathering information from many sources (DDTC-WUTA-2026, KPMG-TP-2025).
  solution: The practitioner has the model gather and analyse information from various websites to explain commercial factors behind margin changes. The PwC Singapore example was the surge in margins in glove manufacturing during the pandemic, and the output was said to be usable when engaging with tax authorities (DDTC-WUTA-2026). KPMG says GenAI can automate the industry and functional analyses within TP documentation (KPMG-TP-2025).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: DDTC-WUTA-2026
  prerequisites:
  - Source websites and reports the practitioner can cite
  - Detailed instructions to the model (DDTC-WUTA-2026)
  risks_and_guardrails:
  - Outputs need supervision, risk assessment and quality clean-up by a person (P&G's head of tax for Asia Pacific, India, Middle East, Turkiye and Africa, DDTC-WUTA-2026)
  - A conference speaker cited an Italian tax court case where a draft decision was produced with AI without adequate review (as reported by DDTC; case not identified) (DDTC-WUTA-2026)
  - A hallucination risk and wrong-prompt risk were named for large language models (NOEMA Global founding partner, DDTC-WUTA-2026)
  human_checkpoints:
  - Practitioner checks the facts and sources before they enter the analysis (DDTC-WUTA-2026)
  role_evolution: The speakers present the practitioner as supervisor and risk assessor of the draft (DDTC-WUTA-2026).
  evidence_grade: C
  sources:
  - ref: DDTC-WUTA-2026
    title: Challenges in Transfer Pricing Benchmarking Changes in the AI Era (DDTC report from the WU-TA Advanced Transfer Pricing Programme 2026, Singapore, 28 Sep-1 Oct 2026)
    publisher: DDTCNews (Audreyda Farahbella Anandivi)
    type: press
    url: https://news.ddtc.co.id/en/insight/1822922/challenges-in-transfer-pricing-benchmarking-changes-in-the-ai-era
    date: '2026-10-01'
    access: full
    locator: Jimit Parikh paragraphs (industry dynamics; glove manufacturing); fireside chat paragraphs (Italian tax court case; junior-associate analogy)
  - ref: KPMG-TP-2025
    title: GenAI Revolutionizes Transfer Pricing and Valuation
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/us/en/articles/2025/genai-revolutionizes-transfer-pricing-valuation.html
    date: 2025-04
    access: full
    locator: 'opening paragraph: automate TP documentation including functional, industry and comparable analyses'
  notes: One illustrative example in a conference report plus a firm claim. No figure published for this step.
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
- id: tax-transfer-pricing-03
  title: First-draft TP documentation narrative (local file, master file, entity descriptions) with expert review
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: US taxpayers have 30 days to give the IRS their TP documentation if it is requested, there are no transaction-size thresholds, and annual updates are required. An Exactera speaker named check-the-box documents with generic or copied company descriptions as the most common mistake (TR-CHECKPOINT-2025).
  solution: The professional supplies the facts and context, the model drafts the narrative, and the expert reviews, edits and approves (AIBIDIA-WEBINAR-2026). Participants at Aibidia briefings said they use Microsoft Copilot, ChatGPT and Claude to draft and review documentation (AIBIDIA-STATETP-2026). KPMG's podcast series covers process-improvement methods to find where GenAI helps in TP workflows, balancing quality and accuracy (KPMG-TPPOD-2025). An IBFD journal article covers private GenAI set-up and the credibility and security of outputs (IBFD-ITPJ-2025).
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: AIBIDIA-WEBINAR-2026
  prerequisites:
  - Facts and context supplied by the professional (AIBIDIA-WEBINAR-2026)
  - Standardised, accessible data, mature internal TP processes and functional analyses and agreements already in order (the 'four pillars', AIBIDIA-WEBINAR-2026)
  - A private or secured GenAI set-up (IBFD-ITPJ-2025)
  risks_and_guardrails:
  - Hallucination and overconfident answers; general-purpose models cannot interpret company-specific TP data without context (AIBIDIA-STATETP-2026)
  - Output must be traceable to the evidence behind it (AIBIDIA-WEBINAR-2026)
  - A plausible answer is not enough in TP, because documentation forms the basis of an audit defence (AIBIDIA-WEBINAR-2026)
  human_checkpoints:
  - An accountable professional validates every AI output before it becomes part of the record ('human oversight architecture', AIBIDIA-WEBINAR-2026)
  role_evolution: Local finance or tax contacts who touch TP once a year can use the model as a sparring partner when updating entity descriptions; the expert signs off (AIBIDIA-WEBINAR-2026).
  evidence_grade: C
  sources:
  - ref: AIBIDIA-WEBINAR-2026
    title: 'AI in Transfer Pricing: What''s Working, What''s Not, and What''s Next (summary of the webinar ''From Hype to Help: Where AI Is Working in Transfer Pricing'')'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/ai-in-transfer-pricing-whats-working-whats-not-and-whats-next
    date: 2026-06
    access: full
    locator: section 'What AI Is Actually Good At', paragraphs 'Documentation and narrative drafting' and 'Acting as a sparring partner'; 'Four Pillars for Readiness'
  - ref: AIBIDIA-STATETP-2026
    title: 'From information to intelligence: What senior TP leaders say must change (draws on the Aibidia Report: The State of Transfer Pricing 2026 and London and Helsinki briefings)'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/from-information-to-intelligence-what-senior-tp-leaders-say-must-change
    date: '2026-09-23'
    access: full
    locator: theme 4 (AI adoption is accelerating but integration is lagging)
  - ref: AIBIDIA-TPMINDS-2026
    title: 'TPMinds International 2026: Five Strategic Shifts in Transfer Pricing'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/tpminds-international-2026-five-strategic-shifts-in-transfer-pricing
    date: 2026-06
    access: full
    locator: theme 2 (organisations already deploying AI, including contemporaneous documentation)
  - ref: KPMG-TPPOD-2025
    title: How Can GenAI Improve Transfer Pricing Processes? (Exploring Transfer Pricing podcast)
    publisher: KPMG US
    type: podcast
    url: https://kpmg.com/us/en/podcasts/2025/genai-tp.html
    date: '2025-11-14'
    access: full
    locator: episode description
  - ref: IBFD-ITPJ-2025
    title: 'Operationalizing Transfer Pricing with Generative Artificial Intelligence: Practical Applications and Challenges (D. Olzhabayeva, International Transfer Pricing Journal 32(6); abstract only)'
    publisher: IBFD
    type: academic
    url: https://shop.ibfd.org/journal/operationalizing-transfer-pricing-generative-artificial-intelligence-practical-applications
    date: '2025-09-26'
    access: full
    locator: Overview (abstract)
  - ref: TR-CHECKPOINT-2025
    title: 'Transfer Pricing Expert: ''Prepare Now'' for Best Chance to Avoid Scrutiny (report on an Exactera webinar of 12 September 2025)'
    publisher: Thomson Reuters Checkpoint News (Tim Shaw)
    type: press
    url: https://tax.thomsonreuters.com/news/transfer-pricing-expert-prepare-now-for-best-chance-to-avoid-scrutiny/
    date: '2025-10-15'
    access: full
    locator: paragraphs on the 30-day request window and the 'check-the-box' documentation mistake
  notes: All sources are vendor, firm or event write-ups. No named organisation reports a result for AI-drafted documentation. An undated vendor customer case study on documentation time was read and excluded (see Gaps).
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
- id: tax-transfer-pricing-04
  title: Documentation review against country-specific requirements and for internal consistency
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Documentation must meet country-specific rules that change often. OECD guidelines are not law, and local rules differ (EXACTERA-2025).
  solution: Exactera describes a Word-based app (ExactReport) that reviews a draft against country-specific requirements and suggests real-time edits ('Grammarly for transfer pricing'). It also describes AI that flags inconsistent information and monitors shifting regulations. The source is a sponsored advertising supplement with an early-adopter programme (EXACTERA-2025).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: EXACTERA-2025
  prerequisites:
  - Draft documentation in Word
  - Country-requirement content maintained by the vendor (EXACTERA-2025)
  risks_and_guardrails:
  - The only source is vendor-sponsored; quality of the suggestions is not independently measured (EXACTERA-2025)
  - The IRS closely scrutinises the functional analysis and wants detailed reasons for the chosen method, data sources reviewed and methods rejected (TR-CHECKPOINT-2025)
  human_checkpoints:
  - The preparer accepts or rejects each suggested edit (inferred from the described 'suggestions' workflow in EXACTERA-2025)
  role_evolution: The vendor says professionals move from mundane tasks to more analytical work (EXACTERA-2025).
  evidence_grade: C
  sources:
  - ref: EXACTERA-2025
    title: AI is transforming transfer pricing (sponsored advertising supplement, Q&A with Exactera COO Mimi Song)
    publisher: Exactera in The Tax Adviser (AICPA)
    type: vendor
    url: https://www.thetaxadviser.com/issues/2025/sep/ai-is-transforming-transfer-pricing/
    date: '2025-08-31'
    access: full
    locator: answers to questions 2-4
  - ref: TR-CHECKPOINT-2025
    title: 'Transfer Pricing Expert: ''Prepare Now'' for Best Chance to Avoid Scrutiny (report on an Exactera webinar of 12 September 2025)'
    publisher: Thomson Reuters Checkpoint News (Tim Shaw)
    type: press
    url: https://tax.thomsonreuters.com/news/transfer-pricing-expert-prepare-now-for-best-chance-to-avoid-scrutiny/
    date: '2025-10-15'
    access: full
    locator: section 'Reliance on FAQs'
  notes: Announced as an early-adopter programme (Aug 2025). No customer named and no result published.
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
- id: tax-transfer-pricing-05
  title: Intercompany agreement first drafts from the TP policy, and multi-agent legal/TP/VAT/withholding review
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Drafting intercompany agreements from the TP policy is a task that often stalls for weeks, in the view of a Plante Moran article (PLANTEMORAN-2026).
  solution: AI generates a first draft directly from the TP policy; qualified TP and legal professionals review it before finalising (PLANTEMORAN-2026). A TPMinds International 2026 example (organisation not named in Aibidia's recap) used multi-agent workflows to review legal, TP, VAT and withholding tax implications at once before producing draft agreements (AIBIDIA-TPMINDS-2026).
  outcomes:
  - lever: speed
    description: Plante Moran says a task that often stalls for weeks becomes manageable within hours
    figure: weeks -> hours (qualitative)
    measures: time to produce a first draft of an intercompany agreement; a firm's general statement with no sample or method
    provenance: self-reported
    source_ref: PLANTEMORAN-2026
  prerequisites:
  - A written TP policy to draft from (PLANTEMORAN-2026)
  - Supervising TP and legal reviewers (PLANTEMORAN-2026)
  risks_and_guardrails:
  - The draft is a starting point, not bespoke legal or tax advice (PLANTEMORAN-2026)
  - Speakers at TPMinds were unanimous that AI enhances expertise but does not replace it (AIBIDIA-TPMINDS-2026)
  human_checkpoints:
  - Qualified TP and legal professionals review before the agreement is finalised (PLANTEMORAN-2026)
  role_evolution: Not described beyond reviewers keeping responsibility (PLANTEMORAN-2026).
  evidence_grade: C
  sources:
  - ref: PLANTEMORAN-2026
    title: 'Using AI in transfer pricing: Practical opportunities and pitfalls for growing companies'
    publisher: Plante Moran (Lara Witte, Biz Pavelich, Kevin Lee)
    type: firm
    url: https://plantemoran.com/explore-our-thinking/insight/2026/08/using-ai-in-transfer-pricing
    date: '2026-08-05'
    access: full
    locator: item 'Drafting intercompany agreements' and 'Key takeaways'
  - ref: AIBIDIA-TPMINDS-2026
    title: 'TPMinds International 2026: Five Strategic Shifts in Transfer Pricing'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/tpminds-international-2026-five-strategic-shifts-in-transfer-pricing
    date: 2026-06
    access: full
    locator: theme 2 (multi-agent example)
  notes: The multi-agent example is a conference recap written by a vendor; no organisation, result or error rate is given.
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
- id: tax-transfer-pricing-06
  title: 'In-year operational TP monitoring: margin tracking against policy ranges and exception flagging'
  work_types:
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: In the Aibidia State of Transfer Pricing 2026 survey (97 in-house tax professionals, as reported by Aibidia), 38% described operational TP processes as well defined and managed, 60% rely mainly on Excel, email and other manual processes, only 7% formally monitor transfer prices monthly, and half report moderately or very significant year-end adjustments (AIBIDIA-STATETP-2026).
  solution: A practitioner loads raw data into an AI tool to produce simple dashboards that track margins against target ranges through the year, flag unusual transactions or deviations and highlight higher-risk jurisdictions (PLANTEMORAN-2026). A TPMinds recap says organisations already deploy AI to monitor operational outcomes and flag audit risks in real time (AIBIDIA-TPMINDS-2026). An Aibidia interviewee describes a monthly OTP cycle in which ERP data is loaded to a TP tool, results are reviewed using trend analysis and unusual movements investigated (AIBIDIA-OTP-2026).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: AIBIDIA-STATETP-2026
  prerequisites:
  - Granular, centralised data and clear ownership of loads, exception review and sign-off (AIBIDIA-OTP-2026)
  - A calculation layer under the language model, because LLMs are weak with numbers (AIBIDIA-WEBINAR-2026)
  risks_and_guardrails:
  - Untested AI analyses can fall short on rationale in an audit without professional review (PLANTEMORAN-2026)
  - Controls must show what data was used, what changed, who reviewed and who approved (AIBIDIA-OTP-2026)
  human_checkpoints:
  - TP team investigates flagged deviations and decides adjustments; controllers and finance own execution (AIBIDIA-STATETP-2026, AIBIDIA-OTP-2026)
  role_evolution: The ideal described by a participant is a real-time view of margin against policy benchmarks, so teams act before year-end corrections (AIBIDIA-STATETP-2026). TP professionals can identify risk but do not always control the commercial decisions that create exposure (AIBIDIA-STATETP-2026).
  evidence_grade: C
  sources:
  - ref: AIBIDIA-STATETP-2026
    title: 'From information to intelligence: What senior TP leaders say must change (draws on the Aibidia Report: The State of Transfer Pricing 2026 and London and Helsinki briefings)'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/from-information-to-intelligence-what-senior-tp-leaders-say-must-change
    date: '2026-09-23'
    access: full
    locator: theme 3 (policy versus operational reality) and theme 1
  - ref: PLANTEMORAN-2026
    title: 'Using AI in transfer pricing: Practical opportunities and pitfalls for growing companies'
    publisher: Plante Moran (Lara Witte, Biz Pavelich, Kevin Lee)
    type: firm
    url: https://plantemoran.com/explore-our-thinking/insight/2026/08/using-ai-in-transfer-pricing
    date: '2026-08-05'
    access: full
    locator: item 'Monitoring results and flagging risk'
  - ref: AIBIDIA-OTP-2026
    title: 'Connected, Controlled and Audit-ready: That''s the Future of Operational Transfer Pricing (interview with Roshni D''Silva)'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/connected-controlled-and-audit-ready-thats-the-future-of-operational-transfer-pricing
    date: '2026-07-03'
    access: full
    locator: answers on the monthly OTP process and controls
  - ref: AIBIDIA-WEBINAR-2026
    title: 'AI in Transfer Pricing: What''s Working, What''s Not, and What''s Next (summary of the webinar ''From Hype to Help: Where AI Is Working in Transfer Pricing'')'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/ai-in-transfer-pricing-whats-working-whats-not-and-whats-next
    date: 2026-06
    access: full
    locator: section 'The Challenges Are Real', paragraph 'LLMs and numbers don't mix well'
  - ref: AIBIDIA-TPMINDS-2026
    title: 'TPMinds International 2026: Five Strategic Shifts in Transfer Pricing'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/tpminds-international-2026-five-strategic-shifts-in-transfer-pricing
    date: 2026-06
    access: full
    locator: theme 2
  notes: Survey figures are vendor-published and describe the problem, not a result of AI. Respondent counts differ across Aibidia pages (97 for the 2026 survey; 140+ for the earlier edition) and the sample is not described as random.
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
- id: tax-transfer-pricing-07
  title: AI-assisted aggregation and standardisation of ERP and ledger data for TP analyses
  work_types:
  - data-reporting
  - transaction-processing
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: Seventy-nine percent of respondents to Aibidia's 2026 survey spend more than 10% of their team's time sourcing, cleaning and formatting data, 21% at least half, and nearly half operate across four or more ERP or financial reporting systems (AIBIDIA-STATETP-2026). Year-end analyses become a scramble to pull, reconcile and standardise data (PLANTEMORAN-2026).
  solution: Plante Moran says AI can aggregate information from multiple accounting and ERP platforms into a consistent format with less manual spreadsheet work and without heavy IT investment (PLANTEMORAN-2026). Webinar speakers say fragmented or manual data should be standardised first (AIBIDIA-WEBINAR-2026).
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: AIBIDIA-STATETP-2026
  prerequisites:
  - Shared definitions and clear data ownership across tax, finance, controlling, IT and local teams (AIBIDIA-STATETP-2026)
  risks_and_guardrails:
  - Only 22% of respondents believe their TP data is structured and clean enough for AI to use without manual intervention (AIBIDIA-STATETP-2026)
  - Advisers should review the AI input process (PLANTEMORAN-2026)
  human_checkpoints:
  - Advisers or the TP team review how inputs were prepared (PLANTEMORAN-2026)
  role_evolution: The survey write-up says highly skilled TP professionals spend time reconstructing context instead of interpreting it (AIBIDIA-STATETP-2026).
  evidence_grade: C
  sources:
  - ref: AIBIDIA-STATETP-2026
    title: 'From information to intelligence: What senior TP leaders say must change (draws on the Aibidia Report: The State of Transfer Pricing 2026 and London and Helsinki briefings)'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/from-information-to-intelligence-what-senior-tp-leaders-say-must-change
    date: '2026-09-23'
    access: full
    locator: theme 2 (data wrangling) and theme 4
  - ref: PLANTEMORAN-2026
    title: 'Using AI in transfer pricing: Practical opportunities and pitfalls for growing companies'
    publisher: Plante Moran (Lara Witte, Biz Pavelich, Kevin Lee)
    type: firm
    url: https://plantemoran.com/explore-our-thinking/insight/2026/08/using-ai-in-transfer-pricing
    date: '2026-08-05'
    access: full
    locator: item 'Aggregation and standardization of data'
  - ref: AIBIDIA-WEBINAR-2026
    title: 'AI in Transfer Pricing: What''s Working, What''s Not, and What''s Next (summary of the webinar ''From Hype to Help: Where AI Is Working in Transfer Pricing'')'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/ai-in-transfer-pricing-whats-working-whats-not-and-whats-next
    date: 2026-06
    access: full
    locator: '''The Challenges Are Real'', paragraph ''Data quality is make-or-break'''
  notes: Practitioners treat data readiness as a prerequisite for AI more than as a result of it. Evidence for AI doing the aggregation is a single firm article.
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
- id: tax-transfer-pricing-08
  title: Grounded TP research and regulatory-change assistant (local requirements, deadlines, definitions, guidance)
  work_types:
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Regulations, guidelines and case law change constantly; central TP teams cover dozens of jurisdictions, and local subsidiaries touch TP perhaps once a year (AIBIDIA-WEBINAR-2026).
  solution: TP Aurora (Aibidia with IBFD) answers TP questions from IBFD data on legislation, benchmarking guidelines and compliance insights; the release says it was available to all from 22 May 2025 with a free trial (AIBIDIA-IBFD-2025). Webinar speakers describe an always-on assistant to check definitions, deadlines and local requirements (AIBIDIA-WEBINAR-2026). KPMG says GenAI can scrutinise global tax and TP developments (KPMG-TP-2025).
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: AIBIDIA-IBFD-2025
  prerequisites:
  - Curated, up-to-date legal and guidance content as the grounding source (AIBIDIA-IBFD-2025)
  risks_and_guardrails:
  - General-purpose models can give authoritative-looking answers without clear sourcing; traceability is needed (AIBIDIA-WEBINAR-2026)
  - Consumer-facing AI TP tools may oversimplify complex rules (PLANTEMORAN-2026)
  human_checkpoints:
  - User confirms the answer against the cited source before relying on it (inferred from the 'grounded in IBFD data' design, AIBIDIA-IBFD-2025)
  role_evolution: The assistant lets every user, including non-specialists, get up to speed without burdening the central team (AIBIDIA-WEBINAR-2026).
  evidence_grade: C
  sources:
  - ref: AIBIDIA-IBFD-2025
    title: 'Aibidia and IBFD Launch TP Aurora: A Groundbreaking AI Transfer Pricing Research Assistant'
    publisher: IBFD / Aibidia
    type: vendor
    url: https://www.ibfd.org/news/aibidia-and-ibfd-launch-tp-aurora-groundbreaking-ai-transfer-pricing-research-assistant
    date: '2025-05-22'
    access: full
    locator: paragraphs 1-3 and 'When is TP Aurora available?'
  - ref: AIBIDIA-WEBINAR-2026
    title: 'AI in Transfer Pricing: What''s Working, What''s Not, and What''s Next (summary of the webinar ''From Hype to Help: Where AI Is Working in Transfer Pricing'')'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/ai-in-transfer-pricing-whats-working-whats-not-and-whats-next
    date: 2026-06
    access: full
    locator: paragraph 'Research and staying current'
  - ref: KPMG-TP-2025
    title: GenAI Revolutionizes Transfer Pricing and Valuation
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/us/en/articles/2025/genai-revolutionizes-transfer-pricing-valuation.html
    date: 2025-04
    access: full
    locator: opening paragraph
  - ref: PLANTEMORAN-2026
    title: 'Using AI in transfer pricing: Practical opportunities and pitfalls for growing companies'
    publisher: Plante Moran (Lara Witte, Biz Pavelich, Kevin Lee)
    type: firm
    url: https://plantemoran.com/explore-our-thinking/insight/2026/08/using-ai-in-transfer-pricing
    date: '2026-08-05'
    access: full
    locator: section 'Understanding AI's limits'
  notes: The release is a launch announcement. No customer, usage figure or accuracy test is published.
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
- id: tax-transfer-pricing-09
  title: 'Controversy support: drafting and stress-testing responses to tax-authority queries'
  work_types:
  - document-production
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: An IRS LB&I official expects TP expert witnesses to explain inputs, assumptions, methods and any AI tools, and wants to see the formulas (IRS-LBI-TP-2026). A PwC TP principal says examiners now ask about intent and business purpose, which makes contemporaneous records important (TR-CHECKPOINT-2026).
  solution: KPMG says GenAI can review historical documents and formulate responses in TP controversy (KPMG-TP-2025). Participants at Aibidia briefings said they use general AI tools to stress-test responses to tax authorities (AIBIDIA-STATETP-2026). The PwC Singapore example of gathering information to explain margin changes was framed as support when engaging with tax authorities (DDTC-WUTA-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: KPMG-TP-2025
  prerequisites:
  - Contemporaneous documentation to draw on (TR-CHECKPOINT-2026)
  risks_and_guardrails:
  - Taxpayers using AI for benchmarking or other analysis must still show the underlying work, with human judgment and oversight (TR-CHECKPOINT-2026)
  - AI can support but not replace legal, economic and factual judgment (IRS-LBI-TP-2026)
  human_checkpoints:
  - The practitioner and responsible expert own the response; the IRS can test the formulas (IRS-LBI-TP-2026)
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
  - ref: KPMG-TP-2025
    title: GenAI Revolutionizes Transfer Pricing and Valuation
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/us/en/articles/2025/genai-revolutionizes-transfer-pricing-valuation.html
    date: 2025-04
    access: full
    locator: opening paragraph (TP controversy)
  - ref: AIBIDIA-STATETP-2026
    title: 'From information to intelligence: What senior TP leaders say must change (draws on the Aibidia Report: The State of Transfer Pricing 2026 and London and Helsinki briefings)'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/from-information-to-intelligence-what-senior-tp-leaders-say-must-change
    date: '2026-09-23'
    access: full
    locator: theme 4, list of uses
  - ref: DDTC-WUTA-2026
    title: Challenges in Transfer Pricing Benchmarking Changes in the AI Era (DDTC report from the WU-TA Advanced Transfer Pricing Programme 2026, Singapore, 28 Sep-1 Oct 2026)
    publisher: DDTCNews (Audreyda Farahbella Anandivi)
    type: press
    url: https://news.ddtc.co.id/en/insight/1822922/challenges-in-transfer-pricing-benchmarking-changes-in-the-ai-era
    date: '2026-10-01'
    access: full
    locator: Jimit Parikh paragraph on glove manufacturing
  - ref: IRS-LBI-TP-2026
    title: Report on recent US international tax developments, 31 July 2026 (reports IRS LB&I remarks on AI in transfer pricing, 29 July 2026)
    publisher: Ernst & Young LLP (EY Tax News & Developments)
    type: firm
    url: https://taxnews.ey.com/news/2026-1658-report-on-recent-us-international-tax-developments-31-july-2026
    date: '2026-07-31'
    access: full
    locator: paragraphs 3-4 of the TP item
  - ref: TR-CHECKPOINT-2026
    title: AI-powered IRS audits are here but taxpayers have new relief options, tax pros say (report on a 30 July 2026 PwC webcast)
    publisher: Thomson Reuters Checkpoint News (Tim Shaw)
    type: press
    url: https://tax.thomsonreuters.com/news/ai-powered-irs-audits-are-here-but-taxpayers-have-new-relief-options-tax-pros-say/
    date: '2026-08-05'
    access: full
    locator: section 'Economic substance, transfer pricing lead compliance hot topics'
  notes: A firm claim and a vendor-reported participant practice; no named user or result.
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
- id: tax-transfer-pricing-10
  title: Self-run audit-risk screening of intercompany results against signals tax authorities use
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: A Checkpoint report on an Exactera webinar says the IRS sent compliance letters to low-margin limited-risk distributors, and that the IRS uses algorithms to find companies with unreasonable losses or very low margins (TR-CHECKPOINT-2025). Reptune says tax authorities are moving to near real-time data and AI to assess TP continuously (REPTUNE-TPMWC-2026).
  solution: Exactera says AI can predict where a company is most vulnerable to audits and adjustments (EXACTERA-2025). A TPMinds International session was scheduled on AI for risk assessment and on whether authorities will adopt similar tools (TPMINDS-INTL-2026). An ABA panel was scheduled on risk-assessment automation and the likelihood that tax authorities deploy similar technologies (ABA-MAYMTG-2026).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: EXACTERA-2025
  prerequisites:
  - Entity-level margin and transaction data (see use case 07)
  risks_and_guardrails:
  - An AI arms race between tax authorities and multinationals is a stated worry (KPMG-TNF-2024)
  - The commentary notes that authority models only help if administrators understand them (KPMG-TNF-2024)
  human_checkpoints:
  - TP team decides whether to adjust pricing or prepare a defence for flagged results (TR-CHECKPOINT-2025)
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
  - ref: EXACTERA-2025
    title: AI is transforming transfer pricing (sponsored advertising supplement, Q&A with Exactera COO Mimi Song)
    publisher: Exactera in The Tax Adviser (AICPA)
    type: vendor
    url: https://www.thetaxadviser.com/issues/2025/sep/ai-is-transforming-transfer-pricing/
    date: '2025-08-31'
    access: full
    locator: answer to question 1
  - ref: TR-CHECKPOINT-2025
    title: 'Transfer Pricing Expert: ''Prepare Now'' for Best Chance to Avoid Scrutiny (report on an Exactera webinar of 12 September 2025)'
    publisher: Thomson Reuters Checkpoint News (Tim Shaw)
    type: press
    url: https://tax.thomsonreuters.com/news/transfer-pricing-expert-prepare-now-for-best-chance-to-avoid-scrutiny/
    date: '2025-10-15'
    access: full
    locator: section 'IRS Cuts and Shift Towards AI'
  - ref: TPMINDS-INTL-2026
    title: TPMinds International 2026, Main Summit Day 1 agenda (16 June 2026, London)
    publisher: Informa Connect
    type: conference
    url: https://informaconnect.com/tp-minds-international-conference/agenda/
    date: '2026-06-16'
    access: full
    locator: Day 1, 15:45-16:30 session description
  - ref: ABA-MAYMTG-2026
    title: 'ABA Section of Taxation May Tax Meeting 2026, final program (Transfer Pricing session ''AI and Transfer Pricing Under §482: Transforming Compliance and Risk Management'')'
    publisher: ABA Section of Taxation
    type: conference
    url: https://sitepilot11.firmseek.com/client/chamberlain/www/media/event/657_ABA_Section_of_Taxation_2026_May_Meeting_Agenda.pdf
    date: '2026-05-08'
    access: full
    locator: Transfer Pricing programme, session description
  - ref: REPTUNE-TPMWC-2026
    title: Reptune sponsor profile, TPMinds West Coast (event 4-5 Nov 2026; page publication date not shown)
    publisher: Informa Connect / Reptune
    type: vendor
    url: https://informaconnect.com/tp-minds-west-coast/sponsors/reptune/
    date: '2026'
    access: full
    locator: '''Profile'' paragraph (vendor marketing; publication date not shown)'
  - ref: KPMG-TNF-2024
    title: AI May Take Transfer Pricing Up a Notch but Carries Some Risk (KPMG TaxNewsFlash reprint of a Bloomberg Tax commentary)
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/kpmg-us/content/dam/kpmg/taxnewsflash/pdf/2024/10/ai-transfer-pricing-risk-oct21-2024.pdf
    date: '2024-10-21'
    access: full
    locator: bullets and paragraphs on tax authority use of AI
  notes: Vendor claims and scheduled panels only. The ABA and TPMinds entries are programme text, not reported findings.
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
- id: tax-transfer-pricing-11
  title: AI support for APA and MAP case management, negotiation preparation and outcome prediction (idea)
  work_types:
  - expert-judgment
  - coordination-scheduling
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: APAs and MAPs involve case tracking, negotiation preparation and uncertain outcomes (KPMG-TNF-2024).
  solution: A KPMG commentary (Oct 2024) suggests AI could improve case management, give data-driven negotiation support and predict outcomes from past cases. It also floats an 'AI pre-pre-filing conference' in which a taxpayer feeds data to a model trained on historical MAP and APA data (KPMG-TNF-2024).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: KPMG-TNF-2024
  prerequisites:
  - Authority-held historical MAP and APA data made available to taxpayers, as the commentary envisages (KPMG-TNF-2024)
  risks_and_guardrails:
  - The same piece warns AI could lead to scrutiny of every small transaction and an arms race among authorities (KPMG-TNF-2024)
  human_checkpoints:
  - Not specified
  role_evolution: Not described in the sources.
  evidence_grade: D
  sources:
  - ref: KPMG-TNF-2024
    title: AI May Take Transfer Pricing Up a Notch but Carries Some Risk (KPMG TaxNewsFlash reprint of a Bloomberg Tax commentary)
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/kpmg-us/content/dam/kpmg/taxnewsflash/pdf/2024/10/ai-transfer-pricing-risk-oct21-2024.pdf
    date: '2024-10-21'
    access: full
    locator: paragraphs under 'But it isn't necessarily all bad news for taxpayers'
  notes: Idea only, discussed by a practitioner commentary (dated Oct 2024, older than the 12-18 month window and used as foundation). No deployment found. A TPMinds Americas 2027 planned session list includes APA/MAP certainty but does not tie it to AI (TPMINDS-AM-2027).
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
- id: tax-transfer-pricing-12
  title: 'Connected TP ''system of intelligence'': policy, agreements, financials and benchmarks in one evidence-linked model'
  work_types:
  - data-reporting
  - review-assurance
  pattern: reconcile-exceptions
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Policies, agreements, benchmarks, financial results, documentation and audit history usually exist but sit in different systems, so teams connect them by hand (AIBIDIA-STATETP-2026).
  solution: Aibidia described a system that reads and structures agreements, financial data, policies and benchmarks, makes transaction flows visible, finds inconsistencies and traces insights to evidence. In a Helsinki demonstration it identified and quantified a potential EUR 4.8 million risk in one entity, linked it to the supporting agreement and proposed an action (AIBIDIA-STATETP-2026). Majorities of survey respondents expect AI agents to gather and format data, monitor compliance and do first-pass audit reviews within two to three years (AIBIDIA-STATETP-2026). A scheduled TPMinds West Coast session says AI is evolving from a productivity tool into an integral component of TP operating models, with speakers from Anthropic, OpenAI, Uber and KPMG (TPMINDS-WC-2026).
  outcomes:
  - lever: risk
    description: Potential risk quantified by the system in a vendor demonstration
    figure: EUR 4.8 million, one entity (demonstration)
    measures: amount of potential risk identified in a demonstration at a vendor briefing; not a customer result
    provenance: vendor-published
    source_ref: AIBIDIA-STATETP-2026
  prerequisites:
  - Connected, structured data (only 22% of respondents say theirs is clean enough) (AIBIDIA-STATETP-2026)
  - Domain-specific logic, guardrails and traceability to source (AIBIDIA-STATETP-2026)
  - 'Step-by-step build: one-shot end-to-end agents are not expected on the first attempt (AIBIDIA-WEBINAR-2026)'
  risks_and_guardrails:
  - The goal is stated as not autonomous AI making unsupported decisions (AIBIDIA-STATETP-2026)
  - Every flag should link back to a source for a reviewer or auditor (AIBIDIA-STATETP-2026)
  human_checkpoints:
  - Controller, reviewer or auditor inspects the evidence behind each flag (AIBIDIA-STATETP-2026)
  role_evolution: Speakers say teams should decide where to build enduring internal understanding and where to rely on technology or external expertise (AIBIDIA-STATETP-2026).
  evidence_grade: C
  sources:
  - ref: AIBIDIA-STATETP-2026
    title: 'From information to intelligence: What senior TP leaders say must change (draws on the Aibidia Report: The State of Transfer Pricing 2026 and London and Helsinki briefings)'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/from-information-to-intelligence-what-senior-tp-leaders-say-must-change
    date: '2026-09-23'
    access: full
    locator: themes 4 and 5; section 'The next era of transfer pricing'
  - ref: AIBIDIA-WEBINAR-2026
    title: 'AI in Transfer Pricing: What''s Working, What''s Not, and What''s Next (summary of the webinar ''From Hype to Help: Where AI Is Working in Transfer Pricing'')'
    publisher: Aibidia
    type: vendor
    url: https://www.aibidia.com/blog/ai-in-transfer-pricing-whats-working-whats-not-and-whats-next
    date: 2026-06
    access: full
    locator: '''Four Pillars for Readiness'' and ''The Right Mindset'''
  - ref: TPMINDS-WC-2026
    title: TPMinds West Coast 2026, Day 1 and Day 2 agendas (4-5 November 2026, Palo Alto; programme published, event not yet held)
    publisher: Informa Connect
    type: conference
    url: https://informaconnect.com/tp-minds-west-coast/agenda/
    date: '2026-11-04'
    access: full
    locator: Day 1, 15:35-16:35 session 'Case Studies on the Application of AI in Transfer Pricing'
  notes: Vendor positioning and demonstration. TPMinds West Coast is scheduled for 4-5 Nov 2026 and has not been held; no session content is reported.
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
- id: tax-transfer-pricing-13
  title: TP policy modelling and planning-opportunity screening
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Advisers and tax teams look for planning opportunities across jurisdictions and updated calculations (KPMG-TP-2025).
  solution: KPMG says GenAI can scrutinise global tax and TP developments to pinpoint planning prospects, parse financials and update calculations (KPMG-TP-2025). Plante Moran says some companies are experimenting with lightweight models that test subsidiary financials against standardised country tax rates, and calls these a jump-start for a conversation with an adviser, not a self-contained answer (PLANTEMORAN-2026).
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: PLANTEMORAN-2026
  prerequisites:
  - Subsidiary financials in structured form (PLANTEMORAN-2026)
  risks_and_guardrails:
  - Outputs work best as input to adviser discussion, not as conclusions (PLANTEMORAN-2026)
  - Plante Moran calls these concepts promising but best used as a conversation starter (PLANTEMORAN-2026)
  human_checkpoints:
  - Adviser reviews the model's result before any policy change (PLANTEMORAN-2026)
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
  - ref: KPMG-TP-2025
    title: GenAI Revolutionizes Transfer Pricing and Valuation
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/us/en/articles/2025/genai-revolutionizes-transfer-pricing-valuation.html
    date: 2025-04
    access: full
    locator: opening paragraph
  - ref: PLANTEMORAN-2026
    title: 'Using AI in transfer pricing: Practical opportunities and pitfalls for growing companies'
    publisher: Plante Moran (Lara Witte, Biz Pavelich, Kevin Lee)
    type: firm
    url: https://plantemoran.com/explore-our-thinking/insight/2026/08/using-ai-in-transfer-pricing
    date: '2026-08-05'
    access: full
    locator: item 'Monitoring results and flagging risk', last two sentences
  notes: Firm claim plus a statement that 'some companies' experiment; no named user.
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  last_reviewed: '2026-10-17'
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **TP policy design and planning:** expert-judgment, research-synthesis (use case 13; KPMG-TP-2025, PLANTEMORAN-2026).
- **Functional and industry analysis:** research-synthesis, document-production (use case 02; DDTC-WUTA-2026).
- **Benchmarking and comparables search:** research-synthesis, data-reporting (use case 01; DDTC-WUTA-2026, PLANTEMORAN-2026).
- **Master file, local file and country-by-country report preparation:** document-production, data-reporting; review against country rules is review-assurance (use cases 03 and 04; TR-CHECKPOINT-2025 defines the three documents; EXACTERA-2025).
- **Intercompany agreements:** document-production, review-assurance (use case 05; PLANTEMORAN-2026).
- **Operational transfer pricing:** a monthly cycle in which ERP data is loaded to a TP tool, calculations run, results reviewed by trend analysis, unusual movements investigated, TP entries posted and ledger balances reconciled; transaction-processing, data-reporting (use cases 06, 07; AIBIDIA-OTP-2026).
- **Data collection from local entities and controllers:** data-reporting (use case 07; AIBIDIA-STATETP-2026).
- **Audit defence, APAs, MAPs and disputes:** expert-judgment, document-production, client-interaction (use cases 09-11; KPMG-TP-2025, KPMG-TNF-2024).

### Common pain points

- **Fragmented data:** 79% of respondents spend more than 10% of team time sourcing, cleaning and formatting data, 21% at least half, and nearly half run four or more ERP or reporting systems (AIBIDIA-STATETP-2026).
- **Thin teams:** 63% have three or fewer dedicated TP professionals, while more than four in five respondents' organisations have revenue above USD 1 billion (AIBIDIA-STATETP-2026).
- **Policy versus reality:** only 7% formally monitor transfer prices monthly and half report moderately or very significant year-end adjustments (AIBIDIA-STATETP-2026).
- **Enforcement pressure with a smaller IRS:** compliance letters to low-margin limited-risk distributors, algorithms to find persistent losses, and a stated expectation of catch-up audits (TR-CHECKPOINT-2025, a report on an Exactera webinar).
- **Short windows:** 30 days to hand over documentation on IRS request, no transaction-size threshold, annual updates (TR-CHECKPOINT-2025).
- **Cost of benchmarking:** a PwC Singapore partner said a single analysis cost tens of thousands of US dollars two decades ago (DDTC-WUTA-2026).

### Metrics and benchmarks (what each figure measures)

| Figure | What it measures, in the source's words | Provenance | Ref |
|---|---|---|---|
| 93% use AI; 7% no AI use (down from 36%); 37% regular use across TP processes (up from 18%) | respondents reporting AI use, one-year change; 97 in-house tax professionals | vendor-published | AIBIDIA-STATETP-2026 |
| 22% | respondents who believe their TP data is structured and clean enough for AI to use without manual intervention | vendor-published | AIBIDIA-STATETP-2026 |
| 53% hybrid sourcing, up from 38% in 2024 | respondents that combine substantial internal capability with external support | vendor-published | AIBIDIA-STATETP-2026 |
| roughly 40% minimal AI use; dedicated TP software adoption nearly doubled | earlier edition of the Aibidia survey, 140+ respondents; definitions differ from the 2026 'no use' figure, so the two cannot be compared directly | vendor-published | AIBIDIA-WEBINAR-2026 |
| up to 100 hours to about 30 minutes | analysis (type unspecified) 'under certain conditions', conference remark | self-reported | DDTC-WUTA-2026 |
| about 80% | share of comparability-analysis work AI 'may' complete, conference remark | self-reported | DDTC-WUTA-2026 |
| up to 40% of the adjustment | penalty exposure without contemporaneous documentation, per an Exactera speaker | self-reported | TR-CHECKPOINT-2025 |
| about 80% of Fast Track Settlement cases settled in roughly 100 days | PwC speaker on IRS dispute programmes; not about AI | self-reported | TR-CHECKPOINT-2026 |
| 6 months to more than a year per case | length of a complete TP audit, per a CIAT blog author; authority side | self-reported | CIAT-BLOG-2026 |

No independent benchmark of AI accuracy, override rate or tax-authority acceptance in transfer pricing was found.

### Guardrails and regulatory points

- **IRS LB&I (29 July 2026):** AI can support legal, economic and factual judgment but should not replace it. Expert witnesses are expected to explain inputs, assumptions, methods and AI tools, and the IRS wants to see the formulas to test them (IRS-LBI-TP-2026).
- **PwC TP principal (30 July 2026 webcast):** even where AI prompts are used for benchmarking, the formulas and methodology still need human judgment and oversight; examiners now ask about intent and business purpose (TR-CHECKPOINT-2026).
- **Documentation standard:** the IRS wants specific reasons for the method chosen, data sources reviewed and methods rejected; generic or copied descriptions are called the most common mistake (TR-CHECKPOINT-2025).
- **Cross-cutting conduct rules** (IRS OPR Alert 2026-19, UK PCRT guidance, Australia TPB guidance) are in the landscape file and were not re-read for this angle.
- **OECD Chapter VII (intra-group services) consultation:** launched 1 June 2026 with 21 new examples, comments due 22 July 2026, stated not to change the general principles (PWC-DE-OECD-2026). Bloomberg reports the draft's examples include sharing AI tools between related companies, and that AstraZeneca asked the OECD to clarify how to characterise AI transactions between affiliates (OECD-INTRAGROUP-2026).
- **HMRC International Controlled Transactions Schedule (proposal of 28 April 2025):** a schedule designed to enable automated data-led risk assessment; the information is described as corresponding to what a Local File holds (KPMG-UK-ICTS-2025). Whether it was adopted was not checked.
- **Confidentiality:** entering sensitive company data into AI systems raises privacy and confidentiality risk, and vendor security practices warrant evaluation (DDTC-WUTA-2026, PLANTEMORAN-2026).
- **Search-only items (not used for grading):** an ABA Tax Times summary says panelists held that AI may increase speed and scale but does not change the legal framework, so practitioners stay responsible for method selection, input integrity and defensibility (ABA-TAXTIMES-2026). A BDO Canada piece is described as saying AI output often falls short on functional analyses, benchmarking, method selection and DEMPE without human review (BDO-CA-2026). KPMG Germany said GenAI can speed master and local file creation but specialists must check plausibility (KPMG-DE-2025).

### Frontier signals (dated)

- **2025-05-22:** Aibidia and IBFD launch TP Aurora, a TP research assistant grounded in IBFD data (AIBIDIA-IBFD-2025).
- **2025-11-14:** KPMG's podcast frames the question as where to start, using process-improvement methods to find where GenAI helps TP workflows (KPMG-TPPOD-2025).
- **2026-02-03:** a CIAT blog author argues tax administrations are moving from predictive risk models to agentic AI for end-to-end TP control, 'always under human supervision' (CIAT-BLOG-2026; author's opinion).
- **2026-05-08:** ABA Tax Section panel on AI and section 482, with an IRS panelist; described topics are AI-driven benchmarking, documentation automation, monitoring and risk assessment, defensibility of AI analyses, and whether authorities will use similar tools (ABA-MAYMTG-2026, PILLSBURY-ABA-2026).
- **2026-06-16/17:** Aibidia's recap says AI dominated TPMinds International and the focus moved from theory to practice, including a multi-agent agreement-review example (AIBIDIA-TPMINDS-2026).
- **2026-07-29:** IRS LB&I remarks on AI and expert witnesses (IRS-LBI-TP-2026).
- **2026-09-23:** majorities of Aibidia survey respondents expect AI agents to gather and format data, monitor compliance and do first-pass audit reviews within two to three years (AIBIDIA-STATETP-2026; vendor survey).
- **2026-11-04/05 (scheduled):** TPMinds West Coast lists a case-study session with TP heads from Anthropic, OpenAI and Uber and a panel on human TP skills in the age of AI (TPMINDS-WC-2026).
- **2027-03-01 (planned):** TPMinds Americas AI Transformation Day, and planned sessions 'The AI Arms Race in TP' and on managing audits in the age of AI and enhanced data analytics (TPMINDS-AM-2027).
- **Vendor positioning:** Reptune says tax authorities are using near real-time data and AI to assess TP continuously (REPTUNE-TPMWC-2026).

### Workforce and role effects

- The TPMinds West Coast panel 'Redefining Human TP Skills in the Age of AI' asks how to build expertise and judgment when foundational processes become automated, what skills gain value, and where humans must stay accountable. It explicitly covers 'rationalizing headcount' (TPMINDS-WC-2026; programme text, outcome not reported).
- New role titles appear in speaker lists: Global Head of Transfer Pricing and Tax Automation (Deutsche Bank, TPMINDS-INTL-2026) and Global Transfer Pricing Technology Leader (KPMG, TPMINDS-WC-2026).
- A webinar panelist said AI will not take your job but someone using AI might (AIBIDIA-WEBINAR-2026). A NOEMA Global founding partner compared AI to the calculator (DDTC-WUTA-2026). A P&G head of tax likened AI to a junior associate (DDTC-WUTA-2026).
- Aibidia's London session reported participants questioning the value of traditional advisory models when substantive work is offshored, automated or delegated to juniors, and a shift toward hybrid sourcing (53% in 2026 against 38% in 2024). The source does not attribute the shift to AI (AIBIDIA-STATETP-2026).
- Speakers say practitioners move toward validation, supervision and judgment (CIAT-BLOG-2026, DDTC-WUTA-2026). Michel Braun of WTS Digital concludes AI will enhance, not replace, the tax professional (ITR-BRAUN-2025; standfirst only).

### Objections and concerns practitioners raise

- **Hallucination and wrong-prompt risk,** including a reported Italian tax court case with an AI-produced draft decision and no adequate review (DDTC-WUTA-2026; case unidentified).
- **Language models and numbers:** LLMs are strong on language and weak on arithmetic, so a calculation layer is needed (AIBIDIA-WEBINAR-2026).
- **Defensibility:** untested AI analyses can fall short on rationale in an audit; plug-and-play outputs can create a false sense of security (PLANTEMORAN-2026).
- **Data privacy and the need for regulatory boundaries,** compared by the PwC partner to roads, speed limits and traffic lights for cars (DDTC-WUTA-2026).
- **An AI arms race** between authorities and multinationals, and opaque authority models (KPMG-TNF-2024; TPMinds Americas 2027 planned session, TPMINDS-AM-2027).
- **Source bias:** much of the public record is vendor-authored or vendor-sponsored (Aibidia, Exactera, Reptune), so adoption and benefit claims should be read as claims.
- **AI changes the facts being priced:** AI is hard to separate into functions, assets and risks, and a TP analysis for one year may not hold the next as the technology changes (IBA-TAXAI-2025; report on a 2024 session).

### Interview probes for an advisor

1. Which TP steps does the team let a model touch today (comparables, local file narrative, agreement drafts, margin monitoring), and who signs off the output before it enters the file?
2. How many ERPs and ledgers feed your TP analysis, who owns the mapping, and how clean is the data when you start the year-end work? (Aibidia's survey puts 22% as clean enough.)
3. If an authority asked you to explain inputs, assumptions and formulas for an AI-assisted analysis, what could you show today?
4. Has an AI-suggested comparable set, draft clause or flagged risk ever been wrong or rejected, and how was it caught? (No error-rate evidence exists publicly.)
5. How is the split between in-house work and outside advisers changing, and what would you stop paying an adviser for?

---

## 4. Routed to other modules

- **To research-advisory:** advice on the TP of AI-enabled transactions, AI-generated assets and DEMPE in AI value chains. This includes the Bloomberg Tax commentary on pricing AI-generated content (BTAX-ZERBE-2026), the OECD Chapter VII examples and AstraZeneca's request (OECD-INTRAGROUP-2026), the IBA report on AI as a new type of transaction (IBA-TAXAI-2025), the KPMG podcast series on value, IP and cost allocation (KPMG-TPPOD1-2026, KPMG-TPPOD-2026), the TPMinds West Coast session on AI value chains (TPMINDS-WC-2026), and the Oxford CBT question on delegation to AI and substantive TP law (OXFORD-CBT-2026).
- **To controversy (tax-authority AI):** authority-side AI in TP audit and risk assessment: the CIAT agent-based audit blog and working paper (CIAT-BLOG-2026, CIAT-WP06-2025), HMRC's ICTS proposal (KPMG-UK-ICTS-2025), IRS algorithms flagging distributor losses (TR-CHECKPOINT-2025, TR-CHECKPOINT-2026), and the PwC webcast on IRS AI-powered enforcement (TR-CHECKPOINT-2026).
- **To tax-data-technology:** the agentic AI and digital tax transparency framework proposed for royalty withholding reconciliation and TP master-file cross-validation, an op-ed by a Samsung Electronics tax manager (BTAX-LEE-2025), and the TPMinds 'Tax Transformation and Technology' panel with Deutsche Bank, AstraZeneca and Temenos speakers (TPMINDS-INTL-2026).
- **To international-pillar-two:** the TPMinds International session on operational implementation of Pillar Two, data and technology challenges (TPMINDS-INTL-2026, Pillar 2 Summit day).
- **Cross-cutting:** an op-ed arguing that AI cannot replace a tax professional's judgment and skepticism, not specific to TP (BTAX-ZERBE-2025).

---

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ABA-MAYMTG-2026 | ABA Section of Taxation May Tax Meeting 2026, final program (Transfer Pricing session 'AI and Transfer Pricing Under §482: Transforming Compliance and Risk Management') | ABA Section of Taxation | conference | https://sitepilot11.firmseek.com/client/chamberlain/www/media/event/657_ABA_Section_of_Taxation_2026_May_Meeting_Agenda.pdf | 2026-05-08 | full |
| PILLSBURY-ABA-2026 | AI and Transfer Pricing Under §482: Transforming Compliance and Risk Management (event listing) | Pillsbury Winthrop Shaw Pittman | firm | https://www.pillsburylaw.com/en/news-and-insights/ai-transfer-pricing-482-compliance-risk-management.html | 2026-05-08 | full |
| IRS-LBI-TP-2026 | Report on recent US international tax developments, 31 July 2026 (reports IRS LB&I remarks on AI in transfer pricing, 29 July 2026) | Ernst & Young LLP (EY Tax News & Developments) | firm | https://taxnews.ey.com/news/2026-1658-report-on-recent-us-international-tax-developments-31-july-2026 | 2026-07-31 | full |
| TR-CHECKPOINT-2026 | AI-powered IRS audits are here but taxpayers have new relief options, tax pros say (report on a 30 July 2026 PwC webcast) | Thomson Reuters Checkpoint News (Tim Shaw) | press | https://tax.thomsonreuters.com/news/ai-powered-irs-audits-are-here-but-taxpayers-have-new-relief-options-tax-pros-say/ | 2026-08-05 | full |
| TR-CHECKPOINT-2025 | Transfer Pricing Expert: 'Prepare Now' for Best Chance to Avoid Scrutiny (report on an Exactera webinar of 12 September 2025) | Thomson Reuters Checkpoint News (Tim Shaw) | press | https://tax.thomsonreuters.com/news/transfer-pricing-expert-prepare-now-for-best-chance-to-avoid-scrutiny/ | 2025-10-15 | full |
| DDTC-WUTA-2026 | Challenges in Transfer Pricing Benchmarking Changes in the AI Era (DDTC report from the WU-TA Advanced Transfer Pricing Programme 2026, Singapore, 28 Sep-1 Oct 2026) | DDTCNews (Audreyda Farahbella Anandivi) | press | https://news.ddtc.co.id/en/insight/1822922/challenges-in-transfer-pricing-benchmarking-changes-in-the-ai-era | 2026-10-01 | full |
| TPMINDS-INTL-2026 | TPMinds International 2026, Main Summit Day 1 agenda (16 June 2026, London) | Informa Connect | conference | https://informaconnect.com/tp-minds-international-conference/agenda/ | 2026-06-16 | full |
| TPMINDS-WC-2026 | TPMinds West Coast 2026, Day 1 and Day 2 agendas (4-5 November 2026, Palo Alto; programme published, event not yet held) | Informa Connect | conference | https://informaconnect.com/tp-minds-west-coast/agenda/ | 2026-11-04 | full |
| TPMINDS-AM-2026 | TPMinds Americas, 'Main Summit 2026 - Day 1 Agenda' (Fort Lauderdale; month not shown on the page) | Informa Connect | conference | https://informaconnect.com/tp-minds-americas-conference/agenda/ | 2026 | full |
| TPMINDS-AM-2027 | TPMinds Americas 2027 event page (AI Transformation Day 1 March 2027; planned session list) | Informa Connect | conference | https://informaconnect.com/tp-minds-americas-conference/ | 2027-03-01 | full |
| KPMG-TP-2025 | GenAI Revolutionizes Transfer Pricing and Valuation | KPMG US | firm | https://kpmg.com/us/en/articles/2025/genai-revolutionizes-transfer-pricing-valuation.html | 2025-04 | full |
| KPMG-TPPOD-2025 | How Can GenAI Improve Transfer Pricing Processes? (Exploring Transfer Pricing podcast) | KPMG US | podcast | https://kpmg.com/us/en/podcasts/2025/genai-tp.html | 2025-11-14 | full |
| KPMG-TPPOD1-2026 | Is Adoption of GenAI Redefining Value and Transfer Pricing? Part 1 (Exploring Transfer Pricing podcast) | KPMG US | podcast | https://kpmg.com/us/en/podcasts/2026/adoption-genai-redefining-value-transfer-pricing.html | 2026-06-01 | full |
| KPMG-TPPOD-2026 | Is Adoption of GenAI Redefining Value and Transfer Pricing? Part 2 (Exploring Transfer Pricing podcast) | KPMG US | podcast | https://kpmg.com/us/en/podcasts/2026/gen-ai-value-tp-pt2.html | 2026-07-15 | full |
| PLANTEMORAN-2026 | Using AI in transfer pricing: Practical opportunities and pitfalls for growing companies | Plante Moran (Lara Witte, Biz Pavelich, Kevin Lee) | firm | https://plantemoran.com/explore-our-thinking/insight/2026/08/using-ai-in-transfer-pricing | 2026-08-05 | full |
| EXACTERA-2025 | AI is transforming transfer pricing (sponsored advertising supplement, Q&A with Exactera COO Mimi Song) | Exactera in The Tax Adviser (AICPA) | vendor | https://www.thetaxadviser.com/issues/2025/sep/ai-is-transforming-transfer-pricing/ | 2025-08-31 | full |
| AIBIDIA-IBFD-2025 | Aibidia and IBFD Launch TP Aurora: A Groundbreaking AI Transfer Pricing Research Assistant | IBFD / Aibidia | vendor | https://www.ibfd.org/news/aibidia-and-ibfd-launch-tp-aurora-groundbreaking-ai-transfer-pricing-research-assistant | 2025-05-22 | full |
| AIBIDIA-WEBINAR-2026 | AI in Transfer Pricing: What's Working, What's Not, and What's Next (summary of the webinar 'From Hype to Help: Where AI Is Working in Transfer Pricing') | Aibidia | vendor | https://www.aibidia.com/blog/ai-in-transfer-pricing-whats-working-whats-not-and-whats-next | 2026-06 | full |
| AIBIDIA-TPMINDS-2026 | TPMinds International 2026: Five Strategic Shifts in Transfer Pricing | Aibidia | vendor | https://www.aibidia.com/blog/tpminds-international-2026-five-strategic-shifts-in-transfer-pricing | 2026-06 | full |
| AIBIDIA-STATETP-2026 | From information to intelligence: What senior TP leaders say must change (draws on the Aibidia Report: The State of Transfer Pricing 2026 and London and Helsinki briefings) | Aibidia | vendor | https://www.aibidia.com/blog/from-information-to-intelligence-what-senior-tp-leaders-say-must-change | 2026-09-23 | full |
| AIBIDIA-OTP-2026 | Connected, Controlled and Audit-ready: That's the Future of Operational Transfer Pricing (interview with Roshni D'Silva) | Aibidia | vendor | https://www.aibidia.com/blog/connected-controlled-and-audit-ready-thats-the-future-of-operational-transfer-pricing | 2026-07-03 | full |
| IBFD-ITPJ-2025 | Operationalizing Transfer Pricing with Generative Artificial Intelligence: Practical Applications and Challenges (D. Olzhabayeva, International Transfer Pricing Journal 32(6); abstract only) | IBFD | academic | https://shop.ibfd.org/journal/operationalizing-transfer-pricing-generative-artificial-intelligence-practical-applications | 2025-09-26 | full |
| IFA-LISBON-2025 | IBFD Dialogues seminar 'Unlocking the Potential of Generative AI for Tax Professionals', 77th IFA Congress (programme page) | IBFD | conference | https://www.ibfd.org/events/ibfd-dialogues-seminar-ifa-lisbon-2025-0 | 2025-10-06 | full |
| OXFORD-CBT-2026 | Oxford CBT Summer Conference 2026 booklet, Session 4 'Tax and Artificial Intelligence' | Oxford University Centre for Business Taxation | conference | https://oxfordtax.sbs.ox.ac.uk/sitefiles/cbt-summer-conference-booklet-2026 | 2026-06-26 | full |
| OECD-INTRAGROUP-2026 | Companies Want OECD to Clarify Character of AI Transactions (opening paragraphs only; paywalled after) | Bloomberg Tax Daily Tax Report | press | https://news.bgov.com/daily-tax-report/companies-want-oecd-to-clarify-character-of-ai-transactions | 2026-08-25 | full |
| PWC-DE-OECD-2026 | OECD: Public consultation on Transfer Pricing Guidelines (Chapter VII, intra-group services) | PwC Germany, Tax & Legal blog | firm | https://blogs.pwc.de/en/german-tax-and-legal-news/article/255082/oecd-public-consultation-on-transfer-pricing-guidelines/ | 2026-06-10 | full |
| CIAT-WP06-2025 | Study on Artificial Intelligence Applied to Transfer Pricing (Jairo A. Godoy G., Working Paper WP-06-2025) | CIAT (Inter-American Center of Tax Administrations) | regulator | https://www.ciat.org/Biblioteca/DocumentosdeTrabajo/2026/WP-06-2025.pdf | 2025-08 | full |
| CIAT-BLOG-2026 | Artificial Intelligence Agents in the control of Transfer Pricing (Pablo Porporatto, CIAT blog) | CIAT (Inter-American Center of Tax Administrations) | regulator | https://www.ciat.org/artificial-intelligence-agents-in-the-control-of-transfer-pricing/?lang=en | 2026-02-03 | full |
| KPMG-UK-ICTS-2025 | HMRC proposals to enable automated TP risk assessment at scale | KPMG UK | firm | https://kpmg.com/uk/en/insights/tax/tmd-hmrc-proposals-to-enable-automated-tp-risk-assessment-at-scale.html | 2025-04-30 | full |
| KPMG-TNF-2024 | AI May Take Transfer Pricing Up a Notch but Carries Some Risk (KPMG TaxNewsFlash reprint of a Bloomberg Tax commentary) | KPMG US | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/taxnewsflash/pdf/2024/10/ai-transfer-pricing-risk-oct21-2024.pdf | 2024-10-21 | full |
| BTAX-ZERBE-2026 | Here's How Businesses Can Handle AI Content and Transfer Pricing (Dean Zerbe, Alliant) | Bloomberg Tax (commentary) | press | https://news.bloombergtax.com/tax-insights-and-commentary/heres-how-businesses-can-handle-ai-content-and-transfer-pricing | 2026-01-13 | full |
| BTAX-LEE-2025 | US Must Lead Global AI-Driven Tax Transparency Standards Now (Jiseon Lee, Samsung Electronics) | Bloomberg Tax (commentary) | press | https://news.bloombergtax.com/tax-insights-and-commentary/us-must-lead-global-ai-driven-tax-transparency-standards-now | 2025-12-19 | full |
| BTAX-ZERBE-2025 | AI Will Never Replace a Human Tax Pro's Judgment and Skepticism (Dean Zerbe, Alliant) | Bloomberg Tax (commentary) | press | https://news.bloombergtax.com/tax-insights-and-commentary/ai-will-never-replace-a-human-tax-pros-judgment-and-skepticism | 2025-12-08 | full |
| IBA-TAXAI-2025 | Tax-AI-tion and the digital divide: how does artificial intelligence impact on tax practice? (report on a 19 Sep 2024 IBA Taxes Committee session) | International Bar Association | professional-body | https://www.ibanet.org/ai-impact-on-tax-practice | 2025-11-25 | full |
| REPTUNE-TPMWC-2026 | Reptune sponsor profile, TPMinds West Coast (event 4-5 Nov 2026; page publication date not shown) | Informa Connect / Reptune | vendor | https://informaconnect.com/tp-minds-west-coast/sponsors/reptune/ | 2026 | full |
| BTAX-KPMGQA-2024 | Q&A: How KPMG Is Using AI to Find Transfer Pricing Comparables (opening paragraphs only; paywalled after) | Bloomberg Tax | press | https://news.bloombergtax.com/payroll/q-a-how-kpmg-is-using-ai-to-find-transfer-pricing-comparables | 2024-02-28 | full |
| ITR-BRAUN-2025 | Reflections on the ITR AI in Tax Forum 2025 (Michel Braun, WTS Digital; standfirst only, paywalled) | International Tax Review | press | https://www.internationaltaxreview.com/article/2fms48aicg0sntt6c6dxc/direct-tax/reflections-on-the-itr-ai-in-tax-forum-2025 | 2025-11-26 | full |
| ABA-TAXTIMES-2026 | Tax Times committee report 'Transforming Compliance Risk Management' on the 8 May 2026 AI and TP panel (page blocked to curl; search extract only) | ABA Section of Taxation | professional-body | https://www.americanbar.org/groups/taxation/resources/tax-times/2026/transforming-compliance-risk-management/ | 2026 | search-only |
| KPMG-DE-2025 | Transfer pricing: Why GenAI will significantly simplify the creation of master files and local files in future (page now returns 404; search extract only) | KPMG Germany | firm | https://kpmg.com/de/en/home/insights/2025/01/unlocking-the-future-of-transfer-pricing.html | 2025-01 | search-only |
| BDO-CA-2026 | AI governance in transfer pricing: how to create defensible documentation (page blocked to curl; search extract only) | BDO Canada | firm | https://www.bdo.ca/insights/ai-governance-in-transfer-pricing-how-to-create-defensible-documentation | 2026-08 | search-only |

Date notes: ABA-MAYMTG-2026, TPMINDS-INTL-2026 and TPMINDS-WC-2026 are dated to the event or session day because the programme documents carry no publication date. TPMINDS-AM-2026 is dated by year only; the page shows the 2026 agenda but not the month, and a search extract placed it in February 2026 in Fort Lauderdale. TPMINDS-AM-2027 is dated to the event start. REPTUNE-TPMWC-2026 is dated by year only because the sponsor page shows no date. The AIBIDIA-WEBINAR-2026 and AIBIDIA-TPMINDS-2026 pages show different dates in the page body and the structured data (June 2026 in both cases), so month precision is used. EXACTERA-2025 is the byline date; the printed issue is September 2025.

---

## 6. Gaps

- **No independent quality evidence.** No error rate, override rate, parallel run, regulator inspection finding or independent benchmark for AI in TP was found. All figures are speaker claims or vendor survey data.
- **No community discussion reached.** Reddit, LinkedIn and preparer forums were not reachable and the one search aimed at them returned vendor pages. Practitioner chatter on AI-made fabricated comparables is therefore not covered.
- **Session content is thinly reported.** TPMinds, ABA and Oxford entries are agenda text. The ABA Tax Times recap and BDO Canada piece were blocked to curl (search extracts only). TPMinds West Coast has not been held (programme only). The ITR AI in Tax Forum 2025 reflections and the Bloomberg Tax KPMG comparables Q&A were paywalled after the opening paragraphs.
- **Primary OECD documents not reached.** The OECD site was blocked, so the Chapter VII discussion draft, its AI-related examples and the public comments (including AstraZeneca's) were read only through Bloomberg's opening paragraph and firm notes.
- **Aibidia's full 2026 report was not read.** Only blog summaries were available. Respondent counts differ across Aibidia pages (97 for the 2026 survey; 140+ for the earlier edition), and neither sampling method nor response rate is given.
- **Excluded for lack of a date or AI link:** an Aibidia customer case study on documentation time (https://www.aibidia.com/case-studies/how-trivium-packaging-cut-tp-documentation-time-by-80-percent-with-aibidia; no publication date, and the result is attributed to the documentation platform, not specifically to AI) and the Moody's TP Catalyst product page (no date).
- **KPMG Germany's January 2025 article now returns 404,** so only the search extract exists.
- **Searches not run because the shared budget was spent:** APA and MAP practice with AI, IRS APMA statements, Thomson Reuters ONESOURCE TP and other product updates, Big Four TP-specific AI announcements other than KPMG, and in-house case studies from named TP teams (Inter IKEA, WPP, ADM, Uber, OpenAI and Anthropic appear as scheduled TPMinds speakers; their content is not yet public).
- **Not covered here:** vendor deployments with named customers and product documentation (practice angle), and regulator and standard-setter evidence (governance angle).

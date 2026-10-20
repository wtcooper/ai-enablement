# Advisory / transactions: AI in transaction advisory (QoE, due diligence, deal support, integration)

Run date: 2026-10-20. Wave 5. Archetype `advisory`, module `transactions`, angle `combined` (practice, discourse, governance and evidence).

Conventions: refs follow `PUBLISHER-SHORT-YYYY` and reuse the landscape refs where the same document appears (`FORVIS-QOE-2026`). `access: full` means the page was opened and read in this run (directly, or through the r.jina.ai mirror). `access: search-only` means seen only in search results. Vendor pages with no publication date carry the access date 2026-10-20 and say so. Quotations are under 25 words. Figures are self-reported or vendor-published unless marked independent.

---

## 1. Summary

**Public evidence on AI in transaction advisory is thin, and almost all of it is firm or vendor self-description.** There is no A-grade use case in this pass. I found no published error rate, override rate, parallel-run result, inspection finding or independent accuracy measurement for AI-assisted quality of earnings (QoE) or financial due diligence. The only measured accuracy figure close to this work (74% to 95% accuracy on commercial-contract review) comes from a law firm's own legal due diligence tests, which is adjacent, so it caps at B.

**What the evidence does show:**

1. **Named deployments appeared in the last five months, mostly at the large-firm end.** Forvis Mazars Group announced a multi-country rollout of Opio's due diligence platform on 2026-09-25 after a nine-month pilot (FORVISGROUP-OPIO-2026). Deloitte unveiled an M&A Platform on 2026-09-22 and says it is in use across more than 1,000 client engagements (DELOITTE-MAPLATFORM-2026). PwC and ToltIQ announced an exclusive relationship on 2026-06-15, with usage counts of 4,000+ PwC Deals practitioners and 5,000+ deals (PWC-TOLTIQ-2026). None publishes an outcome measure.
2. **Mid-market evidence comes mainly from AI-native providers.** QoEAgent, Shepi and Audit Sight sell proof-of-cash, first-pass QoE and flux analysis. Only a handful of named customers appear (Miller Cooper Ltd. for Audit Sight; one searcher for QoEAgent). Their speed claims (27%, 80%, 24 hours) are vendor-published with no method.
3. **Practitioners split the work into a mechanical half and a judgment half.** AI is credited with data collection, trial balance mapping, proof of cash, first-draft schedules and document review. Add-backs, adjustments and footnotes are where practitioners say it degrades (WORKWISE-QOE-2026; SEARCHFUNDER-SOURCETABLE-2025). Forvis Mazars US warns that over-reliance yields thin, unsupported reports and depletes the junior pipeline (FORVIS-QOE-2026).
4. **Governance is being set by contracts, insurers and a lender rule more than by standard-setters.** M&A lawyers report seller NDAs that restrict AI tools or require consent (KJK-NDA-2026). Counsel expect R&W insurers to scrutinise and possibly exclude target-AI risk (FASKEN-RWI-2026). SBA SOP 50 10 8.1 took effect 2026-10-01; per vendor summaries it requires an independent QoE on 7(a) acquisitions of $3 million or more (SBA-SOP5010-2026; QOEAGENT-SBAUPDATE-2026). The AICPA consulting standard (CS 100) applies its general standards of competence, due care, planning and supervision, and sufficient relevant data to consulting work (JOFA-CS100-2024).
5. **Surveys say adoption is broad and uneven.** In S&P Global's GP survey, due diligence had the highest AI integration at 31% somewhat or fully integrated (SPGLOBAL-PE-2026). Datasite and SS&C Intralinks report about 50% regular or fully integrated use, with 21-30% self-reported time savings in diligence from the Intralinks survey. These are vendor-commissioned surveys of dealmakers generally, not TAS-specific, and their definitions differ.

**Two things to carry into interviews.** First, the open question is evidence of quality, not speed: nobody public reports how often a reviewer changes an AI-proposed adjustment. Second, buyers' own in-house first-pass diligence and AI-native QoE tiers are the competitive pressure; Forvis Mazars US says AI is also raising the number of cheaper, thinner QoE products (FORVIS-QOE-2026).

**Source type coverage (46 distinct sources; 45 opened, 1 search-only):** firm 11, vendor 10, press 8, survey 6, community 3, academic 2, professional body 2, job posting 2, regulator 1, conference 1. No podcast, no standard-setter text, no inspection finding and no independent practitioner survey specific to transaction advisory were found.

---

## 2. Use cases

```yaml
- id: advisory-transactions-01
  title: "Financial due diligence workbench: data ingestion, trial balance mapping and first-draft databook"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [transaction-processing, data-reporting]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Financial due diligence starts with collecting, checking and adjusting data before anyone can interpret it, and a large share of junior time goes there (Opio CEO, as reported by Tech.eu). Forvis Mazars US adds that teams can still be held up by target companies that struggle to pull requested data."
  solution: "An AI platform built for transaction services teams reads large volumes of unstructured deal information, structures the data and drafts first-pass outputs. Forvis Mazars US describes AI helping with trial balance mapping, first versions of schedules, trend and anomaly spotting, missing-data checks, reconciliations and tailored questions for management. Forvis Mazars Group says its rollout uses embedded controls, full traceability and mandatory human review."
  outcomes:
    - lever: speed
      description: "Opio reports average time saved per financial due diligence (FDD) engagement"
      figure: "27%"
      measures: "Opio product page: 'Average time saved per FDD'. Tech.eu words it as saving transaction services professionals 27 per cent of their time. Method, sample and baseline not published."
      provenance: vendor-published
      source_ref: OPIO-SITE-2026
    - lever: quality
      description: "Forvis Mazars Group says that after testing, the solution improved the quality and depth of its due diligence and let teams analyse a broader range of information"
      figure: "none published"
      measures: "Qualitative statement by the Group's Financial Advisory Innovation leader in the rollout release; no metric given"
      provenance: self-reported
      source_ref: FORVISGROUP-OPIO-2026
  prerequisites:
    - "A pilot with transaction services professionals and the group AI team (the release describes a nine-month pilot before rollout)"
    - "A deployment that fits confidentiality rules; the release says the platform operates exclusively on premise and does not train on data"
    - "Engagement data in structured form (trial balance, databook) for the platform to work from"
  risks_and_guardrails:
    - "The release says outputs are fully auditable and every figure traceable to its source document (FORVISGROUP-OPIO-2026)"
    - "Forvis Mazars US warns that firms relying too heavily on automation can produce thin, unsupported conclusions (FORVIS-QOE-2026)"
    - "Opio's compliance and certification claims (SOC 2 Type II, ISO 27001, GDPR, AI Act) are vendor statements (OPIO-SITE-2026)"
  human_checkpoints:
    - "Mandatory human review of platform outputs (FORVISGROUP-OPIO-2026)"
    - "Professionals own the judgment calls between dataroom and report (OPIO-SITE-2026)"
  role_evolution: "Opio's CEO says automating data collection and checking lets junior professionals spend time earlier on analysis, judgement and client relationships (TECHEU-OPIO-2026). Forvis Mazars US warns that cutting junior ranks will leave gaps in senior insight later (FORVIS-QOE-2026)."
  evidence_grade: B
  sources:
    - { ref: FORVISGROUP-OPIO-2026, title: "Forvis Mazars scales AI-powered transaction advisory solution", publisher: "Forvis Mazars Group", type: firm, url: "https://www.forvismazars.com/group/en/who-we-are/news-publications/latest-news/scaling-ai-powered-transaction-advisory-solutions", date: "2026-09-25", access: full, locator: "paragraphs 1-5 (rollout, nine-month pilot, mandatory human review); quotes from G. Volpi and T. Fulchiron; 'Responsible AI' paragraph" }
    - { ref: OPIO-SITE-2026, title: "Frontier AI for transaction services (product page)", publisher: "Opio", type: vendor, url: "https://www.opio.fi", date: "2026-10-20", access: full, locator: "statistics block (27% average time saved per FDD; 15 countries; 1M+ documents); security section. Page is undated; date is access date" }
    - { ref: TECHEU-OPIO-2026, title: "Opio raises EUR 4M to automate the grunt work of financial due diligence", publisher: "Tech.eu", type: press, url: "https://tech.eu/2026/09/16/opio-raises-eur4m-to-automate-the-grunt-work-of-financial-due-diligence/", date: "2026-09-16", access: full, locator: "paragraphs 3-6 (27% claim, Forvis Mazars Group and BDO named as customers, 15 countries)" }
    - { ref: FORVIS-QOE-2026, title: "Quality of Earnings & Due Diligence in an AI World", publisher: "Forvis Mazars US (Transaction Advisory)", type: firm, url: "https://www.forvismazars.us/forsights/2026/09/quality-of-earnings-due-diligence-in-an-ai-world", date: "2026-09-08", access: full, locator: "sections '1. Speed' and '3. Talent'" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: Forvis Mazars Group is an international network (not Big Four); the BDO customer claim comes only from Tech.eu. Opio is an AI-native provider founded in Paris in 2025 (Tech.eu). The group release does not say whether the US member firm uses the platform. The release gives no timing or error figure. Opio's own claim of 'ten countries' of live use appears only in the CEO quote in the release. Independence: not researched beyond the Deloitte footnote in use case 11; buy-side diligence on a third-party target is the usual setting."

- id: advisory-transactions-02
  title: "Transaction-level anomaly scoring and flux analysis to prepare management meetings and EBITDA adjustment candidates"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Preparing for the first management meeting has been a bottleneck: teams eyeball trial balances and comb thousands of rows to find movements worth asking about (Miller Cooper principal and vendor release)."
  solution: "A module scores each transaction for anomaly risk (Audit Sight's FARS model), flags material balances and movements against materiality and standard-deviation thresholds the user sets, tracks candidate EBITDA adjustments to raise with management, and calculates profitability and efficiency ratios to focus the interview questions."
  outcomes:
    - lever: speed
      description: "Audit Sight says the module eliminates prep time for the management-meeting step"
      figure: "80%"
      measures: "Vendor claim: share of QoE professionals' prep time eliminated for the initial management meeting. Basis not published."
      provenance: vendor-published
      source_ref: CPAPA-AUDITSIGHT-2025
    - lever: speed
      description: "A principal at Miller Cooper Ltd., a named Audit Sight customer, says the tool shaved days off the deal cycle"
      figure: "none published (days, unquantified)"
      measures: "Customer's recollection quoted in the vendor release; no tracked metric"
      provenance: self-reported
      source_ref: CPAPA-AUDITSIGHT-2025
  prerequisites:
    - "Trial balance or ledger data for the deal period"
    - "Team-set materiality and standard-deviation thresholds"
  risks_and_guardrails:
    - "Flagged movements are candidates to discuss with management, not conclusions (CPAPA-AUDITSIGHT-2025)"
    - "Practitioners say first-pass automation weakens once normalization and judgment matter (SEARCHFUNDER-SOURCETABLE-2025)"
  human_checkpoints:
    - "QoE team decides which flagged movements become adjustments and what to ask management (CPAPA-AUDITSIGHT-2025)"
  role_evolution: "The vendor says the tool lets transaction advisory professionals ask better questions and spend less time on manual data review (CPAPA-AUDITSIGHT-2025)."
  evidence_grade: B
  sources:
    - { ref: CPAPA-AUDITSIGHT-2025, title: "Audit Sight Launches Management Meeting Module for Transaction Advisory Teams to Accelerate Deal Cycles and Surface Key Insights", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2025/07/10/audit-sight-launches-management-meeting-module-for-transaction-advisory-teams-to-accelerate-deal-cycles-and-surface-key-insights/164674/", date: "2025-07-10", access: full, locator: "intro paragraph; 'Designed for Transaction Advisory Professionals'; FARS paragraph; Todd Wrenn (Miller Cooper) quote under 'Built to Accelerate Deal Execution'" }
    - { ref: SEARCHFUNDER-SOURCETABLE-2025, title: "Has anyone used Sourcetable AI for QoE Analysis?", publisher: "Searchfunder (community thread)", type: community, url: "https://searchfunder.com/post/has-anyone-used-sourcetable-ai-for-qoe-analysis", date: "2025-10", access: full, locator: "reply from a professional (9 months old on the page); date approximate from relative timestamps" }
  last_reviewed: "2026-10-20"
  notes: "Vendor: Audit Sight. Miller Cooper Ltd. is a named accounting firm customer; its size and ranking were not verified. The release is 15 months old. Pricing and other customers not found."

- id: advisory-transactions-03
  title: "Proof of cash and bank-to-ledger reconciliation by AI agents for lower-middle-market QoE"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [transaction-processing, review-assurance]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "In lower-middle-market deals the seller's books are often thin: scanned bank statements, several accounts, a system migration or a CPA who posts accruals once a year. Reconciling several years of bank activity to the ledger by hand takes weeks (QoEAgent)."
  solution: "AI agents read bank statements, including scanned PDFs, tie revenue and expenses to the bank, map the trial balance to GAAP-format financials, and pass flagged items to CPAs and M&A advisors who review them and deliver a sourced databook. QoEAgent sells this as a proof of cash within 24 hours, a 48-hour first look, and a full QoE."
  outcomes:
    - lever: speed
      description: "QoEAgent says a proof of cash is reconciled within a stated tolerance within a stated time of receiving data"
      figure: "within 1% in 24 hours"
      measures: "Vendor claim: revenue and expenses tied to bank statements to within 1%, within 24 hours of receiving the data. Not independently measured."
      provenance: vendor-published
      source_ref: QOEAGENT-HOME-2026
    - lever: risk
      description: "In one described engagement, the proof of cash rebuilt monthly cash-basis statements and found year-end 2024 revenue and cost-of-sales deferrals documented by the seller's CPA but never recorded in the general ledger; the verified numbers did not support the price and the buyer walked away before closing"
      figure: "46 months rebuilt (January 2022 to October 2025); 1 engagement"
      measures: "A single QoEAgent engagement published with the client's written permission; target and seller unnamed"
      provenance: vendor-published
      source_ref: QOEAGENT-CASE-2026
  prerequisites:
    - "Bank statements for every account (scanned PDFs accepted), the general ledger and trial balance; prior-year tax returns for a lender QoE (QOEAGENT-HOME-2026)"
    - "Seller cooperation on a defined list of items, held through weekly diligence calls (QOEAGENT-CASE-2026)"
  risks_and_guardrails:
    - "A QoEAgent post tells buyers to ask any AI diligence tool vendor for its exception rate, its training data and what the human review step looks like (SEARCHFUNDER-QOEAGENT-2026)"
    - "The case study is one engagement written by the vendor (QOEAGENT-CASE-2026)"
  human_checkpoints:
    - "Credentialed professionals own every conclusion; software does extraction and matching (QOEAGENT-CASE-2026)"
    - "CPAs and M&A advisors review every flagged item (QOEAGENT-HOME-2026)"
  role_evolution: "QoEAgent's own account is that the platform does the heavy lifting and credentialed people do the judgment (QOEAGENT-HOME-2026). The founding team combines M&A advisory, valuation and an AI researcher (QOEAGENT-HOME-2026)."
  evidence_grade: B
  sources:
    - { ref: QOEAGENT-HOME-2026, title: "QoEAgent: AI quality of earnings, proof of cash and SBA lender QoE (home page)", publisher: "QoEAgent", type: vendor, url: "https://qoeagent.ai/", date: "2026-10-20", access: full, locator: "hero section; 'How AI quality of earnings works' steps 01-04; FAQ. Page is undated; date is access date" }
    - { ref: QOEAGENT-CASE-2026, title: "Proof of Cash Case Study: An SBA Acquisition the Numbers Did Not Support", publisher: "QoEAgent", type: vendor, url: "https://qoeagent.ai/proof-of-cash-case-study-sba-acquisition/", date: "2026-10-15", access: full, locator: "opening summary; 'The problem'; 'What we did'; 'What we found'; 'The outcome'" }
    - { ref: SEARCHFUNDER-QOEAGENT-2026, title: "QoEAgent AI: AI Proof of Cash and Quality of Earnings for LMM Diligence", publisher: "Searchfunder (vendor-authored post)", type: community, url: "https://searchfunder.com/post/qoeagent-ai-ai-proof-of-cash-quality-of-earnings-for-lmm-diligence", date: "2026-08", access: full, locator: "post body, three questions to ask before trusting any AI diligence tool; date approximate from '2mos ago'" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: AI-native provider (Denver, founded 2023 per its site). Grade B rests on one named client engagement with no tracked metric; the client quote and outcome are published by the vendor. The engagement was completed before the SBA technical update effective 2026-10-01 (per the case page). No independent review of QoEAgent was found."

- id: advisory-transactions-04
  title: "AI-suggested EBITDA adjustment candidates with source-linked evidence for reviewer sign-off"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [expert-judgment, data-reporting]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "The adjustments from reported to normalized EBITDA decide the price, and the work of finding, supporting and tracing them is slow and hard to audit in spreadsheets (Shepi). Forvis Mazars US notes that a single identified adjustment can be worth many times the fee."
  solution: "A platform surfaces adjustment candidates, links each to supporting records where source evidence is available, shows gaps, and lets a person approve or reject each one before a PDF and Excel package is produced. Shepi's demo shows a normalized EBITDA bridge with 'adjustments reviewed 12 / 14' and source coverage percentages."
  outcomes:
    - lever: quality
      description: "Vendor says every conclusion is linked to source evidence and reviewers can follow a number back to its origin"
      figure: "none published"
      measures: "Product description and a demo mock-up on the vendor page; the on-page percentages (source coverage 96%, GL reconciliation 93%) are illustrative demo values, not results"
      provenance: vendor-published
      source_ref: SHEPI-HOME-2026
  prerequisites:
    - "Connected accounting data or uploaded trial balance, ledger, bank statements and supporting files"
  risks_and_guardrails:
    - "Shepi states the platform surfaces candidates and people decide which adjustments belong; neither path is an audit, review, attestation, valuation or fairness opinion (SHEPI-HOME-2026)"
    - "A practitioner buyer's guide says extraction is accurate on clean top-line numbers and degrades on add-backs, adjustments and footnotes, so a qualified analyst still owns the number (WORKWISE-QOE-2026). This is an opinion, not a measurement."
    - "Intralinks reports that 80% of surveyed dealmakers had AI-related security or accuracy incidents or near-misses in the past 12 months, with hallucinated outputs leading to inaccurate diligence among the clusters (INTRALINKS-AIDEAL-2026). The release does not state the denominator for the cluster percentages."
  human_checkpoints:
    - "User reviews and approves each adjustment (SHEPI-HOME-2026, Self-Service tier)"
    - "Licensed CPA reviews adjustments before delivery in the Done-For-You tier (SHEPI-HOME-2026)"
  role_evolution: "Shepi pitches the tool to searchers, brokers, accountants and lenders; for accountants it is positioned as extra capacity with traceable workpapers (SHEPI-HOME-2026)."
  evidence_grade: C
  sources:
    - { ref: SHEPI-HOME-2026, title: "Shepi: AI Quality of Earnings Software for SMB M&A", publisher: "Shepi", type: vendor, url: "https://www.shepi.ai", date: "2026-10-20", access: full, locator: "hero section; 'Built around the deal'; pricing tiers; 'Why Shepi'. Page is undated; date is access date" }
    - { ref: WORKWISE-QOE-2026, title: "The Best AI Tools for Quality of Earnings and Financial Due Diligence in 2026", publisher: "WorkWise Solutions (AI consulting firm)", type: vendor, url: "https://workwisesolutions.org/guides/best-ai-qoe-financial-due-diligence-tools.html", date: "2026-07-20", access: full, locator: "TLDR; section 1 'What a Quality of Earnings Analysis Is, and Where AI Fits'" }
    - { ref: INTRALINKS-AIDEAL-2026, title: "AI Use Permeates Dealmaking Despite Operational Concerns: SS&C Intralinks Report", publisher: "SS&C Intralinks (via Business Wire / Nasdaq)", type: survey, url: "https://www.nasdaq.com/press-release/ai-use-permeates-dealmaking-despite-operational-concerns-ssc-intralinks-report-2026", date: "2026-04-08", access: full, locator: "key findings list, incident bullet" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: vendor (AI-native). Grade C: product claims only; no named customer, no measured outcome. A Capterra listing seen in search showed $2,000 per project against $1,000 on the vendor page now, so pricing has moved or sources conflict (search-only, not used as an outcome). No user ratings found. The WorkWise guide is a consultancy opinion piece that says it takes no referral fees."

- id: advisory-transactions-05
  title: "AI-native QoE service tiers (QoE first look, self-service with CPA review) priced below a traditional engagement"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [document-production, transaction-processing]
  pattern: draft-review-loop
  ladder: augment
  change_scope: model
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Small and lower-middle-market buyers (searchers, independent sponsors) must choose between an expensive traditional engagement and fragile spreadsheet work (Shepi). One searcher reply puts QoE costs anywhere from $500 to $25,000 or more depending on size, industry and scope (SearchFunder)."
  solution: "AI-native providers sell a tiered, scoped product: QoEAgent's Flash Cash Review, Proof-of-Cash Plus in 48 hours, QoE Essentials and a lender QoE at fixed fees quoted up front; Shepi's Self-Service at $1,000 per project or Done-For-You with licensed CPA review. A Columbia team posted that its custom model cuts production cost 'significantly' even with an accountant verifying."
  outcomes:
    - lever: cost
      description: "Shepi lists a flat price for self-service QoE software"
      figure: "$1,000 per project (Self-Service)"
      measures: "List price on the vendor page read 2026-10-20; excludes the Done-For-You tier. Not a measured saving."
      provenance: vendor-published
      source_ref: SHEPI-HOME-2026
    - lever: cost
      description: "A Columbia team says production cost is significantly lower with an accountant in the loop"
      figure: "none published"
      measures: "Claim in a community post seeking feedback; no cost figure given"
      provenance: self-reported
      source_ref: SEARCHFUNDER-COLUMBIA-2026
  prerequisites:
    - "Buyer or lender willing to accept a software-assisted, non-attest analysis"
  risks_and_guardrails:
    - "Shepi says lenders may require independent CPA involvement and that neither path is an audit, review, attestation or valuation (SHEPI-HOME-2026)"
    - "A lender-side searcher reply says banks favour providers that help buyer and lender get comfortable with a reconciliation or normalization, and criticised report-only providers (SEARCHFUNDER-COLUMBIA-2026)"
    - "QoEAgent's reading of the SBA rule is that software cannot be the provider and an independent financial professional must stand behind the conclusions (QOEAGENT-WHO-2026). This is a vendor interpretation."
  human_checkpoints:
    - "Licensed CPA reviews adjustments (Shepi Done-For-You); credentialed professionals own conclusions (QoEAgent)"
  role_evolution: "Not stated by the sources beyond the human-review models above."
  evidence_grade: C
  sources:
    - { ref: SHEPI-HOME-2026, title: "Shepi: AI Quality of Earnings Software for SMB M&A", publisher: "Shepi", type: vendor, url: "https://www.shepi.ai", date: "2026-10-20", access: full, locator: "'Choose the right level of support' (Self-Service and Done-For-You); scope disclaimer" }
    - { ref: QOEAGENT-HOME-2026, title: "QoEAgent: AI quality of earnings, proof of cash and SBA lender QoE (home page)", publisher: "QoEAgent", type: vendor, url: "https://qoeagent.ai/", date: "2026-10-20", access: full, locator: "'Four products, one continuum' section" }
    - { ref: SEARCHFUNDER-COLUMBIA-2026, title: "Columbia Team working on Cheaper Quality of Earnings Reports", publisher: "Searchfunder (community thread)", type: community, url: "https://www.searchfunder.com/post/columbia-team-working-on-cheaper-quality-of-earnings-reports", date: "2026-06", access: full, locator: "original post and the two visible replies; date approximate from '4mos ago'" }
    - { ref: QOEAGENT-WHO-2026, title: "Who Can Prepare an SBA Quality of Earnings Report", publisher: "QoEAgent", type: vendor, url: "https://qoeagent.ai/who-can-prepare-sba-quality-of-earnings/", date: "2026-09-05", access: full, locator: "opening summary and arrangements table" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: AI-native providers. The 12 comments on the Columbia thread and 8 on the Sourcetable thread are mostly behind login; only the visible replies were read. Pricing here is the vendor's list price, not a firm's fee data; firm pricing of the firm's own work is routed to professional-services."

- id: advisory-transactions-06
  title: "Sub-contracted or white-labelled AI QoE capacity for TAS and CPA firms"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [transaction-processing, document-production]
  pattern: bulk-transformation
  ladder: augment
  change_scope: model
  runtime_class: workflow-automation
  maturity: announced
  problem: "Transaction advisory and CPA firms need capacity for proof-of-cash and trial-balance work during busy periods without adding headcount (QoEAgent; Shepi)."
  solution: "QoEAgent says it white-labels or supports parts of engagements for transaction advisory and CPA firms, from proof of cash and trial balance mapping through the databook. Shepi pitches accountants and CPAs on extra capacity through structured workpapers and repeatable analysis."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "Positioning statements on vendor pages; no named firm customer or result found"
      provenance: vendor-published
      source_ref: QOEAGENT-HOME-2026
  prerequisites:
    - "Firm engagement terms that allow a sub-contractor or software to handle client financial data"
  risks_and_guardrails:
    - "Seller NDAs may restrict who and what may handle diligence material (KJK-NDA-2026)"
  human_checkpoints:
    - "Not described beyond the vendors' own review steps"
  role_evolution: "Not stated by the sources."
  evidence_grade: C
  sources:
    - { ref: QOEAGENT-HOME-2026, title: "QoEAgent: AI quality of earnings, proof of cash and SBA lender QoE (home page)", publisher: "QoEAgent", type: vendor, url: "https://qoeagent.ai/", date: "2026-10-20", access: full, locator: "'Who we serve' (TAS and CPA firms); FAQ 'Do you work with transaction advisory and CPA firms?'" }
    - { ref: SHEPI-HOME-2026, title: "Shepi: AI Quality of Earnings Software for SMB M&A", publisher: "Shepi", type: vendor, url: "https://www.shepi.ai", date: "2026-10-20", access: full, locator: "'Built around the deal' (Accountants and CPAs)" }
    - { ref: KJK-NDA-2026, title: "AI and M&A NDAs: Managing Artificial Intelligence Risks in Confidentiality Agreements", publisher: "Kohrman Jackson & Krantz", type: firm, url: "https://kjk.com/2026/03/12/ai-and-ma-ndas-managing-artificial-intelligence-risks-in-confidentiality-agreements/", date: "2026-03-12", access: full, locator: "'Why AI Use in M&A Due Diligence Raises NDA Concerns'" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: AI-native providers selling to accounting firms. No accounting firm was found publicly naming either vendor as a sub-contractor. Marked announced because only vendor positioning was found."

- id: advisory-transactions-07
  title: "AI-assisted lender QoE for SBA 7(a) change-of-ownership loans"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "SBA SOP 50 10 8.1, effective 2026-10-01, makes an independent QoE with a cash proof a condition on larger 7(a) acquisitions, and the lender must use the QoE earnings in the debt service calculation (SBA-SOP5010-2026; QOEAGENT-SBAREQ-2026). Lenders and buyers need many such reports quickly."
  solution: "QoEAgent offers an SBA Lender QoE built to the SOP: a cash proof for the trailing twelve months and two prior fiscal years, GAAP-format financials, adjusted EBITDA schedules, a book-to-tax reconciliation, and working capital and customer analysis, delivered through a lender portal."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "Vendor says the rule adds weeks to credit processes; no turnaround data for the lender product"
      provenance: vendor-published
      source_ref: QOEAGENT-SBAREQ-2026
  prerequisites:
    - "Independent, experienced financial professional engaged for the benefit of the lender (per the SOP clause as quoted by QoEAgent)"
    - "Bank statements, ledger and trial balance, and prior-year tax returns (QOEAGENT-HOME-2026)"
  risks_and_guardrails:
    - "Per QoEAgent's reading, the seller-prepared report is barred outright. A buyer-commissioned report is allowed only if one of the lender's own vendors reviews it and the review findings are kept in the loan file (QOEAGENT-SBAUPDATE-2026)"
    - "The SBA page confirms version 8.1 with technical updates effective 2026-10-01; the SOP's QoE clause text was read only through vendor pages because the SBA document download returned an error (SBA-SOP5010-2026)"
    - "The $3 million threshold and the Owner Buyout and ESOP exemptions are as stated by QoEAgent; not verified against the SBA text (QOEAGENT-SBAUPDATE-2026)"
  human_checkpoints:
    - "A named professional stands behind the conclusions; lender vendor review where a buyer-commissioned report is used (QOEAGENT-SBAUPDATE-2026)"
  role_evolution: "Not stated by the sources."
  evidence_grade: C
  sources:
    - { ref: SBA-SOP5010-2026, title: "Lender and Development Company Loan Programs (SOP 50 10)", publisher: "U.S. Small Business Administration", type: regulator, url: "https://www.sba.gov/document/sop-50-10-lender-development-company-loan-programs", date: "2026-10-01", access: full, locator: "document header: 'Effective: October 1, 2026'; 'Version 8.1 with Technical Updates'. Date is the effective date; publication date not shown. QoE clause not on this page" }
    - { ref: QOEAGENT-SBAUPDATE-2026, title: "The September 25 Update: A Buyer's QoE Can Now Reach the Lender", publisher: "QoEAgent", type: vendor, url: "https://qoeagent.ai/sba-qoe-september-25-update/", date: "2026-10-01", access: full, locator: "'What the clause said, and what it says now'; 'The vendor review is the condition'; 'What did not change'" }
    - { ref: QOEAGENT-SBAREQ-2026, title: "SBA Quality of Earnings: What the 2026 Rule Requires", publisher: "QoEAgent", type: vendor, url: "https://qoeagent.ai/sba-quality-of-earnings-requirement/", date: "2026-09-01", access: full, locator: "opening 'Short answer'; 'The earnings number is no longer the seller's number'" }
    - { ref: QOEAGENT-HOME-2026, title: "QoEAgent: AI quality of earnings, proof of cash and SBA lender QoE (home page)", publisher: "QoEAgent", type: vendor, url: "https://qoeagent.ai/", date: "2026-10-20", access: full, locator: "'SBA Lender QoE' section" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: AI-native provider. This is a regulatory demand driver for QoE in the lower middle market, with AI as the delivery method claimed by one vendor. Independence: the SBA clause is about the lender's reliance on the report, not auditor independence. The valuation clause (no valuation prepared for the applicant or seller) is routed to valuation."

- id: advisory-transactions-08
  title: "AI-assisted sell-side QoE and pre-sale diligence readiness"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Sellers who wait for the buyer's diligence meet findings late, in the middle of a process, which can trigger price adjustments (Pease Bell)."
  solution: "Run AI-driven pre-sale diligence and a sell-side QoE with proof of cash before going to market, so issues are found and addressed early. Pease Bell describes this for sellers; QoEAgent lists sell-side advisors as a customer group."
  outcomes:
    - lever: risk
      description: "Pease Bell says pre-sale AI diligence reduces the likelihood of purchase price adjustments and speeds the path to closing"
      figure: "none published"
      measures: "General claim in a firm article; no data or engagement cited"
      provenance: self-reported
      source_ref: PEASEBELL-2026
  prerequisites:
    - "Seller willingness to open books to a pre-sale review"
  risks_and_guardrails:
    - "Per QoEAgent's summary of the SBA rule, a seller-prepared report cannot be used by the lender (QOEAGENT-SBAUPDATE-2026)"
  human_checkpoints:
    - "Not described"
  role_evolution: "Pease Bell says many entry-level TAS tasks (aggregation, reconciliation, schedule preparation, initial analysis) can be handled by AI with minimal oversight and that early-career staff must interpret outputs with professional skepticism (PEASEBELL-2026). It gives no staffing data."
  evidence_grade: C
  sources:
    - { ref: PEASEBELL-2026, title: "AI in Transaction Advisory", publisher: "Pease Bell CPAs", type: firm, url: "https://www.peasebell.com/insights/artificial-intelligence-in-transaction-advisory/", date: "2026-02-27", access: full, locator: "sections 'How AI Accelerates Due Diligence' (sell-side paragraph) and 'What AI Means for Transaction Advisory Staffing'. Read through the r.jina.ai mirror" }
    - { ref: QOEAGENT-HOME-2026, title: "QoEAgent: AI quality of earnings, proof of cash and SBA lender QoE (home page)", publisher: "QoEAgent", type: vendor, url: "https://qoeagent.ai/", date: "2026-10-20", access: full, locator: "'Who we serve' (sell-side bankers and advisors)" }
    - { ref: QOEAGENT-SBAUPDATE-2026, title: "The September 25 Update: A Buyer's QoE Can Now Reach the Lender", publisher: "QoEAgent", type: vendor, url: "https://qoeagent.ai/sba-qoe-september-25-update/", date: "2026-10-01", access: full, locator: "'What the clause said, and what it says now'" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: mid-market CPA firm (Pease Bell; size not verified) and AI-native provider. The article says firms are 'already seeing measurable gains' but gives no figures. A broker's marketing page (CTACQ-QOE-2026) says sell-side QoE typically costs 40-60% of a buy-side QoE; that is a general price observation, not AI-specific, and is not used as an outcome."

- id: advisory-transactions-09
  title: "Data-room document intelligence with source citations for diligence teams"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Data rooms are growing and timelines are compressing, making it harder to bring the same judgment to each issue (PwC-ToltIQ release). Contract review is often descoped from financial diligence because of time (PwC deals leader, ICAEW)."
  solution: "Tools ingest data rooms and disparate documents, surface key points with source citations, and let teams question the corpus. PwC's Deals practice has used ToltIQ on live transactions; PwC UK describes using Harvey to analyse deal-room material with citations. PwC's deals leader says contracts that used to be descoped can now be reviewed, which creates follow-up on anomalies."
  outcomes:
    - lever: capacity
      description: "PwC and ToltIQ report how widely the platform has been used inside PwC Deals"
      figure: "4,000+ PwC Deals practitioners; 5,000+ deals; 2 million+ documents"
      measures: "Usage counts stated in the joint release: practitioners who have used ToltIQ, deals it has been used on at PwC, and documents processed. Adoption counts, not performance."
      provenance: self-reported
      source_ref: PWC-TOLTIQ-2026
    - lever: quality
      description: "Adjacent measurement: a law firm's tests of LLM review of commercial contracts in M&A legal due diligence"
      figure: "74% to 95% accuracy on average"
      measures: "Addleshaw Goddard's accuracy of LLM review of commercial contracts in its own legal due diligence test, before and after optimised retrieval and prompting. Legal DD, not financial DD."
      provenance: self-reported
      source_ref: ARTLAW-AG-2024
    - lever: speed
      description: "Adjacent estimate: Deloitte UK's e-discovery lead on legal due diligence document review"
      figure: "25% saving versus traditional AI; 75% versus manual review"
      measures: "Efficiency saving as stated by Peter Robinson (Deloitte UK) for GenAI in legal due diligence; method not published. Legal DD, a recollection in a magazine interview."
      provenance: self-reported
      source_ref: ICAEW-BIGSIX-2024
  prerequisites:
    - "Enterprise-grade or private-environment deployment that satisfies seller NDAs (KJK-NDA-2026)"
    - "Citation back to source documents so reviewers can verify (BLOCKCHAINNEWS-PWCUK-2026)"
  risks_and_guardrails:
    - "Uploading confidential data to an AI tool may breach NDA terms on retention, permitted representatives and use (KJK-NDA-2026)"
    - "Intralinks reports hallucinated outputs leading to inaccurate diligence among the incident clusters it observed (INTRALINKS-AIDEAL-2026)"
    - "PwC UK's approach anchors outputs to verifiable sources (BLOCKCHAINNEWS-PWCUK-2026, secondary summary)"
  human_checkpoints:
    - "Practitioners review anomalies the AI flags; PwC's deals leader gives an illustrative 20 hours of human time on follow-up (ICAEW-BIGSIX-2024)"
  role_evolution: "PwC's deals leader says staff can gain more insight and that it is hard to predict which tasks are replaced versus created (ICAEW-BIGSIX-2024). BDO's transaction services partner says GenAI could lead to new roles in AI oversight, data interpretation and client engagement (ICAEW-BIGSIX-2024)."
  evidence_grade: B
  sources:
    - { ref: PWC-TOLTIQ-2026, title: "Reimagining deals for the Age of AI: PwC and ToltIQ enter strategic relationship", publisher: "PwC US", type: firm, url: "https://www.pwc.com/us/en/about-us/newsroom/press-releases/reimagining-deals-for-the-age-of-ai.html", date: "2026-06-15", access: full, locator: "'Built for the realities of deal execution' paragraph (usage counts); three priorities paragraph. Read through the r.jina.ai mirror" }
    - { ref: BLOCKCHAINNEWS-PWCUK-2026, title: "PwC Leverages AI for Faster Deal Execution", publisher: "Blockchain.News (secondary summary of PwC UK Deals CTO)", type: press, url: "https://blockchain.news/news/pwc-ai-deal-execution", date: "2026-05-06", access: full, locator: "paragraphs 1-4 (document ingestion with citations, valuation reading, generative drafting)" }
    - { ref: ICAEW-BIGSIX-2024, title: "Insight: AI and the Big Six", publisher: "ICAEW Corporate Financier", type: professional-body, url: "https://www.icaew.com/technical/corporate-finance/corporate-finance-faculty/corporate-financier/2024/articles/december/insight-ai-and-the-big-six", date: "2024-12-10", access: full, locator: "PwC (T. Popplewell) contracts example; Deloitte (P. Robinson) legal DD efficiency paragraph; BDO (M. Jones) on roles" }
    - { ref: ARTLAW-AG-2024, title: "AG Proves LLMs Can Do Well On Due Diligence", publisher: "Artificial Lawyer (reporting Addleshaw Goddard's research report)", type: press, url: "https://www.artificiallawyer.com/2024/10/08/ag-proves-llms-can-do-well-on-due-diligence/", date: "2024-10-08", access: full, locator: "accuracy 74% to 95% quote; chunking strategy 14%-22% improvement" }
    - { ref: KJK-NDA-2026, title: "AI and M&A NDAs: Managing Artificial Intelligence Risks in Confidentiality Agreements", publisher: "Kohrman Jackson & Krantz", type: firm, url: "https://kjk.com/2026/03/12/ai-and-ma-ndas-managing-artificial-intelligence-risks-in-confidentiality-agreements/", date: "2026-03-12", access: full, locator: "'Why AI Use in M&A Due Diligence Raises NDA Concerns'; 'How M&A NDAs Are Evolving'" }
    - { ref: INTRALINKS-AIDEAL-2026, title: "AI Use Permeates Dealmaking Despite Operational Concerns: SS&C Intralinks Report", publisher: "SS&C Intralinks (via Business Wire / Nasdaq)", type: survey, url: "https://www.nasdaq.com/press-release/ai-use-permeates-dealmaking-despite-operational-concerns-ssc-intralinks-report-2026", date: "2026-04-08", access: full, locator: "incident bullet" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: Big Four (PwC US, PwC UK, Deloitte UK) with a vendor (ToltIQ) and a law firm. Grade capped at B: named deployment with usage counts only, and the accuracy and efficiency measurements are from legal DD, an adjacent process. The ICAEW article is 22 months old and is used as a foundation. PwC UK's May 2026 account is a secondary news summary; PwC's own page was not read. The older PwC UK-Harvey alliance (2023) appeared only as a search result. Independence: PwC's and Deloitte's attest-client restrictions were not researched here."

- id: advisory-transactions-10
  title: "Deeper-cut analytics (SKU, customer, vendor, workforce, working capital) enabled by automation of routine diligence"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [data-reporting, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Routine preparation consumes the time that would otherwise go to deeper analysis, and an identified EBITDA adjustment can be worth many times the fee (Forvis Mazars US)."
  solution: "By automating the routine, diligence teams spend more of the engagement on SKU-level data, customer and vendor insight, employee productivity and working capital trends. Forvis Mazars US pairs this with sector-specific experience and says the result is more analysis, throughput and data-driven insight."
  outcomes:
    - lever: quality
      description: "Forvis Mazars US says depth of analysis increases"
      figure: "none published"
      measures: "Qualitative statement in a firm article; no engagement, tool or metric named"
      provenance: self-reported
      source_ref: FORVIS-QOE-2026
  prerequisites:
    - "Pairing experienced professionals with current tools (FORVIS-QOE-2026)"
  risks_and_guardrails:
    - "The same article warns that firms that over-rely on automation can head down wrong paths, not know when to stop and miss the true issues, and that AI is raising the prevalence of lower-quality QoE products (FORVIS-QOE-2026)"
  human_checkpoints:
    - "Professional judgment on EBITDA quality, net working capital, debt-like items and what matters to the deal (FORVIS-QOE-2026)"
  role_evolution: "Forvis Mazars US describes a 'talent flywheel' in high-performing firms and warns that depleting junior ranks will create future holes in executive-level insight (FORVIS-QOE-2026)."
  evidence_grade: C
  sources:
    - { ref: FORVIS-QOE-2026, title: "Quality of Earnings & Due Diligence in an AI World", publisher: "Forvis Mazars US (Transaction Advisory)", type: firm, url: "https://www.forvismazars.us/forsights/2026/09/quality-of-earnings-due-diligence-in-an-ai-world", date: "2026-09-08", access: full, locator: "sections '2. Depth' and '3. Talent'; 'Need for Diligence'" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: top-tier US firm (Forvis Mazars US; ranking not verified in this pass). Marked emerging and C because the article is a view from a named practice leader and does not name a tool or engagement. Forvis Mazars US's January 2024 article on diligence of AI-enabled targets is covered in module notes."

- id: advisory-transactions-11
  title: "Lifecycle M&A platform with an agent harness, from diligence to integration"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [research-synthesis, coordination-scheduling, expert-judgment]
  pattern: end-to-end-case-agent
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Deal teams run diligence, structuring and integration as separate, isolated tasks across tax, technology and financial workstreams (Deloitte)."
  solution: "Deloitte's M&A Platform embeds AI across the deal lifecycle, supported by an agentic harness to scale, govern and manage AI agents, and runs structured, interconnected workflows from strategy and diligence through integration. It is delivered through Deloitte's Ascend service delivery platform. EY-Parthenon markets a comparable Diligence Edge platform with a digital diligence assistant and an automation suite."
  outcomes:
    - lever: capacity
      description: "Deloitte says how many client engagements the platform is in use across"
      figure: "more than 1,000 client engagements"
      measures: "Count of client engagements in which the platform is in use, per Deloitte's release. Adoption count, not outcome."
      provenance: self-reported
      source_ref: DELOITTE-MAPLATFORM-2026
    - lever: speed
      description: "Deloitte's own survey of 500 corporate and PE leaders reports benefits realised from AI in M&A"
      figure: "66% automated status reporting; 60% enhanced decision-making; 51% streamlined cross-functional coordination"
      measures: "Share of surveyed dealmakers who say they already see productivity gains in each area (Deloitte GenAI in M&A Pulse Survey, 500 corporate and PE leaders); respondent perceptions, not measured performance"
      provenance: vendor-published
      source_ref: DELOITTE-MAPLATFORM-2026
  prerequisites:
    - "Approved deal data sources: integration with them is the capability respondents rank as most important (DELOITTE-PULSE-2026)"
    - "Ring-fenced client and transaction data environment (DELOITTE-MAPLATFORM-2026)"
  risks_and_guardrails:
    - "Deloitte says the platform is designed to protect and ringfence client and transaction data (DELOITTE-MAPLATFORM-2026)"
    - "Human review remains the top requirement for high-stakes GenAI use in Deloitte's pulse study (DELOITTE-PULSE-2026)"
    - "Deloitte's earlier survey release carries the note that certain services may not be available to attest clients under public accounting rules (DELOITTE-GENAIMA-2025). Which deal services this covers was not verified."
  human_checkpoints:
    - "Deloitte describes the platform as human-led and AI-powered (DELOITTE-MAPLATFORM-2026)"
  role_evolution: "Deloitte's leaders say the platform lets deal teams achieve deeper insight by combining human judgment with AI (DELOITTE-MAPLATFORM-2026)."
  evidence_grade: B
  sources:
    - { ref: DELOITTE-MAPLATFORM-2026, title: "Deloitte Expands AI and Agentic AI Capabilities With M&A Platform Enabling Smarter, More Streamlined Deal Execution", publisher: "Deloitte US", type: firm, url: "https://www.deloitte.com/us/en/about-us/press-room/deloitte-announces-ma-platform.html", date: "2026-09-22", access: full, locator: "paragraphs 2-3 (in use across more than 1,000 client engagements; agentic harness); survey paragraphs; closing paragraphs on data protection and Ascend" }
    - { ref: DELOITTE-PULSE-2026, title: "2026 Generative AI in M&A Pulse Study", publisher: "Deloitte US", type: survey, url: "https://www.deloitte.com/us/en/what-we-do/capabilities/mergers-acquisitions-restructuring/articles/m-and-a-generative-ai-study.html", date: "2026", access: full, locator: "'Key takeaways from the survey'. Page is undated; the 2026-09-22 Deloitte release calls the pulse survey recently released" }
    - { ref: DELOITTE-GENAIMA-2025, title: "Deloitte Survey: 86% of Corporate and Private Equity Leaders Now Use Generative AI, with Plans to Boost Spending in 2025", publisher: "Deloitte US", type: survey, url: "https://www.deloitte.com/us/en/about/press-room/deloitte-survey-genai-in-mna.html", date: "2025-10-09", access: full, locator: "boilerplate paragraph on attest-client services" }
    - { ref: EY-DILIGENCEEDGE-2026, title: "Diligence Edge: AI Diligence Platform", publisher: "EY-Parthenon", type: firm, url: "https://www.ey.com/en_uk/services/strategy/dilligence-edge", date: "2026-10-20", access: full, locator: "sections 'Digital Diligence Assistant', 'Automation suite', 'People-powered innovation'. Page is undated; date is access date. Read through the r.jina.ai mirror (the US page did not render)" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: Big Four (Deloitte, EY). Grade B because Deloitte names the platform and a usage count but publishes no outcome. The EY page is marketing copy with no usage or outcome data (grade C on its own); an ICAEW 2024 article reports EY has a tool called EY Edge and an in-house LLM, EYQ (ICAEW-BIGSIX-2024). Deloitte's 2025 and 2026 surveys use different samples (1,000 US leaders versus 500) and different measures and should not be compared. Deloitte sells M&A services, so its survey findings are vendor-published."

- id: advisory-transactions-12
  title: "AI-drafted diligence deliverables: QoE exhibits, databook summary slides, red-flag reports and executive summaries from workpapers"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Turning workpapers and databooks into executive-ready exhibits, summary slides and findings decks is slow, senior-reviewed work (General Catalyst job board posting)."
  solution: "Generative drafting of report pages and summaries from workpapers. PwC UK's Deals CTO describes producing executive-ready summaries from complex workpapers (secondary summary). A July 2026 expert-network posting says a foundation AI lab wants TAS managers to create, evaluate and refine AI-generated QoE exhibits, databook summary slides, diligence findings decks, working capital pages and red-flag reports."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "No measured result; the sources describe intent and tasks"
      provenance: self-reported
      source_ref: BLOCKCHAINNEWS-PWCUK-2026
  prerequisites:
    - "Workpapers and databooks in a form a model can draft from"
  risks_and_guardrails:
    - "Forvis Mazars US warns AI can make thin reports look professional but they will not hold up under scrutiny (FORVIS-QOE-2026)"
    - "Cautionary analogue outside this module: Deloitte Australia agreed to repay the final instalment of a AU$440,000 government review after AI-generated errors including nonexistent references were found; Deloitte said the errors did not affect the findings (CITYAM-DELOITTEAU-2025)"
  human_checkpoints:
    - "Experienced TAS managers evaluate and refine the AI-generated pages (GC-ETHOS-JOB-2026)"
  role_evolution: "The posting pays experienced Big Four-level TAS managers an hourly rate to train a model on report production, which shows the source of expertise labs want; it says nothing about how firms staff the work (GC-ETHOS-JOB-2026)."
  evidence_grade: C
  sources:
    - { ref: GC-ETHOS-JOB-2026, title: "Expert Opportunity - Transaction Advisory Services Manager", publisher: "Ethos via General Catalyst job board", type: job-posting, url: "https://jobs.generalcatalyst.com/companies/ethos-2-e1b0048b-7d7c-4a76-97d7-b71911ec294a/jobs/86831351-expert-opportunity-transaction-advisory-services-manager-100-hr-up-to-2-000-week", date: "2026-07-18", access: full, locator: "'About This Opportunity' (task list); 'Qualifications'" }
    - { ref: BLOCKCHAINNEWS-PWCUK-2026, title: "PwC Leverages AI for Faster Deal Execution", publisher: "Blockchain.News (secondary summary of PwC UK Deals CTO)", type: press, url: "https://blockchain.news/news/pwc-ai-deal-execution", date: "2026-05-06", access: full, locator: "paragraph on generative drafting" }
    - { ref: FORVIS-QOE-2026, title: "Quality of Earnings & Due Diligence in an AI World", publisher: "Forvis Mazars US (Transaction Advisory)", type: firm, url: "https://www.forvismazars.us/forsights/2026/09/quality-of-earnings-due-diligence-in-an-ai-world", date: "2026-09-08", access: full, locator: "section '3. Talent'" }
    - { ref: CITYAM-DELOITTEAU-2025, title: "Deloitte refunds Australian government after AI 'made up citations' in report", publisher: "City AM", type: press, url: "https://www.cityam.com/?p=2367690", date: "2025-10-06", access: full, locator: "paragraphs 1-6" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: Big Four (PwC UK, via secondary source) and an AI lab (unnamed) recruiting through an expert network. The posting pays $100 per hour for 5-20 hours a week and is not evidence that firms use the output. The Deloitte Australia incident was a government assurance review, not transaction advisory; it is a deliverable-quality analogue and is also a candidate for routing to risk-controls."

- id: advisory-transactions-13
  title: "Buyers and sponsors run first-pass diligence with generative AI in-house"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: research-brief
  ladder: augment
  change_scope: model
  runtime_class: personal-assistant
  maturity: in-production
  problem: "PE and corporate deal teams must evaluate more opportunities and process larger information volumes under tight deadlines. This is the demand-side shift TAS providers face: some first-pass diligence moves in-house (Datasite; Intralinks)."
  solution: "Deal teams use AI tools in diligence themselves: S&P Global finds diligence has the highest AI integration among PE operations, Datasite reports half of dealmakers regularly use AI in diligence, and Deloitte finds 35% of adopters apply GenAI to diligence."
  outcomes:
    - lever: capacity
      description: "S&P Global: share of GPs reporting AI integrated into due diligence"
      figure: "31%"
      measures: "GPs who say AI is somewhat or fully integrated in due diligence, in S&P Global Market Intelligence's 2026 PE survey; sample size not stated in the release portion read"
      provenance: independent
      source_ref: SPGLOBAL-PE-2026
    - lever: capacity
      description: "Datasite and FT Longitude: share of dealmakers with AI regularly embedded in due diligence"
      figure: "50%"
      measures: "Respondents who report AI regularly embedded in due diligence; survey of 1,000 senior dealmakers (C-suite or C-1) in 27 countries, March 2026, commissioned by Datasite"
      provenance: vendor-published
      source_ref: DATASITE-NEWDEALTEAM-2026
    - lever: speed
      description: "SS&C Intralinks: reported time saving in the diligence phase"
      figure: "21-30%"
      measures: "Time savings that surveyed dealmakers (400 global M&A dealmakers, with Reuters) report from AI tools in the due diligence phase; self-reported perceptions"
      provenance: vendor-published
      source_ref: INTRALINKS-AIDEAL-2026
  prerequisites:
    - "Enterprise-grade tools that satisfy seller NDAs and data-room terms (KJK-NDA-2026)"
  risks_and_guardrails:
    - "S&P respondents name lack of expertise (49%), data privacy concerns (43%) and model accuracy concerns (38%) as barriers (SPGLOBAL-PE-2026)"
    - "Deloitte's 2025 survey: 67% cite data security and 65% cite data quality and availability as leading concerns (DELOITTE-GENAIMA-2025)"
    - "Datasite: 58% rely on human review and validation to trust AI outputs (DATASITE-NEWDEALTEAM-2026)"
  human_checkpoints:
    - "Human review and validation (Datasite); 45% say the decision to sign should always remain human (DATASITE-NEWDEALTEAM-2026)"
  role_evolution: "Datasite respondents say negotiation, strategic judgment, assessing trust and accountability are hardest for AI to replicate (DATASITE-NEWDEALTEAM-2026)."
  evidence_grade: C
  sources:
    - { ref: SPGLOBAL-PE-2026, title: "S&P Global Market Intelligence's 2026 Private Equity Survey Shows Fundraising Confidence Rising as Managers Pivot to Operational Value", publisher: "S&P Global Market Intelligence", type: survey, url: "https://press.spglobal.com/2026-04-13-S-P-Global-Market-Intelligences-2026-Private-Equity-Survey-Shows-Fundraising-Confidence-Rising-as-Managers-Pivot-to-Operational-Value", date: "2026-04-13", access: full, locator: "'Limited AI adoption' bullet" }
    - { ref: DATASITE-NEWDEALTEAM-2026, title: "Datasite: AI Is Becoming Indispensable in Dealmaking, But Trust and Governance Will Determine the Winners", publisher: "Datasite (GlobeNewswire, with FT Longitude)", type: survey, url: "https://www.finanznachrichten.de/nachrichten-2026-07/68975080-datasite-ai-is-becoming-indispensable-in-dealmaking-but-trust-and-governance-will-determine-the-winners-399.htm", date: "2026-07-08", access: full, locator: "'Four key findings from the research'; 'About the report'" }
    - { ref: INTRALINKS-AIDEAL-2026, title: "AI Use Permeates Dealmaking Despite Operational Concerns: SS&C Intralinks Report", publisher: "SS&C Intralinks (via Business Wire / Nasdaq)", type: survey, url: "https://www.nasdaq.com/press-release/ai-use-permeates-dealmaking-despite-operational-concerns-ssc-intralinks-report-2026", date: "2026-04-08", access: full, locator: "key findings list" }
    - { ref: DELOITTE-GENAIMA-2025, title: "Deloitte Survey: 86% of Corporate and Private Equity Leaders Now Use Generative AI, with Plans to Boost Spending in 2025", publisher: "Deloitte US", type: survey, url: "https://www.deloitte.com/us/en/about/press-room/deloitte-survey-genai-in-mna.html", date: "2025-10-09", access: full, locator: "paragraphs on pre-sign use (35% due diligence) and barriers" }
    - { ref: SEARCHFUNDER-SOURCETABLE-2025, title: "Has anyone used Sourcetable AI for QoE Analysis?", publisher: "Searchfunder (community thread)", type: community, url: "https://searchfunder.com/post/has-anyone-used-sourcetable-ai-for-qoe-analysis", date: "2025-10", access: full, locator: "original post and the professional's reply; date approximate" }
    - { ref: KJK-NDA-2026, title: "AI and M&A NDAs: Managing Artificial Intelligence Risks in Confidentiality Agreements", publisher: "Kohrman Jackson & Krantz", type: firm, url: "https://kjk.com/2026/03/12/ai-and-ma-ndas-managing-artificial-intelligence-risks-in-confidentiality-agreements/", date: "2026-03-12", access: full, locator: "'How M&A NDAs Are Evolving to Address AI'" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: PE sponsors and corporate buyers (the clients of TAS firms), surveyed by a data vendor, a data-room vendor and a Big Four firm. These surveys cover diligence generally, not QoE or TAS, so they cap at C. Figures conflict across sources: a Post-Trade 360 article reports the S&P figure as 'just shy of one in four' while S&P's own release says 31% (the release is used). The 27% 'effective in creating value during diligence' figure comes only from the Post-Trade 360 secondary article (POSTTRADE-SPGLOBAL-2026) and is not in the outcomes. A&M's 2026 European diligence report (80%+ using or experimenting; 70% of Tier 1 funds using consistently versus 41% of large and 28% of mid-sized funds) was seen only in search (AM-EURODD-2026, search-only). The Datasite page lists related coverage dated 2026-06-25, earlier than the 2026-07-08 release date used here. Intralinks' separate H2 2026 sentiment report uses different numbers and is not comparable."

- id: advisory-transactions-14
  title: "Post-deal integration planning, TSA drafting and synergy sizing with generative AI"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [coordination-scheduling, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Post-deal value realisation needs coordinated execution across systems and is less structured and harder to scale than pre-deal analysis (Accenture's PE lead, via CFO Dive). Line leaders must juggle integration work with their day jobs (Bain)."
  solution: "Bain expects early adopters to draft integration workplans and transition service agreements in less than 20% of the time previously spent, then use company data to size cost and revenue synergies and draft value creation plans. Deloitte's pulse study reports that 52% of respondents apply GenAI in post-close integration (its survey question covers use or piloting)."
  outcomes:
    - lever: speed
      description: "Bain's expectation for early adopters over the following 12 months"
      figure: "less than 20% of prior time"
      measures: "Bain's forward-looking expectation for the time early adopters will spend drafting integration workplans and TSAs relative to what they previously spent; not a measured result"
      provenance: vendor-published
      source_ref: BAIN-GENAIMA-2025
    - lever: capacity
      description: "Accenture: share of organizations investing in GenAI for post-deal M&A activity"
      figure: "27% in 2026, up from 18% in 2024"
      measures: "Share of surveyed organizations investing in GenAI for post-deal M&A activity; Accenture survey of 650 senior dealmakers in 12 industries and 24 countries, January 2026 (pre-deal was 46%, up from 31%)"
      provenance: vendor-published
      source_ref: CFODIVE-ACCENTURE-2026
  prerequisites:
    - "Integration with approved deal data sources (DELOITTE-PULSE-2026)"
  risks_and_guardrails:
    - "Not described in these sources beyond the human-review requirement in the pulse study (DELOITTE-PULSE-2026)"
  human_checkpoints:
    - "Human review remains the top requirement for high-stakes use (DELOITTE-PULSE-2026)"
  role_evolution: "Bain says generative AI will pick up project management tasks and M&A teams should rethink the skills they need, with more focus on strategic value creation (BAIN-GENAIMA-2025)."
  evidence_grade: C
  sources:
    - { ref: BAIN-GENAIMA-2025, title: "Generative AI in M&A: You're Not Behind-Yet", publisher: "Bain & Company (2025 M&A Report)", type: firm, url: "https://www.bain.com/insights/generative-ai-m-and-a-report-2025/", date: "2025-02-04", access: full, locator: "paragraphs on integration workplans and TSAs; 'Protecting people and the business during M&A'" }
    - { ref: CFODIVE-ACCENTURE-2026, title: "GenAI gains ground in M&A, but post-deal adoption lags", publisher: "CFO Dive", type: press, url: "https://www.cfodive.com/news/generative-ai-gains-ground-mergers-postdeal-adoption-lags/814895/", date: "2026-03-17", access: full, locator: "paragraphs 2-3 (adoption figures) and the sentence on McKinsey's integration expectation" }
    - { ref: DELOITTE-PULSE-2026, title: "2026 Generative AI in M&A Pulse Study", publisher: "Deloitte US", type: survey, url: "https://www.deloitte.com/us/en/what-we-do/capabilities/mergers-acquisitions-restructuring/articles/m-and-a-generative-ai-study.html", date: "2026", access: full, locator: "'Key takeaways' (49% deal closing, 52% post-close integration)" }
  last_reviewed: "2026-10-20"
  notes: "Firm types: consultancies (Bain, Accenture, Deloitte) writing about corporate and PE acquirers rather than reporting an advisory-firm deployment. McKinsey's expectation that agentic AI will take over more than 50% of integration planning and execution tasks appears only inside the CFO Dive article. Deloitte's M&A Platform (use case 11) covers integration but publishes no integration outcome. No integration-management-office case with outcomes was found."

- id: advisory-transactions-15
  title: "LLM-supported knowledge capture to retain rather than replace an acquired company's systems"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [research-synthesis, software-systems]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Post-merger systems integration often loses the human and system-embedded knowledge of the acquired firm, which pushes acquirers to rip out and replace the target's ERP (ECIS 2026 paper)."
  solution: "In a study of two consecutive acquisitions of the same digital target, the second acquirer used LLM-supported 'learning system knowledge through chat' to adopt a retain-and-revive approach for the target's proprietary ERP instead of the first acquirer's rip-and-replace."
  outcomes:
    - lever: risk
      description: "The authors report increased knowledge transferability, aggregation and efficiency, and lower assumed system opacity, personnel dependence and conversion cost"
      figure: "none published"
      measures: "Qualitative findings from a two-acquisition case study; organizations unnamed"
      provenance: independent
      source_ref: ECIS-PMI-2026
  prerequisites:
    - "Access to the target's system documentation, code or people to build a knowledge base"
  risks_and_guardrails:
    - "Not discussed in the abstract"
  human_checkpoints:
    - "Not discussed in the abstract"
  role_evolution: "Not discussed in the abstract."
  evidence_grade: C
  sources:
    - { ref: ECIS-PMI-2026, title: "From Knowledge Loss To Knowledge Leverage: How Gen AI Affordances Transform Post-Merger IS Integration", publisher: "ECIS 2026 Proceedings (AIS eLibrary); Erber, Ortiz de Guinea, Steininger", type: academic, url: "https://aisel.aisnet.org/ecis2026/is_adopt/is_adopt/24/", date: "2026", access: full, locator: "abstract (only the abstract was read). Month of publication not shown on the page" }
  last_reviewed: "2026-10-20"
  notes: "Firm type: acquirers, not advisory firms. Grade C: the case organizations are unnamed so this cannot meet B. Only the abstract was read."

- id: advisory-transactions-16
  title: "Autonomous quality-of-earnings analysis (idea)"
  archetype: advisory
  module: transactions
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: "QoE is a judgment-heavy, multi-week product; dealmakers see an agent that runs the whole analysis as a coming disruption (SS&C Intralinks survey)."
  solution: "An agent would own the QoE end to end (ingest, map, test, normalize, draft) with human checkpoints. This is an idea discussed by surveyed dealmakers, not a deployed product; the July 2026 buyer's guide says no AI tool runs a full QoE because it turns on judgment."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "Intralinks reports that autonomous QoE analysis is among the most highly anticipated disruptions expected by 2030; no performance data"
      provenance: vendor-published
      source_ref: INTRALINKS-AIDEAL-2026
  prerequisites:
    - "Reliable add-back and footnote handling, which practitioners say is where tools degrade (WORKWISE-QOE-2026)"
  risks_and_guardrails:
    - "Over 80% of Intralinks respondents say they are comfortable with AI executing some multi-step workflows with minimal human intervention, while more than 57% report rising senior-level resistance driven by accuracy, explainability and fiduciary concerns (INTRALINKS-AIDEAL-2026)"
    - "Under the SBA rule as QoEAgent reads it, software cannot be the provider of a lender QoE (QOEAGENT-WHO-2026)"
  human_checkpoints:
    - "Not specified; the source describes minimal-human-intervention workflows generally"
  role_evolution: "Not stated."
  evidence_grade: D
  sources:
    - { ref: INTRALINKS-AIDEAL-2026, title: "AI Use Permeates Dealmaking Despite Operational Concerns: SS&C Intralinks Report", publisher: "SS&C Intralinks (via Business Wire / Nasdaq)", type: survey, url: "https://www.nasdaq.com/press-release/ai-use-permeates-dealmaking-despite-operational-concerns-ssc-intralinks-report-2026", date: "2026-04-08", access: full, locator: "key findings: comfort with multi-step workflows and autonomous QoE" }
    - { ref: WORKWISE-QOE-2026, title: "The Best AI Tools for Quality of Earnings and Financial Due Diligence in 2026", publisher: "WorkWise Solutions (AI consulting firm)", type: vendor, url: "https://workwisesolutions.org/guides/best-ai-qoe-financial-due-diligence-tools.html", date: "2026-07-20", access: full, locator: "TLDR" }
    - { ref: QOEAGENT-WHO-2026, title: "Who Can Prepare an SBA Quality of Earnings Report", publisher: "QoEAgent", type: vendor, url: "https://qoeagent.ai/who-can-prepare-sba-quality-of-earnings/", date: "2026-09-05", access: full, locator: "opening summary" }
  last_reviewed: "2026-10-20"
  notes: "Idea (D). The idea is discussed in a vendor survey and a consultancy guide, not demonstrated. Vendors above (use cases 03 to 05) sell staged versions with human review."
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Scoping, data request and data-room set-up** (`coordination-scheduling`, `transaction-processing`). Target teams with limited deal experience are a bottleneck even when the adviser's tools are fast (FORVIS-QOE-2026).
- **Data ingestion, trial balance and ledger mapping, proof of cash** (`transaction-processing`, `data-reporting`). The most automated step in public sources (use cases 01, 03).
- **Trend, flux and anomaly analysis and management meetings** (`data-reporting`, `client-interaction`). Question lists tailored to gaps (use case 02; FORVIS-QOE-2026).
- **Adjusted EBITDA, add-backs, net working capital and debt-like items** (`expert-judgment`). Where practitioners say AI is least reliable (use case 04).
- **Revenue, customer, vendor and SKU analysis** (`data-reporting`) (use case 10).
- **Contract and data-room review** (`research-synthesis`, `review-assurance`) (use case 09).
- **Databook, red-flag report and summary production** (`document-production`) (use case 12).
- **SPA support and completion accounts** (`expert-judgment`, `document-production`). KPMG's TAS AI lead names carve-out planning and analysing large data sets for completion accounts as AI roles (ICAEW-BIGSIX-2024; spoken view, no deployment detail).
- **Post-deal: Day-1, integration planning, TSAs, synergy tracking** (`coordination-scheduling`) (use case 14).
- **Sell-side readiness and vendor due diligence** (`document-production`, `review-assurance`) (use case 08).

### Common pain points

- Compressing timelines and growing data rooms (PWC-TOLTIQ-2026).
- Scanned bank statements, multiple accounts, system migrations and year-end-only accruals in small targets (QOEAGENT-CASE-2026; QOEAGENT-SBAREQ-2026).
- Buyers' and lenders' demand for reconciliation and normalization they can trust, not report-only output (SEARCHFUNDER-COLUMBIA-2026, one lender-side reply).
- Cost: a broker's marketing page estimates 2026 QoE fees of $25,000-$200,000 with Big Four and national firms higher; treat as an estimate, not data (CTACQ-QOE-2026). A searcher reply puts the range at $500 to $25,000+ for small deals (SEARCHFUNDER-COLUMBIA-2026).
- Post-deal work is less structured and harder to scale than pre-deal (CFODIVE-ACCENTURE-2026).

### Metrics and benchmarks

| Metric | Value | What it measures | Source | Provenance |
|---|---|---|---|---|
| Time saved per FDD | 27% | Opio's average time saved per FDD; no method | OPIO-SITE-2026 | vendor-published |
| QoE prep time eliminated | 80% | Audit Sight claim for management-meeting prep | CPAPA-AUDITSIGHT-2025 | vendor-published |
| Proof of cash tie-out | within 1% in 24 hours | QoEAgent claim | QOEAGENT-HOME-2026 | vendor-published |
| Time saving in diligence | 21-30% | Dealmakers' self-reported saving, 400 respondents | INTRALINKS-AIDEAL-2026 | vendor-published |
| AI fully integrated across deal stages | 49% (90% using) | Intralinks survey of 400 dealmakers | INTRALINKS-AIDEAL-2026 | vendor-published |
| Incidents or near-misses, past 12 months | 80% | Dealmakers reporting AI-related security or accuracy incidents; cluster figures 48% access control, 40% hallucinated outputs (denominator not stated) | INTRALINKS-AIDEAL-2026 | vendor-published |
| Senior-level resistance increased | more than 57% | Respondents reporting rising resistance | INTRALINKS-AIDEAL-2026 | vendor-published |
| AI regularly embedded in diligence | 50% | Datasite and FT Longitude survey of 1,000 dealmakers, March 2026 | DATASITE-NEWDEALTEAM-2026 | vendor-published |
| Human-only decisions no longer defensible | 62% | Same survey | DATASITE-NEWDEALTEAM-2026 | vendor-published |
| GPs with AI somewhat or fully integrated in diligence | 31% | S&P Global 2026 PE survey (highest of the categories listed) | SPGLOBAL-PE-2026 | independent |
| Adopters using GenAI for due diligence | 35% | Deloitte 2025 survey of 1,000 US corporate and PE leaders (86% had integrated GenAI) | DELOITTE-GENAIMA-2025 | vendor-published |
| Organizations using AI in M&A | 90% (37% across multiple stages) | Deloitte 2026 pulse survey of 500 leaders | DELOITTE-MAPLATFORM-2026 | vendor-published |
| Pre-deal and post-deal GenAI investment | 46% and 27% (2026) | Accenture survey of 650 dealmakers, January 2026 | CFODIVE-ACCENTURE-2026 | vendor-published |
| M&A timeline and cost effect | 10-30% shorter; about 20% lower cost | McKinsey, based on a February 2025 survey (corporate acquirers, not TAS) | CFODIVE-MCKINSEY-2026 | vendor-published |
| LLM accuracy on commercial-contract review | 74% to 95% | Addleshaw Goddard legal DD test (adjacent) | ARTLAW-AG-2024 | self-reported |
| Practitioners with an AI platform | 2,500 in PwC UK deals, each with at least one platform | PwC UK deals leader, Dec 2024 | ICAEW-BIGSIX-2024 | self-reported |

Not found: error rates, override rates, parallel-run results, inspection outcomes or independent measurement of AI-assisted QoE accuracy or timeline.

### Guardrails and regulatory points

- **Confidentiality and NDAs.** Public AI tools may retain inputs or license content, and an AI provider may not count as a permitted representative under an NDA. Some sellers now bar uploads to public AI, restrict tools that train on data or retain it, or require prior written consent; parties are also agreeing secure enterprise or closed-environment tools (KJK-NDA-2026, 2026-03-12).
- **R&W insurance.** Fasken expects heightened insurer scrutiny of target-AI risk, possible exclusions limited to a known issue or broader if the diligence record is incomplete, and a possible move toward standardized AI exclusions (FASKEN-RWI-2026, 2026-08-13). I found no source on how underwriters treat QoE reports prepared with AI tools.
- **SBA SOP 50 10 8.1** (effective 2026-10-01 per the SBA page): vendor summaries say a QoE is required on 7(a) initial acquisitions of $3 million or more, with an independent professional, a cash proof, and a lender-vendor review of any buyer-commissioned report (SBA-SOP5010-2026; QOEAGENT-SBAUPDATE-2026). QoE clause text unverified against the SBA document.
- **Professional standards.** CS Section 100 says the general standards of professional competence, due professional care, planning and supervision, and sufficient relevant data apply to consulting services (JOFA-CS100-2024). I found no AICPA, IESBA or PCAOB statement on AI in transaction advisory specifically.
- **Independence.** Deloitte's 2025 survey release carries the note that certain services may not be available to attest clients under public accounting rules (DELOITTE-GENAIMA-2025). Which diligence services, if any, are restricted for audit clients was not verified.
- **Vendor controls.** Opio says its platform runs on premise, does not train on client data and is auditable; Deloitte says its platform ring-fences client and transaction data (FORVISGROUP-OPIO-2026; DELOITTE-MAPLATFORM-2026). Both are self-descriptions.
- **Diligence of the target's own AI** (demand created by AI, not use of AI). Forvis Mazars US set out five buy-side considerations in January 2024: AI capability and data, cybersecurity and privacy, scalability and integration, ethical practices, and regulatory compliance (FORVIS-AIBUYSIDE-2024). Grant Thornton's 2026 AI survey of PE leaders reports 9% very confident they could pass an AI governance audit in 90 days (GT-PEAI-2026; publication date not found on the page; routed below).

### Frontier signals (dated, sourced)

- 2026-10-01: SBA SOP 50 10 8.1 effective; creates mandatory QoE demand for larger SBA acquisitions (SBA-SOP5010-2026).
- 2026-09-25: Forvis Mazars Group deploys Opio across multiple countries after a nine-month pilot (FORVISGROUP-OPIO-2026).
- 2026-09-22: Deloitte unveils its M&A Platform with an agentic harness (DELOITTE-MAPLATFORM-2026).
- 2026-09-16: Opio raises EUR 4M; names Forvis Mazars Group and BDO as customers (TECHEU-OPIO-2026).
- 2026-09-08: Forvis Mazars US says AI is also increasing lower-quality, cost-cut QoE products (FORVIS-QOE-2026).
- 2026-08-13: Fasken flags AI exclusions in R&W policies as likely recurring (FASKEN-RWI-2026).
- 2026-07-18: An AI lab recruits TAS managers through an expert network to train models on QoE exhibits and databook slides (GC-ETHOS-JOB-2026).
- 2026-07-08: Datasite survey: 62% say human-only decision-making is no longer defensible in complex deals (DATASITE-NEWDEALTEAM-2026).
- 2026-06-15: PwC Deals and ToltIQ form an exclusive relationship (PWC-TOLTIQ-2026).
- 2026-04-08: Intralinks survey: autonomous QoE analysis is among the disruptions most anticipated by 2030 (INTRALINKS-AIDEAL-2026).
- Conference: ACG DealMAX 2026 (April 27-29, 3,500+ attendees, nearly 900 PE professionals) included expert presentations on AI's impact on the deal world; no session titles or speakers were named in the recap (ACG-DEALMAX-2026).

### Workforce and role effects

- Forvis Mazars US: depleting junior ranks will create future holes in executive-level insight; firms that over-rely on automation risk poorly trained people who cannot tell thin from sound work (FORVIS-QOE-2026).
- Opio's CEO: junior time goes to collecting, checking and adjusting data before interpretation; automating it moves time to analysis and client relationships (TECHEU-OPIO-2026).
- PwC UK deals leader: contract review once descoped can now be done, but anomalies then need about 20 hours of human follow-up in his example, so AI can create work (ICAEW-BIGSIX-2024, Dec 2024). BDO's transaction services partner compares AI to spreadsheets and says it could create roles in AI oversight, data interpretation and client engagement (ICAEW-BIGSIX-2024).
- Pease Bell: entry-level aggregation, reconciliation and schedule tasks can be handled with minimal oversight; staff must interpret outputs and challenge them (PEASEBELL-2026). No staffing data in any source.
- Job postings: an EY-Parthenon financial diligence posting (Kuala Lumpur, 2026-10-09) mentions AI-powered technology only in the firm description; the responsibilities portion read lists no AI-specific task (EY-JOB-2026). Job postings are weak evidence for AI use in this module.

### Objections and concerns practitioners raise

- Accuracy degrades on add-backs, adjustments and footnotes (WORKWISE-QOE-2026); fully automated tools fall short once normalization and judgment matter (SEARCHFUNDER-SOURCETABLE-2025, one practitioner who sells a competing tool).
- Thin, unsupported reports that look professional; a market of cheaper, lower-quality QoE (FORVIS-QOE-2026).
- NDA breach, data retention and trade-secret exposure (KJK-NDA-2026).
- Data security (67%) and data quality (65%) as top barriers in Deloitte's 2025 survey (DELOITTE-GENAIMA-2025); lack of expertise (49%), privacy (43%) and model accuracy (38%) in S&P's (SPGLOBAL-PE-2026).
- Senior-level resistance rising on accuracy, explainability, fiduciary risk and client perception (INTRALINKS-AIDEAL-2026).
- Lenders and insurers: SBA reliance rules; AI exclusions in R&W policies (QOEAGENT-SBAUPDATE-2026; FASKEN-RWI-2026).
- Fabricated content in advisory deliverables (CITYAM-DELOITTEAU-2025, outside this module).

### Interview probes for an advisor

1. In your last three QoEs, which steps did a tool touch (trial balance mapping, proof of cash, flux, add-back candidates, databook), and what did the reviewer change? Do you track exception or override rates?
2. How do your engagement letters, seller NDAs and data-room terms treat AI tools, and has a seller, lender or R&W underwriter asked how AI was used in your diligence?
3. How has scoping or pricing changed when a sponsor arrives with its own first-pass analysis, or when a cheaper AI-native QoE is on the table? What do you do when their numbers conflict with yours?
4. Who does the spreading and reconciliation work now, and how are you training juniors who used to learn from it?
5. Build, buy or partner: which platform do you use, how long did the pilot run, and what would make you stop using it?

---

## 4. Routed to other modules

- **valuation:** SBA valuation independence clause (no valuation prepared for the applicant or seller; no dollar threshold) (QOEAGENT-WHO-2026). Purchase price allocation and fairness opinions were not researched here. IVSC AI disclosure items are in the landscape.
- **risk-controls:** AI risk and governance diligence on targets (FORVIS-AIBUYSIDE-2024; FASKEN-RWI-2026); PE leaders' AI governance readiness (GT-PEAI-2026: 9% very confident they could pass an AI governance audit in 90 days; 45% still piloting; 24% report revenue growth from AI; date not found); Deloitte Australia AI-error refund as a deliverable-quality case (CITYAM-DELOITTEAU-2025, see use case 12).
- **fpa-performance:** Portfolio-company value creation and operational AI (S&P: 72% of GPs rank operational improvements top, SPGLOBAL-PE-2026; GT-PEAI-2026).
- **forensic-disputes:** Fraud and misrepresentation findings surfaced in diligence; deepfaked or forged documents in data rooms (not researched).
- **professional-services (firm operations):** Forvis Mazars US on junior-pipeline depletion and the effect of cheap QoE products on market pricing (FORVIS-QOE-2026); firms' own pricing and staffing leverage; PE and APS ownership; fee ranges quoted on a broker page (CTACQ-QOE-2026).
- **tax:** Transaction tax diligence and structuring (not researched).
- **Outside the archetype (legal and commercial diligence, deal-team tools):** legal contract-review accuracy studies (ARTLAW-AG-2024 used here only as an adjacent measure); expert-call and commercial diligence synthesis (THIRDBRIDGE-PEDD-2026, vendor guide read in full: AI summarises expert-call transcripts and finds patterns across a corpus, no measures); R&W policy mechanics (FASKEN-RWI-2026).
- **Withdrawn academic paper:** "Financial Statement Analysis with Large Language Models" (Kim, Muhn, Nikolaev), an arXiv paper on GPT-4 predicting earnings direction, was withdrawn in 2025 after a co-author found data inconsistencies; it should not be cited as evidence of LLM accuracy on financial statements (ARXIV-KIM-2024).

---

## 5. Sources

Access: full = opened and read; search-only = seen only in search results. Dates are publication dates unless noted.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| FORVIS-QOE-2026 | Quality of Earnings & Due Diligence in an AI World | Forvis Mazars US | firm | https://www.forvismazars.us/forsights/2026/09/quality-of-earnings-due-diligence-in-an-ai-world | 2026-09-08 | full |
| FORVIS-AIBUYSIDE-2024 | Navigating the AI Landscape: 5 Considerations for Private Equity Buy-Side Transactions | Forvis Mazars US | firm | https://www.forvismazars.us/forsights/2024/01/navigating-the-ai-landscape-5-considerations-for-private-equity-buy-side-transactions | 2024-01-18 | full |
| FORVISGROUP-OPIO-2026 | Forvis Mazars scales AI-powered transaction advisory solution | Forvis Mazars Group | firm | https://www.forvismazars.com/group/en/who-we-are/news-publications/latest-news/scaling-ai-powered-transaction-advisory-solutions | 2026-09-25 | full |
| OPIO-SITE-2026 | Frontier AI for transaction services (product page) | Opio | vendor | https://www.opio.fi | 2026-10-20 (access date; undated) | full |
| TECHEU-OPIO-2026 | Opio raises EUR 4M to automate the grunt work of financial due diligence | Tech.eu | press | https://tech.eu/2026/09/16/opio-raises-eur4m-to-automate-the-grunt-work-of-financial-due-diligence/ | 2026-09-16 | full |
| CPAPA-AUDITSIGHT-2025 | Audit Sight Launches Management Meeting Module for Transaction Advisory Teams | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/07/10/audit-sight-launches-management-meeting-module-for-transaction-advisory-teams-to-accelerate-deal-cycles-and-surface-key-insights/164674/ | 2025-07-10 | full |
| QOEAGENT-HOME-2026 | QoEAgent: AI quality of earnings, proof of cash and SBA lender QoE (home page) | QoEAgent | vendor | https://qoeagent.ai/ | 2026-10-20 (access date; undated) | full |
| QOEAGENT-CASE-2026 | Proof of Cash Case Study: An SBA Acquisition the Numbers Did Not Support | QoEAgent | vendor | https://qoeagent.ai/proof-of-cash-case-study-sba-acquisition/ | 2026-10-15 | full |
| QOEAGENT-SBAUPDATE-2026 | The September 25 Update: A Buyer's QoE Can Now Reach the Lender | QoEAgent | vendor | https://qoeagent.ai/sba-qoe-september-25-update/ | 2026-10-01 | full |
| QOEAGENT-SBAREQ-2026 | SBA Quality of Earnings: What the 2026 Rule Requires | QoEAgent | vendor | https://qoeagent.ai/sba-quality-of-earnings-requirement/ | 2026-09-01 | full |
| QOEAGENT-WHO-2026 | Who Can Prepare an SBA Quality of Earnings Report | QoEAgent | vendor | https://qoeagent.ai/who-can-prepare-sba-quality-of-earnings/ | 2026-09-05 | full |
| SHEPI-HOME-2026 | Shepi: AI Quality of Earnings Software for SMB M&A | Shepi | vendor | https://www.shepi.ai | 2026-10-20 (access date; undated) | full |
| SBA-SOP5010-2026 | Lender and Development Company Loan Programs (SOP 50 10) | U.S. Small Business Administration | regulator | https://www.sba.gov/document/sop-50-10-lender-development-company-loan-programs | 2026-10-01 (effective date) | full (landing page only) |
| SPGLOBAL-PE-2026 | S&P Global Market Intelligence's 2026 Private Equity Survey Shows Fundraising Confidence Rising... | S&P Global Market Intelligence | survey | https://press.spglobal.com/2026-04-13-S-P-Global-Market-Intelligences-2026-Private-Equity-Survey-Shows-Fundraising-Confidence-Rising-as-Managers-Pivot-to-Operational-Value | 2026-04-13 | full |
| POSTTRADE-SPGLOBAL-2026 | AI finds its foothold in private equity, but mostly in due diligence | Post-Trade 360 | press | https://posttrade360.com/news/fund-ops/ai-finds-its-foothold-in-private-equity-but-mostly-in-due-diligence/ | 2026-04-13 | full |
| DELOITTE-GENAIMA-2025 | Deloitte Survey: 86% of Corporate and Private Equity Leaders Now Use Generative AI... | Deloitte US | survey | https://www.deloitte.com/us/en/about/press-room/deloitte-survey-genai-in-mna.html | 2025-10-09 | full |
| DELOITTE-MAPLATFORM-2026 | Deloitte Expands AI and Agentic AI Capabilities With M&A Platform... | Deloitte US | firm | https://www.deloitte.com/us/en/about-us/press-room/deloitte-announces-ma-platform.html | 2026-09-22 | full |
| DELOITTE-PULSE-2026 | 2026 Generative AI in M&A Pulse Study | Deloitte US | survey | https://www.deloitte.com/us/en/what-we-do/capabilities/mergers-acquisitions-restructuring/articles/m-and-a-generative-ai-study.html | 2026 (page undated) | full |
| DATASITE-NEWDEALTEAM-2026 | Datasite: AI Is Becoming Indispensable in Dealmaking, But Trust and Governance Will Determine the Winners | Datasite (GlobeNewswire) | survey | https://www.finanznachrichten.de/nachrichten-2026-07/68975080-datasite-ai-is-becoming-indispensable-in-dealmaking-but-trust-and-governance-will-determine-the-winners-399.htm | 2026-07-08 | full |
| INTRALINKS-AIDEAL-2026 | AI Use Permeates Dealmaking Despite Operational Concerns: SS&C Intralinks Report | SS&C Intralinks (Business Wire via Nasdaq) | survey | https://www.nasdaq.com/press-release/ai-use-permeates-dealmaking-despite-operational-concerns-ssc-intralinks-report-2026 | 2026-04-08 | full |
| AM-EURODD-2026 | European Due Diligence Report 2026 (as summarised in search results) | Alvarez & Marsal | survey | https://www.alvarezandmarsal.com/node/96976 | 2026-08-11 | search-only (page returned 403) |
| PWC-TOLTIQ-2026 | Reimagining deals for the Age of AI: PwC and ToltIQ enter strategic relationship | PwC US | firm | https://www.pwc.com/us/en/about-us/newsroom/press-releases/reimagining-deals-for-the-age-of-ai.html | 2026-06-15 | full (via mirror) |
| BLOCKCHAINNEWS-PWCUK-2026 | PwC Leverages AI for Faster Deal Execution | Blockchain.News | press | https://blockchain.news/news/pwc-ai-deal-execution | 2026-05-06 | full |
| EY-DILIGENCEEDGE-2026 | Diligence Edge: AI Diligence Platform | EY-Parthenon | firm | https://www.ey.com/en_uk/services/strategy/dilligence-edge | 2026-10-20 (access date; undated) | full (via mirror) |
| CFODIVE-ACCENTURE-2026 | GenAI gains ground in M&A, but post-deal adoption lags | CFO Dive | press | https://www.cfodive.com/news/generative-ai-gains-ground-mergers-postdeal-adoption-lags/814895/ | 2026-03-17 | full |
| CFODIVE-MCKINSEY-2026 | Generative AI reduces M&A costs by 20%, McKinsey says | CFO Dive | press | https://www.cfodive.com/news/generative-ai-reduces-merger-acquisition-costs-20percent-mckinsey/812514/ | 2026-02-18 (page metadata; page also shows a Jan. 13, 2026 byline on a related item) | full |
| BAIN-GENAIMA-2025 | Generative AI in M&A: You're Not Behind-Yet | Bain & Company | firm | https://www.bain.com/insights/generative-ai-m-and-a-report-2025/ | 2025-02-04 | full |
| KJK-NDA-2026 | AI and M&A NDAs: Managing Artificial Intelligence Risks in Confidentiality Agreements | Kohrman Jackson & Krantz | firm | https://kjk.com/2026/03/12/ai-and-ma-ndas-managing-artificial-intelligence-risks-in-confidentiality-agreements/ | 2026-03-12 | full |
| FASKEN-RWI-2026 | When AI meets RWI in M&A | Fasken | firm | https://www.fasken.com/en/knowledge/2026/08/when-ai-meets-rwi-in-ma-what-impact-will-ai-have-on-representation-and-warranty-insurance | 2026-08-13 | full (via mirror) |
| WORKWISE-QOE-2026 | The Best AI Tools for Quality of Earnings and Financial Due Diligence in 2026 | WorkWise Solutions | vendor | https://workwisesolutions.org/guides/best-ai-qoe-financial-due-diligence-tools.html | 2026-07-20 | full |
| CTACQ-QOE-2026 | 2026 QoE Provider Comparison: 18 Firms Ranked by Price & Sector | CT Acquisitions (M&A advisory marketing page) | vendor | https://www.ctacquisitions.com/guides/qoe-provider-comparison-2026/ | 2026-05-16 (updated 2026-10-14) | full (opening only) |
| THIRDBRIDGE-PEDD-2026 | PE due diligence with AI: The complete workflow (2026 guide) | Third Bridge | vendor | https://www.thirdbridge.com/en-us/about-us/media/perspectives/ai-due-diligence-private-equity | 2026 (page undated) | full |
| SEARCHFUNDER-SOURCETABLE-2025 | Has anyone used Sourcetable AI for QoE Analysis? | Searchfunder | community | https://searchfunder.com/post/has-anyone-used-sourcetable-ai-for-qoe-analysis | 2025-10 (approximate) | full (via mirror; 8 comments behind login) |
| SEARCHFUNDER-COLUMBIA-2026 | Columbia Team working on Cheaper Quality of Earnings Reports | Searchfunder | community | https://www.searchfunder.com/post/columbia-team-working-on-cheaper-quality-of-earnings-reports | 2026-06 (approximate) | full (via mirror; 12 comments behind login) |
| SEARCHFUNDER-QOEAGENT-2026 | QoEAgent AI: AI Proof of Cash and Quality of Earnings for LMM Diligence | Searchfunder (vendor-authored) | community | https://searchfunder.com/post/qoeagent-ai-ai-proof-of-cash-quality-of-earnings-for-lmm-diligence | 2026-08 (approximate) | full (via mirror) |
| ECIS-PMI-2026 | From Knowledge Loss To Knowledge Leverage: How Gen AI Affordances Transform Post-Merger IS Integration | ECIS 2026 Proceedings | academic | https://aisel.aisnet.org/ecis2026/is_adopt/is_adopt/24/ | 2026 | full (abstract) |
| ARXIV-KIM-2024 | Financial Statement Analysis with Large Language Models (withdrawn) | arXiv | academic | https://arxiv.org/abs/2407.17866 | 2024-07-25 (withdrawn 2025-02-20) | full (abstract) |
| ARTLAW-AG-2024 | AG Proves LLMs Can Do Well On Due Diligence | Artificial Lawyer | press | https://www.artificiallawyer.com/2024/10/08/ag-proves-llms-can-do-well-on-due-diligence/ | 2024-10-08 | full |
| ICAEW-BIGSIX-2024 | Insight: AI and the Big Six | ICAEW Corporate Financier | professional-body | https://www.icaew.com/technical/corporate-finance/corporate-finance-faculty/corporate-financier/2024/articles/december/insight-ai-and-the-big-six | 2024-12-10 | full |
| JOFA-CS100-2024 | Clarification proposed for CPAs' financial statement preparation engagements | Journal of Accountancy (AICPA & CIMA) | professional-body | https://www.journalofaccountancy.com/news/2024/sep/updates-cpa-consulting-services/ | 2024-09-20 | full |
| PEASEBELL-2026 | AI in Transaction Advisory | Pease Bell CPAs | firm | https://www.peasebell.com/insights/artificial-intelligence-in-transaction-advisory/ | 2026-02-27 | full (via mirror) |
| GC-ETHOS-JOB-2026 | Expert Opportunity - Transaction Advisory Services Manager | Ethos via General Catalyst job board | job-posting | https://jobs.generalcatalyst.com/companies/ethos-2-e1b0048b-7d7c-4a76-97d7-b71911ec294a/jobs/86831351-expert-opportunity-transaction-advisory-services-manager-100-hr-up-to-2-000-week | 2026-07-18 | full |
| EY-JOB-2026 | EYP Associate/Senior Associate - Financial Diligence (Kuala Lumpur) | EY | job-posting | https://careers.ey.com/ey/job/Kuala-Lumpur-EYP-Associate-Senior-Associate-Financial-Diligence-Fede-50490/1214314201/ | 2026-10-09 | full (first part of posting) |
| ACG-DEALMAX-2026 | ACG Sets New Benchmark with Largest, Most Efficient DealMAX to Date | Association for Corporate Growth | conference | https://www.acg.org/news-trends/news/acg-sets-new-benchmark-largest-most-efficient-dealmax-date | 2026-04-29 | full |
| CITYAM-DELOITTEAU-2025 | Deloitte refunds Australian government after AI 'made up citations' in report | City AM | press | https://www.cityam.com/?p=2367690 | 2025-10-06 | full |
| GT-PEAI-2026 | Private equity insights: 2026 AI Impact Survey | Grant Thornton | firm | https://grantthornton.com/insights/survey-reports/private-equity/2026/private-equity-insights-2026-ai-impact-survey | 2026 (publication date not found) | full (summary only) |

(CITYAM-DELOITTEAU-2025 is cited in use case 12 and section 4; section 4 uses the same ref.)

**Counts by type (46 distinct sources; 45 full, 1 search-only):** firm 11 (FORVIS-QOE-2026, FORVIS-AIBUYSIDE-2024, FORVISGROUP-OPIO-2026, DELOITTE-MAPLATFORM-2026, PWC-TOLTIQ-2026, EY-DILIGENCEEDGE-2026, BAIN-GENAIMA-2025, KJK-NDA-2026, FASKEN-RWI-2026, PEASEBELL-2026, GT-PEAI-2026); vendor 10; press 8; survey 6; community 3; academic 2; professional body 2; job posting 2; regulator 1; conference 1. Search-only item: AM-EURODD-2026. Finsider.ai's launch release was seen as a lead only (page returned not found) and is not counted or cited as evidence.

---

## 6. Gaps

- **No quality evidence.** No error rate, override rate, parallel-run result, inspection finding or independent accuracy test for AI-assisted QoE or financial due diligence. All speed figures (27%, 80%, 24 hours, 21-30%) are vendor-published or self-reported, with no method.
- **No A-grade use case.** The strongest measures are adjacent (law-firm contract review accuracy) or are usage counts (ToltIQ, Deloitte platform).
- **Mid-market accounting firms are nearly invisible.** Only Miller Cooper Ltd. (Audit Sight customer quote) and Pease Bell (generic article) appear. I found no named RSM, Baker Tilly, CohnReznick, Marcum, Citrin Cooperman, CBIZ or Crowe transaction advisory AI tool, deployment or case study.
- **Big Four coverage is announcement-level.** KPMG deal advisory and EY deployments have no opened primary source beyond a product page and a 2024 magazine piece. A PwC UK account is secondary. The Deloitte platform and PwC relationship release no outcomes.
- **Sources not reachable.** Finsider.ai launch release (page not found; the vendor's own site timed out); A&M European Due Diligence Report (403, summary only via search); Accenture's source report and the Datasite and Intralinks full reports (only press releases read); the SBA SOP document text (download returned an error; QoE clause read only through vendor pages); EY's US product page (rendered only through the mirror); the Withum and Pease Bell pages through plain curl (Cloudflare blocks); SearchFunder comments behind login.
- **Podcasts and conference sessions.** No podcast on AI in transaction advisory was found. ACG DealMAX 2026 agenda, ENGAGE and AICPA FVS session lists with TAS content were not reachable; the DealMAX recap names no AI session. Conference evidence is therefore limited to one recap.
- **Standards and regulators.** No statement from the AICPA, IESBA, PCAOB or SEC on AI in transaction advisory. The AICPA consulting standard was read only through a Journal of Accountancy article. Independence limits for diligence services to audit clients were not verified.
- **Insurers and lenders.** No source on how R&W underwriters or lenders treat AI-assisted QoE reports, beyond the SBA clause as read through a vendor.
- **Date uncertainty.** SearchFunder posts are dated from relative timestamps (approximate). The Deloitte pulse page, ECIS paper and Grant Thornton PE survey page carry no publication date I could confirm. CFO Dive's McKinsey article shows 2026-02-18 in metadata and a Jan. 13 byline in an adjacent item. The Datasite page lists related coverage dated before the release.
- **Figure conflicts.** S&P diligence integration: 31% in the release versus 'just shy of one in four' in a trade summary (release used). Shepi price: $1,000 on its page versus $2,000 in a search listing. Opio's funding round is called seed in one source and Series A in another (seen in search only, not used).
- **Out of scope here.** Valuation, tax, forensic and firm-operations material noted in section 4 was routed, not researched.

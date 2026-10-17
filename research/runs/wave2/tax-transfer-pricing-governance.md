# Transfer pricing, governance angle: what constrains and measures AI use

- **Archetype:** tax
- **Module:** transfer-pricing (policy, benchmarking and comparables searches, intercompany agreements, local and master files, CbCR, intragroup services, operational TP, APAs and disputes)
- **Angle:** governance (regulator and tax-authority statements, professional-body guidance, standards, academic work, surveys and benchmarks)
- **Prepared:** 2026-10-17 (wave 2). Web search budget was exhausted partway through; later gaps are listed in section 6.

## 1. Summary

- **No regulator has issued TP-specific AI rules.** The binding constraints are the existing ones: IRS Circular 230 duties as restated in OPR Alert 2026-19 (24 Jun 2026), the section 6662(e) documentation regime, expert-evidence rules, and the UK, Australian and AICPA professional-conduct guidance. The only TP-specific regulator statement found is from the IRS LB&I director of treaty and transfer pricing operations (29 Jul 2026): AI can support but not replace judgment, and expert witnesses must explain inputs, assumptions, methods and AI tools (IRS-LBI-TP-2026, reported by EY).
- **The OECD is the one standard-setter touching the module, and from the other direction.** Its June 2026 draft of revised Chapter VII (intra-group services) has 21 new examples, and Bloomberg Tax reports companies, including AstraZeneca, asking the OECD to clarify how AI transactions between affiliates are characterised. The OECD draft itself was not reachable (site blocks bots), so its AI examples are unverified.
- **Evidence on quality is almost absent.** No survey, error rate, override rate or parallel run specific to AI in TP was found. The measurements that exist are independent but adjacent: TIGTA on IRS exam-selection models (2025), GAO on IRS AI governance (2026), and TaxCalcBench on return calculation (2025). TP-specific "results" are practitioner estimates at a conference (PwC Singapore, about 80% of comparability work, 100 hours to about 30 minutes) and vendor claims.
- **Qualitative failure modes are consistent across firm sources.** BDO Canada reports recurring gaps in AI-generated TP documentation: functional profiles that miss operational reality, unsupported method selection, shallow benchmarking, and thin DEMPE treatment. Andersen Australia warns of false confidence. These match what the IRS says it wants in documentation (IRS-TPFAQ-2026).
- **Tax authorities are the other half of the governance story.** Hungary's 2026 inspection plan, as summarised by WTS, uses AI-based models to select TP audit targets. The IRS uses machine learning to select large-partnership and international-risk cases. KPMG authors say South Africa and Nigeria have not confirmed AI-driven TP audits. Independent oversight finds the IRS lacks processes to show its models beat prior methods (TIGTA-2025).
- **Use cases: 17.** Grades: A 0, B 2, C 12, D 3. Both B entries are authority-side. No A is supportable because no TP-specific outcome has been measured by a named organisation.

## 2. Use cases

```yaml
- id: tax-transfer-pricing-01
  title: AI-assisted comparables search and screening for TP benchmarking
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  work_types: [research-synthesis, data-reporting]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Benchmarking requires searching databases and company websites one at a time, screening on functional criteria (for example no material intangibles) and documenting the rejection logic. It is slow and costly."
  solution: "AI ranks or screens candidate comparables from a functional profile instead of industry codes alone, and gathers company information in parallel. A practitioner reviews the screen, the rejections and the adjustments. Exactera describes ExactMatch as ranking companies by comparability; PwC Singapore speakers describe giving AI detailed screening instructions."
  outcomes:
    - lever: speed
      description: "PwC Singapore speakers at a Singapore programme said AI may complete about 80% of the comparability-analysis work and that an analysis once needing up to 100 hours can, under certain conditions, take about 30 minutes. Both are the speakers' views, not a study."
      figure: "about 80% of comparability-analysis work; up to 100 hours to about 30 minutes"
      measures: "Share of the work in a comparability analysis that historically consumed practitioners' time which AI may complete (speaker's view); manual hours for one analysis versus time with AI under certain conditions. No sample, no error rate."
      provenance: self-reported
      source_ref: DDTC-PWCSG-2026
    - lever: quality
      description: "BDO Canada reports benchmarking outputs from AI that lack depth, screening rationale or adjustments. No rate is given."
      figure: "none published"
      measures: "Qualitative observation by BDO Canada of recurring gaps; no denominator."
      provenance: self-reported
      source_ref: BDO-AIGOV-2026
  prerequisites:
    - "Clean, reliable input data; the PwC speaker summarised the dependency as AI being good if the data is good (DDTC-PWCSG-2026)."
    - "A closed or private AI environment, because of confidentiality of company data (DDTC-PWCSG-2026; IBFD-ITPJ-2025 abstract covers set-up of private GenAI tools)."
    - "Access to licensed financial databases for the underlying comparables data (not stated in the sources; the sources do not say how AI tools connect to them)."
  risks_and_guardrails:
    - "The IRS expects documentation to address all comparability criteria, the effect of risk and function differences, and reasoned adjustments (IRS-TPFAQ-2026, Q4). An AI screen that cannot show its rejection logic fails that expectation."
    - "Section 6662(e) documentation does not automatically protect against penalties; it must also be adequate and reasonable (IRS-TPFAQ-2026, preamble). Practitioners remain responsible for due diligence and for understanding AI limits under Circular 230 sections 10.22 and 10.35 (IRS-OPR-2026)."
    - "ABA panel framing: reliability and defensibility of AI-generated analyses is an open question (ABA-MAYMTG-2026)."
  human_checkpoints:
    - "Practitioner approves the search strategy, screening criteria and each rejection."
    - "Practitioner reviews comparability adjustments and the final interquartile range."
  role_evolution: "PwC Singapore speakers said the remaining crucial 20% still needs human perspective (DDTC-PWCSG-2026). They did not describe staffing changes."
  evidence_grade: C
  sources:
    - { ref: DDTC-PWCSG-2026, title: "Challenges in Transfer Pricing Benchmarking Changes in the AI Era", publisher: DDTCNews, type: conference, url: "https://news.ddtc.co.id/en/insight/1822922/challenges-in-transfer-pricing-benchmarking-changes-in-the-ai-era", date: 2026-10-01, access: full, locator: "paragraphs on Falgun Thakkar and Jimit Parikh (WU-TA Advanced TP Programme 2026, Singapore)" }
    - { ref: EXACTERA-2025, title: "AI is transforming transfer pricing (advertising supplement)", publisher: "The Tax Adviser (Exactera)", type: vendor, url: "https://www.thetaxadviser.com/issues/2025/sep/ai-is-transforming-transfer-pricing/", date: 2025-08-31, access: full, locator: "Q&A 2, ExactMatch" }
    - { ref: BDO-AIGOV-2026, title: "AI governance in transfer pricing: Is your documentation CRA-ready?", publisher: BDO Canada, type: firm, url: "https://www.bdo.ca/insights/ai-governance-in-transfer-pricing-how-to-create-defensible-documentation", date: 2026-08-20, access: full, locator: "section 'How is AI being used', list of recurring gaps" }
    - { ref: IRS-TPFAQ-2026, title: "Transfer pricing documentation best practices FAQs", publisher: IRS, type: regulator, url: "https://www.irs.gov/businesses/international-businesses/transfer-pricing-documentation-best-practices-frequently-asked-questions-faqs", date: 2026-06-28, access: full, locator: "preamble; Q4" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory Framework items 1 and 3" }
    - { ref: ABA-MAYMTG-2026, title: "ABA Section of Taxation May Meeting 2026 agenda", publisher: ABA Section of Taxation, type: conference, url: "https://sitepilot11.firmseek.com/client/chamberlain/www/media/event/657_ABA_Section_of_Taxation_2026_May_Meeting_Agenda.pdf", date: 2026-05-08, access: full, locator: "Transfer Pricing program, 4:15 PM session, p. 34" }
  last_reviewed: 2026-10-17
  notes: "Grade C: the only figures are a conference speaker's estimates and a vendor description. The IBFD abstract is paywalled beyond its overview."

- id: tax-transfer-pricing-02
  title: AI-assisted drafting of TP documentation (local file, master file, TP report narrative)
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "TP reports, local files and master files are long, repetitive and country-specific, and are updated every year."
  solution: "GenAI drafts sections such as industry and economic analysis, summarises transaction flows and promotes consistency across jurisdictions; a TP professional validates and owns the conclusions. KPMG's article says GenAI can automate documentation including functional, industry and comparable analyses. BDO lists drafting, summarising and preliminary benchmarking among current uses."
  outcomes:
    - lever: quality
      description: "BDO Canada says it is seeing recurring gaps in AI-generated TP outputs: functional profiles not reflecting operational reality, unsupported method selection, benchmarking lacking depth, oversimplified intangibles and DEMPE treatment, and documentation that looks complete but lacks audit-ready support. No incidence is given."
      figure: "none published"
      measures: "Qualitative observation; no sample or rate."
      provenance: self-reported
      source_ref: BDO-AIGOV-2026
  prerequisites:
    - "Strong data foundation and controls over inputs (BDO-AIGOV-2026)."
    - "Data supplied to the IRS in a functional format that preserves calculations, and a clear intercompany transaction summary, which the IRS says speeds review (IRS-TPFAQ-2026, Q5 and Q6)."
    - "Enterprise-approved AI only; no client data to unsecured sites (IRS-OPR-2026, item 6)."
  risks_and_guardrails:
    - "Documentation must be in existence when the return is filed and provided on request to avoid the net adjustment penalty; the IRS can still find it inadequate (IRS-TPFAQ-2026; BTAX-GT6662-2024). No source tests how AI-drafted documentation fares under these rules."
    - "Written advice must rest on reasonable assumptions and verified inputs; opaque logic may make reliance unreasonable (IRS-OPR-2026, item 5, section 10.37)."
    - "In Canada, BDO frames the risk as adjustments, penalties, interest and double taxation if gaps surface in a CRA audit (BDO-AIGOV-2026)."
    - "The EU AI Act and data protection law treatment of AI in TP is described as unsettled (INTERTAX-SIVA-2026 abstract)."
  human_checkpoints:
    - "TP professional validates functional profile against how the business actually operates."
    - "Sign-off on method selection and benchmarking."
    - "Review of every AI-created passage before delivery to the client or authority (IRS-OPR-2026, item 1)."
  role_evolution: "BDO says people remain accountable for the judgment that makes documentation defensible (BDO-AIGOV-2026). Andersen asks who in a company will own AI-assisted documentation if the preparer is not a TP specialist (ANDERSEN-AI-2026)."
  evidence_grade: C
  sources:
    - { ref: KPMG-TP-2025, title: "GenAI Revolutionizes Transfer Pricing and Valuation", publisher: KPMG US, type: firm, url: "https://kpmg.com/us/en/articles/2025/genai-revolutionizes-transfer-pricing-valuation.html", date: 2025, access: full, locator: "opening paragraph" }
    - { ref: BDO-AIGOV-2026, title: "AI governance in transfer pricing: Is your documentation CRA-ready?", publisher: BDO Canada, type: firm, url: "https://www.bdo.ca/insights/ai-governance-in-transfer-pricing-how-to-create-defensible-documentation", date: 2026-08-20, access: full, locator: "'How is AI being used' and 'recurring gaps' list" }
    - { ref: IRS-TPFAQ-2026, title: "Transfer pricing documentation best practices FAQs", publisher: IRS, type: regulator, url: "https://www.irs.gov/businesses/international-businesses/transfer-pricing-documentation-best-practices-frequently-asked-questions-faqs", date: 2026-06-28, access: full, locator: "Q4, Q5, Q6" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "items 1, 5, 6" }
    - { ref: BTAX-GT6662-2024, title: "IRS Transfer Pricing Enforcement Trend Calls for Self-Assessment", publisher: Bloomberg Tax (author Steven C. Wrappe, Grant Thornton), type: firm, url: "https://news.bloombergtax.com/tax-insights-and-commentary/irs-transfer-pricing-enforcement-trend-calls-for-self-assessment", date: 2024-09-23, access: full, locator: "section on Section 6662 penalties" }
    - { ref: INTERTAX-SIVA-2026, title: "AI in Transfer Pricing: Risk or Opportunity?", publisher: "Intertax 54(6/7) (Pramod Siva)", type: academic, url: "https://kluwerlawonline.com/journalarticle/Intertax/54.6/TAXI2026050", date: 2026-06-01, access: full, locator: "abstract (full text paywalled)" }
    - { ref: ANDERSEN-AI-2026, title: "AI in Transfer Pricing: Insight, Illusion and Risk", publisher: Andersen Australia, type: firm, url: "https://au.andersen.com/ai-in-transfer-pricing/", date: 2026-02-17, access: full, locator: "section 'Our View on the Use of AI'" }
  last_reviewed: 2026-10-17
  notes: "No named organisation with a deployment and no measurement. Maturity 'emerging' because BDO describes market use without naming users. The KPMG page date is shown as 2025 from its URL path; page metadata shows 2026-10-12, likely a modification date."

- id: tax-transfer-pricing-03
  title: AI-prepared functional analysis and DEMPE support
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Functional, asset and risk analysis, and DEMPE assessment of intangibles, depend on interviews and documents and are the part of a TP file authorities most often probe."
  solution: "AI drafts functional analyses from available documents and notes for a TP professional to test against how functions, risks and decisions occur in practice. BDO lists functional analyses among AI uses and says AI cannot determine whether arrangements reflect practice."
  outcomes:
    - lever: quality
      description: "BDO Canada says AI can draft documentation that aligns with contractual arrangements but cannot determine whether they reflect where key functions, risks and decisions sit in practice; it names tech, life sciences and manufacturing as sectors where the gap is likely to matter."
      figure: "none published"
      measures: "Qualitative statement; no sample."
      provenance: self-reported
      source_ref: BDO-AIGOV-2026
  prerequisites:
    - "Operational facts gathered from the business, not only contracts (BDO-AIGOV-2026)."
    - "Intercompany agreements and risk allocation that agree with the functional analysis; the IRS names inconsistency between risk analysis and agreements as a documentation weakness (IRS-TPFAQ-2026, Q4)."
  risks_and_guardrails:
    - "Generic functional profiles that mirror contract form rather than operational reality (BDO-AIGOV-2026)."
    - "Transfer pricing is judgment-intensive; an AI system that misses one relevant factor may systematically mischaracterise legitimate arrangements (BTAX-AFRICA-2026, written about authority-side AI but the same limit applies)."
  human_checkpoints:
    - "TP professional validates functional profile with business interviews."
    - "DEMPE conclusions reviewed by a senior practitioner."
  role_evolution: "No source describes role change for this step."
  evidence_grade: C
  sources:
    - { ref: BDO-AIGOV-2026, title: "AI governance in transfer pricing: Is your documentation CRA-ready?", publisher: BDO Canada, type: firm, url: "https://www.bdo.ca/insights/ai-governance-in-transfer-pricing-how-to-create-defensible-documentation", date: 2026-08-20, access: full, locator: "'Industry lens' section" }
    - { ref: IRS-TPFAQ-2026, title: "Transfer pricing documentation best practices FAQs", publisher: IRS, type: regulator, url: "https://www.irs.gov/businesses/international-businesses/transfer-pricing-documentation-best-practices-frequently-asked-questions-faqs", date: 2026-06-28, access: full, locator: "Q4, risk analysis consistent with intercompany agreements" }
    - { ref: BTAX-AFRICA-2026, title: "South Africa and Nigeria Drive AI-Enabled Transfer Pricing Audits", publisher: "Bloomberg Tax (authors from KPMG South Africa and Nigeria)", type: firm, url: "https://news.bloomberglaw.com/tax-insights-and-commentary/south-africa-and-nigeria-drive-ai-enabled-transfer-pricing-audits", date: 2026-06-08, access: full, locator: "'Emerging AI dilemma' section" }
  last_reviewed: 2026-10-17
  notes: "Grade C because the only support is a firm's list of uses and observed shortcomings."

- id: tax-transfer-pricing-04
  title: AI review of TP documentation for country requirements and cross-report consistency
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: "Local files must meet country-specific rules that change often, and authorities compare figures across local files, master files, CbC reports and income tax returns. Mismatches invite scrutiny."
  solution: "A Word-based reviewer checks documentation against country requirements and suggests edits (Exactera ExactReport, offered through an early adopter programme). KPMG South Africa and Nigeria authors advise reconciling data across financial statements, local and master files, CbC reports, VAT and income tax filings to avoid automated flags."
  outcomes:
    - lever: quality
      description: "Exactera says ExactReport reviews documentation for country-specific requirements and offers real-time modifications where sections are insufficient. No result is reported."
      figure: "none published"
      measures: "Product description in an advertising supplement."
      provenance: vendor-published
      source_ref: EXACTERA-2025
  prerequisites:
    - "Consistent underlying data across financial statements, TP files, CbC reports, VAT and income tax returns (BTAX-AFRICA-2026)."
    - "A maintained source of local requirements; the Exactera interviewee notes OECD guidelines are not law and local rules change (EXACTERA-2025)."
  risks_and_guardrails:
    - "A reviewer tool does not make documentation adequate; the IRS says even complete section 6662(e) documentation is assessed for adequacy and reasonableness (IRS-TPFAQ-2026)."
    - "Vendor claim in a sponsored supplement; not independently tested (EXACTERA-2025)."
  human_checkpoints:
    - "TP lead accepts or rejects each suggested change."
    - "Reconciliation breaks are explained by a person before filing."
  role_evolution: "Exactera expects tax professionals to spend less time on repetitive tasks and more on analysis (EXACTERA-2025); this is the vendor's expectation."
  evidence_grade: C
  sources:
    - { ref: EXACTERA-2025, title: "AI is transforming transfer pricing (advertising supplement)", publisher: "The Tax Adviser (Exactera)", type: vendor, url: "https://www.thetaxadviser.com/issues/2025/sep/ai-is-transforming-transfer-pricing/", date: 2025-08-31, access: full, locator: "Q&A 2 and 3, ExactReport" }
    - { ref: BTAX-AFRICA-2026, title: "South Africa and Nigeria Drive AI-Enabled Transfer Pricing Audits", publisher: "Bloomberg Tax (authors from KPMG South Africa and Nigeria)", type: firm, url: "https://news.bloomberglaw.com/tax-insights-and-commentary/south-africa-and-nigeria-drive-ai-enabled-transfer-pricing-audits", date: 2026-06-08, access: full, locator: "'What Can Multinationals Do?', data integrity and documentation consistency" }
    - { ref: IRS-TPFAQ-2026, title: "Transfer pricing documentation best practices FAQs", publisher: IRS, type: regulator, url: "https://www.irs.gov/businesses/international-businesses/transfer-pricing-documentation-best-practices-frequently-asked-questions-faqs", date: 2026-06-28, access: full, locator: "preamble" }
  last_reviewed: 2026-10-17

- id: tax-transfer-pricing-05
  title: AI drafting and abstraction of intercompany agreements and transaction flows
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  work_types: [document-production, research-synthesis]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Intercompany agreements must match the risk allocation and pricing in the TP policy and the real flows. Large agreement sets are hard to draft, update and check."
  solution: "AI drafts intercompany agreements, summarises transaction flows, and extracts pricing, scope, IP and risk clauses from contracts and invoices for checking against the TP policy. BDO lists drafting agreements among uses. Exactera's interviewee says agents can read contracts and invoices and extract information."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "No measurement found."
      provenance: self-reported
      source_ref: BDO-AIGOV-2026
  prerequisites:
    - "Agreements and risk allocation that the actual conduct supports; the IRS says risk analysis should be consistent with intercompany agreements (IRS-TPFAQ-2026, Q4)."
  risks_and_guardrails:
    - "Substance over form: authorities look beyond written contracts (BTAX-AFRICA-2026). KPMG authors say South African authorities could use NLP to flag clauses on pricing, scope, IP and risk allocation, so poorly aligned agreements may be flagged."
    - "Confidentiality of agreements entered into public AI tools (IRS-OPR-2026, item 6)."
  human_checkpoints:
    - "Legal and TP review of each draft against actual conduct."
  role_evolution: "No source describes role change."
  evidence_grade: C
  sources:
    - { ref: BDO-AIGOV-2026, title: "AI governance in transfer pricing: Is your documentation CRA-ready?", publisher: BDO Canada, type: firm, url: "https://www.bdo.ca/insights/ai-governance-in-transfer-pricing-how-to-create-defensible-documentation", date: 2026-08-20, access: full, locator: "list of uses" }
    - { ref: EXACTERA-2025, title: "AI is transforming transfer pricing (advertising supplement)", publisher: "The Tax Adviser (Exactera)", type: vendor, url: "https://www.thetaxadviser.com/issues/2025/sep/ai-is-transforming-transfer-pricing/", date: 2025-08-31, access: full, locator: "Q&A 2" }
    - { ref: BTAX-AFRICA-2026, title: "South Africa and Nigeria Drive AI-Enabled Transfer Pricing Audits", publisher: "Bloomberg Tax (authors from KPMG South Africa and Nigeria)", type: firm, url: "https://news.bloomberglaw.com/tax-insights-and-commentary/south-africa-and-nigeria-drive-ai-enabled-transfer-pricing-audits", date: 2026-06-08, access: full, locator: "South Africa: AI in audit initiation and document review" }
    - { ref: IRS-TPFAQ-2026, title: "Transfer pricing documentation best practices FAQs", publisher: IRS, type: regulator, url: "https://www.irs.gov/businesses/international-businesses/transfer-pricing-documentation-best-practices-frequently-asked-questions-faqs", date: 2026-06-28, access: full, locator: "Q4" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "item 6" }
  last_reviewed: 2026-10-17

- id: tax-transfer-pricing-06
  title: Continuous operational TP monitoring of intercompany flows
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "TP positions are set annually and tested after year end, so margin drift against policy is found late, when true-ups and adjustments are harder."
  solution: "ML or agent-based monitoring watches intercompany transactions and flags invoices, margins or restructurings that fall out of range against policy, so teams can adjust during the year. A sponsored Nexdigm piece describes this as 'agentic monitoring'. A peer-reviewed-style survey article reports MNEs applying ML to operational TP monitoring and predictive compliance controls."
  outcomes:
    - lever: risk
      description: "The Intertax article lists faster benchmarking and documentation, predictive compliance controls and more consistent policy application as measurable opportunities drawn from the literature; the abstract gives no figures."
      figure: "none published"
      measures: "Literature review abstract; no figures."
      provenance: independent
      source_ref: INTERTAX-SIVA-2026
  prerequisites:
    - "Data governance is named as the critical constraint: TP data spread across ERPs, entity structures, agreements and functional analyses is rarely clean (ITR-NEXDIGM-2026)."
    - "KPMG Greece advises automated data collection, cloud platforms and real-time data access to compute transfer prices and identify risk areas (KPMG-GR-2026)."
  risks_and_guardrails:
    - "Source is a sponsored piece by a service provider; its claims that platforms already do this are unquantified (ITR-NEXDIGM-2026)."
    - "The Intertax author concludes AI is a net opportunity only as decision support under human-in-the-loop safeguards with explainability, audit trails and periodic bias review (INTERTAX-SIVA-2026)."
  human_checkpoints:
    - "Professionals decide what to do about a flagged position (ITR-NEXDIGM-2026 says the decision still belongs to professionals)."
  role_evolution: "ITR-NEXDIGM-2026 argues the work shifts from annual retrospective justification to continuous compliance; this is a sponsor's view."
  evidence_grade: C
  sources:
    - { ref: ITR-NEXDIGM-2026, title: "Transfer pricing at the crossroads: disruption, data, and the decade ahead (sponsored)", publisher: "International Tax Review (Nexdigm)", type: vendor, url: "https://www.internationaltaxreview.com/article/2gxa3xiio1u5wu2o18y68/sponsored/transfer-pricing-at-the-crossroads-disruption-data-and-the-decade-ahead", date: 2026-09-21, access: full, locator: "section 'When AI enters - on both sides of the table'" }
    - { ref: INTERTAX-SIVA-2026, title: "AI in Transfer Pricing: Risk or Opportunity?", publisher: "Intertax 54(6/7) (Pramod Siva)", type: academic, url: "https://kluwerlawonline.com/journalarticle/Intertax/54.6/TAXI2026050", date: 2026-06-01, access: full, locator: "abstract" }
    - { ref: KPMG-GR-2026, title: "Ensuring Robust, Relevant, and Fit-for-Purpose Transfer Pricing", publisher: KPMG Greece, type: firm, url: "https://kpmg.com/gr/en/insights/2026/03/ensuring-robust-relevant-and-fit-for-purpose-transfer-pricing.html", date: 2026-03-02, access: full, locator: "closing recommendations paragraph" }
  last_reviewed: 2026-10-17
  notes: "Intertax full text was not reachable; only the abstract was read."

- id: tax-transfer-pricing-07
  title: Pre-filing audit-risk scoring of intercompany positions against authority indicators
  archetype: tax
  module: transfer-pricing
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Authorities select TP audits on indicators such as routine entities running at a loss or very low profit, low income tax relative to revenue, or revenue almost wholly from related parties. Taxpayers rarely test their own positions against these before filing."
  solution: "Taxpayer-side analytics score intercompany positions against known authority selection patterns and the IRS self-assessment suggestions (sensitivity analysis, several profit level indicators), so documentation can be strengthened before filing. Exactera says AI can predict where a taxpayer is most vulnerable to audits and adjustments."
  outcomes:
    - lever: risk
      description: "none published. Exactera claims prediction of audit vulnerability; no accuracy is reported."
      figure: "none published"
      measures: "No measurement found."
      provenance: vendor-published
      source_ref: EXACTERA-2025
  prerequisites:
    - "Knowledge of the indicators in use. Examples: Hungary's 2026 plan targets routine manufacturing, distribution or service entities at a loss or with extremely low profitability (WTS-NAV-2026); the Philippine BIR memorandum order uses indicators such as sustained net losses with large revenue, income tax due below 2% of gross sales, and related-party-dependent revenue, per Grant Thornton Philippines (GT-BIR-2026)."
  risks_and_guardrails:
    - "The IRS says self-assessment helps anticipate questions but its documentation features provide no safe harbour against examination or penalties (IRS-TPFAQ-2026, Q2 and Q5)."
    - "Authority indicators are published by secondary sources and may change; the Philippine framework is described as system-assisted analytics, not specified as AI (GT-BIR-2026)."
  human_checkpoints:
    - "TP lead decides whether a flagged position needs more documentation, a price change or an APA."
  role_evolution: "No source describes role change."
  evidence_grade: C
  sources:
    - { ref: EXACTERA-2025, title: "AI is transforming transfer pricing (advertising supplement)", publisher: "The Tax Adviser (Exactera)", type: vendor, url: "https://www.thetaxadviser.com/issues/2025/sep/ai-is-transforming-transfer-pricing/", date: 2025-08-31, access: full, locator: "Q&A 1" }
    - { ref: IRS-TPFAQ-2026, title: "Transfer pricing documentation best practices FAQs", publisher: IRS, type: regulator, url: "https://www.irs.gov/businesses/international-businesses/transfer-pricing-documentation-best-practices-frequently-asked-questions-faqs", date: 2026-06-28, access: full, locator: "Q1, Q2, Q5" }
    - { ref: WTS-NAV-2026, title: "2026 tax inspection plan of the Hungarian tax authority", publisher: WTS Klient, type: firm, url: "https://wtsklient.hu/en/2026/03/12/2026-tax-inspection-plan-of-the-hungarian-tax-authority/", date: 2026-03-12, access: full, locator: "'Strengthening of transfer pricing audits'" }
    - { ref: GT-BIR-2026, title: "Transfer pricing consideration in BIR's new audit selection process", publisher: Grant Thornton Philippines, type: firm, url: "https://www.grantthornton.com.ph/insights/articles-and-updates1/lets-talk-tp/transfer-pricing-consideration-in-birs-new-audit-selection-process/", date: 2026-02-24, access: full, locator: "discussion of RMO No. 1-2026 triggers" }
  last_reviewed: 2026-10-17

- id: tax-transfer-pricing-08
  title: Grounded AI research assistant for TP law, guidance and compliance questions
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  work_types: [research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "TP rules, OECD guidance and local requirements differ by jurisdiction and change often; finding the right authority is slow."
  solution: "TP Aurora, launched by Aibidia and IBFD on 22 May 2025, answers TP questions from IBFD's curated data on legislation, benchmarking guidelines and compliance insights; a trial was offered. The IBFD journal article covers set-up of private GenAI tools and the credibility and security of outputs."
  outcomes:
    - lever: speed
      description: "none published; the launch release makes qualitative claims of speed, accuracy and clarity."
      figure: "none published"
      measures: "Launch announcement; no measurement."
      provenance: vendor-published
      source_ref: AIBIDIA-IBFD-2025
  prerequisites:
    - "Licensed curated content as the grounding source (AIBIDIA-IBFD-2025)."
  risks_and_guardrails:
    - "Independent testing of TP-specific assistants was not found."
    - "Credibility and security of AI-generated outputs are the article's stated challenges (IBFD-ITPJ-2025)."
    - "Practitioners must understand AI limits and verify citations (IRS-OPR-2026, items 1 and 3)."
  human_checkpoints:
    - "Practitioner checks the cited source before relying on an answer."
  role_evolution: "No source describes role change."
  evidence_grade: C
  sources:
    - { ref: AIBIDIA-IBFD-2025, title: "Aibidia and IBFD Launch TP Aurora", publisher: IBFD, type: vendor, url: "https://www.ibfd.org/news/aibidia-and-ibfd-launch-tp-aurora-groundbreaking-ai-transfer-pricing-research-assistant", date: 2025-05-22, access: full, locator: "body of release" }
    - { ref: IBFD-ITPJ-2025, title: "Operationalizing Transfer Pricing with Generative Artificial Intelligence: Practical Applications and Challenges", publisher: "International Transfer Pricing Journal 32(6) (D. Olzhabayeva)", type: academic, url: "https://shop.ibfd.org/journal/operationalizing-transfer-pricing-generative-artificial-intelligence-practical-applications", date: 2025-09-26, access: full, locator: "overview (abstract only; article paywalled)" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "items 1 and 3" }
  last_reviewed: 2026-10-17

- id: tax-transfer-pricing-09
  title: Business-side self-service AI Q&A on TP documentation requirements
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  work_types: [client-interaction, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Non-specialist finance staff and clients need a first answer on TP requirements before engaging a specialist."
  solution: "Businesses query general AI platforms about TP requirements. Andersen Australia tested one on Australian documentation requirements and published the transcript; it found the answers well structured but warned the tool cannot own the conclusion."
  outcomes:
    - lever: experience
      description: "Andersen reports that over six months more businesses turned to AI for technical expertise, and that an AI assistant produced a structured, risk-differentiated outline of documentation requirements. No rate is given."
      figure: "none published"
      measures: "Single-test transcript and firm observation; no sample."
      provenance: self-reported
      source_ref: ANDERSEN-AI-2026
  prerequisites:
    - "A named owner within the organisation who interrogates assumptions and signs off (ANDERSEN-AI-2026)."
  risks_and_guardrails:
    - "False confidence: detailed, well-structured answers may be taken as accurate and definitive (ANDERSEN-AI-2026)."
    - "Possible oversight of subtle risk indicators or fact-specific misapplication (ANDERSEN-AI-2026)."
  human_checkpoints:
    - "Specialist review before any position or document is relied on."
  role_evolution: "Andersen sees AI raising baseline client knowledge and the quality of questions put to advisers (ANDERSEN-AI-2026)."
  evidence_grade: C
  sources:
    - { ref: ANDERSEN-AI-2026, title: "AI in Transfer Pricing: Insight, Illusion and Risk", publisher: Andersen Australia, type: firm, url: "https://au.andersen.com/ai-in-transfer-pricing/", date: 2026-02-17, access: full, locator: "sections 'The Rise of AI-Assisted Expertise' and 'The Execution Gap'" }
  last_reviewed: 2026-10-17
  notes: "Firm marketing page; the test is a single conversation."

- id: tax-transfer-pricing-10
  title: AI-assisted responses to audit information requests using prior documentation
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  work_types: [document-production, research-synthesis]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Audit and controversy responses require reading years of prior files and formulating consistent answers under deadline."
  solution: "KPMG says GenAI can contribute to TP controversy by reviewing historical documents and formulating responses. The IRS says organised, user-friendly documentation with a summary of intercompany transactions helps examiners focus and can improve the chance of issue deselection."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "Firm claim; no measurement."
      provenance: vendor-published
      source_ref: KPMG-TP-2025
  prerequisites:
    - "Organised historical files and calculations kept in functional formats (IRS-TPFAQ-2026, Q5)."
  risks_and_guardrails:
    - "Written advice and filings need verified facts and citations (IRS-OPR-2026, items 1 and 5)."
    - "Tax Court practice shows the cost of unverified AI output: in Clinco the court found three of four cited cases likely LLM hallucinations and issued a warning, not formal sanctions (TAXCT-CLINCO-2026)."
  human_checkpoints:
    - "Controversy lead reviews every statement of fact and every citation before submission."
  role_evolution: "No source describes role change."
  evidence_grade: C
  sources:
    - { ref: KPMG-TP-2025, title: "GenAI Revolutionizes Transfer Pricing and Valuation", publisher: KPMG US, type: firm, url: "https://kpmg.com/us/en/articles/2025/genai-revolutionizes-transfer-pricing-valuation.html", date: 2025, access: full, locator: "opening paragraph" }
    - { ref: IRS-TPFAQ-2026, title: "Transfer pricing documentation best practices FAQs", publisher: IRS, type: regulator, url: "https://www.irs.gov/businesses/international-businesses/transfer-pricing-documentation-best-practices-frequently-asked-questions-faqs", date: 2026-06-28, access: full, locator: "Q1, Q5, Q6" }
    - { ref: TAXCT-CLINCO-2026, title: "A recipe for sanctions: AI-hallucinated citations in tax", publisher: Journal of Accountancy, type: regulator, url: "https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/", date: 2026-09-01, access: full, locator: "discussion of Clinco v. Commissioner, T.C. Memo. 2026-16" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "items 1 and 5" }
  last_reviewed: 2026-10-17

- id: tax-transfer-pricing-11
  title: AI-assisted economic analysis for TP controversy and expert reports, with disclosure of tools
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  work_types: [expert-judgment, document-production]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Expert economists run benchmarking, valuation and allocation models for litigation and appeals. If AI is used, the reliability of the output becomes an evidence question."
  solution: "Experts may use AI for parts of the analysis. The IRS LB&I official said experts must explain processes, including inputs, assumptions, methods and AI tools, and that the IRS wants to see formulas to test them. Proposed Federal Rule of Evidence 707 would require machine output offered without a sponsoring expert to meet the Rule 702 reliability criteria; it was sent back for revision in June 2026."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "No measurement; the sources are regulator remarks and a rulemaking status."
      provenance: independent
      source_ref: IRS-LBI-TP-2026
  prerequisites:
    - "Validation and explainability materials for any AI-based analysis offered in court, which the Proskauer commentary says litigators should prepare (PROSKAUER-707-2026)."
    - "Spreadsheets or models that show formulas and preserve calculations (IRS-LBI-TP-2026; IRS-TPFAQ-2026, Q5)."
  risks_and_guardrails:
    - "The IRS official said AI can support but not replace legal, economic and factual judgment (IRS-LBI-TP-2026)."
    - "Proposed Rule 707 is not adopted: the Standing Committee decided on 3-4 June 2026 not to recommend action at this time (PROSKAUER-707-2026)."
    - "ABA panel scope included the reliability and defensibility of AI-generated analyses and the balance between GenAI automation and professional judgment (ABA-MAYMTG-2026)."
  human_checkpoints:
    - "The testifying expert must be able to explain and defend every input, assumption and method."
  role_evolution: "The IRS expectation puts personal accountability on the expert, not the tool (IRS-LBI-TP-2026)."
  evidence_grade: D
  sources:
    - { ref: IRS-LBI-TP-2026, title: "Report on recent US international tax developments, 31 July 2026", publisher: "EY Tax News (reporting IRS LB&I remarks of 29 Jul 2026)", type: regulator, url: "https://taxnews.ey.com/news/2026-1658-report-on-recent-us-international-tax-developments-31-july-2026", date: 2026-07-31, access: full, locator: "paragraphs 1-2 under the IRS AI in transfer pricing item" }
    - { ref: PROSKAUER-707-2026, title: "Machine-Generated Evidence Challenges the Federal Rules: Inside the Contested Proposed FRE 707", publisher: Proskauer Rose, type: firm, url: "https://www.proskauer.com/blog/machine-generated-evidence-challenges-the-federal-rules-inside-the-contested-proposed-federal-rule-of-evidence-707", date: 2026-07, access: full, locator: "timeline and 'Divided Opinions' sections" }
    - { ref: ABA-MAYMTG-2026, title: "ABA Section of Taxation May Meeting 2026 agenda", publisher: ABA Section of Taxation, type: conference, url: "https://sitepilot11.firmseek.com/client/chamberlain/www/media/event/657_ABA_Section_of_Taxation_2026_May_Meeting_Agenda.pdf", date: 2026-05-08, access: full, locator: "p. 34, panel description" }
  last_reviewed: 2026-10-17
  notes: "Idea: discussed by an IRS official, an ABA panel and a law-firm commentary; no deployment or measurement found. The IRS remark is a statement of expectation, reported second-hand by EY. The proskauer.com page carries no visible date; 2026-07 is from the lexblog syndication path (2026/07/29)."

- id: tax-transfer-pricing-12
  title: Authority-side ML selection of large-corporate and international-risk cases (IRS)
  archetype: tax
  module: transfer-pricing
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "The IRS has had too few resources to assess risks relating to large corporations and complex structures, and high no-change rates mean audits that burden compliant taxpayers."
  solution: "The IRS says it uses AI and advanced analytics to select complex partnerships for audit, with machine learning applied to risk in partnership tax, general income tax and accounting, and international tax. TIGTA reviewed the LB&I and SB/SE AI models used to select returns and issues for examination. IRS also names large corporations suspected of TP tactics as recipients of non-audit alternative interventions such as compliance alerts."
  outcomes:
    - lever: quality
      description: "TIGTA found the IRS has not established processes to evaluate whether AI model performance is better than prior methods or achieves intended objectives, so it cannot readily show the models improve examination compliance work. TIGTA made three recommendations (use exam results in model monitoring, evaluate ensemble machine learning, and set a measurement plan including drift); the IRS agreed with all three, two subject to staffing constraints and expected Treasury guidance."
      figure: "3 recommendations; IRS agreed with all 3"
      measures: "TIGTA recommendations on LB&I and SB/SE AI return and issue selection models, and the IRS response. Not specific to TP."
      provenance: independent
      source_ref: TIGTA-2025
    - lever: risk
      description: "GAO counted 126 active IRS AI use cases in the June 2025 inventory, including 65 too sensitive or exempt R&D for public reporting, up from 10 in August 2022; over 25 percent of use cases did not say how they would benefit the agency; one group said it lost 63 employees who worked on AI full or part time."
      figure: "126 use cases (65 non-public); over 25% without benefit information; 63 staff lost"
      measures: "GAO: active AI use cases in the IRS inventory as of June 2025; share of inventory entries lacking benefit information; employees in the Research, Applied Analytics and Statistics group who worked on AI full or part time and were lost."
      provenance: independent
      source_ref: GAO-2026
  prerequisites:
    - "Examination results fed back into models, and a measurement plan with metrics to monitor benefit and correct drift (TIGTA-2025)."
    - "An AI skills plan and complete use-case inventory (GAO-2026 recommendations)."
  risks_and_guardrails:
    - "Werfel framework risks for tax authorities include hallucination, drift and explainability, with illustrative controls such as audit logs linking outputs to inputs (AICPA-WERFEL-2026, Appendix A)."
    - "Fairness: the IRS acknowledged research finding that Black taxpayers were three to five times more likely to be audited (IRS-SOP-2024). This relates to individuals, not TP."
  human_checkpoints:
    - "Examiners and managers decide whether to open an examination; the sources do not detail the review step for TP issues."
  role_evolution: "GAO links staff reductions to a shortage of skilled employees to support or develop AI tools (GAO-2026)."
  evidence_grade: B
  sources:
    - { ref: TIGTA-2025, title: "The IRS Could Leverage Examination Results in AI Examination Case Selection Models and Improve Processes to Evaluate Performance (2025-308-022)", publisher: TIGTA, type: regulator, url: "https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf", date: 2025-05-19, access: full, locator: "Highlights page and memorandum, Figure 2 discussion" }
    - { ref: GAO-2026, title: "Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522)", publisher: GAO, type: regulator, url: "https://www.gao.gov/products/gao-26-107522", date: 2026-03-24, access: full, locator: "What GAO Found; Recommendations (read via text mirror)" }
    - { ref: IRS-SOP-2024, title: "IRS IRA Strategic Operating Plan, Annual Update Supplement (Pub. 3744-A)", publisher: IRS, type: regulator, url: "https://www.irs.gov/pub/irs-pdf/p3744a.pdf", date: 2024-04, access: full, locator: "pp. 36-38: 'Alternative Interventions' and 'Leveraging Data and AI'" }
    - { ref: AICPA-WERFEL-2026, title: "A Risk Framework for the Use of AI in Tax Administration and Preparation (appendices)", publisher: "AICPA, The Tax Adviser (Danny Werfel)", type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: 2026-06, access: full, locator: "Appendix A, risks 1-3" }
  last_reviewed: 2026-10-17
  notes: "Grade capped at B: the measurements concern IRS selection models and the AI programme generally, not TP case selection. The IRS Supplement and the GAO report do not say whether any model targets TP issues specifically; the only TP reference is the compliance-alert sentence."

- id: tax-transfer-pricing-13
  title: Authority-side AI and real-time data to select TP audit targets (Hungary)
  archetype: tax
  module: transfer-pricing
  function: risk-compliance-legal
  work_types: [review-assurance, transaction-processing]
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Tax authorities want to find TP risk earlier and with less manual selection."
  solution: "WTS summarises Hungary's 2026 inspection plan: audit targets will be chosen even more through data-driven processes using AI and real-time information, and the authority uses AI-based analytical models and real-time data processing to filter high-risk companies, even at the moment an invoice is issued. TP is a priority, targeting routine-function entities at a loss or very low profit. Audits can also be launched from CbC reports and international data exchange."
  outcomes:
    - lever: risk
      description: "none published. WTS expects a further increase in TP inspections compared with 2025."
      figure: "none published"
      measures: "No figures in the source."
      provenance: self-reported
      source_ref: WTS-NAV-2026
  prerequisites:
    - "Real-time invoice and transaction data feeds to the authority (WTS-NAV-2026)."
  risks_and_guardrails:
    - "Single secondary source summarising the authority's plan; the plan itself was not read."
    - "KPMG authors warn that AI-driven risk assessment could systematically mischaracterise legitimate arrangements and call for SOPs defining which data indicators trigger enhanced review (BTAX-AFRICA-2026, Nigeria section)."
  human_checkpoints:
    - "Not described. WTS says cooperative taxpayers who make mistakes will continue to receive support, with fast and firm action for repeated non-compliance."
  role_evolution: "No source describes role change for Hungarian auditors."
  evidence_grade: B
  sources:
    - { ref: WTS-NAV-2026, title: "2026 tax inspection plan of the Hungarian tax authority", publisher: WTS Klient, type: firm, url: "https://wtsklient.hu/en/2026/03/12/2026-tax-inspection-plan-of-the-hungarian-tax-authority/", date: 2026-03-12, access: full, locator: "paragraphs under 'Strengthening of transfer pricing audits'" }
    - { ref: BTAX-AFRICA-2026, title: "South Africa and Nigeria Drive AI-Enabled Transfer Pricing Audits", publisher: "Bloomberg Tax (authors from KPMG South Africa and Nigeria)", type: firm, url: "https://news.bloomberglaw.com/tax-insights-and-commentary/south-africa-and-nigeria-drive-ai-enabled-transfer-pricing-audits", date: 2026-06-08, access: full, locator: "Nigeria section, 'Key Considerations'" }
  last_reviewed: 2026-10-17
  notes: "Grade B rests on a named authority's stated practice, reported second-hand."

- id: tax-transfer-pricing-14
  title: Authority-side NLP review of TP documentation, benchmarking studies and intercompany agreements
  archetype: tax
  module: transfer-pricing
  function: risk-compliance-legal
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "Tax authorities must read large volumes of agreements, invoices, memos, policies and TP files at audit initiation."
  solution: "KPMG South Africa and Nigeria authors describe how AI-powered risk engines and NLP could flag high-risk multinationals by checking consistency across financial statements, returns, TP documentation and intercompany agreements, and how OCR plus NLP could extract and classify clauses in audit document review. They say SARS has not openly confirmed GenAI use in audits, and that no evidence shows Nigeria has deployed an advanced AI-driven TP audit system."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "No measurement; prospective description."
      provenance: self-reported
      source_ref: BTAX-AFRICA-2026
  prerequisites:
    - "Consolidated, high-quality tax data; Nigeria's migration of TP filings to one platform is described as foundational (BTAX-AFRICA-2026)."
  risks_and_guardrails:
    - "KPMG authors call for taxpayer rights to challenge assumptions, human-in-the-loop review, data governance, pre-audit dialogue and internal SOPs for AI-supported audits (BTAX-AFRICA-2026)."
    - "The ABA panel scope included the likelihood that authorities deploy similar technologies (ABA-MAYMTG-2026). Aprio says authorities including the IRS, HMRC and ATO have begun integrating AI into TP audits but cites only an IRS plan on partnership audit targeting (APRIO-AI-2025)."
  human_checkpoints:
    - "Audit officials interview the taxpayer and decide on adjustments (BTAX-AFRICA-2026)."
  role_evolution: "No source describes role change."
  evidence_grade: D
  sources:
    - { ref: BTAX-AFRICA-2026, title: "South Africa and Nigeria Drive AI-Enabled Transfer Pricing Audits", publisher: "Bloomberg Tax (authors from KPMG South Africa and Nigeria)", type: firm, url: "https://news.bloomberglaw.com/tax-insights-and-commentary/south-africa-and-nigeria-drive-ai-enabled-transfer-pricing-audits", date: 2026-06-08, access: full, locator: "South Africa section" }
    - { ref: APRIO-AI-2025, title: "AI and the Future of Transfer Pricing: Risks and Opportunities", publisher: Aprio, type: firm, url: "https://www.aprio.com/ai-and-the-future-of-transfer-pricing-risks-and-opportunities-ins-article-intl/", date: 2025-08-14, access: full, locator: "section 'AI tools for worldwide taxing authorities'" }
    - { ref: ABA-MAYMTG-2026, title: "ABA Section of Taxation May Meeting 2026 agenda", publisher: ABA Section of Taxation, type: conference, url: "https://sitepilot11.firmseek.com/client/chamberlain/www/media/event/657_ABA_Section_of_Taxation_2026_May_Meeting_Agenda.pdf", date: 2026-05-08, access: full, locator: "p. 34, panel description" }
  last_reviewed: 2026-10-17
  notes: "Idea: practitioners discuss it; no confirmed authority deployment of document-reading AI for TP was found. ITR-NEXDIGM-2026 (sponsored) asserts authorities are deploying AI agent frameworks for TP audits but names none, so it is not used as support."

- id: tax-transfer-pricing-15
  title: AI-assisted APA and MAP preparation, and outcome prediction
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  work_types: [expert-judgment, research-synthesis]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "APAs and MAP cases are lengthy negotiations; KPMG authors expect APAs to become more attractive as audit technology advances."
  solution: "Aprio says some authorities are developing proprietary AI models to predict outcomes in MAP and APA processes, without naming any. KPMG authors recommend bilateral APAs to gain certainty. The UN draft protocol on dispute prevention and resolution lists APAs among proposed mechanisms (EY)."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "No measurement."
      provenance: self-reported
      source_ref: APRIO-AI-2025
  prerequisites:
    - "Consistent documentation and data across reporting layers (BTAX-AFRICA-2026)."
  risks_and_guardrails:
    - "Unattributed claim about authority models (APRIO-AI-2025)."
    - "Opacity of AI logic makes the arm's length principle difficult to validate (APRIO-AI-2025)."
  human_checkpoints:
    - "Negotiation and position-setting remain with practitioners and competent authorities; Nexdigm's sponsored piece says no algorithm will sit opposite a revenue officer (ITR-NEXDIGM-2026)."
  role_evolution: "No source describes role change."
  evidence_grade: D
  sources:
    - { ref: APRIO-AI-2025, title: "AI and the Future of Transfer Pricing: Risks and Opportunities", publisher: Aprio, type: firm, url: "https://www.aprio.com/ai-and-the-future-of-transfer-pricing-risks-and-opportunities-ins-article-intl/", date: 2025-08-14, access: full, locator: "section 'AI tools for worldwide taxing authorities'" }
    - { ref: BTAX-AFRICA-2026, title: "South Africa and Nigeria Drive AI-Enabled Transfer Pricing Audits", publisher: "Bloomberg Tax (authors from KPMG South Africa and Nigeria)", type: firm, url: "https://news.bloomberglaw.com/tax-insights-and-commentary/south-africa-and-nigeria-drive-ai-enabled-transfer-pricing-audits", date: 2026-06-08, access: full, locator: "'What Can Multinationals Do?', APA programs" }
    - { ref: IRS-LBI-TP-2026, title: "Report on recent US international tax developments, 31 July 2026", publisher: "EY Tax News", type: regulator, url: "https://taxnews.ey.com/news/2026-1658-report-on-recent-us-international-tax-developments-31-july-2026", date: 2026-07-31, access: full, locator: "UN draft protocol paragraph" }
    - { ref: ITR-NEXDIGM-2026, title: "Transfer pricing at the crossroads (sponsored)", publisher: "International Tax Review (Nexdigm)", type: vendor, url: "https://www.internationaltaxreview.com/article/2gxa3xiio1u5wu2o18y68/sponsored/transfer-pricing-at-the-crossroads-disruption-data-and-the-decade-ahead", date: 2026-09-21, access: full, locator: "paragraph beginning 'None of this should be read as a claim'" }
  last_reviewed: 2026-10-17
  notes: "Idea. No APA or MAP deployment of AI was found."

- id: tax-transfer-pricing-16
  title: Cross-tax agent review of intercompany transactions (TP, VAT, withholding, customs)
  archetype: tax
  module: transfer-pricing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "The same intercompany transaction has TP, VAT, withholding tax and customs consequences handled by different teams, so inconsistencies show up late."
  solution: "A sponsored Nexdigm article says multi-agent workflows can review a transaction's TP, VAT, withholding tax and customs implications at once and identify inconsistencies across reporting lines before they become audit issues."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Sponsored claim; no measurement."
      provenance: vendor-published
      source_ref: ITR-NEXDIGM-2026
  prerequisites:
    - "Clean data across ERPs, entities and agreements (ITR-NEXDIGM-2026)."
  risks_and_guardrails:
    - "Sponsored source with no named customer; treat as an unverified capability claim."
  human_checkpoints:
    - "Professionals decide on the resolution of any inconsistency."
  role_evolution: "No source describes role change."
  evidence_grade: C
  sources:
    - { ref: ITR-NEXDIGM-2026, title: "Transfer pricing at the crossroads: disruption, data, and the decade ahead (sponsored)", publisher: "International Tax Review (Nexdigm)", type: vendor, url: "https://www.internationaltaxreview.com/article/2gxa3xiio1u5wu2o18y68/sponsored/transfer-pricing-at-the-crossroads-disruption-data-and-the-decade-ahead", date: 2026-09-21, access: full, locator: "paragraph on new generation of AI-powered TP platforms" }
  last_reviewed: 2026-10-17
  notes: "The VAT and customs parts may route to the indirect-tax module."

- id: tax-transfer-pricing-17
  title: AI-use and verification log embedded in TP workpapers
  archetype: tax
  module: transfer-pricing
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "If an AI-assisted TP position is challenged, a firm may not be able to show what the AI suggested versus what a person verified."
  solution: "Maintain a record of which AI tools were used, what inputs were given, and how outputs were reviewed and validated. BDO, the IRS OPR alert and the Werfel preparer risk register all recommend variants of this. The pattern is a governance control, not an automation; it is listed so advisers can ask whether it exists."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Recommended control; no measurement."
      provenance: self-reported
      source_ref: BDO-AIGOV-2026
  prerequisites:
    - "A documented AI use policy covering disclosure, review requirements and documentation standards (AICPA-WERFEL-2026, Appendix C, risk 12)."
  risks_and_guardrails:
    - "Circular 230 section 10.36 expects firm procedures, training, vetting of third-party AI tools and documentation of adherence (IRS-OPR-2026, item 4)."
    - "Fee practice: the OPR alert says billing manual time not actually spent may violate section 10.27 and that savings should be credited openly; the AICPA has asked the IRS for clarification, saying the language does not seem to allow value pricing (IRS-OPR-2026, item 2; AICPA-CART-2026)."
  human_checkpoints:
    - "Reviewer attests to verification of each AI-assisted section."
  role_evolution: "Werfel's preparer register also lists skill erosion, vendor dependence and institutional knowledge loss as workforce risks, with controls such as capability assessments and documented manual workflows (AICPA-WERFEL-2026, Appendix C, risks 13-15)."
  evidence_grade: D
  sources:
    - { ref: BDO-AIGOV-2026, title: "AI governance in transfer pricing: Is your documentation CRA-ready?", publisher: BDO Canada, type: firm, url: "https://www.bdo.ca/insights/ai-governance-in-transfer-pricing-how-to-create-defensible-documentation", date: 2026-08-20, access: full, locator: "'3 ways to build audit-ready AI practices', third principle" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "items 2 and 4; 'Best Practices for Responsible AI Use'" }
    - { ref: AICPA-WERFEL-2026, title: "A Risk Framework for the Use of AI in Tax Administration and Preparation (appendices)", publisher: "AICPA, The Tax Adviser (Danny Werfel)", type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: 2026-06, access: full, locator: "Appendix C, risks 12-15" }
    - { ref: AICPA-CART-2026, title: "AICPA, former IRS commissioner to lead initiative on AI in tax", publisher: "The Tax Adviser (AICPA)", type: professional-body, url: "https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/", date: 2026-09-23, access: full, locator: "final paragraphs" }
    - { ref: PCRT-AI-2026, title: "Professional bodies issue AI advice to members", publisher: "Association of Taxation Technicians (PCRT bodies)", type: standard-setter, url: "https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members", date: 2026-01-19, access: full, locator: "news item body" }
  last_reviewed: 2026-10-17
  notes: "Idea: recommended by firms, a regulator alert and a risk framework; no evidence of adoption rates. Pattern 'other': a control layer wrapped around AI-assisted work. The OPR alert is general to federal tax practice, not TP-specific."
```

## 3. Module notes

### Processes and key steps, with work types

- **Policy design and intercompany agreements:** characterise transactions, choose method, allocate risk, draft agreements (expert-judgment, document-production). Source: IRS-TPFAQ-2026 Q4 (risk analysis must match agreements).
- **Benchmarking and comparables searches:** functional profile, database search, screening, adjustments, range (research-synthesis, data-reporting). Source: DDTC-PWCSG-2026; IRS-TPFAQ-2026 Q4.
- **Documentation (local file, master file, TP report):** functional analysis, industry and economic analysis, method justification (document-production, review-assurance). Source: BDO-AIGOV-2026; KPMG-TP-2025.
- **CbC reporting and data consistency:** reconcile financials, local and master files, CbC reports, VAT and returns (data-reporting). Source: BTAX-AFRICA-2026.
- **Operational TP:** in-year monitoring, true-ups (data-reporting). Source: ITR-NEXDIGM-2026 (sponsored).
- **Intragroup services pricing:** benefit test, cost-plus, shareholder activities (expert-judgment). Source: HLB-CH7-2026.
- **Controversy, APAs and expert evidence:** audit responses, expert reports, MAP/APA (expert-judgment, document-production). Source: IRS-LBI-TP-2026.

### Common pain points

- Slow, costly benchmarking: a PwC Singapore speaker said one analysis once cost tens of thousands of US dollars (DDTC-PWCSG-2026).
- Documentation that looks complete but lacks audit-ready support (BDO-AIGOV-2026) and often fails to give reasoned rejection of specified methods or full comparability analysis (IRS-TPFAQ-2026, Q4).
- Inconsistent data across financial statements, TP files, CbC reports and returns, which authority analytics may flag (BTAX-AFRICA-2026).
- Dispute friction on the benefit test and documentation proportionality in intra-group services, where commenters want evidence guidance without an overly detailed checklist (HLB-CH7-2026).

### Metrics and benchmarks (with provenance)

- **TP-specific adoption rates or error rates: none found.** See gaps.
- PwC Singapore speakers: about 80% of comparability-analysis work; up to 100 hours to about 30 minutes under certain conditions (self-reported, conference, DDTC-PWCSG-2026).
- IRS AI inventory: 126 use cases at June 2025, 65 non-public, over 25% without benefit information (independent, GAO-2026). IRS did not show its selection models beat earlier methods (independent, TIGTA-2025).
- OECD Chapter VII draft: 21 new examples; comments due 22 Jul 2026; public submissions published 24 Aug 2026; consultation meeting scheduled for November 2026 (HLB-CH7-2026; PWCDE-CH7-2026).
- Penalty exposure: section 6662(e) net adjustment penalty is avoided only with adequate, timely documentation (IRS-TPFAQ-2026). A Grant Thornton author reports the IRS asserting penalties in Newell Brands and Airbnb cases (Sep 2024, BTAX-GT6662-2024).
- Adjacent accuracy benchmark: models computed fewer than a third of simplified federal income tax returns correctly (TaxCalcBench, independent academic, COLUMN-TAXCALCBENCH-2025). Not TP, and the authors' company sells a deterministic engine.

### Guardrails and regulatory points

- **US practitioner conduct:** Circular 230 sections 10.22 (due diligence), 10.27 (fees), 10.35 (competence), 10.36 (firm procedures), 10.37 (written advice), and IRC 6713 and 7216 on return-information disclosure (IRS-OPR-2026).
- **US documentation:** section 6662(e) and Treas. Reg. 1.6662-6 documentation must support a reasonable method and application; documentation does not guarantee penalty protection (IRS-TPFAQ-2026).
- **Expert evidence:** IRS expects experts to explain inputs, assumptions, methods and AI tools and show formulas (IRS-LBI-TP-2026). Proposed FRE 707 sent back for revision on 3-4 Jun 2026 (PROSKAUER-707-2026).
- **UK:** PCRT topical guidance on AI applies fundamental principles (integrity, due care, confidentiality) (PCRT-AI-2026).
- **Risk frameworks:** Werfel's 20-risk framework, tested by the AICPA's Council on AI Risk in Tax (AICPA-WERFEL-2026; AICPA-CART-2026). The AICPA says AI moves too fast for lasting standards (landscape-tax.md, from the CART/Werfel coverage).
- **Courts:** Tax Court warning in Clinco on hallucinated citations (TAXCT-CLINCO-2026). An Indian tribunal order recalled after relying on non-existent judgments (ITATONLINE-BUCKEYE-2025); this concerns tax-authority AI misuse, not TP.
- **OECD:** Chapter VII revisions "not intended to change the general principles" (PWCDE-CH7-2026). Firms say AI services may need cost-plus pricing to be tested, but this is secondary and unverified here.

### Frontier signals

- 2026-06-01 to 2026-08-24: OECD Chapter VII consultation with AI-tool examples; AstraZeneca asks for clarity on AI transactions between affiliates (OECD-INTRAGROUP-2026; HLB-CH7-2026).
- 2026-05-08: first ABA panel on AI and section 482 with a listed IRS panelist (ABA-MAYMTG-2026).
- 2026-06-26: Oxford CBT session asks how delegating decisions to AI affects substantive TP law (OXFORD-CBT-2026).
- 2026-07-29: IRS LB&I official sets expert-witness expectations on AI (IRS-LBI-TP-2026).
- 2026-03-12: Hungary 2026 plan uses AI-based models for TP audit selection (WTS-NAV-2026).
- 2026-06-08: KPMG authors describe where AI-enabled TP audits could go in South Africa and Nigeria (BTAX-AFRICA-2026).
- 2026-01-05 (planned): Philippine BIR RMO No. 1-2026 adds TP indicators to analytics-based audit selection (GT-BIR-2026; the date is the memorandum year per the article; no AI claim).

### Workforce and role effects

- PwC Singapore speakers: humans keep the final 20% (DDTC-PWCSG-2026).
- Werfel preparer register: skill erosion, vendor dependence and institutional knowledge loss (AICPA-WERFEL-2026, Appendix C).
- OPR fee guidance: pass AI savings to clients; AICPA asked for clarification (IRS-OPR-2026; AICPA-CART-2026). This affects pricing of TP compliance work.
- GAO: IRS lost skilled AI staff (GAO-2026).
- Andersen: in-house non-TP staff using AI raises the question of who owns the documentation (ANDERSEN-AI-2026).

### Objections and concerns practitioners raise

- False confidence from well-structured output (ANDERSEN-AI-2026).
- Black-box outputs, bias and unsettled EU AI Act treatment (INTERTAX-SIVA-2026).
- Confidentiality of company data in AI tools (DDTC-PWCSG-2026; IRS-OPR-2026).
- Balance of power: whether an AI-assisted authority assessment will carry more weight than a taxpayer's evidence in a dispute (BTAX-AFRICA-2026).
- Proportionality: documentation checklists can raise compliance burden (HLB-CH7-2026).

### Interview probes for an advisor

1. When your team uses AI for a comparables screen, can you reproduce the rejection logic for each excluded company at audit, and who signs it off?
2. Has AI-drafted documentation ever been challenged by an authority or an auditor, and what did the gaps look like (functional profile, method choice, DEMPE)?
3. If an expert on your matter used AI, could you show the inputs, formulas and tool versions the IRS says it wants to test?
4. Which authority indicators do you test your own positions against before filing, and is any of that automated?
5. Where is your AI-use log for TP workpapers, and does your fee model account for AI time savings given the OPR fee language?

## 4. Routed to other modules

- **controversy:** *Clinco v. Commissioner* (TAXCT-CLINCO-2026), the Indian ITAT *Buckeye Trust* recall (ITATONLINE-BUCKEYE-2025), proposed FRE 707 (PROSKAUER-707-2026). Court and tribunal governance beyond TP. IRS selection-model oversight (TIGTA-2025, GAO-2026) also belongs there as tax-authority AI.
- **research-advisory:** PCRT-AI-2026, IRS-OPR-2026 and AICPA-WERFEL-2026 apply across tax advice; TaxCalcBench (COLUMN-TAXCALCBENCH-2025) is about return calculation, so it belongs to compliance.
- **international-pillar-two:** the Pillar One Amount B and UN dispute-prevention protocol items in the EY report (IRS-LBI-TP-2026).
- **indirect-tax:** the VAT and customs parts of tax-transfer-pricing-16.
- **tax-data-technology:** data governance as the critical constraint (ITR-NEXDIGM-2026; KPMG-GR-2026).

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ABA-MAYMTG-2026 | ABA Section of Taxation May Meeting 2026 agenda (TP panel p. 34) | ABA Section of Taxation | conference | https://sitepilot11.firmseek.com/client/chamberlain/www/media/event/657_ABA_Section_of_Taxation_2026_May_Meeting_Agenda.pdf | 2026-05-08 | full |
| IRS-LBI-TP-2026 | Report on recent US international tax developments, 31 July 2026 | EY Tax News (IRS remarks of 2026-07-29) | regulator | https://taxnews.ey.com/news/2026-1658-report-on-recent-us-international-tax-developments-31-july-2026 | 2026-07-31 | full |
| KPMG-TP-2025 | GenAI Revolutionizes Transfer Pricing and Valuation | KPMG US | firm | https://kpmg.com/us/en/articles/2025/genai-revolutionizes-transfer-pricing-valuation.html | 2025 | full |
| KPMG-TPPOD-2026 | Is Adoption of GenAI Redefining Value and TP? (Part 2) | KPMG US | podcast | https://kpmg.com/us/en/podcasts/2026/gen-ai-value-tp-pt2.html | 2026-07-15 | full (page description only; audio not heard) |
| IBFD-ITPJ-2025 | Operationalizing TP with Generative AI | International Transfer Pricing Journal | academic | https://shop.ibfd.org/journal/operationalizing-transfer-pricing-generative-artificial-intelligence-practical-applications | 2025-09-26 | full (abstract) |
| AIBIDIA-IBFD-2025 | Aibidia and IBFD Launch TP Aurora | IBFD | vendor | https://www.ibfd.org/news/aibidia-and-ibfd-launch-tp-aurora-groundbreaking-ai-transfer-pricing-research-assistant | 2025-05-22 | full |
| EXACTERA-2025 | AI is transforming transfer pricing (advertising supplement) | The Tax Adviser (Exactera) | vendor | https://www.thetaxadviser.com/issues/2025/sep/ai-is-transforming-transfer-pricing/ | 2025-08-31 | full |
| OECD-INTRAGROUP-2026 | Companies Want OECD to Clarify Character of AI Transactions | Bloomberg Tax | press | https://news.bgov.com/daily-tax-report/companies-want-oecd-to-clarify-character-of-ai-transactions | 2026-08-25 | full (first paragraphs; paywalled) |
| HLB-CH7-2026 | OECD Proposes Revisions to TP Guidelines on Intra-group Services | HLB Thailand | firm | https://www.hlbthai.com/oecd-proposes-revisions-to-transfer-pricing-guidelines-on-intra-group-services/ | 2026-08-31 | full |
| PWCDE-CH7-2026 | OECD: Public consultation on Transfer Pricing Guidelines | PwC Germany | firm | https://blogs.pwc.de/en/german-tax-and-legal-news/article/255082/oecd-public-consultation-on-transfer-pricing-guidelines/ | 2026-06-10 | full |
| IRS-OPR-2026 | Alert 2026-19, Introductory Guidelines for Responsible AI Use in Federal Tax Practice | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| IRS-TPFAQ-2026 | Transfer pricing documentation best practices FAQs | IRS | regulator | https://www.irs.gov/businesses/international-businesses/transfer-pricing-documentation-best-practices-frequently-asked-questions-faqs | 2026-06-28 | full |
| IRS-SOP-2024 | IRS IRA Strategic Operating Plan, Annual Update Supplement (Pub. 3744-A) | IRS | regulator | https://www.irs.gov/pub/irs-pdf/p3744a.pdf | 2024-04 | full |
| TIGTA-2025 | IRS Could Leverage Examination Results in AI Examination Case Selection Models (2025-308-022) | TIGTA | regulator | https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf | 2025-05-19 | full |
| GAO-2026 | AI: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522) | GAO | regulator | https://www.gao.gov/products/gao-26-107522 | 2026-03-24 | full (text mirror) |
| TAXCT-CLINCO-2026 | A recipe for sanctions: AI-hallucinated citations in tax (Clinco, T.C. Memo. 2026-16) | Journal of Accountancy | regulator | https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/ | 2026-09-01 | full |
| PROSKAUER-707-2026 | Machine-Generated Evidence Challenges the Federal Rules: Proposed FRE 707 | Proskauer Rose | firm | https://www.proskauer.com/blog/machine-generated-evidence-challenges-the-federal-rules-inside-the-contested-proposed-federal-rule-of-evidence-707 | 2026-07 | full |
| AICPA-WERFEL-2026 | A Risk Framework for the Use of AI in Tax Administration and Preparation (appendices) | AICPA / The Tax Adviser | professional-body | https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf | 2026-06 | full |
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax | The Tax Adviser | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 | full |
| PCRT-AI-2026 | Professional bodies issue AI advice to members | ATT (PCRT bodies) | standard-setter | https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members | 2026-01-19 | full |
| BTAX-AFRICA-2026 | South Africa and Nigeria Drive AI-Enabled Transfer Pricing Audits | Bloomberg Tax (KPMG authors) | firm | https://news.bloomberglaw.com/tax-insights-and-commentary/south-africa-and-nigeria-drive-ai-enabled-transfer-pricing-audits | 2026-06-08 | full |
| WTS-NAV-2026 | 2026 tax inspection plan of the Hungarian tax authority | WTS Klient | firm | https://wtsklient.hu/en/2026/03/12/2026-tax-inspection-plan-of-the-hungarian-tax-authority/ | 2026-03-12 | full |
| GT-BIR-2026 | Transfer pricing consideration in BIR's new audit selection process | Grant Thornton Philippines | firm | https://www.grantthornton.com.ph/insights/articles-and-updates1/lets-talk-tp/transfer-pricing-consideration-in-birs-new-audit-selection-process/ | 2026-02-24 | full |
| INTERTAX-SIVA-2026 | AI in Transfer Pricing: Risk or Opportunity? (Pramod Siva) | Intertax 54(6/7) | academic | https://kluwerlawonline.com/journalarticle/Intertax/54.6/TAXI2026050 | 2026-06-01 | full (abstract) |
| BDO-AIGOV-2026 | AI governance in transfer pricing: Is your documentation CRA-ready? | BDO Canada | firm | https://www.bdo.ca/insights/ai-governance-in-transfer-pricing-how-to-create-defensible-documentation | 2026-08-20 | full (text mirror) |
| APRIO-AI-2025 | AI and the Future of Transfer Pricing: Risks and Opportunities | Aprio | firm | https://www.aprio.com/ai-and-the-future-of-transfer-pricing-risks-and-opportunities-ins-article-intl/ | 2025-08-14 | full (text mirror) |
| ANDERSEN-AI-2026 | AI in Transfer Pricing: Insight, Illusion and Risk | Andersen Australia | firm | https://au.andersen.com/ai-in-transfer-pricing/ | 2026-02-17 | full |
| DDTC-PWCSG-2026 | Challenges in Transfer Pricing Benchmarking Changes in the AI Era | DDTCNews | conference | https://news.ddtc.co.id/en/insight/1822922/challenges-in-transfer-pricing-benchmarking-changes-in-the-ai-era | 2026-10-01 | full |
| ITR-NEXDIGM-2026 | Transfer pricing at the crossroads (sponsored by Nexdigm) | International Tax Review | vendor | https://www.internationaltaxreview.com/article/2gxa3xiio1u5wu2o18y68/sponsored/transfer-pricing-at-the-crossroads-disruption-data-and-the-decade-ahead | 2026-09-21 | full |
| BTAX-GT6662-2024 | IRS Transfer Pricing Enforcement Trend Calls for Self-Assessment | Bloomberg Tax (Grant Thornton author) | firm | https://news.bloombergtax.com/tax-insights-and-commentary/irs-transfer-pricing-enforcement-trend-calls-for-self-assessment | 2024-09-23 | full |
| KPMG-GR-2026 | Ensuring Robust, Relevant, and Fit-for-Purpose Transfer Pricing | KPMG Greece | firm | https://kpmg.com/gr/en/insights/2026/03/ensuring-robust-relevant-and-fit-for-purpose-transfer-pricing.html | 2026-03-02 | full |
| ITATONLINE-BUCKEYE-2025 | Buckeye Trust v. Registrar, ITAT (Karnataka High Court) digest | itatonline.org | press | https://itatonline.org/digest/verdicts/buckeye-trust-v-registrar-itat/ | 2025-09-18 | full |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task | arXiv (Column Tax) | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 | full (abstract) |
| OXFORD-CBT-2026 | Oxford CBT Summer Conference 2026 booklet, Session 4 | Oxford Centre for Business Taxation | conference | https://oxfordtax.sbs.ox.ac.uk/sitefiles/cbt-summer-conference-booklet-2026 | 2026-06-26 | full |
| IFA-LISBON-2025 | IBFD Dialogues seminar on GenAI for tax professionals | IBFD | conference | https://www.ibfd.org/events/ibfd-dialogues-seminar-ifa-lisbon-2025-0 | 2025-10-06 | full (listing only; no content) |
| ITR-AIFORUM-2025 | ITR AI in Tax Forum speakers | International Tax Review | conference | https://event.internationaltaxreview.com/event/bfd4f100-335f-47de-841d-b03beb6a3d86/speakers | 2025-09-16 | full (speaker list only) |
| OECD-GOVAI-2025 | Governing with AI (OECD), via Grant Thornton Ireland summary | Grant Thornton Ireland | firm | https://www.grantthornton.ie/insights/factsheets/governing-ai-tax-authorities/ | 2025-09-18 | full (summary only) |
| ABA-TT-2026 | Transforming compliance risk management (ABA Tax Times report on the AI and TP panel) | ABA Section of Taxation | professional-body | https://www.americanbar.org/groups/taxation/resources/tax-times/2026/transforming-compliance-risk-management/ | 2026-05 | search-only |

Source type count (distinct sources, 39 including 1 search-only): conference 5, regulator 8, standard-setter 1, professional-body 3 (one search-only), firm 14, vendor 3, academic 3, press 2, podcast 1. No survey sources: none specific to TP were found.

## 6. Gaps

- **No TP-specific survey or benchmark.** No published adoption rate, error rate, override rate, parallel-run result or inspection outcome for AI in TP was found. A search surfaced an aggregator (Stealth Agents) quoting "31% of multinationals have deployed AI for TP documentation; 67% plan to within two years" attributed to Deloitte 2025; it could not be traced to a Deloitte report and is excluded.
- **OECD primary documents not read.** The OECD site blocks bots (including via the text mirror), so the Chapter VII draft, its AI examples and the AstraZeneca submission were read only through Bloomberg Tax (first paragraphs), HLB Thailand and PwC Germany. PwC's own detailed alerts returned 403.
- **IRS LB&I remarks are second-hand** (EY Tax News). I did not find an IRS transcript. The ABA panel agenda lists "Joe Tobin, IRS"; a search result suggested a person of that name now at Deloitte, so his affiliation should be checked before attributing remarks. The ABA Tax Times report on the panel was blocked (search-only).
- **Proposed FRE 707** status comes from one law-firm blog; uscourts.gov was not read.
- **Tax authorities.** No primary statement from HMRC, ATO, BZSt, CBDT or SARS on AI in TP audits was found. Search budget ran out before follow-up searches on each. Hungary and the Philippines are known only through consultancy summaries; the Philippine item does not say AI.
- **Intercompany AI pricing.** OECD examples on AI tools shared between affiliates, and PwC's view that cost-plus pricing of AI-enabled services should be tested, are search-extract level only.
- **Academic.** arXiv has no paper on AI and TP (search of "transfer pricing" returned only unrelated pricing and finance papers). The Intertax article was read as an abstract only. No empirical academic study of AI comparables selection was found.
- **Not read or paywalled:** IBFD article full text, Tax Notes, ITR news, Bloomberg Tax articles beyond their opening, TR/EY/Deloitte surveys (these are general tax surveys listed in landscape-tax.md section 9; none opened for TP content), KPMG TP Minds podcast audio, KPMG Germany master/local file article (404).
- **Dates.** KPMG-TP-2025 is dated 2025 from its URL path; page metadata shows 2026-10-12. PROSKAUER-707-2026 is dated 2026-07 from a syndication path.

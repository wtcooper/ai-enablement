# Deep dive: assurance / specialists (combined angle)

- **Archetype:** assurance
- **Module:** specialists. Using the work of auditor's specialists and management's experts (ISA 620, ISA 500 on management's experts, PCAOB AS 1210, AS 1105 Appendix A and AS 1201 Appendix C), covering valuation, actuarial, tax, forensic and environmental specialists, plus "AI as a specialist-like input" (complex client models, heavy client reliance on AI outputs).
- **Angle:** combined (practice, discourse, governance and evidence)
- **Prepared:** 2026-10-16. **Inputs:** `landscape-assurance.md` (wave 1 rerun), `vocabulary.md`.
- **Method note.** Pages were fetched with `curl` through the session proxy, with `r.jina.ai` as the mirror for sites that block `curl` (BV Resources, Federal Register, Going Concern, Corporate Board Member). PDFs were read with `pdftotext`. Crossref and arXiv metadata were used to reach academic abstracts that SSRN blocks. Each source below is marked `access: full` (opened and read, including abstract-only reads of papers, which are flagged) or `access: search-only` (teaser page or search extract only). Page references for PDFs are PDF page numbers. Quotations are under 25 words.

---

## 1. Summary

- **Evidence is low, as the landscape predicted, and the pattern is specific.** In the sources opened, no audit firm, regulator or standard-setter states that audit-employed valuation, actuarial, tax or forensic specialists use AI on audits. The practice evidence sits on the valuation-provider side (Big Four valuation practices, CohnReznick, valuation software vendors). That side matters to auditors because those providers are often management's experts. Most of it is press-level and has no published measurements.
- **The specialist standards do not mention AI.**
  - ISA (UK) 620 (Revised September 2026) was published on 23 Sep 2026 and applies to audits for periods commencing on or after 15 Dec 2026 (FRC-620NEWS-2026; FRC-620STD-2026, para 4). The change is ethics-driven: it makes explicit that the auditor "shall not use" an expert whose competence or capabilities are lacking, or whose objectivity threats cannot be reduced to an acceptable level (FRC-620STD-2026, para 9A).
  - A keyword search of the standard found no reference to AI. The FRC feedback statement does not mention it either (FRC-620-2026).
  - Of the 49 readable comment letters on the IAASB's April 2025 draft (50 posted; one had no text layer) (IAASB-620ED-2025), one named AI: the Institute of Chartered Accountants of Nigeria asked for AI and machine-learning experts to be added to the application-material examples (ICAN-620-2025). Six letters mention technology as a growing field for experts, among them ICAEW's, which does not name AI (ICAEW-620-2025).
  - The PCAOB's February 2025 specialists Spotlight has no AI content (PCAOB-SPECIALISTS-2025). The PCAOB's technology-assisted-analysis amendments say they do not address artificial intelligence (PCAOB-TAA-2024).
- **The valuation standard-setter is moving first.**
  - The IVSC's July 2025 paper says no model, including an AI model, can produce an IVS-compliant valuation without the valuer's judgment (IVSC-AI-2025, p5).
  - Its January 2026 exposure draft proposes mandatory requirements on "significant use" of AI in scope of work, data and inputs, models, and documentation, plus a new quality-controls chapter (IVSC-IVSED-2026, pp4-5, 13). The IVSC says the next edition would be published on 31 Jan 2027 with an effective date of 31 Jan 2028, subject to responses (IVSC-IVSED-2026, p10).
  - An IVSC Advisory Forum session on AI and practical guidance is scheduled for 17 Nov 2026 (IVSC-AGM-2026).
- **"AI as a specialist-like input" is now named in guidance.** The AICPA practice aid (13 Oct 2026) says that when an entity's AI plays a significant role in financial reporting, considerations may resemble those for external specialists and complex valuation models (AT-AICPAPA-2026). The AUASB (July 2025) adds that restricted access to a third-party AI application's logic, data and assumptions may be a scope limitation (AUASB-AI-2025). Audit partners rate client AI governance as advanced in only 6% of cases (BOARDMEMBER-CAQ-2026).
- **Independent quality evidence is thin but real, and none of it is specialist-specific.**
  - A preregistered randomized field experiment (100 auditors, one unnamed global firm, an inventory valuation task) found a firm-specific LLM improved output quality and cut completion time, but did not improve adherence to internal audit guidelines (SSRN-LLMAQ-2026, abstract only).
  - Benchmarks show agents build financial models far better than they derive company-specific assumptions (ARXIV-GAUGE-2026), and that LLMs are weaker on actuarial case reasoning than on standardized knowledge (ARXIV-INSACTBENCH-2026).
  - The FRC's 2026 inspection review has specialist-related findings and good-practice examples, none tied to AI (FRC-ARAQ-2026).
- **Role effects are mostly about talent, not substitution.** Valuation leaders worry about the junior apprenticeship model (BVR-PANEL-2026). Big Four postings requiring AI expertise rose from under 2% (2022) to nearly 7% (2025), as reported from an FT analysis (COMPUTERWORLD-FT-2026). Audit firms increasingly need data and AI specialists as a new kind of auditor's expert (FRC-ARAQ-2026, p28).

---

## 2. Use cases

Grades: 0 A, 2 B, 5 C, 11 D. Ideas graded D are labelled "idea" and each has a regulator, standard-setter, professional-body, practitioner or academic source that discusses it. Items 07, 15 and 16 carry independent measurements but are graded below A because there is no named-organization deployment in this module's process (see each `notes`).

```yaml
- id: assurance-specialists-01
  title: Valuation analysts use AI to gather data, format it and build routine model components
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [data-reporting, research-synthesis]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Valuation analysts spend many hours importing filings data, adjusting multiples and benchmarking against guideline public companies before judgment work begins [BVR-BIGFOUR-2025]."
  solution: "Big Four valuation practice leaders told the ASA Spring Fair Value Conference in New York that AI is used primarily to automate data gathering, formatting and routine modelling, so analysts can focus on interpretation and judgment. They described AI or RPA tools handling tasks such as importing 10-K data, adjusting multiples and benchmarking against guideline public companies [BVR-BIGFOUR-2025]. A 2026 BVR report on the same conference series says Big Four leaders described AI as accelerating valuation workflows while changing how juniors are trained [BVR-PANEL-2026]."
  outcomes:
    - { lever: capacity, description: "Leaders said routine tasks that took hours of manual effort are increasingly handled by AI or RPA tools; no time or cost figures were given", figure: "none published", measures: "not applicable; qualitative panel statement", provenance: self-reported, source_ref: BVR-BIGFOUR-2025 }
  prerequisites:
    - "Proprietary or approved platforms: panelists said EY is developing a platform (EYQ) because firms do not see public tools as suitable for confidential work [BVR-BIGFOUR-2025]"
  risks_and_guardrails:
    - "Junior staff may miss the learning that came from building models and digging into source data; one panelist said they may miss key learning if they rely on AI results without understanding inputs and assumptions [BVR-BIGFOUR-2025]"
    - "Panelists said final valuations still require human oversight and professional skepticism [BVR-BIGFOUR-2025]"
  human_checkpoints:
    - "Analysts interpret outputs and validate AI-generated results; final valuations stay with people [BVR-BIGFOUR-2025]"
  role_evolution: "Junior staff move toward interpreting outputs, exercising judgment and validating AI-generated results [BVR-BIGFOUR-2025]. A 2026 panel said firms may need to be more intentional about training and mentorship as the apprenticeship model evolves, and some panelists saw juniors reaching substantive analysis sooner [BVR-PANEL-2026]."
  evidence_grade: B
  sources:
    - { ref: BVR-BIGFOUR-2025, title: "Big Four investing heavily in AI", publisher: "Business Valuation Resources (BVWire)", type: press, url: "https://www.bvresources.com/articles/bvwire/big-four-investing-heavily-in-ai", date: 2025-05-21, access: full, locator: "whole article (panelists from PwC, Deloitte, KPMG, EY; moderator from Kroll)" }
    - { ref: BVR-PANEL-2026, title: "Big Four panel: AI is reshaping the valuation talent pipeline", publisher: "Business Valuation Resources (BVWire)", type: press, url: "https://www.bvresources.com/articles/bvwire/big-four-panel-ai-is-reshaping-the-valuation-talent-pipeline", date: 2026-05-20, access: full, locator: "whole article" }
  last_reviewed: 2026-10-16
  notes: "Grade B is capped by adjacency. The panelists spoke for Big Four valuation advisory practices. Neither article says audit-employed valuation specialists use these tools, and no named audit engagement is described. The 2025-05-21 date comes from a search extract; the page itself shows no date. The 2025 conference was in May 2025; BVR's 2026 conference was held 7 May 2026 [BVR-ASA2026-2026]."

- id: assurance-specialists-02
  title: Valuation advisory practice adds AI-driven valuation analytics for private-market valuations
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [data-reporting, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Fund managers are asked for more frequent, faster and more traceable valuations amid investor scrutiny and tougher audit expectations, often without matching budget or headcount [COHNREZNICK-VALUATION-2026]."
  solution: "CohnReznick announced on 26 Mar 2026 that its Valuation Advisory practice is incorporating 73 Strings' valuation analytics into its established methodologies to analyse large data sets, increase consistency across models and give deeper insight into valuation drivers, across private equity, private credit, public company and complex asset classes [COHNREZNICK-VALUATION-2026; CPAPA-COHNREZNICK-2026]."
  outcomes:
    - { lever: quality, description: "The firm says the analytics support faster, more transparent and more defensible valuations; no measurements were published", figure: "none published", measures: "not applicable; firm claim", provenance: self-reported, source_ref: COHNREZNICK-VALUATION-2026 }
  prerequisites:
    - "A third-party analytics platform (73 Strings) integrated into existing valuation methodology [COHNREZNICK-VALUATION-2026]"
  risks_and_guardrails:
    - "The firm says it keeps independence, professional judgment and oversight by its valuation professionals [COHNREZNICK-VALUATION-2026]"
  human_checkpoints:
    - "Valuation professionals retain judgment on complex inputs, scenario analysis and conclusions [COHNREZNICK-VALUATION-2026]"
  role_evolution: "The firm says the technology lets teams spend more time on complex inputs, scenario analysis and defensible conclusions [COHNREZNICK-VALUATION-2026]."
  evidence_grade: C
  sources:
    - { ref: COHNREZNICK-VALUATION-2026, title: "CohnReznick's Valuation Advisory practice enhances valuation services through advanced analytics technology", publisher: "CohnReznick", type: firm, url: "https://www.cohnreznick.com/insights/cohnreznicks-valuation-advisory-enhanced-through-ai-analytics/", date: 2026-03-26, access: full, locator: "press release body" }
    - { ref: CPAPA-COHNREZNICK-2026, title: "CohnReznick's Valuation Advisory Practice Enhances Valuation Services", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2026/03/24/cohnreznicks-valuation-advisory-practice-enhances-valuation-services/180187/", date: 2026-03-24, access: full, locator: "article body" }
  last_reviewed: 2026-10-16
  notes: "Graded C because this is an announcement with no usage detail, so maturity is announced rather than in-production. CohnReznick is a valuation provider to fund clients. In an audit it would typically be management's expert, whose work auditors evaluate under ISA 500 or AS 1105 Appendix A. The release itself cites 'tougher audit expectations'. The firm's release dates from 26 Mar 2026; trade press ran it 24-25 Mar. 73 Strings is a vendor, and no financial terms of the arrangement were found."

- id: assurance-specialists-03
  title: Valuation teams build client-facing sensitivity analyses, dashboards and scenario portals with AI
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [client-interaction, data-reporting]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Valuation deliverables are static reports, so clients cannot easily explore how assumptions change value [BVR-BIGFOUR-2025]."
  solution: "Big Four panelists said AI tools are being developed to enhance client deliverables and interactivity, such as running automated sensitivity analyses, generating dashboards and creating custom scenario modelling portals [BVR-BIGFOUR-2025]."
  outcomes:
    - { lever: experience, description: "none published", figure: "none published", measures: "not applicable", provenance: self-reported, source_ref: BVR-BIGFOUR-2025 }
  prerequisites:
    - "Firm-controlled platforms for confidential client data [BVR-BIGFOUR-2025]"
  risks_and_guardrails:
    - "Panelists said valuations still need human oversight and professional skepticism [BVR-BIGFOUR-2025]"
  human_checkpoints:
    - "Final valuation opinion remains with the valuation professional [BVR-BIGFOUR-2025]"
  role_evolution: "Not described in the source."
  evidence_grade: C
  sources:
    - { ref: BVR-BIGFOUR-2025, title: "Big Four investing heavily in AI", publisher: "Business Valuation Resources (BVWire)", type: press, url: "https://www.bvresources.com/articles/bvwire/big-four-investing-heavily-in-ai", date: 2025-05-21, access: full, locator: "paragraph beginning 'AI tools are also being developed'" }
  last_reviewed: 2026-10-16
  notes: "Weak audit relevance: interactive deliverables change what auditors later receive from a management's expert, not how specialists support the audit. Included because it was reported with the same panel as item 01. The source says 'being developed', so no use is evidenced."

- id: assurance-specialists-04
  title: Valuation software recommends peer companies and transactions with AI
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [research-synthesis, data-reporting]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Selecting comparable companies and transactions is a manual, judgment-heavy step in valuation work [VALUTICO-APR26-2026]."
  solution: "Valutico's April 2026 release adds continuous AI-powered recommendations to improve peer selection, transactions and qualitative assessments, and expanded AI capabilities for financial structuring and reporting [VALUTICO-APR26-2026]. Valutico bought the AI specialist Paraloq Analytics on 24 Jun 2025 to integrate its AI into the platform [VALUTICO-PARALOQ-2025]."
  outcomes:
    - { lever: speed, description: "The vendor says the features help users save time and produce more efficient, data-driven valuations; no figures published", figure: "none published", measures: "not applicable; vendor claim", provenance: vendor-published, source_ref: VALUTICO-APR26-2026 }
  prerequisites:
    - "Vendor platform with uploaded financial statements and supporting documents [VALUTICO-APR26-2026]"
  risks_and_guardrails:
    - "IVS requires the valuer to assess and select data and inputs using professional judgment, so recommendations do not remove the valuer's responsibility [IVSC-AI-2025]"
  human_checkpoints:
    - "Valuer reviews and selects peers and inputs [IVSC-AI-2025]"
  role_evolution: "Not described in the source."
  evidence_grade: C
  sources:
    - { ref: VALUTICO-APR26-2026, title: "April 2026 Masterclass: Powering Smarter, More Connected Valuations", publisher: Valutico, type: vendor, url: "https://help.valutico.com/en/articles/15773327-april-2026-masterclass-powering-smarter-more-connected-valuations", date: 2026-07-01, access: full, locator: "webinar description" }
    - { ref: VALUTICO-PARALOQ-2025, title: "Valutico Acquires AI Innovator Paraloq Analytics to Revolutionize Private Company Analysis", publisher: Valutico, type: vendor, url: "https://valutico.com/valutico-acquires-paraloq-analytics/", date: 2025-06-24, access: full, locator: "press release body" }
    - { ref: IVSC-AI-2025, title: "Navigating the Rise of Artificial Intelligence in Valuation: Opportunities, Risks, and Standards", publisher: "International Valuation Standards Council", type: standard-setter, url: "https://ivsc.org/wp-content/uploads/2025/07/Navigating-the-Rise-of-AI-in-Valuation-Opportunities-Risks-and-Standards.pdf", date: 2025-07-23, access: full, locator: "p4 (IVS 104 quotation)" }
  last_reviewed: 2026-10-16
  notes: "Vendor product description only. The Valutico site lists an 'Audit / Tax / Accounting' industry page, but no named audit-firm customer or use by auditor's specialists was found."

- id: assurance-specialists-05
  title: Valuers use GenAI to draft report sections such as market commentary, and some firms automate report writing
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Valuation reports contain narrative sections (market commentary, descriptions) that take time to write [IVSC-AI-2025]."
  solution: "The IVSC says AI is already frequently used by some valuers to assist report writing, through ChatGPT or other publicly available AI for parts such as market commentary, and that in other cases report writing may be a fully automated process within the firm [IVSC-AI-2025]."
  outcomes:
    - { lever: speed, description: "none published", figure: "none published", measures: "not applicable; standard-setter observation without named organizations", provenance: independent, source_ref: IVSC-AI-2025 }
  prerequisites:
    - "Valuer keeps control of content: materiality and relevance of descriptions, verified data sources, unbiased and accurate facts [IVSC-AI-2025]"
  risks_and_guardrails:
    - "Open-source or some closed-source AI without safeguards may pose client-confidentiality risks and could breach data-protection laws or non-disclosure agreements [IVSC-AI-2025]"
    - "The IVSC sees transparency as a core principle: valuers should state whether, how and why AI was used in the scope of work or documentation [IVSC-AI-2025]"
  human_checkpoints:
    - "Valuer verifies data sources and confirms facts before issuing the report [IVSC-AI-2025]"
  role_evolution: "Not described in the source."
  evidence_grade: C
  sources:
    - { ref: IVSC-AI-2025, title: "Navigating the Rise of Artificial Intelligence in Valuation: Opportunities, Risks, and Standards", publisher: "International Valuation Standards Council", type: standard-setter, url: "https://ivsc.org/wp-content/uploads/2025/07/Navigating-the-Rise-of-AI-in-Valuation-Opportunities-Risks-and-Standards.pdf", date: 2025-07-23, access: full, locator: "pp10-12 (IVS 106 documentation and reporting; transparency; data and inputs)" }
  last_reviewed: 2026-10-16
  notes: "Graded C because the IVSC does not name any organization or give a measure. It reports that the IVSC is aware of valuers 'knowingly or unknowingly' using AI elements (p10), which is itself a risk signal for auditors relying on valuation reports."

- id: assurance-specialists-06
  title: AI-assisted quality-control review of valuation reports (idea)
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [review-assurance]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Valuation reports must use the correct basis of value and be consistent internally, and quality controls are manual [IVSC-AI-2025]."
  solution: "The IVSC paper says AI and other technology could be used in the valuation quality-control process, to review valuation reports for the correct basis of value and for inconsistencies, and to check that the scope of work contains all relevant elements [IVSC-AI-2025]. The IVSC's January 2026 draft would add a new quality-controls chapter (IVS 107) and AI requirements across several chapters [IVSC-IVSED-2026]."
  outcomes:
    - { lever: quality, description: "none published", figure: "none published", measures: "not applicable; idea", provenance: independent, source_ref: IVSC-AI-2025 }
  prerequisites:
    - "Valuation quality-control procedures that an AI check can sit inside (IVS 100) [IVSC-AI-2025]"
  risks_and_guardrails:
    - "The IVSC says IVS may need revising so quality controls include review and challenge of AI-based work [IVSC-AI-2025]"
  human_checkpoints:
    - "Valuer or reviewer remains responsible for the report [IVSC-AI-2025]"
  role_evolution: "Not described in the source."
  evidence_grade: D
  sources:
    - { ref: IVSC-AI-2025, title: "Navigating the Rise of Artificial Intelligence in Valuation: Opportunities, Risks, and Standards", publisher: "International Valuation Standards Council", type: standard-setter, url: "https://ivsc.org/wp-content/uploads/2025/07/Navigating-the-Rise-of-AI-in-Valuation-Opportunities-Risks-and-Standards.pdf", date: 2025-07-23, access: full, locator: "p8 (IVS 100, 101, 102 boxes); pp13-14 (quality control)" }
    - { ref: IVSC-IVSED-2026, title: "International Valuation Standards: Summary and Consultation Questions (IVS Exposure Draft, January 2026)", publisher: "International Valuation Standards Council", type: standard-setter, url: "https://ivsc.org/_ivs_effective_31_january-2028_exposure-draft-summary-and-consultation-questions-final_", date: 2026-01, access: full, locator: "pp4-5 (summary of proposed changes); p13 (consultation questions)" }
  last_reviewed: 2026-10-16
  notes: "Idea (label: idea). The IVSC describes it as a possibility, not a deployment. No named user found."

- id: assurance-specialists-07
  title: Agents build complete valuation or financial models, with analysts supplying and reviewing assumptions (idea)
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [data-reporting, expert-judgment]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: "Building a full valuation model is slow, and the judgment sits in company-specific assumptions [ARXIV-GAUGE-2026]."
  solution: "Researchers report that language-model agents can now construct complete financial models, and introduce GAUGE, a benchmark built from 1,001 professional valuations spanning 922 companies to grade them [ARXIV-GAUGE-2026]."
  outcomes:
    - { lever: quality, description: "Current agents are far better at constructing financial models than at deriving the company-specific assumptions that drive valuation, a gap that persists after fine-tuning", figure: "median score 0.33", measures: "median score when financial models built by different professional analysts for the same company are graded against one another under standard tolerances, which the authors use to show single-reference grading confounds disagreement with error", provenance: independent, source_ref: ARXIV-GAUGE-2026 }
  prerequisites:
    - "Evaluation sets that tolerate legitimate professional disagreement instead of a single expert answer [ARXIV-GAUGE-2026]"
  risks_and_guardrails:
    - "Agents may build mechanically sound models with weak assumptions, so assumption review is the control point [ARXIV-GAUGE-2026]"
  human_checkpoints:
    - "Analyst supplies and challenges company-specific assumptions [ARXIV-GAUGE-2026]"
  role_evolution: "Not described in the source."
  evidence_grade: D
  sources:
    - { ref: ARXIV-GAUGE-2026, title: "One Analyst Is Not Ground Truth: Grading Agent-Built Financial Models Against Observed Professional Practice", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2607.24889", date: 2026-07-27, access: full, locator: "abstract" }
  last_reviewed: 2026-10-16
  notes: "Idea (label: idea). Graded D because no deployment was found, even though the benchmark gives an independent measurement. Abstract only. A Reference Global paper on LLM discounted-cash-flow valuation (look-ahead leakage; landscape lead A14) was not reopened in this pass."

- id: assurance-specialists-08
  title: Actuaries use GenAI for analysis and code under model-validation standards (idea)
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [expert-judgment, data-reporting]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Actuarial work must meet standards of practice that require explaining methods, justifying assumptions and validating models, which opaque GenAI tools complicate [SOA-GENAI-2026]."
  solution: "The American Academy of Actuaries paper treats GenAI as a model, so ASOP No. 56 applies, and says a result cannot be used without validation [AAA-GENAI-2024]. The SOA's September 2026 guide describes actuarial use cases as human-led with agent support, or agent-led with human support [SOA-GENAI-2026]. A July 2026 benchmark of 12,050 actuarial questions found frontier LLMs strong on standardized knowledge but much weaker on case reasoning, tool-based workflows and jurisdiction-sensitive practice [ARXIV-INSACTBENCH-2026]."
  outcomes:
    - { lever: quality, description: "Capability boundary: strong on standardized actuarial knowledge, much weaker on long-context case reasoning, spreadsheet and R-code tasks, and jurisdiction-sensitive practice", figure: "none published (abstract gives no scores)", measures: "benchmark of 12,050 Q&A pairs from public exams and sample questions of 16 actuarial associations; nine LLMs and human actuarial experts compared", provenance: independent, source_ref: ARXIV-INSACTBENCH-2026 }
  prerequisites:
    - "Validation testing and analysis sufficient to support conclusions (ASOP No. 56) [AAA-GENAI-2024]"
  risks_and_guardrails:
    - "The AAA paper says actuaries should refrain from using AI to fill a critical skill or knowledge gap [AAA-GENAI-2024]"
    - "GenAI results are not always accurate and reproducible, so great care is warranted where explainability matters [AAA-GENAI-2024]"
    - "The AAA paper asks whether reliance on AI could withstand audit challenge and whether free public tools allow meeting audit requirements [AAA-GENAI-2024]"
  human_checkpoints:
    - "Actuary vets and validates AI recommendations before applying them [AAA-GENAI-2024]"
  role_evolution: "The AAA paper says actuaries must stay qualified to do the service without AI and encourages interdisciplinary work with AI specialists [AAA-GENAI-2024]."
  evidence_grade: D
  sources:
    - { ref: AAA-GENAI-2024, title: "Actuarial Professionalism Considerations for Generative AI", publisher: "American Academy of Actuaries", type: professional-body, url: "https://actuary.org/article/actuarial-professionalism-considerations-for-generative-ai/", date: 2024, access: full, locator: "Part 1 questions; Part 2 practical considerations" }
    - { ref: SOA-GENAI-2026, title: "Model Governance/Ethics for GenAI Models - Practical Guide and Educational Handbook", publisher: "Society of Actuaries Research Institute", type: professional-body, url: "https://www.soa.org/resources/research-reports/2026/model-gov-ethics-for-gen-ai/", date: 2026-09-23, access: full, locator: "Overview and FAQ" }
    - { ref: ARXIV-INSACTBENCH-2026, title: "INS-ActBench: A Comprehensive Benchmark for Assessing Professional Actuarial Capability of Large Language Models", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2607.24273", date: 2026-07-27, access: full, locator: "abstract" }
  last_reviewed: 2026-10-16
  notes: "Idea (label: idea). It covers actuaries generally, including management's actuaries whose work auditors evaluate. No named actuarial team deployment was found. The AAA paper's year is from the page ('released earlier this year', reprinted in late 2024); its first release month was not found."

- id: assurance-specialists-09
  title: Actuarial audit specialists test AI reserving models with explainability techniques and benchmarks (idea)
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Black-box reserving models give little visibility of inner workings, so auditors' usual in-model checks (visual inspection of claim development, lapse plots) may no longer work [FORVIS-RESERVING-2025]."
  solution: "A Forvis Mazars Ireland actuarial director describes ten steps. They include upskilling actuarial audit teams in machine learning, treating model bias, overfitting, data quality and transparency as in-scope risks, benchmarking against traditional reserving methods, testing explainability with global techniques such as surrogate models and local ones such as LIME and SHAP, assessing architecture and hyperparameters, and testing reproducibility [FORVIS-RESERVING-2025]."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable; practitioner proposal", provenance: self-reported, source_ref: FORVIS-RESERVING-2025 }
  prerequisites:
    - "Actuarial audit staff with machine-learning skills [FORVIS-RESERVING-2025]"
    - "Insurer documentation of code management, model logs and deployment procedures to allow reproducibility [FORVIS-RESERVING-2025]"
  risks_and_guardrails:
    - "The author says commonly accepted AI audit standards are even less mature than AI use in reserving [FORVIS-RESERVING-2025]"
    - "Manual data cleansing and feature engineering are potential sources of management bias and will likely become an audit focus [FORVIS-RESERVING-2025]"
  human_checkpoints:
    - "Actuarial audit teams apply expert judgment and professional skepticism about when to bring more sophisticated techniques in [FORVIS-RESERVING-2025]"
  role_evolution: "Actuarial audit specialists need machine-learning and coding skills, and the author expects scarcity of that blend to concentrate reliance on a small group of management experts [FORVIS-RESERVING-2025]."
  evidence_grade: D
  sources:
    - { ref: FORVIS-RESERVING-2025, title: "Ten steps to help auditors evolve and adapt to AI reserving systems", publisher: "Forvis Mazars (Ireland)", type: firm, url: "https://www.forvismazars.com/ie/en/insights/news-opinions/steps-to-adapt-to-ai-reserving-systems", date: 2025, access: full, locator: "steps 1-10" }
  last_reviewed: 2026-10-16
  notes: "Idea (label: idea). The page shows no publication date. The year 2025 is an estimate (the article uses the Forvis Mazars name, which postdates 2024), so treat the date as unverified. No firm states it has done this on an engagement."

- id: assurance-specialists-10
  title: Auditor's actuarial specialist builds an independent AI challenger model to test a client's AI reserving model (idea)
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: "If a client's black-box model claims results that traditional methods cannot validate, the auditor has no independent comparison [FORVIS-RESERVING-2025]."
  solution: "The Forvis Mazars author says using one AI model to challenge another ('black box versus black box') could become commonplace in actuarial audit and could help identify user bias in model selection and design, which requires actuarial audit teams to build coding skills to develop credible algorithms independently [FORVIS-RESERVING-2025]."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable; practitioner proposal", provenance: self-reported, source_ref: FORVIS-RESERVING-2025 }
  prerequisites:
    - "Access to the client's data and model documentation, and independent coding capability in the audit team [FORVIS-RESERVING-2025]"
  risks_and_guardrails:
    - "Neural-network models cannot be identically replicated, so the author says teams should aim to reproduce reasonable imitations [FORVIS-RESERVING-2025]"
  human_checkpoints:
    - "Specialist judges whether differences between the client's and the challenger model are explained [FORVIS-RESERVING-2025]"
  role_evolution: "Actuarial audit specialists become model builders as well as reviewers [FORVIS-RESERVING-2025]."
  evidence_grade: D
  sources:
    - { ref: FORVIS-RESERVING-2025, title: "Ten steps to help auditors evolve and adapt to AI reserving systems", publisher: "Forvis Mazars (Ireland)", type: firm, url: "https://www.forvismazars.com/ie/en/insights/news-opinions/steps-to-adapt-to-ai-reserving-systems", date: 2025, access: full, locator: "steps 4-5" }
  last_reviewed: 2026-10-16
  notes: "Idea (label: idea). Same source and date caveat as item 09."

- id: assurance-specialists-11
  title: Auditors obtain AI-use disclosures and validation evidence when management's expert uses AI (idea)
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "A specialist's work is highly technical and often not entirely transparent to the auditor, who may not have complete access to it [PCAOB-SPECIALISTS-2025]. AI inside an expert's valuation adds opacity."
  solution: "The IVSC says valuers should disclose whether, how and why AI was used, in the scope of work or documentation, and must understand and assess any valuation model for fit with its intended use [IVSC-AI-2025]. Its January 2026 draft would make documentation of significant AI use mandatory in IVS 106 [IVSC-IVSED-2026]. Auditors already evaluate a company specialist's data, significant assumptions and methods (not by re-performing the specialist's work) [PCAOB-SPECIALISTS-2025], so such disclosures would feed that evaluation."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable; idea", provenance: independent, source_ref: IVSC-AI-2025 }
  prerequisites:
    - "Valuation standards that require AI-use disclosure; the IVSC draft would take effect 31 Jan 2028 if adopted as proposed, subject to responses [IVSC-IVSED-2026]"
  risks_and_guardrails:
    - "Auditor evaluation of company-produced data, external data, assumptions and methods remains required [PCAOB-SPECIALISTS-2025]"
    - "Neither ISA (UK) 620 nor the PCAOB specialist material read here mentions AI, so the procedure would rest on general requirements [FRC-620STD-2026; PCAOB-SPECIALISTS-2025]"
  human_checkpoints:
    - "Engagement partner and team evaluate whether the specialist's work provides sufficient appropriate evidence [PCAOB-SPECIALISTS-2025]"
  role_evolution: "Not described in the sources."
  evidence_grade: D
  sources:
    - { ref: IVSC-AI-2025, title: "Navigating the Rise of Artificial Intelligence in Valuation: Opportunities, Risks, and Standards", publisher: "International Valuation Standards Council", type: standard-setter, url: "https://ivsc.org/wp-content/uploads/2025/07/Navigating-the-Rise-of-AI-in-Valuation-Opportunities-Risks-and-Standards.pdf", date: 2025-07-23, access: full, locator: "pp10-12 (transparency; data and inputs; valuation models)" }
    - { ref: IVSC-IVSED-2026, title: "International Valuation Standards: Summary and Consultation Questions (IVS Exposure Draft, January 2026)", publisher: "International Valuation Standards Council", type: standard-setter, url: "https://ivsc.org/_ivs_effective_31_january-2028_exposure-draft-summary-and-consultation-questions-final_", date: 2026-01, access: full, locator: "pp4-5; p10 (effective date); p13 (questions 4-9)" }
    - { ref: PCAOB-SPECIALISTS-2025, title: "Spotlight: Considerations for Audit Firms Using the Work of Specialists", publisher: PCAOB, type: regulator, url: "https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/use-of-specialist-spotlight.pdf", date: 2025-02, access: full, locator: "p3 (background); p6 (evaluating a company specialist)" }
    - { ref: FRC-620STD-2026, title: "ISA (UK) 620 (Revised September 2026) Using the Work of an Auditor's Expert", publisher: FRC, type: regulator, url: "https://www.caalley.com/intl_cnt/frc/ISA_UK_620_Revised_September_2026.pdf", date: 2026-09-23, access: full, locator: "paras 2(b), 6, A22, A35-A37" }
  last_reviewed: 2026-10-16
  notes: "Idea (label: idea). The IVSC asks valuers to disclose AI use. No source describes auditors requesting or using that disclosure. The IVS draft's comment period closed 30 Apr 2026, so the final text may differ."

- id: assurance-specialists-12
  title: Auditors treat a client's significant AI use like complex valuation models and external specialists (idea)
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Clients embed AI in financial reporting faster than their governance matures: only 6% of audit partners rate AI governance at their largest client as advanced [BOARDMEMBER-CAQ-2026]."
  solution: "The AICPA practice aid says that when an entity's AI plays a significant role in financial reporting, considerations may be similar to those for entities using external specialists and complex valuation models. If management lacks the understanding needed to take responsibility for the outputs, that may indicate a lack of appropriate skills and competencies [AT-AICPAPA-2026]. The AUASB says auditors need to understand AI applications that produce material information and that restricted access to a third-party AI application's logic, data and assumptions may be a scope limitation if no alternative procedures are possible [AUASB-AI-2025]."
  outcomes:
    - { lever: risk, description: "Audit partners rate AI governance at their largest client as advanced in a small minority of cases", figure: "6%", measures: "share of audit partners who described the maturity of AI governance at their largest client as advanced, meaning formal frameworks, policies and oversight structures fully in place (46% early stage, 40% developed but incomplete); sample size not stated in the source", provenance: independent, source_ref: BOARDMEMBER-CAQ-2026 }
    - { lever: risk, description: "Most frequently cited AI-related internal control challenges at the largest client include insufficient in-house AI expertise and thin model documentation", figure: "33% and 26%", measures: "share of audit partners citing insufficient in-house AI expertise and control capability (33%) and insufficient documentation of AI models, assumptions and decision logic (26%) as most significant challenges at their largest client", provenance: independent, source_ref: BOARDMEMBER-CAQ-2026 }
  prerequisites:
    - "Auditor understanding of the entity's AI use in the risk-assessment phase [AT-AICPAPA-2026]"
    - "Access to the AI application's logic, data and assumptions, or suitable alternative procedures [AUASB-AI-2025]"
  risks_and_guardrails:
    - "The AICPA practice aid is non-authoritative, and further guidance on risk of material misstatement and audit evidence is promised [AT-AICPAPA-2026]"
    - "The AUASB says auditors should not over-rely on technology-generated information (automation bias) [AUASB-AI-2025]"
  human_checkpoints:
    - "Auditor remains responsible for the audit and the opinion [AICPA-PA-2026]"
  role_evolution: "The AICPA says practitioners may need a blend of auditing expertise, AI knowledge, data skills, professional skepticism and specialist support [AICPA-PA-2026]."
  evidence_grade: D
  sources:
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "acceptance and continuance section; quotation on external specialists and complex valuation models" }
    - { ref: AICPA-PA-2026, title: "AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing", publisher: AICPA & CIMA, type: standard-setter, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: 2026-10-13, access: full, locator: "'Considering an organization's use of AI' bullets" }
    - { ref: AUASB-AI-2025, title: "Impact of AI on Auditors", publisher: AUASB, type: regulator, url: "https://auasb.gov.au/publications/impact-of-ai-on-auditors/", date: 2025-07, access: full, locator: "section 'Impact of the use of AI by audited entities'" }
    - { ref: BOARDMEMBER-CAQ-2026, title: "What Audit Partners Are Seeing On AI And What It Means For Audit Committees", publisher: "Corporate Board Member (CAQ author)", type: survey, url: "https://boardmember.com/?p=50023", date: 2026-07-15, access: full, locator: "items 1 and 3 (Spring 2026 Audit Partner Pulse)" }
  last_reviewed: 2026-10-16
  notes: "Idea (label: idea) as applied to the specialist toolbox: the guidance exists, but no source documents auditors using specialists this way on engagements. The AICPA practice aid full text is behind a login; its wording here comes from the AICPA release and Accounting Today. The AUASB page URL is the AUASB home page because the exact page address was not recorded; the page was opened in the landscape run and read in this pass from the saved copy."

- id: assurance-specialists-13
  title: AI and data-science experts are engaged as auditor's experts or internal specialists to evaluate client AI (idea)
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "ISA 620 and PCAOB specialist standards list valuation, actuarial, environmental, legal and tax examples, not AI [FRC-620STD-2026; PCAOB-SPECIALISTS-2025]. Audit teams still need people who can evaluate AI systems."
  solution: "ICAN asked the IAASB to expand application-material examples in ISA 620 and ISAE 3000 to refer to AI and machine-learning experts, noting AI experts, data scientists and cybersecurity professionals are increasingly engaged [ICAN-620-2025]. The AICPA says engagement teams may need specialist support [AICPA-PA-2026]. The FRC reports a recent spike in demand for AI specialists across audit and consultancy [FRC-ARAQ-2026]."
  outcomes:
    - { lever: capacity, description: "Share of Big Four job postings requiring AI expertise rose; this is hiring evidence, not evidence of AI specialists acting as auditor's experts", figure: "nearly 7% in 2025 versus under 2% in 2022", measures: "share of the four firms' job postings that required AI expertise, per an FT analysis as reported by Computerworld; one firm noted a single posting can cover multiple positions", provenance: independent, source_ref: COMPUTERWORLD-FT-2026 }
  prerequisites:
    - "Evaluation of the expert's competence, capabilities and objectivity under the revised ISA 620 (effective for periods commencing on or after 15 Dec 2026 in the UK version) [FRC-620STD-2026]"
  risks_and_guardrails:
    - "An AI vendor or data-science team that built or tuned the client's system may face the objectivity threats ISA 620 para 9A treats as disqualifying if not reduced to an acceptable level [FRC-620STD-2026]"
  human_checkpoints:
    - "Auditor evaluates adequacy of the expert's work for the auditor's purposes [FRC-620STD-2026]"
  role_evolution: "The FRC says firms must attract and retain staff for advanced technology, with a recent spike in demand for AI specialists [FRC-ARAQ-2026]. About a third of 54 surveyed US firms said they needed at least one non-traditional skill, led by data analysts, data scientists and IT specialists [CPACOM-ATR-2025]."
  evidence_grade: D
  sources:
    - { ref: ICAN-620-2025, title: "Response template, ED of proposed narrow-scope amendments arising from IESBA's Using the Work of an External Expert project (ICAN)", publisher: "Institute of Chartered Accountants of Nigeria", type: professional-body, url: "https://www.iaasb.org/sites/default/files/2025-07/IAASB-Exposure-Draft-Narrow-Scope-Amendments-Experts-Response-Template_0.pdf", date: 2025-07, access: full, locator: "Part B, question 4 'Other matters', item 2 (PDF p11)" }
    - { ref: AICPA-PA-2026, title: "AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing", publisher: AICPA & CIMA, type: standard-setter, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: 2026-10-13, access: full, locator: "'Considering an organization's use of AI' bullet on audit team capabilities" }
    - { ref: FRC-ARAQ-2026, title: "Annual Review of Audit Quality 2026", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/9772/Annual_Review_of_Audit_Quality_2026_2eSTaw8P.pdf", date: 2026-07-22, access: full, locator: "p28 (resourcing and AI specialists)" }
    - { ref: COMPUTERWORLD-FT-2026, title: "The Big Four accounting firms are now hiring more AI specialists than accountants", publisher: "Computerworld (reporting an FT analysis)", type: press, url: "https://www.computerworld.com/article/4173296/the-big-four-accounting-firms-are-now-hiring-more-ai-specialists-than-accountants.html", date: 2026-05-19, access: full, locator: "whole article" }
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report (Opportunity through audit transformation)", publisher: "CPA.com and AICPA", type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "p20 (new approaches require new skills)" }
    - { ref: FRC-620STD-2026, title: "ISA (UK) 620 (Revised September 2026) Using the Work of an Auditor's Expert", publisher: FRC, type: regulator, url: "https://www.caalley.com/intl_cnt/frc/ISA_UK_620_Revised_September_2026.pdf", date: 2026-09-23, access: full, locator: "paras 6(a), 9, 9A, A1, A19A" }
  last_reviewed: 2026-10-16
  notes: "Idea (label: idea). The scope item is partly routed: IT and AI-system assurance belongs to controls-testing and an assurance-over-AI cross-cut. It is kept here only for how it touches ISA 620 and specialist use. ISA 620 defines an auditor's expert as an individual or organization, so an AI tool is not itself an expert [FRC-620STD-2026, para 6(a)]. The 2025 ICAN letter is the only one of 49 readable letters that names AI. Hiring data is about AI roles generally, not auditor's experts."

- id: assurance-specialists-14
  title: Forensic specialists authenticate suspect digital evidence when AI-fabricated documents are a risk (idea)
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "AI can produce documents, signatures and records that look authentic, which weakens ordinary evidence procedures [ISACA-DEEPFAKE-2026]."
  solution: "An ISACA Now blog post by an internal-audit lead urges a zero-trust stance, validating authenticity before relying on evidence, and building digital-forensics skills to authenticate evidence [ISACA-DEEPFAKE-2026]. The AUASB says auditors should be alert to AI-fabricated third-party documents and may need to rely more on independent third-party sources such as direct confirmations [AUASB-AI-2025]."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable; practitioner and regulator discussion", provenance: self-reported, source_ref: ISACA-DEEPFAKE-2026 }
  prerequisites:
    - "Digital-forensics capability inside or available to the engagement team [ISACA-DEEPFAKE-2026]"
  risks_and_guardrails:
    - "The ISACA post is a single practitioner's opinion, not guidance [ISACA-DEEPFAKE-2026]"
  human_checkpoints:
    - "Auditor decides what evidence can be trusted after authentication checks [ISACA-DEEPFAKE-2026]"
  role_evolution: "The post says auditors should develop AI literacy and strengthen digital-forensics skills [ISACA-DEEPFAKE-2026]."
  evidence_grade: D
  sources:
    - { ref: ISACA-DEEPFAKE-2026, title: "The Audit Evidence Crisis: How AI Deepfakes Are Rewriting Assurance Standards", publisher: "ISACA Now Blog", type: community, url: "https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2026/the-audit-evidence-crisis-how-ai-deepfakes-are-rewriting-assurance-standards", date: 2026, access: full, locator: "sections 'Why a Zero-Trust Approach is Essential' and 'The Path Forward'" }
    - { ref: AUASB-AI-2025, title: "Impact of AI on Auditors", publisher: AUASB, type: regulator, url: "https://auasb.gov.au/publications/impact-of-ai-on-auditors/", date: 2025-07, access: full, locator: "section 'Impact of the use of AI by audited entities', last paragraph" }
  last_reviewed: 2026-10-16
  notes: "Idea (label: idea). A Wolters Kluwer piece (6 May 2026) on AI-generated audit evidence appeared in search results only [WK-AIEVIDENCE-2026] and is not relied on. Baseline without AI: the FRC reports one KPMG audit where forensic specialists joined fraud risk assessment and improved journal-entry testing [FRC-ARAQ-2026, p82]. Evidence authenticity is mainly a substantive-testing topic (see section 4)."

- id: assurance-specialists-15
  title: A firm AI system gives contradictory evidence on management's complex estimates, in place of specialist input (idea)
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Firms invest in AI to help auditors evaluate complex estimates, but auditors may discount AI advice more than identical human advice [COMMERFORD-2022]."
  solution: "In an experiment, auditors received contradictory evidence about management's complex estimate from either the firm's AI system or a human specialist [COMMERFORD-2022]."
  outcomes:
    - { lever: quality, description: "Auditors facing contradictory evidence from the AI system proposed smaller adjustments to management's estimates than those facing a human specialist, especially when management used relatively objective inputs", figure: "none (abstract gives direction only)", measures: "size of adjustments auditors proposed to management's complex estimates, AI-source versus human-specialist-source conditions in an experiment", provenance: independent, source_ref: COMMERFORD-2022 }
  prerequisites:
    - "A firm AI system able to produce evidence on complex estimates [COMMERFORD-2022]"
  risks_and_guardrails:
    - "The authors say auditor susceptibility to algorithm aversion could prove costly for the profession and financial statement users [COMMERFORD-2022]"
  human_checkpoints:
    - "Auditor decides how large an adjustment to propose [COMMERFORD-2022]"
  role_evolution: "Training would need to address how auditors weigh AI evidence versus specialist advice [COMMERFORD-2022]."
  evidence_grade: D
  sources:
    - { ref: COMMERFORD-2022, title: "Man Versus Machine: Complex Estimates and Auditor Reliance on Artificial Intelligence", publisher: "Journal of Accounting Research (vol. 60, issue 1, pp. 171-201)", type: academic, url: "https://doi.org/10.1111/1475-679x.12407", date: 2021-12, access: full, locator: "abstract" }
  last_reviewed: 2026-10-16
  notes: "Idea (label: idea): the experiment tests a scenario, not a deployment. The date is the first-published month from Crossref; the landscape lists the paper as 2022 (issue year). Abstract only."

- id: assurance-specialists-16
  title: Auditors use a firm-specific LLM on a complex inventory valuation task
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Complex valuation tasks require auditors to produce correct documentation under time pressure [SSRN-LLMAQ-2026]."
  solution: "A preregistered randomized field experiment gave 100 professional auditors at a global audit firm a complex inventory valuation task, either with the traditional digital tool set or with additional support from a firm-specific LLM [SSRN-LLMAQ-2026]."
  outcomes:
    - { lever: quality, description: "LLM access significantly improved audit output quality (more formally correct documentation) and reduced task completion time; it did not improve adherence to internal audit guidelines", figure: "none (abstract gives direction only)", measures: "audit output quality and task completion time of 100 auditors with versus without firm-specific LLM access, on one inventory valuation task", provenance: independent, source_ref: SSRN-LLMAQ-2026 }
    - { lever: quality, description: "Gains were largest for active users and did not differ systematically by auditor experience", figure: "none (abstract gives direction only)", measures: "heterogeneity of performance gains by LLM adoption intensity and auditor experience in the same experiment", provenance: independent, source_ref: SSRN-LLMAQ-2026 }
  prerequisites:
    - "A firm-specific LLM provided to auditors [SSRN-LLMAQ-2026]"
  risks_and_guardrails:
    - "The abstract concludes LLMs enhance productivity and output quality without uniformly strengthening process discipline [SSRN-LLMAQ-2026]"
  human_checkpoints:
    - "Not described in the abstract."
  role_evolution: "No experience-based difference in gains, which the authors call surprising given earlier evidence that LLMs help less-experienced users more [SSRN-LLMAQ-2026]."
  evidence_grade: C
  sources:
    - { ref: SSRN-LLMAQ-2026, title: "The Effect of Large Language Models on Audit Quality: Causal Evidence from a Randomized Field Experiment", publisher: "SSRN (Jezierski, Kaltenpoth, Mueller, Weissenberger)", type: academic, url: "https://doi.org/10.2139/ssrn.6095166", date: 2026, access: full, locator: "abstract (retrieved from the Crossref record; SSRN page blocked)" }
  last_reviewed: 2026-10-16
  notes: "This is the strongest independent quality result found but is graded C: the firm is not named in the abstract, so no named-organization measurement exists, and inventory valuation is a substantive procedure rather than specialist work, which would cap any grade at B. Abstract only; the paper's figures were not read. The Crossref record was created 2026-07-29; the paper's posting date was not found. Route also to substantive-testing."

- id: assurance-specialists-17
  title: "Tax specialists use a GenAI tax research assistant (adjacent: tax advisory, not audit tax specialists)"
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Tax professionals spend time searching and analysing tax legislation and case law [KPMGUK-BLUEJ-2024]."
  solution: "KPMG UK and Blue J announced on 22 Feb 2024 a generative AI product (Ask Blue J), built on fine-tuned OpenAI GPT models and Blue J's curated tax content, to answer tax research questions. KPMG said it was available in the firm's 3,000-strong tax and legal function and that KPMG would have exclusive access among UK Big Four firms for three years [KPMGUK-BLUEJ-2024]."
  outcomes:
    - { lever: speed, description: "The release says the tool dramatically reduces time spent searching legislation and case law; no figure given", figure: "none published", measures: "not applicable; qualitative claim", provenance: vendor-published, source_ref: KPMGUK-BLUEJ-2024 }
    - { lever: quality, description: "KPMG says its earlier Blue J alliance predicts tax scenario outcomes, such as employed versus self-employed status, with 90%+ accuracy for employees to review; this refers to a separate predictive tool", figure: "90%+", measures: "accuracy of tax-scenario outcome predictions; basis and sample not stated", provenance: vendor-published, source_ref: KPMGUK-BLUEJ-2024 }
  prerequisites:
    - "Curated tax content database and a fine-tuned model [KPMGUK-BLUEJ-2024]"
  risks_and_guardrails:
    - "The release says employees review the predictions [KPMGUK-BLUEJ-2024]"
  human_checkpoints:
    - "Tax professionals review outputs and advise clients [KPMGUK-BLUEJ-2024]"
  role_evolution: "KPMG says tax experts can spend more time on complicated and urgent issues [KPMGUK-BLUEJ-2024]."
  evidence_grade: B
  sources:
    - { ref: KPMGUK-BLUEJ-2024, title: "KPMG UK and Blue J expand strategic alliance to introduce generative AI into tax tools", publisher: "KPMG UK", type: firm, url: "https://kpmg.com/uk/en/media/press-releases/2024/02/kpmg-uk-and-blue-j-expand-strategic-alliance-to-introduce-generative-ai-into-tax-tools.html", date: 2024-02-22, access: full, locator: "press release body" }
  last_reviewed: 2026-10-16
  notes: "Grade B is capped by adjacency: the release is about KPMG's tax and legal advisory function, not specialists supporting audits. It also predates the 12-18 month window, so use it as a foundation, and its present status was not verified. The release says both that the product 'will launch' and that the tool is 'now available'. No source on audit income-tax-provision specialists using AI was found (see Gaps). Hux, Andiola and Noga (2022) document audit tax specialists' roles through 33 interviews but do not cover AI [HUX-2022]."

- id: assurance-specialists-18
  title: Domain specialists review the outputs of firm AI tools used in audit (idea)
  archetype: assurance
  module: specialists
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Reviewers of AI output need the competence to spot deficiencies, and audit and accounting expertise may not be enough for some tools and use cases [FRC-GENAI-2026]."
  solution: "The FRC guidance says that, for some tools and use cases, specialist expertise may be required for reviewers of generative or agentic AI outputs [FRC-GENAI-2026]. The AUASB says the design, use, results and conclusions of AI audit tools should be reviewed by the audit partner and firm specialists [AUASB-AI-2025]."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable; guidance", provenance: independent, source_ref: FRC-GENAI-2026 }
  prerequisites:
    - "Firm specialists available to engagement teams, and tools certified for the use case [FRC-GENAI-2026]"
  risks_and_guardrails:
    - "Reviewers should apply professional skepticism and be aware of automation bias [FRC-GENAI-2026]"
  human_checkpoints:
    - "Review of final outputs by appropriately competent staff [FRC-GENAI-2026]"
  role_evolution: "Specialists gain a review role over audit AI outputs [FRC-GENAI-2026; AUASB-AI-2025]."
  evidence_grade: D
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "p37 (Review: appropriate reviewers)" }
    - { ref: AUASB-AI-2025, title: "Impact of AI on Auditors", publisher: AUASB, type: regulator, url: "https://auasb.gov.au/publications/impact-of-ai-on-auditors/", date: 2025-07, access: full, locator: "section 'Consideration on using AI tools in audits', 'Review' bullet" }
  last_reviewed: 2026-10-16
  notes: "Idea (label: idea). 'Specialists' here are firm technical specialists reviewing AI output, a different sense from ISA 620 auditor's experts. Mainly relevant to quality-management (see section 4)."
```

---

## 3. Module notes

### Processes and key steps (with work types)

1. **Determine whether an expert is needed.** Required when expertise in a field other than accounting or auditing is necessary (ISA (UK) 620 para 7). Examples in the standard's application material include valuation of complex instruments, actuarial calculation of insurance and benefit liabilities, oil and gas reserves, environmental liabilities, interpretation of contracts and laws, and complex tax issues (FRC-620STD-2026, A1). `expert-judgment`.
2. **Evaluate competence, capabilities and objectivity.** ISA (UK) 620 para 9. The revised para 9A bars use of an expert who lacks competence or capabilities, or whose objectivity threats cannot be reduced to an acceptable level. A UK-specific para 9-1 requires an independence confirmation from external experts on public-interest-entity audits (FRC-620STD-2026). The PCAOB treats objectivity as a spectrum, so a less objective engaged specialist can be used with additional procedures (PCAOB-SPECIALISTS-2025, p11). `review-assurance`.
3. **Agree the work and responsibilities with the expert** (ISA (UK) 620 para 11; PCAOB: establish and document an understanding of who tests data and develops or evaluates assumptions and methods, PCAOB-SPECIALISTS-2025, p10). `coordination-scheduling`.
4. **Evaluate the expert's data, assumptions and methods, and the adequacy of the work.** The PCAOB says evaluation of a company specialist's work does not require re-performing it, and that auditors must test company-produced data and evaluate external data (PCAOB-SPECIALISTS-2025, pp6-7). `review-assurance`.
5. **Management's expert** is handled under ISA (UK) 500, paras A45-A59 (FRC-620STD-2026, para 2(b) and footnote 2) and PCAOB AS 1105 Appendix A. `review-assurance`.
6. **Specialist production work:** valuation models, actuarial calculations, tax provision support, forensic analysis, environmental or reserve estimates. `data-reporting`, `expert-judgment`.
7. **Documentation** (UK para 15-1: document each request for advice and the advice received, FRC-620STD-2026). `document-production`.
8. **New step: audit the client's AI-based estimate or AI-supported expert.** The AICPA, AUASB and CAQ material treat this as an extension of complex-model work (AT-AICPAPA-2026; AUASB-AI-2025). `review-assurance`.

### Common pain points

- **Evaluation of company specialists and their data.** PCAOB inspection staff cite auditors who did not evaluate a company specialist's work beyond filing the report, did not test non-financial company data used by a specialist (such as geological or engineering data), or did not involve a specialist where they lacked the skill (PCAOB-SPECIALISTS-2025, p12).
- **Challenge of valuation judgments and use of experts (UK).** In the FRC's 2026 review of BDO audits, six audits lacked evidence of challenge of key assumptions in valuing assets and liabilities, and on five of those six the evidence for involving an auditor's expert was insufficient (FRC-ARAQ-2026, p45). For PwC, on one impairment and the key independence finding, teams did not respond adequately to points raised by specialists and experts (FRC-ARAQ-2026, p95).
- **Roles and timing.** Common firm-identified themes include unclear allocation of roles across core teams, specialists and components, and late engagement of senior reviewers and specialists (FRC-ARAQ-2026, p14).
- **Data used by actuaries.** One Forvis Mazars UK insurer audit lacked sufficient evidence over the reliability of actuarial data behind technical provisions (FRC-ARAQ-2026, p73).
- **Reliance behaviour.** An experiment with 60 auditors found reliance on IT specialists shifts with the specialist's office location and how distinct their knowledge is, so reliance is partly social, not only technical (HIRSCH-2019; abstract only).
- **Opacity of AI.** Black-box models limit in-model checks and raise the importance of pre-model data governance (FORVIS-RESERVING-2025); the PCAOB says specialist work is often not entirely transparent to the auditor even without AI (PCAOB-SPECIALISTS-2025, p3).

### Baseline good practice (non-AI)

- The FRC's 2026 review records specialist-related good practice: extensive specialists on complex impairments and valuation models at EY (two audits) with senior group-team engagement with component and management specialists (FRC-ARAQ-2026, p63); five KPMG audits with strong challenge and use of specialists, including forensic specialists in fraud risk assessment (FRC-ARAQ-2026, p82); and a PwC audit where risk-modelling specialists reviewed an expected-credit-loss model including code reviews of new elements (FRC-ARAQ-2026, p92). None involves AI. The code-review example is the closest precedent for auditing an AI-based estimate.

### Metrics and benchmarks (with sources)

- **GenAI in UK audits.** The FRC says some firms now deploy GenAI tools to perform audit procedures and generate documentation (FRC-ARAQ-2026, p26), but "limited use of GenAI on audits" was observed in the past year while AI-enabled techniques such as transaction scoring and automated evidence matching are increasingly common (FRC-ARAQ-2026, p27). No count of specialist-related AI use is given.
- **AI-enabled tool growth.** The largest six networks collectively reported about a 30% year-over-year increase in AI-enabled tools in 2025 (IFIAR-TECH-2026, p5; the report says reporting practices differ by network). Numerator and denominator are not given.
- **Client AI governance (audit partners' views).** 6% advanced, 40% developed but incomplete, 46% early stage or reactive at their largest client; top AI control challenges: in-house expertise 33%, data quality 27%, missing governance frameworks 27%, thin model documentation 26% (BOARDMEMBER-CAQ-2026). Sample size not stated.
- **Randomized field experiment.** 100 auditors, firm-specific LLM, inventory valuation: better output quality and speed, no improvement in guideline adherence (SSRN-LLMAQ-2026; abstract only).
- **Agent-built models.** Median agreement of 0.33 between professional analysts' models of the same company under standard tolerances (ARXIV-GAUGE-2026).
- **Actuarial LLM benchmark.** 12,050 questions from 16 associations, nine LLMs, strong on knowledge and weaker on case reasoning (ARXIV-INSACTBENCH-2026).
- **Hiring.** Nearly 7% of Big Four postings required AI expertise in 2025 versus under 2% in 2022 (COMPUTERWORLD-FT-2026).
- **No** inspection-outcome, override-rate or parallel-run data on AI use by specialists was found.

### Guardrails and regulatory points

- **ISA 620 revision.** IAASB narrow-scope amendments were published on 5 Jan 2026 and respond to IESBA Code changes on using external experts; they cover ISA 620, ISRE 2400, ISAE 3000 and ISRS 4400 (IAASB-620NEWS-2026). The IAASB approvals went through the PIOB in December 2025 and the effective date is 15 Dec 2026 (FRC-620-2026, paras 3-4). The UK version was published 23 Sep 2026 (FRC-620NEWS-2026). The IESBA Code revisions were made in December 2024 (FRC-620-2026, para 14). **These changes are about ethics and objectivity, not technology.** The standard text defines an expert as an individual or organization (FRC-620STD-2026, para 6(a)); no keyword reference to AI was found, so an AI tool is not an auditor's expert on the standard's wording.
- **PCAOB.** Standards in play are AS 1105 Appendix A (company specialists), AS 1201 Appendix C (auditor-employed specialists) and AS 1210 (auditor-engaged specialists) (PCAOB-SPECIALISTS-2025, p5). The technology-assisted-analysis amendments to AS 1105 and AS 2301 take effect for fiscal years beginning on or after 15 Dec 2025 (the notice makes this subject to SEC approval; an approval order is listed in the Federal Register) and say they focus on technology-assisted analysis and not on other technologies such as blockchain or artificial intelligence (PCAOB-TAA-2024, Summary). In the PCAOB's 2026 standard-setting consultation, firms favored guidance over prescriptive AI standards; KPMG asked that guidance address "externally generated or model-based information" (GOINGCONCERN-PCAOB-2026).
- **Valuation standards.** Current IVS (effective 31 Jan 2025) requires the valuer to understand and assess any model (IVS 105) and says no model without valuer judgment, including an AVM, can produce an IVS-compliant valuation (IVSC-AI-2025, pp4-5). The January 2026 draft would add mandatory AI requirements and IVS 107 on quality controls; the IVSC says the next edition would be published 31 Jan 2027 with effect from 31 Jan 2028, subject to responses (IVSC-IVSED-2026, p10).
- **Actuarial standards.** The AAA says GenAI is a model, so ASOP No. 56 applies, with validation and disclosure expectations (AAA-GENAI-2024).
- **Ethics.** IESBA staff guidance on emerging technologies (reported 20 Aug 2026) says professional accountants are expected to understand the technology enough to judge whether reliance on outputs is appropriate (ICAS-IESBA-2026).
- **Audit-firm AI governance.** The FRC says reviewers may need specialist expertise (FRC-GENAI-2026, p37). The FRC plans a thematic review on how the largest firms govern GenAI in audits (FRC-ARAQ-2026, p27).
- **Client AI.** Heavy client reliance on AI may resemble use of complex valuation models, and restricted access to a third-party AI application's logic may be a scope limitation (AT-AICPAPA-2026; AUASB-AI-2025).

### Frontier signals (dated)

- **2026-01-05:** IAASB issues the ISA 620 narrow-scope amendments (effective 15 Dec 2026) (IAASB-620NEWS-2026). ICAN had asked in July 2025 for AI experts to be named in application material; the UK final standard shows no such addition (ICAN-620-2025; FRC-620STD-2026).
- **2026-01 to 2026-04-30:** IVS exposure draft with AI requirements and IVS 107; comments closed 30 Apr 2026 (IVSC-IVSED-2026).
- **2026-03:** BV Resources reports Big Four valuation leaders discussing where AI delivers efficiency and where it falls short (BVR-BIGFOURLIMITS-2026; teaser only).
- **2026-03-26:** CohnReznick announces 73 Strings analytics in its valuation practice (COHNREZNICK-VALUATION-2026).
- **2026-04-20:** IFIAR reports roughly 30% growth in AI-enabled tools at the largest networks and plans to explore agentic AI (IFIAR-TECH-2026, p5).
- **2026-06-25:** IVSC Valuation Dialogue session on AI in valuation with PwC US's valuation services leader and the co-founder of 73 Strings (IVSC-DIALOGUE-2026).
- **2026-07-22:** FRC's annual review says some firms deploy GenAI to perform audit procedures and plans a GenAI governance thematic (FRC-ARAQ-2026, pp26-27).
- **2026-07-27:** Two benchmarks on agent-built valuation models and LLM actuarial capability (ARXIV-GAUGE-2026; ARXIV-INSACTBENCH-2026).
- **2026-07:** BV Resources reports Big Four valuation leaders listing AI governance among areas where the profession needs new guidance (BVR-FVGUIDANCE-2026; teaser only).
- **2026-08-12:** Firms' PCAOB comment letters say AI should be a priority but oppose prescriptive standards now (GOINGCONCERN-PCAOB-2026).
- **2026-09-23:** FRC final ISA (UK) 620 for periods from 15 Dec 2026 (FRC-620NEWS-2026); SOA publishes its GenAI model-governance guide (SOA-GENAI-2026).
- **2026-10-13:** AICPA practice aid, with more sections promised on risk assessment and audit evidence (AICPA-PA-2026).
- **2026-11-17:** IVSC Advisory Forum session "AI and practical guidance around the globe" in Cologne (IVSC-AGM-2026).
- **2027-01-31 (planned):** next IVS edition to be published, effective 31 Jan 2028, subject to responses (IVSC-IVSED-2026, p10).

### Workforce and role effects

- **Junior valuation staff.** Firms may need to be more intentional about training and mentorship (BVR-PANEL-2026); panelists feared juniors miss learning if they rely on AI results (BVR-BIGFOUR-2025).
- **Specialists need new skills.** Actuarial audit teams need machine-learning skills (FORVIS-RESERVING-2025). Demand for AI specialists has spiked at audit and consultancy firms (FRC-ARAQ-2026, p28; COMPUTERWORLD-FT-2026).
- **New roles in smaller firms.** About a third of 54 surveyed US firms needed at least one non-traditional skill, and about 20% had hired staff with non-traditional backgrounds; data analysts or scientists and IT specialists were listed most often (CPACOM-ATR-2025, p20).
- **Pricing.** Big Four valuation panelists rejected the idea that AI efficiencies should lower billing rates and expect value-based pricing to evolve (BVR-BIGFOUR-2025).

### Objections and concerns practitioners raise

- **Do not use AI to fill a skill gap.** Actuaries unqualified to do the work without AI are likely unqualified with it (AAA-GENAI-2024).
- **Reproducibility and audit challenge.** The AAA paper asks whether reliance on AI could withstand professional, regulatory or audit challenge and whether free public tools allow meeting audit requirements (AAA-GENAI-2024).
- **Black boxes.** The IVSC warns valuers to avoid "black box" situations (IVSC-AI-2025, pp12-13); Forvis Mazars says opacity limits in-model checks and could concentrate reliance on a few management experts (FORVIS-RESERVING-2025).
- **Confidentiality.** Public AI tools may breach client confidentiality or data-protection duties (IVSC-AI-2025, p12); EY is building a proprietary platform for this reason (BVR-BIGFOUR-2025).
- **Premature rules.** Large firms oppose prescriptive AI standards for now (GOINGCONCERN-PCAOB-2026).
- **Algorithm aversion and over-reliance.** Auditors may discount AI evidence relative to human specialists (COMMERFORD-2022), while an LLM did not improve adherence to internal guidelines in the field experiment (SSRN-LLMAQ-2026).
- **Judgment about "acceptable level" of threats.** FRC feedback respondents noted possible inconsistency in deciding what is an acceptable threat level to an expert's objectivity (FRC-620-2026, para 10).

### Interview probes

1. When a client's valuation provider or actuary says AI or machine learning is in the model, what do you ask for (logic, data lineage, versions, prompts), and who on your team signs off on the answer?
2. Do your own valuation, actuarial, tax or forensic specialists use GenAI or vendor AI on audits? How is use approved and certified, and is it written into the agreement with the specialist?
3. How do you decide when a question needs a specialist versus an AI-assisted generalist, and has that decision changed in the last year?
4. What has happened to junior specialist training now that data gathering and model build are partly automated, and has headcount or hiring mix changed?
5. What evidence would convince you that an AI-built valuation or reserve estimate is reliable (back-testing, challenger models, reproducibility), and how do you document outputs that cannot be reproduced exactly?

---

## 4. Routed to other modules

- **controls-testing / assurance-over-AI cross-cut:** IT-audit specialists and ITGCs over AI components. BDO ITGC paper (BDO-ITGC-2026) and COSO GenAI guidance (COSO-GENAI-2026) are landscape sources not reopened here. The PCAOB's Dec 2024 inspection priorities say GenAI use at companies could amplify existing IT risks and that staff will evaluate procedures over ITGCs (PCAOB-PRIORITIES-2025, p6-7).
- **substantive-testing:** evidence authenticity and AI-fabricated third-party documents (AUASB-AI-2025; ISACA-DEEPFAKE-2026) and the LLM inventory-valuation experiment (SSRN-LLMAQ-2026). The FRC contract-review example (FRC-GENAI-2026, example 2) is also substantive testing, although ISA 620 lists contract interpretation as an expert field.
- **quality-management:** firm-level tool governance and certification (FRC-GENAI-2026; FRC-ARAQ-2026, p27 thematic; IFIAR-TECH-2026); firm specialists as reviewers of AI output (use case 18); the PCAOB standard-setting comment letters (GOINGCONCERN-PCAOB-2026).
- **planning-risk-assessment:** client AI governance maturity and understanding of the entity's AI use (BOARDMEMBER-CAQ-2026; AT-AICPAPA-2026).
- **acceptance-independence:** independence of audit-tool and AI vendors (for example SOC tool-provider arrangements and private-equity structures in the landscape) belongs there; this module covers only the objectivity of experts under ISA 620 para 9.
- **Advisory, not audit:** the KPMG-Anthropic global alliance announced 19 May 2026 (Digital Gateway for tax clients and private equity) was seen only in search results (KPMG-ANTHROPIC-2026) and concerns client delivery, not audit specialists.
- **other-assurance:** the IAASB narrow-scope amendments also cover ISAE 3000, ISRE 2400 and ISRS 4400 (IAASB-620NEWS-2026).

---

## 5. Sources

Types follow the vocabulary. Dates are ISO. `access: search-only` means a teaser page or search extract only.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| FRC-620STD-2026 | ISA (UK) 620 (Revised September 2026) Using the Work of an Auditor's Expert (copy of the FRC PDF) | FRC | regulator | https://www.caalley.com/intl_cnt/frc/ISA_UK_620_Revised_September_2026.pdf | 2026-09-23 | full |
| FRC-620NEWS-2026 | FRC publishes final revisions to UK standards on using the work of an auditor's expert | FRC | regulator | https://www.frc.org.uk/news-and-events/news/2026/09/frc-publishes-final-revisions-to-uk-standards-on-using-the-work-of-an-auditors-expert/ | 2026-09-23 | full |
| FRC-620-2026 | Feedback Statement, ISA (UK) 620 and ISAE (UK) 3000 (HTML version, AI-converted and not human-verified per its own warning) | FRC | regulator | https://www.frc.org.uk/docs/9935/html/ | 2026-09-23 | full |
| IAASB-620NEWS-2026 | IAASB Issues Narrow-Scope Amendments Related to IESBA's Using the Work of Experts | IAASB | standard-setter | https://www.iaasb.org/news-events/2026-01/iaasb-issues-narrow-scope-amendments-related-iesba-s-using-work-experts | 2026-01-05 | full |
| IAASB-620ED-2025 | Proposed Narrow-Scope Amendments to IAASB Standards Arising from the IESBA's Using the Work of an External Expert Project (page and 50 comment letters) | IAASB | standard-setter | https://www.iaasb.org/publications/proposed-narrow-scope-amendments-iaasb-standards-arising-iesba-s-using-work-external-expert-project | 2025-04-25 | full |
| ICAN-620-2025 | Response template, narrow-scope amendments ED (Institute of Chartered Accountants of Nigeria) | ICAN via IAASB | professional-body | https://www.iaasb.org/sites/default/files/2025-07/IAASB-Exposure-Draft-Narrow-Scope-Amendments-Experts-Response-Template_0.pdf | 2025-07 | full |
| ICAEW-620-2025 | Response to the narrow-scope amendments ED (ICAEW); mentions technology as a growth area for experts but not AI by name | ICAEW via IAASB | professional-body | https://www.iaasb.org/sites/default/files/2025-07/IAASB-Exposure-Draft-Narrow-Scope-Amendments-Experts-Response-Template-ICAEW-pdf-doc.pdf | 2025-07 | full |
| PCAOB-SPECIALISTS-2025 | Spotlight: Considerations for Audit Firms Using the Work of Specialists | PCAOB | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/use-of-specialist-spotlight.pdf | 2025-02 | full |
| PCAOB-TAA-2024 | Notice of filing: Amendments related to technology-assisted analysis of information in electronic form (AS 1105, AS 2301); read via Federal Register through a text mirror | PCAOB / Federal Register | regulator | https://www.federalregister.gov/documents/2024/07/02/2024-14488/public-company-accounting-oversight-board-notice-of-filing-of-proposed-rules-on-amendments-related | 2024-07-02 | full |
| PCAOB-PRIORITIES-2025 | Spotlight: Staff Priorities for 2025 Inspections and Interactions With Audit Committees | PCAOB | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/2025-priorities-spotlight_v3.pdf | 2024-12 | full |
| FRC-ARAQ-2026 | Annual Review of Audit Quality 2026 | FRC | regulator | https://www.frc.org.uk/documents/9772/Annual_Review_of_Audit_Quality_2026_2eSTaw8P.pdf | 2026-07-22 | full (sections on specialists, technology, resourcing and firm appendices read by keyword location, not line by line) |
| FRC-GENAI-2026 | Generative and Agentic AI Guidance | FRC | regulator | https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 | full (reviewed sections located by keyword) |
| IFIAR-TECH-2026 | Use of technology in audits: Innovation and audit quality 2026 (news release page blocked; PDF text read from a copy saved in the landscape run) | IFIAR | regulator | https://www.ifiar.org/latest-news/ifiar-releases-2026-report-on-the-use-of-technology-in-audits/ | 2026-04-20 | full |
| AUASB-AI-2025 | Impact of AI on Auditors | AUASB | regulator | https://auasb.gov.au/publications/impact-of-ai-on-auditors/ | 2025-07 | full |
| AICPA-PA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | full |
| AT-AICPAPA-2026 | AICPA releases practice guide for auditors dealing with AI | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai | 2026-10-14 | full |
| IVSC-AI-2025 | Navigating the Rise of Artificial Intelligence in Valuation: Opportunities, Risks, and Standards | IVSC | standard-setter | https://ivsc.org/wp-content/uploads/2025/07/Navigating-the-Rise-of-AI-in-Valuation-Opportunities-Risks-and-Standards.pdf | 2025-07-23 | full |
| IVSC-IVSED-2026 | International Valuation Standards: Summary and Consultation Questions (IVS Exposure Draft, consultation 31 Jan to 30 Apr 2026) | IVSC | standard-setter | https://ivsc.org/_ivs_effective_31_january-2028_exposure-draft-summary-and-consultation-questions-final_ | 2026-01 | full |
| IVSC-DIALOGUE-2026 | IVSC Valuation Dialogue Series 2026, Sponsored by PwC (25 Jun 2026 session on AI) | IVSC | conference | https://ivsc.org/ivsc-valuation-dialogue-series-2026/ | 2026-06-25 | full (agenda page; session content not seen) |
| IVSC-AGM-2026 | IVSC AGM 2026 (Advisory Forum, 17 Nov 2026, Cologne) | IVSC | conference | https://ivsc.org/ivsc-agm-2026/ | 2026-06-17 | full (agenda page) |
| ICAS-IESBA-2026 | IESBA issues guidance on the ethical implications of emerging technologies | ICAS | professional-body | https://icas.com/news-insights-events/news/ethics/iesba-issues-guidance-on-the-ethical-implications-of-emerging-technologies/ | 2026-08-20 | full |
| BVR-BIGFOUR-2025 | Big Four investing heavily in AI (ASA Spring Fair Value Conference) | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/big-four-investing-heavily-in-ai | 2025-05-21 | full (date from search extract) |
| BVR-PANEL-2026 | Big Four panel: AI is reshaping the valuation talent pipeline | Business Valuation Resources | press | https://www.bvresources.com/articles/bvwire/big-four-panel-ai-is-reshaping-the-valuation-talent-pipeline | 2026-05-20 | full |
| BVR-BIGFOURLIMITS-2026 | How Big Four Firms Are Using, and Limiting, AI in Their Valuation Practices (teaser only) | Business Valuation Resources | press | https://www.bvresources.com/articles/business-valuation-update/how-big-four-firms-are-using-and-limiting-ai-in-their-valuation-practices | 2026-03 | search-only |
| BVR-FVGUIDANCE-2026 | Big Four Valuation Leaders Point to the Need for Fair Value Guidance (teaser lists AI governance among areas needing guidance) | Business Valuation Resources | press | https://www.bvresources.com/articles/business-valuation-update/big-four-valuation-leaders-point-to-the-need-for-fair-value-guidance | 2026-07 | search-only |
| BVR-ASA2026-2026 | Special Conference Report: Extended Coverage of the ASA Spring Fair Value Conference, May 7, 2026 (teaser only) | Business Valuation Resources | conference | https://www.bvresources.com/articles/bvresearch/special-conference-report-extended-coverage-of-the-asa-spring-fair-value-conference-may-7-2026 | 2026-05 | search-only |
| COHNREZNICK-VALUATION-2026 | CohnReznick's Valuation Advisory practice enhances valuation services through advanced analytics technology | CohnReznick | firm | https://www.cohnreznick.com/insights/cohnreznicks-valuation-advisory-enhanced-through-ai-analytics/ | 2026-03-26 | full |
| CPAPA-COHNREZNICK-2026 | CohnReznick's Valuation Advisory Practice Enhances Valuation Services | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/24/cohnreznicks-valuation-advisory-practice-enhances-valuation-services/180187/ | 2026-03-24 | full |
| VALUTICO-APR26-2026 | April 2026 Masterclass: Powering Smarter, More Connected Valuations | Valutico | vendor | https://help.valutico.com/en/articles/15773327-april-2026-masterclass-powering-smarter-more-connected-valuations | 2026-07-01 | full |
| VALUTICO-PARALOQ-2025 | Valutico Acquires AI Innovator Paraloq Analytics | Valutico | vendor | https://valutico.com/valutico-acquires-paraloq-analytics/ | 2025-06-24 | full |
| KPMGUK-BLUEJ-2024 | KPMG UK and Blue J expand strategic alliance to introduce generative AI into tax tools | KPMG UK | firm | https://kpmg.com/uk/en/media/press-releases/2024/02/kpmg-uk-and-blue-j-expand-strategic-alliance-to-introduce-generative-ai-into-tax-tools.html | 2024-02-22 | full |
| KPMG-ANTHROPIC-2026 | KPMG and Anthropic sign global alliance and launch digital gateway powered by Claude | KPMG | firm | https://kpmg.com/xx/en/media/press-releases/2026/05/kpmg-and-anthropic-sign-global-alliance-and-launch-digital-gateway-powered-by-claude.html | 2026-05-19 | search-only |
| FORVIS-RESERVING-2025 | Ten steps to help auditors evolve and adapt to AI reserving systems | Forvis Mazars (Ireland) | firm | https://www.forvismazars.com/ie/en/insights/news-opinions/steps-to-adapt-to-ai-reserving-systems | 2025 (estimated; page undated) | full |
| AAA-GENAI-2024 | Actuarial Professionalism Considerations for Generative AI | American Academy of Actuaries | professional-body | https://actuary.org/article/actuarial-professionalism-considerations-for-generative-ai/ | 2024 | full |
| SOA-GENAI-2026 | Model Governance/Ethics for GenAI Models: Practical Guide and Educational Handbook | Society of Actuaries Research Institute | professional-body | https://www.soa.org/resources/research-reports/2026/model-gov-ethics-for-gen-ai/ | 2026-09-23 | full (landing page; report PDF not downloaded) |
| ARXIV-GAUGE-2026 | One Analyst Is Not Ground Truth: Grading Agent-Built Financial Models Against Observed Professional Practice | arXiv | academic | https://arxiv.org/abs/2607.24889 | 2026-07-27 | full (abstract) |
| ARXIV-INSACTBENCH-2026 | INS-ActBench: A Comprehensive Benchmark for Assessing Professional Actuarial Capability of Large Language Models | arXiv | academic | https://arxiv.org/abs/2607.24273 | 2026-07-27 | full (abstract) |
| COMMERFORD-2022 | Man Versus Machine: Complex Estimates and Auditor Reliance on Artificial Intelligence | Journal of Accounting Research | academic | https://doi.org/10.1111/1475-679x.12407 | 2021-12 | full (abstract) |
| SSRN-LLMAQ-2026 | The Effect of Large Language Models on Audit Quality: Causal Evidence from a Randomized Field Experiment | SSRN | academic | https://doi.org/10.2139/ssrn.6095166 | 2026 | full (abstract via Crossref; SSRN page blocked) |
| HUX-2022 | Auditors' and Tax Specialists' Interprofessional Collaboration During Audit Engagements | SSRN (Hux, Andiola, Noga) | academic | https://doi.org/10.2139/ssrn.4260469 | 2022 | full (abstract via Crossref) |
| HIRSCH-2019 | The Effect of Spatial Distance and Domain Knowledge Distinctiveness on Auditor Reliance on IT Specialists | Journal of Information Systems | academic | https://doi.org/10.2308/isys-52456 | 2019-06-14 | full (abstract via Crossref) |
| BOARDMEMBER-CAQ-2026 | What Audit Partners Are Seeing On AI And What It Means For Audit Committees | Corporate Board Member (CAQ author) | survey | https://boardmember.com/?p=50023 | 2026-07-15 | full |
| CPACOM-ATR-2025 | 2025 Audit Transformation Report | CPA.com and AICPA | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 | full (p20 read) |
| GOINGCONCERN-PCAOB-2026 | Firms (and Some Guy Obsessed With China) Have Weighed in on the PCAOB Turning an Eye to AI | Going Concern | press | https://www.goingconcern.com/firms-and-some-guy-obsessed-with-china-have-weighed-in-on-the-pcaob-turning-an-eye-to-ai/ | 2026-08-12 | full |
| COMPUTERWORLD-FT-2026 | The Big Four accounting firms are now hiring more AI specialists than accountants (reporting an FT analysis of job postings; the FT piece was not opened) | Computerworld | press | https://www.computerworld.com/article/4173296/the-big-four-accounting-firms-are-now-hiring-more-ai-specialists-than-accountants.html | 2026-05-19 | full |
| ISACA-DEEPFAKE-2026 | The Audit Evidence Crisis: How AI Deepfakes Are Rewriting Assurance Standards | ISACA Now Blog | community | https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2026/the-audit-evidence-crisis-how-ai-deepfakes-are-rewriting-assurance-standards | 2026 | full |
| WK-AIEVIDENCE-2026 | AI-generated audit evidence: rethinking trust and authenticity | Wolters Kluwer | vendor | https://www.wolterskluwer.com/en/expert-insights/ai-generated-audit-evidence-rethinking-trust-authenticity | 2026-05-06 | search-only |

Source counts for this angle: 47 distinct documents listed (42 opened in full or in the relevant part, 5 search-only; FORVIS-RESERVING-2025 is opened but carries an estimated date). The landscape's own keys not reopened in this pass (BDO-ITGC-2026, COSO-GENAI-2026, REFGLOBAL-DCF-2026) are cited only in section 4 and the gaps and are not counted.

---

## 6. Gaps

- **No audit-side deployment evidence.** No named audit firm or regulator statement was found on AI use by audit-employed valuation, actuarial, tax, forensic or environmental specialists. Searches for firm-specific specialist tools (Omnia, Clara, EY Canvas) and for tax-provision AI agents returned only general agentic-AI coverage. No tax-specialist, environmental-specialist or forensic-specialist AI use case with a named organization exists in the sources read.
- **No measured outcomes for specialists.** No error rates, override rates, parallel-run results or inspection findings tied to AI use by specialists were found. The FRC's 2026 review shows specialist-related findings but none mention AI.
- **ISA 500 and management's expert.** The IAASB's August 2026 exposure drafts of ISA 330, 500 and 520 sit behind a login on the IAASB site, so the proposed treatment of management's experts and tools was not read. The IAASB consultations page lists the comment period as "July 28 to December 15" while the project page shows 5 Aug 2026 as the publication date (the landscape used 5 Aug); the discrepancy was not resolved.
- **ISA 620 basis for conclusions** and the IESBA Code's new external-expert provisions were not opened; the IESBA Code text and the IAASB amendments themselves were read only through the UK standard and the FRC feedback statement.
- **PCAOB primary pages.** `pcaobus.org` pages for AS 1210, AS 1105 Appendix A, the 2018-2019 specialists release and the TAA adopting release were blocked or unreached (the Federal Register API was blocked mid-session). Specialist requirements were read through the PCAOB's February 2025 Spotlight, and the TAA amendments through the Federal Register notice of filing. The Federal Register order approving the TAA amendments (23 Aug 2024) was seen only as a title in a search listing.
- **SSRN paper.** Only the abstract of the inventory-valuation field experiment was reached (SSRN blocked, Crossref used). Effect sizes, firm identity and task details are unknown.
- **Paywalled or login material.** BV Resources articles on KPMG's AI push (10 Jun 2026) and the March 2026 Big Four valuation article were teaser-only; the AICPA practice aid full text is behind a login; the SOA guide PDF was not downloaded; the Reference Global DCF paper (landscape A14) was not located.
- **Dates not found.** FORVIS-RESERVING-2025 and ISACA-DEEPFAKE-2026 show no month of publication; BVR-BIGFOUR-2025's date came from a search extract; the AAA paper's first release date was not found.
- **Conference sessions.** The IVSC 25 Jun 2026 AI session content and the 17 Nov 2026 Advisory Forum session were seen as agendas only. The 2026 ASA conference's Big Four panel was seen as a teaser. No recording, transcript or podcast on specialists and AI was found. Forensic and valuation conferences (for example the AICPA & CIMA forensic and valuation services conference) were not searched.
- **Job postings.** No actual valuation, actuarial or tax specialist job postings were found. The only posting-based evidence is a press report of an FT analysis (not opened) covering AI roles across the Big Four.
- **Community discussion.** No practitioner-forum material on specialists and AI was reachable (Reddit blocked per landscape); the only community item is one ISACA blog post by a single author.
- **IFIAR 2026.** The IFIAR news release page returned a Cloudflare block; the report text was read from a copy saved earlier in the session, and the PDF's own URL was not recorded.

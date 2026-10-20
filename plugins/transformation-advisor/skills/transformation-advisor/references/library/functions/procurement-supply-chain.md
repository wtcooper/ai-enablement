# Procurement and supply chain

Function id `procurement-supply-chain`. Last reviewed 2026-10-20. Source keys in brackets are listed in §8. **Read this first:** the
best measured supply-chain results (Walmart and UPS routing) come from optimization, not generative AI. The one widely cited AI
negotiation case (Walmart with a negotiation-bot vendor) has vendor-published figures reported second-hand. Independent evidence on
AI negotiation comes only from experiments. Gartner's 2026 survey of 101 CPOs describes individual gains that fade at team level
[GARTNER-2026].

## Contents

1. [What this function covers](#1-what-this-function-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Metrics and benchmarks](#4-metrics-and-benchmarks)
5. [Interview probes](#5-interview-probes)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Sources](#8-sources)

## 1. What this function covers

Procurement (sourcing, contracting, purchasing, supplier management) and supply-chain planning and execution in any organization.
The SCOR standard describes seven process groupings: Orchestrate, Plan, Order, Source, Transform, Fulfill, Return [ASCM-2026]. No
archetype covers firms that sell procurement or logistics services; use this card. In-house buyers of legal and advisory services
appear in the professional-services archetype (outside-counsel guidelines, proposal comparison).

## 2. Processes and key steps

| Process | Key steps | Work types | Typical pain |
|---|---|---|---|
| Plan (demand, supply, inventory) | Determine requirements; gather resource information; balance requirements and resources; act on gaps [ASCM-2026] | data-reporting, coordination-scheduling, expert-judgment | No measured in-house AI case found; one consultancy proof of concept (see §3) |
| Source (procure) | Spend analysis; sourcing events; negotiation; contracting; ordering and receipt | research-synthesis, expert-judgment, document-production, transaction-processing | Buyers cannot negotiate with every supplier: around 20% of Walmart's 100,000-plus suppliers had agreements with terms that were often not negotiated [HBR-2022] |
| Supplier management and risk | Onboarding; performance; risk monitoring; alternative sources | review-assurance, research-synthesis, coordination-scheduling | Siloed ways of working are the top barrier to value (57%), then competing priorities (46%) (survey of 250+ CPOs) [DELOITTE-2025] |
| Contracting in the public sector | Document validation; regulatory review; award | review-assurance, document-production | Long acquisition lead times by acquisition type [NPS-2026] |
| Transform and Fulfill (where in scope) | Schedule production; pick, pack, ship, invoice [ASCM-2026] | physical-field, coordination-scheduling, transaction-processing | Routing and loading at network scale (see §3) |
| Return | Reverse flow of goods and services [ASCM-2026] | transaction-processing, physical-field | No measured AI case found |
| Orchestrate and pay | Business rules, network design, contracts, compliance, risk; supplier payment | expert-judgment, review-assurance | Business email compromise targets businesses that work with suppliers and regularly make wire transfers [FBI-2025] |

## 3. Where AI is changing the work

**Improve the step** (assist or augment)

- **Contract and document review in contracting, with a person in the loop**
  ([document-to-decision](../patterns/document-to-decision.md); augment; step). 39th Contracting Squadron, Incirlik Air Base (defense,
  public sector): an AI assistant for document validation and regulatory review, prototype under development with a vendor; the
  paper's lead-time reductions (for example 34% projected at scale) are vendor-authored projections, not measurements. Grade B
  [NPS-2026].
- **Scope RFPs and compare supplier or adviser proposals** ([document-to-decision](../patterns/document-to-decision.md); augment;
  process). Archetype entry `professional-services-pursuit-proposals-20` (C).

**Automate the flow**

- **Negotiate with tail suppliers who were not negotiated before**
  ([end-to-end-case-agent](../patterns/end-to-end-case-agent.md), bounded; automate; process). Walmart (retail) with a negotiation-bot
  vendor: a chatbot negotiates price, payment terms and other items for smaller contracts with equipment suppliers. The vendor's
  January 2023 release reported deals closed with 68% of suppliers approached and 3% average savings; Bloomberg reported nearly three in four suppliers
  preferred the bot. Vendor-published, reported second-hand. Grade B [PYMNTS-2023; HBR-2022].
- **Optimize truck routing and loading; link network planning to daily execution**
  ([monitor-diagnose-act](../patterns/monitor-diagnose-act.md); automate; process). Walmart (retail logistics): in FY23, 108,000 routes
  and 33 million miles eliminated and $91.5 million saved, per the paper; the award release gives $75 million and 72 million pounds of
  CO2 instead of 98.6 million, and neither source explains the difference. Self-reported; optimization, not generative AI. Grade A
  [INFORMS-2024; INFORMS-2023].
- **Optimize delivery routes** ([monitor-diagnose-act](../patterns/monitor-diagnose-act.md); automate; process). UPS ORION
  (logistics): more than $320 million saved as of December 2015, with over 35,000 of 55,000 US drivers using it. Self-reported award
  summary; older, pre-generative AI. Grade A [INFORMS-2016].
- **Supplier risk monitoring and alternative sourcing** ([monitor-diagnose-act](../patterns/monitor-diagnose-act.md); automate;
  process). Surveyed CPOs rate active alternative sources (74%), supply-chain visibility (64%) and supplier information sharing (61%)
  as effective risk strategies; no measured AI deployment found. Grade C [DELOITTE-2025].
- **Demand forecasting** ([monitor-diagnose-act](../patterns/monitor-diagnose-act.md); automate; process). A consultancy proof of
  concept at an unnamed grocery retailer (about 150 stores, 500 products) reports 33% lower forecast error than the retailer's
  current software (machine learning, not generative AI; consultancy-published). Grade C [SUPCHAINS-2025].

**Delegate the outcome**

- **Agents that plan across demand, supply and logistics** ([end-to-end-case-agent](../patterns/end-to-end-case-agent.md); delegate;
  process). Idea; no public deployment with results found. Grade D.

**Reinvent the work**

- **Buying AI-enabled managed services and pressing suppliers to share AI savings.** Archetype entries:
  `tax-compliance-corporate-15` (C, compliance bought as an AI-enabled managed service) and
  `professional-services-scoping-pricing-11` (B, AI-savings terms in outside-counsel guidelines).

**In the archetypes**: `professional-services-scoping-pricing-11` (B), `professional-services-firm-finance-08` (B, licence decisions
gated on weekly active use), `professional-services-pursuit-proposals-20` (C), `professional-services-client-development-17` (C),
`assurance-quality-management-06` (C, due diligence on third-party AI tools), `tax-compliance-corporate-15` (C).

## 4. Metrics and benchmarks

- **Negotiation (vendor-reported):** 68% of suppliers closed, 3% average savings, 83% found the bot easy to use, 2,000 suppliers
  negotiated at once; deals closed in days rather than weeks per Bloomberg [PYMNTS-2023].
- **Returns on generative AI (survey):** top-quartile "Digital Masters" report an average 3.2x return; followers projected slightly
  above 1.5x (self-reported by surveyed CPOs) [DELOITTE-2025].
- **Where cost falls:** supply-chain management is among the functions most often reporting AI cost reductions (global survey)
  [MCKINSEY-SOAI-2026].
- **Routing:** routes, miles, CO2 and dollars (Walmart); dollars and fuel (UPS) [INFORMS-2024; INFORMS-2016].
- **Readiness to redesign:** 36% of CPOs are very confident they can redesign roles and processes around AI [GARTNER-2026].
- **Not found:** a benchmark for contract cycle time, spend under management or savings rate from a source that could be opened.

## 5. Interview probes

1. "What share of suppliers or spend gets a negotiated deal, and what is left on standard terms?" Reveals tail-spend scope
   [HBR-2022].
2. "What may a bot agree to, and where does it hand back to a buyer?" Reveals bounds and escalation; Walmart limited its bot to
   smaller contracts [PYMNTS-2023].
3. "Does the relationship with this supplier matter after the deal?" Reveals the trust cost of a competitive bot [HEROLD-2025].
4. "Who owns the redesign of buyer roles, and which tasks are innately human?" Reveals the gap between individual gains and team
   outcomes [GARTNER-2026].
5. "What is the lead time from request to contract, by type of purchase?" Reveals the baseline for cycle-time claims [NPS-2026].
6. "How do you verify a changed supplier bank detail?" Reveals payment-fraud exposure [FBI-2025].
7. "Where does planning sit relative to sourcing?" Reveals whether a process-level change across Plan and Source is in scope
   [ASCM-2026].
8. "What do you measure after go-live that is not hours?" Reveals value capture; Gartner advises aligning gains to financial
   outcomes [GARTNER-2026].
9. "Which suppliers are critical, and how do you find alternatives today?" Reveals the risk-monitoring opportunity [DELOITTE-2025].

## 6. Guardrails

- **Bound the bot's scope.** Walmart's chatbot negotiates only smaller contracts with equipment suppliers, not goods for sale
  (Bloomberg, via PYMNTS) [PYMNTS-2023].
- **Choose the negotiation stance deliberately.** In experiments, a competitively prompted buyer chatbot won a higher discount, better
  payment terms and quicker deals, while suppliers trusted a collaboratively prompted one more and wanted future interaction more
  [HEROLD-2025].
- **Watch fairness and concession patterns.** In bargaining games, LLMs favored conservative, concessionary proposals while humans
  followed fairness norms; similar total surplus can hide different procedures [QIAN-2025].
- **Verify payments and bank-detail changes** outside the channel that requested them (advisor rule drawn from the fraud reports)
  [FBI-2025].
- **EU AI Act:** Annex III high-risk categories cover employment and credit uses; ordinary supplier negotiation and sourcing are not
  listed [EU-AIACT-ANNEX3-2024].
- **Decisions that need human judgment:** supplier strategy; critical or high-value contracts; trade-offs between price and
  relationship; exceptions that cross policy.

## 7. Roles and how they evolve

- **Buyers move to larger contracts** while the bot handles the tail (Bloomberg, via PYMNTS) [PYMNTS-2023].
- **Roles are redesigned by task:** Gartner recommends separating "innately human" tasks from "AI-native" ones, aligning gains to
  financial outcomes and updating productivity measures [GARTNER-2026].
- **Technology and talent together:** a Deloitte principal says organizations that prioritize both technology modernization and
  talent investment are better able to thrive (a statement in the survey release, not a reported measure) [DELOITTE-2025].

## 8. Sources

- **ASCM-2026**: ASCM, *SCOR Digital Standard* (professional body, accessed 2026-10-20). https://www.ascm.org/corporate-transformation/standards-tools/scor-ds/
- **DELOITTE-2025**: Deloitte US, *Procurement at the Tipping Point: 2025 Chief Procurement Officer Survey* (survey release, 2025-08-19). https://deloitte.com/us/en/about/press-room/2025-chief-procurement-officer-survey.html
- **EU-AIACT-ANNEX3-2024**: Regulation (EU) 2024/1689, *Annex III: High-risk AI systems* (regulation text via artificialintelligenceact.eu, 2024). https://artificialintelligenceact.eu/annex/3/
- **FBI-2025**: FBI Internet Crime Complaint Center, *2024 IC3 Annual Report* (regulator, 2025). https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf
- **GARTNER-2026**: Gartner, *Just 36% of Chief Procurement Officers Are Very Confident in Ability to Redesign Function for AI* (survey release, n=101, 2026-05-19). https://gcom.pdo.aws.gartner.com/en/newsroom/press-releases/2026-05-19-gartner-survey-shows-just-36-perecent-of-chief-procurement-officers-are-very-confident-in-ability-to-redesign-function-for-ai
- **HBR-2022**: Van Hoek et al., Harvard Business Review, *How Walmart Automated Supplier Negotiations* (press, 2022-11-08; paywalled beyond the opening). https://hbr.org/2022/11/how-walmart-automated-supplier-negotiations
- **HEROLD-2025**: Herold et al., *Brave new procurement deals: an experimental study of how generative AI chatbots negotiate*, Journal of Purchasing and Supply Management (academic, 2025-10). https://cris.maastrichtuniversity.nl/en/publications/brave-new-procurement-deals-an-experimental-study-of-how-generati/
- **INFORMS-2016**: INFORMS, *UPS On-Road Integrated Optimization and Navigation (ORION) Project* (professional body, 2016). https://www.informs.org/Impact/O.R.-Analytics-Success-Stories/UPS-On-Road-Integrated-Optimization-and-Navigation-ORION-Project
- **INFORMS-2023**: INFORMS, *Walmart Awarded the 2023 INFORMS Edelman Award* (professional body, 2023-04). https://www.informs.org/News-Room/INFORMS-Releases/Awards-Releases/Operations-Research-Enhances-Retail-Truck-Routing-and-Load-Planning-Walmart-Awarded-the-2023-INFORMS-Edelman-Award
- **INFORMS-2024**: Mehrotra et al., *Optimizing Walmart's Supply Chain from Strategy to Execution*, INFORMS Journal on Applied Analytics 54(1) (academic, 2024-01). https://courses.ie.bilkent.edu.tr/ie479/wp-content/uploads/sites/16/2024/11/Optimizing-Walmarts-Supply-Chain-from-Strategy-to-Execution.pdf
- **MCKINSEY-SOAI-2026**: McKinsey, *The state of AI in 2026: On the road to ROI* (survey, n=1,719, 2026-08-25). https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- **NPS-2026**: Eudia authors, *Augmented Acquisition: Operationalizing Human-in-the-Loop AI to Accelerate Warfighting Capabilities*, prepared for the Naval Postgraduate School Acquisition Research Symposium (vendor-authored paper, 2026-04-30). https://dair.nps.edu/bitstream/123456789/5528/1/SYM-AM-26-091.pdf
- **PYMNTS-2023**: PYMNTS, *Walmart Reportedly Finds 75% of Vendors Prefer Negotiating With Chatbot* (press, 2023-04-26). https://www.pymnts.com/news/artificial-intelligence/2023/walmart-finds-75-percent-vendors-prefer-negotiating-with-chatbot/
- **QIAN-2025**: Qian et al., *Humans, LLMs and Bayesian agents in multi-player bargaining* (academic, arXiv 2509.09071, 2025-09). https://arxiv.org/abs/2509.09071
- **SUPCHAINS-2025**: N. Vandeput, *Retail demand forecasting: reducing the error by 33%* (consultancy, 2025-06-16). https://nicolas-vandeput.medium.com/retail-demand-forecasting-reducing-the-error-by-33-3aeba728954f

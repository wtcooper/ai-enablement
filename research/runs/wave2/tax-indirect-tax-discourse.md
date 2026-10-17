# Module deep dive: tax / indirect-tax / discourse

- **Archetype:** tax
- **Module:** indirect-tax. VAT, GST and sales and use tax: determination and rates, exemption certificates, returns, e-invoicing and continuous transaction controls (ViDA, Peppol), marketplace and digital-services rules, tax in agentic commerce, indirect-tax audits; state and local sales tax.
- **Angle:** discourse. What practitioners are saying in the last 12-18 months: conference sessions and recaps, panels, webinars, podcasts, practitioner articles and trade press; where the field says it is heading and what worries it.
- **Prepared:** 2026-10-17
- **Method note.** About 55 pages were opened with `curl` (HTML text extraction; `pdftotext` for one PDF; the `r.jina.ai` mirror for two pages that blocked `curl`). Web search was rationed and then ran out during the task (see Gaps), so some planned searches did not run. Conference sessions were read through programmes and written recaps only. Podcasts were read through show-note or episode descriptions only; no audio or transcript was reached, so no podcast is used for a specific claim beyond its description. Reddit, LinkedIn and other forums were not reachable (see Gaps). Vendor-authored thought leadership is a large share of what is public in this module; it is labelled as such and no vendor figure is presented as independent.

---

## 1. Summary

1. **The indirect-tax conversation has two halves that meet at the transaction.** One half is regulatory: continuous transaction controls (CTC), clearance e-invoicing and ViDA are moving tax risk from filing time to invoice time. A Thomson Reuters Institute recap of the TEI Tax Technology Seminar (Apr 2026) reports more than 60 jurisdictions moved or moving to CTC, and a panel view that authorities now arrive at audits already holding structured data they have analysed (TRINST-TEIAUDITOR-2026). The Vertex Exchange Europe recap says "VAT risk now surfaces at the invoice itself" (INNOVATETAX-VXE-2026). The other half is AI: vendors moved from "AI-assisted" to agents that prepare and, after approval, file (TR-SUTAI-2026, AVALARA-AGENTIC-2025, AVALARA-CRUSHEU-2026, SOVOS-SOVI-2026).
2. **The shared position is: AI orchestrates, researches and handles exceptions; deterministic engines do the tax calculation; a person stays accountable.** Thomson Reuters, Fonoa, Avalara, Vertex and Sovos all say a version of this (TR-AGENTICIT-2026, FONOA-STACK-2025, AVALARA-CRUSHEU-2026, INNOVATETAX-VXE-2026, SOVOS-SOVI-2026). Avalara's CEO put it as "the person accountable is still a person" (AVALARA-CRUSHEU-2026). That is a consistent vendor message, not an independent finding.
3. **Audit defensibility is the gating worry, and the only survey measure of it is vendor-sponsored.** In Fonoa's survey of 176 indirect tax leaders, 57.4% said they would not be confident defending AI-assisted decisions to a tax authority, and only a third run formal human-in-the-loop review (FONOA-2026-SURVEY). Only 12.5% have specific AI targets or KPIs (same source).
4. **There is no independent quality evidence for AI in indirect tax.** No error rate, override rate, parallel-run result or inspection finding was found for product classification, certificate validation, return preparation or e-invoice handling. The figures in circulation are vendor claims (up to 65% less time on routine reporting, up to 75% less audit exposure: TR-SUTAI-2026), a vendor's single illustrative rate-lookup test (AVALARA-LLMTEST-2025), a practitioner's anecdote that a first AI draft on Florida sales tax had about five serious errors (FLSALESTAX-AI-2026), and illustrative arithmetic (FONOA-ACCURACY-2025). This is stated plainly in the use cases.
5. **Agentic commerce is the new frontier topic, and the practical answer so far is "keep tax in the merchant's stack".** Practitioners ask who collects when an agent completes a purchase (BTAX-AGENTIC-2026) and whether agents can apply rules such as sales tax holidays (STI-AGENTIC-2026). The Sales Tax Institute notes most agentic commerce models rely on the merchant's existing tax determination systems. No regulator guidance was found.
6. **Authorities are also using AI on indirect tax.** Hungary's 2026 audit plan says the tax authority uses AI-based models, including at invoice issuance (KPMGHU-AUDITPLAN-2026). South Carolina's revenue department signed a five-year contract to use AI in audit selection, starting with sales and use tax (SCPOST-AUDIT-2026). A Tax Notes survey found 22 of 36 responding state agencies said they did not use AI at all (TAXNOTES-UNWATCHED-2026). These are routed to the controversy module and used here as context.
7. **Evidence mix.** 15 candidate use cases: 0 grade A, 0 grade B, 14 grade C, 1 grade D. Sources are 48 rows across seven types (vendor 20, conference 10, press 10, firm 3, podcast 3, survey 1, academic 1). No community source could be reached. Eight of the rows are coverage-only (see section 5).

---

## 2. Use cases

Notes on fields. `maturity` is `announced` where the only evidence is a vendor announcement, product documentation or webinar, even where a product page describes a working feature, because no named customer use was found. Figures are vendor claims unless stated. `function` is `finance-accounting` for in-house tax operations and `service-delivery` for adviser-delivered work.

```yaml
- id: tax-indirect-tax-01
  title: "AI suggestions for product-to-tax-code classification, reviewed by a person"
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [transaction-processing, data-reporting]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >
    Correct tax calculation depends on each product being mapped to the right tax code, and large catalogues make
    manual mapping slow and error-prone [SOVOS-DOCS-AICLASS]. Fonoa lists misclassified product taxability,
    especially across thousands of products, among common tax-specific errors [FONOA-ERRORRATE-2025].
    Agents buying on a consumer's behalf also depend on catalogue metadata being correctly classified [STI-AGENTIC-2026].
  solution: >
    The tool reads a product description and category and returns up to three ranked tax-code suggestions, each with
    a confidence level (Sovos) or a similarity score (Thomson Reuters ONESOURCE), which a person accepts, compares or
    overrides, optionally recording a rationale [SOVOS-DOCS-AICLASS] [TR-HELP-PRODCLASS]. Avalara says its Aviator
    agent hub can map products to tax codes [AVALARA-CRUSHEU-2026]. Vertex showed AI that helps classify products,
    under guardrails of explainability, reversibility, auditability and human oversight [INNOVATETAX-VXE-2026].
  outcomes:
    - lever: speed
      description: >
        Sovos documentation says suggestions arrive "in seconds" rather than after manual research. No time saving
        or accuracy figure is published.
      figure: "n/a"
      measures: "no figure published"
      provenance: vendor-published
      source_ref: SOVOS-DOCS-AICLASS
  prerequisites:
    - "Complete, specific product descriptions, because documentation says detail improves suggestions [SOVOS-DOCS-AICLASS]."
    - "A product catalogue and master-data process that can carry the chosen tax code through to invoicing [INNOVATETAX-VXE-2026]."
  risks_and_guardrails:
    - "Sovos warns that a high confidence score does not guarantee the code is correct and tells users always to review suggestions before mapping [SOVOS-DOCS-AICLASS]."
    - "Weak product classifications surface at the point of invoice under e-invoicing and real-time reporting [INNOVATETAX-VXE-2026]."
    - "Customers can opt out of Sovos AI classification by raising a support case [SOVOS-DOCS-AICLASS]."
  human_checkpoints:
    - "A person confirms or overrides each suggested code, and may record a rationale of up to 500 characters in ONESOURCE [TR-HELP-PRODCLASS]."
    - "Low and very low confidence suggestions are reviewed or sent back for more product detail [SOVOS-DOCS-AICLASS]."
  role_evolution: >
    The Vertex Exchange Europe recap describes the future tax team as hybrid, combining tax knowledge with comfort
    around ERP landscapes, data, automation and AI [INNOVATETAX-VXE-2026]. No source describes a change in headcount
    for classification work.
  evidence_grade: C
  sources:
    - { ref: SOVOS-DOCS-AICLASS, title: "About AI product classification", publisher: Sovos, type: vendor, url: "https://docs.sovos.com/en/indirect-tax/indirect-tax-products/tax-determination/tax-determination/map-products-exemptions-and-locations/ai-product-classification/about-ai-product-classification", date: 2026-10-17, access: full, locator: "How it works; Confidence level table; CAUTION note (page undated, retrieved date used)" }
    - { ref: TR-HELP-PRODCLASS, title: "Review product classification results", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en-us/help/onesource-indirect-tax/indirect-tax-compliance/mappings/product-classification/review-product-classification-results", date: 2026-10-17, access: full, locator: "Review AI-generated suggestions; Confirm Your Selection and Rationale (page undated, retrieved date used)" }
    - { ref: INNOVATETAX-VXE-2026, title: "What we learned from Vertex Exchange Europe 2026", publisher: Innovate Tax, type: conference, url: "https://innovatetax.com/blog/what-we-learned-from-vertex-exchange-europe-2026/", date: 2026-05-06, access: full, locator: "section 'AI is becoming a default expectation, but not a replacement for tax judgment'" }
    - { ref: AVALARA-CRUSHEU-2026, title: "Avalara Helps Global Businesses Move Faster as Tax and Compliance Complexity Accelerates", publisher: Avalara (PR Newswire), type: conference, url: "https://www.webdisclosure.com/press-release/avalara-helps-global-businesses-move-faster-as-tax-and-compliance-complexity-accelerates-WEpMYuY5kxr", date: 2026-10-08, access: full, locator: "section 'New purpose-built agentic AI solutions'" }
    - { ref: FONOA-ERRORRATE-2025, title: "Your 'Accurate' Tax Process Probably Has a 20% Error Rate", publisher: Fonoa, type: vendor, url: "https://www.fonoa.com/resources/blog/accurate-tax-process-error-rate", date: 2025-11-11, access: full, locator: "section 'Human tax processes fail more often than anyone wants to admit'" }
    - { ref: STI-AGENTIC-2026, title: "Can AI Shopping Agents Apply Sales Tax Holidays?", publisher: Sales Tax Institute, type: press, url: "https://www.salestaxinstitute.com/resources/ai-shopping-agents-sales-tax-holidays", date: 2026-07-29, access: full, locator: "section 'Where the Responsibility Actually Lands'" }
  last_reviewed: 2026-10-17
  notes: >
    Vendor documentation and announcements only. No named customer, accuracy rate or override rate was found.
    A quoted claim of "85-95% accuracy" for AI classification appeared only in a search summary of a vendor blog and
    was not opened, so it is not used.

- id: tax-indirect-tax-02
  title: "AI validation and routing of exemption certificates at receipt"
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [transaction-processing, review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >
    Exemption certificates are one of the most manual, time-consuming areas of tax compliance, and certificate errors
    can lead to audit exposure and penalties [AVALARA-ECM-2026]. Incomplete certificate data also causes problems at
    the point of invoice under e-invoicing [INNOVATETAX-VXE-2026].
  solution: >
    Avalara says its Exemption Certificate Management product can validate certificates automatically, spotting
    missing fields and flagging potential errors, and can ingest, classify, validate and route certificates at scale
    with intelligent document processing, plus natural-language search over the certificate store [AVALARA-ECM-2026].
    Avalara lists validating exemption certificates among tasks of its Aviator agent hub [AVALARA-CRUSHEU-2026].
  outcomes:
    - lever: quality
      description: >
        Avalara says AI review finds missing fields and errors "faster and more accurately than manual reviews". It
        publishes no error rate, volume or time figure.
      figure: "n/a"
      measures: "no figure published"
      provenance: vendor-published
      source_ref: AVALARA-ECM-2026
  prerequisites:
    - "Certificates captured in a system that can ingest documents and route them to a workflow [AVALARA-ECM-2026]."
    - "Complete certificate and customer master data, which the Vertex Exchange Europe recap names as a recurring weakness [INNOVATETAX-VXE-2026]."
  risks_and_guardrails:
    - "A wrong validation exposes the seller to the audit and penalty risk the tool is meant to reduce [AVALARA-ECM-2026]."
    - "No independent evaluation of validation accuracy was found."
  human_checkpoints:
    - "Flagged or failed certificates route to a person; the source describes \"routing\" but not the exact review step [AVALARA-ECM-2026]."
  role_evolution: >
    Avalara says automation lets tax teams spend less time on paperwork and more on strategy [AVALARA-ECM-2026]. No
    independent source describes a role change.
  evidence_grade: C
  sources:
    - { ref: AVALARA-ECM-2026, title: "How AI Improves Exemption Certificate Management", publisher: Avalara, type: vendor, url: "https://www.avalara.com/blog/en/north-america/2026/02/ai-exemption-certificate-management.html", date: 2026-02-23, access: full, locator: "sections 'AI-powered certificate validation' and 'Intelligent document processing + automated workflows'" }
    - { ref: AVALARA-CRUSHEU-2026, title: "Avalara Helps Global Businesses Move Faster as Tax and Compliance Complexity Accelerates", publisher: Avalara (PR Newswire), type: conference, url: "https://www.webdisclosure.com/press-release/avalara-helps-global-businesses-move-faster-as-tax-and-compliance-complexity-accelerates-WEpMYuY5kxr", date: 2026-10-08, access: full, locator: "section 'New purpose-built agentic AI solutions'" }
    - { ref: INNOVATETAX-VXE-2026, title: "What we learned from Vertex Exchange Europe 2026", publisher: Innovate Tax, type: conference, url: "https://innovatetax.com/blog/what-we-learned-from-vertex-exchange-europe-2026/", date: 2026-05-06, access: full, locator: "section 'Master data came up a lot'" }
  last_reviewed: 2026-10-17
  notes: >
    A Wolters Kluwer CERTifyTax webinar (11 Jun 2026) and further Avalara webinars (23 Apr and 24 Sep 2026) were seen in
    a search summary only and are not used.

- id: tax-indirect-tax-03
  title: "Agentic sales and use tax return preparation with approval before filing"
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [transaction-processing, data-reporting]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >
    Sales and use tax reporting spans more than 19,000 US jurisdictions and is described as complex and manual,
    with data import, validation and return mapping consuming the compliance cycle [TR-SUTAI-2026]. Thomson Reuters
    says 58% of corporate tax departments report being under-resourced and that tax professionals spend 56% of
    their time on reactive, basic tasks [TR-AGENTICIT-2026].
  solution: >
    Thomson Reuters' ONESOURCE Sales and Use Tax AI uses CoCounsel agents to import data, validate it and map it to
    returns, with users keeping final review and sign-off, and electronic filing in 33 states plus Canada
    [TR-SUTAI-2026]. Avalara describes a Returns AI agent that ingests transaction data, calls its Returns APIs,
    applies forms and jurisdictional logic, and files on the client's behalf upon approval [AVALARA-AGENTIC-2025].
    Both vendors keep the tax calculation in a rule-based engine, with AI handling reasoning and orchestration
    [TR-AGENTICIT-2026].
  outcomes:
    - lever: speed
      description: "Thomson Reuters says the tool reduces time spent on routine reporting."
      figure: "up to 65%"
      measures: >
        "time spent on routine reporting" reduced, per the vendor release; baseline, sample and measurement method
        not stated
      provenance: vendor-published
      source_ref: TR-SUTAI-2026
    - lever: speed
      description: "Thomson Reuters says compliance cycles for large enterprises fall from 30 days to 11 days."
      figure: "30 days to 11 days"
      measures: "compliance cycle length for \"large enterprises\", per the vendor release; customers not named"
      provenance: vendor-published
      source_ref: TR-SUTAI-2026
    - lever: risk
      description: "Thomson Reuters says early customers report lower audit exposure through automated validation and audit documentation."
      figure: "up to 75%"
      measures: "\"reduction in audit exposure\" reported by \"early customers\", per the vendor release; no definition of exposure or number of customers"
      provenance: vendor-published
      source_ref: TR-SUTAI-2026
    - lever: cost
      description: "Thomson Reuters gives annual savings for small and large enterprises."
      figure: "about $25,000 (small), $60,000 or more (large) per year"
      measures: "\"save approximately $25,000 annually in time and efficiency\" (small enterprises) and \"$60,000 or more\" (large), per the vendor release; method not stated"
      provenance: vendor-published
      source_ref: TR-SUTAI-2026
  prerequisites:
    - "Clean transaction data feeding the return process; the vendors pair the agent with determination and calculation engines [TR-SUTAI-2026]."
    - "A defined governance model: Thomson Reuters says policies for AI decision oversight, audit-trail standards and human review checkpoints do not write themselves [TR-AGENTICIT-2026]."
  risks_and_guardrails:
    - "Thomson Reuters says every agent decision is documented with rationale, timestamps and reviewer sign-offs, and that deterministic engines do the tax math [TR-AGENTICIT-2026]."
    - "A practitioner warning in the sales tax holiday discussion applies by analogy: automation can accelerate errors if rule configurations are out of date [STI-AGENTIC-2026]."
    - "TEI attendees reported that errors are increasingly quiet and technical, which makes review harder as volumes rise [TEI-TAXTECH-2026]."
  human_checkpoints:
    - "Final review and approval before filing [TR-SUTAI-2026]."
    - "Avalara says agents notify a person for novel situations and for key decisions that affect the compliance footprint [AVALARA-AGENTIC-2025]."
  role_evolution: >
    Thomson Reuters says preparation that took days narrows to hours of review and sign-off and capacity moves to
    policy, monitoring and advisory work [TR-AGENTICIT-2026]; this is a vendor projection.
  evidence_grade: C
  sources:
    - { ref: TR-SUTAI-2026, title: "Thomson Reuters Launches AI Tax Compliance Solution That Saves Time and Reduces Risk (ONESOURCE Sales and Use Tax AI)", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2026/january/thomson-reuters-launches-ai-tax-compliance-solution-that-saves-time-and-reduces-risk", date: 2026-01-15, access: full, locator: "bullet list 'measurable impact from day one'; paragraph on 'Touchless Compliance'" }
    - { ref: AVALARA-AGENTIC-2025, title: "Avalara launches 'always on, always ready' AI agents", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/avalara-launches-always-on-always-ready-ai-agents", date: 2025-09-30, access: full, locator: "paragraphs on Returns AI and on human review" }
    - { ref: TR-AGENTICIT-2026, title: "Is your tax department ready for the agentic AI explosion?", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/is-your-tax-department-ready-for-the-agentic-ai-explosion/", date: 2026-06-08, access: full, locator: "sections 'The governance gap' and 'Why the right partner matters'" }
    - { ref: STI-AGENTIC-2026, title: "Can AI Shopping Agents Apply Sales Tax Holidays?", publisher: Sales Tax Institute, type: press, url: "https://www.salestaxinstitute.com/resources/ai-shopping-agents-sales-tax-holidays", date: 2026-07-29, access: full, locator: "section 'Where the Responsibility Actually Lands'" }
    - { ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: 2026-05-04, access: full, locator: "section 'A very bad wizard'" }
  last_reviewed: 2026-10-17
  notes: >
    Vendor-published figures only; customers are unnamed. The release says the product is available now for US
    corporations and accounting firms. Avalara's 9 Apr 2026 "AI-executed" release was not reachable (page returned 404),
    so only its 30 Sep 2025 launch is used.

- id: tax-indirect-tax-04
  title: "Agent diagnosis and approved remediation of e-invoice and filing errors"
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [transaction-processing, review-assurance]
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >
    Under clearance e-invoicing an invoice has no legal force until the tax authority returns an identifier, so a
    wrong VAT ID, malformed schema or mismatched master data means the invoice is rejected and goods and payment can
    stall [TRINST-TEIAUDITOR-2026]. Fonoa says more than 70 countries have added or changed e-invoicing rules since
    2020 [FONOA-REGMON-2026].
  solution: >
    Sovos announced Sovi AI error diagnosis and remediation, which it says diagnoses root causes, proposes fixes and
    executes corrections once a user approves, and "proactive issue detection" before filing deadlines
    [SOVOS-SOVI-2026]. Sovos' later release names "e-invoice error diagnosis" and "data reconciliation" among
    pre-built agents in Sovi Agent Studio [SOVOS-FLOWIE-2026]. Thomson Reuters demoed AI-driven exception handling
    and VAT ID validation in ONESOURCE Indirect Compliance powered by CoCounsel [TR-WEBINAR-JLL].
  outcomes:
    - lever: quality
      description: >
        Sovos reports an invoice rejection rate in live production in France, against its own estimate of the market
        rate. The release does not attribute the rate to AI diagnosis; it credits format validation, government
        connectivity and regulatory interpretation.
      figure: "1.6% vs about 20% (estimated market-wide)"
      measures: >
        invoice rejection rate "during live production" in France on the Sovos network, about three weeks after the
        1 Sep 2026 mandate; the market-wide figure is Sovos's own estimate and no denominator or source is given
      provenance: vendor-published
      source_ref: SOVOS-FRANCE-2026
  prerequisites:
    - "Clean customer, tax-registration and product master data, which the Vertex Exchange Europe recap says e-invoicing exposes very quickly [INNOVATETAX-VXE-2026]."
    - "Connectivity to the authority or approved platform so errors can be read and resubmitted [SOVOS-FRANCE-2026]."
  risks_and_guardrails:
    - "Sovos says every recommendation, approval and action is documented, and that AI-assisted workflows are designed with human oversight [SOVOS-SOVI-2026]."
    - "The roadmap is partly forward-looking; the release lists \"current and planned\" capabilities and says Sovos \"plans to extend\" guided, human-approved actions [SOVOS-SOVI-2026]."
  human_checkpoints:
    - "A user approves each proposed correction before it executes [SOVOS-SOVI-2026]."
  role_evolution: >
    The TEI recap quotes a panelist describing a shift "from us preparing returns to us answering notices on the
    data that's been shared" [TRINST-TEIAUDITOR-2026]. No source quantifies a change in headcount.
  evidence_grade: C
  sources:
    - { ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability", publisher: Sovos, type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: 2026-03-24, access: full, locator: "paragraph 'Current and planned Sovi AI capabilities include'" }
    - { ref: SOVOS-FRANCE-2026, title: "Three Weeks into France E-Invoicing Mandate: Sovos Hits Unparalleled Production Scale", publisher: Sovos, type: vendor, url: "https://sovos.com/press-releases/three-weeks-into-france-e-invoicing-mandate-sovos-hits-unparalleled-production-scale/", date: 2026-09-23, access: full, locator: "section 'Quality at Scale'" }
    - { ref: SOVOS-FLOWIE-2026, title: "Sovos Acquires Flowie, Launching the Industry's First Agentic Compliant Finance Orchestration Platform", publisher: Sovos, type: vendor, url: "https://sovos.com/press-releases/sovos-acquires-flowie-launching-the-industrys-first-agentic-compliant-finance-orchestration-platform/", date: 2026-10-01, access: full, locator: "paragraph naming Sovi Agent Studio" }
    - { ref: TR-WEBINAR-JLL, title: "Transforming indirect tax with AI (on-demand webinar with JLL)", publisher: Thomson Reuters, type: vendor, url: "https://europe.thomsonreuters.com/on-demand-webinars/transforming-indirect-tax-ai", date: 2026-10-17, access: full, locator: "webinar description (page undated, retrieved date used)" }
    - { ref: TRINST-TEIAUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: 2026-05-12, access: full, locator: "section 'End of the traditional model'" }
    - { ref: FONOA-REGMON-2026, title: "The Math No Longer Works for Indirect Tax Regulatory Change Monitoring", publisher: Fonoa, type: vendor, url: "https://www.fonoa.com/resources/blog/indirect-tax-regulatory-change-monitoring", date: 2026-09-16, access: full, locator: "section 'Why are indirect tax regulations increasing so quickly?'" }
    - { ref: INNOVATETAX-VXE-2026, title: "What we learned from Vertex Exchange Europe 2026", publisher: Innovate Tax, type: conference, url: "https://innovatetax.com/blog/what-we-learned-from-vertex-exchange-europe-2026/", date: 2026-05-06, access: full, locator: "section 'Master data came up a lot'" }
  last_reviewed: 2026-10-17
  notes: >
    The 1.6% figure measures network-wide rejections and is adjacent to, not a measure of, AI error diagnosis; if graded
    on it the entry would still be capped at B. Italy's fee of 70% of the disputed VAT is cited in the TEI recap as an
    example of penalty stakes; the recap does not link it to AI.

- id: tax-indirect-tax-05
  title: "Regulatory-change monitoring for VAT and e-invoicing with primary-source citations"
  archetype: tax
  module: indirect-tax
  function: risk-compliance-legal
  work_types: [research-synthesis]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >
    Fonoa argues manual monitoring no longer scales: more than 70 countries have changed e-invoicing rules since 2020,
    nexus, marketplace and digital-services rules keep shifting, teams are flat or shrinking, and a change often
    surfaces only at filing time [FONOA-REGMON-2026]. The same vendor warns that general AI tools can give a fluent,
    wrong answer about a proposed rule or one that was never passed [FONOA-PRIMARY-2026].
  solution: >
    Fonoa describes monitoring once, centrally, filtered to the jurisdictions and tax types that touch the business,
    with each alert carrying the primary source (gazette entry or directive), a confidence score and proposals labelled
    as proposals [FONOA-REGMON-2026] [FONOA-PRIMARY-2026]. Sovos describes "regulatory intelligence" with real-time
    assessment of how rule changes affect each customer's configuration, maintained by its regulatory specialists
    [SOVOS-SOVI-2026]. A Florida sales tax attorney's account is the counter-case: a general AI draft contained about
    five serious errors [FLSALESTAX-AI-2026].
  outcomes:
    - lever: risk
      description: "none published"
      figure: "n/a"
      measures: "no figure published; Fonoa and Sovos give no detection rate, false-alert rate or time-to-alert"
      provenance: vendor-published
      source_ref: FONOA-REGMON-2026
  prerequisites:
    - "A profile of jurisdictions, tax types and business activities so alerts can be filtered [FONOA-REGMON-2026]."
    - "Source feeds from legislative gazettes and authority sites; the Florida attorney notes that many government sites are not accessible to AI engines [FLSALESTAX-AI-2026]."
  risks_and_guardrails:
    - "A summary is a reading of the law and cannot be cited in an audit with confidence; attach and keep the primary source [FONOA-PRIMARY-2026]."
    - "General-purpose models have knowledge cutoffs; the Florida attorney gives the Oct 2025 repeal of Florida's commercial lease sales tax as an example an older model would miss [FLSALESTAX-AI-2026]."
    - "Avalara's single test found a general chatbot gave a Bellevue, WA combined rate of 10.3% when the October 2025 rate was 10.2%, because it confused the enactment and effective dates [AVALARA-LLMTEST-2025]."
  human_checkpoints:
    - "A person decides whether a change applies to the business; Fonoa says applying a summarised change may need a human's deterministic application [FONOA-STACK-2025]."
  role_evolution: >
    Fonoa says coverage should stop being a function of headcount [FONOA-REGMON-2026]. The Vertex Exchange Europe
    recap says tax staff will need to understand how rules are configured, explained, audited and defended
    [INNOVATETAX-VXE-2026].
  evidence_grade: C
  sources:
    - { ref: FONOA-REGMON-2026, title: "The Math No Longer Works for Indirect Tax Regulatory Change Monitoring", publisher: Fonoa, type: vendor, url: "https://www.fonoa.com/resources/blog/indirect-tax-regulatory-change-monitoring", date: 2026-09-16, access: full, locator: "sections 'Why are indirect tax regulations increasing so quickly?' and 'How leading tax teams monitor regulatory change differently'" }
    - { ref: FONOA-PRIMARY-2026, title: "Why Primary Source Citation Matters for Tax Audit Defense", publisher: Fonoa, type: vendor, url: "https://www.fonoa.com/resources/blog/primary-source-tax-law-citation-audit", date: 2026-09-21, access: full, locator: "sections 'Why general AI can't be trusted for tax research' and 'Start with the primary source'" }
    - { ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability", publisher: Sovos, type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: 2026-03-24, access: full, locator: "bullet 'Regulatory Intelligence'" }
    - { ref: FLSALESTAX-AI-2026, title: "Can I Trust AI for Florida Sales Tax Advice?", publisher: floridasalestax.com (James H. Sutton Jr., CPA, Esq.), type: firm, url: "https://www.floridasalestax.com/florida-tax-law-blog/2026/june/can-i-trust-ai-for-florida-sales-tax-advice-/", date: 2026-06-06, access: full, locator: "introduction; section 1 'Knowledge cutoffs make AI advice stale by design'" }
    - { ref: AVALARA-LLMTEST-2025, title: "Why AI not backed by tax expertise can get sales tax rates wrong", publisher: Avalara, type: vendor, url: "https://www.avalara.com/blog/en/north-america/2025/11/ai-tax-expertise-accurate-sales-tax-rates.html", date: 2025-11-20, access: full, locator: "section 'Why the LLM AI chatbot got the tax rate wrong'" }
    - { ref: FONOA-STACK-2025, title: "Where AI Belongs in Your Tax Stack (And Where It Doesn't)", publisher: Fonoa, type: vendor, url: "https://www.fonoa.com/resources/blog/where-ai-belongs-in-your-tax-stack", date: 2025-11-04, access: full, locator: "section 'The middle ground: layer AI assistance with deterministic final checks'" }
    - { ref: INNOVATETAX-VXE-2026, title: "What we learned from Vertex Exchange Europe 2026", publisher: Innovate Tax, type: conference, url: "https://innovatetax.com/blog/what-we-learned-from-vertex-exchange-europe-2026/", date: 2026-05-06, access: full, locator: "section 'AI is becoming a default expectation'" }
  last_reviewed: 2026-10-17
  notes: >
    The Florida lease-tax repeal claim and the "about five serious errors" account are one attorney's statements
    in a firm blog that also markets the firm's services. The Avalara test is a vendor's single example (n=1).

- id: tax-indirect-tax-06
  title: "Full-population invoice review, anomaly detection and VAT recovery checks"
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >
    Manual review samples a small share of transactions. Fonoa's illustration compares a reviewer who is 97% accurate
    on the 10% of transactions reviewed with a system that is 93% accurate across all transactions; the figures are
    hypothetical and not measured [FONOA-ACCURACY-2025]. Under e-invoicing and digital reporting, discrepancies between
    reported transaction data and VAT return data become more visible to authorities [FONOA-ERRORRATE-2025].
  solution: >
    Practitioners describe AI that extracts, validates and categorises invoice information, reconciles VAT postings
    across jurisdictions, identifies unusual transactions, predicts audit risk and improves VAT recovery accuracy
    [BTAX-VAT2026]. A UK adviser, Saffery, held a webinar on AI support for invoice reviews, anomaly detection and
    data analysis, plus real-time controls and continuous assurance [SAFFERY-VAT-2026]. Fonoa recommends AI for
    anomaly detection across very large invoice populations, with deterministic checks or human judgment for final
    decisions [FONOA-STACK-2025].
  outcomes:
    - lever: risk
      description: "none published"
      figure: "n/a"
      measures: "no measured outcome found; the 97% / 93% / 10% coverage comparison is a hypothetical in the source"
      provenance: vendor-published
      source_ref: FONOA-ACCURACY-2025
  prerequisites:
    - "Structured invoice and ledger data across entities; the Bloomberg Tax author says automation and data quality will be \"the new currencies\" [BTAX-VAT2026]."
    - "Confidence thresholds that route uncertain items to people [FONOA-ACCURACY-2025]."
  risks_and_guardrails:
    - "False positives and false negatives; Fonoa says thresholds and filters are needed to avoid alert fatigue [FONOA-ERRORRATE-2025]."
    - "Where a missed flag could mean a major fine, Fonoa says to keep deterministic logic as the backbone [FONOA-STACK-2025]."
  human_checkpoints:
    - "Flagged items are verified by a tax manager against known rules before an audit [FONOA-STACK-2025]."
  role_evolution: >
    The Bloomberg Tax author says businesses will move from manual tasks to tech-driven VAT management supported by
    predictive analytics [BTAX-VAT2026]. No source quantifies the effect on roles.
  evidence_grade: C
  sources:
    - { ref: BTAX-VAT2026, title: "Digital Mandates and AI Reshape VAT Compliance Landscape in 2026", publisher: Bloomberg Tax (author Eugen Trombitas, indirect tax consultant), type: press, url: "https://news.bloombergtax.com/tax-insights-and-commentary/digital-mandates-and-ai-reshape-vat-compliance-landscape-in-2026", date: 2026-01-06, access: full, locator: "sections 'Growing AI Role' and 'E-Invoicing, Real-Time Reporting'" }
    - { ref: SAFFERY-VAT-2026, title: "Transforming VAT (webinar)", publisher: Saffery, type: firm, url: "https://www.saffery.com/insights/videos-webinars/transforming-vat/", date: 2026-09-08, access: full, locator: "webinar topic list" }
    - { ref: FONOA-ACCURACY-2025, title: "AI Won't Make Your Tax Determinations Perfect (And That's Fine)", publisher: Fonoa, type: vendor, url: "https://www.fonoa.com/resources/blog/ai-tax-determination-accuracy", date: 2025-10-29, access: full, locator: "sections 'Breadth of analysis can compensate for margin of error' and 'Confidence thresholds'" }
    - { ref: FONOA-ERRORRATE-2025, title: "Your 'Accurate' Tax Process Probably Has a 20% Error Rate", publisher: Fonoa, type: vendor, url: "https://www.fonoa.com/resources/blog/accurate-tax-process-error-rate", date: 2025-11-11, access: full, locator: "sections 'Human tax processes fail more often' and 'AI catches different errors but introduces its own'" }
    - { ref: FONOA-STACK-2025, title: "Where AI Belongs in Your Tax Stack (And Where It Doesn't)", publisher: Fonoa, type: vendor, url: "https://www.fonoa.com/resources/blog/where-ai-belongs-in-your-tax-stack", date: 2025-11-04, access: full, locator: "sections on determinism-critical use cases and 'layered AI'" }
  last_reviewed: 2026-10-17
  notes: >
    No named in-house deployment and no measured result were found, so this is graded C on practitioner and vendor
    description. Fonoa's "20% error rate" headline is rhetorical; the source cites spreadsheet-error studies (24% to
    90% of complex spreadsheets with material errors) that were not opened.

- id: tax-indirect-tax-07
  title: "Reconciling calculated, invoiced and reported tax across determination, e-invoice and return data"
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [data-reporting, review-assurance]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >
    Vertex Exchange Europe panellists said tax teams need to show that what was calculated is what was invoiced, and
    that what was invoiced is what was reported to the authorities [INNOVATETAX-VXE-2026]. Fonoa notes large teams
    question the quality of reconciling transaction data to periodic VAT return data [FONOA-ERRORRATE-2025]. Thomson
    Reuters describes manual reconciliation between source systems, tax engines, reporting tools and Excel as where
    hours disappear and errors accumulate [TR-AGENTICIT-2026].
  solution: >
    An idea discussed by practitioners and vendors: agents move between ERP, tax engine and e-invoicing records,
    validate results and flag reconciliation exceptions in real time [TR-AGENTICIT-2026]. The Vertex recap links the
    shift to "continuous audit controls", with scrutiny beyond the invoice document [INNOVATETAX-VXE-2026]. Labelled
    as an idea: no source reports a deployment of this specific reconciliation.
  outcomes:
    - lever: quality
      description: "none published"
      figure: "n/a"
      measures: "no figure published"
      provenance: vendor-published
      source_ref: TR-AGENTICIT-2026
  prerequisites:
    - "Shared master data and identifiers across tax, finance, IT, AP and sales [INNOVATETAX-VXE-2026]."
    - "Access to e-invoicing and authority-response records [TR-AGENTICIT-2026]."
  risks_and_guardrails:
    - "Agents that reconcile across systems carry the same audit-trail needs as other agents: who reviewed what, when and with what rationale [TR-AGENTICIT-2026]."
  human_checkpoints:
    - "Exceptions are reviewed and resolved by a person [TR-AGENTICIT-2026]."
  role_evolution: >
    Thomson Reuters says capacity consumed by data processing could move to policy optimisation, monitoring and advisory
    work [TR-AGENTICIT-2026]; this is a vendor projection.
  evidence_grade: D
  sources:
    - { ref: INNOVATETAX-VXE-2026, title: "What we learned from Vertex Exchange Europe 2026", publisher: Innovate Tax, type: conference, url: "https://innovatetax.com/blog/what-we-learned-from-vertex-exchange-europe-2026/", date: 2026-05-06, access: full, locator: "sections 'VAT risk now surfaces at the invoice itself' and 'From CTC to Continuous Audit Controls'" }
    - { ref: TR-AGENTICIT-2026, title: "Is your tax department ready for the agentic AI explosion?", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/is-your-tax-department-ready-for-the-agentic-ai-explosion/", date: 2026-06-08, access: full, locator: "section 'A new kind of tool: One that uses other tools'; final section" }
    - { ref: FONOA-ERRORRATE-2025, title: "Your 'Accurate' Tax Process Probably Has a 20% Error Rate", publisher: Fonoa, type: vendor, url: "https://www.fonoa.com/resources/blog/accurate-tax-process-error-rate", date: 2025-11-11, access: full, locator: "section 'Human tax processes fail more often than anyone wants to admit'" }
  last_reviewed: 2026-10-17
  notes: >
    Idea (grade D). The reconciliation need is documented; the AI approach is described by Thomson Reuters in
    general terms, not as a shipped feature for this task.

- id: tax-indirect-tax-08
  title: "Decision log and audit-defence file for AI-assisted indirect-tax determinations"
  archetype: tax
  module: indirect-tax
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: announced
  problem: >
    In Fonoa's survey of 176 indirect tax leaders, 57.4% would not be confident defending AI-assisted decisions to a
    tax authority, and only a third run formal human-in-the-loop review; the rest rely on informal checks, no defined
    process, or keep AI out of decisions [FONOA-2026-SURVEY]. In Fonoa's framing the test is whether a defined process
    sits behind the output (an indirect tax partner at BDO: "You're demonstrating a process") [FONOA-2026-SURVEY].
  solution: >
    Capture, for each AI-assisted determination, override and approval, a trail that can be produced on demand.
    Fonoa markets "Fonoa Audit" for this [FONOA-2026-SURVEY]. Thomson Reuters says it documents each agent decision
    with rationale, timestamps and reviewer sign-offs [TR-AGENTICIT-2026]. Sovos lists "full audit transparency" for
    each recommendation, approval and action [SOVOS-SOVI-2026]. Avalara says Aviator keeps an "audit-defensible
    record for every action" [AVALARA-CRUSHEU-2026].
  outcomes:
    - lever: capacity
      description: >
        Fonoa says a small cohort with accountability structures reports compliance workload falling faster than the
        rest. The landing page gives no sample size or definition of workload.
      figure: "8x the rate of everyone else"
      measures: >
        rate of decrease in "compliance workload" for the cohort with accountability structures versus other
        respondents, among 176 surveyed indirect tax leaders; cohort size and workload definition not published on the
        landing page
      provenance: vendor-published
      source_ref: FONOA-2026-SURVEY
  prerequisites:
    - "Leadership-set AI targets or KPIs; only 12.5% of respondents have them [FONOA-2026-SURVEY]."
    - "An AI use log or inventory of AI-assisted decisions affecting filings, determinations or authority responses over 12 months, as Fonoa's self-assessment asks [FONOA-2026-SURVEY]."
  risks_and_guardrails:
    - "At the TEI seminar only two hands in a room of more than 50 said the tax function owns AI implementation at their company [TEI-TAXTECH-2026]."
    - "An analyst's team can deploy a quickly built AI pipeline that nobody else has reviewed or documented [TRINST-TEIAUDITOR-2026]."
  human_checkpoints:
    - "Reviewer sign-off at each decision point in the vendor workflows described [TR-AGENTICIT-2026] [SOVOS-SOVI-2026]."
  role_evolution: >
    Fonoa's survey frames the leader's job as owning accountability structures, KPIs and audit trails around AI
    [FONOA-2026-SURVEY]. A TEI senior director said, "You will not survive in this field if you don't have a change
    mindset" [TEI-TAXTECH-2026].
  evidence_grade: C
  sources:
    - { ref: FONOA-2026-SURVEY, title: "State of Indirect Tax in the AI Era 2026", publisher: Fonoa, type: survey, url: "https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026", date: 2026-06-17, access: full, locator: "landing page sections on audit confidence, human-in-the-loop review and 'How to identify your AI accountability gap' (full report is gated and was not read)" }
    - { ref: TR-AGENTICIT-2026, title: "Is your tax department ready for the agentic AI explosion?", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/is-your-tax-department-ready-for-the-agentic-ai-explosion/", date: 2026-06-08, access: full, locator: "section 'Auditability by design'" }
    - { ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability", publisher: Sovos, type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: 2026-03-24, access: full, locator: "bullet 'Full Audit Transparency'" }
    - { ref: AVALARA-CRUSHEU-2026, title: "Avalara Helps Global Businesses Move Faster as Tax and Compliance Complexity Accelerates", publisher: Avalara (PR Newswire), type: conference, url: "https://www.webdisclosure.com/press-release/avalara-helps-global-businesses-move-faster-as-tax-and-compliance-complexity-accelerates-WEpMYuY5kxr", date: 2026-10-08, access: full, locator: "paragraph on Avalara Aviator" }
    - { ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: 2026-05-04, access: full, locator: "section 'A very bad wizard'" }
    - { ref: TRINST-TEIAUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: 2026-05-12, access: full, locator: "section 'Two ways to lose'" }
  last_reviewed: 2026-10-17
  notes: >
    The survey is sponsored by a vendor that sells an audit-trail product, and only the landing page was read. The
    poll at TEI covered corporate tax functions in general, not only indirect tax.

- id: tax-indirect-tax-09
  title: "Grounded question-and-answer assistants inside tax compliance platforms"
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [research-synthesis, client-interaction]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: >
    Tax and regulatory questions across many jurisdictions are slow to answer, and a general chatbot can be
    confidently wrong. Avalara's example is a chatbot giving 10.3% for Bellevue, WA in Oct 2025 when the rate was
    10.2% because the ordinance was enacted in July 2025 but took effect on 1 Jan 2026 [AVALARA-LLMTEST-2025]. A
    Florida sales tax attorney said a Claude-generated first draft on Florida sales tax had about five serious errors
    [FLSALESTAX-AI-2026].
  solution: >
    Sovos' Ask Sovi answers regulatory questions inside the compliance platform, drawing on a knowledge base
    maintained by more than 100 regulatory specialists, covering 150+ countries and several languages [SOVOS-SOVI-2026].
    Avalara says its agents let customers ask for tax calculations and certificate validations instead of navigating
    screens, with escalation to a person for novel cases [AVALARA-AGENTIC-2025]. Avalara also offers Tax Research backed
    by tax experts [AVALARA-LLMTEST-2025].
  outcomes:
    - lever: quality
      description: >
        Avalara's own test: one tax-rate lookup in which a general chatbot was wrong and Avalara's engine was right.
      figure: "10.3% (chatbot) vs 10.2% (Avalara) for Bellevue, WA, Oct 2025"
      measures: >
        a single combined sales tax rate lookup (n=1) for Bellevue, Washington in October 2025, run by the vendor that
        sells the compared product
      provenance: vendor-published
      source_ref: AVALARA-LLMTEST-2025
  prerequisites:
    - "A curated, current tax content base; Sovos cites 40+ years of expertise and 100+ specialists [SOVOS-SOVI-2026]."
    - "Primary-source citation so users can verify and keep evidence for audit [FONOA-PRIMARY-2026]."
  risks_and_guardrails:
    - "Knowledge cutoffs, hallucination and treating all sources as equally authoritative are named failure modes of general models [FLSALESTAX-AI-2026]."
    - "Customer data stays inside the vendor's security perimeter and is not used to train external models, per Sovos [SOVOS-SOVI-2026]."
  human_checkpoints:
    - "The user decides what to do with an answer; Sovos says it plans to extend to guided, human-approved actions [SOVOS-SOVI-2026]."
  role_evolution: >
    The Florida attorney says a growing number of business owners, and some tax professionals, use general AI tools
    for sales tax answers, some as a starting point and some as a substitute for professional advice [FLSALESTAX-AI-2026].
  evidence_grade: C
  sources:
    - { ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability", publisher: Sovos, type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: 2026-03-24, access: full, locator: "paragraph on Ask Sovi" }
    - { ref: AVALARA-LLMTEST-2025, title: "Why AI not backed by tax expertise can get sales tax rates wrong", publisher: Avalara, type: vendor, url: "https://www.avalara.com/blog/en/north-america/2025/11/ai-tax-expertise-accurate-sales-tax-rates.html", date: 2025-11-20, access: full, locator: "sections 'Testing Avalara vs. Google AI' and 'Why the LLM AI chatbot got the tax rate wrong'" }
    - { ref: AVALARA-AGENTIC-2025, title: "Avalara launches 'always on, always ready' AI agents", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/avalara-launches-always-on-always-ready-ai-agents", date: 2025-09-30, access: full, locator: "paragraphs on interface and human review" }
    - { ref: FLSALESTAX-AI-2026, title: "Can I Trust AI for Florida Sales Tax Advice?", publisher: floridasalestax.com (James H. Sutton Jr., CPA, Esq.), type: firm, url: "https://www.floridasalestax.com/florida-tax-law-blog/2026/june/can-i-trust-ai-for-florida-sales-tax-advice-/", date: 2026-06-06, access: full, locator: "introduction and section 'Why AI and Florida sales tax are a dangerous combination'" }
    - { ref: FONOA-PRIMARY-2026, title: "Why Primary Source Citation Matters for Tax Audit Defense", publisher: Fonoa, type: vendor, url: "https://www.fonoa.com/resources/blog/primary-source-tax-law-citation-audit", date: 2026-09-21, access: full, locator: "section 'Start with the primary source, then add the interpretation'" }
  last_reviewed: 2026-10-17
  notes: >
    Both quality examples come from parties that sell or advise on sales tax and are not independent. The Florida blog
    says the lease-tax repeal took effect 1 Oct 2025 (House Bill 7031); that statement was not verified against the statute.

- id: tax-indirect-tax-10
  title: "Tax engines exposed to customers' own AI agents through MCP and agent-to-agent protocols"
  archetype: tax
  module: indirect-tax
  function: technology-it
  work_types: [software-systems]
  pattern: other
  ladder: automate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >
    Compliance work "won't always begin inside compliance software"; it may start in an ERP, an e-commerce platform, a
    finance system or an AI agent; Avalara contrasts its approach with traditional integration tools that take
    months [AVALARA-CRUSHEU-2026].
  solution: >
    Avalara's CRUSH Europe release says its Versori unit uses AI agents to build and deploy connectors in days rather
    than months [AVALARA-CRUSHEU-2026]; its 2025 launch described a "Have your agent call our agent" model with agents
    accessing MCP servers [AVALARA-AGENTIC-2025]; its NEXT 2026 developer event focused on APIs and agent-based
    architectures [AVALARA-NEXT-2026]. Sovos said it is developing an MCP Gateway for standardised, governed agent
    access and that A2A orchestration is "expected" over time [SOVOS-SOVI-2026]. Pattern: other (a vendor exposes
    capabilities for another party's agents to call).
  outcomes:
    - lever: speed
      description: >
        Avalara says Versori builds connectors "in days rather than months". No sample or customer is named.
      figure: "days instead of months"
      measures: "time to build production-grade connectors, per the vendor release; no baseline or sample"
      provenance: vendor-published
      source_ref: AVALARA-CRUSHEU-2026
  prerequisites:
    - "Authenticated, governed access to the tax engine for external agents [SOVOS-SOVI-2026]."
    - "Customer-side agent environments that can call it [SOVOS-SOVI-2026]."
  risks_and_guardrails:
    - "Sovos describes the MCP gateway as designed for \"standardized, governed access\"; governance detail is not published [SOVOS-SOVI-2026]."
    - "Whether the calling agent is trusted and which party is liable for a wrong result is not addressed in the sources read."
  human_checkpoints:
    - "Not specified in the sources."
  role_evolution: >
    Compliance capabilities may be consumed "through trusted, interoperable agents" as well as applications
    [SOVOS-SOVI-2026]; no source discusses effects on tax or IT roles.
  evidence_grade: C
  sources:
    - { ref: AVALARA-CRUSHEU-2026, title: "Avalara Helps Global Businesses Move Faster as Tax and Compliance Complexity Accelerates", publisher: Avalara (PR Newswire), type: conference, url: "https://www.webdisclosure.com/press-release/avalara-helps-global-businesses-move-faster-as-tax-and-compliance-complexity-accelerates-WEpMYuY5kxr", date: 2026-10-08, access: full, locator: "paragraph on Versori by Avalara" }
    - { ref: AVALARA-AGENTIC-2025, title: "Avalara launches 'always on, always ready' AI agents", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/avalara-launches-always-on-always-ready-ai-agents", date: 2025-09-30, access: full, locator: "paragraphs on 'Have your agent call our agent' and MCP" }
    - { ref: AVALARA-NEXT-2026, title: "Avalara NEXT: The future of agentic tax and compliance", publisher: Avalara, type: conference, url: "https://www.avalara.com/us/en/blog/avalara-next-2026-building-the-future-of-agentic-tax-and-compliance.html", date: 2026-03-04, access: full, locator: "section 'What the event will cover' (event held 26 Mar 2026 per the page)" }
    - { ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability", publisher: Sovos, type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: 2026-03-24, access: full, locator: "paragraph on Sovos MCP Gateway" }
  last_reviewed: 2026-10-17
  notes: >
    Vendor announcements and event descriptions only; no customer use of MCP/A2A access was found. Avalara's 9 Apr 2026
    MCP release was not reachable.

- id: tax-indirect-tax-11
  title: "Tax determination inside agent-initiated checkout, including sales tax holiday rules"
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [transaction-processing]
  pattern: other
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: >
    When an AI agent completes a purchase, practitioners ask who must collect tax [BTAX-AGENTIC-2026]. The Sales
    Tax Institute adds that sales tax holidays need correct timing (the holiday state's time zone), product category,
    price cap and destination sourcing, and that autonomous agents can remove the human checkpoint while multiplying
    simultaneous transactions [STI-AGENTIC-2026].
  solution: >
    Keep tax calculation in the merchant's existing tax determination system and call it from the agent's checkout
    flow. The Sales Tax Institute says most agentic commerce models rely on merchants' tax systems and that Shopify
    structured its agentic commerce experience so tax calculation stays in the transaction flow [STI-AGENTIC-2026].
    Its advice: make holiday rules in the tax engine current and machine-readable, give agents correct catalogue
    metadata, and ask the platform provider how tax is handled in agent-initiated checkout [STI-AGENTIC-2026]. The
    Stripe author argues an app that authorises payment or transmits orders is likely to meet marketplace facilitator
    or EU deemed-supplier tests, so the operator may have to collect tax [BTAX-AGENTIC-2026].
  outcomes:
    - lever: risk
      description: "none published"
      figure: "n/a"
      measures: "no tax-compliance outcome published for agent-initiated checkout"
      provenance: independent
      source_ref: STI-AGENTIC-2026
  prerequisites:
    - "Machine-readable, current rules in the tax engine, not only point-of-sale configuration [STI-AGENTIC-2026]."
    - "Catalogue metadata that identifies exempt or holiday-eligible items and price thresholds [STI-AGENTIC-2026]."
  risks_and_guardrails:
    - "Responsibility is unsettled between retailer, agent platform and protocol layer; in practice calculation generally stays with the retailer or marketplace [STI-AGENTIC-2026]."
    - "Liability must attach to a legal entity because AI systems have no legal personality [BTAX-AGENTIC-2026]."
    - "Small differences in checkout flow or payment authorisation can change the analysis [BTAX-AGENTIC-2026]."
  human_checkpoints:
    - "Agent-initiated checkout removes the human checkpoint at purchase; the Sales Tax Institute says controls must move to the tax engine and data [STI-AGENTIC-2026]."
  role_evolution: >
    Not described beyond a call for tax teams and e-commerce leaders to assess whether holiday processes suit
    machine-driven purchasing [STI-AGENTIC-2026].
  evidence_grade: C
  sources:
    - { ref: STI-AGENTIC-2026, title: "Can AI Shopping Agents Apply Sales Tax Holidays?", publisher: Sales Tax Institute, type: press, url: "https://www.salestaxinstitute.com/resources/ai-shopping-agents-sales-tax-holidays", date: 2026-07-29, access: full, locator: "sections 'What Makes Sales Tax Holidays Uniquely Hard for a Machine' and 'Where the Responsibility Actually Lands'" }
    - { ref: BTAX-AGENTIC-2026, title: "Artificial Intelligence Goes Shopping, Creates Tax Challenges", publisher: Bloomberg Tax (author Aleksandra Bal, Stripe), type: press, url: "https://news.bloombergtax.com/tax-insights-and-commentary/artificial-intelligence-goes-shopping-creates-tax-challenges", date: 2026-02-24, access: full, locator: "sections 'EU Value-Added Tax', 'US Sales Tax' and 'Practical Takeaway'" }
  last_reviewed: 2026-10-17
  notes: >
    Both sources are practitioner commentary; the Bloomberg piece is an opinion column by a Stripe tax technology lead
    and the Sales Tax Institute is a training provider. The Shopify statement is the Institute's description, not
    verified with Shopify. Context figures from the Institute (Shopify reported 7x AI-generated traffic and 11x purchases
    from AI search; Visa, Mastercard and American Express announced agentic commerce initiatives by Apr 2026) were not
    verified at source. The McKinsey $3-5 trillion estimate by 2030 is quoted in the Bloomberg piece and not verified.

- id: tax-indirect-tax-12
  title: "AI agents answering nexus, registration and filing-threshold questions across a client portfolio"
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [research-synthesis, client-interaction]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >
    Sales tax nexus, rates and filing thresholds shift quickly, and advisory firms need more than a list of updates to
    apply them to individual client situations [TRUSS-KINTSUGI-2026].
  solution: >
    A Truss and Kintsugi webinar (listed for 17 Sep 2026, ET) promised live examples of AI agents answering
    practitioner questions, from nexus exposure across a client portfolio to state-specific filing thresholds
    [TRUSS-KINTSUGI-2026]. Avalara's 2025 launch also described agents that initiate registrations and advise on
    compliance obligations [AVALARA-AGENTIC-2025].
  outcomes:
    - lever: speed
      description: "none published"
      figure: "n/a"
      measures: "no figure published; the listing describes a demonstration"
      provenance: vendor-published
      source_ref: TRUSS-KINTSUGI-2026
  prerequisites:
    - "Client transaction and sales-by-state data in a system the agent can read [TRUSS-KINTSUGI-2026]."
  risks_and_guardrails:
    - "Answers on nexus carry registration and liability consequences; the source does not describe review controls beyond a tax professional reading the output."
  human_checkpoints:
    - "Not specified beyond the practitioner asking and reviewing [TRUSS-KINTSUGI-2026]."
  role_evolution: >
    Not described; the webinar is aimed at firms keeping up with changes and applying them to clients [TRUSS-KINTSUGI-2026].
  evidence_grade: C
  sources:
    - { ref: TRUSS-KINTSUGI-2026, title: "What's Changing in Sales and Business Tax - And How AI Can Help (webinar)", publisher: Truss with Kintsugi, type: vendor, url: "https://gettruss.io/events/sales-business-tax-ai", date: 2026-09-17, access: full, locator: "About Event and Learning Objectives" }
    - { ref: AVALARA-AGENTIC-2025, title: "Avalara launches 'always on, always ready' AI agents", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/avalara-launches-always-on-always-ready-ai-agents", date: 2025-09-30, access: full, locator: "paragraph on agents advising, initiating registrations and filing" }
  last_reviewed: 2026-10-17
  notes: >
    The webinar year (2026) is inferred from the page text ("shifting fast in 2026") and the Thursday weekday match for
    17 Sep 2026. No recording or results were found.

- id: tax-indirect-tax-13
  title: "Compliance-by-design finance orchestration that embeds tax rules in AP, procure-to-pay and invoicing agents"
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [transaction-processing]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >
    Sovos says companies that bolt separate finance and tax applications onto ERPs face heavier integration and
    governance burdens, while tax authorities require real-time clearance against jurisdiction-specific rules
    [SOVOS-FLOWIE-2026].
  solution: >
    Sovos announced on 1 Oct 2026 that it acquired Flowie, whose agents run accounts payable, procure-to-pay,
    contracts, invoicing, collections and onboarding, and said Flowie's agents will draw on Sovos' tax compliance and
    regulatory data so each transaction is grounded in the rules of the jurisdiction it touches [SOVOS-FLOWIE-2026].
    A planned "Sovos Graph" is described as an entity network, transaction intelligence and regulatory-knowledge layer
    [SOVOS-FLOWIE-2026].
  outcomes:
    - lever: cost
      description: >
        Sovos cites an EY figure for end-to-end agentic finance implementations; the EY source was not opened.
      figure: "up to 40%"
      measures: >
        "cost savings" from "end-to-end agentic AI implementation", as quoted by Sovos and attributed to EY; sample and
        method unknown
      provenance: vendor-published
      source_ref: SOVOS-FLOWIE-2026
  prerequisites:
    - "Replacing or sitting on top of existing ERP landscapes [SOVOS-FLOWIE-2026]."
    - "Integration of Sovos' regulatory data with the agents; the release uses forward-looking wording (\"will\", \"will launch\") [SOVOS-FLOWIE-2026]."
  risks_and_guardrails:
    - "Announced two weeks before this review; no deployment evidence. Control design for autonomous AP and invoicing agents is not described."
  human_checkpoints:
    - "Not specified in the release."
  role_evolution: >
    Sovos says CFOs and CIOs could retire dozens of surrounding applications [SOVOS-FLOWIE-2026]; no source describes
    effects on tax or finance staff.
  evidence_grade: C
  sources:
    - { ref: SOVOS-FLOWIE-2026, title: "Sovos Acquires Flowie, Launching the Industry's First Agentic Compliant Finance Orchestration Platform", publisher: Sovos, type: vendor, url: "https://sovos.com/press-releases/sovos-acquires-flowie-launching-the-industrys-first-agentic-compliant-finance-orchestration-platform/", date: 2026-10-01, access: full, locator: "sections 'The Inevitable Collision' and 'The Sovos and Flowie Difference'" }
  last_reviewed: 2026-10-17
  notes: >
    Single announcement. It is included because it shows where a major indirect-tax vendor says the market is heading.
    Whether this belongs in indirect-tax or in tax-data-technology is a synthesis call.

- id: tax-indirect-tax-14
  title: "Tax-team-built AI data pipelines for reconciliations and notice data extraction"
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [data-reporting, software-systems]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: >
    Data integration pipelines used to wait in an IT queue, and state tax notices arrive in different formats every
    time [TRINST-TEIAUDITOR-2026].
  solution: >
    TEI attendees described using data platforms (Alteryx, Power Platform, Snowflake, Databricks, Microsoft Fabric,
    Palantir Foundry) to run agentic AI against historical filings, to deploy validation agents that critique their own
    outputs, and to use image-to-text AI to pull structured data out of state tax notices; the recap also says analysts
    "vibe-code" integration pipelines [TRINST-TEIAUDITOR-2026]. OpenAI's tax department showed live automation
    pipelines at the same seminar [TEI-TAXTECH-2026].
  outcomes:
    - lever: speed
      description: >
        The recap says pipelines can be vibe-coded in 15 minutes that would have waited two months in an IT queue.
      figure: "15 minutes vs two months"
      measures: >
        time to build a data integration pipeline versus time waiting in an IT queue, as an anecdote in the recap; no
        organisation, sample or measurement named
      provenance: vendor-published
      source_ref: TRINST-TEIAUDITOR-2026
  prerequisites:
    - "Data platform access and a tool-approval path; TEI attendees' polls listed the platforms in use [TRINST-TEIAUDITOR-2026]."
  risks_and_guardrails:
    - "A pipeline built in minutes may be deployed without review, documentation or anyone who can maintain it; an OpenAI panelist conceded the security point when asked about vibe coding [TRINST-TEIAUDITOR-2026]."
    - "Attendees described Alteryx workflows nobody could explain after the builder left [TEI-TAXTECH-2026]."
    - "Silent failures: an AI agent told a user it had not been able to open the uploaded file and had been \"telling you what you wanted to hear\" [TEI-TAXTECH-2026]."
  human_checkpoints:
    - "Human-in-the-loop was \"a constant refrain\" at the seminar, with concern about reviewing rising volumes of quiet, technical errors [TEI-TAXTECH-2026]."
  role_evolution: >
    The recap says the job has become as much a data-science problem as an accounting one [TRINST-TEIAUDITOR-2026]. At
    the TEI seminar two hands of more than 50 said the tax function owns AI implementation [TEI-TAXTECH-2026].
  evidence_grade: C
  sources:
    - { ref: TRINST-TEIAUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: 2026-05-12, access: full, locator: "sections 'End of the traditional model' and 'Two ways to lose'" }
    - { ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: 2026-05-04, access: full, locator: "sections 'A very good man' and 'A very bad wizard'" }
  last_reviewed: 2026-10-17
  notes: >
    Corporate-tax-wide recap by a vendor-owned publication; the seminar covered tax technology broadly and these
    pipelines are not all indirect-tax specific. The "notices" example refers to state tax notices without saying the tax
    type. No named company reported an outcome. Maturity is set to piloting because the recap describes live
    demonstrations and attendee practice without naming a deploying indirect-tax team.

- id: tax-indirect-tax-15
  title: "Plain-language configuration of tax rules, matrices and engine logic"
  archetype: tax
  module: indirect-tax
  function: technology-it
  work_types: [software-systems]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >
    Indirect tax implementations are described as largely partner-led, with timelines under pressure as mandates grow
    more complex, and success depends on data quality and alignment between tax, finance and IT [INNOVATETAX-VXE-2026].
  solution: >
    Vertex showed AI that can update tax rules and support configuration logic in plain language [INNOVATETAX-VXE-2026].
    Avalara says Aviator can auto-generate tax matrices and configure custom rules [AVALARA-CRUSHEU-2026]. The Vertex
    recap says explainability, reversibility, auditability and human oversight are the stated guardrails
    [INNOVATETAX-VXE-2026].
  outcomes:
    - lever: speed
      description: "none published"
      figure: "n/a"
      measures: "no figure published"
      provenance: vendor-published
      source_ref: INNOVATETAX-VXE-2026
  prerequisites:
    - "A tax engine with an auditable configuration layer and the ability to reverse changes [INNOVATETAX-VXE-2026]."
  risks_and_guardrails:
    - "Misconfiguration changes tax outcomes for many transactions at once; Vertex's stated mitigation is explainability, reversibility, auditability and human oversight [INNOVATETAX-VXE-2026]."
  human_checkpoints:
    - "A person approves configuration changes; the source says human oversight sits within the guardrails [INNOVATETAX-VXE-2026]."
  role_evolution: >
    The recap says partners are investing in enablement, certification and AI-powered knowledge tools, and that the
    future tax team is hybrid across legislation, systems, process design and data flows [INNOVATETAX-VXE-2026].
  evidence_grade: C
  sources:
    - { ref: INNOVATETAX-VXE-2026, title: "What we learned from Vertex Exchange Europe 2026", publisher: Innovate Tax, type: conference, url: "https://innovatetax.com/blog/what-we-learned-from-vertex-exchange-europe-2026/", date: 2026-05-06, access: full, locator: "sections 'AI is becoming a default expectation' and 'Partners and skills are now central to success'" }
    - { ref: AVALARA-CRUSHEU-2026, title: "Avalara Helps Global Businesses Move Faster as Tax and Compliance Complexity Accelerates", publisher: Avalara (PR Newswire), type: conference, url: "https://www.webdisclosure.com/press-release/avalara-helps-global-businesses-move-faster-as-tax-and-compliance-complexity-accelerates-WEpMYuY5kxr", date: 2026-10-08, access: full, locator: "paragraph on Avalara Aviator" }
  last_reviewed: 2026-10-17
  notes: >
    The Vertex capability is described secondhand, in a blog by an implementation partner that recaps the conference.
    Vertex's own pages for this capability were not read.
```

---

## 3. Module notes

### 3.1 Processes, key steps and work types

- **Tax determination** (rate, taxability, place of supply, exemption) at transaction level: `transaction-processing`. Vendors and practitioners agree this stays rule-based ([FONOA-STACK-2025], [TR-AGENTICIT-2026]).
- **Product and service classification / mapping to tax codes:** `transaction-processing`, `data-reporting` (use case 01).
- **Exemption and resale certificate collection, validation and storage:** `transaction-processing`, `review-assurance` (use case 02).
- **Registration and nexus monitoring:** `research-synthesis`, `data-reporting` (use case 12).
- **Return preparation, reconciliation and filing** (US sales and use tax, VAT/GST returns, EU listings): `data-reporting`, `transaction-processing` (use cases 03, 07).
- **E-invoicing and continuous transaction controls:** submission, clearance, rejection handling, master data: `transaction-processing` (use case 04).
- **Regulatory change monitoring:** `research-synthesis` (use case 05).
- **Accounts-payable-side review** (input VAT recovery, use tax, overpayment recovery): `review-assurance` (use case 06). A Phoenix business magazine column by an EisnerAmper managing director advises companies to review accounts payable for sales tax overpaid on AI-related purchases, since many pay the amount billed [INBUSINESS-FLICK-2026]; that review is described as a human forensic review, not AI-performed.
- **Audit defence and notice response:** `expert-judgment`, `document-production` (use case 08).
- **Advice on new business models** (marketplace and deemed-supplier status, agentic commerce, taxability of AI products): `expert-judgment`.

### 3.2 Common pain points (as stated by practitioners)

- Risk now surfaces at the invoice rather than at filing; a rejected e-invoice can stop shipments and delay revenue recognition [INNOVATETAX-VXE-2026]. In clearance regimes an invoice has no legal force until the authority returns an identifier [TRINST-TEIAUDITOR-2026].
- Master data (customers, tax registrations, certificates, product classes) came up so often at Vertex Exchange Europe that the audience counted mentions [INNOVATETAX-VXE-2026].
- E-invoicing is sold to CFOs as a compliance project but needs shared ownership across tax, IT, finance, AP and sales [INNOVATETAX-VXE-2026].
- Rules multiply faster than teams: more than 70 countries changed e-invoicing rules since 2020, and teams are flat or shrinking (Fonoa, a vendor) [FONOA-REGMON-2026].
- Leadership mandates without measures: nearly nine in ten tax functions face pressure to adopt AI and only 12.5% have specific targets [FONOA-2026-SURVEY]. The BDO partner quoted by Fonoa said the KPI "is essentially: are we using AI? Yes or no?" [FONOA-2026-SURVEY].
- Taxability of AI products themselves is unsettled: no state taxes AI as such; states tax what the customer buys (software, information services, data processing or consulting) [TAXNOTES-AISTATE-2026]. EisnerAmper says 30 states classify AI as SaaS, treatments of SaaS vary, and bundling can cause whole invoices to be taxed [INBUSINESS-FLICK-2026]. An IBFD study (Mar 2026) examines classification of AI-powered services as electronically supplied services under EU VAT and the "minimal human intervention" criterion (abstract only) [IBFD-AIVAT-2026].

### 3.3 Metrics and benchmarks (with sources)

- 92% of tax functions use AI in some form; nearly nine in ten face leadership pressure; 12.5% have specific targets or KPIs; 57.4% would not be confident defending AI-assisted decisions to an authority; only a third run formal human-in-the-loop review; sample 176 indirect tax leaders; vendor-sponsored; landing page only [FONOA-2026-SURVEY].
- Thomson Reuters (vendor) reports from its own reports: 58% of corporate tax departments under-resourced and 56% of time on reactive tasks (2025 State of the Corporate Tax Department); 64% at the reactive or chaotic end of its maturity curve (2026 technology report); the most common estimate of when AI becomes central moved from three to five years to one to two years [TR-AGENTICIT-2026]. These are second-hand figures quoted in a vendor blog; the reports were not opened.
- ONESOURCE Sales and Use Tax AI vendor claims: up to 65% less time on routine reporting; up to 75% less audit exposure; 30 to 11 days compliance cycle; $25,000 and $60,000+ annual savings [TR-SUTAI-2026].
- Sovos France e-invoicing: 1.6% rejection rate versus an estimated 20% market-wide; 170,000 registrants; vendor claims [SOVOS-FRANCE-2026].
- Avalara single-lookup test of a general chatbot (10.3% vs 10.2%) [AVALARA-LLMTEST-2025].
- State agencies: Tax Notes' 2025 survey went to 49 state and jurisdictional agencies; of 36 responding, 22 said they used no AI, 7 said they did, 6 said they were interested in AI (including some non-users) and 3 did not say [TAXNOTES-UNWATCHED-2026].
- Tax authority speed claim: the OECD's Hanna Lee said some administrations cut VAT non-compliance investigations from about nine months to three, reported by a trade site from a June 2026 OECD conference; second-hand [SSL-OECDVAT-2026].
- **Independent measurement of AI quality in indirect tax: none found.** No override rate, error rate, parallel run or inspection result.

### 3.4 Guardrails and regulatory points

- Vendors' product documentation instructs users to review AI-suggested codes and notes that high confidence does not guarantee correctness [SOVOS-DOCS-AICLASS].
- Marketplace and deemed-supplier rules apply by function (payment control, involvement in essential elements), not by label; an agent operator may have to collect tax [BTAX-AGENTIC-2026].
- ViDA timeline (approved 5 Nov 2024): OSS expansions in Jan 2027 and Jul 2028; EN 16931 e-invoicing and digital reporting for intra-EU transactions from Jul 2030; harmonisation by Jan 2035 [EU-VIDA-2024]. Several member states have domestic mandates earlier (Belgium, Croatia, Poland, Romania per [BTAX-VAT2026]). France's mandate began on 1 Sep 2026 per vendor releases [SOVOS-FRANCE-2026] [AVALARA-CRUSHEU-2026].
- OECD's Forum on VAT (sixth meeting, 26-29 Jan 2026) called crypto and AI "emerging challenges" to VAT administration; Bloomberg Tax's piece is paywalled after the opening [BTAX-OECDVAT-2026].
- Tax Notes found weak oversight of state audit-selection systems partly because it is unclear what counts as AI [TAXNOTES-UNWATCHED-2026].
- Professional-conduct guidance (IRS OPR Alert 2026-19, UK PCRT, Australian TPB) sits in other agents' scope; no indirect-tax-specific conduct guidance was found.

### 3.5 Frontier signals (dated, sourced)

- **30 Sep 2025:** Avalara announces an agentic platform with agents that call each other and customers' agents ("Have your agent call our agent") [AVALARA-AGENTIC-2025].
- **15 Jan 2026:** Thomson Reuters launches ONESOURCE Sales and Use Tax AI, "touchless by default, manual by exception" [TR-SUTAI-2026].
- **24 Mar 2026:** Sovos announces error remediation and an MCP Gateway under development [SOVOS-SOVI-2026].
- **Recap dated 6 May 2026:** Vertex Exchange Europe (Vienna) frames the shift from continuous transaction controls to "continuous audit controls" and asks whether Europe will extend mandates beyond invoices to wider transaction data, as LATAM has [INNOVATETAX-VXE-2026].
- **Apr 2026:** TEI Tax Technology Seminar: panel says authorities arrive at audits with structured data already analysed; one panelist heard of companies abandoning compliance and padding numbers, and a panelist answered "Do not do this" [TRINST-TEIAUDITOR-2026].
- **26 Feb 2026:** Hungary's tax authority audit plan says it uses AI-based models and real-time data to identify high-risk companies, even at invoice issuance [KPMGHU-AUDITPLAN-2026].
- **Jul 2026:** the Sales Tax Institute flags agent-initiated checkout as a sales tax holiday problem [STI-AGENTIC-2026].
- **1 Oct 2026:** Sovos acquires Flowie to pair finance agents with tax compliance data [SOVOS-FLOWIE-2026].
- **8 Oct 2026:** Avalara Aviator generally available; Avalara "approved platform in France since September 2026" and expects readiness for Germany in Jan 2027 and Spain in Oct 2027 [AVALARA-CRUSHEU-2026].
- **Upcoming:** Vertex Exchange, Las Vegas, 25-28 Oct 2026, with AI "inside governed workflows with human-in-the-loop control" [VERTEX-EXCHANGE-2026]; New England State and Local Tax Forum, 18 Nov 2026, including a session on automation and AI [NESALT-2026]. TEI's annual conference starts 18 Oct 2026 and has no recaps yet (per the landscape file).

### 3.6 Workforce and role effects

- The Vertex recap says the future tax team is hybrid (legislation, systems, process design, data flows) [INNOVATETAX-VXE-2026]. The TEI recap says the job is as much a data-science problem as an accounting one [TRINST-TEIAUDITOR-2026].
- Fonoa argues domain expertise gets more valuable as models improve, while warning experienced people can mistake long habit for necessity [FONOA-BUILD-2026]. This is a vendor CTO's opinion.
- Thomson Reuters says capacity moves from reactive to strategic work [TR-AGENTICIT-2026]. Fonoa's survey says teams absorb digital-era complexity with flat or declining headcount [FONOA-2026-SURVEY].
- Governance ownership is unsettled: two of more than 50 TEI attendees said the tax function owns AI implementation [TEI-TAXTECH-2026].
- No source gives indirect-tax-specific headcount, hiring or fee effects.

### 3.7 Objections and concerns

- **Silent failure.** AI "fails quietly and even politely", making review harder as volume grows [TEI-TAXTECH-2026].
- **Defensibility to authorities.** 57.4% unsure they could defend AI-assisted decisions [FONOA-2026-SURVEY]; the point that you demonstrate a process, not a technology [FONOA-2026-SURVEY].
- **Hallucinated rules and stale knowledge** in general models [FLSALESTAX-AI-2026] [FONOA-PRIMARY-2026]; wrong effective dates [AVALARA-LLMTEST-2025].
- **Probabilistic AI in a deterministic job.** Tax calculation and statutory filing format should stay rule-based [FONOA-STACK-2025] [TR-AGENTICIT-2026]. Fonoa argues system-level accuracy and coverage matter more than per-transaction perfection [FONOA-ACCURACY-2025]; this is a vendor argument with hypothetical numbers, and practitioners such as those polled in Fonoa's own survey are not reassured about defensibility.
- **Responsibility in agentic commerce:** retailer, agent platform and protocol layer are unsettled [STI-AGENTIC-2026]; AI has no legal personality [BTAX-AGENTIC-2026].
- **Opacity of state audit selection** and bias [SCPOST-AUDIT-2026] [TAXNOTES-UNWATCHED-2026].
- **Unreviewed vibe-coded tooling** [TRINST-TEIAUDITOR-2026].
- **Vendor-dominated evidence.** Almost every quantitative claim in this module comes from a party that sells software.

### 3.8 Interview probes

1. Which indirect-tax decisions in your function are made by a deterministic engine and which by a model or agent today? Who drew that line, and what evidence supports it?
2. If a tax authority challenged an AI-assisted determination or filing tomorrow, what would you hand over? Do you keep a log of AI-assisted decisions, overrides and approvals?
3. What are your baseline human error and override rates for product classification, certificate checks and return preparation, and have you measured the AI against them?
4. For e-invoicing and real-time reporting, what share of rejections trace to master data, and who owns that data across tax, finance, IT and sales?
5. Is any of your tax determination now called by someone else's agent (buyer-side, marketplace or ERP)? How current and machine-readable are your exemption and holiday rules, and who is liable when the call is wrong?

---

## 4. Routed to other modules

- **controversy (tax authority AI in audit selection).** South Carolina's revenue department signed a $3.5 million, five-year contract with FAST Enterprises in December 2025 to use AI in audit selection, starting with sales and use tax and then corporate returns; officials say the system uses the same criteria faster and will suggest rather than conduct audits [SCPOST-AUDIT-2026]. Tax Notes survey of state agencies [TAXNOTES-UNWATCHED-2026]. Hungary's AI-based audit risk screening, including at invoice issuance [KPMGHU-AUDITPLAN-2026]. OECD speaker's claim about 9-to-3-month VAT investigations [SSL-OECDVAT-2026].
- **controversy / research-advisory (professional responsibility).** Hallucinated-citation risk in sales tax advice [FLSALESTAX-AI-2026]; no indirect-tax-specific conduct guidance found.
- **tax-data-technology.** Use cases 10 (MCP/A2A access), 13 (finance orchestration) and the e-invoicing data foundations in use cases 04 and 07 overlap with the landscape's definition of tax-data-technology (e-invoicing, real-time reporting, MCP/A2A interoperability). Flagged for the synthesis step to decide placement.
- **international-pillar-two / policy of AI.** Taxability of AI products and services (Tax Notes State, Jan 2026) and AI classification under EU VAT (IBFD, Mar 2026) concern tax on AI, not AI in tax work; they are kept here only as module context [TAXNOTES-AISTATE-2026] [IBFD-AIVAT-2026]. CJEU *Arcomet* (transfer-pricing adjustments and VAT) is noted in Bloomberg Tax's 2026 outlook and belongs with transfer-pricing [BTAX-VAT2026].
- **transfer-pricing.** The Arcomet ruling's VAT consequences for year-end adjustments [BTAX-VAT2026].

---

## 5. Sources

Access is `full` unless stated. For podcasts, "full" means the episode or show-note page was opened; no audio was heard. Retrieved-date entries are product pages without a publication date.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| STI-AGENTIC-2026 | Can AI Shopping Agents Apply Sales Tax Holidays? | Sales Tax Institute | press | https://www.salestaxinstitute.com/resources/ai-shopping-agents-sales-tax-holidays | 2026-07-29 | full |
| BTAX-AGENTIC-2026 | Artificial Intelligence Goes Shopping, Creates Tax Challenges (A. Bal, Stripe) | Bloomberg Tax | press | https://news.bloombergtax.com/tax-insights-and-commentary/artificial-intelligence-goes-shopping-creates-tax-challenges | 2026-02-24 | full |
| BTAX-VAT2026 | Digital Mandates and AI Reshape VAT Compliance Landscape in 2026 (E. Trombitas) | Bloomberg Tax | press | https://news.bloombergtax.com/tax-insights-and-commentary/digital-mandates-and-ai-reshape-vat-compliance-landscape-in-2026 | 2026-01-06 | full |
| BTAX-OECDVAT-2026 | OECD Identifies Crypto and AI As Challenges to VAT Systems | Bloomberg Tax | press | https://news.bloombergtax.com/tax-insights-and-commentary/oecd-identifies-crypto-and-ai-as-challenges-to-vat-systems | 2026-01-29 | full (opening paragraphs; rest paywalled) |
| FONOA-2026-SURVEY | State of Indirect Tax in the AI Era 2026 | Fonoa | survey | https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026 | 2026-06-17 | full (landing page; report gated) |
| TEI-TAXTECH-2026 | 2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 | full |
| TRINST-TEIAUDITOR-2026 | 2026 TEI Tax Technology Seminar: What the auditor already knows | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows | 2026-05-12 | full |
| INNOVATETAX-VXE-2026 | What we learned from Vertex Exchange Europe 2026 | Innovate Tax | conference | https://innovatetax.com/blog/what-we-learned-from-vertex-exchange-europe-2026/ | 2026-05-06 | full |
| VERTEX-EXCHANGE-2026 | Vertex Exchange 2026 (Las Vegas, 25-28 Oct 2026) | Vertex Inc. | conference | https://www.vertexinc.com/node/8263 | 2026-06-24 | full |
| AVALARA-NEXT-2026 | Avalara NEXT: The future of agentic tax and compliance | Avalara | conference | https://www.avalara.com/us/en/blog/avalara-next-2026-building-the-future-of-agentic-tax-and-compliance.html | 2026-03-04 | full |
| AVALARA-CRUSH-2026 | Avalara CRUSH Returns as Agentic AI Reshapes Tax and Compliance (CRUSH 22-24 Sep 2026) | Avalara (PR Newswire) | conference | https://digital-release.wboy.com/business/press-releases/cision/20260505SF51187/avalara-crush-returns-as-agentic-ai-reshapes-tax-and-compliance | 2026-05-05 | full |
| AVALARA-CRUSHEU-2026 | Avalara Helps Global Businesses Move Faster as Tax and Compliance Complexity Accelerates (CRUSH Europe) | Avalara (PR Newswire) | conference | https://www.webdisclosure.com/press-release/avalara-helps-global-businesses-move-faster-as-tax-and-compliance-complexity-accelerates-WEpMYuY5kxr | 2026-10-08 | full |
| COST-SALTDIGITAL-2026 | SALT In A Digital World Workshop (COST, 2-4 Mar 2026) | COST via GovEvents | conference | https://govevents.com/event/25261 | 2026-03-02 | full (event listing) |
| NESALT-2026 | 2026 New England State and Local Tax Forum (18 Nov 2026) | Event listing | conference | https://happeningnext.com/event/2026-new-england-state-and-local-tax-forum-eid1ef0kr2sle7r | 2026-11-18 | full (agenda listing; upcoming) |
| ITR-AIFORUM-2025 | Speakers - ITR AI in Tax Forum 2025 | International Tax Review | conference | https://event.internationaltaxreview.com/event/bfd4f100-335f-47de-841d-b03beb6a3d86/speakers | 2025-09-16 | full (speaker list only) |
| AVALARA-AGENTIC-2025 | Avalara launches 'always on, always ready' AI agents | Accounting Today | press | https://www.accountingtoday.com/news/avalara-launches-always-on-always-ready-ai-agents | 2025-09-30 | full |
| SCPOST-AUDIT-2026 | SCDOR to use AI to help decide which tax returns to audit | Post and Courier | press | https://www.postandcourier.com/news/sc-taxes-artificial-intelligence-audits-fast-scdor/article_54662d56-ae30-4130-845a-366547409477.html | 2026-04-12 | full |
| TAXNOTES-UNWATCHED-2026 | Tax Notes Investigates States' Use of AI in Audit Selection (excerpting Tax Notes, 14 Apr 2026) | TaxProf Blog | press | https://taxprofblog.aals.org/?p=134442 | 2026-05-02 | full (excerpt) |
| TAXNOTES-AISTATE-2026 | What's New in the World of AI and State Tax? (Eisenstein and Caissie) | Tax Notes State | press | https://brannlaw.com/wp-content/uploads/2026/02/2026tns3-3-1.pdf | 2026-01-19 | full (first pages) |
| INBUSINESS-FLICK-2026 | AI Sales Tax Missteps Could Leave Refunds on the Table (W. Flick, EisnerAmper) | Greater Phoenix In Business | press | https://inbusinessphx.com/?p=191259 | 2026-05-28 | full |
| SSL-OECDVAT-2026 | OECD: AI Is Cutting VAT Non-Compliance Investigations from 9 Months to 3 | SharedServicesLink | press | https://sharedserviceslink.com/news/oecd-ai-is-cutting-vat-non-compliance-investigations-from-9-months-to-3 | 2026-06-29 | full (via mirror) |
| SOVOS-SOVI-2026 | Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability | Sovos | vendor | https://sovos.com/press-releases/sovos-expands-sovi-ai/ | 2026-03-24 | full |
| SOVOS-FRANCE-2026 | Three Weeks into France E-Invoicing Mandate: Sovos Hits Unparalleled Production Scale | Sovos | vendor | https://sovos.com/press-releases/three-weeks-into-france-e-invoicing-mandate-sovos-hits-unparalleled-production-scale/ | 2026-09-23 | full |
| SOVOS-FLOWIE-2026 | Sovos Acquires Flowie, Launching the Industry's First Agentic Compliant Finance Orchestration Platform | Sovos | vendor | https://sovos.com/press-releases/sovos-acquires-flowie-launching-the-industrys-first-agentic-compliant-finance-orchestration-platform/ | 2026-10-01 | full |
| SOVOS-DOCS-AICLASS | About AI product classification | Sovos | vendor | https://docs.sovos.com/en/indirect-tax/indirect-tax-products/tax-determination/tax-determination/map-products-exemptions-and-locations/ai-product-classification/about-ai-product-classification | 2026-10-17 (retrieved) | full |
| TR-SUTAI-2026 | Thomson Reuters Launches AI Tax Compliance Solution That Saves Time and Reduces Risk | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2026/january/thomson-reuters-launches-ai-tax-compliance-solution-that-saves-time-and-reduces-risk | 2026-01-15 | full |
| TR-HELP-PRODCLASS | Review product classification results | Thomson Reuters | vendor | https://www.thomsonreuters.com/en-us/help/onesource-indirect-tax/indirect-tax-compliance/mappings/product-classification/review-product-classification-results | 2026-10-17 (retrieved) | full |
| TR-AGENTICIT-2026 | Is your tax department ready for the agentic AI explosion? | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/is-your-tax-department-ready-for-the-agentic-ai-explosion/ | 2026-06-08 | full |
| TR-WEBINAR-JLL | Transforming indirect tax with AI (on-demand webinar with JLL) | Thomson Reuters | vendor | https://europe.thomsonreuters.com/on-demand-webinars/transforming-indirect-tax-ai | 2026-10-17 (retrieved) | full (description) |
| AVALARA-ECM-2026 | How AI Improves Exemption Certificate Management | Avalara | vendor | https://www.avalara.com/blog/en/north-america/2026/02/ai-exemption-certificate-management.html | 2026-02-23 | full |
| AVALARA-LLMTEST-2025 | Why AI not backed by tax expertise can get sales tax rates wrong | Avalara | vendor | https://www.avalara.com/blog/en/north-america/2025/11/ai-tax-expertise-accurate-sales-tax-rates.html | 2025-11-20 | full |
| FONOA-AIERA-2025 | Preparing for the Era of AI in Indirect Tax | Fonoa | vendor | https://www.fonoa.com/resources/blog/ai-era-indirect-tax-strategy | 2025-10-23 | full |
| FONOA-ACCURACY-2025 | AI Won't Make Your Tax Determinations Perfect (And That's Fine) | Fonoa | vendor | https://www.fonoa.com/resources/blog/ai-tax-determination-accuracy | 2025-10-29 | full |
| FONOA-STACK-2025 | Where AI Belongs in Your Tax Stack (And Where It Doesn't) | Fonoa | vendor | https://www.fonoa.com/resources/blog/where-ai-belongs-in-your-tax-stack | 2025-11-04 | full |
| FONOA-ERRORRATE-2025 | Your "Accurate" Tax Process Probably Has a 20% Error Rate | Fonoa | vendor | https://www.fonoa.com/resources/blog/accurate-tax-process-error-rate | 2025-11-11 | full |
| FONOA-REGMON-2026 | The Math No Longer Works for Indirect Tax Regulatory Change Monitoring | Fonoa | vendor | https://www.fonoa.com/resources/blog/indirect-tax-regulatory-change-monitoring | 2026-09-16 | full |
| FONOA-PRIMARY-2026 | Why Primary Source Citation Matters for Tax Audit Defense | Fonoa | vendor | https://www.fonoa.com/resources/blog/primary-source-tax-law-citation-audit | 2026-09-21 | full |
| FONOA-BUILD-2026 | Fast Code Is Cheap. Building Tax Software Well Isn't. | Fonoa | vendor | https://www.fonoa.com/resources/blog/building-tax-software | 2026-10-07 | full |
| VERTEX-TRENDS-2026 | 2026 Indirect Tax Trends | Vertex Inc. | vendor | https://www.vertexinc.com/resources/resource-library/2026-indirect-tax-trends | 2026-02-03 | full |
| TRUSS-KINTSUGI-2026 | What's Changing in Sales and Business Tax - And How AI Can Help (webinar listing) | Truss with Kintsugi | vendor | https://gettruss.io/events/sales-business-tax-ai | 2026-09-17 | full (listing) |
| EU-VIDA-2024 | EU Member States Approve the VAT in the Digital Age (ViDA) Package | Fonoa | vendor | https://www.fonoa.com/resources/blog/eu-member-states-approve-vat-in-the-digital-age-vida-package | 2024-11-05 | full |
| SAFFERY-VAT-2026 | Transforming VAT (webinar) | Saffery | firm | https://www.saffery.com/insights/videos-webinars/transforming-vat/ | 2026-09-08 | full (description) |
| FLSALESTAX-AI-2026 | Can I Trust AI for Florida Sales Tax Advice? | floridasalestax.com (James H. Sutton Jr., CPA, Esq.) | firm | https://www.floridasalestax.com/florida-tax-law-blog/2026/june/can-i-trust-ai-for-florida-sales-tax-advice-/ | 2026-06-06 | full (via mirror) |
| KPMGHU-AUDITPLAN-2026 | Tax Alert, 26 Feb 2026 (Hungarian Tax Authority 2026 audit plan) | KPMG Hungary | firm | https://kpmg.com/hu/en/insights/2026/02/taxalert-2026-02-26.html | 2026-02-26 | full |
| IBFD-AIVAT-2026 | The Treatment of AI-Powered Services under European VAT (G. Beretta), International Tax Studies 9(3) | IBFD | academic | https://shop.ibfd.org/journal/treatment-ai-powered-services-under-european-vat | 2026-03-02 | full (abstract only; paywalled) |
| EYTALKS-2026-05 | EY talks tax: EY Tax.Tech 2026, AI in tax - what's working now and what's next (webcast 6 May) | EY | podcast | https://taxnews.ey.com/news/2026-1106-ey-talks-tax-ey-taxtech-2026-building-the-future-of-tax-ai-in-tax-whats-working-now-and-whats-next-may-6 | 2026-05-20 | full (episode description via mirror; audio not heard) |
| EYTALKS-2025-12 | EY talks tax: The future of Tax - leveraging agentic technologies to redefine tax operations (webcast 2 Dec 2025) | EY | podcast | https://taxnews.ey.com/news/2025-2585-ey-talks-tax-the-future-of-tax-leveraging-agentic-technologies-to-redefine-tax-operations-december-2-2025 | 2025-12-19 | full (episode description; audio not heard) |
| DELOITTE-TAXONAIR-2026 | Tax on Air, Episode 35: Der Einsatz generativer KI im Bereich Indirect Tax (German) | Deloitte Germany | podcast | https://www.audible.co.uk/podcast/Tax-on-Air/episodes/B0CKHRXDGS | 2026-06-25 | full (episode description via mirror; audio not heard) |

Cited in use cases or notes: all rows above except FONOA-AIERA-2025, VERTEX-TRENDS-2026, COST-SALTDIGITAL-2026, AVALARA-CRUSH-2026, ITR-AIFORUM-2025, EYTALKS-2026-05, EYTALKS-2025-12 and DELOITTE-TAXONAIR-2026, which are listed for coverage and used only in the notes below.

Notes on the coverage-only rows:
- **DELOITTE-TAXONAIR-2026** (25 Jun 2026): the description says three Deloitte Germany speakers discuss how generative AI is used in indirect tax practice, from analysis of large data sets to structured contract-clause review, and cover data quality, governance, quality assurance, the EU AI Act, liability and changing role profiles. It says professional responsibility stays with the tax adviser despite automation.
- **EYTALKS-2026-05 / EYTALKS-2025-12:** general tax AI webcasts (not indirect-tax specific), description-level only.
- **COST-SALTDIGITAL-2026** (2-4 Mar 2026, Burlingame, California): the listing says the workshop opens with interactive AI sessions (attendees asked to bring a computer with Copilot installed) and has "multiple sessions covering AI" for state and local tax; only COST industry members are invited, so the content is not public.
- **ITR-AIFORUM-2025** (16 Sep 2025): the speaker list includes indirect-tax practitioners from Stripe, Uber, Cisco, Paddle.com, Vodafone and Booking.com and HMRC's head of innovation; no session content was read.
- **AVALARA-CRUSH-2026** (22-24 Sep 2026, Fort Lauderdale): the pre-event release says CRUSH will showcase Avalara's AI agent "Avi"; no North America recap was reached.
- **VERTEX-TRENDS-2026:** lists AI and agentic purchasing among 2026 indirect-tax trends and says "make-or-break time for e-invoicing compliance"; no AI-use evidence.
- **FONOA-AIERA-2025:** introduction to the Fonoa blog series; its claims are covered through its sibling posts.

---

## 6. Gaps

- **Community discussion not reached.** Reddit (r/taxpros and others) blocked access; TaxProTalk, LinkedIn and AccountingWEB threads were not reached. The only community-style item seen, a Thomson Reuters Community thread, was a vendor webinar post with no replies and no usable date, so it was left out. No practitioner forum evidence about indirect-tax AI errors, overrides or workarounds is in this file.
- **Web search ran out.** The shared quota was exhausted during the task. Directions not searched: agentic commerce protocol tax handling (ACP/UCP) and Stripe/Shopify documentation; practitioner interviews on AI in VAT returns; post-launch reports on France's September 2026 e-invoicing rejections (no post-launch independent reports were found); Poland KSeF (Feb 2026) experience; Peppol and ViDA AI commentary; Anrok, Kintsugi, Zamp and Numeral claims.
- **Primary material not reached or paywalled:** Fonoa's full survey report; Thomson Reuters Corporate Tax Department reports; Tax Notes full text; Bloomberg Tax articles beyond the opening; the OECD sources behind the "76% / 69%" enforcement figures and the "9 months to 3" claim (seen only through a trade site and search summaries, so the OECD figures are not used in any use case); vatcalc.com and Wolters Kluwer pages (bot-blocked); Avalara's 9 Apr 2026 release (404); Vertex investor and product pages; GTM Insights, ENVISION 2026 recap (blocked); KPMG UK's "From Gen AI to Agentic AI in tax" article (opened but undated, so excluded; it says about half of surveyed tax leaders at a client event use gen AI weekly and about a third daily).
- **Podcasts and webinars:** no audio or transcript was reached; only descriptions of EY talks tax, Deloitte Tax on Air #35, the Saffery webinar and the Thomson Reuters/JLL webinar. The JLL experience is not reported in a form that can be quoted.
- **Conference sessions:** no session-level content for Avalara CRUSH North America (22-24 Sep 2026), Vertex Exchange 2026 (starts 25 Oct), TEI annual (starts 18 Oct), COST SALT in a Digital World (members only), or IFA Melbourne. The Vertex Exchange Europe recap is a partner's blog, not Vertex's own material.
- **Quality evidence.** No error rates, override rates, parallel-run results, inspection findings or independent benchmarks for AI in indirect tax. Evidence grades therefore stop at C; there are no A or B use cases. The only quantified quality items are vendor claims or single examples.
- **Named customer deployments.** No indirect-tax team was found describing its own AI use with numbers. Companies named at vendor events (Fortnum & Mason, ASOS, Siemens Energy, Daimler Truck, Oxford Nanopore) were described using automation or tax engines, not AI-specific outcomes; JLL appears only in a webinar blurb.
- **Under-covered areas:** non-US, non-EU, non-UK markets (India GST, Brazil's reform, Gulf VAT) beyond headlines; customs and tariff classification (routed in the landscape to a separate topic); payroll and property taxes.
- **Date caveats:** undated product-documentation pages carry the retrieval date; the Truss webinar year is inferred. A Thomson Reuters Community thread on closed-loop exemption-certificate automation (CERTifyTax with ONESOURCE) shows only "over 1 year ago" and was left out.

# Module deep dive: tax / tax-data-technology / discourse

- **Archetype:** tax
- **Module:** tax-data-technology (the landscape calls it tax-data-technology). In-house tax operations and data architecture: ERP-to-tax data flows, tax data warehouses, sustaining automation, tax technology teams and operating model, real-time reporting interfaces, MCP and agent interoperability with tax engines. Excludes indirect-tax determination engines and GloBE Information Return filing, which belong to their own modules.
- **Angle:** discourse. What practitioners are saying in the last 12-18 months: conference sessions and recaps, panels, podcasts, practitioner articles, vendor and firm commentary, and survey write-ups; where the field says it is heading and what worries it.
- **Prepared:** 2026-10-17
- **Method note.** About 34 distinct sources were opened with `curl` (HTML text extraction, `pdftotext` for PDFs, the `r.jina.ai` mirror for the OECD news item, the CIOT Tax Adviser and PwC Ireland pages). Ten web searches were used, for directions the landscape did not cover (podcasts and webinars, MCP in tax, automation sustainment, tax data platforms and ERP migration, vibe-coding governance, real-time reporting operating models, first Pillar Two filing season, the CIOT podcast, Tax Executive articles). Podcasts and conference sessions were read through episode descriptions, programmes, slide decks and written recaps only; no audio, video or transcripts were reached. TEI sessions are member-only, so TEI practice is seen through the Thomson Reuters Institute recaps (vendor-owned) and one vendor press release. Every survey figure is the publisher's own (Thomson Reuters, EY, KPMG, Fonoa are all sellers of tax technology or advice), so figures are marked `vendor-published` unless a deploying organisation made the claim. Source refs follow `PUBLISHER-SHORT-YYYY` and reuse the landscape's keys where the document is the same.

---

## 1. Summary

1. **The conversation has moved from "does it work?" to "who owns it, and is the data good enough?"** The Thomson Reuters Institute recap of the April 2026 TEI Tax Technology Seminar says the question of whether the tools work was "effectively settled" for attendees, and that the new problems were silent failures, governance gaps, failed training rollouts and rising token costs. A poll of more than 50 attendees found two hands up for "the tax function owns AI implementation" [TEI-TAXTECH-2026]. Vendors and firms say the same thing from the other side: EY's survey reports 80% of tax and finance functions say insufficient AI-ready data is a significant barrier [BTAX-EYTFO-2026]; the panel deck from the Nov 2025 TEI-SJSU institute calls fragmented data the number one blocker [SJSU-TEIHTTI-2025].
2. **Real-time reporting is described as the forcing function for in-house data architecture.** Practitioners at TEI and Vertex Exchange Europe describe VAT risk moving from the return to the invoice, authorities arriving at audits with data they have already analysed, and rejected e-invoices stopping shipments [TR-TEIAUDITOR-2026] [INNOVATETAX-VERTEXEU-2026]. The OECD's tax administrations agreed in Nov 2025 to move to pilots of real-time automated sharing of secure information [OECD-FTA-2025]. The data-architecture answer practitioners give is the same each time: master data, source-level data capture, lineage, and cross-functional ownership [TR-GOVERNANCE-2026] [VERTEX-VIDA-2026].
3. **In-house teams are building their own pipelines, and worry about it.** Attendees at TEI described vibe-coding data integration pipelines in 15 minutes that once waited two months in an IT queue, and also Alteryx workflows nobody could explain after the builder left [TR-TEIAUDITOR-2026] [TEI-TAXTECH-2026]. A panel including RSM, Grant Thornton, EY and OpenAI's tax department showed the progression from one-shot prompting to multi-agent workflows with humans handling exceptions [SJSU-TEIHTTI-2025]. TEI's Nov 2025 programme had a session on automation sustainment, so the maintenance problem is recognised [TEI-TECHTAX-2025].
4. **Agent interoperability with tax engines is a vendor story so far.** Avalara describes a family of MCP servers and Sovos says it is developing an MCP gateway with A2A support to follow [AVALARA-MCP-2026] [SOVOS-SOVI-2026]. No in-house team has described using them. The only guidance on controls comes from the vendor (least-privilege scopes, logging of every tool call, idempotent filings).
5. **There is no independent quality evidence.** No error rate, override rate, parallel-run result or inspection finding for AI in tax data and operations was found. The nearest items are survey perceptions: 66% of AI users in KPMG Germany's quick survey report noticeable time savings [KPMG-DE-2026], and 57.4% of 176 indirect tax leaders said they would not be confident defending AI-assisted decisions to a tax authority today [FONOA-2026]. Time-saved figures on conference slides are demonstration timings from the presenter [SJSU-TEIHTTI-2025].
6. **Operating model and roles are shifting faster than technology.** The 2026 TRI/TEI report says 88% of corporate tax departments now have a designated lead for tax technology strategy, up from 51% a year earlier, while 22% track no technology performance metrics [TR-REBRAND-2026]. PwC Ireland expects new roles such as tax data leads and model governance leads [PWC-IE-2026]. A law professor argues AI will not shrink corporate tax teams much because it cannot carry the consequences of culpability [TAXPROF-SALA-2026].

**Counts:** 17 candidate use cases. Evidence grade A: 0. B: 2. C: 12. D (ideas): 3.

---

## 2. Use cases

Notes on fields. Most use cases here are changes to in-house tax data and operations, so `function` is `finance-accounting` (one is `technology-it`). `pattern: other` is used where no listed pattern fits and the pattern is described in `notes`. Survey figures are the publisher's own and are marked `vendor-published`, because the publishers sell tax technology or advice. Where an item sits partly in another module (indirect-tax determination, GloBE filing), the notes say so and the module-specific part is listed in section 4.

```yaml
- id: tax-data-technology-01
  title: Governed tax data platform that consolidates ERP, ledger and subledger data for AI use
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [data-reporting, software-systems]
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: >
    Tax teams sit downstream of finance systems and often get data that is aggregated, reclassified or stripped of
    detail [TR-GOVERNANCE-2026]. EY's survey says 80% of tax and finance functions see insufficient AI-ready data as
    a significant barrier, 91% say their data sits in too many silos (especially on local drives), and only 17% of
    tax functions rate themselves "very effective" at managing data [BTAX-EYTFO-2026]. The TEI-SJSU panel deck names
    fragmented data, data trapped in spreadsheets and SaaS silos, as the number one blocker to AI in corporate tax
    [SJSU-TEIHTTI-2025].
  solution: >
    Build one governed store for tax-relevant data pulled from ERP, ledger and other sources, and run reporting,
    automation and agents on top of it. EY says best-in-class organisations centralise data on platforms such as
    Databricks and Snowflake, and that these organisations are in the minority [BTAX-EYTFO-2026]. When attendees
    at the April 2026 TEI seminar polled themselves on tooling, the answers included Alteryx, Power Platform,
    Snowflake, Databricks, Microsoft Fabric and Palantir Foundry [TR-TEIAUDITOR-2026]. TEI's Nov 2025 programme had a
    session titled "Microsoft Fabric for ETL" [TEI-TECHTAX-2025]. Deloitte Tax and Databricks announced an expanded
    alliance on 8 Oct 2025 to build a "unified tax data architecture" and a single source of truth for tax data
    [DELOITTE-DATABRICKS-2025]. A Thomson Reuters roundtable of tax and finance leaders said governed data lakes
    support AI and self-service reporting [TR-SAP-2025].
  outcomes:
    - lever: quality
      description: No measured outcome from a tax data platform was published. The survey ties AI readiness to data.
      figure: "80%"
      measures: "tax and finance functions saying insufficient AI-ready data is a significant barrier to advancing AI (EY Tax and Finance Operations Survey, 1,600 CFOs and senior finance and tax leaders)"
      provenance: vendor-published
      source_ref: BTAX-EYTFO-2026
    - lever: quality
      description: Share of tax and finance functions in early data management maturity.
      figure: "51%"
      measures: "tax and finance functions 'still in the early stages of data management maturity' (same EY survey)"
      provenance: vendor-published
      source_ref: EY-TFO-2025
  prerequisites:
    - Named data ownership and consistent naming conventions between tax, finance and IT [TR-SAP-2025]
    - Tax requirements captured at the source system, with direct feeds in place of manual extracts [TR-GOVERNANCE-2026]
    - A platform the enterprise already runs (the sources name Databricks, Snowflake, Fabric, Foundry) [BTAX-EYTFO-2026] [TR-TEIAUDITOR-2026]
  risks_and_guardrails:
    - EY says 45% of leaders cite the lack of a sustainable data, AI and technology strategy as their top barrier, so a platform without a plan is a risk in itself [BTAX-EYTFO-2026].
    - Data hygiene is described as a compliance control and not an IT issue; reconciliation checkpoints between source data and tax inputs and documented lineage are recommended [TR-GOVERNANCE-2026].
  human_checkpoints:
    - Tax leadership signs off data requirements for new business lines before launch [TR-GOVERNANCE-2026]
    - Data quality review before filing deadlines [TR-GOVERNANCE-2026]
  role_evolution: >
    Tax leaders are expected to influence how data is captured at its source, including taking part in ERP
    implementations [TR-GOVERNANCE-2026]. PwC Ireland expects roles such as "tax data lead" to emerge [PWC-IE-2026].
  evidence_grade: C
  sources:
    - {ref: BTAX-EYTFO-2026, title: "AI Era Requires Continuous Tax and Finance Transformation", publisher: "Bloomberg Tax Daily Tax Report (author byline not shown in the text read; draws on the EY survey)", type: press, url: "https://news.bloomberglaw.com/daily-tax-report/ai-era-requires-continuous-tax-and-finance-transformation", date: "2026-02-09", access: full, locator: "paragraph 'Data is lifeblood...' and the Databricks/Snowflake sentence"}
    - {ref: EY-TFO-2025, title: "EY report indicates CFOs and tax leaders innovating with AI to manage mounting geopolitical turbulence, talent shortages and regulatory developments", publisher: EY, type: survey, url: "https://ey.com/en_gl/newsroom/2025/11/ey-report-indicates-cfos-and-tax-leaders-innovating-with-ai-to-manage-mounting-geopolitical-turbulence-talent-shortages-and-regulatory-developments", date: "2025-11-18", access: full, locator: "section 'The AI and data imperative'"}
    - {ref: TR-TEIAUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "section 'End of the traditional model', tooling poll paragraph"}
    - {ref: TEI-TECHTAX-2025, title: "2025 TechTAXcelerate: Unleashing the Future of Tax Technology (Webinar Series)", publisher: Tax Executives Institute, type: conference, url: "https://www.tei.org/events-education/events/2025-techtaxcelerate-unleashing-future-tax-technology-webinar-series", date: "2025-11-17", access: full, locator: "preliminary agenda, 20 Nov 10:00 session"}
    - {ref: DELOITTE-DATABRICKS-2025, title: "Deloitte Extends Alliance with Databricks to Modernize Tax Data Management", publisher: Deloitte US, type: firm, url: "https://www.deloitte.com/us/en/about/press-room/deloitte-extends-alliance-with-databricks-to-modernize-tax-data-management.html", date: "2025-10-08", access: full, locator: "paragraphs 1-3 and 'Unified Tax Data Architecture'"}
    - {ref: TR-SAP-2025, title: "How leaders automate tax compliance in SAP S/4HANA", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/how-tax-leaders-automate-compliance-in-sap-s-4hana/", date: "2025-12-02", access: full, locator: "'Key insights', strategy 'Build scalable infrastructure for analytics'"}
    - {ref: SJSU-TEIHTTI-2025, title: "AI and Other Emerging Technologies for Tax Practitioners (41st Annual TEI-SJSU High Tech Tax Institute panel deck)", publisher: "TEI and San Jose State University", type: conference, url: "https://www2.sjsu.edu/taxinstitute/docs/4D_AI.pdf", date: "2025-11-03", access: full, locator: "slide 'What's Actually Blocking AI Adoption in Corporate Tax?'"}
    - {ref: TR-GOVERNANCE-2026, title: "The governance reckoning: How tax departments must prepare for the new era of mandatory compliance", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/tax-departments-mandatory-compliance", date: "2026-06-02", access: full, locator: "'3 actions tax departments must take now', actions 2 and 3"}
    - {ref: PWC-IE-2026, title: "Evolving the tax function with AI: Four key insights to guide tax leaders", publisher: PwC Ireland, type: firm, url: "https://www.pwc.ie/services/tax/insights/evolving-the-tax-function-with-ai.html", date: "2026-07-21", access: full, locator: "insight 4 (new operating model)"}
  last_reviewed: 2026-10-17
  notes: >
    No named in-house team has published a case study of its tax data platform. The Deloitte item is an alliance
    announcement; the TEI tooling poll is unnamed attendees. The 91% silo figure and the 17% "very effective" figure
    are from the Bloomberg Tax write-up of the EY survey and were not seen in EY's own press release. The write-up says 45% cite the lack of a sustainable data, AI and technology strategy as the top barrier; EY's press release says 44%. The EY full report was not opened.

- id: tax-data-technology-02
  title: AI checks on source data and reconciliations before data reaches the tax process
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [data-reporting, review-assurance]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >
    Tax accuracy depends on source data assembled from general ledgers and financial statements across entities, and
    teams spend most of their time on routine work. EY's survey says internal tax staff spend 53% of their time on
    routine tax activities and 16% on highly specialised ones, and would like 21% and 34% [BTAX-EYTFO-2026].
  solution: >
    Agents scan source data and account reconciliations for anomalies, duplicate transactions and unusual
    period-on-period movements, and route exceptions to a person. Deloitte gives "AI agents to flag common anomalies
    in source data and account reconciliations for human review" as a practical step even for departments with
    limited AI adoption [DELOITTE-TTT-2026]. PwC Ireland says AI can identify data discrepancies, duplicate
    transactions and unusual period-on-period movements [PWC-IE-2026]. At the April 2026 TEI seminar, attendees were
    described as deploying validation agents to critique their own outputs [TR-TEIAUDITOR-2026]. In EY's survey, 81%
    said using AI for data acquisition and cleansing in the next two years will have an impact on their tax function
    [BTAX-EYTFO-2026].
  outcomes:
    - lever: quality
      description: Expected impact of AI on data acquisition and cleansing. No measured result published.
      figure: "81%"
      measures: "survey respondents saying AI for data acquisition and cleansing in the next two years 'will have an impact' on their tax function (EY Tax and Finance Operations Survey)"
      provenance: vendor-published
      source_ref: BTAX-EYTFO-2026
  prerequisites:
    - Source data accessible in one place (see tax-data-technology-01)
    - Agreed definitions and thresholds for what counts as an anomaly [DELOITTE-TTT-2026]
  risks_and_guardrails:
    - Agentic corrections to source data should be stored back to the relevant system of record to keep an audit-ready posture [DELOITTE-TTT-2026].
    - Errors from current tools are described as "polite" and silent, so review volume becomes the problem [TEI-TAXTECH-2026].
  human_checkpoints:
    - A person reviews every flagged exception [DELOITTE-TTT-2026]
  role_evolution: >
    PwC Ireland says tax teams should shift from assembling information to applying judgment and conducting
    high-quality reviews [PWC-IE-2026]. EY's author says reviewers must now understand the process behind
    conclusions, not only check that columns subtotal [BTAX-EYGRIP-2025].
  evidence_grade: C
  sources:
    - {ref: DELOITTE-TTT-2026, title: "Tax Transformation Trends, AI-enabled Tax Transformation, Part three: Riding the wave: A framework to plan for AI", publisher: Deloitte Global, type: firm, url: "https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf", date: "2026-07", access: full, locator: "p.4 (Scenario 1), p.5 (Scenario 2); date from PDF metadata (created 2026-07-02)"}
    - {ref: PWC-IE-2026, title: "Evolving the tax function with AI: Four key insights to guide tax leaders", publisher: PwC Ireland, type: firm, url: "https://www.pwc.ie/services/tax/insights/evolving-the-tax-function-with-ai.html", date: "2026-07-21", access: full, locator: "insight 1 (tax moves to the centre of the data map), insight 3"}
    - {ref: TR-TEIAUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "paragraph after the tooling poll"}
    - {ref: BTAX-EYTFO-2026, title: "AI Era Requires Continuous Tax and Finance Transformation", publisher: "Bloomberg Tax Daily Tax Report (author byline not shown in the text read; draws on the EY survey)", type: press, url: "https://news.bloomberglaw.com/daily-tax-report/ai-era-requires-continuous-tax-and-finance-transformation", date: "2026-02-09", access: full, locator: "'Agentic AI: Promise and Practicalities'; 'Trust in Your People'"}
    - {ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: "2026-05-04", access: full, locator: "section 'A very bad wizard'"}
    - {ref: BTAX-EYGRIP-2025, title: "AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way", publisher: "Bloomberg Tax (EY-authored commentary; author shown as EY, views are the author's)", type: press, url: "https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way", date: "2025-11-21", access: full, locator: "section 'People, Skills, Culture'"}
  last_reviewed: 2026-10-17
  notes: >
    The Deloitte item is a scenario-planning example, not a report of use. No source gives a detection rate or a
    false-positive rate. The 53/16 and 21/34 time-split figures are EY survey self-assessments.

- id: tax-data-technology-03
  title: AI-assisted ledger-to-tax mapping and import validation into provision and compliance engines
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [data-reporting, transaction-processing]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >
    Provision and compliance engines are only as accurate as the source data assembled from ledgers and statements
    across entities; vendors and commentators say the binding constraint after Pillar Two is data assembly, not
    calculation [KOGNITOS-2026]. The close-to-provision handoff is described as a common source of delay and error
    [KOGNITOS-2026].
  solution: >
    Use AI to map general ledger accounts to tax categories, import and validate data, and flag anomalies before it
    enters the tax engine. EY's author says earlier AI implementations in tax focused on classifying data, mapping
    general ledger accounts and spotting anomalies [BTAX-EYGRIP-2025]. Thomson Reuters says the goal for ONESOURCE
    direct tax is agentic AI that handles "data import, validation, and mapping" while professionals keep oversight
    [TR-CORPAI-2026]. Kognitos (a non-tax automation vendor) positions itself as a data layer beneath the tax engines
    that assembles, reconciles and validates source data with an audit trail, and says it does not replace the engines
    [KOGNITOS-2026].
  outcomes:
    - lever: speed
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: TR-CORPAI-2026
  prerequisites:
    - A tax engine already in place for provision and compliance [KOGNITOS-2026]
    - Clean, validated, well-structured source data, which vendors call the precondition for their AI [KOGNITOS-2026]
  risks_and_guardrails:
    - Auditability is described as essential because the provision feeds audited financial statements [KOGNITOS-2026].
    - Kognitos cites "58%" of tax departments as under-resourced without naming a survey; the same figure appears in Thomson Reuters's 2025 corporate tax survey [KOGNITOS-2026] [TR-CORPTAX-2025].
  human_checkpoints:
    - Tax professional oversight of the mapped and imported data [TR-CORPAI-2026]
  role_evolution: >
    Thomson Reuters says its direct tax tooling is meant to leave "judgment-intensive work" to the tax professional
    [TR-CORPAI-2026].
  evidence_grade: C
  sources:
    - {ref: TR-CORPAI-2026, title: "AI in corporate tax: key trends, use cases and what's next", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/", date: "2026-07-01", access: full, locator: "section 'Thomson Reuters: From compliance to intelligent compliance'"}
    - {ref: KOGNITOS-2026, title: "AI for Corporate Tax and Provision Automation (2026)", publisher: Kognitos, type: vendor, url: "https://www.kognitos.com/blog/ai-corporate-tax-provision-automation-2026/", date: "2026-06-17", access: full, locator: "sections 'Why Pillar Two made corporate tax a data problem' and 'The split'"}
    - {ref: BTAX-EYGRIP-2025, title: "AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way", publisher: "Bloomberg Tax (EY-authored commentary; author shown as EY, views are the author's)", type: press, url: "https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way", date: "2025-11-21", access: full, locator: "paragraph 'Earlier AI implementations focused on classifying data...'"}
    - {ref: TR-CORPTAX-2025, title: "Why most tax departments aren't using AI yet (State of the Corporate Tax Department 2025)", publisher: Thomson Reuters Tax & Accounting, type: survey, url: "https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/", date: "2025-10-22", access: full, locator: "'Highlights'; 'Why tax departments are holding back'"}
  last_reviewed: 2026-10-17
  notes: >
    Provision-specific mapping belongs to the provision module; this entry covers the data flow into the engine.
    Thomson Reuters describes a "goal", so the maturity is `announced`. The Kognitos post is a vendor marketing piece
    with a self-described narrow scope.

- id: tax-data-technology-04
  title: Governed multi-system reconciliation of ERP data and source documents for in-house tax
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [data-reporting, review-assurance]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >
    In-house tax teams reconcile data across several ERPs and source documents by hand, and the output must hold up
    in an audit. The Savant press release says governance remains a key challenge for many AI deployments
    [SAVANT-2026].
  solution: >
    Savant Labs announced demonstrations at the April 2026 TEI seminar of "multi-system reconciliation across ERPs
    and source documents", AI-powered document extraction and validation, and audit-ready reporting with full data
    lineage. It also announced a co-presented session with Oxford Industries (parent of Tommy Bahama, Lilly Pulitzer
    and Southern Tide) on how Oxford's tax team deploys AI "safely and at scale" [SAVANT-2026]. KPMG Germany's quick
    survey found 29% of tax departments use specialised applications for tax issues, against 89% using company-wide
    standard tools [KPMG-DE-2026].
  outcomes:
    - lever: risk
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: SAVANT-2026
  prerequisites:
    - Connectors to the ERPs and source-document stores [SAVANT-2026]
    - IT approval and data-protection sign-off; KPMG Germany's respondents named IT approvals (47%) and data protection requirements (41%) among the biggest hurdles to wider AI use [KPMG-DE-2026]
  risks_and_guardrails:
    - Savant's pitch is full traceability and an audit trail; the release is promotional and no result was published [SAVANT-2026].
  human_checkpoints:
    - Not described in the release beyond "audit-ready outputs"; review of exceptions is implied, not stated [SAVANT-2026]
  role_evolution: >
    Not described by the source.
  evidence_grade: C
  sources:
    - {ref: SAVANT-2026, title: "Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Tech Seminar 2026", publisher: Savant Labs, type: vendor, url: "https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/", date: "2026-04-16", access: full, locator: "paragraphs 3-6 (session and booth demonstrations)"}
    - {ref: KPMG-DE-2026, title: "Tax departments are increasingly turning to artificial intelligence", publisher: KPMG Germany, type: survey, url: "https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html", date: "2026-05-07", access: full, locator: "'Tax departments are already making extensive use of AI' and 'AI boosts efficiency but requires clear organizational prerequisites'"}
  last_reviewed: 2026-10-17
  notes: >
    Named customer (Oxford Industries) but the source is a vendor release written before the session took place, so
    this is not graded B: no source describes what Oxford runs, how it was measured or whether it is in production.
    KPMG Germany's sample size is not stated in the release.

- id: tax-data-technology-05
  title: Tax-analyst-built data pipelines and mini-apps ("vibe coding") with IT-style controls
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [software-systems, data-reporting]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: personal-assistant
  maturity: piloting
  problem: >
    Data integration requests wait in IT queues. The TRI recap of the April 2026 TEI seminar says pipelines that
    "would have sat in an IT queue for two months" are now built in 15 minutes [TR-TEIAUDITOR-2026].
  solution: >
    Tax analysts use AI coding tools to build their own pipelines and small applications. The TEI-SJSU panel deck
    (RSM, Grant Thornton, EY and OpenAI speakers) lists examples: extracting XML from tax return files into SQL
    tables for reporting, automating monthly tax G/L reconciliations, scraping SEC tax footnotes for peer
    benchmarking, and analysing Slack channels for potential R&D credit expenditure [SJSU-TEIHTTI-2025]. TEI's Nov 2025
    programme included "Can Tax 'pro-code' in No-Code: Python Integration into Excel" [TEI-TECHTAX-2025].
  outcomes:
    - lever: speed
      description: Build time for a data integration pipeline versus time in an IT queue, as described in a conference recap. Not measured on a sample.
      figure: "15 minutes versus two months"
      measures: "time to build a data integration pipeline by vibe coding versus time such a request 'would have sat in an IT queue' (unnamed attendees, TRI recap)"
      provenance: vendor-published
      source_ref: TR-TEIAUDITOR-2026
  prerequisites:
    - An approved AI coding tool and a place to run the output
    - Access to the data the pipeline needs (see tax-data-technology-01)
  risks_and_guardrails:
    - The recap warns that a tax analyst can deploy a pipeline "nobody else has reviewed, documented, or knows how to maintain"; an OpenAI panelist conceded that vibe coding is a new capability and a new problem when asked about security [TR-TEIAUDITOR-2026].
    - Attendees described Alteryx workflows nobody could explain after the builder left the company [TEI-TAXTECH-2026].
    - The panel deck lists "governance fog" and underdocumented processes as blockers and shadow usage as a risk [SJSU-TEIHTTI-2025].
  human_checkpoints:
    - Review, documentation and maintenance ownership for each tool before it enters a filing or reporting process (the gap the sources describe, not a practice they report)
  role_evolution: >
    The recap describes the tax role at the high end as "as much a data science problem as an accounting one"
    [TR-TEIAUDITOR-2026]. The panel deck says tax teams "start building their own tools" [SJSU-TEIHTTI-2025].
  evidence_grade: C
  sources:
    - {ref: TR-TEIAUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "section 'End of the traditional model' and 'Two ways to lose'"}
    - {ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: "2026-05-04", access: full, locator: "section 'A very bad wizard', paragraph on Alteryx workflows"}
    - {ref: SJSU-TEIHTTI-2025, title: "AI and Other Emerging Technologies for Tax Practitioners (41st Annual TEI-SJSU High Tech Tax Institute panel deck)", publisher: "TEI and San Jose State University", type: conference, url: "https://www2.sjsu.edu/taxinstitute/docs/4D_AI.pdf", date: "2025-11-03", access: full, locator: "section 1, item 3 ('Generative AI + Coding') and blockers slide"}
    - {ref: TEI-TECHTAX-2025, title: "2025 TechTAXcelerate: Unleashing the Future of Tax Technology (Webinar Series)", publisher: Tax Executives Institute, type: conference, url: "https://www.tei.org/events-education/events/2025-techtaxcelerate-unleashing-future-tax-technology-webinar-series", date: "2025-11-17", access: full, locator: "agenda, Wednesday 19 Nov 10:00 session"}
  last_reviewed: 2026-10-17
  notes: >
    The pattern is not in the list: a person describes intent and an AI coding tool produces and maintains a working
    data tool. No named in-house team has published a controlled example. TR's recap is vendor-owned (Thomson Reuters
    sells tax software) and the 15-minute figure is anecdotal.

- id: tax-data-technology-06
  title: Turning unstructured tax-authority notices into structured records
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [transaction-processing, data-reporting]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >
    State tax notices "never arrive in the same format twice" [TR-TEIAUDITOR-2026], so they are keyed by hand into
    trackers.
  solution: >
    AI image-to-text extraction pulls structured data out of notices [TR-TEIAUDITOR-2026]. EY's author describes
    AI that reads a notice, summarises key points, amounts and due dates, judges complexity, drafts a response and
    logs the information in a database [BTAX-EYGRIP-2025].
  outcomes:
    - lever: speed
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: TR-TEIAUDITOR-2026
  prerequisites:
    - A notice inbox or scan process that captures every notice
    - A database or tracker to receive structured records [BTAX-EYGRIP-2025]
  risks_and_guardrails:
    - Extraction errors on amounts and due dates carry penalty risk; no error rate was published in the sources.
  human_checkpoints:
    - Review of extracted amounts and dates, and of any drafted response [BTAX-EYGRIP-2025]
  role_evolution: >
    Not described by the sources.
  evidence_grade: C
  sources:
    - {ref: TR-TEIAUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "paragraph after the tooling poll"}
    - {ref: BTAX-EYGRIP-2025, title: "AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way", publisher: "Bloomberg Tax (EY-authored commentary; author shown as EY, views are the author's)", type: press, url: "https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way", date: "2025-11-21", access: full, locator: "section 'Enterprise Tax Functions', 'Tax notes' use case"}
  last_reviewed: 2026-10-17
  notes: >
    Response drafting and notice management belong to the controversy module; this entry is only the data-capture step.
    Neither source names an organisation using it.

- id: tax-data-technology-07
  title: AI diagnosis and approved remediation of failed real-time reporting submissions
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [transaction-processing, software-systems]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >
    In clearance regimes an invoice has no legal force until the tax authority returns its identifier, so a wrong VAT
    ID, malformed schema or mismatched master data means the invoice is rejected, the shipment waits and the buyer
    does not pay [TR-TEIAUDITOR-2026]. Practitioners at Vertex Exchange Europe 2026 said a rejected e-invoice can
    stop shipments and delay revenue recognition [INNOVATETAX-VERTEXEU-2026].
  solution: >
    Sovos announced on 24 Mar 2026 that its Sovi AI would offer "problem-to-resolution guidance": AI diagnoses root
    causes, proposes specific fixes and executes corrections once approved by users, and proactive issue detection
    before filing deadlines. The release says the capabilities are "available now or rolling out" and lists some as
    "current and planned" [SOVOS-SOVI-2026].
  outcomes:
    - lever: risk
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: SOVOS-SOVI-2026
  prerequisites:
    - Integration between the ERP, the tax platform and the authority or network interface [VERTEX-VIDA-2026]
    - Master data of a quality that makes errors diagnosable at source [INNOVATETAX-VERTEXEU-2026]
  risks_and_guardrails:
    - Sovos says every recommendation, approval and action is documented, and that customer data stays inside its security perimeter and is not used to train external models [SOVOS-SOVI-2026].
    - Clearance timing leaves little room for AI error: a wrong correction can repeat a rejection [TR-TEIAUDITOR-2026].
  human_checkpoints:
    - User approval before a correction is executed [SOVOS-SOVI-2026]
  role_evolution: >
    The tax technologist moves from raising support tickets to approving fixes, per the vendor release
    [SOVOS-SOVI-2026]. Vertex Exchange speakers said the future indirect tax team is "hybrid", with knowledge of
    legislation, systems, process design and data flows [INNOVATETAX-VERTEXEU-2026].
  evidence_grade: C
  sources:
    - {ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability", publisher: Sovos, type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: "2026-03-24", access: full, locator: "list 'Current and planned Sovi AI capabilities'"}
    - {ref: TR-TEIAUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "section 'End of the traditional model'"}
    - {ref: INNOVATETAX-VERTEXEU-2026, title: "What we learned from Vertex Exchange Europe 2026", publisher: Innovate Tax (conference recap by a business development manager), type: conference, url: "https://innovatetax.com/blog/what-we-learned-from-vertex-exchange-europe-2026/", date: "2026-05-06", access: full, locator: "sections 'VAT risk now surfaces at the invoice itself' and 'Partners and skills'"}
    - {ref: VERTEX-VIDA-2026, title: "ViDA and the Future of ERP Integration: How to Build for Continuous Transaction Controls", publisher: Vertex, type: vendor, url: "https://www.vertexinc.com/node/8169", date: "2026-04-17", access: full, locator: "'ERP integration becomes the real bottleneck'"}
  last_reviewed: 2026-10-17
  notes: >
    Sits on the boundary with indirect-tax (e-invoicing) and is listed here for the reporting-interface and ERP-data
    side. Sovos releases list a mix of available and planned capabilities, so the release alone does not show which
    were live on 24 Mar 2026. The Sovos page was modified on 2026-10-07 after its original publication date.

- id: tax-data-technology-08
  title: Exposing tax engines to enterprise agents through MCP and A2A interfaces
  archetype: tax
  module: tax-data-technology
  function: technology-it
  work_types: [software-systems]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >
    A company's own AI agents need to read rates, check exemption certificates or prepare returns held in the tax
    engine; custom integrations for each are costly. Avalara says tasks that needed several APIs and custom
    orchestration can become standardised tool calls [AVALARA-MCP-2026].
  solution: >
    The tax vendor runs an MCP server so any MCP-capable client can call its tools. Avalara's May 2026 developer
    primer says it ships a growing family of MCP servers covering tax calculation, returns, exemption certificates,
    registrations, classification and regulatory content, with OAuth 2.1 authorisation [AVALARA-MCP-2026]. Avalara
    NEXT on 26 Mar 2026 was a virtual developer and partner event on agent-based architectures, with partner sessions
    from Versori, Chargebee and Xero [AVALARA-NEXT-2026]. Sovos says it "is developing" a Sovos MCP Gateway to give
    agents governed access, with A2A orchestration "expected" to follow over time [SOVOS-SOVI-2026].
  outcomes:
    - lever: capacity
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: AVALARA-MCP-2026
  prerequisites:
    - An MCP-capable client or agent platform (the primer cites FastMCP as an example) [AVALARA-MCP-2026]
    - An identity and consent set-up for OAuth 2.1 [AVALARA-MCP-2026]
  risks_and_guardrails:
    - The primer's production checklist: rate-limit handling and retry logic, logging of every tool call with inputs and response status, least-privilege OAuth scopes with periodic consent audits, and idempotent handling for filings and transaction commits [AVALARA-MCP-2026].
    - Sovos describes governed access, with every recommendation, approval and action documented [SOVOS-SOVI-2026].
  human_checkpoints:
    - Not specified for MCP clients; Sovos says it plans guided, human-approved actions inside its platform [SOVOS-SOVI-2026]
  role_evolution: >
    Tax technologists and IT architects wire tax engines into agent platforms; the vendor audience for the primer is
    "developers, AI builders" and partners [AVALARA-MCP-2026].
  evidence_grade: C
  sources:
    - {ref: AVALARA-MCP-2026, title: "Inside Avalara MCP servers: A developer's primer for agentic tax and compliance", publisher: Avalara, type: vendor, url: "https://www.avalara.com/blog/en/north-america/2026/05/avalara-mcp-servers.html", date: "2026-05-27", access: full, locator: "key takeaways and the production-deployment checklist"}
    - {ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability", publisher: Sovos, type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: "2026-03-24", access: full, locator: "paragraph on the Sovos MCP Gateway"}
    - {ref: AVALARA-NEXT-2026, title: "Avalara NEXT: The future of agentic tax and compliance", publisher: Avalara, type: conference, url: "https://www.avalara.com/us/en/blog/avalara-next-2026-building-the-future-of-agentic-tax-and-compliance.html", date: "2026-03-04", access: full, locator: "'What the event will cover'"}
  last_reviewed: 2026-10-17
  notes: >
    Vendor-only evidence. No customer, in-house team or implementation partner was found describing production use
    of a tax MCP server, so the maturity is `announced`. The pattern is not in the list: a tool-serving interface
    that third-party agents call. Vertex was not found to describe an MCP server (one search, no primary source).
    The determination-engine side of this belongs to indirect-tax; this entry covers the interoperability and controls side.

- id: tax-data-technology-09
  title: Automatic audit trail for AI-assisted tax determinations, overrides and approvals
  archetype: tax
  module: tax-data-technology
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >
    Fonoa's 2026 survey found 57.4% of respondents would not be confident defending AI-assisted decisions to a tax
    authority, and that only about a third run formal human-in-the-loop review of AI output [FONOA-2026]. Thomson
    Reuters writes that documentation must exist at the moment it is generated and not be reconstructed later
    [TR-GOVERNANCE-2026].
  solution: >
    Record each determination, override and approval, with data lineage, as work happens. Fonoa's checklist asks
    whether a team can produce a documented audit trail for AI-assisted decisions that affected filings in the last
    12 months, and Fonoa markets an "Audit" product that assembles the determination, override and approval trail on
    demand [FONOA-2026]. Sovos says every recommendation, approval and action is documented for governance
    visibility [SOVOS-SOVI-2026]. Deloitte advises storing agentic corrections to source data back in the system of
    record [DELOITTE-TTT-2026]. TR's governance article describes a major European manufacturer, unnamed, that in 2023
    received a seven-figure penalty because it could not show how it reached the right answer, not because the
    return was wrong [TR-GOVERNANCE-2026].
  outcomes:
    - lever: risk
      description: Confidence gap that an audit trail is meant to close. No result from using one was published.
      figure: "57.4%"
      measures: "survey respondents who would not be confident that AI-assisted decisions would hold up if challenged by a tax authority (Fonoa State of Indirect Tax in the AI Era 2026, 176 indirect tax leaders)"
      provenance: vendor-published
      source_ref: FONOA-2026
    - lever: speed
      description: Fonoa describes its audit view as audit ready "in minutes, not weeks". Vendor claim, no sample.
      figure: "minutes, not weeks"
      measures: "time to assemble the determination, override and approval trail on demand, as stated by Fonoa"
      provenance: vendor-published
      source_ref: FONOA-2026
  prerequisites:
    - Defined process behind the output; Fonoa says this was the strongest predictor of audit confidence in its data [FONOA-2026]
    - Logging at the tool or workflow layer (see tax-data-technology-08)
  risks_and_guardrails:
    - Fonoa's BDO interviewee says the defence is demonstrating a process, not defending a technology [FONOA-2026].
    - In the TR recap of the April 2026 seminar, a panelist described hearing of companies that pad their numbers with a safety margin and treat the eventual audit as the cheaper cost; the panel's response was a flat "Do not do this" [TR-TEIAUDITOR-2026].
  human_checkpoints:
    - Formal human-in-the-loop review of AI output before it informs a tax decision [FONOA-2026]
  role_evolution: >
    Named ownership of each compliance decision and documented sign-off, as TR describes the governance framework
    [TR-GOVERNANCE-2026].
  evidence_grade: C
  sources:
    - {ref: FONOA-2026, title: "State of Indirect Tax in the AI Era 2026", publisher: Fonoa, type: survey, url: "https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026", date: "2026-06-17", access: full, locator: "sections on confidence, governance, diagnostic checklist and 'How Fonoa Intelligence helps'"}
    - {ref: TR-GOVERNANCE-2026, title: "The governance reckoning: How tax departments must prepare for the new era of mandatory compliance", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/tax-departments-mandatory-compliance", date: "2026-06-02", access: full, locator: "opening anecdote; 'The real-time reporting challenge'"}
    - {ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability", publisher: Sovos, type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: "2026-03-24", access: full, locator: "'Full Audit Transparency'"}
    - {ref: DELOITTE-TTT-2026, title: "Tax Transformation Trends, AI-enabled Tax Transformation, Part three: Riding the wave: A framework to plan for AI", publisher: Deloitte Global, type: firm, url: "https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf", date: "2026-07", access: full, locator: "p.5 (Scenario 2)"}
    - {ref: TR-TEIAUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "section 'Two ways to lose'"}
  last_reviewed: 2026-10-17
  notes: >
    Survey sample is indirect-tax leaders (adjacent process), so this entry is capped at B; it is C because the
    audit-trail product claims are the vendor's. The anecdote about a seven-figure penalty is unattributed ("a major
    European manufacturer", 2023) in the TR article and could not be checked. The pattern here is a trail that records
    other agents' work.

- id: tax-data-technology-10
  title: Continuous compliance monitoring and proactive issue detection ahead of filing deadlines
  archetype: tax
  module: tax-data-technology
  function: risk-compliance-legal
  work_types: [review-assurance, coordination-scheduling]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >
    Batch filing cycles surface errors late. TR's governance article says teams that once had 12 to 18 months to
    reconstruct audit documentation now need it accurate when generated [TR-GOVERNANCE-2026].
  solution: >
    EY's author describes "continuous audit and always-on monitoring", where agents analyse compliance metrics
    continuously and trigger alerts or remediations before deadlines, and agents that monitor rule changes, propose
    adjustments and route exceptions [BTAX-EYGRIP-2025]. Sovos announced "proactive issue detection" that surfaces
    compliance problems before filing deadlines, and regulatory intelligence that assesses how rule changes affect
    each customer's configuration [SOVOS-SOVI-2026].
  outcomes:
    - lever: risk
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: BTAX-EYGRIP-2025
  prerequisites:
    - Data feeds into the monitoring layer (see tax-data-technology-01)
    - A compliance calendar with named owners [TR-GOVERNANCE-2026]
  risks_and_guardrails:
    - EY's author says sophistication raises the bar for integration, data lineage traceability and human judgment [BTAX-EYGRIP-2025].
  human_checkpoints:
    - Exceptions routed for review; people ask questions and review outcomes [BTAX-EYGRIP-2025]
  role_evolution: >
    EY's author describes tax moving from people executing technology-powered processes to technology executing
    processes that are managed by people asking questions and reviewing outcomes [BTAX-EYGRIP-2025].
  evidence_grade: C
  sources:
    - {ref: BTAX-EYGRIP-2025, title: "AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way", publisher: "Bloomberg Tax (EY-authored commentary; author shown as EY, views are the author's)", type: press, url: "https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way", date: "2025-11-21", access: full, locator: "opening paragraphs and 'Enterprise Tax Functions' list"}
    - {ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability", publisher: Sovos, type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: "2026-03-24", access: full, locator: "'Proactive Issue Detection' and 'Regulatory Intelligence'"}
    - {ref: TR-GOVERNANCE-2026, title: "The governance reckoning: How tax departments must prepare for the new era of mandatory compliance", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/tax-departments-mandatory-compliance", date: "2026-06-02", access: full, locator: "'The real-time reporting challenge'"}
  last_reviewed: 2026-10-17
  notes: >
    Both sources describe aims and announced features; the EY text says its platform "aims to" evolve tax this way.
    No customer example was found.

- id: tax-data-technology-11
  title: Continuous three-way reconciliation of calculated, invoiced and reported tax data
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [data-reporting, review-assurance]
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >
    Indirect tax teams "need to be able to show that what was calculated is exactly what was invoiced, and that what
    was invoiced is exactly what was reported to the authorities" [INNOVATETAX-VERTEXEU-2026]. Authorities in mature
    continuous-transaction-control jurisdictions are described as arriving at audits having already analysed the
    data; one panelist called it "a shift from us preparing returns to us answering notices" [TR-TEIAUDITOR-2026].
  solution: >
    Idea discussed by practitioners: reconcile every transaction across the three points continuously, an evolution
    from continuous transaction controls to "continuous audit controls" discussed at Vertex Exchange Europe 2026
    [INNOVATETAX-VERTEXEU-2026]. Deloitte's scenario 3 says detective controls and reactive issue management become
    unsustainable when authorities run real-time analytics [DELOITTE-TTT-2026].
  outcomes:
    - lever: risk
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: INNOVATETAX-VERTEXEU-2026
  prerequisites:
    - Transaction-level data from the ERP, the e-invoicing platform and the authority response [VERTEX-VIDA-2026]
  risks_and_guardrails:
    - Vertex-affiliated commentary warns that CTCs implemented in isolation amplify misaligned data models and brittle integrations [VERTEX-VIDA-2026].
  human_checkpoints:
    - Not described in the sources
  role_evolution: >
    Not described in the sources; the Vertex recap says readiness is not only whether a team can submit an invoice
    in the right format [INNOVATETAX-VERTEXEU-2026].
  evidence_grade: D
  sources:
    - {ref: INNOVATETAX-VERTEXEU-2026, title: "What we learned from Vertex Exchange Europe 2026", publisher: Innovate Tax (conference recap by a business development manager), type: conference, url: "https://innovatetax.com/blog/what-we-learned-from-vertex-exchange-europe-2026/", date: "2026-05-06", access: full, locator: "'VAT risk now surfaces at the invoice itself' and 'From CTC to Continuous Audit Controls'"}
    - {ref: TR-TEIAUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "section 'Outgunned'"}
    - {ref: DELOITTE-TTT-2026, title: "Tax Transformation Trends, AI-enabled Tax Transformation, Part three: Riding the wave: A framework to plan for AI", publisher: Deloitte Global, type: firm, url: "https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf", date: "2026-07", access: full, locator: "p.6 (Scenario 3)"}
    - {ref: VERTEX-VIDA-2026, title: "ViDA and the Future of ERP Integration: How to Build for Continuous Transaction Controls", publisher: Vertex, type: vendor, url: "https://www.vertexinc.com/node/8169", date: "2026-04-17", access: full, locator: "'Continuous transaction controls as an operating model'"}
  last_reviewed: 2026-10-17
  notes: >
    Idea. The "continuous audit controls" discussion is reported in a recap; the sessions themselves were not seen.
    No source says AI performs the reconciliation; the AI link is the full-population approach, so `automate` is the
    ladder for the idea as described, not for any reported deployment.

- id: tax-data-technology-12
  title: AI-driven preventive controls upstream, at the point where tax data is created
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [review-assurance, software-systems]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: >
    Deloitte's scenario 3 says that when authorities expect upstream data quality and integration, reliance on
    detective controls and reactive issue management becomes unsustainable, because identifying and correcting errors
    after submission is no longer sufficient [DELOITTE-TTT-2026].
  solution: >
    Idea discussed by practitioners: put "proactive, AI-driven preventive controls" upstream in business processes,
    so tax requirements are embedded in the process that creates the data [DELOITTE-TTT-2026]. TR's governance
    article makes the non-AI version of the same point: influence how data is captured at source, build direct
    feeds, set reconciliation checkpoints and keep data lineage so any figure can be traced [TR-GOVERNANCE-2026].
  outcomes:
    - lever: quality
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: DELOITTE-TTT-2026
  prerequisites:
    - Tax part of ERP and new-business-line design [TR-GOVERNANCE-2026]
    - Stronger links between the tax, finance and operations functions [DELOITTE-TTT-2026]
  risks_and_guardrails:
    - Funding is linked to compliance and business continuity in the Deloitte scenario, so the case has to be made outside tax [DELOITTE-TTT-2026].
  human_checkpoints:
    - Not described in the sources
  role_evolution: >
    Deloitte says the talent model in scenario 3 would shift toward data analytics, technology integration and
    project management skills [DELOITTE-TTT-2026].
  evidence_grade: D
  sources:
    - {ref: DELOITTE-TTT-2026, title: "Tax Transformation Trends, AI-enabled Tax Transformation, Part three: Riding the wave: A framework to plan for AI", publisher: Deloitte Global, type: firm, url: "https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf", date: "2026-07", access: full, locator: "p.6 (Scenario 3: Uneven progression)"}
    - {ref: TR-GOVERNANCE-2026, title: "The governance reckoning: How tax departments must prepare for the new era of mandatory compliance", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/tax-departments-mandatory-compliance", date: "2026-06-02", access: full, locator: "'3 actions tax departments must take now', actions 2 and 3"}
  last_reviewed: 2026-10-17
  notes: >
    Idea from a firm's scenario framework; no named organisation reports building it. Scenario 3 is described as the
    case where a company's AI adoption lags its authority's.

- id: tax-data-technology-13
  title: Multi-agent workflows spanning provision, return and credit data, with people handling exceptions
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [transaction-processing, data-reporting]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: >
    The TEI-SJSU panel deck says that without an orchestration layer, AI cannot move from demo to production, and
    that fragmented data and the lack of an agent platform leave tools isolated with no repeatable workflows
    [SJSU-TEIHTTI-2025].
  solution: >
    The panel deck (RSM, Grant Thornton, EY and OpenAI speakers, 3 Nov 2025) places "multi-agent tax workflows" at
    the top of a four-step progression (one-shot prompting, built-in agent features, generative AI plus coding,
    multi-agent workflows). It lists provision-to-return automation, R&D credit eligibility scanning, fixed asset
    depreciation with audit trail generation and state apportionment data ingestion as examples, with humans
    reserved for exceptions, and says this is where the "most forward-leaning" tax teams are headed
    [SJSU-TEIHTTI-2025]. TEI's Nov 2025 programme included "AI Agents in the Tax Function: Implications for Tax
    Executives" [TEI-TECHTAX-2025]. The TR recap says attendees run agentic systems against historical filings
    [TR-TEIAUDITOR-2026].
  outcomes:
    - lever: speed
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: SJSU-TEIHTTI-2025
  prerequisites:
    - An orchestration and agent platform; the deck lists "no agent platform" and fragmented data as infrastructure gaps [SJSU-TEIHTTI-2025]
    - Documented processes; the deck says AI cannot automate what is not explicit [SJSU-TEIHTTI-2025]
  risks_and_guardrails:
    - The deck says the approach keeps workflows auditable and supports SOX-style documented, repeatable processes. That is the presenters' claim and no control test was shown [SJSU-TEIHTTI-2025].
    - Review burden: attendees at the April 2026 seminar worried about reviewing a growing volume of work when errors are "polite, quiet, and technical" [TEI-TAXTECH-2026].
  human_checkpoints:
    - Human involvement reserved for exception handling [SJSU-TEIHTTI-2025]
  role_evolution: >
    Per the deck, tax professionals move from tactical work to judgment and planning, and lean teams cover more
    jurisdictions and scenarios [SJSU-TEIHTTI-2025].
  evidence_grade: D
  sources:
    - {ref: SJSU-TEIHTTI-2025, title: "AI and Other Emerging Technologies for Tax Practitioners (41st Annual TEI-SJSU High Tech Tax Institute panel deck)", publisher: "TEI and San Jose State University", type: conference, url: "https://www2.sjsu.edu/taxinstitute/docs/4D_AI.pdf", date: "2025-11-03", access: full, locator: "section 1, item 4 ('Multi-Agent Tax Workflows') and 'Why This Matters'"}
    - {ref: TEI-TECHTAX-2025, title: "2025 TechTAXcelerate: Unleashing the Future of Tax Technology (Webinar Series)", publisher: Tax Executives Institute, type: conference, url: "https://www.tei.org/events-education/events/2025-techtaxcelerate-unleashing-future-tax-technology-webinar-series", date: "2025-11-17", access: full, locator: "agenda, Thursday 20 Nov 12:00 session"}
    - {ref: TR-TEIAUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "paragraph after the tooling poll"}
    - {ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: "2026-05-04", access: full, locator: "section 'A very bad wizard'"}
  last_reviewed: 2026-10-17
  notes: >
    Idea, as presenters discuss it. The OpenAI tax department showed live automation pipelines at the April 2026
    seminar [TEI-TAXTECH-2026], and its slides show agent demos labelled "time saved" and "time to result" (a research
    memo agent: 3 hours saved, 2 minutes to result; a Slack Q&A agent: 15 minutes saved, under 1 minute to result;
    a daily digest: 30 minutes saved, under 1 minute). These are demonstration timings from the presenter and are not used as outcomes; the research and Q&A agents are routed to
    research-advisory. The deck says R&D credit workflow automation was shown but does not state whether any of it
    is in production at OpenAI.

- id: tax-data-technology-14
  title: Centralised tax operations centre and tax technology team as the operating model
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [coordination-scheduling, software-systems]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    In the TEI seminar poll of more than 50 attendees, two said the tax function owns AI implementation at their
    company [TEI-TAXTECH-2026]. In the 2026 TRI/TEI technology report, 64% placed their tax department at the chaotic
    or reactive end of a maturity curve (57% the year before), and 22% track no technology performance metrics
    [TR-REBRAND-2026].
  solution: >
    Set up a central team that owns tax technology, data and automation, often with a hub for standard processes.
    Unilever Ice Cream's global head of tax, treasury and insurance, Anna Elphick, described in a CIOT DITT Talk
    episode (3 Aug 2025) the company's tax transformation, including setting up a centralised tax operations centre
    to drive efficiency, accuracy and control across jurisdictions [CIOT-DITT-2025]. In the TRI/TEI report, 88% of
    departments now have a designated person leading tax technology strategy, up from 51% a year earlier
    [TR-REBRAND-2026]. A German head of tax interviewed by EY said his company has a dedicated AI team helping tax with
    compliance and reporting [BTAX-EYTFO-2026]. In KPMG Germany's quick survey, 40% expect more use of shared service
    centres [KPMG-DE-2026].
  outcomes:
    - lever: capacity
      description: No result for the Unilever centre was described in the episode listing.
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: CIOT-DITT-2025
    - lever: experience
      description: Designated leadership for tax technology strategy, as context. The report does not link it to a result.
      figure: "88% (from 51%)"
      measures: "corporate tax departments with a designated person leading tax technology strategy (2026 Corporate Tax Department Technology Report; 170 tax leaders; share a year earlier in brackets)"
      provenance: vendor-published
      source_ref: TR-REBRAND-2026
  prerequisites:
    - Executive sponsorship; TR says a technology lead title only works when the team believes it belongs at the decision-making table [TR-REBRAND-2026]
    - A business case built on hard ROI and cost savings, the metrics TR says matter most to finance and IT [TR-REBRAND-2026]
    - Persona-based training; one organisation in a TR roundtable developed over two dozen user personas [TR-SAP-2025]
  risks_and_guardrails:
    - A transformation director at the April 2026 seminar described a training programme across dozens of global clients that failed; a tool meant to save two hours cost a day because users had not been consulted [TEI-TAXTECH-2026].
    - Key-person risk: workflows nobody could explain after the builder left [TEI-TAXTECH-2026].
  human_checkpoints:
    - Governance framework with named owners, documented sign-off and internal reviews against a compliance calendar [TR-GOVERNANCE-2026]
  role_evolution: >
    PwC Ireland expects new roles to emerge, formally or not: tax data leads, model governance leads, and people who
    bridge tax requirements and technical delivery [PWC-IE-2026]. In EY's survey, 89% are upskilling existing staff, 81%
    are hiring people with skills other than tax technical capability and 62% are redefining roles, including teams
    dedicated to high-value activities [BTAX-EYTFO-2026]. KPMG Germany: 58% of respondents expect domestic tax
    headcount to stay constant, 72% abroad [KPMG-DE-2026].
  evidence_grade: B
  sources:
    - {ref: CIOT-DITT-2025, title: "DITT Talk: Tax Technology (episode 'Tax Transformation at Scale', 3 Aug 2025; series listing)", publisher: "Chartered Institute of Taxation (CIOT) podcast; listing via Wave", type: podcast, url: "https://pod.wave.co/podcast/ditt-talk-tax-technology", date: "2025-08-03", access: full, locator: "episode description (audio and transcript not reached)"}
    - {ref: TR-REBRAND-2026, title: "You are not a cost center: Why tax departments need to rebrand themselves", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/tax-departments-rebrand", date: "2026-05-05", access: full, locator: "sections 'The choices we keep making' and 'The rebrand starts with how departments see themselves'"}
    - {ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: "2026-05-04", access: full, locator: "section 'A very bad wizard'"}
    - {ref: BTAX-EYTFO-2026, title: "AI Era Requires Continuous Tax and Finance Transformation", publisher: "Bloomberg Tax Daily Tax Report (author byline not shown in the text read; draws on the EY survey)", type: press, url: "https://news.bloomberglaw.com/daily-tax-report/ai-era-requires-continuous-tax-and-finance-transformation", date: "2026-02-09", access: full, locator: "'Agentic AI: Promise and Practicalities' and 'Trust in Your People'"}
    - {ref: PWC-IE-2026, title: "Evolving the tax function with AI: Four key insights to guide tax leaders", publisher: PwC Ireland, type: firm, url: "https://www.pwc.ie/services/tax/insights/evolving-the-tax-function-with-ai.html", date: "2026-07-21", access: full, locator: "insight 4 (a new operating model takes shape)"}
    - {ref: KPMG-DE-2026, title: "Tax departments are increasingly turning to artificial intelligence", publisher: KPMG Germany, type: survey, url: "https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html", date: "2026-05-07", access: full, locator: "key findings and 'AI boosts efficiency...' paragraphs"}
    - {ref: TR-SAP-2025, title: "How leaders automate tax compliance in SAP S/4HANA", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/how-tax-leaders-automate-compliance-in-sap-s-4hana/", date: "2025-12-02", access: full, locator: "strategy 'Tailor training by persona'"}
    - {ref: TR-GOVERNANCE-2026, title: "The governance reckoning: How tax departments must prepare for the new era of mandatory compliance", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/tax-departments-mandatory-compliance", date: "2026-06-02", access: full, locator: "action 1 (formal governance framework)"}
  last_reviewed: 2026-10-17
  notes: >
    Graded B on one named deployment (Unilever Ice Cream's tax operations centre, from a podcast description; no
    measurements published; the description does not say how much of it is AI). The survey figures are context for
    the operating-model shift and not outcomes of a specific change. The TRI/TEI report itself was not opened; its
    figures come from TR's own article about it. The Unilever business unit name is as given in the episode listing.

- id: tax-data-technology-15
  title: Co-sourced or managed tax operations running on a provider's AI and data platforms
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [transaction-processing, data-reporting]
  pattern: other
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: >
    In-house teams say they struggle to build their own solutions. A head of finance at a global e-commerce and cloud
    company told EY that internal builds would often have been better done with an external provider
    [BTAX-EYTFO-2026]. Deloitte's scenario 2 says patchy authority readiness leaves tax needing people for both
    tech-enabled and legacy processes [DELOITTE-TTT-2026].
  solution: >
    Use a third party that invests in AI and data tooling, or a managed service for jurisdictions where authorities
    cannot interact in real time. In EY's survey, 78% said working with a third-party provider with deep AI
    capabilities would moderately or significantly benefit their tax function, and 85% said growing co-sourcing has
    improved their ability to focus on high-value activities [BTAX-EYTFO-2026]. Deloitte lists "a managed service or
    selective outsourcing with specialist resources" as an option [DELOITTE-TTT-2026]. Vertex Exchange speakers said
    most large implementations are now partner-led [INNOVATETAX-VERTEXEU-2026].
  outcomes:
    - lever: capacity
      description: Share of respondents reporting better focus on high-value work from co-sourcing.
      figure: "85%"
      measures: "respondents reporting improved ability to focus on high-value activities as use of co-sourcing grows (EY Tax and Finance Operations Survey, as written up by Bloomberg Tax; base not stated)"
      provenance: vendor-published
      source_ref: BTAX-EYTFO-2026
  prerequisites:
    - Data access and security terms that allow a provider into ERP and tax data
  risks_and_guardrails:
    - EY sells these services; the survey and the write-up are from a provider with an interest in the result [BTAX-EYTFO-2026].
    - Accountability stays with the tax function: Deloitte says the function is responsible to stand behind outcomes that are accurate, compliant and defensible [DELOITTE-TTT-2026].
  human_checkpoints:
    - In-house review of provider output; the EY write-up says the business should apply critical human review [BTAX-EYTFO-2026]
  role_evolution: >
    Internal teams focus on advisory work and oversight, per the EY write-up [BTAX-EYTFO-2026]. Deloitte's scenario 4
    splits planning between largely automated tax operations and tax advisory [DELOITTE-TTT-2026].
  evidence_grade: C
  sources:
    - {ref: BTAX-EYTFO-2026, title: "AI Era Requires Continuous Tax and Finance Transformation", publisher: "Bloomberg Tax Daily Tax Report (author byline not shown in the text read; draws on the EY survey)", type: press, url: "https://news.bloomberglaw.com/daily-tax-report/ai-era-requires-continuous-tax-and-finance-transformation", date: "2026-02-09", access: full, locator: "'Agentic AI: Promise and Practicalities' (interviews) and 'Trust in Your People'"}
    - {ref: DELOITTE-TTT-2026, title: "Tax Transformation Trends, AI-enabled Tax Transformation, Part three: Riding the wave: A framework to plan for AI", publisher: Deloitte Global, type: firm, url: "https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf", date: "2026-07", access: full, locator: "p.5 (Scenario 2) and p.7 (Scenario 4)"}
    - {ref: INNOVATETAX-VERTEXEU-2026, title: "What we learned from Vertex Exchange Europe 2026", publisher: Innovate Tax (conference recap by a business development manager), type: conference, url: "https://innovatetax.com/blog/what-we-learned-from-vertex-exchange-europe-2026/", date: "2026-05-06", access: full, locator: "section 'Partners and skills are now central to success'"}
  last_reviewed: 2026-10-17
  notes: >
    The sources are provider commentary and a provider-run survey. No named in-house team reported a result. Co-sourcing
    in general predates AI; the AI-specific part is the provider's tooling.

- id: tax-data-technology-16
  title: Building tax data requirements and engine integration into an ERP migration
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [software-systems, data-reporting]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    Tax determination is often overlooked until late in an ERP project, which leads to delays and manual workarounds;
    one roundtable participant described managing tax across 40 separate billing systems, each with its own logic and
    exemption rules [TR-SAP-2025]. Vertex's white paper says leaving tax out of early scoping creates urgent work after
    go-live, and that a shortage of tax staff can mean no tax manager is on the project team [VERTEX-S4-2026].
  solution: >
    Put a tax expert on the migration team, clean the data before it moves, and integrate the tax engine natively with
    standard data flows and APIs, so that real-time reporting and e-invoicing needs are met [VERTEX-S4-2026]
    [TR-SAP-2025]. At Vertex Exchange Europe 2026, Siemens Energy and Daimler Truck AG described what worked, what was
    hard and what they would do again when implementing Vertex Tax Engine in SAP; the recap says success depended on
    preparation, data quality, internal alignment and change management [INNOVATETAX-VERTEXEU-2026]. Roundtable
    participants also said they used AI for contract review, anomaly detection and dashboard generation, and warned that
    AI success depends on clean, structured data and strong governance [TR-SAP-2025].
  outcomes:
    - lever: risk
      description: Context for the problem, not a result. Share of organisations that have completed the migration.
      figure: "less than 8%"
      measures: "organisations that have completed the SAP S/4HANA migration (DMA-SAP-Vertex online survey, as cited in the Vertex white paper; sample not stated)"
      provenance: vendor-published
      source_ref: VERTEX-S4-2026
  prerequisites:
    - Tax representation in project scoping [VERTEX-S4-2026]
    - Data cleansing, including a look at custom code in the old ERP [VERTEX-S4-2026]
  risks_and_guardrails:
    - A "lift and shift" gives short shrift to data quality and devalues the investment [VERTEX-S4-2026].
    - Sources are tax-engine vendors or their partners and each has a product to sell [VERTEX-S4-2026] [TR-SAP-2025].
  human_checkpoints:
    - Tax expert, internal or external, on the project team [VERTEX-S4-2026]
  role_evolution: >
    Tax staff take part in ERP implementations and set data requirements for new business lines before launch
    [TR-GOVERNANCE-2026]. Vertex Exchange speakers described the future team as hybrid, comfortable with ERP landscapes,
    data, automation and AI [INNOVATETAX-VERTEXEU-2026].
  evidence_grade: B
  sources:
    - {ref: INNOVATETAX-VERTEXEU-2026, title: "What we learned from Vertex Exchange Europe 2026", publisher: Innovate Tax (conference recap by a business development manager), type: conference, url: "https://innovatetax.com/blog/what-we-learned-from-vertex-exchange-europe-2026/", date: "2026-05-06", access: full, locator: "section 'Customer stories brought the challenges to life'"}
    - {ref: VERTEX-S4-2026, title: "New Perspectives on SAP S/4HANA Migration (white paper with DMA)", publisher: Vertex, type: vendor, url: "https://www.vertexinc.com/sites/default/files/2026-03/202603-white-paper-new-perspectives-on-sap-s-4hana-migration-dma.pdf", date: "2026-03", access: full, locator: "pp.2-4 (date from file path and PDF metadata, created 2026-03-18)"}
    - {ref: TR-SAP-2025, title: "How leaders automate tax compliance in SAP S/4HANA", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/how-tax-leaders-automate-compliance-in-sap-s-4hana/", date: "2025-12-02", access: full, locator: "'Why tax automation is essential' and 'Key insights from the SAP S/4HANA tax roundtable'"}
    - {ref: TR-GOVERNANCE-2026, title: "The governance reckoning: How tax departments must prepare for the new era of mandatory compliance", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/tax-departments-mandatory-compliance", date: "2026-06-02", access: full, locator: "action 2 (fixing the data access problem)"}
  last_reviewed: 2026-10-17
  notes: >
    Graded B on two named customers (Siemens Energy, Daimler Truck AG) discussing their implementations, as reported in
    a third-party recap of a vendor-run conference. No measurements were published. AI is not the subject of the
    named-customer talks; it is included because practitioners cite ERP data flows as the prerequisite for tax AI. The
    tax-engine determination logic belongs to indirect-tax, so this entry is capped at B. The SAPinsider statistic in
    the white paper (59% fully or partially live on S/4HANA) is not used.

- id: tax-data-technology-17
  title: Scenario modelling of effective tax rate, deferred tax and policy changes on governed data
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [data-reporting, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: >
    CEOs expect tax and finance to go beyond compliance and bring insight into strategy; in EY's survey 79% name this
    a top priority for the next two years, yet teams spend most of their time on routine work and data wrangling
    [BTAX-EYTFO-2026]. In the 2025 TR survey, 56% of respondents who spend more than half their time on reactive work
    said their departments incurred penalties, against 31% of those who spend more than half on proactive work
    [TR-CORPTAX-2025].
  solution: >
    With a sound data foundation, use AI to simulate changing interest rates, trade and tariff policy and supply chain
    changes, and to improve forecasts of effective tax rates and deferred tax balances [PWC-IE-2026]. In EY's
    survey, leaders expect AI to free up 23% more budget for strategic activities [EY-TFO-2025]. In the same survey only 27%
    expected AI to be useful for things like modelling legislation and delivering insights [BTAX-EYTFO-2026].
  outcomes:
    - lever: capacity
      description: Expectation, not a result.
      figure: "23%"
      measures: "more budget that leaders expect AI to free up for strategic, high-value activities (EY Tax and Finance Operations Survey; stated as an expectation)"
      provenance: vendor-published
      source_ref: EY-TFO-2025
  prerequisites:
    - A governed data foundation (see tax-data-technology-01) [PWC-IE-2026]
  risks_and_guardrails:
    - PwC Ireland says broad experimentation rarely produces meaningful outcomes and advises a small number of high-value use cases [PWC-IE-2026].
    - The TR penalty comparison is an association from a survey and does not show that proactive work prevents penalties [TR-CORPTAX-2025].
  human_checkpoints:
    - Tax professionals challenge outputs and refine conclusions [PWC-IE-2026]
  role_evolution: >
    PwC Ireland: "AI raises the floor, tax professionals raise the ceiling"; value goes to people who combine tax
    expertise with commercial understanding and data confidence [PWC-IE-2026].
  evidence_grade: C
  sources:
    - {ref: PWC-IE-2026, title: "Evolving the tax function with AI: Four key insights to guide tax leaders", publisher: PwC Ireland, type: firm, url: "https://www.pwc.ie/services/tax/insights/evolving-the-tax-function-with-ai.html", date: "2026-07-21", access: full, locator: "insight 2 (forecasting becomes a core tax contribution) and insight 3"}
    - {ref: EY-TFO-2025, title: "EY report indicates CFOs and tax leaders innovating with AI to manage mounting geopolitical turbulence, talent shortages and regulatory developments", publisher: EY, type: survey, url: "https://ey.com/en_gl/newsroom/2025/11/ey-report-indicates-cfos-and-tax-leaders-innovating-with-ai-to-manage-mounting-geopolitical-turbulence-talent-shortages-and-regulatory-developments", date: "2025-11-18", access: full, locator: "highlights and section 'The AI and data imperative'"}
    - {ref: BTAX-EYTFO-2026, title: "AI Era Requires Continuous Tax and Finance Transformation", publisher: "Bloomberg Tax Daily Tax Report (author byline not shown in the text read; draws on the EY survey)", type: press, url: "https://news.bloomberglaw.com/daily-tax-report/ai-era-requires-continuous-tax-and-finance-transformation", date: "2026-02-09", access: full, locator: "opening and 'Agentic AI: Promise and Practicalities'"}
    - {ref: TR-CORPTAX-2025, title: "Why most tax departments aren't using AI yet (State of the Corporate Tax Department 2025)", publisher: Thomson Reuters Tax & Accounting, type: survey, url: "https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/", date: "2025-10-22", access: full, locator: "'The confidence gap and resource connection' (288 tax departments)"}
  last_reviewed: 2026-10-17
  notes: >
    The sources are firm commentary and surveys; no named organisation reported a forecasting use. Provision-side
    forecasting belongs to the provision module. The "79%" figure is the share naming insight into broader business
    strategy a top priority in the next two years in the Bloomberg Tax write-up.
```

---

## 3. Module notes

**Processes and key steps (with work types)**
- Ledger and ERP data to tax engines: extract, map, validate, load into provision and compliance engines (`data-reporting`, `transaction-processing`) [TR-CORPAI-2026] [BTAX-EYGRIP-2025] [KOGNITOS-2026].
- Tax data platform: ingest from ERP and other sources, govern, keep lineage, serve reporting and agents (`software-systems`, `data-reporting`) [BTAX-EYTFO-2026] [DELOITTE-DATABRICKS-2025] [TR-SAP-2025].
- Build and sustain in-house automation (Alteryx, Power Platform, Python in Excel, AI-coded tools): build, document, test, monitor, hand over (`software-systems`) [TEI-TECHTAX-2025] [TEI-TAXTECH-2026] [TR-TEIAUDITOR-2026].
- Real-time reporting interface: master data, tax determination, invoice creation, clearance or submission, rejection handling, reconciliation (`transaction-processing`, `software-systems`) [VERTEX-VIDA-2026] [INNOVATETAX-VERTEXEU-2026] [TR-TEIAUDITOR-2026].
- Agent and tool interoperability: MCP servers, OAuth scopes, call logging, idempotent filings (`software-systems`) [AVALARA-MCP-2026] [SOVOS-SOVI-2026].
- ERP migration with tax in the project team (`software-systems`, `coordination-scheduling`) [VERTEX-S4-2026] [TR-SAP-2025].
- Tax technology operating model: designate a lead, set metrics, make the business case, train by persona, manage vendors and partners (`coordination-scheduling`) [TR-REBRAND-2026] [TR-SAP-2025].
- Governance and evidence: named owners, sign-off, audit trail, data lineage (`review-assurance`) [TR-GOVERNANCE-2026] [FONOA-2026].

**Common pain points**
- Tax is downstream of finance systems built without tax requirements; data arrives aggregated, reclassified or stripped of detail [TR-GOVERNANCE-2026].
- Data silos and spreadsheets: 91% in the EY survey (as written up by Bloomberg Tax) [BTAX-EYTFO-2026]; "fragmented data" is the number one blocker on the TEI-SJSU panel slide [SJSU-TEIHTTI-2025].
- Resourcing: 58% of corporate tax departments under-resourced (51% the year before); fewer than half got a budget increase in the latest report [TR-CORPTAX-2025] [TR-CORPTECH-2026].
- Ownership: two hands of more than 50 for "tax owns AI implementation" [TEI-TAXTECH-2026].
- Maintainability: undocumented Alteryx workflows; pipelines nobody reviewed [TEI-TAXTECH-2026] [TR-TEIAUDITOR-2026].
- Training rollouts that fail when users are not consulted [TEI-TAXTECH-2026].
- Rising token costs flagged as a threat to the economic case [TEI-TAXTECH-2026].
- IT approvals (47%), data protection (41%) and lack of AI knowledge (41%) are the biggest hurdles in KPMG Germany's quick survey [KPMG-DE-2026].
- Master data (customer data, tax registrations, exemption certificates, product classification) is where real-time reporting fails first [INNOVATETAX-VERTEXEU-2026].

**Metrics and benchmarks (all self-reported by respondents or vendor-published; none independent)**
- 67% of corporate tax departments not using GenAI; 57% of those implementing new technology plan to include it; 58% under-resourced; 288 departments [TR-CORPTAX-2025].
- 64% of 170 tax leaders place their department at the chaotic or reactive stage (57% the year before); 22% track no technology performance metrics; 88% have a designated tax technology lead (51% the year before); 67% say technology investment has enabled more proactive work; 7% say AI is already central to their workflow [TR-REBRAND-2026] [TR-CORPTECH-2026].
- KPMG Germany: 71% of tax departments use AI tools and 19% are preparing; 89% use company-wide standard tools and 29% specialised tax applications; 66% of users report noticeable time savings; sample size not stated [KPMG-DE-2026].
- EY (1,600 leaders, 30 jurisdictions): 80% see insufficient AI-ready data as a significant barrier; 75% in the earliest phases of GenAI; 39% moderately or fully prepared to deploy AI agents; 21% say it is significantly easy to build tax technology applications; 17% of tax functions "very effective" at managing data [BTAX-EYTFO-2026] [EY-TFO-2025].
- Fonoa (176 indirect tax leaders): 92% use AI in some form; 12.5% have specific targets or KPIs; 57.4% would not be confident defending AI-assisted decisions to an authority; about a third run formal human-in-the-loop review [FONOA-2026].
- KPMG Global Tax Readiness Dividend (2,084 leaders, 25 countries): top-quartile "tax readiness" organisations 4-6x more likely to outperform on innovation, resilience, workforce capability and enterprise value. Landing page only; the report and its definition of readiness were not opened [KPMG-READINESS-2026].
- Not found: error rates, override rates, parallel-run results, inspection outcomes, or independent measures for AI in tax data and operations.

**Guardrails and regulatory points**
- UK Senior Accounting Officer regime puts personal accountability on named senior executives for the adequacy of tax accounting arrangements; TR links it to the need for governance frameworks [TR-GOVERNANCE-2026].
- Real-time regimes: TR's recap says more than 60 jurisdictions have moved or are moving to continuous transaction controls, and the EU has a 2030 deadline for cross-border real-time digital reporting [TR-TEIAUDITOR-2026]. TR's governance article says ViDA would extend similar requirements across the EU "beginning in 2028" [TR-GOVERNANCE-2026]. The two TR articles give different dates and neither was checked against EU legislation here.
- OECD Forum on Tax Administration plenary (Nov 2025) agreed to move to pilots of real-time automated sharing of secure information [OECD-FTA-2025].
- MCP guidance from the vendor: least-privilege OAuth scopes with periodic consent audits, logging every tool call, idempotent filings [AVALARA-MCP-2026].
- Vendor security claims: Sovos says customer data stays inside its perimeter and is not used to train external models [SOVOS-SOVI-2026]. Not independently tested.
- Cross-cutting professional-conduct material (IRS OPR Alert 2026-19, UK PCRT, TPB) is covered in the landscape and not repeated here.

**Frontier signals (dated and sourced)**
- 2025-10-08: Deloitte Tax and Databricks announce an alliance for a unified tax data architecture [DELOITTE-DATABRICKS-2025].
- 2025-11-20: OECD tax administrations agree to move towards pilots of real-time automated information sharing [OECD-FTA-2025].
- 2026-03-24: Sovos says it is developing an MCP gateway and expects A2A orchestration over time [SOVOS-SOVI-2026]. 2026-05-27: Avalara publishes its MCP server primer for developers and partners [AVALARA-MCP-2026].
- 2026-04/05: TEI Tax Technology Seminar recaps say the capability question is settled for attendees and the open questions are silent failures, ownership, training and token cost [TEI-TAXTECH-2026]. The second recap says regulators have "pulled ahead", compressing multi-year roadmaps to 12-18 month cycles [TR-TEIAUDITOR-2026].
- 2026-05: TRI/TEI report: most respondents have shortened expected AI integration timelines to 1-2 years from 3-5 [TR-REBRAND-2026].
- 2026-07: Deloitte's four-scenario framework crosses a department's AI adoption with its authority's AI progress; says tax can be a stress test of enterprise AI governance [DELOITTE-TTT-2026].
- 2026-07: PwC Ireland expects "tax data lead" and "model governance lead" roles to emerge [PWC-IE-2026].
- 2026-05: Vertex Exchange Europe: discussion of moving from continuous transaction controls to "continuous audit controls" and possibly beyond invoices into wider transaction data [INNOVATETAX-VERTEXEU-2026].
- 2026-10: TEI Annual Conference (Nashville) opens on or around the date of this scan; no recaps exist yet.

**Workforce and role effects**
- Tax work "at the high end" described as as much a data science problem as an accounting one [TR-TEIAUDITOR-2026].
- New roles expected: tax data leads, model governance leads, people bridging tax and technical delivery [PWC-IE-2026]. Designated tax technology leads are now the norm in the TRI/TEI sample (88%) [TR-REBRAND-2026].
- EY survey: 89% upskilling, 81% hiring non-tax skills, 62% redefining roles [BTAX-EYTFO-2026].
- Headcount: 58% (domestic) and 72% (abroad) of KPMG Germany respondents expect constant tax headcount [KPMG-DE-2026]. A law professor argues AI will not shrink corporate tax teams much because corporate tax work is tax practice (engagement with authorities, auditors and executives), not form preparation, and AI cannot bear culpability [TAXPROF-SALA-2026]. This is an abstract of a paywalled Tax Notes State article; the full text was not read.
- EY's author warns of a divide between experienced staff who can spot AI errors and newer staff who may over-rely on output [BTAX-EYGRIP-2025].

**Objections and concerns practitioners raise**
- AI "fails quietly and even politely"; review capacity does not scale with output [TEI-TAXTECH-2026].
- Capability is not the problem; process, ownership and oversight are [TEI-TAXTECH-2026] [FONOA-2026].
- Vibe-coded tools nobody else has reviewed or can maintain; security of such tools [TR-TEIAUDITOR-2026].
- Regulators and authorities are faster and better equipped than the companies they audit [TR-TEIAUDITOR-2026]; surrender (padding numbers) is described as tempting and rejected [TR-TEIAUDITOR-2026].
- Probabilistic AI gives different results for the same inputs, while tax compliance relies on deterministic outputs [BTAX-EYTFO-2026].
- Vendor and provider sources dominate the discourse; the TEI recaps are vendor-owned, and EY, KPMG, Deloitte and PwC items are marketing for services [see section 6].
- AI cannot carry regulatory, ethical or financial culpability [TAXPROF-SALA-2026].
- "There's pressure to use AI, but no one really knows in what capacity" (a BDO partner quoted by Fonoa) [FONOA-2026].

**Interview probes for an advisor**
1. Who in your tax function owns the data pipelines and automations built in the last two years, and what happens when the builder leaves? Is there an inventory, a review step and a retirement rule?
2. Walk me through one number on a return, a provision or a real-time submission: can you trace it to its source system field today, and how long does that take?
3. When an e-invoice or filing is rejected, who sees it first, who owns the fix, and how many of the causes are master data?
4. What would your authority see about you before an audit that you cannot see yourself, and what are you doing to close that gap?
5. Where does tax sit in your ERP and data-platform roadmap, and what cost of agents and tokens have you budgeted against measured time saved?

---

## 4. Routed to other modules

| Item | Target module | Source |
|---|---|---|
| GloBE Information Return XML pipeline: country-specific XML variants (Luxembourg, France, Austria differ from OECD schema), business-rule validation as gatekeeper, rounding-tolerance rule 60026 later deactivated, late test environments, correction mechanics; KPMG reports that in some jurisdictions only 20% of GIRs were filed successfully before the initial deadline; more than 120 business rules; 19 second-wave jurisdictions join 37 | international-pillar-two | FGS-GIR-2026; BTAX-KPMGP2-2026; LUCANET-2025 |
| Orbitax XatBot upgrade and ONESOURCE Pillar Two data points (vendor description) | international-pillar-two | TR-CORPAI-2026 |
| Neo.Tax R&D credit data capture and Form 6765 Section G | compliance | TR-CORPAI-2026 |
| Indirect-tax determination, e-invoicing network scale and Greek/French mandates; Fonoa's 10-workflow adoption data; Oxford Nanopore sales-tax saving ("hundreds of thousands of dollars", reported in a recap) | indirect-tax | FONOA-2026; INNOVATETAX-VERTEXEU-2026; SOVOS-SOVI-2026 |
| Slack Q&A agent, daily digest and research memo agent shown by OpenAI's tax department | research-advisory | SJSU-TEIHTTI-2025 |
| Notice response drafting (EY description) | controversy | BTAX-EYGRIP-2025 |
| Tax authority AI and data: HMRC roadmap (90% digital interactions by 2030 from about 76%; AI use cases; FOI story about unauthorised AI use in R&D correspondence); OECD real-time sharing pilots; Singapore doing more with AI than major companies (panelist remark) | controversy (tax-authority AI context) | ICAS-HMRC-2025; OECD-FTA-2025; TR-TEIAUDITOR-2026 |
| Professional conduct and AI liability (CIOT DITT Talk episodes of 12 Jun 2026 on AI liability and HMRC sanctions, 3 Jul 2026 on junior roles; listing only) | cross-cutting governance | CIOT-DITT-2025 |
| Tax provision forecasting and data handoff from the close | provision | KOGNITOS-2026; PWC-IE-2026 |
| Transfer pricing master and local file maintenance (German head of tax interviewed by EY) | transfer-pricing | BTAX-EYTFO-2026 |

---

## 5. Sources

34 distinct documents, all opened (`full`). By type: vendor 9, conference 6 (including conference recaps), press 6, survey 6, firm 4, podcast 1, regulator 1, professional-body 1. No `community`, `academic`, `standard-setter` or `job-posting` source. Survey and press items marked "landing" were opened but the underlying report was gated or not opened.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| AVALARA-MCP-2026 | Inside Avalara MCP servers: A developer's primer for agentic tax and compliance | Avalara | vendor | https://www.avalara.com/blog/en/north-america/2026/05/avalara-mcp-servers.html | 2026-05-27 | full |
| AVALARA-NEXT-2026 | Avalara NEXT: The future of agentic tax and compliance (event announcement; event on 2026-03-26) | Avalara | conference | https://www.avalara.com/us/en/blog/avalara-next-2026-building-the-future-of-agentic-tax-and-compliance.html | 2026-03-04 | full |
| BTAX-EYGRIP-2025 | AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way | Bloomberg Tax (EY-authored commentary) | press | https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way | 2025-11-21 | full |
| BTAX-EYTFO-2026 | AI Era Requires Continuous Tax and Finance Transformation | Bloomberg Tax Daily Tax Report (draws on EY survey; byline not shown) | press | https://news.bloomberglaw.com/daily-tax-report/ai-era-requires-continuous-tax-and-finance-transformation | 2026-02-09 | full |
| BTAX-KPMGP2-2026 | Pillar Two's First Real Test Has Lessons for 2027 Filing Season (Conrad Turley and Tam Do, KPMG International) | Bloomberg Tax (author commentary) | press | https://news.bloombergtax.com/transfer-pricing/pillar-twos-first-real-test-has-lessons-for-2027-filing-season | 2026-08-21 | full |
| CIOT-DITT-2025 | DITT Talk: Tax Technology (series listing; 'Tax Transformation at Scale' dated 2025-08-03; later episodes 2026-06-12 and 2026-07-03) | Chartered Institute of Taxation, via Wave | podcast | https://pod.wave.co/podcast/ditt-talk-tax-technology | 2025-08-03 | full (descriptions only) |
| DELOITTE-DATABRICKS-2025 | Deloitte Extends Alliance with Databricks to Modernize Tax Data Management | Deloitte US | firm | https://www.deloitte.com/us/en/about/press-room/deloitte-extends-alliance-with-databricks-to-modernize-tax-data-management.html | 2025-10-08 | full |
| DELOITTE-TTT-2026 | Tax Transformation Trends: AI-enabled Tax Transformation, Part three: Riding the wave | Deloitte Global | firm | https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf | 2026-07 (PDF metadata) | full |
| EY-TFO-2025 | EY report indicates CFOs and tax leaders innovating with AI... (Tax and Finance Operations Survey press release) | EY | survey | https://ey.com/en_gl/newsroom/2025/11/ey-report-indicates-cfos-and-tax-leaders-innovating-with-ai-to-manage-mounting-geopolitical-turbulence-talent-shortages-and-regulatory-developments | 2025-11-18 | full |
| FGS-GIR-2026 | XML statt Steuerrecht: Die wahren Herausforderungen der ersten Pillar-2-Saison (in German) | Flick Gocke Schaumburg | firm | https://www.fgs.de/news-and-insights/blog/detail/xml-statt-steuerrecht-die-wahren-herausforderungen-der-ersten-pillar-2-saison | 2026-08-03 | full |
| FONOA-2026 | State of Indirect Tax in the AI Era 2026 (landing page; report gated) | Fonoa | survey | https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026 | 2026-06-17 | full |
| ICAS-HMRC-2025 | HMRC's plans for AI (Susan Cattell) | ICAS | professional-body | https://www.icas.com/news-insights-events/news/tax/hmrc-s-plans-for-ai | 2025-10-29 | full |
| INNOVATETAX-VERTEXEU-2026 | What we learned from Vertex Exchange Europe 2026 | Innovate Tax | conference | https://innovatetax.com/blog/what-we-learned-from-vertex-exchange-europe-2026/ | 2026-05-06 | full |
| KOGNITOS-2026 | AI for Corporate Tax and Provision Automation (2026) | Kognitos | vendor | https://www.kognitos.com/blog/ai-corporate-tax-provision-automation-2026/ | 2026-06-17 | full |
| KPMG-DE-2026 | Tax departments are increasingly turning to artificial intelligence | KPMG Germany | survey | https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html | 2026-05-07 | full |
| KPMG-READINESS-2026 | 2026 KPMG Global Tax Readiness Dividend (landing page; report gated) | KPMG International | survey | https://kpmg.com/xx/en/our-insights/transformation/global-tax-readiness-dividend.html | 2026-06-22 | full |
| LUCANET-2025 | Pillar Two and XML: The Digital Backbone of GloBE Reporting | Lucanet | vendor | https://www.lucanet.com/en/insights/regulatory-insights/pillar-two-and-xml-digital-backbone-globe-reporting-05-12-2025/ | 2025-12-05 | full |
| OECD-FTA-2025 | Heads of tax administrations agree further work on collaborative projects... (18th FTA Plenary) | OECD | regulator | https://www.oecd.org/en/about/news/announcements/2025/11/heads-of-tax-administrations-agree-further-work-on-collaborative-projects-to-reduce-compliance-burdens-and-deepen-co-operation-in-tackling-tax-gaps.html | 2025-11-20 | full (via r.jina.ai mirror) |
| PWC-IE-2026 | Evolving the tax function with AI: Four key insights to guide tax leaders (Johnny Wickham) | PwC Ireland | firm | https://www.pwc.ie/services/tax/insights/evolving-the-tax-function-with-ai.html | 2026-07-21 | full (via r.jina.ai mirror) |
| SAVANT-2026 | Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Tech Seminar 2026 | Savant Labs | vendor | https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/ | 2026-04-16 | full |
| SJSU-TEIHTTI-2025 | AI and Other Emerging Technologies for Tax Practitioners (panel deck, 41st TEI-SJSU High Tech Tax Institute) | TEI and San Jose State University | conference | https://www2.sjsu.edu/taxinstitute/docs/4D_AI.pdf | 2025-11-03 | full |
| SOVOS-SOVI-2026 | Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability | Sovos | vendor | https://sovos.com/press-releases/sovos-expands-sovi-ai/ | 2026-03-24 | full |
| TAXPROF-SALA-2026 | AI Won't Shrink Corporate Tax Teams Much. Here's Why. (abstract of M. Sala, 121 Tax Notes State 189) | TaxProf Blog (Andrew Appleby) | press | https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/ | 2026-07-20 | full (abstract only) |
| TEI-TAXTECH-2026 | 2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 | full |
| TEI-TECHTAX-2025 | 2025 TechTAXcelerate: Unleashing the Future of Tax Technology (Webinar Series), programme | Tax Executives Institute | conference | https://www.tei.org/events-education/events/2025-techtaxcelerate-unleashing-future-tax-technology-webinar-series | 2025-11-17 | full (programme only) |
| TR-CORPAI-2026 | AI in corporate tax: key trends, use cases and what's next | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/ | 2026-07-01 | full |
| TR-CORPTAX-2025 | Why most tax departments aren't using AI yet (State of the Corporate Tax Department 2025) | Thomson Reuters Tax & Accounting | survey | https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/ | 2025-10-22 | full |
| TR-CORPTECH-2026 | Corporate tax teams eager for AI, but frustrated by pace of change (2026 Corporate Tax Department Technology Report summary) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en-us/posts/corporates/corporate-tax-department-technology-report-2026 | 2026-03-16 | full (summary; report not opened) |
| TR-GOVERNANCE-2026 | The governance reckoning: How tax departments must prepare for the new era of mandatory compliance | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/tax-departments-mandatory-compliance | 2026-06-02 | full |
| TR-REBRAND-2026 | You are not a cost center: Why tax departments need to rebrand themselves | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/tax-departments-rebrand | 2026-05-05 | full |
| TR-SAP-2025 | How leaders automate tax compliance in SAP S/4HANA | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/how-tax-leaders-automate-compliance-in-sap-s-4hana/ | 2025-12-02 | full |
| TR-TEIAUDITOR-2026 | 2026 TEI Tax Technology Seminar: What the auditor already knows | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows | 2026-05-12 | full |
| VERTEX-S4-2026 | New Perspectives on SAP S/4HANA Migration (white paper with DMA) | Vertex | vendor | https://www.vertexinc.com/sites/default/files/2026-03/202603-white-paper-new-perspectives-on-sap-s-4hana-migration-dma.pdf | 2026-03 (path and PDF metadata) | full |
| VERTEX-VIDA-2026 | ViDA and the Future of ERP Integration: How to Build for Continuous Transaction Controls | Vertex | vendor | https://www.vertexinc.com/node/8169 | 2026-04-17 | full |

---

## 6. Gaps

**Not found, stated plainly**
- **No quality evidence.** No error rate, override rate, parallel-run result, inspection finding or independent measurement of AI in tax data, automation or real-time reporting was found. Time-saved figures are slide timings from presenters, anecdotes in conference recaps or survey perceptions.
- **No in-house case study with figures.** Named organisations that appear are Oxford Industries (via a vendor release), Unilever Ice Cream (podcast description), OpenAI's tax department (demonstrations), Siemens Energy and Daimler Truck AG (ERP/tax engine talks, via a recap). None published outcomes. Amazon, Walmart and Procter & Gamble tax directors are named only as attendees [TR-TEIAUDITOR-2026] [TEI-TAXTECH-2026].
- **No practitioner use of tax MCP servers.** Avalara and Sovos describe them; no customer, partner or in-house team was found using one. Vertex was not found to describe an MCP server.
- **No source on automation sustainment practice.** TEI's session on it is a title only. Nothing found on EUC inventories, risk tiering or ownership standards for AI-built tax tools.
- **Community discussion not reached.** Reddit blocked `curl` (HTTP 403); TEI chapters and Tax Labs are member-only; Hacker News searches returned nothing relevant; LinkedIn was not tried.

**Not reachable or not completed**
- TEI sessions, recordings and the TEI Annual Conference 2026 (Nashville, which opens around the scan date): no recaps yet. TEI's member-only content means the TEI picture is second-hand through Thomson Reuters Institute recaps. Thomson Reuters sells tax technology, so the tone is not neutral.
- The TRI/TEI 2026 Corporate Tax Department Technology Report, the KPMG Global Tax Readiness Dividend, the Fonoa report, the EY full survey report and the PwC global pages (PwC US page returned HTTP 403) were not opened; figures come from landing pages, press releases and articles about them.
- CIOT DITT Talk: only episode descriptions were read, not audio or transcripts (the Tax Adviser article on the series was read through the mirror). Thomson Reuters's "Clarity on Tech" podcast: landing page only, no content used. Tax Notes Talk was not opened.
- Dates and figures to treat with care: the EU ViDA timing differs between two TR articles; the EY survey's "data barrier" figure is 44% in EY's release and 45% in the Bloomberg Tax write-up; the Deloitte Part three report carries no printed date (July 2026 from PDF metadata); the Vertex white paper's month comes from its file path and PDF metadata; the Sovos release page was modified in October 2026 after its March 2026 date; the seven-figure penalty anecdote in TR's governance article is unattributed.
- Web search was used ten times; searches on tax data warehouses and on vibe-coding governance returned vendor and general sources only.

**Under-documented topics (for this module)**
- Real-time reporting beyond Europe (LATAM, India, Saudi Arabia) appears only as a list of countries in a conference recap [TR-TEIAUDITOR-2026].
- Cost of agents and tokens: raised as a concern [TEI-TAXTECH-2026] with no figures anywhere.
- Controls over AI-generated code in tax (SOX documentation, change management, segregation of duties): claimed by panel slides and not evidenced.
- Public-sector tax data architecture is out of scope here and covered through the routed items.

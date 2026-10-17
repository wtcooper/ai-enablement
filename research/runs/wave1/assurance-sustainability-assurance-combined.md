# Module deep dive: assurance / sustainability-assurance / combined (practice + discourse + governance & evidence)

- **Archetype:** assurance
- **Module:** sustainability-assurance: assurance over sustainability and ESG reporting (ISSA 5000, CSRD limited assurance and ESRS, ISAE 3000/3410 GHG assurance, US regimes such as California SB 253): scoping, data gathering from many sources, evidence over estimates and value-chain data, double materiality, reporting, and how AI is used by assurance providers (and by preparers in ways that affect assurance).
- **Angle:** combined (practice + discourse + governance & evidence). This is a low-evidence module, so all three angles are covered in one pass.
- **Prepared:** 2026-10-16
- **Inputs:** `research/runs/wave1/landscape-assurance.md` (sections 3, 7, 9, 13) and `research/briefs/templates/vocabulary.md`
- **Access note:** `access: full` means this analyst opened the page or PDF. Several pages blocked direct `curl` (Cloudflare or Akamai 403); where a text mirror (`r.jina.ai`) returned the document, the source is marked `full` and the URL is the original. Standards and long documents were read at the cited paragraphs and keyword-scanned elsewhere; the Sources table says so. `search-only` items appear in the sources list only if they back a claim, and none backs an outcome.
- **How to read the grades.** Grade reflects evidence for AI use in *this module*. Material from financial-audit AI platforms (EY Canvas, IFIAR technology reports and so on) is adjacent and is routed, not graded here.

---

## 1. Summary

- **Evidence of what assurance providers actually do with AI on sustainability engagements is close to absent.**
  - The only public statement naming provider tools is one sentence in a Verdantix press release (11 Nov 2024). It says Deloitte has an AI-powered Omnia ESG tool that automates disclosure roadmaps and tracks regulatory requirements, and that KPMG uses NLP and machine learning to detect potential greenwashing in clients' reports (VERDANTIX-GQ-2024). I found no Deloitte or KPMG primary source for either claim, no figure, and no statement of whether either is used on assurance engagements rather than readiness work.
  - EY's April 2026 agentic-AI release covers 130,000 assurance professionals and 160,000 audit engagements. The text describes audit engagements and does not mention sustainability assurance (EY-MENAPR-2026).
  - The two Big Four job postings opened (KPMG Australia, posted 4 Jun 2026; EY Malaysia, posted 3 Oct 2026) list no AI duty. EY asks for ESG data-analysis tools as an advantage (KPMG-JOBAU-2026; EY-JOBMY-2026).
  - No error rate, override rate, parallel run or inspection finding for any AI tool in sustainability assurance was found.
- **The standards say nothing about AI by name; they speak of "automated tools and techniques".**
  - A text count found zero mentions of "artificial intelligence" in ISSA 5000, its Implementation Guide, the IAASB FAQs and webinar slides on planning and risk assessment, the CEAOB's EU limited-assurance advice, the Omnibus directive and the IFAC/AICPA State of Play (all opened for this note).
  - The usable text is ISSA 5000 paras A91 (overreliance on automated tools impairs critical assessment of evidence), A96–A98, A231 and A249, plus the IESSA ethics standard's technology provisions: R5320.11 (decide whether tool output is appropriate), 5300.6 A2 and the automation-bias example at 5120.12 A2 (ISSA5000-2024; IESBA-IESSA-2025).
  - The IAASB's Technology Catalog (v3, July 2026) lists "sustainability and other assurance engagements" with a "Low" priority and direction "continue monitoring" until ISSA 5000 is applied (IAASB-TECHCAT-2026, Theme 10(a), pp. 13–14).
- **The dates are firm and the regime is narrowing.**
  - ISSA 5000 and the IESSA take effect for periods beginning on or after 15 Dec 2026 (or "as at" a date on or after it). IESSA independence provisions for value-chain components are deferred to periods beginning on or after 1 Jul 2028. ISAE 3000 (Revised) and ISAE 3410 stop applying to sustainability engagements on the same date (ISSA5000-2024 para 15; IESBA-SUST-2024; IAASB-ISSA5000FAQ-2025).
  - Directive (EU) 2026/470 (OJ 26 Feb 2026) limits CSRD to undertakings above EUR 450 million net turnover and 1,000 average employees, removes the requirement for the Commission to adopt reasonable-assurance standards, and moves the limited-assurance standard deadline to 1 Jul 2027 (EU-OMNIBUS-2026). The CEAOB delivered its technical advice, based on ISSA 5000 with EU add-ons and carve-outs, on 25 Sep 2026 (CEAOB-TA-2026). Revised ESRS (Delegated Regulation (EU) 2026/1563, OJ 21 Sep 2026) apply from financial years beginning 1 Jan 2027 (EU-ESRS-2026).
  - In the US, the SEC proposed on 29 May 2026 to rescind its 2024 climate rules (DECHERT-SEC-2026). California's first SB 253 Scope 1 and 2 report moved to 10 Nov 2026, and the initial regulation does not yet require assurance; CARB previewed 2027 assurance text in July 2026 (HL-CARB-ROADMAP-2026; HL-CARB-PREVIEW-2026).
- **Most of the AI activity is on the preparer side, and nearly all of it is vendor claims.** Workiva launched a Sustainability Disclosure Agent on 12 Jun 2026; Watershed publishes customer-time figures; PwC Germany promotes a CSRD AI tool. These matter to assurance through traceability, estimates for missing data and independence: the IESSA treats implementing sustainability-reporting software for an assurance client as a self-review threat and bars it for public-interest entities (IESBA-IESSA-2025, 5606.4 A3 and R5606.6).
- **Practitioner discourse is thin and mostly vendor or academic.** ICAEW's July 2026 outlook treats AI in audit and sustainability assurance as two separate themes (ICAEW-VIEW-2026). The only practitioner survey on AI in sustainability assurance found (n = 77, Moldova, 2025) reports results about AI in financial audit; its abstract claim of faster review with no loss of greenwashing detection comes with no figures in the text (ASE-CIKE-2025).
- **Independent measurement exists for sustainability assurance itself, not for AI.** IFIAR's June 2026 factsheet shows 17% of responding members (47 took part) had inspected sustainability assurance engagements (9% in 2023), and 57% planned to start (IFIAR-SATF-2026). A Leeds/Wits study for the IAASB finds assurance scope barely moved from 2015 to 2023 (LEEDS-ASSURANCE-2026).
- **15 candidate use cases: 0 at grade A, 0 at B, 8 at C, 7 at D (labelled idea).** No named organisation published a measured outcome for any use case on an assurance engagement.

---

## 2. Use cases

```yaml
- id: assurance-sustainability-assurance-01
  title: ESRS and ISSB requirement mapping and disclosure-completeness check by the assurance team
  archetype: assurance
  module: sustainability-assurance
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Sustainability information is spread across many report sections and supporting documents. Before testing, the team has to find each disclosure, map it to the reporting standard's requirements, and spot missing baselines, targets or methods."
  solution: "NLP or LLM tools locate the relevant passages, classify them against ESRS-type categories (governance, strategy, impacts, risks and opportunities, policies, actions, targets, metrics) and produce a preliminary gap list. The output prompts the practitioner's own assessment of completeness; it is not a compliance conclusion. Analyst commentary says Deloitte has an AI-powered Omnia ESG tool that automates disclosure roadmaps and tracks regulatory requirements. A research prototype (SSKG Hub) builds expert-reviewed knowledge graphs of sustainability standards that such mapping could draw on."
  outcomes:
  - lever: speed
    description: "No time, accuracy or coverage result is published. The analyst describes what the Deloitte tool does, not how well it does it."
    figure: none published
    measures: "Not a measure; one analyst sentence about a firm tool. The source does not say whether the tool is used on assurance engagements or on readiness advice."
    provenance: vendor-published
    source_ref: VERDANTIX-GQ-2024
  prerequisites:
  - "Report text in a machine-readable form, and the entity's own list of material topics from its materiality process."
  - "A firm-approved tool; ISSA 5000 says the engagement leader may depend on the firm's technology development and maintenance programmes when using firm-approved technology (ISSA5000-2024, A97)."
  - "Practitioners able to challenge the output; the engagement team's competence includes expertise in the automated tools to be used (ISSA5000-2024, A98)."
  risks_and_guardrails:
  - "AI mapping is a screening aid. ESRS alignment needs interpretation, an understanding of double materiality and professional judgement (MDPI-SUSAI-2026, section 4.2)."
  - "Overreliance on automated tools can stop the team assessing evidence critically (ISSA5000-2024, A91)."
  - "Before using tool output, the practitioner must determine whether the use is appropriate for the purpose (IESBA-IESSA-2025, R5320.11)."
  human_checkpoints:
  - "Practitioner confirms each AI-identified disclosure is complete, relevant, entity-specific and supported by evidence (MDPI-SUSAI-2026, section 4.2)."
  - "Engagement leader approves the tool for the engagement under firm policy (ISSA5000-2024, A96–A97)."
  role_evolution: "The proposed competence profile adds data-analytics literacy and the ability to challenge AI limits and bias, without making assurance staff software engineers (MDPI-SUSAI-2026, section 7.2)."
  evidence_grade: C
  sources:
  - ref: VERDANTIX-GQ-2024
    title: "Verdantix Green Quadrant Benchmark Highlights Leading ESG & Sustainability Assurance Vendors"
    publisher: Verdantix
    type: vendor
    url: https://www.verdantix.com/insights/press-release/verdantix-green-quadrant-benchmark-highlights-leading-esg-sustainability-assurance-vendors
    date: 2024-11-11
    access: full
    locator: "Key report findings, second bullet (AI paragraph)"
  - ref: MDPI-SUSAI-2026
    title: "Artificial Intelligence in Sustainability Assurance: Accounting Challenges, Audit Risks and a Conceptual Framework for ESG Verification"
    publisher: "Preprints.org (MDPI); peer-reviewed version in Accounting and Auditing 2026, 2(3), 15"
    type: academic
    url: https://www.preprints.org/manuscript/202607.1236/v1
    date: 2026-07
    access: full
    locator: "Sections 4.2, 6.2, 7.2"
  - ref: ARXIV-SSKG-2026
    title: "SSKG Hub: An Expert-Guided Platform for LLM-Empowered Sustainability Standards Knowledge Graphs"
    publisher: arXiv 2603.00669
    type: academic
    url: https://arxiv.org/abs/2603.00669
    date: 2026-02-28
    access: full
    locator: Abstract
  - ref: ISSA5000-2024
    title: "ISSA 5000, General Requirements for Sustainability Assurance Engagements"
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2025-01/IAASB-International-Standard-on-Sustainability-Assurance-ISSA-5000.pdf
    date: 2024-11
    access: full
    locator: "A91 (p. 79); A96–A98 (p. 81)"
  - ref: IESBA-IESSA-2025
    title: "International Ethics Standards for Sustainability Assurance (including International Independence Standards) and Other Revisions to the Code (final pronouncement, updated version)"
    publisher: IESBA
    type: standard-setter
    url: "https://ifacweb.blob.core.windows.net/publicfiles/2025-08/IESSA%20and%20Revisions%20to%20the%20Code%20Final%20Pronouncement%20%28updated%20082525%29.pdf"
    date: 2025-08
    access: full
    locator: "R5320.11 and 5320.11 A1 (p. 45)"
  last_reviewed: 2026-10-16
  notes: "Grade C rests on one analyst sentence from Nov 2024. The three academic items are proposals or a research prototype, not deployments. Verdantix's full report is paywalled and was not opened."

- id: assurance-sustainability-assurance-02
  title: NLP and ML screening of draft sustainability reports for greenwashing-type claims and unsupported statements
  archetype: assurance
  module: sustainability-assurance
  function: service-delivery
  work_types:
  - review-assurance
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Sustainability reports mix hard metrics with soft narrative. Spotting vague, promotional or unsupported claims across a long report is slow, and assurance must consider whether information is balanced and not misleading."
  solution: "Text-analysis models score each report for tone, specificity and whether a claim is backed by other statements in the same report, and compare tone with an external performance proxy. The output is a set of risk flags that tells the practitioner where to look first. Analyst commentary says KPMG uses NLP and machine learning to detect potential greenwashing in clients' reports."
  outcomes:
  - lever: quality
    description: "A university prototype on 150 DAX-company ESG reports (2020–2023) found that more specific wording went with stronger internal claim support. The authors say the aim is to prioritise review, not to classify greenwashing, and that automated external fact-checking proved difficult."
    figure: "Spearman rho 0.310 (p = 0.036) between average specificity and average internal claim score"
    measures: "Correlation across company-level averages of traffic-related disclosure text in 150 DAX ESG reports, 2020–2023; a research signal, not a precision or recall result"
    provenance: independent
    source_ref: SWISSTEXT-2025
  - lever: speed
    description: "A conference paper's abstract says AI-assisted review reduces time while keeping or improving detection of exaggeration. The 8-page text read reports no time or F1 figures for this claim."
    figure: none published
    measures: "Abstract claim only; the paper's survey part (77 practitioners, Moldova) reports views on AI in financial audit"
    provenance: independent
    source_ref: ASE-CIKE-2025
  - lever: quality
    description: "Verdantix names the KPMG practice but gives no result."
    figure: none published
    measures: "Not a measure; one analyst sentence"
    provenance: vendor-published
    source_ref: VERDANTIX-GQ-2024
  prerequisites:
  - "Report drafts or published reports in text form; an external benchmark if tone is compared with performance."
  - "Scarce reliably labelled data limits conventional supervised learning for greenwashing detection (SWISSTEXT-2025, introduction)."
  risks_and_guardrails:
  - "NLP models can misread context in formal reporting language, and heuristic filtering limits precision and recall (SWISSTEXT-2025, section 5)."
  - "A flag is a risk signal that must be checked against source documents and external evidence (MDPI-SUSAI-2026, section 4.3)."
  human_checkpoints:
  - "Practitioner investigates each flag and decides whether more procedures are needed (MDPI-SUSAI-2026, sections 4.3 and 6.3)."
  role_evolution: "Reviewers spend less time reading for tone and more on testing the flagged claims; no source measures this shift."
  evidence_grade: C
  sources:
  - ref: VERDANTIX-GQ-2024
    title: "Verdantix Green Quadrant Benchmark Highlights Leading ESG & Sustainability Assurance Vendors"
    publisher: Verdantix
    type: vendor
    url: https://www.verdantix.com/insights/press-release/verdantix-green-quadrant-benchmark-highlights-leading-esg-sustainability-assurance-vendors
    date: 2024-11-11
    access: full
    locator: "Key report findings, second bullet"
  - ref: SWISSTEXT-2025
    title: "Detecting Greenwashing Hints in ESG Reports: Linguistic and Claim Analysis in Traffic-Related Emissions Disclosures"
    publisher: "Technische Universität Berlin (SwissText 2025)"
    type: academic
    url: https://www.swisstext.org/wp-content/uploads/2025/05/Detecting-Greenwashing-Hints-in-ESG-Reports-Linguistic-and-Claim-Analysis-in-Traffic-Related-Emissions-Disclosures.pdf
    date: 2025-05
    access: full
    locator: "Abstract; section 4.3; section 5 (discussion)"
  - ref: ASE-CIKE-2025
    title: "The Application of Artificial Intelligence in Auditing Sustainability Reports: Between Ethical Challenges and Efficiency"
    publisher: "Annual International Scientific Conference CIKE, Chisinau, 26-27 Sep 2025 (proceedings pp. 432-439)"
    type: conference
    url: https://conferences.ase.ro/?p=875
    date: 2025-09-26
    access: full
    locator: "Abstract; 'Basic content' section"
  - ref: MDPI-SUSAI-2026
    title: "Artificial Intelligence in Sustainability Assurance: Accounting Challenges, Audit Risks and a Conceptual Framework for ESG Verification"
    publisher: "Preprints.org (MDPI)"
    type: academic
    url: https://www.preprints.org/manuscript/202607.1236/v1
    date: 2026-07
    access: full
    locator: "Sections 4.3, 6.3"
  last_reviewed: 2026-10-16
  notes: "Maturity is 'announced' because the KPMG practice rests on one analyst sentence and no KPMG source was found. The SwissText date comes from the publisher's upload path (2025/05). The abstract claim in ASE-CIKE-2025 is not backed by figures in the text read."

- id: assurance-sustainability-assurance-03
  title: Anomaly and consistency analytics over multi-year sustainability data and narrative-versus-number checks (idea)
  archetype: assurance
  module: sustainability-assurance
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Reports carry multi-year data on emissions, energy, water, waste, workforce and safety. Unexplained changes, unit inconsistencies, restatements and contradictions between narrative and numbers are easy to miss when data arrives in many formats."
  solution: "Analytics or AI run over all reported data points and the narrative to flag unusual swings, missing values, inconsistent units and text that contradicts the numbers. For example, a sharp emissions fall might reflect a boundary or method change. The practitioner investigates each flag."
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: "Researchers propose the use; no deployment or measurement was found for sustainability assurance"
    provenance: independent
    source_ref: MDPI-SUSAI-2026
  prerequisites:
  - "Structured data export or a sustainability data platform; a baseline of prior-year data."
  - "Definitions of boundaries and methods to separate real change from reporting change."
  risks_and_guardrails:
  - "AI output creates risk flags, not conclusions; a technically polished result can create a false impression of objectivity (MDPI-SUSAI-2026, sections 4.3 and 7.2)."
  - "Black-box models can be hard to explain to regulators and assurance providers (MDPI-SLR-2026, section 4.5)."
  human_checkpoints:
  - "Practitioner decides whether each anomaly needs recalculation, source inspection, inquiry or control testing (MDPI-SUSAI-2026, section 6.3)."
  role_evolution: "The reviewed literature expects assurance providers to need new skills in model evaluation, data validation and AI governance (MDPI-SLR-2026, section 4.6)."
  evidence_grade: D
  sources:
  - ref: MDPI-SUSAI-2026
    title: "Artificial Intelligence in Sustainability Assurance: Accounting Challenges, Audit Risks and a Conceptual Framework for ESG Verification"
    publisher: "Preprints.org (MDPI)"
    type: academic
    url: https://www.preprints.org/manuscript/202607.1236/v1
    date: 2026-07
    access: full
    locator: "Sections 4.3, 6.3, 7.2"
  - ref: LI-JETA-2024
    title: "Using Artificial Intelligence in ESG Assurance"
    publisher: "Journal of Emerging Technologies in Accounting 21(2), 83-99 (Li, Kim, Dai, Vasarhelyi)"
    type: academic
    url: https://digitalcommons.mtu.edu/michigantech-p2/1154
    date: 2024-10
    access: full
    locator: "Abstract (repository page)"
  - ref: MDPI-SLR-2026
    title: "AI and Data Analytics in Sustainable Financial Reporting and ESG Disclosure: A Systematic Literature Review"
    publisher: "Sustainability 18(11), 5393 (MDPI)"
    type: academic
    url: https://www.mdpi.com/2071-1050/18/11/5393
    date: 2026-05-26
    access: full
    locator: "Sections 3.2.3, 4.3, 4.5, 4.6"
  last_reviewed: 2026-10-16
  notes: "Idea. Grade D because the sources are conceptual or review papers. The systematic review found 8 of its 45 studies in the AI-in-assurance theme; it does not report any live assurance use. The Moldova survey in ASE-CIKE-2025 ranks anomaly detection as the top automation priority (88.9%) but concerns financial audit, so it is not used as support."

- id: assurance-sustainability-assurance-04
  title: External-data triangulation of GHG, supplier and value-chain claims (satellite imagery, emission-factor databases, media and regulatory sources) (idea)
  archetype: assurance
  module: sustainability-assurance
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Much sustainability evidence comes from the entity itself or from suppliers the practitioner cannot reach. The team often has no independent source to compare reported emissions, supplier claims or controversies against."
  solution: "AI tools match reported figures with outside data: satellite images for site emissions, recognised emission-factor databases, peer outliers, media and regulatory records. The result is used to target procedures and to corroborate, not to replace direct evidence."
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: "A cited academic demonstration used satellite images to verify GHG emissions; the systematic review lists it among the most influential studies in its AI-assurance theme (36 citations) but gives no accuracy result"
    provenance: independent
    source_ref: MDPI-SLR-2026
  prerequisites:
  - "Access to licensed or open external datasets and the skill to assess their reliability and relevance."
  - "Location and activity data for the sites or suppliers being checked."
  risks_and_guardrails:
  - "External data must itself be assessed for reliability, relevance and completeness; triangulation is a risk-assessment and corroboration aid, not substitute evidence (MDPI-SUSAI-2026, section 4.4)."
  - "ISSA 5000 warns that evidence obtained only from easily accessible sources can bias selection; evidence should come from multiple sources where possible (ISSA5000-2024, A91 and A228)."
  human_checkpoints:
  - "Practitioner decides whether an external signal calls for further procedures at the entity or supplier (MDPI-SUSAI-2026, section 4.4)."
  role_evolution: "Not described in the sources beyond the need for model-evaluation and data-validation skills (MDPI-SLR-2026, section 4.6)."
  evidence_grade: D
  sources:
  - ref: MDPI-SLR-2026
    title: "AI and Data Analytics in Sustainable Financial Reporting and ESG Disclosure: A Systematic Literature Review"
    publisher: "Sustainability 18(11), 5393 (MDPI)"
    type: academic
    url: https://www.mdpi.com/2071-1050/18/11/5393
    date: 2026-05-26
    access: full
    locator: "Sections 3.2.3 and 4.3"
  - ref: MDPI-SUSAI-2026
    title: "Artificial Intelligence in Sustainability Assurance: Accounting Challenges, Audit Risks and a Conceptual Framework for ESG Verification"
    publisher: "Preprints.org (MDPI)"
    type: academic
    url: https://www.preprints.org/manuscript/202607.1236/v1
    date: 2026-07
    access: full
    locator: "Section 4.4"
  - ref: LI-JETA-2024
    title: "Using Artificial Intelligence in ESG Assurance"
    publisher: "Journal of Emerging Technologies in Accounting 21(2), 83-99"
    type: academic
    url: https://digitalcommons.mtu.edu/michigantech-p2/1154
    date: 2024-10
    access: full
    locator: "Abstract (proposes AI and exogenous data)"
  - ref: ISSA5000-2024
    title: "ISSA 5000, General Requirements for Sustainability Assurance Engagements"
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2025-01/IAASB-International-Standard-on-Sustainability-Assurance-ISSA-5000.pdf
    date: 2024-11
    access: full
    locator: "A91 (p. 79)"
  last_reviewed: 2026-10-16
  notes: "Idea. The underlying satellite study (Gu, Dai, Vasarhelyi, Int. J. Accounting Information Systems 2023) was not opened (ScienceDirect blocked); its description comes from the systematic review. ISSA 5000 A228 was read as the paragraph on obtaining evidence in an unbiased manner from multiple sources; its page was not recorded."

- id: assurance-sustainability-assurance-05
  title: Source-linked drafting of evidence matrices, procedure descriptions and workpaper summaries (idea)
  archetype: assurance
  module: sustainability-assurance
  function: service-delivery
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Sustainability engagements generate long reports, policies, datasets and correspondence that must be summarised and documented in the assurance file."
  solution: "Generative AI summarises long documents, prepares a preliminary evidence matrix and drafts descriptions of procedures, with every output linked to its source, logged and reviewed by the team."
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: "Proposed in an academic framework; no deployment or time figure found for sustainability assurance"
    provenance: independent
    source_ref: MDPI-SUSAI-2026
  prerequisites:
  - "A firm-approved generative tool with confidentiality controls for client data."
  - "Retention of prompts, output versions, source links and reviewer comments in the file (MDPI-SUSAI-2026, section 6.3)."
  risks_and_guardrails:
  - "ISSA 5000 says the engagement leader may depend on the firm's technology programmes when using firm-approved technology (ISSA5000-2024, A97)."
  - "The practitioner must decide whether tool output suits its purpose and consider the firm's oversight and controls over the tool (IESBA-IESSA-2025, 5320.11 A1)."
  human_checkpoints:
  - "Reviewer corrects and source-checks all AI drafts before they enter the file (MDPI-SUSAI-2026, section 4.4)."
  role_evolution: "Not described in the sources."
  evidence_grade: D
  sources:
  - ref: MDPI-SUSAI-2026
    title: "Artificial Intelligence in Sustainability Assurance: Accounting Challenges, Audit Risks and a Conceptual Framework for ESG Verification"
    publisher: "Preprints.org (MDPI)"
    type: academic
    url: https://www.preprints.org/manuscript/202607.1236/v1
    date: 2026-07
    access: full
    locator: "Sections 4.4, 6.3"
  - ref: ISSA5000-2024
    title: "ISSA 5000, General Requirements for Sustainability Assurance Engagements"
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2025-01/IAASB-International-Standard-on-Sustainability-Assurance-ISSA-5000.pdf
    date: 2024-11
    access: full
    locator: "A96–A97 (p. 81)"
  - ref: IESBA-IESSA-2025
    title: "International Ethics Standards for Sustainability Assurance (including International Independence Standards) and Other Revisions to the Code (final pronouncement, updated version)"
    publisher: IESBA
    type: standard-setter
    url: "https://ifacweb.blob.core.windows.net/publicfiles/2025-08/IESSA%20and%20Revisions%20to%20the%20Code%20Final%20Pronouncement%20%28updated%20082525%29.pdf"
    date: 2025-08
    access: full
    locator: "5320.11 A1 (p. 45)"
  last_reviewed: 2026-10-16
  notes: "Idea. Large financial-audit platforms (EY, KPMG, Deloitte) describe agents that draft audit documentation; none says this extends to sustainability work. That material is routed to other modules."

- id: assurance-sustainability-assurance-06
  title: AI-supported risk assessment and planning priorities for sustainability engagements (idea)
  archetype: assurance
  module: sustainability-assurance
  function: service-delivery
  work_types:
  - expert-judgment
  - coordination-scheduling
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "ISSA 5000 asks for risk assessment across many topics, sites and value-chain components. Teams have limited time to decide where the risk of material misstatement is highest and to allocate testing."
  solution: "AI highlights high-risk areas, unusual metrics, missing evidence and inconsistent disclosures so the team can prioritise procedures and allocate resources. The risk assessment itself remains the practitioner's."
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: "Proposed in an academic framework and a JETA paper; no deployment found"
    provenance: independent
    source_ref: MDPI-SUSAI-2026
  prerequisites:
  - "Prior-year files, entity documents and data in machine-readable form."
  - "A documented link between AI risk signals and the engagement's risk assessment (MDPI-SUSAI-2026, section 6.2)."
  risks_and_guardrails:
  - "AI signals are converted into assurance-relevant risk signals and evaluated for relevance and materiality; they are not final conclusions (MDPI-SUSAI-2026, section 6.2)."
  human_checkpoints:
  - "Practitioner remains responsible for the risk assessment; each AI signal is evaluated for relevance, materiality and the need for additional procedures (MDPI-SUSAI-2026, section 6.2)."
  role_evolution: "Not described in the sources."
  evidence_grade: D
  sources:
  - ref: MDPI-SUSAI-2026
    title: "Artificial Intelligence in Sustainability Assurance: Accounting Challenges, Audit Risks and a Conceptual Framework for ESG Verification"
    publisher: "Preprints.org (MDPI)"
    type: academic
    url: https://www.preprints.org/manuscript/202607.1236/v1
    date: 2026-07
    access: full
    locator: "Sections 4.4, 6.2"
  - ref: LI-JETA-2024
    title: "Using Artificial Intelligence in ESG Assurance"
    publisher: "Journal of Emerging Technologies in Accounting 21(2), 83-99"
    type: academic
    url: https://digitalcommons.mtu.edu/michigantech-p2/1154
    date: 2024-10
    access: full
    locator: "Abstract (AI across the assurance process)"
  last_reviewed: 2026-10-16
  notes: "Idea. The financial-audit analogue (FRC example on summarising board minutes for risk assessment; IFIAR 55% frequency of tools in risk assessment) sits in landscape-assurance.md and is routed to planning-risk-assessment."

- id: assurance-sustainability-assurance-07
  title: Continuous or real-time evaluation of digital sustainability data by automated tools (idea)
  archetype: assurance
  module: sustainability-assurance
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "Annual engagements review data months after the fact. Some sustainability data exists only in digital form on a continuous basis (for example meter or sensor feeds), so point-in-time sampling can miss problems."
  solution: "Automated tools run continuously over the digital data, evaluate its relevance and reliability, and raise exceptions for the practitioner. ISSA 5000 gives this as an example of how the practitioner may use automated tools. The literature frames it as a move from retrospective document review to continuous, data-driven assurance."
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: "Standard-setter example and literature discussion; no engagement result found"
    provenance: independent
    source_ref: MDPI-SLR-2026
  prerequisites:
  - "Digital data available continuously, with stable definitions and system controls over its integrity (ISSA5000-2024, A262)."
  - "Tools designed to operate in real time, evaluated and approved by the firm (ISSA5000-2024, A249 and A97)."
  risks_and_guardrails:
  - "Overreliance on automated tools can stop critical assessment of evidence (ISSA5000-2024, A91)."
  human_checkpoints:
  - "Practitioner evaluates the relevance and reliability of the information and the tool's operation (ISSA5000-2024, A249)."
  role_evolution: "Not described in the sources."
  evidence_grade: D
  sources:
  - ref: ISSA5000-2024
    title: "ISSA 5000, General Requirements for Sustainability Assurance Engagements"
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2025-01/IAASB-International-Standard-on-Sustainability-Assurance-ISSA-5000.pdf
    date: 2024-11
    access: full
    locator: "A249 (p. 114); A262 (p. 117)"
  - ref: MDPI-SLR-2026
    title: "AI and Data Analytics in Sustainable Financial Reporting and ESG Disclosure: A Systematic Literature Review"
    publisher: "Sustainability 18(11), 5393 (MDPI)"
    type: academic
    url: https://www.mdpi.com/2071-1050/18/11/5393
    date: 2026-05-26
    access: full
    locator: "Sections 3.2.3 and 4.3 (Audit 4.0 framework)"
  - ref: MDPI-SUSAI-2026
    title: "Artificial Intelligence in Sustainability Assurance: Accounting Challenges, Audit Risks and a Conceptual Framework for ESG Verification"
    publisher: "Preprints.org (MDPI)"
    type: academic
    url: https://www.preprints.org/manuscript/202607.1236/v1
    date: 2026-07
    access: full
    locator: "Sections 3.6 and 4.4"
  last_reviewed: 2026-10-16
  notes: "Idea. ISSA 5000 A249 is an illustration of a permitted approach, not evidence that anyone does it."

- id: assurance-sustainability-assurance-08
  title: Agent that checks disclosures against ESRS or ISSB and drafts fixes inside the reporting platform before assurance (preparer side)
  archetype: assurance
  module: sustainability-assurance
  function: finance-accounting
  work_types:
  - review-assurance
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Reporting teams compare long standards with existing content line by line. Gaps that surface late, during executive, legal or assurance review, can force new data, evidence or approvals under deadline."
  solution: "Workiva's Sustainability Disclosure Agent assesses selected content against chosen ESRS or ISSB requirements, marks each as present, partial or missing in a scorecard, and drafts a first version. It runs inside the platform, which the vendor says keeps audit trail and version control. A multi-agent design splits the tasks. Workiva presents it as supporting expert judgement; sign-off stays with the team."
  outcomes:
  - lever: speed
    description: "No time, accuracy or usage figure was published. Coverage describes features only."
    figure: none published
    measures: "Product description; availability is for customers on Workiva's advanced solution tiers"
    provenance: vendor-published
    source_ref: ITBRIEF-WORKIVA-2026
  prerequisites:
  - "Disclosure content and underlying data already held in the vendor's platform."
  - "A workflow in which the gap list and draft are reviewed by people with standards knowledge."
  risks_and_guardrails:
  - "Agent output is a draft for review and is not an assurance conclusion; the vendor says interpretation and sign-off stay with the client team (ESGPOST-WORKIVA-2026)."
  - "ISSA 5000 warns that overreliance on automated tools can stop critical assessment of evidence (ISSA5000-2024, A91). The Workiva sources do not say how assurance providers treat agent-produced material."
  human_checkpoints:
  - "Reporting team reviews the scorecard and the first draft before they enter the report (ESGNEWS-WORKIVA-2026)."
  role_evolution: "Workiva's product chief says finance, sustainability, risk and compliance teams are moving from execution to orchestration as agents take on more work (ITBRIEF-WORKIVA-2026)."
  evidence_grade: C
  sources:
  - ref: ESGNEWS-WORKIVA-2026
    title: "Workiva Launches AI Disclosure Agent to Help Companies Close Sustainability Reporting Gaps Earlier"
    publisher: ESG News
    type: press
    url: https://esgnews.com/workiva-launches-ai-disclosure-agent-to-help-companies-close-sustainability-reporting-gaps-earlier/
    date: 2026-06-12
    access: full
    locator: "Sections 'Agent Targets Gaps Before Review' and 'From Assessment to Draft'"
  - ref: ESGPOST-WORKIVA-2026
    title: "Workiva launches AI-powered agent to automate sustainability disclosure analysis"
    publisher: ESG Post
    type: press
    url: https://esgpost.com/workiva-launches-ai-powered-agent-to-automate-sustainability-disclosure-analysis/
    date: 2026-06-12
    access: full
    locator: "Body, paragraphs 1-6"
  - ref: ITBRIEF-WORKIVA-2026
    title: "Workiva launches AI agents for reporting & compliance"
    publisher: IT Brief UK
    type: press
    url: https://itbrief.co.uk/story/workiva-launches-ai-agents-for-reporting-compliance
    date: 2026-07-30
    access: full
    locator: "Opening paragraphs; 'New agents'; 'Audit trail focus'"
  last_reviewed: 2026-10-16
  notes: "Dates conflict across coverage: ESG News and ESG Post date the Sustainability Disclosure Agent launch 12 Jun 2026; IT Brief (30 Jul 2026) reports it as one of three agents launched together. Some search extracts gave late July. This entry uses 12 Jun 2026 for the agent. All figures and features are vendor-stated."

- id: assurance-sustainability-assurance-09
  title: Automated ingestion, cleaning and spend-based Scope 3 classification with calculation lineage (preparer side)
  archetype: assurance
  module: sustainability-assurance
  function: finance-accounting
  work_types:
  - data-reporting
  - transaction-processing
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Scope 3 data arrives from hundreds of suppliers as PDFs, spreadsheets and inconsistent questionnaires. Reconciling it takes weeks each cycle, and numbers without a traceable source are hard for assurance to verify."
  solution: "OCR extracts data from bills and supplier documents, agents standardise units, dates and codes and remove duplicates, and models map procurement lines to emissions categories using spend and descriptions. Each output is meant to trace to its source, emission factor and approval history, which is what an assurance provider needs to follow the numbers."
  outcomes:
  - lever: speed
    description: "Vendor-reported customer outcome for OCR data entry."
    figure: "90% reduction in OCR data entry time"
    measures: "As stated by the vendor for customers using its PDF scanner; baseline and sample not given"
    provenance: vendor-published
    source_ref: WATERSHED-AI-2026
  - lever: speed
    description: "Vendor-reported time to actionable data across its test customers; one company did a five-hour data job in 20 minutes."
    figure: "65-80% reduction in time to actionable data"
    measures: "As stated by the vendor across Watershed test customers; number of customers, tasks and baseline not given"
    provenance: vendor-published
    source_ref: WATERSHED-AI-2026
  - lever: speed
    description: "Vendor says Smiths Group completed its SB 261 report in two days, and Harris Farm Markets completed emissions measurement six times faster than manually."
    figure: "Two days; six times faster"
    measures: "Vendor statements about two named customers; SB 261 is a climate-risk report, not an assured GHG inventory; baselines not given"
    provenance: vendor-published
    source_ref: WATERSHED-AI-2026
  prerequisites:
  - "Supplier and utility documents in digital form; an emission-factor library with a documented source."
  - "A logged workflow in which each agent hand-off keeps lineage (WATERSHED-AI-2026)."
  risks_and_guardrails:
  - "When agents hand off without logging, calculation lineage breaks and auditors cannot follow the chain (WATERSHED-AI-2026, 'Why many AI sustainability deployments underdeliver')."
  - "Vendors claiming 99%+ accuracy without caveats are overstating, by the vendor's own checklist; ask for failure modes and a dry run with your auditor (WATERSHED-AI-2026)."
  human_checkpoints:
  - "Humans review outputs before they are used in disclosures (WATERSHED-AI-2026, 'Where AI delivers measurable value')."
  - "Assurance practitioner evaluates relevance and reliability of the data, including the system controls that keep it intact (ISSA5000-2024, A262)."
  role_evolution: "The vendor says AI absorbs data preparation so sustainability teams can spend more time on strategy and reduction planning (WATERSHED-AI-2026)."
  evidence_grade: C
  sources:
  - ref: WATERSHED-AI-2026
    title: "Sustainability AI in 2026: what works, what doesn't, and why the difference matters"
    publisher: Watershed
    type: vendor
    url: https://watershed.com/blog/sustainability-ai-in-2026-what-works-what-doesnt-and-why-the-difference-matters
    date: 2026-06-10
    access: full
    locator: "'Where AI delivers measurable value in sustainability workflows'; 'Why many AI sustainability deployments underdeliver'"
  - ref: ISSA5000-2024
    title: "ISSA 5000, General Requirements for Sustainability Assurance Engagements"
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2025-01/IAASB-International-Standard-on-Sustainability-Assurance-ISSA-5000.pdf
    date: 2024-11
    access: full
    locator: "A262 (p. 117)"
  last_reviewed: 2026-10-16
  notes: "Grade C because every figure is vendor-published, even though two customers are named. Preparer-side; included because the module covers preparer AI that affects assurance. SB 261 enforcement was paused per a Dechert note of Jun 2026 (DECHERT-SEC-2026, footnote 5), so the Smiths Group example may not be a required filing."

- id: assurance-sustainability-assurance-10
  title: AI-generated gap-filling and estimates for missing or value-chain data (preparer side, with assurance consequences)
  archetype: assurance
  module: sustainability-assurance
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Value-chain data is often unavailable or unreliable. Reporting rules let entities use estimates, and the assurance provider must evaluate the data, methods and assumptions behind them."
  solution: "Tools flag data gaps and propose gap-fill methods such as proxy data, sector averages and estimation models, and keep a record of the assumption and rationale. The vendor argues this record reduces friction with auditors."
  outcomes:
  - lever: quality
    description: "No result is published; the vendor states that auditors require documentation of gaps and gap-fill rationale."
    figure: none published
    measures: "Vendor assertion; no accuracy or error figure"
    provenance: vendor-published
    source_ref: WATERSHED-AI-2026
  prerequisites:
  - "A policy on when estimates are acceptable and how uncertainty is disclosed."
  - "Data on the part of the value chain that is available, to support sample or sector-based estimation."
  risks_and_guardrails:
  - "The revised ESRS 1 lets entities estimate value-chain information from indirect sources, sector averages, sample analyses, spend-based data or other proxies, depending on practicability and reliability (EU-ESRS-2026, ESRS 1 paras 65-66)."
  - "Where reliable direct or estimated data covers only part of operations or the value chain, the entity discloses that scope limit, except for gross Scope 1, 2, 3 GHG metrics (EU-ESRS-2026, ESRS 1 para 91)."
  - "For estimates, limited-assurance procedures respond to risk at disclosure level, and reasonable-assurance procedures test how management developed the estimate (ACCA-ABMAG-2026)."
  - "Where information comes from a supplier's own assurance report, the practitioner may find it insufficient and need other procedures (ISSA5000-2024, A131)."
  human_checkpoints:
  - "Practitioner considers assumptions, method changes, comparability and transparency, and whether assumptions are consistent with external evidence and free of management bias (ACCA-ABMAG-2026)."
  role_evolution: "Not described in the sources."
  evidence_grade: C
  sources:
  - ref: WATERSHED-AI-2026
    title: "Sustainability AI in 2026: what works, what doesn't, and why the difference matters"
    publisher: Watershed
    type: vendor
    url: https://watershed.com/blog/sustainability-ai-in-2026-what-works-what-doesnt-and-why-the-difference-matters
    date: 2026-06-10
    access: full
    locator: "'Anomaly detection and gap-filling'"
  - ref: EU-ESRS-2026
    title: "Commission Delegated Regulation (EU) 2026/1563 amending Delegated Regulation (EU) 2023/2772 (simplified ESRS)"
    publisher: European Commission (Official Journal)
    type: regulator
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601563
    date: 2026-09-21
    access: full
    locator: "Annex I, ESRS 1 paras 65, 66, 91; entry into force and application articles"
  - ref: ACCA-ABMAG-2026
    title: "Get ready for ISSA 5000 (Accounting and Business magazine, April 2026 issue)"
    publisher: ACCA
    type: professional-body
    url: https://abmagazine.accaglobal.com/global/articles/2026/apr/practice/get-ready-for-issa-5000.html
    date: 2026-04
    access: full
    locator: "Body, paragraphs on ACCA/CAANZ report on estimates and forward-looking information"
  - ref: ISSA5000-2024
    title: "ISSA 5000, General Requirements for Sustainability Assurance Engagements"
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2025-01/IAASB-International-Standard-on-Sustainability-Assurance-ISSA-5000.pdf
    date: 2024-11
    access: full
    locator: "A130–A131 (pp. 89–90)"
  last_reviewed: 2026-10-16
  notes: "Grade C: one vendor statement. The regulatory and standards points show why the use case matters to assurance; they do not show AI is used for estimates in practice. ESRS paragraph numbers are as numbered in the Official Journal annex text."

- id: assurance-sustainability-assurance-11
  title: Big Four firm AI tool for client CSRD data collection, KPI calculation and report generation (advisory side, with independence consequences)
  archetype: assurance
  module: sustainability-assurance
  function: finance-accounting
  work_types:
  - data-reporting
  - document-production
  pattern: bulk-transformation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "CSRD reporters must gather thousands of data points across the value chain and calculate many KPIs; manual handling is slow and error-prone."
  solution: "PwC Germany's CSRD.AI Manager, built with SAP on SAP AI Core, HANA Cloud and Datasphere, extracts, organises and analyses data, calculates KPIs and speeds up report generation for clients, using the firm's CSRD content and customisable data models."
  outcomes:
  - lever: speed
    description: "A PwC product owner says it removed a heavy resource drain for clients. No figure is given."
    figure: none published
    measures: "Self-reported statements in a trade article; no time, cost or accuracy figure"
    provenance: self-reported
    source_ref: KNOWESG-PWCAI-2025
  prerequisites:
  - "SAP technology stack and the firm's CSRD content (KNOWESG-PWCAI-2025)."
  - "An independence assessment of the service if the same firm or network audits or assures the client (IESBA-IESSA-2025, subsection 5606)."
  risks_and_guardrails:
  - "Implementing sustainability-information management systems or reporting software for a sustainability assurance client can create a self-review threat, whether or not the firm built it (IESBA-IESSA-2025, 5606.4 A3)."
  - "A firm or network firm shall not provide IT systems services to a public-interest sustainability assurance client if a self-review threat may arise (IESBA-IESSA-2025, R5606.6)."
  - "Designing or implementing software to collect or produce sustainability data is listed among activities that count as a management responsibility (IESBA-IESSA-2025, 5400.20 A3)."
  human_checkpoints:
  - "Firm evaluates threats and safeguards before accepting a non-assurance service for an assurance client (IESBA-IESSA-2025, section 5600)."
  role_evolution: "Not described in the source."
  evidence_grade: C
  sources:
  - ref: KNOWESG-PWCAI-2025
    title: "AI-Powered Sustainability: PwC's New Tool Changes the Game for CSRD"
    publisher: KnowESG
    type: press
    url: https://knowesg.com/tech/ai-powered-sustainability-pwcs-new-tool-changes-the-game-for-csrd-06062025
    date: 2025-06-06
    access: full
    locator: "'Automation to the Rescue'; 'Built on a Strong Tech Foundation'"
  - ref: IESBA-IESSA-2025
    title: "International Ethics Standards for Sustainability Assurance (including International Independence Standards) and Other Revisions to the Code (final pronouncement, updated version)"
    publisher: IESBA
    type: standard-setter
    url: "https://ifacweb.blob.core.windows.net/publicfiles/2025-08/IESSA%20and%20Revisions%20to%20the%20Code%20Final%20Pronouncement%20%28updated%20082525%29.pdf"
    date: 2025-08
    access: full
    locator: "5400.20 A3 (pp. 84-85); 5606.4 A3 and R5606.6 (pp. 172-173)"
  last_reviewed: 2026-10-16
  notes: "Not graded B because no client is named and the only source is one promotional article. Nothing in the sources says PwC Germany assures clients that use the tool; the IESSA points explain why the question matters. The article was read through a text mirror because direct access was blocked."

- id: assurance-sustainability-assurance-12
  title: AI-assisted double materiality assessment by preparers, and assurance over the entity's process to identify reportable information
  archetype: assurance
  module: sustainability-assurance
  function: finance-accounting
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "The materiality assessment decides what is reported. Under ESRS it must consider impacts and financial effects, and ISSA 5000 requires the practitioner to consider the entity's process to identify the information to report. The work is large, judgement-heavy and a frequent source of assurance findings."
  solution: "Preparers use AI to support materiality assessments. Survey respondents name it a primary AI use case and an investment priority for the next three years. The assurance provider still has to understand and test the entity's process, whatever tool supports it."
  outcomes:
  - lever: capacity
    description: "A survey summary reports AI in materiality assessments as a primary use case among respondents that use AI. No time or quality figure is given."
    figure: none published
    measures: "Reuters Events 2025 Sustainability Reporting Outlook as summarised by Thomson Reuters Institute; the use-case share is not stated"
    provenance: independent
    source_ref: TRI-SUSTAIN-2025
  prerequisites:
  - "A documented materiality methodology with inputs, thresholds and approvals."
  - "Evidence that stakeholder and expert input behind the AI-assisted result can be shown to the practitioner."
  risks_and_guardrails:
  - "ISSA 5000 has fuller requirements and application material on the entity's process to identify sustainability information and on double materiality, in response to EU concerns (IAASB-EUFAQ-2025, Q5)."
  - "The entity's materiality process differs from the practitioner's own materiality in planning and performing the engagement; the IAASB covers the difference in the Implementation Guide (IAASB-MATFAQ-2026, resource list)."
  - "The CSRD limited-assurance opinion covers the process the undertaking carried out to identify the reported information (EU-OMNIBUS-2026, Article 2(12)(a), amended Article 34(1)(aa) of the Accounting Directive)."
  human_checkpoints:
  - "Practitioner evaluates the entity's process and its outcome against the framework's criteria (IAASB-EUFAQ-2025, Q5)."
  role_evolution: "Not described in the sources."
  evidence_grade: C
  sources:
  - ref: TRI-SUSTAIN-2025
    title: "Future-proofing sustainability reporting: Solutions to AI and data challenges for CSRD compliance (Reuters Events 2025 Sustainability Reporting Outlook)"
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/sustainability-reporting-solutions-csrd-compliance
    date: 2025-06
    access: full
    locator: "Section on AI in materiality assessments (paragraph after the 37% / 22% figures)"
  - ref: IAASB-EUFAQ-2025
    title: "ISSA 5000 FAQ: Relevance of ISSA 5000 to Assurance on Sustainability Reports in the European Union"
    publisher: IAASB (staff)
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2025-11/IAASB-ISSA-5000-FAQ-Relevant-to-European-Union.pdf
    date: 2025-11
    access: full
    locator: "Q5 (p. 3)"
  - ref: IAASB-MATFAQ-2026
    title: "ISSA 5000 FAQ: The Application of Materiality under ISSA 5000"
    publisher: IAASB (staff)
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2026-06/IAASB-ISSA-5000-Sustainability-Frequently-Asked-Questions-FAQ-Materiality.pdf
    date: 2026-06
    access: full
    locator: "Opening pages and 'Existing Resources on Materiality' list only"
  - ref: EU-OMNIBUS-2026
    title: "Directive (EU) 2026/470 amending Directives 2006/43/EC, 2013/34/EU, (EU) 2022/2464 and (EU) 2024/1760"
    publisher: European Parliament and Council (Official Journal)
    type: regulator
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202600470
    date: 2026-02-26
    access: full
    locator: "Article 2(12)(a), amending Article 34(1), second subparagraph, point (aa) of Directive 2013/34/EU (Accounting Directive)"
  last_reviewed: 2026-10-16
  notes: "The survey figure is second-hand (TRI summarising Reuters Events) and preparer-side. The use case is preparer-side AI with an assurance consequence; no source shows an assurance provider testing an AI-assisted materiality assessment."

- id: assurance-sustainability-assurance-13
  title: Assurance procedures over a client's AI-assisted or automated sustainability reporting pipeline (provenance, prompt logs, tool lineage) (idea)
  archetype: assurance
  module: sustainability-assurance
  function: service-delivery
  work_types:
  - review-assurance
  pattern: reconcile-exceptions
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "As preparers draft and calculate with AI, the practitioner must decide how to obtain evidence about information produced by systems the team cannot easily inspect, and whether the entity's controls keep the data intact."
  solution: "Assurance teams extend their understanding of the entity's information system to cover AI-assisted steps: what tool, what data, what prompts or parameters, what validation, and how the output reached the report. Practitioners and vendors suggest asking for traceability and running a dry run of AI-generated reports with the auditor. A sector site says assurance providers are developing methods for assessing AI-generated disclosures; no method is described."
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: "Discussed by researchers, an industry site and vendors; no method or result published"
    provenance: independent
    source_ref: MDPI-SUSAI-2026
  prerequisites:
  - "Preparer keeps prompt logs, output versions, source links and validation records (MDPI-SUSAI-2026, section 6.3)."
  - "General IT controls that maintain the integrity of the sustainability information (ISSA5000-2024, A262)."
  risks_and_guardrails:
  - "The IAASB expects questions on the practitioner's understanding of the entity's information system and internal control, the reliability of information used as evidence, and estimates, assumptions and models as entities use complex systems and external data (IAASB-TECHCAT-2026, Theme 10(a))."
  - "The IAASB's direction is to keep monitoring and wait for ISSA 5000 implementation experience before deciding whether sustainability-specific clarification is needed (IAASB-TECHCAT-2026, Theme 10(a))."
  human_checkpoints:
  - "Practitioner decides what evidence is sufficient and appropriate for information from AI-assisted processes (IAASB-TECHCAT-2026, Theme 10(a))."
  role_evolution: "Not described in the sources."
  evidence_grade: D
  sources:
  - ref: IAASB-TECHCAT-2026
    title: "Technology Catalog: Catalog of Technology-Related Matters and Preliminary Direction on Actions, Version 3"
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2026-07/IAASB-Technology-Catalog-of-Issues-Proposed-Actions.pdf
    date: 2026-07
    access: full
    locator: "Theme 10(a), pp. 13-14 (priority 'Low')"
  - ref: MDPI-SUSAI-2026
    title: "Artificial Intelligence in Sustainability Assurance: Accounting Challenges, Audit Risks and a Conceptual Framework for ESG Verification"
    publisher: "Preprints.org (MDPI)"
    type: academic
    url: https://www.preprints.org/manuscript/202607.1236/v1
    date: 2026-07
    access: full
    locator: "Sections 5.4, 6.3"
  - ref: ESGSOURCE-2026
    title: "The State of ESG in 2026: What's Changed and What's Next"
    publisher: ESGsource
    type: community
    url: https://esgsource.com/state-of-esg-2026
    date: 2026-10-16
    access: full
    locator: "Sections 'AI in ESG Reporting' and 'AI Governance for ESG'"
  - ref: WATERSHED-AI-2026
    title: "Sustainability AI in 2026: what works, what doesn't, and why the difference matters"
    publisher: Watershed
    type: vendor
    url: https://watershed.com/blog/sustainability-ai-in-2026-what-works-what-doesnt-and-why-the-difference-matters
    date: 2026-06-10
    access: full
    locator: "'How to evaluate sustainability AI: a checklist' (dry run with your auditor)"
  - ref: ISSA5000-2024
    title: "ISSA 5000, General Requirements for Sustainability Assurance Engagements"
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2025-01/IAASB-International-Standard-on-Sustainability-Assurance-ISSA-5000.pdf
    date: 2024-11
    access: full
    locator: "A262 (p. 117)"
  last_reviewed: 2026-10-16
  notes: "Idea. The IAASB item is the strongest source: a standard-setter acknowledging the question exists. ESGsource is a low-authority site and the page date is its live-update stamp. The financial-audit counterpart (AICPA practice aid on AI-operated controls; COSO guidance) is routed to controls-testing and specialists."

- id: assurance-sustainability-assurance-14
  title: AI-assisted digital tagging of sustainability statements by preparers, with the assurance opinion covering mark-up (idea)
  archetype: assurance
  module: sustainability-assurance
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "EU sustainability statements must be marked up in machine-readable form, and the limited-assurance opinion includes compliance with the mark-up requirement. Tagging many datapoints is repetitive and error-prone."
  solution: "Preparers may use AI to tag datapoints. The securities regulator says it will consult on tagging rules for sustainability statements and keep monitoring AI and its possible use in the European Single Electronic Format (ESEF). The assurance provider checks the mark-up as part of the opinion."
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: "Regulator commitment to monitor; no AI tagging result found"
    provenance: independent
    source_ref: ESMA-AWP-2027
  prerequisites:
  - "ESEF taxonomy for sustainability statements, which ESMA plans to consult on in Q1 2027 (ESMA-AWP-2027)."
  - "Practitioner able to test tagging, including with tools."
  risks_and_guardrails:
  - "The amended Accounting Directive text gives the limited-assurance opinion scope including compliance with the mark-up requirement (EU-OMNIBUS-2026, Article 2(12)(a), amended Article 34(1)(aa))."
  human_checkpoints:
  - "Assurance practitioner concludes on mark-up compliance as part of the opinion (EU-OMNIBUS-2026, Article 2(12)(a))."
  role_evolution: "Not described in the sources."
  evidence_grade: D
  sources:
  - ref: ESMA-AWP-2027
    title: "ESMA 2027 Annual Work Programme"
    publisher: ESMA
    type: regulator
    url: https://www.esma.europa.eu/sites/default/files/2026-09/ESMA22-50751485-1673_Annual_Work_Programme_2027.pdf
    date: 2026-09-28
    access: full
    locator: "Corporate reporting section (ESEF paragraph); 2027 outputs table (ESEF RTS consultation, Q1)"
  - ref: EU-OMNIBUS-2026
    title: "Directive (EU) 2026/470 amending Directives 2006/43/EC, 2013/34/EU, (EU) 2022/2464 and (EU) 2024/1760"
    publisher: European Parliament and Council (Official Journal)
    type: regulator
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202600470
    date: 2026-02-26
    access: full
    locator: "Article 2(12)(a) (amended Article 34(1)(aa) of Directive 2013/34/EU); Article 2(10) (Article 29f inserted: technological solutions report by 19 Mar 2028)"
  last_reviewed: 2026-10-16
  notes: "Idea and weak. ESMA's sentence is about AI in ESEF in general, not about assurance. The use case records that assurance covers mark-up and that the regulator is watching AI there; nothing links AI tagging to assurance work. The directive also asks the Commission to report by 19 Mar 2028 on technological solutions that let undertakings collect and exchange data in an automated way (new Article 29f of Directive 2013/34/EU); it does not mention AI."

- id: assurance-sustainability-assurance-15
  title: LLM drafting of ESRS and ISSB narrative by preparers, grounded in verified data (preparer side)
  archetype: assurance
  module: sustainability-assurance
  function: finance-accounting
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: "CSRD narrative is long and repetitive across frameworks and audiences. Teams want drafts quickly but fear unsupported statements that fail assurance."
  solution: "Preparers use LLMs to draft or adapt disclosure narrative from underlying data. Vendors say drafting is valuable only when each statement is tied to verified data, transparent sources and human review, so the text survives assurance."
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: "Vendor blogs and a sector site describe the practice; no time or error figure"
    provenance: vendor-published
    source_ref: IRIS-GENAI-2026
  prerequisites:
  - "Verified data and source documents the model can cite."
  - "A review step by someone who can check each figure against its source."
  risks_and_guardrails:
  - "Hallucinated facts and numbers read smoothly, so a quick human fact-check is not enough (IRIS-GENAI-2026)."
  - "Hallucination is a threat where accuracy is legally material; organisations are adding human review workflows and audit trails (ESGSOURCE-2026, 'AI in ESG Reporting')."
  human_checkpoints:
  - "Human reviewer checks each AI-drafted statement against sources before publication (IRIS-GENAI-2026; BRIINK-2025)."
  role_evolution: "A vendor argues AI frees ESG analysts from reading and drafting so they can interpret and plan, in a market short of sustainability talent (BRIINK-2025)."
  evidence_grade: C
  sources:
  - ref: IRIS-GENAI-2026
    title: "Generative AI in ESG Reporting: Drafting Narratives Without Losing Accuracy"
    publisher: IRIS Carbon
    type: vendor
    url: https://iriscarbon.com/blog/generative-ai-in-esg-reporting-drafting-narratives-without-losing-accuracy/
    date: 2026-08-14
    access: full
    locator: "Introduction; 'Why Just Fact-Check It Isn't Enough'; 'The Bottom Line'"
  - ref: BRIINK-2025
    title: "Will AI really change the game in ESG Reporting (or are we hallucinating)?"
    publisher: Briink
    type: vendor
    url: https://www.briink.com/post/will-ai-really-change-the-game-in-esg-reporting-or-are-we-hallucinating
    date: 2025-06-18
    access: full
    locator: "Opening sections"
  - ref: ESGSOURCE-2026
    title: "The State of ESG in 2026: What's Changed and What's Next"
    publisher: ESGsource
    type: community
    url: https://esgsource.com/state-of-esg-2026
    date: 2026-10-16
    access: full
    locator: "Section 'AI in ESG Reporting: Transforming the Practitioner's Toolkit'"
  last_reviewed: 2026-10-16
  notes: "Grade C because all sources are vendor or low-authority site claims. The ESGsource statement that a majority of sustainability executives use AI tools has no cited source and is not used as a figure. A FINRA statement quoted by IRIS Carbon relates to broker-dealers and is not relied on."
```

---

## 3. Module notes

### 3.1 Processes and key steps, with work types

Step names follow the ISSA 5000 contents list (ISSA5000-2024, contents and paragraph ranges). ISSA 5000 serves both limited and reasonable assurance; the EU is limited-assurance only after the Omnibus.

- **Acceptance and continuance** (paras 26–29): suitable criteria, preconditions, competence, ethics and independence under the IESSA. Work types: `review-assurance`, `expert-judgment`. Value-chain components bring extra independence rules, deferred to 1 Jul 2028 (IESBA-SUST-2024).
- **Scoping and planning** (paras 95–102): scope of information assured (all or part), materiality, group and value-chain components, use of experts. Work types: `expert-judgment`, `coordination-scheduling`.
- **Understanding the entity and its process to identify information to report** (Appendix 2 and risk assessment paras 103L–125): the materiality or double-materiality process, information system and controls. Work types: `review-assurance`, `research-synthesis`.
- **Risk assessment and response** (paras 103L–152): disclosure-level responses for limited assurance, assertion-level for reasonable. Work types: `expert-judgment`, `review-assurance`.
- **Evidence gathering** (paras 89–94; A225–A276): inquiry, analytical procedures, inspection, recalculation, evidence from suppliers and other practitioners (one-to-many reports, A130–A131), estimates and forward-looking information. Work types: `review-assurance`, `data-reporting`, `research-synthesis`.
- **Misstatements, representations, conclusion and report** (paras 153–212): `expert-judgment`, `document-production`.
- **Quality management and documentation** (paras 30–74): firm-approved technology, supervision and review. Work type: `review-assurance`.

### 3.2 Common pain points

- Scope barely changed in nine years: assurance stays on historical environmental data, with little coverage of forward-looking information or underlying systems (LEEDS-ASSURANCE-2026).
- Assurance providers differ: other providers apply ISAE 3000 (Revised) in 38% of cases against 94% for firms, so quality floors vary (IFAC-STATEPLAY-2026, key findings page).
- Estimates, assumptions and lack of verifiable data make forward-looking information hard to assure; users may read it as a guarantee (ACCA-ABMAG-2026).
- Value-chain data: the revised ESRS 1 allows estimates from proxies and caps what can be demanded of small suppliers; assurance has to assess the method (EU-ESRS-2026, ESRS 1 paras 65–66; EU-OMNIBUS-2026).
- Data quality is a concern for half of respondents in the Reuters Events preparer survey; 42% cite data volume as a CSRD challenge (TRI-SUSTAIN-2025).
- Talent: demand for ESG assurance skills exceeds supply, per the analyst (VERDANTIX-GQ-2024).
- Regulatory churn: EU scope cut, SEC rescission proposal, CARB timing and assurance details unsettled (EU-OMNIBUS-2026; DECHERT-SEC-2026; HL-CARB-PREVIEW-2026).

### 3.3 Metrics and benchmarks

| Metric | Value | What it measures (source's words) | Source |
|---|---|---|---|
| Companies obtaining some assurance, 2024 | 75% (51% in 2019) | "obtained some level of assurance", among 1,400 of the largest companies in 22 jurisdictions | IFAC-STATEPLAY-2026, p. 3 |
| Assurance that was limited, 2024 | 83% | share of assurance that was limited | IFAC-STATEPLAY-2026, p. 3 |
| Assurance engagements conducted by audit firms, 2024 | 59% (63% in 2019) | "assurance engagements conducted by firms" | IFAC-STATEPLAY-2026, p. 3 |
| Firms applying ISAE 3000 (Revised) vs other providers, 2024 | 94% vs 38% | share applying ISAE 3000 (Revised) | IFAC-STATEPLAY-2026, p. 3 |
| Assured subject matters, 2015 to 2023 | 517 to 2,294 (4.4 times) | subject matters identified and evaluated across 120 large listed companies | LEEDS-ASSURANCE-2026, p. 1–2 |
| Assurance quality scores (0 to 1), 2023 vs 2015 | nature 0.45 (0.31); extent 0.49 (0.36); scope 0.26 (0.24); overall 0.36 (0.28) | the study's eight-indicator index, by dimension | LEEDS-ASSURANCE-2026, pp. 2–3 |
| Audit-firm share and co-assurance, 2023 | over 55% (63% in 2019); 76% (65%) | firms' share of engagements; same firm audits financials and sustainability | LEEDS-ASSURANCE-2026, p. 3 |
| S&P 500 companies with assurance, 2023 data | 362 (340 in 2022); 87 from public-company auditors (74) | companies obtaining assurance or verification over certain metrics | CAQ-SP500-2025 |
| IFIAR members with mandatory assurance requirement | 61% in 2025 (21% in 2023); 47 members took part, 42-46 answered each question | respondents reporting laws or regulations requiring assurance | IFIAR-SATF-2026, p. 1 |
| IFIAR members that have inspected sustainability assurance engagements | 17% in 2025 (9% in 2023); 57% planning | respondents conducting inspections | IFIAR-SATF-2026, p. 1 |
| CSRD statements under limited assurance, FY2025 | "nearly all" of 196 statements; reasonable assurance uncommon | EY's review of 196 sustainability statements, mostly first-wave reporters | EY-CSRDBAROMETER-2026 |
| Preparers using AI, with and without assurance | 37% of those reporting Scope 1-3 with assurance; 22% without assurance | respondents using AI in reporting processes, Reuters Events 2025 Outlook | TRI-SUSTAIN-2025 |
| Practitioner AI risk concerns (financial audit, Moldova, n = 77) | unclear responsibility 87.3%; overreliance 87.3%; reduced skepticism 82.5% | respondents flagging each risk | ASE-CIKE-2025, "Basic content" |
| Audit-technology tools reported by the six largest networks | about 30% year-on-year increase in AI-enabled tools in 2025 | adjacent: audits generally, not sustainability | IFIAR-TTF-2026, p. 5 |

No AI-specific accuracy, override, error or inspection figure exists for sustainability assurance.

### 3.4 Guardrails and regulatory points

- **ISSA 5000.** Effective for engagements on information reported for periods beginning on or after 15 Dec 2026, or as at a date on or after it; early application permitted (ISSA5000-2024, para 15, p. 9). Covers limited and reasonable assurance, any framework (IAASB-EUFAQ-2025, Q1).
- **Replacement of older standards.** ISAE 3000 (Revised) and ISAE 3410 no longer apply to sustainability engagements after the effective date for those claiming IAASB compliance, unless a jurisdiction requires a local equivalent (IAASB-ISSA5000FAQ-2025, Q1–Q4; IAASB-ENEWS-2025).
- **Adoption (IAASB list, Sep 2026).**
  - Adopted: Australia (ASSA 5000, periods beginning on or after 1 Jan 2025), Canada (CSSA 5000, periods beginning on or after 15 Dec 2027), the UK (ISSA (UK) 5000), Hong Kong, New Zealand, South Africa, Malaysia and others.
  - In progress: Germany, India, Singapore, South Korea and the US. In the US the AICPA ASB is converging its attestation standards with ISSA 5000; the PCAOB does not adopt IAASB standards.
  - Several European jurisdictions (for example France, Spain and the Netherlands) are listed as dependent on the Commission's delegated act (IAASB-ISSA5000PAGE-2026).
- **IESSA ethics standard.** Same effective date, with value-chain-component independence provisions from periods beginning on or after 1 Jul 2028 (IESBA-SUST-2024). Technology provisions: R5320.11 (decide if output is appropriate), 5320.11 A1 (tool testing, firm oversight, input quality), 5300.6 A2 (data and tool threats), 5120.12 A2 (automation bias) (IESBA-IESSA-2025). IT systems services that implement sustainability reporting software create a self-review threat; prohibited for public-interest entities if the threat arises (5606.4 A3; R5606.6).
- **ISSA 5000 technology text.** A91 (overreliance on automated tools impedes critical assessment), A96–A98 (technological resources; competence in tools), A231 (procedure design and manual versus automated), A249 (real-time tools), A262 (general IT controls maintain integrity) (ISSA5000-2024).
- **EU.**
  - Directive (EU) 2026/470: scope above EUR 450 million turnover and over 1,000 average employees; Member States transpose Articles 1–3 by 19 Mar 2027; limited-assurance standards by delegated act by 1 Jul 2027 (Article 1(3)); the requirement to adopt reasonable-assurance standards is removed (EU-OMNIBUS-2026, recitals 4–5, Article 1(3), Article 5).
  - Companies outside the new scope fall out from financial years starting 1 Jan 2027; Member States may exempt them for financial years beginning 1 Jan 2025 to 31 Dec 2026 (EU-OMNIBUS-2026, recital 31).
  - Revised ESRS: in force 10 Nov 2026, apply from financial years beginning 1 Jan 2027; for 2026 years entities may choose previous ESRS, revised ESRS or previous ESRS with certain reliefs (EU-ESRS-2026; WPK-ESRS-2026).
  - CEAOB technical advice, 25 Sep 2026; the Commission is expected to consult this autumn (CEAOB-TA-2026; ACCA-EUPA-2026).
- **US.**
  - SB 253: first Scope 1 and 2 report due 10 Nov 2026; first-year options include reporting data held on 5 Dec 2024 or a no-data statement; initial regulation approved by CARB on 26 Feb 2026 (HL-CARB-2026-03), revised draft published 27 Jul 2026 (HL-CARB-ROADMAP-2026). A 13 Oct 2026 headline says the Office of Administrative Law approved it (HL-OAL-2026, headline only).
  - The statute directs limited assurance for 2026 Scope 1 and 2 reports, but CARB's initial regulation omits it and CARB plans to add assurance later; 2027 draft text on assurance was previewed 21 Jul 2026 (WINSTON-CARB-2026; HL-CARB-PREVIEW-2026).
  - SEC: proposed rescission of the 2024 climate rules on 29 May 2026; Eighth Circuit case in abeyance since 12 Sep 2025 (DECHERT-SEC-2026).
- **Regulators on AI.** IFIAR's 2026 technology report asks firms to govern technology under ISQM 1 and keep auditors in control; it has no sustainability content (IFIAR-TTF-2026). The IAASB's technology quality-management roundtables (243 participants) have no sustainability content (IAASB-TQM-2026). A keyword scan of the FRC's March 2026 GenAI guidance (a copy fetched by another analyst in this session) found no "sustainab" or "ISAE" hits; it is not in the source list.

### 3.5 Frontier signals (dated)

- 2026-10-05: IAASB says Technology Quality Management guide 1 is anticipated in November 2026 subject to 28 Oct approval; it plans ISSA 5000 FAQs on general matters and a joint IAASB-IESBA FAQ in Q4 2026; the "other assurance engagements" information-gathering report is due at the December 2026 meeting; a consultation on the 2028–2031 strategy is expected early 2027 (IAASB-ENEWS-2026).
- 2026-07: IAASB Technology Catalog v3 lists sustainability assurance and technology as "continue monitoring", priority Low (IAASB-TECHCAT-2026, Theme 10(a)).
- 2026-09-25: CEAOB advice delivered; delegated act due by 2027-07-01 (CEAOB-TA-2026; EU-OMNIBUS-2026).
- 2026-09-21: revised ESRS published; apply from FY2027 (EU-ESRS-2026).
- 2026-09-28: ESMA says it will consult on tagging rules for sustainability statements (Q1 2027) and monitor AI in ESEF (ESMA-AWP-2027).
- 2026-06-09: IFIAR reports inspection programmes for sustainability assurance are at an early stage, with most respondents planning them (IFIAR-SATF-2026).
- 2026-07: California CARB previews 2027 assurance text; rulemaking package expected in the fall (HL-CARB-PREVIEW-2026).
- 2026-06-12: Workiva launches a sustainability disclosure agent aimed at gaps before assurance (ESGNEWS-WORKIVA-2026).
- By 2028-03-19: Commission report on technological solutions for automated sustainability data exchange (EU-OMNIBUS-2026, Article 2(10), new Article 29f).
- 2026-12-15: ISSA 5000 and IESSA effective (ISSA5000-2024; IESBA-SUST-2024).
- 2026-07: ICAEW says the FRC is working on a voluntary sustainability assurance register that could launch later in 2026 (ICAEW-VIEW-2026).

### 3.6 Workforce and role effects

- ISSA 5000 is designed for both professional accountants and non-accountant assurance practitioners (IAASB-ISSA5000PAGE-2026); in 2024, audit firms performed 59% of engagements (IFAC-STATEPLAY-2026).
- Skills: the literature expects data-analytics literacy and the ability to challenge AI limits (MDPI-SUSAI-2026, section 7.2). EY and PwC run sustainability training programmes in response to a talent shortage; neither is described as AI-related (VERDANTIX-GQ-2024).
- ICAEW's audit director says members, especially mid-tier and smaller firms, face many AI tool providers and need to choose investments for their scale, and that sustainability information means more work with non-accountant specialists (ICAEW-VIEW-2026).
- No source measures changes in team size, staffing pyramid or fees for sustainability engagements.

### 3.7 Objections and concerns practitioners raise

- Overreliance and automation bias: named in the standards themselves (ISSA5000-2024, A91; IESBA-IESSA-2025, 5120.12 A2).
- Accountability and skepticism: in the Moldova survey, 87.3% flagged unclear responsibility for decisions and 82.5% reduced professional skepticism (ASE-CIKE-2025).
- Hallucination and traceability: vendors stress that a number without a traceable source cannot be verified by an auditor (WATERSHED-AI-2026; IRIS-GENAI-2026).
- Explainability and bias in black-box models (MDPI-SLR-2026, section 4.5).
- Assurance used symbolically can give false confidence if it ignores systems and forward-looking information (LEEDS-ASSURANCE-2026, p. 4).
- Independence when firms sell or implement reporting software (IESBA-IESSA-2025, 5606.4 A3).
- Regulatory uncertainty and thin supply of skills (VERDANTIX-GQ-2024; EU-OMNIBUS-2026).

### 3.8 Interview probes

1. On your last limited-assurance sustainability engagement, which procedures used automated tools or AI, who approved the tool, and where is that recorded in the file?
2. When a client uses AI to draft narrative, classify Scope 3 spend or fill value-chain gaps, what evidence do you ask for (lineage, prompts, model versions, assumptions), and what has your team rejected?
3. Does your firm or network sell, build or implement sustainability-reporting software for clients you also assure? How do you apply the IESSA's IT-systems-services rules (5606) in practice?
4. Do the agent platforms your firm rolled out for financial audit reach sustainability engagements yet? If not, what would you need to see (pilot results, regulator feedback) before they do?
5. How are you preparing for the first ISSA 5000 engagements from December 2026: what changes in scoping, the entity's materiality process, and evidence from value-chain components?

---

## 4. Routed to other modules

- **planning-risk-assessment / substantive-testing / quality-management:** EY's agentic AI release covering 130,000 assurance professionals and 160,000 audit engagements; EY says AI is embedded in all audit phases now and it expects end-to-end support by 2028. The text opened is audit-only (EY-MENAPR-2026, 20 Apr 2026).
- **quality-management:** IFIAR's April 2026 report on technology in audits: networks reported about 30% growth in AI-enabled tools in 2025 and agentic AI plans; asks for ISQM 1 monitoring and auditor control (IFIAR-TTF-2026). IAASB technology quality-management roundtables (243 participants) and the planned guide series (IAASB-TQM-2026; IAASB-ENEWS-2026).
- **substantive-testing:** IAASB's ISA 330/500/520 exposure drafts (comments due 15 Dec 2026), referenced in IAASB-ENEWS-2026.
- **assurance-over-ai (separate module):** The IAASB's item on AI assurance (Technology Catalog 10(b): firms starting to offer AI assurance engagements; IAASB-TECHCAT-2026). A summary of an FT report (3 Jun 2025) says the Big Four are developing services to verify AI tools, building on ESG assurance experience (FT-AIASSURE-2025).
- **acceptance-independence:** IESSA 5606 and 5400.20 A3 on software and management responsibility (IESBA-IESSA-2025). The landscape's AICPA SOC tool-provider ethics article may transfer the same reasoning.
- **controls-testing / specialists:** assurance over a client's AI-operated controls (landscape R20, R24; not re-opened here).
- **Preparer-side sustainability reporting (outside the assurance archetype):** Workiva, Watershed, IRIS Carbon, Briink and PwC Germany tool claims (use cases 08, 09, 11, 15) are recorded here for their effect on assurance; they belong in a corporate-reporting or sustainability-function archetype if one is researched.

---

## 5. Sources

Access: `full` = opened and read (some keyword-scanned only where noted). Refs reuse the landscape file's key where it is the same document.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ISSA5000-2024 | ISSA 5000, General Requirements for Sustainability Assurance Engagements | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2025-01/IAASB-International-Standard-on-Sustainability-Assurance-ISSA-5000.pdf | 2024-11 | full |
| IAASB-ISSA5000PAGE-2026 | Understanding the ISSA 5000 (focus page with jurisdictional adoption, updated Sep 2026) | IAASB | standard-setter | https://www.iaasb.org/focus-areas/sustainability-assurance | 2026-09 | full |
| IAASB-ISSA5000FAQ-2025 | FAQ: Applicability of ISSA 5000, ISAE 3000 (Revised) and ISAE 3410 | IAASB (staff) | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2025-08/IAASB-ISSA-5000-FAQ-Applicability-ISAE-3000-3410.pdf | 2025-08 | full |
| IAASB-EUFAQ-2025 | FAQ: Relevance of ISSA 5000 to Assurance on Sustainability Reports in the EU | IAASB (staff) | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2025-11/IAASB-ISSA-5000-FAQ-Relevant-to-European-Union.pdf | 2025-11 | full |
| IAASB-IMPLGUIDE-2025 | ISSA 5000 Implementation Guide | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2025-11/IAASB-ISSA-5000-Implementation-Guide-Sustainability-Assurance.pdf | 2025-01 | full (keyword-scanned; cover dated Jan 2025) |
| IAASB-MATFAQ-2026 | FAQ: The Application of Materiality under ISSA 5000 | IAASB (staff) | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-06/IAASB-ISSA-5000-Sustainability-Frequently-Asked-Questions-FAQ-Materiality.pdf | 2026-06 | full (opening pages and resource list read) |
| IAASB-JOINTFAQ-2025 | Joint IAASB-IESBA FAQs: Sustainability Assurance Engagements, ISSA 5000 and the IESBA Code | IAASB and IESBA (staff) | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2025-06/Joint-IAASB-IESBA-FAQs-on-Sustainability-Assurance.pdf | 2025-06 | full (keyword-scanned) |
| IAASB-TECHCAT-2026 | Technology Catalog, Version 3 | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-07/IAASB-Technology-Catalog-of-Issues-Proposed-Actions.pdf | 2026-07 | full (Theme 10 read) |
| IAASB-ENEWS-2025 | IAASB eNews April 2025 | IAASB | standard-setter | https://www.iaasb.org/news-events/2025-04/iaasb-enews-april-2025 | 2025-04-14 | full |
| IAASB-ENEWS-2026 | IAASB eNews October 2026 | IAASB | standard-setter | https://www.iaasb.org/news-events/2026-10/iaasb-enews-october-2026 | 2026-10-05 | full |
| IAASB-TQM-2026 | Technology Quality Management Roundtables: Outcomes and Next Steps | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-02/IAASB-Technology-Quality-Management-Roundtables-Feedback.pdf | 2026-02 | full |
| IAASB-WEBINAR2-2025 | ISSA 5000 in Focus webinar 2: Engagement Planning, Risk Assessment and Response (slides) | IAASB | conference | https://ifacweb.blob.core.windows.net/publicfiles/2025-10/IAASB-ISSA-5000-in-Focus-Webinar-2-Engagement-Planning-Risk-Assessment.pdf | 2025-10 | full (keyword-scanned: no AI or technology content) |
| IESBA-IESSA-2025 | IESSA and Revisions to the Code, Final Pronouncement (updated version) | IESBA | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2025-08/IESSA%20and%20Revisions%20to%20the%20Code%20Final%20Pronouncement%20%28updated%20082525%29.pdf | 2025-08 | full (technology and non-assurance-service sections read) |
| IESBA-SUST-2024 | IESBA Sustainability project page (Dec 2024 meeting highlights: effective dates) | IESBA | standard-setter | https://www.ethicsboard.org/consultations-projects/sustainability | 2024-12 | full |
| EU-OMNIBUS-2026 | Directive (EU) 2026/470 (Omnibus I) | European Parliament and Council | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202600470 | 2026-02-26 | full |
| EU-ESRS-2026 | Commission Delegated Regulation (EU) 2026/1563 (simplified ESRS) | European Commission | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601563 | 2026-09-21 | full (keyword-read) |
| CEAOB-TA-2026 | CEAOB technical advice: standard for limited assurance on sustainability reporting | CEAOB (via European Commission) | regulator | https://finance.ec.europa.eu/document/download/abd3fbf5-e2e1-4eb2-8af8-8d8fd5803303_en?filename=260925-ceaob-technical-advice-limited-assurance-sustainability-reporting_en.pdf | 2026-09-25 | full (opening pages and keyword scan) |
| ESMA-AWP-2027 | ESMA 2027 Annual Work Programme | ESMA | regulator | https://www.esma.europa.eu/sites/default/files/2026-09/ESMA22-50751485-1673_Annual_Work_Programme_2027.pdf | 2026-09-28 | full (keyword-read) |
| IFIAR-SATF-2026 | Public Factsheet on the 2025 Sustainability Survey Results | IFIAR | regulator | https://www.ifiar.org/?wpdmdl=20061 | 2026-06-09 | full (via text mirror) |
| IFIAR-TTF-2026 | Use of technology in audits: Innovation and audit quality 2026 | IFIAR | regulator | https://www.ifiar.org/?wpdmdl=19893 | 2026-04-20 | full (via text mirror) |
| WPK-CEAOB-2026 | Standard des CEAOB zur Prüfung von Nachhaltigkeitsberichten mit begrenzter Sicherheit | Wirtschaftsprüferkammer (WPK) | professional-body | https://www.wpk.de/neu/technical-advice-standard-for-limited-assurance-on-sustainability-reporting/ | 2026-10-06 | full |
| WPK-ESRS-2026 | Delegierte Verordnungen zu den überarbeiteten ESRS und zum VS im EU-Amtsblatt veröffentlicht | Wirtschaftsprüferkammer (WPK) | professional-body | https://www.wpk.de/neu/delegierte-verordnungen-zu-den-ueberarbeiteten-esrs-und-zum-vs-im-eu-amtsblatt-veroeffentlicht/ | 2026-09-23 | full |
| ACCA-EUPA-2026 | EU updates (Europe public affairs) | ACCA | professional-body | https://www.accaglobal.com/sg/en/professional-insights/public-affairs/europe-public-affairs.html | 2026-10 | full |
| ACCA-ABMAG-2026 | Get ready for ISSA 5000 (April 2026 issue) | ACCA, Accounting and Business | professional-body | https://abmagazine.accaglobal.com/global/articles/2026/apr/practice/get-ready-for-issa-5000.html | 2026-04 | full |
| ICAEW-VIEW-2026 | 2026: AI and sustainability assurance on the way (Alex Russell) | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/jul-2026/2026-ai-and-sustainability-assurance | 2026-07 | full |
| CAQ-SP500-2025 | S&P 500 Companies' Sustainability Reporting and Assurance Practices | Center for Audit Quality | professional-body | https://www.thecaq.org/aia-sp500-sustainability-reporting-assurance-2025 | 2025-07-21 | full |
| IFAC-STATEPLAY-2026 | The State of Play: Sustainability Disclosure and Assurance, six-year trends 2019-2024 | IFAC and AICPA & CIMA | survey | https://ifacweb.blob.core.windows.net/publicfiles/2026-07/IFAC-State-of-Play-Sustainability-Disclosure-Assurance-2019-2024.pdf | 2026-06 | full |
| TRI-SUSTAIN-2025 | Future-proofing sustainability reporting: Solutions to AI and data challenges for CSRD compliance (Reuters Events 2025 Outlook) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/sustainability-reporting-solutions-csrd-compliance | 2025-06 | full |
| LEEDS-ASSURANCE-2026 | The State of Global Sustainability Assurance and Implications for ISSA 5000 (research snapshot) | Leeds University Business School and Univ. of the Witwatersrand, for the IAASB | academic | https://ifacweb.blob.core.windows.net/publicfiles/2026-07/The-State-of-Global-Sustainability-Assurance-Finding-Snapshot.pdf | 2026-07 | full |
| MDPI-SUSAI-2026 | Artificial Intelligence in Sustainability Assurance: Accounting Challenges, Audit Risks and a Conceptual Framework for ESG Verification (preprint) | Preprints.org (MDPI) | academic | https://www.preprints.org/manuscript/202607.1236/v1 | 2026-07 | full (via text mirror; published MDPI version blocked) |
| MDPI-SLR-2026 | AI and Data Analytics in Sustainable Financial Reporting and ESG Disclosure: A Systematic Literature Review | Sustainability 18(11), 5393 | academic | https://www.mdpi.com/2071-1050/18/11/5393 | 2026-05-26 | full (via text mirror) |
| LI-JETA-2024 | Using Artificial Intelligence in ESG Assurance | Journal of Emerging Technologies in Accounting 21(2) | academic | https://digitalcommons.mtu.edu/michigantech-p2/1154 | 2024-10 | full (abstract page) |
| SWISSTEXT-2025 | Detecting Greenwashing Hints in ESG Reports | TU Berlin, SwissText 2025 | academic | https://www.swisstext.org/wp-content/uploads/2025/05/Detecting-Greenwashing-Hints-in-ESG-Reports-Linguistic-and-Claim-Analysis-in-Traffic-Related-Emissions-Disclosures.pdf | 2025-05 | full |
| ARXIV-SSKG-2026 | SSKG Hub: LLM-Empowered Sustainability Standards Knowledge Graphs | arXiv 2603.00669 | academic | https://arxiv.org/abs/2603.00669 | 2026-02-28 | full (abstract) |
| ASE-CIKE-2025 | The Application of AI in Auditing Sustainability Reports: Between Ethical Challenges and Efficiency | CIKE conference, Chisinau | conference | https://conferences.ase.ro/?p=875 | 2025-09-26 | full |
| EY-CSRDBAROMETER-2026 | EY CSRD Barometer 2026 | EY | firm | https://www.ey.com/en_gl/technical/csrd-technical-resources/ey-csrd-barometer-2026 | 2026-05-29 | full (summary page; date from page metadata) |
| EY-MENAPR-2026 | EY's global launch of agentic AI in Assurance (MENA press release) | EY | firm | https://www.ey.com/en_ae/newsroom/2026/04/ey-s-global-launch-of-agentic-ai-in-assurance-to-redefine-audit-experience-for-menaclients | 2026-04-20 | full |
| VERDANTIX-GQ-2024 | Verdantix Green Quadrant Benchmark Highlights Leading ESG & Sustainability Assurance Vendors | Verdantix | vendor | https://www.verdantix.com/insights/press-release/verdantix-green-quadrant-benchmark-highlights-leading-esg-sustainability-assurance-vendors | 2024-11-11 | full |
| WATERSHED-AI-2026 | Sustainability AI in 2026: what works, what doesn't | Watershed | vendor | https://watershed.com/blog/sustainability-ai-in-2026-what-works-what-doesnt-and-why-the-difference-matters | 2026-06-10 | full |
| BRIINK-2025 | Will AI really change the game in ESG Reporting (or are we hallucinating)? | Briink | vendor | https://www.briink.com/post/will-ai-really-change-the-game-in-esg-reporting-or-are-we-hallucinating | 2025-06-18 | full |
| IRIS-GENAI-2026 | Generative AI in ESG Reporting: Drafting Narratives Without Losing Accuracy | IRIS Carbon | vendor | https://iriscarbon.com/blog/generative-ai-in-esg-reporting-drafting-narratives-without-losing-accuracy/ | 2026-08-14 | full |
| ESGNEWS-WORKIVA-2026 | Workiva Launches AI Disclosure Agent to Help Companies Close Sustainability Reporting Gaps Earlier | ESG News | press | https://esgnews.com/workiva-launches-ai-disclosure-agent-to-help-companies-close-sustainability-reporting-gaps-earlier/ | 2026-06-12 | full |
| ESGPOST-WORKIVA-2026 | Workiva launches AI-powered agent to automate sustainability disclosure analysis | ESG Post | press | https://esgpost.com/workiva-launches-ai-powered-agent-to-automate-sustainability-disclosure-analysis/ | 2026-06-12 | full |
| ITBRIEF-WORKIVA-2026 | Workiva launches AI agents for reporting & compliance | IT Brief UK | press | https://itbrief.co.uk/story/workiva-launches-ai-agents-for-reporting-compliance | 2026-07-30 | full |
| KNOWESG-PWCAI-2025 | AI-Powered Sustainability: PwC's New Tool Changes the Game for CSRD | KnowESG | press | https://knowesg.com/tech/ai-powered-sustainability-pwcs-new-tool-changes-the-game-for-csrd-06062025 | 2025-06-06 | full (via text mirror) |
| ESGSOURCE-2026 | The State of ESG in 2026: What's Changed and What's Next | ESGsource | community | https://esgsource.com/state-of-esg-2026 | 2026-10-16 | full (live-updated page; low authority) |
| HL-CARB-2026-03 | California Air Resources Board unanimously approves initial climate disclosure regulation | Hogan Lovells | press | https://www.hoganlovells.com/en/publications/california-air-resources-board-unanimously-approves-initial-climate-disclosure-regulation | 2026-03-04 | full |
| HL-CARB-PREVIEW-2026 | California Air Resources Board previews 2027 GHG reporting requirements while 2026 reporting deadline remains delayed until Q4 | Hogan Lovells | press | https://www.hoganlovells.com/en/publications/california-air-resources-board-previews-2027-ghg-reporting-requirements-while-2026-reporting | 2026-07-22 | full |
| HL-CARB-ROADMAP-2026 | California Air Resources Board provides a roadmap: 2026 revised initial regulations open for public comment | Hogan Lovells | press | https://www.hoganlovells.com/en/publications/california-air-resources-board-provides-a-roadmap | 2026-07-29 | full |
| HL-OAL-2026 | Breaking: Office of Administrative Law approves CARB's initial regulation implementing SB 253 (headline on Hogan Lovells listing) | Hogan Lovells | press | https://www.hoganlovells.com/en/publications/california-air-resources-board-unanimously-approves-initial-climate-disclosure-regulation | 2026-10-13 | search-only (headline seen on a page opened; article itself not opened) |
| WINSTON-CARB-2026 | CARB advances climate disclosure rules as Ninth Circuit appeal continues | Winston & Strawn (now Winston Taylor) | press | https://www.winstontaylor.com/insights/carb-advances-climate-disclosure-rules-as-ninth-circuit-appeal-continues | 2026-01-29 | full |
| DECHERT-SEC-2026 | SEC Proposes to Rescind Climate-Related Disclosure Rules | Dechert | press | https://www.dechert.com/knowledge/onpoint/2026/6/sec-proposes-to-rescind-climate-related-disclosure-rules.html | 2026-06-01 | full |
| FT-AIASSURE-2025 | Big Four accountancy firms poised to enter burgeoning AI Assurance market (summary of FT article) | Privacy Newsfeed (summary of Financial Times) | press | https://www.freevacy.com/news/financial-times/big-four-accountancy-firms-poised-to-enter-burgeoning-ai-assurance-market/6428 | 2025-06-03 | full (summary only; FT article paywalled) |
| KPMG-JOBAU-2026 | Manager, ESG Assurance (Sydney) job posting | KPMG Australia (via Simplify Jobs) | job-posting | https://simplify.jobs/p/2f5797de-76c6-43ef-9a21-5502835620ef/Manager--ESG-Assurance | 2026-06-04 | full |
| EY-JOBMY-2026 | Assurance ESG, Manager/Senior Manager (Kuala Lumpur) job posting | EY | job-posting | https://careers.ey.com/ey/job/Kuala-Lumpur-Assurance-ESG,-Manager-Senior-Manager-Fede-50490/1412710033/ | 2026-10-03 | full |

---

## 6. Gaps

- **No firm primary source for sustainability-specific AI.** Deloitte Omnia ESG and KPMG's NLP and ML greenwashing detection appear only in the Verdantix press release (2024). The Verdantix report is paywalled. No EY, PwC, Deloitte or KPMG release found that names AI in sustainability assurance. Searches for DNV, Bureau Veritas, ERM CVS and SGS returned no AI content.
- **No quality evidence.** No error, override, parallel-run, inspection or enforcement result for AI in sustainability assurance. No regulator inspection findings for sustainability assurance found at all (AFM, H3C, FRC, CEAOB searches returned only background). IFIAR's survey is about regime status, not findings.
- **Practitioner survey caveat.** The only practitioner survey on AI in sustainability assurance (ASE-CIKE-2025, n = 77, Moldova) reports its percentages for AI in financial audit; the abstract's efficiency and greenwashing-detection claims have no figures in the text read.
- **No podcasts, one low-authority community source, one conference paper.** ICAEW and IAASB podcast searches returned nothing relevant. Reddit and LinkedIn were not used. A Korean Institute of CPAs forum on ISSA 5000 turned up only in a search snippet and had no AI content.
- **Blocked or not reached.**
  - PwC global sustainability reporting survey pages (403). A search extract said AI use for reporting rose to 28% from 11% and that PwC's March 2026 survey cited early assurance engagement by 37% of reporters; neither is verified or used.
  - Akin Gump's note on the CARB delay (403), covered instead by Hogan Lovells.
  - The ScienceDirect paper by Gu, Dai and Vasarhelyi on satellite images and GHG assurance (captcha); the MDPI-published version of the AI in sustainability assurance paper (403); an ESG Today column by a Workiva executive (403).
  - The full Hogan Lovells 13 Oct 2026 article on OAL approval (only the headline was seen).
- **Landscape discrepancy.** The landscape describes the MDPI paper as proposing graded reliance ceilings, non-delegable judgments and tool lineage. The preprint read for this note does not contain those terms; the published version may differ.
- **Partly read.** The Implementation Guide, joint FAQ, materiality FAQ, ISSA 5000 and the CEAOB advice were read at the cited paragraphs and keyword-scanned, not end to end. The revised ESRS annex was read at the cited paragraphs.
- **Secondary-only points.** The FRC's voluntary sustainability assurance register (ICAEW-VIEW-2026); the AICPA ASB convergence project (IAASB focus page); the ESRS option for 2026 years (WPK-ESRS-2026, confirmed only for the application date in the OJ text).
- **Not checked.** ISSA (UK) 5000 on the FRC site; the FRC's March 2026 GenAI guidance itself (a keyword scan of another analyst's copy found no sustainability references, and it is not cited as a source); wave-1 company treatment in individual Member States; whether any assurance firm's engagement letters or reports mention AI use on sustainability engagements.
- **Date notes.** The KPMG posting shows "6/4/2026" on the aggregator and is read here as 4 June. ISSA 5000 was issued in Nov 2024 per the IAASB; the CEAOB paper says Dec 2024 and the file path says Jan 2025. The IESSA file is the updated version (Aug 2025). The EY barometer date is from page metadata; the ESGsource page date is a live-update stamp. IFIAR's factsheet is dated 9 Jun 2026 inside the PDF and 8 Jun on the news page.

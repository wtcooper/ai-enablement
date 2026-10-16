# Deep dive: assurance / soc-attestation / practice

- **Archetype:** assurance
- **Module:** soc-attestation: SOC 1 / SOC 2 / SOC 3 and ISAE 3402 / ISAE 3000 service-organization examinations and other attestation engagements, end to end, plus compliance-automation platforms and quality concerns about commoditized SOC 2 (individual control tests are covered by the separate controls-testing module)
- **Angle:** practice: what service auditors, compliance platforms and service organizations actually do with AI
- **Prepared:** 2026-10-16
- **Inputs:** `research/runs/wave1/landscape-assurance.md`, `research/briefs/templates/vocabulary.md`. Controls-testing pilot files were consulted only for SOC leads (EY conference PDF, JofA articles, KPMG UK report).
- **Method note:** pages were fetched with `curl` (and `pdftotext` for PDFs); one vendor release (Drata) was read through a text mirror because the host returned 403. The web-search allowance ran out partway through, so later work relied on direct fetches of known pages, sitemaps and job-board feeds. Every source below was opened and read unless the Gaps section says otherwise. Quotations are kept under 25 words; most are paraphrased.

---

## 1. Summary

- **22 candidate use cases:** 1 at grade A, 12 at B, 8 at C and 1 at D (an idea). 16 are rated in-production, 4 piloting, 1 announced and 1 emerging.
- **The only published firm-side measurements come from one firm.**
  - KPMG UK reports about 18% less testing time on recent controls assurance engagements (SOC 1, SOC 2, ISAE 3402, ISAE (UK) 3000) using Clara AI, Microsoft 365 Copilot and DataSnipper, and about 15% on one team using DataSnipper alone (KPMGUK-CONTROLS-2026).
  - Both figures are self-reported, with no baseline or engagement count, and come from a tool bundle, so they cannot be credited to AI alone.
- **No independent measure of AI quality in SOC work was found.** There is no error rate, override rate, parallel-run result, peer review finding or inspection outcome tied to AI use in a SOC examination. No peer-review statistics on SOC 2 practices were found.
- **Adoption is concentrated on preparation and administration, not on opinion-forming judgement.**
  - At the 2026 EY SOC conference, a live poll found AI used for evidence collection (63%), updating the Section 3 description (45%), drafting management responses to deviations (41%) and project management (29%) (EY-SOC-2026). It is a poll of attendees, not a survey.
  - Service-auditor-side uses described by named firms are walkthrough preparation, transcription into flowcharts, evidence extraction, report review, acceptance and scheduling (KPMGUK-CONTROLS-2026, LINFORD-ASSURE-2026).
- **The service model is contested, and the contest is about quality and independence rather than technology.**
  - Dozens of tool vendors market fast, cheap SOC 2 and some route clients to networks of audit firms; the AICPA SOC 2 Working Group chair says speed may come at the expense of quality and objectivity (JOFA-FAST-2026).
  - AICPA responses in 2026: ethics staff guidance on tool-provider arrangements (6 Apr), a Peer Review Board reviewer alert (May, with staff outreach planned from 1 June), and a notice that it is looking into allegations about an unnamed compliance vendor (JOFA-SOCETH-2026, JOFA-PRB-2026, AICPA-SOC-2026).
  - In March 2026 an anonymous whistleblower alleged that the Delve platform produced fake evidence and pre-written auditor conclusions; Delve denies it. Named customers then moved to another platform and independent auditors (TECHCRUNCH-DELVE-2026, TECHCRUNCH-LITELLM-2026, TECHCRUNCH-CONTEXT-2026).
- **Two business models are visible.**
  - Auditor-led firms pair a licensed CPA firm with AI tooling (A-LIGN's A-SCEND, Thoropass Assurance, KPMG UK).
  - Platform-led vendors (Vanta, Drata, Secureframe, Comp AI, Oneleet) automate readiness and pass the examination to partner audit firms; Vanta says more than 100 audit firms work with it (VANTA-AUDITORS-2026).
  - A specialist firm argues AI made compliance cheaper but not assurance (LINFORD-ASSURE-2026).
  - The sources contain no firm-published fee change. Price evidence is limited to a lead-generation directory (SOC2AUDITORS-COST-2026).
- **Standards are moving but are not settled.**
  - The AICPA's TQA 9561 (11 Sep 2026) says AI creates no separate SOC model and no new criteria; relevance depends on how the service organization uses AI (SDOWNS-TQA9561-2026).
  - A KPMG webcast page (22 Sep 2026) says forthcoming Trust Services Criteria changes are expected to restructure the criteria and address emerging technology including AI (KPMG-SOC-2026). A Cloud Security Alliance note (30 Aug 2026) says the AICPA has published no AI-specific criteria and no exposure draft (CSA-SOC2-2026). The two statements are reconcilable only if "forthcoming" means unpublished; flagged as unresolved.
- **Thin or absent:** ISAE 3402 and ISAE 3000 practice outside KPMG UK; bridge letters; Big Four product detail for SOC; SOC specialist firms' own AI use (Schellman and BARR publish none that was found); academic evidence; audit-firm job postings (only vendor postings were found).

---

## 2. Use cases

Evidence grades and maturity follow the vocabulary. Where a figure came from a vendor page or testimonial, `provenance` says `vendor-published`. Entries 10, 11 and 14 to 17 sit on the service-organization or report-user side of the SOC ecosystem, so their `function` is `risk-compliance-legal`.

```yaml
- id: assurance-soc-attestation-01
  title: Control-wording review and walkthrough preparation with firm-built AI agents
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Walkthroughs with control owners take many meetings, and control descriptions of uneven quality lead to repeated follow-up requests.
  solution: KPMG UK describes custom agents in its in-house Clara AI that review control wording, list the control attributes and walkthrough questions, draft agendas, and give a score for the control description against what a good control looks like. The firm calls the score decision support, not a conclusion.
  outcomes:
  - {lever: experience, description: KPMG UK says the agents reduce the number of meetings and the time needed from control owners and cut follow-up requests; no figure is given, figure: none published, measures: n/a (qualitative statement), provenance: self-reported, source_ref: KPMGUK-CONTROLS-2026}
  prerequisites:
  - Secure, firm-operated AI environment (Clara AI) and, 'where permitted', client permission to use it on engagement material
  - Control descriptions or walkthrough material from the service organization
  risks_and_guardrails:
  - The score is framed as decision support and not as the auditor's conclusion (KPMGUK-CONTROLS-2026)
  - Use depends on client permission for AI use on engagement information (KPMGUK-CONTROLS-2026)
  human_checkpoints:
  - The auditor runs the walkthrough and decides on control design
  - The auditor decides what to do with the control-description score
  role_evolution: Control owners are asked for fewer and shorter meetings, and the engagement team arrives with a structured question list (KPMGUK-CONTROLS-2026).
  evidence_grade: B
  sources:
  - {ref: KPMGUK-CONTROLS-2026, title: 'Reimagining Controls Assurance with AI: Latest Insights for Leaders (SOC 1, SOC 2, ISAE 3402, ISAE (UK) 3000, AAF 01/20, AAF 05/20)', publisher: KPMG in the UK, type: firm, url: 'https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf', date: 2026-01, access: full, locator: 'p.5, ''KPMG Clara AI: SOC custom agents'' and ''Control test plan designer'' panels'}
  last_reviewed: '2026-10-16'
  notes: The document does not say how many engagements use each agent. The 'in-production' rating rests on the firm's statement that it uses these agents on assurance engagements.
- id: assurance-soc-attestation-02
  title: Walkthrough transcription into flowcharts and a draft Test of Design
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - document-production
  - research-synthesis
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Walkthrough notes must be turned into process maps and test-of-design documentation after each meeting, and follow-up questions follow when notes are incomplete.
  solution: KPMG UK uses Microsoft 365 Copilot during walkthroughs to transcribe the discussion into flowcharts and process maps and to generate a Test of Design, plus meeting recaps and action lists. The firm says transcription happens within Microsoft 365 and does not use a separate AI system.
  outcomes:
  - {lever: quality, description: KPMG UK says the approach identifies all control attributes and reduces follow-up requests to control owners; no figure is given, figure: none published, measures: n/a (qualitative statement), provenance: self-reported, source_ref: KPMGUK-CONTROLS-2026}
  prerequisites:
  - Microsoft 365 Copilot licensing under the KPMG-Microsoft alliance
  - Client agreement to transcription of walkthroughs
  risks_and_guardrails:
  - Drafting and editing of workpapers with Copilot is described as needing teams to ensure outputs still reflect auditor judgement (KPMGUK-CONTROLS-2026)
  human_checkpoints:
  - Auditor reviews the generated flowchart and Test of Design before it enters the workpapers
  role_evolution: Staff spend less time writing up meetings and more on the judgemental areas of testing (KPMGUK-CONTROLS-2026).
  evidence_grade: B
  sources:
  - {ref: KPMGUK-CONTROLS-2026, title: 'Reimagining Controls Assurance with AI: Latest Insights for Leaders (SOC 1, SOC 2, ISAE 3402, ISAE (UK) 3000, AAF 01/20, AAF 05/20)', publisher: KPMG in the UK, type: firm, url: 'https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf', date: 2026-01, access: full, locator: 'p.5-6, ''Walkthroughs'' panel and ''M365 Copilot'' panel'}
  last_reviewed: '2026-10-16'
- id: assurance-soc-attestation-03
  title: Consolidating reviewer comments on the Description of Service
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - document-production
  - coordination-scheduling
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Several reviewers comment on the service organization's system description, and someone has to reconcile the comments into one set of points for the client.
  solution: A KPMG Clara AI custom agent collates comments on a Description of Service from multiple reviewers and produces a client-ready summary of key themes (KPMG UK).
  outcomes:
  - {lever: capacity, description: Listed as one of the custom agents; no outcome figure is given for this agent, figure: none published, measures: n/a, provenance: self-reported, source_ref: KPMGUK-CONTROLS-2026}
  prerequisites:
  - Draft Description of Service and reviewer comments in a form the agent can read
  risks_and_guardrails:
  - The summary goes to the client, so the reviewing team must check it reflects the reviewers' actual points (inference from the described workflow; the source states only the capability)
  human_checkpoints:
  - Engagement team reviews the summary before it goes to the client
  role_evolution: Not described beyond the time saved on coordination (KPMGUK-CONTROLS-2026).
  evidence_grade: B
  sources:
  - {ref: KPMGUK-CONTROLS-2026, title: 'Reimagining Controls Assurance with AI: Latest Insights for Leaders (SOC 1, SOC 2, ISAE 3402, ISAE (UK) 3000, AAF 01/20, AAF 05/20)', publisher: KPMG in the UK, type: firm, url: 'https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf', date: 2026-01, access: full, locator: 'p.5, list of custom-agent capabilities'}
  last_reviewed: '2026-10-16'
  notes: 'Thin evidence: one bullet in a firm brochure. Kept because it is a distinct step (system-description review) where AI is named.'
- id: assurance-soc-attestation-04
  title: Evidence extraction and test execution in SOC and ISAE controls assurance engagements
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Testing operating effectiveness means reading large populations of tickets and evidence items and keying details into testing tables.
  solution: KPMG UK combines Clara AI, M365 Copilot and DataSnipper to automate control analysis, evidence extraction and standardised documentation. One example population was IT system change tickets, where DataSnipper pulled key details from request tickets to fill the testing tables.
  outcomes:
  - {lever: speed, description: Testing-time reduction on recent controls assurance engagements using the tool set, figure: about 18%, measures: 'reduction in testing time on ''recent engagements'' (SOC 1, SOC 2, ISAE 3402, ISAE (UK) 3000, AAF); baseline, number of engagements and method not stated', provenance: self-reported, source_ref: KPMGUK-CONTROLS-2026}
  - {lever: speed, description: Testing-time reduction for one engagement team using DataSnipper alone, figure: about 15%, measures: 'reduction in testing time for one engagement team; single engagement, baseline not stated', provenance: self-reported, source_ref: KPMGUK-CONTROLS-2026}
  prerequisites:
  - Licensed DataSnipper, M365 Copilot and Clara AI inside a secure firm environment
  - Evidence delivered electronically, for example through KPMG Clara Collaboration where control owners upload evidence (KPMGUK-CONTROLS-2026)
  risks_and_guardrails:
  - Teams are said to ensure outputs still reflect auditor judgement (KPMGUK-CONTROLS-2026)
  - Extraction accuracy and exception rates are not reported, so the quality effect is unmeasured
  human_checkpoints:
  - Auditor reviews extracted values and test conclusions
  - Auditor evaluates deviations
  role_evolution: The firm says effort moves to the most judgemental areas that drive stakeholder insight (KPMGUK-CONTROLS-2026).
  evidence_grade: A
  sources:
  - {ref: KPMGUK-CONTROLS-2026, title: 'Reimagining Controls Assurance with AI: Latest Insights for Leaders (SOC 1, SOC 2, ISAE 3402, ISAE (UK) 3000, AAF 01/20, AAF 05/20)', publisher: KPMG in the UK, type: firm, url: 'https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf', date: 2026-01, access: full, locator: p.2 (foreword) for the 18% figure; p.6 (DataSnipper panel) for the change-ticket example and the 15% figure}
  last_reviewed: '2026-10-16'
  notes: Best published SOC-specific figure found, but self-reported by the deploying firm, with no baseline. The tool set is a bundle, so the 18% cannot be attributed to AI alone (DataSnipper and the collaboration portal contribute).
- id: assurance-soc-attestation-05
  title: Pre-fieldwork evidence evaluation against audit intent (A-LIGN A-SCEND with EvidenceIQ)
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Clients submit evidence that fails the control's intent, which causes rework during fieldwork, and evidence is re-requested for each framework.
  solution: A-LIGN's audit platform evaluates a client's evidence against audit intent before auditors review it, shows coverage and gaps with explanations, maps existing evidence to additional frameworks, and deduplicates requests. A-LIGN says AI features can be switched on or off by the customer and that auditors remain accountable.
  outcomes:
  - {lever: capacity, description: Average hours saved per framework when existing evidence is reused for an additional framework, figure: about 15 hours per framework, measures: 'hours saved per additional framework by reusing evidence, as stated by A-LIGN; basis and sample not stated', provenance: vendor-published, source_ref: ALIGN-ASCEND-2026}
  - {lever: speed, description: Named customer (Teleperformance) reports evidence gathering and validation time reduced, figure: about 30-40%, measures: reduction in evidence gathering and validation time reported by Teleperformance's audit and compliance specialist; method not stated, provenance: vendor-published, source_ref: ALIGN-ASCEND-2026}
  - {lever: capacity, description: Same customer reports overall audit preparation effort reduced, figure: about 25%, measures: reduction in overall audit preparation effort reported by the same specialist; method not stated, provenance: vendor-published, source_ref: ALIGN-ASCEND-2026}
  prerequisites:
  - Client uploads evidence once to the platform or works from a connected GRC platform
  - Multi-framework engagements make reuse worthwhile
  risks_and_guardrails:
  - A-LIGN states auditors remain accountable for every decision and that the platform enforces documentation standards (ALIGN-ASCEND-2026)
  - The AICPA FAQ, as summarised by Linford, says a service organization's use of a tool does not change the service auditor's responsibilities (LINFORD-TOOLS-2021)
  human_checkpoints:
  - Auditor review and validation precede the final report (page process list)
  role_evolution: Fewer repeated evidence requests reach client staff, and prior-year evidence rolls forward automatically (ALIGN-ASCEND-2026).
  evidence_grade: B
  sources:
  - {ref: ALIGN-ASCEND-2026, title: 'A-SCEND: audit management platform with EvidenceIQ (product page)', publisher: A-LIGN, type: firm, url: 'https://www.a-lign.com/a-scend', date: 2026-10, access: full, locator: 'sections ''Audit intelligence'', ''Accelerate audits with responsible AI'' and the customer testimonial'}
  - {ref: LINFORD-TOOLS-2021, title: 'How Does the Usage of SOC 2 Software Tools Affect SOC 2 Audits?', publisher: Linford & Company, type: firm, url: 'https://linfordco.com/blog/using-soc-2-software-tools-for-audit-compliance', date: '2021-12-22', access: full, locator: 'section ''Does SOC 2 Compliance Software Affect an Individual Auditor''s Responsibilities?'''}
  last_reviewed: '2026-10-16'
  notes: 'Grade B rather than A: the figures are an approximate customer testimonial and an average from A-LIGN''s own page, without a stated method, and part of the effect comes from evidence reuse that is not AI. A-LIGN reports serving over 6,400 organizations (vendor-published). The page is undated; the ''date'' is the access month.'
- id: assurance-soc-attestation-06
  title: 'Agent-executed SOC engagement: planning, testing, exception drafting and orchestration'
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  - coordination-scheduling
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: SOC examinations repeat the same request, test and document cycle for every control, and firms with a growing SOC practice are capacity-bound.
  solution: 'Fieldguide describes four agents for SOC work: a planner that builds the engagement plan from methodology, scope and prior-year workpapers; an auditor agent that sends client requests, validates evidence and runs test procedures; a reviewer agent that surfaces exceptions and judgement calls; and an orchestrator that coordinates the agents. A live demonstration of an agent-run SOC 2 engagement was scheduled for 13 October 2026.'
  outcomes:
  - {lever: capacity, description: Vendor figures listed under 'real results from firms' on the SOC page, figure: 55% reduction in engagement hours; 90% time savings on testing; 4x engagement capacity, measures: 'not defined on the page: no firm, engagement type, baseline or sample is given', provenance: vendor-published, source_ref: FIELDGUIDE-SOC-2026}
  - {lever: capacity, description: Vendor claim in a job posting about customers' manual tasks and capacity, figure: up to 75% of time on manual tasks saved; over 4x capacity, measures: not defined in the posting, provenance: vendor-published, source_ref: FIELDGUIDE-JOBS-2026}
  prerequisites:
  - Firm methodology configured in the platform (Fieldguide is hiring an Audit Methodology Lead to integrate methodology partners, FIELDGUIDE-JOBS-2026)
  - Prior-year workpapers and client evidence in the client portal
  risks_and_guardrails:
  - Fieldguide's own posting for an audit transformation director says someone must decide which procedures suit agent execution and how output is documented to withstand inspection (FIELDGUIDE-JOBS-2026)
  - AICPA staff and peer review guidance warn against substituting platform output for the inquiry and testing the standards require (JOFA-PRB-2026; JOFA-FAST-2026)
  human_checkpoints:
  - Practitioner reviews drafted exceptions (FIELDGUIDE-WEBINAR-2026)
  - Reviewer agent routes judgement calls to a practitioner (FIELDGUIDE-SOC-2026)
  role_evolution: Fieldguide says practitioner time shifts to judgement, review and the client relationship (FIELDGUIDE-WEBINAR-2026) and is hiring for a move 'from traditional audit execution to an agentic operating model' (FIELDGUIDE-JOBS-2026).
  evidence_grade: C
  sources:
  - {ref: FIELDGUIDE-SOC-2026, title: 'SOC audits: Field Agents execute across the SOC engagement (solution page)', publisher: Fieldguide, type: vendor, url: 'https://fieldguide.io/solutions/soc-audits', date: '2026-08-11', access: full, locator: '''Field Agents execute across the SOC engagement'' and ''Real results from firms'''}
  - {ref: FIELDGUIDE-WEBINAR-2026, title: See Field Agents Execute SOC 2 Engagements Live (webinar page), publisher: Fieldguide, type: vendor, url: 'https://info.fieldguide.io/live-demo-soc-mar10', date: '2026-10-13', access: full, locator: webinar description}
  - {ref: FIELDGUIDE-JOBS-2026, title: 'Director, Audit Transformation; Audit Methodology Lead (job postings)', publisher: Fieldguide, type: job-posting, url: 'https://jobs.ashbyhq.com/fieldguide/df0e17ea-85bc-45bc-b939-fe54426fb170', date: '2026-10-02', access: full, locator: '''About us'' and ''About the role'' sections of the Director, Audit Transformation posting'}
  - {ref: JOFA-PRB-2026, title: AICPA guides peer reviewers to address SOC 2 risks, publisher: Journal of Accountancy (AICPA), type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/', date: '2026-05-14', access: full, locator: section 'A heightened focus on SOC 2 quality'}
  - {ref: JOFA-FAST-2026, title: Promises of 'fast and easy' threaten SOC credibility, publisher: Journal of Accountancy (AICPA), type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/', date: '2026-02-01', access: full, locator: 'section ''What''s the issue?'''}
  last_reviewed: '2026-10-16'
  notes: 'No named SOC firm is tied to the figures. Search-only (not opened): a Fieldguide page seen in search results claims firms saved 36-50 hours per SOC engagement and a customer cut test-procedure drafting time by 66%; not relied on. A Fieldguide case study (Weaver, entry 07) says the firm plans to embed the agents.'
- id: assurance-soc-attestation-07
  title: Engagement platform with client portal replacing spreadsheet and email workflows in an attestation practice
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - coordination-scheduling
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Evidence collection and review in attestation and internal audit engagements ran on spreadsheets, email chains and manual trackers, with multiple versions of documents.
  solution: Weaver, a firm with proprietary third-party attestation and internal audit methodologies, adopted Fieldguide as a single engagement workspace and client portal while keeping its own methodology. The firm says its next step is to embed the platform's AI agents under a phased rollout.
  outcomes:
  - {lever: growth, description: Weaver reports an increase in realization in the first year, figure: 10-12%, measures: increase in realization in year one after adopting the platform; baseline and engagement mix not stated, provenance: vendor-published, source_ref: FIELDGUIDE-WEAVER-2026}
  prerequisites:
  - Firm methodology configurable in the platform
  - Clients willing to use a portal
  risks_and_guardrails:
  - Weaver says AI does not replace professional experience and judgement and its staff validate the work (FIELDGUIDE-WEAVER-2026)
  - The firm used a phased rollout and kept risk management and review standards intact (FIELDGUIDE-WEAVER-2026)
  human_checkpoints:
  - Reviewers work from the latest version and validate engagement output
  role_evolution: Reviewers always see current information; staff shift from administrative tasks to higher-value advisory work, per the firm (FIELDGUIDE-WEAVER-2026).
  evidence_grade: B
  sources:
  - {ref: FIELDGUIDE-WEAVER-2026, title: Weaver scales GRC services with Fieldguide to deliver transparency and accelerate growth (case study), publisher: Fieldguide, type: vendor, url: 'https://www.fieldguide.io/case-studies/weaver-scales-grc-services-with-fieldguide-to-deliver-transparency-and-accelerate-growth', date: '2026-05-28', access: full, locator: '''The Results'' and ''The Road Ahead'' sections'}
  last_reviewed: '2026-10-16'
  notes: 'Pattern ''other'': engagement workflow and client-portal platform. Grade capped at B: the measured effect (realization) comes from a workflow platform, not from AI. A vendor case study, undated on the page (the date is the sitemap last-modified date). A second Fieldguide case study (BerryDunn, page last modified 2025-11-21 and apparently from the pandemic period) reports an expected 30-50% efficiency gain and a 75% cut in on-site travel; not used as an outcome because the date and AI content are unclear.'
- id: assurance-soc-attestation-08
  title: AI review of draft SOC reports for errors and inconsistencies
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Draft SOC reports are long, and a reviewer can miss a detail buried deep in the document.
  solution: Linford & Company, an IT-audit specialist firm, says it uses AI for reviewing reports, among other uses. It says the aim is a more thorough job, such as finding things on a late page of a long report, and that the AI does not save the firm time.
  outcomes:
  - {lever: quality, description: Firm states the AI helps it catch details a human might miss; it says it does not save time; no figure, figure: none published, measures: n/a (opinion statement by the firm), provenance: self-reported, source_ref: LINFORD-ASSURE-2026}
  prerequisites:
  - An approved AI tool and a draft report in reviewable form
  risks_and_guardrails:
  - The author states AI cannot judge whether a control reduces the risk it was designed for, and does not replace professional skepticism (LINFORD-ASSURE-2026)
  human_checkpoints:
  - Partner review and sign-off remain the control against rubber-stamping (LINFORD-ASSURE-2026)
  role_evolution: The firm frames AI as a way to raise thoroughness, not to cut hours (LINFORD-ASSURE-2026).
  evidence_grade: B
  sources:
  - {ref: LINFORD-ASSURE-2026, title: AI Made Compliance Cheaper. It Didn't Make Assurance Cheaper., publisher: Linford & Company, type: firm, url: 'https://linfordco.com/blog/ai-compliance-vs-assurance/', date: '2026-09-23', access: full, locator: section 'What Actually Got Cheaper' and 'What AI Can't Do'}
  last_reviewed: '2026-10-16'
  notes: One sentence in an opinion blog post by a named firm. No tool, volume or error-catch rate is reported.
- id: assurance-soc-attestation-09
  title: AI in client acceptance, sample selection and concurrent-audit scheduling at a SOC specialist firm
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - coordination-scheduling
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: A SOC practice must decide which engagements to accept, select samples, and schedule many concurrent audits.
  solution: Linford & Company says it uses AI for client acceptance, sampling of results and scheduling concurrent audits, alongside report review (entry 08). The post gives no detail on tools or methods.
  outcomes:
  - {lever: quality, description: 'Firm says the uses make audits more thorough, not faster; no figure', figure: none published, measures: n/a (opinion statement by the firm), provenance: self-reported, source_ref: LINFORD-ASSURE-2026}
  prerequisites:
  - Not stated in the source
  risks_and_guardrails:
  - The same post warns about 'bargain-basement' audits with offshored testing and no partner review of the report, which it says AI does not cause but can run (LINFORD-ASSURE-2026)
  human_checkpoints:
  - Acceptance and sampling decisions remain with the firm (the post presents AI as a support)
  role_evolution: Not described.
  evidence_grade: B
  sources:
  - {ref: LINFORD-ASSURE-2026, title: AI Made Compliance Cheaper. It Didn't Make Assurance Cheaper., publisher: Linford & Company, type: firm, url: 'https://linfordco.com/blog/ai-compliance-vs-assurance/', date: '2026-09-23', access: full, locator: section 'What Actually Got Cheaper'}
  last_reviewed: '2026-10-16'
  notes: 'Pattern ''other'': AI decision support across acceptance, sampling and scheduling. Merges three uses because the source lists them in one sentence. Split if a firm gives separate detail. The post also cites 2025 PCI Security Standards Council guidance that an AI system cannot act as assessor; that guidance was not opened (the URL tried returned 404).'
- id: assurance-soc-attestation-10
  title: Drafting and updating the system description (Section 3) with AI
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: Service organization management must keep the Section 3 description current and consistent with its procedures and the Trust Services Criteria each year.
  solution: EY conference speakers describe consolidating process and procedure documentation into draft control descriptions, standardising terminology, and mapping completeness against the AICPA Trust Services Criteria. In a live poll, 45% of respondents said they use AI for updating Section 3.
  outcomes:
  - {lever: capacity, description: Share of poll respondents who use AI to update Section 3, figure: 45%, measures: share of attendees choosing 'Updating Section 3' in a live poll at the 2026 EY SOC conference; multiple answers allowed; respondent count not stated, provenance: self-reported, source_ref: EY-SOC-2026}
  prerequisites:
  - An AI inventory and governance first, then simple automations in controlled environments (EY advice)
  - Current procedure documents and prior SOC reports as inputs
  risks_and_guardrails:
  - EY says AI can invent details and fill gaps even when told not to, so outputs need human oversight (EY-SOC-2026)
  - Per Schneider Downs' summary of AICPA TQA 9561, when AI is incorporated into the services, management must check the description remains accurate and complete (SDOWNS-TQA9561-2026)
  human_checkpoints:
  - Management reviews and owns the description
  - The service auditor evaluates the description during the examination
  role_evolution: Not described beyond EY's advice to start with governance and an AI inventory (EY-SOC-2026).
  evidence_grade: C
  sources:
  - {ref: EY-SOC-2026, title: 'How AI assurance builds trust with SOC, attestation and certification (14th annual EY SOC, Attestation and Certification Conference highlights)', publisher: EY, type: conference, url: 'https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf', date: 2026-09, access: full, locator: p.4 (six practical areas) and p.5 (poll chart)}
  - {ref: SDOWNS-TQA9561-2026, title: 'AI in SOC Examinations: What the AICPA''s New TQA Section 9561 Means for Service Organizations', publisher: Schneider Downs, type: firm, url: 'https://schneiderdowns.com/our-thoughts-on/ai-in-soc-examinations-what-the-aicpas-new-tqa-section-9561-means-for-service-organizations/', date: '2026-09-30', access: full, locator: 'section ''SOC 2: AI Fits Within the Existing Trust Services Criteria'''}
  last_reviewed: '2026-10-16'
  notes: Maturity set to piloting because the poll shows use by unnamed attendee organizations; no named deployer. The poll is of conference attendees, not a representative survey.
- id: assurance-soc-attestation-11
  title: Drafting management responses to deviations with AI
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: Each deviation in the Section 4 test results needs a management response covering root cause, remediation, timeline and ongoing monitoring, often written under deadline.
  solution: EY speakers describe using AI to draft structured management responses that address root cause analysis, remediation actions, timelines and monitoring commitments. In the live poll, 41% of respondents said they use AI for drafting coherent management responses to deviations.
  outcomes:
  - {lever: speed, description: Share of poll respondents who use AI to draft management responses to deviations, figure: 41%, measures: share of attendees choosing 'Drafting coherent management responses to deviations' in a live poll at the 2026 EY SOC conference; multiple answers allowed; respondent count not stated, provenance: self-reported, source_ref: EY-SOC-2026}
  prerequisites:
  - Deviation details and remediation facts supplied by control owners
  risks_and_guardrails:
  - EY warns AI may fill in blanks, so management must confirm the facts in each response (EY-SOC-2026)
  human_checkpoints:
  - Management approves each response, since it is management's own statement in the report
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - {ref: EY-SOC-2026, title: 'How AI assurance builds trust with SOC, attestation and certification (14th annual EY SOC, Attestation and Certification Conference highlights)', publisher: EY, type: conference, url: 'https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf', date: 2026-09, access: full, locator: p.4 item 2 and p.5 poll chart}
  last_reviewed: '2026-10-16'
- id: assurance-soc-attestation-12
  title: Continuous control monitoring and automated evidence collection by compliance-automation platforms
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types:
  - data-reporting
  - review-assurance
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Preparing for a SOC 2 examination meant collecting screenshots and spreadsheets from many systems each period, and controls could drift between audits.
  solution: Platforms such as Vanta connect to cloud and business systems, run continuous tests and collect evidence into a central dashboard, with AI agents added in 2025 and 2026 to draft policies, verify evidence and flag issues. Vanta launched compliance, third-party-risk and customer-trust agents in March 2026.
  outcomes:
  - {lever: speed, description: 'Reduction in audit preparation time, attributed by Vanta to an IDC finding', figure: 82%, measures: 'less time spent per audit by companies using Vanta, per an IDC finding quoted by Vanta; sample and baseline not stated on the page', provenance: vendor-published, source_ref: VANTA-AUDIT-2026}
  - {lever: capacity, description: Customer (WorkJam CISO) says weekly compliance effort fell, figure: about 1 hour a week instead of 7 or 8, measures: 'weekly hours on compliance tasks, as estimated by the customer''s CISO and published by Vanta', provenance: vendor-published, source_ref: VANTA-AI-2026}
  prerequisites:
  - Integrations with the client's cloud, identity, HR and ticketing systems
  - A defined control set mapped to the Trust Services Criteria
  risks_and_guardrails:
  - 'The service auditor must understand and test what the tool collects: coverage, reliability, consistency and gaps (LINFORD-TOOLS-2021, summarising the AICPA FAQ)'
  - AICPA staff and peer review warn that some firms lean too heavily on platforms without applying professional judgement (JOFA-PRB-2026)
  - A control that is monitored by software can still be missing from the integration, so tool coverage is itself a risk (LINFORD-FAQ-2022)
  human_checkpoints:
  - Service organization staff approve policies and remediation
  - The service auditor performs inspection, inquiry and observation beyond the tool (LINFORD-TOOLS-2021)
  role_evolution: Vanta describes its agent as a GRC engineer the customer never had to hire (VANTA-AI-2026).
  evidence_grade: B
  sources:
  - {ref: VANTA-AUDIT-2026, title: 'Compliance audit software: Streamline your audit experience (product page)', publisher: Vanta, type: vendor, url: 'https://www.vanta.com/products/audit', date: 2026-10, access: full, locator: hero statistics and 'Stay audit-ready with continuous compliance'}
  - {ref: VANTA-AI-2026, title: 'Vanta AI: Your 24/7 GRC engineer for security and compliance (product page)', publisher: Vanta, type: vendor, url: 'https://www.vanta.com/products/ai', date: 2026-10, access: full, locator: customer quotes (WorkJam)}
  - {ref: VERDICT-VANTA-2026, title: Vanta introduces automation tools to streamline enterprise compliance, publisher: Verdict, type: press, url: 'https://www.verdict.co.uk/vanta-introduces-automation-tools/', date: '2026-03-20', access: full, locator: paragraphs on the three agent types}
  - {ref: LINFORD-TOOLS-2021, title: 'How Does the Usage of SOC 2 Software Tools Affect SOC 2 Audits?', publisher: Linford & Company, type: firm, url: 'https://linfordco.com/blog/using-soc-2-software-tools-for-audit-compliance', date: '2021-12-22', access: full, locator: 'section ''What are Potential Risks When Using SOC 2 Software Tools?'''}
  - {ref: DRATA-AGENTGOV-2026, title: Drata Extends Trust Management Platform to Continuously Monitor and Govern AI Agents (press release; read through a text mirror because the host returned 403), publisher: Drata, type: vendor, url: 'https://drata.com/about/news/drata-extends-trust-management-platform-to-continuously-monitor-and-govern-ai-agents', date: '2026-08-04', access: full, locator: '''About Drata'' paragraph (8,500+ organizations)'}
  - {ref: JOFA-PRB-2026, title: AICPA guides peer reviewers to address SOC 2 risks, publisher: Journal of Accountancy (AICPA), type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/', date: '2026-05-14', access: full, locator: 'quote from Carl Mayes, AICPA'}
  - {ref: LINFORD-FAQ-2022, title: 'AICPA FAQs on SOC 2 Automation Tools: Insights from an Auditor', publisher: Linford & Company, type: firm, url: 'https://linfordco.com/blog/soc-2-automation-tools-aicpa-faqs', date: '2022-06-15', access: full, locator: section on integrations}
  - {ref: SACRA-VANTA-2026, title: $300M/year SOC 2 for AI (Vanta update), publisher: Sacra, type: press, url: 'https://sacra.com/research/vanta-at-300m-year/', date: '2026-04-30', access: full, locator: TL;DR (ARR estimate)}
  - {ref: VANTA-AUDITORS-2026, title: 'Vanta for Auditors: Become a Vanta auditor (partner page)', publisher: Vanta, type: vendor, url: 'https://www.vanta.com/partners/auditors', date: 2026-10, access: full, locator: '''100+ audit firms'' and ''26,000+ audits'' statistics'}
  - {ref: SECUREFRAME-2026, title: 'Secureframe: build trust, unlock growth (home page)', publisher: Secureframe, type: vendor, url: 'https://secureframe.com/', date: 2026-10, access: full, locator: hero line (6000+ customers)}
  - {ref: ONELEET-2026, title: 'Oneleet: security-first compliance (home page)', publisher: Oneleet, type: vendor, url: 'https://www.oneleet.com/', date: 2026-10, access: full, locator: 'hero section (1,700+ teams)'}
  - {ref: COMPAI-2026, title: 'Comp AI: AI compliance software for SOC 2, ISO 27001 and HIPAA (home page)', publisher: Comp AI, type: vendor, url: 'https://trycomp.ai/', date: 2026-10, access: full, locator: 'hero line (1,000+ companies)'}
  last_reviewed: '2026-10-16'
  notes: 'Grade B: several named customers use these platforms in production, but the outcome figures are vendor-quoted estimates, not measured studies. Scale, all vendor-published or analyst estimates: Vanta says 100+ audit firms and 26,000+ audits completed through it (VANTA-AUDITORS-2026); Sacra estimates Vanta reached about $300M ARR in April 2026, up about 69% year on year (SACRA-VANTA-2026); Drata says 8,500+ organizations (DRATA-AGENTGOV-2026); Secureframe says 6000+ customers (SECUREFRAME-2026); Oneleet says 1,700+ teams (ONELEET-2026); Comp AI says 1,000+ companies (COMPAI-2026). A Vanta Business Wire release on a Vanta Agent for Risk (June 2026) was seen only in search results and is not used.'
- id: assurance-soc-attestation-13
  title: Service auditor pulls evidence and control status directly from the client's compliance platform
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - data-reporting
  - review-assurance
  pattern: other
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Auditors historically collected evidence by screenshots, screen-shares and emailed samples, with duplicated effort between the client's platform and the audit tool.
  solution: Platforms expose auditor APIs and portals so evidence and control statuses flow into the auditor's tool or workspace, and requests, comments and status sit in one place. Vanta lists an Auditor API and optional auditor access to test source data; A-LIGN says its auditors can work behind the scenes while clients stay in their preferred GRC platform.
  outcomes:
  - {lever: speed, description: A-LIGN's strategic alliances lead says organizations using Vanta cut audit completion time, figure: 50%, measures: 'reduction in audit completion time, stated by an A-LIGN executive in a quote on Vanta''s page; method not stated', provenance: vendor-published, source_ref: VANTA-AUDITORS-2026}
  prerequisites:
  - Client uses a platform with an auditor interface
  - Auditor understands the integrations and what data each provides (LINFORD-FAQ-2022)
  risks_and_guardrails:
  - The service auditor must validate a sample of results the tool reports and perform procedures outside it (LINFORD-TOOLS-2021)
  - AICPA ethics staff say contract terms that make the auditor pay the tool provider for access to evidence can raise doubts about obtaining sufficient evidence (JOFA-SOCETH-2026)
  - Peer reviewers are told to look at the firm's use of external SOC platforms and the reasonableness of timelines (JOFA-PRB-2026)
  human_checkpoints:
  - Auditor tests tool-reported results by inspection, inquiry and observation
  role_evolution: Vanta says in-platform collaboration replaces email chains between client and auditor (VANTA-AUDITORS-2026). AICPA ethics staff describe tool-provider-driven deadlines and bundled examination fees as independence threats (JOFA-SOCETH-2026).
  evidence_grade: B
  sources:
  - {ref: VANTA-AUDITORS-2026, title: 'Vanta for Auditors: Become a Vanta auditor (partner page)', publisher: Vanta, type: vendor, url: 'https://www.vanta.com/partners/auditors', date: 2026-10, access: full, locator: '''Integrated auditor workflows'' and the A-LIGN quote'}
  - {ref: VANTA-Q5AUDITOR-2025, title: 'Choosing a trusted auditor: 5 key questions to ask your potential auditor', publisher: Vanta, type: vendor, url: 'https://www.vanta.com/resources/5-key-questions-to-ask-your-auditor', date: '2025-03-21', access: full, locator: question 4 (Vanta API for auditors using their own tools)}
  - {ref: ALIGN-ASCEND-2026, title: 'A-SCEND: audit management platform with EvidenceIQ (product page)', publisher: A-LIGN, type: firm, url: 'https://www.a-lign.com/a-scend', date: 2026-10, access: full, locator: '''Work where you already work'''}
  - {ref: LINFORD-TOOLS-2021, title: 'How Does the Usage of SOC 2 Software Tools Affect SOC 2 Audits?', publisher: Linford & Company, type: firm, url: 'https://linfordco.com/blog/using-soc-2-software-tools-for-audit-compliance', date: '2021-12-22', access: full, locator: 'section ''What Procedures Should Be Implemented in Conjunction with SOC 2 Software Tools?'''}
  - {ref: JOFA-SOCETH-2026, title: 'SOC engagements: Ethics risks with tool providers', publisher: Journal of Accountancy (AICPA Professional Ethics Division staff), type: standard-setter, url: 'https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/', date: '2026-04-06', access: full, locator: '''Obtaining sufficient evidence and meeting SSAE requirements'''}
  - {ref: JOFA-PRB-2026, title: AICPA guides peer reviewers to address SOC 2 risks, publisher: Journal of Accountancy (AICPA), type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/', date: '2026-05-14', access: full, locator: bullets on technology and timelines}
  - {ref: LINFORD-FAQ-2022, title: 'AICPA FAQs on SOC 2 Automation Tools: Insights from an Auditor', publisher: Linford & Company, type: firm, url: 'https://linfordco.com/blog/soc-2-automation-tools-aicpa-faqs', date: '2022-06-15', access: full, locator: section 'Benefits of SOC 2 Tools Depend on Integrations with Key Systems'}
  last_reviewed: '2026-10-16'
  notes: 'Pattern ''other'': API-based evidence exchange between the client''s platform and the auditor''s workspace. The AICPA''s own FAQ on software tools (first issued 30 June 2021 per LINFORD-FAQ-2022; the AICPA page shows 31 March 2026) is behind a free login; its content is taken from the two Linford summaries.'
- id: assurance-soc-attestation-14
  title: Security questionnaire answers drafted from approved answers and issued SOC reports
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types:
  - client-interaction
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: After a SOC report is issued, customers still send long security questionnaires that ask for the same facts.
  solution: EY speakers list drafting tailored questionnaire responses that learn from issued SOC reports and approved answers. Vanta's AI suggests answers from a knowledge base and previous responses.
  outcomes:
  - {lever: capacity, description: Vanta says suggested questionnaire answers are accepted at a high rate, figure: 95% acceptance, measures: 'share of AI-suggested answers accepted by users, as stated by Vanta; sample and period not stated', provenance: vendor-published, source_ref: VANTA-AI-2026}
  prerequisites:
  - A maintained knowledge base of approved answers and the current SOC report
  risks_and_guardrails:
  - EY says AI may invent details, so each drafted answer needs human review (EY-SOC-2026)
  human_checkpoints:
  - The user reviews and submits each answer set (VANTA-AI-2026)
  role_evolution: Security and compliance staff review suggested answers instead of writing them (VANTA-AI-2026).
  evidence_grade: C
  sources:
  - {ref: EY-SOC-2026, title: 'How AI assurance builds trust with SOC, attestation and certification (14th annual EY SOC, Attestation and Certification Conference highlights)', publisher: EY, type: conference, url: 'https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf', date: 2026-09, access: full, locator: p.4 item 5}
  - {ref: VANTA-AI-2026, title: 'Vanta AI: Your 24/7 GRC engineer for security and compliance (product page)', publisher: Vanta, type: vendor, url: 'https://www.vanta.com/products/ai', date: 2026-10, access: full, locator: '''Questionnaire responses in seconds'''}
  - {ref: TECHCRUNCH-DELVEYC-2026, title: Embattled startup Delve has 'parted ways' with Y Combinator, publisher: TechCrunch, type: press, url: 'https://techcrunch.com/2026/04/04/embattled-startup-delve-has-parted-ways-with-y-combinator/', date: '2026-04-04', access: full, locator: paragraph quoting Delve's blog on the 70% questionnaire figure}
  last_reviewed: '2026-10-16'
  notes: Customer-assurance work next to the SOC engagement rather than part of the examination. Delve said, in its own defence, that the anonymous critic acknowledged its AI automated 70% of a security questionnaire (Delve statement as reported in TECHCRUNCH-DELVEYC-2026); a company claim, not used as an outcome.
- id: assurance-soc-attestation-15
  title: AI-assisted remediation of failing controls before the examination, with expert approval
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types:
  - software-systems
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: Readiness work surfaces failing tests (misconfigured access, missing encryption), and engineers must fix them before the observation period.
  solution: Vanta's agent generates remediation snippets for tools such as Terraform, AWS CLI and CloudFormation; Secureframe sells 'Comply AI for Remediation'. Oneleet says its AI fixes gaps and an expert approves every fix before it counts as done.
  outcomes:
  - {lever: speed, description: No outcome measure published for remediation specifically, figure: none published, measures: n/a, provenance: vendor-published, source_ref: VANTA-AI-2026}
  prerequisites:
  - Integration with the cloud and code environment
  - Engineers who can apply and approve changes
  risks_and_guardrails:
  - Oneleet's approach routes every fix to an expert so that 'green' means verified, not just marked done (ONELEET-2026)
  - Allegations about fabricated evidence at another platform show the risk of marking controls as done without operating evidence (TECHCRUNCH-DELVE-2026, allegations denied by the company)
  human_checkpoints:
  - Engineer or expert approves each change (ONELEET-2026)
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - {ref: VANTA-AI-2026, title: 'Vanta AI: Your 24/7 GRC engineer for security and compliance (product page)', publisher: Vanta, type: vendor, url: 'https://www.vanta.com/products/ai', date: 2026-10, access: full, locator: '''Faster remediation'''}
  - {ref: SECUREFRAME-2026, title: 'Secureframe: build trust, unlock growth (home page)', publisher: Secureframe, type: vendor, url: 'https://secureframe.com/', date: 2026-10, access: full, locator: AI section ('Comply AI for Remediation')}
  - {ref: ONELEET-2026, title: 'Oneleet: security-first compliance (home page)', publisher: Oneleet, type: vendor, url: 'https://www.oneleet.com/', date: 2026-10, access: full, locator: '''How it works'''}
  - {ref: TECHCRUNCH-DELVE-2026, title: Delve accused of misleading customers with 'fake compliance', publisher: TechCrunch, type: press, url: 'https://techcrunch.com/2026/03/21/delve-accused-of-misleading-customers-with-fake-compliance/', date: '2026-03-22', access: full, locator: paragraph on fabricated-evidence allegations}
  last_reviewed: '2026-10-16'
- id: assurance-soc-attestation-16
  title: Policy, risk-assessment and control-set drafting tailored to the company
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: A first SOC 2 program needs policies, risk assessments and control narratives, and generic templates produce look-alike documents.
  solution: Vanta's agent drafts tailored policies and compares policies with what is happening in the environment; Comp AI says its AI learns a company's stack and processes and generates policies and assessments mapped to SOC 2 controls. A Comp AI founder says an agent may draft a policy but a person approves it.
  outcomes:
  - {lever: speed, description: Comp AI claims companies can be audit-ready quickly, figure: 'SOC 2 Type I and II audit-ready ''in days, not weeks or months''', measures: 'not defined on the page; no customer, baseline or sample', provenance: vendor-published, source_ref: COMPAI-2026}
  prerequisites:
  - Access to the company's systems to read its configuration
  risks_and_guardrails:
  - The AICPA SOC 2 Working Group chair says templated look-alike reports are a quality concern (JOFA-FAST-2026)
  - Delve said its templates, such as board-meeting notes, are starting points only, after allegations that such content was presented as evidence (TECHCRUNCH-DELVEYC-2026)
  human_checkpoints:
  - A person reviews and approves each draft policy (TECHCRUNCH-COMPAI-2026)
  - The service auditor tests operation of the controls, not the existence of the policy
  role_evolution: Vanta presents the agent as a GRC engineer the customer never had to hire (VANTA-AI-2026).
  evidence_grade: C
  sources:
  - {ref: VANTA-AI-2026, title: 'Vanta AI: Your 24/7 GRC engineer for security and compliance (product page)', publisher: Vanta, type: vendor, url: 'https://www.vanta.com/products/ai', date: 2026-10, access: full, locator: '''Policies and practices in sync'''}
  - {ref: COMPAI-2026, title: 'Comp AI: AI compliance software for SOC 2, ISO 27001 and HIPAA (home page)', publisher: Comp AI, type: vendor, url: 'https://trycomp.ai/', date: 2026-10, access: full, locator: '''How it works'' steps 1-2'}
  - {ref: TECHCRUNCH-COMPAI-2026, title: Comp AI sets eyes on a continuously agentic future for security and compliance, publisher: TechCrunch, type: press, url: 'https://techcrunch.com/2026/09/17/comp-ai-sets-eyes-on-a-continiously-agentic-future-for-security-and-complaince/', date: '2026-09-17', access: full, locator: paragraphs quoting the CEO on human approval}
  - {ref: JOFA-FAST-2026, title: Promises of 'fast and easy' threaten SOC credibility, publisher: Journal of Accountancy (AICPA), type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/', date: '2026-02-01', access: full, locator: 'section ''What''s the issue?'' (template concern)'}
  - {ref: TECHCRUNCH-DELVEYC-2026, title: Embattled startup Delve has 'parted ways' with Y Combinator, publisher: TechCrunch, type: press, url: 'https://techcrunch.com/2026/04/04/embattled-startup-delve-has-parted-ways-with-y-combinator/', date: '2026-04-04', access: full, locator: paragraph on templates as starting points}
  last_reviewed: '2026-10-16'
  notes: Comp AI raised a $34M Series A (17 Sep 2026, per TechCrunch; $37.5M raised to date). The company says its software does not replace independent audit review.
- id: assurance-soc-attestation-17
  title: AI review of received vendor SOC reports and security documentation by report users
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - research-synthesis
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: User organizations read many vendor SOC reports and security documents to find scope limits, exceptions and complementary user-entity controls.
  solution: EY speakers say recipients can use AI to review SOC reports, compare them with their own risk assessments, find changes from prior periods and call out control deviations. Vanta's vendor-risk feature pulls out the most important details from vendor documentation, according to a Duolingo security risk manager.
  outcomes:
  - {lever: capacity, description: Duolingo manager says the feature saves combing vendor documentation word for word; no figure, figure: none published, measures: n/a (customer quote), provenance: vendor-published, source_ref: VANTA-AI-2026}
  prerequisites:
  - Repository of vendor reports and the user's own risk assessment
  risks_and_guardrails:
  - EY says AI may invent details and that outputs need human oversight (EY-SOC-2026)
  human_checkpoints:
  - Reviewer decides whether the vendor's controls meet the user's risk needs
  role_evolution: Not described.
  evidence_grade: B
  sources:
  - {ref: EY-SOC-2026, title: 'How AI assurance builds trust with SOC, attestation and certification (14th annual EY SOC, Attestation and Certification Conference highlights)', publisher: EY, type: conference, url: 'https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf', date: 2026-09, access: full, locator: 'p.5, paragraph on SOC report recipients'}
  - {ref: VANTA-AI-2026, title: 'Vanta AI: Your 24/7 GRC engineer for security and compliance (product page)', publisher: Vanta, type: vendor, url: 'https://www.vanta.com/products/ai', date: 2026-10, access: full, locator: Duolingo quote}
  last_reviewed: '2026-10-16'
  notes: Overlaps with the controls-testing pilot (third-party SOC report review); see 'Routed to other modules'. Included because report users are part of the SOC ecosystem.
- id: assurance-soc-attestation-18
  title: Evidence feed and control monitoring for AI agents inside the service organization
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: model
  runtime_class: background-agent
  maturity: piloting
  problem: Service organizations now run AI agents that touch customer data, and the controls and evidence a SOC examination relies on were not built to attribute agent actions.
  solution: 'Drata made ''AI Agent Governance'' available in limited availability on 4 August 2026: a device sensor, an MCP proxy that checks each agent tool call against policy, and a tamper-evident telemetry feed. It ships first for Anthropic, with other providers in development. The company says it maps to the same controls and evidence logic as its compliance programs.'
  outcomes:
  - {lever: risk, description: No outcome figure; one early-access customer quote about inventory and policy testing, figure: none published, measures: n/a, provenance: vendor-published, source_ref: DRATA-AGENTGOV-2026}
  prerequisites:
  - Agents running on supported providers
  - Policies written in plain English and compiled into rules, per the vendor
  risks_and_guardrails:
  - CSA argues SOC 2 criteria assume actions are attributable to a human or service account, leaving an accountability gap for autonomous agents (CSA-SOC2-2026)
  - AICPA TQA 9561 says an AI tool outside the in-scope system does not enter scope merely because it is AI (SDOWNS-TQA9561-2026)
  human_checkpoints:
  - Manual approval of recommended actions unless autonomous enforcement is authorized (DRATA-AGENTGOV-2026)
  role_evolution: Drata is hiring an alliances manager for enterprise audit firms and a product engineer for AI features aimed at compliance practitioners (DRATA-JOBS-2026).
  evidence_grade: B
  sources:
  - {ref: DRATA-AGENTGOV-2026, title: Drata Extends Trust Management Platform to Continuously Monitor and Govern AI Agents (press release; read through a text mirror because the host returned 403), publisher: Drata, type: vendor, url: 'https://drata.com/about/news/drata-extends-trust-management-platform-to-continuously-monitor-and-govern-ai-agents', date: '2026-08-04', access: full, locator: announcement and 'Customers are already running' paragraph}
  - {ref: CSA-SOC2-2026, title: 'The SOC 2 AI Gap: Auditors Improvise Where AICPA Has Not Acted', publisher: Cloud Security Alliance (AI Safety Initiative), type: professional-body, url: 'https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/', date: '2026-08-30', access: full, locator: 'Security Analysis, second paragraph'}
  - {ref: DRATA-JOBS-2026, title: 'Senior SI and Audit Firm Alliances Manager; Senior Product Engineer 2, Audit (job postings)', publisher: Drata, type: job-posting, url: 'https://jobs.ashbyhq.com/drata/739d3f1a-4305-4ad3-88d4-b1b5713b67a3', date: '2026-09-08', access: full, locator: 'job summary of the Senior Product Engineer 2, Audit posting'}
  - {ref: SDOWNS-TQA9561-2026, title: 'AI in SOC Examinations: What the AICPA''s New TQA Section 9561 Means for Service Organizations', publisher: Schneider Downs, type: firm, url: 'https://schneiderdowns.com/our-thoughts-on/ai-in-soc-examinations-what-the-aicpas-new-tqa-section-9561-means-for-service-organizations/', date: '2026-09-30', access: full, locator: 'section ''Start With How AI Is Used, Not With the Technology Label'''}
  last_reviewed: '2026-10-16'
  notes: A platform entering a new product line (governing AI agents) rather than changing how SOC work is done. Detail on assurance over AI goes to a separate module (see 'Routed to other modules'). Drata's June 2026 announcement was not reachable.
- id: assurance-soc-attestation-19
  title: Platform-bundled automated SOC production through an affiliated audit-firm network (alleged and contested)
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - document-production
  - review-assurance
  pattern: end-to-end-case-agent
  ladder: automate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: Startups need a SOC 2 report quickly and cheaply to close enterprise deals, and fast-turnaround offers compete on speed and price.
  solution: An anonymous whistleblower alleged that the Delve platform generated auditor conclusions, test procedures and reports before any independent review, and that virtually all customers went through two audit firms that rubber-stamped the output. Delve denies the allegations and says it is an automation platform and that licensed auditors issue the final opinions. The AICPA says it is looking into allegations about an unnamed compliance vendor.
  outcomes:
  - {lever: risk, description: Named customers moved to another platform and independent auditors; a third said it had left earlier, figure: '2 named customers moved after the allegations (LiteLLM, Context AI); 1 more (Lovable) said it left in late 2025', measures: count of Delve customers TechCrunch named as having left; LiteLLM and Context AI said they moved to Vanta (Context AI also engaged Insight Assurance for new examinations); Lovable said it had left before the allegations, provenance: independent, source_ref: TECHCRUNCH-CONTEXT-2026}
  prerequisites:
  - A platform that controls the evidence, templates and referral to auditors
  risks_and_guardrails:
  - 'AICPA ethics staff list risk terms: tool-provider-set deadlines, bundled packages that set the examination fee, cross-referral concentration, contract terms limiting scope or evidence (JOFA-SOCETH-2026)'
  - The AICPA Peer Review Board treats identical reports, risk assessments, sample sizes and procedures across clients as a possible nonconforming engagement (JOFA-PRB-2026)
  - The AICPA's Amy Pawlicki says CPAs not enrolled in peer review, or unlicensed signatories posing as CPAs, who sign fraudulent SOC reports violate state law (JOFA-PODSOC-2026)
  human_checkpoints:
  - The licensed service auditor's independent examination and signature are the control the allegations say was bypassed (TECHCRUNCH-DELVE-2026)
  role_evolution: The allegations describe the platform acting as implementer and examiner, which removes the auditor's independent role (TECHCRUNCH-DELVE-2026, reporting the whistleblower's claim).
  evidence_grade: C
  sources:
  - {ref: TECHCRUNCH-DELVE-2026, title: Delve accused of misleading customers with 'fake compliance', publisher: TechCrunch, type: press, url: 'https://techcrunch.com/2026/03/21/delve-accused-of-misleading-customers-with-fake-compliance/', date: '2026-03-22', access: full, locator: paragraphs on DeepDelver's claims and Delve's response}
  - {ref: TECHCRUNCH-DELVEYC-2026, title: Embattled startup Delve has 'parted ways' with Y Combinator, publisher: TechCrunch, type: press, url: 'https://techcrunch.com/2026/04/04/embattled-startup-delve-has-parted-ways-with-y-combinator/', date: '2026-04-04', access: full, locator: Delve's statements on re-audits and removing audit firms}
  - {ref: TECHCRUNCH-CONTEXT-2026, title: Another customer of troubled startup Delve suffered a big security incident, publisher: TechCrunch, type: press, url: 'https://techcrunch.com/2026/04/23/another-customer-of-troubled-startup-delve-suffered-a-big-security-incident/', date: '2026-04-23', access: full, locator: paragraph quoting Context AI}
  - {ref: AICPA-SOC-2026, title: 'System and Organization Controls: SOC Suite of Services (landing page with notice on vendor allegations)', publisher: AICPA & CIMA, type: standard-setter, url: 'https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2', date: 2026-10, access: full, locator: '''Notice'' paragraph'}
  - {ref: IANS-DELVE-2026, title: Delve Allegations Expose Weak Points in Modern Compliance, publisher: IANS Research, type: press, url: 'https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/03/30/delve-allegations-expose-weak-points-in-modern-compliance', date: '2026-03-24', access: full, locator: key points}
  - {ref: JOFA-PODSOC-2026, title: 'The risks of quick-turn SOC engagements and what CPAs should know (podcast with Amy Pawlicki, AICPA)', publisher: Journal of Accountancy (AICPA), type: podcast, url: 'https://www.journalofaccountancy.com/podcast/2026/apr/the-risks-of-quick%e2%80%91turn-soc-engagements-and-what-cpas-should-know/', date: '2026-04-30', access: full, locator: answer on peer review and state law}
  - {ref: JOFA-SOCETH-2026, title: 'SOC engagements: Ethics risks with tool providers', publisher: Journal of Accountancy (AICPA Professional Ethics Division staff), type: standard-setter, url: 'https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/', date: '2026-04-06', access: full, locator: 'section ''Objectivity, conflicts of interest, and independence'''}
  - {ref: JOFA-PRB-2026, title: AICPA guides peer reviewers to address SOC 2 risks, publisher: Journal of Accountancy (AICPA), type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/', date: '2026-05-14', access: full, locator: paragraph on nonconforming engagements}
  - {ref: SACRA-VANTA-2026, title: $300M/year SOC 2 for AI (Vanta update), publisher: Sacra, type: press, url: 'https://sacra.com/research/vanta-at-300m-year/', date: '2026-04-30', access: full, locator: TL;DR (Sacra's 493 figure)}
  - {ref: TECHCRUNCH-DELVE2-2026, title: 'Delve whistleblower strikes again, with alleged receipts about ''fake compliance''', publisher: TechCrunch, type: press, url: 'https://techcrunch.com/2026/03/30/delve-whistleblower-strikes-again-with-alleged-receipts-about-fake-compliance/', date: '2026-03-30', access: full, locator: opening paragraph (CEO denial and whistleblower follow-up of 30 Mar)}
  last_reviewed: '2026-10-16'
  notes: 'Cautionary entry, not a recommended practice. Everything about the conduct is allegation; Delve disputes it and TechCrunch did not independently verify the claims. Figures in circulation (hundreds of near-identical reports; Sacra says 493, SACRA-VANTA-2026, characterising the allegations) trace to the whistleblower''s analysis and were not verified. A WebProNews article on the story contradicts TechCrunch on basic facts (funding, valuation) and was not used. Search-only: price points of $6,000-$15,000 appear in a secondary blog and are not used. No outcome of any AICPA or state-board action was found as of 16 Oct 2026.'
- id: assurance-soc-attestation-20
  title: 'Platform-owned licensed CPA firm: ''auditor-led, AI-powered'' audits'
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: workflow-automation
  maturity: in-production
  problem: Readiness software and the audit are bought separately, so evidence is collected twice and the client manages two relationships.
  solution: Thoropass combines a compliance platform with a licensed CPA firm (Thoropass Assurance) and says it uses AI to map controls, identify gaps and organize evidence, so the audit runs in the same platform. It says the platform enforces consistency in evidence collection and control validation.
  outcomes:
  - {lever: capacity, description: Vendor reports a customer base and a peer review claim; no time or cost measure, figure: '1,000+ customers', measures: number of customers claimed on Thoropass's home page; period not stated, provenance: vendor-published, source_ref: THOROPASS-2026}
  prerequisites:
  - Client adopts the vendor's platform, or runs it beside its own
  risks_and_guardrails:
  - AICPA ethics staff say an arrangement where the tool provider is in the auditor's network or an alternative practice structure needs an independence evaluation, and bundles that set the examination fee can impair independence (JOFA-SOCETH-2026)
  - The AICPA's peer review guidance asks reviewers to look at engagement timelines and tailoring (JOFA-PRB-2026)
  human_checkpoints:
  - Licensed auditors perform the examination and sign the report (THOROPASS-2026)
  role_evolution: Thoropass staffs its assurance practice with former Big Four and specialist-firm auditors and describes the model as 'auditor-led' (THOROPASS-2026).
  evidence_grade: B
  sources:
  - {ref: THOROPASS-2026, title: 'Thoropass: auditor-led, AI-powered audits (home page)', publisher: Thoropass, type: vendor, url: 'https://www.thoropass.com/', date: 2026-10, access: full, locator: 'hero statement, FAQ on ''audit experience different from a traditional audit firm'', footer on the licensed firm'}
  - {ref: JOFA-SOCETH-2026, title: 'SOC engagements: Ethics risks with tool providers', publisher: Journal of Accountancy (AICPA Professional Ethics Division staff), type: standard-setter, url: 'https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/', date: '2026-04-06', access: full, locator: '''Network firm considerations'''}
  - {ref: JOFA-PRB-2026, title: AICPA guides peer reviewers to address SOC 2 risks, publisher: Journal of Accountancy (AICPA), type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/', date: '2026-05-14', access: full, locator: bullets on technology and timelines}
  last_reviewed: '2026-10-16'
  notes: 'Pattern ''other'': a platform and a licensed firm sold as one service, with AI mapping and evidence organizing. This entry records a structure, not a finding. The source does not say the arrangement raises an independence issue; the AICPA article describes what must be evaluated. Thoropass''s claim of the highest AICPA peer review rating is its own and was not verified.'
- id: assurance-soc-attestation-21
  title: AI-native CPA firm with a published machine-readable method and complete-population testing
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: full-population-testing
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Buyers cannot tell from a SOC 2 report whether the auditor inspected evidence or only collected screenshots, because firms do not publish their testing methods.
  solution: A former Deloitte SOC fieldwork auditor who started a new firm published the method as machine-readable files (86 controls, 355 test attributes with pass criteria, 498 calibration examples of AI judgement calls) under an open licence. The author says the method tests complete populations by default because AI makes looking at all items cheap in small companies, with sampling kept as a disclosed fallback using seeded selection.
  outcomes:
  - {lever: quality, description: 'No outcome yet: the author says the firm has issued one Type I and no Type II', figure: none published, measures: n/a, provenance: self-reported, source_ref: HN-CHIARO-2026}
  prerequisites:
  - Small populations at client companies (the author's stated reason for complete-population testing)
  - A licensed firm that signs the report
  risks_and_guardrails:
  - The author says a model grades itself generously without calibration examples (HN-CHIARO-2026)
  - Peer review for the firm is enrolled, with its first review due in 2027 (HN-CHIARO-2026)
  human_checkpoints:
  - A licensed firm issues the actual audit (HN-CHIARO-2026)
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - {ref: HN-CHIARO-2026, title: 'Show HN: Ex-Deloitte auditor open-sourced the whole SOC 2 method for your AI (thread; date derived from ''73 days ago'')', publisher: Hacker News, type: community, url: 'https://news.ycombinator.com/item?id=49171140', date: '2026-08-04', access: full, locator: author's top-level comment and replies}
  last_reviewed: '2026-10-16'
  notes: Single self-description on a forum, flagged in the thread; the GitHub repository was not reachable, so the counts are the author's claims. The date is derived from '73 days ago' on the page. The author states the firm has only a method and no track record.
- id: assurance-soc-attestation-22
  title: Authenticity screening of client-supplied evidence in SOC testing (idea)
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - review-assurance
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: AI can produce convincing documents, signatures and metadata, and tool-collected or client-supplied evidence may be fabricated or too clean.
  solution: 'Idea discussed by practitioners: apply a zero-trust approach, validate the authenticity of evidence before relying on it, and look harder at evidence that looks too perfect. No SOC-specific detection tool or deployment was found.'
  outcomes:
  - {lever: risk, description: none published, figure: none published, measures: n/a, provenance: self-reported, source_ref: ISACA-EVIDENCE-2026}
  prerequisites:
  - Authenticity-checking skills and tools; evidence obtained directly from source systems where possible
  risks_and_guardrails:
  - An internal-audit author reports an AI-generated document with synthetic signatures and fabricated metadata, harmless in that case (ISACA-EVIDENCE-2026)
  human_checkpoints:
  - The auditor challenges evidence that looks too perfect (LINFORD-ASSURE-2026)
  role_evolution: Authors call for AI literacy and digital forensics skills among auditors (ISACA-EVIDENCE-2026).
  evidence_grade: D
  sources:
  - {ref: ISACA-EVIDENCE-2026, title: 'The Audit Evidence Crisis: How AI Deepfakes Are Rewriting Assurance Standards', publisher: ISACA (ISACA Now blog), type: professional-body, url: 'https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2026/the-audit-evidence-crisis-how-ai-deepfakes-are-rewriting-assurance-standards', date: '2026-06-08', access: full, locator: '''The New Reality for Assurance Professionals'' and ''The Path Forward'''}
  - {ref: LINFORD-ASSURE-2026, title: AI Made Compliance Cheaper. It Didn't Make Assurance Cheaper., publisher: Linford & Company, type: firm, url: 'https://linfordco.com/blog/ai-compliance-vs-assurance/', date: '2026-09-23', access: full, locator: section 'When the Evidence Looks Too Clean'}
  last_reviewed: '2026-10-16'
  notes: 'Idea: practitioner opinion and one anecdote. Not a measured or deployed use.'
```

---

## 3. Module notes

### Processes and key steps (with work types)

1. **Scoping and acceptance:** choose services, Trust Services categories (one to five for SOC 2), system boundary, Type 1 or Type 2 and period (`expert-judgment`, `coordination-scheduling`) (JOFA-PODSOC-2026). AI use by the service organization is a new scoping question (SDOWNS-TQA9561-2026).
2. **Readiness and remediation:** gap assessment, control design, fixing failing tests (`review-assurance`, `software-systems`). Platform vendors concentrate here (entries 12, 15, 16).
3. **System description (Section 3) and management assertion** (`document-production`) (entry 10).
4. **Risk assessment, control set and test plan** (`expert-judgment`, `document-production`). Fieldguide and KPMG UK describe agents for plan and test-procedure drafting (entries 01, 06).
5. **Walkthroughs and test of design** (`research-synthesis`, `review-assurance`) (entries 01, 02).
6. **Evidence requests and collection** (`coordination-scheduling`, `data-reporting`) (entries 05, 12, 13).
7. **Testing operating effectiveness,** including sampling and the procedures needed when the evidence comes from a tool (`review-assurance`) (entries 04, 06, 13, 21).
8. **Deviation evaluation and management responses** (`expert-judgment`, `document-production`) (entry 11).
9. **Reporting:** opinion, Section 4, report review, partner sign-off (`document-production`, `review-assurance`) (entry 08).
10. **Bridge letters and interim communications to user entities** (`client-interaction`, `document-production`): no AI evidence found.
11. **Firm quality and peer review of the SOC practice** (`review-assurance`): see "Routed to other modules".
12. **Use of the report by customers:** vendor-risk review and questionnaires (`research-synthesis`, `client-interaction`) (entries 14, 17).

### Common pain points

- Collecting screenshots and user lists by hand: a Linford author recalls a compliance officer spending two weeks screenshotting a user list about ten years ago (LINFORD-ASSURE-2026).
- Repeated evidence requests and re-doing audits per framework (ALIGN-ASCEND-2026).
- Client and buyer pressure for speed and low price, with tool vendors setting expectations of weeks or even hours (JOFA-FAST-2026, JOFA-PODSOC-2026).
- Control failures cluster in manual controls and system access in KPMG UK's benchmark: 90% of operating-effectiveness exceptions were on manually operated controls, and 39% of exceptions were on system access and authorisation (KPMGUK-CONTROLS-2026).
- Uncertainty on how to scope and test service organizations' own AI (CSA-SOC2-2026, KPMG-SOC-2026, SDOWNS-TQA9561-2026).
- Report users cannot easily tell a tailored report from a template (HN-CHIARO-2026, JOFA-FAST-2026).

### Metrics and benchmarks

| Metric | Value | What it measures | Provenance | Ref |
|---|---|---|---|---|
| Testing-time reduction, KPMG UK SOC and ISAE engagements | about 18% | Reduction in testing time on recent engagements using Clara AI, Copilot and DataSnipper; baseline and number of engagements not stated | self-reported | KPMGUK-CONTROLS-2026 (p.2) |
| Testing-time reduction, one team with DataSnipper | about 15% | One engagement team; baseline not stated | self-reported | KPMGUK-CONTROLS-2026 (p.6) |
| AI use in SOC work among EY conference attendees | evidence collection 63%; Section 3 45%; deviation responses 41%; project management 29% | Share of attendees choosing each use in a live poll; multiple answers; respondent count not stated | self-reported (EY event) | EY-SOC-2026 (p.5) |
| Benchmark: share of operating-effectiveness exceptions on manual controls | 90% | Exceptions in 180+ controls assurance reports issued between 2024 and 2025 | self-reported analysis | KPMGUK-CONTROLS-2026 (p.10) |
| Benchmark: share of exceptions on system access and authorisation | 39% | Same report set | self-reported analysis | KPMGUK-CONTROLS-2026 (p.10) |
| Benchmark: qualified reports | 15% in 2024-25 against 20% in 2023-24 | Share of reports issued that were qualified | self-reported analysis | KPMGUK-CONTROLS-2026 (p.10) |
| Respondents who would switch auditors to improve the quality of the final audit report | 60% | A-LIGN's sixth annual benchmark, 1,000+ respondents; the figure was read from an image on the page; the report itself was not opened | vendor-published | ALIGN-BENCH-2026 |
| Audit prep time reduction with Vanta | 82% | Reduction attributed to an IDC finding quoted by Vanta; method not stated | vendor-published | VANTA-AUDIT-2026 |
| Hours saved per additional framework | about 15 | A-LIGN's average from evidence reuse; basis not stated | vendor-published | ALIGN-ASCEND-2026 |
| Vanta ARR | about $300M in April 2026, up about 69% year on year | Analyst estimate | independent estimate | SACRA-VANTA-2026 |
| Listed SOC 2 Type 2 fees by firm type | specialist CPA firms $15,500-$50,000; full-service CPA firms $30,000-$80,000; Big Four $65,000-$200,000 | Median listed minimum to median listed maximum fee in a lead-generation directory (62, 106 and 19 listings); estimates, not quotes or paid fees | vendor-published (affiliate directory) | SOC2AUDITORS-COST-2026 |
| Median ballpark quote for SOC 2 Type 2 | $9,000 for 1-10 and for 11-50 employees (Jul-Sep 2026 quote requests) | Buyers' quote requests routed through the directory; AI companies saw $9,500 | vendor-published (affiliate directory) | SOC2AUDITORS-COST-2026, SOC2AUDITORS-AI-2026 |
| SOC reports issued per year by one specialist firm | more than 2,000 | Firm's own statement | self-reported | SCHELLMAN-2026 |

Not found: any SOC-specific accuracy, error-catch, override or rework rate for an AI tool; peer review deficiency rates for SOC 2 practices; hours or fee trends published by an auditing firm.

### Guardrails and regulatory points

- **AICPA TQA 9561 (11 Sep 2026).** AI creates no separate SOC model and no new criteria. Whether AI belongs in a report depends on whether it is used in the services delivered or only internally, and on whether it affects the system, risks and controls already in scope. For SOC 1, the description must disclose AI's nature where it is part of the services and relevant to user entities' ICFR (SDOWNS-TQA9561-2026; AICPA-TQA9561-2026 landing page confirms the scope, full text is behind a login).
- **AICPA FAQ on software tools.** First issued 30 June 2021; the AICPA page shows 31 March 2026. Linford's summaries say the service auditor must consider tool coverage, reliability and consistency, must not rely on the tool alone, and must validate a sample of the tool's results (LINFORD-TOOLS-2021, LINFORD-FAQ-2022, AICPA-SOCFAQ-2026).
- **AICPA ethics staff on SOC tool providers (6 Apr 2026).** Terms that shift control, judgement, financial dependency, promotion or evidence access to the tool provider can create independence and objectivity threats. Examples: concentrated cross-referrals, provider-driven deadlines, bundled packages that set the fee, a provider's ability to change the fee, non-disparagement or liability terms that stop the auditor communicating required matters, and paying the provider for evidence access. If the provider is in the auditor's network or an alternative practice structure, its relationships with attest clients must be considered (JOFA-SOCETH-2026).
- **AICPA Peer Review Board (May 2026).** Identical reports, risk assessments, sample sizes and procedures across engagements can make an engagement "nonconforming". A single file review is often insufficient; reviewers are guided to understand the firm's use of platforms and the reasonableness of timelines. Elevated risk may lead to about five engagements from different partners being compared. Staff planned structured outreach from 1 June 2026 (JOFA-PRB-2026).
- **State law.** The AICPA says SOC 2 is an examination-level attestation signed by a licensed CPA, not a certification; unlicensed signatories posing as CPAs, or CPAs not in peer review, who sign fraudulent reports violate state law (JOFA-PODSOC-2026).
- **Third-party claims.** The SOC 2 Working Group chair notes a CPA can be held liable for false claims a third party makes on the CPA's behalf, if the firm endorses them by act or omission (JOFA-FAST-2026).
- **AI risk inside the firm.** EY warns AI may invent details and agents may change behaviour to get around anomalies, so human oversight stays (EY-SOC-2026).
- **Gap in criteria.** CSA says the Trust Services Criteria (last substantively revised 2017, points of focus 2022) lack AI-specific criteria, so auditors request model lineage, inference logging, drift monitoring and AI subprocessor evidence in different ways (CSA-SOC2-2026).

### Frontier signals (dated)

- **2026-01:** KPMG UK says it is introducing a reasonable-assurance opinion over AI governance and controls through "SOC 2+" (KPMGUK-CONTROLS-2026, p.2 and p.7-8).
- **2026-02-01:** The AICPA is exploring a SOC Quality Center as a badge of quality for participating firms (JOFA-FAST-2026).
- **2026-03-20:** Vanta launches compliance, third-party-risk and customer-trust agents (VERDICT-VANTA-2026).
- **2026-03-22 to 2026-04-23:** the Delve allegations and fallout: YC parted ways (4 Apr), LiteLLM and Context AI moved to another platform and independent auditors, Delve offered re-audits and said it was removing audit firms that did not meet its standards (TECHCRUNCH-DELVE-2026, TECHCRUNCH-DELVE2-2026 for the whistleblower's second post on 30 Mar, TECHCRUNCH-DELVEYC-2026, TECHCRUNCH-CONTEXT-2026).
- **2026-04-06 to 2026-05-14:** AICPA ethics guidance, podcast and Peer Review Board alert on tool-provider SOC 2 (JOFA-SOCETH-2026, JOFA-PODSOC-2026, JOFA-PRB-2026).
- **2026-08-04:** Drata releases AI Agent Governance in limited availability (DRATA-AGENTGOV-2026). The same day, a former Deloitte SOC auditor posts a public, machine-readable SOC 2 method and says complete-population testing should be the default at small-company scale (HN-CHIARO-2026).
- **2026-09-11:** AICPA TQA 9561 on AI in SOC 1 and SOC 2 (SDOWNS-TQA9561-2026).
- **2026-09-17:** Comp AI announces a $34M Series A (TECHCRUNCH-COMPAI-2026).
- **2026-09-22:** KPMG webcast page says forthcoming Trust Services Criteria changes are expected to restructure the criteria and add emerging-technology considerations (KPMG-SOC-2026).
- **2026-09-23:** a SOC specialist firm argues that AI made compliance cheaper but assurance no cheaper (LINFORD-ASSURE-2026).
- **2026-10-13:** Fieldguide schedules a live demonstration of agents executing a SOC 2 engagement (FIELDGUIDE-WEBINAR-2026), after posting a role to lead the move to an "agentic operating model" (FIELDGUIDE-JOBS-2026, 2026-10-02).

### Service model and pricing

- **Bundling and routing.** Vendors act as a front door for SOC 2; some cultivate firm networks, and marketing references thousands of reports a year (JOFA-FAST-2026). Ethics staff treat bundled packages that set the examination fee as an independence risk (JOFA-SOCETH-2026).
- **Auditor-led alternatives.** A-LIGN (6,400+ organizations claimed) pairs its audit platform with a PCAOB-registered CPA firm (ALIGN-ASCEND-2026, ALIGN-BENCH-2026); Thoropass runs a licensed CPA firm beside its platform (THOROPASS-2026); Vanta's page says it works with a trusted network of audit firms and with an organization's own auditor (VANTA-AUDIT-2026).
- **Positioning after Delve.** Oneleet markets against "badge" platforms, saying an expert approves every fix and an independent auditor signs the report (ONELEET-2026); Comp AI says its software does not replace independent audit review (TECHCRUNCH-COMPAI-2026); Vanta's guidance to buyers stresses not choosing an auditor on price alone (VANTA-Q5AUDITOR-2025).
- **Fees.** Mid-market firms face intense fee pressure, per the SOC 2 Working Group chair (JOFA-FAST-2026). The AICPA reports "exceedingly low flat-rate prices" for what some vendors call SOC certification (JOFA-PODSOC-2026). No firm-published fee or realization change tied to AI was found, except Weaver's reported 10-12% realization increase after adopting an engagement platform (FIELDGUIDE-WEAVER-2026, vendor-published).
- **Capacity.** Vendors market capacity (Fieldguide: 4x; A-LIGN: hours per framework); the AICPA warns against cutting hours to match high-volume shops (JOFA-FAST-2026).

### Workforce and role effects

- Control owners and client staff are asked for fewer meetings and repeated requests (KPMGUK-CONTROLS-2026, ALIGN-ASCEND-2026).
- Fieldguide is hiring an audit methodology lead and a director of audit transformation to encode methodology and change management for agent-led engagements (FIELDGUIDE-JOBS-2026). Drata is hiring a product engineer for AI features aimed at compliance practitioners and an alliances manager for enterprise audit firms (DRATA-JOBS-2026). These are vendor roles; no audit-firm job posting showing real SOC use was found.
- The AICPA says a SOC examiner needs deep subject-matter expertise in security and privacy (JOFA-PODSOC-2026). Linford warns about testing offshored to unqualified staff, with no walkthroughs and no partner review of the report (LINFORD-ASSURE-2026).
- EY says organizations are hiring chief data strategy officers and that fixing data governance is the most important investment (EY-SOC-2026).
- ISACA authors call for AI literacy and digital forensics skills among auditors (ISACA-EVIDENCE-2026).

### Objections and concerns practitioners raise

- **Commoditisation:** templated, look-alike reports with a different client logo; very few CPA firms signing high volumes (JOFA-FAST-2026).
- **Independence and control:** vendors setting deadlines, fees and evidence access (JOFA-SOCETH-2026).
- **Reliance on dashboards in place of inquiry and testing:** peer reviewers are alerted (JOFA-PRB-2026; CSA-SOC2-2026).
- **Marketing language:** SOC 2 "compliance" and "certification" are terms the AICPA says do not apply (JOFA-FAST-2026, JOFA-PODSOC-2026).
- **Criteria gap for AI:** the same clean report may cover different AI controls (CSA-SOC2-2026).
- **Agent accountability:** autonomous actions are hard to attribute under access and change-management criteria (CSA-SOC2-2026).
- **Evidence authenticity:** evidence that looks too perfect, and AI-generated documents (ISACA-EVIDENCE-2026, LINFORD-ASSURE-2026).
- **Accuracy:** AI may invent details; agents may rewrite their own behaviour (EY-SOC-2026).
- **Time claims:** a SOC firm says AI does not save it time; it raises thoroughness (LINFORD-ASSURE-2026).
- **Platform security:** a researcher reportedly accessed sensitive Delve data (TECHCRUNCH-DELVE-2026, reported claim).

### Interview probes for an advisor

1. When a client arrives through a platform or referral partner, who sets scope, fee and report date, and does any contract term cover deadlines, evidence access, non-disparagement or fee changes?
2. How do you test what a compliance platform collects: what share of tool-reported results do you re-perform, how do you check integration coverage, and what stays outside the tool?
3. Where do you use AI today (readiness, walkthroughs, evidence extraction, testing, report review, acceptance, scheduling), what is the review standard for AI output, and what do you measure (hours per engagement, deviations found, rework)?
4. At small-company population sizes, do you still sample? What would a complete-population approach change in your methodology, documentation and peer review?
5. How have fees, realization and staffing mix changed since platforms and AI arrived, and what do you do to show a buyer that your report is tailored and not a template?

---

## 4. Routed to other modules

- **assurance over AI (the split-off module; landscape section 10, change 1):**
  - KPMG UK's SOC 2+ opinion over AI governance and controls (KPMGUK-CONTROLS-2026, p.7-8).
  - AICPA TQA 9561 scoping of service organizations' AI use (SDOWNS-TQA9561-2026, AICPA-TQA9561-2026).
  - The CSA note on the missing AI criteria (CSA-SOC2-2026) and the KPMG webcast on forthcoming Trust Services Criteria changes (KPMG-SOC-2026).
  - EY's conference theme of AI assurance through SOC and ISO (EY-SOC-2026, pp.2-3).
  - Linford's 2023 note on SOC 2 considerations for AI and ML service organizations (LINFORD-AIML-2023, 2023-07-05).
  - The directory listing of ISO 42001 certification bodies (SOC2AUDITORS-AI-2026).
  - Drata's agent governance product (entry 18).
- **acceptance-independence:** tool-provider arrangements, referral concentration, bundled fees and network or alternative-practice-structure questions (JOFA-SOCETH-2026); the AICPA's notice on allegations about a compliance vendor (AICPA-SOC-2026); the platform-plus-licensed-firm structure (entry 20).
- **quality-management:** the Peer Review Board's SOC 2 alert and outreach (JOFA-PRB-2026); the AICPA's SOC Quality Center idea (JOFA-FAST-2026); firm-level tool governance for SOC practices.
- **controls-testing:** user-side review of third-party SOC reports (entry 17; the pilot controls-testing module holds a use case on it); evidence-request and testing agents (entry 06).
- **substantive-testing:** Fieldguide's Audit Testing Agent for financial audit, which the company says can automate up to 70% of testing (FIELDGUIDE-FINAUDIT-2025, June 2025; vendor claim).

---

## 5. Sources

Access is `full` for every source: each was opened and read. Two notes:
- AICPA-TQA9561-2026 and AICPA-SOCFAQ-2026: the landing pages were read; the PDFs are behind a free AICPA login, so the substance comes from the secondary summaries named in the entries.
- DRATA-AGENTGOV-2026: read through a text mirror because the host returned 403.

Ref | Title | Publisher | Type | URL | Date | Access
---|---|---|---|---|---|---
AICPA-SOC-2026 | System and Organization Controls: SOC Suite of Services (landing page with notice on vendor allegations) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2 | 2026-10 | full
AICPA-SOCFAQ-2026 | FAQs: Effect of the use of software tools on SOC 2 examinations (landing page; PDF behind free login) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/article/faqs-effect-of-the-use-of-software-tools-on-soc-2-r-examinations | 2026-03-31 | full
AICPA-TQA9561-2026 | TQA Section 9561: SOC Examinations: Effect of the Service Organization's Use of AI on SOC 1 and SOC 2 Examinations (landing page; PDF behind free login) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/download/tqa-section-9561-soc-examinations-effect-of-the-service-organizations-use-of-ai-on-soc1-and-soc2-examinations | 2026-09-11 | full
ALIGN-ASCEND-2026 | A-SCEND: audit management platform with EvidenceIQ (product page) | A-LIGN | firm | https://www.a-lign.com/a-scend | 2026-10 | full
ALIGN-BENCH-2026 | 2026 Compliance Benchmark Report (landing page; report download not opened) | A-LIGN | survey | https://www.a-lign.com/resources/2026-compliance-benchmark-report | 2026-01 | full
BARR-2026 | BARR Advisory home page | BARR Advisory | firm | https://www.barradvisory.com/ | 2026-10 | full
COMPAI-2026 | Comp AI: AI compliance software for SOC 2, ISO 27001 and HIPAA (home page) | Comp AI | vendor | https://trycomp.ai/ | 2026-10 | full
CSA-SOC2-2026 | The SOC 2 AI Gap: Auditors Improvise Where AICPA Has Not Acted | Cloud Security Alliance (AI Safety Initiative) | professional-body | https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/ | 2026-08-30 | full
DRATA-AGENTGOV-2026 | Drata Extends Trust Management Platform to Continuously Monitor and Govern AI Agents (press release; read through a text mirror because the host returned 403) | Drata | vendor | https://drata.com/about/news/drata-extends-trust-management-platform-to-continuously-monitor-and-govern-ai-agents | 2026-08-04 | full
DRATA-JOBS-2026 | Senior SI and Audit Firm Alliances Manager; Senior Product Engineer 2, Audit (job postings) | Drata | job-posting | https://jobs.ashbyhq.com/drata/739d3f1a-4305-4ad3-88d4-b1b5713b67a3 | 2026-09-08 | full
EY-SOC-2026 | How AI assurance builds trust with SOC, attestation and certification (14th annual EY SOC, Attestation and Certification Conference highlights) | EY | conference | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf | 2026-09 | full
FIELDGUIDE-FINAUDIT-2025 | Increase capacity and audit quality with Field Agents for financial audit (blog; sitemap last-modified 2025-06-26, text refers to AICPA ENGAGE 9-11 June 2025) | Fieldguide | vendor | https://www.fieldguide.io/blog/increase-capacity-and-audit-quality-with-field-agents-for-financial-audit | 2025-06 | full
FIELDGUIDE-JOBS-2026 | Director, Audit Transformation; Audit Methodology Lead (job postings) | Fieldguide | job-posting | https://jobs.ashbyhq.com/fieldguide/df0e17ea-85bc-45bc-b939-fe54426fb170 | 2026-10-02 | full
FIELDGUIDE-SOC-2026 | SOC audits: Field Agents execute across the SOC engagement (solution page) | Fieldguide | vendor | https://fieldguide.io/solutions/soc-audits | 2026-08-11 | full
FIELDGUIDE-WEAVER-2026 | Weaver scales GRC services with Fieldguide to deliver transparency and accelerate growth (case study) | Fieldguide | vendor | https://www.fieldguide.io/case-studies/weaver-scales-grc-services-with-fieldguide-to-deliver-transparency-and-accelerate-growth | 2026-05-28 | full
FIELDGUIDE-WEBINAR-2026 | See Field Agents Execute SOC 2 Engagements Live (webinar page) | Fieldguide | vendor | https://info.fieldguide.io/live-demo-soc-mar10 | 2026-10-13 | full
HN-CHIARO-2026 | Show HN: Ex-Deloitte auditor open-sourced the whole SOC 2 method for your AI (thread; date derived from '73 days ago') | Hacker News | community | https://news.ycombinator.com/item?id=49171140 | 2026-08-04 | full
IANS-DELVE-2026 | Delve Allegations Expose Weak Points in Modern Compliance | IANS Research | press | https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/03/30/delve-allegations-expose-weak-points-in-modern-compliance | 2026-03-24 | full
ISACA-EVIDENCE-2026 | The Audit Evidence Crisis: How AI Deepfakes Are Rewriting Assurance Standards | ISACA (ISACA Now blog) | professional-body | https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2026/the-audit-evidence-crisis-how-ai-deepfakes-are-rewriting-assurance-standards | 2026-06-08 | full
JOFA-FAST-2026 | Promises of 'fast and easy' threaten SOC credibility | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/ | 2026-02-01 | full
JOFA-PODSOC-2026 | The risks of quick-turn SOC engagements and what CPAs should know (podcast with Amy Pawlicki, AICPA) | Journal of Accountancy (AICPA) | podcast | https://www.journalofaccountancy.com/podcast/2026/apr/the-risks-of-quick%e2%80%91turn-soc-engagements-and-what-cpas-should-know/ | 2026-04-30 | full
JOFA-PRB-2026 | AICPA guides peer reviewers to address SOC 2 risks | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/ | 2026-05-14 | full
JOFA-SOCETH-2026 | SOC engagements: Ethics risks with tool providers | Journal of Accountancy (AICPA Professional Ethics Division staff) | standard-setter | https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/ | 2026-04-06 | full
KPMG-SOC-2026 | The future of SOC reporting: Mastering AI risks and the changing Trust Services Criteria (webcast page) | KPMG US | firm | https://kpmg.com/us/en/webcasts/2026/soc-reporting-ai-risks-trust-services-criteria.html | 2026-09-22 | full
KPMGUK-CONTROLS-2026 | Reimagining Controls Assurance with AI: Latest Insights for Leaders (SOC 1, SOC 2, ISAE 3402, ISAE (UK) 3000, AAF 01/20, AAF 05/20) | KPMG in the UK | firm | https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf | 2026-01 | full
LINFORD-AIML-2023 | SOC 2 Audit Considerations for AI & ML Subservice Organizations | Linford & Company | firm | https://linfordco.com/blog/soc-2-audit-considerations-ai-ml-platforms/ | 2023-07-05 | full
LINFORD-ASSURE-2026 | AI Made Compliance Cheaper. It Didn't Make Assurance Cheaper. | Linford & Company | firm | https://linfordco.com/blog/ai-compliance-vs-assurance/ | 2026-09-23 | full
LINFORD-FAQ-2022 | AICPA FAQs on SOC 2 Automation Tools: Insights from an Auditor | Linford & Company | firm | https://linfordco.com/blog/soc-2-automation-tools-aicpa-faqs | 2022-06-15 | full
LINFORD-TOOLS-2021 | How Does the Usage of SOC 2 Software Tools Affect SOC 2 Audits? | Linford & Company | firm | https://linfordco.com/blog/using-soc-2-software-tools-for-audit-compliance | 2021-12-22 | full
ONELEET-2026 | Oneleet: security-first compliance (home page) | Oneleet | vendor | https://www.oneleet.com/ | 2026-10 | full
SACRA-VANTA-2026 | $300M/year SOC 2 for AI (Vanta update) | Sacra | press | https://sacra.com/research/vanta-at-300m-year/ | 2026-04-30 | full
SCHELLMAN-2026 | Schellman Learning Center and services navigation (blog index) | Schellman | firm | https://www.schellman.com/blog | 2026-10 | full
SDOWNS-TQA9561-2026 | AI in SOC Examinations: What the AICPA's New TQA Section 9561 Means for Service Organizations | Schneider Downs | firm | https://schneiderdowns.com/our-thoughts-on/ai-in-soc-examinations-what-the-aicpas-new-tqa-section-9561-means-for-service-organizations/ | 2026-09-30 | full
SECUREFRAME-2026 | Secureframe: build trust, unlock growth (home page) | Secureframe | vendor | https://secureframe.com/ | 2026-10 | full
SOC2AUDITORS-AI-2026 | SOC 2 auditors for AI companies: 26 firms compared (lead-generation directory) | SOC2Auditors.org | vendor | https://soc2auditors.org/soc-2-auditors-ai/ | 2026-10-09 | full
SOC2AUDITORS-COST-2026 | SOC 2 audit cost in 2026: fees and budget (lead-generation directory) | SOC2Auditors.org | vendor | https://soc2auditors.org/soc-2-audit-cost/ | 2026-10-05 | full
TECHCRUNCH-COMPAI-2026 | Comp AI sets eyes on a continuously agentic future for security and compliance | TechCrunch | press | https://techcrunch.com/2026/09/17/comp-ai-sets-eyes-on-a-continiously-agentic-future-for-security-and-complaince/ | 2026-09-17 | full
TECHCRUNCH-CONTEXT-2026 | Another customer of troubled startup Delve suffered a big security incident | TechCrunch | press | https://techcrunch.com/2026/04/23/another-customer-of-troubled-startup-delve-suffered-a-big-security-incident/ | 2026-04-23 | full
TECHCRUNCH-DELVE-2026 | Delve accused of misleading customers with 'fake compliance' | TechCrunch | press | https://techcrunch.com/2026/03/21/delve-accused-of-misleading-customers-with-fake-compliance/ | 2026-03-22 | full
TECHCRUNCH-DELVE2-2026 | Delve whistleblower strikes again, with alleged receipts about 'fake compliance' | TechCrunch | press | https://techcrunch.com/2026/03/30/delve-whistleblower-strikes-again-with-alleged-receipts-about-fake-compliance/ | 2026-03-30 | full
TECHCRUNCH-DELVEYC-2026 | Embattled startup Delve has 'parted ways' with Y Combinator | TechCrunch | press | https://techcrunch.com/2026/04/04/embattled-startup-delve-has-parted-ways-with-y-combinator/ | 2026-04-04 | full
TECHCRUNCH-LITELLM-2026 | Popular AI gateway startup LiteLLM ditches controversial startup Delve | TechCrunch | press | https://techcrunch.com/2026/03/30/popular-ai-gateway-startup-litellm-ditches-controversial-startup-delve/ | 2026-03-30 | full
THOROPASS-2026 | Thoropass: auditor-led, AI-powered audits (home page) | Thoropass | vendor | https://www.thoropass.com/ | 2026-10 | full
VANTA-AI-2026 | Vanta AI: Your 24/7 GRC engineer for security and compliance (product page) | Vanta | vendor | https://www.vanta.com/products/ai | 2026-10 | full
VANTA-AUDIT-2026 | Compliance audit software: Streamline your audit experience (product page) | Vanta | vendor | https://www.vanta.com/products/audit | 2026-10 | full
VANTA-AUDITORS-2026 | Vanta for Auditors: Become a Vanta auditor (partner page) | Vanta | vendor | https://www.vanta.com/partners/auditors | 2026-10 | full
VANTA-Q5AUDITOR-2025 | Choosing a trusted auditor: 5 key questions to ask your potential auditor | Vanta | vendor | https://www.vanta.com/resources/5-key-questions-to-ask-your-auditor | 2025-03-21 | full
VERDICT-VANTA-2026 | Vanta introduces automation tools to streamline enterprise compliance | Verdict | press | https://www.verdict.co.uk/vanta-introduces-automation-tools/ | 2026-03-20 | full

**Count by type (48 sources):** vendor 15, firm 10, press 9, professional-body 4, standard-setter 4, job-posting 2, conference 1, podcast 1, survey 1, community 1. No regulator or academic source applies to this angle (see Gaps).

Date notes: dates marked with a month only (for example 2026-10) are product, home and landing pages with no publication date; the month is the access date. ALIGN-BENCH-2026 is dated from the asset path (January 2026 uploads). FIELDGUIDE-WEAVER-2026 and FIELDGUIDE-SOC-2026 use the page's last-modified date. HN-CHIARO-2026 is dated from "73 days ago". KPMG-SOC-2026 carries the page's publication date; the webcast date was not stated. FIELDGUIDE-FINAUDIT-2025 is dated from its text (June 2025) and the sitemap. TECHCRUNCH-DELVE-2026 was first posted 21 March and updated 22 March.

---

## 6. Gaps

- **Search allowance.** Web search ran out partway through, so no further discovery searches were possible. Remaining leads were followed by direct fetches only.
- **No independent quality evidence.** No error rate, override rate, parallel-run result, inspection finding or peer-review statistic for AI use in SOC engagements. No academic study on AI in SOC or attest work. The AICPA's SOC Quality Center, if built, would be a source.
- **Delve.** The allegations are unproven and Delve denies them. The 493-report figure appears only in Sacra's summary (SACRA-VANTA-2026) and in a secondary blog that could not be dated, so it is not used as fact. A WebProNews article on the story gives funding and valuation figures that contradict TechCrunch's, so it was excluded. The last development found is dated 23 April 2026; the outcome of the AICPA's inquiry, any state-board action, and the class action mentioned in search results are unknown.
- **SOC specialist firms.** Schellman (SCHELLMAN-2026) and BARR (BARR-2026) publish nothing found on their own use of AI in examinations (BARR's pages show AI governance content only); Coalfire and Prescient were not reached. A-LIGN's pages describe the platform, not audit methodology change. The 2026 A-LIGN benchmark PDF is gated; the 60% figure came from an image and a 95% "using technology" figure was not confirmed.
- **Big Four SOC practices.** Only EY (conference highlights) and KPMG (UK report, US webcast page) were reached; no Deloitte or PwC SOC AI material; no BDO, Grant Thornton, Baker Tilly or Armanino statements on SOC AI use.
- **ISAE 3402 and ISAE 3000.** Outside KPMG UK, no practice evidence from Europe or elsewhere; no NOREA, ICAEW or IAASB material on AI in these engagements.
- **Bridge letters, SOC 1 and SOC 3.** No AI-specific evidence on bridge letters or SOC 3; SOC 1 appears only through KPMG UK and TQA 9561.
- **Gated or blocked.** AICPA TQA 9561 and the AICPA software-tools FAQ (free login); Business Wire releases for Vanta's Agentic Trust Platform (Nov 2025) and Agent for Risk (Jun 2026) (403; seen only in search results, not used); Drata's June 2026 release (403); a Deloitte DART SOC page (not found); Going Concern and Reddit (not attempted); the GitHub repository behind HN-CHIARO-2026 (not reachable); the PCI SSC AI guidance cited by Linford (URL tried returned 404).
- **Search-only items not used as evidence:** Fieldguide claims of 36-50 hours saved per SOC engagement and 66% less time drafting test procedures; BARR's reported Audit AI and MCP connectors; Vanta's reported customer count above 16,000; Secureframe, Sprinto and Thoropass feature descriptions from review sites.
- **Pricing.** Only a lead-generation directory with listed bands and ballpark quotes; no fee data from auditing firms or buyers.
- **Conflict to resolve.** KPMG's webcast page says Trust Services Criteria changes are forthcoming; CSA says no AICPA activity on AI-specific criteria exists. CSA also describes proposed revisions to AT-C 105, 205 and 210 aimed at sustainability and general methodology, not effective before mid-2029 (CSA-SOC2-2026, secondary; not checked against AICPA sources).

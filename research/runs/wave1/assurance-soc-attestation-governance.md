# Module deep dive: assurance / soc-attestation / governance & evidence

- **Archetype:** assurance
- **Module:** soc-attestation: SOC 1 / SOC 2 / SOC 3 and ISAE 3402 / ISAE 3000 service-organization examinations and other attestation engagements, end to end, plus compliance-automation platforms and quality concerns about commoditized SOC 2. Individual control tests are covered by the controls-testing module.
- **Angle:** governance & evidence
- **Prepared:** 2026-10-16
- **Inputs:** `research/runs/wave1/landscape-assurance.md` (section 13, other-assurance leads) and `research/briefs/templates/vocabulary.md`
- **Access note:** `access: full` means this analyst opened the page or PDF. Where a document sits behind an AICPA login, only the landing page was read and the locator says so. One source (EY SOC conference poll) is carried from the landscape file and is marked `search-only`. The web-search quota ran out during this task, so several planned searches did not run (see Gaps).

---

## 1. Summary

- **The profession's governance response to "fast and easy" SOC 2 arrived in a burst in 2026, and it is guidance and peer-review pressure, not enforcement.**
  - Journal of Accountancy (1 Feb 2026): the chair of the AICPA SOC 2 Working Group says "fast and easy" may come at the expense of quality and objectivity. Tool vendors now number in the dozens (JOFA-FAST-2026).
  - AICPA ethics article (6 Apr 2026) and Ethics Staff Insights (13 Apr 2026): contract terms that shift control, judgment, fees or evidence access to a tool provider can create independence and objectivity threats (JOFA-SOCETH-2026, AICPA-ESISOC-2026).
  - Peer review alert (May 2026): engagements with identical reports, risk assessments, sample sizes and tests are "nonconforming" in peer review. Staff outreach to team captains was planned to start 1 Jun 2026 (JOFA-PEER-2026).
  - AICPA TQA 9561 on a service organisation's use of AI in SOC 1 and SOC 2 examinations: 11 Sep 2026; full text gated (AICPA-TQA9561-2026).
  - No regulator or state-board enforcement action against a named SOC firm was found. The AICPA says it is looking into allegations about a compliance vendor (AICPA-SOC-2026).
- **The one public test case is an anonymous allegation, not a finding.** In March 2026 an anonymous author alleged that the vendor Delve pre-wrote auditor conclusions for SOC 2 reports and routed customers through two firms. Delve and one named firm deny it (DEEPDELVER-2026, TC-DELVE-2026, DELVE-RESPONSE-2026). Delve apologised on 3 Apr 2026 and said it would rebuild its auditor network (DELVE-RECORD-2026). Independent verification was not found.
- **Independent quality evidence is missing.** No SOC error, qualification or nonconformance rate was found. Two state peer review administering-entity reports for 2025 show zero SOC engagements reviewed (OSCPA-PR-2026, LASCPA-PR-2026). The AAA's 2023 call for research says little is known about how auditors perform or rely on SOC services (AAA-CIIA-2023). The only inspection evidence is adjacent: PCAOB found deficiencies in auditors' testing of data and reports, including service-organisation information (PCAOB-DATA-2024).
- **Most of the "AI" in SOC practice is automation of evidence collection and drafting.** Vendor pages describe AI features; the only figures are vendor-published and undefined. The anonymous Delve author alleges that its "AI" was thin; that is an allegation (TC-DELVE-2026).
- **The standards have not changed for tools or for AI.** SOC 2 still uses the 2017 Trust Services Criteria with 2022 points of focus, and no AI-specific criteria existed as of 13 Oct 2026 (AICPA-TSC-2023 listing; SOC2AUDITORS-AI-2026, CSA-SOC2-2026). The ASB's attestation exposure drafts (Feb and Mar 2026; effective 15 Jun 2029 if finalised) address baseline concepts and sustainability, not AI (JOFA-ATTEST-2026).
- **12 candidate use cases:** 4 at grade B, 7 at grade C, 1 at grade D (labelled idea), none at A. No named organisation published a measured outcome for any of them.
- **Cautions on secondary sources** are in section 3, including three places where commentary misdates or overstates the primary text.

---

## 2. Use cases

```yaml
- id: assurance-soc-attestation-01
  title: Continuous control monitoring and evidence collection by a compliance-automation platform (service-organisation side)
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - data-reporting
  - review-assurance
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Preparing for a SOC 2 or SOC 1 examination used to mean gathering screenshots and spreadsheets by hand, and keeping controls running between annual examinations.
  solution: A platform connects to the service organisation's cloud and SaaS systems, pulls control evidence on a schedule, monitors configurations against mapped controls and shows status in a dashboard. The service auditor can later use the same data. The sources describe this as automation and integration. Only vendor pages describe AI inside it.
  outcomes:
  - lever: speed
    description: SOC practitioners say the tools make the examination process quicker and more efficient. No time or cost figure is published in the source.
    figure: none published
    measures: Not a measured result; practitioner statement in a trade article.
    provenance: self-reported
    source_ref: JOFA-FAST-2026
  prerequisites:
  - Integrations to every in-scope system (APIs), correctly configured, so the tool covers the whole system boundary.
  - A named control owner on the service-organisation side who reviews and remediates tool findings; tools do not remediate controls.
  - A choice of CPA firm that is independent of the tool provider.
  risks_and_guardrails:
  - Tools confirm that a configuration is on for the assets they see; they do not show that it is effective across the environment (KPMG-CHECKBOX-2026, p. 3).
  - A broken integration can leave outdated data in the tool, so reliance would rest on stale evidence (LINFORD-FAQ-2022).
  - Management may over-rely on the tool or leave templated policies and risk assessments unadapted to its own risks (LINFORD-FAQ-2022).
  - A tool provider that supplies vital operations to the service organisation may itself be a candidate subservice organisation, in one practitioner's view (LINFORD-TOOLS-2021).
  human_checkpoints:
  - Service organisation reviews exceptions and decides remediation.
  - Service auditor evaluates whether the tool's coverage matches the system description before relying on its data.
  role_evolution: Service auditors can spend less time collecting evidence and more on control execution and management oversight, per one Big Four firm's guide (KPMG-CHECKBOX-2026, p. 4). The AICPA warns that firms must keep exercising their own judgment (JOFA-PEER-2026).
  evidence_grade: B
  notes: Grade B rests on named tools and a named customer (Wispr Flow with Drata), not on any measurement. No independent measure of time saved or quality effect was found. The EY conference poll (63% of attendees chose AI for evidence collection; multiple answers allowed; respondent count not captured) is carried from the landscape file and is not an A or B basis.
  last_reviewed: '2026-10-16'
  sources:
  - ref: JOFA-FAST-2026
    title: Promises of 'fast and easy' threaten SOC credibility
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/
    date: '2026-02-01'
    access: full
    locator: Section 'The rise of SOC tool vendors'
  - ref: KPMG-CHECKBOX-2026
    title: 'Beyond the Checkbox: How Confident Are You in Your SOC 2 Reports?'
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/beyond-checkbox.pdf
    date: 2026-07
    access: full
    locator: pp. 2-3, 'The Rise of SOC 2 Tools' table
  - ref: LINFORD-FAQ-2022
    title: 'AICPA FAQs on SOC 2 Automation Tools: Insights from an Auditor'
    publisher: Linford & Co
    type: firm
    url: https://linfordco.com/blog/soc-2-automation-tools-aicpa-faqs
    date: '2022-06-15'
    access: full
    locator: Sections on integrations and risks
  - ref: LINFORD-TOOLS-2021
    title: 'SOC 2 Software Tools: How They Affect the SOC Audit Process'
    publisher: Linford & Co
    type: firm
    url: https://linfordco.com/blog/using-soc-2-software-tools-for-audit-compliance
    date: '2021-12-22'
    access: full
    locator: Functionality list; 'Type of reliance' section (names Vanta, Drata and Tugboat Logic as tools the author has used)
  - ref: WISPR-2026
    title: Our path to a new, independent audit
    publisher: Wispr Flow (customer company blog)
    type: firm
    url: https://wisprflow.ai/post/new-independent-audit
    date: '2026-03-27'
    access: full
    locator: Paragraphs 2-3 (engaged Drata for continuous, automated monitoring; named customer)
  - ref: EY-SOC-2026
    title: EY SOC, Attestation and Certification Conference (14th annual) highlights, as summarised in the wave 1 landscape file (page not re-opened by this analyst)
    publisher: EY
    type: conference
    url: research/runs/wave1/landscape-assurance.md (section 9, item S8; EY page URL not given there)
    date: 2026-09
    access: search-only
    locator: Live-poll figure of 63% for evidence collection is carried from the landscape file (section 9, S8); not re-opened
- id: assurance-soc-attestation-02
  title: Service auditor tests technical controls from tool-collected, population-level evidence through an auditor portal
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Service auditors have traditionally requested evidence item by item, observed screen shares and tested samples, which is slow for both sides.
  solution: The service organisation gives the service auditor access to the platform. The auditor pulls evidence directly, reviews configuration and population data for technical controls, and does the remaining testing outside the tool. One practitioner says the auditor can do much of the work in the tool without help from the client.
  outcomes:
  - lever: speed
    description: Less client effort during the examination and less auditor time spent requesting evidence, according to one SOC practitioner. No figure published.
    figure: none published
    measures: Practitioner statement; no numerator or denominator.
    provenance: self-reported
    source_ref: LINFORD-TOOLS-2021
  prerequisites:
  - Auditor understands what each integration provides and how reports (for example CSV exports) are generated.
  - Auditor can reach source systems for higher-risk controls.
  - Independence from the tool provider assessed and documented.
  risks_and_guardrails:
  - The AICPA's peer review leadership says some firms lean too heavily on third-party SOC platforms without applying the judgment the standards require (JOFA-PEER-2026).
  - Engagements with identical reports, risk assessments, sample sizes and testing procedures can be judged nonconforming in peer review (JOFA-PEER-2026).
  - ISAE 3402 requires other procedures in combination with enquiry, to learn how, how consistently and by whom a control was applied (XRB-3402-2026, para 25(a)).
  - A report downloaded from a tool can be edited after it is generated; the auditor should not rely on a report whose parameters they do not understand (LINFORD-FAQ-2022).
  - A service auditor cannot simply download the tool's report and issue it; data from the tool needs validation, sometimes at the source system (LINFORD-FAQ-2022).
  human_checkpoints:
  - Auditor validates tool data against source for higher-risk controls.
  - Auditor sets scope, timing and sample sizes by professional judgment, not tool defaults.
  - Engagement partner reviews the tailoring of the risk assessment and tests.
  role_evolution: Peer reviewers are told that reviewing a single SOC 2 file is often insufficient and that they may select about five engagements from different partners and compare them (JOFA-PEER-2026).
  evidence_grade: B
  notes: Grade B is based on practitioner descriptions of normal use, not published measurements. XRB-3402-2026 is New Zealand's adoption of ISAE 3402; the paragraph cited mirrors the international text but this analyst did not open the IAASB original.
  last_reviewed: '2026-10-16'
  sources:
  - ref: LINFORD-TOOLS-2021
    title: 'SOC 2 Software Tools: How They Affect the SOC Audit Process'
    publisher: Linford & Co
    type: firm
    url: https://linfordco.com/blog/using-soc-2-software-tools-for-audit-compliance
    date: '2021-12-22'
    access: full
    locator: Section 'How does the use of a SOC 2 compliance software tool impact the SOC audit process?'
  - ref: LINFORD-FAQ-2022
    title: 'AICPA FAQs on SOC 2 Automation Tools: Insights from an Auditor'
    publisher: Linford & Co
    type: firm
    url: https://linfordco.com/blog/soc-2-automation-tools-aicpa-faqs
    date: '2022-06-15'
    access: full
    locator: Sections 'CPA firms still need to follow SOC 2 guidance' and the CSV example
  - ref: JOFA-PEER-2026
    title: AICPA guides peer reviewers to address SOC 2 risks
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/
    date: '2026-05-14'
    access: full
    locator: Sections 'A heightened focus on SOC 2 quality' and 'Responding when elevated risks are identified'
  - ref: XRB-3402-2026
    title: International Standard on Assurance Engagements (New Zealand) 3402, Assurance Reports on Controls at a Service Organisation (XRB 2026/44)
    publisher: NZ Auditing and Assurance Standards Board / External Reporting Board
    type: standard-setter
    url: https://www.xrb.govt.nz/dmsdocument/5983/
    date: '2026-04-09'
    access: full
    locator: Paragraph 25
  - ref: WISPR-2026
    title: Our path to a new, independent audit
    publisher: Wispr Flow (customer company blog)
    type: firm
    url: https://wisprflow.ai/post/new-independent-audit
    date: '2026-03-27'
    access: full
    locator: Paragraph 3 (customer chose A-LIGN after assessing its independence from the platform)
- id: assurance-soc-attestation-03
  title: 'Platform-generated readiness documents: policy library, risk-assessment questions and draft system description'
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Service organisations preparing for a first SOC 2 must write policies, a risk assessment and a system description from scratch.
  solution: The platform supplies policy templates, predefined risk-assessment questions and, in Vanta's case as described on its own page, an auto-generated SOC 2 system description. Vanta's page says its agent also maps and summarises policies and evaluates evidence. Management is expected to edit the drafts.
  outcomes:
  - lever: speed
    description: Vendor page describes auto-generation of the system description and policy support. No time saving is stated.
    figure: none published
    measures: No figure in source.
    provenance: vendor-published
    source_ref: VANTA-VS-2026
  prerequisites:
  - Management reviews and adapts every draft to its own services and risks.
  - Service auditor evaluates the description against the criteria.
  risks_and_guardrails:
  - Templated policies and predefined risk questions may not cover a client's unique industry risks, so significant risks can go unidentified (LINFORD-FAQ-2022).
  - Delve says draft templates are not the same as pre-filled evidence (quoted in TC-DELVE-2026). The anonymous allegations say customers adopted templates as evidence of processes that did not happen (DEEPDELVER-2026, TC-DELVE-2026). Delve disputes this.
  - Tool-provider involvement in the examination can create self-interest or undue-influence threats for the CPA (JOFA-SOCETH-2026).
  human_checkpoints:
  - Management owns and signs the description and assertion.
  - Auditor tests whether the description fairly presents the system.
  role_evolution: Readiness consultants and preparers move from drafting to adapting and challenging generated text. The sources do not describe any change in headcount.
  evidence_grade: C
  notes: Grade C because the only description of the AI features is vendor-published. The EY conference poll in the landscape file puts drafting the Section 3 system description at 45% of attendees' AI uses (carried from the landscape file; not re-opened).
  last_reviewed: '2026-10-16'
  sources:
  - ref: VANTA-VS-2026
    title: Vanta vs. Drata vs. Delve
    publisher: Vanta
    type: vendor
    url: https://vanta.com/resources/vanta-vs-drata-vs-delve
    date: '2026-03-22'
    access: full
    locator: Audit-readiness and AI sections (vendor comparison page; competitor claims about Delve are marketing)
  - ref: LINFORD-FAQ-2022
    title: 'AICPA FAQs on SOC 2 Automation Tools: Insights from an Auditor'
    publisher: Linford & Co
    type: firm
    url: https://linfordco.com/blog/soc-2-automation-tools-aicpa-faqs
    date: '2022-06-15'
    access: full
    locator: Section 'What are the risks arising from the use of SOC 2 automation tools?'
  - ref: TC-DELVE-2026
    title: Delve accused of misleading customers with 'fake compliance'
    publisher: TechCrunch
    type: press
    url: https://techcrunch.com/2026/03/21/delve-accused-of-misleading-customers-with-fake-compliance/
    date: '2026-03-22'
    access: full
    locator: Delve's response paragraphs
  - ref: DEEPDELVER-2026
    title: Delve - Fake Compliance as a Service - Part I (anonymous allegations)
    publisher: DeepDelver (pseudonymous Substack)
    type: community
    url: https://deepdelver.substack.com/p/delve-fake-compliance-as-a-service
    date: '2026-03-19'
    access: full
    locator: Opening summary of allegations
  - ref: JOFA-SOCETH-2026
    title: 'SOC engagements: Ethics risks with tool providers'
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/
    date: '2026-04-06'
    access: full
    locator: Section 'Common threats'
- id: assurance-soc-attestation-04
  title: Platform-drafted report text and test results ahead of auditor testing (contested practice)
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Drafting a SOC 2 report (system description, test procedures, results, opinion) is time-consuming for the service auditor.
  solution: A platform gives auditors a dashboard and produces a draft report for the customer to edit; the auditor then tests and issues the final report. Delve describes this flow. The anonymous allegations say draft reports already held conclusions and test procedures before any evidence existed, and were signed without change. Delve and Accorp deny wrongdoing. The AICPA describes, without naming anyone, vendors allegedly drafting boilerplate reports signed by a CPA with no involvement.
  outcomes:
  - lever: speed
    description: The vendor's stated benefit is speed. The sources contain no published measure of quality or time for this pattern. The allegation-based figures are in notes.
    figure: none published
    measures: No figure from the deployer or from an independent party.
    provenance: vendor-published
    source_ref: DELVE-RESPONSE-2026
  prerequisites:
  - A CPA firm licensed by the state, enrolled in peer review, that designs and runs its own tests.
  - Written account of who drafted the opinion and test results, and when.
  risks_and_guardrails:
  - The AICPA says CPAs enrolled in peer review that do this should expect deficiencies; licensed CPAs outside peer review, or unlicensed signatories, may violate state law (JOFA-POD-2026).
  - Engagements with identical reports, risk assessments, sample sizes and procedures can be judged nonconforming (JOFA-PEER-2026).
  - A tool provider that is the 'responsible party' under the attestation standards requires the CPA to be independent of it too (JOFA-SOCETH-2026).
  - In a Dec 2022 alert the AICPA said non-CPA tool providers contracting with CPA firms to deliver an examination from tool data may create a self-review threat, and some tool-provider sites listed providers that did not appear to be licensed CPA firms, as summarised by Grant Thornton (GT-SOC2-2023).
  - Sources are mostly allegations from one anonymous author plus the vendor's denial. No regulator finding on any named firm was found (AICPA-SOC-2026 says the AICPA is looking into allegations).
  human_checkpoints:
  - Auditor-authored test procedures and conclusions, supported by auditor evidence, before any opinion is drafted.
  - Independence and licence checks by the buyer (CPAverify, state board, peer review public file).
  role_evolution: If the pattern is real, the signing CPA's role shrinks to a signature, which the AICPA treats as a breach. Standards-compliant use keeps the CPA as author of the tests and the opinion.
  evidence_grade: C
  notes: 'Allegation-based figures, from an anonymous author and not verified by an independent party: in a leaked set of 575 files (81 not SOC 2), the author reports one test-procedure string in 493 of 494 SOC 2 reports (99.8%) and an identical auditor-conclusion sentence in 259 of 259 SOC 2 Type II reports (DEEPDELVER-2026, section 5). IANS repeats these figures as allegations (IANS-DELVE-2026). Delve disputes the characterisation. Grade C because there is no published measurement and the practice is contested.'
  last_reviewed: '2026-10-16'
  sources:
  - ref: DELVE-RESPONSE-2026
    title: Response to Misleading Claims
    publisher: Delve
    type: vendor
    url: https://delve.co/blog/response-to-misleading-claims
    date: '2026-03-20'
    access: full
    locator: Point 1 ('Delve does not conduct audits...') describing draft report and auditor dashboard
  - ref: DEEPDELVER-2026
    title: Delve - Fake Compliance as a Service - Part I (anonymous allegations)
    publisher: DeepDelver (pseudonymous Substack)
    type: community
    url: https://deepdelver.substack.com/p/delve-fake-compliance-as-a-service
    date: '2026-03-19'
    access: full
    locator: Sections 5 and 6 on analysis of leaked reports
  - ref: TC-DELVE-2026
    title: Delve accused of misleading customers with 'fake compliance'
    publisher: TechCrunch
    type: press
    url: https://techcrunch.com/2026/03/21/delve-accused-of-misleading-customers-with-fake-compliance/
    date: '2026-03-22'
    access: full
    locator: Allegation and response paragraphs
  - ref: JOFA-POD-2026
    title: The risks of quick-turn SOC engagements and what CPAs should know (podcast with Amy Pawlicki, AICPA)
    publisher: Journal of Accountancy (AICPA)
    type: podcast
    url: https://www.journalofaccountancy.com/podcast/2026/apr/the-risks-of-quick%E2%80%91turn-soc-engagements-and-what-cpas-should-know/
    date: '2026-04-30'
    access: full
    locator: Pawlicki answer on 'the biggest problem we've seen in the marketplace'
  - ref: JOFA-PEER-2026
    title: AICPA guides peer reviewers to address SOC 2 risks
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/
    date: '2026-05-14'
    access: full
    locator: Section 'A heightened focus on SOC 2 quality'
  - ref: AICPA-SOC-2026
    title: 'System and Organization Controls: SOC Suite of Services (landing page with notice on allegations about a compliance vendor)'
    publisher: AICPA & CIMA
    type: standard-setter
    url: https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services
    date: '2026'
    access: full
    locator: Notice at top of page
  - ref: IANS-DELVE-2026
    title: Delve Allegations Expose Weak Points in Modern Compliance
    publisher: IANS Research
    type: vendor
    url: https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/03/30/delve-allegations-expose-weak-points-in-modern-compliance
    date: '2026-03-24'
    access: full
    locator: Key points and quoted analysis
  - ref: GT-SOC2-2023
    title: What businesses need to know about SOC 2 developments
    publisher: Grant Thornton US
    type: firm
    url: https://www.grantthornton.com/insights/articles/advisory/2023/what-businesses-need-to-know-about-soc-2-developments
    date: '2023-02-16'
    access: full
    locator: Section 'Focus on tools'
  - ref: SOC2AUDITORS-DELVE-2026
    title: 'Delve Review (2026): Who Actually Audits You?'
    publisher: SOC2Auditors.org (comparison site)
    type: press
    url: https://soc2auditors.org/insights/delve-review/
    date: '2026-10-13'
    access: full
    locator: Dispute table (secondary summary of Accorp's and Delve's denials)
- id: assurance-soc-attestation-05
  title: 'Bundled ''SOC-as-a-service'': platform plus affiliated auditor network at a quick, flat price'
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - transaction-processing
  - review-assurance
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: workflow-automation
  maturity: in-production
  problem: Startups need a SOC 2 report quickly to close enterprise deals and find traditional examinations slow and costly.
  solution: A platform vendor sells readiness, evidence collection and the examination as one package through its own network of CPA firms, with quick turnaround and a low flat fee. The AICPA describes vendors who aim to automate the service entirely. The vendor says it grants auditors dashboard access, offers its network or any auditor of the customer's choice, and that final opinions come only from licensed auditors.
  outcomes:
  - lever: cost
    description: Vendors promise quick turnaround and very low flat-rate prices. No price or timing figure is published in the sources opened.
    figure: none published
    measures: No figure; marketing promises described qualitatively by the AICPA.
    provenance: vendor-published
    source_ref: JOFA-POD-2026
  prerequisites:
  - Fee, scope and timing set by the CPA, not the vendor.
  - Disclosure of referral fees to the client where payments are in substance referral fees.
  risks_and_guardrails:
  - A bundled model where the tool provider sets the examination fee can impair independence; the CPA must set the fee by professional judgment (JOFA-SOCETH-2026, citing ET 1.230.030).
  - Concentrated cross-referrals, vendor deadlines, vendor rights to observe the work and 'non-disparagement' clauses are named as threats to independence and to compliance with the standards (JOFA-SOCETH-2026).
  - Guaranteeing outcomes ('clean audit', '100% pass rate') may breach the advertising rule, and a CPA cannot outsource misleading marketing to a vendor (JOFA-SOCETH-2026).
  - Small numbers of firms signing high volumes of reports, sometimes with overseas operations, were raised by SOC leaders (JOFA-FAST-2026).
  - After the March 2026 allegations Delve apologised, said it would rebuild its auditor network and remove firms that do not meet its standards, and offered re-audits (DELVE-RECORD-2026, DELVE-CHANGES-2026).
  human_checkpoints:
  - Buyer vets the signing firm, licence and peer review result.
  - CPA's engagement letter states who sets scope, sampling and fee.
  role_evolution: Mid-market SOC practices face fee pressure to match speed and volume; SOC leaders advise explaining why quality takes time and cost (JOFA-FAST-2026).
  evidence_grade: B
  notes: Grade B because a named vendor operates the model and acknowledges an auditor network. Quality outcomes are contested and unmeasured. Secondary reporting (SOC2AUDITORS-DELVE-2026) says Delve and Y Combinator parted in April 2026 and lists two federal suits filed in April 2026 with no ruling on the allegations; this analyst did not check court dockets (CourtListener rate-limited the request).
  last_reviewed: '2026-10-16'
  sources:
  - ref: JOFA-POD-2026
    title: The risks of quick-turn SOC engagements and what CPAs should know (podcast with Amy Pawlicki, AICPA)
    publisher: Journal of Accountancy (AICPA)
    type: podcast
    url: https://www.journalofaccountancy.com/podcast/2026/apr/the-risks-of-quick%E2%80%91turn-soc-engagements-and-what-cpas-should-know/
    date: '2026-04-30'
    access: full
    locator: Pawlicki answers on vendors that 'automate the service entirely'
  - ref: JOFA-FAST-2026
    title: Promises of 'fast and easy' threaten SOC credibility
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/
    date: '2026-02-01'
    access: full
    locator: Sections 'What's the issue?' and 'How can SOC examiners respond?'
  - ref: JOFA-SOCETH-2026
    title: 'SOC engagements: Ethics risks with tool providers'
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/
    date: '2026-04-06'
    access: full
    locator: Sections 'Objectivity, conflicts of interest, and independence' and 'Advertising and other forms of solicitation'
  - ref: DELVE-RESPONSE-2026
    title: Response to Misleading Claims
    publisher: Delve
    type: vendor
    url: https://delve.co/blog/response-to-misleading-claims
    date: '2026-03-20'
    access: full
    locator: Points 1 and 2
  - ref: DELVE-RECORD-2026
    title: Delve sets the record straight on anonymous attacks (apology and changes)
    publisher: Delve
    type: vendor
    url: https://delve.co/blog/delve-sets-the-record-straight-on-anonymous-attacks
    date: '2026-04-03'
    access: full
    locator: List of changes
  - ref: DELVE-CHANGES-2026
    title: Delve Announces Changes and New Customer Support Measures
    publisher: Delve
    type: vendor
    url: https://delve.co/blog/delve-announces-changes-and-new-customer-support-measures
    date: '2026-03-24'
    access: full
    locator: '''New Customer Support Measures'''
  - ref: SOC2AUDITORS-DELVE-2026
    title: 'Delve Review (2026): Who Actually Audits You?'
    publisher: SOC2Auditors.org (comparison site)
    type: press
    url: https://soc2auditors.org/insights/delve-review/
    date: '2026-10-13'
    access: full
    locator: Summary of Delve statements and later events (secondary; court details not independently checked)
- id: assurance-soc-attestation-06
  title: Platform-curated auditor network and audit hub for scheduling, evidence requests and auditor access
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Examination timelines slip on evidence requests, access provisioning and coordination between service organisation and auditor.
  solution: Platforms run an auditor portal with scoped access and comments, and keep a list of audit-firm partners. Vanta describes an integrated auditor portal that limits evidence to what auditors need. Drata describes a partner ecosystem with expectations on quality and the ability to remove firms, and says it has never bundled audits.
  outcomes:
  - lever: speed
    description: Vendor pages describe less back-and-forth. No figure.
    figure: none published
    measures: No figure in source.
    provenance: vendor-published
    source_ref: VANTA-VS-2026
  prerequisites:
  - Auditor selected on independence from the platform.
  - Written clarity on who owns scope, sampling and drafting.
  risks_and_guardrails:
  - Cross-referral concentration between a tool provider and a CPA firm is a named independence threat (JOFA-SOCETH-2026).
  - A customer that left Delve said it assessed the new auditor's independence from its GRC platform before signing (WISPR-2026).
  - 'Drata states four pillars: independence, quality over speed, oversight of its audit ecosystem, and transparency about who the auditor is (DRATA-INTEGRITY-2026). These are vendor statements.'
  human_checkpoints:
  - Buyer asks the CPA, in writing, about referral or revenue arrangements with the platform (SOC2AUDITORS-DELVE-2026 buyer checklist).
  role_evolution: Project-management work in SOC engagements moves into platform workflows. The sources give no headcount effects.
  evidence_grade: B
  notes: Grade B rests on named platforms and a named customer; no outcome measurement exists. The EY conference poll in the landscape file gives project management at 29% of attendee AI uses (carried from the landscape file; not re-opened).
  last_reviewed: '2026-10-16'
  sources:
  - ref: VANTA-VS-2026
    title: Vanta vs. Drata vs. Delve
    publisher: Vanta
    type: vendor
    url: https://vanta.com/resources/vanta-vs-drata-vs-delve
    date: '2026-03-22'
    access: full
    locator: '''Audit readiness'' section'
  - ref: DRATA-INTEGRITY-2026
    title: 'SOC 2 Audit Integrity: Why Independence Matters'
    publisher: Drata
    type: vendor
    url: https://drata.com/blog/soc-2-audit-integrity
    date: '2026-01-09'
    access: full
    locator: Four pillars (page opened through a text mirror because the host returned 403)
  - ref: WISPR-2026
    title: Our path to a new, independent audit
    publisher: Wispr Flow (customer company blog)
    type: firm
    url: https://wisprflow.ai/post/new-independent-audit
    date: '2026-03-27'
    access: full
    locator: Paragraph 3
  - ref: JOFA-SOCETH-2026
    title: 'SOC engagements: Ethics risks with tool providers'
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/
    date: '2026-04-06'
    access: full
    locator: '''Objectivity, conflicts of interest, and independence'' list'
  - ref: SOC2AUDITORS-DELVE-2026
    title: 'Delve Review (2026): Who Actually Audits You?'
    publisher: SOC2Auditors.org (comparison site)
    type: press
    url: https://soc2auditors.org/insights/delve-review/
    date: '2026-10-13'
    access: full
    locator: Buyer checklist ('Named CPA' row); secondary
- id: assurance-soc-attestation-07
  title: Live trust centre fed by monitored controls, with AI chat for buyer questions
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - client-interaction
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Buyers ask service organisations the same security questions repeatedly and want current proof between annual reports.
  solution: A public trust page shows control status and documents, with gated access and an AI chatbot answering buyer questions. Vanta's page describes a trust centre with an AI chatbot, CRM-based gating and NDA automation.
  outcomes:
  - lever: experience
    description: Vendor page says the chatbot helps deflect inbound reviews. No figure.
    figure: none published
    measures: No figure in source.
    provenance: vendor-published
    source_ref: VANTA-VS-2026
  prerequisites:
  - Only controls that are implemented and monitored appear on the page.
  - A clear label that a trust page is not an attestation.
  risks_and_guardrails:
  - The anonymous allegations say some customers hosted trust pages listing measures that were never implemented (TC-DELVE-2026, DEEPDELVER-2026). Unverified.
  - The AICPA says a SOC 2 report is not a certification, and that compliance and certification badges imply every engagement is the same (JOFA-POD-2026).
  - IANS advises customers to narrow or remove public security claims until validated if their report is in doubt (IANS-DELVE-2026).
  human_checkpoints:
  - Security owner approves published claims.
  role_evolution: Security and sales-engineering teams spend less time on repeat questions. No source measures this.
  evidence_grade: C
  notes: Adjacent to attestation (it is a client-side publishing step) but central to how the market consumes SOC reports. Grade C because the only evidence of the AI feature is the vendor's own page.
  last_reviewed: '2026-10-16'
  sources:
  - ref: VANTA-VS-2026
    title: Vanta vs. Drata vs. Delve
    publisher: Vanta
    type: vendor
    url: https://vanta.com/resources/vanta-vs-drata-vs-delve
    date: '2026-03-22'
    access: full
    locator: '''Trust Center'' and AI sections'
  - ref: TC-DELVE-2026
    title: Delve accused of misleading customers with 'fake compliance'
    publisher: TechCrunch
    type: press
    url: https://techcrunch.com/2026/03/21/delve-accused-of-misleading-customers-with-fake-compliance/
    date: '2026-03-22'
    access: full
    locator: Paragraph on trust pages
  - ref: JOFA-POD-2026
    title: The risks of quick-turn SOC engagements and what CPAs should know (podcast with Amy Pawlicki, AICPA)
    publisher: Journal of Accountancy (AICPA)
    type: podcast
    url: https://www.journalofaccountancy.com/podcast/2026/apr/the-risks-of-quick%E2%80%91turn-soc-engagements-and-what-cpas-should-know/
    date: '2026-04-30'
    access: full
    locator: Opening explanation that SOC 2 is not a certification
  - ref: IANS-DELVE-2026
    title: Delve Allegations Expose Weak Points in Modern Compliance
    publisher: IANS Research
    type: vendor
    url: https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/03/30/delve-allegations-expose-weak-points-in-modern-compliance
    date: '2026-03-24'
    access: full
    locator: Faculty recommendations
- id: assurance-soc-attestation-08
  title: AI answers to security questionnaires drawn from SOC evidence and policy libraries
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - client-interaction
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Customers send long security questionnaires alongside, or in place of, a SOC report; answering them is repetitive.
  solution: 'The platform answers questionnaires from a tagged knowledge base of policies and evidence. '
  outcomes:
  - lever: speed
    description: Vanta's comparison page says questionnaires are completed up to 81% faster, with up to 73% coverage and 95% acceptance of generated responses.
    figure: up to 81% faster; up to 73% coverage; up to 95% acceptance
    measures: Page does not define the numerators, denominators or baseline for 'coverage', 'acceptance' or 'faster'.
    provenance: vendor-published
    source_ref: VANTA-VS-2026
  prerequisites:
  - A current, tagged knowledge base.
  - A reviewer who signs off answers before they are sent.
  risks_and_guardrails:
  - 'Answers inherit any gap between the policy library and what is implemented (the Delve allegations are about exactly that gap: DEEPDELVER-2026, unverified).'
  - Vendor figures are 'up to' maxima and come from a comparison page that also criticises competitors.
  human_checkpoints:
  - Reviewer approves answers before sending (a recommended control; the vendor page does not describe one).
  role_evolution: Not reported.
  evidence_grade: C
  notes: Outside the attest engagement itself; included because it competes with and complements SOC reports. Vendor-published only.
  last_reviewed: '2026-10-16'
  sources:
  - ref: VANTA-VS-2026
    title: Vanta vs. Drata vs. Delve
    publisher: Vanta
    type: vendor
    url: https://vanta.com/resources/vanta-vs-drata-vs-delve
    date: '2026-03-22'
    access: full
    locator: '''Questionnaire automation'' paragraph'
- id: assurance-soc-attestation-09
  title: 'Idea: cross-report similarity analysis by peer reviewers, buyers and investigators to detect templated SOC reports'
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: reconcile-exceptions
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Templated, look-alike reports are hard to spot one engagement at a time, so quality problems at high-volume SOC practices hide in plain sight.
  solution: Reviewers compare several engagements from different partners with each other and with prior-year reports, looking for identical risk assessments, control designs, sample sizes and test procedures. Anonymous investigators of one vendor ran text-frequency analysis across a leaked set of reports. Neither source says AI performed the comparison.
  outcomes:
  - lever: quality
    description: None published by a peer review body. The AICPA describes the manual procedure and says nonconforming conclusions raise the chance of deficiencies and follow-up actions.
    figure: none published
    measures: No finding rates for SOC engagements were found at national level; two state administering-entity reports show zero SOC engagements reviewed.
    provenance: self-reported
    source_ref: JOFA-PEER-2026
  prerequisites:
  - Access to several reports from the same firm.
  - 'For buyers: a way to compare the system description, tests and results for tailoring.'
  risks_and_guardrails:
  - The May 2026 reviewer alert is staff communication not approved by the Peer Review Board and not 'other guidance' (AICPA-REVALERT-2026).
  - Secondary coverage overstates the alert; the JofA text says identical engagements are not performed in accordance with standards in all material respects and are called nonconforming in peer review (JOFA-PEER-2026; CYBERSECIFY-2026 headline).
  - Analysis from a leaked set of reports by an anonymous author is not independent evidence (DEEPDELVER-2026).
  human_checkpoints:
  - Team captain decides whether elevated risk exists and which engagements to select.
  - Reviewer decides whether an engagement is nonconforming.
  role_evolution: Peer reviewers of firms with SOC 2 practices are asked to understand the firm's use of technology, timelines and tailoring; AICPA staff intend to contact team captains early from 1 June 2026 (JOFA-PEER-2026).
  evidence_grade: D
  notes: 'Labelled idea (grade D). The manual comparison is an AICPA peer review procedure and one anonymous text-frequency analysis exists, but no source says AI or software performs the comparison for a named organisation. Peer review data: Oregon''s 2025 report (issued 2026-03-01) shows 0 SOC 1 and 0 SOC 2 engagements reviewed; Louisiana''s 2025 report (issued 2026-03-03) shows SOC Reports 0 reviewed.'
  last_reviewed: '2026-10-16'
  sources:
  - ref: JOFA-PEER-2026
    title: AICPA guides peer reviewers to address SOC 2 risks
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/
    date: '2026-05-14'
    access: full
    locator: Sections 'Responding when elevated risks are identified' and 'A new monitoring and outreach process'
  - ref: JOFA-FAST-2026
    title: Promises of 'fast and easy' threaten SOC credibility
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/
    date: '2026-02-01'
    access: full
    locator: Quote by Terry O'Brien (Schellman) on comparing five reports
  - ref: DEEPDELVER-2026
    title: Delve - Fake Compliance as a Service - Part I (anonymous allegations)
    publisher: DeepDelver (pseudonymous Substack)
    type: community
    url: https://deepdelver.substack.com/p/delve-fake-compliance-as-a-service
    date: '2026-03-19'
    access: full
    locator: Section 5, analysis of leaked reports
  - ref: AICPA-REVALERT-2026
    title: Reviewer Alert, combined editions February 2021 to September 2026 (landing page; content behind free login, not read)
    publisher: AICPA & CIMA Peer Review Program
    type: standard-setter
    url: https://www.aicpa-cima.com/resources/article/reviewer-alert
    date: '2026-09-23'
    access: full
    locator: Disclaimer on the landing page
  - ref: OSCPA-PR-2026
    title: Annual Report on Peer Review Activities for 2025 (Oregon administering entity)
    publisher: Oregon Society of CPAs
    type: professional-body
    url: https://www.orcpa.org/storage/assets/Pages/About/Peer%20Review/Annual%20Report%202025.pdf
    date: '2026-03-01'
    access: full
    locator: Table of engagements reviewed (SOC1 and SOC2 rows)
  - ref: LASCPA-PR-2026
    title: Annual Report on Peer Review Activities, 1 Jan to 31 Dec 2025 (Louisiana administering entity)
    publisher: Society of Louisiana CPAs
    type: professional-body
    url: https://prod.louisiana.cpa/storage/assets/Peer%20Review/AE%20Annual%20Report%20on%20Peer%20Review%20Activities%202025.pdf
    date: '2026-03-03'
    access: full
    locator: Engagement table (SOC Reports row)
  - ref: CYBERSECIFY-2026
    title: AICPA Flags Cookie-Cutter SOC 2 as Nonconforming
    publisher: Cybersecify (penetration-testing vendor)
    type: vendor
    url: https://cybersecify.com/blog/aicpa-nonconforming-soc2-peer-review-2026/
    date: '2026-08-22'
    access: full
    locator: Opening and 'What this does not mean'
- id: assurance-soc-attestation-10
  title: Automated intake and review of received SOC reports by user auditors and third-party-risk teams
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: User auditors and vendor-risk teams must check each SOC report for scope, exclusions, complementary user entity controls (CUECs), exceptions and time gaps. PCAOB inspectors find that auditors often do not test the data and reports they rely on.
  solution: Vendor-risk tools read incoming SOC reports and extract scope, exceptions and control mappings for a reviewer. Vanta's page claims AI-driven vendor risk management and evidence parsing. The sources do not show a named firm using it on SOC reports.
  outcomes:
  - lever: quality
    description: 'Baseline, not an AI result: about 17% of total PCAOB comment forms in each of the 2021 and 2022 inspection cycles contained deficiencies in testing the accuracy and completeness of company-produced information or other data and reports, including information produced by service organisations.'
    figure: about 17% of comment forms (each of 2021 and 2022)
    measures: Share of total PCAOB inspection comment forms for each cycle with deficiencies where the auditor did not perform sufficient procedures to test, or test controls over, accuracy and completeness of IPC or other data and reports. Not specific to SOC reports.
    provenance: independent
    source_ref: PCAOB-DATA-2024
  prerequisites:
  - A reviewer who knows what the report does and does not cover.
  - A record of how CUECs are tested at the user entity.
  risks_and_guardrails:
  - PCAOB staff observed auditors who relied on a service organisation's controls without testing the CUECs the SOC report specified (PCAOB-DATA-2024, p. 9).
  - 'PCAOB staff list questions: did the report cover controls relevant to the information, are there scope exclusions, who tests CUECs, how long since the period covered (PCAOB-DATA-2024, p. 10).'
  - KPMG advises treating receipt of a SOC 2 report as the start of due diligence, checking testing detail, over-reliance on inquiry and 'test of one' approaches (KPMG-CHECKBOX-2026, p. 5).
  human_checkpoints:
  - Reviewer decides reliance and documents CUEC testing and gap-period procedures.
  role_evolution: Vendor-risk analysts move from reading reports to challenging extracted findings. No source reports this change.
  evidence_grade: C
  notes: Grade C because only a vendor describes the AI step. PCAOB figure is a baseline from an adjacent process, so the outcome is not evidence that AI improves the result. The AICPA CPE session on common errors when relying on SOC reports (AAR2503) came up in search results and was not opened.
  last_reviewed: '2026-10-16'
  sources:
  - ref: PCAOB-DATA-2024
    title: 'Spotlight: Inspection Observations Related to Auditor Use of Data and Reports'
    publisher: PCAOB
    type: regulator
    url: https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/data-and-reports-spotlight.pdf
    date: 2024-04
    access: full
    locator: p. 3 (17% figure) and pp. 9-10 (service organisation observations and questions)
  - ref: KPMG-CHECKBOX-2026
    title: 'Beyond the Checkbox: How Confident Are You in Your SOC 2 Reports?'
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/beyond-checkbox.pdf
    date: 2026-07
    access: full
    locator: p. 5, 'A Guide to Evaluating SOC 2 Report Quality'
  - ref: VANTA-VS-2026
    title: Vanta vs. Drata vs. Delve
    publisher: Vanta
    type: vendor
    url: https://vanta.com/resources/vanta-vs-drata-vs-delve
    date: '2026-03-22'
    access: full
    locator: Vendor risk management paragraphs
  - ref: KPMG-BEYOND-2025
    title: 'Beyond compliance: Navigating the critical choice for high-quality SOC audits'
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/kpmg-us/content/dam/kpmg/frv/pdf/2025/beyond-compliance-high-quality-soc-audits.pdf
    date: 2025-12
    access: full
    locator: p. 2, 'Implications of low-quality SOC reports'
- id: assurance-soc-attestation-11
  title: AI drafting of management responses to deviations and exceptions in SOC reports
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: When testing finds deviations, management writes responses for the report. They are time-consuming and affect how users read the report.
  solution: Practitioners use AI to draft management responses. This is the only SOC-specific AI usage poll found and it is carried from the landscape file.
  outcomes:
  - lever: speed
    description: None published beyond the poll in notes.
    figure: none published
    measures: No time or quality figure.
    provenance: self-reported
    source_ref: EY-SOC-2026
  prerequisites:
  - A policy on confidential client data in AI tools.
  risks_and_guardrails:
  - Poll respondents were conference attendees, so the figures do not describe practice generally (EY-SOC-2026, as summarised in the landscape file).
  human_checkpoints:
  - Management reviews responses before they go into the report.
  role_evolution: Not reported.
  evidence_grade: C
  notes: 'Search-only. Poll figures as carried from the landscape file: evidence collection 63%, drafting Section 3 system description 45%, drafting management responses to deviations 41%, project management 29% (multiple answers allowed; respondent count not captured; EY conference, Sep 2026).'
  last_reviewed: '2026-10-16'
  sources:
  - ref: EY-SOC-2026
    title: EY SOC, Attestation and Certification Conference (14th annual) highlights, as summarised in the wave 1 landscape file (page not re-opened by this analyst)
    publisher: EY
    type: conference
    url: research/runs/wave1/landscape-assurance.md (section 9, item S8; EY page URL not given there)
    date: 2026-09
    access: search-only
    locator: 'Live poll results as summarised in the landscape file, section 9 (S8): not re-opened'
- id: assurance-soc-attestation-12
  title: Cross-framework control mapping to reuse SOC 2 evidence for ISO 27001, HIPAA and other frameworks
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types:
  - data-reporting
  - review-assurance
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Service organisations answer to several frameworks and duplicate evidence work for each.
  solution: Platforms map one control set to several frameworks, so one body of evidence supports SOC 2 and other audits, sometimes with the same audit firm. Wispr Flow's re-engagement covers SOC 2, HIPAA and ISO 27001 with one auditor. The CSA also describes SOC 2+ reports that add further criteria to a SOC 2 examination.
  outcomes:
  - lever: growth
    description: Vanta says it supports 35+ frameworks with cross-mapping. The figure counts frameworks supported, not time saved.
    figure: 35+ frameworks
    measures: Number of frameworks the vendor says it supports (comparison page).
    provenance: vendor-published
    source_ref: VANTA-VS-2026
  prerequisites:
  - Each framework's own scope and criteria are confirmed with each auditor.
  - Evidence meets the strictest framework's requirements.
  risks_and_guardrails:
  - A SOC 2 report covers selected criteria over a defined system; it is not a certificate for another framework (JOFA-POD-2026).
  - ISO 42001 is described as a separate certification engagement; a SOC 2 or SOC 2+ report does not provide the certificate (SOC2AUDITORS-AI-2026).
  human_checkpoints:
  - Auditor for each framework decides what evidence it accepts.
  role_evolution: Not reported.
  evidence_grade: C
  notes: 'Pattern is cross-framework control mapping, which fits none of the listed patterns. Grade C: vendor-published count; the named customer is a plan, not a result.'
  last_reviewed: '2026-10-16'
  sources:
  - ref: VANTA-VS-2026
    title: Vanta vs. Drata vs. Delve
    publisher: Vanta
    type: vendor
    url: https://vanta.com/resources/vanta-vs-drata-vs-delve
    date: '2026-03-22'
    access: full
    locator: '''Framework coverage'' paragraph'
  - ref: WISPR-2026
    title: Our path to a new, independent audit
    publisher: Wispr Flow (customer company blog)
    type: firm
    url: https://wisprflow.ai/post/new-independent-audit
    date: '2026-03-27'
    access: full
    locator: Paragraphs 3-4
  - ref: CSA-SOC2-2026
    title: 'The SOC 2 AI Gap: Auditors Improvise Where AICPA Has Not Acted'
    publisher: Cloud Security Alliance AI Safety Initiative
    type: professional-body
    url: https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/
    date: '2026-08-30'
    access: full
    locator: Strategic considerations; SOC 2+ precedent from January 2023
  - ref: JOFA-POD-2026
    title: The risks of quick-turn SOC engagements and what CPAs should know (podcast with Amy Pawlicki, AICPA)
    publisher: Journal of Accountancy (AICPA)
    type: podcast
    url: https://www.journalofaccountancy.com/podcast/2026/apr/the-risks-of-quick%E2%80%91turn-soc-engagements-and-what-cpas-should-know/
    date: '2026-04-30'
    access: full
    locator: Pawlicki on scope of trust services criteria
  - ref: SOC2AUDITORS-AI-2026
    title: 'SOC 2 for AI Companies (2026): Scope, Controls & AICPA Guidance'
    publisher: SOC2Auditors.org (comparison site)
    type: press
    url: https://soc2auditors.org/insights/soc-2-for-ai-companies/
    date: '2026-10-13'
    access: full
    locator: Table on SOC 2, SOC 2+ and ISO 42001
```

---

## 3. Module notes

### Processes and key steps (work types)

- **Scoping and acceptance:** choose SOC 1, SOC 2 (any of five trust services categories), SOC 3, or ISAE 3402; agree the system boundary and period; assess independence and competence. `expert-judgment`. A SOC 2 engagement can cover one to five categories and varies in complexity (JOFA-POD-2026).
- **Readiness and system description:** gap assessment, policies, risk assessment, description of the system. `document-production`, `review-assurance`. Platforms now supply templates (LINFORD-FAQ-2022).
- **Design evaluation (Type 1) and operating-effectiveness testing (Type 2):** the service auditor evaluates the description, then tests controls over the period. `review-assurance`, `data-reporting`. ISAE 3402 requires procedures in combination with enquiry, and prior-period evidence does not reduce testing (XRB-3402-2026, paras 24-25).
- **Subservice organisations:** carve-out or inclusive method, adequately described in the system description (XRB-3402-2026, para 9 definitions and para 21(d)). An AICPA panel noted that SOC 2 criterion CC9.2 gives a way to report inadequate vendor-management processes, while SOC 1 has no equivalent criterion, so it is harder to report such a gap in a SOC 1 (AICPA-VIDEO-2023).
- **Deviations and exceptions:** evaluate, report, and obtain management's responses. `expert-judgment`, `document-production`.
- **Subsequent events and report issuance:** the service auditor enquires about events up to the report date and has no obligation after it (XRB-3402-2026, paras 43-44). `document-production`.
- **Bridge (gap-period) letters:** the term does not appear in the sources opened. The underlying issue does: PCAOB staff ask how much time has passed since the period covered and whether controls changed in the gap (PCAOB-DATA-2024, p. 10).
- **Oversight and quality:** state licensure, peer review (system review, engagement selection, enhanced oversight), AICPA monitoring. `review-assurance` (JOFA-PEER-2026, JOFA-POD-2026).
- **User-side reliance:** user auditors and vendor-risk teams evaluate scope, exclusions, CUECs, exceptions and gap period (PCAOB-DATA-2024, pp. 9-10; KPMG-CHECKBOX-2026, p. 5).

### Common pain points

- Tool vendors marketing SOC 2 with promises of compliance in weeks or hours, and slogans stressing speed. They now dominate online search results for SOC 2 services, per the working group chair (JOFA-FAST-2026).
- Fee pressure on mid-market firms to match speed and volume (JOFA-FAST-2026).
- Customers buying a report to satisfy a contract and getting something partners can reject as cookie-cutter (JOFA-FAST-2026).
- Under-tuned tools: management expects the tool to do more than it can, and does not remediate gaps (LINFORD-FAQ-2022).
- SOC 2 reports are read by buyers as a pass/fail credential, while they attest to scoped controls over a period (IANS-DELVE-2026; CSA-SOC2-2026).
- User auditors sometimes do not test CUECs or the accuracy and completeness of service-organisation data (PCAOB-DATA-2024, p. 9).
- SOC 2 has no AI-specific criteria, so auditors request different AI evidence from firm to firm, per a Cloud Security Alliance note (CSA-SOC2-2026). That claim cites a comparison site and one-firm examples and is secondary.

### Metrics and benchmarks

- 17% (approximately) of total PCAOB inspection comment forms in each of 2021 and 2022 contained deficiencies in testing accuracy and completeness of company-produced information or other data and reports, including service-organisation information. Not SOC-specific (PCAOB-DATA-2024, p. 3). Independent.
- Peer review at administering-entity level: Oregon's 2025 report (issued 1 Mar 2026) lists 0 SOC 1 and 0 SOC 2 engagements reviewed; Louisiana's (issued 3 Mar 2026) lists 0 SOC reports reviewed. Their overall nonconforming rates are not SOC rates (OSCPA-PR-2026; LASCPA-PR-2026).
- Allegation-based, anonymous, unverified: in a leaked set of 575 files (81 not SOC 2), the author reports one test string in 493 of 494 SOC 2 reports and an identical auditor-conclusion sentence in 259 of 259 Type II reports (DEEPDELVER-2026, section 5; repeated in IANS-DELVE-2026).
- Standards timing: ASB exposure drafts of 26 Feb and 25 Mar 2026, comments due 30 Jun 2026, effective for engagements beginning on or after 15 Jun 2029 if finalised (JOFA-ATTEST-2026; CPAPA-ASB-2026).
- Timelines cited by a customer re-doing its audit: about eight weeks expected for a re-verified SOC 2, stated as a plan (WISPR-2026). A vendor guide puts a Type II observation period at three months or more (SOC2AUDITORS-DELVE-2026, secondary).
- No SOC qualification rate, deviation rate, overturned-report rate or independent AI accuracy measure was found.

### Guardrails and regulatory points

- **Who may perform SOC:** the AICPA says state law (the Uniform Accountancy Act definition of attest) requires attest engagements, including SOC, to be performed by licensed CPAs; licensed CPAs outside peer review or unlicensed signatories may violate state law (JOFA-POD-2026).
- **Standards:** SOC 1 under AT-C 320 and SOC 2 under AT-C 205 (AICPA-TQA9561-2026); ISAE 3402 is used with ISAE 3000 (Revised), which was effective for reports dated on or after 15 Dec 2015 and amended ISAE 3402 (IAASB-3000-2013, IAASB-3402-2009).
- **Ethics, tool providers:** the Code applies in full; independence modifications for SSAE engagements are in ET 1.297; threats named are undue influence and self-interest. Examples: concentrated cross-referrals, vendor rights to observe, vendor deadlines, bundled fees, non-disparagement clauses, paying the vendor to access evidence, vendor-inserted material around the report, guaranteed outcomes. Where threats are significant and safeguards cannot reduce them, performing or continuing the examination is not appropriate (JOFA-SOCETH-2026). The AICPA's full staff paper is gated (AICPA-ESISOC-2026).
- **Fee-setting and referral fees:** the examination fee must be set by the service auditor, and payments to or from a tool provider may be referral fees needing written disclosure (JOFA-SOCETH-2026, citing ET 1.230.030 and 1.520.001).
- **Earlier AICPA signals:** a Dec 2022 AICPA alert said tool misuse can lead to nonconforming examinations and that some tool-provider sites listed providers that did not appear to be licensed CPA firms; the SOC 2 guide was updated in Oct 2022 (GT-SOC2-2023). An AICPA FAQ on software tools in SOC 2 examinations was dated 30 Jun 2021 per practitioners and shows 31 Mar 2026 on the AICPA page (LINFORD-FAQ-2022; AICPA-FAQ-2026). Whether the content changed in 2026 was not confirmed because the PDF is gated.
- **Peer review:** the reviewer alert says a single file is often insufficient, directs reviewers to understand the firm's use of technology, platform relationships, timelines and tailoring, and warns of deficiencies or follow-up action such as revising the system of quality management or outside review of completed engagements (JOFA-PEER-2026). The combined Reviewer Alert page states that its contents are not approved by the Peer Review Board and are not "other guidance" (AICPA-REVALERT-2026).
- **TQA 9561 (11 Sep 2026):** covers the effect of a service organisation's AI use on SOC 1 (AT-C 320) and SOC 2 (AT-C 205), split into SOC 1 only, SOC 2 only and both (DART-TQA-2026; AICPA-TQA9561-2026). A comparison site describes TQAs as nonauthoritative and relays a CPA firm's reading that a third-party AI provider inside the system is analysed like any subservice organisation; that reading could not be verified against the gated text (SOC2AUDITORS-AI-2026).
- **Experts:** IAASB narrow-scope amendments to ISAE 3000 on using an external expert take effect 15 Dec 2026, adopted in the UK on that date; respondents supported making the competence and objectivity prohibition explicit (FRC-620-2026). The sources do not say whether SOC examiners' use of vendor staff falls under these amendments.
- **Other jurisdictions:** New Zealand gazetted ISAE (NZ) 3402 on 9 Apr 2026, effective 7 May 2026. Whether this is a new adoption or a revision was not determined (XRB-3402-2026).
- **Vendor self-governance statements** (vendor-published, not verified): Drata says it has never bundled audits and separates software, auditor selection and audit judgment (DRATA-INTEGRITY-2026). Delve said on 3 Apr 2026 it would rebuild its auditor network, remove firms that fell short, halt automation that interacts with audit workflows and open direct customer-auditor channels (DELVE-RECORD-2026).

### Frontier signals (dated)

- 2026-02-01: AICPA is exploring a "SOC Quality Center" that could act as a quality badge for participating firms; the working group chair warns that tool vendors may seek the larger audit market next (JOFA-FAST-2026).
- 2026-02-26 and 2026-03-25: ASB exposure drafts revising the baseline attestation standards (AT-C 105, 205, 210), with conforming amendments including AT-C 320; effective 2029-06-15 if finalised (JOFA-ATTEST-2026).
- 2025-07-22: Delve announced a $32M Series A led by Insight Partners at a $300M valuation, which shows the capital behind bundled SOC-as-a-service (TC-DELVE-2026 for the amount and valuation; SYKES-DELVE-2026 for the date, a secondary timeline).
- 2026-03-19 to 2026-04-03: allegation, denial, apology and customer migration in the Delve case (DEEPDELVER-2026, TC-DELVE-2026, DELVE-RECORD-2026, WISPR-2026).
- 2026-04-13 and 2026-05-14: AICPA ethics staff paper, then the peer review alert; 2026-06-01: planned structured monitoring of peer reviews of firms with SOC 2 practices (JOFA-PEER-2026).
- 2026-08-30: a Cloud Security Alliance note argues the AICPA has not acted on AI-specific criteria and that auditors improvise evidence requests; it misdates one AICPA document (see cautions) (CSA-SOC2-2026).
- 2026-09-11: TQA 9561 published. 2026-09-22: KPMG webcast describes expected restructuring of the Trust Services Criteria, criteria designed specifically for SOC 2 and SOC 3, and new or enhanced AI considerations; no AICPA effective date is announced (KPMG-SOC-2026, SOC2AUDITORS-AI-2026).
- 2025-10-23 and 2026-03-05: CSA STAR for AI launched and CSA guidance for CPAs performing STAR for AI attestation (SOC 2+ based) released (CSA-STAR-2025, CSA-CPAGUIDE-2026). Routed (see section 4).
- 2026-12-15: ISAE 3000 narrow-scope amendments effective (FRC-620-2026).

### Workforce and role effects

- Service auditors are told to resist pressure to cut hours, set internal benchmarks that define a thorough examination and explain value to clients (JOFA-FAST-2026).
- Peer reviewers take on deeper reviews for firms with SOC 2 practices: multi-engagement comparison, understanding of platforms and timelines (JOFA-PEER-2026).
- Evidence collection moves into platforms; auditors are told to treat tool data as a starting point and spend time on control execution and management oversight (KPMG-CHECKBOX-2026, pp. 3-4).
- New-entrant competition: individual CPAs and new firms offering SOC reports at high discounts, per KPMG (KPMG-BEYOND-2025, p. 1). KPMG is an established competitor, so treat the framing with care.
- No headcount or staffing data for SOC practices was found.

### Objections and concerns practitioners raise

- "Fast and easy may come at the expense of quality and objectivity" (SOC 2 Working Group chair, JOFA-FAST-2026).
- Tool vendors that are not CPA firms cannot attest, and some cultivate networks of small or overseas firms that can sign high volumes (JOFA-FAST-2026).
- A SOC 2 report is not a certification and cannot imply every engagement is the same (JOFA-POD-2026).
- Tools show control existence and configuration, not effectiveness in the client's environment; templated risk assessments miss specific risks (KPMG-CHECKBOX-2026; LINFORD-FAQ-2022).
- The vendor view: tools make SOC 2 more accessible and efficient, and templates are not evidence (JOFA-FAST-2026; TC-DELVE-2026).
- The AICPA stresses that most SOC reports are done properly and most firms use technology appropriately (JOFA-POD-2026).
- Interest check: the practitioners quoted are from established SOC practices, KPMG and Linford sell SOC services, and several vendor and comparison sites compete with one another (VANTA-VS-2026, SOC2AUDITORS-DELVE-2026, CYBERSECIFY-2026). Weight their statements accordingly.
- A report answers a narrower question than buyers assume, especially for AI vendors (CSA-SOC2-2026).

### Interview probes for an advisor

1. "Take your last ten SOC 2 engagements. For each, who set the sample sizes, the risk assessment and the test procedures, you or the platform default? If a peer reviewer compared five of them, what would they see?"
2. "When is the system description, the test procedure text and the opinion first drafted, and by whom, relative to period end and to evidence arrival?"
3. "Which relationships do you have with tool providers (referrals, bundled fees, contract terms on scope, timing, evidence access or disparagement), and what threat evaluation have you documented?"
4. "How do you confirm a platform's integrations cover the whole system boundary, that syncs did not break, and that exported data was not altered?"
5. "On the user side, how do you check complementary user entity controls, exclusions and the gap period before relying on a SOC report, and how often do you reject one?"

### Cautions on sources and corrections to the landscape file

- **CSA research note (30 Aug 2026)** dates the AICPA forensic and valuation AI guidelines to "early 2026"; the AICPA page shows 1 Oct 2025 (AICPA-FVSAI-2025). The note also says the alert directed reviewers to apply added scrutiny from 1 Jun 2026; the JofA text says AICPA staff intend to start outreach to team captains from 1 Jun (JOFA-PEER-2026). Treat the CSA note as a lead.
- **Cybersecify (22 Aug 2026)** headlines that the Peer Review Board "now treats" identical reports as failing standards. The JofA text says such engagements are judged nonconforming after reviewers examine them, and the alert is staff communication (JOFA-PEER-2026, AICPA-REVALERT-2026).
- **Landscape item P14** reads the CSA note as reporting a Peer Review Board alert in May 2026; confirmed against JofA. The landscape's TQA 9561 summary (no new criteria, scope follows system boundary) is secondary and was not verified here either.
- **SSAE numbering:** the CPA Practice Advisor article labels SSAE numbers inconsistently with the JofA article; this note cites AT-C sections, which both articles name (CPAPA-ASB-2026, JOFA-ATTEST-2026).
- **Court details** on the Delve case come from a comparison site and were not checked against dockets (SOC2AUDITORS-DELVE-2026).
- **Dates:** AICPA-SOC-2026 is an undated landing page whose latest listed item is dated 14 May 2026; its year-only date is a placeholder. KPMG-BEYOND-2025 and KPMG-CHECKBOX-2026 dates come from PDF metadata (Dec 2025 and Jul 2026), not a printed date.

---

## 4. Routed to other modules

- **assurance / assurance over AI systems (other-assurance split):** TQA 9561 scoping of AI in SOC 1 and SOC 2, KPMG's expected Trust Services Criteria changes, CSA STAR for AI and STAR for AI attestation guidance for CPAs, ISO/IEC 42001 as a separate certification engagement, and Baker Tilly's guidance on embedding AI controls in the five categories (AICPA-TQA9561-2026, DART-TQA-2026, KPMG-SOC-2026, CSA-STAR-2025, CSA-CPAGUIDE-2026, BAKERTILLY-AISOC2-2025, SOC2AUDITORS-AI-2026, CSA-SOC2-2026). These change what is examined rather than how the examiner works, so they are not entered as use cases here.
- **assurance / controls-testing:** the mechanics of automated evidence tests and continuous control monitoring overlap with use cases 01 and 02; leave the control-test detail there.
- **assurance / acceptance-independence:** the AICPA's tool-provider reasoning (undue influence and self-interest threats, bundled fees, referral concentration, responsible-party test) may transfer to firms licensing AI audit tools; the article itself says it may apply to other attest work (JOFA-SOCETH-2026). Also the alternative-practice-structure thread in the landscape.
- **assurance / quality-management:** the peer review alert's use of firm-level quality management as the remedy (JOFA-PEER-2026) and the AICPA's monitoring of SOC peer reviews.
- **assurance / sustainability-assurance:** the ASB's proposed AT-C 325 and 330 for sustainability information, in the same exposure drafts as the baseline changes (JOFA-ATTEST-2026, CPAPA-ASB-2026).
- **Any third-party-risk or vendor-risk module (outside this archetype):** consumption of SOC reports by vendor-risk teams, questionnaire automation, trust centres (use cases 07, 08, 10 sit on the boundary).

---

## 5. Sources

Access: `full` = opened and read (for gated AICPA documents, only the landing page); `search-only` = not opened by this analyst. Dates are ISO; see section 3 for placeholders.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| JOFA-FAST-2026 | Promises of 'fast and easy' threaten SOC credibility | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/ | 2026-02-01 | full |
| JOFA-SOCETH-2026 | SOC engagements: Ethics risks with tool providers | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/ | 2026-04-06 | full |
| JOFA-PEER-2026 | AICPA guides peer reviewers to address SOC 2 risks | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/ | 2026-05-14 | full |
| JOFA-POD-2026 | The risks of quick-turn SOC engagements and what CPAs should know (podcast with Amy Pawlicki, AICPA) | Journal of Accountancy (AICPA) | podcast | https://www.journalofaccountancy.com/podcast/2026/apr/the-risks-of-quick%E2%80%91turn-soc-engagements-and-what-cpas-should-know/ | 2026-04-30 | full |
| JOFA-ATTEST-2026 | Proposed attestation changes: What CPAs should know | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/apr/proposed-attestation-changes-what-cpas-should-know/ | 2026-04-24 | full |
| CPAPA-ASB-2026 | AICPA Seeks Public Comment on Proposed Updates to Attestation Standards | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/02/27/aicpa-seeks-public-comment-on-proposed-updates-to-attestation-standards/177561/ | 2026-02-27 | full |
| AICPA-ESISOC-2026 | Ethics Staff Insights: Business arrangements with SOC tool providers (landing page; PDF behind free login, not read) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/article/esi-soc | 2026-04-13 | full |
| AICPA-FAQ-2026 | FAQs: Effect of the use of software tools on SOC 2 examinations (landing page; PDF behind free login, not read) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/article/faqs-effect-of-the-use-of-software-tools-on-soc-2-r-examinations | 2026-03-31 | full |
| AICPA-TQA9561-2026 | TQA Section 9561 SOC Examinations: Effect of the Service Organization's Use of AI on SOC 1 and SOC 2 Examinations (landing page; full text behind free login, not read) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/download/tqa-section-9561-soc-examinations-effect-of-the-service-organizations-use-of-ai-on-soc1-and-soc2-examinations | 2026-09-11 | full |
| DART-TQA-2026 | AICPA Releases TQAs on a Service Organization's Use of AI | Deloitte DART | firm | https://dart.deloitte.com/USDART/home/news/all-news/2026/sep/aicpa-releases-tqas-service-organization-use-ai | 2026-09-21 | full |
| AICPA-SOC-2026 | System and Organization Controls: SOC Suite of Services (landing page with notice on allegations about a compliance vendor) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services | 2026 | full |
| AICPA-REVALERT-2026 | Reviewer Alert, combined editions February 2021 to September 2026 (landing page; content behind free login, not read) | AICPA & CIMA Peer Review Program | standard-setter | https://www.aicpa-cima.com/resources/article/reviewer-alert | 2026-09-23 | full |
| AICPA-FVSAI-2025 | Guidelines for Responsible Use of Artificial Intelligence (AI) in Forensic and Valuation Services Engagements (landing page) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/download/guidelines-for-responsible-use-of-artificial-intelligence-ai-in-forensic-and | 2025-10-01 | full |
| AICPA-TSC-2023 | 2017 Trust Services Criteria (With Revised Points of Focus, 2022) (landing page) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022 | 2023-09-30 | full |
| AICPA-VIDEO-2023 | Maintaining high standards for SOC engagements | AICPA & CIMA Insights Blog | professional-body | https://www.aicpa-cima.com/professional-insights/video/maintaining-high-standards-for-soc-engagements | 2023-12-06 | full |
| CSA-SOC2-2026 | The SOC 2 AI Gap: Auditors Improvise Where AICPA Has Not Acted | Cloud Security Alliance AI Safety Initiative | professional-body | https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/ | 2026-08-30 | full |
| CSA-STAR-2025 | Cloud Security Alliance Launches STAR for AI | Cloud Security Alliance | professional-body | https://cloudsecurityalliance.org/press-releases/2025/10/23/cloud-security-alliance-launches-star-for-ai-establishing-the-global-framework-for-responsible-and-auditable-artificial-intelligence | 2025-10-23 | full |
| CSA-CPAGUIDE-2026 | Guidelines for CPAs Providing CSA STAR or STAR for AI Attestation Program (landing page) | Cloud Security Alliance | professional-body | https://cloudsecurityalliance.org/artifacts/guidelines-for-cpas-providing-csa-star-or-star-for-ai-attestation-program | 2026-03-05 | full |
| BAKERTILLY-AISOC2-2025 | Representing AI controls in your SOC 2 report (Evolving SOC 2 reports for AI controls) | Baker Tilly | firm | https://www.bakertilly.com/insights/ai-controls-for-soc-2-reports | 2025-12-18 | full |
| KPMG-BEYOND-2025 | Beyond compliance: Navigating the critical choice for high-quality SOC audits | KPMG US | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/frv/pdf/2025/beyond-compliance-high-quality-soc-audits.pdf | 2025-12 | full |
| KPMG-CHECKBOX-2026 | Beyond the Checkbox: How Confident Are You in Your SOC 2 Reports? | KPMG US | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/beyond-checkbox.pdf | 2026-07 | full |
| KPMG-SOC-2026 | The future of SOC reporting: Mastering AI risks and the changing Trust Services Criteria (webcast page) | KPMG US | firm | https://kpmg.com/us/en/webcasts/2026/soc-reporting-ai-risks-trust-services-criteria.html | 2026-09-22 | full |
| PCAOB-DATA-2024 | Spotlight: Inspection Observations Related to Auditor Use of Data and Reports | PCAOB | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/data-and-reports-spotlight.pdf | 2024-04 | full |
| AAA-CIIA-2023 | Call for Papers from Current Issues in Auditing: System and Organization Controls (SOC) Services | American Accounting Association, Auditing Section | academic | https://aaahq.org/portals/0/documents/segments/aud/2023/CIIA%20CFP%20SOC%20Services.pdf | 2023 | full |
| OSCPA-PR-2026 | Annual Report on Peer Review Activities for 2025 (Oregon administering entity) | Oregon Society of CPAs | professional-body | https://www.orcpa.org/storage/assets/Pages/About/Peer%20Review/Annual%20Report%202025.pdf | 2026-03-01 | full |
| LASCPA-PR-2026 | Annual Report on Peer Review Activities, 1 Jan to 31 Dec 2025 (Louisiana administering entity) | Society of Louisiana CPAs | professional-body | https://prod.louisiana.cpa/storage/assets/Peer%20Review/AE%20Annual%20Report%20on%20Peer%20Review%20Activities%202025.pdf | 2026-03-03 | full |
| TC-DELVE-2026 | Delve accused of misleading customers with 'fake compliance' | TechCrunch | press | https://techcrunch.com/2026/03/21/delve-accused-of-misleading-customers-with-fake-compliance/ | 2026-03-22 | full |
| DEEPDELVER-2026 | Delve - Fake Compliance as a Service - Part I (anonymous allegations) | DeepDelver (pseudonymous Substack) | community | https://deepdelver.substack.com/p/delve-fake-compliance-as-a-service | 2026-03-19 | full |
| DELVE-RESPONSE-2026 | Response to Misleading Claims | Delve | vendor | https://delve.co/blog/response-to-misleading-claims | 2026-03-20 | full |
| DELVE-CHANGES-2026 | Delve Announces Changes and New Customer Support Measures | Delve | vendor | https://delve.co/blog/delve-announces-changes-and-new-customer-support-measures | 2026-03-24 | full |
| DELVE-RECORD-2026 | Delve sets the record straight on anonymous attacks (apology and changes) | Delve | vendor | https://delve.co/blog/delve-sets-the-record-straight-on-anonymous-attacks | 2026-04-03 | full |
| IANS-DELVE-2026 | Delve Allegations Expose Weak Points in Modern Compliance | IANS Research | vendor | https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/03/30/delve-allegations-expose-weak-points-in-modern-compliance | 2026-03-24 | full |
| SYKES-DELVE-2026 | The Delve Scandal: Compliance as a Grift | Brian Sykes (Substack) | community | https://bsykes.substack.com/p/the-delve-scandal-compliance-as-a | 2026-03-26 | full |
| WISPR-2026 | Our path to a new, independent audit | Wispr Flow (customer company blog) | firm | https://wisprflow.ai/post/new-independent-audit | 2026-03-27 | full |
| SOC2AUDITORS-DELVE-2026 | Delve Review (2026): Who Actually Audits You? | SOC2Auditors.org (comparison site) | press | https://soc2auditors.org/insights/delve-review/ | 2026-10-13 | full |
| SOC2AUDITORS-AI-2026 | SOC 2 for AI Companies (2026): Scope, Controls & AICPA Guidance | SOC2Auditors.org (comparison site) | press | https://soc2auditors.org/insights/soc-2-for-ai-companies/ | 2026-10-13 | full |
| DRATA-INTEGRITY-2026 | SOC 2 Audit Integrity: Why Independence Matters | Drata | vendor | https://drata.com/blog/soc-2-audit-integrity | 2026-01-09 | full |
| VANTA-VS-2026 | Vanta vs. Drata vs. Delve | Vanta | vendor | https://vanta.com/resources/vanta-vs-drata-vs-delve | 2026-03-22 | full |
| CYBERSECIFY-2026 | AICPA Flags Cookie-Cutter SOC 2 as Nonconforming | Cybersecify (penetration-testing vendor) | vendor | https://cybersecify.com/blog/aicpa-nonconforming-soc2-peer-review-2026/ | 2026-08-22 | full |
| LINFORD-FAQ-2022 | AICPA FAQs on SOC 2 Automation Tools: Insights from an Auditor | Linford & Co | firm | https://linfordco.com/blog/soc-2-automation-tools-aicpa-faqs | 2022-06-15 | full |
| LINFORD-TOOLS-2021 | SOC 2 Software Tools: How They Affect the SOC Audit Process | Linford & Co | firm | https://linfordco.com/blog/using-soc-2-software-tools-for-audit-compliance | 2021-12-22 | full |
| GT-SOC2-2023 | What businesses need to know about SOC 2 developments | Grant Thornton US | firm | https://www.grantthornton.com/insights/articles/advisory/2023/what-businesses-need-to-know-about-soc-2-developments | 2023-02-16 | full |
| IAASB-3000-2013 | ISAE 3000 (Revised), Assurance Engagements Other than Audits or Reviews of Historical Financial Information (publication page) | IAASB | standard-setter | https://www.iaasb.org/publications/international-standard-assurance-engagements-isae-3000-revised-assurance-engagements-other-audits-or | 2013-12-09 | full |
| IAASB-3402-2009 | Staff Overview, ISAE 3402, Assurance Reports on Controls at a Service Organization (publication page) | IAASB | standard-setter | https://www.iaasb.org/publications/staff-overview-international-standard-assurance-engagements-isae-3402-assurance-reports-controls | 2009-11-30 | full |
| XRB-3402-2026 | International Standard on Assurance Engagements (New Zealand) 3402, Assurance Reports on Controls at a Service Organisation (XRB 2026/44) | NZ Auditing and Assurance Standards Board / External Reporting Board | standard-setter | https://www.xrb.govt.nz/dmsdocument/5983/ | 2026-04-09 | full |
| FRC-620-2026 | Feedback Statement: ISA (UK) 620 and ISAE (UK) 3000 (HTML version, machine-converted by the FRC) | Financial Reporting Council | regulator | https://www.frc.org.uk/docs/9935/html/ | 2026 | full |
| EY-SOC-2026 | EY SOC, Attestation and Certification Conference (14th annual) highlights, as summarised in the wave 1 landscape file (page not re-opened by this analyst) | EY | conference | research/runs/wave1/landscape-assurance.md (section 9, item S8; EY page URL not given there) | 2026-09 | search-only |

**Counts by type:** conference 1; regulator 2; standard-setter 10; professional-body 10; firm 9; vendor 7; academic 1; survey 0; press 4; podcast 1; community 2; job-posting 0. Total 47 sources, of which 46 opened and 1 search-only.


---

## 6. Gaps

- **No independent measure of SOC quality.** No qualification rate, deviation rate, rejected-report rate, or AI accuracy measure was found. National AICPA peer review results for SOC engagements were not found; two state administering-entity reports show zero SOC engagements reviewed (OSCPA-PR-2026, LASCPA-PR-2026).
- **No academic empirical study on SOC reliance or quality was found.** The AAA call for papers (2023) says little is known (AAA-CIIA-2023). The resulting papers, if any, were not located. SSRN, Accounting Horizons, JIS and *Current Issues in Auditing* were not searched because the web-search quota ran out. The journal site returned 403.
- **No survey of SOC users or practitioners was opened.** The only usage poll (EY conference, Sep 2026) is carried from the landscape file and not re-opened. Benchmark studies by SOC firms (for example CBIZ's SOC benchmark) returned 403.
- **Gated AICPA documents were not read:** TQA 9561, Ethics Staff Insights on SOC tool providers, the software-tools FAQ, the Reviewer Alert and the Trust Services Criteria. Only landing pages and secondary descriptions were used. Schneider Downs' summary of TQA 9561 returned 403 and is known only through a comparison site.
- **Searches not run (quota exhausted):** Delve developments from April to October 2026 beyond secondary summaries; state board of accountancy actions on SOC signatories (one search found none); other platform controversies; non-US regulators and bodies on ISAE 3402 (ICAEW AAF 01/20, Dutch and Danish bodies); whether the IAASB has an ISAE 3402 project; evidence on bridge letters; SOC 3, SOC for Cybersecurity and SOC for Supply Chain quality.
- **Court dockets** for the Delve case could not be checked (CourtListener rate-limited the request); details rest on a comparison site (SOC2AUDITORS-DELVE-2026).
- **Delve allegations are unresolved.** The anonymous author, Delve and one named firm disagree; no regulator finding was found. Do not treat any allegation figure as established.
- **ISAE 3402 international text** was not opened; the New Zealand adoption was used for paragraph references. Differences from the IAASB text were not checked.
- **AI-specific SOC practice by CPA firms:** no firm-published case of an AI tool used in SOC testing, with or without measurement, was found. AI claims are vendor-published.
- **Access routes:** the Drata blog (403 to direct requests) and the PCAOB staff publications list were fetched through a text mirror, as the brief allows; only the Drata page is cited as a source. The FRC feedback statement page says it was machine-converted from PDF and not human verified.
- **Source types not found:** no job postings, and no community discussion beyond two Substack posts (Reddit and LinkedIn were not used).

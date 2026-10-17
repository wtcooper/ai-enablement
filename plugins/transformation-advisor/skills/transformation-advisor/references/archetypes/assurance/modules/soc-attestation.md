# SOC and attestation (assurance)

Last reviewed 2026-10-17. Use cases live in `../use-cases/soc-attestation.yaml` (16 entries). `#05` means
`assurance-soc-attestation-05`; other modules' ids are in full. The controls-testing module already holds AI-assisted
SOC testing (`assurance-controls-testing-11`), SOC-cycle drafting of Section 3 and deviation responses (`assurance-controls-testing-12`),
reading vendor SOC reports (`assurance-controls-testing-13`), platforms feeding examiners (`assurance-controls-testing-14`) and
evidence-fabrication screening (`assurance-controls-testing-23`); use those ids here instead of looking for duplicates. Source keys in brackets are in the YAML or in §10.
Almost every figure is self-reported or vendor-published. No independent measure of AI quality in SOC work was found.
Everything about Delve is allegation: Delve denies it, and no regulator finding exists. Say both whenever it comes up.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

The SOC and attestation service end to end: SOC 1 (controls relevant to customers' financial reporting, AICPA
AT-C 320), SOC 2 (controls against the AICPA Trust Services Criteria, or TSC, AT-C 205), SOC 3, and the
international ISAE 3402 / ISAE 3000 equivalents. A Type 1 report covers design at a point in time; a Type 2 report
tests operation over a period. The module runs from scoping and readiness through the service organisation's system
description ("Section 3"), testing, deviations and reporting to how customers use the report. It also covers the
compliance-automation platforms (Vanta, Drata and others) that now sit between service organisations and auditors,
and the 2026 quality concerns about commoditised SOC 2. In the 2026 sources the debate is mostly about quality and
independence; AI as a productivity tool comes second.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Scoping and acceptance | Choose SOC 1/2/3 or ISAE 3402, Trust Services categories (one to five), system boundary, Type 1 or 2, period; subservice organisations (outside providers) carved out or included; independence check | expert-judgment, coordination-scheduling | Platform referrals can set fee and timeline [JOFA-SOCETH-2026]; whether the client's AI is in scope is a new question [SD-TQA] |
| Readiness and remediation | Gap assessment, policies, risk assessment, fixing failing tests | review-assurance, software-systems, document-production | Templated policies and risk questions miss industry risks [LINFORD-FAQ-2022] |
| System description and assertion | Management writes Section 3 and asserts it is fair | document-production | Two companies should never share a Section 3; identical text signals a template [CHIARO-VIBE-2026, KPMG-CHECKBOX-2026] |
| Planning | Risk assessment, test plan, sample sizes | expert-judgment | Identical risk assessments and sample sizes across clients are flagged by peer review [JOFA-PRB] |
| Walkthroughs and test of design | Meetings with control owners; flowcharts; design conclusion | research-synthesis, review-assurance | Many meetings and follow-ups (`assurance-controls-testing-01`, `assurance-controls-testing-11`) |
| Evidence requests and collection | Requests, platform integrations, screenshots, exports | coordination-scheduling, data-reporting | Screenshots and Excel files; stale integrations; wrong populations [SCRUT-EVIDENCE-2026] |
| Operating-effectiveness testing | Inquiry, observation, inspection, reperformance, sampling (test detail sits in controls-testing) | review-assurance | 90% of exceptions on manual controls, 39% on system access (KPMG UK, 180+ reports) [K-UKCA]; over-reliance on inquiry and "test of one" [KPMG-CHECKBOX-2026] |
| Deviations and management responses | Evaluate, root-cause, respond, judge effect on opinion | expert-judgment, document-production | Logical access behind 52% of SOC 1 and 40% of SOC 2 deviations (EY, 2,000+ reports) [EY-SOC-2025] |
| Reporting and issuance | Opinion, Sections 3 and 4, report review, partner sign-off; subsequent events up to the report date | document-production, review-assurance | Long reports hide details [LINFORD-ASSURE-2026]; KPMG UK: 15% of reports qualified in 2024-25 (20% in 2023-24) [K-UKCA] |
| Bridge (gap-period) letters | Cover the gap after the period the report tested | client-interaction | No AI evidence found; PCAOB staff ask how long since the period and what changed [PCAOB-DATA-2024] |
| After issuance | Security questionnaires, trust centre, annual renewal | client-interaction | Questionnaires keep coming; trust pages can overstate [IANS-DELVE] |
| Use of the report | Customers and their auditors check scope, exclusions, CUECs (controls the customer must run), deviations, gap period | research-synthesis, review-assurance | ~17% of PCAOB comment forms (2021, 2022) found weak testing of data and reports, incl. service-organisation information [PCAOB-DATA-2024] |
| Firm quality and peer review | Licensure, peer review, AICPA monitoring | review-assurance | Two 2025 state peer review reports show 0 SOC engagements reviewed [OSCPA-PR-2026, LASCPA-PR-2026] |

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path),
delegate (an agent owns a multi-step outcome), reinvent (the service or business model changes). Evidence is
platform-heavy: half the entries sit on the service-organisation side (`function: risk-compliance-legal`).

**Scoping, acceptance and planning (service auditor)**
- Improve: `#01` Linford uses AI for client acceptance, sampling and scheduling concurrent audits; it says this makes
  audits more thorough, not faster. `assurance-controls-testing-02`: KPMG UK agents score control wording and draft test plans.

**Readiness (service organisation)**
- Improve: `#02` platforms draft policies, risk assessments and system descriptions (Vanta, Comp AI); a person
  approves each. `#03` AI-generated remediation snippets with expert approval (Vanta, Secureframe, Oneleet).
  `#04` cross-framework mapping and evidence reuse (A-LIGN: ~15 hours saved per extra framework, vendor figure).
  `assurance-controls-testing-12`: general AI for updating Section 3 (45% of EY poll attendees) and deviation responses (41%).
- Automate: `#05` continuous control monitoring with agent-collected evidence (Vanta, Drata; named users Snyk,
  WorkJam, Wispr Flow). Only vendor figures: 82% less time per audit (IDC via Vanta), 4 hours a week.

**Walkthroughs, evidence and testing (service auditor)**
- Improve: `assurance-controls-testing-11` and `assurance-controls-testing-01`, KPMG UK: ~18% less testing time on recent controls assurance engagements with
  Clara AI, Copilot and DataSnipper, the only firm-published measure. `#06` A-LIGN screens evidence against audit
  intent before fieldwork (Teleperformance: 30-40% less evidence time, vendor-published). `#07` Weaver's engagement
  platform and client portal (process change, little AI yet): realization up 10-12% in year one.
- Automate: `assurance-controls-testing-14`, the examiner pulls evidence from the client's platform (contested; see §6).
- Delegate: `#08` Fieldguide's four agents (planner, auditor, reviewer, orchestrator) run a SOC engagement;
  announced, demo scheduled 13 Oct 2026; vendor figures (55% fewer hours, 4x capacity) are undefined.
- Idea: `assurance-controls-testing-23`, screening evidence for AI fabrication; an ISACA Now author reports an AI-fabricated document [ISACA-EVIDENCE-2026].

**Reporting**
- Improve: `#09` Linford reviews draft reports with AI to catch details on late pages; it says it saves no time.

**After issuance and report use**
- Improve: `#10` questionnaire answers drafted from the issued report and approved answers (Vanta: 95% of
  suggestions accepted, vendor). `assurance-controls-testing-13`: AI reads received SOC reports for scope, deviations and CUECs. `#12`
  flagging templated reports by uniform language (Whistic, announced); AI in peer review comparison is an idea.
- Automate: `#11` trust centre with an AI chatbot answering buyers (Vanta); claims must not exceed the report.

**Service and operating model (reinvent)**
- `#13` platforms as the front door: curated auditor networks and audit hubs (Vanta: 100+ audit firms, 26,000+
  audits; Drata says it has never bundled audits).
- `#14` bundled "SOC-as-a-service": platform, referred CPA firm, fixed fee and timeline. The AICPA says some
  vendors "automate the service entirely". Delve is the named case: allegations, denied.
- `#15` platform and licensed CPA firm sold as one "auditor-led" service (Thoropass; A-LIGN).
- `#16` AI-native CPA firm (Chiaro) publishes its method, tests complete populations by default and bundles
  readiness; one Type I issued, no Type II.

**Coverage.** Ladder: assist 4, augment 7, automate 3, delegate 2. Scope: step 9, process 3, model 4. Delegate rests
on one announced product (`#08`) and one new firm's self-description (`#16`); no measured delegate deployment exists.
No AI evidence was found for bridge letters, SOC 3, or ISAE 3402 practice outside KPMG UK.

## 4. Interview probes

1. **SOC practice: "Where do new SOC clients come from: direct, a platform referral or a bundled package? Who sets scope, fee and
   report date?"** Reveals independence exposure: ethics staff list referral concentration, vendor deadlines,
   bundled fees, non-disparagement and paid evidence access as threats (`#13`, `#14`).
2. **"Take five recent SOC 2 engagements. Who set the risk assessment, sample sizes and test procedures: you or the
   platform defaults? What would a peer reviewer comparing them see?"** Reveals template risk; identical
   engagements can be judged nonconforming.
3. **"When are the system description, test-procedure text and opinion first drafted, and by whom, relative to
   period end and evidence arrival?"** Reveals the pattern at the centre of the Delve allegations and AICPA warnings.
4. **"How do you test what a compliance platform collects? What share do you re-perform at the source system, and
   how do you catch broken syncs, wrong populations or edited exports?"** Reveals reliance on tool data (`assurance-controls-testing-14`, `#05`).
5. **"Where do you use AI today (readiness, walkthroughs, evidence extraction, testing, report review, acceptance,
   scheduling)? What is the review standard, and what do you measure?"** Reveals maturity against KPMG UK's ~18%
   and whether any quality evidence (deviations found, rework, overrides) exists. Most have hours at best.
6. **"Where do you draw the line on AI-drafted text: Section 3, deviation responses, test conclusions? Who owns
   each?"** Reveals whether the management/auditor boundary holds (management owns its responses).
7. **"At small-company population sizes, do you still sample? What would testing every item change in your
   method, documentation and peer review?"** Reveals readiness for `#16`'s model and its caveat on incomplete populations.
8. **"When a client builds an LLM into its product or uses foundation-model providers, what changes in scoping,
   description and carve-out analysis under TQA 9561?"** Reveals AI-as-test-object readiness (`assurance-controls-testing-15`) and scope inflation.
9. **"What client evidence goes into AI tools, under what terms, and do clients know?"** Reveals confidentiality
   exposure; no standard requires disclosing AI use [CHIARO-WHO-2026].
10. **"How have fees, realization and staff mix changed since platforms and AI arrived? How do you show a buyer
    your report is tailored?"** Reveals business-model pressure (`#07`, `#14`, `#15`).
11. **Report users: "Since March 2026, what changed in how you read vendors' SOC reports (signing firm, CUECs,
    exclusions, gap period)? How often do you reject one?"** Reveals buyer due diligence (`assurance-controls-testing-13`, `#12`).
12. **Service organisations: "How do you know your platform's integrations cover the whole system boundary and the
    right populations, such as service accounts?"** Reveals false-green risk in `#05`.

## 5. Metrics and benchmarks

**Firm-published (self-reported; no baseline or engagement count)**
- KPMG UK: ~18% less testing time on recent controls assurance engagements; ~15% for one team using DataSnipper
  (`assurance-controls-testing-11`) [K-UKCA]. The tools are bundled, so AI alone cannot be credited.
- KPMG UK benchmark of 180+ reports (2024-25): 90% of operating-effectiveness exceptions on manual controls; 39%
  on system access and authorisation; qualified reports 15% (20% the year before) [K-UKCA].
- EY review of 2,000+ SOC reports: logical access behind 52% of SOC 1 and 40% of SOC 2 deviations [EY-SOC-2025].
- Schellman says it issues more than 2,000 SOC reports a year [SCHELLMAN-2026].

**Usage poll (EY SOC conference, Sep 2026; attendees, multiple answers, n not stated)**: evidence collection 63%,
updating Section 3 45%, drafting deviation responses 41%, project management 29% [EY-SOC].

**Vendor claims (grade C unless a named customer is attached; ask for measured cases)**
- Vanta: 82% less time per audit (Vanta cites IDC; study not shown); AI agent saves 4 hours a week on average; WorkJam
  ~1 hour a week instead of 7-8 (`#05`); questionnaire answers 95% accepted (`#10`).
- A-LIGN: ~15 hours saved per extra framework (`#04`); Teleperformance 30-40% less evidence time, 25% less prep (`#06`).
- Fieldguide: 55% fewer engagement hours, 90% less testing time, 4x capacity; firm and baseline not named (`#08`).
- Weaver: realization up 10-12% in year one on an engagement platform, published by the vendor (`#07`).

**Market and price (asking prices, not paid fees)**
- Directory fee bands for SOC 2 Type 2, mostly the site's own estimates: specialist CPA firms $15,500-$50,000;
  full-service $30,000-$80,000; Big Four $65,000-$200,000 [SOC2AUD-COST-2026]. Median ballpark quote $9,000 for companies of
  1-50 staff; $9,500 for AI companies (middle half $7,000-$13,500); fastest listed fieldwork-to-report: 1 week (`#14`).
- Vanta ~$300M ARR in April 2026, up ~69% (Sacra estimate); 16,000+ customers (Fortune, from Vanta) (`#05`).
- A-LIGN benchmark (1,000+ respondents): 60% would switch auditors to improve the quality of the final report
  (figure read from an image) [ALIGN-BENCH-2026].

**Quality and oversight**: no SOC error, override, rework or parallel-run figure for AI exists. Peer review outcomes
for SOC practices are not published; two state reports show 0 SOC engagements reviewed in 2025. The AAA said in
2023 that little is known about how auditors perform or rely on SOC services [AAA-CIIA-2023].

**What to measure (recommend these, not hours alone)**: hours per engagement before and after; share of
tool-reported results re-performed at source; deviations found per engagement against prior years; review notes and
rework; issues caught in report review; time from period end to report; how alike the firm's reports are (the peer
review test); customer rejections or re-examinations; questionnaire answers spot-checked against controls.

## 6. Guardrails

**Standards and the profession (no body prohibits AI; none has AI-specific SOC criteria)**
- **TQA 9561 (11 Sep 2026; an AICPA technical Q&A, text behind a login).** AI creates no separate SOC model
  and no new criteria; relevance depends on whether AI is used in the services delivered or only internally. A SOC 1
  description must disclose AI's nature where it is part of the services and relevant to customers' financial
  reporting. Third-party AI providers go through the subservice analysis. Schneider Downs adds that an auditor
  using AI stays responsible and warns against scope inflation [SD-TQA, DART-TQA-2026, AICPA-TQA9561-2026].
- **Criteria.** SOC 2 still uses the 2017 TSC with 2022 points of focus; no AI-specific criteria as of Oct 2026
  [AICPA-TSC-2023, CSA-SOC2, SOC2AUD-AICOS-2026]. A KPMG webcast page (22 Sep 2026) expects a restructuring with AI considerations; no
  effective date is announced [KPMG-SOC-2026].
- **Software tools FAQ (AICPA; first issued 30 Jun 2021, page dated 31 Mar 2026).** Per Linford's summaries:
  consider tool coverage, reliability and consistency; do not rely on the tool alone; validate a sample of its
  results [LINFORD-TOOLS-2021, LINFORD-FAQ-2022, AICPA-FAQ-2026].
- **Ethics staff on tool providers (6 and 13 Apr 2026).** Terms that shift control, judgement, fees or evidence
  access to the provider can create independence threats. The auditor sets the fee; disclose referral fees; avoid guaranteed
  outcomes. If significant threats cannot be reduced by safeguards, performing the examination is not appropriate
  [JOFA-SOCETH-2026, AICPA-ESISOC-2026].
- **Peer review alert (May 2026).** Identical reports, risk assessments, sample sizes and procedures can be judged
  nonconforming. A single file is often not enough; reviewers may compare about five engagements from different
  partners; outreach from 1 Jun 2026. Staff communication, not Board-approved guidance [JOFA-PRB, AICPA-REVALERT-2026].
- **State law.** SOC is attest work for licensed CPAs; unlicensed signatories, or CPAs outside peer review, who sign
  fraudulent reports violate state law. A SOC 2 report is not a "certification" [JOFA-PODSOC].
- **Liability.** A CPA can be liable for a third party's false claims made on its behalf if it endorses them by act
  or omission [JOFA-FAST].
- **ISAE 3402.** Enquiry must be combined with other procedures; subsequent-events duty ends at the report date
  (New Zealand adoption, paras 25 and 43-44) [XRB-3402-2026]. ISAE 3000 expert amendments apply from 15 Dec 2026 [FRC-620-2026].
- **Coming.** ASB exposure drafts revising AT-C 105, 205 and 210 (Feb and Mar 2026) address baseline concepts and
  sustainability (the JofA summary does not mention AI); effective 15 Jun 2029 if finalised [JOFA-ATTEST-2026].
- **Confidentiality.** Client evidence entered into generative AI tools may be shared with the tool's owners; the
  AICPA Code's guidance on outside service providers applies [CHIARO-WHO-2026].
- **Model behaviour.** EY: AI may invent details even when told not to; agents may change behaviour to work around
  anomalies [EY-SOC].

**Design guardrails seen in practice**: validate tool data at the source for higher-risk controls; keep a record of
who drafted what and when; calibration examples for AI judgement calls (`#16`); an expert approves every AI fix
(`#03`); a person approves every AI-drafted policy (`#02`); customers can switch AI features off (`#06`); trust pages
claim nothing the report does not support (`#11`).

**Steps that stay with a person**: scope and system boundary; acceptance, independence and fee setting; risk
assessment, sample sizes and tests tailored to the client; evidence sufficiency; deviation evaluation and effect on
the opinion; the opinion and signature. Management (not the auditor or vendor) owns the description, assertion and
responses to deviations. Customers decide reliance and test CUECs.

## 7. Roles and how they evolve

- **Service-organisation compliance staff** keep scoping and exception decisions as tools automate retrieval
  [SCRUT-EVIDENCE-2026]; "GRC Engineer" appears as a VantaCon speaker title [VANTACON-2026] (`#05`).
- **Service auditors** spend less time collecting evidence and more on control execution and management oversight
  [KPMG-CHECKBOX-2026]. SOC leaders urge them to resist cutting hours and to set internal benchmarks for a
  thorough examination [JOFA-FAST]. The AICPA says SOC examiners need deep security and privacy expertise [JOFA-PODSOC].
- **Warning signs** named by a specialist firm: testing offshored to unqualified staff, no walkthroughs, no partner
  review of the report [LINFORD-ASSURE-2026].
- **Peer reviewers** of firms with SOC 2 practices dig deeper and, when risk is elevated, compare engagements [JOFA-PRB].
- **Vendor-risk teams** treat a report as the start of due diligence and vet the signing CPA [KPMG-CHECKBOX-2026, WHISTIC-DELVE-2026].
- **New roles, so far at vendors only**: Fieldguide's audit methodology lead and director of audit transformation for
  an "agentic operating model"; Drata's audit-firm alliances manager. No audit-firm job posting showing AI use in SOC
  work was found [FIELDGUIDE-JOBS-2026, DRATA-JOBS-2026].
- **Skills**: AI literacy and digital forensics [ISACA-EVIDENCE-2026]; EY notes firms hiring chief data strategy officers [EY-SOC].

## 8. Frontier

- **2025-11-19** Vanta launches its "Agentic Trust Platform" and AI Agent 2.0 [VANTA-HNS-2025].
- **2026-01** KPMG UK introduces a reasonable-assurance "SOC 2+" opinion over AI governance (assurance-over-AI module) [K-UKCA].
- **2026-02-01** AICPA SOC 2 Working Group chair warns that "fast and easy" may cost quality; a SOC Quality Center
  badge is being explored [JOFA-FAST].
- **2026-02-26 / 03-25** ASB attestation exposure drafts (effective 2029-06-15 if finalised) [JOFA-ATTEST-2026].
- **2026-03-19 to 04-23** Delve: anonymous allegations, denied; Delve apologises and says it will rebuild its
  auditor network (3 Apr); Y Combinator parts ways; named customers move [DEEPDELVER-2026, DELVE-RECORD-2026, TC-DELVEYC-2026, TC-CONTEXT-2026].
- **2026-03-20** Vanta launches compliance, third-party-risk and customer-trust agents [VERDICT-VANTA-2026].
- **2026-04-06 to 06-01** AICPA ethics guidance, podcast, Peer Review alert and reviewer outreach [JOFA-SOCETH-2026, JOFA-PODSOC, JOFA-PRB].
- **2026-08-04** Drata releases AI Agent Governance in limited availability; Chiaro publishes its SOC 2 method
  [DRATA-AGENTGOV-2026, HN-CHIARO-2026].
- **2026-08-30** CSA note: auditors improvise AI evidence requests without AI criteria [CSA-SOC2].
- **2026-09-11** TQA 9561 on AI in SOC 1 and SOC 2 [AICPA-TQA9561-2026, SD-TQA].
- **2026-09-17** Comp AI raises a $34M Series A [TC-COMPAI-2026].
- **2026-09-22** KPMG expects a TSC restructuring with AI considerations [KPMG-SOC-2026].
- **2026-09-23** Linford: AI made compliance cheaper, not assurance [LINFORD-ASSURE-2026].
- **2026-10-13** Fieldguide scheduled a live demonstration of agents running a SOC 2 engagement [FIELDGUIDE-WEBINAR-2026].
- **2026-11-10 to 11-12** VantaCon, billed as "the AI governance event" (scheduled) [VANTACON-2026].
- **2026-12-15** ISAE 3000 expert amendments take effect [FRC-620-2026]. Watch: AICPA inquiry outcome, TSC changes,
  SOC Quality Center, first national peer review data on SOC practices.

## 9. Common objections

- **"AI makes SOC 2 cheap now."** A SOC firm says AI made compliance cheaper but not assurance (`#09`); the Working
  Group reports intense fee pressure. Directory medians of ~$9,000 are asking prices, not proof of adequate work.
- **"The platform already tested everything."** Tools confirm configuration exists, not effectiveness; dashboards do
  not show the right population was used; the auditor must validate a sample of tool results (`#05`).
- **"Templates are just efficient."** Peer review can judge identical engagements nonconforming; a Working Group
  member said some firms' reports differ only by logo [JOFA-FAST, JOFA-PRB].
- **"Referral partners are just a sales channel."** Ethics staff name referral concentration, vendor deadlines and
  bundled fees as threats; document the evaluation (`#13`, `#14`).
- **"AI will save hours on every engagement."** KPMG UK reports ~18% from a tool bundle; Linford says AI saves it no
  time but makes it more thorough. Nobody has published a quality measure. Measure your own.
- **"TQA 9561 means every report needs an AI section."** No: AI matters only where it is in the services or affects
  in-scope controls; scope inflation is the wrong reaction [SD-TQA].
- **"Testing every item means certainty."** Chiaro's own caveat: a flawless census of an incomplete population
  proves nothing; reasonable assurance still applies (`#16`).
- **"Delve proves the platforms are fraudulent."** The claims are unproven allegations, denied, from an anonymous
  author. The AICPA says most service organisations hire credible firms and most firms use technology appropriately [JOFA-PODSOC].
- **"No regulator will act."** A compliance podcast says regulators are unlikely to step in, so buyers must reassess
  due diligence [CPN-WEEDS-2026]. AICPA staff planned peer review outreach from 1 Jun 2026, and state law applies to signatories.

## 10. Sources

Full details (title, publisher, type, URL, date, access) are in the YAML.
- **In the YAML, professional bodies and standard-setters:** JOFA-FAST, JOFA-PRB, JOFA-PODSOC, JOFA-SOCETH-2026, AICPA-SOC-2026, AICPA-REVALERT-2026, CSA-SOC2, XRB-3402-2026, OSCPA-PR-2026, LASCPA-PR-2026.
- **In the YAML, firms and conferences:** EY-SOC, KPMG-CHECKBOX-2026, BAKERTILLY-TRUST-2026, LINFORD-ASSURE-2026, LINFORD-FAQ-2022, LINFORD-TOOLS-2021, GT-SOC2-2023, ALIGN-ASCEND-2026, ALIGN-BENCH-2026, WISPR-2026, CHIARO-METHOD-2026, CHIARO-BUNDLE-2026, CHIARO-AINATIVE-2026, CHIARO-WHO-2026, VANTACON-2026.
- **In the YAML, vendors:** VANTA-AUDIT-2026, VANTA-AI-2026, VANTA-AUDITORS-2026, VANTA-VS-2026, DRATA-AGENTGOV-2026, DRATA-INTEGRITY-2026, DRATA-JOBS-2026, FIELDGUIDE-SOC-2026, FIELDGUIDE-WEBINAR-2026, FIELDGUIDE-JOBS-2026, FIELDGUIDE-WEAVER-2026, THOROPASS-2026, COMPAI-2026, SECUREFRAME-2026, ONELEET-2026, SCRUT-EVIDENCE-2026, WHISTIC-DELVE-2026, CYBERSECIFY-2026, SOC2AUD-FIRMS-2026, SOC2AUD-AICOS-2026, SOC2AUD-DELVE-2026.
- **In the YAML, press and community:** VANTA-HNS-2025, VERDICT-VANTA-2026, FORTUNE-VANTA-2026, SACRA-VANTA-2026, TC-DELVE-2026, TC-WHISTLE2-2026, TC-DELVEYC-2026, TC-LITELLM-2026, TC-CONTEXT-2026, TC-COMPAI-2026, IANS-DELVE, DEEPDELVER-2026 (anonymous, unverified), DELVE-RESPONSE-2026, DELVE-CHANGES-2026, DELVE-RECORD-2026, HN-CHIARO-2026.
- **Not in the YAML (all opened and checked on 2026-10-17 unless noted):**
  - K-UKCA (KPMG UK, *Reimagining Controls Assurance with AI*, 2026-01, https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf); in controls-testing YAML.
  - EY-SOC-2025 (EY, *13th annual EY SOC Reporting Conference highlights*, 2025-08, https://www.ey.com/content/dam/ey-unified-site/ey-com/en-ch/insights/technology-risk/documents/ey-13th-annual-soc-reporting-conference-highlights.pdf).
  - SD-TQA (Schneider Downs, *AI in SOC Examinations: TQA Section 9561*, 2026-09-30, https://schneiderdowns.com/our-thoughts-on/ai-in-soc-examinations-what-the-aicpas-new-tqa-section-9561-means-for-service-organizations/); in controls-testing YAML.
  - AICPA-TQA9561-2026 (AICPA, TQA 9561, 2026-09-11, landing page only, https://www.aicpa-cima.com/resources/download/tqa-section-9561-soc-examinations-effect-of-the-service-organizations-use-of-ai-on-soc1-and-soc2-examinations).
  - DART-TQA-2026 (Deloitte DART, 2026-09-21, https://dart.deloitte.com/USDART/home/news/all-news/2026/sep/aicpa-releases-tqas-service-organization-use-ai).
  - AICPA-FAQ-2026 (AICPA, software-tools FAQ, 2026-03-31, landing page only, https://www.aicpa-cima.com/resources/article/faqs-effect-of-the-use-of-software-tools-on-soc-2-r-examinations).
  - AICPA-ESISOC-2026 (AICPA, Ethics Staff Insights on SOC tool providers, 2026-04-13, landing page only, https://www.aicpa-cima.com/resources/article/esi-soc).
  - AICPA-TSC-2023 (AICPA, 2017 TSC with 2022 points of focus, 2023-09-30, https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022).
  - KPMG-SOC-2026 (KPMG US webcast page, 2026-09-22, https://kpmg.com/us/en/webcasts/2026/soc-reporting-ai-risks-trust-services-criteria.html).
  - JOFA-ATTEST-2026 (JofA, *Proposed attestation changes*, 2026-04-24, https://www.journalofaccountancy.com/issues/2026/apr/proposed-attestation-changes-what-cpas-should-know/).
  - FRC-620-2026 (FRC, feedback statement ISA (UK) 620 and ISAE (UK) 3000, 2026, https://www.frc.org.uk/docs/9935/html/).
  - PCAOB-DATA-2024 (PCAOB, *Spotlight: auditor use of data and reports*, 2024-04, https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/data-and-reports-spotlight.pdf).
  - AAA-CIIA-2023 (AAA, call for papers on SOC services, 2023, https://aaahq.org/portals/0/documents/segments/aud/2023/CIIA%20CFP%20SOC%20Services.pdf).
  - ISACA-EVIDENCE-2026 (ISACA Now, *The Audit Evidence Crisis*, 2026-06-08, https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2026/the-audit-evidence-crisis-how-ai-deepfakes-are-rewriting-assurance-standards).
  - CHIARO-VIBE-2026 (Chiaro, *What is vibe compliance?*, 2026-05-02, https://chiarohq.com/soc-2/vibe-compliance).
  - SOC2AUD-COST-2026 (SOC2Auditors.org lead-generation directory, 2026-10-05, https://soc2auditors.org/soc-2-audit-cost/).
  - SCHELLMAN-2026 (Schellman blog index, accessed 2026-10, https://www.schellman.com/blog).
  - CPN-WEEDS-2026 (Compliance Podcast Network, show notes only, 2026-04-01, https://compliancepodcastnetwork.net/compliance-into-the-weeds-ai-driven-soc-audits-and-the-growing-trust-gap/).

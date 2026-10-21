# Advisory guardrails

Last researched 2026-10-21. Use this in Frame (constraints), in Reimagine fit checks and for the risks in Make the case.
It covers what applies across advisory lines; each module's §6 has the line-specific detail. Firm-wide duties
(engagement letters, quality review, billing ethics, insurance) are in
[professional-services guardrails](../professional-services/guardrails.md). Source keys in brackets resolve in
[sources.md](sources.md). This is a briefing, not legal advice: confirm rules against primary text per engagement.

## Contents

1. [Principles](#1-principles)
2. [Who sets or enforces what](#2-who-sets-or-enforces-what)
3. [Independence: the firm's own audit clients](#3-independence-the-firms-own-audit-clients)
4. [Fees: contingent, outcome-linked and AI-shortened work](#4-fees-contingent-outcome-linked-and-ai-shortened-work)
5. [Client data and confidentiality](#5-client-data-and-confidentiality)
6. [Standards and frameworks by line](#6-standards-and-frameworks-by-line)
7. [Courts, evidence and disclosure of AI use](#7-courts-evidence-and-disclosure-of-ai-use)
8. [Steps that need human judgment](#8-steps-that-need-human-judgment)
9. [Checks before a plan goes ahead](#9-checks-before-a-plan-goes-ahead)

## 1. Principles

- **Existing duties apply now.** The research found no standard or regulator AI guidance written for CAS, transaction
  advisory or family offices; codes and standards apply to AI as they stand (module §6 in each). A JofA article by the
  AICPA Professional Ethics Division says competence and due care are unchanged and the member owns the final work
  product [JOFA-ETHAI-2026].
- **The limit follows the client, not the service line.** The same service can be sold freely to one client and be
  restricted for a client the firm or an affiliate audits [SEC-RULE2-01-2026].
- **No AI-specific independence ruling was found.** The same article says existing nonattest and information-systems
  rules apply and members should use the conceptual framework where the Code is silent [JOFA-ETHAI-2026].
- **A person signs.** Valuers, experts, testers and CFO-level advisers stay responsible for conclusions, whatever
  tools are used [ISA-AO41-2026; KTS-EXPERTAI-2026].
- **Quality bars are not numeric.** No body sets an error-rate threshold for AI in this work; firms have to define
  their own review and evidence standard (risk-controls module §6).

## 2. Who sets or enforces what

| Body | Reach in advisory | Key examples |
|---|---|---|
| SEC; PCAOB | Independence for issuer audit clients; examination of registered advisers | [SEC-RULE2-01-2026; PCAOB-RULES3520-2026; SEC-EXAMPRI-FY2026] |
| AICPA (ethics committee, FVS section, practice aids) | Code of Professional Conduct, nonattest services, consulting standard, AI guidance | [JOFA-ETHAI-2026; JOFA-NONATTEST-2016; BVR-AICPAAIGUIDE-2025; JOFA-CS100-2024] |
| IESBA | International Code: non-assurance services, data custody, PE workstream | [IESBA-TECHREV-2023; IESBA-PE-2026] |
| COSO; IIA | Control frameworks and internal-audit standards used in risk-controls work | [COSO-GENAI-2026; IIA-AIFW-2024; BAKERTILLY-GAM-2026] |
| IVSC; Appraisal Foundation; AICPA, ASA, RICS | Valuation standards, USPAP, the proposed performance framework | [IVSC-IVSED-2026; ISA-AO41-2026; ACCTODAY-VPF-2026] |
| Federal courts and rules committees | Expert reliability, machine-generated evidence, sanctions | [USCOURTS-EVID-2026; USCOURTS-STDCOMM-2026; KTS-EXPERTAI-2026] |
| IRS OPR | Circular 230 where advisory work touches tax matters | [IRS-OPR-2026] |
| FTC | Safeguards Rule for firms that complete income tax returns | [FTC-SAFEGUARDS-2026] |
| SBA; lenders | Lender QoE requirements on SBA 7(a) acquisitions | [SBA-SOP5010-2026] |
| FINRA; SEC examinations | Member firms and registered investment advisers, for wealth affiliates | [FINRA-ROR-2026; SEC-EXAMPRI-FY2026] |

## 3. Independence: the firm's own audit clients

**SEC Rule 2-01 (issuer audit clients).** Paragraph (c)(4) lists ten non-audit services that impair independence:
bookkeeping and accounting records; financial information systems design and implementation; appraisal, valuation and
fairness opinions; actuarial services; internal audit outsourcing; management functions; human resources;
broker-dealer, investment adviser or investment banking services; legal services; and expert services for advocacy.
The first five ((i)-(v)) carry an exception when it is reasonable to conclude the results will not be subject to audit
procedures; the other five, including management functions, carry none. Paragraph (c)(5) bars contingent fees on any service to the audit client
[SEC-RULE2-01-2026]. SEC staff apply a rebuttable presumption that a prohibited service will be subject to audit
procedures; materiality does not overcome it, and a prohibited service in a prior period cannot be cured
[PWC-SECFAQ-2019].

| Module | Services the SEC list restricts for issuer audit clients |
|---|---|
| client-accounting-services | Bookkeeping, financial statements and source data, financial-system design ((c)(4)(i), (ii)) |
| risk-controls | Internal-audit outsourcing on accounting controls, systems or statements; ongoing monitoring as a management function ((v), (vi)) |
| valuation | Appraisal, valuation, fairness opinions ((iii)) |
| forensic-disputes | Expert services advocating the client's interests in litigation or regulatory proceedings; factual accounts are carved out ((x)) |
| transactions | Investment-banking-type services; any contingent fee ((viii), (c)(5)) |
| fpa-performance | Management functions; financial information systems design and implementation ((vi), (ii)) |
| private-client | Investment-adviser services ((viii)); PCAOB Rule 3523 on tax services to people in financial reporting oversight roles |

Mapping from the independence research [SEC-RULE2-01-2026; PCAOB-RULES3520-2026]. Which specific diligence, FP&A or
platform scopes cross these lines was not analysed in the sources; confirm per engagement
(assurance-acceptance-independence-15).

**AICPA Code (private-company attest clients).** Nonattest services are permitted when threats are at an acceptable
level and the client takes management responsibility, oversees the service through a suitably skilled person,
evaluates the results and accepts responsibility, with the understanding documented beforehand. This is a 2016
description; the current Code text was not opened in the sources [JOFA-NONATTEST-2016]. Module-by-module AICPA
treatment of valuation, internal audit and forensic services for private attest clients is therefore not stated.

**IESBA Code.** Bookkeeping for a non-public-interest audit client only if routine or mechanical; automated services
are judged by what the technology does. Hosting or storing an audit client's data, or being the only access to its
system, counts as assuming a management responsibility [IESBA-TECHREV-2023].

**AI-specific points.** Developing or hosting an AI system for an attest client can raise independence concerns
[JOFA-ETHAI-2026]. The closest SEC staff analogy is firm-built software: a tax module that generates accrual and
disclosure information counts as financial information system design [PWC-SECFAQ-2019]. Whether a firm-built agent
that drafts entries or variance explanations for an audit client falls under that reasoning is unaddressed. A firm that
runs a client's books inside a firm-hosted AI environment faces a data-custody question as well as a confidentiality
one; this is a reading of the cited paragraphs, not an authoritative interpretation.

**Structures.** In one alternative practice structure described in 2016, the attest firm (Mayer Hoffman McCann) must
consider the advisory firm's (CBIZ) services as if it had provided them [JOFA-NONATTEST-2016]; Crowe notes some services may not be available to attest clients
[CROWE-KKR-2026]. The AICPA rule on these structures is still moving [JOFA-PEEC-2026].

**Operating practice.** Independence is checked in systems, not left to teams: one firm's billing system would not
assign a client number until the engagement was entered in the independence system, and RSM's independence director
called private-equity affiliates the most significant monitoring challenge (2016) [JOFA-NONATTEST-2016].

## 4. Fees: contingent, outcome-linked and AI-shortened work

- **Contingent fees.** Barred for any service to an SEC issuer audit client, including by affiliates (Rule 2-01(c)(5);
  PCAOB Rule 3521) [SEC-RULE2-01-2026; PCAOB-RULES3520-2026]. The AICPA Code proscribes them where the firm performs an
  audit or review, certain compilations or an examination of prospective financial information, and for preparing an
  original or amended tax return or refund claim; fees fixed by courts
  are not contingent, and a range based on effort rather than result is not a contingent fee (2015 description)
  [NYSSCPA-CONTFEE-2015].
- **Outcome pricing collides here.** Outcome-linked advisory fees are promoted with the caveat that audit firms cannot
  take contingent fees tied to financial results [BBTAX-SH-2026]. Write down which clients are eligible first.
- **AI-shortened work in tax matters.** The IRS OPR says billing for time not actually spent, or double billing for
  AI-assisted tasks, may violate Circular 230 section 10.27 depending on the facts, and savings should be passed on
  openly [IRS-OPR-2026]. It covers matters before the IRS; the tax archetype has the detail and the debate.
- **A sister profession.** A secondary summary of ABA Formal Opinion 512 says lawyers billing hourly may charge only for
  time actually spent [EZEL-ABA512-2024]. A signal of how ethics bodies treat the question, not a rule for CPAs.

## 5. Client data and confidentiality

- **The Code's question first.** Before client data goes into any AI system: is it confidential client information,
  is consent required, and has the client specifically consented? Some public tools use inputs for training
  [JOFA-ETHAI-2026]. IESBA expects protection across collection, use, transfer, storage and destruction, and names
  training and product development as uses that need authorization [IESBA-TECHREV-2023].
- **Statutes.** The FTC Safeguards Rule treats a firm that completes income tax returns as a financial institution:
  oversee service providers by contract and periodic assessment, and notify the FTC of certain breaches. It protects
  individual consumers' information, not business-client data as such [FTC-SAFEGUARDS-2026]. Section 7216 consent
  governs tax return information (tax archetype) [TREAS-7216-2008]. The IRS OPR says client data goes only into secure,
  enterprise-approved AI [IRS-OPR-2026].
- **Vendor terms are a start, not an answer.** Anthropic and Microsoft state that commercial and enterprise products do
  not train on customer data by default [ANTHROPIC-PRIVACY-2026; MS-COPILOTPRIV-2026]. That does not settle consent,
  service-provider oversight or unapproved use: 34% of professionals in one survey use AI their organisation has not
  approved [TR-FOPREPORT-2026].
- **Line-specific limits.** Deal NDAs: an AI provider may not count as a permitted representative, and parties now negotiate
  clauses that bar uploads to public AI platforms or require prior written consent [KJK-NDA-2026]. Litigation: keep privileged and protective-order material out of open
  tools [KTS-EXPERTAI-2026]. Family offices: keep family, legal, tax, estate and security information out of tools the
  policy does not cover [NT-FOAIPOLICY-2026].
- **Controls practitioners propose.** An agent inventory with a named owner, replayable evidence, risk-scaled sign-off,
  close reading of third-party assurance, and monitoring with an exit threshold [CPAPA-AGENTSCLOSE-2026]; data
  classification, least-privilege access for agents and human approval for higher-risk actions [JOFA-CHECKLIST-2026].
- **Disclosure.** As of April 2025 no specific federal law or professional standard required CPAs to disclose AI use
  to clients, though some state laws (California, Utah) require some disclosure [JOFA-DISCLOSE-2025]; in tax matters
  the IRS OPR says practitioners should disclose AI activities [IRS-OPR-2026]. Clients ask anyway
  ([state-of-ai.md](state-of-ai.md) §3).

## 6. Standards and frameworks by line

| Line | What applies | Status | Source |
|---|---|---|---|
| CAS | AICPA Code; SQMS No. 1 for compilation and review work from 15 Dec 2025; COSO for clients' close agents | In force; guidance | [JOFA-ETHAI-2026; LINFORD-SQMS-2024; COSO-GENAI-2026] |
| Risk and controls | COSO generative-AI guidance; IIA AI Auditing Framework and Topical Requirements; FRC guidance as a model; AICPA TQA 9561 on SOC and AI | Guidance; standards in force by date | [COSO-GENAI-2026; IIA-AIFW-2024; BAKERTILLY-GAM-2026; FRC-GENAI-2026; DART-TQA9561-2026] |
| Transactions | AICPA consulting standard CS 100 (competence, due care, planning, sufficient data); SBA lender rules | In force | [JOFA-CS100-2024; SBA-SOP5010-2026] |
| Valuation | IVS exposure draft on AI disclosure and IVS 107; USPAP AO-41; AICPA FVS guidelines; proposed Valuation Performance Framework | Draft; adopted; members-only; draft | [IVSC-IVSED-2026; ISA-AO41-2026; BVR-AICPAAIGUIDE-2025; ACCTODAY-VPF-2026] |
| Forensic | Rule 702 case law; Rule 707 on machine-generated evidence; AICPA FVS guidelines; UK Civil Justice Council work on expert evidence | Case law; published draft withdrawn, revised draft under study; guidance; consultation | [KTS-EXPERTAI-2026; USCOURTS-EVID-2026; CJC-AIDOCS-2026] |
| FP&A | COSO for insight generation in controls; SEC limits on systems design and management functions | Guidance; in force | [COSO-GENAI-2026; SEC-RULE2-01-2026] |
| Private client | IRS OPR; FINRA oversight report; SEC examination priorities for adviser affiliates | Guidance; priorities | [IRS-OPR-2026; FINRA-ROR-2026; SEC-EXAMPRI-FY2026] |

The EU AI Act amendment moves stand-alone high-risk duties to 2 Dec 2027 [CUATRECASAS-AIOMNIBUS-2026]; it feeds
client AI-governance work (risk-controls module §6).

## 7. Courts, evidence and disclosure of AI use

- *Kohls v. Ellison* (D. Minn., 2025) excluded an expert declaration for unverified AI citations; in *Matter of Weber*
  (N.Y. Sur. Ct., 2024) the court re-ran an expert's Copilot queries, got different numbers, and said counsel must
  disclose AI use [KTS-EXPERTAI-2026; GOLDMAN-WEBER-2024]. The failures turned on unverified or unreproducible
  output; *Weber* also held that counsel must disclose AI use and that AI-generated evidence may face a Frye hearing.
- Proposed Rule 707 would apply Rule 702 reliability tests to machine output offered without an expert. It is not law:
  in May 2026 the evidence rules committee withdrew the published draft and sent a modified proposal for further study
  [USCOURTS-FRE707-2025; USCOURTS-EVID-2026].
- Prompts and drafts could be discoverable in some circumstances, panellists say [BVR-DISCOVERY-2026].
- Deliverable failures carry fee consequences: Deloitte Australia agreed to repay the final instalment of a government
  review contract after AI-generated errors [CITYAM-DELOITTE-2025].

## 8. Steps that need human judgment

| Line | Steps that stay with a named person (from the modules) |
|---|---|
| CAS | Low-confidence coding, write-offs, accruals and estimates, approval of agent plans and entries, period sign-off, payment release |
| Risk and controls | Scope and risk ratings, sufficiency of evidence, missing support versus failure, deficiency severity, approving auto-clear rules, sign-off |
| Transactions | Which flags become adjustments; add-backs, working capital and debt-like items; what matters to the deal; sign-off |
| Valuation | Selecting comparables and inputs, projection assumptions, reconciling methods, the conclusion of value, signing and defending |
| Forensic | Whether an anomaly is meaningful, damages, validating review output, authoring and explaining every opinion, testimony |
| FP&A | Targets and assumptions, which variance explanation is true, model structure, sign-off of anything a board or lender relies on |
| Private client | Posting and moving money, investment, legal and estate interpretation, sign-off on reports, relationships with principals |
| All lines | Independence and consent decisions; for audit clients, every management decision |

## 9. Checks before a plan goes ahead

1. Which clients in scope are attest clients of the firm or an affiliate, under which regime, and who confirmed it?
2. Does the design host client data or build AI the client relies on? Is the independence analysis written down?
3. Is the fee basis eligible for every client in scope (no contingent fee for restricted clients)?
4. Which tools touch client data, on which terms, with what consent, and what does the engagement letter say?
5. Is there a named reviewer, a record of AI use on the file, and a reproducible result where a lender, court or auditor
   will rely on it?
6. Has the vendor's accuracy claim been reproduced on the firm's own data, with an exit plan if the vendor fails?

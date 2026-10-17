# Assurance guardrails

Last researched 2026-10-17. Use this in Frame (constraints), in Reimagine (fit checks), in Make the case (risks and
human checkpoints) and whenever someone says "the regulator won't allow it". "Guidance" here is non-binding unless
stated; the binding layer is the auditing and quality standards (ISA and ISQM, PCAOB, AICPA), the ethics codes and the
law. Firm-level tool governance in depth is in [quality-management](modules/quality-management.md). Source keys in
brackets resolve in §12 or in [sources.md](sources.md).

## Contents

1. [Principles](#1-principles)
2. [Who sets or enforces what](#2-who-sets-or-enforces-what)
3. [Standards changing, with dates](#3-standards-changing-with-dates)
4. [What inspectors look at](#4-what-inspectors-look-at)
5. [Documentation and evidence](#5-documentation-and-evidence)
6. [Client data and confidentiality](#6-client-data-and-confidentiality)
7. [EU AI Act](#7-eu-ai-act)
8. [Independence, ownership and AI vendors](#8-independence-ownership-and-ai-vendors)
9. [Liability and insurance](#9-liability-and-insurance)
10. [Steps that need human judgment](#10-steps-that-need-human-judgment)
11. [Checks before a plan goes ahead](#11-checks-before-a-plan-goes-ahead)
12. [Sources](#12-sources)

## 1. Principles

- **No regulator prohibits AI in audit, and every one that has spoken keeps the human auditor accountable.** The FRC says
  accountability is unchanged [FRC-NEWS-2026]; IFIAR says audits "will remain human-led" and firms should explain what that
  means [IFIAR-TTF-2026]; India's NFRA staff say the opinion belongs to an identified auditor, not a tool
  [NFRA-CAALLEY-2026]; the AICPA says the auditor remains responsible for the audit and the opinion [JOFA-AIPA-2026].
- **The binding rules have barely changed; the guidance layer has.** Several regulators say their AI guidance creates no
  new requirement [FRC-AIAUDIT-2025; NFRA-CAALLEY-2026]. The IAASB chose guidance over a technology requirement
  [IAASB-ED500-2026].
- **Regulatory attention is moving from the single tool to the firm's system of quality management** [FRC-SUPERVISION-2026;
  IFIAR-TTF-2026; JOFA-QC1000-2026].
- **Regulation is rarely the real blocker.** PCAOB staff recorded in 2024 that firms did not see standards as impediments
  [PCAOB-GENAI-2024]. When a leader says "regulation stops us", ask which document says so.

## 2. Who sets or enforces what

| Body | Role | AI position, dated | Binding? |
|---|---|---|---|
| PCAOB (US) | Standards and inspections for US issuer audits | 2024 staff outreach; technology-assisted-analysis amendments; QC 1000 amendments adopted 9 Sep 2026; data and technology research project; independence project [PCAOB-GENAI-2024; PCAOB-SSR-PAGE-2026] | Standards yes; staff material no |
| SEC (Office of the Chief Accountant) | Oversees the PCAOB; owns independence rules | Independence rules must stay fit for purpose as AI enters audit delivery; review starts with refreshed FAQs (June 2026) [KPMG-HOHL-2026; TR-HOHL-2026] | Rules yes; speeches no |
| IAASB | ISAs, ISQMs, ISSA 5000 | Evidence exposure drafts (5 Aug 2026); technology quality-management guides planned [IAASB-ED500-2026; IAASB-TQMPLAN-2026] | Standards yes; guides no |
| IESBA | International ethics and independence code | 2023 technology revisions in force; no further code changes planned; AI material planned [IESBA-SNAPSHOT-2026] | Code yes |
| IFIAR | Forum of audit regulators | Technology reports (Mar 2025, Apr 2026) [IFIAR-TTF-2025; IFIAR-TTF-2026] | No |
| FRC (UK) | Regulator and standard-setter | AI documentation guidance (Jun 2025); certification thematic review; GenAI and agentic guidance (30 Mar 2026); sandbox; new supervision model [FRC-AIAUDIT-2025; FRC-ATT-2025; FRC-GENAI-2026; FRC-SANDBOX-2026] | Standards yes; guidance not prescriptive |
| AICPA (ASB, ethics committee, peer review board) | US non-issuer standards, ethics code, peer review | Practice aid (13 Oct 2026); SOC guidance on AI (11 Sep 2026); alternative-practice-structure project; SOC 2 peer-review alert (May 2026) [AICPA-PA-2026; DART-TQA-2026; JOFA-PEEC-2026; JOFA-PEER-2026] | Standards and code yes; practice aids no |
| CPAB (Canada), NFRA (India), IRBA, AUASB | National regulators and standard-setters | Inspection observations; principles; risk communiques [CPAB-EVOLVING-2025; NFRA-CAALLEY-2026; IRBA-AI-2024; AUASB-AI-2025] | Guidance |
| COSO | Internal control framework | Generative AI control guidance (Feb 2026) [JOFA-COSO-2026] | Voluntary |
| EU institutions, EDPB | AI Act; GDPR | AI Omnibus adopted by 1 Jul 2026 [ADDLESHAW-AIOMNIBUS-2026; EDPB-OPINION-2024] | Law |

## 3. Standards changing, with dates

| Item | Status | Date | Source |
|---|---|---|---|
| PCAOB technology-assisted-analysis amendments (AS 1105, AS 2301) | In force | Fiscal years beginning on or after 15 Dec 2025 | [PCAOB-TAA-2024] |
| PCAOB AS 2310 (confirmations; direct access to external sources) | In force | Fiscal years ending on or after 15 Jun 2025 | [PCAOB-AS2310-2023] |
| PCAOB QC 1000, as amended | Adopted 9 Sep 2026; SEC approval pending at last check | 15 Dec 2026 | [PCAOB-SSR-PAGE-2026; JOFA-QC1000-2026] |
| ISSA 5000 (sustainability assurance) | Issued | Periods beginning on or after 15 Dec 2026 | [ISSA5000-2024] |
| ISA (UK) 620 on using experts | Final | 15 Dec 2026 | [FRC-620-2026] |
| IAASB ED ISA 330, 500, 520 | Exposure draft | Comments by 15 Dec 2026; final not before 2027 (inference) | [IAASB-ED500-2026] |
| PCAOB auditor independence | Proposal in preparation | Q1 2027 (anticipated) | [PCAOB-SSR-PAGE-2026] |
| AICPA alternative practice structures | Second exposure draft in preparation | After the October 2026 meeting | [JOFA-PEEC-2026] |
| AICPA SAS 150 (confirmations) and SAS 151 (fraud) | Issued or approved | Periods ending on or after 15 Dec 2028 | [JOFA-SAS150-2026; JOFA-SAS151-2026] |
| EU AI Act high-risk obligations | Delayed by the Omnibus | 2 Dec 2027 (Annex III); 2 Aug 2028 (Annex I) | [GIBSONDUNN-AIOMNIBUS-2026] |

## 4. What inspectors look at

- **FRC.** Most of the six largest UK firms had established certification processes for automated tools, some less
  mature and undocumented, and firms were still adapting certification to AI risks and building ways to monitor use and
  quality impact [FRC-ATT-2025]. From April 2026 supervision puts the firm's system of quality management at the centre
  [FRC-SUPERVISION-2026]. The March 2026 guidance was "not a response to identified quality deficiencies" [FRC-NEWS-2026].
- **IFIAR.** 31% of members found tools not used as intended [IFIAR-TTF-2025]. Monitoring may be fragmented between
  networks and member firms. Documents such as invoices "may originate from AI systems", and auditors should watch for
  deliberate misuse of AI by audited entities [IFIAR-TTF-2026].
- **CPAB.** The first public AI-type finding: tools used as primary evidence with limited input validation and no testing
  of items rated low risk [CPAB-EVOLVING-2025].
- **PCAOB.** Inspectors said AI and private-equity transactions would be 2026 focus areas [CAALLEY-PCAOBPE-2025]; no
  inspection-report finding specific to AI tools was found.
- **AICPA peer review.** A May 2026 alert targets SOC 2 engagements with identical reports, risk assessments and samples,
  and asks reviewers to understand the firm's use of SOC platforms [JOFA-PEER-2026].

## 5. Documentation and evidence

- **Central versus file (FRC, the most detailed).** Centrally: what the tool is, when it is appropriate, how it was built
  and on what data, why the firm trusts it, training (including against automation bias) and explainability. On the
  audit file: tool and model version, configuration and prompts or data input, why use was appropriate, approval, and
  how outputs informed conclusions [FRC-AIAUDIT-2025].
- **Proportionate.** The more widely a tool is used, the more sits centrally; for a language-model tool whose outputs are
  all checked to cited sources it "may well be appropriate to document less" [FRC-AIAUDIT-2025].
- **Traceable.** An experienced auditor with no prior involvement should be able to follow which tool processed which
  balance and how much human review followed [CPAB-EVOLVING-2025; NFRA-CAALLEY-2026].
- **Revalidate on change.** Re-approve tools when they or their models change [IFIAR-TTF-2026; NFRA-CAALLEY-2026].
- **No lower evidence bar.** Tool output meets the same evidence standard; low-risk classifications by a tool should be
  tested periodically [NFRA-CAALLEY-2026]. AI-enabled procedures need not match the persuasiveness of the procedure they
  replace if the methodology does not overstate them [FRC-GENAI-2026].
- **No safe harbour for LLM evidence.** The IAASB considered and rejected a requirement to evaluate tool inputs,
  operation and outputs, because for GenAI that may be impossible [IAASB-ED500-2026]. Firms build the test themselves.

## 6. Client data and confidentiality

- **Ethics codes apply in full.** The IESBA code covers the whole data lifecycle, and using client data to train AI
  "requires proper authorization" [IESBA-SNAPSHOT-2026]. AICPA ethics staff suggest asking, before pasting client data
  into an AI system: is it confidential client information, is specific consent needed, could it reach third parties
  [JOFA-ETHAI-2026].
- **Firms stay responsible for vendors.** A firm "cannot rely on a vendor's terms of service (without validation)";
  contracts should cover data protection, explainability documentation, audit rights and continuity [NFRA-CAALLEY-2026].
- **Privacy law can limit tools.** The IAASB draft lists data-protection law as a factor and notes some client data may
  not be used in some tools without consent or safeguards [IAASB-ED500-2026].
- **Engagement letters.** AICPA guidance (as reported) says AU-C 210 does not require naming AI tools, though state law
  or firm policy may [AT-AICPAPA-2026]; South Africa's regulator recommended engagement-letter language on AI use
  [IRBA-AI-2024].
- **Gap.** No audit regulator document works through GDPR roles, lawful basis or transfers for audit AI tools.

## 7. EU AI Act

- Audit firms mostly meet the Act as deployers of general-purpose tools and as employers. Annex III as published names
  employment and credit scoring but, on one reading, no audit or assurance category [AIACT-ANNEX3].
- An AI tool for staffing, task allocation or performance evaluation could fall in the employment category depending on
  design (an inference, not a regulator statement) [AIACT-ANNEX3].
- The AI literacy duty has applied since 2 Feb 2025, softened by the Omnibus to supporting staff literacy
  [GIBSONDUNN-AIOMNIBUS-2026].
- Clients using AI for credit scoring or HR decisions may be in scope from December 2027, which is audit-relevant
  compliance exposure (inference) [AIACT-ANNEX3; GIBSONDUNN-AIOMNIBUS-2026].

## 8. Independence, ownership and AI vendors

- **SEC and PCAOB** are reviewing independence rules, prompted by private equity and AI adoption; a PCAOB proposal is
  anticipated in Q1 2027 [TR-HOHL-2026; PCAOB-SSR-PAGE-2026].
- **AICPA.** Contract terms that shift control, judgment, fees or evidence access to a SOC tool provider can threaten
  independence, and "may also be relevant" to other attest work [JOFA-SOCETH-2026]. Building or hosting an AI system for an
  attest client can raise independence concerns [JOFA-ETHAI-2026]. Whether licensing an AI audit tool from a vendor that
  also serves audit clients raises an issue is unresolved [AT-PEEC-2026].
- **IESBA.** The 2023 technology revisions cover self-review, management responsibility and commercial dependencies in
  technology services [IESBA-SNAPSHOT-2026].
- **UK.** The FRC is "not in principle against" private capital and expects early engagement with full candour
  [FRC-PCLETTER-2024].
- Treat vendor equity, fee-sharing, referral or control terms, and any outside capital, as items for independence review
  before a plan commits. Module detail: [acceptance-independence](modules/acceptance-independence.md).

## 9. Liability and insurance

- No reported case turns on AI use in an audit. A UK law firm expects ordinary negligence principles to apply: an AI
  error is "unlikely, by itself" to be a defence, and liability is unlikely to shift to the tool provider
  [DAC-AUDITAI-2026].
- Likely triggers it names: unreviewed reliance, AI-flagged anomalies not investigated, staff who do not understand tool
  limits, weak governance or testing [DAC-AUDITAI-2026]. A US law firm adds confidential data in AI platforms
  [HEPLER-LIAB-2026].
- Underwriters say standard professional liability cover generally includes AI-related negligence unless a policy has an
  AI exclusion, and exclusions may follow claims growth; this is not audit-specific [BUSINESSINS-AIEO-2026]. Check the
  wording at renewal.

## 10. Steps that need human judgment

No regulator publishes a closed list of human-only steps. The shared structure is accountability plus defined control
points.

| Step or decision | What regulators say | Source |
|---|---|---|
| Forming and signing the opinion | Belongs to an identified auditor; responsibility unchanged | [NFRA-CAALLEY-2026; JOFA-AIPA-2026] |
| Decision checkpoints in agent workflows | Assign named people; review autonomous decisions overall | [IFIAR-TTF-2026] |
| Choosing control points | Set by judgement from the main risks of deficient output; can trigger when a tool escalates | [FRC-GENAI-2026] |
| Risk assessment conclusions | An AI risk output is an input to judgement, not a conclusion | [FRC-GENAI-2026] |
| Review of AI output | Reviewers need competence, scepticism and awareness of automation bias; may need an independent view of the source | [FRC-GENAI-2026] |
| Scepticism | Cannot be delegated; fluent output must not reduce challenge | [NFRA-CAALLEY-2026; IESBA-SNAPSHOT-2026] |
| Relying on opaque output | "Not acceptable" without assessing fitness, limits and data quality | [IESBA-SNAPSHOT-2026] |
| Supervision and review responsibilities | Unchanged by AI use | [PCAOB-GENAI-2024] |
| Low-risk items screened out by a tool | Test them periodically | [NFRA-CAALLEY-2026; CPAB-EVOLVING-2025] |

None of the sources says going concern, EQR or KAM selection must be human-only by rule; they stay with the auditor
through the accountability principle.

## 11. Checks before a plan goes ahead

- Is each tool certified for this use, and what triggers recertification when the vendor updates the model?
- Can the firm show, for one tool on one engagement, what sits on the file and what sits centrally?
- Who owns monitoring (network, member firm, engagement team), and what is measured?
- What client data can go into which tool, and who approved that against confidentiality duties and engagement terms?
- Has independence reviewed every vendor and capital relationship in the plan?
- What did the last professional-indemnity renewal say about AI?
- For EU operations: has anyone decided whether staffing or performance tools fall under the AI Act's employment category?

## 12. Sources

Keys not listed here are in [sources.md](sources.md).

<!-- sources:auto -->
- **AT-AICPAPA-2026**: Accounting Today, *AICPA releases practice guide for auditors dealing with AI* (press, 14 Oct 2026). https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai
- **FRC-SUPERVISION-2026**: FRC, *FRC introduces evolved approach to audit supervision* (regulator, 25 Mar 2026). https://www.frc.org.uk/news-and-events/news/2026/03/frc-introduces-evolved-approach-to-audit-supervision/
- **HEPLER-LIAB-2026**: Hepler Broom LLC, *Professional Liability Risks for CPA Firms in 2026 (white paper, Glenn E. Davis)* (law firm, Jun 2026). https://heplerbroom.com/wp-content/uploads/2026/06/accounting-malpractice-white-paper-8JY697202.pdf

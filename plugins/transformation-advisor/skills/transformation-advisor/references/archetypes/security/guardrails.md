# Security guardrails

Last researched 2026-10-17. Use this in Frame (constraints), in Reimagine (fit checks) and in Make the case (risks).
It covers reporting clocks, accountability, rules about AI, insurance, provider duties and the steps that need a
person. This is not legal advice: where the sources leave a question open, say so and point to counsel. Module files
hold step-level guardrails. Source keys in brackets resolve in §10 or in [sources.md](sources.md).

## Contents

1. [The short version](#1-the-short-version)
2. [Disclosure and reporting clocks](#2-disclosure-and-reporting-clocks)
3. [Accountability and personal liability](#3-accountability-and-personal-liability)
4. [Rules and standards about AI](#4-rules-and-standards-about-ai)
5. [Cyber insurance as a guardrail](#5-cyber-insurance-as-a-guardrail)
6. [Steps that need human judgment](#6-steps-that-need-human-judgment)
7. [Service providers and data](#7-service-providers-and-data)
8. [Readiness for AI incidents](#8-readiness-for-ai-incidents)
9. [Questions to ask](#9-questions-to-ask)
10. [Sources](#10-sources)

## 1. The short version

- **No rule read bans or specifically regulates AI in SOC triage or response.** EU and New York texts encourage
  defensive AI [EURLEX-NIS2-2022, recital 51; EC-ACTIONPLAN-2026; NYDFS-AI-2024]. No rule found mandates human
  approval of SOC actions; that is an absence in the sources, not a legal opinion.
- **What binds:** accountability of the management body, reporting clocks started by human determinations,
  third-party and data-protection duties, risk-assessment updates and, for providers of high-risk AI, oversight design.
- **Direction is mixed.** US disclosure rules face rollback pressure while EU product reporting went live; "US
  loosens, EU tightens" is too simple [SIFMA-SEC-2026; EC-CRAREPORTING-2026; EC-NIS2].
- **Hygiene is becoming a regulatory expectation** because AI speeds up vulnerability discovery [NYDFS-FRONTIER-2026;
  GOVIE-NCSC-2026].

## 2. Disclosure and reporting clocks

| Regime | Clock (as sourced) | Status on 2026-10-17 | Source |
|---|---|---|---|
| SEC Form 8-K Item 1.05 (US listed companies) | Four business days after the company determines an incident is material; Item 106 requires annual description of risk management and governance | In force; trade groups urged rescission on 2026-04-10; no rescission found | [SEC-CYBER-2023; SIFMA-SEC-2026; DEBEVOISE-8K-2026] |
| NIS2 (EU essential and important entities) | Early warning 24 hours from awareness of a significant incident; notification 72 hours; final report within a month | In force; Commission proposed easing amendments on 2026-01-20 | [EURLEX-NIS2-2022, Art 23; EC-NIS2] |
| DORA (EU financial entities and ICT providers) | Major ICT incidents reported on templates; time limits in technical standards (not read) | Applied from 2025-01-17 | [EURLEX-DORA-2022, Art 19; EIOPA-DORA-2025] |
| Cyber Resilience Act (EU product manufacturers) | 24 hours early warning, 72 hours notification for actively exploited vulnerabilities and severe incidents | Reporting applies from 2026-09-11; main duties from 2027-12-11 | [EC-CRAREPORTING-2026; EC-CRA-2026] |
| CIRCIA (US critical infrastructure) | 72 hours for covered incidents, 24 hours for ransom payments | Final rule sent for White House review 2026-10-01 | [COVINGTON-CIRCIA-2026] |
| UK Cyber Security and Resilience Bill | 24-hour report, full report in 72 hours (as described by the Government); medium and large MSPs in scope | In the House of Lords | [HANSARD-CSRB-2026] |
| HIPAA Security Rule overhaul (US health) | Proposes a technology-asset inventory that would include AI touching ePHI | Proposal (NPRM 2025-01-06); no final rule found in the sources read | [HHS-HIPAA-NPRM-2025] |
| EU AI Act serious-incident reporting | Providers of high-risk AI report serious incidents, outer limit 15 days | A provider duty, not a general SOC duty | [AIACT-EXPLORER-2024, Art 73] |

Practice note: after SEC staff's May 2024 clarification, 29 issuers filed under Item 1.05 and 50 under Item 8.01 for
incidents not yet determined material (law-firm tracker, to 2026-05-21) [DEBEVOISE-8K-2026]. Whether AI-assisted
detection changes when an entity is "aware" is a legal question the sources do not answer; raise it before automating
incident classification.

## 3. Accountability and personal liability

- **Management bodies, not CISOs as such, carry it in the EU.** NIS2 has management bodies approve and oversee
  risk-management measures and makes them liable; maximum fines for essential entities are at least EUR 10M or 2% of
  worldwide turnover, whichever is higher [EURLEX-NIS2-2022, Art 20, Art 34]. DORA gives the management body ultimate responsibility for
  ICT risk [EURLEX-DORA-2022, Art 5].
- **US: the SolarWinds case ended.** Most SEC claims against SolarWinds and its CISO were dismissed in 2024; claims
  that survived concerned the published "Security Statement" [HUNTON-SOLARWINDS-2024]. The SEC dismissed the rest with
  prejudice on 2025-11-20 [COVINGTON-SOLARWINDS-2025]. CISOs interviewed afterwards still describe responsibility
  without authority, and stress accuracy in public descriptions of security programmes and D&O cover [CSO-SOLARWINDS-2025].
- **Who answers for AI harm is unsettled.** Asked who would be responsible if an AI system causes harm, ISACA poll
  respondents split: 28% board or executives, 18% CIO or CTO, 13% CISO, 20% did not know [ISACA-AIPULSE-2026]. Dark
  Reading reports that no legal system has tested an agent-caused breach [DARKREADING-LIABILITY-2026].
- **Staffing and liability:** 76% of ISC2 respondents agreed organizations should be held accountable for a breach
  after cutting security staff (opinion) [ISC2-WORKFORCE-2025].

## 4. Rules and standards about AI

**Binding or supervisory**
- **EU AI Act:** applicable from 2026-08-02; Annex III high-risk duties moved to 2027-12-02 by the AI Omnibus (in force
  2026-07-27) [EC-AIACT-2026]. Annex III covers AI used as safety components in managing critical digital
  infrastructure; whether a SOC or detection tool qualifies is for counsel [AIACT-EXPLORER-2024, Annex III]. High-risk
  providers must let people override output and stop the system, and resist manipulation [AIACT-EXPLORER-2024, Art 14, 15].
- **NIS2 recital 51:** Member States should encourage AI for detection and prevention, in line with data-protection law
  (accuracy, minimisation, fairness, transparency, security) [EURLEX-NIS2-2022].
- **NYDFS (New York financial services):** the 2024 letter adds no requirements but expects board-level understanding
  of AI risk, third-party diligence and training for security staff, and suggests MFA factors that deepfakes cannot
  impersonate; it notes AI's value for log review and anomaly detection [NYDFS-AI-2024]. The 2026-05-21 letter asks for faster remediation and updated
  risk assessments [NYDFS-FRONTIER-2026].

**Voluntary guidance and standards** (no duty, but customers, auditors and insurers cite them)
- NIST CSF 2.0 (the value chain here) [NIST-CSF-2024]; NIST AI RMF [NIST-AIRMF]; NIST AI 100-2 adversarial ML
  taxonomy [NIST-AI1002-2025]; COSAiS control overlays for AI, in draft [NIST-COSAIS-2026].
- CISA with Australia's ACSC, "Careful Adoption of Agentic AI Services" (2026-05-01) [CISA-AGENTIC-2026].
- OWASP Top 10 for LLM Applications [OWASP-LLM-2025] and for Agentic Applications [OWASP-AGENTIC-2025]; MITRE ATLAS
  [MITRE-ATLAS] and ATT&CK v20 AI techniques [MITRE-ATTCK-2026].
- ISO/IEC 42001 certification appears in vendor practice (ai-security, governance-risk); its text was not reviewed.

## 5. Cyber insurance as a guardrail

- **Underwriting asks for baseline controls:** MFA, EDR, backups and third-party oversight, increasingly with a vendor
  inventory [BIS-FSI75-2026]. Know what your insurance application attests to.
- **AI in cyber policies:** "So far, AI risks are not yet excluded in most cyber policies," per a BIS/FSI paper, which
  warns of "silent AI" [BIS-FSI75-2026]. Beazley confirmed affirmative AI wording in its cyber and tech E&O policies
  (2026-09-17), for AI-related risks it says were already covered, subject to jurisdiction and terms [BEAZLEY-AICYBER-2026].
- **Exclusions elsewhere:** optional generative-AI exclusions for US general liability took effect January 2026
  [INDAGENT-VERISK-2025]; CSIS reports, second-hand, that regulators approved more than 80% of carrier requests to
  exclude AI-related damages, and reads AI-related breaches as generally still insurable under standalone cyber
  [CSIS-INSURANCE-2026]. Wording, not headlines, decides coverage.

## 6. Steps that need human judgment

What the sources place on a person, with the reason:

| Step | Why a person | Source |
|---|---|---|
| Materiality, "significant incident", "major ICT incident", CRA reportability | Each starts a legal clock; the determination is the entity's | [SEC-CYBER-2023; EURLEX-NIS2-2022; EURLEX-DORA-2022; EC-CRAREPORTING-2026] |
| Approving and overseeing risk measures, and AI risk reporting to the board | Management-body duty | [EURLEX-NIS2-2022, Art 20; EURLEX-DORA-2022, Art 5; NYDFS-AI-2024] |
| Dispositions on escalated or contested alerts; sampling what the AI closed | Benchmarks show high miss rates for some designs; log content can steer AI | [ARXIV-2610.10608; ARXIV-2605.24421] |
| Containment and other actions touching users, production or availability | Event SOCs keep humans on critical responses; agents "prepare", analysts decide | [SPLUNK-RSACSOC-2026; CISCO-SPLUNK-CONF26-2026] |
| Granting and withdrawing agent autonomy; halting an agent | Oversight design for high-risk AI includes a stop function | [AIACT-EXPLORER-2024, Art 14] |
| Risk acceptance and exceptions | Accountability sits with named owners | governance-risk module |
| Customer-facing MDR decisions | Gartner's quoted definition keeps MDR "human-led" | [EXPEL-GARTNERMDR-2026] |

Caution: a named reviewer without evidence, time or tooling is not a control. Only 36% in ISACA's poll say humans
approve most AI actions before execution [ISACA-AIPULSE-2026].

## 7. Service providers and data

- **Providers are named in law as suppliers and targets.** NIS2 recitals 85-86 put MSSP risk into supply-chain duties
  and note that providers have been targeted [EURLEX-NIS2-2022]; the UK bill brings medium and large MSPs into scope
  [HANSARD-CSRB-2026].
- **Customers' regulators expect AI diligence on vendors:** NYDFS points to third-party diligence and notification
  terms [NYDFS-AI-2024]. An MDR provider selling an agentic service should expect clients to ask who decides, who logs
  and who notifies.
- **AI in the security stack is itself an asset to inventory:** NYDFS, HHS and NIST point to inventories, risk
  assessments and board reporting that include AI [NYDFS-AI-2024; HHS-HIPAA-NPRM-2025; NIST-COSAIS-2026]. Shadow AI in
  the SOC is a compliance gap, not only a leak risk.
- **Data leaving the tenant:** logs, cases and code often hold personal and customer data; data-protection conditions
  apply to defensive AI [EURLEX-NIS2-2022, recital 51]. Zero-retention and self-hosted options are in operations §6.
- **Not covered by the sources:** provider liability caps and indemnities, professional indemnity for AI-assisted
  services, GDPR articles on automated decisions in security tools, APAC and Middle East regimes.

## 8. Readiness for AI incidents

ISACA's State of Cybersecurity 2026 (more than 1,800 respondents, global): 8% of organizations conduct AI-related
incident response exercises regularly and 64% have run none; 17% include AI in broader exercises and 16% plan to;
48% either do not know whether they have AI incident playbooks or say they have none [ISACA-SOC-2026]. In ISACA's
poll, 56% did not know how fast they could halt an AI system after an incident, and 43% had high confidence they
could investigate and explain a serious AI incident to leadership or regulators [ISACA-AIPULSE-2026].

## 9. Questions to ask

1. Which determinations start a legal clock for you, who makes each one, and what AI-generated analysis feeds it?
2. Is there an inventory of AI in your security tooling, including vendor-embedded features, and does the board see it?
3. If an agent misbehaved today, how fast could you halt it, and when did you last rehearse that?
4. What does your insurance application attest about controls and AI, and has anyone read the AI wording?
5. Which providers use AI on your data, and what do contracts say about notification and data use?
6. Where is the line between "the agent prepares" and "a person decides", and where is it written?

## 10. Sources

Keys not listed here are in [sources.md](sources.md).

- **CSIS-INSURANCE-2026**: CSIS (Gregory C. Allen), *The Insurance Industry's Retreat from AI Threatens to Slow Innovation and Adoption* (think tank, 2026-09-04). https://www.csis.org/analysis/insurance-industrys-retreat-ai-threatens-slow-innovation-and-adoption
- **CSO-SOLARWINDS-2025**: CSO Online, *What CISOs should know about the SolarWinds lawsuit dismissal* (press, 2025-12-22). https://www.csoonline.com/article/4109992/what-cisos-should-know-about-the-solarwinds-lawsuit-dismissal.html
- **EIOPA-DORA-2025**: EIOPA, *Digital Operational Resilience Act (DORA)* (regulator, applied 2025-01-17). https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en
- **HHS-HIPAA-NPRM-2025**: HHS via Federal Register, *HIPAA Security Rule To Strengthen the Cybersecurity of Electronic Protected Health Information (proposed rule)* (regulator, 2025-01-06). https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information
- **MITRE-ATLAS**: MITRE, *ATLAS matrix for AI systems* (standard-setter, checked 2026-10-17). https://atlas.mitre.org/
- **NIST-AI1002-2025**: NIST, *AI 100-2 E2025: Adversarial Machine Learning taxonomy* (standard-setter, 2025-03). https://csrc.nist.gov/pubs/ai/100/2/e2025/final
- **NIST-AIRMF**: NIST, *AI Risk Management Framework* (standard-setter, checked 2026-10-17). https://www.nist.gov/itl/ai-risk-management-framework
- **OWASP-LLM-2025**: OWASP GenAI Security Project, *Top 10 for LLM Applications 2025* (standard-setter, 2025-03-12). https://genai.owasp.org/llm-top-10/
- **SEC-CYBER-2023**: US SEC, *SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure by Public Companies* (regulator, 2023-07-26). https://www.sec.gov/newsroom/press-releases/2023-139

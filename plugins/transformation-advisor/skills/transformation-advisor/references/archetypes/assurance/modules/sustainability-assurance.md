# Sustainability assurance (assurance)

Last reviewed 2026-10-17. Use cases live in `../use-cases/sustainability-assurance.yaml` (13 entries). Ids are shortened
here: `#05` means `assurance-sustainability-assurance-05`. Source keys in brackets, such as [ISSA5000-2024], are in the
YAML or listed in §12.

**Read this first.** This is the thinnest module in the archetype: no use case is graded A or B. No named assurance
provider has published a measured result for AI on a sustainability assurance engagement, and the standards and EU
texts checked never say "artificial intelligence" (they say "automated tools and techniques"). Most AI activity is on
the **preparer side** (the reporting company and its software vendors), and nearly all of it is vendor claims. Keep the
two sides apart, say plainly that evidence is missing, and use this module mainly for context, probes and open questions.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Context: dates, scope and data](#2-context-dates-scope-and-data)
3. [Processes and key steps](#3-processes-and-key-steps)
4. [Where AI is changing the work](#4-where-ai-is-changing-the-work)
5. [Interview probes](#5-interview-probes)
6. [Metrics and benchmarks](#6-metrics-and-benchmarks)
7. [Guardrails](#7-guardrails)
8. [Roles and how they evolve](#8-roles-and-how-they-evolve)
9. [Frontier](#9-frontier)
10. [Open questions](#10-open-questions)
11. [Common objections](#11-common-objections)
12. [Sources](#12-sources)

## 1. What this module covers

Independent assurance over sustainability and ESG reporting: ISSA 5000 (the IAASB's new general standard for
sustainability assurance), CSRD limited assurance over ESRS reports in the EU, ISAE 3000 (Revised) and ISAE 3410
(greenhouse-gas, GHG, assurance) engagements, and US regimes such as California SB 253. It runs from acceptance and
scoping through the entity's double-materiality process (deciding which topics matter for impacts on people and
environment and for financial effects), evidence over estimates and value-chain data, to the conclusion. It also covers
preparer-side AI where it changes what the assurance provider must test.

## 2. Context: dates, scope and data

**ISSA 5000 and the ethics standard**
- ISSA 5000 and the IESSA (IESBA's ethics and independence standards for sustainability assurance) take effect for
  periods beginning on or after **15 Dec 2026**, or "as at" a date on or after it; early application is permitted
  [ISSA5000-2024, para 15; IESBA-SUST-2024]; IESSA independence provisions for value-chain components start for periods
  beginning on or after 1 Jul 2028 [IESBA-SUST-2024]. ISSA 5000 covers limited and reasonable assurance under any
  suitable framework [IAASB-EUFAQ-2025, Q1].
- From that date ISAE 3000 (Revised) no longer applies internationally to sustainability engagements, and ISAE 3410 is
  withdrawn (approved Mar 2025). A jurisdiction that has not yet adopted ISSA 5000, or whose law requires a local ISAE
  3410, may keep the older standard, but practitioners then cannot claim IAASB compliance [IAASB-ISSA5000FAQ-2025, Q1–Q4].
- Adoption (IAASB list, Sep 2026): adopted in Australia (ASSA 5000, periods from 1 Jan 2025), Canada (CSSA 5000, periods
  beginning on or after 15 Dec 2027), the UK, Hong Kong, New Zealand, South Africa, Malaysia and others; in progress in
  Germany, India, Singapore, South Korea and the US, where the AICPA ASB is converging its attestation standards and the
  PCAOB does not adopt IAASB standards. The Netherlands, France, Spain and several other EU states are marked as
  subject to the Commission's delegated act [IAASB-ISSA5000PAGE-2026].

**EU: CSRD after the Omnibus**
- Directive (EU) 2026/470 (OJ 26 Feb 2026) limits CSRD to undertakings above EUR 450 million net turnover and 1,000
  average employees, removes the requirement to adopt reasonable-assurance standards, and sets a limited-assurance
  standard by delegated act by 1 Jul 2027. Member States transpose Articles 1–3 by 19 Mar 2027 [EU-OMNIBUS-2026].
- First-wave companies outside the new scope fall out from financial years starting 1 Jan 2027; Member States may
  exempt them for financial years starting in 2025–2026 [EU-OMNIBUS-2026, recital 31].
- The limited-assurance opinion covers the process used to identify reported information and compliance with the
  digital mark-up (tagging) requirement [EU-OMNIBUS-2026, Art. 2(12)(a)].
- CEAOB technical advice (adopted 25 Sep 2026, published 30 Sep) is based on ISSA 5000 with EU add-ons and carve-outs
  [CEAOB-TA-2026; ACCA-EUPA-2026]; the Commission will launch a public consultation this autumn [ACCA-EUPA-2026].
- Revised ESRS (Delegated Regulation (EU) 2026/1563, OJ 21 Sep 2026) apply from financial years beginning 1 Jan 2027
  [EU-ESRS-2026, Art. 3]; for 2026 years entities may choose among the previous ESRS, the revised ESRS or the previous
  ESRS with certain reliefs [EU-ESRS-2026, Art. 2; WPK-ESRS-2026].
- EY's review of 196 FY2025 CSRD statements found "nearly all" under limited assurance [EY-CSRDBAROMETER-2026].

**US**
- The SEC proposed on 29 May 2026 to rescind its 2024 climate rules [DECHERT-SEC-2026].
- California SB 253: the state's Office of Administrative Law approved CARB's initial regulation on 12 Oct 2026, so the
  first Scope 1 and 2 report is due 10 Nov 2026. The statute directs limited assurance from 2026, but the regulation
  omits it and CARB accepts reports with or without assurance [HL-CARB-OAL-2026; WINSTON-CARB-2026]. Draft 2027
  assurance text was previewed on 21 Jul 2026; a proposed rulemaking package is due in Q4 2026 [HL-CARB-PREVIEW-2026].

**Independence and reporting software (the IESSA line)**
- Implementing sustainability-information systems or reporting software, whether or not the firm built it, creates a
  self-review threat when it forms part of or affects the client's sustainability records or controls
  [IESBA-IESSA-2025, 5606.4 A3].
- A firm or network firm shall not provide IT systems services to a public-interest sustainability assurance client if
  they might create a self-review threat [IESBA-IESSA-2025, R5606.6].
- Taking responsibility for designing or implementing software to collect or produce the client's sustainability data
  is an example of a management responsibility [IESBA-IESSA-2025, 5400.20 A3]. This matters when a firm sells an AI
  reporting tool (`#11`).

**Data challenges**
- Value-chain data: the revised ESRS 1 lets entities estimate from indirect sources, sector averages, samples,
  spend-based data or other proxies; where data covers only part of the value chain the entity discloses that limit,
  except for gross Scope 1, 2 and 3 GHG metrics [EU-ESRS-2026, ESRS 1 paras 65, 91]. Another practitioner's assurance
  report on a value-chain entity may be insufficient, so the practitioner may need other procedures [ISSA5000-2024, A131].
- Estimates, assumptions and lack of verifiable data make forward-looking information hard to assure, and users may
  read it as a guarantee [ACCA-ABMAG-2026].
- In the Reuters Events preparer survey, data quality is a concern for half of respondents and 42% cite data volume as a
  CSRD challenge [TRI-SUSTAIN-2025].

## 3. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Acceptance and continuance (paras 26–29) | Suitable criteria, preconditions, competence, ethics and independence under the IESSA | review-assurance, expert-judgment | Self-review threats when the firm sells or implements reporting software; value-chain independence rules from 2028 |
| Scoping and planning (paras 95–102) | Scope of information assured (all or part), materiality, group and value-chain components, experts | expert-judgment, coordination-scheduling | Regulatory churn: EU scope cut, SEC rescission proposal, CARB timing unsettled |
| Understanding the entity's reporting process (Appendix 2; paras 103L–125) | The materiality or double-materiality process, information system and controls | review-assurance, research-synthesis | Large and judgement-heavy; ISSA 5000 added fuller requirements on it after EU concerns [IAASB-EUFAQ-2025, Q5] |
| Risk assessment and response (paras 103L–152) | Disclosure-level responses for limited assurance; assertion-level for reasonable | expert-judgment, review-assurance | Many topics, sites and value-chain components to weigh in limited time |
| Evidence gathering (paras 89–94; A225–A276) | Inquiry, analytics, inspection, recalculation; supplier and other-practitioner evidence; estimates | review-assurance, data-reporting, research-synthesis | Proxy-based value-chain data; estimates; data quality and volume |
| Misstatements, conclusion and report (paras 153–212) | Evaluate misstatements, obtain representations, form and report the conclusion | expert-judgment, document-production | Scope barely moved 2015–2023: mostly historical environmental data, little on systems or forward-looking information [LEEDS-ASSURANCE-2026] |
| Quality management and documentation (paras 30–74) | Firm-approved technology, supervision and review | review-assurance | Uneven floors: 94% of firms vs 38% of other providers apply ISAE 3000 (Revised) [IFAC-STATEPLAY-2026] |

## 4. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome), reinvent (service or operating model changes). **Only improve and automate have entries. No source
supports a delegate or reinvent use case in this module.** Grades in brackets.

**A. Assurance-provider side (nearly no evidence)**

- *Planning and risk assessment.* Improve: `#06` AI flags high-risk areas, unusual metrics and missing evidence so the
  team can prioritise procedures (idea, D).
- *Disclosure review.* Improve: `#01` map disclosures to ESRS or ISSB requirements and list gaps before testing (C:
  one analyst sentence says Deloitte has an AI-powered Omnia ESG tool). `#02` screen reports for greenwashing-type and
  unsupported claims (C: the same analyst says KPMG uses NLP and ML; a TU Berlin prototype found Spearman rho 0.310
  between wording specificity and internal claim support, and says the aim is review prioritisation).
- *Evidence.* Improve: `#03` anomaly and narrative-versus-number checks over multi-year data (idea, D). `#04` triangulate
  GHG and supplier claims with satellite, emission-factor, media and regulatory data (idea, D).
  Automate: `#07` continuous evaluation of digital data such as meter feeds; ISSA 5000 A249 gives it as an example of a
  permitted approach, not evidence of use (idea, D).
- *Documentation.* Improve: `#05` source-linked drafting of evidence matrices and workpaper summaries (idea, D).
- *Testing the client's AI.* Improve: `#13` procedures over a client's AI-assisted reporting pipeline: tool, data,
  prompts, validation, lineage (idea, D). The IAASB lists related technology questions for sustainability engagements
  (complex systems, external data; AI not named) but rates them "Low" priority, "continue monitoring"
  [IAASB-CATALOG-2026, Theme 10(a)].
- *Not evidenced:* EY's April 2026 agentic-AI release (130,000 assurance professionals, 160,000 engagements) describes
  audit engagements and does not mention sustainability [EY-MENAPR-2026]. Two Big Four ESG assurance job postings list
  no AI duty [KPMG-JOBAU-2026; EY-JOBMY-2026].

**B. Preparer side (vendor claims; matters to assurance through lineage, estimates and independence)**

- Improve: `#08` Workiva's Sustainability Disclosure Agent (launched 12 Jun 2026) scores content against ESRS or ISSB as
  present, partial or missing and drafts text; LLM narrative drafting generally (C). `#10` AI proposes gap-fill methods
  and estimates for missing value-chain data and records the rationale (C). `#12` AI support for double-materiality
  assessments, named a primary use case in a preparer survey (C).
- Automate: `#09` OCR, data cleaning and spend-based Scope 3 classification with calculation lineage; Watershed cites
  65–80% less time to actionable data across test customers (vendor-published) (C). `#11` PwC Germany's CSRD.AI
  Manager collects data, calculates KPIs and speeds up report generation; raises the IESSA 5606 question (C).

## 5. Interview probes

Ask in the person's setting: assurance provider (Big Four, mid-tier, engineering or certification firm) or preparer.

1. **"On your last sustainability engagement, which procedures used automated tools or AI, who approved the tool, and
   where is that recorded?"** Reveals whether any provider-side use exists (`#01`–`#07`) and ISSA 5000 A96–A98 readiness.
2. **"Do the agent platforms your firm rolled out for financial audit reach sustainability engagements yet? If not, what
   would you need to see first?"** Reveals the gap between audit platforms and this module; no source shows the link.
3. **"When a client uses AI to draft narrative, classify Scope 3 spend or fill value-chain gaps, what evidence do you
   ask for (lineage, prompts, model versions, assumptions), and what have you rejected?"** Reveals readiness for `#13`.
4. **"Does your firm or network sell, build or implement sustainability-reporting software for clients you also
   assure? How do you apply IESSA 5606?"** Reveals independence exposure (`#11`), sharpest for public-interest entities.
5. **"How are you preparing for the first ISSA 5000 engagements from 15 Dec 2026: scoping, the entity's materiality
   process, evidence from value-chain components?"** Reveals where effort is going and which steps a tool could serve.
6. **"How much of your clients' reported value-chain data is estimated or proxy-based, and how do you test the
   method?"** Reveals the data problem behind `#09` and `#10`, and the ESRS 1 disclosure of scope limits.
7. **"Which clients stay in scope after the Omnibus, and which regimes (ISSA 5000 locally, CEAOB-based EU standard,
   SB 253) apply to your book?"** Reveals volume and timing, which shape any business case for tools.
8. **"How do you read a report today for balance and unsupported claims?"** Reveals whether `#02` screening would add
   anything, and whether flags would be followed up against evidence.
9. **"Who is on your team: accountants, engineers, other specialists? Who could challenge an AI tool's output?"**
   Reveals competence (ISSA 5000 A98); ICAEW's audit director says firms may need more specialists, including
   non-accountants [ICAEW-VIEW-2026].
10. **"Has a regulator inspected any of your sustainability engagements, or asked about tools?"** Reveals oversight
    pressure; only 17% of IFIAR respondents had inspected such work by 2025 [IFIAR-SATF-2026].
11. **Preparer: "Which reporting steps use AI, and have you walked your assurance provider through the outputs and their
    sources before year-end?"** Reveals whether lineage will survive assurance (Watershed suggests a dry run with your auditor).
12. **"If you tried AI on this work, did you compare its flags or drafts with your own on the same engagement?"**
    Reveals whether any quality evidence exists; none is published.

## 6. Metrics and benchmarks

**No AI-specific accuracy, override, error or inspection figure exists for sustainability assurance.** Use these for
the market baseline.

| Metric | Value | Source |
|---|---|---|
| Large companies with some assurance, 2024 (1,400 companies, 22 jurisdictions) | 75% (51% in 2019); 83% of it limited | IFAC-STATEPLAY-2026, p. 3 |
| Engagements done by audit firms, 2024 | 59% (63% in 2019) | IFAC-STATEPLAY-2026, p. 3 |
| Applying ISAE 3000 (Revised): firms vs other providers | 94% vs 38% | IFAC-STATEPLAY-2026, p. 3 |
| Assured subject matters, 120 large listed companies | 517 (2015) to 2,294 (2023) | LEEDS-ASSURANCE-2026 |
| Assurance quality index (0–1), overall | 0.28 (2015) to 0.36 (2023); scope 0.24 to 0.26 | LEEDS-ASSURANCE-2026 |
| Same firm audits financials and sustainability | 76% in 2023 (65% in the study's comparison year) | LEEDS-ASSURANCE-2026 |
| S&P 500 companies with assurance or verification (2023 data) | 362; 87 from public-company auditors | CAQ-SP500-2025 |
| IFIAR members reporting mandatory assurance (47 took part) | 61% in 2025 (21% in 2023) | IFIAR-SATF-2026 |
| IFIAR members that have inspected sustainability engagements | 17% in 2025 (9% in 2023); 57% planning | IFIAR-SATF-2026 |
| Preparers using AI in reporting | 37% of Scope 1–3 reporters with assurance; 22% without | TRI-SUSTAIN-2025 |
| Practitioner AI risk concerns (Moldova, n = 77, about financial audit) | unclear responsibility 87.3%; overreliance 87.3%; reduced skepticism 82.5% | ASE-CIKE-2025 |
| Vendor time claims (preparer side) | 90% less OCR data entry; 65–80% less time to actionable data | WATERSHED-AI-2026 (`#09`) |

**What to measure if a team tries AI here:** hours per disclosure area before and after; share of AI flags that led to
further procedures; flags the team found that the tool missed (a parallel run); reviewer overrides; review notes on
AI-drafted documentation; inspection or quality-review findings. Treat the Watershed figures as vendor claims.

## 7. Guardrails

**Standards text on technology (none names AI; none prohibits it)**
- ISSA 5000: overreliance on automated tools can stop critical assessment of evidence (A91); firm-approved
  technology and team competence in tools (A96–A98); manual versus automated procedures (A231); real-time tools
  (A249); general IT controls maintain data integrity (A262) [ISSA5000-2024].
- IESSA: decide whether tool output is appropriate before using it (R5320.11); consider tool testing, firm oversight
  and input quality (5320.11 A1); automation bias example (5120.12 A2) [IESBA-IESSA-2025].
- Evidence from only easily accessible sources can bias selection; use multiple sources where possible
  [ISSA5000-2024, A91, A228]. External data is a corroboration aid, not substitute evidence (`#04`).
- Estimates: limited-assurance procedures respond to risk at disclosure level; reasonable-assurance procedures test
  how management developed the estimate [ACCA-ABMAG-2026].
- Regulators' AI guidance is audit-focused: IFIAR's 2026 technology report has no sustainability content
  [IFIAR-TTF-2026]; neither do the IAASB technology quality-management roundtables [IAASB-TQM-2026].

**Steps that stay with a person:** completeness and relevance of each disclosure; the risk assessment; whether an
anomaly or flag needs more procedures; evaluating the entity's materiality process; judging estimates and management
bias; the conclusion on mark-up; sign-off. AI output is a risk signal, not a conclusion [MDPI-SUSAI-2026, ss. 6.2–7.2].

**Preparer-side guardrails that affect assurance:** log every agent hand-off or lineage breaks and auditors cannot
follow the chain; distrust "99%+ accuracy" claims without caveats [WATERSHED-AI-2026]; check AI-drafted statements
against sources, since hallucinated numbers read smoothly [IRIS-GENAI-2026].

## 8. Roles and how they evolve

- ISSA 5000 is designed for professional accountants and non-accountant practitioners [IAASB-ISSA5000PAGE-2026]; audit
  firms did 59% of engagements in 2024 [IFAC-STATEPLAY-2026].
- Researchers expect data-analytics literacy and the ability to challenge AI limits and bias, without turning
  assurance staff into software engineers [MDPI-SUSAI-2026, s. 7.2], plus model-evaluation and data-validation skills
  [MDPI-SLR-2026, s. 4.6].
- ICAEW's audit director says mid-tier and smaller firms face many AI tool providers and must choose investments for
  their scale, and that the range of information in annual reports, such as sustainability information, may mean
  more work with specialists, including non-accountants [ICAEW-VIEW-2026].
- Demand for ESG assurance skills exceeds supply; EY and PwC run sustainability training, not described as AI-related
  [VERDANTIX-GQ-2024]. ESG assurance manager postings list no AI duty; EY asks for ESG data-analysis tools as an
  advantage [KPMG-JOBAU-2026; EY-JOBMY-2026].
- Preparer side: Workiva's product chief says reporting teams are moving from execution to orchestration as agents take
  on more work [ITBRIEF-WORKIVA-2026].
- No source measures team size, staffing pyramid or fees for sustainability engagements.

## 9. Frontier

- **2026-06-09** IFIAR: sustainability inspection programmes at an early stage; most respondents plan them [IFIAR-SATF-2026].
- **2026-06-12** Workiva launches a sustainability disclosure agent aimed at gaps before assurance [ESGNEWS-WORKIVA-2026].
- **2026-07** IAASB Technology Catalog v3: sustainability and technology "continue monitoring", priority Low [IAASB-CATALOG-2026].
- **2026-07-14** ICAEW: the FRC is working on a voluntary sustainability assurance register, possibly later in 2026 [ICAEW-VIEW-2026].
- **2026-07-21** CARB previews 2027 assurance text; rulemaking package expected in Q4 2026 [HL-CARB-PREVIEW-2026].
- **2026-09-21** Revised ESRS published; apply from FY2027 [EU-ESRS-2026].
- **2026-09-25** CEAOB advice adopted; EU limited-assurance standard due by 2027-07-01 [CEAOB-TA-2026; EU-OMNIBUS-2026].
- **2026-09-28** ESMA will consult on tagging rules for sustainability statements (Q1 2027) and keep monitoring AI in
  ESEF, the EU electronic reporting format [ESMA-AWP-2027]. No source links AI tagging to assurance work yet.
- **2026-10-05** IAASB plans ISSA 5000 FAQs on general matters and a joint IAASB-IESBA FAQ in Q4 2026; first technology
  quality-management guide (on AI-enabled tools) anticipated November 2026, subject to approval [IAASB-ENEWS-2026].
- **2026-10-12** California OAL approves CARB's SB 253 initial regulation; no assurance requirement [HL-CARB-OAL-2026].
- **2026-11-10** First SB 253 Scope 1 and 2 reports due [HL-CARB-OAL-2026].
- **2026-12-15** ISSA 5000 and IESSA effective [ISSA5000-2024; IESBA-SUST-2024].
- **2028-03-19** Commission report due on technological solutions for automated sustainability data exchange; the text
  does not mention AI [EU-OMNIBUS-2026, Art. 2(10)].

## 10. Open questions

- Do the Big Four agent platforms reach sustainability engagements? No public statement says so.
- Are Deloitte's Omnia ESG tool and KPMG's greenwashing analytics used on assurance engagements or on readiness work?
  Only one 2024 analyst sentence mentions them, with no figure [VERDANTIX-GQ-2024].
- How will practitioners obtain evidence over preparer information produced by AI? No standard-setter addresses it by
  name; the IAASB will wait for ISSA 5000 experience before deciding on any sustainability-specific clarification on
  technology [IAASB-CATALOG-2026].
- Where is the IESSA line for licensing or configuring an AI reporting tool for an assurance client (`#11`)?
- What will the CEAOB-based EU standard and CARB's 2027 assurance text require, and will either mention technology?
- Will regulator inspections of sustainability work produce findings on tool use? None are published.

## 11. Common objections

- **"AI can't judge double materiality or ESRS alignment."** Agreed in the literature: mapping is a screening aid and
  alignment needs interpretation and judgement [MDPI-SUSAI-2026]. Use AI for finding and listing; keep the assessment
  human (`#01`, `#12`).
- **"We'll stop thinking critically."** The standards name this risk: A91 on overreliance and the IESSA's automation
  bias example. Design review so the practitioner investigates each flag (`#02`, `#03`).
- **"Client numbers from AI can't be traced."** That is the core risk; vendors themselves say an untraceable number
  cannot be verified [WATERSHED-AI-2026]. Ask for lineage and prompt logs (`#13`).
- **"Black-box models won't satisfy regulators."** Researchers flag explainability and bias [MDPI-SLR-2026, s. 4.5].
  Prefer tools whose flags link to source passages.
- **"Selling clients a reporting tool is good business."** Check independence first: the IESSA treats implementing
  reporting software as a self-review threat when it affects the client's sustainability records or controls, and
  bars it for public-interest assurance clients when it might create that threat (`#11`).
- **"Why invest when the rules keep moving?"** A fair point: EU scope is narrower, the SEC proposes rescission and
  CARB's assurance text is pending. ISSA 5000's 15 Dec 2026 date is firm; start with work the standard requires anyway.
- **"Vendors say this saves most of the time."** All figures here are vendor-published, and none comes from an
  assurance engagement. Ask for a named, measured case.

## 12. Sources

Full details for keys used in use cases are in the YAML. Keys used only in this file (all opened and checked on
2026-10-17):
- IESBA-SUST-2024: IESBA, Sustainability project page (effective dates), 2024-12, https://www.ethicsboard.org/consultations-projects/sustainability; IAASB-ISSA5000FAQ-2025: IAASB staff, FAQ on applicability of ISSA 5000, ISAE 3000 (Revised) and ISAE 3410, 2025-08, https://ifacweb.blob.core.windows.net/publicfiles/2025-08/IAASB-ISSA-5000-FAQ-Applicability-ISAE-3000-3410.pdf
- IAASB-ISSA5000PAGE-2026: IAASB, Understanding the ISSA 5000 (adoption list), 2026-09, https://www.iaasb.org/focus-areas/sustainability-assurance
- IAASB-ENEWS-2026: IAASB eNews October 2026, 2026-10-05, https://www.iaasb.org/news-events/2026-10/iaasb-enews-october-2026
- IAASB-TQM-2026: IAASB, Technology Quality Management Roundtables, 2026-02, https://ifacweb.blob.core.windows.net/publicfiles/2026-02/IAASB-Technology-Quality-Management-Roundtables-Feedback.pdf
- CEAOB-TA-2026: CEAOB technical advice on limited assurance on sustainability reporting, 2026-09-25, https://finance.ec.europa.eu/document/download/abd3fbf5-e2e1-4eb2-8af8-8d8fd5803303_en?filename=260925-ceaob-technical-advice-limited-assurance-sustainability-reporting_en.pdf
- ESMA-AWP-2027: ESMA 2027 Annual Work Programme, 2026-09-28, https://www.esma.europa.eu/sites/default/files/2026-09/ESMA22-50751485-1673_Annual_Work_Programme_2027.pdf
- WPK-ESRS-2026: Wirtschaftsprüferkammer, revised ESRS published in the OJ, 2026-09-23, https://www.wpk.de/neu/delegierte-verordnungen-zu-den-ueberarbeiteten-esrs-und-zum-vs-im-eu-amtsblatt-veroeffentlicht/; ACCA-EUPA-2026: ACCA, EU update - September 2026 (Europe public affairs page), 2026-09, https://www.accaglobal.com/sg/en/professional-insights/public-affairs/europe-public-affairs.html
- IFIAR-SATF-2026: IFIAR, Public Factsheet on the 2025 Sustainability Survey Results, 2026-06-09, https://www.ifiar.org/?wpdmdl=20061; IFIAR-TTF-2026: IFIAR, Use of technology in audits: Innovation and audit quality 2026, 2026-04-20, https://www.ifiar.org/?wpdmdl=19893
- IFAC-STATEPLAY-2026: IFAC and AICPA & CIMA, The State of Play: Sustainability Disclosure and Assurance 2019-2024, 2026-06, https://ifacweb.blob.core.windows.net/publicfiles/2026-07/IFAC-State-of-Play-Sustainability-Disclosure-Assurance-2019-2024.pdf
- LEEDS-ASSURANCE-2026: Leeds University Business School and Wits, for the IAASB, The State of Global Sustainability Assurance, 2026-07, https://ifacweb.blob.core.windows.net/publicfiles/2026-07/The-State-of-Global-Sustainability-Assurance-Finding-Snapshot.pdf
- CAQ-SP500-2025: Center for Audit Quality, S&P 500 sustainability reporting and assurance, 2025-07-21, https://www.thecaq.org/aia-sp500-sustainability-reporting-assurance-2025
- EY-CSRDBAROMETER-2026: EY CSRD Barometer 2026, 2026-05-29, https://www.ey.com/en_gl/technical/csrd-technical-resources/ey-csrd-barometer-2026
- EY-MENAPR-2026: EY, global launch of agentic AI in Assurance (MENA release), 2026-04-20, https://www.ey.com/en_ae/newsroom/2026/04/ey-s-global-launch-of-agentic-ai-in-assurance-to-redefine-audit-experience-for-menaclients
- ICAEW-VIEW-2026: ICAEW, 2026: AI and sustainability assurance on the way, 2026-07-14, https://www.icaew.com/insights/viewpoints-on-the-news/2026/jul-2026/2026-ai-and-sustainability-assurance
- KPMG-JOBAU-2026: KPMG Australia, Manager, ESG Assurance posting, 2026-06-04, https://simplify.jobs/p/2f5797de-76c6-43ef-9a21-5502835620ef/Manager--ESG-Assurance; EY-JOBMY-2026: EY, Assurance ESG Manager/Senior Manager posting, 2026-10-03, https://careers.ey.com/ey/job/Kuala-Lumpur-Assurance-ESG,-Manager-Senior-Manager-Fede-50490/1412710033/
- DECHERT-SEC-2026: Dechert, SEC proposes to rescind climate disclosure rules, 2026-06-01, https://www.dechert.com/knowledge/onpoint/2026/6/sec-proposes-to-rescind-climate-related-disclosure-rules.html; WINSTON-CARB-2026: Winston & Strawn (now Winston Taylor), CARB advances climate disclosure rules, 2026-01-29, https://www.winstontaylor.com/insights/carb-advances-climate-disclosure-rules-as-ninth-circuit-appeal-continues
- HL-CARB-OAL-2026: Hogan Lovells, Office of Administrative Law approves CARB's initial regulation implementing SB 253, 2026-10-13, https://www.hoganlovells.com/en/publications/breaking-office-of-administrative-law-approves-carbs-initial-regulation; HL-CARB-PREVIEW-2026: Hogan Lovells, CARB previews 2027 GHG reporting requirements, 2026-07-22, https://www.hoganlovells.com/en/publications/california-air-resources-board-previews-2027-ghg-reporting-requirements-while-2026-reporting

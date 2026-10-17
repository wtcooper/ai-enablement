# Specialists (assurance)

Synthesised 2026-10-17; not yet source-verified. Use cases live in `../use-cases/specialists.yaml` (13 entries).
Ids are shortened here: `#05` means `assurance-specialists-05`. Source keys in brackets are listed in §10.

**Read this first.** This is a low-evidence module. No audit firm, regulator or standard-setter source states that
audit-employed valuation, actuarial, tax, forensic or environmental specialists use AI on audits. The practice
evidence sits with valuation and tax *advisory* practices, which are often management's experts in an audit.
Eight of the 13 entries are ideas (grade D), three are grade C, and the two grade-B entries are adjacent (advisory,
not audit). Use this module mainly for **risk awareness and interview probes**: how to audit expert work and client
models that AI has touched, what ISA 620 and AS 1210 do and do not say, and what the IVSC exposure draft would change.

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

Using the work of experts in an audit: the auditor's own experts (ISA 620; PCAOB AS 1201 Appendix C for
auditor-employed and AS 1210 for auditor-engaged specialists) and management's experts (ISA 500; AS 1105 Appendix A),
across valuation, actuarial, tax, forensic and environmental work. It also covers "AI as a specialist-like input":
a client whose financial reporting leans heavily on AI, which the AICPA compares with complex valuation models and
external specialists [AT-AICPAPA-2026]. IT-audit work on AI components sits in controls-testing and assurance-over-ai.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Decide an expert is needed | Required when expertise outside accounting or auditing is necessary (ISA (UK) 620 para 7): complex instruments, insurance liabilities, reserves, environmental liabilities, contracts and laws, complex tax [FRC-620STD-2026] | expert-judgment | PCAOB inspectors cite teams that did not involve a specialist where they lacked the skill [PCAOB-SPECIALISTS-2025, p12] |
| Evaluate competence, capabilities, objectivity | ISA (UK) 620 para 9; revised para 9A bars an expert whose competence is lacking or whose objectivity threats cannot be reduced to an acceptable level; UK para 9-1 independence confirmation for public-interest audits [FRC-620STD-2026]. PCAOB treats objectivity as a spectrum [PCAOB-SPECIALISTS-2025, p11] | review-assurance | Respondents to the FRC flagged possible inconsistency in judging an "acceptable level" of threat [FRC-620-2026, para 10] |
| Agree the work | Agree scope and who tests data and develops or evaluates assumptions and methods (ISA 620 para 11) [PCAOB-SPECIALISTS-2025, p10] | coordination-scheduling | Unclear roles across core team, specialists and components; specialists engaged late [FRC-ARAQ-2026, p14] |
| Specialist production work | Valuation models, actuarial calculations, tax provision support, forensic analysis, reserve estimates | data-reporting, expert-judgment | Where the AI evidence and ideas cluster (#01-#08, #13); the deployments found are all on the advisory side |
| Evaluate the expert's data, assumptions, methods | Evaluate without re-performing; test company-produced data, evaluate external data [PCAOB-SPECIALISTS-2025, pp6-7] | review-assurance | Report filed but not evaluated; non-financial data (geological, engineering) not tested [PCAOB-SPECIALISTS-2025, p12]; six BDO audits lacked challenge of key valuation assumptions [FRC-ARAQ-2026, p45] |
| Management's expert | ISA (UK) 500 paras A45-A59; AS 1105 Appendix A [FRC-620STD-2026] | review-assurance | Actuarial data behind technical provisions not evidenced on one insurer audit [FRC-ARAQ-2026, p73] |
| New: client AI-based estimate or AI-supported expert | Treat like complex-model work: understand the AI, its logic, data and assumptions [AT-AICPAPA-2026; AUASB-AI-2025] | review-assurance | Opacity: black-box models defeat in-model checks [FORVIS-RESERVING-2025]; restricted access may be a scope limitation [AUASB-AI-2025] |
| Documentation | UK para 15-1: document each request for advice and the advice received [FRC-620STD-2026] | document-production | Teams did not respond adequately to points specialists raised (PwC, one impairment) [FRC-ARAQ-2026, p95] |

Reliance on specialists is partly social: in an experiment with 60 auditors, reliance on IT specialists shifted with
the specialist's office location and how distinct their knowledge was [HIRSCH-2019; abstract only].

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path),
delegate (an agent owns a multi-step outcome), reinvent (the service or operating model changes). **Automate has no
entry, delegate has one idea, and reinvent has one idea.** Do not present any of this as audit-side practice.

**Valuation production (mostly management's experts)**
- Improve: `#01` Big Four valuation practices use AI or RPA for data gathering, formatting and routine model build
  (grade B, adjacent). `#02` CohnReznick adds 73 Strings analytics; Valutico adds AI peer and transaction
  recommendations (announced). `#03` the IVSC says some valuers draft market commentary with public GenAI, and some
  firms fully automate report writing. `#04` idea: AI checks valuation reports for basis of value and consistency.
- Delegate (idea): `#05` agents build whole financial models; benchmarks show they are far weaker on the
  company-specific assumptions that drive value [ARXIV-GAUGE-2026].

**Actuarial work and auditing AI reserving models**
- Improve (ideas): `#06` actuaries use GenAI; the AAA treats GenAI as a model under ASOP No. 56, so it needs validation.
  `#07` actuarial audit specialists benchmark, explain and reproduce a client's AI reserving model. `#08` they build
  an independent AI "challenger" model to test the client's.

**Evaluating experts and client AI**
- Improve (ideas): `#09` ask management's experts whether, how and why they used AI, as the IVSC proposes valuers
  disclose. `#10` apply the complex-model and specialist toolbox to a client's significant AI use.
- Reinvent (idea): `#11` AI and data-science experts become a new kind of auditor's expert.

**Auditor-side evidence and tax**
- Improve: `#12` randomized field experiment: a firm-specific LLM improved quality and speed on an inventory
  valuation task but not guideline adherence (grade C). `#13` KPMG UK tax advisers use Ask Blue J for tax research
  (grade B, adjacent; 2024).

Covered in sibling modules, not repeated: algorithm aversion when the firm's AI contradicts management's estimate
(`assurance-substantive-testing-19`); authenticating AI-fabricated evidence, including forensic skills
(`assurance-substantive-testing-04`); specialists as reviewers of firm AI output (`assurance-quality-management-18`).

## 4. Interview probes

Ask audit partners, specialist leads (valuation, actuarial, tax, forensic) and methodology staff.

1. **"When a client's valuer or actuary says AI or machine learning is in the model, what do you ask for, and who
   signs off?"** Reveals whether AI in management's experts' work is detected at all. The IVSC says valuers use AI
   "knowingly or unknowingly" [IVSC-AI-2025, p10]; PCAOB inspectors already find reports filed but not evaluated.
2. **"Which significant estimates at your clients now rely on AI or ML (reserving, fair value, credit loss)?"**
   Reveals exposure. Only 6% of audit partners rate their largest client's AI governance as advanced (#10).
3. **"If the client or its vendor will not show the model's logic, data or assumptions, what do you do?"** Reveals
   whether alternative procedures exist; the AUASB says restricted access may be a scope limitation (#10).
4. **"Do your own valuation, actuarial, tax or forensic specialists use GenAI or vendor AI on audits? How is it
   approved, and is it in the agreement with the specialist?"** Reveals governance. No public source shows
   audit-side use, so any answer is new information; ISA 620 para 11 is where the agreement would sit.
5. **"How would you assess the competence and objectivity of an AI vendor or data-science team you engage as an
   expert?"** Reveals readiness for revised ISA 620 para 9A (effective 15 Dec 2026): the team that built the
   client's system may face threats that disqualify it if not reduced to an acceptable level (#11).
6. **"Can your actuarial or valuation specialists benchmark a client model, run explainability tests, check
   reproducibility, or build a challenger?"** Reveals capability; Forvis Mazars says these skills are scarce and
   reliance may concentrate on a few management experts (#07, #08).
7. **"What evidence would convince you an AI-built estimate is reliable, and how do you document outputs that
   cannot be reproduced exactly?"** Reveals the evidence standard. The AAA asks whether AI reliance can withstand
   audit challenge (#06); agent-built models are weakest on assumptions (#05).
8. **"Has the line between 'needs a specialist' and 'an AI-assisted generalist can do it' moved?"** Reveals
   skill-gap risk: the AAA says do not use AI to fill a critical skill gap [AAA-GENAI-2024].
9. **"When the firm's AI and a human specialist disagree on an estimate, which do teams believe?"** Reveals
   algorithm aversion: auditors proposed smaller adjustments when contradictory evidence came from AI [COMMERFORD-2022].
10. **"Are you tracking the IVS exposure draft, and will you ask valuers for their AI-use documentation from 2028?"**
    Reveals whether the team sees the coming evidence source (#09).
11. **"When are specialists brought in, and who owns which part of the estimate?"** Reveals the baseline pain AI
    will not fix: late involvement and unclear roles are common firm-identified themes [FRC-ARAQ-2026, p14].
12. **"What has happened to junior specialist training now that data gathering and model build are partly
    automated?"** Reveals talent risk; valuation leaders worry about the apprenticeship model (#01).

## 5. Metrics and benchmarks

**No published figure measures AI use or AI outcomes for specialists on audits.** No inspection finding, override
rate or parallel-run result tied to specialist AI use was found. What exists:
- **UK audits:** some firms deploy GenAI to perform procedures and generate documentation [FRC-ARAQ-2026, p26], but
  the FRC saw "limited use of GenAI on audits" in the past year [FRC-ARAQ-2026, p27]. No specialist-specific count.
- **Tool growth:** the six largest networks reported about 30% more AI-enabled tools in 2025; reporting practices
  differ by network, and no numerator or denominator is given [IFIAR-TTF-2026, p5].
- **Client AI governance (audit partners, largest client):** 6% advanced, 40% developed but incomplete, 46% early
  stage; challenges: in-house expertise 33%, data quality 27%, governance frameworks 27%, model documentation 26%;
  sample size not stated [BOARDMEMBER-CAQ-2026].
- **Field experiment:** 100 auditors, firm-specific LLM, inventory valuation: better quality and speed, no better
  guideline adherence; abstract only, no effect sizes (#12).
- **Agent-built models:** professional analysts' models of the same company agree at a median score of 0.33 under
  standard tolerances, so single-answer grading confuses disagreement with error (#05).
- **Actuarial LLM benchmark:** 12,050 questions from 16 associations; strong on knowledge, weaker on case
  reasoning, spreadsheet and R-code tasks (#06).
- **Hiring:** nearly 7% of Big Four postings required AI expertise in 2025 versus under 2% in 2022 (#11).

**Suggested measures (no benchmark yet):** share of significant estimates where an expert used AI (disclosed or
found); specialist review notes and inspection findings on those estimates; challenger-versus-client model gaps;
reproducibility test results; specialist hours per estimate before and after any AI use.

## 6. Guardrails

**ISA 620 and AS 1210: what they say about AI (nothing explicit)**
- The IAASB narrow-scope amendments (issued 5 Jan 2026, effective 15 Dec 2026) respond to IESBA Code changes on
  external experts and are about ethics and objectivity, not technology [IAASB-620NEWS-2026; FRC-620-2026]. The UK
  version was published 23 Sep 2026 [FRC-620NEWS-2026]. A keyword search found no reference to AI in the standard or
  the feedback statement; of 49 readable IAASB comment letters, only ICAN named AI (#11).
- ISA 620 defines an expert as an individual or organization (para 6(a)), so on its wording **an AI tool is not an
  auditor's expert** [FRC-620STD-2026]. An AI vendor or data-science team engaged as an expert would face
  the para 9A objectivity test (#11).
- PCAOB: AS 1105 Appendix A, AS 1201 Appendix C and AS 1210 are the standards in play; the February 2025 Spotlight has
  no AI content [PCAOB-SPECIALISTS-2025]. The technology-assisted-analysis amendments (fiscal years from 15 Dec 2025)
  say they do not address AI [PCAOB-TAA-2024].
- IAASB ED-500 (5 Aug 2026): the board considered a requirement on tool inputs, operation and outputs and chose
  guidance instead, saying GenAI strains the "input-output" model of audit evidence [IAASB-ED500-2026].

**Auditing AI-influenced expert work and client models**
- Evaluating a company specialist's data, assumptions and methods remains required [PCAOB-SPECIALISTS-2025].
- Heavy client AI use may call for complex-model and specialist procedures; management that cannot explain outputs
  may lack the skills to take responsibility for them (AICPA, non-authoritative) [AT-AICPAPA-2026].
- No access to a third-party AI's logic, data and assumptions, and no alternative procedures, may be a scope
  limitation; do not over-rely on technology-generated information [AUASB-AI-2025].
- For black-box reserving models: data governance before the model, benchmarks, explainability, reproducibility
  and challenger models (#07, #08). Closest non-AI precedent: risk-modelling specialists code-reviewing an
  expected-credit-loss model [FRC-ARAQ-2026, p92].

**The IVSC exposure draft (valuation)**
- Current IVS (effective 31 Jan 2025): no model, AI included, produces an IVS-compliant valuation without the
  valuer's judgment; the valuer must understand and assess any model (IVS 105) [IVSC-AI-2025, pp4-5].
- The January 2026 draft proposes mandatory requirements on "significant use" of AI in scope of work, data and
  inputs, models and documentation, and a new quality-controls chapter (IVS 107). Comments closed 30 Apr 2026;
  publication planned 31 Jan 2027, effective 31 Jan 2028, subject to responses [IVSC-IVSED-2026].
- Idea `#09`: such documentation would feed the auditor's evaluation of a valuer acting as management's expert; no
  source yet shows auditors requesting or using it.

**Other professions and ethics**
- Actuaries: GenAI is a model under ASOP No. 56; validate before use; stay qualified to do the work without AI (#06).
- IESBA staff guidance: accountants should understand a technology well enough to judge whether relying on its
  outputs is appropriate [ICAS-IESBA-2026].
- FRC: reviewers of AI output may need specialist expertise [FRC-GENAI-2026, p37].

**Steps that stay with a person:** deciding an expert is needed; judging competence and objectivity; agreeing scope;
challenging significant assumptions; deciding whether the expert's work is adequate evidence; any scope-limitation
call; the final valuation or actuarial opinion.

## 7. Roles and how they evolve

- **Junior valuation staff** move toward interpreting and validating AI output; firms may need to be more
  intentional about training and mentorship, and some panelists saw juniors reach substantive analysis sooner (#01).
- **Actuarial audit specialists** need machine-learning and coding skills and may become model builders (#07, #08).
- **AI and data specialists** are a new kind of expert: the FRC reports a spike in demand for AI specialists; about a
  third of 54 US firms needed a non-traditional skill such as data science (#11).
- **Tax experts** spend more time on complicated issues, KPMG says (#13). No audit tax-specialist evidence exists.
- **Pricing:** Big Four valuation panelists rejected lower billing rates for AI efficiency and expect value-based
  pricing to evolve [BVR-BIGFOUR-2025].

## 8. Frontier

- **2025-07-23** IVSC paper: AI supports but does not replace valuer judgment [IVSC-AI-2025].
- **2026-01-05** IAASB issues ISA 620 amendments (effective 15 Dec 2026) [IAASB-620NEWS-2026].
- **2026-01 to 04-30** IVS exposure draft with AI requirements and IVS 107 [IVSC-IVSED-2026].
- **2026-03** BV Resources: Big Four valuation leaders on where AI helps and where it falls short [BVR-BIGFOURLIMITS-2026; teaser only].
- **2026-03-26** CohnReznick announces 73 Strings analytics (#02).
- **2026-06-25** IVSC Valuation Dialogue session on AI with PwC US's valuation leader and 73 Strings [IVSC-DIALOGUE-2026].
- **2026-07** Big Four valuation leaders list AI governance among areas needing guidance [BVR-FVGUIDANCE-2026; teaser only].
- **2026-07-22** FRC review plans a thematic on how the largest firms govern GenAI in audits [FRC-ARAQ-2026, p27].
- **2026-07-27** Benchmarks on agent-built valuation models and actuarial LLM capability (#05, #06).
- **2026-08-12** Firms tell the PCAOB AI is a priority but oppose prescriptive standards now [GOINGCONCERN-PCAOB-2026].
- **2026-09-23** UK ISA 620 final [FRC-620NEWS-2026]; SOA GenAI model-governance guide [SOA-GENAI-2026].
- **2026-10-13** AICPA practice aid; more sections promised on risk assessment and evidence [AICPA-PA-2026].
- **2026-11-17** IVSC Advisory Forum session "AI and practical guidance around the globe", Cologne [IVSC-AGM-2026].
- **2026-12-15** Revised ISA 620 effective [FRC-620-2026]; IAASB ED-500 comments due [IAASB-ED500-2026].
- **2027-01-31 (planned)** Next IVS edition published, effective 31 Jan 2028 [IVSC-IVSED-2026].

## 9. Common objections

- **"Our specialists don't use AI, so nothing changes for us."** Management's experts may: Big Four valuation
  practices automate data and model build (#01), providers buy AI analytics (#02), and the IVSC sees valuers using AI
  "knowingly or unknowingly" (#03). Ask the expert, and plan for IVS disclosure from 2028 (#09).
- **"AI can cover where we lack a specialist."** The AAA says actuaries should not use AI to fill a critical skill
  gap (#06), and PCAOB inspectors already cite teams that skipped a needed specialist [PCAOB-SPECIALISTS-2025, p12].
- **"The AI tool is our expert."** Not on ISA 620's wording: an expert is an individual or organization (#11).
- **"We can't audit a black box."** The AUASB says restricted access may be a scope limitation if no alternative
  procedures are possible. Practitioner-proposed alternatives: benchmarks, explainability, reproducibility and
  challenger models (#07, #08).
- **"The model's numbers are exact, so accept them."** Agents build sound models with weak assumptions (#05); LLM
  help did not improve guideline adherence (#12). Conversely, auditors may under-weight AI evidence [COMMERFORD-2022].
- **"Public chatbots are fine for drafting."** The IVSC warns of confidentiality and data-protection breaches;
  EY is building a proprietary platform for this reason (#01, #03).
- **"Wait for the standards."** The IVSC has dates; the AICPA aid exists, though non-authoritative; large firms prefer
  guidance to prescriptive AI rules [GOINGCONCERN-PCAOB-2026]. Existing specialist requirements already apply.

## 10. Sources

Full details for entry sources are in the YAML. Keys cited here that are not in the YAML:
- FRC-620NEWS-2026: FRC, *FRC publishes final revisions to UK standards on using the work of an auditor's expert*,
  2026-09-23, https://www.frc.org.uk/news-and-events/news/2026/09/frc-publishes-final-revisions-to-uk-standards-on-using-the-work-of-an-auditors-expert/
- FRC-620-2026: FRC, *Feedback Statement, ISA (UK) 620 and ISAE (UK) 3000*, 2026-09-23, https://www.frc.org.uk/docs/9935/html/
- IAASB-620NEWS-2026: IAASB, *IAASB Issues Narrow-Scope Amendments Related to IESBA's Using the Work of Experts*,
  2026-01-05, https://www.iaasb.org/news-events/2026-01/iaasb-issues-narrow-scope-amendments-related-iesba-s-using-work-experts
- IAASB-ED500-2026: IAASB, *Exposure Draft: Proposed ISA 500 (Revised), Audit Evidence*, 2026-08-05,
  https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-500-Exposure-Draft.pdf
- PCAOB-TAA-2024: PCAOB via Federal Register, *Notice of filing: amendments related to technology-assisted analysis*,
  2024-07-02, https://www.federalregister.gov/documents/2024/07/02/2024-14488/public-company-accounting-oversight-board-notice-of-filing-of-proposed-rules-on-amendments-related
- FRC-GENAI-2026: FRC, *Generative and Agentic AI Guidance*, 2026-03-30,
  https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf
- IFIAR-TTF-2026: IFIAR, *Use of technology in audits: Innovation and audit quality*, 2026-04-20,
  https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf
- ICAS-IESBA-2026: ICAS, *IESBA issues guidance on the ethical implications of emerging technologies*, 2026-08-20,
  https://icas.com/news-insights-events/news/ethics/iesba-issues-guidance-on-the-ethical-implications-of-emerging-technologies/
- GOINGCONCERN-PCAOB-2026: Going Concern, comment letters on the PCAOB and AI, 2026-08-12,
  https://www.goingconcern.com/firms-and-some-guy-obsessed-with-china-have-weighed-in-on-the-pcaob-turning-an-eye-to-ai/
- IVSC-DIALOGUE-2026: IVSC, *Valuation Dialogue Series 2026* (agenda only), 2026-06-25, https://ivsc.org/ivsc-valuation-dialogue-series-2026/
- IVSC-AGM-2026: IVSC, *IVSC AGM 2026* (agenda only), 2026-06-17, https://ivsc.org/ivsc-agm-2026/
- BVR-BIGFOURLIMITS-2026 (search only): BV Resources, *How Big Four Firms Are Using, and Limiting, AI in Their
  Valuation Practices*, 2026-03, https://www.bvresources.com/articles/business-valuation-update/how-big-four-firms-are-using-and-limiting-ai-in-their-valuation-practices
- BVR-FVGUIDANCE-2026 (search only): BV Resources, *Big Four Valuation Leaders Point to the Need for Fair Value
  Guidance*, 2026-07, https://www.bvresources.com/articles/business-valuation-update/big-four-valuation-leaders-point-to-the-need-for-fair-value-guidance
- COMMERFORD-2022: Commerford et al., *Man Versus Machine: Complex Estimates and Auditor Reliance on AI*, Journal of
  Accounting Research 60(1), https://doi.org/10.1111/1475-679x.12407 (full entry in `assurance-substantive-testing-19`)
- HIRSCH-2019: *The Effect of Spatial Distance and Domain Knowledge Distinctiveness on Auditor Reliance on IT
  Specialists*, Journal of Information Systems, 2019-06-14, https://doi.org/10.2308/isys-52456 (abstract)

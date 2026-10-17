# Controversy (tax)

Sources checked 2026-10-17. Use cases live in `../use-cases/controversy.yaml` (25 entries). Ids are shortened here:
`#05` means `tax-controversy-05`; other modules' ids are in full. Source keys in brackets, such as [GAO-2026], are
given in full in the YAML or in §10. Read this first: almost every figure in this module describes **tax
authorities**, not practitioners.
No firm or in-house team has published an error rate, override rate, parallel-run result or time saving for notice,
examination or Appeals work. Vendor and firm claims are graded C; say so when you quote one. The module is honestly
thin: 10 of 25 entries are graded A or B, and nine of those ten are authority-side.

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

Tax disputes from the taxpayer and adviser side: notices (for example the CP2000, the IRS letter that flags a
mismatch with third-party data), examinations (audits), Appeals and alternative dispute resolution (ADR), collection, and
litigation in the Tax Court or tribunals. It also covers how tax authorities use AI to select, notify, serve and
decide, because that sets the pace and the evidence bar for every dispute. Authorities are scaling AI while
shrinking; practitioners mostly use AI to read notices, draft replies and research, and their failures show up in
court filings.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Selection and matching (authority) | Models score returns and issues; third-party matching and fraud screens generate notices or refund holds | review-assurance, data-reporting | Selection criteria are not published [TSCPA-2026; ACCTODAY-2026] |
| Notice intake and triage | Read the notice, tie it to the return, extract issue, amount and deadline; file a power of attorney; route | transaction-processing | First read slow and inconsistent between staff [WK-NOTICE-2026]; one commentator expects notice volume to rise while IRS capacity to resolve notices has fallen [ACCTODAY-2026] |
| Notice response | Choose agree, partial agree, disagree or penalty abatement; draft client explanation and agency letter; assemble support | document-production, expert-judgment | Drafted from scratch each time under short windows |
| Pre-filing exposure review | Reconcile to third-party forms (1099-K, 1099-DA, K-1); document positions | review-assurance | A correct return can still draw a notice if numbers do not visibly reconcile [TSCPA-2026] |
| Examination | Answer information document requests (IDRs, the examiner's formal record requests), interviews, proposed adjustments | coordination-scheduling, document-production | In e-invoicing (continuous transaction control) jurisdictions, authorities arrive with transaction data already analysed [TRINST-TEIAUDITOR-2026] |
| Appeals, Fast Track, ADR | Protest, settlement, mediation | expert-judgment, document-production | Appeals lost 29% of staff in 2025, per a law-firm commentary [CPAPA-APPEALS-2026]; no taxpayer-side AI evidence |
| Litigation | Research, briefs, motions, expert reports | research-synthesis, document-production | Hallucinated citations by taxpayer counsel and by the IRS [TAXCT-CLINCO-2026; BLAW-TAXCT-2026] |
| Collection and service | Payment plans, calls, chatbots, identity verification | client-interaction, transaction-processing | IRS assistor-answered calls down 20%, hold time 8 to 14 minutes in the 2026 filing season (FS2026) [NTA-OBJ-2026] |
| Practice governance | AI policy, engagement letters, billing, confidentiality, privilege | review-assurance | Fee and privilege rules unsettled [AICPA-CART-2026; MOFO-HEPPNER-2026] |

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path),
delegate (an agent owns a multi-step outcome), reinvent (the service or operating model changes). Practitioner-side
evidence covers improve only; automate and delegate exist only on the authority side, and delegate only as
announcements.

**Notices (practitioner side)**
- Improve: `#01` AI reads a notice and lists deadline, amount, issue and response paths (Wolters Kluwer, CoCounsel
  Tax; EY calls pilots early-stage). `#02` drafts client explanations and agency replies; the practitioner verifies
  every number and authority. `#03` weekly transcript monitoring for 700 clients catches the underreporter flag before
  the CP2000 arrives (one named practitioner, 2019).
- Delegate: no controversy-specific evidence. The nearest is Accrual's Arc agent demo, which includes notice intake
  and response letters; it sits in `tax-compliance-individual-business-09` [ACCRUAL-ARC-2026]. Indirect-tax notices: `tax-indirect-tax-14`.

**Pre-filing and documentation**
- Improve: `#04` review a return "as though it were a partner-level signer" for audit-sensitive items before sign-off
  (vendor feature, no outcomes; compliance overlaps `tax-compliance-corporate-13`, `tax-compliance-individual-business-12`).
  `#05` check TP documentation against public data (EY TP Doc Insights; see `tax-transfer-pricing-08` and `tax-transfer-pricing-16`). `#06` in-house teams summarise legislation and dispute files (EY survey: 39% built a
  controversy pilot or tool).
- Reinvent (idea): `#12` preventive controls and real-time data exchange replace after-the-fact audit defence
  (Deloitte scenarios; OECD real-time sharing pilots agreed Nov 2025 [OECD-FTA-2025]).

**Examination, Appeals and litigation**
- Improve: `#07` agents draft responses to audit queries and track IDRs (described by EY authors; no deployment;
  the TP version is `tax-transfer-pricing-16`).
  `#08` AI-assisted research and drafting for filings, with citation verification as the control (Clinco: 3 of 4
  cited cases apparently invented; tooling in `tax-research-advisory-19` and `tax-research-advisory-20`). `#09` idea: counsel-directed enterprise AI to protect privilege after *Heppner*.
- Authority side: `#22` Agentforce case summaries for Chief Counsel, Appeals and TAS (the Taxpayer Advocate Service) (announced, single source).
  `#23` Brazil groups similar appeal files for the same officers (over 80% sensitivity and specificity in early trials; a model accuracy measure, not a speed result).
  `#21` examiner and caseworker assistants (ATO orders substantiation documents; HMRC document scanning; IRS revenue
  agents reportedly draft IDRs).
- Delegate (announced): `#24` agentic case management (ATO's seven priorities, HMRC roadmap).

**Selection, notices and service (authority side)**
- Improve: `#13` IRS ML selection of returns and issues; TIGTA found no sufficient process to show it beats prior methods.
  `#15` risk targeting at HMRC (GBP 10 billion credited), Austria, Hungary and US states. `#19` ATO prompts taxpayers
  to check unusual entries before lodging. `#20` agent-assist tools for service staff (IRS Archie, CDTFA, HMRC).
- Automate: `#16` fraud and identity-theft screens that pause refunds. `#17` amended returns from 12-16 weeks to
  under three days (IRS CIO remark). `#18` voicebots and chatbots: only 17% of voicebot volume completed in the bot.
- Ideas: `#14` feedback, drift and disparity testing for selection models; `#25` LLMs that detect abusive strategies.

**Practice governance**
- Reinvent (idea): `#10` value-based pricing versus the fee guidance of OPR (the IRS Office of Professional Responsibility). Improve (idea): `#11` Werfel's risk register
  as pre-deployment due diligence.

## 4. Interview probes

1. Walk me through the last notice: who read it, in what system, how long to first client contact, and which part
   could a model summarise without a person re-reading it? *Reveals the real intake bottleneck and readiness for `#01`.*
2. Where have you caught a wrong deadline, amount or issue, by a person or a tool? *Reveals whether verification is
   designed in or assumed.*
3. Do you reconcile returns to third-party reporting (1099-K, 1099-DA, K-1) before filing or after the CP2000? *Shows
   whether `#03`/`#04` would move work upstream.*
4. Where does AI-generated text or a cited authority enter anything sent to the IRS, Appeals or a court, who checks
   each citation, and is the check logged? *Tests exposure to Clinco-type failures; see `#08`.*
5. Do you check that a real case actually supports the proposition, not just that it exists? *Zzaman shows existence
   checks are not enough.*
6. What does your engagement letter say about AI on client data, and how do you price notice and exam work as
   drafting time falls? *Reveals §7216 consent (client permission to use return data), OPR fee exposure and readiness for `#10`.*
7. Who owns AI in your tax function (tax, IT, legal)? *In a TEI room poll, two of more than 50 hands said tax does
   [TEI-TAXTECH-2026]; no owner usually means no verification standard.*
8. Since 2025, where has resolution slowed (power-of-attorney processing, exam assignment, Appeals, collection), and what changed in
   client expectations or staffing? *Measures the capacity gap that commentators describe.*
9. Do clients use consumer AI on their own matters, and do you tell them about privilege? *Heppner risk; `#09`.*
10. If an authority used AI against your client, what record would you request, and what have you been given?
    *Shows how the firm handles opaque selection; links to `#13`-`#15`.*
11. What data would show whether AI shortens your notice cycle or reduces re-work, and do you collect it today?
    *Most firms cannot answer; this is the measurement gap.*

## 5. Metrics and benchmarks

| Metric | Figure | Provenance | Source |
|---|---|---|---|
| IRS active AI use cases | 126 (Jun 2025), up from 10 (Aug 2022); 65 withheld; 61% in development; over 25% lacked benefit information | independent | [GAO-2026] |
| Other IRS counts (not comparable) | 61 in Treasury public inventory (Jan 2026); 225 as of Dec 2025 per TIGTA via press | independent / press | [TREAS-AIINV-2026; ACCTODAY-TIGTA-2026] |
| High-impact AI documentation | 4 of 5 sampled lacked testing documentation; 2 of 5 lacked an impact assessment | independent (via press) | [ACCTODAY-TIGTA-2026] |
| IRS selection pilot (Form 1040) | Higher assessment per exam hour and higher no-change rate; figures redacted | independent | [TIGTA-2025] |
| No-change rate, audited filers under $50,000 | FY2025 almost half FY2024; no-response up more than 10 points; not attributed to AI | independent | [NTA-AR-2025] |
| IRS voicebots (FS2026) | 17% completed in bot; about 46% transferred; about 14% disconnected | independent | [NTA-OBJ-2026] |
| IRS chatbot usefulness | 80% negative (Jan-Aug 2025); international chatbot 11.5% helpful | independent | [NTA-AR-2025] |
| IRS amended returns | 12-16 weeks to under three days for "hundreds of thousands" of about 5 million | self-reported, spoken | [IRS-AIFIRST-2026] |
| HMRC | GBP 10 billion protected and recovered with AI and analytics (2025-26); method not published | self-reported | [HMRC-ARA-2026] |
| ATO filing prompts | More than 636,000 prompts; about AUD 78.9 million protected (2023-24) | self-reported via OECD | [OECD-GOVAI-2025] |
| ATO AI governance | 74% of production models without a completed data ethics assessment | independent | [ANAO-ATO-2025] |
| Austria risk models | About EUR 185 million additional revenue from about 6.5 million cases (2023) | self-reported via OECD | [OECD-GOVAI-2025] |
| Brazil appeal-file classification | Over 80% sensitivity and specificity on 2,000 labelled files | self-reported via OECD | [OECD-GOVAI-2025] |
| VAT investigations | Some administrations cut them from about nine months to three (OECD speaker, second-hand) | press report | [SSL-OECDVAT-2026] |
| Authority adoption | 70% of 54 FTA members use AI tools (2024 data); 22 of 36 responding US state agencies said they used no AI | independent | [OECD-DIGIT-2025; TAXNOTES-UNWATCHED-2026] |
| Practitioner adoption | 39% built a controversy pilot or tool; 46% vs 31% "very satisfied" (GenAI users vs not) | vendor-published survey | [EY-TAXRISK-2025] |
| Tax Court | Over three-quarters of cases pro se; fewer than a dozen hallucination instances seen by one judge | independent | [BLAW-TAXCT-2026] |
| Hallucination decisions | About 2,200 worldwide, 25 tagged tax | independent database | [CHARLOTIN-DB-2026] |
| Audit-rate disparity | Black taxpayers audited at 2.9 to 4.7 times the rate of others (older data) | independent | [SIEPR-AUDIT-2023] |

No independent benchmark exists for AI in notice response, audit defence or Appeals. No authority publishes an
override or error rate for its selection models.

## 6. Guardrails

**Practitioner rules ("existing duties apply")**
- IRS OPR Alert 2026-19 (Circular 230, the IRS rules for tax practitioners, and IRC §§6713 and 7216), AICPA SSTS §1.4
  (Statements on Standards for Tax Services), the Australian Tax Practitioners Board's TPB(GS) 55/2026 and the UK PCRT
  (Professional Conduct in Relation to Taxation) guidance are set out once in [the archetype guardrails](../guardrails.md). For controversy work:
  treat AI text as a draft and use only enterprise-approved tools for client data [IRS-OPR-2026]; the AICPA has asked
  for clarification on value pricing [AICPA-CART-2026].

**Courts and evidence**
- Tax Court: no AI rule; Rule 201(a) binds lawyers to the ABA Model Rules [TAXCT-CLINCO-2026]; IRC §6673 penalties up to
  $25,000. Judge Holmes doubts a blanket "no AI" certification makes sense [BLAW-TAXCT-2026].
- UK tribunals: the person who relies on AI bears responsibility (Elden); real cases cited for the wrong proposition
  also count (Zzaman) [ICAS-TAXTRIB-2026].
- IRS LB&I: AI can support but not replace judgment; experts must explain inputs, assumptions, methods and AI tools,
  and the IRS wants to see the formulas [IRS-LBI-TP-2026]. Proposed Federal Rule of Evidence 707 on machine-generated
  evidence was not recommended for action on 3-4 Jun 2026 [PROSKAUER-707-2026].
- Privilege: *Heppner* (S.D.N.Y., 17 Feb 2026) held a client's own consumer-AI reports were not privileged
  [MOFO-HEPPNER-2026].

**Authority governance**
- IRM 10.24.1 treats AI that influences audit selection as presumed high-impact: impact assessment, testing,
  monitoring, human oversight, consistent remedies or appeals; staff may not put taxpayer data into unapproved AI
  [IRM-10-24-1]. GAO made eight recommendations, all accepted [GAO-2026]; TIGTA recommended a performance-measurement
  plan [TIGTA-2025].
- ATO: adverse decisions are made by a human with a right of review [ATO-AI-2026]. HMRC lost a tribunal case for
  refusing to confirm or deny LLM use in R&D compliance [ELSBURY-ICO-2025].
- EU AI Act Recital 59: tax-authority administrative AI is not classed as high-risk law-enforcement AI, leaving no
  dedicated category [EU-AIACT-2024; HADWICK-EUAIACT].

**Steps that need human judgment:** choosing the position on a notice; signing anything sent to an authority or
court; verifying every authority, number and deadline; settlement and Appeals strategy; fee basis and AI disclosure;
on the authority side, every adverse decision and every selection override.

## 7. Roles and how they evolve

- Practitioners: from assembling information to review and judgment [BTAX-EYGRIP-2025]; responsibility stays with
  the signer, with supervisory review and citation logs added [TAXCT-CLINCO-2026; IRS-OPR-2026]. Commentary sees a
  shift toward documentation readiness and year-round risk advice, unmeasured [ACCTODAY-2026].
- In-house: talent is the top barrier (44%) [EY-TAXRISK-2025]; tax rarely owns AI [TEI-TAXTECH-2026]. One Tax Notes State author
  argues AI cannot hold culpability, so corporate tax teams will shrink less than predicted [SALA-TAXNOTES-2026].
- IRS: headcount flat at about 74,000; leadership says AI is "not designed to eliminate jobs" [IRS-AIFIRST-2026]. GAO
  found AI skills lost and no workforce plan [GAO-2026]. A Chief Counsel attorney: adopt or leave
  [IRS-AGENTFORCE-2025; quotation not re-checked, see `#22`]. Classifiers review and override model suggestions [TIGTA-2025].
- HMRC: broadly the same size in 2030 with AI assisting officials [CSW-HMRC-2026]; 5,500 more compliance officers
  [PINSENT-HMRC-2026]. Assistor-answered calls fell 20% while voicebot volume rose 4% [NTA-OBJ-2026].
- Werfel's register lists skill erosion (preparers) and expertise erosion (authorities) as risks [TAXADVISER-WERFEL-2026].

## 8. Frontier

| Date | Signal | Source |
|---|---|---|
| 2025-07-21 | HMRC roadmap names agentic AI for case management | [ICAS-HMRC-2025] |
| 2025-11 | OECD tax administrations agree to pilot real-time automated information sharing | [OECD-FTA-2025] |
| 2025-11-21 | Axios reports the IRS deploying Salesforce Agentforce in Chief Counsel, Appeals and TAS (EisnerAmper confirms the rollout) | [IRS-AGENTFORCE-2025; EISNER-IRSAI-2026] |
| 2025-12 | South Carolina signs a five-year AI audit-selection contract, starting with sales and use tax | [SCPOST-AUDIT-2026] |
| 2026-02-03 | CIAT author: authorities moving to agentic AI for end-to-end TP control (opinion) | [CIAT-BLOG-2026] |
| 2026-02-18 | EY India announces agents for research, compliance and litigation | [EY-INDIA-2026] |
| 2026-03 | Clinco and Khoja; Tax Court "feeling our way" on guardrails | [BLAW-TAXCT-2026] |
| 2026-04-22 | ATO CDO calls agentic AI "the next frontier" | [ATO-SPEECH-2026] |
| 2026-06-24 | OPR Alert 2026-19 | [IRS-OPR-2026] |
| 2026-07 | HMRC credits AI with GBP 10 billion; first Chief AI Officer appointed Apr 2026 | [HMRC-ARA-2026] |
| 2026-09-23 | AICPA launches the Council on AI Risk in Tax to test Werfel's framework | [AICPA-CART-2026] |
| 2026-09-28 | TIGTA finds documentation gaps in high-impact IRS AI | [ACCTODAY-TIGTA-2026] |
| 2026-10-02 | IRS CEO sets an "AI-first IRS" with a mid-90s compliance aim (about 85% now) | [IRS-AIFIRST-2026] |
| Fall 2026 | IRS responses to GAO's recommendations due | [GAO-2026] |
| 2026-12 | ATO enterprise-wide model-performance monitoring due | [ANAO-ATO-2025] |

Not yet moved: a Tax Court AI rule; Treasury minimum-practice guidance (none as of July 2026 per TIGTA
[ACCTODAY-TIGTA-2026]); any Circular 230 discipline for AI misuse.

## 9. Common objections

- **"AI makes up cases."** True, and courts have seen it on both sides (Clinco, Khoja, Elden, Riddle Aggregates).
  The response is a logged verification step: check each authority exists *and* supports the point
  [TAXCT-CLINCO-2026; ICAS-TAXTRIB-2026]. A training vendor's suggested workflow uses AI for structure and explanation, not citation [FINDSKILL-2026].
- **"Client data can't go into these tools."** Correct for consumer tools: OPR limits client data to
  enterprise-approved tools and cites §§6713 and 7216 [IRS-OPR-2026]; Australia expects client permission [TPB-GS55-2026].
- **"If AI saves time, we lose fees."** OPR says do not bill time not spent; the AICPA is contesting the value-pricing
  reading [IRS-OPR-2026; AICPA-CART-2026]. Treat pricing as an open design choice, not a reason to wait.
- **"The IRS's models are a black box, so why bother?"** Criteria are unpublished, but TIGTA, GAO and TAS publish what
  they find [TIGTA-2025; GAO-2026; NTA-AR-2025]. Reconciling to third-party data before filing is the practical counter
  [TSCPA-2026].
- **"Authority AI is biased."** There is evidence of disparity risk [SIEPR-AUDIT-2023; GAO-EQUITY-2024; STANFORD-AUDIT-2022]
  and weak state oversight [NTT-BIAS-2026]; IRM 10.24.1 lists consistent remedies or appeals among the
  minimum practices for high-impact AI [IRM-10-24-1].
- **"There's no proof it works for us."** Accurate: no practitioner-side measurement exists. Start with notice
  reading (`#01`), measure cycle time and re-work yourself, and keep the human signature.
- **"It fails silently."** The Thomson Reuters Institute's recap of a TEI seminar says AI now "fails quietly and even
  politely" [TEI-TAXTECH-2026]; design checks that do not depend on the tool reporting its own failure.

## 10. Sources

Full titles, URLs, dates and locators are in the YAML. Keys used here but not in the YAML:

- ACCRUAL-ARC-2026: Accrual launches Arc AI (Accounting Today, 2026-09-22), https://www.accountingtoday.com/news/accrual-launches-arc-ai-can-learn-from-and-replicate-accounting-workflows
- EU-AIACT-2024: Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act), Recital 59 (European Parliament and Council, 2024-06-13), https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
- HADWICK-EUAIACT: Slipping Through the Cracks (European Papers, 2024-12-30), https://www.europeanpapers.eu/e-journal/slipping-through-cracks-carve-outs-ai-tax-enforcement-systems-eu-ai-act
- OECD-DIGIT-2025: Tax Authorities Increasingly Use AI in Audits (Bloomberg Tax, 2025-06-17), https://news.bloombergtax.com/daily-tax-report/tax-authorities-increasingly-use-ai-in-audits-oecd-report-finds
- ATT-PCRTAI-2026: Professional bodies issue AI advice to members (Association of Taxation Technicians, for the PCRT bodies, 2026-01-19), https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members
- PROSKAUER-707-2026: Proposed FRE 707 (Proskauer Rose, 2026-07-29), https://www.proskauer.com/blog/machine-generated-evidence-challenges-the-federal-rules-inside-the-contested-proposed-federal-rule-of-evidence-707
- SALA-TAXNOTES-2026: AI Won't Shrink Corporate Tax Teams Much (Tax Notes State, abstract, 2026-07-20), https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/
- SSL-OECDVAT-2026: OECD: AI Is Cutting VAT Investigations from 9 Months to 3 (SharedServicesLink, 2026-06-29), https://sharedserviceslink.com/news/oecd-ai-is-cutting-vat-non-compliance-investigations-from-9-months-to-3
- TEI-TAXTECH-2026: 2026 TEI Tax Technology Seminar recap (Thomson Reuters Institute, 2026-05-04), https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain

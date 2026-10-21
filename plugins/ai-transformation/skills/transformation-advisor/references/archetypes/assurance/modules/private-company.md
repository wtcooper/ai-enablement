# Private-company assurance (assurance, mid-market)

Last reviewed 2026-10-21. Use cases live in `../use-cases/private-company.yaml` (20 entries: 9 B, 9 C, 2 D, none A).
`#05` means `assurance-private-company-05`; other modules' ids are in full. This module holds only what differs at
mid-market scale: the tools themselves (disclosure checklists, risk suggestions, evidence matching, Excel agents) sit in
planning-risk-assessment, substantive-testing, completion-reporting and quality-management, and single audits and
nonprofit work sit in nonprofit-government. Source keys in brackets are in the YAML or in §10.
**Evidence is thin on outcomes.** No firm in this module has published a measured AI result; every time or accuracy figure
is vendor-published or a firm quote or survey inside vendor material. Use it for risk awareness, probes and examples.

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

Audits of private, middle-market companies under AICPA auditing standards, plus preparation, compilation and review
engagements under SSARS (the AICPA's Statements on Standards for Accounting and Review Services), as delivered by
local, regional, top-100 and private-equity-backed firms. The binding constraints at this scale are client data
(QuickBooks-type systems, exports, PDFs), the firm's choice of methodology platform, and quality management tested by
peer review (the AICPA's triennial review of a firm's quality system and sample engagements), not model quality.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Choose methodology and platform | Pick an audit methodology and file (often bought: DAS on Caseware, Thomson Reuters Guided Assurance); AI now arrives inside it | expert-judgment, coordination-scheduling | Methodology, workpapers and AI come from one vendor (#01); an ENGAGE 2026 panel was built around how to choose [GRF-ENGAGE-2026] |
| Acceptance and engagement terms | Accept or continue the client, independence, engagement letter (see `assurance-acceptance-independence-10`, `-11`) | review-assurance, client-interaction | AI-related services to an attest client can raise independence concerns [JOFA-ETHAI-2026] |
| Planning and risk assessment | Understand the entity, assess risks, often from a prior-year file and trial balance | review-assurance, research-synthesis | Peer reviewers report weak risk-assessment documentation and weak links to procedures [NYSSCPA-PEERDEF-2026] |
| Client data intake | PBC ("prepared by client") list, trial balance, general ledger, bank statements | data-reporting, coordination-scheduling | 60% of 54 firms name poor client data and 53% lack of access as top blockers [CPACOM-ATR-2025]; clients refuse API access [CPAPA-ATLAB-2025] |
| Fieldwork | Tests of details, sampling, proof of cash, lease and debt recalculation | review-assurance, data-reporting | Long documents (board minutes, indentures, contracts); a small firm over-audited and found leaner samples hard to justify to peer reviewers [TR-SAMBROWN-2026] |
| Completion | Draft statements, disclosure checklist, tie-out, report | document-production, review-assurance | A completed disclosure checklist can run 1,200-1,500 requirements in one vendor's methodology [TR-DISCLOSURE-2026] |
| Review and sign-off | Manager and partner review; engagement quality review where required | review-assurance | For many small firms QM and peer-review effort can feel as if it rivals the time spent on the audit [JOFA-SMALLFIRM-2026] |
| Preparation, compilation, review (SSARS) | Import trial balance, draft statements and notes, analytical inquiries (reviews) | document-production, review-assurance | 43 of 295 reviews (15%) nonconforming across four states in 2025 reports (#17); no AI evidence found |
| Firm quality management and peer review | System of quality management (SQMS No. 1), annual evaluation, annual practice questionnaire, triennial review | review-assurance, coordination-scheduling | First QM peer reviews in 2026, called a test-and-learn year [AICPA-QMPEER-2026]; top system-review deficiencies are engagement performance and monitoring [TSCPA-PEERREVIEW-2025] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step, or redesign the flow with a person still on each item), automate (no person
on the normal path; exceptions to people), delegate (an agent owns a multi-step outcome), reinvent (the service or
business model changes). Kind of firm in brackets.

**Platform, methodology and firm set-up**
- Improve: `#01` one platform (DAS plus Caseware Verity) for audit, PCR and benefit plan work; adoption counts only
  (Withum, PKF O'Connor Davies: Top 25; EisnerAmper: Top 15-20, private-equity-backed; Citrin Cooperman: private
  middle-market focus). `#02` standardise workpapers and the knowledge base before AI, a project of more than a year
  (Citrin Cooperman). `#03` test platforms and agents on the firm's own files and re-test when the model changes
  (vendor advice; idea for most firms). `#04` own platforms that start with private-company audits (Grant Thornton
  gtap, national PE-backed; EisnerAI agent): announced. `#05` firm-built agents with overnight runs and reviewer agents
  (FGMK; PKF O'Connor Davies co-development).
- Improve (firm governance): `#06` named assurance technology leaders and AI-fluent audit managers (Citrin, EisnerAmper,
  Withum, BPM: Top 100; BW&O CPAs: local). `#07` written policy, approved tools, named owner, training before access
  (surveys only). `#08` transformation plan and baselines (75% of 54 firms have no formal plan).
- Not repeated here: writing AI into the SQMS risk assessment and annual evaluation, and governing staff-built agents
  (`assurance-quality-management-26`, `-27`); Oath as an AI-native firm (`assurance-quality-management-28`); vendor due diligence `assurance-quality-management-06`;
  vendor-contract independence review `assurance-acceptance-independence-13`.

**Client data and evidence intake**
- Improve: `#12` agent validates PBC submissions; source documents extracted into workpapers (Caseware early access
  and beta; Suralink). Vendors only.
- Automate: `#13` proof of cash from QuickBooks-type exports, templates and PDF bank statements; every bank and book
  transaction reconciled, people take the unreconciled items (Audit Sight; partner quote at Holbrook & Manter).

**Fieldwork and workpapers**
- Improve: `#09` general GenAI on low-risk drafting first (Beever and Struthers, UK mid-tier; independent study).
  `#10` research and document assistant (Plante Moran, large; Harris, Hardy & Johnstone, mid-sized). `#11` RSM Luca
  ecosystem for middle-market audits (national). `#15` assistant inside the Excel workpaper (Caseware; announced).
- Automate: `#14` risk-focused sample selection recorded as a workpaper to justify leaner samples to peer reviewers
  (Sam Brown CPA, small local firm; owner's estimate of at least five to six hours per audit).
- Elsewhere: Excel agents for clients reporting in a common format, and single-audit tests (`assurance-nonprofit-government-07`);
  firm-built Excel agents (`assurance-substantive-testing-11`); data cleaning to the trial balance (`assurance-substantive-testing-07`).

**Completion, review and peer review**
- Improve: `#16` gap flagging, cross-file checks and risk-to-procedure links aimed at peer-review findings (AICPA
  column and vendor claims; no named firm). Disclosure checklist agents: `assurance-completion-reporting-01`, `-03`.

**Preparation, compilation and review (SSARS)**
- Improve: `#17` PCR on the same AI-enabled platform as audits (Citrin, Withum, EisnerAmper); what AI does inside PCR is
  not described, so AI drafting there is still an idea.

**Pricing, risk and business model**
- Reinvent: `#18` decide and explain where savings go (margin, capacity, fees, value reporting); `#20` idea: start-ups
  selling continuous, AI-run audits against hours-based fees (machine-written podcast summary only).
- Improve: `#19` idea: check professional-liability cover for AI exclusions.
- Delegate: **no evidence** in this module beyond the `#20` idea. No firm describes an agent owning a multi-step
  private-company audit outcome; `#05` agents run in the background but people review every workpaper.

## 4. Interview probes

1. "Which audit file and methodology do your private-company engagements run in, who chose it, and did you test
   alternatives side by side?" Reveals platform lock-in, who decides, and whether `#01` or `#03` applies.
2. "How does client data reach you: ERP export, QuickBooks, spreadsheets, PDFs from the bank? On what share of audits
   do you rebuild data before testing?" Reveals whether data, not tooling, is the constraint (`#12`, `#13`).
3. "Who owns AI in the assurance practice by name, what do they report on, and how much of their time is it?"
   Reveals journey stage; no owner usually means Curious or Experimenting (`#06`).
4. "Which AI tools touched a client file last busy season, who approved them, and how do you know staff did not use
   others?" Reveals shadow use and whether a policy is real (`#07`).
5. "Where does AI appear in your system of quality management risk assessment, and what did first-year monitoring find?"
   Reveals QM readiness before the next peer review (`assurance-quality-management-26`).
6. "If a peer reviewer opened a file where AI helped, what would they see: tool, version, who reviewed, what it got
   wrong? What did your last reviewer ask about technology?" Reveals documentation gaps (`#16`; `assurance-quality-management-23`).
7. "For preparations, compilations and reviews, who drafts the statements and notes, does anyone use AI there, and how
   do you keep the no-assurance and independence lines clear?" Reveals untested SSARS use (`#17`).
8. "If your vendor's agent gave a wrong checklist answer or missed a risk, how would you find out? Have you scored it
   against answers you already know?" Reveals reliance on vendor claims (`#03`).
9. "What baseline do you have: hours per checklist or selection, review notes per file, nonconformity history?"
   Reveals whether any value case can be made (`#08`).
10. "If hours per audit fell, what happens to price, staffing and the junior pipeline? What have clients or audit
    committees asked about AI and fees?" Reveals the fee and workforce choice (`#18`).
11. "What do your engagement letters and your liability policy say about AI?" Reveals consent and cover gaps (`#19`;
    `assurance-quality-management-24`).

## 5. Metrics and benchmarks

**Independent quality baseline (not AI measures).** State peer-review annual reports for reviews accepted in 2025;
nonconforming engagements over engagements reviewed. Samples are small and rates are not comparable across states.

| Engagement type | Tennessee | Connecticut | Minnesota and ND | Missouri | Four-state sum |
|---|---|---|---|---|---|
| Single audit | 2 of 11 | 3 of 9 | 3 of 15 | 8 of 22 | 16 of 57 (28%) |
| Other audits under SAS | 8 of 53 | 3 of 39 | 6 of 78 | 6 of 60 | 23 of 230 (10%) |
| Reviews | 13 of 99 | 5 of 63 | 14 of 75 | 11 of 58 | 43 of 295 (15%) |
| Compilations (and preparations) with disclosures | 2 of 44 | 4 of 47 | 5 of 51 | 1 of 20 | 12 of 162 (7%) |
| Compilations (and preparations) omitting disclosures | 5 of 175 | 2 of 67 | 4 of 138 | 3 of 102 | 14 of 482 (3%) |
| All types | 34 of 448 | 18 of 256 | 38 of 418 | 45 of 363 | 135 of 1,485 (9%) |

[TSCPA-PEERREVIEW-2025; CTCPA-PEERREVIEW-2025; MNCPA-PEERREVIEW-2025; MOCPA-PEERREVIEW-2025]; sums are
arithmetic across the four tables. Missouri's compilation cells exclude preparations (2 of 18 omitting disclosures nonconforming); the
other three states report compilations and preparations together. The Oklahoma, South Dakota and Kansas entity reported 86 of 525 (16.38%), including 12 of 40 single
audits [OKSCPA-PEERREVIEW-2025]. System reviews passed: Tennessee 40 of 46, Connecticut 28 of 34, Minnesota 41 of 44,
Missouri 23 of 31, Oregon 32 of 36, Oklahoma group 35 of 55 [same reports; OSCPA-PR-2026]. None of these reports
mentions AI. For plan audits, the EBSA found 30% of sampled audits (2020 form year) had major deficiencies and that peer
review did not help identify them [EBSA-AUDITQ-2023] (detail in benefit-plan work).

**Adoption and practice (surveys).**
- 54 US firms, not representative: 75% no formal transformation plan; nearly a quarter use no AI or advanced
  automation; 89% use no technology for substantive analytics; 83% name staff efficiency as a top-two ROI outcome,
  54% quality, 6% do not measure [CPACOM-ATR-2025].
- Written AI policy: 57% of 162 firms (CPAFMA, via a blog) against 21% (Karbon, vendor survey); samples differ
  [CPAFMA-WINSOME-2026; KARBON-AI-2026]. More than one in three professionals admit unauthorised AI use [TRI-FOP-2026].
- Firm size: 63% of large tax and accounting firms (30+ professionals) versus 35% of small ones (1-3) proactive or
  optimised in technology [TR-SOTP-2026]. Technology and AI change management ranks first for five-year impact in all
  six size groups of the AICPA top-issues survey (629 respondents) [AICPA-TOPISSUES-2026; JOFA-TOPISSUES-2026].
- UK mid-tier: 86% of 35 firms have a technology strategy that includes AI [ICAEW-MIDTIER-2026]. At Beever and
  Struthers, 74% of staff said some tasks were faster but 22% saw a marked rise in output (`#09`) [ICAS-AMBS-2025].

**Tool figures (vendor-published; no sample sizes).**
- Caseware: disclosure checklist agent 2.7 review hours saved per run on average, varying by engagement
  [CASEWARE-VERITY-2026]; 94% accuracy on golden-dataset items from beta traces [CASEWARE-LAUNCH-2026]; Verity for Excel
  nine hours per engagement and 75% per task in its own testing [CASEWARE-VERITYXL-2026].
- Thomson Reuters: 91% of 140+ Plante Moran pilot respondents said research was faster [TR-SCALING-2026]; Disclosure
  Review used by roughly 30% of eligible customers, close to 300 analyses a month [TR-DISCLOSURE-2026].
- CPA.com says LLM-based research tools in audit and advisory are helping cut document analysis time by 50% or more;
  no firm, sample or measurement is named [CPACOM-AIACC-2025].

**What to measure.** Hours per checklist, selection and review round; review notes per file; overrides of AI answers;
peer-review and monitoring findings; realisation and margin per engagement (28% of firms track margin per engagement)
[CPACOM-ATR-2025]. **Not found anywhere:** an error rate, override rate, parallel-run result or peer-review outcome for
AI in a private-company audit, review or compilation. The one independent link between AI investment and audit quality
concerns the 36 largest firms before generative AI [FEDYK-2022] (see `assurance-quality-management-07`).

## 6. Guardrails

- **No AI standard.** The AICPA practice aid *AI Considerations for Financial Statement Auditors* (13 Oct 2026) is
  nonauthoritative; part 1 covers the client's AI in reporting and controls, part 2 the firm's own use (QM policies,
  team competence, planning AI use, supervision, review, and the engagement partner's duty to understand the tools and
  confirm they are firm-approved and used correctly); risk-assessment and
  evidence content is to follow [AICPA-PA-2026; AICPA-AIPAID-2026; JOFA-AIPA-2026]. No Auditing Standards Board AI
  standard and no ARSC guidance for SSARS work was found.
- **Quality management is the binding channel.** Firms had to have an SQMS No. 1 system by 15 Dec 2025, with the
  annual evaluation within a year [CPACOM-SQMS-2026]. Peer reviewers now look for tailored quality risks and interview
  leadership on monitoring [AICPA-QMPEER-2026]. All enrolled firms answer an annual practice questionnaire from June
  2026; the AICPA's 2026 peer review update lists AI and automation among emerging areas [AICPA-APQ-2026;
  ICPAS-PRAF-2026]. Yellow Book (government auditing standards) users evaluate their system by 15 Dec 2026
  [GAO-YBFAQ-2025].
- **Documentation.** The Texas State Board (Aug 2026) says existing rules apply, AI analyses are not audit evidence and
  do not replace required procedures, names audits, reviews and compilations, and suggests recording how AI was used
  and validated without logging every interaction [TSBPA-2026]. One state board only. A CalCPA author reads AU-C 230 as
  requiring working papers that let an experienced auditor understand AI procedures and judgments [CALCPA-AISTD-2026].
- **Client data and consent.** The Confidential Client Information Rule (ET 1.700.001) applies before client data goes
  into an AI system, and consent may be needed [JOFA-ETHAI-2026]. Read licence terms: with a free tool "you are the
  product" [JOFA-AAFOCUS-2025]. The practice aid's Q&A says AICPA standards do not require disclosing AI use to the
  client, but law, contract or firm policy may [CFODIVE-AICPAPA-2026] (`assurance-quality-management-24`).
- **Independence.** Building or hosting an AI system for an attest client can raise independence concerns
  [JOFA-ETHAI-2026]. Tool-provider terms can shift control or evidence access [JOFA-SOCETH-2026]. PEEC is discussing
  a second exposure draft on alternative practice structures, including a ban on attest-client investment in firms
  [JOFA-PEEC-2026]. Several tools produce client-side schedules (lease schedules, journal entries); the sources do not
  discuss independence, so ask.
- **SSARS 27** takes statements prepared within a consulting engagement out of AR-C 70 for periods ending on or after
  15 Dec 2026; it does not mention AI [CPACOM-SSARS27-2025].
- **Steps that need human judgment:** accepting or overriding every AI suggestion and client submission; risk
  conclusions; concluding on unreconciled items and exceptions; sample design and approval; signing the opinion or the
  compilation or review report; pricing; the annual QM evaluation; deciding whether a client's data may go into a tool.

## 7. Roles and how they evolve

- **New owners.** Named assurance innovation or technology leaders at Citrin Cooperman, EisnerAmper and Withum; BPM
  advertised an Audit AI Technology Director with KPIs and vendor budgets; BW&O CPAs an audit manager to refine work with
  AI agents (`#06`). About a third of 54 firms say they need at least one non-traditional skill and about 20% have hired staff with
  non-traditional backgrounds [CPACOM-ATR-2025].
- **Managing partner as QM owner.** The CEO or managing partner owns the QM system, evaluates it yearly and is interviewed
  by peer reviewers on it [AICPA-QMPEER-2026] (the article does not mention AI); engagement partners confirm tools are
  approved and used correctly [AICPA-PA-2026].
  At Citrin Cooperman firm-level AI governance sits with the Risk Management Officer and domain policies with practice
  leaders (vendor blog) [CASEWARE-READINESS-2026].
- **Juniors.** Firms say cited AI output teaches juniors: a Withum partner likened Verity to a partner walking a junior
  through a checklist line by line [CASEWARE-VERITY-2026]. Accountancy Europe names junior development as a risk
  [ACCTEU-GENAI-2026], and a trade-press opinion piece says AI is absorbing the chasing, rekeying and reconciling that
  taught the first two years, and most firms have yet to replace that learning with a deliberate model [CPAPA-STOP-2026]. Neither side has measured it.
- **Capacity.** The AICPA small-firm column suggests contractors (often retired practitioners) and shared resources,
  and says some firms should consider leaving audit work [JOFA-SMALLFIRM-2026]. A Thomson Reuters executive says 75% of
  audit partners are scheduled to retire within ten years (vendor interview) [TR-STATE-2026]. Bennett Thrasher says it
  uses AI to move professionals from lower-level compliance work to consultative roles earlier [ATODAY-TOP100-2026].
- **Reviewers.** Caseware pitches cross-file checks and review packs to managers (`#16`); FGMK runs reviewer agents as a
  second pass (`#05`). No firm has described how reviewers' work changed; treat it as a hypothesis.

## 8. Frontier

- **2026-12-15:** SSARS 27 effective [CPACOM-SSARS27-2025]; first Yellow Book QM evaluations due [GAO-YBFAQ-2025].
- **2026-10-19:** AICPA and AIUC announce one CPA-led engagement combining SOC 2 and AIUC-1 for AI systems, full launch
  expected early 2027 [JOFA-AIUC-2026]; a possible service line for firms with SOC practices, though the article names no
  firms or firm sizes (soc-attestation, assurance-over-ai).
- **2026-10-13:** AICPA practice aid issued, with risk-assessment and evidence content and more Q&As to come [AICPA-PA-2026].
- **2026-10-08:** PKF O'Connor Davies joins Caseware's Agentic Pioneer Program to build its own agents (`#05`) [CASEWARE-PKF-2026].
- **2026-10-06:** Caseware Risk Suggestion Agent launched worldwide at no extra cost, with a GRF partner quoted [CASEWARE-RSA-2026]
  (`assurance-planning-risk-assessment-09`).
- **2026-09-23:** Thomson Reuters Disclosure Review launched for Guided Assurance customers with the Disclosure module;
  it plans to extend into 'no' and 'not applicable' determinations [TR-DISCLOSURE-2026] (`assurance-completion-reporting-04`).
- **2026-09-21:** Accountancy Europe paper for small and medium practices says higher autonomy needs more governance [ACCTEU-GENAI-2026].
- **2026-09-09:** Verity for Excel generally available; Client Requests and Response Validation Agent in early access
  (`#12`, `#15`) [CASEWARE-VERITYXL-2026].
- **2026-08:** Texas State Board statement on AI in attest work [TSBPA-2026]; PEEC continues APS discussions [JOFA-PEEC-2026].
- **2026-06 to 2026-07:** annual practice questionnaire launches [AICPA-APQ-2026]; first QM peer reviews under way [AICPA-QMPEER-2026];
  Withum (3 Jun), EisnerAmper (25 Jun) and Citrin Cooperman (13 Jul) announce DAS adoption (`#01`).
- **2026-05-20:** Caseware Verity launch with a stated goal of automating 50% of the engagement workflow; a roadmap, not
  a result [CASEWARE-LAUNCH-2026].
- **2026-05-07:** Grant Thornton gtap goes to private-company audits first, public-company audits the next year (`#04`) [GT-GTAP-2026].
- **2026-03-09 and 2026-01-08:** EisnerAI Audit Design Agent announced [EISNER-AUDITAGENT-2026]; RSM Ask Luca, described
  as a base for future agents [RSM-ASKLUCA-2026].
- **Direction:** private-company audits are becoming the proving ground for firm platforms; agents arrive inside the
  audit file small firms already use; peer review of QM systems is where AI governance will first be tested.

## 9. Common objections

- **"The practice aid is nonauthoritative, so we can wait."** True, but peer reviewers test whether the QM system works
  and the AICPA says leaders should expect questions on monitoring [AICPA-AIPAID-2026; AICPA-QMPEER-2026].
- **"We are too small for AI."** A small Ohio firm credits a sampling tool with at least five to six hours per audit (an
  estimate) and peer-review defensibility (`#14`); the AICPA column lists technology among ways small firms keep audit
  work viable [JOFA-SMALLFIRM-2026]. Start with low-risk drafting (`#09`).
- **"Our clients' data is too messy."** It is the top blocker [CPACOM-ATR-2025]. Tools that take exports, templates and
  PDF bank statements exist (`#13`), but the evidence is a podcast and a partner quote.
- **"The vendor has governed it."** Governance claims are vendor-published [CASEWARE-LAUNCH-2026], and the AICPA has
  warned that some firms lean too heavily on third-party SOC platforms without applying the judgment standards require
  [JOFA-PEER-2026]; that warning was about SOC 2 work, but the point carries. Test on your own files (`#03`).
- **"It will get things wrong."** 72% of staff at a UK mid-tier firm feared incorrect output [ICAS-AMBS-2025]. Every tool
  here keeps a person reviewing the output or its exceptions; no error rate is published either way, so measure your own.
- **"Clients will demand fee cuts."** CFOs ask where savings go and are split on whether auditor AI improved quality;
  one FERF respondent reported 25-30% cuts after a competitive review [FEIDAILY-FERF-2026]. No mid-market case tied to
  AI was found. Prepare the answer with data (`#18`).
- **"Time saved is not real."** In the one study, 74% of staff said some tasks were faster but only 22% reported a
  marked rise in overall output [ICAS-AMBS-2025]. Baseline before rollout (`#08`).
- **"Staff will use it anyway."** More than one in three already use unauthorised tools [TRI-FOP-2026]; approved tools
  plus training is the response (`#07`).
- **"Juniors will not learn."** Firms say cited output teaches; others warn it removes the work that taught. Neither is
  measured; design supervision deliberately (`assurance-quality-management-25`).

## 10. Sources

Full details for every key used in the use cases are in `../use-cases/private-company.yaml`. Keys cited only here:

- AICPA-QMPEER-2026: AICPA & CIMA Insights, *Peer reviews of QM systems: What firms need to know now* (2026-06-25). https://www.aicpa-cima.com/professional-insights/article/peer-reviews-of-qm-systems-what-firms-need-to-know-now
- AICPA-APQ-2026: AICPA & CIMA, *Annual Practice Questionnaire for Peer Review FAQs* (2026-06-30; launch week of 1 June 2026). https://www.aicpa-cima.com/resources/article/annual-practice-questionnaire-for-peer-review-faqs
- CPACOM-SQMS-2026: CPA.com, *Waiting for peer review cycles puts firms at risk under SQMS 1* (2026-09-03). https://www.cpa.com/blog/2026/09/03/waiting-peer-review-cycles-puts-firms-risk-under-sqms-1
- ICPAS-PRAF-2026: Illinois CPA Society, *Peer Review Alliance Forum 2026, participant slides* (catalogue description, 2026). https://learn.icpas.org/AssetListing/Peer-Review-Alliance-Forum-Virtual-17790/2026-Forum-%E2%80%93-Participant-Slides-29361
- AICPA-AIPAID-2026: AICPA & CIMA, *Explore new AICPA guidance on AI and the financial statement audit* (2026-10-12). https://www.aicpa-cima.com/resources/article/explore-new-aicpa-guidance-on-artificial-intelligence-ai-and-the-financial-statement-audit
- JOFA-AIPA-2026: Journal of Accountancy, *AI and the audit: AICPA publishes practice aid to assist auditors* (2026-10-13). https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/
- CFODIVE-AICPAPA-2026: CFO Dive, *AICPA issues guidance for AI-assisted auditing* (2026-10-13). https://www.cfodive.com/news/aicpa-issues-guidance-ai-assisted-auditing/832907/
- TSBPA-2026: Texas State Board of Public Accountancy, *Board Report*, vol. 168 (2026-08). https://www.tsbpa.texas.gov/wp-content/uploads/2026/08/br_082026_web_final.pdf
- GAO-YBFAQ-2025: GAO-26-108710, *Government Auditing Standards FAQ on a system of quality management* (2025-12-15). https://files.gao.gov/reports/GAO-26-108710/index.html
- JOFA-PEEC-2026: Journal of Accountancy, *PEEC to continue discussions on alternative practice structures* (2026-08-10). https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures/
- JOFA-AIUC-2026: Journal of Accountancy, *AICPA partners on new offering that assures AI systems and agents* (2026-10-19). https://www.journalofaccountancy.com/news/2026/oct/aicpa-partners-on-new-offering-that-assures-ai-systems-and-agents/
- TR-DISCLOSURE-2026: Thomson Reuters, *Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence* (vendor, 2026-09-23). https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/
- CASEWARE-READINESS-2026: Caseware blog, *The AI Readiness Gap* (vendor, 2026-09-03). https://www.caseware.com/resources/blog/the-ai-readiness-gap-why-audit-and-accounting-leaders-arent-seeing-the-value-they-expect
- CPAPA-STOP-2026: CPA Practice Advisor, *Stop Training CPAs for Yesterday's Work* (opinion, 2026-09-02). https://www.cpapracticeadvisor.com/2026/09/02/stop-training-cpas-for-yesterdays-work/189548/
- AICPA-TOPISSUES-2026: CPA Practice Advisor on the AICPA PCPS Top Issues Survey (2026-06-23). https://www.cpapracticeadvisor.com/2026/06/23/aicpa-survey-cites-change-management-for-technology-and-ai-as-top-long-term-issue-facing-accounting-firms/185547/
- JOFA-TOPISSUES-2026: Journal of Accountancy, *AICPA Top Issues Survey: Firms' focus on technology rises* (2026-06-23). https://www.journalofaccountancy.com/news/2026/jun/aicpa-top-issues-survey-firms-focus-on-technology-rises/
- ICAEW-MIDTIER-2026: ICAEW, *Mid-tier firms focused on AI and consolidation* (2026-05-22). https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/mid-tier-firms-focused-on-ai-and-consolidation
- CPACOM-AIACC-2025: CPA.com, *2025 AI in Accounting Report* (2025-06). https://www.cpa.com/sites/cpa/files/2025-06/2025_AI_in_Accounting_Report.pdf
- ATODAY-TOP100-2026: Accounting Today, *Top 100 Firms* print PDF (2026-03). https://arizent.brightspotcdn.com/68/01/115c3908493183df05d3879ed2e5/act0326-top100.pdf
- FEDYK-2022: Fedyk et al., *Is artificial intelligence improving the audit process?*, Review of Accounting Studies (2022). https://ideas.repec.org/a/spr/reaccs/v27y2022i3d10.1007_s11142-022-09697-x.html

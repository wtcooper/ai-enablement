# Work production (professional services)

Sources checked 2026-10-19. Use cases live in `../use-cases/work-production.yaml` (25 entries: A 2, B 16,
C 5, D 2). Ids are shortened here: `#08` means `professional-services-work-production-08`; other archetypes' ids
are in full. Source keys in brackets are in the YAML or in §10. The named public record is almost all legal (law
firms and in-house legal teams); consulting and accounting firms publish little. Most outcome figures are
vendor-published or self-reported, and no firm publishes an error, override or parallel-run rate for AI-assisted
work. Say so when you quote a figure.

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

The substantive work a firm or in-house team produces for a client: research and synthesis, extraction from
document sets, first drafts, review against a playbook (the written list of preferred and fallback positions) or
standard, and the checks before anything is released. It is the shared layer only. Audit procedures, tax technical
work and security operations live in the assurance, tax and security archetypes; overlaps are named by id below.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Brief and set up | Load documents or precedent into a controlled workspace; pick the playbook, template or workflow | coordination-scheduling, document-production | Each matter rebuilt from a checklist, a prior deal or memory [HARVEY-ORCH-2026] |
| Research | Find and synthesise authority or evidence | research-synthesis | Tools invent or misstate sources; multi-jurisdiction questions are weak [STANFORD-MAGESH-2024; VALS-VLAIRRES-2025] |
| Synthesis of records | Summaries, chronologies, transcript analysis, first-pass translation | research-synthesis | Orientation eats early matter time; language skills scarce [LEGORA-GRANTTHORNTON-2026] |
| Extraction | Clauses and fields to tables; question answering over a document set | data-reporting | Manual abstracting; multi-clause questions answered incompletely [VALS-VLAIRFEB-2025] |
| First draft | Clause, memo, brief, agreement, report or deck from precedent and standards | document-production | Repeats past work; quality depends on who drafts [LEGALIT-BMW-2026] |
| Review against a standard | Playbook review and redlining (marking up the other side's draft); consistency checks | review-assurance | Slow, repetitive, uneven between reviewers; lawyers still beat tools on open-ended redlining [VALS-VLAIRFEB-2025] |
| Verify and release | Check citations, quotes and figures; supervisor sign-off; client disclosure where required | review-assurance, expert-judgment | Fluent output is wrong in ways that look right; 2,202 court decisions on hallucinated content [CHARLOTIN-DB-2026] |
| Tool approval and re-test | Policy, approved tools, training, evaluation when models change | review-assurance | Coverage varies by firm size; vendor claims hard to test [ILTA-TECHSURVEY-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome with checkpoints), reinvent (`change_scope: model`, or a process that stops existing).
**Coverage:** assist 6, augment 14, automate 1, delegate 4; step 13, process 11, model 1. All four delegate
entries are announcements or benchmarks (grade C). Automate has one firm example, from March 2025 (`#13`). Reinvent
has one entry, a set of plans and announcements (`#21`); no firm reports a step that has stopped existing.

**Research and synthesis**
- Improve: `#01` cited research, checked against sources (Deutsche Telekom in-house, Gleiss Lutz law firm). AI
  scored 74-78% against 69% for lawyers in one benchmark; the largest research platforms were not tested. Tax
  equivalent: tax-research-advisory-01.
- Improve: `#02` summaries, chronologies, transcript analysis and first-pass translation (Grant Thornton UK
  forensic, accounting firm). Tools beat the lawyer baseline on summarisation; chronology at best matched it.
- Improve: `#04` regulatory horizon scanning (Hogan Lovells Cadwalader, BMW Group; announced). Tax:
  tax-research-advisory-23.

**Extraction**
- Improve: `#03` clause and field extraction and cited Q&A (Goodwin, CMS, A&O Shearman law firms; Dentsu
  in-house). Q&A was the tools' strongest task; extraction was close to the lawyer baseline.
- Automate: `#13` PwC's task agents extract from PDFs and spreadsheets, map to target formats and validate (Big
  Four, 250 agents reported March 2025). Tax: tax-data-technology-11.

**Drafting**
- Improve: `#05` first drafts from approved precedent (Goodwin, Gleiss Lutz; BMW in-house, announced; Microsoft,
  OpenAI, Litera products). No firm publishes draft error rates.
- Improve: `#06` randomised trial, 133 patent lawyers: drafts better with AI, but the durable unaided-skill gain
  went to seniors. `#07` consulting analysis and deliverables (BCG experiment; Deloitte Australia): faster inside
  AI's capability, worse outside it, so set task-by-task rules. Related: assurance-completion-reporting-13,
  tax-transfer-pricing-07, security-incident-response-14.

**Review against a standard**
- Improve: `#08` playbook review with tracked-change suggestions in Word (Microsoft in-house, GE Aerospace
  in-house): users kept about 70% of suggestions (vendor telemetry). The 2026 contract-review benchmarks are vendor-run; lawyers led
  the one independent redlining test (2025).
- Improve: `#09` AI as a sparring partner on a draft (O'Melveny, Bracewell law firms). `#10` idea: a human
  challenger role so teams can defend AI-structured work without AI.

**Verification and release**
- Improve: `#11` pre-release check of citations, references and internal consistency (Grant Thornton UK; Deloitte
  Australia and Canada incidents; ICMCI code). Tax: tax-research-advisory-19, -20; assurance-quality-management-19.
- Improve: `#25` record AI use, disclose material use, and apply each client's AI terms at matter opening (Public
  Services and Procurement Canada as a client rule).

**Whole matters and multi-step work**
- Improve, process scope: `#12` diligence over whole data rooms (O'Melveny, CMS, PwC with client IFS); `#20`
  shared AI workspaces with clients and co-counsel (O'Melveny, Dentsu, Deutsche Telekom with Gleiss Lutz).
  Related: tax-research-advisory-21, assurance-substantive-testing-14.
- Delegate: `#14` an agent reads a whole data room and writes the memo (Harvey benchmark only; tax:
  tax-research-advisory-22); `#15` matter templates with agent tasks and a named reviewer at each gate (Harvey,
  announced 2026-10-15); `#16` general-purpose agent workspaces from Anthropic, Google, OpenAI and Microsoft, with
  checkpoints sized to risk and access limited by matter (announced; the Law Society reports very limited
  autonomous use).

**Operating model and governance**
- Improve, process scope: `#17` legal engineers (lawyers who turn legal work into tool workflows) and practice
  teams build playbooks, vaults (secure document collections a tool can query) and custom agents (Hogan Lovells
  Cadwalader, Blank Rome, MinterEllison, Reed Smith, Duane Morris). `#18` in-house lawyers build workflow agents
  for data protection impact assessments (Dentsu; compare security-data-privacy-15). `#19` in-house AI-first
  defaults and keeping work in-house (TC Energy, GE Aerospace, Dentsu, BMW, JLL).
- Improve, process scope: `#22` gated rollout (policy, approved tools, training before access, human-review rule);
  `#23` test tools on the firm's own work against an expert baseline and re-test (Vals law-firm consortium,
  Covington & Burling); `#24` idea: log edits, overrides and review findings.
- Reinvent: `#21` firm expertise packaged as agents and offered to others (A&O Shearman with Harvey; Fried Frank
  considering; Kirkland emphasising exclusivity). Plans only. Subscription services without a professional in
  the loop (PwC One) sit in scoping-pricing; tax: tax-research-advisory-24.

## 4. Interview probes

1. **"Which first-draft, extraction or playbook-review tasks do people already do with AI, and what is the written
   rule for who checks the output?"** Reveals real adoption against licences; ILTA shows review rules range from
   31% to 83% of firms by size (`#22`).
2. **"Which document types and playbooks do you use most, and which are written down well enough for a tool to
   apply?"** Reveals readiness for `#05` and `#08`; a playbook in people's heads cannot be applied.
3. **"Do you measure AI-assisted work (edits kept, errors caught in review, rework, time to first draft) against a
   pre-AI baseline, or rely on anecdotes?"** Reveals whether any quality evidence exists; none is public (`#24`).
4. **"Where does verification sit for citations, quotes and extracted figures, who owns it, and what did it last
   catch?"** Reveals whether `#11` is a real gate or a habit; courts now ask leaders what measures exist.
5. **"Before you relied on a tool, did you test it on your own matters against a lawyer or expert result? When did
   you last re-test?"** Reveals `#23`; the ABA allows sample-testing, and California expects re-assessment.
6. **"Which tasks have you decided stay human-first, and on what evidence?"** Reveals whether the team knows where
   AI hurts (`#07`: 19% less likely correct outside its capability).
7. **"Who builds and maintains your playbooks, templates and agents, and are they released from fee-earning work to
   do it?"** Reveals capacity for `#17`; MinterEllison relieved accelerator staff of billable work.
8. **"When a client asks what AI saved on their matter, what do you show them, and how do client AI terms reach
   the people doing the work?"** Reveals `#25` and the proof gap; firms say they are still gathering data.
9. **"Where does early-career work come from now that drafts, summaries and first-pass review come from tools?"**
   Reveals junior-skill risk (`#06`; juniors' unaided scores split); route detail to talent-learning.
10. **"Do any multi-step agents act without a person at each step? What can they reach and send?"** Reveals
    readiness for `#15`-`#16` and confidentiality exposure across matters.
11. **"In-house: what work have you stopped sending to outside counsel, and did your firms' AI use lower your
    bills?"** Reveals `#19`; in one vendor-commissioned survey only one in-house team reported savings.
12. **"Consulting and accounting: which deliverables include AI-drafted content, and who checks every reference
    before release?"** Reveals exposure to a Deloitte-type incident (`#07`, `#11`).

## 5. Metrics and benchmarks

**Independent task benchmarks (tools tested in isolation, not firm deployments)**
- Vals, February 2025 [VALS-VLAIRFEB-2025], share of checks passed, lawyer baseline first: document Q&A 70.1% vs
  94.8% best tool; summarisation 50.3% vs 77.2%; transcript analysis 53.7% vs 77.8%; extraction 71.1% vs 75.1%;
  chronology 80.2% vs 80.2%; redlining 79.7% vs 65.0% (59.4% in the report text); EDGAR research 70.1% vs 55.2%.
  Vendors chose which tasks to enter, and Vals discloses a customer relationship with a participant.
- Vals legal research, October 2025: AI 74-78% weighted score vs 69% for lawyers; AI ahead on 150 of 200 questions;
  multi-jurisdiction 14 points lower [VALS-VLAIRRES-2025]. LawSites reports 210 questions and 79-81% vs 71% on
  accuracy alone [LAWSITES-VALSRESEARCH-2025].
- Stanford 2024: tools from two leading providers each hallucinated (gave incorrect information or cited a source that does not support it)
  17% to 33% of the time [STANFORD-MAGESH-2024].
- OpenAI GDPval (44 occupations, not specific to professional services): the best model was rated as good as or
  better than experts in just under half of tasks (47.6% on the 220-task gold subset); vendor-run [OPENAI-GDPVAL-2025].

**Trials with professionals**
- Patent drafting, 133 lawyers, three months: quality +0.34 SD (standard deviations) at 10 days and +0.38 SD at 90
  days; unaided redlining afterwards +0.32 SD overall, +0.45 SD for seniors, no average gain for juniors.
  Run and funded by Google, whose model was tested (vendor-published) [NBER-AUTOR-2026].
- BCG, 758 consultants, GPT-4 (2023): 12.2% more tasks and 25.1% faster inside AI's capability; 19% less likely
  correct on a task outside it [HBS-DELLACQUA-2023].

**Vendor and firm figures (vendor-published or self-reported)**
- Microsoft Legal Agent: more than 1,800 users, nearly 100,000 edits, about 70% of suggestions kept; internal
  fluency, conciseness and relevance scores above 90%, 95% and 85%; no independent benchmark [MSFT-COPILOTLEGAL-2026].
- Harvey diligence benchmark (synthetic data rooms, LLM-judged): 23.3% to 62.4% mean rubric pass rate [HARVEY-RLM-2026].
- Dentsu (in-house): DPIA agent "cut the process by 75%" (method not stated); estimated 4-10 hours a week per
  lawyer; 93% weekly use [HARVEY-DENTSU-2026].
- RSGI survey of Harvey customers, commissioned by Harvey (87 respondents): power users save 11 hours a week, up
  from 8.5; 89% of law firms say they can take on more work; 48% of in-house teams mandated AI at their firms, one reported savings
  [LEGALIT-RSGI-2026].
- Adoption, not quality: CMS 95% active use among 3,000+ lawyers [HARVEY-CMS-2026]; Reed Smith 1,400 monthly users
  of about 1,800 lawyers [HARVEY-REEDSMITH-2026]; Crowell 91% of 700+ attorneys are users, nearly 70% weekly
  [LEGORA-CROWELL-2026]. Vendor customer pages carry headline stats with no method [HARVEY-CUSTOMERS-2026].

**Surveys**
- ILTA (508 law firms): 94% engaged with GenAI; formal policy 57% (under 50 lawyers) to 98% (350-699); training
  before use 11% to 72% [ILTA-TECHSURVEY-2026]. Only 19% of firms using or exploring Microsoft 365 Copilot had fully
  rolled it out to lawyers (Legal Geek, citing ILTA) [LEGALIT-LEGALGEEK-2026].
- Thomson Reuters (1,816 professionals): 34% use unsanctioned AI; 66% with a named AI strategy say AI meets
  expectations vs 22% without; 78% of corporate clients call AI quality gains very important or essential, 6% say
  most providers deliver them [TR-FOP-REPORT-2026]. A TR speaker said firms with a strategy are 3.9 times more likely to see ROI and 22%
  have one [TRI-LEGALWEEK-2026].
- In-house: nearly 60% saw no noticeable savings from outside counsel's AI [BLOOMBERGLAW-ACC-2025]. Consultants:
  50% use GenAI for content creation, 54% use unapproved tools [LEXISNEXIS-FOW-2026]. Professional-services firms:
  43.6% of projects use AI, up from 23.1% [SPI-AI-2026].

**What to measure:** share of AI suggestions kept, edited or rejected; errors caught at review and after release;
rework; time to first draft and to sign-off; recall on a test set before relying on a tool; how often juniors work
unaided. Hours saved alone says nothing about quality.

## 6. Guardrails

- **ABA Formal Opinion 512 (2024-07-29):** verification proportionate to tool and task; sample-testing a tool
  before relying on it is acceptable; managers set policy and train; AI material may be marked in files;
  self-learning tools can expose one client's data in another matter [ABA-OP512-2024].
- **State Bar of California (approved 2026-05-14):** supervision rises with autonomy; agents must not make
  substantive legal determinations, give advice, file, or send client data out without lawyer review; re-assess
  tools as they change; follow client AI restrictions [CALBAR-GENAI-2026]. Proposed rule amendments (candour to
  verify citations, manager duty to set AI policy) were out for comment to 2026-05-04 [CALBAR-RULES-2026].
- **England and Wales:** the Divisional Court expects AI research checked against authoritative sources and will
  ask what leaders did [EWHC-AYINDE-2025]; the SRA warned after 42 misuse reports in a year [LAWSOCIE-SRAWARN-2026];
  judicial guidance was updated in October 2025 [JUDICIARY-AIGUIDE-2025]; the Bar Standards Board advised "absolute
  caution" on agentic AI (headline only) [LAW360-BSB-2026].
- **Ireland:** High Court practice direction HC 142 (from 2026-09-01) requires independent verification of
  AI-generated material [LAWSOCIE-HC142-2026].
- **Management consulting:** the ICMCI code (May 2026) bars unreviewed AI output as finished work, requires
  verification of facts, calculations and references, and disclosure where AI materially affects advice
  [ICMCI-AICODE-2026].
- **Tax practitioners:** IRS Office of Professional Responsibility guidance (2026-06-24) maps Circular 230 duties
  onto AI; detail is in the tax archetype [IRS-OPR-2026].
- **EU:** AI literacy obligations apply since 2025-02-02; the AI Act became applicable on 2026-08-02 with
  exceptions [EC-AIACT-2026].
- **Clients:** Public Services and Procurement Canada requires suppliers to declare AI use in advance
  [BNN-DELOITTE-2025]; guidelines that say "use AI", "not without permission" and "won't pay for AI work" arrive
  together [TRI-LEGALWEEK-2026].

**Steps that stay with a person:** deciding relevance and what a finding means; accepting each redline; signing
advice, filings and reports; confirming every cited authority; choosing which tasks are AI-first; approving what
an agent may reach or send; disclosure decisions.

## 7. Roles and how they evolve

- **Drafters become reviewers and approvers.** Microsoft's in-house counsel spends saved time on judgment and
  negotiation [MSFT-COPILOTLEGAL-2026]. A former McKinsey consultant says validating AI output is now a big part of
  the junior job [STRATEGYCASE-JUNIOR-2026].
- **Juniors.** Seniors kept the skill benefit and juniors' unaided outcomes split [NBER-AUTOR-2026]; 48% of
  professionals fear harm to judgment development [TR-FOP-REPORT-2026]. Blank Rome and Duane Morris answer with
  apprenticeship, champions and mentoring [HARVEY-BLANKROME-2026; TRI-ONBOARDING-2026]. Allens lawyers say AI
  minimised grunt work and changed mentoring [ALLENS-XEXAM-2026]. A Georgetown writing professor does not see the
  feared skills degradation [TRI-CLARITYWRITE-2026].
- **New roles.** Legal engineers at vendors (34 Harvey and 54 Legora postings by title on 2026-10-19) and firms
  (PwC Legal Brussels) [HARVEY-JOBS-2026; LEGORA-JOBS-2026; PWC-LEGALJOB-2026];
  chief pricing and innovation officer and AI innovation head [TRI-LEGALWEEK-2026]. Ascend (accounting) has a
  30-person AI team working alongside CPAs [AT-AINATIVE-2026].
- **Hiring signals (vendor-commissioned survey of Harvey customers):** 82% of law firms and 94% of in-house teams are changing hiring criteria
  toward AI skills; 69% of firms do not plan to cut graduate intake over two years [LEGALIT-RSGI-2026].
- **Leaders and in-house teams.** Leaders carry documented accountability [EWHC-AYINDE-2025]. In-house counsel
  draft more themselves and value outside counsel for judgment [TRI-AIFORUM-2026]. Firms are racing to extract
  lawyers' knowledge into AI workflows [VAULT-PYRAMID-2026].

## 8. Frontier

- **2026-05-12** Anthropic: 20+ legal connectors and 12 practice plugins that start by learning playbooks [LAWSITES-ANTHROPIC-2026].
- **2026-05-14** California approves guidance covering agentic AI [CALBAR-GENAI-2026].
- **2026-05-18** UK Bar Standards Board: "absolute caution" on agentic AI [LAW360-BSB-2026].
- **2026-06-04** ICMCI launches its AI code for consultants; **2026-06-24** IRS OPR AI guidance [ICMCI-NEWS-2026; IRS-OPR-2026].
- **2026-06-12 / 09-08** Harvey agent benchmarks for in-house contracting and diligence [HARVEY-LABCONTRACT-2026; HARVEY-RLM-2026].
- **2026-08** SRA warning notice on AI misuse [LAWSOCIE-SRAWARN-2026]. ILTACON: seat-to-consumption AI pricing a hallway worry [EDISCOVERYTODAY-ILTACON-2026].
- **2026-09** NBER patent-drafting trial [NBER-AUTOR-2026]. Irish practice direction HC 142 in force (2026-09-01).
- **2026-09-17** OpenAI Astra for Law with Trusted Access for Am Law 200 firms [LAWSITES-OPENAI-2026].
- **2026-10-15** Microsoft Copilot for Legal generally available, the fourth AI major with a legal vertical in five months [LAWSITES-MSFT-2026]. Harvey Legal Work Orchestration; Harvey forecasts agents taking a further 20% of workflow steps in six months [HARVEY-ORCH-2026]. Legal Geek: the path runs chatbot, workflow, delegated task [LEGALIT-LEGALGEEK-2026].
- **2026-10-16** Hogan Lovells Cadwalader announces both Legora and Harvey [LEGORA-HLC-2026; HARVEY-HLC-2026].
- **2026-10-19** Law Society: very limited use of fully autonomous agents so far [LAWSOC-WHATAGENTIC-2026].
- **2026-11-11 (scheduled)** TRI webinar on accountability "beyond human in the loop" [TRI-EVENTS-2026]. Signal only.

## 9. Common objections

- **"The numbers are vendor marketing."** Largely true for firm results. Benchmarks test tools
  (Vals, Stanford); trials measure people with AI (HBS; NBER, which Google ran and funded). LegalOn's own CEO says to treat vendor benchmarks sceptically
  [ARTLAW-LEGALON-2026]. Answer: test on your own matters before relying (`#23`).
- **"It hallucinates."** Yes: 17-33% in 2024 research tools [STANFORD-MAGESH-2024]; 2,202 court decisions
  [CHARLOTIN-DB-2026]; Deloitte Australia's partial refund [CTV-DELOITTE-2025]. Answer: grounded tools plus a
  recorded check of every reference (`#01`, `#11`); solicitors stay responsible whether or not AI is used
  [LAWSOC-WHATAGENTIC-2026].
- **"It can't do what our lawyers do."** Partly right: lawyers led on redlining and EDGAR research; AI led on Q&A,
  summarisation and research accuracy [VALS-VLAIRFEB-2025; VALS-VLAIRRES-2025]. Answer: allocate task by task (`#07`).
- **"Clients won't pay for it, or won't let us use it."** Both are happening: some clients mandate AI, some bar it,
  some refuse to pay for AI work [TRI-LEGALWEEK-2026]. Answer: capture client terms at matter opening (`#25`).
- **"We can't prove savings."** Firms say they are in an anecdotal phase [TRI-LEGALWEEK-2026], and SPI calls hours
  saved but not turned into revenue "the leak" [SPI-AI-2026]. Answer: log edits and review findings (`#24`).
- **"Juniors won't learn."** A real risk [NBER-AUTOR-2026]; a counterview reports no degradation
  [TRI-CLARITYWRITE-2026]. Answer: keep unaided practice and a challenger step (`#10`).
- **"It's hype; it will pass."** An ILTA respondent said so [ILTA-TECHSURVEY-2026]. LawSites called ILTACON 2026
  "peak legal tech", meaning peak energy, not a fading trend [LAWSITES-PEAK-2026]. ILTA reports 94% of firms engaged.
- **"What happens to my job and the time saved?"** Employees ask this [TRI-CLARITYHUMAN-2026]. Talk about roles and
  capacity (§7), not headcount.

## 10. Sources

Full details for YAML keys are in the YAML. Keys cited here but not in the YAML:
- ALLENS-XEXAM-2026: Law Institute of Victoria, Cross-Examined podcast, How AI in legal supervision is changing lawyer training, 2026-03-23, https://www.castfox.net/podcast/cross-examined-7610284/episode/how-ai-in-legal-supervision-is-changing-lawyer-training-1785836
- AT-AINATIVE-2026: Accounting Today, On the Air podcast, The AI-native firm (Ascend CEO), 2026, https://www.accountingtoday.com/podcast/the-ai-native-firm
- EDISCOVERYTODAY-ILTACON-2026: eDiscovery Today, My Five ILTACON 2026 Takeaways, 2026-09-04, https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/
- HARVEY-CUSTOMERS-2026: Harvey, customers page (undated; read 2026-10), https://www.harvey.ai/customers
- HARVEY-LABCONTRACT-2026: Harvey, Extending Harvey's Legal Agent Bench to In-House Contracting, 2026-06-12, https://www.harvey.ai/blog/legal-agent-benchmark-in-house-contracting
- ICMCI-NEWS-2026: ICMCI, Launches Global Code for the Responsible Use of AI in Management Consulting, 2026-06-04, https://www.cmc-global.org/content/icmci-launches-global-code-responsible-use-ai-management-consulting
- IRS-OPR-2026: IRS Office of Professional Responsibility, Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19), 2026-06-24, https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
- JUDICIARY-AIGUIDE-2025: Courts and Tribunals Judiciary, AI Judicial Guidance (October 2025), 2025-10-31, https://www.judiciary.uk/guidance-and-resources/artificial-intelligence-ai-judicial-guidance/
- LAW360-BSB-2026: Law360 UK, Treat Agentic AI With 'Absolute Caution,' BSB Guidance Warns, 2026-05-18, https://www.law360.co.uk/articles/2477570 (headline only)
- LAWSITES-PEAK-2026: LawSites, Have We Reached 'Peak Legal Tech?', 2026-08-28, https://www.lawnext.com/2026/08/have-we-reached-peak-legal-tech-sure-felt-that-way-at-iltacon-this-week.html
- LEGORA-CROWELL-2026: Legora, Crowell & Moring shares results from firmwide Legora integration, 2026 (date unconfirmed), https://legora.com/customers/crowell
- OPENAI-GDPVAL-2025: OpenAI, GDPval (arXiv 2510.04374), 2025-10-05, https://arxiv.org/abs/2510.04374
- SPI-AI-2026: SPI Research, Impact of AI on Professional Services 2026 (summary page; report paywalled), 2026-10, https://spiresearch.com/reports/2026-ai-professional-services-survey/
- TRI-CLARITYHUMAN-2026: Thomson Reuters Institute, Clarity podcast S6 E8, human side of AI transformation, 2026-10-15, https://www.thomsonreuters.com/en/institute/podcast/human-side-of-ai-transformation
- TRI-CLARITYWRITE-2026: Thomson Reuters Institute, Clarity podcast S6 E6, Is AI ruining legal writing?, 2026-10-07, https://www.thomsonreuters.com/en/institute/podcast/ai-ruining-legal-writing
- TRI-EVENTS-2026: Thomson Reuters Institute, events listing (read 2026-10-19), https://www.thomsonreuters.com/en/institute/events

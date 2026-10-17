# Research and advisory (tax)

Sources checked 2026-10-17. Use cases live in `../use-cases/research-advisory.yaml` (25 entries).
Ids are shortened here: `#05` means `tax-research-advisory-05`. Source keys in brackets are in the YAML or in §10.

**Read this first.** Adoption is broad, but measured evidence is thin. Grades: A 0, B 11, C 8, D 6 (44% A/B). No entry
reaches grade A: the before-and-after times (#01, #02, #09) are named practitioners' estimates quoted in case studies
published by the vendors that sell the tools, not measurements, so those entries are graded B.
No independent test of a commercial tax research product (Blue J, CoCounsel, Bloomberg Tax AI, CCH) exists. The
independent numbers test models or adjacent legal-research tools, and they are unflattering: the best model scored
49% on corporate tax research questions (fully correct, citation-adjusted) [VALS-TAXAGENT-2026]. Use the speed figures as practitioner
claims and lead with verification, ownership and fees, which is where the field's argument now sits.

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

Technical tax research, memos, written advice and opinions, planning and structuring, and M&A tax diligence, done by
advisers in CPA, law and Big Four firms and by in-house tax counsel. There are two distinct buyers: firm advisers (Blue J,
Accordance, CoCounsel Tax, Bloomberg Tax, CCH) and corporate tax departments (TEI's research labs, enterprise assistants).
Return preparation sits in compliance, litigation conduct in controversy, and in-house data pipelines in tax-data-technology.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Scope the question | Take the client's or business's facts, frame the issues, set the deadline | client-interaction, expert-judgment | Clients arrive with chatbot answers of their own (#18) |
| Locate and read authority | Code, regulations, rulings, cases, treaties, commentary; several tools per firm (three on average) [BLUEJ-OUTLOOK-2025] | research-synthesis | 81.3% also use search engines; legacy tools used weekly or daily by 50-61% versus 88% for those with AI tools (vendor survey) [BLUEJ-OUTLOOK-2025]; gray-area questions take most of a day [ACCORDANCE-WFY-2026] |
| Analyse and conclude | Apply law to facts, weigh authority, compute effects, model planning alternatives | expert-judgment, data-reporting | An S-corporation election analysis took about 10 hours [ACCORDANCE-FINNEY-2025]; models get calculations wrong in ways hard to see [COLUMN-TAXCALCBENCH-2025] |
| Draft | Memo, advice letter, opinion, workpaper footnote, client email | document-production | Days of junior time per draft [BTAX-LOWY-2026] |
| Review and sign off | Partner or national-office review; JofA now recommends firm policies requiring human verification of every cited authority [TAXCT-CLINCO-2026] | review-assurance | Errors that are "polite, quiet and technical" and hard to review at volume [TEI-TAXTECH-2026] |
| Deliver and follow up | Answer client, business-unit and auditor questions | client-interaction | "We will research and call you back" [ACCORDANCE-BARNES-2026] |
| Transaction work | Read SPAs and partnership agreements, spot issues, write the diligence report, structure | review-assurance, document-production | Deal deadlines; long documents [KPMG-MA-2025] |
| Monitor and keep knowledge | Track law changes; keep playbooks, prior memos, internal guidance | research-synthesis, coordination-scheduling | Outdated law in model answers [BTAX-HALLUC-2026]; knowledge leaves as seniors retire [TR-AGENTICBLOG-2026] |
| In-house: serve the business | Ad hoc questions from finance, legal, auditors | research-synthesis, client-interaction | 58% of 288 departments under-resourced; over half of time reactive [TR-CORPTAX-2025] |
| Scope and price | Engagement letter, fee basis | coordination-scheduling | Hourly billing versus OPR's fee rule (#25) |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome), reinvent (service or operating model changes). **Automate has one grade-C entry (#20) and no
process-level automation. Delegate has four entries, none above C. Reinvent has two (#24, #25) plus an idea in #15.**

**Research**
- Improve: `#01` (B) cited conversational assistant; named firms report single tasks falling from hours to minutes.
  `#02` (B) multi-step research plans for gray-area questions (Accordance agents per step; Bloomberg Deep Thinking Mode).
  `#07` (B) one approved, closed tool firm-wide with a named tax AI leader (Crowe, KPMG, PwC). `#08` (B) the assistant as
  a tutor for juniors. `#06` (C) in-house research and question triage. `#05` (C) assistant over the firm's own memos.
  `#04` (idea) a specialist workflow for 50-state and multi-jurisdiction questions, where tools score worst.
- Delegate: `#03` (C) an agent works a question end to end and submits a cited memo; benchmarked, not deployed.
  `#23` (C) law-change monitoring that drafts client impact notes (KPMG Digital Gateway, announced).

**Analysis and planning**
- Improve: `#09` (B) reusable planning "blueprints" that turn client data into a decision matrix (S-corp election,
  10 hours to 2-2.5). `#13` (B) document-grounded analysis of operating agreements, trusts and schedules.
  `#12` (C) model translates rules, a deterministic engine calculates, the trace goes in the file.
  `#10` (idea) planning ideation and anti-abuse screening. `#11` (idea) AI argues the other side or cross-checks.

**Drafting and client communication**
- Improve: `#14` (B) first drafts of memos, letters and client emails (Blue J Tax Writing, CoCounsel, Nelson Mullins
  pilot). `#16` (B) answering during the client call. `#15` (idea) opinion and written-advice support.
  `#17` (idea) client-facing assistant with escalation. `#18` (idea) triage of client- or opponent-supplied AI material.
- Reinvent (idea): `#15` also carries Sala's question whether in-house teams could get direction from a technical tax
  AI before or instead of a Big Four opinion [SALA-TAXNOTES-2026].

**Review**
- Improve: `#19` (B) citation verification plus an AI-use record as a standing step (KPMG M&A Tax; JofA, OPR, TPB, PCRT).
- Automate: `#20` (C) automated existence-and-support check on every citation (PelAIkan; no performance data).

**Transactions**
- Improve: `#21` (B) KPMG M&A Tax: clause review against baselines and a first-draft diligence report.
- Delegate: `#22` (C) a vendor agent reads the data room and drafts the risk assessment (demo, no named customer).

**Commercial model**
- Reinvent: `#25` (B) fixed-fee and value pricing (Sasserath, RKL, RSM). `#24` (C) firms co-build agents with clients
  on their platforms (KPMG with Claude; EY Tax Agent Factory).

Sibling modules (final ids not yet published at this synthesis): controversy holds *Clinco* as litigation conduct and
notice responses; compliance holds TaxCalcBench and return agents; tax-data-technology holds in-house pipelines and
OpenAI's automation demos; provision holds PwC's explainable effective-tax-rate model.

## 4. Interview probes

Ask tax partners, research or national-office leads, in-house tax directors and knowledge or AI leads.

1. **"Take the last memo that used AI. Which steps did the tool do, how was each authority checked, who signed, and what
   does the file show?"** Reveals whether verification is real and recorded (#19). OPR expects documented procedures.
2. **"Which questions go to the tool first, which go straight to a senior or national office, and is that line written
   down?"** Reveals triage maturity and where novelty, penalty exposure or jurisdiction trigger escalation (#01, #15).
3. **"When did an AI-assisted answer last go wrong, and who caught it: author, reviewer, client or tax authority?"**
   Reveals real error experience. In reported cases the authority or tribunal often found the errors (#18).
4. **"What have you measured: errors found at review, rework, parallel runs against a human answer, disagreements?"**
   Reveals whether any baseline exists. Only 19% of firms deploying GenAI measure ROI [CPAPA-TR-2026].
5. **"Which tools are sanctioned, which do people use anyway, and who owns tax AI?"** Reveals shadow use (more than a
   third admit unauthorized tools) and the owner gap (two of 50+ TEI attendees said tax owns AI) (#06, #07).
6. **"How have engagement letters, time capture and fees changed since OPR Alert 2026-19?"** Reveals exposure on the
   s10.27 fee point and readiness for fixed or value pricing (#25).
7. **"How do you handle client data in research tools: closed systems, consent, section 7216?"** Reveals confidentiality
   control; the TPB requires client permission before data goes to third-party AI (#07, #13).
8. **"How are juniors learning the research craft if first drafts are machine-made?"** Reveals skill-erosion risk and
   whether training covers judging AI output (#08).
9. **"Do you keep simple lookups and gray-area questions on different tools or processes?"** Reveals whether multi-step
   research (#02) or agent runs (#03) are understood, and how review scales with longer answers.
10. **"Which questions do you refuse to put through AI at all?"** Reveals the boundary. The sources point to opinion-level work
    (#15), policy interpretation [PWC-MEGNA-2025] and client-identifying facts in public tools [PCRT-AI-2026].
11. **(In-house) "What do business teams ask you most, and could an assistant over your own guidance answer it?"**
    Reveals the case for #05 and #06; 58% of departments say they are under-resourced.

## 5. Metrics and benchmarks

**Adoption (do not average across surveys; samples differ)**
- 65% of 1,808 AICPA members who prepared 2025 returns for a fee use AI in tax research; 16% have no plans (24.3% a
  year earlier) [AICPA-TAXSW-2026] (professional-body survey).
- 60% of 1,000 US accountants (Mar 2026) work at firms that adopted AI-powered tax research (33% in 2025, different
  sample); 80% use AI for tax research weekly or monthly; 90% have access to general-purpose AI, 46% to tax-specific AI
  [BLUEJ-OUTLOOK-2026] (vendor survey).
- 81% of tax and audit professionals use AI regularly; more than one third admit unauthorized tools [TR-FOP-2026].
- 34% of tax firms deploy GenAI at organization level (from 21%); 19% of those measure ROI; 14% use agentic AI now
  [CPAPA-TR-2026] (Thomson Reuters-authored).
- In-house: 67% of 288 corporate departments not using GenAI in 2025 [TR-CORPTAX-2025]; 71% of companies in KPMG
  Germany's quick surveys use AI tools in tax, and 66% of users report noticeable time savings (sample not stated) [KPMG-DE-2026].

**Time (all vendor-published, single-firm estimates)**
- 1 hour to 10 minutes; 1.5 days to 3 hours; 8 hours to 1 hour; 2-6 hours to 15-20 minutes; 10 hours to 2-2.5 hours
  (#01, #02, #09). 2.94 hours a week saved across research and drafting [BLUEJ-OUTLOOK-2025]; 32% per task for
  CoCounsel users [CPAPA-TR-2026].

**Quality (independent unless stated)**
- Vals Tax Agent Bench (updated 2026-10-16): best model 49.19% fully correct and citation-adjusted on 193 private
  corporate tax research questions; best by category: rule and source lookup 66.67%, current and temporal 66.67%, forms
  and filings 40.00%, controversy and precedence 36.67% [VALS-TAXAGENT-2026]. Simple tax Q&A no longer separates models:
  Vals archived TaxEval v2 as saturated, with a top score of 80.38% [VALS-TAXEVAL-2026].
- Legal research tools (adjacent): 17% to 33% hallucination [STANFORD-HALLUC-2024]; AI products 74%-78% versus a 69%
  lawyer baseline; participants scored 14 points lower on average on multi-jurisdiction questions [VALS-VLAIR-2025].
- ChatGPT on taxpayer questions: 39% to 47% correct (2023-24, older models) [ANTINOZZI-2024]. Return calculation: best
  model 32.35% strict on 51 simplified returns (vendor-authored) [COLUMN-TAXCALCBENCH-2025].
- Vendor signal only: Blue J users disagree with answers less than 0.2% of the time; not an accuracy rate [BLUEJ-OUTLOOK-2025].

**Incidents**
- 2,199 decisions worldwide addressing hallucinated content, about 25 tagged tax [CHARLOTIN-DB-2026]. A preprint reports
  nearly 800 cases of AI-related citation errors or hallucinations in 25+ countries by late 2025, about 90% without formal professional sanctions
  [PREPRINTS-HALLUC-2026]. Judge Holmes had seen fewer than a dozen in Tax Court filings by March 2026 [BLAW-TAXCT-2026].

**Governance**
- 57.4% of 176 indirect tax leaders would not be confident defending AI-assisted decisions to an authority; 12.5% have
  AI targets [FONOA-2026] (adjacent).

**Not found:** error, override or parallel-run rates from any firm deployment; inspection findings; any head-to-head of
commercial tax research tools. **Suggested measures:** errors caught at review per AI-assisted memo, review time,
rework, disagreement with seniors' answers, citation-check failures, share of answers escalated.

## 6. Guardrails

**United States**
- OPR Alert 2026-19 (24 Jun 2026) applies existing Circular 230 duties: due diligence (s10.22: verify facts, citations
  and calculations), fees (s10.27: do not bill manual time not spent; pass savings on openly), competence (s10.35),
  firm procedures (s10.36), written advice (s10.37: opaque logic can make reliance unreasonable), and IRC 6713 and 7216
  on taxpayer information [IRS-OPR-2026]. Law-firm commentary reads it as covering corporate, payroll and plan advice,
  not only Form 1040 work [NATLAW-OPR-2026].
- AICPA SSTS section 1.4: members may rely on tools, stay responsible, and may use AI to enhance but not supplant judgment
  (as summarised by JofA) [TAXCT-CLINCO-2026].
- Tax Court: *Clinco* (T.C. Memo. 2026-16) admonished counsel for three probable hallucinated cases of four, without
  sanctions [TAXCT-CLINCO-2026]. Judge Holmes calls section 6673 the most prominent tool and doubts a no-AI
  certification would make sense [BLAW-TAXCT-2026].
- No authority yet on whether AI-generated advice supports reasonable cause or a preparer-penalty defence (#15).

**United Kingdom and Australia**
- PCRT topical guidance (19 Jan 2026): treat output like a junior colleague's work; consider disclosing actual use;
  explain how a conclusion was reached; keep an audit trail; no client data in public tools without consent or
  anonymisation [PCRT-AI-2026]. Tribunals: in *Elden v HMRC* an ICAEW-regulated firm was criticised for unverified AI
  output; *Zzaman* involved real cases that did not support the argument [ICAS-TAXTRIB-2026].
- HMRC (28 Jan 2026) expects generative-AI tax software to flag nuanced rules and prompt users to check [HMRC-GENAI-2026].
- TPB(GS) 55/2026 (22 Jul 2026): AI "cannot be relied on as a replacement for tax knowledge"; client permission before
  data goes into third-party AI; document verification [TPB-GS55-2026].

**Frameworks, not standards**
- Werfel's framework: 20 risks for tax authorities and 15 for preparers (hallucinated advice, control dilution, skill
  erosion, liability ambiguity), with limited-scope pilots first [TAXADVISER-WERFEL-2026; AICPA-WERFEL-2026]. The AICPA's
  CART (23 Sep 2026) will test it [AICPA-CART-2026]; the AICPA says AI moves too fast for lasting standards [ACCTODAY-CART-2026].
- Fees are disputed: the AICPA calls OPR's fee language "overly simplistic" and seeks IRS clarification [AICPA-FEES-2026].
- Disclosure to clients: in April 2025 JofA found no federal law or professional standard mandating it, with some states
  requiring some disclosure [JOFA-DISCLOSE-2025]; OPR's 2026 alert now says practitioners should disclose AI activities, in
  general or specific terms, when crediting cost savings [IRS-OPR-2026].

**Steps that stay with a person:** deciding what may go through AI; reading the authority that carries the argument;
the conclusion and its confidence level; anything signed (opinions, written advice, filings); planning against substance
doctrines; the fee basis; what is said live to a client [IRS-OPR-2026; PCRT-AI-2026; TPB-GS55-2026].

## 7. Roles and how they evolve

- **Associates** do more first-pass research: Blue J's users are 40.8% associates, 27.7% mid-level, 31.5% seniors (#01).
- **Reviewers** check a "junior colleague's" output [PCRT-AI-2026]; Lowy rates current output at average junior-associate
  level and calls AI proficiency a core competency [BTAX-LOWY-2026]. The client file records the prompts, how outputs
  were verified and who reviewed (#19).
- **New roles:** Crowe's Tax AI Leader, PwC's US AI Tax Leader and governance committee, AI leads or committees, knowledge
  managers on AI panels (#07, #05). PwC reports 3,200 AI champions and about 80% of US people trained [PWC-MEGNA-2025].
- **Juniors:** skill erosion and knowledge loss are named risks [TAXADVISER-WERFEL-2026]; firms should define the
  early-career role [TR-FOP-2026]. More than a quarter of professionals would not join a firm lacking professional-grade
  AI, and almost a third would consider leaving if expectations go unmet within two years [TR-FOP-2026].
- **Headcount:** Sala argues corporate tax teams will shrink little [SALA-TAXNOTES-2026]; 58% of companies in KPMG Germany's
  surveys expect stable domestic tax headcount [KPMG-DE-2026]; Deloitte's scenarios move professionals toward oversight, interpretation,
  policy and disputes [DELOITTE-TTT-2026].
- **Partners:** an RSM partner says AI frees time for deeper advisory work and strategy discussions (#25); KPMG's and
  EY's platforms let professionals and clients build agents together (#24).

## 8. Frontier

- **2025-08-04** Blue J raises $122M and says it more than doubled revenue and customers in H1 2025 [BLUEJ-SERIESD-2025].
- **2025-09-08** Accordance launches with $13M (Anthropic among investors); reports 10x usage growth in six months [ACCORDANCE-RAISE-2025].
- **2025-11-05** CoCounsel in use at 1,300+ firms (company claim) [TR-COCOUNSEL-2025]. **2025-11-25** EY Tax Agent Factory (#24).
- **2026-01** PCRT guidance (19th), HMRC software guidelines (28th); ICAS summarises UK tribunal AI cases including *Elden* (26th) [ICAS-TAXTRIB-2026].
- **2026-03-09** Bloomberg Tax Deep Thinking Mode (#02). **2026-03-20** Tax Court "feeling our way in the dark" [BLAW-TAXCT-2026].
- **2026-03-26** Werfel presents his framework at Duke [TAXPROF-WERFEL-2026]. **2026-05-01** TR: "reason-and-act" research (#02).
- **2026-05-20** KPMG and Anthropic Digital Gateway, initial focus on tax clients and PE firms (#23, #24). **2026-06-24** OPR Alert 2026-19.
- **2026-07-22** TPB guidance. **2026-08-31** Werfel framework published. **2026-09-08** AICPA asks IRS to clarify fees.
- **2026-09-23** CART launched [AICPA-CART-2026]. **2026-10-16** Vals Tax Agent Bench update, best model below 50% (#03).
- **Advisory demand from AI itself:** companies asked the OECD to clarify how AI transactions between affiliates are
  characterised (AstraZeneca commented that AI will change how intragroup services are performed), and the draft
  intragroup-services examples cover pricing shared AI tools (Aug 2026) [OECD-INTRAGROUP-2026]; nexus and
  value-creation questions were on the D.C. Bar programme [DCBAR-TAX-2026]; R&D credit for clients' AI projects
  [CPAPA-RD-2026]. These are advice topics, not AI-in-practice use cases.
- **Watch:** conferences after the scan date were not covered; Siva's proposed judicial certification and s10.22
  amendment are one practitioner's proposal [BTAX-SIVA2-2026].

## 9. Common objections

- **"It hallucinates."** True, including retrieval tools (17-33% in legal research) [STANFORD-HALLUC-2024]. The answer is
  a recorded verification step (#19), a citation checker as a second line (#20) and reading the authority that carries
  the argument. Courts and regulators already expect this [IRS-OPR-2026; TAXCT-CLINCO-2026].
- **"The speed claims are vendor marketing."** Mostly yes: every tax-tool figure is vendor-published (#01). Ask the
  client to run a small parallel test and count review findings (§5 suggested measures).
- **"Clients won't pay for hours we no longer spend."** OPR agrees on the fee point; firms are moving to fixed or value
  fees, and 69% of adopters are considering alternatives to hourly billing (#25). The AICPA is contesting the language.
- **"Agents can do the whole memo now."** Not reliably: the best model is fully correct on under half of research
  questions, and answers run about four times longer than expert ones, which loads review (#03).
- **"We'll lose our juniors' judgment."** A real, named risk [TAXADVISER-WERFEL-2026]; firms use the tool as a tutor and
  supervise reasoning, not answers (#08).
- **"Confidentiality rules it out."** Closed, approved tools with no training on client data, client consent where
  required (TPB, PCRT) and no client data in public tools address it (#07); verification duties remain.
- **"AI will replace the tax team."** Sala argues culpability cannot be delegated and teams will shrink little; most
  respondents to KPMG Germany's surveys expect stable headcount (#06).
- **"Nobody here owns it."** Common: two of 50+ TEI attendees said tax owns AI. Name an owner and an approved list (#07).

## 10. Sources

Full details for entry sources are in the YAML. Keys cited here that are not in the YAML:
- AICPA-TAXSW-2026: The Tax Adviser (AICPA), *2026 tax software survey*, 2026-08-31, https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/
- VALS-TAXEVAL-2026: Vals AI, *TaxEval v2 leaderboard and methodology (archived)*, 2026-09-01, https://www.vals.ai/benchmarks/tax_eval_v2
- PREPRINTS-HALLUC-2026: Preprints.org, *Citing the Unseen: AI Hallucinations in Tax and Legal Practice* (preprint, not
  peer reviewed), 2026-01, https://www.preprints.org/manuscript/202601.0187/v1
- NATLAW-OPR-2026: The National Law Review, *IRS OPR Issues AI Guidance: Tax Professionals Also Face AI Ethics and
  Compliance Obligations*, 2026-08-04, https://natlawreview.com/article/irs-office-professional-responsibility-opr-issues-ai-guidance-tax-professionals
- ACCTODAY-CART-2026: Accounting Today, *Former IRS commissioner teams with AICPA to form AI tax risk group*, 2026-10-08,
  https://www.accountingtoday.com/news/former-irs-commissioner-teams-with-aicpa-to-form-ai-tax-risk-group
- TAXPROF-WERFEL-2026: TaxProf Blog, *Werfel Presents Risk Framework ... at Duke*, 2026-03-26, https://taxprofblog.aals.org/2026/03/26/werfel-presents-risk-framework-for-the-use-of-artificial-intelligence-in-tax-administration-and-practice-today-at-duke/
- BLUEJ-SERIESD-2025: Blue J, *Blue J Announces $122M Series D Financing*, 2025-08-04, https://www.bluej.com/blog/blue-j-announces-122m-series-d-financing-led-by-oak-hc-ft-and-sapphire-ventures
- ACCORDANCE-RAISE-2025: Accordance, *Accordance Raises $13M from Khosla Ventures and General Catalyst*, 2025-09-08, https://www.accordance.com/press/accordance-raises-13m-from-khosla-ventures-and-general-catalyst
- TR-COCOUNSEL-2025: Thomson Reuters, *Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and
  Accounting Workflows*, 2025-11-05, https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows
- OECD-INTRAGROUP-2026: Bloomberg Tax Daily Tax Report, *Companies Want OECD to Clarify Character of AI Transactions*
  (opening paragraphs only), 2026-08-25, https://news.bgov.com/daily-tax-report/companies-want-oecd-to-clarify-character-of-ai-transactions
- DCBAR-TAX-2026: D.C. Bar, *Rise of the Machines: How Artificial Intelligence Is Changing the Tax World*, 2026-01-08,
  https://events.dcbar.org/Tax2026/session/3513387/rise-of-the-machines-how-artificial-intelligence-is-changing-the-tax-world
- CPAPA-RD-2026: CPA Practice Advisor, *Spotting R&D Tax Credit Opportunities in Clients' Custom AI Projects*, 2026-08-10,
  https://www.cpapracticeadvisor.com/2026/08/10/spotting-rd-tax-credit-opportunities-in-clients-custom-ai-projects/188227/

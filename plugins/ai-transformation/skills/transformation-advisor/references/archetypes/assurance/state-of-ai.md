# State of AI in assurance

Last researched 2026-10-17; figures are as published up to that date. Use this in onboarding to bring in one real
example early, in Frame to set a realistic baseline, and whenever a leader says "everyone else is already doing it".
Keep three things apart: what is **measured**, what is **announced**, and what is **forecast**. Source keys in brackets
resolve in §8 or in [sources.md](sources.md).

## Contents

1. [Headlines](#1-headlines)
2. [Measured adoption](#2-measured-adoption)
3. [What leaders are doing](#3-what-leaders-are-doing)
4. [How maturity is spread](#4-how-maturity-is-spread)
5. [Client-side maturity drives new work](#5-client-side-maturity-drives-new-work)
6. [What is not measured](#6-what-is-not-measured)
7. [Using this in a conversation](#7-using-this-in-a-conversation)
8. [Sources](#8-sources)

## 1. Headlines

- **Broad at the top, thin below.** KPMG, EY, Deloitte and Grant Thornton US announced firm-wide agent platforms between
  April 2025 and June 2026; PwC has tools for each audit step and plans a global platform [KPMG-CLARA-2025;
  EY-CANVAS-2026; GT-GTAP-2026; DELOITTE-OMNIA-2026; PWC-AT-2025]. In the main public benchmark of US CPA firms (54 firms
  of varying sizes), 75% had no documented transformation plan [CPACOM-ATR-2025].
- **Uneven by audit area.** Regulators most often see automated tools in journal-entry testing and least often in IT
  application work [IFIAR-TTF-2025].
- **Measured savings are modest so far.** PwC's US assurance leader said in October 2026 that busy-season savings were
  "not that drastic yet" [CFODIVE-PWC-2026]. The large figures in circulation are vendor-published.
- **No regulator prohibits AI.** Regulators have moved from observing to issuing guidance (see [guardrails.md](guardrails.md)).
- **No independent quality measure exists** for any audit AI tool in live use: no published error, override or
  parallel-run result was found in public sources.

## 2. Measured adoption

**Regulators' view of audit files (international).** Share of IFIAR members that "frequently" saw automated tools in the
audit files they inspected (42-49 members answering per row; this measures what inspectors see, not the share of audits)
[IFIAR-TTF-2025]:

| Audit area | 2023 | 2024 |
|---|---|---|
| Journal-entry testing | 86% | 88% |
| Risk assessment | 49% | 55% |
| Substantive procedures | 51% | 55% |
| Internal-controls testing | 33% | 43% |
| IT applications and security configurations | 33% | 39% |

- 31% of members reported findings that a tool "was not used as intended" (29% the year before); common findings were
  misread results, thin testing of outliers and weak ITGC testing [IFIAR-TTF-2025].
- IFIAR's 2026 report adds 2025 data, but only as a chart: frequent observations were largely unchanged or slightly
  higher, with more use in substantive procedures, from a larger group of respondents [IFIAR-TTF-2026].
- The six global networks reported about 30% more AI-enabled tools in 2025 than in 2024, with reporting practices that
  differ by network [IFIAR-TTF-2026].
- Canada's regulator reported 2025 inspection cases where tools were the primary source of evidence for a class of
  transactions, with limited validation of input data and, for one tool, no testing of items it rated low risk
  [CPAB-EVOLVING-2025].

**US CPA firms of varying sizes** (CPA.com and AICPA, 54 firms with complete data, June-August 2025; the authors say the
sample is not representative and do not break results down by size) [CPACOM-ATR-2025]:
- 75% had no documented transformation plan; a quarter to a third used no AI at all (the report gives both figures);
  22% had no automated solution.
- Automated solutions in place: workflow management 39%, foot-and-proof 39%, confirmations 39%, trial-balance import
  35%, engagement letters 26%, risk assessment 22%, data ingestion 19%, report production 17%, substantive analytics 11%.
- Top blockers: staff not trained 66%, poor client data 60%, no access to client systems 53%, budget 53%.
- How firms measure return: staff efficiency 83%, audit quality 54%, cost savings 37%.

**Internal audit.**
- 83% of audit functions were trying or using AI and 12% planned to within a year (Gartner, 119 CAEs, August 2025;
  the category mixes trials with production). CAEs reported low confidence in reaching their goals because of data
  quality, skills and access [GARTNER-2026].
- About 75% of 47 Nordic internal audit leaders were using or planning AI tools; data access or quality was the top
  barrier (60%) [KPMG-NORDIC-2026].
- Only 39% of 213 leaders expected AI to transform the profession significantly within five years, and 28% were
  confident their teams could audit AI risks (vendor survey) [OPTRO-FOF-2026].

**Professionals and SOC practices.**
- 81% of tax and audit professionals said they use AI regularly, and more than a third admitted using unauthorised tools
  (Thomson Reuters Institute; vendor-run) [TRI-FOP-2026].
- At EY's SOC conference, attendees reported using AI for evidence collection (63%), updating the Section 3 system
  description (45%) and drafting management responses to deviations (41%) (live poll, multiple answers, sample not
  stated) [EY-SOC-2026].

## 3. What leaders are doing

| Firm | What was said | Scale claimed | Status | Source |
|---|---|---|---|---|
| KPMG | Agents in Clara for expense vouching, unrecorded liabilities and accrued expenses; controls-testing agents promised within 12 months | More than 95,000 auditors | Announced 22 Apr 2025; no public confirmation of controls agents found by Oct 2026 | [KPMG-CLARA-2025] |
| EY | Multi-agent framework in EY Canvas "in all phases"; end-to-end support expected by 2028 | 130,000 assurance professionals, 160,000 engagements | Rolled out 7 Apr 2026; end-to-end is a forecast | [EY-CANVAS-2026] |
| Deloitte | Unified agents in Omnia run preliminary procedures and draft preliminary conclusions for review | Nearly 85,000 practitioners | Launched 24 Jun 2026 | [DELOITTE-OMNIA-2026] |
| PwC | Tools by audit step (planning, walkthroughs, Evidence Match); in Oct 2025 it aimed for end-to-end tools in 2026 and a global agentic platform about 18 months after that | Firm-wide AI investment of nearly US$1.5bn | Some in use, others planned (forecast by PwC) | [PWC-AT-2025; CFODIVE-PWC-2026] |
| Grant Thornton US | gtap platform; private-company audits first, public companies the next year | Full US Audit & Assurance practice, phased | Launched 7 May 2026 | [GT-GTAP-2026] |
| RSM US | Control-testing platform with Andera for internal audit; guidance copilot and staffing tool | Not stated | Announced 26 Aug 2026 | [ANDERA-RSM-2026; CAQ-RSM-2026] |

**Vendors that mid-size and small firms license** (all figures vendor-published):
- Thomson Reuters Disclosure Review: about 30% of eligible customers, close to 300 analyses a month [TR-DISCLOSURE-2026].
- MindBridge Agentic Risk Assessment for planning, launched 22 Sep 2026 [MINDBRIDGE-ARA-2026].
- DataSnipper claims more than US$1.4bn of customer productivity savings in 2025, method not given [DATASNIPPER-2026].
- Fieldguide raised US$75m at a US$700m valuation [FIELDGUIDE-2026].

**In-house.** Optro reports Reddit's internal audit team automated 175 controls, over 40% of its SOX scope, and cut
testing time per control by 60% in three months, and has since extended agents to over 75% of its SOX controls (single
customer, vendor-published) [OPTRO-CRX-2026]. More in-house
cases are in [controls-testing](modules/controls-testing.md).

## 4. How maturity is spread

| Tier | What the evidence shows | Typical stage |
|---|---|---|
| Global networks | Platform-wide agents announced; firm training programmes; certification processes at most of the six largest UK firms, some less mature; many tools held but few used on most audits [FRC-ATT-2025; IFIAR-TTF-2025] | Adopting to Scaling, varying by service line |
| Large national and PE-backed mid-tier | Own or adapted platforms (gtap) or licensed partners (RSM with Andera); PE capital partly sought for AI (Crowe, Eide Bailly) [GT-GTAP-2026; CFOBREW-PE-2026] | Experimenting to Adopting |
| Small and mid-size practices | Best proxy is the mixed-size 54-firm benchmark: no plan at 75%; Excel and Power BI the most used tools; blockers are training, client data, access and budget [CPACOM-ATR-2025] | Curious to Experimenting |
| Internal audit | Broad trials; some agent-based SOX testing; flat headcount; outside help for AI skills [GARTNER-2026; KPMG-NORDIC-2026; OPTRO-FOF-2026; OPTRO-CRX-2026] | Experimenting, with leaders at Adopting in controls testing |
| AI-native entrants | Repodo (Denmark), Oath Verified (US), Modus (invests in firms): announced starts, no market share or quality results [REPODO-2026; AT-PEEC-2026; MODUS-2026] | Claim AI-native; unproven |

- Thomson Reuters executives say adoption "has not been at the pace that many expected" because auditors are
  conservative (vendor interview) [TR-STATE-2026].
- The UK regulator launched a research project to build an evidence base on the barriers smaller firms face in adopting
  audit technology [FRC-SANDBOX-2026].
- In onboarding, use the stage markers in [ARCHETYPE.md](ARCHETYPE.md), not the tier, to place a specific firm.

## 5. Client-side maturity drives new work

- In the CAQ's Spring 2026 pulse, audit partners rated AI governance at their largest client as advanced in only 6% of
  cases; 40% developed but incomplete and 46% early stage [BOARDMEMBER-CAQ-2026; CAQ-PULSE-2026].
- AI governance was the top audit-committee challenge (57%), ahead of cybersecurity (51%); about two-thirds said the audit
  committee had raised AI use in operations or reporting [BOARDMEMBER-CAQ-2026].
- The AICPA's practice aid on AI (13 Oct 2026) covers how a client's AI affects risk assessment, data reliability, the
  team's capabilities and controls, as well as auditors' own AI use; the AICPA also issued guidance on service
  organisations' AI in SOC 1 and SOC 2 examinations [AICPA-PA-2026; DART-TQA-2026].
- This creates audit work regardless of the firm's own tools; see
  [assurance-over-ai](modules/assurance-over-ai.md) and [planning-risk-assessment](modules/planning-risk-assessment.md).

## 6. What is not measured

- Accuracy, error, override or false-positive rates of any audit AI tool in live use.
- Change in audit hours, fees, staffing mix or margin caused by AI at any firm.
- Lab benchmarks exist but are not practice evidence. An ICAEW test found three chatbots did not perform ISA 315 risk
  assessment as a human would [ICAEW-PIERPOINT-2025]. A September 2026 benchmark (FinancialAuditBench) was built by
  Modus, an AI audit vendor: six of its eight authors list Modus, which also supported the work. Its abstract says
  eleven frontier models complete substantial parts of staff-level workpaper tasks but sometimes perform inappropriate
  procedures or write incorrect documentation; the best model passed 69% of 90 tasks at first attempt [ARXIV-FAB-2026].
- Smaller-firm adoption outside the US 54-firm sample; non-Big Four platform details.

## 7. Using this in a conversation

- **Split every claim into three numbers:** who uses it, which workflows changed, what measure moved. "Everyone uses AI"
  usually means the first number only.
- **Quote with provenance.** Say "regulators see tools in most journal-entry testing files", not "88% of audits use AI".
- **For small firms**, start from the data-in steps that are already automated (confirmations, foot-and-proof,
  trial-balance import) and from a documented plan, not from agents (see [value-chain.md](value-chain.md) §4).
- **For internal audit**, the realistic frame is more coverage within a flat budget (see [economics.md](economics.md) §8).

## 8. Sources

Keys not listed here are in [sources.md](sources.md).

- **PWC-AT-2025**: Accounting Today, *PwC expects end-to-end AI audit automation within 2026* (press, 28 Oct 2025). https://www.accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026
- **TR-STATE-2026**: Thomson Reuters Tax and Accounting, *The state of AI in audit in 2026: Interview with experts* (vendor, 2026-03-30). https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/

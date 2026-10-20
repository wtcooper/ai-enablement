# State of AI in tax

Last researched 2026-10-17; figures are as published up to that date. Use this in onboarding to bring in one real
example early, in Frame to set a realistic baseline, and whenever a leader says "everyone else is already doing it".
Keep three things apart: what is **measured**, what is **announced**, and what is **forecast**. Source keys in brackets
resolve in §9 or in [sources.md](sources.md).

## Contents

1. [Headlines](#1-headlines)
2. [Measured adoption](#2-measured-adoption)
3. [What leaders are doing](#3-what-leaders-are-doing)
4. [Quality evidence that exists](#4-quality-evidence-that-exists)
5. [How maturity is spread](#5-how-maturity-is-spread)
6. [The tax authority's adoption](#6-the-tax-authoritys-adoption)
7. [What is not measured](#7-what-is-not-measured)
8. [Using this in a conversation](#8-using-this-in-a-conversation)
9. [Sources](#9-sources)

## 1. Headlines

- **Use is broad; measurement is thin.** Most surveys find a majority of tax professionals or functions using AI in
  some form, but few set targets: 92% of 176 indirect tax leaders use AI and 12.5% have specific AI targets or KPIs
  [FONOA-2026].
- **Agentic products shipped between late 2025 and mid 2026**, mostly from vendors (Thomson Reuters, Black Ore, Basis,
  Accrual, Avalara, Sovos) and the Big Four (EY, KPMG, PwC). Production evidence is mostly vendor-stated, and one
  4,500-return firm that evaluated five AI preparation vendors in 2026 said "no one is ready" [WCG-2026].
- **Independent accuracy evidence is scarce and unflattering.** Unaided frontier models computed fewer than a third of
  simplified federal returns correctly (2025 models) [COLUMN-TAXCALCBENCH-2025]; the best model scored 49% on a
  corporate tax research benchmark [VALS-TAXAGENT-2026].
- **Governance lags use.** More than a third of tax and audit professionals admit using unauthorized AI tools [TR-FOP-2026];
  in house, tax rarely owns AI implementation [TEI-TAXTECH-2026].
- **The counterparty is moving too.** The IRS had 126 active AI use cases in June 2025, up from 10 in 2022 [GAO-2026].
- **No regulator prohibits AI.** Every practitioner regulator found says existing duties apply ([guardrails.md](guardrails.md)).

## 2. Measured adoption

Read as published; samples and definitions differ, so do not average or trend across rows.

**Firms and professionals**

| Survey (who ran it) | Sample, date | Headline | Bias note |
|---|---|---|---|
| Future of Professionals, tax and audit (Thomson Reuters Institute) [TR-FOP-2026] | Jul 2026; subset size not stated | 81% use AI tools regularly; more than a third admit unauthorized tools | Vendor-owned |
| Tax software survey (AICPA) [AICPA-TAXSW-2026] | 1,808 members who prepared 2025 returns for a fee | 65% use AI in tax research; 16% have no plans (24.3% a year earlier); 93% use no tool to find planning opportunities in returns | Professional body |
| AI Tax Research Outlook (Blue J with CPA.com) [BLUEJ-OUTLOOK-2026] | 1,000 US accountants, spring 2026 | 60% work at firms that adopted AI tax research (33% in 2025, different sample) | Vendor-run |
| Tax firm deployment (Thomson Reuters-authored) [CPAPA-TR-2026] | 2026 | 34% of tax firms deploy GenAI at organization level (21% before); 19% of those measure ROI; 14% use agentic AI | Vendor-authored |
| Top Issues (AICPA PCPS) [AICPA-TOPISSUES-2026] | 629 practitioners, Apr-May 2026 | Technology change and AI adoption rank in the top two issues for five of six firm-size groups (third for firms of 2-10 staff); tax law complexity ranks first for solo and up-to-10-staff firms | Ranks concerns, does not measure use |

**In-house departments**

| Survey (who ran it) | Sample, date | Headline | Bias note |
|---|---|---|---|
| State of the Corporate Tax Department (Thomson Reuters) [TR-CORPTAX-2025] | 288 departments, 2025 (blog dated 22 Oct 2025) | 67% not using GenAI; of those implementing new technology, 57% plan GenAI and 17% "more advanced" such as agentic | Vendor-owned |
| AI in tax departments (KPMG Germany) [KPMG-DE-2026] | Quick surveys, May 2026; sample not stated | 71% use AI tools, 19% preparing; 89% use company-wide tools and 29% specialised tax applications; 66% of users report noticeable time savings | Big Four, one market |
| Tax and Finance Operations (EY) [EY-TFO-2025] | 1,600 CFOs and tax and finance leaders, 30 jurisdictions, Nov 2025 | 86% call data, GenAI and technology a top priority; 51% are early in data-management maturity; 44% name inability to execute a data, AI and technology plan as the biggest barrier | Big Four |
| Corporate tax technology (Thomson Reuters blog on its department data) [TR-UNDERSTAFF-2026] | US corporate tax departments; blog dated 23 Jul 2026 | 9% call themselves active AI users; 27% can secure budget when needed | Vendor-owned |
| Indirect tax in the AI era (Fonoa) [FONOA-2026] | 176 indirect tax leaders, Jun 2026 | 92% use AI in some form; 12.5% have targets; about a third run formal human review; 57.4% would not be confident defending AI-assisted decisions to an authority | Vendor-sponsored |

**Corrections to figures in circulation.** EY's own release gives 51% (early data maturity) and 44% (cannot execute the
plan); the "80% struggle with foundational data" and "75% in earliest stages" figures are not in it [EY-TFO-2025]. The
AICPA Top Issues result is "top two in five of six size groups", not "top issue in every band" [AICPA-TOPISSUES-2026].
The 2025 "67% not using" and the 2026 "71% using" describe different populations, not a trend [TR-CORPTAX-2025; KPMG-DE-2026].

## 3. What leaders are doing

| State | Examples (who says so) |
|---|---|
| **In production, per the organization** | PwC US: agents for K-1 data mapping and tax diagnostics "moving beyond pilots and into production" in a "human-reviewed, multi-eye process"; 800+ custom GPTs and 250+ agents firm-wide (interview, Jun 2025) [PWC-MEGNA-2025]. Savant announced a TEI session in which Oxford Industries would show how its tax team "deploys AI safely and at scale" (vendor announcement; no outcomes published) [SAVANT-2026]. H&R Block uses AI to remove manual data entry in pilot offices and will expand the model to a full market [HRB-Q4CALL-2026]. OpenAI's tax department showed live automation pipelines at TEI [TEI-TAXTECH-2026] |
| **Pilot or early adopter** | Thomson Reuters Ready to Review: early adopter programme; one firm said it cut about an hour from a simple 1040 [TR-COCOUNSEL-2025]. Black Ore: 75 firms in a two-year pilot before opening on 29 Apr 2026 [BLACKORE-2026]. OpenAI's Tax AI pilot with Crete firms: 7,000 1040 and 1041 returns (published by OpenAI, the co-developer) [OPENAI-CODEX-2026] |
| **Announced** | EY.ai Tax Labs and Tax Agent Factory (25 Nov 2025), with no deployment counts [EY-TAXLABS-2025]; KPMG Digital Gateway with Claude, tax clients first (20 May 2026) [KPMG-ANTHROPIC-2026]; RSM myRSM Tax on a US$1bn plan [RSM-MYRSM-2025]; Sovos MCP gateway "in development" [SOVOS-SOVI-2026] |
| **Roadmap** | Ready to Review support for K-1s and consolidated 1099s reported for November 2026 (WCG's account of a vendor conversation) [WCG-2026] |

**The most informative practice evidence is a sceptical adopter.** WCG (about 4,500 1040s, heavy on K-1s) found gaps in
K-1 and consolidated 1099 support, a "reset" risk when a return hits an exception on a proprietary platform, the
handoff into the firm's tax software, and prices of US$100-150 or more per return. One firm's published opinion, not a
study [WCG-2026].

## 4. Quality evidence that exists

- **Return calculation.** TaxCalcBench: unaided 2025 frontier models were correct on fewer than a third of simplified
  federal returns, misusing tax tables and misjudging eligibility; the authors sell a tax engine
  [COLUMN-TAXCALCBENCH-2025].
- **Research.** Vals Tax Agent Bench (updated 16 Oct 2026): best model 49.19% fully correct and citation-adjusted on 193
  corporate tax research questions [VALS-TAXAGENT-2026]. Older study: 39-47% of ChatGPT answers to common taxpayer
  questions correct (2023-24 models) [ANTINOZZI-2024].
- **Hybrid designs.** A Johns Hopkins prototype pairs a language model that translates statute into logic with a
  symbolic solver and treats auditability as the design requirement (research, not a product) [JHU-TAXREASON-2025].
- **Vendor accuracy claims** (definitions not published): Black Ore says accuracy above 99% across tens of thousands of
  pilot returns [BLACKORE-2026]; OpenAI says 86% of pilot returns reached 75% correct field completion after six weeks
  [OPENAI-CODEX-2026].
- **Failures on the record.** Fabricated citations reached the Tax Court (*Clinco*, an admonishment, no sanction)
  [TAXCT-CLINCO-2026]; the IRS withdrew two expert reports after AI-related errors were raised (*Riddle Aggregates*)
  [RIDDLE-TRANSCRIPT-2026]. TEI attendees describe AI that "fails quietly and even politely" [TEI-TAXTECH-2026].

## 5. How maturity is spread

| Group | Typical position | Evidence |
|---|---|---|
| Big Four | Firm platforms and agent factories announced or in production for named steps; selling agents to clients | [PWC-MEGNA-2025; EY-TAXLABS-2025; KPMG-ANTHROPIC-2026] |
| Mid-tier and PE-backed | Platform investment (RSM US$1bn; Grant Thornton Advisors US$1bn); offshore plus AI | [RSM-MYRSM-2025; GT-CBIZ-2026; IPA-OFFSHORE-2026] |
| Small firms and EAs | Research tools and assistants; evaluating agentic preparers; tax law complexity still the top issue for the smallest | [AICPA-TAXSW-2026; WCG-2026; AICPA-TOPISSUES-2026] |
| AI-native entrants | Software sold to firms (Black Ore, Basis, Accrual) or roll-ups running bought practices on AI (Multiplier, Crete) | [BLACKORE-2026; MULTIPLIER-2025; CRETE-REUTERS-2025] |
| In-house departments | Company-wide assistants first, specialised tax tools second; data and ownership the binding constraints | [KPMG-DE-2026; EY-TFO-2025; TEI-TAXTECH-2026] |
| Indirect tax functions | High reported use, few targets, low confidence defending AI decisions | [FONOA-2026] |

KPMG's readiness survey of 2,084 senior leaders finds most organizations in "the early or mid-stages of tax readiness"
(its own index) [KPMG-READINESS-2026]. Use [ARCHETYPE.md](ARCHETYPE.md) journey markers to place a scope, not these tiers.

## 6. The tax authority's adoption

- 70% of 54 OECD Forum on Tax Administration members use AI tools (2024 data) [OECD-DIGIT-2025].
- IRS: 126 active use cases in June 2025, 65 withheld as sensitive or exempt; the AI skills base eroded after 2025 staff
  cuts and there is no AI workforce plan [GAO-2026]. The IRS CEO calls for an "AI-first IRS" and sees a mid-90s
  compliance rate in five years, against about 85% now (a forecast); headcount held flat near 74,000 through 2026
  [IRS-AIFIRST-2026].
- HMRC says AI and advanced analytics enabled it to protect and recover GBP 10 billion in 2025-26
  (self-reported; method not published) [HMRC-ARA-2026]; its roadmap targets
  90% digital interactions by 2030 and names agentic case management [ICAS-HMRC-2025].
- Detail and practitioner implications are in [controversy](modules/controversy.md).

## 7. What is not measured

- Production error, override or parallel-run rates for any agent-prepared return, provision, filing or memo.
- Review time and rework on AI-assisted work at any named firm or department.
- Fee or margin change on the same tax work after AI adoption ([economics.md](economics.md) §7).
- Independent head-to-head tests of commercial tax preparation or research products.
- In-house case studies with named metrics; practitioner community data (forums were unreachable).

## 8. Using this in a conversation

- Lead with one example from the leader's focus module and its grade, then say who published the figure.
- When a leader cites a vendor percentage, ask for the customer's own baseline and a parallel run on last year's work.
- When a leader says "everyone is doing it", separate use (high) from targets, measurement and ownership (low).
- Point in-house leaders to the authority side: their counterparty may be further ahead on data than they are
  [DELOITTE-TTT-2026].

## 9. Sources

Keys not listed here are in [sources.md](sources.md).

- **ANTINOZZI-2024**: Antinozzi and Cooper (Wealth Strategies Journal posting), *Is ChatGPT an Accurate Source of Information for Uninformed Taxpayers?* (academic, 2024-06-18). https://wealthstrategiesjournal.com/2024/06/30/hannah-smith-antinozzi-lauren-cooper-is-chatgpt-an-accurate-source-of-information-for-uninformed-taxpayers-june-18-2024/
- **CPAPA-TR-2026**: CPA Practice Advisor, *The Real AI Story in Tax and Audit Isn't Adoption: It's Impact (Thomson Reuters-authored piece)* (press, 2026-04-21). https://www.cpapracticeadvisor.com/2026/04/21/the-real-ai-story-in-tax-and-audit-isnt-adoption-its-impact/181846/
- **HRB-Q4CALL-2026**: H&R Block (transcript via earningswhispers.com), *H&R Block Q4 fiscal 2026 earnings call transcript* (firm, 2026-08-11). https://earningswhispers.com/transcript/HRB/Q42026
- **KPMG-READINESS-2026**: KPMG, *2026 KPMG Global Tax Readiness Dividend* (survey, 2026). https://kpmg.com/xx/en/our-insights/transformation/global-tax-readiness-dividend.html
- **OECD-DIGIT-2025**: Bloomberg Tax, *Tax Authorities Increasingly Use AI in Audits, OECD Report Finds (OECD FTA digitalisation report, 2024 data)* (press, 17 Jun 2025). https://news.bloombergtax.com/daily-tax-report/tax-authorities-increasingly-use-ai-in-audits-oecd-report-finds

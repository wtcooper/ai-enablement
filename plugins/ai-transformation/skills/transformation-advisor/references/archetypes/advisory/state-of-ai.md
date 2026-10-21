# State of AI in advisory

Last researched 2026-10-21; figures are as published between 2025 and October 2026. Use this in onboarding (bring
evidence in early) and in Frame. It says who measured each figure. Module files hold the step-level evidence. Source
keys in brackets resolve in [sources.md](sources.md).

## Contents

1. [Headlines](#1-headlines)
2. [Practitioner surveys](#2-practitioner-surveys)
3. [The client side](#3-the-client-side)
4. [What leaders are doing](#4-what-leaders-are-doing)
5. [Quality evidence that exists](#5-quality-evidence-that-exists)
6. [How maturity is spread](#6-how-maturity-is-spread)
7. [What is not measured](#7-what-is-not-measured)
8. [Using this in a conversation](#8-using-this-in-a-conversation)

## 1. Headlines

- **Use is near-universal; embedding is not.** Vendor-run practitioner surveys put AI use at 88-98% of firms, but 30%
  say AI is embedded as the default and 21% have an AI policy or strategy [INTUIT-ACCTTECH-2026; KARBON-SOAI-2026].
  The gap between use and an owned, reviewed workflow is the main stage discriminator.
- **The same gap exists on the client side.** Among AI-using middle-market companies, 86% have integrated AI at least
  partly and 36% have it fully embedded in core processes [RSM-MMAI-2026; CPAPA-RSMMM-2026].
- **CAS has the most evidence and the only grade A.** An independent field study links genAI use in SME bookkeeping
  with a shorter close and more granular ledgers (associations) [STANFORD-JAR-2026]. Most other figures are vendor
  benchmarks or small-firm case studies.
- **Agents are in production in internal audit, mostly in-house.** Named in-house teams hand defined control tests to
  agents; firms are now running agents in co-sourced work (risk-controls `#05`, `#06`).
- **Deals, valuation, forensic, FP&A and private client are announcement-heavy.** Usage counts (PwC, Deloitte),
  alliances and launches, with no measured outcome from a named firm (transactions, valuation, forensic-disputes,
  fpa-performance and private-client modules, §5).
- **Nobody publishes quality data.** No firm, platform or regulator has published an error, override or parallel-run
  rate for AI-assisted advisory work.

## 2. Practitioner surveys

All are sponsored by vendors or firms, and respondent pools skew toward adopters.

| What it measures | Result | Who measured, when, sample |
|---|---|---|
| Firms using AI; with a policy or strategy | 98%; 21%; about 60 minutes a day saved per employee (self-reported) | Karbon, released January 2026, about 600 respondents [KARBON-SOAI-2026] |
| AI for at least one client service; embedded as default; situational | 88%; 30%; 54%; 77% say the gap between embedded and occasional firms is widening | Intuit QuickBooks, May 2026, 725 US accounting and bookkeeping professionals [INTUIT-ACCTTECH-2026] |
| Top advisory blockers | Manual data cleanup 30%, staffing shortages 24%, app overload 16% | Same [INTUIT-ACCTTECH-2026] |
| GenAI use; integrated across operations | 56%; 10%; data security the top client-facing concern (39%) | Ramp with CalCPA, 2026, 400+ California professionals (landing page) [RAMP-CALCPA-2026] |
| AI for tax research weekly; advisory projects as the top use | 60% (33% in 2025); 44% | Blue J with CPA.com, June 2026, 1,000+ US tax professionals [CPACOM-BLUEJ-2026] |
| Professionals using AI weekly; organisation falls short of AI's potential | 74%; 91% | Thomson Reuters Institute, March-April 2026, 1,816 professionals in 62 countries [TR-FOPPR-2026] |
| Use of AI their organisation has not approved | 34% | Same survey, report page [TR-FOPREPORT-2026] |
| AI the top ethical challenge | 61% (32% in 2024) | ACCA, October 2026, 1,178 in 135 countries [ACCA-ETHICS-2026] |
| Internal audit: any AI use; for pre-planning; for testing | 93%; 60%; 30% | Gartner poll of 743 audit professionals, as reported [ACCTIMES-GARTNER-2026] |
| Anti-fraud: AI or ML in analysis; genAI as a tool; plan to adopt genAI | 25% (18% in 2024); 16%; 58% | ACFE with SAS, March 2026, 713 respondents [ACFE-TECHBENCH-2026] |
| FP&A: genAI in forecasting; ML in forecasting | 21%; 12% | FP&A Trends survey sponsored by OneStream, July 2026, 475 respondents [ONESTREAM-FPATRENDS-2026] |
| Dealmakers: AI regularly embedded in diligence | 50% | Datasite, July 2026, 1,000 dealmakers [DATASITE-NEWDEALTEAM-2026] |
| Valuation practitioners expecting AI to change their work "significantly" | 73%, with usage low (sample not visible) | BVR polls, 2025, summary only [BVR-POLLS-2025] |
| Family offices using AI for operations or investment analysis | 22% (13% in 2024) | Citi, 2025 report, sample not on the page [CITI-AIFO-2026] |

**Reading these.** Each survey asks a different question; do not add them up or rank firms against them. The
Thomson Reuters release and report page give slightly different client-side figures, so cite the release
([§3](#3-the-client-side)).

## 3. The client side

| What it measures | Result | Who measured, when, sample |
|---|---|---|
| Middle-market AI integration | 86% partly or fully integrated; 36% fully embedded; 54% say AI exceeded ROI expectations | RSM, March 2026, 1,030 AI-using leaders in the US and Canada (RSM sells consulting) [RSM-MMAI-2026; CPAPA-RSMMM-2026] |
| Barriers to scaling | Data quality 34%, security and privacy 30%, legacy integration 28%, talent 28% | Same [RSM-MMAI-2026; CPAPA-RSMMM-2026] |
| Large-company finance: active AI use | 30% (2024) to 75% (March 2026); 71% say AI meets or exceeds ROI expectations | KPMG, 1,013 finance leaders, revenue $250M+ [KPMG-AIFINANCE-2026] |
| Assurance readiness | 42% fully assurance-ready; 29% track where AI adoption fails; error-reduction improvement 33% vs 6% for assurance-ready organisations | Same [KPMG-AIFINANCE-2026] |
| Finance AI implementation slower than expected | 63% in 2025; forecasting among the lowest-rated uses | Gartner [GARTNER-AIREPORTCARD-2026] |
| Clients' view of providers | 78% rate AI-enabled quality very important or essential; 6% say most providers deliver it; 32% will reconsider relationships within 12 months | Thomson Reuters, June 2026 (legal and accounting) [TR-FOPPR-2026] |
| Clients asking accountants for proof of AI data protection | Three in five say always or frequently; 33% of firms explain AI use proactively | Accountants' view of their clients [INTUIT-ACCTTECH-2026] |

What it means: clients are deploying faster than they are assuring, which is the demand behind the risk-controls
module's AI governance work, and buyers are moving some first-pass work in house (transactions `#13`).

## 4. What leaders are doing

Status words are the sources' own. "Announced" is not "in production".

| Who | What | Status | Source |
|---|---|---|---|
| RSM (top-10 mid-market) | $1B multiyear AI and digital-core investment; Microsoft 365 Copilot to nearly 20,000 professionals | Firm-reported | [RSM-IMPACT-2026] |
| RSM | Beacon, an AI-guided internal-audit testing platform with Andera | Announced as live, 2026-08-28 | [ACCTODAY-RSMBEACON-2026] |
| Grant Thornton Advisors (PE-backed) | $1B over three years; Copilot to 13,500+ people; "as many as seven tools each quarter" | Announced; CEO statement | [GT-1B-2025; GT-CBIZ-2026] |
| CBIZ | Agent-native operating platform on Microsoft Foundry; training for 9,500+ | Announced | [CBIZ-MICROSOFT-2026] |
| CLA (Top 20) | Firm-trained model with Digits for its CAAS practice, rolling out over three years | Announced | [ACCTODAY-CLA-2026] |
| Cherry Bekaert, Aprio, Protiviti | Fieldguide as agentic platform for internal-audit and risk work | Committed in 2026 | risk-controls `#06`, `#13` |
| Forvis Mazars Group | Opio FDD workbench rolled out across several countries after a nine-month pilot | Rolled out, 2026-09-25 | [FORVISGROUP-OPIO-2026] |
| PwC Deals | ToltIQ data-room tool: 4,000+ practitioners, 5,000+ deals | Self-reported usage | [PWC-TOLTIQ-2026] |
| Deloitte | M&A platform with an agent harness, in 1,000+ client engagements | Self-reported usage | [DELOITTE-MAPLATFORM-2026] |
| CohnReznick | Valuation practice builds 73 Strings' AI-enabled analytics into its methodology | Firm release, no figures | [COHNREZNICK-VALUATION-2026] |
| Stout; Kroll | Recurring valuation platforms (Drivr; REVS) | Announced | [STOUT-DRIVR-2026; KROLL-REVS-2026] |
| J.S. Held (forensic, not a CPA firm) | AI-assisted data preparation and tracing case studies | Self-reported narratives | [JSHELD-AIFRAUD-2026] |
| Citrin Cooperman | Acquired AI implementation firm Rosetree for middle-market work | Effective 2026-10-01 | [ACCTODAY-ROSETREE-2026] |
| PKF O'Connor Davies | Collaboration with Asseta AI for family-office modernization | Announced | [PKF-ASSETA-2026] |

Firm moves of this kind sit beside AI-native providers and vendors (Pilot, Basis, Petual, QoEAgent) and a failure
(Botkeeper). See
[disruption.md](disruption.md) §3.

## 5. Quality evidence that exists

- **Independent and measured (associations).** Choi and Xie (Journal of Accounting Research, June 2026): survey of 277
  accountants plus platform data on 79 SMEs and 200,000+ transactions. GenAI use is associated with productivity
  gains, a shift from data entry to communication and quality assurance, more granular ledgers and faster close; a
  framed experiment found relying on non-consensus AI recommendations can raise error risk [STANFORD-JAR-2026]. The
  CAS module gives the effect sizes and limits (`#01`).
- **Vendor and third-party benchmarks.** Digits, Mercor, Penrose and DualEntry test models on accounting tasks; Penrose
  saw balances drift more than 15% after several months unattended (CAS module §5) [PENROSE-ACCTBENCH-2025].
- **Adjacent independent evidence.** E-discovery review data and federal judges' survey results (forensic module §5);
  legal AI research tools hallucinating 17-33% of the time [STANFORD-LEGALAI-2024].
- **Failure cases.** A Deloitte Australia government report with AI-generated errors, after which Deloitte agreed to
  repay the final instalment [CITYAM-DELOITTE-2025]; a court that re-ran an expert's Copilot queries and got different
  numbers [GOLDMAN-WEBER-2024].

## 6. How maturity is spread

| Group | Typical position | Evidence |
|---|---|---|
| Big Four and top-10 platforms | Scaling platforms and firmwide assistants; usage counts published, outcomes not | RSM, Deloitte, PwC rows in §4 |
| PE-backed and mid-market firms | Committing to one agentic platform per practice; buying AI capability | Fieldguide commitments; Citrin and Rosetree; GT and CBIZ |
| Small and solo firms | Most named results, usually in vendor case studies on AI-native ledgers | CAS module §5 (Elev8, TFMA, Arclow) |
| AI-native providers | Selling direct or supplying firms; results company-stated | CAS `#16`; risk-controls `#15`; transactions `#05` |
| In-house teams | Internal audit often further along than its outside providers | risk-controls `#05`, `#14` |

By module: CAS and risk-controls have named deployments; transactions and forensic have usage counts and
self-reported narratives; valuation, FP&A and private client have mostly announcements and ideas (module tables in
[ARCHETYPE.md](ARCHETYPE.md)).

## 7. What is not measured

- Error, override, rework or parallel-run rates for any AI-assisted advisory deliverable.
- Fee, realisation or margin changes attributable to AI at any firm.
- Whether CAS clients convert into advisory clients, and at what fee.
- AI-native providers' share of middle-market accounting spend.
- Adoption specific to transaction advisory, forensic or private-client teams at accounting firms; no survey found.
- The 2026 CAS Benchmark Survey report, due December 2026, may give the first CAS technology dataset
  [CPACOM-CASBENCH-2026].

## 8. Using this in a conversation

- Lead with the gap, not the headline: "Most firms say they use AI; about a third say it is the default. Where are you?"
- Say who measured a figure: most are vendors surveying their own users.
- Offer the one independent study for CAS, and say plainly that the other modules have none.
- When a leader quotes a vendor speed-up, ask whether anyone reproduced it on their own clients' data.

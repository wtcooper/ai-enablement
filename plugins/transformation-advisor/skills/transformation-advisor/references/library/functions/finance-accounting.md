# Finance and accounting

Function id `finance-accounting`. Last reviewed 2026-10-20. Source keys in brackets are listed in §8. **Read this first:** adoption
is broad but shallow. In Gartner's 2025 survey of 183 finance leaders, 59% of finance functions use AI and 91% report low or moderate
impact initially [GARTNER-2025]. The best measured in-house evidence is step-level (minutes per reconciliation, dollars recovered by
screening). No named in-house team publishes override, escalation or error rates for finance AI; COSO's guidance names override
percentages as a monitoring indicator but gives no benchmark [DELOITTE-DART-2026].

## Contents

1. [What this function covers](#1-what-this-function-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Metrics and benchmarks](#4-metrics-and-benchmarks)
5. [Interview probes](#5-interview-probes)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Sources](#8-sources)

## 1. What this function covers

The in-house finance function of any organization: payables, receivables, close and reporting, planning and forecasting, treasury,
and the controls around payments. Firms that sell accounting, audit or tax work are covered by the assurance, tax and
professional-services archetypes; a firm's own billing and economics are in the professional-services `billing-collections` and
`firm-finance` modules. Tax work inside a company routes to the tax archetype.

## 2. Processes and key steps

The process list is a working grouping, not a named framework's categories.

| Process | Key steps | Work types | Typical pain |
|---|---|---|---|
| Procure-to-pay (payables) | Invoice capture and coding; match to order and receipt; approval; exceptions; payment run | transaction-processing, review-assurance | Impersonation and payment fraud: $2.77 billion in business email compromise losses reported to the FBI in 2024 [FBI-2025] |
| Order-to-cash (receivables) | Billing; cash application; disputes; collections follow-up | transaction-processing, client-interaction | Reconciliation across systems and spreadsheets; reconciliation was a top Microsoft finance use case [CFODIVE-2024] |
| Record-to-report (close) | Journals and accruals; reconciliations; intercompany; consolidation; variance review; disclosures | data-reporting, review-assurance, document-production | A vendor argues task-level AI gains did not shorten the close because the days sit in handoffs (vendor blog) [KOGNITOS-2026] |
| Planning, budgeting, forecasting | Driver models; rolling forecasts; variance commentary; scenarios | data-reporting, expert-judgment | Data literacy, skills, data quality and availability are the largest adoption obstacles (survey) [GARTNER-2025] |
| Treasury | Cash positioning and forecasting; FX exposure and hedging; payments | data-reporting, coordination-scheduling, transaction-processing | About 180 forecasters submitting monthly, called "extremely painful and inaccurate" by one treasury lead [NEUGROUP-2025] |
| Controls and payment integrity | Control testing; segregation of duties; payment authorization and verification; fraud screening | review-assurance, transaction-processing | Verifying AI output: an average 26% of work time, in a vendor survey of 270 US finance leaders [DATARAILS-2026] |

## 3. Where AI is changing the work

**Improve the step** (assist or augment)

- **Policy, standards and procedure questions** ([grounded-knowledge-assistant](../patterns/grounded-knowledge-assistant.md); assist;
  step). Knowledge management is the most common finance use case among adopters, 49% (survey) [GARTNER-2025]. No measured named
  deployment found. Grade C.
- **Reconciliation and working the breaks** ([reconcile-exceptions](../patterns/reconcile-exceptions.md); augment; step). Microsoft
  finance (technology): receivables reconciliation saved an average 20 minutes per account; an FP&A team's weekly reconciliation fell
  from 1-2 hours to 10 minutes. Self-reported internal results shared with a journalist; method unpublished; Microsoft also sells
  the tool. Grade A [CFODIVE-2024].
- **Variance analysis and commentary** ([draft-review-loop](../patterns/draft-review-loop.md); augment; step). Microsoft finance was
  testing it with "promising results so far"; no figure. Grade B [CFODIVE-2024].
- **Analysts writing their own automations with code generation** ([bulk-transformation](../patterns/bulk-transformation.md);
  assist; step). Ranked highest for impact by finance leaders (survey). Grade C [GARTNER-2025].
- **Transaction classification and a faster close** ([bulk-transformation](../patterns/bulk-transformation.md); augment; process).
  79 small and mid-sized firms using AI accounting tools (accounting services): month-end statements finalized 7.5 days faster and
  8.5% less time on routine back-office work. Independent academic study of platform data; adopters may differ from non-adopters;
  services firms, not in-house teams. Grade B [STANFORD-2025].

**Automate the flow** (no person on the normal path)

- **Payables automation, anomaly and error detection** ([full-population-testing](../patterns/full-population-testing.md),
  [intake-triage](../patterns/intake-triage.md); automate; process). Used by 37% and 34% of adopters (survey). Grade C [GARTNER-2025].
- **Payment-integrity screening** ([monitor-diagnose-act](../patterns/monitor-diagnose-act.md); automate; step). US Treasury, Office
  of Payment Integrity (public sector): over $4 billion prevented and recovered in FY2024, against $652.7 million in FY2023; $1 billion
  of recovery credited to machine learning that identifies check fraud. Self-reported; method not published. Grade A [TREASURY-2024].
- **Cash and FX forecasting from data instead of submissions** ([monitor-diagnose-act](../patterns/monitor-diagnose-act.md);
  automate; process). AIA Group Treasury (insurance), a pilot in some markets: "up to 90% more accurate forecasts on specific cash flow items", a
  self-reported statement with no denominator. Grade B [TREASURYTODAY-2024]. An unnamed mega-cap treasury ran legacy and machine-learning forecasts in
  parallel for about seven months, then "reverse parallel" for three, and reports about 25% better accuracy (statements at a peer-group
  meeting). Grade C (organization unnamed) [NEUGROUP-2025].

**Delegate the outcome** (an agent owns a multi-step outcome)

- **Agent runs close steps end to end, with deterministic checks between steps**
  ([end-to-end-case-agent](../patterns/end-to-end-case-agent.md); delegate; process). Argued in a vendor blog [KOGNITOS-2026]; in KPMG's
  survey of 1,013 finance leaders, organizations deploying agentic AI report stronger performance on key finance metrics, a perception
  measure [KPMG-2026]. No named deployment. Grade C. On a third-party benchmark of 537 entry-level analyst questions, the top agent scored
  64.37% as of 2026-06-04 (evaluation, not deployment; grade D) [VALS-2026].

**Reinvent the work** (operating model changes)

- No cross-industry measured example in finance. The closest are in-house tax operating models in the tax archetype:
  `tax-data-technology-22` (B) and `tax-compliance-corporate-07` (B).

**In the archetypes**: `professional-services-billing-collections-13` (B, in-house review of every outside-counsel invoice),
`professional-services-firm-finance-04` (B), `professional-services-firm-finance-11` (B, governing usage-based AI spend),
`tax-data-technology-01` (B), `tax-data-technology-08` (B, automations run as controlled assets), `tax-data-technology-09` (B),
`tax-indirect-tax-20` (B), `security-human-risk-06` (C, deepfake drills for finance staff).

## 4. Metrics and benchmarks

- **Adoption and impact:** 59% of finance functions use AI (58% in 2024, 37% in 2023); 91% low or moderate impact initially; those
  further along were over two times more likely to see moderate impact (survey of 183 leaders, Gartner) [GARTNER-2025]. In KPMG's 2026
  survey, 71% say AI meets or exceeds ROI expectations in finance (perception measure) [KPMG-2026].
- **Close:** 7.5 days faster and a 12% rise in reporting granularity among 79 firms (independent) [STANFORD-2025]. An APQC median of
  about 6.4 days from trial balance to consolidated statements is quoted second-hand by a vendor and was not checked [KOGNITOS-2026].
- **Forecast accuracy:** average variance to actuals under 10% across 14 hedged currencies at 12-18 months, as low as 5% for some
  (statements by a treasury manager, organization unnamed) [NEUGROUP-2025].
- **Review load:** 26% of work time verifying or correcting AI output; 96% spend at least 10% (vendor survey of 270 leaders at US
  organizations with $100 million+ revenue) [DATARAILS-2026].
- **Trust:** 14% of 100 mid-market US CFOs completely trust AI to deliver accurate accounting data on its own; 86% report at least
  one inaccurate or hallucinated output (vendor-commissioned) [WAKEFIELD-2026].
- **Control monitoring:** transaction volume, transaction size and override percentages, per commentary on COSO's 2026
  publication [DELOITTE-DART-2026].
- **Fraud exposure:** 21,442 business email compromise complaints and $2,770,151,146 in reported losses in 2024 (complaints to the
  FBI, not all incidents) [FBI-2025].

## 5. Interview probes

1. "Show me days-to-close and manual journals for the last six closes. Where does the clock stop between steps?" Reveals whether the
   constraint is task time or handoffs [KOGNITOS-2026, a vendor argument to test against the user's data].
2. "For each reconciliation, how many items match without a person, and how many breaks does a person clear?" Reveals the baseline
   for `reconcile-exceptions` and who owns the exception queue [CFODIVE-2024].
3. "How much of your team's week goes on checking AI output today?" Reveals hidden review load [DATARAILS-2026].
4. "Who releases a payment, and what happens when a request arrives with new bank details or an urgent instruction from a senior
   person on a video call?" Reveals whether payment authorization resists impersonation [CNN-2024; FBI-2025].
5. "What would you run in parallel before switching, for how long, and who decides it passed?" Reveals readiness to prove quality
   (seven months parallel, three months reverse parallel in one treasury) [NEUGROUP-2025].
6. "Do juniors and seniors review AI output differently?" Reveals rubber-stamp risk: juniors accepted outputs flagged as uncertain
   more often [STANFORD-2025].
7. "Which control in your ICFR inventory would an AI step touch, and who tracks override rates?" Reveals control ownership
   [DELOITTE-DART-2026].
8. "Is your data in one governed place or in spreadsheets?" Reveals data readiness, the top barrier in Gartner's survey [GARTNER-2025].
9. "Where will the hours released go, and who decided?" Reveals whether capacity has a destination; in one vendor survey 60% redeploy
   staff to higher-value work [DATARAILS-2026].
10. "In a design that runs several steps in sequence, which steps does the AI interpret and which does software execute by rule?"
    Reveals compounding-error exposure; the vendor's arithmetic (0.85 to the tenth power is about 19.7%) is an illustration, not a
    measurement [KOGNITOS-2026].

## 6. Guardrails

- **Internal control over financial reporting.** COSO's February 2026 publication extends its 2013 framework to generative AI with a
  six-step roadmap (govern, inventory, assess, design, implement, monitor); Deloitte's commentary says "set-and-forget" does not work
  when generative AI is used in financial reporting [DELOITTE-DART-2026; JOA-2026].
- **Payment release and bank-detail changes stay under a person's control** (advisor rule drawn from the incidents). Arup's finance
  worker paid HK$200 million (about $25.6 million) in 15 transactions after a video call with deepfaked colleagues [CNN-2024]; the FBI
  lists virtual meeting applications among channels fraudsters compromise [FBI-2025].
- **Accounting judgments stay with people:** estimates, policy choices and final sign-off. Co-author Jung Ho Choi, quoted in
  Stanford's write-up, says the "final judgment call" is still a human decision; seniors step in when system confidence drops
  [STANFORD-2025].
- **Risk frameworks:** NIST AI RMF 1.0 and its Generative AI Profile [NIST-AIRMF-2023; NIST-AI600-1-2024].
- **EU AI Act:** Annex III lists AI that evaluates the creditworthiness of natural persons as high-risk, excluding AI used to detect
  financial fraud; most internal finance work is not on the list, consumer-credit work is [EU-AIACT-ANNEX3-2024].
- **Decisions that need human judgment:** payment release; accounting estimates and policy; approval of journals above threshold;
  sign-off on reported numbers; the switch from a legacy forecast after a parallel run.

## 7. Roles and how they evolve

- **Accountants** spent 8.5% less time on routine back-office work; the write-up says they can redirect that time toward business
  communication, quality assurance and client-facing advisory work (accounting services firms) [STANFORD-2025].
- **Seniors become reviewers of AI output;** juniors gained less and accepted flagged outputs more often [STANFORD-2025].
- **Capacity:** in a vendor survey, 60% of respondents are redeploying employees to higher-value work and 3% are cutting finance staff
  because AI replaced work [DATARAILS-2026].
- **Talent mix:** 38% are upskilling existing finance teams and 28% are hiring for different skill sets; KPMG reads this as
  retraining people in place rather than rethinking the talent mix [KPMG-2026].
- **Process owners** set override and parallel-run rules and own the exception queue (advisor reading of the control guidance above).

## 8. Sources

- **CFODIVE-2024**: CFO Dive, *Microsoft finance team uses Copilot* (press, 2024-09-17). https://www.cfodive.com/news/microsoft-finance-copilot-generativeai-software/727176/
- **CNN-2024**: CNN Business, *British engineering giant Arup revealed as $25 million deepfake scam victim* (press, 2024-05-16). https://edition.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk
- **DATARAILS-2026**: CFO Dive on a Datarails survey, *AI verification eats up 26% of finance teams' workweek* (vendor survey, 2026-10-06). https://www.cfodive.com/news/ai-verification-eats-26percent-finance-teams-workweek-datarails/832210/
- **DELOITTE-DART-2026**: Deloitte DART, *COSO Releases Publication on Internal Controls Related to Generative AI* (firm commentary, 2026-04-03). https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai
- **EU-AIACT-ANNEX3-2024**: Regulation (EU) 2024/1689, *Annex III: High-risk AI systems* (regulation text via artificialintelligenceact.eu, 2024). https://artificialintelligenceact.eu/annex/3/
- **FBI-2025**: FBI Internet Crime Complaint Center, *2024 IC3 Annual Report* (regulator, 2025). https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf
- **GARTNER-2025**: Gartner, *Finance AI Adoption Remains Steady in 2025* (survey release via CPA Practice Advisor, n=183, 2025-11-18). https://www.cpapracticeadvisor.com/2025/11/18/gartner-survey-shows-finance-ai-adoption-remains-steady-in-2025/173371/
- **JOA-2026**: Journal of Accountancy, *COSO creates audit-ready guidance for governing generative AI* (professional body, 2026-02-26). https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/
- **KOGNITOS-2026**: Kognitos, *Why AI Hasn't Shortened Your Month-End Close* (vendor blog, 2026-08-19). https://www.kognitos.com/blog/why-ai-has-not-shortened-the-month-end-close/
- **KPMG-2026**: KPMG International, *Global AI in Finance 2026* (survey, n=1,013, 2026-06). https://assets.kpmg.com/content/dam/kpmgsites/kz/pdf/2026/06/AI-in-Finance-ENG.pdf
- **NEUGROUP-2025**: NeuGroup, *Working Cash Flow Forecast Magic With Data Wizards and ML Models* (peer-group community, 2025-09-24). https://connect.neugroup.com/public/blogs/working-cash-flow-forecast-magic-with-data-wizards-and-ml-models
- **NIST-AIRMF-2023**: NIST, *AI Risk Management Framework 1.0* (standard-setter, 2023-01). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **NIST-AI600-1-2024**: NIST, *AI RMF: Generative AI Profile* (standard-setter, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **STANFORD-2025**: Stanford GSB Insights on Choi and Xie, *AI Is Reshaping Accounting Jobs by Doing the "Boring" Stuff* (academic, 2025-06-26). https://gsb.stanford.edu/insights/ai-reshaping-accounting-jobs-doing-boring-stuff
- **TREASURY-2024**: US Department of the Treasury, *Enhanced Fraud Detection Processes, Including Machine Learning AI, Prevented and Recovered Over $4 Billion in Fiscal Year 2024* (government release, 2024-10-17). https://home.treasury.gov/news/press-releases/jy2650
- **TREASURYTODAY-2024**: Treasury Today, *Best Cash Flow Forecasting Solution Winner: AIA* (press, 2024-01). https://treasurytoday.com/?p=93746
- **VALS-2026**: Vals AI, *Finance Agent v1.1 Leaderboard* (third-party benchmark, updated 2026-06-04). https://www.vals.ai/benchmarks/finance_agent
- **WAKEFIELD-2026**: CFO Dive on Wakefield Research for Maximor AI, *CFOs insist on human oversight for AI in accounting* (vendor-commissioned survey, 2026-01-28). https://www.cfodive.com/news/massive-trust-gap-hinders-cfo-ai-ambitions-study-finds/810786/

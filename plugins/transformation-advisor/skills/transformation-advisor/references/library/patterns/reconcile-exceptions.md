# Pattern: reconcile-exceptions

Matches records across sources and works the breaks. Read this when an option compares two or more lists, ledgers
or record sets and chases the differences. Keys in brackets are listed in §11. Lines marked *(guidance)* are design
advice, not findings from a source.

## Contents

1. [What it is](#1-what-it-is)
2. [Where it fits](#2-where-it-fits)
3. [Up the ladder](#3-up-the-ladder)
4. [How it is built](#4-how-it-is-built)
5. [Prerequisites](#5-prerequisites)
6. [Failure modes and controls](#6-failure-modes-and-controls)
7. [Value and metrics](#7-value-and-metrics)
8. [Governance](#8-governance)
9. [Evidence](#9-evidence)
10. [Probes](#10-probes)
11. [Sources](#11-sources)

## 1. What it is

The system matches records across sources, clears what matches, classifies and explains the breaks, proposes
resolutions, and sends unresolved breaks to a named person. It is often rules first and AI second: a retailer
auto-matches 99.6% of transactions with rule-based matching and rejected an AI vendor as unproven
[BLACKLINE-BEAUTYPIE-2026]. Models add most where keys are messy: zero-shot GPT-4 beat the best fine-tuned
entity-matching baseline on three of six benchmarks and trailed it on the other three [PEETERS-ENTITYLLM-2024].
The exception queue is where both the value and the risk sit.

**How to recognize it** *(guidance)*: "we compare two lists and chase the differences"; "the close is late because
of unreconciled items"; "we sample because we cannot check everything"; "a few analysts know why things break".

## 2. Where it fits

- **Work types:** `transaction-processing`, `data-reporting`.
- **Shapes seen:** bank, e-commerce and ERP three-way matching [BLACKLINE-BEAUTYPIE-2026]; bank reconciliation at volume [HIGHRADIUS-KONICA-2025]; small-business bank feeds [DIGIT-XERO-2026]; trade breaks [NASDAQ-BROADRIDGE-2019]; client-money reconciliation [FCA-CASS715-2026]; benefit-to-tax-record matching, as a warning [ROBODEBT-RC-2023].
- **Not when rules already clear about 99% and the long tail is small** [BLACKLINE-BEAUTYPIE-2026].
- **Not to turn mismatches directly into demands on people** [ROBODEBT-RC-2023].
- **Not to reconcile against the counterparty's record where rules require your own books** [FCA-CASS715-2026].
- **Not to auto-write off differences without a policy owner** *(guidance)*.
- **Not if auto-match rate is the only success measure**; no published case reports its false-match rate.

## 3. Up the ladder

| Rung | What the AI does | What the person does | Runtime class | Checkpoint before moving up |
|---|---|---|---|---|
| `assist` | Explains a break or drafts a matching rule on request | Traces and clears breaks | `personal-assistant` | Break reasons coded; book of record stated |
| `augment` | Proposes matches and break reasons; lower-confidence items stay suggestions [DIGIT-XERO-2026] | Confirms or rejects | `shared-team-skills`, `workflow-automation` | Analyst override rate on proposed matches measured by break type |
| `automate` | Posts matches above a rule or confidence threshold; queues exceptions | Clears unresolved breaks; owns ageing | `workflow-automation`, `background-agent` | Sampled audit of auto-matched items shows the false-match rate is within tolerance *(guidance)* |
| `delegate` | Investigates a break across systems and drafts the correcting entry for approval | Approves postings | `managed-agent-runtime` | No named, measured case found; announced only [NASDAQ-BROADRIDGE-2019] |

Typical end state *(guidance)*: continuous matching in place of period-end matching, a `process` change.

## 4. How it is built

- **Inputs.** Two or more record sets, matching rules and tolerances, reason codes, ageing rules. Beauty Pie said import definitions and matching rules were the main learning [BLACKLINE-BEAUTYPIE-2026].
- **The AI's role.** Three separable jobs: propose matches where keys are messy, classify and explain breaks, propose resolutions. Model matchers are prompt-sensitive: "there is no single best prompt" [PEETERS-ENTITYLLM-2024].
- **Deterministic first.** Exact and rule-based matching clears the bulk; add a model where rules leave a long tail *(guidance)*.
- **Human checkpoints.** A named person clears unresolved breaks; the account owner approves auto-clear rules and tolerances *(guidance)*. Xero's design makes auto-reconciliation opt-in per account, shows the rule or document behind each match, and allows undo [DIGIT-XERO-2026].
- **Thresholds and sampling.** Confidence-gated posting [DIGIT-XERO-2026]; audit the auto-matched population for false matches with a defined sampling plan [NIST-SAMPLING-2026]; track unmatched items by age, not count alone *(guidance)*.
- **Logging.** UK client-money rules require a record of the date, actions and outcome of each reconciliation, and policies on resolving discrepancies [FCA-CASS715-2026]. Keep the evidence for each AI-touched match so a reviewer can reconstruct it *(guidance)*.

## 5. Prerequisites

- **Data and access.** Read access to every source and a trusted reference; stable keys or a plan for fuzzy keys. State which side is the book of record; CASS requires the firm's own ledger values [FCA-CASS715-2026].
- **Policy.** Tolerance limits, write-off authority, and who may post corrections (not the matcher).
- **Skills.** Someone who can read a break and trace it to its cause. Beauty Pie found an ERP that posted converted amounts in the wrong currency, wrong by 20% on those items [BLACKLINE-BEAUTYPIE-2026].

## 6. Failure modes and controls

| Failure | How it shows up | Control that catches it |
|---|---|---|
| Forced matches hide real breaks | Auto-match rate high, problems surface later | One-to-one match constraints; tolerance policy owned by finance; sample the auto-matched set *(guidance)* |
| Mismatch treated as a finding about a person | Debts or denials raised from a discrepancy (Robodebt) [ROBODEBT-RC-2023] | A break prompts investigation; a person verifies before any adverse action |
| Wrong book of record | Reconciled to statement values | State the book of record in the design [FCA-CASS715-2026] |
| Demo rates do not survive real data | Splits, foreign currency and journals need oversight in practice [DIGIT-XERO-2026]; a vendor asserts 65-75% touchless in production vs 90-99% in demos [KOGNITOS-AP-2026] | Pilot on a month of real history, including bad months; report by break type |
| Plateau because the answer is elsewhere | Exceptions stall | Give access to contracts, vendor master and approvals; measure root causes fixed [KOGNITOS-AP-2026] |
| Unexplained matches | Reviewer cannot say why items were paired | Store evidence per match; test that it can be reconstructed |

## 7. Value and metrics

- **Levers:** `capacity`, `speed`, `quality`, `risk`, `cost`.
- **Typical figures:** Beauty Pie, 99.6% auto-matched, 4,100 unreconciled of over 1,000,000 transactions, "many days" to "a few hours" (customer-reported, rule-based) [BLACKLINE-BEAUTYPIE-2026]; Konica Minolta about 99% automated matching and close from 30 to 7 days (vendor-published) [HIGHRADIUS-KONICA-2025]; Globe Telecom 90% auto-match (vendor-published) [CASESTUDIES-GLOBE-2026]. None reports a false-match rate.
- **Auto-match rate**: transactions matched without a person divided by total transactions in the period.
- **Quality metrics to demand:** false-match rate from a sampled audit; unreconciled items by age; reopen rate; analyst override rate on proposed matches; share of breaks with the root cause fixed at source (Broadridge framed the aim as finding the underlying cause [NASDAQ-BROADRIDGE-2019]).
- **Risk:** defects surfaced, such as Beauty Pie's currency posting fault.

## 8. Governance

- **Financial services.** UK client money must be reconciled daily from the previous business day's records [FCA-CASS715-2026]; model risk guidance applies if models drive matching or auto-clear [FRB-SR117-2011].
- **EU AI Act.** Ledger reconciliation is not on the Annex III list; exposure arises where the output evaluates benefit eligibility or creditworthiness (Annex III 5(a)-(b)) [EU-AIACT-2024], with Annex III duties from 2 December 2027 [EC-2026].
- **Public sector.** The Robodebt Royal Commission recommended review paths, disclosure, business rules open to scrutiny and an audit body for automated decisions [ROBODEBT-RC-2023]; GDPR Art. 22 where a result triggers a decision about a person [EU-GDPR-2016].
- **NIST AI RMF.** MEASURE 2.5 (validity, limits of generalization) and MANAGE 4.1 (monitoring, override) for any AI matcher [NIST-AIRMF-2023].
- **ISO/IEC 42001.** Lifecycle and use-of-AI controls, per a practitioner summary [ISMS-ISO42001-2025].

## 9. Evidence

No cross-industry example of this pattern reaches grade A: the measured one is rule-based, the AI ones are vendor
figures.

| Organization | Industry | What changed | Outcome (provenance) | Grade | Source |
|---|---|---|---|---|---|
| Beauty Pie | Retail | Three-way matching of bank, e-commerce and ERP moved from spreadsheets to rule-based software | 99.6% auto-matched; ERP currency defect found (customer-reported on a vendor page; not AI) | B | BLACKLINE-BEAUTYPIE-2026 |
| Services Australia (Robodebt) | Public sector | Benefit records matched to tax income; discrepancies treated as debts | Royal Commission recommendations on automated decisions (independent; failure case; not AI) | B | ROBODEBT-RC-2023 |
| Konica Minolta | Manufacturing | AI/ML matching for bank reconciliation | About 99% matching; close 30 to 7 days (vendor-published) | C | HIGHRADIUS-KONICA-2025 |
| Globe Telecom | Telecommunications | Configurable matching replaced an end-of-life system | 90% auto-match; reporting 30 to 8-12 days (vendor-published) | C | CASESTUDIES-GLOBE-2026 |
| AutoNation | Vehicle retail | AI-assisted reconciliations at volume | "Near 100%" auto-match, 200,000 transactions a month; no baseline (vendor-published) | C | TRINTECH-AUTONATION-2026 |
| Xero | Accounting software | Confidence-gated auto-reconciliation, opt-in, with explanation and undo | Demo: 113 of 118 handled; accuracy claim above 97% (vendor-published, demo conditions) | C | DIGIT-XERO-2026 |
| Broadridge | Financial services | ML break classification for trade reconciliation | Announced; no outcomes (vendor-published) | C | NASDAQ-BROADRIDGE-2019 |

**In the archetypes:** `assurance-completion-reporting-06` (A), `security-operations-21` (A),
`assurance-substantive-testing-10` (B), `assurance-controls-testing-07` (B),
`professional-services-billing-collections-13` (B), `tax-data-technology-09` (B), `tax-transfer-pricing-12` (B),
`security-identity-access-20` (B).

## 10. Probes

| Ask | What the answer reveals |
|---|---|
| "What is your match rate today, and what happens to what does not match?" | Whether the exception queue is owned and aged |
| "Do rules already clear most of it?" | Whether the AI case is the long tail only |
| "When a break is found, who investigates, and does anything get fixed at the source?" | Whether value is cleared items or removed causes |
| "Which record is the book of record, and who can post a correction?" | Matching to the right side; separation of matcher and poster |
| "What does a false match cost compared with a missed match?" | Where to set thresholds |
| "How will you measure false matches in the auto-cleared set?" | Whether a sampled audit is planned |
| "Does a mismatch ever lead to action against a person or customer?" | Whether human verification is needed before adverse action |
| "Can we run it on your worst month, not your cleanest?" | Demo-to-production gap |

## 11. Sources

- `BLACKLINE-BEAUTYPIE-2026` — BlackLine, *From manual matching to 99.6% automation: Beauty Pie*, retrieved 2026-10-20. https://www.blackline.com/customers/beauty-pie/
- `CASESTUDIES-GLOBE-2026` — CaseStudies.com, *Globe Telecom reduces audit findings time by 60% with BlackLine*, retrieved 2026-10-20. https://www.casestudies.com/company/blackline/case-study/globe-cuts-time-to-audit-findings-by-60-with-blackline
- `DIGIT-XERO-2026` — Digit Business, *Xero AI roadmap: JAX, Syft analytics*, 2026-02-23. https://digit.business/insights/xero/xero-ai-roadmap-jax-syft-analytics
- `EC-2026` — European Commission, *AI Omnibus enters into force*, 2026-07-27. https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force
- `EU-AIACT-2024` — European Union, *Regulation (EU) 2024/1689 (AI Act)*, 2024-06-13. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
- `EU-GDPR-2016` — European Union, *GDPR Art. 22*, 2016-04-27. https://gdpr-info.eu/art-22-gdpr/
- `FCA-CASS715-2026` — FCA Handbook, *CASS 7.15 Records, accounts and reconciliations*, 2026-09-25. https://www.handbook.fca.org.uk/handbook/CASS/7/15.html
- `FRB-SR117-2011` — Federal Reserve and OCC, *SR 11-7: Model Risk Management*, 2011-04-04. https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
- `HIGHRADIUS-KONICA-2025` — HighRadius, *Konica Minolta close and reconciliation case study*, 2025-04-17. https://www.highradius.com/en-gb/value-creation/http://konica-minolta-close-and-reconciliation/
- `ISMS-ISO42001-2025` — ISMS.online, *ISO 42001 Annex A controls* (practitioner summary), 2025-08-21. https://www.isms.online/iso-42001/annex-a-controls/
- `KOGNITOS-AP-2026` — Kognitos, *Why most agentic AP pilots stall at 70% touchless*, 2026-06-02. https://www.kognitos.com/blog/agentic-ap-pilot-stalled-70-percent-touchless/
- `NASDAQ-BROADRIDGE-2019` — Broadridge via Nasdaq, *New AI and ML platform for reconciliation, matching and exception management*, 2019-12-03. https://www.nasdaq.com/press-release/new-artificial-intelligence-and-machine-learning-platform-for-reconciliation-matching
- `NIST-AIRMF-2023` — NIST, *AI Risk Management Framework 1.0 (NIST AI 100-1)*, 2023-01. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `NIST-SAMPLING-2026` — NIST/SEMATECH, *e-Handbook of Statistical Methods* §6.2.1–6.2.2 (acceptance sampling), retrieved 2026-10-20. https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc22.htm
- `PEETERS-ENTITYLLM-2024` — Peeters, Steiner, Bizer, *Entity Matching using Large Language Models*, 2024-10-18. https://arxiv.org/pdf/2310.11244
- `ROBODEBT-RC-2023` — Royal Commission into the Robodebt Scheme, *Report: recommendations*, 2023-07-07. https://robodebt.royalcommission.gov.au/publications/report
- `TRINTECH-AUTONATION-2026` — Trintech, *The reality of AI reconciliations: AutoNation* (webinar abstract), 2026-08-19. https://www.trintech.com/webinar/reality-of-ai-reconciliations-autonation/

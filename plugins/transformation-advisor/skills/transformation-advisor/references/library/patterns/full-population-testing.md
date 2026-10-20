# Pattern: full-population-testing

Tests every item instead of a sample and surfaces exceptions for people to investigate. Read this when an option
replaces sampling or spot checks with a test of the whole population. Keys in brackets are listed in §11. Lines
marked *(guidance)* are design advice, not findings from a source.

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

Rules, a model or both run over every item in a population (or a defined stratum), score or flag the unusual ones,
explain why, and route exceptions to a named person who investigates and concludes. Auditing standards already
recognize "selecting all items (100 percent examination)" where a procedure can be automated over the population;
testing specific items is not sampling and its results "cannot be projected to the entire population"
[PCAOB-AS1105-2026]. "We test everything now" covers only the items and criteria the tool actually evaluates. It is
not necessarily AI: the UK FRC's worked example combines rules with an AI score [FRC-AIAUDIT-2025]. Its sibling,
`monitor-diagnose-act`, runs the same idea over signals in time.

**How to recognize it** *(guidance)*: "we only have time to check 5%"; "we find it after the money has gone or the
release has shipped"; "rules fire thousands of alerts and most are noise"; "random spot checks each quarter".

## 2. Where it fits

- **Work types:** `review-assurance`, `transaction-processing`, `data-reporting`.
- **Seen with:** payment integrity and fraud screening [TREASURY-OPI-2024; DWP-ATRS-2025]; anti-money-laundering monitoring [GOOGLE-HSBC-2023]; pre-payment claims analytics [HHSOIG-FPS-2015]; static analysis on every code change [ACM-TRICORDER-2018]; journal-entry testing [FRC-AIAUDIT-2025].
- **Not for automatic adverse decisions on individuals with no human review and no control sample** (MiDAS, Robodebt) [MICHIGANPUBLIC-MIDAS-2016; CONVERSATION-ROBODEBT-2023].
- **Not with protected or proxy attributes such as nationality as inputs** [AMNESTY-DUTCH-2021].
- **Not on incomplete or unreliable data reported as "100% tested"** [PCAOB-AS1105-2026; FRC-AIAUDIT-2025].
- **Not when flagged volume exceeds review capacity** *(guidance)*, or the "exception" is a matter of opinion rather than a rule or measurable deviation.
- **Not when rules over the full population already solve it**; ask before proposing a model [FRC-AIAUDIT-2025].

## 3. Up the ladder

| Rung | What the AI does | What the person does | Runtime class | Checkpoint before moving up |
|---|---|---|---|---|
| `assist` | Runs a one-off analysis over a full extract | Designs the test; reviews results | `personal-assistant` | Population completeness and accuracy tested |
| `augment` | Scores every item; explains each flag | Reviews each flagged item and concludes | `shared-team-skills`, `workflow-automation` | Precision (share of flags confirmed) measured; flagged volume fits capacity |
| `automate` | Scheduled runs; exceptions queued; nobody on the clean path | Investigates exceptions; adverse outcomes stay human | `workflow-automation`, `background-agent` | Random control sample including low-scored items; precision by cohort (DWP design) |
| `delegate` | Investigates exceptions across systems and drafts the conclusion | Signs off | `managed-agent-runtime` | Documented investigation trail and sign-off; measured only in archetype entries (§9) |

Even where screening is automatic, the human decides adverse outcomes: DWP states "there is always a human
intervention and decision" [DWP-ATRS-2025].

## 4. How it is built

- **Inputs.** A complete population extract with its completeness and accuracy tested [PCAOB-AS1105-2026]. The FRC example makes the tool mandatory only where ledger data is "complete and accurate" with the needed fields [FRC-AIAUDIT-2025].
- **The AI's role.** Score or rank items and explain each flag, so users can design follow-up responsive to the feature that triggered it [FRC-AIAUDIT-2025]. Run rules alongside the model: an outlier detector misses items consistently posted to unusual accounts [FRC-AIAUDIT-2025].
- **Thresholds.** Setting weights and cut-offs needs "significant professional judgement" and experimentation with data [FRC-AIAUDIT-2025]. Google accepts a code-review check only if under 10% of its findings are effective false positives, and disables noisy analyzers [ACM-TRICORDER-2018].
- **Control sample.** DWP sends a random sample of low-risk and high-risk items to decision makers, who see no risk rating [DWP-ATRS-2025]. This yields a false-negative signal and a lift figure, and limits confirmation bias.
- **Review budget.** A preprint found detectors that look strong on the full population can concentrate their top flags on one anomaly type [GRONEWALD-ARXIV-2026]; evaluate against the number of items people can actually review *(guidance)*.
- **Logging.** Version control so only the approved tool version runs; model frozen before deployment [FRC-AIAUDIT-2025]; EU high-risk logs kept at least six months [EU-AIACT-2024].

## 5. Prerequisites

- **Data and access.** A complete, accurate population with the needed fields; item-level read access to the system of record.
- **Policy.** A human decision for any adverse outcome and an appeal route [DWP-ATRS-2025; OMB-M2521-2025].
- **Capacity.** A staffed exceptions queue sized to the flagged volume *(guidance)*; HSBC says fewer alerts let investigators focus on "genuinely suspicious cases" [GOOGLE-HSBC-2023].
- **Skills.** Data science to calibrate; domain experts to set criteria; central tool certification, which the FRC found partly informal [FRC-ATTREVIEW-2025].
- **Reviewer acceptance.** External reviewers rated analytics-based audit procedures lower quality for appearing less effortful [EMETT-CAR-2023]; plan that conversation.

## 6. Failure modes and controls

| Failure | How it shows up | Control that catches it |
|---|---|---|
| False positives swamp reviewers | Danske's earlier rules-based system produced false positives "at times reaching 99.5%", in the vendor's words [FINTECHFUTURES-DANSKE-2017] | Track precision; retune or disable noisy checks [ACM-TRICORDER-2018]; set thresholds against a control sample |
| Blind spots | Items unusual in a consistent way are not flagged [FRC-AIAUDIT-2025] | Rules alongside the model; random sample of low-scored items [DWP-ATRS-2025] |
| Adverse action at scale with no human check | MiDAS: a state review found 93% of fraud findings wrong [MICHIGANPUBLIC-MIDAS-2016]; $20 million settlement [UMICH-MIDAS-2024] | Human decision, appeal, pre-deployment testing, monitoring [OMB-M2521-2025] |
| Disparate impact | Some cohorts referred more often but correctly less often [DWP-FAIRNESS-2025] | Referral rate against confirmed rate by cohort; retrain; drop proxy variables |
| Overstated benefit | $454.0 million identified vs $133.2 million certified savings [HHSOIG-FPS-2015] | Agree the savings definition with an independent party before reporting |
| Tool drift | Recertification triggers identified "informally" [FRC-ATTREVIEW-2025] | Defined recertification triggers; version control |

## 7. Value and metrics

- **Levers:** `risk`, `cost`, `quality`, `capacity`, `speed`.
- **Typical figures:** HSBC alerts down 60% with two to four times as much suspicious activity identified, 12 months after go-live vs the 12 before (self-reported) [GOOGLE-HSBC-2023]; DWP's model 2.5 times more effective than a random control sample (self-reported) [DWP-ATRS-2025]; US Treasury over $4 billion prevented and recovered in FY2024, of which $1 billion is tied to machine learning (self-reported) [TREASURY-OPI-2024]; Google about 5,000 "Please fix" clicks a day against about 250 "Not useful" [ACM-TRICORDER-2018].
- **Quality metrics to require:** precision overall and by cohort; dismiss or override rate; false-negative rate from a control sample; reviewer time per exception; share of exceptions concluded as true findings.
- **Illustrative arithmetic, not a measurement:** with 0.1% true exceptions in 1,000,000 items, a test with 90% sensitivity and 99% specificity flags about 900 true and 9,990 false items, so about 8% of flags are real.

## 8. Governance

- **NIST AI RMF.** MEASURE 2.4 (monitored in production), MANAGE 2.4 (ability to "supersede, disengage, or deactivate"), MANAGE 4.1 (monitoring with appeal and override), MAP 3.5 [NIST-AIRMF-2023]; automation bias [NIST-AI600-2024].
- **EU AI Act.** Annex III 5(a) covers public-benefit eligibility, including to "grant, reduce, revoke, or reclaim"; 5(b) excludes financial-fraud detection from credit scoring; Art. 6(3) narrow-task derogations never cover profiling; Art. 27 fundamental rights impact assessments for public deployers [EU-AIACT-2024]. Annex III duties apply from 2 December 2027 [EC-2026].
- **ISO/IEC 42001.** An organization-level, certifiable management system [BSI-ISO42001-2026]; no clause-level guidance for this pattern was read.
- **US federal.** OMB presumes detection of fraudulent use of government services "high-impact" and requires testing, monitoring, human oversight and timely human review or appeal [OMB-M2521-2025].
- **Audit.** PCAOB AS 1105 on 100% examination and information reliability [PCAOB-AS1105-2026]; FRC guidance and thematic review [FRC-AIAUDIT-2025; FRC-ATTREVIEW-2025]. The FRC found none of six large firms formally measured the audit-quality impact of their automated tools [FRC-ATTREVIEW-2025].

## 9. Evidence

| Organization | Industry | What changed | Outcome (provenance) | Grade | Source |
|---|---|---|---|---|---|
| HSBC | Financial services | ML model replaced rules-based transaction monitoring (over 1.2 billion transactions a month) | Alerts -60%; two to four times the suspicious activity; 12-month before-and-after (self-reported) | A | GOOGLE-HSBC-2023 |
| UK DWP | Public sector | Model risk-scores all advance requests; high-risk to a human; random control sample | 2.5 times more effective than a random control sample; cohort fairness gaps led to retraining (self-reported) | A | DWP-ATRS-2025 |
| US Treasury | Public sector | Risk-based screening of federal payments plus ML on check fraud | Over $4 billion prevented and recovered in FY2024 vs $652.7 million in FY2023 (self-reported) | A | TREASURY-OPI-2024 |
| US CMS Fraud Prevention System | Healthcare payer | Predictive analytics on all Medicare fee-for-service claims; leads investigated | $133.2 million certified savings, ROI $2.84 (independent inspector general; pre-generative AI) | A | HHSOIG-FPS-2015 |
| Google (Tricorder) | Technology | Analyzers run on every code change inside review | About 50,000 changes a day; noisy analyzers disabled above 10% "Not useful" (self-reported; not ML) | A | ACM-TRICORDER-2018 |
| BMW Group, Debrecen | Manufacturing | AI evaluates sensor and camera data; 100% end-of-line inspection | No figures (self-reported press statement) | B | BMW-DEBRECEN-2025 |
| Michigan unemployment agency | Public sector | Automated fraud determinations with no human on the path | 93% of reviewed findings wrong; $20 million settlement (press; failure case) | B | MICHIGANPUBLIC-MIDAS-2016 |
| Dutch Tax Administration | Public sector | Risk model scored childcare benefit applications, with nationality as a parameter | Described by Amnesty as racial profiling (independent NGO; failure case) | B | AMNESTY-DUTCH-2021 |

**In the archetypes:** `assurance-controls-testing-08` (A), `security-application-security-07` (A),
`security-ai-security-17` (A), `security-vulnerability-exposure-02` (A), `tax-controversy-15` (A),
`assurance-substantive-testing-01` (B), `assurance-planning-risk-assessment-08` (B),
`professional-services-quality-review-06` (B).

## 10. Probes

| Ask | What the answer reveals |
|---|---|
| "What fraction of items do you check today, and how were they chosen?" | Whether sampling is random or risk-based, and what the real constraint is |
| "If we tested everything and flagged 1%, who would look at them, and how long does each take?" | Capacity on the exceptions queue |
| "What share of what your current alerts flag turns out to be real?" | Baseline precision a new tool must beat |
| "How will you find what the tool misses?" | Whether a control sample or parallel rules are planned |
| "What happens to the person or item when flagged, and who decides?" | Whether adverse action happens without a human decision |
| "Is the data complete, and who tested that?" | Whether "100% tested" means anything |
| "Which groups are flagged more often, and are those flags right more often?" | Cohort precision and fairness |
| "How will savings or findings be counted, and who agrees the definition?" | Attribution risk |

## 11. Sources

- `ACM-TRICORDER-2018` — Sadowski et al., *Lessons from Building Static Analysis Tools at Google*, Communications of the ACM, 2018-04. https://cacm.acm.org/research/lessons-from-building-static-analysis-tools-at-google/
- `AMNESTY-DUTCH-2021` — Amnesty International, *Xenophobic Machines: the Dutch childcare benefits scandal*, 2021-10. https://www.amnesty.org/en/wp-content/uploads/2021/10/EUR3546862021ENGLISH.pdf
- `BMW-DEBRECEN-2025` — BMW Group, *Plant Debrecen media information*, 2025-09-17. https://www.press.bmwgroup.com/global/article/attachment/T0452702EN/637986
- `BSI-ISO42001-2026` — BSI, *ISO/IEC 42001: AI Management System* (description), retrieved 2026-10-20. https://www.bsigroup.com/en-GB/products-and-services/standards/iso-42001-ai-management-system/
- `CONVERSATION-ROBODEBT-2023` — Peter Whiteford, The Conversation, *The Robodebt royal commission will tell us who's to blame*, 2023-07-07. https://theconversation.com/the-robodebt-royal-commission-will-tell-us-whos-to-blame-but-thats-just-the-start-208916
- `DWP-ATRS-2025` — DWP, *Universal Credit Advances Model* (transparency record), 2025-12-16. https://www.gov.uk/algorithmic-transparency-records/dwp-universal-credit-advances-model
- `DWP-FAIRNESS-2025` — DWP, *Universal Credit Advances Model: fairness assessment 2024-25*, 2025-07-17. https://www.gov.uk/government/publications/fairness-assessment-including-statistical-analysis-of-the-universal-credit-advances-machine-learning-model-1-april-2024-to-31-march-2025/universal-credit-advances-model-fairness-assessment
- `EC-2026` — European Commission, *AI Omnibus enters into force*, 2026-07-27. https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force
- `EMETT-CAR-2023` — Emett et al., *Auditing with data and analytics: external reviewers' judgments*, Contemporary Accounting Research, 2023-10. https://doi.org/10.1111/1911-3846.12894
- `EU-AIACT-2024` — European Union, *Regulation (EU) 2024/1689 (AI Act)*, 2024-06-13. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
- `FINTECHFUTURES-DANSKE-2017` — FinTech Futures, *Danske Bank turns to Teradata for AI-powered fraud detection*, 2017-10-23. https://www.fintechfutures.com/ai-in-fintech/danske-bank-turns-to-teradata-for-ai-powered-fraud-detection
- `FRC-AIAUDIT-2025` — Financial Reporting Council, *AI in audit*, 2025-06-26. https://www.frc.org.uk/documents/8384/AI_in_Audit.pdf
- `FRC-ATTREVIEW-2025` — Financial Reporting Council, *Thematic review: certification of automated tools and techniques*, 2025-06. https://www.frc.org.uk/documents/8383/Thematic_Review_on_the_Certification_of_Automated_Tools_and_Techniques.pdf
- `GOOGLE-HSBC-2023` — Richard D. May (HSBC), Google Cloud blog, *Fighting money launderers with AI at HSBC*, 2023-11-30. https://cloud.google.com/blog/topics/financial-services/how-hsbc-fights-money-launderers-with-artificial-intelligence
- `GRONEWALD-ARXIV-2026` — Gronewald et al., *Machine learning for journal entry testing under a review budget* (preprint), 2026-10-05. https://arxiv.org/abs/2610.06133
- `HHSOIG-FPS-2015` — HHS Office of Inspector General, *The Fraud Prevention System increased recovery and prevention of improper Medicare payments*, 2015-06. https://www.oig.hhs.gov/documents/audit/5785/A-01-14-00503-Complete%20Report.pdf
- `MICHIGANPUBLIC-MIDAS-2016` — Michigan Public, *State review: 93% of unemployment fraud findings were wrong*, 2016-12-16. https://www.michiganpublic.org/politics-government/2016-12-16/state-review-93-of-state-unemployment-fraud-findings-were-wrong
- `NIST-AI600-2024` — NIST, *AI RMF Generative AI Profile (NIST AI 600-1)*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `NIST-AIRMF-2023` — NIST, *AI Risk Management Framework 1.0 (NIST AI 100-1)*, 2023-01. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `OMB-M2521-2025` — US OMB, *M-25-21: Accelerating federal use of AI*, 2025-04-03. https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf
- `PCAOB-AS1105-2026` — PCAOB, *AS 1105: Audit Evidence*, accessed 2026-10. https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105
- `TREASURY-OPI-2024` — US Treasury, *Enhanced fraud detection processes prevented and recovered over $4 billion in FY2024*, 2024-10-17. https://home.treasury.gov/news/press-releases/jy2650
- `UMICH-MIDAS-2024` — University of Michigan Ford School STPP, *MIDAS case finally settled* (explainer), 2024-08. https://stpp.fordschool.umich.edu/sites/stpp/files/2024-08/stpp-midas-explainer.pdf

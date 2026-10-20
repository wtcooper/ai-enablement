# Pattern: document-to-decision

Extracts facts from documents and checks them against criteria to propose a decision. Read this when an option
reads forms, claims, contracts or evidence and decides whether something qualifies, complies or is approved. Keys
in brackets are listed in §11. Lines marked *(guidance)* are design advice, not findings from a source.

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

The AI extracts each needed field from a document with a pointer to where it found it, applies written criteria,
and proposes a decision with a rationale; below a threshold it may take the decision itself. Keep two stages
separate *(guidance)*: field extraction with evidence, then criteria application. Extraction confidence is the hard
engineering problem: on a 55-field invoice benchmark, frontier models failed on 26% of fields and token
probabilities separated right from wrong answers only weakly [KUMAR-EXTRACTCONF-2026].

**How to recognize it** *(guidance)*: "we read X and decide whether it qualifies, complies or is approved"; "we
check forms against a policy"; "people re-key from PDFs"; "a checklist with yes/no answers"; "most items are
routine and a few need judgment".

## 2. Where it fits

- **Work types:** `review-assurance`, `transaction-processing`; `expert-judgment` where the AI only prepares.
- **Shapes seen:** expense-policy approval [RAMP-AGENTS-2025]; loan-agreement review [ABAJ-COIN-2017]; contract data capture [ZENML-VENDR-2026]; insurance claim coverage checks [INSURANCENEWS-NEMO-2025]; benefit rating [VAOIG-ABD-2023]; medical-necessity decisions [PROPUBLICA-CIGNA-2023].
- **Not for decisions that significantly affect a person with no individualized review** (Cigna bulk denials, Robodebt) [PROPUBLICA-CIGNA-2023; ROBODEBT-RC-2023].
- **Not where criteria are unwritten, inconsistent or secret** [VAOIG-ABD-2023; REEDSMITH-CMSAI-2024].
- **Not where review is set up for bulk sign-off at speed**, which produces rubber-stamping (1.2 seconds a case at Cigna) [PROPUBLICA-CIGNA-2023].
- **Not for low-volume, high-variance documents** where the rubric never pays back; first ask whether generic OCR or a point tool is enough [ZENML-VENDR-2026].
- **Not when the only quality check sits inside the project team**: the VA project's internal review reported 100% accuracy that its leaders did not question [VAOIG-ABD-2023].

## 3. Up the ladder

| Rung | What the AI does | What the person does | Runtime class | Checkpoint before moving up |
|---|---|---|---|---|
| `assist` | Pulls fields or checks a clause on request | Decides | `personal-assistant` | Written criteria and a labelled gold set of real documents |
| `augment` | Extracts fields with citations and a first-pass verdict | Confirms or overrides each item | `shared-team-skills`, `workflow-automation` | Per-field accuracy and override rate measured; thresholds set per field |
| `automate` | Decides items above a confidence and risk threshold; escalates the rest (a vendor says 10-15% escalate [RAMP-AGENTS-2025]) | Decides escalations; audits a sample of automated decisions | `workflow-automation`, `background-agent` | Independent sample of the automated decisions with a pre-set plan [NIST-SAMPLING-2026]; appeal route |
| `delegate` | Also gathers missing documents, chases the requester and updates systems | Approves at checkpoints | `managed-agent-runtime` | Evidence is thin outside assurance (§9) |

The checkpoint moves rather than disappears: from "review every item" to "review the sample, the exceptions and the
thresholds". The VA and Cigna cases show that `automate` without independent quality measurement is the unsafe rung.

## 4. How it is built

- **Inputs.** Documents of varying quality plus the written criteria. Preprocess (deskew, rotate, crop) and combine OCR with multimodal reading, which "tend to hallucinate more" but see signatures and strikethroughs [ZENML-VENDR-2026].
- **The AI's role.** Extract each field with a citation (page, snippet, confidence) so reviewers verify rather than re-read [HN-ASKHN-2025]; apply criteria; write a rationale. Ramp says every agent action comes with a rationale and is logged [RAMP-AGENTS-2025].
- **Field rubrics.** Write what each field means: whether "total price" includes tax, how to treat strikethroughs [ZENML-VENDR-2026].
- **Deterministic checks around the model.** Cross-check extracted values against external records [HN-ASKHN-2025]; keep calculation in a deterministic engine (see `tax-research-advisory-12`).
- **Thresholds.** Per field, calibrated on your own documents. A multi-signal confidence engine reached 99.1% accuracy on the 80% of fields it automated, against a 73.3% base rate, on 267 test fields; log-probabilities alone did not [KUMAR-EXTRACTCONF-2026, vendor-affiliated author, preprint].
- **Sampling.** Audit automated decisions with a formal plan (acceptable quality level, single, double or sequential plans) [NIST-SAMPLING-2026]; sample escalated items too *(guidance)*. The VA planned no check on automated decisions beyond possible random selection for routine quality review [VAOIG-ABD-2023].
- **Logging.** Keep inputs, extracted values with citations, criteria version, model version, verdict, reviewer and override. High-risk EU systems must allow automatic event logging, kept by deployers at least six months [EU-AIACT-2024]. Bank guidance reads a high override rate as a sign the model is not performing as intended [FRB-SR117-2011].

## 5. Prerequisites

- **Data.** Representative real documents including bad scans, and a gold set labelled by people who apply the criteria. Settle the criteria first: VA guidance that "varied from" the claims manual fed its error rate [VAOIG-ABD-2023].
- **Access.** Read access to records used for cross-checks; write access only for the decision step.
- **Policy.** A decision-rights table (who approves what, above what value); an appeal route; criteria owned by a named person; log retention. CMS expects criteria to stay fixed and public [REEDSMITH-CMSAI-2024].
- **Skills.** Domain reviewers who can write rubrics [ZENML-VENDR-2026]; someone who can run an evaluation set.

## 6. Failure modes and controls

| Failure | How it shows up | Control that catches it |
|---|---|---|
| Extraction error treated as fact | A wrong number reaches the system of record [HN-ASKHN-2025] | Multi-signal per-field confidence; line sums to totals; external record match; citations [KUMAR-EXTRACTCONF-2026] |
| Confabulated value | Field filled with no support in the document | Require source text for every value; flag fields with none [NIST-AI600-2024; HN-ASKHN-2025] |
| Rubber-stamp review | 1.2 seconds per case on bulk denials [PROPUBLICA-CIGNA-2023] | Do not target review speed; seeded challenge items *(guidance)*; overseer training [EU-AIACT-2024 Art. 14] |
| Criteria drift or ambiguity | VA decisions inaccurate in 27% of sampled claims [VAOIG-ABD-2023] | Version criteria; one owner; re-test after every change |
| Quality checks blind to automated items | Internal review reported 100% accuracy while the inspector general found deficiencies [VAOIG-ABD-2023] | Independent sample of automated decisions with a pre-set plan |
| Errors few people contest | Only 0.2% of denials appealed in 2021, per a KFF analysis cited by the press [HCDIVE-UNH-2023] | Do not use appeal rate as the error metric; sample denials proactively *(guidance)* |
| Wrong notices | At least 8,000 automated survivor-benefit decisions or letters omitted favorable findings or had other deficiencies [VAOIG-DIC-2026] | Test the letter, not just the decision |

## 7. Value and metrics

- **Levers:** `capacity`, `speed`, `quality`, `risk`, `cost`, `experience`.
- **Typical figures:** Allianz says claim processing time fell 80% in a pilot (measurement basis not stated) [INSURANCENEWS-NEMO-2025]; JPMorgan said COIN covered work that took about 360,000 hours a year (rough estimate, via press) [ABAJ-COIN-2017]; VBA reported 61.3 vs 25.1 days from in-house metrics, but had done no specific study, so the inspector general said leaders could not know whether timeliness improved [VAOIG-ABD-2023]. Ramp's 99% accuracy is not defined, so it is not comparable [RAMP-AGENTS-2025].
- **Quality metrics, each named:** field accuracy against a gold set; share of automated decisions overturned in a sampled audit; override rate; escalation rate and the error rate inside escalated and automated sets; appeal or reversal rate; AI-to-reviewer agreement compared with reviewer-to-reviewer agreement ("humans don't always agree" [DSIT-CONSULT-2025]).
- **Watch the cost metric.** Cigna's bulk process targeted the cost of denials [PROPUBLICA-CIGNA-2023]; a cost metric can reward the wrong behaviour.
- No named organization publishes override, escalation and error rates together for an AI deployment of this pattern.

## 8. Governance

- **EU AI Act.** High-risk when it evaluates eligibility for public benefits, creditworthiness of natural persons (fraud detection excepted), or life and health insurance pricing; employment screening is also listed (Annex III 4(a), 5(a)-(c)). Deployers need competent, trained overseers and logs [EU-AIACT-2024]. Annex III duties apply from 2 December 2027 [EC-2026].
- **GDPR Art. 22.** Right to human intervention and to contest solely automated decisions with significant effects [EU-GDPR-2016]; nominal review can be used to avoid "solely" [GREEN-OVERSIGHT-2022].
- **NIST AI RMF.** MAP 3.5, GOVERN 3.2, MEASURE 2.5 (validity and limits of generalization), MANAGE 4.1 (monitoring with appeal and override) [NIST-AIRMF-2023].
- **ISO/IEC 42001.** Annex A groups controls on impact assessment, lifecycle and responsible use including human oversight, per a practitioner summary [ISMS-ISO42001-2025].
- **Credit.** Adverse-action reasons must be specific and accurate; creditors may not use complex algorithms when that means they cannot give those reasons [CFPB-CIRC2203-2022].
- **Health insurance.** Medicare Advantage coverage must rest on individualized determinations and published criteria, per a law-firm summary of CMS guidance [REEDSMITH-CMSAI-2024]; California requires a licensed physician or other competent health care provider to make medical-necessity denials [CASENATE-SB1120-2024].

## 9. Evidence

| Organization | Industry | What changed | Outcome (provenance) | Grade | Source |
|---|---|---|---|---|---|
| Veterans Benefits Administration | Public sector | Automation extracts blood-pressure evidence into a summary sheet; processors decide | Inspector general sample: 16 of 60 claims (27%) inaccurate; summary sheets deficient in 37% and 57% of two samples; internal review had reported 100% (independent; rule-based, so adjacent) | B | VAOIG-ABD-2023 |
| Veterans Benefits Administration | Public sector | Rules-based system issues survivor-benefit decisions and letters | Inspector general: at least 8,000 decisions or letters deficient; at least 2% with legal errors, about $2.7 million improper payments (independent; rule-based, so adjacent) | B | VAOIG-DIC-2026 |
| Cigna | Health insurance | Doctors bulk-deny claims matched to a list without opening the file | Over 300,000 denials in two months at 1.2 seconds each (journalism; disputed by the company) | B | PROPUBLICA-CIGNA-2023 |
| Allianz Australia | Insurance | Seven agents do coverage and fraud checks on small claims; a person makes the payout decision | Processing time -80% in a trial; basis not stated (self-reported) | B | INSURANCENEWS-NEMO-2025 |
| Vendr with Extend | Technology | Model extraction from order forms and contracts with targeted human review | Over 100,000 documents; no accuracy figures (self-reported, conference talk) | B | ZENML-VENDR-2026 |
| JPMorgan Chase | Financial services | Software reviews commercial loan agreements | About 360,000 hours a year covered; rough estimate (self-reported, via press) | B | ABAJ-COIN-2017 |
| Ramp | Fintech | Agent approves low-risk expenses against a policy PDF, escalates the rest | 99% accuracy (undefined); 10–15% of expenses escalated (vendor-published) | C | RAMP-AGENTS-2025 |
| UnitedHealth / naviHealth | Health insurance | Alleged model use in post-acute coverage | Lawsuit alleges over 90% of appealed denials were overturned; allegations, not findings | C | HCDIVE-UNH-2023 |

**In the archetypes:** `assurance-controls-testing-05` (A), `assurance-controls-testing-06` (A),
`assurance-controls-testing-11` (A), `security-identity-access-03` (B), `security-governance-risk-03` (B),
`tax-compliance-individual-business-02` (B), `professional-services-work-production-12` (B),
`tax-research-advisory-21` (B).

## 10. Probes

| Ask | What the answer reveals |
|---|---|
| "Take the last 20 items decided. Where did the facts come from, and what rule applied?" | Whether criteria are written and consistent |
| "Who would measure the automated items, and how would they sample?" | Whether quality checks can see the automated decisions |
| "How long does a reviewer spend per item, and is anyone scored on speed?" | Rubber-stamp risk |
| "Which fields, if wrong, cost money or hurt a person?" | Per-field thresholds and where deterministic cross-checks are needed |
| "What share could be decided at 99% accuracy, and what goes to people?" | The coverage-versus-accuracy trade-off |
| "Does the decision affect someone's credit, coverage, benefits or job? Where?" | Which legal regime applies |
| "If someone disagrees with a decision, what happens, and how many do?" | Whether appeals can serve as a quality signal (usually not) |
| "Show me the log for one decision a year from now." | Audit-trail readiness |

## 11. Sources

- `ABAJ-COIN-2017` — ABA Journal, *JPMorgan Chase uses tech to save 360,000 hours of annual work*, 2017-03-02. https://www.abajournal.com/news/article/jpmorgan_chase_uses_tech_to_save_360000_hours_of_annual_work_by_lawyers_and
- `CASENATE-SB1120-2024` — California Senate (Sen. Becker), *Physicians Make Decisions Act signed*, 2024-09-30. https://sd13.senate.ca.gov/node/934
- `CFPB-CIRC2203-2022` — CFPB, *Circular 2022-03: adverse action notices and complex algorithms*, 2022-05-26. https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/
- `DSIT-CONSULT-2025` — UK DSIT, *Humphrey AI tool reviews consultation responses for first time*, 2025-05-14. https://www.gov.uk/government/news/government-built-humphrey-ai-tool-reviews-responses-to-consultation-for-first-time-in-bid-to-save-millions
- `EC-2026` — European Commission, *AI Omnibus enters into force*, 2026-07-27. https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force
- `EU-AIACT-2024` — European Union, *Regulation (EU) 2024/1689 (AI Act)*, 2024-06-13. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
- `EU-GDPR-2016` — European Union, *GDPR Art. 22*, 2016-04-27. https://gdpr-info.eu/art-22-gdpr/
- `FRB-SR117-2011` — Federal Reserve and OCC, *SR 11-7: Model Risk Management*, 2011-04-04. https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
- `GREEN-OVERSIGHT-2022` — Ben Green, *The flaws of policies requiring human oversight of government algorithms*, 2022. https://arxiv.org/pdf/2109.05067v3
- `HCDIVE-UNH-2023` — Healthcare Dive, *UnitedHealth algorithm lawsuit*, 2023-11-15. https://www.healthcaredive.com/news/unitedhealth-algorithm-lawsuit-care-denials/699834/
- `HN-ASKHN-2025` — Hacker News, *Ask HN: Is anyone using LLM based document processing in production?*, 2025-12-18. https://news.ycombinator.com/item?id=46319267
- `INSURANCENEWS-NEMO-2025` — insuranceNEWS.com.au, *AI trial provides blueprint for future, Allianz says*, 2025-11-24. https://www.insurancenews.com.au/insurtech/ai-trial-provides-blueprint-for-future-allianz-says
- `ISMS-ISO42001-2025` — ISMS.online, *ISO 42001 Annex A controls* (practitioner summary), 2025-08-21. https://www.isms.online/iso-42001/annex-a-controls/
- `KUMAR-EXTRACTCONF-2026` — N. Kumar, *Beyond Logprobs: A Multi-Signal Confidence Engine for LLM Document Field Extraction*, 2026-06-23. https://arxiv.org/pdf/2606.24420
- `NIST-AI600-2024` — NIST, *AI RMF Generative AI Profile (NIST AI 600-1)*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `NIST-AIRMF-2023` — NIST, *AI Risk Management Framework 1.0 (NIST AI 100-1)*, 2023-01. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `NIST-SAMPLING-2026` — NIST/SEMATECH, *e-Handbook of Statistical Methods* §6.2.1–6.2.2 (acceptance sampling), retrieved 2026-10-20. https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm
- `PROPUBLICA-CIGNA-2023` — ProPublica, *How Cigna saves millions by having its doctors reject claims without reading them*, 2023-03-25. https://www.propublica.org/article/cigna-pxdx-medical-health-insurance-rejection-claims
- `RAMP-AGENTS-2025` — Ramp, *Ramp agents announcement*, 2025-07-09. https://ramp.com/blog/ramp-agents-announcement
- `REEDSMITH-CMSAI-2024` — Reed Smith, *CMS confirms Medicare Advantage organizations may use AI in coverage determinations*, 2024-02-13. https://www.reedsmith.com/de/perspectives/2024/02/cms-confirms-medicare-advantage-organizations-may-use-ai-in-making-coverage
- `ROBODEBT-RC-2023` — Royal Commission into the Robodebt Scheme, *Report: recommendations*, 2023-07-07. https://robodebt.royalcommission.gov.au/publications/report
- `VAOIG-ABD-2023` — VA Office of Inspector General, *Improvements Needed for VBA's Claims Automation Project*, 2023-09-25. https://www.oversight.gov/sites/default/files/oig-reports/VA/VAOIG-22-02936-175.pdf
- `VAOIG-DIC-2026` — VA Office of Inspector General, *Review of Automated Decisions for Veterans' Service-Connected Death Claims* (report 25-00153-47), 2026-04-30. https://www.vaoig.gov/node/22762
- `ZENML-VENDR-2026` — ZenML LLMOps database, *Scaling Document Processing with LLMs and Human Review* (Vendr and Extend talk), retrieved 2026-10-20. https://zenml.io/llmops-database/scaling-document-processing-with-llms-and-human-review

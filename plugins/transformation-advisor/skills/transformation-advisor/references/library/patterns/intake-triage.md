# Pattern: intake-triage

Reads incoming requests or items, classifies, routes and prioritizes them. Read this when an option sorts what
arrives at a front door. Keys in brackets are listed in §11. Lines marked *(guidance)* are design advice, not
findings from a source; treat them as hypotheses to test with the user.

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

The AI reads each incoming item (letter, email, call, ticket, order, alert), classifies it, extracts key fields,
flags priority or risk, and routes it to a team, queue or pre-approved template; some tools also create the case
record. It rests on three things: a classifier with a known error rate, a rule for what goes to a person, and a
log that lets someone check the rule. Its sibling, `service-agent-escalation`, answers the sender directly.

**How to recognize it** *(guidance)*: "someone sorts the inbox every morning"; "it takes a day before the right
person sees it"; "urgent ones get buried"; "people pick the wrong category on the form"; "we re-key emails into
the case system"; one shared mailbox, phone line or form feeding several specialist teams. A sourced version of the
last cue: UiPath found the chance that product, deployment type and issue type were all correct at ticket creation
was below 50% [UIPATH-CCA-2026].

## 2. Where it fits

- **Work types:** `transaction-processing`, `coordination-scheduling`; any front door with volume (DWP reads about
  25,000 scanned letters a day [PUBTECH-WHITEMAIL-2025]; the ICO created on average 6,340 cases a month [ATRS-ICO-2026]).
- **Not when rules are enough.** The Home Office's visitor-visa router "does not use machine learning" [ATRS-HO-CARSV-2024]. Ask whether declared fields already decide the route.
- **Not when triage denies or reduces a service with no human review** (GDPR Art. 22; EU AI Act Annex III 5(a)) [EU-GDPR-2016; EU-AIACT-2024].
- **Not when the urgent class is rare, a miss is severe and nobody will measure recall.** A model alone more sensitive than dispatchers did not significantly improve dispatcher recognition of cardiac arrest in a randomized trial [JAMANO-BLOMBERG-2021].
- **Not when the taxonomy is unstable or unowned, or items are mostly unreadable attachments** *(guidance)*; HMT removed unreadable files before testing [ATRS-HMT-2024].

## 3. Up the ladder

| Rung | What the AI does | What the person does | Runtime class | Checkpoint before moving up |
|---|---|---|---|---|
| `assist` | Summarizes or suggests a category for an item a person pastes in | Decides and routes | `personal-assistant` | A labelled sample of past items and a named taxonomy owner |
| `augment` | Proposes team, summary, flags; may create a draft case | Confirms or overwrites each item (HMT, ICO, DWP designs) | `workflow-automation`, `shared-team-skills` | Override rate and recall on the urgent class measured per category |
| `automate` | Routes on arrival; failed validation goes to a manual queue (ICO expects "upwards of 90%" of case creation) | Owns the exception queue; spot checks | `workflow-automation`, `background-agent` | Per-category error rate inside tolerance; permanent random audit sample in place *(guidance)* |
| `delegate` | Triages, then investigates and closes across systems | Approves at checkpoints; audits | `managed-agent-runtime` | Only seen in security operations in the archetypes, with deterministic checks first and evidence-gated dismissal (§9) |

Move up per category, not for the whole inbox *(guidance)*.

## 4. How it is built

- **Inputs.** Items made machine-readable and redacted before the model sees them: DWP scans letters, converts text and redacts personal data automatically [PUBTECH-WHITEMAIL-2025].
- **The AI's role.** Often several models. HMT uses a support vector machine for team, a large language model for summary and flags, and retrieval to match standard lines; it "does not write the entire response" [ATRS-HMT-2024].
- **Constrain the output.** FCDO's consular tool has the model return only template and topic identifiers, so the worst case is an irrelevant but valid template, or none [ATRS-FCDO-CONSULAR-2024]. ICO validates parsed data against a data contract per case type and creates the case only if it passes [ATRS-ICO-2026].
- **Thresholds.** DWP used test documents to "calibrate label synonyms and confidence thresholds" and reviewed outputs daily in controlled production [ATRS-DWP-WHITEMAIL-2025]. Raw model confidence is a weak threshold until checked, because modern neural networks were found poorly calibrated [ARXIV-GUO-2017].
- **Human checkpoints and sampling.** FCDO "will review all cases" where a user submits a written enquiry, plus spot checks [ATRS-FCDO-CONSULAR-2024]. Acceptance sampling sits between no inspection and 100% inspection [NIST-SAMPLING-2026]. *(Guidance:)* start at 100% review; thin review by category and confidence band only once that stratum's error rate is measured; always review the highest-severity categories; keep a permanent random audit sample.
- **Logging.** DWP gives each document a unique ID traced to the customer record and keeps the scanned image beside the shortlist [ATRS-DWP-WHITEMAIL-2025]; HMT's accuracy feeds "an automatically updating report" [ATRS-HMT-2024]. *(Guidance:)* log item reference, model and prompt version, predicted fields and confidence, the override and the final outcome, so override rate can be computed.

## 5. Prerequisites

- **Data.** A labelled history of items and where they went (HMT trained on 1,085,710 documents [ATRS-HMT-2024]; DWP captured 80,000 caller utterances [ATRS-DWPCONV-2025]). Without history, DWP used synthetic documents plus two redacted real letters per test [ATRS-DWP-WHITEMAIL-2025]; treat that as thin.
- **Access.** API access to the case system; a scanning or mailbox feed.
- **Policy.** Data protection impact and equality assessments [ATRS-DWP-WHITEMAIL-2025]; a decision on whether data may leave your estate.
- **Skills.** A named owner of the taxonomy and templates; at FCDO only a limited number of trained staff can change templates [ATRS-FCDO-CONSULAR-2024].

## 6. Failure modes and controls

| Failure | How it shows up | Control that catches it |
|---|---|---|
| Misrouting from overlapping categories | Items bounce between teams | Hub coordinator redirects out-of-scope items [ATRS-HMT-2024]; override rate by category |
| Wrong data written to the case record | Wrong names or emails saved | Peer review before any response [ATRS-FCDO-CORR-2025]; flag unmatched organizations [ATRS-ICO-2026] |
| Invented routing target or text | Free text flows into systems | Identifiers-only output [ATRS-FCDO-CONSULAR-2024] |
| Model refuses or returns nothing | Sensitive items silently dropped | Filtered inputs classed "offensive" and sent to manual review [ATRS-FCDO-CORR-2025] |
| Queue floods reviewers | Alerts on many items yet misses the cases that matter | Measure precision and recall locally; a hospital sepsis model alerted on 18% of patients and missed 67% of cases [WONG-ESM-2021] |
| Reviewers defer to the tool | Override rate near zero | Treat automation bias as a named risk [NIST-AI600-2024]; explanations raised acceptance of AI advice whether right or wrong [ARXIV-BANSAL-2021] |
| Hostile or injected content | Instructions hidden in inbound text | Treat inbound text as untrusted; least privilege; human approval for high-risk actions [OWASP-LLM01-2025; WILLISON-TRIFECTA-2025] |

## 7. Value and metrics

- **Levers:** `capacity`, `speed`, `quality`, `risk`, `experience`.
- **Measured:** DWP's telephony platform reports right-first-time routing up 21% and deflection up 9% (denominators and baselines not stated) [ATRS-DWPCONV-2025]. Stated benefits, not measurements: FCDO "several hours of manual work per day" [ATRS-FCDO-CORR-2025]; ICO's expectation of "upwards of 90%" automated case creation [ATRS-ICO-2026].
- **Quality metrics in sources:** accuracy, macro F1, precision and recall per field [ATRS-FCDO-CORR-2025]; share correct against staff choices on historic batches [ATRS-FCDO-CONSULAR-2024].
- **Metrics to add** *(guidance)*: override rate by category; recall on the urgent class; share sent to the manual queue; time to the right team; repeat misroutes.
- No source publishes an override rate, a miss rate on urgent items or a review sampling rate for a production triage tool. Hours saved are not value until they have a destination (`../index.md` §5).

## 8. Governance

- **EU AI Act.** Annex III lists emergency-call classification and dispatch priority, emergency patient triage (5(d)), public-benefit eligibility (5(a)), creditworthiness (5(b)), life and health insurance pricing (5(c)) and filtering job applications (4(a)) as high-risk; Art. 14 oversight must let the overseer stay aware of automation bias; Art. 26 requires competent, trained overseers and logs kept at least six months [EU-AIACT-2024]. Annex III duties apply from 2 December 2027 [EC-2026].
- **GDPR Art. 22.** A right not to be subject to solely automated decisions with legal or similarly significant effects [EU-GDPR-2016]. Ask whether triage only orders a queue or denies something.
- **NIST AI RMF.** MAP 3.5 (oversight documented), MEASURE 2.1 (test sets and metrics documented), MANAGE 4.1 (post-deployment monitoring with appeal and override) [NIST-AIRMF-2023].
- **ISO/IEC 42001.** An organization-level AI management system that can be certified; it governs how you manage AI, not triage thresholds [BSI-ISO42001-2026].
- **UK public sector.** Departments publish transparency records; DWP states "a caseworker will always decide if extra support is needed" [PUBTECH-WHITEMAIL-2025].

## 9. Evidence

| Organization | Industry | What changed | Outcome (provenance) | Grade | Source |
|---|---|---|---|---|---|
| DWP (telephony) | Public sector | Callers say why they call; the system signposts, helps log in or routes to an adviser; a person on request | Right-first-time routing +21%, deflection +9%, 97% speech recognition; baselines not stated (self-reported) | A | ATRS-DWPCONV-2025 |
| Copenhagen Emergency Medical Services | Healthcare | Model listens to emergency calls and alerts dispatchers to suspected cardiac arrest | Randomized trial, 5,242 calls: recognition 93.1% with alerts vs 90.5% without, not significant (independent) | A | JAMANO-BLOMBERG-2021 |
| FCDO (correspondence) | Public sector | Classifies, summarizes and logs mailbox emails; does not write replies | Category accuracy 0.7333, macro F1 0.7467 on a test of the tool; a prompt classifier rose from about 0.34 to about 0.6 (self-reported; tool test, not a work outcome) | B | ATRS-FCDO-CORR-2025 |
| FCDO (consular) | Public sector | Questions matched to approved templates before an enquiry is sent; identifiers only | Correct template for 76% to 81% of historic enquiries vs staff choices (self-reported; tool test) | B | ATRS-FCDO-CONSULAR-2024 |
| DWP (letters) | Public sector | Flags potentially vulnerable people and labels letters into nine themes; caseworkers decide | About 25,000 documents a day; no accuracy published (self-reported) | B | ATRS-DWP-WHITEMAIL-2025 |
| HM Treasury | Public sector | Predicts team, flags and standard lines for ministerial correspondence; officers overwrite | "As good or better than existing processes"; no figures (self-reported) | B | ATRS-HMT-2024 |
| Information Commissioner's Office | Regulator | Parses complaint emails into case data; failures to a manual queue; officers review each case | 6,340 cases a month; 90%+ is an expectation, not an outcome (self-reported) | B | ATRS-ICO-2026 |
| UiPath | Technology | Support cases classified by retrieval plus a model constrained to valid field combinations | Baseline under 50% fully correct; result figures not published in text (self-reported) | B | UIPATH-CCA-2026 |
| Danfoss | Manufacturing | Email B2B orders read and processed by an AI platform | "Up to 80%" of transactional decisions automated; turnaround "potentially" 42 hours to near real time (vendor-published, qualified) | B | DANFOSS-GCLOUD-2026 |

**In the archetypes:** `assurance-controls-testing-04` (A), `security-identity-access-21` (A),
`security-operations-01` (A), `security-vulnerability-exposure-01` (A), `assurance-acceptance-independence-01` (B),
`professional-services-acceptance-risk-03` (B), `security-human-risk-07` (B), `tax-controversy-23` (B).

## 10. Probes

| Ask | What the answer reveals |
|---|---|
| "Walk me through one item from arrival to the right person. How often does it go to the wrong place?" | The real baseline, and whether the pain is routing, reading or waiting |
| "Which items must never wait, and what happens if one is missed?" | The urgent class that needs recall measured and always-reviewed handling |
| "Who owns the category list, and when did it last change?" | Taxonomy ownership; a classifier learns the labels it is given |
| "Do you have past items with the team that handled each?" | Whether an evaluation set exists, or must be built first |
| "Could rules on the form's fields decide the route?" | Whether AI is needed at all [ATRS-HO-CARSV-2024] |
| "Does triage decide anything about a person, or only the order of work?" | The legal class: queue ordering versus denial or eligibility |
| "Where does the AI's output go next: a person, a template or another system?" | Whether an identifiers-only design is possible, and injection exposure |
| "If everything were routed right, where would the saved time go?" | The capacity destination the business case needs |

## 11. Sources

- `ARXIV-BANSAL-2021` — Bansal et al., *Does the Whole Exceed its Parts? AI explanations and team performance* (CHI '21), 2021-01-12. https://arxiv.org/pdf/2006.14779
- `ARXIV-GUO-2017` — Guo et al., *On Calibration of Modern Neural Networks* (ICML 2017), 2017-08-03. https://arxiv.org/pdf/1706.04599
- `ATRS-DWP-WHITEMAIL-2025` — DWP, *Whitemail Insights and Vulnerability Scanner* (transparency record), 2025-11-27. https://www.gov.uk/algorithmic-transparency-records/whitemail-insights-and-vulnerability-scanner
- `ATRS-DWPCONV-2025` — DWP, *Conversational Platform* (transparency record), 2025-12-16. https://www.gov.uk/algorithmic-transparency-records/dwp-conversational-platform
- `ATRS-FCDO-CONSULAR-2024` — FCDO, *Consular Digital Triage: Written Enquiries LLM*, 2024-12-17. https://www.gov.uk/algorithmic-transparency-records/fcdo-consular-digital-triage-written-enquiries-llm
- `ATRS-FCDO-CORR-2025` — FCDO, *Correspondence Triage* (transparency record), 2025-12-16. https://www.gov.uk/algorithmic-transparency-records/fcdo-correspondence-triage
- `ATRS-HMT-2024` — HM Treasury, *Correspondence Triage Automation Tool*, 2024-12-17. https://www.gov.uk/algorithmic-transparency-records/hmt-correspondence-triage-automation-tool
- `ATRS-HO-CARSV-2024` — Home Office, *Complexity Application Routing Solution: Visits*, 2024-12-17. https://www.gov.uk/algorithmic-transparency-records/home-office-complexity-application-routing-solution-visits
- `ATRS-ICO-2026` — ICO, *ICE 360 Case Creation Automation*, 2026-01-14. https://www.gov.uk/algorithmic-transparency-records/ico-ice-360-case-creation-automation
- `BSI-ISO42001-2026` — BSI, *ISO/IEC 42001: AI Management System* (description), retrieved 2026-10-20. https://www.bsigroup.com/en-GB/products-and-services/standards/iso-42001-ai-management-system/
- `DANFOSS-GCLOUD-2026` — Google Cloud, *Danfoss and Go Autonomous* (customer story), retrieved 2026-10-20. https://cloud.google.com/customers/danfoss
- `EC-2026` — European Commission, *AI Omnibus enters into force*, 2026-07-27. https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force
- `EU-AIACT-2024` — European Union, *Regulation (EU) 2024/1689 (AI Act)*, 2024-06-13. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
- `EU-GDPR-2016` — European Union, *GDPR Art. 22*, 2016-04-27. https://gdpr-info.eu/art-22-gdpr/
- `JAMANO-BLOMBERG-2021` — Blomberg et al., *Effect of Machine Learning on Dispatcher Recognition of Out-of-Hospital Cardiac Arrest*, JAMA Network Open, 2021-01-04. https://pmc.ncbi.nlm.nih.gov/articles/PMC7788469/
- `NIST-AI600-2024` — NIST, *AI RMF Generative AI Profile (NIST AI 600-1)*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `NIST-AIRMF-2023` — NIST, *AI Risk Management Framework 1.0 (NIST AI 100-1)*, 2023-01. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `NIST-SAMPLING-2026` — NIST/SEMATECH, *e-Handbook of Statistical Methods* §6.2.1–6.2.2 (acceptance sampling), retrieved 2026-10-20. https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm
- `OWASP-LLM01-2025` — OWASP Gen AI Security Project, *LLM01:2025 Prompt Injection*, 2025. https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- `PUBTECH-WHITEMAIL-2025` — PublicTechnology, *DWP taps AI to scan 25,000 letters a day*, 2025-12-08. https://www.publictechnology.net/?p=12665
- `UIPATH-CCA-2026` — UiPath Engineering, *Enterprise Case Classification Agent: Support Ticket Routing with AI*, 2026-01-12. https://engineering.uipath.com/enterprise-case-classification-agent-support-ticket-routing-with-ai-de5c822d8153
- `WILLISON-TRIFECTA-2025` — Simon Willison, *The lethal trifecta for AI agents*, 2025-06-16. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- `WONG-ESM-2021` — Wong et al., *External Validation of a Widely Implemented Proprietary Sepsis Prediction Model*, JAMA Internal Medicine, 2021-08. https://doi.org/10.1001/jamainternmed.2021.2626

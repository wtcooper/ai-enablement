# Service delivery and operations

Function id `service-delivery`. Last reviewed 2026-10-20. Source keys in brackets are listed in §8. **Read this first:** measured,
comparison-group evidence for AI in in-house operations comes mostly from public bodies, because they publish evaluations. The same
task can go both ways: AI summaries saved time with similar decision quality in one government pilot and scored 47% against 81% for
human summaries in another proof of concept [HOMEOFFICE-ASYLUM-2025; ASIC-SENATE-2024]. Test on the organization's own work first.
Private-sector operations examples are vendor-published, with estimates and no quality measures.

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

The in-house team that produces and delivers the organization's core service or product to customers, citizens or patients:
fulfilment, case and application processing, site or field operations, back-office operations and the quality control around them.
Customer contact is the customer-service card. In the archetypes, `service-delivery` mostly tags firms delivering engagements to
clients (assurance testing, tax advice, professional-services work production and delivery management, managed security); for those
firms use the archetype modules, and use this card for operations outside them.

## 2. Processes and key steps

The process list is a working grouping, not a named framework's categories.

| Process | Key steps | Work types | Typical pain |
|---|---|---|---|
| Demand and capacity planning | Forecast volumes; set staffing and schedules; reallocate across queues | coordination-scheduling, data-reporting | No measured AI case found |
| Intake and registration | Receive orders, requests or cases; capture data; check completeness | transaction-processing, client-interaction | Orders arrive by email and need manual entry across up to five systems (Danfoss) [GOOGLE-DANFOSS-2026] |
| Triage, routing and dispatch | Classify; prioritize; assign; book appointments | coordination-scheduling, transaction-processing | Routine scheduling and standardized communications take staff time (DHL) [DHL-HAPPYROBOT-2025] |
| Fulfilment or case work | Gather information; assess against rules; decide; produce; deliver | expert-judgment, transaction-processing, document-production, physical-field | Document-heavy preparation: asylum interview transcripts "can extend to 50 pages or more" [HOMEOFFICE-ASYLUM-2025] |
| Exceptions and escalations | Detect breaks; investigate; approve; resolve | expert-judgment, transaction-processing | Pricing exceptions stay with staff (Danfoss) [GOOGLE-DANFOSS-2026] |
| Quality assurance and rework | Sample or check outputs; record findings; correct | review-assurance | Equality checks need larger samples than pilots give [HOMEOFFICE-ASYLUM-2025] |
| Performance monitoring and reporting | Track cycle time, backlog, quality, cost; trigger action | data-reporting | Value does not reach enterprise level: 37% report any EBIT impact [MCKINSEY-SOAI-2026] |
| Improvement and partner coordination | Root-cause analysis; process change; outsourced work | coordination-scheduling, research-synthesis | Pilots do not reach production: 5% of evaluated enterprise-grade tools, custom or vendor-sold, did (preliminary, interview-based) [MIT-NANDA-2025] |

## 3. Where AI is changing the work

**Improve the step** (assist or augment)

- **Case or transcript summary as a reviewer aid; the decision-maker still reads and decides**
  ([document-to-decision](../patterns/document-to-decision.md), summary step only; augment; step). UK Home Office (immigration): the test
  group reviewed transcripts 23 minutes quicker (a 32% saving) against a comparison group; sustained-decision rates were similar; 9% of
  summaries were removed as inaccurate or incomplete; 23% of users were not fully confident. Government evaluation of small-scale
  pilots; self-logged cases. Grade A [HOMEOFFICE-ASYLUM-2025]. Counter-evidence: Australian Securities and Investments Commission
  (regulator): in a five-week proof of concept, AI summaries of submissions scored 35 of 75 (47%) against 61 of 75 (81%) for humans;
  assessors said the output could create more work. One model, one use case. Grade A (negative) [ASIC-SENATE-2024].
- **Policy and knowledge search over approved sources, with references**
  ([grounded-knowledge-assistant](../patterns/grounded-knowledge-assistant.md); augment; step). UK Home Office: 37 minutes saved per
  case against a comparison group; 82% of queries judged sufficient with references; the user must open the full policy note.
  Self-reported. Grade A [HOMEOFFICE-ASYLUM-2025].
- **Classify and map very large free-text sets, with a person verifying each mapping**
  ([document-to-decision](../patterns/document-to-decision.md); augment; process). UK Department for Work and Pensions with the
  government's AI incubator (public sector): 87,738 consultation responses reviewed by 125 people; F1 0.816 against a single reviewer
  and 0.710 between two reviewers; reviewers changed nothing for 73% of mappings; no evidence of bias by self-reported disability
  status. A government unit evaluating its own tool. Grade A [IAI-CONSULT-DWP-2025].
- **Ambient documentation for frontline professionals** ([draft-review-loop](../patterns/draft-review-loop.md); augment; step). The
  Permanente Medical Group, Kaiser Permanente (healthcare): 7,260 physicians used an AI scribe in 2,576,627 encounters (October 2023 to
  December 2024); the organization's analysis found nearly 16,000 hours of documentation time saved; physicians review and edit each
  note. Grade A [KP-AISCRIBE-2025].
- **General-purpose assistant for everyday admin** (pattern `other`: a personal assistant; assist; step). UK cross-government trial
  (20,000 employees): 26 minutes a day, estimated by users from ranges; the trial could not show how saved time was spent. Grade B
  [GDS-COPILOT-2025]. HM Revenue and Customs: licences allocated at random; self-reported 2-3% of the working week, which HMRC calls "a
  baseline estimate". Grade B [HMRC-COPILOT-2026].
- **Maintenance or repair guidance** (assist; step). Siemens announced a maintenance offering for its industrial assistant; no outcomes.
  Grade C [SIEMENS-COPILOT-2025].

**Automate the flow**

- **Email or order intake to order entry; people handle pricing and other exceptions**
  ([intake-triage](../patterns/intake-triage.md), [document-to-decision](../patterns/document-to-decision.md); automate; process).
  Danfoss (manufacturing): "up to 80%" of transactional decision-making and communication automated; response time "potentially" from
  42 hours to near real time; about five minutes saved per order is the team's estimate; no error or override rate. Vendor customer
  story. Grade B [GOOGLE-DANFOSS-2026].
- **Operational communication agents for scheduling, status calls and coordination**
  ([service-agent-escalation](../patterns/service-agent-escalation.md); automate; step). DHL Supply Chain (logistics): agents handle
  phone and email for appointment scheduling, driver follow-up and warehouse coordination; "measurable impact" claimed without figures.
  Grade B [DHL-HAPPYROBOT-2025].

**Delegate the outcome**

- **Monitor operations, diagnose and act, with an agent owning the loop**
  ([monitor-diagnose-act](../patterns/monitor-diagnose-act.md), [end-to-end-case-agent](../patterns/end-to-end-case-agent.md);
  delegate; process). No cross-industry measured example found. Archetype entries: a PMO agent estate with a human approval gate
  (`professional-services-delivery-management-12`, B); engagements run by teams of people and agents
  (`professional-services-delivery-management-14`, B).

**Reinvent the work**

- **Replace outsourced back-office work with AI-run processes** (automate; model). MIT NANDA's preliminary, anonymized interviews
  report that some of the most dramatic savings came from back-office automation, including ending outsourced (BPO) spend ($2-10
  million a year). Grade C [MIT-NANDA-2025].
- **Managed services delivered by agents with human accountability:** `security-operations-22` (B).

**In the archetypes**: `professional-services-work-production-06` (A, drafting assistant in a randomized trial with blinded scoring),
`professional-services-work-production-07` (A), `professional-services-delivery-management-01` (B),
`professional-services-delivery-management-02` (B), `professional-services-delivery-management-12` (B),
`professional-services-delivery-management-14` (B), `security-operations-05` (B, AI analyst closes the benign majority of
alerts), `security-operations-22` (B).

## 4. Metrics and benchmarks

- **Time per case against a comparison group:** 23 and 37 minutes (Home Office; self-logged) [HOMEOFFICE-ASYLUM-2025].
- **Decision quality as a control:** sustained-decision rate from an existing quality tool, similar in test and comparison groups;
  dip-sample sizes not stated [HOMEOFFICE-ASYLUM-2025].
- **Rejection before use:** 9% of AI summaries removed after specialist review [HOMEOFFICE-ASYLUM-2025].
- **Agreement with a human baseline:** tool-to-reviewer F1 0.816 against reviewer-to-reviewer 0.710; median review 19 seconds per
  response [IAI-CONSULT-DWP-2025].
- **Blind rubric against human work:** 47% against 81% [ASIC-SENATE-2024].
- **Self-estimated time:** 26 minutes a day [GDS-COPILOT-2025]; 2-3% of the working week, reduced about 20% for non-use
  [HMRC-COPILOT-2026].
- **Documentation hours:** nearly 16,000 hours across 2.58 million encounters [KP-AISCRIBE-2025].
- **Enterprise value:** 37% of respondents report any EBIT impact, unchanged from 2025; cost reductions most often in supply chain,
  service operations and manufacturing [MCKINSEY-SOAI-2026].

## 5. Interview probes

1. "Pick one queue. What are the volume, handling time per item and share needing judgment, and how do you know?" Reveals whether
   baselines exist; the Home Office could measure because case logs and a quality tool existed [HOMEOFFICE-ASYLUM-2025].
2. "Show me what a person sees when they review the AI output. Can they trace each statement to the source?" Reveals review effort;
   summaries without references limited time saved for some users [HOMEOFFICE-ASYLUM-2025].
3. "How often do two of your people agree on this work today?" Reveals whether accuracy can be defined; two reviewers agreed with each
   other less than the tool agreed with one [IAI-CONSULT-DWP-2025].
4. "Which exceptions go to a senior person, and what should the system do instead of guessing?" Reveals the escalation design
   [GOOGLE-DANFOSS-2026].
5. "If we test a model on your own documents, what would failure look like, and who would score it blind?" Reveals appetite for a
   blind test [ASIC-SENATE-2024].
6. "Who gets the time back, and what will they do with it?" Reveals whether capacity has a destination [GDS-COPILOT-2025;
   MCKINSEY-SOAI-2026].
7. "Which systems would an agent need to read or write, and who owns each?" Reveals integration load; Gartner says integrating agents
   into legacy systems "can be technically complex" [GARTNER-AGENTIC-2025].
8. "What do your newest people do differently from your experienced ones?" Reveals where assistance may help most; novices gained most
   in a customer-support study (adjacent) [NBER-BRYNJOLFSSON-2023].
9. "If the automation were switched off on Monday, could the team still do the work?" Reveals skill erosion and the need for a manual
   fallback [BAINBRIDGE-1983].
10. "What outsourced or contracted work could AI do, and do the contracts allow change?" Reveals model-level options [MIT-NANDA-2025].

## 6. Guardrails

- **Keep the decision with the person.** The Home Office designed its tools so decision-makers "cannot use the tool by itself to make
  a decision" [HOMEOFFICE-ASYLUM-2025].
- **Decide what the reviewer must see.** Citations are a design choice that changes review effort [HOMEOFFICE-ASYLUM-2025].
- **Exceptions stay with staff** (Danfoss pricing exceptions) [GOOGLE-DANFOSS-2026].
- **Watch over-reliance and skill erosion.** Automation leaves operators the hard residual tasks and erodes the skill needed for them
  [BAINBRIDGE-1983]; the EU AI Act asks overseers of high-risk systems to "remain aware" of over-reliance [EU-AIACT-ART14-2024].
- **Plan monitoring with appeal and override** after deployment, and record who overrode what [NIST-AIRMF-2023].
- **Classify each use.** AI used by public authorities to evaluate eligibility for essential public benefits is high-risk under the
  EU AI Act; most internal operations uses are not listed, so check per use [EU-AIACT-ANNEX3-2024].
- **Decisions that need human judgment:** the case decision; exceptions and pricing; anything irreversible for the customer;
  sub-group fairness conclusions.

## 7. Roles and how they evolve

- **Reviewers become verifiers:** reviewers check and amend each mapping; decision-makers read a summary, then decide
  [IAI-CONSULT-DWP-2025; HOMEOFFICE-ASYLUM-2025].
- **Fewer systems, faster onboarding:** Danfoss staff moved from up to five systems to one interface and focus on "value-added
  activities" [GOOGLE-DANFOSS-2026].
- **Novices gain most** in an adjacent customer-support study (34% for novice and low-skilled workers) [NBER-BRYNJOLFSSON-2023].
- **Strain is uneven:** 47% of mid-level managers and individual contributors report AI-related strain, against 31% of executives
  [MCKINSEY-SOAI-2026].

## 8. Sources

- **ASIC-SENATE-2024**: ASIC, *Response to question on notice 001 and Generative AI Document Summarisation Proof of Concept*, Senate Select Committee on Adopting AI (regulator, 2024-07-05). https://www.aph.gov.au/DocumentStore.ashx?id=b4fd6043-6626-4cbe-b8ee-a5c7319e94a0
- **BAINBRIDGE-1983**: Lisanne Bainbridge, *Ironies of Automation*, Automatica 19(6) (academic, 1983). https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf
- **DHL-HAPPYROBOT-2025**: DHL Group, *DHL boosts operational efficiency and customer communications with AI agents* (firm release, 2025-11-11). https://group.dhl.com/en/media-relations/press-releases/2025/dhl-boosts-operational-efficiency-and-customer-communications-with-happyrobots-ai-agents.html
- **EU-AIACT-ANNEX3-2024**: Regulation (EU) 2024/1689, *Annex III: High-risk AI systems* (regulation text, 2024). https://artificialintelligenceact.eu/annex/3/
- **EU-AIACT-ART14-2024**: Regulation (EU) 2024/1689, *Article 14: Human oversight* (regulation text, 2024). https://artificialintelligenceact.eu/article/14/
- **GARTNER-AGENTIC-2025**: Gartner, *Over 40% of Agentic AI Projects Will Be Canceled by End of 2027* (analyst prediction, 2025-06-25). https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- **GDS-COPILOT-2025**: Government Digital Service, *M365 Copilot Experiment Findings Report* (government evaluation, 2025-06-02). https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf
- **GOOGLE-DANFOSS-2026**: Google Cloud, *Danfoss: Reimagining order management at scale* (vendor customer story, 2026-02, earliest archived copy). https://cloud.google.com/customers/danfoss
- **HMRC-COPILOT-2026**: HM Revenue and Customs, *Evaluating the Impact of Microsoft Copilot in HMRC* (government evaluation, 2026-07-09). https://www.gov.uk/government/publications/evaluation-report-phase-3-trial-of-microsoft-copilot/evaluating-the-impact-of-microsoft-copilot-in-hmrc
- **HOMEOFFICE-ASYLUM-2025**: UK Home Office, *Evaluation of AI trials in the asylum decision making process* (government evaluation, 2025-04-29). https://www.gov.uk/government/publications/evaluation-of-ai-trials-in-the-asylum-decision-making-process/evaluation-of-ai-trials-in-the-asylum-decision-making-process
- **IAI-CONSULT-DWP-2025**: Incubator for AI (UK government), *Consult Evaluation: DWP's Pathways to Work consultation* (government evaluation, 2025-10, from the publication asset date). https://assets.publishing.service.gov.uk/media/68f63fe01c9076042263f0bd/evaluation-report.pdf
- **KP-AISCRIBE-2025**: Kaiser Permanente Division of Research, *AI-assisted notetaking gains steady support from Kaiser Permanente physicians* (firm, 2025-04-01). https://divisionofresearch.kaiserpermanente.org/ai-assisted-notetaking-gains-steady-support-from-kaiser-permanente-physicians/
- **MCKINSEY-SOAI-2026**: McKinsey, *The state of AI in 2026: On the road to ROI* (survey, n=1,719, 2026-08-25). https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- **MIT-NANDA-2025**: MIT Project NANDA, *The GenAI Divide: State of AI in Business 2025* (preliminary, interview-based, 2025-07). https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- **NBER-BRYNJOLFSSON-2023**: Brynjolfsson, Li, Raymond, *Generative AI at Work*, NBER Working Paper 31161 (academic, 2023-11). https://www.nber.org/papers/w31161
- **NIST-AIRMF-2023**: NIST, *AI Risk Management Framework 1.0* (standard-setter, 2023-01). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **SIEMENS-COPILOT-2025**: Process Worldwide, *Expansion of Industrial Copilot with New Generative AI-Powered Maintenance Offering* (press, 2025-03-29). https://www.process-worldwide.com/expansion-of-industrial-copilot-with-new-generative-ai-powered-maintenance-offering-a-8d2a08a7783bcfcd5119b473ef49c638/

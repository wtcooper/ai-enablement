# Risk, compliance and legal

Function id `risk-compliance-legal`. Last reviewed 2026-10-20. Source keys in brackets are listed in §8. **Read this first:** the
strongest measured result is a before-and-after on a high-volume screening step (HSBC); the strongest warnings are about autonomy
(Michigan's automated fraud system) [HSBC-GOOGLE-2023; UMICH-MIDAS-2024]. US and UK financial regulators and prosecutors are asking for evidence of
control rather than new AI-specific rules; the EU AI Act is the exception [FCA-AIAPPROACH-2025; DOJ-ECP-2024]. In-house legal is well surveyed, but its private-sector cases are vendor-published with unstated methods, and no
source publishes override or escalation rates for in-house legal or compliance AI.

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

In-house teams that identify and manage risk, keep the organization within law and policy, and give legal advice and contracts; in
financial services this includes financial-crime compliance, and in the public sector payment integrity and fraud control. Firms that
sell legal, audit or tax work are the professional-services, assurance and tax archetypes. Security governance, risk and compliance
is the security archetype (`governance-risk` module).

## 2. Processes and key steps

The process list is a working grouping, not a named framework's categories.

| Process | Key steps | Work types | Typical pain |
|---|---|---|---|
| Risk identification and assessment | Register; likelihood and impact; appetite; report | data-reporting, expert-judgment | No measured cross-industry case found |
| Policy and control framework | Draft and update policies; map controls to obligations; attest | document-production, review-assurance | Training gaps: 64% of corporate professionals had no generative AI training (2025 survey) [TR-GENAI-2025] |
| Regulatory change and obligations | Monitor; interpret; map to policies and controls; brief owners | research-synthesis, expert-judgment | No measured cross-industry case found |
| Compliance monitoring and testing | Screen transactions or communications; test controls; investigate alerts | transaction-processing, review-assurance, data-reporting | False positives swamp investigators: HSBC screens over 1.2 billion transactions a month and its rules produced many false positives [HSBC-GOOGLE-2023] |
| Customer and third-party due diligence | Collect documents; screen; score; approve; re-screen | transaction-processing, research-synthesis | 33% of AI use cases in UK financial services are third-party implementations [BOE-FCA-AISURVEY-2024] |
| Contract lifecycle | Intake; draft from template; review against playbook; negotiate; sign; track obligations | document-production, review-assurance, expert-judgment | Volume: Luminance's own legal team handled "over 50 contracts each day" [TECHUK-LUMINANCE-2024] |
| Legal advice, research and matters | Research; advise; manage outside counsel | expert-judgment, research-synthesis, coordination-scheduling | Invented legal content: leading research tools hallucinated 17-33% of the time in a 2024 test [STANFORD-MAGESH-2024]; outside-counsel cost [ACC-EVERLAW-2025] |
| Investigations and regulator engagement | Open case; gather evidence; decide; report; remediate | expert-judgment, coordination-scheduling, document-production | No measured case found |
| Governance of the organization's own AI | Inventory uses; approve tools; set oversight; monitor; report incidents | review-assurance, coordination-scheduling | US prosecutors ask how quickly the company can "detect and correct decisions made by AI" [DOJ-ECP-2024] |

## 3. Where AI is changing the work

**Improve the step** (assist or augment)

- **Fraud-risk referral model with a person always deciding** ([intake-triage](../patterns/intake-triage.md); augment; step). UK
  Department for Work and Pensions (benefits): high-risk advance requests go to an employee who decides, mixed with control-group
  referrals, and the reviewer does not see the risk rating; the annual fairness analysis found, for some age groups and non-UK
  nationals, higher referral likelihood without higher likelihood of a correct referral, and the model will be retrained; approved referred
  advances were paid a median 1 day later than automatically approved ones. Self-reported, including unfavourable findings. Grade A [DWP-UCADV-2025].
- **In-house contract first-pass review and redlining, with a lawyer approving each change**
  ([draft-review-loop](../patterns/draft-review-loop.md); augment; step). Inspired Thinking Group (marketing and technology): a 60%
  cut in contract review time "recorded during the pilot"; no method. Grade B [QANOONI-ITG-2026]. Luminance's own legal team: review
  time down "over 60%"; no baseline or method; vendor's own team. Grade B [TECHUK-LUMINANCE-2024]. A randomized study with law
  students found quality gains in four of six legal tasks but not in the one transactional drafting task (an NDA); idea (experiment
  only), grade D [UMN-SCHWARCZ-2025; LAWNEXT-2025].
- **Grounded legal research assistant with citations** ([grounded-knowledge-assistant](../patterns/grounded-knowledge-assistant.md);
  assist to augment; step). Evaluations, not in-house deployments: in a preregistered 2024 test, one leading tool answered 65% of
  queries accurately and another 42%, with hallucination between 17% and 33% [STANFORD-MAGESH-2024]; a 2025 third-party benchmark
  scored four products at 74-78% against 69% for a lawyer baseline on 200 research questions [VALS-VLAIR-2025]. Test on the team's own
  questions.

**Automate the flow**

- **Machine-learning scoring of transactions in place of rules; investigators work the alerts**
  ([full-population-testing](../patterns/full-population-testing.md); automate; step). HSBC (banking): comparing 12 months after
  go-live with the 12 months before, two to four times as much suspicious activity identified and 60% fewer alerts, with a stated
  method (seasonality adjusted, first month excluded). Self-reported by an HSBC financial-crime executive on a vendor's blog. Grade A
  [HSBC-GOOGLE-2023].
- **Payment-integrity screening** ([monitor-diagnose-act](../patterns/monitor-diagnose-act.md); automate; step). US Treasury: $1 billion
  of FY2024 recovery attributed to machine-learning check-fraud identification and $2.5 billion of prevention to prioritizing high-risk
  transactions; no method or false-positive figures. Grade A [TREASURY-2024].
- **Template contracts generated by non-lawyers, and a legal front door**
  ([service-agent-escalation](../patterns/service-agent-escalation.md); automate; process). Luminance: helpdesk response under an hour,
  "over 90%" of work kept in-house (no method). Grade B [TECHUK-LUMINANCE-2024]. Archetype: `professional-services-acceptance-risk-14` (B).
- **Counter-example: automated fraud determinations with limited oversight** (automate; process). Michigan Unemployment Insurance
  Agency (public sector): the error rate reached 93% and about 40,000 people were wrongly accused (per a university summary of the
  case); a $20 million settlement for about 3,000 plaintiffs was approved in January 2024. Grade B [UMICH-MIDAS-2024].

**Delegate the outcome**

- No in-house deployment with published results was found. FINRA flags agent risks of autonomy without validation, acting beyond
  scope and hard-to-trace reasoning [FINRA-GENAI-2025]. In UK financial services, 2% of AI use cases are fully autonomous
  [BOE-FCA-AISURVEY-2024].

**Reinvent the work**

- **Move work from outside counsel to the in-house team** (augment; model). Survey expectations: 64% of in-house professionals expect
  to rely less on outside counsel; 78% expect to insource drafting, 71% contract management, 62% research (vendor co-sponsored).
  Grade C [ACC-EVERLAW-2025]. Archetype: `professional-services-work-production-19` (B).

**In the archetypes**: `security-governance-risk-01` (A, security questionnaires answered from an approved knowledge base),
`security-governance-risk-05` (A, mapping controls across frameworks), `security-ai-security-23` (A), `tax-controversy-15` (A, AI risk
targeting at tax authorities), `professional-services-acceptance-risk-14` (B), `professional-services-work-production-18` (B),
`professional-services-work-production-19` (B), `professional-services-knowledge-management-13` (B).

## 4. Metrics and benchmarks

- **Detection and alert load:** suspicious activity identified and alert volume, measured pre and post (HSBC) [HSBC-GOOGLE-2023].
- **Referral accuracy by group:** referral likelihood against correct-referral likelihood per group (DWP) [DWP-UCADV-2025].
- **Recovered and prevented value:** over $4 billion in FY2024 against $652.7 million in FY2023 (self-reported) [TREASURY-2024].
- **Legal research accuracy:** 65% and 42% accuracy; 17-33% hallucination [STANFORD-MAGESH-2024]; 74-78% against a 69% lawyer
  baseline [VALS-VLAIR-2025].
- **Legal task productivity (randomized, law students):** gains of about 38% to 115% with one tool and 34% to 140%
  with another, in five of six tasks (speed, not quality) [UMN-SCHWARCZ-2025; LAWNEXT-2025].
- **Financial-sector use:** 75% of surveyed UK firms use AI; 55% of use cases involve some automated decision-making, 24%
  semi-autonomous, 2% fully autonomous [BOE-FCA-AISURVEY-2024].
- **In-house adoption:** generative AI use in corporate law "more than doubles in a single year" (657 respondents, 30 countries;
  year-on-year comparisons US only; vendor co-sponsored) [ACC-EVERLAW-2025].

## 5. Interview probes

1. "Which decisions about a person or a transaction does the team make, and for which must a person decide?" Reveals the autonomy
   boundary [DWP-UCADV-2025; UMICH-MIDAS-2024].
2. "What are your alert volume, false-positive rate and cost per alert?" Reveals whether a scoring change has a baseline
   [HSBC-GOOGLE-2023].
3. "How would you know the model is wrong for some groups or cases?" Reveals monitoring maturity [DWP-UCADV-2025; DOJ-ECP-2024].
4. "Do you have an inventory of AI used in the function, including inside vendor tools?" Reveals governance gaps
   [BOE-FCA-AISURVEY-2024; FINRA-GENAI-2025].
5. "What does your policy say on approved tools, and what training have people had?" Reveals the policy and training gap
   [TR-GENAI-2025; ACC-EVERLAW-2025].
6. "Who checks citations and authorities before anything leaves the team, and how is it recorded?" Reveals verification practice;
   courts are recording fabricated citations [STANFORD-MAGESH-2024; CHARLOTIN-2026].
7. "Which contract types are routine enough for templates or a playbook, and which are never touched without a lawyer?" Reveals the
   split between automate and augment [TECHUK-LUMINANCE-2024; QANOONI-ITG-2026].
8. "If a prosecutor asked what baseline of human decision-making you compare the AI against, what would you show?" Reveals
   measurement readiness [DOJ-ECP-2024].
9. "What do you tell customers, investors and clients about your AI use, and who verifies it?" Reveals "AI washing" and
   chatbot-statement exposure [SEC-2024-36; MCCARTHY-MOFFATT-2024].
10. "How much outside-counsel spend could move in-house, and what would the team stop doing to make room?" Reveals whether a
    model-level change is intended [ACC-EVERLAW-2025].

## 6. Guardrails

- **Show evidence of control.** US prosecutors ask what "baseline of human decision-making" is used to assess AI, how accountability
  is enforced and how fast AI decisions are detected and corrected [DOJ-ECP-2024]. FINRA lists testing, prompt and output logs,
  model-version tracking and human review [FINRA-GENAI-2025]. The FCA relies on existing frameworks such as the Consumer Duty and
  senior-manager accountability [FCA-AIAPPROACH-2025].
- **EU AI Act.** High-risk systems must allow effective human oversight with awareness of automation bias [EU-AIACT-ART14-2024];
  deployers assign oversight to people with "competence, training and authority" [EU-AIACT-ART26-2024]. Annex III includes
  creditworthiness (excluding fraud detection), eligibility for essential public benefits, employment and judicial uses; check each
  in-house use case by case [EU-AIACT-ANNEX3-2024].
- **Design a person who really decides:** DWP's reviewer does not see the risk rating or know the referral came from the model
  [DWP-UCADV-2025]. Plan "appeal and override" in post-deployment monitoring [NIST-AIRMF-2023].
- **Claims about AI must be true:** the SEC settled with two investment advisers over false statements about AI use, $400,000 in total
  penalties [SEC-2024-36]. A tribunal held Air Canada liable for its chatbot's advice and awarded $650.88 in damages plus interest and fees
  [CRT-2024; MCCARTHY-MOFFATT-2024].
- **Decisions that need human judgment:** approving or declining a referred claim [DWP-UCADV-2025]; each suggested contract change
  [QANOONI-ITG-2026]; alert dispositions [HSBC-GOOGLE-2023]; legal advice that leaves the team; regulator engagement.

## 7. Roles and how they evolve

- **Investigators spend more time on genuinely suspicious cases** as alert volume falls [HSBC-GOOGLE-2023].
- **Lawyers review and approve AI-proposed edits with citations** and stay responsible for approvals [QANOONI-ITG-2026].
- **Non-lawyers generate contracts from approved templates** behind a legal helpdesk [TECHUK-LUMINANCE-2024].
- **Work moves in-house,** and 61% of surveyed in-house professionals plan to push for change in how legal services are delivered and
  priced [ACC-EVERLAW-2025].
- **Juniors who no longer draft first versions** face the skill-erosion risk Bainbridge describes (advisor inference from the paper)
  [BAINBRIDGE-1983].

## 8. Sources

- **ACC-EVERLAW-2025**: Everlaw with the Association of Corporate Counsel, *64% of In-House Counsel Expect GenAI to Reduce Reliance on Outside Counsel* (survey release, 2025-10-14). https://blog.everlaw.com/press/release/acc-report-2025
- **BAINBRIDGE-1983**: Lisanne Bainbridge, *Ironies of Automation*, Automatica 19(6) (academic, 1983). https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf
- **BOE-FCA-AISURVEY-2024**: Bank of England and FCA, *Artificial intelligence in UK financial services - 2024* (regulator, 2024-11-21). https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024
- **CRT-2024**: British Columbia Civil Resolution Tribunal, *Moffatt v. Air Canada, 2024 BCCRT 149* (tribunal decision, 2024-02-14). https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do
- **CHARLOTIN-2026**: Damien Charlotin, *AI Hallucination Cases Database* (community, live database, 2026-10). https://www.damiencharlotin.com/hallucinations/
- **DOJ-ECP-2024**: US Department of Justice, *Evaluation of Corporate Compliance Programs* (regulator, 2024-09). https://www.justice.gov/criminal/criminal-fraud/page/file/937501/dl
- **DWP-UCADV-2025**: UK Department for Work and Pensions, *Universal Credit Advances Model: Fairness Assessment* (government, 2025-07-17). https://assets.publishing.service.gov.uk/media/6876219388da2e5804bb6a17/UC_Advances_model_fairness_assessment_-_July_2025.pdf
- **EU-AIACT-ANNEX3-2024**: Regulation (EU) 2024/1689, *Annex III: High-risk AI systems* (regulation text, 2024). https://artificialintelligenceact.eu/annex/3/
- **EU-AIACT-ART14-2024**: Regulation (EU) 2024/1689, *Article 14: Human oversight* (regulation text, 2024). https://artificialintelligenceact.eu/article/14/
- **EU-AIACT-ART26-2024**: Regulation (EU) 2024/1689, *Article 26: Obligations of deployers of high-risk AI systems* (regulation text, 2024). https://artificialintelligenceact.eu/article/26/
- **FCA-AIAPPROACH-2025**: Financial Conduct Authority, *AI and the FCA: our approach* (regulator, 2025-09-08). https://www.fca.org.uk/firms/innovation/ai-approach
- **FINRA-GENAI-2025**: FINRA, *2026 Annual Regulatory Oversight Report: GenAI* (regulator, 2025-12-09). https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai
- **HSBC-GOOGLE-2023**: Richard May (HSBC) on the Google Cloud blog, *Fighting money launderers with artificial intelligence at HSBC* (self-reported on a vendor blog, 2023-11-30). https://cloud.google.com/blog/topics/financial-services/how-hsbc-fights-money-launderers-with-artificial-intelligence
- **LAWNEXT-2025**: LawSites, *Another new study of legal AI shows some models can significantly improve work quality and efficiency* (press, 2025-03-05). https://lawnext.com/2025/03/another-new-study-of-legal-ai-shows-some-models-can-significantly-improve-work-quality-and-efficiency.html
- **MCCARTHY-MOFFATT-2024**: McCarthy Tetrault, *Moffatt v. Air Canada: A Misrepresentation by an AI Chatbot* (law firm commentary, 2024-02). https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot
- **NIST-AIRMF-2023**: NIST, *AI Risk Management Framework 1.0* (standard-setter, 2023-01). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **QANOONI-ITG-2026**: Legal Futures (vendor associate content), *In-house team cuts contract review time by 60% after AI pilot in Microsoft Word* (vendor-written associate content, 2026-02-04). https://www.legalfutures.co.uk/associate-news/in-house-team-cuts-contract-review-time-by-60-after-ai-pilot-in-microsoft-word/
- **SEC-2024-36**: US Securities and Exchange Commission, *SEC Charges Two Investment Advisers with Making False and Misleading Statements About Their Use of AI* (regulator, 2024-03). https://www.sec.gov/newsroom/press-releases/2024-36
- **STANFORD-MAGESH-2024**: Magesh et al., *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools* (academic, arXiv 2405.20362, 2024-05-30). https://arxiv.org/abs/2405.20362
- **TECHUK-LUMINANCE-2024**: techUK, *AI adoption case study: Luminance's legal team reduced time spent on contract review with AI* (vendor case study, 2024-10-13). https://www.techuk.org/insights/guest-insights/ai-adoption-case-study-learn-how-luminance-s-legal-team-reduced-time-spent-on-contract-review-with-ai
- **TR-GENAI-2025**: Thomson Reuters Institute, *2025 Generative AI in Professional Services Report* (survey release, 2025-04-15). https://thomsonreuters.com/en/press-releases/2025/april/from-incubation-to-integration-generative-ai-adoption-nearly-doubles-as-professional-services-reach-crossroads
- **TREASURY-2024**: US Department of the Treasury, *Enhanced Fraud Detection Processes, Including Machine Learning AI, Prevented and Recovered Over $4 Billion in Fiscal Year 2024* (government release, 2024-10-17). https://home.treasury.gov/news/press-releases/jy2650
- **UMICH-MIDAS-2024**: University of Michigan Ford School, *Case Over the Michigan Unemployment Insurance Agency's Faulty Automated System Finally Settled* (academic, 2024). https://stpp.fordschool.umich.edu/sites/stpp/files/2024-08/stpp-midas-explainer.pdf
- **UMN-SCHWARCZ-2025**: Schwarcz et al., *AI-Powered Lawyering: AI Reasoning Models, Retrieval Augmented Generation, and the Future of Legal Practice* (academic, 2025-03). https://www.governance.ai/research-paper/ai-powered-lawyering-ai-reasoning-models-retrieval-augmented-generation-and-the-future-of-legal-practice
- **VALS-VLAIR-2025**: Vals AI, *VLAIR - Legal Research* (third-party benchmark, 2025-10-14). https://www.vals.ai/industry-reports/vlair-10-14-25

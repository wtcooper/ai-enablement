# Security governance, risk and compliance (security)

Last reviewed 2026-10-17. Use cases live in `../use-cases/governance-risk.yaml` (21 entries). Ids are shortened here:
`#05` means `security-governance-risk-05`. Source keys in brackets are in the YAML or in §10.
Read this first: every outcome figure for AI in GRC work is **vendor-published** on a GRC vendor's own site (Vanta,
Conveyor, Whistic, Hyperproof, Safe Security) and quotes the customer. No override rate, error rate, parallel run,
auditor-reliance study or regulator inspection finding exists for AI used in GRC work. The independent numbers are
small lab studies and surveys. 13 of 21 entries are graded A or B; the two A grades (`#01`, `#05`) rest on vendor
case studies. Say "vendor-published" whenever you quote a figure. Regulation and workforce at archetype level are in
the cross-cutting research files `research/runs/wave4/security-x-guardrails-regulation.md` and
`research/runs/wave4/security-x-workforce-talent.md`; this file links to them rather than repeating them.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

Security governance, risk and compliance (GRC): answering customers' security reviews, assessing vendors (third-party
risk management, TPRM), running control frameworks such as SOC 2 and ISO 27001 and their audits, writing policy,
keeping the risk register, quantifying cyber risk and reporting to boards and regulators. It also covers two things
the landscape scan asked to add: the security team's own AI policy (and its role as AI policy author for the
business), and the security workforce and operating model. Security architecture is treated as a lens here, mostly
as approval gates and limits on agents. Runtime controls for agents belong to ai-security; AI incident handling to
incident-response.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Customer security reviews | Answer questionnaires; share audit reports through a trust centre (a portal of security documents) | client-interaction, document-production | 60% of surveyed teams run reviews with 2 or fewer people (vendor survey) [CONVEYOR-BENCH-2026]; 300+ questionnaires in a short time at GitHub after a launch [VANTA-GITHUB-2026] |
| Vendor intake and assessment | Tier the vendor, collect SOC 2, pen test and questionnaire, decide inherent and residual risk | review-assurance | About 130 reviews a month at Samsara [VANTA-SAMSARA-2026]; "a paper exercise" in large firms [CLOUDSECPOD-LOVABLE-2026] |
| Vendor monitoring | Reassess after new reports, subprocessors, incidents or new AI features | review-assurance, coordination-scheduling | Approvals are point-in-time; embedded vendor AI is hard to see [TECHTARGET-AIREG-2026] |
| Control framework and mapping | Keep a common control set mapped to each framework | review-assurance, document-production | 820 duplicated controls across 10 frameworks at Samsara [VANTA-SAMSARA-2026] |
| Evidence and control monitoring | Collect evidence, check it against each control's baseline, chase owners | review-assurance, data-reporting | Manual compliance work was 60% of Perforce's team time [VANTA-PERFORCE-2026]; screenshots and spreadsheets [BLEEPING-ANECDOTES-2026] |
| Control testing and audits | Test controls, write workpapers, answer auditor requests | review-assurance, document-production | 70 hours of expert interviews per audit cycle at Samsara [VANTA-SAMSARA-2026] |
| Policy and standards | Draft, update, check against standards and practice | document-production, review-assurance | Gaps found only in a thorough audit [ARXIV-2607.22885] |
| Regulatory mapping | Track rules (EU AI Act, NIS2, DORA, SEC) and map them to controls | research-synthesis | Fragmented, volatile AI rules [TECHTARGET-AIREG-2026] |
| Risk register and assessment | Intake, triage, scenario analysis, treatment | expert-judgment | Classifying and linking risks by hand [ANTHROPIC-JOB-RISKANALYST-2026] |
| Risk quantification | Frequency and loss estimates in money (FAIR: a method for expressing cyber risk in financial terms) | data-reporting, expert-judgment | Expert time; estimates go stale [ANTHROPIC-JOB-RISKENG-2026] |
| Board and regulator reporting | Board packs, disclosures, notifications | document-production, data-reporting | Five to ten minutes with the board; reports framed around security, not business [TECHTARGET-BOARD-2026] |
| AI governance for the business | Acceptable-use policy, AI vendor review, approval gates | expert-judgment, review-assurance | 79% of CISOs expected to manage AI risk without proportional resources [PROOFPOINT-VOC-2026] |
| The security team's own AI use | Approved tools, logging, autonomy limits, AI incident playbooks | review-assurance, document-production | 79% of SOCs use AI, 36% in a defined workflow [SANS-SOC-2026] |
| Workforce and operating model | Roles, hiring, training, career paths | coordination-scheduling | Skills, not headcount, bind (60/40) [RSAC-WORKFORCE-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome with checkpoints), reinvent (the service or operating model changes). In every deployment found, a
person still decides residual risk, approves mappings and policy, and owns what goes to auditors, boards and
regulators.

**Customer assurance**
- Automate: `#01` questionnaires answered from an approved knowledge base; uncertain answers go to an analyst. GitHub
  automated 93% of inbound questionnaires in six months; Carta reports 83% less review time and 95% accuracy
  (vendor-published, grade A).
- Automate: `#02` a trust centre with an AI agent answers questions before they reach the team; Synthesia resolves
  20-30% of customer questions this way, portal and agent combined (grade B).

**Third-party risk**
- Delegate: `#03` an agent collects vendor documents, extracts exceptions, drafts the evaluation and follow-ups; the
  analyst decides residual risk. Samsara "up to 50% faster" (no baseline); Anthropic, Plaid and OpenAI postings
  describe the work (grade B).
- Improve: `#04` trigger-based reassessment instead of annual reviews, extended (as an idea) to AI features and agents
  vendors add after approval (grade B on one posting).

**Controls, evidence and audits**
- Improve: `#05` an agent proposes a common control set and maps evidence; Samsara went from 820 to 260 controls
  (grade A). Vanta's own mapping precision rose from below 35% to 78% on an offline test set.
- Automate: `#06` connectors and agents collect evidence and flag drift continuously; owners get the exceptions.
  Synthesia 60% of evidence collection automated, AI and non-AI not separated (grade B).
- Delegate: `#07` agents test controls on the full evidence set and assemble workpapers (Optro, announced, grade C).
- Improve: `#15` AI drafts audit responses and one evidence set serves several audits; Synthesia ran five framework
  audit cycles in one month (grade B).
- Improve: `#16` verify automated attestations: spot-check 5 to 10 controls and confirm the auditor ran its own tests
  (IANS after the disputed Delve allegations, grade C).

**Policy and regulation**
- Improve: `#08` drafting and upkeep of policies (Synthesia, grade B). `#09` gap analysis of policy against a
  standard or against practice (Calastone; ReCon lab benchmark 80.65% agreement with experts, grade B).
- Improve: `#10` mapping AI and security regulations into controls from shared principles (postings, Gartner; grade C).

**Risk**
- Improve: `#11` risk intake triage and first-draft analyses (Anthropic, Plaid postings; grade B). Five LLMs
  consistently underestimated risk against 50 experts [ARXIV-2605.05424].
- Improve: `#12` quantification with AI scoping, data gathering and LLM "expert panels" (lab r = 0.91-0.98; 80% of a
  sponsored survey use or test AI; grade C).
- Improve: `#13` risk analyses extended to the firm's own agents, model providers and coding agents (FAIR guidance,
  grade C). `#14` board packs drafted from programme data and re-based for AI-accelerated exploitation (grade C).

**AI governance and the operating model (reinvent)**
- `#17` the security team becomes AI policy author and reviewer for the business (Cengage: 67 AI vendors assessed in
  15 months, self-reported; grade B).
- `#18` the security function's own AI-use policy: approved tools, logged prompts and outputs, autonomy tiers, AI
  incident playbooks (Trail of Bits handbook; grade B).
- `#19` GRC engineering: engineers and analysts build automation and agents inside GRC (seven employers' postings,
  grade B). `#20` roles redesigned around AI oversight, with training (surveys, grade C). `#21` deliberate
  apprenticeship for juniors (idea, grade D).

Coverage: all four ladder levels and all three scopes have entries. Thin cells: automate (three entries, none at
model scope); delegate (`#03` B, `#07` announced, `#20` survey-based); model scope has no measured outcome. Related
entries elsewhere: ai-security-21/22/24 (AI inventory, governance, AI vendor assurance), ai-security-07/08/12 and
operations-19/20 (agent gates and logs), incident-response-02/15/16/17 (tabletops, regulator notifications,
post-incident review, AI-agent incidents), identity-access-11 (policy as code).

## 4. Interview probes

1. **When a tool drafts a questionnaire answer or vendor assessment, what share goes out unchanged, and do you log
   overrides?** Reveals whether anyone measures quality; no published override rate exists anywhere (`#01`, `#03`).
2. **Which documents may the AI answer from, who keeps them current, and what happens when they contradict a
   contract or audit report?** Reveals knowledge-base readiness; Carta cleaned up documentation first (`#01`).
3. **Have your auditors said what they will accept from AI-prepared evidence or workpapers (sampling, prompts, logs)?**
   Reveals the biggest unknown for `#06`, `#07`, `#15`; no source documents auditor reliance.
4. **How many controls do you carry across frameworks, and how many duplicate each other?** Reveals the size of the
   mapping prize (`#05`: 820 to 260 at Samsara).
5. **What triggers a vendor reassessment today, and how would you find AI features a vendor added after approval, or
   tools your own staff built?** Reveals readiness for `#04` and the "mini vendor" problem.
6. **How do you check a compliance platform or auditor: have you spot-checked controls or confirmed the auditor ran
   its own tests?** Reveals attestation risk after the Delve allegations (`#16`).
7. **Which risk-register entries and board metrics assume pre-AI patch windows or exploit scarcity, and when did you
   last revisit them?** Reveals whether `#13` and `#14` are needed; CSA asks for an update within 45 days.
8. **How do you quantify risk today (heat map, money, scenarios), and who calibrates AI-produced estimates?** Reveals
   fit for `#12`; LLMs understated risk against experts.
9. **Who writes the policy on staff and agent use of AI, who approves agent actions on sensitive data, and have you
   rehearsed an AI-related incident?** Reveals the state of `#17` and `#18`.
10. **Which AI uses in your own security team have a named owner, an approved-tool list and logged prompts, outputs
    and model versions?** Reveals whether the team governs its own AI (`#18`).
11. **If vendor reviews or customer requests doubled next quarter, what would you automate first and what would you
    refuse to automate?** Reveals appetite and the human lines (`#01`-`#04`).
12. **Who in GRC can read a system configuration or call an API, and where will juniors learn judgment if evidence
    collection disappears?** Reveals fit for `#19` and the pipeline risk (`#21`).

## 5. Metrics and benchmarks

| Metric | Figure | Source (provenance) |
|---|---|---|
| Questionnaires automated | 93% of inbound in 6 months (GitHub; goal was 12) | [VANTA-GITHUB-2026] (vendor-published) |
| Time on customer security reviews | 83% less; 95% "AI accuracy", method not stated (Carta) | [CONVEYOR-CARTA-2026] (vendor-published) |
| Questions resolved without staff | 20-30%, portal and agent combined (Synthesia) | [VANTA-SYNTHESIA-2026] (vendor-published) |
| Vendor review time | "up to 50% faster", about 130 reviews a month (Samsara) | [VANTA-SAMSARA-2026] (vendor-published) |
| Controls after consolidation | 820 to 260 across 10 frameworks; 1,200 evidence items mapped | [VANTA-SAMSARA-2026] (vendor-published) |
| Expert interview time per audit | 70 to 40 hours (Samsara) | [VANTA-SAMSARA-2026] (vendor-published) |
| Evidence collection automated | 60% across 50-60 systems; five audit cycles in one month (Synthesia) | [VANTA-SYNTHESIA-2026] (vendor-published) |
| Manual compliance share of team time | 60% to 15% after platform consolidation (Perforce) | [VANTA-PERFORCE-2026] (vendor-published) |
| Control-to-evidence mapping precision | below 35% to 78%, offline test set | [VANTA-QUALITYEVAL-2026] (vendor-published) |
| Policy gap analysis vs experts | 80.65% agreement, best of 8 small models; 4 of 8 under 60% balanced accuracy | [ARXIV-2607.22885] (independent, lab) |
| Policy-to-code correctness | 50.3% structured pipeline vs 15.3% single prompt | [ARXIV-2609.24036] (independent, lab) |
| LLM risk scoring vs 50 experts | five models consistently lower | [ARXIV-2605.05424] (independent, lab) |
| LLM expert panel vs ground truth | r = 0.91-0.98 on proxies | [ARXIV-2602.08889] (independent, lab) |
| AI in cyber risk programmes | 80% use or test (37% / 43%); boardroom use of risk data 63% | [FAIR-CRMSURVEY-2026] (survey of 400, vendor-sponsored) |
| Security staff in AI policy | 56% involved; 51% help implement AI (29% in 2024) | [ISACA-SOC-2026] (survey, 1,800+) |
| AI-specific response exercises | 8% regularly, 64% none (see §6 on a conflicting reading) | [ISACA-SOC-2026] |
| Assess AI tool security | 64% (37% in 2025) | [WEF-GCO-2026] (survey) |
| Agents allowed to act unapproved | 22% fully; 38% partial | [PWC-GDTI-2027] (survey, 3,934) |
| Primary GRC tool | spreadsheets most cited (93 of 795); skill 5.4 of 10 | [GRCENGINEER-STATEOFGRC-2026] (independent, self-selected) |

What to measure with a client: share of AI answers and assessments sent unchanged; override and correction rate by
reviewer; sampled accuracy of AI answers against an assessor; vendor review cycle time and backlog; controls per
framework; evidence freshness and drift caught before audit; auditor findings on AI-prepared evidence; time from a
vendor trigger to reassessment.

## 6. Guardrails

- **Regulation at archetype level** (disclosure clocks, NIS2 and DORA accountability, EU AI Act, insurance, steps that
  need a person) is in `research/runs/wave4/security-x-guardrails-regulation.md`. Module-specific points follow.
- **EU AI Act.** Applicable from 2026-08-02; the AI Omnibus (in force 2026-07-27) moved Annex III high-risk duties to
  2027-12-02 [EC-AIACT-2026]. **NIS2** makes top management accountable for risk-management measures [EC-NIS2].
  **DORA** covers ICT third-party risk; the first critical ICT providers were designated on 2025-11-18 [EBA-CTPP-2025].
- **US.** Trade groups asked the SEC on 2026-04-10 to rescind or narrow Item 106 cyber disclosure; no final action
  was found [SIFMA-SEC-2026]. FINRA expects due diligence on vendors' GenAI use, contract terms on data, and logged
  prompts, outputs and model versions for GenAI supervision [FINRA-OVERSIGHT-2026].
- **Standards.** NIST's draft Cyber AI Profile lists compliance assessment, policy enforcement and executive risk
  communication as AI opportunities and says AI-generated reports need human review [NIST-CYBERAI-2025]. CSA's AI
  Controls Matrix adds an AI questionnaire (AI-CAIQ) for vendor assessment [CSA-AICM-2026]. Joint CISA, NSA and
  partner guidance (2026-05-01) asks for limited agent access, strong identity and monitoring [CISA-AGENTIC-BULLETIN-2026].
- **Attestations are not guarantees.** A SOC 2 Type II report covers specified controls over a limited period
  [IANS-DELVE-2026]; spot-check before relying on platform-produced evidence (`#16`).
- **A named reviewer for AI findings that trigger action** (CSA note, AI-assisted and not formally reviewed)
  [CSA-AGENTS-2026]; keep thresholds and policy decisions human and the rest deterministic [BLEEPING-ANECDOTES-2026].
- **Known failure modes.** Mapping precision started below 35% [VANTA-QUALITYEVAL-2026]; small models invented policy
  content and gave confidence scores that track the verdict, not certainty [ARXIV-2607.22885]; LLMs understated risk
  [ARXIV-2605.05424]; a single adversarial alert can steer a SOC LLM [ARXIV-2610.09906].
- **Data conflict to flag.** Two research angles read ISACA's 2026 release as 56% involved in AI policy and 8%
  running regular AI exercises (64% none); the cross-cutting regulation file read 60% and 71% none and could not find
  the 8% [ISACA-SOC-2026]. Check the release before quoting.
- **Human judgment stays on:** residual-risk and vendor approval decisions; approving control mappings and policy;
  what is told to customers, auditors, boards and regulators; risk appetite and acceptance; calibration of risk
  estimates; which agent actions need approval; disclosure and notification determinations.

## 7. Roles and how they evolve

- **GRC analysts:** from collecting evidence and answering forms to verifying agent drafts and tuning the tools
  (Anthropic supplier-assurance and risk-analyst postings) [ANTHROPIC-JOB-SUPPLIER-2026, ANTHROPIC-JOB-RISKANALYST-2026];
  "from collecting to managing" [BLEEPING-ANECDOTES-2026]. Plaid asks analysts to handle more reviews without adding
  headcount and to be "AI power users" [PLAID-JOB-TPRM-2026, PLAID-JOB-RISK-2026].
- **GRC engineers:** seven employers post builder roles in GRC (`#19`); a practitioner says most of the work is
  reading systems, learnable in months [GRCENGINEER-086-2026].
- **Risk analysts:** add system-card reading, agent privilege review and engineering literacy [FAIR-RISKREPORT-2026,
  FAIR-AGENTICCODING-2026]; Anthropic rebuilds risk "to operate as an engineering function" [ANTHROPIC-JOB-RISKANALYST-2026].
- **Customers' GRC teams:** verifiers of their compliance platform and auditor [IANS-DELVE-2026].
- **CISO:** Gartner predicts business acumen will differentiate high performers by 2028 [TECHTARGET-CISO-2026];
  Venables sees a "Chief Digital Risk Officer" form of the role (opinion) [VENABLES-CISO2-2026].
- **New roles:** 30% of organisations add AI governance analysts, 32% AI security engineers [RSAC-WORKFORCE-2026];
  Anthropic posts a GRC "security policy partner for AI agent governance" [ANTHROPIC-JOB-AGENTSEC-2026]. In eight EU
  countries AI builder postings outnumber governance postings about 7 to 1 (all functions) [VANTA-AIGOVGAP-2026].
- **Juniors:** Venables proposes control-failure post-mortems instead of evidence gathering (`#21`). Wider pipeline,
  skills and hiring data: `research/runs/wave4/security-x-workforce-talent.md`.
- Not measured anywhere: entry-level GRC hiring, analysts' override rates, headcount effects.

## 8. Frontier

- 2025-12-16: NIST preliminary draft Cyber AI Profile, with AI for compliance and executive risk communication
  [NIST-CYBERAI-2025].
- 2026-03-24: Delve allegations (denied) put verification of automated attestations at the centre [IANS-DELVE-2026].
- 2026-04-10: trade groups ask the SEC to rescind Item 106 [SIFMA-SEC-2026].
- 2026-04-12: CSA "Mythos-ready" briefing tells CISOs to update risk models and board reporting [CSA-MYTHOSREADY-2026].
- 2026-05-01: joint CISA, NSA and partner guidance on adopting agentic AI [CISA-AGENTIC-BULLETIN-2026].
- 2026-06: Vanta describes TPRM, compliance and risk "agents" [VANTA-TPRMAGENT-2026].
- 2026-06 to 10: Anthropic, OpenAI, Plaid, Cloudflare, Okta, GitLab and Figma post GRC roles that build or
  supervise agents (`#19`).
- 2026-06-22: CSA AI Controls Matrix v1.1 with AI-CAIQ [CSA-AICM-2026].
- 2026-07-21: Gartner's first Hype Cycle for AI Governance (via a secondary blog) [SOFTWARESTRATEGIES-GARTNERHC-2026].
- 2026-07-27: EU AI Omnibus in force; 2026-08-02 AI Act applicable [EC-AIACT-2026].
- 2026-08-25: Gartner names AI-enabled vulnerability discovery the top emerging risk, with third-party controls among
  its recommendations [GARTNER-EMERGING-2026].
- 2026-09-22: ISACA finds AI incident readiness lags AI use [ISACA-SOC-2026].
- 2026-10-01: PwC finds 22% would let agents act without approval and no single owner for AI governance [PWC-GDTI-2027].
- 2026-10-02 to 14: FAIR Institute series on assessing agents, coding agents and the AI attack surface
  [FAIR-AGENTICCODING-2026, FAIR-ATTACKSURFACE-2026].
- 2026-10-03: Venables' pyramid-to-diamond workforce argument [VENABLES-WORKFORCE-2026].
- 2026-10-12: CSA note on vendor-embedded agents and liability [CSA-AGENTS-2026].
- 2026-10-14: Optro (formerly AuditBoard) announces agentic compliance, autonomous testing and agentic TPRM [OPTRO-CRX-2026].

## 9. Common objections

- **"The AI will make things up in what we tell customers."** A real risk: Vanta treats hallucinated compliance
  detail as an audit risk [VANTA-QUALITYEVAL-2026]. Route uncertain answers to an analyst, use citations and
  confidence scores [WHISTIC-CALASTONE-2025], and measure accepted-unchanged rates (`#01`).
- **"The vendor numbers are marketing."** Partly right: every A/B figure here is vendor-published, several mix AI with
  portals or platform consolidation (`#02`, `#06`), and Samsara's "up to 50%" has no baseline. Ask for the baseline
  and pilot on your own questionnaires or vendors.
- **"Tools cast too wide a net."** Vanta's mapping precision started below 35% before tuning to 78%
  [VANTA-QUALITYEVAL-2026]; insist on an offline test set and expert review (`#05`).
- **"LLMs can't judge risk."** In one study five models consistently underestimated risk against experts
  [ARXIV-2605.05424]; the authors say use them alongside people, not alone. Keep calibration with analysts (`#11`, `#12`).
- **"Speed will cost us assurance."** The Delve allegations (denied) show the worry [IANS-DELVE-2026]; the Anecdotes
  author names a "verification tax" [BLEEPING-ANECDOTES-2026]. Build spot-checks and auditor independence in (`#16`).
- **"We should just block AI."** 78% block or limit employee GenAI [PROOFPOINT-VOC-2026], but Sendbird's CSO says
  blocking everything cannot be won [CLOUDSECPOD-SENDBIRD-2025] and Gartner warns more security can stall AI adoption
  [TECHTARGET-CISO-2026]. Cengage aimed to stop being "the Department of No" [BSIDESLV-2026].
- **"Our auditors won't accept it."** Unknown: no source documents auditor reliance. Ask them early (probe 3).
- **"Juniors will lose the work that taught them."** Venables agrees and proposes deliberate on-ramps (`#21`); only
  24% of organisations have well-defined career progression [RSAC-WORKFORCE-2026].

## 10. Sources

Full details are in the YAML. Keys cited here but not in the YAML:

- [EBA-CTPP-2025] European Banking Authority (for the ESAs), "The ESAs designate critical ICT third-party providers
  under the Digital Operational Resilience Act", press release, 2025-11-18.
  https://www.eba.europa.eu/publications-and-media/press-releases/european-supervisory-authorities-designate-critical-ict-third-party-providers-under-digital%5C

Most-used YAML keys: VANTA-SAMSARA-2026, VANTA-SYNTHESIA-2026, VANTA-GITHUB-2026, CONVEYOR-CARTA-2026,
VANTA-QUALITYEVAL-2026, ANTHROPIC-JOB-SUPPLIER-2026, ANTHROPIC-JOB-CONTROLS-2026, ARXIV-2607.22885, ARXIV-2605.05424,
FAIR-CRMSURVEY-2026, FAIR-RISKREPORT-2026, IANS-DELVE-2026, ISACA-SOC-2026, RSAC-WORKFORCE-2026, TECHTARGET-BOARD-2026,
TECHTARGET-AIREG-2026, NIST-CYBERAI-2025, FINRA-OVERSIGHT-2026, CSA-MYTHOSREADY-2026, PWC-GDTI-2027.

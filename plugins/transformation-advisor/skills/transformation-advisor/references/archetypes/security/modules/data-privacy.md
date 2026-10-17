# Data security and privacy (security)

Last reviewed 2026-10-17. Use cases live in `../use-cases/data-privacy.yaml` (21 entries). Ids are shortened here:
`#06` means `security-data-privacy-06`; other modules' ids are in full. Source keys in brackets are in the YAML or in
§10. **Evidence is thin.** This module had one combined deep dive. 8 of 21 entries are graded A or B; the two A
entries (Meta's rule-versus-LLM routing split, Microsoft's privacy code detection) are the deploying teams' own
figures, and neither publishes an error or miss rate. No independent override, false-positive or miss rate was found
for LLM-based DLP, alert triage or classification in production. Most other numbers are vendor telemetry that sizes
the problem, not the effect of a control. Several vendor customer stories (Cyera, MIND) carry no publication date;
the YAML gives the retrieval date (2026-10-17) and says so. Say all this when you quote a figure.

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

Finding, classifying and protecting sensitive data: data discovery and classification, data loss prevention (DLP:
tools that spot sensitive data leaving by email, endpoint, cloud or AI tool and warn or block), encryption and key
and certificate management, data access governance (who can see what, oversharing), and privacy engineering
(privacy impact assessments, lineage, retention, purpose limits, privacy review of code). It also covers data
exposure *through* AI tools: prompts and pastes, AI assistants reading overshared content, and agents passing
personal data to other services. Agent identities sit in ai-security; insider risk sits in human-risk.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Discover and inventory data | Scan cloud, SaaS, file shares and catalogs; for AI also prompts, retrieval sources, vector stores, tool links and logs [OWASP-DATASEC-2026] | data-reporting | About 1 in 10 companies had labelled files (vendor telemetry) [VARONIS-SODS-2025] |
| Classify and label | Assign sensitivity tags; stewards settle edge cases; labels should follow data into embeddings, caches and backups [OWASP-DATASEC-2026; ARXIV-GLYPH-2026] | transaction-processing, review-assurance | One catalog of about 3.4M columns would take about 30 person-years by hand (authors' estimate) [ARXIV-GLYPH-2026]; the same field name can be personal data or system metadata [META-ENG-ASSETCLASS-2026] |
| Prevent and detect data loss (DLP) | Write policies; triage and tune alerts; investigate | software-systems, transaction-processing, expert-judgment | Of respondents who lost data, 16% said DLP blocked their most significant incident [CSA-AI-2026]; OpenWeb could not trust legacy DLP alerts [MIND-OPENWEB-2026] |
| Govern access | Find overshared content, right-size permissions, control what AI assistants can retrieve [MSFT-SPRCD-2026; MSFT-PURVIEWAI-2026] | review-assurance | 99% of 1,000 environments held sensitive data AI can easily surface (vendor telemetry) [VARONIS-SODS-2025] |
| Encrypt and manage keys and certificates | Inventory, rotate and renew | software-systems | Certificate lifespans step down toward 47 days by 2029 [APPVIEWX-SUMMER-2026] |
| Privacy engineering | Privacy impact assessments (PIA/DPIA), data mapping and lineage, retention and deletion, purpose-limitation controls, privacy code review [PEPR-2026] | document-production, software-systems, review-assurance | "Assessment fatigue" from manual PIAs and reassessments [ONETRUST-W26-2026]; derived copies (embeddings, backups) can outlive a deleted record [OWASP-DATASEC-2026] |
| Control AI-specific exposure | Shadow-AI discovery, prompt and paste controls, retrieval access control, agent tool-call minimisation | review-assurance, software-systems | 29% could routinely produce a 30-day report of sensitive data sent to GenAI tools [CSA-AI-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome), reinvent (the service or operating model changes). **Coverage:** 2 assist, 11 augment, 8
automate; 12 step, 9 process. **No evidence was found for delegate or for model-level change**; do not suggest they
are happening. Agents that act (#11) still need approval for each action. Of the 8 automate entries, three are research ideas
(#16 to #18) and three rest on vendor documentation or telemetry with no named user (#08, #09, #12).

**Discovery and classification** (the best-evidenced area)
- Improve: `#01` LLM agents write column descriptions and suggest sensitivity tags; stewards accept or reject each one
  (steward acceptance 63.3% to 99.8% over six weeks; grade B because the deploying organization is not named).
  `#03` Gemini labels Drive files from admin-written instructions instead of trained models (open beta, C).
  `#04` natural-language search for sensitive data and bulk credential scanning (preview, C). `#05` AI-native
  data security posture platforms (DSPM: tools that find, classify and track risk on data) at ChenMed, Paramount
  and Vetcor (vendor-published counts, B).
- Automate: `#02` Meta answers about 85% of asset-classification requests with rules distilled from LLM findings;
  the LLM handles the other 15% (A, routing and cost only).

**Data loss prevention**
- Improve: `#06` agent sorts DLP alerts into "needs attention" and "less urgent" with a rationale (preview, C).
  `#07` context-aware AI classification replacing pattern-matching DLP at OpenWeb (CISO estimate, B).
- Automate: `#08` warn or block sensitive pastes and uploads into GenAI tools (C). `#18` idea: a plain-text policy
  file that an LLM uses to block risky prompts to coding agents (D). `#16` idea: LLM or hybrid PII detection
  (PII: personal data that identifies someone) to redact prompts and logs (D).

**Access governance and AI exposure**
- Improve: `#10` assess and reduce oversharing before AI assistant rollout (C). `#11` agents propose fixes (remove
  public links, revoke permissions) that an admin approves (C).
- Automate: `#09` discover shadow AI and block or steer to managed accounts (C; see also security-ai-security-21 and
  security-human-risk-16). `#12` enforce labels and entitlements when AI retrieves content, and carry labels onto
  embeddings (C). `#17` idea: middleware that strips agent tool calls to the minimum personal data (D).

**Encryption and key management**
- Improve: `#19` the only item found: an MCP server (a standard interface that lets AI agents call tools) exposing
  certificate inventory to agents (announced, C). No deployment or measurement exists.

**Privacy engineering**
- Improve: `#14` retrieval-augmented LLM flags privacy-relevant code patterns in pull requests at Microsoft (A; also
  see security-application-security-04). `#13` Meta's LLM-guided workflow that turns privacy requirements into
  data controls using lineage (B). `#15` AI first drafts of PIAs, reassessments and evidence reviews (C).
  `#20` Capital One found direct differentially private synthesis beat an LLM-based generator (B, negative result;
  differential privacy adds calibrated noise so no one person can be singled out).
- Automate: `#21` Google's "Provably Private Insights": LLMs interpret unstructured usage data inside attested secure
  hardware (trusted execution environments) and only differentially private totals leave (B, Recorder app).

## 4. Interview probes

1. **Which data stores feed your AI assistants, retrieval indexes or agents, and do labels and permissions follow
   the data into embeddings, caches and backups?** Reveals whether #12 is real or assumed, and whether erasure
   reaches derived copies [OWASP-DATASEC-2026].
2. **When did DLP last block a real incident before data left, and do you measure what it misses?** Separates alert
   counting from prevention; compare with the 16% CSA figure [CSA-AI-2026].
3. **Roughly how many DLP alerts a week, how many investigated, and who tunes the rules?** Sizes the case for #06
   or #07 and shows whether anyone owns false positives.
4. **Can you produce a 30-day report of sensitive data sent to GenAI tools, split by managed and personal
   accounts?** Only 29% of CSA respondents could [CSA-AI-2026]; a "no" points to #08 and #09 first.
5. **Who owns the shadow-AI decision: security, procurement or privacy?** Without an owner, block lists age and
   embedded AI features go unreviewed [OWASP-DATASEC-2026; NETSKOPE-CTR-2026].
6. **What share of your data is labelled, and who adjudicates labels a model proposes?** Low coverage blocks
   label-based DLP and retrieval controls; someone to adjudicate suggestions is a prerequisite for #01 to #03.
7. **Do you track missed sensitive data (false negatives) as well as acceptance of suggestions?** Acceptance alone
   cannot see misses [ARXIV-GLYPH-2026]; Meta tracks per-class recall [META-ENG-ASSETCLASS-2026].
8. **Before rolling out an AI assistant, did you review who can see what?** Reveals oversharing risk (#10) and
   whether temporary controls are standing in for permission clean-up [MSFT-SPRCD-2026].
9. **Where do PIAs, DPIAs and privacy code review spend their time, and which part could a first draft cover with a
   reviewer signing off?** Points to #15 or #14, and to the reviewer capacity they need.
10. **Do agents you run pass customer or employee data to outside tools or services?** Opens #17 and the
    ai-security module; research measured unnecessary sensitive data in 81-88% of tool calls under default prompts [ARXIV-TOOLMINIMIZE-2026].
11. **Do you have a current inventory of keys and certificates, and who renews them?** Reveals readiness for shorter
    certificate lifespans; AI evidence here is a single vendor announcement (#19).

## 5. Metrics and benchmarks

What to measure: prevention (incidents blocked before data left), DLP false-positive and miss rates, alert
investigation rate, label coverage, steward acceptance *and* missed classifications, share of AI traffic visible
and on managed accounts, time to remediate exposures, and assessment cycle time.

| Measure | Figure and what it counts | Source | Provenance |
|---|---|---|---|
| DLP prevention | 16% of respondents who lost data said DLP blocked their most significant incident (433 surveyed) | CSA-AI-2026 | independent survey |
| GenAI visibility | 29% can routinely produce a 30-day report of sensitive data sent to GenAI tools | CSA-AI-2026 | independent survey |
| Data controls in place | Only three of seven key data risk measures implemented; data classification 49%, DLP on key egress channels 48% (3,934 leaders) | PWC-GDTI-2027 | survey |
| AI-caused data loss | Misuse or misconfiguration of AI tools caused 37% of material data loss cases | PROOFPOINT-VOC-2026 | vendor survey |
| Shadow-AI breaches | Shadow-AI incidents exposed personal data in 65% (global average 53%) and IP in 40% (33%); population is breached organizations | IBM-CODB-2025 | vendor survey |
| Unapproved-tool sharing | Of employees using unapproved tools, 54% share internal messages and emails, 45% HR information, 39% confidential documents | OKTA-AIAGENTS-2026 | vendor survey |
| GenAI policy violations | Average organization: 3% of genAI users commit about 223 violations a month; 50% of organizations lack enforceable genAI data policies | NETSKOPE-CTR-2026 | vendor telemetry |
| Sensitive data in AI use | 39.7% of data movements into AI tools involve sensitive data; 32.3% of ChatGPT use via personal accounts | CYBERHAVEN-AIRISK-2026 | vendor telemetry |
| Exposure to AI | 99% of 1,000 environments had sensitive data AI can easily surface | VARONIS-SODS-2025 | vendor telemetry |
| Steward acceptance | 63.3% to 99.8% over six weeks, about 24,000 decisions; blind to false negatives | ARXIV-GLYPH-2026 | self-reported |
| Tagging quality | F2 0.890 fused (F2 weights recall twice as much as precision); regex alone 0.050; 4 evaluation files | ARXIV-GLYPH-2026 | self-reported |
| Rules versus LLM | About 85% of requests by rules, 15% by LLM at roughly 400x the compute | META-ENG-ASSETCLASS-2026 | self-reported |
| Privacy code detection | Retrieval found more than 2x the confirmed issues of a standalone LLM; false positives not significantly improved | PEPR-2026 | self-reported |
| DLP noise (case study) | About 16,000 false-positive events cut to "just a handful" (unnamed institution) | CYERA-FI-2026 | vendor-published |
| PII detector limits | Rule-based recall 0.07 on the most sensitive categories; no detector reached full cross-turn coverage without false positives | ARXIV-REDACT-2026; ARXIV-PIITRACE-2026 | independent (academic) |
| Agent over-sharing | 81-88% of tool calls held unnecessary sensitive data; 36-76% even with privacy instructions | ARXIV-TOOLMINIMIZE-2026 | independent (academic) |
| Breach cost | Global average US$4.99M; US$1.93M lower with extensive security AI and automation (landing page only) | IBM-CODB-2026 | vendor survey |

Benchmarks for override rate or accuracy of DLP triage agents in production: **none published.**

## 6. Guardrails

- **GDPR and AI models.** The EDPB says a model trained on personal data is not automatically anonymous; anonymity is
  assessed case by case. It also sets out a three-step legitimate-interest test for developing and deploying AI
  models [EDPB-OPINION2824-2024].
- **EU law in flux.** The Digital Omnibus proposal (19 November 2025) would add a legitimate-interest basis for AI
  training (Article 88c); a law-firm analysis says a Council compromise of 10 June 2026 would drop it in favour of a
  recital. The outcome is not confirmed [NOERR-OMNIBUS-2026]. The EU AI Act has applied since 2026-08-02, with
  Annex III high-risk obligations moved to 2027-12-02 [EC-AIACT-2026].
- **NIST.** AI 600-1 lists data privacy as a generative AI risk, including memorisation, leakage and inference
  [NIST-AI600-2024]. Privacy Framework 1.1 was still a draft on a page updated 2026-04-01 [NIST-PF-2026].
- **OWASP.** The GenAI data security guide (v1.0, March 2026) lists 21 data risks with tiered mitigations. It says
  context windows have no internal access control and its mitigations work around that limit [OWASP-DATASEC-2026].
- **US state oversight.** A law-firm recap of the 2026 IAPP summit reports California regulators moving toward
  audit-style oversight [PERKINSCOIE-IAPPGPS-2026].
- **Product limits to check.** The Purview DLP triage agent skips simulation-mode policies, files above 2 MB and
  non-content conditions; Microsoft says to triage those by hand [MSFT-PURVIEWAGENTS-2026]. SharePoint Restricted
  Content Discovery does not change permissions and is described as temporary [MSFT-SPRCD-2026].
- **Keep evaluation independent.** Meta found that optimising against the model's own earlier labels looked better
  but drifted from policy; it keeps a frozen human-reviewed reference set [META-ENG-ASSETCLASS-2026].
- **Steps that need human judgment:** adjudicating tags and reference labels (#01, #02); approving rule promotions
  that could reduce protection (#02); warn-versus-block policy decisions (#08); approving each remediation action
  (#11); interpreting privacy requirements (#13); validating AI-completed assessment fields (#15); evaluating
  synthetic-data fidelity before use (#20).

## 7. Roles and how they evolve

- **Data stewards** move from writing tags to adjudicating model suggestions, which then retrain the model
  [ARXIV-GLYPH-2026]. At Meta, people focus on ambiguous policy, reference labels, high-risk disagreements and rule
  promotion [META-ENG-ASSETCLASS-2026].
- **Data security admins** write natural-language classification instructions instead of curating training files
  [GOOGLE-WSAICLASS-2026], and approve or tune agent-proposed fixes [MSFT-DSPM-2026].
- **DLP analysts** work a ranked queue with explanations and tune it with feedback
  [MSFT-PURVIEWDLPTRIAGE-2026]; OpenWeb's CISO says the team now trusts alerts enough to use them for decisions and automation
  [MIND-OPENWEB-2026].
- **Privacy engineers** are a growing dedicated role: Anthropic describes one of its first dedicated privacy engineers
  building automated discovery, classification, lineage and compliance controls [ANTHROPIC-JOB-PRIVACYENG-2026].
  Coinbase's privacy incident analyst posting asks for automation and responsible GenAI use with human oversight
  [COINBASE-JOB-PRIVACYANALYST-2026]. Datadog hires a product manager for AI and data security
  [DATADOG-JOB-AIDATASEC-2026].
- **Privacy experts**: in the Privy research, non-experts prepare first drafts while experts take product-specific,
  high-impact decisions [PEPR-2026].
- Vendors claim smaller teams can run discovery and clean-up at scale [CYERA-VETCOR-2026]; no staffing data is
  published.

## 8. Frontier

| Date | Signal | Source |
|---|---|---|
| 2025-11-17 | Gartner abstract (search-only, paywalled) says conventional DLP cannot manage GenAI data loss risks | GARTNER-DLP-2025 |
| 2026-01-28 | MIND announces DLP for agentic AI (agent discovery, risky-access detection, remediation) | MIND-AGENTICDLP-2026 |
| 2026-03-17 | OWASP publishes its GenAI data security risks and mitigations guide v1.0 | OWASP-DATASEC-2026 |
| 2026-04-29 | Black Hat Asia privacy keynote asks which privacy tools are "privacy theater" | BLACKHAT-ASIAPR-2026 |
| 2026-06-01 | PEPR 2026: LLM-for-privacy-engineering talks from Meta, Microsoft, Google, Capital One, CMU and others, open about limits | PEPR-2026 |
| 2026-06-10 | Cyera announces a US$600 million Series G at a US$12 billion valuation | CYERA-SERIESG-2026 |
| 2026-06-25 | Meta describes shrinking the LLM's role by distilling its findings into rules | META-ENG-ASSETCLASS-2026 |
| 2026-07-02 | Akamai completes its LayerX purchase (browser security and AI usage control, about US$205 million) | AKAMAI-LAYERX-2026 |
| 2026-08-17 | Microsoft moves general availability of DLP triage summaries in Defender XDR from August 2026 to August 2027 | MSFT-MC1255406-2026 |
| 2026-08-28 | Google opens instruction-driven Gemini classification for Drive in beta | GOOGLE-WSAICLASS-2026 |
| 2026-09-25 | OpenAI discloses research agents sent training and evaluation data to third-party services, including 53 user images posted as unlisted links (see security-ai-security-17) | OPENAI-HFUPDATES-2026 |
| 2026-10-07 | Wiz describes an agent that finds exposed data on public pages and redacts raw values before alerting (see security-vulnerability-exposure-21) | WIZ-REDAGENT-2026 |
| 2026-10-09 | CSA publishes its DLP-in-the-AI-era survey | CSA-AI-2026 |
| 2026-10-15 | Proofpoint agrees to buy Varonis for about US$6.3 billion; close expected first half of 2027 | VARONIS-PROOFPOINT-2026 |

Direction: the market is consolidating around data plus AI security (the deals above). Research prototypes target
what agents send to tools and coding agents (#17, #18); no deployment was found. Practitioner discourse is very thin: 100 recent Risky Business episode titles
had none on DLP or privacy engineering [RISKYBIZ-2026].

## 9. Common objections

- **"LLM output isn't reproducible, so we can't enforce on it."** Agreed, and Meta's design reflects that: rules
  enforce, the LLM is a fallback and a source of candidate rules, and rules go through holdout and shadow testing
  [META-ENG-ASSETCLASS-2026] (#02).
- **"AI DLP vendors all claim near-zero false positives."** The case-study claims are vendor-published, often from
  CISO estimates or unnamed customers, and none gives a miss rate [MIND-OPENWEB-2026; CYERA-FI-2026]. Ask for false
  positives *and* misses, measured on your data.
- **"High acceptance means the tags are right."** Acceptance only counts tags the system emitted; it cannot see
  missed sensitive columns [ARXIV-GLYPH-2026]. Plain accuracy also hides rare-class failure
  [META-ENG-ASSETCLASS-2026].
- **"We'll just block ChatGPT."** 90% of Netskope customers block at least one genAI app, but tracked apps grew from
  317 to more than 1,600 in a year [NETSKOPE-CTR-2026], and blocking does not reach AI embedded in procured software
  [OWASP-DATASEC-2026]. Pair blocks with sanctioned alternatives (#09).
- **"Copilot respects permissions, so we're safe."** It returns what users can already reach. Microsoft says generative AI amplifies
  oversharing [MSFT-PURVIEWAI-2026]; Varonis found sensitive data AI can easily surface in 99% of 1,000 environments
  [VARONIS-SODS-2025]. Restricting discovery is temporary and leaves access unchanged
  [MSFT-SPRCD-2026] (#10).
- **"AI can write our DPIAs."** Vendor tools flag AI-completed fields for review [ONETRUST-W26-2026]; one study found
  stricter formats gave consistent output but more hallucinations [ARXIV-DPIALLM-2026]. Treat output as a first draft.
- **"Retrieval will fix the false positives."** At Microsoft it found more than twice the issues but did not
  significantly cut false positives [PEPR-2026] (#14).
- **"LLM-generated synthetic data solves sharing."** Capital One found model bias, not privacy noise, was the main
  error, and direct differentially private synthesis did better [PEPR-2026] (#20).
- **"Policy is enough."** In three German organizations, regulatory pressure became policy without regard to actual
  tool use [ARXIV-GENAIAGILE-2026]; one practitioner says policy-only rules do not work [HN-ASKLLMAPI-2026].

## 10. Sources

Full details (title, URL, date, access, locator) for these keys are in the YAML: ARXIV-GLYPH-2026,
META-ENG-ASSETCLASS-2026, GOOGLE-WSAICLASS-2026, GOOGLE-WSAISEC-2024, MSFT-PURVIEWAGENTS-2026,
MSFT-PURVIEWDLPTRIAGE-2026, MSFT-MC1255406-2026, MSFT-PURVIEWAI-2026, MSFT-DSPM-2026, MSFT-SPRCD-2026,
CYERA-CHENMED-2026, CYERA-PARAMOUNT-2026, CYERA-VETCOR-2026, CYERA-FI-2026, CYERA-SERIESG-2026, MIND-OPENWEB-2026,
VARONIS-SODS-2025, CSA-AI-2026, NETSKOPE-CTR-2026, CYBERHAVEN-AIRISK-2026, HN-ASKLLMAPI-2026, OWASP-DATASEC-2026,
AKAMAI-LAYERX-2026, ARXIV-ARBITER-2025, PEPR-2026, ONETRUST-W26-2026, ARXIV-PIABENCH-2026, ARXIV-DPIALLM-2026,
ARXIV-REDACT-2026, ARXIV-PIITRACE-2026, ARXIV-MINDGAP-2026, ARXIV-SURROGATESHIELD-2026, ARXIV-TOOLMINIMIZE-2026,
ARXIV-POLICYGUARD-2026, APPVIEWX-SUMMER-2026. Cyera and MIND customer stories are undated (retrieval date given).

Cited here only (all opened in full unless marked):
- ANTHROPIC-JOB-PRIVACYENG-2026: Staff+ Software Engineer, Privacy (job posting), Anthropic, 2026-08-07, https://job-boards.greenhouse.io/anthropic/jobs/5383114008
- ARXIV-GENAIAGILE-2026: Between Policy and Practice: GenAI Adoption in Agile Software Development Teams, arXiv, 2026-01-11, https://arxiv.org/abs/2601.07051
- BLACKHAT-ASIAPR-2026: Black Hat Asia 2026 post-event press release, Black Hat (Informa), 2026-04-29, https://blackhat.com/html/press/2026-04-29.html
- COINBASE-JOB-PRIVACYANALYST-2026: Analyst, Privacy (Incident Management) (job posting), Coinbase, 2026-09-01, https://www.coinbase.com/careers/positions/8168175?gh_jid=8168175
- DATADOG-JOB-AIDATASEC-2026: Product Manager II, AI & Data Security (job posting), Datadog, 2026-06-04, https://careers.datadoghq.com/detail/7982288/?gh_jid=7982288
- EC-AIACT-2026: AI Act regulatory framework status page (undated; checked 2026-10-17), European Commission, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EDPB-OPINION2824-2024: Opinion 28/2024 on data protection aspects of AI models, EDPB, 2024-12-17, https://www.edpb.europa.eu/system/files/documents/2024-12/edpb_opinion_202428_ai-models_en.pdf
- GARTNER-DLP-2025: Gartner Insights abstract, document 7192130, Gartner, 2025-11-17, https://www.gartner.com/en/documents/7192130 (search-only)
- IBM-CODB-2025: IBM Report, 13% of organizations reported breaches of AI models or applications (Cost of a Data Breach 2025), IBM, 2025-07-30, https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls
- IBM-CODB-2026: Cost of a Data Breach Report 2026 (landing page only), IBM / Ponemon, 2026-09-16, https://www.ibm.com/reports/data-breach
- MIND-AGENTICDLP-2026: MIND Announces Autonomous DLP for Agentic AI, MIND, 2026-01-28, https://mind.io/newsroom/mind-announces-autonomous-dlp-for-agentic-ai
- NIST-AI600-2024: NIST AI 600-1, Generative AI Profile, NIST, 2024-07, https://doi.org/10.6028/NIST.AI.600-1
- NIST-PF-2026: NIST Privacy Framework 1.1 page, NIST, 2026-04-01, https://www.nist.gov/privacy-framework/privacy-framework-version-11
- NOERR-OMNIBUS-2026: Digital Omnibus AI is nearing the finish line, Noerr, 2026-06-18, https://www.noerr.com/en/insights/digital-omnibus-ai-is-nearing-the-finish-line-is-eu-data-law-heading-down-the-wrong-track
- OKTA-AIAGENTS-2026: AI Agents at Work 2026 (survey of 292 executives and 492 knowledge workers), Okta, 2026-05, https://www.okta.com/newsroom/articles/ai-agents-at-work-2026-agentic-enterprise-security/
- OPENAI-HFUPDATES-2026: The Hugging Face incident and other third-party impact from misaligned models (running updates), OpenAI, 2026-09-30, https://openai.com/hugging-face-incident-and-misalignment/
- PERKINSCOIE-IAPPGPS-2026: Key Takeaways From the 2026 IAPP Global Privacy Summit, Perkins Coie, 2026-04-17, https://www.ashurstperkinscoie.com/en/insights/where-privacy-is-headed-next-key-takeaways-from-the-2026-iapp-global-privacy-summit/
- PROOFPOINT-VOC-2026: The risk has moved: Proofpoint's 2026 Voice of the CISO, Proofpoint, 2026-09-09, https://www.proofpoint.com/au/blog/corporate-news/risk-has-moved-what-proofpoints-2026-voice-ciso-reveals
- PWC-GDTI-2027: 2027 Global Digital Trust Insights (survey of 3,934 leaders), PwC, 2026-10-01, https://www.pwc.com/gx/en/issues/cybersecurity/global-digital-trust-insights.html
- RISKYBIZ-2026: Risky Business podcast feed (100 episode titles scanned), 2026-10-14, https://risky.biz/feeds/risky-business/
- VARONIS-PROOFPOINT-2026: Proofpoint to Acquire Varonis in a $6.3 Billion Transaction, Varonis / Proofpoint, 2026-10-15, https://www.varonis.com/announcement
- WIZ-REDAGENT-2026: How the Wiz Red Agent caught a Fortune 500 firm's data exposure, Wiz, 2026-10-07, https://www.wiz.io/blog/red-agent-financial-services-data-exposure

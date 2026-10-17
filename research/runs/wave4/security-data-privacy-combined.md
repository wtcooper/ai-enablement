# Data security and privacy: combined deep dive (practice, discourse, governance and evidence)

Archetype: security. Module: data-privacy. Angle: combined. Compiled 2026-10-17.

## 1. Summary

Module: data-privacy (data discovery and classification, DLP, encryption and key management, data access governance, privacy engineering, plus AI for these and data exposure through AI tools). Angle: combined (practice, discourse, governance and evidence). Compiled 2026-10-17. Working files were kept in a private `mktemp -d` folder. Web search was used 13 times, for items that could not be reached directly (Black Hat Asia coverage, Cyera finance, PEPR, Purview agent results, Digital Omnibus status, DLP case studies, podcasts, cryptographic inventory, OneTrust, Cyberhaven, IAPP, Gartner, Copilot oversharing). Everything else was opened with `curl`, the Microsoft Learn search API, the `r.jina.ai` mirror, arXiv abstract pages and the public Greenhouse job-board API.

Use cases by grade: A = 3, B = 5, C = 10, D = 3 (21 total; 8 of 21 graded A or B, which is below the usual 50% target because public evidence is thin). Sources: 53 distinct references (by type: vendor 22, academic 11, firm 4, job-posting 4, standard-setter 3, conference 2, regulator 2, survey 2, community 1, podcast 1, press 1); one is search-only.

- **The best-evidenced change is in classification, not in DLP.** Two engineering accounts describe production LLM classification with humans adjudicating: Apple-affiliated authors report steward acceptance of tag suggestions rising from 63.3% to 99.8% over six weeks (about 24,000 decisions), and Meta reports that about 85% of asset-classification requests are answered by deterministic rules distilled from LLM findings, with the LLM kept as a fallback for about 15% (ARXIV-GLYPH-2026; META-ENG-ASSETCLASS-2026). Neither publishes a miss rate.
- **DLP evidence is mostly vendor case studies and survey baselines.** The only independent number is a CSA survey of 433 practitioners: of respondents who lost data, 16% said DLP blocked their most significant incident, and 29% could routinely produce a 30-day report of sensitive data sent to GenAI tools (CSA-AI-2026). No independent override, false-positive or miss rate for LLM-based DLP or alert triage in production was found.
- **Data exposure through AI tools is measured by vendor telemetry.** Netskope, Cyberhaven and Varonis each report large exposure baselines (for example 39.7% of data movements into AI tools involve sensitive data; 99% of 1,000 environments hold sensitive data that AI can surface), but these describe the problem, not the effect of a control (CYBERHAVEN-AIRISK-2026; VARONIS-SODS-2025).
- **Privacy engineering is where practitioners are most open about limits.** At PEPR 2026, Microsoft reported that retrieval-augmented detection of privacy-relevant code patterns found more than twice as many confirmed issues as a standalone LLM but did not reduce false positives, and Capital One reported that direct differentially private synthesis beat an LLM-based generator (PEPR-2026).
- **The market is consolidating around data plus AI security.** Proofpoint agreed to buy Varonis for about US$6.3 billion (announced 2026-10-15, closing expected in the first half of 2027); Akamai completed its US$205 million LayerX purchase on 2026-07-02; Cyera announced a US$600 million Series G on 2026-06-10 (VARONIS-PROOFPOINT-2026; AKAMAI-LAYERX-2026; CYERA-SERIESG-2026).
- **Encryption and key management has almost no public AI-for-defender evidence.** One vendor announced an MCP server that exposes certificate inventory to agents (APPVIEWX-SUMMER-2026). Public discourse (podcast titles, community threads) on this module is very thin.

## 2. Use cases

```yaml
- id: security-data-privacy-01
  title: LLM agents describe and sensitivity-tag data-catalog columns, with data stewards adjudicating each suggestion
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - data-reporting
  - review-assurance
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Data lakes gain tables faster than stewards can document or classify them, so columns lack descriptions and governance labels. The paper says sensitive-data tagging lags discovery by months and that PII is often found only after an incident (ARXIV-GLYPH-2026, Section 1).
  solution: Glyph is described as a production system built from cooperating LLM agents. A Descriptor writes column descriptions grounded in the pipeline source code that produces each column. A Tagger assigns labels from a governed 275-leaf Data Classification Ontology by running three strategies in parallel (description-based, line-of-business regex, and a fine-tuned metadata encoder over a vector database) and fusing the ranked results. It never reads cell values. Stewards accept or reject each suggested column-tag pair, and those decisions are written back and used to re-fine-tune the encoder weekly (ARXIV-GLYPH-2026, Abstract; Sections 1, 4, 5.2).
  outcomes:
  - lever: quality
    description: Share of Glyph tag suggestions that stewards accepted, tracked weekly in production
    figure: 63.3% rising to 99.8% over six consecutive weeks
    measures: Weekly steward acceptance of suggested column-tag pairs, about 24,000 adjudicated pairs in total; decision volume grew 21x over the window. The authors call the trend an association, not a causal effect, and note that acceptance only counts tags the system emitted, so it is blind to false negatives.
    provenance: self-reported
    source_ref: ARXIV-GLYPH-2026
  - lever: quality
    description: End-to-end tagging quality of the full fusion configuration against steward-curated expectations
    figure: Overall F2 0.890 (metadata tagger alone 0.880; regex tagger alone 0.050)
    measures: Micro-averaged F2 (recall weighted twice as heavily as precision) over 4 evaluation files drawn from 1,905 tables that are disjoint from the 15,205-table training index; fusion uses Claude Sonnet 4.5; p50 request latency 57.8 s.
    provenance: self-reported
    source_ref: ARXIV-GLYPH-2026
  - lever: capacity
    description: Scale the authors say makes manual tagging infeasible
    figure: About 30 person-years of effort for one catalog of about 3.4M columns across about 98,000 tables
    measures: The authors' own estimate, at an assumed (and optimistic) rate of one column per minute; it is a motivation figure, not a measured saving.
    provenance: self-reported
    source_ref: ARXIV-GLYPH-2026
  prerequisites:
  - A governed sensitivity ontology (275 leaf tags in the paper) maintained by data stewards
  - Pipeline source code reachable from an enterprise code repository so descriptions can be grounded
  - An existing corpus of steward-tagged columns to fine-tune the metadata encoder
  - Steward-curated, line-of-business evaluation sets that are disjoint from the training corpus
  risks_and_guardrails:
  - The design never reads column values, so it can run on restricted-access tables (ARXIV-GLYPH-2026, Section 1 and Discussion)
  - The authors chose a recall-weighted F2 because a missed sensitive column silently defeats access control, while an over-applied tag is cheap for a steward to dismiss (ARXIV-GLYPH-2026, Section 5)
  - 'No single strategy was sufficient: the regex tagger alone scored near zero and the description tagger alone scored 0.238 F2 (ARXIV-GLYPH-2026, Table 3)'
  - The fused configuration is slow, with a p50 of 57.8 s per request (ARXIV-GLYPH-2026, Table 3 discussion)
  human_checkpoints:
  - A data steward adjudicates every suggested column-tag pair before it takes effect (ARXIV-GLYPH-2026, Section 5.2)
  - Accepted and rejected pairs feed a weekly re-training loop (ARXIV-GLYPH-2026, Section 5.2)
  role_evolution: Stewards review and correct model suggestions instead of writing every description and tag by hand; their decisions become training data (ARXIV-GLYPH-2026, Section 5.2). The paper does not report headcount effects.
  evidence_grade: A
  sources:
  - ref: ARXIV-GLYPH-2026
    title: 'Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology Tagging of Enterprise Data Catalogs (Kudriavtsev, Rafi, Sundaram; Apple affiliation)'
    publisher: arXiv preprint
    type: academic
    url: https://arxiv.org/abs/2609.10430
    date: '2026-09-09'
    access: full
    locator: Abstract; Section 1 (scale and cost); Table 3 (F2 by configuration); Section 5.2 and Figure 2 (steward acceptance)
  last_reviewed: '2026-10-17'
  notes: The authors are affiliated with Apple, but the paper describes 'a single organization's production catalog' without naming the deploying organization, so the deployer is not independently confirmed. Acceptance and F2 are both measured by the deploying team (self-reported); no outside measurement exists. The F2 evaluation uses only 4 evaluation files.
- id: security-data-privacy-02
  title: Deterministic-first asset classification with an LLM fallback, where stable LLM findings are distilled into versioned rules
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - data-reporting
  - software-systems
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Privacy controls (retention, access, purpose limits, sharing, anonymization) need a reliable view of what each data asset is, and manual review cannot keep up with the volume and pace of AI-native products. The same field name can be personal data in one context and system metadata in another (META-ENG-ASSETCLASS-2026, 'Why Asset Classification Matters').
  solution: 'Meta describes a hybrid classifier. It assembles an evidence brief per asset (code resolution, lineage, ownership, semantic annotations, scanner outputs), masks any pre-existing privacy label to avoid circular reasoning, and routes the asset through a funnel: versioned deterministic rules first, an LLM only for novel or ambiguous assets. A nightly lane samples served decisions, scores them against human-reviewed reference labels using a three-judge LLM panel, and proposes rules distilled from stable patterns. Rules go through holdout validation and shadow mode before promotion (META-ENG-ASSETCLASS-2026, decision-funnel and rule-distillation sections).'
  outcomes:
  - lever: cost
    description: Share of classification requests answered by cheap deterministic rules rather than the LLM fallback, in Meta's production deployment
    figure: About 85% by rules in single-digit milliseconds (about 40 ms including context assembly); about 15% LLM fallback taking seconds at roughly 400 times the compute cost
    measures: Share of classification requests resolved on the deterministic path versus the LLM path, as read from Figure 4 and Figure 7 captions; this is a routing and cost measure, not an accuracy or error-rate measure.
    provenance: self-reported
    source_ref: META-ENG-ASSETCLASS-2026
  prerequisites:
  - Code search and resolution, lineage, ownership metadata and semantic annotations that can be assembled per asset
  - A human-reviewed, append-only reference label set kept separate from model output
  - A rule engine with versioned, replayable decisions and shadow-mode promotion
  - A scoped taxonomy per classifier (one question per classifier)
  risks_and_guardrails:
  - Fields masked from the LLM are also blocked from rule distillation so a masked signal cannot re-enter through a learned rule; Meta reports a masking-handling bug that silently pushed requests to the LLM fallback until fixed (META-ENG-ASSETCLASS-2026, rule-routing section)
  - The LLM confidence score is a self-assessment and is checked for calibration against reviewed labels before it is used for routing (META-ENG-ASSETCLASS-2026)
  - 'Evaluation is kept independent of optimisation: frozen human-reviewed reference set, different judge and classifier models, regression gates. An optimisation run scored against the model''s own earlier labels appeared to improve but drifted from policy (META-ENG-ASSETCLASS-2026, ''What We Learned'')'
  - Plain accuracy hides rare-class failure; Meta tracks per-class recall, macro F1 and Matthews correlation (META-ENG-ASSETCLASS-2026)
  human_checkpoints:
  - People adjudicate the reference labels and approve rule promotions that could change enforcement (META-ENG-ASSETCLASS-2026)
  - Escalation to human review on low calibrated confidence, judge-panel disagreement, a rare sensitive class, fragile reasoning, or a protection-reducing rule (META-ENG-ASSETCLASS-2026, 'Automate the Right Things')
  role_evolution: Automation covers context acquisition, evidence briefs, candidate classification, evaluation runs, failure analysis and candidate rule proposals. People concentrate on ambiguous policy interpretation, reference labels, high-risk disagreements and rule-promotion decisions (META-ENG-ASSETCLASS-2026, 'Automate the Right Things').
  evidence_grade: A
  sources:
  - ref: META-ENG-ASSETCLASS-2026
    title: 'Privacy-Aware Infrastructure in the AI-Native Era: An Asset Classification Case Study'
    publisher: Engineering at Meta (Meta Platforms)
    type: firm
    url: https://engineering.fb.com/2026/06/25/security/privacy-aware-infrastructure-in-the-ai-native-era-an-asset-classification-case-study/
    date: '2026-06-25'
    access: full
    locator: Decision-funnel section and Figure 4/7 captions (85% / 15% / 400x); 'Automate the Right Things'; 'What We Learned'
  last_reviewed: '2026-10-17'
  notes: Graded A because a measured outcome from a named organization is published, but that outcome is a routing and cost split. The post publishes no accuracy, error-rate, override-rate or classifier-versus-human agreement figure, so quality evidence is absent. The post is the deploying team's own account (self-reported).
- id: security-data-privacy-03
  title: Instruction-driven Gemini labelling of Drive files, replacing admin-trained classification models
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - data-reporting
  - transaction-processing
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: Label-based DLP and retention policies only work on files that are correctly labelled, and labelling put a considerable manual burden on admins (GOOGLE-WSAISEC-2024). The earlier AI classification required admins to find and hand-label training files so the model could learn each classification level (GOOGLE-WSAICLASS-2026).
  solution: Google announced in open beta (2026-08-28) that Gemini models apply classification labels to Drive files from administrator-written instructions, with no manual model training. Admins choose the label, write the instructions and scope the audience. Owners and editors with label permission can accept or modify a Gemini-applied label, audit logs capture labelling and user decisions, and the admin console shows metrics on Gemini-applied labels (GOOGLE-WSAICLASS-2026).
  outcomes:
  - lever: quality
    description: Google states the capability helps admins reach higher classification accuracy at scale
    figure: none published
    measures: No accuracy, coverage or time figure is given in the announcement.
    provenance: vendor-published
    source_ref: GOOGLE-WSAICLASS-2026
  prerequisites:
  - Supported Workspace licence (Enterprise Plus, Google AI Pro for Education, or Frontline Plus per the announcement)
  - Admin console data classification set up with labels (Security > Access and data control > Data classification)
  - Administrator-written classification instructions and a defined file audience
  risks_and_guardrails:
  - Administrators keep control over the labels, instructions and scope (GOOGLE-WSAICLASS-2026)
  - Audit logs record when files are labelled, including user acceptance or modification (GOOGLE-WSAICLASS-2026)
  - Google presents labels as a way to stop agentic workflows from acting on sensitive data without authorisation; no evidence of that effect is published (GOOGLE-WSAICLASS-2026)
  human_checkpoints:
  - File owners and editors with label permission can review and accept or modify each Gemini-applied label (GOOGLE-WSAICLASS-2026)
  role_evolution: Admins write and tune natural-language instructions instead of curating labelled training files; file owners review labels on their own files (GOOGLE-WSAICLASS-2026).
  evidence_grade: C
  sources:
  - ref: GOOGLE-WSAICLASS-2026
    title: Gemini-based data classification in Google Drive is now available in open beta
    publisher: Google Workspace Updates blog
    type: vendor
    url: https://workspaceupdates.googleblog.com/2026/08/gemini-based-data-classification-in-Google-Drive-is-now-available-in-open-beta.html
    date: '2026-08-28'
    access: full
    locator: Whole announcement; 'Rollout pace' and 'Availability'
  - ref: GOOGLE-WSAISEC-2024
    title: Introducing a new AI Security add-on for Google Workspace
    publisher: Google Workspace Updates blog
    type: vendor
    url: https://workspaceupdates.googleblog.com/2024/04/ai-security-add-on-google-workspace.html
    date: '2024-04-09'
    access: full
    locator: '''What''s changing'' and ''Why it matters'''
  last_reviewed: '2026-10-17'
  notes: Vendor announcement of an open beta, with rollout targeted to complete by 30 September (year not stated in the post; the post is dated 2026-08-28). No customer or measurement is named.
- id: security-data-privacy-04
  title: Natural-language search for sensitive data and bulk credential scanning with an LLM posture agent (preview)
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - research-synthesis
  - review-assurance
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: Searching for relevant data and finding out how it is protected is, in Microsoft's words, time-consuming, tedious and highly manual; keyword and filter search misses intent (MSFT-PURVIEWAGENTS-2026, 'Data Security Posture Agent').
  solution: The Data Security Posture Agent in Microsoft Purview uses LLMs to interpret a plain-language request, searches scoped Microsoft 365 content (documents, emails, messages and Copilot interactions) and returns results with a summary and an LLM-generated risk analysis. In Data Security Investigations a second posture agent (preview) scans Microsoft 365 locations for exposed credentials at scale, writes AI risk assessments and tracks remediation tasks on a Kanban-style board (MSFT-PURVIEWAGENTS-2026).
  outcomes:
  - lever: speed
    description: Microsoft says the agent returns search results quickly and spares users manual search
    figure: none published
    measures: No time, accuracy or adoption figure is given.
    provenance: vendor-published
    source_ref: MSFT-PURVIEWAGENTS-2026
  prerequisites:
  - Microsoft Purview agents run on Security Compute Units (SCUs), which must be provisioned
  - Roles for deploying and using the agent; an agent identity (recommended) or the setup user's identity
  - Microsoft 365 data in scope
  risks_and_guardrails:
  - Both posture agents are labelled 'in preview' (MSFT-PURVIEWAGENTS-2026)
  - The agent can run under its own Entra agent identity, which Microsoft recommends over the administrator's identity (MSFT-PURVIEWAGENTS-2026, 'Agent identity')
  human_checkpoints:
  - The requester reads the search results and LLM risk summary and decides what to act on; remediation tasks are tracked for human review (MSFT-PURVIEWAGENTS-2026)
  role_evolution: Data security analysts ask questions in natural language instead of building keyword or filter searches (MSFT-PURVIEWAGENTS-2026).
  evidence_grade: C
  sources:
  - ref: MSFT-PURVIEWAGENTS-2026
    title: Security Copilot Agents in Microsoft Purview overview
    publisher: Microsoft Learn
    type: vendor
    url: https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview
    date: '2026-03-23'
    access: full
    locator: '''Data Security Posture Agent'' section; ''Agent identity'''
  last_reviewed: '2026-10-17'
  notes: Product documentation only; no named customer or measurement found. Page date is the ms.date metadata (2026-03-23).
- id: security-data-privacy-05
  title: AI-native data security posture platforms that discover, classify and remediate sensitive data across cloud, SaaS and file shares
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - data-reporting
  - review-assurance
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Organizations do not know what sensitive data they hold or where; Varonis telemetry across 1,000 environments found only about one in ten companies had labelled files (VARONIS-SODS-2025).
  solution: 'Cyera''s customer stories describe agentless scanning of data stores to find and classify sensitive records, then clean-up and remediation: ChenMed resolved more than 32,000 data security issues and strengthened compliance across 30 policies; Paramount scanned trillions of records and identified billions as sensitive; Vetcor found and fixed externally shared sensitive files, including data left from a Google-to-Microsoft migration (CYERA-CHENMED-2026; CYERA-PARAMOUNT-2026; CYERA-VETCOR-2026). The pages do not describe how AI contributes beyond the platform being called ''AI-native''.'
  outcomes:
  - lever: risk
    description: Issues remediated at a named healthcare organization
    figure: More than 32,000 data security issues resolved; compliance strengthened across 30 distinct policies
    measures: ChenMed's resolved data security issues and policies covered, as stated in the vendor's 'Key Takeaways'; the period and definition of an 'issue' are not given.
    provenance: vendor-published
    source_ref: CYERA-CHENMED-2026
  - lever: capacity
    description: Scan scale at a named enterprise (Paramount)
    figure: Trillions of records scanned, billions identified as sensitive; purchase to full operationalization 'within months'
    measures: Records scanned and records flagged sensitive, as stated in the vendor's 'Key Takeaways'; no precision or review rate is given.
    provenance: vendor-published
    source_ref: CYERA-PARAMOUNT-2026
  - lever: quality
    description: Vendor claim of classification precision at scale
    figure: More than 95% precision on exabytes of data
    measures: Cyera's own claim about discovery and classification, reported by trade press; the sample, labelling method and denominator are not stated.
    provenance: vendor-published
    source_ref: CYERA-SERIESG-2026
  prerequisites:
  - Access (agentless in the Paramount story) to cloud, SaaS and file-share data stores
  - Named owners able to act on remediation findings
  - A policy set to map findings to (ChenMed cites 30 policies)
  risks_and_guardrails:
  - All figures come from the vendor's own customer stories and funding coverage; none is independent (CYERA-CHENMED-2026; CYERA-SERIESG-2026)
  - The stories give no false-positive, miss or override rate
  - Varonis, a competitor, reports that 99% of 1,000 environments hold sensitive data that AI can easily surface, which frames the exposure these tools target (VARONIS-SODS-2025)
  human_checkpoints:
  - Security and data owners decide which findings to remediate; Vetcor says tabletop exercises validated what data would be exposed in an attack (CYERA-VETCOR-2026)
  role_evolution: The vendor stories say a leaner or small team can run discovery, clean-up and protection at scale (CYERA-CHENMED-2026; CYERA-VETCOR-2026). This is a vendor claim with no staffing figures.
  evidence_grade: B
  sources:
  - ref: CYERA-CHENMED-2026
    title: ChenMed Achieves Data Security Excellence with Cyera, Remediating Over 32,000 Issues (customer story; page shows no publication date, date given is retrieval date)
    publisher: Cyera
    type: vendor
    url: https://www.cyera.com/customer-story/chenmed-achieves-data-security-excellence-with-cyera
    date: '2026-10-17'
    access: full
    locator: '''Key Takeaways'''
  - ref: CYERA-PARAMOUNT-2026
    title: Paramount Gains Full Data Visibility with Cyera, Identifying Billions of Sensitive Records (customer story; no publication date shown, date given is retrieval date)
    publisher: Cyera
    type: vendor
    url: https://www.cyera.com/customer-story/paramount-gains-full-data-visibility-with-cyera-identifying-billions-of-sensitive-records
    date: '2026-10-17'
    access: full
    locator: '''Key Takeaways'''
  - ref: CYERA-VETCOR-2026
    title: Vetcor Achieves Rapid Data Visibility and Protection with Cyera (customer story; no publication date shown, date given is retrieval date)
    publisher: Cyera
    type: vendor
    url: https://www.cyera.com/customer-story/vetcor-achieves-rapid-data-visibility-and-protection-with-cyera
    date: '2026-10-17'
    access: full
    locator: '''Key Takeaways'''
  - ref: CYERA-SERIESG-2026
    title: Cyera Raises $600 Million Series G At $12 Billion Valuation To Expand Enterprise AI Trust Layer (trade-press report of a company announcement)
    publisher: Pulse 2.0
    type: press
    url: https://pulse2.com/cyera-raises-300-million-at-12-billion-valuation-in-rapid-ascent-to-top-of-data-security-market/
    date: '2026-06-10'
    access: full
    locator: Paragraph on the AI-native platform and >95% precision
  - ref: VARONIS-SODS-2025
    title: Data Security Report Reveals 99% of Orgs Have Sensitive Information Exposed to AI (2025 State of Data Security Report summary)
    publisher: Varonis
    type: vendor
    url: https://www.varonis.com/blog/state-of-data-security-report
    date: '2025-05-20'
    access: full
    locator: '''About the report'''
  last_reviewed: '2026-10-17'
  notes: 'Graded B: named deployments with vendor-published program counts, not measures of classification quality. The customer-story pages show no publication dates (date given is retrieval date). Cyera''s funding and acquisition details came from trade press and an aggregator (search-only for acquisitions); the $1B Oasis deal reported by one aggregator is unverified.'
- id: security-data-privacy-06
  title: Agent triage of DLP alerts into 'needs attention' and 'less urgent' queues with a written rationale
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - transaction-processing
  - review-assurance
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: Triaging and prioritising DLP alerts is complex and time-consuming (MSFT-PURVIEWAGENTS-2026). The CSA report says DLP often detects data loss after the fact and examines how false positives and alert fatigue affect analyst workload and team retention (CSA-AI-2026).
  solution: The Microsoft Purview Triage Agent in DLP reads alerts from active-mode DLP policies on Exchange, Teams, OneDrive, SharePoint and endpoint devices, analyses the content of the files behind each alert, and sorts alerts into 'Needs attention' and 'Less urgent' with an explanation. It ranks on content risk (sensitive information types, trainable classifiers, default labels), exfiltration risk and policy risk. Admins can add natural-language custom instructions (content conditions only) and give feedback to revise a verdict (MSFT-PURVIEWAGENTS-2026; MSFT-PURVIEWDLPTRIAGE-2026). AI summaries and categories also appear in Defender XDR; Microsoft's Message Center says the public preview would begin rolling out in early April 2026 (MSFT-MC1255406-2026).
  outcomes:
  - lever: speed
    description: Microsoft says prioritisation reduces triage time and sharpens analyst focus
    figure: none published
    measures: No alert volumes, time savings, accuracy or override rates are published.
    provenance: vendor-published
    source_ref: MSFT-PURVIEWAGENTS-2026
  prerequisites:
  - Microsoft DLP licensing plus provisioned Security Compute Units (usage depends on alert count and type)
  - DLP policies in active mode (simulation-mode alerts are not triaged)
  - Endpoint evidence collection for file activities on devices if device alerts are in scope
  - Roles for deploying the agent and acting on its verdicts
  risks_and_guardrails:
  - 'Documented limits: files above 2 MB are not triaged; for alerts with 10 or more files only the top 10 risky files are summarised, with a note; alerts raised only by non-content conditions (for example an email subject match) are not triaged; some alerts end up ''Not categorized'' (MSFT-PURVIEWAGENTS-2026; MSFT-PURVIEWDLPTRIAGE-2026)'
  - Microsoft says analysts should triage manually any alert the agent does not evaluate (MSFT-PURVIEWAGENTS-2026)
  - Feedback does not change the current alert until an admin re-runs a triage pass (MSFT-PURVIEWDLPTRIAGE-2026, 'Feedback for alerts triaged')
  - The Defender XDR general-availability date moved from August 2026 to August 2027 in a Message Center update of 2026-08-17 (MSFT-MC1255406-2026)
  human_checkpoints:
  - Analysts review each categorised alert and rationale and can overrule it through feedback (MSFT-PURVIEWDLPTRIAGE-2026)
  - The agent runs under its own agent identity, or the administrator's identity if chosen (MSFT-PURVIEWAGENTS-2026)
  role_evolution: Analysts work a ranked queue with explanations and tune the agent with custom instructions and feedback, instead of working alerts in arrival order (MSFT-PURVIEWAGENTS-2026; MSFT-PURVIEWDLPTRIAGE-2026).
  evidence_grade: C
  sources:
  - ref: MSFT-PURVIEWAGENTS-2026
    title: Security Copilot Agents in Microsoft Purview overview
    publisher: Microsoft Learn
    type: vendor
    url: https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview
    date: '2026-03-23'
    access: full
    locator: '''Data Security Triage Agent''; ''How agents prioritize''; ''Alert triage details'''
  - ref: MSFT-PURVIEWDLPTRIAGE-2026
    title: Get started with the Microsoft Purview Triage Agent in Data Loss Prevention
    publisher: Microsoft Learn
    type: vendor
    url: https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started
    date: '2026-06-25'
    access: full
    locator: Licensing; 'Feedback for alerts triaged'
  - ref: MSFT-MC1255406-2026
    title: MC1255406 Microsoft Purview | Data Security Triage Agent Summaries for DLP Alerts in Microsoft Defender XDR (Message Center archive; published 2026-03-18, updated 2026-08-17)
    publisher: Microsoft 365 Message Center (archive at mc.merill.net)
    type: vendor
    url: https://mc.merill.net/message/MC1255406
    date: '2026-03-18'
    access: full
    locator: Summary and 'When this will happen'
  - ref: CSA-AI-2026
    title: 'DLP in the AI Era: Data Loss Prevention Survey Report (landing page and abstract; report body is login-gated and was not read)'
    publisher: Cloud Security Alliance
    type: survey
    url: https://cloudsecurityalliance.org/artifacts/dlp-in-the-ai-era-survey-report
    date: '2026-10-09'
    access: full
    locator: Abstract and key takeaways
  last_reviewed: '2026-10-17'
  notes: Product documentation and a Message Center post; no named customer or measured outcome was found despite a targeted search. Message Center dates conflict between the archive (GA August 2027, previously August 2026) and a third-party mirror seen in search; the archive is used here.
- id: security-data-privacy-07
  title: Context-aware, AI-based DLP classification to replace pattern-matching and cut false-positive alert load
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - transaction-processing
  - review-assurance
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Legacy DLP tools struggled to classify nuanced unstructured files and produced so many false positives that OpenWeb's team could not trust the alerts (MIND-OPENWEB-2026). In the CSA survey, only 16% of respondents who suffered data loss said DLP blocked their most significant incident before data left (CSA-AI-2026).
  solution: OpenWeb replaced its DLP tools with MIND, which the vendor says uses tailored algorithms and a proprietary AI engine to discover and classify unstructured data at rest with context, and shows who has access to which data (MIND-OPENWEB-2026). An unnamed US financial institution says Cyera helped it discover, tag and move data into quarantine for a document-retention programme that had stalled for years (CYERA-FI-2026).
  outcomes:
  - lever: cost
    description: OpenWeb's CISO estimates the time spent managing DLP
    figure: '''Probably a fifth'' of the time spent before (the page headline also says 80% fewer resources)'
    measures: The CISO's own estimate of time spent managing the DLP programme compared with legacy tools; no baseline hours given.
    provenance: vendor-published
    source_ref: MIND-OPENWEB-2026
  - lever: quality
    description: False-positive alert volume at an unnamed US financial institution
    figure: About 16,000 false-positive DLP events reduced to 'just a handful'
    measures: False-positive DLP events as stated in the vendor's results list; the customer is not named and the period is not given.
    provenance: vendor-published
    source_ref: CYERA-FI-2026
  prerequisites:
  - Discovery and classification of data at rest across cloud, Microsoft 365 and file shares
  - Teams willing to tune the tool with the vendor
  - Agreed policies for quarantine or retention actions
  risks_and_guardrails:
  - Both outcomes are vendor-published case-study statements, one from an unnamed customer; there is no independent measurement (MIND-OPENWEB-2026; CYERA-FI-2026)
  - The OpenWeb page says 'almost no false positives' but gives no recall or miss rate, so missed leaks are not measured (MIND-OPENWEB-2026)
  human_checkpoints:
  - Security teams review remaining alerts; the institution describes a risk-driven DLP programme that security, privacy and governance teams could use together (CYERA-FI-2026)
  role_evolution: OpenWeb's CISO says the team now trusts alerts enough to use them for decisions and automation (MIND-OPENWEB-2026). The institution says DLP moved from a manual, noisy process to a risk-driven programme shared by security, privacy and governance teams (CYERA-FI-2026).
  evidence_grade: B
  sources:
  - ref: MIND-OPENWEB-2026
    title: OpenWeb uses MIND to modernize and automate data loss prevention (customer story; no publication date shown, date given is retrieval date)
    publisher: MIND
    type: vendor
    url: https://mind.io/customers/openweb
    date: '2026-10-17'
    access: full
    locator: Challenge, solution and results sections; CISO quotes
  - ref: CYERA-FI-2026
    title: 'Turning Data Noise into Actionable Security: Lessons from a Leading Financial Institution (customer story, institution unnamed; no publication date shown, date given is retrieval date)'
    publisher: Cyera
    type: vendor
    url: https://www.cyera.com/customer-story/lessons-from-a-leading-financial-institution
    date: '2026-10-17'
    access: full
    locator: '''Results'''
  - ref: CSA-AI-2026
    title: 'DLP in the AI Era: Data Loss Prevention Survey Report (landing page and abstract; report body is login-gated and was not read)'
    publisher: Cloud Security Alliance
    type: survey
    url: https://cloudsecurityalliance.org/artifacts/dlp-in-the-ai-era-survey-report
    date: '2026-10-09'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-17'
  notes: 'Graded B: one named customer (OpenWeb) with a CISO estimate, plus an unnamed institution. Both case-study pages are undated (date given is retrieval date). Search-only vendor claims, for example a Palo Alto Networks statement of more than 90% fewer potential false positives and a Frost and Sullivan report quoting an unnamed customer at 80% less DLP resource use, are not used as outcomes.'
- id: security-data-privacy-08
  title: Inline DLP on prompts, pastes and uploads to generative AI tools
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - transaction-processing
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Staff paste source code, regulated data and credentials into generative AI tools. Netskope telemetry shows the average organization has 3% of genAI users committing about 223 policy violations a month (NETSKOPE-CTR-2026), and Cyberhaven reports that 39.7% of data movements into AI tools involve sensitive data (CYBERHAVEN-AIRISK-2026). In the CSA survey, only 29% of respondents could routinely produce a 30-day report of sensitive data sent to GenAI tools (CSA-AI-2026).
  solution: Endpoint DLP policies in Microsoft Purview can warn or block users who paste sensitive information into third-party generative AI sites in a browser (for example credit card numbers into ChatGPT), and sensitive information types and trainable classifiers can inspect prompts and responses in supported AI apps (MSFT-PURVIEWAI-2026). A practitioner on Hacker News describes routing LLM API traffic through a proxy that tokenises PII and blocks secrets, and says policy-only rules do not work (HN-ASKLLMAPI-2026).
  outcomes:
  - lever: risk
    description: 'Baseline: genAI policy violations detected per organization'
    figure: 3% of genAI users committing an average of 223 violations a month
    measures: Netskope's average organization; the share of genAI users who commit violations and the monthly number of genAI data policy violations. Netskope says violations roughly doubled over the past year, and that 50% of organizations lack enforceable genAI data protection policies, so true leakage is likely higher.
    provenance: vendor-published
    source_ref: NETSKOPE-CTR-2026
  - lever: risk
    description: 'Baseline: sensitive content in AI data movements'
    figure: 39.7% of data movements into AI tools involve sensitive data
    measures: Share of all data movements into AI tools (prompts, copy-paste) that involve sensitive data, from Cyberhaven Labs' billions of observed data movements.
    provenance: vendor-published
    source_ref: CYBERHAVEN-AIRISK-2026
  - lever: quality
    description: 'Baseline: ability to evidence GenAI leakage'
    figure: 29% of respondents can routinely produce a 30-day report of sensitive data sent to GenAI tools
    measures: Share of the 433 surveyed IT and security professionals reporting this capability, per the CSA abstract.
    provenance: independent
    source_ref: CSA-AI-2026
  prerequisites:
  - Endpoints onboarded to the DLP product and a browser extension or configuration for browser-based AI sites
  - Sensitive information types or classifiers that match the organization's data
  - A decision on which AI sites and accounts are sanctioned
  risks_and_guardrails:
  - The three outcomes are baselines of exposure and visibility, not measured effects of a control (NETSKOPE-CTR-2026; CYBERHAVEN-AIRISK-2026; CSA-AI-2026)
  - Users can override a warning where the policy allows it (MSFT-PURVIEWAI-2026)
  - 'Personal-account use is still material (Cyberhaven: 32.3% of ChatGPT usage through personal accounts), which limits what organizational controls can see (CYBERHAVEN-AIRISK-2026)'
  human_checkpoints:
  - Policy owners decide warn versus block; users can be shown a warning they may override (MSFT-PURVIEWAI-2026)
  role_evolution: Not documented in these sources beyond DLP owners adding AI sites and prompt content to existing policies.
  evidence_grade: C
  sources:
  - ref: MSFT-PURVIEWAI-2026
    title: Microsoft Purview data security and compliance protections for Microsoft 365 Copilot and other generative AI apps
    publisher: Microsoft Learn
    type: vendor
    url: https://learn.microsoft.com/en-us/purview/ai-microsoft-purview
    date: '2026-05-27'
    access: full
    locator: '''Data loss prevention and AI interactions''; ''Data classification and AI interactions'''
  - ref: NETSKOPE-CTR-2026
    title: 'Cloud and Threat Report: 2026'
    publisher: Netskope
    type: vendor
    url: https://www.netskope.com/blog/cloud-and-threat-report-2026
    date: '2026-01-05'
    access: full
    locator: '''GenAI data policy violation incidents are rapidly increasing'''
  - ref: CYBERHAVEN-AIRISK-2026
    title: '2026 AI Adoption & Risk Report: Data Governance Gaps Widening (press release)'
    publisher: Cyberhaven
    type: vendor
    url: https://www.cyberhaven.com/press-releases/cyberhaven-2026-ai-adoption-risk-report
    date: '2026-02-05'
    access: full
    locator: Press release body
  - ref: CSA-AI-2026
    title: 'DLP in the AI Era: Data Loss Prevention Survey Report (landing page and abstract; report body is login-gated and was not read)'
    publisher: Cloud Security Alliance
    type: survey
    url: https://cloudsecurityalliance.org/artifacts/dlp-in-the-ai-era-survey-report
    date: '2026-10-09'
    access: full
    locator: Abstract
  - ref: HN-ASKLLMAPI-2026
    title: 'Ask HN: Are companies preventing sensitive data from being sent to external LLM APIs (thread of 2 comments; comment 47265310)'
    publisher: Hacker News
    type: community
    url: https://news.ycombinator.com/item?id=47259975
    date: '2026-03-05'
    access: full
    locator: Comment 47265310
  last_reviewed: '2026-10-17'
  notes: Marked 'announced' because no named organization using the control with measured results was found; the telemetry comes from unnamed customers of the vendors. The CSA figure is a survey of practitioners and is the only non-vendor measure here, but it is a self-report of capability, not an audit.
- id: security-data-privacy-09
  title: Discover shadow AI use and block or steer unsanctioned AI apps and personal accounts
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - data-reporting
  - review-assurance
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Employees adopt AI tools outside security and procurement review, and AI features appear inside existing procured apps without governance being told (OWASP-DATASEC-2026, DSGAI03, p. 24-25).
  solution: Netskope reports that 90% of organizations actively block at least one genAI app (10 on average), led by ZeroGPT (45% of organizations) and DeepSeek (43%), while the share of AI users on personal AI apps fell from 78% to 47% as managed accounts rose from 25% to 62% (NETSKOPE-CTR-2026). OWASP's recommended controls are an allowed-tool policy, a central AI service catalogue with security and privacy review, vendor contracts covering retention and training, governed enterprise alternatives, and DLP and CASB controls (OWASP-DATASEC-2026, DSGAI03). Akamai completed its acquisition of the browser-security provider LayerX on 2026-07-02, after announcing a deal of about US$205 million on 14 May (AKAMAI-LAYERX-2026).
  outcomes:
  - lever: risk
    description: Organizations actively blocking unwanted genAI apps
    figure: 90% of organizations; 10 apps blocked on average
    measures: Share of Netskope's customer organizations with an active block policy that is actually preventing access, and the average number of apps blocked; it excludes organizations outside Netskope's customer base.
    provenance: vendor-published
    source_ref: NETSKOPE-CTR-2026
  - lever: risk
    description: Shift from personal to organization-managed AI accounts
    figure: Personal-account share of AI users fell from 78% to 47%; managed-account share rose from 25% to 62%
    measures: Percentage of genAI users using personal versus organization-managed accounts, year on year, in Netskope's telemetry.
    provenance: vendor-published
    source_ref: NETSKOPE-CTR-2026
  prerequisites:
  - An AI service catalogue and an approved-tools policy
  - Network or browser visibility into AI domains and accounts
  - Enterprise AI alternatives so staff have a sanctioned route
  risks_and_guardrails:
  - Blocking does not reach AI features embedded in already-procured software or internally built tooling (OWASP-DATASEC-2026, DSGAI03)
  - Netskope notes that the number of tracked genAI apps rose from 317 to more than 1,600 in a year, so block lists age quickly (NETSKOPE-CTR-2026)
  - Telemetry is from the vendor's customers and is not independently audited
  human_checkpoints:
  - Security and procurement owners approve the allowed-tool list and review new AI services (OWASP-DATASEC-2026, DSGAI03 Tier 1)
  role_evolution: Not documented in these sources.
  evidence_grade: C
  sources:
  - ref: NETSKOPE-CTR-2026
    title: 'Cloud and Threat Report: 2026'
    publisher: Netskope
    type: vendor
    url: https://www.netskope.com/blog/cloud-and-threat-report-2026
    date: '2026-01-05'
    access: full
    locator: '''SaaS genAI use is rapidly increasing''; ''Blocking unwanted genAI apps reduces data exposure risk'''
  - ref: OWASP-DATASEC-2026
    title: OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0, 103-page PDF)
    publisher: OWASP GenAI Security Project
    type: standard-setter
    url: https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/
    date: '2026-03-17'
    access: full
    locator: DSGAI03, pages 24-26
  - ref: AKAMAI-LAYERX-2026
    title: Akamai Completes Acquisition of Secure Enterprise Browser Provider LayerX
    publisher: Akamai
    type: vendor
    url: https://www.akamai.com/newsroom/press-release/akamai-completes-acquisition-of-secure-enterprise-browser-provider-layerx
    date: '2026-07-02'
    access: full
    locator: Opening paragraphs
  - ref: CYBERHAVEN-AIRISK-2026
    title: '2026 AI Adoption & Risk Report: Data Governance Gaps Widening (press release)'
    publisher: Cyberhaven
    type: vendor
    url: https://www.cyberhaven.com/press-releases/cyberhaven-2026-ai-adoption-risk-report
    date: '2026-02-05'
    access: full
    locator: Personal-account shares
  last_reviewed: '2026-10-17'
  notes: Vendor telemetry without named customers, so 'announced' is the closest maturity value.
- id: security-data-privacy-10
  title: Assess and reduce oversharing before and during rollout of AI assistants over enterprise content
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - review-assurance
  - data-reporting
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: AI assistants surface content quickly, which amplifies existing oversharing; Microsoft states generative AI 'amplifies the problem' of oversharing and leaking data (MSFT-PURVIEWAI-2026). Varonis reports that 99% of 1,000 analysed environments hold sensitive data that AI can easily surface (VARONIS-SODS-2025).
  solution: Microsoft Purview DSPM tracks agent and AI-app activity such as oversharing, exfiltration and unusual access, and offers data risk assessments (MSFT-DSPM-2026; MSFT-PURVIEWAI-2026). SharePoint Restricted Content Discovery removes selected sites from organization-wide search and Copilot, and hides AI entry points on those sites, as a temporary control while permissions are right-sized (MSFT-SPRCD-2026).
  outcomes:
  - lever: risk
    description: Baseline from Varonis telemetry on AI-reachable exposed data
    figure: 99% of 1,000 organizations had sensitive data exposed that AI can easily surface
    measures: Share of 1,000 real-world IT environments analysed by Varonis (nearly 10 billion files) with exposed sensitive data; a baseline of exposure, not a measured effect of remediation. The same report says only 1 in 10 companies had labelled files.
    provenance: vendor-published
    source_ref: VARONIS-SODS-2025
  prerequisites:
  - Sensitivity labels and permission data for the content estate
  - Owners for sites that need review
  - Licences and roles for the DSPM or SharePoint admin features
  risks_and_guardrails:
  - Restricted Content Discovery does not change permissions; users who already have access keep direct access (MSFT-SPRCD-2026)
  - Microsoft warns that excessive use reduces the completeness and relevance of search and Copilot answers, and the feature does not cover OneDrive (MSFT-SPRCD-2026)
  - Microsoft describes it as a temporary governance control (MSFT-SPRCD-2026)
  human_checkpoints:
  - Admins choose which sites to restrict and decide on permission clean-up (MSFT-SPRCD-2026)
  role_evolution: Not documented in these sources.
  evidence_grade: C
  sources:
  - ref: MSFT-PURVIEWAI-2026
    title: Microsoft Purview data security and compliance protections for Microsoft 365 Copilot and other generative AI apps
    publisher: Microsoft Learn
    type: vendor
    url: https://learn.microsoft.com/en-us/purview/ai-microsoft-purview
    date: '2026-05-27'
    access: full
    locator: Section 'Microsoft Purview strengthens information protection for AI apps' (oversharing statement); related-content link to DSPM for AI Data Risk Assessment
  - ref: MSFT-DSPM-2026
    title: Learn about Microsoft Purview Data Security Posture Management (DSPM)
    publisher: Microsoft Learn
    type: vendor
    url: https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about
    date: '2026-05-01'
    access: full
    locator: AI observability description
  - ref: MSFT-SPRCD-2026
    title: Restrict discovery of SharePoint sites and content
    publisher: Microsoft Learn
    type: vendor
    url: https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
    date: '2026-10-11'
    access: full
    locator: Whole page
  - ref: VARONIS-SODS-2025
    title: Data Security Report Reveals 99% of Orgs Have Sensitive Information Exposed to AI (2025 State of Data Security Report summary)
    publisher: Varonis
    type: vendor
    url: https://www.varonis.com/blog/state-of-data-security-report
    date: '2025-05-20'
    access: full
    locator: '''About the report'''
  last_reviewed: '2026-10-17'
  notes: No named-customer result for oversharing remediation was found in public sources (a targeted search returned consultant and vendor marketing and one unnamed anecdote).
- id: security-data-privacy-11
  title: Agents propose and, with approval, carry out fixes for exposed data such as public links and excess permissions
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - review-assurance
  - software-systems
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: Access and sharing problems are found in dashboards but fixed by hand, one object at a time. Microsoft describes DSPM as consolidating DLP, insider risk, labelling and investigation signals into one view of data risks and policy coverage (MSFT-DSPM-2026).
  solution: In the current Purview DSPM, Security Copilot and AI agents analyse access patterns, sharing behaviour and policy gaps, prioritise risks, and can take direct action on detected risks such as removing public sharing links, applying DLP policies or revoking permissions. Microsoft says users review, approve or customise the automated actions, and the actions are audited (MSFT-DSPM-2026, 'How AI helps achieve data security outcomes').
  outcomes:
  - lever: speed
    description: Microsoft says AI makes data security 'more adaptive' and less reliant on manual intervention
    figure: none published
    measures: No time, volume or accuracy figure is given.
    provenance: vendor-published
    source_ref: MSFT-DSPM-2026
  prerequisites:
  - Security Copilot and Security Compute Units
  - Entra Compliance Administrator or Purview Compliance Administrator role, and the Data Security Viewer role for Security Copilot
  - Allow about a day after first set-up before tenant data appears (MSFT-DSPM-2026)
  risks_and_guardrails:
  - Actions are approved or customised by a person and are always audited (MSFT-DSPM-2026)
  - Agents can run under a dedicated Entra agent identity rather than an admin's identity (MSFT-PURVIEWAGENTS-2026, 'Agent identity')
  - Coverage of non-Microsoft locations depends on partner integrations; Microsoft names Varonis, Cyera, BigID and OneTrust as integrated partners (MSFT-DSPM-2026)
  human_checkpoints:
  - An administrator approves or edits each automated action before it takes effect (MSFT-DSPM-2026)
  role_evolution: Data security admins approve and tune agent-proposed fixes instead of performing each fix themselves (MSFT-DSPM-2026).
  evidence_grade: C
  sources:
  - ref: MSFT-DSPM-2026
    title: Learn about Microsoft Purview Data Security Posture Management (DSPM)
    publisher: Microsoft Learn
    type: vendor
    url: https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about
    date: '2026-05-01'
    access: full
    locator: '''How AI helps achieve data security outcomes''; partner integrations paragraph'
  - ref: MSFT-PURVIEWAGENTS-2026
    title: Security Copilot Agents in Microsoft Purview overview
    publisher: Microsoft Learn
    type: vendor
    url: https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview
    date: '2026-03-23'
    access: full
    locator: '''Agent identity'''
  last_reviewed: '2026-10-17'
  notes: Product documentation; the page does not mark this capability as preview or generally available, so 'piloting' is a conservative reading. No named customer or measurement found.
- id: security-data-privacy-12
  title: Enforce sensitivity labels and user entitlements when AI assistants retrieve content, and carry labels onto embeddings and indexes
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - review-assurance
  - software-systems
  pattern: grounded-knowledge-assistant
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: In a generative AI system the context window pools system prompts, retrieved passages, user input and tool output into one flat space with no internal access control, so a chunk from a confidential HR store sits beside user input with equal trust (OWASP-DATASEC-2026, p. 6). Classification and lifecycle rules that stop at the raw file do not reach embeddings, caches or backups (OWASP-DATASEC-2026, DSGAI07, p. 42-43).
  solution: Microsoft states that supported AI apps use existing controls so tenant data is not returned to, or used by, the model if the user lacks access, and that for encrypted sensitivity labels the user needs both VIEW and EXTRACT rights before an AI app returns the content (MSFT-PURVIEWAI-2026). OWASP recommends that labels propagate to every derivative (embeddings, indexes, caches, backups), that retrieval enforce per-document access control and redaction, and that erasure workflows cover derived artifacts (OWASP-DATASEC-2026, p. 9-10, 42-44). A research prototype, ARBITER, uses few-shot LLMs for role-based filtering of RAG queries (ARXIV-ARBITER-2025).
  outcomes:
  - lever: risk
    description: Research result for LLM-based role filtering of RAG queries (prototype)
    figure: 85% accuracy and 89% F1 on query filtering
    measures: Accuracy and F1 for allowing or filtering queries by role, on 389 queries from a synthetic dataset; authors say results are close to traditional RBAC. Not a production measurement.
    provenance: independent
    source_ref: ARXIV-ARBITER-2025
  prerequisites:
  - Sensitivity labels applied to the content estate, with labels enabled for SharePoint and OneDrive files (MSFT-PURVIEWAI-2026)
  - A live inventory linking source records to derived artifacts (OWASP-DATASEC-2026, DSGAI07)
  - Per-user or per-tenant identity passed through to retrieval
  risks_and_guardrails:
  - Microsoft notes that without labels enabled for SharePoint and OneDrive, the encrypted files AI can reach are limited to data in use from Office apps on Windows (MSFT-PURVIEWAI-2026)
  - Password-protected files cannot be read by AI apps unless already open in the same app, and S/MIME email is not returned (MSFT-PURVIEWAI-2026)
  - OWASP says its mitigations 'work around' the flat-context limitation rather than solve it (OWASP-DATASEC-2026, p. 6-7)
  - A simulated deletion test (delete a test record and check database, logs, embeddings, backups and outputs) is recommended as a standard validation (OWASP-DATASEC-2026, DSGAI07)
  human_checkpoints:
  - Data owners assign labels and review high-impact RAG corpora (OWASP-DATASEC-2026, p. 11)
  role_evolution: Not documented in these sources.
  evidence_grade: C
  sources:
  - ref: MSFT-PURVIEWAI-2026
    title: Microsoft Purview data security and compliance protections for Microsoft 365 Copilot and other generative AI apps
    publisher: Microsoft Learn
    type: vendor
    url: https://learn.microsoft.com/en-us/purview/ai-microsoft-purview
    date: '2026-05-27'
    access: full
    locator: '''Sensitivity labels and AI interactions''; ''Encryption without sensitivity labels and AI interactions'''
  - ref: OWASP-DATASEC-2026
    title: OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0, 103-page PDF)
    publisher: OWASP GenAI Security Project
    type: standard-setter
    url: https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/
    date: '2026-03-17'
    access: full
    locator: p. 6-7 (flat context window); p. 9-11 (DSPM for GenAI); DSGAI07 p. 42-44
  - ref: ARXIV-ARBITER-2025
    title: 'ARBITER: AI-Driven Filtering for Role-Based Access Control'
    publisher: arXiv preprint
    type: academic
    url: https://arxiv.org/abs/2512.20535
    date: '2025-12-23'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-17'
  notes: 'Marked ''announced'': the Microsoft page documents shipped behaviour but names no customer, and no measured result for either vendor controls or OWASP''s mitigations was found. The research figure is from a synthetic dataset and is shown for scale only.'
- id: security-data-privacy-13
  title: LLM-guided workflow that turns privacy requirements into enforceable data controls using lineage
  archetype: security
  module: data-privacy
  function: risk-compliance-legal
  work_types:
  - document-production
  - software-systems
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Turning textual privacy requirements, especially purpose limitation, into controls across large data ecosystems is slow, error-prone and hard to validate (PEPR-2026, Meta session 'From Legalese to Logic', Monday 9:30).
  solution: Meta engineers described an experience report on an LLM-powered guided workflow that helps engineers break requirement text into implementable 'privacy jobs to be done', walk data lineage to find affected datasets and flows, suggest enforcement and monitoring points, and track each requirement from interpretation to implementation to verification. A companion talk describes Meta's in-memory lineage graph, which processes billions of edges across web, warehouse and AI systems and supports 'agentic analysis' through interactive traversals (PEPR-2026, Monday 4:10).
  outcomes:
  - lever: speed
    description: The session covers where automation helped and where human judgment stayed essential, including misinterpretations and lineage gaps
    figure: none published
    measures: Only the session abstracts were read; no time, accuracy or error-rate figures appear in the abstracts.
    provenance: self-reported
    source_ref: PEPR-2026
  prerequisites:
  - A data lineage graph covering web, warehouse and AI systems
  - Machine-readable inventory of datasets and flows
  - Engineers who own the controls and the verification step
  risks_and_guardrails:
  - The abstract names misinterpretation of requirements and lineage gaps as failure modes (PEPR-2026, Monday 9:30)
  - Slides and videos were not opened; claims here are limited to the program abstracts
  human_checkpoints:
  - Engineers review each suggested job, enforcement point and verification state; the talk says human judgment remained essential in places (PEPR-2026, Monday 9:30)
  role_evolution: Engineers work from decomposed 'privacy jobs' and tracked state instead of reading requirement text and mapping data flows manually (PEPR-2026, Monday 9:30).
  evidence_grade: B
  sources:
  - ref: PEPR-2026
    title: PEPR '26 program (USENIX Conference on Privacy Engineering Practice and Respect, 1-2 June 2026, Santa Clara)
    publisher: USENIX
    type: conference
    url: https://www.usenix.org/conference/pepr26/program
    date: '2026-06-01'
    access: full
    locator: Monday 9:30 am 'From Legalese to Logic'; Monday 4:10 pm 'Architecting Scalable Data Lineage Graph for Privacy Compliance and Agentic Analysis'
  last_reviewed: '2026-10-17'
  notes: Named deployment (Meta) described in a conference abstract. The abstract says the team is presenting 'an experience report on deploying' the workflow but does not say how widely it is used, so maturity is kept at 'piloting'. Companion Meta blog (META-ENG-ASSETCLASS-2026) covers the related classification layer.
- id: security-data-privacy-14
  title: Retrieval-augmented LLM detection of privacy-relevant code patterns in pull requests
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - review-assurance
  - software-systems
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Many privacy failures come from ordinary design and coding choices rather than obvious privacy code. Default Grant Access, where access is allowed unless a developer blocks it, is hard for static analysis because the risk depends on defaults, conditional logic and framework behaviour (PEPR-2026, Microsoft session, Tuesday 2:00).
  solution: Microsoft researchers and engineers reported deploying language-model-based detection of Default Grant Access in pull requests at scale, then replacing a static-prompt approach with retrieval-augmented generation to address high false-positive rates, using curated examples from known incidents (PEPR-2026, Tuesday 2:00).
  outcomes:
  - lever: quality
    description: RAG detector against standalone LLM detector
    figure: More than twice as many confirmed privacy-relevant issues found
    measures: Confirmed privacy-relevant issues found by the RAG system versus the standalone LLM approach across nine production repositories, four languages and 183,000+ methods; absolute counts and the confirmation process are not given in the abstract.
    provenance: self-reported
    source_ref: PEPR-2026
  - lever: quality
    description: False-positive rate after adding retrieval
    figure: No significant improvement; language-specific noise, especially in TypeScript and C++
    measures: The abstract reports that false-positive rates did not improve significantly; no rate is given.
    provenance: self-reported
    source_ref: PEPR-2026
  prerequisites:
  - A curated corpus of examples from known incidents for retrieval
  - Integration into pull-request review workflows
  - Language coverage tuned for noisy languages (TypeScript and C++ were noisy)
  risks_and_guardrails:
  - False-positive rates remained a problem after RAG (PEPR-2026, Tuesday 2:00)
  - The talk covers managing retrieval trade-offs and not overwhelming reviewers (PEPR-2026, Tuesday 2:00)
  human_checkpoints:
  - Code reviewers see detections inside the pull request review and confirm issues (PEPR-2026, Tuesday 2:00)
  role_evolution: Reviewers receive privacy-relevant flags in pull requests and must triage them, with the talk stressing avoiding reviewer overload (PEPR-2026, Tuesday 2:00).
  evidence_grade: A
  sources:
  - ref: PEPR-2026
    title: PEPR '26 program (USENIX Conference on Privacy Engineering Practice and Respect, 1-2 June 2026, Santa Clara)
    publisher: USENIX
    type: conference
    url: https://www.usenix.org/conference/pepr26/program
    date: '2026-06-01'
    access: full
    locator: 'Tuesday 2:00 pm ''Surfacing Hidden Privacy Risks in Code: Lessons from LLM and Retrieval Assisted Detection'''
  last_reviewed: '2026-10-17'
  notes: Graded A on a measured, named-organization result, but the evidence is a conference abstract (talk slides and paper not read), the measures are the team's own, and the abstract gives no absolute counts. The topic overlaps application-security.
- id: security-data-privacy-15
  title: AI first drafts of privacy impact assessments, reassessments and evidence reviews
  archetype: security
  module: data-privacy
  function: risk-compliance-legal
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Product teams often lack the expertise to spot privacy risks early, so privacy experts translate principles and correct late choices (PEPR-2026, Privy session, Monday 9:10). Privacy teams describe 'assessment fatigue' from manual PIAs and recurring reassessments (ONETRUST-W26-2026). Writing a DPIA is hard because it needs interdisciplinary expertise and follows no standard format (ARXIV-DPIALLM-2026).
  solution: 'OneTrust''s Winter ''26 release adds ''AI Inventory Analysis'', which drafts suggested answers for reassessments from earlier evaluations and flags AI-completed fields for review, and ''AI Evidence Analysis'', which reviews evidence in several file formats and produces a summary, a justification score and gap and remediation guidance (ONETRUST-W26-2026). Academic work tests the same idea: Privy gives non-privacy experts a GenAI ''first draft'' of risks and mitigations during AI product ideation, and PIA-Bench measures LLMs against 73 structured PIAs curated from 499 US federal agency PIAs (PEPR-2026; ARXIV-PIABENCH-2026).'
  outcomes:
  - lever: quality
    description: 'Privy: expert rating of the generated privacy assessments'
    figure: 13 independent privacy experts rated the assessments high quality
    measures: Ratings by 13 privacy experts of assessments produced by 24 practitioners using Privy (after a formative study with 11 practitioners); a research study, not a deployment.
    provenance: self-reported
    source_ref: PEPR-2026
  - lever: quality
    description: 'PIA-Bench: whether off-the-shelf LLMs can assess privacy risks'
    figure: '''Meaningful assessments'', with avenues for improvement; no accuracy figure in the abstract'
    measures: Benchmark of 451 privacy risk items and 831 mitigation items across 73 structured PIAs; the abstract gives no score.
    provenance: independent
    source_ref: ARXIV-PIABENCH-2026
  prerequisites:
  - A record of prior assessments for the same processing activities, assets or vendors
  - Defined evidence criteria (controls, legal basis, stakeholder guidance)
  - Privacy reviewers to validate AI-completed fields
  risks_and_guardrails:
  - OneTrust says AI-completed fields are clearly flagged for review and validation (ONETRUST-W26-2026)
  - For DPIA-style documents, less strict guidelines needed richer prompt context to stay consistent and complete; stricter formats produced consistent output but more hallucinations (ARXIV-DPIALLM-2026)
  - PIA-Bench's authors call for accountable LLM infrastructure and new quality standards for PIAs (ARXIV-PIABENCH-2026)
  human_checkpoints:
  - Privacy staff validate AI-completed reassessment fields and review evidence-analysis scores (ONETRUST-W26-2026)
  - Privacy experts still make the product-specific, high-impact decisions in Privy's design (PEPR-2026)
  role_evolution: Privy's authors describe experts focusing on product-specific, high-impact decisions while non-experts prepare first drafts (PEPR-2026). OneTrust describes privacy automation as a 'friction reducer' for teams under constrained budgets (ONETRUST-W26-2026).
  evidence_grade: C
  sources:
  - ref: ONETRUST-W26-2026
    title: 'Evolving Privacy Programs with AI: What''s New in the OneTrust Winter ''26 Release (date from page metadata; a search snippet dated the release to March 2026)'
    publisher: OneTrust
    type: vendor
    url: https://www.onetrust.com/blog/evolving-privacy-programs-with-ai-whats-new-in-the-onetrust-winter-26-release/
    date: '2026-06-10'
    access: full
    locator: '''From Assessment Fatigue to Intelligent Automation'''
  - ref: PEPR-2026
    title: PEPR '26 program (USENIX Conference on Privacy Engineering Practice and Respect, 1-2 June 2026, Santa Clara)
    publisher: USENIX
    type: conference
    url: https://www.usenix.org/conference/pepr26/program
    date: '2026-06-01'
    access: full
    locator: Monday 9:10 am 'Envisioning and Mitigating Privacy Risks for Consumer-Facing AI Product Concepts through Human-AI Teaming'
  - ref: ARXIV-PIABENCH-2026
    title: 'PIA-Bench: Towards Automated Privacy Impact Assessment with Large Language Models'
    publisher: arXiv preprint
    type: academic
    url: https://arxiv.org/abs/2609.12571
    date: '2026-09-11'
    access: full
    locator: Abstract
  - ref: ARXIV-DPIALLM-2026
    title: 'From Regulation to Implementation: A Critical Evaluation of LLM-Assisted Regulatory Compliance in Industry'
    publisher: arXiv preprint
    type: academic
    url: https://arxiv.org/abs/2608.21317
    date: '2026-08-21'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-17'
  notes: 'Graded C: the deployed element is a vendor feature claim; the measured elements are research studies, not deployments. A search snippet said OneTrust AI agents cut assessments ''from weeks to minutes''; that claim was not opened and is not used.'
- id: security-data-privacy-16
  title: 'Idea: LLM-based PII and sensitive-data detection to redact prompts, conversation logs and stored text'
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - data-reporting
  - transaction-processing
  pattern: bulk-transformation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: AI providers scan multi-turn conversations for PII and mask it before storing or processing them, yet most PII detectors and benchmarks target self-contained records (ARXIV-PIITRACE-2026). Benchmarks also hide failures under realistic input shift (ARXIV-MINDGAP-2026).
  solution: Researchers compare rule-based, encoder and LLM detectors and propose hybrids. REDACT tests Presidio, GLiNER, the OpenAI Privacy Filter, GPT-4.1 and Claude Sonnet 4.6; PII-TRACE tests eleven baselines on multi-turn dialogues; Mind the Gap tests spaCy, Presidio and Qwen2.5-3B on shifted inputs. SurrogateShield, a client-side proxy, swaps detected PII for type-consistent surrogates before sending a query to a model (ARXIV-REDACT-2026; ARXIV-PIITRACE-2026; ARXIV-MINDGAP-2026; ARXIV-SURROGATESHIELD-2026).
  outcomes:
  - lever: quality
    description: 'REDACT: recall of a rule-based detector on the most sensitive categories'
    figure: Recall 0.07 on HIGH-sensitivity categories for the rule-based detector; LLM detectors more robust
    measures: Recall on the HIGH-sensitivity tier (a GDPR-aligned tier) for Presidio, on a locked 1,000-record language-stratified sample of a 13,427-record, 25-language benchmark.
    provenance: independent
    source_ref: ARXIV-REDACT-2026
  - lever: quality
    description: 'PII-TRACE: coverage of recurring identifiers across turns'
    figure: No detector reaches full entity-level coverage without substantial false positives on PII-free conversations; single-pass reading loses a third of gold characters on long dialogues
    measures: Eleven baselines including frontier LLMs, evaluated on 13,148 synthetic multi-turn dialogues in 13 languages.
    provenance: independent
    source_ref: ARXIV-PIITRACE-2026
  - lever: quality
    description: 'Mind the Gap: behaviour under distribution shift'
    figure: All three architectures degrade, each with a different failure mode
    measures: Seven categories of natural distribution shift, comparing encoder NER, rule-based hybrid and generative LLM extraction; no single architecture was uniformly reliable.
    provenance: independent
    source_ref: ARXIV-MINDGAP-2026
  prerequisites:
  - Labelled evaluation data that matches the organization's text (formats, languages, informal text)
  - A decision on acceptable miss rate versus false-positive rate
  - Where surrogate substitution is used, local encrypted storage for the mapping (as in SurrogateShield)
  risks_and_guardrails:
  - Aggregate scores mask failures on the highest-stakes categories and non-verbatim disclosures (ARXIV-REDACT-2026)
  - LLM detectors show entity-type confusion and generation instability (ARXIV-MINDGAP-2026)
  - Benchmarks are synthetic or author-built; none reports a production deployment
  human_checkpoints:
  - Not specified in the research; reviewers would set thresholds and spot-check misses.
  role_evolution: Not documented in these sources.
  evidence_grade: D
  sources:
  - ref: ARXIV-REDACT-2026
    title: 'REDACT: A Systematically Controlled Multilingual Benchmark for Personal Information Detection'
    publisher: arXiv preprint
    type: academic
    url: https://arxiv.org/abs/2606.19881
    date: '2026-06-18'
    access: full
    locator: Abstract
  - ref: ARXIV-PIITRACE-2026
    title: 'PII-TRACE: A Benchmark for Context-Aware PII Detection in Multi-Turn LLM Conversations'
    publisher: arXiv preprint
    type: academic
    url: https://arxiv.org/abs/2609.22200
    date: '2026-08-31'
    access: full
    locator: Abstract
  - ref: ARXIV-MINDGAP-2026
    title: 'Mind the Gap: Robustness Risks in PII Detection Systems'
    publisher: arXiv preprint
    type: academic
    url: https://arxiv.org/abs/2609.03464
    date: '2026-09-03'
    access: full
    locator: Abstract
  - ref: ARXIV-SURROGATESHIELD-2026
    title: 'SurrogateShield: Beyond Redaction for High-Utility, Privacy-Preserving LLM Interactions'
    publisher: arXiv preprint
    type: academic
    url: https://arxiv.org/abs/2606.29567
    date: '2026-06-28'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-17'
  notes: 'Idea: discussed in recent research, with benchmark measurements but no named production deployment found. Presidio-style redaction is long established; the idea here is LLM-based or hybrid detection. Figures are from authors'' own benchmarks.'
- id: security-data-privacy-17
  title: 'Idea: middleware that rewrites AI-agent tool calls to the minimum personal data the tool needs'
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - software-systems
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: LLM agents routinely put privacy-sensitive data into tool-call arguments beyond what the tool needs, sending it across trust boundaries to third-party services. Gating (allow or block) cannot rewrite argument values (ARXIV-TOOLMINIMIZE-2026).
  solution: ToolMinimize intercepts tool calls and rewrites arguments using removal, generalisation, substitution and truncation, guided by a schema-aware necessity analysis, with an optional LLM layer that strips irrelevant free-text content (ARXIV-TOOLMINIMIZE-2026).
  outcomes:
  - lever: risk
    description: Measured over-sharing by agents before any control
    figure: 81-88% of tool calls contained unnecessary sensitive data under default prompts; 36-76% still did with explicit privacy instructions
    measures: Share of tool calls that include unnecessary privacy-sensitive data, across three production LLMs (GPT-4o, Claude 3.5 Sonnet, Llama-3.3-70B), per the authors' controlled measurement.
    provenance: independent
    source_ref: ARXIV-TOOLMINIMIZE-2026
  - lever: risk
    description: Reduction in privacy cost with the middleware
    figure: 81.2-92.0% reduction at 100% argument-level task validity; median latency 1.77 ms
    measures: Authors' privacy-cost metric on 307 live tool calls across the three LLMs; 79.0% on 25 unannotated MCP schemas.
    provenance: independent
    source_ref: ARXIV-TOOLMINIMIZE-2026
  prerequisites:
  - Tool schemas with 'minimum necessary' metadata, or schema-aware necessity analysis
  - A proxy or middleware layer in front of agent tool calls
  risks_and_guardrails:
  - Detection tools miss implicit sensitive data (the paper's example is a hospital name implying a diagnosis) (ARXIV-TOOLMINIMIZE-2026)
  - Results are from the authors' own controlled tests, not a production deployment
  human_checkpoints:
  - Not specified in the paper.
  role_evolution: Not documented in these sources.
  evidence_grade: D
  sources:
  - ref: ARXIV-TOOLMINIMIZE-2026
    title: 'ToolMinimize: Auditing and Rewriting LLM Agent Tool Calls to Minimize Privacy Exposure'
    publisher: arXiv preprint
    type: academic
    url: https://arxiv.org/abs/2608.24957
    date: '2026-08-25'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-17'
  notes: 'Idea: a research prototype with measurements, no named deployment. The over-sharing measurement is the most useful independent number for sizing the exposure risk.'
- id: security-data-privacy-18
  title: 'Idea: natural-language policy files that let an LLM classify and block prompts before they reach coding agents'
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - transaction-processing
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Coding agents accept free-form prompts that may contain credentials, PII or proprietary data. Existing DLP relies on rigid regex, model fine-tuning or vendor-managed classifiers with limited customisability (ARXIV-POLICYGUARD-2026).
  solution: PolicyGuard intercepts prompts before the model and classifies them with an LLM guided by a plain-text policy file that non-engineers can edit without retraining (ARXIV-POLICYGUARD-2026).
  outcomes:
  - lever: quality
    description: Block rate and false positives on the authors' frozen test set
    figure: 96.5% effective block rate with 3.0% false-positive rate; 100% on a 217-prompt hidden holdout
    measures: Effective block rate and false-positive rate on a frozen test set of 927 prompts from a 2,000-prompt multilingual set; the same policy reached 86.4-96.5% across four different LLMs.
    provenance: independent
    source_ref: ARXIV-POLICYGUARD-2026
  prerequisites:
  - A written policy file describing what must not leave the organization
  - A pre-model interception point for prompts
  risks_and_guardrails:
  - Results are from the authors' own sealed evaluation, not a production deployment
  - Portability across models varied (86.4% to 96.5%)
  human_checkpoints:
  - Policy owners edit the policy file; blocking decisions are automated (ARXIV-POLICYGUARD-2026).
  role_evolution: Non-engineers can change DLP rules by editing a plain-text policy file (ARXIV-POLICYGUARD-2026).
  evidence_grade: D
  sources:
  - ref: ARXIV-POLICYGUARD-2026
    title: 'PolicyGuard: Prompt-Configurable Semantic DLP for LLM Coding Agents'
    publisher: arXiv preprint
    type: academic
    url: https://arxiv.org/abs/2608.02687
    date: '2026-08-03'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-17'
  notes: 'Idea: research prototype. Closely related vendor products (for example MIND''s ''DLP for Agentic AI'', announced 2026-01-28, MIND-AGENTICDLP-2026) were not found with published measurements.'
- id: security-data-privacy-19
  title: Agent access to certificate and cryptographic inventory through a governed interface
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - software-systems
  - data-reporting
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Certificate lifespans are stepping down toward 47 days by 2029, so manual certificate management does not scale (APPVIEWX-SUMMER-2026).
  solution: AppViewX's Summer 2026 release adds a native Model Context Protocol server that gives AI agents governed, structured access to certificate inventory and metadata. The company calls this a foundation for later AI-driven certificate lifecycle operations (APPVIEWX-SUMMER-2026).
  outcomes:
  - lever: speed
    description: Vendor describes AI-driven visibility into certificate inventory
    figure: none published
    measures: The initial release only exposes inventory and metadata to agents; it does not claim automated actions or results.
    provenance: vendor-published
    source_ref: APPVIEWX-SUMMER-2026
  prerequisites:
  - A certificate lifecycle management platform with up-to-date inventory
  - Policy-based renewal rules
  risks_and_guardrails:
  - The release preserves policy enforcement and governed access for agent clients (APPVIEWX-SUMMER-2026)
  - OWASP lists vector-store encryption and key-management alignment among AI data controls (OWASP-DATASEC-2026, p. 10)
  human_checkpoints:
  - Not specified; the release only exposes read access to inventory and metadata.
  role_evolution: Not documented in these sources.
  evidence_grade: C
  sources:
  - ref: APPVIEWX-SUMMER-2026
    title: 'Summer 2026 Product Release: Overview'
    publisher: AppViewX
    type: vendor
    url: https://www.appviewx.com/blogs/summer-2026-product-release/
    date: '2026-06-19'
    access: full
    locator: Key takeaways; 'Native MCP support for AI-driven certificate visibility'
  - ref: OWASP-DATASEC-2026
    title: OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0, 103-page PDF)
    publisher: OWASP GenAI Security Project
    type: standard-setter
    url: https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/
    date: '2026-03-17'
    access: full
    locator: p. 10 (vector store and embedding security posture)
  last_reviewed: '2026-10-17'
  notes: This is the only public AI-for-encryption or key-management item found; it is a vendor feature announcement with no customer. Search results for other vendors (cryptographic inventory, key lifecycle) were marketing pages and a patent filing and are not used.
- id: security-data-privacy-20
  title: Testing LLM-generated differentially private synthetic data against direct synthesis (financial transactions)
  archetype: security
  module: data-privacy
  function: risk-compliance-legal
  work_types:
  - data-reporting
  - research-synthesis
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: Differentially private synthetic data is hard for high-dimensional tabular data, so teams ask whether LLM simulators could help (PEPR-2026, Capital One session, Tuesday 10:00).
  solution: Capital One researchers condensed customer attributes into compact user profiles under differential privacy, seeded an LLM-based generator (PersonaLedger) to produce transactions, and compared the result with direct DP synthesis on the same financial data (PEPR-2026).
  outcomes:
  - lever: quality
    description: LLM-based approach versus direct DP synthesis
    figure: Direct DP synthesis 'significantly' outperformed the LLM approach on fraud-detection utility and distributional fidelity; no figures in the abstract
    measures: Qualitative comparison on fraud-detection utility and distributional fidelity for one financial transaction dataset; systematic LLM bias, not DP noise, was the dominant error source.
    provenance: self-reported
    source_ref: PEPR-2026
  prerequisites:
  - A DP profile-generation step
  - A rigorous fidelity evaluation before any production use
  risks_and_guardrails:
  - The model's learned priors about 'typical' financial behaviour overrode the statistical distributions supplied as input, especially for demographic and categorical features (PEPR-2026)
  - The speakers advise rigorous fidelity evaluation before deploying LLM-generated synthetic data in production pipelines (PEPR-2026)
  human_checkpoints:
  - Privacy engineers evaluate fidelity and utility before use (PEPR-2026).
  role_evolution: Not documented in these sources.
  evidence_grade: B
  sources:
  - ref: PEPR-2026
    title: PEPR '26 program (USENIX Conference on Privacy Engineering Practice and Respect, 1-2 June 2026, Santa Clara)
    publisher: USENIX
    type: conference
    url: https://www.usenix.org/conference/pepr26/program
    date: '2026-06-01'
    access: full
    locator: 'Tuesday 10:00 am ''Profile-Then-Simulate: Can LLMs Faithfully Generate Differentially Private Synthetic Data?'''
  last_reviewed: '2026-10-17'
  notes: Included as a named-organization negative result; no production deployment is claimed. Abstract-level evidence only.
- id: security-data-privacy-21
  title: 'Privacy-preserving analytics on AI chatbot use: LLMs interpret unstructured data inside secure enclaves and release only differentially private aggregates'
  archetype: security
  module: data-privacy
  function: technology-it
  work_types:
  - data-reporting
  - research-synthesis
  pattern: other
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Understanding real-world generative AI usage is needed to improve products, but conventional analytics risks exposing sensitive input data (PEPR-2026, Google session, Tuesday 9:00).
  solution: Google's 'Provably Private Insights' framework combines trusted execution environments (for external transparency and verifiability), 'Data Expert' LLMs that interpret unstructured data inside the enclave, and differential privacy for aggregation. The speakers describe the open-sourced architecture and its real-world use in the Recorder app (PEPR-2026).
  outcomes:
  - lever: risk
    description: Provably private standard for server-side processing
    figure: none published
    measures: The abstract describes a design and a real-world application, with no measured utility or privacy-loss figures.
    provenance: self-reported
    source_ref: PEPR-2026
  prerequisites:
  - Trusted execution environments and remote attestation
  - A differential privacy budget and aggregation design
  risks_and_guardrails:
  - Server-side processing is limited to privacy-preserving computations by design (PEPR-2026)
  human_checkpoints:
  - Not specified in the abstract.
  role_evolution: Not documented in these sources.
  evidence_grade: B
  sources:
  - ref: PEPR-2026
    title: PEPR '26 program (USENIX Conference on Privacy Engineering Practice and Respect, 1-2 June 2026, Santa Clara)
    publisher: USENIX
    type: conference
    url: https://www.usenix.org/conference/pepr26/program
    date: '2026-06-01'
    access: full
    locator: Tuesday 9:00 am 'Toward Provably Private Insights into AI Use'
  last_reviewed: '2026-10-17'
  notes: Named deployment in a consumer app described in a conference abstract; deployment scale is not stated.
```

## 3. Module notes

### Processes and key steps (with work types)

- **Discover and inventory data** (`data-reporting`): scan cloud, SaaS, file shares and catalogs; for AI, also inventory prompts, RAG sources, vector stores, tool integrations and logs (OWASP-DATASEC-2026, p. 9).
- **Classify and label** (`transaction-processing`, `review-assurance`): assign sensitivity tags and labels; stewards adjudicate edge cases; labels must propagate to embeddings, caches and backups (OWASP-DATASEC-2026, p. 9, 42-43; ARXIV-GLYPH-2026).
- **Prevent and detect data loss** (`software-systems` for policy design; `transaction-processing` for alert triage; `expert-judgment` for investigation): DLP policies on email, endpoints, cloud and AI tools; triage and tune alerts (MSFT-PURVIEWAGENTS-2026; CSA-AI-2026).
- **Govern access and entitlements** (`review-assurance`): find overshared content, right-size permissions, control what AI assistants can retrieve (MSFT-SPRCD-2026; MSFT-PURVIEWAI-2026).
- **Encrypt and manage keys and certificates** (`software-systems`): inventory, rotate and renew; certificate lifespans are shortening (APPVIEWX-SUMMER-2026).
- **Privacy engineering** (`document-production`, `software-systems`, `review-assurance`): privacy impact assessments, data mapping and lineage, retention and deletion, purpose-limitation controls, privacy review of code (PEPR-2026; ONETRUST-W26-2026).
- **Control AI-specific exposure** (`monitor-diagnose-act`): shadow AI discovery, prompt and paste controls, RAG access control, agent tool-call data minimisation (NETSKOPE-CTR-2026; OWASP-DATASEC-2026, p. 24-26; ARXIV-TOOLMINIMIZE-2026).

### Common pain points

- DLP often detects loss after the fact; among respondents who lost data, 16% said DLP blocked their most significant incident (CSA-AI-2026).
- Alert noise and false positives: OpenWeb said it could not trust legacy DLP alerts (MIND-OPENWEB-2026); the CSA report examines how alert fatigue affects analyst workload and retention (CSA-AI-2026).
- Classification does not scale by hand: one catalog of about 3.4M columns would take about 30 person-years at one column a minute, per the authors' estimate (ARXIV-GLYPH-2026, Section 1); the same field name can be personal data or a cache TTL (META-ENG-ASSETCLASS-2026).
- Derived data outlives the source: embeddings and backups can keep a deleted person's data alive and re-expose it on re-indexing (OWASP-DATASEC-2026, DSGAI07, p. 42-43).
- Poor visibility into GenAI use: only 29% could routinely produce a 30-day report of sensitive data sent to GenAI tools (CSA-AI-2026); Netskope says 50% of organizations lack enforceable genAI data protection policies (NETSKOPE-CTR-2026).
- Policy and practice diverge: in a study of three German organizations (17 interviews), regulatory pressure was often turned into policies without regard to actual tool use, and data privacy, validation effort and weak governance were barriers to GenAI adoption (ARXIV-GENAIAGILE-2026).
- Manual privacy assessments and reassessments cause 'assessment fatigue' (ONETRUST-W26-2026).

### Metrics and benchmarks (with sources)

| Measure | Value and what it counts | Source | Provenance |
|---|---|---|---|
| DLP prevention | 16% of respondents who experienced data loss said DLP blocked their most significant incident before data left (survey of 433 IT and security professionals) | CSA-AI-2026 | independent (practitioner survey) |
| GenAI visibility | 29% of respondents could routinely produce a 30-day report of sensitive data sent to GenAI tools | CSA-AI-2026 | independent (practitioner survey) |
| GenAI data policy violations | Average organization: 3% of genAI users committing about 223 violations a month; violations roughly doubled in a year; 50% of organizations lack enforceable genAI data protection policies | NETSKOPE-CTR-2026 | vendor-published telemetry |
| Sensitive content in AI use | 39.7% of data movements into AI tools involve sensitive data; 32.3% of ChatGPT use via personal accounts | CYBERHAVEN-AIRISK-2026 | vendor-published telemetry |
| Exposure to AI | 99% of 1,000 analysed environments had sensitive data exposed that AI can easily surface; about 1 in 10 companies had labelled files | VARONIS-SODS-2025 | vendor-published telemetry |
| Steward acceptance | 63.3% to 99.8% over six weeks, about 24,000 adjudicated column-tag pairs (precision-like; blind to false negatives) | ARXIV-GLYPH-2026 | self-reported |
| Tagging quality | Overall F2 0.890 (fusion), 0.880 (metadata tagger alone), 0.050 (regex alone), 4 evaluation files | ARXIV-GLYPH-2026 | self-reported |
| Rule versus LLM routing | About 85% of classification requests by rules, about 15% by LLM fallback at roughly 400x compute | META-ENG-ASSETCLASS-2026 | self-reported |
| Privacy code detection | RAG found more than 2x the confirmed issues of a standalone LLM over 183,000+ methods; false positives not significantly improved | PEPR-2026 | self-reported |
| PII detector robustness | Presidio recall 0.07 on HIGH-sensitivity categories (REDACT); no detector gets full cross-turn coverage without false positives (PII-TRACE, 11 baselines) | ARXIV-REDACT-2026; ARXIV-PIITRACE-2026 | independent (academic) |
| Agent over-sharing | 81-88% of tool calls include unnecessary sensitive data under default prompts; 36-76% with explicit privacy instructions | ARXIV-TOOLMINIMIZE-2026 | independent (academic) |
| Policy-as-prompt DLP | 96.5% effective block rate, 3.0% false positives on a 927-prompt frozen test set | ARXIV-POLICYGUARD-2026 | independent (academic, authors' own test) |
| Breach cost context | Global average breach cost US$4.99M (up 12%); US$1.93M lower with extensive security AI and automation | IBM-CODB-2026 | vendor-published (landing page only; report body not read) |

No override rate, acceptance rate for DLP triage, or independent parallel-run result was found for LLM-based DLP or alert triage. The closest are the Apple-affiliated steward acceptance rate and Meta's routing split, both self-reported.

### Guardrails and regulatory points

- **GDPR and AI models.** The EDPB's Opinion 28/2024 says an AI model trained on personal data is not automatically anonymous; anonymity is assessed case by case and needs insignificant likelihood of extracting personal data directly or through queries. It also sets out the three-step legitimate-interest test for developing and deploying AI models (EDPB-OPINION2824-2024, summary pages 2-3).
- **Legislative flux.** The Commission's 19 November 2025 Digital Omnibus proposal would add a legitimate-interest basis for AI training (Article 88c). A law-firm analysis dated 2026-06-18 says a Council compromise text of 10 June 2026 would drop Article 88c in favour of a recital, and that mediation had made no decisive progress (NOERR-OMNIBUS-2026). The final outcome was not confirmed.
- **EU AI Act.** Applicable since 2026-08-02, with Annex III high-risk obligations moved to 2027-12-02 by the AI Omnibus (in force 2026-07-27) (EC-AIACT-2026).
- **NIST.** AI 600-1 lists data privacy as a generative AI risk, including memorisation, leakage and inference of sensitive information (NIST-AI600-2024, section 2.4). The Privacy Framework 1.1 initial public draft was released 2025-04-14 and comments closed 2025-06-13; the final version was still marked 'coming soon' on a page updated 2026-04-01 (NIST-PF-2026).
- **OWASP.** The GenAI data security guide (v1.0, March 2026) catalogues 21 data risks, including shadow AI, classification and lifecycle gaps, vector-store security and over-broad context windows, with tiered mitigations (OWASP-DATASEC-2026).
- **US state oversight.** A law-firm recap of the 2026 IAPP Global Privacy Summit reports California regulators moving toward audit-style oversight, which makes proactive auditing important (PERKINSCOIE-IAPPGPS-2026).
- **Vendor-side limits.** The Purview DLP triage agent skips simulation-mode policies, files above 2 MB and non-content conditions (MSFT-PURVIEWAGENTS-2026). SharePoint Restricted Content Discovery does not change permissions and is described as temporary (MSFT-SPRCD-2026).

### Frontier signals (dated, sourced)

| Date | Signal | Source |
|---|---|---|
| 2025-11-17 | Gartner abstract (seen in search only) says conventional DLP cannot manage GenAI data loss risks and recommends adaptive, risk-based DLP integrated with SSE and DSPM; the full text is paywalled | GARTNER-DLP-2025 |
| 2026-01-28 | MIND announces 'DLP for Agentic AI' (agent discovery, risky-access detection, remediation) | MIND-AGENTICDLP-2026 |
| 2026-03 | OWASP publishes the GenAI Data Security Risks and Mitigations guide v1.0 | OWASP-DATASEC-2026 |
| 2026-04-23 | Black Hat Asia privacy keynote asks which privacy tools give real agency and which are 'privacy theater' | BLACKHAT-ASIAPR-2026 |
| 2026-05-14 / 2026-07-02 | Akamai announces, then completes, the LayerX acquisition (about US$205 million; browser security and AI usage control) | AKAMAI-LAYERX-2026 |
| 2026-06-01/02 | PEPR 2026 has LLM-for-privacy-engineering sessions from Meta, Microsoft, CMU and others, with honest accounts of limits | PEPR-2026 |
| 2026-06-10 | Cyera announces a US$600 million Series G at a US$12 billion valuation | CYERA-SERIESG-2026 |
| 2026-06-25 | Meta describes shrinking the LLM's role by distilling findings into deterministic rules | META-ENG-ASSETCLASS-2026 |
| 2026-08-17 | Microsoft moves general availability of DLP triage-agent summaries in Defender XDR from August 2026 to August 2027 | MSFT-MC1255406-2026 |
| 2026-08-28 | Google opens Gemini-based Drive classification (instruction-driven) in beta | GOOGLE-WSAICLASS-2026 |
| 2026-10-09 | CSA publishes the DLP-in-the-AI-era survey | CSA-AI-2026 |
| 2026-10-15 | Proofpoint to acquire Varonis for about US$6.3 billion; close expected first half of 2027 | VARONIS-PROOFPOINT-2026 |

### Workforce and role effects

- Stewards move from authoring tags to adjudicating model suggestions that then retrain the model (ARXIV-GLYPH-2026, Section 5.2); at Meta, people adjudicate reference labels and approve rule promotions (META-ENG-ASSETCLASS-2026).
- Admins write natural-language classification instructions rather than curate training files (GOOGLE-WSAICLASS-2026), and approve or tune agent-proposed fixes (MSFT-DSPM-2026).
- Dedicated privacy engineering roles are being created: Anthropic describes the role as one of its first dedicated privacy engineers, building automated data discovery, classification, lineage and compliance controls (ANTHROPIC-JOB-PRIVACYENG-2026). Coinbase's privacy incident analyst role asks for automation work and the responsible use of generative AI with human oversight (COINBASE-JOB-PRIVACYANALYST-2026). Datadog hires a product manager for AI and data security (DATADOG-JOB-AIDATASEC-2026).
- Vendors claim smaller teams can run discovery and clean-up at scale (CYERA-VETCOR-2026); no staffing data is published.
- Non-experts may prepare first-draft privacy assessments while experts focus on product-specific decisions (PEPR-2026, Privy session).

### Objections and concerns practitioners raise

- LLM output is not reproducible, so enforcement should run on replayable rules and LLM output should be treated as a recommendation, not truth (META-ENG-ASSETCLASS-2026).
- Aggregate accuracy hides failures on rare, high-stakes classes and under input shift (ARXIV-REDACT-2026; ARXIV-MINDGAP-2026; META-ENG-ASSETCLASS-2026).
- Acceptance rates can mislead: Apple-affiliated authors note that steward acceptance cannot see false negatives (ARXIV-GLYPH-2026).
- LLM-generated synthetic data inherits model bias (PEPR-2026, Capital One session).
- Retrieval-augmented privacy detection did not cut false positives (PEPR-2026, Microsoft session).
- Context windows have no internal access control, so mitigations only work around the limit (OWASP-DATASEC-2026, p. 6-7).
- Privacy tools may be 'privacy theater' if they give no real agency (BLACKHAT-ASIAPR-2026).
- Policy-only rules for AI use do not work, according to one practitioner comment (HN-ASKLLMAPI-2026); the thread had two comments in total.
- Product dependence: Microsoft's own triage agent has documented size, scope and condition limits, and its Defender XDR general availability slipped by a year (MSFT-PURVIEWAGENTS-2026; MSFT-MC1255406-2026).

### Interview probes for an advisor

1. Which data stores feed your AI assistants, RAG indexes or agents, and can you show that labels and entitlements follow the data into embeddings, caches and backups? What happens to those copies when a record is erased?
2. When did DLP last block a real incident before data left? Roughly how many alerts do you get a week, how many are investigated, and who tunes the rules? Do you measure what DLP misses?
3. Can you produce a 30-day report of sensitive data sent to GenAI tools, split by managed and personal accounts? Who owns the shadow-AI decision (security, procurement, privacy)?
4. If a model or agent proposes sensitivity tags, who adjudicates them, and do you track missed (false-negative) classifications as well as acceptance? What would make you move from review to automation?
5. In privacy engineering, where do assessments (PIAs, DPIAs, reassessments) and privacy code review spend their time today, and which part could a first draft safely cover with a reviewer signing off?

## 4. Routed to other modules

- **ai-security (agent identity and containment).** OWASP DSGAI02 and the just-in-time data access pattern, where an agent gets a short-lived per-task credential instead of standing database access (OWASP-DATASEC-2026, p. 10). Also MIND's agent discovery and risky-access detection (MIND-AGENTICDLP-2026) and OneTrust's agent detection for AWS Bedrock, Azure Foundry and Google Vertex (ONETRUST-W26-2026).
- **ai-security (confidential AI processing).** Google's Private AI Compute, which processes data in a hardware-sealed, attested cloud environment so that data is not accessible even to Google (announced 2025-11-11) (GOOGLE-PRIVATEAI-2025).
- **human-risk.** The Purview Insider Risk Management triage agent (MSFT-PURVIEWAGENTS-2026), and Netskope's finding that 60% of insider threat incidents involve personal cloud app instances (NETSKOPE-CTR-2026).
- **governance-risk.** Anthropic's hiring for agent-security policy and compliance (policies and standards for how agents are built and operated, access reviews, handling of regulated data) (ANTHROPIC-JOB-AGENTSEC-2026); EU AI Act and Digital Omnibus obligations and timing (EC-AIACT-2026; NOERR-OMNIBUS-2026); NIST AI 600-1 (NIST-AI600-2024).
- **incident-response.** Privacy incident triage, severity classification and escalation as a defined role at Coinbase (COINBASE-JOB-PRIVACYANALYST-2026); breach-cost context (IBM-CODB-2026).
- **application-security.** The pull-request privacy-pattern detection in use case 14 sits on the boundary with code review (PEPR-2026).

## 5. Sources

Date rules: where a page showed no publication date the retrieval date (2026-10-17) is given and the title says so. `access: full` means the page or document was opened and read; `search-only` means seen only in search results.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| `ARXIV-ARBITER-2025` | ARBITER: AI-Driven Filtering for Role-Based Access Control | arXiv preprint | academic | https://arxiv.org/abs/2512.20535 | 2025-12-23 | full |
| `ARXIV-DPIALLM-2026` | From Regulation to Implementation: A Critical Evaluation of LLM-Assisted Regulatory Compliance in Industry | arXiv preprint | academic | https://arxiv.org/abs/2608.21317 | 2026-08-21 | full |
| `ARXIV-GENAIAGILE-2026` | Between Policy and Practice: GenAI Adoption in Agile Software Development Teams | arXiv preprint | academic | https://arxiv.org/abs/2601.07051 | 2026-01-11 | full |
| `ARXIV-GLYPH-2026` | Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology Tagging of Enterprise Data Catalogs (Kudriavtsev, Rafi, Sundaram; Apple affiliation) | arXiv preprint | academic | https://arxiv.org/abs/2609.10430 | 2026-09-09 | full |
| `ARXIV-MINDGAP-2026` | Mind the Gap: Robustness Risks in PII Detection Systems | arXiv preprint | academic | https://arxiv.org/abs/2609.03464 | 2026-09-03 | full |
| `ARXIV-PIABENCH-2026` | PIA-Bench: Towards Automated Privacy Impact Assessment with Large Language Models | arXiv preprint | academic | https://arxiv.org/abs/2609.12571 | 2026-09-11 | full |
| `ARXIV-PIITRACE-2026` | PII-TRACE: A Benchmark for Context-Aware PII Detection in Multi-Turn LLM Conversations | arXiv preprint | academic | https://arxiv.org/abs/2609.22200 | 2026-08-31 | full |
| `ARXIV-POLICYGUARD-2026` | PolicyGuard: Prompt-Configurable Semantic DLP for LLM Coding Agents | arXiv preprint | academic | https://arxiv.org/abs/2608.02687 | 2026-08-03 | full |
| `ARXIV-REDACT-2026` | REDACT: A Systematically Controlled Multilingual Benchmark for Personal Information Detection | arXiv preprint | academic | https://arxiv.org/abs/2606.19881 | 2026-06-18 | full |
| `ARXIV-SURROGATESHIELD-2026` | SurrogateShield: Beyond Redaction for High-Utility, Privacy-Preserving LLM Interactions | arXiv preprint | academic | https://arxiv.org/abs/2606.29567 | 2026-06-28 | full |
| `ARXIV-TOOLMINIMIZE-2026` | ToolMinimize: Auditing and Rewriting LLM Agent Tool Calls to Minimize Privacy Exposure | arXiv preprint | academic | https://arxiv.org/abs/2608.24957 | 2026-08-25 | full |
| `HN-ASKLLMAPI-2026` | Ask HN: Are companies preventing sensitive data from being sent to external LLM APIs (thread of 2 comments; comment 47265310) | Hacker News | community | https://news.ycombinator.com/item?id=47259975 | 2026-03-05 | full |
| `BLACKHAT-ASIAPR-2026` | Black Hat Asia 2026 Unveils Key Insights on AI Security and Cloud Infrastructure (post-event press release, read via text mirror) | Black Hat (Informa) | conference | https://blackhat.com/html/press/2026-04-29.html | 2026-04-29 | full |
| `PEPR-2026` | PEPR '26 program (USENIX Conference on Privacy Engineering Practice and Respect, 1-2 June 2026, Santa Clara) | USENIX | conference | https://www.usenix.org/conference/pepr26/program | 2026-06-01 | full |
| `GARTNER-DLP-2025` | Gartner Insights Abstract, document 7192130 (conventional DLP and GenAI data loss; seen only in search results, page blocked) | Gartner | firm | https://www.gartner.com/en/documents/7192130 | 2025-11-17 | search-only |
| `META-ENG-ASSETCLASS-2026` | Privacy-Aware Infrastructure in the AI-Native Era: An Asset Classification Case Study | Engineering at Meta (Meta Platforms) | firm | https://engineering.fb.com/2026/06/25/security/privacy-aware-infrastructure-in-the-ai-native-era-an-asset-classification-case-study/ | 2026-06-25 | full |
| `NOERR-OMNIBUS-2026` | Digital Omnibus AI is nearing the finish line: is EU data law heading down the wrong track? | Noerr (law firm) | firm | https://www.noerr.com/en/insights/digital-omnibus-ai-is-nearing-the-finish-line-is-eu-data-law-heading-down-the-wrong-track | 2026-06-18 | full |
| `PERKINSCOIE-IAPPGPS-2026` | Where Privacy Is Headed Next: Key Takeaways From the 2026 IAPP Global Privacy Summit | Perkins Coie (now Ashurst Perkins Coie), law firm | firm | https://www.ashurstperkinscoie.com/en/insights/where-privacy-is-headed-next-key-takeaways-from-the-2026-iapp-global-privacy-summit/ | 2026-04-17 | full |
| `ANTHROPIC-JOB-AGENTSEC-2026` | Security Risk & Compliance, Agent Security (job posting; first published 2026-10-05) | Anthropic | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/5443871008 | 2026-10-05 | full |
| `ANTHROPIC-JOB-PRIVACYENG-2026` | Staff+ Software Engineer, Privacy (job posting; first published 2026-08-07, updated 2026-09-21) | Anthropic | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/5383114008 | 2026-08-07 | full |
| `COINBASE-JOB-PRIVACYANALYST-2026` | Analyst, Privacy (Incident Management) (job posting; first published 2026-09-01) | Coinbase | job-posting | https://www.coinbase.com/careers/positions/8168175?gh_jid=8168175 | 2026-09-01 | full |
| `DATADOG-JOB-AIDATASEC-2026` | Product Manager II, AI & Data Security (job posting; first published 2026-06-04) | Datadog | job-posting | https://careers.datadoghq.com/detail/7982288/?gh_jid=7982288 | 2026-06-04 | full |
| `RISKYBIZ-2026` | Risky Business podcast feed (episode titles scanned, 100 most recent episodes, 2025-04-09 to 2026-10-14) | Risky Business Media | podcast | https://risky.biz/feeds/risky-business/ | 2026-10-14 | full |
| `CYERA-SERIESG-2026` | Cyera Raises $600 Million Series G At $12 Billion Valuation To Expand Enterprise AI Trust Layer (trade-press report of a company announcement) | Pulse 2.0 | press | https://pulse2.com/cyera-raises-300-million-at-12-billion-valuation-in-rapid-ascent-to-top-of-data-security-market/ | 2026-06-10 | full |
| `EC-AIACT-2026` | AI Act: regulatory framework for AI (status page, checked 2026-10-17; the page carries no publication date) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-17 | full |
| `EDPB-OPINION2824-2024` | Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models | European Data Protection Board | regulator | https://www.edpb.europa.eu/system/files/documents/2024-12/edpb_opinion_202428_ai-models_en.pdf | 2024-12-17 | full |
| `NIST-AI600-2024` | NIST AI 600-1, Artificial Intelligence Risk Management Framework: Generative AI Profile | NIST | standard-setter | https://doi.org/10.6028/NIST.AI.600-1 | 2024-07 | full |
| `NIST-PF-2026` | NIST Privacy Framework 1.1 page (initial public draft released 2025-04-14; page last updated 2026-04-01) | NIST | standard-setter | https://www.nist.gov/privacy-framework/privacy-framework-version-11 | 2026-04-01 | full |
| `OWASP-DATASEC-2026` | OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0, 103-page PDF) | OWASP GenAI Security Project | standard-setter | https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/ | 2026-03-17 | full |
| `CSA-AI-2026` | DLP in the AI Era: Data Loss Prevention Survey Report (landing page and abstract; report body is login-gated and was not read) | Cloud Security Alliance | survey | https://cloudsecurityalliance.org/artifacts/dlp-in-the-ai-era-survey-report | 2026-10-09 | full |
| `IBM-CODB-2026` | Cost of a Data Breach Report 2026 (landing page; date is the page's dateModified, report release date not shown) | IBM / Ponemon Institute | survey | https://www.ibm.com/reports/data-breach | 2026-09-16 | full |
| `AKAMAI-LAYERX-2026` | Akamai Completes Acquisition of Secure Enterprise Browser Provider LayerX | Akamai | vendor | https://www.akamai.com/newsroom/press-release/akamai-completes-acquisition-of-secure-enterprise-browser-provider-layerx | 2026-07-02 | full |
| `APPVIEWX-SUMMER-2026` | Summer 2026 Product Release: Overview | AppViewX | vendor | https://www.appviewx.com/blogs/summer-2026-product-release/ | 2026-06-19 | full |
| `CYBERHAVEN-AIRISK-2026` | 2026 AI Adoption & Risk Report: Data Governance Gaps Widening (press release) | Cyberhaven | vendor | https://www.cyberhaven.com/press-releases/cyberhaven-2026-ai-adoption-risk-report | 2026-02-05 | full |
| `CYERA-CHENMED-2026` | ChenMed Achieves Data Security Excellence with Cyera, Remediating Over 32,000 Issues (customer story; page shows no publication date, date given is retrieval date) | Cyera | vendor | https://www.cyera.com/customer-story/chenmed-achieves-data-security-excellence-with-cyera | 2026-10-17 | full |
| `CYERA-FI-2026` | Turning Data Noise into Actionable Security: Lessons from a Leading Financial Institution (customer story, institution unnamed; no publication date shown, date given is retrieval date) | Cyera | vendor | https://www.cyera.com/customer-story/lessons-from-a-leading-financial-institution | 2026-10-17 | full |
| `CYERA-PARAMOUNT-2026` | Paramount Gains Full Data Visibility with Cyera, Identifying Billions of Sensitive Records (customer story; no publication date shown, date given is retrieval date) | Cyera | vendor | https://www.cyera.com/customer-story/paramount-gains-full-data-visibility-with-cyera-identifying-billions-of-sensitive-records | 2026-10-17 | full |
| `CYERA-VETCOR-2026` | Vetcor Achieves Rapid Data Visibility and Protection with Cyera (customer story; no publication date shown, date given is retrieval date) | Cyera | vendor | https://www.cyera.com/customer-story/vetcor-achieves-rapid-data-visibility-and-protection-with-cyera | 2026-10-17 | full |
| `GOOGLE-PRIVATEAI-2025` | Private AI Compute: our next step in building private and helpful AI | Google | vendor | https://blog.google/technology/ai/google-private-ai-compute/ | 2025-11-11 | full |
| `GOOGLE-WSAICLASS-2026` | Gemini-based data classification in Google Drive is now available in open beta | Google Workspace Updates blog | vendor | https://workspaceupdates.googleblog.com/2026/08/gemini-based-data-classification-in-Google-Drive-is-now-available-in-open-beta.html | 2026-08-28 | full |
| `GOOGLE-WSAISEC-2024` | Introducing a new AI Security add-on for Google Workspace | Google Workspace Updates blog | vendor | https://workspaceupdates.googleblog.com/2024/04/ai-security-add-on-google-workspace.html | 2024-04-09 | full |
| `MIND-AGENTICDLP-2026` | MIND Announces Autonomous DLP for Agentic AI, Bringing a Data-Centric Approach to AI Security | MIND | vendor | https://mind.io/newsroom/mind-announces-autonomous-dlp-for-agentic-ai | 2026-01-28 | full |
| `MIND-OPENWEB-2026` | OpenWeb uses MIND to modernize and automate data loss prevention (customer story; no publication date shown, date given is retrieval date) | MIND | vendor | https://mind.io/customers/openweb | 2026-10-17 | full |
| `MSFT-DSPM-2026` | Learn about Microsoft Purview Data Security Posture Management (DSPM) | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about | 2026-05-01 | full |
| `MSFT-MC1255406-2026` | MC1255406 Microsoft Purview / Data Security Triage Agent Summaries for DLP Alerts in Microsoft Defender XDR (Message Center archive; published 2026-03-18, updated 2026-08-17) | Microsoft 365 Message Center (archive at mc.merill.net) | vendor | https://mc.merill.net/message/MC1255406 | 2026-03-18 | full |
| `MSFT-PURVIEWAGENTS-2026` | Security Copilot Agents in Microsoft Purview overview | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview | 2026-03-23 | full |
| `MSFT-PURVIEWAI-2026` | Microsoft Purview data security and compliance protections for Microsoft 365 Copilot and other generative AI apps | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/purview/ai-microsoft-purview | 2026-05-27 | full |
| `MSFT-PURVIEWDLPTRIAGE-2026` | Get started with the Microsoft Purview Triage Agent in Data Loss Prevention | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started | 2026-06-25 | full |
| `MSFT-SPRCD-2026` | Restrict discovery of SharePoint sites and content | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery | 2026-10-11 | full |
| `NETSKOPE-CTR-2026` | Cloud and Threat Report: 2026 | Netskope | vendor | https://www.netskope.com/blog/cloud-and-threat-report-2026 | 2026-01-05 | full |
| `ONETRUST-W26-2026` | Evolving Privacy Programs with AI: What's New in the OneTrust Winter '26 Release (date from page metadata; a search snippet dated the release to March 2026) | OneTrust | vendor | https://www.onetrust.com/blog/evolving-privacy-programs-with-ai-whats-new-in-the-onetrust-winter-26-release/ | 2026-06-10 | full |
| `VARONIS-PROOFPOINT-2026` | Proofpoint to Acquire Varonis in a $6.3 Billion Transaction (joint press release) | Varonis / Proofpoint | vendor | https://www.varonis.com/announcement | 2026-10-15 | full |
| `VARONIS-SODS-2025` | Data Security Report Reveals 99% of Orgs Have Sensitive Information Exposed to AI (2025 State of Data Security Report summary) | Varonis | vendor | https://www.varonis.com/blog/state-of-data-security-report | 2025-05-20 | full |

## 6. Gaps

- **Independent quality evidence.** No override, false-positive, miss or parallel-run result was found for LLM-based DLP, alert triage, classification (beyond self-reported figures from two engineering teams) or privacy assessments in production. Almost every performance figure is self-reported or vendor-published.
- **Gated or blocked reports.** The CSA DLP report body is login-gated (only the abstract was read). IBM Cost of a Data Breach 2026 was read as a landing page only; the report body and release date were not found. Microsoft Data Security Index, Cisco Data Privacy Benchmark and Gartner pages returned 403 or were behind verification; the Gartner abstract is search-only. The IAPP site, IAPP-EY governance surveys and ISACA material were not read, so professional-body guidance is absent from this note.
- **Undated vendor pages.** Cyera and MIND customer stories show no publication dates; the date given is the retrieval date (2026-10-17). Treat them as undated.
- **Conference depth.** PEPR 2026 was read from the program abstracts only; slides, papers and videos were not opened. The Black Hat Asia privacy keynote was read from the organiser's press release, not from the planned Computer Weekly coverage, which was not reachable. No RSAC 2026 or Gartner Security and Risk Summit data-security session lists were read.
- **Practitioner discourse is very thin.** A scan of 100 recent Risky Business episode titles found none on data discovery, DLP or privacy engineering; Hacker News had one relevant two-comment thread and several low-engagement 'Show HN' posts; Reddit, LinkedIn and Cloud Security Podcast episode content were not reached. This may reflect the access routes rather than the field.
- **Encryption and key management.** Only one vendor feature announcement (AppViewX) was found. No deployment, customer, or measurement. Post-quantum migration is outside this module's AI lens and was not pursued.
- **Data access governance with AI.** No named-customer outcome for oversharing remediation or access-review automation was found.
- **DSAR, retention and deletion automation.** No public deployment with results was found for AI in data-subject-request handling; a search snippet about OneTrust agents reducing assessments 'from weeks to minutes' was not opened and is not used.
- **Regulatory status.** The final shape of the EU Digital Omnibus on data (Article 88c and the personal-data definition) is unresolved in the sources found, and search results disagreed on procedural status. The CNIL, ICO and national DPA positions on AI and data security were not read beyond the ICO landing page.
- **Corporate details.** Cyera's acquisitions and the reported Oasis deal were seen only in search results and an aggregator; they are not used as facts. Gartner and Forrester views are paywalled.
- **Non-English and non-EU/US sources** (APAC, Middle East regulators, sector regulators such as banking and health supervisors) were not covered.

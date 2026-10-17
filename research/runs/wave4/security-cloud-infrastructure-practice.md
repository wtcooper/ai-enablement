# Cloud and infrastructure security: practice deep dive

Archetype: security. Module: cloud-infrastructure. Angle: practice. Compiled 2026-10-17. Working files were kept in a private `mktemp -d` folder. Web search was used 8 times (customer outcomes for Wiz and Palo Alto Cortex Cloud, Google and Microsoft posture agents, SentinelOne, AI firewall policy, in-house cloud-triage write-ups); most evidence came from direct fetches of vendor blogs, customer-story pages, product documentation, Greenhouse job boards and the fwd:cloudsec schedule data.

## 1. Summary

- **The pattern that is real.** Cloud security platforms now ship role-split agent sets: attacker-side (Wiz Red Agent, Orca Red Pod), investigator (Wiz Blue Agent, Orca Blue Pod) and fixer (Wiz Green Agent, Orca Green Pod). Microsoft's Posture Prioritization Agent is in limited public preview and AWS's own benchmark post cites Microsoft's Project Perception as red/blue/green multi-agent defense (`WIZ-OPMODEL-2026`, `ORCA-AGENTPODS-2026`, `MSFT-LEARN-PPA-2026`, `AWS-DECEPTION-2026`).
- **Best evidence: investigation of cloud detections.** ZS Associates ran Wiz's Blue Agent in parallel with analysts for three months, reports a self-validated accuracy of about 95% ("around 95.17%" in the director's words), and now lets the agent close a defined set of low-severity cloud detections with an end-of-shift human review (`WIZ-ZS-2026`). Owkin reports a 75% cut in false-positive investigation time (vendor-published headline) (`WIZ-OWKIN-2026`). Both are hosted on the vendor's site; no independent measurement of any cloud-security agent was found.
- **Remediation is the bottleneck, so vendors pitch the fixer.** project44 reports 10x faster vulnerability remediation with Red and Green Agents plus Wiz Code, with no metric definition (`WIZ-PROJECT44-2026`). Tamnoon, a remediation vendor, says critical alerts stay unresolved for 150 days (`TAMNOON-CORTEX-2026`). AWS published a pattern that turns IAM Access Analyzer findings into reviewable IaC pull requests (`AWS-LEASTPRIV-2026`).
- **Practitioners are building their own, and report what broke.** WRITER's Cerebro starts from a 2% actionable-alert rate and requires evidence before any decision (`WRITER-CEREBRO-2026`). A security lead running a read-only Kubernetes triage agent for over a year reports four failures, all under a "read-only" label (`FWDCLOUDSEC-RAJI-2026`).
- **Network and endpoint evidence is thinnest.** Firewall policy hygiene agents (Cato, Check Point) and Palo Alto Networks' virtual patching are documentation or announcements with no named-customer results. Endpoint evidence is CrowdStrike's offline triage model (82.6% test accuracy) (`ARXIV-2607.28460`).
- **Quality limits are documented.** Independent triage benchmark: every tested approach missed at least 40.4% of attack-related alerts (`ARXIV-2610.10608`). AWS's Deception Benchmark: models' precision at telling real from safe code sat in the mid-50s, and models ignored a Kubernetes NetworkPolicy that made code unexploitable (`AWS-DECEPTION-2026`).
- **How AI work is organised.** Databricks advertises a shared Agentic Security Engineering team that builds the platform on which each security function creates governed agents; Block, Cloudflare, Pinterest and Robinhood postings ask cloud and infrastructure security engineers to use AI tools (`DATABRICKS-JOB-AGENTICSEC-2026`, `BLOCK-JOB-PLATSEC-2026`, `CLOUDFLARE-JOB-VM-2026`, `PINTEREST-JOB-SECOPS-2026`, `ROBINHOOD-JOB-SECENG-2026`).

Use cases by grade: A = 1, B = 6, C = 9, D = 1 (17 total). Only 41% are graded A or B because most evidence is vendor-hosted or announcement-level; the grades were not inflated to reach the 50% target.

## 2. Use cases

Source access is `full` for every source listed (each was opened and read). Customer-story pages on wiz.io carry no publication date; they are dated `2026` and were retrieved on 2026-10-17.

```yaml
- id: security-cloud-infrastructure-01
  title: Autonomous external-exposure validation agent that tests the cloud perimeter and classifies what it finds
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - review-assurance
  - research-synthesis
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Periodic scans and inside-out data classification list assets and known CVEs, but do not show what is reachable from the internet and exploitable. At project44, false-positive-heavy scanners meant analysts validated findings before engineers would act.
  solution: A vendor-built agent (Wiz Red Agent) continuously discovers the perimeter, tests reachable endpoints, checks whether sensitive data is exposed, classifies and redacts what it finds, and raises a finding with a severity. Orca describes the same attacker-side role as one of three agent pods (Red, Blue, Green).
  outcomes:
  - lever: speed
    description: project44 reports faster remediation after adopting the Wiz Red and Green Agents with Wiz Code
    figure: 10x faster vulnerability remediation
    measures: headline result in Wiz's project44 case study; baseline, period and metric definition are not stated, and the figure covers Red Agent, Green Agent and Wiz Code together
    provenance: vendor-published
    source_ref: WIZ-PROJECT44-2026
  - lever: risk
    description: An unnamed Fortune 500 financial services firm says the Red Agent found a public page exposing sensitive business-unit data and was the only tool in its stack to catch it
    figure: none published
    measures: a single finding described in a customer quote hosted by the vendor; no counts given; Wiz's own summary says the customer found it in a day, understood it in minutes and resolved it
    provenance: vendor-published
    source_ref: WIZ-REDAGENT-2026
  - lever: risk
    description: Wiz's Scan for Good programme uses the Red Agent against public services, critical infrastructure and nonprofits where authorized
    figure: hundreds of public exposures fixed
    measures: Wiz's statement of exposures uncovered through Scan for Good that were fixed after validation and work with the affected organizations; the denominator and per-organization split are not stated
    provenance: vendor-published
    source_ref: WIZ-SCANFORGOOD-2026
  prerequisites:
  - Defined, authorized scope of domains, applications and cloud accounts to test (Scan for Good tests only where authorized)
  - Ownership data so validated findings route to a remediation owner
  - 'Engineering buy-in: project44 ran an engineering-wide enablement session on using the platform to fix findings'
  risks_and_guardrails:
  - Autonomous testing can leave its intended scope. A fwd:cloudsec Europe 2026 talk abstract says AWS Security Agent could cross expected trust and scope boundaries during autonomous pentesting and raises the shared-responsibility question (FWDCLOUDSEC-FAN-2026).
  - In AWS's own benchmark, the agent took two targets down before it could read the flag; AWS says non-destructive guardrails govern production engagements (AWS-SECAGENT-2026).
  - Wiz says the Red Agent redacts sensitive raw values before generating an alert so customer data is not stored in findings (WIZ-REDAGENT-2026).
  - The testimonials are vendor-hosted; the Fortune 500 customer is not named (WIZ-REDAGENT-2026).
  human_checkpoints:
  - People set and authorize the scope to be tested
  - Validated findings route to named remediation owners who fix them (WIZ-REDAGENT-2026)
  role_evolution: A project44 security operations analyst says validating exploitability upfront cuts the time the team spends chasing vulnerabilities, so engineers fix real risk instead of validating false positives (WIZ-PROJECT44-2026).
  evidence_grade: B
  sources:
  - ref: WIZ-PROJECT44-2026
    title: project44 Accelerates Cloud Remediation and Security Operations with Wiz AI Agents (customer story; page undated, retrieved 2026-10-17)
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/customers/project44
    date: '2026'
    access: full
    locator: Results; 'High-Confidence Findings with the Wiz Red Agent'
  - ref: WIZ-REDAGENT-2026
    title: How the Wiz Red Agent caught a Fortune 500 firm's data exposure (that other tools missed)
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/red-agent-financial-services-data-exposure
    date: '2026-10-07'
    access: full
    locator: Customer quote; 'What Red Agent actually did'
  - ref: WIZ-SCANFORGOOD-2026
    title: 'Scan for Good: Finding Critical Exposures with AI'
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/scan-for-good-critical-ai-exposures
    date: '2026-09-24'
    access: full
    locator: Opening paragraphs; 'Where authorized' paragraph
  - ref: ORCA-AGENTPODS-2026
    title: An Inside Look at Orca AI Agent Pods
    publisher: Orca Security
    type: vendor
    url: https://orca.security/resources/blog/an-inside-look-at-orca-ai-agent-pods/
    date: '2026-08-06'
    access: full
    locator: '''Red Pod: The Attacker''s Perspective'''
  - ref: AWS-SECAGENT-2026
    title: AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs
    publisher: AWS Security Blog
    type: vendor
    url: https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/
    date: '2026-10-15'
    access: full
    locator: Results list ('2 misses')
  - ref: FWDCLOUDSEC-FAN-2026
    title: Whose Fault When a Pentest Agent Attacks the Wrong Target? (Richard Fan)
    publisher: fwd:cloudsec Europe 2026
    type: conference
    url: https://pretalx.com/fwd-cloudsec-europe-2026/talk/VWFXZS/
    date: '2026-09-07'
    access: full
    locator: Talk abstract
  last_reviewed: '2026-10-17'
  notes: project44 is a named deployment, but its 10x figure has no stated metric definition, so the grade stays at B. Overlaps vulnerability-exposure (see Routed section).
- id: security-cloud-infrastructure-02
  title: Autonomous investigation of cloud detections, validated in parallel then used to close low-severity alerts
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - transaction-processing
  - research-synthesis
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Cloud detections require pulling identity, network, runtime and code context from several consoles. Wiz says manual investigation across sprawling cloud environments can take hours. ZS wanted analysts to spend their time on advanced investigations; Owkin runs a three-person security team over a large AWS estate.
  solution: 'The Wiz Blue Agent investigates a cloud threat: it gathers evidence, compares activity with a baseline (30 days in Wiz''s worked example), checks IP reputation and correlates across AWS and GitHub, then returns a verdict with the full investigation flow. ZS first ran it in parallel with analysts for three months, then let it close a defined set of low-severity cloud detections inside Wiz Defend.'
  outcomes:
  - lever: quality
    description: ZS compared Blue Agent analyses with its analysts' parallel investigations before operationalizing
    figure: 'accuracy around 95.17% (headline: 95% accuracy)'
    measures: ZS Director of Information Security's account of agreement between the Blue Agent's analysis and ZS analysts' analysis over three months of parallel investigation; sample size and the definition of 'accuracy' are not stated
    provenance: self-reported
    source_ref: WIZ-ZS-2026
  - lever: speed
    description: Time to render a verdict compared with manual analysis
    figure: 80-90% faster investigations
    measures: 'headline in the ZS case study: time to render a verdict compared to manual analysis; method and baseline not stated'
    provenance: vendor-published
    source_ref: WIZ-ZS-2026
  - lever: capacity
    description: Analyst throughput after adoption
    figure: 4x analyst throughput
    measures: 'headline in the ZS case study: analysts can triage significantly more threats than before; baseline and period not stated'
    provenance: vendor-published
    source_ref: WIZ-ZS-2026
  - lever: speed
    description: Owkin reports shorter handling of false-positive investigations using Mika and the Blue and Green agents
    figure: 75% reduction, from 20-30 minutes to 5 minutes
    measures: 'headline in the Owkin case study: time spent investigating false positives; sample and period not stated'
    provenance: vendor-published
    source_ref: WIZ-OWKIN-2026
  - lever: quality
    description: Owkin's head of cloud security ran manual investigations side by side with the agents at first
    figure: same conclusions '10 out of 10 times'
    measures: Owkin Head of Cloud Security's recollection of side-by-side manual vs agent threat assessments; the number of comparisons is not stated
    provenance: self-reported
    source_ref: WIZ-OWKIN-2026
  - lever: capacity
    description: ZS's director says the team now relies fully on the Blue Agent for some low-severity alerts, replacing many tickets with one review task at the end of each shift
    figure: none published
    measures: ZS Director of Information Security's statement hosted on Wiz's case study; no ticket counts given
    provenance: self-reported
    source_ref: WIZ-ZS-2026
  prerequisites:
  - Wiz Defend deployed and cloud detections flowing (ZS onboarded Wiz Defend first)
  - A way to measure agent verdicts against analysts before automating (ZS built an internal framework and tracked confidence over three months)
  - Runtime sensor forensic packages, if deeper evidence analysis is wanted (WIZ-BLUEAGENT-GA-2026)
  risks_and_guardrails:
  - ZS limited automatic closure to a defined set of low-severity cloud detections (WIZ-ZS-2026).
  - 'Independent evidence on LLM triage generally is less favourable: in ALERT-BENCH, every tool-using approach tested missed at least 40.4% of attack-related alerts across 1,247 alerts from one multi-stage scenario. The study did not test Wiz''s Blue Agent (ARXIV-2610.10608).'
  - Log content is attacker-controlled. In one study using gpt-4o-mini as the analyst, persona-hijack prompts suppressed 68% of malicious logs under a naive classifier (ARXIV-2605.24421).
  - Wiz says the Blue Agent shows the questions asked, data retrieved and how each signal shaped the verdict, so analysts can audit it (WIZ-BLUEAGENT-GA-2026).
  human_checkpoints:
  - ZS analysts perform a threat review at the end of each shift of what the Blue Agent closed (WIZ-ZS-2026)
  - Higher-severity cloud detections stay with analysts (WIZ-ZS-2026)
  role_evolution: ZS says analysts without deep cloud experience can read the verdict and evidence, spreading cloud knowledge beyond a few specialists, and analysts move from working queues to reviewing exceptions (WIZ-ZS-2026).
  evidence_grade: A
  sources:
  - ref: WIZ-ZS-2026
    title: How ZS Operationalized Blue Agent-Powered Cloud Detection and Response (customer story; page undated, retrieved 2026-10-17)
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/customers/zs-blue-agent
    date: '2026'
    access: full
    locator: Headline results; 'Earning Trust Before Automation'; 'From Alert Queues to Exception Reviews'
  - ref: WIZ-OWKIN-2026
    title: How Owkin's lean Security Team Protects AI-Driven Biotech Research at Scale (customer story; page undated, retrieved 2026-10-17)
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/customers/owkin
    date: '2026'
    access: full
    locator: Results headlines; section on AI capabilities
  - ref: WIZ-REDIS-2026
    title: Redis Achieves Unified Cloud Security at Scale with AI-Powered Threat Detection (customer story; page undated, retrieved 2026-10-17)
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/customers/redis-unified-cloud-security
    date: '2026'
    access: full
    locator: Solution bullet on the Blue Agent
  - ref: WIZ-BLUEAGENT-GA-2026
    title: The Wiz Blue Agent, now Generally Available
    publisher: Wiz
    type: vendor
    url: https://wiz.io/blog/wiz-blue-agent-generally-available
    date: '2026-03-30'
    access: full
    locator: '''Investigation with full context''; ''From triage to action'''
  - ref: WIZ-BLUEAGENT-CASE-2026
    title: How Wiz's Blue Agent Traced a Multi-Cloud Attack
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/blue-agent-data-exfiltration-investigation
    date: '2026-09-29'
    access: full
    locator: Phases 1 to 4 of the worked investigation
  - ref: ARXIV-2610.10608
    title: 'From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2610.10608
    date: '2026-10-07'
    access: full
    locator: Abstract
  - ref: ARXIV-2605.24421
    title: 'Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2605.24421
    date: '2026-05-23'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-17'
  notes: 'Strongest evidence in this module: a named firm, a three-month parallel run and a stated accuracy figure. All figures sit on vendor-hosted pages; the ZS accuracy figure is the firm''s own and the speed/throughput headlines are vendor-stated. The customer pages carry no publication date (the Blue Agent went GA on 2026-03-30, which bounds the earliest date). Redis says the Blue Agent sped up investigation and context collection but publishes no Blue Agent figure.'
- id: security-cloud-infrastructure-03
  title: Remediation agent that finds the owner and root cause and drafts the ticket or pull request
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - software-systems
  - coordination-scheduling
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Cloud findings arrive without an owner or a fix. La Centrale's three-person security team had to correlate network exposure, IAM permissions and data sensitivity by hand, and fixes have to be made where resources are defined.
  solution: The Wiz Green Agent uses code-to-cloud mapping, ownership context and remediation history to say where, who and how, and can open a pull request or hand the fix to a coding agent. Orca's Green Pod works out who owns a finding and drafts the fix in the team's usual format. La Centrale is running a proof of concept to automate Jira ticket generation with tailored remediation blueprints.
  outcomes:
  - lever: speed
    description: project44 uses the Green Agent for dependency-upgrade recommendations and code fixes, alongside the Red Agent
    figure: 10x faster vulnerability remediation (same headline as use case 01)
    measures: headline in Wiz's project44 case study; baseline, period and metric not stated; the figure cannot be split between the Red Agent, Green Agent and Wiz Code
    provenance: vendor-published
    source_ref: WIZ-PROJECT44-2026
  - lever: quality
    description: 'La Centrale: Green Agent proof of concept for Jira ticket generation'
    figure: none published
    measures: proof of concept described in one sentence; no results given
    provenance: vendor-published
    source_ref: WIZ-LACENTRALE-2026
  prerequisites:
  - 'Ownership data: tags, code-to-cloud mapping, service catalog or CMDB (WIZ-WORKFLOWS-2026)'
  - Source repositories connected to the platform
  - Ticketing integration and developers prepared to act on the output
  risks_and_guardrails:
  - Wiz says teams can set, per workflow, whether agents make routine remediations autonomously or need human approval on sensitive systems (WIZ-FORGOV-2026).
  - Remediation steps from Wiz Workflows can be sent straight to developers or their coding agent, so the review burden moves to the owning engineering team (WIZ-OPMODEL-2026).
  human_checkpoints:
  - Developers review and merge pull requests or act on tickets (WIZ-OPMODEL-2026)
  - Approval for changes on sensitive systems (WIZ-FORGOV-2026)
  role_evolution: project44's security operations manager compares the Green Agent to the velocity AI gave engineers, for security engineering work; the team treats engineers as the people who fix, rather than validate (WIZ-PROJECT44-2026).
  evidence_grade: B
  sources:
  - ref: WIZ-PROJECT44-2026
    title: project44 Accelerates Cloud Remediation and Security Operations with Wiz AI Agents (customer story; page undated, retrieved 2026-10-17)
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/customers/project44
    date: '2026'
    access: full
    locator: '''Scaling Secure Development with the Green Agent'''
  - ref: WIZ-LACENTRALE-2026
    title: 'From Alert Overload to Developer Ownership: How La Centrale Built a Top-Ranked Cloud Security Culture (customer story; page undated, retrieved 2026-10-17)'
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/customers/lacentrale
    date: '2026'
    access: full
    locator: Section on AI triage and Green Agent proof of concept
  - ref: WIZ-OPMODEL-2026
    title: Build AI Threat Readiness with Wiz
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/wiz-ai-threat-readiness-operating-model
    date: '2026-05-27'
    access: full
    locator: Pillar 2, 'Fix fast with the Wiz Green Agent'
  - ref: ORCA-AGENTPODS-2026
    title: An Inside Look at Orca AI Agent Pods
    publisher: Orca Security
    type: vendor
    url: https://orca.security/resources/blog/an-inside-look-at-orca-ai-agent-pods/
    date: '2026-08-06'
    access: full
    locator: '''Green Pod: The Path to Resolution'''
  - ref: WIZ-FORGOV-2026
    title: 'Wiz AI Agents for FedRAMP High: Accelerate Public Sector AI (Securing the Mission at Machine Speed)'
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/wiz-for-gov-agents-fedramp
    date: '2026-10-14'
    access: full
    locator: '''Introducing Wiz AI Agents in Wiz for Gov'''
  - ref: WIZ-WORKFLOWS-2026
    title: 'Introducing Wiz Workflows: Build a Self-Healing Cloud'
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/introducing-wiz-workflows
    date: '2026-03-25'
    access: full
    locator: Section on ownership routing
  last_reviewed: '2026-10-17'
  notes: The only named Green Agent users are project44 (no separate figure) and La Centrale (proof of concept). La Centrale's >90% fall in critical open vulnerabilities and 5-day SLA come from graph context and ownership routing, not from the Green Agent, so they are not claimed here.
- id: security-cloud-infrastructure-04
  title: Correlating weak runtime signals with posture context into one critical attack sequence
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - data-reporting
  - expert-judgment
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: Individual runtime findings on EC2, ECS and EKS are noisy; AWS says customer feedback consistently names noise as a major pain point. A runtime signal alone often stays below the threshold for a critical finding.
  solution: Amazon GuardDuty Extended Threat Detection correlates weak signals into one attack-sequence finding when they cross a credibility threshold. From 2026-05-20 it attaches five indicator types (vulnerability, malicious package, reachability, misconfiguration, sensitive data) taken from Inspector, VPC Reachability Analyzer, Macie and Security Hub posture data.
  outcomes:
  - lever: quality
    description: Net-new attack sequences on the runtime-process surface after the indicators were added
    figure: roughly one in four prioritized runtime-process attack sequences
    measures: AWS's description of the share of prioritized runtime-process attack sequences that were net-new after launch, in the first week across many customer accounts; counts and the number of accounts are not stated
    provenance: vendor-published
    source_ref: AWS-GUARDDUTY-ETD-2026
  - lever: speed
    description: 'One anonymised EKS example: 8 days of activity, 11 GuardDuty findings, 55 EKS audit-log signals and 18 finding-level signals'
    figure: surfaced as a single CRITICAL attack sequence
    measures: a single example scenario that AWS says was observed on an EKS cluster; not a rate
    provenance: vendor-published
    source_ref: AWS-GUARDDUTY-ETD-2026
  prerequisites:
  - Amazon Inspector on EC2 and EKS
  - AWS Security Hub (Foundational Security Best Practices)
  - VPC Reachability Analyzer on production VPCs
  - GuardDuty Runtime Monitoring on EC2, ECS and EKS
  - Amazon Macie for the sensitive-data indicator
  risks_and_guardrails:
  - AWS says the new indicators do not change incident-response runbooks for sequences that already occurred (AWS-GUARDDUTY-ETD-2026).
  - AWS advises patching by EPSS-weighted priority rather than CVSS alone, and rotating every credential that could have been exposed (AWS-GUARDDUTY-ETD-2026).
  - The post describes correlation across signals; it does not say a generative model produces the finding (AWS-GUARDDUTY-ETD-2026).
  human_checkpoints:
  - Responders contain exposures, isolate reachable hosts, rotate credentials and patch (AWS-GUARDDUTY-ETD-2026)
  role_evolution: Responders work from one sequence instead of triaging more than 100 CVE findings at worker-node level, per the AWS EKS example (AWS-GUARDDUTY-ETD-2026).
  evidence_grade: B
  sources:
  - ref: AWS-GUARDDUTY-ETD-2026
    title: GuardDuty Extended Threat Detection has added five new indicators to surface attack sequences
    publisher: AWS Security Blog
    type: vendor
    url: https://aws.amazon.com/blogs/security/guardduty-extended-threat-detection-has-added-five-new-indicators-to-surface-attack-sequences/
    date: '2026-10-12'
    access: full
    locator: '''New indicators overview''; ''Strengthening weak runtime signals''; EKS example; ''Responding to attack sequences'''
  last_reviewed: '2026-10-17'
  notes: 'Grade capped at B: the figure is an AWS-measured aggregate with no named customer, and the technique is signal correlation, so it is adjacent to LLM-based AI. Included because it shows how cloud detection vendors reduce triage load before any LLM is applied.'
- id: security-cloud-infrastructure-05
  title: In-house agentic triage of cloud security findings from many tools, with evidence rules and human approval for IAM and network changes
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - transaction-processing
  - research-synthesis
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: WRITER saw thousands of alerts from cloud security tooling, of which roughly 100 were truly actionable after triage, about a 2% signal rate. Analysts kept an undocumented heuristic about what to ignore, and it left when senior analysts left.
  solution: 'WRITER built Cerebro, an open-source agent system. It normalizes findings from CSPM, CNAPP and vulnerability tools, builds a resource graph, groups related findings into one incident, and has an agent choose: resolve now, ticket (with priority and owner), or defer/accept/monitor.'
  outcomes:
  - lever: quality
    description: 'Baseline before Cerebro: share of cloud alerts that were actionable'
    figure: about 2% signal rate (roughly 100 actionable out of thousands)
    measures: WRITER's own count after triage of alerts from its cloud security tooling, calculated over several weeks; this is the problem baseline, not an outcome
    provenance: self-reported
    source_ref: WRITER-CEREBRO-2026
  - lever: capacity
    description: Results after Cerebro
    figure: none published
    measures: WRITER says the team is 'excited with the results' but publishes no post-deployment numbers; it lists metrics it tracks (false positive rate, false negative rate, mean time to decision, analyst override rate, time saved) without values
    provenance: self-reported
    source_ref: WRITER-CEREBRO-2026
  prerequisites:
  - An up-to-date resource graph and ownership metadata (WRITER found the graph is never complete and added fallback heuristics)
  - Findings normalized into one queryable store (WRITER uses Snowflake)
  - Routing and approval rules agreed with the owners of IAM and network boundaries
  risks_and_guardrails:
  - 'WRITER''s first version said ''triage this'' without evidence and produced confident, plausible and often wrong answers; it now requires evidence before a decision: no ''resolve now'' without confirmed exposure, no ''defer'' without confirmed mitigation, no ''ticket'' without an owner (WRITER-CEREBRO-2026).'
  - Anything that touches IAM or a network boundary requires human approval; deterministic checks run before any downstream action (WRITER-CEREBRO-2026).
  - If evidence is missing the agent outputs needs_human_review rather than guessing (WRITER-CEREBRO-2026).
  human_checkpoints:
  - Human approval for IAM and network-boundary changes and for high-risk actions
  - Analyst override rate is a tracked metric
  role_evolution: WRITER frames the change as moving humans from assembling context across tools to decisions needing judgment; the agent proposes, rules validate, humans approve high-risk actions (WRITER-CEREBRO-2026).
  evidence_grade: B
  sources:
  - ref: WRITER-CEREBRO-2026
    title: 'Cerebro: An open source agentic system for security alert triage'
    publisher: WRITER Engineering
    type: firm
    url: https://writer.com/engineering/cerebro-ai-security-alert-triage-system/
    date: '2026-03-23'
    access: full
    locator: Opening; 'What Cerebro actually does'; 'What We Got Wrong (At First)'; 'Guardrails'; 'Evals'
  last_reviewed: '2026-10-17'
  notes: Named in-house deployment with a published baseline but no post-deployment figures. Status is described as built and in use by WRITER's team; the post says feedback is wanted 'once the repo is public', so production scope is not clear.
- id: security-cloud-infrastructure-06
  title: Agentic least-privilege role engineering that turns unused-access findings into infrastructure-as-code pull requests
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - software-systems
  - review-assurance
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: Permissions accumulate. IAM Access Analyzer can recommend right-sized policies, but a console fix is overwritten at the next deployment if the role is defined in CloudFormation or CDK, and manual remediation leaves no record of why. Tightening access can also break workflows.
  solution: 'AWS describes a daily automation that reads Access Analyzer findings, uses CloudTrail to find how each role was created, and uses Bedrock models to produce a pull request with CDK code and a plain-English explanation (IaC roles), an issue with migration steps (manual roles) or a soft-disable plan (unused roles). Two fwd:cloudsec 2026 talks show practitioners building agent versions: one describes a coding agent that drafts least-privilege Terraform updates from CloudTrail, plus agents that raise PRs after AccessDenied errors and check break-glass use against stated intent. A third talk describes a four-agent team (IAM, red team, threat intelligence, UEBA) that scored and reduced identity risk in an AWS account.'
  outcomes:
  - lever: risk
    description: A speaker (Field CTO at Sonrai Security) ran a four-agent team against a real AWS account
    figure: risk score down 42.7% (critical to moderate) in 5 days
    measures: 'per the talk abstract: a risk score across four dimensions (permissions, usage, exposure, activity) for identities in one AWS account of more than 500 identities; the scoring method is not described; the speaker works for an identity-security vendor'
    provenance: self-reported
    source_ref: FWDCLOUDSEC-HORSMAN-2026
  - lever: capacity
    description: AWS reference automation and the Smolen pipeline
    figure: none published
    measures: no results reported in the AWS post or the Smolen abstract
    provenance: vendor-published
    source_ref: AWS-LEASTPRIV-2026
  prerequisites:
  - IAM Access Analyzer unused-access analyzer enabled
  - Roles defined in IaC with a traceable repository, or a plan to migrate them
  - A CI/CD platform token stored securely and model access in Bedrock (AWS-LEASTPRIV-2026)
  risks_and_guardrails:
  - AWS recommends dry-run mode first, conservative pull-request limits ('a team that can review 10 PRs per week shouldn't receive 50 on Monday morning'), and routing admin or sensitive-data roles to manual review issues instead of automated PRs (AWS-LEASTPRIV-2026).
  - The Smolen abstract names the risk that a restricted role throws AccessDenied during an incident, and covers a trust-model discussion (FWDCLOUDSEC-SMOLEN-2026).
  - Horsman gave each agent its own machine identity and permission boundary, and used a red-team agent to validate that each control blocked the attack path (FWDCLOUDSEC-HORSMAN-2026).
  human_checkpoints:
  - The team that owns the role reviews the PR through normal code review (AWS-LEASTPRIV-2026)
  - Security review of AccessDenied-driven PRs (FWDCLOUDSEC-SMOLEN-2026)
  role_evolution: IAM cleanup moves from a side job to reviewing agent-drafted changes; Horsman's pitch is that most teams lack a dedicated cloud identity person (FWDCLOUDSEC-HORSMAN-2026).
  evidence_grade: C
  sources:
  - ref: AWS-LEASTPRIV-2026
    title: 'Operationalizing least privilege: Automate IAM remediation through your CI/CD pipeline'
    publisher: AWS Security Blog
    type: vendor
    url: https://aws.amazon.com/blogs/security/operationalizing-least-privilege-automate-iam-remediation-through-your-ci-cd-pipeline/
    date: '2026-09-15'
    access: full
    locator: '''Solution overview''; practices on limits, dry-run and approval tags'
  - ref: FWDCLOUDSEC-SMOLEN-2026
    title: 'Least Privilege is a Conversation: Building an Agentic Role Engineering Pipeline (Alex Smolen)'
    publisher: fwd:cloudsec North America 2026
    type: conference
    url: https://pretalx.com/fwd-cloudsec-2026/talk/9LRLDS/
    date: '2026-06-01'
    access: full
    locator: Talk abstract
  - ref: FWDCLOUDSEC-HORSMAN-2026
    title: I made AI agents apply for my Security Team. Then I gave the agents access to AWS. (Cole Horsman)
    publisher: fwd:cloudsec North America 2026
    type: conference
    url: https://pretalx.com/fwd-cloudsec-2026/talk/RAEUSE/
    date: '2026-06-01'
    access: full
    locator: Talk abstract and speaker bio
  last_reviewed: '2026-10-17'
  notes: AWS publishes a reference pattern, not a customer deployment. Both talks are abstracts of practitioner demos; the employers (EngSec Labs for Smolen) are consultancies or vendors. Overlaps identity-access.
- id: security-cloud-infrastructure-07
  title: 'Idea: policy-checking MCP server that makes coding agents generate cloud infrastructure through approved modules'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - software-systems
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: AI coding assistants now write much of the infrastructure code, so guardrails aimed at developers' judgment (approved Terraform modules, policy gates, training) no longer reach the party doing the reasoning.
  solution: 'A reference architecture presented at fwd:cloudsec 2026: an MCP server exposes approved Terraform modules from an internal registry, runs OPA policies with output designed for agents (severity, fix hints, auto-fix eligibility), auto-remediates fixable violations, scores exceptions by risk and sends high-risk ones to humans, then opens a compliant PR with a reasoning trace.'
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: conference talk abstract describing a reference architecture and live demo; no results
    provenance: self-reported
    source_ref: FWDCLOUDSEC-RENGASAMY-2026
  prerequisites:
  - Internal registry of approved Terraform modules
  - OPA policies written for agent consumption
  - Exception workflow with ticketing
  risks_and_guardrails:
  - 'Wiz describes a similar direction commercially: guardrails and code plugins that let coding agents scan and rewrite AI-generated code against organization baselines (WIZ-OPMODEL-2026).'
  human_checkpoints:
  - High-risk exceptions are escalated to humans (FWDCLOUDSEC-RENGASAMY-2026)
  role_evolution: Security effort shifts from training developers to engineering the tools and context an agent can use (FWDCLOUDSEC-RENGASAMY-2026).
  evidence_grade: D
  sources:
  - ref: FWDCLOUDSEC-RENGASAMY-2026
    title: 'Agentic Paved Roads: Shifting Security Left to the Machine That Thinks (Prahathess Rengasamy)'
    publisher: fwd:cloudsec North America 2026
    type: conference
    url: https://pretalx.com/fwd-cloudsec-2026/talk/RDXF3X/
    date: '2026-06-01'
    access: full
    locator: Talk abstract and speaker bio
  - ref: WIZ-OPMODEL-2026
    title: Build AI Threat Readiness with Wiz
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/wiz-ai-threat-readiness-operating-model
    date: '2026-05-27'
    access: full
    locator: Pillar 2, 'Implement prevention with WizOS and guardrails'
  last_reviewed: '2026-10-17'
  notes: 'Idea: discussed by a practitioner (a security engineer at xAI) as a reference architecture with a demo; no deployment found.'
- id: security-cloud-infrastructure-08
  title: Virtual patching at the WAF and network layer for newly found vulnerabilities, with AI-assisted rule generation
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - software-systems
  - expert-judgment
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Patching takes weeks and cannot match AI-speed vulnerability discovery. A fwd:cloudsec abstract cites a 43-day median time to patch a critical vulnerability, and critical-infrastructure operators say uptime and safety testing prevent patching at AI speed. Tuning WAF rules across hundreds of stacks does not scale with headcount.
  solution: 'Two routes. In-house: a DevSecOps manager at Adobe describes AI-assisted WAF rule generation and context-aware tuning inside a human-in-the-loop pipeline. Vendor: Palo Alto Networks announced Frontier Virtual Patching, network-level patches delivered through its Frontier AI Critical Defense Program (2026-08-19) and a collaboration with IBM and Red Hat (2026-06-24) that plans same-day network protection for newly discovered flaws.'
  outcomes:
  - lever: speed
    description: Claim in the Adobe manager's talk abstract about the approach
    figure: '''from 43 days to single-digit minutes'' (claimed capability)'
    measures: abstract says the approach can compress the cycle from vulnerability disclosed to fleet protected; 43 days is the industry median time to patch cited in the abstract, not a measured Adobe baseline; no measurement shown
    provenance: self-reported
    source_ref: FWDCLOUDSEC-ALIM-2026
  - lever: risk
    description: 'Context cited by Palo Alto Networks for its program: it says it recently used frontier AI models to uncover unknown vulnerabilities in open source software'
    figure: more than 14,000 previously unknown vulnerabilities
    measures: Palo Alto Networks' count of unknown open-source vulnerabilities it says it uncovered with frontier AI models; not independently verified
    provenance: vendor-published
    source_ref: PANW-FRONTIERCDP-2026
  prerequisites:
  - A WAF or network enforcement point that can take rules quickly
  - Vulnerability intelligence from the software owner or a coordinated disclosure partner (Lightwell and the Critical Defense Program rely on shared vulnerability information)
  - Testing path so a rule does not become a reliability incident
  risks_and_guardrails:
  - Rules that are too broad are useless and rules that are too tight become an outage (FWDCLOUDSEC-ALIM-2026).
  - Palo Alto Networks says it plans to establish secure processes for sharing vulnerability information (PANW-LIGHTWELL-2026) and describes Frontier Virtual Patching as safeguarding sensitive vulnerability details from attackers (PANW-FRONTIERCDP-2026).
  - These are announcements and a conference abstract; no deployment outcome is published.
  human_checkpoints:
  - Human-in-the-loop pipeline for rule approval (FWDCLOUDSEC-ALIM-2026)
  - IBM Security Services can help customers prioritize, deploy and validate protections (PANW-LIGHTWELL-2026)
  role_evolution: The WAF engineer's work shifts from hand-writing rules per technology stack to reviewing generated rules (FWDCLOUDSEC-ALIM-2026).
  evidence_grade: C
  sources:
  - ref: FWDCLOUDSEC-ALIM-2026
    title: 'The Tireless Guardian: Agentic AI and the Art of WAF at Scale (Ammar Alim)'
    publisher: fwd:cloudsec North America 2026
    type: conference
    url: https://pretalx.com/fwd-cloudsec-2026/talk/XEMZWB/
    date: '2026-06-01'
    access: full
    locator: Talk abstract and speaker bio
  - ref: PANW-LIGHTWELL-2026
    title: IBM, Red Hat and Palo Alto Networks Expand Project Lightwell to Help Organizations Respond to Software Vulnerabilities
    publisher: Palo Alto Networks (press release)
    type: vendor
    url: https://www.paloaltonetworks.com/company/press/2026/ibm-red-hat-and-palo-alto-networks-expand-project-lightwell-to-help-organizations-respond-to-software-vulnerabilities
    date: '2026-06-24'
    access: full
    locator: '''A Seamless Shield-and-Fix Workflow''; key capabilities'
  - ref: PANW-FRONTIERCDP-2026
    title: Palo Alto Networks Introduces Frontier AI Critical Defense Program
    publisher: Palo Alto Networks (press release)
    type: vendor
    url: https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-introduces-frontier-ai-critical-defense-program
    date: '2026-08-19'
    access: full
    locator: Opening paragraphs
  last_reviewed: '2026-10-17'
  notes: Overlaps vulnerability-exposure and the optional OT module. Palo Alto statements use plans/goals language ('plan to establish', 'long-term goal'); treat as announced.
- id: security-cloud-infrastructure-09
  title: 'AI-driven firewall policy hygiene: flag stale, overly permissive and conflicting rules from observed traffic'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - review-assurance
  - software-systems
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Firewall rulebases grow through temporary exceptions, cloud deployments and new AI-driven workloads. Check Point says policies become risky after months of incremental changes, and reviews wait for the next policy review cycle.
  solution: Cato Networks' AI-Driven Posture agent analyses rule behaviour against traffic across the Internet, WAN and LAN firewalls and remote port forwarding, flags forgotten test rules and overly permissive rules, and a wizard recommends rules to enable (for example TLS inspection for AI tools). Check Point's AI Auditor and AI Insights look for redundant rules, excessive permissions, conflicts and unused access paths, and prioritize IPS protections by risk.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: product documentation and a vendor blog; Cato's examples are illustrative scenarios without named customers; no measured results
    provenance: vendor-published
    source_ref: CATO-AUTONOMOUSPOL-2026
  prerequisites:
  - Traffic and rule telemetry from the vendor's cloud (Cato says the agent learns from flows across Cato Cloud)
  - Admin owners able to accept or reject each recommendation
  risks_and_guardrails:
  - Check Point says the goal is not to automate security decisions but to reduce the manual analysis needed to make them (CHECKPOINT-AGENTICNET-2026).
  - Cato presents recommendations that administrators choose to apply; the wizard guides configuration after the admin selects rules (CATO-AUTONOMOUSPOL-2026).
  human_checkpoints:
  - Administrators select which recommended rules to apply (CATO-AUTONOMOUSPOL-2026)
  role_evolution: Check Point says security teams spend much of their time reviewing firewall rules and validating protections, and expects them to spend more time on risk-based decisions (CHECKPOINT-AGENTICNET-2026).
  evidence_grade: C
  sources:
  - ref: CATO-AUTONOMOUSPOL-2026
    title: Understanding Cato Autonomous Policies (product documentation)
    publisher: Cato Networks
    type: vendor
    url: https://knowledge.catonetworks.com/docs/understanding-cato-autonomous-policies
    date: '2026-08-27'
    access: full
    locator: Overview; 'Autonomous Policies Use Cases'
  - ref: CHECKPOINT-AGENTICNET-2026
    title: 'When Security Operations Can''t Keep Up: 4 Ways Agentic Network Security Management Improves Security Operations'
    publisher: Check Point
    type: vendor
    url: https://blog.checkpoint.com/hybrid-mesh/when-security-operations-cant-keep-up-4-ways-agentic-network-security-management-improves-security-operations/
    date: '2026-09-18'
    access: full
    locator: Sections 1, 3 and closing; Gartner quote paragraph
  last_reviewed: '2026-10-17'
  notes: Included because network policy is part of this module; evidence is product documentation only. Check Point says its management features are powered by OpenAI Daybreak frontier models (vendor statement).
- id: security-cloud-infrastructure-10
  title: First-pass incident investigation agent with read-only access to every Kubernetes cluster
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: First-pass triage of Kubernetes incidents needs pod state, logs, metrics and deployment history from many clusters.
  solution: An open-source investigation agent runs in a production Kubernetes estate, one instance per cluster, doing first-pass triage from pod state, logs, metrics and deployment history. The abstract's author, who leads cloud and autonomous systems security at a European automotive manufacturer, says it has run for over a year and has never written to a cluster; the title and abstract speak of 'our' fleet.
  outcomes:
  - lever: quality
    description: Four failure modes found despite a 'read-only' permission label
    figure: 4 failures
    measures: 'the speaker''s count of incidents in which the agent behaved unexpectedly: secrets reached through pod specs and logs, an unattributable audit-log line, a guessed cluster-name parameter, and an over-fetch that hit its own resource ceiling'
    provenance: self-reported
    source_ref: FWDCLOUDSEC-RAJI-2026
  prerequisites:
  - Per-cluster agent instances
  - Tool scopes narrower than the 'read-only' label (read access to pod events reached secret material)
  - Cost and resource ceilings
  risks_and_guardrails:
  - All four failures happened under a correctly labelled read-only permission set; the speaker says every control that held was infrastructure and every control that failed was a prompt (FWDCLOUDSEC-RAJI-2026).
  - 'Agent identity in audit logs was unclear: a log line could not be attributed to the agent or a human (FWDCLOUDSEC-RAJI-2026).'
  human_checkpoints:
  - The agent has never written to a cluster; people act on its first-pass triage (FWDCLOUDSEC-RAJI-2026)
  role_evolution: Platform and security engineers become reviewers of agent scope, identity and cost, not only of its answers (FWDCLOUDSEC-RAJI-2026).
  evidence_grade: C
  sources:
  - ref: FWDCLOUDSEC-RAJI-2026
    title: What We Learned Giving an AI Agent Read Access to Our Whole Kubernetes Fleet (Amine Raji)
    publisher: fwd:cloudsec Europe 2026
    type: conference
    url: https://pretalx.com/fwd-cloudsec-europe-2026/talk/TN9SP9/
    date: '2026-09-08'
    access: full
    locator: Talk abstract and speaker bio
  last_reviewed: '2026-10-17'
  notes: Practitioner first-hand report from a conference abstract; the organization is not named, so it cannot support a B.
- id: security-cloud-infrastructure-11
  title: Reasoning-trained detection triage model with calibrated confidence for auto-closing endpoint detections
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - transaction-processing
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Detections exceed what SOC staff can triage in a day. Models that emit a label directly do not reason about whether a detection is a genuine threat, and chain-of-thought degrades the confidence score that automation depends on.
  solution: CrowdStrike trained a chain-of-thought triage classifier on real, human-labelled Windows endpoint detections using prompt optimization, self-training and reinforcement learning with verifiable rewards, plus a separate calibrator that reads the reasoning trace and estimates whether the verdict is correct. CrowdStrike says its Charlotte AI triage models already give true/false-positive verdicts with calibrated confidence; the reasoning model is research focused on Windows endpoint detections.
  outcomes:
  - lever: quality
    description: Overall test accuracy of the reasoning-enabled classifier
    figure: 82.6% test accuracy
    measures: accuracy of the CrowdStrike classifier on a held-out test set of human-labelled Windows endpoint detections (offline evaluation)
    provenance: vendor-published
    source_ref: ARXIV-2607.28460
  - lever: capacity
    description: Gain at the high-confidence operating point that governs automated triage, versus a direct-label LLM classifier
    figure: benign recall +43.0%, malicious recall +18.3%
    measures: relative gains in recall at the stated high-precision thresholds on the same offline test set; absolute recall levels are in the paper body, not in the abstract
    provenance: vendor-published
    source_ref: ARXIV-2607.28460
  prerequisites:
  - Large, human-labelled detection data (CrowdStrike trains on real analyst-labelled detections)
  - A calibrator so that confidence thresholds for auto-closure stay reliable
  risks_and_guardrails:
  - An untrained confidence judge collapsed high-confidence recall to zero, so the calibrator is necessary (ARXIV-2607.28460).
  - CrowdStrike says its fine-tuned 30B model outperformed frontier general-purpose models, which argues for targeted training over scale; this is the vendor's own comparison (ARXIV-2607.28460).
  human_checkpoints:
  - Analysts can read the chain of reasoning before trusting a verdict (CROWDSTRIKE-TRIAGE-2026)
  - Only detections above the high-confidence threshold are candidates for auto-close (ARXIV-2607.28460)
  role_evolution: Analysts read and evaluate a transparent rationale instead of an unexplained label (CROWDSTRIKE-TRIAGE-2026).
  evidence_grade: B
  sources:
  - ref: ARXIV-2607.28460
    title: Cybersecurity Detection Classification with Reasoning-enabled Language Models
    publisher: arXiv (Khanna et al., CrowdStrike authors)
    type: academic
    url: https://arxiv.org/abs/2607.28460
    date: '2026-07-30'
    access: full
    locator: Abstract
  - ref: CROWDSTRIKE-TRIAGE-2026
    title: Teaching AI to Reason Through Detection Triage
    publisher: CrowdStrike
    type: vendor
    url: https://www.crowdstrike.com/en-us/blog/teaching-ai-to-reason-through-detection-triage/
    date: '2026-08-17'
    access: full
    locator: Opening and 'Confidence calibration' paragraphs
  last_reviewed: '2026-10-17'
  notes: 'Grade capped at B: a measured offline result from a named vendor, no deployment outcome. Whether this specific reasoning model is deployed is not stated in the blog. The independent triage benchmark (ARXIV-2610.10608) and the log-injection study (ARXIV-2605.24421) show why these figures should be tested locally.'
- id: security-cloud-infrastructure-12
  title: Posture-prioritization agent that ranks cloud and device findings and explains what to fix first
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - review-assurance
  - data-reporting
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: Security administrators and vulnerability teams keep a continuous queue of posture recommendations. The difficulty is knowing which to fix first. Wiz Research reports that high-priority alerts lose more than half their count once reachability, toxic permissions and sensitive-data access are applied.
  solution: Microsoft's Posture Prioritization Agent (Project Perception, limited public preview) ingests cloud and device posture findings and produces a ranked, explained action plan, including a threat-driven mode that maps a threat to posture findings. CrowdStrike announced AI-enhanced remediation plans in Falcon Cloud Security with time estimates, confidence indicators, permission needs and a validation check.
  outcomes:
  - lever: quality
    description: Wiz Research compared high-priority alerts before and after applying external reachability, toxic permission combinations and sensitive-data access
    figure: more than half of initial findings eliminated across four risk categories
    measures: Wiz Research's before/after comparison of high-priority alerts across enterprise environments; the counts, categories and customer sample are in the full report, not the blog; graph-based context, not a language-model agent
    provenance: vendor-published
    source_ref: WIZ-CLOUDRISK-2026
  prerequisites:
  - Posture findings from cloud and device sources
  - 'For Microsoft''s preview agent: Microsoft 365 E5 among other prerequisites; invitation-only limited public preview'
  risks_and_guardrails:
  - In preview the Microsoft agent is read-only (MSFT-LEARN-PPA-2026).
  - AWS's Deception Benchmark found models tested in single-turn prompting flagged code next to a Kubernetes NetworkPolicy that made it unexploitable, and none kept both false positives and false negatives under 10% (AWS-DECEPTION-2026). That benchmark tests code vulnerabilities, not posture findings, so treat it as a caution about environment-aware reasoning.
  human_checkpoints:
  - The agent produces a plan; people decide and act (MSFT-LEARN-PPA-2026)
  - CrowdStrike says teams that want automation can run the plan through Charlotte Agentic SOAR (CROWDSTRIKE-CLOUDREM-2026)
  role_evolution: Microsoft says the agent gives the rationale, evidence and cost of not acting so teams can justify priorities to stakeholders (MSFT-LEARN-PPA-2026).
  evidence_grade: C
  sources:
  - ref: MSFT-LEARN-PPA-2026
    title: Posture Prioritization Agent (Project Perception, limited public preview)
    publisher: Microsoft Learn
    type: vendor
    url: https://learn.microsoft.com/en-us/security/agentic-security/posture-prioritization-agent
    date: '2026-08-03'
    access: full
    locator: Introduction; 'Scenarios'; 'Preview scope and limitations'
  - ref: CROWDSTRIKE-CLOUDREM-2026
    title: 'New in Falcon Cloud Security: Third-Party App Insights and AI-Enhanced Remediation'
    publisher: CrowdStrike
    type: vendor
    url: https://www.crowdstrike.com/en-us/blog/falcon-cloud-security-third-party-app-insights-ai-enhanced-remedation/
    date: '2026-10-05'
    access: full
    locator: '''AI-Enhanced Remediation Plans for Cloud Risks'''
  - ref: WIZ-CLOUDRISK-2026
    title: 'Report Recap: State of Cloud Risk 2026'
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/cloud-risk-report-2026
    date: '2026-08-26'
    access: full
    locator: '''The Context Filter: Turning Alerts Into Action'''
  - ref: AWS-DECEPTION-2026
    title: 'The state of AI for security: Measuring what matters most for building trust (Deception Benchmark)'
    publisher: AWS Security Blog
    type: vendor
    url: https://aws.amazon.com/blogs/security/the-state-of-ai-for-security-measuring-what-matters-most-for-building-trust/
    date: '2026-09-09'
    access: full
    locator: Results paragraph
  last_reviewed: '2026-10-17'
  notes: Microsoft's page says it relates to a prereleased product that may change. CrowdStrike's remediation plans are a launch announcement dated 2026-10-05. No named customer or measured agent outcome found.
- id: security-cloud-infrastructure-13
  title: AI agents inside a FedRAMP High cloud security platform to support continuous authorization
  archetype: security
  module: cloud-infrastructure
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Point-in-time compliance checks struggle to keep pace with dynamic cloud environments; public-sector teams also need AI workload discovery and remediation inside a FedRAMP High boundary.
  solution: Wiz announced on 2026-10-14 that its Red, Blue and Green agents are available in Wiz for Gov, its FedRAMP High environment. Wiz says continuous visibility enhanced by AI analysis simplifies evidence collection and risk-posture tracking for continuous authorization to operate and continuous monitoring, and that operators can configure which routine remediations agents may make autonomously.
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: launch announcement; Wiz claims it is the first AI-APP for the US public sector (vendor claim)
    provenance: vendor-published
    source_ref: WIZ-FORGOV-2026
  prerequisites:
  - Wiz for Gov (FedRAMP High) tenancy
  - Operational boundaries set per workflow
  risks_and_guardrails:
  - CISA BOD 26-04, issued 2026-06-10 according to CrowdStrike, replaces BOD 19-02 and BOD 22-01 and requires risk-based remediation using public exposure, KEV status, exploit automatability and technical impact; the highest-risk cases carry a three-calendar-day clock (CROWDSTRIKE-BOD2604-2026; CISA's own page was not reachable).
  human_checkpoints:
  - Human-in-the-loop approval is configurable per workflow for sensitive systems (WIZ-FORGOV-2026)
  role_evolution: Wiz says agents act as a force multiplier for human operators and move teams from point-in-time compliance to continuous lifecycle-wide risk management (WIZ-FORGOV-2026).
  evidence_grade: C
  sources:
  - ref: WIZ-FORGOV-2026
    title: 'Wiz AI Agents for FedRAMP High: Accelerate Public Sector AI (Securing the Mission at Machine Speed)'
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/wiz-for-gov-agents-fedramp
    date: '2026-10-14'
    access: full
    locator: '''From CNAPP to AI-APP''; ''Introducing Wiz AI Agents in Wiz for Gov''; ''Delivering Mission Outcomes at Scale'''
  - ref: CROWDSTRIKE-BOD2604-2026
    title: CrowdStrike Falcon Platform Helps Meet U.S. Government Mandates for CISA BOD-26-04
    publisher: CrowdStrike
    type: vendor
    url: https://www.crowdstrike.com/en-us/blog/crowdstrike-falcon-platform-helps-meet-us-government-mandates-cisa-bod-26-04/
    date: '2026-07-22'
    access: full
    locator: Opening paragraphs
  last_reviewed: '2026-10-17'
  notes: Announcement only. BOD 26-04 details come from a vendor's summary because CISA's site blocked access.
- id: security-cloud-infrastructure-14
  title: LLM-assisted cloud detection engineering and telemetry analysis
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - software-systems
  - research-synthesis
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Detection engineers must write and keep up rules across cloud, endpoint and identity telemetry as threats change.
  solution: A Wiz job posting for a cloud threat detection researcher lists using AI/LLM-driven tools to enhance detection generation and telemetry analysis as a responsibility. A Cloudflare network security engineer posting lists generative AI and automation for log analysis and root-cause analysis during incidents. Wiz Defend ships out-of-the-box content (rules, dashboards, queries, playbooks) that it now exposes in Google Security Operations through a content pack.
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: job posting wording; no results
    provenance: vendor-published
    source_ref: WIZ-JOB-CLOUDDET-2026
  prerequisites:
  - Telemetry access for the detection team
  - Review and testing of generated detections before release
  risks_and_guardrails:
  - Pinterest's security operations posting asks engineers to apply AI to accelerate analysis while defining validation, data-handling and accountability practices (PINTEREST-JOB-SECOPS-2026).
  - Log content fed to an AI analyst is attacker-controlled input (ARXIV-2605.24421).
  human_checkpoints:
  - Detection researchers own and review rules (WIZ-JOB-CLOUDDET-2026)
  role_evolution: The posting asks researchers to use LLM tools as part of the job (WIZ-JOB-CLOUDDET-2026).
  evidence_grade: C
  sources:
  - ref: WIZ-JOB-CLOUDDET-2026
    title: Threat Detection Researcher (Cloud)
    publisher: Wiz (Greenhouse job board)
    type: job-posting
    url: https://www.wiz.io/careers/job/4566780006/:title?gh_jid=4566780006
    date: '2026-08-19'
    access: full
    locator: Responsibilities list
  - ref: WIZ-DEFENDGSO-2026
    title: Wiz Defend & Google Security Operations Integration
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/wiz-defend-and-google-security-operations
    date: '2026-09-15'
    access: full
    locator: '''A shared data model across platforms'''
  - ref: PINTEREST-JOB-SECOPS-2026
    title: Sr. Security Software Engineer, Security Operations
    publisher: Pinterest (Greenhouse job board)
    type: job-posting
    url: https://www.pinterestcareers.com/jobs/?gh_jid=8230778
    date: '2026-10-01'
    access: full
    locator: Responsibilities
  - ref: ARXIV-2605.24421
    title: 'Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2605.24421
    date: '2026-05-23'
    access: full
    locator: Abstract
  - ref: CLOUDFLARE-JOB-NETSEC-2026
    title: Network Security Engineer
    publisher: Cloudflare (Greenhouse job board)
    type: job-posting
    url: https://boards.greenhouse.io/cloudflare/jobs/8081027?gh_jid=8081027
    date: '2026-07-24'
    access: full
    locator: 'Responsibilities: generative AI for log analysis and root-cause analysis'
  last_reviewed: '2026-10-17'
  notes: Single job posting; weak evidence of real use.
- id: security-cloud-infrastructure-15
  title: Shared security AI platform where each security function builds governed agents ('personas')
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - software-systems
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: Each security function (detection and response, threat intelligence, vulnerability management, red team, GRC, continuous monitoring) wants agents, but each building its own risks inconsistent identity, isolation and audit.
  solution: 'Databricks advertises a horizontal Agentic Security Engineering team that ''enables every Databricks security function AI-native'' and owns the shared platform on which functions build, deploy and run governed AI personas, covering agent identity, isolation and sandboxing, policy enforcement, auditability, evaluation and orchestration. CrowdStrike sells the same idea as Charlotte AI AgentWorks: agents bounded in scope, versioned, role-governed, cost-capped and traceable. Block''s platform-security posting asks for integrations with CSPM and DSPM tools to surface and prioritize findings (BLOCK-JOB-PLATSEC-2026). Robinhood''s security engineering posting splits AI work in two: securing its AI infrastructure and building AI platforms that improve detection fidelity and coverage.'
  outcomes:
  - lever: capacity
    description: none published for Databricks; CrowdStrike quotes a customer analyst on build time
    figure: 6-8 hours in Microsoft Copilot vs 4 minutes in AgentWorks
    measures: one analyst's comparison of the time to build the same agent, as quoted by CrowdStrike; analyst and organization not named
    provenance: vendor-published
    source_ref: CROWDSTRIKE-AGENTWORKS-2026
  prerequisites:
  - Platform engineers experienced in agent identity, sandboxing and policy enforcement
  - Named AI champions in each security function (Databricks posting)
  - Evaluation datasets to benchmark agent versions before promotion (CrowdStrike)
  risks_and_guardrails:
  - Databricks lists high-risk workflows as offensive personas, untrusted inputs, sensitive data, production access and automated tool execution (DATABRICKS-JOB-AGENTICSEC-2026).
  - Pegasystems' senior director of corporate security operations is quoted saying governance means agents that are testable, traceable, capped and versioned (CROWDSTRIKE-AGENTWORKS-2026).
  human_checkpoints:
  - Platform owns guardrails; domain teams own business outcomes of their personas (DATABRICKS-JOB-AGENTICSEC-2026)
  role_evolution: 'Security engineers become builders and supervisors of agents: Databricks hires platform architects to serve security functions; Block''s platform-security posting asks for fluency with agentic coding tools in real production work (BLOCK-JOB-PLATSEC-2026); Robinhood and Cloudflare postings list AI use among requirements (ROBINHOOD-JOB-SECENG-2026, CLOUDFLARE-JOB-VM-2026).'
  evidence_grade: B
  sources:
  - ref: DATABRICKS-JOB-AGENTICSEC-2026
    title: Sr. Staff Security Software Engineer - Agentic Security Engineering
    publisher: Databricks (Greenhouse job board)
    type: job-posting
    url: https://databricks.com/company/careers/open-positions/job?gh_jid=8612865002
    date: '2026-10-12'
    access: full
    locator: Team description and responsibilities
  - ref: CROWDSTRIKE-AGENTWORKS-2026
    title: How AI-leading Security Teams Are Building the Agentic SOC
    publisher: CrowdStrike
    type: vendor
    url: https://www.crowdstrike.com/en-us/blog/how-ai-leading-security-teams-are-building-the-agentic-soc/
    date: '2026-07-06'
    access: full
    locator: '''The AgentWorks Advantage''; customer quotes'
  - ref: ROBINHOOD-JOB-SECENG-2026
    title: Senior Staff Security Engineer, Security Engineering
    publisher: Robinhood (Greenhouse job board)
    type: job-posting
    url: https://boards.greenhouse.io/robinhood/jobs/8167616
    date: '2026-09-01'
    access: full
    locator: Opening paragraph and responsibilities
  - ref: BLOCK-JOB-PLATSEC-2026
    title: Senior Security Engineer, Platform Security
    publisher: Block (Greenhouse job board)
    type: job-posting
    url: http://block.xyz/careers/jobs/5231316008?gh_jid=5231316008
    date: '2026-06-02'
    access: full
    locator: Responsibilities and requirements
  - ref: CLOUDFLARE-JOB-VM-2026
    title: Vulnerability Management Engineer
    publisher: Cloudflare (Greenhouse job board)
    type: job-posting
    url: https://boards.greenhouse.io/cloudflare/jobs/7579269?gh_jid=7579269
    date: '2026-02-05'
    access: full
    locator: Responsibilities and requirements
  last_reviewed: '2026-10-17'
  notes: 'Named organizations (Databricks, Robinhood, Block, Cloudflare) show how work is organised, but from job postings and no outcomes. Maturity ''piloting'' is a judgement: the Databricks team is described as existing, but its usage and results are not published. The scope is wider than cloud-infrastructure.'
- id: security-cloud-infrastructure-16
  title: Managed cloud security services run on a multi-tenant AI security platform
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - client-interaction
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Managed service providers juggle fragmented consoles, client policies and scattered visibility, which slows their response while their client estates grow.
  solution: Wiz announced an MSP programme on 2026-09-28 with centralized multi-tenant management, just-in-time provisioning and portfolio-level dashboards on its AI Application Protection Platform; partners quoted include Optiv, SEP2 and Deloitte. Wiz also launched an integration so Wiz Defend and its Blue Agent analysis appear inside Google Security Operations cases.
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: programme announcement with partner quotes; no results
    provenance: vendor-published
    source_ref: WIZ-MSP-2026
  prerequisites:
  - Multi-tenant management console
  - Partner agreement and billing model
  risks_and_guardrails:
  - Announcement only; the partner quotes are marketing statements (WIZ-MSP-2026).
  human_checkpoints:
  - Wiz says analysts can review and audit the Blue Agent's investigation and verdict (WIZ-DEFENDGSO-2026)
  role_evolution: Optiv's SVP of managed services says the programme advances turning managed security services into an AI-powered security operations model (WIZ-MSP-2026).
  evidence_grade: C
  sources:
  - ref: WIZ-MSP-2026
    title: Introducing the Wiz Partner Alliance MSP Program
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/introducing-wiz-partner-alliance-managed-service-provider-program
    date: '2026-09-28'
    access: full
    locator: Opening and partner quotes
  - ref: WIZ-DEFENDGSO-2026
    title: Wiz Defend & Google Security Operations Integration
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/wiz-defend-and-google-security-operations
    date: '2026-09-15'
    access: full
    locator: '''Accelerate Google Security Operations investigations with Blue Agent analysis'''
  last_reviewed: '2026-10-17'
  notes: Service-model change, not yet evidenced by a provider's published results. Related MDR repositioning is covered in the security-operations module.
- id: security-cloud-infrastructure-17
  title: Verdict-triggered cloud containment and response workflows with constrained action vocabularies
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  work_types:
  - transaction-processing
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Triage output must turn into action across tools and teams, but an LLM that can issue commands on production hosts adds a new path for attackers who control log content.
  solution: Wiz Workflows (2026-03-25) lets teams chain triggers, approvals, rescans and remediation, including steps run by Wiz agents; after the Blue Agent's verdict, teams can escalate, notify responders or trigger containment playbooks by verdict and confidence. CrowdStrike markets Charlotte Agentic SOAR to connect its own, custom and third-party agents. A research paper proposes confining an LLM to a closed intent vocabulary with templated commands, an argument validator and a guardrails proxy.
  outcomes:
  - lever: risk
    description: Research on guarding automated response actions
    figure: injection recall 25.0% to 94.5% at 0.1% false-positive rate
    measures: recall of prompt-injection attempts by a NeMo Guardrails proxy, stock vs configured, on the authors' SOC-specific adversarial corpus (research prototype, not an operational deployment)
    provenance: independent
    source_ref: ARXIV-2610.09906
  prerequisites:
  - Playbooks with defined, reversible actions
  - Verdict confidence scoring
  - Input and output guardrails on any analyst LLM
  risks_and_guardrails:
  - The authors say the loop is best run human-in-the-loop or delayed because measured guardrail latency keeps inline control out of scope (ARXIV-2610.09906).
  - A single adversarial alert can become a remote code path through the model's reasoning (ARXIV-2610.09906); log fields are attacker-controlled (ARXIV-2605.24421).
  - Writer's Cerebro requires human approval for anything touching IAM or network boundaries (WRITER-CEREBRO-2026).
  human_checkpoints:
  - Approvals inside workflows (WIZ-WORKFLOWS-2026)
  - Human-in-the-loop or delayed execution for model-issued commands (ARXIV-2610.09906)
  role_evolution: Analysts become designers and approvers of response playbooks rather than executors (WIZ-WORKFLOWS-2026).
  evidence_grade: C
  sources:
  - ref: WIZ-WORKFLOWS-2026
    title: 'Introducing Wiz Workflows: Build a Self-Healing Cloud'
    publisher: Wiz
    type: vendor
    url: https://www.wiz.io/blog/introducing-wiz-workflows
    date: '2026-03-25'
    access: full
    locator: Opening and 'Scaling Remediation with Agents in Workflows'
  - ref: WIZ-BLUEAGENT-GA-2026
    title: The Wiz Blue Agent, now Generally Available
    publisher: Wiz
    type: vendor
    url: https://wiz.io/blog/wiz-blue-agent-generally-available
    date: '2026-03-30'
    access: full
    locator: '''From triage to action'''
  - ref: CROWDSTRIKE-AGENTWORKS-2026
    title: How AI-leading Security Teams Are Building the Agentic SOC
    publisher: CrowdStrike
    type: vendor
    url: https://www.crowdstrike.com/en-us/blog/how-ai-leading-security-teams-are-building-the-agentic-soc/
    date: '2026-07-06'
    access: full
    locator: Charlotte Agentic SOAR paragraph
  - ref: ARXIV-2610.09906
    title: Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2610.09906
    date: '2026-10-07'
    access: full
    locator: Abstract
  - ref: ARXIV-2605.24421
    title: 'Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2605.24421
    date: '2026-05-23'
    access: full
    locator: Abstract
  - ref: WRITER-CEREBRO-2026
    title: 'Cerebro: An open source agentic system for security alert triage'
    publisher: WRITER Engineering
    type: firm
    url: https://writer.com/engineering/cerebro-ai-security-alert-triage-system/
    date: '2026-03-23'
    access: full
    locator: '''Human-in-the-Loop Thresholds'''
  last_reviewed: '2026-10-17'
  notes: Vendor capability announcements plus an academic prototype; no named customer using automatic containment found.
```

## 3. Module notes

### Processes and key steps (with work types)

1. **Inventory and exposure discovery** (`data-reporting`, `research-synthesis`): find accounts, assets, internet-facing apps and shadow or "vibe-coded" apps; AI role is perimeter testing and classification (use case 01; `WIZ-OPMODEL-2026` Pillar 1).
2. **Posture assessment and prioritization** (`review-assurance`, `data-reporting`): rank findings by reachability, privilege and data sensitivity (use cases 04, 12).
3. **Ownership and remediation** (`software-systems`, `coordination-scheduling`): map owner, root cause and fix, then ticket or PR (use cases 03, 06).
4. **Preventive guardrails in IaC and pipelines** (`software-systems`): policy-as-code and approved modules, now also for coding agents (use case 07).
5. **Runtime detection, investigation and response** (`transaction-processing`, `expert-judgment`): cloud and Kubernetes alerts, verdicts, containment (use cases 02, 05, 10, 17).
6. **Network and edge policy** (`software-systems`, `review-assurance`): firewall rule hygiene, WAF and virtual patching (use cases 08, 09).
7. **Endpoint detection triage** (`transaction-processing`): label detections true or false positive and auto-close the confident ones (use case 11).
8. **Compliance and continuous authorization** (`review-assurance`, `data-reporting`): evidence and monitoring for FedRAMP-style regimes (use case 13).

### Common pain points

- **Alert noise.** WRITER found about 100 actionable alerts among thousands, a roughly 2% signal rate (`WRITER-CEREBRO-2026`). AWS says customer feedback on individual GuardDuty runtime findings consistently names noise as a major pain point (`AWS-GUARDDUTY-ETD-2026`).
- **Fixing, not finding.** Tamnoon's 2026 State of Cloud Remediation report, as cited on its blog, says critical alerts stay unresolved for 150 days (vendor figure) (`TAMNOON-CORTEX-2026`). AWS says permissions accumulate because "later rarely comes" (`AWS-LEASTPRIV-2026`).
- **Persistent hygiene gaps.** In Datadog's 2025 data, 59% of AWS IAM users had an active access key older than one year, and 49% of EC2 instances enforced IMDSv2; 1% of S3 buckets were effectively public (`DATADOG-SOCS-2025`).
- **Basic weaknesses behind AI-agent incidents.** CERT-In says the weaknesses were ordinary: credentials and keys exposed in code, repositories and configuration, old and test APIs still reachable from the internet, and cloud roles granting broad read and write access (`THN-CERTIN-2026`).
- **Ownership and graph gaps.** WRITER found its infrastructure graph is never complete (missing tags, stale ownership) (`WRITER-CEREBRO-2026`).

### Metrics and benchmarks (with provenance)

| Metric | Value | What it measures | Provenance | Source |
|---|---|---|---|---|
| Agent verdict agreement | about 95.17% | ZS's account of Blue Agent vs analysts over 3 months of parallel investigation | self-reported | `WIZ-ZS-2026` |
| Investigation speed | 80-90% faster; 4x throughput | ZS case-study headlines; baselines not stated | vendor-published | `WIZ-ZS-2026` |
| False-positive investigation time | 75% lower (20-30 min to 5 min) | Owkin case-study headline | vendor-published | `WIZ-OWKIN-2026` |
| Remediation speed | 10x | project44 headline; metric undefined | vendor-published | `WIZ-PROJECT44-2026` |
| Net-new attack sequences | about 1 in 4 prioritized runtime-process sequences | AWS first-week launch data | vendor-published | `AWS-GUARDDUTY-ETD-2026` |
| Findings removed by context | more than half | Wiz Research before/after on high-priority alerts, four risk categories | vendor-published | `WIZ-CLOUDRISK-2026` |
| Externally exposed machines tied to high-impact lateral movement | 30% of observed cloud environments | at least one such machine | vendor-published | `WIZ-CLOUDRISK-2026` |
| Exposures found by Unit 42 Frontier AI Exposure Analysis | 100% of customers assessed; 37% of those rated high or critical | Palo Alto's description; denominators unclear ("more than 100 Unit 42 customer engagements" cited for validation) | vendor-published | `PANW-UNIT42-CFAD-2026` |
| Missed attack alerts, tool-using triage agents | at least 40.4% for every approach tested | 1,247 alerts from one multi-stage scenario in ALERT-BENCH | independent | `ARXIV-2610.10608` |
| Precision, real vs safe code (direct prompting) | 52% to 71%, clustered in the mid-50s | 12 models on 14,822-sample Deception Benchmark | vendor-published | `AWS-DECEPTION-2026` |
| Log-borne prompt injection | persona hijack suppressed 68% of malicious logs (naive classifier); 26.6% to 11.8% average injection success with strongest defense | study with gpt-4o-mini as analyst | independent | `ARXIV-2605.24421` |
| Guardrail proxy | injection recall 25.0% to 94.5% at 0.1% false positives | authors' SOC adversarial corpus, prototype | independent | `ARXIV-2610.09906` |
| Endpoint triage classifier | 82.6% test accuracy | offline, human-labelled Windows detections | vendor-published | `ARXIV-2607.28460` |

### Guardrails and regulatory points

- **US federal.** CISA BOD 26-04, issued 2026-06-10 per CrowdStrike's summary, moves agencies to risk-based remediation using public exposure, KEV status, exploit automatability and technical impact (`CROWDSTRIKE-BOD2604-2026`). CISA's own page could not be opened.
- **Regulator warning on agents.** CERT-In's 2026-10-15 advisory says AI agents under online testing reached live systems and read business records, and no affected organization noticed; it asks organizations to find and rotate exposed credentials, scan every commit for secrets and shut down unused APIs (`THN-CERTIN-2026`).
- **EU sovereignty.** Palo Alto Networks and Deutsche Telekom announced Sovereign Cortex with T Security (2026-06-09), citing GDPR, NIS2 and DORA and offering sovereign controls over data, keys, audited access logs and EU-based support (`PANW-DT-2026`).
- **Public-sector authorization.** Wiz says its agents run inside a FedRAMP High environment and can be set to autonomous or approval mode per workflow (`WIZ-FORGOV-2026`).
- **Shared responsibility for agentic testing.** A fwd:cloudsec Europe talk asks who is responsible when a cloud pentest agent leaves scope (`FWDCLOUDSEC-FAN-2026`).
- **Operating controls practitioners report:** evidence-before-decision rules and approval for IAM and network changes (`WRITER-CEREBRO-2026`); dry-run mode, PR limits and manual review tags (`AWS-LEASTPRIV-2026`); treat "read-only" as insufficient and enforce scope in infrastructure, not prompts (`FWDCLOUDSEC-RAJI-2026`); treat log content as adversarial input (`ARXIV-2605.24421`).

### Frontier signals (dated and sourced)

- 2026-03-25 / 2026-03-30: Wiz Workflows (agentic and deterministic orchestration) and Blue Agent general availability (`WIZ-WORKFLOWS-2026`, `WIZ-BLUEAGENT-GA-2026`).
- 2026-08-03 (page date): Microsoft's Posture Prioritization Agent, read-only, limited public preview (`MSFT-LEARN-PPA-2026`).
- 2026-08-06: Orca groups core agents into Red, Blue and Green pods and offers custom agents and an MCP server (`ORCA-AGENTPODS-2026`).
- 2026-08-19 and 2026-09-22: Palo Alto Networks' Frontier AI Critical Defense Program and Unit 42 Continuous Frontier AI Defense, a subscription service built on gated frontier cyber models (`PANW-FRONTIERCDP-2026`, `PANW-UNIT42-CFAD-2026`).
- 2026-09-01: Wiz Continuous Vulnerability Assessment (public preview), which reassesses exposure when a CVE is published (`WIZ-CVA-2026`).
- 2026-09-08: a fwd:cloudsec Europe talk argues cloud security's build-out phase is over and risk is moving into application code, AI workload pipelines and software supply chains (`FWDCLOUDSEC-GONDA-2026`).
- 2026-09-18: Check Point positions "agentic network security management" for policy audit, AIOps and compliance (`CHECKPOINT-AGENTICNET-2026`).
- 2026-10-05 and 2026-10-14: CrowdStrike AI-enhanced remediation plans; Wiz agents in a FedRAMP High environment (`CROWDSTRIKE-CLOUDREM-2026`, `WIZ-FORGOV-2026`).
- 2026-10-14: AWS shows a per-deploy pentest gate scoped to the change (routed to vulnerability-exposure) (`AWS-CONTINUUM-GATE-2026`).
- Wiz says Forrester named it a Leader in the Proactive Security Platforms Wave (Q3 2026), a category the vendor ties to continuous threat exposure management; this is the vendor's post, not Forrester's report (`WIZ-FORRESTER-2026`).

### Workforce and role effects

- **Exception reviewers.** At ZS, analysts review what the agent closed at end of shift instead of working queues; analysts without deep cloud experience can read agent verdicts (`WIZ-ZS-2026`).
- **Small teams cover large estates.** Owkin (three people, more than 50 AWS accounts) and La Centrale (three people, more than 2,000 Lambda functions) credit graph context and AI-assisted triage (`WIZ-OWKIN-2026`, `WIZ-LACENTRALE-2026`).
- **Platform teams for agents.** Databricks' Agentic Security Engineering team is horizontal shared services across detection and response, threat intelligence, vulnerability management, red team, GRC and continuous monitoring (`DATABRICKS-JOB-AGENTICSEC-2026`).
- **AI skills in postings.** Cloudflare asks vulnerability management engineers to use and integrate AI tools into triage; Pinterest asks for AI use with validation and accountability practices; Block asks for fluency with AI coding tools in production work (`CLOUDFLARE-JOB-VM-2026`, `PINTEREST-JOB-SECOPS-2026`, `BLOCK-JOB-PLATSEC-2026`).
- **From specialists to reviewers of agents.** Engineers become reviewers of agent scope and cost, not only answers (`FWDCLOUDSEC-RAJI-2026`). Some teams use agents to fill missing specialist roles such as cloud identity (`FWDCLOUDSEC-HORSMAN-2026`).
- **Engineering takes more of the fix.** project44 held an engineering-wide enablement session; developers receive pre-populated tickets or PRs (`WIZ-PROJECT44-2026`, `WIZ-OPMODEL-2026`).
- No hard data on junior-analyst hiring or headcount change was found.

### Objections and concerns practitioners raise

- **Read-only is not safe.** Secrets, identity and cost can still go wrong (`FWDCLOUDSEC-RAJI-2026`).
- **Scope and responsibility.** An autonomous pentest agent can cross boundaries; documentation can leave responsibility unclear (`FWDCLOUDSEC-FAN-2026`).
- **Benchmarks and contamination.** AWS says public CVE benchmarks are saturated because models recognize the vulnerabilities, and that its own refreshed benchmark is "contamination-reduced, not contamination-free" (`AWS-SECAGENT-2026`).
- **False alarms.** AWS says single-turn models flag safe code and ignore deployment context, and asks buyers to ask vendors how often a system is wrong (`AWS-DECEPTION-2026`).
- **Attack surface of the defender's AI.** Log fields are attacker-controlled (`ARXIV-2605.24421`); a single adversarial alert could become a remote code path (`ARXIV-2610.09906`).
- **Incomplete context.** Agents reason from a graph that is never complete (`WRITER-CEREBRO-2026`).
- **Backlog growth.** Tamnoon says AI scanning will deepen configuration backlogs (`TAMNOON-CORTEX-2026`; vendor view).
- **Vendor-hosted proof.** Nearly all customer figures in this module are published by the vendor.

### Interview probes for an advisor

1. When a cloud finding is raised, who owns it and how do you know? What share of findings has a confirmed owner today, and where would an agent-drafted ticket or PR go?
2. If an agent investigated your low-severity cloud detections, how long a parallel run and what agreement rate would you need before it closed alerts alone, and who reviews what it closed?
3. What can each of your agents reach (identities, scopes, secrets, cost ceiling)? What happens if a log line or alert field contains instructions?
4. When AI proposes an IAM or network change, where does the fix live (console or infrastructure-as-code), how many reviews a week can your teams absorb, and what is the break-glass path?
5. Which signals do you use to decide a finding matters (internet reachability, privilege, data sensitivity), and have you measured how much that removes from the queue?

## 4. Routed to other modules

- **vulnerability-exposure:** AWS Security Agent captured 33 of 37 recent CVEs end to end (89.2%) in AWS's own contamination-reduced test, with two captures reclassified and two targets taken down (`AWS-SECAGENT-2026`); the AWS per-deploy pentest gate that can block promotion (`AWS-CONTINUUM-GATE-2026`); Wiz Continuous Vulnerability Assessment (`WIZ-CVA-2026`); Unit 42 Continuous Frontier AI Defense (`PANW-UNIT42-CFAD-2026`); BOD 26-04 (`CROWDSTRIKE-BOD2604-2026`); a fwd:cloudsec talk that used an agentic workflow with deterministic integration tests to find over a dozen new AWS IAM privilege-escalation paths (`FWDCLOUDSEC-ART-2026`).
- **application-security:** Google's pre-submit agentic scanning of infrastructure code, with a triage agent reported at over 92% precision in under a minute and an open-source harness called Mantis (`GOOGLE-AGENTICSCAN-2026`); Wiz Red Agent finding a GitHub Actions workflow flaw in a Snowflake repository that GitHub Advanced Security did not flag, disclosed 2026-06-23 and fixed the same day (exploit detail deliberately not recorded) (`WIZ-REDAGENT-SNOWFLAKE-2026`); AWS Deception Benchmark for code-level false alarms (`AWS-DECEPTION-2026`).
- **security-operations:** CrowdStrike Charlotte AI AgentWorks customer quotes from Pegasystems, American Express Global Business Travel, Americas Styrenics and Pan-American Life (`CROWDSTRIKE-AGENTWORKS-2026`); CrowdStrike's three stated reasons agentic SOC efforts fail: fragmented data, isolated agents, ungoverned automation (`CROWDSTRIKE-AGSOC-2026`).
- **incident-response:** Centene's FIRST 2026 session on a six-layer log-to-timeline pipeline over OCSF for hybrid-cloud incident response, held 2026-06-18 (`FIRST-CON-2026`); Wiz's worked multi-cloud investigation spanning GitHub and two AWS accounts (`WIZ-BLUEAGENT-CASE-2026`).
- **identity-access and ai-security:** Brucato's benchmark of 10 models across 599 autonomous attack runs in AWS, with and without cloud canaries (`FWDCLOUDSEC-BRUCATO-2026`); agent identity and authorization talks at fwd:cloudsec (titles only seen); CERT-In (`THN-CERTIN-2026`).
- **ot-critical-infrastructure:** Palo Alto Networks' Frontier AI Critical Defense Program partners, including Siemens, Idaho National Laboratory, Mitsubishi Electric, Axis Communications and EPRI (`PANW-FRONTIERCDP-2026`).
- **data-security-privacy:** the Red Agent's built-in classification and redaction of exposed data (`WIZ-REDAGENT-2026`).
- **security-governance-risk:** sovereign-cloud security operations (`PANW-DT-2026`); AWS's advice to ask vendors for false-alarm rates (`AWS-DECEPTION-2026`).

## 5. Sources

Counts below are distinct sources listed here. Every source was opened and read (`access: full`).

**Totals:** 62 distinct sources. By type: vendor 38, firm 2, conference 10, academic 4, press 1, job-posting 7.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| `AWS-CONTINUUM-GATE-2026` | Penetration testing every deployment with AWS Continuum | AWS Security Blog | vendor | https://aws.amazon.com/blogs/security/penetration-testing-every-deployment-with-aws-continuum/ | 2026-10-14 | full |
| `AWS-DECEPTION-2026` | The state of AI for security: Measuring what matters most for building trust (Deception Benchmark) | AWS Security Blog | vendor | https://aws.amazon.com/blogs/security/the-state-of-ai-for-security-measuring-what-matters-most-for-building-trust/ | 2026-09-09 | full |
| `AWS-GUARDDUTY-ETD-2026` | GuardDuty Extended Threat Detection has added five new indicators to surface attack sequences | AWS Security Blog | vendor | https://aws.amazon.com/blogs/security/guardduty-extended-threat-detection-has-added-five-new-indicators-to-surface-attack-sequences/ | 2026-10-12 | full |
| `AWS-LEASTPRIV-2026` | Operationalizing least privilege: Automate IAM remediation through your CI/CD pipeline | AWS Security Blog | vendor | https://aws.amazon.com/blogs/security/operationalizing-least-privilege-automate-iam-remediation-through-your-ci-cd-pipeline/ | 2026-09-15 | full |
| `AWS-SECAGENT-2026` | AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs | AWS Security Blog | vendor | https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/ | 2026-10-15 | full |
| `CATO-AUTONOMOUSPOL-2026` | Understanding Cato Autonomous Policies (product documentation) | Cato Networks | vendor | https://knowledge.catonetworks.com/docs/understanding-cato-autonomous-policies | 2026-08-27 | full |
| `CHECKPOINT-AGENTICNET-2026` | When Security Operations Can't Keep Up: 4 Ways Agentic Network Security Management Improves Security Operations | Check Point | vendor | https://blog.checkpoint.com/hybrid-mesh/when-security-operations-cant-keep-up-4-ways-agentic-network-security-management-improves-security-operations/ | 2026-09-18 | full |
| `CROWDSTRIKE-AGENTWORKS-2026` | How AI-leading Security Teams Are Building the Agentic SOC | CrowdStrike | vendor | https://www.crowdstrike.com/en-us/blog/how-ai-leading-security-teams-are-building-the-agentic-soc/ | 2026-07-06 | full |
| `CROWDSTRIKE-AGSOC-2026` | CrowdStrike Delivers the Next Evolution of the Agentic SOC | CrowdStrike | vendor | https://www.crowdstrike.com/en-us/blog/crowdstrike-delivers-next-evolution-of-agentic-soc/ | 2026-09-02 | full |
| `CROWDSTRIKE-BOD2604-2026` | CrowdStrike Falcon Platform Helps Meet U.S. Government Mandates for CISA BOD-26-04 | CrowdStrike | vendor | https://www.crowdstrike.com/en-us/blog/crowdstrike-falcon-platform-helps-meet-us-government-mandates-cisa-bod-26-04/ | 2026-07-22 | full |
| `CROWDSTRIKE-CLOUDREM-2026` | New in Falcon Cloud Security: Third-Party App Insights and AI-Enhanced Remediation | CrowdStrike | vendor | https://www.crowdstrike.com/en-us/blog/falcon-cloud-security-third-party-app-insights-ai-enhanced-remedation/ | 2026-10-05 | full |
| `CROWDSTRIKE-TRIAGE-2026` | Teaching AI to Reason Through Detection Triage | CrowdStrike | vendor | https://www.crowdstrike.com/en-us/blog/teaching-ai-to-reason-through-detection-triage/ | 2026-08-17 | full |
| `DATADOG-SOCS-2025` | State of Cloud Security (2025 edition) | Datadog | vendor | https://www.datadoghq.com/state-of-cloud-security/ | 2025-10-08 | full |
| `MSFT-LEARN-PPA-2026` | Posture Prioritization Agent (Project Perception, limited public preview) | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/security/agentic-security/posture-prioritization-agent | 2026-08-03 | full |
| `ORCA-AGENTPODS-2026` | An Inside Look at Orca AI Agent Pods | Orca Security | vendor | https://orca.security/resources/blog/an-inside-look-at-orca-ai-agent-pods/ | 2026-08-06 | full |
| `PANW-DT-2026` | Palo Alto Networks and Deutsche Telekom Bring AI-Driven Security with Advanced Sovereignty Controls for European Regulated Industries | Palo Alto Networks (press release) | vendor | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-and-deutsche-telekom-bring-ai-driven-security-with-advanced-sovereignty-controls-for-european-regulated-industries | 2026-06-09 | full |
| `PANW-FRONTIERCDP-2026` | Palo Alto Networks Introduces Frontier AI Critical Defense Program | Palo Alto Networks (press release) | vendor | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-introduces-frontier-ai-critical-defense-program | 2026-08-19 | full |
| `PANW-LIGHTWELL-2026` | IBM, Red Hat and Palo Alto Networks Expand Project Lightwell to Help Organizations Respond to Software Vulnerabilities | Palo Alto Networks (press release) | vendor | https://www.paloaltonetworks.com/company/press/2026/ibm-red-hat-and-palo-alto-networks-expand-project-lightwell-to-help-organizations-respond-to-software-vulnerabilities | 2026-06-24 | full |
| `PANW-UNIT42-CFAD-2026` | Palo Alto Networks Delivers Anthropic's Mythos and OpenAI's GPT-5.6 to Customers with Unit 42 Continuous Frontier AI Defense | Palo Alto Networks (press release) | vendor | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-delivers-anthropic-s-mythos-and-openai-s-gpt-5-6-to-customers-with-unit-42-continuous-frontier-ai-defense | 2026-09-22 | full |
| `TAMNOON-CORTEX-2026` | CDR and CNAPP Remediation: Fixing Findings Across Cortex Cloud's Unified View | Tamnoon | vendor | https://tamnoon.io/blog/cdr-and-cnapp-remediation/ | 2026-06-22 | full |
| `WIZ-BLUEAGENT-CASE-2026` | How Wiz's Blue Agent Traced a Multi-Cloud Attack | Wiz | vendor | https://www.wiz.io/blog/blue-agent-data-exfiltration-investigation | 2026-09-29 | full |
| `WIZ-BLUEAGENT-GA-2026` | The Wiz Blue Agent, now Generally Available | Wiz | vendor | https://wiz.io/blog/wiz-blue-agent-generally-available | 2026-03-30 | full |
| `WIZ-CLOUDRISK-2026` | Report Recap: State of Cloud Risk 2026 | Wiz | vendor | https://www.wiz.io/blog/cloud-risk-report-2026 | 2026-08-26 | full |
| `WIZ-CVA-2026` | Introducing Continuous Vulnerability Assessment (CVA) | Wiz | vendor | https://www.wiz.io/blog/introducing-cva | 2026-09-01 | full |
| `WIZ-DEFENDGSO-2026` | Wiz Defend & Google Security Operations Integration | Wiz | vendor | https://www.wiz.io/blog/wiz-defend-and-google-security-operations | 2026-09-15 | full |
| `WIZ-FORGOV-2026` | Wiz AI Agents for FedRAMP High: Accelerate Public Sector AI (Securing the Mission at Machine Speed) | Wiz | vendor | https://www.wiz.io/blog/wiz-for-gov-agents-fedramp | 2026-10-14 | full |
| `WIZ-FORRESTER-2026` | Wiz a Leader: Forrester Wave Proactive Security 2026 (vendor post) | Wiz | vendor | https://www.wiz.io/blog/forrester-wave-for-proactive-security-2026 | 2026-09-24 | full |
| `WIZ-LACENTRALE-2026` | From Alert Overload to Developer Ownership: How La Centrale Built a Top-Ranked Cloud Security Culture (customer story; page undated, retrieved 2026-10-17) | Wiz | vendor | https://www.wiz.io/customers/lacentrale | 2026 | full |
| `WIZ-MSP-2026` | Introducing the Wiz Partner Alliance MSP Program | Wiz | vendor | https://www.wiz.io/blog/introducing-wiz-partner-alliance-managed-service-provider-program | 2026-09-28 | full |
| `WIZ-OPMODEL-2026` | Build AI Threat Readiness with Wiz | Wiz | vendor | https://www.wiz.io/blog/wiz-ai-threat-readiness-operating-model | 2026-05-27 | full |
| `WIZ-OWKIN-2026` | How Owkin's lean Security Team Protects AI-Driven Biotech Research at Scale (customer story; page undated, retrieved 2026-10-17) | Wiz | vendor | https://www.wiz.io/customers/owkin | 2026 | full |
| `WIZ-PROJECT44-2026` | project44 Accelerates Cloud Remediation and Security Operations with Wiz AI Agents (customer story; page undated, retrieved 2026-10-17) | Wiz | vendor | https://www.wiz.io/customers/project44 | 2026 | full |
| `WIZ-REDAGENT-2026` | How the Wiz Red Agent caught a Fortune 500 firm's data exposure (that other tools missed) | Wiz | vendor | https://www.wiz.io/blog/red-agent-financial-services-data-exposure | 2026-10-07 | full |
| `WIZ-REDAGENT-SNOWFLAKE-2026` | Red Agent Exploits Snowflake Vuln Missed by Github Copilot | Wiz | vendor | https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug | 2026-08-17 | full |
| `WIZ-REDIS-2026` | Redis Achieves Unified Cloud Security at Scale with AI-Powered Threat Detection (customer story; page undated, retrieved 2026-10-17) | Wiz | vendor | https://www.wiz.io/customers/redis-unified-cloud-security | 2026 | full |
| `WIZ-SCANFORGOOD-2026` | Scan for Good: Finding Critical Exposures with AI | Wiz | vendor | https://www.wiz.io/blog/scan-for-good-critical-ai-exposures | 2026-09-24 | full |
| `WIZ-WORKFLOWS-2026` | Introducing Wiz Workflows: Build a Self-Healing Cloud | Wiz | vendor | https://www.wiz.io/blog/introducing-wiz-workflows | 2026-03-25 | full |
| `WIZ-ZS-2026` | How ZS Operationalized Blue Agent-Powered Cloud Detection and Response (customer story; page undated, retrieved 2026-10-17) | Wiz | vendor | https://www.wiz.io/customers/zs-blue-agent | 2026 | full |
| `GOOGLE-AGENTICSCAN-2026` | Changing the game: Using agentic AI to secure infrastructure code (Using AI agents to secure Google infrastructure) | Google Cloud Blog | firm | https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/ | 2026-09-19 | full |
| `WRITER-CEREBRO-2026` | Cerebro: An open source agentic system for security alert triage | WRITER Engineering | firm | https://writer.com/engineering/cerebro-ai-security-alert-triage-system/ | 2026-03-23 | full |
| `FIRST-CON-2026` | 38th FIRST Conference program (Centene: From Logs to Living Timelines) | FIRST | conference | https://www.first.org/conference/2026/program | 2026-06 | full |
| `FWDCLOUDSEC-ALIM-2026` | The Tireless Guardian: Agentic AI and the Art of WAF at Scale (Ammar Alim) | fwd:cloudsec North America 2026 | conference | https://pretalx.com/fwd-cloudsec-2026/talk/XEMZWB/ | 2026-06-01 | full |
| `FWDCLOUDSEC-ART-2026` | Discovering New AWS Privilege Escalation Paths with an AI-Driven Workflow (Seth Art) | fwd:cloudsec North America 2026 | conference | https://pretalx.com/fwd-cloudsec-2026/talk/Q9NXBS/ | 2026-06-01 | full |
| `FWDCLOUDSEC-BRUCATO-2026` | Lessons from benchmarking AI attackers in AWS (Alessandro Brucato) | fwd:cloudsec Europe 2026 | conference | https://pretalx.com/fwd-cloudsec-europe-2026/talk/ZAWFW7/ | 2026-09-08 | full |
| `FWDCLOUDSEC-FAN-2026` | Whose Fault When a Pentest Agent Attacks the Wrong Target? (Richard Fan) | fwd:cloudsec Europe 2026 | conference | https://pretalx.com/fwd-cloudsec-europe-2026/talk/VWFXZS/ | 2026-09-07 | full |
| `FWDCLOUDSEC-GONDA-2026` | Cloud Security Is Dead. Long Live Infrastructure Security. (Tim Gonda) | fwd:cloudsec Europe 2026 | conference | https://pretalx.com/fwd-cloudsec-europe-2026/talk/M7LSGF/ | 2026-09-08 | full |
| `FWDCLOUDSEC-HORSMAN-2026` | I made AI agents apply for my Security Team. Then I gave the agents access to AWS. (Cole Horsman) | fwd:cloudsec North America 2026 | conference | https://pretalx.com/fwd-cloudsec-2026/talk/RAEUSE/ | 2026-06-01 | full |
| `FWDCLOUDSEC-RAJI-2026` | What We Learned Giving an AI Agent Read Access to Our Whole Kubernetes Fleet (Amine Raji) | fwd:cloudsec Europe 2026 | conference | https://pretalx.com/fwd-cloudsec-europe-2026/talk/TN9SP9/ | 2026-09-08 | full |
| `FWDCLOUDSEC-RENGASAMY-2026` | Agentic Paved Roads: Shifting Security Left to the Machine That Thinks (Prahathess Rengasamy) | fwd:cloudsec North America 2026 | conference | https://pretalx.com/fwd-cloudsec-2026/talk/RDXF3X/ | 2026-06-01 | full |
| `FWDCLOUDSEC-SMOLEN-2026` | Least Privilege is a Conversation: Building an Agentic Role Engineering Pipeline (Alex Smolen) | fwd:cloudsec North America 2026 | conference | https://pretalx.com/fwd-cloudsec-2026/talk/9LRLDS/ | 2026-06-01 | full |
| `ARXIV-2605.24421` | Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content | arXiv | academic | https://arxiv.org/abs/2605.24421 | 2026-05-23 | full |
| `ARXIV-2607.28460` | Cybersecurity Detection Classification with Reasoning-enabled Language Models | arXiv (Khanna et al., CrowdStrike authors) | academic | https://arxiv.org/abs/2607.28460 | 2026-07-30 | full |
| `ARXIV-2610.09906` | Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy | arXiv | academic | https://arxiv.org/abs/2610.09906 | 2026-10-07 | full |
| `ARXIV-2610.10608` | From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage | arXiv | academic | https://arxiv.org/abs/2610.10608 | 2026-10-07 | full |
| `THN-CERTIN-2026` | CERT-In Warns AI Agents Accessed Sensitive Data at Indian Organizations During Testing | The Hacker News | press | https://thehackernews.com/2026/10/cert-in-warns-ai-agents-accessed.html | 2026-10-16 | full |
| `BLOCK-JOB-PLATSEC-2026` | Senior Security Engineer, Platform Security | Block (Greenhouse job board) | job-posting | http://block.xyz/careers/jobs/5231316008?gh_jid=5231316008 | 2026-06-02 | full |
| `CLOUDFLARE-JOB-NETSEC-2026` | Network Security Engineer | Cloudflare (Greenhouse job board) | job-posting | https://boards.greenhouse.io/cloudflare/jobs/8081027?gh_jid=8081027 | 2026-07-24 | full |
| `CLOUDFLARE-JOB-VM-2026` | Vulnerability Management Engineer | Cloudflare (Greenhouse job board) | job-posting | https://boards.greenhouse.io/cloudflare/jobs/7579269?gh_jid=7579269 | 2026-02-05 | full |
| `DATABRICKS-JOB-AGENTICSEC-2026` | Sr. Staff Security Software Engineer - Agentic Security Engineering | Databricks (Greenhouse job board) | job-posting | https://databricks.com/company/careers/open-positions/job?gh_jid=8612865002 | 2026-10-12 | full |
| `PINTEREST-JOB-SECOPS-2026` | Sr. Security Software Engineer, Security Operations | Pinterest (Greenhouse job board) | job-posting | https://www.pinterestcareers.com/jobs/?gh_jid=8230778 | 2026-10-01 | full |
| `ROBINHOOD-JOB-SECENG-2026` | Senior Staff Security Engineer, Security Engineering | Robinhood (Greenhouse job board) | job-posting | https://boards.greenhouse.io/robinhood/jobs/8167616 | 2026-09-01 | full |
| `WIZ-JOB-CLOUDDET-2026` | Threat Detection Researcher (Cloud) | Wiz (Greenhouse job board) | job-posting | https://www.wiz.io/careers/job/4566780006/:title?gh_jid=4566780006 | 2026-08-19 | full |

## 6. Gaps

- **No independent measurement of cloud-security agents.** All customer figures for Wiz, Orca, Palo Alto and CrowdStrike are on vendor-hosted pages; ZS's accuracy is its own validation. The only independent evidence found concerns LLM triage in general (`ARXIV-2610.10608`, `ARXIV-2605.24421`).
- **Endpoint protection.** No named customer outcome. SentinelOne's Aston Martin case page (2026-02-21) is a video page with no results text; an IDC figure on Purple AI was seen only in search results and is not used. Microsoft Defender for Endpoint and CrowdStrike customer outcomes were not reached.
- **Network security.** Cato and Check Point are product documentation and a vendor blog without named customers or results. Cisco, Zscaler, Fortinet and Palo Alto Strata AI features were not reached.
- **Primary vendor docs not reached:** Google Security Command Center AI features and Microsoft Defender for Cloud AI-agent posture pages (including a licensing change on 2026-07-01 and Security Command Center Standard-tier changes) appeared only in search results and are not used for any claim. Datadog's Bits Security Analyst claim (alert investigation cut from hours to about 30 seconds) is search-only and unused.
- **Blocked pages.** CISA (BOD 26-04 and the joint agentic AI guidance listed in the landscape) returned access denied, so BOD 26-04 details come from a vendor summary. Gartner and Forrester research is paywalled; Forrester appears only through Wiz's post.
- **Undated customer pages.** Wiz customer stories carry no publication date; a sitemap shows a bulk last-modified of 2026-10-15, which is not a publication date.
- **Conference coverage.** fwd:cloudsec was scanned from the schedule data by AI-related keyword and only abstracts were read, not recordings. Black Hat and RSAC session lists were not attempted; the landscape file reports they are scripted pages.
- **Job postings.** Only Greenhouse boards were scanned (about 36 company boards); Lever, Workday and other boards were not. Postings show intent, not results.
- **Not covered:** AI for cloud cost or FinOps, Kubernetes runtime vendors such as Sysdig, Orca customer outcomes, and any effect on junior-analyst hiring.
- **Terminology.** The landscape file notes CISA and NIST copies showing "Super Intelligence (SI)" for "AI"; I could not re-check them because CISA denied access.

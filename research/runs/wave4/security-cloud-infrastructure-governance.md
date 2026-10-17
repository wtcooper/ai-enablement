# Security / cloud-infrastructure: governance angle (wave 4)

Compiled 2026-10-17. Archetype `security`, module `cloud-infrastructure` (cloud security posture and workload protection, network security, endpoint protection and infrastructure configuration), angle governance and evidence: what constrains and measures AI use. Sources were opened and read unless marked `search-only`; arXiv items were read at abstract level (stated in each locator).


## 1. Summary

**Counts.** 16 candidate use cases: evidence grade A: 0, B: 0, C: 1, D: 15. Sources: see section 5 (counts by type are in the reply to the caller). No source gives a measured outcome from a named organization using AI for cloud posture, network or endpoint security in production. All grade-D entries are labelled "idea" and rest on academic benchmarks, regulator guidance or both.

**What the evidence says**

1. **Regulators converge on the same short list of controls for AI that touches infrastructure, and none of them is a ban.** CERT-In (2026-10-15) tells organizations to give each agent run a short-lived least-privilege identity, enforce default-deny egress at the network layer, and keep tamper-resistant logs of actions on production (`CERTIN-CIAD0049-2026`). The joint CISA/NSA/ASD/Cyber Centre/NCSC-NZ/NCSC-UK guidance (2026-05-01) asks for human approval of high-impact steps and bars agents from changing their own privileges (`CISA-AGENTIC-2026`). NIST's draft Cyber AI Profile says AI-initiated network changes and privilege use should be gated by human approval or policy checks (`NIST-IR8596-2025`). FINRA lists the same considerations for firms (`FINRA-ROR-2026`).
2. **The unresolved tension is speed against approval.** ENISA (2026-07-07) names an "Authority Gap": human change boards cannot authorise a fix in the minutes available against autonomous exploits, so critical providers may be forced into autonomous patching, with the risk that automated updates break systems (`ENISA-FRONTIER-2026`). The only peer-reviewed evidence on a middle path is PatchWeaver, which cut change-policy violations by about half against a standard toolchain in the authors' Kubernetes tests (`USENIX-PATCHWEAVER-2026`).
3. **The strongest measured evidence is about where AI output cannot be trusted.** In a Terraform study, 83.3% of repairs removed the targeted scanner finding but only 10.4% were clean under a full scan, and human adjudication judged 71.4% of plan-compared real-world repairs deceptive (`ARXIV-2606.26590`). LLM-written IaC had 3.21x to 3.87x the vulnerability density of human-written IaC of the same size (`ARXIV-2608.28021`). Cloud-provider guardrails largely missed log-embedded injections (Azure Prompt Shield detected 1 of 32 payloads, GCP Model Armor none) (`ARXIV-2604.15368`).
4. **Independent baselines for the posture problem exist; independent measures of AI's effect on it do not.** Datadog telemetry shows 59% of AWS IAM users with an active access key older than one year (`DATADOG-CLOUDSEC-2025`). Unit 42 reports preventable gaps contributed to over 90% of its 2025 incidents (`UNIT42-IR-2026`). ENISA found misconfiguration and accidental exposure at 20.7% of the unauthorised-access incidents where an intrusion vector was identified (`ENISA-ETL-2026`). No override rates, false-negative rates in production, parallel-run results or regulator inspection findings on AI cloud-security tools were found.
5. **Law is mostly indirect.** DORA's oversight of 19 designated critical ICT third-party providers (including AWS, Google Cloud and Microsoft entities) governs the cloud layer on which AI tooling runs (`EBA-CTPP-2025`). NIS2 and the EU AI Act set the surrounding duties (`EC-NIS2`, `EC-AIACT-2026`). The AI-specific security material (NIST, CISA and partners, CERT-In, ENISA, CSA) is guidance, not binding rule, as far as the sources show.


## 2. Use cases

```yaml
- id: security-cloud-infrastructure-01
  title: Scanner-verified LLM repair of infrastructure-as-code security findings (idea)
  work_types:
  - software-systems
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: IaC scanners flag cloud misconfigurations before deployment, but fixing each flagged Terraform or Kubernetes file is still manual work (ARXIV-2607.11390).
  solution: An LLM proposes a fix for each scanner finding; tooling re-runs the scanner, checks the provider schema and plan, and escalates to a person when deployment-specific context is missing, rather than returning a plausible but unverified fix (ARXIV-2607.11390, ARXIV-2609.28488).
  outcomes:
  - lever: quality
    description: Verification-guided iterative repair lifts the share of fixes that pass full verification, compared with single-shot repair
    figure: 32-50% (single-shot) vs 68-92% (verification-guided)
    measures: 'share of 630 runs (70 real-world misconfigured Terraform and Kubernetes artifacts, three repair strategies, three LLM families) passing four checks: syntactic validity, target-issue resolution, regression safety, patch minimality'
    provenance: independent
    source_ref: ARXIV-2609.28488
  - lever: quality
    description: A tool-grounded agent with escalation raises scanner-verified fix rates against a one-shot baseline
    figure: 26.6% to 78.4% (Checkov); 44.8% to 72.4% (Trivy)
    measures: scanner-verified fix rate on the combined AWS benchmark of two vulnerable-by-design Terraform repositories, agent versus controlled one-shot baseline
    provenance: independent
    source_ref: ARXIV-2607.11390
  - lever: risk
    description: Scanner-passing repairs overstate real security improvement
    figure: 83.3% targeted-finding removal vs 10.4% full-scanner cleanliness; 71.4% deceptive
    measures: 'for the primary model on 288 first-pass repairs (68 TerraDS modules plus 28 injected-defect modules): share where the targeted Checkov finding disappeared, versus full-scanner cleanliness; 71.4% is the share of plan-compared real-world repairs that human adjudication judged deceptive (pass automated checks, vulnerability remains)'
    provenance: independent
    source_ref: ARXIV-2606.26590
  - lever: risk
    description: Iterative repair can break checks that previously passed
    figure: 13.8% of scenarios (standard detection); 3.3% (strict detection)
    measures: scenarios with at least one previously passing CIS check failing after a repair iteration, out of 5,968 scenario timelines from the IaC-Eval benchmark, up to five iterations each; the authors treat 3.3% as the conservative rate
    provenance: independent
    source_ref: ARXIV-2608.13404
  prerequisites:
  - IaC held in version control with at least one scanner (the studies use Checkov and Trivy) in the pipeline (ARXIV-2607.11390)
  - Provider schema and dependency context available to the repair tool (ARXIV-2607.11390)
  - A non-production plan or apply step to compare behaviour before and after a fix (ARXIV-2606.26590)
  risks_and_guardrails:
  - 'Do not treat disappearance of the targeted finding as success: deceptive fixes and wildcard IAM grants persisted in the TerraProbe sample (ARXIV-2606.26590).'
  - 'Re-run the full scanner after each iteration and cap iterations: iteration 3 was the optimal stopping point in the regression study (ARXIV-2608.13404).'
  - Escalate instead of fabricating a fix when deployment-specific context is missing (ARXIV-2607.11390).
  - The IaC-Guard-V authors found structured prompting consistently reduced Terraform repair quality (ARXIV-2609.28488).
  human_checkpoints:
  - Reviewer approves the plan diff before apply (inferred from the studies' escalation and verification design; no source names an approval step)
  - Person handles every finding the tool escalates (ARXIV-2607.11390)
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: D
  sources:
  - ref: ARXIV-2609.28488
    title: 'IaC-Guard-V: A Verification Framework for LLM-Generated Infrastructure-as-Code Repairs (arXiv preprint, abstract read: arXiv API lists first submission 2026-08-12 although the identifier prefix suggests September)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.28488
    date: '2026-08-12'
    access: full
    locator: abstract
  - ref: ARXIV-2607.11390
    title: 'TerraRepair: A Tool-Grounded LLM Agent for Infrastructure-as-Code Repair (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2607.11390
    date: '2026-07-13'
    access: full
    locator: abstract
  - ref: ARXIV-2606.26590
    title: 'TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2606.26590
    date: '2026-06-25'
    access: full
    locator: abstract
  - ref: ARXIV-2608.13404
    title: Does Fixing Break Security? An Empirical Study of Security Degradation in Iterative LLM-Driven Infrastructure-as-Code Repair (arXiv preprint, abstract read)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2608.13404
    date: '2026-08-13'
    access: full
    locator: abstract
  - ref: ENISA-FRONTIER-2026
    title: ENISA's view on Cybersecurity in the Frontier AI Era
    publisher: ENISA
    type: regulator
    url: https://www.enisa.europa.eu/sites/default/files/2026-07/ENISA%20view%20on%20cybersecurity%20in%20the%20frontier%20AI%20era_en_0.pdf
    date: '2026-07-07'
    access: full
    locator: p.12, 'Talent and human capital'
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments. The models studied are mostly older generations (for example GPT-4o, Claude 3.5 Sonnet), so current performance may differ.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-02
  title: Policy-scanner gate on AI-generated infrastructure code (idea)
  work_types:
  - software-systems
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Developers increasingly use LLMs to write Terraform and other IaC, where one insecure default is provisioned straight into production (ARXIV-2608.28021). Models that produce valid code do not necessarily produce secure code (ARXIV-2608.02672).
  solution: 'Treat AI-written IaC as untrusted input: run it through multiple policy engines (for example Checkov, Trivy, KICS) in the CI/CD pipeline and block or send back failures, instead of relying on prompt wording alone (ARXIV-2608.02672).'
  outcomes:
  - lever: risk
    description: LLM-generated IaC carries more vulnerabilities than human-written IaC of the same size
    figure: 3.21x to 3.87x human baseline (size-matched)
    measures: vulnerability density of 1,196 artifacts from 12 model configurations across 100 deployment scenarios, relative to 634 human-authored templates scanned with the same three policy engines; the authors say the corpus cannot isolate unprompted default posture
    provenance: independent
    source_ref: ARXIV-2608.28021
  - lever: quality
    description: Few generated scripts were secure without scanning
    figure: 7% secure; 17% (GPT-4o) and 8% (Gemini 2.0 Flash) with an explicit secure-code instruction
    measures: share of scripts generated for 89 vulnerable synthetic scenarios that were secure
    provenance: independent
    source_ref: ARXIV-2602.03648
  - lever: quality
    description: Syntactic validity and security compliance are separate properties
    figure: 'WizardCoder-33B: 77.8% validate rate, 0 Checkov compliance; Claude Opus 4: 23.1% Checkov and 92.5% Trivy pass under detailed security prompting'
    measures: pass@5 across 17 AWS Terraform scenarios, seven models, scanners run in a GitLab CI/CD pipeline
    provenance: independent
    source_ref: ARXIV-2608.02672
  - lever: quality
    description: Even editing existing cloud infrastructure code is hard for models
    figure: 34% best-model success
    measures: share of tasks (incremental edits to real AWS CDK repositories) where the best model's change passed the supplied test cases; the model tested was an older generation
    provenance: independent
    source_ref: ARXIV-2606.05249
  prerequisites:
  - A CI/CD pipeline that runs more than one IaC policy scanner on every change (ARXIV-2608.02672)
  - A rule that AI-written changes get the same review as any other change (inferred; no source states it)
  risks_and_guardrails:
  - Prompt engineering alone was insufficient; the authors conclude automated multi-tool scanning stays necessary whatever the model (ARXIV-2608.02672).
  - Scanner agreement varies across tools, so a single scanner pass is weak assurance (ARXIV-2609.28488).
  human_checkpoints:
  - Reviewer sees scanner results alongside the AI-generated change (inferred; no source names a checkpoint)
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: D
  sources:
  - ref: ARXIV-2608.28021
    title: Compared to What? A Human-Anchored Security Benchmark for LLM-Generated Infrastructure-as-Code (arXiv preprint, abstract read)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2608.28021
    date: '2026-08-28'
    access: full
    locator: abstract
  - ref: ARXIV-2602.03648
    title: Can Developers rely on LLMs for Secure IaC Development? (arXiv preprint, abstract read)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2602.03648
    date: '2026-02-03'
    access: full
    locator: abstract
  - ref: ARXIV-2608.02672
    title: 'Security-First Evaluation of Text-to-Terraform: Benchmarking LLMs and SLMs for Secure IaC Generation (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2608.02672
    date: '2026-08-02'
    access: full
    locator: abstract
  - ref: ARXIV-2606.05249
    title: 'SWE-InfraBench: Evaluating Language Models on Cloud Infrastructure Code (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2606.05249
    date: '2026-06-03'
    access: full
    locator: abstract
  - ref: ARXIV-2609.28488
    title: 'IaC-Guard-V: A Verification Framework for LLM-Generated Infrastructure-as-Code Repairs (arXiv preprint, abstract read: arXiv API lists first submission 2026-08-12 although the identifier prefix suggests September)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.28488
    date: '2026-08-12'
    access: full
    locator: abstract
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments. This entry describes a control on AI use rather than an AI defence; it is kept because it is the most measured governance issue in the module.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-03
  title: AI triage of static-analysis and posture findings to cut false positives (idea)
  work_types:
  - review-assurance
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Rule-based IaC analysers over-approximate and produce many false positives, which burden manual inspection (ARXIV-2601.14595). Rule-based CSPM also produces many false positives from limited context (ARXIV-2508.12584).
  solution: Keep the rules for broad coverage and add a model that filters their output. IntelliSA distils an LLM teacher into a small student classifier that removes false positives from IaC findings; a second line of work validates whether a flagged misconfiguration is actually exploitable using automated probes (ARXIV-2601.14595, ARXIV-2508.12584).
  outcomes:
  - lever: quality
    description: Neural filtering of IaC security-smell findings
    figure: F1 83%; outperforms baselines by 7-42%; 60% of smells found while inspecting under 2% of the codebase
    measures: F1 on a human-labelled dataset of 241 security smells in 11,814 lines of real-world IaC, versus two static analysers and three LLM baselines
    provenance: independent
    source_ref: ARXIV-2601.14595
  - lever: quality
    description: Active behavioural probing of CSPM alerts (not LLM-based; adjacent evidence)
    figure: 93% average false-positive reduction
    measures: average reduction in false-positive rate across misconfiguration and vulnerability alerts in a reproducible AWS test setup; the method uses scripted probes, not a language model
    provenance: independent
    source_ref: ARXIV-2508.12584
  prerequisites:
  - An existing scanner or CSPM producing findings to filter
  - Human-labelled findings to train or evaluate the filter (ARXIV-2601.14595)
  risks_and_guardrails:
  - Filtering can hide real findings; the studies report precision-style scores on test sets, not miss rates in production (ARXIV-2601.14595).
  - Probes that test exploitability must not affect the live service; the CSPM study designs probes to avoid impact (ARXIV-2508.12584).
  human_checkpoints:
  - Analyst reviews what the filter suppresses or ranks low (inferred; not stated in the abstracts)
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: D
  sources:
  - ref: ARXIV-2601.14595
    title: 'IntelliSA: An Intelligent Static Analyzer for IaC Security Smell Detection Using Symbolic Rules and Neural Inference (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2601.14595
    date: '2026-01-21'
    access: full
    locator: abstract
  - ref: ARXIV-2508.12584
    title: Reducing False Positives with Active Behavioral Analysis for Cloud Security (arXiv preprint, abstract read)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2508.12584
    date: '2025-08-18'
    access: full
    locator: abstract
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments. The CSPM false-positive figure comes from an adjacent, non-LLM method and is context only.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-04
  title: Topology-aware remediation of Kubernetes posture findings (idea)
  work_types:
  - software-systems
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Patches generated from Kubernetes security posture (KSPM) findings in isolation can break a runtime service dependency the model cannot see, with destructive blast radius (ARXIV-2607.25995). Developers also report persistent misconfigurations across project stages (ARXIV-2609.27030).
  solution: Give the model live cluster context (service call graph, service-account bindings, scanner findings) before it drafts a patch, and validate output against Kubernetes schemas (ARXIV-2607.25995, ARXIV-2609.27030).
  outcomes:
  - lever: quality
    description: Live topology context raises correctness of dependency-sensitive patches
    figure: 11.1% to 78.0%
    measures: topology-dependent patch correctness across 248 trials on a purpose-built 36-deployment, four-namespace test cluster with 31 injectable findings across seven dependency classes
    provenance: independent
    source_ref: ARXIV-2607.25995
  - lever: quality
    description: Schema-guided validation on top of contextual LLM remediation
    figure: 89.06% (best standalone model) to 98.50%
    measures: correction accuracy when remediating misconfigurations taken from 2,662 developer-reported Stack Overflow issues
    provenance: independent
    source_ref: ARXIV-2609.27030
  prerequisites:
  - Live service-mesh or call-graph data and service-account bindings (ARXIV-2607.25995)
  - A scanner producing KSPM findings (the study uses Trivy) (ARXIV-2607.25995)
  risks_and_guardrails:
  - Results come from a synthetic healthcare test cluster and Stack Overflow snippets, not production clusters (ARXIV-2607.25995, ARXIV-2609.27030).
  - Context-free patches can sever call edges and crash downstream callers (ARXIV-2607.25995).
  human_checkpoints:
  - Operator reviews the patch before applying it to a cluster (inferred; the abstracts do not describe a review step)
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: D
  sources:
  - ref: ARXIV-2607.25995
    title: Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches? (arXiv preprint, abstract read)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2607.25995
    date: '2026-07-28'
    access: full
    locator: abstract
  - ref: ARXIV-2609.27030
    title: 'Kubernetes Misconfigurations in the Wild: Taxonomy, Evolution, and Automated Repair with Large Language Models (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.27030
    date: '2026-09-22'
    access: full
    locator: abstract
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-05
  title: AI-derived least-privilege policies for cloud functions and Kubernetes workloads (idea)
  work_types:
  - software-systems
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Developers rely on default settings, so serverless functions and Kubernetes workloads carry excess permissions (ARXIV-2603.25393, ARXIV-2608.26699).
  solution: Static analysis extracts the permissions a function or workload needs, and a fine-tuned or prompted model writes the vendor-specific policy or repaired manifest; KubeGuard also uses runtime logs to refine Roles, NetworkPolicies and Deployments, presented as recommendations for operators to review (ARXIV-2603.25393, ARXIV-2608.26699, ARXIV-2509.04191).
  outcomes:
  - lever: risk
    description: Least-privilege extraction coverage across serverless functions
    figure: 94.8%
    measures: coverage for least-privilege extraction over 8,322 real-world functions across AWS, Google Cloud and Azure
    provenance: independent
    source_ref: ARXIV-2603.25393
  - lever: risk
    description: Capability reduction in Kubernetes manifests
    figure: 54.97% average reduction
    measures: average capability reduction rate on 10 representative Go-based Kubernetes projects; the motivating study found 74.67% of projects lacked capability configuration across three open-source datasets
    provenance: independent
    source_ref: ARXIV-2608.26699
  prerequisites:
  - Access to function code or deployment specs, and runtime logs for the log-driven variant (ARXIV-2603.25393, ARXIV-2509.04191)
  risks_and_guardrails:
  - Over-trimmed permissions can break workloads; KubeGuard frames its output as recommendations that users review and adopt (ARXIV-2509.04191).
  - ALPS adds real-time monitoring to block unauthorised access and adapt to code changes (ARXIV-2603.25393).
  human_checkpoints:
  - Developer or operator reviews and adopts the recommended policy or manifest (ARXIV-2509.04191)
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: D
  sources:
  - ref: ARXIV-2603.25393
    title: 'ALPS: Automated Least-Privilege Enforcement for Securing Serverless Functions (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2603.25393
    date: '2026-03-26'
    access: full
    locator: abstract
  - ref: ARXIV-2608.26699
    title: 'KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2608.26699
    date: '2026-08-27'
    access: full
    locator: abstract
  - ref: ARXIV-2509.04191
    title: 'KubeGuard: LLM-Assisted Kubernetes Hardening via Configuration Files and Runtime Logs Analysis (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2509.04191
    date: '2025-09-04'
    access: full
    locator: abstract
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments. KubeGuard reports precision, recall and F1 as ''high'' in its abstract without figures, so none are recorded.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-06
  title: Policy-bounded autonomous remediation under change management (idea)
  work_types:
  - software-systems
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: Remediation workflows are bound by maintenance windows, staged rollouts, blast-radius limits and approval gates; scripted playbooks are safe but rigid, while LLM agents are flexible but often violate those rules (USENIX-PATCHWEAVER-2026). ENISA says human Change Advisory Boards cannot authorise interventions in the minutes available against autonomous exploits (ENISA-FRONTIER-2026).
  solution: Encode change rules as executable policy and have the agent score candidate remediation plans for progress and policy-violation risk before acting, replanning when reality diverges (USENIX-PATCHWEAVER-2026). ENISA notes critical service providers may be forced to use autonomous patching, at the cost of risk of automated updates breaking systems (ENISA-FRONTIER-2026).
  outcomes:
  - lever: risk
    description: Fewer policy violations than a standard toolchain baseline
    figure: 4.73% vs 9.95% step-level violations (52.5% fewer)
    measures: step-level change-policy violations across four Kubernetes remediation workloads, versus a Gatekeeper + Argo Rollouts + Cosign baseline
    provenance: independent
    source_ref: USENIX-PATCHWEAVER-2026
  - lever: risk
    description: Fewer worst-case violations than an LLM-agent baseline
    figure: 16.8% vs 51.3% (p99 episode violations); 79.1% fewer step violations
    measures: p99 episode-level policy violations over the same four workloads, versus an LLM-agent baseline
    provenance: independent
    source_ref: USENIX-PATCHWEAVER-2026
  prerequisites:
  - A continuously refreshed graph of Kubernetes assets, dependencies, identities, vulnerabilities, approvals and evidence (USENIX-PATCHWEAVER-2026)
  - Change rules expressed as executable predicates (USENIX-PATCHWEAVER-2026)
  - Tools to check AI-generated patches quickly without introducing new bugs (ENISA-FRONTIER-2026, p.11)
  risks_and_guardrails:
  - Autonomous patching risks outages; verifying AI-generated patches may become a bottleneck (ENISA-FRONTIER-2026, p.11).
  - FINRA lists human-in-the-loop points, tracking of agent actions and guardrails limiting agent behaviour as considerations for agents (FINRA-ROR-2026).
  - Joint agency guidance recommends consensus controls by risk, with human approval added for high-stakes actions (CISA-AGENTIC-2026, PDF p.18).
  - The evaluation covers four Kubernetes workloads in the authors' own setup; no production result is reported (USENIX-PATCHWEAVER-2026).
  human_checkpoints:
  - High-impact or irreversible actions go to a person (CISA-AGENTIC-2026, PDF pp.15 and 18)
  - PatchWeaver separates immediate blocks from escalations (11.0% of security stress-test events were escalations, 88.7% immediate blocks) (USENIX-PATCHWEAVER-2026)
  role_evolution: ENISA asks for human-gated AI workflows and upskilling the security workforce (ENISA-FRONTIER-2026, p.6). No source gives an evidenced change to named roles.
  evidence_grade: D
  sources:
  - ref: USENIX-PATCHWEAVER-2026
    title: 'PatchWeaver: Risk-Bounded Autonomous Vulnerability Remediation Under Change-Management Policies (USENIX Security ''26)'
    publisher: USENIX Association
    type: academic
    url: https://www.usenix.org/conference/usenixsecurity26/presentation/li-rui
    date: 2026-08
    access: full
    locator: abstract
  - ref: ENISA-FRONTIER-2026
    title: ENISA's view on Cybersecurity in the Frontier AI Era
    publisher: ENISA
    type: regulator
    url: https://www.enisa.europa.eu/sites/default/files/2026-07/ENISA%20view%20on%20cybersecurity%20in%20the%20frontier%20AI%20era_en_0.pdf
    date: '2026-07-07'
    access: full
    locator: pp.6, 8-9 ('Authority Gap'), 11
  - ref: FINRA-ROR-2026
    title: '2026 FINRA Annual Regulatory Oversight Report: GenAI section (incl. AI agents) and Cybersecurity section'
    publisher: FINRA
    type: regulator
    url: https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai
    date: '2025-12-09'
    access: full
    locator: 'GenAI section, ''Emerging Trends in GenAI: Agents'''
  - ref: CISA-AGENTIC-2026
    title: Careful Adoption of Agentic AI Services (joint guidance; read via the NCSC-NZ copy of the PDF and the Canadian Cyber Centre notice)
    publisher: CISA, NSA, ASD's ACSC, Canadian Cyber Centre, NCSC-NZ, NCSC-UK
    type: regulator
    url: https://www.ncsc.govt.nz/assets/guidance/Documents/Careful-adoption-of-agentic-AI-services_FINAL.pdf
    date: '2026-05-01'
    access: full
    locator: '''Oversight mechanisms'' best practices (PDF p.15); ''Operating agentic AI securely'' (PDF p.18)'
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments. Peer-reviewed (USENIX Security ''26); the single author affiliation is a small firm (Dawn Computing).'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-07
  title: Agent-based configuration drift detection and IaC reconciliation (idea)
  work_types:
  - software-systems
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: When consoles, CLIs and SDKs are used alongside IaC, deployed systems drift from the IaC specification and later IaC runs may undo valid changes (ARXIV-2510.20211, ARXIV-2603.02345). NIST lists configuration drift management among defensive AI opportunities (NIST-IR8596-2025).
  solution: Agents read API traces or telemetry to detect out-of-band change and propose updates to the IaC program; RIVA adds a verifier agent and cross-validation so wrong tool outputs do not cause missed drift or false alarms (ARXIV-2510.20211, ARXIV-2603.02345).
  outcomes:
  - lever: quality
    description: Drift reconciliation accuracy
    figure: 0.71 to 0.97 (pass@3)
    measures: pass@3 on 372 injected drift scenarios across five real-world Terraform projects, NSync versus a baseline
    provenance: independent
    source_ref: ARXIV-2510.20211
  - lever: quality
    description: Drift detection accuracy when tools return wrong outputs
    figure: 27.3% to 50.0% (with erroneous tool responses); 28% to 43.8% (without)
    measures: task accuracy on the AIOpsLab benchmark, RIVA versus a baseline ReAct agent
    provenance: independent
    source_ref: ARXIV-2603.02345
  prerequisites:
  - IaC as source of truth, and API-trace or telemetry access (ARXIV-2510.20211)
  risks_and_guardrails:
  - Agents cannot tell a broken tool from a real infrastructure problem unless outputs are cross-checked (ARXIV-2603.02345).
  - NIST's draft profile asks organizations to evaluate continuously whether AI defence capabilities are mature enough (NIST-IR8596-2025, section 2.1.2, p.12).
  human_checkpoints:
  - Engineer reviews proposed IaC updates before merge (inferred; not described in the abstracts)
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: D
  sources:
  - ref: ARXIV-2510.20211
    title: Automated Cloud Infrastructure-as-Code Reconciliation with AI Agents (NSync) (arXiv preprint, abstract read)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2510.20211
    date: '2025-10-23'
    access: full
    locator: abstract
  - ref: ARXIV-2603.02345
    title: 'RIVA: Leveraging LLM Agents for Reliable Configuration Drift Detection (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2603.02345
    date: '2026-03-02'
    access: full
    locator: abstract
  - ref: NIST-IR8596-2025
    title: 'NIST IR 8596 (initial preliminary draft): Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile)'
    publisher: NIST
    type: standard-setter
    url: https://csrc.nist.gov/pubs/ir/8596/iprd
    date: '2025-12-16'
    access: full
    locator: 'section 2.1.2 (Defend), ''Mission assurance: configuration management'', pp.10-12'
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-08
  title: Intent-to-network-policy generation with verify-then-act checks (idea)
  work_types:
  - software-systems
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Network policy is large and heterogeneous, so manual management is impractical; LLMs translate intent well but miss policy violations when not grounded in topology (ARXIV-2609.21103).
  solution: A model translates operator intent into network configuration; a separate layer retrieves live network facts and checks each proposed intent against existing security policy before approval (ARXIV-2609.21103). NIST's draft profile says AI-initiated network changes and privilege use should be gated by human approval or policy-based checks (NIST-IR8596-2025, PR.IR-01).
  outcomes:
  - lever: quality
    description: Grounded verification lowers missed policy violations
    figure: over 30% lower false-negative rate
    measures: false-negative rate when checking whether a proposed intent violates an existing security policy, versus ungrounded baselines, on a 2,224-sample synthetic benchmark of campus, enterprise and WAN topologies
    provenance: independent
    source_ref: ARXIV-2609.21103
  prerequisites:
  - A live, queryable model of network topology and group hierarchy (ARXIV-2609.21103)
  risks_and_guardrails:
  - Fine-tuned LLMs showed false negatives in policy-violation checks; the root cause was lack of persistent grounding in topology (ARXIV-2609.21103).
  - Gate AI-initiated network changes with human approval or policy checks (NIST-IR8596-2025, PR.IR-01 'Defend' column).
  human_checkpoints:
  - Human approval or policy-based check before an AI-initiated network change (NIST-IR8596-2025, PR.IR-01)
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: D
  sources:
  - ref: ARXIV-2609.21103
    title: 'NetInspector: Measuring and Improving LLM Capabilities for Reliable Intent-Based Networking Policy Generation (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.21103
    date: '2026-09-17'
    access: full
    locator: abstract
  - ref: NIST-IR8596-2025
    title: 'NIST IR 8596 (initial preliminary draft): Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile)'
    publisher: NIST
    type: standard-setter
    url: https://csrc.nist.gov/pubs/ir/8596/iprd
    date: '2025-12-16'
    access: full
    locator: Profile table, PR.IR-01, Defend column
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments. Benchmark is synthetic.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-09
  title: Evidence-grounded AI investigation of cloud security incidents (idea)
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: Investigators must reconstruct what happened in a compromised cloud host or network from alerts, disk artefacts and logs; existing benchmarks mostly cover pre-compromise settings (ARXIV-2607.26791).
  solution: Agents investigate cloud telemetry or host snapshots, produce a forensic report and remediation plan, and are scored on whether they find silent intrusions rather than only repeating alerts; Holmes adds auditable evidence packs for DDoS investigation (ARXIV-2604.12040, ARXIV-2607.26791, ARXIV-2601.14601).
  outcomes:
  - lever: quality
    description: Authors' own agent on an incident-response benchmark
    figure: 97.1% true-positive detection; 73.4% false-positive rejection; 5.67 novel key findings per case
    measures: results of the authors' SIR agent on 794 test cases derived from 129 anonymised incident patterns replayed in controlled cloud environments, judged by an adversarial LLM-as-judge
    provenance: independent
    source_ref: ARXIV-2604.12040
  - lever: quality
    description: Frontier models on post-compromise investigation
    figure: no model achieved complete detection and remediation on any single range
    measures: 23 frontier LLMs evaluated on 10 cyber ranges built from compromised cloud hosts; agents found alert-exposed problems but struggled with silent intrusions and verified remediation plans
    provenance: independent
    source_ref: ARXIV-2607.26791
  - lever: quality
    description: Prompt-injection screening before cloud-log analysis
    figure: precision, recall and F1 above 93%
    measures: PromptShield scores under attack conditions on real-world AWS and Azure datasets
    provenance: independent
    source_ref: ARXIV-2604.03912
  prerequisites:
  - Forensic-grade cloud logs and disk snapshots (ARXIV-2607.26791)
  - Controlled replay environments to test agents before production (ARXIV-2604.12040)
  risks_and_guardrails:
  - Untrusted log content can steer an agent; see use case 11 (ARXIV-2604.15368).
  - Auditable evidence anchors make failures easier to localise (ARXIV-2601.14601).
  human_checkpoints:
  - Investigator validates findings; the benchmark's judge demands concrete forensic evidence before crediting an investigation (ARXIV-2604.12040)
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: D
  sources:
  - ref: ARXIV-2604.12040
    title: 'SIR-Bench: Evaluating Investigation Depth in Security Incident Response Agents (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2604.12040
    date: '2026-04-13'
    access: full
    locator: abstract
  - ref: ARXIV-2607.26791
    title: 'SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2607.26791
    date: '2026-07-29'
    access: full
    locator: abstract
  - ref: ARXIV-2604.03912
    title: Automating Cloud Security and Forensics Through a Secure-by-Design Generative AI Framework (arXiv preprint, abstract read)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2604.03912
    date: '2026-04-05'
    access: full
    locator: abstract
  - ref: ARXIV-2601.14601
    title: 'Holmes: An Evidence-Grounded LLM Agent for Auditable DDoS Investigation in Cloud Networks (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2601.14601
    date: '2026-01-21'
    access: full
    locator: abstract
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments. Overlaps the incident-response module; kept here for its cloud-specific benchmarks.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-10
  title: LLM agents that tune endpoint detection and response policy (idea)
  work_types:
  - software-systems
  - expert-judgment
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: Commercial EDR has shifted from operator-configured rules to systems with autonomous AI components, so a defence agent tuning EDR is acting on a black box that can change its own behaviour (ARXIV-2606.08168).
  solution: An LLM agent selects EDR hardening actions from a finite, tool-enforced catalogue; the architecture bounds the agent's choices and is evaluated against attack-graph data and, in a separate framework, against a commercial EDR and an autonomous pentester in a lab (ARXIV-2605.03034, ARXIV-2606.08168).
  outcomes:
  - lever: risk
    description: Lower attacker expected payoff versus a greedy baseline
    figure: 59% reduction
    measures: reduction in the attacker's expected payoff (game value) for a tool-mediated Claude Sonnet 4 controller versus a deterministic greedy baseline on paired offensive and defensive telemetry, zero variance across 40 runs; a smaller model converged to worse values but stayed within the action catalogue
    provenance: independent
    source_ref: ARXIV-2605.03034
  prerequisites:
  - EDR telemetry that supports per-policy attribution, separating agent actions from the EDR's own autonomous actions (ARXIV-2606.08168)
  risks_and_guardrails:
  - Commercial EDR telemetry is built for analyst workflows, not benchmarking, and the EDR's autonomous behaviour varied during evaluation (ARXIV-2606.08168).
  - Constrain agent choices to a finite catalogue enforced at the tool-output interface (ARXIV-2605.03034).
  human_checkpoints:
  - Not described in the sources
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: D
  sources:
  - ref: ARXIV-2605.03034
    title: 'Stable Agentic Control: Tool-Mediated LLM Architecture for Autonomous Cyber Defense (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2605.03034
    date: '2026-05-04'
    access: full
    locator: abstract
  - ref: ARXIV-2606.08168
    title: 'Closing the Sim-to-Real Gap: An Evaluation Framework for Autonomous Cyber Defense Configuration of Commercial EDR (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2606.08168
    date: '2026-06-06'
    access: full
    locator: abstract
  - ref: AVC-EPR-2026
    title: Endpoint Prevention & Response (EPR) Test 2026
    publisher: AV-Comparatives
    type: survey
    url: https://av-comparatives.org/tests/endpoint-prevention-response-epr-test-2026/
    date: '2026-09-15'
    access: full
    locator: Introduction (independent endpoint test context; no AI attribution)
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments. AV-Comparatives'' 2026 EPR test (50 targeted attack scenarios, 14 enterprise products, 11 certified) measures endpoint products independently but does not attribute results to AI components, so it is context, not an outcome for this use case.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-11
  title: Operations agents that read cloud telemetry and run fixes, with telemetry sanitisation (idea)
  work_types:
  - software-systems
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: AIOps solutions increasingly use autonomous LLM agents to read telemetry, diagnose incidents and take corrective action with minimal human intervention (USENIX-AIOPSDOOM-2026). Attackers who can influence logs can steer those agents (ARXIV-2604.15368, ARXIV-2607.14493).
  solution: Run diagnosis and remediation agents only behind input sanitisation, layered filtering and output validation, and with command execution restricted; AIOpsShield sanitises structured telemetry and layered defences cut log-injection success in the lab (USENIX-AIOPSDOOM-2026, ARXIV-2607.14493).
  outcomes:
  - lever: risk
    description: Cloud-log injection against LLM debugging agents
    figure: 0% (Claude Sonnet 4.6) to 86.2% (Llama 3.3 70B) verbatim command execution
    measures: share of runs in which the agent executed an injected command verbatim, active condition, 8 models, 32 attack payloads, n=160 per model; remote code execution via a piped shell download succeeded on 6 of 8 models
    provenance: independent
    source_ref: ARXIV-2604.15368
  - lever: risk
    description: Cloud-provider guardrails against log-embedded injection
    figure: Azure Prompt Shield detected 1 of 32 payloads; GCP Model Armor detected none
    measures: payloads detected in log context, although the same payloads were detected in isolation
    provenance: independent
    source_ref: ARXIV-2604.15368
  - lever: risk
    description: Passive prompt injection in network-log analysis
    figure: up to 88.2% attack success (83.4% average); 90.4% reduction with layered defences, 8.4% residual
    measures: attack success rate on a benchmark of 12,847 log entries (2,569 adversarial) across three production LLMs and four attack objectives; reduction from input filtering, prompt hardening and output validation combined
    provenance: independent
    source_ref: ARXIV-2607.14493
  prerequisites:
  - Structured telemetry where user-controlled content can be isolated (USENIX-AIOPSDOOM-2026)
  - Restricted execution rights for the agent (ARXIV-2604.15368)
  risks_and_guardrails:
  - Telemetry manipulation can mislead AIOps agents into actions that compromise infrastructure integrity; the authors' AIOpsShield blocked their attacks without hurting normal agent performance in their experiments (USENIX-AIOPSDOOM-2026).
  - Passive instructions such as 'do not execute fixes' reduced most models to 0% but one still executed 30.0% (ARXIV-2604.15368).
  - Residual vulnerability persists after layered defences, so human oversight for security-critical decisions remains (ARXIV-2607.14493).
  human_checkpoints:
  - Human oversight of security-critical decisions (ARXIV-2607.14493)
  - Human approval for high-stakes agent actions (CISA-AGENTIC-2026, PDF p.18)
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: D
  sources:
  - ref: USENIX-AIOPSDOOM-2026
    title: 'When AIOps Become ''AI Oops'': Subverting LLM-driven IT Operations via Telemetry Manipulation (USENIX Security ''26)'
    publisher: USENIX Association
    type: academic
    url: https://www.usenix.org/conference/usenixsecurity26/presentation/pasquini
    date: 2026-08
    access: full
    locator: abstract
  - ref: ARXIV-2604.15368
    title: 'LogJack: Indirect Prompt Injection Through Cloud Logs Against LLM Debugging Agents (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2604.15368
    date: '2026-04-15'
    access: full
    locator: abstract
  - ref: ARXIV-2607.14493
    title: 'Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation (also in the USENIX Security ''26 program) (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2607.14493
    date: '2026-07-16'
    access: full
    locator: abstract
  - ref: CISA-AGENTIC-2026
    title: Careful Adoption of Agentic AI Services (joint guidance; read via the NCSC-NZ copy of the PDF and the Canadian Cyber Centre notice)
    publisher: CISA, NSA, ASD's ACSC, Canadian Cyber Centre, NCSC-NZ, NCSC-UK
    type: regulator
    url: https://www.ncsc.govt.nz/assets/guidance/Documents/Careful-adoption-of-agentic-AI-services_FINAL.pdf
    date: '2026-05-01'
    access: full
    locator: '''Operating agentic AI securely'' (PDF p.18)'
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments. Several results are attack-side measurements; they are recorded because they set the guardrail requirements for the use case.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-12
  title: LLM-drafted policy-as-code and compliance checks for cloud controls (idea)
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - document-production
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Policy-as-code adoption is hindered by the complexity of policy languages and the risk of misconfiguration (ARXIV-2507.10584). Financial firms must show cloud controls under PCI DSS v4.0 and DORA, which the CSA survey links to growth in CSPM use (CSA-FSCLOUD-2026).
  solution: A model turns natural-language policy into executable Rego, tests it, and checks or corrects Terraform against it; NIST's draft profile lists automated policy enforcement and compliance assessment, including FedRAMP-type regimes, among defensive AI opportunities (ARXIV-2507.10584, ARXIV-2603.15799, NIST-IR8596-2025).
  outcomes:
  - lever: quality
    description: Natural-language access policy to executable Rego
    figure: 95.3% compile rate; 82.2% positive-test and 98.9% negative-test pass
    measures: compile rate for accepted policies and automated test pass rates on the ACRE dataset
    provenance: independent
    source_ref: ARXIV-2603.15799
  prerequisites:
  - Policy engine and test harness (OPA/Rego in the studies) (ARXIV-2603.15799)
  risks_and_guardrails:
  - The tools lint, compile and generate tests to bound unreliable policy text, with auditability as a design aim (ARXIV-2603.15799).
  - FedRAMP's AI prioritisation criteria (2025-2026) required that model information from training on customer data not leave the customer environment without customer authorization (FEDRAMP-AI-2026); this governs AI services bought by agencies, not security tooling.
  human_checkpoints:
  - Policy owner approves generated rules before enforcement (inferred; not stated)
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: D
  sources:
  - ref: ARXIV-2507.10584
    title: 'ARPaCCino: An Agentic-RAG for Policy as Code Compliance (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2507.10584
    date: '2025-07-11'
    access: full
    locator: abstract
  - ref: ARXIV-2603.15799
    title: 'Prose2Policy (P2P): A Practical LLM Pipeline for Translating Natural-Language Access Policies into Executable Rego (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2603.15799
    date: '2026-03-16'
    access: full
    locator: abstract
  - ref: NIST-IR8596-2025
    title: 'NIST IR 8596 (initial preliminary draft): Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile)'
    publisher: NIST
    type: standard-setter
    url: https://csrc.nist.gov/pubs/ir/8596/iprd
    date: '2025-12-16'
    access: full
    locator: section 2.1.2 (Defend), 'Mission assurance', pp.10-11
  - ref: CSA-FSCLOUD-2026
    title: State of Cloud and AI for Financial Services, 2026 Industry Survey Report (340 respondents; marked 'Unofficial AI-assisted Research')
    publisher: Cloud Security Alliance (CSAI Foundation)
    type: survey
    url: https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/state-of-cloud-and-ai-for-financial-services-2026-v1.pdf
    date: '2026-03-31'
    access: full
    locator: 'PDF p.11, ''Security Posture: Tools, Risks, and Priorities'''
  - ref: FEDRAMP-AI-2026
    title: FedRAMP AI prioritization page (initiative Aug 2025 to Apr 2026; page undated, month taken from its text)
    publisher: FedRAMP (US GSA)
    type: regulator
    url: https://www.fedramp.gov/ai/
    date: 2026-04
    access: full
    locator: criteria list
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments. ARPaCCino reports no figures in its abstract.'
  archetype: security
  module: cloud-infrastructure
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-13
  title: AI discovery of exposed credentials and the resources they open (idea)
  work_types:
  - review-assurance
  - research-synthesis
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: Regex scanners work on well-formatted code but miss credentials in emails, chat threads and tickets and do not say what the credential unlocks (ARXIV-2607.09011). CERT-In found AI agents re-using credentials left exposed in configuration, public repositories and permissive cloud roles (CERTIN-CIAD0049-2026).
  solution: A detection agent favouring recall and a review agent removing false positives extract each secret together with the account, endpoint or cloud resource it opens, plus evidence (ARXIV-2607.09011).
  outcomes:
  - lever: quality
    description: Recall against a regex scanner, and speed against analysts
    figure: more than 3x the recall at matched precision; 5 to 17 times faster than 13 analysts
    measures: results on synthetic benchmarks spanning 23 secret types; multi-agent versus single-agent precision gains of up to 16 percentage points on door extraction
    provenance: independent
    source_ref: ARXIV-2607.09011
  prerequisites:
  - Access to unstructured documents (mail, chat, tickets, notes) with appropriate approval
  risks_and_guardrails:
  - Evaluation used synthetic data because real credential data is sensitive; real-world performance is untested (ARXIV-2607.09011).
  - CERT-In asks organizations to rotate any exposed credential, purge it from history and verify the fix from outside (CERTIN-CIAD0049-2026).
  human_checkpoints:
  - Responders triage and remediate each finding (ARXIV-2607.09011)
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: D
  sources:
  - ref: ARXIV-2607.09011
    title: 'Secret Scanner Agent: Extracting Secrets and Access Context from Unstructured Documents (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2607.09011
    date: '2026-07-10'
    access: full
    locator: abstract
  - ref: CERTIN-CIAD0049-2026
    title: 'CERT-In Advisory CIAD-2026-0049: AI Agents as Attack Vectors (agents under evaluation; misuse of open-source agentic AI tools)'
    publisher: CERT-In (India)
    type: regulator
    url: https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2026-0049&pageid=PUBVLNOTES02
    date: '2026-10-15'
    access: full
    locator: '''The weaknesses exploited are conventional''; Recommended Actions B'
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-14
  title: Autonomous exploit validation against cloud-hosted services before release
  work_types:
  - review-assurance
  - software-systems
  pattern: full-population-testing
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Pen tests and quarterly scans cannot keep pace with disclosure volume; CSA describes the constraint moving from finding flaws to absorbing them (CSA-FRC-2026).
  solution: AWS describes an autonomous penetration-testing agent that maps a target, raises candidate risks, validates them, builds and runs an exploit, and has every capture audited against a reference exploit (AWS-SECAGENT-2026).
  outcomes:
  - lever: quality
    description: Self-run test on recent CVEs packaged as live containerised targets
    figure: 33 of 37 (89.2%) captured through the intended vulnerability
    measures: CVEs from 2025-2026 run once with a 10-hour limit per sample; 35 of 37 flags captured, 2 reclassified as off the intended path after audit, 2 misses where the agent took the target down; median time to capture about 4 hours; AWS calls the result contamination-reduced, not contamination-free
    provenance: vendor-published
    source_ref: AWS-SECAGENT-2026
  prerequisites:
  - An isolated sandbox target; the agent starts from an endpoint and a one-line hint (AWS-SECAGENT-2026)
  risks_and_guardrails:
  - In both misses the agent took the target down before reading the flag; AWS says non-destructive guardrails for production engagements are meant to prevent that (AWS-SECAGENT-2026).
  - AWS says public CVE benchmarks saturate as models memorise write-ups (AWS-SECAGENT-2026).
  - UK NCSC and ENISA both expect disclosure volume to rise and tell organizations to prioritise external attack surfaces (NCSC-PATCHWAVE-2026, ENISA-FRONTIER-2026).
  human_checkpoints:
  - Per-sample integrity audit by hand and tooling (AWS-SECAGENT-2026)
  role_evolution: No source describes a role change for this use. ENISA says humans will still need to understand the environments they are responsible for (ENISA-FRONTIER-2026, p.12).
  evidence_grade: C
  sources:
  - ref: AWS-SECAGENT-2026
    title: AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs
    publisher: AWS Security Blog
    type: vendor
    url: https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/
    date: '2026-10-15'
    access: full
    locator: '''The numbers'' table; ''Why we built a fresh benchmark'''
  - ref: CSA-FRC-2026
    title: Frontier Ready Cybersecurity initiative hub (AI Vulnerability Storm; undated page, retrieval date)
    publisher: Cloud Security Alliance (CSAI Foundation)
    type: standard-setter
    url: https://cloudsecurityalliance.org/csai-foundation/frontier-ready-cybersecurity
    date: '2026-10-17'
    access: full
    locator: '''The milestone'' section'
  - ref: NCSC-PATCHWAVE-2026
    title: Preparing for a 'vulnerability patch wave'
    publisher: UK National Cyber Security Centre
    type: regulator
    url: https://www.ncsc.gov.uk/blogs/prepare-for-vulnerability-patch-wave
    date: '2026-05-01'
    access: full
    locator: '''Prioritise external attack surfaces'''
  - ref: ENISA-FRONTIER-2026
    title: ENISA's view on Cybersecurity in the Frontier AI Era
    publisher: ENISA
    type: regulator
    url: https://www.enisa.europa.eu/sites/default/files/2026-07/ENISA%20view%20on%20cybersecurity%20in%20the%20frontier%20AI%20era_en_0.pdf
    date: '2026-07-07'
    access: full
    locator: pp.7-9
  notes: 'Grade C: a vendor''s own benchmark. The targets are web applications and platforms, not cloud configuration, so the evidence is adjacent to this module and capped. Primary home is vulnerability-exposure; see the routing section.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-15
  title: Containment controls for AI agents that operate on cloud and Kubernetes infrastructure (idea)
  work_types:
  - software-systems
  - review-assurance
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: Agents reached live systems of Indian organizations through exposed credentials and over-permissive cloud roles, and none of the organizations detected it (CERTIN-CIAD0049-2026). Agents with write access to production change the state of clusters and can be redirected by content they read (ARXIV-2610.02861).
  solution: Regulators recommend short-lived least-privilege identity per agent run, default-deny network egress enforced in the network (not by instructions to the model), tamper-resistant logs of actions that touch production, human approval for high-impact steps, and override or emergency shutdown (CERTIN-CIAD0049-2026, CERTIN-BLUEPRINT-2026, CISA-AGENTIC-2026). One preprint maps this to Kubernetes mechanisms including workload identity, admission policy, sandboxing, egress policy and an agent gateway (ARXIV-2610.02861).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: The Kubernetes framework preprint reports no measured attack-success or overhead figures; regulator documents give recommendations, not measured results
    provenance: independent
    source_ref: ARXIV-2610.02861
  prerequisites:
  - Per-run workload identity and a policy point at the tool boundary (ARXIV-2610.02861)
  - Network egress control at the infrastructure layer (CERTIN-CIAD0049-2026)
  - An inventory of the agents running, since 82% of surveyed organizations found previously unknown agents (CSA-UNKNOWNAGENTS-2026)
  risks_and_guardrails:
  - Do not treat the model as a security boundary; assume the agent may be compromised by prompt injection (ARXIV-2610.02861).
  - Prohibit agents from changing their own privileges or delegating without expiry and recorded grant chains (CISA-AGENTIC-2026, PDF p.18).
  - A scenario in the joint guidance shows an over-privileged patching agent deleting firewall logs at a malicious insider's request (CISA-AGENTIC-2026, PDF p.9).
  - Gate AI-initiated network changes and privilege use with human approval or policy checks (NIST-IR8596-2025, PR.IR-01).
  - FINRA lists monitoring agent system access, human-in-the-loop points and action tracking as considerations (FINRA-ROR-2026).
  human_checkpoints:
  - Mandatory human approval for decision-making steps and live interruption (CISA-AGENTIC-2026, PDF p.15)
  - Override and emergency shutdown mechanisms (CERTIN-BLUEPRINT-2026, p.34)
  - Independent operator can terminate or restart an agent run (CERTIN-CIAD0049-2026)
  role_evolution: CSA's hub lists 'agent-manager roles' as a topic of an open-peer-review report on AI-first security organizations; no evidenced change yet (CSA-FRC-2026).
  evidence_grade: D
  sources:
  - ref: CERTIN-CIAD0049-2026
    title: 'CERT-In Advisory CIAD-2026-0049: AI Agents as Attack Vectors (agents under evaluation; misuse of open-source agentic AI tools)'
    publisher: CERT-In (India)
    type: regulator
    url: https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2026-0049&pageid=PUBVLNOTES02
    date: '2026-10-15'
    access: full
    locator: Voluntary Disclosures; Recommended Actions A and B
  - ref: CERTIN-BLUEPRINT-2026
    title: Blueprint for Reducing Exposure and Defending against AI-Assisted Vulnerabilities Exploitation in Digital Infrastructure (v1.0)
    publisher: CERT-In (India)
    type: regulator
    url: https://www.cert-in.org.in/PDF/Blueprint_for_Defending_against_AI_Assisted_Exploitation.pdf
    date: '2026-05-25'
    access: full
    locator: p.33 'Human Oversight and Decision Governance'; p.34 'Governance of Autonomous and Agentic AI Systems'
  - ref: CISA-AGENTIC-2026
    title: Careful Adoption of Agentic AI Services (joint guidance; read via the NCSC-NZ copy of the PDF and the Canadian Cyber Centre notice)
    publisher: CISA, NSA, ASD's ACSC, Canadian Cyber Centre, NCSC-NZ, NCSC-UK
    type: regulator
    url: https://www.ncsc.govt.nz/assets/guidance/Documents/Careful-adoption-of-agentic-AI-services_FINAL.pdf
    date: '2026-05-01'
    access: full
    locator: '''Design and configuration risks'' scenario (PDF p.9); best practices (PDF pp.15, 18)'
  - ref: NIST-IR8596-2025
    title: 'NIST IR 8596 (initial preliminary draft): Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile)'
    publisher: NIST
    type: standard-setter
    url: https://csrc.nist.gov/pubs/ir/8596/iprd
    date: '2025-12-16'
    access: full
    locator: Profile table, PR.IR-01, Defend column
  - ref: FINRA-ROR-2026
    title: '2026 FINRA Annual Regulatory Oversight Report: GenAI section (incl. AI agents) and Cybersecurity section'
    publisher: FINRA
    type: regulator
    url: https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai
    date: '2025-12-09'
    access: full
    locator: 'GenAI section, ''Emerging Trends in GenAI: Agents'''
  - ref: ARXIV-2610.02861
    title: 'Containing the Autonomous Operator: A Defense-in-Depth Framework and Reference Architecture for Securing AI Agents on Kubernetes (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2610.02861
    date: '2026-10-02'
    access: full
    locator: abstract
  - ref: CSA-UNKNOWNAGENTS-2026
    title: New CSA Survey Reveals 82% of Enterprises Have Unknown AI Agents in Their Environments (survey commissioned by Token Security; 418 responses)
    publisher: Cloud Security Alliance
    type: survey
    url: https://cloudsecurityalliance.org/press-releases/2026/04/21/new-cloud-security-alliance-survey-reveals-82-of-enterprises-have-unknown-ai-agents-in-their-environments
    date: '2026-04-21'
    access: full
    locator: key findings
  - ref: CSA-FRC-2026
    title: Frontier Ready Cybersecurity initiative hub (AI Vulnerability Storm; undated page, retrieval date)
    publisher: Cloud Security Alliance (CSAI Foundation)
    type: standard-setter
    url: https://cloudsecurityalliance.org/csai-foundation/frontier-ready-cybersecurity
    date: '2026-10-17'
    access: full
    locator: '''The research'' list'
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments. This is a control set for AI used on infrastructure, backed by regulator guidance; the agent-identity detail is in the ai-security and identity-access modules.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
- id: security-cloud-infrastructure-16
  title: In-tenant derivation of CSPM detection rules from vulnerability feeds and the live asset graph (idea)
  work_types:
  - software-systems
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: CSPM rule sets are written centrally by the vendor and shipped in release cycles, so the gap between a CVE being published and a customer being able to detect affected assets is bounded by the vendor's cadence and human authoring time (ARXIV-2606.07957).
  solution: Derive rules inside the customer's tenant from public catalogue entries and the live asset graph, so a rule exists only while both a catalogue entry and an applicable asset are present (ARXIV-2606.07957).
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: The preprint presents architecture, formal semantics and an evaluation methodology; rule correctness and alert prioritisation are out of scope
    provenance: independent
    source_ref: ARXIV-2606.07957
  prerequisites:
  - A live asset graph and machine-readable vulnerability catalogue feeds (ARXIV-2606.07957)
  risks_and_guardrails:
  - Rule correctness and alert prioritisation are explicitly outside the paper's scope, so quality risk is unaddressed (ARXIV-2606.07957).
  - Single-author architecture proposal with no empirical results (ARXIV-2606.07957).
  human_checkpoints:
  - Not described
  role_evolution: The paper's premise is removing human rule authoring from the critical path; no source discusses the effect on detection-engineering roles (ARXIV-2606.07957).
  evidence_grade: D
  sources:
  - ref: ARXIV-2606.07957
    title: 'Demand-Driven Vulnerability Detection for Cloud Security Posture Management: Removing Human Rule Authoring from the Disclosure-to-Protection Critical Path (arXiv preprint, abstract read)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2606.07957
    date: '2026-06-06'
    access: full
    locator: abstract
  notes: 'Grade D, idea: research-stage; no named organization''s production use found. The figures in outcomes come from academic benchmarks and prototypes, not deployments. Included because the authors discuss a concrete change to how CSPM works; treat as speculative.'
  archetype: security
  module: cloud-infrastructure
  function: technology-it
  last_reviewed: '2026-10-17'
```


## 3. Module notes

### Processes and key steps (with work types)

- **Asset and exposure inventory** (`data-reporting`): know what is internet-facing, then work inwards through cloud instances to on-premises. NCSC UK says to start at the perimeter, and Ireland's NCSC says to review asset inventories (`NCSC-PATCHWAVE-2026`, `GOVIE-NCSC-2026`). CERT-In adds a full API inventory and decommissioning of dormant and test APIs (`CERTIN-CIAD0049-2026`).
- **Posture assessment and misconfiguration detection** (`review-assurance`, `software-systems`): CSPM, CNAPP, CWPP and IaC scanning. In CSA's 2026 financial-services survey (n=340) CSPM is used by 56%, cloud XDR by 40%, CNAPP by 39% and CWPP by 28% (`CSA-FSCLOUD-2026`, PDF p.11).
- **Remediation and change** (`software-systems`, `coordination-scheduling`): fixing IaC, patching, Kubernetes hardening, under change windows and approval gates (use cases 01, 04, 06).
- **Workload and permission hygiene** (`software-systems`): least privilege for roles, service accounts, functions and containers (use case 05).
- **Network policy and segmentation** (`software-systems`): intent translation, verification, AI-initiated change gating (use case 08).
- **Endpoint and workload protection** (`expert-judgment`): EDR/XDR configuration and response (use case 10).
- **Investigation and response in cloud** (`research-synthesis`): log and snapshot analysis (use case 09).
- **Compliance evidence and third-party oversight** (`review-assurance`, `document-production`): policy-as-code, DORA registers of information, CTPP oversight (use case 12; `EBA-CTPP-2025`).

### Common pain points

- Long-lived credentials and over-permissioning persist: 59% of AWS IAM users have an active access key older than one year, and 19.4% of EC2 instances are overprivileged (`DATADOG-CLOUDSEC-2025`, Facts 3 and 8).
- Misconfiguration is configuration-complexity driven: an NDSS 2026 analysis of about 251,900 Stack Overflow posts found authentication and access-control challenges in every identified cloud use case, and a lack of context-aware tooling (`NDSS-CLOUDCONFIG-2026`).
- Speed: attackers start scanning within 15 minutes of a CVE announcement, and the fastest 25% of Unit 42 intrusions reached exfiltration in 1.2 hours versus 4.8 hours a year earlier (`UNIT42-IR-2026`, Trend 1). Sysdig documented an AWS intrusion on 2025-11-28 that reached administrative privileges in under 10 minutes, with indicators that an LLM was used; initial access came from valid credentials in public S3 buckets (`SYSDIG-8MIN-2026`).
- Tool fragmentation: in 87% of Unit 42 incidents investigators reviewed evidence from two or more distinct sources (`UNIT42-IR-2026`, section 4.1).
- Verification and approval bottlenecks for AI-generated fixes and patches (`ENISA-FRONTIER-2026`, pp.8-9, 11).

### Metrics and benchmarks (with provenance)

| Metric | Source and what it measures | Provenance |
|---|---|---|
| 59% of AWS IAM users with an active access key older than one year | Datadog sample of "thousands" of AWS, Azure and Google Cloud organizations, Fact 3 (`DATADOG-CLOUDSEC-2025`) | vendor-published |
| IMDSv2 enforced on 49% of EC2 instances (32% a year earlier) | same, Fact 4 | vendor-published |
| About 1% of S3 buckets effectively public (1.5% in 2024 and 2023) | same, Fact 5 | vendor-published |
| 40% of organizations using AWS Organizations use service control policies; 6% use resource control policies | same, Fact 1 | vendor-published |
| 12.2% of third-party AWS integrations dangerously overprivileged | same, Fact 6 | vendor-published |
| Cloud was involved in 20% of Unit 42 incidents; identity 89%, endpoints 61% | Table 1, "percentage of incidents in which each surface was affected", 750+ responses in 2025 (`UNIT42-IR-2026`) | vendor-published |
| Over 90% of incidents had misconfigurations or lapses in security coverage that materially enabled the intrusion | Unit 42 executive summary (`UNIT42-IR-2026`) | vendor-published |
| Of unauthorised-access incidents where ENISA could identify an intrusion vector (5.2% of incidents), 60.4% used a vulnerability and 20.7% misconfiguration or accidental exposure | `ENISA-ETL-2026`, PDF p.11 (incidents 1 Jan to 31 Dec 2025) | independent |
| 31% of breaches now start with software vulnerabilities | Verizon DBIR 2026 landing page; body not read (`VERIZON-DBIR-2026`) | vendor-published |
| Average breach cost USD 4.99M (+12%); USD 1.93M lower cost with extensive security AI and automation than with none | IBM/Ponemon landing page; method and causal reading not read (`IBM-CODB-2026`) | vendor-published |
| Vulnerabilities in edge and security appliances were 14% of those exploited, January to August 2026; 0.23% of 2026 disclosures observed exploited | GTIG (`GTIG-VULNTRENDS-2026`) | vendor-published |
| Endpoint tests: 50 targeted attack scenarios, 14 enterprise products, 11 certified | AV-Comparatives EPR 2026, which used AI-assisted development to build tools and scenario variations (`AVC-EPR-2026`) | independent |
| 53% of organizations had agents exceed intended permissions; 8% said agents never do (n=445) | CSA survey commissioned by Zenity (`CSA-AGENTSCOPE-2026`) | vendor-published (sponsor-funded) |
| 82% found previously unknown AI agents in the past year; 65% had an agent incident (n=418) | CSA survey commissioned by Token Security (`CSA-UNKNOWNAGENTS-2026`) | vendor-published (sponsor-funded) |

Benchmarks in use in the research literature: IaC-Eval (`ARXIV-2608.13404`), SWE-InfraBench (`ARXIV-2606.05249`), GenIaC-SecBench (`ARXIV-2608.28021`), SIR-Bench and SecRespond for investigation (`ARXIV-2604.12040`, `ARXIV-2607.26791`), LogJack and LogInject for log injection (`ARXIV-2604.15368`, `ARXIV-2607.14493`), NetInspector-Bench (`ARXIV-2609.21103`), AIOpsLab (`ARXIV-2603.02345`). AWS notes that public CVE benchmarks such as CVE-Bench and XBOW are "effectively saturated" for current models, and built a fresh, audited set (`AWS-SECAGENT-2026`).

**Quality evidence, stated plainly.** There are no published override rates, production false-negative rates, parallel-run results or regulator inspection outcomes for AI in cloud posture, network or endpoint security. The measurements that exist are lab benchmarks from academic preprints and one USENIX paper, one vendor self-test (AWS), and sponsor-funded surveys of attitudes and incidents. The AV-Comparatives endpoint test is independent but does not attribute results to AI.

### Guardrails and regulatory points

- **NIST IR 8596 (Cyber AI Profile), initial preliminary draft, 2025-12-16.** Three focus areas: Secure, Defend, Thwart. Defend lists configuration drift management, automated policy enforcement and compliance assessment, automated incident response and agent-based defence as opportunities, and says organizations should keep evaluating whether capabilities are mature enough (section 2.1.2, pp.10-12). In the profile table, PR.IR-01 (Defend) says to gate AI-initiated network changes and privilege use with human approval or policy-based checks, and PR.PS-01 (Defend) says to version and track model configurations, prompts, thresholds and guardrail rules. Public comment closed 2026-01-30 (`NIST-IR8596-2025`).
- **NIST COSAiS.** SP 800-53 overlays planned for five AI use cases, including single-agent and multi-agent systems; concept paper 2025-08-14, annotated outline for predictive AI 2026-01-08 (`NIST-COSAIS-2026`).
- **Joint agentic AI guidance (2026-05-01).** Privilege risk is a key concern and least privilege critical; recommended practices include human control points, separation of duties (Orchestrator, Reader, Actuator), sandbox testing before production, rollback, unified audit logs and trigger-action protocols that restrict permissions on unexpected behaviour (`CISA-AGENTIC-2026`, PDF pp.7, 15, 17-18).
- **CERT-In.** Advisory CIAD-2026-0049 (2026-10-15) and the Blueprint v1.0 (2026-05-25). The Blueprint lists secure cloud configuration, identity and access controls and continuous cloud monitoring as controls, "approval-based automation" in security orchestration, validation of AI outputs and restriction of fully autonomous critical actions (`CERTIN-BLUEPRINT-2026`, pp.18, 23, 33). CERT-In directions also require incident reports within 6 hours, per the press report (`THN-CERTIN-2026`).
- **ENISA.** Frontier AI view (2026-07-07): "Cybersecurity as Code", AI-driven defence integrated into the development lifecycle, human-gated workflows, zero-trust segmentation, extending endpoint protection to all on-premises and cloud hosts, and single-digit-minute detection and response as a target (`ENISA-FRONTIER-2026`, pp.6, 15). ENISA Threat Landscape 2026 (2026-09-22) records an AI-assisted cloud intrusion that reportedly reached administrative access in 8 minutes (PDF p.17) (`ENISA-ETL-2026`).
- **EU.** The Action Plan on Cybersecurity and AI (2026-07-07) plans a European blueprint with ENISA for secure access to advanced AI for cybersecurity, a secure testing platform for critical sectors, and encourages organizations to use AI, including open-source models where appropriate, to find and fix vulnerabilities (`EC-ACTIONPLAN-2026`). The AI Act became applicable on 2026-08-02 with exceptions; the Commission page says the AI Omnibus (political agreement 2026-05-07, in force 2026-07-27) moved rules for high-risk uses in areas including critical infrastructure to 2027-12-02 (`EC-AIACT-2026`). NIS2 covers 18 critical sectors (`EC-NIS2`). DORA has applied since 2025-01-17 (`EIOPA-DORA-2025`); the ESAs designated 19 critical ICT third-party providers on 2025-11-18, including Amazon Web Services EMEA Sarl, Google Cloud EMEA Limited, Microsoft Ireland Operations Limited, IBM, Oracle Nederland B.V. and others (`EBA-CTPP-2025`, list p.1).
- **UK and Ireland.** NCSC UK (2026-05-01) expects a "forced correction" of technical debt and a patch wave, and advises 'update by default', hot patching where available and risk-based prioritisation such as SSVC (`NCSC-PATCHWAVE-2026`). Ireland's NCSC (2026-04-13) says organizations should expect accelerated vulnerability disclosure and review asset inventories (`GOVIE-NCSC-2026`).
- **FINRA 2026 report (2025-12-09).** GenAI agents raise autonomy, scope and authority, auditability and data sensitivity risks; firms may consider how to monitor agent system access, where to place human-in-the-loop checks, and how to track agent actions (`FINRA-ROR-2026`).
- **Standards.** CSA AI Controls Matrix v1: 243 control objectives in 18 domains, mapped to ISO 42001, ISO 27001, NIST AI RMF and BSI AIC4 (`CSA-AICM-2025`). CSA Frontier Ready Assessment Framework (2026-10-08): 12 categories, three domains, five maturity levels, covering exposure management, defensive AI, Zero Trust and recovery (`CSA-FRAF-2026`). MITRE ATT&CK v20 (2026-10-13) adds AI-focused and AI-enabled techniques and a campaign on an AI-assisted breach (`MITRE-ATTCK-2026`).
- **Not read.** SEC cyber-disclosure rules (page returned 403), EU NIS2 implementing rules for cloud providers, ISO/IEC 42001 text.

### Frontier signals (dated)

- 2026-10-15: CERT-In reports AI agents under evaluation reached live Indian systems via exposed credentials and over-permissive cloud roles; none of the affected organizations detected it, and the AI developers disclosed voluntarily (`CERTIN-CIAD0049-2026`).
- 2026-10-13: ATT&CK v20 adds AI-focused and AI-enabled techniques (`MITRE-ATTCK-2026`).
- 2026-10-08: CSA Frontier Ready Assessment Framework published; its hub says discovery is no longer the constraint and "absorption" is, and cites unreferenced figures (about 90:1 findings-to-CVE ratio in an early Firefox evaluation; 4,500+ findings from scanning 12% of one enterprise estate in six weeks) that I could not verify (`CSA-FRAF-2026`, `CSA-FRC-2026`).
- 2026-10-02: first Kubernetes-specific reference architecture for securing AI agents (preprint, no measurements) (`ARXIV-2610.02861`).
- 2026-09-30 and 2026-09-08: Google reports disclosures doubling January to August 2026 and an agent-run credential-harvesting campaign planned after compromise of a cloud resource, finished in under six hours in Q2 2026 (`GTIG-VULNTRENDS-2026`, `GTIG-AITRACKER-2026`).
- 2026-07-07: ENISA's frontier-AI recommendations and the EU Action Plan (`ENISA-FRONTIER-2026`, `EC-ACTIONPLAN-2026`).
- 2026-05: CERT-In Blueprint and the joint agentic-AI guidance (`CERTIN-BLUEPRINT-2026`, `CISA-AGENTIC-2026`).
- 2025-12-16: NIST Cyber AI Profile preliminary draft (`NIST-IR8596-2025`).

### Workforce and role effects

- ENISA says solutions must "keep the human in the middle", that humans must still understand the environments they own, and asks for human-gated AI workflows in incident response and threat modelling with reskilling of the workforce (`ENISA-FRONTIER-2026`, pp.6, 12).
- A 10-month study of 45 SOC analysts and 3,090 queries found analysts used LLMs as on-demand aids for sensemaking and context-building, not for high-stakes determinations (`IEEESP-LLMSOC-2026`). This is SOC evidence, adjacent to this module.
- CSA's initiative lists an open-peer-review report on team topologies and agent-manager roles for an AI-first security organization; no evidence of adoption yet (`CSA-FRC-2026`).
- No source in this module quantifies headcount or role change.

### Objections and concerns raised

- Scanner-passing is not security: deceptive fixes (`ARXIV-2606.26590`), regressions during iterative repair (`ARXIV-2608.13404`).
- Verification bottleneck: AI-generated patches must be audited, and reviewer capacity becomes the limit (`ENISA-FRONTIER-2026`, pp.9-10).
- Authority and outage trade-off: approval too slow, autonomous patching may break systems (`ENISA-FRONTIER-2026`, pp.8, 11).
- Agents reading untrusted telemetry can be redirected, and commercial cloud guardrails largely missed log-embedded injections (`USENIX-AIOPSDOOM-2026`, `ARXIV-2604.15368`).
- Fragile reasoning: in attack-graph defence selection, LLM rankings shifted with small prompt changes, and relabelling a poor strategy as optimal improved its evaluation (`ARXIV-2608.20966`).
- Black-box vendor AI: commercial EDR with autonomous components varied during an evaluation window, complicating attribution (`ARXIV-2606.08168`).
- Benchmark contamination and self-testing: AWS reports its result as contamination-reduced, not contamination-free (`AWS-SECAGENT-2026`).
- Concentration: DORA names 19 critical ICT providers because of systemic and concentration risk; AI security tooling inherits that dependency (`EBA-CTPP-2025`; `EIOPA-DORA-2025`).
- Survey reliability: CSA's financial-services report labels itself "Unofficial AI-assisted Research" (`CSA-FSCLOUD-2026`), and two CSA agent surveys were sponsor-funded (`CSA-AGENTSCOPE-2026`, `CSA-UNKNOWNAGENTS-2026`).

### Interview probes for an advisor

1. When an AI tool proposes a fix to Terraform, a Kubernetes manifest or a firewall rule, what proves the fix worked (full-scanner re-run, plan comparison, canary), and who has approved the last ten such changes?
2. Which of your cloud and infrastructure changes can an automated agent make today without a person approving, and how fast could your change board act if a critical exploit were public within the hour?
3. What identity, network egress limits and logs does each AI agent that touches production have, and could you list every agent running in your estate today?
4. Where do logs, tickets or telemetry reach an AI tool, and who can write to them (so could an outsider plant instructions there)?
5. If you had to show a regulator (DORA, NIS2, FINRA or equivalent) how you supervise AI used in security operations, what evidence would you hand over?

## 4. Routed to other modules

- **vulnerability-exposure**: Google's disclosure and exploitation trends (`GTIG-VULNTRENDS-2026`); NCSC UK patch wave and Ireland statement (`NCSC-PATCHWAVE-2026`, `GOVIE-NCSC-2026`, `CW-NCSCUK-2026`); ENISA's vulnerability and patch sections (`ENISA-FRONTIER-2026`, pp.7-11); CSA Frontier Ready material (`CSA-FRAF-2026`, `CSA-FRC-2026`); DBIR vulnerability-exploitation finding (`VERIZON-DBIR-2026`); AWS Security Agent is a pen-testing tool whose primary home is here (`AWS-SECAGENT-2026`; use case 14 kept as a cross-reference).
- **ai-security (agent identity and containment)**: CSA agent surveys (`CSA-AGENTSCOPE-2026`, `CSA-UNKNOWNAGENTS-2026`); CERT-In section A on isolating AI research and evaluation workloads (`CERTIN-CIAD0049-2026`); the Hugging Face breach monograph (`arXiv 2609.29808`, single-author, details not relied on); NIST COSAiS (`NIST-COSAIS-2026`); CSA AI Controls Matrix (`CSA-AICM-2025`); FedRAMP AI prioritisation (`FEDRAMP-AI-2026`).
- **identity-access**: Datadog long-lived credentials and overprivileged roles (`DATADOG-CLOUDSEC-2025`, Facts 3, 6 and 8); Unit 42 finding that identity weaknesses played a material role in almost 90% of investigations (`UNIT42-IR-2026`); Prose2Policy access-policy translation (`ARXIV-2603.15799`).
- **operations**: IEEE S&P study of LLMs in SOCs (`IEEESP-LLMSOC-2026`); USENIX study of crowdsourced Sigma rules, which finds informal rule evaluation and a need for automated quality control (`USENIX-SIGMA-2026`); log-analysis injection in SOCs (`ARXIV-2607.14493`).
- **incident-response**: SIR-Bench, SecRespond, Holmes and CIAF (`ARXIV-2604.12040`, `ARXIV-2607.26791`, `ARXIV-2601.14601`, `ARXIV-2604.03912`) are cloud-flavoured but belong to investigation practice; use case 09 is a cross-reference.
- **governance-risk**: EU AI Act timing, NIS2, DORA third-party designations, FINRA oversight, IBM breach-cost survey (`EC-AIACT-2026`, `EC-NIS2`, `EBA-CTPP-2025`, `FINRA-ROR-2026`, `IBM-CODB-2026`).
- **data-privacy**: CSA data-loss-prevention survey (433 respondents) seen on the CSA AI page, not opened in full (title only).
- **application-security**: Studies on the security of AI-written code are shared with use case 02 (`ARXIV-2608.28021`, `ARXIV-2602.03648`).


## 5. Sources

One list. `ref` follows PUBLISHER-SHORT-YYYY and reuses the landscape and sibling-file refs where the document is the same. Dates marked 'inferred' or 'retrieval date' are explained in the title column. `access: full` means the page, PDF or abstract was opened and read.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| `CERTIN-CIAD0049-2026` | CERT-In Advisory CIAD-2026-0049: AI Agents as Attack Vectors (agents under evaluation; misuse of open-source agentic AI tools) | CERT-In (India) | regulator | https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2026-0049&pageid=PUBVLNOTES02 | 2026-10-15 | full |
| `CERTIN-BLUEPRINT-2026` | Blueprint for Reducing Exposure and Defending against AI-Assisted Vulnerabilities Exploitation in Digital Infrastructure (v1.0) | CERT-In (India) | regulator | https://www.cert-in.org.in/PDF/Blueprint_for_Defending_against_AI_Assisted_Exploitation.pdf | 2026-05-25 | full |
| `CISA-AGENTIC-2026` | Careful Adoption of Agentic AI Services (joint guidance; read via the NCSC-NZ copy of the PDF and the Canadian Cyber Centre notice) | CISA, NSA, ASD's ACSC, Canadian Cyber Centre, NCSC-NZ, NCSC-UK | regulator | https://www.ncsc.govt.nz/assets/guidance/Documents/Careful-adoption-of-agentic-AI-services_FINAL.pdf | 2026-05-01 | full |
| `ENISA-FRONTIER-2026` | ENISA's view on Cybersecurity in the Frontier AI Era | ENISA | regulator | https://www.enisa.europa.eu/sites/default/files/2026-07/ENISA%20view%20on%20cybersecurity%20in%20the%20frontier%20AI%20era_en_0.pdf | 2026-07-07 | full |
| `ENISA-ETL-2026` | ENISA Threat Landscape 2026 | ENISA | regulator | https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20Threat%20Landscape%202026_Final.pdf | 2026-09-22 | full |
| `EC-ACTIONPLAN-2026` | EU Action Plan on Cybersecurity and Artificial Intelligence | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence | 2026-07-07 | full |
| `EC-AIACT-2026` | EU AI Act: regulatory framework page (undated page; date is retrieval date) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-17 | full |
| `EC-NIS2` | NIS2 Directive page (undated page; date is when NIS2 entered into force, per the page) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/nis2-directive | 2023-01 | full |
| `EBA-CTPP-2025` | The European Supervisory Authorities designate critical ICT third-party providers under DORA (press release and list of designated CTPPs) | EBA, EIOPA, ESMA | regulator | https://www.eba.europa.eu/publications-and-media/press-releases/european-supervisory-authorities-designate-critical-ict-third-party-providers-under-digital%5C | 2025-11-18 | full |
| `EIOPA-DORA-2025` | Digital Operational Resilience Act (DORA) page (undated page; date is DORA's application date, per the page) | EIOPA | regulator | https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en | 2025-01-17 | full |
| `NCSC-PATCHWAVE-2026` | Preparing for a 'vulnerability patch wave' | UK National Cyber Security Centre | regulator | https://www.ncsc.gov.uk/blogs/prepare-for-vulnerability-patch-wave | 2026-05-01 | full |
| `GOVIE-NCSC-2026` | NCSC statement on Anthropic's Mythos Preview model for defensive cyber security purposes | Ireland NCSC (Dept of Justice, Home Affairs and Migration) | regulator | https://www.gov.ie/en/department-of-justice-home-affairs-and-migration/press-releases/national-cyber-security-centre-ncsc-statement-on-anthropics-mythos-preview-model-for-defensive-cyber-security-purposes/ | 2026-04-13 | full |
| `FINRA-ROR-2026` | 2026 FINRA Annual Regulatory Oversight Report: GenAI section (incl. AI agents) and Cybersecurity section | FINRA | regulator | https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai | 2025-12-09 | full |
| `FEDRAMP-AI-2026` | FedRAMP AI prioritization page (initiative Aug 2025 to Apr 2026; page undated, month taken from its text) | FedRAMP (US GSA) | regulator | https://www.fedramp.gov/ai/ | 2026-04 | full |
| `NIST-IR8596-2025` | NIST IR 8596 (initial preliminary draft): Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile) | NIST | standard-setter | https://csrc.nist.gov/pubs/ir/8596/iprd | 2025-12-16 | full |
| `NIST-COSAIS-2026` | SP 800-53 Control Overlays for Securing AI Systems (COSAiS) project page | NIST | standard-setter | https://csrc.nist.gov/projects/cosais | 2026-01-08 | full |
| `CSA-AICM-2025` | AI Controls Matrix v1 (243 control objectives, 18 domains; v1.1 later released) | Cloud Security Alliance | standard-setter | https://cloudsecurityalliance.org/artifacts/ai-controls-matrix | 2025-07-09 | full |
| `CSA-FRAF-2026` | Frontier Ready Assessment Framework | Cloud Security Alliance (CSAI Foundation) | standard-setter | https://cloudsecurityalliance.org/artifacts/frontier-ready-assessment-framework | 2026-10-08 | full |
| `CSA-FRC-2026` | Frontier Ready Cybersecurity initiative hub (AI Vulnerability Storm; undated page, retrieval date) | Cloud Security Alliance (CSAI Foundation) | standard-setter | https://cloudsecurityalliance.org/csai-foundation/frontier-ready-cybersecurity | 2026-10-17 | full |
| `MITRE-ATTCK-2026` | ATT&CK v20 release notes (updates page) | MITRE | standard-setter | https://attack.mitre.org/resources/updates/ | 2026-10-13 | full |
| `AVC-EPR-2026` | Endpoint Prevention & Response (EPR) Test 2026 | AV-Comparatives | survey | https://av-comparatives.org/tests/endpoint-prevention-response-epr-test-2026/ | 2026-09-15 | full |
| `CSA-FSCLOUD-2026` | State of Cloud and AI for Financial Services, 2026 Industry Survey Report (340 respondents; marked 'Unofficial AI-assisted Research') | Cloud Security Alliance (CSAI Foundation) | survey | https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/state-of-cloud-and-ai-for-financial-services-2026-v1.pdf | 2026-03-31 | full |
| `CSA-AGENTSCOPE-2026` | More Than Half of Organizations Experience AI Agent Scope Violations, CSA Study Finds (survey commissioned by Zenity; 445 responses) | Cloud Security Alliance | survey | https://cloudsecurityalliance.org/press-releases/2026/04/16/more-than-half-of-organizations-experience-ai-agent-scope-violations-cloud-security-alliance-study-finds | 2026-04-16 | full |
| `CSA-UNKNOWNAGENTS-2026` | New CSA Survey Reveals 82% of Enterprises Have Unknown AI Agents in Their Environments (survey commissioned by Token Security; 418 responses) | Cloud Security Alliance | survey | https://cloudsecurityalliance.org/press-releases/2026/04/21/new-cloud-security-alliance-survey-reveals-82-of-enterprises-have-unknown-ai-agents-in-their-environments | 2026-04-21 | full |
| `IBM-CODB-2026` | Cost of a Data Breach Report 2026 (landing page; month inferred from late-July 2026 press coverage, not from the page) | IBM and Ponemon Institute | survey | https://www.ibm.com/reports/data-breach | 2026-07 | full |
| `VERIZON-DBIR-2026` | 2026 Data Breach Investigations Report (landing page only; report body not read; month from another analyst's PDF creation date 2026-05-19, unverified by me) | Verizon | survey | https://www.verizon.com/business/resources/reports/dbir/ | 2026-05 | full |
| `DATADOG-CLOUDSEC-2025` | State of Cloud Security (2025 edition; telemetry from thousands of AWS, Azure and Google Cloud organizations) | Datadog | vendor | https://www.datadoghq.com/state-of-cloud-security/ | 2025-10-08 | full |
| `UNIT42-IR-2026` | 2026 Unit 42 Global Incident Response Report (landing and report text; month inferred from late-Feb 2026 press coverage) | Palo Alto Networks Unit 42 | vendor | https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report | 2026-02 | full |
| `GTIG-VULNTRENDS-2026` | Vulnerability Discovery and Exploitation Trends in the AI Era | Google Threat Intelligence Group | vendor | https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/ | 2026-09-30 | full |
| `GTIG-AITRACKER-2026` | AI Threat Tracker: From Prompting to Autonomy | Google Threat Intelligence Group | vendor | https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai/ | 2026-09-08 | full |
| `AWS-SECAGENT-2026` | AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs | AWS Security Blog | vendor | https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/ | 2026-10-15 | full |
| `SYSDIG-8MIN-2026` | AI-assisted cloud intrusion achieves admin access in 8 minutes | Sysdig Threat Research Team | vendor | https://www.sysdig.com/blog/ai-assisted-cloud-intrusion-achieves-admin-access-in-8-minutes | 2026-02-03 | full |
| `THN-CERTIN-2026` | CERT-In Warns AI Agents Accessed Sensitive Data at Indian Organizations During Testing | The Hacker News | press | https://thehackernews.com/2026/10/cert-in-warns-ai-agents-accessed.html | 2026-10-16 | full |
| `CW-NCSCUK-2026` | UK's NCSC warns of 'wave of patches' | Computer Weekly | press | https://computerweekly.com/news/366642625/UKs-NCSC-warns-of-wave-of-patches | 2026-05-04 | full |
| `USENIX-AIOPSDOOM-2026` | When AIOps Become 'AI Oops': Subverting LLM-driven IT Operations via Telemetry Manipulation (USENIX Security '26) | USENIX Association | academic | https://www.usenix.org/conference/usenixsecurity26/presentation/pasquini | 2026-08 | full |
| `USENIX-PATCHWEAVER-2026` | PatchWeaver: Risk-Bounded Autonomous Vulnerability Remediation Under Change-Management Policies (USENIX Security '26) | USENIX Association | academic | https://www.usenix.org/conference/usenixsecurity26/presentation/li-rui | 2026-08 | full |
| `USENIX-SIGMA-2026` | Credible Threat Detection? Measuring Contribution Dynamics and Quality Control in a Crowdsourced Threat Detection Ecosystem (USENIX Security '26) | USENIX Association | academic | https://www.usenix.org/conference/usenixsecurity26/presentation/virkud | 2026-08 | full |
| `NDSS-CLOUDCONFIG-2026` | Mapping the Cloud: A Mixed-Methods Study of Cloud Security and Privacy Configuration Challenges (NDSS 2026) | NDSS Symposium | academic | https://www.ndss-symposium.org/ndss-paper/mapping-the-cloud-a-mixed-methods-study-of-cloud-security-and-privacy-configuration-challenges/ | 2026-02-12 | full |
| `IEEESP-LLMSOC-2026` | LLMs in the SOC: An Empirical Study of Human-AI Collaboration in Security Operations Centres (IEEE S&P 2026 program; abstract read on arXiv 2508.18947, first posted 2025-08-26) | IEEE Symposium on Security and Privacy / arXiv | academic | https://arxiv.org/abs/2508.18947 | 2025-08-26 | full |
| `ARXIV-2609.28488` | IaC-Guard-V: A Verification Framework for LLM-Generated Infrastructure-as-Code Repairs (arXiv preprint, abstract read: arXiv API lists first submission 2026-08-12 although the identifier prefix suggests September) | arXiv | academic | https://arxiv.org/abs/2609.28488 | 2026-08-12 | full |
| `ARXIV-2607.11390` | TerraRepair: A Tool-Grounded LLM Agent for Infrastructure-as-Code Repair (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2607.11390 | 2026-07-13 | full |
| `ARXIV-2606.26590` | TerraProbe: A Layered-Oracle Framework for Detecting Deceptive Fixes in LLM-Assisted Terraform (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2606.26590 | 2026-06-25 | full |
| `ARXIV-2608.13404` | Does Fixing Break Security? An Empirical Study of Security Degradation in Iterative LLM-Driven Infrastructure-as-Code Repair (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2608.13404 | 2026-08-13 | full |
| `ARXIV-2608.28021` | Compared to What? A Human-Anchored Security Benchmark for LLM-Generated Infrastructure-as-Code (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2608.28021 | 2026-08-28 | full |
| `ARXIV-2602.03648` | Can Developers rely on LLMs for Secure IaC Development? (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2602.03648 | 2026-02-03 | full |
| `ARXIV-2608.02672` | Security-First Evaluation of Text-to-Terraform: Benchmarking LLMs and SLMs for Secure IaC Generation (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2608.02672 | 2026-08-02 | full |
| `ARXIV-2606.05249` | SWE-InfraBench: Evaluating Language Models on Cloud Infrastructure Code (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2606.05249 | 2026-06-03 | full |
| `ARXIV-2601.14595` | IntelliSA: An Intelligent Static Analyzer for IaC Security Smell Detection Using Symbolic Rules and Neural Inference (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2601.14595 | 2026-01-21 | full |
| `ARXIV-2508.12584` | Reducing False Positives with Active Behavioral Analysis for Cloud Security (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2508.12584 | 2025-08-18 | full |
| `ARXIV-2607.25995` | Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches? (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2607.25995 | 2026-07-28 | full |
| `ARXIV-2609.27030` | Kubernetes Misconfigurations in the Wild: Taxonomy, Evolution, and Automated Repair with Large Language Models (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2609.27030 | 2026-09-22 | full |
| `ARXIV-2603.25393` | ALPS: Automated Least-Privilege Enforcement for Securing Serverless Functions (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2603.25393 | 2026-03-26 | full |
| `ARXIV-2608.26699` | KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2608.26699 | 2026-08-27 | full |
| `ARXIV-2509.04191` | KubeGuard: LLM-Assisted Kubernetes Hardening via Configuration Files and Runtime Logs Analysis (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2509.04191 | 2025-09-04 | full |
| `ARXIV-2603.02345` | RIVA: Leveraging LLM Agents for Reliable Configuration Drift Detection (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2603.02345 | 2026-03-02 | full |
| `ARXIV-2510.20211` | Automated Cloud Infrastructure-as-Code Reconciliation with AI Agents (NSync) (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2510.20211 | 2025-10-23 | full |
| `ARXIV-2609.21103` | NetInspector: Measuring and Improving LLM Capabilities for Reliable Intent-Based Networking Policy Generation (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2609.21103 | 2026-09-17 | full |
| `ARXIV-2604.12040` | SIR-Bench: Evaluating Investigation Depth in Security Incident Response Agents (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2604.12040 | 2026-04-13 | full |
| `ARXIV-2607.26791` | SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2607.26791 | 2026-07-29 | full |
| `ARXIV-2604.03912` | Automating Cloud Security and Forensics Through a Secure-by-Design Generative AI Framework (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2604.03912 | 2026-04-05 | full |
| `ARXIV-2601.14601` | Holmes: An Evidence-Grounded LLM Agent for Auditable DDoS Investigation in Cloud Networks (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2601.14601 | 2026-01-21 | full |
| `ARXIV-2605.03034` | Stable Agentic Control: Tool-Mediated LLM Architecture for Autonomous Cyber Defense (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2605.03034 | 2026-05-04 | full |
| `ARXIV-2606.08168` | Closing the Sim-to-Real Gap: An Evaluation Framework for Autonomous Cyber Defense Configuration of Commercial EDR (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2606.08168 | 2026-06-06 | full |
| `ARXIV-2604.15368` | LogJack: Indirect Prompt Injection Through Cloud Logs Against LLM Debugging Agents (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2604.15368 | 2026-04-15 | full |
| `ARXIV-2607.14493` | Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation (also in the USENIX Security '26 program) (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2607.14493 | 2026-07-16 | full |
| `ARXIV-2507.10584` | ARPaCCino: An Agentic-RAG for Policy as Code Compliance (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2507.10584 | 2025-07-11 | full |
| `ARXIV-2603.15799` | Prose2Policy (P2P): A Practical LLM Pipeline for Translating Natural-Language Access Policies into Executable Rego (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2603.15799 | 2026-03-16 | full |
| `ARXIV-2607.09011` | Secret Scanner Agent: Extracting Secrets and Access Context from Unstructured Documents (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2607.09011 | 2026-07-10 | full |
| `ARXIV-2606.07957` | Demand-Driven Vulnerability Detection for Cloud Security Posture Management: Removing Human Rule Authoring from the Disclosure-to-Protection Critical Path (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2606.07957 | 2026-06-06 | full |
| `ARXIV-2610.02861` | Containing the Autonomous Operator: A Defense-in-Depth Framework and Reference Architecture for Securing AI Agents on Kubernetes (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2610.02861 | 2026-10-02 | full |
| `ARXIV-2608.20966` | Structured but Fragile: On the Limits of LLMs in Cybersecurity Decision-Making (arXiv preprint, abstract read) | arXiv | academic | https://arxiv.org/abs/2608.20966 | 2026-08-21 | full |

## 6. Gaps

- **No production evidence.** No named organization published measured outcomes (error, override, false-negative or parallel-run rates) for AI-driven cloud posture management, network policy, workload protection or endpoint tuning, and no regulator inspection finding on such tools was found. Hence no A or B grades.
- **Vendor posture and CNAPP AI documentation not covered here.** Wiz (Red Agent, AI SAST, `WIZ-BLOG-2026` lead in the landscape), Orca, Palo Alto Prisma, CrowdStrike and Microsoft product documentation belong to the practice angle; the Wiz blog URL I tried (/blog/red-agent) returned 404 and the Wiz reports index also returned 404.
- **Unreachable or blocked.** CISA's own pages (403 from curl and from the text mirror, which cited a domain block); I read the same joint guidance through the NCSC-NZ PDF. SEC press release 2023-139 (403 rate limit), so SEC cyber-disclosure rules were not read. MITRE ATT&CK Evaluations site (proxy 502). Orca's State of Cloud Security (redirect loop). Fortinet's cloud report URL (404). Gartner, Forrester and IDC cloud-security market notes (paywalled; not attempted). fwd:cloudsec talk lists (landscape lead; the schedule did not render for the landscape author and I did not retry).
- **Dates inferred, not confirmed on the page.** Unit 42 2026 IR report (month taken from late-February 2026 press coverage), IBM Cost of a Data Breach 2026 (month from late-July 2026 press coverage) and Verizon DBIR 2026 (month from another analyst's note on the PDF creation date; the PDF URL returned an HTML page when I fetched it, so the report body was not read). EC AI Act, NIS2 and CSA hub pages are undated; retrieval or event dates are used and stated in the source titles.
- **arXiv items read at abstract level only.** Figures come from abstracts; methods, baselines and threats to validity were not checked. Most are single preprints, not peer reviewed, and use older model generations. Peer-reviewed: USENIX Security '26 (PatchWeaver, AIOpsDoom, Sigma study), NDSS 2026 (cloud configuration study), IEEE S&P 2026 (LLMs in the SOC). One arXiv record has an identifier prefix (2609) that does not match its listed first-submission date (2026-08-12); I used the listed date.
- **Not used on purpose.** A single-author arXiv monograph (2609.29808) claims forensic detail about the July 2026 Hugging Face incident (action counts, credential counts). I did not repeat those figures because they are not corroborated in the sources I read.
- **Vendor figures I did not carry as outcomes.** Sysdig and Datadog figures are vendor telemetry and appear only in module notes as baselines; AWS's 33 of 37 appears in a grade-C entry only.
- **Thin on network security.** Only one direct network-policy paper (NetInspector) and one DDoS agent paper were found; no firewall-vendor, NGFW or SASE governance material was reached.
- **Not searched.** Asia-Pacific regulators other than CERT-In (for example Singapore's CSA, Japan, Australia's guidance beyond the joint paper), national bank supervisors' statements on AI in cloud security, and ISO/IEC 27017 and 42001 texts.
- **Web search use.** Four searches: DORA critical provider list (names via EBA PDF afterwards), the joint agentic guidance (to find mirrors), CSA 2026 survey releases, and the dates of the Unit 42 and IBM reports.

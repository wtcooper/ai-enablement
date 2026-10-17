# Security / application-security: practice angle (wave 4)

Compiled 2026-10-17. Archetype: security. Module: application-security. Angle: practice.

## 1. Summary

**What this covers.** How application security teams and providers use AI in 2026 for secure development, code review, scanning and testing, software supply chain security and product security, based on named deployments, vendor product documentation, firm and in-house engineering posts, maintainer accounts, conference abstracts, job postings and academic studies. 74 distinct sources are listed; all were opened and read at page or abstract level (no web searches were used; the research leads came from the landscape file and links followed from them).

**Candidate use cases.** 25, graded A: 8, B: 12, C: 5, D: 0 (see the YAML for rationale; use case 02 is capped at B because it measures general code review, and use cases 03, 12 and 18 rest partly on abstracts of conference talks for an event not yet held).

**Four findings that should steer the module**

1. **The bottleneck has moved from finding to closing.** Anthropic reports 6,157 vulnerabilities disclosed to 591 open-source projects with 516 patched upstream "to our knowledge" at 2026-10-02, and says human triage is the rate-limiting step (ANTHROPIC-CVD-2026). Meta's abstract says AI-written diffs fixed over 40% of its critical vulnerabilities without by themselves shortening time to fix (UNPROMPTED-2026). GitHub's advisory curators went from about a week to multiple weeks per advisory under a surge (GITHUB-ADVDB-2026). Practitioner designs now focus on verification, ownership and closure states (UC 06, 12, 21).
2. **The best evidence is self-measured by large engineering organisations and security firms; independent measurement is thin and contested.** Google, Meta, Mandiant, Trail of Bits and GitHub publish figures about their own use. Independent checks exist for adjacent questions (insecure AI-generated code, patch benchmarks, reviewer load) but not for AI appsec tools in production. The Trail of Bits and 1Password dispute and the memorisation finding on SusVibes show that vendor and academic benchmarks can overstate ability (UC 21, 23).
3. **Work is organised around harnesses, not prompts.** Google, Mandiant, GitHub and Trail of Bits all describe deterministic orchestration, validators, threat-model context and human approval gates around the model, and Google says a multi-agent harness can have substantial impact beyond the choice of model (GOOGLE-AGENTICSCAN-2026; GTIG-AVDH-2026; GITHUB-TASKFLOW-2026).
4. **AppSec roles are shifting towards building and operating agent systems, with humans as the judgement layer.** Anthropic's posting says Claude drives its static analysis, drafts fixes, does first-line bounty triage and assists threat modelling (ANTHROPIC-JOB-APPSEC-2026). Ten further job postings from nine other companies ask for AI-driven triage, testing or remediation tooling, for evaluating AI detection against labelled data, or for securing agentic applications.

## 2. Use cases

One YAML list, in the format of `research/briefs/templates/vocabulary.md`.

```yaml
- id: security-application-security-01
  title: Pre-submit agentic vulnerability scanning with triage and fix agents on every code change
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - software-systems
  - review-assurance
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: One-off security scans of large codebases are slow and lack context, so vulnerabilities are found late, while AI is increasing the amount of code that needs securing.
  solution: Google's AI Infrastructure team checks each code check-in with AI agents inside tools developers already use. A multi-agent review harness (Mantis, now open source) is matched to localized threat models built from live codebase metadata and a cross-package call graph. A quick scan is validated by a triage agent that uses abstract syntax tree parsing, call-graph traversal and pre-indexed safety rules to test whether the vulnerable path is reachable. A nightly post-submit scan is a second layer. A bug-fix agent builds fixes from the scan results and generated proofs and submits them for human review inside the original change request.
  outcomes:
  - lever: quality
    description: False-positive rates reduced with localized threat models
    figure: 3% in some cases
    measures: false-positive rate of the scanning agents 'in some cases'; the post gives no denominator, sample or baseline
    provenance: self-reported
    source_ref: GOOGLE-AGENTICSCAN-2026
  - lever: quality
    description: Triage agent confirms reachability quickly and precisely
    figure: over 92% precision, under one minute
    measures: precision of the triage agent's reachability proofs; the post does not state the sample
    provenance: self-reported
    source_ref: GOOGLE-AGENTICSCAN-2026
  - lever: risk
    description: Vulnerabilities stopped before they reach the code base or production
    figure: hundreds per month
    measures: Google's statement of vulnerabilities prevented per month by continuous scanning of every code change; no baseline or denominator given
    provenance: self-reported
    source_ref: GOOGLE-AGENTICSCAN-2026
  prerequisites:
  - Threat models that are kept current and exposed as live codebase metadata
  - Call-graph and AST parsing across packages and libraries
  - Pre-submit integration in the developer workflow
  - Separate harnesses, rules and context for the development, scanning and triage agents (the post's own advice)
  risks_and_guardrails:
  - Proposed fixes go to human review rather than landing automatically (GOOGLE-AGENTICSCAN-2026, 'Bug fix agents close the loop')
  - The post advises keeping development, scanning and triage systems separate to prevent bias and pairing lightweight AI scans with deterministic structural validation (GOOGLE-AGENTICSCAN-2026, 'Learnings and call to action')
  - No independent measurement of the figures was found
  human_checkpoints:
  - Reviewer approves each proposed fix as part of the change request
  role_evolution: The blog post does not describe role changes. The Google Cloud session abstract for [un]prompted 2026 (talk not yet delivered) says the team rebuilt its security engineering function around collaborative secure development, starting with Mantis for vulnerability discovery (UNPROMPTED-2026, 'Secure Product Development With Mantis').
  evidence_grade: A
  sources:
  - ref: GOOGLE-AGENTICSCAN-2026
    title: 'Changing the game: Using agentic AI to secure infrastructure code (page title: Using AI agents to secure Google infrastructure)'
    publisher: Google Cloud Blog (Google AI Infrastructure team)
    type: firm
    url: https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/
    date: '2026-09-19'
    access: full
    locator: 'Sections: Pervasive pre-submit agentic scanning; The importance of localized threat models; Specialized triage agents; Bug fix agents; Learnings'
  - ref: UNPROMPTED-2026
    title: '[un]prompted 2026 agenda (conference 2026-10-27 to 2026-10-29, San Francisco; abstracts of upcoming talks)'
    publisher: '[un]prompted (AI security practitioner conference)'
    type: conference
    url: https://unpromptedcon.org/agenda-10-2026/
    date: '2026-10-06'
    access: full
    locator: 'Session: Secure Product Development With Mantis (Nick Galloway, Ruchi Shah, Google Cloud)'
  last_reviewed: '2026-10-17'
  notes: All figures are Google's own and are 'in some cases' or unbounded; treat as in-house self-reported. Related talk abstract is for an event on 2026-10-27 to 2026-10-29, not yet held.
- id: security-application-security-02
  title: Risk-tiered automated review and landing of low-risk code changes
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - review-assurance
  - software-systems
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: AI coding agents increase code volume faster than reviewers can read it, so the share of changes that get timely review falls.
  solution: Meta's RADAR (Risk Aware Diff Auto Review) is a funnel that classifies each diff by authorship and source type, applies eligibility gates and static heuristics, scores it with a machine-learned Diff Risk Score, runs LLM-based automated code review and then deterministic validation before landing qualifying changes. A diff that does not qualify stays on the normal human review path.
  outcomes:
  - lever: capacity
    description: Volume handled by the funnel
    figure: 535K+ diffs reviewed, 331K+ landed
    measures: diffs reviewed and landed by RADAR (paper abstract; period not stated in the abstract)
    provenance: self-reported
    source_ref: ARXIV-2605.30208
  - lever: capacity
    description: Approval yield when the risk threshold is relaxed
    figure: 60.31% approve rate
    measures: approve rate after relaxing the Diff Risk Score threshold from the 25th to the 50th percentile
    provenance: self-reported
    source_ref: ARXIV-2605.30208
  - lever: quality
    description: Safety of RADAR-reviewed diffs compared with other diffs
    figure: revert rate one third, production incident rate one fiftieth
    measures: revert rate and Production Incident rate of RADAR-reviewed diffs relative to non-RADAR diffs; the abstract does not say the groups were randomised
    provenance: self-reported
    source_ref: ARXIV-2605.30208
  - lever: speed
    description: Review latency
    figure: over 330% reduction in median time to close; 35% reduction in median diff review wall time
    measures: as stated in the abstract; difference-in-differences analysis of efficiency outcomes
    provenance: self-reported
    source_ref: ARXIV-2605.30208
  prerequisites:
  - A trained diff risk model and eligibility rules
  - Telemetry on reverts and production incidents to calibrate the threshold
  - Deterministic validation steps before landing
  risks_and_guardrails:
  - The threshold trades automation yield against safety (the paper's second research question)
  - Outcome comparison is against non-RADAR diffs, which may differ in risk profile; the abstract does not describe controls beyond difference-in-differences for efficiency
  human_checkpoints:
  - Diffs that fail eligibility, risk-score or validation gates go to human reviewers
  role_evolution: The abstract frames the problem as a gap between code supply and reviewer bandwidth; it does not describe role changes.
  evidence_grade: B
  sources:
  - ref: ARXIV-2605.30208
    title: 'Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency'
    publisher: arXiv (Meta authors)
    type: academic
    url: https://arxiv.org/abs/2605.30208
    date: '2026-05-28'
    access: full
    locator: Abstract
  - ref: ARXIV-2607.01904
    title: 'AI Writes Faster Than Humans Can Review: A Longitudinal Study of an Enterprise 2x Mandate'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2607.01904
    date: '2026-07-02'
    access: full
    locator: 'Abstract: per-reviewer load roughly doubled and automated review overtook human review at another AI-forward company, merge and revert rates steady'
  last_reviewed: '2026-10-17'
  notes: 'Grade capped at B: this is general code review (revert and incident outcomes), not security-specific review. Only the arXiv abstract page was read, not the full paper. The ''330%'' phrasing is the abstract''s.'
- id: security-application-security-03
  title: Machine-written fixes for scanner alerts and critical vulnerabilities, delivered as reviewable changes
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - software-systems
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: GitHub says developers often have little secure-coding training, so fixing code-scanning alerts takes substantial effort; Snyk says its data as of October 2026 showed roughly eight new vulnerabilities introduced for every one remediated.
  solution: LLMs draft a fix for a code-scanning alert or a critical vulnerability and present it as a proposed change that a developer must review before accepting. GitHub's Copilot Autofix does this for CodeQL alerts on pull requests and default branches; Meta reports AI-written diffs for critical vulnerabilities; Google's bug-fix agent submits fixes inside the original change request; Snyk sells an agentic fix architecture.
  outcomes:
  - lever: speed
    description: Share of critical vulnerabilities fixed by AI-written diffs, with no faster fix by itself
    figure: over 40%
    measures: share of critical vulnerabilities fixed by AI-written diffs at Meta, from the abstract of an upcoming talk; denominator and period not stated. The abstract adds that this did not by itself reduce the time to fix
    provenance: self-reported
    source_ref: UNPROMPTED-2026
  - lever: quality
    description: Secure-and-functional fix rate with and without vendor security context
    figure: 74.6% to 85.4% (Claude Opus 4.6 alone vs with Snyk Intelligence)
    measures: share of about 150 single-vulnerability samples (50 Python, 54 JavaScript, 39 Java) where a hidden security test and a hidden functional test both pass on the first try; Snyk's own benchmark
    provenance: vendor-published
    source_ref: SNYK-AGENTFIX-2026
  prerequisites:
  - Scanner alerts or confirmed findings to fix
  - Test coverage so a developer can check that behaviour is unchanged (GitHub advises this)
  - Dependency-review controls for fixes that add or update packages
  risks_and_guardrails:
  - GitHub's application card says suggestions can be non-deterministic, semantically wrong, partial, at the wrong location, or can introduce fabricated dependencies, and that review is required (GITHUB-APPCARD-2026, section 7 Limitations)
  - GitHub tests Autofix on a harness of over 2,300 alerts and reports that 'many' suggestions could be committed as-is, but publishes no success rate (GITHUB-APPCARD-2026, Custom evaluations)
  - Meta's abstract reports that AI-written fixes did not by themselves shorten time to fix (UNPROMPTED-2026)
  - In a 15-day single-case study in a closed-source industrial C++ repository, AI-assisted remediation produced hundreds of commits that saturated build-on-commit CI and reviewer attention until changes were batched by directory and capped in size (ARXIV-2609.29172)
  human_checkpoints:
  - Developer reviews and accepts or edits every suggested fix
  - Fixes that add or update dependencies are checked before merge
  role_evolution: Developers evaluate a suggested fix instead of starting from a search for how to fix the issue (GITHUB-APPCARD-2026, section on intended uses).
  evidence_grade: B
  sources:
  - ref: UNPROMPTED-2026
    title: '[un]prompted 2026 agenda (conference 2026-10-27 to 2026-10-29, San Francisco; abstracts of upcoming talks)'
    publisher: '[un]prompted (AI security practitioner conference)'
    type: conference
    url: https://unpromptedcon.org/agenda-10-2026/
    date: '2026-10-06'
    access: full
    locator: 'Session: How Meta Changed Building Secure Software With AI (David Molnar, Meta)'
  - ref: GITHUB-APPCARD-2026
    title: 'Application card: GitHub security and quality AI features (page undated; date is retrieval date)'
    publisher: GitHub Docs
    type: vendor
    url: https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning
    date: '2026-10-17'
    access: full
    locator: 'Sections: Copilot Autofix; Limitations; Custom evaluations'
  - ref: SNYK-AGENTFIX-2026
    title: Benchmarking Secure-and-Functional Remediation and How Snyk Agent Fix Lifts Frontier-Model Fix Rates by over 14%
    publisher: Snyk Blog
    type: vendor
    url: https://snyk.io/blog/snyk-agent-fix-remediation-benchmark/
    date: '2026-08-18'
    access: full
    locator: Headline findings and Golden Tests design
  - ref: GOOGLE-AGENTICSCAN-2026
    title: 'Changing the game: Using agentic AI to secure infrastructure code (page title: Using AI agents to secure Google infrastructure)'
    publisher: Google Cloud Blog (Google AI Infrastructure team)
    type: firm
    url: https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/
    date: '2026-09-19'
    access: full
    locator: Bug fix agents close the loop
  - ref: SNYK-AGENTIC-2026
    title: 'Introducing Evo Agentic AppSec: Security That Keeps Up With AI Development'
    publisher: Snyk Blog
    type: vendor
    url: https://snyk.io/blog/announcing-snyk-agentic-appsec/
    date: '2026-10-15'
    access: full
    locator: 'Problem statement: introduced-to-remediated ratio, Snyk data as of October 2026'
  - ref: ARXIV-2609.29172
    title: 'Orchestrating AI-Assisted Code Remediation: Socio-Technical Bottlenecks in a Large Industrial Repository'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.29172
    date: '2026-09-24'
    access: full
    locator: 'Abstract: CI and review bottlenecks from mass AI remediation'
  last_reviewed: '2026-10-17'
  notes: The Meta figure is from a conference abstract for an event not yet held (2026-10-27 to 2026-10-29), so graded B rather than A. The Snyk figure is a vendor benchmark of its own product.
- id: security-application-security-04
  title: Expert-directed AI patching of open-source vulnerabilities in partnership with maintainers
  archetype: security
  module: application-security
  function: service-delivery
  work_types:
  - software-systems
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Frontier models produce a flood of security findings that stretched open-source maintainers must sort into real vulnerabilities and plausible false positives.
  solution: Trail of Bits, with OpenAI, pairs its engineers with open-source projects. Agents find bugs and write patches while the engineers direct the work, triage the findings and check the results; maintainers then decide whether to merge, revise or reject each pull request. A bot (Patchy) tracks findings and merged patches. Work includes tests, fuzzing harnesses and CI scanning as well as security fixes.
  outcomes:
  - lever: capacity
    description: First-week output
    figure: 64 pull requests and 51 issues across 19 projects; 37 pull requests merged
    measures: public tally at 2026-06-22; the post says private reports are not counted
    provenance: self-reported
    source_ref: TOB-PTP-2026
  - lever: quality
    description: Maintainer acceptance of submitted patches
    figure: 126 of 186 merged (67.7%)
    measures: Patch the Planet pull requests merged out of the 186 that maintainers had merged or closed by 2026-09-14; 60 closed without merging, 4 of those explicitly rejected on technical grounds
    provenance: self-reported
    source_ref: TOB-1PASSWORD-2026
  - lever: quality
    description: Merged patches that kept the proposed security fix
    figure: 91 of 126 (72.2%)
    measures: merged pull requests where maintainers accepted the security fix as originally proposed
    provenance: self-reported
    source_ref: TOB-1PASSWORD-2026
  prerequisites:
  - Access to frontier models, including a cyber-oriented model variant (the posts name GPT-5.5-Cyber)
  - Engineer time set aside for the work (the first week cleared dozens of engineers' schedules)
  - Coordinated-disclosure channels and a public tracking process
  risks_and_guardrails:
  - Trail of Bits discloses a freenginx case in which an agent-written patch left one vulnerable path open and added a crash during request cleanup; the maintainer's own fix had the same cleanup crash (TOB-1PASSWORD-2026)
  - The firm says its post-patch-validation skill was not used in the work reported (TOB-1PASSWORD-2026)
  - Maintainers decide what ships (TOB-PTP-2026; GITHUB-SECUREFUND-2026)
  human_checkpoints:
  - Trail of Bits engineers direct the agents and check results
  - Project maintainers decide whether to merge each pull request
  role_evolution: The firm says its experts orchestrate and triage findings and handle fixing and hardening alongside maintainers, rather than filing issues and leaving (TOB-PTP-2026).
  evidence_grade: A
  sources:
  - ref: TOB-PTP-2026
    title: Introducing Patch the Planet
    publisher: Trail of Bits Blog
    type: firm
    url: https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/
    date: '2026-06-22'
    access: full
    locator: First-week tally and project list
  - ref: TOB-1PASSWORD-2026
    title: 1Password's AI patching benchmark is misleading
    publisher: Trail of Bits Blog
    type: firm
    url: https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/
    date: '2026-09-15'
    access: full
    locator: Patch the Planet merge statistics and the freenginx case
  - ref: GITHUB-SECUREFUND-2026
    title: What 50 open source projects taught us about security in the AI era
    publisher: GitHub Blog
    type: vendor
    url: https://github.blog/open-source/maintainers/what-50-open-source-projects-taught-us-about-security-in-the-ai-era/
    date: '2026-08-13'
    access: full
    locator: 'Lesson: AI helps maintainers investigate, prioritize and respond; maintainers keep judgement and accountability'
  last_reviewed: '2026-10-17'
  notes: All figures are the firm's own. The merge rate counts only pull requests already merged or closed at 2026-09-14, so open ones are excluded.
- id: security-application-security-05
  title: Multi-agent vulnerability discovery harness run by consultants on client and incident code
  archetype: security
  module: application-security
  function: service-delivery
  work_types:
  - review-assurance
  - software-systems
  pattern: draft-review-loop
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Manual source-code review is slow, and when proprietary source code is exposed defenders must find and patch vulnerabilities before attackers do.
  solution: 'Google Threat Intelligence Group''s Mandiant uses an Agentic Vulnerability Discovery Harness (AVDH), built on Google''s Agent Development Kit, in proactive reviews, penetration tests, red team work and incident response. A deterministic pipeline chains specialist agents: explorers identify the codebase''s purpose and a threat model; discovery agents extract entry points; enrichment agents gather context; access-control and data-flow agents brainstorm hypotheses under a consultant-set confidence filter; later stages validate and rank findings for a human expert.'
  outcomes:
  - lever: speed
    description: Critical findings in one incident response
    figure: over 100 true-positive critical vulnerabilities in two days
    measures: count of true-positive critical vulnerabilities the harness found in a single investigation of stolen corporate repositories; the post says this took a fraction of manual review time and gives no baseline
    provenance: self-reported
    source_ref: GTIG-AVDH-2026
  - lever: quality
    description: Assigned CVEs from large-scale runs
    figure: 12 CVEs assigned
    measures: CVEs assigned for flaws in web extensions and open-source projects, from analysis spanning tens of millions of lines of code, thousands of pipelines and tens of thousands of findings
    provenance: self-reported
    source_ref: GTIG-AVDH-2026
  prerequisites:
  - Asset inventories, SBOMs, architecture documentation and threat intelligence as agent context
  - A distilled human knowledge base so agents pick relevant skills and vulnerability patterns
  - Agent orchestration framework (the post names Google ADK)
  risks_and_guardrails:
  - The harness orchestrates agents deterministically to limit LLM non-determinism (GTIG-AVDH-2026)
  - Early agents do minimal self-validation and are filtered by a consultant-configured confidence filter (GTIG-AVDH-2026)
  - 12 assigned CVEs against tens of thousands of findings shows that most findings do not become CVEs; the post does not give a precision rate
  human_checkpoints:
  - Consultant verifies the textual and visual threat model before analysis continues
  - Human expert reviews the prioritized, risk-rated findings
  role_evolution: The post says the framework lets humans focus their impact on routine-vulnerability discovery and validation that agents now augment (GTIG-AVDH-2026).
  evidence_grade: A
  sources:
  - ref: GTIG-AVDH-2026
    title: Staying Ahead of Adversarial AI Through Agentic Source Code Review
    publisher: Google Cloud Blog (Google Threat Intelligence Group / Mandiant)
    type: firm
    url: https://cloud.google.com/blog/topics/threat-intelligence/staying-ahead-of-adversarial-ai-through-agentic-source-code-review
    date: '2026-08-18'
    access: full
    locator: 'Sections: results after 10 months of use; pipeline description; threat model approval gate'
  last_reviewed: '2026-10-17'
  notes: Self-reported by Google's Mandiant and GTIG. The harness is described as an internal, point-in-time architecture.
- id: security-application-security-06
  title: Frontier-model scanning of widely used open-source projects with human triage before disclosure
  archetype: security
  module: application-security
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: full-population-testing
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Widely used open-source code has bugs that survived years of expert review and automated testing, and maintainers cannot afford large security teams.
  solution: Anthropic runs Claude models, including a Mythos Preview snapshot, over open-source repositories. Candidate findings go to one of six external security research firms that reproduce each issue, rate severity and write a report, and confirmed bugs are disclosed to maintainers under a coordinated disclosure policy. With Mozilla, Claude Opus 4.6 found vulnerabilities in Firefox, and Mozilla's triage process shaped what was submitted. An opt-in OSS Scanner now offers some projects reports straight from the model without human review.
  outcomes:
  - lever: quality
    description: Firefox findings in a two-week collaboration
    figure: 22 vulnerabilities, 14 rated high-severity by Mozilla
    measures: vulnerabilities Claude Opus 4.6 found in Firefox in February 2026; Anthropic says the 14 high-severity ones are almost a fifth of all high-severity Firefox vulnerabilities remediated in 2025
    provenance: vendor-published
    source_ref: ANTHROPIC-FIREFOX-2026
  - lever: capacity
    description: Disclosure ledger
    figure: 6,157 vulnerabilities disclosed across 591 projects; 516 patched upstream; 584 CVE or advisory identifiers
    measures: dashboard counts as of 2026-10-02 for findings discovered 2025-11-01 to 2026-10-02; 'patched' is 'to our knowledge'
    provenance: vendor-published
    source_ref: ANTHROPIC-CVD-2026
  - lever: quality
    description: True-positive rate of triaged findings
    figure: 92.7% true positives
    measures: share of manually reviewed findings that the external firms confirmed as valid; includes already-reported and won't-fix bugs; the retrieved dashboard text does not make the denominator unambiguous
    provenance: vendor-published
    source_ref: ANTHROPIC-CVD-2026
  prerequisites:
  - Access to the most capable models (gated through Anthropic's Cyber Verification Program)
  - External triage capacity and a coordinated-disclosure policy
  - Reproducible evidence in each report (Mozilla named three submission components that built trust)
  - 'For OSS Scanner: a Dockerfile so an offline agent can build and audit the project'
  risks_and_guardrails:
  - Anthropic says human triage is the rate-limiting step and the disclosed count is a subset of what models found (ANTHROPIC-CVD-2026)
  - Reports without human review may contain false positives (ANTHROPIC-CVD-2026; ANTHROPIC-OSSSCAN-2026)
  - In exploit tests of several hundred runs costing about $4,000, Opus 4.6 turned only two Firefox bugs into crude exploits, in an environment without the sandbox (ANTHROPIC-FIREFOX-2026)
  - Anthropic says the bottleneck is now verifying, disclosing and patching, not finding (ANTHROPIC-CYBERMISSION-2026; ANTHROPIC-EXPAND-2026)
  human_checkpoints:
  - External security firm reproduces and rates each finding before disclosure
  - Maintainers acknowledge, fix and decide whether to publish advisories
  role_evolution: Anthropic says it will shift its support from finding vulnerabilities to disclosing, fixing and deploying patched software (ANTHROPIC-EXPAND-2026). Mozilla researchers have started experimenting with Claude for security internally (ANTHROPIC-FIREFOX-2026).
  evidence_grade: A
  sources:
  - ref: ANTHROPIC-FIREFOX-2026
    title: Partnering with Mozilla on Firefox security
    publisher: Anthropic Frontier Red Team (red.anthropic.com)
    type: vendor
    url: https://red.anthropic.com/2026/firefox/
    date: '2026-03-06'
    access: full
    locator: Opening summary; task verifiers; exploit evaluation
  - ref: ANTHROPIC-CVD-2026
    title: Anthropic's coordinated vulnerability disclosure dashboard (counts as of 2026-10-02)
    publisher: Anthropic Frontier Red Team (red.anthropic.com)
    type: vendor
    url: https://red.anthropic.com/2026/cvd/
    date: '2026-10-02'
    access: full
    locator: Counts as of 2026-10-02; triage process and glossary
  - ref: ANTHROPIC-EXPAND-2026
    title: Expanding Project Glasswing
    publisher: Anthropic
    type: vendor
    url: https://www.anthropic.com/news/expanding-project-glasswing
    date: '2026-06-02'
    access: full
    locator: Partners' more than 10,000 high- or critical-severity flaws; bottleneck statement
  - ref: ANTHROPIC-OSSSCAN-2026
    title: OSS Scanner
    publisher: Anthropic Frontier Red Team (red.anthropic.com)
    type: vendor
    url: https://red.anthropic.com/oss-scanner
    date: 2026-10
    access: full
    locator: Fast-track without human review
  - ref: ANTHROPIC-GLASSWING-2026
    title: 'Project Glasswing: Securing critical software for the AI era'
    publisher: Anthropic
    type: vendor
    url: https://www.anthropic.com/glasswing
    date: '2026-04-07'
    access: full
    locator: Launch partners and claims
  last_reviewed: '2026-10-17'
  notes: All counts are vendor-published by the model provider and are not independently audited. Mozilla confirmed the high-severity ratings per Anthropic's account; no Mozilla-authored source was read. Glasswing partners' own results (more than 10,000 high- or critical-severity flaws) are reported by Anthropic, not by the partners.
- id: security-application-security-07
  title: Third-party AI-augmented audit of a single critical open-source project
  archetype: security
  module: application-security
  function: service-delivery
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: A heavily scrutinised project like curl still has undiscovered vulnerabilities, and its volunteer team cannot find them all alone.
  solution: Engineers at Aisle pointed AI-powered tooling at the curl source over about a year, with human security staff backing each finding, and worked closely with the curl team. The team published Aisle's audit report on its website as the fifth external audit.
  outcomes:
  - lever: quality
    description: Published curl vulnerabilities attributed to the Aisle work
    figure: 35 vulnerabilities with CVE identifiers
    measures: count stated by curl's lead maintainer of published curl vulnerabilities resulting from Aisle engineers' AI-assisted analysis over about a year
    provenance: independent
    source_ref: CURL-AISLE-2026
  prerequisites:
  - Close cooperation with maintainers
  - Humans who validate findings before reporting
  - Maintainer capacity to fix reports quickly
  risks_and_guardrails:
  - The maintainer says curl is continuously scanned by countless humans and AIs and that he cannot say how many or who (CURL-AISLE-2026)
  - The post does not report how many AI-generated candidates were rejected, so yield per finding is unknown
  human_checkpoints:
  - Aisle's skilled humans back up each finding
  - curl maintainers assess and fix reports
  role_evolution: The maintainer says Aisle employees have authored several dozen commits in curl (CURL-AISLE-2026), so the external auditors also act as contributors.
  evidence_grade: A
  sources:
  - ref: CURL-AISLE-2026
    title: A curl audit by Aisle
    publisher: daniel.haxx.se (Daniel Stenberg, curl lead maintainer)
    type: community
    url: https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/
    date: '2026-10-14'
    access: full
    locator: Whole post
  last_reviewed: '2026-10-17'
  notes: The count comes from the project lead, a third party to the vendor, hence 'independent', but it is a short blog post, not an audit of the audit. The source does not say which AI tools Aisle used.
- id: security-application-security-08
  title: 'Agent-built fuzzing campaigns: harnesses, coverage gap analysis and crash triage'
  archetype: security
  module: application-security
  function: service-delivery
  work_types:
  - software-systems
  - review-assurance
  pattern: draft-review-loop
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Fuzzing needs a human to watch coverage, write harnesses for unreached code and triage crashes, and that attention is the bottleneck.
  solution: GitHub Security Lab's Fuzzing Taskflow takes a C or C++ repository and lets an LLM agent identify entry points, analyse the build, write harnesses, run AFL++, read coverage reports, improve the harnesses and triage crashes into per-bug reports, with deterministic tools doing the execution and a database holding state. Trail of Bits drove GPT-5.5-Cyber through Codex's /goal command to build a zlib fuzzing lab with a strict definition of a reportable finding.
  outcomes:
  - lever: speed
    description: Time to stand up a bespoke fuzzing lab
    figure: built in under a day; Trail of Bits estimates two to three weeks for one fuzzing expert
    measures: the firm's estimate of manual effort for the zlib fuzzing lab; not measured
    provenance: self-reported
    source_ref: TOB-PTP-2026
  prerequisites:
  - A buildable C or C++ project and a disposable, unprivileged execution environment
  - A frontier model that does not refuse security tasks (GitHub notes some models impose guardrails; its default passed its internal tests)
  - Validity rules written into the goal so the agent does not report unreachable crashes (Trail of Bits)
  risks_and_guardrails:
  - GitHub warns that the taskflow runs afl-fuzz, clang and LLM-chosen build commands directly on the host, so a prompt-injected agent could do anything the user can; run it only in a disposable environment (GITHUB-TASKFLOW-2026)
  - Suggested patches are marked review required and the author says the agent does get things wrong (GITHUB-TASKFLOW-2026)
  - Without strong validity rules the agent produces high-confidence noise; weaker models escalate crashes that are not reachable (TOB-ZLIB-2026)
  human_checkpoints:
  - Human reviews each crash report and suggested diff
  - Disclosure of findings after maintainers patch
  role_evolution: GitHub's author hands coverage reading, harness writing, gap chasing and crash triage to the agent and treats verdicts as a prepared starting point for a human (GITHUB-TASKFLOW-2026).
  evidence_grade: B
  sources:
  - ref: GITHUB-TASKFLOW-2026
    title: AI-powered fuzzing with the GitHub Security Lab Taskflow Agent
    publisher: GitHub Blog
    type: vendor
    url: https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/
    date: '2026-09-24'
    access: full
    locator: Design rule; coverage loop; crash triage; warning on host execution
  - ref: TOB-ZLIB-2026
    title: GPT-5.5-Cyber built a zlib fuzzing lab in a day
    publisher: Trail of Bits Blog
    type: firm
    url: https://blog.trailofbits.com/2026/07/02/field-reports-from-patch-the-planet/
    date: '2026-07-02'
    access: full
    locator: Narrative of the zlib campaign and the validity-rule lesson
  - ref: TOB-PTP-2026
    title: Introducing Patch the Planet
    publisher: Trail of Bits Blog
    type: firm
    url: https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/
    date: '2026-06-22'
    access: full
    locator: 'Highlight: a fuzzing lab built in a day'
  last_reviewed: '2026-10-17'
  notes: The two-to-three-week figure is an estimate by the firm, not a measurement. The zlib findings were not yet public when the post was written.
- id: security-application-security-09
  title: Open-source security-agent taskflows tuned to one application class (Android) for targeted audits
  archetype: security
  module: application-security
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Mobile application vulnerability classes are less widely known, and LLM runs are non-deterministic, so a general prompt can miss essential classes.
  solution: A GitHub Security Lab researcher added taskflows that separate mobile entry points from non-mobile ones and that make the model check a fixed list of vulnerability classes for each entry point and component, then combined that strict prompt with a broad one over repeated runs. Results land in a SQLite table for the researcher to review before reporting.
  outcomes:
  - lever: quality
    description: Android application vulnerabilities found and reported
    figure: 24 (the text also says more than 20 reported)
    measures: vulnerabilities in Android applications that the researcher reported using the taskflows; the title says 24 and the text says 'more than 20', then 'in total ... 24'
    provenance: self-reported
    source_ref: GITHUB-ANDROID-2026
  prerequisites:
  - GitHub Copilot licence and premium model requests
  - Taskflow prompts maintained as YAML
  - 'Token budget: a run takes an hour or two on a medium-sized repository and can consume many tokens'
  risks_and_guardrails:
  - The author combines a strict prompt, a broad prompt and repeated runs because LLMs are non-deterministic (GITHUB-ANDROID-2026)
  - Findings are validated by the researcher and disclosed through advisories; the post gives no count of rejected candidates
  human_checkpoints:
  - Researcher reviews the audit_results table and reports confirmed vulnerabilities
  role_evolution: The framework lets security researchers automate, package and share the prompts and workflows that work for them (GITHUB-ANDROID-2026).
  evidence_grade: A
  sources:
  - ref: GITHUB-ANDROID-2026
    title: How we found 24 Android vulnerabilities using our open source AI security agent
    publisher: GitHub Blog
    type: vendor
    url: https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/
    date: '2026-09-28'
    access: full
    locator: 'Sections: intro; taskflow changes; results'
  last_reviewed: '2026-10-17'
  notes: Single-researcher account by the vendor's own security lab. No false-positive rate given.
- id: security-application-security-10
  title: Autonomous application penetration-testing agent that validates exploitability
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - review-assurance
  - software-systems
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Manual reviews and periodic pentests do not keep up with how fast code is written, and scanners report candidate issues without proof that they can be exploited.
  solution: AWS Security Agent (now part of AWS Continuum) is an autonomous penetration-testing agent. In AWS's test it started from an endpoint and a one-line hint, mapped the attack surface, used specialist agents to raise candidate risks, had a validator confirm or reject each before exploitation, then built exploits with a shell, Python runtime, browser and out-of-band listener. AWS audited every capture against the canonical proof of concept.
  outcomes:
  - lever: quality
    description: Exploits built end to end on recent real CVEs
    figure: 33 of 37 (89.2%)
    measures: recent CVEs (2025-2026) packaged as live containerised targets where the agent captured the flag through the intended vulnerability after an integrity audit; one run, 10-hour limit per sample; two further captures were reclassified as off-path and counted unsolved; two misses crashed the target
    provenance: vendor-published
    source_ref: AWS-SECAGENT-2026
  - lever: quality
    description: Validator filtering of the agent's own findings
    figure: 159 auto-labelled false positives of 475 surfaced findings; over 1,200 more de-duplicated
    measures: counts from the pipeline's validation layer in the same run
    provenance: vendor-published
    source_ref: AWS-SECAGENT-2026
  prerequisites:
  - Live or sandboxed target environment with seed credentials
  - Non-destructive guardrails for production engagements (AWS says these govern production use)
  - A contamination-reduced benchmark of recent CVEs to measure progress
  risks_and_guardrails:
  - In both misses the agent exploited the bug and then took the target down; AWS says non-destructive guardrails keep that off customer systems (AWS-SECAGENT-2026)
  - AWS reports the result as contamination-reduced, not contamination-free, and the benchmark covers known-CVE reproduction, not novel discovery (AWS-SECAGENT-2026)
  - Self-test by the vendor; the post does not name customers
  human_checkpoints:
  - Not stated for customer engagements in the post
  role_evolution: Not stated.
  evidence_grade: C
  sources:
  - ref: AWS-SECAGENT-2026
    title: AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs
    publisher: AWS Security Blog
    type: vendor
    url: https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/
    date: '2026-10-15'
    access: full
    locator: Summary results; benchmark design; finding validation; integrity audit
  last_reviewed: '2026-10-17'
  notes: Vendor lab test, not a customer deployment. The post says the run used Claude Opus 5 as the model. XBOW and Wiz also market autonomous testing agents; only their blog listings were seen, so they are not evidence here.
- id: security-application-security-11
  title: Reasoning-based code scanning that builds a threat model, validates findings and proposes a patch
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - review-assurance
  - software-systems
  pattern: end-to-end-case-agent
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: Rule-based static analysis matches known patterns and misses business-logic and access-control flaws, while teams already spend significant time triaging noisy findings.
  solution: Agentic scanners read the repository, build a project-specific threat model that the team can edit, search for vulnerabilities, test findings in a sandbox where possible and propose a fix. OpenAI's Codex Security (formerly Aardvark), Anthropic's Claude Code Security, Wiz AI SAST, Semgrep Agentic Workflows and Snyk's Code Scanning Agent follow this pattern. Findings are filtered by severity and confidence and nothing is applied without human approval.
  outcomes:
  - lever: quality
    description: Noise reduction during OpenAI's beta
    figure: 84% less noise in one case; over-reported severity down over 90%; false-positive rate down over 50% across repositories
    measures: changes since initial rollout when scanning the same repositories in OpenAI's beta cohort; OpenAI does not state baselines or sample sizes
    provenance: vendor-published
    source_ref: OPENAI-CODEXSEC-2026
  - lever: capacity
    description: Beta scanning volume
    figure: '1.2 million commits in 30 days: 792 critical and 10,561 high-severity findings'
    measures: external beta repositories over the last 30 days before the post; critical findings appeared in under 0.1% of commits
    provenance: vendor-published
    source_ref: OPENAI-CODEXSEC-2026
  - lever: quality
    description: Recall on test repositories (Aardvark)
    figure: 92%
    measures: known and synthetically introduced vulnerabilities identified in OpenAI's 'golden' repositories
    provenance: vendor-published
    source_ref: OPENAI-AARDVARK-2025
  - lever: quality
    description: True positives found per unit cost versus a model alone
    figure: 3.5x more true positives at 19% lower cost per true positive
    measures: Semgrep's own benchmarking of AI-powered detection versus Opus 4.8 alone; the post does not describe the benchmark
    provenance: vendor-published
    source_ref: SEMGREP-AGENTICWF-2026
  prerequisites:
  - A buildable project environment (OSS Scanner requires a Dockerfile so an offline agent can build and audit)
  - A reviewed threat model
  - Security-team time to adjust finding criticality, which the tool uses as feedback (OpenAI)
  risks_and_guardrails:
  - Each vendor says a human approves patches (ANTHROPIC-CCS-2026; OPENAI-CODEXSEC-2026)
  - An [un]prompted abstract from AISLE reports that an LLM scanner can miss a real bug on one run and find it on the next, across 25,000 trials on 50 models; repeated passes and diverse cheaper models helped (UNPROMPTED-2026)
  - Contaminated or memorised benchmarks can inflate results (see use case 23)
  - Semgrep's design partners were unnamed; their 'virtually all true positives' claim is vendor-reported (SEMGREP-AGENTICWF-2026)
  human_checkpoints:
  - Analyst or developer reviews validated findings and approves patches
  - Team edits the threat model and finding criticality
  role_evolution: Anthropic says developers always make the call on patches; Snyk says teams focus on setting policy and owning decisions while agents do program work (ANTHROPIC-CCS-2026; SNYK-AGENTIC-2026).
  evidence_grade: B
  sources:
  - ref: OPENAI-CODEXSEC-2026
    title: 'Codex Security: now in research preview'
    publisher: OpenAI
    type: vendor
    url: https://openai.com/index/codex-security-now-in-research-preview/
    date: '2026-03-06'
    access: full
    locator: Intro; How it works; named early users NETGEAR and vLLM; scan statistics
  - ref: OPENAI-AARDVARK-2025
    title: 'Introducing Aardvark: OpenAI''s agentic security researcher (page updated 2026-03-06 to say Aardvark is now Codex Security)'
    publisher: OpenAI
    type: vendor
    url: https://openai.com/index/introducing-aardvark/
    date: '2025-10-30'
    access: full
    locator: Benchmark testing on golden repositories
  - ref: ANTHROPIC-CCS-2026
    title: Making frontier cybersecurity capabilities available to defenders (Claude Code Security)
    publisher: Anthropic
    type: vendor
    url: https://www.anthropic.com/news/claude-code-security
    date: '2026-02-20'
    access: full
    locator: Limited research preview; multi-stage verification; human approval
  - ref: WIZ-AISAST-2026
    title: 'Wiz AI SAST: AI Code Security With Code-to-Cloud Context'
    publisher: Wiz Blog
    type: vendor
    url: https://www.wiz.io/blog/introducing-wiz-ai-sast
    date: '2026-10-06'
    access: full
    locator: Public preview announcement, 2026-10-06
  - ref: SEMGREP-AGENTICWF-2026
    title: 'Introducing Semgrep Agentic Workflows: Automate Deep Vulnerability Hunting at Scale (date from the Semgrep blog listing)'
    publisher: Semgrep Blog
    type: vendor
    url: https://semgrep.dev/blog/2026/introducing-semgrep-agentic-workflows-automate-deep-vulnerability-hunting-at-scale
    date: '2026-07-28'
    access: full
    locator: Nine agentic workflows in public beta; design partner feedback; benchmark claim
  - ref: SNYK-AGENTIC-2026
    title: 'Introducing Evo Agentic AppSec: Security That Keeps Up With AI Development'
    publisher: Snyk Blog
    type: vendor
    url: https://snyk.io/blog/announcing-snyk-agentic-appsec/
    date: '2026-10-15'
    access: full
    locator: Evo Code Scanning Agent and Security Review Agent
  - ref: UNPROMPTED-2026
    title: '[un]prompted 2026 agenda (conference 2026-10-27 to 2026-10-29, San Francisco; abstracts of upcoming talks)'
    publisher: '[un]prompted (AI security practitioner conference)'
    type: conference
    url: https://unpromptedcon.org/agenda-10-2026/
    date: '2026-10-06'
    access: full
    locator: 'Session: The Scanner Said Clean. We Ran It Again (Petr Simecek, AISLE)'
  last_reviewed: '2026-10-17'
  notes: Graded B because OpenAI names early-access users (NETGEAR, vLLM) but all outcome figures are vendor-published. OpenAI says the 2026-03-06 date is also when Aardvark became Codex Security. The AISLE abstract is for an upcoming talk.
- id: security-application-security-12
  title: Reachability-first triage and closure tracking for AI-generated vulnerability candidates
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - review-assurance
  - data-reporting
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: AI-assisted programs generate more vulnerability candidates and patch pull requests than engineering teams can review, so an opened pull request is not a fixed bug.
  solution: Rubrik's product security lead describes an operating loop that moves each verified finding to merge, rejection, deferral or formal risk acceptance, using root-cause de-duplication, reachability-first ranking, typed refutation reasons, explicit ownership, detector replay, and a refusal to auto-patch bug classes that cannot be validated cheaply. Opened, reviewed and fixed are kept as separate states. Google's triage agent likewise proves reachability using call-graph analysis before a finding reaches a developer.
  outcomes:
  - lever: quality
    description: Operating-loop results
    figure: none published
    measures: the abstract lists the loop's components but no measured results
    provenance: self-reported
    source_ref: UNPROMPTED-2026
  prerequisites:
  - Closure-state schema that separates opened, reviewed and fixed
  - Ownership data per finding
  - Detectors that can be replayed to check a fix
  risks_and_guardrails:
  - The abstract says a passing build does not prove the vulnerable path is gone and that pull-request volume can hide the review bottleneck (UNPROMPTED-2026)
  - The abstract cites Anthropic's Glasswing update as saying a high or critical bug found by Mythos Preview takes two weeks to patch on average; that update was not located, so this is second-hand
  human_checkpoints:
  - Engineers review before merge; formal risk acceptance by an accountable owner
  role_evolution: The abstract says that once discovery is cheap, review and closure are the scarce resource (UNPROMPTED-2026).
  evidence_grade: B
  sources:
  - ref: UNPROMPTED-2026
    title: '[un]prompted 2026 agenda (conference 2026-10-27 to 2026-10-29, San Francisco; abstracts of upcoming talks)'
    publisher: '[un]prompted (AI security practitioner conference)'
    type: conference
    url: https://unpromptedcon.org/agenda-10-2026/
    date: '2026-10-06'
    access: full
    locator: 'Session: Opened Is Not Fixed (Shayaun Nejad, Rubrik)'
  - ref: GOOGLE-AGENTICSCAN-2026
    title: 'Changing the game: Using agentic AI to secure infrastructure code (page title: Using AI agents to secure Google infrastructure)'
    publisher: Google Cloud Blog (Google AI Infrastructure team)
    type: firm
    url: https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/
    date: '2026-09-19'
    access: full
    locator: Specialized triage agents
  - ref: ARXIV-2601.02941
    title: 'SastBench: A Benchmark for Testing Agentic SAST Triage'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2601.02941
    date: '2026-01-06'
    access: full
    locator: 'Abstract: SAST false positives require costly manual triage; benchmark for agentic triage'
  - ref: OPENAI-CODEXDOCS-2026
    title: Codex Security (product documentation; page undated, date is retrieval date)
    publisher: OpenAI Developers
    type: vendor
    url: https://developers.openai.com/codex/security
    date: '2026-10-17'
    access: full
    locator: 'Task: triage a backlog (findings from another scanner or issue tracker)'
  - ref: ANTHROPIC-CYBERMISSION-2026
    title: Introducing the Anthropic Cyber Mission
    publisher: Anthropic
    type: vendor
    url: https://www.anthropic.com/news/anthropic-cyber-mission
    date: '2026-10-08'
    access: full
    locator: Verifying, prioritizing and fixing remain the challenge
  last_reviewed: '2026-10-17'
  notes: Abstract of a talk not yet delivered, so no measurements. SastBench was read at abstract level only.
- id: security-application-security-13
  title: Agentic secure code review of pull requests before merge
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: Lightweight pre-merge analysis tools are noisy and miss context-dependent vulnerabilities, while deep security assessment is deferred to later stages, which delays feedback and raises the cost of fixing.
  solution: AgenticSCR, studied at Atlassian, is an agent with code navigation and security-focused semantic memory that reviews code before integration and comments on probable vulnerabilities. In practice, Anthropic's Claude Code GitHub Action reviews each pull request and posts inline comments with fix recommendations, and Semgrep runs managed scans on every pull request in Cursor Origin.
  outcomes:
  - lever: quality
    description: Review comments judged correct versus baselines
    figure: at least 153% relative improvement
    measures: comments with correct localisation, vulnerability type and relevance versus a static LLM baseline, a multi-agent reviewer and SAST tools, in the paper's evaluation
    provenance: self-reported
    source_ref: ARXIV-2601.19138
  - lever: quality
    description: Share of comments validated in a shadow deployment
    figure: 54%
    measures: comments validated by security engineers for developer reporting in a shadow deployment
    provenance: self-reported
    source_ref: ARXIV-2601.19138
  prerequisites:
  - Code navigation tools for the agent and a security knowledge base (the paper's semantic memory)
  - Security engineers to validate comments during a shadow period
  - Pull request integration
  risks_and_guardrails:
  - Only about half of comments were validated in shadow mode, which the authors say underscores the difficulty of the task (ARXIV-2601.19138)
  - Anthropic's account of caught vulnerabilities (a DNS-rebinding RCE and an SSRF in internal tools) is an anecdote with no counts (ANTHROPIC-SECREVIEW-2025)
  - Humans caught seeded flaws only 3% to 61% of the time in a 2022 study of 150 participants, so the human baseline is weak but the study tested two specific flaws, not a general rate (ARXIV-2202.04586, via SEMGREP-ENDCR-2026)
  human_checkpoints:
  - Security engineers validated comments before developer reporting in the shadow deployment
  - Developers act on inline comments
  role_evolution: Not stated beyond security engineers acting as validators of AI comments.
  evidence_grade: A
  sources:
  - ref: ARXIV-2601.19138
    title: 'AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2601.19138
    date: '2026-01-27'
    access: full
    locator: Abstract
  - ref: ANTHROPIC-SECREVIEW-2025
    title: Automate security reviews with Claude Code
    publisher: Anthropic
    type: vendor
    url: https://www.anthropic.com/news/automate-security-reviews-with-claude-code
    date: '2025-08-06'
    access: full
    locator: The /security-review command and GitHub Action; examples caught internally
  - ref: SEMGREP-CURSOR-2026
    title: 'Cursor Origin Security Scanning: Semgrep Checks Every PR'
    publisher: Semgrep Blog
    type: vendor
    url: https://semgrep.dev/blog/2026/cursor-origin-security-scanning
    date: '2026-10-14'
    access: full
    locator: Scans on every pull request in Cursor Origin
  - ref: ARXIV-2202.04586
    title: 'Less is More: Supporting Developers in Vulnerability Detection during Code Review'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2202.04586
    date: '2022-02-09'
    access: full
    locator: 'Abstract: asking reviewers to focus on security raised detection probability eightfold; checklist added little'
  last_reviewed: '2026-10-17'
  notes: Study setting is Atlassian per the abstract; author affiliations were not checked, so provenance is marked self-reported. Shadow deployment means comments were not sent to developers, hence piloting. The 3% to 61% figures are quoted by Semgrep's blog, not read in the 2022 paper's body.
- id: security-application-security-14
  title: 'Security guardrails inside coding agents: scanning, rules files and hooks at the point of generation'
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - software-systems
  - review-assurance
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Coding agents write production code that people review less, and independent studies find security flaws in a large share of AI-generated code.
  solution: 'Security checks are attached to the coding agent''s own loop: IDE and MCP integrations scan every file an agent touches (Semgrep Guardian, Snyk Studio in Snowflake Cortex Code), organisations write security custom-instruction files and reusable rule packs for agents (OpenSSF guide; Reddit''s product security posting), and package firewalls block malicious dependencies during generation.'
  outcomes:
  - lever: capacity
    description: Scan volume and speed
    figure: over 3 million scans a week; 95% complete in under 5 seconds
    measures: scans across Semgrep's customer base and the share finishing under five seconds, as stated by the vendor
    provenance: vendor-published
    source_ref: SEMGREP-GUARDIAN-2026
  - lever: risk
    description: Critical issues prevented at one customer
    figure: over 180 a week
    measures: critical issues prevented per week at one unnamed B2B SaaS company after rollout; no baseline stated
    provenance: vendor-published
    source_ref: SEMGREP-GUARDIAN-2026
  prerequisites:
  - Agent-side hooks or MCP support in the coding tools in use
  - Central policy for what is blocked, fixed or sent to review
  - Enterprise deployment through MDM or agent admin controls (Semgrep)
  risks_and_guardrails:
  - 'Independent measurements show the underlying risk: 55.8% of 3,500 LLM-generated artifacts had at least one vulnerability (formal-verification study, 500 security-critical prompts, 7 models), and explicit security instructions cut the rate only by about 4 points (ARXIV-2604.05292)'
  - Veracode reports risky flaws in 45% of tests across over 100 LLMs and says larger, newer models did not improve security (VERACODE-GENAI-2025, vendor)
  - A CodeQL analysis of 7,703 GitHub files attributed to AI tools found 87.9% had no identifiable CWE-mapped vulnerability, with Python worse than JavaScript and TypeScript (ARXIV-2510.26103)
  - A study of top-1,000 GitHub repositories (2022-2025) found AI-written code concentrated in glue code, tests and boilerplate, with core logic and security-critical configuration mostly human-written, and that AI-introduced defects persisted longer where review was shallow (ARXIV-2512.18567)
  - The OpenSSF guide says the developer stays responsible and that engineering practices such as code review, testing and static analysis still apply (OPENSSF-AIGUIDE-2025)
  - A July 2026 poster (2,700 test cases, eight LLMs) found average vulnerability rates above 56% across three realistic risk scenarios (ambiguous requirements, under-specified operational context, security-functionality conflict), and that security-aware prompting gave up to 45% improvement (ARXIV-2607.23088)
  human_checkpoints:
  - Security team sets policy; developers review agent output as for any contributor
  role_evolution: Reddit's posting asks for a staff engineer to make the secure path the easiest path for engineers and AI agents (REDDIT-JOB-PSE-2026).
  evidence_grade: C
  sources:
  - ref: SEMGREP-GUARDIAN-2026
    title: 'Introducing Semgrep Guardian: Real-Time Security for AI-Written Code (date from the Semgrep blog listing)'
    publisher: Semgrep Blog
    type: vendor
    url: https://semgrep.dev/blog/2026/introducing-semgrep-guardian-real-time-security-for-ai-written-code
    date: '2026-06-23'
    access: full
    locator: Guardian description and customer statistics
  - ref: SNYK-SNOWFLAKE-2026
    title: Snyk Studio for Snowflake Cortex Code
    publisher: Snyk Blog
    type: vendor
    url: https://snyk.io/blog/announcing-snyk-studio-integration-snowflake-cortex-code/
    date: '2026-07-30'
    access: full
    locator: Snyk Studio inside Snowflake Cortex Code
  - ref: OPENSSF-AIGUIDE-2025
    title: Security-Focused Guide for AI Code Assistant Instructions
    publisher: OpenSSF Best Practices and AI/ML Working Groups
    type: standard-setter
    url: https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions
    date: '2025-08-01'
    access: full
    locator: Guide purpose and principles
  - ref: REDDIT-JOB-PSE-2026
    title: 'Job posting: Staff Product Security Engineer'
    publisher: Reddit (Greenhouse)
    type: job-posting
    url: https://job-boards.greenhouse.io/reddit/jobs/7868511
    date: '2026-04-29'
    access: full
    locator: 'Responsibilities: reusable rule packs and skills for coding agents'
  - ref: ARXIV-2604.05292
    title: 'Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2604.05292
    date: '2026-04-07'
    access: full
    locator: Abstract
  - ref: VERACODE-GENAI-2025
    title: 2025 GenAI Code Security Report (landing page; Oct 2025 update; page last modified 2026-07-09)
    publisher: Veracode
    type: vendor
    url: https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/
    date: '2025-07-25'
    access: full
    locator: Landing page summary
  - ref: ARXIV-2510.26103
    title: 'Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis of Public GitHub Repositories'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2510.26103
    date: '2025-10-30'
    access: full
    locator: Abstract
  - ref: ARXIV-2607.23088
    title: 'Poster: Rethinking Security in LLM Code Generation through Real-World Risk Scenarios'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2607.23088
    date: '2026-07-25'
    access: full
    locator: Abstract
  - ref: ARXIV-2512.18567
    title: 'AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code in Modern Software'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2512.18567
    date: '2025-12-21'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-17'
  notes: 'Grade C: the only deployment outcomes are vendor statistics; the Reddit posting shows intent to build such controls, not that they exist. Semgrep''s page names Notion, Snowflake and Dropbox as customers of its platform, not of Guardian specifically.'
- id: security-application-security-15
  title: Agents that upgrade vulnerable dependencies and prove the upgrade builds and removes the vulnerability
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - software-systems
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Most vulnerable packages already have a fixed version, but upgrading safely is hard because most are transitive, about a quarter need a major version bump and even minor releases can break builds.
  solution: A remediation agent applies one recommended upgrade per task, runs the build and tests, rescans, and repairs errors before finishing. Snyk's Evo Remediation Agent is the product example; Anthropic lists automated dependency vulnerability remediation across its own code base as a representative project for its application security team, and GitLab's code security team posting describes a service that turns security advisories into automated dependency-update merge requests (the posting does not say the service uses AI).
  outcomes:
  - lever: quality
    description: Pass rate on real dependency upgrades, all agents on Claude Sonnet 5.5
    figure: Evo Remediation Agent 90.2%; Claude Code with Snyk scan 77.5%; Claude Code unaided 59.6%; package-manager bump with no AI 46.9%
    measures: share of 307 upgrade tasks across 43 repositories and 2,066 fixable vulnerabilities that passed all gates (vulnerabilities removed, project installs, builds and passes tests) when checked in a clean container; Snyk's own VulnBump benchmark
    provenance: vendor-published
    source_ref: SNYK-VULNBUMP-2026
  prerequisites:
  - Projects that install, build and pass most of their tests before the change
  - Scanner data to confirm the vulnerability is gone
  - Policy on which upgrades auto-merge, which need review
  risks_and_guardrails:
  - In 70 of 124 failures, unaided Claude Code said it had fixed vulnerabilities that a rescan still found (SNYK-VULNBUMP-2026)
  - Build success was about 93% for all three agents, so removing the vulnerability, not keeping the build green, was the hard part (SNYK-VULNBUMP-2026)
  - GitHub warns that AI fixes may suggest fabricated or unsupported dependency versions (GITHUB-APPCARD-2026)
  - Snyk says deterministic engines should verify proposed fixes rather than the model that wrote them (SNYK-AGENTIC-2026)
  human_checkpoints:
  - Teams define policies and acceptance criteria; items outside policy go to human review (SNYK-AGENTIC-2026)
  role_evolution: Not stated beyond security teams owning policy and agents doing the upgrades.
  evidence_grade: C
  sources:
  - ref: SNYK-VULNBUMP-2026
    title: 'VulnBump: Can AI Agents Safely Fix Dependencies?'
    publisher: Snyk Blog
    type: vendor
    url: https://snyk.io/blog/vulnbump/
    date: '2026-10-15'
    access: full
    locator: Findings and method
  - ref: SNYK-AGENTIC-2026
    title: 'Introducing Evo Agentic AppSec: Security That Keeps Up With AI Development'
    publisher: Snyk Blog
    type: vendor
    url: https://snyk.io/blog/announcing-snyk-agentic-appsec/
    date: '2026-10-15'
    access: full
    locator: Evo Remediation Agent
  - ref: ANTHROPIC-JOB-APPSEC-2026
    title: 'Job posting: Staff+ Application Security Engineer (first published 2025-01-22, updated 2026-08-21)'
    publisher: Anthropic (Greenhouse)
    type: job-posting
    url: https://job-boards.greenhouse.io/anthropic/jobs/4502508008
    date: '2026-08-21'
    access: full
    locator: 'Representative project: automated dependency vulnerability remediation'
  - ref: GITLAB-JOB-CODESEC-2026
    title: 'Job posting: Senior Software Engineer, Security Factory: Code Security'
    publisher: GitLab (Greenhouse)
    type: job-posting
    url: https://job-boards.greenhouse.io/gitlab/jobs/8738179002
    date: '2026-10-09'
    access: full
    locator: 'Responsibilities: advisories to dependency-update merge requests'
  last_reviewed: '2026-10-17'
  notes: The benchmark and the product belong to the same vendor. Snyk also reports from its own data that 94% of 459 million findings over six months had a known fixed version and only about 10% had been resolved; that is a vendor statistic about backlog, not about the agent.
- id: security-application-security-16
  title: Malicious-package detection, incident blast-radius scanning and install-time blocking
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - review-assurance
  - transaction-processing
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Malicious packages are reaching developer machines before any pull-request scan runs, and teams scramble to learn whether a breaking supply chain incident affects them.
  solution: Vendors add three automated layers. Semgrep says it updates its malware database with AI-assisted, expert-verified rules within minutes of a major incident, rescans customer repositories with only the new advisories, and triggers org-wide policies such as tickets and alerts; a malware firewall in private beta intercepts dependency requests at the network level. Snyk's Dependency Firewall blocks malicious and out-of-policy packages at install time, including when coding agents install them.
  outcomes:
  - lever: speed
    description: Time from incident to updated detection
    figure: within minutes
    measures: Semgrep's statement of how fast its on-call monitoring updates the malware database with AI-assisted, expert-verified rules after a major supply chain incident; no measured distribution
    provenance: vendor-published
    source_ref: SEMGREP-MALWARE-2026
  prerequisites:
  - Repository inventory and dependency data for rescans
  - Organisation-wide response policies (tickets, alerts, webhooks)
  - Package-manager integration for install-time blocking
  risks_and_guardrails:
  - AI-generated code can reference package names that do not exist; a research detector reached 76% hallucination-free runs on 300 prompts and found that half of flagged hallucinations were lookalike packages already registered on PyPI (ARXIV-2608.23897)
  - GitHub's application card warns of fabricated dependencies in suggested fixes (GITHUB-APPCARD-2026)
  - Semgrep's rules are expert-verified, so AI assists rather than decides
  human_checkpoints:
  - Expert verifies AI-assisted rules before they publish (Semgrep)
  role_evolution: Not stated.
  evidence_grade: C
  sources:
  - ref: SEMGREP-MALWARE-2026
    title: Introducing Malware Detection and Response Automation
    publisher: Semgrep Blog
    type: vendor
    url: https://semgrep.dev/blog/2026/introducing-malware-detection-and-response-automation
    date: '2026-09-24'
    access: full
    locator: Malware detection and response automation; malware firewall (private beta)
  - ref: SNYK-AGENTIC-2026
    title: 'Introducing Evo Agentic AppSec: Security That Keeps Up With AI Development'
    publisher: Snyk Blog
    type: vendor
    url: https://snyk.io/blog/announcing-snyk-agentic-appsec/
    date: '2026-10-15'
    access: full
    locator: Evo Dependency Firewall
  - ref: ARXIV-2608.23897
    title: 'Names Can Hurt: Spotting Slopsquatting Risks Caused by Package Name Hallucinations in Local Coding LLMs'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2608.23897
    date: '2026-08-24'
    access: full
    locator: Abstract
  - ref: GITHUB-APPCARD-2026
    title: 'Application card: GitHub security and quality AI features (page undated; date is retrieval date)'
    publisher: GitHub Docs
    type: vendor
    url: https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning
    date: '2026-10-17'
    access: full
    locator: Dependency changes limitation
  last_reviewed: '2026-10-17'
  notes: Vendor announcements only. Semgrep cites an estimate of 1.8 million malicious packages in Q2 2026 and Snyk cites more than 20 high-profile attacks in 2026; both are unverified vendor figures and are not used as outcomes.
- id: security-application-security-17
  title: AI-assisted research for curators of a vulnerability advisory database
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - research-synthesis
  - transaction-processing
  pattern: intake-triage
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Advisory submissions surged, and the hard ones need package disambiguation, version-range reconstruction, multi-ecosystem verification and reconciliation of conflicting upstream data, which takes human time.
  solution: GitHub gave curators of the Advisory Database AI-powered assistance during the research phase of advisory review and improved automation for extracting data from upstream CVE information. Curators still make every decision, and reviewed advisories remain human-validated.
  outcomes:
  - lever: capacity
    description: Advisory output during the surge
    figure: 1,560 reviewed advisories in May 2026, over five times a typical month
    measures: reviewed advisories published by the GitHub Advisory Database in May 2026; the post attributes the output to the whole programme, not to the AI tooling
    provenance: self-reported
    source_ref: GITHUB-ADVDB-2026
  - lever: speed
    description: Processing time under load
    figure: about a week, then multiple weeks for a meaningful share
    measures: GitHub's account of publication times since mid-April; internal goals not consistently met despite the AI-assisted tooling
    provenance: self-reported
    source_ref: GITHUB-ADVDB-2026
  prerequisites:
  - Human-validated review standard
  - Triage and prioritisation of inbound submissions
  risks_and_guardrails:
  - GitHub says publishing faster by skipping verification would increase false positives at scale (GITHUB-ADVDB-2026)
  - 'Throughput, not data quality, was the failing point: CVE assignment rate held between 91% and 94% (GITHUB-ADVDB-2026)'
  human_checkpoints:
  - Curators make every decision on advisories
  role_evolution: Curators keep decision authority and receive AI help for routine research (GITHUB-ADVDB-2026).
  evidence_grade: B
  sources:
  - ref: GITHUB-ADVDB-2026
    title: Inside the Advisory Database and what happens when vulnerability volume breaks records
    publisher: GitHub Blog
    type: vendor
    url: https://github.blog/security/supply-chain-security/inside-the-advisory-database-and-what-happens-when-vulnerability-volume-breaks-records/
    date: '2026-06-29'
    access: full
    locator: 'Sections: the surge; building AI-assisted research tools; expanding automation'
  last_reviewed: '2026-10-17'
  notes: No measurement of the AI tooling's own effect was published. Private vulnerability reports rose from about 550 a week in January to over 3,000 a week for most of May, per the same post. NIST's own AI-enabled NVD effort is routed to vulnerability-exposure.
- id: security-application-security-18
  title: Agent-assisted security design review and threat-modelling intake
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - expert-judgment
  - document-production
  - coordination-scheduling
  pattern: end-to-end-case-agent
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Security reviews are a chronic bottleneck because specialists manually gather context while developers wait.
  solution: Stripe describes AI agents that manage the security review lifecycle from context gathering and threat modelling to ticket creation, risk tracking and fix verification, with scoped authority and evidence-based outputs so human experts focus on complex architectural decisions. Anthropic's application security team lists AI-assisted threat modelling that generates intake questions, drafts the model and recommends which design reviews need a human, and MongoDB's assessments team lists AI-based analysis for threat modelling.
  outcomes:
  - lever: speed
    description: Security review duration
    figure: from weeks to minutes
    measures: Stripe's description in a conference abstract of its self-service agent workflow; the abstract gives no sample or definition of a review
    provenance: self-reported
    source_ref: UNPROMPTED-2026
  prerequisites:
  - Scoped agent authority with evidence-based outputs
  - A repeatable framework for choosing agent-worthy workflows (Stripe)
  - Ticketing and risk-tracking integration
  risks_and_guardrails:
  - Stripe says it uses scoped authority and evidence-based outputs so experts can verify (UNPROMPTED-2026)
  - Anthropic describes AI recommending which reviews need a human, so a mis-triage would skip expert review; no controls are described (ANTHROPIC-JOB-APPSEC-2026)
  human_checkpoints:
  - Human experts take complex, high-risk architectural decisions (Stripe)
  role_evolution: Stripe says its framework moves security teams from managing a queue to higher-order safety challenges (UNPROMPTED-2026).
  evidence_grade: B
  sources:
  - ref: UNPROMPTED-2026
    title: '[un]prompted 2026 agenda (conference 2026-10-27 to 2026-10-29, San Francisco; abstracts of upcoming talks)'
    publisher: '[un]prompted (AI security practitioner conference)'
    type: conference
    url: https://unpromptedcon.org/agenda-10-2026/
    date: '2026-10-06'
    access: full
    locator: 'Session: There Isn''t a Security Problem an Agent Can''t Help Solve (Amol Deshpande, Stripe)'
  - ref: ANTHROPIC-JOB-APPSEC-2026
    title: 'Job posting: Staff+ Application Security Engineer (first published 2025-01-22, updated 2026-08-21)'
    publisher: Anthropic (Greenhouse)
    type: job-posting
    url: https://job-boards.greenhouse.io/anthropic/jobs/4502508008
    date: '2026-08-21'
    access: full
    locator: Representative projects
  - ref: MONGODB-JOB-PSE-2026
    title: 'Job posting: Senior Product Security Engineer, Assessments'
    publisher: MongoDB (Greenhouse)
    type: job-posting
    url: https://www.mongodb.com/careers/job/?gh_jid=8268264
    date: '2026-10-12'
    access: full
    locator: 'Responsibilities: AI-based analysis for threat modelling and pentest workflows'
  - ref: GTIG-AVDH-2026
    title: Staying Ahead of Adversarial AI Through Agentic Source Code Review
    publisher: Google Cloud Blog (Google Threat Intelligence Group / Mandiant)
    type: firm
    url: https://cloud.google.com/blog/topics/threat-intelligence/staying-ahead-of-adversarial-ai-through-agentic-source-code-review
    date: '2026-08-18'
    access: full
    locator: Consultant approves the generated threat model before analysis continues
  last_reviewed: '2026-10-17'
  notes: Stripe's claim is from a conference abstract for an event on 2026-10-27 to 2026-10-29 that has not yet taken place. Job-posting items describe intended projects.
- id: security-application-security-19
  title: First-line triage of bug-bounty and inbound vulnerability reports by AI
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - transaction-processing
  - review-assurance
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Programs and maintainers receive rising volumes of reports, many low quality or AI-generated, and each needs reproduction before it can be fixed.
  solution: Anthropic's application security team says Claude performs first-line bug-bounty triage and drafting while engineers handle escalations and corner cases. Coinbase's application security posting asks for AI-driven automation of vulnerability triage, validation and remediation workflows for the bug bounty and response pipeline, with human oversight. Anthropic, citing feedback from the Firefox team, urges researchers who use LLM tools to include evidence of verification and reproducibility with each report.
  outcomes:
  - lever: capacity
    description: AI triage effect
    figure: none published
    measures: the postings state intended or current practice without measured results
    provenance: self-reported
    source_ref: ANTHROPIC-JOB-APPSEC-2026
  prerequisites:
  - A public programme with defined scope and severity
  - Engineers on an escalation rota
  - Reproduction environments for reports
  risks_and_guardrails:
  - The Linux Foundation says maintainers face higher velocity of security reports, many AI-generated (LF-GLASSWING-2026)
  - OpenAI says maintainers want fewer low-quality reports and false positives, not more (OPENAI-CODEXSEC-2026)
  - Anthropic's own scanner offers a fast track that skips human review only to opted-in projects that can keep up (ANTHROPIC-OSSSCAN-2026)
  human_checkpoints:
  - Engineers handle escalations and corner cases (Anthropic)
  - Humans oversee generative AI output (Coinbase)
  role_evolution: Anthropic's posting says automation handles routine triage and root-cause work while engineers handle escalations (ANTHROPIC-JOB-APPSEC-2026).
  evidence_grade: B
  sources:
  - ref: ANTHROPIC-JOB-APPSEC-2026
    title: 'Job posting: Staff+ Application Security Engineer (first published 2025-01-22, updated 2026-08-21)'
    publisher: Anthropic (Greenhouse)
    type: job-posting
    url: https://job-boards.greenhouse.io/anthropic/jobs/4502508008
    date: '2026-08-21'
    access: full
    locator: About the role; Key responsibilities
  - ref: COINBASE-JOB-PSE-2026
    title: 'Job posting: Product Security Engineer (Offensive Security, Application Security team)'
    publisher: Coinbase (Greenhouse)
    type: job-posting
    url: https://www.coinbase.com/careers/positions/8165389?gh_jid=8165389
    date: '2026-08-28'
    access: full
    locator: 'Responsibilities: AI-driven automation for vulnerability triage, validation and remediation'
  - ref: ANTHROPIC-FIREFOX-2026
    title: Partnering with Mozilla on Firefox security
    publisher: Anthropic Frontier Red Team (red.anthropic.com)
    type: vendor
    url: https://red.anthropic.com/2026/firefox/
    date: '2026-03-06'
    access: full
    locator: What the Firefox team said built trust
  - ref: LF-GLASSWING-2026
    title: 'Introducing Project Glasswing: Giving Maintainers Advanced AI to Secure the World''s Code'
    publisher: Linux Foundation
    type: community
    url: https://www.linuxfoundation.org/blog/project-glasswing-gives-maintainers-advanced-ai-to-secure-open-source
    date: '2026-04-07'
    access: full
    locator: Maintainer burden from AI-generated reports
  - ref: GITHUB-ADVDB-2026
    title: Inside the Advisory Database and what happens when vulnerability volume breaks records
    publisher: GitHub Blog
    type: vendor
    url: https://github.blog/security/supply-chain-security/inside-the-advisory-database-and-what-happens-when-vulnerability-volume-breaks-records/
    date: '2026-06-29'
    access: full
    locator: Private vulnerability reports from about 550 a week in January to over 3,000 a week in May
  last_reviewed: '2026-10-17'
  notes: Anthropic's posting describes current practice at one named company (hence B), but no figures. Other postings show intent. A FIRST 2026 session on agentic 'PSIRT 2.0' is title-only (see use case 25).
- id: security-application-security-20
  title: Agents build bespoke analysis tooling and formal models before a manual security audit
  archetype: security
  module: application-security
  function: service-delivery
  work_types:
  - review-assurance
  - software-systems
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: A new virtual machine with a custom assembly language and almost no developer tooling is hard to review manually.
  solution: Trail of Bits used six months before the audit to have agents build an LSP server and VS Code extension, a decompiler, a static analysis engine and a Lean model of the Miden VM executor, then used those tools in the review alongside agent-driven code review. The pattern is 'agents build the review workbench', not only 'agents review code'.
  outcomes:
  - lever: quality
    description: Machine-checked proofs and findings from the prepared tooling
    figure: 95 machine-checked correctness proofs; one named vulnerability (unvalidated prover-supplied input enabling Falcon signature forgery)
    measures: proofs covering a large component of the Miden core library, produced from the agent-built Lean model; the firm says the tooling found real issues, giving this one as an example
    provenance: self-reported
    source_ref: TOB-MIDEN-2026
  prerequisites:
  - Months of lead time before the audit
  - Engineers who can specify and verify the tools agents build
  - Client scope that allows the work
  risks_and_guardrails:
  - The post is the firm's own account of its method; no independent verification of the proofs or findings was read
  human_checkpoints:
  - Auditors use and check the tools during the manual review
  role_evolution: 'The firm says its security expertise compounds as code: every engagement''s skills and workflows make the next one faster (TOB-AINATIVE-2026).'
  evidence_grade: A
  sources:
  - ref: TOB-MIDEN-2026
    title: Auditing in the age of (good enough) AI
    publisher: Trail of Bits Blog
    type: firm
    url: https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/
    date: '2026-09-18'
    access: full
    locator: Introduction and tooling sections
  - ref: TOB-AINATIVE-2026
    title: How we made Trail of Bits AI-native (so far)
    publisher: Trail of Bits Blog
    type: firm
    url: https://blog.trailofbits.com/2026/03/31/how-we-made-trail-of-bits-ai-native-so-far/
    date: '2026-03-31'
    access: full
    locator: AI-native definition
  last_reviewed: '2026-10-17'
  notes: 'The client is named in the post (Miden). Pattern set to ''other'': agent-built bespoke review tooling, not a standard pattern.'
- id: security-application-security-21
  title: Independent verification of AI-written security patches before human review
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - review-assurance
  - software-systems
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: A patch can stop a proof-of-concept crash without fixing the root cause, and both agents and developers submit incomplete fixes.
  solution: Trail of Bits released two agent skills. Post-patch-validation has the agent write a check that fails on the vulnerable code and passes on the patched version, test at least one other path to the same failure, check for regressions and new vulnerabilities with project tests, a sanitizer or a bounded fuzzing run, and treat broken builds as inconclusive. Review-walkthrough turns a branch diff into an ordered walkthrough with findings beside the code. Anthropic describes 'task verifiers' that check the vulnerability is gone and functionality is preserved, and Snyk has deterministic engines check proposed fixes.
  outcomes:
  - lever: quality
    description: Developer first fixes that failed to fully resolve the issue (human baseline)
    figure: 283 of 2,265 (12.5%; 95% interval 10.5% to 14.5%)
    measures: first fixes proposed for vulnerabilities in 236 Trail of Bits security assessments, 2024 to 2026, where the firm reviewed the fix; the firm says informal corrections may be missing, so failures may be undercounted
    provenance: self-reported
    source_ref: TOB-1PASSWORD-2026
  - lever: quality
    description: Agent patches that blocked the supplied exploit in the firm's reanalysis of another study
    figure: 2,634 of 3,067 (86%)
    measures: patches in 1Password's published data from trials where agents could run code and were not told to apply the wrong fix, excluding runs that consulted the upstream fix; the firm notes this does not establish a complete repair
    provenance: self-reported
    source_ref: TOB-1PASSWORD-2026
  - lever: quality
    description: Inflation from checking only the proof-of-concept
    figure: 1.83 times on average
    measures: increase in agents' patching solve rate when validated only by whether the proof-of-concept still triggers a crash, across 11 agents including the top three AIxCC agents; 25% of agent patches on average were substantially similar to historical developer patches
    provenance: independent
    source_ref: ARXIV-2609.04075
  prerequisites:
  - A vulnerability report and the vulnerable and patched revisions
  - Project tests, sanitizer builds or bounded fuzzing
  - Reviewers able to read an ordered walkthrough of the diff
  risks_and_guardrails:
  - Trail of Bits says the skills were not used in its Patch the Planet work (TOB-1PASSWORD-2026)
  - The 1Password report (2026-08-06) reports a 26% clean-fix headline that Trail of Bits disputes; the 1Password report itself was not read
  - Anthropic says it cannot guarantee that patches passing its verifiers are good enough to merge and recommends the same scrutiny as for any outside patch (ANTHROPIC-FIREFOX-2026)
  human_checkpoints:
  - Engineers review the walkthrough and decide to merge (TOB-1PASSWORD-2026)
  - Maintainers review AI-authored patches as for any external author (ANTHROPIC-FIREFOX-2026)
  role_evolution: The post releases review-walkthrough to help engineers review patches they are responsible for merging; it does not describe role changes (TOB-1PASSWORD-2026).
  evidence_grade: B
  sources:
  - ref: TOB-1PASSWORD-2026
    title: 1Password's AI patching benchmark is misleading
    publisher: Trail of Bits Blog
    type: firm
    url: https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/
    date: '2026-09-15'
    access: full
    locator: Sections on fix review data, reanalysis and the released skills
  - ref: ARXIV-2609.04075
    title: 'PatchBench: Evaluating AI Agents for Vulnerability Patching'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.04075
    date: '2026-09-03'
    access: full
    locator: Abstract
  - ref: ANTHROPIC-FIREFOX-2026
    title: Partnering with Mozilla on Firefox security
    publisher: Anthropic Frontier Red Team (red.anthropic.com)
    type: vendor
    url: https://red.anthropic.com/2026/firefox/
    date: '2026-03-06'
    access: full
    locator: Task verifiers
  - ref: SNYK-VULNBUMP-2026
    title: 'VulnBump: Can AI Agents Safely Fix Dependencies?'
    publisher: Snyk Blog
    type: vendor
    url: https://snyk.io/blog/vulnbump/
    date: '2026-10-15'
    access: full
    locator: Independent verifier in a clean container
  last_reviewed: '2026-10-17'
  notes: PatchBench was read at abstract level only. The 86% reanalysis is the firm's, in a published dispute.
- id: security-application-security-22
  title: Security team builds its own AI skills, agents and rules library with a maturity ladder and usage handbook
  archetype: security
  module: application-security
  function: service-delivery
  work_types:
  - expert-judgment
  - software-systems
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Handing people chat licences did not change how security work flows, and security experts resist tools that seem to replace their judgement.
  solution: 'Trail of Bits standardised on one coding agent, wrote an AI handbook listing approved and unapproved tools and rules for sensitive data, built a curated marketplace of plugins and skills with sandboxing, and used a maturity matrix and hackathons so expertise is encoded as reusable skills. Other teams show similar models: Anthropic''s application security engineers each own a Claude-powered security system end to end, GitLab expects all team members to use AI in daily work, and Cloudflare, Coinbase and Samsara postings ask security engineers to build AI-driven triage and detection tooling.'
  outcomes:
  - lever: capacity
    description: Library size and adoption
    figure: 94 plugins, 201 skills and 84 agents; about 5% of the firm on board a year earlier
    measures: firm's own counts at 2026-03-31; the 5% is the author's statement of the starting point a year earlier
    provenance: self-reported
    source_ref: TOB-AINATIVE-2026
  - lever: quality
    description: Bugs found per week on selected engagements
    figure: 200 a week
    measures: the firm's claim for AI-augmented auditors 'on the right engagements'; no definition of bug or engagement basis
    provenance: self-reported
    source_ref: TOB-AINATIVE-2026
  prerequisites:
  - Executive sponsor who uses the tools first
  - Standard toolchain and one-command setup
  - Handbook with approved tools and data rules
  - Sandboxing and a curated marketplace
  risks_and_guardrails:
  - The firm names four adoption barriers (self-enhancing bias, identity threat, intolerance for imperfection, opacity) and designs each programme element against one (TOB-AINATIVE-2026)
  - The handbook bars at least one coding tool from client code except on blockchain engagements (TOB-AINATIVE-2026)
  human_checkpoints:
  - Not specified beyond the handbook's approval rules
  role_evolution: Senior auditors write skills that encode their expertise; the firm says level 3 on its matrix is inventing new ways and building tools, and Anthropic's posting says the human work is the judgement layer (TOB-AINATIVE-2026; ANTHROPIC-JOB-APPSEC-2026).
  evidence_grade: B
  sources:
  - ref: TOB-AINATIVE-2026
    title: How we made Trail of Bits AI-native (so far)
    publisher: Trail of Bits Blog
    type: firm
    url: https://blog.trailofbits.com/2026/03/31/how-we-made-trail-of-bits-ai-native-so-far/
    date: '2026-03-31'
    access: full
    locator: Whole post
  - ref: ANTHROPIC-JOB-APPSEC-2026
    title: 'Job posting: Staff+ Application Security Engineer (first published 2025-01-22, updated 2026-08-21)'
    publisher: Anthropic (Greenhouse)
    type: job-posting
    url: https://job-boards.greenhouse.io/anthropic/jobs/4502508008
    date: '2026-08-21'
    access: full
    locator: About the role
  - ref: GITLAB-JOB-CODESEC-2026
    title: 'Job posting: Senior Software Engineer, Security Factory: Code Security'
    publisher: GitLab (Greenhouse)
    type: job-posting
    url: https://job-boards.greenhouse.io/gitlab/jobs/8738179002
    date: '2026-10-09'
    access: full
    locator: Team expectation to use AI in daily workflows; evaluation of AI detection
  - ref: CLOUDFLARE-JOB-PSE-2026
    title: 'Job posting: Product Security Engineer'
    publisher: Cloudflare (Greenhouse)
    type: job-posting
    url: https://boards.greenhouse.io/cloudflare/jobs/8102768?gh_jid=8102768
    date: '2026-08-04'
    access: full
    locator: 'Responsibilities: AI-driven tools to automate code analysis and triage'
  - ref: COINBASE-JOB-PSE-2026
    title: 'Job posting: Product Security Engineer (Offensive Security, Application Security team)'
    publisher: Coinbase (Greenhouse)
    type: job-posting
    url: https://www.coinbase.com/careers/positions/8165389?gh_jid=8165389
    date: '2026-08-28'
    access: full
    locator: 'Responsibilities: mentor junior engineers on integrating AI into offensive security workflows'
  - ref: SAMSARA-JOB-APPSEC-2026
    title: 'Job posting: Staff Application Security Engineer'
    publisher: Samsara (Greenhouse)
    type: job-posting
    url: https://www.samsara.com/company/careers/roles/8205149?gh_jid=8205149
    date: '2026-09-15'
    access: full
    locator: 'Qualification: hands-on AI use in triage, detection logic and remediation drafting'
  last_reviewed: '2026-10-17'
  notes: 'Pattern is ''other'': an operating-model change, not a workflow pattern. The 200-bugs claim has no stated definition and is not independently measured.'
- id: security-application-security-23
  title: Measuring AI security tools on labelled, contamination-reduced benchmarks before trusting them
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - review-assurance
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Public benchmarks built from known CVEs can be memorised by models, proof-of-concept-only checks inflate results, and one LLM scan run can miss a bug the next run finds.
  solution: Teams build their own evaluation harnesses. GitLab's code security team posts for engineers who build harnesses measuring false positives and missed findings against benchmark applications with known vulnerabilities. AWS built a continuously refreshed benchmark of recent CVEs, disabled runtime CVE lookup and audited every success. Semgrep measured how closely a model's 'secure' solutions matched the project's real code. AISLE reports repeated-run variability in an upcoming talk.
  outcomes:
  - lever: quality
    description: Benchmark inflation from memorisation (Claude Opus 5.5 on SusVibes)
    figure: 93 of 176 judged solutions (53%) near-identical to the real code; 57 of 102 secure solutions (56%) memorised
    measures: solutions with code similarity of 0.80 or more to the project's real implementation (comparing added lines in non-test files); Semgrep says similarity is not proof of recall
    provenance: vendor-published
    source_ref: SEMGREP-SUSVIBES-2026
  - lever: quality
    description: Headline score on the same benchmark
    figure: 54.8% correct and secure of 186 tasks, against a previous best of 43.5%
    measures: tasks where a solution passed the project's functional tests and the CVE-fix security tests, run by Semgrep under the leaderboard protocol on 2026-09-26
    provenance: vendor-published
    source_ref: SEMGREP-SUSVIBES-2026
  - lever: quality
    description: Inflation of patching results from proof-of-concept-only validation
    figure: 1.83 times on average
    measures: see use case 21
    provenance: independent
    source_ref: ARXIV-2609.04075
  prerequisites:
  - Labelled vulnerable applications or recent CVEs the model has not seen
  - Per-vulnerability reporting and repeated trials
  - Agreement checks between automated graders and expert review
  risks_and_guardrails:
  - AWS reports its own benchmark as contamination-reduced, not contamination-free (AWS-SECAGENT-2026)
  - Trail of Bits found 8% of ActiveMQ verdicts in a rival study penalised an intended behaviour change and automated graders agreed with human reviewers on the full outcome in 65.9% of reviewed cases, quoting that study's tables (TOB-1PASSWORD-2026)
  - A failed run caused by a broken build can be mistaken for evidence (TOB-1PASSWORD-2026)
  human_checkpoints:
  - Expert review of graders' verdicts
  role_evolution: GitLab asks security engineers for experience evaluating AI-driven detection against labelled data, measuring false positives and missed findings (GITLAB-JOB-CODESEC-2026).
  evidence_grade: B
  sources:
  - ref: GITLAB-JOB-CODESEC-2026
    title: 'Job posting: Senior Software Engineer, Security Factory: Code Security'
    publisher: GitLab (Greenhouse)
    type: job-posting
    url: https://job-boards.greenhouse.io/gitlab/jobs/8738179002
    date: '2026-10-09'
    access: full
    locator: Responsibilities and qualifications
  - ref: AWS-SECAGENT-2026
    title: AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs
    publisher: AWS Security Blog
    type: vendor
    url: https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/
    date: '2026-10-15'
    access: full
    locator: Benchmark design; contamination
  - ref: SEMGREP-SUSVIBES-2026
    title: 'Is AI-Generated Code Secure? Testing Claude Opus 5.5 (listing title: Claude Opus 5.5 Writes Working Code but Only Half of It Is Secure)'
    publisher: Semgrep Blog
    type: vendor
    url: https://semgrep.dev/blog/2026/claude-opus-5-5-susvibes-benchmark
    date: '2026-09-29'
    access: full
    locator: TL;DR and memorisation analysis
  - ref: ARXIV-2609.04075
    title: 'PatchBench: Evaluating AI Agents for Vulnerability Patching'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.04075
    date: '2026-09-03'
    access: full
    locator: Abstract
  - ref: TOB-1PASSWORD-2026
    title: 1Password's AI patching benchmark is misleading
    publisher: Trail of Bits Blog
    type: firm
    url: https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/
    date: '2026-09-15'
    access: full
    locator: Benchmark design principles and grading critique
  - ref: UNPROMPTED-2026
    title: '[un]prompted 2026 agenda (conference 2026-10-27 to 2026-10-29, San Francisco; abstracts of upcoming talks)'
    publisher: '[un]prompted (AI security practitioner conference)'
    type: conference
    url: https://unpromptedcon.org/agenda-10-2026/
    date: '2026-10-06'
    access: full
    locator: 'Session: The Scanner Said Clean. We Ran It Again (Petr Simecek, AISLE)'
  last_reviewed: '2026-10-17'
  notes: Pattern is 'other'. The SusVibes run is by a scanner vendor. The ActiveMQ and grader-agreement numbers are the firm's reading of another organisation's report, which was not read.
- id: security-application-security-24
  title: Agent-applied compiler bounds-safety annotations and rewrites to remove vulnerability classes
  archetype: security
  module: application-security
  function: technology-it
  work_types:
  - software-systems
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: Patching one bug at a time does not remove whole classes of memory-safety vulnerability, such as the libwebp heap overflow used in a zero-click iOS exploit.
  solution: Google DeepMind's CodeMender agent applied -fbounds-safety annotations to parts of the libwebp image library so the compiler adds bounds checks, fixed its own compile errors and test failures, and used an LLM judge configured for functional equivalence. It only surfaces patches for human review after validation by static and dynamic analysis, differential testing, fuzzing and SMT solvers. Anthropic lists rebuilding legacy code bases in memory-safe languages among defensive tasks such models can do.
  outcomes:
  - lever: capacity
    description: Fixes upstreamed during the research
    figure: 72 security fixes
    measures: fixes upstreamed to open-source projects (some up to 4.5 million lines of code) over the six months of building CodeMender; not limited to hardening annotations
    provenance: self-reported
    source_ref: DEEPMIND-CODEMENDER-2025
  prerequisites:
  - Compiler support for the annotations
  - Strong test suites and program-analysis tooling to validate each change
  - Maintainer willingness to take the changes
  risks_and_guardrails:
  - DeepMind says mistakes in code security could be costly and that only validated, high-quality patches reach human review (DEEPMIND-CODEMENDER-2025)
  - Results are described as early research
  human_checkpoints:
  - Humans review surfaced patches
  role_evolution: DeepMind says the agent frees developers and maintainers to focus on building good software (DEEPMIND-CODEMENDER-2025).
  evidence_grade: B
  sources:
  - ref: DEEPMIND-CODEMENDER-2025
    title: 'Introducing CodeMender: an AI agent for code security'
    publisher: Google DeepMind
    type: vendor
    url: https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/
    date: '2025-10-06'
    access: full
    locator: Whole post; libwebp section
  - ref: ANTHROPIC-EXPAND-2026
    title: Expanding Project Glasswing
    publisher: Anthropic
    type: vendor
    url: https://www.anthropic.com/news/expanding-project-glasswing
    date: '2026-06-02'
    access: full
    locator: Defensive tasks Mythos Preview can support
  last_reviewed: '2026-10-17'
  notes: The 72-fix count is not a measure of the hardening work itself, for which no figures were published. The post was last modified 2026-07-13.
- id: security-application-security-25
  title: Agentic AI operations for product security incident response teams (PSIRT)
  archetype: security
  module: application-security
  function: service-delivery
  work_types:
  - transaction-processing
  - coordination-scheduling
  pattern: end-to-end-case-agent
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Product security teams must triage inbound reports and, in the EU, meet new vulnerability reporting duties.
  solution: 'The programme of the 38th FIRST Conference lists a session, ''PSIRT 2.0 in Action: Implementing Agentic AI Architecture for Autonomous Operations'', by staff of GMO Cybersecurity by IERAE and Ken Associates LLC, scheduled for 2026-06-18. The session was marked TLP:AMBER, so the architecture and results were not visible.'
  outcomes:
  - lever: capacity
    description: Session results
    figure: none published
    measures: only the title, authors, date and traffic-light marking were readable
    provenance: self-reported
    source_ref: FIRST-CON-2026
  prerequisites:
  - Not visible
  risks_and_guardrails:
  - Not visible. EU Cyber Resilience Act reporting obligations apply from 2026-09-11 and main obligations from 2027-12-11 (EC-CRA-2026)
  human_checkpoints:
  - Not visible
  role_evolution: Not visible.
  evidence_grade: C
  sources:
  - ref: FIRST-CON-2026
    title: 38th FIRST Conference program (Denver, 2026-06-14 to 2026-06-19)
    publisher: FIRST
    type: conference
    url: https://www.first.org/conference/2026/program
    date: '2026-06-18'
    access: full
    locator: 'Session listing, 2026-06-18 13:30-14:15; Dell session ''The Clock is Ticking: CRA Compliance at Scale'' on the same programme'
  - ref: EC-CRA-2026
    title: Cyber Resilience Act (policy page; undated, date is retrieval date; text cites guidance of 2026-07-27)
    publisher: European Commission
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
    date: '2026-10-17'
    access: full
    locator: Application dates
  last_reviewed: '2026-10-17'
  notes: Title-only evidence from a conference programme; the ladder value is set to the neutral 'augment' because the autonomy level is unknown. Graded C as a consultancy presentation claim.
```

## 3. Module notes

### 3.1 Processes and key steps (with work types)

| Process | Key steps | Work types | Use cases |
|---|---|---|---|
| Secure design and threat modelling | Intake, threat model, design review, risk tracking | expert-judgment, document-production | 18 |
| Secure coding and agent guardrails | IDE and agent hooks, rules files, package firewalls | software-systems, review-assurance | 14 |
| Code review | Human and automated review, risk tiering | review-assurance | 02, 13 |
| Scanning in CI (SAST, SCA, secrets, DAST) | Pre-submit scan, validation, reachability proof | review-assurance | 01, 11, 10 |
| Fuzzing, audit and pentest | Harness building, coverage, crash triage, targeted audit | review-assurance, software-systems | 05, 08, 09, 20 |
| Finding triage and prioritisation | De-duplication, reachability ranking, closure states | transaction-processing, data-reporting | 12 |
| Remediation | Fix authoring, dependency upgrades, hardening, fix verification | software-systems | 03, 04, 15, 21, 24 |
| Software supply chain | Dependency intake, malware detection, advisory curation | review-assurance, research-synthesis | 16, 17 |
| Vulnerability intake and disclosure | Bug bounty, PSIRT, coordinated disclosure, OSS reports | transaction-processing, client-interaction | 06, 07, 19, 25 |
| Programme reporting | Time to remediate, vulnerabilities found and closed | data-reporting | 12 (Semgrep names these as AppSec reporting items: SEMGREP-APPSEC-2026) |

One vendor describes AppSec as a very broad remit held together by relationships with developers, processes that fit into existing work, and tools, "in that order of importance" (SEMGREP-APPSEC-2026).

### 3.2 Common pain points

- **Code volume outruns review.** At Meta, significant lines of code per human-landed diff grew 105.9% year over year and agentic AI was responsible for over 80% of that growth (ARXIV-2605.30208). At another AI-forward company, per-reviewer load roughly doubled while automated review overtook human review and merge and revert rates held steady (ARXIV-2607.01904, abstract).
- **Backlog and noise.** Snyk says its data as of October 2026 showed roughly eight new vulnerabilities introduced for every one remediated, and that 94% of 459 million findings had a known fixed version but only about 10% had been resolved (SNYK-AGENTIC-2026; SNYK-VULNBUMP-2026; vendor figures). Static-analysis false positives require costly manual triage (ARXIV-2601.02941).
- **Fix quality.** In Trail of Bits' records, 12.5% of developers' first fixes did not fully resolve the reported issue (TOB-1PASSWORD-2026).
- **Maintainer overload.** Open-source maintainers face more pull requests and security reports, many AI-generated (LF-GLASSWING-2026). GitHub private vulnerability reports rose from about 550 a week in January to over 3,000 a week for most of May 2026 (GITHUB-ADVDB-2026). curl's security team is six volunteers (CURL-TEAM-2026).
- **Supply chain.** Malicious packages can run at install, before a pull-request scan (SNYK-AGENTIC-2026); AI tools can suggest non-existent or unsafe dependencies (GITHUB-APPCARD-2026; ARXIV-2608.23897).

### 3.3 Metrics and benchmarks (with provenance)

| Metric | Value | Measures | Provenance | Ref |
|---|---|---|---|---|
| Scanner false-positive rate, localized threat models | 3% in some cases | false positives of Google's security agents | self-reported | GOOGLE-AGENTICSCAN-2026 |
| Triage agent precision | over 92% | reachability proofs, under a minute | self-reported | GOOGLE-AGENTICSCAN-2026 |
| Revert rate, RADAR vs non-RADAR | one third | Meta diffs auto-reviewed vs others | self-reported | ARXIV-2605.30208 |
| Disclosure funnel | 6,157 disclosed; 516 patched | findings 2025-11-01 to 2026-10-02 | vendor-published | ANTHROPIC-CVD-2026 |
| True-positive rate of triaged model findings | 92.7% | external firm confirmations of reviewed findings | vendor-published | ANTHROPIC-CVD-2026 |
| Exploit capture on recent CVEs | 33 of 37 (89.2%) | AWS agent, intended-path captures after audit | vendor-published | AWS-SECAGENT-2026 |
| AIxCC final: synthetic vulnerabilities | 54 of 63 found; 43 patched (68% of 63); 18 real non-synthetic vulnerabilities found; 11 patches for real ones | competition systems at DEF CON 33 | independent (organiser) | DARPA-AIXCC-2025 |
| Secure-and-functional fix rate | 74.6% to 85.4% (Opus 4.6 alone vs with Snyk context) | about 150 samples, hidden tests | vendor-published | SNYK-AGENTFIX-2026 |
| Dependency upgrade pass rate | 90.2% / 77.5% / 59.6% / 46.9% | 307 tasks (agent / Claude Code with scan / unaided / no AI) | vendor-published | SNYK-VULNBUMP-2026 |
| LLM code with at least one vulnerability | 55.8% of 3,500 artifacts | 7 LLMs, 500 security-critical prompts, formal verification | independent (academic) | ARXIV-2604.05292 |
| Same study: industry tools | six tools combined miss 97.8% of formally proven findings | Z3-proven vulnerabilities | independent (academic) | ARXIV-2604.05292 |
| Risky flaws in AI-generated code | 45% of tests | over 100 LLMs, 4 languages | vendor-published | VERACODE-GENAI-2025 |
| Correct and secure, Opus 5.5 | 54.8% of 186 tasks; 53% of solutions near-identical to real code | SusVibes run by Semgrep | vendor-published | SEMGREP-SUSVIBES-2026 |
| Agentic secure code review | 54% of comments validated in shadow mode | Atlassian setting | self-reported | ARXIV-2601.19138 |
| Human detection of seeded flaws | 3% to 61% | two specific flaws, 2022 experiment (via Semgrep) | independent (academic, second-hand) | ARXIV-2202.04586; SEMGREP-ENDCR-2026 |
| Patch benchmark inflation | 1.83 times | PoC-only vs fuller validation, 11 agents | independent (academic) | ARXIV-2609.04075 |

**Quality evidence: what exists and what is missing.** No source published override or acceptance rates for AI security-review comments at scale, and none published a parallel run of AI against human AppSec review in production. The independent measurements are about insecure AI-generated code, benchmark validity and reviewer load, not about the AI appsec tools. curl's maintainer is an independent confirmation of Aisle's CVE count but not of its false-positive rate (CURL-AISLE-2026).

### 3.4 Guardrails and regulatory points

- **EU Cyber Resilience Act.** In force since 2024-12-10; reporting obligations apply from 2026-09-11 and main obligations from 2027-12-11; the Commission published guidance on 2026-07-27 (EC-CRA-2026).
- **NIST.** SSDF version 1.2 was published as an initial public draft on 2025-12-17 (NIST-SSDF-218R1-2025); SP 800-218A adds AI-model practices to the SSDF (NIST-SP800218A-2024).
- **OpenSSF.** Guide for security instructions given to AI code assistants, dated 2025-08-01: the developer remains responsible and normal review, testing and static analysis still apply (OPENSSF-AIGUIDE-2025).
- **Product documentation.** GitHub requires review of Autofix suggestions and warns about semantic errors, partial fixes and fabricated dependencies (GITHUB-APPCARD-2026). Anthropic and OpenAI say patches need human approval (ANTHROPIC-CCS-2026; OPENAI-CODEXSEC-2026).
- **Disclosure norms.** Anthropic follows coordinated vulnerability disclosure with external triage, and, citing Mozilla's feedback, urges AI-assisted researchers to include evidence of verification and reproducibility in reports (ANTHROPIC-CVD-2026; ANTHROPIC-FIREFOX-2026).
- **Agent execution safety.** GitHub warns its fuzzing taskflow runs LLM-chosen commands on the host and should only be run in a disposable environment (GITHUB-TASKFLOW-2026). AWS's two misses took targets down; its guardrails are non-destructive (AWS-SECAGENT-2026).
- **Access gating of frontier cyber models.** Anthropic's Cyber Verification Program has three access tiers for qualifying security professionals (ANTHROPIC-GLASSWING-2026, update of 2026-10-06).
- **Compliance without per-change human review.** A Semgrep blog (opinion, second-hand) reports that Amp's engineers push straight to main, and quotes Amp as saying SOC 2 does not require pull requests; Semgrep argues for risk-tiered review (SEMGREP-ENDCR-2026). This is a vendor's argument, not an auditor's statement.

### 3.5 Frontier signals (dated)

- 2026-02-20: Anthropic previews Claude Code Security, scanning and suggesting patches for human review (ANTHROPIC-CCS-2026).
- 2026-03-06: OpenAI renames Aardvark to Codex Security and opens a research preview (OPENAI-CODEXSEC-2026).
- 2026-04-07: Project Glasswing launches with a gated frontier model for defenders (ANTHROPIC-GLASSWING-2026).
- 2026-06-02: Anthropic expands Glasswing to about 150 more organisations, says the bottleneck is verifying, disclosing and patching, and expects other AI companies to have comparable models within 6 to 12 months (ANTHROPIC-EXPAND-2026; a vendor prediction).
- 2026-06-23 to 2026-07-28: Semgrep launches Guardian for agent-written code and nine Agentic Workflows (SEMGREP-GUARDIAN-2026; SEMGREP-AGENTICWF-2026).
- 2026-09-19: Google describes pre-submit agentic scanning of every change (GOOGLE-AGENTICSCAN-2026).
- 2026-09-30: Google Threat Intelligence Group advises moving from unprioritised mass patching to threat-intelligence-driven triage with automated agentic remediation (GTIG-VULNTRENDS-2026).
- 2026-10-06 to 2026-10-15: Wiz AI SAST preview, Anthropic OSS Scanner fast track without human review, Semgrep in Cursor Origin, Snyk Evo Agentic AppSec (WIZ-AISAST-2026; ANTHROPIC-CYBERMISSION-2026; SEMGREP-CURSOR-2026; SNYK-AGENTIC-2026).
- 2026-10-27 to 2026-10-29: [un]prompted sessions announced on closure of AI-found bugs, repeatability of LLM scans and agent-run security reviews (UNPROMPTED-2026).

### 3.6 Workforce and role effects

- **Builders and operators.** Anthropic's application security engineers each own a Claude-powered system end to end, and the posting says the human work is the judgement layer (ANTHROPIC-JOB-APPSEC-2026). GitLab expects all team members to use AI in daily work and wants engineers who can evaluate AI detection against labelled data (GITLAB-JOB-CODESEC-2026).
- **AI skills as a hiring criterion.** Postings ask for AI use or AI-driven tooling in triage, testing, detection or remediation work (Samsara, Cloudflare, Coinbase, Okta, MongoDB, Stripe: SAMSARA-JOB-APPSEC-2026; CLOUDFLARE-JOB-PSE-2026; COINBASE-JOB-PSE-2026; OKTA-JOB-PSE-2026; MONGODB-JOB-PSE-2026; STRIPE-JOB-VM-2026). Coinbase asks engineers to mentor juniors on integrating AI (COINBASE-JOB-PSE-2026).
- **New security work on AI systems.** Datadog's postings ask for application security on agentic applications, MCP and A2A, and product security for its coding agent (DATADOG-JOB-APPSEC-2026; DATADOG-JOB-PSE-AGENTS-2026). Routed to ai-security.
- **Reviewers carry more.** Reviewer load roughly doubled in one company's mandate, and a Semgrep summary of the same study says the share of pull requests with written human feedback fell from 39% to 21% (ARXIV-2607.01904 for the load; SEMGREP-ENDCR-2026 for the 39% to 21%, not verified in the paper).
- **Professional-body view.** ISC2 says professionals expect roles to emerge and evolve rather than be replaced, and prioritise AI skills development (ISC2-WORKFORCE-2025).
- **Resistance is a design problem.** Trail of Bits says about 5% of the firm was on board a year before 2026-03-31 and describes four psychological barriers it designed against (TOB-AINATIVE-2026).
- **No hard data on junior pipeline** was found (see gaps).

### 3.7 Objections and concerns practitioners raise

- **Benchmarks overstate ability.** Models may reproduce public CVE fixes from memory (SEMGREP-SUSVIBES-2026); PoC-only checks inflate patching results (ARXIV-2609.04075); AWS calls its own benchmark contamination-reduced, not free (AWS-SECAGENT-2026); Trail of Bits calls 1Password's 26% clean-fix headline misleading (TOB-1PASSWORD-2026).
- **Non-determinism.** An LLM scanner can miss a bug on one run and find it the next (UNPROMPTED-2026, AISLE abstract); GitHub says Autofix may not produce a viable suggestion on repeat (GITHUB-APPCARD-2026).
- **Fixes can regress.** Both an agent patch and the maintainer's fix introduced the same cleanup crash in freenginx (TOB-1PASSWORD-2026). Unaided Claude Code claimed fixes that a rescan still found in 70 of 124 failures (SNYK-VULNBUMP-2026).
- **Speed of fix.** AI-written fixes did not by themselves speed up fixing at Meta (UNPROMPTED-2026).
- **Noise for maintainers.** Maintainers say they need fewer low-quality reports, not more (OPENAI-CODEXSEC-2026; LF-GLASSWING-2026).
- **Vendor claims with unnamed customers.** Several vendor figures come from unnamed design partners or customers (SEMGREP-AGENTICWF-2026; SEMGREP-GUARDIAN-2026).
- **Agent safety.** Prompt-injected or runaway agents (GITHUB-TASKFLOW-2026; AWS-SECAGENT-2026).

### 3.8 Interview probes for an advisor

1. Where does AI-found or AI-generated vulnerability volume now queue in your process (triage, fix authoring, review, release), and how long from a confirmed finding to a merged fix? Do you track opened, reviewed and fixed separately?
2. Which scanners or fixers do you use that include AI, and how do you measure their false positives and missed findings, on what labelled set? What happens when two runs of the same scan disagree?
3. Which changes can your coding agents land without a human reviewer, who decided that, and what revert or incident data supports it?
4. Which AppSec tasks (triage, threat modelling, bounty reports, dependency upgrades) have you handed to agents, with what scoped authority, and which did you deliberately keep human?
5. How do you handle inbound reports from researchers and AI tools (evidence required, de-duplication, owner, deadline), and are you ready for reporting duties under the EU Cyber Resilience Act?

## 4. Routed to other modules

| Item | Target module | Source |
|---|---|---|
| NIST request for information on modernising the National Vulnerability Database, and its unreleased AI-enabled tool V-etalon (RFI dated 2026-08-12 per the article) | vulnerability-exposure | SOCKET-NVD-2026 |
| Recommendation to shift from mass patching to threat-intelligence-driven triage with agentic remediation; disclosure and exploitation trend data | vulnerability-exposure | GTIG-VULNTRENDS-2026 |
| CISA's use of AI in vulnerability management and the Gold Eagle intake platform for AI-discovered vulnerabilities (session abstract) | vulnerability-exposure | UNPROMPTED-2026 |
| Anthropic Critical Infrastructure Defense Program for operational technology providers (founding partners include Accenture, Booz Allen, CrowdStrike, Deloitte, Dragos, Hitachi, Nozomi Networks, Palo Alto Networks, PwC, Rockwell Automation) | vulnerability-exposure (OT) | ANTHROPIC-CYBERMISSION-2026 |
| Autonomous exposure-management and pentest products (XBOW, Wiz Red Agent): only blog listings were seen | vulnerability-exposure; cloud-infrastructure | not cited (listing only) |
| Wiz AI SAST correlating code findings with what runs in production | cloud-infrastructure | WIZ-AISAST-2026 |
| Application security for agentic applications, MCP and A2A; product security for a coding agent; AI red-teaming postings (Datadog, Coinbase, Cloudflare) | ai-security | DATADOG-JOB-APPSEC-2026; DATADOG-JOB-PSE-AGENTS-2026; COINBASE-JOB-PSE-2026; CLOUDFLARE-JOB-PSE-2026 |
| Agent sandboxes and containment: warning that a prompt-injected agent can do what its user can; sandbox sessions at [un]prompted | ai-security | GITHUB-TASKFLOW-2026; UNPROMPTED-2026 |
| Package-name hallucination and slopsquatting research | ai-security | ARXIV-2608.23897 |
| Metrics for production security agents (triage, threat intel, detection) session; Cloudflare 'agentic security operations harness' post (title seen in the blog feed only, 2026-10-07) | operations | UNPROMPTED-2026 |
| AI tool-use policy for client code; compliance without per-change human review; SSDF and CRA duties | governance-risk | TOB-AINATIVE-2026; SEMGREP-ENDCR-2026; NIST-SSDF-218R1-2025; EC-CRA-2026 |
| Use of the discovery harness during an incident response involving stolen repositories | incident-response | GTIG-AVDH-2026 |

## 5. Sources

All sources were opened and read (full text for web pages and postings; abstract pages only for arXiv items; agenda text for conference pages). Refs follow PUBLISHER-SHORT-YYYY; where the landscape file bundled several posts under one ref (TOB-BLOG-2026, SNYK-BLOG-2026, WIZ-BLOG-2026, GOOGLE-SECBLOG-2026), each post has its own ref here. Dates for undated pages are retrieval dates (2026-10-17) and are labelled in the title. Job-posting dates are first-published dates on the employer's board unless the title says updated.

Count by type: academic 12, community 3, conference 2, firm 8, job-posting 11, professional-body 1, regulator 2, standard-setter 3, vendor 32 (total 74).

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| `GOOGLE-AGENTICSCAN-2026` | Changing the game: Using agentic AI to secure infrastructure code (page title: Using AI agents to secure Google infrastructure) | Google Cloud Blog (Google AI Infrastructure team) | firm | https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/ | 2026-09-19 | full |
| `GTIG-AVDH-2026` | Staying Ahead of Adversarial AI Through Agentic Source Code Review | Google Cloud Blog (Google Threat Intelligence Group / Mandiant) | firm | https://cloud.google.com/blog/topics/threat-intelligence/staying-ahead-of-adversarial-ai-through-agentic-source-code-review | 2026-08-18 | full |
| `GTIG-VULNTRENDS-2026` | Vulnerability Discovery and Exploitation Trends in the AI Era | Google Cloud Blog (Google Threat Intelligence Group) | firm | https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/ | 2026-09-30 | full |
| `AWS-SECAGENT-2026` | AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs | AWS Security Blog | vendor | https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/ | 2026-10-15 | full |
| `GITHUB-TASKFLOW-2026` | AI-powered fuzzing with the GitHub Security Lab Taskflow Agent | GitHub Blog | vendor | https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/ | 2026-09-24 | full |
| `GITHUB-ANDROID-2026` | How we found 24 Android vulnerabilities using our open source AI security agent | GitHub Blog | vendor | https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/ | 2026-09-28 | full |
| `GITHUB-SECUREFUND-2026` | What 50 open source projects taught us about security in the AI era | GitHub Blog | vendor | https://github.blog/open-source/maintainers/what-50-open-source-projects-taught-us-about-security-in-the-ai-era/ | 2026-08-13 | full |
| `GITHUB-ADVDB-2026` | Inside the Advisory Database and what happens when vulnerability volume breaks records | GitHub Blog | vendor | https://github.blog/security/supply-chain-security/inside-the-advisory-database-and-what-happens-when-vulnerability-volume-breaks-records/ | 2026-06-29 | full |
| `GITHUB-APPCARD-2026` | Application card: GitHub security and quality AI features (page undated; date is retrieval date) | GitHub Docs | vendor | https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning | 2026-10-17 | full |
| `ANTHROPIC-GLASSWING-2026` | Project Glasswing: Securing critical software for the AI era | Anthropic | vendor | https://www.anthropic.com/glasswing | 2026-04-07 | full |
| `ANTHROPIC-EXPAND-2026` | Expanding Project Glasswing | Anthropic | vendor | https://www.anthropic.com/news/expanding-project-glasswing | 2026-06-02 | full |
| `ANTHROPIC-CCS-2026` | Making frontier cybersecurity capabilities available to defenders (Claude Code Security) | Anthropic | vendor | https://www.anthropic.com/news/claude-code-security | 2026-02-20 | full |
| `ANTHROPIC-FIREFOX-2026` | Partnering with Mozilla on Firefox security | Anthropic Frontier Red Team (red.anthropic.com) | vendor | https://red.anthropic.com/2026/firefox/ | 2026-03-06 | full |
| `ANTHROPIC-CVD-2026` | Anthropic's coordinated vulnerability disclosure dashboard (counts as of 2026-10-02) | Anthropic Frontier Red Team (red.anthropic.com) | vendor | https://red.anthropic.com/2026/cvd/ | 2026-10-02 | full |
| `ANTHROPIC-OSSSCAN-2026` | OSS Scanner | Anthropic Frontier Red Team (red.anthropic.com) | vendor | https://red.anthropic.com/oss-scanner | 2026-10 | full |
| `ANTHROPIC-CYBERMISSION-2026` | Introducing the Anthropic Cyber Mission | Anthropic | vendor | https://www.anthropic.com/news/anthropic-cyber-mission | 2026-10-08 | full |
| `ANTHROPIC-SECREVIEW-2025` | Automate security reviews with Claude Code | Anthropic | vendor | https://www.anthropic.com/news/automate-security-reviews-with-claude-code | 2025-08-06 | full |
| `OPENAI-AARDVARK-2025` | Introducing Aardvark: OpenAI's agentic security researcher (page updated 2026-03-06 to say Aardvark is now Codex Security) | OpenAI | vendor | https://openai.com/index/introducing-aardvark/ | 2025-10-30 | full |
| `OPENAI-CODEXSEC-2026` | Codex Security: now in research preview | OpenAI | vendor | https://openai.com/index/codex-security-now-in-research-preview/ | 2026-03-06 | full |
| `OPENAI-CODEXDOCS-2026` | Codex Security (product documentation; page undated, date is retrieval date) | OpenAI Developers | vendor | https://developers.openai.com/codex/security | 2026-10-17 | full |
| `DEEPMIND-CODEMENDER-2025` | Introducing CodeMender: an AI agent for code security | Google DeepMind | vendor | https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/ | 2025-10-06 | full |
| `LF-GLASSWING-2026` | Introducing Project Glasswing: Giving Maintainers Advanced AI to Secure the World's Code | Linux Foundation | community | https://www.linuxfoundation.org/blog/project-glasswing-gives-maintainers-advanced-ai-to-secure-open-source | 2026-04-07 | full |
| `TOB-1PASSWORD-2026` | 1Password's AI patching benchmark is misleading | Trail of Bits Blog | firm | https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/ | 2026-09-15 | full |
| `TOB-PTP-2026` | Introducing Patch the Planet | Trail of Bits Blog | firm | https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/ | 2026-06-22 | full |
| `TOB-ZLIB-2026` | GPT-5.5-Cyber built a zlib fuzzing lab in a day | Trail of Bits Blog | firm | https://blog.trailofbits.com/2026/07/02/field-reports-from-patch-the-planet/ | 2026-07-02 | full |
| `TOB-AINATIVE-2026` | How we made Trail of Bits AI-native (so far) | Trail of Bits Blog | firm | https://blog.trailofbits.com/2026/03/31/how-we-made-trail-of-bits-ai-native-so-far/ | 2026-03-31 | full |
| `TOB-MIDEN-2026` | Auditing in the age of (good enough) AI | Trail of Bits Blog | firm | https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/ | 2026-09-18 | full |
| `SNYK-AGENTIC-2026` | Introducing Evo Agentic AppSec: Security That Keeps Up With AI Development | Snyk Blog | vendor | https://snyk.io/blog/announcing-snyk-agentic-appsec/ | 2026-10-15 | full |
| `SNYK-VULNBUMP-2026` | VulnBump: Can AI Agents Safely Fix Dependencies? | Snyk Blog | vendor | https://snyk.io/blog/vulnbump/ | 2026-10-15 | full |
| `SNYK-AGENTFIX-2026` | Benchmarking Secure-and-Functional Remediation and How Snyk Agent Fix Lifts Frontier-Model Fix Rates by over 14% | Snyk Blog | vendor | https://snyk.io/blog/snyk-agent-fix-remediation-benchmark/ | 2026-08-18 | full |
| `SNYK-SNOWFLAKE-2026` | Snyk Studio for Snowflake Cortex Code | Snyk Blog | vendor | https://snyk.io/blog/announcing-snyk-studio-integration-snowflake-cortex-code/ | 2026-07-30 | full |
| `SEMGREP-GUARDIAN-2026` | Introducing Semgrep Guardian: Real-Time Security for AI-Written Code (date from the Semgrep blog listing) | Semgrep Blog | vendor | https://semgrep.dev/blog/2026/introducing-semgrep-guardian-real-time-security-for-ai-written-code | 2026-06-23 | full |
| `SEMGREP-AGENTICWF-2026` | Introducing Semgrep Agentic Workflows: Automate Deep Vulnerability Hunting at Scale (date from the Semgrep blog listing) | Semgrep Blog | vendor | https://semgrep.dev/blog/2026/introducing-semgrep-agentic-workflows-automate-deep-vulnerability-hunting-at-scale | 2026-07-28 | full |
| `SEMGREP-SUSVIBES-2026` | Is AI-Generated Code Secure? Testing Claude Opus 5.5 (listing title: Claude Opus 5.5 Writes Working Code but Only Half of It Is Secure) | Semgrep Blog | vendor | https://semgrep.dev/blog/2026/claude-opus-5-5-susvibes-benchmark | 2026-09-29 | full |
| `SEMGREP-APPSEC-2026` | What Application Security Actually Does All Day | Semgrep Blog | vendor | https://semgrep.dev/blog/2026/what-application-security-does | 2026-09-25 | full |
| `SEMGREP-ENDCR-2026` | AI Code Review and the End of Reviewing Every Change (listing title: The End Is Nigh for Code Review) | Semgrep Blog | vendor | https://semgrep.dev/blog/2026/end-is-nigh-for-code-review | 2026-10-09 | full |
| `SEMGREP-CURSOR-2026` | Cursor Origin Security Scanning: Semgrep Checks Every PR | Semgrep Blog | vendor | https://semgrep.dev/blog/2026/cursor-origin-security-scanning | 2026-10-14 | full |
| `SEMGREP-MALWARE-2026` | Introducing Malware Detection and Response Automation | Semgrep Blog | vendor | https://semgrep.dev/blog/2026/introducing-malware-detection-and-response-automation | 2026-09-24 | full |
| `WIZ-AISAST-2026` | Wiz AI SAST: AI Code Security With Code-to-Cloud Context | Wiz Blog | vendor | https://www.wiz.io/blog/introducing-wiz-ai-sast | 2026-10-06 | full |
| `VERACODE-GENAI-2025` | 2025 GenAI Code Security Report (landing page; Oct 2025 update; page last modified 2026-07-09) | Veracode | vendor | https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/ | 2025-07-25 | full |
| `CURL-AISLE-2026` | A curl audit by Aisle | daniel.haxx.se (Daniel Stenberg, curl lead maintainer) | community | https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/ | 2026-10-14 | full |
| `UNPROMPTED-2026` | [un]prompted 2026 agenda (conference 2026-10-27 to 2026-10-29, San Francisco; abstracts of upcoming talks) | [un]prompted (AI security practitioner conference) | conference | https://unpromptedcon.org/agenda-10-2026/ | 2026-10-06 | full |
| `FIRST-CON-2026` | 38th FIRST Conference program (Denver, 2026-06-14 to 2026-06-19) | FIRST | conference | https://www.first.org/conference/2026/program | 2026-06-18 | full |
| `ARXIV-2605.30208` | Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency | arXiv (Meta authors) | academic | https://arxiv.org/abs/2605.30208 | 2026-05-28 | full |
| `ARXIV-2604.05292` | Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code | arXiv | academic | https://arxiv.org/abs/2604.05292 | 2026-04-07 | full |
| `ARXIV-2512.18567` | AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code in Modern Software | arXiv | academic | https://arxiv.org/abs/2512.18567 | 2025-12-21 | full |
| `ARXIV-2609.04075` | PatchBench: Evaluating AI Agents for Vulnerability Patching | arXiv | academic | https://arxiv.org/abs/2609.04075 | 2026-09-03 | full |
| `ARXIV-2607.01904` | AI Writes Faster Than Humans Can Review: A Longitudinal Study of an Enterprise 2x Mandate | arXiv | academic | https://arxiv.org/abs/2607.01904 | 2026-07-02 | full |
| `ARXIV-2607.23088` | Poster: Rethinking Security in LLM Code Generation through Real-World Risk Scenarios | arXiv | academic | https://arxiv.org/abs/2607.23088 | 2026-07-25 | full |
| `ARXIV-2202.04586` | Less is More: Supporting Developers in Vulnerability Detection during Code Review | arXiv | academic | https://arxiv.org/abs/2202.04586 | 2022-02-09 | full |
| `ARXIV-2601.19138` | AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection | arXiv | academic | https://arxiv.org/abs/2601.19138 | 2026-01-27 | full |
| `ARXIV-2601.02941` | SastBench: A Benchmark for Testing Agentic SAST Triage | arXiv | academic | https://arxiv.org/abs/2601.02941 | 2026-01-06 | full |
| `ARXIV-2510.26103` | Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis of Public GitHub Repositories | arXiv | academic | https://arxiv.org/abs/2510.26103 | 2025-10-30 | full |
| `ARXIV-2609.29172` | Orchestrating AI-Assisted Code Remediation: Socio-Technical Bottlenecks in a Large Industrial Repository | arXiv | academic | https://arxiv.org/abs/2609.29172 | 2026-09-24 | full |
| `ARXIV-2608.23897` | Names Can Hurt: Spotting Slopsquatting Risks Caused by Package Name Hallucinations in Local Coding LLMs | arXiv | academic | https://arxiv.org/abs/2608.23897 | 2026-08-24 | full |
| `DARPA-AIXCC-2025` | AI Cyber Challenge marks pivotal inflection point for cyber defense (page undated; AIxCC final was at DEF CON 33, August 2025) | DARPA | regulator | https://www.darpa.mil/news/2025/aixcc-results | 2025-08 | full |
| `NIST-SSDF-218R1-2025` | SP 800-218 Rev. 1 (initial public draft), Secure Software Development Framework (SSDF) Version 1.2 | NIST CSRC | standard-setter | https://csrc.nist.gov/pubs/sp/800/218/r1/ipd | 2025-12-17 | full |
| `NIST-SP800218A-2024` | SP 800-218A, Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile | NIST CSRC | standard-setter | https://csrc.nist.gov/pubs/sp/800/218/a/final | 2024-07-26 | full |
| `EC-CRA-2026` | Cyber Resilience Act (policy page; undated, date is retrieval date; text cites guidance of 2026-07-27) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act | 2026-10-17 | full |
| `OPENSSF-AIGUIDE-2025` | Security-Focused Guide for AI Code Assistant Instructions | OpenSSF Best Practices and AI/ML Working Groups | standard-setter | https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions | 2025-08-01 | full |
| `ISC2-WORKFORCE-2025` | 2025 ISC2 Cybersecurity Workforce Study | ISC2 | professional-body | https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study | 2025-12-04 | full |
| `SOCKET-NVD-2026` | NIST Proposes AI-Enabled NVD Overhaul After Cutting Routine CVE Enrichment | Socket Blog | vendor | https://socket.dev/blog/nist-nvd-ai-automation | 2026-08-17 | full |
| `ANTHROPIC-JOB-APPSEC-2026` | Job posting: Staff+ Application Security Engineer (first published 2025-01-22, updated 2026-08-21) | Anthropic (Greenhouse) | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/4502508008 | 2026-08-21 | full |
| `DATADOG-JOB-PSE-AGENTS-2026` | Job posting: Senior Product Security Engineer - AI Agents | Datadog (Greenhouse) | job-posting | https://careers.datadoghq.com/detail/7993198/?gh_jid=7993198 | 2026-06-10 | full |
| `DATADOG-JOB-APPSEC-2026` | Job posting: Senior Application Security Engineer | Datadog (Greenhouse) | job-posting | https://careers.datadoghq.com/detail/8230663/?gh_jid=8230663 | 2026-09-25 | full |
| `GITLAB-JOB-CODESEC-2026` | Job posting: Senior Software Engineer, Security Factory: Code Security | GitLab (Greenhouse) | job-posting | https://job-boards.greenhouse.io/gitlab/jobs/8738179002 | 2026-10-09 | full |
| `COINBASE-JOB-PSE-2026` | Job posting: Product Security Engineer (Offensive Security, Application Security team) | Coinbase (Greenhouse) | job-posting | https://www.coinbase.com/careers/positions/8165389?gh_jid=8165389 | 2026-08-28 | full |
| `CLOUDFLARE-JOB-PSE-2026` | Job posting: Product Security Engineer | Cloudflare (Greenhouse) | job-posting | https://boards.greenhouse.io/cloudflare/jobs/8102768?gh_jid=8102768 | 2026-08-04 | full |
| `STRIPE-JOB-VM-2026` | Job posting: Software Engineer, Vulnerability Management | Stripe (Greenhouse) | job-posting | https://stripe.com/jobs/search?gh_jid=8089353 | 2026-08-04 | full |
| `MONGODB-JOB-PSE-2026` | Job posting: Senior Product Security Engineer, Assessments | MongoDB (Greenhouse) | job-posting | https://www.mongodb.com/careers/job/?gh_jid=8268264 | 2026-10-12 | full |
| `SAMSARA-JOB-APPSEC-2026` | Job posting: Staff Application Security Engineer | Samsara (Greenhouse) | job-posting | https://www.samsara.com/company/careers/roles/8205149?gh_jid=8205149 | 2026-09-15 | full |
| `REDDIT-JOB-PSE-2026` | Job posting: Staff Product Security Engineer | Reddit (Greenhouse) | job-posting | https://job-boards.greenhouse.io/reddit/jobs/7868511 | 2026-04-29 | full |
| `OKTA-JOB-PSE-2026` | Job posting: Staff Product Security Engineer, Reviews | Okta (Greenhouse) | job-posting | https://www.okta.com/company/careers/opportunity/8156825?gh_jid=8156825 | 2026-09-17 | full |
| `CURL-TEAM-2026` | The 2026 curl team | daniel.haxx.se (Daniel Stenberg, curl lead maintainer) | community | https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/ | 2026-10-12 | full |

## 6. Gaps

- **Independent outcome evidence.** No independent measurement of AI appsec tools in production: override rates, acceptance of review comments, false-negative rates, cost per validated finding, or parallel runs against human review. Figures are self-reported or vendor-published, and the one independent confirmation (curl) covers counts, not accuracy.
- **Named customer deployments with figures.** Vendor posts mostly cite unnamed customers (Semgrep, Snyk, Wiz Red Agent). Named users were found only for Codex Security (NETGEAR quote, vLLM), Mozilla/Firefox, curl/Aisle, Atlassian (research setting) and the large in-house teams.
- **Conference content is announcements, not delivered talks.** [un]prompted runs 2026-10-27 to 2026-10-29, after the research date, so the Meta, Stripe, Rubrik, Microsoft, Google Cloud and AISLE items are abstracts only. The FIRST PSIRT 2.0 session was TLP:AMBER. Black Hat, DEF CON, OWASP Global AppSec USA (2026-11-05 to 2026-11-06) and RSAC session content were not reached.
- **Sources not reached or only partly read.** Microsoft's primary announcements (MDASH and FORGE Lab appear only as a session abstract), Gartner and Forrester research, the 1Password AI patching report itself, the full text of arXiv papers (abstracts only), the Glasswing update that the Rubrik abstract cites for a two-week average patch time, Socket's Anthropic case study (undated, access blocked on direct fetch), Cursor and CodeRabbit product evidence, Checkmarx, Black Duck, and SANS/GIAC workforce reports.
- **Undated pages not used as outcome support.** The Stack Overflow 2026 developer survey AI page and Sonatype's 2026 supply chain report loaded but carried no publication date, so they are not cited.
- **Junior-engineer pipeline and role data.** No hard data on entry-level AppSec hiring or on how reviewer judgement changes beyond one company's pull-request panel.
- **Supply chain depth.** AI-specific evidence on SBOM generation, provenance, and CI/CD pipeline hardening was not found beyond vendor announcements; IaC scanning with AI was not covered.
- **Date and metric caveats.** Semgrep blog dates come from the blog listing, not article metadata. The Anthropic CVD dashboard's funnel text did not make the denominator of its 92.7% true-positive figure unambiguous. Pages for OpenAI Codex docs, GitHub's application card and the EU CRA are undated and carry the retrieval date.
- **Terminology.** CISA and NIST pages were flagged in the landscape as showing 'Super Intelligence' in place of 'AI'; the NIST SSDF pages read here used ordinary terms.

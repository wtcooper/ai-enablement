# Security / application-security: governance and evidence (wave 4)

Compiled 2026-10-17. Archetype: security. Module: application-security. Angle: governance (what constrains and measures the work). Working method: pages opened with curl, pdftotext and the r.jina.ai mirror; 2 web searches used for items that could not be reached directly (those items are marked `search-only` and kept out of A/B outcomes). Figures are copied with the source's own denominator; provenance is marked on every outcome.

## 1. Summary

- **The regulatory frame has not caught up with AI in AppSec.** The binding texts that constrain secure development say nothing about AI as a tool. The EU Cyber Resilience Act (reporting duties from 2026-09-11, main duties from 2027-12-11), NIS2 Article 21(2)(e) and the DORA RTS on ICT risk (Delegated Regulation (EU) 2024/1774, Article 16: source code review covering static and dynamic testing, including open-source code before deployment) all set outcome duties. A keyword search of the DORA RTS text and of the NIST SSDF 1.2 initial public draft (2025-12-17) found no mention of AI. NIS2 recitals 51 and 89 only encourage AI-based tools. The AI-specific material is voluntary: NIST SP 800-218A (AI model development), the NIST Cyber AI Profile draft (IR 8596), NCSC UK's "vibe coding spectrum" (2026-06-18), the OpenSSF assistant-instructions guide (2025-08-01) and the Linux kernel's AI contribution rules.
- **The best quality evidence is on AI-written security patches, and it is contested.** 1Password's FLAWED study (6,080 valid iterations) found 26.0% of agent patches fully mitigated the target flaw with no side effects. Trail of Bits disputes that headline, reanalysing the same data to 86% for trials where agents could run code and were not told to apply the wrong fix, and reports that maintainers merged 126 of 186 agent-written Patch the Planet pull requests. An academic benchmark (PatchBench) found proof-of-concept-only validation inflates agent solve rates by 1.83x on average. No source offers a like-for-like human-versus-agent comparison; Trail of Bits says its human figure (12.5% of first fixes incomplete) is not directly comparable.
- **Measured security of AI-generated code is poor but the studies are of mixed quality.** Veracode (vendor): 45% of samples failed security tests. A formal-verification preprint: 55.8% of 3,500 artifacts had a flagged vulnerability. CodeRabbit (vendor): AI-co-authored pull requests had about 1.7x more issues. A large-scale academic measurement finds that AI-introduced defects persist longer when human review is shallow.
- **AI review and AI scanning are themselves attack surfaces.** A 2026 preprint got a bias-injection attack past two real review pipelines in 32 of 33 cases; an NDSS 2026 paper shows familiar-pattern attacks on LLM static analysis. Regulators (NCSC UK) say oversight should scale with code criticality.
- **Vulnerability volume is the pressure.** Google Threat Intelligence Group counts disclosures doubling from 5,045 (Jan 2026) to 10,740 (Aug 2026) a month, but cautions that automated CNA assignment inflates counts. Ireland's NCSC (2026-04-13) noted the frontier model behind these claims was unavailable for independent testing.

Evidence grades across the 22 use cases: A 4, B 7, C 4, D 7.

## 2. Use cases

```yaml
- id: security-application-security-01
  title: Pre-submit agentic security scanning of every code change, grounded in live threat models
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance, software-systems]
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Security scans of large code bases are one-off, slow and short on context, so flaws are found late. Code volume is rising with AI-assisted development."
  solution: "Google describes scanning each code check-in with AI agents before submission, using its open-source Mantis multi-agent review harness. Agents are paired with localized threat models built from live code base metadata and a dependence call graph. A post-submit scan in nightly integration testing is a second layer."
  outcomes:
    - lever: risk
      description: "Google states the pipeline is preventing hundreds of vulnerabilities per month from reaching its code base or production."
      figure: "hundreds per month"
      measures: "Vulnerabilities prevented from reaching the code base or production per month, across hundreds of millions of lines of code deployed on Google infrastructure (the source gives no exact count or denominator)."
      provenance: self-reported
      source_ref: GOOGLE-AGENTICSCAN-2026
    - lever: quality
      description: "Localized threat models reduce false positives."
      figure: "3% false-positive rate 'in some cases'"
      measures: "False-positive rate of the scanning agent in some cases, as stated; the source does not define the denominator or say how many cases."
      provenance: self-reported
      source_ref: GOOGLE-AGENTICSCAN-2026
  prerequisites:
    - "Existing threat models that can be kept current from code base metadata."
    - "Pre-submit hook in the tools developers already use, with low latency."
    - "Dependence call graph across packages and libraries."
  risks_and_guardrails:
    - "Google advises keeping the development, scanning and triage agents' harnesses, rules and context separate to prevent bias (GOOGLE-AGENTICSCAN-2026, section 'Learnings and call to action')."
    - "Pair lightweight AI scans with deterministic structural validation (same section)."
    - "Reviewers of LLM-assisted security review should know that pull-request framing can bias LLM judgments (ARXIV-2603.18740, abstract)."
  human_checkpoints:
    - "Fixes proposed by the bug-fix agent go to human review as part of the original change request (GOOGLE-AGENTICSCAN-2026)."
  role_evolution: "Security becomes a routine developer-tool check, like readability or rule checkers, rather than a periodic expert scan (GOOGLE-AGENTICSCAN-2026). Developers are expected to keep threat models up to date because the scanner consumes them."
  evidence_grade: A
  sources:
    - { ref: GOOGLE-AGENTICSCAN-2026, title: "Changing the game: Using agentic AI to secure infrastructure code (Using AI agents to secure Google infrastructure)", publisher: "Google Cloud Blog (AI Infrastructure team)", type: vendor, url: "https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/", date: 2026-09-19, access: full, locator: "sections 'Pervasive pre-submit agentic scanning', 'The importance of localized threat models'" }
    - { ref: ARXIV-2603.18740, title: "Measuring and Exploiting Contextual Bias in LLM-Assisted Security Code Review", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2603.18740", date: 2026-03-19, access: full, locator: abstract }
  last_reviewed: 2026-10-17
  notes: "In-house case study published by Google about its own infrastructure; figures are self-reported and not independently audited. The post's 'in some cases' wording on the 3% rate means it should not be read as an average. Landscape also lists a GTIG post of 2026-08-18 on agentic source code review that was not opened."

- id: security-application-security-02
  title: Reachability-proving triage agent that validates scanner findings before developers see them
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance]
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Scanner output is noisy; checking every finding for exploitability delays check-ins and burns reviewer time."
  solution: "A lightweight scan's findings are checked by a specialized triage agent that uses abstract syntax tree parsing, call-graph traversal and pre-indexed domain safety rules to show whether the vulnerable path is reachable by an attacker."
  outcomes:
    - lever: quality
      description: "Triage agent precision and turnaround as stated by Google."
      figure: "over 92% precision; under one minute"
      measures: "Precision of the specialized triage agent, as stated in the source ('over 92% precision'); the source does not define numerator, denominator or sample size. Time is the agent's completion time per finding."
      provenance: self-reported
      source_ref: GOOGLE-AGENTICSCAN-2026
  prerequisites:
    - "Deterministic code-structure tooling (AST, call graph) the agent can call."
    - "Pre-indexed domain safety rules."
  risks_and_guardrails:
    - "Precision is stated without recall; missed findings are not reported in the source."
    - "Google keeps triage separate from the scanning and development agents to avoid shared bias (GOOGLE-AGENTICSCAN-2026)."
  human_checkpoints:
    - "Not stated for triage verdicts; human review is stated only for proposed fixes."
  role_evolution: "Not stated in the source."
  evidence_grade: A
  sources:
    - { ref: GOOGLE-AGENTICSCAN-2026, title: "Changing the game: Using agentic AI to secure infrastructure code", publisher: "Google Cloud Blog", type: vendor, url: "https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/", date: 2026-09-19, access: full, locator: "section 'Specialized triage agents speed up development'" }
  last_reviewed: 2026-10-17
  notes: "Precision only; no recall or sampling method published. Treat as a self-reported design claim from a named in-house deployment."

- id: security-application-security-03
  title: Bug-fix agent turns scanner proofs into fixes that go to the normal code review
  archetype: security
  module: application-security
  function: technology-it
  work_types: [software-systems]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Finding vulnerabilities is only half the work; the time between detection and resolution is long."
  solution: "An automated bug-fix agent uses scan results and generated proofs (code showing how the flaw is exercised) to construct fixes consistent with internal coding standards, and submits them for human review within the original change request."
  outcomes:
    - lever: speed
      description: "Google says the agent reduces time between detection and resolution; no figure is given."
      figure: "none published"
      measures: "No measure published."
      provenance: self-reported
      source_ref: GOOGLE-AGENTICSCAN-2026
  prerequisites:
    - "Scanner output that includes a proof snippet."
    - "Internal coding standards the agent can follow."
  risks_and_guardrails:
    - "Independent studies show agent patches can be incomplete or introduce new flaws: 1Password's FLAWED study found 26.0% of agent patches fully clean (ONEPASSWORD-FLAWED-2026, section 5.1); see use case 09."
  human_checkpoints:
    - "Human review of the fix as part of the change request (GOOGLE-AGENTICSCAN-2026)."
  role_evolution: "Not stated in the source."
  evidence_grade: B
  sources:
    - { ref: GOOGLE-AGENTICSCAN-2026, title: "Changing the game: Using agentic AI to secure infrastructure code", publisher: "Google Cloud Blog", type: vendor, url: "https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/", date: 2026-09-19, access: full, locator: "section 'Bug fix agents close the loop'" }
    - { ref: ONEPASSWORD-FLAWED-2026, title: "Frontier Models' Vulnerability Patches are Often F.L.A.W.E.D.", publisher: "1Password (Off-by-1 Labs)", type: vendor, url: "https://1password.com/files/resources/frontier-models-vulnerability-patches-flawed.pdf", date: 2026-08-06, access: full, locator: "section 5.1" }
  last_reviewed: 2026-10-17
  notes: "Named in-house deployment with no published fix-quality measure, so B. Date of the 1Password report is taken from the Trail of Bits post (TOB-1PASSWORD-2026), which says it was published on 2026-08-06."

- id: security-application-security-04
  title: Risk-tiered automated review that lands low-risk diffs without a human reviewer
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance]
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "AI-assisted coding raised code volume faster than reviewer capacity: lines per human-landed diff rose and the share of diffs getting timely review fell."
  solution: "Meta's RADAR classifies each diff by authorship and source type, applies eligibility gates, static heuristics, a machine-learned Diff Risk Score, LLM-based automated code review and deterministic validation before landing qualifying changes."
  outcomes:
    - lever: capacity
      description: "Volume reviewed and landed by the funnel."
      figure: "535K+ diffs reviewed; 331K+ landed"
      measures: "Diffs reviewed by RADAR and diffs landed through it, per the authors' telemetry."
      provenance: self-reported
      source_ref: ARXIV-2605.30208
    - lever: quality
      description: "Revert and production-incident rates for RADAR-reviewed diffs compared with non-RADAR diffs."
      figure: "revert rate 1/3; production incident rate 1/50 of non-RADAR diffs"
      measures: "Revert rate and Production Incident rate of RADAR-reviewed diffs relative to non-RADAR diffs. The abstract does not say whether the comparison diffs were matched for risk; RADAR only lands diffs that pass its eligibility and risk gates."
      provenance: self-reported
      source_ref: ARXIV-2605.30208
    - lever: speed
      description: "Review latency effects."
      figure: "median review wall time down 35%; median time to close down 'over 330%'"
      measures: "Median diff review wall time and median time to close, from difference-in-differences analysis, as worded in the abstract."
      provenance: self-reported
      source_ref: ARXIV-2605.30208
    - lever: capacity
      description: "Effect of loosening the risk threshold."
      figure: "approve rate 60.31%"
      measures: "Approve rate after relaxing the Diff Risk Score threshold from the 25th to the 50th percentile."
      provenance: self-reported
      source_ref: ARXIV-2605.30208
  prerequisites:
    - "A trained diff risk model and deterministic validation in the landing path."
    - "Telemetry to track reverts and production incidents."
  risks_and_guardrails:
    - "The measured safety outcomes are reverts and production incidents, not security defects."
    - "LLM-based review can be steered by crafted pull-request context (ARXIV-2603.18740)."
  human_checkpoints:
    - "Diffs failing gates go to human reviewers; the abstract does not describe sampling of auto-landed diffs."
  role_evolution: "Reviewer attention is reserved for higher-risk changes; authors' framing is review capacity as the bottleneck created by AI-driven code growth (ARXIV-2605.30208)."
  evidence_grade: B
  sources:
    - { ref: ARXIV-2605.30208, title: "Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency", publisher: "arXiv (Meta authors)", type: academic, url: "https://arxiv.org/abs/2605.30208", date: 2026-05-28, access: full, locator: abstract }
  last_reviewed: 2026-10-17
  notes: "Grade capped at B: the measurements are general code-review efficiency and production-safety outcomes, adjacent to security-specific review. Only the abstract was read; the full paper may qualify the comparison."

- id: security-application-security-05
  title: Human-validated AI-assisted vulnerability discovery reported to maintainers
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Audits of mature code bases find fewer issues each round, and maintainers are swamped by low-quality reports."
  solution: "Aisle engineers pointed AI-powered tooling at the curl source code over about a year, with skilled humans validating findings, producing published CVEs and commits. Separately, GTIG tracks vulnerabilities that were likely surfaced by autonomous agents and finds a different risk profile from conventionally found ones."
  outcomes:
    - lever: quality
      description: "curl's lead maintainer reports the number of published vulnerabilities from Aisle's work."
      figure: "35"
      measures: "Published curl vulnerabilities and CVE IDs resulting from Aisle engineers' use of AI-powered tooling on curl over 'the last year or so', per the maintainer."
      provenance: independent
      source_ref: CURL-AISLE-2026
    - lever: risk
      description: "GTIG compares AI-discovered with other vulnerabilities."
      figure: "50% of AI-discovered vulnerabilities lead to RCE versus 26% across the broader CVE ecosystem"
      measures: "Share of vulnerabilities, January to August 2026, with remote code execution as exploitation consequence, among those GTIG identified as likely AI-discovered versus those not identified as AI-discovered. GTIG says public data undercount AI-found flaws."
      provenance: vendor-published
      source_ref: GTIG-VULNTRENDS-2026
    - lever: risk
      description: "Time to exploitation after disclosure of one AI-discovered flaw."
      figure: "first exploiting cluster within 4 days; five more within 7 days"
      measures: "Threat clusters GTIG observed exploiting CVE-2026-1731 (found by a third-party research agent) after public disclosure."
      provenance: vendor-published
      source_ref: GTIG-VULNTRENDS-2026
  prerequisites:
    - "Skilled humans to validate each finding; the maintainer credits 'a team of skilled humans' behind the findings."
    - "A working relationship with the maintainer and coordinated disclosure."
  risks_and_guardrails:
    - "Defenders' discoveries can be weaponised quickly after disclosure (GTIG-VULNTRENDS-2026)."
    - "Kernel policy tells AI users to build a reproducer before reporting, because many unverified reports prove invalid (LINUX-KERNEL-AI-2026)."
  human_checkpoints:
    - "Human validation of findings before CVE publication (CURL-AISLE-2026)."
  role_evolution: "Audit firm staff author commits in the project (CURL-AISLE-2026); validation of AI findings becomes the scarce skill."
  evidence_grade: A
  sources:
    - { ref: CURL-AISLE-2026, title: "A curl audit by Aisle", publisher: "Daniel Stenberg (daniel.haxx.se)", type: community, url: "https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/", date: 2026-10-14, access: full, locator: "paragraphs 1-4" }
    - { ref: GTIG-VULNTRENDS-2026, title: "Vulnerability Discovery and Exploitation Trends in the AI Era", publisher: "Google Threat Intelligence Group", type: vendor, url: "https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/", date: 2026-09-30, access: full, locator: "sections 'AI as the Hunter', 'Risk Profile Divergence'" }
  last_reviewed: 2026-10-17
  notes: "The maintainer's count is a third-party statement, hence 'independent', but Aisle's own blog (reported by the maintainer as '24 CVEs, 18 ship today') was not read. The same post names a curl high-severity report found by Anthropic's 'OSS Scanner' (presumably AI-based, per the maintainer). Vendor-authored GTIG figures rely on a heuristic AI-attribution method."

- id: security-application-security-06
  title: Frontier-model autonomous vulnerability discovery with restricted defensive access
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: "Finding and exploiting software flaws has needed scarce expert time, so many flaws go unnoticed for years."
  solution: "Anthropic's Project Glasswing gives a consortium of large technology companies access to an unreleased model (Claude Mythos Preview) to find and fix flaws in widely used software, with disclosure to maintainers and hashed details published until fixes land."
  outcomes:
    - lever: risk
      description: "Anthropic reports it found thousands of high-severity vulnerabilities, including in every major operating system and web browser."
      figure: "thousands (no exact count)"
      measures: "Zero-day vulnerabilities Anthropic says it identified with the model 'over the past few weeks' before 2026-04-07; the post states nearly all were found autonomously. Not independently verified."
      provenance: vendor-published
      source_ref: ANTHROPIC-GLASSWING-2026
  prerequisites:
    - "Restricted access programme with coordinated disclosure."
    - "Maintainer capacity to receive and patch the findings."
  risks_and_guardrails:
    - "Ireland's NCSC said on 2026-04-13 the model was unavailable for independent testing and urged safeguards, coordinated disclosure and engagement with national CSIRTs (GOVIE-NCSC-2026)."
    - "UK NCSC expects a 'forced correction' of technical debt and advises preparing for a 'patch wave' (CW-NCSCUK-2026)."
    - "Anthropic said it would report publicly within 90 days (ANTHROPIC-GLASSWING-2026); that report was not located."
  human_checkpoints:
    - "Reports go to maintainers; hashes of undisclosed details are published until fixes are in place (ANTHROPIC-GLASSWING-2026)."
  role_evolution: "Maintainers and defenders face higher disclosure volume; Ireland's NCSC advises reviewing asset inventories and patch discipline (GOVIE-NCSC-2026)."
  evidence_grade: C
  sources:
    - { ref: ANTHROPIC-GLASSWING-2026, title: "Project Glasswing", publisher: Anthropic, type: vendor, url: "https://www.anthropic.com/glasswing", date: 2026-04-07, access: full, locator: "opening and 'zero-day' paragraphs" }
    - { ref: GOVIE-NCSC-2026, title: "NCSC statement on Anthropic's Mythos Preview model for defensive cyber security purposes", publisher: "Ireland NCSC (Department of Justice, Home Affairs and Migration)", type: regulator, url: "https://www.gov.ie/en/department-of-justice-home-affairs-and-migration/press-releases/national-cyber-security-centre-ncsc-statement-on-anthropics-mythos-preview-model-for-defensive-cyber-security-purposes/", date: 2026-04-13, access: full, locator: "paragraphs 1-4" }
    - { ref: CW-NCSCUK-2026, title: "UK's NCSC warns of 'wave of patches'", publisher: Computer Weekly, type: press, url: "https://computerweekly.com/news/366642625/UKs-NCSC-warns-of-wave-of-patches", date: 2026-05-04, access: full, locator: "quotes from NCSC CTO Ollie Whitehouse" }
  last_reviewed: 2026-10-17
  notes: "Vendor claim about its own model, so C. A security vendor CISO quoted in the Computer Weekly piece says Mozilla fixed 271 Firefox vulnerabilities found with the model; this is a secondhand quote, not verified against Mozilla."

- id: security-application-security-07
  title: Autonomous fuzzing pipeline that writes harnesses, reads coverage and triages crashes
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [software-systems, review-assurance]
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Fuzzing needs people to watch coverage, write harnesses for unreached code and triage crashes, so even long-enrolled projects keep hidden bugs."
  solution: "GitHub Security Lab's Fuzzing Taskflow Agent, pointed at a C/C++ repository, identifies entry points, analyses the build, writes harnesses, runs AFL++, reads coverage reports, improves harnesses, triages each crash and writes a report per unique bug with root cause, reachability and exploitability assessment, a suggested patch and regression test."
  outcomes:
    - lever: capacity
      description: "No quantified outcome in the post."
      figure: "none published"
      measures: "No measure published in the post; related posts listed in the landscape (24 Android vulnerabilities, 2026-09-28) were not opened."
      provenance: vendor-published
      source_ref: GITHUB-TASKFLOW-2026
  prerequisites:
    - "Buildable C/C++ project; sanitizer builds (ASan, UBSan) and separate coverage builds."
  risks_and_guardrails:
    - "The author states suggested patches are marked 'review required' because the agent can be wrong; verdicts are a starting point for a human."
    - "Distinguishes real vulnerabilities (reachable via public API) from harness bugs, a judgment call that otherwise needs manual tracing."
  human_checkpoints:
    - "Human review of every report and patch (GITHUB-TASKFLOW-2026)."
  role_evolution: "Human attention shifts from writing harnesses and reading coverage to validating reports."
  evidence_grade: B
  sources:
    - { ref: GITHUB-TASKFLOW-2026, title: "AI-powered fuzzing with the GitHub Security Lab Taskflow Agent", publisher: "GitHub Blog (Security Lab)", type: vendor, url: "https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/", date: 2026-09-24, access: full, locator: "intro and 'Triage and vulnerability reports'" }
  last_reviewed: 2026-10-17
  notes: "Named tool, openly released for maintainers; no published measurements in the post."

- id: security-application-security-08
  title: Autonomous cyber reasoning systems that find and patch vulnerabilities in open-source code
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [software-systems, review-assurance]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "Finding and patching vulnerabilities by current methods is slow, expensive and depends on a limited workforce (DARPA director, quoted)."
  solution: "DARPA's AI Cyber Challenge (AIxCC, 2023-2025) had seven finalist teams build fully autonomous systems; all seven systems are being released as open source and DARPA/ARPA-H added prizes to integrate them into critical-infrastructure-relevant software."
  outcomes:
    - lever: quality
      description: "Final-round discovery and patch rates against synthetic vulnerabilities, up from the semifinal."
      figure: "86% found (37% at semifinals); 68% of those found were patched (25% at semifinals)"
      measures: "Share of the competition's synthetic vulnerabilities identified by teams, and share of identified vulnerabilities patched, in the Final Competition scored round. In total 54 unique synthetic vulnerabilities were discovered in 63 challenges and 43 patched."
      provenance: independent
      source_ref: AIXCC-DARPA-2025
    - lever: cost
      description: "Average cost per competition task."
      figure: "about USD 152"
      measures: "Average cost per competition task of competitor systems, as stated by DARPA."
      provenance: independent
      source_ref: AIXCC-DARPA-2025
    - lever: quality
      description: "Real, non-synthetic findings."
      figure: "18 real vulnerabilities; 11 patches"
      measures: "Real vulnerabilities discovered in the Final Competition (6 in C, 12 in Java, being disclosed to maintainers) and patches the teams provided for real vulnerabilities."
      provenance: independent
      source_ref: AIXCC-DARPA-2025
  prerequisites:
    - "Open-source code base with build and test infrastructure; LLM credits (the frontier labs donated credits to each finalist)."
  risks_and_guardrails:
    - "Scoring used synthetic vulnerabilities, so rates may not transfer to production code; a USENIX Security 2026 systematization of the competition says it also exposes limitations that remain open (USENIX-SEC-2026, SoK abstract)."
    - "PatchBench shows PoC-only validation inflates agent patch success (ARXIV-2609.04075)."
  human_checkpoints:
    - "Real findings are disclosed to maintainers for confirmation (AIXCC-DARPA-2025)."
  role_evolution: "Not stated."
  evidence_grade: B
  sources:
    - { ref: AIXCC-DARPA-2025, title: "AI Cyber Challenge marks pivotal inflection point for cyber defense", publisher: DARPA, type: regulator, url: "https://www.darpa.mil/news/2025/aixcc-results", date: 2025-08, access: full, locator: "'Deep Dive: Final Competition Findings'" }
    - { ref: USENIX-SEC-2026, title: "SoK: DARPA's AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned (35th USENIX Security Symposium)", publisher: USENIX, type: academic, url: "https://www.usenix.org/conference/usenixsecurity26/technical-sessions", date: 2026-08, access: full, locator: "Software Security 2 session, abstract" }
  last_reviewed: 2026-10-17
  notes: "Capped at B: a government-run competition with synthetic vulnerabilities, adjacent to production AppSec. DARPA is the organizer and scorer, so figures are organizer-published. The page byline date was not captured; August 2025 is taken from the landscape and the event timing."

- id: security-application-security-09
  title: Agent-written security patches reviewed and merged by maintainers
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [software-systems, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: "Vulnerability findings pile up faster than people can write and verify fixes. Developers' own first fixes are often incomplete."
  solution: "Trail of Bits, with OpenAI under 'Patch the Planet', co-authored hundreds of patches for open-source projects: agents wrote the patches, engineers directed and checked them, and maintainers decided whether to merge."
  outcomes:
    - lever: quality
      description: "Maintainer acceptance of agent-written security pull requests."
      figure: "126 of 186 merged (67.7%); 91 of 126 merged (72.2%) with no security-relevant revision observed; 33 (26.2%) with security-relevant revision"
      measures: "Pull requests in Trail of Bits' dataset that maintainers had merged or closed by 2026-09-14 (186); of the 126 merged, those accepted with or without security-relevant revisions. Of 60 closed unmerged, 4 were explicitly rejected on technical grounds."
      provenance: self-reported
      source_ref: TOB-1PASSWORD-2026
    - lever: quality
      description: "Defects found after merge."
      figure: "10+ functional bugs, 4 build/test/release automation bugs, 1 performance bug; no exploitable security vulnerabilities"
      measures: "Result of reviewing about 33,500 subsequent commits in Patch the Planet projects for later changes that repaired a problem the Trail of Bits patch introduced; the firm says it is extending the review to all its patches."
      provenance: self-reported
      source_ref: TOB-1PASSWORD-2026
    - lever: quality
      description: "Autonomous patch success in a controlled study."
      figure: "26.0% fully mitigated with no side effects; 49.3% failed to fix at least one exploit path; 4.5% introduced a new vulnerability"
      measures: "Share of 6,080 valid iterations (two frontier coding agents, six recent high-complexity CVEs, several prompting and iteration modes) graded S1 (clean), S3 (unsuccessful, no new vulnerability), and S4+S5 (new vulnerability introduced). Trail of Bits says the sample was chosen for difficulty, 22% of the data used prompts telling agents to apply a wrong fix and 36% prohibited testing."
      provenance: vendor-published
      source_ref: ONEPASSWORD-FLAWED-2026
    - lever: quality
      description: "Trail of Bits reanalysis of the 1Password data."
      figure: "2,634 of 3,067 patches (86%) blocked the supplied exploit"
      measures: "Patches from trials in which agents could run code and were not instructed to apply the wrong fix, excluding runs that consulted the upstream fix; blocking the exploit does not establish a complete repair, as the authors note."
      provenance: self-reported
      source_ref: TOB-1PASSWORD-2026
    - lever: quality
      description: "Academic check of patch-benchmark validity."
      figure: "25% of agent patches substantially similar to historical developer patches; PoC-only validation inflates solve rates by 1.83x on average across 11 agents"
      measures: "C/C++ vulnerability patching; patch similarity metric for memorisation; solve rate under original PoC-only validation versus PatchBench's validation, across 11 agents including the top three AIxCC agents."
      provenance: independent
      source_ref: ARXIV-2609.04075
    - lever: quality
      description: "Human baseline from Trail of Bits consulting."
      figure: "283 of 2,265 first fixes (12.5%) failed to fully resolve the issue; 95% CI 10.5% to 14.5%"
      measures: "First fixes submitted for reported vulnerabilities across 236 assessments, 2024-2026, as reviewed by Trail of Bits. The firm says this may undercount failures and is not directly comparable with agent results."
      provenance: self-reported
      source_ref: TOB-1PASSWORD-2026
  prerequisites:
    - "Maintainers willing to review; a skilled engineer directing the agent."
    - "Validation that tests more than the supplied exploit: variant paths, regressions, sanitizers or fuzzing."
  risks_and_guardrails:
    - "Agent and human maintainer made the same cleanup-path crash on one freenginx fix (TOB-1PASSWORD-2026)."
    - "1Password concludes highly automated LLM remediation pipelines are more likely to change behaviour or introduce or mask vulnerabilities than fix them, and recommends tightly constrained environments with skilled oversight (ONEPASSWORD-FLAWED-2026, abstract)."
    - "Validate with more than a PoC; PoC-only checks overstate success (ARXIV-2609.04075)."
  human_checkpoints:
    - "Engineer directs and checks the agent; maintainer decides on merge (TOB-1PASSWORD-2026)."
  role_evolution: "Engineers become directors and verifiers of agent patches; maintainer review is the quality gate."
  evidence_grade: A
  sources:
    - { ref: TOB-1PASSWORD-2026, title: "1Password's AI patching benchmark is misleading", publisher: "Trail of Bits blog", type: firm, url: "https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/", date: 2026-09-15, access: full, locator: "sections 'What happened to our patches in real projects', 'How the experiment produces a misleading headline'" }
    - { ref: ONEPASSWORD-FLAWED-2026, title: "Frontier Models' Vulnerability Patches are Often F.L.A.W.E.D.", publisher: "1Password (Off-by-1 Labs)", type: vendor, url: "https://1password.com/files/resources/frontier-models-vulnerability-patches-flawed.pdf", date: 2026-08-06, access: full, locator: "abstract; section 3.1; section 5.1" }
    - { ref: ARXIV-2609.04075, title: "PatchBench: Evaluating AI Agents for Vulnerability Patching", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.04075", date: 2026-09-03, access: full, locator: abstract }
  last_reviewed: 2026-10-17
  notes: "The strongest quality evidence found, but the sources conflict and use different samples: 1Password measured autonomous patching on six hard CVEs; Trail of Bits measured human-directed patches accepted by maintainers. The 1Password report's own date was not printed in the PDF text read; 2026-08-06 comes from the Trail of Bits post. Trail of Bits co-runs Patch the Planet, so its figures are self-reported. 1Password's study ran on models named in the paper; no other vendor reproduced it."

- id: security-application-security-10
  title: Agent skills for post-patch validation and interactive review walkthroughs
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Agent patches can be incomplete or regress behaviour, and engineers must review them."
  solution: "Trail of Bits released post-patch-validation (reproduce the bug, test a variant path, check regressions, treat broken test runs as inconclusive) and review-walkthrough (turns a branch diff into a reading-order walkthrough with findings beside the code), alongside variant-analysis, property-based-testing and mutation-testing skills."
  outcomes:
    - lever: quality
      description: "No measured outcome."
      figure: "none published"
      measures: "The firm states post-patch-validation was not used in the Patch the Planet work described."
      provenance: self-reported
      source_ref: TOB-1PASSWORD-2026
  prerequisites:
    - "An agent harness that can load skills; vulnerability report and vulnerable and patched revisions."
  risks_and_guardrails:
    - "Failed or missing test runs must not count as evidence of reproduction (TOB-1PASSWORD-2026, 'Agent skills for better security patches')."
  human_checkpoints:
    - "Engineers review the patches they are responsible for merging, using the walkthrough."
  role_evolution: "Not stated."
  evidence_grade: C
  sources:
    - { ref: TOB-1PASSWORD-2026, title: "1Password's AI patching benchmark is misleading", publisher: "Trail of Bits blog", type: firm, url: "https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/", date: 2026-09-15, access: full, locator: "section 'Agent skills for better security patches'" }
  last_reviewed: 2026-10-17
  notes: "Released tooling announced by the firm, with no use evidence; C."

- id: security-application-security-11
  title: Agentic exploit validation of web applications as dynamic testing, with a validator layer filtering false positives
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [review-assurance]
  pattern: full-population-testing
  ladder: automate
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Scanners flag possible issues; proving exploitability needs skilled testers."
  solution: "AWS Security Agent (now part of AWS Continuum) attempts end-to-end exploitation of vulnerable targets; a validation layer labels findings as confirmed-exploitable, low-confidence or auto-labeled false positive."
  outcomes:
    - lever: quality
      description: "Result on AWS's own audited benchmark of recent CVEs."
      figure: "33 of 37 (89.2%)"
      measures: "CVEs from 2025-2026 in an internally developed CTF-style benchmark that the agent captured through the intended vulnerability end to end, confirmed by a per-sample audit against the canonical PoC; the audit reclassified 2 captures as off the intended path and they count as unsolved."
      provenance: vendor-published
      source_ref: AWS-SECAGENT-2026
    - lever: quality
      description: "Validator layer on 475 surfaced findings."
      figure: "159 labeled auto false positives; more than 1,200 additional findings de-duplicated"
      measures: "Findings surfaced across the benchmark targets that the validation layer labeled as the agent's own false positives, plus additional findings de-duplicated; 234 further high-confidence issues were confirmed beyond the seeded CVEs."
      provenance: vendor-published
      source_ref: AWS-SECAGENT-2026
  prerequisites:
    - "Authorised, isolated targets; non-destructive guardrails for production engagements."
  risks_and_guardrails:
    - "In both misses the agent's exploitation took the target down; the benchmark ran without the non-destructive guardrails that govern production engagements (AWS-SECAGENT-2026)."
    - "AWS says public CVE benchmarks are effectively saturated by training-data contamination, which is why it built a refreshed, audited one."
  human_checkpoints:
    - "Per-sample human-and-tool integrity audit of every capture (benchmark only)."
  role_evolution: "Not stated."
  evidence_grade: B
  sources:
    - { ref: AWS-SECAGENT-2026, title: "AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs", publisher: "AWS Security Blog", type: vendor, url: "https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/", date: 2026-10-15, access: full, locator: "sections 'Why we built a fresh benchmark', 'Signal quality', 'We audited every win'" }
  last_reviewed: 2026-10-17
  notes: "Vendor self-test on known CVEs, not a customer deployment; grade capped at B per adjacency (benchmark, not production AppSec). Overlaps vulnerability-exposure (penetration testing)."

- id: security-application-security-12
  title: Evaluate security agents on contamination-resistant, audited benchmarks before adopting them
  archetype: security
  module: application-security
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Vendor and public benchmark scores for AI security tools can be inflated by memorisation, weak validation or unrepresentative samples, and secure-code benchmarks for code models often test function rather than security."
  solution: "Buyers and engineering leads check patch and exploit claims with checks that go beyond the original PoC: patch-similarity tests for memorisation, transplanted and mutated vulnerabilities, per-win audits, and reporting of failure categories separately."
  outcomes:
    - lever: risk
      description: "Evidence that unvalidated benchmarks overstate performance."
      figure: "25% of agent patches substantially similar to historical developer patches; 1.83x average inflation of solve rate under PoC-only validation"
      measures: "C/C++ patching study across 11 agents, as in use case 09."
      provenance: independent
      source_ref: ARXIV-2609.04075
    - lever: risk
      description: "Dispute over how to read a headline patching rate."
      figure: "26.0% (1Password) versus 86% (Trail of Bits reanalysis)"
      measures: "See use case 09: different subsets and success definitions applied to the same dataset."
      provenance: vendor-published
      source_ref: TOB-1PASSWORD-2026
  prerequisites:
    - "Access to benchmark data and code; engineers able to audit samples."
  risks_and_guardrails:
    - "CSET observed that code-model evaluation benchmarks often measure function but not security, and training-data transparency is inadequate (CSET-CODEGEN-2024, key findings)."
    - "AWS reports a refreshed benchmark with per-sample audit that caught two benchmark faults (AWS-SECAGENT-2026)."
  human_checkpoints:
    - "Human audit of automated grading (Trail of Bits found model graders matched human reviewers on the full five-category outcome in 65.9% of reviewed cases in the 1Password study)."
  role_evolution: "Security leads become evaluators of AI tool claims."
  evidence_grade: B
  sources:
    - { ref: ARXIV-2609.04075, title: "PatchBench: Evaluating AI Agents for Vulnerability Patching", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.04075", date: 2026-09-03, access: full, locator: abstract }
    - { ref: TOB-1PASSWORD-2026, title: "1Password's AI patching benchmark is misleading", publisher: "Trail of Bits blog", type: firm, url: "https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/", date: 2026-09-15, access: full, locator: "'How the experiment produces a misleading headline'" }
    - { ref: AWS-SECAGENT-2026, title: "AWS Security Agent exploited 33 of 37 new real-world CVEs", publisher: "AWS Security Blog", type: vendor, url: "https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/", date: 2026-10-15, access: full, locator: "section 'Why we built a fresh benchmark'" }
    - { ref: CSET-CODEGEN-2024, title: "Cybersecurity Risks of AI-Generated Code", publisher: "Georgetown CSET", type: academic, url: "https://cset.georgetown.edu/publication/cybersecurity-risks-of-ai-generated-code/", date: 2024-11, access: full, locator: "key findings" }
  last_reviewed: 2026-10-17
  notes: "Practice evidence is named organizations publishing their own evaluation methods and critiques, not a buyer programme; grade B reflects that. The 65.9% agreement figure is as reported by Trail of Bits from the 1Password paper's Table 24."

- id: security-application-security-13
  title: Separate AI reviewer pass over AI-generated code, backed by deterministic checks
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Code assistants produce insecure code by default, and human reviewers cannot keep pace."
  solution: "Asking a model (or a separate agent) to review generated code for security issues before human review. A formal-verification preprint found models identified their own vulnerable outputs far more often in review mode than they avoided producing them. Google advises keeping generator, scanner and triage agents separate and pairing AI with deterministic validation."
  outcomes:
    - lever: quality
      description: "Self-review detection versus default generation."
      figure: "78.7% identified in review mode versus 55.8% vulnerable at default generation"
      measures: "Share of the models' own vulnerable outputs they identified when asked to review them, versus share of 3,500 artifacts (7 LLMs, 500 security-critical prompts) containing at least one vulnerability flagged by the authors' COBALT/Z3 pipeline."
      provenance: independent
      source_ref: ARXIV-2604.05292
  prerequisites:
    - "Deterministic checks (tests, SAST, sanitizers) in addition to the model."
  risks_and_guardrails:
    - "Contextual-bias injection into pull-request metadata got past two real review pipelines (Claude Code and CodeRabbit) in 32 of 33 CVE re-introduction cases; the authors stress human oversight (ARXIV-2603.18740, abstract)."
    - "Six industry tools combined missed 97.8% of the preprint's Z3-proven findings (ARXIV-2604.05292, abstract)."
  human_checkpoints:
    - "Human review remains the control; NCSC UK says another AI agent can help with the oversight activities (NCSC-VIBE-2026)."
  role_evolution: "Reviewers supervise machine review output."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2604.05292, title: "Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2604.05292", date: 2026-04-07, access: full, locator: abstract }
    - { ref: ARXIV-2603.18740, title: "Measuring and Exploiting Contextual Bias in LLM-Assisted Security Code Review", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2603.18740", date: 2026-03-19, access: full, locator: abstract }
    - { ref: NCSC-VIBE-2026, title: "The 'vibe coding spectrum' approach to AI-assisted software development", publisher: "UK National Cyber Security Centre", type: regulator, url: "https://www.ncsc.gov.uk/sites/default/files/2026-07/The-vibe-coding-spectrum-approach-to-AI-assisted-software-development.pdf", date: 2026-06-18, access: full, locator: "'It's about oversight, not avoidance'" }
  last_reviewed: 2026-10-17
  notes: "Preprint (8 pages) using the authors' own tool; not peer reviewed at time of reading. C because evidence is research measurement plus guidance, with no named production measurement."

- id: security-application-security-14
  title: Disclosure, attribution and human accountability rules for AI-assisted contributions
  archetype: security
  module: application-security
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Tool-generated contributions raise submission volume while reviewer and maintainer bandwidth is scarce; provenance and legal certification are unclear."
  solution: "The Linux kernel project's documentation tells AI tools and developers to follow the standard process; bars AI agents from adding Signed-off-by tags (only humans certify the Developer Certificate of Origin); asks for an 'Assisted-by' tag naming the model and analysis tools; and requires that bug reports from AI assistants include a reproducer for non-trivial bugs and that fixes are written."
  outcomes:
    - lever: risk
      description: "No measured outcome; the page explains the aim of keeping trust and conserving reviewer bandwidth."
      figure: "none published"
      measures: "No measure published."
      provenance: self-reported
      source_ref: LINUX-KERNEL-AI-2026
  prerequisites:
    - "Existing patch process and DCO sign-off culture."
  risks_and_guardrails:
    - "The human submitter reviews all AI-generated code, checks licensing (GPL-2.0-only compatibility) and takes full responsibility (LINUX-KERNEL-AI-2026, 'Signed-off-by and Developer Certificate of Origin')."
    - "Lacking a reproducer may cause a report to be ignored, as many unverified bug reports to maintainers are invalid (same page, 'Procedure for finding and fixing bugs')."
  human_checkpoints:
    - "Human certification of origin and human review before submission."
  role_evolution: "Contributors using AI carry explicit accountability for the output."
  evidence_grade: B
  sources:
    - { ref: LINUX-KERNEL-AI-2026, title: "AI Coding Assistants; Kernel Guidelines for Tool-Generated Content", publisher: "The Linux Kernel documentation", type: community, url: "https://docs.kernel.org/process/coding-assistants.html", date: 2026, access: full, locator: "sections 'Signed-off-by and Developer Certificate of Origin', 'Attribution', 'Procedure for finding and fixing bugs'; companion page https://docs.kernel.org/process/generated-content.html 'Purpose'" }
  last_reviewed: 2026-10-17
  notes: "Named project policy in force, no outcome data. The pages show no publication date; the documentation build read was version 7.3.0-rc7, so the date is recorded as 2026 only. A git history check was not possible."

- id: security-application-security-15
  title: Oversight level set by code criticality for AI-assisted development
  archetype: security
  module: application-security
  function: risk-compliance-legal
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Blanket bans or blanket acceptance of AI-generated code do not match differing risk."
  solution: "NCSC UK's 'vibe coding spectrum': move toward manual coding for authentication and authorisation logic, sensitive personal data, secrets handling and safety-critical or CNI code; accept full vibe coding for prototypes, demos and low-exposure internal tools. For higher-risk work: review, understand, check for vulnerabilities and verify; consider ETSI baseline requirements."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Guidance only."
      provenance: independent
      source_ref: NCSC-VIBE-2026
  prerequisites:
    - "Classification of code by criticality and exposure."
  risks_and_guardrails:
    - "NCSC says to calibrate to today's model reliability, not tomorrow's potential."
    - "Research shows both generated code and AI review can fail (ARXIV-2604.05292; ARXIV-2603.18740)."
  human_checkpoints:
    - "Review, understanding, vulnerability checks and verification for high-risk code."
  role_evolution: "Developers and architects choose a position on the spectrum per project and architect the wider system to limit the impact of exploitation."
  evidence_grade: D
  sources:
    - { ref: NCSC-VIBE-2026, title: "The 'vibe coding spectrum' approach to AI-assisted software development", publisher: "UK National Cyber Security Centre", type: regulator, url: "https://www.ncsc.gov.uk/sites/default/files/2026-07/The-vibe-coding-spectrum-approach-to-AI-assisted-software-development.pdf", date: 2026-06-18, access: full, locator: "'Choosing your position'" }
  last_reviewed: 2026-10-17
  notes: "Idea: regulator guidance with no named adopter or measurement found."

- id: security-application-security-16
  title: Security measurement and gating of AI-generated code before merge
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "AI-generated code often carries security flaws, defaults to insecure patterns, and spreads similar flaws across unrelated projects."
  solution: "Treat AI-authored code as untrusted: apply SAST, SCA, secrets and formal checks at the pull request, track AI-authored share, and focus human review where AI concentrates or where flaws persist."
  outcomes:
    - lever: risk
      description: "Share of generated samples failing security tests."
      figure: "45%"
      measures: "Code samples that 'failed security tests and introduced OWASP Top 10 vulnerabilities' in Veracode's tests of over 100 LLMs across Java, JavaScript, Python and C#; Java failure rate 72%; cross-site scripting (CWE-80) defended in only 14% of relevant samples (failed in 86%)."
      provenance: vendor-published
      source_ref: VERACODE-GENAI-2025
    - lever: risk
      description: "Formal-verification measurement of default generation."
      figure: "55.8%; explicit security instructions cut the mean by 4 points"
      measures: "Share of 3,500 artifacts from 7 LLMs on 500 security-critical prompts (five CWE categories) with at least one COBALT-identified vulnerability; 1,055 formally proven by Z3 witnesses; no model better than grade D."
      provenance: independent
      source_ref: ARXIV-2604.05292
    - lever: risk
      description: "Pull-request level issue rates."
      figure: "about 1.7x issues overall; security issues up to 2.74x"
      measures: "Issues per pull request across 470 open-source GitHub PRs (320 AI-co-authored, 150 human-only): 10.83 versus 6.45; security issues up to 2.74 times higher in AI PRs."
      provenance: vendor-published
      source_ref: CODERABBIT-2025
    - lever: risk
      description: "Ecosystem measurement of AI-written code in the wild."
      figure: "qualitative"
      measures: "Study of commits from the top 1,000 GitHub repositories (2022-2025) and 7,000+ CVE-linked code changes: AI concentrates in glue code, tests, refactoring and boilerplate; when review is shallow, AI-introduced defects persist longer and spread further."
      provenance: independent
      source_ref: ARXIV-2512.18567
  prerequisites:
    - "Reliable detection of AI-authored changes (hard; the Dec 2025 study built its own detection pipeline)."
    - "Pipeline security gates and policy on what blocks a merge."
  risks_and_guardrails:
    - "Existing secure-development practices and the NIST CSF remain the baseline; the burden should not rest only on individual users (CSET-CODEGEN-2024, key findings)."
    - "Industry scanners can miss flaws a formal method finds (ARXIV-2604.05292)."
    - "A user study found participants with an assistant wrote less secure code and were more confident in it (ARXIV-2211.03622)."
  human_checkpoints:
    - "Humans act as security gatekeepers in human-AI edit chains (ARXIV-2512.18567)."
  role_evolution: "Reviewers triage AI volume; trust calibration matters: more developers distrust AI accuracy (46%) than trust it (33%) in Stack Overflow's 2025 survey (STACKOVERFLOW-2025)."
  evidence_grade: C
  sources:
    - { ref: VERACODE-GENAI-2025, title: "Insights from 2025 GenAI Code Security Report", publisher: Veracode, type: vendor, url: "https://www.veracode.com/blog/genai-code-security-report/", date: 2025-07-30, access: full, locator: "findings section" }
    - { ref: ARXIV-2604.05292, title: "Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2604.05292", date: 2026-04-07, access: full, locator: abstract }
    - { ref: CODERABBIT-2025, title: "State of AI vs Human Code Generation Report", publisher: CodeRabbit, type: vendor, url: "https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report", date: 2025-12-17, access: full, locator: "findings 1 and 6" }
    - { ref: ARXIV-2512.18567, title: "AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code in Modern Software", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2512.18567", date: 2025-12-21, access: full, locator: abstract }
    - { ref: CSET-CODEGEN-2024, title: "Cybersecurity Risks of AI-Generated Code", publisher: "Georgetown CSET", type: academic, url: "https://cset.georgetown.edu/publication/cybersecurity-risks-of-ai-generated-code/", date: 2024-11, access: full, locator: "key findings" }
    - { ref: ARXIV-2211.03622, title: "Do Users Write More Insecure Code with AI Assistants?", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2211.03622", date: 2022-11-07, access: full, locator: abstract }
    - { ref: STACKOVERFLOW-2025, title: "2025 Developer Survey: AI", publisher: "Stack Overflow", type: survey, url: "https://survey.stackoverflow.co/2025/ai", date: 2025, access: full, locator: "'Accuracy of AI tools'" }
  last_reviewed: 2026-10-17
  notes: "Measurements are of code generation, not of a deployed gating practice, so C. Veracode and CodeRabbit are vendors with products in the area; the formal-verification result is a preprint using the authors' own pipeline and its 97.8% miss rate depends on that pipeline. The Stack Overflow page gives the survey year but no publication date. The CCS-era user study used an older model (codex-davinci-002), so it is a foundation, not current evidence."

- id: security-application-security-17
  title: Adversarial testing of AI code-review and static-analysis pipelines
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "LLM-based review and analysis are trusted to catch bugs, but can be steered by presentation of context or by familiar-looking code."
  solution: "Red-team the review pipeline (for example with misleading pull-request metadata or familiar-pattern code edits) before relying on it, and keep human and deterministic controls in the path."
  outcomes:
    - lever: risk
      description: "none published as a deployed practice (idea)"
      figure: "32 of 33"
      measures: "Vulnerability re-introduction cases (33 CVEs across 20 real-world projects, two pipelines: Claude Code and CodeRabbit) in which the authors' LLM-assisted refinement attack succeeded; template-based attacks were ineffective."
      provenance: independent
      source_ref: ARXIV-2603.18740
  prerequisites:
    - "A copy of the review pipeline to test against."
  risks_and_guardrails:
    - "NDSS 2026 'Familiar Pattern Attacks' are transferable across OpenAI, Anthropic and Google models and remain effective when models are warned (NDSS-FPA-2026, abstract)."
  human_checkpoints:
    - "Human oversight and contributor trust stressed by the authors (ARXIV-2603.18740)."
  role_evolution: "Not stated."
  evidence_grade: D
  sources:
    - { ref: ARXIV-2603.18740, title: "Measuring and Exploiting Contextual Bias in LLM-Assisted Security Code Review", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2603.18740", date: 2026-03-19, access: full, locator: abstract }
    - { ref: NDSS-FPA-2026, title: "Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias", publisher: "NDSS Symposium 2026", type: academic, url: "https://www.ndss-symposium.org/ndss-paper/trust-me-i-know-this-function-hijacking-llm-static-analysis-using-bias/", date: 2026-02, access: full, locator: abstract }
  last_reviewed: 2026-10-17
  notes: "Idea: researchers discuss the testing need; no organization was found running such tests. Attack details deliberately not recorded beyond what defenders need."

- id: security-application-security-18
  title: Checking AI-suggested dependencies against registries before install
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance]
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Code-generating models invent package names, a new route for package-confusion attacks on the software supply chain."
  solution: "Verify that every package an assistant adds exists, is the intended one and passes dependency policy before it is installed; the paper evaluates mitigation strategies that reduce hallucinations."
  outcomes:
    - lever: risk
      description: "none published as a deployed practice (idea)"
      figure: "at least 5.2% (commercial models); 21.7% (open-source models)"
      measures: "Average percentage of hallucinated packages across 576,000 code samples in two languages from 16 LLMs, with 205,474 unique hallucinated package names."
      provenance: independent
      source_ref: USENIX-SEC-2025-HALLUC
  prerequisites:
    - "Dependency allow-lists or registry verification in the build."
  risks_and_guardrails:
    - "The paper reports mitigation strategies significantly reduce hallucinations while maintaining code quality; effects in production were not found."
  human_checkpoints:
    - "Not stated."
  role_evolution: "Not stated."
  evidence_grade: D
  sources:
    - { ref: USENIX-SEC-2025-HALLUC, title: "We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs", publisher: "USENIX Security 2025 (Distinguished Paper)", type: academic, url: "https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen", date: 2025-08, access: full, locator: abstract }
  last_reviewed: 2026-10-17
  notes: "Idea: peer-reviewed measurement of the problem; no named organization deploying the control was found in this pass."

- id: security-application-security-19
  title: Security-focused instruction files for AI code assistants
  archetype: security
  module: application-security
  function: technology-it
  work_types: [software-systems]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Assistants default to insecure patterns unless security requirements are stated."
  solution: "OpenSSF's guide describes writing custom instructions (for example Claude markdown, Copilot instructions, Cursor rules) covering application code security, supply chain safety and language-specific points, and asking the assistant to review and improve its own work."
  outcomes:
    - lever: risk
      description: "none published as a deployed practice (idea)"
      figure: "4 points"
      measures: "Reduction in the mean vulnerable-artifact rate when explicit security instructions were added, in the Broken by Default preprint (3,500 artifacts, 7 LLMs)."
      provenance: independent
      source_ref: ARXIV-2604.05292
  prerequisites:
    - "A team convention for sharing assistant instruction files."
  risks_and_guardrails:
    - "OpenSSF says the guidance is expert opinion and literature, not measured, and warns irrelevant copied instructions can cause extraneous or incorrect code (OPENSSF-AIGUIDE-2025)."
    - "The developer remains responsible; AI output goes through normal review, testing and static analysis (same source, TL;DR)."
  human_checkpoints:
    - "Developer critically evaluates and edits AI output."
  role_evolution: "Developers act as owners of the instructions as well as the code."
  evidence_grade: D
  sources:
    - { ref: OPENSSF-AIGUIDE-2025, title: "Security-Focused Guide for AI Code Assistant Instructions", publisher: "OpenSSF Best Practices and AI/ML Working Groups", type: standard-setter, url: "https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions", date: 2025-08-01, access: full, locator: "TL;DR" }
    - { ref: ARXIV-2604.05292, title: "Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2604.05292", date: 2026-04-07, access: full, locator: abstract }
  last_reviewed: 2026-10-17
  notes: "Idea: published guidance and a single small measured effect; no named adopter."

- id: security-application-security-20
  title: Threat models derived from code and tracked as diffs to detect security intent drift
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance, document-production]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "When AI-assisted changes arrive faster than people can review them, security-relevant behaviour can change without a traditional vulnerability."
  solution: "A USENIX Security 2026 talk describes automatically deriving threat models from code, infrastructure and configuration artifacts and computing threat-model diffs to flag changes to attack surfaces, trust boundaries, privilege relationships and sensitive data flows."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Talk abstract only."
      provenance: self-reported
      source_ref: USENIX-SEC-2026
  prerequisites:
    - "Code, infrastructure and configuration artifacts parseable into a model."
  risks_and_guardrails:
    - "Not stated."
  human_checkpoints:
    - "Not stated beyond maintaining 'security oversight'."
  role_evolution: "Not stated."
  evidence_grade: D
  sources:
    - { ref: USENIX-SEC-2026, title: "35th USENIX Security Symposium technical sessions (talk by Preeti Ravindra on deriving and diffing threat models)", publisher: USENIX, type: conference, url: "https://www.usenix.org/conference/usenixsecurity26/technical-sessions", date: 2026-08, access: full, locator: "talk abstract preceding the Test of Time discussion" }
  last_reviewed: 2026-10-17
  notes: "Idea from a practitioner talk. Google's pre-submit scanner (use case 01) uses live threat models as context, a related but different change."

- id: security-application-security-21
  title: LLM-guided runtime containment as a stopgap between detection and patch
  archetype: security
  module: application-security
  function: technology-it
  work_types: [software-systems]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "A 'response gap' between vulnerability detection and patching leaves web applications exposed; code fixes can break functionality and global runtime policies cause false positives."
  solution: "Kintsugi (USENIX Security 2026) uses differential syscall analysis to locate vulnerability-related functions, an LLM to delineate the offending code and set policy trigger points, then temporary runtime protection."
  outcomes:
    - lever: risk
      description: "none read"
      figure: "none published"
      measures: "Abstract was read only up to the pipeline description; results were not captured."
      provenance: independent
      source_ref: USENIX-SEC-2026
  prerequisites:
    - "Reproducible normal and malicious request traces."
  risks_and_guardrails:
    - "Not read."
  human_checkpoints:
    - "Not read."
  role_evolution: "Not stated."
  evidence_grade: D
  sources:
    - { ref: USENIX-SEC-2026, title: "Kintsugi: Empowering LLMs to Mitigate Web Vulnerabilities via Runtime Policy Injection (USENIX Security 2026)", publisher: USENIX, type: academic, url: "https://www.usenix.org/conference/usenixsecurity26/technical-sessions", date: 2026-08, access: full, locator: "session listing with abstract" }
  last_reviewed: 2026-10-17
  notes: "Research prototype idea; no deployment found."

- id: security-application-security-22
  title: LLM filtering of static-analysis false positives
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Static analysers raise many false alarms."
  solution: "A search result for an ICSE 2026 software-engineering-in-practice paper describes hybrid LLM plus static analysis approaches in an industrial setting."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "Search-only figures not recorded as outcomes."
      provenance: independent
      source_ref: ICSE-SEIP-2026
  prerequisites:
    - "Not read."
  risks_and_guardrails:
    - "Not read."
  human_checkpoints:
    - "Not read."
  role_evolution: "Not stated."
  evidence_grade: D
  sources:
    - { ref: ICSE-SEIP-2026, title: "Reducing False Positives in Static Bug Detection with LLMs: An Empirical Study in Industry", publisher: "ICSE 2026 Software Engineering in Practice", type: conference, url: "https://conf.researchr.org/details/icse-2026/icse-2026-software-engineering-in-practice/72/Reducing-False-Positives-in-Static-Bug-Detection-with-LLMs-An-Empirical-Study-in-Ind", date: 2026, access: search-only, locator: "search result summary" }
  last_reviewed: 2026-10-17
  notes: "Search-only. The search summary said the hybrid approach eliminated 94-98% of false positives with high recall in a Tencent study; this is unverified and kept out of outcomes. Page not opened; exact date not confirmed."
```

## 3. Module notes

**Processes and key steps (with work types)**
- Secure SDLC requirements, design and threat modelling (expert-judgment, document-production).
- Secure coding and code review: human and AI review, pre-submit checks (review-assurance, software-systems).
- Static, dynamic and interactive testing, fuzzing, penetration testing (review-assurance, software-systems).
- Software supply chain: dependency intake, SBOM, provenance (review-assurance, data-reporting).
- Vulnerability handling: triage, fix, disclosure, regulatory reporting (transaction-processing, coordination-scheduling).
- Security governance: policy, maturity benchmarking, attestation (review-assurance).

**Common pain points**
- Code volume outpaces reviewer capacity. Meta: lines per human-landed diff +105.9% year over year, per-developer diff volume +51%, with agentic AI responsible for over 80% of that growth, while the share of diffs receiving timely review fell (ARXIV-2605.30208).
- Disclosure volume. GTIG counts monthly disclosures at 5,045 (Jan 2026) and 10,740 (Aug 2026) but says automated CNA assignment inflates counts (about 5,000 Linux kernel CVEs Jan-Aug 2026 with no observed exploited zero-days) (GTIG-VULNTRENDS-2026).
- Fix quality: 12.5% of developers' first fixes were incomplete in Trail of Bits' reviews (TOB-1PASSWORD-2026).
- Public data undercount AI-found flaws: no standard AI-attribution metadata in CVE records, and cloud/SaaS providers patch without CVEs (GTIG-VULNTRENDS-2026).

**Metrics and benchmarks (with sources)**
- Patch quality: 1Password S1-S5 grading (26.0% clean, 4.5% new-vulnerability rate, 10.8% cheat rate) (ONEPASSWORD-FLAWED-2026); maintainer acceptance 67.7% (TOB-1PASSWORD-2026); PatchBench 1.83x inflation (ARXIV-2609.04075).
- Discovery and patching on synthetic flaws: AIxCC 86% found, 68% patched (AIXCC-DARPA-2025).
- AI-generated code: Veracode 45%; formal verification 55.8%; CodeRabbit 1.7x issues (use case 16).
- Software security maturity: BSIMM16 analysed 111 organizations and was published January 2026; the landing page names AI adoption, supply chain/SBOM growth and regulatory self-attestation as themes. The report body is gated and was not read (BLACKDUCK-BSIMM-2026).
- Developer sentiment: Stack Overflow 2025: 46% actively distrust AI tool accuracy, 33% trust it, 3% highly trust; 87% concerned about accuracy and 81% about security and privacy of data (STACKOVERFLOW-2025).
- Independent measurement of AI review precision/recall in production: none found.

**Guardrails and regulatory points**
- EU CRA: reporting of actively exploited vulnerabilities and severe incidents applies from 2026-09-11 (early warning within 24 hours, full notification within 72 hours, final report within 14 days after a corrective measure for exploited vulnerabilities), through ENISA's Single Reporting Platform; main obligations from 2027-12-11; Commission guidance 2026-07-27 (EC-CRA-2026, EC-CRA-REPORTING-2026).
- NIS2 Article 21(2)(e): security in acquisition, development and maintenance, including vulnerability handling and disclosure. Recitals 51 and 89 encourage AI/ML tools (EURLEX-NIS2-2022).
- DORA RTS (Delegated Regulation (EU) 2024/1774) Article 16(3) and (8): source code review covering static and dynamic testing, with an action plan and monitoring; proprietary, third-party and, where feasible, open-source code analysed before production. Paragraph 9 extends this to systems built outside the ICT function on a risk basis. No AI-specific text found (EURLEX-DORA-RTS-2024).
- EU AI Act: applicable 2026-08-02; Annex III high-risk obligations moved to 2027-12-02 and Annex I to 2028-08-02 by the AI Omnibus (in force 2026-07-27); the July 2026 Action Plan plans an EU capacity to evaluate advanced models before placing on the market, expected operational by 2027 (EC-AIACT-2026).
- NIST: SSDF 1.2 initial public draft (2025-12-17, comments closed 2026-01-30) responds to Executive Order 14306 and contains no AI-specific text in the PDF read (NIST-SSDF-218R1-2025). SP 800-218A (July 2024) augments SSDF 1.1 for AI model development, not for using AI to write code (NIST-SSDF-218A-2024). The Cyber AI Profile preliminary draft (IR 8596, 2025-12-16) has three focus areas (Secure, Defend, Thwart) and, for CSF 2.0 PR.PS-06 (secure software development), a Secure-area note to extend AI checks to secure software development with prompt tests, adversarial tests and evaluation gates; its Defend text lists AI source-code vulnerability detection among examples (NIST-CYBERAI-2025). The COSAiS overlays cover AI system uses including AI agents (NIST-COSAIS-2026).
- CISA Secure by Design (revised 2023-10-25; ten US and international partners initially, then eight more co-sealers) and CISA/ACSC joint guidance on adopting agentic AI (2026-05-01; landing page only read) (CISA-SBD-2023, CISA-AGENTIC-2026).
- UK Software Security Code of Practice: 14 principles for vendors, first published 2025-05-07, updated 2026-01-15 (UK-DSIT-SSCOP-2025). NCSC UK vibe coding spectrum (NCSC-VIBE-2026).
- Open-source projects: Linux kernel rules (use case 14). CRA reporting duties also reach open-source software stewards (EC-CRA-REPORTING-2026).

**Frontier signals (dated, sourced)**
- 2025-08: AIxCC finals; all seven systems to be open-sourced (AIXCC-DARPA-2025).
- 2026-04-07: Project Glasswing announced; 2026-04-13 Ireland's NCSC response; 2026-05-04 UK NCSC "patch wave" guidance (ANTHROPIC-GLASSWING-2026, GOVIE-NCSC-2026, CW-NCSCUK-2026).
- 2026-08-06 / 2026-09-15: 1Password FLAWED report and Trail of Bits rebuttal; 2026-09-03 PatchBench (see use case 09).
- 2026-09-19: Google moves to pre-submit agentic scanning (use case 01). 2026-09-24: GitHub Taskflow fuzzing agent.
- 2026-09-11: CRA reporting platform live. 2026-10-14: curl publishes Aisle audit (35 CVEs).
- OWASP Global AppSec USA 2026-11-05/06 and ACM CCS 2026-11-15/19 are upcoming and unread.

**Workforce and role effects**
- Validation becomes the bottleneck: the curl maintainer credits "a team of skilled humans" behind accepted findings (CURL-AISLE-2026); 1Password concludes oversight from skilled engineers with domain expertise is needed (ONEPASSWORD-FLAWED-2026).
- Humans act as security gatekeepers in human-AI edit chains and shallow review lets defects persist (ARXIV-2512.18567).
- Developers' accountability is explicit under kernel rules (LINUX-KERNEL-AI-2026).
- A user study found assistant users wrote less secure code yet were more confident; participants who trusted the AI less and engaged more wrote fewer vulnerabilities (ARXIV-2211.03622, older model).

**Objections and concerns practitioners raise**
- Benchmarks mislead (Trail of Bits on 1Password; AWS on public CVE suites; PatchBench).
- The frontier model behind the flood claims could not be independently tested (GOVIE-NCSC-2026).
- AI review can be manipulated (ARXIV-2603.18740; NDSS-FPA-2026).
- Defensive discoveries are weaponised within days (GTIG-VULNTRENDS-2026).
- Reviewer bandwidth and invalid reports (LINUX-KERNEL-AI-2026).
- Precision claims without recall (use case 02).

**Interview probes for an advisor**
1. Which code is AI-authored today, how do you know, and what share ships without line-by-line human review?
2. What check beyond the original exploit or test decides that an AI-written fix is accepted? Who audits the grader?
3. If disclosures double next quarter, which step breaks first: triage, fix, review or release, and what is your CRA or NIS2 reporting clock for an actively exploited flaw?
4. Which AI scanner, reviewer or patcher claims did you accept from a vendor, and what did you measure yourself (false positives, missed findings, reverts)?
5. How would you detect an attack on your own AI review pipeline, for example through pull-request text or familiar-looking code?

## 4. Routed to other modules

- **vulnerability-exposure**: GTIG disclosure/exploitation trends and its advice to move from mass patching to threat-intelligence-driven triage with automated remediation (GTIG-VULNTRENDS-2026); UK/Ireland NCSC "patch wave" preparedness (CW-NCSCUK-2026, GOVIE-NCSC-2026); missing AI-attribution metadata in CVE records; AWS exploit agent as penetration testing (AWS-SECAGENT-2026); PatchWeaver, a USENIX Security 2026 system for policy-bounded autonomous remediation of Kubernetes workloads (reported 4.73% versus 9.95% step-level policy violations against a toolchain baseline; abstract only) (USENIX-SEC-2026).
- **ai-security**: NIST SP 800-218A, COSAiS overlays and the Cyber AI Profile "Secure" area (securing AI systems); GTIG's 2,076 cumulative AI-related CVEs (over 1,500 in Jan-Aug 2026) in agent and LLM frameworks (GTIG-VULNTRENDS-2026); OWASP agentic and LLM lists (landing pages only); CISA/ACSC agentic AI adoption guidance; GoodVibe (neuron-level security tuning of code models, USENIX Security 2026).
- **governance-risk**: mapping CRA, NIS2, DORA and AI Act duties to one control set; BSIMM16 benchmarking; the SEC incident-disclosure debate (not examined here).
- **security-operations**: none from this pass.

## 5. Sources

Type counts (43 documents): regulator 11 (including DARPA, typed that way for lack of a better value), academic 11, vendor 8, standard-setter 5, community 2, survey 2, conference 2, press 1, firm 1. Of the 43, 42 were opened (`access: full`; for CISA agentic guidance and BSIMM16 only the landing page) and 1 is `search-only` (ICSE-SEIP-2026). IEEE-SP-2026 was scanned for titles only and supports no claim.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| NIST-SSDF-218A-2024 | SP 800-218A, Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile | NIST | standard-setter | https://csrc.nist.gov/pubs/sp/800/218/a/final | 2024-07 |
| NIST-SSDF-218R1-2025 | SP 800-218 Rev 1 initial public draft, Secure Software Development Framework (SSDF) 1.2 | NIST | standard-setter | https://csrc.nist.gov/pubs/sp/800/218/r1/ipd | 2025-12-17 |
| NIST-CYBERAI-2025 | IR 8596 initial preliminary draft, Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile) | NIST | standard-setter | https://csrc.nist.gov/pubs/ir/8596/iprd | 2025-12-16 |
| NIST-COSAIS-2026 | SP 800-53 Control Overlays for Securing AI Systems (COSAiS) | NIST | standard-setter | https://csrc.nist.gov/projects/cosais | 2026-01-08 |
| EC-CRA-2026 | Cyber Resilience Act | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act | 2026-09-07 |
| EC-CRA-REPORTING-2026 | Cyber Resilience Act reporting obligations | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/cra-reporting | 2026-09-11 |
| EC-AIACT-2026 | AI Act regulatory framework (status page) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10 |
| EURLEX-NIS2-2022 | Directive (EU) 2022/2555 (NIS2) | EU | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555 | 2022-12-27 |
| EURLEX-DORA-RTS-2024 | Commission Delegated Regulation (EU) 2024/1774 (ICT risk management framework) | EU | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1774 | 2024-06-25 |
| CISA-SBD-2023 | Secure-by-Design: Shifting the Balance of Cybersecurity Risk | CISA | regulator | https://www.cisa.gov/resources-tools/resources/secure-by-design | 2023-10-25 |
| CISA-AGENTIC-2026 | Careful Adoption of Agentic AI Services (landing page; page shows "SI") | CISA with ASD's ACSC | regulator | https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services | 2026-05-01 |
| GOVIE-NCSC-2026 | NCSC statement on Anthropic's Mythos Preview model | Ireland NCSC | regulator | https://www.gov.ie/en/department-of-justice-home-affairs-and-migration/press-releases/national-cyber-security-centre-ncsc-statement-on-anthropics-mythos-preview-model-for-defensive-cyber-security-purposes/ | 2026-04-13 |
| CW-NCSCUK-2026 | UK's NCSC warns of 'wave of patches' | Computer Weekly | press | https://computerweekly.com/news/366642625/UKs-NCSC-warns-of-wave-of-patches | 2026-05-04 |
| NCSC-VIBE-2026 | The 'vibe coding spectrum' approach to AI-assisted software development | UK NCSC | regulator | https://www.ncsc.gov.uk/sites/default/files/2026-07/The-vibe-coding-spectrum-approach-to-AI-assisted-software-development.pdf | 2026-06-18 |
| UK-DSIT-SSCOP-2025 | Software Security Code of Practice | UK DSIT / NCSC | regulator | https://www.gov.uk/government/publications/software-security-code-of-practice | 2025-05-07 |
| AIXCC-DARPA-2025 | AI Cyber Challenge marks pivotal inflection point for cyber defense | DARPA | regulator | https://www.darpa.mil/news/2025/aixcc-results | 2025-08 |
| GOOGLE-AGENTICSCAN-2026 | Changing the game: Using agentic AI to secure infrastructure code | Google Cloud Blog | vendor | https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/ | 2026-09-19 |
| GTIG-VULNTRENDS-2026 | Vulnerability Discovery and Exploitation Trends in the AI Era | Google Threat Intelligence Group | vendor | https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/ | 2026-09-30 |
| AWS-SECAGENT-2026 | AWS Security Agent exploited 33 of 37 new real-world CVEs | AWS Security Blog | vendor | https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/ | 2026-10-15 |
| GITHUB-TASKFLOW-2026 | AI-powered fuzzing with the GitHub Security Lab Taskflow Agent | GitHub Blog | vendor | https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/ | 2026-09-24 |
| ANTHROPIC-GLASSWING-2026 | Project Glasswing | Anthropic | vendor | https://www.anthropic.com/glasswing | 2026-04-07 |
| TOB-1PASSWORD-2026 | 1Password's AI patching benchmark is misleading | Trail of Bits | firm | https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/ | 2026-09-15 |
| ONEPASSWORD-FLAWED-2026 | Frontier Models' Vulnerability Patches are Often F.L.A.W.E.D. | 1Password (Off-by-1 Labs) | vendor | https://1password.com/files/resources/frontier-models-vulnerability-patches-flawed.pdf | 2026-08-06 |
| CURL-AISLE-2026 | A curl audit by Aisle | Daniel Stenberg | community | https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/ | 2026-10-14 |
| LINUX-KERNEL-AI-2026 | AI Coding Assistants; Kernel Guidelines for Tool-Generated Content | Linux kernel documentation | community | https://docs.kernel.org/process/coding-assistants.html | 2026 |
| OPENSSF-AIGUIDE-2025 | Security-Focused Guide for AI Code Assistant Instructions | OpenSSF | standard-setter | https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions | 2025-08-01 |
| VERACODE-GENAI-2025 | Insights from 2025 GenAI Code Security Report | Veracode | vendor | https://www.veracode.com/blog/genai-code-security-report/ | 2025-07-30 |
| CODERABBIT-2025 | State of AI vs Human Code Generation Report | CodeRabbit | vendor | https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report | 2025-12-17 |
| BLACKDUCK-BSIMM-2026 | BSIMM16 Report (landing page; report gated) | Black Duck | survey | https://www.blackduck.com/resources/analyst-reports/bsimm.html | 2026-01 |
| STACKOVERFLOW-2025 | 2025 Developer Survey: AI | Stack Overflow | survey | https://survey.stackoverflow.co/2025/ai | 2025 |
| CSET-CODEGEN-2024 | Cybersecurity Risks of AI-Generated Code | Georgetown CSET | academic | https://cset.georgetown.edu/publication/cybersecurity-risks-of-ai-generated-code/ | 2024-11 |
| ARXIV-2604.05292 | Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code | arXiv | academic | https://arxiv.org/abs/2604.05292 | 2026-04-07 |
| ARXIV-2512.18567 | AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code in Modern Software | arXiv | academic | https://arxiv.org/abs/2512.18567 | 2025-12-21 |
| ARXIV-2605.30208 | Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency | arXiv | academic | https://arxiv.org/abs/2605.30208 | 2026-05-28 |
| ARXIV-2609.04075 | PatchBench: Evaluating AI Agents for Vulnerability Patching | arXiv | academic | https://arxiv.org/abs/2609.04075 | 2026-09-03 |
| ARXIV-2603.18740 | Measuring and Exploiting Contextual Bias in LLM-Assisted Security Code Review | arXiv | academic | https://arxiv.org/abs/2603.18740 | 2026-03-19 |
| ARXIV-2211.03622 | Do Users Write More Insecure Code with AI Assistants? | arXiv | academic | https://arxiv.org/abs/2211.03622 | 2022-11-07 |
| ARXIV-2108.09293 | Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions (IEEE S&P 2022) | arXiv | academic | https://arxiv.org/abs/2108.09293 | 2021-08-20 |
| NDSS-FPA-2026 | Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias | NDSS Symposium | academic | https://www.ndss-symposium.org/ndss-paper/trust-me-i-know-this-function-hijacking-llm-static-analysis-using-bias/ | 2026-02 |
| USENIX-SEC-2026 | 35th USENIX Security Symposium technical sessions (AIxCC SoK, PatchWeaver, Kintsugi, GoodVibe, threat-model talk) | USENIX | academic | https://www.usenix.org/conference/usenixsecurity26/technical-sessions | 2026-08 |
| USENIX-SEC-2025-HALLUC | We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs | USENIX Security 2025 | academic | https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen | 2025-08 |
| IEEE-SP-2026 | IEEE Symposium on Security and Privacy 2026 program (titles scanned only) | IEEE | conference | https://sp2026.ieee-security.org/program.html | 2026-05 |
| ICSE-SEIP-2026 | Reducing False Positives in Static Bug Detection with LLMs: An Empirical Study in Industry (search-only) | ICSE 2026 SEIP | conference | https://conf.researchr.org/details/icse-2026/icse-2026-software-engineering-in-practice/72/Reducing-False-Positives-in-Static-Bug-Detection-with-LLMs-An-Empirical-Study-in-Ind | 2026 |

ARXIV-2108.09293 is a foundation reference listed but not relied on in any use case.

## 6. Gaps

- **Not reached or only partly read:** CISA/ACSC agentic guidance body (landing page only; cyber.gov.au failed); BSIMM16 report body and GitLab's 2026 DevSecOps survey (gated or figures only in images); OWASP agentic and LLM lists (landing pages only, not used for claims); Veracode and other 2026 follow-ups; Sonatype, Snyk, Cloudsmith and Endor supply-chain reports (fetch failed or returned older reports); the Aisle blog; the GitHub "50 open source projects" and Android posts; the Mozilla primary source for the 271-vulnerability claim; the GTIG 2026-08-18 agentic source code review post; full text of most USENIX, NDSS and IEEE papers (abstracts or titles only).
- **No independent measurement found** of production AI code-review or AI SAST precision/recall, override rates, or parallel-run results against human reviewers. The nearest are Google's precision-only claim and Meta's revert/incident comparison.
- **No like-for-like human versus agent patch comparison.**
- **No evidence found** of a regulator inspection finding on AI-generated code, or of a supervisory statement that AI use changes DORA, NIS2 or CRA obligations. SEC rules were not examined.
- **Anthropic's 90-day Glasswing report** and an independent test of the model were not located.
- **Dates:** Linux kernel pages (year only), Stack Overflow survey (year only), DARPA release (month inferred), EC AI Act page (living page, retrieved 2026-10-17), and the 1Password report date (taken from Trail of Bits). Pages for NIST and CISA showed the term "super intelligence (SI)" in place of AI in titles and body text on retrieval; document titles above use the original "AI" form where the same document displays it.
- Search was used twice; results gave a UK NCSC RSA 2026 keynote and a Cloud Security Alliance summary that were not opened and are not relied on.

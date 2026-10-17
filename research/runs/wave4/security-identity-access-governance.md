# Identity and access: governance and evidence deep dive

Archetype: security. Module: identity-access. Angle: governance (what constrains and measures the work). Compiled 2026-10-17. Working files were kept in a private `mktemp -d` folder. Web search was used 10 times (DHS remote-identity testing, identity-security surveys, Entrust identity-fraud report, access-review/IGA analyst views, EU payments regulation, SailPoint survey, Microsoft Digital Defense Report, bank deepfake-voice case studies, service-desk verification, account-takeover case studies). Everything else was opened with curl, pdftotext or the r.jina.ai text mirror. Sources opened and read are `access: full`; items seen only in search results are `access: search-only` and appear in notes, never in the outcomes of an A or B entry.

## 1. Summary

- **Regulators are further ahead than the evidence.** NIST SP 800-63-4 (July 2025) is the most concrete public rulebook for AI in this module. It requires remote identity proofing to detect injected and forged media, sets numeric thresholds (for example presentation-attack accept rate below 0.07 and document false-accept and false-reject rates of 0.1 or less), requires published test results, and adds a section that makes any use of AI or ML in an identity system documented, disclosed to relying parties and risk-assessed (`NIST-SP80063-4-2025`, `NIST-SP80063A-4-2025`). FinCEN (2024-11) and NYDFS (2024-10) say the same thing from the financial-regulator side: criminals use generative AI to circumvent identity verification (FinCEN) and deepfakes have been used to mimic a person's voice or appearance to defeat biometric checks (NYDFS), so both point to phishing-resistant factors and liveness checks, and NYDFS advises avoiding SMS, voice or video authentication (`FINCEN-ALERT004-2024`, `NYDFS-AIGUIDE-2024`).
- **No named-organization measurement of AI in IAM work was found.** There is no A or B entry. The only quantified deployment-like figure is a vendor's anonymised bank case (about 960 synthetic-voice calls flagged among 1.7M analysed, with no confirmation rate) (`REALDEFENDER-BANK-2025`). Access-review recommendation features, entitlement right-sizing and identity risk scoring are documented by Microsoft and Google with no accuracy, override-rate or reviewer-agreement figures (`MSFT-ENTRA-ACCESSREV-2026`, `GOOGLE-IAMREC-2026`).
- **The best independent measurements show the limits of detection.** Twelve state-of-the-art deepfake-voice detectors were benchmarked; the best equal error rate was 13.50% and all others exceeded 20% (`USENIX-VOICEWUKONG-2025`). A 2026 preprint finds modern voice cloning trained on very small samples can bypass commercial speaker verification (`ARXIV-2601.02914`). Passkeys, the main phishing-resistant answer, had at least one high-severity flaw on 53 of 103 evaluated sites (`USENIX-PASSKEYS-2026`).
- **Identity-related loss data is large but AI attribution is thin.** FBI IC3 2025: 22,364 complaints with AI-related information and USD 893,346,472 in adjusted losses; about 4,700 account-takeover complaints and USD 359.7 million in losses (`FBI-IC3-2025`). The IC3 itself says many victims do not realise how far AI was involved.
- **The pressure is moving to non-human identities.** A vendor survey (n=2,930, fielded Mar-Apr 2026) reports 109 machine identities per human and that 90% of organizations had at least one identity-related breach in 12 months (`PANW-IDLANDSCAPE-2026`). Agent identity is routed to ai-security.

Use cases by grade: A = 0, B = 0, C = 8, D = 6 (14 total). Grade C is used for three kinds of evidence that the vocabulary does not separate: vendor product documentation, a vendor claim about an independent test, and regulator-observed practice by unnamed institutions. Each entry says which.

## 2. Use cases

```yaml
- id: security-identity-access-01
  title: Injection-resistant liveness and presentation-attack detection in remote identity proofing
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types: [review-assurance, transaction-processing]
  pattern: document-to-decision
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Remote onboarding and account recovery depend on a selfie or video and an image of an identity document. Criminals use
    generative AI to create altered documents, photographs and videos, and can insert forged media into the capture channel,
    so a face comparison alone no longer shows that a live person is present (FINCEN-ALERT004-2024, "Creation and Use of
    Deepfake Fraudulent Identities"; NIST-SP80063A-4-2025, Sec. 3.14).
  solution: >-
    Layered capture controls: live document capture, passive or active presentation attack detection (PAD), checks that
    the camera is a genuine sensor (virtual camera, emulator or jailbreak detection), analysis of submitted media for
    manipulation, and in attended sessions random human-in-the-loop cues such as requested movements. The controls are
    tested against known attack artifacts and the false-negative rates documented (NIST-SP80063A-4-2025, Sec. 3.11 and 3.14).
  outcomes:
    - lever: risk
      description: >-
        Identy.io says its system was the only one of 18 vendors in the Active PAD evaluation of the DHS S&T 2025 Remote
        Identity Validation Rally (run at the Maryland Test Facility) to reach zero attack acceptance across all three
        attack classes and both operating systems.
      figure: "0% APCER"
      measures: >-
        Attack presentation classification error rate: the share of attack presentations accepted, by vendor press
        release, across three attack classes on Android and iOS. The DHS report itself was not reachable.
      provenance: vendor-published
      source_ref: IDENTY-RIVR-2026
    - lever: experience
      description: >-
        Same press release: genuine-user rejection on Android was low and iOS was about one percentage point above the 5%
        threshold the release cites.
      figure: "BPCER 3.4% on Android"
      measures: >-
        Bona fide presentation classification error rate: genuine captures wrongly rejected, per the vendor's release.
        The iOS figure is described only as 1 percentage point above 5%.
      provenance: vendor-published
      source_ref: IDENTY-RIVR-2026
    - lever: risk
      description: >-
        Research prototype: randomized gesture challenges separated real-time face-swap attacks from genuine sessions
        better than a static calibration segment. A hand-occlusion challenge against one tool scored below the static baseline.
      figure: "AUC 0.988 (mean over active-gesture windows) vs 0.878 (static segment)"
      measures: >-
        Session-level AUC for separating attack sessions from genuine ones in 108 live sessions with six subjects, 24
        impersonated identities and two face-swap tools injected through a virtual camera. Small lab sample; preprint.
      provenance: independent
      source_ref: ARXIV-2610.16417
  prerequisites:
    - "Presentation attack detection tested to ISO/IEC 30107-3 with an impostor attack presentation accept rate (IAPAR) below 0.07 for remote biometric collection (NIST-SP80063A-4-2025, Sec. 3.11)"
    - "Biometric performance tests conformant to ISO/IEC 19795-1 and 19795-10, including demographic testing, with results made public (NIST-SP80063A-4-2025, Sec. 3.11)"
    - "Technical controls that detect virtual cameras, emulators and jailbroken devices; device attestation or sensor authentication where feasible (NIST-SP80063A-4-2025, Sec. 3.14)"
    - "A documented list of AI/ML use disclosed to relying parties, plus a privacy risk assessment (NIST-SP80063-4-2025, Sec. 3.8)"
  risks_and_guardrails:
    - "NIST states that a biometric comparison on a captured sample does not stop injection attacks, and that live capture and PAD help but do not cover all cases (NIST-SP80063A-4-2025, Sec. 3.14)"
    - "Biometric verification must perform for each demographic group no more than 25% worse than for the overall population, using a fixed threshold (NIST-SP80063A-4-2025, Sec. 3.11, item 12)"
    - "A USENIX Security 2025 paper reports a presentation attack on an enterprise-grade near-infrared face authentication system using a display costing under USD 400; Microsoft's security response center confirmed the behaviour and a CVE was scheduled for June 2025 (USENIX-REDBLEED-2025, abstract)"
    - "Vendor figures come from a vendor press release about an independent test, not from the test report (IDENTY-RIVR-2026)"
  human_checkpoints:
    - "Algorithmic media analysis and automated decisions should be augmented by manual review to address detection errors (NIST-SP80063A-4-2025, Sec. 3.14, item 2)"
    - "In attended sessions proofing agents and trusted referees must be trained to spot manipulated media and must use random cues (NIST-SP80063A-4-2025, Sec. 3.14)"
  role_evolution: >-
    Proofing agents and trusted referees take on a media-forensics duty: they are required to be trained on signs such as high
    latency, synchronisation problems and inconsistent skin tone or resolution, and to issue unpredictable prompts
    (NIST-SP80063A-4-2025, Sec. 3.14).
  evidence_grade: C
  sources:
    - { ref: NIST-SP80063A-4-2025, title: "NIST SP 800-63A-4 Digital Identity Guidelines: Identity Proofing and Enrollment", publisher: NIST, type: standard-setter, url: "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63A-4.pdf", date: 2025-07, access: full, locator: "Sec. 3.11 (biometrics), Sec. 3.14 (injection prevention and forged media detection)" }
    - { ref: NIST-SP80063-4-2025, title: "NIST SP 800-63-4 Digital Identity Guidelines", publisher: NIST, type: standard-setter, url: "https://doi.org/10.6028/NIST.SP.800-63-4", date: 2025-07, access: full, locator: "Sec. 3.8 (AI and ML in identity systems)" }
    - { ref: FINCEN-ALERT004-2024, title: "FinCEN Alert on Fraud Schemes Involving Deepfake Media Targeting Financial Institutions (FIN-2024-Alert004)", publisher: FinCEN, type: regulator, url: "https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf", date: 2024-11-13, access: full, locator: "pp. 2-4, 'Creation and Use of Deepfake Fraudulent Identities' and 'Detecting and Mitigating Deepfake Identity Documents'" }
    - { ref: IDENTY-RIVR-2026, title: "Identy.io Achieves Zero Attack Acceptance in DHS RIVR Face Liveness Evaluation", publisher: Business Wire (Identy.io press release), type: vendor, url: "https://businesswire.com/news/home/20260318279525/en/Identy.io-Achieves-Zero-Attack-Acceptance-in-DHS-RIVR-Face-Liveness-Evaluation-Leads-Field-on-Speed-and-User-Satisfaction", date: 2026-03-18, access: full, locator: "headline and first three bullets" }
    - { ref: ARXIV-2610.16417, title: "Not All Challenges Are Equal: Evaluating Interactive Liveness Detection Against Real-Time Face Swaps", publisher: arXiv (Firc et al.), type: academic, url: "https://arxiv.org/abs/2610.16417", date: 2026-10-12, access: full, locator: "abstract" }
    - { ref: USENIX-REDBLEED-2025, title: "Red Bleed: A Pragmatic Near-Infrared Presentation Attack on Facial Biometric Authentication Systems", publisher: USENIX Security 2025, type: academic, url: "https://www.usenix.org/conference/usenixsecurity25/presentation/hu-bowen", date: 2025-08, access: full, locator: "abstract" }
  last_reviewed: 2026-10-17
  notes: >-
    DHS S&T ran an independent evaluation (RIVR 2025), but the DHS page was not reachable (404 on the guessed URL, 403 on
    others), so the only readable results are vendor releases. Search-only: Incode and IDRnD make similar claims about
    DHS testing, with differing vendor counts (18 versus 21), so treat counts as unverified. Search-only: Entrust's 2026
    Identity Fraud Report (released 2025-11-18, over 1 billion verifications) says deepfakes were about one in five
    biometric fraud attempts, deepfake selfies rose 58% in 2025 and injection attacks 40% year on year (ENTRUST-IDFRAUD-2026).
    A 2026 preprint on selfie-capture motion (CanSelfie, 30 participants) found accelerometer traces reject all stationary
    attack proxies, but false acceptance on its attack proxies was 32.0% to 43.8% in the best configurations reported;
    cross-device, cross-session and real injection attacks were not evaluated (ARXIV-2605.00218). It cites ETSI TS 119 461 and CEN/TS 18099 as the European requirements for injection
    attack detection; those standards were not opened.

- id: security-identity-access-02
  title: Forged-document and manipulated-media analysis with synthetic-identity screening at account opening
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types: [review-assurance, transaction-processing]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    FinCEN's analysis of Bank Secrecy Act data shows criminals using generative AI to alter or create identity documents
    and photographs, combining them with stolen or fake personal data into synthetic identities, and using the resulting
    accounts to receive and launder fraud proceeds (FINCEN-ALERT004-2024, pp. 3-4).
  solution: >-
    Automated checks of submitted documents and images (metadata, tamper and generation artifacts, MRZ and barcode
    consistency, document liveness, reverse-image lookup against galleries of generated faces) feed analysts who re-review
    account-opening files and escalate with enhanced due diligence and suspicious activity reports.
  outcomes:
    - lever: risk
      description: >-
        FinCEN says institutions often detect GenAI-altered documents by re-reviewing account-opening files and, when
        investigating a suspect image, reverse-image searches; it also notes more sophisticated tools such as metadata
        examination and deepfake-detection software. It publishes no detection rates.
      figure: none published
      measures: "Descriptive regulator observation of BSA reporting; no numerator or denominator"
      provenance: independent
      source_ref: FINCEN-ALERT004-2024
  prerequisites:
    - "Document false acceptance and false rejection rates of 0.1 or less for automated evidence validation, with live capture and document-liveness checks (NIST-SP80063A-4-2025, Sec. 3.13)"
    - "Image-analysis algorithms tested against available attack artifacts and genuine media, with the expected false-positive and false-negative rates documented and given to relying parties on request (NIST-SP80063A-4-2025, Sec. 3.14, item 2)"
    - "Periodic testing by independent entities (should) and public test results (shall) (NIST-SP80063A-4-2025, Sec. 3.13, items 5-6)"
    - "A death-records check and a mechanism to tell relying parties about suspected fraud (NIST-SP80063A-4-2025, Sec. 3.2)"
  risks_and_guardrails:
    - "FinCEN states that its red flags are not conclusive alone and that deepfake users may claim technical glitches to avoid live checks (FINCEN-ALERT004-2024, p. 4)"
    - "A USENIX Security 2025 paper builds cryptographically signed fake photos that fool both deepfake and image-recapture detectors, showing that detector-plus-signature stacks can be bypassed (USENIX-CHIMERA-2025, abstract)"
    - "A 2026 preprint by a detector vendor says in-the-wild evaluations report 45-50% AUC drops for open-source detectors; its own results are self-reported on public benchmarks (ARXIV-2607.13234, abstract)"
  human_checkpoints:
    - "Analysts re-review account-opening documents and conduct enhanced due diligence on accounts with other suspicious indicators (FINCEN-ALERT004-2024, p. 4)"
    - "Institutions file SARs citing the key term FIN-2024-DEEPFAKEFRAUD (FINCEN-ALERT004-2024, p. 1)"
  role_evolution: >-
    Onboarding and fraud analysts add a media-authenticity step to document review, and FinCEN asks them to tag
    suspected cases with a dedicated SAR key term so that typologies can be tracked (FINCEN-ALERT004-2024).
  evidence_grade: C
  sources:
    - { ref: FINCEN-ALERT004-2024, title: "FinCEN Alert on Fraud Schemes Involving Deepfake Media Targeting Financial Institutions", publisher: FinCEN, type: regulator, url: "https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf", date: 2024-11-13, access: full, locator: "pp. 1-4" }
    - { ref: NIST-SP80063A-4-2025, title: "NIST SP 800-63A-4 Identity Proofing and Enrollment", publisher: NIST, type: standard-setter, url: "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63A-4.pdf", date: 2025-07, access: full, locator: "Sec. 3.2, 3.13, 3.14" }
    - { ref: USENIX-CHIMERA-2025, title: "Chimera: Creating Digitally Signed Fake Photos by Fooling Image Recapture and Deepfake Detectors", publisher: USENIX Security 2025, type: academic, url: "https://www.usenix.org/conference/usenixsecurity25/presentation/park", date: 2025-08, access: full, locator: "abstract" }
    - { ref: ARXIV-2607.13234, title: "Continuously Evolving Deepfake Detection: An Architecture and Public-Benchmark Evaluation of a Dynamic Detection System", publisher: arXiv (Miyachi and Uys; BitMind), type: academic, url: "https://arxiv.org/abs/2607.13234", date: 2026-07-14, access: full, locator: "abstract" }
  last_reviewed: 2026-10-17
  notes: >-
    Graded C as the closest fit: this is regulator-observed practice by unnamed financial institutions, with no named
    deployment and no vendor claim. The preprint's own detector results are from a vendor and not independently verified.

- id: security-identity-access-03
  title: One-to-many biometric deduplication to find duplicate enrolments and fraud rings, with mandatory manual review
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types: [review-assurance, transaction-processing]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Fraudsters can enrol the same face under different names to build synthetic or duplicate identities. Searching an
    applicant's biometric against everyone already enrolled can flag the overlap, but false matches would wrongly block
    genuine applicants such as twins.
  solution: >-
    Identity providers run a 1:N search of the applicant's biometric against the enrolled gallery for resolution,
    deduplication or fraud detection, under a privacy risk assessment, and route hits to a person.
  outcomes:
    - lever: risk
      description: "none published"
      figure: none published
      measures: "n/a. NIST sets a permitted false positive identification rate for 1:N searches but no deployment result is public"
      provenance: independent
      source_ref: NIST-SP80063A-4-2025
  prerequisites:
    - "Privacy risk assessment before use of 1:N identification (NIST-SP80063A-4-2025, Sec. 3.11, item 9)"
    - "A false positive identification rate of 1:1,000 or better, shown in tests with a gallery of at least 90% of the current or intended operational size (NIST-SP80063A-4-2025, Sec. 3.11, items 9-10)"
  risks_and_guardrails:
    - "The CSP must not decline an enrolment on the strength of an automated 1:N result without manual review that confirms it is not a false positive, for example twins submitting photographs for different accounts (NIST-SP80063A-4-2025, Sec. 3.11, item 11)"
    - "Demographic performance of biometric verification must be within 25% of the overall population (NIST-SP80063A-4-2025, Sec. 3.11, item 12)"
  human_checkpoints:
    - "Manual review confirms every automated 1:N match before an enrolment is declined (NIST-SP80063A-4-2025, Sec. 3.11, item 11)"
  role_evolution: >-
    A manual-review queue for biometric matches becomes a required role; NIST does not describe the staffing.
  evidence_grade: D
  sources:
    - { ref: NIST-SP80063A-4-2025, title: "NIST SP 800-63A-4 Identity Proofing and Enrollment", publisher: NIST, type: standard-setter, url: "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63A-4.pdf", date: 2025-07, access: full, locator: "Sec. 3.11, items 9-12" }
  last_reviewed: 2026-10-17
  notes: >-
    Idea: the standard permits and constrains the practice, but no named deployment or measurement was found.

- id: security-identity-access-04
  title: Synthetic-voice and deepfake detection scoring on contact-centre and meeting channels
  archetype: security
  module: identity-access
  function: customer-service
  work_types: [review-assurance, client-interaction]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Voice biometrics and callback checks were not designed for AI-generated speech. NYDFS warns that deepfakes can mimic a
    person's voice or appearance to circumvent biometric verification, and advises avoiding SMS, voice or video as
    authentication channels against AI-manipulated content (NYDFS-AIGUIDE-2024, social engineering and access controls sections).
  solution: >-
    A detection service scores the probability that call or meeting audio is synthetic and shows the score to frontline staff
    and fraud analysts, who triage and escalate. A vendor describes the set-up for one unnamed bank across Zoom, Meet, NICE,
    Twilio and Five9.
  outcomes:
    - lever: risk
      description: >-
        Vendor case study for an unnamed tier-one bank: synthetic-voice calls that earlier controls had not flagged were
        found, and detection was delivered in real time to frontline reps. No false-positive or confirmation rate is given.
      figure: "about 960 synthetic voice calls detected; over 1.7M customer calls analysed in 2024; about 600 frontline reps"
      measures: >-
        Calls the vendor's tool scored as synthetic out of customer calls analysed in 2024 across US and LATAM operations;
        not independently confirmed; the bank is not named.
      provenance: vendor-published
      source_ref: REALDEFENDER-BANK-2025
    - lever: quality
      description: >-
        Independent benchmark: across 12 state-of-the-art deepfake-voice detectors the best performer's error rate was 13.50%
        and every other detector exceeded 20%; a multimodal LLM showed no detection ability.
      figure: "best EER 13.50%; others above 20%"
      measures: >-
        Equal error rate for 12 detectors on VoiceWukong (265,200 English and 148,200 Chinese deepfake samples, 38 variants
        across six manipulation types); the paper also ran a user study with more than 300 participants.
      provenance: independent
      source_ref: USENIX-VOICEWUKONG-2025
  prerequisites:
    - "Integration with the contact-centre or meeting platform so audio can be scored in real time (REALDEFENDER-BANK-2025)"
    - "A triage and escalation process for flagged calls (REALDEFENDER-BANK-2025, Key Results)"
    - "Callback or step-up verification that does not depend on voice, SMS or video (NYDFS-AIGUIDE-2024, access controls section)"
  risks_and_guardrails:
    - "Detectors face significant challenges in real-world conditions, with dramatically declining performance, according to the VoiceWukong authors (USENIX-VOICEWUKONG-2025, abstract)"
    - "A 2026 preprint finds voice clones trained on very small samples can bypass commercial speaker verification and that anti-spoofing detectors do not generalise across synthesis methods (ARXIV-2601.02914, abstract)"
    - "NYDFS suggests avoiding SMS, voice or video authentication in favour of factors deepfakes cannot impersonate, such as digital certificates and physical security keys (NYDFS-AIGUIDE-2024, access controls section)"
  human_checkpoints:
    - "Fraud analysts triage flagged calls; the bank created a new internal triage and escalation process (REALDEFENDER-BANK-2025, Key Results)"
  role_evolution: >-
    Frontline reps receive an authenticity signal during the call; the fraud team gains a triage queue for calls the older
    controls had not flagged (REALDEFENDER-BANK-2025).
  evidence_grade: C
  sources:
    - { ref: REALDEFENDER-BANK-2025, title: "How a Global Bank Defends Contact Centers Against Deepfake Threats with Reality Defender (page undated; date inferred from the 2024 data window)", publisher: Reality Defender, type: vendor, url: "https://www.realitydefender.com/case-studies/how-a-tier-one-bank-stopped-deepfaked-audio-with-reality-defender", date: 2025, access: full, locator: "Key Results" }
    - { ref: USENIX-VOICEWUKONG-2025, title: "VoiceWukong: Benchmarking Deepfake Voice Detection", publisher: USENIX Security 2025, type: academic, url: "https://www.usenix.org/conference/usenixsecurity25/presentation/yan-ziwei", date: 2025-08, access: full, locator: "abstract" }
    - { ref: ARXIV-2601.02914, title: "Vulnerabilities of Audio-Based Biometric Authentication Systems Against Deepfake Speech Synthesis", publisher: arXiv (Hong et al.), type: academic, url: "https://arxiv.org/abs/2601.02914", date: 2026-01-06, access: full, locator: "abstract" }
    - { ref: NYDFS-AIGUIDE-2024, title: "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks (Industry Letter)", publisher: NYDFS, type: regulator, url: "https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks", date: 2024-10-16, access: full, locator: "sections on AI-enabled social engineering and Access Controls" }
  last_reviewed: 2026-10-17
  notes: >-
    Graded C: the deployment is unnamed and the figures are vendor-published. The case study's publication date was not
    found; the year is inferred and flagged in Gaps. Search-only: a vendor-adjacent 2026 guide notes narrowband call audio
    can degrade detection; not used.

- id: security-identity-access-05
  title: Identity verification of the requester before service-desk password and MFA resets
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [transaction-processing, client-interaction]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Help desks decide under time pressure whether the caller is the employee. The joint CISA, FBI and international
    advisory on Scattered Spider describes actors posing as employees to persuade help-desk staff to reset passwords and
    transfer MFA to devices they control, and posing as IT staff to obtain one-time codes (CISA-AA23-320A-2025, social
    engineering sections). The advisory does not mention AI; the AI link here comes from NYDFS and a vendor.
  solution: >-
    A verification step inside the ticket: the agent presses a button, the requester completes an ID-and-selfie check, and
    the result appears in the incident before a reset is made. Nametag announced this integration with ServiceNow.
  outcomes:
    - lever: speed
      description: >-
        The vendor says end users complete verification in under 30 seconds using an ID and a selfie (or a selfie alone if
        returning). No fraud-reduction or error-rate figure is published.
      figure: "under 30 seconds"
      measures: "Vendor's stated end-user completion time; sample and conditions not stated"
      provenance: vendor-published
      source_ref: NAMETAG-SERVICENOW-2026
  prerequisites:
    - "A service-management tool the verification can plug into, and a policy that sensitive actions such as password and MFA resets wait for verification (NAMETAG-SERVICENOW-2026)"
    - "Account-recovery methods defined in advance: saved or issued recovery codes, recovery contacts or repeated identity proofing, with a notification to the subscriber after every recovery (NIST-SP80063B-4-2025, Sec. 4.2)"
  risks_and_guardrails:
    - "An ID-and-selfie check is itself exposed to deepfakes and injected media; the same controls as remote identity proofing apply (NIST-SP80063A-4-2025, Sec. 3.14)"
    - "CISA recommends FIDO/WebAuthn or PKI-based MFA, which resists push bombing and SIM swap, rather than relying on help-desk judgement alone (CISA-AA23-320A-2025, Mitigations)"
    - "NYDFS advises training that covers verifying a requester's identity for unusual requests and says when human review must be part of verification (NYDFS-AIGUIDE-2024, training section)"
  human_checkpoints:
    - "The help-desk agent initiates the verification and decides whether to proceed once the result is shown (NAMETAG-SERVICENOW-2026)"
  role_evolution: >-
    Help-desk agents stop acting as ad hoc interrogators; the vendor says they should not need to question callers or run
    video calls (NAMETAG-SERVICENOW-2026). NYDFS wants staff trained to challenge unusual requests (NYDFS-AIGUIDE-2024).
  evidence_grade: C
  sources:
    - { ref: NAMETAG-SERVICENOW-2026, title: "Prevent Deepfake Impersonation at the ServiceNow IT Service Desk with Nametag Identity Verification (page undated, retrieved 2026-10-17)", publisher: Nametag, type: vendor, url: "https://getnametag.com/newsroom/servicenow-identity-verification", date: 2026-10-17, access: full, locator: "body and customer quote (ElevateBio)" }
    - { ref: CISA-AA23-320A-2025, title: "Scattered Spider (joint advisory AA23-320A, updated 2025-07-29)", publisher: CISA with FBI and international partners, type: regulator, url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a", date: 2025-07-29, access: full, locator: "Summary, social engineering lists, Mitigations" }
    - { ref: NIST-SP80063B-4-2025, title: "NIST SP 800-63B-4 Authentication and Authenticator Management", publisher: NIST, type: standard-setter, url: "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63B-4.pdf", date: 2025-07, access: full, locator: "Sec. 4.2 (account recovery)" }
    - { ref: NYDFS-AIGUIDE-2024, title: "Cybersecurity Risks Arising from AI and Strategies to Combat Related Risks", publisher: NYDFS, type: regulator, url: "https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks", date: 2024-10-16, access: full, locator: "Training section" }
  last_reviewed: 2026-10-17
  notes: >-
    The vendor release quotes an ElevateBio security director but does not say how long it has been in use, so maturity is
    announced. Search-only: Ping Identity, Pindrop and an NHI Management Group FAQ recommend tiered resets and separate
    verification paths for high-risk actions; no organization with measured results was found.

- id: security-identity-access-06
  title: Machine-learning risk scoring of sign-ins, users and tokens to drive step-up or block
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Federal and industry guidance says adversaries increasingly target the identity tokens and assertions behind SSO,
    federation and API access to move laterally (CISA-IR8587-2026). In a vendor survey 85% of respondents agree that
    fragmented identity tools delay detection and response, and 97% say fragmentation adds time per incident, averaging 12
    hours (PANW-IDLANDSCAPE-2026, Chapter 2).
  solution: >-
    Identity platforms compute sign-in and user risk from detections such as anomalous tokens, atypical travel, anonymous
    or malicious IP addresses and suspicious MFA approvals, some in real time and some offline, and feed policy that can
    require step-up or block (MSFT-ENTRAIDP-2026, risk detection tables).
  outcomes:
    - lever: speed
      description: >-
        Baseline, not an AI effect: respondents who say tool fragmentation adds time to identity-related incidents report an
        average of 12 hours per incident.
      figure: "12 hours per incident"
      measures: >-
        Average added time per identity-related incident among the 97% of 2,930 respondents who report that tool
        fragmentation adds time; vendor-commissioned survey fielded March-April 2026.
      provenance: vendor-published
      source_ref: PANW-IDLANDSCAPE-2026
    - lever: risk
      description: "No detection accuracy, false-positive or analyst-override figure is published for the risk detections."
      figure: none published
      measures: "n/a. Product documentation lists detections and whether each is real-time or offline"
      provenance: vendor-published
      source_ref: MSFT-ENTRAIDP-2026
  prerequisites:
    - "A tier of the identity platform that includes the premium detections; the free tier shows only a generic 'additional risk detected' entry (MSFT-ENTRAIDP-2026)"
    - "Token issuance, validation and lifecycle controls aligned with the CISA and NIST token-protection report (CISA-IR8587-2026)"
    - "Response actions that can revoke tokens, terminate sessions and reduce privilege, not only reset passwords"
  risks_and_guardrails:
    - "In the survey only 45% of organizations include forced MFA step-up, 41% token or key revocation and 36% termination of privileged sessions among their incident-response actions; 51% include password reset (PANW-IDLANDSCAPE-2026, Figure 5)"
    - "Push-based MFA is exposed to fatigue attacks and SIM swap; CISA advises FIDO/WebAuthn or PKI-based MFA (CISA-AA23-320A-2025, Mitigations)"
  human_checkpoints:
    - "An administrator can confirm a user as compromised, which is itself a detection input (MSFT-ENTRAIDP-2026, risk detection table)"
  role_evolution: >-
    Identity administrators and responders work from a shared risk view instead of correlating across consoles; the survey
    ties slow response to console fragmentation (PANW-IDLANDSCAPE-2026, Chapter 2).
  evidence_grade: C
  sources:
    - { ref: MSFT-ENTRAIDP-2026, title: "What are risk detections? Microsoft Entra ID Protection (page undated, retrieved 2026-10-17)", publisher: Microsoft Learn, type: vendor, url: "https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks", date: 2026-10-17, access: full, locator: "risk detection tables" }
    - { ref: CISA-IR8587-2026, title: "CISA and NIST Release Guidelines to Protect Federal Cloud Identity Systems from Token Theft, Forgery, and Misuse (announcing NIST IR 8587)", publisher: CISA, type: regulator, url: "https://www.cisa.gov/news-events/news/cisa-and-nist-release-guidelines-protect-federal-cloud-identity-systems-token-theft-forgery-and", date: 2026-09-15, access: full, locator: "body of press release" }
    - { ref: PANW-IDLANDSCAPE-2026, title: "2026 Identity Security Landscape (Palo Alto Networks, research by Vanson Bourne)", publisher: Palo Alto Networks, type: survey, url: "https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/2026-identity-security-landscape-report.pdf", date: 2026-06, access: full, locator: "Chapter 2, pp. 12-14, Figure 5" }
    - { ref: CISA-AA23-320A-2025, title: "Scattered Spider (AA23-320A)", publisher: CISA with FBI and international partners, type: regulator, url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a", date: 2025-07-29, access: full, locator: "Mitigations" }
  last_reviewed: 2026-10-17
  notes: >-
    NIST IR 8587 is final (published 2026-09-15 per its NIST page); only the CISA press release and the abstract header
    were read, and neither describes AI, so the link to ML detection is the product documentation. Search-only: secondary
    summaries of Microsoft's Digital Defense Report 2025 say over 97% of identity attacks are password spray or brute
    force and that token theft, adversary-in-the-middle and similar techniques are under 3% (MSFT-DDR-2025). The Verizon
    2026 DBIR landing page says 31% of breaches start with software vulnerabilities, ahead of stolen passwords as the top
    entry route (VERIZON-DBIR-2026; report body not read).

- id: security-identity-access-07
  title: Continuous and behavioural authentication as a second factor
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [transaction-processing]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    One-time logins leave sessions exposed after a device or token is taken; deepfakes defeat single-moment biometric checks.
  solution: >-
    Keep verifying the user during a session with signals such as keystroke and navigation patterns or wearable sensor data.
    NYDFS lists a fingerprint combined with keystrokes and navigation patterns as one option, and the EU NIS2 implementing
    regulation accepts continuous authentication mechanisms as an alternative to multiple factors.
  outcomes:
    - lever: risk
      description: "none published"
      figure: none published
      measures: "n/a. A research prototype is described in notes"
      provenance: independent
      source_ref: NDSS-PPG-2026
  prerequisites:
    - "Strength of authentication appropriate to the classification of the asset to be accessed (NIS2-IMPL-2024, point 11.7.2)"
    - "Liveness detection or texture analysis where fingerprints or other biometrics are used (NYDFS-AIGUIDE-2024, Access Controls)"
  risks_and_guardrails:
    - "The EU AI Act prohibits AI systems that infer emotions of a person in the workplace, with medical and safety exceptions, so behavioural analytics must not drift into emotion inference (EU-AIACT-2024, Art. 5(1)(f))"
    - "NYDFS warns that stolen biometric data can be used to imitate users, bypass MFA and generate realistic deepfakes (NYDFS-AIGUIDE-2024, biometric data paragraph)"
  human_checkpoints:
    - "No human checkpoint is described in the sources; fallback to another factor is the usual design for failed biometric checks (NIST-SP80063B-4-2025, Sec. 3.2.3)"
  role_evolution: >-
    Not described in the sources.
  evidence_grade: D
  sources:
    - { ref: NIS2-IMPL-2024, title: "Commission Implementing Regulation (EU) 2024/2690 (technical and methodological requirements under NIS2)", publisher: European Commission, type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2690", date: 2024-10-18, access: full, locator: "Annex, point 11.7" }
    - { ref: NYDFS-AIGUIDE-2024, title: "Cybersecurity Risks Arising from AI and Strategies to Combat Related Risks", publisher: NYDFS, type: regulator, url: "https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks", date: 2024-10-16, access: full, locator: "Access Controls" }
    - { ref: NDSS-PPG-2026, title: "Know Me by My Pulse: Toward Practical Continuous Authentication on Wearable Devices via Wrist-Worn PPG", publisher: NDSS Symposium 2026, type: academic, url: "https://www.ndss-symposium.org/ndss-paper/know-me-by-my-pulse-toward-practical-continuous-authentication-on-wearable-devices-via-wrist-worn-ppg/", date: 2026-02, access: full, locator: "abstract" }
    - { ref: EU-AIACT-2024, title: "Regulation (EU) 2024/1689 (Artificial Intelligence Act)", publisher: European Parliament and Council, type: regulator, url: "https://eur-lex.europa.eu/eli/reg/2024/1689/oj", date: 2024-07-12, access: full, locator: "Art. 5(1)(f)" }
  last_reviewed: 2026-10-17
  notes: >-
    Idea. The NDSS 2026 smartwatch study (26 subjects in the authors' dataset) reports average accuracy 88.11%, false
    acceptance 0.48%, false rejection 11.77% and equal error rate 2.76%, and that models trained on resting data fail
    under motion. These are research results, not deployment results.

- id: security-identity-access-08
  title: Reviewer decision support in access reviews and certifications
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Regulators set review frequencies that produce a lot of reviewer work: DORA's technical standard requires access
    rights to be updated at least once a year, and at least every six months for systems supporting critical or important
    functions (DORA-RTS-2024, Art. 21(e)(iv)); NYDFS requires at least annual review (NYDFS-AIGUIDE-2024, Access Controls);
    the NIS2 implementing regulation requires reviews at planned intervals with documented results (NIS2-IMPL-2024, point
    11.2.3). Survey respondents describe stale standing access, such as credentials active years after a project ended
    (PANW-IDLANDSCAPE-2026, p. 15).
  solution: >-
    The review tool pre-fills a recommended action. Microsoft's decision helpers recommend Deny for users with no sign-in in
    30 days, and a machine-learning recommendation flags group members who sit far from other members in the reporting
    structure. Reviewers still decide.
  outcomes:
    - lever: quality
      description: >-
        Microsoft says the machine-learning recommendation opens the way to automating access reviews and reduces
        attestation fatigue. No accuracy, agreement or override rate is published.
      figure: none published
      measures: "n/a. Product documentation; the fatigue claim is a vendor statement"
      provenance: vendor-published
      source_ref: MSFT-ENTRA-ACCESSREV-2026
  prerequisites:
    - "Manager attribute and an organizational hierarchy for the affiliation recommendation; groups above 600 users are not supported (MSFT-ENTRA-ACCESSREV-2026)"
    - "An ID Governance licence for the user-to-group affiliation recommendation (MSFT-ENTRA-ACCESSREV-2026)"
    - "A register of access rights granted and logging of access-rights management (NIS2-IMPL-2024, point 11.2.2)"
  risks_and_guardrails:
    - "The inactivity recommendation is computed when the review starts and is not updated while it is in progress (MSFT-ENTRA-ACCESSREV-2026)"
    - "Reporting-structure distance can mark legitimate cross-division members as low affiliation; the documentation's own example shows a Deny recommendation for a member from another division (MSFT-ENTRA-ACCESSREV-2026)"
    - "Search-only: a July 2026 analyst summary says AI in access administration works only when recommendations are explainable, deterministic and auditable, with final approval anchored in explicit rules (NHIMG-NEXIS-2026)"
  human_checkpoints:
    - "Reviewers choose whether to follow each recommendation (MSFT-ENTRA-ACCESSREV-2026)"
  role_evolution: >-
    Reviewers move from reading every entitlement to confirming flagged ones. A search-only commentary argues reviewer
    attention should be ranked by anomaly rather than bulk-approved (NHIMG-NEXIS-2026).
  evidence_grade: C
  sources:
    - { ref: MSFT-ENTRA-ACCESSREV-2026, title: "Review recommendations for access reviews, Microsoft Entra ID Governance (page undated, retrieved 2026-10-17)", publisher: Microsoft Learn, type: vendor, url: "https://learn.microsoft.com/en-us/entra/id-governance/review-recommendations-access-reviews", date: 2026-10-17, access: full, locator: "inactive-user and User-to-Group Affiliation sections" }
    - { ref: DORA-RTS-2024, title: "Commission Delegated Regulation (EU) 2024/1774 (ICT risk management framework RTS under DORA)", publisher: European Commission, type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1774", date: 2024-06-25, access: full, locator: "Art. 20 and 21" }
    - { ref: NIS2-IMPL-2024, title: "Commission Implementing Regulation (EU) 2024/2690", publisher: European Commission, type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2690", date: 2024-10-18, access: full, locator: "Annex, points 11.2 and 11.3.3" }
    - { ref: NYDFS-AIGUIDE-2024, title: "Cybersecurity Risks Arising from AI and Strategies to Combat Related Risks", publisher: NYDFS, type: regulator, url: "https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks", date: 2024-10-16, access: full, locator: "Access Controls" }
    - { ref: PANW-IDLANDSCAPE-2026, title: "2026 Identity Security Landscape", publisher: Palo Alto Networks, type: survey, url: "https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/2026-identity-security-landscape-report.pdf", date: 2026-06, access: full, locator: "'The Ghosts of Access Past', p. 15" }
    - { ref: NHIMG-NEXIS-2026, title: "Explainability Is the Deciding Factor in AI Access Administration (NHI Management Group, citing Nexis and Gartner)", publisher: NHI Management Group, type: community, url: "https://nhimg.org/articles/explainability-is-the-deciding-factor-in-ai-access-administration/", date: 2026-07-28, access: search-only, locator: "search snippet" }
  last_reviewed: 2026-10-17
  notes: >-
    Search-only figures, not used as outcomes: SailPoint's 2026-04-29 infographic says 44% of security leaders are burdened
    by manual tasks and 30% cite reviewer fatigue leading to rubber-stamping (SAILPOINT-INFOGRAPHIC-2026; no
    methodology found); a Pathlock summary of Gartner's 2026 IGA Market Guide says IGA is moving from quarterly manual
    reviews to continuous, outcome-driven processes (PATHLOCK-GARTNER-IGA-2026). No study of override rates or of whether
    recommendations reduce rubber-stamping was found.

- id: security-identity-access-09
  title: Machine-learning entitlement right-sizing recommendations
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [software-systems, review-assurance]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Least privilege is mandated but hard to maintain. DORA's technical standard requires access rights based on
    need-to-know, need-to-use and least privilege (DORA-RTS-2024, Art. 21(a)); 56% of survey respondents say they cannot
    effectively enforce continuous least privilege for service accounts across cloud, SaaS and on-premises environments
    (PANW-IDLANDSCAPE-2026, p. 15).
  solution: >-
    Google's IAM recommender examines up to 90 days of permission usage and recommends removing or replacing roles that
    grant excess permissions; a machine-learning model also tries to identify permissions a principal is likely to need
    even if not recently used, using co-occurrence patterns and word embeddings.
  outcomes:
    - lever: risk
      description: "No reduction in excess permissions, accuracy or false-removal rate is published in the documentation."
      figure: none published
      measures: "n/a. Product documentation"
      provenance: vendor-published
      source_ref: GOOGLE-IAMREC-2026
  prerequisites:
    - "A minimum observation period, 90 days by default (30 or 60 days configurable for project-level recommendations) (GOOGLE-IAMREC-2026)"
    - "Usage data for the principals, with PII dropped and k-anonymity applied in the model pipeline (GOOGLE-IAMREC-2026)"
  risks_and_guardrails:
    - "Recommendations rest on observed use within the window, so rarely used but needed permissions are the risk; the ML component exists to reduce that (GOOGLE-IAMREC-2026)"
    - "Automated lifecycle management is only expected 'where feasible and appropriate' under DORA (DORA-RTS-2024, Art. 20)"
  human_checkpoints:
    - "Recommendations suggest removal or replacement; applying them is a separate step (GOOGLE-IAMREC-2026)"
  role_evolution: >-
    Platform and IAM teams move from writing roles by hand to approving or rejecting recommended changes at scale
    (GOOGLE-IAMREC-2026, overview).
  evidence_grade: C
  sources:
    - { ref: GOOGLE-IAMREC-2026, title: "Overview of role recommendations, Google Cloud Policy Intelligence (page undated, retrieved 2026-10-17)", publisher: Google Cloud, type: vendor, url: "https://cloud.google.com/policy-intelligence/docs/role-recommendations-overview", date: 2026-10-17, access: full, locator: "overview and 'Machine learning for policy insights'" }
    - { ref: DORA-RTS-2024, title: "Commission Delegated Regulation (EU) 2024/1774", publisher: European Commission, type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1774", date: 2024-06-25, access: full, locator: "Art. 20 and 21(a)" }
    - { ref: PANW-IDLANDSCAPE-2026, title: "2026 Identity Security Landscape", publisher: Palo Alto Networks, type: survey, url: "https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/2026-identity-security-landscape-report.pdf", date: 2026-06, access: full, locator: "p. 15" }
  last_reviewed: 2026-10-17
  notes: >-
    Product documentation only. No customer, deployment or measured result was found for any cloud entitlement-recommendation tool.

- id: security-identity-access-10
  title: Just-in-time and zero-standing-privilege access with automated governance for privileged accounts
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [software-systems, review-assurance]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Regulators require privileged, emergency and administrator access to be granted on a need-to-use or ad hoc basis, with
    strong authentication (DORA-RTS-2024, Art. 21(e)(ii) and (f)(ii)); the NIS2 implementing regulation
    requires individualised, restricted administration privileges and reviews at planned intervals (NIS2-IMPL-2024, point
    11.3). Only 36% of survey respondents include terminating active privileged sessions in incident-response procedures
    and 40% include removing admin rights (PANW-IDLANDSCAPE-2026, Figure 5).
  solution: >-
    Replace permanent admin rights with just-in-time grants, with zero standing privilege, and automate governance across the
    identity lifecycle. Palo Alto Networks describes its Idira platform on these lines.
  outcomes:
    - lever: risk
      description: "No outcome is published for the platform; the survey figures are baseline practice, not results."
      figure: none published
      measures: "n/a. Vendor product description in the back matter of a vendor survey"
      provenance: vendor-published
      source_ref: PANW-IDLANDSCAPE-2026
  prerequisites:
    - "Separate administration accounts used only for administration (NIS2-IMPL-2024, point 11.3.2)"
    - "Logging of privileged and emergency access, which the DORA simplified framework requires (DORA-RTS-2024, Art. 33)"
  risks_and_guardrails:
    - "56% say they cannot enforce continuous least privilege for service accounts (PANW-IDLANDSCAPE-2026, p. 15), so just-in-time cover may be partial"
  human_checkpoints:
    - "Approval of elevation requests is not described in the sources; DORA requires ad hoc assignment (DORA-RTS-2024, Art. 21(e)(ii))"
  role_evolution: >-
    Not described beyond the product pitch.
  evidence_grade: C
  sources:
    - { ref: PANW-IDLANDSCAPE-2026, title: "2026 Identity Security Landscape", publisher: Palo Alto Networks, type: survey, url: "https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/2026-identity-security-landscape-report.pdf", date: 2026-06, access: full, locator: "Figure 5 (p. 14); 'Introducing Palo Alto Networks Idira' (p. 28)" }
    - { ref: DORA-RTS-2024, title: "Commission Delegated Regulation (EU) 2024/1774", publisher: European Commission, type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1774", date: 2024-06-25, access: full, locator: "Art. 21" }
    - { ref: NIS2-IMPL-2024, title: "Commission Implementing Regulation (EU) 2024/2690", publisher: European Commission, type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2690", date: 2024-10-18, access: full, locator: "Annex, point 11.3" }
  last_reviewed: 2026-10-17
  notes: >-
    The product description is marketing text at the end of a vendor survey. The landscape file dates Idira to 2026-05-12
    (PANW-PRESS-2026, not re-opened here).

- id: security-identity-access-11
  title: LLM triage of identity telemetry for compromised-account and insider cases
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [research-synthesis, review-assurance]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Identity telemetry is noisy and insider cases often hide in subtle behaviours across several data surfaces. Public
    training data is small, synthetic data lacks realism, and enterprise data is sensitive (NDSS-CHIMERA-INSIDER-2026, abstract).
  solution: >-
    Language models read identity and activity records, decide which are worth investigating and give a verdict. Researchers
    generate synthetic insider-threat data with multi-agent LLM simulation and benchmark models on it.
  outcomes:
    - lever: quality
      description: >-
        On a synthetic benchmark, eight models reached identical triage F1 yet split between verdict F1 of 1.0 and 0.80;
        models at the same verdict accuracy differed by two orders of magnitude in triage noise.
      figure: "triage F1 0.80 for eight models; verdict F1 1.0 vs 0.80"
      measures: >-
        OrgForge-IT synthetic corpus: 51 simulated days, 2,904 telemetry records at a 96.4% noise rate, four detection
        scenarios, a ten-model leaderboard. Synthetic data; single-author preprint.
      provenance: independent
      source_ref: ARXIV-2603.22499
  prerequisites:
    - "Records from several surfaces (identity, email, endpoint) so that single-surface rules are not the only triage path (ARXIV-2603.22499, abstract)"
  risks_and_guardrails:
    - "In the vishing scenario, lower-tier models detected the attack but misclassified the victim; the benchmark found that rigid multi-signal thresholds exclude single-surface negligent insiders (ARXIV-2603.22499, abstract)"
    - "Baseline false-positive rate must be reported next to verdict F1 (ARXIV-2603.22499, abstract)"
  human_checkpoints:
    - "Not described; the benchmark scores model output without an analyst loop"
  role_evolution: >-
    Not described in the sources.
  evidence_grade: D
  sources:
    - { ref: ARXIV-2603.22499, title: "OrgForge-IT: A Verifiable Synthetic Benchmark for LLM-Based Insider Threat Detection", publisher: arXiv (Flynt), type: academic, url: "https://arxiv.org/abs/2603.22499", date: 2026-03-23, access: full, locator: "abstract" }
    - { ref: NDSS-CHIMERA-INSIDER-2026, title: "Chimera: Harnessing Multi-Agent LLMs for Automatic Insider Threat Simulation", publisher: NDSS Symposium 2026, type: academic, url: "https://www.ndss-symposium.org/ndss-paper/chimera-harnessing-multi-agent-llms-for-automatic-insider-threat-simulation/", date: 2026-02, access: full, locator: "abstract (first paragraph read)" }
  last_reviewed: 2026-10-17
  notes: >-
    Idea: researchers discuss and benchmark it; no deployment found. The measured figures are lab results on synthetic data,
    so outcomes are not claimed. Overlaps with security-operations triage patterns.

- id: security-identity-access-12
  title: Learned password-guessing models used to audit password strength and screen choices
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Password policy is judged by how well guessing attacks do. Attackers now have LLM-based guessers; defenders and
    password-feedback tools need to know how strong a password is against them.
  solution: >-
    Use LLM-based guessing frameworks as the benchmark when auditing password strength, and test whether general LLMs can
    estimate strength and give feedback. Pattern: other (offline audit of credential strength against a learned attacker model).
  outcomes:
    - lever: risk
      description: "none published"
      figure: none published
      measures: "n/a. Research results are described in notes"
      provenance: independent
      source_ref: USENIX-PASSLLM-2025
  prerequisites:
    - "A password blocklist of commonly used, expected or compromised values checked against the entire password (NIST-SP80063B-4-2025, Sec. 3.1.1.2)"
  risks_and_guardrails:
    - "The audit tooling is the same capability an attacker uses; handling and access to such tools must be controlled"
  human_checkpoints:
    - "Not described in the sources"
  role_evolution: >-
    Not described in the sources.
  evidence_grade: D
  sources:
    - { ref: USENIX-PASSLLM-2025, title: "Password Guessing Using Large Language Models", publisher: USENIX Security 2025, type: academic, url: "https://www.usenix.org/conference/usenixsecurity25/presentation/zou-yunkai", date: 2025-08, access: full, locator: "abstract" }
    - { ref: IEEESP-2026, title: "IEEE Symposium on Security and Privacy 2026 program (lists 'Can Foundation LLMs Accurately Estimate Password Strength and Provide Appropriate Password Feedback?'; title only)", publisher: IEEE, type: academic, url: "https://sp2026.ieee-security.org/program.html", date: 2026-05, access: full, locator: "Track 3: Passwords" }
    - { ref: NIST-SP80063B-4-2025, title: "NIST SP 800-63B-4 Authentication and Authenticator Management", publisher: NIST, type: standard-setter, url: "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63B-4.pdf", date: 2025-07, access: full, locator: "Sec. 3.1.1.2" }
  last_reviewed: 2026-10-17
  notes: >-
    Idea. PassLLM reports higher guessing success than its closest prior method on 11 real-world password datasets (2.87%-17.07%
    higher for broad guessing; 12.54%-31.63% of common users guessed within 100 guesses when personal information is known).
    The abstract is attacker-side; defensive use is the stated purpose of password-strength evaluation. The IEEE S&P paper
    was seen by title only.

- id: security-identity-access-13
  title: Customer account-takeover and impersonation-scam detection with payment friction
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types: [transaction-processing, review-assurance]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    FBI IC3 received about 4,700 account-takeover complaints with USD 359.7 million in losses in 2025, and notes that its
    recovery asset team saw a rise in tech-support and ATO cases, where an ATO case can involve 50 or more simultaneous
    ACH transactions to different recipient accounts (FBI-IC3-2025). The EU deal on payment services would require a
    provider to refund customers defrauded by someone posing as its staff, if they report to the police and inform the provider (EP-PSR-2025).
  solution: >-
    Banks and payment providers combine strong customer authentication, payee-name matching, spending limits, risk
    assessment and analytics to hold or block suspicious payments and freeze receiving accounts. The EU deal sets many of
    these as obligations. Where machine learning scores account behaviour is not described in the regulator sources.
  outcomes:
    - lever: risk
      description: "No effectiveness figure for AI-based ATO detection is published in the regulator sources."
      figure: none published
      measures: "n/a. IC3 counts loss and complaints, not detector performance"
      provenance: independent
      source_ref: FBI-IC3-2025
  prerequisites:
    - "Strong customer authentication and a fraud-risk assessment (EP-PSR-2025)"
    - "Ability to freeze a suspicious transaction at the receiving provider (EP-PSR-2025)"
  risks_and_guardrails:
    - "If a provider fails to implement appropriate fraud prevention, it is liable for the customer's losses; for impersonation of its own staff it must refund the full amount if the customer reports to the police and informs it (EP-PSR-2025)"
    - "The deal still needs formal adoption by Parliament and Council (EP-PSR-2025, Next steps); a search-only source reports the scope was narrowed to impersonation of the provider or its staff (not confirmed against final text)"
  human_checkpoints:
    - "Users must have access to human customer support, not only chatbots (EP-PSR-2025)"
  role_evolution: >-
    Fraud operations absorb refund liability and receiving-side freeze duties; the regulator text does not describe staffing.
  evidence_grade: D
  sources:
    - { ref: FBI-IC3-2025, title: "2025 Internet Crime Report", publisher: FBI Internet Crime Complaint Center, type: regulator, url: "https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf", date: 2026-04, access: full, locator: "Cyber-Enabled Fraud in 2025 (ATO box, PDF p. 12); IC3 Recovery Asset Team (PDF p. 17)" }
    - { ref: EP-PSR-2025, title: "Payment services deal: More protection from online fraud and hidden fees", publisher: European Parliament, type: regulator, url: "https://www.europarl.europa.eu/news/en/press-room/20251121IPR31540/payment-services-deal-more-protection-from-online-fraud-and-hidden-fees", date: 2025-11, access: full, locator: "'Protecting customers from fraud' and 'Next steps'" }
    - { ref: FINTECHGLOBAL-ATO-2026, title: "Account takeover fraud exposes gaps beyond authentication", publisher: Fintech Global, type: press, url: "https://fintech.global/2026/09/18/account-takeover-fraud-exposes-gaps-beyond-authentication/", date: 2026-09-18, access: search-only, locator: "search snippet" }
  last_reviewed: 2026-10-17
  notes: >-
    Idea: ML-based ATO detection is widely discussed, but no named bank with a measured result was found (one search). The
    EP press release date is taken as 2025-11 from the provisional agreement of 27 November 2025 reported by secondary
    sources; the page itself shows no date.

- id: security-identity-access-14
  title: Continuous collection of access-control evidence for regulatory reviews
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Several regimes require documented, periodic proof of who has access: DORA (reviews at least annually, six-monthly for
    critical or important functions), the NIS2 implementing regulation (a register of access rights and documented review
    results), and NYDFS (annual review of access privileges) (DORA-RTS-2024, Art. 21; NIS2-IMPL-2024, points 11.2.2-11.2.3;
    NYDFS-AIGUIDE-2024).
  solution: >-
    Instead of point-in-time sampling, an automated process tests the full population of accounts and entitlements against
    policy (inactive accounts, shared accounts, privileged access, reviews overdue) and records the result as evidence.
  outcomes:
    - lever: quality
      description: "none published"
      figure: none published
      measures: "n/a"
      provenance: vendor-published
      source_ref: PATHLOCK-GARTNER-IGA-2026
  prerequisites:
    - "A register of access rights granted and logging of access-rights management (NIS2-IMPL-2024, point 11.2.2)"
    - "Documented review results including changes made (NIS2-IMPL-2024, point 11.2.3)"
  risks_and_guardrails:
    - "Under NIS2 and DORA the legal duty to review stays with the entity; automating evidence does not move accountability (NIS2-IMPL-2024, Art. 2; DORA-RTS-2024, Art. 21)"
  human_checkpoints:
    - "Not described; reviews are the entity's responsibility under the regulations"
  role_evolution: >-
    Not described in the sources.
  evidence_grade: D
  sources:
    - { ref: PATHLOCK-GARTNER-IGA-2026, title: "2026 Gartner IGA Market Guide: top findings (Pathlock summary)", publisher: Pathlock, type: vendor, url: "https://pathlock.com/blog/2026-gartner-iga-market-guide-top-findings/", date: 2026, access: search-only, locator: "search snippet" }
    - { ref: DORA-RTS-2024, title: "Commission Delegated Regulation (EU) 2024/1774", publisher: European Commission, type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1774", date: 2024-06-25, access: full, locator: "Art. 21" }
    - { ref: NIS2-IMPL-2024, title: "Commission Implementing Regulation (EU) 2024/2690", publisher: European Commission, type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2690", date: 2024-10-18, access: full, locator: "Annex, points 11.2.2-11.2.3" }
    - { ref: NYDFS-AIGUIDE-2024, title: "Cybersecurity Risks Arising from AI and Strategies to Combat Related Risks", publisher: NYDFS, type: regulator, url: "https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks", date: 2024-10-16, access: full, locator: "Access Controls" }
  last_reviewed: 2026-10-17
  notes: >-
    Idea: the direction (continuous rather than quarterly review) is attributed to Gartner by a vendor summary seen only in
    search; the Gartner guide is paywalled. No organization using AI to produce regulator-facing IAM evidence was found.
```

## 3. Module notes

**Processes and key steps (with work types)**
- Identity proofing and enrolment: capture ID and selfie, validate evidence, detect liveness and injection, deduplicate, decide (review-assurance, transaction-processing). Sources: `NIST-SP80063A-4-2025`.
- Authentication and credential management: issue passkeys or other authenticators, set password rules, handle biometrics (software-systems). Sources: `NIST-SP80063B-4-2025`, `USENIX-PASSKEYS-2026`.
- Account recovery and service-desk resets: verify the requester, reset, re-bind MFA (transaction-processing, client-interaction). Sources: `CISA-AA23-320A-2025`, `NIST-SP80063B-4-2025` (Sec. 4.2).
- Joiner, mover, leaver and provisioning: grant, change and revoke access; deactivate unneeded identities (transaction-processing). Sources: `DORA-RTS-2024` Art. 20-21, `NIS2-IMPL-2024` point 11.5.
- Access reviews, segregation of duties and recertification (review-assurance). Sources: `DORA-RTS-2024`, `NYDFS-AIGUIDE-2024`.
- Privileged access: just-in-time grants, session control, separate admin accounts (software-systems). Sources: `NIS2-IMPL-2024` point 11.3.
- Identity threat detection and response: risk scoring, token and session abuse, containment (data-reporting, coordination). Sources: `CISA-IR8587-2026`, `MSFT-ENTRAIDP-2026`.
- Identity-related fraud: synthetic identities, account takeover, impersonation (review-assurance, transaction-processing). Sources: `FINCEN-ALERT004-2024`, `FBI-IC3-2025`.

**Common pain points**
- Fragmented tools: 85% of survey respondents say fragmented identity systems delay detection and response; 97% say fragmentation adds time, averaging 12 hours per incident (`PANW-IDLANDSCAPE-2026`, Chapter 2; vendor survey, n=2,930).
- Stale standing access: respondents cite credentials active for years after projects end, permissions that persist after role changes, and legacy permissions from sister companies (`PANW-IDLANDSCAPE-2026`, p. 15).
- Response relies on basic actions: 51% include password reset but only 41% revoke tokens or keys and 36% terminate privileged sessions (`PANW-IDLANDSCAPE-2026`, Figure 5).
- Detectors do not generalise: the best of 12 deepfake-voice detectors had a 13.50% equal error rate (`USENIX-VOICEWUKONG-2025`).
- Reviewer workload set by regulator-mandated frequency (`DORA-RTS-2024` Art. 21(e)(iv); `NYDFS-AIGUIDE-2024`).

**Metrics and benchmarks (with sources)**
- NIST SP 800-63A-4 thresholds: 1:1 face verification false match rate 1:10,000 or better and false non-match rate 1:100 or better; 1:N false positive identification rate 1:1,000 or better with a gallery of at least 90% of the intended operational size; presentation attack IAPAR below 0.07; document false acceptance and rejection rates 0.1 or less; demographic groups no more than 25% worse than the whole population (`NIST-SP80063A-4-2025`, Sec. 3.11 and 3.13).
- Deepfake-voice detection: best EER 13.50%, others above 20% on VoiceWukong (`USENIX-VOICEWUKONG-2025`).
- Passkey deployments: 872 passkey-enabled sites tracked; 103 evaluated; 15 attack types; critical attacks on 18 sites; 53 vulnerable to at least one high-CVSS attack (`USENIX-PASSKEYS-2026`).
- Loss data: 22,364 AI-related complaints, USD 893,346,472 adjusted losses; about 4,700 ATO complaints, USD 359.7 million; losses in investment complaints with a reported AI nexus exceeded USD 632 million while overall investment-scam losses exceeded USD 8 billion, and IC3 says many victims do not realise how far AI was involved (`FBI-IC3-2025`, AI section and Cyber-Enabled Fraud section).
- ENISA: phishing was about 60% of initial intrusion vectors; ENISA reports, citing a KnowBe4 report, that over 80% of phishing emails identified between September 2024 and February 2025 used AI to some extent (`ENISA-ETL-2025`, booklet p. 4 and section 4.5).
- Survey: 90% of organizations report at least one successful identity-related breach in 12 months, 83% at least two, 76% three or more (vendor-commissioned, `PANW-IDLANDSCAPE-2026`, p. 13).
- Benchmark for insider-threat LLM triage: OrgForge-IT (51 days, 2,904 records, 96.4% noise) (`ARXIV-2603.22499`).

**Guardrails and regulatory points**
- NIST SP 800-63-4, Sec. 3.8: all uses of AI/ML in the identity system must be documented and disclosed to relying parties; vendors must give model training methods, data-set descriptions, update frequency and test results to customers; the NIST AI RMF should be used; privacy risk assessments are mandatory (`NIST-SP80063-4-2025`).
- NIST 63A-4 Sec. 3.14 requires sensor-authenticity controls and media-manipulation analysis, with documented false-negative rates; 3.11 requires published biometric test results (`NIST-SP80063A-4-2025`).
- FinCEN: SAR key term FIN-2024-DEEPFAKEFRAUD; phishing-resistant MFA and live verification are named as best practices, with the caution that criminals may respond to live prompts with synthetic audio and video (`FINCEN-ALERT004-2024`).
- NYDFS: as of November 2025 MFA is required for all authorized users; consider avoiding SMS, voice or video factors; use liveness detection or texture analysis; annual review of access privileges (`NYDFS-AIGUIDE-2024`).
- DORA RTS (EU 2024/1774): unique identities, automated identity lifecycle where feasible and appropriate, least privilege, access updates at least yearly (six-monthly for critical or important functions), strong authentication for remote and privileged access (`DORA-RTS-2024`, Art. 20-21).
- NIS2 implementing regulation (EU 2024/2690): access control policy, register of access rights, privileged account policy, MFA or continuous authentication, applies to the entity types in its Article 1 (DNS providers, cloud, data-centre, CDN, managed service providers, marketplaces, search engines, social networks, trust services) (`NIS2-IMPL-2024`).
- EU AI Act: Annex III biometrics high-risk entry excludes AI used only for one-to-one biometric verification that a person is who they claim to be; emotion inference in the workplace is prohibited (Art. 5(1)(f)); providers of systems generating synthetic content must mark outputs as machine-readable (Art. 50(2)) (`EU-AIACT-2024`). Application dates, including the postponement of Annex III obligations to 2027-12-02, are taken from the landscape file's reading of the Commission page (`EC-AIACT-2026`), not re-opened here.
- EU payments: the Parliament and Council deal makes a provider refund customers defrauded by someone posing as its staff when the customer reports to the police and informs the provider; formal adoption still pending in the source (`EP-PSR-2025`).
- CISA: phishing-resistant MFA (FIDO/WebAuthn or PKI) recommended against help-desk social engineering, MFA fatigue and SIM swap (`CISA-AA23-320A-2025`). CISA and NIST token-protection report IR 8587 final (`CISA-IR8587-2026`).
- US SEC rules (Item 1.05, Reg S-P, Reg S-ID) were not examined; see Gaps.

**Frontier signals (dated and sourced)**
- 2025-07: NIST finalises SP 800-63-4 with AI/ML requirements and injection and forged-media rules (`NIST-SP80063-4-2025`).
- 2025-11-27 (provisional deal): EU payments reform shifts impersonation-fraud losses to providers; adoption not yet confirmed (`EP-PSR-2025`).
- 2025-05-07: UK NCSC assesses that AI will almost certainly make parts of cyber intrusion, including access through social engineering, more effective and efficient to 2027 (`NCSC-AI2027-2025`).
- 2026-03-18: a vendor reports that only one of 18 systems in the Active PAD part of DHS S&T's 2025 remote-identity rally had zero attack acceptance (`IDENTY-RIVR-2026`).
- 2026-04: FBI IC3 reports 22,364 AI-related complaints (`FBI-IC3-2025`).
- 2026-06: survey of 2,930 decision-makers reports 109 machine identities per human and AI agents as a joint top driver of identity growth (`PANW-IDLANDSCAPE-2026`).
- 2026-08: USENIX Security 2026 passkey study finds exploitable flaws on about half of 103 tested sites (`USENIX-PASSKEYS-2026`).
- 2026-09-15: CISA and NIST finalise IR 8587 on token theft and forgery for federal cloud identity (`CISA-IR8587-2026`).
- 2026-10-12: preprint shows challenge sets must be re-tested against current face-swap tools (`ARXIV-2610.16417`).

**Workforce and role effects**
- ISC2 2025 workforce study (published 2025-12-04): AI was the most pressing skills need (41%), ahead of cloud security (36%); IAM was a skills need for 35% of respondents focused on cloud skills; among respondents focused on zero trust, least-privilege implementation (33%) and identity-centric security (30%) were focus areas. Traditional roles such as SOC analyst and incident responder are described as evolving (`ISC2-WORKFORCE-2025`, skills and AI sections).
- Proofing agents and trusted referees must be trained on manipulated-media signs (`NIST-SP80063A-4-2025`, Sec. 3.14).
- Help-desk agents become a security control point; the vendor pitch is that they verify instead of interrogate (`NAMETAG-SERVICENOW-2026`).
- Identity teams govern a far larger non-human population (109:1 in the vendor survey) (`PANW-IDLANDSCAPE-2026`).

**Objections and concerns practitioners raise**
- Detection will not keep up: independent benchmarks show high error rates in real-world conditions (`USENIX-VOICEWUKONG-2025`, `ARXIV-2601.02914`, `USENIX-CHIMERA-2025`).
- Phishing-resistant factors are not immune, and adoption is uneven (a census of the top 100K sites finds adoption tracks site popularity and often depends on external identity providers, `ARXIV-2602.15135`): passkey implementations had account-takeover and lock-out flaws (`USENIX-PASSKEYS-2026`); an analysis of FIDO2 attack vectors concludes successful attacks need substantial effort and resources but that the phishing-resistance claim has limits (`ARXIV-2604.20826`, abstract).
- Biometric data theft and bias: NYDFS on stolen biometrics; NIST on the 25% demographic limit.
- Explainability of AI in access decisions (search-only, `NHIMG-NEXIS-2026`).
- Vendor-sourced evidence: nearly all quantitative adoption and outcome data come from vendors (`PANW-IDLANDSCAPE-2026`, `IDENTY-RIVR-2026`, `REALDEFENDER-BANK-2025`).
- Attack-mix scepticism: the DBIR 2026 landing page says vulnerability exploitation now beats stolen passwords as the top entry route (`VERIZON-DBIR-2026`; body not read).

**Interview probes for an advisor**
1. Where do you decide that a person is who they claim to be (onboarding, account recovery, service desk, high-value payment approvals), and which of those still rely on voice, video, SMS or knowledge questions?
2. If a vendor tool scores a selfie, document or call as synthetic, who reviews the score, what is your false-positive tolerance, and have you tested it against current face-swap and voice-clone tools or only the vendor's data?
3. When reviewers get a recommendation in an access review, how often do they override it, and do you measure whether reviewers approve in bulk?
4. Which response actions can your identity team run in minutes without opening a ticket (revoke tokens, end privileged sessions, remove roles), and which need another team?
5. Which regulators ask you for proof of access reviews (DORA, NIS2, NYDFS, others), and how much of the evidence is assembled by hand?

## 4. Routed to other modules

- **ai-security (agent identity, authorization, containment).** The OpenID Foundation whitepaper "Identity Management for Agentic AI" (published 2025-10-07; `OPENID-AGENTID-2025`); the survey's agent findings: 99% report using AI agents, 79 AI-agent identities per human, 40% of AI agents and machine identities already have access to organizational data, 90% agree agents should run under least privilege (`PANW-IDLANDSCAPE-2026`, pp. 7-8); a measurement of 7,973 live remote MCP servers finding 40.55% expose tools without authentication, with 119 OAuth-enabled servers tested all showing at least one flaw (`ARXIV-2605.22333`, abstract); USENIX Security 2026 title "FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion" (title only, `USENIX-SEC-2026-TITLES`).
- **human-risk (scams, deepfakes, impersonation, awareness).** USENIX Security 2026 romance-baiting study: 87% of scam labour is systematised conversational work, and an LLM agent obtained 46% compliance versus 18% for human operators in a week-long blinded study (`USENIX-ROMANCE-2026`); IC3 AI-involved employment scams of almost USD 13 million, and voice-spoofing in online interviews (`FBI-IC3-2025`, AI section); ENISA's AI-supported phishing figures (`ENISA-ETL-2025`); NYDFS training expectations on deepfake exercises (`NYDFS-AIGUIDE-2024`).
- **application-security / cloud-infrastructure.** A 2026 preprint on secrets in production web code: 113 of about 2,000 assets in one organization (5.65%) served live credentials, and the best of nine scanners found 36.6% (static) or 77.8% (runtime-aware) of a ground-truth set (`ARXIV-2609.23042`, abstract). CISA/NIST IR 8587's cloud identity-provider architecture guidance (`CISA-IR8587-2026`).
- **security-governance-risk.** EU AI Act application dates and AI Omnibus (`EC-AIACT-2026`, landscape); NIST AI RMF reference in SP 800-63-4 (`NIST-SP80063-4-2025`); SEC rules not examined here.
- **security-operations.** LLM triage generalities beyond identity (`ARXIV-2603.22499` overlaps).

## 5. Sources

Ref | Title | Publisher | Type | URL | Date | Access

- `NIST-SP80063-4-2025` | Digital Identity Guidelines, SP 800-63-4 | NIST | standard-setter | https://doi.org/10.6028/NIST.SP.800-63-4 | 2025-07 | full
- `NIST-SP80063A-4-2025` | SP 800-63A-4 Identity Proofing and Enrollment | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63A-4.pdf | 2025-07 | full
- `NIST-SP80063B-4-2025` | SP 800-63B-4 Authentication and Authenticator Management | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63B-4.pdf | 2025-07 | full
- `FINCEN-ALERT004-2024` | FinCEN Alert on Fraud Schemes Involving Deepfake Media (FIN-2024-Alert004) | FinCEN | regulator | https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf | 2024-11-13 | full
- `NYDFS-AIGUIDE-2024` | Cybersecurity Risks Arising from AI and Strategies to Combat Related Risks | NYDFS | regulator | https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks | 2024-10-16 | full
- `CISA-IR8587-2026` | CISA and NIST Release Guidelines to Protect Federal Cloud Identity Systems from Token Theft, Forgery, and Misuse (NIST IR 8587) | CISA | regulator | https://www.cisa.gov/news-events/news/cisa-and-nist-release-guidelines-protect-federal-cloud-identity-systems-token-theft-forgery-and | 2026-09-15 | full (press release; IR 8587 text itself not read)
- `CISA-AA23-320A-2025` | Scattered Spider, joint advisory AA23-320A (updated 2025-07-29) | CISA, FBI and partners | regulator | https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a | 2025-07-29 | full
- `ENISA-ETL-2025` | ENISA Threat Landscape 2025 | ENISA | regulator | https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025 | 2025-10 | full (the PDF read is labelled v1.3, September 2026, with a cover date of October 2025)
- `FBI-IC3-2025` | 2025 Internet Crime Report | FBI IC3 | regulator | https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf | 2026-04 | full (date from PDF creation metadata, 2026-04-16)
- `NCSC-AI2027-2025` | Impact of AI on cyber threat from now to 2027 | UK NCSC | regulator | https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027 | 2025-05-07 | full
- `DORA-RTS-2024` | Commission Delegated Regulation (EU) 2024/1774 | European Commission | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1774 | 2024-06-25 | full
- `NIS2-IMPL-2024` | Commission Implementing Regulation (EU) 2024/2690 | European Commission | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2690 | 2024-10-18 | full
- `EU-AIACT-2024` | Regulation (EU) 2024/1689 (AI Act) | European Parliament and Council | regulator | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 2024-07-12 | full
- `EP-PSR-2025` | Payment services deal: More protection from online fraud and hidden fees | European Parliament | regulator | https://www.europarl.europa.eu/news/en/press-room/20251121IPR31540/payment-services-deal-more-protection-from-online-fraud-and-hidden-fees | 2025-11 | full
- `EC-AIACT-2026` | EU AI Act status page (from landscape file; not re-opened) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-17 | search-only (second-hand via landscape)
- `USENIX-VOICEWUKONG-2025` | VoiceWukong: Benchmarking Deepfake Voice Detection | USENIX Security 2025 | academic | https://www.usenix.org/conference/usenixsecurity25/presentation/yan-ziwei | 2025-08 | full
- `USENIX-REDBLEED-2025` | Red Bleed: A Pragmatic Near-Infrared Presentation Attack on Facial Biometric Authentication Systems | USENIX Security 2025 | academic | https://www.usenix.org/conference/usenixsecurity25/presentation/hu-bowen | 2025-08 | full
- `USENIX-CHIMERA-2025` | Chimera: Creating Digitally Signed Fake Photos by Fooling Image Recapture and Deepfake Detectors | USENIX Security 2025 | academic | https://www.usenix.org/conference/usenixsecurity25/presentation/park | 2025-08 | full
- `USENIX-PASSLLM-2025` | Password Guessing Using Large Language Models | USENIX Security 2025 | academic | https://www.usenix.org/conference/usenixsecurity25/presentation/zou-yunkai | 2025-08 | full
- `USENIX-PASSKEYS-2026` | The State of Passkeys: Studying the Adoption and Security of Passkeys on the Web | USENIX Security 2026 | academic | https://www.usenix.org/conference/usenixsecurity26/presentation/jannett | 2026-08 | full
- `USENIX-ROMANCE-2026` | Love, Lies, and Language Models: Investigating AI's Role in Romance-Baiting Scams | USENIX Security 2026 | academic | https://www.usenix.org/conference/usenixsecurity26/presentation/gressel | 2026-08 | full
- `USENIX-SEC-2026-TITLES` | USENIX Security 2026 technical sessions list (FragFuse title) | USENIX | academic | https://www.usenix.org/conference/usenixsecurity26/technical-sessions | 2026-08 | full (titles only)
- `NDSS-PPG-2026` | Know Me by My Pulse: Continuous Authentication on Wearable Devices via Wrist-Worn PPG | NDSS Symposium 2026 | academic | https://www.ndss-symposium.org/ndss-paper/know-me-by-my-pulse-toward-practical-continuous-authentication-on-wearable-devices-via-wrist-worn-ppg/ | 2026-02 | full
- `NDSS-CHIMERA-INSIDER-2026` | Chimera: Harnessing Multi-Agent LLMs for Automatic Insider Threat Simulation | NDSS Symposium 2026 | academic | https://www.ndss-symposium.org/ndss-paper/chimera-harnessing-multi-agent-llms-for-automatic-insider-threat-simulation/ | 2026-02 | full
- `IEEESP-2026` | IEEE Symposium on Security and Privacy 2026 program | IEEE | academic | https://sp2026.ieee-security.org/program.html | 2026-05 | full (titles only)
- `ARXIV-2610.16417` | Not All Challenges Are Equal: Evaluating Interactive Liveness Detection Against Real-Time Face Swaps | arXiv | academic | https://arxiv.org/abs/2610.16417 | 2026-10-12 | full
- `ARXIV-2601.02914` | Vulnerabilities of Audio-Based Biometric Authentication Systems Against Deepfake Speech Synthesis | arXiv | academic | https://arxiv.org/abs/2601.02914 | 2026-01-06 | full
- `ARXIV-2605.00218` | Selfie-Capture Dynamics as an Auxiliary Signal Against Deepfakes and Injection Attacks for Mobile Identity Verification | arXiv | academic | https://arxiv.org/abs/2605.00218 | 2026-04-30 | full
- `ARXIV-2607.13234` | Continuously Evolving Deepfake Detection (BitMind) | arXiv | academic | https://arxiv.org/abs/2607.13234 | 2026-07-14 | full
- `ARXIV-2603.22499` | OrgForge-IT: A Verifiable Synthetic Benchmark for LLM-Based Insider Threat Detection | arXiv | academic | https://arxiv.org/abs/2603.22499 | 2026-03-23 | full
- `ARXIV-2604.20826` | An Analysis of Attack Vectors Against FIDO2 Authentication | arXiv | academic | https://arxiv.org/abs/2604.20826 | 2026-04-22 | full
- `ARXIV-2602.15135` | State of Passkey Authentication in the Wild: A Census of the Top 100K Sites | arXiv | academic | https://arxiv.org/abs/2602.15135 | 2026-02-16 | full (abstract; adoption correlates with site popularity and often depends on external identity providers)
- `ARXIV-2605.22333` | A First Measurement Study on Authentication Security in Real-World Remote MCP Servers | arXiv | academic | https://arxiv.org/abs/2605.22333 | 2026-05 | full (abstract; routed)
- `ARXIV-2609.23042` | Secrets That Survive Everything: Runtime Credential Exposure in Production Web Applications | arXiv | academic | https://arxiv.org/abs/2609.23042 | 2026-09 | full (abstract; routed)
- `PANW-IDLANDSCAPE-2026` | 2026 Identity Security Landscape (research by Vanson Bourne, n=2,930, fielded March-April 2026) | Palo Alto Networks | survey | https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/2026-identity-security-landscape-report.pdf | 2026-06 | full (month from PDF creation metadata; vendor-commissioned)
- `VERIZON-DBIR-2026` | 2026 Data Breach Investigations Report (landing page) | Verizon | survey | https://www.verizon.com/business/resources/reports/dbir/ | 2026 | full (landing page only; publication date not stated)
- `IDENTY-RIVR-2026` | Identy.io Achieves Zero Attack Acceptance in DHS RIVR Face Liveness Evaluation | Identy.io via Business Wire | vendor | https://businesswire.com/news/home/20260318279525/en/Identy.io-Achieves-Zero-Attack-Acceptance-in-DHS-RIVR-Face-Liveness-Evaluation-Leads-Field-on-Speed-and-User-Satisfaction | 2026-03-18 | full
- `REALDEFENDER-BANK-2025` | How a Global Bank Defends Contact Centers Against Deepfake Threats with Reality Defender | Reality Defender | vendor | https://www.realitydefender.com/case-studies/how-a-tier-one-bank-stopped-deepfaked-audio-with-reality-defender | 2025 (inferred) | full
- `NAMETAG-SERVICENOW-2026` | Prevent Deepfake Impersonation at the ServiceNow IT Service Desk with Nametag Identity Verification | Nametag | vendor | https://getnametag.com/newsroom/servicenow-identity-verification | 2026-10-17 (retrieved; undated) | full
- `MSFT-ENTRA-ACCESSREV-2026` | Review recommendations for access reviews | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/entra/id-governance/review-recommendations-access-reviews | 2026-10-17 (retrieved; undated) | full
- `MSFT-ENTRAIDP-2026` | What are risk detections? Microsoft Entra ID Protection | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks | 2026-10-17 (retrieved; undated) | full
- `GOOGLE-IAMREC-2026` | Overview of role recommendations | Google Cloud | vendor | https://cloud.google.com/policy-intelligence/docs/role-recommendations-overview | 2026-10-17 (retrieved; undated) | full
- `ISC2-WORKFORCE-2025` | 2025 ISC2 Cybersecurity Workforce Study | ISC2 | professional-body | https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study | 2025-12-04 | full
- `OPENID-AGENTID-2025` | Identity Management for Agentic AI (whitepaper) | OpenID Foundation | standard-setter | https://openid.net/new-whitepaper-tackles-ai-agent-identity-challenges/ | 2025-10-07 | full (announcement page and PDF opening only; routed)
- `ENTRUST-IDFRAUD-2026` | Entrust 2026 Identity Fraud Report (press release 2025-11-18) | Entrust | vendor | https://www.entrust.com/resources/reports/identity-fraud-report | 2025-11-18 | search-only
- `SAILPOINT-INFOGRAPHIC-2026` | SailPoint infographic on identity governance (April 2026) | SailPoint | vendor | https://www.sailpoint.com/identity-library/future-of-identity-governance | 2026-04-29 | search-only
- `PATHLOCK-GARTNER-IGA-2026` | 2026 Gartner IGA Market Guide: top findings (Pathlock summary) | Pathlock | vendor | https://pathlock.com/blog/2026-gartner-iga-market-guide-top-findings/ | 2026 | search-only
- `NHIMG-NEXIS-2026` | Explainability Is the Deciding Factor in AI Access Administration | NHI Management Group | community | https://nhimg.org/articles/explainability-is-the-deciding-factor-in-ai-access-administration/ | 2026-07-28 | search-only
- `MSFT-DDR-2025` | Secondary summary of Microsoft Digital Defense Report 2025 (97% of identity attacks involve passwords) | Expert Insights | press | https://expertinsights.com/news/97-of-identity-attacks-involve-passwords-says-microsoft | 2025-10 (month inferred from related coverage) | search-only
- `FINTECHGLOBAL-ATO-2026` | Account takeover fraud exposes gaps beyond authentication | Fintech Global | press | https://fintech.global/2026/09/18/account-takeover-fraud-exposes-gaps-beyond-authentication/ | 2026-09-18 | search-only

Counts of opened-and-read sources (access: full): 43 distinct. By type: regulator 11, standard-setter 4, academic 19, survey 2, vendor 6, professional-body 1. Seven further items are search-only or second-hand (listed above, not used as outcomes).

## 6. Gaps

- **No named-organization measured outcome** for any AI use in IAM work. There are no override rates, reviewer-agreement figures, parallel-run results, false-positive rates from production, or inspection findings in the public sources reached. The two most quantitative deployment-like items are an unnamed bank's vendor case (`REALDEFENDER-BANK-2025`) and a vendor's claim about an independent test (`IDENTY-RIVR-2026`).
- **DHS S&T Remote Identity Validation Rally reports** (the main independent testing of liveness and document validation) were not reachable; dhs.gov returned 403 or 404. Only vendor releases were read.
- **Not reached or paywalled:** Entrust 2026 Identity Fraud Report (Business Wire returned 403; search-only), Microsoft Digital Defense Report 2025 (403; secondary summaries only), Gartner IGA Market Guide and Hype Cycle for Digital Identity, SailPoint's underlying survey (infographic seen via search), CrowdStrike Global Threat Report (landing page only), Verizon DBIR 2026 body, NIST IR 8587 full text, NIST NCCoE agent-identity project (403), CISA deepfake information sheet (403), MAS deepfake paper (404), FS-ISAC and UK NCSC CAF B2 identity pages (shell only).
- **US SEC:** the FY2026 exam priorities URL returned 404, so SEC treatment of Regulation S-ID (identity-theft red flags), Regulation S-P amendments and Item 1.05 in relation to identity fraud was not checked.
- **Peer-reviewed coverage:** USENIX Security 2025/2026 and NDSS 2026 papers were read at abstract level only. IEEE S&P 2026 papers on passwords and passkeys were seen by title only. ACM CCS 2026 has not yet taken place (15-19 Nov 2026). Several academic items are preprints that are not peer reviewed (`ARXIV-*`), and one deepfake-detection preprint is written by a detector vendor.
- **Dates:** the Reality Defender case study, Microsoft Learn pages, Google documentation and Nametag release carry no publication date; retrieval date or an inferred year is used and flagged. The Verizon DBIR 2026 landing page and Pathlock summary are dated by year only. The European Parliament press release date (2025-11) is taken from secondary reporting of the provisional agreement.
- **Not found:** an independent measurement of rubber-stamping before and after AI recommendations; any study of AI in joiner-mover-leaver automation with outcomes; named-bank ATO deployments with measured results; regulator guidance specific to AI-based access-review tools.
- **Scope note:** the DBIR 2026 landing page and the Microsoft DDR 2025 summary suggest password-based and vulnerability-based entry still dominate; this report did not test how much of identity loss is AI-driven.

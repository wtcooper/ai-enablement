# Assurance / assurance-over-ai / practice

- **Archetype:** assurance
- **Module:** assurance-over-ai (auditing AI the entity uses in financial reporting and internal control; standalone assurance services over AI systems)
- **Angle:** practice (what firms and buyers actually do)
- **Prepared:** 2026-10-16
- **Method:** Pages were fetched with `curl` (PDFs with `pdftotext`). Every source below was opened unless it is marked `search-only`. The web-search budget ran out after about 16 searches, so the later leads (pricing, certificate counts, other firms' offers) were followed only by direct URL and many stayed unreached (see Gaps).

**Reading convention for this module.** In most entries the AI is the *subject* of the engagement, not the tool that does the work. The vocabulary's `ladder`, `pattern` and `runtime_class` describe how much AI does the work, so for these entries they are placeholders (`assist`, `other`, `personal-assistant` or `shared-team-skills`) and each entry's `notes` says so. The meaningful field is `change_scope: model`, because most of these entries are new services, new credentials or new roles for assurance firms. Work done *with* AI inside assurance engagements is routed to other modules.

---

## 1. Summary

- **The practice is real but thin at the client end.**
  - Named *firm-side* activity is plentiful: KPMG UK sells an AI governance assurance product; KPMG US and KPMG International certified their own AI management systems; PwC Canada launched an ISO/IEC 42001 certification solution; PwC Taiwan and two EY Italian entities were certified; EY says it runs a certification body that certifies to ISO/IEC 42001; Deloitte and EY describe AI assurance offers.
  - Named *client* engagements are scarce. The only named buyers found are AI-native companies certified under AIUC-1 (Cursor, Fin, ElevenLabs, Harvey, UiPath, Lovable) and two start-ups, Evisort and StackAware, that Schellman audited as practice runs for its ISO/IEC 42001 accreditation.
  - No issued Big Four assurance report over a client's AI, no fee, and no certificate count was found.
- **Certification-body (CB) capacity is the leading edge, and specialists got there first.**
  - Schellman was the first ANAB-accredited ISO/IEC 42001 certifier (announced Sep 2024; it reported 26 signed client contracts in Oct 2024).
  - BSI added ANAB accreditation on 10 Mar 2026, which it says makes it the first CB with ANAB, UKAS and RvA accreditation for the standard.
  - ISO/IEC 42006 (published 2025) is moving into accreditation programmes. A compliance-vendor blog reports a European accreditation decision of 20 Nov 2025 to make it mandatory. The Big Four mostly appear as *certified organisations* and *advisers*, with EY's CertifyPoint the one Big Four-owned CB found.
- **There are now two competing product shapes for "assurance over AI".**
  - *Management-system certification* (ISO/IEC 42001, by an accredited CB).
  - *Attestation over controls* (KPMG UK's ISAE (UK) 3000 report built on SOC principles, described in KPMG's own paper as "SOC2+" reasonable assurance).
  - A third shape, adversarial-testing certification plus insurance (AIUC-1), is aimed at AI agents. KPMG LLP got its own aIQ Capture platform certified on 27 Aug 2026.
- **Inside financial-statement audits, scoping of AI is guidance-led and mostly "test around".**
  - The AICPA practice aid (13 Oct 2026), the COSO GenAI roadmap (Feb 2026) and BDO's ITGC paper (Jul 2026) tell auditors to establish whether the entity *relies* on AI output, treat AI components as in-scope systems, and extend ITGC thinking to models, data pipelines and agents.
  - KPMG states that SOX programmes are still testing "around" AI and expects the first AI-related material weaknesses in 2027. That is a firm expectation, not a measurement.
  - No inspection finding or independent measurement on auditors' scoping of AI in ICFR audits was found.
- **Demand evidence is mostly self-reported or old.**
  - UK government (Nov 2024): 524 firms supply AI assurance goods and services, 84 of them specialised, with about £1.01bn of estimated gross value added (GVA).
  - KPMG UK says procurement teams increasingly ask for AI assurance (its own experience claim).
  - Regulation does not yet force most buyers. For most Annex III high-risk categories, the EU AI Act allows provider self-assessment, so third-party demand there is not guaranteed.

**Two most important insights.** (1) Firms are building credibility by certifying themselves first, which is a prerequisite and a marketing signal, while client engagements are unnamed; accreditation, competence and independence rules (ISO/IEC 42006, impartiality limits on consulting-plus-certification) shape who can sell what. (2) For auditors of financial statements, the practical question is "does the entity rely on this AI output?" Reliance pulls in the ITGC, SOC-report and tests-of-controls machinery, and the profession's own guidance concedes its testing methods for probabilistic, third-party AI are still open.

---

## 2. Use cases

Counts: 19 entries. Grades: A = 1, B = 4, C = 13, D = 1. The A is for demand/accreditation figures that are self-reported, not quality results (see its `notes`).

```yaml
- id: assurance-assurance-over-ai-01
  title: Reasonable-assurance report over an organisation's AI governance and controls (SOC-style, ISAE (UK) 3000)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: Customers, boards and procurement teams cannot see whether a supplier's AI is governed in practice rather than only on paper, and no prescriptive regulation requires external assurance.
  solution: A firm's assurance practice tests whether AI governance controls are clearly defined, suitably designed and operating effectively, and issues an independent assurance report that the client can share with customers. KPMG UK says the criteria are based on the Trust Services Criteria and informed by its Trusted AI framework (which incorporates relevant EU AI Act and ISO/IEC 42001 requirements). KPMG's January 2026 paper calls the approach SOC 2+ and says it gives reasonable assurance over governance and controls around AI systems, with scoping, readiness and formal opinion as stages.
  outcomes:
    - lever: growth
      description: KPMG UK states, from its own experience, that AI assurance is increasingly requested and assessed by procurement and supplier-risk teams. No figure published.
      figure: none published
      measures: qualitative statement by the provider; no count of requests, clients or reports
      provenance: self-reported
      source_ref: KPMGUK-GOVAI-2026
  prerequisites:
    - A defined AI governance control framework at the client (ownership, escalation, lifecycle management) that can be tested.
    - Suitable criteria; the criteria here are the firm's own, built on Trust Services Criteria.
    - A practitioner competent in both SOC-type attestation and AI risk.
  risks_and_guardrails:
    - Engagement performed under ISAE (UK) 3000, issued by the FRC (KPMGUK-GOVAI-2026, section "Make AI Trust Stand Up to Scrutiny").
    - KPMG US material notes that some services may not be permissible for KPMG audit clients (KPMGUS-ISO-2025, closing disclaimer); independence is routed to acceptance-independence.
    - The CSA note argues no AI-specific Trust Services Criteria exist, so evidence requests are improvised (carried from the landscape; not re-read here).
  human_checkpoints:
    - Partner-signed assurance opinion.
    - Management's assertion and controls description.
  role_evolution: SOC and controls-assurance teams add AI control objectives to their reports; KPMG describes the team as one that tests, examines evidence and reports on management's process, controls and claims on responsible AI (KPMGUK-CONTROLS-2026, p.8).
  evidence_grade: C
  sources:
    - { ref: KPMGUK-GOVAI-2026, title: "Independent confidence in how you govern AI", publisher: KPMG UK, type: firm, url: "https://kpmg.com/uk/en/insights/audit/independent-confidence-in-how-you-govern-ai.html", date: 2026-09-22, access: full, locator: "sections 'Make AI Trust Stand Up to Scrutiny' and 'Differentiate in the market'; date from page metadata" }
    - { ref: KPMGUK-CONTROLS-2026, title: "Reimagining Controls Assurance with AI: Latest Insights for Leaders", publisher: KPMG UK, type: firm, url: "https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf", date: 2026-01, access: full, locator: "foreword item 2 'Assurance of AI'; p.8" }
  last_reviewed: 2026-10-16
  notes: "Product page and paper describe an offer; no named client, issued report or opinion wording was found, and the web page does not state the assurance level (the paper does: reasonable). Ladder, pattern and runtime_class are placeholders because AI is the subject, not the tool."

- id: assurance-assurance-over-ai-02
  title: ISO/IEC 42001 certification of an AI management system by an accredited certification body
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Enterprise buyers cannot inspect a supplier's models, data pipelines or internal controls, and need an independent signal that the supplier operates a managed AI governance system.
  solution: An accredited certification body audits the client's AI management system against ISO/IEC 42001 and issues a certificate. Schellman became the first ANAB-accredited body after an eight-month process in which ANAB witnessed audits of two start-ups, Evisort and StackAware. BSI announced ANAB accreditation on 10 Mar 2026, in addition to UKAS and RvA accreditation. ISO/IEC 42006 adds AI-specific competence rules and an audit-time method for certification bodies.
  outcomes:
    - lever: growth
      description: Schellman's CEO said in Oct 2024 that the firm already had signed contracts with clients wanting ISO/IEC 42001 certification.
      figure: "26"
      measures: "signed client contracts for ISO/IEC 42001 certification at Schellman at the time of the interview (Accounting Today, 28 Oct 2024)"
      provenance: self-reported
      source_ref: SCHELLMAN-AT-2024
    - lever: growth
      description: BSI reports that a share of organisations in its research are taking steps toward ISO/IEC 42001.
      figure: "26%"
      measures: "organizations that 'report taking steps to align with ISO/IEC 42001', per BSI research cited in its release; sample size and date not stated"
      provenance: vendor-published
      source_ref: BSI-ANAB-2026
  prerequisites:
    - A documented AI management system with a defined scope, AI policy, risk and impact assessments, and Annex A controls.
    - A certification body accredited for the scheme; the market mixes bodies accredited before and after ISO/IEC 42006 existed.
    - Audit teams that together cover AI, management systems, auditing and relevant law (ISO/IEC 42006 as described in BRIGHT-42006-2026).
  risks_and_guardrails:
    - A BSI accredited body does not certify a client for the same management system that another part of BSI has consulted on (BSI-ANAB-2026, "Our Accreditation").
    - Early certification rules reportedly asked firms to make algorithms transparent; Schellman's CEO says she pushed back because algorithms are proprietary (SCHELLMAN-AT-2024).
    - ISO/IEC 42006 audit time is a calculated minimum, and deviations must be documented (BRIGHT-42006-2026, secondary source).
    - A certificate is only as good as the issuing body; the CSA note advises buyers to check the body's accreditation, not just the certificate (CSA-AIASSURE-2026; lead source).
  human_checkpoints:
    - Certification decision by the certification body.
    - Accreditation-body witness audits and office visits.
  role_evolution: Management-system auditors and AI specialists work as combined teams; Schellman, a SOC audit firm, expanded into AI governance certification as clients began large AI investments (SCHELLMAN-AT-2024).
  evidence_grade: A
  sources:
    - { ref: SCHELLMAN-AT-2024, title: "Inside Schellman's journey to provide certification for ISO 42001 AI framework", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/inside-schellmans-journey-to-provide-certification-for-iso-42001-ai-framework", date: 2024-10-28, access: full, locator: "paragraphs on the eight-month ANAB process, Evisort and StackAware, and 'Ready to meet demand'" }
    - { ref: BSI-ANAB-2026, title: "BSI secures ANAB accreditation to certify ISO/IEC 42001", publisher: BSI, type: vendor, url: "https://www.bsigroup.com/en-US/insights-and-media/media-center/press-releases/2026/march/bsi-secures-anab-accreditation-to-certify-isoiec-42001/", date: 2026-03-10, access: full, locator: "release body; 'Our Accreditation' footer" }
    - { ref: BRIGHT-42006-2026, title: "ISO 42006 Raises the Bar for ISO 42001 Certifiers", publisher: Bright Defense, type: vendor, url: "https://brightdefense.com/news/iso-42006-raises-the-bar-for-iso-42001-certifiers", date: 2026-09-14, access: full, locator: "sections on competence and audit time; European accreditation vote of 20 Nov 2025" }
  last_reviewed: 2026-10-16
  notes: "Graded A only because named organisations published figures (contracts, accreditation); neither figure measures audit quality or client outcomes. The Schellman figure is two years old. Bright Defense is a compliance vendor and a secondary source for ISO/IEC 42006 details (ISO page returned 403). No count of certificates issued was found."

- id: assurance-assurance-over-ai-03
  title: Big Four member firms certify their own AI management systems before selling AI assurance
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: A firm selling AI governance advice or assurance must show it holds itself to the same standard, and clients ask who has been through the process.
  solution: Firms obtain ISO/IEC 42001 certification for their own AI systems from an accredited body and publicise it. KPMG LLP (US) announced its certification on 18 Nov 2025, citing Schellman Compliance as the certification body. KPMG International followed in December 2025 and said Australia, Spain, India and the USA firms were already certified. SGS issued PwC Taiwan its first ISO/IEC 42001 certificate in Taiwan (15 Jun 2026). Two EY Italian entities hold certificates (EY S.p.A. first issued 23 Oct 2025 by Certiquality; EY Advisory S.p.A. decision of 20 Apr 2026 by ACM Cert).
  outcomes:
    - lever: growth
      description: Firms present the certificate as proof of experience and as a basis to help clients with their own certification. No figure published.
      figure: none published
      measures: qualitative statements in firm and certifier releases
      provenance: self-reported
      source_ref: KPMGINTL-ISO-2025
  prerequisites:
    - An in-scope AI estate (KPMG names Workbench and aIQ Chat as tools covered by the certification).
    - An accredited certification body that is independent of the firm's consulting arm.
  risks_and_guardrails:
    - Certification covers the firm's own management system and does not assure any client's AI.
    - Certificates have a defined scope; the EY Advisory certificate scope covers AI systems and AI-enabled services supporting client data handling and consulting services (EYIT-CERT-2026).
  human_checkpoints:
    - Certification-body audit and decision.
  role_evolution: Firm AI governance teams (KPMG's US Trusted AI leader is quoted) become reference practitioners for client work.
  evidence_grade: B
  sources:
    - { ref: KPMGUS-ISO-2025, title: "KPMG LLP Among First of the Big Four in the U.S. to Receive ISO 42001 AI Certification", publisher: KPMG US, type: firm, url: "https://kpmg.com/us/en/media/news/kpmg-receives-iso-ai-certification.html", date: 2025-11-18, access: full, locator: "release body; certification body named in the penultimate paragraph" }
    - { ref: KPMGINTL-ISO-2025, title: "KPMG International becomes first Big Four international entity to attain ISO 42001 certification for AI Management Systems", publisher: KPMG International, type: firm, url: "https://kpmg.com/xx/en/media/press-releases/2025/12/kpmg-international-first-to-attain-iso-certification-for-ai-management-systems.html", date: 2025-12, access: full, locator: "paragraphs 1 and 4; exact day not on the page (URL path shows 2025/12)" }
    - { ref: SGS-PWCTW-2026, title: "PwC Taiwan Achieves ISO/IEC 42001 AI Management System Certification", publisher: SGS, type: vendor, url: "https://www.sgs.com/en/news/2026/06/pwc-taiwan-achieves-iso-iec-42001-ai-management-system-certification", date: 2026-06-15, access: full, locator: "body text; 'Why SGS?'" }
    - { ref: EYIT-CERT-2025, title: "Certificate no. 72849, EY S.p.A., ISO/IEC 42001:2023", publisher: Certiquality (published on ey.com), type: firm, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/it-it/campaigns/corporate-responsibilty/documents/ey-certificato-iso42001-eyspa-11-25.pdf", date: 2025-10-23, access: full, locator: "page 1, first issue and expiry (22 Oct 2028)" }
    - { ref: EYIT-CERT-2026, title: "Certificate IT26-08316, EY Advisory S.p.A., UNI CEI ISO/IEC 42001", publisher: ACM Cert (published on ey.com), type: firm, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/it-it/campaigns/corporate-responsibilty/documents/ey-eyadv-certificato-iso42001-4-26.pdf", date: 2026-04-20, access: full, locator: "page 1, decision date and scope" }
  last_reviewed: 2026-10-16
  notes: "Self-certification is a market-entry signal, not a client service. The KPMG International release is not dated on the page; the UK trade press headline of 12 Dec 2025 (search result, not opened) is consistent with a release on or before that date. Deloitte's own certification status was not found."

- id: assurance-assurance-over-ai-04
  title: Firm-owned certification body offers ISO/IEC 42001 certification (EY CertifyPoint)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: Firms with an assurance brand can only issue management-system certificates if they run an accredited certification body with its own impartiality rules.
  solution: EY Japan's service page says EY supports ISO/IEC 42001:2023 through EY's ISO certification body, and names EY CertifyPoint, based in Amsterdam, as the global body offering certification for AI management systems. The page describes a typical three-year certification cycle, and lists readiness services alongside it.
  outcomes:
    - lever: growth
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: EYJP-CERTIFYPOINT-2026
  prerequisites:
    - Accreditation of the body for the scheme (the page says it is accredited for several ISO standards, not specifically 42001).
    - Separation of readiness consulting from certification (BSI's published rule shows the constraint: BSI-ANAB-2026).
  risks_and_guardrails:
    - The page does not state ISO/IEC 42001 accreditation for CertifyPoint; do not assume it.
    - Combining readiness services and certification under one brand creates the impartiality question that accredited bodies must manage.
  human_checkpoints:
    - Certification decision by the body.
  role_evolution: not stated
  evidence_grade: C
  sources:
    - { ref: EYJP-CERTIFYPOINT-2026, title: "Services related to the AI management system standard ISO/IEC 42001:2023 (Japanese)", publisher: EY Japan, type: firm, url: "https://www.ey.com/ja_jp/services/technology-risk/iso-iec-42001-2023", date: 2026, access: full, locator: "sections 'What EY can do' and 'Why EY'; page is undated (related items run to Jun 2026)" }
  last_reviewed: 2026-10-16
  notes: "Page read in Japanese; the CertifyPoint home page could not be reached (proxy error), so accreditation scope is unverified. Placeholder fields as above."

- id: assurance-assurance-over-ai-05
  title: ISO/IEC 42001 certification offer from a Big Four firm to clients (PwC Canada)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: Canadian companies lack a clear independent way to prove their AI is trustworthy; less than half have formalised responsible AI and risk processes according to a PwC report.
  solution: Trade coverage of the PwC Canada launch (16 Feb 2026) says PwC launched a certification solution for ISO/IEC 42001 and claims to be the first Big Four firm to offer accreditation services for the standard. The offer covers assessing governance and oversight frameworks, evaluating data sourcing and management for bias and model risk, strengthening the security posture of AI environments, and testing controls and monitoring.
  outcomes:
    - lever: growth
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: CONSULTINGCA-PWC-2026
  prerequisites:
    - Unclear from the source; whether PwC acts as the accredited certification body or as adviser is not stated.
  risks_and_guardrails:
    - The wording "accreditation services" and "certification" is ambiguous; certification by an accredited body is a different activity from advisory readiness work (BSI-ANAB-2026 on impartiality).
  human_checkpoints:
    - not stated
  role_evolution: not stated
  evidence_grade: C
  sources:
    - { ref: CONSULTINGCA-PWC-2026, title: "PwC launches new AI governance certification solution", publisher: Consulting.ca, type: press, url: "https://www.consulting.ca/news/4859/pwc-canada-launches-new-ai-governance-certification-solution", date: 2026-02-16, access: full, locator: "article body, paragraphs 1-6" }
  last_reviewed: 2026-10-16
  notes: "PwC's own release (pwc.com/ca) returned 403. A search extract gave 10 Feb 2026 as its date and a CEO-survey figure; neither was verified and both are search-only, so they are not used as outcomes."

- id: assurance-assurance-over-ai-06
  title: AI governance readiness and gap assessment against ISO/IEC 42001 and NIST AI RMF
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Clients adopting AI need to know where their governance falls short of a benchmark standard before an auditor or customer asks.
  solution: Deloitte UK describes a five-pillar framework (governance, data management, modelling and development, pre-deployment evaluation, deployment and operation) aligned to ISO/IEC 42001, with "no-regret" steps such as an AI governance committee, an AI system inventory and risk or impact assessments. Its AI Assurance page offers objective third-party challenge over AI risk, governance and control maturity, including certification readiness. A Deloitte Singapore AI Assurance posting (25 Jun 2026) shows the work being staffed: consultants apply the Trustworthy AI methodology, identify and document bias, fairness, transparency, robustness, security and privacy risks, maintain client AI risk registers, and support gap analyses and remediation roadmaps.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: DELOITTE-42001-2025
  prerequisites:
    - An AI system inventory and policy baseline at the client.
    - Staff able to work from NIST AI RMF and ISO/IEC 42001.
  risks_and_guardrails:
    - Readiness work is advisory, not assurance; a firm that advises on a management system cannot also certify it as an accredited body (BSI-ANAB-2026).
  human_checkpoints:
    - Review by senior consultants of risk and quality reports (Deloitte Singapore posting).
  role_evolution: The Singapore posting seeks 2-4 years of experience and treats ISO/IEC 42001, ISO 31000 or ISO 27001 familiarity as an advantage, not a requirement, with expectation to deepen expertise on the job.
  evidence_grade: C
  sources:
    - { ref: DELOITTE-42001-2025, title: "Navigating AI Assurance: Spotlight on ISO/IEC 42001 standard", publisher: Deloitte UK, type: firm, url: "https://www.deloitte.com/uk/en/services/audit/blogs/navigating-ai-assurance-spotlight-on-iso-iec.html", date: 2025-10-07, access: full, locator: "sections 'Deloitte's Five-Pillar AI Framework' and 'No-Regret Steps'" }
    - { ref: DELOITTE-AIA-UK-2026, title: "AI Assurance for Responsible and Scalable AI Adoption", publisher: Deloitte UK, type: firm, url: "https://www.deloitte.com/uk/en/services/audit-assurance/services/ai-assurance.html", date: 2026-10-16, access: full, locator: "pillars list; page undated, date is retrieval date" }
    - { ref: DELOITTE-JOB-SG-2026, title: "A&A - SG - AI Assurance (Consultant / Senior Consultant)", publisher: Deloitte Singapore (via Monster Thailand), type: job-posting, url: "https://www.monster.co.th/job/a-a-sg-ai-assurance-deloitte-singapore-53507371", date: 2026-06-25, access: full, locator: "'Work you'll do' and requirements; posting marked closed; posted date from page data" }
  last_reviewed: 2026-10-16
  notes: "Offer and staffing evidence only; no named client. Deloitte NL and South Africa postings seen in a search result did not render or returned 404."

- id: assurance-assurance-over-ai-07
  title: Independent challenge of AI technical build and performance (model validation, GenAI testing)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Governance review alone does not show whether a given AI use case is accurate, robust, explainable and fair.
  solution: Deloitte UK's AI Assurance page lists objective third-party challenge over the technical build and performance of AI use cases, covering data, architecture, robustness, precision and accuracy, explainability, transparency, bias and fairness, and monitoring. The page also lists operational controls over AI-enabled applications: security, resilience, data governance, change control, incident management and third-party oversight.
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: DELOITTE-AIA-UK-2026
  prerequisites:
    - Access to model documentation, data and test results (access constraints are a recurring pain point; see module notes).
  risks_and_guardrails:
    - GenAI non-determinism and hallucination make validation harder; Deloitte UK lists a GenAI model validation article among related content but it was not opened.
  human_checkpoints:
    - not stated
  role_evolution: Model validation and algorithm assurance specialists join assurance teams (Deloitte UK refers to its "Algorithm and AI Assurance team": DELOITTE-42001-2025).
  evidence_grade: C
  sources:
    - { ref: DELOITTE-AIA-UK-2026, title: "AI Assurance for Responsible and Scalable AI Adoption", publisher: Deloitte UK, type: firm, url: "https://www.deloitte.com/uk/en/services/audit-assurance/services/ai-assurance.html", date: 2026-10-16, access: full, locator: "pillar on technical build and performance; page undated, date is retrieval date" }
  last_reviewed: 2026-10-16
  notes: "Firm service description only. Step-level change inside a broader offer; overlaps with entries 06 and 08 but is a distinct testing activity."

- id: assurance-assurance-over-ai-08
  title: Assurance suite for audit and non-audit clients spanning AI diagnostics, governance, risk management and controls (EY)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: As organisations embed AI, they need independent views of readiness and AI-related risk; the market uses "AI audit" and "AI assurance" loosely for very different assessments.
  solution: EY's 7 Apr 2026 global release says its updated audit methodology and frameworks underpin a suite of assurance services for audit and non-audit clients spanning AI diagnostics, governance, risk management and controls, and notes that the complexities of providing assurance on AI are dynamic and still emerging. An EY article written with ACCA sorts AI assessments into governance, conformity and performance assessments and recommends that each state what is assessed, use a clear methodology and suitable criteria, and be done by a suitably qualified provider.
  outcomes:
    - lever: growth
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: EY-CANVAS-2026
  prerequisites:
    - Clear scope and criteria (EY's own recommendation in EY-AIASSESS-2025).
  risks_and_guardrails:
    - The same suite is offered to audit clients, which raises auditor-independence questions routed to acceptance-independence.
    - EY notes that some assessments give explicit opinions and others only a summary of procedures (EY-AIASSESS-2025), so buyers need to read the report type.
  human_checkpoints:
    - not stated
  role_evolution: not stated beyond the release's statement that human judgement and scepticism stay central.
  evidence_grade: C
  sources:
    - { ref: EY-CANVAS-2026, title: "EY launches enterprise-scale agentic AI to redefine the audit experience for the AI era", publisher: EY, type: firm, url: "https://www.ey.com/en_ca/newsroom/2026/04/ey-launches-enterprise-scale-agentic-ai-to-redefine-the-audit-experience-for-the-ai-era", date: 2026-04-07, access: full, locator: "headline bullets; section 'Supporting organizations through their own transformation journeys'" }
    - { ref: EY-AIASSESS-2025, title: "How AI assessments can enhance confidence in AI", publisher: EY (written with ACCA), type: firm, url: "https://www.ey.com/en_ca/insights/public-policy/how-ai-assessments-can-enhance-confidence-in-ai", date: 2025-08, access: full, locator: "sections 'Understanding the AI assessment landscape' and 'Next steps for business leaders'; month from trade-press coverage dated 5 Aug 2025 (search result)" }
  last_reviewed: 2026-10-16
  notes: "Announcement language only; the release does not describe scope, criteria or named clients."

- id: assurance-assurance-over-ai-09
  title: Agent certification by adversarial testing with insurance backing (AIUC-1, audited by Schellman and others)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: Enterprises will not deploy AI agents without evidence that guardrails hold against jailbreaks, hallucination, data leakage and unauthorised actions, and generic governance frameworks do not test that.
  solution: AIUC-1 is a security, safety and reliability standard for AI agents, audited with a large automated adversarial test programme and retesting, and linked to insurance cover. Schellman, a SOC audit firm and the first ANAB-accredited ISO/IEC 42001 body, became the first authorized auditor on 3 Feb 2026. On 27 Aug 2026 KPMG LLP announced AIUC-1 certification of its aIQ Capture platform after more than 900 technical tests. AIUC lists Cursor, Fin, ElevenLabs, Harvey, UiPath and KPMG as certified, and its release names Lovable.
  outcomes:
    - lever: risk
      description: Number of technical tests run against KPMG's aIQ Capture before certification.
      figure: "900+"
      measures: "technical tests of the aIQ Capture agentic platform covering hallucinations, high-risk domain interactions, content safety, prompt injection and other scenarios (joint KPMG/AIUC release)"
      provenance: vendor-published
      source_ref: AIUC-KPMG-2026
    - lever: risk
      description: ElevenLabs obtained the first AIUC-1-backed insurance policy, reported with a coverage limit.
      figure: "$50 million"
      measures: "coverage on the first AIUC-1-backed policy (ElevenLabs), for risks such as hallucination-driven loss, data leakage and faulty tool actions, as reported by Forkast"
      provenance: vendor-published
      source_ref: FORKAST-AIUC-2026
    - lever: quality
      description: UiPath's head of GRC says testing produced new guardrails the company can show customers (qualitative).
      figure: none published
      measures: qualitative customer quote on the AIUC-1 website
      provenance: vendor-published
      source_ref: AIUC-SERIES-A-2026
  prerequisites:
    - An agentic product to test, with logging and guardrails in place.
    - Willingness to be retested; Forkast reports quarterly retests to keep certification valid.
  risks_and_guardrails:
    - Test counts measure activity, not residual risk; Forkast notes it is unknown how insurance policies would perform in a systemic failure.
    - Consortium size and auditor model are changing (Schellman's Feb 2026 release says 60+ security leaders; AIUC's Aug 2026 release and homepage say 250+).
  human_checkpoints:
    - Authorised auditor reviews guardrail implementation and red-team results (AIUC website describes a 50+ page independent audit report).
  role_evolution: SOC auditors add AI red-team and agent-testing capability; Big Four firms appear as certified organisations first and "open the door to a broader assurance relationship" (AIUC co-founder quoted in AIUC-KPMG-2026).
  evidence_grade: B
  sources:
    - { ref: SCHELLMAN-AIUC-2026, title: "Schellman Becomes the First Accredited Auditor for AIUC-1, the Security Standard for AI Agents", publisher: Schellman, type: vendor, url: "https://www.schellman.com/blog/news/schellman-becomes-the-first-accredited-auditor-for-aiuc-1", date: 2026-02-03, access: full, locator: "release body; the body text says 'authorized auditor'" }
    - { ref: AIUC-KPMG-2026, title: "KPMG LLP Becomes First Big Four Firm with AIUC-1 Certified AI Capability", publisher: AIUC, type: vendor, url: "https://aiuc.com/updates/kpmg-llp-becomes-first-big-four-firm-with-aiuc-1-certified-ai-capability", date: 2026-08-27, access: full, locator: "paragraphs 2-5" }
    - { ref: AIUC-SERIES-A-2026, title: "Series A to build the confidence infrastructure for frontier AI (and AIUC-1 certified-agents page)", publisher: AIUC, type: vendor, url: "https://aiuc.com/updates/series-a-announcement", date: 2026-09-15, access: full, locator: "post body; customer quotes are on https://www.aiuc-1.com/ (opened, undated)" }
    - { ref: FORKAST-AIUC-2026, title: "AIUC Raises $40M to Build the Certification and Insurance Layer That Makes Agent Governance Auditable", publisher: Forkast, type: press, url: "https://forkast.news/aiuc-raises-40m-to-build-the-certification-and-insurance-layer-that-makes-agent-governance-auditable/", date: 2026-09-16, access: full, locator: "paragraphs 4-6 and closing paragraph" }
  last_reviewed: 2026-10-16
  notes: "Not an audit-firm product in origin; included because Schellman (an attestation firm) and KPMG are in it and it shows a testing-led, insured alternative to management-system certification. AIUC's homepage later says it raised $55M, above the $40M Series A; the later round was not dated. Ladder is augment because automated adversarial tests run under auditor oversight; AI remains the subject."

- id: assurance-assurance-over-ai-10
  title: Registry-based AI trust mark combining automated self-assessment scoring with an accredited ISO/IEC 42001 certificate (CSA STAR for AI)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Vendor-risk teams get long bespoke AI questionnaires and cannot compare suppliers' claims.
  solution: Per the CSA research note, STAR for AI Level 1 is a self-assessment against the AI-CAIQ, with an enhanced Level 1 once the self-assessment passes an automated scoring system; Level 2 (introduced Nov 2025) requires that scored self-assessment plus an accredited third-party ISO/IEC 42001 certification. The note says AIUC-1 was added to the STAR registry on 30 Jun 2026. Coalfire, a CSA STAR auditor-type vendor, describes the AI Controls Matrix (243 control objectives across 18 domains).
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: CSA-AIASSURE-2026
  prerequisites:
    - Completed AI-CAIQ; for Level 2, an accredited ISO/IEC 42001 certificate.
  risks_and_guardrails:
    - CSA (a trade body that also runs the scheme) wrote the note; its figures on EU notified-body capacity come from a secondary source (eyreACT) and are unverified.
    - The landscape reports the note says it was generated with AI assistance and not reviewed by CSA; that disclosure was not found on the web page opened here, so treat the note as a lead.
  human_checkpoints:
    - Third-party certification body at Level 2.
  role_evolution: not stated
  evidence_grade: C
  sources:
    - { ref: CSA-AIASSURE-2026, title: "Who Assures the Assurers? Third-Party AI Assessment Standards", publisher: Cloud Security Alliance Labs, type: professional-body, url: "https://labs.cloudsecurityalliance.org/research/csa-research-note-third-party-ai-assurance-standards-2026092/", date: 2026-09-27, access: full, locator: "paragraphs 3-5 and reference list; date from the document file name" }
    - { ref: COALFIRE-STAR-2025, title: "Enhancing Trust in AI: An Overview of AI Certification with the Cloud Security Alliance (CSA)", publisher: Coalfire, type: vendor, url: "https://coalfire.com/the-coalfire-blog/enhancing-trust-in-ai-an-overview-of-ai-certification-with-the-cloud-security-alliance-csa", date: 2025-08-29, access: full, locator: "section 'Introducing CSA STAR for AI'" }
  last_reviewed: 2026-10-16
  notes: "No named STAR for AI certified organisation was found. Change scope is process because scoring is automated and layered on a certificate."

- id: assurance-assurance-over-ai-11
  title: "Idea: bundle ISO/IEC 42001 with ISO/IEC 27001 and other certifications in one engagement"
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: AI systems touch security, privacy, resilience and data integrity, so separate audits duplicate evidence requests.
  solution: Schellman's CEO said in Oct 2024 that, although ISO/IEC 42001 certification is available alone, she expects it will usually be bundled with other certifications such as ISO/IEC 27001. The idea is that one audit team re-uses evidence across schemes.
  outcomes:
    - lever: cost
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: SCHELLMAN-AT-2024
  prerequisites:
    - A certification body accredited for each scheme.
  risks_and_guardrails:
    - Impartiality rules limit combining consultancy with certification of the same management system (BSI-ANAB-2026).
  human_checkpoints:
    - not stated
  role_evolution: Auditors cover several schemes per engagement (implied; not stated by the source).
  evidence_grade: D
  sources:
    - { ref: SCHELLMAN-AT-2024, title: "Inside Schellman's journey to provide certification for ISO 42001 AI framework", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/inside-schellmans-journey-to-provide-certification-for-iso-42001-ai-framework", date: 2024-10-28, access: full, locator: "paragraph beginning 'While technically 42001 certification is now available as a standalone service'" }
  last_reviewed: 2026-10-16
  notes: "Idea. A practitioner's expectation in 2024; no later evidence found that bundled audits are sold or priced."

- id: assurance-assurance-over-ai-12
  title: Regulatory-compliance and conformity assurance over AI (EU AI Act, DSA audits)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: Providers of high-risk AI systems and very large online platforms face conformity-assessment or independent-audit duties and need help showing compliance.
  solution: Deloitte UK offers objective third-party challenge over compliance with the EU AI Act (including conformity assessment for high-risk systems), the AI-specific aspects of wider digital regulation including the independent audit, and sector rules. Under Article 43, providers of Annex III point 1 systems may choose internal control or a notified-body route; providers of points 2 to 8 follow the internal-control procedure.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: DELOITTE-AIA-UK-2026
  prerequisites:
    - A determination of whether a system is high-risk and which conformity route applies.
    - Notified bodies designated for the relevant category (capacity is reported to be limited; see notes).
  risks_and_guardrails:
    - Article 43(2) means most Annex III categories use internal control, which limits mandatory third-party demand (AIACT-ART43-2024).
    - The CSA note cites a secondary source that few if any bodies were fully designated by early 2026; not verified (CSA-AIASSURE-2026).
  human_checkpoints:
    - Notified body assessment where required.
  role_evolution: not stated
  evidence_grade: C
  sources:
    - { ref: DELOITTE-AIA-UK-2026, title: "AI Assurance for Responsible and Scalable AI Adoption", publisher: Deloitte UK, type: firm, url: "https://www.deloitte.com/uk/en/services/audit-assurance/services/ai-assurance.html", date: 2026-10-16, access: full, locator: "compliance pillar; page undated, date is retrieval date" }
    - { ref: AIACT-ART43-2024, title: "Article 43: Conformity Assessment (Regulation (EU) 2024/1689)", publisher: artificialintelligenceact.eu (unofficial text), type: regulator, url: "https://artificialintelligenceact.eu/article/43/", date: 2024-06-13, access: full, locator: "paragraphs 1 and 2; date is the Regulation's adoption date; site annotation says Article 43 comes into force 2 Aug 2026" }
  last_reviewed: 2026-10-16
  notes: "Application dates of EU AI Act provisions may have changed after the text was adopted; the site annotation is not a primary source and was not cross-checked."

- id: assurance-assurance-over-ai-13
  title: Independent algorithmic bias audits under New York City Local Law 144
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Employers using automated employment decision tools must obtain annual independent bias audits, but the law leaves "auditor" and "tool" loosely defined.
  solution: Since July 2023 NYC employers using automated employment decision tools have had to undergo annual bias audits by an independent auditor. An interview study of 16 experts and practitioners found that auditors, tool vendors and employers defined practice themselves, producing four distinct auditor roles, and concluded the law has not established an effective audit regime.
  outcomes:
    - lever: quality
      description: Independent researchers judged the regime not effective at protecting applicants; key terms undefined, data access hard for auditors, and disagreement over who is a legitimate auditor.
      figure: "16"
      measures: "experts and practitioners interviewed within the New York City Local Law 144 regime"
      provenance: independent
      source_ref: GROVES-2024
  prerequisites:
    - Access to tool outputs and demographic data (data access is named as a barrier).
  risks_and_guardrails:
    - Undefined independence and scope let buyers and vendors narrow the audit (GROVES-2024).
  human_checkpoints:
    - Independent auditor signs the bias audit.
  role_evolution: Four auditor roles emerged because there was no agreed definition of a legitimate auditor (GROVES-2024).
  evidence_grade: B
  sources:
    - { ref: GROVES-2024, title: "Auditing Work: Exploring the New York City algorithmic bias audit regime", publisher: arXiv (Groves, Metcalf, Kennedy, Vecchione, Strait), type: academic, url: "https://arxiv.org/abs/2402.08101", date: 2024-02-12, access: full, locator: abstract" }
  last_reviewed: 2026-10-16
  notes: "Qualitative study, no audit outcome statistics and no named audit firms. Included as the best independent evidence of how algorithmic audits work in a live mandatory regime. Date is the arXiv submission date."

- id: assurance-assurance-over-ai-14
  title: Financial-statement auditor determines whether and how the entity relies on AI in financial reporting and controls
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Entities use AI directly or indirectly in accounting and reporting, and auditors need to know the extent of reliance to scope risk assessment, team competence and evidence.
  solution: The AICPA practice aid (13 Oct 2026) asks the auditor to establish early the extent to which the company relies on AI in financial reporting, how AI differs from ordinary automation, how data quality affects reliability, whether the team has the right blend of audit, AI and data skills, and what new risks arise (data, model, hallucination, explainability, bias, drift). Accounting Today's account says heavy AI reliance may resemble use of complex valuation models, and may reveal a lack of management competence. COSO's definition of AI reliance (management depends on AI output without re-performing or independently validating it) is used by BDO to separate reliance from non-reliance.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: independent
      source_ref: AICPA-PA-2026
  prerequisites:
    - Understanding of the entity's AI use, governance and the people who decide whether to rely on an AI output.
    - Team with AI, data and specialist support (AICPA-PA-2026).
  risks_and_guardrails:
    - The aid is non-authoritative guidance; the auditor remains responsible for the opinion (AICPA-PA-2026).
    - AI agents may run without traceable workflows, which can limit evidence gathering (AT-AICPAPA-2026).
  human_checkpoints:
    - Engagement partner judgement on acceptance and on whether AI use affects financial reporting.
  role_evolution: Audit teams add data and AI skills and specialist support; the aid says the blend of auditing expertise, AI knowledge, data skills and scepticism may be needed (AICPA-PA-2026).
  evidence_grade: C
  sources:
    - { ref: AICPA-PA-2026, title: "AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing", publisher: AICPA & CIMA, type: standard-setter, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: 2026-10-13, access: full, locator: "section 'Considering an organization's use of AI'; full practice aid behind AICPA login, not read" }
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "paragraphs on acceptance and continuance, understanding the entity and risk assessment" }
    - { ref: BDO-ITGC-2026, title: "Artificial Intelligence: IT Audit Considerations with Focus on Information Technology General Controls", publisher: BDO USA, type: firm, url: "https://www.bdo.com/getmedia/2444fe7c-c0fc-4c8e-9b2f-6ca3032eaf54/AASSR-TPA-IT-Audit-Considerations-insight-V-1.pdf?ext=.pdf", date: 2026-07, access: full, locator: "reliance versus non-reliance section; date from PDF creation metadata (28 Jul 2026) and web page (20 Jul 2026)" }
  last_reviewed: 2026-10-16
  notes: "Guidance, not a deployment. Detail on the aid beyond the AICPA release comes from Accounting Today's article because the aid itself needs a login. Placeholder fields as above."

- id: assurance-assurance-over-ai-15
  title: Evidence strategy for AI-operated controls (test the outputs, test controls, or test around the AI)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: A control that runs through a probabilistic model cannot be tested like a deterministic automated control, and some AI is bought from third parties whose internals the auditor cannot inspect.
  solution: The AICPA aid says an auditor may be able to substantively test AI outputs; if that alone is not sufficient, the auditor designs tests of controls, and the strategy for controls operated by AI may differ from that for traditional automated controls because models can learn, drift and give probabilistic results. KPMG's SOX 2030 paper states that SOX programmes have largely avoided AI-related material weaknesses so far because they are still testing "around" the AI, relying on manual and other automated controls, and expects reliance to become unavoidable, with a first wave of material weaknesses in 2027. KPMG says its paper cites the lack of widely accepted methods for auditing black-box systems as an open challenge.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: KPMG-SOX-2026
  prerequisites:
    - Evidence the entity has designed controls over data quality, model performance and safeguards (AT-AICPAPA-2026).
    - Output validation methods; the COSO roadmap lists performance testing, multi-model validation, data analytics monitoring and third-party validation as evolving approaches (KPMG-COSO-2026).
  risks_and_guardrails:
    - A human approval step that rubber-stamps every AI recommendation provides no real control value (KPMG-SOX-2026).
    - Protiviti, quoted in a legal-industry blog, says AI-driven workforce reductions can weaken controls such as segregation of duties, so controls may be an afterthought in AI planning (TCC-ICFR-2026).
  human_checkpoints:
    - Meaningful human review of AI recommendations, where the reviewer is competent and has real authority.
  role_evolution: Internal audit and SOX teams must define what meaningful oversight means for AI-operated controls (KPMG-SOX-2026).
  evidence_grade: C
  sources:
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "paragraphs on how auditors should respond to risks" }
    - { ref: KPMG-SOX-2026, title: "The Future of SOX: 2030 Point of View", publisher: KPMG US, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026-09, access: full, locator: "pp.5-6 ('A new SOX frontier: auditing AI itself'; 'The first AI-related material weaknesses'); 'Challenges on the horizon'; date from PDF creation metadata (23 Sep 2026)" }
    - { ref: KPMG-COSO-2026, title: "COSO releases GenAI roadmap", publisher: KPMG US, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/frv/pdf/2026/coso-releases-gen-ai-roadmap.pdf", date: 2026-05-01, access: full, locator: "pp.2-3, 'Interaction with the KPMG Guide'" }
    - { ref: TCC-ICFR-2026, title: "Your 2026 Audit Committee Agenda: ICFR During AI Transformations", publisher: TheCorporateCounsel.net, type: press, url: "https://www.thecorporatecounsel.net/blog/2026/02/your-2026-audit-committee-agenda-icfr-during-ai-transformations.html", date: 2026-02-06, access: full, locator: "Protiviti quotation in the second half of the post" }
  last_reviewed: 2026-10-16
  notes: "Firm statements of expectation, not measurements. The KPMG 2027 material-weakness expectation is a forecast. No inspection finding on auditors' reliance on AI-operated controls was found."

- id: assurance-assurance-over-ai-16
  title: Extend ITGC scoping and testing to AI components and to AI agents' access to in-scope systems
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Traditional ITGCs cover databases and operating systems, but AI models, data pipelines and agents add components and access paths that are not tested by default.
  solution: BDO's paper tells auditors to map AI use, then for each component (the model, data pipelines, orchestration software, agents) assess risk and scope which ITGCs apply, noting that ITGCs matter far more where management relies on AI output. It separates AI-specific risk considerations (input data, output reliability, drift) from ITGC implications (access, change management, operations) and gives an example check: whether ERP user access reviews cover AI agents' access. The AICPA aid adds that traditional ITGCs may not address all AI-specific risks, and that where AI is bought from a third party, alternative procedures such as a SOC report may be needed.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: BDO-ITGC-2026
  prerequisites:
    - An inventory of AI components and service providers behind each in-scope process.
    - IT audit specialists who understand cloud and SaaS AI architectures.
  risks_and_guardrails:
    - Relevant ITGCs may sit with a third-party provider, so access to evidence depends on the contract and service-organisation reports (BDO-ITGC-2026; AT-AICPAPA-2026).
    - The IFIAR 2025 report (carried from the landscape; not re-opened) found ITGC testing weaknesses common in tool-assisted audits.
  human_checkpoints:
    - IT audit specialist judgement on which components are in scope.
  role_evolution: IT audit specialists add AI knowledge; ISACA created the AAIA credential for IT auditors and advisors (see entry 19).
  evidence_grade: C
  sources:
    - { ref: BDO-ITGC-2026, title: "Artificial Intelligence: IT Audit Considerations with Focus on Information Technology General Controls", publisher: BDO USA, type: firm, url: "https://www.bdo.com/getmedia/2444fe7c-c0fc-4c8e-9b2f-6ca3032eaf54/AASSR-TPA-IT-Audit-Considerations-insight-V-1.pdf?ext=.pdf", date: 2026-07, access: full, locator: "ITGC domains and component list on pp.1-2" }
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "paragraph on traditional general IT controls" }
  last_reviewed: 2026-10-16
  notes: "A firm thought-leadership paper. The landscape recommended folding IT-audit work for AI components into this module."

- id: assurance-assurance-over-ai-17
  title: Rely on service-auditor (SOC) reports and management representations for AI provided by a service organisation
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: When an entity uses a service organisation's AI, or that organisation uses AI inside its system, the user auditor often cannot inspect the AI directly.
  solution: The AICPA aid says a service auditor's report often becomes important audit evidence in this situation; if it is insufficient, further procedures may include obtaining AI-related representations from management, such as which AI the entity uses. The AICPA also points to separate guidance on how service organisations' AI use affects SOC 1 and SOC 2 engagements.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: independent
      source_ref: AT-AICPAPA-2026
  prerequisites:
    - A SOC report whose system description and criteria reach the AI in scope; the CSA note says no AI-specific Trust Services Criteria exist (carried from the landscape, not re-read).
  risks_and_guardrails:
    - Reliance depends on whether the report covers model-specific properties; a SOC 2 Type II reliably covers conventional IT general controls, not model behaviour, according to the CSA note cited in the landscape (not re-read here).
  human_checkpoints:
    - User auditor evaluation of the service auditor's report.
  role_evolution: SOC teams must decide whether and how AI is in the system description (routed detail in other-assurance).
  evidence_grade: C
  sources:
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "paragraph on service organizations" }
    - { ref: AICPA-PA-2026, title: "AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing", publisher: AICPA & CIMA, type: standard-setter, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: 2026-10-13, access: full, locator: "section 'Additional AI-related guidance'" }
  last_reviewed: 2026-10-16
  notes: "TQA 9561 text is behind a login and was not read. Detail comes from trade-press summary of the practice aid."

- id: assurance-assurance-over-ai-18
  title: Internal audit and SOX teams map AI controls with the COSO GenAI capability taxonomy and add AI systems to the audit universe
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Organisations lack an agreed way to say what good internal control over generative AI looks like, so auditors have no common benchmark.
  solution: COSO's February 2026 roadmap groups GenAI use into eight capability types, each with examples, minimum control expectations aligned to the five COSO components and illustrative metrics for monitoring and audit evidence, plus starter templates such as risk matrices and control-testing procedures. EY's commentary recommends that chief audit executives explicitly include AI systems with ICFR impact in the audit universe, with scope following where judgement occurs. The IIA published an AI Auditing Framework (13 Sep 2024) for internal auditors.
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: not applicable
      provenance: independent
      source_ref: COSO-GENAI-2026
  prerequisites:
    - An AI inventory with the capability types identified for each system.
    - Control owners for each capability (COSO text on accountability).
  risks_and_guardrails:
    - KPMG notes the roadmap is guidance to apply the 2013 framework, not a new formal framework or a complete list of risks and controls (KPMG-COSO-2026).
    - The eighth capability's name differs between sources: the COSO PDF and CAQ use "knowledge retrieval and summarization"; the Journal of Accountancy says "regulatory intelligence". The COSO PDF is treated as correct.
  human_checkpoints:
    - Control owners and reviewers with competence and independence (COSO text on reviewers).
  role_evolution: Internal audit takes on AI governance assurance; the IIA framework helps internal auditors identify AI risks and the controls to manage them (IIA-AIFW-2024).
  evidence_grade: C
  sources:
    - { ref: COSO-GENAI-2026, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf", date: 2026-02, access: full, locator: "capability table, 'AI reliance' working definition, control sections by COSO principle; copy hosted by a Spanish internal-audit body; release date 23 Feb 2026 per KPMG-COSO-2026" }
    - { ref: JOFA-COSO-2026, title: "COSO creates audit-ready guidance for governing generative AI", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/", date: 2026-02-26, access: full, locator: "bullets on capability taxonomy and audit-ready control mapping" }
    - { ref: EY-COSO-2026, title: "COSO 2026 and the shift in AI governance", publisher: EY, type: firm, url: "https://www.ey.com/en_us/cro-risk/coso-2026-and-the-shift-in-ai-governance", date: 2026-06-24, access: full, locator: "internal audit section on audit universe and judgement" }
    - { ref: IIA-AIFW-2024, title: "The IIA's Artificial Intelligence Auditing Framework", publisher: The IIA, type: professional-body, url: "https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/", date: 2024-09-13, access: full, locator: "'What is The IIA's updated AI Auditing Framework?'" }
  last_reviewed: 2026-10-16
  notes: "Guidance only; no named internal audit function was found applying the taxonomy. In-house internal audit overlaps this module."

- id: assurance-assurance-over-ai-19
  title: AI-audit credentials and competence requirements for assurance teams
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: in-production
  problem: Few auditors have AI skills, and certification bodies and assurance providers must show competence; an ICAEW-reported view in 2025 was that more assurers were working out what to do than doing it.
  solution: ISACA offers an Advanced in AI Audit (AAIA) certification for holders of CISA or another qualified designation (including CIA, CPA, ACCA, ICAEW ACA/FCA), with domains in AI governance and risk, AI operations and AI auditing tools and techniques. ISO/IEC 42006 requires certification-body audit teams to hold collective competence across AI, management systems, auditing, AI governance and relevant law, as reported by a compliance vendor. Deloitte's Singapore posting hires juniors who are expected to deepen ISO/IEC 42001 expertise on the job.
  outcomes:
    - lever: capacity
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: ISACA-AAIA-2026
  prerequisites:
    - A qualifying designation (ISACA); a team structure that spans AI and auditing skills.
  risks_and_guardrails:
    - The ICAEW article quotes a practitioner who asks what assurers are being measured against.
  human_checkpoints:
    - Exam and experience requirements (ISACA); competence review by the accrediting body (ISO/IEC 42006).
  role_evolution: Existing IT auditors, internal auditors and accountants add AI audit credentials; junior hires work under senior review (DELOITTE-JOB-SG-2026).
  evidence_grade: B
  sources:
    - { ref: ISACA-AAIA-2026, title: "AAIA Certification: ISACA Advanced in AI Audit", publisher: ISACA, type: professional-body, url: "https://www.isaca.org/credentialing/aaia", date: 2026-10-16, access: full, locator: "eligibility and domain sections; page undated, date is retrieval date" }
    - { ref: ICAEW-AIASSURE-2025, title: "Where are we now with AI assurance?", publisher: ICAEW Insights, type: professional-body, url: "https://icaew.com/insights/viewpoints-on-the-news/2025/mar-2025/where-are-we-now-with-ai-assurance", date: 2025-03-04, access: full, locator: "section 'Fundamental start line'" }
    - { ref: BRIGHT-42006-2026, title: "ISO 42006 Raises the Bar for ISO 42001 Certifiers", publisher: Bright Defense, type: vendor, url: "https://brightdefense.com/news/iso-42006-raises-the-bar-for-iso-42001-certifiers", date: 2026-09-14, access: full, locator: "section 'What Competence Does ISO 42006 Require'" }
  last_reviewed: 2026-10-16
  notes: "No counts of credential holders or audit teams were found. The credential exists and is open for registration, but how many assurance engagements it staffs is unknown."
```

---

## 3. Module notes

### Processes and key steps (with work types)

*Assurance over AI systems (AI is the subject)*
1. Scope the system, its boundary and the criteria (ISO/IEC 42001 clauses and Annex A, Trust Services Criteria plus AI objectives, AIUC-1, or a bespoke set). `expert-judgment`.
2. Readiness or gap assessment against the chosen standard; build the AI inventory, risk register and policy set. `review-assurance`, `document-production`.
3. Design-effectiveness test of governance and controls. `review-assurance`.
4. Operating-effectiveness test over a period (KPMG UK's "operating effectively – embedded in practice and monitored"). `review-assurance`.
5. Technical testing: adversarial or red-team tests, performance and bias tests (AIUC-1; Deloitte UK technical-build pillar). `review-assurance`, `software-systems`.
6. Report, opinion or certificate decision. `document-production`. For certification, a three-year cycle appears on the EY Japan page, and the EY S.p.A. certificate runs from 23 Oct 2025 to 22 Oct 2028.
7. Accreditation of the certifying body (witness audits, office visit, ISO/IEC 42006 competence and audit-time rules). `review-assurance`.

*Auditing the entity's AI in a financial-statement or ICFR audit*
1. Acceptance and continuance: how much the entity relies on AI; ability to gather evidence (routed detail in acceptance-independence). `expert-judgment`.
2. Understand the entity, its AI use and governance; identify who decides whether to rely on AI outputs. `research-synthesis`.
3. Risk assessment: data, model, hallucination, explainability, bias, drift, cyber. `review-assurance`.
4. Scope controls and ITGCs by AI component, separating reliance from non-reliance cases. `review-assurance`.
5. Choose evidence: substantive test of outputs, tests of controls, SOC reports, representations. `review-assurance`.
6. Evaluate deficiencies and communicate (KPMG expects the first AI-related material weaknesses in 2027). `document-production`.

### Common pain points
- **Criteria are not settled.** An ICAEW-reported practitioner view (Mar 2025): assurers are still working out what they are assuring for or against (ICAEW-AIASSURE-2025). EY and ACCA say the same term "audit" or "assurance" covers very different assessments (EY-AIASSESS-2025).
- **Who assures the assurers.** The CSA note argues certification schemes grew faster than accreditation of the certifiers, and that the supplier base grew from 17 to 84 specialised UK firms in one year (CSA-AIASSURE-2026, citing DSIT-ASSURANCE-2024).
- **Access and proprietary models.** Schellman's CEO says early certification rules asked for algorithm transparency, which clients rarely accept (SCHELLMAN-AT-2024). NYC auditors struggled to get data (GROVES-2024). A survey of 35 AI-audit practitioners found tooling supports evaluation but not accountability goals (OJEWALE-2025, abstract).
- **Black-box controls.** KPMG says widely accepted methods for auditing black-box systems do not exist (KPMG-SOX-2026).
- **Third-party AI.** An auditor's ability to perform procedures may be limited when AI is purchased (AT-AICPAPA-2026).
- **Weak independent evidence of what audits achieve.** Birhane et al. find only a subset of AI audit studies translate into accountability outcomes (BIRHANE-2024).

### Metrics and benchmarks (with sources)
- UK AI assurance market: 524 firms supplying AI assurance goods and services, 84 specialised (17 in the 2023 AI Sector Study), est. GVA £1.01bn, 12,572 employees; market could exceed £6.53bn by 2035 if opportunities are realised (DSIT-ASSURANCE-2024, summary paragraphs; ICAEW-AIASSURE-2025 repeats the £1.01bn as "revenues", which DSIT calls GVA).
- Schellman: 26 signed clients for ISO/IEC 42001 in Oct 2024 (SCHELLMAN-AT-2024); accreditation took about eight months.
- BSI research: 26% of organisations report taking steps to align with ISO/IEC 42001 (BSI-ANAB-2026; sample not stated).
- KPMG aIQ Capture: 900+ technical tests for AIUC-1 (AIUC-KPMG-2026). AIUC-1 overall: 5,000 adversarial tests (Forkast); $50M ElevenLabs policy.
- KPMG SOX survey context (not AI-specific): SOX control maintenance cost up 45% between the 2023 and 2025 surveys; testing hours per control up from 12 (FY2022) to 16 (FY2024) (KPMG-SOX-2026, p.4). Useful for the cost side of any AI-in-ICFR business case.
- Routed, not for this module: KPMG UK testing-time reduction of about 18% from AI-assisted controls assurance (see section 4).
- **No fee, price, margin, certificate-count or measured audit-quality figures for assurance over AI were found.** Pricing and demand remain unquantified beyond the items above.

### Guardrails and regulatory points
- ISAE (UK) 3000 is the cited basis for KPMG UK's product (KPMGUK-GOVAI-2026). IAASB/ISSA material was not found to address AI.
- ISO/IEC 42006:2025 sets requirements for CBs, adding AI competence and audit-time rules (BRIGHT-42006-2026, secondary); the primary page returned 403.
- Accredited bodies cannot certify a system they or a group affiliate consulted on (BSI-ANAB-2026). KPMG's release carries the line that some services may not be permissible for audit clients (KPMGUS-ISO-2025).
- EU AI Act Art. 43: providers of Annex III points 2 to 8 follow internal control; third-party notified-body routes apply to point 1 (biometrics) and product-embedded systems (AIACT-ART43-2024).
- AICPA practice aid and COSO roadmap are non-authoritative guidance; KPMG stresses COSO's roadmap is not a new framework (KPMG-COSO-2026).
- Unverified for this module: PCAOB and IFIAR statements about auditors' use of AI tools (landscape items), which concern firm tools rather than assurance over client AI.

### Frontier signals (dated and sourced)
- 2025-11-20: a European accreditation body vote to make ISO/IEC 42006 mandatory for accrediting AIMS certifiers (BRIGHT-42006-2026, secondary source; not verified at the primary).
- 2026-02-03: Schellman named first authorised AIUC-1 auditor (SCHELLMAN-AIUC-2026).
- 2026-02-23: COSO publishes GenAI roadmap (KPMG-COSO-2026).
- 2026-03-10: BSI adds ANAB accreditation (BSI-ANAB-2026).
- 2026-04-07: EY announces an assurance suite for audit and non-audit clients spanning AI diagnostics, governance, risk and controls (EY-CANVAS-2026).
- 2026-08-27: KPMG LLP first Big Four AIUC-1 certification (AIUC-KPMG-2026).
- 2026-09-15: AIUC raises a $40M Series A (AIUC-SERIES-A-2026).
- 2026-09: KPMG says a "new mandate" to assure AI systems themselves will emerge and expects the first wave of AI-related material weaknesses in 2027 (KPMG-SOX-2026, pp.5-6).
- 2026-10-13: AICPA says further sections on risk of material misstatement and audit evidence for AI-using entities will be added (AICPA-PA-2026).

### Workforce and role effects
- Assurance providers hire AI-assurance consultants at 2-4 years' experience and train on the job (DELOITTE-JOB-SG-2026).
- SOC audit firms (Schellman) and certification bodies (BSI, SGS) are the visible early movers; Big Four firms gain credibility by certifying themselves first.
- IT auditors and accountants can add ISACA's AAIA (ISACA-AAIA-2026). ISO/IEC 42006 expects team-level competence in AI, management systems, auditing and law (BRIGHT-42006-2026).
- Auditors of financial statements need teams combining audit, AI and data skills with specialist support (AICPA-PA-2026).

### Objections and concerns practitioners raise
- Accreditation and competence lag the market (CSA-AIASSURE-2026; lead source).
- The NYC regime shows what happens when "independent auditor" is undefined (GROVES-2024).
- Demand is limited by weak buyer understanding (DSIT-ASSURANCE-2024); ICAEW's interviewee notes there is no insurance-driven requirement yet for AI assurance (ICAEW-AIASSURE-2025). AIUC's insurance link is a new counter-example (FORKAST-AIUC-2026), with unproven payout behaviour.
- Rubber-stamp human oversight offers no control value (KPMG-SOX-2026).
- AI-driven workforce cuts can weaken segregation of duties (Protiviti, via TCC-ICFR-2026).
- Independence of firms selling AI assurance or readiness to audit clients (KPMGUS-ISO-2025; EY-CANVAS-2026).

### Interview probes for an advisor
1. When a client asks for AI assurance, who is the buyer (procurement, board, regulator, insurer), what triggered it, and would they have bought it without a customer demand?
2. For an AI management system or governance audit, how do you scope audit time and team competence, and what share of engagements need technical testing as well as document and control review?
3. In ICFR audits, where have you met AI-operated controls or AI-generated information? Did you rely on them or test around them, and what evidence did you take (own testing, SOC reports, representations)?
4. What can you sell to an audit client (readiness, certification, attestation over AI), what safeguards separate consulting from certification, and how did you decide?
5. How do you price AI assurance compared with a SOC 2 examination, and what assurance level and report format do clients accept?

---

## 4. Routed to other modules

| Item | Target module | Why | Source |
|---|---|---|---|
| About 18% testing-time reduction in KPMG UK controls assurance using AI tools; one team's about 15% reduction with DataSnipper | controls-testing / other-assurance (SOC) | This is assurance done *with* AI, not assurance over AI. Firm-reported ("recent engagements"), no denominator stated. | KPMGUK-CONTROLS-2026, foreword and p.? (foreword; DataSnipper example in the engagement examples) |
| KPMG's views on synthetic data, agents stress-testing controls, 100% coverage in SOX | controls-testing | AI as a tool for control testing. | KPMG-SOX-2026, pp.8-10 |
| AI as an acceptance and continuance factor (reliance resembles complex valuation models; evidence gathering may be limited); independence of AI assurance sold to audit clients; certifier impartiality rules | acceptance-independence | Acceptance and independence analysis. | AT-AICPAPA-2026; KPMGUS-ISO-2025; BSI-ANAB-2026; EY-CANVAS-2026 |
| ISACA AAIA, "specialist support" in AICPA aid, AI-component ITGC specialists | specialists | Specialist competence and use of experts. | ISACA-AAIA-2026; AICPA-PA-2026 |
| Firms' own use of AI tools under quality management (AICPA aid Part 2) | quality-management | Firm-level tool governance, not assurance over client AI. | AICPA-PA-2026 |
| Effect of a service organisation's AI on SOC 1 and SOC 2 (TQA 9561); CSA's criticism of AI in SOC reports | other-assurance (SOC) | SOC engagement design. | AICPA-PA-2026 (mention only); CSA-AIASSURE-2026 |

---

## 5. Sources

Access `full` means opened and read; `search-only` means seen in search results, a landscape file or a blocked page only. Dates in brackets are retrieval dates for undated pages.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| KPMGUK-GOVAI-2026 | Independent confidence in how you govern AI | KPMG UK | firm | https://kpmg.com/uk/en/insights/audit/independent-confidence-in-how-you-govern-ai.html | 2026-09-22 | full |
| KPMGUK-CONTROLS-2026 | Reimagining Controls Assurance with AI | KPMG UK | firm | https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf | 2026-01 | full |
| KPMGUS-ISO-2025 | KPMG LLP Among First of the Big Four in the U.S. to Receive ISO 42001 AI Certification | KPMG US | firm | https://kpmg.com/us/en/media/news/kpmg-receives-iso-ai-certification.html | 2025-11-18 | full |
| KPMGINTL-ISO-2025 | KPMG International becomes first Big Four international entity to attain ISO 42001 certification | KPMG International | firm | https://kpmg.com/xx/en/media/press-releases/2025/12/kpmg-international-first-to-attain-iso-certification-for-ai-management-systems.html | 2025-12 | full |
| CONSULTINGCA-PWC-2026 | PwC launches new AI governance certification solution | Consulting.ca | press | https://www.consulting.ca/news/4859/pwc-canada-launches-new-ai-governance-certification-solution | 2026-02-16 | full |
| PWC-CA-ISO-2026 | PwC Canada launches AI governance certification (primary release) | PwC Canada | firm | https://www.pwc.com/ca/en/media/release/pwc-canada-iso-42001-ai-trust-certification.html | 2026-02 (10 Feb per search extract) | search-only (403) |
| SGS-PWCTW-2026 | PwC Taiwan Achieves ISO/IEC 42001 Certification | SGS | vendor | https://www.sgs.com/en/news/2026/06/pwc-taiwan-achieves-iso-iec-42001-ai-management-system-certification | 2026-06-15 | full |
| EYIT-CERT-2025 | Certificate 72849, EY S.p.A. | Certiquality via ey.com | firm | https://www.ey.com/content/dam/ey-unified-site/ey-com/it-it/campaigns/corporate-responsibilty/documents/ey-certificato-iso42001-eyspa-11-25.pdf | 2025-10-23 | full |
| EYIT-CERT-2026 | Certificate IT26-08316, EY Advisory S.p.A. | ACM Cert via ey.com | firm | https://www.ey.com/content/dam/ey-unified-site/ey-com/it-it/campaigns/corporate-responsibilty/documents/ey-eyadv-certificato-iso42001-4-26.pdf | 2026-04-20 | full |
| EYJP-CERTIFYPOINT-2026 | ISO/IEC 42001:2023 related services (Japanese) | EY Japan | firm | https://www.ey.com/ja_jp/services/technology-risk/iso-iec-42001-2023 | 2026 (page undated) | full |
| EY-CANVAS-2026 | EY launches enterprise-scale agentic AI... | EY | firm | https://www.ey.com/en_ca/newsroom/2026/04/ey-launches-enterprise-scale-agentic-ai-to-redefine-the-audit-experience-for-the-ai-era | 2026-04-07 | full |
| EY-AIASSESS-2025 | How AI assessments can enhance confidence in AI (with ACCA) | EY | firm | https://www.ey.com/en_ca/insights/public-policy/how-ai-assessments-can-enhance-confidence-in-ai | 2025-08 | full |
| EY-COSO-2026 | COSO 2026 and the shift in AI governance | EY | firm | https://www.ey.com/en_us/cro-risk/coso-2026-and-the-shift-in-ai-governance | 2026-06-24 | full |
| DELOITTE-42001-2025 | Navigating AI Assurance: Spotlight on ISO/IEC 42001 | Deloitte UK | firm | https://www.deloitte.com/uk/en/services/audit/blogs/navigating-ai-assurance-spotlight-on-iso-iec.html | 2025-10-07 | full |
| DELOITTE-AIA-UK-2026 | AI Assurance for Responsible and Scalable AI Adoption | Deloitte UK | firm | https://www.deloitte.com/uk/en/services/audit-assurance/services/ai-assurance.html | [2026-10-16] | full |
| DELOITTE-JOB-SG-2026 | A&A - SG - AI Assurance posting | Deloitte Singapore via Monster | job-posting | https://www.monster.co.th/job/a-a-sg-ai-assurance-deloitte-singapore-53507371 | 2026-06-25 | full |
| BDO-ITGC-2026 | AI: IT Audit Considerations with Focus on ITGCs | BDO USA | firm | https://www.bdo.com/getmedia/2444fe7c-c0fc-4c8e-9b2f-6ca3032eaf54/AASSR-TPA-IT-Audit-Considerations-insight-V-1.pdf?ext=.pdf | 2026-07 | full |
| KPMG-SOX-2026 | The Future of SOX: 2030 Point of View | KPMG US | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf | 2026-09 | full |
| KPMG-COSO-2026 | COSO releases GenAI roadmap | KPMG US | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/frv/pdf/2026/coso-releases-gen-ai-roadmap.pdf | 2026-05-01 | full |
| BSI-ANAB-2026 | BSI secures ANAB accreditation to certify ISO/IEC 42001 | BSI | vendor | https://www.bsigroup.com/en-US/insights-and-media/media-center/press-releases/2026/march/bsi-secures-anab-accreditation-to-certify-isoiec-42001/ | 2026-03-10 | full |
| BRIGHT-42006-2026 | ISO 42006 Raises the Bar for ISO 42001 Certifiers | Bright Defense | vendor | https://brightdefense.com/news/iso-42006-raises-the-bar-for-iso-42001-certifiers | 2026-09-14 | full |
| SCHELLMAN-AT-2024 | Inside Schellman's journey to provide certification for ISO 42001 | Accounting Today | press | https://accountingtoday.com/news/inside-schellmans-journey-to-provide-certification-for-iso-42001-ai-framework | 2024-10-28 | full |
| SCHELLMAN-AIUC-2026 | Schellman Becomes the First Accredited Auditor for AIUC-1 | Schellman | vendor | https://www.schellman.com/blog/news/schellman-becomes-the-first-accredited-auditor-for-aiuc-1 | 2026-02-03 | full |
| AIUC-KPMG-2026 | KPMG LLP Becomes First Big Four Firm with AIUC-1 Certified AI Capability | AIUC | vendor | https://aiuc.com/updates/kpmg-llp-becomes-first-big-four-firm-with-aiuc-1-certified-ai-capability | 2026-08-27 | full |
| AIUC-SERIES-A-2026 | Series A to build the confidence infrastructure for frontier AI | AIUC | vendor | https://aiuc.com/updates/series-a-announcement | 2026-09-15 | full |
| FORKAST-AIUC-2026 | AIUC Raises $40M... | Forkast | press | https://forkast.news/aiuc-raises-40m-to-build-the-certification-and-insurance-layer-that-makes-agent-governance-auditable/ | 2026-09-16 | full |
| CSA-AIASSURE-2026 | Who Assures the Assurers? Third-Party AI Assessment Standards | Cloud Security Alliance Labs | professional-body | https://labs.cloudsecurityalliance.org/research/csa-research-note-third-party-ai-assurance-standards-2026092/ | 2026-09-27 | full |
| COALFIRE-STAR-2025 | Enhancing Trust in AI: AI Certification with CSA | Coalfire | vendor | https://coalfire.com/the-coalfire-blog/enhancing-trust-in-ai-an-overview-of-ai-certification-with-the-cloud-security-alliance-csa | 2025-08-29 | full |
| DSIT-ASSURANCE-2024 | Assuring a responsible future for AI | UK DSIT | regulator | https://www.gov.uk/government/publications/assuring-a-responsible-future-for-ai/assuring-a-responsible-future-for-ai | 2024-11-06 | full |
| ICAEW-AIASSURE-2025 | Where are we now with AI assurance? | ICAEW | professional-body | https://icaew.com/insights/viewpoints-on-the-news/2025/mar-2025/where-are-we-now-with-ai-assurance | 2025-03-04 | full |
| AICPA-PA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | full (release; practice aid itself behind login) |
| AT-AICPAPA-2026 | AICPA releases practice guide for auditors dealing with AI | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai | 2026-10-14 | full |
| COSO-GENAI-2026 | Achieving Effective Internal Control Over Generative AI | COSO | standard-setter | https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf | 2026-02 | full |
| JOFA-COSO-2026 | COSO creates audit-ready guidance for governing generative AI | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/ | 2026-02-26 | full |
| IIA-AIFW-2024 | The IIA's Artificial Intelligence Auditing Framework | The IIA | professional-body | https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/ | 2024-09-13 | full |
| ISACA-AAIA-2026 | AAIA Certification | ISACA | professional-body | https://www.isaca.org/credentialing/aaia | [2026-10-16] | full |
| TCC-ICFR-2026 | Your 2026 Audit Committee Agenda: ICFR During AI Transformations | TheCorporateCounsel.net | press | https://www.thecorporatecounsel.net/blog/2026/02/your-2026-audit-committee-agenda-icfr-during-ai-transformations.html | 2026-02-06 | full |
| AIACT-ART43-2024 | Article 43: Conformity Assessment | artificialintelligenceact.eu | regulator | https://artificialintelligenceact.eu/article/43/ | 2024-06-13 | full |
| GROVES-2024 | Auditing Work: Exploring the NYC algorithmic bias audit regime | arXiv | academic | https://arxiv.org/abs/2402.08101 | 2024-02-12 | full (abstract) |
| BIRHANE-2024 | AI auditing: The Broken Bus on the Road to AI Accountability | arXiv / IEEE SaTML | academic | https://arxiv.org/abs/2401.14462 | 2024-01-25 | full (abstract) |
| OJEWALE-2025 | Towards AI Accountability Infrastructure: Gaps and Opportunities in AI Audit Tooling | arXiv / ACM CHI | academic | https://arxiv.org/abs/2402.17861 | 2025-02-27 | full (abstract; v3 date) |
| ELEVATE-COST-2026 | ISO 42001 Certification Cost Breakdown | Elevate Consulting | vendor | https://elevateconsult.com/insights/iso-42001-certification-cost-breakdown-what-enterprise-ai-teams-pay-in-2026/ | 2026-03-17 (per CSA reference list) | search-only (403) |
| EYREACT-NB-2026 | Notified Bodies Under the EU AI Act | eyreACT | vendor | https://eyreact.com/notified-bodies-ai-act/ | 2026-02-02 (per CSA reference list) | search-only (TLS error) |
| IFIAR-TTF-2025 | Use of technology in audits | IFIAR | regulator | (not opened here) | 2025-03-27 | search-only (carried from landscape) |

Count: 40 sources opened in full (16 firm/BDO/KPMG/EY/Deloitte items, 6 vendor, 6 press, 6 professional-body, 3 academic, 2 standard-setter, 2 regulator... see below), 3 search-only.

By type, opened sources: firm 17, vendor 6, press 6, professional-body 5, standard-setter 2, regulator 2, academic 3, job-posting 1 = 42 entries in the table above counting each distinct ref once (3 more entries are search-only).

---

## 6. Gaps

- **Pricing and fees.** No ISO/IEC 42001 audit fee, AI-assurance engagement fee or margin was found. The main lead (Elevate Consulting cost breakdown, cited in the CSA note) returned 403, and vendor price pages tried returned 403 or 404.
- **Certificate and engagement counts.** No count of ISO/IEC 42001 certificates, no list of issued ISAE 3000 AI assurance reports, no named client of any Big Four AI assurance engagement. ANAB, UKAS and IAF directories were not reached (403 or not tried).
- **Primary pages blocked.** ISO pages (42001, 42006) 403; PwC Canada release 403; Accountancy Today UK article on KPMG's certification 403; ACCA report page failed DNS; eyreACT TLS error; Elevate 403; SCC bulletin 403; Burges Salmon 403; EY CertifyPoint home page proxy error; AICPA practice aid and TQA 9561 text behind login.
- **Not reached by search budget.** KPMG Netherlands AI Assurance page; Grant Thornton, BDO, RSM, Forvis Mazars and other mid-tier AI assurance offers (guessed URLs returned 403/404 or only a generic page); A-LIGN, Coalfire, TÜV, DNV, LRQA, Bureau Veritas ISO 42001 pages; ICAEW AI Assurance Conference (6 Jul 2026) and other conference material; job postings beyond one Deloitte Singapore posting.
- **Auditor practice on AI in ICFR.** No inspection finding, survey or measurement on how external auditors actually scope or test entity AI. The CAQ Audit Partner Pulse and IFIAR figures in the landscape were not re-opened here. Only firm guidance, a firm forecast (KPMG) and the AICPA aid (via release and trade press) were read.
- **Measured quality outcomes.** None for assurance over AI: no error rates, override rates or independent measurement of certification quality. The only independent evidence on audit practice is qualitative academic work (NYC LL144; tool-ecosystem interviews).
- **Source quality notes.** The CSA note is a trade-body note whose EU capacity claim rests on a secondary vendor; the landscape says it discloses AI-assisted drafting, which was not seen on the opened page. Bright Defense is a compliance vendor and is the only source here for ISO/IEC 42006 detail and the 20 Nov 2025 vote.
- **Data conflicts.** (1) DSIT calls the £1.01bn "GVA"; ICAEW calls it "revenues". (2) AIUC consortium size: 60+ (Feb 2026, Schellman release) versus 250+ (Aug-Sep 2026, AIUC); different dates. (3) AIUC raised $40M Series A (15 Sep 2026) but its homepage later cites $55M. (4) COSO's eighth capability is "knowledge retrieval and summarization" in the COSO PDF and CAQ; the Journal of Accountancy and the landscape say "regulatory intelligence".
- **Search budget.** About 16 web searches were used before the budget ended; the rest of the work used direct fetches. Further searches would be the next step for pricing, certificate counts, other firms' offers and the Deloitte and EY AI-assurance case studies.

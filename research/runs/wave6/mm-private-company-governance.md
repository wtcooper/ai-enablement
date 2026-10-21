# Private-company assurance: governance and evidence (mid-market)

Researched 2026-10-21. Archetype: assurance (mid-market extension). Module: private-company. Angle: governance, what constrains and measures the work. Cross-links: [planning-risk-assessment](../../../plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/modules/planning-risk-assessment.md), [substantive-testing](../../../plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/modules/substantive-testing.md), [completion-reporting](../../../plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/modules/completion-reporting.md) and [quality-management](../../../plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/modules/quality-management.md). Source keys in brackets resolve in section 5. Where the landscape file already had a key for the same document, the same key is used (the AICPA practice aid news release is `AICPA-AIPA-2026` here and `AICPA-PA-2026` in the archetype).

## 1. Summary

- **Result.** 16 candidate use cases: 0 graded A, 3 B, 7 C, 6 D (all D entries are labelled ideas). No use case reaches A. Every governance practice found is described by a standard-setter, professional body, survey or vendor; no mid-market firm has published a measured quality outcome from AI in a private-company audit, review or compilation.
- **Where the constraint actually bites.** There is no AI-specific rule for private-company assurance. The AICPA's practice aid on AI (13 Oct 2026) is nonauthoritative and the Auditing Standards Board has issued no AI standard that this research found [AICPA-AIPA-2026; AICPA-AIPADL-2026]. The binding channel is the system of quality management (SQMS No. 1, due 15 Dec 2025) tested by triennial peer review, which began reviewing QM systems in 2026 and which the AICPA calls a test-and-learn year [AICPA-QMPEER-2026; CPACOM-SQMS-2026]. Four 2025 state peer-review reports contain no reference to AI.
- **Independent baseline.** Peer-review data give the only independent quality measure for this work. Share of reviewed engagements nonconforming in 2025: Tennessee 34 of 448 (8%), Connecticut 18 of 256 (7.03%), Minnesota 38 of 418 (9%), Oklahoma, South Dakota and Kansas 86 of 525 (16.38%); reviews, single audits and other audits are the weak spots in several reports [TSCPA-PEERREVIEW-2025; CTCPA-PEERREVIEW-2025; MNCPA-PEERREVIEW-2025; OSCPA-PEERREVIEW-2025]. The Department of Labor found 30% of sampled employee benefit plan audits (2020 form year) had major deficiencies and that peer review and practice monitoring did not help identify them [EBSA-AUDITQ-2023]. Any AI quality claim in this market should be read against that baseline.
- **Tool choice is a governance choice.** The AICPA-developed DAS methodology runs on Caseware's platform, and Withum, EisnerAmper, Citrin Cooperman and PKF O'Connor Davies have adopted it, so the methodology, the workpapers and the AI come from one vendor [CASEWARE-DASUPD-2026; WITHUM-DAS-2026; EISNER-DAS-2026; CITRIN-DAS-2026; PKF-DAS-2026]. The AICPA already warns that firms lean too heavily on third-party SOC platforms and that tool-provider contracts can shift control and evidence access [JOFA-PEER-2026; JOFA-SOCETH-2026].
- **Measurement is vendor-run or adjacent.** The only accuracy and time figures for tools in mid-market audit files are Caseware beta results (94% on golden dataset items; 2.7 review hours per disclosure checklist) [CASEWARE-VERITY-2026]. Independent studies are adjacent: AI investment and restatements at the 36 largest US firms before generative AI [FEDYK-RAST-2022], a year-long study at a UK mid-tier firm [ICAS-AMBS-2025], and field data from bookkeeping software [STANFORD-CHOIXIE-2025].
- **Survey evidence on firm governance conflicts.** 21% of Karbon's respondent firms have an AI policy against 57% in the CPAFMA survey of 162 firms; the samples differ [KARBON-AI-2026; CPAFMA-WINSOME-2026].

## 2. Use cases

```yaml
- id: assurance-private-company-01
  title: >-
    Idea: write AI into the system-of-quality-management risk assessment of a small or mid-size firm, and expect
    peer review to test it
  archetype: assurance
  module: private-company
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Peer reviewers are now evaluating a firm's system of quality management (QM) rather than a quality-control manual,
    and the AICPA says the first QM peer reviews started in 2026 (AICPA-QMPEER-2026). Staff and vendors bring AI
    tools into private-company audits and SSARS engagements, but the four 2025 state peer-review annual reports
    read for this brief do not mention AI (TSCPA-PEERREVIEW-2025; CTCPA-PEERREVIEW-2025; MNCPA-PEERREVIEW-2025;
    OSCPA-PEERREVIEW-2025).
  solution: >-
    The firm names AI-related quality risks (unapproved tools, competence, supervision, confidentiality), ties each
    to a response, monitors the responses during the year and reports on them in the annual QM evaluation, rather
    than leaving AI to an acceptable-use memo. The AICPA practice aid's section on firms' own AI use emphasises
    QM policies and procedures for AI tools, engagement-team competence, planning of intended AI use on specific
    engagements, and partners ensuring tools are firm-approved and used correctly (AICPA-AIPA-2026). Peer reviewers
    are described as looking for tailored risks rather than generic ones (AICPA-QMPEER-2026). The firm also answers
    the AICPA's new annual practice questionnaire; the AICPA's 2026 peer review update lists AI and automation among
    emerging areas (ICPAS-PRAF-2026), although the questionnaire FAQ itself does not name AI (AICPA-APQ-2026).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a
    source_ref: AICPA-QMPEER-2026
  prerequisites:
  - >-
    A named leader accountable for the QM system who evaluates it at least annually (AICPA-QMPEER-2026)
  - >-
    An inventory of AI tools, including AI embedded in software the firm already licenses and tools staff use unofficially
  - >-
    Quality risks written for this firm's engagements, not generic text, each matched to a response (AICPA-QMPEER-2026)
  - >-
    Monitoring that starts when the system is set up, not in the months before the annual evaluation (CPACOM-SQMS-2026)
  risks_and_guardrails:
  - >-
    The practice aid is described as nonauthoritative guidance (AICPA-AIPADL-2026); no Auditing Standards Board
    standard on AI was found in this research
  - >-
    The AICPA calls the first year of QM peer review a test-and-learn period and says guidance and reviewer calibration
    are still evolving (AICPA-QMPEER-2026)
  - >-
    No AI-specific peer review criteria were found; the questionnaire FAQ describes emerging areas generally (AICPA-APQ-2026)
  - >-
    Very small firms may monitor themselves, which the GAO says can be less effective than monitoring by another
    person; that FAQ is written for Yellow Book organisations (GAO-YBFAQ-2025)
  human_checkpoints:
  - Managing partner or QM leader signs the annual evaluation (AICPA-QMPEER-2026)
  - Engagement partner confirms the tool is firm-approved before use (AICPA-AIPA-2026)
  - >-
    Peer reviewer interviews firm leadership about how the system is monitored (AICPA-QMPEER-2026)
  role_evolution: >-
    The managing partner of a small firm becomes the accountable owner of AI risk in the QM system and must be able
    to explain it to a reviewer (AICPA-QMPEER-2026).
  evidence_grade: D
  sources:
  - {ref: AICPA-AIPA-2026, title: "AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting\
      \ and Auditing (news release for the practice aid 'Artificial Intelligence (AI) Considerations for Financial\
      \ Statement Auditors'; also keyed AICPA-PA-2026 in the archetype)", publisher: AICPA & CIMA, type: standard-setter,
    url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing",
    date: '2026-10-13', access: full, locator: 'Section two bullets: QM policies, competence, planning of AI use,
      partner responsibilities'}
  - {ref: AICPA-AIPADL-2026, title: "Explore new AICPA guidance on artificial intelligence (AI) and the financial\
      \ statement audit (download page; the 1.5 MB practice aid file is members-only and was not opened)", publisher: AICPA
      & CIMA, type: standard-setter, url: "https://www.aicpa-cima.com/resources/article/explore-new-aicpa-guidance-on-artificial-intelligence-ai-and-the-financial-statement-audit",
    date: '2026-10-12', access: full, locator: Paragraph 2 (nonauthoritative guidance)}
  - {ref: AICPA-QMPEER-2026, title: "Peer reviews of QM systems: What firms need to know now (Tim Kindem, AICPA\
      \ Technical Director, Peer Review)", publisher: AICPA & CIMA Insights Blog, type: professional-body, url: "https://www.aicpa-cima.com/professional-insights/article/peer-reviews-of-qm-systems-what-firms-need-to-know-now",
    date: '2026-06-25', access: full, locator: "Sections 'From documentation to demonstrable performance' and 'Working\
      \ within an evolving process'"}
  - {ref: CPACOM-SQMS-2026, title: "Waiting for peer review cycles puts firms at risk under SQMS 1 (Emily Remington,\
      \ CPA.com; CPA.com is an AICPA affiliate that also sells audit-platform implementation)", publisher: CPA.com,
    type: professional-body, url: "https://www.cpa.com/blog/2026/09/03/waiting-peer-review-cycles-puts-firms-risk-under-sqms-1",
    date: '2026-09-03', access: full, locator: Sections on the annual evaluation and on peer review checklists}
  - {ref: AICPA-APQ-2026, title: "Annual Practice Questionnaire for Peer Review (FAQ page; page undated, launch\
      \ week of 1 Jun 2026)", publisher: AICPA & CIMA, type: professional-body, url: "https://www.aicpa-cima.com/resources/article/annual-practice-questionnaire-for-peer-review-faqs",
    date: 2026-06, access: full, locator: 'FAQ: what is an emerging area; who receives the questionnaire'}
  - {ref: CTCPA-EMERGING-2026, title: "Changes to the Peer Review Program: Requirement for Completion of an Annual\
      \ Emerging Areas Questionnaire (page undated; written before the June 2026 launch)", publisher: Connecticut
      Society of CPAs, type: professional-body, url: 'https://www.ctcpas.org/peer-review-emerging-areas', date: '2026',
    access: full, locator: Questions on intent and discretionary reviews}
  - {ref: ICPAS-PRAF-2026, title: "Peer Review Alliance Forum (Virtual): 2026 Forum - Participant Slides (catalogue\
      \ description of an AICPA Peer Review update; slides themselves not opened)", publisher: Illinois CPA Society,
    type: conference, url: "https://learn.icpas.org/AssetListing/Peer-Review-Alliance-Forum-Virtual-17790/2026-Forum-%E2%80%93-Participant-Slides-29361",
    date: '2026', access: full, locator: 'Catalogue description, paragraph 2 (emerging areas)'}
  - {ref: GAO-YBFAQ-2025, title: "GAO-26-108710, Government Auditing Standards: Frequently Asked Questions on a\
      \ system of quality management", publisher: US Government Accountability Office, type: regulator, url: 'https://files.gao.gov/reports/GAO-26-108710/index.html',
    date: '2025-12-15', access: full, locator: FAQ on self-monitoring by very small audit organisations}
  - {ref: TSCPA-PEERREVIEW-2025, title: Annual Report on Peer Review Activities 2025 (Tennessee; 424 firms enrolled),
    publisher: Tennessee Society of CPAs, type: professional-body, url: "https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf",
    date: '2026-03-31', access: full, locator: Report pp. 1-2 (no AI content)}
  last_reviewed: '2026-10-21'
  notes: >-
    Idea: labelled because no public example was found of a mid-market firm's QM documentation or a peer review
    finding that names AI. Firms had to have a QM system by 15 Dec 2025 per the CPA.com blog (CPACOM-SQMS-2026);
    the annual evaluation falls due within a year of implementation. The AICPA Peer Review Board required the questionnaire
    in Nov 2025 (CTCPA-EMERGING-2026). Peer review is triennial; CPA.com describes firms with reviews scheduled
    for 2027 or 2028 acting as if they have time (CPACOM-SQMS-2026).
- id: assurance-private-company-02
  title: >-
    Written AI acceptable-use policy with an approved-tool list, a named owner and trained staff in a private-company
    practice
  archetype: assurance
  module: private-company
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - document-production
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Staff in small and mid-size firms use general chat tools for client work faster than firms write rules. Survey
    figures for firm policies differ widely, and over a third of surveyed tax and audit professionals admit using
    unauthorised AI tools (TRI-FOP-2026).
  solution: >-
    The firm writes down which tools are approved and on which plan, what client information may go into them, which
    review standard applies to AI-assisted work, and who owns the policy; some firms add a strategy committee with
    a designated representative (CPAFMA-WINSOME-2026). AICPA ethics staff note that many firms steer staff to approved
    tools with clear data-handling protections (JOFA-ETHAI-2026). The practice aid expects the engagement partner
    to know the tools in use, confirm they are firm-approved and that staff use them correctly (AICPA-AIPA-2026).
    A practitioner checklist published in the Journal of Accountancy scores a firm on 12 baseline security areas,
    one of them AI governance and responsible use (JOFA-CYBERCK-2026).
  outcomes:
  - lever: risk
    description: >-
      A survey of 162 firms reports 57% with a written AI policy that staff have been trained on, against 20% in
      2024, and 47% with a dedicated AI strategy committee
    figure: 57% (2026 survey), 20% (2024), 47%
    measures: >-
      Share of the 162 responding firms with a written AI policy that people have been trained on; share with a
      dedicated AI strategy committee and designated representative (blog's wording; original report not opened)
    provenance: independent
    source_ref: CPAFMA-WINSOME-2026
  - lever: risk
    description: >-
      Karbon's survey reports 21% of firms with an AI policy and 21% with an AI strategy; firms with a policy report
      17% more time saved
    figure: 21% policy; 17% more time saved
    measures: >-
      Share of respondents' firms that have an AI policy (about 593 respondents, mostly US, Oct 2025); the 17% is
      the report's self-reported time saved by firms with a policy compared with firms without one
    provenance: vendor-published
    source_ref: KARBON-AI-2026
  - lever: risk
    description: More than one-third of professionals surveyed admit to using unauthorised AI tools
    figure: more than 1 in 3
    measures: >-
      Share of professionals in Thomson Reuters' 2026 Future of Professionals Report who admit using unauthorised
      AI tools (the page does not state the base)
    provenance: vendor-published
    source_ref: TRI-FOP-2026
  prerequisites:
  - Inventory of tools already in use, including AI inside existing software
  - One named owner for the policy and the vendor file
  - >-
    Enterprise-tier accounts so approved tools carry contractual data protections (JOFA-CYBERCK-2026)
  - Training so staff know the rules (CPAFMA-WINSOME-2026)
  risks_and_guardrails:
  - >-
    The two policy surveys disagree (21% against 57%); samples and wording differ, so neither is a firm-population
    rate
  - A policy without monitoring does not remove unauthorised use (TRI-FOP-2026)
  - >-
    The AICPA Code's competence, confidentiality and independence duties apply however the tool is sourced (JOFA-ETHAI-2026)
  human_checkpoints:
  - Policy owner approves each tool and use
  - Engagement partner confirms approved tools are used correctly (AICPA-AIPA-2026)
  role_evolution: >-
    A partner or technology lead becomes the accountable AI policy owner; the CPAFMA summary argues that a named
    representative is what keeps governance from defaulting to individual staff judgement (CPAFMA-WINSOME-2026).
  evidence_grade: C
  sources:
  - {ref: CPAFMA-WINSOME-2026, title: "AI Governance Shocks in the 2026 CPAFMA Digitally Driven Firm Survey (secondary\
      \ blog summary of a survey of 162 firms run in Dec 2025 by Roman Kepczyk; original report not opened)", publisher: Winsome
      Marketing, type: survey, url: "https://winsomemarketing.com/professional-services-marketing/ai-governance-shocks-in-the-2026-cpafma-digitally-driven-firm-survey",
    date: '2026-07-01', access: full, locator: 'Paragraphs 2-4 (57%, 20%, 47%)'}
  - {ref: KARBON-AI-2026, title: "The State of AI in Accounting 2026 (survey Oct 2025, 593 respondents; PDF creation\
      \ date Jan 2026, publication date not printed)", publisher: Karbon, type: survey, url: "https://a.storyblok.com/f/321253/x/e2116b7c8a/the-state-of-ai-in-accounting-report-2026-by-karbon.pdf",
    date: 2026-01, access: full, locator: "p. 18 (21% policy and strategy, 17% and 20% more time saved, 46% training);\
      \ p. 3 (survey n and caveat)"}
  - {ref: TRI-FOP-2026, title: "What the 2026 Future of Professionals Report says tax and audit firm leaders should\
      \ be prioritizing now", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026",
    date: '2026-07-21', access: full, locator: '''Govern the tools being used'' priority'}
  - {ref: JOFA-ETHAI-2026, title: Accounting ethics in the age of AI (AICPA Professional Ethics Division staff),
    publisher: Journal of Accountancy, type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/',
    date: '2026-08-05', access: full, locator: Section 'AI can create confidentiality risks quickly'}
  - {ref: AICPA-AIPA-2026, title: "AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting\
      \ and Auditing (news release for the practice aid 'Artificial Intelligence (AI) Considerations for Financial\
      \ Statement Auditors'; also keyed AICPA-PA-2026 in the archetype)", publisher: AICPA & CIMA, type: standard-setter,
    url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing",
    date: '2026-10-13', access: full, locator: Section two bullets}
  - {ref: JOFA-CYBERCK-2026, title: New checklist helps CPAs manage AI cyber risks, publisher: Journal of Accountancy,
    type: press, url: "https://www.journalofaccountancy.com/news/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/",
    date: '2026-10-01', access: full, locator: Paragraphs on the Baseline Security Checklist and authorized AI tools}
  last_reviewed: '2026-10-21'
  notes: >-
    Maturity is 'emerging' because the surveys are anonymous and no named mid-market firm has published its policy
    or its results. Grade C: survey figures from a vendor, a vendor survey and a consultant survey seen only through
    a blog. ISACA reports 38% of 3,400+ digital trust professionals with a formal comprehensive AI policy (ISACA-PULSE-2026);
    that population is not accounting-specific.
- id: assurance-private-company-03
  title: >-
    Idea: address AI use in engagement letters and client consent for private-company audits and SSARS engagements
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - client-interaction
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Clients and some states care how a firm uses AI on their data, while auditing standards do not require disclosure.
    A firm that says nothing may face a client who rejects AI use on privacy or quality grounds, and one that over-relies
    on output while not disclosing it invites a claim that it misdescribed its capability (JOFA-GENAIDISC-2025).
  solution: >-
    The firm decides in writing whether engagement letters and terms of business permit AI use, what the wording
    covers (AI used to perform the service, AI notetakers, AI used generally in the business), how consent works,
    and what happens if a client objects (ACCA-ENGLTR-2026). The AICPA practice aid's Q&A says disclosure is not
    required by AICPA auditing standards but may be required by law, contract or firm policy, and notes that some
    states require advance disclosure of certain AI uses, which can sit in the engagement letter (CFODIVE-AIPA-2026).
    A liability-programme article suggests a disclosure that covers quality control before delivery, third-party
    disclosure and a request for consent, and distinguishes specific from general consent (JOFA-GENAIDISC-2025).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a
    source_ref: JOFA-GENAIDISC-2025
  prerequisites:
  - A decision on which AI uses, if any, are client-facing disclosures
  - >-
    Counsel's view on state disclosure laws; the 2025 article names California and Utah (JOFA-GENAIDISC-2025)
  - >-
    A route to do the work without AI, or to decline, for a client who objects (ACCA-ENGLTR-2026)
  - Monitoring that a client restriction is actually followed (ACCA-ENGLTR-2026)
  risks_and_guardrails:
  - >-
    Confidential client information may not be disclosed without specific client consent under the AICPA Code (JOFA-ETHAI-2026)
  - Accommodating an objection may raise cost or mean the firm cannot act (ACCA-ENGLTR-2026)
  - >-
    A blanket ban may be unworkable because AI is already embedded in firm systems (ACCA-ENGLTR-2026)
  - >-
    ACCA and CCAB material is UK guidance, and the CCAB case is a hypothetical teaching case, not a reported event
    (CCAB-CASE2-2026)
  human_checkpoints:
  - Engagement partner confirms the letter wording matches how AI will really be used
  - Client decision to consent, restrict or decline
  role_evolution: >-
    Partners handle client questions about AI use; the CCAB case recommends training teams to explain AI-assisted
    approaches without losing client confidence (CCAB-CASE2-2026).
  evidence_grade: D
  sources:
  - {ref: CFODIVE-AIPA-2026, title: AICPA issues guidance for AI-assisted auditing, publisher: CFO Dive, type: press,
    url: 'https://www.cfodive.com/news/aicpa-issues-guidance-ai-assisted-auditing/832907/', date: '2026-10-13',
    access: full, locator: Paragraphs on the practice aid's FAQ about engagement letters}
  - {ref: JOFA-GENAIDISC-2025, title: "Should I disclose my use of gen AI to clients? (Professional Liability Spotlight;\
      \ author is a risk consulting director at CNA, underwriter of the AICPA Professional Liability Insurance Program)",
    publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2025/apr/should-i-disclose-my-use-of-gen-ai-to-clients/",
    date: '2025-04-01', access: full, locator: "Sections 'Legal and ethical compliance', 'Risks when transparency\
      \ is lacking', 'Creating disclosure and consent'"}
  - {ref: ACCA-ENGLTR-2026, title: "Engagement letters, AI and PCRT (UK technical advice; PCRT is the UK tax conduct\
      \ guidance, updated Jan 2026)", publisher: ACCA, type: professional-body, url: "https://www.accaglobal.com/gb/en/technical-activities/uk-tech/in-practice-ezine-archive/In-Practice-archive-2026/september/Engagement-letters-AI-and-PCRT.html",
    date: 2026-09, access: full, locator: Section on whether engagement letters permit AI use; objecting clients}
  - {ref: JOFA-ETHAI-2026, title: Accounting ethics in the age of AI (AICPA Professional Ethics Division staff),
    publisher: Journal of Accountancy, type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/',
    date: '2026-08-05', access: full, locator: Section on confidentiality}
  - {ref: CCAB-CASE2-2026, title: "Case Study 2: Professional Accountant in Practice - AI in Audit Evidence Collection\
      \ (hypothetical teaching case, UK)", publisher: CCAB, type: professional-body, url: "https://www.ccab.org.uk/case-study-2-professional-accountant-in-practice-ai-in-audit-evidence-collection/",
    date: '2026-05-07', access: full, locator: 'Recommended actions: update engagement letters'}
  last_reviewed: '2026-10-21'
  notes: >-
    Idea: no sample audit-engagement-letter AI clause from the AICPA or a named mid-market firm was found. The practice
    aid itself is members-only; its FAQ is known through CFO Dive. The existing quality-management module covers
    disclosure at large-firm level (assurance-quality-management-24); this entry is the private-company, small-firm
    version.
- id: assurance-private-company-04
  title: >-
    Idea: review AI vendor terms (retention, training on client data, tenant separation) before staff put client
    files into a tool
  archetype: assurance
  module: private-company
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - software-systems
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    A tool that searches every client file can draw a figure from the wrong client, and consumer and business tiers
    of the same product can carry different data terms (CPAPA-7216-2026). Small firms rarely have a technology function
    to negotiate terms.
  solution: >-
    Before approving a tool, the firm gets written answers on whether the provider keeps prompts and files and for
    how long, whether it trains on customer data, whether a zero-retention agreement covers the app staff use or
    only the API, and how client data is kept apart (CPAPA-7216-2026). The Journal of Accountancy's liability article
    lists similar questions on storage, training, access, retention and incident responsibilities, and notes the
    Gramm-Leach-Bliley safeguards duties for CPA firms (JOFA-GENAIDISC-2025). A cyber checklist article suggests
    considering enterprise versions of general assistants and technical guardrails for agents with data access (JOFA-CYBERCK-2026).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a
    source_ref: CPAPA-7216-2026
  prerequisites:
  - An approved-tool list and a vendor file (CPAPA-7216-2026)
  - Someone able to read provider terms for the exact plan the firm uses (CPAPA-7216-2026)
  - >-
    Written confirmation from the vendor that client data is not used for training; the article treats a refusal
    as the answer (CPAPA-7216-2026)
  risks_and_guardrails:
  - >-
    The most specific source is a guest article by an AI implementation firm's co-founder, aimed at tax data (CPAPA-7216-2026)
  - >-
    IRS OPR Alert 2026-19 asks tax practitioners to use secure, enterprise-approved AI and ties disclosure risk
    to IRC sections 6713 and 7216; it is tax guidance, and the IRS has not said whether sending return data to an
    AI tool is a disclosure needing consent (IRS-OPR-2026; CPAPA-7216-2026)
  - >-
    The AICPA Code's confidential client information rule applies to audit and SSARS files (JOFA-ETHAI-2026)
  human_checkpoints:
  - Policy owner approves the vendor and the plan
  - Partner decides whether a client's data may go into the tool
  role_evolution: >-
    The policy owner takes on vendor due diligence, which in small firms has usually sat with an outsourced IT provider.
  evidence_grade: D
  sources:
  - {ref: CPAPA-7216-2026, title: "What to Settle Before Client Tax Data Touches AI (guest article by the co-founder\
      \ of an AI implementation firm for accounting firms)", publisher: CPA Practice Advisor, type: press, url: 'https://www.cpapracticeadvisor.com/?p=191491',
    date: '2026-10-12', access: full, locator: "Sections 'Read the terms for the exact plan you use' and 'Keep each\
      \ client's data in its own lane'"}
  - {ref: JOFA-GENAIDISC-2025, title: "Should I disclose my use of gen AI to clients? (Professional Liability Spotlight;\
      \ author is a risk consulting director at CNA, underwriter of the AICPA Professional Liability Insurance Program)",
    publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2025/apr/should-i-disclose-my-use-of-gen-ai-to-clients/",
    date: '2025-04-01', access: full, locator: Sections on legal environment and provider questions}
  - {ref: JOFA-CYBERCK-2026, title: New checklist helps CPAs manage AI cyber risks, publisher: Journal of Accountancy,
    type: press, url: "https://www.journalofaccountancy.com/news/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/",
    date: '2026-10-01', access: full, locator: Paragraphs on enterprise versions and AI agent guardrails}
  - {ref: IRS-OPR-2026, title: 'OPR Alert 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax
      Practice', publisher: IRS Office of Professional Responsibility, type: regulator, url: 'https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70',
    date: '2026-06-24', access: full, locator: Section on IRC 6713 and 7216; section 10.36 procedures}
  - {ref: JOFA-ETHAI-2026, title: Accounting ethics in the age of AI (AICPA Professional Ethics Division staff),
    publisher: Journal of Accountancy, type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/',
    date: '2026-08-05', access: full, locator: Section on confidentiality}
  last_reviewed: '2026-10-21'
  notes: >-
    Idea for assurance: the detailed guidance found is tax-led. In a survey of staff at a mid-tier UK firm, 52%
    were concerned about how client information is handled when genAI is used (ICAS-AMBS-2025).
- id: assurance-private-company-05
  title: >-
    Choose a governed vertical audit platform (methodology plus embedded AI) so a mid-market firm inherits traceability
    and data controls, with a phased rollout
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Mid-market firms cannot build and certify their own AI audit tooling, and surveys of 54 firms point to untrained
    staff (66%), poor client data (60%) and no formal transformation plan (75%) as the obstacles (CPACOM-ATR-2025).
  solution: >-
    Firms adopt a platform whose methodology, workpapers and AI sit in one system. Caseware's DAS suite uses a methodology
    the AICPA developed with audit professionals and operates within Caseware's AI ecosystem alongside Verity (CASEWARE-DASUPD-2026;
    WITHUM-DAS-2026). Withum, EisnerAmper, Citrin Cooperman and PKF O'Connor Davies are named adopters; the DAS
    suite includes preparation, compilation and review (PCR) and employee benefit plan modules (EISNER-DAS-2026;
    CITRIN-DAS-2026; PKF-DAS-2026). Caseware states that AI outputs are citation-backed, reviewable and traceable
    before entering the file, run within firm-configured permissions with engagement-level data isolation, and that
    it supports enterprise compliance requirements including SOC 2 Type II and ISO 27001 certification (CASEWARE-VERITY-2026).
    EisnerAmper rolled DAS out in phases with training, pilot projects and change management, working with CPA.com
    (EISNER-DAS-2026). Grant Thornton's US firm announced its own gtap platform, to be introduced first with private
    company audits (GT-GTAP-2026); RSM built a firm-approved guidance assistant for its 4,000+ assurance professionals
    serving the middle market (RSM-ASKLUCA-2026).
  outcomes:
  - lever: capacity
    description: >-
      Withum reports more than 1,000 active users on DAS and more than 6,000 engagements completed on it
    figure: more than 1,000 users; more than 6,000 engagements
    measures: >-
      Active users on the platform and engagements completed to date (adoption counts, not quality or time measures;
      DAS is the audit platform, not only its AI features)
    provenance: vendor-published
    source_ref: WITHUM-DAS-2026
  - lever: capacity
    description: >-
      EisnerAmper reports more than 1,100 professionals on the DAS suite and over 1,500 client engagements completed
      on it
    figure: more than 1,100 professionals; over 1,500 engagements
    measures: >-
      Professionals using the suite and client engagements completed on it (adoption counts only)
    provenance: vendor-published
    source_ref: EISNER-DAS-2026
  prerequisites:
  - 'A methodology decision: the platform''s methodology becomes the firm''s audit methodology'
  - Data migration, training and change management (CITRIN-DAS-2026; EISNER-DAS-2026)
  - Firm-configured permissions and engagement-level data separation (CASEWARE-VERITY-2026)
  - >-
    Documented firm review of the vendor's controls, because the vendor's claims are self-published
  risks_and_guardrails:
  - >-
    All adoption figures and governance claims are vendor-published press releases; no firm has published quality
    or time results from the AI features (WITHUM-DAS-2026; EISNER-DAS-2026)
  - >-
    The platform couples methodology and AI to one vendor; the AICPA ethics article warns about terms that shift
    control, judgment, financial dependency or access to evidence toward a tool provider (JOFA-SOCETH-2026, written
    about SOC 2 tools and said to be relevant to other attest work)
  - >-
    Reliance on a third-party platform without applying professional judgment is a concern the AICPA raised for
    SOC 2 engagements (JOFA-PEER-2026)
  - The AI layer's beta results cover a limited set of firms (CASEWARE-CWX-2026)
  human_checkpoints:
  - Auditors accept, refine or override suggestions inside the workflow (CASEWARE-VERITY-2026)
  - >-
    Managers and partners review as before; the AI is described as a second set of eyes whose review points remain
    the reviewer's call (CASEWARE-CWX-2026)
  role_evolution: >-
    Caseware's release says a first-year auditor at Withum can understand disclosure checklist requirements and
    trace outputs to supporting evidence, so the platform doubles as training (WITHUM-DAS-2026); Citrin Cooperman's
    innovation leader makes a similar point about learning the reasoning behind procedures (CITRIN-DAS-2026). Both
    are vendor-published statements.
  evidence_grade: B
  sources:
  - {ref: WITHUM-DAS-2026, title: Withum Fully Adopts DAS Powered by the Caseware Verity AI Platform, publisher: Caseware,
    type: vendor, url: "https://www.caseware.com/news/withum-fully-adopts-das-powered-by-the-caseware-verity-ai-platform-to-drive-its-future-ready-audit-practice",
    date: '2026-06-03', access: full, locator: 'Paragraphs 2-4 (1,000+ users, 6,000+ engagements; DAS methodology)'}
  - {ref: EISNER-DAS-2026, title: EisnerAmper Leverages DAS Powered by Caseware to Unify Audit and Build an Agentic
      Future, publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/eisneramper-leverages-das-powered-by-caseware-to-unify-audit-and-build-an-agentic-future-across-its-multi-vertical-practice",
    date: '2026-06-25', access: full, locator: 'Paragraphs 1-4 (1,100+ professionals, 1,500+ engagements; phased
      rollout; CPA.com)'}
  - {ref: CITRIN-DAS-2026, title: 'Citrin Cooperman & Company, LLP Adopts AI-Enabled DAS Suite Powered by Caseware',
    publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth",
    date: '2026-07-13', access: full, locator: 'Paragraphs 1-6 (DAS Audit, PCR, EBP; CPA.com implementation partner)'}
  - {ref: PKF-DAS-2026, title: "PKF O'Connor Davies Adopts AI-Enabled DAS Suite Powered by Caseware Verity, and\
      \ Joins the Caseware Agentic Pioneer Program", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program",
    date: '2026-10-08', access: full, locator: Subtitle and paragraph 1 (Agentic Pioneer Program)}
  - {ref: CASEWARE-VERITY-2026, title: "Caseware Launches Caseware Verity to Bring Workflow-Native AI Agents Directly\
      \ Into Assurance Engagements", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements",
    date: '2026-05-20', access: full, locator: 'Sections ''Governance, traceability and human oversight'' and beta
      results'}
  - {ref: CASEWARE-DASUPD-2026, title: "AICPA Dynamic Assurance Solution (DAS) Expands Connected Audit Workflows\
      \ with New Risk, Controls and PCAOB Capabilities", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/aicpa-dynamic-assurance-solution-das-expands-connected-audit-workflows-with-new-risk-controls-and-pcaob-capabilities",
    date: '2026-06-08', access: full, locator: Paragraph 2 (methodology developed by the AICPA)}
  - {ref: CASEWARE-CWX-2026, title: "CwX 2026: How agentic AI is transforming audit and assurance (blog on a May\
      \ 2026 conference session)", publisher: Caseware, type: conference, url: "https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance",
    date: '2026-06-17', access: full, locator: Sections 'Governance and accountability' and 'Feedback from beta
      partner firms'}
  - {ref: GT-GTAP-2026, title: Grant Thornton launches gtap to transform audit delivery across U.S. practice, publisher: Grant
      Thornton US, type: firm, url: "https://www.grantthornton.com/insights/press-releases/2026/may/grant-thornton-launches-gtap-audit-transformation-us",
    date: '2026-05-07', access: full, locator: Paragraphs 2-5 (private company audits first; any ERP; supervision)}
  - {ref: RSM-ASKLUCA-2026, title: 'RSM US Launches Ask Luca, Expanding AI Capabilities in the Audit', publisher: RSM
      US, type: firm, url: 'https://rsmus.com/newsroom/2026/rsm-launches-ask-luca.html', date: '2026-01-08', access: full,
    locator: Paragraphs 2-4 and 'Transforming the audit process' section}
  - {ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report (2025 CPA.com and AICPA Audit Benchmark Survey;\
      \ 54 US firms; not representative)", publisher: CPA.com and AICPA, type: survey, url: 'https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf',
    date: 2025-12, access: full, locator: p. 8 (blockers); p. 9 (75% without formal plan)}
  last_reviewed: '2026-10-21'
  notes: >-
    Firm types: Withum and PKF O'Connor Davies are described by Caseware as Top 25 US firms and EisnerAmper as Top
    20 (another article calls it Top 15, EISNER-AUDITAGENT-2026); Citrin Cooperman is described as serving private,
    middle-market businesses and high-net-worth individuals. Grant Thornton and RSM are national firms whose platforms
    are aimed at private-company and middle-market audits. Grade B: named deployments, usage counts only. No regional
    or local firm below the top 100 was found with a public deployment of these tools.
- id: assurance-private-company-06
  title: >-
    Test AI agents against a firm-held answer key before relying on them, and re-test when the model changes
  archetype: assurance
  module: private-company
  function: risk-compliance-legal
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >-
    Smaller firms depend on the vendor's own statements of accuracy and have no independent measure. The only published
    accuracy figures found for tools used in mid-market audit files are vendor-run beta results.
  solution: >-
    Before relying on a checklist, extraction or risk-suggestion agent, the firm scores its output against engagements
    where the right answers are known, records the miss rate by item type, sets the review depth to match, and repeats
    the test when the vendor changes the model. Caseware reports that Verity achieved 94% accuracy on golden dataset
    items captured from beta traces, cut indicative manual workflows from 15-20 minutes to under two minutes, and
    saved 2.7 review hours per workflow for its disclosure checklist agent on average (CASEWARE-VERITY-2026). Beta
    firms described the same 2.7 hours as an average that varied by engagement, and one found the agent surfaced
    checklist questions that had been answered incorrectly (CASEWARE-CWX-2026).
  outcomes:
  - lever: quality
    description: Caseware reports 94% accuracy on golden dataset items captured from beta traces
    figure: 94%
    measures: >-
      Accuracy on golden dataset items captured from beta traces (Caseware does not give the item count or define
      the numerator and denominator)
    provenance: vendor-published
    source_ref: CASEWARE-VERITY-2026
  - lever: speed
    description: >-
      Caseware reports indicative manual workflows falling from 15-20 minutes to under two minutes, up to 85% per
      interaction
    figure: up to 85% time saved per interaction
    measures: >-
      Time per interaction on indicative manual workflows in beta (Caseware's wording; workflows not specified)
    provenance: vendor-published
    source_ref: CASEWARE-VERITY-2026
  - lever: speed
    description: Disclosure checklist agent saves 2.7 review hours per workflow on average
    figure: 2.7 hours per workflow
    measures: >-
      Average review hours saved per disclosure checklist run among beta firms; results varied by engagement
    provenance: vendor-published
    source_ref: CASEWARE-CWX-2026
  prerequisites:
  - >-
    Engagements or checklists with known answers, held by the firm and not supplied by the vendor
  - Scoring criteria, and a tolerance linked to the review that follows
  - >-
    A trigger to re-test when the vendor changes the model (see assurance-quality-management-01 for recertification
    triggers at large firms)
  - Vendor willingness to share traces and version histories
  risks_and_guardrails:
  - Both figures are vendor-published beta results and are not independently verified
  - An answer key built from the vendor's own traces tests what the vendor already saw
  - >-
    Fluent, cited output can hide errors, so reviewers must check the cited source (CASEWARE-VERITY-2026 says outputs
    are citation-backed and reviewable)
  - No firm has published its own miss rate for these agents
  human_checkpoints:
  - >-
    Auditor reviews and accepts or overrides each citation-backed suggestion (CASEWARE-VERITY-2026)
  - Firm methodology lead signs off the test results before the agent goes into engagement use
  role_evolution: >-
    Beta partners described reviewing and validating instead of searching (CASEWARE-CWX-2026); the firm's methodology
    lead takes on test-set maintenance.
  evidence_grade: C
  sources:
  - {ref: CASEWARE-VERITY-2026, title: "Caseware Launches Caseware Verity to Bring Workflow-Native AI Agents Directly\
      \ Into Assurance Engagements", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements",
    date: '2026-05-20', access: full, locator: Paragraph 4 (beta results) and agent suites section}
  - {ref: CASEWARE-CWX-2026, title: "CwX 2026: How agentic AI is transforming audit and assurance (blog on a May\
      \ 2026 conference session)", publisher: Caseware, type: conference, url: "https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance",
    date: '2026-06-17', access: full, locator: Section 'Disclosure Checklist Agent'}
  last_reviewed: '2026-10-21'
  notes: >-
    Grade C: vendor claims. Maturity 'piloting': the figures come from beta programmes; the Document Intelligence
    agent was in closed beta and the Risk Suggestion agent in alpha at launch (CASEWARE-VERITY-2026). The disclosure
    checklist time saving is also an outcome for completion-reporting; see routing.
- id: assurance-private-company-07
  title: >-
    AI cross-file checks and review packs to catch problems before partner sign-off and peer review
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Peer review of private-company work finds nonconforming engagements most often in reviews, single audits and
    other audits. In 2025 state reports: Tennessee 34 of 448 engagements reviewed nonconforming (8%), including
    13 of 99 reviews and 8 of 53 'other' audits (TSCPA-PEERREVIEW-2025); Connecticut 18 of 256 (7.03%) (CTCPA-PEERREVIEW-2025);
    Minnesota 38 of 418 (9%), including 14 of 75 reviews (MNCPA-PEERREVIEW-2025); the Oklahoma, South Dakota and
    Kansas administering entity 86 of 525 (16.38%), including 12 of 40 single audits and 20 of 61 other audits under
    SAS (OSCPA-PEERREVIEW-2025). Categories differ between reports and should not be pooled.
  solution: >-
    Platform vendors describe AI that helps managers review through cross-file risk checks, unresolved-issue tracking
    and automated review pack generation, and gives partners earlier visibility into sign-off readiness and inspection
    risks (CASEWARE-VERITY-2026). Caseware's CwX demonstration showed a planning review where the assistant surfaced
    a trial-balance variance with no associated risk (CASEWARE-CWX-2026). The AICPA's 2026 peer review update uses
    case studies in compilations, reviews and audits, and names recurring problem areas such as risk assessment,
    control documentation, accounting standard changes and reporting departures (ICPAS-PRAF-2026), which are the
    areas a firm could point such checks at.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: n/a
    source_ref: CASEWARE-VERITY-2026
  prerequisites:
  - A firm view of its own recurring review notes and past nonconformity types
  - Engagement data in one system so cross-file checks have something to check
  - A rule that AI-found issues are cleared and documented, not just counted
  risks_and_guardrails:
  - No peer review result, inspection result or error rate for any AI review aid was found
  - >-
    Peer review samples are small and administered state by state; state rates are not comparable
  - >-
    EBSA found that peer review and practice monitoring did not help identify deficient plan audits, so passing
    peer review is weak evidence of tool quality (EBSA-AUDITQ-2023)
  - >-
    A system that flags risks may anchor reviewers on its flags; the CCAB case describes junior auditors focusing
    only on AI-flagged issues (CCAB-CASE2-2026, hypothetical)
  human_checkpoints:
  - >-
    Manager and partner remain the reviewers; the tool is described as giving review points that stay 'yours to
    call' (CASEWARE-CWX-2026)
  - Engagement quality review where required
  role_evolution: >-
    Reviewers move from locating gaps to clearing flagged ones; the firm's national office can see sign-off readiness
    earlier (CASEWARE-VERITY-2026).
  evidence_grade: C
  sources:
  - {ref: CASEWARE-VERITY-2026, title: "Caseware Launches Caseware Verity to Bring Workflow-Native AI Agents Directly\
      \ Into Assurance Engagements", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements",
    date: '2026-05-20', access: full, locator: 'Paragraph on roles: preparers, managers, partners'}
  - {ref: CASEWARE-CWX-2026, title: "CwX 2026: How agentic AI is transforming audit and assurance (blog on a May\
      \ 2026 conference session)", publisher: Caseware, type: conference, url: "https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance",
    date: '2026-06-17', access: full, locator: Planning review scenario}
  - {ref: TSCPA-PEERREVIEW-2025, title: Annual Report on Peer Review Activities 2025 (Tennessee; 424 firms enrolled),
    publisher: Tennessee Society of CPAs, type: professional-body, url: "https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf",
    date: '2026-03-31', access: full, locator: 'Report p. 2, table 2(c)'}
  - {ref: CTCPA-PEERREVIEW-2025, title: "Annual Report on Peer Review Activities (Connecticut; 249 firms administered\
      \ at 31 Dec 2025)", publisher: Connecticut Society of CPAs, type: professional-body, url: 'https://www.ctcpas.org/storage/assets/PDFs/Annual%20Report%20on%20PR%20Activities.pdf',
    date: '2026-01-12', access: full, locator: Report table 2(c)}
  - {ref: MNCPA-PEERREVIEW-2025, title: 2025 Annual Report on Peer Review Activities (Minnesota and North Dakota;
      269 firms), publisher: Minnesota Society of CPAs, type: professional-body, url: "https://www.mncpa.org/mncpa/media/Documents-Shared/peer-review/2025-MNCPA-annual-report-on-peer-review-activities.pdf",
    date: 2026-02, access: full, locator: Report table 2(c)}
  - {ref: OSCPA-PEERREVIEW-2025, title: "2025 Annual Report on Peer Review Activities (Oklahoma, South Dakota and\
      \ Kansas; 387 firms)", publisher: Oklahoma Society of CPAs, type: professional-body, url: "https://prod.oscpa.com/storage/assets/Peer%20Review/Annual%20Report/2025%20OSCPA%20Peer%20Review%20Activities.pdf",
    date: 2026-03, access: full, locator: Report table 2(c)}
  - {ref: ICPAS-PRAF-2026, title: "Peer Review Alliance Forum (Virtual): 2026 Forum - Participant Slides (catalogue\
      \ description of an AICPA Peer Review update; slides themselves not opened)", publisher: Illinois CPA Society,
    type: conference, url: "https://learn.icpas.org/AssetListing/Peer-Review-Alliance-Forum-Virtual-17790/2026-Forum-%E2%80%93-Participant-Slides-29361",
    date: '2026', access: full, locator: 'Catalogue description, paragraph on nonconforming engagements'}
  - {ref: EBSA-AUDITQ-2023, title: "Audit Quality Study, November 2023 (fourth EBSA assessment of employee benefit\
      \ plan audits; 2020 form year, 307 audit reports)", publisher: 'US Department of Labor, Employee Benefits
      Security Administration', type: regulator, url: "https://www.dol.gov/sites/dolgov/files/ebsa/about-ebsa/our-activities/resource-center/publications/november-2023-audit-quality-study.pdf",
    date: 2023-11, access: full, locator: 'Executive summary, paragraph 2'}
  last_reviewed: '2026-10-21'
  notes: >-
    Grade C: vendor description of features; peer-review data are independent but measure the problem, not an AI
    effect. Maturity 'announced': the cross-file checks and review packs are listed as capabilities at launch, without
    evidence of use. The nonconformity rates are the independent baseline against which any firm's AI quality claim
    should be read.
- id: assurance-private-company-08
  title: >-
    Write a transformation plan and baseline the metrics that show whether AI changes hours, review notes and quality
  archetype: assurance
  module: private-company
  function: strategy-planning
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Of 54 firms in the CPA.com and AICPA audit benchmark, 75% had no formal documentation of their audit transformation,
    and the metrics most firms track (realization 87%, billable hours 76%, utilisation 72%) say little about AI's
    effect (CPACOM-ATR-2025). The ISACA global poll found only 22% saying AI return on investment met or exceeded
    expectations, while 22% did not know it (ISACA-PULSE-2026, not accounting-specific).
  solution: >-
    The firm records a baseline before rollout (hours per checklist, per selection, per review round; review notes
    per file; nonconformity history) and tracks it after. The AICPA benchmark report suggests newer metrics such
    as deliverable-based accountability and client readiness, and a formal policy to reinvest a defined share of
    saved time (the report gives 20% as an example) (CPACOM-ATR-2025).
  outcomes:
  - lever: quality
    description: 75% of 54 firms had no formal documentation of their audit transformation
    figure: 75%
    measures: >-
      Share of the 54 responding US firms that do not formally document audit transformation (survey not representative
      of all firms)
    provenance: independent
    source_ref: CPACOM-ATR-2025
  - lever: cost
    description: >-
      6% of firms do not measure return on technology investment; 83% name staff efficiency as a top-two priority
    figure: 6%; 83%
    measures: >-
      Shares of the 54 firms: not measuring technology ROI; naming staff efficiency (time savings) among the two
      outcomes most prioritised when evaluating technology ROI
    provenance: independent
    source_ref: CPACOM-ATR-2025
  - lever: quality
    description: Few firms track margin, deliverable-based accountability or client readiness
    figure: 28%; 22%; 13%
    measures: >-
      Shares of the 54 firms tracking audit margin per engagement; deliverable-based accountability; client readiness
      metrics
    provenance: independent
    source_ref: CPACOM-ATR-2025
  prerequisites:
  - A named owner and a written plan (CPACOM-ATR-2025)
  - Pre-rollout baselines in the same units the firm will use afterwards
  - Time-recording that can separate AI-assisted from other work
  risks_and_guardrails:
  - >-
    The benchmark was run by CPA.com and the AICPA, which also sell DAS services; it is a non-representative sample
    of 54 firms (CPACOM-ATR-2025, p. 3)
  - >-
    Time saved is the dominant measure, quality the second (54%), so savings may be claimed without a quality check
  - >-
    Karbon reports firms with an AI policy saving 17% more time and firms with a strategy 20% more, self-reported
    (KARBON-AI-2026, p. 18)
  human_checkpoints:
  - Practice leader reviews baseline and post-rollout figures together
  - Partner decides how much saved time is reinvested
  role_evolution: Practice leaders add AI value tracking to hours, realization and utilisation reporting.
  evidence_grade: C
  sources:
  - {ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report (2025 CPA.com and AICPA Audit Benchmark Survey;\
      \ 54 US firms; not representative)", publisher: CPA.com and AICPA, type: survey, url: 'https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf',
    date: 2025-12, access: full, locator: "p. 3 (sample and caveat); p. 9 (75%); p. 12 (ROI priorities and 6%);\
      \ p. 16 (reinvest 20% example); p. 22 (metrics tracked)"}
  - {ref: ISACA-PULSE-2026, title: "AI use accelerates while governance and ROI lag, says new ISACA research (3,400+\
      \ digital trust professionals, global; not accounting-specific)", publisher: ISACA, type: survey, url: "https://isaca.org/about-us/newsroom/press-releases/2026/ai-use-accelerates-while-governance-and-roi-lag-says-new-isaca-research",
    date: '2026-05-05', access: full, locator: Paragraphs on ROI}
  - {ref: KARBON-AI-2026, title: "The State of AI in Accounting 2026 (survey Oct 2025, 593 respondents; PDF creation\
      \ date Jan 2026, publication date not printed)", publisher: Karbon, type: survey, url: "https://a.storyblok.com/f/321253/x/e2116b7c8a/the-state-of-ai-in-accounting-report-2026-by-karbon.pdf",
    date: 2026-01, access: full, locator: p. 18}
  last_reviewed: '2026-10-21'
  notes: >-
    Grade C: survey data on measurement practice; no firm has published AI-specific before-and-after figures for
    a private-company audit. Maturity 'emerging'.
- id: assurance-private-company-09
  title: >-
    Roll out general-purpose GenAI to all staff at a mid-tier firm with skills sessions and an independent study
    of what changes
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - document-production
  - research-synthesis
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Firms adopt general assistants without measuring whether time saved becomes output or whether staff trust the
    results.
  solution: >-
    Beever and Struthers, a mid-tier UK practice, introduced GenAI under a year-long study by Alliance Manchester
    Business School and Aston Business School that combined surveys of more than 200 staff, 50 interviews, targeted
    skills sessions and four case studies (ICAS-AMBS-2025). Staff used it to draft or refine written material (53%),
    summarise meetings or long documents (46%) and support spreadsheet work (33%) (ICAS-AMBS-2025).
  outcomes:
  - lever: speed
    description: 74% said GenAI helped them complete certain tasks faster
    figure: 74%
    measures: >-
      Share of survey respondents saying genAI helped complete certain tasks more quickly (article does not state
      each figure's base; survey drew on more than 200 staff)
    provenance: independent
    source_ref: ICAS-AMBS-2025
  - lever: capacity
    description: 22% said the time savings had become a marked rise in overall output
    figure: 22%
    measures: >-
      Share of respondents reporting that time savings turned into a marked rise in their overall output
    provenance: independent
    source_ref: ICAS-AMBS-2025
  - lever: risk
    description: >-
      72% feared incorrect output or flawed decisions; 52% worried about how client information is handled
    figure: 72%; 52%
    measures: >-
      Shares of respondents concerned about incorrect genAI output; concerned about client information handling
      and protection
    provenance: independent
    source_ref: ICAS-AMBS-2025
  prerequisites:
  - Skills sessions alongside the tool (ICAS-AMBS-2025)
  - A way to ask staff and measure output, not just licences issued
  risks_and_guardrails:
  - >-
    The study found genAI most effective for routine, structured work, while tasks needing nuanced understanding,
    collaboration or ethical decision-making still depend on professional expertise (ICAS-AMBS-2025)
  - >-
    The firm is UK and tasks are general accounting work, not audit-specific, so the grade is capped at B
  - Only the press report was read; the ICAS report was not opened
  human_checkpoints:
  - >-
    Staff review all output; ICAS's lead says people must stay in the driving seat of professional decisions (ICAS-AMBS-2025)
  role_evolution: >-
    Output rises for a minority; the gap between faster tasks (74%) and more output (22%) suggests time is absorbed
    elsewhere (inference from the two figures, not stated by the source).
  evidence_grade: B
  sources:
  - {ref: ICAS-AMBS-2025, title: "ICAS study finds widespread concern over genAI accounting errors (reports ICAS,\
      \ 'Generative AI and Professional Judgement in Accounting'; Alliance Manchester and Aston Business Schools\
      \ study of Beever and Struthers; ICAS report itself not opened)", publisher: The Accountant, type: academic,
    url: 'https://www.theaccountant-online.com/news/icas-study-finds-widespread/', date: '2026-03-17', access: full,
    locator: 'Paragraphs 3-12 (design, 74%, 22%, 72%, 52%, task uses)'}
  last_reviewed: '2026-10-21'
  notes: >-
    Adjacent evidence: a named mid-tier firm and an independent academic study, but UK and not assurance-specific;
    the grade is capped at B. The date of the article (17 Mar 2026) corrects the landscape file, which listed the
    study as undated.
- id: assurance-private-company-10
  title: >-
    Central AI and analytics capability supporting audit execution, tracked against restatements and fees
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: >-
    Firms need evidence that investing in AI changes audit quality, not only hours. The one independent quantitative
    study found concerns the largest US public-company audit firms, before generative AI.
  solution: >-
    The 36 largest US audit firms employed AI-skilled staff concentrated in central teams; the study links more
    AI workers to fewer restatements and slightly lower fees (FEDYK-RAST-2022). Interviews with 17 audit partners,
    including eight from non-Big 4 firms, found AI developed centrally, widely used in audit, and used mainly for
    quality, then efficiency (FEDYK-RAST-2022). Mid-market firms mostly reach the same tools by buying platforms
    (see 05) rather than building.
  outcomes:
  - lever: quality
    description: >-
      A one-standard-deviation change in recent AI investment is associated with a 5.0% reduction in the likelihood
      of an audit restatement
    figure: 5.0%
    measures: >-
      Association between a firm's recent AI investment (share of AI workers over the prior three years) and the
      likelihood of an audit restatement; 36 largest US public accounting firms, 2010-2019, more than 310,000 resumes
    provenance: independent
    source_ref: FEDYK-RAST-2022
  - lever: cost
    description: The same change is associated with a 0.9% drop in audit fees
    figure: 0.9%
    measures: Association with audit fees, same sample
    provenance: independent
    source_ref: FEDYK-RAST-2022
  - lever: capacity
    description: Number of accounting employees falls 3.6% after three years and 7.1% after four
    figure: 3.6%; 7.1%
    measures: >-
      Reduction in the number of accounting employees following a one-standard-deviation change in recent AI investment
    provenance: independent
    source_ref: FEDYK-RAST-2022
  prerequisites:
  - A central team with AI-skilled staff (FEDYK-RAST-2022)
  - Outcome data to compare, such as restatements and peer review results
  risks_and_guardrails:
  - >-
    The sample is public-company audits at the 36 largest firms, 2010-2019, before generative AI; the paper reports
    associations, not firm-level controlled trials
  - The effect on labour takes years to appear (FEDYK-RAST-2022)
  - Mid-market private-company audits have no restatement data comparable to issuer audits
  human_checkpoints:
  - Partners remain accountable for the opinion; no checkpoint in the study design
  role_evolution: The study reports fewer accounting employees after three and four years (FEDYK-RAST-2022).
  evidence_grade: B
  sources:
  - {ref: FEDYK-RAST-2022, title: "Is artificial intelligence improving the audit process? (Fedyk, Hodson, Khimich,\
      \ Fedyk; Review of Accounting Studies 27:938-985)", publisher: Review of Accounting Studies (Springer), type: academic,
    url: 'https://doi.org/10.1007/s11142-022-09697-x', date: '2022-07-07', access: full, locator: 'Abstract; Introduction
      (5.0%, 1.4%, 1.9%); Section 2 (sample 2010-2019)'}
  last_reviewed: '2026-10-21'
  notes: >-
    Independent and measured, but an adjacent process: public-company audits, largest firms, pre-GenAI. The grade
    is therefore capped at B. Included because it is the only independent quantitative link between AI investment
    and audit quality found, and it frames what mid-market firms would need to measure.
- id: assurance-private-company-11
  title: >-
    Make role-based AI training a condition of tool access, and train leaders and reviewers as well as preparers
  archetype: assurance
  module: private-company
  function: people-hr
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Staff training is the most cited obstacle in the AICPA audit benchmark: 66% of 54 firms ranked untrained staff
    among their top blockers (CPACOM-ATR-2025, p. 8). Only 46% of Karbon's respondent firms invest in training (KARBON-AI-2026,
    p. 18).
  solution: >-
    The firm ties access to a tool to completed training for the role, and covers the engagement team's competence,
    which the practice aid lists as a firm-level consideration (AICPA-AIPA-2026). EisnerAmper's DAS rollout used
    training, pilot projects and champion leadership with CPA.com (EISNER-DAS-2026), and Citrin Cooperman used CPA.com
    for training and change management (CITRIN-DAS-2026). Thomson Reuters' paper adds that junior staff still need
    structured development, with supervision in place before automation erodes it (TRI-FOP-2026).
  outcomes:
  - lever: risk
    description: 66% of firms rank untrained staff among top blockers to audit transformation
    figure: 66%
    measures: >-
      Share of the 54 firms ranking staff not trained in advanced approaches or methodologies among top perceived
      blockers and risks
    provenance: independent
    source_ref: CPACOM-ATR-2025
  - lever: capacity
    description: >-
      46% of firms invest in AI training; 17% more time saved at firms with an AI policy (self-reported)
    figure: 46%; 17%
    measures: >-
      Share of respondents' firms investing in training for their teams (up 9% year on year); the 17% is time saved
      by firms with a policy against those without
    provenance: vendor-published
    source_ref: KARBON-AI-2026
  prerequisites:
  - Role-specific curricula for preparers, reviewers and partners
  - A record of who completed training before access
  - Protected time (EisnerAmper describes a deliberate phased rollout, EISNER-DAS-2026)
  risks_and_guardrails:
  - >-
    Training figures are survey self-reports; no firm has published whether trained staff make fewer AI-related
    review notes
  - No firm size split of training rates was read in a primary source
  human_checkpoints:
  - Partner confirms team competence before engagement use (AICPA-AIPA-2026)
  - Training owner certifies completion
  role_evolution: >-
    Juniors move from preparing work to reviewing AI output, which Thomson Reuters says needs deliberate supervision
    to protect development (TRI-FOP-2026); more than one-quarter of professionals said they would not accept a job
    at a firm lacking professional-grade AI (TRI-FOP-2026).
  evidence_grade: C
  sources:
  - {ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report (2025 CPA.com and AICPA Audit Benchmark Survey;\
      \ 54 US firms; not representative)", publisher: CPA.com and AICPA, type: survey, url: 'https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf',
    date: 2025-12, access: full, locator: p. 8 (blockers)}
  - {ref: KARBON-AI-2026, title: "The State of AI in Accounting 2026 (survey Oct 2025, 593 respondents; PDF creation\
      \ date Jan 2026, publication date not printed)", publisher: Karbon, type: survey, url: "https://a.storyblok.com/f/321253/x/e2116b7c8a/the-state-of-ai-in-accounting-report-2026-by-karbon.pdf",
    date: 2026-01, access: full, locator: p. 18}
  - {ref: AICPA-AIPA-2026, title: "AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting\
      \ and Auditing (news release for the practice aid 'Artificial Intelligence (AI) Considerations for Financial\
      \ Statement Auditors'; also keyed AICPA-PA-2026 in the archetype)", publisher: AICPA & CIMA, type: standard-setter,
    url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing",
    date: '2026-10-13', access: full, locator: 'Section two: competence and capabilities of the team'}
  - {ref: EISNER-DAS-2026, title: EisnerAmper Leverages DAS Powered by Caseware to Unify Audit and Build an Agentic
      Future, publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/eisneramper-leverages-das-powered-by-caseware-to-unify-audit-and-build-an-agentic-future-across-its-multi-vertical-practice",
    date: '2026-06-25', access: full, locator: Rollout and training paragraphs}
  - {ref: CITRIN-DAS-2026, title: 'Citrin Cooperman & Company, LLP Adopts AI-Enabled DAS Suite Powered by Caseware',
    publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth",
    date: '2026-07-13', access: full, locator: CPA.com implementation paragraph}
  - {ref: TRI-FOP-2026, title: "What the 2026 Future of Professionals Report says tax and audit firm leaders should\
      \ be prioritizing now", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026",
    date: '2026-07-21', access: full, locator: '''Define the role of early-career professionals'' and talent paragraph'}
  last_reviewed: '2026-10-21'
  notes: >-
    Grade C: survey figures and vendor-published rollout descriptions. A search summary of IPA data (about 25% of
    firms under $10 million offering AI training against 69% of firms over $100 million) was not opened and is not
    used as evidence. Overlaps assurance-quality-management-10 (large-firm, role-differentiated training); this
    entry is the small and mid-size version.
- id: assurance-private-company-12
  title: >-
    Idea: screen AI platform and co-development arrangements for independence and ethics threats before signing
  archetype: assurance
  module: private-company
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Firms are entering platform, resale and co-development arrangements with AI vendors, and some outside capital
    arrives with them. The AICPA warns that contract terms can move control, judgment, financial dependency, promotion
    or evidence access to a tool provider (JOFA-SOCETH-2026).
  solution: >-
    Before adopting a platform or joining a co-development programme, the firm's ethics lead reviews terms against
    the AICPA Code's independence and ethical-conflict provisions and asks whether the arrangement limits the firm's
    ability to set scope and timing, obtain evidence, communicate deficiencies or stay objective (JOFA-SOCETH-2026).
    AICPA ethics staff add that building or hosting an AI system for an attest client can raise independence concerns
    under the nonattest-services rules (JOFA-ETHAI-2026). The PEEC is separately considering a second exposure draft
    on alternative practice structures, including a new interpretation barring attest-client investment in firms
    (JOFA-PEEC-2026). PKF O'Connor Davies joined a Caseware programme to co-develop proprietary agents on Caseware's
    platform, an example of the kind of arrangement in question (PKF-DAS-2026), though no source says it raises
    a threat.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a
    source_ref: JOFA-SOCETH-2026
  prerequisites:
  - Ethics or national-office reviewer who reads the contract
  - A rule that new vendor arrangements pass an independence check before signature
  risks_and_guardrails:
  - >-
    The AICPA article is about SOC 2 tool providers and says its considerations may be relevant to other audit and
    attest services (JOFA-SOCETH-2026)
  - >-
    AICPA says some firms lean too heavily on third-party SOC platforms without applying the professional judgment
    standards require (JOFA-PEER-2026)
  - PEEC drafts were still under discussion in Aug 2026 (JOFA-PEEC-2026)
  human_checkpoints:
  - Ethics lead and managing partner sign the independence conclusion
  - Document the analysis when the Code does not address the case (JOFA-ETHAI-2026)
  role_evolution: Ethics and national-office roles add vendor-contract review.
  evidence_grade: D
  sources:
  - {ref: JOFA-SOCETH-2026, title: 'SOC engagements: Ethics risks with tool providers', publisher: Journal of Accountancy,
    type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/apr/soc-engagements-ethics-risks-with-tool-providers/",
    date: '2026-04-06', access: full, locator: Paragraphs 1-3 and 'Network firm considerations'}
  - {ref: JOFA-ETHAI-2026, title: Accounting ethics in the age of AI (AICPA Professional Ethics Division staff),
    publisher: Journal of Accountancy, type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/',
    date: '2026-08-05', access: full, locator: Section 'AI services can raise independence concerns for attest clients'}
  - {ref: JOFA-PEEC-2026, title: PEEC to continue discussions on alternative practice structures, publisher: Journal
      of Accountancy, type: press, url: "https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures/",
    date: '2026-08-10', access: full, locator: Paragraph 1}
  - {ref: JOFA-PEER-2026, title: AICPA guides peer reviewers to address SOC 2 risks, publisher: Journal of Accountancy,
    type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/",
    date: '2026-05-14', access: full, locator: Paragraph 3 (AICPA quote)}
  - {ref: PKF-DAS-2026, title: "PKF O'Connor Davies Adopts AI-Enabled DAS Suite Powered by Caseware Verity, and\
      \ Joins the Caseware Agentic Pioneer Program", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program",
    date: '2026-10-08', access: full, locator: Subtitle}
  last_reviewed: '2026-10-21'
  notes: >-
    Idea: AICPA ethics material exists, but no named firm has described this screening for an AI platform. Routed
    in part to acceptance-independence and soc-attestation.
- id: assurance-private-company-13
  title: >-
    Idea: put staff-built AI agents, automations and macros through the firm's change management
  archetype: assurance
  module: private-company
  function: technology-it
  work_types:
  - software-systems
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Staff can now build their own agents, dashboards and automations ('vibe coding'). A Cherry Bekaert partner says
    that as this spreads across clients, a more rigorous process is expected (JOFA-CYBERCK-2026).
  solution: >-
    Agents or automations that will be widely used get ownership, review and formal change management; the firm
    keeps records of how each was created and what it does; AI agents with data access get sandboxing and restricted
    tool, API and credential permissions (JOFA-CYBERCK-2026).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a
    source_ref: JOFA-CYBERCK-2026
  prerequisites:
  - Named owner for each tool
  - A register of staff-built automations
  - Technical guardrails for agent access (JOFA-CYBERCK-2026)
  risks_and_guardrails:
  - >-
    Without a retained record of how an agent was built, scalable and secure deployment is hard, per a SAV Associates
    partner (JOFA-CYBERCK-2026)
  - >-
    Agent access to enterprise data, credentials and APIs introduces new attack paths (JOFA-CYBERCK-2026)
  human_checkpoints:
  - Reviewer approves an automation before it touches client files
  role_evolution: Technical staff and senior associates become reviewers of staff-built tools.
  evidence_grade: D
  sources:
  - {ref: JOFA-CYBERCK-2026, title: New checklist helps CPAs manage AI cyber risks, publisher: Journal of Accountancy,
    type: press, url: "https://www.journalofaccountancy.com/news/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/",
    date: '2026-10-01', access: full, locator: 'Paragraphs on vibe coding, change management and agent guardrails'}
  last_reviewed: '2026-10-21'
  notes: >-
    Idea: discussed by practitioners quoted in one article; no firm has described the process in operation.
- id: assurance-private-company-14
  title: 'Idea: tell the professional-liability insurer how AI is used and check for AI exclusions'
  archetype: assurance
  module: private-company
  function: risk-compliance-legal
  work_types:
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Insurers say errors from unvetted AI output can be covered like any error unless a policy excludes AI, and that
    exclusions may come if claims rise (BUSINESSINS-AIEO-2026). A CNA risk director, writing in the Journal of Accountancy,
    says the lack of a CPA-specific AI standard is unlikely to help defend a negligence claim that work was not
    properly reviewed (JOFA-GENAIDISC-2025); CNA underwrites the AICPA's professional liability programme.
  solution: >-
    The firm asks its broker whether the policy has an AI exclusion or sublimit, tells the insurer how AI is used,
    and keeps the policy, review and consent records that show the output was verified (BUSINESSINS-AIEO-2026; JOFA-GENAIDISC-2025).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a
    source_ref: BUSINESSINS-AIEO-2026
  prerequisites:
  - Broker conversation and a written answer on AI coverage
  - An AI use inventory (see 02)
  risks_and_guardrails:
  - >-
    The insurer commentary is general and uses law and medicine as examples; accounting-firm underwriting practice
    was not found
  - >-
    Insurers said exclusions are discouraged by competitive pressure for now (BUSINESSINS-AIEO-2026)
  - Shadow AI use makes it hard to trace how an error arose (BUSINESSINS-AIEO-2026)
  human_checkpoints:
  - Managing partner reviews coverage annually
  role_evolution: Risk partner adds AI to the insurer renewal discussion.
  evidence_grade: D
  sources:
  - {ref: BUSINESSINS-AIEO-2026, title: "AI use amplifies professional liability risks (insurer commentary; examples\
      \ are mainly law and medicine, not accounting)", publisher: Business Insurance, type: press, url: 'https://www.businessinsurance.com/ai-use-amplifies-professional-liability-risks/',
    date: '2026-06-26', access: full, locator: Paragraphs 2-6 and 'Insurers cautious on E&O exclusions'}
  - {ref: JOFA-GENAIDISC-2025, title: "Should I disclose my use of gen AI to clients? (Professional Liability Spotlight;\
      \ author is a risk consulting director at CNA, underwriter of the AICPA Professional Liability Insurance Program)",
    publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2025/apr/should-i-disclose-my-use-of-gen-ai-to-clients/",
    date: '2025-04-01', access: full, locator: 'Section ''Legal and ethical compliance'', final paragraph'}
  last_reviewed: '2026-10-21'
  notes: 'Idea: no accounting-firm insurer statement on AI exclusions was found.'
- id: assurance-private-company-15
  title: >-
    Revisit fee model, fee disclosure and value pricing when AI shortens private-company engagements
  archetype: assurance
  module: private-company
  function: finance-accounting
  work_types:
  - client-interaction
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Most of the 54 firms in the AICPA benchmark anticipate raising fees (74%) while only 13% track the share of
    engagements on value-billing agreements (CPACOM-ATR-2025). In a Thomson Reuters survey 78% of tax, audit and
    accounting respondents mainly bill hourly (TR-SOTP-2026), and one-third say their firms have not yet adapted
    commercial models while nearly half feel pressure to gain financially from AI (TRI-FOP-2026).
  solution: >-
    The firm decides how AI-shortened hours are priced and explained to clients. The IRS OPR alert warns tax practitioners
    that billing for manual time not spent, or double billing AI-assisted work, may violate the Circular 230 fee
    rule and says cost savings should be passed on openly (IRS-OPR-2026); the equivalent for audits is not stated
    in AICPA guidance found.
  outcomes:
  - lever: cost
    description: >-
      74% of 54 firms anticipate increasing fees; 13% track the share of engagements on value-billing agreements
    figure: 74%; 13%
    measures: >-
      Shares of the 54 firms anticipating fee increases as a growth strategy; tracking engagements on value billing
      agreements (fixed fee billed in advance) as a metric
    provenance: independent
    source_ref: CPACOM-ATR-2025
  - lever: cost
    description: 78% of respondents primarily use hourly billing
    figure: 78%
    measures: >-
      Share of the 600 respondents (tax, audit and accounting firms; 64% US) whose firms primarily use hourly billing
    provenance: vendor-published
    source_ref: TR-SOTP-2026
  prerequisites:
  - Time and cost data from the baseline in 08
  - A pricing policy and a client message
  risks_and_guardrails:
  - >-
    Fee disclosure duties for audits are not stated in the AICPA guidance read; the OPR alert is tax-specific (IRS-OPR-2026)
  - >-
    No mid-market fee-reduction case was found; the single reported case in the landscape file (KPMG and its UK
    auditor, low-reliability secondary report, not opened here) involves a Big Four client
  human_checkpoints:
  - Engagement partner and managing partner approve pricing for AI-shortened work
  role_evolution: >-
    Partners spend more time pricing and explaining; the TR paper describes three strategic paths, including productivity
    without added headcount (TRI-FOP-2026).
  evidence_grade: C
  sources:
  - {ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report (2025 CPA.com and AICPA Audit Benchmark Survey;\
      \ 54 US firms; not representative)", publisher: CPA.com and AICPA, type: survey, url: 'https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf',
    date: 2025-12, access: full, locator: p. 9 growth strategies chart (74%); p. 22 (13%)}
  - {ref: TR-SOTP-2026, title: "2026 State of Tax Professionals Report (600 respondents; small = 1-3, midsize =\
      \ 4-29, large = 30+ professionals)", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2026/06/2026-State-of-Tax-Professionals-Report.pdf",
    date: 2026-06, access: full, locator: p. 4 (78% hourly)}
  - {ref: TRI-FOP-2026, title: "What the 2026 Future of Professionals Report says tax and audit firm leaders should\
      \ be prioritizing now", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026",
    date: '2026-07-21', access: full, locator: Paragraph on financial pressure and commercial models}
  - {ref: IRS-OPR-2026, title: 'OPR Alert 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax
      Practice', publisher: IRS Office of Professional Responsibility, type: regulator, url: 'https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70',
    date: '2026-06-24', access: full, locator: Section on 10.27 fees}
  last_reviewed: '2026-10-21'
  notes: >-
    Grade C: vendor and benchmark survey figures; no mid-market firm has published a pricing change attributed to
    AI. Economics are covered in the archetype's economics.md.
- id: assurance-private-company-16
  title: >-
    AI-assisted preparation, compilation and review (SSARS) workflow with disclosure checks, aimed at peer-review
    nonconformity
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Reviews and compilations are the largest part of small-firm peer-review samples. In 2025 reports: Tennessee
    13 of 99 reviews and 7 of 219 compilations or preparations nonconforming (TSCPA-PEERREVIEW-2025); Minnesota
    14 of 75 reviews and 9 of 189 compilations (MNCPA-PEERREVIEW-2025); Connecticut 5 of 63 reviews and 6 of 114
    (CTCPA-PEERREVIEW-2025). Oklahoma's administering entity lists 8 of 40 and 7 of 41 reviews in two overlapping
    categories (OSCPA-PEERREVIEW-2025). The AICPA update names reporting departures and risk assessment as recurring
    issues (ICPAS-PRAF-2026).
  solution: >-
    Firms use one engagement platform for audits and for preparation, compilation and review: Citrin Cooperman,
    Withum and EisnerAmper adopted the DAS suite including DAS PCR (CITRIN-DAS-2026; WITHUM-DAS-2026; EISNER-DAS-2026).
    Caseware's Disclosure Checklist Agent returns citation-backed answers that the auditor accepts, refines or overrides
    inside the DAS workflow (CASEWARE-VERITY-2026), and in beta one firm used it to catch incorrectly answered checklist
    items (CASEWARE-CWX-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: n/a
    source_ref: CASEWARE-VERITY-2026
  prerequisites:
  - Engagement platform that covers PCR work, not only audits
  - Disclosure checklists in a form the agent can read
  - A firm rule on when AI-drafted statements may be issued
  risks_and_guardrails:
  - >-
    No AICPA or Accounting and Review Services Committee AI guidance for SSARS engagements was found (landscape;
    confirmed by search)
  - >-
    The sources do not say which Caseware agents run in the PCR module; the named agent is described in the audit
    workflow (CASEWARE-VERITY-2026)
  - Peer-review nonconformity rates differ by state and are not comparable across reports
  human_checkpoints:
  - Accountant reviews and signs the compilation or review report
  - Reviewer clears each overridden or disputed disclosure answer
  role_evolution: >-
    Staff review citation-backed answers rather than search statements manually (CASEWARE-CWX-2026).
  evidence_grade: C
  sources:
  - {ref: CITRIN-DAS-2026, title: 'Citrin Cooperman & Company, LLP Adopts AI-Enabled DAS Suite Powered by Caseware',
    publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth",
    date: '2026-07-13', access: full, locator: 'Paragraph 2 (DAS Audit, DAS PCR, DAS EBP)'}
  - {ref: WITHUM-DAS-2026, title: Withum Fully Adopts DAS Powered by the Caseware Verity AI Platform, publisher: Caseware,
    type: vendor, url: "https://www.caseware.com/news/withum-fully-adopts-das-powered-by-the-caseware-verity-ai-platform-to-drive-its-future-ready-audit-practice",
    date: '2026-06-03', access: full, locator: 'Paragraph 2 (DAS, DAS PCR, DAS EBP)'}
  - {ref: EISNER-DAS-2026, title: EisnerAmper Leverages DAS Powered by Caseware to Unify Audit and Build an Agentic
      Future, publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/eisneramper-leverages-das-powered-by-caseware-to-unify-audit-and-build-an-agentic-future-across-its-multi-vertical-practice",
    date: '2026-06-25', access: full, locator: 'Paragraph 1 (modules for preparation, compilation and review)'}
  - {ref: CASEWARE-VERITY-2026, title: "Caseware Launches Caseware Verity to Bring Workflow-Native AI Agents Directly\
      \ Into Assurance Engagements", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements",
    date: '2026-05-20', access: full, locator: Disclosure Checklist Agent paragraph}
  - {ref: CASEWARE-CWX-2026, title: "CwX 2026: How agentic AI is transforming audit and assurance (blog on a May\
      \ 2026 conference session)", publisher: Caseware, type: conference, url: "https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance",
    date: '2026-06-17', access: full, locator: Section 'Disclosure Checklist Agent'}
  - {ref: TSCPA-PEERREVIEW-2025, title: Annual Report on Peer Review Activities 2025 (Tennessee; 424 firms enrolled),
    publisher: Tennessee Society of CPAs, type: professional-body, url: "https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf",
    date: '2026-03-31', access: full, locator: Table 2(c)}
  - {ref: MNCPA-PEERREVIEW-2025, title: 2025 Annual Report on Peer Review Activities (Minnesota and North Dakota;
      269 firms), publisher: Minnesota Society of CPAs, type: professional-body, url: "https://www.mncpa.org/mncpa/media/Documents-Shared/peer-review/2025-MNCPA-annual-report-on-peer-review-activities.pdf",
    date: 2026-02, access: full, locator: Table 2(c)}
  - {ref: CTCPA-PEERREVIEW-2025, title: "Annual Report on Peer Review Activities (Connecticut; 249 firms administered\
      \ at 31 Dec 2025)", publisher: Connecticut Society of CPAs, type: professional-body, url: 'https://www.ctcpas.org/storage/assets/PDFs/Annual%20Report%20on%20PR%20Activities.pdf',
    date: '2026-01-12', access: full, locator: Table 2(c)}
  - {ref: OSCPA-PEERREVIEW-2025, title: "2025 Annual Report on Peer Review Activities (Oklahoma, South Dakota and\
      \ Kansas; 387 firms)", publisher: Oklahoma Society of CPAs, type: professional-body, url: "https://prod.oscpa.com/storage/assets/Peer%20Review/Annual%20Report/2025%20OSCPA%20Peer%20Review%20Activities.pdf",
    date: 2026-03, access: full, locator: Table 2(c)}
  - {ref: ICPAS-PRAF-2026, title: "Peer Review Alliance Forum (Virtual): 2026 Forum - Participant Slides (catalogue\
      \ description of an AICPA Peer Review update; slides themselves not opened)", publisher: Illinois CPA Society,
    type: conference, url: "https://learn.icpas.org/AssetListing/Peer-Review-Alliance-Forum-Virtual-17790/2026-Forum-%E2%80%93-Participant-Slides-29361",
    date: '2026', access: full, locator: Catalogue description}
  last_reviewed: '2026-10-21'
  notes: >-
    Grade C: vendor claim. Maturity 'announced' for the AI element; the DAS suite itself is in production at the
    named firms. Compilation totals: Tennessee 2 of 44 plus 5 of 175 = 7 of 219; Minnesota 5 of 51 plus 4 of 138
    = 9 of 189; Connecticut 4 of 47 plus 2 of 67 = 6 of 114 (sums of the two reported categories). The preparation
    and compilation side may belong to a future accounting and client-advisory archetype.
```

## 3. Module notes

### Processes and key steps (governance view)

| Step | What governance adds | Work types | Existing module |
|---|---|---|---|
| Accept and continue a private-company client | Ask how the entity uses AI in financial reporting; heavy reliance on AI output can bear on acceptance, evidence access and management's skills [AT-AICPAPA-2026] | review-assurance, expert-judgment | acceptance-independence, planning-risk-assessment |
| Choose methodology and tools | Methodology and AI come as one package (DAS on Caseware, gtap, Ask Luca); check the vendor's governance claims and contract terms [CASEWARE-DASUPD-2026; JOFA-SOCETH-2026] | expert-judgment, coordination-scheduling | quality-management |
| Write AI into the QM system | Risk assessment, responses, monitoring, annual evaluation; peer review tests whether it operated [AICPA-QMPEER-2026] | review-assurance | quality-management |
| Plan and assess risk for a smaller entity | AI-suggested risks must be tailored, not templated [AICPA-QMPEER-2026; CASEWARE-CWX-2026] | review-assurance | planning-risk-assessment |
| Test on client data that is often poor or hard to reach | 60% of 54 firms cite poor client data and 53% lack access to client systems as blockers [CPACOM-ATR-2025]; AI extraction can capture incomplete data from a custom system (hypothetical case) [CCAB-CASE2-2026] | data-reporting | substantive-testing |
| Prepare, compile or review under SSARS | Same platform, checklists and review as audits; no AI guidance for SSARS found | document-production, review-assurance | (this module, entry 16) |
| Complete and report | Disclosure checklist agents with citation-backed answers [CASEWARE-VERITY-2026] | review-assurance | completion-reporting |
| Review, EQR and file documentation | Partner confirms tool is firm-approved and used correctly [AICPA-AIPA-2026] | review-assurance | quality-management |
| Monitor, evaluate annually, face peer review | Annual QM evaluation; annual practice questionnaire; triennial review [AICPA-APQ-2026; CPACOM-SQMS-2026] | review-assurance | quality-management |
| Agree client terms | Engagement-letter wording, consent, client objections [CFODIVE-AIPA-2026; ACCA-ENGLTR-2026] | client-interaction | (this module, entry 3) |

### Common pain points

- **Governance lags use.** More than one-third of surveyed tax and audit professionals admit using unauthorised AI tools [TRI-FOP-2026]; Karbon reports data-security concern at 83% of respondents, up 7% year on year in the report's wording [KARBON-AI-2026, p. 17].
- **Staff skills and client data.** 66% of 54 firms rank untrained staff among top blockers, 60% poor client data, 53% lack of access to client systems and 53% budget [CPACOM-ATR-2025, p. 8].
- **No plan.** 75% of the 54 firms have no formal documentation of audit transformation [CPACOM-ATR-2025, p. 9].
- **Quality systems under stress.** Leading system-review deficiency reasons in 2025: Tennessee engagement performance 6 and monitoring 5 of 16 [TSCPA-PEERREVIEW-2025]; Oklahoma administering entity engagement performance 19, monitoring 13 and human resources 8 of 45 [OSCPA-PEERREVIEW-2025]; Connecticut acceptance and continuance 3 and engagement performance 3 of 9 [CTCPA-PEERREVIEW-2025].
- **Overreliance on platforms.** The AICPA says some firms lean too heavily on third-party SOC platforms without applying required professional judgment [JOFA-PEER-2026].
- **Small-firm monitoring.** For Yellow Book organisations the GAO says self-monitoring by a very small firm is permitted but may be less effective [GAO-YBFAQ-2025].

### Metrics and benchmarks

| Metric | Value | What it measures | Source | Provenance |
|---|---|---|---|---|
| Nonconforming engagements, Tennessee 2025 | 34 of 448 (8%); reviews 13 of 99; single audits 2 of 11; ERISA 2 of 21; other audits 8 of 53; compilations with disclosures 2 of 44, omitting disclosures 5 of 175 | Engagements not performed or reported on in conformity with professional standards in all material respects, among engagements reviewed | [TSCPA-PEERREVIEW-2025] | independent |
| Same, Connecticut 2025 | 18 of 256 (7.03%); single audits 3 of 9; reviews 5 of 63 | Same | [CTCPA-PEERREVIEW-2025] | independent |
| Same, Minnesota and North Dakota 2025 | 38 of 418 (9%); reviews 14 of 75; single audits 3 of 15; ERISA 2 of 16 | Same | [MNCPA-PEERREVIEW-2025] | independent |
| Same, Oklahoma, South Dakota, Kansas 2025 | 86 of 525 (16.38%); single audits 12 of 40 (30%); other audits under SAS 20 of 61 (32.79%); reviews 8 of 40 | Same; the report lists overlapping categories, so do not sum | [OSCPA-PEERREVIEW-2025] | independent |
| System review results, 2025 | Pass: Tennessee 40 of 46 (87%); Connecticut 28 of 34 (82.35%); Minnesota 41 of 44 (93%); Oklahoma group 35 of 55 (64%) | Share of system reviews accepted with a pass rating | four reports above | independent |
| Plan audits with major deficiencies | 30% (2020 form year; 307 audit reports sampled); 39% in the 2015 study (2011 form year) | EBSA's estimate of audits with major deficiencies against GAAS | [EBSA-AUDITQ-2023] | independent |
| Firms without formal transformation documentation | 75% of 54 | Self-reported benchmark responses; not representative | [CPACOM-ATR-2025] | independent |
| Firms with a written AI policy | 57% of 162 (CPAFMA); 21% (Karbon) | Different samples and wording; see use case 02 | [CPAFMA-WINSOME-2026; KARBON-AI-2026] | independent; vendor-published |
| AI accuracy and time | 94% on golden dataset items; 15-20 minutes to under two; 2.7 review hours per checklist | Vendor beta results | [CASEWARE-VERITY-2026; CASEWARE-CWX-2026] | vendor-published |
| AI investment and restatements | 5.0% lower likelihood of restatement per one-standard-deviation change in recent AI investment | 36 largest US firms, 2010-2019, pre-GenAI | [FEDYK-RAST-2022] | independent (adjacent) |
| Staff view of GenAI at a UK mid-tier firm | 74% faster on some tasks; 22% marked rise in output; 72% fear errors; 52% worry about client information | Survey of staff at Beever and Struthers | [ICAS-AMBS-2025] | independent (adjacent) |
| Small-firm technology maturity | 63% of large firms (30+ professionals) proactive or optimised against 35% of small firms (1-3) and 54% of small firms ad hoc or reactive | Tax-focused survey of 600; respondents 56% midsize | [TR-SOTP-2026, pp. 5, 9] | vendor-published |
| Top issue by size | Managing technology and AI change ranks first for five-year impact in all six firm-size groups | AICPA PCPS biennial survey | [AICPA-TOPISSUES-2026] | independent |

**What peer reviewers find.** The four 2025 reports give engagement types, not causes, and contain no AI finding. The AICPA's 2026 peer review update names recurring problems in compilations, reviews and audits as risk assessment, control documentation, accounting standard changes and reporting departures, and lists AI and automation among emerging areas [ICPAS-PRAF-2026]. The AICPA's May 2026 reviewer alert on SOC 2 asks reviewers to examine a firm's use of technology and external platforms, the reasonableness of timelines and whether engagements are tailored, and may sample about five engagements from different partners and compare reports [JOFA-PEER-2026]. No peer-review finding on AI in audits, reviews or compilations was found.

### Guardrails and regulatory points

- **AICPA Code.** Competence and due care (ET 1.300.001 and 2.300.001), the confidential client information rule (ET 1.700.001) and the independence rules apply however the tool is sourced; independence concerns can arise from building or hosting an AI system for an attest client [JOFA-ETHAI-2026].
- **Practice aid (13 Oct 2026).** Nonauthoritative; 51 pages; part 1 covers the entity's AI in reporting and controls, part 2 the firm's own use (QM, supervision, review, skepticism, planning, partner responsibilities); risk-of-material-misstatement and evidence content and more Q&As to follow [AICPA-AIPA-2026; CFODIVE-AIPA-2026; AICPA-AIPADL-2026].
- **Engagement letters.** The practice aid's Q&A says AICPA standards do not require disclosure of AI use but law, contract or firm policy may, and some states require advance disclosure of certain AI uses [CFODIVE-AIPA-2026]. The 2025 Journal of Accountancy article names California and Utah and the Gramm-Leach-Bliley safeguards duties for CPA firms [JOFA-GENAIDISC-2025].
- **Quality management.** SQMS No. 1 implementation deadline 15 Dec 2025, annual evaluation within a year [CPACOM-SQMS-2026]. Yellow Book 2024 system of quality management by 15 Dec 2025 with the first evaluation by 15 Dec 2026 [GAO-YBFAQ-2025]. PCAOB QC 1000 amendments adopted 9 Sep 2026, effective 15 Dec (year not printed in the text read), pending SEC approval; this governs issuer audits, so it reaches only firms with public-company clients [JOFA-QC1000-2026]. SSARS Nos. 26 (quality management) and 27 exist per a CPE listing, text not read [MNCPA-SSARSCPE-2026].
- **Independence and ownership.** PEEC is discussing a second exposure draft on alternative practice structures, including a network-firm definition change and a ban on attest-client investment [JOFA-PEEC-2026].
- **Tax-side counterpart.** IRS OPR Alert 2026-19 ties AI use to Circular 230 firm procedures (section 10.36) and fee rules (section 10.27) and urges enterprise-approved AI; the section 7216 consent question for AI tools is open [IRS-OPR-2026; CPAPA-7216-2026]. Route to the tax archetype.
- **Other bars.** ABA Formal Opinion 512 (29 Jul 2024) is cited in the Journal of Accountancy as the lawyer analogue on verification and consent; the opinion itself was not readable [JOFA-GENAIDISC-2025; ABA-OP512-2024]. No SRA, state bar or medical-council material was needed or reviewed for this accounting module.
- **Liability.** Insurers quoted by Business Insurance say standard E&O generally covers AI-related negligence unless a specific exclusion applies, and exclusions may follow rising claims; the article is general [BUSINESSINS-AIEO-2026].

### Frontier signals (dated)

- **2026-10-13.** AICPA practice aid issued; more guidance on risk assessment and evidence to be added; more Q&As expected [AICPA-AIPA-2026].
- **2026-10-19.** AICPA and AIUC announce a CPA-led engagement combining SOC 2 and AIUC-1 for AI systems; multiple firms already deliver it and a full launch is expected in early 2027 [AICPA-AIUC-2026]. Route to assurance-over-ai.
- **2026-10-08.** PKF O'Connor Davies adopts the DAS suite and joins Caseware's Agentic Pioneer Program to co-develop proprietary agents [PKF-DAS-2026]. EisnerAmper (25 Jun), Withum (3 Jun) and Citrin Cooperman (13 Jul) announced DAS adoption [EISNER-DAS-2026; WITHUM-DAS-2026; CITRIN-DAS-2026].
- **2026-09 onward.** Accountancy Europe's paper for small and medium-sized practices on generative AI in audit (summary only read) [ACCTEU-GENAI-2026]; the FRC's guidance of 30 Mar 2026 is the first from any audit regulator, which the FRC says codifies good practice and does not respond to quality deficiencies [FRC-NEWS-2026].
- **2026-06 (week of 1 Jun).** AICPA annual practice questionnaire for all enrolled firms launches; the AICPA's 2026 peer review update names AI and automation among emerging areas [AICPA-APQ-2026; ICPAS-PRAF-2026].
- **2026-06-25.** First QM peer reviews under way; AICPA calls year one test-and-learn [AICPA-QMPEER-2026].
- **2026-05-20.** Caseware launches Verity with agents aimed at the full engagement lifecycle and a stated goal of automating 50% of the workflow [CASEWARE-VERITY-2026].
- **2026-05-07.** Grant Thornton US announces gtap, to reach private company audits first [GT-GTAP-2026].
- **2026-05-14.** AICPA Peer Review Board alert on third-party SOC 2 platforms [JOFA-PEER-2026].
- **2026-12-15 (dated ahead).** Yellow Book first QM evaluation due [GAO-YBFAQ-2025]; the PCAOB QC 1000 effective date of 15 Dec is pending SEC approval, year not printed in the text read [JOFA-QC1000-2026].
- **Governmental audit watch item.** The AICPA's governmental quality centre lists emerging ethics, quality management and AI-related guidance as items it is monitoring, so no AI guidance exists yet for single audits [GAQC-DEV-2026].

### Workforce and role effects

- Employment of 22-25 year olds in AI-exposed occupations is 19% below trend in ADP payroll data through June 2026, through reduced hiring; the study is economy-wide, not accounting-specific [STANFORD-CANARIES-2026].
- At the 36 largest US firms, accounting employees fell 3.6% after three years and 7.1% after four following a one-standard-deviation change in recent AI investment [FEDYK-RAST-2022].
- Karbon reports 20% of respondents have started changing organisational design, including outsourcing junior roles and filling junior roles with AI [KARBON-AI-2026, p. 17].
- More than one-quarter of tax and audit professionals say they would not accept a job at a firm lacking professional-grade AI; almost one in three say they would consider leaving if AI expectations are unmet within two years [TRI-FOP-2026].
- Peer reviewers and QM leaders: managing partners become accountable owners of the QM system and are interviewed by reviewers [AICPA-QMPEER-2026]. Partners must understand tools and ensure staff use approved ones [AICPA-AIPA-2026].
- Juniors: vendors present platforms as training aids [WITHUM-DAS-2026; CITRIN-DAS-2026]; Thomson Reuters says supervision must exist before automation erodes junior development [TRI-FOP-2026].

### Objections and concerns practitioners raise

- **"The practice aid is nonauthoritative, so we can wait."** The guidance is nonauthoritative, but peer reviewers test whether the QM system works, and the AICPA says leaders should expect questions on monitoring [AICPA-AIPADL-2026; AICPA-QMPEER-2026].
- **"We are too small for governance."** Karbon reports firms with an AI policy saving more time (self-reported) [KARBON-AI-2026, p. 18]; the GAO lets very small Yellow Book organisations self-monitor, while noting the limit [GAO-YBFAQ-2025].
- **"Staff will use it anyway."** More than a third of surveyed professionals already use unauthorised tools [TRI-FOP-2026].
- **"Clients will object."** ACCA says a restriction may increase cost or mean the firm cannot act, and a blanket ban may be unworkable [ACCA-ENGLTR-2026].
- **"The vendor has governed it."** Governance claims are vendor-published; the AICPA warns about leaning on platforms [CASEWARE-VERITY-2026; JOFA-PEER-2026].
- **Errors and bias.** 72% of staff at a UK mid-tier firm feared incorrect output [ICAS-AMBS-2025]; in an IDC survey sponsored by Caseware, 79% rated algorithmic bias in AI used for critical functions as moderately, very or extremely significant and 55% were willing or very willing to accept lower AI performance for stronger security or safety [IDC-CASEWARE-2026].
- **Time saved does not equal output.** 74% said tasks were faster; 22% saw a marked rise in output [ICAS-AMBS-2025].

### Interview probes

1. Show me where AI appears in your system of quality management risk assessment. What monitoring ran in the first year, and what does the annual evaluation say about AI?
2. Which AI tools touched a client file last busy season, who approved them, and how do you know staff did not use others? Is tool use recorded on the file?
3. What do your engagement letters say about AI? What did you do the last time a client asked you not to use it?
4. If your methodology vendor's agent gave a wrong checklist answer or missed a risk, how would you find out? What have you tested against answers you already know?
5. What did your last peer reviewer ask about technology, platforms and tailoring? Did you list AI when you completed the annual practice questionnaire?

## 4. Routed to other modules

| Item | Target module | Why |
|---|---|---|
| Entity's own use of AI in financial reporting, and AI at acceptance and continuance (practice aid part 1; heavy AI use may bear on evidence and management skills) [AT-AICPAPA-2026] | planning-risk-assessment; assurance-over-ai | Risk assessment and client-side AI |
| Disclosure Checklist Agent time saving (2.7 review hours) and citation-backed answers [CASEWARE-VERITY-2026] | completion-reporting | Disclosure checklists are a completion step; also used here in entries 06 and 16 |
| Document Intelligence Agent and Risk Suggestion Agent [CASEWARE-VERITY-2026; CASEWARE-CWX-2026] | substantive-testing; planning-risk-assessment | Extraction into workpapers and AI-suggested risks |
| gtap "works with data from any ERP" and full-population analysis, private company audits first [GT-GTAP-2026] | substantive-testing (data acquisition in value-chain.md section 4) | Non-ERP and any-ERP data ingestion |
| Engagement-level supervision, recording AI use on the file, automation bias [JOFA-ETHAI-2026; AICPA-AIPA-2026] | quality-management (entries 17, 19, 20, 23) | Already covered; not repeated here |
| Firm-level tool certification and recertification [FRC-NEWS-2026] | quality-management (entries 01-09) | Large-firm mechanics already covered |
| SOC 2 platform reliance and reviewer alert [JOFA-PEER-2026]; ethics risks with tool providers [JOFA-SOCETH-2026]; AICPA and AIUC combined offering [AICPA-AIUC-2026] | soc-attestation; assurance-over-ai | SOC and AI-assurance practice |
| PEEC alternative practice structure drafts and attest-client investment ban [JOFA-PEEC-2026] | acceptance-independence | Ownership and independence |
| EBSA audit-quality findings, firm-size link, EBPAQC membership, DAS EBP module, CalCPA session on AI in plan audits [EBSA-AUDITQ-2023; CITRIN-DAS-2026] | benefit-plan-audits (proposed in landscape) | Own regulator and quality centre. EBSA's findings: 30% major deficiencies; clear link between number of plan audits a firm does and quality; audits by EBP Audit Quality Center members had a significantly lower deficiency rate [EBSA-AUDITQ-2023] |
| Yellow Book quality management, single-audit quality review, GAQC AI watch item [GAO-YBFAQ-2025; GAQC-DEV-2026] | nonprofit-government (proposed in landscape) | Government audit regime |
| OPR Alert 2026-19, section 7216 consent, Circular 230 sections 10.27 and 10.36 [IRS-OPR-2026; CPAPA-7216-2026] | Tax archetype: compliance modules and guardrails | Tax practice rules |
| Field data from 79 small and mid-sized firms using one AI accounting platform: 55% more weekly client support; about 8.5% of time moved from data entry [STANFORD-CHOIXIE-2025] | Future accounting and client-advisory archetype (bookkeeping and close) | Bookkeeping, not assurance; one vendor's customers; abstract only read. It also bears on quality of client records feeding compilations |
| Fee pressure, pricing models [CPACOM-ATR-2025; TR-SOTP-2026] | economics.md (archetype file) | Archetype-level economics |
| Employment effects on early-career staff [STANFORD-CANARIES-2026; FEDYK-RAST-2022] | workforce.md (archetype file) | Archetype-level workforce |

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ABA-OP512-2024 | ABA Formal Opinion 512, Generative Artificial Intelligence Tools (cited in the Journal of Accountancy article JOFA-GENAIDISC-2025 with the date 29 Jul 2024; the PDF returned 403 to curl and to the text mirror, so it was not read) | American Bar Association | professional-body | https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf | 2024-07-29 | search-only |
| ACCA-ENGLTR-2026 | Engagement letters, AI and PCRT (UK technical advice; PCRT is the UK tax conduct guidance, updated Jan 2026) | ACCA | professional-body | https://www.accaglobal.com/gb/en/technical-activities/uk-tech/in-practice-ezine-archive/In-Practice-archive-2026/september/Engagement-letters-AI-and-PCRT.html | 2026-09 | full |
| ACCTEU-GENAI-2026 | Generative AI in audit and assurance: use cases and examples (paper for small and medium-sized practices; read only through a Spanish-language summary on the INCP site) | Accountancy Europe (summary by INCP Colombia) | professional-body | https://incp.org.co/?p=136646 | 2026-09 | search-only |
| AICPA-AIPA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing (news release for the practice aid 'Artificial Intelligence (AI) Considerations for Financial Statement Auditors'; also keyed AICPA-PA-2026 in the archetype) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | full |
| AICPA-AIPADL-2026 | Explore new AICPA guidance on artificial intelligence (AI) and the financial statement audit (download page; the 1.5 MB practice aid file is members-only and was not opened) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/article/explore-new-aicpa-guidance-on-artificial-intelligence-ai-and-the-financial-statement-audit | 2026-10-12 | full |
| AICPA-AIUC-2026 | AICPA partners on new offering that assures AI systems and agents | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/aicpa-partners-on-new-offering-that-assures-ai-systems-and-agents.html | 2026-10-19 | full |
| AICPA-APQ-2026 | Annual Practice Questionnaire for Peer Review (FAQ page; page undated, launch week of 1 Jun 2026) | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/resources/article/annual-practice-questionnaire-for-peer-review-faqs | 2026-06 | full |
| AICPA-QMPEER-2026 | Peer reviews of QM systems: What firms need to know now (Tim Kindem, AICPA Technical Director, Peer Review) | AICPA & CIMA Insights Blog | professional-body | https://www.aicpa-cima.com/professional-insights/article/peer-reviews-of-qm-systems-what-firms-need-to-know-now | 2026-06-25 | full |
| AICPA-TOPISSUES-2026 | AICPA Survey Cites Change Management for Technology and AI as Top Long-Term Issue Facing Accounting Firms (PCPS CPA Firm Top Issues Survey) | CPA Practice Advisor | survey | https://www.cpapracticeadvisor.com/2026/06/23/aicpa-survey-cites-change-management-for-technology-and-ai-as-top-long-term-issue-facing-accounting-firms/185547/ | 2026-06-23 | full |
| AT-AICPAPA-2026 | AICPA releases practice guide for auditors dealing with AI | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai | 2026-10-14 | full |
| BUSINESSINS-AIEO-2026 | AI use amplifies professional liability risks (insurer commentary; examples are mainly law and medicine, not accounting) | Business Insurance | press | https://www.businessinsurance.com/ai-use-amplifies-professional-liability-risks/ | 2026-06-26 | full |
| CAQ-RSM-2026 | Shaping the future of assurance: Advancing AI in the audit (blog by RSM's assurance digital leader) | Center for Audit Quality | professional-body | https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit | 2026-08-25 | full |
| CASEWARE-CWX-2026 | CwX 2026: How agentic AI is transforming audit and assurance (blog on a May 2026 conference session) | Caseware | conference | https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance | 2026-06-17 | full |
| CASEWARE-DASUPD-2026 | AICPA Dynamic Assurance Solution (DAS) Expands Connected Audit Workflows with New Risk, Controls and PCAOB Capabilities | Caseware | vendor | https://www.caseware.com/news/aicpa-dynamic-assurance-solution-das-expands-connected-audit-workflows-with-new-risk-controls-and-pcaob-capabilities | 2026-06-08 | full |
| CASEWARE-VERITY-2026 | Caseware Launches Caseware Verity to Bring Workflow-Native AI Agents Directly Into Assurance Engagements | Caseware | vendor | https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements | 2026-05-20 | full |
| CCAB-CASE2-2026 | Case Study 2: Professional Accountant in Practice - AI in Audit Evidence Collection (hypothetical teaching case, UK) | CCAB | professional-body | https://www.ccab.org.uk/case-study-2-professional-accountant-in-practice-ai-in-audit-evidence-collection/ | 2026-05-07 | full |
| CFODIVE-AIPA-2026 | AICPA issues guidance for AI-assisted auditing | CFO Dive | press | https://www.cfodive.com/news/aicpa-issues-guidance-ai-assisted-auditing/832907/ | 2026-10-13 | full |
| CITRIN-DAS-2026 | Citrin Cooperman & Company, LLP Adopts AI-Enabled DAS Suite Powered by Caseware | Caseware | vendor | https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth | 2026-07-13 | full |
| CPACOM-ATR-2025 | 2025 Audit Transformation Report (2025 CPA.com and AICPA Audit Benchmark Survey; 54 US firms; not representative) | CPA.com and AICPA | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 | full |
| CPACOM-SQMS-2026 | Waiting for peer review cycles puts firms at risk under SQMS 1 (Emily Remington, CPA.com; CPA.com is an AICPA affiliate that also sells audit-platform implementation) | CPA.com | professional-body | https://www.cpa.com/blog/2026/09/03/waiting-peer-review-cycles-puts-firms-risk-under-sqms-1 | 2026-09-03 | full |
| CPAFMA-WINSOME-2026 | AI Governance Shocks in the 2026 CPAFMA Digitally Driven Firm Survey (secondary blog summary of a survey of 162 firms run in Dec 2025 by Roman Kepczyk; original report not opened) | Winsome Marketing | survey | https://winsomemarketing.com/professional-services-marketing/ai-governance-shocks-in-the-2026-cpafma-digitally-driven-firm-survey | 2026-07-01 | full |
| CPAPA-7216-2026 | What to Settle Before Client Tax Data Touches AI (guest article by the co-founder of an AI implementation firm for accounting firms) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=191491 | 2026-10-12 | full |
| CTCPA-EMERGING-2026 | Changes to the Peer Review Program: Requirement for Completion of an Annual Emerging Areas Questionnaire (page undated; written before the June 2026 launch) | Connecticut Society of CPAs | professional-body | https://www.ctcpas.org/peer-review-emerging-areas | 2026 | full |
| CTCPA-PEERREVIEW-2025 | Annual Report on Peer Review Activities (Connecticut; 249 firms administered at 31 Dec 2025) | Connecticut Society of CPAs | professional-body | https://www.ctcpas.org/storage/assets/PDFs/Annual%20Report%20on%20PR%20Activities.pdf | 2026-01-12 | full |
| EBSA-AUDITQ-2023 | Audit Quality Study, November 2023 (fourth EBSA assessment of employee benefit plan audits; 2020 form year, 307 audit reports) | US Department of Labor, Employee Benefits Security Administration | regulator | https://www.dol.gov/sites/dolgov/files/ebsa/about-ebsa/our-activities/resource-center/publications/november-2023-audit-quality-study.pdf | 2023-11 | full |
| EISNER-AUDITAGENT-2026 | EisnerAmper Rolls Out In-House AI Audit Design Agent | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/20/eisneramper-rolls-out-in-house-ai-audit-design-agent/180020/ | 2026-03-20 | full |
| EISNER-DAS-2026 | EisnerAmper Leverages DAS Powered by Caseware to Unify Audit and Build an Agentic Future | Caseware | vendor | https://www.caseware.com/news/eisneramper-leverages-das-powered-by-caseware-to-unify-audit-and-build-an-agentic-future-across-its-multi-vertical-practice | 2026-06-25 | full |
| FEDYK-RAST-2022 | Is artificial intelligence improving the audit process? (Fedyk, Hodson, Khimich, Fedyk; Review of Accounting Studies 27:938-985) | Review of Accounting Studies (Springer) | academic | https://doi.org/10.1007/s11142-022-09697-x | 2022-07-07 | full |
| FRC-NEWS-2026 | Innovative new guidance supports audit firm adoption of emerging AI technologies (Generative and Agentic AI Guidance) | Financial Reporting Council | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | 2026-03-30 | full |
| GAO-YBFAQ-2025 | GAO-26-108710, Government Auditing Standards: Frequently Asked Questions on a system of quality management | US Government Accountability Office | regulator | https://files.gao.gov/reports/GAO-26-108710/index.html | 2025-12-15 | full |
| GAQC-DEV-2026 | Key developments affecting the governmental auditing environment | AICPA & CIMA Insights Blog (Governmental Audit Quality Center) | professional-body | https://www.aicpa-cima.com/professional-insights/article/key-developments-affecting-the-governmental-auditing-environment | 2026-10-08 | full |
| GT-GTAP-2026 | Grant Thornton launches gtap to transform audit delivery across U.S. practice | Grant Thornton US | firm | https://www.grantthornton.com/insights/press-releases/2026/may/grant-thornton-launches-gtap-audit-transformation-us | 2026-05-07 | full |
| ICAS-AMBS-2025 | ICAS study finds widespread concern over genAI accounting errors (reports ICAS, 'Generative AI and Professional Judgement in Accounting'; Alliance Manchester and Aston Business Schools study of Beever and Struthers; ICAS report itself not opened) | The Accountant | academic | https://www.theaccountant-online.com/news/icas-study-finds-widespread/ | 2026-03-17 | full |
| ICPAS-PRAF-2026 | Peer Review Alliance Forum (Virtual): 2026 Forum - Participant Slides (catalogue description of an AICPA Peer Review update; slides themselves not opened) | Illinois CPA Society | conference | https://learn.icpas.org/AssetListing/Peer-Review-Alliance-Forum-Virtual-17790/2026-Forum-%E2%80%93-Participant-Slides-29361 | 2026 | full |
| IDC-CASEWARE-2026 | Audit firms step up AI adoption while seeking safeguards (IDC global survey of 1,005 audit and accounting decision-makers, sponsored by Caseware) | IT Brief UK | survey | https://itbrief.co.uk/story/audit-firms-step-up-ai-adoption-while-seeking-safeguards | 2026-03-12 | full |
| IRS-OPR-2026 | OPR Alert 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| ISACA-PULSE-2026 | AI use accelerates while governance and ROI lag, says new ISACA research (3,400+ digital trust professionals, global; not accounting-specific) | ISACA | survey | https://isaca.org/about-us/newsroom/press-releases/2026/ai-use-accelerates-while-governance-and-roi-lag-says-new-isaca-research | 2026-05-05 | full |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors.html | 2026-10-13 | full |
| JOFA-CYBERCK-2026 | New checklist helps CPAs manage AI cyber risks | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/ | 2026-10-01 | full |
| JOFA-ETHAI-2026 | Accounting ethics in the age of AI (AICPA Professional Ethics Division staff) | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/ | 2026-08-05 | full |
| JOFA-GENAIDISC-2025 | Should I disclose my use of gen AI to clients? (Professional Liability Spotlight; author is a risk consulting director at CNA, underwriter of the AICPA Professional Liability Insurance Program) | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2025/apr/should-i-disclose-my-use-of-gen-ai-to-clients/ | 2025-04-01 | full |
| JOFA-PEEC-2026 | PEEC to continue discussions on alternative practice structures | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures/ | 2026-08-10 | full |
| JOFA-PEER-2026 | AICPA guides peer reviewers to address SOC 2 risks | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/ | 2026-05-14 | full |
| JOFA-QC1000-2026 | PCAOB finalizes simplified quality control amendments | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/sep/pcaob-finalizes-simplified-quality-control-amendments/ | 2026-09-09 | full |
| JOFA-SOCETH-2026 | SOC engagements: Ethics risks with tool providers | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/apr/soc-engagements-ethics-risks-with-tool-providers/ | 2026-04-06 | full |
| KARBON-AI-2026 | The State of AI in Accounting 2026 (survey Oct 2025, 593 respondents; PDF creation date Jan 2026, publication date not printed) | Karbon | survey | https://a.storyblok.com/f/321253/x/e2116b7c8a/the-state-of-ai-in-accounting-report-2026-by-karbon.pdf | 2026-01 | full |
| MNCPA-PEERREVIEW-2025 | 2025 Annual Report on Peer Review Activities (Minnesota and North Dakota; 269 firms) | Minnesota Society of CPAs | professional-body | https://www.mncpa.org/mncpa/media/Documents-Shared/peer-review/2025-MNCPA-annual-report-on-peer-review-activities.pdf | 2026-02 | full |
| MNCPA-SSARSCPE-2026 | Surgent's Guide and Update to Compilations, Reviews and Preparations (CPE listing seen in search results; names SSARS Nos. 26 and 27; no AI content) | Minnesota Society of CPAs | conference | https://www.mncpa.org/cpe/webinars/detail/26ws-0504/ | 2026 | search-only |
| OSCPA-PEERREVIEW-2025 | 2025 Annual Report on Peer Review Activities (Oklahoma, South Dakota and Kansas; 387 firms) | Oklahoma Society of CPAs | professional-body | https://prod.oscpa.com/storage/assets/Peer%20Review/Annual%20Report/2025%20OSCPA%20Peer%20Review%20Activities.pdf | 2026-03 | full |
| PKF-DAS-2026 | PKF O'Connor Davies Adopts AI-Enabled DAS Suite Powered by Caseware Verity, and Joins the Caseware Agentic Pioneer Program | Caseware | vendor | https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program | 2026-10-08 | full |
| RSM-ASKLUCA-2026 | RSM US Launches Ask Luca, Expanding AI Capabilities in the Audit | RSM US | firm | https://rsmus.com/newsroom/2026/rsm-launches-ask-luca.html | 2026-01-08 | full |
| STANFORD-CANARIES-2026 | Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence (Aug 2026 version; ADP payroll data through Jun 2026; economy-wide, not accounting-specific) | Stanford Digital Economy Lab | academic | https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine/ | 2026-08 | full |
| STANFORD-CHOIXIE-2025 | Human + AI in Accounting: Early Evidence from the Field (working paper; abstract page read) | Stanford Graduate School of Business | academic | https://www.gsb.stanford.edu/faculty-research/working-papers/human-ai-accounting-early-evidence-field | 2025-05-07 | full |
| TR-SOTP-2026 | 2026 State of Tax Professionals Report (600 respondents; small = 1-3, midsize = 4-29, large = 30+ professionals) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2026/06/2026-State-of-Tax-Professionals-Report.pdf | 2026-06 | full |
| TRI-FOP-2026 | What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07-21 | full |
| TSCPA-PEERREVIEW-2025 | Annual Report on Peer Review Activities 2025 (Tennessee; 424 firms enrolled) | Tennessee Society of CPAs | professional-body | https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf | 2026-03-31 | full |
| WITHUM-DAS-2026 | Withum Fully Adopts DAS Powered by the Caseware Verity AI Platform | Caseware | vendor | https://www.caseware.com/news/withum-fully-adopts-das-powered-by-the-caseware-verity-ai-platform-to-drive-its-future-ready-audit-practice | 2026-06-03 | full |

57 sources: academic 4, conference 3, firm 2, press 11, professional-body 17, regulator 4, standard-setter 2, survey 8, vendor 6. 54 opened and read (access: full); 3 search-only (the Accountancy Europe paper was seen through a Spanish summary; ABA Formal Opinion 512 was blocked; one CPE listing). 'Opened and read' for the AICPA practice aid means its news release and download page, not the members-only file.

## 6. Gaps

- **No AI finding from peer review.** None of the four 2025 state peer-review reports read mentions AI [TSCPA-PEERREVIEW-2025; CTCPA-PEERREVIEW-2025; MNCPA-PEERREVIEW-2025; OSCPA-PEERREVIEW-2025]. The AICPA Peer Review Board's annual questionnaire FAQ does not name AI, and the exact questions were not found. No AICPA or state-society report of early SQMS No. 1 peer review results was found.
- **No independent error, override or parallel-run data** for any AI tool in a private-company audit, review or compilation. Vendor beta figures are the only accuracy numbers, and the number of items behind the 94% figure is not stated [CASEWARE-VERITY-2026].
- **Practice aid not opened.** The 51-page AICPA practice aid is members-only; content comes from the AICPA release, CFO Dive, Accounting Today and the Journal of Accountancy. Its Q&A on engagement letters is known through CFO Dive only [CFODIVE-AIPA-2026].
- **SSARS.** No AICPA, Accounting and Review Services Committee or state-board guidance on AI in preparation, compilation or review engagements was found; the only SSARS items are CPE listings [MNCPA-SSARSCPE-2026].
- **Client AI terms.** No audit client contract clause, bank or lender requirement, or sample AICPA engagement-letter clause was found; guidance is from a UK body, a liability-programme article and the practice aid Q&A [ACCA-ENGLTR-2026; JOFA-GENAIDISC-2025; CFODIVE-AIPA-2026].
- **Vendor and platform terms.** Caseware's data-protection and security statements are press-release claims; no firm's vendor contract or due-diligence file is public.
- **Academic evidence.** No NBER or Stanford study of AI in private-company audit was found. The relevant independent work is adjacent: Fedyk et al. (public-company audits, pre-GenAI), the Beever and Struthers study (UK; ICAS report not opened) and Choi and Xie (bookkeeping; abstract only) [FEDYK-RAST-2022; ICAS-AMBS-2025; STANFORD-CHOIXIE-2025]. The Stanford labour paper is economy-wide.
- **Bar and professional-body sources.** ABA Formal Opinion 512 was blocked (403) and is cited only through the Journal of Accountancy. SRA, state bar and MCA material was not pursued because it governs law and medicine, not accounting.
- **Surveys.** Firm-size breakdowns of AI findings in the CPA.com and AICPA report were not given; the PCPS top-issues figures by group were not extracted; the CPAFMA original report was not opened; the IPA training split was seen only in a search summary [CPACOM-ATR-2025; AICPA-TOPISSUES-2026; CPAFMA-WINSOME-2026].
- **Podcast, community and job-posting sources** were not found for this angle; the source types read are standard-setter, regulator, professional body, firm, vendor, academic, survey, press and conference.
- **Regional and local firms.** No named deployment below the top 100 firms was found; examples come from national, top-25 and PE-backed or private-company-focused firms.
- **Differences from the landscape file.** (1) The DOL 30% deficiency figure is from the November 2023 audit quality study (2020 form year), not a 2025 report; the 39% figure is the 2015 study (2011 form year), so the deficiency rate fell, while dollars at risk rose by $274 billion compared with prior studies [EBSA-AUDITQ-2023]. The December 2025 article the landscape used repeats the 2023 figures. (2) The ICAS study report is dated 17 Mar 2026 and the CPA Practice Advisor article on section 7216 is dated 12 Oct 2026 and written by an AI implementation firm's co-founder. (3) Caseware's CwX blog says the beta partners piloted on live engagements 'during the 2025 busy season'; the page is dated 17 Jun 2026 and the year was not reconciled [CASEWARE-CWX-2026].

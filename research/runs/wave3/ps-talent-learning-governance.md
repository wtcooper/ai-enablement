# Talent and learning, governance and evidence: professional services

Prepared 2026-10-19. Archetype: professional-services. Module: talent-learning (recruiting, graduate intake, training and the apprenticeship model when AI does entry-level work, performance, career paths and the leverage pyramid). Angle: governance (what constrains and measures the work). Method: `curl`, `pdftotext` and the r.jina.ai text mirror for pages; 11 rationed web searches before the shared budget ran out. Sources marked `search-only` were not opened in full. Quotations are under 25 words. Public sources only.

## 1. Summary

**What the evidence says.** The strongest independent measurement is a three-month pre-registered trial of 133 patent lawyers at eleven US IP firms (NBER 35720, September 2026): AI access raised delivered work quality by 0.34 to 0.38 SD, but on a later no-AI redline the advantage sat with seniors (0.45 SD) and juniors showed no average gain. Nothing else found measures skill formation in professional services. Everything else is adjacent: cross-industry payroll data, hiring counts, surveys and job-ad analyses.

- **Entry-level hiring is falling in AI-exposed fields, but the cause is contested.** A Stanford/NBER update (data to June 2026) puts employment of 22-25 year-olds in AI-exposed occupations 19% below the less-exposed peer path, mainly through reduced hiring; the authors call it descriptive, not causal. NALP counted 6,588 new graduates hired by 500+ lawyer firms in 2025, down 7.5% from the 2024 peak, and two-thirds of 57 large firms surveyed by Citi expect fewer first-years in 2028 than 2025. But the UK High Fliers report and ICAEW both say economic conditions, offshoring and cost cuts confound the AI explanation, and Big Four firms still plan 1,000+ junior hires each in 2026 (ICAEW). Citi found demand for lawyer hours rose 4.2% in the first half of 2026, and the Bloomberg Law columnist concludes AI has not yet reduced the hours clients buy.
- **The training problem is named everywhere and solved nowhere with data.** Surveys from TR (1,816 professionals) and LexisNexis (873 UK legal professionals) show sizeable shares of respondents worried about judgment development (48% in the TR survey; 72% and 69% naming skills gaps in the Lexis survey), and only 2% in the Lexis survey said AI mainly strengthens learning. The only firm programme described in detail is Duane Morris's onboarding redesign (TRI, 12 October 2026), with no outcome figures.
- **Regulators fix who is accountable, not how to train.** California's State Bar (2026) expects supervisors to set AI policies, train staff and refresh training as autonomy grows; the SRA warning notice of 17 August 2026 (seen through a law-firm article) followed 42 reports of AI misuse in a year and a case in which a junior associate delegated the 'entire thinking process' to AI. Billing rules limit funding training from client fees: hourly time saved by AI cannot be billed (Texas 705, quoting D.C. 388).
- **AI in recruiting, promotion and training selection is the live regulatory frontier.** Illinois (from 1 January 2026) reaches AI used in hiring, promotion, selection for training or apprenticeship and discipline; Colorado SB26-189 (signed 2026-05-14) applies from 1 January 2027; EU Annex III employment obligations apply from 2 December 2027. No professional-services firm was found describing AI-based screening or performance scoring.
- **Performance and career-path evidence is thin.** No source measures how AI has changed associate evaluation, promotion or pay. The nearest are a LexisNexis finding that leaders weight revenue and client feedback above billable hours, and TRI's observation that only 39% of professionals have personal AI goals.

**Counts:** 19 use cases (A 1, B 6, C 10, D 2). 44 sources listed (41 opened in full, 3 search-only); by type: academic 5, conference 1, firm 4, press 11, professional-body 7, regulator 7, survey 6, vendor 3. No podcast, community or job-posting sources were found for this angle.

## 2. Use cases

Use-case ids follow `professional-services-talent-learning-NN`. Source dates use the best date found; where a page showed none, the year only is given and the note says so.

```yaml
- id: professional-services-talent-learning-01
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: AI literacy, policy and verification training required before tool access
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Lawyers and advisers adopt AI faster than firm policy and training reach them, so juniors form habits (and make errors) before any firm standard applies. Professional-conduct guidance now expects managers to train staff and to refresh that training as tools become more autonomous.
  solution: 'Make a training step and a written policy a condition of access to GenAI tools (policy, approved-tool list, human review of output, independent verification of citations), and repeat training as tools change. ILTA reports this is common in large firms and rare in small ones. The pattern is ''other'': it is a gating and learning step, not an agentic pattern.'
  outcomes:
  - lever: risk
    description: Share of firms whose official GenAI policy or guidance requires specific training before use rises with firm size.
    figure: 11% (under 50 lawyers), 30% (50-149), 47% (150-349), 63% (350-699), 72% (over 700)
    measures: Percentage of responding firms in each lawyer-count band that selected 'Specific training required before use' as describing their current official GenAI policies or guidance (ILTA Q3.18; 508 firms in the survey overall)
    provenance: independent
    source_ref: ILTA-TECHSURVEY-2026
  - lever: risk
    description: Share of firms requiring human review of GenAI-assisted work product, by firm size.
    figure: 31% (under 50), 59% (50-149), 69% (150-349), 83% (350-699), 79% (over 700)
    measures: Percentage of responding firms in each lawyer-count band that selected 'Work product must be reviewed by a human' (ILTA Q3.18)
    provenance: independent
    source_ref: ILTA-TECHSURVEY-2026
  prerequisites:
  - A written GenAI policy and an approved-tool list
  - A training owner (the ILTA summary says firms expect added headcount in training, innovation, KM and data science)
  - 'Licence provisioning that can be gated (ILTA: more than half of respondents issue Copilot licences only on request)'
  risks_and_guardrails:
  - Managerial and supervisory lawyers should set clear policies on GenAI, including agentic tools, and give staff periodic training; policies and training should be updated as systems become more autonomous (CALBAR-GENAI-2026, p.7).
  - The EU Commission page states that AI literacy obligations under the AI Act have applied since 2 February 2025; whether the AI Omnibus changed that duty was not checked (EC-AIACT-2026).
  - ABA Formal Opinion 512 is summarised in secondary sources as asking managers to set AI policies and train lawyers and staff; the primary text was not reached (ABA-OP512-2024).
  human_checkpoints:
  - Training completion before access is granted
  - Periodic refresh when tools or autonomy change (CALBAR-GENAI-2026, p.7)
  role_evolution: 'Training, innovation and AI-governance roles are expected to grow: ILTA reports firms anticipating added headcount in IT, innovation, security, training, KM and data science (ILTA-TECHSURVEY-2026, p.5).'
  evidence_grade: C
  sources:
  - ref: ILTA-TECHSURVEY-2026
    title: 'The ILTA Technology Survey 2026: Executive Summary'
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: p.5, table for Q3.18 and the paragraph before it
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.7, Duty to Supervise Lawyers and Nonlawyers
  - ref: EC-AIACT-2026
    title: 'AI Act: regulatory framework for AI (page last updated 2026-10-19)'
    publisher: European Commission, Shaping Europe's digital future
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: 'Timeline paragraph: ''AI literacy obligations entered into application from 2 February 2025'''
  - ref: ABA-OP512-2024
    title: 'ABA Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: search-only
    locator: Not opened (403); summary only seen in secondary sources
  - ref: TRI-GENAI-TALENT-2024
    title: 'GenAI in the legal industry: Where it''s already impacting legal talent management'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/genai-legal-talent
    date: '2024-11-04'
    access: full
    locator: Section 'Training is crucial to getting the most out of GenAI'
  last_reviewed: '2026-10-19'
  notes: 'Grade C: a survey of unnamed firms plus regulator and bar text, no named firm outcome. The ILTA figures describe policy content, not training completion or error rates. An older TRI figure (Nov 2024, outside the 18-month window) said 18% of law-firm and 25% of corporate legal respondents to a TRI GenAI in Professional Services report had received GenAI training; kept here only as a baseline. In-house: corporate legal departments appear in the TRI baseline only.'
- id: professional-services-talent-learning-02
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: 'First-year onboarding rebuilt around AI habits: extended orientation, practice-group AI champions and a separate mentoring track'
  work_types:
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: AI is absorbing the tasks that used to build junior lawyers' judgment, yet entrants still expect the firm to develop them, and many already use AI regardless of firm rules.
  solution: 'Duane Morris, according to its Chief Legal Talent and Growth Officer, runs a two-day in-person orientation that includes a live AI-and-library research session, then twice-monthly extended sessions from September to June with internal staff and outside speakers. Each practice group has designated AI champions (a partner, counsel or senior associate with early access to test tools on real work) who show new lawyers the tools that suit that practice. A separate traditional mentoring track remains, and the outgoing class is debriefed each summer to redesign the next programme. One fixed principle: a first draft is never an appropriate final submission.'
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: No participation, error-rate or retention figures are given in the article
    provenance: self-reported
    source_ref: TRI-ONBOARDING-2026
  prerequisites:
  - A senior talent leader with authority over onboarding (Duane Morris has a Chief Legal Talent and Growth Officer)
  - Practice-group champions with early tool access
  - Annual feedback loop from the outgoing class
  risks_and_guardrails:
  - The article says AI-use training must include verification steps and human review to be effective (TRI-ONBOARDING-2026).
  - California's guidance expects supervisors to provide training on the ethical and practical aspects and pitfalls of AI tools used with limited real-time human direction (CALBAR-GENAI-2026, p.7).
  human_checkpoints:
  - First drafts are never final submissions (firm principle as reported)
  - Mentoring track for questions such as whether using AI with a given partner will be read as inefficient
  role_evolution: Mid-level associates build their own agents and automate repeatable tasks whether or not the firm trains them; practice-group champions become a new informal role (TRI-ONBOARDING-2026). The article argues that 'power skills' (client confidence, business fluency) now differentiate good from outstanding lawyers.
  evidence_grade: B
  sources:
  - ref: TRI-ONBOARDING-2026
    title: Redesigning new attorney onboarding for the AI era
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding
    date: '2026-10-12'
    access: full
    locator: Sections 'Associates are already forming AI habits' and 'What a redesigned onboarding program looks like'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.7, Duty to Supervise
  last_reviewed: '2026-10-19'
  notes: Single named firm, described by its own talent leader in a TRI Institute article; no measurements. As reported, the firm leaves it to lawyers how to use AI in first drafts.
- id: professional-services-talent-learning-03
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: Verification exercises and 'thinking partner' framing to protect junior legal reasoning
  work_types:
  - expert-judgment
  - review-assurance
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Juniors use AI for research, first drafts and document review, the work that used to teach judgment. Surveyed UK lawyers see gaps in deep legal reasoning and in verification skills.
  solution: Position AI to juniors as a 'thinking partner' for challenge and iteration rather than a shortcut, and set verification exercises in which juniors check AI output against authoritative sources. At PKF Smith Cooper, a manager quoted by ICAEW questions a trainee's AI-assisted results even when they are right, to confirm the trainee understands the reasoning.
  outcomes:
  - lever: quality
    description: Survey respondents' views on what would help juniors build reasoning and judgment while using AI.
    figure: 65% chose 'thinking partner' framing; 52% chose verification exercises
    measures: Share of respondents (UK-based legal professionals surveyed January 2026; 873 in the survey overall) who selected each option; the release does not say whether every respondent saw this question
    provenance: vendor-published
    source_ref: LEXIS-MENTORSHIP-2026
  - lever: risk
    description: Perceived skills gaps among juniors.
    figure: 72% cite deep legal reasoning and argumentation; 69% flag verification and source-checking
    measures: Share of respondents citing each as a skills gap among junior lawyers (same survey; denominator as above)
    provenance: vendor-published
    source_ref: LEXIS-MENTORSHIP-2026
  prerequisites:
  - Access to authoritative sources for checking
  - Reviewers with time to question juniors on reasoning, not just results
  risks_and_guardrails:
  - Only 2% of respondents said AI mainly strengthens learning (LEXIS-MENTORSHIP-2026, report page).
  - A lawyer's duty of competence includes reviewing, verifying and correcting AI output consistent with the skill reasonably necessary for the representation (CALBAR-GENAI-2026, p.4).
  human_checkpoints:
  - Reviewer questions the junior on the reasoning behind AI-assisted conclusions (ICAEW-WORRY-2026)
  role_evolution: Reviewers carry more of the teaching load; the panel recap says the answer is not to preserve inefficient work but to identify what that work taught (source discipline, factual patience, pattern recognition) and teach it another way (LEXIS-SYMPOSIUM-2026).
  evidence_grade: C
  sources:
  - ref: LEXIS-MENTORSHIP-2026
    title: AI Is Speeding Up Junior Lawyers' Work but Raising Questions About How Judgment Is Learned (press release on The mentorship gap report)
    publisher: LexisNexis Legal & Professional
    type: survey
    url: https://www.lexisnexis.com/community/amp-pressroom/ai-is-speeding-up-junior-lawyers-work-but-raising-questions-about-how-judgment-is-learned
    date: '2026-02-02'
    access: full
    locator: Press release paragraphs 3-5; report page (873 respondents, 2% figure)
  - ref: LEXIS-SYMPOSIUM-2026
    title: 'Lawyering in the Age of AI: Preparing the Next Generation for Practice (LexisNexis AI Symposium panel recap)'
    publisher: LexisNexis Legal & Professional
    type: vendor
    url: https://www.lexisnexis.com/community/amp-insights/82/lawyering-in-the-age-of-ai-preparing-the-next-generation-for-practice
    date: '2026-06-02'
    access: full
    locator: Section 'AI can accelerate growth, but not without cost'
  - ref: ICAEW-WORRY-2026
    title: 'AI: are junior accountants worried about roles?'
    publisher: ICAEW Insights
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2026/jun-2026/ai-are-junior-accountants-worried-about-roles
    date: '2026-06-10'
    access: full
    locator: Section 'Building foundations', Laurenti quote
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.4, Duties of Competence and Diligence
  last_reviewed: '2026-10-19'
  notes: Vendor-commissioned survey (LexisNexis sells legal AI). The survey measures opinions about what would help, not whether the exercises work. No firm that runs verification exercises was named.
- id: professional-services-talent-learning-04
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: AI-supported simulations for early-career practice (advocacy, feedback conversations, client scenarios)
  work_types:
  - client-interaction
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: If AI takes routine tasks, juniors lose low-risk practice. Panelists and talent leaders look for places where juniors can practise, make mistakes safely and see what good supervision looks like.
  solution: Three Crowns has worked with Stanford on a cross-examination simulator that lets lawyers and students practise advocacy against an AI-supported witness (described by its CEO at a LexisNexis symposium). Duane Morris's talent chief reported early talks about adapting a physician bedside-manner simulator for attorneys; at a prior (unnamed) firm, an avatar tool for difficult feedback conversations saw little use when a human coach drove it, while a later ChatGPT-based version succeeded, with no figures given.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: No usage, learning or quality figures are reported for any simulator
    provenance: self-reported
    source_ref: LEXIS-SYMPOSIUM-2026
  prerequisites:
  - A simulator built or configured for the skill (cross-examination, feedback, client intake)
  - 'A place in the training calendar (law school, firm training, practice group or client-service team: the panel asks where these should sit)'
  risks_and_guardrails:
  - The Three Crowns CEO did not present simulation as a cure-all (LEXIS-SYMPOSIUM-2026).
  - Simulators do not replace supervised real work; no source tests that.
  human_checkpoints:
  - Debrief by a supervisor or coach (implied by the panel's emphasis on learning what good supervision looks like; not stated for any named tool)
  role_evolution: Training and talent teams own simulation design; panel and TRI sources argue juniors need earlier client-facing practice because routine work shrinks.
  evidence_grade: B
  sources:
  - ref: LEXIS-SYMPOSIUM-2026
    title: 'Lawyering in the Age of AI: Preparing the Next Generation for Practice (LexisNexis AI Symposium panel recap)'
    publisher: LexisNexis Legal & Professional
    type: vendor
    url: https://www.lexisnexis.com/community/amp-insights/82/lawyering-in-the-age-of-ai-preparing-the-next-generation-for-practice
    date: '2026-06-02'
    access: full
    locator: Sections 'Law school has to change the training ground' and the Hugh Carlson passage
  - ref: TRI-ONBOARDING-2026
    title: Redesigning new attorney onboarding for the AI era
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding
    date: '2026-10-12'
    access: full
    locator: Paragraphs on AI simulations and power skills
  last_reviewed: '2026-10-19'
  notes: 'Weak B: the Three Crowns example comes from a vendor-authored panel recap and the Duane Morris item is ''early talks''. Treat maturity as piloting only for the Three Crowns/Stanford simulator.'
- id: professional-services-talent-learning-05
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: Associate rotation into the firm's AI innovation group as a career route
  work_types:
  - software-systems
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: AI adoption needs lawyers who can configure, govern and explain tools, and juniors need career routes that do not depend on the work AI is absorbing.
  solution: At A&O Shearman, associates work inside the Markets Innovation Group (MIG), a 27-person multidisciplinary team of lawyers, developers and innovation specialists led by a partner who is also the firm's global lead for AI Advisory. One associate joined for her fourth seat and stayed; her work moved from explaining AI to clients to governance and guardrails and then to product work on ContractMatrix, a Word add-in built with Harvey and Microsoft that is used internally and licensed to clients. The role includes demos, client conversations and product tutorials.
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: The article gives team size (27) and tenure examples but no outcome measures
    provenance: self-reported
    source_ref: NONBILLABLE-AOS-2026
  prerequisites:
  - A funded innovation group with developers and partner sponsorship
  - Rotation (seat) mechanism for trainees
  - Governance and security frameworks built before wide rollout (the firm sandboxed Harvey from September 2022 first, per the article)
  risks_and_guardrails:
  - 'Small cohort: the article profiles three associates, not a scaled programme.'
  human_checkpoints:
  - Not described
  role_evolution: Associates become product, governance and client-education contributors; one interviewee says AI work is now recognised as helpful for a legal career, where at first it was a 'passion project' (NONBILLABLE-AOS-2026).
  evidence_grade: B
  sources:
  - ref: NONBILLABLE-AOS-2026
    title: Meet the junior lawyers putting AI to work inside A&O Shearman
    publisher: Non-Billable
    type: press
    url: https://www.nonbillable.co.uk/posts/junior-lawyers-ai-innovation-a-o-shearman-harvey
    date: '2026-03-10'
    access: full
    locator: Opening sections on MIG, then the Susannah McMillan interview
  last_reviewed: '2026-10-19'
  notes: Trade-press profile; the firm's own figures were not seen. Sibling evidence for the same idea at other firms was not found.
- id: professional-services-talent-learning-06
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: 'AI drafting assistant with periodic no-AI skill checks: measuring whether juniors keep building expertise'
  work_types:
  - document-production
  - expert-judgment
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: personal-assistant
  maturity: piloting
  problem: AI can raise the quality of delivered work while stunting the expertise professionals would otherwise develop by doing it. Firms have had no controlled measurement of which effect dominates for juniors.
  solution: In a pre-registered three-month randomised controlled trial, 133 practising patent lawyers at eleven US IP firms were given a custom AI patent drafting assistant. Blinded expert patent attorneys scored all work. After three months everyone redlined an existing patent application without AI, a core task requiring expert judgment. The design (assistant plus a later no-AI test) is itself a template for a firm-level control on skill formation.
  outcomes:
  - lever: quality
    description: Quality of delivered benchmark patent drafting tasks with AI access versus control, larger gains among juniors.
    figure: +0.34 SD at 10 days; +0.38 SD at 90 days
    measures: Difference in blinded expert scores between treated and control lawyers, in standard deviations, on benchmark patent drafting tasks (133 lawyers, 11 firms)
    provenance: independent
    source_ref: NBER-AUTOR-2026
  - lever: quality
    description: 'Judgment on a no-AI redline task after three months: treated outperformed controls overall, but the advantage sat with seniors.'
    figure: +0.32 SD overall; +0.45 SD for seniors; no average gain for juniors
    measures: Difference in blinded expert scores on a no-AI patent redline between treated and control lawyers, in standard deviations, overall and for senior lawyers; juniors showed no average gain
    provenance: independent
    source_ref: NBER-AUTOR-2026
  - lever: quality
    description: Junior scores on the no-AI task bifurcated.
    figure: none published as a single figure
    measures: The abstract says sharply fewer mediocre scores were offset by more poor and more good ones; the authors suggest AI served as a springboard for some juniors and a cushion for others
    provenance: independent
    source_ref: NBER-AUTOR-2026
  prerequisites:
  - A task with blind expert scoring
  - A baseline test of judgment without the tool
  - Willingness to withhold the tool from a control group (research design; not a firm practice)
  risks_and_guardrails:
  - The authors state that foundational expertise may be a prerequisite for extracting durable skill from AI-assisted practice (NBER-AUTOR-2026, abstract).
  - 'Custom assistant, one practice area (patent drafting), three months: results may not transfer to other tools or tasks.'
  human_checkpoints:
  - Blinded expert scoring of all work (study design)
  role_evolution: 'Pyramid implication stated cautiously: seniors kept a durable skill advantage from AI use; juniors did not on average, so firms cannot assume AI-assisted juniors develop at the same rate.'
  evidence_grade: A
  sources:
  - ref: NBER-AUTOR-2026
    title: Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER Working Paper 35720)
    publisher: National Bureau of Economic Research (Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere)
    type: academic
    url: https://www.nber.org/papers/w35720
    date: '2026-09-07'
    access: full
    locator: Abstract (full paper returned 403 and was not read)
  last_reviewed: '2026-10-19'
  notes: Grade A rests on a pre-registered study with measured outcomes by named authors at a named institution; the participating firms are unnamed and only the abstract was read, so p-values (garbled in the mirror) are not repeated. It is a research deployment, not a firm programme, so maturity is piloting. No second source replicates it.
- id: professional-services-talent-learning-07
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: 'Skill-aware task routing: use AI most where juniors gain, and train staff on where it fails'
  work_types:
  - expert-judgment
  - document-production
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Gains from AI differ by task and by the user's baseline skill; for tasks outside AI's competence it can make results worse. Firms need evidence on which tasks to hand to juniors with AI and which to protect.
  solution: 'Use controlled-experiment evidence to set task rules: a 758-person BCG experiment found AI users completed 12.2% more tasks, 25.1% faster, on tasks inside the frontier, but were 19% less likely to get a managerial task outside the frontier right; lower-baseline performers gained more. A randomised experiment with law students found GPT-4 gave large, consistent speed gains and only slight, inconsistent quality gains, with the weakest participants gaining most where quality improved. Combined with the NBER patent result (use case 06), these suggest training should teach the boundary of reliable use, not only prompting.'
  outcomes:
  - lever: speed
    description: Consultants using GPT-4 on tasks inside the frontier.
    figure: 12.2% more tasks completed; 25.1% faster
    measures: Average difference between AI-access and no-AI groups across 18 realistic tasks in a preregistered experiment with 758 knowledge workers at BCG
    provenance: independent
    source_ref: HBS-DELLACQUA-2023
  - lever: quality
    description: Consultants using AI on a task outside the frontier.
    figure: 19% less likely to produce correct solutions
    measures: Comparison with the no-AI group on one complex managerial task chosen to be outside AI's capabilities
    provenance: independent
    source_ref: HBS-DELLACQUA-2023
  - lever: quality
    description: Lower baseline proficiency gained more on a creative product-innovation task.
    figure: 43% performance boost for the lowest-baseline individuals
    measures: BCG's description of boosted performance for individuals with the lowest baseline proficiency on the creative product-innovation task in the same experiment
    provenance: vendor-published
    source_ref: BCG-JAGGED-2023
  - lever: speed
    description: Law students with GPT-4 on four legal tasks.
    figure: none published as a single figure
    measures: 'Abstract: large, consistent speed gains; slight, inconsistent quality gains; weakest participants gained most where AI helped (randomised trial of law-school students; sample size is not in the abstract)'
    provenance: independent
    source_ref: UMN-CHOI-2024
  prerequisites:
  - A task inventory marked inside or outside the frontier
  - Baseline skill assessment of juniors
  - Review capacity for tasks outside the frontier
  risks_and_guardrails:
  - The NBER trial found juniors had no average durable gain on a no-AI task (NBER-AUTOR-2026), so leveling on output is not the same as leveling on skill.
  - Studies used GPT-4 in 2023; current tools differ.
  human_checkpoints:
  - Human review of any task flagged as outside the frontier
  role_evolution: Supervisors and learning teams maintain the frontier map; juniors are taught when to rely on AI and when to challenge it.
  evidence_grade: B
  sources:
  - ref: HBS-DELLACQUA-2023
    title: Navigating the Jagged Technological Frontier (HBS Working Paper 24-013)
    publisher: Harvard Business School with Boston Consulting Group
    type: academic
    url: https://www.hbs.edu/faculty/Pages/item.aspx?num=64700
    date: 2023-09
    access: full
    locator: Abstract
  - ref: BCG-JAGGED-2023
    title: How People Create and Destroy Value with Gen AI
    publisher: Boston Consulting Group
    type: firm
    url: https://www.bcg.com/publications/2023/how-people-create-and-destroy-value-with-gen-ai
    date: '2023-09-21'
    access: full
    locator: Paragraph beginning 'The lower the individual's baseline proficiency'
  - ref: UMN-CHOI-2024
    title: Lawyering in the Age of Artificial Intelligence, 109 Minn. L. Rev. 147
    publisher: University of Minnesota Law Review (Choi, Monahan, Schwarcz)
    type: academic
    url: https://scholarship.law.umn.edu/minnlrev/vol109/iss1/3
    date: 2024-11
    access: full
    locator: Abstract
  - ref: NBER-AUTOR-2026
    title: Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER Working Paper 35720)
    publisher: National Bureau of Economic Research (Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere)
    type: academic
    url: https://www.nber.org/papers/w35720
    date: '2026-09-07'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-19'
  notes: 'Capped at B: these experiments measure task performance, not training programmes, and are 2023-2024 (outside the 18-month window; used as foundations). The HBS page was read through a text mirror because direct access returned 403.'
- id: professional-services-talent-learning-08
  archetype: professional-services
  module: talent-learning
  function: strategy-planning
  title: Resize first-year classes and shift the associate mix toward laterals and non-equity lawyers
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: The associate pyramid rested on junior work that both billed and trained. If AI removes some of that work, firms must decide how many first-years to hire, but 19% of surveyed firms do not know what they will need in 2028.
  solution: 'Large firms plan smaller first- and second-year classes and favour lateral hires. Evidence: NALP counted 6,588 graduates hired by firms of over 500 lawyers in 2025, down 7.5% from the 2024 peak; a Citi survey of 57 large firms found two-thirds expect fewer first-years in 2028 than 2025. Reporting from Vault cites BCG Attorney Search that 86% of large firms plan to grow associate ranks through 2027 while 35% plan larger first-year classes. TRI''s Q2 2026 index finds associates and non-equity partners absorbing most extra workload. No AI tool is involved in the decision; AI is a stated driver of the uncertainty.'
  outcomes:
  - lever: cost
    description: Hiring of new law graduates by the largest firms fell in 2025.
    figure: 6,588 hired; down 538 (7.5%) from the 2024 peak
    measures: Number of new law-school graduates hired in 2025 by firms with more than 500 lawyers, per NALP data cited by Bloomberg Law
    provenance: independent
    source_ref: BLOOMBERG-FIRSTYEAR-2026
  - lever: cost
    description: Large-firm expectations for 2028 versus 2025.
    figure: Two-thirds expect fewer first-years; nearly 60% expect fewer second-years; 19% do not know
    measures: Share of 57 large firms in a Citi law-firm banking group survey (summer 2026) with each expectation for 2028 compared with 2025
    provenance: independent
    source_ref: BLOOMBERG-FIRSTYEAR-2026
  - lever: capacity
    description: Demand for lawyer time rose rather than fell in the first half of 2026.
    figure: 4.2% demand growth versus a normal of about 1.5%
    measures: Growth in demand for lawyers' hours in the first half of 2026 as reported by Citi's law firm banking group (Bloomberg Law column)
    provenance: independent
    source_ref: BLOOMBERG-AICOST-2026
  prerequisites:
  - Scenario planning for intake under uncertainty
  - A view on lateral integration and associate career paths
  risks_and_guardrails:
  - 'Attribution is contested: the same column notes historical patterns where first-year hiring bottoms out three years after a peak, and that 2025 was not a recession year. The High Fliers UK report ties graduate cuts to economic uncertainty, not AI (HIGHFLIERS-GM-2026). The Stanford/NBER ''canaries'' paper calls its own results descriptive, not causal (STANFORD-CANARIES-2026).'
  - 'A pipeline gap risk: the ICAEW piece reports a view that firms that closed intake after 2008 struggled for management talent about five years later (ICAEW-JUNIOR-2026).'
  human_checkpoints:
  - Partner and talent-committee decision on class size
  role_evolution: Fewer entry-level hires and more lateral and non-equity roles; the Vault piece cites BCG data that equity partner headcount fell 0.5% while total lawyer headcount grew in the first nine months of 2025, with leverage up 4.3% (secondary report, BCG primary not opened).
  evidence_grade: C
  sources:
  - ref: BLOOMBERG-FIRSTYEAR-2026
    title: Big Law First-Year Hiring Set to Plunge as History, AI Collide (Big Law Business column, Roy Strom)
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/big-law-first-year-hiring-set-to-plunge-as-history-ai-collide
    date: '2026-09-10'
    access: full
    locator: Body of the column (NALP and Citi data)
  - ref: BLOOMBERG-AICOST-2026
    title: Big Law AI Cost Savings Remain a Mystery as Billable Hours Jump (Big Law Business column, Roy Strom)
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/big-law-ai-cost-savings-remain-a-mystery-as-billable-hours-jump
    date: '2026-09-03'
    access: full
    locator: Paragraphs on Citi's 4.2% demand growth and the billable hour
  - ref: VAULT-PYRAMID-2026
    title: 'The Compressed Pyramid: What AI Means for the Associate Career Ladder (Travis Whitsitt)'
    publisher: Vault
    type: press
    url: https://legacy.vault.com/blogs/vaults-law-blog-legal-careers-and-industry-news/the-compressed-pyramid-what-ai-means-for-the-associate-career-ladder
    date: '2026-08-11'
    access: full
    locator: Sections 'The Numbers Behind the Shift' and 'How Firms Are Responding'
  - ref: TRI-LFFI-Q2-2026
    title: 'Q2 2026 LFFI: A heavier load, yet a faster crossing'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed
    date: '2026-08-10'
    access: full
    locator: Section 'Who's actually doing the rowing'
  - ref: STANFORD-CANARIES-2026
    title: Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence (updated version, data through June 2026)
    publisher: Stanford Digital Economy Lab / NBER (Brynjolfsson, Chandar, Chen)
    type: academic
    url: https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf
    date: 2026-08
    access: full
    locator: Abstract and facts (2)-(4)
  - ref: HIGHFLIERS-GM-2026
    title: The Graduate Market in 2026 (report page)
    publisher: High Fliers Research
    type: survey
    url: https://highfliers.co.uk/publication-the-graduate-market-report
    date: '2026-03-19'
    access: full
    locator: Section 'An Unprecedented Drop in Graduate Jobs'
  last_reviewed: '2026-10-19'
  notes: C because no named firm reports a decision or an outcome; the measurements are market-level. The Stanford/NBER paper (cross-industry, ADP payroll data) finds employment of 22-25 year-olds in AI-exposed occupations 19% below the less-exposed peer path, mainly through reduced hiring; it covers all occupations, not professional services specifically, so it is context only. Its lawyers and accountants appear in occupation lists only; no professional-services-specific figure was extracted.
- id: professional-services-talent-learning-09
  archetype: professional-services
  module: talent-learning
  function: strategy-planning
  title: Resize graduate intake at accounting and advisory firms while offshoring and automating entry-level tasks
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: in-production
  problem: Entry-level accounting and audit work is the most automatable part of the pipeline, yet firms need future managers. Press attributes intake cuts to AI, cost pressure and offshoring together.
  solution: UK Big Four graduate intakes fell between 2023 and the year before mid-2025 (press-reported figures below); ICAEW reports all four still plan to hire at least 1,000 juniors this year, with EY expecting 1,600, and that 68% of mid-tier firms in its research expect AI to reduce the need for some early-career roles. Junior roles are being reshaped toward reviewing and validating AI output.
  outcomes:
  - lever: cost
    description: UK Big Four graduate intake reductions reported from The Telegraph.
    figure: KPMG 1,399 to 942 (-29%); Deloitte 1,700 to 1,400 (-18%); EY 1,800 to 1,600 (-11%); PwC 1,600 to 1,500 (-6%)
    measures: Graduate recruitment numbers per firm for 2023 versus 'last year' as reported by Scottish Financial News on 2025-06-23, citing The Telegraph; not published by the firms
    provenance: independent
    source_ref: SFN-BIGFOUR-2025
  - lever: cost
    description: UK accountancy graduate job adverts.
    figure: -44% versus 2023 (all graduate jobs -33%)
    measures: 'Indeed data cited in the same article: UK accountancy graduate job adverts ''this year'' (2025) versus 2023'
    provenance: independent
    source_ref: SFN-BIGFOUR-2025
  - lever: cost
    description: Mid-tier firms' expectation that AI reduces early-career roles.
    figure: 68%
    measures: Share of those surveyed in ICAEW's Evolution of Mid-Tier Accountancy Firms research who expect AI to reduce the need for some early-career roles (sample size not given in the article)
    provenance: independent
    source_ref: ICAEW-WORRY-2026
  prerequisites:
  - Offshore delivery hubs (the article names Malaysia, the Philippines and India for the Big Four)
  - A plan for who reviews AI output once seniors lose junior capacity
  risks_and_guardrails:
  - ICAEW says it is unclear how much AI contributed once offshoring and general cost reductions are factored in (ICAEW-WORRY-2026).
  - High Fliers attributes 2023-2025 UK graduate cuts to economic uncertainty after the 2024 election (HIGHFLIERS-GM-2026).
  - Junior staff given AI oversight too early risk approving incorrect outputs (ICAEW-WORRY-2026, MacDonald quote).
  human_checkpoints:
  - Every AI output reviewed by a qualified accountant (Laurenti quote, ICAEW-WORRY-2026)
  role_evolution: Early-career professionals spend less time on data entry and more on reviewing outputs, validating information and spotting anomalies (Robert Half talent director quoted in ICAEW-JUNIOR-2026); managers must find effective work for juniors, which AI makes harder (Larsen quote, same article).
  evidence_grade: B
  sources:
  - ref: SFN-BIGFOUR-2025
    title: Big Four slash graduate jobs as AI takes over entry-level tasks (reporting The Telegraph)
    publisher: Scottish Financial News
    type: press
    url: https://www.scottishfinancialnews.com/articles/big-four-slash-graduate-jobs-as-ai-takes-over-entry-level-tasks
    date: '2025-06-23'
    access: full
    locator: Paragraphs 2-4
  - ref: ICAEW-JUNIOR-2026
    title: Why we still need junior accountants in the age of AI, and how their roles might change
    publisher: ICAEW Insights
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2026/apr-2026/why-we-still-need-junior-accountants-and-how-their-role-might-change
    date: '2026-04-02'
    access: full
    locator: Opening paragraphs and sections 'Managers need a mindset change' and 'Junior accountants will do data review and validation'
  - ref: ICAEW-WORRY-2026
    title: 'AI: are junior accountants worried about roles?'
    publisher: ICAEW Insights
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2026/jun-2026/ai-are-junior-accountants-worried-about-roles
    date: '2026-06-10'
    access: full
    locator: Key takeaways and intro; 'The risk of too much early responsibility'
  - ref: HIGHFLIERS-GM-2026
    title: The Graduate Market in 2026 (report page)
    publisher: High Fliers Research
    type: survey
    url: https://highfliers.co.uk/publication-the-graduate-market-report
    date: '2026-03-19'
    access: full
    locator: Section 'An Unprecedented Drop in Graduate Jobs'
  last_reviewed: '2026-10-19'
  notes: 'Search-only, not used in outcomes: a Fortune/Business Insider item seen in search results reports PwC UK intake of 1,300 versus 1,500 and says its UK chief called the UK slowdown the single biggest factor (FORTUNE-PWC-2025, 2025-09-08). Another set of results says PwC plans to cut US entry-level hiring by almost a third over three years; neither was opened. The People Matters summary of the same story (2025-07-21) misattributes the Indeed 44% to Big Four postings, so it was not used. Sources are UK-centred.'
- id: professional-services-talent-learning-10
  archetype: professional-services
  module: talent-learning
  function: strategy-planning
  title: Keep expanding analyst intake on the premise that juniors are more AI-fluent than mid-career hires
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: announced
  problem: Consulting's project model relies on junior analytical capacity and an apprenticeship route into the firm; cutting it risks the pipeline.
  solution: McKinsey's North America chair told reporters in September 2025 that the firm planned to grow North American headcount by 12% in 2026 over 2025, that its 5,000-7,000 non-partner staff in the region could rise 15-20% over five years, and that younger recruits tend to be more fluent in AI tools than experienced staff.
  outcomes:
  - lever: capacity
    description: Planned headcount growth, stated by the firm.
    figure: 12% planned growth in North American workforce in 2026 versus 2025
    measures: Planned change in North American workforce as reported by Reuters (via People Matters); a plan, not a measured result
    provenance: self-reported
    source_ref: PEOPLEMATTERS-MCK-2025
  prerequisites:
  - Demand for project capacity
  - A view that AI use is a differentiator for new recruits
  risks_and_guardrails:
  - It is a stated plan from September 2025; no later outcome was found. Another summary of the same period says McKinsey and BCG froze starting salaries for 2026, a third year (search-result summary of an ESCP article; not opened).
  human_checkpoints:
  - Not described
  role_evolution: The chair's argument is that AI-fluent juniors handle work that cannot be done with machines at the same pace (PEOPLEMATTERS-MCK-2025).
  evidence_grade: C
  sources:
  - ref: PEOPLEMATTERS-MCK-2025
    title: McKinsey rejects AI job fears, to boost hiring by 12% in 2026 (reporting Reuters and the Wall Street Journal)
    publisher: People Matters
    type: press
    url: https://www.peoplematters.in/news/strategic-hr/mckinsey-rejects-ai-job-fears-to-boost-hiring-by-12percent-in-2026-43536
    date: '2025-09-12'
    access: full
    locator: Whole article (Reuters and WSJ reporting)
  last_reviewed: '2026-10-19'
  notes: 'Grade C: statements of intent to reporters, secondary report. Counter-example to use case 09. People Matters is a trade summary of Reuters and WSJ reports, not the originals.'
- id: professional-services-talent-learning-11
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: Redefine entry-level roles around judgment, review and 'seniorised' skills
  work_types:
  - expert-judgment
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Routine tasks that taught juniors are being automated, while 71% of professionals in the TR survey believe early-career roles need structured support from experienced peers to develop the skills AI risks displacing.
  solution: Shift entry-level job content toward reviewing outputs, validating quality, interpreting results and client contact, with deliberate mentoring and training. PwC's job-ad analysis finds AI-exposed junior roles asking for more senior skills; the ICAEW pieces describe the same direction for accountants.
  outcomes:
  - lever: quality
    description: AI-exposed junior roles ask for senior skills.
    figure: 7 times more likely to demand traditionally senior skills such as leadership and strategic thinking
    measures: 'Job-ad analysis (over one billion ads, Lightcast data): most AI-exposed junior roles compared with least AI-exposed junior roles; cross-sector, not professional services alone'
    provenance: vendor-published
    source_ref: PWC-AIJB-2026
  - lever: capacity
    description: '''Seniorised'' entry-level roles are growing while other entry-level roles decline.'
    figure: 35% growth since 2019 in AI-exposed 'seniorised' entry-level roles
    measures: Growth in 'seniorised' entry-level postings since 2019 in highly AI-exposed sectors, per PwC analysis of job-ad data; the professional-services report repeats the figure
    provenance: vendor-published
    source_ref: PWC-AIJB-PS-2026
  - lever: risk
    description: Professionals' views on the pipeline.
    figure: 71% say early-career roles need structured support; 48% fear a negative impact on independent judgment development
    measures: Share of 1,816 surveyed professionals (law, tax, audit, accounting, compliance, risk and trade; private practice and in-house; 62 countries; March-April 2026)
    provenance: vendor-published
    source_ref: TR-FOP-2026
  - lever: quality
    description: Time to trusted judgment diverges by profession.
    figure: Legal expects it to lengthen by nearly two years (1.7); tax expects it to shorten by one (1.0)
    measures: Professionals' expected change in the timeline to trusted judgment, as the report states it (units given as years in the text)
    provenance: vendor-published
    source_ref: TR-FOP-2026
  prerequisites:
  - Mentors with capacity
  - Redesigned onboarding, mentoring and training (PwC's own recommendation)
  - Clear definition of what each junior role is expected to review
  risks_and_guardrails:
  - Juniors tasked with AI oversight too early may pass incorrect outputs (ICAEW-WORRY-2026).
  - Risk of creating lawyers who can supervise AI outputs without being able to judge whether they are correct (Vault summary of an Axios piece, VAULT-PYRAMID-2026).
  - PwC's figures describe job-ad content across sectors; they do not show that juniors are developing faster.
  human_checkpoints:
  - Structured support from experienced peers for early-career staff (TR-FOP-2026)
  role_evolution: Entry-level staff move from producing first passes to checking, interpreting and advising; PwC recommends reinventing early-career pathways by redesigning onboarding, mentorship and training (PWC-AIJB-2026). Mid-career staff become more critical as mentors (TR-FOP-2026 notes mid-career risk of leaving).
  evidence_grade: B
  sources:
  - ref: PWC-AIJB-2026
    title: '2026 AI Jobs Barometer: Two futures for jobs in an AI era'
    publisher: PwC
    type: firm
    url: https://www.pwc.com/gx/en/services/ai/ai-jobs-barometer.html
    date: '2026-06-15'
    access: full
    locator: Section 'AI transforms entry level work' and 'Next steps for business leaders'
  - ref: PWC-AIJB-PS-2026
    title: '2026 Global AI Jobs Barometer: Professional Services sector report'
    publisher: PwC
    type: firm
    url: https://www.pwc.com/gx/en/issues/artificial-intelligence/job-barometer/2026/pwc-aijb-2026-professional-services-report.pdf
    date: '2026-06-17'
    access: full
    locator: Key findings page
  - ref: TR-FOP-2026
    title: 'Future of Professionals Report 2026: When the AI strategy doesn''t reach the desk'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: Key findings 07; 'A generation of disrupted development'
  - ref: ICAEW-JUNIOR-2026
    title: Why we still need junior accountants in the age of AI, and how their roles might change
    publisher: ICAEW Insights
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2026/apr-2026/why-we-still-need-junior-accountants-and-how-their-role-might-change
    date: '2026-04-02'
    access: full
    locator: Sections 'Junior accountants will do data review and validation' and 'Professional judgement is becoming more of a focus'
  - ref: ICAEW-WORRY-2026
    title: 'AI: are junior accountants worried about roles?'
    publisher: ICAEW Insights
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2026/jun-2026/ai-are-junior-accountants-worried-about-roles
    date: '2026-06-10'
    access: full
    locator: '''The risk of too much early responsibility'''
  - ref: VAULT-PYRAMID-2026
    title: 'The Compressed Pyramid: What AI Means for the Associate Career Ladder (Travis Whitsitt)'
    publisher: Vault
    type: press
    url: https://legacy.vault.com/blogs/vaults-law-blog-legal-careers-and-industry-news/the-compressed-pyramid-what-ai-means-for-the-associate-career-ladder
    date: '2026-08-11'
    access: full
    locator: Section 'Why This Is a Training Problem'
  last_reviewed: '2026-10-19'
  notes: 'Capped at B: measurements are cross-sector job-ad content (PwC, itself a professional-services firm with a stake in the narrative) and a vendor survey (Thomson Reuters sells professional AI). No firm reports developmental outcomes for redesigned roles. The TR survey includes in-house corporate and government departments, so some respondents are in-house.'
- id: professional-services-talent-learning-12
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: Recruit and assess for learning agility and AI fluency alongside technical knowledge
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: When AI lowers the bar for surface competence, technical knowledge alone is a weaker hiring signal.
  solution: A Robert Half talent director, quoted by ICAEW, says hiring managers increasingly assess a candidate's appetite to learn, adaptability and comfort with technology, and that training is becoming more personalised and combines structured AI-tool training with guidance on responsible use. Duane Morris's talent chief argues that 'power skills' such as client confidence and business fluency now distinguish outstanding lawyers.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: No hiring-quality or retention figures are reported
    provenance: self-reported
    source_ref: ICAEW-JUNIOR-2026
  prerequisites:
  - Assessment methods for learning agility
  - Compliance with employment-AI rules if AI is used to score candidates (see use case 18)
  risks_and_guardrails:
  - If AI tools score or rank candidates, notice, bias-audit and human-review duties may apply (use case 18).
  human_checkpoints:
  - Hiring manager assessment
  role_evolution: Selection criteria shift toward adaptability and power skills; the PwC barometer finds skills required for AI-exposed jobs changing more than twice as fast as for less exposed jobs (PWC-AIJB-2026).
  evidence_grade: C
  sources:
  - ref: ICAEW-JUNIOR-2026
    title: Why we still need junior accountants in the age of AI, and how their roles might change
    publisher: ICAEW Insights
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2026/apr-2026/why-we-still-need-junior-accountants-and-how-their-role-might-change
    date: '2026-04-02'
    access: full
    locator: Section 'Appetite to learn is becoming more important'
  - ref: TRI-ONBOARDING-2026
    title: Redesigning new attorney onboarding for the AI era
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding
    date: '2026-10-12'
    access: full
    locator: Section 'Raising the bar for power skills'
  - ref: PWC-AIJB-2026
    title: '2026 AI Jobs Barometer: Two futures for jobs in an AI era'
    publisher: PwC
    type: firm
    url: https://www.pwc.com/gx/en/services/ai/ai-jobs-barometer.html
    date: '2026-06-15'
    access: full
    locator: Section 'AI accelerates skills transformation'
  last_reviewed: '2026-10-19'
  notes: Practitioner and recruiter statements; no named firm describes a changed selection process in detail.
- id: professional-services-talent-learning-13
  archetype: professional-services
  module: talent-learning
  function: risk-compliance-legal
  title: Junior AI-use disclosure and second-level review protocol
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Juniors can submit polished AI-assisted work without checking sources or telling the supervisor. A junior associate in Cork & Anor v Smith [2026] EWHC 1199 (Ch) was found to have delegated the 'entire thinking process' to AI, and fictitious authorities reached the court.
  solution: Require juniors to tell supervisors when AI was used, verify every authority and quote, escalate errors at once, and give supervisors the basis for effective second-level review. Regulators and bars place responsibility on supervisors and firms as well as the junior.
  outcomes:
  - lever: risk
    description: Reports of AI misuse received by the solicitors' regulator.
    figure: 42 reports in the past year
    measures: Reports of AI misuse to the SRA in the past year, as stated in a law-firm article on the SRA warning notice of 17 August 2026 (SRA text not reached)
    provenance: independent
    source_ref: DWF-SRA-2026
  - lever: risk
    description: Recorded UK AI hallucination cases.
    figure: 67 as of 10 July (2026)
    measures: Recorded cases of AI hallucinations in the UK as of 10 July, per the same article; period covered not stated
    provenance: independent
    source_ref: DWF-SRA-2026
  - lever: risk
    description: Firm policies by size on human review and verification.
    figure: 'Human review required: 31% (under 50 lawyers) to 83% (350-699); outputs must be cited or independently verified: 25% to 60%; supervisor or partner approval required: 4% to 19%'
    measures: Percentage of responding firms in each lawyer-count band selecting each item in ILTA Q3.18 (508 firms in the survey)
    provenance: independent
    source_ref: ILTA-TECHSURVEY-2026
  prerequisites:
  - A firm AI policy that juniors have read
  - Supervisors trained to review AI-assisted work
  risks_and_guardrails:
  - 'Supervisory duty: managerial and supervisory lawyers must make reasonable efforts to ensure subordinates comply; a subordinate must exercise independent professional judgment on AI use (CALBAR-GENAI-2026, p.7).'
  - Under D.C. Rules 5.1 and 5.3, a lawyer should take reasonable measures so that any supervised lawyer's or nonlawyer's GenAI use conforms to the rules (DCBAR-OP388-2024, section C).
  - The Texas committee says lawyers are responsible for work product regardless of who or what does the original research and drafting (TXBAR-OP705-2025, Oversight/Supervision).
  - Responsibility for erroneous work falls on trainees, solicitors, supervising partners and the firm (DWF-SRA-2026).
  human_checkpoints:
  - Junior discloses AI use to the supervisor
  - Supervisor second-level review with sources checked
  - Lawyer approves any filing (CALBAR-GENAI-2026, p.9)
  role_evolution: Supervisors take on explicit review-of-AI duties; juniors are expected to be transparent and to escalate errors immediately (DWF-SRA-2026).
  evidence_grade: C
  sources:
  - ref: DWF-SRA-2026
    title: 'Prompt, review, repeat: A guide to AI for trainees and junior solicitors'
    publisher: DWF Group
    type: firm
    url: https://dwfgroup.com/en/news-and-insights/insights/2026/8/prompt-review-repeat-a-guide-to-ai-for-trainees-and-junior-solicitors
    date: '2026-08-21'
    access: full
    locator: Sections 'The SRA's warning notice', 'Hallucinations' and 'Key steps for trainees and junior lawyers'
  - ref: SRA-WARNING-2026
    title: SRA warning notice on the use of AI (issued 17 August 2026)
    publisher: Solicitors Regulation Authority
    type: regulator
    url: https://www.sra.org.uk
    date: '2026-08-17'
    access: search-only
    locator: Primary text not reached (Cloudflare challenge); content seen only through the DWF article
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.7 Duty to Supervise; p.9 Candor to the Tribunal
  - ref: DCBAR-OP388-2024
    title: 'Ethics Opinion 388: Attorneys'' Use of Generative Artificial Intelligence in Client Matters'
    publisher: District of Columbia Bar
    type: professional-body
    url: https://www.dcbar.org/for-lawyers/legal-ethics/ethics-opinions-210-present/ethics-opinion-388
    date: 2024-04
    access: full
    locator: Section C, Responsibilities Regarding Lawyers in a Firm and Their Nonlawyer Assistants
  - ref: TXBAR-OP705-2025
    title: 'Opinion 705: lawyer''s use of generative artificial intelligence'
    publisher: Professional Ethics Committee for the State Bar of Texas (hosted by the Texas Center for Legal Ethics)
    type: professional-body
    url: https://www.legalethicstexas.com/resources/opinions/opinion-705/
    date: 2025-02
    access: full
    locator: Section 'Oversight/Supervision'
  - ref: ILTA-TECHSURVEY-2026
    title: 'The ILTA Technology Survey 2026: Executive Summary'
    publisher: International Legal Technology Association
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: p.5, Q3.18 table
  last_reviewed: '2026-10-19'
  notes: The SRA figures are second-hand through a law-firm article; the SRA warning notice itself was not read (marked search-only). The DWF article also states Law Society statistics that UK lawyers' use of generative AI rose from 46% to 61% in eight months; not verified at source.
- id: professional-services-talent-learning-14
  archetype: professional-services
  module: talent-learning
  function: strategy-planning
  title: Decouple junior training and performance measures from billable hours
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: 'Junior work has ''always served two purposes: billing and training'' (Guggenberger, quoted in Vault). If AI removes billable junior tasks, firms lose both the fee and the training vehicle, while ethics rules limit what can be billed.'
  solution: 'Idea discussed by academics and commentators: fund development time outside client billing and weigh associates on client feedback and revenue contribution, not only hours. Evidence is indirect: the LexisNexis survey shows firm leaders rank revenue growth (55%) and client feedback (49%) above billable hours (38%), while associates rank billable hours and client feedback equally (54% each).'
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: No firm reports a change to training funding or performance metrics
    provenance: self-reported
    source_ref: VAULT-PYRAMID-2026
  prerequisites:
  - Firm economics that can absorb non-billable development time
  - Alternative metrics accepted by associates
  risks_and_guardrails:
  - Hourly billing must reflect time actually spent; flat fees may build AI savings in (CALBAR-GENAI-2026, p.8).
  - A lawyer billing hourly may not charge for time 'saved' by AI, per Texas Opinion 705 quoting D.C. Opinion 388 (TXBAR-OP705-2025, Fees).
  - ABA Opinion 512 is summarised elsewhere as saying not to bill a client for the time spent learning AI in general; primary text not opened (ABA-OP512-2024).
  human_checkpoints:
  - Partner and talent-committee approval of the new metrics
  role_evolution: Associate evaluation and career paths would shift from hours toward client feedback, revenue contribution and supervision of AI work (idea).
  evidence_grade: D
  sources:
  - ref: VAULT-PYRAMID-2026
    title: 'The Compressed Pyramid: What AI Means for the Associate Career Ladder (Travis Whitsitt)'
    publisher: Vault
    type: press
    url: https://legacy.vault.com/blogs/vaults-law-blog-legal-careers-and-industry-news/the-compressed-pyramid-what-ai-means-for-the-associate-career-ladder
    date: '2026-08-11'
    access: full
    locator: Section 'Why This Is a Training Problem'
  - ref: LEXIS-MENTORSHIP-2026
    title: AI Is Speeding Up Junior Lawyers' Work but Raising Questions About How Judgment Is Learned (press release on The mentorship gap report)
    publisher: LexisNexis Legal & Professional
    type: survey
    url: https://www.lexisnexis.com/community/amp-pressroom/ai-is-speeding-up-junior-lawyers-work-but-raising-questions-about-how-judgment-is-learned
    date: '2026-02-02'
    access: full
    locator: Paragraph on how success is measured
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.8, Charging for Work Produced by Generative AI
  - ref: TXBAR-OP705-2025
    title: 'Opinion 705: lawyer''s use of generative artificial intelligence'
    publisher: Professional Ethics Committee for the State Bar of Texas (hosted by the Texas Center for Legal Ethics)
    type: professional-body
    url: https://www.legalethicstexas.com/resources/opinions/opinion-705/
    date: 2025-02
    access: full
    locator: Section 'Fees'
  - ref: ABA-OP512-2024
    title: 'ABA Formal Opinion 512: Generative Artificial Intelligence Tools'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: search-only
    locator: Not opened (403); secondary summaries only
  - ref: BLOOMBERG-AICOST-2026
    title: Big Law AI Cost Savings Remain a Mystery as Billable Hours Jump (Big Law Business column, Roy Strom)
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/big-law-ai-cost-savings-remain-a-mystery-as-billable-hours-jump
    date: '2026-09-03'
    access: full
    locator: Paragraph on Citi survey of 57 firms and the billable hour
  last_reviewed: '2026-10-19'
  notes: 'Label: idea. Practitioners and academics discuss it (Vault quotes law professors; Citi finds three-fourths of surveyed firms expect the billable hour to be affected by AI in 2028, and about half say it already has); no deployment found. The LexisNexis percentages are survey results (vendor-published), kept here as context, not as outcomes.'
- id: professional-services-talent-learning-15
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: Professional-grade AI tooling and AI-linked recognition as a retention and recruiting lever
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Professionals who see a gap between AI's value to the organisation and to themselves are more likely to consider leaving, and mid-career professionals are the most mobile.
  solution: Provide approved professional-grade AI tools, communicate the AI strategy, and tie AI value to individual recognition and progression. TR also reports that professionals with access to the kind of AI it sells are more likely to turn down a role without it.
  outcomes:
  - lever: risk
    description: Professionals experiencing an AI value gap who are considering leaving.
    figure: 24% considering leaving within two years; $232,000 estimated replacement cost per professional
    measures: Share of professionals experiencing an AI value gap (more than nine in ten) who are considering leaving their organisation within two years (TR survey, 1,816 professionals); replacement cost is TR's estimate
    provenance: vendor-published
    source_ref: TR-FOP-2026
  - lever: experience
    description: Access to professional-grade AI as a talent signal.
    figure: 32% of users of fiduciary-grade AI would turn down a role without it, versus 12% of those without access
    measures: Share of professionals in each group (users with and without access) in the TR survey who say they would turn down a role that did not offer such AI
    provenance: vendor-published
    source_ref: TR-FOP-2026
  - lever: risk
    description: Unsanctioned AI use.
    figure: 34%
    measures: Share of surveyed professionals who say they use AI tools their organisation has not sanctioned
    provenance: vendor-published
    source_ref: TR-FOP-2026
  prerequisites:
  - Sanctioned tools that meet confidentiality and verification needs
  - A communicated AI strategy
  risks_and_guardrails:
  - Where a named AI strategy exists, 35% still say day-to-day practice does not match it (TR-FOP-2026).
  - Shadow AI raises data-exposure and governance risk (TR-FOP-2026).
  human_checkpoints:
  - Not described
  role_evolution: TR expects expectations around recognition, progression and pay to shift with AI (TR-FOP-2026, section 'The professionals most likely to leave').
  evidence_grade: C
  sources:
  - ref: TR-FOP-2026
    title: 'Future of Professionals Report 2026: When the AI strategy doesn''t reach the desk'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: Key findings 03, 05, 06 and 08; 'The professionals most likely to leave'
  last_reviewed: '2026-10-19'
  notes: 'Vendor-published: Thomson Reuters sells the tools it says professionals want (''fiduciary-grade AI''). The full report is gated; the web summary was read. The sample includes in-house corporate and government departments (in-house).'
- id: professional-services-talent-learning-16
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: Personal AI goals in performance objectives
  work_types:
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Organisations announce AI strategies that individuals do not see in their own objectives, so use stays sporadic.
  solution: Set and link personal AI adoption goals for each professional and communicate the organisation's AI strategy so that individual accountability supports firm goals. TRI cites its 2025 Future of Professionals report on the effect.
  outcomes:
  - lever: quality
    description: Professionals with clearly defined AI goals report more benefits.
    figure: 1.8 times as likely to see tangible organisational benefits
    measures: Comparison of professionals who say they have clearly defined AI goals with those who do not, in TR's 2025 Future of Professionals survey (sample size not stated in the article)
    provenance: vendor-published
    source_ref: TRI-TALENT-AI-2025
  - lever: quality
    description: Prevalence of personal AI goals.
    figure: 39% of professionals have personal goals linked to AI adoption
    measures: Share of all professionals surveyed saying they have personal goals linked to AI adoption (TR 2025 survey)
    provenance: vendor-published
    source_ref: TRI-TALENT-AI-2025
  prerequisites:
  - Communicated organisational AI strategy
  - Performance framework that can carry the goals
  risks_and_guardrails:
  - Goals tied to AI use can reward usage over judgment; no source tests this.
  - If AI is used to evaluate people, employment-AI rules may apply (use case 19).
  human_checkpoints:
  - Manager review of goals
  role_evolution: Managers hold individuals to AI adoption goals; AI posture becomes part of progression criteria (in TRI's framing).
  evidence_grade: C
  sources:
  - ref: TRI-TALENT-AI-2025
    title: 'Future of Professionals: How to maximize the value of AI investments through talent'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/future-of-professionals-maximizing-ai-investment-through-talent
    date: '2025-11-17'
    access: full
    locator: Sections 'Clearly communicate organization's AI strategy and goals' and 'Leverage professionals' personal AI use to drive accountability'
  last_reviewed: '2026-10-19'
  notes: Survey from Nov 2025 article about the 2025 report; no named firm. The 1.8 times and 39% figures are correlations in a vendor survey.
- id: professional-services-talent-learning-17
  archetype: professional-services
  module: talent-learning
  function: service-delivery
  title: Upskill resource and engagement managers to run hybrid human-and-agent teams
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Resource managers are being asked to staff teams that mix experts and AI agents without outcome data or playbooks.
  solution: The Resource Management Institute study for Kantata finds most organisations early in the transition and calls for playbooks, skills enablement and workflow changes before hybrid staffing is routine.
  outcomes:
  - lever: capacity
    description: Readiness to manage hybrid teams.
    figure: 52.7% not equipped; 28.4% slightly equipped; 4% well equipped
    measures: Share of respondents (resource managers, sample size not stated in the release) rating their equipment to manage hybrid human-and-AI-agent teams
    provenance: vendor-published
    source_ref: KANTATA-RMI-2026
  - lever: quality
    description: Outcome data in staffing.
    figure: 7.3% say outcome data is easily accessible and routinely used
    measures: Share of respondents who say outcome data is easily accessible and routinely used in staffing decisions
    provenance: vendor-published
    source_ref: KANTATA-RMI-2026
  prerequisites:
  - Skills and outcomes data in one place
  - Playbooks for team composition
  risks_and_guardrails:
  - EU AI Act high-risk rules for employment-related AI apply from 2 December 2027 (EC-AIACT-2026); AI-assisted staffing decisions fall under that regime.
  human_checkpoints:
  - Resource manager approves team composition (implied)
  role_evolution: 72% of respondents say resource management is primarily or solely operational today; the study frames a shift toward strategic team-composition roles (KANTATA-RMI-2026).
  evidence_grade: C
  sources:
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services (study by the Resource Management Institute, commissioned by Kantata)
    publisher: Kantata
    type: survey
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Body of the press release
  - ref: EC-AIACT-2026
    title: 'AI Act: regulatory framework for AI (page last updated 2026-10-19)'
    publisher: European Commission, Shaping Europe's digital future
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: 'Timeline: rules for employment-related high-risk uses apply from 2 December 2027'
  last_reviewed: '2026-10-19'
  notes: Vendor-commissioned (Kantata sells PSA software). Overlaps staffing-resourcing; kept here for the manager-skills angle.
- id: professional-services-talent-learning-18
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: AI screening and ranking of applicants under bias-audit, notice and human-review rules
  work_types:
  - transaction-processing
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: AI tools sort CVs and score applicants. Regulators say that, if not lawful and fair, they may unfairly exclude people or compromise privacy. Rules are arriving in several jurisdictions at once.
  solution: 'Use AI to source, summarise and score applicants only with the controls regulators now expect: a bias audit and public summary (New York City), notice to employees or applicants (New York City, Illinois), documentation and human review (Colorado from 1 January 2027), fair and minimal processing and clear candidate explanations (UK ICO), and high-risk obligations from 2 December 2027 for EU employment uses such as CV-sorting software.'
  outcomes:
  - lever: risk
    description: UK regulator audit of AI recruitment tools.
    figure: Almost 300 recommendations, all accepted or partially accepted
    measures: Recommendations made by the ICO to several audited providers and developers of AI recruitment tools; providers accepted or partially accepted all
    provenance: independent
    source_ref: ICO-AIRECRUIT-2024
  prerequisites:
  - Vendor documentation on training data and limitations
  - Bias audit and notice processes
  - A route for candidates to ask for human review
  risks_and_guardrails:
  - 'New York City: tool must have had a bias audit within one year of use, audit information must be public, and notices given (NYC-LL144-2023).'
  - 'Illinois (effective 1 January 2026): using AI that has the effect of discriminating in recruitment, hiring, promotion, selection for training or apprenticeship, discipline and other terms is a civil rights violation, and employers must notify employees of such AI use (ILLINOIS-HB3773-2024, section (L)).'
  - 'Colorado SB26-189 (signed 2026-05-14): developers must give deployers documentation from 1 January 2027, deployers must describe the tool''s role after an adverse decision, and consumers may request human review (COLORADO-SB26189-2026).'
  - 'EU: CV-sorting software for recruitment is cited as a high-risk example; Annex III obligations extended to 2 December 2027 (EC-AIACT-2026).'
  - California State Bar guidance flags AI in screening of clients or candidates as a risk of unlawful or unethical bias (CALBAR-GENAI-2026, p.9).
  - 'Litigation: Mobley v. Workday is described as the first major test of whether an AI vendor, not just the employer, can be liable for algorithmic hiring bias (NATLAW-AIHIRING-2026).'
  human_checkpoints:
  - Human review of adverse outcomes on request (Colorado)
  - Bias audit before use (New York City)
  role_evolution: Recruiters and HR leads own vendor due diligence, audits and candidate notices.
  evidence_grade: C
  sources:
  - ref: ICO-AIRECRUIT-2024
    title: ICO intervention into AI recruitment tools leads to better data protection for job seekers
    publisher: UK Information Commissioner's Office
    type: regulator
    url: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/11/ico-intervention-into-ai-recruitment-tools-leads-to-better-data-protection-for-job-seekers/
    date: '2024-11-06'
    access: full
    locator: News item text
  - ref: NYC-LL144-2023
    title: Automated Employment Decision Tools (AEDT), Local Law 144 of 2021
    publisher: New York City Department of Consumer and Worker Protection
    type: regulator
    url: https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page
    date: 2023-07
    access: full
    locator: Page introduction
  - ref: ILLINOIS-HB3773-2024
    title: Public Act 103-0804 (HB 3773), amending the Illinois Human Rights Act; effective 1 January 2026
    publisher: Illinois General Assembly
    type: regulator
    url: https://www.ilga.gov/legislation/publicacts/fulltext.asp?Name=103-0804
    date: '2026-01-01'
    access: full
    locator: Section (L) Use of artificial intelligence; Effective Date 1/1/2026
  - ref: COLORADO-SB26189-2026
    title: SB26-189 Automated Decision-Making Technology (signed by the Governor 2026-05-14)
    publisher: Colorado General Assembly
    type: regulator
    url: https://leg.colorado.gov/bills/sb26-189
    date: '2026-05-14'
    access: full
    locator: Bill Summary; status table (Governor Signed 05/14/2026)
  - ref: EC-AIACT-2026
    title: 'AI Act: regulatory framework for AI (page last updated 2026-10-19)'
    publisher: European Commission, Shaping Europe's digital future
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: High-risk list and timeline
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.9
  - ref: NATLAW-AIHIRING-2026
    title: Patchwork AI Hiring Laws Create Rising Compliance Risks for Employers (Andrew Adams, Darrow Everett LLP)
    publisher: The National Law Review
    type: press
    url: https://natlawreview.com/article/patchwork-ai-hiring-laws-create-rising-compliance-risks-employers
    date: '2026-05-12'
    access: full
    locator: Sections on Illinois, Colorado and 'Litigation Signals the Stakes'
  last_reviewed: '2026-10-19'
  notes: 'No professional-services firm was found describing its use of AI applicant screening, so this entry documents the regulatory conditions for a common recruiting practice rather than a named firm deployment (grade C: regulator-documented tools, no named firm). The ICO item is outside the 18-month window and is used as a foundation. The National Law Review alert (May 2026) describes the earlier Colorado Act; the enacted SB26-189 replaced those provisions. Mobley v. Workday status after 2025 was not confirmed.'
- id: professional-services-talent-learning-19
  archetype: professional-services
  module: talent-learning
  function: people-hr
  title: AI-assisted decisions on promotion, training selection, discipline and pay
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: Performance and career decisions in firms rest on partner judgment and hours data; AI could score, rank or flag people, which brings the same legal duties as hiring.
  solution: 'Idea (not found deployed in professional services): use AI-generated indicators in performance review, promotion, selection for training and pay. The laws below already treat these as in scope.'
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: No professional-services deployment or measurement was found
    provenance: self-reported
    source_ref: ILLINOIS-HB3773-2024
  prerequisites:
  - Validated, explainable indicators
  - Notice to employees
  - Impact assessment where required
  risks_and_guardrails:
  - Illinois lists recruitment, hiring, promotion, renewal, selection for training or apprenticeship, discharge and discipline, and requires notice to employees (ILLINOIS-HB3773-2024, section (L)).
  - Colorado defines a consequential decision as one relating to access to, eligibility for or compensation related to employment, and gives consumers a right to request human review after adverse outcomes (COLORADO-SB26189-2026).
  - The EU page lists AI tools for employment and management of workers among high-risk uses, with obligations from 2 December 2027 (EC-AIACT-2026).
  - California flags use of AI in employment actions as a bias risk and says firms should set policies to identify and address bias (CALBAR-GENAI-2026, p.9).
  human_checkpoints:
  - Human decision and review for every adverse outcome
  role_evolution: Partners and HR retain decision rights; AI indicators would be inputs.
  evidence_grade: D
  sources:
  - ref: ILLINOIS-HB3773-2024
    title: Public Act 103-0804 (HB 3773), amending the Illinois Human Rights Act; effective 1 January 2026
    publisher: Illinois General Assembly
    type: regulator
    url: https://www.ilga.gov/legislation/publicacts/fulltext.asp?Name=103-0804
    date: '2026-01-01'
    access: full
    locator: Section (L)
  - ref: COLORADO-SB26189-2026
    title: SB26-189 Automated Decision-Making Technology (signed by the Governor 2026-05-14)
    publisher: Colorado General Assembly
    type: regulator
    url: https://leg.colorado.gov/bills/sb26-189
    date: '2026-05-14'
    access: full
    locator: Bill Summary
  - ref: EC-AIACT-2026
    title: 'AI Act: regulatory framework for AI (page last updated 2026-10-19)'
    publisher: European Commission, Shaping Europe's digital future
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: High-risk use-case list
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (replaces the November 2023 version)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: p.9
  last_reviewed: '2026-10-19'
  notes: 'Label: idea. Regulators describe the category; no firm announcement was found. Kept so interviews can check whether any client firm already does it.'
```

## 3. Module notes

### Processes and key steps (work types)

- **Graduate and lateral recruiting and selection** (coordination-scheduling; transaction-processing when applicants are screened): forecast intake, source, screen, assess, offer. AI-based screening falls under employment-AI rules (NYC-LL144-2023, ILLINOIS-HB3773-2024, COLORADO-SB26189-2026, EC-AIACT-2026).
- **Onboarding and AI-literacy training** (coordination-scheduling; expert-judgment): orientation, tool training, policy sign-off, champions, mentoring (TRI-ONBOARDING-2026; ILTA-TECHSURVEY-2026).
- **Apprenticeship and skill formation** (expert-judgment; review-assurance): supervised practice on real work, review, feedback, rotation. The step that is changing: first-pass research, drafting, document review and data processing now done or pre-done by AI (LEXIS-SYMPOSIUM-2026; ICAEW-JUNIOR-2026).
- **Supervision of AI-assisted junior work** (review-assurance): disclosure, source checking, second-level review (CALBAR-GENAI-2026; DWF-SRA-2026).
- **Performance, promotion and pay** (data-reporting; expert-judgment): hours, client feedback, revenue; no evidence of AI-based scoring found.
- **Career paths and leverage design** (coordination-scheduling; data-reporting): class sizes, lateral mix, non-equity roles, innovation seats (BLOOMBERG-FIRSTYEAR-2026; TRI-LFFI-Q2-2026; NONBILLABLE-AOS-2026).

### Common pain points

- Junior work served two purposes, billing and training; AI removes the training value when it removes the task (VAULT-PYRAMID-2026, quoting Guggenberger).
- Managers already found it hard to give juniors effective work; AI removes more of it (ICAEW-JUNIOR-2026, Larsen quote).
- Firms cannot yet show clients AI savings at matter level; 'still gathering the data' (TRI-LEGALWEEK-2026), which complicates reinvesting savings in training.
- Intake planning under uncertainty: 19% of surveyed large firms cannot say what they will need in 2028 (BLOOMBERG-FIRSTYEAR-2026).
- Retention of mid-career staff who see an AI value gap (TR-FOP-2026).
- Shadow AI: 34% of professionals use tools their organisation has not sanctioned (TR-FOP-2026).

### Metrics and benchmarks

| Metric | Value | Measures | Source |
|---|---|---|---|
| Quality gain with AI (patent drafting) | +0.34 SD (10 days), +0.38 SD (90 days) | Blinded expert scores, treated vs control, 133 lawyers | NBER-AUTOR-2026 |
| Retained skill, no-AI redline | +0.32 SD overall, +0.45 SD seniors, no average gain for juniors | Same trial, later test | NBER-AUTOR-2026 |
| Young workers in AI-exposed jobs | 19% below peer path (15% at the July 2025 vintage) | Employment of ages 22-25, most vs least exposed occupations, ADP data to June 2026 | STANFORD-CANARIES-2026 |
| New graduates hired, 500+ lawyer firms | 6,588 in 2025, down 7.5% from 2024 peak | NALP via Bloomberg Law | BLOOMBERG-FIRSTYEAR-2026 |
| Large firms expecting fewer first-years in 2028 vs 2025 | Two-thirds (57 firms) | Citi survey, summer 2026 | BLOOMBERG-FIRSTYEAR-2026 |
| Training required before GenAI access | 11% (under 50 lawyers) to 72% (over 700) | ILTA Q3.18, share of firms per band | ILTA-TECHSURVEY-2026 |
| Skills gaps among juniors | 72% reasoning and argumentation; 69% verification | LexisNexis UK survey, 873 respondents | LEXIS-MENTORSHIP-2026 |
| Early-career support need | 71% say structured support from experienced peers needed | TR survey, 1,816 professionals | TR-FOP-2026 |
| Trusted-judgment timeline | Legal +1.7 (lengthen); tax 1.0 (shorten) | TR survey, professionals' expectations | TR-FOP-2026 |
| AI value-gap attrition | 24% of those with a gap considering leaving within two years; $232,000 replacement cost estimate | TR survey and TR estimate | TR-FOP-2026 |
| Mid-tier accountancy firms expecting fewer early-career roles | 68% | ICAEW mid-tier research | ICAEW-WORRY-2026 |
| UK Big Four graduate intake 2023 to 'last year' | KPMG 1,399 to 942; Deloitte 1,700 to 1,400; EY 1,800 to 1,600; PwC 1,600 to 1,500 | Telegraph figures via Scottish Financial News | SFN-BIGFOUR-2025 |
| UK top-employer graduate recruitment since 2022 | -24.5% | High Fliers survey of 100 leading employers | HIGHFLIERS-GM-2026 |
| 'Seniorised' entry-level roles | +35% since 2019; AI-exposed junior roles 7x more likely to ask for senior skills | PwC job-ad analysis | PWC-AIJB-2026 |
| Demand for Big Law lawyer hours | +4.2% in H1 2026 (normal about 1.5%) | Citi law firm banking group | BLOOMBERG-AICOST-2026 |
| SRA reports of AI misuse | 42 in the past year | SRA, via DWF article | DWF-SRA-2026 |
| A&E firm staffing vs revenue | Staff growth 1.2%; revenue forecast +9.5% | Deltek Clarity A&E study (vendor) | DELTEK-CLARITY-2026 |

**Quality evidence.** One controlled study (NBER-AUTOR-2026) and two older experiments (HBS-DELLACQUA-2023, UMN-CHOI-2024). No source reports error rates, override rates or parallel-run results for any training or performance process. No inspection finding about training or supervision of AI-assisted juniors was found; the SRA and court cases are the nearest evidence of failure.

### Guardrails and regulatory points

- **Competence and supervision.** California: the duty of competence includes reviewing and verifying AI output; managers set policies, train staff and update controls; subordinates must exercise independent judgment (CALBAR-GENAI-2026, pp.4, 7). D.C. 388: supervisory duties under Rules 5.1 and 5.3 reach supervised lawyers' GenAI use (DCBAR-OP388-2024). Texas 705: responsibility for work product regardless of who or what drafts it (TXBAR-OP705-2025). ABA Formal Opinion 512 (2024-07-29) primary text blocked; secondary summaries say managers must set policies and train staff (ABA-OP512-2024).
- **Billing limits on training.** Hourly time saved by AI cannot be billed (TXBAR-OP705-2025, quoting D.C. 388); California says hourly billing must reflect time actually spent and general AI subscriptions are overhead (CALBAR-GENAI-2026, p.8). Secondary summaries of ABA 512 say not to bill clients to learn AI in general.
- **UK solicitors.** SRA warning notice of 17 August 2026 on AI misuse (hallucinations; confidential data in unsafe tools), seen only through DWF (DWF-SRA-2026). Responsibility for erroneous work falls at all levels, per DWF.
- **Employment-AI law (recruiting, promotion, training selection, discipline, pay).** NYC bias audit and notice (NYC-LL144-2023); Illinois notice and anti-discrimination, effective 2026-01-01 (ILLINOIS-HB3773-2024); Colorado SB26-189 signed 2026-05-14, developer duties and consumer human-review rights from 2027-01-01 (COLORADO-SB26189-2026); EU AI Act Annex III employment uses from 2027-12-02 under the Omnibus that entered into force 2026-07-27 (EC-AIACT-2026); UK ICO recruitment-tool audit with almost 300 recommendations (ICO-AIRECRUIT-2024).
- **AI literacy.** The EU Commission page says AI literacy obligations applied from 2 February 2025; whether the Omnibus altered that duty was not checked (EC-AIACT-2026).
- **Client AI terms.** Some clients ask for line-item AI transparency on invoices or still demand permission before AI use (TRI-LEGALWEEK-2026). No client term specific to junior staffing or training was found.
- **Accounting.** The CCAB Ethics Group plans a draft Statement to the Profession on ethical AI use, with a webinar in the autumn (ICAEW-CCAB-2026, planned, not published when read). No AICPA, ACCA or FRC text on training or entry-level work was reached.

### Frontier signals (dated)

- 2026-10-12: TRI describes Duane Morris onboarding with practice-group AI champions and a fixed 'first draft is never final' principle (TRI-ONBOARDING-2026).
- 2026-09-10: Bloomberg Law reports Citi survey: two-thirds of 57 large firms expect fewer first-years in 2028 (BLOOMBERG-FIRSTYEAR-2026).
- 2026-09-07: NBER publishes the patent-drafting expertise trial (NBER-AUTOR-2026).
- 2026-08: Stanford/NBER update widens the entry-level gap to 19% (STANFORD-CANARIES-2026).
- 2026-08-17: SRA issues AI warning notice (DWF-SRA-2026, secondary).
- 2026-06-15: PwC AI Jobs Barometer: 'seniorised' entry-level roles up 35% since 2019 (PWC-AIJB-2026).
- 2026-05: California's State Bar issues revised guidance covering agentic AI (CALBAR-GENAI-2026; the PDF creation date is 2026-05-15, adoption date not stated).
- 2026-05-14: Colorado SB26-189 signed; developer duties from 2027-01-01 (COLORADO-SB26189-2026).
- 2026-04-07: CCAB Ethics Group announces a planned draft Statement on ethical AI use for the profession (ICAEW-CCAB-2026).
- 2026-02-02: LexisNexis publishes The mentorship gap survey (LEXIS-MENTORSHIP-2026).

### Workforce and role effects

- Entry-level roles move toward review, validation, anomaly spotting and client contact (ICAEW-JUNIOR-2026; PWC-AIJB-2026).
- Juniors are asked to supervise AI output earlier than before, which trainees themselves flag as a risk (ICAEW-WORRY-2026).
- New roles: practice-group AI champions, chief legal talent and growth officer, associate innovation seats (TRI-ONBOARDING-2026; NONBILLABLE-AOS-2026).
- Leverage: associates and non-equity partners carry most extra workload; the ratio of non-equity to equity partner hours is the highest since late 2018 (TRI-LFFI-Q2-2026).
- Pay premium: AI-related roles in professional services advertise a 67% wage premium over non-AI roles in the sector (PWC-AIJB-PS-2026).
- Mid-career professionals are the most mobile and operationally critical (TR-FOP-2026).
- In-house: the TR survey covers corporate and government departments; legal ops is described as becoming a design function for how work is structured (TR-FOP-2026, respondent quote) (in-house).

### Objections and concerns practitioners raise

- Juniors will lose the foundational tasks that built judgment; 48% of TR respondents fear this (TR-FOP-2026).
- Supervisors cannot easily tell polished AI work from understood work (ICAEW-WORRY-2026, Laurenti).
- Counter-view: some trainees say the tasks AI took over were not ones they would have learnt from (ICAEW-WORRY-2026, James).
- Veteran scepticism: prior 'transformative innovations' produced little change (ILTA respondent, ILTA-TECHSURVEY-2026).
- AI cannot be blamed for intake cuts that follow economic cycles (HIGHFLIERS-GM-2026; ICAEW-WORRY-2026).
- Risk of 'creating lawyers who can supervise AI outputs' without judging correctness (VAULT-PYRAMID-2026).

### Interview probes for an advisor

1. Which tasks did first- and second-year staff do two years ago that AI now does, and where do they now learn what those tasks taught? Who checks that they have?
2. Do you test junior judgment without AI at any point (a closed-book review, a live redline)? What would you see if skills were eroding?
3. What is your intake plan for 2027-2028, what assumptions drive it, and what is your fallback if you are wrong in either direction?
4. How are junior utilisation targets, reviews and bonuses treated when AI shortens a task, and how do you fund development time given billing rules and client pushback?
5. Does any tool score applicants, rank staff, or suggest who gets training or promotion? Has legal checked it against Illinois, NYC, Colorado or EU rules?
6. What must a junior disclose to a supervisor when AI contributed, and who reviews the sources?

## 4. Routed to other modules

- **scoping-pricing:** STANFORD-DEL-2026 (hybrid and asset-based pricing); Citi finding that three-fourths of 57 firms expect the billable hour to be affected by AI in 2028 (BLOOMBERG-AICOST-2026).
- **billing-collections:** California rules on charging for AI costs and subscriptions (CALBAR-GENAI-2026, p.8); clients asking for line-item AI billing (TRI-LEGALWEEK-2026).
- **firm-finance:** LFFI Q2 2026 leverage economics (TRI-LFFI-Q2-2026); AI-skill wage premium (PWC-AIJB-PS-2026); Citi's demand growth of 4.2% (BLOOMBERG-AICOST-2026).
- **staffing-resourcing:** Kantata/RMI readiness data (KANTATA-RMI-2026); Deltek A&E staff growth and turnover (DELTEK-CLARITY-2026); employment-AI rules apply to AI-assisted staffing decisions (EC-AIACT-2026).
- **quality-review / acceptance-risk:** SRA warning notice, Cork & Anor v Smith and the 67 UK hallucination cases (DWF-SRA-2026); California rules on agentic confidentiality (CALBAR-GENAI-2026, pp.5-6).
- **client-development:** TR survey on clients reconsidering firms for AI capability (TR-FOP-2026).
- **knowledge-management:** Firms 'extracting the knowledge of their lawyers' into AI workflows (VAULT-PYRAMID-2026, quoting Engstrom).

## 5. Sources

Date is publication date or the best date found; 'access' is full (opened and read) or search-only. ILTA's date is inferred from the file prefix '2606' (a text mirror reports the object date as 2026-09-16). The California PDF date is the file creation date. TR-FOP-2026 shows only the survey period (March-April 2026); no publication date was visible. The High Fliers date is the page's last-modified date; the report itself is described as published in early January.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER Working Paper 35720) | National Bureau of Economic Research (Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere) | academic | https://www.nber.org/papers/w35720 | 2026-09-07 | full |
| STANFORD-CANARIES-2026 | Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence (updated version, data through June 2026) | Stanford Digital Economy Lab / NBER (Brynjolfsson, Chandar, Chen) | academic | https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf | 2026-08 | full |
| UMN-CHOI-2024 | Lawyering in the Age of Artificial Intelligence, 109 Minn. L. Rev. 147 | University of Minnesota Law Review (Choi, Monahan, Schwarcz) | academic | https://scholarship.law.umn.edu/minnlrev/vol109/iss1/3 | 2024-11 | full |
| HBS-DELLACQUA-2023 | Navigating the Jagged Technological Frontier (HBS Working Paper 24-013) | Harvard Business School with Boston Consulting Group | academic | https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 | 2023-09 | full |
| BCG-JAGGED-2023 | How People Create and Destroy Value with Gen AI | Boston Consulting Group | firm | https://www.bcg.com/publications/2023/how-people-create-and-destroy-value-with-gen-ai | 2023-09-21 | full |
| STANFORD-DEL-2026 | Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives | Stanford Digital Economy Lab (Brynjolfsson, Petropoulos) | academic | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | 2026-08-23 | full |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (replaces the November 2023 version) | State Bar of California, Standing Committee on Professional Responsibility and Conduct | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05 | full |
| EC-AIACT-2026 | AI Act: regulatory framework for AI (page last updated 2026-10-19) | European Commission, Shaping Europe's digital future | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-19 | full |
| ICO-AIRECRUIT-2024 | ICO intervention into AI recruitment tools leads to better data protection for job seekers | UK Information Commissioner's Office | regulator | https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/11/ico-intervention-into-ai-recruitment-tools-leads-to-better-data-protection-for-job-seekers/ | 2024-11-06 | full |
| NYC-LL144-2023 | Automated Employment Decision Tools (AEDT), Local Law 144 of 2021 | New York City Department of Consumer and Worker Protection | regulator | https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page | 2023-07 | full |
| ILLINOIS-HB3773-2024 | Public Act 103-0804 (HB 3773), amending the Illinois Human Rights Act; effective 1 January 2026 | Illinois General Assembly | regulator | https://www.ilga.gov/legislation/publicacts/fulltext.asp?Name=103-0804 | 2026-01-01 | full |
| COLORADO-SB26189-2026 | SB26-189 Automated Decision-Making Technology (signed by the Governor 2026-05-14) | Colorado General Assembly | regulator | https://leg.colorado.gov/bills/sb26-189 | 2026-05-14 | full |
| SRA-WARNING-2026 | SRA warning notice on the use of AI (issued 17 August 2026) | Solicitors Regulation Authority | regulator | https://www.sra.org.uk | 2026-08-17 | search-only |
| DCBAR-OP388-2024 | Ethics Opinion 388: Attorneys' Use of Generative Artificial Intelligence in Client Matters | District of Columbia Bar | professional-body | https://www.dcbar.org/for-lawyers/legal-ethics/ethics-opinions-210-present/ethics-opinion-388 | 2024-04 | full |
| TXBAR-OP705-2025 | Opinion 705: lawyer's use of generative artificial intelligence | Professional Ethics Committee for the State Bar of Texas (hosted by the Texas Center for Legal Ethics) | professional-body | https://www.legalethicstexas.com/resources/opinions/opinion-705/ | 2025-02 | full |
| ABA-OP512-2024 | ABA Formal Opinion 512: Generative Artificial Intelligence Tools | American Bar Association, Standing Committee on Ethics and Professional Responsibility | professional-body | https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf | 2024-07-29 | search-only |
| MCA-SURVEY-2026 | MCA Member Survey 2026 | Management Consultancies Association | professional-body | https://www.mca.org.uk/reports/mca-member-survey-2026 | 2026-01-20 | full |
| ICAEW-JUNIOR-2026 | Why we still need junior accountants in the age of AI, and how their roles might change | ICAEW Insights | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/apr-2026/why-we-still-need-junior-accountants-and-how-their-role-might-change | 2026-04-02 | full |
| ICAEW-WORRY-2026 | AI: are junior accountants worried about roles? | ICAEW Insights | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/jun-2026/ai-are-junior-accountants-worried-about-roles | 2026-06-10 | full |
| ICAEW-CCAB-2026 | How can accountants use AI ethically? | ICAEW Insights (reporting the CCAB Ethics Group) | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/apr-2026/how-can-accountants-use-ai-ethically | 2026-04-07 | full |
| ILTA-TECHSURVEY-2026 | The ILTA Technology Survey 2026: Executive Summary | International Legal Technology Association | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 | full |
| TR-FOP-2026 | Future of Professionals Report 2026: When the AI strategy doesn't reach the desk | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 | full |
| HIGHFLIERS-GM-2026 | The Graduate Market in 2026 (report page) | High Fliers Research | survey | https://highfliers.co.uk/publication-the-graduate-market-report | 2026-03-19 | full |
| LEXIS-MENTORSHIP-2026 | AI Is Speeding Up Junior Lawyers' Work but Raising Questions About How Judgment Is Learned (press release on The mentorship gap report) | LexisNexis Legal & Professional | survey | https://www.lexisnexis.com/community/amp-pressroom/ai-is-speeding-up-junior-lawyers-work-but-raising-questions-about-how-judgment-is-learned | 2026-02-02 | full |
| LEXIS-SYMPOSIUM-2026 | Lawyering in the Age of AI: Preparing the Next Generation for Practice (LexisNexis AI Symposium panel recap) | LexisNexis Legal & Professional | vendor | https://www.lexisnexis.com/community/amp-insights/82/lawyering-in-the-age-of-ai-preparing-the-next-generation-for-practice | 2026-06-02 | full |
| KANTATA-RMI-2026 | New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services (study by the Resource Management Institute, commissioned by Kantata) | Kantata | survey | https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services | 2026-04-09 | full |
| TRI-LFFI-Q2-2026 | Q2 2026 LFFI: A heavier load, yet a faster crossing | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed | 2026-08-10 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-ONBOARDING-2026 | Redesigning new attorney onboarding for the AI era | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding | 2026-10-12 | full |
| TRI-TALENT-AI-2025 | Future of Professionals: How to maximize the value of AI investments through talent | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/future-of-professionals-maximizing-ai-investment-through-talent | 2025-11-17 | full |
| TRI-GENAI-TALENT-2024 | GenAI in the legal industry: Where it's already impacting legal talent management | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/genai-legal-talent | 2024-11-04 | full |
| PWC-AIJB-2026 | 2026 AI Jobs Barometer: Two futures for jobs in an AI era | PwC | firm | https://www.pwc.com/gx/en/services/ai/ai-jobs-barometer.html | 2026-06-15 | full |
| PWC-AIJB-PS-2026 | 2026 Global AI Jobs Barometer: Professional Services sector report | PwC | firm | https://www.pwc.com/gx/en/issues/artificial-intelligence/job-barometer/2026/pwc-aijb-2026-professional-services-report.pdf | 2026-06-17 | full |
| DWF-SRA-2026 | Prompt, review, repeat: A guide to AI for trainees and junior solicitors | DWF Group | firm | https://dwfgroup.com/en/news-and-insights/insights/2026/8/prompt-review-repeat-a-guide-to-ai-for-trainees-and-junior-solicitors | 2026-08-21 | full |
| BLOOMBERG-FIRSTYEAR-2026 | Big Law First-Year Hiring Set to Plunge as History, AI Collide (Big Law Business column, Roy Strom) | Bloomberg Law | press | https://news.bgov.com/business-and-practice/big-law-first-year-hiring-set-to-plunge-as-history-ai-collide | 2026-09-10 | full |
| BLOOMBERG-AICOST-2026 | Big Law AI Cost Savings Remain a Mystery as Billable Hours Jump (Big Law Business column, Roy Strom) | Bloomberg Law | press | https://news.bgov.com/business-and-practice/big-law-ai-cost-savings-remain-a-mystery-as-billable-hours-jump | 2026-09-03 | full |
| VAULT-PYRAMID-2026 | The Compressed Pyramid: What AI Means for the Associate Career Ladder (Travis Whitsitt) | Vault | press | https://legacy.vault.com/blogs/vaults-law-blog-legal-careers-and-industry-news/the-compressed-pyramid-what-ai-means-for-the-associate-career-ladder | 2026-08-11 | full |
| SFN-BIGFOUR-2025 | Big Four slash graduate jobs as AI takes over entry-level tasks (reporting The Telegraph) | Scottish Financial News | press | https://www.scottishfinancialnews.com/articles/big-four-slash-graduate-jobs-as-ai-takes-over-entry-level-tasks | 2025-06-23 | full |
| PEOPLEMATTERS-MCK-2025 | McKinsey rejects AI job fears, to boost hiring by 12% in 2026 (reporting Reuters and the Wall Street Journal) | People Matters | press | https://www.peoplematters.in/news/strategic-hr/mckinsey-rejects-ai-job-fears-to-boost-hiring-by-12percent-in-2026-43536 | 2025-09-12 | full |
| NATLAW-AIHIRING-2026 | Patchwork AI Hiring Laws Create Rising Compliance Risks for Employers (Andrew Adams, Darrow Everett LLP) | The National Law Review | press | https://natlawreview.com/article/patchwork-ai-hiring-laws-create-rising-compliance-risks-employers | 2026-05-12 | full |
| NONBILLABLE-AOS-2026 | Meet the junior lawyers putting AI to work inside A&O Shearman | Non-Billable | press | https://www.nonbillable.co.uk/posts/junior-lawyers-ai-innovation-a-o-shearman-harvey | 2026-03-10 | full |
| DELTEK-CLARITY-2026 | Latest Deltek Clarity industry studies highlight AI challenges | Deltek | vendor | https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/ | 2026-05-12 | full |
| KARBON-SOAI-2026 | The State of AI in Accounting Report 2026 (landing page; report gated) | Karbon | vendor | https://karbonhq.com/resources/ebooks/state-of-ai-accounting-report-2026/ | 2026 | full |
| FORTUNE-PWC-2025 | PwC UK chief on cutting entry-level jobs (Fortune, reporting Business Insider; seen in search results only) | Fortune | press | https://fortune.com/2025/09/08/pwc-uk-chief-cutting-entry-level-junior-gen-z-jobs-ai-economic-headwinds-like-amazon-salesforce | 2025-09-08 | search-only |

Also read for context but not cited: a TRI CMBDO Forum article on law-firm talent (2026-02-06, https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-long-game-on-talent). Secondary summaries of ABA 512 read at todaysgeneralcounsel.com and gc.ai (cited under ABA-OP512-2024 as search-only because the primary was not reached).

## 6. Gaps

- **Primary texts blocked:** ABA Formal Opinion 512 (403, mirror blocked); SRA warning notice and SRA site (Cloudflare challenge); NALP (403); SSRN (CAPTCHA); NBER full text (403). The NBER result uses the abstract only; the Choi/Monahan/Schwarcz sample size is not in the abstract.
- **Not reached at all:** AICPA, ACCA and FRC material on training or entry-level work; Law Society of England and Wales statistics (46% to 61% generative AI use appears only in DWF); General Assembly and BCG Attorney Search primaries; Axios original (quoted via Vault); Guardian and FT originals on Big Four cuts; PwC US and UK intake documents (only a search-result summary); Law360 junior-lawyer survey (paywalled); California ADS regulations (primary page returned 404).
- **PwC professional-services report:** read through a text mirror; only the first pages were captured.
- **No evidence found on:** error or override rates for juniors using AI; parallel runs of AI-assisted versus traditional training; how firms measure the quality of junior development; AI-based performance review or promotion in any professional-services firm; AI applicant screening at a named professional-services firm; client terms that restrict junior staffing or training time; apprenticeship models in architecture, engineering or project consulting; independent measurement of the Duane Morris or A&O Shearman programmes.
- **Search budget:** the shared web-search budget ran out after 11 successful searches, so SRA, AICPA and ACCA leads could not be followed through search. Mobley v. Workday status after 2025 was not confirmed.
- **Source skew:** UK and US large-firm material dominates; vendors (LexisNexis, Thomson Reuters, Kantata, PwC) supply many of the survey figures.

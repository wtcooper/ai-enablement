# Professional services, talent and learning: practice angle (wave 3 deep dive)

- **Archetype:** professional-services
- **Module:** talent-learning (recruiting, graduate intake, training and the apprenticeship model when AI does entry-level work, performance, career paths and the leverage pyramid)
- **Angle:** practice (what firms and in-house teams actually do)
- **Prepared:** 2026-10-19
- **Method note:** Sources were opened with `curl` and the `r.jina.ai` text mirror (most publisher pages), `pdftotext` for PDFs, and the EconPapers abstract page for NBER. About 16 web searches were run before the shared search budget ran out; the last two attempts were refused. Working files stayed in a private folder. Source refs follow the landscape file (`PUBLISHER-SHORT-YYYY`). Quotations are under 25 words.

## 1. Summary

- **Practice is moving faster than evidence.** Named firms are redesigning how juniors learn (Ropes & Gray billable credit for AI learning, Sidley's compulsory AI seat, Duane Morris onboarding, PwC and KPMG UK reviewer-first programmes), but none published a skill, error-catch, retention or quality measurement. The only independent measure of learning outcomes is a pre-registered NBER trial of 133 patent lawyers (NBER-AUTOR-2026).
- **The apprenticeship problem is now measured, not just argued.** In that trial, AI raised work quality by 0.34 to 0.38 SD, but the durable skill gain without AI went entirely to senior lawyers (+0.45 SD); juniors showed no average gain and their scores split. Surveys echo it: 72% of 873 UK legal professionals worry juniors cannot build legal reasoning, and only 2% think AI strengthens learning (LEXIS-MENTORSHIP-2026; LCN-LEXIS-2026).
- **Intake is shrinking, but attribution to AI is weak.** Citi's survey says two-thirds of 57 large law firms expect fewer first-years in 2028 than in 2025, and NALP data show large-firm graduate hiring fell 7.5% from the 2024 peak. Bloomberg Law notes past cycles produced the same pattern and that 19% of firms did not know their 2028 needs (BLAW-FIRSTYEAR-2026). UK Big Four graduate schemes were cut by 6% to 29% between 2023 and 2024 per press (SFN-BIG4-2025).
- **Reviewer-first roles are the common redesign.** PwC's assurance leader expects new hires to supervise AI-performed routine work; KPMG UK front-loads exams and has graduates learn beside partners; the AICPA frames it as moving from doing to supervising (BI-PWC-2025; CITYAM-BIG4TRAINING-2026; JOA-TRAINING-2026). The unresolved question is how reviewers learn to review.
- **Talent systems are being used to force adoption.** KPMG will rate staff on AI objectives in 2026 reviews, Shoosmiths tied a firmwide bonus pool to one million Copilot prompts (reached more than four months early, a tracked usage metric), and Accenture pairs upskilling with exits of people it judges cannot be reskilled (BLOOMBERG-KPMG-2025; LEGALCHEEK-SHOOSMITHS-2025; FORTUNE-ACCENTURE-2025).
- **Recruiting with AI is a trial, with regulation attached.** Mishcon de Reya is trialling an AI screening interview with humans making all screening decisions; McKinsey is reported to test candidates' work with its Lilli tool. UK ICO, New York City Local Law 144 and the EU AI Act (high-risk employment uses from 2 December 2027) frame the guardrails (MISHCON-BRIGHT-2025; GUARDIAN-MCKINSEY-2026; ICO-RECRUIT-2024; NYC-AEDT-2023; EC-AIACT-2026).
- **Coverage skews to law and large firms.** Most named evidence is from legal and large accounting firms. No named in-house shared-service talent deployment was found; in-house voices appear only in surveys and quotes (tagged in-house in notes). No usable job postings from named firms were reached.
- **Counts:** 25 candidate use cases: 2 grade A, 13 grade B, 8 grade C, 2 grade D (ideas).

## 2. Use cases

```yaml
- id: professional-services-talent-learning-01
  title: Protected billable-credit time for first-years to learn and build with AI (Ropes & Gray TrAIlblazers)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - expert-judgment
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: AI takes over research, drafting and review tasks that used to fill a junior lawyer's year, while billable
    targets leave little time to learn the new tools. Associates also worry about how AI affects their careers (BLAW-ASSOCIATES-2026,
    para on message boards).
  solution: First-year associates can put up to 20% of their billable hours (reported as nearly 400 hours a year)
    toward mastering the firm's AI tools, testing emerging tools, writing tailored prompts for client matters and
    experimenting (LCN-ROPES-2025). The programme, called TrAIlblazers, started in the US in 2025 and was extended
    to Europe in January 2026 with formal and on-demand training, partner-led mentoring circles and peer cohorts
    (LCN-ROPES-EU-2026). Inside it, two first-years in the registered funds practice present their AI use to partners
    each month, and a 'World Cup' competition had teams of the firm's young lawyers and summer associates build
    AI workflows for real problems, with full billable credit for taking part (BLAW-ASSOCIATES-2026). The firm's
    tools include Hebbia, ProVision and Harvey (LCN-ROPES-EU-2026).
  outcomes:
  - lever: capacity
    description: Competition entries gave the firm ideas that could scale across first-year work. The winning team
      built a workflow that extracts information from transaction documents to help draft real estate closing documents.
    figure: 25 teams
    measures: teams entered in the firm's AI 'World Cup' for young lawyers and summer associates, judged on problem-solving,
      feasibility, appropriate AI use and presentation
    provenance: self-reported
    source_ref: BLAW-ASSOCIATES-2026
  - lever: quality
    description: none published
    figure: none published
    measures: proficiency, quality, retention or hours-used data for the programme (none found)
    provenance: self-reported
    source_ref: LCN-ROPES-2025
  prerequisites:
  - Firm-approved AI tools and a knowledge-management lead to run the competitions (BLAW-ASSOCIATES-2026)
  - A billing-credit rule that lets AI learning count as billable time (LCN-ROPES-2025)
  - Partners who agree to mentor and to hear junior presentations (LCN-ROPES-EU-2026; BLAW-ASSOCIATES-2026)
  risks_and_guardrails:
  - Competition entries were judged partly on appropriate AI use (BLAW-ASSOCIATES-2026)
  - 'Observation (analyst): protected time costs billable output; no source quantifies the trade-off'
  human_checkpoints:
  - Partners hear and react to junior presentations (BLAW-ASSOCIATES-2026)
  - Mentoring circles led by partners (LCN-ROPES-EU-2026)
  role_evolution: A partner said watching a first-year be 'seniorized' quickly was exciting for the practice group
    (BLAW-ASSOCIATES-2026). In the European rollout, junior lawyers work in peer cohorts on client challenges and
    contribute practical insights to the firm's wider innovation efforts (LCN-ROPES-EU-2026).
  evidence_grade: B
  sources:
  - ref: LCN-ROPES-2025
    title: Ropes & Gray junior lawyers to dedicate 20% of billable time to AI training
    publisher: LawCareers.Net
    type: press
    url: https://www.lawcareers.net/Explore/News/Ropes-Gray-junior-lawyers-to-dedicate-20-of-billable-time-to-AI-training-191120
    date: '2025-11-19'
    access: full
    locator: paragraphs 2-4 (20% allocation, nearly 400 hours, activities)
  - ref: LCN-ROPES-EU-2026
    title: Ropes & Gray commits 20% of junior lawyer billable hours to AI exploration across Europe
    publisher: LawCareers.Net
    type: press
    url: https://www.lawcareers.net/Explore/News/Ropes-Gray-commits-20-of-junior-lawyer-billable-hours-to-AI-exploration-across
    date: '2026-01-14'
    access: full
    locator: paragraphs 1-3 (Europe expansion, mentoring circles, tool list)
  - ref: BLAW-ASSOCIATES-2026
    title: What Does It Take to Get Big Law Associates Excited About AI? (Big Law Business column)
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/what-does-it-take-to-get-big-law-associates-excited-about-ai
    date: '2026-07-30'
    access: full
    locator: paragraphs 3-8 (Ropes & Gray registered funds practice, World Cup)
  last_reviewed: '2026-10-19'
  notes: '''Nearly 400 hours'' is LawCareers.Net citing Reuters (6 Nov 2025), which was blocked; the Law Gazette
    and City AM versions were not used for figures. The 1,900-hour target seen in a search summary is not in any
    page I opened. No Ropes & Gray press release was reached.'
- id: professional-services-talent-learning-02
  title: Compulsory AI working seat in the trainee rotation (Sidley London AI Knowledge Lab)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: announced
  problem: Trainee solicitors used to learn through rotations of practice-area seats, and AI changes the work in
    each seat. Few firms make AI experience a formal part of qualification (LEGALCHEEK-SIDLEY-2026).
  solution: From September 2026 every Sidley London trainee completes one seat in the firm's AI Knowledge Lab as
    part of a new six-seat training contract (up from four). The seat comes after two practice-group seats. Trainees
    carry out genuine assignments for practice groups alongside the Knowledge Management, Research and Data & AI
    teams, test approaches, help build tools for wider use, and are expected to judge AI output critically and decide
    when a lawyer must step in (LEGALCHEEK-SIDLEY-2026). The same article notes a six-month innovation-team seat
    at Stephenson Harwood and a funded technology LL.M at Freshfields (see use case 03).
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: any trainee, quality or retention outcome (the scheme starts in the month of the article)
    provenance: self-reported
    source_ref: LEGALCHEEK-SIDLEY-2026
  prerequisites:
  - An internal KM, research and data/AI function able to host trainees (LEGALCHEEK-SIDLEY-2026)
  - 'A longer rotation structure: six four-month seats (LEGALCHEEK-SIDLEY-2026)'
  risks_and_guardrails:
  - The managing partner calls it a working seat, not a classroom, so trainee work must meet the quality of real
    assignments (LEGALCHEEK-SIDLEY-2026)
  human_checkpoints:
  - Trainees work with practice-group lawyers and KM/research/data staff (LEGALCHEEK-SIDLEY-2026)
  role_evolution: Trainees become testers and co-developers of tools and are expected to qualify with hands-on experience
    of applying AI critically and responsibly (LEGALCHEEK-SIDLEY-2026). A consultant quoted by TRI also suggests
    rotating juniors through knowledge management, professional development and technology teams (TRI-LDEV-2026,
    'Aligning the talent model').
  evidence_grade: C
  sources:
  - ref: LEGALCHEEK-SIDLEY-2026
    title: Sidley adds AI seat in training contract shake-up
    publisher: Legal Cheek
    type: press
    url: https://www.legalcheek.com/2026/09/sidley-adds-ai-seat-in-training-contract-shake-up/amp/
    date: '2026-09-02'
    access: full
    locator: paragraphs 1-6 (AI seat, six seats, Lab description)
  - ref: TRI-LDEV-2026
    title: Rethinking lawyer development in future AI-enabled law firms
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/lawyer-development-ai-enabled-law-firms
    date: '2026-04-16'
    access: full
    locator: section 'Aligning the talent model to the future business model' (rotation suggestion)
  last_reviewed: '2026-10-19'
  notes: Graded C because this is the firm's own announcement of a scheme that takes effect in the month of publication;
    no evidence of operation was found. Sidley recruits up to 19 London trainees a year (Legal Cheek, Firms Most
    List 2027).
- id: professional-services-talent-learning-03
  title: Funded technology-and-law master's for incoming trainees (Freshfields with King's College London)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Incoming trainees need an understanding of technology and AI before they start, and the firm wants it
    earlier in careers (FRESHFIELDS-KCL-2025).
  solution: Freshfields offers fully funded places on a King's College London LL.M in Law & Technology to future
    trainees in its February 2026, August 2026 and February 2027 intakes, with a group from the August 2025 cohort
    to pioneer it. It includes a GBP 20,000 maintenance grant and chances to work with the Innovation team and the
    Freshfields Lab. Trainees start the Trainee Associate Programme after the LL.M. The firm describes it as the
    first such programme offered by a law firm (FRESHFIELDS-KCL-2025).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: any programme outcome (none found)
    provenance: self-reported
    source_ref: FRESHFIELDS-KCL-2025
  prerequisites:
  - An academic partner offering a technology pathway (FRESHFIELDS-KCL-2025)
  - Funding for tuition and a maintenance grant (FRESHFIELDS-KCL-2025)
  risks_and_guardrails:
  - No guardrail stated in the source.
  human_checkpoints:
  - Continued firm connection during studies (FRESHFIELDS-KCL-2025)
  role_evolution: The training principal says the lawyers hired today will lead the firm through the 2030s, so the
    aim is to build their understanding of the technology and the legal challenges it brings for clients (FRESHFIELDS-KCL-2025).
  evidence_grade: C
  sources:
  - ref: FRESHFIELDS-KCL-2025
    title: Freshfields partners with King's College London to offer future trainees LL.M in Law and Technology
    publisher: Freshfields
    type: firm
    url: https://www.freshfields.com/en/our-thinking/news/news-search/2025/07/freshfields-partners-with-kings-college-london-to-offer-future-trainees--ll.m-in-law-and-technology
    date: '2025-07-02'
    access: full
    locator: paragraphs 1-4 and bullet list (programme terms, quotes)
  last_reviewed: '2026-10-19'
  notes: Firm press release, 2 Jul 2025, so slightly outside the 12-18 month window. Uptake and outcomes were not
    found.
- id: professional-services-talent-learning-04
  title: 'Rebuilt onboarding for new associates: AI orientation, practice-level AI champions and a ''first draft
    is never final'' rule (Duane Morris)'
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - expert-judgment
  - document-production
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: The routine tasks that built associates' judgment are being absorbed by AI, yet new lawyers still expect
    their employer to develop them, and many already use AI tools with or without rules (TRI-ONBOARDING-2026).
  solution: 'New Duane Morris lawyers get a two-day in-person orientation that includes a live AI-and-library research
    session, then twice-monthly extended sessions from September to June with internal staff and outside experts.
    Each practice group has designated AI champions (a partner, counsel or senior associate with early access to
    test tools against real work) who help new lawyers use practice-relevant tools. The firm leaves the choice of
    how to use AI in first drafts to the lawyer but holds one fixed principle: a first draft is never an appropriate
    final submission. A separate mentorship track remains, and the firm debriefs each outgoing class to redesign
    the next programme (TRI-ONBOARDING-2026).'
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: onboarding, error or ramp-up outcomes (none published)
    provenance: self-reported
    source_ref: TRI-ONBOARDING-2026
  prerequisites:
  - Practice-level AI champions with early access to tools (TRI-ONBOARDING-2026)
  - A talent function that owns learning design (the interviewee is Chief Legal Talent and Growth Officer) (TRI-ONBOARDING-2026)
  risks_and_guardrails:
  - Responsible-use training must include verification steps and human review to be effective (TRI-ONBOARDING-2026)
  - 'Mixed messages: some partners and clients may say not to use AI while leadership says to use it (TRI-CLOSEGAP-2026)'
  human_checkpoints:
  - First drafts are never final submissions (TRI-ONBOARDING-2026)
  - Mentorship track covers cultural questions, including whether using AI with a given partner will look inefficient
    (TRI-ONBOARDING-2026)
  role_evolution: The firm puts more weight on power skills, such as instilling client confidence and business fluency,
    because AI raises the baseline everyone is judged against (TRI-ONBOARDING-2026). Mid-level associates are already
    building their own agents (TRI-ONBOARDING-2026).
  evidence_grade: B
  sources:
  - ref: TRI-ONBOARDING-2026
    title: Law firms need to redesign new attorney onboarding for the AI era
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding
    date: '2026-10-12'
    access: full
    locator: sections 'What a redesigned onboarding program looks like' and 'Raising the bar for power skills'
  - ref: TRI-CLOSEGAP-2026
    title: 4 ways law firms can close gaps in legal judgment & professional identity
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/closing-legal-judgment-and-professional-identity-gaps
    date: '2026-09-10'
    access: full
    locator: section 'Why associates are facing an identity crisis'
  last_reviewed: '2026-10-19'
  notes: Single-interview account on a Thomson Reuters Institute page (a legal-information vendor's research arm).
    The AI-simulation anecdote concerns the interviewee's prior, unnamed firm; it is used in use case 05, not here.
- id: professional-services-talent-learning-05
  title: AI simulations, personas and pre-review feedback tools that stand in for lost junior repetitions
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - expert-judgment
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: When AI does routine drafting, reconciliation or review, juniors lose the repetitions and the mistake-and-feedback
    loops that built judgment, and seniors have little time to coach (KARBON-JUNIOR-2026; TRI-TEACHV-2026).
  solution: Four approaches are described. (1) Kennedys is launching a training programme with Spellbook that uses
    drafting and review tools to create simulated learning scenarios of the kind juniors would have met on live
    work, first in the US and UK offices (SPELLBOOK-KENNEDYS-2025). (2) Barbri's co-CEO says it plans to launch
    a simulation tool that bridges law school and practice (TRI-TEACHV-2026). (3) At Brigham Young University, an
    accounting professor built an AI review tool for Excel that entry-level staff use to find and fix problems before
    a manager reviews; students also train a deliberately 'ignorant' AI until it passes an exam, and interview an
    AI persona (JOA-TRAINING-2026). (4) A Duane Morris executive describes a ChatGPT-based tool for rehearsing difficult
    feedback conversations, built at her prior firm, that people used privately after a coach-controlled avatar
    version went largely unused (TRI-ONBOARDING-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: skill, error-catch or retention outcomes for any of the four approaches (none found)
    provenance: self-reported
    source_ref: SPELLBOOK-KENNEDYS-2025
  prerequisites:
  - Drafting and review tools that can run exercises (SPELLBOOK-KENNEDYS-2025)
  - A defined verification routine to practise against (TRI-TEACHV-2026)
  risks_and_guardrails:
  - Cognitive offloading and shallow understanding if lawyers rely on AI output (TRI-DESIGNL-2026)
  - A firm-built assistant lets juniors produce advanced output, but they 'may not be able to review it', so firm-level
    review controls are needed (JOA-TRAINING-2026, High Rock Accounting CEO)
  human_checkpoints:
  - Senior lawyers who supervise juniors need training to evaluate AI-assisted work (TRI-TEACHV-2026)
  - Managers still review after the junior's self-check (JOA-TRAINING-2026)
  role_evolution: Juniors practise on simulated work and get immediate, tailored feedback, while seniors move from
    correcting basics to supervising verification (TRI-DESIGNL-2026; TRI-TEACHV-2026).
  evidence_grade: C
  sources:
  - ref: SPELLBOOK-KENNEDYS-2025
    title: 'Preparing the Next Generation of AI-Fluent Lawyers: Spellbook Partners with Kennedys'
    publisher: Spellbook
    type: vendor
    url: https://spellbook.com/stories/kennedys
    date: '2025'
    access: full
    locator: paragraphs 1-4 (programme description)
  - ref: TRI-TEACHV-2026
    title: 'The missing skill in legal AI training: How to teach verification and judgment'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/teaching-verification-and-judgment
    date: '2026-09-01'
    access: full
    locator: section 'Solving the junior lawyer learning paradox'
  - ref: JOA-TRAINING-2026
    title: How will accountants learn new skills when AI does the work?
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/
    date: '2026-03-01'
    access: full
    locator: sections 'AI affects all rungs of the career ladder' and 'Use AI as a training partner'
  - ref: TRI-ONBOARDING-2026
    title: Law firms need to redesign new attorney onboarding for the AI era
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding
    date: '2026-10-12'
    access: full
    locator: section 'Raising the bar for power skills'
  - ref: TRI-DESIGNL-2026
    title: 'Designing lawyers: Attorney growth in the age of AI-fueled practice'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/designing-lawyers-professional-growth
    date: '2026-05-11'
    access: full
    locator: section 'A new model for learning'
  last_reviewed: '2026-10-19'
  notes: 'Grade C: Kennedys and Barbri are announcements or plans (a vendor customer story and a trade-press interview),
    and BYU''s tools are academic. The Spellbook page is undated; the programme is described as set to debut ''later
    this year'', and LawCareers.Net (19 Nov 2025) mentions it, so 2025 is the best date. Kennedys is spelt ''Spellbrook''
    in that LawCareers.Net text.'
- id: professional-services-talent-learning-06
  title: Assurance new hires start as reviewers of AI-performed routine work, with training shifted to fundamentals
    and skepticism (PwC)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - review-assurance
  - expert-judgment
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Entry-level audit work such as data gathering and processing is being taken over by AI, which removes
    the work that used to teach execution first and judgment later (BI-PWC-2025).
  solution: PwC's AI assurance leader said new assurance hires will oversee AI doing routine audit tasks and so
    become reviewers and supervisors quickly. She expects first-years to feel like fourth-years three years from
    now. Training has moved to a back-to-basics approach on what an audit should do for a client, with more programme
    time for critical thinking, negotiation and professional skepticism, which would previously have been taught
    later (BI-PWC-2025). The AICPA's CPA-candidate lead describes the same pivot from doing to supervising and warns
    that supervising a bot requires understanding the underlying procedure (JOA-TRAINING-2026). Withum's chief talent
    officer says it is pushing responsibilities down from seniors to juniors (JOA-TRAINING-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: junior review accuracy, error-catch rates or progression speed (none published)
    provenance: self-reported
    source_ref: BI-PWC-2025
  prerequisites:
  - AI tooling that performs the data gathering and processing (BI-PWC-2025)
  - Training that teaches the underlying procedure so juniors can supervise a tool (JOA-TRAINING-2026)
  risks_and_guardrails:
  - Without the entry-level work, juniors lose error exposure, pattern recognition and judgment under uncertainty
    (KARBON-JUNIOR-2026)
  - Juniors who are 'very good at reviewing AI output' may be uncertain what to do when the AI is wrong (KARBON-JUNIOR-2026)
  - The AI assurance leader acknowledged fear that AI would reduce critical thinking (BI-PWC-2025)
  human_checkpoints:
  - Reviewers and supervisors sign off AI-performed tasks (BI-PWC-2025)
  - Firm-level controls on review of work (JOA-TRAINING-2026)
  role_evolution: First-year roles are expected to resemble manager roles of today within three years, according
    to PwC's AI assurance leader, who spoke of assurance staff only, not advisory or tax (BI-PWC-2025). The AICPA
    frames the shift as executor to evaluator and has launched a 'Profession Ready' research project on early-career
    skills, with findings expected in 2027 (JOA-TRAINING-2026).
  evidence_grade: B
  sources:
  - ref: BI-PWC-2025
    title: PwC is training junior accountants to be like managers, because AI is going to be doing the entry-level
      work
    publisher: Business Insider
    type: press
    url: https://www.businessinsider.com/pwc-ai-training-changing-the-job-accountants-jenn-kosar-2025-8
    date: '2025-08-08'
    access: full
    locator: paragraphs 2-9 (Kosar interview)
  - ref: JOA-TRAINING-2026
    title: How will accountants learn new skills when AI does the work?
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/
    date: '2026-03-01'
    access: full
    locator: sections 'Introduction', 'Upskilling at scale inside firms'
  - ref: KARBON-JUNIOR-2026
    title: How do junior accountants learn when AI does the grunt work?
    publisher: Karbon
    type: vendor
    url: https://karbonhq.com/resources/training-junior-accountants-ai/
    date: '2026-04-30'
    access: full
    locator: section 'What's actually at stake?' and 'Redesigning junior roles around oversight'
  last_reviewed: '2026-10-19'
  notes: The three-year view is the PwC executive's expectation in an interview, not a measured result. Business
    Insider notes she was speaking about assurance, not advisory or tax. The Karbon post is a vendor blog; it reports
    that 20% of accounting firm leaders in Karbon's 2026 survey are already changing organisational design by outsourcing
    junior roles or filling them with AI (survey of about 600 professionals; vendor-published).
- id: professional-services-talent-learning-07
  title: UK Big Four graduate programmes rebuilt around judgement-based work earlier and explicit human-skills training
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - expert-judgment
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Graduates' first-year work of data entry and basic report preparation is being automated, so the old
    sequence of manual tasks, then judgement, no longer fits (CITYAM-BIG4TRAINING-2026).
  solution: City AM asked KPMG, Deloitte, EY and PwC how they are adapting graduate training; it reports all four
    have recently completed major overhauls or are restructuring. KPMG's reworked programme front-loads exams so
    graduates have the technical and regulatory knowledge to advise clients in year two, and has graduates learn
    alongside experienced staff and partners before client engagements. KPMG's chief people officer says graduates
    will review and exercise judgement more than produce outputs. PwC introduced debating sessions and KPMG added
    coaching on basic workplace behaviours. All four told City AM their programmes now train human and workplace
    skills, which the columnist lists as critical thinking, resilience, adaptability and relationship-building (CITYAM-BIG4TRAINING-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: any programme outcome (none published)
    provenance: self-reported
    source_ref: CITYAM-BIG4TRAINING-2026
  prerequisites:
  - Reworked exam and curriculum timelines (CITYAM-BIG4TRAINING-2026)
  - Experienced staff and partners available to teach alongside graduates (CITYAM-BIG4TRAINING-2026)
  risks_and_guardrails:
  - Graduates arrive with strong LLM familiarity but little workplace experience, so basic behaviours need dedicated
    coaching (CITYAM-BIG4TRAINING-2026)
  human_checkpoints:
  - Learning alongside experienced staff and partners before client engagements (CITYAM-BIG4TRAINING-2026)
  role_evolution: Graduates become reviewers and judgement-makers sooner; human skills are now an explicit training
    target (CITYAM-BIG4TRAINING-2026).
  evidence_grade: B
  sources:
  - ref: CITYAM-BIG4TRAINING-2026
    title: How AI is forcing the Big Four to rethink graduate training (Beyond The Billable column)
    publisher: City AM
    type: press
    url: https://www.cityam.com/?p=2459320
    date: '2026-09-23'
    access: full
    locator: sections 'Human skills are the new valuable skill to have' and 'The human touch'
  last_reviewed: '2026-10-19'
  notes: The firms' statements are answers to a City AM questionnaire; the author's wider claim that AI now handles
    first-year tasks is the columnist's framing. No Deloitte or EY programme details beyond quotes.
- id: professional-services-talent-learning-08
  title: Smaller graduate and school-leaver intake alongside AI taking entry-level tasks (UK Big Four, as reported)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: automate
  change_scope: model
  runtime_class: workflow-automation
  maturity: in-production
  problem: The leverage pyramid depends on a wide base of junior staff doing routine work; if AI and offshoring
    take that work, the cost of a large intake looks harder to justify (SFN-BIG4-2025).
  solution: Scottish Financial News, reporting The Telegraph, says the four UK firms recruited fewer graduates and
    school leavers than in 2023 as AI took over entry-level administrative tasks, and also cites cost cutting and
    shifting work to lower-cost countries. KPMG's scheme fell from 1,399 in 2023 to 942 'last year' (the article
    is dated June 2025), with about 1,000 hires expected in 2025. Deloitte went from 1,700 to 1,400 and expects
    flat recruitment, EY from 1,800 to 1,600, and PwC from 1,600 to 1,500. Indeed data show UK accountancy graduate
    job adverts down 44% versus 2023 (SFN-BIG4-2025).
  outcomes:
  - lever: cost
    description: KPMG graduate scheme recruitment fell 29% (1,399 to 942); Deloitte 18% (1,700 to 1,400); EY 11%
      (1,800 to 1,600); PwC 6% (1,600 to 1,500)
    figure: 29%, 18%, 11%, 6%
    measures: change in graduate and school-leaver recruitment per firm between 2023 and the latest full year, as
      compiled by The Telegraph and relayed by Scottish Financial News
    provenance: independent
    source_ref: SFN-BIG4-2025
  - lever: cost
    description: UK accountancy graduate job adverts were 44% lower than in 2023, against 33% lower for all graduate
      jobs
    figure: 44%
    measures: decrease in UK accountancy graduate job adverts on Indeed in 2025 compared with 2023
    provenance: independent
    source_ref: SFN-BIG4-2025
  prerequisites:
  - Offshore and automation capacity to absorb routine work (SFN-BIG4-2025)
  risks_and_guardrails:
  - EY and KPMG say they continue to invest in talent and recruit graduates, school leavers and apprentices; PwC
    and Deloitte declined to comment (SFN-BIG4-2025)
  - 'Causation is not established: the report links the cuts to AI, cost reduction and offshoring together (SFN-BIG4-2025)'
  human_checkpoints:
  - None stated.
  role_evolution: A smaller entry cohort with more work moved to automation and lower-cost locations (SFN-BIG4-2025).
    Compare use case 07 for how remaining graduates are trained.
  evidence_grade: B
  sources:
  - ref: SFN-BIG4-2025
    title: Big Four slash graduate jobs as AI takes over entry-level tasks (reporting The Telegraph, 22 Jun 2025)
    publisher: Scottish Financial News
    type: press
    url: https://www.scottishfinancialnews.com/articles/big-four-slash-graduate-jobs-as-ai-takes-over-entry-level-tasks
    date: '2025-06-23'
    access: full
    locator: paragraphs 1-6 (figures and firm responses)
  last_reviewed: '2026-10-19'
  notes: 'Secondary source: The Telegraph original (22 Jun 2025) was paywalled and not read. The 12-18 month window
    is stretched to 16 months. The City AM column (CITYAM-BIG4TRAINING-2026) says the firms are ''reported'' to
    have scaled back intakes. A search-summary item about PwC taking 1,300 UK graduates (down from 1,500) could
    not be confirmed on a page I opened and is excluded.'
- id: professional-services-talent-learning-09
  title: Large law firms plan smaller first-year classes and favour lateral and AI-experienced hires
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: If AI absorbs repetitive junior work, firms must decide how many first-years to hire and whether to buy
    experience laterally instead (LAW360-CITI-2025).
  solution: A Citi Global Wealth at Work and Hildebrandt Consulting report found 86% of large law firms plan to
    grow associate ranks through 2027 while only 35% plan larger first-year classes, which the report reads as a
    shift to a more senior associate population driven by generative AI (LAW360-CITI-2025). Citi's summer 2026 survey
    of 57 large firms found two-thirds expect fewer first-years in 2028 than in 2025 (BLAW-FIRSTYEAR-2026). SurePoint
    reports laterals were 51% of Am Law 200 associate hires, and mid-size firms prefer laterals because they need
    less training (GLP-SUREPOINT-2026).
  outcomes:
  - lever: cost
    description: Share of large firms planning to increase associate ranks versus first-year classes
    figure: 86% versus 35%
    measures: large law firms planning to increase the size of associate ranks through 2027, and of first-year classes
      (Citi/Hildebrandt report; the base is not stated in the Law360 account)
    provenance: independent
    source_ref: LAW360-CITI-2025
  - lever: cost
    description: Two-thirds of firms expect fewer first-years in 2028 than in 2025; nearly 60% expect fewer second-years;
      19% did not know their 2028 first-year needs
    figure: two-thirds; nearly 60%; 19%
    measures: firms among 57 large firms surveyed by Citi's law firm banking group in summer 2026
    provenance: independent
    source_ref: BLAW-FIRSTYEAR-2026
  - lever: cost
    description: Firms with more than 500 lawyers hired 6,588 new graduates last year, 538 (7.5%) fewer than the
      2024 peak, the first fall since 2011
    figure: 6,588 (-538; -7.5%)
    measures: new law graduates hired by firms of more than 500 lawyers, from NALP data as cited by Bloomberg Law
    provenance: independent
    source_ref: BLAW-FIRSTYEAR-2026
  - lever: cost
    description: Lateral associates were 51% of associate hires in the Am Law 200 last year; lateral hiring rose
      12% from 2024 to 2025 while entry-level hiring was flat
    figure: 51%; +12%
    measures: lateral share of associate hires, and year-on-year change in associate lateral hiring, from SurePoint's
      Law School Hiring Report 2026 as reported by Global Legal Post
    provenance: vendor-published
    source_ref: GLP-SUREPOINT-2026
  prerequisites:
  - Lateral pipeline and onboarding capacity (GLP-SUREPOINT-2026)
  risks_and_guardrails:
  - 'The decline may also follow the historical hiring cycle: past peaks were followed by smaller classes three
    years later, and 2024 was not a recession year (BLAW-FIRSTYEAR-2026)'
  - NALP's own release reports the fall in hires of large firms but does not mention AI (NALP-CLASS2025-2026)
  - Demand for lawyer time was still surging as AI use grew, which could keep hiring up (BLAW-FIRSTYEAR-2026)
  human_checkpoints:
  - None stated.
  role_evolution: Associate populations skew more senior, with more technical roles added (LAW360-CITI-2025). Lateral
    AI-specialism associate hiring grew 106% in 2025 per SurePoint's 2025 report (GLP-SUREPOINT-2026).
  evidence_grade: C
  sources:
  - ref: LAW360-CITI-2025
    title: Law Firms' Junior Roles At Risk From AI, Report Says (on the Citi Global Wealth at Work and Hildebrandt
      Consulting report)
    publisher: Law360 Pulse
    type: press
    url: https://www.law360.com/articles/2422148/law-firms-junior-roles-at-risk-from-ai-report-says
    date: '2025-12-15'
    access: full
    locator: paragraphs 1-4 (associate ranks versus first-year classes)
  - ref: BLAW-FIRSTYEAR-2026
    title: Big Law First-Year Hiring Set to Plunge as History, AI Collide (Big Law Business column)
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/big-law-first-year-hiring-set-to-plunge-as-history-ai-collide
    date: '2026-09-10'
    access: full
    locator: paragraphs 1-3, 7-9 (NALP data, Citi survey)
  - ref: NALP-CLASS2025-2026
    title: Strong Entry-Level Legal Employment Persists Despite Sharp Drop in Federal Government and Public Interest
      Hiring (Class of 2025 selected findings)
    publisher: NALP
    type: professional-body
    url: https://www.nalp.org/uploads/PressReleases/Classof2025SelectedFindings_PressRelease.pdf
    date: '2026-08-05'
    access: full
    locator: key employment findings, bullets 4-5
  - ref: GLP-SUREPOINT-2026
    title: Demand for AI experience drives lateral associate hiring increase, study finds (on SurePoint's Law School
      Hiring Report 2026)
    publisher: Global Legal Post
    type: press
    url: https://www.globallegalpost.com/news/demand-for-ai-experience-drives-lateral-associate-hiring-increase-study-finds-969604187
    date: '2026-07-21'
    access: full
    locator: paragraphs 1-5 (lateral share, AI specialism)
  last_reviewed: '2026-10-19'
  notes: 'Grade C: survey and market-data evidence, no named firm describing its own decision. Hiring figures are
    independent measures of hiring, not of AI impact. The SurePoint report itself is gated; only the Global Legal
    Post account was read.'
- id: professional-services-talent-learning-10
  title: Leverage and staffing-model redesign as AI absorbs junior tasks
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - coordination-scheduling
  - expert-judgment
  pattern: other
  ladder: automate
  change_scope: model
  runtime_class: workflow-automation
  maturity: emerging
  problem: The pyramid model uses many junior hours to produce work that partners review; AI compresses the junior
    layer, and clients are reluctant to pay for tasks done by junior associates (TRI-LDEV-2026).
  solution: 'Firms report they are beginning to plan for changed leverage: the Citi/Hildebrandt report found a quarter
    of law firms expect leverage changes by 2027 and 63% by 2035, and the share of large firms expecting AI to affect
    professional staffing models within two years doubled to 36% (LAW360-CITI-2025). In a General Assembly survey
    of 258 leaders of consulting, accounting and legal firms, 74% of law firms plan to keep headcount flat while
    using AI for efficiency, 14% expect to move to a model where AI agents do most work, and 6% plan to hire more
    staff to scale (the source gives the 14% and 6% figures straight after the law-firm figure without restating
    the base); the survey''s head of professional services argues mid-level professionals should become ''workflow
    engineers'' (LAW360-GA-2026). An ILTA respondent said GenAI will compress the document review, research and
    drafting that has powered the associate pyramid (ILTA-TECHSURVEY-2026).'
  outcomes:
  - lever: cost
    description: Share of large law firms expecting AI to affect professional staffing models in the next two years
      doubled year on year
    figure: 36%
    measures: large firms expecting AI to affect their professional staffing models in the following two years (Citi/Hildebrandt
      report, as summarised by Law360 Pulse)
    provenance: independent
    source_ref: LAW360-CITI-2025
  - lever: capacity
    description: Law firms planning flat headcount with AI-driven efficiency versus agents doing most work versus
      hiring more
    figure: 74%; 14%; 6%
    measures: law firm respondents (74%; base for 14% and 6% not restated) in a Feb 12-25, 2026 General Assembly
      survey of 258 leaders at consulting, accounting and legal firms in the UK and US (law-firm subset size not
      stated)
    provenance: vendor-published
    source_ref: LAW360-GA-2026
  prerequisites:
  - Data on matter economics and staffing by level (observation, analyst; not in a source)
  - Agreement on a business model (billable, value-based or frontier-model scenarios) before the talent model can
    be set (TRI-LDEV-2026)
  risks_and_guardrails:
  - Designing a talent model for an unknown business model is difficult; the timing of changes is the unknown (TRI-LDEV-2026)
  - A veteran ILTA respondent noted earlier 'transformative' innovations produced minimal change (ILTA-TECHSURVEY-2026)
  human_checkpoints:
  - Partners and management committees decide structure (observation, analyst; not in a source).
  role_evolution: A Major Lindsey & Africa executive said firms will likely add roles such as data scientists and
    technologists and focus more on strengthening the equity partnership, and TruLegal's founder named product managers,
    pricing experts, project managers and AI governance practitioners as increasingly prominent roles (LAW360-CITI-2025).
    Firms anticipate extra headcount in IT, innovation, security, training, knowledge management and data science
    (ILTA-TECHSURVEY-2026).
  evidence_grade: C
  sources:
  - ref: LAW360-CITI-2025
    title: Law Firms' Junior Roles At Risk From AI, Report Says (on the Citi Global Wealth at Work and Hildebrandt
      Consulting report)
    publisher: Law360 Pulse
    type: press
    url: https://www.law360.com/articles/2422148/law-firms-junior-roles-at-risk-from-ai-report-says
    date: '2025-12-15'
    access: full
    locator: paragraphs 4-8 (leverage expectations, roles)
  - ref: LAW360-GA-2026
    title: AI Set To Transform Junior Lawyer Roles, Survey Finds (on the General Assembly survey of 258 leaders)
    publisher: Law360 UK
    type: press
    url: https://www.law360.com/articles/2456965/ai-set-to-transform-junior-lawyer-roles-survey-finds
    date: '2026-03-24'
    access: full
    locator: paragraphs 1-12 (survey results)
  - ref: ILTA-TECHSURVEY-2026
    title: ILTA Technology Survey 2026 Executive Summary
    publisher: ILTA
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: section 'The Curtain Rises on Enterprise-Scale Adoption'
  - ref: TRI-LDEV-2026
    title: Rethinking lawyer development in future AI-enabled law firms
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/lawyer-development-ai-enabled-law-firms
    date: '2026-04-16'
    access: full
    locator: sections 'Planning around 3 law firm business models' and 'Aligning the talent model'
  last_reviewed: '2026-10-19'
  notes: Law360 defines lawyer leverage as the ratio of equity partners to all other lawyers, which looks inverted
    relative to the usual definition; the source's wording is reproduced. General Assembly is an AI training provider
    with a commercial interest in the finding.
- id: professional-services-talent-learning-11
  title: AI-led virtual screening interview replaces the long graduate application form (Mishcon de Reya trial of
    Bright Apply)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - transaction-processing
  - client-interaction
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: Application forms limit what candidates can say, and recruiters must make early screening decisions from
    thin information (MISHCON-BRIGHT-2025).
  solution: For its 2026 graduate season Mishcon de Reya is trialling Bright Apply, an AI screening tool from Bright
    Network. It uses information from an applicant's application to start a conversation, producing a tailored,
    untimed virtual interview with practice elements in place of a long form. Each transcript is reviewed by the
    firm's team, and the Early Careers team continues to make all screening decisions (MISHCON-BRIGHT-2025).
  outcomes:
  - lever: experience
    description: Almost three quarters of students rated the experience 4 or 5 out of 5, and 93% of student responses
      said the AI chat responses felt personalised and relevant
    figure: almost 75%; 93%
    measures: student ratings and responses in an anonymous survey (who ran it and the number of respondents are
      not stated)
    provenance: self-reported
    source_ref: MISHCON-BRIGHT-2025
  prerequisites:
  - A tool built for graduate screening (Bright Network's Bright Apply, first use at Mishcon and the tool's debut)
    (MISHCON-BRIGHT-2025)
  - Recruiter capacity to read every transcript (MISHCON-BRIGHT-2025)
  risks_and_guardrails:
  - The UK ICO audited AI recruitment tools and made almost 300 recommendations after finding tools that let recruiters
    filter by protected characteristics, inferred gender and ethnicity from names, or kept data indefinitely (ICO-RECRUIT-2024)
  - New York City Local Law 144 requires a bias audit within a year of use, a public summary and notices for automated
    employment decision tools (NYC-AEDT-2023)
  - EU AI Act lists CV-sorting recruitment software as high-risk, with obligations applying from 2 December 2027
    (EC-AIACT-2026)
  human_checkpoints:
  - Firm team reviews each transcript and makes all screening decisions (MISHCON-BRIGHT-2025)
  role_evolution: Early-careers recruiters move from reading forms to reading interview transcripts (MISHCON-BRIGHT-2025).
  evidence_grade: B
  sources:
  - ref: MISHCON-BRIGHT-2025
    title: Mishcon de Reya trials 'Bright Apply' to deliver fairer, more efficient hiring
    publisher: Mishcon de Reya
    type: firm
    url: https://www.mishcon.com/news/mishcon-de-reya-trials-bright-apply-to-deliver-fairer-more-efficient-hiring
    date: '2025-12-01'
    access: full
    locator: paragraphs 1-4 and quotes (trial description, survey figures)
  - ref: ICO-RECRUIT-2024
    title: ICO intervention into AI recruitment tools leads to better data protection for job seekers
    publisher: Information Commissioner's Office (UK)
    type: regulator
    url: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/11/ico-intervention-into-ai-recruitment-tools-leads-to-better-data-protection-for-job-seekers/
    date: 2024-11
    access: full
    locator: section 'About the audits'
  - ref: NYC-AEDT-2023
    title: Automated Employment Decision Tools (AEDT), Local Law 144 of 2021
    publisher: NYC Department of Consumer and Worker Protection
    type: regulator
    url: https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page
    date: '2023-07-05'
    access: full
    locator: first paragraph
  - ref: EC-AIACT-2026
    title: AI Act (regulatory framework page)
    publisher: European Commission
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: list of high-risk use cases; timeline section
  last_reviewed: '2026-10-19'
  notes: Graded B (named firm, live trial) but the only outcome figures come from a firm and vendor press release
    about candidate experience, not selection quality, fairness or time saved. No bias or validity data were published.
    A search summary reported that Mishcon said AI scores would not be used for decisions; that line is not on the
    page I read, which says the Early Careers team make all screening decisions.
- id: professional-services-talent-learning-12
  title: Assessing how candidates work with an AI tool in final-round interviews (McKinsey, as reported)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: Graduate selection tests built for unaided analysis do not show whether a candidate can direct and check
    an AI tool, which juniors will do from day one (GUARDIAN-MCKINSEY-2026).
  solution: McKinsey is reported to be including an 'AI interview' in some final rounds. According to CaseBasix,
    a US firm that helps candidates apply, finalists in select US final rounds complete practical consulting tasks
    with McKinsey's internal tool Lilli, prompting it, reviewing its output and applying judgment to produce a structured
    answer. The focus is said to be collaboration and reasoning, not technical AI skill. The Financial Times first
    reported use of Lilli with business school graduates (GUARDIAN-MCKINSEY-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: any validity, pass-rate or fairness data (none published)
    provenance: self-reported
    source_ref: GUARDIAN-MCKINSEY-2026
  prerequisites:
  - An internal AI tool able to be used safely in assessment (Lilli) (GUARDIAN-MCKINSEY-2026)
  - Assessors trained to judge how candidates question and verify AI output (observation, analyst; not in a source)
  risks_and_guardrails:
  - McKinsey declined to comment; the description comes from a candidate-preparation firm (GUARDIAN-MCKINSEY-2026)
  - Whether employment AI rules (NYC Local Law 144, the EU AI Act) apply to an AI-assisted exercise that human assessors
    score is not addressed in the sources I read (NYC-AEDT-2023; EC-AIACT-2026)
  human_checkpoints:
  - The AI interview sits alongside problem-solving and personal-impact assessments (GUARDIAN-MCKINSEY-2026)
  role_evolution: Candidates are expected to treat the AI like a junior team member, communicating their reasoning
    clearly (GUARDIAN-MCKINSEY-2026). McKinsey's chief executive has said it has 20,000 agents working alongside
    40,000 staff (GUARDIAN-MCKINSEY-2026).
  evidence_grade: C
  sources:
  - ref: GUARDIAN-MCKINSEY-2026
    title: McKinsey asks graduates to use AI chatbot in recruitment process
    publisher: The Guardian
    type: press
    url: https://www.theguardian.com/business/2026/jan/14/mckinsey-graduates-ai-chatbot-recruitment-consultancy
    date: '2026-01-14'
    access: full
    locator: paragraphs 1-9
  last_reviewed: '2026-10-19'
  notes: 'Graded C: relayed by a candidate-coaching firm, McKinsey declined to comment. Search-only (not opened):
    a December 2025 report described it as a pilot mostly for Business Analyst candidates with broader use expected
    in spring or summer 2026; a headline in The Lawyer says A&O Shearman tests graduates on AI by asking how they
    would write accurate prompts. Neither is used for grading.'
- id: professional-services-talent-learning-13
  title: Screen for curiosity, judgment and human skills rather than AI-tool familiarity (Fredrikson & Byron; ambiguity-based
    interviews)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Because AI makes surface competence easy to show, traditional hiring proxies such as GPA, school and
    tool knowledge say less about who will perform when the answer is unclear (TRI-TAAP2030-2026; TRI-ONBOARDING-2026).
  solution: Fredrikson & Byron's chief legal operations officer says the firm prioritises curiosity, openness and
    human skills over a checklist of AI tools when recruiting, and builds its associate development around AI fluency,
    faster development of legal judgment and human skills (TRI-LDEV-2026). A TRI series on the 2030 accounting firm
    recommends giving candidates an ambiguous problem and watching how they work through it, rather than interviewing
    only for what they know (TRI-TAAP2030-2026). Ascend's CEO says firms will want to hire young people who are
    curious, hardworking 'sponges' (ATODAY-ASCEND-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: hire quality, retention or performance data (none published)
    provenance: self-reported
    source_ref: TRI-LDEV-2026
  prerequisites:
  - Interviewers trained to run and score open-ended exercises (TRI-TAAP2030-2026)
  risks_and_guardrails:
  - Where AI is used to screen candidates, employment AI rules can apply (ICO-RECRUIT-2024; NYC-AEDT-2023; EC-AIACT-2026)
  - Fredrikson says the judgment-acceleration work 'has not fully happened yet' and a formal curriculum on supervising
    AI output is a stated goal for the year ahead (TRI-LDEV-2026)
  human_checkpoints:
  - Interviewers judge how a candidate reasons, not whether the answer is right (TRI-TAAP2030-2026)
  role_evolution: The talent pool may widen beyond high-GPA accounting graduates to candidates with problem-solving
    histories (TRI-TAAP2030-2026).
  evidence_grade: B
  sources:
  - ref: TRI-LDEV-2026
    title: Rethinking lawyer development in future AI-enabled law firms
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/lawyer-development-ai-enabled-law-firms
    date: '2026-04-16'
    access: full
    locator: section 'Aligning the talent model to the future business model'
  - ref: TRI-TAAP2030-2026
    title: 'The tax, accounting & audit firm of 2030: Building the people of tomorrow''s tax firm (Jody Padar)'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/tax-audit-accounting-firm-of-2030-building-people-for-tomorrow
    date: '2026-10-16'
    access: full
    locator: section 'Firms have to hire for figure-it-out ability'
  - ref: ATODAY-ASCEND-2026
    title: The 'AI Native' firm (On the Air podcast with Ascend CEO David Wurtzbacher)
    publisher: Accounting Today
    type: podcast
    url: https://www.accountingtoday.com/podcast/the-ai-native-firm
    date: '2026-10-19'
    access: full
    locator: answer on hiring young people (curious, hardworking sponges)
  - ref: ICO-RECRUIT-2024
    title: ICO intervention into AI recruitment tools leads to better data protection for job seekers
    publisher: Information Commissioner's Office (UK)
    type: regulator
    url: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/11/ico-intervention-into-ai-recruitment-tools-leads-to-better-data-protection-for-job-seekers/
    date: 2024-11
    access: full
    locator: section 'About the audits'
  last_reviewed: '2026-10-19'
  notes: Graded B on one named firm's stated recruiting priority (Fredrikson), with no outcome data. The interview-design
    advice is from a consultant (Dr Rachel Anevski, quoted in a TRI series) and is an idea.
- id: professional-services-talent-learning-14
  title: Teach 'power' and 'durable' human skills deliberately alongside AI fluency
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: As AI raises the baseline for drafting and analysis, firms see differentiation moving to client confidence,
    empathy, coachability and judgment, which juniors previously absorbed slowly on the job (TRI-ONBOARDING-2026;
    BLAW-ASSOCIATES-2026).
  solution: A firm rendered in the source as Winston Taylor developed a list of 12 'durable' skills (including work
    ethic, empathy and coachability) about a year ago and teaches them, in part through a partnership with Chicago's
    Steppenwolf Theater Company, and hosts 30 incoming first-year law students for the training without recruiting
    aims. A firm rendered as Sheppard LLP hired an AI-mindset trainer, who presented to about 50 senior leaders
    in May and whose exercises were due to roll out more broadly in the fall (BLAW-ASSOCIATES-2026). Duane Morris
    stresses client confidence and business fluency (TRI-ONBOARDING-2026). PwC UK added debating sessions and KPMG
    UK dedicated coaching on workplace behaviours (CITYAM-BIG4TRAINING-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: skills, retention or client outcomes of these programmes (none published)
    provenance: self-reported
    source_ref: BLAW-ASSOCIATES-2026
  prerequisites:
  - A professional-development function with budget for external coaches and partners (BLAW-ASSOCIATES-2026)
  risks_and_guardrails:
  - Associates get mixed messages from leadership, partners and clients about whether to use AI (TRI-CLOSEGAP-2026)
  human_checkpoints:
  - Actors and coaches give live feedback on scenes (BLAW-ASSOCIATES-2026)
  role_evolution: Professional-development staff become designers of judgment-building experiences (TRI-CLOSEGAP-2026);
    associates are coached on empathy and reading a room (BLAW-ASSOCIATES-2026).
  evidence_grade: B
  sources:
  - ref: BLAW-ASSOCIATES-2026
    title: What Does It Take to Get Big Law Associates Excited About AI? (Big Law Business column)
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/what-does-it-take-to-get-big-law-associates-excited-about-ai
    date: '2026-07-30'
    access: full
    locator: paragraphs on Sheppard LLP and Winston Taylor
  - ref: TRI-ONBOARDING-2026
    title: Law firms need to redesign new attorney onboarding for the AI era
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding
    date: '2026-10-12'
    access: full
    locator: section 'Raising the bar for power skills'
  - ref: CITYAM-BIG4TRAINING-2026
    title: How AI is forcing the Big Four to rethink graduate training (Beyond The Billable column)
    publisher: City AM
    type: press
    url: https://www.cityam.com/?p=2459320
    date: '2026-09-23'
    access: full
    locator: section 'The human touch'
  - ref: TRI-CLOSEGAP-2026
    title: 4 ways law firms can close gaps in legal judgment & professional identity
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/closing-legal-judgment-and-professional-identity-gaps
    date: '2026-09-10'
    access: full
    locator: section 'Why associates are facing an identity crisis'
  last_reviewed: '2026-10-19'
  notes: Firm names are reproduced as they appear in the Bloomberg Law text I retrieved ('Winston Taylor', 'Sheppard
    LLP'); they look like possible mirror or editing artefacts and should be checked against the original column
    before use. No outcome data anywhere in this cluster.
- id: professional-services-talent-learning-15
  title: AI use built into performance objectives and tracked through tool data (KPMG; PwC US partner expectations)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: personal-assistant
  maturity: in-production
  problem: Firms that have invested in AI cannot capture value unless staff use it, and leaders lack a view of who
    is using which tools (BLOOMBERG-KPMG-2025).
  solution: KPMG tracks how staff use AI using data from tools such as Microsoft Copilot, according to its global
    AI workforce lead, and will assess staff on how well they met the firm's AI objectives in their 2026 performance
    reviews. Everyone, including juniors, is asked at year end what they will do to bring AI into their work. The
    firm says the monitoring is not for policing but to ensure everyone uses the tools and to measure the value
    of the investment (BLOOMBERG-KPMG-2025). PwC's US CEO told the Financial Times that partners who resist AI would
    not last, that no one gets a free pass, and that senior staff not 'paranoid about being AI-first' would likely
    be replaced (CPAPA-PWC-2026).
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: adoption rates, rating distributions or value realised (none published)
    provenance: self-reported
    source_ref: BLOOMBERG-KPMG-2025
  prerequisites:
  - Usage telemetry from AI tools such as Copilot (BLOOMBERG-KPMG-2025)
  - Managers able to set AI-related objectives for each role (BLOOMBERG-KPMG-2025)
  risks_and_guardrails:
  - Associates may get mixed signals when partners or clients discourage AI while leadership expects it (TRI-CLOSEGAP-2026)
  - The billable hour was long a stand-in for a lawyer's worth, and AI removes that proof point without a replacement
    metric (TRI-CLOSEGAP-2026)
  - EU AI Act lists AI for employment and management of workers as high-risk, with obligations from 2 December 2027;
    whether usage monitoring falls within that is not addressed in the sources I read (EC-AIACT-2026)
  human_checkpoints:
  - Year-end objective setting and review by managers (BLOOMBERG-KPMG-2025)
  role_evolution: AI use becomes a condition of progression for juniors and partners alike (BLOOMBERG-KPMG-2025;
    CPAPA-PWC-2026).
  evidence_grade: B
  sources:
  - ref: BLOOMBERG-KPMG-2025
    title: KPMG Staff to Be Rated on AI Usage in Yearly Performance Reviews
    publisher: Bloomberg
    type: press
    url: https://news.bgov.com/health-law-and-business/kpmg-staff-to-be-rated-on-ai-usage-in-yearly-performance-reviews
    date: '2025-10-31'
    access: full
    locator: paragraphs 1-8 (tracking, 2026 reviews, quotes)
  - ref: CPAPA-PWC-2026
    title: PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm' (reporting the Financial Times)
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/
    date: '2026-03-25'
    access: full
    locator: paragraphs 1-4 (partners, no free pass)
  - ref: TRI-CLOSEGAP-2026
    title: 4 ways law firms can close gaps in legal judgment & professional identity
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/closing-legal-judgment-and-professional-identity-gaps
    date: '2026-09-10'
    access: full
    locator: section 'Why associates are facing an identity crisis'
  - ref: EC-AIACT-2026
    title: AI Act (regulatory framework page)
    publisher: European Commission
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: 'high-risk list: employment and management of workers'
  last_reviewed: '2026-10-19'
  notes: Tracking is in use; the rating in reviews applies from the 2026 cycle. PwC's statements are CEO interview
    remarks relayed by a trade outlet quoting the FT, not a published policy.
- id: professional-services-talent-learning-16
  title: Firmwide bonus pool tied to staff Copilot prompt volume (Shoosmiths)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: A general-purpose AI tool delivers little unless many people use it, and a firm wants to encourage everyday
    use without mandating it (LEGALCHEEK-SHOOSMITHS-2025).
  solution: Shoosmiths set a target of one million Microsoft Copilot prompts as part of its multi-million 'collegiate'
    bonus scheme. Reaching it unlocks an additional GBP 1 million for the firmwide bonus pool, payable in the new
    financial year if the firm also meets its core financial metric. The firm says Copilot is used to tidy emails,
    summarise documents, generate ideas, support research and manage meetings, and is not used for work requiring
    legal training or expertise (LEGALCHEEK-SHOOSMITHS-2025).
  outcomes:
  - lever: capacity
    description: The firm reached one million Copilot prompts more than four months ahead of schedule, unlocking
      GBP 1 million for the bonus pool
    figure: 1,000,000 prompts; more than 4 months early; GBP 1m
    measures: cumulative Microsoft Copilot prompts by staff against a firmwide target of one million (as reported;
      the period and eligible population are not stated in the article)
    provenance: self-reported
    source_ref: LEGALCHEEK-SHOOSMITHS-2025
  prerequisites:
  - Firmwide Copilot licences and prompt telemetry (LEGALCHEEK-SHOOSMITHS-2025)
  - A bonus scheme open to all staff (LEGALCHEEK-SHOOSMITHS-2025)
  risks_and_guardrails:
  - The metric counts prompts, which measures use rather than quality or value (observation, analyst)
  - Hill Dickinson restricted general access to several AI tools after a surge in lawyer and staff usage, a counter-example
    in the same article (LEGALCHEEK-SHOOSMITHS-2025)
  - The firm says the tool is for non-legal tasks only (LEGALCHEEK-SHOOSMITHS-2025)
  human_checkpoints:
  - The payout is conditional on a core financial metric (LEGALCHEEK-SHOOSMITHS-2025)
  role_evolution: The CEO says AI frees people to focus on human-to-human client work (LEGALCHEEK-SHOOSMITHS-2025).
  evidence_grade: A
  sources:
  - ref: LEGALCHEEK-SHOOSMITHS-2025
    title: Shoosmiths drops £1 million into bonus pot after staff hit AI prompt target
    publisher: Legal Cheek
    type: press
    url: https://www.legalcheek.com/2025/12/shoosmiths-drops-1-million-into-bonus-pot-after-staff-hit-ai-prompt-target/
    date: '2025-12-17'
    access: full
    locator: paragraphs 1-6 (target reached, scheme, use cases)
  last_reviewed: '2026-10-19'
  notes: 'Grade A because the firm reports a tracked metric against a stated target, but the metric is activity
    (prompt volume), not talent or quality outcomes. Conflict: the article says the scheme is open to all staff;
    a search-only summary of the April 2025 announcement said partners and business services directors were excluded;
    I could not open the original. Shoosmiths'' own press page URL returned 404.'
- id: professional-services-talent-learning-17
  title: AI to compile performance-review summaries, analyse written feedback and check evaluations for bias
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - data-reporting
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: 'Associate evaluations take a great deal of time, and feedback often arrives stale: 44% of surveyed firms
    took more than four weeks to deliver feedback after evaluations were completed (CANLAW-NALP-2025).'
  solution: Of 106 US and Canadian law firms surveyed by the NALP Foundation in July and August, 31% had integrated
    AI into associate performance evaluations. Most of those used it to generate performance summaries or analyse
    written feedback, and some for assessing bias. Many other firms are exploring AI for long-term performance tracking
    and for training and guidance during review discussions (CANLAW-NALP-2025; NALP-BULLETIN-2026).
  outcomes:
  - lever: capacity
    description: 31% of surveyed firms had integrated AI into performance evaluation; 69% had not
    figure: 31%
    measures: share of 106 US and Canadian law firms in the NALP Foundation survey (Jul-Aug 2025) that reported
      integrating AI into evaluations
    provenance: independent
    source_ref: CANLAW-NALP-2025
  prerequisites:
  - 'Structured evaluation inputs: supervisors'' qualitative comments (100% of respondents), quantitative metrics
    (96%), self-evaluations (93%) (CANLAW-NALP-2025)'
  risks_and_guardrails:
  - The EU AI Act lists AI tools for employment and management of workers as high-risk, with obligations from 2
    December 2027 (EC-AIACT-2026)
  - NYC Local Law 144 covers automated employment decision tools used for employees and candidates, requiring bias
    audits and notices (NYC-AEDT-2023)
  human_checkpoints:
  - Supervising lawyers write the qualitative comments; AI helps compile and analyse them (CANLAW-NALP-2025; NALP-BULLETIN-2026)
  role_evolution: Evaluators keep the judgment role; the NALP Foundation says firms want to use evaluations more
    effectively for associate development and talent management (CANLAW-NALP-2025).
  evidence_grade: C
  sources:
  - ref: CANLAW-NALP-2025
    title: 'Most law firm associate evaluations don''t use AI or give speedy feedback: survey (on the NALP Foundation
      performance evaluation study)'
    publisher: Canadian Lawyer
    type: press
    url: https://www.canadianlawyermag.com/resources/practice-management/most-law-firm-associate-evaluations-dont-use-ai-or-give-speedy-feedback-survey/393386
    date: '2025-11-18'
    access: full
    locator: paragraphs 1-3 and feedback-timing paragraph
  - ref: NALP-BULLETIN-2026
    title: 'NALP Foundation: Putting Performance Evaluations Through Their Paces: Problems and Potential'
    publisher: NALP Bulletin
    type: professional-body
    url: https://nalpbulletin.mydigitalpublication.com/articles/nalp-foundation-putting-performance-evaluations-through-their-paces-problems-and-potential
    date: 2026-02
    access: full
    locator: section 'Role of AI'
  - ref: EC-AIACT-2026
    title: AI Act (regulatory framework page)
    publisher: European Commission
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: list of high-risk use cases
  - ref: NYC-AEDT-2023
    title: Automated Employment Decision Tools (AEDT), Local Law 144 of 2021
    publisher: NYC Department of Consumer and Worker Protection
    type: regulator
    url: https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page
    date: '2023-07-05'
    access: full
    locator: first paragraph
  last_reviewed: '2026-10-19'
  notes: Survey evidence only; no firm is named and no error, bias or time-saved data were reported. The NALP Foundation
    full report is paywalled.
- id: professional-services-talent-learning-18
  title: Firmwide AI training and certification at network scale (PwC, Accenture, Deloitte with Anthropic)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - coordination-scheduling
  - document-production
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Large firms need hundreds of thousands of people to use AI tools consistently and safely, and ad hoc
    learning does not scale (ATODAY-PWC-2026; CIODIVE-ACCENTURE-2025).
  solution: PwC says over 330,000 people have taken AI training and it is rolling out AI-powered learning platforms
    alongside USD 3 billion invested network-wide in AI and other capabilities (ATODAY-PWC-2026). Accenture's CEO
    said over 550,000 employees are trained in generative AI fundamentals and that AI and data staff nearly doubled
    to 77,000 in two years (CIODIVE-ACCENTURE-2025). Deloitte and Anthropic announced a certification programme
    to train and certify 15,000 Deloitte professionals on Claude, tied to a Claude Center of Excellence (ANTHROPIC-DELOITTE-2025).
  outcomes:
  - lever: capacity
    description: Over 330,000 people at PwC have taken AI training
    figure: 330,000+
    measures: people who have taken AI training at PwC (as stated; the denominator is not given)
    provenance: self-reported
    source_ref: ATODAY-PWC-2026
  - lever: capacity
    description: More than 550,000 Accenture people trained in generative AI fundamentals; AI and data professionals
      reached 77,000
    figure: 550,000+; 77,000
    measures: employees trained in generative AI fundamentals; AI and data professionals (CEO statements on the
      Q4 FY25 call, relayed by CIO Dive)
    provenance: self-reported
    source_ref: CIODIVE-ACCENTURE-2025
  - lever: capacity
    description: Deloitte and Anthropic plan to certify 15,000 Deloitte professionals on Claude
    figure: 15,000
    measures: professionals Deloitte and Anthropic say they are co-creating a certification programme to train and
      certify
    provenance: vendor-published
    source_ref: ANTHROPIC-DELOITTE-2025
  prerequisites:
  - A platform deal and learning platform (ANTHROPIC-DELOITTE-2025; ATODAY-PWC-2026)
  - A centre of excellence or specialists to support implementation (ANTHROPIC-DELOITTE-2025)
  risks_and_guardrails:
  - Most AI training teaches what tools do and rarely when to trust, verify or override output (TR-FOP-2026, 'Strategy-execution
    gap')
  - 43% of professionals with a strategy-execution gap say people are not equipped or trained to work in the intended
    way (TR-FOP-2026)
  - Training before access is required by 11% of law firms under 50 lawyers but 72% of firms over 700 (ILTA-TECHSURVEY-2026)
  - Karbon's survey of about 600 accounting professionals finds fewer than half of firms invest in AI training and
    21% have an AI policy or strategy (KARBON-SOAI-2026)
  human_checkpoints:
  - Certified practitioners lead implementations (ANTHROPIC-DELOITTE-2025)
  role_evolution: A tier of certified AI practitioners emerges inside the firm to lead internal and client implementations
    (ANTHROPIC-DELOITTE-2025).
  evidence_grade: B
  sources:
  - ref: ATODAY-PWC-2026
    title: PwC grows 2026 global revenue to $60.2B
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/pwc-grows-2026-global-revenue-to-60-2b
    date: '2026-10-19'
    access: full
    locator: paragraph on investment and learning platforms
  - ref: CIODIVE-ACCENTURE-2025
    title: Accenture completes 'reinvention' as generative AI revenues roll in
    publisher: CIO Dive
    type: press
    url: https://www.ciodive.com/news/accenture-generative-ai-revenue-skills-training-data-modernization/761161/
    date: '2025-09-25'
    access: full
    locator: paragraph on 77,000 AI and data professionals and 550,000 trained
  - ref: ANTHROPIC-DELOITTE-2025
    title: Deloitte will make Claude available to 470,000 people across its global network
    publisher: Anthropic
    type: vendor
    url: https://www.anthropic.com/news/deloitte-anthropic-partnership
    date: '2025-10-06'
    access: full
    locator: paragraphs 1-2
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: sections on the strategy-execution gap
  - ref: ILTA-TECHSURVEY-2026
    title: ILTA Technology Survey 2026 Executive Summary
    publisher: ILTA
    type: survey
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: policy table (training required before use)
  - ref: KARBON-SOAI-2026
    title: Karbon State of AI in Accounting 2026 Report shows strategy, training, and governance unlock AI's full
      potential
    publisher: Karbon
    type: vendor
    url: https://karbonhq.com/resources/state-of-ai-accounting-2026/
    date: '2026-01-23'
    access: full
    locator: paragraphs 1-2
  last_reviewed: '2026-10-19'
  notes: Counts of people trained measure activity, not skill or behaviour change, and none of the firms publishes
    an effect measure. Accenture figures are relayed by trade press from the earnings call; the call transcript
    and release body were not read. PwC's figure appears in an Accounting Today summary (the page notes its introductory
    bullets were AI-created with editorial review). The Deloitte item is an announcement.
- id: professional-services-talent-learning-19
  title: Talent strategy of upskilling, with compressed-timeline exits where reskilling is not viable (Accenture)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: workflow-automation
  maturity: in-production
  problem: Skills a services firm needs change faster than it can retrain everyone, and the firm's structure and
    measures of performance may not match its AI strategy (FORTUNE-ACCENTURE-2025).
  solution: 'Accenture announced a six-month business optimisation programme with up to USD 865 million of related
    charges and a three-part talent strategy: invest in upskilling, exit people on a compressed timeline where reskilling
    is not a viable path for the skills needed, and drive operating efficiencies. Its CEO said savings above USD
    1 billion are expected, to be reinvested, and that headcount is still expected to rise overall (FORTUNE-ACCENTURE-2025).'
  outcomes:
  - lever: cost
    description: Accenture expects more than USD 1 billion of savings from the optimisation programme, with up to
      USD 865 million of related charges
    figure: USD 1bn+ savings; up to USD 865m charges
    measures: expected savings and charges for the six-month business optimisation programme (CEO statements, relayed
      by Fortune)
    provenance: self-reported
    source_ref: FORTUNE-ACCENTURE-2025
  prerequisites:
  - Skills taxonomy and a view of which skills the firm needs (FORTUNE-ACCENTURE-2025)
  - Training capacity for the 'upskilling' leg (CIODIVE-ACCENTURE-2025)
  risks_and_guardrails:
  - The CEO described emotional and strategic difficulty in the departures of senior team leaders and the restructuring
    (FORTUNE-ACCENTURE-2025)
  - Selection criteria for exits were not published (observation, analyst)
  human_checkpoints:
  - None stated.
  role_evolution: Employees are called 'reinventors'; leaders must build new skills to shape AI-enabled business
    strategy (FORTUNE-ACCENTURE-2025).
  evidence_grade: B
  sources:
  - ref: FORTUNE-ACCENTURE-2025
    title: Accenture's $865 million reinvention includes saying goodbye to people without the right AI skills
    publisher: Fortune
    type: press
    url: https://www.fortune.com/2025/09/27/accenture-865-million-reinvention-exiting-people-ai-skills
    date: '2025-09-27'
    access: full
    locator: paragraphs 1-2 and Sweet interview sections
  - ref: CIODIVE-ACCENTURE-2025
    title: Accenture completes 'reinvention' as generative AI revenues roll in
    publisher: CIO Dive
    type: press
    url: https://www.ciodive.com/news/accenture-generative-ai-revenue-skills-training-data-modernization/761161/
    date: '2025-09-25'
    access: full
    locator: paragraph on AI and data professionals
  last_reviewed: '2026-10-19'
  notes: Figures are expected values from a company announcement; no outcome data on retraining success or exits.
    Search-summary figures on headcount changes and a second charge breakdown are not used.
- id: professional-services-talent-learning-20
  title: Re-scoping support-function roles around AI (Clifford Chance London, Baker McKenzie)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - transaction-processing
  - document-production
  pattern: other
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Finance, HR, IT, marketing and secretarial support teams carry routine work that AI and hub operations
    can take over (CITYAM-CC-2025; LEGALCHEEK-BAKERMCK-2026).
  solution: Clifford Chance told London business-services staff that greater use of AI and reduced demand for some
    services meant jobs had to go, with work also done in hubs such as Poland and India (CITYAM-CC-2025). Baker
    McKenzie's spokesperson said a review of its business professionals functions, rethinking how it works including
    through AI, means some roles will likely be phased out and others will evolve, subject to consultation (LEGALCHEEK-BAKERMCK-2026).
  outcomes:
  - lever: cost
    description: About 10% of Clifford Chance's 550 London business-services employees were set to lose their jobs
    figure: about 10% of 550
    measures: employees in the London business services team expected to be made redundant (Financial Times, relayed
      by City AM)
    provenance: independent
    source_ref: CITYAM-CC-2025
  prerequisites:
  - Consultation processes in applicable jurisdictions (LEGALCHEEK-BAKERMCK-2026)
  risks_and_guardrails:
  - Baker McKenzie's headcount is stated ambiguously by Legal Cheek ('less than 10% - or roughly 600 positions'),
    and the firm has not confirmed numbers (LEGALCHEEK-BAKERMCK-2026)
  - Employees were unhappy about timing of the announcement before Christmas (CITYAM-CC-2025)
  human_checkpoints:
  - Statutory consultation before decisions are final (LEGALCHEEK-BAKERMCK-2026)
  role_evolution: Some support roles disappear and others 'evolve' toward the roles that best serve clients (LEGALCHEEK-BAKERMCK-2026).
    Legal Cheek notes Freshfields and Irwin Mitchell have also announced paralegal layoffs (LEGALCHEEK-BAKERMCK-2026).
  evidence_grade: B
  sources:
  - ref: CITYAM-CC-2025
    title: Clifford Chance AI-driven redundancies hit London business service roles
    publisher: City AM
    type: press
    url: https://www.cityam.com/?p=2380354
    date: '2025-11-21'
    access: full
    locator: paragraphs 1-4
  - ref: LEGALCHEEK-BAKERMCK-2026
    title: Baker McKenzie to cut business services roles as AI use grows
    publisher: Legal Cheek
    type: press
    url: https://www.legalcheek.com/2026/02/baker-mckenzie-to-cut-business-services-roles-as-ai-use-grows/
    date: '2026-02-06'
    access: full
    locator: paragraphs 1-6
  last_reviewed: '2026-10-19'
  notes: Counted here because it is the support-staff side of the talent pyramid. Press-reported; the firms did
    not publish counts. Clifford Chance's cause is 'AI and reduced demand' per the FT; Baker McKenzie lists AI among
    several factors. A&O Shearman's reported cuts appear only in search summaries and are excluded.
- id: professional-services-talent-learning-21
  title: Embedded 'explain this change' assistants let interns and juniors learn from live work product (Ascend,
    as described by its CEO)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - research-synthesis
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: In the apprentice model juniors learn by doing returns and waiting for busy-season reviews, a slow loop
    that automation and outsourcing are cutting (ATODAY-ASCEND-2026).
  solution: Ascend, a private-equity-backed accounting-firm platform with a 30-person AI team, describes tools that
    sit inside the work product so a junior can ask what changed in a return, why the partner made a change and
    what else it affected. Its CEO says one firm reported its spring interns 'leveled themselves up' to staff level
    without extra training (ATODAY-ASCEND-2026).
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: measured time-to-competence (the intern claim is an anecdote)
    provenance: self-reported
    source_ref: ATODAY-ASCEND-2026
  prerequisites:
  - A 'closed loop' data environment capturing workflow traces, corrections and client preferences (ATODAY-ASCEND-2026)
  - Firm know-how extracted from partners' heads into the system (ATODAY-ASCEND-2026)
  risks_and_guardrails:
  - The host asks whether people who no longer do the returns can be as well informed about clients (ATODAY-ASCEND-2026)
  - A platform CEO's account of customer firms is a vendor claim (observation, analyst)
  human_checkpoints:
  - Partners' changes remain the source of truth the assistant explains (ATODAY-ASCEND-2026)
  role_evolution: The CEO expects careers to move toward trusted advisory and a re-generalised profession, with
    production work largely done by technology within about two years at Ascend (ATODAY-ASCEND-2026).
  evidence_grade: C
  sources:
  - ref: ATODAY-ASCEND-2026
    title: The 'AI Native' firm (On the Air podcast with Ascend CEO David Wurtzbacher)
    publisher: Accounting Today
    type: podcast
    url: https://www.accountingtoday.com/podcast/the-ai-native-firm
    date: '2026-10-19'
    access: full
    locator: answers on interns, career paths and closed loop (transcript)
  last_reviewed: '2026-10-19'
  notes: 'Grade C: a podcast transcript (AI-created, per the page) of a vendor-platform CEO. Date taken from page
    metadata (2026-10-19).'
- id: professional-services-talent-learning-22
  title: 'AI drafting assistant for practising patent lawyers: quality gain versus durable skill (pre-registered
    field experiment)'
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - document-production
  - expert-judgment
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: AI can raise the quality of professional work while stunting the expertise professionals would develop
    by doing it (NBER-AUTOR-2026).
  solution: In a pre-registered three-month randomised controlled trial, 133 practising patent lawyers at eleven
    US IP firms were given a custom AI patent-drafting assistant. Researchers measured performance with AI and then
    professional judgment afterwards without it, all scored by blinded expert patent attorneys (NBER-AUTOR-2026).
  outcomes:
  - lever: quality
    description: AI access raised the quality of benchmark patent drafting at 10 days and at 90 days, with larger
      gains among junior lawyers
    figure: +0.34 SD (p=0.03) at 10 days; +0.38 SD (p=0.01) at 90 days
    measures: standard-deviation difference in blinded expert scores between lawyers given AI access and controls
      on benchmark patent drafting tasks (133 lawyers, 11 firms)
    provenance: independent
    source_ref: NBER-AUTOR-2026
  - lever: quality
    description: On a no-AI redlining task after three months, treated lawyers outperformed controls overall, but
      the advantage was concentrated entirely among senior lawyers; juniors showed no average gain and their scores
      split into fewer mediocre and more poor and more good results
    figure: +0.32 SD (p=0.04) overall; +0.45 SD (p=0.02) seniors; juniors no average gain
    measures: standard-deviation difference in blinded expert scores on redlining an existing patent application
      without AI, treated versus control
    provenance: independent
    source_ref: NBER-AUTOR-2026
  prerequisites:
  - Foundational expertise appears to be a prerequisite for extracting durable skill from AI-assisted practice (NBER-AUTOR-2026)
  risks_and_guardrails:
  - 'Junior outcomes bifurcate: AI may act as a springboard for some juniors and a cushion for others (NBER-AUTOR-2026)'
  human_checkpoints:
  - Blinded expert attorneys scored all work (NBER-AUTOR-2026)
  role_evolution: Seniors retain a skill advantage after AI-assisted practice, while juniors' development is uneven,
    so supervision and unaided practice for juniors matter (NBER-AUTOR-2026).
  evidence_grade: A
  sources:
  - ref: NBER-AUTOR-2026
    title: Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent
      Drafting (NBER Working Paper 35720)
    publisher: NBER, via EconPapers (abstract page only)
    type: academic
    url: https://econpapers.repec.org/RePEc:nbr:nberwo:35720
    date: 2026-09
    access: full
    locator: Abstract
  last_reviewed: '2026-10-19'
  notes: Only the abstract page (EconPapers, dated 2026-09) was read; the full NBER PDF was unreachable from this
    environment (DNS). The abstract lists authors Autor, Rodchenko, Martin, Iscenko, Strand, Pearl and Ferere. The
    firms are not named in the abstract, and the task is patent drafting, a practice-specific substantive task,
    so the finding may not carry over to other junior tasks. Grade A rests on an independent, pre-registered trial.
- id: professional-services-talent-learning-23
  title: Vendor-run AI literacy academies and law-school programmes that move AI training upstream (Harvey Academy;
    Harvey and Legora law-school programmes)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - expert-judgment
  - document-production
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: New lawyers often arrive without much experience using AI, so the burden of training falls on employers
    and delays use on client work (NONBILLABLE-HARVEY-2026).
  solution: Harvey launched Harvey Academy in January 2026, a free hub for lawyers, legal operations teams, innovation
    leaders and law students with Intro to Harvey, a certification course 'AI for Legal Basics', hands-on 'Harvey
    in Practice' videos and digital certificates; guided onboarding and role-based modules for enterprise customers
    were announced as coming (HARVEY-ACADEMY-2026). Harvey says it works with more than 100 law schools, including
    Oxford, BPP and The University of Law, and BPP made it available to hundreds of masters and SQE2 students (NONBILLABLE-HARVEY-2026).
    Legora launched a US law-school programme with nine founding schools, including Stanford, Chicago, Cornell and
    UCLA, to train students and faculty on drafting, analysis and document review (NONBILLABLE-LEGORA-2026).
  outcomes:
  - lever: capacity
    description: Harvey reports working with more than 100 law schools; academic users run more than one million
      queries a week
    figure: 100+ schools; 1,000,000+ queries a week
    measures: law schools working with Harvey; queries run by academic users per week on the platform (vendor statements)
    provenance: vendor-published
    source_ref: NONBILLABLE-HARVEY-2026
  - lever: capacity
    description: Legora's programme started with nine founding US schools
    figure: 9 schools
    measures: founding schools in Legora's US law-school partnership programme (vendor statement)
    provenance: vendor-published
    source_ref: NONBILLABLE-LEGORA-2026
  prerequisites:
  - Law schools that choose to adopt the tools in curricula; policies vary (NONBILLABLE-HARVEY-2026; TRI-TEACHV-2026)
  risks_and_guardrails:
  - 'Vendor motive: partnerships are seen as a way to embed tools early (NONBILLABLE-LEGORA-2026)'
  - The University of Chicago Law School bans AI and devices in first-year core classes while offering Harvey in
    other courses (NONBILLABLE-HARVEY-2026)
  human_checkpoints:
  - None stated.
  role_evolution: Harvey's strategy chief expects firms to notice which law schools send associates who are ready
    to use AI, and recruiting to follow (NONBILLABLE-HARVEY-2026).
  evidence_grade: B
  sources:
  - ref: HARVEY-ACADEMY-2026
    title: 'Harvey Academy: Shaping the Future of Legal AI Literacy'
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/introducing-harvey-academy
    date: '2026-01-27'
    access: full
    locator: sections 'The Path From Curiosity to Confidence' and 'Deepen AI Skills'
  - ref: NONBILLABLE-HARVEY-2026
    title: Harvey passes 100 law schools as firms seek AI-ready recruits
    publisher: Non-Billable
    type: press
    url: https://www.nonbillable.co.uk/news/harvey-law-schools-ai-ready-recruits-juniors
    date: '2026-10-08'
    access: full
    locator: paragraphs 1-12
  - ref: NONBILLABLE-LEGORA-2026
    title: Legora takes AI platform into law schools as US expansion accelerates
    publisher: Non-Billable
    type: press
    url: https://www.nonbillable.co.uk/news/legora-us-law-school-programme
    date: '2026-03-25'
    access: full
    locator: paragraphs 1-6
  - ref: TRI-TEACHV-2026
    title: 'The missing skill in legal AI training: How to teach verification and judgment'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/teaching-verification-and-judgment
    date: '2026-09-01'
    access: full
    locator: paragraph on law-school policy variation
  last_reviewed: '2026-10-19'
  notes: 'In-house: Harvey Academy explicitly targets legal operations teams and innovation leaders as well as law
    firms (HARVEY-ACADEMY-2026); no named in-house deployment of it was found. All figures are vendor-published;
    BPP is the only named user quoted.'
- id: professional-services-talent-learning-24
  title: Teach verification explicitly with a portable checklist and structured exercises from day one (idea)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - review-assurance
  - expert-judgment
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Surveyed lawyers say juniors lack deep legal reasoning (72%) and verification and source-checking skills
    (69%), and only 2% believe AI mainly strengthens learning (LEXIS-MENTORSHIP-2026).
  solution: 'Idea discussed by practitioners: Barbri''s co-CEO proposes an aviation-style verification checklist
    built into a student''s first learning exercises and carried through the first employer until it becomes habit
    (TRI-TEACHV-2026). In LexisNexis''s survey, 52% support structured verification exercises that require juniors
    to check AI output against authoritative sources and 65% favour positioning AI as a ''thinking partner'' (LCN-LEXIS-2026).
    Fredrikson & Byron says a formal curriculum on supervising AI output is a goal for the year ahead (TRI-LDEV-2026).
    TR''s survey finds training rarely covers when to trust, verify or override (TR-FOP-2026).'
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: no deployment with outcome data found; survey support only (52% back structured verification exercises)
    provenance: independent
    source_ref: LCN-LEXIS-2026
  prerequisites:
  - Supervisors trained to evaluate AI-assisted work (TRI-TEACHV-2026)
  risks_and_guardrails:
  - Partners and senior associates may bypass juniors because AI makes polished work quickly, starving juniors of
    repetitions (TRI-TEACHV-2026)
  human_checkpoints:
  - Mentorship and supervision remain central; judgment needs friction, failure and guidance (TRI-TEACHV-2026; LCN-LEXIS-2026)
  role_evolution: Supervisors become coaches of verification; juniors defend AI-assisted work independently (TRI-TEACHV-2026).
  evidence_grade: D
  sources:
  - ref: TRI-TEACHV-2026
    title: 'The missing skill in legal AI training: How to teach verification and judgment'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/teaching-verification-and-judgment
    date: '2026-09-01'
    access: full
    locator: sections 'A checklist for verifying AI legal work' and 'Solving the junior lawyer learning paradox'
  - ref: LEXIS-MENTORSHIP-2026
    title: The mentorship gap (LexisNexis survey of 873 UK legal professionals, January 2026)
    publisher: LexisNexis UK
    type: vendor
    url: https://www.lexisnexis.co.uk/insights/the-mentorship-gap/index.html
    date: 2026-02
    access: full
    locator: survey headline figures
  - ref: LCN-LEXIS-2026
    title: New survey highlights shifts in junior lawyer learning as AI use grows
    publisher: LawCareers.Net
    type: press
    url: https://www.lawcareers.net/Explore/News/New-survey-highlights-shifts-in-junior-lawyer-learning-as-AI-use-grows-11022026
    date: '2026-02-11'
    access: full
    locator: paragraphs 1-4
  - ref: LEGALCHEEK-LEXIS-2026
    title: Research suggests AI is impacting junior lawyers' judgement
    publisher: Legal Cheek
    type: press
    url: https://www.legalcheek.com/2026/02/research-suggests-ai-is-impacting-junior-lawyers-judgement/
    date: '2026-02-10'
    access: full
    locator: paragraphs 1-6
  - ref: TRI-LDEV-2026
    title: Rethinking lawyer development in future AI-enabled law firms
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/lawyer-development-ai-enabled-law-firms
    date: '2026-04-16'
    access: full
    locator: Fredrikson tactics
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026'
    access: full
    locator: '''Strategy-execution gap'' section'
  last_reviewed: '2026-10-19'
  notes: Idea, not a deployment. The LexisNexis survey base is 873 UK legal professionals (LexisNexis page; other
    coverage says about 900) fielded in January 2026; in-house lawyers are among the voices quoted (Colt Technology
    Services; an unnamed in-house lawyer) - in-house.
- id: professional-services-talent-learning-25
  title: 'Milestone-based progression: define what a junior should do at 18-24 months and the evidence of readiness
    (idea)'
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types:
  - expert-judgment
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Time-served progression assumed judgment would emerge from repetition; if repetition goes, firms need
    another way to develop and certify readiness (TRI-TAAP2030-2026; TRI-DESIGNL-2026).
  solution: 'Idea discussed by practitioners: a consultant proposes progression built on milestones (what the person
    must know and be able to do, who teaches it, how often they practise, what evidence shows readiness), with early-career
    staff starting nearer where today''s seniors begin and learning through deliberate exposure, such as returns
    with buried issues, plausible-but-wrong AI recommendations and client meetings followed by debriefs (TRI-TAAP2030-2026).
    A TRI contributor writing as a law-firm leader argues leaders must act as systems design architects, since the
    link between repetitive work and judgment is inferred, not proven (TRI-DESIGNL-2026). Withum reports pushing
    tasks down from seniors to juniors (JOA-TRAINING-2026). General Assembly''s head of professional services suggests
    mid-level staff become workflow engineers (LAW360-GA-2026).'
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: no firm reporting a milestone-based model with outcome data was found
    provenance: independent
    source_ref: TRI-TAAP2030-2026
  prerequisites:
  - Competency definitions per role and level (TRI-TAAP2030-2026)
  - Feedback loops that turn experience into judgment (TRI-TAAP2030-2026)
  risks_and_guardrails:
  - Profession built around getting things right is uncomfortable with deliberate mistakes; learning needs safe,
    controlled settings (TRI-TAAP2030-2026)
  human_checkpoints:
  - Debrief questions after meetings and simulations ask what the person noticed, missed and would do differently
    (TRI-TAAP2030-2026)
  role_evolution: Entry-level staff start closer to senior-level work; mid-level staff may become designers of scalable
    workflows (TRI-TAAP2030-2026; LAW360-GA-2026).
  evidence_grade: D
  sources:
  - ref: TRI-TAAP2030-2026
    title: 'The tax, accounting & audit firm of 2030: Building the people of tomorrow''s tax firm (Jody Padar)'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/tax-audit-accounting-firm-of-2030-building-people-for-tomorrow
    date: '2026-10-16'
    access: full
    locator: sections 'Start training through experience' and 'The first 2 years need to look completely different'
  - ref: TRI-DESIGNL-2026
    title: 'Designing lawyers: Attorney growth in the age of AI-fueled practice'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/designing-lawyers-professional-growth
    date: '2026-05-11'
    access: full
    locator: sections 'A new model for learning' and 'Leadership in an AI age'
  - ref: JOA-TRAINING-2026
    title: How will accountants learn new skills when AI does the work?
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/
    date: '2026-03-01'
    access: full
    locator: section 'Upskilling at scale inside firms'
  - ref: LAW360-GA-2026
    title: AI Set To Transform Junior Lawyer Roles, Survey Finds (on the General Assembly survey of 258 leaders)
    publisher: Law360 UK
    type: press
    url: https://www.law360.com/articles/2456965/ai-set-to-transform-junior-lawyer-roles-survey-finds
    date: '2026-03-24'
    access: full
    locator: paragraph quoting Ash Khanna
  last_reviewed: '2026-10-19'
  notes: Idea. Discussed by a consultant, a law firm leader and a survey vendor; no firm has published a milestone-based
    progression model with data.
```

## 3. Module notes

### Processes and key steps (with work types)

1. **Workforce planning and intake sizing** (coordination-scheduling): decide graduate or first-year class size, the lateral share and support-staff levels. Use cases 08, 09, 10, 20.
2. **Sourcing and screening candidates** (transaction-processing, client-interaction): application forms, screening interviews. Use case 11.
3. **Selection and assessment** (expert-judgment): final-round exercises, criteria for hiring. Use cases 12, 13.
4. **Onboarding and foundational training** (document-production for curricula, coordination-scheduling): orientation, AI champions, certification, law-school pipeline. Use cases 01, 04, 07, 18, 23.
5. **On-the-job development and supervision** (review-assurance, expert-judgment): reviewing work, feedback loops, simulations. Use cases 05, 06, 22, 24.
6. **Performance management and incentives** (data-reporting, expert-judgment): objectives, evaluations, bonuses, billable credit. Use cases 15, 16, 17, 01.
7. **Career paths, rotations and leverage** (expert-judgment, coordination-scheduling): seats, progression, the pyramid. Use cases 02, 03, 10, 25.
8. **Workforce transition** (coordination-scheduling): reskilling, exits, support-role redesign. Use cases 19, 20.

### Common pain points

- The tasks that taught judgment are the ones AI absorbs first: reconciling, workpapers, routine drafting and review (KARBON-JUNIOR-2026; JOA-TRAINING-2026; TRI-ONBOARDING-2026).
- Training teaches tool operation, not when to trust, verify or override output (TR-FOP-2026, strategy-execution section; TRI-CLOSEGAP-2026).
- Partners are the least-prepared group: 55% of respondents in the General Assembly survey (74% among law firms) named partners as least prepared, and 54% of legal respondents said associates and analysts were most prepared (LAW360-GA-2026).
- Mixed messages: leadership tells associates to use AI while partners or clients say not to, and the billable hour no longer works as a proxy for a lawyer's worth (TRI-CLOSEGAP-2026).
- Evaluation feedback arrives late: 44% of surveyed firms took over four weeks after evaluations to deliver feedback (CANLAW-NALP-2025).
- Partners and senior associates may quietly bypass juniors because AI makes polished work fast, starving juniors of repetitions (TRI-TEACHV-2026).
- Clients are bringing more legal work in-house until the near-final stage, shrinking the junior work outside counsel sees (TRI-LDEV-2026) - in-house effect on the pyramid.

### Metrics and benchmarks (with provenance)

- **Hiring (independent):** firms with more than 500 lawyers hired 6,588 new law graduates last year, down 538 or 7.5% from the 2024 peak (BLAW-FIRSTYEAR-2026, citing NALP); the Class of 2025 entry-level market shrank by about 2,700 jobs while the class was also smaller (NALP-CLASS2025-2026). Citi: 86% of large firms plan more associates through 2027 versus 35% planning bigger first-year classes (LAW360-CITI-2025). Lateral associates were 51% of Am Law 200 associate hires (GLP-SUREPOINT-2026, vendor-published).
- **UK Big Four graduate intake (press-compiled):** KPMG 1,399 to 942; Deloitte 1,700 to 1,400; EY 1,800 to 1,600; PwC 1,600 to 1,500, 2023 to the latest year (SFN-BIG4-2025).
- **Adoption and training (survey):** 94% of 508 law firms engaged with GenAI, up 14 points; training required before access is 11% in firms under 50 lawyers and 72% in firms over 700; human review of work product required 31% to 83% across size bands (ILTA-TECHSURVEY-2026). 98% of about 600 accounting professionals use AI, fewer than half of firms invest in AI training and 21% have a documented policy or strategy (KARBON-JUNIOR-2026; KARBON-SOAI-2026, vendor-published). Karbon states firms using AI save about 60 minutes per employee per day (KARBON-JUNIOR-2026, vendor-published).
- **Learning pipeline (survey, in-house included):** in the 1,816-professional Thomson Reuters survey (private practice and in-house departments in 62 countries, March-April 2026), 71% believe early-career roles need structured support from experienced peers, 48% worry about AI's effect on independent judgment, and legal professionals expect the time to trusted judgment to lengthen by about 1.7 years while tax professionals expect it to shorten by 1.0 (TR-FOP-2026). In the same survey more than nine in ten report some AI value gap, one in four of those expect to leave within two years, at an estimated USD 232,000 per replacement (TR-FOP-2026).
- **Junior skills (survey):** 72% see deep legal reasoning as the biggest junior gap, 69% flag weak verification, 2% say AI mainly strengthens learning, 65% favour AI as a 'thinking partner', 52% support structured verification exercises (LEXIS-MENTORSHIP-2026; LCN-LEXIS-2026).
- **Evaluation practice (survey):** 31% of 106 firms use AI in associate evaluations; 100% include supervisors' qualitative comments (CANLAW-NALP-2025).
- **Leadership expectations (survey):** 71% of law-firm leaders expect junior roles to evolve; 83% of law firms plan to hire or train for AI-centric roles in 12 months; 85% of law firms rely on manual checks to enforce AI policies (LAW360-GA-2026).
- **Staffing and talent strain (vendor-commissioned):** 52.7% of resource managers say they are not equipped to manage hybrid human-agent teams, 4% feel well equipped (KANTATA-RMI-2026). Architecture and engineering firms report 1.2% staff growth, turnover above 13%, and talent and AI literacy as limiting factors (DELTEK-CLARITY-2026).
- **Quality evidence:** the only independent, blinded measurement is NBER-AUTOR-2026. No firm has published override rates, error-catch rates, parallel-run results or inspection findings for AI-supported junior review, onboarding, AI screening or AI-assisted evaluation.

### Guardrails and regulatory points

- **Supervision and training duties (California):** managerial and supervisory lawyers should set clear policies on generative and agentic AI, give appropriate training, review policies and training as tools become more autonomous, and ensure lawyer and nonlawyer staff get periodic training; a subordinate lawyer must not use AI in a way that breaches their own professional obligations and must exercise independent judgment (CALBAR-GENAI-2026, p. 7, 'Duty to Supervise').
- **AI in recruitment and worker management:** the EU AI Act lists AI for employment and worker management, such as CV-sorting for recruitment, as high-risk, with Annex III obligations extended to 2 December 2027 (EC-AIACT-2026). New York City requires a bias audit within a year of use, a public summary and notices (NYC-AEDT-2023). The UK ICO audited AI recruitment tools, made almost 300 recommendations, and found tools that filtered by protected characteristics or inferred gender and ethnicity from names (ICO-RECRUIT-2024).
- **Human decision retained:** Mishcon's Early Careers team makes all screening decisions (MISHCON-BRIGHT-2025); Duane Morris holds that a first draft is never a final submission (TRI-ONBOARDING-2026).
- **Policy and training gap by size:** formal GenAI policy in 57% of firms under 50 lawyers versus 98% and 91% of firms with 350-699 and over 700 lawyers (ILTA-TECHSURVEY-2026).
- **Disclosure caution on named-firm items:** several firm statements come via trade press and are not primary documents (see Gaps).

### Frontier signals (dated)

- 2026-06 and 2026-03 (past events): the AICPA & CIMA ENGAGE programme included a session on attracting, engaging and retaining younger talent and AI-integration sessions for CPAs (KARBON-ENGAGE-2026); Legalweek's programme included 'Starting Over: What Law Firms Would Change If They Built a New Firm Today' and a session framing AI value to include impact on people and their careers (EDRM-LEGALWEEK-2026). Session content was not captured.
- 2026-10-12: Duane Morris argues onboarding must be rebuilt mid-transition, not after things settle (TRI-ONBOARDING-2026).
- 2026-10-08: Harvey reports working with 100+ law schools; its strategy chief expects firms to notice which schools send AI-ready associates (NONBILLABLE-HARVEY-2026).
- 2026-09-10: Bloomberg Law reports two-thirds of 57 large firms expect fewer first-years in 2028 than 2025 (BLAW-FIRSTYEAR-2026).
- 2026-09-02: Sidley makes an AI seat compulsory for every London trainee (LEGALCHEEK-SIDLEY-2026).
- 2026-09: NBER trial shows durable skill gain went to seniors only (NBER-AUTOR-2026).
- 2026-07-30: Ropes & Gray and others use billable credit, competitions and human-skills training to raise AI use among associates (BLAW-ASSOCIATES-2026).
- 2026-03-24: General Assembly survey: 71% of law-firm leaders expect junior roles to evolve (LAW360-GA-2026).
- 2026-03 (cover story): the AICPA's Profession Ready initiative is researching early-career skills, with findings expected in 2027 (JOA-TRAINING-2026).
- 2026-01-14: McKinsey is reported to test graduates' work with Lilli in final rounds (GUARDIAN-MCKINSEY-2026).
- 2025-12-15: Citi/Hildebrandt: 86% versus 35% (LAW360-CITI-2025).
- 2025-10-31: KPMG to rate staff on AI objectives in 2026 reviews (BLOOMBERG-KPMG-2025).
- 2025-09-25: Accenture pairs upskilling with exits (CIODIVE-ACCENTURE-2025; FORTUNE-ACCENTURE-2025).

### Workforce and role effects

- Entry roles become review and supervision roles: PwC assurance, AICPA, Withum (BI-PWC-2025; JOA-TRAINING-2026).
- New or growing roles: AI champions inside practices (TRI-ONBOARDING-2026); data scientists and technologists (a Major Lindsey & Africa executive) and product managers, pricing experts, project managers and AI governance practitioners (TruLegal's founder) (LAW360-CITI-2025); training, innovation, KM and data science headcount (ILTA-TECHSURVEY-2026); TruLegal's founder also says hourly rates are already rising for lawyers with AI expertise (LAW360-CITI-2025, practitioner claim).
- Mid-level associates are already building their own agents, and mid-career professionals are the most mobile: almost three in ten would change jobs within two years if AI fails to deliver the value they expect (TRI-ONBOARDING-2026; TR-FOP-2026).
- Support staff are being cut or re-scoped at Clifford Chance and Baker McKenzie (CITYAM-CC-2025; LEGALCHEEK-BAKERMCK-2026).
- McKinsey's chief executive reportedly describes 20,000 agents alongside 40,000 staff, a digital workforce framing for capacity planning (GUARDIAN-MCKINSEY-2026).

### Objections and concerns practitioners raise

- Loss of the learning loop: error exposure, pattern recognition and judgment under uncertainty (KARBON-JUNIOR-2026); cognitive offloading, homogenised output and fear that blocks learning (TRI-DESIGNL-2026).
- The causal link between repetitive work and judgment is inferred rather than proven, so removing it is an uncontrolled experiment (TRI-DESIGNL-2026).
- Reviewers who never did the work cannot tell when the AI is wrong (KARBON-JUNIOR-2026; JOA-TRAINING-2026).
- Identity and fairness: associates wonder whether using AI counts as cheating or avoiding it means falling behind (TRI-CLOSEGAP-2026).
- Skeptics note earlier transformative innovations produced little change (ILTA-TECHSURVEY-2026), and Bloomberg Law cautions that the current hiring dip may follow historical cycles (BLAW-FIRSTYEAR-2026).
- Vendor-led training and law-school programmes may embed one vendor's tools early (NONBILLABLE-LEGORA-2026).
- Concern about training quality under hybrid working in UK consulting (MCA-SURVEY-2026, foreword).

### In-house tags

- **in-house:** TR-FOP-2026 covers in-house departments alongside firms (pipeline and attrition findings above). LEXIS-MENTORSHIP-2026 quotes in-house lawyers, including a deputy general counsel at Colt Technology Services, on juniors' research skills and on AI as drudgery removal. TRI-STANDOUT-2026 reports general counsel facing tool proliferation without governance, limited legal-ops infrastructure and team resistance. Harvey Academy targets legal operations teams (HARVEY-ACADEMY-2026). No named in-house deployment about junior development, recruiting or evaluation was found.

### Interview probes for an advisor

1. Walk through what a first-year or graduate did in their first year three years ago and now. Which tasks are gone, which are new, and what is teaching judgment in their place?
2. How are intake size and the lateral-versus-graduate mix decided, which AI assumptions sit in that plan, and who is accountable if they prove wrong?
3. When a junior reviews AI-assisted work, how do you know they can catch errors? Do you track error-catch or override rates, and who reviews the reviewers?
4. How is AI use reflected in objectives, bonuses and billable or chargeable credit, and what stops a usage metric being gamed?
5. For people whose work is absorbed: what are the rules for reskilling versus exit, and how do in-house or support teams get the same development as fee-earners?

## 4. Routed to other modules

- **staffing-resourcing:** Kantata's finding that 52.7% of resource managers are not equipped to manage hybrid human-agent teams and only 7.3% routinely use outcome data in staffing (KANTATA-RMI-2026); Deltek's utilisation, turnover above 13% and 1.2% staff growth (DELTEK-CLARITY-2026); the EU AI Act's treatment of AI for worker management when used to allocate work (EC-AIACT-2026).
- **firm-finance:** KPMG's stated aim of measuring the value of its AI investment through usage tracking (BLOOMBERG-KPMG-2025); PwC's USD 3 billion network investment (ATODAY-PWC-2026); Accenture's USD 865 million charges and USD 1 billion expected savings (FORTUNE-ACCENTURE-2025); Fredrikson's three business-model scenarios (TRI-LDEV-2026); Citi's expectation that AI investment will drive consolidation (LAW360-CITI-2025).
- **scoping-pricing:** clients asking for AI line items and refusing to pay for AI-done work (TRI-LEGALWEEK-2026); PwC's plan for subscription services with no PwC person in the loop (CPAPA-PWC-2026); 75% of law firms rethinking how they communicate about pricing and 41% reporting increased client scrutiny (LAW360-GA-2026).
- **client-development:** the finding that partners are not discussing AI with clients and are the commercial transmission mechanism of the firm (TRI-STANDOUT-2026).
- **quality-review:** California supervision duties for AI use (CALBAR-GENAI-2026); 85% of law firms using manual checks to enforce AI policies (LAW360-GA-2026).
- **knowledge-management / work-production:** Hogan Lovells Cadwalader's pilot of more than 1,300 lawyers in 18 practice teams before a global Legora rollout (LEGORA-HLC-2026); Ascend's 'closed loop' data capture (ATODAY-ASCEND-2026).

## 5. Sources

59 distinct sources cited in this file: 58 opened and read, 1 seen only in search results. By type: press 31, vendor 9, regulator 4, professional-body 4, conference 3, survey 3, firm 2, podcast 1, academic 1, job-posting 1. Community sources were blocked (see Gaps).

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ATODAY-PWC-2026 | PwC grows 2026 global revenue to $60.2B | Accounting Today | press | https://www.accountingtoday.com/news/pwc-grows-2026-global-revenue-to-60-2b | 2026-10-19 | full |
| BI-PWC-2025 | PwC is training junior accountants to be like managers, because AI is going to be doing the entry-level work | Business Insider | press | https://www.businessinsider.com/pwc-ai-training-changing-the-job-accountants-jenn-kosar-2025-8 | 2025-08-08 | full |
| BLAW-ASSOCIATES-2026 | What Does It Take to Get Big Law Associates Excited About AI? (Big Law Business column) | Bloomberg Law | press | https://news.bgov.com/business-and-practice/what-does-it-take-to-get-big-law-associates-excited-about-ai | 2026-07-30 | full |
| BLAW-FIRSTYEAR-2026 | Big Law First-Year Hiring Set to Plunge as History, AI Collide (Big Law Business column) | Bloomberg Law | press | https://news.bgov.com/business-and-practice/big-law-first-year-hiring-set-to-plunge-as-history-ai-collide | 2026-09-10 | full |
| BLOOMBERG-KPMG-2025 | KPMG Staff to Be Rated on AI Usage in Yearly Performance Reviews | Bloomberg | press | https://news.bgov.com/health-law-and-business/kpmg-staff-to-be-rated-on-ai-usage-in-yearly-performance-reviews | 2025-10-31 | full |
| CANLAW-NALP-2025 | Most law firm associate evaluations don't use AI or give speedy feedback: survey (on the NALP Foundation performance evaluation study) | Canadian Lawyer | press | https://www.canadianlawyermag.com/resources/practice-management/most-law-firm-associate-evaluations-dont-use-ai-or-give-speedy-feedback-survey/393386 | 2025-11-18 | full |
| CIODIVE-ACCENTURE-2025 | Accenture completes 'reinvention' as generative AI revenues roll in | CIO Dive | press | https://www.ciodive.com/news/accenture-generative-ai-revenue-skills-training-data-modernization/761161/ | 2025-09-25 | full |
| CITYAM-BIG4TRAINING-2026 | How AI is forcing the Big Four to rethink graduate training (Beyond The Billable column) | City AM | press | https://www.cityam.com/?p=2459320 | 2026-09-23 | full |
| CITYAM-CC-2025 | Clifford Chance AI-driven redundancies hit London business service roles | City AM | press | https://www.cityam.com/?p=2380354 | 2025-11-21 | full |
| CPAPA-PWC-2026 | PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm' (reporting the Financial Times) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/ | 2026-03-25 | full |
| FORTUNE-ACCENTURE-2025 | Accenture's $865 million reinvention includes saying goodbye to people without the right AI skills | Fortune | press | https://www.fortune.com/2025/09/27/accenture-865-million-reinvention-exiting-people-ai-skills | 2025-09-27 | full |
| GLP-SUREPOINT-2026 | Demand for AI experience drives lateral associate hiring increase, study finds (on SurePoint's Law School Hiring Report 2026) | Global Legal Post | press | https://www.globallegalpost.com/news/demand-for-ai-experience-drives-lateral-associate-hiring-increase-study-finds-969604187 | 2026-07-21 | full |
| GUARDIAN-MCKINSEY-2026 | McKinsey asks graduates to use AI chatbot in recruitment process | The Guardian | press | https://www.theguardian.com/business/2026/jan/14/mckinsey-graduates-ai-chatbot-recruitment-consultancy | 2026-01-14 | full |
| LAW360-CITI-2025 | Law Firms' Junior Roles At Risk From AI, Report Says (on the Citi Global Wealth at Work and Hildebrandt Consulting report) | Law360 Pulse | press | https://www.law360.com/articles/2422148/law-firms-junior-roles-at-risk-from-ai-report-says | 2025-12-15 | full |
| LAW360-GA-2026 | AI Set To Transform Junior Lawyer Roles, Survey Finds (on the General Assembly survey of 258 leaders) | Law360 UK | press | https://www.law360.com/articles/2456965/ai-set-to-transform-junior-lawyer-roles-survey-finds | 2026-03-24 | full |
| LCN-LEXIS-2026 | New survey highlights shifts in junior lawyer learning as AI use grows | LawCareers.Net | press | https://www.lawcareers.net/Explore/News/New-survey-highlights-shifts-in-junior-lawyer-learning-as-AI-use-grows-11022026 | 2026-02-11 | full |
| LCN-ROPES-2025 | Ropes & Gray junior lawyers to dedicate 20% of billable time to AI training | LawCareers.Net | press | https://www.lawcareers.net/Explore/News/Ropes-Gray-junior-lawyers-to-dedicate-20-of-billable-time-to-AI-training-191120 | 2025-11-19 | full |
| LCN-ROPES-EU-2026 | Ropes & Gray commits 20% of junior lawyer billable hours to AI exploration across Europe | LawCareers.Net | press | https://www.lawcareers.net/Explore/News/Ropes-Gray-commits-20-of-junior-lawyer-billable-hours-to-AI-exploration-across | 2026-01-14 | full |
| LEGALCHEEK-BAKERMCK-2026 | Baker McKenzie to cut business services roles as AI use grows | Legal Cheek | press | https://www.legalcheek.com/2026/02/baker-mckenzie-to-cut-business-services-roles-as-ai-use-grows/ | 2026-02-06 | full |
| LEGALCHEEK-LEXIS-2026 | Research suggests AI is impacting junior lawyers' judgement | Legal Cheek | press | https://www.legalcheek.com/2026/02/research-suggests-ai-is-impacting-junior-lawyers-judgement/ | 2026-02-10 | full |
| LEGALCHEEK-SHOOSMITHS-2025 | Shoosmiths drops £1 million into bonus pot after staff hit AI prompt target | Legal Cheek | press | https://www.legalcheek.com/2025/12/shoosmiths-drops-1-million-into-bonus-pot-after-staff-hit-ai-prompt-target/ | 2025-12-17 | full |
| LEGALCHEEK-SIDLEY-2026 | Sidley adds AI seat in training contract shake-up | Legal Cheek | press | https://www.legalcheek.com/2026/09/sidley-adds-ai-seat-in-training-contract-shake-up/amp/ | 2026-09-02 | full |
| NONBILLABLE-HARVEY-2026 | Harvey passes 100 law schools as firms seek AI-ready recruits | Non-Billable | press | https://www.nonbillable.co.uk/news/harvey-law-schools-ai-ready-recruits-juniors | 2026-10-08 | full |
| NONBILLABLE-LEGORA-2026 | Legora takes AI platform into law schools as US expansion accelerates | Non-Billable | press | https://www.nonbillable.co.uk/news/legora-us-law-school-programme | 2026-03-25 | full |
| SFN-BIG4-2025 | Big Four slash graduate jobs as AI takes over entry-level tasks (reporting The Telegraph, 22 Jun 2025) | Scottish Financial News | press | https://www.scottishfinancialnews.com/articles/big-four-slash-graduate-jobs-as-ai-takes-over-entry-level-tasks | 2025-06-23 | full |
| TRI-CLOSEGAP-2026 | 4 ways law firms can close gaps in legal judgment & professional identity | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/closing-legal-judgment-and-professional-identity-gaps | 2026-09-10 | full |
| TRI-DESIGNL-2026 | Designing lawyers: Attorney growth in the age of AI-fueled practice | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/designing-lawyers-professional-growth | 2026-05-11 | full |
| TRI-LDEV-2026 | Rethinking lawyer development in future AI-enabled law firms | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/lawyer-development-ai-enabled-law-firms | 2026-04-16 | full |
| TRI-ONBOARDING-2026 | Law firms need to redesign new attorney onboarding for the AI era | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding | 2026-10-12 | full |
| TRI-TAAP2030-2026 | The tax, accounting & audit firm of 2030: Building the people of tomorrow's tax firm (Jody Padar) | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/tax-audit-accounting-firm-of-2030-building-people-for-tomorrow | 2026-10-16 | full |
| TRI-TEACHV-2026 | The missing skill in legal AI training: How to teach verification and judgment | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/teaching-verification-and-judgment | 2026-09-01 | full |
| ANTHROPIC-DELOITTE-2025 | Deloitte will make Claude available to 470,000 people across its global network | Anthropic | vendor | https://www.anthropic.com/news/deloitte-anthropic-partnership | 2025-10-06 | full |
| DELTEK-CLARITY-2026 | The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity Pressures for Project-Based Businesses | Deltek | vendor | https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/ | 2026-05-12 | full |
| HARVEY-ACADEMY-2026 | Harvey Academy: Shaping the Future of Legal AI Literacy | Harvey | vendor | https://www.harvey.ai/blog/introducing-harvey-academy | 2026-01-27 | full |
| KANTATA-RMI-2026 | New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services | Kantata | vendor | https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services | 2026-04-09 | full |
| KARBON-JUNIOR-2026 | How do junior accountants learn when AI does the grunt work? | Karbon | vendor | https://karbonhq.com/resources/training-junior-accountants-ai/ | 2026-04-30 | full |
| KARBON-SOAI-2026 | Karbon State of AI in Accounting 2026 Report shows strategy, training, and governance unlock AI's full potential | Karbon | vendor | https://karbonhq.com/resources/state-of-ai-accounting-2026/ | 2026-01-23 | full |
| LEGORA-HLC-2026 | Hogan Lovells Cadwalader rolls out Legora globally | Legora | vendor | https://legora.com/newsroom/hogan-lovells-cadwalader-rolls-out-legora-globally | 2026-10-16 | full |
| LEXIS-MENTORSHIP-2026 | The mentorship gap (LexisNexis survey of 873 UK legal professionals, January 2026) | LexisNexis UK | vendor | https://www.lexisnexis.co.uk/insights/the-mentorship-gap/index.html | 2026-02 | full |
| SPELLBOOK-KENNEDYS-2025 | Preparing the Next Generation of AI-Fluent Lawyers: Spellbook Partners with Kennedys | Spellbook | vendor | https://spellbook.com/stories/kennedys | 2025 | full |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision) | State Bar of California, COPRAC | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05 | full |
| EC-AIACT-2026 | AI Act (regulatory framework page) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-19 | full |
| ICO-RECRUIT-2024 | ICO intervention into AI recruitment tools leads to better data protection for job seekers | Information Commissioner's Office (UK) | regulator | https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/11/ico-intervention-into-ai-recruitment-tools-leads-to-better-data-protection-for-job-seekers/ | 2024-11 | full |
| NYC-AEDT-2023 | Automated Employment Decision Tools (AEDT), Local Law 144 of 2021 | NYC Department of Consumer and Worker Protection | regulator | https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page | 2023-07-05 | full |
| JOA-TRAINING-2026 | How will accountants learn new skills when AI does the work? | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/ | 2026-03-01 | full |
| MCA-SURVEY-2026 | MCA Member Survey 2026 | Management Consultancies Association | professional-body | https://www.mca.org.uk/reports/mca-member-survey-2026 | 2026 | full |
| NALP-BULLETIN-2026 | NALP Foundation: Putting Performance Evaluations Through Their Paces: Problems and Potential | NALP Bulletin | professional-body | https://nalpbulletin.mydigitalpublication.com/articles/nalp-foundation-putting-performance-evaluations-through-their-paces-problems-and-potential | 2026-02 | full |
| NALP-CLASS2025-2026 | Strong Entry-Level Legal Employment Persists Despite Sharp Drop in Federal Government and Public Interest Hiring (Class of 2025 selected findings) | NALP | professional-body | https://www.nalp.org/uploads/PressReleases/Classof2025SelectedFindings_PressRelease.pdf | 2026-08-05 | full |
| EDRM-LEGALWEEK-2026 | Legalweek 2026 (Select) Educational Sessions Preview | EDRM | conference | https://edrm.net/2026/03/legalweek-2026-select-educational-sessions-preview/ | 2026-03-06 | full |
| KARBON-ENGAGE-2026 | 23 must-see sessions at AICPA & CIMA ENGAGE 2026 | Karbon | conference | https://karbonhq.com/resources/aicpa-cima-engage-2026/ | 2026-05-21 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| ILTA-TECHSURVEY-2026 | ILTA Technology Survey 2026 Executive Summary | ILTA | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 | full |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 | full |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 | full |
| FRESHFIELDS-KCL-2025 | Freshfields partners with King's College London to offer future trainees LL.M in Law and Technology | Freshfields | firm | https://www.freshfields.com/en/our-thinking/news/news-search/2025/07/freshfields-partners-with-kings-college-london-to-offer-future-trainees--ll.m-in-law-and-technology | 2025-07-02 | full |
| MISHCON-BRIGHT-2025 | Mishcon de Reya trials 'Bright Apply' to deliver fairer, more efficient hiring | Mishcon de Reya | firm | https://www.mishcon.com/news/mishcon-de-reya-trials-bright-apply-to-deliver-fairer-more-efficient-hiring | 2025-12-01 | full |
| ATODAY-ASCEND-2026 | The 'AI Native' firm (On the Air podcast with Ascend CEO David Wurtzbacher) | Accounting Today | podcast | https://www.accountingtoday.com/podcast/the-ai-native-firm | 2026-10-19 | full |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER Working Paper 35720) | NBER, via EconPapers (abstract page only) | academic | https://econpapers.repec.org/RePEc:nbr:nberwo:35720 | 2026-09 | full |
| EXPERIS-TRAINING-2026 | AI Technology Training Specialist (job posting for a New York or New Jersey law firm; seen in search summary only, posting page now expired) | Experis (ManpowerGroup) | job-posting | https://www.experis.com/en/job/385376/ai-technology-training-specialist- | 2026-04-16 | search-only |

## 6. Gaps

- **No quality or outcome data for junior development programmes.** No firm published error-catch, override, retention or time-to-competence figures for Ropes & Gray's credit scheme, Sidley's AI seat, Duane Morris onboarding, PwC or KPMG programmes, Mishcon's screening trial, KPMG's AI performance objectives or AI-assisted evaluations. Only NBER-AUTOR-2026 is an independent measurement, and its full paper was unreachable (abstract read only).
- **Job postings.** No usable posting from a named firm was opened. A search summary described an April 2026 posting for a law-firm AI training specialist (Experis, EXPERIS-TRAINING-2026; the posting page was expired) and a September 2026 Luxembourg 'Digital Learning & Legal Technology Specialist' role, and several contract 'AI trainer' gigs; none could be read, so they support no grade. Searches ran out of budget before targeted firm-careers searches could be tried.
- **Web search was exhausted.** About 16 searches were run; the last two attempted (first-year AI academies at named US firms; the A&O Shearman graduate AI assessment) were refused. Items known only from search results are marked in notes: the McKinsey December 2025 pilot detail, the A&O Shearman graduate AI assessment (The Lawyer headline), and the Shoosmiths April 2025 scheme details.
- **Blocked or unreadable:** Reuters on Ropes & Gray (CAPTCHA), Law Gazette (CAPTCHA), The Lawyer (challenge), Seyfarth/Law360 article on summer-associate AI training (challenge), Fortune's McKinsey piece (rate-limited mirror), TechDay on Kennedys/Spellbook (403), SurePoint's report (gated form), Citi's report (404), Reddit r/biglaw (403), The Telegraph on Big Four graduate cuts (paywalled body), NBER PDF (DNS).
- **Primary firm documents.** Most firm claims arrive through trade press or interviews. Primary newsrooms for PwC, KPMG, EY, Deloitte UK programmes and for McKinsey were not reached; the Accenture earnings release body and call transcript were not read.
- **Possible mirror artefacts.** The Bloomberg Law text I retrieved shows firm names 'Winston Taylor' and 'Sheppard LLP'; verify against the original column.
- **Community voices.** No community source (forum, newsletter thread) could be opened; the Reddit thread cited by Bloomberg Law was blocked.
- **Beyond law and accounting.** Evidence for consulting, architecture/engineering and project-based services is thin: McKinsey (reported), Deltek (talent strain, no programme), MCA (training-quality concern, no figures). No evidence found of AI changing graduate development at mid-tier consultancies or in-house shared-service centres.
- **Conference sessions.** Only previews were read (ENGAGE talent sessions; Legalweek's 'Starting Over' session title). No session content on talent and learning was captured; the Professional Development Consortium conference mentioned by TRI-CLOSEGAP-2026 was not found.
- **Dates inferred.** Page-metadata dates were used for ATODAY-PWC-2026, ATODAY-ASCEND-2026 and EC-AIACT-2026 (2026-10-19), CALBAR-GENAI-2026 (PDF creation, 2026-05), LEXIS-MENTORSHIP-2026 (inferred from coverage dated 2026-02-10), and the Spellbook page (2025, undated). TR-FOP-2026 shows no publication date (survey fielded March-April 2026).

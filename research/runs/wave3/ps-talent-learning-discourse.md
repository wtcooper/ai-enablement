# Professional services, talent and learning: discourse angle

Prepared 2026-10-19. Archetype: professional-services. Module: talent-learning. Angle: discourse (what practitioners are saying, last 12 to 18 months). Method: `curl` and `pdftotext` through a private working folder, plus a handful of web searches (the shared search budget ran out before the last planned searches). Every source below was opened unless marked `search-only`. Quotations are under 25 words. Items tagged **in-house** come from corporate legal or other client-side settings.

## 1. Summary

**What practitioners are saying.** The talent conversation in professional services has moved in about 12 months from "will AI cut headcount?" to "where does judgment come from if the work that built it goes away?". The associate (and the junior accountant, and the consulting analyst) is now the named pressure point. At Legalweek 2026 the junior lawyer question "graduated from a half-whispered aside to main-stage conversation" (TRI-LEGALWEEK-ASSOC-2026). Thomson Reuters' 2026 survey puts a number on the worry: 48% of professionals fear a negative effect on independent judgment development (TR-FOP-2026).

- **Evidence is thin where it matters most.** Only one measured study speaks directly to learning: an NBER randomised trial of 133 patent lawyers in which AI raised work quality, but the unaided-skill advantage after three months sat with senior lawyers, and juniors showed no average gain (NBER-AUTOR-2026). It was conducted and funded by Google, covers one task, and only the abstract was readable here. Everything else in this module is practitioner statement, survey, or announcement. No source reports error rates, override rates or parallel-run results for AI-supervising juniors.
- **Hiring signals diverge.** Large US firms hired 6,588 new graduates in 2025, down 7.5% from the 2024 peak (NALP, via BLOOMBERGLAW-HIRING-2026). Two-thirds of 57 large firms surveyed by Citi expect fewer first-years in 2028 than 2025, and 19% did not know (BLOOMBERGLAW-HIRING-2026). UK Big Four graduate intakes were reported cut by between 6% and 29% over two years (CITYAM-BIG4-2025; ICAEW-EXPECT-2026), although PwC UK named the economy as "the single biggest factor" (PEOPLEMATTERS-PWC-2025). Against that, McKinsey said it planned to grow North American staff 12% in 2026 (PEOPLEMATTERS-MCK-2025) and an ICAEW article says the Big Four each plan at least 1,000 junior hires this year (ICAEW-JUNIOR-2026). Cause and effect are disputed.
- **Firms are rebuilding training, mostly with simulation, coaching and "supervise the AI" curricula.** The named, concrete moves are small and self-reported: Duane Morris's onboarding redesign (TRI-ONBOARD-2026), Ropes & Gray giving first-years about 20% of billable time for AI work (LEGALCHEEK-RG-2025), A&O Shearman's associate seats in its innovation group (NONBILLABLE-AOS-2026), Kennedys with Spellbook (LAWNEXT-KENNEDYS-2025). None publishes outcome measures.
- **Incentives are being rewired from the top.** PwC's US CEO said staff with an "opportunity to opt out" of AI would not be there long (REGISTER-PWC-2026). Accenture reportedly tracks senior staff AI log-ins and requires "regular adoption" for leadership promotion (DECRYPT-ACCENTURE-2026).
- **Mid-career is the quiet risk.** TR reports that mid-career professionals are the most mobile and that 24% of those seeing an AI value gap are considering leaving within two years (TR-FOP-2026). That survey comes from a company that sells AI products.

**Use cases.** 20 candidates: 1 grade A, 6 grade B, 9 grade C, 4 grade D (labelled ideas). Only the A (the NBER trial) rests on a figure measured by the organisation that ran it; no firm has published outcome figures for its own talent changes.

## 2. Use cases

```yaml
- id: professional-services-talent-learning-01
  title: Simulation-based practice replaces the "repetition loop" for junior lawyers
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [expert-judgment]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >-
    Junior lawyers learned judgment by repeating foundational tasks (drafting, review, deposition preparation) under
    senior feedback. AI is absorbing those tasks, so the repetitions and the feedback loop are disappearing, and juniors
    are being pushed into advisory work before they have built instinct.
  solution: >-
    Scenario-based practice with AI role-players and AI feedback, such as deposition simulations where the AI witness has
    a fixed truth but freedom within it, with adjustable cooperation or hostility, and drafting exercises with structured
    feedback that stands in for senior coaching. Supervisors' knowledge is captured into the scenarios.
  outcomes:
    - lever: experience
      description: No outcome measures published. Described uses include a litigation chair running a live teaching demonstration for 500 attorneys, mentor-mentee coaching built on the tool's feedback, and associates preparing for real depositions.
      figure: none published
      measures: n/a
      provenance: vendor-published
      source_ref: TRI-SIM-2026
  prerequisites:
    - A rubric tied to clear learning objectives, with feedback anchored to specific skills and judgment calls
    - Built-in unpredictability so the learner has to adapt
    - Supervisors and experienced lawyers willing to contribute scenario knowledge
  risks_and_guardrails:
    - No published evidence that skills learned in simulation transfer to live matters
    - A Kennedys leader said the firm has not "cracked the problem" and that the programme was in its infancy at announcement (LEGALITINSIDER-KENNEDYS-2025)
    - Vendor leaders describe the profession as slow to treat training as strategic (TRI-SIM-2026)
  human_checkpoints:
    - Mentor-mentee coaching conversations using the simulation feedback
    - Partner or practice-group sign-off on scenario realism
  role_evolution: >-
    Associates can fail privately before failing in front of partners (Orrick's Kate Orr, TRI-LEGALWEEK-ASSOC-2026). A Smith Gambrell partner framed the aim as leading at trial in year 10 rather than year 20 (aspiration, not a result).
  evidence_grade: C
  sources:
    - {ref: TRI-SIM-2026, title: "How AI simulation could reshape legal training and education", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/ai-simulation-legal-training", date: 2026-05-15, access: full, locator: "Sections: AI and the cultivation of legal judgment; three design pillars"}
    - {ref: TRI-LEGALWEEK-ASSOC-2026, title: "Move over, 'Death of the billable hour,' Legalweek 2026 has found a new existential crisis", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-new-existential-crisis", date: 2026-03-19, access: full, locator: "Section: Fewer reps, greater weight (Developing the Future Lawyer panel)"}
    - {ref: LAWNEXT-KENNEDYS-2025, title: "Kennedys partners with Spellbook to launch groundbreaking legal training programme for the AI era", publisher: LawNext (Kennedys press release), type: press, url: "https://www.lawnext.com/2025/10/kennedys-partners-with-spellbook-to-launch-groundbreaking-legal-training-programme-for-the-ai-era.html", date: 2025-10-01, access: full, locator: "Paragraphs 3-5"}
    - {ref: LEGALITINSIDER-KENNEDYS-2025, title: "'A massive step in the right direction': Kennedys partners with Spellbook to rethink junior training in the AI era", publisher: Legal IT Insider, type: press, url: "https://legaltechnology.com/a-massive-step-in-the-right-direction-kennedys-partners-with-spellbook-to-rethink-junior-training-in-the-ai-era/", date: 2025-10-02, access: full, locator: "Paragraphs 2-8"}
    - {ref: HARBOR-LEGALSOUNDINGS-2026, title: "Legal Soundings: Talent & Innovation in the Age of AI (episode 1)", publisher: Harbor, type: podcast, url: "https://harborglobal.com/audio/legal-soundings-talent-innovation-in-the-age-of-ai/", date: 2026-01-28, access: full, locator: "Episode description (show notes read; audio not heard)"}
  last_reviewed: 2026-10-19
  notes: >-
    AltaClaro (the DepoSim vendor) says it has served the Am Law 200 for almost a decade; customers are not named, so the maturity is set to piloting rather than in-production. Kennedys' programme was announced as "set to launch later this year" (2025); no later status was found.

- id: professional-services-talent-learning-02
  title: AI persona rehearsal for client, interview and difficult-feedback conversations
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [client-interaction, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: >-
    Power skills (delivering bad news, interviewing a client, giving or receiving hard feedback) used to be absorbed on
    the job; rehearsing with a live coach has low uptake, and the work that exposed juniors to client conversations is
    shrinking.
  solution: >-
    A language-model persona that juniors practise against in private, with feedback. Examples described: a ChatGPT-based
    tool for rehearsing difficult feedback conversations, and an AI interviewee persona used in an accounting course.
  outcomes:
    - lever: experience
      description: Duane Morris's talent chief said an earlier avatar tool with a human coach controlled in real time saw very few users, while a later ChatGPT-based version for the same purpose "succeeded" with people who would not rehearse with a live coach. No usage figures given.
      figure: none published
      measures: n/a
      provenance: self-reported
      source_ref: TRI-ONBOARD-2026
  prerequisites:
    - Private practice space so juniors are not observed failing
    - A coach or rubric defining what good looks like
  risks_and_guardrails:
    - Evidence is anecdotal; the tools described were built at an unnamed prior firm and under the speaker's later leadership, and she is "in early talks" with a former colleague on a related concept (TRI-ONBOARD-2026)
    - The accounting examples are university teaching tools, not firm deployments (JOFA-LEARN-2026)
  human_checkpoints:
    - Debrief with a senior after the rehearsal
  role_evolution: >-
    Power skills are treated as the differentiator between good and outstanding lawyers, because AI raises the baseline for surface competence (TRI-ONBOARD-2026).
  evidence_grade: C
  sources:
    - {ref: TRI-ONBOARD-2026, title: "Law firms need to redesign new attorney onboarding for the AI era", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding", date: 2026-10-12, access: full, locator: "Section: Raising the bar for power skills"}
    - {ref: JOFA-LEARN-2026, title: "How will accountants learn new skills when AI does the work?", publisher: Journal of Accountancy (AICPA & CIMA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/", date: 2026-03-01, access: full, locator: "Sections: Use AI as a training partner; The future of education may be simulation-based"}
  last_reviewed: 2026-10-19
  notes: >-
    Grade capped at C: the law-firm example has no named deployment with data, and the accounting examples are higher-education tools (adjacent setting).

- id: professional-services-talent-learning-03
  title: Redesigned onboarding for new associates around AI fluency, AI champions and judgment
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [expert-judgment, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    New associates already form AI habits before the firm gives guidance, and the tasks that built their capability are
    being absorbed by AI, so a one-time training session no longer develops either AI practice or judgment.
  solution: >-
    Duane Morris describes a layered programme: a two-day in-person orientation including a live AI-and-library research
    session; twice-monthly extended sessions from September to June; designated AI champions in each practice group
    (a partner, counsel or senior associate with early access who tests tools on real work and helps others); and a
    separate traditional mentorship track. One fixed rule: a first draft is never an appropriate final submission.
    The talent team debriefs each outgoing class every summer to redesign the next.
  outcomes:
    - lever: experience
      description: No outcome measures published.
      figure: none published
      measures: n/a
      provenance: self-reported
      source_ref: TRI-ONBOARD-2026
  prerequisites:
    - A named talent and growth leader with authority over the programme
    - Practice-group champions given early access to tools
    - Annual debrief of the outgoing class
  risks_and_guardrails:
    - The firm lets lawyers choose how to use AI for first drafts; the control is the review rule, not tool restriction (TRI-ONBOARD-2026)
    - Reported only by the firm's own talent chief; no independent check
  human_checkpoints:
    - Mandatory human review of every AI-assisted first draft
    - Mentorship track for questions such as whether using AI with a given partner will look inefficient
  role_evolution: >-
    Mid-level associates who once warned peers off ChatGPT are now building their own agents; the firm emphasises "power skills" such as client confidence and business fluency (TRI-ONBOARD-2026).
  evidence_grade: B
  sources:
    - {ref: TRI-ONBOARD-2026, title: "Law firms need to redesign new attorney onboarding for the AI era", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding", date: 2026-10-12, access: full, locator: "Sections: Associates are already forming AI habits; What a redesigned onboarding program looks like"}
    - {ref: LIV-CROSSEXAMINED-2026, title: "How AI in legal supervision is changing lawyer training (Cross-Examined, S1 E4)", publisher: Law Institute of Victoria, type: podcast, url: "https://www.castfox.net/podcast/cross-examined-7610284/episode/how-ai-in-legal-supervision-is-changing-lawyer-training-1785836", date: 2026-03-23, access: full, locator: "Episode description (show notes only; audio not heard)"}
  last_reviewed: 2026-10-19
  notes: >-
    In-house tag: none. The Law Institute of Victoria episode (Allens speakers) is cited only for its description of mentoring changes and digital-literacy programmes. Latham's AI Academy (mandatory two-day in-person associate training, launched 2024) and Freshfields paying for incoming trainees' LLM at King's College London are mentioned in NONBILLABLE-RG-2026 and are covered in use case 18.

- id: professional-services-talent-learning-04
  title: Billable-credited time for junior lawyers to experiment with and train on AI
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [expert-judgment]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >-
    Innovation and training time competes with billable targets, so juniors have little protected time to learn AI
    tools or to develop new ways of working.
  solution: >-
    Ropes & Gray's "Trailblazers" programme gives first-year associates (and, in Europe, trainees and newly qualified
    lawyers) around 20% of billable hours for hands-on experimentation, formal and on-demand training, partner-led
    mentoring circles and peer cohorts. The time is tracked as billable and progress reported in regular group sessions.
    Use cases and feedback flow into the firm's wider AI strategy.
  outcomes:
    - lever: experience
      description: No outcome measures published. A spokesperson called the work "essential to professional development".
      figure: none published
      measures: n/a
      provenance: self-reported
      source_ref: SCOTTISHLEGAL-RG-2026
  prerequisites:
    - Firm willingness to count the time as billable so that fee targets do not penalise participation
    - Partner mentors and a forum for sharing use cases
  risks_and_guardrails:
    - Cost of the programme is borne in billable-hour credit; no published view on its economics
    - Legal Cheek's figures of a 1,900-hour target and about 400 hours of AI training are worded "reportedly" and "roughly"; treat as approximate (LEGALCHEEK-RG-2025)
  human_checkpoints:
    - Partner-led mentoring circles
    - Regular group reporting of progress
  role_evolution: >-
    Early-career lawyers are positioned to shape how the firm uses AI, not only to receive training (NONBILLABLE-RG-2026).
  evidence_grade: B
  sources:
    - {ref: LEGALCHEEK-RG-2025, title: "Ropes & Gray encourages junior lawyers to spend 20% of billable time on AI", publisher: Legal Cheek, type: press, url: "https://www.legalcheek.com/2025/11/ropes-gray-encourages-juniors-to-spend-20-of-billable-hours-on-ai/amp/", date: 2025-11-19, access: full, locator: "Paragraphs 1-3 and 5"}
    - {ref: SCOTTISHLEGAL-RG-2026, title: "Law firm tasks junior lawyers with exploring AI", publisher: Scottish Legal News, type: press, url: "https://www.scottishlegal.com/articles/ropes-gray-tasks-junior-lawyers-with-exploring-ai", date: 2026-01-12, access: full, locator: "Whole article"}
    - {ref: NONBILLABLE-RG-2026, title: "Ropes & Gray gives junior lawyers 20% of billable time for AI work", publisher: Non-Billable, type: press, url: "https://www.nonbillable.co.uk/news/ropes-gray-gives-junior-lawyers-20-of-billable-time-for-ai-work", date: 2026, access: full, locator: "Paragraphs 1-4"}
  last_reviewed: 2026-10-19
  notes: >-
    The Non-Billable page showed only a crawl timestamp, so its date is given as 2026 (it describes the European expansion; Scottish Legal News dates the London plan to 2026-01-12). Legal Cheek says Reed Smith has also offered credit for innovation-related projects; no primary source for that was opened.

- id: professional-services-talent-learning-05
  title: Formal curriculum for supervising and validating AI output
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [review-assurance, expert-judgment]
  pattern: draft-review-loop
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Most AI training teaches what the tools do, not when to trust, verify or override them, yet professionals are held
    accountable for AI-assisted work.
  solution: >-
    Training built around reviewing AI-assisted work alongside experienced practitioners, seeing where errors arise, and
    practising challenge and override. Examples: Fredrikson & Byron's stated goal of a formal curriculum on efficiently
    supervising AI output; PwC's "back to basics" shift toward audit fundamentals and professional skepticism; Withum's
    "AI analytical mindset"; a University of Central Florida "critical thinking milestone staircase" from AI user to AI
    evaluator.
  outcomes:
    - lever: quality
      description: Among professionals whose organisation has a strategy-execution gap, 43% say it is because people are not equipped or trained to work in the intended way.
      figure: "43%"
      measures: "Share of professionals experiencing a strategy-execution gap who gave 'people are not equipped or trained to work in the intended way' as the reason (TR 2026 survey of 1,816 professionals)"
      provenance: vendor-published
      source_ref: TR-FOP-2026
  prerequisites:
    - Role-specific standards for validation and override embedded in workflows (TRI-STANDARDS-2026)
    - Supervised review time for juniors, with exposure to edge cases and AI failures
  risks_and_guardrails:
    - A junior who cannot review AI output may pass errors on; a UK trainee warned that junior staff tasked with AI oversight too early is a "banana skin" (ICAEW-WORRIED-2026)
    - Fredrikson's leader said the goal "has not fully happened yet" (TRI-LAWYERDEV-2026)
  human_checkpoints:
    - Senior review of juniors' challenge-and-override decisions
    - Tracking of override patterns to retrain either system or people (TRI-STANDARDS-2026)
  role_evolution: >-
    Juniors move from executing tasks to evaluating output; the TR 2026 report says most training misses "the judgment layer" (TR-FOP-2026).
  evidence_grade: C
  sources:
    - {ref: TRI-LAWYERDEV-2026, title: "Rethinking lawyer development in future AI-enabled law firms", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/lawyer-development-ai-enabled-law-firms", date: 2026-04-16, access: full, locator: "Section: Aligning the talent model to the future business model"}
    - {ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: 2026, access: full, locator: "Recommendations section: 'Among professionals experiencing a strategy-execution gap, 43%...'"}
    - {ref: JOFA-LEARN-2026, title: "How will accountants learn new skills when AI does the work?", publisher: Journal of Accountancy (AICPA & CIMA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/", date: 2026-03-01, access: full, locator: "Sections: From memorization to conceptual mastery; Upskilling at scale inside firms"}
    - {ref: BI-PWC-2025, title: "PwC is training junior accountants to be like managers, because AI is going to be doing the entry-level work", publisher: Business Insider (syndicated on Yahoo Finance), type: press, url: "https://finance.yahoo.com/news/pwc-training-junior-accountants-managers-170001522.html", date: 2025-08-08, access: full, locator: "Section: AI has got PwC rethinking how it trains its junior employees"}
    - {ref: TRI-STANDARDS-2026, title: "Between accountability and chaos: Setting the AI standards that professionals demand", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/between-accountability-and-chaos", date: 2026-10-12, access: full, locator: "Section: What standards should actually look like (professional competency standard)"}
    - {ref: TRI-AIUNDERGRADS-2026, title: "From AI users to AI thinkers: Reimagining what accounting undergrads need to succeed", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/ai-needs-accounting-undergrads", date: 2026-07-21, access: full, locator: "Section: Building a curriculum the marketplace needs"}
  last_reviewed: 2026-10-19
  notes: >-
    The UCF framework is a university curriculum (adjacent setting). Fredrikson's curriculum is a stated goal for the year ahead as of April 2026, not a launched programme.

- id: professional-services-talent-learning-06
  title: Entry-level hires start as reviewers and supervisors of AI work (compressed progression)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    If AI performs routine preparation work, a junior who only executes tasks has little to do, and the career ladder
    has an empty bottom rung.
  solution: >-
    PwC's AI assurance leader said new hires in assurance will arrive as reviewers and supervisors of AI doing routine
    audit tasks, and expects first-years to function more like fourth-years within about three years. Withum is "pushing
    certain responsibilities down from senior to junior team members". Both are accompanied by training changes.
  outcomes:
    - lever: capacity
      description: None published. PwC's statement is a forward-looking expectation ("we will feel like the first years are functioning more like fourth years").
      figure: none published
      measures: n/a
      provenance: self-reported
      source_ref: BI-PWC-2025
  prerequisites:
    - AI performing the routine data gathering and processing reliably enough to be supervised
    - Training in audit fundamentals, critical thinking, negotiation and professional skepticism earlier in careers
  risks_and_guardrails:
    - The PwC statement applies to its assurance division, not advisory or tax (BI-PWC-2025)
    - Reviewers who cannot judge AI output may "rubber-stamp"; a Karbon article warns of juniors "very uncertain about what to do when the AI is wrong" (KARBON-JUNIOR-2026)
    - A PKF Smith Cooper manager said over-reliance shows when a trainee cannot answer questions confidently (ICAEW-WORRIED-2026)
  human_checkpoints:
    - Manager questioning of trainees on logic and reasoning, even when the result is right
  role_evolution: >-
    The entry-level job becomes review and oversight. Karbon reports that 20% of accounting firm leaders in its survey are already changing organisational design by outsourcing junior roles or filling them with AI (vendor survey; sample size not captured).
  evidence_grade: C
  sources:
    - {ref: BI-PWC-2025, title: "PwC is training junior accountants to be like managers, because AI is going to be doing the entry-level work", publisher: Business Insider (syndicated on Yahoo Finance), type: press, url: "https://finance.yahoo.com/news/pwc-training-junior-accountants-managers-170001522.html", date: 2025-08-08, access: full, locator: "Paragraphs 3-9"}
    - {ref: JOFA-LEARN-2026, title: "How will accountants learn new skills when AI does the work?", publisher: Journal of Accountancy (AICPA & CIMA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/", date: 2026-03-01, access: full, locator: "Section: Upskilling at scale inside firms (Richardson, Withum)"}
    - {ref: KARBON-JUNIOR-2026, title: "How do junior accountants learn when AI does the grunt work?", publisher: Karbon Magazine, type: vendor, url: "https://karbonhq.com/resources/training-junior-accountants-ai/", date: 2026-04-30, access: full, locator: "Sections: What's actually at stake; Redesigning junior roles around oversight"}
    - {ref: ICAEW-WORRIED-2026, title: "AI: are junior accountants worried about roles?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/jun-2026/ai-are-junior-accountants-worried-about-roles", date: 2026-06, access: full, locator: "Quotes from MacDonald and Laurenti"}
  last_reviewed: 2026-10-19
  notes: >-
    The 2025 Business Insider interview is about 14 months old; no follow-up showing realised progression was found. The Karbon 20% figure is quoted from a vendor article about its own survey; the survey report is gated.

- id: professional-services-talent-learning-07
  title: "Idea: milestone-based development and deliberate-mistake exercises in the first two years"
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [expert-judgment]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Time served on repetitive tasks was the assumed route to judgment; with that work automated, firms cannot wait 10 to
    15 years for judgment to appear.
  solution: >-
    Replace time-served progression with milestones (what the person must know, do, who teaches it, how often practised,
    what evidence shows readiness), and give juniors seeded-error exercises: completed returns with buried issues, a
    plausible but incomplete AI recommendation, a client scenario with several defensible answers, and sitting in on a
    client conversation followed by structured debrief questions (what did you notice, what did you miss).
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: n/a
      provenance: self-reported
      source_ref: TRI-TAX2030-2026
  prerequisites:
    - Managers who can teach and give specific, timely feedback rather than only review (CPAPA-STOP-2026)
    - A defined view of what a junior should be able to do 18 to 24 months in
  risks_and_guardrails:
    - Profession is "built around getting things right", so deliberate mistakes need a safe environment, not live client engagements (TRI-TAX2030-2026)
    - AICPA's "Profession Ready" research on early-career roles and skills is not expected to report until 2027 (JOFA-LEARN-2026)
  human_checkpoints:
    - Manager debrief after each exercise or client meeting
  role_evolution: >-
    The entry-level accountant may start closer to where a senior begins; hiring shifts to "figure-it-out" ability (TRI-TAX2030-2026).
  evidence_grade: D
  sources:
    - {ref: TRI-TAX2030-2026, title: "The tax, accounting & audit firm of 2030: Building the people of tomorrow's tax firm", publisher: Thomson Reuters Institute (Jody Padar, The Radical CPA), type: press, url: "https://www.thomsonreuters.com/en/institute/articles/tax-audit-accounting-firm-of-2030-building-people-for-tomorrow", date: 2026-10-16, access: full, locator: "Sections: Start training through experience; The first 2 years need to look completely different"}
    - {ref: CPAPA-STOP-2026, title: "Stop Training CPAs for Yesterday's Work", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/09/02/stop-training-cpas-for-yesterdays-work/189548/", date: 2026-09-02, access: full, locator: "Paragraphs 3-7 (source document literacy, structured mentorship)"}
    - {ref: JOFA-LEARN-2026, title: "How will accountants learn new skills when AI does the work?", publisher: Journal of Accountancy (AICPA & CIMA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/", date: 2026-03-01, access: full, locator: "Section: From memorization to conceptual mastery (Profession Ready)"}
  last_reviewed: 2026-10-19
  notes: >-
    Idea (grade D). The milestone model is attributed to Dr Rachel Anevski of Matters of Management in a column by a consultant; no firm was named as using it.

- id: professional-services-talent-learning-08
  title: AI feedback coach on junior work product
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Tailored feedback on a junior's work is essential to growth but is scarce because senior time is limited and
    hierarchy can inhibit asking.
  solution: >-
    Review tools that let juniors see problems and fix them before the manager does, giving detailed feedback without
    using manager training time; bespoke firm-trained assistants that supply immediate tailored feedback; and AI that
    plays devil's advocate or runs mock negotiations.
  outcomes:
    - lever: speed
      description: A BYU professor reports that an AI-based Excel tool automating parts of the review process is used by entry-level staff so they "get detailed feedback and improve without requiring training time from their manager". No measures given.
      figure: none published
      measures: n/a
      provenance: self-reported
      source_ref: JOFA-LEARN-2026
  prerequisites:
    - Firm-specific standards and examples for the tool to check against
    - Controls at firm level on review of juniors' work (High Rock Accounting's CEO)
  risks_and_guardrails:
    - Beautifully crafted AI output can create "the illusion of competence" and cognitive offloading (TRI-SEYFARTH-2026)
    - A junior using a firm-trained assistant may deliver advanced output "they may not be able to review" (JOFA-LEARN-2026)
  human_checkpoints:
    - Manager review remains; the tool pre-screens
  role_evolution: >-
    Seyfarth's managing partner suggests AI feedback could supplement mentorship by widening access to guidance "previously limited by time, ego, and hierarchy" (TRI-SEYFARTH-2026).
  evidence_grade: C
  sources:
    - {ref: JOFA-LEARN-2026, title: "How will accountants learn new skills when AI does the work?", publisher: Journal of Accountancy (AICPA & CIMA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/", date: 2026-03-01, access: full, locator: "Sections: AI affects all rungs of the career ladder; Theoretical understanding isn't enough"}
    - {ref: TRI-SEYFARTH-2026, title: "Designing lawyers: Attorney growth in the age of AI-fueled practice", publisher: Thomson Reuters Institute (Lorie Almon, Seyfarth Shaw), type: press, url: "https://www.thomsonreuters.com/en/institute/articles/designing-lawyers-professional-growth", date: 2026-05-11, access: full, locator: "Section: Leadership in an AI age"}
    - {ref: TRI-GENAITALENT-2024, title: "GenAI in the legal industry: Where it's already impacting legal talent management", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/genai-legal-talent", date: 2024-11-04, access: full, locator: "Section: Long-term impact on professionals (older foundation, outside the 18-month window)"}
  last_reviewed: 2026-10-19
  notes: >-
    Grade C: a named professor describes a tool in use by entry-level staff but not where or with what results. The 2024 article is cited only as the earliest TRI statement that AI could provide virtual training environments and draft feedback.

- id: professional-services-talent-learning-09
  title: Associate seats inside the firm's AI and innovation group
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [software-systems, client-interaction]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Associates need a development path when drafting and diligence no longer fill the day, and the firm needs people who
    understand both the practice and the AI tools.
  solution: >-
    A&O Shearman's Markets Innovation Group (MIG) is a 27-person team of lawyers, developers and innovation specialists
    building internal tools and client-facing AI products. Associates join (one via a fourth seat) and work on prompt and
    playbook refinement, governance and guardrails, product work on the firm's ContractMatrix Word add-in (built with
    Harvey and Microsoft), client demos and tutorials.
  outcomes:
    - lever: experience
      description: No outcome measures published. One associate says AI has moved from a "passion project" to something that "can actually really be helpful and useful for your career".
      figure: none published
      measures: n/a
      provenance: self-reported
      source_ref: NONBILLABLE-AOS-2026
  prerequisites:
    - An established innovation group with partner leadership (led by a partner who is global lead for AI Advisory)
    - Early adoption: the firm began sandboxing Harvey in September 2022
  risks_and_guardrails:
    - Small number of seats relative to an intake; coverage is by the firm's trade-press interviews, not the firm's own data
  human_checkpoints:
    - Outputs are checked against the playbook and compared to what a senior associate would have drafted (NONBILLABLE-AOS-2026)
  role_evolution: >-
    The associate role in a product journey includes demos, client conversations and relationship building, which a traditional seat does not.
  evidence_grade: B
  sources:
    - {ref: NONBILLABLE-AOS-2026, title: "Meet the junior lawyers putting AI to work inside A&O Shearman", publisher: Non-Billable, type: press, url: "https://www.nonbillable.co.uk/posts/junior-lawyers-ai-innovation-a-o-shearman-harvey", date: 2026-03-10, access: full, locator: "Sections: Need to know; Susannah McMillan; Emma Jing"}
    - {ref: TRI-LAWYERDEV-2026, title: "Rethinking lawyer development in future AI-enabled law firms", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/lawyer-development-ai-enabled-law-firms", date: 2026-04-16, access: full, locator: "Section: Aligning the talent model (Boyko suggests rotations through KM, professional development, technology)"}
  last_reviewed: 2026-10-19
  notes: >-
    A&O Shearman is also named in the landscape (NONBILLABLE-AOS). The 27-person figure describes the team size, not an outcome.

- id: professional-services-talent-learning-10
  title: "Idea: new junior operational roles (AI compliance, legal data, knowledge curation) as an apprenticeship route"
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [data-reporting, software-systems]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    If drafting and research are cheap, the junior's bottleneck-relieving work moves to operations, data and verification,
    and firms need a defined route into those tasks.
  solution: >-
    Rotate first- and second-year lawyers through roles such as AI compliance specialist (usage policy, vendor claims,
    audit trails), legal data analyst (turning matter history into playbooks and outcome tags), knowledge operations
    curator (keeping clause libraries and precedent reliable) and a lawyer who prototypes workflows in software.
    A related suggestion is rotations through knowledge management, professional development and technology functions.
  outcomes:
    - lever: capacity
      description: none published
      figure: none published
      measures: n/a
      provenance: self-reported
      source_ref: TRI-AILAWPROF-JUNIOR-2026
  prerequisites:
    - Firm KM and data infrastructure that juniors can curate
    - New metrics and compensation structures for junior performance (column author's call)
  risks_and_guardrails:
    - Roles are "transitional", a pathway rather than a destination (TRI-AILAWPROF-JUNIOR-2026)
    - A messy period is expected in which juniors "are asked to double-check outputs without being taught how"
  human_checkpoints:
    - Supervised progression to strategic roles
  role_evolution: >-
    The junior becomes "a hybrid of lawyer, analyst, builder, and quality controller" (TRI-AILAWPROF-JUNIOR-2026).
  evidence_grade: D
  sources:
    - {ref: TRI-AILAWPROF-JUNIOR-2026, title: "The AI Law Professor: When AI forces us to rethink how we train junior lawyers", publisher: Thomson Reuters Institute (Tom Martin, LawDroid), type: press, url: "https://www.thomsonreuters.com/en/institute/articles/ai-law-professor-train-junior-lawyers", date: 2026-02-02, access: full, locator: "Section: The AI-accelerated apprenticeship"}
    - {ref: TRI-LAWYERDEV-2026, title: "Rethinking lawyer development in future AI-enabled law firms", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/lawyer-development-ai-enabled-law-firms", date: 2026-04-16, access: full, locator: "Section: Aligning the talent model to the future business model"}
    - {ref: ILTA-TECHSURVEY-2026, title: "The ILTA Technology Survey 2026 Executive Summary", publisher: ILTA, type: professional-body, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026-06, access: full, locator: "p.5 (firms anticipate added headcount across IT, innovation, security, training, KM, data science)"}
  last_reviewed: 2026-10-19
  notes: >-
    Idea (grade D): a columnist's prediction ("should expect to see"); no firm named as running these rotations other than the A&O seat in use case 09. The ILTA survey date is inferred from the file name (2606) and the landscape note (June 2026); PDF metadata shows creation on 2026-08-14.

- id: professional-services-talent-learning-11
  title: Candidate assessment on working with AI and on judgment rather than credentials
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    GPA, school and technical knowledge say little about how a candidate performs when the answer is unclear and AI can
    supply a fluent first draft.
  solution: >-
    Interview and screening changes: reportedly asking some McKinsey finalists to work with the firm's internal tool
    Lilli in a test; hiring for curiosity, adaptability and "human skills" rather than a checklist of AI tools (Fredrikson
    & Byron); asking candidates to work through an ambiguous problem (consultant column); and McKinsey's CEO saying the
    firm would look more at liberal arts majors it had deprioritised, because AI models have developed problem-solving
    expertise (HBR Ideacast, as reported by Fortune).
  outcomes:
    - lever: quality
      description: None published. McKinsey's CEO said the firm would be "looking more at liberal arts majors, whom we had deprioritized".
      figure: none published
      measures: n/a
      provenance: self-reported
      source_ref: FORTUNE-MCK-2026
  prerequisites:
    - Interviewers able to judge reasoning rather than answers
    - For tool-based tests, a deployed internal AI tool
  risks_and_guardrails:
    - The Lilli test is reported second-hand by an interview-preparation firm (CaseBasix) and the Financial Times; McKinsey did not confirm it in the article (FORTUNE-MCK-2026)
    - AI used in screening may fall under employment-related high-risk rules (see Module notes, guardrails)
  human_checkpoints:
    - Interviewer assessment of reasoning and collaboration with the tool
  role_evolution: >-
    Recruiters at Robert Half report hiring managers weighing appetite to learn and adaptability alongside technical knowledge (ICAEW-JUNIOR-2026).
  evidence_grade: C
  sources:
    - {ref: FORTUNE-MCK-2026, title: "McKinsey challenges graduates to master AI tools as it shifts hiring hunt toward liberal arts majors", publisher: Fortune, type: press, url: "https://fortune.com/2026/01/14/how-to-get-hired-at-mckinsey-ai-tools-liberal-arts-creativity", date: 2026-01-14, access: full, locator: "Paragraphs 2-5"}
    - {ref: TRI-LAWYERDEV-2026, title: "Rethinking lawyer development in future AI-enabled law firms", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/lawyer-development-ai-enabled-law-firms", date: 2026-04-16, access: full, locator: "Section: Aligning the talent model (Fredrikson recruiting)"}
    - {ref: ICAEW-JUNIOR-2026, title: "Why we still need junior accountants in the age of AI, and how their roles might change", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/apr-2026/why-we-still-need-junior-accountants-and-how-their-role-might-change", date: 2026-04-02, access: full, locator: "Quote from David Shogelola (Robert Half)"}
    - {ref: CONSULTANCYUK-PYRAMID-2026, title: "AI may up-end the consulting pyramid", publisher: Consultancy.uk, type: press, url: "https://www.consultancy.uk/news/43210/ai-may-up-end-the-consulting-pyramid", date: 2026-02-19, access: full, locator: "Opening paragraphs"}
  last_reviewed: 2026-10-19
  notes: >-
    The Fortune item combines a CEO statement (HBR Ideacast) with second-hand reporting. The consultancy.uk opinion piece (a managing partner at Mangrove Consulting) mentions that McKinsey tests recruits on AI capabilities without a source.

- id: professional-services-talent-learning-12
  title: Professional-grade AI access as a recruiting and retention lever
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Firms and departments that deploy general-purpose or no AI risk losing experienced people, who are the most mobile and
    hardest to replace.
  solution: >-
    Treat access to professional-grade AI (verified content, confidentiality, explainable reasoning) and a visible AI
    strategy as part of the talent offer, and discuss AI explicitly in lateral recruiting and retention conversations.
  outcomes:
    - lever: risk
      description: Share who would turn down a role without fiduciary-grade AI.
      figure: "32% vs 12%"
      measures: "32% of professionals who use fiduciary-grade AI would turn down a role that did not offer it; 12% of those without access say the same (TR 2026 survey of 1,816 professionals)"
      provenance: vendor-published
      source_ref: TR-FOP-2026
    - lever: cost
      description: Departure risk and replacement cost.
      figure: "24%; $232,000"
      measures: "24% of professionals experiencing an AI value gap consider leaving within two years (Key findings 06); $232,000 is Thomson Reuters' estimated replacement cost per professional"
      provenance: vendor-published
      source_ref: TR-FOP-2026
  prerequisites:
    - A communicated AI strategy that reaches the desk (35% of professionals with a named strategy say daily practice does not match it)
    - Willingness to give AI decision-makers authority
  risks_and_guardrails:
    - Thomson Reuters sells AI products ("Fiduciary-Grade AI" is its own standard), so the survey has a commercial interest
    - Stated intentions are not observed departures
  human_checkpoints:
    - Recruiters prepared to explain tools, workflow fit, client conversations and career impact (TRI-HIRINGMYTH-2026)
  role_evolution: >-
    Senior lawyers who decide on AI purchases, not juniors, are the likeliest to leave over inadequate tools: 32% of AI decision-makers say they would not accept a job without professional-grade AI, against under 10% of lawyers without decision authority (TRI-HIRINGMYTH-2026).
  evidence_grade: C
  sources:
    - {ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: 2026, access: full, locator: "Key findings 06 and 08; 'The price of departure'"}
    - {ref: TRI-HIRINGMYTH-2026, title: "The AI hiring myth: Why AI decision-makers are the real law firm recruiting risk", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/ai-hiring-myth", date: 2026-08-17, access: full, locator: "Sections: By the numbers; The impact on hiring"}
    - {ref: TRI-STANDARDS-2026, title: "Between accountability and chaos: Setting the AI standards that professionals demand", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/between-accountability-and-chaos", date: 2026-10-12, access: full, locator: "Section: Strategic case for standards"}
  last_reviewed: 2026-10-19
  notes: >-
    The report page shows fieldwork in March-April 2026 but no publication date; "2026" is used. In-house settings are included in the sample (private practice and corporate or government departments).

- id: professional-services-talent-learning-13
  title: AI adoption built into promotion decisions, goals and partner expectations
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Leaders want adoption, but most professionals lack personal goals or clarity on the organisation's AI strategy, and
    senior sceptics slow change.
  solution: >-
    Accenture reportedly began collecting weekly log-ins of senior staff to its AI platforms and told managers and
    associate directors that moving into leadership requires "regular adoption" of AI. PwC's US CEO told the Financial
    Times that staff with an "opportunity to opt out" of AI would not be there long. Thomson Reuters recommends personal
    AI goals linked to business objectives.
  outcomes:
    - lever: speed
      description: Professionals with clearly defined AI goals are more likely to see benefits (correlation from a survey, not a firm result).
      figure: "1.8x; 39%"
      measures: "1.8 times as likely to see tangible organisational benefits (professionals with clearly defined AI goals vs others); 39% of all professionals surveyed have personal goals linked to AI adoption (TR 2025 Future of Professionals survey)"
      provenance: vendor-published
      source_ref: TRI-FOPTALENT-2025
  prerequisites:
    - Internal AI platforms that staff can use regularly (Accenture's tracked tools include its AI Refinery platform)
    - Clear communication of strategy to individuals (65% of those with personal AI goals are unaware of their organisation's AI strategy)
  risks_and_guardrails:
    - Usage tracking can reward log-ins rather than quality; no source measures the effect on output
    - PwC's own January survey of 4,454 business leaders found many saw neither higher revenue nor lower costs from AI (REGISTER-PWC-2026)
  human_checkpoints:
    - Promotion decisions into leadership consider AI adoption (reported); how usage is weighed was not published
  role_evolution: >-
    Partners and senior staff are the target: AI posture becomes part of seniority. Accenture's CEO told investors in September 2025 that people who could not adapt would be "exited" (as reported by Decrypt).
  evidence_grade: B
  sources:
    - {ref: DECRYPT-ACCENTURE-2026, title: "Accenture Is Tracking Whether Employees Use AI, and Promotions Are on the Line", publisher: Decrypt, type: press, url: "https://decrypt.co/358616/accenture-tracking-employees-use-ai-promotions", date: 2026-02-19, access: full, locator: "Paragraphs 1-6"}
    - {ref: REGISTER-PWC-2026, title: "PwC will say goodbye to staff who aren't convinced about AI", publisher: The Register, type: press, url: "https://theregister.com/2026/03/19/pwc_ai", date: 2026-03-19, access: full, locator: "Paragraphs 1-6"}
    - {ref: CIO-PWC-2026, title: "PwC US tells staff to opt out of company, not AI", publisher: CIO, type: press, url: "https://www.cio.com/article/4148222/pwc-us-tells-staff-to-opt-out-of-company-not-ai-2.html", date: 2026-03-20, access: full, locator: "Paragraphs 1-3"}
    - {ref: TRI-FOPTALENT-2025, title: "Future of Professionals: How to maximize the value of AI investments through talent", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/future-of-professionals-maximizing-ai-investment-through-talent", date: 2025-11-17, access: full, locator: "Sections: Clearly communicate organization's AI strategy; Leverage professionals' personal AI use"}
  last_reviewed: 2026-10-19
  notes: >-
    Accenture's account comes from the Financial Times via Decrypt; the memo itself was not seen. Accenture's spokesperson said only that its strategy "requires the adoption of the latest tools". Grade B for named firms with announced practice but no outcome measure; the 1.8x figure is a TR survey correlation (vendor-published) and does not lift the grade.

- id: professional-services-talent-learning-14
  title: Measuring unaided judgment after a period of AI-assisted work (randomised trial design)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [expert-judgment, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: >-
    AI may raise the quality of delivered work while stunting the expertise professionals would otherwise develop
    producing it; firms have no measure of which effect dominates, or for whom.
  solution: >-
    A pre-registered three-month randomised trial gave 133 practising patent lawyers at eleven US IP firms a custom AI
    patent drafting assistant, scored work with blinded expert patent attorneys, and then had all subjects redline an
    existing patent application without AI to test unaided judgment.
  outcomes:
    - lever: quality
      description: AI access raised the quality of delivered drafting work at 10 and 90 days, with larger gains among junior lawyers.
      figure: "+0.34 SD at 10 days; +0.38 SD at 90 days"
      measures: "Standard deviations of blinded expert-attorney quality scores on benchmark patent drafting tasks, AI-access group vs control (abstract)"
      provenance: vendor-published
      source_ref: NBER-AUTOR-2026
    - lever: quality
      description: In the unaided redlining test after three months, treated lawyers outperformed controls, but the advantage was concentrated entirely among seniors; juniors showed no average gain and their scores split into fewer mediocre results and more poor and more good ones.
      figure: "+0.32 SD overall; +0.45 SD seniors; none for juniors on average"
      measures: "Standard deviations of unaided redline scores, treated vs control, all subjects (0.32), senior subgroup (0.45) (abstract)"
      provenance: vendor-published
      source_ref: NBER-AUTOR-2026
  prerequisites:
    - Control group, blinded expert scorers and a defined unaided task
    - Firm cooperation across eleven firms
  risks_and_guardrails:
    - The study was conducted by Google and Google funded the direct costs; five of the seven authors disclose Google employment or contractor ties and the lead author acknowledges Google fellowship support (NBER-AUTOR-2026)
    - One task (patent drafting), one custom assistant, three months; the abstract suggests foundational expertise may be a prerequisite for durable gain, which is the authors' interpretation
  human_checkpoints:
    - Blinded expert patent attorneys scored all work
  role_evolution: >-
    Seniors keep durable skill gains; the authors suggest AI "served as a springboard for some juniors and a cushion for others" (abstract).
  evidence_grade: A
  sources:
    - {ref: NBER-AUTOR-2026, title: "Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting", publisher: NBER (Working Paper 35720), type: academic, url: "https://www.nber.org/papers/w35720", date: 2026-09, access: full, locator: "Abstract and Acknowledgements and Disclosures (full PDF returned HTTP 403)"}
  last_reviewed: 2026-10-19
  notes: >-
    Grade A rests on a measured study, but only the abstract and disclosures were read here, and the use case is a research design rather than reported firm practice. The paper is dated September 2026 (revised October 2026). The landscape recorded the same study as NBER-AUTOR-2026. The "p" values in the abstract were garbled in the page text and are omitted.

- id: professional-services-talent-learning-15
  title: Resize and reshape entry-level intake as AI absorbs junior work (pyramid to diamond)
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [coordination-scheduling, data-reporting]
  pattern: other
  ladder: automate
  change_scope: model
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    The leverage pyramid depended on large cohorts of juniors doing high-volume work at billable rates while training;
    if AI does that work and clients will not pay for junior time, the base of the pyramid has no economic role.
  solution: >-
    Firms plan or make smaller entry-level classes, add experienced and mid-level staff (the "diamond" shape discussed in
    consulting), and shift work offshore or into AI.
  outcomes:
    - lever: cost
      description: US firms with more than 500 lawyers hired fewer law-school graduates in 2025, the first fall since 2011.
      figure: "6,588 hired; down 538 (7.5%)"
      measures: "New graduates hired by firms with more than 500 lawyers in 2025, down from the 2024 peak (NALP data as reported by Bloomberg Law)"
      provenance: independent
      source_ref: BLOOMBERGLAW-HIRING-2026
    - lever: cost
      description: Expectation of smaller junior classes.
      figure: "two-thirds; nearly 60%; 19%"
      measures: "Of 57 large firms in a Citi law firm banking group survey (summer 2026): two-thirds expect fewer first-year associates in 2028 than 2025; nearly 60% expect fewer second-years; 19% answered 'don't know' for 2028 first-year hiring"
      provenance: independent
      source_ref: BLOOMBERGLAW-HIRING-2026
    - lever: cost
      description: UK Big Four graduate intake cuts.
      figure: "KPMG 1,399 to 942; Deloitte -18%; EY -11%; PwC -6%"
      measures: "UK graduate scheme intake reductions over about two years as reported by City AM; PwC UK later said it would recruit 1,300 entrants against 1,500 the previous year and that the economy was the single biggest factor (PEOPLEMATTERS-PWC-2025)"
      provenance: self-reported
      source_ref: CITYAM-BIG4-2025
    - lever: cost
      description: Employment of 22-25 year olds in AI-exposed occupations is below trend in US payroll data (cross-economy, not professional services specifically).
      figure: "19% below"
      measures: "Employment of workers aged 22-25 in AI-exposed occupations compared with where it would be had it kept pace with less-exposed peers (ADP payroll data through June 2026; revised paper)"
      provenance: independent
      source_ref: STANFORD-CANARIES-2026
  prerequisites:
    - A view on how many juniors are needed to produce future seniors
    - Offshoring or sourcing capacity if work moves rather than disappears
  risks_and_guardrails:
    - Attribution to AI is contested: PwC UK cited the economy; ICAEW says "it's unclear how much the growth of AI contributed" given offshoring and cost reduction (ICAEW-WORRIED-2026)
    - Stanford authors note the patterns attenuate when controlling for education and show some trends predating generative AI
    - 2008 precedent: firms that closed inbound apprenticeships struggled with management talent about five years later (ICAEW-JUNIOR-2026)
  human_checkpoints:
    - Partner and board decisions on class size; annual review against demand
  role_evolution: >-
    "The pyramid model is dead" is a Reddit commenter's view (LEGALCHEEK-REDDIT-2026); Bloomberg Law's columnist notes firms' own AI uncertainty is now driving first-year plans (BLOOMBERGLAW-HIRING-2026). Equity partner headcount at large firms fell 0.5% while leverage rose 4.3% in the first nine months of 2025 (BCG Attorney Search via VAULT-PYRAMID-2026).
  evidence_grade: B
  sources:
    - {ref: BLOOMBERGLAW-HIRING-2026, title: "Big Law First-Year Hiring Set to Plunge as History, AI Collide", publisher: Bloomberg Law (Big Law Business column, Roy Strom), type: press, url: "https://news.bgov.com/business-and-practice/big-law-first-year-hiring-set-to-plunge-as-history-ai-collide", date: 2026-09-10, access: full, locator: "Paragraphs 3-9"}
    - {ref: CITYAM-BIG4-2025, title: "Big Four slash graduate jobs as AI takes on entry level work", publisher: City AM, type: press, url: "https://www.cityam.com/?p=2342067", date: 2025-06-23, access: full, locator: "Paragraphs 1-4"}
    - {ref: PEOPLEMATTERS-PWC-2025, title: "PwC reduces entry-level recruitment as economy slows and AI reshapes jobs", publisher: People Matters, type: press, url: "https://www.peoplematters.in/news/hr-effectiveness/pwc-reduces-entry-level-recruitment-as-economy-slows-and-ai-reshapes-jobs-43454", date: 2025-09-09, access: full, locator: "Paragraphs 2-6 (including PwC US cut by a third by 2028, reported from internal documents)"}
    - {ref: STANFORD-CANARIES-2026, title: "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence", publisher: Stanford Digital Economy Lab, type: academic, url: "https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/", date: 2026-08-12, access: full, locator: "Abstract (revised 2026-08-12)"}
    - {ref: VAULT-PYRAMID-2026, title: "The Compressed Pyramid: What AI Means for the Associate Career Ladder", publisher: Vault, type: press, url: "https://legacy.vault.com/blogs/vaults-law-blog-legal-careers-and-industry-news/the-compressed-pyramid-what-ai-means-for-the-associate-career-ladder", date: 2026-08-11, access: full, locator: "Paragraphs 2-6"}
    - {ref: ICAEW-WORRIED-2026, title: "AI: are junior accountants worried about roles?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/jun-2026/ai-are-junior-accountants-worried-about-roles", date: 2026-06, access: full, locator: "Opening paragraphs (68% of mid-tier firms expect AI to reduce need for some early-career roles)"}
    - {ref: LEGALCHEEK-REDDIT-2026, title: "Junior lawyers split: Is AI 'eating' their jobs, or just an above-average paralegal?", publisher: Legal Cheek (reporting an r/biglaw thread), type: community, url: "https://www.legalcheek.com/2026/07/junior-lawyers-divided-over-whether-ai-is-eating-their-jobs-or-just-cutting-the-boring-bits/amp/", date: 2026-07-08, access: full, locator: "Paragraphs 2-4"}
  last_reviewed: 2026-10-19
  notes: >-
    Grade B: named firms and datasets, but no measure isolates AI as the cause. City AM's headline range ("as much as 29 per cent") does not match its own KPMG figures, which imply a fall of about a third; both are reported as published. The Stanford result is cross-economy (adjacent) and would cap the grade at B on its own. A Slashdot summary of Financial Times and Management Consulted reporting (2025-12-01) says McKinsey, BCG and Bain starting salaries are frozen for a third year and that two unnamed Big Four executives estimated UK graduate recruitment would fall by about half; that estimate is anonymous and secondary, so it is kept out of the outcomes (SLASHDOT-CONSULTING-2025). The landscape's Citi figure is confirmed at source; its BCG Attorney Search figures appear in use case 16.

- id: professional-services-talent-learning-16
  title: Lateral-first and experienced-hire sourcing in place of training from entry level
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    If entry-level work no longer produces future seniors cheaply, firms may buy experience instead of building it, which
    moves the training cost onto other employers and thins the future pipeline.
  solution: >-
    Grow associate ranks through lateral hires and mid-career specialists. In consulting, one managing partner argues
    firms may hire people who have developed sector expertise elsewhere ("specialise first, then move into consulting").
  outcomes:
    - lever: capacity
      description: Laterals outnumbered entry-level hires among Am Law 200 associate hires, and large firms plan more associates but fewer first-years.
      figure: "51%; 86% vs 35%"
      measures: "Lateral associates as a share of Am Law 200 associate hires last year (SurePoint study, as cited by Vault); share of large firms planning to grow overall associate ranks through 2027 (86%) vs share planning larger first-year classes (35%) (BCG Attorney Search 2026 report, as cited by Vault)"
      provenance: vendor-published
      source_ref: VAULT-PYRAMID-2026
  prerequisites:
    - Lateral market supply and integration capacity (TRI-CMBDO-2026 panelists say firms often fail to integrate laterals)
  risks_and_guardrails:
    - Figures are second-hand through Vault; the SurePoint and BCG originals were not opened
    - Free-rider problem: if everyone buys experience, who trains juniors (consultancy.uk, Vault)
  human_checkpoints:
    - Single point of coordination for lateral onboarding (TRI-CMBDO-2026)
  role_evolution: >-
    A consulting career path that inverts, with industry first and consulting later (CONSULTANCYUK-PYRAMID-2026; opinion).
  evidence_grade: C
  sources:
    - {ref: VAULT-PYRAMID-2026, title: "The Compressed Pyramid: What AI Means for the Associate Career Ladder", publisher: Vault, type: press, url: "https://legacy.vault.com/blogs/vaults-law-blog-legal-careers-and-industry-news/the-compressed-pyramid-what-ai-means-for-the-associate-career-ladder", date: 2026-08-11, access: full, locator: "Paragraph 2 (SurePoint) and paragraph 3 (BCG Attorney Search)"}
    - {ref: CONSULTANCYUK-PYRAMID-2026, title: "AI may up-end the consulting pyramid", publisher: Consultancy.uk, type: press, url: "https://www.consultancy.uk/news/43210/ai-may-up-end-the-consulting-pyramid", date: 2026-02-19, access: full, locator: "Sections: The shape of things to come; The graduate question"}
    - {ref: TRI-CMBDO-2026, title: "Chief Marketing & Business Development Officer Forum 2026: Law firms need to play the long game on talent", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-long-game-on-talent", date: 2026-02-06, access: full, locator: "Section: The strategy behind making lateral integration work"}
  last_reviewed: 2026-10-19
  notes: >-
    Lateral hiring is also driven by market factors unrelated to AI; Vault does not attribute the lateral share to AI.

- id: professional-services-talent-learning-17
  title: Keep (or grow) entry-level intake while redesigning the role
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Cutting the intake saves cost now but risks a shortage of managers later and loses AI-fluent young hires; yet managers
    already struggle to find meaningful work for juniors.
  solution: >-
    McKinsey said it planned to expand North American headcount 12% in 2026 and that fears of AI hollowing out entry-level
    roles were misplaced; the Big Four each plan at least 1,000 UK junior hires, with EY expecting 1,600; EY and PwC US
    doubled the bonus for entry-level hires who complete all four CPA exam parts to $10,000.
  outcomes:
    - lever: capacity
      description: McKinsey plans to grow its North American workforce 12% in 2026 over 2025; its chair said non-partner staff, now 5,000 to 7,000, could rise 15% to 20% over five years.
      figure: "12%; 15-20%"
      measures: "Planned growth in McKinsey's North American workforce in 2026 versus 2025 (as reported from Reuters; not graduate-only); possible growth in non-partner staff over five years"
      provenance: self-reported
      source_ref: PEOPLEMATTERS-MCK-2025
    - lever: capacity
      description: Big Four UK junior hiring plans for 2026.
      figure: "at least 1,000 each; EY 1,600"
      measures: "Planned junior hires this year per firm (ICAEW article, April 2026; the article does not state the country, context is UK)"
      provenance: self-reported
      source_ref: ICAEW-JUNIOR-2026
  prerequisites:
    - A role for juniors that managers can supervise ("even more oversight")
    - Willingness to carry the cost of development
  risks_and_guardrails:
    - A mid-tier firm partner said a client told them junior hours were too high and AI should reduce them (ICAEW-EXPECT-2026), so client pressure may still force cuts
    - McKinsey's 12% is for the whole North American workforce, not graduates, though some coverage framed it as graduate hiring
  human_checkpoints:
    - Annual intake decision against demand and client pressure
  role_evolution: >-
    A talent consultant quoted by ICAEW says AI is removing the work managers used to give juniors, which worsens an existing problem and demands more oversight (ICAEW-JUNIOR-2026).
  evidence_grade: C
  sources:
    - {ref: PEOPLEMATTERS-MCK-2025, title: "McKinsey rejects AI job fears, to boost hiring by 12% in 2026", publisher: People Matters (citing Reuters and WSJ), type: press, url: "https://www.peoplematters.in/news/strategic-hr/mckinsey-rejects-ai-job-fears-to-boost-hiring-by-12percent-in-2026-43536", date: 2025-09-12, access: full, locator: "Paragraphs 1-6"}
    - {ref: ICAEW-JUNIOR-2026, title: "Why we still need junior accountants in the age of AI, and how their roles might change", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/apr-2026/why-we-still-need-junior-accountants-and-how-their-role-might-change", date: 2026-04-02, access: full, locator: "Paragraphs 1-4"}
    - {ref: CPAPA-STOP-2026, title: "Stop Training CPAs for Yesterday's Work", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/09/02/stop-training-cpas-for-yesterdays-work/189548/", date: 2026-09-02, access: full, locator: "Paragraph 1"}
    - {ref: ICAEW-EXPECT-2026, title: "Are businesses expecting too much of AI?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/feb-2026/are-businesses-expecting-too-much-of-ai", date: 2026-02, access: full, locator: "Opening paragraphs (anonymous mid-tier partner)"}
  last_reviewed: 2026-10-19
  notes: >-
    Announcements and plans only; no realised 2026 intake figures were found for McKinsey or the Big Four.

- id: professional-services-talent-learning-18
  title: Firmwide AI training, with access gated on completion
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Many professionals use AI without training or policy; adoption outruns governance and skill, especially in smaller
    firms.
  solution: >-
    Mandatory training before tool access (policy), firm-run academies, tool-specific sessions, prompt-engineering
    workshops, and tuition for incoming trainees. Examples: Latham's AI Academy with a mandatory two-day in-person
    associate training; Accenture's training of about 550,000 employees in generative AI; Freshfields paying for incoming
    trainees' LLM in law and technology.
  outcomes:
    - lever: risk
      description: Share of firms with a policy requiring specific training before use rises steeply with firm size.
      figure: "11% (under 50 lawyers) to 72% (over 700 lawyers)"
      measures: "Share of responding firms whose official GenAI policy or guidance includes 'Specific training required before use' (ILTA Q3.18; 508 firms overall), by number of lawyers"
      provenance: independent
      source_ref: ILTA-TECHSURVEY-2026
    - lever: capacity
      description: Accenture trained a majority of staff in generative AI and commits $1 billion a year to learning programmes (reported).
      figure: "550,000 of 780,000"
      measures: "Employees Accenture trained in generative AI, as reported by Decrypt; original Accenture statement not opened"
      provenance: self-reported
      source_ref: DECRYPT-ACCENTURE-2026
  prerequisites:
    - A formal GenAI policy (57% of firms under 50 lawyers have one, versus 91-98% of firms over 350)
    - Budget for headcount in training, innovation, KM and data science (ILTA-TECHSURVEY-2026)
  risks_and_guardrails:
    - Karbon reports fewer than half of accounting firms invest in AI training for staff and only 21% have a documented AI policy or strategy (vendor survey; sample not captured)
    - Training that teaches only tool functions misses the judgment layer (TR-FOP-2026)
  human_checkpoints:
    - Training completion as an access gate
  role_evolution: >-
    New training and innovation roles appear: ILTA says many firms expect added headcount in IT, innovation, security, training, knowledge management and data science.
  evidence_grade: B
  sources:
    - {ref: ILTA-TECHSURVEY-2026, title: "The ILTA Technology Survey 2026 Executive Summary", publisher: ILTA, type: professional-body, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026-06, access: full, locator: "p.5 table Q3.18 and text on training and headcount"}
    - {ref: DECRYPT-ACCENTURE-2026, title: "Accenture Is Tracking Whether Employees Use AI, and Promotions Are on the Line", publisher: Decrypt, type: press, url: "https://decrypt.co/358616/accenture-tracking-employees-use-ai-promotions", date: 2026-02-19, access: full, locator: "Paragraph 6"}
    - {ref: NONBILLABLE-RG-2026, title: "Ropes & Gray gives junior lawyers 20% of billable time for AI work", publisher: Non-Billable, type: press, url: "https://www.nonbillable.co.uk/news/ropes-gray-gives-junior-lawyers-20-of-billable-time-for-ai-work", date: 2026, access: full, locator: "Final two paragraphs (Freshfields; Latham AI Academy)"}
    - {ref: KARBON-JUNIOR-2026, title: "How do junior accountants learn when AI does the grunt work?", publisher: Karbon Magazine, type: vendor, url: "https://karbonhq.com/resources/training-junior-accountants-ai/", date: 2026-04-30, access: full, locator: "Section: The profession is asking the question out loud"}
    - {ref: TRI-GENAITALENT-2024, title: "GenAI in the legal industry: Where it's already impacting legal talent management", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/genai-legal-talent", date: 2024-11-04, access: full, locator: "Section: Training is crucial (18% of law firm respondents had received GenAI training; older baseline)"}
  last_reviewed: 2026-10-19
  notes: >-
    Grade B: named firms (Latham, Accenture, Freshfields) and a professional-body survey, but no outcome measures for the training itself. Latham and Freshfields appear only as second-hand mentions in Non-Billable. The Accenture count is secondary.

- id: professional-services-talent-learning-19
  title: "Idea: independent-reasoning checks (challengers, own-words reconstruction, AI-off days)"
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [review-assurance, expert-judgment]
  pattern: draft-review-loop
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    When AI drafts arrive early and look complete, teams can accept the framing without examining what was omitted, and
    individuals may drift into passive editing of machine output.
  solution: >-
    Assign a challenger to AI-generated work, require team members to set the AI output aside and reconstruct, challenge
    and defend the reasoning in their own words, return to primary sources, run "AI-off days" or agency stress tests for
    critical teams, and document what a junior challenged and why.
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: n/a
      provenance: self-reported
      source_ref: TRI-DESIGNJUDG-2026
  prerequisites:
    - Defined tasks that are never delegated to AI (high-stakes decisions, values-based trade-offs, people evaluations)
    - Tracking of override patterns
  risks_and_guardrails:
    - Reported "cognitive offloading" evidence cited is from outside the professions (an MIT Media Lab study on ChatGPT use, as cited by TRI-COGDEBT-2025); none specific to professional services
  human_checkpoints:
    - Reasoning reconstruction and challenge by someone other than the drafter
  role_evolution: >-
    Performance metrics should reward collaboration, quality judgment and rapid learning, not only throughput (TRI-COGDEBT-2025).
  evidence_grade: D
  sources:
    - {ref: TRI-DESIGNJUDG-2026, title: "Designing judgment: Preserving AI-mediated legal collaboration", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/designing-judgment-ai-mediated-legal-collaboration", date: 2026-10-06, access: full, locator: "Sections: Delegation versus collaboration; key insights"}
    - {ref: TRI-COGDEBT-2025, title: "As AI usage accelerates, companies need to avoid cognitive debt & decay among their talent", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/avoiding-cognitive-debt-agency-decay", date: 2025-10-15, access: full, locator: "Section: Pairing human/AI intelligence"}
    - {ref: TRI-STANDARDS-2026, title: "Between accountability and chaos: Setting the AI standards that professionals demand", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/between-accountability-and-chaos", date: 2026-10-12, access: full, locator: "Section: Judgment validation standard"}
  last_reviewed: 2026-10-19
  notes: >-
    Idea (grade D): proposals by TRI authors and an academic; no firm reported using these checks.

- id: professional-services-talent-learning-20
  title: "Idea: residency-style supervised practice and a funded profession-wide formation system"
  archetype: professional-services
  module: talent-learning
  function: people-hr
  work_types: [expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Law schools teach how to think and firms teach how to practise, but AI reduces the availability of traditional first
    jobs, and the profession has no agreed definition of legal judgment or standards for AI use in training.
  solution: >-
    A Thomson Reuters Institute white paper proposes work-based learning modelled on medical residencies (with the
    Brookings Institution's earlier proposal), decomposing legal judgment into teachable micro-skills, and using AI as a
    thinking partner throughout; funding could come from a small percentage of legal services revenue. Existing models
    cited: Northeastern Law's near-year of guaranteed work experience and UNH Franklin Pierce's Daniel Webster Scholar
    programme.
  outcomes:
    - lever: experience
      description: none published
      figure: none published
      measures: n/a
      provenance: self-reported
      source_ref: TRI-HONING-2026
  prerequisites:
    - Coordination among law schools, legal employers and state supreme courts as regulators
    - Funding mechanism
  risks_and_guardrails:
    - Implementation needs "unprecedented coordination and funding" (TRI-HONING-2026 key insights)
  human_checkpoints:
    - Supervised postgraduate practice as part of licensure (proposed)
  role_evolution: >-
    Juniors would be formed through structured supervised practice rather than through billable repetition.
  evidence_grade: D
  sources:
    - {ref: TRI-HONING-2026, title: "Honing legal judgment: The AI era requires changes to how lawyers are trained during and after law school", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/honing-legal-judgment-training-lawyers", date: 2026-04-02, access: full, locator: "Opening paragraph; Pillar 1"}
  last_reviewed: 2026-10-19
  notes: >-
    Idea (grade D). Partly a regulatory and education proposal, so the governance angle of this module is the better home for follow-up.
```

## 3. Module notes

**Processes and key steps (work types)**

- Intake planning and class sizing: how many juniors to hire, which work they will do (coordination-scheduling, data-reporting).
- Recruiting and assessment, including lateral hiring (review-assurance, expert-judgment).
- Onboarding and orientation (coordination-scheduling).
- Learning through client work: first drafts, diligence, review, research, deposition preparation (document-production, expert-judgment). This is the step AI is absorbing.
- Formal training, simulation and CPE (expert-judgment).
- Feedback, evaluation and promotion (review-assurance, expert-judgment).
- Career-path and role design: leverage ratio, new hybrid roles (coordination-scheduling).
- Retention and lateral integration (coordination-scheduling).

**Common pain points**

- The training ground and the billing base are the same work. Two professors quoted by Vault said junior work "has always served two purposes: billing and training" (VAULT-PYRAMID-2026).
- No agreed definition of legal judgment, so firms cannot say which tasks are essential to retain (TRI-HONING-2026; TRI-SEYFARTH-2026 says expertise formation beliefs are "largely inferential").
- Managers cannot find meaningful work for juniors (ICAEW-JUNIOR-2026).
- Associates form AI habits ahead of firm guidance (TRI-ONBOARD-2026).
- Clients do not want to pay for junior-completed tasks and are bringing near-final work in-house (TRI-LAWYERDEV-2026).

**Metrics and benchmarks (with sources)**

| Metric | Value | What it measures | Source |
|---|---|---|---|
| Large-firm graduate hiring | 6,588 hired, down 7.5% from 2024 | New graduates hired by US firms with more than 500 lawyers in 2025 (NALP) | BLOOMBERGLAW-HIRING-2026 |
| Expected first-year cuts | two-thirds; 19% unsure | Share of 57 large firms expecting fewer first-years in 2028 than 2025; share answering "don't know" | BLOOMBERGLAW-HIRING-2026 |
| Planned growth | 86% vs 35% | Large firms planning more associates through 2027 vs larger first-year classes (BCG Attorney Search 2026, second-hand) | VAULT-PYRAMID-2026 |
| UK Big Four graduate intake | KPMG 1,399 to 942; Deloitte -18%; EY -11%; PwC -6% | Reductions over about two years | CITYAM-BIG4-2025 |
| Fear for judgment development | 48%; 45% for learning through experience; 28% for mentorship quality | Share of professionals concerned | TR-FOP-2026 |
| Need for structured support | 71% | Professionals who believe early-career roles need structured support from experienced peers | TR-FOP-2026 |
| Time to trusted judgment | legal: stretch of about 1.7 years; tax: shorten by 1.0 year | Professionals' expectation by profession | TR-FOP-2026 |
| Training before access | 11% to 72% | By firm size, ILTA Q3.18 | ILTA-TECHSURVEY-2026 |
| Leverage and partner counts | equity partners -0.5%; leverage +4.3% | Large firms, first nine months of 2025 (BCG Attorney Search, second-hand) | VAULT-PYRAMID-2026 |
| Accounting pipeline | enrolment +8.9% spring 2026; interns converted 63.1% (NACE 2024-25) | AICPA enrolment data and NACE conversion, quoted in a trade article | CPAPA-SKILLS-2026 |

**Guardrails and regulatory points**

- Supervision duties scale with AI autonomy in California's State Bar guidance (CALBAR-GENAI-2026, carried from the landscape; not re-opened this run). Relevant because juniors who supervise AI are the supervision layer.
- The EU AI Act treats employment uses (recruitment, evaluation, task allocation) as high-risk, with Annex III obligations delayed to 2 December 2027 under the Omnibus per the landscape (EC-AIACT-2026, carried from the landscape; not re-opened). No discourse source discussed AI-driven screening or evaluation of staff in these firms.
- Incidents cited in the discourse: a Pinsent Masons junior lawyer's AI-assisted research led to citing a non-existent insolvency rule, criticised by a High Court judge; Sullivan & Cromwell apologised to a New York court for AI-hallucinated citations (LEGALCHEEK-REDDIT-2026, reported not verified at source).
- Standards gap: 47% of professionals say they hold responsibility for AI-assisted work while two in five lack professional-grade systems (TRI-STANDARDS-2026).

**Frontier signals (dated, sourced)**

- 2026-10-16: A TRI series says firms should hire for curiosity and "figure-it-out" ability and measure first-two-year milestones, not time served (TRI-TAX2030-2026).
- 2026-10-12: Duane Morris describes year-round onboarding with practice-group AI champions (TRI-ONBOARD-2026).
- 2026-09 (revised 2026-10): NBER trial finds unaided-skill gains concentrated in seniors (NBER-AUTOR-2026).
- 2026-09-10: Citi survey - two-thirds of large firms expect fewer first-years in 2028 than 2025 (BLOOMBERGLAW-HIRING-2026).
- 2026-08-12: Stanford revised paper - 22 to 25 year olds in AI-exposed occupations 19% below trend, no widespread displacement (STANFORD-CANARIES-2026).
- 2026-08-11: Vault says 2026 is the first year several independent data sources agree the shift is visible (VAULT-PYRAMID-2026).
- 2026-07-06 and 2026-07-08: a second-year's r/biglaw post draws hundreds of comments on "rubber stamping" and "the ladder is burning" (NONBILLABLE-REDDIT-2026; LEGALCHEEK-REDDIT-2026).
- 2026-04-30: Karbon says fewer than half of accounting firms invest in AI training for staff (KARBON-JUNIOR-2026).
- 2026-03-19: Legalweek 2026 puts the junior lawyer on the main stage (TRI-LEGALWEEK-ASSOC-2026).
- 2026-03-01: Journal of Accountancy cover story; AICPA "Profession Ready" findings expected in 2027 (JOFA-LEARN-2026).
- 2026-02 to 2026-03: Accenture links leadership promotion to AI adoption; PwC US CEO says staff cannot opt out (DECRYPT-ACCENTURE-2026; REGISTER-PWC-2026).
- 2025-11-19: Ropes & Gray announces billable-credited AI time for first-years (LEGALCHEEK-RG-2025).

**Workforce and role effects**

- Legal and tax professionals expect opposite effects on time to trusted judgment (TR-FOP-2026).
- Juniors move toward review, oversight, operations, data and early client exposure (BI-PWC-2025; TRI-AILAWPROF-JUNIOR-2026).
- Mid-career professionals are the most mobile, AI-engaged and impatient (TR-FOP-2026).
- Associates who build agents unaided are ahead of firm guidance (TRI-ONBOARD-2026).
- Senior lawyers with AI purchasing authority are the highest flight risk over inadequate tools (TRI-HIRINGMYTH-2026).
- Consulting may shift to "diamond" shape; hiring more juniors is "counterproductive" in one managing partner's view (CONSULTANCYUK-PYRAMID-2026).
- The Big Four expect to hire juniors but with a different job (ICAEW-JUNIOR-2026).

**Objections and concerns practitioners raise**

- "Different, not wrong": every generation learned differently, and associates still must read, review and think (Zarwin Baum's managing director, TRI-LEGALWEEK-ASSOC-2026).
- Category error: the purpose of juniors is capacity, risk reduction and pipeline, not particular tasks (TRI-AILAWPROF-JUNIOR-2026).
- Doubt that AI is ready: Harvey and Legora reportedly "fail miserably" on some simple document tasks; leading tools are "an above average paralegal" (LEGALCHEEK-REDDIT-2026, NONBILLABLE-REDDIT-2026).
- Cause is mixed: economy, offshoring and cost, not only AI (CITYAM-BIG4-2025; PEOPLEMATTERS-PWC-2025; ICAEW-WORRIED-2026).
- Evidence quality: surveys are by AI vendors (Thomson Reuters, Karbon); the one trial is Google-run.
- Usage mandates may reward log-ins rather than judgment (author inference from DECRYPT-ACCENTURE-2026; no source measures this).
- Training in tool functions does not teach when to override (TR-FOP-2026).
- Clients: some demand AI use yet refuse to pay for AI-done work (TRI-LEGALWEEK-2026).

**Conference, podcast and community signals**

- Legalweek 2026: due diligence on some financial contracts already compressed to about two hours from 15 to 20, with zero hours "a realistic possibility" (DLA Piper's Barclay Blair, TRI-LEGALWEEK-ASSOC-2026); firms say they are "still gathering the data" on AI savings (TRI-LEGALWEEK-2026).
- Law Firm COO & CFO Forum (24th, Nov 2025): training lawyers was one of several competing priorities, alongside data, metrics and pricing (TRI-COOCFO-2025). The 25th Forum is scheduled for 21-22 October 2026 (landscape; not yet held).
- AICPA ENGAGE 2026 (8-11 June): sessions listed on attracting younger talent and on talent as a driver of firm change (KARBON-ENGAGE-2026, preview of scheduled sessions); the pre-conference think tank listed talent pipeline among topics (CPAPA-ENGAGE-THINKTANK-2026). Session content was not found.
- Podcasts (show notes only): AI and the Future of Law episode 28 (hosts discuss the remark that "the apprenticeship model broke this summer"; ADR-AIFL-EP28-2025); Harbor's Legal Soundings episode 1 on the first-year apprenticeship and simulated environments (HARBOR-LEGALSOUNDINGS-2026); Allens speakers on supervision and mentoring (LIV-CROSSEXAMINED-2026); a Lawyers Weekly episode arguing the fear is overblown (LAWYERSWEEKLY-2026, search-only).
- Community: an r/biglaw thread drew hundreds of comments; positions ranged from "we're all cooked" to "an above average paralegal" (NONBILLABLE-REDDIT-2026; LEGALCHEEK-REDDIT-2026).
- UK consulting: the MCA's foreword to its 2026 member survey flags concern about training quality under hybrid working (MCA-SURVEY-2026, landing page). Karbon reports 98% of accounting professionals use AI (KARBON-SOAI-2026, landing page; report gated). Also see TRI-JUDGMENTGAP-2026 on a "K-shaped" outcome in which experienced professionals gain from AI while entry-level workers lose skill-building experiences.
- Counter-signal on supply: AICPA data quoted by a trade article show accounting enrolment up 8.9% in spring 2026 (CPAPA-SKILLS-2026).

**Interview probes for an advisor**

1. Which tasks did your first- and second-years do three years ago that no longer exist, and what replaced them as the way they learn to judge work?
2. How do you know a junior who reviews AI output can tell when it is wrong? What do you check, and how often does it catch a problem?
3. How many entrants did you plan for this year versus three years ago, and which of the reasons was AI, the economy, or client fee pressure?
4. What counts toward a promotion now that did not before (AI use, review quality, client exposure), and who decides?
5. If your most senior lawyers were asked to give up one habit of the old apprenticeship, which would they refuse to give up, and what would you do about mentoring capacity?

## 4. Routed to other modules

- **staffing-resourcing:** The Kantata/RMI study (KANTATA-RMI-2026) found 52.7% of respondents not equipped to manage hybrid human-agent teams and only 4% well equipped; the sample is 44 organisations across several industries (the landscape did not record this), and Kantata sells the product. Also TRI-HUMANAGENT-2025: 64% of IT leaders surveyed expect HR and IT to merge within five years, and performance and career progression for hybrid teams are undefined.
- **scoping-pricing:** Clients' reluctance to pay for junior-completed tasks (TRI-LAWYERDEV-2026); "we were told our junior hours were too high" and a fee reduction demand (ICAEW-EXPECT-2026); three business-model paths (Fredrikson, TRI-LAWYERDEV-2026).
- **firm-finance:** Leverage and equity-partner counts (VAULT-PYRAMID-2026); frozen consulting starting salaries (SLASHDOT-CONSULTING-2025, secondary); Crowe-KKR employee ownership (landscape AT-CROWE-2026).
- **quality-review:** Hallucinated-citation incidents (LEGALCHEEK-REDDIT-2026); judgment validation and override tracking standards (TRI-STANDARDS-2026); "rubber stamping" concern.
- **knowledge-management:** High Rock Accounting's idea of an assistant grounded in firm reconciliations as a training aid (JOFA-LEARN-2026); legal data and knowledge curator roles (TRI-AILAWPROF-JUNIOR-2026); embedding lawyers' knowledge in AI workflows (VAULT-PYRAMID-2026).
- **delivery-management / sourcing:** Offshoring to India, Malaysia and the Philippines alongside intake cuts (CITYAM-BIG4-2025).
- **client-development:** TRI-AIFORUM-2026 (in-house): corporate legal clients say judgment, transparency and speed now separate firms, and some work moves in-house.
- **in-house:** TRI-AIFORUM-2026 and the TRI "AI success pyramid for corporate legal departments" (2026-07-09, read in part) frame AI success as a skills strategy for in-house teams; no in-house talent case study was found.

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? (WP 35720) | NBER | academic | https://www.nber.org/papers/w35720 | 2026-09 | full (abstract; PDF 403) |
| STANFORD-CANARIES-2026 | Canaries in the Coal Mine? | Stanford Digital Economy Lab | academic | https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/ | 2026-08-12 | full (abstract) |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 (fieldwork Mar-Apr 2026) | full |
| ILTA-TECHSURVEY-2026 | ILTA Technology Survey 2026 Executive Summary | ILTA | professional-body | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 | full |
| MCA-SURVEY-2026 | MCA Member Survey 2026 | MCA | professional-body | https://www.mca.org.uk/reports/mca-member-survey-2026 | 2026-01-20 | full (landing page only; foreword notes concern about training quality with hybrid working) |
| JOFA-LEARN-2026 | How will accountants learn new skills when AI does the work? | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/ | 2026-03-01 | full |
| ICAEW-JUNIOR-2026 | Why we still need junior accountants in the age of AI | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/apr-2026/why-we-still-need-junior-accountants-and-how-their-role-might-change | 2026-04-02 | full |
| ICAEW-WORRIED-2026 | AI: are junior accountants worried about roles? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/jun-2026/ai-are-junior-accountants-worried-about-roles | 2026-06 | full |
| ICAEW-EXPECT-2026 | Are businesses expecting too much of AI? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/feb-2026/are-businesses-expecting-too-much-of-ai | 2026-02 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026 | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-LEGALWEEK-ASSOC-2026 | Legalweek 2026 has found a new existential crisis | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-new-existential-crisis | 2026-03-19 | full |
| TRI-CMBDO-2026 | CMBDO Forum 2026: long game on talent | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/cmbdo-forum-2026-long-game-on-talent | 2026-02-06 | full |
| TRI-COOCFO-2025 | Law Firm COO & CFO Forum: AI solutions and demonstrating value (24th Forum) | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/coo-cfo-forum-ai-solutions-demonstrating-value | 2025-11-03 | full (training is one of several priorities; no talent detail used) |
| TRI-AIFORUM-2026 | 2026 Future of AI & Technology Forum: What AI can't replace (in-house) | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/what-ai-cant-replace | 2026-09-28 | full |
| KARBON-ENGAGE-2026 | 23 must-see sessions at AICPA & CIMA ENGAGE 2026 | Karbon Magazine | conference | https://karbonhq.com/resources/aicpa-cima-engage-2026/ | 2026-05-21 | full (preview of scheduled sessions, e.g. attracting younger talent; no session content) |
| CPAPA-ENGAGE-THINKTANK-2026 | Accounting Thought Leaders Look to the Future of the Profession at AICPA ENGAGE | CPA Practice Advisor | conference | https://www.cpapracticeadvisor.com/2026/06/07/accounting-thought-leader-think-tank-looks-to-the-future-of-the-profession-at-aicpa-engage/184673/ | 2026-06-08 | full (agenda only: talent among topics) |
| CPATRENDLINES-ENGAGE-2026 | At ENGAGE 2026, a Profession Richer and Less Certain Than Ever | CPA Trendlines | conference | https://cpatrendlines.com/2026/06/01/at-engage-2026-a-profession-richer-and-less-certain-than-ever/ | 2026-06-01 | search-only (paywalled teaser) |
| TRI-ONBOARD-2026 | Law firms need to redesign new attorney onboarding for the AI era | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding | 2026-10-12 | full |
| TRI-AILAWPROF-JUNIOR-2026 | The AI Law Professor: rethink how we train junior lawyers | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/ai-law-professor-train-junior-lawyers | 2026-02-02 | full |
| TRI-LAWYERDEV-2026 | Rethinking lawyer development in future AI-enabled law firms | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/lawyer-development-ai-enabled-law-firms | 2026-04-16 | full |
| TRI-SIM-2026 | How AI simulation could reshape legal training and education | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/ai-simulation-legal-training | 2026-05-15 | full |
| TRI-SEYFARTH-2026 | Designing lawyers: Attorney growth in the age of AI-fueled practice | Thomson Reuters Institute (Seyfarth Shaw) | press | https://www.thomsonreuters.com/en/institute/articles/designing-lawyers-professional-growth | 2026-05-11 | full |
| TRI-JUDGMENTGAP-2026 | The professional judgment gap | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/ai-professional-judgment-gap | 2026-03-05 | full (K-shaped argument: entry-level workers lose skill-building; used in objections only) |
| TRI-HONING-2026 | Honing legal judgment | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/honing-legal-judgment-training-lawyers | 2026-04-02 | full |
| TRI-HIRINGMYTH-2026 | The AI hiring myth | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/ai-hiring-myth | 2026-08-17 | full |
| TRI-TAX2030-2026 | The tax, accounting & audit firm of 2030: Building the people | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/tax-audit-accounting-firm-of-2030-building-people-for-tomorrow | 2026-10-16 | full |
| TRI-STANDARDS-2026 | Between accountability and chaos | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/between-accountability-and-chaos | 2026-10-12 | full |
| TRI-DESIGNJUDG-2026 | Designing judgment | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/designing-judgment-ai-mediated-legal-collaboration | 2026-10-06 | full |
| TRI-AIUNDERGRADS-2026 | From AI users to AI thinkers | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/ai-needs-accounting-undergrads | 2026-07-21 | full |
| TRI-FOPTALENT-2025 | Future of Professionals: maximize the value of AI investments through talent | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/future-of-professionals-maximizing-ai-investment-through-talent | 2025-11-17 | full |
| TRI-HUMANAGENT-2025 | How companies are fostering the creation of human & AI agent teams | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/creating-human-ai-agent-teams | 2025-10-22 | full |
| TRI-COGDEBT-2025 | Avoid cognitive debt & decay among talent | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/avoiding-cognitive-debt-agency-decay | 2025-10-15 | full |
| TRI-GENAITALENT-2024 | GenAI in the legal industry: legal talent management | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/genai-legal-talent | 2024-11-04 | full (foundation) |
| BLOOMBERGLAW-HIRING-2026 | Big Law First-Year Hiring Set to Plunge as History, AI Collide | Bloomberg Law | press | https://news.bgov.com/business-and-practice/big-law-first-year-hiring-set-to-plunge-as-history-ai-collide | 2026-09-10 | full |
| VAULT-PYRAMID-2026 | The Compressed Pyramid | Vault | press | https://legacy.vault.com/blogs/vaults-law-blog-legal-careers-and-industry-news/the-compressed-pyramid-what-ai-means-for-the-associate-career-ladder | 2026-08-11 | full |
| CITYAM-BIG4-2025 | Big Four slash graduate jobs as AI takes on entry level work | City AM | press | https://www.cityam.com/?p=2342067 | 2025-06-23 | full |
| PEOPLEMATTERS-PWC-2025 | PwC reduces entry-level recruitment | People Matters | press | https://www.peoplematters.in/news/hr-effectiveness/pwc-reduces-entry-level-recruitment-as-economy-slows-and-ai-reshapes-jobs-43454 | 2025-09-09 | full |
| PEOPLEMATTERS-MCK-2025 | McKinsey rejects AI job fears, to boost hiring by 12% in 2026 | People Matters | press | https://www.peoplematters.in/news/strategic-hr/mckinsey-rejects-ai-job-fears-to-boost-hiring-by-12percent-in-2026-43536 | 2025-09-12 | full |
| BI-PWC-2025 | PwC is training junior accountants to be like managers | Business Insider (via Yahoo Finance) | press | https://finance.yahoo.com/news/pwc-training-junior-accountants-managers-170001522.html | 2025-08-08 | full |
| FORTUNE-MCK-2026 | McKinsey challenges graduates to master AI tools | Fortune | press | https://fortune.com/2026/01/14/how-to-get-hired-at-mckinsey-ai-tools-liberal-arts-creativity | 2026-01-14 | full |
| CONSULTANCYUK-PYRAMID-2026 | AI may up-end the consulting pyramid | Consultancy.uk | press | https://www.consultancy.uk/news/43210/ai-may-up-end-the-consulting-pyramid | 2026-02-19 | full |
| SLASHDOT-CONSULTING-2025 | Top Consultancies Freeze Starting Salaries as AI Threatens 'Pyramid' Model | Slashdot (summarising FT and Management Consulted) | press | https://tech.slashdot.org/story/25/12/01/1241232 | 2025-12-01 | full (secondary) |
| REGISTER-PWC-2026 | PwC will say goodbye to staff who aren't convinced about AI | The Register | press | https://theregister.com/2026/03/19/pwc_ai | 2026-03-19 | full |
| CIO-PWC-2026 | PwC US tells staff to opt out of company, not AI | CIO | press | https://www.cio.com/article/4148222/pwc-us-tells-staff-to-opt-out-of-company-not-ai-2.html | 2026-03-20 | full |
| DECRYPT-ACCENTURE-2026 | Accenture Is Tracking Whether Employees Use AI | Decrypt | press | https://decrypt.co/358616/accenture-tracking-employees-use-ai-promotions | 2026-02-19 | full |
| LEGALCHEEK-RG-2025 | Ropes & Gray encourages junior lawyers to spend 20% of billable time on AI | Legal Cheek | press | https://www.legalcheek.com/2025/11/ropes-gray-encourages-juniors-to-spend-20-of-billable-hours-on-ai/amp/ | 2025-11-19 | full |
| SCOTTISHLEGAL-RG-2026 | Law firm tasks junior lawyers with exploring AI | Scottish Legal News | press | https://www.scottishlegal.com/articles/ropes-gray-tasks-junior-lawyers-with-exploring-ai | 2026-01-12 | full |
| NONBILLABLE-RG-2026 | Ropes & Gray gives junior lawyers 20% of billable time | Non-Billable | press | https://www.nonbillable.co.uk/news/ropes-gray-gives-junior-lawyers-20-of-billable-time-for-ai-work | 2026 | full |
| NONBILLABLE-AOS-2026 | Meet the junior lawyers putting AI to work inside A&O Shearman | Non-Billable | press | https://www.nonbillable.co.uk/posts/junior-lawyers-ai-innovation-a-o-shearman-harvey | 2026-03-10 | full |
| LAWNEXT-KENNEDYS-2025 | Kennedys partners with Spellbook (press release) | LawNext | press | https://www.lawnext.com/2025/10/kennedys-partners-with-spellbook-to-launch-groundbreaking-legal-training-programme-for-the-ai-era.html | 2025-10-01 | full |
| LEGALITINSIDER-KENNEDYS-2025 | 'A massive step in the right direction': Kennedys and Spellbook | Legal IT Insider | press | https://legaltechnology.com/a-massive-step-in-the-right-direction-kennedys-partners-with-spellbook-to-rethink-junior-training-in-the-ai-era/ | 2025-10-02 | full |
| CPAPA-STOP-2026 | Stop Training CPAs for Yesterday's Work | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/09/02/stop-training-cpas-for-yesterdays-work/189548/ | 2026-09-02 | full |
| CPAPA-SKILLS-2026 | Beyond the Accountant Shortage: The Skills Shortage Facing CPA Firms | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/03/beyond-the-accountant-shortage-the-skills-shortage-facing-cpa-firms/187848/ | 2026-08-03 | full |
| KARBON-JUNIOR-2026 | How do junior accountants learn when AI does the grunt work? | Karbon Magazine | vendor | https://karbonhq.com/resources/training-junior-accountants-ai/ | 2026-04-30 | full |
| KARBON-SOAI-2026 | The State of AI in Accounting Report 2026 (landing page) | Karbon | vendor | https://karbonhq.com/resources/ebooks/state-of-ai-accounting-report-2026/ | 2026 | full (landing page: 98% use AI; report gated) |
| KANTATA-RMI-2026 | New Study Finds Resource Management at Strategic Crossroads | Kantata | vendor | https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services | 2026-04-09 | full |
| NONBILLABLE-REDDIT-2026 | 'AI is eating my job': Big Law juniors confront a new reality | Non-Billable | community | https://www.nonbillable.co.uk/news/ai-big-law-juniors-confront-a-new-reality-reddit | 2026-07-06 | full (article; thread not opened) |
| LEGALCHEEK-REDDIT-2026 | Junior lawyers split: Is AI 'eating' their jobs? | Legal Cheek | community | https://www.legalcheek.com/2026/07/junior-lawyers-divided-over-whether-ai-is-eating-their-jobs-or-just-cutting-the-boring-bits/amp/ | 2026-07-08 | full (article; thread not opened) |
| HARBOR-LEGALSOUNDINGS-2026 | Legal Soundings: Talent & Innovation in the Age of AI | Harbor | podcast | https://harborglobal.com/audio/legal-soundings-talent-innovation-in-the-age-of-ai/ | 2026-01-28 | full (show notes; audio not heard) |
| ADR-AIFL-EP28-2025 | AI and the Future of Law, episode 28: Redefining Legal Training with AI | AAA-ICDR / PLI | podcast | https://www.adr.org/podcasts/ai-and-the-future-of-law/ai-and-the-future-of-law-episode-28/ | 2025-07-09 | full (show notes and transcript opening read; "apprenticeship model broke this summer" per Ethan Mollick, as discussed by the hosts) |
| LIV-CROSSEXAMINED-2026 | How AI in legal supervision is changing lawyer training | Law Institute of Victoria | podcast | https://www.castfox.net/podcast/cross-examined-7610284/episode/how-ai-in-legal-supervision-is-changing-lawyer-training-1785836 | 2026-03-23 | full (show notes; audio not heard) |
| LAWYERSWEEKLY-2026 | AI v junior lawyers: Is the fear real or overblown? | Lawyers Weekly | podcast | https://www.lawyersweekly.com.au/podcast/44797-ai-v-junior-lawyers-is-the-fear-real-or-overblown | 2026-08-07 | search-only (paywalled after opening paragraph) |
| CALBAR-GENAI-2026 / EC-AIACT-2026 | Cal Bar guidance; EU AI Act timeline | State Bar of California; European Commission | regulator | see landscape file | 2026 | carried from landscape, not re-opened |

Distinct sources listed: 62, of which 60 were opened and read and 2 are `search-only` (CPATRENDLINES-ENGAGE-2026, LAWYERSWEEKLY-2026); the Cal Bar and EU AI Act row is carried from the landscape and not counted. By type: conference 8 (7 read), professional-body 6, academic 2, survey 1, press 36, vendor 3, community 2, podcast 4 (3 read). Podcast items were read as show notes only. Eight source types are covered; no regulator, standard-setter or job-posting source was read.

## 6. Gaps

- **ILTACON 2026, CLOC, Legal Geek, PMI and MCA event content on talent** was not found. The landscape marks these programmes as JavaScript-rendered or paywalled, and the search budget ran out before targeted searches. Conference evidence here is TRI recaps (Legalweek, CMBDO, COO/CFO, AI Forum) and an ENGAGE preview, not session transcripts.
- **No quality evidence** beyond the NBER trial: no error rates, override rates, parallel-run results or inspection findings for AI-supervising juniors, no tracked skill-retention data from any firm, and no published results for simulation programmes, the Trailblazers programme or the Duane Morris onboarding.
- **NBER 35720 full text** returned HTTP 403, so sample details, task design and effect heterogeneity beyond the abstract were not read.
- **TR Future of Professionals 2026 publication date** is not shown on the report page; fieldwork was March-April 2026. All TR figures are from a vendor with a commercial interest; the full dataset was not seen.
- **Karbon State of AI in Accounting 2026** is gated; the 20%, "fewer than half" and 21% figures come from a Karbon article and the sample is not captured.
- **ICAEW Evolution of Mid-Tier Accountancy Firms research** (68% expect AI to reduce some early-career roles) was seen only through an ICAEW article; sample unknown.
- **Original sources not opened:** Business Insider and FT originals (PwC, Accenture, Big Four cuts), Reuters (McKinsey), the Times (Ropes & Gray London), SurePoint, BCG Attorney Search, NALP, Citi, Journal of Accountancy's Oct 2025 pipeline pieces, AICPA Profession Ready page, the r/biglaw thread itself. Law Gazette returned an HTTP 405 challenge; TechRepublic returned 403.
- **Podcasts:** only show notes were read; no audio or transcripts (except the opening of the ADR episode 28 page). Lawyers Weekly is paywalled.
- **Not found at all:** firm-published data on promotion or evaluation criteria changes (outside Accenture and PwC reports), practitioner discussion of AI screening of candidates, in-house talent case studies, consulting firm primary statements on associate training (McKinsey, BCG, Bain, Deloitte, EY, KPMG pages were not opened), HR-side practitioner sources (SHRM, CIPD) and Legal Evolution or Law21 commentary.
- **Dates:** TR-FOP-2026 and NONBILLABLE-RG-2026 carry year-only dates; ICAEW June and February 2026 pieces carry year and month from the URL only.
- **Landscape corrections:** McKinsey's 12% is North American workforce growth, not a graduate figure; Kantata/RMI's sample is 44 organisations; the Citi hiring figures are confirmed at source (Bloomberg Law), while the BCG Attorney Search 86%/35% figures are second-hand through Vault.

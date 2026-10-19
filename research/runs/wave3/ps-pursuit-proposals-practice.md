# Professional services, pursuit-proposals: practice angle

Prepared 2026-10-19. Archetype: professional-services. Module: pursuit-proposals (RFP and RFI responses, proposals, pitches, credentials, win/loss analysis). Angle: practice (what firms and in-house teams actually do).

Method: `curl` for pages and PDFs, `pdftotext` plus page renders where a PDF had no text layer, and the `r.jina.ai` text mirror for pages that blocked `curl` (marked in the source list). 37 distinct sources were opened. Twelve web searches were used (several returned vendor material only); the shared search budget then ran out, so some leads could not be followed (see Gaps). Public sources only.

---

## 1. Summary

- **Pursuit is the module where AI is most widely used and least measured.** The Loopio 2026 survey (1,533 respondents, all industries, run with APMP) reports 79% of response teams used AI in the last 12 months. Only 17% of respondents list improved win rate as a top benefit, and the same survey's average win rate fell to 39% from 45% (LOOPIO-TRENDS-2026). No error rate, override rate, parallel run or independent measurement was found for any professional-services pursuit use case.
- **Named professional-services deployments are almost all vendor case studies.** The named firms found: Cherry Bekaert (accounting, Loopio), Gordon Rees Scully Mansukhani, Stinson, Gowling WLG (law, ikaun), Arup and Neudesic (design and systems integration, ikaun), Benesch and Woodard & Curran (engineering, Kantiv), Versent (IT services, in-house build), Lynn Pinker Hurst & Schwegmann (law, Harvey), and Serco (government services, AutogenAI; adjacent to the archetype). Their figures are self-reported recollections or estimates inside vendor documents, so no entry reaches grade A.
- **The dominant change is retrieval from a governed library, not free generation.** Cherry Bekaert says it cannot make certain claims, so it extracts validated content from its library and sends output back through review (LOOPIO-CHERRYBEKAERT-2026). Law-firm and AEC cases rest on structured experience, bio and CV data (IKAUN-GRSM-2026, KANTIV-BENESCH-2026).
- **The work is shifting from drafting to qualification and tailoring.** Time saved is described as going into tailoring, go/no-go selectivity and senior review. Loopio top performers (win more than half of RFPs they respond to) are as likely as average teams to use AI for drafting but more likely to use it to analyse quality, check accuracy and interpret data (LOOPIO-TRENDS-2026).
- **Agentic offers arrived in 2026 with little public deployment evidence.** Intapp Celeste general availability (2026-07-15), Introhive MCP server (commercial preview, 2026-04-16), Priori Scout for in-house RFP management (2026-04-07) and Certinia Veda sales agents are announcements, not measured deployments.
- **Two forces act on the buyer side.** RFPs now ask firms how they use AI (ABA-LPMRFP-2026, TRI-LEGALWEEK-2026), and public buyers are told not to ban suppliers' AI use but to do more due diligence (UKGOV-PPN0224-2024). One 2026 legal commentary warns that agency evaluators may use undisclosed generative AI on proposals (NATLAW-BRADLEY-2026).

Use cases: 14 (grade A: 0, B: 7, C: 5, D: 2).

---

## 2. Use cases

```yaml
- id: professional-services-pursuit-proposals-01
  title: Grounded RFP answer drafting from a governed content library
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [document-production, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Proposal teams answer hundreds of repeated questions by copy-pasting from old Word files and chasing subject-matter
    experts. Content is scattered and goes stale, so every response starts close to scratch.
  solution: >-
    Approved answers, bios and service descriptions sit in one tagged library with named owners. The tool retrieves
    the closest approved answer for each question and, where used, drafts from it, so the team starts from a first draft.
    Senior people and subject-matter experts then review and tailor targeted parts instead of writing from scratch.
    Cherry Bekaert (accounting) uses a bought platform; Versent built its own retrieval-augmented tool on Azure services.
  outcomes:
    - lever: speed
      description: >-
        A Cherry Bekaert manager says a government audit RFP that once took about eight hours to draft now takes about two.
        The case study also says drafting overall went from about eight hours to two to four.
      figure: "8 hours to 2 hours (government audit RFP); 8 hours to 2-4 hours (general)"
      measures: >-
        Hours to draft a response, as stated by Cherry Bekaert's Sr. Manager, Pursuit and Sales Asset Leader. No baseline
        method or sample is given, so this is a recollection or estimate.
      provenance: self-reported
      source_ref: LOOPIO-CHERRYBEKAERT-2026
    - lever: capacity
      description: >-
        Cherry Bekaert reports an 80% automation rate across projects, about 550 RFPs a year, and about 600 professionals
        engaged in the platform. Automation rate is not defined in the source.
      figure: "80% automation rate; about 550 RFPs per year; about 600 professionals"
      measures: >-
        Automation rate is undefined in the source; 550 is the annual count of RFPs the proposal team supports; 600 is
        the number of professionals the case study says it engages across the firm.
      provenance: vendor-published
      source_ref: LOOPIO-CHERRYBEKAERT-2026
    - lever: speed
      description: >-
        Versent projects an annual time saving of 600 hours from its internal Bid Assistant. The page states this as a
        projection, with a stated immediate and substantial ROI but no figure.
      figure: "600 hours per year (projected)"
      measures: "Projected annual hours saved by Versent bid teams. A projection, not a measured result."
      provenance: self-reported
      source_ref: VERSENT-BIDASSISTANT-2025
    - lever: capacity
      description: >-
        Cross-industry survey context, not professional-services specific: more teams now use AI to generate specific
        answers.
      figure: "62% in 2025, up from 46% in 2024"
      measures: >-
        Share of 1,533 RFP-team respondents (all industries) saying they use AI for generating specific answers.
      provenance: vendor-published
      source_ref: LOOPIO-TRENDS-2026
  prerequisites:
    - "A curated library with ownership and freshness tracking (Cherry Bekaert governs nearly 2,500 content assets across service-line libraries with industry tags)."
    - "Attorneys, partners or professionals willing to contribute and review; Cherry Bekaert chose a tool its professionals would use."
    - "For an in-house build: data preparation, a chunking strategy and an evaluation baseline before deployment (Versent)."
    - "A secure tool: Loopio notes 57% of respondents use ChatGPT or Copilot and warns against feeding confidential content to general tools."
  risks_and_guardrails:
    - "Cherry Bekaert says it cannot make certain claims, so it extracts validated content from the library and sends output back through reviews and into the library (LOOPIO-CHERRYBEKAERT-2026, Solution section)."
    - "An ABA Law Practice column says drafting with public LLMs that train on firm inputs is an absolute no-no, and advises checking every word, including success stories, awards and bios (ABA-LPMAI-2026, Cautions)."
    - "Win-rate effect is unproven: only 17% of surveyed teams list improved win rate as a top AI benefit, and the report says they may not yet be measuring it (LOOPIO-TRENDS-2026, Speed and Quality are Top AI Benefits)."
  human_checkpoints:
    - "Senior professionals review a project in the shared workspace with an auditor mentality, then go into detail on the parts that matter (LOOPIO-CHERRYBEKAERT-2026)."
    - "Proposal team tailors the draft to the opportunity before submission."
  role_evolution: >-
    Cherry Bekaert built a dedicated proposal function in place of RFPs as a side-of-desk marketing task; the team builds
    first drafts from the library and senior staff review targeted parts (LOOPIO-CHERRYBEKAERT-2026). In the survey,
    32% of teams say leadership expects new responsibilities and 42% expect better results because of AI; 16% say they
    replaced internal people resources with AI (LOOPIO-TRENDS-2026, p.61).
  evidence_grade: B
  sources:
    - { ref: LOOPIO-CHERRYBEKAERT-2026, title: "How Cherry Bekaert Scaled to 550 RFPs a Year, With Loopio", publisher: Loopio, type: vendor, url: "https://loopio.com/case-study/cherry-bekaert/", date: "2026-10-08", access: full, locator: "Results; Solution; quote on guardrails" }
    - { ref: VERSENT-BIDASSISTANT-2025, title: "Accelerating RFP Response with GenAI", publisher: Versent, type: firm, url: "https://versent.com.au/case-studies/accelerating-rfp-response-with-genai/", date: "2025", access: full, locator: "Solution; Outcome / Key Outcomes" }
    - { ref: LOOPIO-TRENDS-2026, title: "RFP Response Trends & Benchmarks 2026", publisher: Loopio with APMP, type: survey, url: "https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf", date: "2026-03", access: full, locator: "pp.56-61, 67" }
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "Cautions" }
  last_reviewed: "2026-10-19"
  notes: >-
    Cherry Bekaert's page is hosted by Loopio. Versent's page has no date; the year comes from image upload paths. The
    Loopio blog (LOOPIO-BLOG-2026) says 47% of teams say leadership expects better results; the report itself says 42%
    (p.61). The report figure is used. Exec-summary drafting (39% of respondents) and tone consistency are folded in here.

- id: professional-services-pursuit-proposals-02
  title: Proposal archive search and technical-narrative drafting for AEC pursuits
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [document-production, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Engineering firms hold hundreds of past proposals, project descriptions and resumes across file servers, a project
    system and SharePoint. People re-ask the marketing team for old language, and resume versions multiply.
  solution: >-
    Past proposals are loaded into a pursuit platform that finds content by document, person and project and drafts
    technical approaches, bios, case studies and award entries from the archive. Benesch also checks first drafts
    against RFP requirements. Woodard and Curran uses it to find the right resume version for each proposal.
  outcomes:
    - lever: speed
      description: >-
        Benesch's marketing communications manager recounts an engineer new to AI who finished a technical approach in
        two hours that would normally take six to eight.
      figure: "2 hours versus 6-8 hours (one anecdote)"
      measures: "Hours for one engineer to write one technical approach, as recounted by Benesch's manager. One person, one proposal."
      provenance: self-reported
      source_ref: KANTIV-BENESCH-2026
    - lever: speed
      description: >-
        Woodard and Curran estimates a 30-40% time saving per proposal from faster search and retrieval.
      figure: "30-40% per proposal (estimate)"
      measures: "Woodard and Curran's own estimate of time saved per proposal on searching and retrieving content. Method not stated."
      provenance: self-reported
      source_ref: KANTIV-WOODARD-2026
    - lever: capacity
      description: >-
        Benesch has almost 1,000 proposals in the platform, used by a 34-person marketing team and nearly 400 technical
        staff. The vendor summary says productivity tripled in certain use cases.
      figure: "almost 1,000 proposals; 34 marketing staff; nearly 400 technical staff; triple productivity in certain use cases"
      measures: "Counts of proposals loaded and of users, as stated; the tripling claim is the vendor's summary with no stated measure."
      provenance: vendor-published
      source_ref: KANTIV-BENESCH-2026
  prerequisites:
    - "Proposal archive uploaded and searchable (Benesch about 1,000 proposals)."
    - "A firm-specific taxonomy of services and project types; a vendor blog argues a generic assistant pointed at SharePoint lacks it (KANTIV-COPILOT-2026, vendor opinion)."
    - "Security and compliance review (Woodard and Curran says the tool met its cybersecurity standards)."
  risks_and_guardrails:
    - "Generic output: the SMPS Q2 2026 report, as summarised by a vendor, notes selection committees recognise generic AI output, so grounding in real project history matters (KANTIV-SMPSQ2-2026; secondary summary)."
    - "Project facts such as square footage or contract value should be verified against the system of record; this is a vendor claim about general assistants (KANTIV-COPILOT-2026)."
  human_checkpoints:
    - "First drafts are checked against RFP requirements and reviewed by the marketing team (KANTIV-BENESCH-2026)."
  role_evolution: >-
    Technical staff pulled into a proposal at short notice can draft a technical approach themselves; marketing is asked
    less for old language because staff search for themselves (KANTIV-BENESCH-2026; KANTIV-ROBINS-2026).
  evidence_grade: B
  sources:
    - { ref: KANTIV-BENESCH-2026, title: "Benesch's Pursuit AI Evolution: Smarter Search, Faster Content and Greater Efficiency", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/case-study/beneschs-ai-evolution-smarter-search-faster-content-and-greater-efficiency", date: "2026-06", access: full, locator: "Summary; The Result" }
    - { ref: KANTIV-WOODARD-2026, title: "How Kantiv Transformed Pursuit Management at Woodard & Curran", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/case-study/a-strategy-to-streamline-how-kantiv-transformed-proposal-management-at-woodard-curran", date: "2026-06", access: full, locator: "The Result, items 1-2" }
    - { ref: KANTIV-ROBINS-2026, title: "Robins & Morton: Unlocking Institutional Knowledge with Kantiv", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/case-study/robins-morton-unlocking-institutional-knowledge-with-kantiv", date: "2026-06", access: full, locator: "The Result" }
    - { ref: KANTIV-SMPSQ2-2026, title: "What the SMPS Q2 AI Report Means for AEC Pursuit Teams", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/blog/smps-q2-ai-report", date: "2026-07-13", access: full, locator: "findings list" }
    - { ref: KANTIV-COPILOT-2026, title: "Custom Copilot Agents: What it actually takes to build agents that can handle pursuits", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/blog/copilot-custom-agent-for-aec-proposals", date: "2026-09-26", access: full, locator: "Four Critical Gaps" }
  last_reviewed: "2026-10-19"
  notes: >-
    The three Kantiv case-study pages carry the same page-metadata date (2026-06-20), so first publication may be earlier.
    Robins and Morton (a construction contractor, adjacent to the archetype) reports award entries cut from 30 hours to
    6; that figure is a quote and is not used as an outcome. The SMPS Q2 2026 AI Quarterly Insight Report was not
    opened (member access); only the vendor's summary was read. Kantiv is the vendor in every source here.

- id: professional-services-pursuit-proposals-03
  title: Pitchbook and proposal assembly from structured bios, matter experience and CVs
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [document-production, data-reporting]
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Pitches are assembled by hand from Word bios, practice overviews and matter lists. Bios drift from the website,
    experience sits in spreadsheets, and CVs for consultants go stale and lose formatting.
  solution: >-
    An experience-management platform holds bios, matter experience, CVs and trial or project history as structured
    data, fed from the website, finance and HR systems. Pitches, proposals and CVs are generated from templates in
    minutes. Gordon Rees Scully Mansukhani also loads an approved-answer library and uses an Answer Agent for RFPs.
  outcomes:
    - lever: speed
      description: >-
        GRSM's marketing manager says proposal generation time fell by more than 50% in the first quarter after go-live
        (November 2025), across about 60 proposals. Pitches that took up to an hour now take minutes.
      figure: "more than 50% reduction; about 60 proposals; up to an hour to minutes"
      measures: >-
        Proposal generation time as stated by GRSM's Marketing Manager; baseline and method are not given. The firm
        handles about 200 pitchbooks and RFPs a year.
      provenance: self-reported
      source_ref: IKAUN-GRSM-2026
    - lever: speed
      description: >-
        Neudesic lists targets of cutting resume preparation time by 75% and proposal preparation time by 50%. The
        results section says getting a CV now takes a fraction of the time, without figures.
      figure: "75% (resumes) and 50% (proposals), stated in the solutions list"
      measures: >-
        Resume preparation time and proposal preparation time; the source does not say whether these are measured
        results or goals.
      provenance: vendor-published
      source_ref: IKAUN-NEUDESIC-2026
    - lever: quality
      description: >-
        Arup says its CV platform doubled the time bid teams can spend tailoring CVs, with over 12,000 professionals
        engaged and about 7,000 CVs imported, across more than 10,000 bids a year.
      figure: "doubled tailoring time; over 12,000 professionals; about 7,000 CVs; 13 languages"
      measures: >-
        Tailoring time has no stated baseline; 12,000 counts professionals who have actively engaged with the platform
        (Arup has over 18,000 professionals).
      provenance: vendor-published
      source_ref: IKAUN-ARUP-2026
  prerequisites:
    - "Data clean-up: GRSM consolidated about 22 hearing-type values in a trial spreadsheet of over 1,100 matters before import."
    - "Feeds from source systems: website bios (GRSM), the finance system (Stinson), HR and billing data (Neudesic), a nightly bio feed from the content management system."
    - "A refresh cadence: Neudesic set quarterly consultant updates with automated reminders; Arup built use into appraisals, onboarding and performance reviews."
  risks_and_guardrails:
    - "GRSM notes verification remains important and needed manual effort when bios lived in Word; it flags confidential trial data and keeps a pitch-specific practice overview with experience not published on the web (IKAUN-GRSM-2026, Before State and Implementation)."
    - "Scope caution: much of this is data-driven document generation. The Arup page does not claim AI, and ikaun's own sources label parts of it AI-powered (IKAUN-NEUDESIC-2026)."
  human_checkpoints:
    - "Lawyers and consultants maintain their own experience entries; talent managers customise resumes (IKAUN-NEUDESIC-2026)."
    - "The team tailors the generated draft to the opportunity (IKAUN-GRSM-2026)."
  role_evolution: >-
    GRSM says proposal work once concentrated among a small group is now spread more evenly because the platform is
    intuitive; Stinson's proposal and experience manager oversees content governance and data (IKAUN-GRSM-2026;
    IKAUN-STINSON-2026).
  evidence_grade: B
  sources:
    - { ref: IKAUN-GRSM-2026, title: "ikaun Helps Am Law 100 Firm GRSM Cut Proposal Time by 50% in Four Months", publisher: ikaun, type: vendor, url: "https://www.ikaun.com/case-studies/ikaun-helps-am-law-100-firm-grsm-cut-proposal-time-by-50-in-four-months", date: "2026", access: full, locator: "The BD Problem at Scale; Implementation; Results" }
    - { ref: IKAUN-NEUDESIC-2026, title: "ikaun Transforms Sales Operations and Redefines Efficiencies for Neudesic", publisher: ikaun, type: vendor, url: "https://www.ikaun.com/case-studies/ikaun-transforms-sales-operations-and-redefines-efficiencies-for-neudesic", date: "2026", access: full, locator: "Solutions powered by ikaun; Results and Next Steps" }
    - { ref: IKAUN-ARUP-2026, title: "Leveraging Global Capability through Arup People", publisher: ikaun, type: vendor, url: "https://www.ikaun.com/case-studies/leveraging-global-capability-through-arup-people", date: "2026", access: full, locator: "Implementation + Rollout; Results" }
    - { ref: IKAUN-STINSON-2026, title: "Winning More Time for Strategy: How Stinson is Transforming RFP and Proposal Responses with ikaun", publisher: ikaun, type: vendor, url: "https://www.ikaun.com/case-studies/winning-more-time-for-strategy-how-stinson-is-transforming-rfp-and-proposal-responses-with-ikaun", date: "2026", access: full, locator: "Background; Results" }
    - { ref: IKAUN-GOWLING-2026, title: "ikaun's World Class Experience Management Solution Drives Business Value Throughout Global Law Firm, Gowling WLG", publisher: ikaun, type: vendor, url: "https://www.ikaun.com/case-studies/ikauns-world-class-experience-management-solution-drives-business-value-throughout-global-law-firm-gowling-wlg", date: "2026", access: full, locator: "Challenges; Results" }
  last_reviewed: "2026-10-19"
  notes: >-
    None of the five ikaun case-study pages shows a publication date; the year is the access year. GRSM's page says
    go-live was November 2025 and results are at four months, so it was published in 2026. The GRSM headline says 50% in
    four months while the quote says over 50% in the first quarter after go-live. Gowling WLG (over 1,500 legal
    professionals) is an experience-management case with no outcome figures and is cited for context only.

- id: professional-services-pursuit-proposals-04
  title: RFP requirement extraction and pre-submission compliance checking
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Long RFPs bury mandatory requirements, deadlines and attachments. Misses cost disqualification, and compliance
    checking is done late, by hand, under deadline.
  solution: >-
    The tool reads the solicitation, lists requirements in a matrix, and checks a drafted response against them.
    Benesch says first drafts can be checked for compliance against RFP requirements. A job posting for a proposal
    manager lists gap analysis against client specifications and human validation of AI output.
  outcomes:
    - lever: quality
      description: "none published; Benesch describes the capability and gives no figure"
      figure: "none published"
      measures: "No figure; qualitative statement from Benesch's marketing communications manager."
      provenance: self-reported
      source_ref: KANTIV-BENESCH-2026
  prerequisites:
    - "A tool that ingests solicitation documents and a defined review step after generation."
  risks_and_guardrails:
    - "An unnamed Big 4 firm's senior bid writer, quoted by AutogenAI, credits an extraction tool with time savings on a security-service proposal (AUTOGENAI-BIG4-2025, p.2); a vendor quote from an unnamed firm."
    - "The Randstad posting asks for compliance, legal and factual accuracy review of AI-generated output (RANDSTAD-PROPOSALMGR-2026)."
  human_checkpoints:
    - "Human validation of AI output for compliance, legal and factual accuracy before submission (RANDSTAD-PROPOSALMGR-2026)."
  role_evolution: >-
    The posting titles the role Proposal Manager (RFX and AI Orchestration), combining drafting with AI tools and
    validation of the output (RANDSTAD-PROPOSALMGR-2026). The employer is not named in the posting.
  evidence_grade: B
  sources:
    - { ref: KANTIV-BENESCH-2026, title: "Benesch's Pursuit AI Evolution", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/case-study/beneschs-ai-evolution-smarter-search-faster-content-and-greater-efficiency", date: "2026-06", access: full, locator: "The Result, Expedited Deliverable Production" }
    - { ref: RANDSTAD-PROPOSALMGR-2026, title: "Proposal Manager (RFX and AI Orchestration), Brentford", publisher: Randstad, type: job-posting, url: "https://www.randstad.com/jobs/proposal-manager_brentford_47525616/", date: "2026-09-30", access: full, locator: "responsibilities list" }
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "item 1" }
    - { ref: AUTOGENAI-BIG4-2025, title: "How the Fastest Growing Big 4 Professional Services Firm Optimised Competitive Tendering with AutogenAI", publisher: AutogenAI, type: vendor, url: "https://autogenai.com/wp-content/uploads/2025/07/Professional-Services-Firm-Case-Study.pdf", date: "2025-07", access: full, locator: "pp.2-3 (image-only PDF, read from page renders)" }
  last_reviewed: "2026-10-19"
  notes: >-
    Grade B rests on one named firm (Benesch) describing a capability with no measure. The ABA column describes the
    same step as an idea; the job posting has no named firm. Date for AUTOGENAI-BIG4-2025 comes from the upload path.

- id: professional-services-pursuit-proposals-05
  title: Go/no-go qualification supported by experience and win/loss data
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [expert-judgment, data-reporting]
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Teams answer more RFPs with less selectivity. Go/no-go meetings run on impressions, and firms cannot quickly tell
    whether they have handled similar work.
  solution: >-
    Experience data tied to financial records lets the team see at once whether the firm has done similar matters
    before deciding to pursue. Vendors and practitioners also describe scoring go/no-go criteria against past wins and
    losses, and predicting win probability from past submissions.
  outcomes:
    - lever: quality
      description: >-
        Stinson says its team can now make faster, more data-driven go/no-go decisions because experience data is
        visible. No figure is given.
      figure: "none published"
      measures: "Qualitative statement in the ikaun case study; no figure."
      provenance: vendor-published
      source_ref: IKAUN-STINSON-2026
    - lever: risk
      description: >-
        Survey context (all industries): go/no-go use fell to its lowest since 2021 while submissions rose; top performers
        use it more.
      figure: "75% of teams use a go/no-go process (81% of top performers); 55% of RFPs received were responded to"
      measures: >-
        Share of 1,533 respondents using a go/no-go process; top performers are teams winning more than 50% of RFPs they
        respond to; 55% is the share of RFPs responded to in 2025.
      provenance: vendor-published
      source_ref: LOOPIO-TRENDS-2026
  prerequisites:
    - "Matter or project experience linked to finance data (Stinson)."
    - "Records of past pursuits with outcomes: a Kantiv post says to score 30 to 40 past pursuits and let results set the criteria weights (vendor method, KANTIV-GONOGO-2026)."
  risks_and_guardrails:
    - "Incomplete or inaccurate bid history can skew win probabilities, and past wins may favour low-profit work (ABA-LPMAI-2026, Cautions)."
  human_checkpoints:
    - "Leadership decides whether to bid; the ABA column frames AI as informing a decision such as whether an 8% chance of winning justifies 35,000 dollars of partner time (a hypothetical, ABA-LPMAI-2026, item 4)."
  role_evolution: >-
    Loopio reports top-performing teams are more likely to be seen as strategic contributors (60% against 47% of the
    average) and to run a go/no-go matrix (LOOPIO-TRENDS-2026, Top Trends and Chapter 7).
  evidence_grade: B
  sources:
    - { ref: IKAUN-STINSON-2026, title: "Winning More Time for Strategy: How Stinson is Transforming RFP and Proposal Responses with ikaun", publisher: ikaun, type: vendor, url: "https://www.ikaun.com/case-studies/winning-more-time-for-strategy-how-stinson-is-transforming-rfp-and-proposal-responses-with-ikaun", date: "2026", access: full, locator: "Results; Top 3 Results" }
    - { ref: LOOPIO-TRENDS-2026, title: "RFP Response Trends & Benchmarks 2026", publisher: Loopio with APMP, type: survey, url: "https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf", date: "2026-03", access: full, locator: "Chapter 1, pp.17-20; Chapter 7" }
    - { ref: KANTIV-GONOGO-2026, title: "How to calibrate your go/no-go matrix using your own wins and losses", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/blog/blog-go-no-go-scorecard-matrix", date: "2026-10-15", access: full, locator: "weighting section" }
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "item 4; Cautions" }
  last_reviewed: "2026-10-19"
  notes: >-
    Stinson is in production on experience search, and its page says it is preparing to adopt agentic capabilities for
    compliance validation and scoring (not yet in use). Predictive bid/no-bid scoring is described only by the ABA
    column and a vendor blog, so that part is an idea. The Loopio go/no-go figures are cross-industry.

- id: professional-services-pursuit-proposals-06
  title: Pitch preparation and urgent new-business response with a firm-knowledge assistant
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [research-synthesis, document-production]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    A competitive request needs experience, prior pitch language and client context pulled from several practice groups
    and systems. Partners cobble this together by hand, often in days.
  solution: >-
    Partners query internal archives and external filings through a legal AI platform to draft a pitch or response and
    prepare for the client meeting. Relationship tools such as Introhive offer an MCP server so assistants such as
    Copilot can read relationship strength and past interactions for pitch preparation.
  outcomes:
    - lever: speed
      description: >-
        Harvey's blog says Lynn Pinker Hurst & Schwegmann used Harvey to craft and deliver a response to an urgent client
        request in under 48 hours and won the new business.
      figure: "under 48 hours; one won pitch"
      measures: "Elapsed time for one urgent client request at one firm, as told by Harvey. A single anecdote from a vendor blog."
      provenance: vendor-published
      source_ref: HARVEY-BDBLOG-2026
  prerequisites:
    - "Firm documents and archives in the platform's secure repository; for relationship context, a clean relationship-data foundation (Introhive says 78% of surveyed partners find firm relationship data hard to act on, INTROHIVE-LAWSITES-2026)."
  risks_and_guardrails:
    - "Introhive's MCP server returns only context needed for the question and inherits existing permissions and governance (INTROHIVE-MCP-2026)."
    - "68% of partners using AI for business development in the Introhive survey rely only on general-purpose tools that cannot see firm relationship data (INTROHIVE-LAWSITES-2026)."
  human_checkpoints:
    - "Lawyers refine and customise the draft for the client (ABA-LPMRFP-2026 describes this as the pattern; no named firm)."
  role_evolution: >-
    Harvey describes partners drafting responses themselves from firm archives rather than waiting for business
    development staff to assemble materials (HARVEY-BDBLOG-2026, Rapid Opportunity and RFP Response).
  evidence_grade: B
  sources:
    - { ref: HARVEY-BDBLOG-2026, title: "AI for Law Firm Business Development", publisher: Harvey, type: vendor, url: "https://www.harvey.ai/blog/ai-for-law-firm-business-development", date: "2026-06-23", access: full, locator: "section 3, Help Partners Respond Faster to RFP Opportunities" }
    - { ref: INTROHIVE-MCP-2026, title: "Introhive Announces MCP Server for Legal AI", publisher: Introhive, type: vendor, url: "https://www.introhive.com/news/introhive-announces-mcp-server-for-legal-ai-enables-copilots-and-ai-agents-with-real-time-relationship-intelligence/", date: "2026-04-16", access: full, locator: "release body, Client Pitch Preparation" }
    - { ref: INTROHIVE-LAWSITES-2026, title: "Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use, Introhive Survey Finds", publisher: LawSites, type: press, url: "https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html", date: "2026-10-13", access: full, locator: "paragraphs on survey findings" }
    - { ref: ABA-LPMRFP-2026, title: "How AI Is Changing the Process of Law Firm Request for Proposals (RFP)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals", date: "2026-07", access: full, locator: "Real-World Scenarios" }
  last_reviewed: "2026-10-19"
  notes: >-
    The Lynn Pinker example is a vendor-told anecdote with no firm-side confirmation. The Introhive MCP server is a
    commercial preview announcement, not evidence of use. The ABA article was read through the r.jina.ai mirror because
    americanbar.org blocked curl. Relationship-intelligence content is routed to client-development.

- id: professional-services-pursuit-proposals-07
  title: Firm-AI playbooks for origination, pitch and business development
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [research-synthesis, coordination-scheduling]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >-
    Firms' AI assistants speed up the practice of law but not the business behind it: origination, pitch material,
    intake and conflicts still run on slow, manual workflows over proprietary firm data.
  solution: >-
    Intapp's Celeste runs multi-step playbooks over the firm's systems of record, including origination and business
    development. For law firms, Intapp says it can surface relevant matters, partner experience and prior pitch
    material for an urgent client request in minutes rather than hours.
  outcomes:
    - lever: speed
      description: "Intapp's claim that pitch material can be surfaced in minutes rather than hours; no measurement published."
      figure: "minutes rather than hours (vendor claim)"
      measures: "Time to surface relevant matters, partner experience and prior pitch material for an urgent request; vendor statement, no data."
      provenance: vendor-published
      source_ref: LAWNEXT-CELESTE-2026
  prerequisites:
    - "Intapp systems of record for intake, conflicts and relationship data, with Celeste integrated natively."
    - "Firm-specific playbooks (library supplied; no-code builder for firm-built ones)."
  risks_and_guardrails:
    - "Intapp says the same ethical walls, need-to-know restrictions and audit requirements that apply to people apply to Celeste, with a full record of actions (LAWNEXT-CELESTE-2026, Executing Multi-Step Workflows)."
  human_checkpoints:
    - "Not specified in the sources for the business-development playbooks."
  role_evolution: >-
    Intapp's chief product officer is quoted saying that clearing 10 times the matters is a new business model; the
    coverage gives no role changes for pursuit staff (LAWNEXT-CELESTE-2026).
  evidence_grade: C
  sources:
    - { ref: LAWNEXT-CELESTE-2026, title: "Intapp Makes Celeste Generally Available, Calling It An AI Coworker To Run the Business Side of Law Firms", publisher: LawSites (Bob Ambrogi), type: press, url: "https://www.lawnext.com/2026/07/intapp-makes-celeste-generally-available-calling-it-an-ai-coworker-to-run-the-business-side-of-law-firms.html", date: "2026-07-16", access: full, locator: "paragraphs on playbooks and early adopters" }
    - { ref: INTAPP-DEALCLOUD-2026, title: "Intapp DealCloud", publisher: Intapp, type: vendor, url: "https://www.intapp.com/dealcloud/", date: "2026", access: full, locator: "AI to power your pipeline and win rates (Knowledge and proposal readiness)" }
  last_reviewed: "2026-10-19"
  notes: >-
    General availability was announced 2026-07-15 after a limited release; named early adopters are BakerHostetler
    (focus so far on intake and conflicts, routed to acceptance-risk) and the private equity firm Hg (deal screening).
    No early adopter is reported using it for pitches or RFPs. The DealCloud page is undated (assets uploaded 2026-02)
    and was read through the r.jina.ai mirror.

- id: professional-services-pursuit-proposals-08
  title: Dedicated generative bid-writing platform for high-volume bid teams
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [document-production, research-synthesis]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Bid teams submit many tenders to tight deadlines. An existing in-house AI knowledge tool and a private ChatGPT were
    not built for end-to-end bid writing.
  solution: >-
    A bid-writing platform with research, expansion and extraction functions produces first drafts and supports
    real-time collaboration. Serco piloted it as one of its Impact Pilots; an unnamed Big 4 firm replaced an in-house
    knowledge tool and private ChatGPT with it.
  outcomes:
    - lever: speed
      description: >-
        AutogenAI's Serco case study reports an 85% efficiency gain in proposal writing and knowledge management and a 5%
        increase in win rates. The vendor's customer page headline says global revenue rose 5%, which the PDF does not say.
      figure: "85% efficiency gain; 5% increase in win rates"
      measures: >-
        Undefined: the PDF gives no numerator, denominator or period for either figure. Serco's own quote says only that
        the functionality was used more than 6,000 times.
      provenance: vendor-published
      source_ref: AUTOGENAI-SERCO-2025
    - lever: speed
      description: "An unnamed Big 4 firm is reported to have cut bid drafting time by 85%; the firm is not named, so this is a vendor claim."
      figure: "85% (unnamed firm)"
      measures: "Bid drafting time; no baseline, sample or period given."
      provenance: vendor-published
      source_ref: AUTOGENAI-BIG4-2025
  prerequisites:
    - "Firm knowledge repository connected to the platform."
    - "Evaluation of alternatives; the unnamed firm compared other bid-specific platforms."
  risks_and_guardrails:
    - "Serco's quoted figure is a usage count (6,000 uses), not an outcome; no accuracy or error data is published in either source."
  human_checkpoints:
    - "Senior stakeholders review less rework and spend time on strategic input (AUTOGENAI-BIG4-2025, p.3; vendor claim)."
  role_evolution: >-
    Quotes from an unnamed Big 4 firm's bid manager, bid director and bid writers describe time shifting to fine-tuning
    answers and strategy (AUTOGENAI-BIG4-2025, pp.2-3).
  evidence_grade: B
  sources:
    - { ref: AUTOGENAI-SERCO-2025, title: "Serco Increases Efficiency by 85% and Global Revenue by 5% with AutogenAI", publisher: AutogenAI, type: vendor, url: "https://autogenai.com/wp-content/uploads/2024/09/Serco-Increases-Efficiency-by-85-and-Global-Revenue-by-5-with-AutogenAI.pdf", date: "2025-03", access: full, locator: "The Solution; Results" }
    - { ref: AUTOGENAI-BIG4-2025, title: "How the Fastest Growing Big 4 Professional Services Firm Optimised Competitive Tendering with AutogenAI", publisher: AutogenAI, type: vendor, url: "https://autogenai.com/wp-content/uploads/2025/07/Professional-Services-Firm-Case-Study.pdf", date: "2025-07", access: full, locator: "pp.1-3 (image-only PDF)" }
    - { ref: AUTOGENAI-CUSTOMERS-2026, title: "AutogenAI customers", publisher: AutogenAI, type: vendor, url: "https://autogenai.com/customers/", date: "2026", access: full, locator: "customer stories list" }
  last_reviewed: "2026-10-19"
  notes: >-
    Serco is a government-services provider, adjacent to the archetype, so the grade is capped at B. The Serco PDF
    metadata shows creation on 2025-03-27 although its path says 2024/09. The customer page also lists Jacobs, Kyndryl
    and Sketch Consulting as speakers in video-style customer stories; the content behind those was not readable.

- id: professional-services-pursuit-proposals-09
  title: Pre-submission AI quality scoring of proposals against RFP criteria
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Reviewers who have read the same response for hours miss gaps, unanswered questions and weak sections before
    submission.
  solution: >-
    The team prompts an AI tool to score a response against the RFP's stated criteria, find gaps in coverage and flag
    inaccurate or incomplete answers as a final check.
  outcomes:
    - lever: quality
      description: "Survey-reported use only. Top performers are significantly more likely to use AI to analyse proposal quality; no outcome data."
      figure: "38% of respondents"
      measures: "Share of 1,533 respondents (all industries) saying they use AI for analysing proposal quality; the chart's 38% is the all-respondent figure."
      provenance: vendor-published
      source_ref: LOOPIO-TRENDS-2026
  prerequisites:
    - "Stated evaluation criteria and a reviewer who can judge the AI's scoring."
  risks_and_guardrails:
    - "The survey notes teams may not be measuring AI's effect on win rates (LOOPIO-TRENDS-2026, p.59)."
  human_checkpoints:
    - "A person reviews the gaps the tool flags; the Loopio blog frames it as a pre-submission gut check (LOOPIO-BLOG-2026)."
  role_evolution: >-
    Not stated in the sources beyond top performers using AI more deeply than average teams (LOOPIO-TRENDS-2026, p.67).
  evidence_grade: C
  sources:
    - { ref: LOOPIO-TRENDS-2026, title: "RFP Response Trends & Benchmarks 2026", publisher: Loopio with APMP, type: survey, url: "https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf", date: "2026-03", access: full, locator: "pp.57, 59, 67" }
    - { ref: LOOPIO-BLOG-2026, title: "AI and the Future of Proposal Management: A Look at Industry Trends", publisher: Loopio, type: vendor, url: "https://loopio.com/blog/how-are-proposal-teams-adopting-ai/", date: "2026-04-14", access: full, locator: "item 5, Analyze Proposal Quality" }
  last_reviewed: "2026-10-19"
  notes: >-
    No named professional-services firm using AI quality scoring was found. The survey covers all industries
    (IT and software dominate) and is vendor-published.

- id: professional-services-pursuit-proposals-10
  title: Data-informed staffing and fee scenarios inside proposals (idea)
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [expert-judgment, data-reporting]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Fee quotes in RFP responses rest on partner judgment and guesswork about comparable past matters, while clients
    ask for alternative fee arrangements.
  solution: >-
    AI analyses historical billing data and prior proposals to benchmark similar matters, model staffing approaches and
    offer several fee scenarios supported by comparable-matter data. Idea: labelled as such.
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "No figure; ABA articles describe hypothetical scenarios."
      provenance: self-reported
      source_ref: ABA-LPMRFP-2026
  prerequisites:
    - "Clean historical billing and matter data (the ABA column warns inaccurate data skews outputs)."
  risks_and_guardrails:
    - "Data bias toward past low-profit work, and incomplete case-management data (ABA-LPMAI-2026, Cautions)."
  human_checkpoints:
    - "Pricing specialists and partners discuss the scenarios with the client (ABA-LPMRFP-2026, How Law Firms Are Using AI in RFP Responses)."
  role_evolution: >-
    Described as supporting conversations between proposal teams, pricing specialists and partners; no role change
    stated (ABA-LPMRFP-2026).
  evidence_grade: D
  sources:
    - { ref: ABA-LPMRFP-2026, title: "How AI Is Changing the Process of Law Firm Request for Proposals (RFP)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals", date: "2026-07", access: full, locator: "pricing and staffing analysis; Real-World Scenarios" }
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "item 8" }
  last_reviewed: "2026-10-19"
  notes: >-
    Idea. The ABA July/August article says some firms are experimenting but names none, and its scenarios are generic
    ("a mid-sized firm"). Main home is scoping-pricing; kept here because the fee proposal is part of the response.

- id: professional-services-pursuit-proposals-11
  title: AI-moderated win/loss interviews after pitches
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [client-interaction, data-reporting]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Clients tell the pitching partner what they want to hear, and firms rarely collect structured reasons for wins and
    losses. Partners' time to run debrief calls is scarce.
  solution: >-
    An AI interviewer contacts the decision-maker after each pitch, asks what drove the decision, how the proposal
    compared and where pricing landed, and turns the answers into a report. Pattern is other: AI-run interviews feeding
    analysis.
  outcomes:
    - lever: quality
      description: "none published; the vendor's documentation says firms that run win/loss research systematically win more of the next ten pitches, with no data."
      figure: "none published"
      measures: "No figure; unsupported vendor assertion."
      provenance: vendor-published
      source_ref: KOJI-PSDOCS-2026
  prerequisites:
    - "Client willingness to take an AI-moderated interview; a defined question set (scale, ranking and open questions)."
  risks_and_guardrails:
    - "None stated by the vendor. Interview quality, bias and client acceptance are unmeasured in the sources."
  human_checkpoints:
    - "Leadership reads the report; the source does not describe a review step."
  role_evolution: >-
    The vendor says partners no longer need to schedule the debrief call; no customer evidence (KOJI-PSDOCS-2026).
  evidence_grade: C
  sources:
    - { ref: KOJI-PSDOCS-2026, title: "AI-Powered Client Research for Professional Services Firms", publisher: Koji, type: vendor, url: "https://www.koji.so/docs/ai-research-for-professional-services", date: "2026-07-08", access: full, locator: "The four client-research moments, 1. Pitch win-loss" }
    - { ref: KANTIV-SMPSQ2-2026, title: "What the SMPS Q2 AI Report Means for AEC Pursuit Teams", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/blog/smps-q2-ai-report", date: "2026-07-13", access: full, locator: "Your firm's AI advantage compounds (win and loss intelligence)" }
  last_reviewed: "2026-10-19"
  notes: >-
    No named professional-services firm using AI win/loss was found. Date is the page's dateModified. The Kantiv post
    names win and loss intelligence as part of the context an AEC firm should build, as reported from the SMPS report
    (secondary). Loopio reports 17% of teams cite improved win rate as an AI benefit but gives no win/loss method data.

- id: professional-services-pursuit-proposals-12
  title: In-house outside-counsel RFP scoping and proposal comparison agent
  archetype: professional-services
  module: pursuit-proposals
  function: risk-compliance-legal
  work_types: [research-synthesis, review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    In-house (legal department) teams scatter the information needed to choose outside counsel across systems, receive
    long narrative proposals, and struggle to scope matters so firms can bid comparably.
  solution: >-
    Priori's Scout agent analyses a matter, recommends a sourcing path (in-house, ALSP, panel or RFP), builds the RFP,
    collects responses and compares proposals through structured evaluation. An ABA article describes similar buyer
    uses: comparative summaries of ten firms' submissions and follow-up questions for panel interviews.
  outcomes:
    - lever: speed
      description: "none published; announcement only"
      figure: "none published"
      measures: "No figure."
      provenance: vendor-published
      source_ref: PRIORI-SCOUT-2026
  prerequisites:
    - "Defined rules of engagement, panel strategy and pricing guidelines; historical billing and firm data in the platform."
  risks_and_guardrails:
    - "Priori says final decisions remain with legal professionals (PRIORI-SCOUT-2026)."
    - "In-house legal teams asking what AI firms use and how it creates savings (GSK at Legalweek 2026, TRI-LEGALWEEK-2026) mean the same data may enter evaluation."
  human_checkpoints:
    - "Legal team makes the final firm selection (PRIORI-SCOUT-2026)."
  role_evolution: >-
    Legal operations teams move from reading each submission to reviewing comparisons and differences, in the ABA
    article's scenarios (ABA-LPMRFP-2026, How Legal Departments Are Using AI); the article gives no named example.
  evidence_grade: C
  sources:
    - { ref: PRIORI-SCOUT-2026, title: "Priori Adds New AI Capabilities to RFP Platform to Bring Greater Structure to Outside Counsel Selection", publisher: Priori, type: vendor, url: "https://www.priorilegal.com/blog/priori-adds-new-ai-capabilities-to-rfp-platform-to-bring-greater-structure-to-outside-counsel-selection/", date: "2026-04-07", access: full, locator: "release body" }
    - { ref: ABA-LPMRFP-2026, title: "How AI Is Changing the Process of Law Firm Request for Proposals (RFP)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals", date: "2026-07", access: full, locator: "How Legal Departments Are Using AI in the RFP Process" }
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: "2026-03-13", access: full, locator: "GSK panel remarks" }
  last_reviewed: "2026-10-19"
  notes: >-
    In-house. Buyer side of the pursuit process. The Priori release was read through the r.jina.ai mirror (globenewswire
    returned 403). ABA cites CLOC survey figures: 27% of legal departments use dedicated legal RFP tools and 46% run
    structured law-firm performance evaluations (ABA-LPMRFP-2026, Where the RFP Process Is Heading; the CLOC report year
    is not stated in that passage; the article cites the 2024 report earlier). The scenarios in the ABA article are
    unnamed. No named legal department reporting results was found.

- id: professional-services-pursuit-proposals-13
  title: Outside counsel guideline and RFP terms risk flagging (idea)
  archetype: professional-services
  module: pursuit-proposals
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Client outside counsel guidelines and RFP terms contain billing, staffing, data security and indemnity clauses
    that can be deal-breakers and are reviewed late and by hand.
  solution: >-
    AI cross-references the client's guidelines against the firm's standard terms and produces a dashboard marking
    clauses as standard, needs-review or potential deal-breaker. Idea: labelled as such.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "No figure; a practitioner column proposes the use."
      provenance: self-reported
      source_ref: ABA-LPMAI-2026
  prerequisites:
    - "The firm's standard terms and risk positions in a form the tool can compare."
  risks_and_guardrails:
    - "Same cautions as other AI proposal uses: use a tool that does not train on firm data; check output (ABA-LPMAI-2026, Cautions)."
  human_checkpoints:
    - "Lawyers review flagged clauses; the column does not say who."
  role_evolution: "Not stated in the source."
  evidence_grade: D
  sources:
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "item 6, Compliance and Risk Flagging" }
  last_reviewed: "2026-10-19"
  notes: >-
    Idea. Overlaps acceptance-risk (terms and risk review at bid stage); kept here because it happens inside the
    response. No firm using it was found.

- id: professional-services-pursuit-proposals-14
  title: PSA-native sales agents for RFP responses, deal coaching and estimates
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [document-production, data-reporting]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >-
    Estimates, bids and call notes sit apart from delivery actuals, so pricing and scope in proposals rely on templates
    or judgment rather than what past engagements really cost.
  solution: >-
    Certinia's Veda agent catalogue on a Salesforce-native professional services system includes an RFP Responder
    agent that drafts tailored responses, an Estimate Creation agent, a Deal Coach, and call summary and coaching
    agents. Certinia says estimates and pricing are grounded in the actuals of every prior engagement.
  outcomes:
    - lever: quality
      description: "none published; product page claims only"
      figure: "none published"
      measures: "No figure."
      provenance: vendor-published
      source_ref: CERTINIA-VEDA-2026
  prerequisites:
    - "Delivery, time and financial actuals in the same platform."
  risks_and_guardrails:
    - "None described on the product page."
  human_checkpoints:
    - "Not stated."
  role_evolution: "Not stated."
  evidence_grade: C
  sources:
    - { ref: CERTINIA-VEDA-2026, title: "Certinia AI: Veda agents", publisher: Certinia, type: vendor, url: "https://certinia.com/solutions/ai", date: "2026-10", access: full, locator: "Sell agent list; Protect margin before it's lost" }
  last_reviewed: "2026-10-19"
  notes: >-
    Page is undated; 2026-10 is the access month. No customer story was found for the RFP Responder agent. Estimate and
    resourcing agents are routed to scoping-pricing and staffing-resourcing.
```

---

## 3. Module notes

### Processes and key steps (with work types)
Synthesised from the Loopio report, the firm case studies and the ABA columns; the sources do not give one canonical list.

- Opportunity intake and go/no-go (expert-judgment, data-reporting). 75% of surveyed teams use a go/no-go process; use is at its lowest since 2021 (LOOPIO-TRENDS-2026, Ch.1).
- RFP shredding, requirements and compliance matrix (review-assurance).
- Retrieval of past answers, bios, matter experience and CVs (research-synthesis). The step most case studies attack.
- Drafting and SME coordination (document-production, coordination-scheduling).
- Pricing and staffing proposal (expert-judgment, data-reporting); belongs mostly to scoping-pricing.
- Review, tailoring and approval (review-assurance).
- Production and submission: formatting, templates, portals (document-production, transaction-processing). 45% of RFPs are submitted through online portals (LOOPIO-TRENDS-2026, Ch.5).
- Pitch and oral preparation (research-synthesis, client-interaction).
- Debrief, win/loss and library update (data-reporting).

### Common pain points
- Bandwidth: 50% of respondents rank having enough bandwidth as a top challenge, ahead of other challenges for the first time (LOOPIO-TRENDS-2026, Top Trends).
- Volume and selectivity: teams averaged 166 RFP submissions, 68% received more RFPs, and the share of RFPs responded to was 55%, the lowest in the report's history. Management consulting responded to the most RFPs: an average of 229 in 2025 against 155 in 2024 (LOOPIO-TRENDS-2026, pp.16-19).
- Scattered content and stale bios: Cherry Bekaert, GRSM, Stinson and Woodard and Curran all describe copy-paste from old documents and multiple content sources.
- Chasing SMEs; formatting and branding rework (Neudesic, ikaun's 2025 survey says over 50% cite branding and formatting, LEGALIT-IKAUN-2025).

### Metrics and benchmarks (with sources)
- Average 33 hours per RFP response, 35 for top performers, down from 35 the year before (LOOPIO-TRENDS-2026, Ch.3). Average win rate 39%, down from 45% (Ch.2). All figures are cross-industry survey responses.
- 79% of teams used AI in the last 12 months, up from 68% in 2024 and 34% in 2023; 84% of those use it weekly and 43% daily (LOOPIO-TRENDS-2026, p.56).
- Tools used: ChatGPT 57%, Microsoft Copilot 57%, RFP software with built-in AI 43% (up from 33%) (LOOPIO-TRENDS-2026, p.58).
- Top AI benefits: reduced response time 47%, improved quality or consistency 40%, improved win rate 17% (LOOPIO-TRENDS-2026, p.59).
- RFPs influenced 40% of average company revenue; management consulting about half (LOOPIO-TRENDS-2026, Ch.2).
- Responsive's 2026 report (more than 1,100 respondents) says 81% of its "SRM Leaders" use AI tools against 60% of "Novices" and that 6 in 10 say all or most of these tools already deliver positive ROI; detail is gated (RESPONSIVE-SRM-2026).
- Law firms: ikaun's 2025 vendor survey says 79% of firms rely on mostly or entirely manual proposal processes and 68% bypass official tools; sample size not given (LEGALIT-IKAUN-2025). ikaun's 2026 report (27% of firms actively use AI in proposals, 74% lack one source of truth for matter experience) is quoted only in a vendor blog and the report was not opened (IKAUN-SIXTOOLS-2026).
- Quality evidence: none independent. No error rate, override rate, hallucination rate in proposals, parallel run or inspection result was found. Versent says it ran an evaluation to benchmark domain expertise before deployment but publishes no result (VERSENT-BIDASSISTANT-2025). The only outcome-adjacent evidence is the Loopio observation that quality gains are not showing up as win-rate gains.

### Guardrails and regulatory points
- UK Cabinet Office PPN 02/24 (March 2024): suppliers' AI use in bids is not prohibited; authorities may ask for disclosure, set controls so bidders do not use confidential tender information as training data, do proportionate due diligence, and allow more time for a rise in responses (UKGOV-PPN0224-2024, para 7). It applies to central government bodies; others may adopt it.
- Evaluator side: a June 2026 Bradley commentary says federal evaluators may use generative AI to summarise proposals without telling offerors, which it says creates bid-protest risk, and advises contractors to read debriefs for signs (NATLAW-BRADLEY-2026). This is a legal commentary about risk, not evidence of widespread practice.
- Firm practice: use secure tools only, validate claims, check bios, awards and past-matter descriptions (ABA-LPMAI-2026); Cherry Bekaert only reuses validated content (LOOPIO-CHERRYBEKAERT-2026).
- Client-facing: RFPs now ask firms which AI tools they use, how they are governed, whether client data trains models and what savings result (ABA-LPMRFP-2026). GSK told Legalweek panels it asks outside firms what they use, how, and how it generates savings (TRI-LEGALWEEK-2026).

### Frontier signals (dated and sourced)
- 2026-04-07: Priori announces Scout, an agent for outside-counsel sourcing from intake to RFP evaluation (PRIORI-SCOUT-2026).
- 2026-04-16: Introhive announces a commercial preview of an MCP server for pitch preparation and cross-sell with assistants such as Copilot (INTROHIVE-MCP-2026).
- 2026-06-23: Harvey publishes a business-development guide with a won-pitch example (HARVEY-BDBLOG-2026).
- 2026-07-13: a vendor summary of the SMPS Foundation Q2 2026 AI report says agentic AI for proposals was the highest-scored AI trend, and notes a backlash against generic "AI slop" (KANTIV-SMPSQ2-2026; secondary).
- 2026-07-15: Intapp makes Celeste generally available, with BD and origination playbooks (LAWNEXT-CELESTE-2026).
- 2026: Stinson says it is preparing to adopt agentic capabilities for compliance validation and scoring (IKAUN-STINSON-2026; undated page).
- 2026-10-13: Introhive's partner survey says 57% of partners sit at BD maturity stage 1 or 2 and 84% expect AI-driven BD within 18 to 24 months (INTROHIVE-LAWSITES-2026). Expectation, not deployment.
- Scheduled, not given: a Legalweek 2026 session titled "RFP 3.0: How Firms and Clients Co-Create AI-Powered Proposals and Pick Winners" was found in search snippets only; the page could not be opened and it is not used for any grade.

### Workforce and role effects
- Teams are mostly not cutting people: 16% say they replaced internal people resources with AI and 16% external; 32% say leadership expects new responsibilities and 42% better results; 27% say AI has not changed roles (LOOPIO-TRENDS-2026, p.61). Associate-level respondents are more likely than senior staff to say AI has not affected their role (p.61).
- 51% of teams say they will need AI and automation skills in 2026 (LOOPIO-TRENDS-2026, Top Trends).
- New role titles: "Proposal Manager (RFX and AI Orchestration)" with human-in-the-loop validation (RANDSTAD-PROPOSALMGR-2026); "Sr. Manager, Pursuit and Sales Asset Leader" at Cherry Bekaert, who built the firm's first dedicated proposal function (LOOPIO-CHERRYBEKAERT-2026).
- A search result (not opened; see Gaps) describes a Deloitte "Proposal Studio Manager" role overseeing pursuit support specialists who draft first-pass responses using generative AI.
- Participation widens: GRSM says the whole team can now execute proposals (IKAUN-GRSM-2026); Benesch has nearly 400 technical staff using the tool (KANTIV-BENESCH-2026).

### Objections and concerns practitioners raise
- Accuracy and claims risk: firms cannot make unverified claims (Cherry Bekaert); check success stories, awards and bios (ABA-LPMAI-2026).
- Data security with general tools: 57% use ChatGPT or Copilot (LOOPIO-TRENDS-2026).
- Sameness: selection committees recognise generic AI output (KANTIV-SMPSQ2-2026, secondary); Loopio advises personalising because buyers see more AI-generated content (LOOPIO-BLOG-2026).
- No win-rate proof: quality gains are claimed but win rates fell in the survey (LOOPIO-TRENDS-2026).
- Leadership expectations rising without more resources (LOOPIO-TRENDS-2026, p.61).
- Disclosure and client attitudes: some clients take restrictive views of AI use; the ABA column advises disclosing AI assistance with oversight (ABA-LPMAI-2026, Cautions).
- Tool sprawl and AI memory that does not carry across a pursuit team (KANTIV-SMPSQ2-2026; vendor summary).
- Build versus buy: a vendor argues that custom Copilot agents hit taxonomy, fact-verification, production and maintenance gaps, and that credit consumption is metered (KANTIV-COPILOT-2026; vendor opinion).

### Interview probes for an advisor
1. Walk me through the last bid you decided not to pursue. Who decided, on what data, and how much of that data lived in a system rather than in people's heads?
2. Where does your approved content live, who owns each piece, and how do you stop an AI tool drafting from something stale or unapproved?
3. After AI, what did you do with the saved hours: more bids, more tailoring, or more senior review? How do you know, and has your win rate moved?
4. How does your team answer client questions about your own AI use, and who signs off on those answers?
5. Who on your team now drafts first (proposal staff, partners, SMEs), and what happened to the work juniors used to do on bids?

---

## 4. Routed to other modules

- **client-development (client-relationship-development):** Introhive's survey of 123 partners (78% find relationship data hard to act on; 47% name surfacing new business as the capability they want most; 63% of firms have no revenue-linked way to measure BD return) and the MCP server (INTROHIVE-LAWSITES-2026, INTROHIVE-MCP-2026); TRI's Stand-out Lawyers finding that only about one-third of embedded-AI partners have discussed AI with at least 60% of clients (TRI-STANDOUT-2026); Intapp coverage and relationship management in DealCloud (INTAPP-DEALCLOUD-2026).
- **scoping-pricing:** fee-scenario modelling (use case 10); Certinia Estimate Creation and Estimation agents (CERTINIA-VEDA-2026); Priori's pricing guidance for matters (PRIORI-SCOUT-2026); GSK's savings questions (TRI-LEGALWEEK-2026).
- **acceptance-risk:** BakerHostetler's Celeste use on intake and conflicts (LAWNEXT-CELESTE-2026); outside counsel guideline review (use case 13).
- **knowledge-management:** the experience, CV and matter databases (Arup People, Gowling WLG, GRSM Trial Tracker) are knowledge-management assets as much as pursuit tools (IKAUN-ARUP-2026, IKAUN-GOWLING-2026, IKAUN-GRSM-2026).
- **staffing-resourcing:** Arup's expert finder and Neudesic's matching of consultants to roles (IKAUN-ARUP-2026, IKAUN-NEUDESIC-2026).
- **talent-learning:** onboarding of new team members with AI (Robins and Morton, KANTIV-ROBINS-2026; Loopio's 15% of respondents using AI for onboarding, LOOPIO-TRENDS-2026, p.57).
- **quality-review:** evaluator-side AI use and protest risk (NATLAW-BRADLEY-2026).

---

## 5. Sources

All 37 were opened (access: full) unless noted. "Mirror" means `curl` was blocked and the page was read through r.jina.ai. Dates marked "page undated" use the year or month of access or an inferred date; the entry says how.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| LOOPIO-TRENDS-2026 | 2026 RFP Response Trends & Benchmarks Report | Loopio with APMP | survey | https://link.loopio.com/hubfs/Content%20Pieces/FY26%20Trends%20Report/trends-report-2026-digital-Master.pdf | 2026-03 (PDF created 2026-03-10) |
| LOOPIO-CHERRYBEKAERT-2026 | How Cherry Bekaert Scaled to 550 RFPs a Year, With Loopio | Loopio | vendor | https://loopio.com/case-study/cherry-bekaert/ | 2026-10-08 |
| LOOPIO-BLOG-2026 | AI and the Future of Proposal Management | Loopio | vendor | https://loopio.com/blog/how-are-proposal-teams-adopting-ai/ | 2026-04-14 |
| RESPONSIVE-SRM-2026 | 2026 State of Strategic Response Management Report (landing page; report gated) | Responsive | survey | https://www.responsive.io/resources/whitepapers/srm-report-2026 | 2026 (page undated) |
| CERTINIA-VEDA-2026 | Certinia AI: Veda agents | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10 (page undated) |
| AUTOGENAI-CUSTOMERS-2026 | AutogenAI customers | AutogenAI | vendor | https://autogenai.com/customers/ | 2026 (page undated) |
| AUTOGENAI-BIG4-2025 | Fastest Growing Big 4 Professional Services Firm case study (unnamed firm) | AutogenAI | vendor | https://autogenai.com/wp-content/uploads/2025/07/Professional-Services-Firm-Case-Study.pdf | 2025-07 (upload path) |
| AUTOGENAI-SERCO-2025 | Serco Increases Efficiency by 85% and Global Revenue by 5% with AutogenAI | AutogenAI | vendor | https://autogenai.com/wp-content/uploads/2024/09/Serco-Increases-Efficiency-by-85-and-Global-Revenue-by-5-with-AutogenAI.pdf | 2025-03 (PDF created 2025-03-27) |
| INTROHIVE-LAWSITES-2026 | Partners Want AI to Help Them Find New Business, But Most Are Running It on Data They Can't Use | LawSites | press | https://www.lawnext.com/2026/10/partners-want-ai-to-help-them-find-new-business-but-most-are-running-it-on-data-they-cant-use-introhive-survey-finds.html | 2026-10-13 |
| INTROHIVE-MCP-2026 | Introhive Announces MCP Server for Legal AI | Introhive | vendor | https://www.introhive.com/news/introhive-announces-mcp-server-for-legal-ai-enables-copilots-and-ai-agents-with-real-time-relationship-intelligence/ | 2026-04-16 |
| ABA-LPMRFP-2026 | How AI Is Changing the Process of Law Firm Request for Proposals (RFP) (Prinn, Windmoeller); mirror | ABA Law Practice magazine | professional-body | https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals | 2026-07 (July/August issue) |
| ABA-LPMAI-2026 | Leveraging AI to Respond to Requests for Proposals (RFPs) (Marketing Column); mirror | ABA Law Practice magazine | professional-body | https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps | 2026-03 (March/April issue) |
| IKAUN-SIXTOOLS-2026 | Six Best AI Tools for Legal Proposal Teams in 2026 | ikaun | vendor | https://www.ikaun.com/blogs/six-best-ai-tools-for-legal-proposal-teams-in-2026 | 2026-08-26 |
| IKAUN-CASEINDEX-2026 | Case Studies: How Legal & AEC Firms Win More Business with ikaun | ikaun | vendor | https://www.ikaun.com/case-studies | 2026 (page undated) |
| IKAUN-GRSM-2026 | ikaun Helps Am Law 100 Firm GRSM Cut Proposal Time by 50% in Four Months | ikaun | vendor | https://www.ikaun.com/case-studies/ikaun-helps-am-law-100-firm-grsm-cut-proposal-time-by-50-in-four-months | 2026 (page undated) |
| IKAUN-ARUP-2026 | Leveraging Global Capability through Arup People | ikaun | vendor | https://www.ikaun.com/case-studies/leveraging-global-capability-through-arup-people | 2026 (page undated) |
| IKAUN-NEUDESIC-2026 | ikaun Transforms Sales Operations and Redefines Efficiencies for Neudesic | ikaun | vendor | https://www.ikaun.com/case-studies/ikaun-transforms-sales-operations-and-redefines-efficiencies-for-neudesic | 2026 (page undated) |
| IKAUN-STINSON-2026 | Winning More Time for Strategy: How Stinson is Transforming RFP and Proposal Responses with ikaun | ikaun | vendor | https://www.ikaun.com/case-studies/winning-more-time-for-strategy-how-stinson-is-transforming-rfp-and-proposal-responses-with-ikaun | 2026 (page undated) |
| IKAUN-GOWLING-2026 | ikaun's World Class Experience Management Solution ... Gowling WLG | ikaun | vendor | https://www.ikaun.com/case-studies/ikauns-world-class-experience-management-solution-drives-business-value-throughout-global-law-firm-gowling-wlg | 2026 (page undated) |
| LEGALIT-IKAUN-2025 | ikaun releases 2025 State of Proposal Generation and BD in Law Firms report | Legal IT Insider | press | https://legaltechnology.com/ikaun-releases-2025-state-of-proposal-generation-and-bd-in-law-firms-report/ | 2025-06-17 |
| VERSENT-BIDASSISTANT-2025 | Accelerating RFP Response with GenAI; mirror | Versent | firm | https://versent.com.au/case-studies/accelerating-rfp-response-with-genai/ | 2025 (page undated; image paths 2025/08) |
| LAWNEXT-CELESTE-2026 | Intapp Makes Celeste Generally Available | LawSites (Ambrogi) | press | https://www.lawnext.com/2026/07/intapp-makes-celeste-generally-available-calling-it-an-ai-coworker-to-run-the-business-side-of-law-firms.html | 2026-07-16 |
| INTAPP-DEALCLOUD-2026 | Intapp DealCloud; mirror | Intapp | vendor | https://www.intapp.com/dealcloud/ | 2026 (page undated) |
| KANTIV-SMPSQ2-2026 | What the SMPS Q2 AI Report Means for AEC Pursuit Teams | Kantiv | vendor | https://www.kantiv.com/blog/smps-q2-ai-report | 2026-07-13 |
| KANTIV-GONOGO-2026 | How to calibrate your go/no-go matrix using your own wins and losses | Kantiv | vendor | https://www.kantiv.com/blog/blog-go-no-go-scorecard-matrix | 2026-10-15 |
| KANTIV-COPILOT-2026 | Custom Copilot Agents: What it actually takes to build agents that can handle pursuits | Kantiv | vendor | https://www.kantiv.com/blog/copilot-custom-agent-for-aec-proposals | 2026-09-26 |
| KANTIV-BENESCH-2026 | Benesch's Pursuit AI Evolution | Kantiv | vendor | https://www.kantiv.com/case-study/beneschs-ai-evolution-smarter-search-faster-content-and-greater-efficiency | 2026-06 (page metadata) |
| KANTIV-ROBINS-2026 | Robins & Morton: Unlocking Institutional Knowledge with Kantiv | Kantiv | vendor | https://www.kantiv.com/case-study/robins-morton-unlocking-institutional-knowledge-with-kantiv | 2026-06 (page metadata) |
| KANTIV-WOODARD-2026 | How Kantiv Transformed Pursuit Management at Woodard & Curran | Kantiv | vendor | https://www.kantiv.com/case-study/a-strategy-to-streamline-how-kantiv-transformed-proposal-management-at-woodard-curran | 2026-06 (page metadata) |
| UKGOV-PPN0224-2024 | Procurement Policy Note 02/24: Improving Transparency of AI use in Procurement | UK Cabinet Office | regulator | https://assets.publishing.service.gov.uk/media/66019771a6c0f7bb15ef9252/PPN_02_24_Improving_Transparency_of_AI_use_in_Procurement.pdf | 2024-03 |
| HARVEY-BDBLOG-2026 | AI for Law Firm Business Development | Harvey | vendor | https://www.harvey.ai/blog/ai-for-law-firm-business-development | 2026-06-23 |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026 | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice: 2026 Stand-out Lawyers Survey | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 |
| PRIORI-SCOUT-2026 | Priori Adds New AI Capabilities to RFP Platform; mirror | Priori | vendor | https://www.priorilegal.com/blog/priori-adds-new-ai-capabilities-to-rfp-platform-to-bring-greater-structure-to-outside-counsel-selection/ | 2026-04-07 |
| KOJI-PSDOCS-2026 | AI-Powered Client Research for Professional Services Firms | Koji | vendor | https://www.koji.so/docs/ai-research-for-professional-services | 2026-07-08 (dateModified) |
| NATLAW-BRADLEY-2026 | Shadow AI in Government Contract Proposal Evaluations: Emerging Bid Protest Risks | National Law Review (Bradley Arant Boult Cummings) | press | https://natlawreview.com/article/shadow-ai-government-contract-proposal-evaluations-emerging-bid-protest-risks | 2026-06-08 |
| RANDSTAD-PROPOSALMGR-2026 | Proposal Manager (RFX and AI Orchestration), Brentford | Randstad | job-posting | https://www.randstad.com/jobs/proposal-manager_brentford_47525616/ | 2026-09-30 |

Counts by type: vendor 24, survey 3, press 4, professional-body 2, conference 1, regulator 1, firm 1, job-posting 1 (total 37).

Sources seen only in search results (not opened, no grade depends on them): Deloitte US India Offices "Manager, Sales Excellence Proposal Studio" posting (usijobs.deloitte.com, requisition id in URL; page returned 404 and 403 on retry); Legalweek 2026 "RFP 3.0" session page (event.law.com); ikaun 2026 State of Winning Work in Law Firms report; SMPS Foundation AI Quarterly Insight Report Q2 2026.

---

## 6. Gaps

- **Search budget.** Twelve searches were used; the shared limit was then reached before a planned search for primary Big Four, McKinsey, BCG or Accenture pursuit-tool announcements. No such primary source was found, so large-consultancy pursuit practice is represented only by an unnamed Big 4 case study (AutogenAI) and the landscape's secondary items.
- **Quality evidence.** None found: no error rates, override rates, hallucination counts in proposals, parallel runs, win-rate studies or independent measurement. Loopio's survey is the only systematic data and it is cross-industry, vendor-run and self-reported.
- **Job postings.** Only one opened posting (Randstad, employer not named). The Deloitte proposal-studio posting was seen in search only and its page was unavailable. No postings from law firms, accounting firms or MBB consultancies were found, and Greenhouse board checks for a few services firms returned no proposal roles.
- **Undated pages.** The five ikaun case-study pages, Versent, Certinia, DealCloud and the AutogenAI customer page show no publication date; dates are inferred and marked.
- **Not accessible.** americanbar.org blocked `curl` (read through the mirror); the Intapp case-study library (403); Priori's wire release (403); SMPS Foundation Q2 2026 report (members only); Loopio, Responsive and ikaun full reports (gated or not opened); the Legalweek RFP 3.0 session page; the AutogenAI Jacobs and Kyndryl customer stories.
- **Win/loss analysis.** No named professional-services firm using AI for win/loss was found; only vendor product documentation.
- **Credentials and experience data.** The sources are vendor case studies; much of what they describe is data-driven document generation, and whether generative AI is involved is not always stated.
- **Legal-department buyers.** No named in-house team reporting results from AI-assisted RFP evaluation; only a vendor announcement and generic scenarios.
- **Consulting and accounting depth.** Cherry Bekaert, Neudesic, Arup, Versent and Woodard and Curran are the only non-law named examples; no public example from a Big Four or mid-tier consultancy beyond the unnamed one.
- **Discrepancies noted.** Loopio blog says 47% of leaders expect better results; the report says 42% (report used). AutogenAI's customer page says Serco global revenue rose 5%; the Serco PDF says win rates rose 5%. The GRSM headline says 50% in four months; the quote says over 50% in the first quarter after go-live.

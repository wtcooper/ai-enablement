# Secure enablement (step 7)

Read this on entering step 7. It moves IT, security and risk from listing risks and blocking to providing approved
tools with a fast request path, built-in controls, a review cadence and clear owners. It also closes the policy:
exceptions, incidents, training and acknowledgement, measures and maintenance. Source keys in brackets are listed in
§9.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [Expert moves](#4-expert-moves)
5. [Checklists and decision rules](#5-checklists-and-decision-rules)
6. [Common traps](#6-common-traps)
7. [Worked example](#7-worked-example)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** Governance people use instead of going around. Practitioner playbooks describe the shift as providing
approved tools with single sign-on, logging and data controls, a request path, and discovery of what is already in use
[GEND-2026; AMPCUS-2026; both vendor blogs, directional]. The evidence for the shift is the survey data on bypass
behaviour, not the blogs: the University of Melbourne and KPMG authors say their findings suggest bans may be
ineffective and that a policy does not guarantee compliance [KPMG-MELB-2025, p.75].

**Exit when all of these are true:**
- **An AI lead or committee** with named jobs, by role.
- **A request path:** where requests go, the triage lanes, and a stated response commitment.
- **An expedited lane** for urgent work with minimum controls and logged exceptions.
- **Re-approval triggers and a review cadence** for the policy, the catalog and the assessments.
- **Exceptions and incidents:** who grants, how logged; how to report, correct, disclose and re-review.
- **Training and acknowledgement** by role, and how compliance is sampled (handed to ai-enablement for design).
- **Measures** the owner will report.
- **The policy marked ready for approval** (`status: in-review`) and the guardrails file consistent with it.

## 2. How to run it

1. **Name the AI lead or committee and its jobs** (move 1). In a partnership, put respected practice leaders on it,
   not only IT (move 6).
2. **Design the request path** with three lanes (§5). Ask what response time the owner can commit to and keep; do
   not invent a number.
3. **Design the expedited lane** (move 2): the minimum controls that always apply, and how exceptions are logged.
4. **Build controls into the approved tools** rather than relying on memory (move 3).
5. **Set re-approval triggers and the review cadence** (move 4).
6. **Write exceptions and incidents** (§5).
7. **Set training and acknowledgement** and hand the program design to the ai-enablement skill.
8. **Agree the measures** (§5) and who reports them, in which meeting.
9. **Play back the whole policy**, regenerate `overlay/guardrails.md` from it, set `status: in-review`, and suggest
   who should approve it.

## 3. Question bank

| # | Question | Scope |
|---|---|---|
| S1 | Who owns the tool catalog, the request path and the response commitment? | [O] |
| S2 | What did the last urgent deployment skip? | [U/O] |
| S3 | Which controls can the approved tools enforce themselves: single sign-on, logging, retention, data-loss prevention? | [U/O] |
| S4 | What are our re-approval triggers, and how often do we review the policy and the catalog? | [O] |
| S5 | What training and acknowledgement will each role complete before access, and how will we sample compliance? | [O] |

More, as needed:
- What are our exit and failure plans for each approved tool? [U/O]
- Which incidents or near misses have we logged, and who reviews them? [O]
- Which use cases are low data-class, low-consequence and quick to approve? [U]
- What would partners need to see to back the request path over a ban? [O]

## 4. Expert moves

1. **Name an AI lead or committee with five jobs: review use cases, approve tools, maintain the policy, monitor
   compliance, handle incidents.** Setup. Reveals who answers the staff question "can I use this?" [CPAI-2026].
2. **Ask "what did the last urgent deployment skip?" and design an expedited lane instead of relying on exceptions.**
   Stress test. 47% of surveyed senior AI executives said their organization had previously not applied its governance
   process to urgent deployments, while 98% had formal policies (EY-commissioned survey of 202 senior AI executives at
   US public companies with at least $1 billion revenue; self-reported) [EY-AIGOV-2026]. The lane design is an advisor
   default.
3. **Build the controls into the tool.** Rollout. Single sign-on, logging, retention and data-loss prevention in the
   approved tool do the work staff memory cannot [GEND-2026, directional]; inventories should include AI features
   inside approved software [NIST-600-1-2024, GV-1.6-002].
4. **Re-run the assessment on a schedule and on triggers.** Maintenance. Microsoft's own responsible AI standard
   requires impact assessments to be updated at least annually, when new intended uses are added, and before a
   release stage advances (a named company's internal standard, used as a template) [MSFT-RAI-2022, A1.3].
5. **Replay incidents against the controls.** Incident design. A good response after an AI error is to correct,
   disclose and re-review the wider set
   (`../../transformation-advisor/references/archetypes/professional-services/guardrails.md` §7, §11).
6. **Put respected business-minded practice leaders in charge, not only technologists.** In partnerships. Partners
   are owners, so the program lead has influence rather than authority; one law-firm chair describes asking talented
   senior business leaders, not technologists, to run the business side of AI and treating it as a business problem
   rather than a tech problem (self-reported) [JOTWELL-EMPSON-2013; POLSINELLI-2026].
7. **Tie partner accountability to the professional-duty floor: policy, training, monitoring, supervision.** When a
   leader says governance is optional. ABA Opinion 512 says managerial lawyers must establish clear policies on the
   firm's permissible use of AI and supervise its use [ABA-OP512-2024]; the SRA warning, as summarised, says those
   responsible for supervision may face consequences if inadequate supervision lets false citations through
   [VINCI-2026].
8. **Make training a condition of access.** Rollout. One law firm studied by CIPD required training before use
   [CIPD-2026]; the CPAi guide recommends training with examples of what cannot be entered and how to redact
   [CPAI-2026].

## 5. Checklists and decision rules

**Request path (advisor default):**

| Lane | Qualifies when | What happens |
|---|---|---|
| Fast | Public or firm-internal data, tier-1 or tier-2 use, an existing catalog entry | Approved against the entry's conditions; logged |
| Standard | A new tool or tier, or client-confidential data | Scorecard (`references/vendor-evaluation.md`), screens, decision |
| High-tier | Tier-4 use, regulated data, agents, or a regime flag | Use-case approval record, own-sample test, regime review (step 5), then a pilot |

**Request form fields:** tool, tier and contract; proposed use and audience; data classes; runtime class and
permissions; regime flags (tax-return information, attest client, legal matter, client terms, EU staff decisions);
requester's role.

**Re-approval triggers:** model change · sub-processor change · terms change · new data class · new use · incident
(advisor default, anchored on [NIST-600-1-2024, GV-1.6-003, GV-6.1-005, GV-6.1-009]).

**Exceptions:** granted only by the role named in the policy; logged at organization level with reason, scope and
expiry condition; a unit may be stricter than the firm baseline, never looser (advisor default).

**Incidents:** one report route; correct, disclose where duties require, re-review the wider set; near misses reviewed
by the incident owner; lessons fed into the tiers and training.

**Measures (advisor default):** share of staff who can name the approved tool; request volume and turnaround;
exceptions granted; incidents and near misses. Measure the firm's own numbers; do not present other organizations'
survey percentages as its baseline.

**Roll-up across units:** one catalog, one data-class and tier matrix, one incident process, one inventory; unit
addenda only for regimes (tax, attest, legal).

**Decision rules**
- A ban with no approved alternative and no request path is not a finished policy (built on [KPMG-MELB-2025, p.75]).
- Every exception has an owner and a log entry; an unowned exception is a gap (advisor default, built on
  [EY-AIGOV-2026]).
- Usage tracking says what it is for and what it is not; it never rates individuals (core rule 1). KPMG is reported to
  say its monitoring is not discipline while adding AI use to performance assessments, which shows why the purpose
  must be explicit [IAB-KPMG-2025].

## 6. Common traps

| Trap | Evidence | How to avoid |
|---|---|---|
| Governance skipped when urgent | In EY's survey of senior AI executives at large US public companies, 47% said the process had been skipped for urgent deployments although 98% had policies (self-reported) [EY-AIGOV-2026] | An expedited lane with minimum controls; log exceptions |
| Treating the approved list as proof of control | Exposure travels through unlisted channels and AI features inside approved software (vendor blog, directional) [AMPCUS-2026] | Discovery, data-loss prevention and an inventory with embedded features [NIST-600-1-2024, GV-1.6-002] |
| Ban-first | [KPMG-MELB-2025, p.75] | Approved tool and request path first |
| Skeptics treated as blockers | Their concerns have public precedent [SDNY-AVIANCA-2023; GUARDIAN-DELOITTE-2025] | Concede the risk and show the control |

## 7. Worked example

Illustrative, not a case study. A consulting firm's baseline found staff using free tools for client emails and
meeting notes, consistent with the pattern in surveys of other organizations [KPMG-MELB-2025; MSFT-WTI-2024], which
are not this firm's data.

- **Lead:** an AI committee of two practice leaders, the IT security lead and the general counsel, with the five jobs.
- **Catalog:** business-tier entries for chat and transcription, each with data classes and conditions.
- **Request path:** fast lane for firm-internal data on catalog entries; standard lane for new tools; high-tier lane
  for anything touching client HR data. The IT security lead commits to a response time and reports turnaround.
- **Expedited lane:** for a client deadline, approved entries only, tier-3 review, exception logged with the GC.
- **Training:** short role-based sessions with redaction examples; training before access; designed with
  ai-enablement.
- **Measures:** staff who can name the approved tool; request turnaround; exceptions; incidents.

## 8. Output

Write section 8 of `overlay/policy.md`; fill every `owners` field; set `status: in-review`, `step_completed: 7`,
`next_step: null`. Set `owner` and `request_path` in `overlay/tool-catalog.yaml`. Regenerate `overlay/guardrails.md`
so every line matches the policy. Then offer the handoffs in `SKILL.md`.

## 9. Sources

- **ABA-OP512-2024**: American Bar Association, *Formal Opinion 512: Generative Artificial Intelligence Tools* (professional body, 2024-07-29). https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
- **AMPCUS-2026**: Ampcus Cyber, *Shadow AI in 2027: A Governance Checklist for Security Leaders* (vendor blog, 2026-10-16). https://www.ampcuscyber.com/blogs/shadow-ai-governance-checklist-for-security-leaders/
- **CIPD-2026**: CIPD with Institute for the Future of Work, *How a law firm introduced an AI legal assistant* (practitioner case study, 2026-03-25). https://www.cipd.org/ae/knowledge/case-studies/ai-legal-assistant/
- **CPAI-2026**: CPAi, *Drafting an AI Policy that Actually Works* (professional association guide, 2026-07). https://www.cpai.com/Education-Resources/My-Firm/Data-Security-Risk-Management/Drafting-an-AI-Policy-that-Actually-Works
- **EY-AIGOV-2026**: Ernst & Young LLP, *EY survey finds that autonomous AI implementation outpaces oversight* (consultancy survey press release, 2026-09-15). https://www.ey.com/en_us/newsroom/2026/09/ey-survey-finds-that-autonomous-ai-implementation-outpaces-oversight-yielding-an-ai-governance-gap
- **GEND-2026**: Gend, *Shadow AI security playbook for CIOs and CTOs (2026)* (vendor blog, 2026-01-08). https://www.gend.co/blog/shadow-ai-security-playbook
- **GUARDIAN-DELOITTE-2025**: The Guardian, *Deloitte to pay money back to Albanese government after using AI in $440,000 report* (news, 2025-10-06). https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report
- **IAB-KPMG-2025**: International Accounting Bulletin, *KPMG to include AI performance reviews* (trade press, secondary, 2025-11-03). https://www.internationalaccountingbulletin.com/?p=44130
- **JOTWELL-EMPSON-2013**: John Flood, JOTWELL, *How Are Professional Service Firms Governed?* (review of Empson, 2013-09-24). https://legalpro.jotwell.com/?p=653
- **KPMG-MELB-2025**: University of Melbourne with KPMG, *Trust, attitudes and use of artificial intelligence: A global study 2025* (academic with consultancy, 2025-05). https://kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf
- **MSFT-RAI-2022**: Microsoft, *Microsoft Responsible AI Standard, v2, General Requirements* (named-company internal standard, 2022-06). https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf
- **MSFT-WTI-2024**: Microsoft and LinkedIn, *AI at Work Is Here. Now Comes the Hard Part* (vendor research, 2024). https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part
- **NIST-600-1-2024**: NIST, *AI RMF: Generative AI Profile, NIST AI 600-1* (standard, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **POLSINELLI-2026**: Bloomberg Law, On the Merits, *Why Polsinelli Lawyers Won't Get Billing Credit for AI Training* (practitioner interview, 2026-03-24). https://news.bgov.com/business-and-practice/why-polsinelli-lawyers-wont-get-billing-credit-for-ai-training
- **SDNY-AVIANCA-2023**: US District Court, S.D.N.Y., *Mata v. Avianca, Inc., Opinion and Order on Sanctions* (court record, 2023-06-22). https://www.courtlistener.com/docket/63107798/54/mata-v-avianca-inc/
- **VINCI-2026**: VinciWorks, *Is SRA's AI warning a wake-up call for UK law firms?* (secondary summary, 2026-08-19). https://vinciworks.com/blog/is-sras-ai-warning-a-wake-up-call-for-uk-law-firms/

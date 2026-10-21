# Tax interview guide

Last researched 2026-10-17; mid-market and multistate questions added 2026-10-21. Use this alongside the method files: onboarding questions come from
[onboarding.md](../../method/onboarding.md), question craft from [interviewing.md](../../method/interviewing.md). This
file gives the tax wording, the field's boundary probes, phase questions and the vocabulary to mirror. Ask one question
at a time and skip what you already know. Source keys in brackets resolve in §9 or in [sources.md](sources.md).

## Contents

1. [Who you are likely talking to](#1-who-you-are-likely-talking-to)
2. [Onboarding questions in tax words](#2-onboarding-questions-in-tax-words)
3. [Choosing focus modules](#3-choosing-focus-modules)
4. [Journey-stage boundary probes](#4-journey-stage-boundary-probes)
5. [Phase questions](#5-phase-questions)
6. [In-house and mid-market variants](#6-in-house-and-mid-market-variants)
7. [Sensitive topics](#7-sensitive-topics)
8. [Vocabulary to mirror](#8-vocabulary-to-mirror)
9. [Sources](#9-sources)

## 1. Who you are likely talking to

| Person | What they usually care about | Open with |
|---|---|---|
| Tax partner or practice leader (firm) | Season capacity, review bottlenecks, realization, staffing, pricing | "Which part of the season eats the most hours or causes the most review notes?" |
| Managing partner or owner (small and mid-size firm) | Capacity, fees, succession, buyers and roll-ups, technology spend | "Why look at AI now, and what would the practice look like in three years?" |
| National office, risk or quality partner | Circular 230, section 7216, written advice, AI policy, insurance | "How do you approve tools today, and what does your policy say about client data?" |
| Head of tax or tax director (in house) | Accuracy, penalties, provision deadlines, audit committee, flat budget | "Where does your team spend its time between the close and the filing deadlines?" |
| Tax technology or tax data lead | Data feeds, engines, automations nobody can explain, ownership, token costs | "Which automations does the team run today, and who could fix one if its builder left?" |
| Indirect tax lead | Engine accuracy, product mapping, certificates, e-invoicing mandates | "Which countries or states are changing your invoicing or filing rules in the next two years?" |
| Transfer pricing lead | Documentation volume, benchmarking, operational TP, audit defence | "How many local files a year, and how much of each is rolled forward?" |
| Controversy lead | Notices, exams, Appeals, deadlines, authority analytics | "How many notices or information requests a year, and how is each one first read?" |
| Partner serving owner-managed or multistate private companies | Pass-through returns, owner basis and salary, nexus, apportionment, PTET, state letters | "Where are your clients' people actually working today, and who compares that list with their state accounts?" |

## 2. Onboarding questions in tax words

Use these in place of, or after, the starred questions in onboarding §3.

| Profile element | Question | Listen for |
|---|---|---|
| Role and scope | "Are you responsible for your own clients, a team, an office, a service line, the firm, or the whole tax department?" | Scope level; firm or in-house |
| What is delivered | "What do you sign or deliver: returns, provisions, VAT or sales tax filings, TP documentation, notice responses, advice?" | Which modules |
| Clients or the business | "Who are the clients: individuals, owner-managed businesses, partnerships, mid-market, multinationals? Or which group do you serve in house?" | Return mix; jurisdictions; data complexity |
| How it is paid | "Is the work priced per return, fixed annual fee, hourly or on value? In house, what is your budget for technology and outside advisers?" | Who keeps an AI saving ([economics.md](economics.md)) |
| Journey stage | "In the last two weeks, who used AI on real client or company work, and for which step? Could you show me where the file records it?" | Real use versus awareness |
| Pressures | "What is pushing hardest: staffing, fees, the filing calendar, new rules such as Pillar Two or e-invoicing, the tax authority's analytics, or competitors?" | Why now |
| Constraints | "What must not change: who signs, client confidentiality and consent, your methodology, what your insurer or auditor expects?" | Guardrails ([guardrails.md](guardrails.md)) |
| Tools and data | "Which tax engines and research tools do you use, and how does data reach them: exports, direct feeds, scanned documents?" | Tool estate; data readiness ([value-chain.md](value-chain.md) §3) |
| Unapproved use | "In most firms some staff use AI tools that haven't been approved. Is that happening here? There's no wrong answer." | Shadow AI: more than a third of tax and audit professionals admit it (vendor survey) [TR-FOP-2026] |
| Session goal | "What would make this worthwhile: something for next season, a plan for the practice or department, or a case for your partners or CFO?" | Path |

**Bring evidence in early.** Once you know the focus, give one real example from the relevant module with its grade,
and say who measured it. In most tax modules the honest answer is "the vendor".

## 3. Choosing focus modules

| If the user says | Module to load |
|---|---|
| "1040s", "K-1s", "organizers", "busy season", "extension season", "our preparers", "8879" | [compliance-individual-business](modules/compliance-individual-business.md) |
| "The 1120", "5471s", "state apportionment", "R&D credit", "Section G", "the tax calendar" | [compliance-corporate](modules/compliance-corporate.md) |
| "The provision", "ASC 740", "rate reconciliation", "ASU 2023-09", "Pillar Two", "the GIR", "XML" | [provision-pillar-two](modules/provision-pillar-two.md) |
| "Sales and use tax", "VAT", "nexus", "exemption certificates", "product tax codes", "e-invoicing" | [indirect-tax](modules/indirect-tax.md) |
| "Local files", "benchmarking", "intercompany agreements", "operational TP", "APA", "DEMPE" | [transfer-pricing](modules/transfer-pricing.md) |
| "Notices", "CP2000", "IDRs", "the exam", "Appeals", "the IRS's AI", "Tax Court" | [controversy](modules/controversy.md) |
| "Research memos", "opinions", "planning ideas", "M&A diligence", "Blue J", "CoCounsel", "hallucinated citations" | [research-advisory](modules/research-advisory.md) |
| "Our data feeds", "Alteryx", "the ERP project", "tax technology team", "MCP", "automations nobody owns" | [data-technology](modules/data-technology.md) |
| "S corp salary", "reasonable compensation", "basis", "Form 7203", "owner estimates" | [compliance-individual-business](modules/compliance-individual-business.md) §10 |
| "Entity choice", "S-election", "owner planning", "planning from filed returns" | [research-advisory](modules/research-advisory.md) §10 |
| "Nexus study", "apportionment", "remote employees in new states", "PTET", "composite returns", "voluntary disclosure", "a state letter" | [multistate-private](modules/multistate-private.md) |

Pick one to three. If the user leads a whole practice or department, start from [value-chain.md](value-chain.md).

## 4. Journey-stage boundary probes

Pick two or three. Markers and gates are in [ARCHETYPE.md](ARCHETYPE.md).

| Boundary | Ask | What decides it |
|---|---|---|
| Curious / Experimenting | "Is there any step where AI is part of how the work is normally done, on more than one client or entity?" | Repeated use on real work |
| | "What does your policy say about putting return data into an AI tool, and what would a senior say it says?" | Lived versus paper policy; section 7216 awareness [IRS-OPR-2026] |
| Experimenting / Adopting | "For the workflow you trust most, what is the baseline: hours per return, review notes, notices, rework?" | An owned, measured workflow |
| | "When an AI-assisted return or memo was wrong, who caught it, and how?" | A designed review step, not a stated intention |
| | "Where is it recorded which tool was used, on what, and how the output was checked?" | Documented procedures (OPR's section 10.36 reading) [IRS-OPR-2026] |
| Adopting / Scaling | "Does your second AI workflow reuse anything from the first: the data feed, the review checklist, the vendor review?" | Reuse |
| | "Who owns tax AI here: tax, finance IT, a central AI team? Who pays the model costs?" | Ownership; two of 50+ at TEI said tax owns it [TEI-TAXTECH-2026] |
| Scaling / AI-native | "Has AI changed how you price, staff or scope any service, or let you sell something new?" | Commercial change |
| Delegation check | "Is any agent preparing or filing without a person checking each item? What are the written rules, and what is the override rate?" | The five gates in onboarding §5 |

## 5. Phase questions

Use these in addition to each phase file's question bank.

**Frame**
- "If preparation took half the hours, what would happen to your fees, your season staffing and your offshore spend?"
  (Of 219 US firms on one billing platform, 3% bill tax preparation hourly and 37% use a fixed fee [IGNITION-2025].)
- "Who keeps an AI saving: you, the client, or both? Has anyone read your engagement letters against OPR's fee
  language?" (OPR says billing manual time not spent may breach section 10.27; the AICPA disputes it [IRS-OPR-2026; AICPA-FEES-2026].)
- "Which of your services would AI threaten, change a lot, or mainly help?" ([disruption.md](disruption.md) §8)
- "Where is the tax authority ahead of you on data and analytics?" (Deloitte's scenarios cross a company's AI adoption
  with its authority's [DELOITTE-TTT-2026].)
- "Has anyone approached you about buying the practice, and what would they do to the production work?" ([economics.md](economics.md) §6)

**Map**
- "Walk me through one return, provision or filing from data in to signature. Where do the hours go, by grade?"
- "How does data reach you: client uploads, ERP extracts, scanned documents, portals? How do you know it is complete?"
- "How many returns, entities, jurisdictions, local files or notices a year? What share is roll-forward?"
- "Which steps are offshore or outsourced today?" (68% of IPA 100 firms offshore tax returns [IPA-OFFSHORE-2026].)
- "Where does review queue up: senior, manager, partner, national office?"

**Diagnose**
- "Which steps produce the most review notes, notices or penalties?"
- "Where does work wait on clients, IT or another team?"
- "Which steps need judgement, and which are mechanical checks against a document or a rule?" (Use the work-type
  table in [value-chain.md](value-chain.md) §4.)
- "How clean is the data feeding your engines?" (51% of tax and finance functions are early in data maturity, per EY
  [EY-TFO-2025].)

**Reimagine**
- "If every return arrived as an agent-prepared draft with cited source documents, what would your reviewers do?"
- "If your tax engine could be called by the company's own agents, what would you have to control?"
- "If the authority saw every invoice in real time, which of your checks would move upstream?"
- "If you started the practice or department today, what would you charge, and whom would you hire?" (lens 4;
  [disruption.md](disruption.md))

**Prioritize**
- "Which options would your risk partner, insurer or auditor block, and why?"
- "Which need data you do not get today, or a consent you have not collected?"
- Raise the risk weight for anything signed or filed, as the Frame method allows.

**Make the case**
- "What is the baseline, measured on real work: hours per return, review notes, notices, amended returns?"
- "Is the comparison onshore cost, offshore cost, or both?" (An AI case that ignores the offshore baseline overstates
  savings; see [economics.md](economics.md) §5.)
- "What will the tool cost per seat, per return or per run?" (Blue J lists its individual plan at US$1,498 a year per user
  [BLUEJ-PRICING-2026]; one firm reported a vendor's average of US$100-150 per return and expected to pay more [WCG-2026]; TEI attendees flagged rising token costs [TEI-TAXTECH-2026].)
- "Where will juniors learn the judgement this step used to teach?" ([workforce.md](workforce.md) §6)

**Plan**
- "Who owns the tool, its vendor review and its monitoring, and who owns the workflow's results?"
- "Which clients or entities go first, and when do you review the parallel run against last year's returns?"
- "Which filing deadlines and rule dates fall inside the plan?" ([frontier.md](frontier.md) §6)

## 6. In-house and mid-market variants

**In-house departments**
- "How did budget and headcount move in the last two years, and who approves technology spend: tax, finance or IT?"
  (About 39% of 170 US departments reported a budget increase [TR-CORPTECHRPT-2026].)
- "What do you spend on outside advisers each year, and which of that work could come in house?"
- "Which automations does the team run, who built them, and who could maintain them?" (TEI attendees described
  workflows nobody could explain after the builder left [TEI-TAXTECH-2026].)
- "How will your auditors review an AI-assisted provision?" (No source found covers auditing AI-prepared tax balances;
  see [provision-pillar-two](modules/provision-pillar-two.md).)
- "Do you expect headcount to change?" (58% of KPMG Germany's respondents expect stable domestic tax headcount [KPMG-DE-2026].)

**Mid-market firms and owner-managed clients** (more probes in each module's §4 or §10)
- "Which owner clients have an S corporation salary backed by a dated, duty-based study, and has any owner brought you a
  chatbot's number?" ([compliance-individual-business](modules/compliance-individual-business.md) `#26`)
- "When an AI-prepared entity return reaches your reviewer, what do they re-check, how long does it take, and do you
  track overrides and errors found?" (In one sponsored recap a firm leader said preparers re-checked everything AI
  produced [OLIVER-BOSUMMIT-2026].)
- "When was the last nexus review that covered income and franchise tax, not only sales tax, and what data fed it?"
  ([multistate-private](modules/multistate-private.md) `#04`)
- "If a state notice arrived tomorrow citing third-party data, how long would it take to assemble your apportionment
  support, and from which systems?" (Few state agencies say they use AI: 7 of 36 responding [TAXNOTES-UNWATCHED-2026].)
- "If you or an adviser used AI on a nexus, apportionment or PTET conclusion, who verified thresholds, rates and
  effective dates state by state, and where is that recorded?" ([multistate-private](modules/multistate-private.md) `#07`, `#14`)
- "What would show that AI shortens a nexus study or reduces rework, and do you collect it today?" (No firm has
  published such a figure; see the multistate module's opening note.)

## 7. Sensitive topics

- **Client and taxpayer data.** Never ask for names, SSNs, figures or returns. Ask for volumes, ranges and roles.
- **Unapproved tools.** Normalise first (§2), after some rapport.
- **Fees and the OPR alert.** Ask what the policy is, not what a given client was billed.
- **Ownership and buyers.** Ask whether an approach has been made, not for terms.
- **Jobs and seasonal staff.** If a leader worries about the team, use
  [people-and-change.md](../../method/people-and-change.md) and [workforce.md](workforce.md); do not promise outcomes.

## 8. Vocabulary to mirror

| Term | Meaning | Note |
|---|---|---|
| Circular 230; OPR | Treasury rules for practice before the IRS; the office that enforces them | Alert 2026-19 applies them to AI |
| Section 7216 consent | Written taxpayer consent to use or disclose return information | Unsettled for AI vendors |
| PTIN; EA; signing preparer | Preparer ID; enrolled agent; the individual with primary responsibility for the return | Who stays accountable |
| Organizer; source documents | The client questionnaire; W-2s, 1099s, K-1s, brokerage statements | Where intake and extraction sit |
| Form 8879; Form 8867 | E-file authorisation; paid-preparer due diligence checklist | Steps that stay personal |
| CP2000; IDR | IRS mismatch notice; information document request in an exam | Controversy |
| ASC 740, IAS 12; ETR; UTP; valuation allowance | Provision standards; effective tax rate; uncertain tax positions; judgement on deferred tax assets | Provision |
| ASU 2023-09 | US disclosure rules for the rate reconciliation and taxes paid | New data workload |
| GloBE; GIR; QDMTT; safe harbour | Pillar Two rules; GloBE Information Return; domestic top-up tax; simplified tests | Pillar Two |
| Local file, master file, CbCR; DEMPE; APA, MAP | TP documentation; functions around intangibles; certainty procedures | Transfer pricing |
| Nexus; exemption certificate; CTC; ViDA | Duty to collect; buyer's exemption proof; continuous transaction controls; EU VAT in the Digital Age | Indirect tax |
| SSTS; PCRT; TPB | AICPA tax standards; UK conduct rules; Australia's practitioner regulator | Professional duties |
| Extension season; roll-forward | The second deadline peak; reusing last year's work | Timing and baseline |
| Reasonable compensation; basis, Form 7203; AAA | An S corporation owner's salary; shareholder basis limits; the accumulated adjustments account | Owner-managed clients |
| Apportionment; PTET; composite return; voluntary disclosure | Splitting income among states; pass-through entity tax election; one return for many nonresident owners; coming forward for limited lookback | Multistate private companies |

**Words to avoid:** "AI files the return", "automated tax advice", "replace preparers", "AI-signed". Say instead
"agent-drafted return for review", "first pass", "the signing preparer", "review record", "human control point".

## 9. Sources

Keys not listed here are in [sources.md](sources.md).

- **OLIVER-BOSUMMIT-2026**: Blake Oliver (post sponsored by Black Ore), *40 Hours of Work Done in 5 Minutes: My Takeaways from Black Ore's AI Tax Summit* (press, 4 Jun 2026). https://www.blakeoliver.com/blog/black-ore-ai-tax-summit
- **TAXNOTES-UNWATCHED-2026**: TaxProf Blog, *Tax Notes Investigates States' Use of AI in Audit Selection (excerpting Tax Notes, 14 Apr 2026)* (press, 2 May 2026). https://taxprofblog.aals.org/?p=134442

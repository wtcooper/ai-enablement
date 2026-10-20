# Agentic patterns: `intake-triage` and `service-agent-escalation`

Research run for the shared backbone library of the transformation advisor. Written 2026-10-20.

Conventions used in this file:

- Every sourced claim carries a ref in square brackets and a locator. Refs are defined in section 7.
- "Advisor judgment" marks a design heuristic that is not taken from a source. Treat it as a hypothesis to test with the user, not as evidence.
- Provenance of figures: `self-reported` (the organization that deployed it), `vendor-published`, `independent` (academic or third-party measure).
- Grades follow `vocabulary.md`. Grade A needs a figure the named organization reports as measured. Vendor case studies with qualified ("up to", "potentially") figures are B.
- Mapping of ladder rungs to runtime classes follows the library index section 4 (assist = `personal-assistant`; augment and automate = `workflow-automation` or `shared-team-skills`; trigger-driven unattended work = `background-agent`; delegate = `managed-agent-runtime`).
- "ATRS" records are the UK government's Algorithmic Transparency Recording Standard records on GOV.UK, written by the deploying department. They were read through the GOV.UK content API.

---

## 1. Summary

- **The two patterns are one family with a different front end.** `intake-triage` sorts what arrives (letters, emails, calls, tickets, orders) and hands it to the right team, template or queue. `service-agent-escalation` answers the sender directly and hands off to a person when it cannot. Both rest on the same three things: a classifier with a known error rate, a rule for what goes to a person, and a log that lets someone check the rule.
- **Published quality numbers are modest and rarely include the number that matters.** UK departments disclose accuracy for triage tools: FCDO correspondence classification accuracy 0.7333 and an AI-prompt classifier at about 0.6 after an earlier model scored about 0.34 [ATRS-FCDO-CORR-2025, 4.2.7]; FCDO consular enquiry matching correct for 76% to 81% of historic enquiries by batch [ATRS-FCDO-CONSULAR-2024, 4.2.7]; HMRC's digital assistant 83.03% on known intents [ATRS-HMRC-2025, 4.2.7]. None of these publishes an override rate, a miss rate on urgent items, or the share of escalations that were warranted.
- **The strongest independent evidence cuts against the easy story.** A randomized field experiment on Alibaba's Taobao found an agentic service system cut chat duration 16.8% in AI-eligible chats, did not change repeat contact significantly, and lowered customer ratings by 0.412 points on a five-point scale for those chats [ARXIV-WANG-2026, section 5.1]. A randomized trial of an ML alert in Copenhagen emergency calls found no significant gain in dispatcher recognition of cardiac arrest (93.1% with alerts vs 90.5% without, P = .15) even though the model alone was more sensitive [JAMANO-BLOMBERG-2021, Results].
- **Handoff design is the product.** In the Taobao experiment, 44.1% of AI-eligible supervised chats were technical escalations, 8.6% emotional escalations and 12.3% human-initiated; human takeover kept quality in technical escalations but worked less well in emotional ones, and early intervention mattered [ARXIV-WANG-2026, sections 5.2 and abstract]. Customers' top stated worry about AI in service is difficulty reaching a person (Gartner survey of 5,728 customers) [GARTNER-CSAT-2024]. The CFPB describes "doom loops" with no off-ramp to a human [CFPB-CHATBOTS-2023].
- **The cheapest safe designs keep the model away from the answer.** FCDO's consular tool has the model return only template and topic identifiers, so the worst case is an irrelevant but valid template or none [ATRS-FCDO-CONSULAR-2024, 5.2]. Air Canada was held liable for a chatbot's wrong fare advice [GUARDIAN-AIRCANADA-2024], and a support bot at a software company invented a policy [ARS-CURSOR-2025]. Constraining output to approved content and identifiers is the strongest control seen.
- **Volume and containment are not value.** Klarna reported two-thirds of chats handled and a 25% drop in repeat inquiries in the first month [KLARNA-AIASSISTANT-2024], then in May 2025 its CEO said it was hiring human agents again after finding AI-handled service of "lower quality" [ENTREPRENEUR-KLARNA-2025]. NS&I reports about 22.23% of calls contained, all of them simple queries [ATRS-NSI-2025, 4.2.7]. Advise users to count resolution and repeat contact, not conversations.
- **Regulation bites on specific uses, not on the pattern.** EU AI Act Annex III lists emergency call classification and dispatch priority, emergency patient triage, public-benefit eligibility and CV filtering as high-risk uses; customer-facing chat triggers the disclosure duty in Article 50 [EUAIA-2024, Annex III points 4(a), 5(a), 5(d); Art. 50(1)]. GDPR Article 22 gives a right to human intervention for solely automated decisions with significant effects [EC-GDPR-2016, Art. 22].
- **Inbound content is untrusted input.** Both patterns read text written by outsiders. Prompt injection and data exfiltration risk rises when an agent combines private data, untrusted content and a way to communicate out [WILLISON-TRIFECTA-2025; OWASP-LLM01-2025].

---

## 2. Item profiles

### 2.1 `intake-triage`

**What it does and where it fits.** Reads incoming items, classifies them, extracts key fields, flags priority or risk, and routes them to a team, queue or pre-approved template; some tools also create the case record. Fits `transaction-processing` and `coordination-scheduling` work, and any front door where one shared inbox, phone line or form feeds several teams.
- Scale examples: DWP's scanner reads about 25,000 scanned letters a day [ATRS-DWP-WHITEMAIL-2025, section 1 description; PUBTECH-WHITEMAIL-2025]; the ICO created on average 6,340 cases a month in ICE 360 [ATRS-ICO-2026, 3.3]; FCDO consular services receive about 100,000 written enquiries a year [ATRS-FCDO-CONSULAR-2024, Description].
- Cues in a user's description of their work (advisor judgment): "someone sorts the inbox every morning"; "it takes a day before the right person sees it"; "urgent ones get buried"; "people pick the wrong category on the form"; "we re-key emails into the case system"; "first-line triage"; a shared mailbox feeding several specialist teams. A sourced version of the last cue: UiPath's analysis found the probability that Product, Deployment Type and Issue Type were all correctly filled at ticket creation was below 50% [UIPATH-CCA-2026, "The problem"].

**Ladder range and runtime class by rung.**
- `assist` (`personal-assistant`): a person pastes an item into a chat assistant for a summary or draft category. No source needed; shows the idea before building anything.
- `augment` (`workflow-automation`, or `shared-team-skills` when consistency across a team is the aim): the tool proposes team, summary, flags; a named person confirms or overwrites. HMT officers can overwrite predicted fields [ATRS-HMT-2024, 3.4]; ICO case officers must review each automated case and give feedback [ATRS-ICO-2026, 3.4]; DWP caseworkers decide on the vulnerability shortlist [ATRS-DWP-WHITEMAIL-2025, 3.2].
- `automate` (`workflow-automation` or `background-agent`, because the tool acts on arrival with no person present): no person on the normal path; failures go to a person. ICO expects automation to handle "upwards of 90%" of case creation, with failed validation sent to a manual queue [ATRS-ICO-2026, 3.3, 3.4]. FCDO's consular tool signposts users before they submit an enquiry [ATRS-FCDO-CONSULAR-2024, Description]. DWP's telephony platform routes callers by what they say, with the option of a human [ATRS-DWPCONV-2025, 2.1, 3.4].
- `delegate` (`managed-agent-runtime`): the agent triages and then acts across systems (investigate and close). The archetype security use cases cover this; no non-security delegate example was found for this pattern (see Gaps).

**How it is built.**
- *Inputs and preprocessing.* Raw items are made machine-readable and redacted before the model sees them: DWP scans letters, converts text, and redacts personal data automatically [PUBTECH-WHITEMAIL-2025]. HMT takes `.msg` or `.eml` files [ATRS-HMT-2024, 4.2.4].
- *The AI's role.* Often a mix of models, not one. HMT uses a support vector machine for team classification, GPT-4 prompting for summary and flags, and retrieval-augmented generation to match standard lines [ATRS-HMT-2024, 2.1]. The AI proposes; it does not write the reply (HMT: "does not write the entire response") [ATRS-HMT-2024, Description]. FCDO's correspondence tool also logs cases through robotic process automation but "will not carry out any full end to end processes" and humans peer review before any response [ATRS-FCDO-CORR-2025, 5.2].
- *Structure and validation.* ICO validates LLM-parsed data against a data contract per case type and creates the case only if the criteria are met; organisation names are matched to the existing database by Levenshtein distance, and unmatched cases are flagged [ATRS-ICO-2026, 2.1, 5.2].
- *Thresholds.* DWP's team used test documents to "calibrate label synonyms and confidence thresholds" and reviewed outputs manually every day in a controlled production phase to refine thresholds [ATRS-DWP-WHITEMAIL-2025, 4.2.7]. UiPath invokes the LLM only when retrieval confidence is below a threshold and constrains answers to a predefined map of valid Product x Deployment x Issue combinations [UIPATH-CCA-2026, Phase 5].
- *Sampling and checkpoints.* Published designs use full human review at the start and spot checks later: FCDO reviews all cases where a user goes on to submit a written enquiry, plus "spot checks and regular testing" [ATRS-FCDO-CONSULAR-2024, 3.4]. Acceptance sampling is "the middle of the road" between no inspection and 100% inspection, and its purpose is to decide whether a lot is acceptable, not to estimate its quality [NIST-HANDBOOK-2026, section 6.2.1]. Advisor judgment: begin at 100% review; thin review by category and confidence band only after the error rate in that stratum is measured; always review the highest-severity categories and keep a permanent random audit sample so drift shows.
- *Logging and audit trail.* DWP gives each scanned document a unique ID that traces to the customer record in separate systems and keeps the original scanned image one click from the shortlist [ATRS-DWP-WHITEMAIL-2025, 3.1 and 2.1]. HMT's accuracy is "captured in an automatically updating report" watched by a project team [ATRS-HMT-2024, 3.4]. Advisor judgment: log item reference, model and prompt version, predicted fields and confidence, the person's override, and the final outcome, so override rate can be computed.

**Prerequisites.**
- *Data.* A labelled history of past items and where they went. HMT trained on 1,085,710 historic documents with an 80/20 test split [ATRS-HMT-2024, 4.3.4]; FCDO used batches of historic anonymised enquiries compared with staff choices [ATRS-FCDO-CONSULAR-2024, 4.2.7]; DWP captured 80,000 caller utterances over one week across benefit lines [ATRS-DWPCONV-2025, 4.3.4, 4.3.6]. Where history is thin, DWP's scanner used synthetic documents: at least 15 per theme plus two redacted production letters in testing [ATRS-DWP-WHITEMAIL-2025, 4.2.7].
- *Access.* API access to the case system (HMT updates the system through an eCase API call [ATRS-HMT-2024, 4.1.1]); a scanning or mailbox feed.
- *Policy.* Data protection impact assessment and equality analysis (DWP lists DPIA, Equality Analysis and external assessment [ATRS-DWP-WHITEMAIL-2025, 5.1]); a decision on whether data may leave the estate.
- *Skills.* A named owner of the taxonomy and standard lines. At FCDO only a limited number of staff can add or remove templates and they are trained to do so [ATRS-FCDO-CONSULAR-2024, 3.5]. HMT team members go through onboarding on use and troubleshooting [ATRS-HMT-2024, 3.5].

**Failure modes and the controls that catch them.**
| Failure | Source and control |
|---|---|
| Misrouted item because categories overlap | HMT: overlap among groups can misdirect emails; the hub coordinator recognizes out-of-scope subjects and redirects [ATRS-HMT-2024, 5.2] |
| Wrong data written into the case record | FCDO: RPA may save incorrect email or names; ongoing optimisation and peer review before any response [ATRS-FCDO-CORR-2025, 5.2]. ICO: mismatched organisations; flag for review, tighten matching parameter if seen [ATRS-ICO-2026, 5.2] |
| Hallucinated routing target or text | FCDO consular: "air gap" so the model returns identifiers only; worst case is an irrelevant but valid template, or none shown [ATRS-FCDO-CONSULAR-2024, 5.2] |
| Model refuses or returns nothing on sensitive text | FCDO: content-filtered inputs are classed "offensive" and sent to manual review [ATRS-FCDO-CORR-2025, 5.2] |
| Error rate too high to use | FCDO measured an older prompt classifier at about 0.34 accuracy and a newer one at about 0.6 [ATRS-FCDO-CORR-2025, 4.2.7]; UiPath tried five designs and dropped the document index because it "underperformed significantly" [UIPATH-CCA-2026, Phases 1-2] |
| Alert or queue floods reviewers | In a hospital deployment, the Epic Sepsis Model alerted for 18% of hospitalized patients and still missed 67% of sepsis cases in the external validation [JAMAIM-WONG-2021, Results] (adjacent: alert scoring, not inbox triage) |
| Reviewers defer to the tool | NIST describes automation bias as excessive deference to automated systems [NIST-AI600-1-2024, 2.7]; in user studies, AI explanations increased the chance people accepted the AI's recommendation whether or not it was correct [ARXIV-BANSAL-2021, Abstract] |
| Scores that look more certain than they are | Modern neural networks were found poorly calibrated, so a raw confidence score is a weak threshold until checked [ARXIV-GUO-2017, Abstract] |
| Hostile or injected content in the item | Treat inbound text as untrusted; restrict privileges; require human approval for high-risk actions [OWASP-LLM01-2025, Mitigation]; avoid combining private data, untrusted content and external communication in one agent [WILLISON-TRIFECTA-2025] |

**Value levers and metrics.** Levers from the library: `capacity`, `speed`, `quality`, `risk`, `experience`.
- Organization-stated benefits (not measured outcomes): FCDO says its tool saves "several hours of manual work per day for multiple team members" [ATRS-FCDO-CORR-2025, 2.2]; DWP lists "reduced time in manually sorting out mail" [PUBTECH-WHITEMAIL-2025].
- Measured: DWP's telephony platform reports right-first-time routing up 21% and deflection up 9% (denominators and baselines not stated) [ATRS-DWPCONV-2025, 4.2.7].
- Quality metrics seen in sources: accuracy, macro F1, precision and recall per field [ATRS-FCDO-CORR-2025, 4.2.7]; share correct against staff on historic batches [ATRS-FCDO-CONSULAR-2024, 4.2.7]; "the recategorization rate", that is how often agents change the assigned category (suggested as a production accuracy measure in a vendor guide; not read, search-only note in Gaps).
- Metrics an advisor should add (advisor judgment): override rate by category; recall on the urgent or high-risk class; share sent to the manual queue; time to the right team; repeat misroutes per item.

**Governance points.**
- EU AI Act Annex III lists as high-risk: AI used to "evaluate and classify emergency calls" or set dispatch priority, and emergency healthcare patient triage (5(d)); public-authority eligibility for benefits (5(a)); creditworthiness (5(b)); life and health insurance risk and pricing (5(c)); analysing and filtering job applications (4(a)) [EUAIA-2024, Annex III]. Article 14 requires oversight designed to prevent or minimise risks and makes the overseer able to stay aware of automation bias and to decide not to use the system [EUAIA-2024, Art. 14]. Article 26 requires deployers to assign oversight to people with competence, training and authority and to keep logs at least six months unless other law says otherwise [EUAIA-2024, Art. 26(2), 26(6)]. The mirror page shows application from 2 December 2027 for Annex III high-risk systems [EUAIA-2024, Art. 14 and Art. 26 pages]; check the Official Journal text before quoting dates.
- GDPR Article 22: a person has the right not to be subject to a decision based solely on automated processing with legal or similarly significant effects, and where an exception applies, at least the right to human intervention [EC-GDPR-2016, Art. 22(1), 22(3)]. Triage that only orders a queue differs from triage that denies a service; ask which it is.
- NIST AI RMF 1.0: MAP 3.5 (human oversight processes defined and documented), MEASURE 2.1 (test sets and metrics documented), MANAGE 4.1 (post-deployment monitoring plans with user input and appeal) [NIST-AI100-1-2023, PDF pp. 32, 34, 38].
- ISO/IEC 42001: an organization-level AI management system standard that can be certified; it sets how the organization manages AI, not triage thresholds [BSI-ISO42001-2026]. The ISO page itself was blocked; only BSI's description was read.
- UK public sector: departments publish ATRS records; DWP's states human review of each vulnerability flag and that "a caseworker will always decide if extra support is needed" [PUBTECH-WHITEMAIL-2025].
- Sector note: the DWP tool reads post that can include health and bank details; DWP states personal data is redacted before the AI step [PUBTECH-WHITEMAIL-2025].

**How it evolves up the ladder.**
- Assist to augment: from one person's chat to a standard prompt or workflow inside the case system with a required confirm step (ICO, HMT).
- Augment to automate: the manual queue shrinks to failures and low-confidence items (ICO's stated expectation of 90%+ [ATRS-ICO-2026, 3.3]). FCDO's consular tool moves the step to before the enquiry exists [ATRS-FCDO-CONSULAR-2024, Description].
- Automate to delegate: the agent takes the next step (investigate, close, act). The archetype security cases describe this with deterministic checks first and evidence-gated dismissal (see ids in section 3).
- Advisor judgment: move up only per category, only after the override rate and the miss rate on the urgent class are measured for that category.

**Anti-patterns (where it should not be used).**
- Where routing can be decided from declared attributes by rules. The Home Office's visitor-visa complexity router "uses algorithms in their most basic form" and "does not use machine learning" [ATRS-HO-CARSV-2024, 2.1]. Start with rules if rules are enough.
- Where the triage decision itself denies or reduces a service and no human reviews it (GDPR Art. 22; Annex III 5(a)) [EC-GDPR-2016; EUAIA-2024].
- Where the taxonomy is unstable or owned by nobody; a classifier fixes the labels it was given, including the wrong ones. Advisor judgment.
- Where the item is mostly attachments or images the pipeline cannot read; check with a sample first (HMT removed unreadable files before testing [ATRS-HMT-2024, 4.3.4]).
- Where the urgent class is rare and a miss is severe, and nobody will measure recall. Advisor judgment, supported by the sepsis and cardiac-arrest results [JAMAIM-WONG-2021; JAMANO-BLOMBERG-2021].

### 2.2 `service-agent-escalation`

**What it does and where it fits.** Answers customers, citizens or staff directly (chat, voice, messaging), gathers information, completes simple transactions where permitted, and hands off to a person when it cannot help, when the sender asks, or when a rule fires. Fits `client-interaction` work: high-volume, repeatable questions with approved answers. Examples span financial services (Klarna, NS&I, Bank of America), public sector (HMRC, DVLA, DWP, MoJ), retail e-commerce (Taobao), transportation (Lyft) and software (Cursor).
- Cues (advisor judgment): "the same twenty questions make up most of our contacts"; "wait times at peak"; "agents spend their day on password resets, order status, opening hours"; "people must reach a human when it is complicated"; "we answer in several languages". Sourced: Klarna's assistant works in more than 35 languages [KLARNA-AIASSISTANT-2024]; Lyft says riders and drivers waited 30 to 40 minutes for an agent before its change [LYFT-ANTHROPIC-2026].

**Ladder range and runtime class by rung.**
- `assist` (`personal-assistant`, `shared-team-skills`): the AI helps the human agent (suggests answers, retrieves past tickets). Adjacent to this pattern, not the pattern itself. Evidence: customer-support agents with a generative assistant resolved 14% more issues per hour on average, 34% more for novice and low-skilled workers [NBER-W31161-2023, Abstract]; a retrieval-and-knowledge-graph assistant reduced median per-issue resolution time by 28.6% after about six months at LinkedIn [ARXIV-LINKEDIN-2024, Abstract].
- `augment` (`workflow-automation`): AI drafts or pre-answers and a person approves, or the bot collects information and a person finishes. DVLA's chatbot gathers the reason for contact and data-protection check data and transfers to a web chat advisor who sees the transcript [ATRS-DVLA-CHATBOT-2025, 3.4]. HMRC's advisers also receive the transcript on transfer [ATRS-HMRC-2025, 3.4].
- `automate` (`workflow-automation`, `background-agent`): the AI resolves defined contact types with no person on the normal path; exceptions go to people. NS&I answers 100% of inbound calls with a voice assistant and reports about 22.23% contained [ATRS-NSI-2025, 4.2.7]. Klarna's assistant handled two-thirds of chats in month one [KLARNA-AIASSISTANT-2024].
- `delegate` (`managed-agent-runtime`): an agent holds a multi-step outcome with tools (refunds, rebooking) under human checkpoints. The vendor benchmark τ-bench tests this and finds low reliability (see section 5). Anthropic's guide says customer support suits agents because success can be measured by resolution and actions can be handled programmatically, with human oversight [ANTHROPIC-AGENTS-2024, Appendix 1A].

**How it is built.**
- *Inputs.* A bounded body of approved content or intents. HMRC's assistant matches user language to curated answers that link to GOV.UK guidance [ATRS-HMRC-2025, 2.1]; DVLA's uses pre-configured scripts and flows and "did not require training" [ATRS-DVLA-CHATBOT-2025, 4.2.8]; NS&I's draws on about 200 web pages and document links [ATRS-NSI-2025, 4.3.3]; GOV.UK Chat uses only GOV.UK content and instructs the model to ignore its prior training data [ATRS-GOVUKCHAT-2025, 2.1].
- *The AI's role.* Intent detection and retrieval of approved answers (HMRC, DVLA, MoJ: "classified into a predefined intent... deterministic dialogue" [ATRS-MOJ-2026, 2.1]) or free generation grounded on content (GOV.UK Chat). Intent-first designs trade flexibility for predictability.
- *Escalation rules.* Triggers named in sources: the bot does not understand or the customer asks (DVLA [ATRS-DVLA-CHATBOT-2025, 5.2]); caller chooses a human (DWP [ATRS-DWPCONV-2025, 3.4]); failure thresholds (repeated failure to understand intent) and high-risk actions such as cancelling orders, large refunds or payments (OpenAI guide [OPENAI-AGENTS-2025, "Plan for human intervention"]); algorithm-detected capability limits and customer frustration, plus human-initiated takeover (Taobao [ARXIV-WANG-2026, 5.2]).
- *Handoff quality.* Transcript passed to the adviser (HMRC, DVLA); Gartner's advice is that the bot should say it will connect the customer and then "pick up where the chatbot left off" [GARTNER-CSAT-2024]. The CFPB treats missing off-ramps as a consumer harm [CFPB-CHATBOTS-2023, "Hindering access to timely human intervention"].
- *Sampling and monitoring.* DVLA staff "undertake observations to monitor the accuracy" [ATRS-DVLA-CHATBOT-2025, 4.1.3]; HMRC developers monitor daily with dashboards and the NLU test set is re-scored (83.03% as of March 2025) [ATRS-HMRC-2025, 4.1.3, 4.2.7]; MoJ's supplier lists transcript review and live-call review after launch, and typical metrics include intent accuracy, containment, "appropriate escalation rate", handling time and satisfaction [ATRS-MOJ-2026, 4.2.7]. Advisor judgment: sample conversations by outcome (resolved, escalated, abandoned) and by intent, with extra weight on conversations that ended without escalation.
- *Logging.* Conversations are stored for review and to improve answers (HMRC [ATRS-HMRC-2025, 4.3.8]). Advisor judgment: log the answer, the source content it used, the escalation trigger, the person who took over, and the end outcome.

**Prerequisites.**
- *Data.* Real contact logs to find the top intents (HMRC trained on 28,575 unique samples from live user input [ATRS-HMRC-2025, 4.3.4, 4.3.6]; DWP on 80,000 utterances [ATRS-DWPCONV-2025, 4.3.4]); current, approved content with an owner [ATRS-FCDO-CONSULAR-2024, 3.5].
- *Access.* Read access to the knowledge base; where the bot acts, scoped tool permissions. Customer identity checks stay with the human adviser in the DVLA design [ATRS-DVLA-CHATBOT-2025, 3.4].
- *Policy.* Disclosure that the customer is talking to AI (EU AI Act Art. 50(1) unless obvious [EUAIA-2024, Art. 50(1)]); a rule on who is liable for the bot's statements (Air Canada [GUARDIAN-AIRCANADA-2024]); jailbreak testing (GOV.UK Chat assessments with the AI Security Institute and an IT health check; both noted that guaranteeing no successful jailbreak is not possible [ATRS-GOVUKCHAT-2025, 5.2]).
- *Skills.* A conversation designer or content owner, an operations team that reviews transcripts, and a person who can change escalation rules. Advisor judgment.

**Failure modes and the controls that catch them.**
| Failure | Source and control |
|---|---|
| Confident wrong answer with legal or financial effect | Air Canada's chatbot gave wrong bereavement-fare guidance; the tribunal held the airline liable and ordered C$650 [GUARDIAN-AIRCANADA-2024]; the tribunal said the airline did not take reasonable care to ensure its chatbot was accurate [MCCARTHY-MOFFATT-2024]. NYC's MyCity bot gave incorrect or incomplete guidance on housing, worker rights and business rules in The Markup's testing [MARKUP-MYCITY-2024]. Control: answer only from approved content; do not let the bot state policy it cannot cite |
| Invented policy | Cursor's support agent told users a non-existent policy applied; the co-founder later apologised and said the underlying cause was a backend change [ARS-CURSOR-2025]. Control: label bot answers; route policy and billing questions to people |
| Brand or safety failure after an update | DPD disabled the AI element of its chat after a system update led it to swear and criticise the company [BBC-DPD-2024]. Control: regression tests after each change (MoJ supplier lists regression testing after each change [ATRS-MOJ-2026, 4.2.7]) and a kill switch |
| No exit to a person | CFPB "doom loops" [CFPB-CHATBOTS-2023]; Gartner's top customer concern [GARTNER-CSAT-2024]. Control: always-available human option (Klarna: "there will always be a human if you want", as told to Bloomberg [ENTREPRENEUR-KLARNA-2025]) and a failure-count trigger [OPENAI-AGENTS-2025] |
| Escalation arrives too late or the human disengages | Taobao: human intervention was less effective in emotional escalations, workers sent fewer messages and showed less proactivity there, and early intervention sustained effort [ARXIV-WANG-2026, abstract, 5.2]. Control: trigger on frustration signals, not only capability limits; hand over early |
| Rule-following drops with repetition | τ-bench: pass^8 below 25% in retail for a state-of-the-art model, meaning the chance all eight repeated trials succeed [ARXIV-TAUBENCH-2024, Abstract]. Control: test with repeated trials, not one pass |
| Data leakage | CRMArena-Pro found "near-zero" inherent confidentiality awareness in tested agents; prompting improved it at a cost to task performance [ARXIV-CRMARENAPRO-2025, Abstract]. Control: scope data access; do not rely on the model to withhold |
| Injection through customer text | OWASP LLM01; the lethal trifecta [OWASP-LLM01-2025; WILLISON-TRIFECTA-2025]. Control: least privilege, human approval for high-risk actions |
| Customers reject AI service | 64% of 5,728 surveyed customers (December 2023) said they would prefer companies not use AI in service; 53% would consider switching [GARTNER-CSAT-2024] (vendor/analyst survey; question wording not read beyond the release) |

**Value levers and metrics.** Levers: `cost`, `capacity`, `speed`, `experience`, `quality`.
- Reported: Klarna, first month, 2.3 million conversations (two-thirds of chats), resolution in under 2 minutes versus 11, 25% drop in repeat inquiries, customer satisfaction "on par" with human agents, and an estimated $40 million profit improvement in 2024 [KLARNA-AIASSISTANT-2024]. Bank of America says Erica for Employees reduced calls into the IT service desk by 50% and is used by over 90% of employees [BOFA-ERICA-2025]. NS&I: about 22.23% contained [ATRS-NSI-2025, 4.2.7]. DWP: 9% increase in deflection, 21% increase in right-first-time routing [ATRS-DWPCONV-2025, 4.2.7].
- Quality metrics to demand: resolution (not containment), repeat contact within a fixed window (Taobao uses re-contact on the same issue within seven days [ARXIV-WANG-2026, 3.x data section]), customer rating of AI-handled versus human-handled contacts, share of escalations that were warranted and share of unescalated contacts that should have been (advisor judgment), intent accuracy [ATRS-HMRC-2025, 4.2.7], appropriate escalation rate [ATRS-MOJ-2026, 4.2.7].
- Caution: hours or contacts removed are not value until the capacity has a destination (library index section 5).

**Governance points.**
- EU AI Act Art. 50(1): systems designed to interact directly with people must inform them they are interacting with AI unless obvious to a reasonably well-informed person; the mirror page gives 2 August 2026 [EUAIA-2024, Art. 50]. Annex III 5(d) high-risk applies if the front door classifies emergency calls or sets dispatch priority [EUAIA-2024, Annex III 5(d)].
- GDPR Art. 22 if the agent decides something with legal or similarly significant effect [EC-GDPR-2016].
- NIST AI 600-1 (generative AI profile) names confabulation (2.2), information security (2.9) and human-AI configuration (2.7) as risks to manage [NIST-AI600-1-2024, section list, PDF pp. 7-13].
- Financial services: the CFPB's 2023 report found that all of the top 10 commercial banks use chatbots of varying complexity, and reported complaints about being stuck in loops [CFPB-CHATBOTS-2023, footnote 12 text and "Limited ability to solve complex problems"]. Local rules on chat disclosure and bar guidance on chatbot communications exist (see `professional-services-acceptance-risk-14` for Oregon Formal Opinion 2026-208); not re-researched here.
- ISO/IEC 42001 as organization-level management system [BSI-ISO42001-2026].
- Contract and liability: Air Canada could not treat the bot as a separate entity [GUARDIAN-AIRCANADA-2024].

**How it evolves up the ladder.**
- Assist: the human agent uses AI suggestions (NBER, LinkedIn evidence).
- Augment: the bot gathers facts and drafts; humans finish (DVLA, HMRC transfers).
- Automate: defined intents resolved end to end; humans take exceptions (NS&I, Klarna, Taobao).
- Delegate: tools to act (refunds, bookings) with checkpoints on high-risk actions [OPENAI-AGENTS-2025]; reliability evidence is weakest here (τ-bench, CRMArena-Pro).
- Advisor judgment: expand by intent, not by channel. Add a new intent only when its resolution, repeat-contact and rating figures match the human baseline.

**Anti-patterns.**
- Using the bot to hold customers away from people. Klarna's own CEO linked cost focus to "lower quality" and a return to hiring humans [ENTREPRENEUR-KLARNA-2025]; Gartner and CFPB describe the harm [GARTNER-CSAT-2024; CFPB-CHATBOTS-2023].
- Answering questions whose wrong answer carries legal or financial liability without approved, citable content [GUARDIAN-AIRCANADA-2024; MARKUP-MYCITY-2024].
- Granting write or refund tools before reliability is shown with repeated trials [ARXIV-TAUBENCH-2024].
- Measuring success by conversations handled or containment alone [KLARNA-AIASSISTANT-2024; ATRS-NSI-2025].
- Emotionally charged or vulnerable-person contacts with no early human path (Taobao emotional escalations) [ARXIV-WANG-2026].
- Voice-only identity checks as the sole gate for sensitive actions (see archetype `security-identity-access-18`; not re-researched).

---

## 3. Examples

### 3.1 `intake-triage`

| # | Organization (industry) | What changed in the work | Ladder / scope | Outcome and provenance | Grade | Source |
|---|---|---|---|---|---|---|
| T1 | DWP (UK public sector, benefits) | Scanner reads scanned letters with no automatic handling rule, flags potentially vulnerable people with a rationale, and a second part labels documents into nine themes for routing; caseworkers review a shortlist with the scanned image | augment / process (an additional service beside manual casework) | Reads about 25,000 documents per day (volume). No accuracy figures published; testing used at least 15 synthetic documents per theme and two redacted production letters; daily manual review in controlled production led to threshold changes. Phase "performing in production". self-reported | B | ATRS-DWP-WHITEMAIL-2025 (4.2.7, 3.1, 3.2); PUBTECH-WHITEMAIL-2025 |
| T2 | HM Treasury (UK public sector, finance ministry) | Tool predicts team, summary, high-risk, follow-up and meeting-request flags, responding minister and standard lines for ministerial correspondence; officer can overwrite; reply still written and signed off by staff | augment / step | Trained on 1,085,710 documents (80/20 split); components "directly evaluated as performing as good or better than existing processes"; no figures published; accuracy report updates automatically. Phase "Production". self-reported | B | ATRS-HMT-2024 (2.1, 3.4, 4.2.7, 4.3.4) |
| T3 | FCDO (UK public sector, foreign affairs) | Classifies emails to the correspondence mailbox, summarises, flags, and logs cases through RPA; may suggest automated replies for repeat enquiries; does not write responses | augment / step | Auto email category classification macro F1 0.7467, accuracy 0.7333; themes classification accuracy 0.7354; AI-prompt email classification accuracy about 0.6 "after old model was found as ~0.34". Several metrics "unavailable". Test set not described. Phase public beta. self-reported | A | ATRS-FCDO-CORR-2025 (2.1, 4.2.7, 5.2) |
| T4 | FCDO consular services (UK public sector) | Before submitting a written enquiry, user's question is split by an LLM and matched to pre-approved templates and topics; model returns identifiers only; user can still submit an enquiry reviewed by a human | automate / process | Template correct for 76% to 81% of enquiries depending on batch, compared with staff choices on historic anonymised enquiries; all submitted cases reviewed; phase beta-pilot. self-reported | A | ATRS-FCDO-CONSULAR-2024 (Description, 2.1, 3.4, 4.2.7, 5.2) |
| T5 | DWP telephony (UK public sector) | Callers say why they are calling; NLU signposts to GOV.UK, helps log in, or routes to an adviser; caller can ask for a person | automate / process | 97% speech recognition success; 9% increase in deflection; right-first-time routing increased by 21%. Denominators and baselines not stated. Built from 80,000 utterances. self-reported | A | ATRS-DWPCONV-2025 (2.1, 3.4, 4.2.7, 4.3.4) |
| T6 | Copenhagen Emergency Medical Services (healthcare, Denmark) | ML model listens to emergency calls and alerts dispatchers when it identifies suspected out-of-hospital cardiac arrest | augment / step | Randomized trial, 169,049 calls examined, 5,242 flagged and randomized: dispatcher recognition 93.1% with alerts vs 90.5% without (P = .15); model alone sensitivity 85.0% vs 77.5% for dispatchers without alerts. No significant improvement. 2018-2019 data; speech recognition plus ML, not an LLM. independent | A | JAMANO-BLOMBERG-2021 (Abstract, Results) |
| T7 | Information Commissioner's Office (UK regulator) | LLM parses unstructured complaint and query emails into case data in the case system; validation failures go to a manual queue; case officers review each automated case and give feedback | automate / process | Average 6,340 cases created per month in the past year; automation "expected to handle upwards of 90%" of case creation (an expectation, not an outcome). No accuracy figure; model benchmark scores cited are the vendor's general benchmarks. Phase "Production". self-reported | B | ATRS-ICO-2026 (3.3, 3.4, 4.1.2, 4.2.7, 5.2) |
| T8 | UiPath (technology) | Case Classification Agent infers Product, Deployment Type and Issue Type from a free-text support case; five design iterations ending in retrieval plus LLM with an ontology of valid combinations and a confidence threshold | augment / step | Baseline: probability all three fields correctly populated at creation below 50%. Final design described as "robust, production-ready performance"; accuracy figures are in images not readable in text. self-reported (engineering blog) | B | UIPATH-CCA-2026 (problem; Phases 1-5) |
| T9 | Danfoss (manufacturing) | Email-based B2B orders read and processed by an AI platform from Go Autonomous on Google Cloud; staff workflow consolidated from up to five systems into one | automate / process | "Automated up to 80% of transactional decision-making and communication"; turnaround "potentially" from 42 hours to near real time for a significant volume of orders; "reduced processing time by 50%"; live in over 20 countries (executive quote). vendor-published case study with customer quotes; qualified figures | B | DANFOSS-GCLOUD-2026 (Results; quotes) |

Archetype use cases already carrying `pattern: intake-triage` (id and grade only; do not re-research):

- Assurance: assurance-acceptance-independence-01 B; -02 C; -03 C; -04 C; assurance-controls-testing-03 C; -04 A; -23 D; assurance-soc-attestation-06 B; -13 B; assurance-substantive-testing-08 B.
- Professional services: professional-services-acceptance-risk-01 C; -02 C; -03 B; -04 C; professional-services-billing-collections-06 C; professional-services-client-development-13 C; professional-services-talent-learning-14 B; professional-services-work-production-25 B.
- Security: security-ai-security-13 B; -20 C; -22 B; -24 B; security-application-security-06 B; -09 C; -14 B; -15 B; security-cloud-infrastructure-01 C; -02 B; -03 B; -05 C; security-data-privacy-06 C; -07 B; -18 D; security-governance-risk-11 C; -17 B; security-human-risk-07 B; -09 D; security-identity-access-21 A; -22 B; -23 C; security-operations-01 A; -03 B; -04 B; -05 B; -06 C; -07 B; -08 B; security-threat-intelligence-03 C; -08 C; -15 B; security-vulnerability-exposure-01 A; -06 B; -07 B; -08 B; -09 C.
- Tax: tax-compliance-corporate-23 D; tax-compliance-individual-business-01 C; -18 C; tax-controversy-01 C; -13 B; -16 B; -23 B; tax-indirect-tax-14 C; tax-research-advisory-18 D.

Coverage note: the archetype set is heavy on security alert triage and on professional-services intake (conflicts, acceptance). Cross-industry cases above are from public sector, healthcare, technology support and manufacturing.

### 3.2 `service-agent-escalation`

| # | Organization (industry) | What changed in the work | Ladder / scope | Outcome and provenance | Grade | Source |
|---|---|---|---|---|---|---|
| S1 | Klarna (fintech / payments) | AI assistant built with OpenAI handles customer service chats globally; customers can still choose a live agent | automate / process | First month: 2.3 million conversations (two-thirds of chats); resolution in under 2 minutes vs 11; 25% drop in repeat inquiries; customer satisfaction score "on par" with human agents; "equivalent work of 700 full-time agents" and "$40 million" profit improvement are estimates. self-reported press release; measurement method not given | A | KLARNA-AIASSISTANT-2024 |
| S2 | Klarna (same), 2025 | CEO told Bloomberg the firm was hiring human customer service staff again so a person is always available; said AI was cheaper but gave "lower quality" | automate to augment (humans added back) / process | Statement by the CEO; no measured figures. A 2024 tester described the bot as "basically a filter" to reach humans (quoted by Entrepreneur). Bloomberg article body not readable (paywall). self-reported statement, secondary report | B | ENTREPRENEUR-KLARNA-2025; BLOOMBERG-KLARNA-2025 (headline only) |
| S3 | Alibaba Taobao (retail e-commerce) | Agentic AI resolves "AI-eligible" chats under human supervision; monitoring algorithm escalates when it detects capability limits or customer frustration; supervisor can also take over | automate / process | Randomized field experiment, 17 days in August 2024, 647 workers, 680,676 chats. Average chat duration down 3.2% overall and 16.8% in AI-eligible chats; retrial rates not significantly changed; ratings in AI-eligible chats down 0.412 points (five-point scale). Of 11,069 AI-eligible supervised chats: 44.1% technical escalations, 8.6% emotional, 12.3% human-initiated, 35.0% resolved entirely by AI. Human takeover preserved quality in technical but not emotional escalations. independent (academic; one co-author at Alibaba) | A | ARXIV-WANG-2026 (abstract; 3.4; 5.1; 5.2) |
| S4 | NS&I (UK financial services, state-owned) | Voice assistant answers inbound calls, handles non-account-specific product questions, escalates complex or sensitive issues | automate / process | After phased rollout, 100% of inbound calls answered by the assistant; about 22.23% of calls contained (simple queries); daily reporting on response, handling time and containment. self-reported | A | ATRS-NSI-2025 (2.1, 4.2.7) |
| S5 | HMRC (UK tax authority) | Digital assistant matches natural-language questions to curated answers; some lines of business allow escalation to web chat with the transcript | automate / step | NLU accuracy test set result March 2025: 83.03% on known intents (measures intent matching, not resolution); trained on 28,575 unique samples. Phase production. self-reported | A | ATRS-HMRC-2025 (2.1, 3.4, 4.2.7, 4.3.4) |
| S6 | Bank of America (US financial services) | Virtual assistant for employees answers IT and other questions; used across the enterprise; client-facing version can schedule appointments, handing off to higher-touch channels | automate / step | Erica for Employees used by over 90% of employees and "reduced calls into the IT service desk by 50%" (baseline period not stated). Client Erica: more than 3 billion interactions since 2018 (volume, not outcome). self-reported press release | A | BOFA-ERICA-2025 |
| S7 | DVLA (UK public sector, driver and vehicle licensing) | Contact-centre chatbot uses intent detection to answer simple questions from pre-set responses and to collect details, then transfers to a web chat advisor who sees the transcript | augment / step | Around 300,000 customers use it each month. Performance statement is the supplier's general intent-accuracy figure ("90%+ on well-trained intents"), not a DVLA measurement. Phase production. self-reported | B | ATRS-DVLA-CHATBOT-2025 (2.1, 3.3, 3.4, 4.2.7, 5.2) |
| S8 | Lyft (transportation / technology) | AI support assistant built on Claude handles support questions; agents focus on complex issues | automate / process | Reports resolution time reduced by over 87% and decision-making accuracy improved by over 30%; measures and baseline definitions not given. vendor-published case study | B | LYFT-ANTHROPIC-2026 |
| S9 | Air Canada (aviation) | Website chatbot gave a customer wrong guidance on bereavement fares; airline argued the chatbot was a separate entity | automate / step (failure case) | Tribunal found the airline liable and it was ordered to pay C$650. independent (tribunal, as reported) | B | GUARDIAN-AIRCANADA-2024; MCCARTHY-MOFFATT-2024 |
| S10 | City of New York (US public sector) | MyCity AI chatbot for business owners | automate / step (failure case) | The Markup's testing found answers that were incomplete and in worst cases "dangerously inaccurate", e.g. wrongly saying landlords need not accept rental-assistance tenants; the bot did not return the same response every time. No error rate published. independent (journalism) | B | MARKUP-MYCITY-2024 |
| S11 | Cursor (software) | Support agent "Sam" told users a non-existent login policy applied | automate / step (failure case) | Co-founder apologised and refunded the user; said the cause was a backend change that unintentionally invalidated sessions. No rates. self-reported statement via press | B | ARS-CURSOR-2025 |
| S12 | DPD (logistics) | Online support chatbot's AI element updated | automate / step (failure case) | Bot swore and criticised the company after an update; AI element disabled; viral post viewed 800,000 times in 24 hours. self-reported statement via press | B | BBC-DPD-2024 |

Adjacent but not the pattern (agent assist, graded B at most for this pattern): NBER-W31161-2023 (5,179 agents; 14% issues resolved per hour; 34% for novice and low-skilled; measured by independent academics at one firm), ARXIV-LINKEDIN-2024 (median per-issue resolution time down 28.6% after about six months, self-reported in a conference paper).

Archetype use cases already carrying `pattern: service-agent-escalation` (id and grade only):

- professional-services-acceptance-risk-14 B; security-governance-risk-02 B; security-human-risk-05 C; security-identity-access-05 B; -18 B; tax-controversy-18 A; tax-research-advisory-17 D; tax-transfer-pricing-03 C.

Coverage note: only 8 archetype entries use this pattern, and none is retail, manufacturing or consumer finance. The cross-industry examples above fill part of that gap.

---

## 4. Expert moves and probes

### 4.1 `intake-triage`

1. **"Walk me through one item from arrival to the right person. Who touches it, and how often is it sent to the wrong place?"** Reveals the real baseline (UiPath found under 50% of tickets had all three routing fields right [UIPATH-CCA-2026]) and whether the pain is routing, reading or waiting.
2. **"Which items must never wait? What happens if one is missed?"** Reveals the urgent class that needs recall measured and always-reviewed handling. Cardiac arrest recognition and vulnerable-claimant flags are examples [JAMANO-BLOMBERG-2021; ATRS-DWP-WHITEMAIL-2025]. If there is no urgent class, the pattern is safer.
3. **"Who owns the category list, and when did it last change?"** Reveals taxonomy ownership. A classifier learns the labels it is given. FCDO restricts template edits to trained staff [ATRS-FCDO-CONSULAR-2024, 3.5].
4. **"Do you have two years of past items with the team that handled each?"** Reveals whether supervised training or an evaluation set exists. Without history, DWP used synthetic documents and a very small real sample [ATRS-DWP-WHITEMAIL-2025, 4.2.7]; treat that as thin evidence.
5. **"Can the answer be decided by rules from fields on the form?"** Reveals whether AI is needed at all. The Home Office's router uses rules, not machine learning [ATRS-HO-CARSV-2024, 2.1].
6. **"What will a reviewer do when the tool is wrong, and how will we know?"** Reveals whether override is easy and logged. HMT officers can overwrite fields and accuracy is reported automatically [ATRS-HMT-2024, 3.4]. Ask for the override rate by category in the pilot.
7. **"Does the triage decide anything about a person, or only the order of work?"** Reveals the legal class: queue ordering versus denial or eligibility (GDPR Art. 22; Annex III) [EC-GDPR-2016; EUAIA-2024].
8. **"Where does the AI's output go next: a person, a template, or another system?"** Reveals whether the FCDO "air gap" design is available (identifiers only) [ATRS-FCDO-CONSULAR-2024, 5.2] or whether free text flows into systems.
9. **"What is in the inbound items that someone outside could control?"** Reveals injection exposure; items from the public are untrusted input [OWASP-LLM01-2025; WILLISON-TRIFECTA-2025].
10. **"If we routed everything correctly, where would the saved time go?"** Reveals the capacity destination required by the business case (library index section 5). FCDO states "several hours of manual work per day" is saved [ATRS-FCDO-CORR-2025, 2.2]; ask whom it is given to.

### 4.2 `service-agent-escalation`

1. **"What are your top 20 contact reasons by volume, and which can be answered from an approved page?"** Reveals the bounded content that makes automation safe (HMRC, NS&I and DVLA bots answer from curated content [ATRS-HMRC-2025; ATRS-NSI-2025; ATRS-DVLA-CHATBOT-2025]).
2. **"Which questions would be costly if answered wrongly?"** Reveals liability exposure (Air Canada, MyCity) and the set to route to people [GUARDIAN-AIRCANADA-2024; MARKUP-MYCITY-2024].
3. **"How does a customer reach a human today, and what do you promise?"** Reveals the off-ramp. Klarna's CEO said customers should always be able to reach a human [ENTREPRENEUR-KLARNA-2025]; customers rank difficulty reaching a person first among concerns [GARTNER-CSAT-2024].
4. **"What triggers a handoff: failure count, request, risk, mood?"** Reveals whether the design has capability and emotion triggers (Taobao) [ARXIV-WANG-2026] and failure-threshold and high-risk-action triggers [OPENAI-AGENTS-2025].
5. **"What does the human see when they take over?"** Reveals handoff quality: transcript, gathered facts, identity status (DVLA, HMRC) [ATRS-DVLA-CHATBOT-2025; ATRS-HMRC-2025].
6. **"How do you define a resolved contact, and how long until you count a repeat?"** Reveals whether the metric is resolution, not containment. Taobao used re-contact within seven days [ARXIV-WANG-2026]; Klarna reported a drop in repeat inquiries [KLARNA-AIASSISTANT-2024].
7. **"Show me ratings for AI-handled versus human-handled contacts."** Reveals the quality gap that speed figures hide: Taobao ratings fell 0.412 points in AI-eligible chats while duration fell [ARXIV-WANG-2026, 5.1].
8. **"Which actions can the agent take, and which need approval?"** Reveals tool risk. OpenAI's guide rates tools low, medium or high by write access, reversibility and financial impact [OPENAI-AGENTS-2025, Guardrails, Tool safeguards]; start read-only.
9. **"Who reads transcripts each week, and what do they change?"** Reveals whether monitoring exists. MoJ's supplier describes transcript and live-call review after launch [ATRS-MOJ-2026, 4.2.7].
10. **"What will you do with the agents' freed time, and what did your customers say when told it was AI?"** Reveals the capacity destination and customer acceptance; 64% of surveyed customers said they would prefer no AI in service [GARTNER-CSAT-2024].

---

## 5. Evidence on what works and what fails

**Controlled and independent studies**
- *Taobao randomized field experiment* (agentic service with supervision) [ARXIV-WANG-2026]. Population: 647 workers, 680,676 chats, 15-31 August 2024. Measured by academics with an Alibaba co-author on Alibaba data (working paper, May 2026, not stated as peer reviewed). Results: duration down, repeat contact not significantly changed, ratings down for AI-eligible chats, quality depends on escalation type and timing. Strongest evidence on handoff design.
- *Copenhagen RCT* (call triage) [JAMANO-BLOMBERG-2021]. A model with higher sensitivity alone did not improve the human-plus-model result. Lesson: model accuracy and workflow benefit are different measures.
- *Customer support assistant at scale* [NBER-W31161-2023]. 5,179 agents; productivity up 14% on average, 34% for novice and low-skilled, minimal for experienced workers; adjacent to this pattern (agent assist). Working paper, not peer reviewed at the time of the revision.
- *Hospital patient-message draft replies* [JAMANO-GARCIA-2024]: 5-week single-group quality improvement study, mean draft utilization 20%, no change in reply time, lower reported task load. Adjacent (draft-review-loop).
- *Emergency department triage with LLMs*: a meta-analysis of 15 studies found pooled accuracy 0.51 for ChatGPT-3.5, 0.70 for GPT-4 variants and 0.81 for optimized versions, and called the evidence for superiority over human triage fragile [BMCEM-GAO-2026, Abstract]; a pediatric study over 228,104 visits found accuracy 0.73 at picking the higher-acuity child of a pair, with a tendency to prioritize younger children [NPJHS-NARANG-2026, Abstract]. These are evaluations, not deployments.
- *Epic Sepsis Model external validation* [JAMAIM-WONG-2021]: AUC 0.63; missed 67% of sepsis cases while alerting on 18% of hospitalized patients. Adjacent (alert scoring) but shows the cost of deploying a scoring model without local validation.

**Benchmarks and lab studies**
- τ-bench (vendor research): leading function-calling agents succeeded on under 50% of tasks; pass^8 under 25% in retail [ARXIV-TAUBENCH-2024, Abstract]. Simulated users; not field data.
- CRMArena-Pro (vendor research): about 58% single-turn and 35% multi-turn success; near-zero inherent confidentiality awareness [ARXIV-CRMARENAPRO-2025, Abstract].
- Human-AI team studies: explanations raised acceptance of AI advice regardless of correctness [ARXIV-BANSAL-2021, Abstract].
- Foundations: learning to defer extends rejection learning by accounting for the downstream human decision-maker and, in experiments, improved accuracy and fairness [ARXIV-MADRAS-2018, Abstract]; modern neural networks are poorly calibrated, so confidence thresholds need checking [ARXIV-GUO-2017, Abstract]; acceptance sampling sits between no inspection and 100% inspection [NIST-HANDBOOK-2026].

**Organization-reported measurements (self-reported)**
- UK ATRS records: FCDO 0.7333 accuracy and macro F1 0.7467 on email category; prompt classifier about 0.6 after about 0.34 [ATRS-FCDO-CORR-2025]; FCDO consular 76-81% [ATRS-FCDO-CONSULAR-2024]; HMRC 83.03% on known intents [ATRS-HMRC-2025]; NS&I 22.23% contained [ATRS-NSI-2025]; DWP telephony +21% right-first-time routing, +9% deflection [ATRS-DWPCONV-2025].
- Klarna month-one figures [KLARNA-AIASSISTANT-2024] and the later CEO statement on quality [ENTREPRENEUR-KLARNA-2025].
- Bank of America 50% fewer IT service desk calls [BOFA-ERICA-2025].

**Failure and incident analyses**
- Air Canada liability [GUARDIAN-AIRCANADA-2024]; MyCity answers [MARKUP-MYCITY-2024]; Cursor invented policy [ARS-CURSOR-2025]; DPD update error [BBC-DPD-2024]; CFPB doom loops [CFPB-CHATBOTS-2023].

**Customer attitudes**
- Gartner survey of 5,728 customers, December 2023: 64% prefer no AI in service; 53% would consider switching; top concern is difficulty reaching a person [GARTNER-CSAT-2024]. Analyst survey; full questionnaire not read.

**What is absent.** No source in this run publishes, for a production triage or service agent: an override or overwrite rate, a miss rate on urgent items, the share of escalations later judged unnecessary or missing, the review sampling rate used, or a parallel run against human handling beyond FCDO's historic-batch comparison. No independent audit of the Klarna, Bank of America, Lyft, Danfoss or NS&I figures was found. Several ATRS fields give the supplier's generic benchmark instead of a local test (DVLA, ICO).

---

## 6. Candidates among `pattern: other` use cases

Skimmed the 226 entries tagged `pattern: other` (the brief says 227). Few resemble these patterns. Candidates:

- `security-ai-security-08` (A): gate agent actions with a tested classifier and send high-impact steps to a human. It classifies items and routes between auto-approve and human approval, with fallback to manual after repeated blocks. Reason: it is an intake-triage shape applied to agent actions rather than incoming requests. Suggest `intake-triage` as a secondary pattern, or keep `other` if the library wants triage limited to inbound requests.
- `assurance-quality-management-02` (B): risk-tiered permitted-use policy with "triage of proposals" and a clearing house. Reason: AI-use proposals are triaged into risk tiers, but the triage is human governance, not AI. Keep `other`.
- `assurance-planning-risk-assessment-22` (B) and `assurance-quality-management-11` (C): staffing request intake and routing; the entries say the AI's role is unspecified. Keep `other`.
- `professional-services-delivery-management-11` (C): tasks routed to agents and people with review gates. Reason: workflow routing, closer to `end-to-end-case-agent`. Keep `other` or move there.
- `tax-compliance-individual-business-10` (D, idea): language model kept for intake, explanation and orchestration with a deterministic engine for calculation. Intake here is information gathering, not triage. Keep `other`.

None of the others (financial, hiring-intake, training, disclosure and governance entries) resembles the two patterns.

---

## 7. Gaps

- **No manufacturing or retail deployment with a measured quality figure for `service-agent-escalation`.** Taobao is the only retail-platform measurement; Danfoss is a vendor case study with qualified figures.
- **No override, miss or warranted-escalation rates** in production for either pattern (see section 5).
- **ISO/IEC 42001 text not read.** The ISO page was blocked (HTTP 403); only BSI's description was read. Controls (Annex A) are not described here.
- **Moffatt v. Air Canada decision not read directly.** CanLII returned 403. The ruling is described through The Guardian and a law-firm summary, which quotes the decision [GUARDIAN-AIRCANADA-2024; MCCARTHY-MOFFATT-2024].
- **Bloomberg's Klarna article** body is paywalled; the 2025 reversal is known through a secondary report that quotes the CEO.
- **Insurance intake (Aviva, Allianz) not usable.** A search surfaced an Aviva claims-AI case on McKinsey's site (liability assessment time cut by 23 days; claims routing accuracy up 30%), but McKinsey blocked access, so the figures stay search-only and are not used. No primary Allianz source for "Project Nemo" results was found.
- **Vendor-reported resolution rates** (Intercom, Zendesk and others) appeared only in search summaries; not opened, so not used. A vendor ticket-triage guide's "recategorization rate" suggestion is search-only.
- **Gartner's 2025 prediction on agentic AI resolving 80% of common service issues** could not be fetched (404); only the 2024 customer survey was read.
- **Healthcare patient-message urgency triage in production**: studies and one draft-reply pilot found, but no production triage measurement.
- **Ticket and IT-service-desk routing** beyond UiPath: no second named engineering write-up with figures found; the arXiv API was unreachable from this environment.
- **Undated pages.** The Lyft, Danfoss, BSI and NIST handbook pages carry no publication date; their refs use the retrieval year and the table shows the retrieval date.
- **Search budget.** Seven web searches were used (Klarna, DWP, insurers, ticket routing, retail/manufacturing service, Taobao, Danfoss). All other sources were fetched directly or through the GOV.UK content API, Europe PMC and the r.jina.ai mirror.
- **Taobao paper status.** Posted May 2026 as a working paper; peer-review status not stated in the text read.
- **EU AI Act dates.** Application dates quoted are those shown on the artificialintelligenceact.eu mirror pages, which reflect Article 113 as that site presents it; verify against the Official Journal.

---

## 8. Sources

Access: `full` = opened and read (for journal articles read through Europe PMC, the abstract and results). `search-only` = seen in search results only; not used for any claim.

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| KLARNA-AIASSISTANT-2024 | Klarna AI assistant handles two-thirds of customer service chats in its first month | Klarna | firm | https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ | 2024-02-27 | full |
| ENTREPRENEUR-KLARNA-2025 | Klarna CEO Reverses Course By Hiring More Humans, Not AI | Entrepreneur | press | https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 | 2025-05-09 | full |
| BLOOMBERG-KLARNA-2025 | Klarna Rethinks AI Cost-Cutting Plan With Call for Real People (headline version "Klarna Slows AI-Driven Job Cuts With Call for Real People") | Bloomberg | press | https://www.bloomberg.com/news/articles/2025-05-08/klarna-turns-from-ai-to-real-person-customer-service | 2025-05-08 | search-only (headline and date via text mirror; body not readable) |
| NBER-W31161-2023 | Generative AI at Work (Brynjolfsson, Li, Raymond) | NBER | academic | https://www.nber.org/system/files/working_papers/w31161/w31161.pdf | 2023-11 (revision of 2023-04) | full |
| ARXIV-LINKEDIN-2024 | Retrieval-Augmented Generation with Knowledge Graphs for Customer Service Question Answering (SIGIR '24) | LinkedIn authors via arXiv | academic | https://arxiv.org/pdf/2404.17723 | 2024-05-06 | full |
| ARXIV-WANG-2026 | Agentic AI and Human-in-the-Loop Interventions: Field Experimental Evidence from Alibaba's Customer Service Operations | Wang, Zhu, Feng, Lu, Jia (Zhejiang, Fudan, Dartmouth, Alibaba) via arXiv | academic | https://arxiv.org/pdf/2605.14830 | 2026-05 | full |
| ARXIV-TAUBENCH-2024 | τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | Sierra via arXiv | academic | https://arxiv.org/pdf/2406.12045 | 2024-06-17 | full |
| ARXIV-CRMARENAPRO-2025 | CRMArena-Pro | Salesforce authors via arXiv | academic | https://arxiv.org/pdf/2505.18878 | 2025-05-24 | full |
| ARXIV-MADRAS-2018 | Predict Responsibly: Improving Fairness and Accuracy by Learning to Defer | Madras, Pitassi, Zemel (NeurIPS 2018) via arXiv | academic | https://arxiv.org/pdf/1711.06664 | 2018-09-07 | full |
| ARXIV-GUO-2017 | On Calibration of Modern Neural Networks | Guo, Pleiss, Sun, Weinberger (ICML 2017) via arXiv | academic | https://arxiv.org/pdf/1706.04599 | 2017-08-03 | full |
| ARXIV-BANSAL-2021 | Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance (CHI '21) | Bansal et al. via arXiv | academic | https://arxiv.org/pdf/2006.14779 | 2021-01-12 | full |
| JAMANO-BLOMBERG-2021 | Effect of Machine Learning on Dispatcher Recognition of Out-of-Hospital Cardiac Arrest During Calls to Emergency Medical Services: A Randomized Clinical Trial | JAMA Network Open (via Europe PMC, PMID 33404620) | academic | https://pmc.ncbi.nlm.nih.gov/articles/PMC7788469/ | 2021-01-04 | full (abstract) |
| JAMANO-GARCIA-2024 | Artificial Intelligence-Generated Draft Replies to Patient Inbox Messages | JAMA Network Open (PMID 38506805) | academic | https://pmc.ncbi.nlm.nih.gov/articles/PMC10955355/ | 2024-03-04 | full (abstract) |
| JAMAIM-WONG-2021 | External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients | JAMA Internal Medicine (PMID 34152373) | academic | https://pmc.ncbi.nlm.nih.gov/articles/PMC8218233/ | 2021-08-01 | full (abstract) |
| BMCEM-GAO-2026 | Accuracy of the large language model ChatGPT in adult emergency department triage: a systematic review and meta-analysis | BMC Emergency Medicine (PMID 41840524) | academic | https://pmc.ncbi.nlm.nih.gov/articles/PMC13104245/ | 2026-03-16 | full (abstract) |
| NPJHS-NARANG-2026 | Assessing acuity in pediatric emergency department triage: performance of a large language model | npj Health Systems (PMID 42552396) | academic | https://pmc.ncbi.nlm.nih.gov/articles/PMC13438747/ | 2026-08-05 | full (abstract) |
| CFPB-CHATBOTS-2023 | Chatbots in consumer finance | Consumer Financial Protection Bureau | regulator | https://www.consumerfinance.gov/data-research/research-reports/chatbots-in-consumer-finance/chatbots-in-consumer-finance/ | 2023-06-06 | full |
| NIST-AI100-1-2023 | Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1 | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 2023-01 | full |
| NIST-AI600-1-2024 | AI RMF: Generative AI Profile, NIST AI 600-1 | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | 2024-07 | full |
| EUAIA-2024 | Regulation (EU) 2024/1689 (AI Act): Annex III, Articles 14, 26, 50 (artificialintelligenceact.eu mirror) | European Union / Future of Life Institute mirror | regulator | https://artificialintelligenceact.eu/annex/3/ ; https://artificialintelligenceact.eu/article/14/ ; /article/26/ ; /article/50/ | 2024-06-13 (regulation adopted; mirror pages undated) | full |
| EC-GDPR-2016 | Art. 22 GDPR: Automated individual decision-making, including profiling (gdpr-info.eu) | European Union | regulator | https://gdpr-info.eu/art-22-gdpr/ | 2016-04-27 (regulation adopted; page undated) | full |
| BSI-ISO42001-2026 | ISO/IEC 42001 - AI Management System | BSI | standard-setter (certification body description) | https://www.bsigroup.com/en-GB/products-and-services/standards/iso-42001-ai-management-system/ | 2026-10-20 (retrieved; page undated) | full |
| NIST-HANDBOOK-2026 | NIST/SEMATECH e-Handbook of Statistical Methods, 6.2.1 What is Acceptance Sampling? | NIST | standard-setter | https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm | 2026-10-20 (retrieved; page undated) | full |
| ATRS-DWP-WHITEMAIL-2025 | DWP: Whitemail Insights and Vulnerability Scanner (algorithmic transparency record) | Department for Work and Pensions via GOV.UK | firm (public-body self-publication) | https://www.gov.uk/algorithmic-transparency-records/whitemail-insights-and-vulnerability-scanner | 2025-11-27 | full |
| PUBTECH-WHITEMAIL-2025 | DWP taps AI to scan 25,000 letters a day and identify vulnerable citizens | PublicTechnology | press | https://www.publictechnology.net/?p=12665 | 2025-12-08 | full (via text mirror) |
| ATRS-HMT-2024 | HMT: Correspondence Triage Automation Tool | HM Treasury via GOV.UK | firm (public-body) | https://www.gov.uk/algorithmic-transparency-records/hmt-correspondence-triage-automation-tool | 2024-12-17 | full |
| ATRS-FCDO-CORR-2025 | FCDO: Correspondence Triage | Foreign, Commonwealth and Development Office via GOV.UK | firm (public-body) | https://www.gov.uk/algorithmic-transparency-records/fcdo-correspondence-triage | 2025-12-16 | full |
| ATRS-FCDO-CONSULAR-2024 | FCDO: Consular Digital Triage - Written Enquiries LLM | FCDO via GOV.UK | firm (public-body) | https://www.gov.uk/algorithmic-transparency-records/fcdo-consular-digital-triage-written-enquiries-llm | 2024-12-17 | full |
| ATRS-ICO-2026 | ICO: ICE 360 Case Creation Automation | Information Commissioner's Office via GOV.UK | firm (public-body) | https://www.gov.uk/algorithmic-transparency-records/ico-ice-360-case-creation-automation | 2026-01-14 (updated 2026-04-13) | full |
| ATRS-DWPCONV-2025 | DWP: Conversational Platform | DWP via GOV.UK | firm (public-body) | https://www.gov.uk/algorithmic-transparency-records/dwp-conversational-platform | 2025-12-16 | full |
| ATRS-HMRC-2025 | HMRC: Ask HMRC online | HM Revenue and Customs via GOV.UK | firm (public-body) | https://www.gov.uk/algorithmic-transparency-records/hmrc-ask-hmrc-online | 2025-06-26 | full |
| ATRS-NSI-2025 | NS&I: PolyAI | National Savings and Investments via GOV.UK | firm (public-body) | https://www.gov.uk/algorithmic-transparency-records/ns-and-i-polyai | 2025-10-30 | full |
| ATRS-DVLA-CHATBOT-2025 | DVLA: Contact Centre Chatbot service | DVLA via GOV.UK | firm (public-body) | https://www.gov.uk/algorithmic-transparency-records/dvla-contact-centre-chatbot-service | 2025-12-16 | full |
| ATRS-MOJ-2026 | MoJ: PolyAI / Luna | Ministry of Justice via GOV.UK | firm (public-body) | https://www.gov.uk/algorithmic-transparency-records/moj-polyai-slash-luna | 2026-09-09 | full |
| ATRS-GOVUKCHAT-2025 | DSIT: GOV.UK Chat | DSIT / GDS via GOV.UK | firm (public-body) | https://www.gov.uk/algorithmic-transparency-records/dsit-gov-dot-uk-chat | 2025-10-07 | full |
| ATRS-HO-CARSV-2024 | Home Office: Complexity Application Routing Solution - Visits | Home Office via GOV.UK | firm (public-body) | https://www.gov.uk/algorithmic-transparency-records/home-office-complexity-application-routing-solution-visits | 2024-12-17 | full |
| BOFA-ERICA-2025 | A Decade of AI Innovation: BofA's Virtual Assistant Erica Surpasses 3 Billion Client Interactions | Bank of America | firm | https://newsroom.bankofamerica.com/content/newsroom/press-releases/2025/08/a-decade-of-ai-innovation--bofa-s-virtual-assistant-erica-surpas.html | 2025-08-20 | full |
| LYFT-ANTHROPIC-2026 | Lyft reduces customer support time by 87% with Claude | Anthropic | vendor | https://www.anthropic.com/customers/lyft | 2026-10-20 (retrieved; page undated) | full |
| DANFOSS-GCLOUD-2026 | Danfoss and Go Autonomous: Reimagining order management at scale with Google Cloud | Google Cloud | vendor | https://cloud.google.com/customers/danfoss | 2026-10-20 (retrieved; page undated) | full |
| UIPATH-CCA-2026 | Enterprise Case Classification Agent: Support Ticket Routing with AI | UiPath Engineering (Medium) | firm | https://engineering.uipath.com/enterprise-case-classification-agent-support-ticket-routing-with-ai-de5c822d8153 | 2026-01-12 | full (via text mirror; figures in images not read) |
| GUARDIAN-AIRCANADA-2024 | Air Canada ordered to pay customer who was misled by airline's chatbot | The Guardian | press | https://www.theguardian.com/world/2024/feb/16/air-canada-chatbot-lawsuit | 2024-02-16 | full |
| MCCARTHY-MOFFATT-2024 | Moffatt v. Air Canada: A Misrepresentation by an AI Chatbot | McCarthy Tetrault | professional-body (law firm blog) | https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot | 2026-10-20 (retrieved; page undated; decision is 2024 BCCRT 149) | full (via text mirror) |
| BBC-DPD-2024 | DPD error caused chatbot to swear at customer | BBC News | press | https://www.bbc.com/news/technology-68025677 | 2024-01-19 | full |
| MARKUP-MYCITY-2024 | NYC's AI Chatbot Tells Businesses to Break the Law | The Markup | press | https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law | 2024-03-29 (date from URL) | full |
| ARS-CURSOR-2025 | Company apologizes after AI support agent invents policy that causes user uproar | Ars Technica | press | https://arstechnica.com/ai/2025/04/cursor-ai-support-bot-invents-fake-policy-and-triggers-user-uproar/ | 2025-04-17 | full |
| GARTNER-CSAT-2024 | Gartner Survey Finds 64% of Customers Would Prefer That Companies Didn't Use AI For Customer Service | Gartner | survey | https://www.gartner.com/en/newsroom/press-releases/2024-07-09-gartner-survey-finds-64-percent-of-customers-would-prefer-that-companies-didnt-use-ai-for-customer-service | 2024-07-09 | full (via text mirror) |
| ANTHROPIC-AGENTS-2024 | Building effective agents | Anthropic | vendor | https://www.anthropic.com/engineering/building-effective-agents | 2024-12-19 | full |
| OPENAI-AGENTS-2025 | A practical guide to building agents | OpenAI | vendor | https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf | 2025-04 (PDF creation date 2025-04-07) | full |
| WILLISON-TRIFECTA-2025 | The lethal trifecta for AI agents: private data, untrusted content, and external communication | Simon Willison | community | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | 2025-06-16 | full |
| OWASP-LLM01-2025 | LLM01:2025 Prompt Injection | OWASP Gen AI Security Project | standard-setter | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | 2024-04-10 (page metadata; 2025 edition page) | full |
| GOVUK-GDS-2024 | Experimenting with how generative AI could help GOV.UK users | Government Digital Service | firm (public-body blog) | https://insidegovuk.blog.gov.uk/2024/01/18/experimenting-with-how-generative-ai-could-help-gov-uk-users/ | 2024-01-18 | full (read; used only for context: testing scaled to 1,000 invited users) |
| MCKINSEY-AVIVA-2025 | Aviva: rewiring the insurance claims journey with AI | McKinsey | firm | https://www.mckinsey.com/capabilities/tech-and-ai/how-we-help-clients/rewired-in-action/aviva-rewiring-the-insurance-claims-journey-with-ai | n/a (blocked, HTTP 403) | search-only |

Source-type counts (distinct documents read in full, counting the four EU AI Act pages as one): academic 12 (including 5 journal abstracts); regulator and standard-setter 7 (CFPB, two NIST documents, EU AI Act, GDPR Art. 22, OWASP, BSI/ISO description, NIST handbook counts as eighth: 8); public-body records 11 (ATRS x10 plus GDS blog); press 7; firm and vendor 8 (Klarna, Bank of America, UiPath, Lyft, Danfoss, Anthropic, OpenAI, Gartner survey as survey); practitioner discourse 2 (Willison, law-firm blog); one search-only. About 48 documents in total.

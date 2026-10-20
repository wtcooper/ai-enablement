# Topic research: AI governance and vendor evaluation in firms

Skill fed: `ai-governance` (policy, data rules, risk tiers and review, records of AI use, profession-specific duties, vendor and tool evaluation, approved-tool catalog).
Research date: 2026-10-20. Public sources only. Tools are described by runtime class (personal assistant, shared team skills, workflow automation, background agent, managed agent runtime). Vendor documents appear below only as evidence of what published terms say; nothing here recommends a vendor.

Conventions used in this file:
- Source refs follow `PUBLISHER-SHORT-YYYY` and are defined in section 9. A locator (section, article, page, figure or action ID) follows each ref.
- "Synthesis" marks an advisor heuristic that I assembled from cited material. It is not a sourced requirement and should be presented to users as a suggested starting point.
- Statistics: each states what it measures and who measured it (section 6). Per the Grade A rule (2026-10-17), a figure is treated as measured only when the named organization reports it as its own measurement (a survey result counts as a measured survey result; a recollection or rough estimate does not).

---

## 1. Summary

- **Governance work is mostly "known duties applied to a new tool", not new law.** The profession-specific duties (AICPA confidentiality and independence, IESBA technology revisions, ABA Model Rules as read in Opinion 512, IRC section 7216 regulations, PCAOB staff observations) all say the existing duties continue to apply and the user stays responsible for the output (JOFA-2026; IESBA-TECH-2023; ABA-512-2024; PCAOB-GENAI-2024).
- **Policy without enablement does not hold.** In a 47-country survey led by the University of Melbourne with KPMG, 48% of employees who use AI said they had uploaded company information to public AI tools, and most workplace users used free public tools. The report authors say the pattern suggests bans may be ineffective and that having a policy does not guarantee compliance (KPMG-MELB-2025). Practitioner playbooks reach the same conclusion: approved tools with a fast request path (GEND-2026; AMPCUS-2026; both vendor blogs, directional only).
- **Govern by data class and consequence of error, not by tool name alone.** The same vendor can publish different terms for consumer and commercial tiers, and the commercial-tier pages say business inputs are not used for training by default, with stated exceptions such as opt-in feedback (ANTHROPIC-PRIV-2026; OPENAI-ENT-ND; MSFT-COPILOT-ND). The unit of approval is therefore tool + tier + contract + data class.
- **Tax-return information is the sharpest data rule.** Section 7216 regulations require prior, signed, specific written consent unless a listed exception applies, forbid making consent a condition of service in most cases, and treat "substantive determinations" (analysis, interpretation or application of law) by another preparer as needing consent. I found no AI-specific IRS guidance (ECFR-7216-2008; gap noted in section 10).
- **Records of AI use are becoming an expectation, proportionately.** The FRC (UK, June 2025) asks for proportionate documentation of what an AI tool does, how it was developed and tested, and how the firm knows it works, including for third-party tools; it states the guidance introduces no new requirements (FRC-AI-2025). The PCAOB staff reported some firms design tools to document underlying source data (PCAOB-GENAI-2024, p.5). A CPA-firm insurer-affiliated guide suggests recording prompts, how outputs were verified and who reviewed them in the client file (CPAI-ND).
- **Vendor evaluation has a published control list.** NIST AI 600-1 gives concrete actions: update procurement due diligence for embedded GenAI, inventory third parties with access to content, keep approved-provider lists, write contracts covering ownership, usage rights, quality and security, and reserve the right to evaluate third-party processes (NIST-600-1-2024, GV-1.6-001 and GV-6.1-004 to -007).
- **The gap between policy and practice is measured, and large.** In an EY-commissioned survey of 202 senior AI executives at US public companies with at least $1 billion revenue (fielded May 28 to June 15, 2026), 98% reported formal AI governance policies and 47% said their organization had previously not applied its governance process to urgent deployments (EY-AIGOV-2026).
- **EU deployer timing changed in 2026.** Regulation (EU) 2026/1744 (dated 8 July 2026) sets application of the Annex III high-risk obligations to 2 December 2027 and softens Article 4 AI literacy from ensuring a sufficient level to supporting its development (EU-OMNIBUS-2026). Most firm use cases (drafting, summarising, research) are not obviously Annex III; employment-related uses are listed (AIACT-EXPL-2026, Annex III point 4).

---

## 2. Core concepts in plain language

1. **Acceptable-use policy (AUP) is the floor, not the program.** An AUP says who may use which tools for what. It only works with three companions: a catalog of approved tools people can actually get, a request path that answers quickly, and training. For knowledge work, the AUP is mostly a data-handling rule ("what may I paste where"), because the main exposure is confidential client information entering a tool. (CPAI-ND; KPMG-MELB-2025, p.75)

2. **Data classification maps to tool tiers.** Define a small number of data classes (for example public, firm-internal, client-confidential, and regulated or privileged such as tax-return information or legal-privileged material) and state which tool tier each class may enter. The tier depends on where inputs are stored, who can access them, whether they are de-identified, and whether they train the tool (CPAI-ND). For AI this means the approval is for a specific product tier and contract, because published terms differ by tier (ANTHROPIC-PRIV-2026; OPENAI-ENT-ND).

3. **Risk tiers set the human review.** Tier a use by what happens if the output is wrong and who relies on it (internal draft, internal research, client-facing deliverable, a decision about a person, an attest or filing). NIST GOVERN 1.3 asks for risk-management effort sized to the organization's risk tolerance (NIST-RMF-2023, p.22). The PCAOB staff heard from firms that AI is expected to augment, not replace, humans, that the engagement team member remains responsible, and that reviewers apply the same diligence as when AI was not involved (PCAOB-GENAI-2024, pp.4-5). The review standard therefore does not drop because AI helped; the tier sets how much extra checking the first-line user must do and how it is recorded.

4. **Records of AI use are about reconstruction.** Someone later (a reviewer, regulator, client or court) must be able to see what tool was used, on what, what was checked, and by whom. What to keep scales with the tier. The FRC calls for proportionate documentation and warns against over-documentation (FRC-AI-2025). Logs also create retention and confidentiality obligations of their own, because tools store prompts and responses (MSFT-COPILOT-ND).

5. **Model risk: you cannot see inside the vendor model, so you challenge it.** Banking supervisors' model-risk guidance says validation applies equally to vendor models, that "effective challenge" comes from objective, informed parties, and that the firm must choose models appropriate for its use even when it relies on a vendor (FRB-SR117-2011, effective challenge on p.4; validation of vendor-supplied models and the footnote on reliance on vendors in the model-validation and model-development sections). For AI tools this translates to testing against your own work samples before approval and re-testing when the vendor changes the underlying model (synthesis, anchored on NIST-600-1-2024 GV-1.6-003, which lists underlying model versions as an inventory field).

6. **Frameworks are vocabularies, not rulebooks.** NIST AI RMF organizes work into GOVERN, MAP, MEASURE and MANAGE (NIST-RMF-2023, p.22 onward); NIST AI 600-1 adds a generative-AI profile with twelve named risks including confabulation, data privacy, information security, intellectual property and value-chain integration (NIST-600-1-2024, section 2). ISO/IEC 42001 is a certifiable management-system standard; its text is paywalled and secondary sources disagree on the Annex A control count (38 vs 39; see gaps). The CSA AI Controls Matrix maps 243 control objectives in 18 domains to ISO 42001, ISO 27001, NIST AI RMF 1.0 and BSI AIC4 (CSA-AICM-2025). Practitioners usually pick one as the backbone and map the others.

7. **EU AI Act: a firm is usually a "deployer".** Deployer duties for high-risk systems include using the system per instructions, assigning human oversight to people with competence, training and authority, monitoring, keeping automatically generated logs under their control for at least six months, and informing workers before workplace use (AIACT-EXPL-2026, Art 26(1),(2),(5),(6),(7)). These apply to systems classified high-risk (Annex III lists, among others, education and employment uses). AI literacy under Article 4 applies to all deployers (AIACT-EXPL-2026, Art 4; EU-OMNIBUS-2026, Art 1(5)).

8. **Profession-specific duties sit on top.** Accountants: competence and due care, confidentiality (AICPA ET 1.700.001), and independence when providing or hosting AI for attest clients (JOFA-2026). IESBA's technology revisions are effective 15 December 2024 (IESBA-TECH-2023). Tax preparers: section 7216 consent (ECFR-7216-2008). Lawyers: competence, confidentiality with informed consent (not boilerplate), communication, supervision and fees, per ABA Opinion 512 (ABA-512-2024, via secondary summary). UK solicitors: supplier due diligence on AI tools and review of terms (LAWSOC-GENAI-2026).

9. **Vendor evaluation is a data-flow and change-control question first.** The security questionnaire matters less than five facts: what data is retained and for how long, whether it trains models, who the sub-processors are and where processing happens, what certifications cover this product (and which scope), and what happens when the vendor changes the model, a sub-processor, or its terms, or when you leave (NIST-600-1-2024, GV-6.1-004, -006, -007, -008; OPENAI-ENT-ND; MSFT-COPILOT-ND).

10. **From risk identification to secure enablement.** The IT and security shift is from "list the risks and block" to "provide approved tools with SSO, logging and data controls, a request path, and discovery of what is already in use" (GEND-2026; AMPCUS-2026; both vendor blogs). The evidence supporting the shift is the survey data on bypass behaviour (KPMG-MELB-2025; MSFT-WTI-2024), not the blogs.

---

## 3. Expert moves

Format: **move** — when to use it — what it reveals — source ref (locator).

1. **Ask "which AI tools did you use last month for client work, including personal accounts and free tools?" before drafting any policy** — onboarding, framing — reveals the actual data flows and the gap between policy and practice; employees' reported behaviour differs from sanctioned use — KPMG-MELB-2025 (exec summary p.6: most use free public tools; p.75: 48% upload); MSFT-WTI-2024 (78% of AI users bring their own tools; vendor survey).

2. **Ask what happened the last time someone was told "no" or "wait"** — policy diagnosis — reveals whether a ban or slow approval drives use out of sight; the KPMG report found uploads most common where a ban existed (67%) or a policy existed (56%) vs no policy (33%) or unsure (38%), and its authors say this suggests bans may be ineffective (self-reported, correlational) — KPMG-MELB-2025 (p.75).

3. **Test policy awareness with a one-question poll: "Do we have an AI policy and what does it say about client data?"** — diagnosis, before launch and after training — reveals the awareness gap; in the survey only about two in five employees said their organization had a policy or guidance and almost one in five did not know — KPMG-MELB-2025 (p.71, Fig 41 text).

4. **Define data classes with one worked example per class, and include a redaction example** — policy drafting — reveals whether staff can classify; the CPAi guide recommends training with examples of what cannot be entered, how to redact, and alternatives that avoid violating privacy requirements — CPAI-ND ("data security" section).

5. **For each candidate tool ask "which product tier and contract?" and record it as a separate catalog entry** — tool evaluation — reveals that the consumer tier and commercial tier of the same vendor carry different data terms; Anthropic's commercial page explicitly separates consumer products (Free, Pro, Max) from commercial ones — ANTHROPIC-PRIV-2026; OPENAI-ENT-ND ("Does OpenAI train its models on my business data?"); MSFT-COPILOT-ND.

6. **Read the exceptions to "we don't train on your data"** — vendor review — reveals opt-in feedback paths and retention for feedback data; the Anthropic page says thumbs-up/down feedback conversations can be stored up to 5 years and that an organization owner can disable the feedback control; OpenAI says opted-in shared data may be used for training — ANTHROPIC-PRIV-2026 ("Feedback", "Disabling Feedback"); OPENAI-ENT-ND.

7. **Ask for retention controls and who holds the activity history** — vendor review and records design — reveals whether admins can set retention and whether prompts and responses are retrievable for audit; OpenAI says workspace admins control retention and deleted conversations are removed within 30 days unless legally required to retain; Microsoft says prompts and responses are stored as activity history and admins can manage retention through Purview — OPENAI-ENT-ND ("data retention"); MSFT-COPILOT-ND.

8. **Ask where inference and storage happen** — vendor review for tax, EU or client-residency constraints — reveals offshore processing; Microsoft's page says customers outside the EU may have queries processed in the US, EU or other regions; under the tax regulations, disclosure outside the US needs prior consent and SSNs cannot be disclosed offshore under consent — MSFT-COPILOT-ND; ECFR-7216-2008 (301.7216-2(d) Example 3; 301.7216-3(a)(3)(i)(D), (b)(4)).

9. **Apply the 7216 triage in order: (a) is it tax return information; (b) is there a listed exception; (c) is the recipient doing only non-substantive processing in the US; (d) otherwise obtain written consent first** — tax practice use cases — reveals which AI steps need consent; consent must be written, signed and dated, name preparer and taxpayer, state purpose and recipient, specify the information, cannot be retroactive, defaults to one year if duration is unstated, and uses and disclosures need separate documents — ECFR-7216-2008 (301.7216-3(a)(1),(a)(3)(i),(b)(1),(b)(5),(c)(1)).

10. **Ask "does the AI step analyse, interpret or apply the law?"** — tax and legal AI use — reveals the "substantive determination" line; in the regulation's example, sending return information to another firm for advice on a deduction needs prior consent, while pure data processing in the US does not — ECFR-7216-2008 (301.7216-2(d)(1) and Example 4). Whether a given AI vendor is a "tax return preparer" or an auxiliary-service provider is an open interpretive question I could not resolve from IRS sources (see gaps); a 2026 ABA Tax Section panel abstract poses exactly this question — WINTHROP-2026.

11. **Do not make 7216 consent a condition of the engagement** — tax engagement letters — reveals a consent-validity trap; the regulation says conditioning services on consent makes it involuntary, with a stated exception for preparer-to-preparer disclosure to assist in preparation — ECFR-7216-2008 (301.7216-3(a)(1),(a)(2)).

12. **For lawyers, ask "is the consent specific, or boilerplate in the engagement letter?"** — legal AI use that puts client information into a tool — reveals non-compliant consent; Opinion 512, as summarised, says boilerplate authorising AI use is not sufficient and consent requires explaining risks; consent is not needed if no client-related information is input — ABA-512-2024 (via Ezel summary, "Plain-English summary", Rule 1.6 paragraph; confirm against the ABA PDF).

13. **Ask how AI-saved time is billed** — legal and any time-based professional services — reveals a fee-policy gap; Opinion 512 (as summarised) says an hourly biller may bill only time actually spent — ABA-512-2024 (via Ezel summary, fees paragraph).

14. **Ask "are we building, hosting or configuring AI for any attest client, and do clients receive any tool we buy?"** — independence screen — reveals nonattest-service and information-systems exposure; the AICPA ethics article says AI-related nonattest services such as developing or hosting an AI system for an attest client can raise independence concerns, and IESBA's revisions address technology-related non-assurance services to audit clients — JOFA-2026 ("AI services can raise independence concerns"); IESBA-TECH-2023.

15. **Tier by consequence of error and audience; write the review step into the tier** — risk-tier design — reveals which uses need verified sources, second-person review or prohibition; examples in the field: some firms in the PCAOB outreach allow GenAI for administrative documents and initial drafts and for internal guidance research, while some do not allow it for audit or attest procedures — PCAOB-GENAI-2024 (p.4, "Current Use" and "Limitations"); NIST-RMF-2023 (GOVERN 1.3). Tier thresholds themselves are synthesis (see section 8).

16. **Set the review standard as "same diligence as if AI were not involved", and keep the user accountable** — review policy — reveals whether supervisors are being asked to relax review; firms told the PCAOB their supervision policies had not changed and that team members remain responsible for results and documentation — PCAOB-GENAI-2024 (pp.4-5); ABA-512-2024 (via Ezel: lawyer fully responsible whatever the review level).

17. **Require three items in the file for substantive AI-assisted work: prompt, how the output was verified, who reviewed** — records of AI use — reveals whether review actually happened; this is a practitioner recommendation, not a mandate — CPAI-ND ("If it isn't documented, it didn't happen").

18. **For firm-built or configured tools, document purpose, appropriate use, development and testing, and how you know it works; for third-party tools, document why you can rely on it where the vendor withholds detail** — audit-quality evidence — reveals the minimum record regulators are signalling; proportionate, not exhaustive — FRC-AI-2025 (news release, key features); KN-2025.

19. **Build the inventory to include embedded AI features and the underlying model and version** — inventory — reveals AI that arrives inside existing software; NIST 600-1 suggests policies define inventory exemptions for GAI embedded in application software and lists data provenance, known issues, human-oversight roles, IP and sensitive-data considerations, and underlying foundation models and versions as inventory fields — NIST-600-1-2024 (GV-1.6-001, -002, -003).

20. **Use NIST's third-party actions as the vendor contract checklist** — contract review — reveals missing clauses: content ownership and usage rights, quality standards, security requirements, provenance expectations (GV-6.1-004); a right to evaluate third-party GAI processes and standards (GV-6.1-006); inventory of all third parties with access to organizational content and an approved-provider list (GV-6.1-007); records of third-party changes to content (GV-6.1-008) — NIST-600-1-2024.

21. **Ask what notice you get when the vendor changes the model, a sub-processor or the terms, and write your re-approval trigger** — change control — reveals silent drift; NIST asks for inventory fields for model versions and records of third-party changes; the sub-processor and notice terms themselves I did not find in a primary source, so treat the trigger design as synthesis — NIST-600-1-2024 (GV-1.6-003, GV-6.1-008).

22. **Ask for the exit and failure plan before signing** — contract and approval — reveals lock-in and continuity gaps; NIST GOVERN 1.7 asks for safe decommissioning processes and GOVERN 6.2 for contingency processes for failures or incidents in high-risk third-party data or AI systems — NIST-RMF-2023 (p.23 GOVERN 1.7; p.24 GOVERN 6.2).

23. **Ask "what did the last urgent deployment skip?"** — governance stress test — reveals the bypass path; 47% of surveyed senior AI executives said their organization had previously not applied its governance process to urgent deployments while 98% had formal policies — EY-AIGOV-2026 (key findings). Design an expedited lane rather than relying on exceptions (synthesis).

24. **Ask "can we detect an unauthorised agent running in our environment?"** — background-agent and workflow-automation classes — reveals visibility gaps; 26% of surveyed executives whose organization uses agentic AI said theirs cannot detect unauthorised AI agents; OWASP lists excessive agency among LLM application risks — EY-AIGOV-2026; OWASP-LLM-2025 (Top 10 listing, "An LLM-based system is often granted a degree of agency").

25. **Run incident replays as scenario tests: "if this output reached the client unverified, which of our controls would catch it?"** — review-design workshops — reveals review controls that exist on paper only; public examples: counsel sanctioned $5,000 for submitting non-existent cases generated by a chatbot, and a consultancy partly refunding a government report containing incorrect references after disclosing generative AI use — SDNY-AVIANCA-2023 (Opinion and Order on Sanctions, ordering paragraph d); GUARDIAN-DELOITTE-2025.

26. **Add AI questions to the privacy impact process you already run, and let the existing owner lead** — governance setup in a firm with a privacy or risk function — reveals the cheapest route to an AI impact assessment; IAPP reports AI impact assessment questions are commonly added to existing privacy documentation, and privacy and legal/compliance are each the top primary owner at 22% of respondents — IAPP-GOV-2025 ("Top functions" list and privacy-program paragraph).

27. **Name an AI lead or committee with five jobs: review use cases, approve tools, maintain policy, monitor compliance, handle incidents** — governance setup — reveals who answers the staff question "can I use this?" — CPAI-ND ("treat it as a governance issue").

28. **Re-run the impact or risk assessment on a schedule and on triggers** — program maintenance — reveals stale approvals; Microsoft's own responsible AI standard requires impact assessments be updated at least annually, when new intended uses are added, and before advancing a release stage (Microsoft's internal product standard, used here only as a named-company template for cadence) — MSFT-RAI-2022 (Goal A1, A1.3).

29. **Use an internal-audit frame for high-tier uses: scope, map, collect artifacts, test, reflect** — high-tier use cases — reveals missing evidence before launch; this is the SMACTR framework, published by Google and Partnership on AI researchers for internal algorithmic audit — RAJI-2020 (section 4).

---

## 4. Question bank

Scope tags: **[T]** team, **[U]** unit, **[O]** organization. Journey stage tags: **[explore]** no approved tools yet, **[pilot]** some approved tools and use cases, **[scale]** many users and use cases.

### Onboard
- What tools do people use for client work today, including personal accounts and browser add-ons? [T/U/O] [explore]
- Which professional regimes bind us (audit/attest, tax-return preparation, legal practice, regulated-client contracts)? [U/O] [explore]
- Who currently decides whether a new tool is allowed, and how long does it take? [U/O] [explore/pilot]
- Do we have an AUP, and what share of staff could state its main rule on client data? [O] [pilot]
- What do our top client contracts and outside-guidelines say about AI use, subcontractors and data location? [U/O] [explore/pilot]

### Frame
- Which decisions or deliverables must never rely on unreviewed AI output? [T/U] [explore]
- What is the worst realistic failure in this unit (confidentiality breach, wrong filing, fabricated authority, independence breach)? [U] [explore]
- What does "approved" mean here: tool, tier, contract, data class, user group? [O] [explore]
- Which standard will the board or partners accept as the backbone (NIST AI RMF, ISO/IEC 42001, internal)? [O] [pilot/scale]
- Which existing owners (privacy, security, risk, ethics, general counsel) already cover part of this? [O] [explore]

### Map
- For this workflow, which data classes enter the AI step, and where does each go (vendor, region, sub-processors)? [T] [pilot]
- Does any step involve tax return information, privileged material, personal data, or attest-client data? [T/U] [pilot]
- Is the AI step a "substantive determination" (analysis, interpretation, application of law)? [T] [pilot]
- Which tool runtime class is in play (personal assistant, shared team skills, workflow automation, background agent, managed agent runtime), and what permissions does it hold? [T/U] [pilot/scale]
- Where is AI already embedded in software we license? [O] [pilot/scale]

### Diagnose
- When did someone last bypass the policy, and why? [T/U] [pilot]
- What did our last urgent deployment skip? [U/O] [scale]
- What evidence would we show a regulator, client or court that review happened on the last five AI-assisted deliverables? [T/U] [pilot/scale]
- Which assurance or audit-quality reviews have looked at AI use, and what did they find? [U/O] [scale]
- Which incidents or near misses have we logged, and who reviews them? [O] [scale]

### Reimagine (four lenses)
- Improve the step: can a lower-risk data class or a redacted input do the same job? [T]
- Automate the flow: which controls (DLP, SSO, logging, retention) can be built into the approved tool rather than relying on staff memory? [U/O]
- Delegate the outcome: if an agent acts, what is its least-privilege scope, what actions need a human approval, and how do we detect unauthorised agents? [U/O] [scale]
- Reinvent the work: if the review step changes (for example verifying citations by machine), what does the reviewer still own personally? [U]

### Prioritize
- Which use cases are low data-class, low-consequence and quick to approve (a fast lane)? [U] [pilot]
- Which candidate uses need consent, an independence check, or a high-tier review before any pilot? [U] [pilot]
- Which approvals unlock the most use for the least risk (one enterprise-tier tool for internal-class data vs many niche tools)? [O] [pilot]

### Make the case
- What does one avoided incident cost us (client loss, sanctions, refund, remediation)? [O] [scale]
- What would we have to show to move this use from pilot to production (test results on our samples, review records, vendor evidence)? [U] [pilot]
- What does non-adoption cost if staff keep using unsanctioned tools? [O] [explore/pilot]

### Plan
- Who owns the tool catalog, the request path, and the response-time commitment? [O] [pilot]
- What are our re-approval triggers (model change, sub-processor change, terms change, new data class, new use)? [O] [scale]
- What are our exit and failure plans for each approved tool? [U/O] [scale]
- What training and acknowledgement will each role complete, and how do we sample compliance? [O] [pilot]
- What is our cadence for reviewing the policy and the catalog? [O] [scale]

### Vendor and tool evaluation (use at Map and Plan)
- Which product tier, contract and data processing terms apply to us? [T/O] [pilot]
- Are inputs and outputs used for training by default; what are the opt-in and feedback exceptions; can admins disable them? [T/O]
- What is retained, for how long, who can retrieve it, and can we set retention? [T/O]
- Where is data stored and processed, and which sub-processors touch it? [O]
- Which certifications cover this product and scope (for example SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 42001), and what period and exclusions? [O]
- What notice do we get of model, sub-processor and terms changes? [O]
- What can we test before approval on our own samples, and what are the known limitations? [U]
- What are the warranties, liability limits and incident-notification terms? [O] (LAWSOC-GENAI-2026 notes warranties are often limited.)
- How do we export our data and leave? [O]

---

## 5. Common traps

| Trap | Why it happens | Evidence | How to avoid |
|---|---|---|---|
| **Ban-first policy** | Risk teams default to blocking | KPMG-MELB-2025: uploads reported by 67% of employees in organizations with a ban, vs 33% with no policy (self-reported, correlational; authors say bans may be ineffective) | Provide an approved tool and a request path first; then restrict (GEND-2026, vendor blog) |
| **Policy exists, nobody knows it** | Policy published without training | KPMG-MELB-2025 p.71: about two in five say policy or guidance exists; almost one in five do not know; 56% used AI at work without knowing if it was allowed (p.75) | Role-based training with examples, acknowledgement, spot checks (CPAI-ND) |
| **Governance skipped when urgent** | Review is slow, deadlines are real | EY-AIGOV-2026: 47% skipped the process for urgent deployments despite 98% having policies | Design an expedited lane with minimum controls; log exceptions |
| **Approving the vendor, not the tier** | Procurement buys "the tool" | Published terms differ by consumer vs commercial tier (ANTHROPIC-PRIV-2026) | Catalog entry = tool + tier + contract + data class |
| **Blanket boilerplate consent** | Easy to add to engagement letters | ABA Opinion 512 (as summarised): boilerplate not sufficient; ECFR-7216-2008: consent must be specific, signed, dated, prior | Consent explains risks, names purpose and recipient; do not condition service on it |
| **Treating the approved list as proof of control** | Lists are easy to publish | Practitioner view that exposure travels with data through unlisted channels and AI features inside approved SaaS (AMPCUS-2026, vendor blog; directional) | Add discovery, DLP and an inventory that includes embedded features (NIST-600-1-2024 GV-1.6-002) |
| **Review that changes nothing** | Reviewers trust fluent output | KPMG-MELB-2025 p.75: 66% of employees reported relying on AI output without evaluating it and 56% reported mistakes from AI use (self-reported); public cases: SDNY-AVIANCA-2023, GUARDIAN-DELOITTE-2025 | Define what the reviewer verifies, require source checks for any citation, record who reviewed |
| **Treating certifications as fitness for your use** | Certificates are easy to request | SOC 2 and ISO 42001 evidence shows controls exist; ISO 42001 certification does not satisfy EU AI Act obligations on its own (OPENLAYER-2026, vendor blog; not independently verified) | Ask for scope, period and exclusions; still test on your data and use |
| **Over-documenting** | Fear of audit | FRC explicitly seeks proportionate documentation and avoidance of over-documentation (FRC-AI-2025) | Scale record to tier; keep logs only as long as needed and secure them (prompts and responses are stored data: MSFT-COPILOT-ND) |
| **Using stale EU dates** | Dates moved in 2026 | EU-OMNIBUS-2026 Art 1(40); AIACT-EXPL-2026 page note | Quote Reg (EU) 2026/1744 and re-verify dates before client advice |
| **Ignoring independence in AI services to attest clients** | AI work is seen as "just technology" | JOFA-2026; IESBA-TECH-2023 | Add an independence screen to the intake form |
| **Agents outside the inventory** | Agents are easy to create inside productivity tools | EY-AIGOV-2026: 26% of agentic-AI users cannot detect unauthorised agents | Inventory agents like users; least privilege; logging; approval for sensitive actions (OWASP-LLM-2025 on excessive agency) |

---

## 6. Evidence

Provenance labels: **independent** (academic or non-commercial body, no stake in the finding), **self-reported** (organization reports its own data or respondents self-report), **vendor-published** (commercial firm publishing about its market or product). A survey is "self-reported" at the respondent level even when the publisher is independent. None of the surveys below measures review effectiveness, error rates or override rates directly.

| # | Data point | What it measures (source's words, paraphrased) | Provenance | Source |
|---|---|---|---|---|
| 1 | 48% (48-49% depending on item) | Share of employees who use AI who report they have uploaded sensitive company information (financial, sales, customer) or copyrighted material to public AI tools | Self-reported survey; University of Melbourne-led with KPMG collaboration; 48,340 respondents, 47 countries, Nov 2024 to mid-Jan 2025; employee sample 32,352 | KPMG-MELB-2025, p.75; sample size p.13 (PDF p.15) |
| 2 | 66% / 56% | Employees who report relying on AI output without critically evaluating it / who report having made mistakes in their work due to AI | Same survey (self-reported) | KPMG-MELB-2025, p.75 |
| 3 | "Two in five"; "almost one in five" | Employees reporting their organization has a policy or guidance on generative AI / who do not know whether one exists | Same survey (self-reported); I cite the text, not the figure bars, which I could not map reliably | KPMG-MELB-2025, p.71 |
| 4 | 67% / 56% / 33% / 38% | Share reporting uploading company information to public tools among employees whose organization banned GenAI / has a guiding policy / has no policy / is unsure | Same survey; authors say findings suggest bans may be ineffective and note social desirability may cause under-reporting | KPMG-MELB-2025, p.75 |
| 5 | 78% (80% at small and medium companies) | Among AI users in Microsoft and LinkedIn's survey, share bringing their own AI tools to work | Vendor-published; survey of 31,000 people in 31 countries; 2024 (page publication date not reliable in my fetch) | MSFT-WTI-2024 |
| 6 | 98% / 47% / 36% / 26% | Senior AI executives reporting formal AI governance policies / that the organization previously did not apply its governance process to urgent deployments / that it experienced an AI incident or failure with materially negative impact / (agentic-AI users only) that it cannot detect unauthorised AI agents | Self-reported; EY-commissioned online survey, 202 US senior AI decision-makers at public companies with at least $1bn revenue, fielded 28 May to 15 June 2026, margin of error ±7 points (EY sells assurance services; vendor-published) | EY-AIGOV-2026 |
| 7 | 57% / 48% / 39% | Among respondents whose organizations ran formal AI assurance reviews: share reporting data quality problems / model drift / shadow AI as common findings | Same EY survey | EY-AIGOV-2026 |
| 8 | 77%; about 90%; 30% | Organizations (survey of more than 670 individuals in 45 countries) working on AI governance; among those already using AI; among those not yet using AI | Self-reported; IAPP survey conducted spring 2024 per the page; page carries a 2025-10-30 timestamp, so the report date is uncertain | IAPP-GOV-2025 |
| 9 | 22% / 22% / 17% / 10% / 6% / 5% | Primary-responsibility function for AI governance: privacy / legal and compliance / IT / data governance / ethics and compliance / security | Same IAPP survey | IAPP-GOV-2025 |
| 10 | 233 incidents; +56.4% | Number of AI-related incidents reported in the AI Incidents Database for 2024, and change from 2023 (counts reports, not true incidence) | Independent (Stanford HAI) reporting a third-party database | HAI-INDEX-2025, Responsible AI chapter, key takeaway 2 |
| 11 | 64% / 63% / 60% | Share of respondents in a McKinsey responsible-AI survey citing inaccuracy / regulatory compliance / cybersecurity as concerns (as reported in the AI Index; I did not read the McKinsey report) | Measured by McKinsey, reported second-hand | HAI-INDEX-2025, key takeaway 3 |
| 12 | more than 240 stakeholders | Participants in IAASB technology roundtables held in late 2025 (participation count, not a rate) | Self-reported by standard-setter | IAASB-TECH-2026 |
| 13 | 1,725 risks from 74 frameworks | Count of risks extracted into the MIT AI Risk Repository from existing taxonomies | Independent academic (arXiv 2408.12622) | MIT-RISKREPO-2024 |
| 14 | 243 control objectives, 18 domains | Size of the CSA AI Controls Matrix (AICM) v1 | Non-profit industry body | CSA-AICM-2025 |
| 15 | $5,000 | Penalty imposed jointly on counsel and firm for submitting non-existent judicial opinions generated by a chatbot (case: Mata v. Avianca, order of June 22, 2023) | Court record (primary) | SDNY-AVIANCA-2023, ordering paragraph d |
| 16 | $440,000 (as stated in the article) | Value of an Australian government department review report for which the consultancy agreed to repay the final contract instalment after errors including incorrect references were found and generative AI use was disclosed; the consultancy did not say AI caused the errors and said findings were unaffected | News reporting (The Guardian) | GUARDIAN-DELOITTE-2025 |

Search-only or second-hand figures I did not use as evidence (found via a rationed search or quoted in vendor blogs, not read at source): Gartner 2025 survey finding that 69% of organizations suspect or have evidence of prohibited public GenAI use; IBM Cost of a Data Breach 2026 figure that shadow AI was involved in 43% of studied incidents (quoted in AMPCUS-2026); McKinsey State of AI 2025 adoption and mitigation figures. Verify at source before use.

---

## 7. Worked examples

These are illustrative composites built from the cited rules; they are not case studies of named firms (except where an incident is cited).

### Example A: Tax practice wants AI to summarise client returns and draft workpaper notes
- **Context:** A US firm prepares individual and business returns. A team proposes a shared team skill (a reusable prompt-and-document workflow in an enterprise assistant) to summarise prior-year returns and draft memos.
- **Triage:** (1) Inputs are tax return information. (2) Is the AI step only processing, or analysis of law? Summarising a return is processing; drafting a position memo applies law (ECFR-7216-2008, 301.7216-2(d)(1), Example 4). (3) Is the vendor a contractor needing the 6713/7216 written notice for individuals receiving information? (301.7216-2(d)(2)). (4) Where is data processed? Outside the US requires consent and SSN redaction (Example 3; 301.7216-3(b)(4)). (5) Which tier and contract: confirm commercial terms on training and retention (OPENAI-ENT-ND, ANTHROPIC-PRIV-2026 and MSFT-COPILOT-ND show what such published terms look like; they are not endorsements).
- **Decision (synthesis):** Approve summarisation on a commercial-tier tool with US processing and masked SSNs; route any position-drafting to a high tier with preparer review and, where the vendor step involves a substantive determination, obtain prior signed consent. Record prompt, verification and reviewer in the file (CPAI-ND). Escalate the unresolved question of whether the vendor is a covered preparer to counsel (no AI-specific IRS guidance found).

### Example B: Audit team uses an assistant for technical research and first drafts of memos
- **Context:** An audit practice allows GenAI for research and drafts but not for performing audit procedures, mirroring practice some firms described to the PCAOB staff (PCAOB-GENAI-2024, p.4).
- **Rules applied:** Supervision unchanged and team member remains responsible (PCAOB-GENAI-2024, pp.4-5). Independence: if the firm builds or hosts an AI tool for an attest client, run the nonattest-services analysis (JOFA-2026). For a firm-built tool used in audit work, document what it does, when it is appropriate, how it was developed and tested, and how the firm knows it works (FRC-AI-2025, for UK audit; US firms should check PCAOB and AICPA requirements, which I did not find as AI-specific rules).
- **Decision (synthesis):** Two lanes. Research/drafting: approved tool, internal-class data only unless the tool is approved for client-confidential, source check on every cited standard. Audit procedures: not allowed until a tool has an approval record, test results on firm samples, and reviewer instructions.

### Example C: Shadow AI discovery turns into an approved-tool catalog
- **Context:** A professional-services firm with a one-page AUP finds staff using free public tools for client emails and meeting notes (consistent with the pattern in KPMG-MELB-2025 and MSFT-WTI-2024, which are other organizations' samples, not this firm's data).
- **Moves:** Discovery poll (Move 1) and policy-awareness question (Move 3); catalog entries per tier; fast lane for internal-class data; request path with a stated response time; training with redaction examples (CPAI-ND); sample reviews quarterly.
- **What to measure (synthesis):** share of staff who can name the approved tool, request volume and turnaround, exceptions logged, incidents. Do not present survey percentages from other firms as the firm's baseline.

### Example D: Vendor adds an AI feature inside an existing SaaS platform
- **Context:** A document-management vendor announces an AI summarisation feature on by default.
- **Rules applied:** NIST-600-1-2024 GV-1.6-001 and -002: update procurement due diligence to cover embedded GAI and define inventory exemptions in policy; GV-6.1-004 and -006: contract clauses on usage rights, security and the right to evaluate; GV-6.1-007: inventory third parties with access to content. Retention and region questions per Moves 7 and 8.
- **Decision (synthesis):** Switch off by default for client-confidential matters until the feature has a catalog entry, the data terms are confirmed, and admin controls (retention, logging) are checked.

---

## 8. Mapping to steps

Thresholds below are either sourced (with ref) or marked "synthesis". Present synthesis items to users as defaults to adjust.

### Onboard
- **Checklist:** professional regimes bound (attest, tax-return preparation, legal, client-contract regimes); existing owners (privacy, security, risk, ethics, general counsel); existing policies (AUP, data classification, third-party risk); tools in use (survey or discovery).
- **Template fields (governance profile):** unit; regimes; data classes handled; tools in use (tool, tier, who pays); current approval path and time; incidents or near misses; sponsor.
- **Decision rule:** if the unit prepares tax returns, flag 7216 from day one; if it serves attest clients, flag independence; if it practises law, flag Rule 1.6 consent and fees (ECFR-7216-2008; JOFA-2026; ABA-512-2024).

### Frame
- **Checklist:** what is being governed and why: define "generative AI" and related terms, then tie use to professional obligations and confidentiality agreements (CPAI-ND); choose the framework backbone (NIST AI RMF, ISO/IEC 42001, internal) and mapping aids (CSA-AICM-2025).
- **Template sections (policy skeleton):** purpose and definitions; scope (people, tools, runtime classes); data classes and tool-tier matrix; approved-tool catalog and request path; risk tiers and review; records of AI use; client disclosure and consent; training and acknowledgement; incidents; exceptions; maintenance and review date.
- **Decision rule:** the policy must say who may approve a tool and who may grant an exception; unowned exceptions are the main bypass route (EY-AIGOV-2026, Move 23).

### Map
- **Checklist (per workflow step):** data classes in; destination (tool, tier, region, sub-processors); runtime class and permissions; human reviewer; output audience; regime flags (7216, independence, privilege, EU Annex III).
- **Template fields (AI inventory entry, from NIST-600-1-2024 GV-1.6-003 plus synthesis):** tool; vendor; product tier and contract; underlying model and version; access mode (personal assistant, shared team skills, workflow automation, background agent, managed agent runtime); data classes permitted; data provenance; known issues; human-oversight roles; IP and sensitive-data considerations; retention and log location; owner; risk tier; client-consent flag; 7216 flag; independence flag; EU high-risk screen; exit plan.
- **Decision rules:** inventory includes embedded features unless policy explicitly exempts them (GV-1.6-002); a workflow with tax return information that involves a substantive determination needs prior consent (ECFR-7216-2008, 301.7216-2(d)(1)).

### Diagnose
- **Checklist:** policy awareness; bypass behaviour; urgent-path behaviour; evidence of review on recent deliverables; vendor terms vs actual use; unauthorised agents.
- **Template (gap register):** gap; evidence; consequence; owner; fix type (policy, tool, training, control).
- **Decision rules:** ban plus no approved alternative = high-priority gap (KPMG-MELB-2025, p.75; synthesis); no record of who reviewed AI-assisted client work = gap (CPAI-ND).

### Reimagine (four lenses)
- **Improve the step:** lower the data class (redact, de-identify, summarise locally) so a lower tier suffices.
- **Automate the flow:** build controls into the approved tool (SSO, logging, retention, DLP) rather than relying on memory (GEND-2026, directional).
- **Delegate the outcome:** agents and automations need least privilege, approval for sensitive actions, logging, and inclusion in the inventory (OWASP-LLM-2025, excessive agency; EY-AIGOV-2026).
- **Reinvent the work:** if review moves, define what remains with the human (PCAOB-GENAI-2024, pp.4-5; ABA-512-2024 on full responsibility).
- **Decision rule (synthesis):** each lens raises the review tier by at least one level whenever autonomy or reach increases, until test evidence supports lowering it.

### Prioritize
- **Checklist:** fast-lane candidates (internal data, low consequence); need-consent candidates; need-independence-review candidates; EU Annex III candidates (HR, education).
- **Template (prioritisation columns):** value, data class, tier, approvals needed, time to approve, dependency (contract, tool, training).
- **Decision rules (synthesis):** pilot first those that need only internal-class data and an existing approved tool; defer those needing client consent or offshore processing until the consent text and processing location are settled.

### Make the case
- **Checklist:** cost of non-adoption (unsanctioned use continues: KPMG-MELB-2025; MSFT-WTI-2024); cost of an incident (SDNY-AVIANCA-2023; GUARDIAN-DELOITTE-2025 are public examples with stated consequences); cost of governance (roles, tooling, training).
- **Template sections:** risk exposure; what controls are proposed; residual risk; what leaders must approve (budget, owner, policy).
- **Decision rule:** do not quote another organization's survey percentage as the client's baseline; measure the client's own discovery results first.

### Plan
- **Checklist:** owner of catalog and request path; response-time commitment; re-approval triggers; exit plans; training and acknowledgement; review cadence; incident handling; records retention.
- **Template (approval record):** tool and tier; approved data classes; approved users; conditions (settings such as retention and feedback controls); test results; reviewer instructions; consent and disclosure requirements; review date; re-approval triggers; exit plan.
- **Sourced thresholds:** impact assessment update at least annually, on new uses and before new release stages (MSFT-RAI-2022, A1.3; a named company's own standard); EU high-risk deployer logs kept at least six months (AIACT-EXPL-2026, Art 26(6)); 7216 consent defaults to one year if no duration is stated (ECFR-7216-2008, 301.7216-3(b)(5)); IESBA technology revisions effective 15 December 2024 (IESBA-TECH-2023); EU Annex III high-risk application 2 December 2027, Annex I 2 August 2028 (EU-OMNIBUS-2026).
- **Decision rule (synthesis):** re-approve a tool on any of: underlying model change, sub-processor change, terms change, new data class, new use, or incident.

### Roll-up across units (unit to organization)
- **Checklist:** one catalog; one data-class and tier matrix; unit-level addenda for regimes (tax, attest, legal); one incident process; one inventory.
- **Template (roll-up table):** unit; tools; tiers; regimes; open gaps; exceptions granted; incidents; next review.
- **Decision rule (synthesis):** a unit may be stricter than the organization baseline, never looser; exceptions are logged at the organization level.

### Runtime-class notes (for the advisor to apply, synthesis)
- **Personal assistant:** main exposure is what the user pastes; the controls are data-class training, enterprise-tier accounts and retention settings.
- **Shared team skills:** reusable prompts and files; version them, own them, and re-test after model changes.
- **Workflow automation:** deterministic steps calling a model; log inputs and outputs per run; define the human check point.
- **Background agent:** acts without a person watching; least privilege, approval for sensitive actions, activity logs, kill switch, inventory entry.
- **Managed agent runtime:** a hosted environment running agents; assess as a platform (tenancy, logging, data location, change notices) and per agent.

---

## 9. Sources

Access: **full** = read the document or page text; **partial** = read an index page, summary or part of the document; **secondary** = read a third-party summary instead of the primary document; **search-only** = result snippets only. "Type" classes: standard/regulation, professional body, regulator/standard-setter, consultancy or research firm, academic, practitioner or vendor blog, vendor documentation, court record, news.

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| NIST-RMF-2023 | Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1 | NIST | standard/framework | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | January 2023 | full |
| NIST-600-1-2024 | AI RMF: Generative AI Profile, NIST AI 600-1 | NIST | standard/framework | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | July 2024 | full |
| AIACT-EXPL-2026 | EU AI Act Explorer: Articles 4, 14, 26, 27, 113 and Annex III (shows amended text) | artificialintelligenceact.eu (Future of Life Institute site) | regulation (annotated) | https://artificialintelligenceact.eu/article/26/ (and /article/4/, /article/14/, /article/27/, /article/113/, /annex/3/) | accessed 2026-10-20; page notes amendments | full |
| EU-OMNIBUS-2026 | Regulation (EU) 2026/1744 amending Regulation (EU) 2024/1689 (Digital Omnibus on AI) | European Parliament and Council (EUR-Lex) | regulation | https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng | 8 July 2026 (OJ publication date not confirmed by me) | full (via text mirror) |
| SIDLEY-2026 | EU Lawmakers Reach Provisional Agreement to Delay Key EU AI Act Obligations | Sidley Austin LLP | law-firm commentary | https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/ | 22 June 2026 | full (via text mirror) |
| ECFR-7216-2008 | 26 CFR 301.7216-1, -2, -3 (disclosure and use of tax return information; consent) | US Treasury / IRS via eCFR | regulation | https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?part=301&section=301.7216-3 (and -2, -1) | T.D. 9375 (Jan 7, 2008) as amended; current eCFR | full |
| PCAOB-GENAI-2024 | Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting | PCAOB staff | regulator staff publication | https://pcaobus.org/documents/generative-ai-spotlight.pdf | July 2024 | full |
| FRC-AI-2025 | FRC publishes landmark guidance providing clarity to audit profession on the uses of AI (news release) | Financial Reporting Council (UK) | regulator | https://www.frc.org.uk/news-and-events/news/2025/06/frc-publishes-landmark-guidance-providing-clarity-to-audit-profession-on-the-uses-of-ai/ | 26 June 2025 | partial (release read; guidance PDF and thematic review not read) |
| KN-2025 | Tech-driven, ethically bound: new FRC and ICAEW guidance on AI use in the accountancy sector | Kingsley Napley LLP | law-firm commentary | https://www.kingsleynapley.co.uk/our-insights/articles/tech-driven-ethically-bound-new-frc-and-icaew-guidance-on-ai-use-in-the-accountancy-sector/ | 24 July 2025 | full |
| JOFA-2026 | Accounting ethics in the age of AI (Kelly D. Mullins) | Journal of Accountancy (AICPA) | professional body | https://www.journalofaccountancy.com/news/2026/aug/accounting-ethics-in-the-age-of-ai.html | 5 August 2026 | full |
| JOFA-2023 | Generative AI and risks to CPA firms | Journal of Accountancy (AICPA); content from CNA risk control | professional body / insurer | https://www.journalofaccountancy.com/issues/2023/oct/generative-ai-and-risks-to-cpa-firms.html | October 2023 | full |
| CPAI-ND | Drafting an AI Policy that Actually Works | CPAi (CPA firm association) | professional association guide | https://www.cpai.com/Education-Resources/My-Firm/Data-Security-Risk-Management/Drafting-an-AI-Policy-that-Actually-Works | undated | full |
| IESBA-TECH-2023 | Final Pronouncement: Technology-related Revisions to the Code | IESBA | standard-setter | https://www.ethicsboard.org/publications/technology-related-revisions-code | 11 April 2023 (updated 30 May 2023); effective 15 Dec 2024 | partial (landing page; full text not read) |
| IAASB-TECH-2026 | Technology and the Future of Audit and Assurance | IAASB | standard-setter | https://www.ethicsboard.org/focus-areas/technology | undated; content refers to December 2025 decisions | full (page) |
| ABA-512-2024 | ABA Formal Opinion 512, Generative AI Tools (29 July 2024), read via summary | American Bar Association; summary by Ezel | professional body (secondary summary) | https://ezel.ai/ethics-opinions/aba/512-generative-ai-tools | 29 July 2024 | secondary (ABA PDF blocked; confirm quotes and consent wording against ABA text) |
| SDNY-AVIANCA-2023 | Mata v. Avianca, Inc., Opinion and Order on Sanctions, ECF 54 | US District Court, S.D.N.Y. | court record | https://www.courtlistener.com/docket/63107798/54/mata-v-avianca-inc/ | 22 June 2023 | full (via text mirror) |
| WINTHROP-2026 | You May Be a Return Preparer: Using AI Without Violating Sections 7216 and 6713 (panel abstract) | Winthrop & Weinstine; ABA Tax Section virtual fall meeting | practitioner talk abstract | https://winthrop.com/bold-perspectives/you-may-be-a-return-preparer-using-ai-without-violating-sections-7216-and-6713/ | panel dated 6 October 2026; I did not verify it took place | full (abstract only) |
| KPMG-MELB-2025 | Trust, attitudes and use of artificial intelligence: A global study 2025 | University of Melbourne with KPMG | academic with consultancy | https://kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf (landing: https://kpmg.com/xx/en/our-insights/ai-and-technology/trust-attitudes-and-use-of-ai.html) | 2025 (files dated May 2025) | full |
| EY-AIGOV-2026 | EY survey finds that autonomous AI implementation outpaces oversight, yielding an AI governance gap (press release on the EY AI Risk and Governance Survey) | Ernst & Young LLP (US) | consultancy survey | https://www.ey.com/en_us/newsroom/2026/09/ey-survey-finds-that-autonomous-ai-implementation-outpaces-oversight-yielding-an-ai-governance-gap | 15 September 2026 | full (release; underlying report not read) |
| MSFT-WTI-2024 | AI at Work Is Here. Now Comes the Hard Part (Work Trend Index) | Microsoft and LinkedIn | vendor research | https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part | 2024 | full (via text mirror) |
| IAPP-GOV-2025 | AI Governance Profession Report 2025 | IAPP (with Credo AI contributor) | professional association research | https://iapp.org/resources/article/ai-governance-profession-report/ | page timestamp 30 Oct 2025; survey spring 2024 | full (web summary) |
| HAI-INDEX-2025 | The 2025 AI Index Report, Responsible AI chapter | Stanford HAI | academic | https://hai.stanford.edu/ai-index/2025-ai-index-report/responsible-ai | 2025 | full (chapter highlights) |
| GUARDIAN-DELOITTE-2025 | Deloitte to pay money back to Albanese government after using AI in $440,000 report | The Guardian | news | https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report | 6 October 2025 | full (via text mirror) |
| RAJI-2020 | Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing (SMACTR) | Raji et al. (Partnership on AI, Google), FAT* 2020 | academic | https://arxiv.org/abs/2001.00973 | January 2020 | full |
| MIT-RISKREPO-2024 | The AI Risk Repository: A Comprehensive Meta-Review, Database, and Taxonomy of Risks From Artificial Intelligence | MIT FutureTech and collaborators | academic | https://arxiv.org/abs/2408.12622 | arXiv 2408.12622 (first posted August 2024; fetched version shows 1,725 risks) | partial (abstract and summary read) |
| CSIRO-RAI-2022 | Responsible AI Pattern Catalogue | CSIRO Data61 researchers | academic | https://arxiv.org/abs/2209.04963 | arXiv 2209.04963 (September 2022) | partial (abstract only read) |
| CSA-AICM-2025 | AI Controls Matrix (AICM) v1 | Cloud Security Alliance | industry body framework | https://cloudsecurityalliance.org/artifacts/ai-controls-matrix | v1 released 9 July 2025; updated 30 Oct 2025 | partial (landing page; spreadsheet not read) |
| OWASP-LLM-2025 | OWASP Top 10 for LLM Applications 2025 (listing page) | OWASP Gen AI Security Project | practitioner standard | https://genai.owasp.org/llm-top-10/ | 2025 | partial (index page only) |
| NCSC-SAI-ND | Guidelines for secure AI system development | UK NCSC (with partners) | regulator guidance | https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development | undated on fetched page | partial (executive summary only); not cited for any claim beyond existence |
| ICO-AI-ND | Artificial intelligence (guidance hub) | UK ICO | regulator guidance | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/ | undated | partial (hub page); not cited for any claim |
| OPENAI-ENT-ND | Enterprise privacy | OpenAI | vendor documentation | https://openai.com/enterprise-privacy/ | undated, fetched 2026-10-20 | full (via text mirror) |
| ANTHROPIC-PRIV-2026 | Is my data used for model training? (commercial products) | Anthropic | vendor documentation | https://privacy.anthropic.com/en/articles/7996868-is-my-data-used-for-model-training | page date 18 August 2026 | full (via text mirror) |
| MSFT-COPILOT-ND | Microsoft 365 Copilot privacy and data protection | Microsoft | vendor documentation | https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy | undated, fetched 2026-10-20 | full (via text mirror) |
| MSFT-RAI-2022 | Microsoft Responsible AI Standard, v2, General Requirements | Microsoft | named-company internal standard (public) | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf | June 2022 | full |
| FRB-SR117-2011 | SR 11-7 Supervisory Guidance on Model Risk Management | Federal Reserve and OCC | regulator | https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf | 4 April 2011 | full |
| LAWSOC-GENAI-2026 | Generative AI: the essentials | Law Society of England and Wales | professional body | https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials | undated; page links to material from April 2026 | full (via text mirror) |
| PWC-RAI-ND | How Responsible AI can improve business and preserve value | PwC | consultancy marketing page | https://www.pwc.com/gx/en/issues/data-and-analytics/artificial-intelligence/what-is-responsible-ai.html | undated | partial (marketing page; no policy detail) |
| DELOITTE-TAI-ND | Trustworthy and Ethical AI Thought Leadership | Deloitte | consultancy page | https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/articles/trustworthy-ethical-ai-thought-leadership.html | undated | partial (names a framework with seven dimensions) |
| KPMG-TAI-ND | KPMG Trusted AI framework | KPMG Australia | consultancy page | https://kpmg.com/au/en/services/ai-services/trusted-ai-framework.html | undated | partial (marketing page; ten pillars not read from this fetch) |
| GEND-2026 | Shadow AI security playbook for CIOs and CTOs (2026) | Gend (vendor blog) | practitioner/vendor blog | https://www.gend.co/blog/shadow-ai-security-playbook | 8 January 2026 | full; directional only |
| AMPCUS-2026 | Shadow AI in 2027: A Governance Checklist for Security Leaders | Ampcus Cyber (vendor blog) | practitioner/vendor blog | https://www.ampcuscyber.com/blogs/shadow-ai-governance-checklist-for-security-leaders/ | 16 October 2026 | full; directional only; secondary for IBM figure |
| OPENLAYER-2026 | ISO 42001: A Complete Guide to AI Management Systems | Openlayer (vendor blog) | practitioner/vendor blog | https://www.openlayer.com/blog/iso-42001-ai-management-systems-guide.md | 17 June 2026 | full; secondary for ISO content |

Not cited and not counted: pages that returned only error or consent screens (ISO.org standard page, ABA PDF, McKinsey State of AI, AICPA AI landing page, FRC guidance PDF, PCAOB original URL, Singapore MGF page, ICAEW AI hub).

Source count: 42 distinct sources listed; 40 are cited for claims (NCSC-SAI-ND and ICO-AI-ND are index-page reads cited for no claim). About 29 were read in full; 13 were partial or secondary (marked in the Access column). By type: standards, frameworks and regulation 9 (NIST-RMF, NIST-600-1, AIACT-EXPL, EU-OMNIBUS, ECFR-7216, CSA-AICM, OWASP-LLM, MSFT-RAI, FRB-SR117); regulator, standard-setter or court 7 (PCAOB, FRC, IESBA, IAASB, SDNY-AVIANCA, NCSC, ICO); professional body or association 6 (JOFA-2026, JOFA-2023, CPAI, ABA-512 via summary, LAWSOC, IAPP); consultancy, research-firm or industry survey 6 (KPMG-MELB, EY, MSFT-WTI, PWC, DELOITTE, KPMG-TAI); academic 4 (RAJI, MIT-RISKREPO, CSIRO-RAI, HAI-INDEX); law-firm commentary or talk abstract 3 (SIDLEY, KN, WINTHROP); vendor documentation 3 (OPENAI, ANTHROPIC, MSFT-COPILOT); vendor or practitioner blogs 3 (GEND, AMPCUS, OPENLAYER); news 1 (GUARDIAN-DELOITTE).

---

## 10. Gaps

- **Primary AICPA text not reached.** The AICPA AI landing page returned "page not found". I relied on the Journal of Accountancy (AICPA publication) for ET 1.700.001 and independence points. I did not read the AICPA Code, SQMS No. 1 or any AICPA AI practice aid. The JofA 2026 article points to an AICPA ethics staff article "AI Through an Ethics Lens" that I did not read.
- **No AI-specific IRS guidance found.** A rationed search surfaced commentary saying no IRS guidance addresses generative AI and section 7216, and mentioning a reported 2026 IRS Office of Professional Responsibility alert; I could not verify either at IRS sources. Section 7216 and 6713 penalty amounts also came only from search snippets, so I left them out of section 6. Whether an AI vendor counts as a "tax return preparer" or auxiliary-service provider is unresolved in my sources (Move 10).
- **ABA Opinion 512 read through a secondary summary.** The ABA PDF was blocked. Quotations and consent detail should be confirmed against the ABA text. State bar rules and opinions vary and were not covered.
- **ISO/IEC 42001 text is paywalled.** Secondary sources disagree on the Annex A control count (38 in several, 39 in others); I did not state a count. Certification process and duration details came from search snippets and a vendor blog and are not used as sourced facts above.
- **FRC guidance and thematic review not read.** I read only the news release (and a law-firm summary). Statements that most of the six largest firms had certification processes and some lacked documented policies came from a search snippet and are not used.
- **IESBA full text and ICAEW Code revisions not read.** Only the IESBA landing page and a law-firm note on ICAEW's 1 July 2025 revisions.
- **EU Digital Omnibus.** I read the regulation's text mirror (dated 8 July 2026) and the Parliament/Council status through Sidley (22 June 2026). The Official Journal publication and entry-into-force dates came from a search result and were not confirmed on the text I read; the Council press page was blocked. The AI Act explorer shows amended text. Check EUR-Lex before advising on dates. Article 50 transparency, Article 5 prohibitions and GPAI obligations for deployers were not covered.
- **No firm's actual acceptable-use policy text found.** Big Four pages (PwC, Deloitte, KPMG) describe responsible-AI frameworks at marketing level; EY's page gave survey results. Named-firm internal AI policies for professional services were not publicly available in what I could reach. The PCAOB staff report describes firm practices anonymously.
- **No independent measurement of review effectiveness.** I found no override rates, parallel-run results, inspection findings on AI use, or error rates for AI-assisted professional work. The incident evidence is two public cases (court sanctions; a consultancy partial refund), which show failure modes, not frequency.
- **Vendor contract term prevalence unknown.** I found no benchmark of what terms firms actually negotiate on sub-processor notice, model-change notice, indemnities or exit. The vendor documents reflect published terms for particular products and may differ from negotiated contracts and change over time.
- **SOC 2 and ISO scope.** I did not read AICPA SOC 2 criteria or any vendor's actual report; OpenAI's page says products completed SOC 2 audits (Type 2 for specified products), which is a vendor statement.
- **Surveys.** The IAPP report date is uncertain (survey spring 2024; page timestamp October 2025). EY's underlying report was not read. McKinsey's State of AI, Gartner and IBM figures were not read at source. Microsoft's Work Trend Index publication date was not reliable in my fetch.
- **Other regimes not covered:** GDPR Article 28 and DPIA detail beyond a hub page, US state AI laws, SEC and FINRA expectations for AI in regulated firms, HIPAA, cyber-insurance requirements, and client-side AI clauses in outside-counsel guidelines.
- **Source mix.** Several practitioner items are vendor blogs and the CPA-firm policy guide is associated with an insurer (CNA content through JofA 2023); treat them as directional practice advice, not requirements.

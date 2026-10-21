# Acceptance and independence (assurance)

Last reviewed 2026-10-17. Use cases live in `../use-cases/acceptance-independence.yaml` (21 entries). Ids are shortened
here: `#05` means `assurance-acceptance-independence-05`. Source keys in brackets are listed in §10 and given in full
in the YAML. **Read this first:** no source anywhere reports a measured result (time, accuracy, false positives,
overrides, missed conflicts) for AI used in acceptance, KYC or independence work. Only one in-use AI tool is named
(`#01`, vendor-published). The one named figure (`#21`, a 14% audit-fee cut argued from AI) is a fee change, not a
measure of AI performance. The stronger evidence is about structural change around firms. Use this module mainly
for risk awareness and interview probes, and say plainly when a client asks for proof that does not exist.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

Deciding whether to take on or keep a client and an engagement (acceptance and continuance), and proving the firm is
independent of it: conflicts checks, client "family trees" (the client's affiliates), personal financial interests,
non-audit service approval, partner rotation, KYC/AML customer due diligence, engagement letters. It runs in two
directions. **Direction 1:** AI and automation inside these checks (thin, almost all vendor-described). **Direction 2:**
AI-related structural change that creates new acceptance and independence questions: private-equity (PE) ownership,
alternative practice structures (APS: the attest firm stays CPA-owned, other services sit in an investor-backed entity
linked by an administrative services agreement), firm-wide alliances with AI developers, AI services sold to audit
clients, AI-native audit firms. Regulators are active on direction 2 and nearly silent on direction 1.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Intake and client risk profiling | Questionnaires, risk scoring, data pulls from internal and third-party sources | client-interaction, research-synthesis | Spreadsheet-and-email workflows; 93% of 15 surveyed compliance professionals and managing partners still collect onboarding data by email (vendor survey) |
| KYC / AML due diligence | Identity, beneficial ownership, sanctions and PEP (politically exposed person) screening, ongoing monitoring | transaction-processing, review-assurance | False-positive screening hits; over-collection of documents; tools that screen but do not verify identity (ICAEW) |
| Conflicts and independence clearance | Map the client's affiliates; check restricted lists, business relationships, services | review-assurance, data-reporting | Family-tree data built by hand; 11 IFIAR findings in 2025 on unreliable tracking systems |
| Acceptance decision and escalation | Partner and risk approval; panels and consultations for high-risk or public-interest cases | expert-judgment | Grey areas in ownership structures; 25 network firms (18%) had an acceptance finding in IFIAR's 2025 survey |
| Non-audit service approval | Pre-approval workflow against an entity database | review-assurance | AI build, host, licence and assurance services have no settled classification |
| Personal independence monitoring | Staff holdings, proscribed-security alerts, confirmations, breach handling | data-reporting | 22 IFIAR findings in 2025 on failing to monitor personal independence |
| Partner rotation | Plan successors within rotation limits | coordination-scheduling | Balancing experience and availability against rule limits |
| Engagement letters and terms | Agree terms; now also AI use and data consent | document-production | Whether to disclose AI use is newly unclear; 26% of 54 US firms automate letters |
| Continuance | Re-assess and roll forward each year | review-assurance, expert-judgment | Point-in-time checks surface issues late |
| Firm-structure independence | Network-firm mapping, investor screening, vendor and alliance review | expert-judgment | Rules still in draft; no rule on AI tool vendors |

Baseline systems are mostly not AI: EY UK's Global Independence and Global Monitoring Systems [EY-TR-2025], Deloitte's
global entity database and pre-approval workflow [DELOITTE-IE-TR-2026], KPMG Australia's mandatory conflicts and
independence checking system [KPMG-AUTR-2025]. Deloitte UK plans a global acceptance and continuance platform for UK
implementation in FY2027, with no mention of AI [DELOITTE-UKTR-2025].

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path),
delegate (an agent owns an outcome), reinvent (the service or operating model changes). **Automate has no evidence;
delegate has one unproven case (`#20`).** Entries `#10`-`#17` are human control steps created by AI-related change;
the AI belongs to the client, a vendor or the firm's owners.

**Direction 1: AI and automation inside the checks (thin; all grade B or C)**
- Improve: `#01` Crete Professionals Alliance clears conflicts and independence across member firms with Intapp's
  AI risk scoring; compliance reviews high-risk results (the only named in-use AI case; no figures). `#02` risk-scored
  acceptance workflows with AI request summaries (Intapp, Kingland; no named customer). `#03` Grant Thornton UK
  selected an AI-powered platform joining KYC, due diligence and acceptance ("thousands of hours", vendor release;
  go-live not stated). `#04` AI document classification and sanctions/PEP hit triage (vendor prototype in early client
  trials, not audit-specific); the UK AML strategy says government will support AI and digital ID in due diligence. `#05` AI extraction of ownership structures into family trees.
- Improve (automation, AI mostly not stated): `#06` independence dashboards, breach workflow, holdings checked within
  24 hours of a trade (the vendor names AI only for reading broker statements); `#07` rotation candidate matching; `#08` engagement-letter automation; `#09` pricing and targeting
  from acceptance data (vendor revenue estimates).

**New acceptance inputs created by AI (ideas from guidance; grade D)**
- Improve: `#10` assess how heavily a client relies on AI in reporting, and whether the team can audit it (AICPA
  practice aid, 13 Oct 2026). `#11` engagement terms on the firm's AI use and client-data consent. `#12`
  audit-committee questions on the independence implications of the auditor's AI use (SEC chief accountant).

**Direction 2: structural change that creates independence and acceptance risk**
- Improve (new controls, ideas): `#13` independence review of AI tool-vendor contracts and licences; `#14` clearing
  firm-wide AI alliances before accepting AI developers, or companies that depend on them, as clients; `#15` a
  permissibility gate for AI services (build, host, license, assure) offered to audit clients.
- Reinvent (grade B, control steps in named firms): `#16` independence due diligence before taking PE money (Grant
  Thornton UK's Cinven structure); `#17` screening clients against the investor group and consulting the regulator
  (Grant Thornton UK declined one "grey area" client after consulting the FRC).
- Reinvent (grade B): `#21` KPMG International pressed its auditor, Grant Thornton UK, to pass on AI savings; its
  audit fee fell 14% (FT report; the AI argument rests on unnamed sources).
- Reinvent (grade C): `#18` Grant Thornton US's gtap AI platform inside an APS, and who supplies shared platforms;
  `#19` Modus ($85M) invests in audit firms and deploys AI workflows; `#20` AI-native audit firms (Repodo, Oath
  Verified); in the US, venture capital sits outside the attest entity.

## 4. Interview probes

Ask in the person's setting: firm risk or independence function, engagement partner, ethics leader, or a firm
considering outside capital. Expect most answers on AI performance to be "we don't measure that"; note who knows.

1. **"Walk me through your last escalated acceptance decision. Which data came from which system, what is still a
   spreadsheet, where does automation or AI touch it, and how would you know it missed a conflict?"** Reveals the
   baseline and whether `#01`-`#03` are real or aspirational; almost no firm can answer the last part.
2. **"For each tool in KYC and independence checks: what does it actually do (verify identity, or screen sanctions,
   PEPs and adverse media)? What are the false-positive and override rates, and who reviews suitability?"** Reveals
   whether the firm understands its tools (ICAEW's main reviewer finding) and whether any quality data exists (`#04`).
3. **"How complete is your client family-tree data, and who validates it?"** Reveals readiness for any AI layer;
   IFIAR still finds unreliable tracking systems (`#05`, `#06`).
4. **"What do you ask clients about their own AI use at acceptance and continuance? Has an answer ever changed a
   decision, the fee or the team? Has an engagement been deferred because evidence could not be obtained?"** Reveals
   whether the AICPA practice aid's new acceptance factor has reached the procedure (`#10`).
5. **"What does your engagement letter say about AI use and client-data consent, and what drove that: state law, a
   client request, firm policy? Have clients refused AI?"** Reveals disclosure risk (`#11`).
6. **"Which AI vendors, platforms or affiliates supply tools you use on audits or sell to audit clients? Who reviews
   each relationship for control, fees, referrals and evidence access before adoption?"** Reveals the biggest
   unowned risk: no rule covers it and no firm describes a process (`#13`).
7. **"How does the firm decide an AI alliance or co-developed client product is clear of independence rules, at
   network level, and has any acceptance or continuance decision changed because of one?"** Reveals monitoring the SEC's
   chief accountant calls "top of mind" (`#14`).
8. **"Do you build, host, license or assure AI for clients you also audit? What test runs before you accept, and
   who in the independence team understands AI services well enough to classify them?"** Reveals self-review and
   management-responsibility risk (`#15`).
9. **"If you are PE-backed, in an APS or considering it: how does acceptance find overlaps with the investor, its
   funds and portfolio companies, and what data must you get from the investor?"** Reveals the screening gap the
   AICPA draft creates (`#16`, `#17`).
10. **"In your structure, who has final say on accepting or keeping a client, and which technology does the
    non-attest entity supply to the audit practice under the services agreement?"** Reveals governance dilution
    (IFAC's concern) and shared-platform independence questions (`#16`, `#18`).
11. **"Have clients asked for lower fees because you use AI? How do you respond, and does it touch fee-dependence
    or quality?"** Reveals business-model pressure (`#21`).

## 5. Metrics and benchmarks

**What is measured: the problem, not the tools**
- IFIAR 2025 survey (44 regulators; 161 member firms of six global networks; per-theme denominators not given): at
  least one independence and ethics finding at 43 firms (30%); acceptance and continuance at 25 firms (18%; 16-18%
  each year 2021-2024); 11 findings on unreliable tracking of relationships, interests and family trees; 22 on failing to
  monitor personal independence [IFIAR-SURVEY-2026]. Not about AI.
- Deloitte UK took 32 matters to its Public Interest Review Group in FY2025 (38 in FY2024); 9% led to work declined
  (19% in FY2024). Not AI-specific [DELOITTE-UKTR-2025].
- 26% of 54 US firms have an automated engagement-letter solution; AI not specified [CPACOM-ATR-2025].
- KPMG International's audit fee fell 14% ($416,000 to $357,000, 2024 to 2025) after it argued AI should cut the
  work; the fee comes from a filing and the AI argument from unnamed sources [IRISHTIMES-KPMG-2026].

**Vendor figures (grade C; no named, measured case behind them)**: Fenergo "thousands of hours" for Grant Thornton UK,
no baseline [FENERGO-GT-2026]; Intapp "potential revenue impact" 1.5-4% from informed pricing, 1-3% from targeting
(a 2018 white paper) [INTAPP-WP-2018]; Kingland checks new holdings within 24 hours of a trade (automation) [KINGLAND-PA-2026]; Zygos: 93%
and 87% of 15 respondents report email intake and incomplete submissions [ZYGOS-AISENSE-2026].

**Structural scale (independent counts; definitions differ)**
- IFAC: more than 1,000 accountancy firms with PE investment in a decade [IFAC-PE-2026]; 46 firms auditing
  public-interest entities (PIEs) owned directly by PE, with 52 more PIE audit firms rolled up into them [IFAC-AQ-2026].
- Accountancy Europe: 385 transactions in 2025, 139 involving audit firms; 15% involve firms with PIE audits; the Dutch
  AFM reports about 30% of Dutch audit firms have PE investment [AE-PE-2026].
- PCAOB: more than 90 significant PE-related deals and mergers since 2020, over half in 2025 [AT-PCAOBPE-2025]; CPA
  Trendlines, cited in a JofA academic update, counts more than 53 from 2020 to mid-2025 [JOFA-FACULTY-2025].
- About half of the 30 largest US firms took outside capital over five years (Bloomberg Tax) [BBL-PCAOBSTRAT-2026].
- AI alliance scale: Claude for 470,000 Deloitte people and 276,000+ KPMG staff [ANTHROPIC-DELOITTE-2025, ANTHROPIC-KPMG-2026].
- 81 comment letters on the AICPA APS draft, none from a technology company (per a commenter) [AT-PEEC-2026].

**Attitudes**: 61% of 1,178 ACCA respondents named AI use among their top ethical challenges (32% in 2024)
[ACCA-ETHICS-2026]. 79% of 257 UK stakeholders are satisfied with how audit firms deploy AI; over-reliance on AI is
the biggest concern [ICAS-ATI-2026].

**What to measure (recommend; nobody publishes these yet)**: false-positive and override rates for screening and
conflict tools; conflicts or independence breaches found after acceptance (a missed-conflict proxy); intake-to-letter
cycle time; share of acceptances escalated; family-tree completeness; coverage of the AI vendor and alliance register.
Caution: a PCAOB inspection report says the number of firm-identified independence instances may reflect monitoring
design, and cautions against comparing firms on it [PCAOB-BOULAY-2026].

## 6. Guardrails

**No regulator prohibits AI in acceptance, KYC or independence work, and none has AI-specific rules for it.** The FRC's
generative and agentic AI guidance does not mention acceptance or independence [FRC-GENAI-2026].

- **AICPA practice aid (Oct 2026; nonauthoritative) [AICPA-AIPAID-2026].** Client AI reliance is an acceptance and
  continuance factor: engagement nature, management integrity and skills, team competence, whether evidence can be
  gathered. AU-C 210 does not require naming AI tools in the engagement letter; state law, contracts or firm policy
  may [AT-AICPAPA-2026, CFODIVE-AICPAPA-2026]. The download is reserved for AICPA members; these positions come from
  press accounts.
- **AICPA ethics.** Developing or hosting an AI system for an attest client can raise independence concerns under
  existing non-attest rules; check consent before client data enters an AI tool [JOFA-ETHAI-2026]. Tool-provider
  contract terms that shift control, judgment, fees or evidence access can create threats; if safeguards fail,
  decline or end the arrangement. Written for SOC 2; "may" apply to other attest work [JOFA-SOCETH-2026].
- **AICPA APS project (PEEC).** Exposure draft Dec 2025 (comments closed 30 Apr 2026): significant influence versus
  control, wider network-firm definition, upstream-entity prohibition [AICPA-APSED-2025, JOFA-PEED-2025]. Second
  exposure draft and a ban on attest-client investment in firms under discussion; PEEC agreed to continue at an
  interim October meeting, scheduled for 19 Oct 2026 [JOFA-PEEC-2026, AICPA-PEECMEET-2026]. Where the Code is silent, apply the conceptual framework [JOFA-NILSEN-2025].
- **IESBA.** Technology revisions (audits of periods from 15 Dec 2024) cover automation bias, confidentiality,
  self-review, management responsibility and commercial dependency in technology services [IESBA-TECHREV-2023,
  IESBA-SNAPSHOT-2026]. Staff publication (15 Jul 2026): vendor updates and model drift are new information requiring
  re-evaluation [IESBA-NAM-2026]. AI-specific publication planned Q4 2026 [IESBA-SNAPSHOT-2026]; PE workstream
  terms of reference approved June 2026 [IESBA-HIGHLIGHTS-2026]. For sustainability assurance clients, the IESSA (periods
  from 15 Dec 2026) treats implementing sustainability reporting software as a self-review threat where it affects the
  client's records or controls (5606.4 A3), bars IT systems services that might create one for public-interest clients
  (R5606.6), and makes designing or implementing software to collect or produce sustainability data a management
  responsibility (5400.20 A3). This applies to firms selling AI reporting tools to clients they assure (`#15`) [IESBA-IESSA-2025].
- **SEC and PCAOB.** Rule 2-01 bars financial information system design and implementation unless the results
  will not be subject to audit procedures [SEC-REGSX-2-01]. The chief accountant says independence rules must stay
  fit for purpose as AI enters audit delivery, AI partnerships complicate them, and nothing is planned to loosen
  them [KPMG-HOHL-2026, STARLING-HOHL-2026, TR-HOHL-2026]. PCAOB: independence on the standard-setting agenda [JOFA-PCAOBAG-2026];
  inspectors will look at firms with PE or APS changes and at AI [AT-PCAOBPE-2025].
- **UK.** The FRC is not against private capital in principle but wants control rules met in substance and form,
  and early engagement [FRC-PCLETTER-2024]; a PE-owned audit firm may not audit the fund or its portfolio companies
  [ICAEW-PE-2024]. AML: AI tools do not shift responsibility; Companies House checks cannot be relied on
  [ICAEW-AML-2026]; the 2026-2029 strategy encourages responsible AI in due diligence [UKGOV-AMLSTRAT-2026].

**Steps that stay with a person**: the acceptance and continuance decision; judging management integrity and the
client's AI reliance; clearing grey-area relationships and consulting the regulator; classifying AI services and
vendor relationships under the conceptual framework; suspicious activity reports (the MLRO); engagement-letter
wording and consent; sign-off on any AI-scored or AI-extracted result.

## 7. Roles and how they evolve

- **Compliance and conflicts teams** move from searching and clearing to reviewing high-risk results (Crete PA,
  vendor-published) [INTAPP-CRETE-2024]; Intapp says its tools free partners' time on routine tasks [INTAPP-INTAKE-2026,
  INTAPP-WP-2018].
- **Independence and ethics leaders** gain new work: vendor contracts, alliances, AI service classification and
  transaction structuring; Accountancy Europe says firms need legal, governance and transaction support
  [AE-BEYONDPE-2025]. No source describes how this work is staffed.
- **Engagement teams** need a blend of audit, AI, data and specialist skills to judge client AI reliance [AICPA-PA-2026].
- **AML**: ICAEW says responsibility should be embedded across the firm; the MLRO need not be an accountant
  [ICAEW-AML-2026].
- **Audit partners in PE-backed firms** may lose influence over client selection (IFAC) [IFAC-AQ-2026]; the PCAOB
  warns profit pressure could cut staffing and specialists [AT-PCAOBPE-2025].
- **New roles and juniors**: Oath hires "accountant engineers" [AT-PEEC-2026]; much automatable work is junior work
  [FINSTORY-OATH-2026]. Grant Thornton UK says it is increasing graduate hiring [IRISHTIMES-GT-2026].

## 8. Frontier

- **2025-10-06 / 2026-05-19** Deloitte and KPMG announce firm-wide Claude alliances [ANTHROPIC-DELOITTE-2025, ANTHROPIC-KPMG-2026].
- **2025-12-09** PCAOB acting chair and inspections director flag PE and AI as areas inspectors will focus on [AT-PCAOBPE-2025].
- **2025-12** AICPA APS exposure draft issued; comments closed 30 Apr 2026 [AICPA-APSED-2025].
- **2025-12** SEC chief accountant tells the WSJ that AI partnerships and PE complicate independence (reported
  2025-12-12; summarised 2026-01-22) [NYSSCPA-HOHL-2025, STARLING-HOHL-2026].
- **2026-03-02** IFAC publishes global PE research [IFAC-PE-2026]. **2026-03-03/04** Grant Thornton UK selects an AI
  onboarding and acceptance platform [FENERGO-GT-2026, GT-FENERGO-2026].
- **2026-03-27** IESBA starts gathering information on APS [JOFA-IESBAAPS-2026]. **2026-04-08** Modus raises $85M [AT-MODUS-2026].
- **2026-05-07** Grant Thornton US launches gtap inside an APS [GT-GTAP-2026]. **2026-05-08** KU/Deloitte symposium
  pairs an ownership-and-independence panel with AI sessions [KU-SYMPOSIUM-2026].
- **2026-06-05** SEC "in listening mode" on PE and AI; independence FAQ refresh first [TR-HOHL-2026].
- **2026-07-15** IESBA emerging-technologies staff publication [IESBA-NAM-2026].
- **2026-08-12/14** Press reports (one linking to an FT article that could not be opened) say AI alliances leave EY
  as Anthropic's likely auditor; unconfirmed [CRYPTOBRIEFING-ANTHROPICEY-2026, FOURTHWEB-ANTHROPICEY-2026].
- **2026-08-27 / 08-31** Repodo raises EUR 8.2M to launch an AI-native Danish audit firm; Oath's Christina Ho says
  AI tool licensing remains ambiguous under the revised APS draft [CFI-REPODO-2026, AT-PEEC-2026].
- **2026-09-15** UK AML strategy: AI and digital ID in due diligence; FCA AI practice examples due 2026-27 [UKGOV-AMLSTRAT-2026].
- **2026-09-22** Grant Thornton UK describes declining a grey-area client after consulting the FRC [IRISHTIMES-GT-2026].
- **2026-10-01** PCAOB agenda includes an auditor-independence standard-setting project [JOFA-PCAOBAG-2026].
- **2026-10-13** AICPA practice aid adds client AI reliance to acceptance; more sections promised [AICPA-PA-2026].
- **2026-10-19** PEEC interim meeting scheduled to continue discussing a second APS exposure draft [JOFA-PEEC-2026, AICPA-PEECMEET-2026].
- **2026-Q4** IESBA AI-specific guidance planned [IESBA-SNAPSHOT-2026]. **2026-12-15** revised AICPA "attest engagement
  team" definition takes effect [JOFA-PEECTEAM-2026].

## 9. Common objections

- **"Show me the AI conflicts tool that works."** There is none with published results; the one named user (`#01`)
  published no figures. Run it in parallel with the current process, and track overrides and conflicts found later.
- **"AI screening means we can trust the KYC result."** ICAEW says technology supports, not replaces, judgment, and
  many tools screen sanctions and PEPs rather than verify identity (`#04`). Know what the tool does.
- **"Our AI vendor is just software; independence doesn't come into it."** Unsettled. AICPA ethics staff flag
  contract terms that shift control, fees or evidence access; a former PCAOB board member calls AI tool licensing
  ambiguous; IESBA says vendor updates need re-evaluation (`#13`). Inventory vendors and document the analysis.
- **"Alliances are a procurement matter."** The SEC's chief accountant calls AI partnerships a complication and
  monitoring "top of mind"; press reports, unconfirmed, say alliances limit who can audit an AI developer (`#14`).
- **"We don't need to tell clients we use AI."** AU-C 210 does not require it, but some state laws do, consent may
  be needed for client data, and some clients refuse AI (`#11`).
- **"PE capital will fund our AI and lift quality."** The FRC is open in principle and the PCAOB says PE can fund AI,
  but PCAOB inspectors are looking at PE-backed firms, the FRC wants early engagement and IFAC flags governance
  dilution. Map investor holdings first
  and consult early, as Grant Thornton UK did (`#16`, `#17`).
- **"Regulators will loosen independence for the AI era."** The SEC chief accountant denies plans to loosen the rules;
  PEEC's draft would widen the network-firm definition and add an upstream-entity prohibition (`#16`).
- **"AI should cut our audit fee."** KPMG International reportedly argued this to its own auditor and its fee fell
  14%; Grant Thornton says fees reflect the cost of people and technology, an analyst warns of integrity
  trade-offs, and the PCAOB's acting chair links profit pressure to aggressive fee talks (`#21`).

## 10. Sources

Full details (title, publisher, type, URL, date, locator) are in the YAML.
- **Regulators and standard-setters:** IFIAR-SURVEY-2026, PCAOB-BOULAY-2026, SEC-REGSX-2-01, FRC-PCLETTER-2024, FRC-GENAI-2026,
  UKGOV-AMLSTRAT-2026, IRBA-AI-2023, AICPA-PA-2026, AICPA-APSED-2025, AICPA-APSCL-2026, IESBA-SNAPSHOT-2026, IESBA-NAM-2026,
  IESBA-APESB-2023, IESBA-TECHREV-2023, IESBA-EEA-2026, APESB-PE-2025, AICPA-AIPAID-2026, IESBA-IESSA-2025.
- **Professional bodies:** JOFA-ETHAI-2026, JOFA-SOCETH-2026, JOFA-NILSEN-2025, JOFA-PE-2025, JOFA-PEED-2025,
  JOFA-PEEC-2026, JOFA-AIPA-2026, ICAEW-PE-2024, ICAEW-AML-2026, ICAS-IESBASNAP-2026, IFAC-AQ-2026, AE-PE-2026, AE-BEYONDPE-2025.
- **Firms:** EY-TR-2025, DELOITTE-UKTR-2025, DELOITTE-IE-TR-2026, DELOITTE-LU-TR-2026, KPMG-AUTR-2025, KPMG-HOHL-2026,
  GT-FENERGO-2026, GT-GTAP-2026, OATH-2026.
- **Vendors:** INTAPP-CRETE-2024, INTAPP-CONFLICTS-2026, INTAPP-INTAKE-2026, INTAPP-EMPCOMP-2026, INTAPP-WP-2018,
  KINGLAND-ACCEPT, KINGLAND-PA-2026, KINGLAND-WP-2024, FENERGO-GT-2026, ZYGOS-AISENSE-2026, ANTHROPIC-DELOITTE-2025, ANTHROPIC-KPMG-2026.
- **Press, community, academic, surveys:** AT-AICPAPA-2026, CFODIVE-AICPAPA-2026, AT-PEEC-2026, AT-PCAOBPE-2025,
  AT-MODUS-2026, CONS-GT, CFI-REPODO-2026, FINSTORY-OATH-2026, IRISHTIMES-GT-2026, TR-HOHL-2026, STARLING-HOHL-2026,
  NYSSCPA-HOHL-2025, IRISHTIMES-KPMG-2026, CPAPA-EY, ACCWEEKLY-INDEP-2026, VERDANTIX, TLT-AML-2026, CRYPTOBRIEFING-ANTHROPICEY-2026,
  FOURTHWEB-ANTHROPICEY-2026, BIG4NEWS-2026, CEBI-2024, JB-JAR-2004, CPACOM-ATR-2025, ICAS-ATI-2026.
- **Not in the YAML:** FRC-GENAI-2026 (FRC, *Generative and Agentic AI Guidance: risks, mitigations and illustrative examples*, 2026-03-30, https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf);
  IFAC-PE-2026 (IFAC, *Private Equity Investment in Accountancy*, 2026-03-02, https://www.ifac.org/news-events/2026-03/private-equity-investment-accountancy-ifac-releases-research-and-online-resource);
  JOFA-FACULTY-2025 (JofA, *What faculty should know about private equity in accounting*, 2025-09-08, https://www.journalofaccountancy.com/newsletters/academic-update/what-faculty-should-know-about-private-equity-in-accounting);
  BBL-PCAOBSTRAT-2026 (Bloomberg Tax, *Audit Oversight Board Set for Renewed Industry-Friendly Strategy*, 2026-01-16, https://news.bloombergtax.com/financial-accounting/audit-oversight-board-set-for-renewed-industry-friendly-strategy);
  ACCA-ETHICS-2026 (ACCA, *Navigating ethics for trust*, 2026-10, https://www.accaglobal.com/content/dam/gb/policy-and-insights/reports/2026/navigating-ethics-trust.pdf);
  AICPA-PEECMEET-2026 (AICPA, *PEEC Meeting Materials and Information*, 2026-09-25, https://www.aicpa-cima.com/resources/article/peec-meeting-information);
  JOFA-PCAOBAG-2026 (JofA, *PCAOB shares agendas for rulemaking, research*, 2026-10-01, https://www.journalofaccountancy.com/news/2026/oct/pcaob-shares-agenda-for-rulemaking-research/);
  JOFA-IESBAAPS-2026 (JofA, *IESBA to assess need for standards on alternative practice structures*, 2026-03-27, https://www.journalofaccountancy.com/news/2026/mar/iesba-to-assess-need-for-standards-on-alternative-practice-structures/);
  IESBA-HIGHLIGHTS-2026 (IESBA, *June 2026 Meeting Highlights*, 2026-07, https://www.ethicsboard.org/_flysystem/azure-private/2026-07/June%202026%20IESBA%20Meeting%20Highlights.pdf);
  JOFA-PEECTEAM-2026 (JofA, *PEEC adopts revised definition of 'attest engagement team'*, 2026-08-17, https://www.journalofaccountancy.com/news/2026/aug/peec-adopts-revised-definition-of-attest-engagement-team/);
  KU-SYMPOSIUM-2026 (University of Kansas, *Deloitte/KU Auditing Symposium agenda*, 2026-05-08, https://business.ku.edu/research-and-faculty/accounting/deloitte-ku-auditing-symposium).

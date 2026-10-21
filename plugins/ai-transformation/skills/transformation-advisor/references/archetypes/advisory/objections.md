# Advisory objections

Last researched 2026-10-21. Use this when a practitioner pushes back. Each response gives the evidence and its
provenance; concede what is true. Objections about a single step (for example "AI gets add-backs wrong") are in the
module files' "Common objections" sections. Source keys in brackets resolve in [sources.md](sources.md).

## Contents

1. [Independence and professional duties](#1-independence-and-professional-duties)
2. [Quality and reliability](#2-quality-and-reliability)
3. [Economics and pricing](#3-economics-and-pricing)
4. [Competitors and clients](#4-competitors-and-clients)
5. [People and skills](#5-people-and-skills)
6. [Data and confidentiality](#6-data-and-confidentiality)
7. [How to respond well](#7-how-to-respond-well)

## 1. Independence and professional duties

| Objection | Response |
|---|---|
| "Independence rules stop us selling this to audit clients anyway, so AI changes nothing." | The limits follow the client, not the service: they apply only where the firm or an affiliate audits or attests for the client [SEC-RULE2-01-2026]. AI can also create new nonattest services: developing or hosting an AI system for an attest client can raise independence concerns, and IESBA treats hosting an audit client's data as a management responsibility [JOFA-ETHAI-2026; IESBA-TECHREV-2023]. Check by client, in a system. |
| "There are no AI rules for advisory, so we'll wait." | Existing duties apply now: the AICPA says competence and due care are unchanged and the member owns the work product [JOFA-ETHAI-2026]. Valuation has a draft AI disclosure duty [IVSC-IVSED-2026] and USPAP's AO-41 applies existing duties to AI [ISA-AO41-2026]. |
| "Outcome-based pricing is the answer." | It is the direction of vendor and commentary material, it needs baselines and system data, and contingent fees are barred for SEC issuer audit clients and restricted under the AICPA Code [BBTAX-SH-2026; SEC-RULE2-01-2026; NYSSCPA-CONTFEE-2015]. No firm has published results from outcome-based client fees. |
| "Courts won't accept AI-assisted analysis." | The exclusions so far turned on unverified or unreproducible output (*Kohls*, *Weber*), though *Weber* also requires counsel to disclose AI use [KTS-EXPERTAI-2026; GOLDMAN-WEBER-2024]. Proposed Rule 707 is not law; its published draft was withdrawn in May 2026 for further study [USCOURTS-EVID-2026]. Log tools, prompts and verification so results can be reproduced. |

## 2. Quality and reliability

| Objection | Response |
|---|---|
| "The vendor numbers are marketing." | Mostly correct. Nearly every speed or accuracy figure in the modules is vendor-published or self-reported, and no firm publishes an error, override or parallel-run rate ([state-of-ai.md](state-of-ai.md) §5). A practitioner checklist says match rates are marketing until client data reproduces them [CPAPA-AGENTSCLOSE-2026]. Run a parallel test on closed work before scaling. |
| "Reviewing AI takes as long as doing it." | Sometimes: in a vendor survey of 270 CFOs and finance leaders, finance teams spend 26% of work time verifying or correcting AI output [CFODIVE-DATARAILS-2026]. Route by confidence, review exceptions, and measure added review time in the pilot, as a JofA guide suggests [JOFA-CASAI-2026]. |
| "It will make our work thin." | Forvis Mazars US warns that QoE firms over-relying on automation reach "thin and unsupported conclusions" and that lower-quality AI-made products are spreading [FORVIS-QOE-2026]. Spend freed time on deeper analysis and keep senior review; Forvis Mazars Group paired its rollout with mandatory human review [FORVISGROUP-OPIO-2026]. |
| "AI makes things up." | It can: Deloitte Australia agreed to repay the final instalment of a government contract after AI-generated errors [CITYAM-DELOITTE-2025]. Keep calculation in deterministic engines and AI in retrieval, drafting and review with source links; check every reference before issue (valuation and forensic modules §9). |
| "Agents will post errors to client books." | Design for it: plan approval, nothing posts without authorization, locked periods, monthly review. In a vendor-run benchmark, model-kept ledgers diverged by more than 15% from the true balances after several months [PENROSE-ACCTBENCH-2025]. |

## 3. Economics and pricing

| Objection | Response |
|---|---|
| "AI efficiency is pure margin." | Unproven. A firm CEO claims margin expansion without figures [GT-CBIZ-2026]; a named RSM partner calls margin versus price cut an open question, and KPMG's advisory vice chair says AI cost is hard to attribute to individual projects [BBLAW-PRICING-2026]. No independent margin data exist ([economics.md](economics.md)). |
| "Clients will keep paying the same fee, so we needn't rethink price." | Most firms have not changed pricing [BILL-AIAMBITION-2026], but 78% of corporate clients of legal and accounting firms rate AI-enabled quality very important or essential and 32% will be reconsidering providers within 12 months [TR-FOPPR-2026], and in tax matters the IRS OPR puts AI-shortened billing in the fee frame [IRS-OPR-2026]. |
| "Value pricing is unproven." | Correct. Intent is high (69% of tax professionals in a vendor-sponsored survey expect to move to value-based, hybrid or fixed-fee billing) and pilots exist, but no firm has published fee-mix or margin results [CPACOM-BLUEJ-2026; BBLAW-PRICING-2026]. Treat it as a hypothesis to test on one service. |
| "The investment is too big for a firm our size." | Large firms are spending at scale (RSM, Grant Thornton and BDO each announced multiyear AI investments of $1B or more) [RSM-IMPACT-2026; GT-1B-2025; BDO-AI-2025], but the strongest named CAS results come from small firms on rented AI-native platforms (CAS module §5). Start with one workflow on a platform you can exit. |

## 4. Competitors and clients

| Objection | Response |
|---|---|
| "AI-native bookkeeping and cheap QoE will undercut us." | They exist and sell direct (CAS `#16`; transactions `#05`), and one first-generation vendor failed [CPAPA-XENDOO-2026]. Larger incumbents are partnering instead (CLA with Digits) [ACCTODAY-CLA-2026]. Per QoEAgent's reading of the SBA rule, software cannot be the QoE provider [QOEAGENT-WHO-2026]. |
| "Clients will do it themselves." | Some will: 40% of AI-spend increasers in RSM's survey take budget from external consulting, without saying what replaces it [CPAPA-RSMMM-2026], and in-house teams run SOX agents (risk-controls `#05`, `#14`). Move to review, interpretation and controls over the client's own agents. |
| "Our clients are small and slow on AI; there's no demand." | More than half of 725 practitioners report higher client demand in every financial category, and three in five say clients ask for proof of AI data protection [INTUIT-ACCTTECH-2026]. AI-enabled advisory demand as such was not measured. |
| "Roll-ups just cut costs; the PE advisory thesis is hype." | The scale is measured: IFAC counts 1,052 PE-linked accounting-firm transactions worldwide in 2015-2025 (177 direct investments, 875 roll-ups) [CPAPA-IFACPE-2026]. The advisory-growth rationale is the buyers' own, and in Accounting Today's 2025 Top 100 data growth at the largest firms slowed largely on advisory declines [WOODARD-TWR-2025]. Ask what a buyer would do to your platform and your attest clients' options. |

## 5. People and skills

| Objection | Response |
|---|---|
| "AI will replace our accountants and analysts." | The sources describe changed work, not replacement: time moving from data entry to communication and quality assurance [STANFORD-JAR-2026]; a BRG author says AI cannot take an oath or withstand cross-examination [CPAPA-FORENSICAI-2025]. Labour data show lower early-career employment in AI-exposed occupations, not accounting-specific [STANFORD-CANARIES-2026]. |
| "We can't cut juniors, or we will have no managers." | Agree on the risk: a consultant quoted by ICAEW recalls firms that closed apprenticeships after 2008 and struggled for management talent about five years later [ICAEW-JUNIOR-2026], and Forvis Mazars US warns of holes in future executive insight [FORVIS-QOE-2026]. Redesign junior work around reviewing AI output rather than removing it ([workforce.md](workforce.md) §6). |
| "Our seniors don't trust it." | Common: over 57% of 400 dealmakers in a vendor survey report rising senior resistance on accuracy and fiduciary grounds [INTRALINKS-AIDEAL-2026]. Start with steps a reviewer can check line by line, such as proof of cash or reconciliations. |

## 6. Data and confidentiality

| Objection | Response |
|---|---|
| "We can't put client data into AI." | Not into consumer tools. Use enterprise tools with written no-training terms, an approved-tool list, and client consent where the Code requires it [JOFA-ETHAI-2026; ANTHROPIC-PRIVACY-2026; MS-COPILOTPRIV-2026]. Deal NDAs and protective orders add limits [KJK-NDA-2026; KTS-EXPERTAI-2026]. |
| "We use an enterprise product, so client data is fine." | Vendor defaults do not settle consent, service-provider oversight under the FTC Safeguards Rule, or section 7216 for tax data [FTC-SAFEGUARDS-2026; TREAS-7216-2008]; and 34% of professionals use unapproved AI anyway [TR-FOPREPORT-2026]. |
| "Clients aren't asking about our AI." | Three in five accountants say clients ask for proof of AI data protection always or frequently, while 33% explain AI use without being asked [INTUIT-ACCTTECH-2026]. A one-page statement of tools, review steps and data handling answers it. |

## 7. How to respond well

- Concede what is true first; most objections in this field are partly right about the evidence.
- Name who measured a figure. In advisory it is usually the vendor or the firm itself.
- Turn the objection into a test on the firm's own work: a parallel run, a reviewer change log, a baseline.
- Bring independence and consent in early, before the design, not as a late veto.
- When the objection is about people, slow down and use [people-and-change.md](../../method/people-and-change.md).

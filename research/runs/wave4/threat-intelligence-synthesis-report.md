# Synthesis report: security / threat-intelligence (wave 4)

Compiled 2026-10-17. Outputs:
- Module: `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/threat-intelligence.md` (283 lines, table of contents)
- Use cases: `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/threat-intelligence.yaml` (24 entries)
- `scripts/validate.py`: no errors or warnings for these files (the remaining errors are in `archetypes/tax/ARCHETYPE.md`, which another agent owns).

## 1. Counts in and out

| Input | Candidates | Grades (A/B/C/D) |
|---|---|---|
| Practice deep dive | 23 | 4 / 7 / 8 / 4 |
| Discourse deep dive | 19 | 1 / 3 / 10 / 5 |
| Governance deep dive | 19 | 0 / 3 / 16 / 0 |
| **Total in** | **61** | 5 / 13 / 34 / 9 |
| **Out (YAML)** | **24** | 2 / 12 / 8 / 2 |

The landscape scan contributed leads, not candidate entries. A/B share out: 14 of 24 (58%).

Three inputs did not become entries. Practice-21 (Datadog's fake-applicant hunting; AI is one phrase in a TLP:AMBER abstract) is routed to human-risk, as the discourse file recommended. Governance-17 (adversary-emulation plans from CTI) appears only as a module frontier signal. Governance-19 (local or open-weight models for restricted intelligence) is an enabler, so it moved into `#13` prerequisites and the module guardrails. Two items were folded in as guardrails: governance-15 (hardening against injected content) into `#21`, and governance-16 (verification gates) into `#05`.

## 2. Duplicates merged

| Out | Merged from | Note |
|---|---|---|
| 01 PIR coverage monitoring (idea) | P15, D13 | D: interview findings only |
| 02 OSINT collection and structuring | G02, D06, D16 | ENISA named use gives B |
| 03 Underground, dark-web, stealer-log triage | P09, D07 | |
| 04 Active forum elicitation (DarkBot) | P19, D17, G14 | Inputs graded A, D and C; set to C (see §4) |
| 05 Report-to-indicator extraction with provenance | P02, D01, G04, G16 | Ladder set to automate, following Cloudflare and Adobe |
| 06 ATT&CK mapping and hunt enrichment | P17, D02, G03 | B from Intel 471's own use |
| 07 Corpus knowledge graphs and vendor overlap (idea) | P18, D14, D15, G12, G13 | |
| 08 Relevance scoring and prioritization | P06, D05, D18, G10 | |
| 12 Briefing drafting and tailoring | P07, D04, G01, P22 | ISAC idea (P22) folded in as context |
| 13 Sharing: PII screening, redaction, STIX | P10, P11, D03, G05, G06 | B from CISA AIS (NLP, deployed) |
| 14 Report-to-detection logic | P05, D09, G07 | |
| 17 Chained report-to-ticket agentic workflow | D19, G11 | |
| 19 Assistants in human-led hunts and frontline work | D10, P12, D12, G08 | Also takes the threat-hunting agents routed from security-operations |
| 21 Scheduled hunt agents with adversarial self-check | D11, G09, G15 | Negative hunting benchmark and log-injection evidence kept as guardrails |
| 24 Model providers' TI teams | P20, G18 | |

Entries kept from one input: 09 (P08), 10 (P14), 11 (P01), 15 (P16), 16 (P03), 18 (D08), 20 (P04), 22 (P13), 23 (P23).

Ref keys made canonical (the same document had different keys in different inputs):
- FLASHPOINT-ENTERPRISE-2026 = FLASHPOINT-ENTERPRISETI-2026.
- SANS-CTIPR-2026 is the press release; practice and governance called it SANS-CTI-2026. SANS-CTI-2026 is now the key-findings page.
- MITRE-TRAM-2023 = MITRE-CTID-TRAM-2023.
- MSFT-DEFENDER-AGENTS-2026 = MSFT-DEFENDERAGENTS-2026. I used the security-operations key; its ms.date is 2026-05-12, and the practice file had 2026-08-05.

## 3. Coverage by ladder and change scope

| | step | process | model |
|---|---|---|---|
| assist | 11, 19 | none | none |
| augment | 02, 06, 09, 12, 13, 14, 15, 23 | 01, 03, 07, 08, 10 | 24 |
| automate | **none** | 05, 16, 18 | none |
| delegate | n/a | 04, 17, 20, 21, 22 | **none** |

- **Automate at step level: no evidence.** The automated cases in the sources are whole pipelines (Cloudflare, Adobe), not single steps.
- **Model scope: one entry.** It covers provider-side misuse intelligence (`#24`, B on Anthropic's own statement). No source shows AI changing CTI pricing, sourcing or service lines. CyberProof's managed hunting service (`#20`) gives no pricing or service-line detail, so it stays at process scope. The nearest other sign is non-security staff querying intelligence themselves (`#11`).
- **Delegate is mostly hunting.** Both grade A entries sit there, and both are partly security-operations territory.

## 4. Grade mix and regrades

- Out: A 2, B 12, C 8, D 2.
- Practice-01 (Cowbell, Superhuman), A → B. Under the 2026-10-17 rule, both figures are a customer's statements in a vendor case study with no method. They are kept and labelled.
- Practice-14 (Microsoft-authored Threat Research Agent), A → B. The paper does not name the deploying organization (Microsoft is an inference). Its figures compare models on a benchmark the team built, not results before and after deployment, and the paper's text and table disagree on the size of the IoC gain.
- Practice-19 (DarkBot), A → C. Its figures come from a research prototype tested by its authors, not from a CTI team's operations. D would understate it because a live trial took place.
- Kept at A:
  - `#21` Grow Therapy: the company's own cost table and finding counts before and after tuning. Its noise shares are labelled as estimates.
  - `#22` Microsoft Dynamic Threat Detection Agent: precision from tracked customer feedback over 120 days. The figure is vendor-published because Microsoft is writing about its own product.
- Grading convention used: lab-only results with no product or deployment are D, labelled "idea". Where a product, vendor claim or named statement exists without measurement, the entry is C or B. The governance file graded lab work C, so several of its entries moved.
- Provenance: academic authors who evaluate their own systems are labelled `independent` (academic), and the measures field says "authors' own system". Governance had used `self-reported` for these.

## 5. Gaps

- **No independent operational evidence.** No source gives override rates, edit rates, error rates of a deployed CTI assistant, a parallel run or an inspection finding. Every figure is vendor-published, self-reported, a survey share or a lab benchmark, and most benchmarks are preprints read at abstract level.
- **Model-scope change and automate at step level:** no evidence (see §3).
- **Decision influence.** No source links AI to the 91% value versus 26% influence gap, or to CTI feedback loops.
- **Workforce.** There is no headcount, hiring or junior-pipeline data for CTI. Only a dozen job postings were read in full, and two analyst postings (Recorded Future, Dragos) do not mention AI.
- **ISACs and government.** There is one panel report (Health-ISAC, RH-ISAC, FS-ISAC), and no ISAC is known to use AI on member submissions. The AI-ISAC had no launch date as of February 2026. Coverage outside the US and EU is thin.
- **Sharing law.** The status of the US Cybersecurity Information Sharing Act of 2015 after 2026-09-30 is unconfirmed.
- **Gated reports:** the full SANS 2026 CTI survey, the Flashpoint report body, Mandiant M-Trends 2026, the CrowdStrike Global Threat Report and the IDC study.
- **Cross-module ids.** Final YAML ids for security-operations, human-risk, vulnerability-exposure and ai-security did not exist when this was written, so overlaps are flagged by module name. When those files exist, add id cross-references:
  - security-operations: `#14`, `#15`, `#21`, `#22`
  - human-risk: `#18`
  - vulnerability-exposure: the GTIG triage advice in module §8

## 6. Routed items

**Picked up from other security deep dives (routed to threat-intelligence)**
- From security-operations practice:
  - Threat hunting agents (Microsoft Threat Hunting Assistant, CrowdStrike Agentic Recon, Google Threat Hunting agent in preview, Dropzone AI Threat Hunter) → `#19`. Only names were passed on, plus TECHINFORMED-GOOGLE-2026 for the preview status.
  - Microsoft Threat Intelligence Briefing Agent → `#12`.
- From incident-response and security-operations discourse: the Apura OSINT copilot (→ `#02`) and Flare StealerLens (→ `#03`).
- From ai-security, both dives: CERT-In's report of a campaign using AI-agent offensive frameworks that cut time from first access to impact to a few hours (THN-CERTIN-2026), and GTIG's under-six-hour campaign → module §8. GTIG's points on theft of AI assets and extortion of AI repositories were not used; they are attacker content.
- From vulnerability-exposure: GTIG's finding that 62% of vulnerabilities exploited January to August 2026 were zero-days → module §8.
- Not used, because no details were passed on:
  - CyberSOCEval (arXiv 2509.20166, from security-operations governance), noted in `#09`.
  - RESILIENTCYBER-FASTER-2026 (from security-operations discourse).
  - The n-day weaponisation hypothesis, BeyondTrust timeline and "first LLM-built zero-day exploit script" (from vulnerability-exposure), which is attacker detail.
  - M-Trends and DBIR initial-access and time-to-exploit statistics, which come from gated reports.
  - Unit 42's AI attack case (from incident-response).

**Routed from the threat-intelligence inputs to other modules (for their synthesis)**
- **security-operations:**
  - Charlotte AI detection triage (CRWD-CHARLOTTE-2026), Cloudflare's agentic Managed Defense harness (post 2026-10-07, not read) and the Cloudy log assistants (CLOUDFLARE-CLOUDY-2025).
  - The SOC side of the Dynamic Threat Detection Agent (ARXIV-2605.20896) and the Grow Therapy hunts (GROWTHERAPY-HUNT-2026).
  - FIRST sessions on tier-1 triage with general LLMs and Cisco's CoAnalyst (FIRST-CON-2026).
  - ALERT-BENCH: every approach missed at least 40.4% of attack alerts; a multi-agent design reached F1 0.958 (ARXIV-2610.10608).
  - The detection rule lifecycle and detection-as-code (DETENGWEEKLY-163-2026, DETENGWEEKLY-168-2026).
  - The log-injection papers (USENIX-LOGINJECT-2026, ARXIV-2605.24421).
- **incident-response:**
  - FIRST sessions on AI-assisted IR timelines on OCSF (Centene) and PSIRT agents.
  - DFIR agents manipulated through forensic artifacts (TLP:AMBER).
  - Atlassian's IR documentation framework.
  - CISA/NIST incident-readiness practices for AI training and evaluation (2026-10-16).
- **vulnerability-exposure:**
  - GTIG disclosure and exploitation trends (5,045 to 10,740 disclosures a month; exploited vulnerabilities 10.5 to 18 a month; only 0.23% of 2026 disclosures observed exploited) and the advice to move to threat-intelligence-driven triage (GTIG-VULNTRENDS-2026).
  - Mandiant's AI-assisted vulnerability management blueprint (MANDIANT-AIVM-2026).
  - Cowbell's vulnerability playbook alerts (RF-COWBELL-2026).
  - UK NCSC statements at CyberUK (TECHRADAR-NCSC-2026).
- **ai-security:**
  - Adversary use of AI (GTIG-AITRACKER-2026, ANTHROPIC-TIR-2026, ANTHROPIC-GTG1002-2025).
  - Google's CISO note on monitoring AI threats (GOOGLE-CISOPERSP-2026).
  - CyCraft and NTT DATA sessions on attacking LLM-assisted and DFIR agents (FIRST-CON-2026).
  - ATT&CK v20 AI techniques (MITRE-ATTCK-2026), semantic malware and malicious agent skills (DETENGWEEKLY-163-2026; INTEL471-AIHUMAN-2026).
  - NIST COSAiS, the CISA/ACSC agentic guidance and the AI-ISAC.
  - KnowHow provenance analysis: all 16 APT campaigns detected, up to 90% fewer node-level false positives (NDSS-KNOWHOW-2026).
  - The NIST Cyber AI Profile (IR 8596; page not opened).
- **human-risk:**
  - Datadog's detection stack for fake job applicants (DPRK) with "AI-driven risk assessment" (FIRST-CON-2026, 2026-06-17), plus OSINT checks on fake personas (BSIDESLV-2026).
  - Brand-abuse and phishing takedown preparation (MEMCYCO-AGENTIC-2026; FORRESTER-PREDICT-2025), which is also kept here as `#18`.
- **security-governance-risk:**
  - The AI-ISAC policy discussion (NEXTGOV-AIISAC-2026) and information-exchange policy (FIRST SIG).
  - Legal review of CTI sharing and AI-use disclosure policy (SANS-CTIPR-2026; FEEDLY-VALUE-2026).
  - SEC disclosure rules, the EU AI Act timeline, ISACA and ISC2 workforce data, and the ISO/IEC 27001/27002 control on threat intelligence (not opened).

## 7. Suggested improvements to the briefs

1. **Give one grading rule for lab benchmarks and prototypes.** The three angles graded the same kind of evidence D, C or even A (DarkBot). A line such as "benchmark or prototype only, no product or deployment = D labelled idea; a product or named statement without measurement = C or B" would remove most regrading.
2. **Say who counts as `independent`** when academic authors evaluate their own system. Governance used `self-reported` and the other two angles used `independent`.
3. **Publish a shared ref register per archetype**, with the canonical key and date per URL, before the deep dives start. The same SANS press release carried two keys and two source types, and the same Microsoft page had two keys and two dates.
4. **Ask deep dives to give the grade-A basis in one line** ("tracked metric / study / customer quote"), so the 2026-10-17 rule can be applied without rereading the source.
5. **Run module syntheses in dependency order, or publish provisional ids early**, so cross-module references can use ids, not module names.
6. **Ask for a ladder × scope matrix in each deep dive**, so missing cells (here automate/step and anything at model scope) are searched for deliberately, not discovered at synthesis.
7. **When routing an item, pass the source details on** (title, date, URL and the figure), not only a ref key. Several routed items here (CyberSOCEval, RESILIENTCYBER-FASTER-2026) could not be used.

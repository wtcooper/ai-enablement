# Synthesis report: security / ai-security (wave 4)

Prepared 2026-10-17. Inputs: `landscape-security.md` and the three angle deep dives (`security-ai-security-threats-redteam.md`,
`-agent-identity-containment.md`, `-governance-assurance.md`), plus the "Routed to other modules" sections of every other
`security-*.md` file in this folder. Outputs:
`plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/ai-security.md` (286 lines)
and `.../security/use-cases/ai-security.yaml` (25 entries). `scripts/validate.py` reports no errors or warnings for either file.

## 1. Counts in and out

| | Threats and red teaming (T) | Agent identity and containment (C) | Governance and assurance (G) | Total |
|---|---|---|---|---|
| Candidates in | 21 | 22 | 19 | 62 |
| Grades in (A/B/C/D) | 8/10/2/1 | 3/10/8/1 | 3/4/11/1 | 14/24/21/3 |

Out: **25 use cases**, grades **A 9, B 11, C 4, D 1** (A/B share 80%). 122 distinct source refs in the YAML; four more
module-only refs (GTIG-VULNTRENDS-2026, VULNCHECK-1H2026, RSAC-ISB-2026, MITRE-ATTCK-2026). 25 was chosen over the brief's
allowance of 30 so the file also meets the validator's 15-25 target.

## 2. Duplicates merged (every input id accounted for)

| Out | Merged from | Notes |
|---|---|---|
| 01 Threat-model against taxonomies | T01 | |
| 02 AI red teaming as a standing practice | T02, T03, T19, T20 | Scoping, in-house roles, outside researchers and bounties, buying criteria |
| 03 Adaptive and crowdsourced robustness measurement | T04, T05, T18 | |
| 04 Pre-deployment frontier evaluation | T07, T08 | OpenAI harness figure moved here from C08 |
| 05 Continuous agentic red teaming | T13, C15 | Graded C (C15 was B): agentic part is a plan, DEF CON results are abstracts |
| 06 Agent identity, scoped tokens, MCP authorisation | C01, C03, C13, C20 | C20 (idea, D) kept as an "idea" note, not an entry |
| 07 Runtime policy enforcement | C04, G09 | |
| 08 Classifier gate plus human approval for high-impact actions | T06, C14 | |
| 09 Secret and privilege sweeps | C16, C21 | |
| 10 Containment architecture | T09, C05, C06, C19 | |
| 11 Monitoring, paging, halt | T10, C08, C09, C17 | Graded B (C08 was A on a harness figure that does not measure monitoring) |
| 12 Attributed tamper-resistant logs | C07, G17 | |
| 13 Untrusted content as hostile input | T14, T17, C18 | |
| 14 AI supply chain vetting and AI-BOMs | T15, C12, G19, G10 | |
| 15 Distillation detection | T16 | |
| 16 Idea: data tampering checks | T21 | Only poisoning entry, kept as D |
| 17 Full-population lookback review | T11, C22, G11 | Three dives described the same Anthropic and OpenAI reviews |
| 18 Independent investigation and victim forensics | T12, G12 (forensic half) | |
| 19 Incident readiness, response and reporting | C10, C11, G12 (disclosure half), G14, G15 | |
| 20 Shared near-miss exchange | G13 | |
| 21 Inventory and shadow AI | G01, G02, C02 | |
| 22 Proportionate governance, tiers, crosswalks | G04, G16, G08, G18 | |
| 23 MSCI agent test for auditors | G03 | |
| 24 Third-party AI assurance and certification | G05, G06 | |
| 25 AIUC-1 certification with insurance | G07 | |

Ref keys were normalised to one per document: NISTCISA-IRKEY-2026 (also NIST-CISA-NSA-IRKEY-2026), ANTHROPIC-EVALINC-2026
(also ANTHROPIC-EVALINCIDENTS-2026), HF-TIMELINE-2026 (also HUGGINGFACE-INTRUSION-2026), NIST-IRKEY-NEWS-2026 (also
NIST-CAISI-INCIDENT-2026; not needed in the final set). OPENAI-HFTECH-2026 was typed "vendor" in one dive and "firm" in
another, with two URLs; the "Hugging-Face%20" URL returns 200 and the other 404, so the working URL and "vendor" are used.

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 01 | 19, 22, 24 | 20 | 5 |
| augment | 02, 09, 16, 18, 23 | 03, 04, 17, 21 | 25 | 10 |
| automate | 12, 13 | 06, 07, 08, 10, 11, 14, 15 | | 9 |
| delegate | | 05 | | 1 |
| Total | 8 | 15 | 2 | 25 |

- **Delegate:** one entry (05), grade C, announced. No evidence was found of an agent owning a security outcome for AI
  systems with human checkpoints in production.
- **Model scope:** two entries (20 shared exchange, grade C; 25 AIUC-1 certification and insurance, grade B). No evidence
  of priced managed services for agent security outcomes.
- Ladder here describes the control or tooling, because AI is usually the object of the work (as in assurance-over-ai).

## 4. Grade mix and regrading

- Out: A 9 (03, 04, 08, 10, 14, 15, 17, 18, 23), B 11, C 4 (05, 07, 20, 21), D 1 (16).
- All nine A entries rest on figures the named organisation reports as measured (studies, counted runs, test counts).
  None is an independent measurement of a deployed enterprise control: six are AI-lab or government evaluation
  settings, 08 and 23 are vendor-published, 14 is a research measurement.
- Downgrades: C08 A to B (merged into 11); C15 B to C (merged into 05). 23 (MSCI) stays A under the 2026-10-17 rule: the
  test counts and severity finding are the tester's results, not a recollection; the CISO quote and MSCI's agent-count
  estimates are treated as B-level and kept in 22 with that label.
- Discrepancy flagged, not resolved: the two dives name OpenAI's production harness differently (Codex vs ChatGPT) for the
  same "under 1% of baseline / over 100x" figure; the YAML leaves it unnamed.

## 5. Cross-references to other security modules

Notes in the YAML point to: `security-identity-access-04`, `-05`; `security-operations-19`, `-20`;
`security-incident-response-03`, `-04`, `-09`, `-15`, `-17`, `-18`, `-19`, `-20`, `-21`; `security-application-security-21`;
`security-vulnerability-exposure-22`; `security-threat-intelligence-24`; and `assurance-assurance-over-ai-19`. The
incident-response module covers much of the same 2026 incident record from the responder's side (entries 17-21 there);
ai-security keeps the AI-specific controls.

## 6. Routed items

### 6.1 Routed into ai-security from other modules (picked up)

Used in the YAML or module: ARXIV-2605.22333 (40.55% of 7,973 remote MCP servers expose tools unauthenticated; from
identity-access governance) and TOB-SKILLS-2026 (public skill scanners bypassed; from application-security discourse) in
14; OKTA-DEX-2026 (Okta's own agent registered in its directory; from identity-access practice) in 06; GTIG-VULNTRENDS-2026
(2,076 AI-related CVEs, 782 in agent-orchestration frameworks) and VULNCHECK-1H2026 (10 of 28 AI-system KEVs exploited) in
module §5; TOB-VMS-2026, REGISTER-BHDC-2026, UKAISI-INCIDENT-2026, CISA-AGENTIC-2026, ARXIV-2605.24421 were already inputs.

Not used (leads for the next pass; source details are in the routing files): SANS-ITDR-2026 (73% use agentic AI needing
credentials, no governance control above 40%); PANW-IDLANDSCAPE-2026 (79 agent identities per human; 40% of agents with
data access); OPENID-AGENTID-2025 whitepaper; Okta for AI Agents kill switch and World Central Kitchen (OKTA-AGENTS-2026,
OKTA-WCK-2026); SailPoint, Saviynt and Microsoft agent-identity products; SailPoint Horizons (79% agents in production);
Okta/Yubico agent verification survey; Forrester Identiverse and Oktane recaps; MANDIANT-AIVM-2026 controls for agents;
TENABLE-HEXA-2026 untrusted-insider agent design; ARXIV-2608.23897 package-name hallucination (slopsquatting); NIST SP
800-218A; Vanta's Samsara and Synthesia ISO 42001 work; Kovrr AI risk quantification; OneTrust and Optro AI governance;
BAKERDONELSON-IBM-2026 (92% of organisations with an AI incident lacked AI access controls); PROMPTARMOR-ELASTIC-2026;
FIRST-CON-2026 sessions on DFIR-agent manipulation and CTI pipeline injection; Detection Engineering Weekly items on coding-
agent monitoring and promptware; MSFT-DEFENDER-AGENTS-2026; REGISTER-COBALT-2026 (AI/LLM pentest severity rates; the
routed summary is ambiguous about which figure is which); CLOUDFLARE-GLASSWING-2026; job postings for agentic product
security (Datadog, Coinbase, Cloudflare).

### 6.2 Routed out of ai-security to other modules (for their synthesis)

- **security-operations:** ARXIV-2610.10608, every studied triage approach missed at least 40.4% of attack-related alerts
  across 1,247 alerts (abstract); Hugging Face's LLM anomaly pipeline; agentic SOC products and FIRST triage sessions.
- **incident-response:** Hugging Face's finding that hosted frontier models refused attack-log analysis, so it used an
  open-weight model and advises vetting one beforehand; LLM triage and log analysis of 17,000+ events; NIST, NSA and CISA
  practices 5-7 (evidence, shutdown, recovery); METR and Hugging Face forensic methods.
- **threat-intelligence:** GTIG adversary move to agentic workflows (a credential-harvesting campaign in under six hours),
  theft and extortion of AI assets; CERT-In's campaign using AI-agent offensive frameworks that cut first access to impact
  from days to hours.
- **identity-access:** general privileged access, CISA/NIST token-theft guidance (2026-09-15), non-human identity beyond
  agents; OWASP maturity Level 1-2 agent registries.
- **cloud-infrastructure:** Kubernetes operator RBAC; Unit 42 on AWS managed policies for compromised IAM credentials
  (2026-09-21); cloud least-privilege reviews.
- **vulnerability-exposure and application-security:** CERT-In's report of credentials in configuration and public repos;
  DEF CON 34 vulnerabilities in AI infrastructure (local runtimes, gateways, CLI agents); ARXIV-2604.05292 (55.8% of 3,500
  AI-generated code artefacts had at least one formally identified vulnerability); rapid host patching implied by
  TOB-VMS-2026; skill and plugin scanning.
- **data-security-privacy:** IBM: shadow-AI incidents exposed more personal data (65% vs 53%) and IP (40% vs 33%); Okta:
  of staff using unapproved tools, 54% share internal messages, 45% HR information, 39% confidential documents; OpenAI's
  disclosure that research agents sent data to third-party services, including 53 user images posted as unlisted links.
- **security-governance-risk:** AI inside GRC work (CSA automated questionnaire scoring; OWASP Level 4 audit-evidence
  automation); the security team's own AI-use policy (56% of ISACA respondents helped write one); AI insurance exclusions;
  credentials market (ISACA AAIA/AAISM/AAIR, CSA TAISE); Anthropic's embedded independent evaluators
  (ANTHROPIC-EVALUATORS-2026).
- **ot-critical-infrastructure (optional):** CISA/ACSC references to AI in operational technology; CISA-AIOT-2025.

## 7. Gaps

- **No independent enterprise outcome data.** No error, override, false-positive or recall rates for agent monitors,
  transcript review, identity or sandbox controls; no before-and-after result for any deployed control; no cost, coverage
  or time measure for an enterprise AI red-team programme.
- **Evidence is lab-heavy.** The strongest figures come from OpenAI, Anthropic and UK AISI evaluation environments; their
  fit to ordinary enterprise agents is adjacent and is flagged per entry.
- **Delegate and model levels are thin** (one and two entries; see §3).
- **Primary documents read only through press or partially:** the CERT-In advisory (via The Hacker News), Anthropic's
  July post (opened by one dive, press-only in another), the CSA/Aembit and CSA/Zenity survey reports, ISO/IEC 42001
  (bot challenge), the CISA/ACSC guide (PDF read by one dive only), MAS sections 4, 5 and 7.
- **Not found:** Big Four or consultancy AI-security service lines; small and mid-size organisations; non-US/EU regulators
  beyond MAS and CERT-In; junior hiring or headcount effects; a production data-poisoning check; how many organisations
  have a working kill switch.
- **Unstable terminology:** US agency pages now print "super intelligence (SI)" for "AI" (Executive Order of 2026-09-29);
  searches need both terms.

## 8. Suggested improvements to the briefs

1. **Give split dives a shared ref-key register before research starts.** Four documents got two keys each, and one
   document got two types and two URLs (one broken).
2. **Assign the shared incident record to one dive.** The OpenAI/Hugging Face, Anthropic, AISI and CERT-In material
   appeared in all three dives and produced three-way duplicates (17, 19); the others should cross-reference it.
3. **Ask researchers to say which claim an A figure supports.** C08 was graded A on a harness-propensity figure that does
   not measure the monitoring control it was attached to.
4. **Require verbatim product, model and harness names next to each figure**, to avoid conflicts like Codex vs ChatGPT.
5. **Ask routing sections to carry full source details** (URL, date, access), so synthesis can cite routed items without
   searching other files.
6. **State ladder semantics when AI is the object of work** in the brief, and invite proposed patterns (here: adversarial
   evaluation of an AI system, agent action gate, containment architecture).
7. **Ask explicitly for enterprise, non-lab deployments** (banks, insurers, mid-size firms) and for a non-US/EU regulator
   sweep, the two weakest areas.
8. **Align the entry ceiling** with `scripts/validate.py` (15-25), or raise the validator's limit for modules allowed 30.

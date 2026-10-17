**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are a research analyst building the **source landscape** for one business archetype. Your output
will steer many later deep-dive researchers, so breadth and accuracy matter more than prose. Today is
2026-10-17.

**Archetype:** security: Security: protecting an organization's systems, data, identities and people from threats. Delivered by in-house security functions (the CISO organization, from small teams to large enterprises) and by security service providers (managed security and MDR providers, security consultancies, penetration-testing and red-team firms, incident-response firms). The value chain follows industry frameworks such as NIST CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover). Include how AI changes defenders' work (AI in the SOC, agentic triage and investigation, AI code review) and the security of AI itself. Attacker use of AI matters only as context for what defenders must do; do not research offensive techniques in detail.
**Proposed modules:** security-governance-risk (security governance, risk management and quantification, policy, compliance attestations and audits, third-party risk) · security-operations (SOC detection engineering, alert triage, investigation, MDR) · threat-intelligence (CTI and threat hunting) · incident-response (response, forensics, recovery and resilience) · vulnerability-exposure (vulnerability management, attack surface, penetration testing and red teaming) · application-security (secure SDLC, code review, software supply chain, DevSecOps, product security) · cloud-infrastructure (cloud posture, network and endpoint security) · identity-access (IAM, privileged access, identity threat detection) · data-security-privacy (data discovery and classification, DLP, encryption, privacy engineering) · human-risk (awareness, phishing, insider risk) · ai-security (securing AI systems and agents: prompt injection, model and agent governance). Check against industry domain models (NIST CSF 2.0, the ISC2 CISSP domains, Gartner and Forrester practice taxonomies) and say whether OT/IoT security, security architecture, or fraud deserve modules.

## What to find

Use web search, and open the pages themselves (see the access note below); don't rely on search
snippets alone. The pilot's scan ran on snippets only and needed corrections.

**Access:** the web-fetch tool can fail on DNS in this environment. Use
`curl -sSL --max-time 30 -A "Mozilla/5.0" <url>` through Bash, and `pdftotext` for PDFs.

Use web search and fetch extensively. Aim to read **at least 40 distinct sources** across at least
**6 source types**. Prefer material from the last 12–18 months. For each item, record its name, the
organizer or publisher, a URL, the date or edition, and one line on why it matters for AI in this
field.

1. **Conferences and events (most important).** The main conferences, symposia and summits in this
   field, plus relevant technology-in-the-field events.
   - Cover the 2025 and 2026 editions.
   - Record AI-related **sessions, tracks, keynotes and panels**: titles, and the organizations of the
     speakers where available.
   - Include proceedings, slide decks, session recordings and recaps if they are public.
2. **Regulators and standard-setters:** statements, staff guidance, spotlights, inspection
   observations, consultations and standard changes that touch technology or AI.
3. **Professional bodies:** guidance, toolkits, surveys and reports on AI.
4. **Academic work:** the main journals and research centers, and notable papers and working papers on
   AI in this field from 2024–2026.
5. **Firms:** large and mid-tier firms' public AI platforms, announcements, reports and case studies.
   Include in-house teams where relevant.
6. **Vendors:** the main technology vendors and recent AI product launches for this field.
7. **Trade press, newsletters, podcasts and practitioner communities.**
8. **Surveys and benchmarks** of AI adoption in this field.

## Also produce

- **Evidence density per module:** high, medium or low, judged by how much specific public material
  exists. Low-density modules get one combined deep dive instead of three.
- **Source keys.** Give every source a ref in the form `PUBLISHER-SHORT-YYYY`. Later researchers reuse
  these refs.
- **Module check.** Is the proposed module list right for how practitioners divide the work? Propose
  changes, with reasons.
- **Journey-stage markers.** For this field, what does each stage look like in practice: Curious,
  Experimenting, Adopting, Scaling, AI-native? Give two or three observable markers per stage.
- **Ten or more frontier signals.** Dated, sourced signals of where AI in this field is heading in the
  next 12–36 months: agentic uses, regulatory moves, business-model shifts.
- **Research leads per module.** For each module, the five or more most promising sources or search
  directions for later deep dives.
- **Gaps.** What you couldn't reach (blocked or paywalled) and what seems under-documented.

## Rules

- Do not invent sources, sessions, speakers or dates. If you can't confirm something, mark it
  `(unverified)` or leave it out.
- Summarize in your own words. Quotations must be under 25 words.
- Public sources only.

## Output

Write a markdown file to `/home/user/ai-enablement/research/runs/wave4/landscape-security.md` with these sections:

1. Summary
2. Conferences & events
3. Regulators & standard-setters
4. Professional bodies
5. Academic
6. Firms
7. Vendors
8. Press, podcasts & communities
9. Surveys & benchmarks
10. Module check
11. Journey-stage markers
12. Frontier signals
13. Research leads per module
14. Gaps
15. Source count by type

Then reply with a summary of **no more than 200 words**: the source count by type, the three most
valuable finds, and the main gaps.


## Security-specific notes

- Conferences to cover include RSAC, Black Hat, DEF CON (defensive and AI Village tracks), BSides, FIRST, SANS summits, Gartner Security & Risk Management Summit, fwd:cloudsec, OWASP Global AppSec, and the academic venues USENIX Security, IEEE S&P, ACM CCS and NDSS.
- Regulators and standards: NIST, CISA, ENISA, NCSC, the SEC cyber disclosure rules, NIS2, DORA, sector regulators; OWASP Top 10 for LLM applications, MITRE ATT&CK and ATLAS, CIS, CSA.
- Workforce: ISC2 and ISACA workforce studies and the effect of AI on SOC analyst and junior roles.
- Public sources only. Do not collect exploit details, malware or attack instructions.

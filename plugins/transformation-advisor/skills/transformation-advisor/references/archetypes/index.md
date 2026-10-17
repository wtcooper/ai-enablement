# Archetypes index

An archetype is researched knowledge of one field: its value chain, real AI use with graded evidence, regulation,
economics, workforce and where it is heading. Match the user's business to one archetype during Onboard, then read
that archetype's `ARCHETYPE.md`; it indexes its own files and modules.

## Available archetypes

| Archetype | Extends | Recognition cues (match on what is delivered, to whom, and who regulates it) | Modules | Status |
|---|---|---|---|---|
| [assurance](assurance/ARCHETYPE.md) | professional-services | Audit opinions, SOC reports, attestation, sustainability assurance, assurance over AI; inspections and peer review; independence rules; "busy season", "workpapers", "sign the opinion". Also in-house internal audit and SOX teams | acceptance-independence · planning-risk-assessment · controls-testing · substantive-testing · specialists · completion-reporting · quality-management · soc-attestation · sustainability-assurance · assurance-over-ai | Available |
| [tax](tax/ARCHETYPE.md) | professional-services | Returns (1040, 1065, 1120), K-1s, organizers, extension season; the provision (ASC 740, IAS 12) and Pillar Two; sales and use tax, VAT, e-invoicing; transfer pricing; notices, exams and Appeals; tax research and advice; Circular 230, section 7216, PCRT. Also in-house corporate tax departments ("head of tax", TEI). Auditing a client's tax balances is assurance | compliance-individual-business · compliance-corporate · provision-pillar-two · indirect-tax · transfer-pricing · controversy · research-advisory · data-technology | Available |
| [security](security/ARCHETYPE.md) | — | Protecting systems, data, identities and people, and the AI an organization runs (NIST CSF 2.0: Govern, Identify, Protect, Detect, Respond, Recover). In-house CISO teams: SOC, "alert fatigue", SIEM and EDR, AppSec and code scanning, IAM and access reviews, GRC, questionnaires and TPRM, NIS2, DORA, SEC 8-K. Providers: MDR, MSSP, pentest and red team, IR retainers. AI security: agent identities, prompt injection, shadow AI. Issuing SOC 2 reports or assurance over AI is assurance | governance-risk · operations · threat-intelligence · incident-response · vulnerability-exposure · application-security · cloud-infrastructure · identity-access · data-privacy · human-risk · ai-security | Available |

## Not yet available

| Archetype | Would cover | Until it exists |
|---|---|---|
| professional-services | The shared base: pursuit and proposals, acceptance and risk, scoping and pricing, staffing, delivery management, quality review, billing, knowledge management. Also the base for consulting and for security service providers | Use the method and the library. Assurance, tax and security files cover the field-specific parts of those firms only |

## How to match

1. Listen for the cues above in what the user says about their work; ask one question if unsure ("What does
   your team deliver, and to whom?").
2. **Overlay first.** If `overlay/archetypes/<id>/` exists in the workspace, it takes precedence over a plugin
   archetype with the same id, and can add an archetype the plugin lacks. A folder labelled provisional came from
   on-the-spot research; say so when you use it.
3. **One match:** record `profile.archetype` and pick focus modules from that archetype's module table, using the
   user's goals and pain points. Load module files only when the conversation reaches them.
4. **Partial match** (for example, an internal audit team, or a firm whose practice spans assurance and tax): use
   the closest archetype for the work it covers, and the library for the rest. Say which parts are covered.
5. **No match:** follow `../library/index.md` §9. Offer on-the-spot research only if the user agrees and you have
   web access (`../briefs/research-archetype.md`).

Consulting is not an archetype: consulting teams use professional services (once available), the library's
functions, and their client's archetype.

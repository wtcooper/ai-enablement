# Archetypes index

An archetype is researched knowledge of one field: its value chain, real AI use with graded evidence, regulation,
economics, workforce and where it is heading. Match the user's business to one archetype during Onboard, then read
that archetype's `ARCHETYPE.md`; it indexes its own files and modules.

## Available archetypes

| Archetype | Extends | Recognition cues (match on what is delivered, to whom, and who regulates it) | Modules | Status |
|---|---|---|---|---|
| [assurance](assurance/ARCHETYPE.md) | professional-services | Audit opinions, SOC reports, attestation, sustainability assurance, assurance over AI; inspections and peer review; independence rules; "busy season", "workpapers", "sign the opinion". Also in-house internal audit and SOX teams | acceptance-independence · planning-risk-assessment · controls-testing · substantive-testing · specialists · completion-reporting · quality-management · soc-attestation · sustainability-assurance · assurance-over-ai | Available |

## Not yet available

| Archetype | Would cover | Until it exists |
|---|---|---|
| tax | Tax compliance, provision, indirect tax, transfer pricing, international and global minimum tax, controversy, advisory, tax data and technology; firms and in-house tax teams | Use the method and the library. Assurance's quality-management and specialists modules touch tax work inside an audit only |
| security | Protecting systems, data, identities and people: governance and risk, security operations, threat intelligence, incident response, vulnerability and exposure management, application security, cloud and infrastructure, identity and access, data security and privacy, human risk, AI security; in-house security functions and security service providers | Use the method and the library. Assurance's assurance-over-ai and soc-attestation modules cover attesting to security controls, not running them |
| professional-services | The shared base: pursuit and proposals, acceptance and risk, scoping and pricing, staffing, delivery management, quality review, billing, knowledge management. Also the base for consulting | Use the method and the library. Assurance files cover the regulated parts of an assurance firm only |

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

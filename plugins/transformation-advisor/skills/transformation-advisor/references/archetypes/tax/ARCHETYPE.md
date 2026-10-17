# Tax (archetype)

Last researched 2026-10-17. The index for the tax archetype: read it once onboarding points to tax, then load only the
module and archetype files the conversation needs. Source keys in brackets resolve in [sources.md](sources.md).

## What it covers

Tax compliance (individual and small-business returns; corporate returns, credits and incentives), income tax
accounting and the global minimum tax, indirect tax, transfer pricing, controversy (including tax authorities' own AI),
research and advisory, and tax data and technology. What the client or the business buys is a correct filing, a
defensible position or a reliable tax number. A named person signs or stands behind it, and a tax authority can
examine it years later.

## Who it serves

- **Firms of every size:** the Big Four, mid-tier and PE-backed firms, small CPA and enrolled-agent practices, retail
  preparers, AI-native entrants and roll-ups. Starting points differ sharply ([state-of-ai.md](state-of-ai.md)).
- **In-house corporate tax departments.** They run compliance, provision, indirect tax and transfer pricing for their
  own group, buy outside help, and often own the tax data and technology. Most are under-resourced: 58% of 288
  departments said so in 2025 [TR-CORPTAX-2025].
- **Typical users:** tax partners, managing partners, heads of tax and tax directors, tax technology, indirect tax,
  transfer pricing and controversy leads, national-office and risk partners.

## What it extends

It extends **professional-services**: pursuit, acceptance, scoping and pricing, staffing, delivery, quality review,
billing and knowledge management all still apply. Tax changes four things. Statute, regulations and tax-authority
practice set the work, not professional standards alone. The individual who signs a return carries "primary
responsibility for the overall substantive accuracy" of it [LII-CFR-SIGN-2026], and preparer penalties attach to the
practitioner ([guardrails.md](guardrails.md) §5). Conduct and
confidentiality rules apply to AI as they stand (Circular 230, IRC section 7216, PCRT, the TPB code) [IRS-OPR-2026;
PCRT-AI-2026; TPB-GS55-2026]. And the counterparty, the tax authority, is scaling its own AI [GAO-2026; IRS-AIFIRST-2026].

## Recognition cues

Match on what is delivered, to whom and who regulates it, not on job titles. Cues that point to tax:
- "We prepare 1040s, 1065s, 1120s", "K-1s", "organizers", "extension season", "e-file", "Form 8879", "PTIN", "EA".
- "The provision", "ASC 740", "IAS 12", "ETR", "rate reconciliation", "Pillar Two", "GloBE", "the GIR", "QDMTT".
- "Sales and use tax", "VAT", "nexus", "exemption certificates", "e-invoicing", "clearance", "ViDA".
- "Transfer pricing", "local file", "master file", "CbCR", "benchmarking", "intercompany agreements", "APA".
- "Notices", "CP2000", "IDRs", "the exam", "Appeals", "Tax Court"; "Circular 230", "OPR", "section 7216".
- "Research memo", "opinion", "planning", "M&A tax diligence", "Blue J", "CoCounsel", "Bloomberg Tax".
- "ONESOURCE", "Corptax", "Vertex", "Avalara", "tax data"; in house: "head of tax", "TEI", "our auditors review the provision".

Not tax: auditing a client's tax balances or provision inside a financial-statement audit (assurance: its specialists
and substantive-testing modules); bookkeeping and the monthly close (no archetype yet; use the library); tax
authorities' own staff (tax-authority AI appears here only as the counterparty, in controversy).

## Modules

**Evidence** reflects each module's share of use cases graded A or B (strong: 50% or more; moderate: 30-49%; thin: under
30%); counts are as of the last review. **Use thin modules for risk awareness and interview probes, not as proof
points.** Quote their examples as ideas or early signals, and say plainly that no named organization has published a
measured result. No module has an independent error, override or parallel-run result for a commercial tax AI tool.

| Module | What it covers | Evidence |
|---|---|---|
| [compliance-individual-business](modules/compliance-individual-business.md) | 1040, 1041, 1065 and 1120-S preparation by CPA firms, EAs and retail preparers: organizers, extraction, agent-prepared returns, review, consent, pricing. Agentic products cluster here; figures are vendor-published | moderate (10 of 25 A/B) |
| [compliance-corporate](modules/compliance-corporate.md) | Corporate federal and state returns, international forms, R&D credit and Section G, calendar; in house and at large firms | thin (3 of 24 A/B) |
| [provision-pillar-two](modules/provision-pillar-two.md) | ASC 740 and IAS 12 provision, ASU 2023-09 disclosures, GloBE calculations and the GIR XML pipeline. Strongest named evidence is rules-based software, not AI | thin (0 of 16 A/B) |
| [indirect-tax](modules/indirect-tax.md) | VAT, GST and sales and use tax: determination, product mapping, certificates, nexus, returns, e-invoicing and CTC, agentic commerce | thin (4 of 22 A/B) |
| [transfer-pricing](modules/transfer-pricing.md) | Policy, agreements, benchmarking, local and master files, operational TP, audit defence, APAs; A/B entries are rules-based automation | thin (3 of 22 A/B) |
| [controversy](modules/controversy.md) | Notices, exams, Appeals and litigation from the taxpayer side, plus tax authorities' AI; nearly all A/B entries are authority-side | moderate (10 of 25 A/B) |
| [research-advisory](modules/research-advisory.md) | Research, memos, written advice, planning and M&A tax diligence; firm and in-house buyers. Speed figures are practitioners' estimates in vendor case studies | moderate (11 of 25 A/B) |
| [data-technology](modules/data-technology.md) | In-house tax data layer, automation and its sustainment, real-time reporting interfaces, MCP access, the tax technology team. Some B entries are not AI | moderate (8 of 24 A/B) |

Professional responsibility (Circular 230, section 7216, PCRT, TPB, Werfel) sits in [guardrails.md](guardrails.md).

## Journey-stage markers (tax)

Stage names and gates follow [onboarding.md](../../method/onboarding.md) §5. Place each scope (team, practice, firm or
department) by markers you can see or count, not by self-rating.

| Stage | Markers in a tax practice or department | Ready for the next stage when |
|---|---|---|
| **Curious** | No AI policy, or a ban, while staff use public tools (more than a third of tax and audit professionals admit unauthorized tools) [TR-FOP-2026]; nobody has read OPR Alert 2026-19 against the firm's procedures [IRS-OPR-2026]; in house, the department is not using GenAI (67% of 288 in 2025) [TR-CORPTAX-2025] | A written rule covers client and return data, section 7216 consent and approved tools; named people use AI weekly on real work |
| **Experimenting** | Seats of a research tool or enterprise assistant; a pilot on one extraction task (W-2s, K-1s, notices) with re-keying as fallback; citations checked by hand after a scare; usage counted but no target (12.5% of 176 indirect tax leaders in a vendor survey have AI targets or KPIs) [FONOA-2026] | One workflow has an owner, a baseline (hours per return, review notes, notices), a written review step and a vetted tool |
| **Adopting** | AI inside production tax software; firm procedures, training and a record of AI use and verification, as OPR's section 10.36 reading expects [IRS-OPR-2026]; engagement letters and consent cover AI; fee basis reviewed | Two or more workflows in production; the second reused the first's data feed or review checklist; value recorded in one place; a named owner for tax AI |
| **Scaling** | Agents across workflows on a shared platform with human review (PwC's K-1 and diagnostics agents) [PWC-MEGNA-2025]; a governance body and risk register; a tax data layer; tax engines exposed to company agents | Value shows in margin, capacity or penalties avoided, and leaders ask what to sell or stop doing |
| **AI-native** | Practice or function built around agents with people on exceptions and signatures; AI-native roll-ups [MULTIPLIER-2025; CRETE-REUTERS-2025]; value or fixed pricing on AI-shortened work | Re-diagnose at each review. No organization has published a measured cost or quality advantage |

**In-house check.** Ownership is the usual gap: in a room of more than 50 at TEI's 2026 technology seminar, two said tax
owns AI implementation (a reporter's account) [TEI-TAXTECH-2026]. **Delegation.** Plan delegated work only at Adopting
or later, behind the five gates in onboarding §5. The tax reference case is an agent drafting an individual or trust
return from source documents into the firm's tax software for a CPA to review and sign
(compliance-individual-business `#05`; figures vendor-published).

## Files in this archetype

| File | Read when | What it gives you |
|---|---|---|
| [interview-guide.md](interview-guide.md) | Onboarding, and on entering each phase | Tax wording, module chooser, boundary probes, phase and in-house questions, vocabulary |
| [value-chain.md](value-chain.md) | Map; choosing focus modules; unit breakdown | Stages, processes and key steps with work types, linked to modules; the data layer |
| [economics.md](economics.md) | Frame; Make the case; fees, budgets or ownership | Revenue, pricing models, fees, costs, offshoring, private equity, in-house budgets, AI pricing pressure |
| [state-of-ai.md](state-of-ai.md) | Onboarding (evidence early); Frame | Surveys (corrected), what is in production versus announced, quality evidence, maturity spread |
| [frontier.md](frontier.md) | Frame (why now); Reimagine lens 4; Plan dates | Dated signals for the next 12-36 months and what each means for a leader |
| [guardrails.md](guardrails.md) | Frame constraints; Reimagine fit checks; Make the case risks | Circular 230, section 7216, PCRT, TPB, courts, insurance, fees, steps that need a person |
| [workforce.md](workforce.md) | Role evolution; capacity choice; any fear for roles | Roles, pipeline, pyramid, offshoring, new hybrid roles, the apprenticeship question |
| [disruption.md](disruption.md) | Unit or organization scope; Frame exposure; lens 4 | Business-model scenarios with evidence status and signals to watch |
| [objections.md](objections.md) | When the user pushes back | Cross-cutting objections with evidence-based responses |
| [sources.md](sources.md) | To resolve a source key, or to plan more research | The source landscape and the shared source list |

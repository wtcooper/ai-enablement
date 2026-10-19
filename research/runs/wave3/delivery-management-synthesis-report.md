# Synthesis report: professional-services / delivery-management

Prepared 2026-10-19. Outputs:
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/delivery-management.md` (300 lines, table of contents)
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/delivery-management.yaml` (16 entries)

`scripts/validate.py`: 0 errors. It warns that the YAML has 7 of 16 entries graded A/B (44%), below the 50% target.
The grades were not raised to meet it (see §4). Every source key in the module is in the YAML or in the module's
Sources section, and every inline key in each YAML entry is in that entry's `sources` (checked by script). No
downloads were needed.

## 1. Counts in and out

| Input | Candidates |
|---|---|
| ps-delivery-management-practice.md | 16 (B 8, C 7, D 1; its own grades) |
| ps-delivery-management-discourse.md | 14 (B 1, C 9, D 4) |
| ps-delivery-management-governance.md | 13 (B 1, C 8, D 4) |
| Routed in from other deep dives | 8 items (see §6) |
| **Total in** | **43 candidates + 8 routed items** |
| **Out** | **16 use cases** (A 0, B 7, C 6, D 3) |

Five governance candidates and one discourse candidate were not kept as entries, because finished entries in other
modules already describe the same change (see §2, last table).

## 2. Duplicates merged

| Out | Title (short) | Merged from (P = practice, D = discourse, G = governance) |
|---|---|---|
| 01 | Plan, solution design and handoff brief from SOW and deal record | P05, P06, D04, G05 |
| 02 | Meeting capture into summaries, actions, requirements | P04, D08, G04 |
| 03 | Status reports and steering packs | P01, D01; G07's verification and disclosure points kept as guardrails |
| 04 | Plain-language status and budget questions over PSA/ERP data | P03, G02, D14 |
| 05 | Agents flag slippage, missing time, discrepancies, health risk | P07, D02, D03, G01 |
| 06 | Scope-drift detection and change-order prompts | P08, D05; scope-scan part of G01 |
| 07 | Margin, burn and forecast monitoring | P11, D06, P10 |
| 08 | Agent project manager keeps plan current | P14; SDTIMES-PLANVIEW-2026 and SILICONANGLE-CERTINIA-2026 routed in |
| 09 | Idea: reminders, calendar, tool setup | D09 |
| 10 | Idea: predictive dependency and risk monitoring | D10 |
| 11 | Matter run from a template: tasks, review gates, status | P09, D07, G03, G13 |
| 12 | Self-built PMO agent estate (Automation Consultants) | P02; ITBRIEF-KANTATA-2026 routed in |
| 13 | Agents take on repeatable implementation tasks (Basware) | D13, P16 |
| 14 | Engagement leads run human-plus-agent teams (Thoughtworks) | P12 |
| 15 | Retrospective drafting | P15, G06 |
| 16 | Idea: engagement economics that count AI and agents | D11, P13, G11 |

Candidates held by finished entries elsewhere (cross-referenced, not duplicated):

| Candidate | Held by |
|---|---|
| G07 client deliverable drafting with disclosure and a source-verification gate (Deloitte Australia) | professional-services-work-production-11 and -25; guardrail kept in 03 |
| D12, G08 matter-level AI value reporting to clients | professional-services-scoping-pricing-09; logging in professional-services-work-production-24 |
| G12 in-house external-counsel AI metrics programme (idea) | professional-services-scoping-pricing-09 and -11 |
| G09 engagement-level AI-use register (idea) | professional-services-work-production-25 and -24 |
| G10 client AI-instruction register (idea) | professional-services-acceptance-risk-11; professional-services-work-production-25 |

Other overlaps handled by note, not by dropping: Spaulding Ridge (01) and Diabsolut (02) results also appear in
professional-services-scoping-pricing-01 as scoping documentation (one deployment each, not two); Harvey
orchestration (11) keeps the task and status layer, with agent execution in professional-services-work-production-15;
law-firm budget alerts (07) overlap professional-services-scoping-pricing-08. Cross-archetype links:
tax-compliance-individual-business-15 (status messages), assurance-soc-attestation-07 (client portal),
assurance-planning-risk-assessment-22 (budget planning), security-ai-security-06 (agent identity).

**Source-key harmonisation.** CERTINIA-PROVING-2026 became CERTINIA-CUSTOMERS-2026 (same URL, key already used in
scoping-pricing). KANTATA-EXPERTAGENT-2026 became KANTATA-AGENT-2026 (same URL; the key the staffing and
knowledge-management dives use). EINFORMATICA-SAINIO-2026 became EINF-2026 (same paper; discourse read the full PDF,
governance only the abstract). The practice dive used EC-AIACT-2026 for the Annex III reproduction on
artificialintelligenceact.eu; that page is now EU-AIACT-ANNEX3-2024, and EC-AIACT-2026 stays the Commission page
(the key the security archetype uses). Types aligned with finished files: CALBAR-GENAI-2026 regulator (2026-05-14),
KANTATA-RMI-2026 and DELTEK-CLARITY-2026 survey, SPI-AI-2026 dated 2026-10, CERTINIA-VEDA-2026 dated 2026-10 (read
date), CERTINIA-CUSTOMERS-2026 dated 2026-09 (page shows 3 September with no year).

## 3. Coverage by ladder and change scope

| | step | process | model | total |
|---|---|---|---|---|
| assist | 1 (04) | 0 | 1 (16) | 2 |
| augment | 5 (01, 02, 03, 06, 15) | 3 (05, 07, 11) | 0 | 8 |
| automate | 1 (09) | 0 | 0 | 1 |
| delegate | 0 | 5 (08, 10, 12, 13, 14) | 0 | 5 |
| total | 7 | 8 | 1 | 16 |

- **Automate** has one entry, a grade D idea from practitioners (09). No source describes a delivery step with no
  person on the normal path.
- **Delegate** has two grade B entries: Automation Consultants' self-reported agent estate (12) and Thoughtworks'
  role design in job postings (14). The rest are announcements (08), plans (13) or an idea (10).
- **Model** has one grade D idea (16). Productised or subscription delivery is in scoping-pricing
  (professional-services-scoping-pricing-22); no delivery-management source describes a model change in use.
- No entry was invented to fill a cell.

## 4. Grade mix and grading decisions

Final: A 0, B 7 (01, 02, 03, 04, 05, 12, 14), C 6 (06, 07, 08, 11, 13, 15), D 3 (09, 10, 16; all titled "Idea").
A/B share 44%. No source reports a measured delivery-management outcome from a named organization, so no A.

Decisions that differ from at least one input:
- **13 (Basware) is C, not practice's B.** The release says Basware is expanding into these areas; the billing dive
  reads the related Agent Studio quote as intent. Maturity piloting.
- **03 (status reports) is B, not discourse's C.** Nextview is a named deployment, qualitative only; PwC's figures
  are projections for an offering with no client named.
- **05 (monitoring) is B but piloting.** B rests on one Siemens sentence; practice said in-production, discourse
  piloting (Certinia's December 2025 early-adopter programme). The conservative maturity was kept.
- **01 is B on Spaulding Ridge only** (an executive's estimate, B under the 2026-10-17 rule); the handoff part alone is C.
- **06 change scope is step** (discourse said process): no source shows a redesigned change-control flow in use.
- **11 ladder is augment** (discourse said delegate): this entry covers routing and status, where people approve
  every gate; the agent-execution side is delegate in professional-services-work-production-15.
- **16 change scope is model**, following practice (agents as team members change who does the work); discourse and
  governance rated their parts process.

## 5. Gaps

- **No quality evidence.** No error, override, correction, false-alarm or parallel-run rate for AI status reports,
  plans, health scores, scope flags or forecasts in any of the three dives.
- **No measured outcome from a named organization.** Every figure is vendor-published or self-reported.
- **Law and accounting.** No named law firm, legal department or accounting firm uses AI for matter planning, status
  or budget tracking in public; Harvey orchestration is announced and BigHand and Planning Blox are listings.
  Accounting engagement management is missing outside the assurance and tax archetypes.
- **Consulting majors.** McKinsey, BCG, Bain, Deloitte, EY, KPMG and Accenture published nothing reachable on AI in
  delivery management; PwC and Deloitte appear only as an offering page and a marketplace listing.
- **Change control.** Only vendor guides and Certinia's "scope scan" wording.
- **Practitioner voice.** One Finnish interview study (12 IT project managers), one newsletter, conference write-ups
  from one publisher (Thomson Reuters Institute). Reddit was blocked; PMI pages returned 403.
- **In-house.** EarthWise Pet, Siemens Digital Industries and Basware are in-house services teams; in-house legal
  delivery management is a Legalweek session title only.
- **Scheduled, not given:** the 2026-10-20 Basware and Kantata session and the 2026-10-21 PMI Global Summit.

## 6. Routed items

**Routed in to delivery-management and how they were used**
- Kantata Agent Studio and Certinia's agents for project administration (ITBRIEF-KANTATA-2026;
  SILICONANGLE-CERTINIA-2026, from billing-collections discourse): used in 08 and 12.
- Planview Agent Resource Management, PM and backlog agents (SDTIMES-PLANVIEW-2026, from staffing practice): 08, 16.
- Kantata portfolio-health monitoring and Certinia project and PMO agents (KANTATA-AGENT-2026; CERTINIA-VEDA-2026,
  from knowledge-management, staffing and quality-review): 01, 05, 08, 15.
- Harvey Legal Work Orchestration task, status and gate mechanics (from work-production, scoping-pricing,
  staffing and quality-review): 11.
- Certinia PMO Quality scope scans and Ayora budget alerts (from scoping-pricing): 06; Ayora left in
  professional-services-scoping-pricing-08.
- Rocketlane Timesheet Policy Agent (ROCKETLANE-2026, from staffing discourse): not used; it is a staffing guide and
  timesheet compliance belongs to billing-collections.
- In-house intake triage and work allocation between in-house and outside counsel (DOCUSIGN-LEGALOPS-2026;
  TRI-INTERDEP-2026, from staffing discourse): not used; intake is professional-services-acceptance-risk-14 and only
  the routing line was available. Worth a look when an in-house or legal-operations extension is written.
- Offshoring alongside Big Four graduate cuts (CITYAM-BIG4-2025, from talent-learning): one line in module §7.

**Routed out by the delivery-management dives, for other modules' synthesis**
- **staffing-resourcing:** Nextview staffing agent scanning 150 colleagues in seconds (CERTINIA-CUSTOMERS-2026);
  Certinia Resourcing, Work Reallocation and Shortlisting agents (CERTINIA-VEDA-2026); zeb's staffing agent that
  proposes and pre-books people (NTTDATA-ZEB-2026); Kantata proactive resourcing and the RMI study, including 52.7%
  not equipped for hybrid teams (KANTATA-AGENT-2026; KANTATA-RMI-2026); Deltek's 40% better time-to-hire claim
  (DELTEK-POLARIS-2026); 66% turned down work because of resourcing constraints (KANTATA-SOPSI-2026); EU AI Act
  treatment of AI that manages workers (EC-AIACT-2026; EU-AIACT-ANNEX3-2024).
- **billing-collections:** Diabsolut invoice turnaround 40% faster (CERTINIA-CUSTOMERS-2026; distinct from the
  invoice-ageing result on CERTINIA-DIABSOLUT-2026); conversational time capture and missing time-card flags
  (CERTINIA-VEDA-2026; IA-CERTINIA-2025; KANTATA-SUPERAGENT-2026; DELTEK-DELA-2026); zeb's timesheet agent
  (NTTDATA-ZEB-2026); Legora-Laurel time capture (LEGORA-LAUREL-2026); pre-bill review against outside counsel
  guidelines as a concept (ILTA-RISE-2025); ABA and California rules on AI costs as overhead or expense.
- **scoping-pricing:** Diabsolut's move to fixed-fee, outcomes-based contracts; Neocol's SOW workflow live in nine
  days (CERTINIA-CUSTOMERS-2026); 75% expect more outcome-based pricing (CERTINIA-GSD-2026); BigHand's survey of
  pricing for AI-augmented work (AL-BIGHAND-2026); client AI line items and "will not pay" guidelines
  (TRI-LEGALWEEK-2026); buyer-side view on fixed-fee and milestone billing (BRIGHTFIELD-2026); subscription products
  (MARKETSCALE-2026); pricing map (STANFORD-DEL-2026); 87% of GCs prefer value or outcome pricing
  (LEGALBUSINESS-KPMGGC-2026).
- **pursuit-proposals:** Certinia RFP Responder and "15 times more RFPs" and SOW 8 hours to 1 (CERTINIA-SOA-2026;
  CERTINIA-VEDA-2026); Kantata Expertise Engine at FOIL (KANTATA-CONSULTANCYUK-2025).
- **client-development:** Penrod seller prep halved (CERTINIA-CUSTOMERS-2026); Basware customer success managers
  redeploying 4-5 hours a day of pre-call research (KANTATA-BASWARE-2026); Introhive agent watching relationship
  signals when a partner leaves (TRI-AGENTIC-2026); leading the client AI-ROI conversation (TRI-LEGALWEEK-2026).
- **acceptance-risk:** Legora Intake for in-house teams (LEGORA-INTAKE-2026); conflicts failure from informal
  knowledge (TRI-PREMORTEM-2026); AI clauses in engagement letters and buyer contracts (ICMCI-AICODE-2026;
  AGS-AIMODELCLAUSES-2025); professional indemnity cover (DACBEACHCROFT-PI-2026).
- **firm-finance:** Harvey Command Center adoption analytics (HARVEY-CC-2026); firm-wide ROI against rates and profit
  (TRI-SOTLM-2026; TRI-LFFI-Q1-2026); SPI's four foundations and "the leak" (SPI-AI-2026).
- **knowledge-management:** Certinia Knowledge Base and Retrospective Drafter agents; Kantata institutional memory in
  handoffs (CERTINIA-VEDA-2026; KANTATA-AGENT-2026; ERPTODAY-KANTATA-2026).
- **quality-review:** verification burden (89%, KANTATA-SOPSI-2026); review as theater (TRI-PREMORTEM-2026);
  court-filing verification and the Deloitte Australia case (ABA-OP512-2024 Part II.D; CTV-DELOITTE-2025);
  jagged-frontier evidence (HBS-DELLACQUA-2023).
- **talent-learning:** PMI AI guidance tool and certification (PMI-AI-2026); pipeline risk from automating junior
  and mid-level work (AL-LADDER-2026); NBER patent-drafting trial and TR-FOP early-career findings.
- **work-production:** BMW Group legal department rolling out Legora (LEGORA-BMW-2026, in-house); report drafting
  itself, as distinct from the verification gate.
- **No clear module:** firm-level PMOs running the firm's own AI and technology projects (TRI-PMO-ILTACON-2025;
  KK-2026; PMI-AISTD-2026). These concern internal AI rollout, not client engagements.

## 7. Suggested improvements to the briefs

1. **Give each deep dive the finished sibling YAMLs to check against before it writes.** Five of 13 governance
   candidates duplicated finished entries in work-production, scoping-pricing and acceptance-risk.
2. **Publish a shared source-key register per archetype** (URL to key, type and date). Three documents had two keys
   each across the dives, and one key pointed at two different documents.
3. **Ask practice dives for named non-vendor sources first.** Every named deployment here came through a vendor's
   customer page; a quota for firm, regulator or independent sources would show the gap earlier.
4. **Tell dives to search for job postings at several firms**, not one; Thoughtworks was the only services firm
   whose postings were read, and postings were one of the few non-vendor signals.
5. **State that a cross-module figure (the same deployment and number) may appear in two modules with a note**, so
   synthesis does not have to choose between dropping evidence and duplicating it.
6. **Set the A/B target per module from the evidence density in the landscape.** The landscape rated this module
   medium with thin case studies; a 50% A/B target invites inflation where the record is mostly vendor claims.

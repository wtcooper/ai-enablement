# Synthesis report: professional-services / acceptance-risk

- **Date:** 2026-10-19
- **Inputs:** `landscape-professional-services.md`, `ps-acceptance-risk-combined.md`, plus the "Routed to other modules"
  sections of every other `ps-*.md` file in `research/runs/wave3/` (items routed to acceptance-risk). Existing assurance,
  tax, security and professional-services YAML files were read only to cross-reference ids and align source keys.
- **Outputs:** `plugins/.../archetypes/professional-services/modules/acceptance-risk.md` (299 lines, contents list at top)
  and `plugins/.../archetypes/professional-services/use-cases/acceptance-risk.yaml` (14 entries).
- **Validator:** `python3 scripts/validate.py` gives 0 errors. It warns that the file is below its generic targets
  (15-25 entries, at least 50% A/B): 14 entries, 43% A/B. The brief's target for this module is 12-20; grades were not
  raised to meet the 50%. A script check confirmed every key cited in the module is in the YAML or in the module's
  Sources list (14 keys marked *), and every outcome `source_ref` is in its entry's sources.
- No downloads were needed; all facts come from the input files.

## 1. Counts in and out

| | Combined deep dive | Landscape | Routed from other modules | Total |
|---|---|---|---|---|
| Candidates in | 17 (0 A, 6 B, 8 C, 3 D) | 0 entries (research leads only) | 0 entries; about 25 routed evidence items from 20 files | 17 |
| Out | | | | **14 (0 A, 6 B, 6 C, 2 D)** |

**Not carried (held in the assurance archetype; cross-referenced by id instead):**

| Combined dive entry | Grade | Why not carried | Held in |
|---|---|---|---|
| 06 Grant Thornton UK selects Fenergo for KYC, CDD and acceptance | C | Same deployment and source already an entry (with the firm's own release) | assurance-acceptance-independence-03 |
| 12 Independence, conflicts and reputational signals in one acceptance decision (Kingland, Intapp accounting) | C | Audit-client independence is practice-specific; same products and pages | assurance-acceptance-independence-02 |
| 13 Independence assessment of AI tools and vendors (idea) | D | Same article (CIBA author) and same idea | assurance-acceptance-independence-13 |

Their regulator points (IESBA snapshot, PCAOB QC 1000) are kept in the module's Guardrails, and IESBA's automation-bias
point is attached to entry 02.

**Routed items used:** Oregon Formal Opinion 2026-208 (client-development governance) in 02 and 09; NYC Bar Opinion
2024-5 and the Chaffetz Lindsey ethical-screen figure (knowledge-management) in 12; Starbucks restriction (quality-review
practice), Legalweek client directives and Litera's relayed ACC figure (pursuit-proposals discourse) in 11; Coheso and
Dentsu (knowledge-management, work-production) as notes in 14; California p. 9 bias point (work-production governance) in
05; BakerHostetler and Practus (client-development, firm-finance, pursuit-proposals) already in 03 and 08; TR-FOP and
LexisNexis shadow-AI figures (work-production discourse), the SRA warning notice (talent-learning governance) and PI
insurance items (quality-review governance) in the module only.

**Routed items not used:** DOCUSIGN-LEGALOPS-2026 (only a title reached this run; no content to cite); Heppner v. Warner
privilege rulings (podcast mention, no detail); TRI-INTERDEP-2026 (work allocation, belongs to delivery or staffing);
Hg's Celeste use (deal screening, not acceptance); NYSSCPA-APS-2025 and TXCPA-APS-2026 (routed to the assurance
archetype, not here).

## 2. Duplicates merged

No two combined-dive entries described the same change, so no within-input merge was made. Entries 01 (Intapp Celeste
conflicts agent) and 17 (small-firm custom conflicts agent) were considered and kept apart: different deployment form
and evidence type (named vendor early adopter vs unnamed builder's account). Renumbered in process order:

| Out | Combined dive | Routed additions | Grade |
|---|---|---|---|
| 01 Opportunity screening | 16 | | C |
| 02 Prepopulated intake and reviewer summaries | 02 | OSB-FO-2026-208 III.C; IESBA-SNAPSHOT-2026 (from 12) | C |
| 03 Agentic conflicts search and triage | 01 | BakerHostetler routed x3 (same source) | B |
| 04 Small-firm conflicts agent | 17 | | C |
| 05 Lateral-hire pre-screen | 14 | CALBAR p. 9 bias point | C |
| 06 LLM due-diligence report (Pinsent Masons) | 05 | | B |
| 07 Idea: adverse-media agent | 07 | | D |
| 08 Risk-based acceptance workflow | 03 | | B |
| 09 Engagement letters | 11 | OSB-FO-2026-208 III.D | C |
| 10 OCG extraction (Fredrikson & Byron) | 08 | | B |
| 11 Idea: client AI-terms register | 09 | EDT-CASEPOINT-2026, TRI-LEGALWEEK-2026, LITERA-GCRFP-2026 | D |
| 12 Ethical walls for AI | 10 | NYCBAR-OP2024-5-2024, IMANAGE-CHAFFETZ-2026 | B |
| 13 Continuous monitoring | 04 | | C |
| 14 In-house front door (in-house) | 15 | AL-COHESO-2026; Dentsu cross-reference | B |

**No grade changed.** Routed items added guardrails and context only.

**Source-key canonicalisation**

| Key used | Input key | Reason |
|---|---|---|
| INTAPP-CONFLICTSAI-2026 | INTAPP-CONFLICTS-2026 (intapp.com/conflicts/) | Assurance already uses INTAPP-CONFLICTS-2026 for a different page (intapp.com/accounting/conflicts) |
| INTAPP-ONBOARDAI-2026 | INTAPP-INTAKE-2026 (intapp.com/intake/) | Assurance already uses INTAPP-INTAKE-2026 for the accounting acceptance page |
| INTAPP-INTAKE-2026 | INTAPP-ACCT-ACCEPT-2026 (accounting acceptance page) | Same document as assurance's key; assurance's last-modified date 2026-07-29 used |
| ACCWEEKLY-INDEP-2026 | CIBA-INDEP-2026 | Same article as assurance's key; typed press (input typed professional-body) |
| ACCEVERLAW-2025 | ACC-EVERLAW-2025 | Same press release as the scoping-pricing key (URL differs: blog.everlaw.com vs everlaw.com.au) |
| KINGLAND-CEA-2026 | (not carried) | Same page as assurance's KINGLAND-ACCEPT, which lacks a year; coordinator may want to fix it there |

Other key notes: ABA-OP512-2024 keeps the lawnext.com mirror URL that was opened (work-production uses the ABA URL).
CALBAR-GENAI-2026 is dated 2026-05 (other files use 2026-05 or 2026-05-14). IESBA-SNAPSHOT-2026 is dated 2026-06 here
and 2026-06-11 in assurance. The landscape's TRI-HUB-2026 summarises the premortem as 20 Feb 2026; the article itself
(TRI-PREMORTEM-2026) is dated 2026-02-18.

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | none | none | none | 0 |
| augment | 01, 02, 03, 04, 07, 10 | 06, 11, 14 | none | 9 |
| automate | 09 | 08, 12, 13 | none | 4 |
| delegate | none | 05 | none | 1 |
| Total | 7 | 7 | 0 | 14 |

- **Model: no evidence.** No source shows acceptance work changing the service or business model. The only statement
  is Intapp's conditional "10 times the matters ... new business model" line, which is not a result.
- **Assist: no separate entry.** Staff asking an assistant about client terms is part of 10. The dropped assist entry
  (AI-vendor independence) lives in assurance.
- **Delegate: one announced capability** (Celeste lateral-hire playbook, 05). No agent owns an acceptance outcome in any
  named firm.
- **Automate is mostly non-AI or announced:** 08 is workflow digitisation (B); 09 and 13 are vendor-described; 12 rests on
  one customer quote.

## 4. Grade mix

0 A, 6 B (43%), 6 C, 2 D. **No A is possible:** no named organisation reports a measured outcome for AI in this module.
The only measured figures (BDO Canada 38%, Sandberg Phoenix 3x, Loeb & Loeb) are vendor-hosted case studies of non-AI
workflow platforms, so 08 is capped at B. B entries rest on named deployments with no measurement: BakerHostetler
(forward-looking quote), Pinsent Masons (future-tense case study), Fredrikson & Byron, Nelson Mullins (undated quote),
and design partners for in-house Intake. Firm kinds: law (most), accounting (BDO Canada, BDO Australia), in-house legal;
no consulting example.

## 5. Gaps

- **No quality evidence for AI:** no error, override, false-positive or missed-conflict rate, parallel run, inspection
  finding or independent benchmark for AI in conflicts, KYC or acceptance. The only false-positive account is an unnamed
  firm's own write-up.
- **Consulting and Big Four acceptance:** no primary document found; no AI independence-check tool found.
- **Client AI terms:** no primary OCG text with AI clauses and no count of how many guidelines carry them; no firm
  describes a structured register (11 stays an idea).
- **Engagement letters:** no 2026 AI-drafted engagement-letter announcement from practice-management vendors or Clio.
- **Regulator primary text:** SRA pages blocked (figures secondary via VinciWorks); PCAOB QC 1000 acceptance provisions,
  the AICPA independence proposal and the SRA warning notice not read at source.
- **Conference content:** event listings only (Sandpiper, Swiss Re, Morgan Lewis); no recorded session or podcast.
- **Job postings:** one opened (employer not shown); three others and the Baker McKenzie posting are search-only.

## 6. Routed to other modules (collected from the combined dive)

| Item | Target | Sources |
|---|---|---|
| Deloitte Australia AI-error refund; engagement risk when the firm's own AI-assisted deliverable is the exposure; PCAOB QC 1000 as a quality-management standard; PI insurance and supervision | quality-review | CTV-DELOITTE-2025, PCAOB-QC1000-2025, DACB-PI-2026, IAMAG-LAWPL-2026 |
| CalBar's "autonomously facilitating client intake" at the website lead stage; Oregon chatbot opinion; DealCloud relationship intelligence (Wotton Kearney, Forvis Mazars Capital Advisors) | client-development | CALBAR-GENAI-2026, OSB-FO-2026-208 |
| Client demands that AI savings be shared; AI line items; "will not pay for AI-done work" | scoping-pricing | TRI-LEGALWEEK-2026, LAYER3-OCG-2026, CALBAR-GENAI-2026 |
| Billing guidelines surfaced at time entry (Intapp Time, Billstream) | firm-finance (billing) | INTAPP-TERMS-2026 |
| Lateral-hire onboarding as a people process; junior conflicts and intake staff | talent-learning | INTAPP-CELESTEGA-2026 |
| Celeste retrieval of matters, partner experience and pitch materials | knowledge-management | INTAPP-CELESTEGA-2026 |
| Intapp FY26 results (cloud ARR, new clients) | firm-finance | INTAPP-Q4-2026 |
| OCG and RFP terms flagged against standard terms during a bid (idea) | pursuit-proposals | ABA-LPMAI-2026, LITERA-GCRFP-2026 |
| Harvey, Legora and Coheso in-house intake | possible legal-operations extension (kept here as 14) | LEGORA-INTAKE-2026, HARVEY-INTAKE-2026, AL-COHESO-2026 |

## 7. Suggested improvements to the briefs

1. **Publish a shared source-key register across archetypes.** Two Intapp keys meant different pages in assurance and
   in this input, and three documents had different keys (CIBA article, Kingland page, ACC-Everlaw release).
2. **Give deep-dive agents the existing extension entries before they research.** Three of 17 candidates duplicated
   assurance entries in substance; the dive could have spent that effort on consulting and in-house gaps.
3. **Set a module-specific validator target.** The brief says 12-20 for this thin module, but the validator warns below
   15 and below 50% A/B; a per-module override would stop an honest file from looking like a failure.
4. **Say how to treat "workflow, not AI" evidence.** The only measured figures here describe non-AI platforms. A flag
   such as `ai_role: workflow-base` would keep them visible without implying AI results.
5. **Ask routed-item writers to include the claim, not only the key.** Several routed lines (Docusign legal ops, Heppner)
   gave a source key with no content, so the receiving synthesis could not use them.
6. **Fix the date rule for undated vendor pages** (access date vs last-modified date); the same Intapp page carried
   2026-07-29 in one file and 2026-10-19 in another.

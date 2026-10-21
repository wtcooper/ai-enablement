# Verification report: acquisition path and acquired-firm rollout playbook

Date: 2026-10-21. Brief: `research/runs/suite/briefs/verify-acquisitions.md`. Sources were downloaded to a private
`mktemp -d` folder. Pages that returned stubs (A&M, CAMICO, PwC, Wolters Kluwer) were read through the r.jina.ai mirror.

Files checked: `transformation-advisor/references/method/acquisitions.md`, `transformation-advisor/references/briefs/assess-target-firm.md`,
`ai-portfolio/references/method/acquired-firms.md`, `ai-portfolio/references/method/stage-gates.md` §9, the pointers in both
`SKILL.md` files, `transformation-advisor/references/method/index.md` and `ai-portfolio/references/method/index.md`.

## Counts

- **Sources cited in the files:** 34. 33 were read in full and 1 was read only in part (see below). One new source was added
  (JOFA-PEEC-2026).
- **Claims checked** (figures, dates, attributed statements, named examples, regulatory points, internal references): about 75.
- **Kept:** 49. **Fixed:** 26 (see the table; several fixes were applied in two or three files). **Removed:** 0.
- **Pointers:** the `SKILL.md` and index rows are all present and correct. The authoring report's suggested
  `ai-portfolio` index row is already in place, so nothing needed changing there.
- **Validator:** `python3 scripts/validate.py` reports 0 errors before and after the edits. All 28 warnings are in
  `archetypes/` and none are in these files.

## Fixes

| # | File(s) | Was | Now | Reason |
|---|---|---|---|---|
| 1 | acquisitions §4; acquired-firms §6 | AICPA rules: "confirm the current status" | Adds that in August 2026 PEEC was discussing further changes and a possible second exposure draft, so the rules are not final. New source JOFA-PEEC-2026 | Regulatory status was out of date as of today |
| 2 | acquired-firms §7 | Quote attributed to "an operating partner in Grant Thornton's survey" | A Grant Thornton transaction advisory partner, writing in the firm's PE survey report | Wrong speaker. The quote is the report author's, not a survey respondent's |
| 3 | acquisitions §5; acquired-firms §3 (layer 5) | Baker Tilly's CEO "expects the P&L change from rebuilt workflows" | Does not expect personal-productivity AI alone to change the P&L materially, and plans workflow-native rebuilds of tax and audit | Embellished. The source does not say the P&L change will come from rebuilds |
| 4 | acquired-firms §3 (intro, layers 1–2, trap); stage-gates §9 rule 4 | "RSM puts policy, data centralization and training ahead of use cases after close"; "Training is in RSM's first wave" | RSM treats AI policy and guardrails as a first-wave priority, and says data must be centralized and governed before AI shows meaningful results. On training, RSM says to formalize it where skills are thin | Overstated. RSM does not put training in the first wave and does not rank any of these against use cases |
| 5 | acquired-firms §5 | "Professional-liability guidance sets written-consent steps…" | The steps come from AICPA ET 1.400.205 as summarized by CAMICO. They apply when the seller keeps no ownership; the equity versus non-equity rule is stated | Misattributed (the steps are the Code's rule, not the insurer's) and the trigger was missing |
| 6 | acquired-firms §5; acquisitions §7 trap | 90-day negative consent presented without a caveat | Adds CAMICO's point that Sec. 7216 consent has no negative-consent option, so affirmative consent is the cautious course for tax-return information | A regulatory point the source makes was missing |
| 7 | acquisitions §4; acquired-firms §5 | 7216: consent for affiliates and uses beyond preparation | Adds that a third-party provider that only helps prepare or process the return needs no consent unless it makes substantive decisions | Incomplete. The source sets the two categories out side by side |
| 8 | acquisitions §2; acquired-firms §5 | Aprio and Baker Tilly describe "investors owning a separate non-attest entity" | Describes the alternative practice structure as the sources state it: a licensed CPA firm does attest work, and a separate unlicensed entity does tax and advisory work | Embellished. Neither source says who owns which entity |
| 9 | acquisitions §2; acquired-firms §2 | NJCPA cited for "fully merged platform … or a capability buy" | Platform buys smaller firms into one organization, or umbrella [NJCPA]; "capability buy" is no longer attributed to NJCPA | Claim attributed to the wrong source. NJCPA names two models and does not describe either as "fully merged" |
| 10 | acquisitions §3 dim 4 | "Who approves new tools?" cited to RSM | RSM's data-privacy question; tool approval labelled as an advisor addition | Not in RSM |
| 11 | acquisitions §4 | Red flag "Client-data handling undocumented" cited to RSM | "Data ungoverned" | RSM covers data in general, not client data |
| 12 | acquisitions §4; acquired-firms §6 | PCAOB "inspections will look at firms that have taken PE" | PCAOB officials said inspections of firms that audit public companies will focus on them | Scope (PCAOB oversees public-company auditors) and the speakers were missing |
| 13 | acquisitions §4; acquired-firms §6 | "FRC and ICAEW urge firms to engage early" cited mainly to Bloomberg Tax | ICAEW cited first. Bloomberg Tax is paywalled and its lede does not carry the claim | The claim rests on ICAEW |
| 14 | acquisitions §5; acquired-firms §2, §3; stage-gates §9 | Bain advice presented as general | "Writing about large deals" | Scope of the source (megadeals) |
| 15 | acquisitions §5 | FTI: "35% call M&A implementation efficient" | "efficient or very efficient" | Source's wording |
| 16 | acquisitions §5 | Grant Thornton finding with no provenance | Marked vendor-published, PE subgroup of 100 | Provenance label was missing |
| 17 | acquisitions §5 | "Human review remains the top requirement" | "…for high-stakes GenAI use in Deloitte's 2026 M&A study (vendor-published)" | Qualifier and provenance were missing |
| 18 | acquisitions §5; acquired-firms §4 | "40% of 1,150 workers surveyed" | Names the Stanford Social Media Lab and BetterUp Labs survey | Originator of the statistic was missing |
| 19 | acquisitions §5 (target side) | "Health-care roll-up studies found price rises after add-on acquisitions" | Anesthesia: after add-ons; gastroenterology: after PE acquisition; neither found a quality gain | The JAMA study does not measure add-ons |
| 20 | acquired-firms §7 | "80% of independent UK firms" | 80% of independent firms in ICAEW's 2025 mid-tier firms report, as cited by Accountancy Europe | "UK" is not in the citing source; secondary citation made explicit |
| 21 | acquired-firms §8 | "No source reports partner attrition … [UVA-FAR-2026]" | The research found no such figures; the UvA project notes little systematic evidence | The cited source does not say "no source reports" |
| 22 | acquired-firms §8 | Report "exceeded, met or missed through `status`" | Met or exceeded maps to `realised`; missed maps to `partly-realised` or `not-realised` | "exceeded", "met" and "missed" are not `benefits.md` status values |
| 23 | acquired-firms §9 | "Platforms pitch AI … alongside local control, capital, shared technology and upskilling" | Current, for example, pairs AI with local leadership and brand, back-office resources, financial backing and upskilling | Generalized from one source |
| 24 | acquired-firms §6 | `professional-duties.md` §4 (bare path) | Full relative path to `ai-governance` | Path did not resolve from `ai-portfolio` |
| 25 | acquisitions §10; acquired-firms §13 | WINSTON-APS-2026: "Winston & Strawn, page undated, 2026" | Winston Taylor (published as Winston & Strawn before the 2026-06-01 combination); date bounded 2025-12-29 to 2026-06-01 | The publisher's name has changed; the page date is now bounded |
| 26 | assess-target-firm.md | No provenance rule | Every figure the firm or its owner publishes about itself is labelled self-reported; vendor surveys are labelled vendor-published, with sample size | Brief requirement: self-reported platform claims must be labelled |

Kept after checking, among others: Current's 31%, up to 98% and 7,000 returns, and its "keep leadership, brand and
culture" (CPA Practice Advisor, 2026-06-03, marked self-reported); Reuters' minority stake (2025-06-04); FTI's 555, 66%,
25% and 19% versus 5%; A&M's 100, 41% and "fewer than one-quarter"; Thomson Reuters' more than one-quarter and one in
three; Wolters Kluwer's "over 40%" (vendor survey); KPMG's SaaS case; RSM's six prerequisites and "six months or less";
Winston's covered members and fund-family scope; NYSSCPA's one year after adoption; CPAI's 7216-2(n) written agreement;
JofA's $10,000 per FTE (author's estimate); NBER's 18% and 25–30%; JAMA's 4.5%; Accountancy Europe's three to seven years
and portfolio monitoring; Baker Tilly's "table stakes" and "red herring"; Newcomer's "early to assess"; the PCAOB acting
chair on paths for junior auditors. All source dates match the pages.

## Fitness for use

- **When to take the path:** covered by the §1 situation table, the `SKILL.md` Onboard sentence and the index row.
  Pass.
- **Assessment recorded as a unit:** §6 uses valid schema values (`mode: desk-review`, `status: desk-review`,
  `category: foundation`, `label: draft-to-validate`). Pass.
- **Desk drafts labelled:** the brief and §6 both say "Draft to validate", and the brief now also labels provenance.
  Pass.
- **Sequenced by dependency:** layers and `depends_on`, with no calendar deadlines. "100 days" appears only as a trap.
  Pass.
- **Consent and independence:** covered by Layer 0, acquired-firms §5 and §6, and the acquisitions red flags. Pass,
  strengthened by fixes 1 and 5–7.
- **No named individuals:** roles only throughout. The GT partner, the PCAOB officials and the CEOs are referred to by
  role. Pass.

## Sources not fully reached

- **BLOOMBERGTAX-FRC-2025:** paywalled; only the headline and lede were read. The early-engagement claim now rests on
  ICAEW.
- **Reached only through the r.jina.ai mirror** (the direct fetch returned a stub): AM-VALUECREATION-2026, CAMICO-MERGE-2022,
  PWC-AIDD-ND, WK-PE-2025.

## Open questions

- What happened at PEEC's interim meeting in October 2026: was a second exposure draft issued? Recheck before relying on
  any APS dates.
- There is still no authoritative reading of AI tools under Sec. 7216, and no guidance on shared AI services across the
  attest line. The files tell the user to take counsel's view.
- No partner or client retention data after acquisitions of accounting firms was found.
- The Deloitte pulse study's sample size is not shown on its page.
- "Capability buy" is now an advisor category with no source. Add a source if one is found.

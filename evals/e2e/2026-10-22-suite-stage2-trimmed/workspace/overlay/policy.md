---
schema: policy/v1
title: "AI policy: firm-wide (DRAFT, risk tiers started on assumptions)"
scope: { level: firm, name: "Firm-wide: audit, tax, advisory, client accounting and internal functions" }
archetype: null
regimes: [attest-independence, tax-7216, client-terms, privacy-law]
owners:
  policy: "Risk lead"
  tool_catalog: "IT/security lead"
  request_path: "To be set at step 7"
  exceptions: "To be set at step 7"
  incidents: "To be set at step 7"
backbone: null
data_classes: []
risk_tiers: [tier-1, tier-2, tier-3, tier-4]
policy_version: 1
status: draft
step_completed: 0
next_step: 1
updated: 2026-10-21
parent: null
---

# AI policy: firm-wide (draft)

**Status of this file.** Draft written by the ai-governance skill, started at step 3 (risk tiers) at the portfolio lead's request so the risk lead has something to react to. Steps 1 (baseline) and 2 (data rules) are not done, so `step_completed` stays 0. **The regimes and owners below are assumptions given by the portfolio lead, not confirmed by the risk lead or counsel. Not legal advice.** Tier thresholds, reviewers and the ladder rule are advisor defaults ("default, adjust"), kept apart from sourced requirements. No client-confidential or personal data is in this file.

## 1. Where we start (step 1)

**Professional regimes (assumed, for the risk lead to correct):**
- `attest-independence`: audit independence and PCAOB rules apply to the audit work.
- `tax-7216`: US tax-return consent rules apply to the tax work (the details are step 5).
- `client-terms`: client engagement letters restrict AI use for some clients (which ones is not yet known).
- `privacy-law`: personal-data law applies (which jurisdictions is not yet known).

Not assumed: `legal-practice`, `eu-deployer`. The risk lead should say if either applies.

**Known so far:** one approved enterprise assistant is in use on non-client material only; IT holds the licence count; there is no list of other AI in use and no written switch-off. The audit plan records that no tool is approved for client evidence and that a client-data approval takes 3-4 months.

Tools in use, existing policies, owners and gaps: not yet gathered (step 1).

## 4. Risk tiers and human review (step 3, draft)

**Standard for every tier (sourced).** Same diligence as if AI were not involved, and the user stays accountable. Firms told PCAOB staff that AI is expected to augment, not replace, people, and that reviewers apply the same diligence as without AI [PCAOB-GENAI-2024, pp.4-5].

| Tier | Uses (default, adjust) | Who reviews | What the reviewer checks | Record needed | Autonomy allowed |
|---|---|---|---|---|---|
| `tier-1` Internal, low consequence | Admin, internal drafts, brainstorming on public or firm-internal data | The user | Reads the output before use | Tool logs only | Assist |
| `tier-2` Informs professional work | Research notes, analysis, template and wording drafts a professional then uses; non-client material; supervision unchanged | The user, then the normal reviewer as usual | Sources and figures verified at source; nothing client-specific pasted | Light: tool used and what was checked | Assist, augment with a person in the loop |
| `tier-3` Client-facing or relied on | Deliverables, advice, client communications, anything leaving the firm | A named qualified reviewer | Facts, figures and every citation against its source before release | Input description, how verified, who reviewed [CPAI-2026] | Augment; a person sends or signs |
| `tier-4` Regulated or high-impact | Audit procedures and evidence, signed tax returns and filings, court submissions, decisions about people, agents acting on client data or outside the firm | Use-case approval record before use, then a named reviewer with written instructions | Test results on firm samples; regime steps (step 5); reviewer owns exceptions and conclusions | Tier 3 plus tool and model version, configuration, why use was appropriate, approval, how the output informed the conclusion | Assist or augment only until test evidence and the delegation gates support more |

**How the assumed regimes shape the tiers (default, adjust)**
- **Audit independence and PCAOB.** Performing audit procedures or handling audit evidence with AI is `tier-4`. If the firm builds, hosts or shares an AI tool with an attest client, run the independence analysis before use (step 5).
- **US tax-return consent.** Any AI step that touches tax return information needs the consent question settled first (specific to the use or boilerplate; processes data or applies the law). Preparing or signing returns is `tier-4`; tax research and drafting that stays inside the firm is `tier-2`; a deliverable that leaves the firm is `tier-3`.
- **Client engagement-letter restrictions.** A client instruction that restricts AI overrides the tier: the use is not permitted for that client whatever the tier. Needs a list of clients with such terms (step 1).
- **Personal-data law.** Personal data in a prompt raises the minimum tier to `tier-2` and needs a data-class rule (step 2). Uses for recruitment, terms of work, task allocation by behaviour or monitoring and evaluating staff are `tier-4` as an advisor default, following the EU AI Act's Annex III list [AIACT-EXPL-2026, Annex III point 4]; the high-risk obligations are dated 2 December 2027 under Regulation (EU) 2026/1744 [EU-OMNIBUS-2026]. Re-verify before relying on dates, and ask counsel whether that Act applies at all.

**Not permitted until approved (default, adjust)**
- Any AI on client evidence or client data in a tool without an approval record (today: all of them; the enterprise assistant is limited to non-client material).
- Performing audit procedures with AI.
- AI on tax return information before the consent question is settled.
- Agents acting on client data or outside the firm.
- AI in decisions about people.
- Personal or consumer accounts for any firm or client work.

**Rule for autonomy (default, adjust).** Each move up the ladder (assist, augment, automate, delegate) raises the tier by at least one level until test evidence supports lowering it. `delegate` is always `tier-4` and must pass the five delegation gates. A tier is set for the use, not the tool; the catalog's `max_risk_tier` is a ceiling.

**Pattern map for the patterns in the portfolio (default minimum tiers)**

| Pattern | Minimum tier | Reviewer must own |
|---|---|---|
| `draft-review-loop` | `tier-3` for client deliverables | Sign-off before anything leaves the team |
| `intake-triage` | `tier-2`; `tier-3` if it routes client requests | Spot checks; the exception queue |
| `reconcile-exceptions` | `tier-3`; `tier-4` in attest work | Clears unresolved breaks; investigates and concludes on exceptions |
| `end-to-end-case-agent` | `tier-4` | Checkpoints at key decisions and before anything irreversible |

### Proposed tier by portfolio item (assumptions for the risk lead to correct)

Not written into `portfolio.yaml`. The portfolio's `risk_tier` stays empty until the risk lead has reacted to this draft.

| Item | Proposed tier | Why |
|---|---|---|
| `sox-prereview-checklist`, `sox-request-template`, `sox-report-register` and the integrated variants | None (no AI); `tier-2` at most if the enterprise assistant drafts wording on non-client material | Process changes; the back-test reads past client files inside the firm, which the risk lead should confirm is permitted |
| `sox-chase-assistant` (Hold) | `tier-3` | Drafts messages that leave the firm to client control owners; a person sends every message; placeholder text only |
| `ct-int-nonclient-drafting` (provisional) | `tier-2` | Templates and wording on non-client material that staff then use in workpapers |
| `sox-client-data-approval` | Not a tiered use | It is the approval route; its output is the tier-4 use-case approval record |
| `sox-listing-tool`, `ct-int-listing-compare-draft` | `tier-4` | Client evidence in audit procedures; exceptions and conclusions stay with a person |
| `sox-ai-secondary-review`, `ct-int-ai-secondary-review` | `tier-4` | Reviews audit workpapers; client evidence |
| `sox-agent-testing` | `tier-4` | `delegate` level; fails four of the five delegation gates today |
| `sox-platform-plus-review` | `tier-4` | Service-model change in attest work; independence and fees to examine first |
| `firm-enterprise-assistant` | Ceiling `tier-2` (catalog `max_risk_tier`, when the catalog exists) | Approved for non-client material only |

### Questions for the risk lead and counsel

1. Which of the four assumed regimes actually bind the firm, and do `legal-practice` or `eu-deployer` apply?
2. Which clients' engagement letters restrict AI use, subcontracting or data location, and where is that list kept?
3. For tax: is client consent specific to the AI use or covered by the engagement letter, and which AI steps only process data versus apply the law?
4. Does using AI on past client files inside the firm (the checklist back-test) need any consent or notice?
5. Should a client-facing message drafted by AI (the chase assistant) be `tier-3` with the sender as the named reviewer, or is that too heavy for placeholder-text drafting?
6. Who owns the policy, the catalog, the request path, exceptions and incidents? The owners above are placeholders.

## Remaining sections

Sections 2 and 3 (acceptable use, data classes and tool tiers), 5 (records of AI use), 6 (profession-specific duties and client consent), 7 (vendor and tool evaluation) and 8 (requests, review and maintenance) are not written. Next step: step 1, the baseline.

## Sources

- **AIACT-EXPL-2026**: Future of Life Institute, *EU AI Act Explorer: Annex III* (annotated regulation, accessed 2026-10-20). https://artificialintelligenceact.eu/annex/3/
- **CPAI-2026**: CPAi, *Drafting an AI Policy that Actually Works* (professional association guide, 2026-07). https://www.cpai.com/Education-Resources/My-Firm/Data-Security-Risk-Management/Drafting-an-AI-Policy-that-Actually-Works
- **EU-OMNIBUS-2026**: European Parliament and Council, *Regulation (EU) 2026/1744 amending Regulation (EU) 2024/1689* (regulation, 2026-07-08). https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng
- **PCAOB-GENAI-2024**: PCAOB staff, *Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting* (regulator staff, 2024-07). https://pcaobus.org/documents/generative-ai-spotlight.pdf

## Approvals and change log

| Version | What changed | Approved by (role) |
|---|---|---|
| 1 | Draft risk tiers started on assumed regimes | Not approved |

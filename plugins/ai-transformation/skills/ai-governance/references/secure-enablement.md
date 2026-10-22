# Secure enablement (step 7)

Read this on entering step 7. It moves IT, security and risk from blocking to providing approved tools with a fast
request path, built-in controls and clear owners, and it closes the policy. Sources are in §8.

## 1. Goal and exit criteria

**Goal.** Governance people use instead of going around. The University of Melbourne and KPMG authors say their
findings suggest bans may be ineffective and that a policy does not guarantee compliance [KPMG-MELB-2025, p.75].

**Exit when all of these are true:**
- **An AI lead or committee** with named jobs; **a request path** with lanes, a stated response commitment and an
  expedited lane (minimum controls, logged exceptions).
- **Re-approval triggers and a review cadence;** **exceptions and incidents** (who grants, how logged, how to report,
  correct, disclose and re-review); **training and acknowledgement** by role; **measures** the owner will report.
- **The policy marked ready for approval** (`status: in-review`) and the guardrails file consistent with it.

## 2. How to run it

1. **Name the AI lead or committee** (move 1). In a partnership, put respected, business-minded practice leaders on
   it, not only IT: partners are owners, so the lead has influence rather than authority.
2. **Design the request path** (§5) and ask what response time the owner can commit to and keep; never invent one.
   Design the expedited lane from S2: urgent work is the usual bypass (`references/policy-and-data.md` move 3).
3. **Build controls into the tools** (move 2); set triggers and cadence (move 3); write exceptions and incidents (§5).
4. **Set training** (move 5) with ai-enablement and agree the measures; then play back the whole policy and write §7.

## 3. Question bank

| # | Question | Scope |
|---|---|---|
| S1 | Who owns the tool catalog, the request path and the response commitment? | [O] |
| S2 | What did the last urgent deployment skip? | [U/O] |
| S3 | Which controls can the approved tools enforce themselves: single sign-on, logging, retention, data-loss prevention? | [U/O] |
| S4 | What are our re-approval triggers, and how often do we review the policy and the catalog? | [O] |
| S5 | What training and acknowledgement will each role complete before access, and how will we sample compliance? | [O] |

## 4. Expert moves

1. **Give the AI lead five jobs:** review use cases, approve tools, maintain the policy, monitor compliance, handle
   incidents [CPAI-2026].
2. **Build the controls into the tool:** single sign-on, logging, retention and data-loss prevention do the work staff
   memory cannot, and the inventory includes AI inside approved software (`references/baseline.md` move 5).
3. **Re-run the assessment on a schedule and on triggers.** Microsoft's own responsible AI standard requires impact
   assessments to be updated at least annually, when new intended uses are added, and before a release stage advances
   (a named company's internal standard, used as a template) [MSFT-RAI-2022, A1.3].
4. **When a leader says governance is optional, point to the duty floor:** ABA Opinion 512 says managerial lawyers
   must establish clear policies on permissible AI use and supervise it [ABA-OP512-2024]. After an AI error, correct,
   disclose and re-review the wider set
   (`../../transformation-advisor/references/archetypes/professional-services/guardrails.md` §7).
5. **Make training a condition of access,** with examples of what cannot be entered and how to redact [CPAI-2026].

## 5. Defaults and decision rules

**Request path (advisor default):**

| Lane | Qualifies when | What happens |
|---|---|---|
| Fast | Public or firm-internal data, tier-1 or tier-2 use, an existing catalog entry | Approved against the entry's conditions; logged |
| Standard | A new tool or tier, or client-confidential data | Scorecard (`references/vendor-evaluation.md`), screens, decision |
| High-tier | Tier-4 use, regulated data, agents, or a regime flag | Use-case approval record, own-sample test, regime review (step 5), then a pilot |

**Request form fields:** tool, tier and contract; use and audience; data classes; runtime class and permissions; regime
flags (tax-return information, attest client, legal matter, client terms, EU staff decisions); requester's role.

**Re-approval triggers (advisor default):** model change · sub-processor change · terms change · new data class · new
use · incident [NIST-600-1-2024, GV-1.6-003, GV-6.1-005, GV-6.1-009].

**Exceptions:** granted only by the named role; logged centrally with reason, scope and expiry; an unowned exception
is a gap. **Incidents:**
one report route; correct, disclose where duties require, re-review the wider set; near misses go to the incident owner.

**Measures (advisor default):** staff who can name the approved tool; request volume and turnaround; exceptions;
incidents and near misses. Use the firm's own numbers, never other organizations' survey figures.

**Across units:** one catalog, matrix, incident process and inventory; unit addenda only for regimes (rule 13).

**Decision rules**
- A ban with no approved alternative and no request path is not a finished policy [KPMG-MELB-2025, p.75].
- Usage tracking states its purpose and never rates individuals (core rule 1): KPMG is reported to call its monitoring
  not discipline while adding AI use to performance assessments (trade press, secondary) [IAB-KPMG-2025].

## 6. Worked example

Illustrative. A consulting firm's committee (two practice leaders, IT security, the general counsel) runs the three
lanes. For a client deadline, the expedited lane allows approved entries only, tier-3 review, the exception logged.

## 7. Output

Write section 8 of `overlay/policy.md`; fill every `owners` field; set `status: in-review`, `step_completed: 7`,
`next_step: null`. Set `owner` and `request_path` in `overlay/tool-catalog.yaml`. Regenerate `overlay/guardrails.md`
to match the policy, then offer the handoffs in `SKILL.md`.

## 8. Sources

- **ABA-OP512-2024**: American Bar Association, *Formal Opinion 512: Generative Artificial Intelligence Tools* (professional body, 2024-07-29). https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
- **CPAI-2026**: CPAi, *Drafting an AI Policy that Actually Works* (professional association guide, 2026-07). https://www.cpai.com/Education-Resources/My-Firm/Data-Security-Risk-Management/Drafting-an-AI-Policy-that-Actually-Works
- **IAB-KPMG-2025**: International Accounting Bulletin, *KPMG to include AI performance reviews* (trade press, secondary, 2025-11-03). https://www.internationalaccountingbulletin.com/?p=44130
- **KPMG-MELB-2025**: University of Melbourne with KPMG, *Trust, attitudes and use of artificial intelligence: A global study 2025* (academic with consultancy, 2025-05). https://kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf
- **MSFT-RAI-2022**: Microsoft, *Microsoft Responsible AI Standard, v2, General Requirements* (named-company internal standard, 2022-06). https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf
- **NIST-600-1-2024**: NIST, *AI RMF: Generative AI Profile, NIST AI 600-1* (standard, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

### USER
The integrated-audit manager has validated `ct-int-nonclient-drafting`. Record `g0` as a Go into discover: the manager's time, released by the practice leader. Then take it to ai-solution-delivery: frame it, decide build versus buy, and open the brief as `g1` evidence.

### TOOLS
- Skill: ai-transformation:ai-portfolio Record g0 (Go into discover) for ct-int-nonclient-drafting
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/portfolio.yaml
- Skill: ai-transformation:ai-solution-delivery Frame ct-int-nonclient-drafting, decide build vs buy, open the brief as g1 evidence. Item is in discover (g0 Go recorded).
- Write: solutions/ct-int-nonclient-drafting/brief.md
- Write: /tmp/claude-0/-home-user-ai-enablement/807fbf4d-3850-5c6c-82b1-8d3750715cd5/scratchpad/check_yaml.py

### ASSISTANT
I've recorded `g0` as a Go and opened the brief, but I couldn't run the YAML parse check on either file. The check needed approval, which I didn't get. I wrote every free-text value in quotes, but please parse both files before you rely on them.

**`g0` for `ct-int-nonclient-drafting`: Go into discover**
- **Decider:** the portfolio lead decides on the light path, with the practice leader consulted. I recorded it under that role on your word that the manager validated the item.
- **Resources:** the integrated-audit manager's time for discovery, released by the practice leader. Data is non-client templates and synthetic cases only.
- **Budget:** you named none, so I wrote "none requested; runs on the existing assistant (to confirm with the finance lead)". Correct that if it's wrong.
- **Conditions:** restate the usage rule, and have a senior review the synthetic examples before shared use.
- **Kill criteria:** four, including client data found in prompts, and the manager's time not held or no benefit owner named by `g1`.
- **Next gate:** `g1`, with the light path's combined `g1`/`g2`. I put six evidence rows, each marked "not presented", in the intake record's evidence table.
- **Files changed:** the item in `portfolio/portfolio.yaml` is now `discover` / `active` with `solution` set, and I removed the `provisional` flag. I also updated its intake record in `portfolio/intake/` and the header comment and `state` in `portfolio.yaml`.

**Brief: `solutions/ct-int-nonclient-drafting/brief.md`**
- **Framing:** this is a `draft-review-loop` at the `assist` rung, on the `personal-assistant` runtime class.
- **Sourcing leaning:** configure the approved enterprise assistant, with no build and no new tool. A template-library-only option, with no AI, is the baseline to try first.
- **Steps 1 and 2 are not ticked.** The baseline (reported 1.5 h, 0–15%, no time record) and the leaning both rest on reported figures, and no one has run an own-sample test. The benefit owner hasn't confirmed the metric either, and I didn't want to present guesses as decisions. The brief's decisions log marks both decisions "proposed", for the business owner to confirm.
- **Junior-learning risk:** the pattern file warns against using this where drafting is how juniors learn. The brief handles it by having juniors critique AI drafts and keep a manual rotation.

**Open points**
- The item's category is still "quick win", but the screen rules would park an item with value 2. I left it for the forum to confirm.
- There is no `overlay/tool-catalog.yaml`, and the risk tier in the draft policy is unapproved. The brief hands tier and catalog entry to **ai-governance**, which I haven't run.
- Seven open questions are listed at the bottom of the brief. The first is who the benefit owner is. The second is the time-record baseline.

### USER
Benefit owner is the integrated-audit manager's practice leader, and the time-record baseline is something I can get from the practice's timekeeping system. Please run ai-governance now to set the risk tier and the tool-catalog entry for the approved assistant. Then confirm the brief's two proposed decisions with those answers and park the quick-win category question for the forum.

### TOOLS
- Skill: ai-transformation:ai-governance Set the risk tier for ct-int-nonclient-drafting and write the tool-catalog entry for the approved enterprise assistant (non-client material only).

### ASSISTANT
Before I write the catalog entry, a reminder: don't paste client-confidential or personal data into this session. Product names, tiers and data classes are all I need.

The tier is the easy part. The draft policy already proposes `tier-2` for this use: wording and templates on non-client material that staff then use in workpapers, with the assistant capped at non-client material. I'll record it as proposed, because only the risk lead can confirm it.

The catalog entry needs facts that aren't in any file, and I won't invent them. There is no `overlay/tool-catalog.yaml` yet, and the draft policy has no data classes or contract details.

**What is the approved assistant's product and tier as the firm names it, and what contract or terms was it approved under?** For example, "Business tier, enterprise terms with a data processing addendum". If the answer is on a vendor page or IT record, the name and tier are enough for now.

### USER
It's the firm's enterprise assistant on the business tier, approved under enterprise terms with a data processing addendum. It doesn't train on our inputs, and it's approved for internal and non-client material only. For this item, record client data as not permitted, and note that the risk lead still has to confirm the tier and the catalog entry.

### TOOLS
- Write: overlay/tool-catalog.yaml
- Edit: overlay/policy.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md

### ASSISTANT
The tier and the catalog entry are recorded as drafts, and the brief's two decisions are confirmed as direction only. I didn't run a YAML parse. Earlier attempts to run my check script needed approval, so please parse `overlay/tool-catalog.yaml` and `portfolio.yaml` before relying on them.

**Risk tier and catalog (ai-governance)**
- **Tier:** `overlay/policy.md` now shows `tier-2` for this item as "proposed; the risk lead has not confirmed it", with client data not permitted. The item's `risk_tier` stays `null` in `portfolio.yaml` and the brief until the risk lead confirms it.
- **Catalog entry:** I created `overlay/tool-catalog.yaml` with one entry, `enterprise-assistant-business`. It is the business tier on enterprise terms with a data processing addendum, with `data_classes: [public, firm-internal]` and `max_risk_tier: tier-2`. Its conditions are non-client material only, no training on the firm's inputs, and review by the professional who relies on the output.
- **Status:** I set it to `under-review` because the risk lead hasn't confirmed it. Other skills treat that status as outside the catalog and flag it. The status flips when the risk lead confirms.
- **Gaps:** I left out vendor, model, regions, retention, user groups and the vendor file because I don't have them. The contract and no-training term are marked as reported, not checked against the signed contract. The request path and exit plan are placeholders for later governance steps. The file header lists all of this.

**Brief decisions**
- **Decision 1 (proceed with the problem frame):** confirmed as direction. The benefit owner is now named, and the baseline source is the practice's timekeeping system.
- **Decision 2 (configure the approved assistant):** confirmed as direction, now backed by the tool's terms.
- **Steps 1 and 2:** both stay unticked. The benefit owner still has to agree the metric, and the baseline hasn't been pulled. The template-library option hasn't been tried, no own-sample test has run, and the risk lead hasn't confirmed anything. The brief's open list reflects this.
- **Benefit owner:** I set it in `portfolio.yaml` to the practice leader role. The intake evidence rows are updated to match.

**Quick-win category:** I left it as drafted, marked "PARKED for the forum" in `portfolio.yaml` and the intake record. The steering group is asked to confirm or change it, and the Go doesn't depend on it.

Next:
1. Pull the time-record baseline (hands-on hours per control test and the template or wording share).
2. Have the practice leader agree the metric.
3. Ask the risk lead to confirm `tier-2` and the catalog entry.
4. Have ai-governance run the vendor evaluation against the signed contract.

Then the brief can move on to the own-sample test and step 3.

### USER
Good, that's clear. Go ahead and draft the risk lead confirmation request for the `tier-2` and the catalog entry, so I can send it. In parallel, I'll pull the time-record baseline from timekeeping. Then set up the own-sample test plan for step 3, using synthetic cases only.

### TOOLS
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md

### ASSISTANT
Here is the draft request and what I added to the brief. I haven't sent anything.

**Draft message to the risk lead**

> **Subject: Confirmation needed: tier-2 for one use, and one assistant catalog entry**
>
> I'm asking you to confirm two things for the portfolio item `ct-int-nonclient-drafting`. It is a discovery-stage item from integrated audit: shared prompts and a senior-approved template set on the approved enterprise assistant, for test-step wording, templates and junior practice cases.
>
> **1. Risk tier.** The draft policy (`overlay/policy.md`, section 4) proposes `tier-2` for this use. It covers templates and wording drafts on non-client material that staff then use in workpapers. Client data is not permitted for this item. Confirm tier-2, or tell me the tier you want and why.
>
> **2. Catalog entry.** `overlay/tool-catalog.yaml` has a draft entry, `enterprise-assistant-business`:
> - Business tier, enterprise terms with a data processing addendum, no training on our inputs. These facts are as reported to me; the signed contract has not been checked.
> - Data classes: public and firm-internal only.
> - Maximum tier: tier-2.
> - Status: `under-review` until you confirm.
> - Conditions: non-client material only; the usage rule restated to users before shared use; the professional who relies on any output reviews it.
>
> Please confirm the entry as written, change it, or tell me what's missing. Not yet recorded: vendor, model, processing regions, retention, user groups and the exit plan.
>
> **What this decides.** The item is in discovery and can't reach its next gate (`g1`) without a confirmed tier. The same tier-2 and catalog entry would cover other uses of the assistant on non-client material.
>
> **Questions back to you:**
> 1. Does the draft policy's assumption that audit independence and PCAOB rules bind the firm hold? It doesn't change the tier here, since no client data is involved.
> 2. Should someone check the signed contract against the no-training term before the status moves off `under-review`?
>
> No client or personal data is in the files.

**Own-sample test plan.** It's in the brief's §2, under "Own-sample test plan (draft; synthetic cases only)". It does not run anything.
- **Cases:** 20 to 30 invented by seniors, in three types. Wording cases turn a control description into a test step. Template cases build a recurring workpaper section. Practice cases are scenarios with a planted gap for juniors, and a few cases are built from past wording mistakes. Nothing comes from real workpapers, even redacted.
- **Comparison:** each case runs three ways: your existing template library, the assistant with a plain prompt, and the assistant with the shared prompt and approved templates.
- **Marking:** a senior marks binary checks on a simple sheet. The checks are the right population and period, a testable step, nothing invented, no client detail, and the planted errors present. Two people who didn't write the case do the marking, and it grades outputs, never people.
- **Review time:** it also records the senior's minutes to accept or fix each draft, because that is what could eat a benefit of at most 0.2 h per test. The time-record baseline you're pulling is the yardstick for it.
- **Thresholds:** I left them empty. The benefit owner (the manager's practice leader) should set the pass rate and the review-minutes limit before the run.
- **Outcomes:** the plan names what the result decides. If your template library already meets the bar for wording and templates, keep those off the assistant. If the shared-prompt version wins within the review limit, step 2 is confirmed as `configure`. If not, the item goes back to the forum.

Two points:
- The test belongs to step 2, not step 3. Step 3 is the design, and step 4 builds the evaluation plan from this test. Step 2 stays unticked until someone runs it.
- Before the run, the usage rule has to be restated to everyone taking part. That is also a condition of the Go.

### USER
Thanks, I'll send the risk lead request as drafted. I'll have the baseline from timekeeping by the end of the week. Now go ahead and have ai-governance run the vendor evaluation against the signed contract. I'll get you the contract's no-training and data-processing terms to check, with no client details in them.

### TOOLS
- Write: overlay/vendors/enterprise-assistant-business.md
- Edit: overlay/tool-catalog.yaml
- Edit: overlay/tool-catalog.yaml
- Edit: overlay/policy.md

### ASSISTANT
I've opened the vendor evaluation but not run it, because it needs the contract terms and I don't have them yet. Every rating is `unknown`, the decision is `pending`, and the file is labelled `draft-to-validate`. The only inputs so far are your statements that the tool has a data processing addendum and doesn't train on your inputs, and those are recorded as reported, not checked.

**What I set up**
- **Evaluation file:** `overlay/vendors/enterprise-assistant-business.md` has the six-dimension scorecard with the open question for each dimension.
- **Screens:** independence, tax-return rules and client terms are marked `not-applicable`. The reason is that no client data or tax return information goes in and nothing is shared with a client. They are marked for the risk lead to confirm, so tell me if the reasoning is wrong.
- **Own-sample test:** marked `not-applicable` for the tool evaluation, since the use is at most tier-2. The item's own-sample test of output quality is separate and sits in the brief.
- **Cross-references:** the catalog entry now points to the evaluation file, and section 7 of `overlay/policy.md` lists the evaluation. Step 6 is not complete, so I left the policy's step counter alone.

**What to bring from the signed contract** (clause references or short excerpts, with the section number; no client details, no prices)
1. **No-training term:** the sentence covering inputs and outputs, and any exception for feedback, opt-in sharing, or human review for abuse monitoring.
2. **Data processing addendum:** purpose limits, retention and deletion, processing regions, the sub-processor list with its notice period, and the breach-notification duty.
3. **Change notice:** how model and terms changes are communicated to you.
4. **Exit:** data export and deletion on termination.
5. **Admin settings:** whether feedback sharing and retention are set at firm level, and who holds them.
6. **Certifications:** which report names this product, and its period.

If some of this sits with the IT/security lead, I can write the request to them, but it's their call whether to share the clauses.

When the excerpts arrive, I'll rate each dimension on that evidence only and write the conditions as settings someone can check. I'll also fill the catalog fields still missing: vendor, regions, retention and exit plan. I can't move the status off `under-review`; that needs the risk lead's confirmation. A contract term that comes back worse than reported (for example, a feedback exception) would change the conditions or the data classes, so the recorded no-training claim stays provisional until then.

### USER
I'll ask the IT/security lead for the contract excerpts, since they hold the signed terms. Please draft that request to them covering the six items, and say clearly that no client details or prices are wanted. I'll send it today. Meanwhile, leave the evaluation as `pending`, and tell me whether anything else in the portfolio can move while we wait.

### ASSISTANT
Here's the draft request to the IT/security lead, then what else can move. I haven't sent or changed anything.

**Draft message to the IT/security lead**

> **Subject: Contract excerpts needed for the enterprise assistant (business tier): no client details, no prices**
>
> I'm completing the vendor evaluation for the firm's enterprise assistant on the business tier. The risk lead is being asked to confirm its catalog entry, and I can't rate the contract terms until I've seen them. You hold the signed terms, so could you send short excerpts or clause references, with the section numbers, for the six items below?
>
> **Please do not send client details, personal data, prices, discounts or commercial terms.** Clause wording on data handling is enough. If a clause mixes in pricing, send only the data-handling sentences or just the section number.
>
> 1. **No-training term:** the wording covering inputs and outputs, and any exception (feedback, opt-in sharing, human review for abuse monitoring). Say whether the admin can switch an exception off, and whether that setting is on.
> 2. **Data processing addendum:** purpose limits, retention and deletion, processing regions, the sub-processor list with its notice period for changes, and the breach-notification duty.
> 3. **Change notice:** how we're told about model and terms changes.
> 4. **Exit:** data export and deletion on termination.
> 5. **Admin settings:** who holds the feedback-sharing and retention settings, and what they're set to.
> 6. **Certifications:** which report or certificate names this product and tier, and its period.
>
> If it's easy, please also give me for the catalog entry: the vendor name, the model if the vendor states it, the processing regions, the retention setting, and which user groups have seats.
>
> **Why now:** the first practice use is a discovery-stage item on non-client material only. The tool stays under review in the catalog until the risk lead confirms it, and your answers are what that confirmation rests on. The excerpts will sit in a vendor file in the overlay folder, so please send only what you're comfortable having there.

The licence count for the live-systems list is a separate ask. You could add it to this message, since you're already writing to the same person.

**What else can move while you wait**

1. **The other `g0` decisions.** The risk lead is already involved, and `g0` for the full-path audit items needs the portfolio lead and the risk lead together. The intake records propose:
   - `sox-prereview-checklist`: Go to discover.
   - `sox-report-register`: Go, with the readiness gaps named as conditions.
   - `sox-request-template` and `sox-listing-tool`: Hold, each with a `revisit_when` trigger already written.
   - `sox-client-data-approval`: its proposal is in the intake record's Screen result; I didn't read it fully.
   You and the risk lead decide these. I'd record them as one `g0` decision per item, each with its resources named, since a Go without resources is incomplete. The unset live limit doesn't hold up `g0`; it binds at `g1`.
2. **The enterprise assistant as a live system** (`firm-enterprise-assistant`). Its intake record needs a use list and a licence count from IT, and it's still `outline`. The same IT/security lead request could cover the licence count, and the portfolio lead is the business owner. Logging it also gives this item's catalog entry a home in the live-systems list.
3. **The item's own groundwork.** None of it depends on the contract:
   - the time-record baseline you're pulling;
   - the practice leader agreeing the metric and the test thresholds;
   - the senior writing the synthetic cases and gold answers;
   - restating the usage rule;
   - trying the template-library baseline.
   The synthetic-case test uses an assistant the firm already approves for this material. Hold the run until the usage rule is restated, and until the risk lead has had your confirmation request for a day or two, if you want the order tidy.
4. **The live limit and the firm-wide capacity stance.** Both are for the steering group. The limit will bind this item's `g1`, because `g1` counts items in prototype, pilot and scale. Getting it set now avoids a queue later.

**What can't move yet**
- **`ct-int-precheck-checklist`, `ct-int-validated-report-register`, `ct-int-listing-compare-draft` and `ct-int-ai-secondary-review`:** each needs the integrated-audit manager's validation, and each waits on its primary item passing `g0` (the secondary-review one on its primary leaving outline).
- **`g1` for this item:** it needs the baseline, the metric, the own-sample test, the risk tier and the vendor evaluation.
- **`sox-junior-development`:** it isn't in the register, so `sox-listing-tool`'s dependency on it can't resolve. That fix belongs to the advisor skill, because its title breaks the YAML in the SOX-only opportunities file.

### USER
Good, I'll send the IT/security lead request today and add the licence count ask to it. For the `g0` decisions, please draft the portfolio lead and risk lead decision records for `sox-prereview-checklist` and `sox-report-register` as Go, with resources and conditions named, and for the two Holds with their `revisit_when` triggers. I'll bring them to the next meeting. Also log `firm-enterprise-assistant` as a live system, with the use list and licence count marked as awaiting IT.

### TOOLS
- Edit: portfolio/intake/firm-enterprise-assistant.md
- Edit: portfolio/intake/firm-enterprise-assistant.md
- Edit: portfolio/intake/firm-enterprise-assistant.md
- Edit: portfolio/intake/firm-enterprise-assistant.md
- Edit: portfolio/portfolio.yaml

### ASSISTANT
The four decision records are drafted below for you to bring to the meeting. None of them is recorded in `portfolio.yaml` yet, because the portfolio lead and the risk lead decide them, not me. `firm-enterprise-assistant` is now logged as a live system, with the licence count and use list marked "awaiting IT".

**Live-system entry**
- **Where:** the table is in the intake record's live-systems section, and the awaiting-IT lines sit at the top of its "Owners to find out" list.
- **Contents:** the entry lists the portfolio lead as business owner and the IT/security lead as technical owner. Permitted data is public and firm-internal, client data is not permitted, and the risk tier is the proposed `tier-2` ceiling. The contract and vendor evaluation are marked pending.
- **Stage:** I left `stage: intake` and `status: outline`. A live-systems entry is an inventory record. Setting `production` would imply `g3`/`g4` evidence that doesn't exist.
- **Risk tier:** `risk_tier` stays null until the risk lead confirms it.

**Checks before the meeting**
1. **Senior manager hours.** The checklist record says the ITGC senior manager's blind back-test takes 2 h a week for 8 weeks, which is 16 h. The report-register record says the same person back-tests at about 6 h a week for 8 weeks. Those can't both be right. I used 16 h below. The practice lead should confirm, because the same person also validates reports at about 4 h a week.
2. **What a `g0` Go releases.** For the report register, the intake record names all of stage 1 (60–88 h, USD 12,600–18,480). A `g0` Go is discovery resources only. I've proposed the discovery slice, which is the plan's first step: 24 h for the first client's validation. The full stage-1 cost is shown as an alternative for the deciders. Say if you want it the other way.
3. **Plan figures.** The hours, the USD 210 rate and the 5-point and "half the notes" thresholds all come from the audit plan, reported. The advisor has not seen the tracking sheet.

**Draft decision records.** All four have `review: null`, are decided outside a review, and are decided by the portfolio lead and the risk lead.

**1. `sox-prereview-checklist`: proposed Go to discover**
- **Reason:** value index 4.33 and readiness index 4.45, a foundation for `sox-client-data-approval`, `sox-listing-tool` and the junior workstream. It needs no AI and no client-data tool. The back-test is the only step that touches past client files.
- **Evidence:** the intake record, the plan's go/no-go, and scores of weighted 4.40. The value range of 5–12 points off the review-note rate is grade D, on reported figures.
- **Resources:**
  - *People:* 2–3 protected senior half-days in the shoulder weeks (6–24 h), released by the practice leader; the ITGC senior manager for the back-test (16 h, pending point 1), also released by the practice leader.
  - *Budget:* none beyond time.
  - *Data:* past files for the blind back-test, released by the risk lead, with the PCAOB comment details kept apart.
- **Conditions:**
  - The risk lead confirms the back-test is permitted under the engagement terms.
  - The back-test protocol is frozen before anyone reads the PCAOB comment text.
  - The methodology owner approves the checklist.
- **Kill criteria:**
  - The back-test would have caught fewer than half the evidence notes on at least ten past files.
  - In the pilot, the completeness note rate falls by less than 5 points, or other note types or re-performance disagreement rise.
  - The plan says "revise before widening"; the forum may prefer a stop after one revision.
- **Next gate, `g1` (full path):**
  - the benefit owner and the metric;
  - the baseline from the tracking sheet and a timed sample of about ten tests;
  - written definitions agreed;
  - the back-test result;
  - where the checklist lives;
  - the risk tier recorded as "none" (no AI).
  - Gatekeepers: practice leader, risk lead, IT/security lead.
- **Note:** `ct-int-precheck-checklist` is its variant. Once this passes, its next-gate row for "primary passes `g0`" is met, and it still waits for the integrated-audit manager's validation.

**2. `sox-report-register`: proposed Go to discover**
- **Reason:** value index 4.11, readiness 3.36, which is just under the 3.5 line. It is a staged big bet, so the Go rests on the readiness work being named as conditions.
- **Evidence:** the intake record and the plan's stage-2 go/no-go. The capacity range of 25–63 staff hours a month is grade D, net of a one-off specialist effort of 180–600 h.
- **Resources:**
  - *People:* the ITGC senior manager at about 4 h a week outside peak, released by the practice leader.
  - *Budget:* the first client's validation (24 h, about USD 5,040 at the plan's USD 210 an hour), counted as real cost because it displaces billable work. The finance lead confirms the treatment and the rate. The alternative is naming all of stage 1 (60–88 h, USD 12,600–18,480).
  - *Data:* access to the first client's key reports, released by the risk lead and the IT/security lead.
- **Conditions:**
  - Risk and quality confirm that a senior manager on the ITGC side can sign a validation record, and what a record contains.
  - A named register owner and re-validation triggers are in place.
  - One client is validated first and timed.
- **Kill criteria:**
  - Measured hours per later client fall outside 12–16 with no explanation.
  - The completeness rate doesn't fall in the stage-1 clients against their prior period, or other notes or re-performance disagreement rise.
  - Risk and quality don't accept the records or the validator role.
- **Next gate, `g1`:** the benefit owner and the metric; the key-report inventory for stage-1 clients; the first client's validation hours; the record's contents agreed; the register's shared place decided; the risk tier "none".
- **Open:** the ITGC senior manager also carries the checklist back-test. I'd put the overload on the meeting's agenda before the Go is recorded.

**3. `sox-request-template`: proposed Hold**
- **Reason:** value index 3.44, below the 3.5 line, with readiness at 4.45. Its quality value overlaps `sox-prereview-checklist` and `sox-report-register` on the same notes, so values aren't added. On the full path the default for this quadrant is Hold. Nothing is wrong with the idea.
- **Evidence:** the intake record and the re-read scores (weighted 4.00).
- **Resources:** none released.
- **`revisit_when`:** "The per-client key-report inventory exists (the first step of `sox-report-register`); in practice it starts client by client as each inventory completes."
- **Note:** this is a Hold, not a stop.

**4. `sox-listing-tool`: proposed Hold**
- **Reason:** both indexes are low (value 2.11, readiness 2.36). The 24–126 staff hours a month is a guess at full coverage, and near zero for the first approved scope. It depends on four items that aren't in place, one of which (`sox-junior-development`) isn't in the register.
- **Evidence:** the intake record, the draft policy's `tier-4` for this use, and the 3–4 month client-data approval path.
- **Resources:** none released.
- **`revisit_when`:** "`sox-prereview-checklist` and `sox-report-register` are in place with baselines, and `sox-client-data-approval` is granted."

**Before you record these**
- **Live limit:** it isn't `g0` evidence. Note each Go's place in the queue only.
- **Risk lead's role:** recording needs both deciders' agreement. If they decide differently, I'll record that.
- **After the meeting:** give me the outcomes and I'll append the `decisions` entries, set `stage`, `status`, `next_gate` and `kill_criteria`, and update the intake records' evidence tables.

### END
session 807fbf4d-3850-5c6c-82b1-8d3750715cd5
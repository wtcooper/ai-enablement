### USER
I'm head of AI at our firm. The audit practice already has a transformation plan in this folder. Set up a firm-wide AI portfolio and bring the audit opportunities into it so we can compare and prioritise them.

### TOOLS
- Skill: ai-transformation:ai-portfolio
- Write: /tmp/claude-0/-home-user-ai-enablement-evals-e2e-2026-10-21-suite-handoff-rerun-workspace/807fbf4d-3850-5c6c-82b1-8d3750715cd5/scratchpad/check.py

### ASSISTANT
I've read the audit plan and both units' opportunity files. I haven't written anything yet.

**What I found**
- **Plan settings:** the plan gives me the value levers and weights (capacity, quality, risk, staff experience, margin), a redeploy stance and the guardrails. I'll inherit these as a starting point for the firm portfolio, and you can change them.
- **Integrated-audit file:** it parses, but it's an unvalidated desk review. Those items will come in as outlines marked "draft to validate".
- **SOX-only file:** `units/sox-only-outsourcing/opportunities.yaml` doesn't parse. An unquoted colon in an item title on line 106 breaks it: "Named junior-development workstream: juniors keep…". The portfolio skill doesn't fix advisor files, so I won't touch it. The transformation-advisor skill can fix that title. I'll import from it only once you've agreed how to handle it. My options are to wait for the fix, or to import the other items now and add that one after the fix.

Reminder: please keep client-confidential and personal data out of anything we write here.

**First step: setting up the portfolio.** Next we log the audit ideas, then score them side by side.

**Question 1:** Which practices and functions should the firm-wide portfolio cover (for example audit, tax, advisory and the internal functions), and should it hold ideas only, or pilots and live AI systems too?

### USER
Cover audit, tax, advisory and client accounting, plus the internal functions like finance, HR and IT. Include ideas, pilots and live AI systems, because we already have the one approved assistant in use and I want it on the same list.

For the SOX-only file, import the other items now and add that one after the title is fixed.

### ASSISTANT
Playback of what I heard:
- **Scope:** audit, tax, advisory, client accounting, and the internal functions (finance, HR, IT).
- **Item types:** ideas, pilots and live AI systems on one register.
- **Existing assistant:** the approved assistant goes on as a live item. Seat and licence roll-outs belong on the enablement line, so I'll log it as an inventory entry for visibility. It won't be scored as a portfolio win.
- **SOX-only import:** I'll bring in every item except the junior-development workstream and add it once the advisor skill has fixed the title.

Next, the decision system: who can say yes to a pilot, and who has to release the resources.

**Question 2:** When a pilot needs people's time, budget or client data, who releases each of those at the moment, and would they sit at the gate that decides whether the pilot goes ahead?

### USER
Right now the AI steering group approves pilots and decides whether they go ahead. Resources are released separately: the practice leader releases people's time, finance holds budget, and IT/security plus the confidentiality or risk lead releases any client data. So the steering group doesn't control any of those releases, and none of those people sit at the gate. I'd want them at the gate so a "yes" actually comes with the resources.

### ASSISTANT
Playback:
- **Today:** the AI steering group approves pilots, but it releases none of the resources. Practice leaders release people's time, finance holds budget, and IT/security plus the confidentiality or risk lead release client data.
- **What you want:** the people who release those resources sit at the gate, so a "yes" comes with them. I'll set the pilot gate (`g2`) and the later gates up that way.
  - **Time:** the practice leader of the submitting practice.
  - **Budget:** finance.
  - **Client data:** IT/security and the risk lead, only where client data is involved.
  - **Steering group:** it stays as the forum.

Next, how heavy each item's route should be.

**Question 3:** Which kinds of items should take a lighter route through the gates (for example ones with no client data and a single team), and who should decide the first screen (`g0`) on the light route and on the full route?

### USER
Light route for anything with no client data, a single team, and no independence or tax-consent angle. That covers things like internal finance, HR and IT ideas, and audit or tax drafting aids that only touch firm-owned material. Everything else takes the full route: any client data, more than one practice, or anything touching independence or tax-return consent.

For the first screen (`g0`), I'd have the portfolio lead (my office) decide on the light route, with the submitting practice leader consulted. On the full route, I'd want the portfolio lead plus the risk lead to decide it, so independence and consent issues get caught at the start.

### ASSISTANT
Playback:
- **Light route:** no client data, a single team, and no independence or tax-consent angle. That covers internal finance, HR and IT ideas, and audit or tax drafting aids that only touch firm-owned material.
- **Full route:** any client data, more than one practice, or anything touching independence or tax-return consent.
- **`g0` on the light route:** the portfolio lead decides, and the submitting practice leader is consulted.
- **`g0` on the full route:** the portfolio lead and the risk lead decide together.

One consequence for the audit items: the plan says the audit work touches client evidence and independence rules, so they'll land on the full route, apart from any that only draft on firm-owned material.

Next, the review forum.

**Question 4:** Who should sit in the regular portfolio review, and what should it decide: should it be the existing AI steering group, or a different group?

### USER
Let's use the existing AI steering group as the regular portfolio review, but add the finance lead and the risk lead as standing members so the people who release budget and client data are in the room. It should decide continue, hold, redirect, stop or scale on each item, and also where any freed capacity goes. Meet monthly, with my office preparing the review pack.

### ASSISTANT
Playback:
- **Forum:** the existing AI steering group, with the finance lead and the risk lead added as standing members.
- **Decisions:** continue, hold, redirect, stop or scale on each item, plus where freed capacity goes.
- **Rhythm:** monthly, with your office preparing the pack.

I'll add one note. A rebalance of weights, balance and the live limit every third review is my default, and you can change it.

Next, the live AI that's already running.

**Question 5:** For the approved assistant and any other AI already in use, is there a list of what's running and who owns each, and is there a defined way to switch one off safely if the forum decides to stop it?

### USER
There's no proper list. Each practice knows what it has switched on, and IT has the licence count for the approved assistant, but nothing records owners or what each tool is used for. There's also no defined switch-off. If the forum said stop, I'd expect IT to cut access and the practice leader to tell people, but that isn't written down anywhere. Please build the live-systems list with a named owner role for each entry, and set a simple retire step for the forum to use.

### TOOLS
- Write: portfolio/portfolio.yaml

### ASSISTANT
Step 1 is saved in `portfolio/portfolio.yaml`. It parses, and both sets of weights sum to 1.

**What's in it**
- **Scope:** audit, tax, advisory, client accounting and the internal functions. It covers ideas, pilots and live systems on one register.
- **Value levers and weights:** I inherited these from the audit plan.
- **Gates:** each gate lists the resource-holders as gatekeepers (practice leader, finance lead, IT/security lead, risk lead), so a "yes" comes with the resources.
- **Routes and `g0`:** light and full routes, with the `g0` deciders as you set them.
- **Forum:** the steering group plus the finance and risk leads, meeting monthly.
- **Retire step:** the IT/security lead cuts access, the practice leader tells users and clients, the inventory is updated, and lessons and reusable assets are kept. The forum triggers it.

**Still open**
- **Capacity stance:** I left it "undecided" firm-wide. The audit plan chose redeploy for its own practice, and I didn't want to present that as a firm decision.
- **Value-lever metrics:** these are audit-specific. Tax, advisory and the others will need their own metric under each lever when their first item is logged.
- **Live limit:** unset. It needs a number based on how many owners and how much review capacity you have.
- **Stage exit evidence:** these are my defaults, tailored for independence and tax consent. Please check them.

**Next, step 2 (intake).** I'll log the audit items from both files and the approved assistant as a live-systems entry. I'll name a placeholder owner role for each and leave the SOX junior-development item out until its title is fixed.

**Question 6:** Who owns the approved assistant today in role terms: the IT lead who holds the licences, or a business owner who decides how it's used?

### USER
The IT lead owns the licences, but a business owner should decide how the assistant is used. Put my office down as the business owner, since I'm head of AI, and the IT lead as the technical owner. Go ahead with intake on that basis. Use placeholder owner roles for the audit items, and leave the SOX junior-development item out until we fix its title.

### TOOLS
- Write: /tmp/claude-0/-home-user-ai-enablement-evals-e2e-2026-10-21-suite-handoff-rerun-workspace/807fbf4d-3850-5c6c-82b1-8d3750715cd5/scratchpad/load.py
- Write: portfolio/intake/firm-enterprise-assistant.md
- Write: portfolio/intake/sox-prereview-checklist.md
- Write: portfolio/intake/sox-request-template.md
- Write: portfolio/intake/sox-chase-assistant.md
- Write: portfolio/intake/sox-report-register.md
- Write: portfolio/intake/sox-client-data-approval.md
- Write: portfolio/intake/sox-listing-tool.md
- Write: portfolio/intake/sox-ai-secondary-review.md
- Write: portfolio/intake/sox-agent-testing.md
- Write: portfolio/intake/sox-platform-plus-review.md
- Write: portfolio/intake/ct-int-validated-report-register.md
- Write: portfolio/intake/ct-int-precheck-checklist.md
- Write: portfolio/intake/ct-int-nonclient-drafting.md
- Write: portfolio/intake/ct-int-listing-compare-draft.md
- Write: portfolio/intake/ct-int-ai-secondary-review.md

### ASSISTANT
Intake is done for 15 items. Step 2 is saved, and `portfolio.yaml` re-parsed cleanly (15 unique ids).

**What's in the register**

| Group | Items | Status |
|---|---|---|
| Live system | `firm-enterprise-assistant` (your office is business owner, the IT/security lead is technical owner) | outline: uses and volume not recorded |
| SOX-only, ready to screen | checklist, request template, chase assistant, report register, client-data approval, listing tool | active |
| SOX-only, parked stubs | AI secondary review, agent testing, platform-plus-review | outline: no value or scores in the advisor file |
| Integrated audit | 5 items | outline, marked draft to validate until an integrated-audit manager reviews them |

- **Left out:** `sox-junior-development`, until the advisor skill fixes its title.
- **Dangling dependency:** `sox-listing-tool` depends on that item, so the dependency shows as missing until it's imported.
- **Owners:** I used placeholder roles from the audit plan: SOX/ICFR practice lead, ITGC senior manager and integrated-audit manager.
- **No-AI items:** three audit items (checklist, request template, report register) are marked as needing no AI, per the plan. They stay in the register as process changes and will be counted apart from AI items in reviews. The integrated-audit checklist and register are marked the same way.
- **Imported as they stand:** scores, value ranges and evidence grades are copied from the advisor files. Step 3 re-scores them, so there are no weighted scores, value or readiness indexes, risk tiers or gate paths yet.

**Overlaps to settle before you prioritise**
- The SOX-only and integrated-audit checklist, report register, listing tool and AI secondary review are the same ideas on two lines. The audit plan intends to merge them at roll-up, so I'll keep their values from being added together.
- `sox-client-data-approval` and `ct-int-listing-compare-draft` both propose opening the same client-data approval. The firm should send one request.

**Live-systems list:** it has one entry, because the assistant is the only tool anyone named. The register can't show other practices' tools until each practice leader and IT report what's switched on. That's a data-gathering step for your office.

**Next, step 3: screen and score.** I'll score each item on the six dimensions and show value and readiness separately. I'll also record the route and the `g0` decision by the right deciders, or "pending the forum".

**Question 7:** Which should we screen first: the SOX-only items that are ready to screen, or the whole register including the integrated-audit drafts as provisional?

### USER
Let's screen the whole register, with the integrated-audit drafts marked provisional so they can't pass `g0` until the integrated-audit manager has validated them. For the overlaps, keep one primary entry for each merged idea and mark the duplicate as a variant. That way nothing gets counted twice.

### ASSISTANT
The screen is done and saved. `portfolio.yaml` parses and has 15 items. I haven't recorded any `g0` decisions yet; each item has a proposed outcome, and the register isn't ready to prioritise firm-wide.

**Merged ideas.** There is one primary per idea, and the duplicate carries `variant_of` so it isn't counted twice:
- `sox-prereview-checklist` has the variant `ct-int-precheck-checklist`.
- `sox-report-register` has the variant `ct-int-validated-report-register`.
- `sox-listing-tool` has the variant `ct-int-listing-compare-draft`.
- `sox-ai-secondary-review` has the variant `ct-int-ai-secondary-review`.

**Provisional items.** All five integrated-audit items are marked `provisional`, and they can't pass `g0` until the integrated-audit manager has validated them. That includes `ct-int-nonclient-drafting`, which isn't a duplicate.

**Scores.** The advisor's scores stand, because your portfolio weights match the plan's. Value and readiness are shown separately:

| Item | Value | Readiness | Proposed `g0` |
|---|---|---|---|
| `sox-prereview-checklist` | 4.33 | 4.45 | Go to discover |
| `sox-report-register` | 4.11 | 3.36 | Go, with readiness work as conditions |
| `sox-request-template` | 3.44 | 4.45 | Hold until the report inventory exists |
| `sox-client-data-approval` | 2.56 | 3.36 | Hold, or Go for stage 0 only as an exception, because it carries the 3-4 month approval lead time for every client-data tool |
| `sox-chase-assistant` | 2.44 | 3.73 | Hold |
| `sox-listing-tool` | 2.11 | 2.36 | Hold until its dependencies are in place |

The three outline stubs, the enterprise assistant and the integrated-audit variants aren't scored as pipeline items.

**Routes.** The chase assistant and the integrated non-client drafting item take the light route. Everything else is on the full route, because it touches client files or client-facing wording.

**Why nothing is decided yet**
- **Deciders:** the full-route items need you and the risk lead together, and the risk lead hasn't been part of this session.
- **Live limit:** it's still unset. The checklist and the register both rest on the same ITGC senior manager and on seniors who are 90–95% booked in busy season, so any Go depends on a limit you set.
- **Risk tiers:** I left them empty, since there's no policy overlay yet. That's a job for the ai-governance skill.

**This is still an audit-only register.** Nothing from tax, advisory, client accounting or the internal functions has been logged, so there's nothing firm-wide to compare against yet.

**Schema extensions.** `variant_of` and `provisional` go beyond the portfolio schema, and I noted that in the file header.

**Question 8:** As portfolio lead, do you want to record `g0` now for the one light-route item you can decide alone (the chase assistant, proposed Hold), and leave the full-route items pending until you and the risk lead decide together?

### USER
Yes, record `g0` for the chase assistant as Hold. Leave the full-route items pending until the risk lead and I can decide them together. Then draft the firm-wide intake request for tax, advisory, client accounting and the internal functions, so we can start filling the gaps.

### ASSISTANT
I recorded `g0` for `sox-chase-assistant` as **Hold**, decided by you as portfolio lead. `portfolio.yaml` still parses with 15 items.

- **Reason:** value index 2.44 with a low end of zero, and the request template may remove most of the chasing.
- **Revisit when:** `sox-request-template` is live and tracking shows chasing time is still material.
- **Consultation:** the light route has the submitting practice leader consulted. I didn't record that it happened, because I don't know whether it did. If it did, tell me and I'll add it.
- **Other items:** the full-route items stay pending until you and the risk lead decide them together. The three outline stubs and the integrated-audit provisional items stay unscreened.

Below is the intake request for the other practices. I've kept it in chat, because the portfolio files don't take drafted messages. Edit it as you like before sending.

---

**Subject: Log your AI ideas and AI already in use in the firm AI portfolio**

We're setting up one firm-wide register of AI ideas, pilots and live AI systems, so the steering group can compare them and decide where to put people, budget and client data. Audit's opportunities are already in. We need tax, advisory, client accounting, finance, HR and IT.

**Please don't include client-confidential or personal data in anything you send.** Describe the work in general terms.

**1. AI already in use (live systems).** Please list every AI tool your team has switched on, approved or not. For each, give:
- what it's used for
- roughly how many people use it
- who in your area owns it (a role, not a name)
- whether client data goes into it

We're not judging anyone for what's on the list. We just need a record, so we can name an owner for each tool and have a safe way to switch it off.

**2. AI ideas.** For each idea, please give:
1. **The activity and the result you expect, in one sentence.** For example: "help preparers do X so that Y moves."
2. **How often it happened last month,** from a record if you have one. Say where the number came from.
3. **What kind of change it is:**
   - people working differently in tools they already have
   - the flow of work changing (steps removed, merged or run without a person)
   - a new service, product or price

   Seat or licence roll-outs aren't portfolio items. They go to the enablement line.
4. **Could simple rules, a template or an existing feature do it?** Tell us what you checked.
5. **The data it needs, who owns it, and whether anyone has looked at it in its real state.** Say whether client data is involved, whether it touches more than one practice, and whether it touches independence or tax-return consent. That decides the light or full route.
6. **Who would lead the work, and who in the business would own the benefit.**
7. **Which measure it would move, and who watches that measure today.** Use the firm's levers: capacity, quality, risk, staff experience, margin. The audit plan's metrics don't fit every practice, so tell us the measure your practice would use for each lever. We'll agree one per lever for your area.
8. **If it works, where do the freed hours go:** redeployed to growth, quality or backlog, or taken out of cost? An early answer is fine.

Incomplete ideas are still welcome. They're logged as outlines and not scored until we have an owner, a problem statement and a data source.

**3. Existing plans.** If your practice already has a transformation plan or opportunity list, send it as it is and we'll import it. If you don't have one, say so. Your leader can run the transformation-advisor skill to build one first.

Please send everything to the portfolio lead's office.

---

**Open items**
- **Metrics:** the lever metrics are still audit-specific. The request asks each practice to propose its own, and you'll need to agree one per lever.
- **Capacity stance:** the firm-wide choice (redeploy or reduce) is still open. Question 8 of the request asks practices for their view.
- **Live limit and risk tiers:** the live limit is still unset. Risk tiers need the ai-governance skill, since there's no policy overlay yet.
- **Junior-development item:** it comes in once the advisor skill has fixed its title.

**Question 9:** Do you want to set the live limit now, as a number the steering group could carry, or leave it until the first full-route `g0` meeting with the risk lead?

### USER
Leave the live limit until the first full-route `g0` meeting with the risk lead. I'd rather set it with them, using real numbers on owners and review capacity. The intake request looks good, so I'll send it as drafted. Next, please set up the risk tiers using the ai-governance skill so the risk lead has something to react to at that meeting.

### TOOLS
- Skill: ai-transformation:ai-governance

### ASSISTANT
I'll use the **ai-governance** skill. No `overlay/` exists yet, so it starts at step 1 (baseline), then data rules, then risk tiers (step 3). That order matters because tier 4 ("regulated or high-impact") depends on which professional rules bind your work. The risk lead will react best to tiers that rest on the firm's actual regimes. I'll draft the tiers from the skill's defaults and label them as defaults to adjust.

The reminder about client-confidential and personal data still applies: describe tools, data classes and roles only.

**What I already have from the audit plan, so I won't ask again**
- Archetype: assurance.
- Constraints: no client data in the enterprise assistant; new client-data tools need risk and quality, CIO and general counsel sign-off (security review, data-handling and retention assessment, independence check, 3–4 months).
- Rules: PCAOB and independence rules apply, and the auditor stays accountable for the opinion.
- Guardrails already agreed in the plan: a person owns evidence selection and sign-off, and a senior or manager reviews every AI-flagged exception.

**What I don't have** is the firm-wide picture. Tax, advisory and client accounting carry different duties from audit, and the policy is firm-level.

**Question 10:** Which professional or contractual rules bind how the firm may use AI in its work? For example: audit independence and PCAOB, US tax-return use and consent rules, client contract or engagement-letter restrictions, EU deployer duties and personal-data law.

### USER
Let's take the highest-priority audit opportunity in the portfolio into prototype. Help me decide build versus buy and set up the solution brief.

### ASSISTANT
I can't take an item into prototype yet, because none of them has passed the earlier gates. I'd rather say that than set up a brief that the gates don't support.

**Where the audit items stand**
- The top-scoring item is `sox-prereview-checklist`: weighted 4.40, value index 4.33, readiness index 4.45. It's still at **intake**. Its `g0` is pending your decision with the risk lead.
- Prototype is entered at **`g1`** (discover to prototype), after a Go at `g0` and a discover stage. That stage needs a baseline from records, the data seen in its real state, and a benefit owner who has agreed the metric. None of that exists yet.
- The live limit is unset, so no Go would be complete yet. A Go has to name its resources and fit within the limit.
- I can only record these decisions. The gatekeepers and the forum make them.

**Build or buy for this item.** It's a written checklist and a back-test. It needs no AI (`ai_use: none`) and there's no tool to buy, so the leaning is to build it in-house. There's nothing to prototype in the technical sense. Discover is the stage that fits: write the criteria, run the blind back-test, and take the baseline from the tracking sheet.

**The highest-priority item that uses AI** is `sox-listing-tool`, and it isn't ready. It scores 2.25, is proposed as a Hold, and is blocked on the checklist, the report register and the client-data approval. A brief for it would be premature.

**What I can do now**
1. Draft the build-or-buy framing for the checklist as a pre-read for your `g0` meeting with the risk lead. It would be marked as a draft, and I wouldn't open a `solutions/` folder.
2. Once `g0` is a Go, hand it to **ai-solution-delivery** with the brief opened as `g1` evidence, as the portfolio process expects.

Separately, the risk-tier work is still waiting on Question 10, about which professional rules bind the firm's AI use. Say when you want to come back to it.

**Question 11:** Do you want the draft build-or-buy framing for the checklist now, as a pre-read for the `g0` meeting, or would you rather wait until `g0` is decided and then open the brief properly?

### USER
Draft the build-or-buy framing for the checklist now as a pre-read for the `g0` meeting. Mark it as a draft and don't open a `solutions/` folder. For Question 10, assume the firm is bound by audit independence and PCAOB rules, US tax-return consent rules, client engagement-letter restrictions, and personal-data law. Use that to start the risk tiers, labelled as assumptions for the risk lead to correct.

### TOOLS
- Write: overlay/policy.md

### ASSISTANT
Both drafts are written, and the policy frontmatter parses. I didn't open a `solutions/` folder.

**1. Build-or-buy pre-read for the `g0` meeting.** It's in a new section of `portfolio/intake/sox-prereview-checklist.md`, marked as a draft pre-read. I put it there because the portfolio files don't take separate documents. It sets out five options:
- **Build in-house:** the seniors write the checklist and the ITGC senior manager back-tests it blind.
- **Configure the audit platform to hold it:** whether the platform can do this is unknown.
- **Use the enterprise assistant to draft wording:** non-client material only.
- **Buy an external checklist pack:** it can't hold this practice's unwritten checks.
- **Do nothing.**

The leaning is to build in-house, with the platform as a later question and the assistant only as an optional aid. It also lists what discover would settle, the evidence so far (grades as recorded: C for use case 03, B for use case 10, and the plan's value range at grade D), the resources a Go would name, and six questions for the meeting. Those include the live limit and who the benefit owner is.

**2. Risk tiers, started on your assumptions.** They're in the new `overlay/policy.md`, status draft, and the regimes and owners are labelled as assumptions. The regimes are audit independence and PCAOB, US tax-return consent, client engagement-letter restrictions, and personal-data law. The file has:
- the four tiers, each with a reviewer, what they check, the record needed and the autonomy allowed
- how each assumed regime shapes the tiers
- a not-permitted-until-approved list
- the autonomy rule
- a proposed tier for every portfolio item
- six questions for the risk lead and counsel

Notable proposed tiers:
- The listing tool, AI secondary review, agent testing and platform-plus-review are tier 4.
- The chase assistant is tier 3, because its messages leave the firm.
- The three process items need no tier.
- The enterprise assistant gets a ceiling of tier 2.

**What's still unfinished**
- **Policy steps:** `step_completed` stays 0, because the baseline and data rules haven't been done. Tier thresholds and the ladder rule are advisor defaults. Only the PCAOB standard is sourced, and the dates in the personal-data row need re-verifying.
- **Portfolio tiers:** I left `risk_tier` empty in `portfolio.yaml`, so your assumptions don't read as settled before the risk lead reacts. I can fill them in after that meeting.
- **No client-data approval or `max_risk_tier`:** the tool catalog doesn't exist yet, so the assistant's ceiling is only proposed.
- **`g0` meeting:** the live limit and the full-route `g0` decisions are still waiting for you and the risk lead.

**Question 12:** Should I continue the governance baseline (step 1: which AI tools are in use, existing policies, and owners) before the `g0` meeting, or stop here so the risk lead reacts to the draft tiers first?

### USER
Stop here so the risk lead can react to the draft tiers first. I'd rather not do the baseline on my own, because the tool inventory and owners are better filled in once the intake responses from the other practices come back.

Please add a short agenda for the `g0` meeting. It should cover the tiers, the live limit, the checklist decision and the chase assistant Hold. Keep it in the same place as the other drafts.

### ASSISTANT
I've added a short draft agenda for the `g0` meeting. It's in `portfolio/intake/sox-prereview-checklist.md`, right after the build-or-buy pre-read. I've stopped the governance work here, as you asked. `overlay/policy.md` stays a draft with its baseline step not done.

**The agenda**
1. **Live limit:** set it as a number, using real figures on owners and review capacity. The ITGC senior manager and the seniors are shared by the checklist and the report register.
2. **Draft risk tiers:** the risk lead corrects the assumed regimes, the tier definitions and the proposed tier for each item. The six questions in the policy draft are the starting list.
3. **Checklist decision:** go through the build-or-buy pre-read, then record the `g0` outcome. For a Go, that includes resources, conditions and kill criteria.
4. **Chase assistant Hold:** note the Hold you recorded, and confirm the proposed tier 3 for client-facing drafts. The open point is whether the sender counts as the named reviewer.

The agenda puts the live limit and the tiers first, because they set the bounds for the checklist decision. It ends with a line on the other pending full-route items, in case time allows. I didn't give it a date or time.

The register is still audit-only and nothing is decided on the full-route items yet. After the meeting I can write the confirmed tiers into the portfolio items' `risk_tier`, record the `g0` outcomes, and fold in the intake responses from the other practices as they come back.

### USER
Thanks, the agenda covers what I need. One thing to add: put a short note under the tiers item saying the regimes and owners are assumptions for the risk lead to correct, so nobody reads the draft as settled. Then let's wait for the other practices' intake responses before we do anything else.

### ASSISTANT
I added the note under the tiers item in the agenda. It says the regimes and the policy, catalog and other owners are assumptions for the risk lead to correct, that the draft isn't settled, and that no portfolio item carries a `risk_tier` yet.

I'll leave everything else as it is until the other practices' intake responses come back.

**Where things stand**
- `portfolio/portfolio.yaml` has 15 items: the audit ones, plus the enterprise assistant as the first live-systems entry.
- One `g0` is recorded: the chase assistant is on Hold. The full-route items are pending you and the risk lead.
- The live limit is unset, to be set with the risk lead.
- `overlay/policy.md` is a draft with the baseline step not done.
- The `sox-junior-development` item isn't imported until the advisor skill fixes its title.

**When responses arrive**, send me each practice's reply or plan file. I'll check it parses, import or log the items as outlines, and add anything it names to the live-systems list. Then I'll screen the new items against the audit ones, using the same weights.

### USER
Sounds good, I'll send the other practices' replies as they come in. When I do, please also pull any AI tools they mention into the live-systems list, so the baseline is ready when we get to it.

### ASSISTANT
Understood. When you send a practice's reply, I'll do two things with it.

**1. Pull each AI tool it mentions into the live-systems list.** Each tool becomes an entry like the enterprise assistant's, with:
- the practice it comes from
- what it's used for and roughly how many people use it, as far as the reply says
- whether client data goes in
- an owner role. If the reply doesn't name one, I'll mark it "owner not named" and won't guess.

An entry stays an outline until it has a use and an owner. I'll also keep a running list of what each tool's baseline still needs, so the governance baseline can start from it later.

**2. Log the ideas.** I'll check any plan file parses and import its items. I'll log other ideas from the intake request as outlines until they have an owner, a problem statement and a data source. Then I'll screen them against the audit items with the same weights.

I won't screen items or record any `g0` decisions beyond the chase assistant's until you and the risk lead have met. I'll flag anything that touches the tiers or the assumptions you gave, so it goes to the risk lead and isn't settled by me.

For tools that come in without any detail, I'll record them as outlines.

### USER
Good. One addition: when a reply names a tool but not who owns it, add a line to the running baseline list asking me to find out the owner, so we don't lose track of it. Otherwise, I'll send the first reply once it lands.

### ASSISTANT
Agreed. When a reply names a tool but not its owner, I'll add a line to the running baseline list: "Find out the owner of [tool], named in the [practice] reply." It stays on the list until you give me an owner role. The entry stays an outline until then.

The running list will live in the "Live-systems list" section of `portfolio/intake/firm-enterprise-assistant.md`. I'm using that file because it's where the live-systems list started, and the portfolio files don't take a separate document. Each line will have the tool, the practice, what's still missing (owner, use, whether client data goes in) and who to ask. The list is easy to find when we reach the governance baseline.

Send the first reply when it arrives.

### USER
Sounds right. One small change: put the "find out the owner" lines at the top of the running list, ahead of the other entries, so they don't get buried as the list grows. Then I'll send the first reply when it lands.

### ASSISTANT
I've changed the live-systems list in `portfolio/intake/firm-enterprise-assistant.md`. A new "Owners to find out" block now sits at the top, ahead of the entries. It currently says "None yet; no practice replies have arrived."

Each line will read "Find out the owner of [tool], named in the [practice] reply". It will also show what else is missing (use, client data) and who to ask. A line comes off once you give me an owner role.

I'm ready for the first reply.

### END
session 807fbf4d-3850-5c6c-82b1-8d3750715cd5
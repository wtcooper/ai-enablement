### USER
I'm an audit partner leading SOX and ICFR controls testing at a mid-tier firm. Help me figure out where AI could transform how we work, and build a plan I can take to leadership.

### ADVISOR
I've loaded the assurance playbook and its controls-testing module, so we'll work from what's known about SOX and ICFR testing instead of starting cold. First I'll ask a few questions about your practice, one at a time. Then we'll map the work, find where AI could change it, and build a plan you can take to leadership. You can correct anything you've told me at any point.

Please don't share client-confidential data or personal information beyond names and roles. Volumes, ranges and role titles are enough.

One example from the field so you know what this is grounded in. Reddit's internal audit team reports automating 175 SOX controls in 90 days, with about 60% less testing time per control. That figure is **vendor-published and confirmed by their CAE, grade C-to-B**. It measures effort, not testing quality, and it comes from an internal audit team, not an external auditor. Most outcome figures in this space are self- or vendor-reported, and I'll label each one.

Start with your role. What are you responsible for in SOX and ICFR testing: your own engagements, a team, a practice, or a whole office or firm?

### USER
I lead the whole SOX/ICFR controls testing practice. That's 40 people: 4 managers, 10 seniors and 26 staff. We cover about 60 integrated audit clients plus 15 SOX-only internal audit outsourcing clients.

### ADVISOR
Here's what I have so far. You lead a 40-person SOX/ICFR controls testing practice: 4 managers, 10 seniors and 26 staff. It serves about 60 integrated audit clients and 15 SOX-only outsourcing clients. The two groups are paid differently and carry different independence and reliance rules. I'll treat them as separate units when we map the work.

Next, I want to know where AI use stands today. In the last two weeks, who in the practice used AI on real client work, and what did they use it for? If you can describe one specific example, that would help.

### USER
A few seniors use the enterprise chat assistant, and only on non-client material. One drafted a control narrative template and another summarized a PCAOB inspection release. Nobody has put real client evidence through it, since client data isn't allowed in the tool, and the audit platform's analytics module is used mainly for sampling. So in practice, AI isn't touching evidence review or documentation yet.

### ADVISOR
That points to the **Curious-to-Experimenting boundary**. A few named seniors use the enterprise assistant on non-client material, and there's a clear rule: no client data. But nothing is owned or measured, and no AI touches evidence review or documentation. I inferred that placement from what you described, so please correct it if it's wrong.

The client-data restriction looks like the binding constraint, more than skills or tools. Nearly every controls-testing use case in the field, such as evidence matching, attribute testing and workpaper drafting, needs client evidence to go through a tool. That will shape the plan. One of the first questions will be which tool and approval path would let that happen safely.

Why look at AI now? What's pushing you: margins, staffing, quality or inspection findings, client or competitor pressure, or something else?

### USER
Mostly margin and inspection risk. Fee pressure is real, we can't keep adding staff to absorb growth, and we got two PCAOB comments last cycle on ITGC evidence. Staff turnover is around 25%, and busy season overtime is a big part of that.

### ADVISOR
Three pressures, then: margin, inspection risk and retention. Overtime feeds the 25% turnover, and two PCAOB comments on ITGC evidence landed last cycle. ITGC testing is also where much of the field's AI effort is aimed. The Microsoft internal audit ITGC change-management agent, for example, reports 850 hours and $185K a year saved. That's **self-reported by Microsoft internal audit, grade B for effort, with nothing on quality**.

You said client data isn't allowed in the enterprise tool. Who decides whether that rule can change for a specific, certified use, and is there any route today for getting a tool approved for client evidence?

### USER
The firm's risk and quality group, together with our CIO and general counsel, signs off on any tool that touches client data. There is a vendor approval path. It needs a security review, a data-handling and retention assessment, and an independence check, and it usually takes 3 to 4 months. No one has put a controls-testing use case through it yet, so we'd be the first.

### ADVISOR
I've saved the profile to `/tmp/tmp.bl5xicpfvt/transformation-plan.md`. Here it is in brief.

- **Scope:** You lead a 40-person SOX/ICFR controls testing practice. It covers about 60 integrated audit clients and 15 SOX-only outsourcing clients.
- **Pressures:** Margin, because fees are under pressure and you can't keep adding staff. Inspection risk, from two PCAOB comments on ITGC evidence. Retention, with turnover around 25% and busy-season overtime a big driver.
- **Stage:** Curious, edging toward Experimenting. A few seniors use the enterprise assistant on non-client material. Nothing is owned or measured, and no AI touches evidence or documentation. I inferred this from your examples, not from usage records.
- **Binding constraint:** There's no approved route for client evidence in any AI tool. The vendor approval path takes 3 to 4 months, and you'd be the first controls-testing case through it. That path is the critical dependency in the plan.
- **Path:** I'd concentrate on one controls-testing workflow, with an owner, a baseline and a designed human check. I wouldn't plan an agent that owns testing yet, because it would fail four of the five readiness gates. I'd also start the approval process early.

What did I get wrong or miss?

### USER
That's mostly right. Two corrections. First, the 15 SOX-only outsourcing clients are probably the easier place to start, since independence is simpler there and we control the workpaper format. Second, don't leave out the 30% review-note rate. Review notes are a big part of the rework, and it's where our managers spend their busy-season time. Also, please make sure the plan has something for the junior staff. I don't want them to end up with nothing to learn from.

### ADVISOR
I've added all three to the plan. Onboarding is done. Two notes first.

- **The review-note rate:** You hadn't mentioned the 30% figure before this message, so nothing was dropped. It's recorded now as your number, not from a record. Later I'll ask what it's a percentage of and which note types dominate. It matters because a lot of the field's AI effort goes into testing, while your pain may sit in review and rework.
- **SOX-only outsourcing as the starting point:** That's a reasonable hypothesis and I've logged it as one. Fewer independence limits and your own workpaper format do make it easier. In the Map phase I'll check whether anything cuts the other way, such as engagement letter terms. Practitioners also report that these outsourced programs are where firms are repackaging testing as "platform plus review" (RSM, Riveron). That's a revenue question as well as an efficiency one.

Junior development is now a design requirement. I'll show it explicitly under role evolution, including what juniors do instead of tick-and-tie. The evidence here is thin and mixed, so I'll label it that way.

Next is **Frame**, where we set the ambition and what leadership will accept as proof. If this goes well, what will be different a year from now for your clients and for your people?

### USER
A year out, I'd want the SOX-only outsourcing clients running on a certified AI-assisted evidence review workflow, with staff time per control test down from roughly 1.5-2 hours to about an hour. I'd also want review-note rates cut meaningfully, say from 30% to under 20%, and no repeat PCAOB comments on ITGC evidence. For people, busy-season overtime should be noticeably lower and juniors should be doing more judgment work. For proof, leadership will want a measured baseline and a pilot comparison on actual workpapers, plus sign-off from risk and quality that the human check holds up.

### ADVISOR
I'll play that back as a draft ambition: **within a year, the SOX-only outsourcing line runs a certified AI-assisted evidence review workflow. Staff time per control test falls from about 1.5-2 hours to about 1, review notes drop from about 30% to under 20%, and there are no repeat PCAOB ITGC evidence comments. Busy-season overtime is lower, and juniors do more judgment work.** It already has quality and risk objectives beside efficiency. The proof leadership wants is a measured baseline, a pilot comparison on real workpapers, and risk and quality sign-off on the human check.

Two points to pin down later. They aren't questions for now.
- **Hours definition:** Your 1.5-2 hours is presumably per test, meaning one sample against its attributes. KPMG's survey figure of 16 hours per control (FY2024, client-reported) covers a whole control. The two aren't comparable until we agree on the unit, so the baseline needs a written definition.
- **Targets:** The 1 hour and under-20% figures are targets, not forecasts. I'll treat them as hypotheses to test against your records, and I won't treat them as a promise.

Now pricing, because it decides where the saved time goes. How is the SOX-only outsourcing work paid for: hourly, fixed fee per program, or something else? And if testing took half the effort, what would happen to that revenue?

### USER
It's mostly fixed fee per annual program, set by the number of key controls and locations, with a small number of clients on hourly rates. If testing took half the effort, we'd keep the fee on the fixed-fee clients, so the savings would go to margin. Some clients would likely ask for a reduction at renewal once they hear we're using AI. I'd want to be upfront about that rather than hide it.

### ADVISOR
Fixed fee per program, with a few hourly clients. On fixed-fee clients the saved hours become margin until renewal. The hourly clients are different: their revenue falls directly with effort. You also expect some renewal pressure and want to be upfront about it. That supports a plan with a stated position on renewals, and I'll put it into the capacity and pricing section.

Some context on the renewal risk. In a Financial Executives Research Foundation survey of 95 finance professionals, organizations that ran competitive reviews reported fee cuts of 25-30%, and the lead researcher says CFOs are asking where the AI savings are going. That is **self-reported, grade C**. Public evidence of AI-driven cuts in assurance is thin. The best-known case is a single, second-hand report of a roughly 14% fee reduction at one small audit. Your clients' renewal behavior is the real unknown, so I'll list it as an assumption to test, not a finding.

Next, boundaries. What must not change in how this work is done, and which steps must stay with a person?

### USER
Evidence selection, sufficiency conclusions, and any deficiency evaluation must stay with a person, and so must the final sign-off. The AI can pull and organize evidence, draft the documentation, and flag exceptions, but a senior or manager has to review every flagged exception and a sample of the unflagged ones. Independence and the rule that client data stays in approved tools don't change. We also can't use anything that makes the workpaper harder to defend to the PCAOB, so every AI-assisted step has to be traceable and reperformable.

### ADVISOR
Those are clear guardrails, and they match what the field's regulators say. The FRC calls them "control points", and the auditor owns the opinion. Played back:

- **Stays with a person:** evidence selection, sufficiency conclusions, deficiency evaluation and sign-off.
- **AI may do:** pull and organize evidence, draft documentation, and flag exceptions.
- **Review design:** a senior or manager reviews every flagged exception and a sample of the unflagged items.
- **Fixed rules:** independence, client data only in approved tools, and every AI-assisted step traceable and reperformable.

The unflagged-item sample is the part that does the most work. It's how you catch an AI that misses an exception. I'll make its size and the tracking of override and miss rates part of the control plan, so review can't become a rubber stamp.

Now ownership. Who would own this effort day to day, and who is the senior sponsor? What can each of them decide without going back to the firm's risk and quality group, CIO or general counsel?

### USER
I'd make myself the day-to-day owner as practice lead, with one of my four managers as the working lead on the pilot, and our managing partner for assurance as the senior sponsor. I can decide the pilot scope, which SOX-only clients go first, the review sample sizes, and the junior staff development design on my own. Anything touching the AI tool and data approvals, the audit methodology and documentation standards, the engagement letter language, or how we describe this to clients needs sign-off from risk and quality, the CIO, and general counsel.

### ADVISOR
I've written a draft of the Frame section to the plan file. The key settings:

- **Ambition:** the SOX-only outsourcing line runs a certified, AI-assisted evidence review workflow that cuts time per test and review notes, avoids repeat PCAOB comments, eases overtime, and gives juniors more judgment work. The human checks and workpaper defensibility don't weaken.
- **Value levers:** capacity 0.25, quality 0.25, risk 0.20, staff experience 0.20, margin 0.10. Quality and risk carry real weight because they're your stated pain.
- **Scoring weights:** the defaults, except risk goes up to 0.20 and time to value down to 0.05. You're inspection-exposed, and the tool approval alone takes 3-4 months, so a defensible design should beat a fast one.
- **Capacity stance (provisional): redeploy.** Freed hours go to lower overtime and better review, then to absorbing growth without adding staff, then to junior development. No reduction is planned. We'll settle it per opportunity when we build the case.
- **Pricing:** I recorded your position that fixed-fee savings go to margin, that some renewal pressure is likely, and that you'd rather be upfront about it. The renewal pressure is flagged as an assumption to test.

Do the levers, weights and redeploy stance match what you'd defend to leadership? If they do, we move to Map next. I'd start with the key-control testing flow on a recent SOX-only program, then compare it with one integrated audit engagement.

### USER
Yes, the levers, weights and redeploy stance are what I'd defend to leadership. For the redeploy stance, I'd just make sure the "no reduction planned" line says it's about staff headcount, so nobody reads it as a promise on fees. Let's move on to Map, starting with the key-control testing flow on a recent SOX-only program and then comparing it with one integrated audit engagement.

### ADVISOR
The "no reduction" line now reads "no reduction in staff headcount", with an explicit note that it is about headcount only and not a commitment on fees. Frame is saved.

We're now in **Map**. Your practice has two natural units, SOX-only outsourcing and integrated audit, so we'll map the flow in each and agree shared definitions before comparing them. Start with the SOX-only line, using a real, recent case, not the typical one.

Think of the last key control you finished testing for a SOX-only outsourcing client. What set that test off?

### USER
The last one was a quarterly access review control, specifically user access recertification for the ERP system, at a SOX-only client. It was triggered by our annual test calendar: the control owner's quarterly review completed, and our staff got a request-list item to pull the evidence. A staff person then pulls the user listing and the reviewer's sign-off from the client portal and emails the control owner for anything missing.

### ADVISOR
That is a useful case to start with. A quarterly user access recertification is an ITGC control, and ITGC evidence is where your two PCAOB comments came from.

So far: your annual test calendar and the control owner's completed review trigger a request-list item. A staff person then pulls the user listing and the reviewer's sign-off from the client portal, and emails the control owner for anything missing.

And then what? Once the staff person has the listing and sign-off, what do they do with them?

### USER
Then the staff person checks the listing against the client's active user population. They look for terminated users or people with changed roles who still have access, confirm the reviewer is the right person and signed within the deadline, and test whether any changes the reviewer requested were actually made. They paste screenshots and extracts into the workpaper, write up the test steps and conclusion, and tick off the attributes. For this one it took about 2.5 hours, mostly on the listing comparison and the writeup. Then it goes to a senior for review, and that's where most of our review notes come from, usually about missing evidence of completeness and accuracy of the listing.

### ADVISOR
I'll play back what you've told me so far, marking what I inferred.

1. **Trigger:** the annual test calendar and the control owner's completed review set it off. *(stated)*
2. **Request:** a request-list item goes out. *(stated)*
3. **Evidence pull:** staff pull the user listing and reviewer sign-off from the client portal and email the control owner for anything missing. *(stated)*
4. **Testing:** staff compare the listing with the active user population, looking for terminated or role-changed users who kept access. They confirm the reviewer and the sign-off date, and check that requested changes were made. *(stated)*
5. **Documentation:** staff paste screenshots and extracts into the workpaper, write up the steps and conclusion, and tick the attributes. *(stated)*
6. **Review:** a senior reviews it. *(stated)*

The time was about 2.5 hours of staff work on this one, mostly the listing comparison and the writeup. That's a reported figure for a single case, and it sits above your 1.5-2 hour range.

Review notes mostly say the evidence doesn't show the listing was complete and accurate. I inferred this connects to your two PCAOB comments. This is the "information produced by the entity" problem, and the 2025 IFIAR inspection findings counted 43 such data and IPE findings at the six largest networks (regulator-published, grade A). Testing the control may not be the weak step. The proof that the listing itself is reliable may be. I'll test this in Diagnose.

For that same case, how many days passed from the request-list item going out to the senior finishing their review?

### USER
About 11 days from the request-list item going out to the senior finishing their review. Most of that was waiting: roughly 4 days for the control owner to send the missing listing support, then about 5 days in the senior's review queue, with the actual staff work spread across a couple of days.

### ADVISOR
That gives the elapsed and hands-on split for this case (reported, one instance):

| Stage | Elapsed | Of which hands-on |
|---|---|---|
| Waiting on the control owner for listing support | about 4 days | none (chasing aside) |
| Staff testing and writeup | spread over about 2 days | about 2.5 hours |
| Waiting in the senior's review queue | about 5 days | senior's review time not yet known |
| **Total, request to review finished** | **about 11 days** | |

About 9 of the 11 days, roughly 80%, were waiting. The staff work was a small slice. This supports a split in the problem. Part of it is waiting on the client for completeness-and-accuracy support, and part is waiting in the review queue. The second part is a capacity and busy-season question as much as a testing one.

Those 4 days waiting on the control owner may matter more than the 2.5 hours of testing. The missing support is probably the same listing-completeness evidence that drives the review notes. If so, the earlier the missing piece is requested, the fewer days of waiting and the fewer notes.

What review notes did the senior write on that one, and what happened to them?

### USER
The senior wrote three notes: the listing had no evidence it was complete and accurate (no report parameters or system-generated proof), the reviewer's sign-off date wasn't tied to the deadline in the policy, and one removed-user exception wasn't traced to the ticket showing access was actually revoked. Staff fixed them by going back to the control owner for the report parameters and a re-run of the listing, which took another 2 days after the review, so I think the real finish was closer to 13 days. That's typical for us, and it usually costs a second round of review from the senior.

### ADVISOR
Here is the full flow for this case, with each time labelled.

| Step | Who | Elapsed | Hands-on | Label |
|---|---|---|---|---|
| Request-list item goes out | Staff | day 0 | not asked | stated |
| Wait for control owner's missing listing support | Client | about 4 days | none | reported |
| Compare listing with active users, check reviewer and sign-off, test requested changes, write up and tick attributes | Staff | about 2 days, spread | about 2.5 hours | reported |
| Senior queue, then review | Senior | about 5 days | not asked | reported |
| Fix three review notes (re-run listing with parameters, tie sign-off date to policy, trace exception to ticket) | Staff and control owner | about 2 days | not asked | reported |
| Second round of senior review | Senior | not asked | not asked | stated, "usually" |
| **Total** | | **about 13 days** (estimate) | | reported |

All three notes were checks against evidence completeness or a written rule: listing parameters, the policy deadline, and the ticket trail. None was a disagreement about the conclusion. That pattern goes into Diagnose as a hypothesis to test. If it holds across more files, much of the rework comes from evidence gaps visible before the work reaches the senior, not from errors of judgment.

You called this case typical. How many control tests did the SOX-only team finish last month, and can we look at the record?

### USER
Last month the SOX-only team finished about 210 control tests, roughly 60 of them ITGC. I can't share the actual workpapers or client records here, but I can give you a rough breakdown from our tracking sheet: about 30% drew review notes, and around two-thirds of those were evidence completeness or IPE issues.

### ADVISOR
Thanks. Aggregate counts are what I need, and I don't need the workpapers. Here is what they imply, labelled as aggregate figures from your tracking sheet that I haven't seen.

| Measure | Value | Label |
|---|---|---|
| Control tests finished last month, SOX-only line | about 210 | from record (tracking sheet), as relayed |
| Of which ITGC | about 60 (about 29%) | same |
| Tests drawing at least one review note | about 30%, so about 63 | same |
| Of those, evidence completeness or IPE issues | about two-thirds, so about 42 (about 20% of all tests) | same |

This also pins down the review-note rate you mentioned earlier. It is the share of control tests drawing at least one note. I'll use that definition from now on.

The arithmetic matters for your target. If those 42 evidence-completeness notes disappeared and nothing else changed, the note rate would fall from about 30% to about 10%. That is well under your under-20% goal. So the target depends mostly on one failure type, not on improving everything. This is a hypothesis from rough aggregates, not a forecast. It assumes the same tests don't also draw other notes, and I'd want to check that against the sheet.

Next is the hidden work. What does the staff person or the senior check on a test like this that isn't written in any procedure?

### USER
Beyond the procedure, the senior mentally checks whether the listing came straight from the system rather than something the control owner edited in Excel. They also check that the report date range covers the whole period, and that the "active user population" used for comparison is itself complete. Staff learn to spot these from experience, and honestly it's mostly what separates a good senior from a new staff person. None of it is written down, and I'd worry about how we'd teach it to juniors if a tool starts doing the first pass.

### ADVISOR
Now the comparison. Think of the last ITGC access review you finished on an integrated audit engagement. How did that one differ from the SOX-only case?

### USER
On the last integrated-audit ITGC access review I finished, the listing came from the client's IT team through our audit platform's request portal, and our IT audit specialist had already tested the report parameters once for the whole engagement. So staff only compared the listing to active users and didn't re-prove completeness on each test. That took about 1.5 hours and drew no review notes. Review sat in the senior's queue only 2 days, since the integrated team is staffed more tightly in busy season.

### ADVISOR
That comparison is useful. It changes the story.

| | SOX-only (sample case) | Integrated audit (sample case) |
|---|---|---|
| Listing source | client portal, plus emails to the control owner | client IT team through the audit platform's request portal |
| Completeness and accuracy of the report | re-proved on each test | tested once per engagement by the IT audit specialist |
| Staff hands-on | about 2.5 h | about 1.5 h |
| Review notes | 3 | none |
| Senior queue | about 5 days | about 2 days |

*(Both reported, one case each.)*

I read this as a structural difference, not a skill difference. In the integrated audit the completeness question is answered once and reused. In the SOX-only line each staff member answers it again on every test, with whatever the control owner sends, and the senior catches the gaps. That points to an improvement that isn't AI at all: validate each key report once and reuse it across tests. AI could then do the repeated part, comparing listings and drafting the write-up, with a proven report underneath. Both cases are single instances, and the engagements differ in season, staffing and client. I'll treat this as a hypothesis until a few more cases or the tracking sheet support it.

Does the SOX-only team have anything like that one-time report testing, and if not, what stops it?

### USER
No, we don't have anything like that on the SOX-only side. Each engagement team handles its own clients, and nobody owns report validation. The IT audit specialists are billed to the integrated engagements, so we rarely have them. There's also no shared place to keep a validated report, so every test starts over.

I think we could get a specialist for a few hours per client if we scoped it up front. I'd want to know how many key reports are really involved, though. Can you help me estimate that?

### ADVISOR
I can set up the estimate, but I can't produce the number. I don't know your clients' report counts, and I won't invent one. Here is the method, then the one thing I need from you.

**What counts as a key report.** A system-generated report that a key control relies on, or that you rely on as evidence. User listings are the obvious case. Others are change tickets, job schedules, aged-item reports and exception reports. Count each distinct report once per client system, however many controls use it. A report that feeds four controls is one validation.

**Estimating the load:**

> specialist hours = clients × distinct key reports per client × hours to validate one report, plus re-validation when a report or its system changes

With 15 SOX-only clients, the table below shows the range. **The report counts and hours are placeholders, not data.**

| Distinct key reports per client | Hours per report | Total specialist hours (15 clients) |
|---|---|---|
| 5 | 2 | 150 |
| 8 | 3 | 360 |
| 12 | 4 | 720 |

The answer swings about fivefold on those two inputs, so a few real counts will pin it down much better than any benchmark.

Two caveats for the plan:
- **Re-validation is part of the cost.** A once-per-engagement test of a report only holds if the report and the system behind it don't change in a way that matters. Whoever owns validation must also track changes, and that links back to the change-management ITGC.
- **A register of validated reports is a reusable asset.** It gives staff something to point to instead of starting over. It would also be the foundation any later tool depends on.

The one input I need: for a representative SOX-only client, roughly how many key controls are in scope, and how many of them rely on a system-generated report? Counts are enough, and no names or client details are needed.

### USER
For a representative SOX-only client, we'd have around 25 key controls in scope, and I'd guess 12 to 15 of them rely on a system-generated report. Those probably collapse to about 8 distinct key reports, since the user listings and change reports get reused across several controls. I'd take 3 hours per report as a working default for now, so that's roughly 360 specialist hours across the 15 clients.

### ADVISOR
Your numbers check out: 15 clients × 8 reports × 3 hours is 360 specialist hours. I've saved it to the plan with these labels:

- **Source:** your estimates, reported, not from records.
- **Sensitivity:** on your own inputs, 6-10 reports at 2-4 hours each gives about 180-600 hours.
- **Not included:** re-validation when a report or its system changes, and coordination time. The 360 is a first-time cost, not an annual one.

For scale, your tracking sheet implies about 42 control tests a month with evidence-completeness notes. Each one costs a rework loop of about 2 days elapsed and a second senior review. If you can tell me the extra staff and senior hours for that loop, we can compare it with the 360 hours. I'll ask for that in the business case, so you don't need it now.

The Map is nearly complete, and the next questions feed Diagnose. Think about the SOX-only flow we just walked through, from request to second-round review. Which steps are mostly looking things up, copying, formatting or chasing, and which depend on someone's judgment?

### USER
Mostly lookup and chasing: pulling the listing from the portal, emailing the control owner for the right version, comparing it to the active user list, copying results into the workpaper template, formatting and tickmarking, and following up when the senior's note comes back. The judgment parts are deciding whether the listing is complete and system-generated, whether an exception is a real deficiency or a timing difference, and what the senior concludes on deficiency severity. I'd guess 60-65% of staff time is the first group and the judgment sits mostly with the seniors and managers.

### ADVISOR
I've saved Map to the plan, and created the SOX-only unit brief at `/tmp/tmp.bl5xicpfvt/units/sox-only-outsourcing/brief.md`.

**One observation to confirm.** Your own split shows the first judgment item is deciding whether the listing is complete and system-generated. It currently sits with the senior at review, after staff have done all the lookups. The three notes on the sample case and roughly two-thirds of the notes in your tracking sheet are about exactly that item. The judgment arrives late, so the rework comes late too.

**Your 60-65% guess** that lookup, copying and chasing is staff time is a reported estimate, not a measurement. I've marked it that way. It should be checked with a time sample on the pilot.

**Units:** I've set two, split by client type and engagement model.
- **SOX-only outsourcing (15 clients):** wave 1, in progress.
- **Integrated audit ICFR testing (about 60 clients):** wave 2, not started.

Both inherit your levers, weights and guardrails, and both use the shared definitions of control test, review-note rate and hands-on time.

For planning mode, I've proposed that you go deep on the SOX-only unit yourself with your pilot manager, and that I draft a first-pass desk review of integrated audit labelled "draft to validate". Is that the right way to plan the two units, or would you rather one of your managers plan integrated audit themselves?

### USER
Your proposal works for me. I'll go deep on SOX-only with my pilot manager, and you can draft the integrated audit desk review labelled "draft to validate". I'd have one of my integrated-audit managers review that draft before it goes to the leadership team. Let's continue.

### ADVISOR
The integrated audit desk review has finished and is saved in `units/integrated-audit/`. The files are `desk-review.md` and `opportunities.yaml`. It's marked **draft to validate**, and the plan notes that one of your integrated-audit managers must review it before it goes to the leadership team.

- **Main opportunity:** a register of specialist-validated reports, the "validated once" pattern from your sample case. It would be standardised, recorded and lent to the SOX-only line.
- **Second option:** a written pre-review checklist that captures your seniors' unwritten checks.
- **Smaller or later options:** shared use of the chat assistant on non-client material, and a certified comparison tool. That tool waits for the 3-4 month approval path and for the first two options.
- **Parked:** AI secondary review of the workpapers.
- **Not planned:** any tool that tests controls on its own. The practice doesn't meet the readiness gates for that yet.

Some caveats:
- I rechecked the weighted scores against your weights and the arithmetic holds.
- I haven't validated the YAML against the plan schema, and I've flagged that in the file.
- It relies on a single sample case from you, and the evidence grades will be re-checked later.
- The Microsoft ITGC agent figure is self-reported by the team that deployed it. I removed the stronger "grade A" label the draft had given it.
- Treat the integrated-audit numbers as hypotheses. They are not the same as the SOX-only tracking-sheet figures.

Your question is still open. During the weeks when the review queue builds, how booked are your seniors, and what happens to the queue when they get busier?

### USER
During busy season my seniors run about 90-95% utilized, and in the weeks when the queue builds, they're reviewing roughly 25-30 workpapers each on top of their own testing. When they get busier, the queue just sits. Staff wait 3-5 days for a review note, and the second-round notes get squeezed into evenings and weekends. Let's keep going.

### ADVISOR
I've written a draft of the Diagnose section to the plan. The shortlist for the next phase is five steps:

1. **Senior review demand:** reduce the files and second rounds that reach the seniors. This is the constraint.
2. **Report completeness proof:** validate each report once and reuse it, and write the three unwritten checks down as criteria.
3. **Evidence request and chase:** get the right report and parameters first time.
4. **Listing comparison and write-up first pass:** only after steps 1 and 2 and the approval path.
5. **Junior development:** how juniors keep learning the seniors' checks.

A note on the table: the "desire" column and the frontier test are still empty, so the AI-fit assessment is incomplete. The desire column is for what your people would hand over and what they'd keep.

Of the lookup, copying and chasing steps, which would your staff gladly hand over, which would they want to share with a tool, and which should stay with a person even though they are routine?

### USER
Staff would gladly hand over the portal pulls, copying results into the workpaper template, formatting and tickmarking, and the first-pass comparison of the listing to the active user list. They'd want to share with a tool the chasing, meaning drafting the request to the control owner and tracking follow-ups, as long as a person still sends it and owns the relationship. They'd keep the check that a report is complete and system-generated, and the call on whether an exception is a timing difference. Those are routine, but that's where juniors learn what the seniors look for, so I'm wary of automating them away.

### ADVISOR
A correction first. At the start I said the Reddit result was "grade C-to-B", and I described Microsoft's ITGC agent as "grade B for effort". The archetype's use-case file actually grades both use cases (#05 and #06) **A**, meaning in production and named. The figures inside them are still vendor-published or self-reported by the deploying team, and they measure effort saved, not testing quality. Grade A describes how well documented the use case is. It isn't a quality guarantee. I've now corrected that in the Reimagine table.

We're now in **Reimagine**. At your stage (Curious edging to Experimenting) I go deep on lenses 1 and 2, improving a step and automating a flow. Delegating an outcome and reinventing the service appear as target pictures, not plans. I haven't hunted for new use cases beyond the ones already in the archetype, because the integrated-audit scout and the module cover this ground. Here is the draft option list for the SOX-only unit. The grades are from the archetype's use-case file, and none of these has been scored yet.

| # | Lens | Option | Ladder / scope | Evidence |
|---|---|---|---|---|
| 1 | Improve | Written pre-review evidence checklist: system-generated, full period, complete population, deadline tie, exception-to-ticket trace. No AI needed, which is a plain process change | assist / step | Your own tacit checks; #10 for the review pattern (B) |
| 2 | Improve | Request template that names the report and its parameters up front, plus a rule-based check when evidence arrives | assist / step | #03 (C, piloting, vendor claim). Template first, no AI |
| 3 | Improve | Shared tool drafts requests to control owners and tracks follow-ups; a person sends and owns the relationship | assist / step | #03 (C) |
| 4 | Improve | One specialist validates each key report once, recorded in a register and reused | assist / process | Your integrated-audit case (reported, one case). No archetype use case |
| 5 | Automate | Certified tool does the portal pull, listing-to-active-user comparison and workpaper first pass; every flagged exception and a sample of unflagged ones go to a person | augment / step | #06 (A, self-reported by Microsoft IA), #07 (B, measured cases are mostly substantive). Needs the approval path first |
| 6 | Improve | AI secondary review of the workpaper before the senior sees it | augment / step | #10 (B, qualitative only). Parked until option 5's tool is approved |
| 7 | Improve | Junior development design: juniors keep running the completeness check and timing-difference call, with synthetic practice cases and coaching against the checklist | assist / process | Mixed evidence, labelled as such; a design choice, not a tool |
| 8 | Delegate | An agent tests a defined control set with cited evidence and a reviewer signs off | delegate / process | #05 (A), #16 (B). Target picture only: you fail four of the five gates today |
| 9 | Reinvent | Controls testing sold as platform plus review instead of hours inside a program fee; or clients in-sourcing the testing | delegate / model | #20 (B), #19 (B). Hypotheses, not plans |

**Order matters because of the constraint.** Options 1, 2 and 4 cut the files and second rounds reaching your seniors, so they come before option 5, which would speed staff up and add to the queue.

Which of these would you keep, change or drop?

### USER
I'd keep 1, 2, 3, 4, 5 and 7, and I'd drop 6, 8 and 9 from the plan and leave them as parked target pictures. On option 7, I want the junior development design to be a named workstream with its own owner, because that's what I'll get asked about first. Let's continue to scoring.

### ADVISOR
I've scored the six options you kept, and saved the details to the SOX-only unit's `opportunities.yaml` and to the plan. Options 6, 8 and 9 are parked as target pictures, as you decided.

| Option | Score (of 5) | Category |
|---|---|---|
| 1 Pre-review evidence checklist | 4.55 | foundation |
| 2 Request template and arrival check | 4.15 | quick win |
| 7 Junior-development workstream | 3.90 | quick win |
| 4 Report validation register | 3.70 | foundation |
| 10 Client-data approval path (new, see below) | 3.15 | foundation |
| 3 Chase assistant | 3.15 | parked, with a trigger to return |
| 5 Certified listing tool | 2.55 | parked until 1, 4 and 10 are done |

**Two points need your attention.**
- **I added option 10.** Options 3 and 5 can't start without a controls-testing use through the 3-4 month client-data approval path. I made that its own foundation item, starting with a narrow scope such as user access recertification at one or two clients. You didn't ask for it, so confirm or remove it.
- **Options 3 and 5 are kept in the plan but scored as "park".** In this method, "park" means "not now, with a trigger to come back", not "dropped". Option 5 scores low because it speeds a staff step, while your constraint is the senior queue, and because it needs approval and written criteria first. Option 3 has a low end of zero hours saved. Both stay in the sequence as Later.

**Don't add the quality values of options 1, 2 and 4.** They attack the same evidence-completeness notes, about 42 of your 210 monthly tests, or roughly 20 of your 30 percentage points. The combined ceiling is about 10% on the note rate. Reaching your under-20% target needs roughly half of the evidence notes caught, about 10 points.

**Sequence, by dependency.** Now: options 1, 2, 10's request, 4's scoping, and naming 7's owner and baselines. Next: option 4 for the first clients. Later: option 5, in shadow mode. Seniors are booked 90-95% in busy season, so writing the checklist needs protected time outside peak weeks.

**What could change the order:**
- How many of the evidence notes the checklist and register actually catch.
- Whether specialist hours are available.
- Whether the integrated-audit pattern is structural or just one case.
- Whether clients ask for fee cuts.

Which three to five of these do you want built into full business cases? My suggestion is options 1, 2 and 4 as one evidence-completeness package, then 7, then 10 with 5 as a staged item. Does that match your gut?

### USER
Yes, that matches my gut. Confirm option 10 and keep it as a foundation item. Build full business cases for options 1, 2 and 4 as one evidence-completeness package, then 7 as its own workstream, then 10 with 5 as a staged item. For the checklist, I can protect two or three senior half-days in the shoulder weeks before busy season, but not during peak.

### ADVISOR
I've confirmed option 10 as a foundation item and written draft business cases for all three. They are in the Make the case section of `transformation-plan.md`. The protected half-days you offered are in the cost lines: 2-3 half-days in the shoulder weeks, none in peak.

**Case A: the evidence-completeness package (options 1, 2 and 4)**
- **Note rate:** the package could take 5-15 points off the 30%, and your under-20% target needs at least 10 of them.
- **Second-round reviews:** 10-32 fewer per month for your seniors.
- **Staff hours:** 25-125 hours a month released.
- **First-season cost:** about 240-780 hours, mostly specialist time.
- **Payback:** in hours only, roughly 2 to 26 months. That's wide because the specialist hours and the staff-hours saving are both uncertain.
- **Cheapest proof:** a back-test of the draft checklist against past files with known notes. It costs nothing new and tells you how many of the evidence notes it would have caught.

**Case B: the junior-development workstream (option 7)**
- **Consumes capacity:** it uses released senior hours for coaching.
- **Measures:** judgment-time share, readiness, overtime and turnover. All need baselines first, and I haven't set targets.
- **Design commitments:** juniors keep the completeness check and the timing-difference call. They explain tool output back before it's used, and a rotating sample of comparisons stays manual.
- **Evidence:** mixed, and flagged that way. I haven't named an owner; I'll ask in the Plan phase.

**Case C: the approval path and listing tool as a staged item (options 10 and 5)**
- **Stages:** approval request, shadow mode on past tests, limited live use, then a decision to widen.
- **Capacity:** 38-158 staff hours a month, but only after Case A has relieved the senior queue.
- **Not planned:** an agent that owns testing.

**Your 1-hour target needs both the package and the tool.** The package alone takes about 0.1-0.6 hours off the average across all tests, and the tool alone about 0.2-0.75. Both go after lookup and compare work, so they don't add up. Getting from 1.5 hours to 1 is plausible. Getting from 2 hours to 1 needs most of both at their high ends.

Any figure marked [placeholder] is my assumption, not your data, and should be replaced with records. I haven't run the optional independent review of the cases. I can do that before leadership sees them if you want a second read.

Looking at those three cases, which line would a finance lead or your risk and quality group challenge first?

### USER
The finance lead would challenge the specialist hours first. That's the 240-780 first-season cost, and it's also why payback runs from 2 to 26 months. I'd want that range narrowed. Can we pin down who the specialist is, how many hours they'd realistically have, and what those hours are worth if they come off billable work? Risk and quality would go straight to whether the back-test can show the checklist would have caught the ITGC evidence issues behind our two PCAOB comments. If you want the independent review of the cases before leadership sees them, run it.

### ADVISOR
The independent review is finished. All three cases came back "ready with changes". I checked the reviewers' key citations against the archetype files before applying anything, and they were right on the points that matter. I've updated the plan and `opportunities.yaml`.

**Corrections to my own work:**
- **Wrong evidence for Case B.** I cited use case #21 for the junior workstream, but it's about SOX practitioners building agent evaluation sets. The "first-years doing complex testing" claim is a partner's statement in a vendor customer story about one 20-person firm. That makes it vendor-published, archetype grade B. I had called it "self-reported, grade C". Both are fixed.
- **Staff-hours ceiling lowered.** The upper end for the report register drops from 125 to 63 hours a month. The 1.0-hour saving per test came from two single cases and would be 50-67% of a typical test.
- **Payback widened.** It runs about 4 to 31 months on staff hours alone, or 5 to 45 months once the share absorbed into other work is netted out. My earlier 2-to-26 figure mixed staff and senior hours. The range is wide because both the specialist cost and the saving are uncertain, which is why I'm staging the spend.
- **Your 1-hour target.** It looks like a stretch. From 1.5 hours it needs the upper half of what both the package and the tool could deliver. From 2 hours it is beyond what these cases support. I told you earlier it was "plausible" and that was too generous.

**Category changes:**
- **Option 4, the report register:** moved from foundation to a staged big bet, because only one option depends on it. That fits "validate one client first".
- **Option 5, the listing tool:** value drops to 2, so it stays parked at 2.25.
- **Option 10, the approval path:** the rules alone would park it. I kept it as a foundation because you decided so, and it is the lead-time item for option 5.
- **Case C:** it now asks only for stage 0, the approval request. Later stages are a conditional target picture.

**Still waiting on you:**
1. **Option 7 scores.** The reviewer suggests value 3 to 2, feasibility 4 to 3 and time to value 4 to 3, because protected coaching time isn't secured while seniors are booked 90-95%. Value 2 would park it. You can still keep it as a named workstream with that reason recorded.
2. **Option 2.** Is the per-client report list already available? If not, data readiness drops to 3 and it loses quick-win status.
3. **Specialist hours.** Your "a few hours per client" doesn't match the roughly 24 hours per client (8 reports × 3 hours) in the base estimate. I also still need who supplies and approves the hours, who owns the register and its re-validation triggers, and the rate.
4. **Junior hiring pace.** No change is assumed in any figure; please confirm.

My open question from before still stands, and it is the most useful one: which role or group would supply the validation hours, and how many hours a week could they realistically give outside peak?

### USER
The specialist would be one of my four managers, ideally a senior manager on the ITGC side. I could give about 4 hours a week outside peak, so roughly 8 weeks to cover the first 6 to 8 clients. I'd cost it at a blended rate of about $210 an hour, and since most of it comes off billable work, count it as a real cost. Please narrow the range using 24 hours per client for the first client only, then 12 to 16 for later ones as the reports get reused.

On your other points: option 2's per-client report list isn't available yet, so drop its data readiness to 3 and take it off quick-win. Keep option 7 as a named workstream with the reason recorded. I'll name a senior manager as its owner, and the register owner would be the same manager as the specialist. No change in junior hiring pace.

### ADVISOR
I've applied your numbers. The narrowed cost is solid, but your pace assumption doesn't fit your own hours.

**Narrowed specialist cost.** With 24 hours for the first client and 12-16 for each of the other 14 (your reuse estimate, untested), validation takes 192-248 hours. At your blended $210 an hour, counted as real cost:

| Scope | Hours | Cost |
|---|---|---|
| First client only | 24 | $5,040 |
| 6-8 clients | 84-136 | $17,640-$28,560 |
| All 15 clients | 192-248 | $40,320-$52,080 |

The first-season total across the whole package narrows from 240-780 hours to about **254-432 hours**. Once all 15 clients are validated, payback on staff hours alone is roughly 4-17 months, or 5-25 months after netting out the share absorbed into other work. That is hours, not value. The cost hours are manager time at $210 and the benefit hours are staff time at a lower rate I don't have, so the real payback is probably longer. The benefit also arrives client by client over the whole validation period, so measured from the start it is longer again. I haven't modelled that.

**The pace doesn't fit.** Four hours a week for 8 weeks is 32 hours. That covers the first client (24 hours) and about half of a second one, not 6 to 8 clients. Six to eight clients need 84-136 hours, about 21-34 weeks at 4 hours a week. All 15 clients need about 48-62 weeks, roughly 11-14 months outside peak.

**Your other decisions, applied:**
- **Option 2:** data readiness is now 3, so it's no longer a quick win. The rules park it with a trigger: the per-client report inventory. In practice it starts client by client as each inventory completes.
- **Option 7:** kept as a named workstream. I used the reviewer's lower scores (value 2, feasibility 3, time to value 3). The rules alone would park it, so I recorded your decision and the reason: it's a stated design requirement and the guard on the junior pipeline. Option 5 now depends on it.
- **Roles and hiring:** the register owner and validator is one senior manager on the ITGC side. The option 7 owner is a senior manager to be named, and no change in junior hiring pace is assumed.

Risk and quality needs to confirm that a senior manager can sign a validation record, since IT audit specialists are billed to integrated engagements.

Do you want to resolve the pace by giving more hours a week, adding a second trained validator for the routine reports, or starting with fewer clients, such as the ones behind your ITGC controls and the two PCAOB comments?

### USER
Let's start with fewer clients: the ones behind our ITGC controls and the two PCAOB comments, probably 4 to 5 clients. That fits 4 hours a week and gives the back-test a direct answer for risk and quality. I'll check with risk and quality on whether a senior manager can sign the validation record, and a second trained validator for the routine reports can come in the next phase.

### ADVISOR
Stage 1 is saved in Case A. It starts with the 4-5 clients behind your ITGC controls and the two PCAOB comments.

**Stage 1 numbers:**
- **Validation:** 24 hours for the first client plus 12-16 for each of the other 3-4. That is 60-88 hours, or $12,600-$18,480 at $210 an hour.
- **Calendar:** at 4 hours a week, that's about 15-22 weeks outside peak. The weekly hours fit, but this is four to five months of off-peak weeks, not 8 weeks.
- **All lines:** the whole stage costs about 122-272 hours, including the checklist, pilot manager time, training and the parallel run. The training and parallel-run lines are my placeholders.
- **Benefit:** about 7-21 staff hours a month if it scales with 4-5 of 15 clients. It could be higher if these clients are heavy on ITGC, but I don't know that.

Stage 1 isn't built to pay back. Its job is to produce measured hours per client and a direct answer for risk and quality from the back-test. I've proposed stage 2 go/no-go criteria in the file for you to set before starting. A second trained validator stays a later-phase option.

**Make the case is complete.** You made detailed decisions on every case, so I'm treating them as confirmed with those changes. Tell me if you want to reopen any.

We're now in **Plan**, the last phase. It sets owners, the first actions that need nobody else's approval, a control plan and KPIs for each live option, the review rhythm, what you tell your people, and a summary you can paste for leadership.

Who will own the checklist and the request template, and can that person commit the protected senior half-days without anyone else's approval?

### USER
I'd own the checklist and request template myself, and I can commit the two or three senior half-days in the shoulder weeks without anyone else's approval. I'll schedule them this week. Please put me down as owner, and add the ITGC senior manager as the person who validates the checklist against past files.

### ADVISOR
You're recorded as owner of options 1 and 2, and the ITGC senior manager is recorded as the person who validates the checklist against past files. Scheduling the protected half-days this week is the first "Now" step, and it needs nobody else's approval. The next steps in the unit's `opportunities.yaml` now show you as owner of the checklist and the request template. The template now depends on the report inventory existing for a client.

**Two flags** (also in the plan's open questions):
- **The ITGC senior manager now holds two jobs.** They are the validator and register owner at about 4 hours a week, and now the checklist back-tester. Unless the back-test hours are budgeted separately, they come out of the same 4 hours and stretch stage 1 beyond the 15-22 weeks I calculated. I had put the back-test inside the pilot manager's 16-40 placeholder hours, which no longer matches who is doing it.
- **The back-test has to stay blind.** The ITGC senior manager should apply the frozen checklist to the original files without having read the PCAOB comment text. Otherwise risk and quality can't rely on the answer.

I also need to know whether the "pilot working lead" role is still needed now that you own options 1 and 2.

Now the review rhythm. Who will look at the results (the note rate, hands-on hours, the back-test outcome and the validation hours), how often, and in which meeting?

### USER
I'd review it in our monthly practice leadership meeting, with the four managers and me. The ITGC senior manager would bring the numbers. Note rate, hands-on hours per test and validation hours would be a standing item each month, and the back-test result would be a one-off review when it's done.

On the flags, back-test hours should be budgeted separately so they don't eat the 4 hours a week. Add about 2 hours a week for 8 weeks, and plan the back-test to be blind. The pilot working lead role isn't needed now that I own options 1 and 2, so drop it.

### ADVISOR
I've recorded your answers and written a draft Plan section. One question is still open before it's finished.

**Applied from your answers:**
- **Review rhythm:** your monthly practice leadership meeting, with you and the four managers. The ITGC senior manager brings the numbers. The note rate, hands-on hours per test and validation hours are a standing item. The back-test result is a one-off review.
- **Back-test:** budgeted separately at 2 hours a week for 8 weeks, so 16 hours. It is planned blind: risk and quality supply the files behind the two comments mixed in with files that drew no comment, and the reviewer doesn't read the comment text. During those 8 weeks the ITGC senior manager carries about 6 hours a week.
- **Pilot working lead role:** dropped everywhere it appeared.
- **Cost:** stage 1 now totals about 138-288 hours. The first-season total across everything is about 270-448 hours.

**Structure of the Plan draft:**
- **Now:** seven steps, none needing anyone else's approval. These include the half-days you'll schedule this week, the baselines and time sample, the first report inventory, the narrow approval request, your check with risk and quality, and naming the option 7 owner.
- **Next:** eight steps, including the blind back-test, the remaining stage-1 validations, the client-by-client request template, the pilot comparison and the stage 2 go/no-go.
- **Later:** option 3, option 5 in shadow mode, and the value review.
- **Control plan:** a table with a metric, baseline, owner, rhythm and response for each live option.
- **Next stage:** Experimenting, with three exit criteria. Most of this plan is process change, not AI, and the criteria say so.

I proposed a weekly 15-minute check, a quarterly value review for the managing partner, and a mid-point reset. These are marked as proposals, not your decisions.

The remaining question: what will you tell your people, and when? The draft proposes a short "what we know, what we don't, what we commit to" note before the checklist work begins. It also asks each manager what they'd say if someone asked whether their job is safe. Do you want to keep that shape, or change it?

### USER
Keep that shape. I'd send the note to all 40 people the week before the checklist work starts. I'd say plainly that we're not cutting staff and not changing junior hiring pace. I'd also say we don't yet know how much time this saves, and that we'll share the measured results after the back-test. I'll ask each manager to tell me in a sentence how they'd answer the "is my job safe" question, and we'll align on it before the note goes out.

### ADVISOR
The plan is complete for the SOX-only unit, and it's saved in `/tmp/tmp.bl5xicpfvt`.

I've added your decisions: keep the "what we know, what we don't, what we commit to" shape, send the note to all 40 people the week before the checklist work starts, and have each manager give you a one-sentence answer to "is my job safe?" so you align before it goes out. Sharing the measured results after the back-test is now a step in the plan. I wrote a draft note for you to edit and added a step to share the measured results after the back-test.

**One caution on the note.** Only promise what you can stand behind and fund. I'd phrase it as "as part of this work", say when you'll review the statement again, and confirm your managing partner backs the headcount and hiring lines for that period. The note shouldn't say anything about fees.

**Files to share:**
- `transformation-plan.md` is the main document. It has the Leadership summary, the Plan and the three business cases.
- `units/sox-only-outsourcing/opportunities.yaml` and `brief.md` are the supporting detail.
- `units/integrated-audit/` is only a desk review, labelled "draft to validate". Don't share it with leadership until one of your integrated-audit managers has reviewed it.

The folder isn't a git repository, so copying the files to your shared location is the way to go. None of the files contains client data.

**What isn't done:**
- **No merged roll-up.** I didn't merge the integrated-audit items into a single practice-level opportunities file. The overlap with the checklist and register items is noted, but the two unit files stand separately.
- **Placeholders remain.** Some cost lines are mine, flagged "[placeholder]", and the benefit hours aren't priced. Finance needs to give an internal rate for staff hours.
- **Evidence limits.** Everything rests on one sample case, tracking-sheet aggregates as you relayed them, and field examples that are mostly self- or vendor-reported. The 1-hour target is a stretch.
- **Your first moves.** Schedule the senior half-days this week and ask risk and quality whether a senior manager can sign validation records. Name the option 7 owner, and settle whether that person is also the ITGC senior manager.

### END
session 807fbf4d-3850-5c6c-82b1-8d3750715cd5, turns 32
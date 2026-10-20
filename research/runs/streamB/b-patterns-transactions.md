# Backbone library research: agentic patterns `document-to-decision` and `reconcile-exceptions`

Run date: 2026-10-20. Stream B, brief `b-patterns-transactions`. Kind: agentic patterns. Items: `document-to-decision`, `reconcile-exceptions`.

How to read this file. Every sourced claim carries a ref in square brackets with a locator, and refs resolve in section 7. Statements marked **(advisor inference)** are design judgments that no source states; they are labelled so the library does not pass them on as findings. Figures are tagged `self-reported`, `vendor-published` or `independent` where they matter. "Adjacent" means the measured system was rule-based automation rather than AI, so the grade is capped at B. Dates: the Annex III dates below are those the Act Explorer displays; see Gaps for the adoption status of the delay.

Source mix: 43 sources opened and read (`access: full`): regulators, courts and legal texts (14), vendor documentation and vendor case studies (9), press and named-organization reporting (5), academic (4), standard-setters (3), law-firm, consulting-firm and partner-firm writing (3), surveys and research firms (2), and one each of a conference-talk summary, a professional body and a practitioner community thread. A further 6 sightings were search-only and are not relied on (section 7).

---

## 1. Summary

- **Both patterns are mature at the step level and thin on measured quality.** Of 15 cross-industry examples, none reaches grade A (8 are B, 7 are C). Every A in the archetype library for these patterns comes from assurance and security work (for example `assurance-controls-testing-05`, `assurance-completion-reporting-06`). No source found publishes an override rate, an escalation rate and an error rate for an LLM document-to-decision deployment together. The only escalation figure is a vendor's 10-15% [RAMP-AGENTS-2025, "Meet Ramp's first set of agents"].
- **The best quality evidence is an independent audit of a failure.** The VA Inspector General found 27% of 60 sampled automated hypertension claims (16 of 60) had inaccurate decisions, and the summary sheets the tool produced were deficient in 37% and 57% of two samples. The programme's internal review of the summary sheet reported 100% accuracy, and OIG attributed the disparity mainly to VBA's two quality-assurance programmes not tailoring their sampling to the automated claims [VAOIG-ABD-2023, pp. iii, 6, 17-18]. The same system is rule-based, so it is adjacent evidence, but the design lesson transfers: measure the automated stream with its own sampling plan, run by someone other than the builder.
- **Extraction confidence is the hard engineering problem, and the common shortcut fails.** On a 55-field invoice benchmark where frontier models failed on 26% of fields, token log-probabilities separated right from wrong answers only weakly (0.705 ROC AUC). A multi-signal engine reached 99.1% accuracy on the 80% of fields it automated, against a 73.3% base rate [KUMAR-EXTRACTCONF-2026, abstract, §1, §6.2; author is at a vendor, so treat as vendor-affiliated]. Advisors should ask how confidence is computed per field, not whether the model "is accurate".
- **A human in the loop is not the same as human oversight.** Cigna doctors reportedly spent an average of 1.2 seconds per case on bulk denials [PROPUBLICA-CIGNA-2023, para 2-3]; a survey of 41 oversight policies finds the evidence that people can supply effective oversight is weak [GREEN-OVERSIGHT-2022, §4.1]. Regulators now name the problem: the EU AI Act asks overseers to stay aware of automation bias [EU-AIACT-ART14-2024, Art 14(4)(b)], and US rules and a California statute require individualized or physician decisions on medical-necessity denials [REEDSMITH-CMSAI-2024; CASENATE-SB1120-2024].
- **Reconciliation automation is often rules first, AI second.** A retailer reports auto-matching 99.6% of more than 1,000,000 transactions with 4,100 left unreconciled, using rule-based matching; it rejected an AI-based vendor as unproven [BLACKLINE-BEAUTYPIE, "Streamlined three-way matches"; customer-reported on a vendor page]. LLMs add most where matching keys are messy: zero-shot GPT-4 beat the best fine-tuned baseline on three of six entity-matching benchmarks and trailed it by 0.73 to 4.49 F1 points on the other three [PEETERS-ENTITYLLM-2024, §4].
- **Exceptions are where the value and the risk sit.** The same retailer found a currency-posting defect in its ERP because unmatched items became visible [BLACKLINE-BEAUTYPIE, "Reduced risk and increased accuracy"]. The opposite design, treating every mismatch as a finding, produced Robodebt; the Royal Commission recommended reviewable, transparent and audited automated decision-making [ROBODEBT-RC-2023, Recs 17.1, 17.2].
- **Governance bites on the object being decided, not the pattern.** Document-to-decision becomes EU high-risk when it evaluates benefit eligibility, creditworthiness or life and health insurance pricing for natural persons [EU-AIACT-ANNEX3-2024, point 5(a)-(c)]. Reconciliation becomes high-stakes when a break is converted into a debt, a denial or a client-money position [FCA-CASS715-2026, 7.15.15R].
- **Agentic ambition outruns evidence.** Gartner predicts over 40% of agentic AI projects will be cancelled by end of 2027, citing cost, unclear value or inadequate risk controls [GARTNER-AGENTIC-2025, para 1]; McKinsey's 2026 survey finds the share of respondents attributing EBIT impact to AI unchanged at 37% and high performers redesigning workflows rather than inserting AI into existing ones [MCKINSEY-STATEAI-2026, key takeaways]. For these patterns that argues for stopping at `automate` with human-cleared exceptions until the quality loop is proven.

---

## 2. Item profiles

### 2.1 `document-to-decision`

**What it does and where it fits.**
- It extracts facts from documents, checks them against written criteria and proposes (or, below a threshold, takes) a decision. Library working definition: [library index §3]. Two stages should be separable: field extraction with evidence, and criteria application [HN-ASKHN-2025, replies by muzani and f_k; ZENML-VENDR, preprocessing and rubric sections] **(advisor inference on the two-stage framing)**.
- Work types: `review-assurance`, `transaction-processing`, sometimes `expert-judgment` where the AI only prepares.
- Cross-industry shapes seen: expense-policy approval (technology/fintech) [RAMP-AGENTS-2025]; contract and loan-agreement review (financial services) [ABAJ-COIN-2017]; SaaS order-form data capture (technology) [ZENML-VENDR]; insurance claim triage and coverage checks [INSURANCENEWS-NEMO-2025]; disability benefit rating (public sector) [VAOIG-ABD-2023]; medical-necessity and coverage determinations (health insurance) [PROPUBLICA-CIGNA-2023; HCDIVE-UNH-2023]; police-report extraction for auto claims (insurance, anonymous practitioner) [HN-ASKHN-2025].
- Cues in a user's description: "we read X and decide whether it qualifies, complies or is approved"; "we check forms against a policy"; "people re-key from PDFs"; "a checklist with yes/no answers"; "most items are routine and a few need judgment". **(advisor inference from the work shapes above)**
- Archetype cases already carry the evidence for assurance, tax, security and professional services (ids in 3.1).

**Ladder range and runtime class by rung** (runtime classes from library index §4; mapping is an **advisor inference** unless a source is cited).

| Rung | What it looks like | Runtime class that fits |
|---|---|---|
| assist | A person uploads a document to an assistant and asks it to pull fields or check a clause; the person decides | `personal-assistant` |
| augment | A shared skill or workflow extracts fields with citations and a first-pass verdict; a reviewer confirms. Ramp describes "guided recommendations" as the start of its range [RAMP-AGENTS-2025, "Flexible autonomy"] | `shared-team-skills`, `workflow-automation` |
| automate | Items above a confidence and risk threshold are approved with no person; the rest escalate. Ramp says its agents escalate "only the 10-15%" (vendor-published) [RAMP-AGENTS-2025]; Allianz Project Nemo has a human make the final payout decision, so it sits at augment [INSURANCENEWS-NEMO-2025] | `workflow-automation`, `background-agent` |
| delegate | An agent owns intake to decision across systems with checkpoints. Evidence is thin outside assurance (see `assurance-controls-testing-05`) | `managed-agent-runtime` |

Typical range: `augment` to `automate`, as the library index says. The VA and Cigna cases show that `automate` without independent quality measurement is the unsafe rung.

**How it is built.**
- *Inputs.* Documents of varying quality, plus the written criteria. Preprocessing matters: deskew, rotate, denoise and crop before the model; use OCR and multimodal readers together because multimodal models "tend to hallucinate more" but see signatures and strikethroughs better [ZENML-VENDR, preprocessing section].
- *The AI's role.* Extract each field with a citation (page, snippet, bounding box, confidence) so reviewers verify rather than re-read [HN-ASKHN-2025, reply by f_k, practitioner product claim]; map entities; apply criteria; write a rationale. Ramp says every approval comes with a rationale and policy citations and that decisions are logged [RAMP-COMM-2025; RAMP-AGENTS-2025, "Full auditability"] (vendor-published).
- *Field rubrics.* Vendr and Extend describe writing rubrics for each field: what "total price" means, whether tax is included, how to treat strikethroughs [ZENML-VENDR, "total price" example and rubric section].
- *Deterministic checks around the model.* Cross-check extracted values against external records and flag mismatches (names, vehicle type) [HN-ASKHN-2025, muzani]; keep calculation in deterministic engines (see `tax-compliance-individual-business-10`, `tax-research-advisory-12`).
- *Human checkpoints.* Per-field routing to review when confidence is low; a person decides above a value or risk threshold; an appeal path for the affected person. Regulatory floors: a licensed physician for medical-necessity denials in California [CASENATE-SB1120-2024]; the right to human intervention for solely automated decisions with significant effects under GDPR [EU-GDPR-ART22-2016, Art 22(3)].
- *Thresholds.* Use per-field thresholds calibrated on your own documents. The 2026 confidence-estimation paper reports that log-probabilities degrade to an all-positive classifier at practical thresholds [KUMAR-EXTRACTCONF-2026, §1]. A practitioner source suggests a very high bar for totals and a lower one for addresses [AIENG-SUBSTACK, search-only, not relied on].
- *Sampling.* Audit the automated stream with a formal plan, not ad hoc spot checks: acceptance sampling defines acceptable quality level, tolerated defect level and the producer's and consumer's risks, and offers single, double, multiple, sequential and skip-lot plans [NIST-SEMATECH-LASP, §6.2.2]. Sample also the escalated items, to learn whether escalation is catching the right ones **(advisor inference)**. The VA case shows the failure of national random samples when the automated claims are a small share [VAOIG-ABD-2023, pp. 17-18].
- *Logging and audit trail.* Retain inputs, extracted values with citations, criteria version, model version, the verdict, the reviewer and any override. EU high-risk systems must technically allow automatic event logging over their lifetime [EU-AIACT-ART12-2024, Art 12(1)]; deployers keep the logs under their control for at least six months unless other law says otherwise [EU-AIACT-ART26-2024, Art 26(6)]. For banks, overrides should be analyzed and documented, and a high override rate is read as a sign the model is not performing as intended [FRB-SR117-2011, §V.2, pp. 12-13].

**Prerequisites.**
- *Data and documents:* a representative set of real documents including bad scans, and a labelled gold set made by people who apply the criteria. The VA error rate traced partly to guidance that "varied from VBA claims processing manual guidance", so written criteria must be settled before automation [VAOIG-ABD-2023, p. iii and fn 10].
- *Access:* read access to the records used for cross-checks; write access only for the decision step.
- *Policy:* a decision rights table (who may approve what, above what value); an appeal route; retention rules for logs and documents; criteria owned by a named person. CMS expects criteria to stay fixed and public, and says tools must not drift into internal criteria [REEDSMITH-CMSAI-2024, "Limit denials" paragraph].
- *Skills:* domain reviewers who can write rubrics (Extend's CEO says domain experts understand business logic best) [ZENML-VENDR]; someone who can run an evaluation set.

**Failure modes and the controls that catch them.**

| Failure mode | Evidence | Control |
|---|---|---|
| Silent extraction error treated as fact | 26% field failure on a hard invoice benchmark [KUMAR-EXTRACTCONF-2026, §1]; HN poster's worry about one wrong number reaching an ERP [HN-ASKHN-2025, opening post] | Per-field confidence from several signals; deterministic cross-checks (line sums to totals; external record match); citations to source |
| Confabulation | Defined in [NIST-GENAI-2024, §2.2, p. 10] | Require supporting text in the source for every extracted value; flag fields with none [HN-ASKHN-2025, f_k] |
| Automation bias and rubber-stamping | [NIST-GENAI-2024, §2.7, p. 13]; [GREEN-OVERSIGHT-2022, §4.1.2]; Cigna's 1.2-second average [PROPUBLICA-CIGNA-2023] | Review speed is not a performance target; challenge samples seeded with known errors **(advisor inference)**; train overseers on limits [EU-AIACT-ART14-2024, Art 14(4)(a)-(b)] |
| Decision rules drift or are unclear | VA guidance varied from the manual and fed the 27% decision error rate [VAOIG-ABD-2023, p. iii] | Version the criteria; one owner; re-test after every criteria change |
| QA that cannot see the automated stream | Internal review reported 100% summary-sheet accuracy while OIG found deficiencies; OIG said VBA's QA programmes did not tailor their sampling to the automated claims [VAOIG-ABD-2023, pp. 17-18] | Independent sample of the automated stream with a pre-set plan [NIST-SEMATECH-LASP, §6.2.2] |
| Denials that few people contest | A KFF analysis, quoted by Healthcare Dive, found members appealed only 0.2% of denials in 2021 (the article does not specify the population) [HCDIVE-UNH-2023, para on appeals] | Do not use appeal rate as the error metric; sample denials proactively **(advisor inference)** |
| Incomplete or wrong notices | OIG found 98% of automated survivor-benefit letters omitted required findings or evidence summaries, as reported by press [WUNC-VADIC-2026] | Test the letter, not just the decision; legal checklist as a test set |
| Over-reach into "significant effect" decisions | Class action alleging a naviHealth algorithm denied care; court allowed breach-of-contract claims to proceed [LOKKEN-ORDER-2025, summary pp. 1-2]; the insurer denies using it for coverage decisions [HCDIVE-UNH-2023] | Individualized review; physician sign-off; see governance below |

**Value levers and metrics.** Levers from library index §5: `capacity`, `speed`, `quality`, `risk`, `cost`, `experience`.
- Capacity and speed: reported hours or days per item. JPMorgan said COIN covered work that had taken about 360,000 hours a year of lawyers and loan officers (self-reported through press, 2017) [ABAJ-COIN-2017]. VBA's in-house numbers were 61.3 days for the traditional process and 25.1 days automated, but OIG found VBA had no reliable study of timeliness and the observed reduction could come from prioritising these claims [VAOIG-ABD-2023, pp. 19-20].
- Quality, which must have a named metric each: field-level accuracy against a gold set; share of automated decisions overturned in sample audit; override rate (reviewer changes the AI's verdict); escalation rate (share routed to people) and the error rate inside the escalated set and inside the automated set; appeal or reversal rate; agreement of AI with a second human reviewer, compared with human-to-human agreement. The last is the method used in a UK government pilot where officials also reviewed every response and noted that "humans don't always agree" [GOV-CONSULT-2025, paras on manual review; adjacent, since the task was theme analysis]. Ramp's announcement does not define its 99% accuracy figure, so it is not comparable with other accuracy figures [RAMP-AGENTS-2025, opening paragraphs].
- Cost: Former Cigna executives told journalists that processing a denial the traditional way can cost a few hundred dollars each, which is the saving the bulk list targeted [PROPUBLICA-CIGNA-2023, "PXDX" section]; treat it as a warning about what a cost metric can reward.

**Governance points.**
- *EU AI Act.* High-risk when used by or for public authorities to evaluate eligibility for essential public benefits and services including healthcare; to evaluate creditworthiness or set a credit score of natural persons (fraud detection excepted); or for risk assessment and pricing for life and health insurance. Employment screening is also listed (point 4) [EU-AIACT-ANNEX3-2024, points 4(a), 5(a)-(c)]. The Act Explorer shows high-risk obligations under Annex III applying from 2 December 2027 [EU-AIACT-ART14-2024, banner citing Art 113(c)]; law-firm commentary reports a provisional political agreement in May 2026 to postpone, with formal adoption expected before 2 August 2026 [GIBSONDUNN-OMNIBUS-2026, intro]. Duties include oversight by competent, trained people with authority [EU-AIACT-ART26-2024, Art 26(2)] and logging [EU-AIACT-ART12-2024].
- *NIST AI RMF.* Define and document human oversight (MAP 3.5); define roles for human-AI configurations (GOVERN 3.2); demonstrate validity and reliability and document limits of generalization (MEASURE 2.5); post-deployment monitoring that includes appeal and override (MANAGE 4.1) [NIST-AIRMF-2023, Core tables]. The Generative AI Profile names confabulation and human-AI configuration (automation bias) as risks [NIST-GENAI-2024, §2.2, §2.7].
- *ISO/IEC 42001.* Annex A groups controls on impact assessment (A.5), lifecycle (A.6) and responsible use including human oversight (A.9), per a practitioner summary; the standard text was not read [ISMS-ISO42001-2025, Annex A control sections].
- *Credit:* creditors must give specific, accurate adverse-action reasons even when using complex algorithms; there is "no special exemption" for AI [CFPB-CIRC2203-2022, Response; CFPB-ADVERSE-2023, Director quote].
- *Health insurance:* Medicare Advantage plans may use algorithms but coverage must rest on individualized determinations and published criteria, per CMS FAQ of 6 February 2024 as summarised by a law firm (primary not opened) [REEDSMITH-CMSAI-2024]. California SB 1120 requires a licensed physician or competent provider to make medical-necessity denial, delay or modification decisions [CASENATE-SB1120-2024]; the senator's release, dated 30 September 2024, says it takes effect 1 January 2024, so confirm the effective date before quoting it.
- *Data protection:* GDPR Art 22 gives a right not to be subject to solely automated decisions with legal or similarly significant effects, with human intervention and contest rights [EU-GDPR-ART22-2016]. Green warns that "solely" can be avoided with nominal review [GREEN-OVERSIGHT-2022, §4.1.1].
- *Banks:* model risk guidance asks for effective challenge, outcomes analysis and override analysis [FRB-SR117-2011, §III, §V.2].

**How it evolves up the ladder.**
- assist to augment: from a person's ad hoc prompt to a shared skill with fixed fields, rubrics and citations (the Vendr and Extend path moves from prompt engineering to domain experts maintaining rubrics) [ZENML-VENDR].
- augment to automate: a threshold, a sampled audit and an exception queue are added. Ramp's range runs from recommendations to autonomous approval, with a watch-and-override stage on day one [RAMP-AGENTS-2025, "Day-zero setup"].
- automate to delegate: the agent also gathers missing documents, chases the requester and updates systems. Evidence for this is mostly in assurance (`assurance-controls-testing-05`, `assurance-controls-testing-19`).
- At every step the checkpoint moves rather than disappears: from "review every item" to "review the sample, the exceptions and the thresholds".

**Anti-patterns (where not to use it).**
- Decisions that significantly affect a person with no individualized review (Cigna bulk denials; the alleged nH Predict use; Robodebt) [PROPUBLICA-CIGNA-2023; LOKKEN-ORDER-2025; ROBODEBT-RC-2023].
- Criteria that are unwritten, inconsistent or secret [VAOIG-ABD-2023, p. iii; REEDSMITH-CMSAI-2024].
- Review staffed and scored on speed, which produces rubber-stamping [PROPUBLICA-CIGNA-2023, scorecard paragraph].
- Low-volume, high-variance documents where a person is faster and the rubric cost never pays back; Extend's CEO first asks whether generic OCR or a point solution is enough [ZENML-VENDR, opening discussion].
- Using the model's own token probabilities as the only gate [KUMAR-EXTRACTCONF-2026, §1].
- Letting the team that built the automation be the only measurer of its quality [VAOIG-ABD-2023, pp. 17-18].

### 2.2 `reconcile-exceptions`

**What it does and where it fits.**
- It matches records across sources, clears what matches, classifies and works the breaks, and sends unresolved breaks to a person. Library working definition: [library index §3].
- Work types: `transaction-processing`, `data-reporting`.
- Shapes seen: bank-to-ledger and e-commerce-to-bank three-way matching (retail) [BLACKLINE-BEAUTYPIE]; large-volume bank reconciliation (manufacturing/imaging) [HIGHRADIUS-KONICA-2025]; telecom reconciliation and monitoring [CASESTUDIES-GLOBE]; vehicle retail [TRINTECH-AUTONATION-2026]; small-business bank feeds (software) [DIGIT-XERO-2026]; trade breaks in capital markets (financial services) [NASDAQ-BROADRIDGE-2019; FIA-BROADRIDGE-2019]; client-money reconciliation under UK rules [FCA-CASS715-2026]; benefit-payment to tax-return matching (public sector, cautionary) [ROBODEBT-RC-2023]; entity matching across product and company records (research) [PEETERS-ENTITYLLM-2024; NARAYAN-FMDATA-2022].
- Cues: "we compare two lists and chase the differences"; "the close is late because of unreconciled items"; "we sample because we cannot check everything"; "a few analysts know why things break". **(advisor inference)**

**Ladder range and runtime class by rung** (mapping is an **advisor inference** unless cited).

| Rung | What it looks like | Runtime class |
|---|---|---|
| assist | An analyst asks an assistant to explain a break or draft a matching rule | `personal-assistant` |
| augment | The system proposes matches and break reasons; an analyst confirms. Xero's feature leaves lower-confidence items as suggestions [DIGIT-XERO-2026, "layered approach" and "controls"] | `shared-team-skills`, `workflow-automation` |
| automate | Matches above a confidence or rule threshold post automatically; exceptions queue for people. Most named cases sit here [BLACKLINE-BEAUTYPIE; HIGHRADIUS-KONICA-2025; CASESTUDIES-GLOBE] | `workflow-automation`, `background-agent` |
| delegate | An agent investigates a break across systems, drafts the correcting entry and routes it for approval. Broadridge announced ML break classification in 2019 but no outcome data are public [NASDAQ-BROADRIDGE-2019] | `managed-agent-runtime` |

Typical range: `automate`, as the library index says. Delegate evidence is announcement-level only (Section 5).

**How it is built.**
- *Inputs.* Two or more record sets with keys of different quality; matching rules and tolerances; reason codes for breaks; ageing rules. Beauty Pie matched bank, e-commerce platform and ERP and said import definitions and matching rules were the main learning [BLACKLINE-BEAUTYPIE, "Streamlined three-way matches"].
- *The AI's role.* Three separable jobs: (1) propose matches where keys are messy (entity or narrative matching), (2) classify and explain breaks, (3) propose resolutions. LLM matching with GPT-4 achieved F1 of 89% or higher on 5 of 6 benchmarks zero-shot, comparable to fine-tuned models trained on thousands of pairs, but "there is no single best prompt" and prompt sensitivity is large [PEETERS-ENTITYLLM-2024, abstract and §4 discussion]. Earlier work found large foundation models reach state-of-the-art on entity matching with prompting alone [NARAYAN-FMDATA-2022, abstract].
- *Deterministic first.* Exact and rule-based matching clears the bulk. Beauty Pie says it considered an "AI-based" vendor and judged it unproven; it chose rule-based matching [BLACKLINE-BEAUTYPIE, vendor selection paragraph]. **(advisor inference: add the model where rules leave a long tail.)**
- *Human checkpoints.* A named person clears unresolved breaks; ownership and ageing of the exception queue is visible; auto-clear rules and tolerances are approved by the account owner **(advisor inference)**. Xero's design makes auto-reconciliation opt-in per bank account, shows the rule or document behind each match on a "Reconciled" page, and allows undo [DIGIT-XERO-2026, "controls" paragraph] (practitioner description of a vendor beta).
- *Thresholds and sampling.* Confidence-gated: Xero describes automatic reconciliation only at high confidence [DIGIT-XERO-2026]. Audit the auto-matched population by sampling for false matches, using a defined plan [NIST-SEMATECH-LASP, §6.2.2]; track the unmatched population by age rather than by count alone **(advisor inference)**.
- *Logging and audit trail.* UK client-money rules require a record of the date, the actions taken and the outcome of each reconciliation [FCA-CASS715-2026, 7.15.7R], and policies on frequency, method and resolution of discrepancies [FCA-CASS715-2026, 7.15.8G]. Reconstructable reasons for each AI-touched match are the equivalent for audit **(advisor inference)**.

**Prerequisites.**
- Read access to both sources and a trusted reference; stable keys or a plan for fuzzy keys. CASS requires the internal reconciliation to use the firm's own ledger values rather than bank statement values [FCA-CASS715-2026, 7.15.13R], a reminder to be explicit about which source is the book of record.
- Policy: tolerance limits, write-off authority, and who may post corrections (not the matcher).
- Skills: someone who can read a break and trace it upstream. Beauty Pie traced an ERP that converted dollar amounts to pounds but posted in dollars, wrong by 20% on those items [BLACKLINE-BEAUTYPIE, "Reduced risk and increased accuracy"].

**Failure modes and the controls that catch them.**

| Failure mode | Evidence | Control |
|---|---|---|
| Forced matches hide real breaks | The pattern's main risk in library index §3. Robodebt shows the opposite error: treating discrepancies as conclusions [ROBODEBT-RC-2023, Recs 17.1-17.2] | One-to-one match constraints; tolerance policy owned by finance; sample the auto-matched set for false matches **(advisor inference)** |
| Mismatch treated as a finding about a person | Robodebt: the Commission recommended review paths, public explanation of automated decisions, availability of business rules for expert scrutiny, and a monitoring body [ROBODEBT-RC-2023, Recs 17.1, 17.2] | Break is a prompt to investigate; a person verifies before any adverse action |
| Matching to the wrong source of truth | CASS 7.15.13R [FCA-CASS715-2026] | State the book of record in the design |
| Demo rates do not survive real data | Practitioner testing of Xero's feature found it handles straightforward feeds well but needs oversight for splits, foreign currency and journals [DIGIT-XERO-2026, "testing" paragraph]; a vendor claims production touchless rates of 65-75% versus demo 90-99% [KOGNITOS-AP-2026, opening] (vendor assertion, unsourced) | Pilot on a month of real history including bad months; report by break type |
| Plateau because the answer is outside the records | The same vendor says 30-40% of invoices need context outside the three matching documents and gives an exception mix without a source [KOGNITOS-AP-2026] | Give the agent contract, vendor-master and approval context; measure resolved root causes |
| Unexplained match decisions | Tookitaki describes a "glass-box" approach with audit trails for its ML matching [NASDAQ-BROADRIDGE-2019] (vendor claim) | Store the evidence for each auto-match; test that a reviewer can reconstruct it |

**Value levers and metrics.** Levers: `capacity`, `speed`, `quality`, `risk`, `cost`.
- Auto-match rate: numerator is transactions matched without a person, denominator is total transactions in the period. Reported cases: 99.6% with 4,100 unreconciled of over 1,000,000 since go-live (customer-reported on vendor page) [BLACKLINE-BEAUTYPIE]; about 99% with 45,000+ line items monthly and close cut from 30 to 7 days (vendor-published) [HIGHRADIUS-KONICA-2025]; 90% auto-match, reporting from 30 days to 8-12 days (vendor case via aggregator) [CASESTUDIES-GLOBE]; "near 100%" and 200,000 transactions monthly (vendor webinar abstract) [TRINTECH-AUTONATION-2026]. None reports the false-match rate.
- Quality metrics to demand: false-match rate from sampled audit; unreconciled items by age; reopen rate; share of breaks with root cause fixed upstream (Broadridge frames the aim as finding the underlying cause, not just clearing breaks) [NASDAQ-BROADRIDGE-2019, McGill quote]; analyst override rate on proposed matches.
- Capacity and speed: days of manual work per period (Beauty Pie: "many days" to "a few hours", customer-reported) [BLACKLINE-BEAUTYPIE]; days to close.
- Risk: defects surfaced (Beauty Pie's FX posting defect).
- Benchmarks: an average invoice exception rate of 14% and best-in-class 9% is attributed to Ardent Partners in secondary sources only [ARDENT-VIA-AGGREGATORS-2025, search-only; not relied on].

**Governance points.**
- *Financial services:* client-money reconciliation daily, from the previous business day's records [FCA-CASS715-2026, 7.15.15R]; model risk expectations if models drive matching or auto-clear [FRB-SR117-2011].
- *EU AI Act:* reconciliation of ledgers is not on the Annex III list; the exposure arises where the output is used to evaluate eligibility for public benefits or creditworthiness [EU-AIACT-ANNEX3-2024, point 5(a)-(b)] **(advisor inference on applicability)**.
- *Public sector:* the Royal Commission's recommendations on automated decision-making [ROBODEBT-RC-2023, Recs 17.1-17.2]; GDPR Art 22 where a reconciliation result triggers an automated decision about a person [EU-GDPR-ART22-2016].
- *NIST AI RMF:* MEASURE 2.5 and MANAGE 4.1 apply to any AI matcher: validity, limits of generalization, monitoring, override [NIST-AIRMF-2023, Core tables].
- *ISO/IEC 42001:* lifecycle and use controls (A.6, A.9) per a practitioner summary [ISMS-ISO42001-2025].

**How it evolves up the ladder.**
- assist to augment: analysts move from tracing breaks by hand to confirming proposed matches and reasons.
- augment to automate: rules and thresholds clear the bulk; the exception queue becomes the work. Beauty Pie moved the team's effort to what does not match and to "match against ourselves" cases such as cancelled transactions that net to zero [BLACKLINE-BEAUTYPIE, "Improved efficiency and gained ROI"].
- automate to delegate: the agent investigates and drafts fixes. No named, measured case was found; treat as announced or emerging.
- Typical end state: continuous matching in place of period-end matching **(advisor inference)**, which is a `process` change rather than `step`.

**Anti-patterns.**
- Using AI where deterministic rules already clear about 99% and the long tail is small [BLACKLINE-BEAUTYPIE].
- Auto-writing off differences without a policy owner **(advisor inference; a practitioner guide says the same but was search-only)**.
- Turning mismatches directly into demands on people [ROBODEBT-RC-2023].
- Reconciling against the counterparty's record where rules require your own books [FCA-CASS715-2026, 7.15.13R].
- Measuring success by auto-match rate alone, since none of the published cases shows the false-match rate (Section 6).

---

## 3. Examples

Ladder and change scope use the vocabulary values. "Provenance" is who measured the figure.

### 3.1 `document-to-decision`

| # | Organization (industry) | What changed in the work | Ladder / scope | Outcome and provenance | Grade | Source |
|---|---|---|---|---|---|---|
| D1 | Veterans Benefits Administration, Automated Benefits Delivery (public sector, US) | Automation extracts blood-pressure evidence into a summary sheet for hypertension rating claims; claims processors decide | augment / process | Independent OIG sample of 60 claims: 16 (27%) had inaccurate and inconsistent determinations; summary sheets deficient in 11 of 30 (37%) and 17 of 30 (57%) of two samples. ABD's internal reviews of 167 of 183 claims reported 100% summary-sheet accuracy (OIG: similar deficiencies were later found on all summary sheets a VBA contractor reviewed). VBA's own figures: 61.3 days traditional vs 25.1 days automated (self-reported; OIG says no reliable timeliness study). `independent` and `self-reported` | B (adjacent: rule-based automation; A-quality measurement) | [VAOIG-ABD-2023, pp. iii, 6, 17-20] |
| D2 | Veterans Benefits Administration, automated survivor-benefit decisions (public sector, US) | Rules-based system issues Dependency and Indemnity Compensation decisions and notices | automate / process | Press report of an OIG review: of about 8,100 automated decisions, errors in about 8,000; 98% of letters omitted required findings or evidence summaries; at least $2.7 million overpaid. The OIG report itself was not opened. `independent`, secondhand | B (adjacent) | [WUNC-VADIC-2026, paras 2-6] |
| D3 | Cigna (health insurance, US) | Doctors bulk-deny claims matched to a procedure-to-diagnosis list, without opening the file | automate / process | Over two months, doctors denied over 300,000 requests at an average of 1.2 seconds per case, from internal documents reviewed by journalists; Cigna says the description is "incorrect". `independent` (journalism), disputed | B (adjacent; failure case) | [PROPUBLICA-CIGNA-2023, paras 2-5] |
| D4 | UnitedHealth Group / naviHealth (health insurance, US) | Alleged use of an AI model to set post-acute care coverage | augment or automate (alleged) / process | Plaintiffs allege over 90% of denials are reversed on appeal; UnitedHealth denies using it for coverage determinations; the court let breach-of-contract claims proceed. `independent` court record of an allegation, not a finding | C (allegation) | [HCDIVE-UNH-2023; LOKKEN-ORDER-2025, pp. 1-2] |
| D5 | Allianz Australia, Project Nemo (insurance) | Seven task-specific agents do coverage checks and fraud detection on food-spoilage claims; a human makes the final payout decision | augment / process | Allianz says processing time fell 80%; for claims under $500, several days to hours. Described as a trial/pilot. Measurement basis not stated. `self-reported` | B | [INSURANCENEWS-NEMO-2025, paras 1-2, 6-7] |
| D6 | Ramp (technology / fintech) | Agent reads a policy PDF, approves low-risk expenses with rationale and citations, escalates the rest | automate / process | Vendor says early customers saw 99% accuracy, 15x more out-of-policy spend detected, 85% fewer manual reviews; agents escalate "only the 10-15%". Accuracy is not defined in the announcement. `vendor-published` | C | [RAMP-AGENTS-2025; RAMP-COMM-2025] |
| D7 | Vendr with Extend (technology, SaaS procurement data) | LLM extraction of structured fields from SaaS order forms and contracts, with embeddings for similarity clustering, targeted human review and entity mapping | augment / step | Processed over 100,000 documents; no accuracy figures in the summary. Conference talk summarised by a third party. `self-reported` | B | [ZENML-VENDR, summary paragraph] |
| D8 | JPMorgan Chase, COIN (financial services) | Software reviews commercial loan agreements | automate / step | Bank said it covered about 360,000 hours of annual work and reduced servicing errors tied to interpreting 12,000 new contracts a year; no error figures. Reported by Bloomberg, relayed 2017. `self-reported` through press; rough estimate | B | [ABAJ-COIN-2017, paras 1-3] |

Industries covered: public sector, health insurance, insurance, technology, financial services. Not covered: retail, manufacturing, professional services outside the archetype (see Gaps).

**Archetype use cases already tagged `pattern: document-to-decision`** (id and grade only; 55 in total: 3 A, 25 B, 23 C, 4 D).
- A: `assurance-controls-testing-05`, `assurance-controls-testing-06`, `assurance-controls-testing-11`.
- B: `assurance-completion-reporting-10`, `assurance-controls-testing-19`, `assurance-controls-testing-20`, `assurance-substantive-testing-11`, `assurance-substantive-testing-12`, `assurance-substantive-testing-13`, `assurance-substantive-testing-15`, `professional-services-acceptance-risk-10`, `professional-services-knowledge-management-11`, `professional-services-pursuit-proposals-06`, `professional-services-pursuit-proposals-07`, `professional-services-work-production-12`, `professional-services-work-production-18`, `security-data-privacy-13`, `security-governance-risk-03`, `security-governance-risk-09`, `security-identity-access-03`, `security-identity-access-06`, `security-identity-access-19`, `tax-compliance-corporate-02`, `tax-compliance-individual-business-02`, `tax-compliance-individual-business-04`, `tax-controversy-21`, `tax-research-advisory-13`, `tax-research-advisory-21`.
- C: `assurance-acceptance-independence-05`, `assurance-completion-reporting-01`, `assurance-completion-reporting-02`, `assurance-completion-reporting-04`, `assurance-completion-reporting-05`, `assurance-controls-testing-13`, `assurance-planning-risk-assessment-17`, `assurance-substantive-testing-14`, `assurance-sustainability-assurance-01`, `assurance-sustainability-assurance-02`, `professional-services-pursuit-proposals-20`, `professional-services-staffing-resourcing-03`, `security-cloud-infrastructure-21`, `security-incident-response-01`, `security-incident-response-10`, `security-threat-intelligence-09`, `tax-compliance-corporate-09`, `tax-compliance-individual-business-17`, `tax-controversy-04`, `tax-data-technology-11`, `tax-indirect-tax-03`, `tax-indirect-tax-10`, `tax-transfer-pricing-08`.
- D: `assurance-completion-reporting-15`, `assurance-sustainability-assurance-06`, `professional-services-pursuit-proposals-19`, `tax-provision-pillar-two-02`.

### 3.2 `reconcile-exceptions`

| # | Organization (industry) | What changed in the work | Ladder / scope | Outcome and provenance | Grade | Source |
|---|---|---|---|---|---|---|
| R1 | Beauty Pie (retail, e-commerce, UK) | Three-way matching of bank, e-commerce platform and ERP moved from spreadsheets (over 100,000 transactions a month) to rule-based matching software | automate / process | Controller says 99.6% auto-matched; of over 1,000,000 transactions since go-live only 4,100 unreconciled; days of monthly work now a few hours; found an ERP posting defect (20% error on affected items). `self-reported` (customer, on vendor page) | B (adjacent: rule-based, not AI) | [BLACKLINE-BEAUTYPIE] |
| R2 | Konica Minolta (manufacturing / imaging) | AI/ML transaction matching for bank reconciliation | automate / process | Vendor page: 75% faster bank reconciliation, about 99% automated matching, 45,000+ line items monthly, close from 30 to 7 days. `vendor-published` | C | [HIGHRADIUS-KONICA-2025, headline block] |
| R3 | Globe Telecom (telecommunications, Philippines) | Replaced an end-of-life reconciliation and monitoring system with a configurable matching service | automate / process | Vendor case via aggregator: time to audit findings down 60%, reporting from 30 days to 8-12 days, auto-matching 90%. `vendor-published` | C | [CASESTUDIES-GLOBE, results paragraph] |
| R4 | AutoNation (vehicle retail) | AI-assisted reconciliations at volume | automate / process | Vendor webinar abstract: "near 100%" auto-match and 200,000 transactions monthly. No baseline. `vendor-published` | C | [TRINTECH-AUTONATION-2026, abstract] |
| R5 | Broadridge with Tookitaki (financial services, trade reconciliation) | ML break classification and automatic matching-scheme configuration | augment to automate / process | Announced December 2019; no customer outcomes in the sources. `vendor-published` | C (announced) | [NASDAQ-BROADRIDGE-2019; FIA-BROADRIDGE-2019] |
| R6 | Xero (accounting software, SMB) | Confidence-gated auto-reconciliation of bank feeds, opt-in per account, with a "Reconciled" explanation page and undo | automate / step | Investor demo: 113 of 118 transactions handled automatically, 3 left for review; Xero claims accuracy above 97%; early users cited saving four to seven hours a week. Demo conditions; a practitioner firm is testing on real files. `vendor-published`, relayed by a Xero-partner firm | C | [DIGIT-XERO-2026, JAX section] |
| R7 | Services Australia, Robodebt (public sector, Australia) | Automated matching of benefit records to tax-return income, with discrepancies treated as debts | automate / process | Royal Commission (report 7 July 2023) made 57 recommendations, including Recs 17.1-17.2 on reviewable, transparent, audited automated decisions. Scale figures (hundreds of thousands of debts) appear only in search-only press and are not cited. `independent` | B (adjacent; failure case) | [ROBODEBT-RC-2023, recommendations list] |

Industries covered: retail, manufacturing, telecommunications, vehicle retail, financial services, software, public sector. Healthcare reconciliation (remittance posting, denials) had no named, measured case that could be opened.

**Archetype use cases already tagged `pattern: reconcile-exceptions`** (id and grade only; 34 in total: 2 A, 12 B, 13 C, 7 D).
- A: `assurance-completion-reporting-06`, `security-operations-21`.
- B: `assurance-acceptance-independence-17`, `assurance-controls-testing-07`, `assurance-specialists-14`, `assurance-substantive-testing-10`, `assurance-substantive-testing-18`, `professional-services-billing-collections-05`, `professional-services-billing-collections-13`, `professional-services-quality-review-15`, `security-identity-access-20`, `tax-compliance-corporate-10`, `tax-data-technology-09`, `tax-transfer-pricing-12`.
- C: `assurance-completion-reporting-03`, `assurance-controls-testing-14`, `assurance-planning-risk-assessment-19`, `assurance-soc-attestation-12`, `assurance-substantive-testing-03`, `assurance-substantive-testing-04`, `professional-services-pursuit-proposals-05`, `professional-services-quality-review-02`, `security-ai-security-21`, `tax-controversy-05`, `tax-data-technology-02`, `tax-provision-pillar-two-03`, `tax-transfer-pricing-14`.
- D: `assurance-assurance-over-ai-06`, `assurance-completion-reporting-16`, `assurance-specialists-04`, `assurance-sustainability-assurance-13`, `professional-services-billing-collections-14`, `security-cloud-infrastructure-12`, `security-vulnerability-exposure-16`.

---

## 4. Expert moves and probes

### 4.1 `document-to-decision`

1. **"Take the last 20 items this team decided. For each, where did the facts come from and what rule applied?"** Reveals whether the criteria are written and consistent; the VA decision errors traced to guidance that differed from the manual [VAOIG-ABD-2023, p. iii].
2. **"Who checks the checker? Who would measure the automated items, and how do they sample?"** Reveals whether QA can see the automated stream. VBA's national samples rarely included the automated claims [VAOIG-ABD-2023, pp. 17-18]. Suggest a pre-set acceptance sampling plan [NIST-SEMATECH-LASP, §6.2.2].
3. **"How long does a reviewer spend per item now, and is anyone scored on speed?"** Reveals rubber-stamp risk. Cigna's scorecard tracked speed on bulk denials [PROPUBLICA-CIGNA-2023, scorecard paragraph]; the oversight literature doubts that people catch algorithm errors reliably [GREEN-OVERSIGHT-2022, §4.1.2].
4. **"Which fields, if wrong, cost money or hurt a person? What is your tolerance per field?"** Sets per-field thresholds and which fields need a deterministic cross-check. Confidence from log-probabilities alone does not separate good from bad extractions [KUMAR-EXTRACTCONF-2026, §1].
5. **"What share could you automate at 99% accuracy and what share goes to people?"** Forces the coverage-versus-accuracy trade-off. In the benchmark, 80% coverage reached 99.1% accuracy only with a multi-signal confidence engine [KUMAR-EXTRACTCONF-2026, §6.2].
6. **"Does the decision significantly affect a person (credit, coverage, benefits, employment)? In which jurisdiction?"** Triggers the governance branch: AI Act Annex III points 4 and 5, GDPR Art 22, CFPB adverse-action rules, CMS and California rules [EU-AIACT-ANNEX3-2024; EU-GDPR-ART22-2016; CFPB-CIRC2203-2022; REEDSMITH-CMSAI-2024; CASENATE-SB1120-2024].
7. **"If a person disagrees with the decision, what happens and how many people actually use it?"** Reveals whether appeals can serve as a quality signal; a KFF analysis quoted by Healthcare Dive found only 0.2% of denials appealed in 2021 [HCDIVE-UNH-2023].
8. **"Show me the log for one decision a year from now: inputs, values, criteria version, model version, reviewer, override."** Reveals audit-trail readiness [EU-AIACT-ART12-2024; FRB-SR117-2011, §V.2]; see `tax-data-technology-19` and `tax-indirect-tax-15` for decision-log practice.
9. **"Would a generic OCR or point tool already do 90% of this?"** Guards against over-building. Extend's CEO opens with this question [ZENML-VENDR].
10. **"Who owns the document types and criteria when they change?"** Reveals drift risk. CMS says tools must not alter coverage criteria over time [REEDSMITH-CMSAI-2024].

### 4.2 `reconcile-exceptions`

1. **"What is your match rate today and what do you do with what does not match?"** Reveals whether the exception queue is owned and aged. Beauty Pie could not tell why items failed to match before automating [BLACKLINE-BEAUTYPIE, "Reduced risk and increased accuracy"].
2. **"Do rules already clear most of it?"** If rules reach about 99%, the AI case is the long tail only [BLACKLINE-BEAUTYPIE; PEETERS-ENTITYLLM-2024 for where models help on messy keys].
3. **"What happens when a break is found: who investigates, and does anything get fixed upstream?"** Reveals whether value is cleared items or removed root causes [NASDAQ-BROADRIDGE-2019, McGill quote].
4. **"Which record is the book of record, and who can post a correction?"** Prevents matching to the wrong side and separates matcher from poster [FCA-CASS715-2026, 7.15.13R].
5. **"What is the cost of a false match versus a missed match?"** Sets thresholds. LLM matchers trade precision and recall; reports give F1, precision and recall separately [PEETERS-ENTITYLLM-2024, §3-4, metrics].
6. **"How will you measure false matches in the auto-cleared set?"** None of the published cases reports it. Propose a sampled audit [NIST-SEMATECH-LASP, §6.2.2].
7. **"Does a mismatch ever lead to an action against a person or customer?"** If yes, add a human verification step before any adverse action [ROBODEBT-RC-2023, Recs 17.1-17.2].
8. **"Run it on your worst month, not your cleanest."** Demo-to-production gaps are reported by practitioners and vendors [DIGIT-XERO-2026; KOGNITOS-AP-2026].
9. **"What is the period-end deadline and the regulatory frequency?"** Daily for UK client money [FCA-CASS715-2026, 7.15.15R]; shows whether continuous matching is a `process` change worth making.
10. **"Where do the facts needed to resolve a break live?"** If outside the matched records (contracts, vendor master), the agent needs those inputs or exceptions will plateau [KOGNITOS-AP-2026] (vendor view).

---

## 5. Evidence on what works and what fails

Provenance in brackets. Absence is stated plainly at the end of the section.

**Independent measurement**
- VA OIG, September 2023. Statistical sample of 60 hypertension claims from 183 automated claims: 27% (16 of 60) inaccurate decisions; deficient summary sheets in 37% and 57% of two samples of 30; internal QA reported 100% accuracy; VBA's timeliness claim (61.3 vs 25.1 days) lacked a study and the observed reduction could reflect prioritisation. Four recommendations including better QA and metrics. `independent`; adjacent (rule-based automation, early project stage) [VAOIG-ABD-2023, pp. ii-iii, 6, 17-20].
- VA OIG on survivor-benefit automation, reported June 2026: about 8,000 of 8,100 automated decisions with errors, 98% of letters deficient, at least $2.7 million overpaid. `independent`, via press; the OIG text was not opened [WUNC-VADIC-2026]. A lawyer quoted says some systems are AI and some rule-based, so treat as adjacent.
- Cigna bulk denials: over 300,000 denials in two months at 1.2 seconds per case; estimate in a corporate document that only 5% of people would appeal. `independent` (journalism), disputed by the company [PROPUBLICA-CIGNA-2023, paras 2-5 and appeal paragraph].
- Royal Commission into the Robodebt Scheme, 7 July 2023: 57 recommendations; Chapter 17 recommends legislative reform for automated decision-making, with review paths, plain-language disclosure, business rules open to expert scrutiny, and a body to monitor and audit [ROBODEBT-RC-2023, Chapter 17].
- Court order, 13 February 2025: allowed breach-of-contract and good-faith claims to proceed in a case alleging an AI model replaced physicians in coverage decisions. A procedural ruling; no finding on accuracy [LOKKEN-ORDER-2025, pp. 1-2].

**Academic and benchmark**
- Extraction confidence: on DocILE (55-field invoices) frontier LLMs failed on 26% of fields; log-prob mean 0.705 ROC AUC; the multi-signal engine reached 0.928 ROC AUC and 99.1% accuracy at 80% coverage vs 73.3% base rate; zero-shot transfer to receipts 0.858 AUC. Workshop paper accepted at IJCAI-ECAI 2026; author affiliated with a vendor [KUMAR-EXTRACTCONF-2026, abstract, §4.1, §6.2].
- Entity matching with LLMs: zero-shot GPT-4 reached 89% F1 or higher on 5 of 6 datasets, beat the best fine-tuned baseline on 3 of 6 by 2.65-4.71% F1 and trailed on the other three by 0.73-4.49%; prompt and model sensitivity high. `independent` academic benchmark; not a business deployment [PEETERS-ENTITYLLM-2024, §4].
- Foundation models on data cleaning and integration reach state of the art with prompting [NARAYAN-FMDATA-2022, abstract].
- Human oversight: survey of 41 policies finds that evidence suggests people cannot perform the desired oversight functions and that policies may legitimise faulty algorithms [GREEN-OVERSIGHT-2022, abstract, §4.1-4.2]. Note that the paper cites a counter-example in which staff overrode many errors (Allegheny Family Screening Tool) [GREEN-OVERSIGHT-2022, §4.1.2].

**Parallel runs and agreement**
- Scottish Government used the UK 'Consult' tool on over 2,000 consultation responses; officials reviewed every response manually as well, and the government reports they agreed most of the time with negligible effect on theme ranking (`self-reported`). The 75,000 days and £20 million figures are projections [GOV-CONSULT-2025, paras 4-6]. Adjacent task (qualitative coding), but it is the one public example of a full parallel run with a human-agreement baseline.

**Vendor-published figures, no independent check**
- Ramp: 99%, 15x, 85%, 10-15% [RAMP-AGENTS-2025; RAMP-COMM-2025]. Reconciliation vendors: 99.6% (customer-reported), about 99%, 90%, "near 100%" [BLACKLINE-BEAUTYPIE; HIGHRADIUS-KONICA-2025; CASESTUDIES-GLOBE; TRINTECH-AUTONATION-2026]. Xero demo 113 of 118 [DIGIT-XERO-2026]. A vendor says agentic AP pilots stall near 70% touchless against 90-99% in demos [KOGNITOS-AP-2026].

**Research-firm and survey context**
- Gartner, 25 June 2025: over 40% of agentic AI projects will be cancelled by end of 2027; "agent washing"; only about 130 of thousands of vendors judged real; forecast that at least 15% of day-to-day work decisions will be made autonomously through agentic AI by 2028 [GARTNER-AGENTIC-2025, paras 1-2, 5-6]. Analyst prediction, not a measurement.
- McKinsey, 25 August 2026 (survey in field 4 May to 8 June 2026, 1,719 respondents): 37% attribute some EBIT impact to AI, unchanged; about 6% are high performers; high performers redesign workflows rather than insert AI into existing ones [MCKINSEY-STATEAI-2026, key takeaways and methodology]. `self-reported` survey.

**Practitioner discourse**
- An Ask HN thread (18 December 2025) asks whether anyone runs LLM document processing reliably, worries that one wrong number in an ERP causes harm, and argues human review defeats the purpose; replies describe cross-checks against external records, per-field citations and layered rules-plus-model setups for precision-critical documents [HN-ASKHN-2025]. `community`; anecdotal.

**What is absent.** No controlled trial, parallel-run study or incident report on an LLM document-to-decision or reconcile-exceptions deployment with override, escalation and error rates reported together was found. No named organization published a false-match rate for AI reconciliation. The strongest quality evidence is an audit of rule-based automation. The grade A entries in the archetype library, for these two patterns, come from assurance and security reporting.

---

## 6. Gaps

- No named organization publishes override rate, escalation rate and error rate together for an AI document-to-decision system; the sole escalation figure is a vendor's.
- No false-match rate for any reconciliation case; all auto-match rates are unaudited and mostly vendor-published.
- No grade A example outside the archetype library. Beauty Pie would be A on figures alone but is rule-based, so it is capped at B.
- Healthcare reconciliation and revenue-cycle exceptions: search found only vendor and blog material. A claim of a 99-bed hospital halving "discharged not final billed" cases traced only to vendor blogs (search-only; not used).
- Aviva claims transformation (McKinsey case study) and the Ardent Partners exception and touchless benchmarks were reachable only as search snippets; the McKinsey page blocked both `curl` and the text mirror. Not used in examples.
- Retail and manufacturing document-to-decision: no named, opened case.
- Primary sources not opened: the CMS February 2024 FAQ (404 on guessed URLs; a law-firm summary used), the NAIC model bulletin (403), the full Robodebt report PDFs (connection errors; only the recommendations page was read), the OIG survivor-benefit report (only press), the ISO/IEC 42001 standard (paywalled; ISO page returned 403; a practitioner summary of Annex A used), the Bloomberg 2017 COIN story (via ABA Journal).
- Adoption status of the EU Digital Omnibus delay: sources show a provisional agreement in May 2026 and an expected adoption before 2 August 2026; I did not confirm formal adoption. The Act Explorer displays 2 December 2027 for Annex III obligations.
- California SB 1120 effective date: the senator's release is dated 30 September 2024 yet says the law takes effect 1 January 2024; confirm before use.
- Undated pages (retrieval date used in section 7): Beauty Pie, Globe Telecom, Vendr and Extend summary, NIST handbook page.
- Ramp's accuracy definition is not in the announcement or the community post; a definition appeared only in a search summary of a support page and is not used.
- Delegate-level evidence for both patterns is announcement or anecdote only.

### Archetype use cases tagged `pattern: other` that should carry one of these ids

Of the 227 entries tagged `other`, I screened titles and, for the closest, problem and solution text. Proposed retags, with reason:

| Id | Proposed pattern | Reason |
|---|---|---|
| `security-human-risk-12` | `document-to-decision` | Verifies identity documents and liveness of remote hires, the same mechanism as `security-identity-access-19`, which is already tagged. |
| `tax-indirect-tax-22` (D) | `document-to-decision` | Splits VAT determination into steps and checks each against a deterministic rule engine: the decision stage of the pattern, as a control design. |
| `assurance-soc-attestation-04` | `document-to-decision` | Maps customer commitments and evidence to controls across frameworks: documents checked against criteria. Low confidence; could stay `other` as a crosswalk. |
| `tax-research-advisory-12` | `document-to-decision` | Model translates rules and facts, deterministic engine computes the outcome. Low confidence. |
| `tax-compliance-individual-business-10` (D) | `document-to-decision` | Same split of model intake from deterministic calculation. Low confidence, idea only. |

Considered and left as `other`: `tax-data-technology-19`, `tax-indirect-tax-15` and `assurance-assurance-over-ai-04` (decision-log and audit-trail practice that supports document-to-decision rather than being one); `security-ai-security-08` (grade A, gating agent actions with a classifier and human approval for high-impact steps; a checkpoint design useful to both patterns); `security-governance-risk-16` (verifying vendor attestations).

---

## 7. Sources

All were opened and read unless marked search-only. Retrieval date for undated pages: 2026-10-20 (flagged).

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| NIST-AIRMF-2023 | Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1 | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 2023-01 | full |
| NIST-GENAI-2024 | AI RMF Generative AI Profile, NIST AI 600-1 | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | 2024-07 | full |
| EU-AIACT-ANNEX3-2024 | Annex III: High-risk AI systems referred to in Article 6(2) (text of Regulation (EU) 2024/1689; unofficial reproduction) | European Union (text reproduced by artificialintelligenceact.eu) | regulator | https://artificialintelligenceact.eu/annex/3/ | 2024-06-13 | full |
| EU-AIACT-ART12-2024 | Article 12: Record-keeping (Regulation (EU) 2024/1689; unofficial reproduction) | European Union (artificialintelligenceact.eu) | regulator | https://artificialintelligenceact.eu/article/12/ | 2024-06-13 | full |
| EU-AIACT-ART14-2024 | Article 14: Human oversight (Regulation (EU) 2024/1689; unofficial reproduction) | European Union (artificialintelligenceact.eu) | regulator | https://artificialintelligenceact.eu/article/14/ | 2024-06-13 | full |
| EU-AIACT-ART26-2024 | Article 26: Obligations of deployers of high-risk AI systems (Regulation (EU) 2024/1689; unofficial reproduction) | European Union (artificialintelligenceact.eu) | regulator | https://artificialintelligenceact.eu/article/26/ | 2024-06-13 | full |
| GIBSONDUNN-OMNIBUS-2026 | EU AI Act Omnibus Agreement: Postponed High-Risk Deadlines and Other Key Changes | Gibson Dunn | firm | https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines/ | 2026-05-27 | full |
| EU-GDPR-ART22-2016 | Art. 22 GDPR: Automated individual decision-making, including profiling (Regulation (EU) 2016/679) | gdpr-info.eu (text of the Regulation) | regulator | https://gdpr-info.eu/art-22-gdpr/ | 2016-04-27 | full |
| ISMS-ISO42001-2025 | ISO 42001 Annex A controls (practitioner summary; standard text not read) | ISMS.online | vendor | https://www.isms.online/iso-42001/annex-a-controls/ | 2025-08-21 | full (summary only) |
| CFPB-CIRC2203-2022 | Consumer Financial Protection Circular 2022-03: Adverse action notification requirements in connection with credit decisions based on complex algorithms | CFPB | regulator | https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/ | 2022-05-26 | full |
| CFPB-ADVERSE-2023 | CFPB issues guidance on credit denials by lenders using artificial intelligence | CFPB | regulator | https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/ | 2023-09-19 | full |
| FRB-SR117-2011 | SR 11-7: Supervisory Guidance on Model Risk Management (attachment) | Federal Reserve Board and OCC | regulator | https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf | 2011-04-04 | full |
| FCA-CASS715-2026 | FCA Handbook, CASS 7.15 Records, accounts and reconciliations | Financial Conduct Authority | regulator | https://www.handbook.fca.org.uk/handbook/CASS/7/15.html | 2026-09-25 (page last updated) | full |
| REEDSMITH-CMSAI-2024 | CMS confirms Medicare Advantage organizations may use AI in making coverage determinations (summary of CMS FAQ of 2024-02-06; CMS primary not opened) | Reed Smith | firm | https://www.reedsmith.com/de/perspectives/2024/02/cms-confirms-medicare-advantage-organizations-may-use-ai-in-making-coverage | 2024-02-13 | full |
| CASENATE-SB1120-2024 | Governor signs Physicians Make Decisions Act, keeping medical decisions between patients and doctors, not AI | Office of Senator Josh Becker, California Senate | regulator | https://sd13.senate.ca.gov/node/934 | 2024-09-30 | full |
| ROBODEBT-RC-2023 | Report of the Royal Commission into the Robodebt Scheme: list of recommendations | Royal Commission into the Robodebt Scheme (Australia) | regulator | https://robodebt.royalcommission.gov.au/publications/report | 2023-07-07 | full (recommendations page only) |
| VAOIG-ABD-2023 | Improvements Needed for VBA's Claims Automation Project (22-02936-175) | VA Office of Inspector General | regulator | https://www.oversight.gov/sites/default/files/oig-reports/VA/VAOIG-22-02936-175.pdf | 2023-09-25 | full |
| WUNC-VADIC-2026 | Audit finds VA automation glitch ruined 98% of veteran survivors' benefits claims | WUNC News | press | https://www.wunc.org/2026-06-19/audit-finds-va-automation-glitch-ruined-98-of-veteran-survivors-benefits-claims | 2026-06-19 | full |
| LOKKEN-ORDER-2025 | Estate of Lokken et al. v. UnitedHealth Group: Memorandum Opinion and Order (D. Minn.) | US District Court, District of Minnesota (via Georgetown litigation tracker) | regulator | https://litigationtracker.law.georgetown.edu/wp-content/uploads/2023/11/Lokken_2025.02.13_MEMORANDUM-OPINION-AND-ORDER.pdf | 2025-02-13 | full |
| NIST-SEMATECH-LASP | NIST/SEMATECH e-Handbook of Statistical Methods, 6.2.2 What kinds of Lot Acceptance Sampling Plans are there? | NIST | standard-setter | https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc22.htm | 2026-10-20 (page undated; retrieval date) | full |
| GREEN-OVERSIGHT-2022 | The flaws of policies requiring human oversight of government algorithms, Computer Law & Security Review 45 | Ben Green, University of Michigan | academic | https://arxiv.org/pdf/2109.05067v3 | 2022 | full |
| PEETERS-ENTITYLLM-2024 | Entity Matching using Large Language Models (arXiv 2310.11244v4) | Peeters, Steiner, Bizer, University of Mannheim | academic | https://arxiv.org/pdf/2310.11244 | 2024-10-18 | full |
| NARAYAN-FMDATA-2022 | Can Foundation Models Wrangle Your Data? (arXiv 2205.09911v2) | Narayan et al., Stanford University | academic | https://arxiv.org/pdf/2205.09911 | 2022-12-24 | full (abstract and introduction) |
| KUMAR-EXTRACTCONF-2026 | Beyond Logprobs: A Multi-Signal Confidence Engine for LLM-Based Document Field Extraction (arXiv 2606.24420) | Nitesh Kumar, Perfios Software Solutions | academic | https://arxiv.org/pdf/2606.24420 | 2026-06-23 | full |
| GARTNER-AGENTIC-2025 | Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027 | Gartner | survey | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | 2025-06-25 | full (via text mirror) |
| MCKINSEY-STATEAI-2026 | The state of AI in 2026: On the road to ROI | McKinsey & Company | survey | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | 2026-08-25 | full (via text mirror) |
| PROPUBLICA-CIGNA-2023 | How Cigna Saves Millions by Having Its Doctors Reject Claims Without Reading Them | ProPublica and The Capitol Forum | press | https://www.propublica.org/article/cigna-pxdx-medical-health-insurance-rejection-claims | 2023-03-25 | full |
| HCDIVE-UNH-2023 | UnitedHealth algorithm lawsuit (care denials) | Healthcare Dive | press | https://www.healthcaredive.com/news/unitedhealth-algorithm-lawsuit-care-denials/699834/ | 2023-11-15 | full |
| INSURANCENEWS-NEMO-2025 | AI trial provides blueprint for future, Allianz says | insuranceNEWS.com.au | press | https://www.insurancenews.com.au/insurtech/ai-trial-provides-blueprint-for-future-allianz-says | 2025-11-24 | full |
| ABAJ-COIN-2017 | JPMorgan Chase uses tech to save 360,000 hours of annual work by lawyers and loan officers (relays Bloomberg) | ABA Journal | press | https://www.abajournal.com/news/article/jpmorgan_chase_uses_tech_to_save_360000_hours_of_annual_work_by_lawyers_and | 2017-03-02 | full |
| GOV-CONSULT-2025 | Government-built 'Humphrey' AI tool reviews responses to consultation for first time, in bid to save millions | UK Government (GOV.UK) | regulator | https://www.gov.uk/government/news/government-built-humphrey-ai-tool-reviews-responses-to-consultation-for-first-time-in-bid-to-save-millions | 2025-05-14 | full |
| RAMP-AGENTS-2025 | Ramp agents announcement | Ramp | vendor | https://ramp.com/blog/ramp-agents-announcement | 2025-07-09 | full |
| RAMP-COMM-2025 | New on Ramp: AI Agents (community post) | Ramp | vendor | https://community.ramp.com/t/new-on-ramp-ai-agents/956 | 2025-07-15 | full |
| ZENML-VENDR | Scaling Document Processing with LLMs and Human Review (Vendr and Extend, NLP Summit talk summary) | ZenML LLMOps database | conference | https://zenml.io/llmops-database/scaling-document-processing-with-llms-and-human-review | 2026-10-20 (page undated; retrieval date) | full |
| HIGHRADIUS-KONICA-2025 | Konica Minolta: close and reconciliation case study | HighRadius | vendor | https://www.highradius.com/en-gb/value-creation/http://konica-minolta-close-and-reconciliation/ | 2025-04-17 (page metadata) | full |
| TRINTECH-AUTONATION-2026 | The Reality of AI Reconciliations: AutoNation spotlight webinar | Trintech | vendor | https://www.trintech.com/webinar/reality-of-ai-reconciliations-autonation/ | 2026-08-19 (page updated) | full (abstract only) |
| BLACKLINE-BEAUTYPIE | From Manual Matching to 99.6% Automation: Beauty Pie's BlackLine Success Story | BlackLine | vendor | https://www.blackline.com/customers/beauty-pie/ | 2026-10-20 (page undated; retrieval date) | full |
| CASESTUDIES-GLOBE | Case Study: Globe Telecom reduces audit findings time by 60% with BlackLine | CaseStudies.com | vendor | https://www.casestudies.com/company/blackline/case-study/globe-cuts-time-to-audit-findings-by-60-with-blackline | 2026-10-20 (page undated; retrieval date) | full |
| NASDAQ-BROADRIDGE-2019 | New AI and ML Platform for Reconciliation, Matching and Exception Management Operations Introduced by Broadridge (press release) | Broadridge via Nasdaq | vendor | https://www.nasdaq.com/press-release/new-artificial-intelligence-and-machine-learning-platform-for-reconciliation-matching | 2019-12-03 | full |
| FIA-BROADRIDGE-2019 | Broadridge teams with Singapore fintech to reduce trade reconciliation inefficiencies | FIA | professional-body | https://www.fia.org/articles/broadridge-teams-singapore-fintech-reduce-trade-reconciliation-inefficiencies | 2019-12-23 | full |
| DIGIT-XERO-2026 | Xero AI roadmap: JAX, Syft analytics | Digit Business (Xero-partner accounting firm) | firm | https://digit.business/insights/xero/xero-ai-roadmap-jax-syft-analytics | 2026-02-23 | full |
| KOGNITOS-AP-2026 | Why Most Agentic AP Pilots Stall at 70% Touchless | Kognitos | vendor | https://www.kognitos.com/blog/agentic-ap-pilot-stalled-70-percent-touchless/ | 2026-06-02 | full |
| HN-ASKHN-2025 | Ask HN: Is anyone using LLM based document processing in production? | Hacker News (read through the Algolia API) | community | https://news.ycombinator.com/item?id=46319267 | 2025-12-18 | full |

Search-only sightings, not relied on for any grade or outcome:

| Ref | What was seen | Type | Date | Access |
|---|---|---|---|---|
| ARDENT-VIA-AGGREGATORS-2025 | Ardent Partners State of ePayables figures (14% average invoice exception rate, 9% best-in-class) quoted by aggregators | survey | 2025 | search-only |
| MCKINSEY-AVIVA | McKinsey case study on Aviva claims (65% fewer complaints quoted in a snippet); page blocked | firm | date not seen | search-only |
| SIMBO-AUBURN | Vendor blogs repeating Auburn Community Hospital results (50% fewer discharged-not-final-billed cases) | vendor | date not seen | search-only |
| AIENG-SUBSTACK | Practitioner post on per-field thresholds | community | date not seen | search-only |
| BASWARE-77 | A 77% touchless match rate reported by Basware for its own AP process, in an aggregator page | vendor | 2025-03 | search-only |
| LUKETINA-VAT-2026 | Study cited in `tax-indirect-tax-22` (not re-researched) | academic | 2026 | via archetype |

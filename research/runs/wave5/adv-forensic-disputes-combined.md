# Advisory: forensic-disputes (combined angles: practice, discourse, governance and evidence)

Run date: 2026-10-20. Wave 5. Archetype: `advisory`. Module: `forensic-disputes`. Angle: `combined`.

Conventions: refs follow `PUBLISHER-SHORT-YYYY` and reuse the landscape's refs where the document is the same (ACFE-TECHBENCH-2026, AICPA-FVS-2026, BVR-AICPAAIGUIDE-2025, JSHELD-AIEXPERT-2026). All quotations are under 25 words. Dates are ISO. `access: full` means the page or PDF was opened and read in this run (directly, or through the r.jina.ai mirror where the site blocked curl). `access: search-only` means the item surfaced only in search results.

---

## 1. Summary

**What the public evidence shows.** Public evidence on AI in forensic and disputes work at accounting and advisory firms is thin on measured results and rich on governance. No accounting-firm forensic practice has published a tracked error rate, override rate, or parallel-run result for AI. The best measured numbers come from adjacent processes: e-discovery document review (a law-firm case study re-analysed by independent academics), corporate anti-fraud programs (ACFE surveys), and federal judges (an FJC survey). **No use case reaches grade A**; six are grade B, four C and five D (ideas).

**Key findings.**

1. **Practice is real but self-reported, and mostly data preparation.** The only named forensic-consulting deployments with figures are two J.S. Held case studies (published 2026-05-21): AI-assisted tools processed 20,000 transactions across 10 accounts "in just hours" and 25,000+ checks "in days rather than weeks". These are narrative case studies with unnamed clients, not tracked metrics (JSHELD-AIFRAUD-2026). J.S. Held is not a CPA firm and says it provides no attest services (JSHELD-AIEXPERT-2026, footer), so independence limits do not apply to it.
2. **The binding constraint is evidence law, not capability.** Two court decisions turned a vague worry into concrete risk for experts: *Kohls v. Ellison* (D. Minn., 2025-01-10) excluded an expert declaration in full over unverified, fabricated AI citations, and *Matter of Weber* (N.Y. Sur. Ct., Saratoga County, 2024) rejected a damages expert's Copilot cross-check after the judge re-ran the query and got different numbers (KTS-EXPERTAI-2026; AICPA-COPILOT-2025).
3. **Proposed Federal Rule of Evidence 707 is not law and its path is unsettled.** It was published for comment in August 2025; the Evidence Rules committee met on 2026-05-07; the Standing Committee's September 2026 report lists only "continued consideration" of a possible new Rule 707 and a possible Rule 901(c) on deepfakes (USCOURTS-STDCOMM-2026; USCOURTS-EVAGENDA-2026). This corrects the landscape's June 2026 "sent back" item, which rested on snippet-only secondary sources.
4. **Deepfake evidence is a discussed risk with thin measured incidence.** A Federal Judicial Center survey found 15 of 931 responding federal judges (about 2%) had met a deepfake challenge (USCOURTS-EVAGENDA-2026, pp. 226-227). One California case ended in a terminating sanction (NBC-DEEPFAKE-2025). Practitioner surveys say fraudsters are ahead: only 7% of ACFE/SAS respondents say they are more than moderately prepared for AI-fuelled fraud (ACFE-TECHBENCH-2026).
5. **Independent measurement of generative-AI review is contested.** Relativity's aiR Review showed 87.7% recall and 28.6% precision in a Redgrave LLP case study; independent academics argue the comparison to managed review was not like for like and that, once adjusted, aiR and manual review are comparable (CGP-ARXIV-2026, dated 2026-10-12).

**Evidence absence, stated plainly.** No survey of accounting-firm forensic teams; no published override or error rates for AI in damages or tracing work; no named Big Four forensic AI launch found; no job postings from forensic practices that show AI duties (the one posting found is an AI lab hiring forensic accountants as trainers); no Reddit or community threads could be reached (blocked). See section 6.

**Counts.** 15 use cases: A=0, B=6, C=4, D=5. 39 sources listed: 38 opened in full and 1 search-only (counts by type in section 5).

---

## 2. Use cases

```yaml
- id: advisory-forensic-disputes-01
  title: AI extraction of bank, check and brokerage records into structured financial evidence
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [data-reporting]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Forensic teams spend a large share of a project turning PDFs, scanned statements and check images into usable
    data before analysis can start. J.S. Held says collection and validation took a substantial share of project
    budgets, sometimes as high as 50%, before AI and machine learning.
  solution: >-
    AI-enhanced OCR and extraction convert bank statements, checks and brokerage statements into structured,
    reconciled data that links back to the source documents; people then analyse the data. J.S. Held does not name
    the software in its case studies. Valid8 sells a purpose-built platform for this step.
  outcomes:
    - lever: speed
      description: >-
        In one matter, full payor details for over 25,000 checks (including poor-image ones) were ready for analysis
        in a few days; the firm contrasts this with weeks.
      figure: "25,000+ checks; 'days rather than weeks'"
      measures: >-
        Count of checks processed in a single healthcare-staffing lapping matter; the weeks comparison is the firm's
        own estimate, not a tracked metric.
      provenance: self-reported
      source_ref: JSHELD-AIFRAUD-2026
    - lever: quality
      description: >-
        A forensic principal at Anders CPAs & Advisors says hand-keying data gets about 85% accuracy and AI tools get
        99%, sometimes 100%, depending on image quality.
      figure: "85% vs 99-100%"
      measures: >-
        Interviewee's stated data-entry accuracy from images, hand-keyed versus AI tools; a recollection with no
        sample size, published in a vendor white paper.
      provenance: vendor-published
      source_ref: VALID8-WP-2025
    - lever: speed
      description: Valid8's site claims millions of transactions reconciled automatically over 10x faster than manual review.
      figure: "over 10x faster"
      measures: "Vendor's stated speed of automatic reconciliation versus manual review; basis not given."
      provenance: vendor-published
      source_ref: VALID8-SITE-2026
  prerequisites:
    - Source documents of readable quality; poor images were still processed in the J.S. Held matter but remain a stated dependency.
    - A reconciliation check on every extracted statement (Valid8 describes balance checks on each statement).
    - Source-to-output linking so every transaction traces back to bank evidence.
  risks_and_guardrails:
    - J.S. Held says OCR inside many PDF editors is unreliable on hard-to-read pages, which is why it uses enhanced AI OCR (JSHELD-AIFRAUD-2026, p. 6).
    - Accuracy depends on image quality (VALID8-WP-2025).
    - Output must stand up as evidence, so extraction needs to be reproducible and tied to originals (JSHELD-AIFRAUD-2026, p. 4).
  human_checkpoints:
    - Every transaction is linked back to the original banking evidence before a report goes out (JSHELD-AIFRAUD-2026, p. 4).
    - Professionals interpret transaction analyses and perform due diligence on flagged people and entities (JSHELD-AIFRAUD-2026, p. 3).
  role_evolution: >-
    J.S. Held's practitioners say the aim is for professionals to spend more time thinking and less time processing
    (JSHELD-AIFRAUD-2026, p. 6). Valid8 pitches the automation partly as a recruiting aid for graduates (VALID8-HUB-2026).
  evidence_grade: B
  sources:
    - { ref: JSHELD-AIFRAUD-2026, title: "AI Fraud Detection and Forensic Accounting: Embracing Innovation to Combat Financial Threats (Third Edition)", publisher: J.S. Held, type: firm, url: "https://www.jsheld.com/uploads/AI-Fraud-Detection-and-Forensic-Accounting-Embracing-Innovation-to-Combat-Financial-Threats_FINAL.pdf", date: 2026-05-21, access: full, locator: "pp. 4-7 (case studies; ML for forensic accounting; OCR)" }
    - { ref: VALID8-WP-2025, title: "The Impact of AI on Fraud Investigations: What Forensic Accountants Need to Know", publisher: Valid8 Financial, type: vendor, url: "https://valid8financial.com/white-paper/ai-impact-on-fraud-investigations", date: 2025-02, access: full, locator: "Kniepmann interview section" }
    - { ref: VALID8-SITE-2026, title: "Verified Financial Intelligence and Forensic Accounting Software (home page)", publisher: Valid8 Financial, type: vendor, url: "https://www.valid8financial.com/", date: 2026-10-08, access: full, locator: "feature section" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: forensic and consulting firm that is not a CPA firm (J.S. Held), a vendor (Valid8) and a mid-market
    CPA firm practitioner (Anders, quoted by the vendor). Independence: not a constraint for J.S. Held, which states
    it provides no attest services; for a CPA firm that audits the same client, expert-witness and litigation-support
    work is likely restricted (not verified in this run; confirm against the AICPA Code and SEC rules).
    The VALID8-WP-2025 date is inferred: the page is undated and a related Valid8 article carries a video upload date
    of 2025-02-10. Valid8's customer base claim ("more than 1,800 accounting firms, law firms, and government agencies")
    is on VALID8-HUB-2026 and is a vendor claim.

- id: advisory-forensic-disputes-02
  title: Full-population matching of checks and transactions to find embezzlement and lapping and to quantify loss
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Tracing a scheme across thousands of checks and several accounts is slow when done by hand, and a lapping scheme
    (payments from one customer applied to another's account) is hard to see without matching every item.
  solution: >-
    AI-assisted software matches every transaction and check to bank records automatically, flags missing or
    incomplete data, and links each item back to evidence. Forensic accountants then interpret the matches, calculate
    losses and write the report. In one matter the work came through an insurer's claim; in the other through a
    buyer's CFO after an acquisition.
  outcomes:
    - lever: speed
      description: >-
        An analysis that could have taken weeks took a matter of days; 20,000 transactions across 10 accounts over
        five years were matched in hours.
      figure: "20,000 transactions, 10 accounts, 5 years; matched 'in just hours'"
      measures: >-
        Transaction count in an embezzlement matter at a school; the weeks-to-days comparison is the firm's estimate.
      provenance: self-reported
      source_ref: JSHELD-AIFRAUD-2026
    - lever: risk
      description: >-
        More than $7 million potentially embezzled was identified in one matter, and more than $30 million of
        potentially misapplied payments in the other (the summary says more than $37 million combined).
      figure: ">$7M and >$30M"
      measures: >-
        Amounts the firm identified as potentially embezzled or misapplied in two matters; these are findings, not a
        measure of AI accuracy, and were not independently checked.
      provenance: self-reported
      source_ref: JSHELD-AIFRAUD-2026
  prerequisites:
    - Complete bank and check image data for the full period.
    - Structured data (see advisory-forensic-disputes-01).
    - A clear matching rule set agreed by the lead professional.
  risks_and_guardrails:
    - Anomalies flagged by AI may be errors rather than fraud, and false positives can derail an investigation (CPAPA-FORENSICAI-2025).
    - Perpetrators can adapt once they learn how algorithms score risk (CPAPA-FORENSICAI-2025).
    - The J.S. Held case studies do not publish false-positive or miss rates; none were found elsewhere.
  human_checkpoints:
    - Forensic accountants interpret matches and calculate damages; every item is linked to the original evidence (JSHELD-AIFRAUD-2026, pp. 4-5).
  role_evolution: >-
    J.S. Held describes AI as augmenting forensic accounting professionals rather than replacing them
    (JSHELD-AIFRAUD-2026, Executive Summary).
  evidence_grade: B
  sources:
    - { ref: JSHELD-AIFRAUD-2026, title: "AI Fraud Detection and Forensic Accounting: Embracing Innovation to Combat Financial Threats (Third Edition)", publisher: J.S. Held, type: firm, url: "https://www.jsheld.com/uploads/AI-Fraud-Detection-and-Forensic-Accounting-Embracing-Innovation-to-Combat-Financial-Threats_FINAL.pdf", date: 2026-05-21, access: full, locator: "pp. 4-5 (two case studies)" }
    - { ref: CPAPA-FORENSICAI-2025, title: "Forensic Accounting in the Age of AI: Opportunities and Risks", publisher: CPA Practice Advisor (author: Frank Dery, BRG), type: press, url: "https://www.cpapracticeadvisor.com/2025/10/15/forensic-accounting-in-the-age-of-ai-opportunities-and-risks-2/170853/", date: 2025-10-15, access: full, locator: "risks section" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: forensic and consulting firm, not a CPA firm. The software is not named. Graded B, not A: the timing
    figures are narrative estimates and the dollar figures are findings. Clients are unnamed in the source.

- id: advisory-forensic-disputes-03
  title: Proactive data monitoring and machine-learning anomaly detection inside client anti-fraud programs
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: >-
    Most occupational fraud is found by tips, and fraud runs for months before it is detected; analytics-based
    detection is in place in fewer than half of the organisations in the ACFE study.
  solution: >-
    Organisations (and advisers who design or run their programs) monitor transactions continuously and use machine
    learning to flag anomalies for investigators. The ACFE data measure data monitoring and analysis in general, not
    AI specifically.
  outcomes:
    - lever: risk
      description: >-
        Where proactive data monitoring/analysis was in place, median fraud loss was $70,000 against $150,000 where it
        was not, and median duration 9 months against 16.
      figure: "$70,000 vs $150,000 (53% lower); 9 vs 16 months"
      measures: >-
        Median loss and duration in cases (of 2,402 occupational fraud cases from 143 countries) where the victim had
        the control versus did not; the control was in place in 49% of cases. An association, not a causal result,
        and it covers analytics broadly, not AI.
      provenance: independent
      source_ref: ACFE-RTTN-2026
    - lever: risk
      description: Automated transaction/data monitoring was the initial detection method in 3% of cases; tips accounted for 43%.
      figure: "3% of cases (tips 43%)"
      measures: >-
        Share of the 2,402 cases in which the fraud was initially detected by each method (Fig. 13).
      provenance: independent
      source_ref: ACFE-RTTN-2026
    - lever: capacity
      description: >-
        25% of surveyed organisations use AI/ML in anti-fraud programs, up from 18% in 2024; another 28% expect to by 2028.
      figure: "25% (18% in 2024)"
      measures: >-
        Share of 713 anti-fraud professionals (ACFE/SAS survey, eight regions) saying their organisation uses AI/ML in
        its anti-fraud program.
      provenance: vendor-published
      source_ref: ACFE-TECHBENCH-2026
  prerequisites:
    - Clean, accessible transaction data across systems.
    - Investigators who can interpret model output with forensic judgment (JRFM-FORENSICAI-2026).
    - Budget: 84% cite budget and financial restrictions as a major or moderate barrier (ACFE-TECHBENCH-2026).
  risks_and_guardrails:
    - Only 18% of respondents test AI models for bias or fairness, and just 6% feel completely confident explaining how their AI/ML models make anti-fraud decisions (ACFE-TECHBENCH-2026).
    - A literature review finds ML beats rule-based methods where quality data exist but says the advantage is not universal and depends on fraud type, model design and context (JRFM-FORENSICAI-2026, Abstract).
    - Evidentiary validity of algorithmic results is flagged as unresolved in the same review (JRFM-FORENSICAI-2026, Abstract).
  human_checkpoints:
    - Investigators decide whether a flagged anomaly is meaningful (CPAPA-FORENSICAI-2025).
  role_evolution: >-
    Practitioner commentary expects AI to change the type of work forensic accountants do without replacing the role
    (CPAPA-FORENSICAI-2025).
  evidence_grade: B
  sources:
    - { ref: ACFE-RTTN-2026, title: "Occupational Fraud 2026: A Report to the Nations", publisher: ACFE, type: professional-body, url: "https://www.acfe-mexico.com.mx/inicio/sitepad-data/uploads/2026/07/Reporte-a-las-Naciones-2026.pdf", date: 2026-05-12, access: full, locator: "Fig. 13 (Detection, pp. 23-25); control-effectiveness tables (p. 41); proactive data monitoring summary (p. 47)" }
    - { ref: ACFE-TECHBENCH-2026, title: "Study: Deepfake fraud surges - and only 7% of organizations are firmly ready (2026 Anti-Fraud Technology Benchmarking Report press release)", publisher: SAS with ACFE, type: survey, url: "https://www.sas.com/en_us/news/press-releases/2026/march/acfe-anti-fraud-technology-study-deepfakes.html", date: 2026-03-25, access: full, locator: "survey findings bullets" }
    - { ref: JRFM-FORENSICAI-2026, title: "Artificial Intelligence and Machine Learning in the Transformation of Forensic Accounting: A Systematic Literature Review", publisher: "Journal of Risk and Financial Management (MDPI)", type: academic, url: "https://doi.org/10.3390/jrfm19070519", date: 2026-07-10, access: full, locator: "Abstract; Conclusions" }
    - { ref: CPAPA-FORENSICAI-2025, title: "Forensic Accounting in the Age of AI: Opportunities and Risks", publisher: CPA Practice Advisor (author: Frank Dery, BRG), type: press, url: "https://www.cpapracticeadvisor.com/2025/10/15/forensic-accounting-in-the-age-of-ai-opportunities-and-risks-2/170853/", date: 2025-10-15, access: full, locator: "opportunities and challenges lists" }
  last_reviewed: 2026-10-20
  notes: >-
    Grade capped at B: the ACFE figures are measured by a named body but concern corporate anti-fraud programs and
    analytics in general, not an advisory firm's AI use. The ACFE report contains no AI-specific findings (searched
    for AI, generative, deepfake and machine learning terms). The 25% adoption figure is from the joint ACFE/SAS
    survey as published in a SAS press release, so provenance is marked vendor-published. Overlaps with risk-controls
    (fraud-risk program design); kept here for the detection and investigation use.

- id: advisory-forensic-disputes-04
  title: Generative-AI first-pass responsiveness and issue review of documents in disputes and investigations
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    First-level review of very large document sets is slow and costly, and results vary between human reviewers.
  solution: >-
    A large language model applies the written review protocol to each document, returns a coding with rationale and
    citations, and people validate by sampling. Relativity aiR for Review is the main product; Everlaw sells a
    comparable tool. In investigations work, forensic firms such as J.S. Held list digital investigations and discovery
    as a practice but publish no review metrics.
  outcomes:
    - lever: quality
      description: >-
        In a Redgrave LLP case study, aiR reached 87.7% recall and 28.6% precision against 64.4% and 39.2% for a managed
        review using Relativity Assisted Learning. Independent academics argue the two are not comparable and that, once
        adjusted, aiR and manual review are comparable.
      figure: "aiR 87.7% recall / 28.6% precision; managed review 64.4% / 39.2%"
      measures: >-
        Recall and precision against a subject-matter expert's coding of a simple random sample of 1,000 documents
        (73 responsive) from a 45,004-document set; recall 95% CI 77.9-94.2% for aiR and 52.3-75.3% for managed review.
        Figures originate with the Redgrave case study and are reproduced here from the independent re-analysis.
      provenance: independent
      source_ref: CGP-ARXIV-2026
    - lever: quality
      description: >-
        In the same data, the first-level reviewers coded as non-responsive 34% of documents the expert deemed
        responsive, and the expert coded as non-responsive 61% of those the reviewers deemed responsive.
      figure: "34% and 61% disagreement"
      measures: >-
        Inter-assessor disagreement between first-level reviewers and the subject-matter expert on the Redgrave data;
        shows ground truth itself is contestable.
      provenance: independent
      source_ref: CGP-ARXIV-2026
    - lever: quality
      description: Relativity says aiR achieves 90%+ recall without the setup that technology-assisted review demands.
      figure: "90%+ recall"
      measures: "Vendor's product-page claim; no sample, matter or method given."
      provenance: vendor-published
      source_ref: RELATIVITY-AIR-2026
    - lever: quality
      description: >-
        Everlaw reports its generative coding tool matched human precision and recall on four datasets and, in the one
        case with a direct comparison, beat first-level reviewers on recall by 36%.
      figure: "+36% recall in one case"
      measures: >-
        Recall comparison against first-level human review in one of four real civil-litigation datasets
        (7,737 documents in total); vendor's own test, 2024.
      provenance: vendor-published
      source_ref: EVERLAW-GENAI-2024
  prerequisites:
    - A written review protocol clear enough to serve as the prompt.
    - A validation sample coded by a subject-matter expert (CGP-ARXIV-2026, section 2).
    - A platform that keeps data in place with audit trails (RELATIVITY-AIR-2026).
  risks_and_guardrails:
    - Recall and precision are measured against a particular assessor, not an infallible ground truth (CGP-ARXIV-2026, section 4).
    - aiR and older machine-learning methods sit at different recall-precision trade-offs, and the independent authors say established continuous active learning showed equal or better efficiency on the Redgrave data (CGP-ARXIV-2026, section 3).
    - Courts have not set gen-AI-specific discovery standards, per a vendor-affiliated author who argues proportionality rules already apply (HAYSTACKID-GENAI-2026).
  human_checkpoints:
    - Sample validation against an expert's coding before relying on the results.
    - Decisions stay with legal practitioners (RELATIVITY-AIR-2026).
  role_evolution: >-
    First-level contract review is the step being replaced in the studies; the Redgrave comparison pitted the tool
    against a team of junior contract lawyers (CGP-ARXIV-2026, section 1).
  evidence_grade: B
  sources:
    - { ref: CGP-ARXIV-2026, title: "Comparing GenAI to Machine Learning and Manual Review for eDiscovery", publisher: "University of Waterloo and Elevate (arXiv:2610.16925)", type: academic, url: "https://arxiv.org/abs/2610.16925", date: 2026-10-12, access: full, locator: "Abstract; sections 1, 2, 4 and Table 1" }
    - { ref: RELATIVITY-AIR-2026, title: "Relativity aiR (product page)", publisher: Relativity, type: vendor, url: "https://www.relativity.com/data-solutions/air/", date: 2026-10-20, access: full, locator: "AI-assisted review section" }
    - { ref: EVERLAW-GENAI-2024, title: "GenAI Document Review Surpasses Human Performance on Real World Litigation Data", publisher: Everlaw, type: vendor, url: "https://www.everlaw.com/blog/ai-and-automation/genai-document-review-surpasses-human-performance-on-real-world-litigation", date: 2024-09-19, access: full, locator: "report summary paragraphs" }
    - { ref: HAYSTACKID-GENAI-2026, title: "From Review to Intelligence: How Gen AI Is Transforming Discovery Strategy", publisher: HaystackID (author Esther Birnbaum, Law.com reprint), type: vendor, url: "https://haystackid.com/wp-content/uploads/2026/01/LTN0123202670120Haystackid.pdf", date: 2026-01-22, access: full, locator: "opening paragraphs; Rule 26(b)(1) discussion" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: law firm and e-discovery consultancy (Redgrave) plus vendors (Relativity, Everlaw). This is an adjacent
    process to accounting-firm forensic work, so the grade is capped at B even though the numbers are measured.
    The page for the product is undated; 2026-10-20 is the access date. The Redgrave paper itself (Keeling et al.)
    was not opened; its numbers are taken from the independent re-analysis. The earlier Relativity and Redgrave Data
    preprint (OMRANI-BEYONDBAR-2024) reported an estimated 96% recall and 60% precision on a live matter; it is a vendor-affiliated
    preprint and is not used for figures. HaystackID's article also quotes unnamed matters (an Am Law 100 firm cutting
    review time by 50-67% with 90%+ accuracy across 126,000 documents; a 2-million-document federal regulatory matter
    at 88% recall and 96% precision); these are unnamed, vendor-authored and not verifiable, so they stay in notes.

- id: advisory-forensic-disputes-05
  title: Plain-language questions over a live investigation or dispute document set, with cited answers
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: >-
    Early in a matter, teams need quick answers about people, events and key documents without waiting for a full review.
  solution: >-
    A question-and-answer assistant runs on the matter data inside the review platform and returns cited answers.
    Relativity describes this as aiR Assist.
  outcomes:
    - lever: speed
      description: An unnamed customer quote on the vendor's page says the tool surfaces critical evidence in minutes.
      figure: none published
      measures: "Anonymous customer testimonial; no measurement."
      provenance: vendor-published
      source_ref: RELATIVITY-AIR-2026
  prerequisites:
    - Matter data hosted in the platform; the page states support for up to 1.5 million documents per workspace.
  risks_and_guardrails:
    - Answers need citations and an auditable platform to be defensible (RELATIVITY-AIR-2026).
    - Rule 707 as drafted would apply to machine output offered without an expert and would require a showing of reliability (USCOURTS-FRE707-2025).
  human_checkpoints:
    - Practitioners verify answers against the cited source documents.
  role_evolution: >-
    Vendor says the aim is to get to direction in moments rather than weeks (RELATIVITY-AIR-2026); no firm has said
    how roles changed.
  evidence_grade: C
  sources:
    - { ref: RELATIVITY-AIR-2026, title: "Relativity aiR (product page)", publisher: Relativity, type: vendor, url: "https://www.relativity.com/data-solutions/air/", date: 2026-10-20, access: full, locator: "aiR Assist section" }
    - { ref: USCOURTS-FRE707-2025, title: "Proposed Federal Rule of Evidence 707, Machine-Generated Evidence (published draft and committee note)", publisher: "US federal judiciary (copy hosted by Steptoe)", type: regulator, url: "https://www.steptoe.com/a/web/mfVW1ZxAuBkvow2pShnt2X/proposed-rule-707.pdf", date: 2025-08, access: full, locator: "rule text and first paragraphs of the committee note" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: vendor. No named deployment or measurement found; maturity is announced.

- id: advisory-forensic-disputes-06
  title: Sandboxed LLM for document review, data requests and summarisation in IP damages and valuation disputes, checked against traditional methods
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >-
    Patent-heavy disputes require reading a patent plus related patents, but time and cost limit how many related
    documents a team can review.
  solution: >-
    J.S. Held's intellectual property practice says it is building models in a private sandbox so data is not disclosed
    to third parties, trained on industry data and prior work, then queried for document review, data requests and
    summaries. Every item is reviewed by a managing director and sourced back to original evidence, and analyses are
    double-checked with traditional methods to compare answers.
  outcomes:
    - lever: quality
      description: >-
        The practice says AI lets it expand greatly the set of related patents it reviews, which it says would be
        impossible to do on a time- or cost-efficient basis without it. No figures published.
      figure: none published
      measures: "Chief intellectual property officer's statement; no sample or metric given."
      provenance: self-reported
      source_ref: JSHELD-AIEXPERT-2026
  prerequisites:
    - A private sandbox environment for client data.
    - A parallel traditional analysis to compare answers.
    - An amended engagement letter notifying clients of AI use (see advisory-forensic-disputes-07).
  risks_and_guardrails:
    - Opacity of proprietary AI makes methods hard to examine and explain (JSHELD-AIEXPERT-2026).
    - Courts have sanctioned lawyers for relying on AI for citations that did not exist (JSHELD-AIEXPERT-2026).
  human_checkpoints:
    - Managing-director review of every item, sourced to original evidence (JSHELD-AIEXPERT-2026).
    - Double-checking AI analyses with traditional methods (JSHELD-AIEXPERT-2026).
  role_evolution: >-
    The article expects AI to become a common part of every expert's practice and says experts should expect questions
    about their AI use in proceedings (JSHELD-AIEXPERT-2026).
  evidence_grade: B
  sources:
    - { ref: JSHELD-AIEXPERT-2026, title: "Expertise in the Age of Algorithms: Trust and Transparency in AI-Assisted Litigation", publisher: J.S. Held, type: firm, url: "https://www.jsheld.com/insights/articles/expertise-in-the-age-of-algorithms-trust-and-transparency-in-ai-assisted-litigation", date: 2026-02-03, access: full, locator: "section quoting James Malackowski on the IP practice" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: forensic and consulting firm, not a CPA firm. Stated as "developing models" so maturity is piloting; the
    parallel-run comparison is described but no results are published. The practice is IP litigation, valuation and
    transactions; the damages and valuation side overlaps with the valuation module. The same article is scheduled as a
    session at the AICPA FVS Conference (FVC2638, 2026-11-06), so it is also a discourse signal.

- id: advisory-forensic-disputes-07
  title: Disclosure, verification and audit-trail protocol for AI use in expert work product
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Courts have excluded or discounted expert work when AI output was unverified or unexplainable, and counsel may now
    ask experts whether AI was used.
  solution: >-
    Experts and their retaining parties add AI-specific terms to engagement letters (written disclosure of tool,
    version, tasks and verification; independent verification not using the same tool; closed-system tools only;
    prompt and output logs; remedies for breach). J.S. Held's IP practice amended its standard engagement letter to
    tell clients it will use AI tools unless they opt out. The pattern is a verification and disclosure layer, not a
    standard agentic pattern.
  outcomes:
    - lever: risk
      description: >-
        In Matter of Weber the judge re-ran the expert's Copilot query on three court computers and got three different
        numerical results, none matching the expert's figure; the court held that AI-assisted calculations need a
        reliability showing and counsel must disclose AI use before such evidence is introduced.
      figure: "3 different results from 3 court computers"
      measures: >-
        Outputs when the judge re-ran the expert's Copilot cross-check query on three court-system computers, as
        reported in a law-firm alert.
      provenance: independent
      source_ref: KTS-EXPERTAI-2026
    - lever: risk
      description: >-
        In Kohls v. Ellison the court excluded an expert declaration in its entirety because it cited two non-existent
        articles and misattributed a third, generated by GPT-4o and not verified.
      figure: "2 fabricated citations plus 1 misattributed"
      measures: "Count of citation errors the court found in one expert declaration."
      provenance: independent
      source_ref: PPC-KOHLS-2025
  prerequisites:
    - Engagement-letter language covering disclosure, verification, confidentiality, logging and remedies.
    - Closed-system or enterprise tools whose terms bar training on inputs.
    - Records of prompts, inputs, tool versions and outputs.
  risks_and_guardrails:
    - The Kohls court excluded the declaration although the errors were described as innocent; intent did not matter (KTS-EXPERTAI-2026).
    - AICPA's FVS committee guidelines are not a standard but remind members to align AI use with engagement terms, confidentiality and professional judgment (BVR-AICPAAIGUIDE-2025).
    - Verification with the same AI tool is not enough (KTS-EXPERTAI-2026, model verification provision).
  human_checkpoints:
    - The expert authors every opinion and can explain the method without the tool (KTS-EXPERTAI-2026).
    - Counsel confirms before a report is finalised whether AI was used, which tools, and what verification was done (KTS-EXPERTAI-2026).
  role_evolution: >-
    Experts take on documentation and disclosure duties; an AICPA article says it falls to the expert and the court to
    judge whether and how far AI use is acceptable (AICPA-COPILOT-2025).
  evidence_grade: B
  sources:
    - { ref: KTS-EXPERTAI-2026, title: "Expert Engagement Agreements in the Age of Generative AI: Best Practices for Governing Expert Use of AI Tools", publisher: Kilpatrick Townsend, type: firm, url: "https://ktslaw.com/insights/alert/2026/8/expert-engagement-agreements-in-the-age-of-generative-ai", date: 2026-08-31, access: full, locator: "case summaries; model provisions" }
    - { ref: PPC-KOHLS-2025, title: "Minnesota court rejects expert testimony tainted by AI-generated citations", publisher: PPC Land, type: press, url: "https://ppc.land/minnesota-court-rejects-expert-testimony-tainted-by-ai-generated-citations/", date: 2025-01-26, access: full, locator: "paragraphs on the declaration's citation errors" }
    - { ref: BVR-KOHLS-2026, title: "Court excludes AI-tainted expert testimony", publisher: BVWire (Business Valuation Resources), type: press, url: "https://www.bvresources.com/articles/bvwire/court-excludes-ai-tainted-expert-testimony", date: 2026-02-25, access: full, locator: "article body" }
    - { ref: AICPA-COPILOT-2025, title: "Expert witness used Copilot to cross-check calculations, irking judge", publisher: AICPA & CIMA, type: professional-body, url: "https://www.aicpa-cima.com/news/article/expert-witness-used-copilot-to-cross-check-calculations-irking-judge", date: 2025-04-16, access: full, locator: "paragraphs 1-5" }
    - { ref: BVR-AICPAAIGUIDE-2025, title: "AICPA issues AI usage guidelines for valuation and forensic work", publisher: BVWire (Business Valuation Resources), type: professional-body, url: "https://www.bvresources.com/articles/bvwire/aicpa-issues-ai-usage-guidelines-for-valuation-and-forensic-work", date: 2025-10-15, access: full, locator: "first two paragraphs (the guidelines themselves are members-only)" }
    - { ref: JSHELD-AIEXPERT-2026, title: "Expertise in the Age of Algorithms: Trust and Transparency in AI-Assisted Litigation", publisher: J.S. Held, type: firm, url: "https://www.jsheld.com/insights/articles/expertise-in-the-age-of-algorithms-trust-and-transparency-in-ai-assisted-litigation", date: 2026-02-03, access: full, locator: "IP practice section (engagement letter)" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: forensic and consulting firm (J.S. Held, not a CPA firm); other sources are a law firm, the AICPA and
    news. Evidence of use is a single named firm's engagement-letter change, so the grade is B on thin evidence.
    The Weber figure rests on a law-firm summary of the opinion; the opinion itself was blocked (Cloudflare) and was
    not opened. KTS gives the citation as 85 Misc.3d 727 (N.Y. Sur. Ct., Saratoga County 2024); the AICPA article places
    it in late 2024 and names the context as a trust dispute over a Bahamas property. The CGP and Weber findings both
    point at the same weakness: unexplainable or unreproducible output. AICPA scheduled sessions on exactly this topic
    for 2026-11-05 and 2026-11-06 (AICPA-FVS-2026, FVC2617, FVC2627, FVC2638); scheduled only, not given.

- id: advisory-forensic-disputes-08
  title: AI red-flag screening of large document and email sets in fraud investigations
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Early-stage fraud work means sifting boxes of documents and thousands of emails for red flags.
  solution: >-
    AI tools scan documents and emails for indicators and surface candidates for a forensic accountant to assess.
    Practitioners describe this in trade articles and vendor white papers; no deployment is documented with outcomes.
  outcomes:
    - lever: speed
      description: >-
        A BRG managing director says a document review that took him a summer by hand early in his career would today
        be completed in a few minutes using technology and AI.
      figure: "summer vs a few minutes"
      measures: "Personal recollection in an opinion column; no sample, tool or matter named."
      provenance: self-reported
      source_ref: CPAPA-FORENSICAI-2025
    - lever: quality
      description: Over 63% of surveyed forensic professionals reported improvements in their investigative processes due to AI and data analytics.
      figure: "over 63%"
      measures: >-
        Share of survey participants reporting improvements; the extended abstract does not give the sample size and
        measures AI and analytics together.
      provenance: independent
      source_ref: FINTAF-FORENSIC-2025
  prerequisites:
    - Documents in searchable form.
    - A reviewer who can separate real patterns from noise.
  risks_and_guardrails:
    - AI-flagged anomalies may be errors, so false positives can derail an investigation (CPAPA-FORENSICAI-2025).
    - Over-reliance risks missing context; AI trained on past fraud may not detect schemes built to evade it (CPAPA-FORENSICAI-2025).
    - Respondents cite cost, data security and inadequate training as barriers (FINTAF-FORENSIC-2025).
  human_checkpoints:
    - A forensic accountant explains the results to courts and regulators; the author says AI cannot take an oath or withstand cross-examination (CPAPA-FORENSICAI-2025).
  role_evolution: >-
    The BRG author argues AI changes the type of work forensic accountants do but not the role (CPAPA-FORENSICAI-2025).
  evidence_grade: C
  sources:
    - { ref: CPAPA-FORENSICAI-2025, title: "Forensic Accounting in the Age of AI: Opportunities and Risks", publisher: CPA Practice Advisor (author: Frank Dery, BRG), type: press, url: "https://www.cpapracticeadvisor.com/2025/10/15/forensic-accounting-in-the-age-of-ai-opportunities-and-risks-2/170853/", date: 2025-10-15, access: full, locator: "opening paragraphs; opportunities and risks lists" }
    - { ref: FINTAF-FORENSIC-2025, title: "Impact of Emerging Technologies on Forensic Accounting Investigations (extended abstract)", publisher: "FinTech and Artificial Intelligence in Finance, Sheffield Hallam University", type: academic, url: "https://journals.shu.ac.uk/index.php/FinTAF/article/download/449/177/1773", date: 2025-03-07, access: full, locator: "findings paragraphs" }
    - { ref: VALID8-WP-2025, title: "The Impact of AI on Fraud Investigations: What Forensic Accountants Need to Know", publisher: Valid8 Financial, type: vendor, url: "https://valid8financial.com/white-paper/ai-impact-on-fraud-investigations", date: 2025-02, access: full, locator: "Chee interview section" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: the source gives only the author's title at BRG, not the firm's size or type; the other sources
    are academic and vendor. Graded C: the BRG statement is an opinion-column
    recollection without a described deployment. The Valid8 white paper (a vendor) also has an estimate that 60% of
    forensic accounting companies use AI-powered tools; that is an unsourced vendor estimate and is not used as an outcome.

- id: advisory-forensic-disputes-09
  title: Generative-AI drafting of investigation and expert report skeletons, narratives and visualisations
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: >-
    Reports, exhibits and client emails take a large part of the time of experienced staff.
  solution: >-
    Generative AI produces a first outline or narrative, summaries of deposition transcripts and draft charts, which the
    expert edits and owns. Dean Dorton's training deck demonstrates this with Copilot; the AICPA FVS 2026 conference
    has a session on AI in visualisation design.
  outcomes:
    - lever: capacity
      description: >-
        Among the 16% of respondents whose organisations use generative AI as an anti-fraud tool, report writing is a top
        application at 45% (phishing and scam detection 49%, risk identification 46%).
      figure: "45% of the 16% using genAI"
      measures: >-
        Share of respondents whose organisation currently uses generative AI as an anti-fraud tool (16% of 713
        respondents) that name report writing as an application.
      provenance: vendor-published
      source_ref: ACFE-TECHBENCH-2026
  prerequisites:
    - Enterprise tools with confidentiality terms (KTS-EXPERTAI-2026).
    - The expert verifies every fact, calculation and citation independently (KTS-EXPERTAI-2026).
  risks_and_guardrails:
    - Fabricated citations in AI-drafted declarations led to exclusion in Kohls v. Ellison (KTS-EXPERTAI-2026).
    - Dean Dorton's deck lists confidentiality, bias and human oversight as the risks and limits (DEANDORTON-AIEXPERT-2025).
  human_checkpoints:
    - The expert authors every opinion and conclusion (KTS-EXPERTAI-2026).
  role_evolution: >-
    A Dean Dorton presenter frames AI as a complement to human expertise (DEANDORTON-AIEXPERT-2025).
  evidence_grade: C
  sources:
    - { ref: ACFE-TECHBENCH-2026, title: "Study: Deepfake fraud surges - and only 7% of organizations are firmly ready (2026 Anti-Fraud Technology Benchmarking Report press release)", publisher: SAS with ACFE, type: survey, url: "https://www.sas.com/en_us/news/press-releases/2026/march/acfe-anti-fraud-technology-study-deepfakes.html", date: 2026-03-25, access: full, locator: "bullet beginning 'GenAI is moving from aspiration to application'" }
    - { ref: DEANDORTON-AIEXPERT-2025, title: "AI in the Expert Witness Toolbox: Enhancing Forensic Accounting & Valuation Testimony (training deck by Josh Shilts)", publisher: Dean Dorton, type: firm, url: "https://deandorton.com/wp-content/uploads/2025/09/AI-Expert-Witness-Toolbox-Dean-Dorton.pdf", date: 2025-09, access: full, locator: "slides 4-7 (practical applications; demo scenarios; risks)" }
    - { ref: AICPA-FVS-2026, title: "AICPA Forensic & Valuation Services Conference 2026 agenda (FVC2604)", publisher: AICPA & CIMA, type: conference, url: "https://tools.eventpower.com/agenda_module/schedule/display/26AICPA-FVC?agenda_id=2652&key=aab743&header=0", date: 2026-11-04, access: full, locator: "FVC2604, Wed Nov 4, 2:10-3:00 pm (scheduled)" }
    - { ref: KTS-EXPERTAI-2026, title: "Expert Engagement Agreements in the Age of Generative AI", publisher: Kilpatrick Townsend, type: firm, url: "https://ktslaw.com/insights/alert/2026/8/expert-engagement-agreements-in-the-age-of-generative-ai", date: 2026-08-31, access: full, locator: "case summaries" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: mid-market regional CPA and advisory firm (Dean Dorton; the source does not give its size) and a survey
    of anti-fraud professionals. The Dean Dorton deck is a training demonstration, not evidence of deployment, and its
    date is inferred from the file path (2025/09). The conference session is scheduled, not yet given, and cannot support
    the grade. The ACFE figure concerns corporate anti-fraud teams, not expert reports, and is adjacent. A forensic
    director at Crowe MacKay says in a vendor white paper that AI can create a report skeleton, scan thousands of
    emails and take notes from recordings (VALID8-WP-2025); descriptive only.

- id: advisory-forensic-disputes-10
  title: Preserving and collecting employees' generative-AI chats and prompts as evidence
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [data-reporting]
  pattern: bulk-transformation
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Employees' prompts and AI outputs may hold evidence, but they sit in tools that legal-hold and collection
    processes were not built for.
  solution: >-
    Relativity says its platform can collect from Claude Enterprise, ChatGPT Enterprise, Gemini, Microsoft 365,
    Google Workspace, Slack and more, and preserve in place; this makes enterprise AI chat data collectable alongside email
    and chat.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: "No customer use or measurement is published."
      provenance: vendor-published
      source_ref: RELATIVITY-AIR-2026
  prerequisites:
    - Enterprise (not consumer) AI accounts with administrative access to logs.
    - A legal-hold process that names AI tools as data sources.
  risks_and_guardrails:
    - Data in AI tools may be privileged or protected; protective-order terms may restrict where it can go (KTS-EXPERTAI-2026).
  human_checkpoints:
    - Counsel decides scope of preservation and collection.
  role_evolution: >-
    No source describes role changes.
  evidence_grade: C
  sources:
    - { ref: RELATIVITY-AIR-2026, title: "Relativity aiR (product page)", publisher: Relativity, type: vendor, url: "https://www.relativity.com/data-solutions/air/", date: 2026-10-20, access: full, locator: "Collect and Legal Hold sections" }
    - { ref: KTS-EXPERTAI-2026, title: "Expert Engagement Agreements in the Age of Generative AI", publisher: Kilpatrick Townsend, type: firm, url: "https://ktslaw.com/insights/alert/2026/8/expert-engagement-agreements-in-the-age-of-generative-ai", date: 2026-08-31, access: full, locator: "confidentiality and 502(d) paragraphs" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: vendor. Product capability claim only; no named deployment. Listed because it is a concrete frontier
    signal that AI-tool data is becoming an evidence source.

- id: advisory-forensic-disputes-11
  title: "Idea: forensic detection and examination of AI-generated or altered evidence (deepfaked audio and video, forged documents)"
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: intake-triage
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Judges worry about hyperrealistic fake evidence, and fraudsters use AI to forge documents and impersonate people.
  solution: >-
    A forensic team examines challenged items for provenance, access and alteration and looks for corroboration, as
    judges are advised to ask. No firm publicly sells or reports such a service in accounting-firm forensic practice;
    this is the discussed need, not a found deployment.
  outcomes:
    - lever: risk
      description: >-
        15 of 931 responding federal judges reported encountering a deepfake challenge; 98% had not. Most respondents
        favoured a rule on deepfakes.
      figure: "15 of 931 judges (about 2%)"
      measures: >-
        Count of judges, among 931 respondents (45% response rate) to the Federal Judicial Center's January 2026 survey of
        federal judges, who said they had encountered a litigant challenge that evidence was a deepfake.
      provenance: independent
      source_ref: USCOURTS-EVAGENDA-2026
    - lever: risk
      description: 77% of anti-fraud respondents report a slight-to-significant increase in deepfake social engineering over two years; 75% in generative-AI document fraud and forgery.
      figure: "77% and 75%"
      measures: >-
        Share of 713 ACFE/SAS respondents reporting a slight-to-significant increase over the past two years in each modality.
      provenance: vendor-published
      source_ref: ACFE-TECHBENCH-2026
  prerequisites:
    - Chain-of-custody and metadata practices for the original item.
    - Access to specialist deepfake analysis (not found in public sources for accounting firms).
  risks_and_guardrails:
    - A California court dismissed a case on 2025-09-09 as a terminating sanction after plaintiffs submitted AI-generated evidence; reconsideration was denied 2025-11-06 (NBC-DEEPFAKE-2025).
    - The judiciary's committee prepared but did not approve a possible Rule 901(c) on deepfakes (USCOURTS-EVAGENDA-2026, Tab IV summary, p. 5).
  human_checkpoints:
    - Judges are advised to ask the source of a suspect item, who had access, whether it was altered, and for corroborating evidence (NBC-DEEPFAKE-2025).
  role_evolution: >-
    Not published for forensic accountants.
  evidence_grade: D
  sources:
    - { ref: USCOURTS-EVAGENDA-2026, title: "Advisory Committee on Evidence Rules, agenda book for the May 7, 2026 meeting", publisher: US federal judiciary, type: regulator, url: "https://www.uscourts.gov/sites/default/files/document/2026-05_evidence_rules_agenda_book.pdf", date: 2026-05-07, access: full, locator: "p. 5 (Tab IV summary); FJC survey memo pp. 226-227" }
    - { ref: NBC-DEEPFAKE-2025, title: "AI-generated evidence showing up in court alarms judges", publisher: NBC News, type: press, url: "https://www.nbcnews.com/tech/tech-news/ai-generated-evidence-deepfake-use-law-judges-object-rcna235976", date: 2025-11-18, access: full, locator: "Mendones case and judges' comments" }
    - { ref: ACFE-TECHBENCH-2026, title: "Study: Deepfake fraud surges - and only 7% of organizations are firmly ready", publisher: SAS with ACFE, type: survey, url: "https://www.sas.com/en_us/news/press-releases/2026/march/acfe-anti-fraud-technology-study-deepfakes.html", date: 2026-03-25, access: full, locator: "'Fraudsters are winning the AI race' bullet" }
    - { ref: FINCEN-DEEPFAKE-2024, title: "FinCEN Alert FIN-2024-Alert004: Fraud Schemes Involving Deepfake Media Targeting Financial Institutions", publisher: US Treasury FinCEN, type: regulator, url: "https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf", date: 2024-11-13, access: full, locator: "pp. 1-2" }
  last_reviewed: 2026-10-20
  notes: >-
    IDEA, labelled as such. Practitioners and judges discuss the need; no accounting-firm deployment found. The incident
    evidence is thin (about 2% of judges; one widely reported sanction case, Mendones v. Cushman and Wakefield,
    Alameda County Superior Court, as reported by NBC News). The AICPA 2025 FVS conference reportedly had a deepfake
    session (snippet-only, not opened in this run). The FinCEN alert is older than the 18-month window; it is a
    foundation source about deepfake fraud against financial institutions.

- id: advisory-forensic-disputes-12
  title: "Idea: investigation services for AI-fuelled fraud and AI-washing claims"
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: end-to-end-case-agent
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Clients expect more AI-enabled fraud (synthetic identities, AI voices, forged documents) and claims that overstate a
    company's AI capabilities, and few feel prepared.
  solution: >-
    Forensic accountants investigate AI-enabled schemes and test AI claims made to investors or customers. The topic
    appears in conference programmes, but no firm reports delivering the service.
  outcomes:
    - lever: growth
      description: none published
      figure: none published
      measures: "No outcomes published; demand signals only (see notes)."
      provenance: independent
      source_ref: ACFE-TECHBENCH-2026
  prerequisites:
    - Skills in AI systems, data forensics and investigation interviews.
  risks_and_guardrails:
    - Only 7% of respondents say their organisations are more than moderately prepared to detect or prevent AI-fuelled fraud (ACFE-TECHBENCH-2026).
  human_checkpoints:
    - Investigators decide scope, interview and report findings.
  role_evolution: >-
    A scheduled AICPA FVS session targets CPAs who want to position themselves as experts in AI-enabled elder fraud (AICPA-FVS-2026, FVC2621).
  evidence_grade: D
  sources:
    - { ref: ACFE-TECHBENCH-2026, title: "Study: Deepfake fraud surges - and only 7% of organizations are firmly ready", publisher: SAS with ACFE, type: survey, url: "https://www.sas.com/en_us/news/press-releases/2026/march/acfe-anti-fraud-technology-study-deepfakes.html", date: 2026-03-25, access: full, locator: "opening paragraph" }
    - { ref: ACFE-APAC-2026, title: "2026 ACFE Fraud Conference Asia-Pacific sessions", publisher: ACFE, type: conference, url: "https://www.fraudconference.com/asiapac2026/sessions.aspx", date: 2026-08-18, access: full, locator: "session 2B, 'How to Uncover Artificial Intelligence Washing' (title only)" }
    - { ref: ACFE-CANADA-2026, title: "2026 ACFE Fraud Conference Canada sessions", publisher: ACFE, type: conference, url: "https://www.fraudconference.com/canada2026/sessions.aspx", date: 2026-11-15, access: full, locator: "pre-conference on ethical AI use in fraud work (Nov 15); session 4C (scheduled)" }
    - { ref: ACFE-CANPR-2026, title: "2026 ACFE Fraud Conference Canada Focuses on AI, Cybercrime, Emerging Risks and More", publisher: ACFE, type: professional-body, url: "https://www.acfe.com/about-the-acfe/newsroom-for-media/press-releases/press-release-detail?s=2026-acfe-fraud-conference-canada-pr", date: 2026-10-01, access: full, locator: "list of presentations" }
    - { ref: AICPA-FVS-2026, title: "AICPA Forensic & Valuation Services Conference 2026 agenda (FVC2621)", publisher: AICPA & CIMA, type: conference, url: "https://tools.eventpower.com/agenda_module/schedule/display/26AICPA-FVC?agenda_id=2652&key=aab743&header=0", date: 2026-11-05, access: full, locator: "FVC2621, Thu Nov 5, 1:05-1:55 pm (scheduled)" }
  last_reviewed: 2026-10-20
  notes: >-
    IDEA, labelled as such. Only session titles were available for the AI-washing session (held at the ACFE
    Asia-Pacific conference on or about 2026-08-18; the page lists it but gives no abstract). Conference items dated
    after today are scheduled, not given, and cannot support the grade. Overlaps with risk-controls.

- id: advisory-forensic-disputes-13
  title: "Idea: agentic AI for blockchain and cryptocurrency fund tracing"
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [data-reporting, research-synthesis]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Following funds through intermediary wallets to exchanges and mixers is manual and requires specialised tooling.
  solution: >-
    A scheduled AICPA FVS session on blockchain tracing says it will include discussion of agentic AI deployment in this
    space. No deployment or product is described.
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: "Session description only; no outcomes."
      provenance: self-reported
      source_ref: AICPA-FVS-2026
  prerequisites:
    - Blockchain explorers and tracing tools; foundational knowledge of public blockchains (per the session description).
  risks_and_guardrails:
    - None stated in the source.
  human_checkpoints:
    - Attendees are trained to follow on-chain flows themselves (AICPA-FVS-2026, FVC2618).
  role_evolution: >-
    Not stated.
  evidence_grade: D
  sources:
    - { ref: AICPA-FVS-2026, title: "AICPA Forensic & Valuation Services Conference 2026 agenda (FVC2618)", publisher: AICPA & CIMA, type: conference, url: "https://tools.eventpower.com/agenda_module/schedule/display/26AICPA-FVC?agenda_id=2652&key=aab743&header=0", date: 2026-11-05, access: full, locator: "FVC2618, Thu Nov 5, 11:15 am-12:05 pm (scheduled)" }
  last_reviewed: 2026-10-20
  notes: >-
    IDEA, labelled as such, and the thinnest entry here. The source is a session abstract for a talk not yet given.

- id: advisory-forensic-disputes-14
  title: "Idea: AI critique of opposing expert reports and AI-assisted cross-examination and testimony preparation"
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Experts and counsel must find flaws in opposing analyses and prepare for cross-examination under time pressure.
  solution: >-
    Use an LLM to summarise an opposing expert's report, list probing questions, or identify inconsistencies; J.S. Held
    says attorneys use AI during depositions and trials this way, and a Dean Dorton training deck demonstrates a mock
    critique with Copilot.
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: "No measurement; the claims are general statements."
      provenance: self-reported
      source_ref: JSHELD-AIEXPERT-2026
  prerequisites:
    - Confidentiality controls for opposing-party material under protective orders.
  risks_and_guardrails:
    - Do not enter confidential or protective-order material into non-closed tools (KTS-EXPERTAI-2026).
  human_checkpoints:
    - The expert reviews the output and keeps independent judgment.
  role_evolution: >-
    J.S. Held expects experts to run pre-emptive AI critical reviews of their own work and to be asked about AI use in proceedings (JSHELD-AIEXPERT-2026).
  evidence_grade: D
  sources:
    - { ref: JSHELD-AIEXPERT-2026, title: "Expertise in the Age of Algorithms: Trust and Transparency in AI-Assisted Litigation", publisher: J.S. Held, type: firm, url: "https://www.jsheld.com/insights/articles/expertise-in-the-age-of-algorithms-trust-and-transparency-in-ai-assisted-litigation", date: 2026-02-03, access: full, locator: "paragraph on AI in depositions; conclusion" }
    - { ref: DEANDORTON-AIEXPERT-2025, title: "AI in the Expert Witness Toolbox (training deck by Josh Shilts)", publisher: Dean Dorton, type: firm, url: "https://deandorton.com/wp-content/uploads/2025/09/AI-Expert-Witness-Toolbox-Dean-Dorton.pdf", date: 2025-09, access: full, locator: "slide 6, demo scenario 4" }
  last_reviewed: 2026-10-20
  notes: >-
    IDEA, labelled as such. Practitioners discuss it; no named deployment or result.

- id: advisory-forensic-disputes-15
  title: "Idea: validation studies and error-rate testing of machine-generated analyses to meet or challenge a reliability standard such as proposed Rule 707"
  archetype: advisory
  module: forensic-disputes
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    If machine output is offered without an expert, the proponent would have to show it meets Rule 702's reliability tests,
    and a black-box process may be hard to defend without independent validation.
  solution: >-
    Experts design and run validation studies (training data, error rates, independent replication) that show a tool's
    reliability for the question at hand, or test an opponent's tool. The committee's draft note says validation studies
    can show a low error rate even for an unexplainable process. Rule 707 is a proposal and may change.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: "No outcomes; the service is described as a possibility."
      provenance: independent
      source_ref: USCOURTS-EVAGENDA-2026
  prerequisites:
    - Access to the tool's training data or the ability to test it on known cases; the committee discussed whether independent researchers would have licences.
  risks_and_guardrails:
    - The rule is not adopted; the Standing Committee's September 2026 report lists only continued consideration (USCOURTS-STDCOMM-2026).
    - The Justice Department raised overall concerns about Rule 707 at the November 2025 committee meeting (USCOURTS-EVAGENDA-2026, minutes, p. 19).
  human_checkpoints:
    - The court decides admissibility under the rule.
  role_evolution: >-
    Defendants could use AI-driven forensic accounting reports if they lay a foundation as an expert would (STEPTOE-FRE707-2026).
  evidence_grade: D
  sources:
    - { ref: USCOURTS-EVAGENDA-2026, title: "Advisory Committee on Evidence Rules, agenda book for the May 7, 2026 meeting", publisher: US federal judiciary, type: regulator, url: "https://www.uscourts.gov/sites/default/files/document/2026-05_evidence_rules_agenda_book.pdf", date: 2026-05-07, access: full, locator: "p. 4 (Tab III: more than 70 written comments); pp. 65-66 (Nov 2025 report: validation studies); p. 19 (DOJ concerns)" }
    - { ref: USCOURTS-STDCOMM-2026, title: "Report of the Committee on Rules of Practice and Procedure, September 2026 (Agenda E-19, rev. 8/27/26)", publisher: US federal judiciary, type: regulator, url: "https://www.uscourts.gov/sites/default/files/document/sept_2026_rules_report_and_attachments_final.pdf", date: 2026-08-27, access: full, locator: "Evidence Rules, Information Items (after p. 25)" }
    - { ref: STEPTOE-FRE707-2026, title: "AI in the Courtroom: How Proposed Rule 707 Could Shape Evidence Standards", publisher: Steptoe, type: firm, url: "https://www.steptoe.com/en/news-publications/the-mother-court-blog/ai-in-the-courtroom-how-proposed-rule-707-could-shape-evidence-standards.html", date: 2026-01-28, access: full, locator: "paragraphs 1-5" }
    - { ref: USCOURTS-FRE707-2025, title: "Proposed Federal Rule of Evidence 707 (published draft and committee note)", publisher: "US federal judiciary (copy hosted by Steptoe)", type: regulator, url: "https://www.steptoe.com/a/web/mfVW1ZxAuBkvow2pShnt2X/proposed-rule-707.pdf", date: 2025-08, access: full, locator: "rule text; committee note" }
  last_reviewed: 2026-10-20
  notes: >-
    IDEA, labelled as such. The service itself is not described by any source; the building blocks (validation studies,
    error-rate evidence) are in the committee's discussion. Rule 707's status is stated from the judiciary's own
    September 2026 report, not from secondary summaries.
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Allegation intake and triage** (`review-assurance`): complaint or hotline tip, scoping, privilege set-up. Tips are the top detection source (43% of 2,402 cases; ACFE-RTTN-2026, Fig. 13).
- **Evidence preservation and collection** (`data-reporting`): legal hold, forensic imaging, collection from email, chat and, now, enterprise AI tools (RELATIVITY-AIR-2026).
- **Data preparation** (`data-reporting`): turning statements, checks and ledgers into structured data. J.S. Held says this once took as much as 50% of project budgets (JSHELD-AIFRAUD-2026, p. 6). Use cases 01 and 02.
- **Forensic analytics and tracing** (`data-reporting`): matching, anomaly tests, fund tracing, lifestyle and bank-deposit analysis. Use cases 02, 03, 13.
- **Document and email review** (`research-synthesis`, `review-assurance`): first-pass review, issue coding, privilege. Use cases 04, 05, 08.
- **Interviews and fact-finding** (`client-interaction`, `expert-judgment`): no public AI use case found.
- **Damages and loss quantification** (`expert-judgment`, `data-reporting`): the Weber and J.S. Held cases sit here.
- **Report, exhibits and testimony** (`document-production`, `expert-judgment`): drafting, visualisation, rebuttal, deposition and trial testimony. Use cases 07, 09, 14, 15.
- **Disclosure, evidence admissibility and sanctions risk** (`review-assurance`): new governance step. Use cases 07, 11, 15.

### Pain points

- Data preparation before analysis starts; poor-quality scans and incomplete bank data (JSHELD-AIFRAUD-2026, pp. 5-7).
- High first-level review costs; inconsistent human reviewers (CGP-ARXIV-2026, section 4: SME and first-level reviewers disagree materially).
- Uncertainty about what a court will accept from AI-assisted analysis; no bright-line rule on AI in expert opinions (AICPA-COPILOT-2025).
- Fraud risk is rising faster than defences: 7% say they are more than moderately prepared for AI-fuelled fraud (ACFE-TECHBENCH-2026).

### Metrics and benchmarks (with sources)

- **ACFE Occupational Fraud 2026** (published 2026-05-12): 2,402 cases, 143 countries; tips detected 43%; automated transaction/data monitoring was the initial detection method in 3%; proactive data monitoring/analysis in place in 49% of cases with median loss $70,000 vs $150,000 and 9 vs 16 months (ACFE-RTTN-2026, Fig. 13, p. 41). Not AI-specific.
- **ACFE/SAS 2026 benchmarking** (2026-03-25, n=713): AI/ML used by 25% (18% in 2024); genAI used by 16%, 58% plan to; 18% test models for bias; 6% fully confident explaining models; 84% cite budget as a major or moderate barrier (ACFE-TECHBENCH-2026).
- **e-Discovery gen-AI review:** 87.7% recall / 28.6% precision (aiR) vs 64.4% / 39.2% (managed review) on a 1,000-document SME sample; independent critique says not comparable (CGP-ARXIV-2026).
- **FJC survey of federal judges** (January 2026): 931 responses, 45% response rate; 15 had met a deepfake challenge (USCOURTS-EVAGENDA-2026, pp. 226-227).
- **Rule 707 comment record:** more than 70 written comments and two hearings (USCOURTS-EVAGENDA-2026, p. 4).
- **Literature:** 76 documents (2019-2026) in a systematic review; ML tends to beat rule-based methods where data quality is high (JRFM-FORENSICAI-2026). For OSINT and cyber investigations, end-to-end hallucination was measured empirically in only one system (4%, favourable and non-reproducible conditions) (OSINT-ARXIV-2026, Abstract and section on the hallucination-validation gap).
- **Quality evidence for accounting-firm forensic AI:** none. No error rate, override rate, parallel-run result or inspection finding was found. The closest is J.S. Held's description of a parallel check (no results).

### Guardrails and regulatory points

- **Proposed Rule 707** would subject machine output offered without an expert to Rule 702(a)-(d) reliability, excluding "simple scientific instruments" (USCOURTS-FRE707-2025). Published for comment August 2025; committee met 2026-05-07; the Standing Committee's September 2026 report lists "continued consideration" (USCOURTS-STDCOMM-2026). The committee had also prepared, but not approved, a possible Rule 901(c) on deepfakes (USCOURTS-EVAGENDA-2026, p. 5). Draft note changes discussed include explainability and independent validation (USCOURTS-EVAGENDA-2026, pp. 18-19 and 65-66).
- **Existing law already bites:** Rule 702 and Daubert in Kohls v. Ellison; Frye in Matter of Weber; counsel's duty to disclose AI evidence in Weber (KTS-EXPERTAI-2026).
- **Professional guidance:** AICPA FVS committee guidelines (Oct 2025, members-only, not a standard) (BVR-AICPAAIGUIDE-2025); AICPA FVS conference sessions on court treatment of AI expert evidence are scheduled for 2026-11-05 (AICPA-FVS-2026, FVC2617).
- **UK:** The Civil Justice Council proposed that expert witnesses explain AI use and that the expert declaration (PD35 3.3) be amended; a July 2026 update points to proportionate transparency for expert evidence and a final report later in 2026 (HSFKRAMER-CJC-2026, search-only, law-firm summary; not verified against CJC documents).
- **Enforcement context:** DOJ's September 2024 compliance guidance asks prosecutors to look at how a company manages AI risk and whether human decision-making is the baseline for assessing AI (DOJ-ECCP-2024, AI sections). FinCEN's November 2024 alert gives deepfake red flags for financial institutions (FINCEN-DEEPFAKE-2024).
- **Independence:** J.S. Held states it is not a CPA firm and provides no attest services (JSHELD-AIEXPERT-2026, footer). For CPA firms, expert-witness and litigation-support work for audit clients is likely restricted; not verified here. Route to the independence and pricing research.

### Discourse signals (what practitioners are saying)

- **Where the field says it is heading:** AI will become a common part of every expert's practice, and opposing experts will use AI to find flaws, so experts should run pre-emptive AI reviews of their own work (JSHELD-AIEXPERT-2026). Practitioners expect to be asked about AI use in proceedings (JSHELD-AIEXPERT-2026).
- **Conference programming (all scheduled sessions are signals only):** the AICPA FVS Conference (2026-11-04 to 11-06) has a topic track "AI, technology and advanced data" and sessions on how courts respond to AI-assisted expert evidence (FVC2617), explaining AI-enabled procedures to a trier of fact (FVC2627) and AI use in expert testimony ethics (FVC2638); a 2025 FVS session on experts' use of AI and court opinions is sold as a rebroadcast webcast (AICPA-FVS-2026; AICPA-FVSWEBCAST-2025). ACFE conferences in Asia-Pacific (August) and Canada (November) list AI-washing and ethical-AI sessions (ACFE-APAC-2026; ACFE-CANADA-2026). No recordings or slides were reachable.
- **Podcasts:** ACFE's Fraud Talk episode 162 (2025-11-11) discusses AI in fraud detection and the need for human intuition alongside automation, per the show notes; the audio was not heard (FRAUDTALK-162-2025).
- **Academic agenda:** the Journal of Forensic Accounting Research issued a call for a special topic on forensic accounting and AI, with submissions due 2026-03-15 (JFAR-CFP-2024). A 2026 systematic review says evidentiary validity of algorithmic results, interpretability, data quality and professional resistance remain open (JRFM-FORENSICAI-2026). An OSINT and cyber-investigation survey says hallucination is flagged as a major concern in over 20 studies but measured end to end in one (OSINT-ARXIV-2026).
- **Vendor-led discourse on review quality:** vendors cite recall of 85-95% for gen-AI review (HAYSTACKID-GENAI-2026) while independent authors dispute a flagship comparison (CGP-ARXIV-2026). A 2024 Relativity and Redgrave Data preprint reported an estimated 96% recall and 60% precision on a live matter and is the earlier vendor-affiliated claim (OMRANI-BEYONDBAR-2024).

### Frontier signals (dated and sourced)

- **2025-09-09:** Alameda County court dismisses a case as a terminating sanction over a deepfake exhibit; reconsideration denied 2025-11-06 (NBC-DEEPFAKE-2025).
- **2025-10 and 2026-02-25:** AICPA FVS committee guidelines on AI use in forensic and valuation engagements; BVR notes the Kohls exclusion for valuation experts (BVR-AICPAAIGUIDE-2025; BVR-KOHLS-2026).
- **2026-01 (survey Jan 15-30):** FJC survey on deepfakes; **2026-05-07** committee meeting; **2026-08-27** Standing Committee report (USCOURTS-EVAGENDA-2026; USCOURTS-STDCOMM-2026).
- **2026-03-25:** ACFE/SAS report: 58% plan to use genAI in anti-fraud work (ACFE-TECHBENCH-2026).
- **2026-05-21:** J.S. Held case studies on AI-assisted tracing (JSHELD-AIFRAUD-2026).
- **2026-08-31:** Law-firm guidance to rewrite expert engagement agreements for AI (KTS-EXPERTAI-2026).
- **2026-10-12:** Independent re-analysis of the first public head-to-head of gen-AI review against managed review (CGP-ARXIV-2026).
- **Scheduled, not yet given:** AICPA FVS Conference 2026-11-04 to 11-06, AI-related sessions FVC2617, FVC2618, FVC2621, FVC2627, FVC2638, FVC2640 (valuation) (AICPA-FVS-2026); ACFE Fraud Conference Canada 2026-11-15 to 11-17 with an ethical-AI pre-conference (ACFE-CANADA-2026).

### Workforce and role effects

- The headline claim is that AI changes the work, not the role; the BRG author says it cannot replace judgment or testimony (CPAPA-FORENSICAI-2025). J.S. Held says professionals will spend more time analysing and less time processing (JSHELD-AIFRAUD-2026, p. 6).
- The first-level review layer is the explicit comparison target in e-discovery (CGP-ARXIV-2026, section 1).
- Experts take on new duties: disclosure, verification logs, and being ready to be asked about AI use (JSHELD-AIEXPERT-2026; KTS-EXPERTAI-2026).
- AI labs are recruiting forensic accountants as trainers and graders (damages calculations, asset tracing, expert report writing), at $75-$150 an hour, posted 2026-08-14 (AFTERQUERY-JOB-2026). This is a market signal about expertise demand, not a firm's use.
- Junior pipeline: no forensic-specific source found; the wider advisory landscape flags the issue (landscape file, cross-cutting thread 4).

### Objections and concerns practitioners raise

- Black-box methods and lack of repeatability make cross-examination hard (JSHELD-AIEXPERT-2026).
- Hallucinated citations and numbers (Kohls; Weber) (KTS-EXPERTAI-2026).
- False positives and over-reliance; fraudsters adapt to algorithms (CPAPA-FORENSICAI-2025).
- Cost, data security and training gaps (FINTAF-FORENSIC-2025).
- Confidentiality and protective orders; consumer tools banned in model engagement clauses (KTS-EXPERTAI-2026).
- Doubt that vendor comparisons are fair: ground truth differs by reviewer and tool trade-offs differ (CGP-ARXIV-2026).
- Government concern that a broad Rule 707 would disadvantage proprietary government software (USCOURTS-EVAGENDA-2026, minutes, p. 19).

### Interview probes for an advisor

1. When an expert or analyst on your team uses a generative-AI or analytics tool, what record do you keep (prompt, version, verification), and could you reproduce it at a deposition? Has counsel or an opposing expert asked about AI use yet?
2. For data preparation and tracing work, which part of project hours has moved, how do you validate extraction (balance checks, sample re-performance), and what error or exception rates do you track?
3. What do you refuse to let AI do in an opinion, and do your engagement letters disclose AI use or let clients opt out?
4. If first-pass document review and data prep shrink, how do you train juniors, and how does that change how you staff and price?
5. If a client or court challenged an audio, video or document as fabricated, what is your protocol, and is it a billed service?

---

## 4. Routed to other modules

- **valuation:** IVSC exposure draft on AI disclosure in valuation scope and reports (already in the landscape); Valuation Performance Framework; AICPA FVS session FVC2640 "Valuation in an AI World" and "MythBusters" myth 40 (AI disclosure language in business valuation reports is not easy to draft) and myth 41 (public-company AI disclosure suits) (AICPA-FVS-2026, FVC2631, FVC2640, scheduled); BVR report quality-control agents.
- **risk-controls:** DOJ ECCP AI risk questions (DOJ-ECCP-2024); FinCEN deepfake alert (FINCEN-DEEPFAKE-2024); ACFE/SAS governance gaps (18% bias testing, 6% explainability confidence) and the ACFE Canada session on AI and data analytics for ethics and compliance programs (ACFE-TECHBENCH-2026; ACFE-CANADA-2026, session 4C); fraud-risk program design behind use case 03.
- **professional-services (firm operations and quality):** Deloitte Australia's AU$440,000 government review that carried AI-fabricated citations; Deloitte confirmed use of Azure OpenAI GPT-4o in drafting, issued a corrected report with an AI disclosure, and agreed to repay the final instalment (CITYAM-DELOITTE-2025). Relevant to quality control and liability for AI-assisted advisory deliverables, not to forensic work specifically.
- **professional-services (independence, PE structures, pricing):** whether forensic and expert-witness work is available to a firm's own audit clients; how AI changes pricing of tracing and review work; the engagement-letter opt-out approach as a pricing and consent matter.
- **assurance:** AI-in-audit guidance (FRC, AICPA practice aid) is not covered here.

---

## 5. Sources

Access is `full` unless marked. Dates marked "inferred" are explained in the notes of the use case that uses them.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| USCOURTS-STDCOMM-2026 | Report of the Committee on Rules of Practice and Procedure, Sept 2026 (Agenda E-19, rev. 8/27/26) | US federal judiciary | regulator | https://www.uscourts.gov/sites/default/files/document/sept_2026_rules_report_and_attachments_final.pdf | 2026-08-27 | full |
| USCOURTS-EVAGENDA-2026 | Advisory Committee on Evidence Rules agenda book, May 7, 2026 meeting (includes Nov 2025 minutes and FJC deepfake survey) | US federal judiciary | regulator | https://www.uscourts.gov/sites/default/files/document/2026-05_evidence_rules_agenda_book.pdf | 2026-05-07 | full |
| USCOURTS-FRE707-2025 | Proposed FRE 707 published draft and committee note (copy hosted by Steptoe) | US federal judiciary | regulator | https://www.steptoe.com/a/web/mfVW1ZxAuBkvow2pShnt2X/proposed-rule-707.pdf | 2025-08 | full |
| STEPTOE-FRE707-2026 | AI in the Courtroom: How Proposed Rule 707 Could Shape Evidence Standards | Steptoe | firm | https://www.steptoe.com/en/news-publications/the-mother-court-blog/ai-in-the-courtroom-how-proposed-rule-707-could-shape-evidence-standards.html | 2026-01-28 | full (via mirror) |
| ACFE-TECHBENCH-2026 | Study: Deepfake fraud surges, and only 7% of organizations are firmly ready (2026 Anti-Fraud Technology Benchmarking Report release) | SAS with ACFE | survey | https://www.sas.com/en_us/news/press-releases/2026/march/acfe-anti-fraud-technology-study-deepfakes.html | 2026-03-25 | full (via mirror) |
| ACFE-RTTN-2026 | Occupational Fraud 2026: A Report to the Nations (English copy hosted by ACFE Mexico) | ACFE | professional-body | https://www.acfe-mexico.com.mx/inicio/sitepad-data/uploads/2026/07/Reporte-a-las-Naciones-2026.pdf | 2026-05-12 (release date per ACFE press list) | full |
| ACFE-CANADA-2026 | 2026 ACFE Fraud Conference Canada sessions | ACFE | conference | https://www.fraudconference.com/canada2026/sessions.aspx | 2026-11-15 (event start; scheduled) | full |
| ACFE-APAC-2026 | 2026 ACFE Fraud Conference Asia-Pacific sessions | ACFE | conference | https://www.fraudconference.com/asiapac2026/sessions.aspx | 2026-08-18 | full |
| ACFE-CANPR-2026 | 2026 ACFE Fraud Conference Canada Focuses on AI, Cybercrime, Emerging Risks and More | ACFE | professional-body | https://www.acfe.com/about-the-acfe/newsroom-for-media/press-releases/press-release-detail?s=2026-acfe-fraud-conference-canada-pr | 2026-10-01 | full |
| AICPA-FVS-2026 | AICPA Forensic & Valuation Services Conference 2026 agenda (embedded agenda feed) | AICPA & CIMA | conference | https://tools.eventpower.com/agenda_module/schedule/display/26AICPA-FVC?agenda_id=2652&key=aab743&header=0 | 2026-11-04 (event; scheduled) | full |
| AICPA-FVSWEBCAST-2025 | AI Right Now for Forensic Accounting Professionals (rebroadcast of a 2025 FVS conference session; speakers from CBIZ and others) | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/cpe-learning/webcast/ai-right-now-for-forensic-accounting-professionals | 2025 (year only; the page gives no date) | full (description only; recording not viewed) |
| AICPA-COPILOT-2025 | Expert witness used Copilot to cross-check calculations, irking judge | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/news/article/expert-witness-used-copilot-to-cross-check-calculations-irking-judge | 2025-04-16 | full |
| BVR-AICPAAIGUIDE-2025 | AICPA issues AI usage guidelines for valuation and forensic work | BVWire | professional-body | https://www.bvresources.com/articles/bvwire/aicpa-issues-ai-usage-guidelines-for-valuation-and-forensic-work | 2025-10-15 | full (via mirror) |
| BVR-KOHLS-2026 | Court excludes AI-tainted expert testimony | BVWire | press | https://www.bvresources.com/articles/bvwire/court-excludes-ai-tainted-expert-testimony | 2026-02-25 | full (via mirror) |
| PPC-KOHLS-2025 | Minnesota court rejects expert testimony tainted by AI-generated citations | PPC Land | press | https://ppc.land/minnesota-court-rejects-expert-testimony-tainted-by-ai-generated-citations/ | 2025-01-26 | full |
| KTS-EXPERTAI-2026 | Expert Engagement Agreements in the Age of Generative AI | Kilpatrick Townsend | firm | https://ktslaw.com/insights/alert/2026/8/expert-engagement-agreements-in-the-age-of-generative-ai | 2026-08-31 | full |
| JSHELD-AIFRAUD-2026 | AI Fraud Detection and Forensic Accounting: Embracing Innovation to Combat Financial Threats (Third Edition) | J.S. Held | firm | https://www.jsheld.com/uploads/AI-Fraud-Detection-and-Forensic-Accounting-Embracing-Innovation-to-Combat-Financial-Threats_FINAL.pdf | 2026-05-21 (PDF publication metadata) | full (via mirror) |
| JSHELD-AIEXPERT-2026 | Expertise in the Age of Algorithms: Trust and Transparency in AI-Assisted Litigation | J.S. Held | firm | https://www.jsheld.com/insights/articles/expertise-in-the-age-of-algorithms-trust-and-transparency-in-ai-assisted-litigation | 2026-02-03 | full (via mirror) |
| CPAPA-FORENSICAI-2025 | Forensic Accounting in the Age of AI: Opportunities and Risks (author Frank Dery, BRG) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/10/15/forensic-accounting-in-the-age-of-ai-opportunities-and-risks-2/170853/ | 2025-10-15 | full |
| DEANDORTON-AIEXPERT-2025 | AI in the Expert Witness Toolbox (training deck, Josh Shilts) | Dean Dorton | firm | https://deandorton.com/wp-content/uploads/2025/09/AI-Expert-Witness-Toolbox-Dean-Dorton.pdf | 2025-09 (inferred from file path) | full |
| VALID8-WP-2025 | The Impact of AI on Fraud Investigations: What Forensic Accountants Need to Know | Valid8 Financial | vendor | https://valid8financial.com/white-paper/ai-impact-on-fraud-investigations | 2025-02 (inferred) | full |
| VALID8-SITE-2026 | Verified Financial Intelligence and Forensic Accounting Software (home page) | Valid8 Financial | vendor | https://www.valid8financial.com/ | 2026-10-08 (site last-published stamp) | full |
| VALID8-HUB-2026 | Valid8 Financial profile page (customer and testimonial claims) | NYSSCPA Resource Hub (vendor content) | vendor | https://hub.nysscpa.org/company/valid8-financial | 2026-10-20 (access date; undated) | full |
| RELATIVITY-AIR-2026 | Relativity aiR (product page) | Relativity | vendor | https://www.relativity.com/data-solutions/air/ | 2026-10-20 (access date; undated) | full |
| CGP-ARXIV-2026 | Comparing GenAI to Machine Learning and Manual Review for eDiscovery (arXiv:2610.16925) | University of Waterloo and Elevate (Cormack, Grossman, Pickens) | academic | https://arxiv.org/abs/2610.16925 | 2026-10-12 | full |
| HAYSTACKID-GENAI-2026 | From Review to Intelligence: How Gen AI Is Transforming Discovery Strategy | HaystackID (Law.com reprint) | vendor | https://haystackid.com/wp-content/uploads/2026/01/LTN0123202670120Haystackid.pdf | 2026-01-22 | full |
| EVERLAW-GENAI-2024 | GenAI Document Review Surpasses Human Performance on Real World Litigation Data | Everlaw | vendor | https://www.everlaw.com/blog/ai-and-automation/genai-document-review-surpasses-human-performance-on-real-world-litigation | 2024-09-19 | full |
| OMRANI-BEYONDBAR-2024 | Beyond the Bar: Generative AI as a Transformative Component in Legal Document Review (preprint) | Relativity and Redgrave Data | academic | https://resources.relativity.com/rs/447-YBT-249/images/Beyond-the-Bar_preprint_2-9%20%281%29.pdf?version=0 | 2024 (year only; preprint copyright line) | full (abstract read; not used for figures) |
| JRFM-FORENSICAI-2026 | AI and Machine Learning in the Transformation of Forensic Accounting: A Systematic Literature Review | J. Risk Financial Manag. (MDPI) | academic | https://doi.org/10.3390/jrfm19070519 | 2026-07-10 | full |
| FINTAF-FORENSIC-2025 | Impact of Emerging Technologies on Forensic Accounting Investigations (extended abstract) | FinTAF, Sheffield Hallam University | academic | https://journals.shu.ac.uk/index.php/FinTAF/article/download/449/177/1773 | 2025-03-07 | full |
| JFAR-CFP-2024 | Call for papers: Forensic Accounting and Artificial Intelligence (special topic) | Journal of Forensic Accounting Research (AAA) | academic | https://aaahq.org/portals/0/documents/calls/2024/CFP%20JFAR%20FA%20and%20AI.pdf | 2024 (year from file path; submissions due 2026-03-15) | full |
| OSINT-ARXIV-2026 | Agentic and Generative AI for OSINT and Cyber Investigations (arXiv:2607.03233) | Palmieri et al. | academic | https://arxiv.org/abs/2607.03233 | 2026-07-03 | full |
| NBC-DEEPFAKE-2025 | AI-generated evidence showing up in court alarms judges | NBC News | press | https://www.nbcnews.com/tech/tech-news/ai-generated-evidence-deepfake-use-law-judges-object-rcna235976 | 2025-11-18 | full |
| FINCEN-DEEPFAKE-2024 | FinCEN Alert FIN-2024-Alert004, Fraud Schemes Involving Deepfake Media | US Treasury FinCEN | regulator | https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf | 2024-11-13 | full |
| DOJ-ECCP-2024 | Evaluation of Corporate Compliance Programs (updated September 2024) | US DOJ Criminal Division | regulator | https://www.justice.gov/criminal/criminal-fraud/page/file/937501/dl | 2024-09 | full |
| CITYAM-DELOITTE-2025 | Deloitte refunds Australian government after AI 'made up citations' in report | City AM | press | https://www.cityam.com/?p=2367690 | 2025-10-06 | full |
| AFTERQUERY-JOB-2026 | Forensic Accounting Expert (AI training role) | AfterQuery via AlignList | job-posting | https://alignlist.com/jobs/afterquery-forensic-accountanting-expert-1772045096095 | 2026-08-14 | full |
| FRAUDTALK-162-2025 | Decoding the Future: Strategic Foresight for Fraud Examiners (Fraud Talk episode 162) | ACFE (Fraud Talk podcast) | podcast | https://acfe.podbean.com/e/decoding-the-future-strategic-foresight-for-fraud-examiners/ | 2025-11-11 | full (show notes only; audio not heard) |
| HSFKRAMER-CJC-2026 | Civil Justice Council publishes update on consultation responses on AI for preparing court documents | Herbert Smith Freehills Kramer (law-firm note) | firm | https://www.hsfkramer.com/notes/litigation/2026-07/civil-justice-council-publishes-update-on-consultation-responses-regarding-use-of-ai-for-preparing-court-documents | 2026-07 | search-only |

**Source counts by type (39 listed):** regulator 5, professional-body 5, conference 3, firm 6, vendor 6, academic 6, survey 1, press 5, podcast 1, job-posting 1, community 0. Opened in full: 38; search-only: 1 (HSFKRAMER-CJC-2026). The brief's target of 25 distinct sources across four source types is met on opened sources (10 types). Caveat: several of the opened items are event listings or vendor product pages rather than substantive documents, and the substantive evidence is concentrated in about ten of them (the three judiciary documents, ACFE-RTTN, ACFE-TECHBENCH, CGP-ARXIV, JSHELD x2, KTS, JRFM).

---

## 6. Gaps

**Not found or not reachable**

- **Quality evidence for accounting-firm forensic AI:** no published error rates, override rates, parallel-run results or inspection findings for AI in tracing, damages or investigation work. The only parallel-run mention (J.S. Held's IP practice) has no results.
- **Survey of accounting-firm forensic teams:** none found. The ACFE/SAS survey covers corporate anti-fraud programs (26% government, 23% banking); the FINTAF survey does not state its sample size.
- **Big Four and large forensic firms:** no forensic-specific AI launch or case study found for Deloitte, EY, KPMG, PwC, Kroll, FTI, Alvarez & Marsal or Stout. A&M's expert interview page (Gary Foster, October 2025) returned access denied; an FTI LegalWeek session ("Innovation in Disputes & Investigations: Three AI Case Studies", March 2026) surfaced only in search and its page could not be opened. Kroll's pages were blocked.
- **Job postings from forensic practices:** none found that show AI duties; searches of ATS boards returned only unrelated research papers. The only posting is an AI lab hiring forensic accountants.
- **Primary court opinions:** Matter of Weber and Kohls v. Ellison opinions were blocked (Cloudflare); both rest on law-firm and trade summaries. Mendones v. Cushman & Wakefield rests on NBC News reporting; the order was not read.
- **Keeling et al. (Redgrave) paper:** not opened; its figures are taken from the independent critique. The 2024 Relativity/Redgrave Data preprint is vendor-affiliated and not used for figures.
- **AICPA FVS 2026 agenda:** session titles and abstracts read; speaker names for the AI sessions were not retrievable. The AICPA FVS AI guidelines (members-only) and the 2025 AICPA FVS webcast (paid) were not read. The 2025 webcast date could not be found beyond "2025".
- **ACFE Global Fraud Conference 2026** (Boston, held 2026-07-12 to 07-17): official recap and keynotes read; no AI session titles or content retrievable.
- **BVR damages-experts AI session** ("Obligated to Use AI?", transcript dated 2026-10-01 per search) is paywalled and was not opened.
- **UK Civil Justice Council** consultation: only law-firm summaries via search (marked search-only); CJC documents not opened.
- **Community discussion:** Reddit and similar were blocked by network policy. No practitioner forum threads were reached.
- **DOJ ECCP and FinCEN** are not forensic-firm sources; used for context only.

**Under-documented topics**

- How AI is changing damages and lost-profits work (beyond the Weber and Kohls failures).
- Interview practice, privilege handling and cross-border data issues with AI in investigations.
- Pricing, staffing leverage and junior roles in forensic practices.
- Independence limits for CPA firms offering forensic and expert-witness work to audit clients: stated here as unverified general background.

**Source-quality caveats**

- J.S. Held figures are self-reported narratives with unnamed clients; Valid8 and Relativity figures are vendor claims.
- Dates inferred or year-only: VALID8-WP-2025 (2025-02 inferred), DEANDORTON-AIEXPERT-2025 (2025-09 inferred from path), AICPA-FVSWEBCAST-2025 (2025), OMRANI-BEYONDBAR-2024 (2024), JFAR-CFP-2024 (2024), RELATIVITY-AIR-2026 and VALID8-HUB-2026 (access date).
- The ACFE report PDF was read from a copy hosted by ACFE Mexico (English text); its release date comes from the ACFE press list.
- The landscape's "June 2026 sent back" claim about Rule 707 was replaced by the judiciary's own September 2026 report ("continued consideration"); the specific June action was not independently confirmed.

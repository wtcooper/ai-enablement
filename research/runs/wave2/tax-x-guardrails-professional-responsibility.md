# Tax x guardrails and professional responsibility

- **Archetype:** tax (compliance, provision, indirect tax, transfer pricing, international and Pillar Two, controversy, research and advisory, tax data and technology; firms and in-house departments).
- **Topic:** the regulators, standards and professional obligations that constrain AI in tax work, across jurisdictions.
- **Prepared:** 2026-10-17 (wave 2). All "today" statements are as of that date.
- **Method:** Primary texts were opened with `curl` (eCFR and Cornell LII for statutes and regulations, `pdftotext` for court documents, the r.jina.ai mirror for the TPB, Charlotin, CAMICO and Thomson Reuters pages). Six web searches were used for directions the landscape did not cover (insurance, Khoja, Deloitte Australia, 7216 and AI commentary, EU AI Act omnibus, the Heppner privilege ruling and similar). Items marked `search-only` were seen only as search extracts and are not relied on for firm claims.
- **Reading note:** "Existing duties apply" is the common theme of every practitioner regulator found. None of them has created a new AI-specific rule, certification form or disclosure duty. Where this file says "no X found", it means no X in the sources read, not that none exists.

---

## 1. Summary

- **Every practitioner regulator found says existing duties apply.** The IRS Office of Professional Responsibility (Alert 2026-19, 24 Jun 2026), the UK PCRT bodies (19 Jan 2026), Australia's Tax Practitioners Board (TPB(GS) 55/2026, 22 Jul 2026) and Germany's Bundessteuerberaterkammer (FAQ dated 27 Jan 2026) each apply their existing conduct rules to AI. The OPR alert does not amend Circular 230 (IRS-OPR-2026; KTS-OPR-2026). The practical consequence is that firm-level procedures, training, vendor vetting and documentation are expected now, not after future rules.
- **The OPR alert maps AI onto six Circular 230 and Code provisions.** These are due diligence (§10.22), fees (§10.27(a)), competence (§10.35), firm procedures (§10.36), written advice (§10.37) and unauthorized use or disclosure of return information (IRC §§6713 and 7216, and Circular 230 §10.51(a)(15)). Firm leaders with "principal authority" are named in §10.36, and discipline there turns on willfulness, recklessness or gross incompetence (IRS-OPR-2026; ECFR-C230-2026).
- **The fee point is contested.** OPR says billing for manual time not actually spent "may violate" §10.27 depending on facts. The AICPA says this appears not to allow value pricing and has asked the IRS for clarification; its CEO called the language non-authoritative. No IRS reply was found (IRS-OPR-2026; JOFA-FEES-2026).
- **§7216 and AI is unsettled in the sources read.** The regulation allows disclosure to another US preparer without consent only where the services "are not substantive determinations or advice affecting the tax liability", and defines a substantive determination as analysis, interpretation or application of the law. Whether an LLM provider is such a "preparer", and what consent form applies, has no IRS answer in the sources read. An ABA Tax Section panel on the question was listed for 6 Oct 2026 (ECFR-7216-2026; WINTHROP-ABA-2026).
- **Fabricated authorities have reached tax courts, an IRS expert and an IRS motion, not only taxpayers' lawyers.** Clinco (Tax Court, 9 Feb 2026) drew an admonition and no sanction. The IRS withdrew two expert rebuttal reports at trial in Riddle Aggregates (18 Mar 2026) after objections about AI-related errors. Bloomberg reports a Tax Court judge ordered a hearing over an IRS motion citing a nonexistent case (Khoja). A UK tax tribunal dealt with invented cases in Harber v HMRC (4 Dec 2023) (TAXCT-CLINCO-2026; TAXCT-RIDDLE-2026; BLOOMBERG-TAXCT-2026; FTT-HARBER-2023).
- **No sanction against a tax practitioner for AI misuse was found.** OPR itself says cases against non-lawyer tax professionals are "slowly emerging" and uses Deloitte Australia's partial refund as its example. The Tax Court has issued no sanction; its judge said it wants to "proceed gingerly" and questioned whether an AI certification rule would make sense (IRS-OPR-2026; BLOOMBERG-TAXCT-2026).
- **Insurers are asking, not yet excluding, in the accounting line.** Aon (administrator of the AICPA programme) said in April 2026 that it had seen no substantive AI claim activity at accounting firms, and that underwriters ask about AI policies and procedures. Exclusion wording reported in other lines (Verisk, Berkley) was seen only as search extracts (DIGIN-INSURERS-2026).
- **The binding human steps are the ones with a signature or a representation.** The signing preparer must be an individual with "primary responsibility for the overall substantive accuracy" of the return; practitioners must have reasonable basis for positions they sign; written advice needs reasonable factual and legal assumptions. These are where regulators locate judgment that AI cannot hold (LII-CFR-SIGN-2026; ECFR-C230-2026; IRS-OPR-2026).

---

## 2. Findings

### 2.1 United States: Circular 230 and IRS OPR Alert 2026-19

**What the alert is.**
- OPR issued Alert 2026-19, "Introductory Guidelines for Responsible AI Use in Federal Tax Practice", on 24 June 2026 through IRS Newswire (IRS-OPR-2026, header and issue number).
- It states that "virtually all professional tax firms use some form of AI", names Westlaw Edge, Bloomberg Tax and Lexis-Nexis as examples of embedded AI, and says generative AI has limitations: fabricated outputs ("hallucinations"), bias and lack of transparency (IRS-OPR-2026, opening section).
- It does not amend Circular 230 or create new rules; it applies existing ones (KTS-OPR-2026, opening paragraphs). The alert's own title says "introductory".
- The alert describes court sanctions on lawyers for fake citations as including financial sanctions "often amounting to several thousand dollars", public censure, ethics courses, default judgments, removal from representation and disciplinary referrals (IRS-OPR-2026, "Real-World Consequences of Improper AI Use").
- It says sanctions against "other types of tax professionals" are "slowly emerging" and cites Deloitte Australia's July 2025 government report, resolved by a partial fee refund (IRS-OPR-2026, same section).

**Provision-by-provision (from the alert's "Regulatory Framework" section).**

| Provision | What the alert says it means for AI | Source locator |
|---|---|---|
| §10.22 due diligence | Practitioners must verify accuracy of facts, citations and calculations produced by AI; cannot rely solely on AI | IRS-OPR-2026, item 1 |
| §10.27(a) fees | Billing manual time not spent, or double-billing AI-assisted tasks, may violate the rule "depending on the facts"; savings should be passed on openly, and AI activities disclosed "in general or specific terms as needed" | IRS-OPR-2026, item 2 |
| §10.35 competence | Practitioners must understand the law and the technology, including AI systems' mechanics, limits and risks | IRS-OPR-2026, item 3 |
| §10.36 procedures | Firms need policies covering staff training, internal rules (secure data handling, accuracy monitoring), vetting of third-party tools, and documentation of each step | IRS-OPR-2026, item 4 |
| §10.37 written advice | Cannot rely on AI projections or representations without verification; opaque logic may make reliance unreasonable; treat AI advice as a starting point | IRS-OPR-2026, item 5 |
| IRC §§6713, 7216(a); §10.51(a)(15) | Use only secure, enterprise-approved AI; willful mishandling can lead to Circular 230 discipline | IRS-OPR-2026, item 6 |

- The alert also names state AI laws (California, Colorado, Illinois, Utah) and ABA Formal Opinion 512 (29 July 2024) as other frameworks, and gives a list of ten best practices (document AI usage and verification, train staff, vet third parties, never upload sensitive data to unsecured sites, treat output as drafts) (IRS-OPR-2026, "State Law and Professional Guidance" and "Best Practices").
- The alert contains no mention of the word "consent" (checked by text search of the full bulletin), so it does not say how §7216 consent applies to AI tools.

**What the underlying rules say (primary text, eCFR).**
- §10.22(a) requires due diligence in preparing, approving and filing returns and in determining the correctness of representations to Treasury and to clients. §10.22(b) presumes due diligence where a practitioner relies on another person's work product and used reasonable care "in engaging, supervising, training, and evaluating the person" (ECFR-C230-2026, §10.22). The sources read do not say whether OPR treats AI tools or their vendors as "another person" for this presumption.
- §10.34(a)(1) bars a practitioner from willfully, recklessly or through gross incompetence signing a return containing a position that lacks reasonable basis, is unreasonable under §6694(a)(2), or reflects a willful attempt to understate liability or reckless disregard under §6694(b)(2). §10.34(d) allows good-faith reliance on client-furnished information without verification but not ignoring implications of information, and requires reasonable inquiries where it appears incorrect, inconsistent or incomplete (ECFR-C230-2026, §10.34).
- §10.35(a) requires "the appropriate level of knowledge, skill, thoroughness, and preparation"; competence may be reached "through various methods, such as consulting with experts" (ECFR-C230-2026, §10.35).
- §10.36(b) ties discipline to willfulness, recklessness or gross incompetence by the individual with principal authority over a firm's practice (as quoted in IRS-OPR-2026, item 4).

**Reaction and open issues.**
- The AICPA says the OPR fee language "implies that any efficiencies gained through AI should be directly passed on to the client" (AICPA's Eva Simpson), which it calls overly simplistic given licensing, implementation, governance and training costs (JOFA-FEES-2026, 8 Sep 2026).
- AICPA CEO Mark Koziel said the OPR language is not authoritative and could be "overstepping a little bit"; AICPA says it is working with the IRS on clarifying language and FAQs (JOFA-FEES-2026).
- No IRS clarification or revised alert was found by 17 Oct 2026.

### 2.2 United States: §7216, §6713 and client data

**Statutes.**
- §7216(a) makes it a misdemeanor for a person engaged in the business of preparing, or providing services in connection with preparing, chapter 1 income-tax returns, or paid to prepare one, to knowingly or recklessly disclose return-related information, or use it for another purpose. The fine is up to $1,000 ($100,000 in the identity-theft-related case in §6713(b)), or up to one year's imprisonment, or both (LII-USC-7216-6713, §7216(a)).
- §6713(a) imposes a civil penalty of $250 per disclosure or use, capped at $10,000 per calendar year per person (LII-USC-7216-6713, §6713(a)).
- Both sections, on their text, refer to returns of the tax "imposed by chapter 1". I did not find authority on whether the same rules reach VAT, sales and use tax or other non-chapter-1 returns.

**Regulations.**
- "Tax return preparer" in Reg. §301.7216-1(b)(2) includes anyone "in the business of providing auxiliary services in connection with the preparation of tax returns, including a person who develops software that is used to prepare or file a tax return" (ECFR-7216-2026, §301.7216-1).
- §301.7216-2(d)(1) lets a preparer disclose to another US-located preparer without consent for preparing a return or for auxiliary services, "so long as the services provided are not substantive determinations or advice affecting the tax liability reported". It defines a substantive determination as "an analysis, interpretation, or application of the law"; disclosing for substantive determinations requires §301.7216-3 consent (ECFR-7216-2026, §301.7216-2(d)(1)).
- §301.7216-3(a) requires written, knowing and voluntary consent; consent cannot be a condition of service (except for preparer-to-preparer disclosure under (a)(2)); it must name the preparer and taxpayer, state the purpose and recipient, specify the information, and be signed and dated. Consent is required before disclosure to a preparer located outside the US (ECFR-7216-2026, §301.7216-3(a)(1) to (3)).
- A Tax Adviser column (Jan 2024, before the AI wave) gives examples of substantive decisions: filing status, how income is reported, which deductions and credits are claimed, how income is allocated. It describes outsourcing to US-based service providers that make substantive decisions as requiring consent (TAXADV-7216-2024, "Inside the United States").

**What is unsettled.**
- No IRS guidance applying §7216 specifically to generative AI was found. A CPE vendor's compliance article (updated 26 Jun 2026, analysis as of April 2026) asserts that no IRS safe harbor or carve-out exists for AI platforms and that consent is the default for AI use (MYCPE-7216-2026). That is a vendor view, and it is broader than the regulatory text, which has exceptions for non-substantive and within-firm use (ECFR-7216-2026, §301.7216-2(c) and (d)).
- Commentary conflicts on the vendor-service exception; one law firm's ABA Tax Section panel notice (listed for 6 Oct 2026) frames the open question as when prompts and outputs are return information, and "whether the AI provider is merely processing information or making a substantive determination" (WINTHROP-ABA-2026).
- A Kilpatrick Townsend alert (29 Sep 2026) says pasting client data into a consumer chatbot may be protected return information even if the prompt omits the client's name, because combined figures may identify the taxpayer (KTS-OPR-2026, "Client Privacy and Tax Return Information"). That is the firm's gloss, not text of the alert.
- CAMICO (professional liability insurer for CPA firms) says for tax engagements firms must ensure compliance with §7216, which restricts use or disclosure "to third parties (including certain AI platforms)", and that written consent "may be required" in some cases (CAMICO-FAQ-2025, Q4).

**Data-security duties beyond 7216.**
- IRS Publication 4557 (Rev. 6-2024) says professional tax preparers are "financial institutions" under the Gramm-Leach-Bliley Act, so the FTC Safeguards Rule requires a written information security plan, a designated qualified individual, multi-factor authentication, risk assessment, and selection and oversight of service providers (IRS-P4557-2024, "Understand the FTC Safeguards Rule"). The publication predates this wave of AI use and does not mention AI in the passages read.

### 2.3 AICPA: SSTS, the Werfel risk framework and CART

**SSTS.**
- The AICPA Tax Executive Committee adopted revised SSTS on 18 May 2023, effective 1 January 2024, adding new standards on data protection, reliance on tools and representation before taxing authorities (AICPA-SSTS-2024, landing page).
- A Journal of Accountancy article cites SSTS Section 1.4 (Reliance on Tools): members may reasonably rely on tools but are not absolved (para 1.4.4); must exercise appropriate professional care and judgment (1.4.3); may use AI to improve understanding of a tax issue but not to supplant professional judgment (1.4.8); remain responsible for work product (1.4.7) (JOFA-CLINCO-2026, "Circular 230, SSTSs, and professional responsibility"). I could not open the SSTS PDF itself; these paragraph cites are secondary.

**Risk framework.**
- Danny Werfel, a former IRS Commissioner, published "A risk framework for AI use in tax administration and preparation" in The Tax Adviser (August 2026 issue, listed 31 Aug 2026). It includes two registers: 20 risks for tax authorities in four categories (information integrity, fairness and legitimacy, security and data, institutional capacity) and 15 risks for preparers in five layers (technical, practice, legal and regulatory, business, workforce and strategic) (AICPA-WERFEL-2026, "AI risk register for tax authorities" and "AI risk register for tax preparers").
- The preparer register names, among others: hallucinated advice, client data leakage, incorrect document extraction (examples: W-2, 1099, K-1), failure of professional judgment, misplaced authority, control dilution, malpractice exposure, "liability ambiguity" (allocation between signing preparer and AI vendor is "legally unclear"), regulatory noncompliance including unauthorized practice by unlicensed staff, lack of transparency, skill erosion, vendor dependence (AICPA-WERFEL-2026, Figure 3).
- It proposes an eight-step method (scope, applicable risks, prioritisation, governance and vendor accountability, and so on), a tiering in which Tier 1 risks must be addressed before launch, and phased deployment, for example restricting a tool to document summarisation before authorising position drafting (AICPA-WERFEL-2026, methodology sections; tiering for the authority register, 'Appendix B' as described in the main text).
- The author states the views are his own and not AICPA policy (AICPA-WERFEL-2026, closing note). The landscape records that AICPA says AI is moving too fast for lasting standards; I did not find that statement in the sources read for this file.

**CART.**
- The AICPA announced the Council on AI Risk in Tax (CART), led with Werfel, with participants from accounting, law, technology, government and academia including the National Association of Enrolled Agents and the Federation of Tax Administrators. Its stated aims are to test and refine the framework, identify further tools and guidance, and create a forum for shared learning. The Tax Adviser article is dated 23 Sep 2026 (TAXADV-CART-2026).

### 2.4 Courts: sanctions, hallucinations and expert evidence

**Clinco v. Commissioner, T.C. Memo. 2026-16 (filed 9 February 2026, Judge Holmes).**
- Counsel's briefs cited cases the court said were likely hallucinations generated by a large language model (opinion text and JOFA-CLINCO-2026, which names Cacchillo, Miller and Tefel as the three nonexistent citations of four on the signature point). Counsel did not correct the record after the IRS flagged the problem and repeated one citation in a table of authorities (JOFA-CLINCO-2026).
- The court's footnote 8 says it is "not absolutely clear from the record" whether counsel used generative AI, that "a bit of embarrassment" is enough for now, and, citing courts that have sanctioned lawyers for AI shortcuts, "Tax Court has not done so. Yet." (TAXCT-CLINCO-2026, n.8). The opinion notes the court has no Rule 11 equivalent beyond Rule 33(b), but lawyers must follow the Model Rules under Rule 201(a), including Model Rule 3.3(a)(1) on false statements of law (TAXCT-CLINCO-2026, n.7).
- Journal of Accountancy calls it the first Tax Court case to address possible AI hallucinations; the court "stopped short of formal sanctions" (JOFA-CLINCO-2026).

**Tax Court's stated direction (Judge Holmes, interviewed by Bloomberg Tax, 20 Mar 2026).**
- Over three-quarters of the court's cases are pro se; he has seen fewer than a dozen instances of hallucinated cases and has issued no sanctions; IRC §6673 (penalties up to $25,000 for frivolous or groundless positions) is the most prominent existing tool; the rules committee "might" require a certification that AI was not used but he is "not sure that would make any sense" (BLOOMBERG-TAXCT-2026).
- He also flagged confidentiality: Social Security numbers, bank accounts and minor children's names appear in "almost 100%" of cases, so any AI discipline system must protect them (BLOOMBERG-TAXCT-2026).
- The court's 26 May 2026 notice of proposed rule amendments (comments to 24 Jul 2026) restyles Title XX on practice before the court and revises admission and disciplinary procedures; the announcement and notice text contain no reference to AI (keyword search of the text layer) (TAXCT-ANNOUNCE-2026). A rule changing AI-specific obligations has not been found.

**IRS-side errors.**
- Bloomberg reports that in Khoja v. Commissioner, Judge Siegel ordered a hearing on an IRS motion containing a citation to a nonexistent case and, on 11 March, questioned the IRS attorney who signed it about apparent AI use and safeguards; a Miller & Chevalier tax controversy counsel called it a warning about "AI without meaningful human review" (BLOOMBERG-TAXCT-2026, "Protecting Taxpayers"). I did not open the Tax Court order, so the result of the hearing is not confirmed.
- In Riddle Aggregates v. Commissioner (Docket 31104-21, trial 18 Mar 2026, Atlanta), petitioners objected to the IRS's rebuttal expert reports, saying the witness "clearly... used artificial intelligence", and pointed to more than 20 errors in his errata sheet for one report and four more for another. Respondent's counsel then said the "best path forward" was to withdraw Exhibits 9006-R and 9007-R. The expert testified he used Grammarly, ChatGPT and Gemini (TAXCT-RIDDLE-2026, Vol. 3, pp. 604 to 609 and 617 to 618; CHARLOTIN-2026 lists the expert as "Grammarly, ChatGPT, and Gemini" with "Report withdrawn"). The cause of the errors was disputed: the IRS argued Grammarly and dictation may have altered quotes (p. 611).

**Other tax tribunals.**
- Harber v HMRC [2023] UKFTT 1007 (TC), released 4 Dec 2023: a taxpayer gave the tribunal nine decisions that were "not genuine"; the tribunal accepted she did not know this, applied the existing reasonable-excuse test and dismissed her appeal on the merits, noting its decision would have been the same without the AI cases. It still said citing invented judgments wastes the tribunal's and HMRC's time and public money (FTT-HARBER-2023, paras 2 to 5, 23 to 24).
- Charlotin's AI Hallucination Cases Database lists 2,199 cases (all jurisdictions and case types, self-described as "a work in progress"; the count as viewed on 17 Oct 2026). Filtering for "tax" shows tax-court or tax-tribunal entries including: Moore v. Commissioner (US Tax Court, 15 Sep 2026, pro se, one fabricated and one misrepresented case); Riddle Aggregates (above); Clinco (9 Feb 2026, "Admonishment"); ZBDD and Commissioner of Taxation (Australian Administrative Review Tribunal, 8 Apr 2026, party listed as "Lawyer", "Admonishment"); iHEAT.ME Ltd v HMRC (UK First-tier Tribunal, Tax Chamber, 23 Jul 2026, pro se); and a Gujarat High Court entry (20 Aug 2026) where the responsible party is shown as "Judge" (I did not open that decision) (CHARLOTIN-2026, ?q=tax listing). The database is a single-person compilation and its entries were not independently checked.
- Non-tax courts have gone further than the Tax Court: JofA cites a default judgment in Flycatcher Corp. v. Affable Avenue (S.D.N.Y., 5 Feb 2026) after repeated false citations (JOFA-CLINCO-2026).

**Adjacent: privilege.**
- Orrick reports that on 13 Feb 2026 Judge Rakoff (S.D.N.Y.) held in United States v. Heppner that a defendant's own conversations with a consumer AI tool were neither attorney-client privileged nor work product, partly because the tool is not a lawyer and partly because of confidentiality terms (ORRICK-HEPPNER-2026). This is a securities-fraud case, not a tax case. No source read applies it to the §7525 federal tax practitioner privilege.

**Adjacent: consulting.**
- Deloitte Australia agreed to repay the final instalment of a A$440,000 report for the Department of Employment and Workplace Relations after fabricated references and a made-up court citation were found. Deloitte added a disclosure that Azure OpenAI GPT-4o was used; the amount repaid was to be made public after the transaction (GUARDIAN-DELOITTE-2025; CYBERDAILY-DELOITTE-2025). The report is a welfare-compliance review, not tax work; OPR cites it as an analogy (IRS-OPR-2026).

### 2.5 Other jurisdictions

**United Kingdom: PCRT.**
- Seven bodies that jointly maintain Professional Conduct in Relation to Taxation (AAT, ACCA, ATT, CIOT, ICAEW, ICAS, STEP) published topical AI guidance on 19 Jan 2026 (ATT-PCRT-2026; ICAEW-PCRT-2026). Its chair said the ethical principles are "consistent regardless of whether AI has been used" (ATT-PCRT-2026).
- Key messages (ICAEW summary): members are responsible for work irrespective of AI use; members unfamiliar with AI "may need to consider consulting an appropriate AI specialist"; integrity includes considering transparency to clients and being able to explain how a conclusion was reached; due diligence on output should use a risk-based approach; entering client data into a public AI model without consent is "likely" a confidentiality breach, so data should be anonymised and generic; extra caution applies when a tool generates tax-planning advice (ICAEW-PCRT-2026, "Key messages" and "Fundamental principles"). I read the ICAEW and ATT summaries, not the guidance document.

**Australia: Tax Practitioners Board.**
- TPB(GS) 55/2026 "The use of Artificial Intelligence and the Code of Professional Conduct" was issued 22 July 2026, after an exposure draft on 24 March 2026 (submissions closed 21 April 2026) (TPB-GS55-2026, "Document history"; TPB-NEWS-2026).
- It applies the Code of Professional Conduct under the Tax Agent Services Act 2009: competence (Code items 7 to 10), record-keeping (Determination s 30), supervision of entities providing services on the practitioner's behalf (s 35) and a documented, enforced system of quality management (s 40) (TPB-GS55-2026, Table 1).
- It says practitioners "should verify and review AI generated content for accuracy throughout each step of the workflow", establish processes to understand and contest AI outputs, and document each step (TPB-GS55-2026, "Competency").
- On confidentiality (Code item 6), it says practitioners "must obtain permission from each client" before divulging information to a third party, which "can include entering client information into AI models and tools, depending on how these tools are configured"; permission can be a signed engagement letter, signed consent or a "fact find" and consent, and a general authority may also be acceptable. It flags the Privacy Act 1988 (Cth) and the Privacy (Tax File Number) Rule 2015 (TPB-GS55-2026, "Confidentiality" and "Privacy Act").
- It lists AI functionality including tools that "may take actions on behalf of the user" and "auto-compiling of a tax form using third-party information" (TPB-GS55-2026, "What is AI?").
- It says it creates no new legal obligations beyond the Act (TPB-GS55-2026, disclaimer).

**Germany: Bundessteuerberaterkammer.**
- The BStBK FAQ "KI im steuerberatenden Berufsstand" (stated as of 27 January 2026, legal status July 2025) says decisions and responsibility "remain in human responsibility", that professional rules (StBerG, BOStB) are technology-neutral, that the duty of confidentiality (§57 StBerG) continues, and that AI tools do not relieve the Steuerberater of professional responsibility; technical decisions must still be reviewed by humans and internal review and approval processes documented. It also notes that vendors often largely exclude liability, and recommends EU-hosted providers and, where possible, a data-processing contract (BSTBK-KI-2026, Praeambel; section 5 "Recht"; "Tool-Governance").
- It cites the AI Act Article 4 AI-literacy duty for firms as deployers (BSTBK-KI-2026, section 1 and section 5).

**EU AI Act and data protection.**
- The AI Act entered into force 1 Aug 2024. A provisional Digital Omnibus agreement (6 May 2026, confirmed by Council representatives 13 May 2026) would defer stand-alone Annex III high-risk obligations to 2 Dec 2027 and Annex I to 2 Aug 2028, keep Article 50 transparency duties from 2 Aug 2026, and soften Article 4 so providers and deployers "support" rather than guarantee AI literacy. These take effect only on formal adoption; formal adoption was expected before 2 Aug 2026 per the 27 May 2026 alert, and I did not confirm it (GIBSON-AIACT-2026).
- EDPB Opinion 28/2024 (17 Dec 2024), as summarised by law firms in search extracts only: legitimate interest is not a default basis for AI model development or use, and AI models trained on personal data cannot always be considered anonymous. I did not open the Opinion (EDPB-OP28-2024, search-only).
- I did not find a source applying the AI Act to tax practitioners' own tools. The landscape's academic reading of AI Act treatment of tax-authority systems is not repeated here.

### 2.6 Liability, insurance and fees

**Insurance.**
- Digital Insurance (21 Apr 2026): professional liability insurers covering CPA firms are "increasingly coming to a consensus" that AI is a risk to be controlled by governance; premiums have not yet reflected AI; Aon (Stan Sterna) said there has been no substantive claim activity linked to AI at accounting firms and no major litigation; insurers "are going to ask a firm about their AI policy and procedures". Sterna predicted insurers will in a year or two ask more detailed questions and perhaps set guidelines (this is his forecast) (DIGIN-INSURERS-2026).
- McGowan (Raspante) recommends engagement-letter language disclosing AI use and an opt-out clause; CAMICO (Florian) says its concern is how a firm uses AI, not whether it does (DIGIN-INSURERS-2026).
- CAMICO's FAQ distinguishes AI used under supervision (generally lower exposure) from AI that autonomously advises or interacts with clients (heightened controls), suggests contract terms that the provider will not train on firm data, and offers sample engagement-letter wording; it says not all AI applications require client disclosure under current rules (CAMICO-FAQ-2025, Q1, Q4, Q6; published 12 Nov 2025 per page metadata).
- Exclusions: a search extract reports Verisk released generative AI exclusion forms CG 40 47 and CG 40 48 effective 1 Jan 2026 (general liability) and Berkley and others use broader E&O exclusions, with carve-backs negotiated where firms have governance (INS-EXCLUSIONS-2026, search-only). None of those sources is about accounting-firm policies, so whether CPA and tax E&O forms carry such exclusions is unverified.

**Penalty exposure that attaches to the signing human.**
- §6694(a): preparer penalty for an understatement due to an unreasonable position the preparer knew or should have known of, the greater of $1,000 or 50% of income derived from the return; reasonable cause and good faith is a defence. §6694(b): willful or reckless conduct, the greater of $5,000 or 75% of income derived (LII-USC-PREP-2026, §6694).
- §6695(b): $50 penalty for failure to sign where required; §6695(g): $500 per failure of due diligence on head of household status and the §24, 25A(a)(1) and 32 credits; §6695(h) indexes the §6695 amounts for inflation (LII-USC-PREP-2026, §6695). Amounts shown are the statutory base amounts.
- Commentary on reasonable-cause reliance on AI found only commentary-level material (Wood LLP, TAS quotation) in search extracts and no US decision on AI reliance (REASONABLE-CAUSE-2026, search-only). The Harber tribunal decided reasonable excuse on conventional principles and did not credit the AI-generated authorities (FTT-HARBER-2023).

**Liability allocation.**
- Werfel's register names "liability ambiguity" between the signing preparer and the AI vendor as a risk (AICPA-WERFEL-2026, Figure 3). The BStBK FAQ notes vendors "often" largely exclude liability (BSTBK-KI-2026). I did not read any vendor's terms.
- An Accounting Today opinion (1 Jul 2026, Rachel Farris, a practitioner) argues that relying on a client's AI-generated memo offers "zero liability protection" and that engagement boundaries are unclear when reviewing a client's AI plan. This is opinion, not analysis of policy or case law (ACCTODAY-LIAB-2026).

**Fees.** See 2.1: OPR §10.27 point and the AICPA dispute (JOFA-FEES-2026).

### 2.7 Preparer signing obligations and the steps that need human judgment

**Signing rules.**
- A "signing tax return preparer" is "the individual tax return preparer who has the primary responsibility for the overall substantive accuracy of the preparation" of the return (Reg. §301.7701-15(b)(1)). That individual must sign after the return is completed and before it is presented to the taxpayer (Reg. §1.6695-1(b)(1)). The definition excludes persons providing only "typing, reproduction, or other mechanical assistance" from "tax return preparer" status, but I did not find a source treating an AI agent's drafting as mechanical assistance or otherwise (LII-CFR-SIGN-2026).
- A "nonsigning" preparer prepares "all or a substantial portion" of a return, so reviewers and specialists who contribute can carry penalty exposure (LII-CFR-SIGN-2026, §301.7701-15(b)(2)).

**Where regulators place human judgment (each tied to a source).**

| Step | Why a human is required | Source and locator |
|---|---|---|
| Signing or approving a return or claim | Signer carries primary responsibility for substantive accuracy; §6694 and §10.34 attach to the practitioner | LII-CFR-SIGN-2026; ECFR-C230-2026 §10.34(a) |
| Positions: reasonable basis, substantial authority, disclosure | §10.34(a)(1) and §6694(a)(2) test whether a position is supportable | ECFR-C230-2026; LII-USC-PREP-2026 |
| Verifying facts, citations, calculations in AI output | §10.22 due diligence | IRS-OPR-2026 item 1 |
| Written advice (opinions, memos to clients) | Reasonable assumptions; independent authentication; opacity can make reliance unreasonable | IRS-OPR-2026 item 5; KTS-OPR-2026 "Written Tax Advice" |
| Deciding what client data can go to which tool; obtaining consent | §7216 and the regulation's "substantive determinations" line; TPB client permission | ECFR-7216-2026; TPB-GS55-2026 "Confidentiality" |
| Evaluating and contesting AI outputs through the workflow | TPB expects documented review at each step | TPB-GS55-2026 "Competency" |
| Expert and transfer pricing analysis | An LB&I official said AI can support but "shouldn't replace" legal, economic and factual judgment, and experts must explain inputs, assumptions, methods and AI tools; the IRS will "want to see the formulas" | EY-LBITP-2026 (reporting remarks of 29 Jul 2026) |
| Filings in court | Rule 201(a) and Model Rule 3.3(a)(1); Rule 33(b) | TAXCT-CLINCO-2026 n.7 |
| Billing | §10.27(a) | IRS-OPR-2026 item 2 |
| Firm-level procedures, training, vendor vetting | §10.36 (principal-authority individuals) | ECFR-C230-2026; IRS-OPR-2026 item 4 |
| Scope and phased deployment decisions | Werfel: start with limited scope, test, and scale only after verification controls pass | AICPA-WERFEL-2026 "Innovate, but responsibly" |

**Evidence that review is thin in practice.**
- Thomson Reuters Institute's 2026 Future of Professionals tax and audit paper (21 Jul 2026) reports 81% of surveyed tax and audit professionals use AI tools regularly and "more than one-third" admit using unauthorized AI tools. Both are vendor-published survey figures; the paper's full survey sample for this subset is not stated in the page read (TR-FOP-2026).
- At the TEI Tax Technology Seminar (27 to 29 Apr 2026), when a Thomson Reuters writer's room of more than 50 was polled on whether the tax function owns AI implementation at their company, "two hands went up". Attendees described the difficulty of reviewing growing volumes when errors were "increasingly polite, quiet, and technical". This is a reporter's account of a poll, not a measured result (TR-TEI-2026).
- GAO (24 Mar 2026) found that IRS's AI governance had several entities overseeing individual use cases but none responsible for managing AI investments across the agency, and that over 25% of inventory use cases lacked information on benefits (GAO-2026). This concerns the tax authority; it is context for practitioner counterparties, not a practitioner standard.

---

## 3. What it means for an AI transformation conversation

### 3.1 Implications

1. **Governance is a precondition, not a follow-up.** Under §10.36 (US), TPB Determination s 40 (Australia) and PCRT's "ensuring staff receive appropriate training" (UK), the expectation is procedures, training and documentation as AI is introduced. A transformation roadmap that sequences "pilot first, policy later" runs against what the OPR alert says about firms using AI "whether they are aware of it or not" (IRS-OPR-2026; TPB-GS55-2026; ICAEW-PCRT-2026).
2. **Design the human step as a control with evidence, not as a stated intention.** The regulator language is "carefully review all documents", "verify and review ... throughout each step", "document AI usage and verification processes". The Werfel register names control dilution as a risk because volume rises while review capacity does not (IRS-OPR-2026; TPB-GS55-2026; AICPA-WERFEL-2026).
3. **Inventory what is AI already.** The alert and TPB both treat AI embedded in research platforms and software as in scope. A tool-approval list needs to include embedded features, not only chatbots (IRS-OPR-2026; TPB-GS55-2026 "What is AI?").
4. **The data decision (7216, confidentiality, privacy) is made per workflow and per tool.** What the tool does (summarise, extract, or make a substantive determination), where data goes, and whether it trains on inputs all change the answer (ECFR-7216-2026; CAMICO-FAQ-2025 Q2, Q4; TPB-GS55-2026).
5. **Pricing and AI are now a regulatory question in the US.** The OPR fee position and the AICPA pushback mean outcome-based pricing models should be reviewed against the §10.27 point before the model is changed, and time records should reflect AI-assisted work accurately (IRS-OPR-2026; JOFA-FEES-2026).
6. **The firm's exposure is wider than a lawyer's filing.** Reports and work product in tax controversy (expert reports, motions), research memos, consulting deliverables, and client-facing chatbots have each produced an AI incident in the sources read (TAXCT-RIDDLE-2026; BLOOMBERG-TAXCT-2026; FTT-HARBER-2023; GUARDIAN-DELOITTE-2025).
7. **In-house departments sit on a thinner governance base.** The one data point found is a reported poll at TEI in which few attendees said the tax function owns AI implementation (TR-TEI-2026). Whether Circular 230 or PCRT applies to in-house staff differently was not established in these sources.

### 3.2 Interview probes

1. "Which AI tools can your people use on client or return data today, who approved them, and how do you know nobody uses others?" (Anchors: TR-FOP-2026 unauthorized use; IRS-OPR-2026 item 6.)
2. "For each AI-assisted workflow, who signs, and what do they review? Can you show the review record for last filing season?" (Anchors: LII-CFR-SIGN-2026; TPB-GS55-2026 documentation.)
3. "Where does client information go when a preparer uses a model, and under what contract terms: no training, retention, location? Have you decided whether any workflow involves a substantive determination by the vendor?" (Anchors: ECFR-7216-2026 §301.7216-2(d)(1); CAMICO-FAQ-2025.)
4. "Has your fee model been looked at against §10.27(a) or your local equivalent now that AI cuts research and drafting time?" (Anchors: IRS-OPR-2026 item 2; JOFA-FEES-2026.)
5. "What happens when AI output reaches a regulator, court or client with a fabricated or wrong authority? Who finds out, who corrects the record, who tells the client?" (Anchors: TAXCT-CLINCO-2026 [counsel did not correct]; IRS-OPR-2026 notes lawyers must notify clients and judges.)
6. "Has your professional liability insurer asked about AI at renewal? What did you tell them?" (Anchor: DIGIN-INSURERS-2026.)
7. For in-house: "Which team owns AI risk for tax data and positions: tax, IT, legal or internal audit?" (Anchor: TR-TEI-2026 poll.)

### 3.3 Objections and evidence-based responses

| Objection | Response from the sources |
|---|---|
| "The rules do not cover AI yet; we will wait for guidance." | OPR, PCRT, TPB and BStBK each say existing rules apply now. OPR names §10.36 firm procedures and training explicitly. Waiting is not a position any of them offers (IRS-OPR-2026; ICAEW-PCRT-2026; TPB-GS55-2026; BSTBK-KI-2026). |
| "Hallucinated citations are a litigator's problem." | Tax cases include an IRS expert's reports withdrawn, an IRS motion queried, counsel admonished, and a taxpayer in a UK penalty appeal. Outside courts, Deloitte Australia refunded part of a fee. Honest limit: no tax-practitioner sanction was found (TAXCT-RIDDLE-2026; BLOOMBERG-TAXCT-2026; TAXCT-CLINCO-2026; FTT-HARBER-2023; GUARDIAN-DELOITTE-2025). |
| "We have human review, so we are covered." | Review has to be real: OPR says verify facts, citations and calculations; TEI attendees described errors that are "quiet" and hard to review at volume; Werfel lists control dilution. Evidence of review, not the presence of a reviewer, is what the TPB and OPR documentation language points to (IRS-OPR-2026; TR-TEI-2026; AICPA-WERFEL-2026). |
| "Our enterprise tool is secure, so §7216 is not an issue." | Security is necessary but the §7216 question is disclosure and use, and the regulation's consent line turns on whether the service is a substantive determination. No IRS guidance on AI was found and commentators disagree; decide per workflow, document the reasoning, and consider consent where the vendor's role is substantive (ECFR-7216-2026; TAXADV-7216-2024; MYCPE-7216-2026 as the broader vendor view). |
| "Value pricing means AI savings are ours." | The AICPA and OPR disagree publicly; OPR's position is not authoritative per the AICPA CEO and no clarification has issued. Pricing on value is not ruled out in the sources, but billing for hours not worked may be an issue under §10.27 "depending on the facts" (IRS-OPR-2026; JOFA-FEES-2026). |
| "Insurers will make this uninsurable, or will not care." | In the accounting line, insurers are asking about policies and procedures and have not yet changed premiums; no substantive AI claims at Aon-administered accounting policies as of April 2026. Exclusions seen elsewhere were not verified for accounting forms (DIGIN-INSURERS-2026). |
| "Disclosure to clients will frighten them." | No universal duty to disclose AI use in most US tax matters is stated in the sources (JOFA-CLINCO-2026, "Disclosure considerations"). UK PCRT asks members to consider transparency; TPB requires client permission when information goes to third parties; McGowan recommends engagement-letter disclosure and an opt-out; some court certification requirements exist (ICAEW-PCRT-2026; TPB-GS55-2026; DIGIN-INSURERS-2026). |

---

## 4. Frontier signals

Dates are as published. "Forecast" items are labelled with who made them.

| Date | Signal | Status | Source |
|---|---|---|---|
| 19 Jan 2026 | UK PCRT bodies publish AI topical guidance | Published | ATT-PCRT-2026 |
| 27 Jan 2026 | BStBK FAQ on AI in tax advice (stated date) | Published | BSTBK-KI-2026 |
| 9 Feb 2026 | Clinco: Tax Court admonishes counsel; says it has not sanctioned for AI "Yet" | Decided | TAXCT-CLINCO-2026 |
| 13 Feb 2026 | Heppner (S.D.N.Y.): consumer AI chats not privileged or work product (non-tax) | Decided | ORRICK-HEPPNER-2026 |
| 11 Mar 2026 | Khoja hearing on an IRS motion with a nonexistent citation (per Bloomberg) | Reported; order not read | BLOOMBERG-TAXCT-2026 |
| 18 Mar 2026 | Riddle Aggregates: IRS withdraws two expert reports at trial | Transcript | TAXCT-RIDDLE-2026 |
| 20 Mar 2026 | Judge Holmes: Tax Court "feeling our way"; rules committee might consider AI certification | Forecast-like remark, not a proposal | BLOOMBERG-TAXCT-2026 |
| 24 Mar to 22 Jul 2026 | TPB exposure draft then Guidance Statement 55/2026 | Final | TPB-GS55-2026 |
| 21 Apr 2026 | Aon's Sterna expects insurers to ask more detailed AI questions within a year or two | Forecast (Aon) | DIGIN-INSURERS-2026 |
| 6 May 2026 | EU provisional agreement to delay high-risk AI Act duties to 2027/2028; formal adoption unconfirmed | Provisional | GIBSON-AIACT-2026 |
| 26 May 2026 | Tax Court proposes Title XX rule amendments; no AI text | Proposed; comments closed 24 Jul 2026 | TAXCT-ANNOUNCE-2026 |
| 24 Jun 2026 | IRS OPR Alert 2026-19 | Published | IRS-OPR-2026 |
| 8 Sep 2026 | AICPA seeks IRS clarity on fee language | Pending | JOFA-FEES-2026 |
| 31 Aug 2026 | Werfel's AI risk framework in The Tax Adviser | Published | AICPA-WERFEL-2026 |
| 23 Sep 2026 | AICPA launches CART | Announced; meets "throughout the year" | TAXADV-CART-2026 |
| 6 Oct 2026 | ABA Tax Section panel on 7216/6713 and AI (listed) | Scheduled | WINTHROP-ABA-2026 |
| 2 Apr 2026 | Perplexity launches an agent that drafts federal returns from uploads (consumer product, requires a $17 per month Pro subscription; company announcement of 2 Apr 2026) | Launched (company announcement) | PYMNTS-PERPLEXITY-2026 |

**Reading across the signals.**
- *Observed:* regulator guidance has converged on "existing duties apply" within a 6-month window (Jan to Jul 2026), and the first formal professional-body risk framework and cross-sector council followed in Aug and Sep 2026.
- *Forecast (landscape, not independently verified here):* a Tax Court rule or standing order on AI within 12 to 24 months. The only source here for this is the judge's own hesitant remark.
- *Not yet observed:* an IRS reply on fees, a §7216 consent form for AI, a tax-practitioner sanction for AI misuse, accounting-line AI exclusions.

---

## 5. Sources

Access: `full` = opened and read for the cited points; `partial` = opened but paywalled or truncated; `search-only` = seen only as a search result or extract.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| IRS-OPR-2026 | Alert 2026-19, Introductory Guidelines for Responsible AI Use in Federal Tax Practice | IRS Office of Professional Responsibility (via IRS Newswire) | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 24 Jun 2026 | full |
| ECFR-C230-2026 | 31 CFR Part 10 (Circular 230) §§10.22, 10.34, 10.35, 10.36, 10.51 | eCFR (Treasury) | regulator | https://www.ecfr.gov/current/title-31/subtitle-A/part-10 | current as of 1 Oct 2026 | full |
| ECFR-7216-2026 | 26 CFR §§301.7216-1, -2, -3 | eCFR / Cornell LII (Treasury) | regulator | https://www.law.cornell.edu/cfr/text/26/301.7216-2 | current | full |
| LII-USC-7216-6713 | 26 USC §§7216, 6713 | Cornell LII (US Code) | regulator | https://www.law.cornell.edu/uscode/text/26/7216 | current | full |
| LII-USC-PREP-2026 | 26 USC §§6694, 6695 | Cornell LII | regulator | https://www.law.cornell.edu/uscode/text/26/6694 | current | full |
| LII-CFR-SIGN-2026 | 26 CFR §301.7701-15 and §1.6695-1 | Cornell LII | regulator | https://www.law.cornell.edu/cfr/text/26/301.7701-15 | current | full |
| IRS-P4557-2024 | Publication 4557, Safeguarding Taxpayer Data (Rev. 6-2024) | IRS | regulator | https://www.irs.gov/pub/irs-pdf/p4557.pdf | Jun 2024 | full |
| TAXCT-CLINCO-2026 | Clinco v. Commissioner, T.C. Memo. 2026-16 | US Tax Court | regulator (court) | https://www.damiencharlotin.com/documents/1474/Clinco_v._Commissionner.pdf | 9 Feb 2026 | full |
| JOFA-CLINCO-2026 | A recipe for sanctions: AI-hallucinated citations in tax | Journal of Accountancy (AICPA), Newkirk and Webber | professional-body | https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/ | Sep 2026 | full |
| BLOOMBERG-TAXCT-2026 | Tax Court Navigates AI Misuse Rules for Self-Represented Filers | Bloomberg Tax Daily Tax Report | press | https://news.bloomberglaw.com/daily-tax-report/tax-court-navigates-ai-misuse-rules-for-self-represented-filers | 20 Mar 2026 | partial (paywall after most of article) |
| TAXCT-RIDDLE-2026 | Riddle Aggregates, LLC v. Commissioner, Docket 31104-21, trial transcript Vol. 3 | US Tax Court (transcript via Charlotin) | regulator (court) | https://www.damiencharlotin.com/documents/1972/Riddle_Aggregates.pdf | 18 Mar 2026 | full |
| TAXCT-ANNOUNCE-2026 | Announcement and notice of proposed rule amendments; press-release listing | US Tax Court | regulator | https://ustaxcourt.gov/files/documents/Announcement_05262026.pdf | 26 May 2026 | full |
| FTT-HARBER-2023 | Felicity Harber v HMRC [2023] UKFTT 1007 (TC) | First-tier Tribunal (Tax Chamber) | regulator (court) | https://caselaw.nationalarchives.gov.uk/ukftt/tc/2023/1007 | 4 Dec 2023 | full |
| CHARLOTIN-2026 | AI Hallucination Cases Database (tax filter) | Damien Charlotin | academic | https://www.damiencharlotin.com/hallucinations/?q=tax | viewed 17 Oct 2026 | full (listing only; underlying decisions mostly not opened) |
| ATT-PCRT-2026 | Professional bodies issue AI advice to members | Association of Taxation Technicians | professional-body | https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members | 19 Jan 2026 | full |
| ICAEW-PCRT-2026 | PCRT bodies publish guidance on using AI in tax | ICAEW | professional-body | https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax | 19 Jan 2026 | full (summary; guidance itself not read) |
| TPB-GS55-2026 | TPB(GS) 55/2026 The use of AI and the Code of Professional Conduct | Tax Practitioners Board (Australia) | regulator | https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct | 22 Jul 2026 | full |
| TPB-NEWS-2026 | TPB releases guidance on responsible AI use for tax practitioners | Tax Practitioners Board | regulator | https://www.tpb.gov.au/tpb-releases-guidance-responsible-ai-use-tax-practitioners | 22 Jul 2026 | full |
| BSTBK-KI-2026 | FAQ: KI im steuerberatenden Berufsstand | Bundessteuerberaterkammer | professional-body | https://www.bstbk.de/downloads/bstbk/digitalisierung/BStBK_FAQ-KI_end.pdf | 27 Jan 2026 | full (read selected sections; German) |
| AICPA-WERFEL-2026 | A risk framework for AI use in tax administration and preparation (Danny Werfel) | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/ | Aug 2026 issue (listed 31 Aug 2026) | full (main text; appendices not read) |
| TAXADV-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax | The Tax Adviser | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 23 Sep 2026 | full |
| AICPA-SSTS-2024 | Statements on Standards for Tax Services landing page | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/resources/landing/statements-on-standards-for-tax-services | page viewed Oct 2026; SSTS effective 1 Jan 2024 | partial (standards PDF not opened) |
| JOFA-FEES-2026 | AICPA seeks IRS clarity on AI guidelines, CPA fees | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/sep/aicpa-seeks-irs-clarity-on-ai-guidelines-cpa-fees/ | 8 Sep 2026 | full |
| TAXADV-7216-2024 | The many implications of Sec. 7216 | The Tax Adviser | professional-body | https://www.thetaxadviser.com/issues/2024/jan/the-many-implications-of-sec-7216.html | Jan 2024 | full |
| KTS-OPR-2026 | Using AI in Tax Practice: What Practitioners Need to Know Before Filing Season | Kilpatrick Townsend (Hughes, Andres) | firm | https://ktslaw.com/blog/kilpatricks-state-and-local-tax-blog/2026/9/using-ai-in-tax-practice-what-practitioners-need-to-know-before-filing-season | 29 Sep 2026 | full |
| WINTHROP-ABA-2026 | You May Be a Return Preparer: Using AI Without Violating Sections 7216 and 6713 (panel notice) | Winthrop & Weinstine | firm | https://winthrop.com/bold-perspectives/you-may-be-a-return-preparer-using-ai-without-violating-sections-7216-and-6713/ | event listed 6 Oct 2026 | full (event notice only) |
| MYCPE-7216-2026 | AI Compliance for CPA and Accounting Firms: Client Consent Rules Under IRC §7216, AICPA, and FTC | MYCPE ONE (CPE vendor) | vendor | https://my-cpe.com/blogs/using-ai-cpa-accounting-firms-irc-7216-aicpa-ftc-compliance-guide | published 6 May 2026; updated 26 Jun 2026 | partial (selected sections) |
| DIGIN-INSURERS-2026 | Insurers eyeing AI risk at CPA firms | Digital Insurance / Accounting Today (Gaetano) | press | https://www.dig-in.com/news/insurers-eyeing-ai-risk-at-cpa-firms | 21 Apr 2026 | full |
| CAMICO-FAQ-2025 | Generative AI: Frequently Asked Risk Management Questions on CAMICO's Advisory Hotline | CAMICO (CPA professional liability insurer) | vendor | https://www.camico.com/blog/generative-artificial-intelligence-ai-frequently-asked-risk-management-questions-faq-on-camicos-advisory-hotline/ | 12 Nov 2025 | full |
| INS-EXCLUSIONS-2026 | Generative AI exclusions in commercial policies (Verisk CG 40 47/48; Berkley; others) | various trade and law-firm pieces | press | https://www.businessinsurance.com/specialty-insurers-weigh-ai-liability-risks-resist-exclusions/ | 2026 | search-only |
| ACCTODAY-LIAB-2026 | AI is creating a new class of tax liability (Rachel Farris) | Accounting Today | press | https://accountingtoday.com/opinion/ai-is-creating-a-new-class-of-tax-liability | 1 Jul 2026 | full (opinion) |
| REASONABLE-CAUSE-2026 | Commentary on reasonable cause and AI reliance (Wood LLP and others) | various | firm | https://www.woodllp.com/Publications/Articles/pdf/IRS_Waives.pdf | undated | search-only |
| GIBSON-AIACT-2026 | EU AI Act Omnibus Agreement: Postponed High-Risk Deadlines and Other Key Changes | Gibson Dunn | firm | https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines/ | 27 May 2026 | full |
| EDPB-OP28-2024 | EDPB Opinion 28/2024 on AI models (as summarised by CMS, Baker Botts, Matheson) | EDPB / law firms | regulator | https://cms.law/en/int/legal-updates/edpb-opinion-28-2024-key-takeaways-on-processing-personal-data-in-the-context-of-ai-models | 17 Dec 2024 | search-only |
| ORRICK-HEPPNER-2026 | Court Rules AI Conversations Are Not Privileged: What United States v. Heppner Means for You | Orrick | firm | https://www.orrick.com/Insights/2026/03/Court-Rules-AI-Conversations-Are-Not-Privileged-What-United-States-v-Heppner-Means-for-You | Mar 2026 (ruling 13 Feb 2026 per Orrick) | full |
| GUARDIAN-DELOITTE-2025 | Deloitte to pay money back to Albanese government after using AI in $440,000 report | The Guardian | press | https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report | 6 Oct 2025 | full |
| CYBERDAILY-DELOITTE-2025 | Deloitte to refund government after using AI in $440k report | Cyber Daily | press | https://www.cyberdaily.au/government/12737-deloitte-to-refund-government-after-using-ai-in-440-000-report | Oct 2025 | full |
| EY-LBITP-2026 | Report on recent US international tax developments, 31 July 2026 | EY Tax News | firm | https://taxnews.ey.com/news/2026-1658-report-on-recent-us-international-tax-developments-31-july-2026 | 31 Jul 2026 | full |
| GAO-2026 | Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522) | US GAO | regulator | https://www.gao.gov/products/gao-26-107522 | 24 Mar 2026 | full (summary page via mirror) |
| TR-FOP-2026 | Future of Professionals 2026: tax and audit paper | Thomson Reuters Institute | survey (vendor) | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 21 Jul 2026 | partial (landing text) |
| TR-TEI-2026 | 2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 4 May 2026 | full |
| PYMNTS-PERPLEXITY-2026 | Perplexity Launches AI Agent That Drafts Tax Returns | PYMNTS | press | https://www.pymnts.com/taxes/2026/perplexity-launches-ai-agent-that-drafts-tax-returns/ | 6 Apr 2026 | full |

Distinct sources read in full or partly: 39 (plus 3 search-only). Source types: regulator, professional-body, press, firm, vendor, survey, conference, academic.

---

## 6. Gaps

- **SSTS text.** The SSTS 1.4 paragraph cites rely on Journal of Accountancy; the AICPA PDF was gated/blocked. The AICPA's own OPR insight page and its FAQ on AI in federal tax practice were gated or not opened.
- **TPB, PCRT primary.** The TPB guidance statement was read in full; the PCRT AI guidance itself (as opposed to ATT/ICAEW summaries) was not located or read.
- **Khoja v. Commissioner.** Only the Bloomberg account was read (paywalled in part). The Tax Court order and hearing outcome were not found. The Bloomberg article's URL date was taken from the landscape and search results (20 Mar 2026).
- **Sanctions on tax practitioners.** No OPR disciplinary action, state board action or malpractice judgment involving AI misuse by a tax preparer or CPA was found. OPR says such cases are "slowly emerging" but names none. The OPR disciplinary-records page was not searched.
- **IRS guidance on §7216 and AI.** None found; the OPR alert is silent on consent. The conflict between the vendor reading (consent is the default) and the regulation's exceptions is unresolved here. I did not open Rev. Proc. 2013-14 itself. Whether VAT, sales tax and non-chapter-1 returns are covered by an equivalent rule, and the position under foreign data-protection law for each, was not established.
- **Preparer status of AI.** No source addresses whether an AI agent's drafting makes a firm or vendor a "tax return preparer", or whether PTIN, e-file or signature rules are strained by agentic preparation. The Perplexity coverage does not describe a preparer role.
- **Insurance.** Only one trade article and one insurer FAQ were read. Accounting-line exclusion wording, underwriting questionnaires and any AICPA-endorsed programme terms were not found. Exclusion evidence is from other lines and search extracts.
- **Reasonable cause with AI.** No US decision or IRS guidance found on whether reliance on an AI tool supports reasonable cause or good faith under §6664(c) or §6694(a)(3).
- **In-house departments.** Nothing found on how Circular 230, PCRT or TPB apply to in-house tax staff using AI, on ICFR or SOX implications for the provision, or on corporate officers' return-signing duties with AI. The TEI poll is one reporter's account.
- **Data protection.** EDPB Opinion 28/2024 was not opened; the UK ICO, the UK GDPR in tax practice and Canadian, Indian, Singaporean and other jurisdictions' tax-professional AI guidance were not covered (a German BStBK FAQ was found; a CPA Canada search returned nothing).
- **EU AI Act.** The formal adoption and Official Journal publication of the Digital Omnibus after 27 May 2026 was not confirmed. Article 4 literacy and the AI Act's application to tax practitioners' own tools were not analysed beyond the BStBK reference.
- **State laws.** OPR names California, Colorado, Illinois and Utah AI laws; none were read, and state boards of accountancy or NASBA guidance was not found.
- **Quality evidence.** No error rates, override rates or independent measurements of compliance with these guardrails were found. The TR (more than one-third using unauthorized tools) and TEI poll are the only practice-level indicators, both from a vendor's institute.
- **Date discrepancies.** The landscape dates the Werfel framework "Sep 2026"; the Tax Adviser listing and Journal of Accountancy place it in the August 2026 issue (31 Aug 2026). The Heppner ruling date is 13 Feb 2026 per Orrick; another source reported a bench ruling on 10 Feb 2026 (search extract), so check the docket before citing.

# Source landscape: advisory and outsourced services (accounting and advisory firms, private middle market)

Run date: 2026-10-20. Wave 5. Archetype: `advisory`.

Conventions used throughout:
- Every source has a ref in the form `PUBLISHER-SHORT-YYYY`. Later researchers should reuse these refs.
- **(opened)** means the page or PDF itself was fetched and read in this run (directly, or through the r.jina.ai mirror where the site blocked curl). **(snippet-only)** means the item surfaced in search results but the page was not read. Snippet-only items are leads, not evidence.
- `(unverified)` marks a fact that rests on a single secondary or vendor source, or that sources disagreed on.
- Quotations are kept under 25 words; everything else is paraphrased.
- Vendor and firm claims (speed-ups, adoption percentages, valuations) are self-reported unless stated otherwise.

---

## 1. Summary

**What the landscape looks like.** AI in advisory and outsourced services is covered unevenly. Client accounting services (CAS) and risk/assurance-adjacent work have a lot of specific public material. Transaction advisory, forensic, consulting/FP&A and private-client have little independent evidence, and much of it is vendor marketing.

**Seven things the evidence supports:**

1. **CAS is the anchor and the growth engine.** In Accounting Today's 2026 Top 100 coverage, 85% of the 88 responding firms reported CAS growth (ACCTODAY-TOP100-2026, snippet-only). Withum says its advisory practice grew out of a small CAS team and that CAS now brings in $70M (ACCTODAY-CASKEYS-2026, opened). The 2026 CAS Benchmark Survey report is due in December 2026 (CPACOM-CASBENCH-2026, opened), so the freshest hard numbers arrive after this run.
2. **Adoption is wide but shallow.** 98% of firms use AI but only 21% have an AI policy or strategy (KARBON-AISTATE-2026). 88% use AI for a client service but only 30% say it is embedded as the default (INTUIT-ACCTTECH-2026). 56% use genAI but only 10% have integrated it across operations (RAMP-CALCPA-2026). The gap between use and embedded workflow is the main journey-stage discriminator.
3. **Structure is changing as fast as technology.** Private-equity-backed alternative practice structures (APS) now include Grant Thornton (New Mountain), Crowe (KKR closed Aug 7, 2026) and Current (Thrive Holdings). The AICPA exposure draft on APS independence closed for comment Apr 30, 2026, and IESBA opened a PE workstream in March 2026. The advisory arm takes investor capital and the attest arm stays separate, so this directly shapes which advisory services are available to audit clients.
4. **Controls and assurance for client AI is a new service line.** KPMG found active AI use in finance rose from 30% to 75% (KPMG-AIFINANCE-2026). A CPA Practice Advisor article reports that only 42% of leaders were fully assurance ready (CPAPA-AGENTSCLOSE-2026), but KPMG's own release uses 42% for a different measure (scaling confidence among assurance-ready organisations, against 14% for others), so the readiness figure may be conflated `(unverified)`. Grant Thornton launched an Enterprise Assurance Services practice with provisional AIUC-1 accreditation on Sep 23, 2026 (GT-EAS-2026). This straddles risk-advisory and the assurance archetype.
5. **Valuation and forensic work are being pulled toward disclosure and reliability rules.** The IVSC exposure draft would require disclosure of significant AI use in the scope of work and the report (final text due Jan 2027, effective Jan 31, 2028; IVSC-IVSED-2026). The AICPA FVS committee issued members-only AI guidelines in Oct 2025 (BVR-AICPAAIGUIDE-2025). Proposed Federal Rule of Evidence 707 on machine-generated evidence drew comments to Feb 16, 2026 and was reportedly sent back for more work in June 2026 (STEPTOE-FRE707-2026 opened; the June status is from snippet-only secondary sources, `(unverified)`).
6. **Pricing and revenue models are under pressure, not yet resolved.** 69% of tax professionals expect to move toward value-based, hybrid or fixed fees (CPACOM-BLUEJ-2026). The IRS Office of Professional Responsibility flagged fee rules as an area to watch as AI shortens task time (IRS-OPR-2026; the fee point is from a commentator summary in search, `(unverified)` against the IRS text, which was opened but is introductory).
7. **Vendor fragility is real.** Botkeeper reportedly closed in Feb 2026 and its platform was acquired by Xendoo (UKU-BOTKEEPER-2026, opened, single vendor-blog source, `(unverified)`), while Basis raised $100M at a reported $1.15B valuation and Fieldguide raised $75M at $700M.

**Best three starting points for deep dives:** ACCTODAY-CASKEYS-2026 plus the CAS Benchmark (CAS), IVSC-IVSED-2026 (valuation), and FORVIS-QOE-2026 plus KPMG-AIFINANCE-2026 (deals and finance-function demand).

**Coverage honesty.** About 105 distinct sources were identified across eight source types; about 75 were opened and read (directly or through the mirror). The rest are search-snippet leads. See section 15 for counts and section 14 for what could not be reached. No official session catalogue was retrievable for ENGAGE, Digital CPA, the AICPA FVS conference or the ACFE Global Fraud Conference, so session-level detail for those is partial and labelled.

---

## 2. Conferences & events

### 2.1 Core events (2025 and 2026 editions)

| Ref | Event | Organizer | Date / edition | URL | Why it matters for AI here |
|---|---|---|---|---|---|
| KARBON-ENGAGE-2026 | AICPA & CIMA ENGAGE 2026 (curated session list) | Karbon Magazine (event run by AICPA & CIMA) | Jun 8-11, 2026, ARIA, Las Vegas (opened) | https://karbonhq.com/resources/aicpa-cima-engage-2026/ | Only retrievable session-level view of ENGAGE. Advisory, tech and forensic content in one place. See 2.2. |
| ATL-ENGAGE-2026 | Accounting Technology Lab podcast recap of ENGAGE 2026 (Randy Johnston, Brian Tankersley) | CPA Practice Advisor | Jul 2026 (opened) | https://www.cpapracticeadvisor.com/podcasts/thought-leader-40-under-40-aicpa-think-tank-accounting-technology-lab-podcast-july-2026/ | Recap: AI ran through most tracks, a standing-room Tech Update and AI prompting session, ~200-vendor expo; discussion of AI plus private equity as a driver of firm modernization. |
| MINDBRIDGE-ENGAGE-2026 | MindBridge at ENGAGE 2026 (Education Lab, tech demo) | MindBridge | Jun 8 and Jun 10, 2026 (opened via mirror) | https://www.mindbridge.ai/events/2026-aicpa-engage/ | Vendor-hosted sessions on AI for audit risk assessment and full-population analysis; shows assurance vendors working the ENGAGE floor. |
| CPACOM-DCPA-2026 | Digital CPA Conference 2026, theme "Vision to Velocity" | CPA.com | Dec 6-9, 2026, San Diego and live online (opened) | https://www.cpa.com/dcpa25 | The CAS and advisory technology conference. Agenda not retrievable; the page lists a speaker bench including Erik Brynjolfsson (Stanford HAI), Barry Melancon (Baker Tilly International), Nitin Mittal (Deloitte global AI leader), and CPA.com's Kim Blascoe (CAS Professional Services) and Brandon Allfrey (tax transformation). Which edition each speaker belongs to is `(unverified)` because the page mixes 2025 and 2026 material. |
| CPACOM-DCPA-2025 | Digital CPA 2025 | CPA.com | Dec 7-10, 2025, Washington DC (same page above) | https://www.cpa.com/dcpa25 | 37 sessions, 50+ speakers, covering CAS, audit, tax and AI. |
| JOFA-HOOD-2026 | Journal of Accountancy podcast with Tom Hood, recorded at Digital CPA (Gaylord National) | AICPA & CIMA | Jan 2026 (opened) | https://www.journalofaccountancy.com/podcast/2026/jan/tom-hood-on-ai-hybrid-work-and-other-2026-themes-shaping-accounting/ | Profession-leader framing: AI shifting from productivity tools to finance agents; Rise 2040 project. |
| ACCTODAY-FGF-2026 | Firm Growth Forum 2026, keynote "Scaling Smart: How AI, CAS Expansion and Advisory Services Can Drive Firm Growth" (Jim Bourke, Withum) | Accounting Today | May 19-20, 2026, San Diego (opened via mirror; dates from search) | https://firm-growth-forum.accountingtoday.com/session/keynote/ | Explicit link between AI pilots, CAS and cross-sold advisory. |
| ACCTODAY-CASSUMMIT-2026 | CAS Summit Virtual 2026 (sessions "CAS 3.0: The Next Frontier in Advisory Services" and "Deepening Adoption of AI & Automation") | Accounting Today | Half-day virtual; dates on the page and in search disagree (Jul 29 vs Aug 13) `(unverified)` (opened) | https://www.accountingtoday.com/cas-summit-virtual-2026-session | The only dedicated CAS event with AI as a named session. |
| FICPA-DES-2026 | Digital Evolution Summit (new) | FICPA with Karbon and Aider | Nov 16-17, 2026, Hollywood FL (opened) | https://www.cpapracticeadvisor.com/2026/09/08/ficpa-partners-with-karbon-and-aider-on-new-digital-evolution-summit/189854/ | New AI-implementation conference for firms; shows vendor-partnered state-society events spreading. |
| ACCOUNTEX-2026 | Accountex London 2026 product roundup | Financial Accountant (UK) | 2026 (opened) | https://financialaccountant.co.uk/blog/accountex-london-2026-product-roundup/ | Platform news: Sage Intacct Advisory update for outsourcing and advisory, Intuit Accountant Suite, Xero's agent builder and Claude integration. |
| AICPA-FVS-2026 | AICPA Forensic & Valuation Services Conference 2026 | AICPA & CIMA | Nov 4-6, 2026, National Harbor MD and live online (opened) | https://events.aicpa-cima.com/fvs/Home | Five topic areas including "AI, technology and advanced data"; 40+ sessions, 2 tracks; IVSC CEO Nick Talbot listed as speaker. Session titles not retrievable (agenda page 404 on the Agenda path). |
| BVR-NACVA-2026 | NACVA Business Valuation & Financial Litigation Super Conference 2026 (BVWire on-site report) | NACVA / BVR | Salt Lake City; Oct 1-2, 2026 per BVR calendar, Sep 30-Oct 2 per another BVWire listing `(unverified)` (opened via mirror) | https://www.bvresources.com/articles/bvwire/early-takeaways-from-the-nacva-conference | Sessions covered AI and changing valuation methods; keynoter Roger Grabowski said AI is a useful tool but does not replace judgment. |
| ACFE-GFC-2026 | 37th ACFE Global Fraud Conference | ACFE | Boston; Jul 12-17, 2026 per listings, opening keynote Mon Jul 13 (opened) | https://www.fraudconferencenews.com/home/keynote-speakers-37th-annual-acfe-global-fraud-conference | Keynotes retrievable (Auditor General of Malaysia, Cressey Award; whistleblower Noelle Webb). A listing says 90+ sessions including AI and OSINT but no AI session titles found. |
| ACFE-CANADA-2026 | ACFE Fraud Conference Canada 2026 | ACFE | Nov 15-17, 2026 (opened) | https://www.fraudconference.com/canada2026/sessions.aspx | Pre-conference "Using AI Ethically in Fraud Prevention and Detection" (Marc Tasse, CPA, CA, CFF); session 4C "AI and Data Analytics for E&C Programs" (speaker TBD). |
| ACFE-APAC-2026 | ACFE Asia-Pacific Fraud Conference 2026 | ACFE | Aug 2026 (opened) | https://www.fraudconference.com/asiapac2026/sessions.aspx | Session 2B "How to Uncover Artificial Intelligence Washing" (Iyad Mourtada, CFE, CIA, CMA). AI washing is a live forensic and risk-advisory topic. |
| IIA-ICONF-2026 | IIA International Conference 2026, theme Transformation | The IIA | Jun 21-24, 2026, Marina Bay Sands, Singapore (opened); one LinkedIn source gives Jun 22-24 `(unverified)` | https://www.theiia.org/en/content/communications/press-releases/2026/may/the-iias-international-conference-2026-to-be-held-june-21-24-in-singapore/ | 40+ sessions; CEO frames AI and automation as the main driver of change. Specific AI session titles not found. |
| IIA-GAM-2026 | IIA Great Audit Minds (GAM) 2026 | The IIA | Mar 9-11, 2026, Las Vegas (opened) | https://www.theiia.org/en/content/communications/press-releases/2026/the-institute-of-internal-auditors-great-audit-minds-conference-to-be-held-march-9-11-in-las-vegas/ | Lead theme "the rise of agentic AI": use cases and frameworks for piloting and scaling agents inside audit workflows; 30+ sessions, 50+ speakers (PayPal, Meta, Reddit, Verizon, Barclays, EY, PwC, KPMG, Deloitte). |
| KPMG-GAM-2026 | KPMG sponsor page for GAM 2026 | KPMG US | Mar 10, 2026 sessions (opened) | https://kpmg.com/us/en/events/2026/kpmg-iias-2026-gam-conference.html | Confirmed sessions: "Leading Internal Audit in the AI Revolution" (Charles King, KPMG; Adnan Rahim, Meta; Shane Negangard, Workiva) and a controls and automation session covering AI and agentic AI for continuous monitoring. |
| ACG-DEALMAX-2026 | ACG DealMAX 2026 recap | Association for Corporate Growth | Apr 27-29, 2026, ARIA, Las Vegas (opened) | https://www.acg.org/news-trends/news/acg-sets-new-benchmark-largest-most-efficient-dealmax-date | 3,500+ attendees incl. ~900 PE professionals; recap mentions AI-and-deals content in 18 sessions but names none. Shows the buyer audience for QoE and diligence is large. |

Snippet-only events (leads): Intuit Connect 2026 (Oct 26-28, Las Vegas; upcoming, so no content yet); Sage Future 2026 (Apr 28-30, San Francisco); Xerocon Denver (Aug 19-20, 2026); XeroCon London 2026; ICPAS AI Summit (Sep 21, 2026). Not covered: QuickBooks Connect 2025 session list, Sage partner events, ACG chapter events (apart from one Utah chapter "AI in Business" listing), quality-of-earnings practitioner forums.

### 2.2 AI-related sessions and speakers found (organizations as listed by the source)

**ENGAGE 2026 (KARBON-ENGAGE-2026; Karbon's picks, not the full catalogue):**
- "AI workshop: Getting technical in AI" (Mon Jun 8, 8am): Chris Ortega (Fresh FP&A), Wesley Hartman (Automata Practice Development). Hands-on, pre-work required.
- "Advisory at scale: Delivering personalized value in a high-growth model" (Tue Jun 9): Laurence Bernstein (Proseer), Nina Chmura (WithumSmith+Brown), Kate Serpe (CPA.com).
- "The tech-enabled adviser: Evolving the role of finance through automation and insight" (Tue): Matthew Wallace (Armanino), Floriana Allen (Wiss & Company). Dimensional reporting, AI-driven insights, open APIs.
- "AI conversations and integration: A practical guide for CPAs and their clients" (Tue): Twyla Verhelst (Karbon), Samantha Bowling (GW CPA), Neha Patel (Weaver & Tidwell). Clients asking CPAs about AI tools and risks.
- "Building automations live" (Tue): Byron Patrick (Karbon), built with Claude Code.
- "Rapid fire apps: Speeding up" (Wed): Byron Patrick (Karbon), Ashley Francis (Andersen), Nicholas Panou (PwC Canada), Brian Tankersley (K2 Enterprises).
- "The distributed firm: technology strategies for remote, hybrid and offshore teams" (Wed): two Baker Tilly speakers, Nina Chmura (Withum), Laurence Whittam (Whitman Advisory).
- "The Great Realignment: Five seismic shifts shaping the next five years of accounting" (Wed): Reyes Florez (Platform Accounting Group).
- "Mergers, acquisitions, and mayhem" (Tue): Matthew May (Sorren), Kenji Kuramoto (Basis), Nathen McEown (Whitley Penn).
- "Forensic accounting in action: Corporate fraud case studies" (Thu): two FBI forensic accountants.
- A Wolters Kluwer listing shows "From GenAI to AI Agents: What's Next for Tax, Audit, and Advisory" (Tue 7:00am) (snippet-only).

**FVS and valuation:** AICPA-FVS-2026 topic list; the 2025 AICPA FVS conference had a deepfake session and a rebroadcast webcast on practitioners' AI use and court opinions on experts' AI use (snippet-only; aicpa-cima.com webcast listing "AI Right Now for Forensic Accounting Professionals").

**Internal audit:** IIA-GAM-2026 and KPMG-GAM-2026 as above. A Protiviti and Optro webinar drew on the IIA Singapore conference (snippet-only).

**Fraud and forensics:** ACFE-CANADA-2026 and ACFE-APAC-2026 as above.

**Public recordings, decks and proceedings:** none found openly. ENGAGE, DCPA and FVS content is behind registration. The AICPA FVS section podcasts are free (BVR-AICPAREPORT-2026 notes this) and the Accounting Technology Lab and Journal of Accountancy podcasts are public.

---

## 3. Regulators & standard-setters

| Ref | Body | Item | Date | URL | Why it matters |
|---|---|---|---|---|---|
| IESBA-PE-2026 | IESBA | Launch of a workstream on private equity investment in accounting firms (APS); also agreed to develop new non-authoritative guidance on technology and AI (opened) | Mar 26, 2026; PE update due at June 2026 meeting | https://www.ethicsboard.org/news-events/2026-03/iesba-launches-workstream-private-equity-investment-accounting-firms | Direct bearing on which advisory services PE-backed firms can sell to attest clients; first sign of AI ethics guidance from IESBA. |
| AICPA-PEEC-APS-2025 | AICPA Professional Ethics Executive Committee | Exposure draft "Proposed Revisions Related to Alternative Practice Structures" (JofA article opened) | Issued Dec 2025; comments due Apr 30, 2026 | https://www.journalofaccountancy.com/news/2025/dec/aicpa-proposes-changes-to-independence-rules-related-to-private-equity/ | Distinguishes investor "significant influence" from "control" over the nonattest entity and changes the "network firm" definition. Final status not confirmed. A NASBA comment letter (Apr 27, 2026) supported a 5% bright-line with disclosures (snippet-only). |
| FRC-GENAI-2026 | UK Financial Reporting Council | Guidance on generative and agentic AI in audit engagements (opened) | Mar 30, 2026 | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | FRC describes it as the first from any audit regulator globally; confidence-in-output framework with illustrative examples such as reviewing contracts for revenue recognition testing. Template for what US regulators may do for non-attest work. |
| IRS-OPR-2026 | IRS Office of Professional Responsibility | Issue 2026-19, Introductory Guidelines for Responsible AI Use in Federal Tax Practice (opened) | Jun 24, 2026 | https://www.irs.gov/pub/opr-taxpros/issue-number-2026-19-introductory-guidelines-for-responsible-ai-use-in-federal-tax-practice.pdf | Circular 230 duties (diligence, competence) apply to AI output; relevant to private-client and valuation work that feeds tax positions. |
| IVSC-IVSED-2026 | International Valuation Standards Council | Exposure draft of IVS (effective 31 Jan 2028): AI and other technology-based tools disclosure in scope of work and reporting; changes to IVS 104, 105, 106; new quality-control standard IVS 107 (opened) | Consultation Jan 31 - Apr 30, 2026 per search; final Jan 2027, effective Jan 31, 2028 per the ED itself | https://ivsc.org/_ivs_effective_31_january-2028_exposure-draft-summary-and-consultation-questions-final_ | Most concrete standard-setting move on AI in any advisory service line. The ED targets opaque tools whose reasoning a valuer cannot readily explain. |
| IVSC-PULSE-2026 | IVSC with 73 Strings | The Valuation Pulse: AI and Technology in Valuation Sentiment Tracker (opened) | May 8, 2026 | https://ivsc.org/the-valuation-pulse-ai-technology-in-valuation-sentiment-tracker/ | Survey instrument to inform the IVSC AI and Technology Working Group; results not yet public. |
| AICPA-AUDITAID-2026 | AICPA | Practice aid "Artificial Intelligence (AI) Considerations for Financial Statement Auditors" (JofA article opened) | Oct 13, 2026 | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | Non-authoritative; covers client AI in financial reporting and controls and the auditor's own AI use. Sets expectations that CAS and controllership clients will be asked about AI controls. |
| PCAOB-GENAI-2024 | PCAOB staff | Spotlight on outreach about GenAI in audits and financial reporting (opened PDF) | Jul 2024 | https://pcaobus.org/documents/generative-ai-spotlight.pdf | Older than the 12-18 month window but still the PCAOB's main published staff view; found no 2025-2026 successor. |
| STEPTOE-FRE707-2026 | US federal judiciary (Advisory Committee on Evidence Rules), via Steptoe | Proposed Federal Rule of Evidence 707 on machine-generated evidence; comment period to Feb 16, 2026 (opened via mirror) | 2026 | https://www.steptoe.com/en/news-publications/the-mother-court-blog/ai-in-the-courtroom-how-proposed-rule-707-could-shape-evidence-standards.html | Uses an AI-produced forensic accounting report as its example. June 2026 "sent back for study" status is from snippet-only Proskauer and NatLawReview items `(unverified)`. |
| SEC-EXAMPRI-FY2026 | SEC Division of Examinations | FY2026 examination priorities (released Nov 17, 2025) with growing attention to AI (snippet-only via Goodwin summary; page blocked) | Nov 2025 | https://www.goodwinlaw.com/en/insights/publications/2025/12/alerts-privateequity-pif-2026-sec-exam-priorities-for-registered-investment-advisers | Relevant to private-client and wealth work through RIA affiliates and to AI-washing claims. Primary SEC document not read. |
| COSO-GENAI-2026 | COSO | February 2026 guidance on internal control over generative AI (cited in CPAPA-AGENTSCLOSE-2026; not fetched directly) | Feb 2026 | see CPAPA-AGENTSCLOSE-2026 | Likely anchor for risk-advisory and SOX-readiness offerings on AI controls. Go to the primary source in deep dives. |
| COLORADO-AIACT-2025 | Colorado | AI Act effective date delayed to Jun 30, 2026 (snippet-only; 2026 session outcome not found) | Aug 2025 | https://www.gtlaw.com/en/insights/2025/9/colorado-delays-comprehensive-ai-law-with-further-changes-anticipated | Possible obligations for firms and clients using AI in consequential decisions; current status unknown. |

**Independence note (where the firm also audits the client).** The APS structures above exist because attest independence limits who can own an audit firm and which services can be sold to attest clients. The Crowe, Grant Thornton and Current releases all describe a licensed CPA firm for attest and a separate non-attest entity taking investor capital (CROWE-KKR-2026, GT-GTAP-2026, ACCTODAY-CURRENT-2026). Services commonly restricted for attest clients under US and international independence rules include bookkeeping and financial-system design, certain valuations, and internal-audit outsourcing (general background, `(unverified)` in this run; deep dives must confirm against AICPA, SEC and PCAOB rules and the IESBA Code). AI assurance (AIUC-1, SOC) sold to non-audit clients is a separate analysis (GT-EAS-2026).

---

## 4. Professional bodies

| Ref | Body | Item | Date | URL | Why it matters |
|---|---|---|---|---|---|
| CPACOM-CASBENCH-2026 | CPA.com and AICPA PCPS | CAS Benchmark Survey page: 2026 report "coming soon" (December 2026); benchmarks revenue and pricing models, staffing, technology adoption, service offerings (opened) | 2026 edition open; 2024 edition is latest published | https://cpa.com/cas-benchmark-survey | The standard CAS benchmark. 2024 edition: 200+ respondents, median growth 17% per JofA (JOFA-CASTIPS-2025). Full 2024 data set is for participants only. |
| JOFA-CASTIPS-2025 | AICPA & CIMA (Journal of Accountancy) | "Tips for providing the CAS services clients want" (opened) | Jul 2025 | https://www.journalofaccountancy.com/issues/2025/jul/tips-for-providing-the-cas-services-clients-want/ | Defines CAS as outsourced or co-sourced financial operations, quotes CohnReznick (60% growth in 2024), Cherry Bekaert and Wipfli alumni. Baseline for the module. |
| CPACOM-BLUEJ-2026 | CPA.com with Blue J | Second annual AI Tax Research Solution Outlook (opened) | Jun 8, 2026 | https://www.cpa.com/news/blue-j-and-cpacom-survey-finds-ai-adoption-among-tax-firms-has-nearly-doubled-one-year | Tax-centred but 44% name advisory projects as the top AI application and 69% expect value-based, hybrid or fixed fees. |
| BVR-AICPAAIGUIDE-2025 | AICPA Forensic & Valuation Services Executive Committee (via BVR) | "Guidelines for Responsible Use of AI in Forensic and Valuation Services Engagements" (members-only; BVR summary opened) | Oct 2025 | https://www.bvresources.com/articles/bvwire/aicpa-issues-ai-usage-guidelines-for-valuation-and-forensic-work | Not a standard; reminders on engagement terms, confidentiality and judgment. Also notes a BVR Leadership Council AI perspective paper (free). |
| BVR-AICPAREPORT-2026 | AICPA FVS podcast series (via BVR) | AI agents as a quality-control layer for valuation reports (podcast speakers: Bethany Hearn, MH CPA; Dr. Victor Jarosiewicz, Georgia State; host Nene Glenn Gianfala, Chaffe & Associates) (opened via mirror) | 2026 (undated on page) | https://www.bvresources.com/articles/bvwire/ai-agents-as-a-quality-control-layer-for-valuation-reports | A concrete use case: agents checking reports for standards compliance, with human review retained. |
| BVR-IVSPODCAST-2026 | AICPA podcast (via BVR) | AI disclosure requirements in the proposed IVS (opened via mirror) | 2026 | https://www.bvresources.com/articles/bvwire/ai-disclosure-requirements-in-proposed-ivs-highlighted-in-aicpa-podcast | Signals US valuers will track the IVS change. |
| ACCTODAY-VPF-2026 | AICPA, American Society of Appraisers, RICS | Proposed Valuation Performance Framework (exposure draft; feedback due Dec 22, 2026) (opened) | Oct 13, 2026 | https://www.accountingtoday.com/news/aicpa-proposes-valuation-framework | Principles-based replacement for the Mandatory Performance Framework. Whether it addresses AI directly was not confirmed. |
| IIA-AIKC-2026 | The IIA (via IIA Belgium) | AI Knowledge Center: AI Auditing Framework support tools and "AI Prompting for Internal Auditors" (Aug 2026) (opened) | Aug 2026 | https://www.iiabelgium.org/news-publications/iia-ai-knowledge-center-new-tools-for-internal-auditors | Practical tooling for internal-audit outsourcing teams; framework date varies by source (2023 vs 2024) `(unverified)`. |
| ACFE-TECHBENCH-2026 | ACFE with SAS | 2026 Anti-Fraud Technology Benchmarking Report (press release opened) | Mar 2026 | https://www.sas.com/en_us/news/press-releases/2026/march/acfe-anti-fraud-technology-study-deepfakes.html | n=713. Only 7% say they are more than moderately prepared for AI-fuelled fraud; 25% use AI/ML in anti-fraud analysis (18% in 2024); 16% use genAI as an anti-fraud tool and 58% plan to. |
| ACCA-ETHICS-2026 | ACCA | "Navigating ethics for trust" (opened via mirror) | Oct 14, 2026 | https://www.accaglobal.com/policy-and-insights/reports/2026/navigating-ethics-for-trust | n=1,178 across 135 countries. 61% rank AI use as the top ethical challenge (32% in 2024). Includes checklists and a toolkit. |
| ICAS-GENAI-2026 | ICAS with University of Manchester | "Generative AI and professional judgement in accounting" plus 2026 case studies (case-study page opened; main report snippet-only, Mar 2026) | 2026 | https://icas.com/news-insights-events/documents/generative-ai-and-professional-judgement-in-accounting-2026-case-studies | Judgement and training angle for advisory staff. |
| CPACOM-GENAITOOLKIT-2023 | CPA.com | Generative AI toolkit (seven-step strategy, security checklist, glossary) (opened) | Oct 2023 | https://insidepublicaccounting.com/2023/10/26/cpa-com-launches-generative-ai-toolkit/ | Older than the window; still the base CPA.com resource. |
| CPACOM-ACCELERATOR-2026 | AICPA and CPA.com | 2026 Startup Accelerator cohort focused on AI (snippet-only) | 2026 | https://www.cpa.com/press-releases?year=2026 | Pipeline of AI vendors for the profession. |

Not found: an AICPA-specific 2025-2026 survey on AI in advisory (a Miles Education blog cites a 1,446-leader AICPA & CIMA survey, 88% expect AI to be the most transformative technology but only 8% feel very well prepared, `(unverified)`, snippet-only).

---

## 5. Academic

| Ref | Source | Item | Date | URL | Why it matters |
|---|---|---|---|---|---|
| STANFORD-JAR-2026 | Journal of Accounting Research (Choi, Xie); listed by Stanford GSB (abstract opened) | "Human + AI in Accounting: Early Evidence from the Field", vol 64(3), pp 1333-1373 | Jun 2026 | https://www.gsb.stanford.edu/index%2ephp/node/629989 | Survey of 277 accountants plus platform data on 79 SMEs (200,000+ transaction records): genAI use is linked to productivity gains and a shift from routine data entry; a related version reports a 55% rise in weekly client support among adopters (snippet-only for the 55%). Best peer-reviewed evidence for the CAS module. |
| BRATTLE-INSOL-2025 | INSOL International technical paper with The Brattle Group (Sandy, Klotz, Moore) (PDF opened) | "A Primer on Generative AI and Valuation Considerations for Insolvency Professionals" | Jun 2025 | https://www.brattle.com/wp-content/uploads/2025/07/A-Primer-on-Generative-AI-and-Valuation-Considerations-for-Insolvency-Professionals.pdf | Concerns valuing genAI businesses in insolvency, not AI-assisted valuation, but useful for valuation of AI companies as a service demand. |
| ICAS-MANCHESTER-2026 | ICAS-commissioned report (snippet-only) | "Shaping the Profession: Generative AI and professional judgement in accounting" | Mar 2026 | https://research.aston.ac.uk/en/publications/shaping-the-profession-generative-ai-and-professional-judgement-i/ | Commissioned research rather than peer-reviewed. |
| ICIS-GENAIVALUE-2025 | ICIS 2025 conference paper (snippet-only) | Firm exposure to and readiness for genAI affects market valuation | 2025 | https://aisel.aisnet.org/icis2025/gen_ai/gen_ai/10/ | Tangential (market valuation of firms). |
| FSR-FAULHABER-2025 | Financial Services Review (snippet-only) | Literature review of genAI effects on financial planning and advisor roles (Faulhaber, Chaffin) | 2025 | https://openjournals.libs.uga.edu/fsr/article/download/4017/3449/11845 | Only academic item touching private-client advice. Journal and year unconfirmed. |

Research centres worth checking next (not verified this run): Rutgers Business School's AI and audit work, AAA sections (Information Systems, Forensic and Investigative Accounting), and Georgia State's valuation and forensic programmes (the FVS podcast speaker is at Georgia State). No SSRN working paper on advisory-specific AI was located; the search tool did not return SSRN pages. The Journal of Emerging Technologies in Accounting and Accounting Horizons returned no direct hits.

---

## 6. Firms

### 6.1 Mid-tier, top-100 and PE-backed platforms

| Ref | Firm | Item | Date | URL | Why it matters |
|---|---|---|---|---|---|
| RSM-ASKLUCA-2026 | RSM US | Ask Luca genAI tool inside RSM Luca audit ecosystem, built on assurance manuals (opened) | Jan 8, 2026 | https://rsmus.com/newsroom/2026/rsm-launches-ask-luca.html | Audit-side, but states it lays groundwork for assurance agents. |
| RSM-IMPACT-2026 | RSM US | 2026 Impact Report: $1B multiyear AI and digital core; Microsoft 365 Copilot to ~20,000 professionals; transatlantic platform 23,000+ people, $5B+ revenue (opened) | Aug 25, 2026 | https://rsmus.com/newsroom/2026/rsm-2026-impact-report-highlights.html | Middle-market framing: "invest, enable, lead, scale, deliver" arc. |
| GT-GTAP-2026 | Grant Thornton US | Gtap analytics and automation platform with AI agents across the audit lifecycle (opened) | May 2026 (consulting.us article dated May 11, 2026) | https://www.consulting.us/news/13378/grant-thornton-launches-ai-platform-for-audit-business | States the APS: Grant Thornton LLP does attest, Grant Thornton Advisors does non-attest; New Mountain Capital owner since 2024. |
| GT-1B-2025 | Grant Thornton Advisors | $1B over three years on AI; Copilot to 13,500+ people in 60 offices; AI maturity model (opened) | Sep 2025 | https://www.internationalaccountingbulletin.com/news/grant-thornton-advisors-1bn-ai-integration/ | Scale benchmark for advisory-side investment. |
| GT-CBIZ-2026 | Grant Thornton Advisors, CBIZ (Bloomberg Tax interview, opened via mirror) | $5B CBIZ acquisition (announced Jul 29, 2026 per the interview and search) as a way to fund AI; CEO Jim Peko says "as many as seven tools each quarter" and expects growing demand for AI governance advisory; deal expected to close Q4 2026 | Sep 2, 2026 | https://news.bloomberglaw.com/financial-accounting/grant-thornton-ceo-says-cbiz-merger-is-key-to-unlocking-ai-value | Largest sector deal in a quarter-century per the article; also notes professional-services share prices fell on automation fears earlier in 2026. |
| GT-EAS-2026 | Grant Thornton LLP | Enterprise Assurance Services practice with provisional AIUC-1 accreditation and ISO certification (opened) | Sep 23, 2026 | https://www.grantthornton.com/insights/press-releases/2026/september/gt-launches-first-of-its-kind-enterprise-assurance-services | New service line selling assurance over agentic AI systems; crosses into the assurance archetype. |
| CBIZ-MICROSOFT-2026 | CBIZ with Microsoft | Enterprise AI initiative: agent-native operating platform on Microsoft Foundry, Copilot firmwide, training for 9,500+ people (CPA Practice Advisor article opened) | Apr 21, 2026 | https://www.cpapracticeadvisor.com/2026/04/21/cbiz-expands-ai-partnership-with-microsoft/181999/ | Public-company CAS and advisory provider building agents; stock-market signal in GT-CBIZ-2026. |
| CROWE-KKR-2026 | Crowe | KKR equity investment in Crowe Advisory LLC closed; Crowe LLP stays a licensed CPA attest firm (opened via mirror) | Aug 7, 2026 | https://www.crowe.com/news/crowe-closes-strategic-investment-from-kkr | Cleanest primary statement of the APS split. Press reports of a ~$3B value are from one secondary source `(unverified)`. |
| ACCTODAY-CURRENT-2026 | Current (formerly Crete Professionals Alliance) | Rebrand; positions AI as letting local firms deliver "Fortune 500-caliber advisory" to small businesses; $428M revenue, 228 partners, 1,800+ staff, 67 offices; No. 28 on 2026 Top 100; backed by Thrive Holdings; 2025 plan of $500M to buy firms with OpenAI partnership (opened) | Jun 2, 2026 | https://www.accountingtoday.com/news/crete-professionalls-alliance-rebrands-as-current | The AI-roll-up thesis in a single firm. |
| BDO-AI-2025 | BDO USA | AI strategy backed by $1B+ over five years; Chat BDO (12,000 users, 600,000+ hours saved), agentic Consultative Selling Account Insights, Risk Assessment Coach, DocPro; Chief Data and AI Officer; RAID team (opened) | May 27, 2025 | https://www.bdo.com/insights/press-releases/bdo-usa-unveils-comprehensive-artificial-intelligence-strategy-fusing-practical-innovation | Detailed tool inventory including sales and client-insight agents (advisory-relevant). Older than 12-18 months but the best BDO primary source found. |
| CB-FIELDGUIDE-2026 | Cherry Bekaert | Fieldguide as strategic AI partner across financial audit, internal audit, SOC and Risk and Cybersecurity (opened) | Jun 3, 2026 | https://www.cbh.com/newsroom/cherry-bekaert-expands-ai-audit-with-fieldguide/ | Internal-audit and SOC outsourcing delivered on an agentic platform. |
| APRIO-FIELDGUIDE-2026 | Aprio | Co-developing role-specific agents across the audit lifecycle with Fieldguide (opened) | Aug 5, 2026 | https://www.cpapracticeadvisor.com/?p=188025 | Firms building their own agents on a vendor platform. |
| CITRIN-TELLEN-2026 | Citrin Cooperman | Investment in Tellen, AI-native platform for accounting practices; multi-year audit-tools partnership (opened) | May 20, 2026 | https://finance.yahoo.com/sectors/technology/articles/citrin-cooperman-advisors-invests-tellen-144822980.html | Firm-as-investor model. Other Citrin AI items (Anthropic work, Intuit Enterprise Suite offering) are snippet-only. |
| FORVIS-QOE-2026 | Forvis Mazars US (Mike Laurie, Transaction Advisory) | "Quality of Earnings & Due Diligence in an AI World" (opened) | Sep 8, 2026 | https://www.forvismazars.us/forsights/2026/09/quality-of-earnings-due-diligence-in-an-ai-world | Rare firm-authored view of AI in QoE: speed (TB mapping, first-draft schedules, anomaly detection), depth (SKU-level, customer and vendor analysis), talent (risk of thin work and junior-pipeline depletion). Warns AI is also enabling lower-quality, cheaper QoE products. |
| ACCTODAY-CASKEYS-2026 | Withum (Jim Bourke) | Advisory built on CAS; $70M CAS revenue in seven years; AI for variance explanations and client dashboards; expects tax to be largely automated (opened) | May 22, 2026 | https://www.accountingtoday.com/news/cas-delivers-the-keys-to-the-kingdom | Clearest practitioner statement of the "CAS to continuous advisory" path. |
| KAUFMAN-FO-2026 | Kaufman Rossin | Family-office director on AI for operations while relationships stay human-led (opened) | 2026 | https://kaufmanrossin.com/news/ai-adoption-in-family-offices/ | Private-client positioning. |
| PKF-ASSETA-2026 | PKF O'Connor Davies | Collaboration with Asseta AI, an AI platform for multi-entity family offices (snippet-only; BusinessWire page unavailable) | Mar 26, 2026 | https://www.businesswire.com/news/home/20260326796176/en/PKF-OConnor-Davies-Announces-Collaboration-with-Asseta-AI-to-Support-Family-Office-Modernization | Family-office accounting and reporting delivered on an AI platform. |
| JSHELD-AIEXPERT-2026 | J.S. Held (forensic and consulting) | "Expertise in the Age of Algorithms: Trust and Transparency in AI-Assisted Litigation" (opened via mirror) | 2026 | https://jsheld.com/insights/articles/expertise-in-the-age-of-algorithms-trust-and-transparency-in-ai-assisted-litigation | Forensic firm guidance on validating AI-assisted analyses and supervising AI-using experts; covers Rule 707, deepfakes and sanctions. |

Not covered or not verified: Baker Tilly, Wipfli and Cherry Bekaert client-accounting AI specifics (only the Fieldguide item for Cherry Bekaert); Eide Bailly PE deal (late June 2026 per a snippet of a Going Concern listing, `(unverified)`).

### 6.2 Big Four and global networks (direction only)

| Ref | Item | Date | Status |
|---|---|---|---|
| KPMG-AIFINANCE-2026 | Global AI in Finance: The Decision Advantage; n=1,013 senior finance leaders, 20 countries, 13 sectors; fieldwork Mar 2026 (press release opened) | May 11, 2026 | https://kpmg.com/xx/en/media/press-releases/2026/05/ai-adoption-in-finance-doubles-but-assurance-readiness-determines-who-wins.html |
| DELOITTE-AGENTS-2026 | Deloitte autonomous agents for audit data work announced June 2026 (cited inside GT-CBIZ-2026; Bloomberg headline only) | Jun 2026 | secondary only |
| EY-AGENTIC-2026 | EY agentic AI in assurance, full coverage by 2028 (aggregator brief citing a DXC release) | Apr 2026 | snippet-only `(unverified)` |
| PWC-FY26-2026 | PwC global revenue $60.2B FY2026, headline on CPA Practice Advisor | Oct 19, 2026 | seen as a headline on an opened page; not read |

---

## 7. Vendors

| Ref | Vendor | Item | Date | URL | Why it matters |
|---|---|---|---|---|---|
| BASIS-SERIESB-2026 | Basis | $100M Series B led by Accel with GV, at $1.15B; $138M raised total; claims use by ~30% of the top 25 firms and ~20% of the top 150; long-horizon agents across accounting, tax, audit (CPA Practice Advisor opened) | Feb 24, 2026 | https://www.cpapracticeadvisor.com/2026/02/24/basis-raises-100-million-to-deploy-ai-agents-for-accounting-firms/178759/ | Platform for firm-side agents. Adoption figures are company claims. |
| FIELDGUIDE-SERIESC-2026 | Fieldguide | $75M Series C led by Goldman Sachs Alternatives at $700M; $125M total; agents across audit and advisory lifecycle; KPMG and Anders named as customers (CPA Practice Advisor opened) | Feb 2, 2026 | https://www.cpapracticeadvisor.com/2026/02/02/fieldguide-raises-75m-series-c-round-to-boost-audit-and-advisory-firms-agentic-ai-capabilities/177323 | Core vendor for risk-advisory (SOC, internal audit, SOX); "half of top 100 firms" is a single-source claim (snippet-only). |
| RILLET-SERIESB-2025 | Rillet | $70M Series B (a16z, ICONIQ); AI-native ERP for mid-market; 4-6 week implementations (company blog opened) | Aug 2025; page updated Aug 25, 2026 | https://rillet.com/blog/fundraise-announcement/ | ERP-advisory and implementation partner opportunity for the consulting-fpa module. |
| UKU-BOTKEEPER-2026 | Botkeeper | Announced closure Feb 2026; platform reportedly acquired by Xendoo (vendor comparison blog, opened) | Updated Oct 17, 2026 | https://getuku.com/articles/botkeeper-alternatives/ | Cautionary signal for CAS tech-stack risk. Vendor-authored, single source `(unverified)`. |
| INTUIT-ACCTTECH-2026 | Intuit QuickBooks | 2026 Accountant Technology Survey (see section 9) and Intuit Accountant Suite and agents (agents Jul 1, 2025; Intelligence and Accountant Suite Oct 2025, snippet-only; later suite update noted in ACCOUNTEX-2026) | 2025-2026 | https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807 | The dominant SMB ledger vendor is shipping agents; a CAS firm's tooling baseline. |
| ACCOUNTEX-2026 | Sage and Xero | Sage Intacct Advisory update for outsourcing and advisory; Xero's natural-language agent builder and Claude integration (Xero launch May 12, 2026 per article) (opened) | 2026 | https://financialaccountant.co.uk/blog/accountex-london-2026-product-roundup/ | Platform vendors moving into agents; relevant to mid-market CAS on Intacct. |
| KARBON-AISTATE-2026 | Karbon | Practice-management vendor; State of AI report (see section 9) | Jan 20, 2026 | https://karbonhq.com/resources/state-of-ai-accounting-2026 | Vendor sponsors both the report and ENGAGE sessions. |
| CPAPA-AGENTSCLOSE-2026 | BlackLine, FloQast, Microsoft, Workday | BlackLine Verity Prepare agents GA Jul 2026; FloQast close agents Mar 2025; Microsoft reconciliation agent in preview; Workday close agent announced for 2026 (article opened) | Aug 13, 2026 | https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/ | The client-side close agents that CAS and controllership teams must govern; five controls checklist. |
| MINDBRIDGE-ENGAGE-2026 | MindBridge | Full-population risk analysis (see section 2) | Jun 2026 | https://www.mindbridge.ai/events/2026-aicpa-engage/ | Audit and risk analytics vendor. |
| TULLION-DCPA-2026 | Trullion | Exhibiting at Digital CPA 2026; "auditable AI" positioning (page opened via mirror) | 2026 | https://trullion.com/events/digital-cpa-2026/ | Lease and revenue accounting vendor aiming at CFO and audit workflows. |
| QOE-VENDORS-2026 | Finsider, QoEAgent, Shepi (QoE automation), ChatFin and Valutico (blog content) | Claims: 100% transaction coverage, proof-of-cash reconciliation, 60-80% faster diligence (snippet-only; all vendor marketing) | 2026 | https://www.barchart.com/story/news/35038707/quality-of-earnings-software-launched-by-finsider-ai-ai-powered-qoe-reports-automation-platform-targets-60-faster-due-diligence-for-ma-deals | Entry-level tools aimed at small buyers and searchers; treat figures as unverified. |
| ASSETA-PKF-2026 | Asseta AI | Family-office platform (see PKF-ASSETA-2026; snippet-only) | Mar 2026 | https://www.businesswire.com/news/home/20260326796176/en/PKF-OConnor-Davies-Announces-Collaboration-with-Asseta-AI-to-Support-Family-Office-Modernization | Private-client tooling. |
| DIGITS-PILOT-PUZZLE-2026 | Digits, Pilot, Puzzle | Agentic general ledger and bank-reconciliation features; Pilot "AI Accountant"; Digits outcome-based pricing at 95% zero-touch (rework.com comparison; single source) (snippet-only) | 2026 | https://resources.rework.com/tools/ai-agents/best-ai-agents-for-bookkeeping-2026 | Candidate AI-native competitors to firm-delivered bookkeeping. Pricing claim `(unverified)`. |

Not found: vendor launches for forensic analytics (for example eDiscovery and investigation platforms), valuation-specific AI products from named valuation firms (Stout, Kroll, Houlihan Lokey), and mid-market QoE tools from established diligence vendors. Treat these as gaps.

---

## 8. Press, podcasts & communities

| Ref | Outlet | Item | Date | URL | Note |
|---|---|---|---|---|---|
| CPAPA-TECHLAB-2026 | CPA Practice Advisor, Accounting Technology Lab podcast | ENGAGE recap (see section 2) (opened) | Jul 2026 | https://www.cpapracticeadvisor.com/podcasts/thought-leader-40-under-40-aicpa-think-tank-accounting-technology-lab-podcast-july-2026/ | Weekly practitioner tech commentary (Randy Johnston, Brian Tankersley). |
| ACCTODAY-NEWS-2026 | Accounting Today | CAS keys (May 2026), Current rebrand (Jun 2026), valuation framework (Oct 2026); Top 100 2026 coverage (snippet-only) | 2026 | https://www.accountingtoday.com/news/cas-delivers-the-keys-to-the-kingdom | Main US trade press and ranking publisher. |
| WOODARD-TWR-2025 | The Woodard Report podcast | Episode 120: How CAS and AI are reshaping the Top 100 (Joe Woodard with Dan Hood). 2025 Top 100 growth 4.89%, with big-firm slowdown attributed largely to advisory declines; smaller firms 14-15% (opened) | Apr 30, 2025 | https://report.woodard.com/articles/twr-podcast-episode-120-how-cas-and-ai-are-reshaping-the-top-100-firms-oaiwr-twrpod-bllwr | Older than window but good growth context. Episode 163 (Mar 18, 2026) on AI scams and platform CAS models is snippet-only. |
| JOFA-HOOD-2026 | Journal of Accountancy podcast | Tom Hood on AI, hybrid work, 2026 themes (opened) | Jan 2026 | see section 2 | Professional-body voice. |
| BVR-BVWIRE-2026 | BVWire (Business Valuation Resources) | Daily valuation-profession news, with AI items on the AICPA guidelines, IVS disclosure, report QC agents (opened via mirror) | 2025-2026 | https://www.bvresources.com/articles/bvwire/ai-agents-as-a-quality-control-layer-for-valuation-reports | Best trade source for valuation; some pages block curl (use mirror). |
| CPATRENDLINES-2026 | CPA Trendlines | Busy Season Barometer: CAS-heavy firms more likely to be considering AI tech (66.7% vs 34.0% per snippet); CAS accountants handle half the book for ten times the fees where CAS is the leading fee generator per chart caption (page opened but article paywalled) | Jan 25, 2026 | https://cpatrendlines.com/2026/01/25/busy-season-2026-the-year-cas-firms-take-the-lea | The 66.7/34.0 figure is snippet-only. |
| CFODIVE-FRACTIONAL-2026 | CFO Dive | "Fractional CFOs see demand surge in AI age" (opened) | Aug 6, 2026 | https://www.cfodive.com/news/fractional-cfos-see-demand-surge-ai-age/827264/ | Cites Business Talent Group: interim C-suite requests up 151% since 2021, interim CFO demand up 14% year on year. |
| FCN-ACFE-2026 | Fraud Conference News | ACFE keynote preview (opened) | 2026 | see section 2 | Event coverage. |
| GOINGCONCERN-2026 | Going Concern | Layoff, PE and AI items (May-Jun 2026), including KPMG plan to hand routine testing to AI (Apr 2026) and AI-fabricated citations in firm reports (snippet-only) | 2026 | https://www.goingconcern.com/category/anr/section/56/0/ | Irreverent but fast-moving; headlines only read. Verify before use. |
| INSIDEPA-2026 | INSIDE Public Accounting | IPA Top 100 / IPA 500 ranking coverage and M&A feed (page opened: M&A and PE headlines Oct 2026; firm release listings snippet-only) | 2026 | https://insidepublicaccounting.com/?p=84787 | Service-line and PE tracking; ranking detail not retrieved. |
| CASMINUTE-2026 | CAS Minute podcast (Roman Villard, CPA) | Episodes on QuickBooks MCP server and shrinking transactional accounting (snippet-only) | Mar 2026 | https://castbox.fm/channel/6233380 | Practitioner community voice. |
| INSIGHTFUL-2026 | Insightful Accountant | Intuit and tech coverage, Intuit Connect 2026 preview (snippet-only) | 2026 | https://insightfulaccountant.com/events/intuit-connect-2026/ | Intuit-ecosystem press. |
| KARBONMAG-2026 | Karbon Magazine | Practitioner-facing AI and PE pieces (the PE and IESBA article is snippet-only) | 2026 | https://karbonhq.com/resources/private-equity-accounting-ethics-review/ | Vendor-run but widely read in the CAS community. |

Communities and newsletters to check later (not opened): Woodard's Scaling New Heights, CPA Trendlines community, AICPA FVS section podcast, the IIA AI Knowledge Center, ACFE chapters.

---

## 9. Surveys & benchmarks

| Ref | Survey | Sample and date | Key findings (as reported) | URL |
|---|---|---|---|---|
| KARBON-AISTATE-2026 | Karbon State of AI in Accounting 2026 | n=593 professionals, six continents, released Jan 20, 2026; selection bias toward Karbon users acknowledged | 98% of firms use AI, most daily; avg 60 min/day saved per employee (+7% year on year); fewer than half invest in training; 21% have an AI policy or strategy; 21-50 staff firms most energized | https://karbonhq.com/resources/state-of-ai-accounting-2026 |
| INTUIT-ACCTTECH-2026 | Intuit QuickBooks 2026 Accountant Technology Survey (reported by CPA Practice Advisor) | n=725 US accounting and bookkeeping professionals, May 2026 | 88% use AI for at least one client service; 86% for firm operations; only 30% say AI is embedded as default, 54% situational; 77% say the gap between embedded and occasional firms is widening; 86% expect AI to expand advisory capacity; manual data cleanup the top advisory blocker (30%) | https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807 |
| RAMP-CALCPA-2026 | Ramp with CalCPA, Benchmarking the Modern CPA Firm 2026 (Accounting Today landing page opened) | 400+ California accounting professionals, 2026 | 56% use genAI, only 10% integrated across operations; top uses client communication (50%), document review (47%), tax research (46%); top barrier training time (31%); data security the top client-facing concern (39%) | https://www.accountingtoday.com/report/benchmarking-the-modern-cpa-firm-2026 |
| CPACOM-BLUEJ-2026 | Blue J and CPA.com AI Tax Research Outlook | n>1,000 US tax professionals, Jun 8, 2026 | 60% use AI for tax research weekly (33% in 2025); advisory projects the top use (44%); 84% say AI saves time; 69% expect value-based, hybrid or fixed fees | https://www.cpa.com/news/blue-j-and-cpacom-survey-finds-ai-adoption-among-tax-firms-has-nearly-doubled-one-year |
| CPACOM-CASBENCH-2026 | CAS Benchmark Survey (biennial) | 2024 edition 200+ respondents; 2026 report due Dec 2026 | 2024: median growth 17% (JofA); technology adoption is a benchmarked area | https://cpa.com/cas-benchmark-survey |
| KPMG-AIFINANCE-2026 | KPMG Global AI in Finance | n=1,013, Mar 2026 | Active use 30% to 75% since 2024; 71% say AI meets or exceeds ROI expectations; assurance-ready organisations see more error reduction (33% vs 6%) and scaling confidence (42% vs 14%); data quality top barrier (36%); sample over-weights tech and financial services (per secondary summary) | https://kpmg.com/xx/en/media/press-releases/2026/05/ai-adoption-in-finance-doubles-but-assurance-readiness-determines-who-wins.html |
| TR-FOP-2026 | Thomson Reuters Institute Future of Professionals 2026 (Spanish-language coverage opened) | n=1,816, 62 countries, Mar-Apr 2026 | 74% use AI weekly; 91% say their organisation is not capturing AI's potential; Thomson Reuters headline on up to $143B US client revenue at risk (snippet-only) | https://mercado.com.ar/ruta-digital/future-of-professionals-2026-thomson-reuters-alerta-por-brecha-de-ia-en-firmas |
| ACFE-TECHBENCH-2026 | ACFE and SAS Anti-Fraud Technology Benchmarking Report | n=713, eight regions, 2026 | 7% well prepared for AI-fuelled fraud; 25% use AI/ML; 16% genAI as anti-fraud tool, 58% plan to; 18% test for bias, 6% fully confident in explaining models | https://www.sas.com/en_us/news/press-releases/2026/march/acfe-anti-fraud-technology-study-deepfakes.html |
| ACCA-ETHICS-2026 | ACCA Navigating ethics for trust | n=1,178, 135 countries, Oct 14, 2026 | 61% rank AI as top ethical challenge (32% in 2024); 72% say AI tools improve work quality and efficiency (snippet-only) | https://www.accaglobal.com/policy-and-insights/reports/2026/navigating-ethics-for-trust |
| JPM-FAMILYOFFICE-2026 | J.P. Morgan Global Family Office Report 2026 (secondary summary opened) | n=333 family offices, 30 countries, Feb 4, 2026 | 65% plan to prioritise AI investments; 86% lack succession plans; 80% outsource some portfolio management (secondary source) | https://letsdatascience.com/news/family-offices-prioritize-ai-despite-limited-venture-exposur-84e00512 |
| WK-FUTUREREADY-2025 | Wolters Kluwer Future Ready Accountant 2025 (snippet-only) | n>2,300, early 2025 | 27% of firms using genAI in workflows; only 25% have AI policies; firms with policies view AI more positively | https://www.cpapracticeadvisor.com/2025/01/14/report-highlights-key-trends-in-tax-accounting-for-2025/154511/ |
| ACCTODAY-TOP100-2026 | Accounting Today Top 100 Firms 2026 (snippet-only) | 88 responding firms | CAS the top growth niche (85% reporting growth), attest second | https://www.accountingtoday.com/news/cas-delivers-the-keys-to-the-kingdom |
| VSCPA-AISURVEY-2026 | VSCPA 2026 AI survey executive summary (snippet-only) | 144 responses from 8,875 members | Thin sample; do not use for benchmarking | https://www.vscpa.com/storage/assets/PDFs%20and%20Docs/2026%20VSCPA%20AI%20Survey%20Executive%20Summary.docx |
| IVSC-PULSE-2026 | IVSC and 73 Strings sentiment tracker | open survey, May 2026 | results pending | https://ivsc.org/the-valuation-pulse-ai-technology-in-valuation-sentiment-tracker/ |

Caveat: vendor-sponsored surveys (Karbon, Intuit, Ramp, Blue J) draw from customer bases that skew toward adopters. None provides adoption data specific to transaction advisory, forensic or private-client services.

---

## 10. Module check

**Verdict:** the seven modules are close to how practitioners divide the work, but four changes are recommended. The practitioner bodies are: AICPA and CPA.com for CAS; the AICPA FVS section, which combines forensic with valuation (and NACVA's conference pairs valuation with financial litigation); ACFE for fraud; IIA for internal audit; ACG for deal professionals; and, for private clients, the AICPA PFP and wealth-advisor communities (not examined).

| Proposed module | Practitioner home found | Evidence density | Recommendation |
|---|---|---|---|
| client-accounting-services | CPA.com and AICPA PCPS CAS benchmark; Digital CPA; Accounting Today CAS Summit; Woodard; Karbon | **High** | **Keep.** Anchor module. Keep fractional CFO and payroll here, since the CAS benchmark and firm practice treat them as CAS service offerings. Treat bill pay as a feature of the delivery stack, not a separate topic. |
| transaction-advisory | ACG (DealMAX); firm transaction-advisory groups (Forvis Mazars) | **Low** (one firm article, vendor marketing, attendance recap) | **Merge for the deep dive** with valuation into a single "deals-and-valuation" research package, because QoE, PPA and fairness work share data, buyers and tools. Keep the two as separate module labels if downstream structure needs it. |
| valuation | AICPA FVS section; NACVA; IVSC; ASA; BVR | **Medium** (strong on standards and guidance, weak on firm case studies) | **Keep as its own module** because the standards track is distinctive (IVSC ED, AICPA guidelines, Valuation Performance Framework). Run in one wave with forensic (below). |
| forensic-disputes | AICPA FVS section (forensic and valuation are one section and one conference); ACFE; courts | **Medium** | **Keep, but pair with valuation under an "FVS" umbrella** for sourcing (same conference, same podcast, same committee). Add the evidence-rule thread (Rule 707) and deepfake risk. Some investigations work (fraud examination) belongs to the risk side. |
| risk-advisory | IIA; ACFE (partly); Protiviti, KPMG, Fieldguide ecosystem | **High** | **Keep and split off an emerging topic:** "AI governance and assurance over client AI" (GT-EAS-2026, KPMG-AIFINANCE-2026, COSO, AIUC-1). This straddles the assurance archetype; research it under risk-advisory but flag the boundary. Internal-audit outsourcing and SOX readiness are the core; cyber and IT risk advisory has almost no AI-specific public evidence found. |
| consulting-fpa | Mixed: CPA.com CAS (CFO services), ERP vendor ecosystems, FP&A software vendors | **Low-Medium** (vendors, CFO Dive, KPMG survey) | **Narrow it** to FP&A, performance improvement and ERP/technology advisory, with fractional CFO left in CAS. Evidence is mostly vendor content; combine into one deep dive. |
| private-client | Wealth and family-office practitioners; PKF, Kaufman Rossin; J.P. Morgan | **Low** | **Keep as one combined deep dive.** Tax and estate technical work belongs to the tax archetype; investment advice sits in regulated RIA territory (SEC). Confine this module to family-office accounting and reporting, succession advisory and the client-experience angle. |

**Belongs elsewhere:**
- AI assurance (AIUC-1, SOC for AI) and audit-side AI (Gtap, Ask Luca, Fieldguide for financial audit, FRC and AICPA audit guidance) belong to the assurance archetype. Reference them from risk-advisory only where the service is sold to non-audit clients.
- Alternative practice structures, PE ownership, firm consolidation and talent models (IESBA, PEEC, Crowe, Current, GT-CBIZ) belong to professional-services (firm operations). Advisory researchers need a short briefing note on them because they set which advisory services are possible for attest clients.
- Tax technical research (Blue J) belongs to tax; use it only for the pricing and advisory-time-shift signal.

**New cross-cutting threads to add to every module:** (1) pricing and fee models, (2) independence and attest-client restrictions, (3) AI governance and client-data confidentiality, (4) junior-talent pipeline (Forvis Mazars flags depletion of junior ranks; Karbon reports graduates favour AI-using firms).

---

## 11. Journey-stage markers

Markers are drawn from the survey and firm evidence above; they are working hypotheses for later researchers to test.

| Stage | Observable markers in advisory and outsourced services |
|---|---|
| **Curious** | Staff use public chatbots individually with no firm policy (only 21% of firms have an AI policy or strategy; KARBON-AISTATE-2026). Leaders attend ENGAGE or DCPA sessions "to get the language" for client conversations (KARBON-ENGAGE-2026). No client deliverable changed; fee model unchanged. |
| **Experimenting** | Approved tools for drafting and research, and AI use is "situational": 54% of firms in INTUIT-ACCTTECH-2026. Pilots on a single task such as trial-balance mapping, variance commentary, or a dashboard. Pilots are tracked informally. Genai use without integration: 56% use, 10% integrated (RAMP-CALCPA-2026). |
| **Adopting** | Named AI owner and written policy; training budget; tools wired into the ledger and practice-management stack (QuickBooks agents, Xero, Karbon). First-pass work shifts to AI with review gates (Forvis Mazars describes AI-assisted trial-balance mapping and first-draft schedules; FORVIS-QOE-2026). Time savings measured (~60 minutes per employee per day in KARBON-AISTATE-2026). Some clients ask CPAs about their own AI tools and risks. |
| **Scaling** | Firm-built or co-built agents embedded in repeatable workflows across practices (Aprio with Fieldguide; Cherry Bekaert consolidating SOC, audit and IA on one platform; BDO's agentic client-insight tools). Firmwide Copilot rollouts (RSM ~20,000; Grant Thornton 13,500+). Clients receive continuous dashboards and variance explanations rather than periodic packages (ACCTODAY-CASKEYS-2026). Pricing experiments with fixed or value-based fees (69% expecting this in CPACOM-BLUEJ-2026). Governance controls such as agent inventory with named owner and replayable evidence (CPAPA-AGENTSCLOSE-2026). |
| **AI-native** | Operating model designed around agents with human review, not retrofitted: PE-backed or venture-backed platforms (Current, Thrive Holdings, OpenAI partnership) that sell strategic advisory to businesses historically served only transactionally (ACCTODAY-CURRENT-2026); firms selling assurance or governance over clients' agents (GT-EAS-2026); outcome-based pricing tied to zero-touch transaction rates (Digits claim, `(unverified)`). Headcount and leverage model visibly different from the pyramid; junior roles redefined. |

---

## 12. Frontier signals (next 12-36 months)

Each signal is dated and sourced; classification in brackets.

1. **Feb 2, 2026. Agentic audit and advisory platforms attract growth capital.** Fieldguide raised $75M at $700M, and says its agents work as part of engagement teams. [agentic, vendor] FIELDGUIDE-SERIESC-2026.
2. **Feb 24, 2026. Firm-side agents for tax, audit and client services at scale.** Basis raised $100M at a reported $1.15B valuation and claims use at about 30% of the top 25 firms (company claim). [agentic, vendor] BASIS-SERIESB-2026.
3. **Feb 2026. First-generation AI bookkeeping vendor fails.** Botkeeper closed and was reportedly acquired by Xendoo. [business model, vendor risk] UKU-BOTKEEPER-2026 `(unverified)`.
4. **Mar 26, 2026. IESBA to develop non-authoritative technology and AI guidance, and a PE workstream.** [regulatory] IESBA-PE-2026.
5. **Mar 30, 2026. First regulator guidance on generative and agentic AI in audit (UK FRC).** Likely template for other regulators, including how firms evidence confidence in AI output. [regulatory] FRC-GENAI-2026.
6. **Jan-Apr 2026 consultation; final text Jan 2027; effective Jan 31, 2028. IVS would require disclosure of significant AI use in valuation scope and reports.** [regulatory, valuation] IVSC-IVSED-2026.
7. **Apr 21, 2026. CBIZ builds an agent-native operating platform on Microsoft Foundry.** [agentic, firm] CBIZ-MICROSOFT-2026.
8. **May 11, 2026. Finance functions are deploying faster than they can assure.** Active AI use in finance 30% to 75%; assurance-ready organisations report better results; demand for controls design and AI governance advisory follows. [business model, risk advisory] KPMG-AIFINANCE-2026; BlackLine Verity Prepare agents generally available Jul 2026 in CPAPA-AGENTSCLOSE-2026.
9. **Jun 2, 2026. AI as the basis for a venture-backed advisory roll-up.** Current (ex-Crete) positions AI as the reason local firms can offer "Fortune 500-caliber" advisory. [business model] ACCTODAY-CURRENT-2026.
10. **Jun 24, 2026. IRS OPR AI guidance applies existing due diligence and competence duties to AI.** Commentators expect scrutiny of fees if AI shortens work. [regulatory, pricing] IRS-OPR-2026.
11. **Jun 8, 2026. Pricing shifts.** 69% of surveyed tax professionals expect value-based, hybrid or fixed fees as AI commoditises routine knowledge. [pricing] CPACOM-BLUEJ-2026.
12. **Jul 29, 2026 announced; close expected Q4 2026. Grant Thornton Advisors to acquire CBIZ for $5B.** CEO links scale to AI investment and expects AI governance demand; markets had sold off professional-services stocks on automation fears earlier in 2026. [business model, consolidation] GT-CBIZ-2026.
13. **Aug 7, 2026. Crowe closes KKR investment in its non-attest arm.** The APS split is becoming the standard structure for outside capital. [business model, regulatory] CROWE-KKR-2026; the AICPA APS exposure draft in AICPA-PEEC-APS-2025.
14. **Sep 8, 2026. Quality-of-earnings work faster and deeper with AI, but cheap, thin products proliferate.** Forvis Mazars expects a talent gap if junior ranks are cut. [agentic, pricing, talent] FORVIS-QOE-2026.
15. **Sep 23, 2026. AI assurance becomes a service line.** Grant Thornton launches Enterprise Assurance Services with provisional AIUC-1 accreditation. [new service] GT-EAS-2026.
16. **Oct 13, 2026. AICPA releases AI auditor practice aid and a proposed Valuation Performance Framework.** Expect further AI guidance, per the AICPA. [regulatory] AICPA-AUDITAID-2026; ACCTODAY-VPF-2026.
17. **Mar 2026 survey. Fraud risk ahead of defenses.** Only 7% are well prepared for AI-fuelled fraud; deepfake and genAI document forgery lead; 58% plan to adopt genAI in anti-fraud work. Points to growth in forensic and fraud-risk advisory demand. [demand] ACFE-TECHBENCH-2026.
18. **2026. Evidence admissibility.** Proposed FRE 707 on machine-generated evidence returned for study in June 2026 per secondary sources; expert-witness firms are already advising on validation and disclosure. [regulatory, forensic] STEPTOE-FRE707-2026 and JSHELD-AIEXPERT-2026 (June status `(unverified)`).
19. **Aug 2026. Fractional and interim finance leadership demand rises, linked to AI.** Interim CFO demand up 14% year on year per Business Talent Group (cited in CFO Dive). [demand] CFODIVE-FRACTIONAL-2026.

---

## 13. Research leads per module

**client-accounting-services** (High evidence)
1. 2026 CAS Benchmark Survey report (due December 2026) and the 2024 report; JofA CAS coverage. CPACOM-CASBENCH-2026, JOFA-CASTIPS-2025.
2. Digital CPA 2026 agenda (Dec 6-9) and 2025 session recordings; CPA.com CAS Professional Services (Kim Blascoe).
3. Accounting Today Top 100 2026 CAS data; CAS Summit sessions "CAS 3.0" and "Deepening Adoption of AI and Automation". ACCTODAY-CASSUMMIT-2026.
4. Withum (Jim Bourke), CohnReznick (Kane Polakoff), Cherry Bekaert (Dixie McCurley) CAS case studies. ACCTODAY-CASKEYS-2026.
5. Platform vendors' agents (Intuit, Xero, Sage Intacct Advisory, Karbon) and failure modes (Botkeeper). ACCOUNTEX-2026, UKU-BOTKEEPER-2026.
6. Stanford/JAR paper (Choi and Xie) for evidence on SME bookkeeping productivity. STANFORD-JAR-2026.
7. Pricing: Digits outcome-based pricing claim; CAS fee models in the benchmark.

**transaction-advisory** (Low; combine with valuation)
1. Forvis Mazars FORsights series (including the PE buy-side AI article referenced there) and other firm transaction-advisory insight pages. FORVIS-QOE-2026.
2. ACG DealMAX 2026 session list and speakers (agenda on acg.org); ACG chapter events with AI sessions.
3. Big Four deal groups: EY-Parthenon AI due diligence (a service line, per its site and job postings, snippet-only), Deloitte, KPMG, PwC transaction-services AI announcements.
4. QoE tool vendors (Finsider, QoEAgent, Shepi, DealRoom/Datasite-type platforms) with independent reviews; search for practitioner critiques.
5. Practitioner forums for QoE (CPA firm deal teams, search-fund communities such as SearchFunder, where QoEAgent was discussed).
6. PE-backed platform playbooks: how PE sponsors price AI-enabled diligence.

**valuation** (Medium)
1. IVSC exposure draft text and responses, final IVS (Jan 2027); IVSC Valuation Pulse results. IVSC-IVSED-2026, IVSC-PULSE-2026.
2. AICPA FVS Executive Committee AI guidelines and BVR Leadership Council AI perspective paper. BVR-AICPAAIGUIDE-2025.
3. Valuation Performance Framework exposure draft (due Dec 22, 2026). ACCTODAY-VPF-2026.
4. AICPA FVS Conference Nov 2026 session list (AI, technology and advanced data topic); NACVA 2026 sessions. AICPA-FVS-2026, BVR-NACVA-2026.
5. BVWire and Business Valuation Update AI coverage; AICPA FVS podcast episodes (report QC agents, IVS disclosure). BVR-AICPAREPORT-2026.
6. Valuation firms' published views (Stout, Kroll, Houlihan Lokey, Chaffe, Mercer Capital) on AI-assisted DCF, comparable screening and PPA.
7. ValuAsia Connect 2026 materials and IVSC Perspectives Paper "Navigating the Rise of AI in Valuation" (page blocked; snippet-only).

**forensic-disputes** (Medium)
1. ACFE-TECHBENCH-2026 full PDF; ACFE Global Fraud Conference 2026 agenda and recordings; Canada and Asia-Pacific session lists. ACFE-CANADA-2026, ACFE-APAC-2026.
2. Rule 707 committee materials on uscourts.gov and law-firm tracking; expert-witness case law on AI use. STEPTOE-FRE707-2026.
3. J.S. Held, Kroll, Alvarez & Marsal, FTI forensic AI publications. JSHELD-AIEXPERT-2026.
4. AICPA FVS "AI Right Now for Forensic Accounting Professionals" webcast and 2025 deepfake session. AICPA-FVS-2026.
5. ACFE and AICPA investigation tooling coverage (document review, anomaly detection); E-discovery vendors (Relativity, Reveal) for AI adoption, none opened.
6. Fraud-risk advisory from audit firms (AI washing, deepfake controls). ACFE-APAC-2026.

**risk-advisory** (High)
1. IIA AI Auditing Framework and Knowledge Center, GAM 2027 (Mar 22-24, 2027, per snippet), IIA International Conference 2026 sessions. IIA-AIKC-2026, IIA-GAM-2026, IIA-ICONF-2026.
2. KPMG, Protiviti, Deloitte SOX and internal-audit AI whitepapers (KPMG "agentic shift in SOX compliance", Protiviti SOX survey; both snippet-only).
3. Fieldguide customer firms (Cherry Bekaert, Aprio) and Fieldguide's product claims (agents for SOC, IA, risk assessments). CB-FIELDGUIDE-2026, APRIO-FIELDGUIDE-2026.
4. COSO Feb 2026 guidance on internal control over generative AI; five-controls checklist. COSO-GENAI-2026, CPAPA-AGENTSCLOSE-2026.
5. AI assurance: Grant Thornton EAS, AIUC-1, KPMG AI Assurance (Sep 2025, snippet-only), CPA Canada and AICPA AI assurance report (Jul 2025, snippet-only). GT-EAS-2026.
6. AICPA practice aid and FRC guidance as model for how outsourced IA or SOX teams document AI use. AICPA-AUDITAID-2026, FRC-GENAI-2026.

**consulting-fpa** (Low-Medium)
1. KPMG Global AI in Finance full report and sector cuts. KPMG-AIFINANCE-2026.
2. CFO Dive and BTG High-End Independent Talent Report on fractional and interim demand. CFODIVE-FRACTIONAL-2026.
3. FP&A and ERP vendors: Rillet, Fresh FP&A (speaker at ENGAGE), Pigment, Cube, Sage Intacct Advisory, Microsoft Dynamics reconciliation agent. RILLET-SERIESB-2025, KARBON-ENGAGE-2026.
4. Deloitte CFO Signals Q2 2026 (cited by a vendor blog as 44% using AI for planning and budgeting; unverified; fetch primary).
5. ENGAGE sessions: "The tech-enabled adviser" (Armanino, Wiss) and "AI workshop: Getting technical in AI". KARBON-ENGAGE-2026.
6. Case studies of firms packaging FP&A as a subscription alongside CAS (Withum, Armanino, Cherry Bekaert).

**private-client** (Low; one combined deep dive)
1. PKF O'Connor Davies insights and Asseta AI collaboration; Kaufman Rossin family-office pieces. PKF-ASSETA-2026, KAUFMAN-FO-2026.
2. J.P. Morgan 2026 Global Family Office Report (primary PDF) and other family-office surveys (UBS, Campden). JPM-FAMILYOFFICE-2026.
3. IRS OPR AI guidance as it applies to estate and tax planning advice. IRS-OPR-2026.
4. SEC FY2026 examination priorities (primary) for wealth affiliates. SEC-EXAMPRI-FY2026.
5. Faulhaber and Chaffin literature review and wealth-planning software vendors. FSR-FAULHABER-2025.
6. AICPA PFP section materials (not reached).

---

## 14. Gaps

**Blocked or paywalled (not read):**
- Official ENGAGE 2026 session catalogue (agenda.aicpastore.com returned 403); Wolters Kluwer ENGAGE page (empty response).
- Digital CPA 2026 agenda; AICPA FVS Conference 2026 agenda and speakers pages (Agenda path returned 404; Program/Agenda path not tried); ACFE Global Fraud Conference 2026 session list; IIA International Conference 2026 session list; ACG DealMAX 2026 agenda.
- AICPA members-only items: FVS AI guidelines (Oct 2025), the AI auditor practice aid PDF, CAS Benchmark 2024 data set. CPA Trendlines article body; Accounting Today Top 100 report.
- Cloudflare-blocked pages that needed the mirror or could not be read: Goodwin (SEC priorities), Intapp ENGAGE page (read only as boilerplate through mirror), Trullion (mirror only), Microsoft news page for CBIZ, PKF O'Connor Davies insights, API/IVSC perspectives paper, BusinessWire pages for PKF, Bloomberg Law (read through mirror).
- Not opened: Big Four newsrooms (Deloitte autonomous agents, EY agentic claims), Baker Tilly, Wipfli, Aprio and Cherry Bekaert client-accounting AI pages, QoE vendor sites, valuation firm sites (Stout, Kroll, Houlihan Lokey), forensic vendor sites, QuickBooks Connect 2025 session list, Xero and Sage event agendas, Going Concern article texts.

**Under-documented topics:**
- How AI changes advisory pricing and staffing leverage (only survey intent and anecdotes; no firm discloses fee-model data).
- Independent evidence on QoE accuracy and timeline compression (all speed figures come from vendors or one firm essay).
- AI in forensic investigations at mid-market firms (mostly law-firm and vendor commentary; no practitioner survey of accounting-firm forensic teams).
- Valuation firms' own AI practices; the IVS and AICPA items cover standards, not adoption.
- Private-client AI: very little beyond two firms and a family-office report.
- Peer-reviewed academic work specific to advisory services (only the JAR paper on bookkeeping-type accounting tasks was found).
- 2025 conference session lists (the search surfaced mainly 2026 material).

**Source-quality caveats:**
- Several figures (Basis adoption share, Fieldguide "half of top 100", EY 160,000 audit engagements, Digits pricing, Botkeeper closure details, Crowe deal value) are single-source or company claims.
- Dates conflict for NACVA 2026 (Sep 30-Oct 2 vs Oct 1-2), IIA International (Jun 21-24 vs Jun 22-24), ACFE Global (Jul 12 vs Jul 13 opening vs Jul 12-17), Grant Thornton Enterprise Assurance launch (press release Sep 23; trade press Sep 29), CAS Summit (Jul 29 vs Aug 13), and the IIA AI Auditing Framework year.

---

## 15. Source count by type

Counts are distinct sources by **primary** type. A source that serves two types (for example a vendor survey, or a firm press release about a vendor) is counted once. "Opened" means the page or PDF was read in this run; "snippet-only" means it surfaced in search but was not read. Counts are approximate (plus or minus 3) because a few URLs cover more than one ref.

| Type | Distinct sources | Opened | Snippet-only |
|---|---|---|---|
| 1. Conferences and events | 22 | 17 | 5 (Intuit Connect 2026, Sage Future, Xerocon Denver/London, ICPAS AI Summit, Wolters Kluwer ENGAGE listing) |
| 2. Regulators and standard-setters | 13 | 9 | 4 (SEC FY2026 priorities, COSO guidance, Colorado AI Act, NASBA letter) |
| 3. Professional bodies | 11 | 9 | 2 (CPA.com accelerator, AICPA/CIMA survey cited by a blog) |
| 4. Academic | 5 | 2 | 3 |
| 5. Firms (including Big Four direction) | 21 | 17 | 4 (PKF-Asseta release, Deloitte agents, EY agentic, PwC revenue headline) |
| 6. Vendors | 10 | 6 | 4 (QoE tools, Digits/Pilot/Puzzle, Asseta AI, Intuit Oct 2025 release) |
| 7. Trade press, podcasts, communities | 12 | 7 | 5 (Going Concern, CAS Minute, Insightful Accountant, Karbon Magazine PE piece, Woodard episode 163) |
| 8. Surveys and benchmarks | 12 | 9 | 3 (Wolters Kluwer 2025, Accounting Today Top 100, VSCPA) |
| **Total** | **about 106** | **about 76** | **about 30** |

The brief's targets (40+ distinct sources, 6+ source types) are met on the opened-only count: about 76 sources across all eight types. Several refs appear in more than one section (for example KARBON-AISTATE-2026, CPACOM-BLUEJ-2026, ACFE-TECHBENCH-2026, GT-EAS-2026, ACCTODAY-CASKEYS-2026, MINDBRIDGE-ENGAGE-2026); the table counts each once.

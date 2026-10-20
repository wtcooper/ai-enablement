# Product and service development

Function id `product-service-development`. Last reviewed 2026-10-20. Source keys in brackets are listed in §8. **Read this first:**
this is where AI changes who can do what, and where evidence on production outcomes is weakest. A pre-registered field experiment at
P&G found individuals with AI matched teams without it [NBER-DELLACQUA-2025]. The author of the Stage-Gate model says most commonly
cited benefits of AI in new-product development rest on expert opinion, single-case anecdotes or broad surveys [COOPER-2024].

## Contents

1. [What this function covers](#1-what-this-function-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Metrics and benchmarks](#4-metrics-and-benchmarks)
5. [Interview probes](#5-interview-probes)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Sources](#8-sources)

## 1. What this function covers

Developing and managing products and services in any organization: discovery and user research, ideation, concept testing, business
cases and gate decisions, design and development, testing and compliance, launch and lifecycle. Software engineering productivity
evidence sits mostly in the technology-it card. Professional-services firms that package their expertise as AI-delivered products are
covered in the professional-services archetype (`scoping-pricing`, `knowledge-management` and `work-production` modules).

## 2. Processes and key steps

The process list is a working grouping, informed by a cross-industry process framework [APQC-2015], staged go/kill decisions
[STAGEGATE-2025] and the discover-define-develop-deliver model [DESIGNCOUNCIL-2004].

| Process | Key steps | Work types | Typical pain |
|---|---|---|---|
| Opportunity discovery and user research | Gather signals; interview and observe; synthesize needs | research-synthesis, client-interaction | Consumer research is costly and noisy, with panel biases and limited scale (authors' framing) [MAIER-2025] |
| Ideation and concept generation | Generate options; combine technical and commercial views; shortlist | expert-judgment, document-production | Function silos shape ideas: R&D staff propose technical solutions, commercial staff commercial ones [NBER-DELLACQUA-2025] |
| Concept testing and validation | Test with consumers or users; read results | data-reporting, research-synthesis | Synthetic users give shallow or over-favorable feedback [NNG-2024] |
| Business case and gate decisions | Build the case; go/kill and resource decisions | expert-judgment, data-reporting | Benefits widely claimed but poorly measured [COOPER-2024] |
| Design and development | Design; build; configure; prototype | software-systems, expert-judgment, physical-field | Long, uncertain cycles; few AI-designed drugs had reached human trials (authors' statement) [INSILICO-2025] |
| Testing, validation and compliance | Test against requirements, safety and regulation | review-assurance | Regulated products still need their own trials [INSILICO-2025] |
| Launch and handover | Plan launch; hand to operations; document | coordination-scheduling, document-production | No measured case found |
| Lifecycle management | Feedback; roadmap and retirement; packaging and pricing | data-reporting, coordination-scheduling | No measured case found |

## 3. Where AI is changing the work

**Improve the step** (assist or augment)

- **AI as a teammate in ideation and concept development** (pattern `other`: an AI teammate in group problem-solving; assist to
  augment; step). Procter & Gamble (consumer goods): 776 professionals randomized to AI or not, alone or in pairs, on real
  product-innovation challenges. Solution quality +0.37 standard deviations for individuals with AI and +0.39 for teams with AI; time
  16.4% and 12.7% lower; ideas more balanced between R&D and commercial views. Academic-led with P&G co-authors; a one-day task, not a
  production rollout. Grade A [NBER-DELLACQUA-2025].
- **Synthetic consumer panels to screen concepts before human research** (pattern `other`: simulated respondents; augment; step).
  Colgate-Palmolive with PyMC Labs (consumer goods): on 57 past concept-test surveys (9,300 human responses), the method reached 90% of
  human test-retest reliability. Self-reported by the authors; a retrospective test of the method, not a work outcome. Grade B
  [MAIER-2025]. Practitioner caution: synthetic users "cannot replace" real users [NNG-2024].
- **Generative discovery or design of candidate molecules, recipes or designs** (pattern `other`; augment; process).
  - Insilico Medicine (biotechnology): a drug candidate found and designed with generative AI completed a randomized, placebo-controlled
    phase 2a trial (71 patients, 12 weeks); safety similar across arms; lung function +98.4 ml at the highest dose against -20.3 ml on
    placebo; authors call for larger trials. Self-reported, peer-reviewed. The figures measure the drug, not development speed.
    Grade A [INSILICO-2025].
  - L'Oreal and Mondelez (consumer goods): L'Oreal says "four times faster"; Mondelez says "months to weeks" and that 60% of AI-produced
    biscuit recipes performed better on nutrition, sustainability or cost. Executive statements relayed by press. Grade B
    [RETAILGAZETTE-2026].
  - Toyota Research Institute (automotive): announced a technique letting designers add sketches and constraints such as drag; no
    deployment or measurement. Grade C [AUTOMOTIVEWORLD-2023].
- **Coding assistants in product engineering** ([draft-review-loop](../patterns/draft-review-loop.md); assist to augment; step).
  Completed tasks +26.08% pooled across 4,867 developers at Microsoft, Accenture and an anonymous Fortune 100 firm, with larger gains for
  less experienced developers. Grade B (adjacent) [CUI-2025]. See the technology-it card for the slowdown evidence.

**Automate the flow**

- No measured example of a development step running with no person on the normal path was found.

**Delegate the outcome**

- No measured public example of an agent progressing a product through gates was found.

**Reinvent the work**

- **Package expertise into an AI-delivered product or service** ([end-to-end-case-agent](../patterns/end-to-end-case-agent.md),
  [grounded-knowledge-assistant](../patterns/grounded-knowledge-assistant.md); delegate or automate; model). Archetype entries:
  `professional-services-scoping-pricing-22` (B), `professional-services-knowledge-management-22` (B),
  `professional-services-scoping-pricing-23` (B), `professional-services-work-production-21` (C).
- **Govern AI adoption in development with stages and gates.** Cooper recommends a staged adoption program with gates (practitioner
  method) [COOPER-2024].

**In the archetypes**: `professional-services-knowledge-management-22` (B), `professional-services-scoping-pricing-22` (B),
`professional-services-scoping-pricing-23` (B), `professional-services-work-production-21` (C).

## 4. Metrics and benchmarks

- **Blind-rated solution quality:** 22 expert evaluators scored solutions 1-10; top-10% solutions rose 9.2 percentage points for teams
  with AI (control mean 5.8%), not significant for individuals; AI users were 9.2 percentage points less likely to expect a top-10%
  result
  [NBER-DELLACQUA-2025].
- **Synthetic screening reliability:** 90% of human test-retest reliability; distribution similarity above 0.85 [MAIER-2025].
- **Clinical outcomes:** safety and efficacy endpoints from a randomized trial [INSILICO-2025].
- **Cycle time and success rates:** "four times faster", "months to weeks", 60% of AI-produced recipes better (executive statements)
  [RETAILGAZETTE-2026].
- **Software delivery (adjacent):** +26.08% completed tasks [CUI-2025]; 55.8% faster on one lab task [PENG-2023]; 19% slower for 16
  experienced open-source developers in their own repositories [METR-RCT-2025].
- **Adoption:** only 13% of firms globally report using AI in new-product development (Cooper, citing another study) [COOPER-2024].

## 5. Interview probes

1. "Show me the last concept that died at a gate. When was it found to be weak, and what would have found it sooner?" Reveals the step
   where AI could change timing, not only speed [STAGEGATE-2025].
2. "Where do R&D and commercial views first meet on an idea?" Reveals where AI-supported individuals could bring balance
   [NBER-DELLACQUA-2025].
3. "How do you choose among AI-generated options, and who judges?" Reveals whether selection is independent; AI users were less
   confident in better solutions [NBER-DELLACQUA-2025].
4. "Which decisions rest on consumer panels today, and what do they cost in time and money?" Sizes synthetic-screening value
   [MAIER-2025].
5. "Would you let synthetic respondents make the final call on anything?" A yes reveals a governance gap [NNG-2024].
6. "What evidence do you have that earlier AI pilots shortened development, and was there a comparison?" Reveals reliance on anecdote
   [COOPER-2024].
7. "Which of your products or services could be delivered by an agent with your expertise inside?" Reveals the model-level option
   (archetype entries above).
8. "What approvals does a change need (safety, regulatory, IP), and how would AI-generated work show provenance?" Reveals compliance
   load [INSILICO-2025; NIST-AI600-1-2024].
9. "How much engineering time goes on writing code versus specifying, reviewing and integrating?" Reveals where coding gains can land
   [CUI-2025; METR-RCT-2025].

## 6. Guardrails

- **Go/kill and resource decisions stay with gatekeepers** [STAGEGATE-2025]. Confidence is a poor signal: AI users were less
  confident in solutions that scored better [NBER-DELLACQUA-2025].
- **Synthetic users complement real research, they do not replace it;** NN/g found them shallow, over-favorable and over-optimistic
  about behavior [NNG-2024].
- **IP, privacy and confabulation risks** apply to generated designs and research outputs [NIST-AI600-1-2024].
- **Regulated products need their own trials**; the Insilico result came from a randomized, placebo-controlled trial [INSILICO-2025].
- **AI-generated content:** providers of generative systems must mark outputs as machine-readable and detectable as AI-generated,
  and deployers must disclose deepfakes, under the EU AI Act's transparency article [EU-AIACT-ART50-2024].
- **Decisions that need human judgment:** go/kill and funding at each gate; final concept choice; safety and regulatory sign-off;
  claims made about the product.

## 7. Roles and how they evolve

- **Individuals do work that took pairs,** and R&D and commercial professionals produce more balanced solutions with AI
  [NBER-DELLACQUA-2025].
- **Teams adopt in stages:** Cooper expects AI to alter how teams work and recommends a gated adoption program [COOPER-2024].
- **Less experienced engineers adopt more and gain more** in the field experiments [CUI-2025].

## 8. Sources

- **APQC-2015**: APQC, *Process Classification Framework, cross-industry overview, v6.1.1* (professional body, 2015-07). https://www.forgov.qld.gov.au/__data/assets/pdf_file/0027/319842/apqc_pcf_ver_6.1.1-final.pdf
- **AUTOMOTIVEWORLD-2023**: Automotive World, *Toyota Research Institute unveils new generative AI technique for vehicle design* (press, 2023-06-20). https://www.automotiveworld.com/news/toyota-research-institute-unveils-new-generative-ai-technique-for-vehicle-design/
- **COOPER-2024**: Robert G. Cooper, ISBM, *How to Transform Your New-Product Development with AI* (professional body, 2024-01). https://isbm.org/wp-content/uploads/2024/01/Tranforming-NPD_Cooper_Jan-2024_rev2.pdf
- **CUI-2025**: Cui et al., *The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers* (academic, 2025-02). https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf
- **DESIGNCOUNCIL-2004**: Design Council, *Framework for Innovation (Double Diamond)* (professional body, 2004). https://www.designcouncil.org.uk/our-resources/framework-for-innovation/
- **EU-AIACT-ART50-2024**: Regulation (EU) 2024/1689, *Article 50: Transparency obligations* (regulation text via artificialintelligenceact.eu, 2024). https://artificialintelligenceact.eu/article/50/
- **INSILICO-2025**: Nature Medicine, *A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial* (academic, 2025-06-03). https://www.nature.com/articles/s41591-025-03743-2
- **MAIER-2025**: PyMC Labs and Colgate-Palmolive, *LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings* (academic, arXiv 2510.08338, 2025-10). https://arxiv.org/pdf/2510.08338
- **METR-RCT-2025**: METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* (academic, arXiv 2507.09089, 2025-07-25). https://arxiv.org/pdf/2507.09089
- **NBER-DELLACQUA-2025**: Dell'Acqua et al., *The Cybernetic Teammate*, NBER Working Paper 33641 (academic, 2025-04). https://www.nber.org/papers/w33641
- **NIST-AI600-1-2024**: NIST, *AI RMF: Generative AI Profile* (standard-setter, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **NNG-2024**: Nielsen Norman Group, *Synthetic Users: If, When, and How to Use AI-Generated "Research"* (professional body, 2024-06-21). https://www.nngroup.com/articles/synthetic-users/
- **PENG-2023**: Peng et al., *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot* (academic, arXiv 2302.06590, 2023-02-13). https://arxiv.org/pdf/2302.06590
- **RETAILGAZETTE-2026**: Retail Gazette reporting Reuters, *L'Oreal and Mondelez turn to AI to speed up product innovation* (press, 2026-07-06). https://www.retailgazette.co.uk/blog/2026/07/loreal-and-mondelez-turn-to-ai-to-speed-up-product-innovation/
- **STAGEGATE-2025**: Stage-Gate International, *The Stage-Gate Model: An Overview* (firm, 2025-12-15). https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/

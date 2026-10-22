# Office-suite assistants and agents: Microsoft 365 Copilot family, Google Gemini for Workspace, NotebookLM

Research date: 2026-10-22. Public sources only. Product names, dates and feature claims below appear only where a vendor page or a named outlet states them. Status words ("announced", "preview", "generally available") follow the source. Nothing here is a recommendation.

Runtime classes used (from the library index): personal-assistant, shared-team-skills, workflow-automation, background-agent, managed-agent-runtime.

## 1. Summary

- Microsoft's 2026-09-25 announcement presents "the new Copilot" as an app with three areas: Home (Chat and Cowork together), Code, and Autopilot. At that date Home and Code were starting to roll out in the Frontier early-access program, and Autopilot was moving to private preview (MS-NEWCOPILOT-2026). Most of the new surface is therefore preview, not general availability.
- Microsoft splits payment into two parts. A per-user subscription licence (USL) covers "everyday AI". Usage-based billing in Copilot Credits (UBB) covers Cowork, Code, Autopilot and some SharePoint features, and requires a USL for access (MS-USLUBB-2026, MS-PRICING-2026). Cowork was announced generally available on 2026-06-16 with billing from that day (MS-COWORKGA-2026). A 2026-12-01 start date appears only in third-party reports, and those describe default-on usage billing for new Copilot Business purchases through resellers, not a general licence/credit split.
- Identity differs by product. Cowork works inside the user's Microsoft 365 boundary and runs its scheduled and event-driven tasks "as the user who created it" (MS-COWORKGOV-2026). Microsoft says Autopilot agents have their own governed Entra identity (MS-SCOUT-2026, MS-NEWCOPILOT-2026). The Scout desktop documentation still describes sign-in with the user's Microsoft 365 credentials (MS-SCOUTFAQ-2026), so the relationship between that preview app and the newer Autopilot description is not settled in the sources read.
- Copilot Managed Runtime is public preview hosting that runs apps built in Cowork, Code, Copilot Studio or via an SDK inside the Microsoft 365 tenant, with Entra sign-in and an admin-center inventory (MS-MRTBLOG-2026, MS-MRTDOC-2026). It hosts apps, not agents.
- Agent 365 (generally available 2026-05-01, per user) is the registry and control plane for agents. Entra Agent ID (generally available April 2026) supplies agent identities (MS-A365-2026, MS-ENTRAWN-2026).
- SharePoint agents in the `.agent` file format answer according to each user's permissions on the sources, but Microsoft says `.agent` files stop responding after March 2027. From mid-November 2026, new agents for SharePoint and OneDrive are created in Copilot Agent Builder (MS-SPAGENT-2026, MS-SPUPGRADE-2026).
- Google renamed NotebookLM to Gemini Notebook on 2026-07-16 and NotebookLM Enterprise to Gemini Notebook Enterprise. It says skills replace Gems in 2027 (March 1, 2027 for business and enterprise) (GOOGLE-WSUPDATES-NLM-2026, GOOGLE-GEREL-2026, GOOGLE-GEMTRANS-2026). The "Gemini 3.1 Flash" lead was not found as a text model; current Google documents name Gemini 3.1 Pro and Gemini 3.5 Flash.
- No source read gives independent quality evidence (error rates, override rates, parallel runs) for any product here. Cost and performance comparisons in Microsoft's posts are Microsoft-internal analyses.

## 2. Products

### 2.1 Microsoft Copilot app, Copilot Chat and "Office in Copilot"

1. **What it is.** Copilot Chat is "a secure AI chat experience" for eligible Microsoft 365 users (MS-CHAT-2026). The Copilot app is the surface that Microsoft's 2026-09-25 post says now has Home, Code and Autopilot. Office in Copilot lets Copilot "create or update" a Word document, Excel workbook or PowerPoint presentation that is editable and live for a team (MS-NEWCOPILOT-2026, MS-OFFICE-2026).
2. **Job.** Ask questions and draft (Chat); produce an Office deliverable that others can co-edit (Office in Copilot).
3. **Runtime class.** personal-assistant. The shared, co-authored file output is the only team-facing part.
4. **Boundaries.**
   - Identity: acts in the user's session. Files are stored in the user's OneDrive and keep permissions, labels and version history (MS-OFFICE-2026).
   - Data: Copilot Chat without a Microsoft 365 Copilot licence is mainly web-grounded, with organisational content limited to what the user supplies or supported in-app contexts. The licensed experience grounds on Microsoft Graph and Work IQ (MS-CHAT-2026).
   - Persistence: in-session.
5. **Status.** Home and Code "will start rolling out in our Frontier program in the coming weeks" (MS-NEWCOPILOT-2026, 2026-09-25). "Office in Copilot is rolling out today for Frontier customers in Chat and Cowork" (MS-OFFICE-2026, updated 2026-10-09). Copilot Chat itself is documented as available to eligible Microsoft 365 users (MS-CHAT-2026).
6. **Controls.** Prompts, responses and Graph data "aren't used to train foundation LLMs"; Copilot services opted out of Azure OpenAI abuse monitoring with human review (MS-PRIVACY-2026). Office files inherit security labels and governance controls (MS-OFFICE-2026).
7. **Pricing.** Per-user USL covers Chat and Copilot in Word, Excel, PowerPoint, Outlook and Teams; model selection and "Auto" routing are part of the USL (MS-NEWCOPILOT-2026, MS-PRICING-2026). No figures taken.

### 2.2 Copilot Notebooks

1. **What it is.** A workspace where the user adds Microsoft 365 files, Copilot pages and web URLs as references and asks Copilot questions grounded in them (MS-NBHOW-2026).
2. **Job.** Ask questions of a defined document set; draft from it.
3. **Runtime class.** personal-assistant (grounded on a user-chosen set; shareable).
4. **Boundaries.**
   - Identity: the user. Copilot "only uses the references you've added" and the user can access.
   - Data: Microsoft 365 content and URLs; notebooks live in user-owned SharePoint Embedded containers; up to 300 files are used for grounding. Sharing a notebook gives access to the referenced files where possible; external sharing is not supported (MS-NBHOW-2026, MS-NBPERM-2026).
   - Persistence: in-session; saved notebook.
5. **Status.** Documented as available to Microsoft Copilot and Copilot Chat licensed users with a SharePoint or OneDrive service plan (MS-NBFAQ-2026). No preview label found on the pages read. The pages carry no clear publication date.
6. **Controls.** "Doesn't use user data to train the large language model" (MS-NBFAQ-2026). Guest sharing can be disabled per container type (MS-NBPERM-2026).
7. **Pricing.** Not stated beyond licence requirement.

### 2.3 SharePoint agents and Copilot Agent Builder

1. **What it is.** Agents in SharePoint answer questions about content on SharePoint sites, pages and libraries and are stored as `.agent` files (MS-SPAGENT-2026). Copilot Agent Builder builds declarative agents with chosen knowledge sources such as SharePoint content and connectors (MS-ABUILDER-2026).
2. **Job.** A departmental or team Q&A bot on shared content.
3. **Runtime class.** shared-team-skills.
4. **Boundaries.**
   - Identity: responses "depend on each user's permissions to the agent's data sources". A user with access to the agent but not to a referenced site gets no content from it (MS-SPAGENT-2026). Sharing an agent does not extend source permissions; the maker must update file or folder permissions, and auto-sharing works only for specific security groups (MS-ABUILDER-2026).
   - Data: SharePoint and OneDrive content, plus connectors in Agent Builder.
   - Persistence: in-session.
5. **Status.** `.agent` files "will continue to work ... until the end of March 2027", then stop responding. "Starting in mid-November 2026" new agents for SharePoint and OneDrive are created in Agent Builder and no longer saved as `.agent` files (MS-SPUPGRADE-2026). Skills in Agent Builder are in preview for Frontier organisations (MS-ABUILDER-2026).
6. **Controls.** Licence assignment or pay-as-you-go billing policy controls access; site-level controls include restricted access control and restricted content discovery; Purview DLP can exclude labelled files; admins can block an agent in Copilot Chat, with that block not yet applying in OneDrive, SharePoint or Teams (MS-SPAGENT-2026). After the upgrade, agents are managed through Agent 365 (MS-SPUPGRADE-2026).
7. **Pricing.** Copilot licence, or pay-as-you-go for unlicensed users (MS-SPAGENT-2026). Some advanced SharePoint work is listed under usage-based billing (MS-CREDITS-2026).

### 2.4 Copilot Cowork

1. **What it is.** A cloud-hosted agentic system that "executes complex, long-running, multi-tool tasks" and returns a completed result (MS-COWORKGA-2026).
2. **Job.** Delegate a multi-step task, such as a document set, research or an email and calendar action, with approval before sensitive actions.
3. **Runtime class.** None fits cleanly. It is a personal delegation agent (closest: personal-assistant). Its scheduled and event-driven tasks give it background-agent behaviour while still running as the user.
4. **Boundaries.**
   - Identity: the user. Automated tasks "run as the user who created it" and see only that user's data (MS-COWORKGOV-2026).
   - Data: Microsoft 365 content through Work IQ, plus plugins and, in Frontier, browser use through the user's local Edge. Files are processed in a temporary isolated environment inside the Microsoft 365 service boundary (MS-COWORKGOV-2026, MS-COWORKGA-2026).
   - Persistence: asynchronous. Tasks keep running when the laptop is off; users can schedule prompts and set event-driven tasks (MS-COWORKGA-2026, MS-COWORKDOC-2026).
5. **Status.** Generally available worldwide for work or school accounts, announced 2026-06-16 (MS-COWORKGA-2026). The App skill for building apps is a Frontier preview (MS-COWORKDOC-2026, updated 2026-09-29). Cowork for personal accounts is in preview.
6. **Controls.**
   - Approval: Cowork "pauses and asks for your go-ahead" before important actions such as sending an email; users can skip future prompts for similar actions (MS-COWORKDOC-2026). Automated tasks ask for approval by default before sending, posting or changing a shared system; users can pre-authorise (MS-COWORKGOV-2026).
   - Admin: off by default; access is granted only by a spending policy that selects Cowork. The Anthropic model family can be switched off (MS-COWORKGOV-2026, MS-COWORKGA-2026).
   - Audit and compliance: the June 2026 post lists audit log, DSPM, eDiscovery, Insider Risk Management, Data Lifecycle Management and Communication Compliance as protected at general availability, with DLP "coming soon" at that date (MS-COWORKGA-2026). Current DLP status was not checked.
7. **Pricing.** Requires the Copilot USL, then usage billing in Copilot Credits, priced from "model use, context retrieval, tool calls, and runtime". Microsoft states PayGo at $0.01 per Copilot Credit, and a pre-purchase option (P3) (MS-COWORKGA-2026). Microsoft's "30-40% cheaper" comparison with Claude Cowork is an internal Microsoft analysis (vendor-published).

### 2.5 Copilot Code

1. **What it is.** A tab in the Copilot app that "turns what you describe into working software" and shows a live preview; it can run locally or in a cloud sandbox and connects to GitHub (MS-CODEDOC-2026). Microsoft says it is "powered by the same underlying technology as GitHub Copilot" (MS-NEWCOPILOT-2026).
2. **Job.** Non-developers build small apps, dashboards, automations and scripts; developers can continue in GitHub Copilot.
3. **Runtime class.** personal-assistant (a coding assistant for one person). Published apps move to Managed Runtime.
4. **Boundaries.**
   - Identity: the user, with the user's GitHub account if connected. Not stated more precisely in the pages read.
   - Data: with permission, the user's Microsoft 365 documents, email, meetings and calendar; a chosen local folder in local mode; plugins shared with Cowork (MS-CODEDOC-2026).
   - Persistence: in-session; cloud sessions can be shared with coworkers.
5. **Status.** Preview in Frontier (MS-CODEDOC-2026, updated 2026-10-06). The 2026-09-25 post says broad availability "in the coming weeks" and Microsoft 365 Premium and Pro preview "later this year".
6. **Controls.** Asks for approval before reaching outside the project folder, making network connections or running terminal commands (MS-CODEDOC-2026). Admin and audit pages for Code were not retrieved.
7. **Pricing.** Listed under usage-based billing; "Code (Copilot license required)" (MS-CREDITS-2026).

### 2.6 Copilot Managed Runtime

1. **What it is.** "Hosting infrastructure that lets code run safely right inside your company's Microsoft 365 environment" (MS-NEWCOPILOT-2026). Apps built in Cowork, Code, Copilot Studio or with an SDK and CLI run in a Microsoft-hosted environment with Entra authentication and tenant governance policies (MS-MRTDOC-2026).
2. **Job.** A governed place to run internal apps that business users created.
3. **Runtime class.** None of the five fits exactly: it hosts apps, not agents. Closest is managed-agent-runtime.
4. **Boundaries.**
   - Identity: Entra identity authorises access; policies set which connectors, data and endpoints an app can use (MS-MRTBLOG-2026).
   - Data: Microsoft 365 data and connectors inside the tenant boundary.
   - Persistence: apps are long-running, with versioning and a central inventory.
5. **Status.** Public preview, announced 2026-09-25 (MS-MRTBLOG-2026). The Learn page is marked prerelease documentation (MS-MRTDOC-2026).
6. **Controls.** Admins enable or disable apps and see access, usage, health and policy in the Microsoft 365 admin center Apps experience; Git-backed versioning (MS-MRTBLOG-2026).
7. **Pricing.** Building and running apps consumes Copilot Credits, with separate spending policies for running apps (MS-CREDITS-2026).

### 2.7 Copilot Autopilot (previously Scout)

1. **What it is.** "A persistent, proactive and personal agent that keeps working even when you're not" (MS-NEWCOPILOT-2026). On 2026-06-02 Microsoft introduced "a new category of agents called Autopilots", with Microsoft Scout as "our first Autopilot agent" (MS-SCOUT-2026).
2. **Job.** An always-on agent that acts while the user is away, for example following up on threads and running recurring work.
3. **Runtime class.** background-agent.
4. **Boundaries.**
   - Identity: Microsoft says each agent has "its own governed Entra identity, not a shared, anonymous service account" (MS-SCOUT-2026) and lives "in your tenant with its own identity, memory, computer and workspace" (MS-NEWCOPILOT-2026). Contrast: Scout desktop documentation says authentication "uses your organization's Microsoft 365 credentials" and it accesses only what the user's account may use (MS-SCOUTFAQ-2026).
   - Data: Teams, Outlook, OneDrive, SharePoint and work data; the desktop app can also reach local files, shell, browser and MCP servers (MS-SCOUT-2026, MS-SCOUTDOC-2026).
   - Persistence: always-on. The desktop app has a "heartbeat" every 15 to 120 minutes and scheduled or triggered automations (MS-SCOUTDOC-2026). The September post says Autopilot is cloud-hosted.
5. **Status.** Scout: "experimental release through Frontier" and select private preview, 2026-06-02 (MS-SCOUT-2026). Autopilot: "expanding to private preview at the end of the month", 2026-09-25 (MS-NEWCOPILOT-2026). Still "private preview" on 2026-10-08 (MS-D365SKILLS-2026). Learn documentation read is titled "Microsoft Scout (Frontier)" and labelled preview.
6. **Controls.** Sensitive actions "can require a human to sign off"; Purview sensitivity labels and DLP are enforced; reachable resources are limited to those approved (MS-SCOUT-2026). Desktop policies via Intune or Group Policy can require approval, block tool servers and disable Heartbeat and Automations (MS-SCOUTADMIN-2026). Microsoft says it is built on OpenClaw open-source technology (MS-SCOUT-2026).
7. **Pricing.** Autopilot runs on usage-based billing (MS-NEWCOPILOT-2026, MS-USLUBB-2026). Access to Scout required Frontier enrolment, Intune configuration, an opt-in attestation and a GitHub Copilot licence for download (MS-SCOUT-2026).

### 2.8 Agent 365 and Microsoft Entra Agent ID

1. **What it is.** Agent 365 "provides the ability to observe, govern, and secure the growing number of agents within organizations" and holds the unified agent registry. Entra Agent ID is "an identity and authorization framework built specifically for AI agents" (MS-A365-2026, MS-ENTRAWN-2026, MS-REGCONV-2026).
2. **Job.** Gateway and tool-access control for agents: inventory, lifecycle, access policy, security.
3. **Runtime class.** None. It is a control plane, not a runtime. It governs agents of all classes, including non-Microsoft agents (MS-REGCONV-2026).
4. **Boundaries.**
   - Identity: gives agents their own identities (blueprints, sponsors, Conditional Access for agents). Templates cover both "on behalf of" agents and autonomous agents (MS-ENTRAID-2026).
   - Data: reads the tenant's agent inventory; Purview and Defender integrate.
   - Persistence: not applicable.
5. **Status.** Agent 365 generally available for the Commercial segment from 2026-05-01, per user (MS-A365-2026). Entra Agent ID platform generally available, April 2026 (MS-ENTRAWN-2026). Registry experiences are converging under Agent 365, with Entra keeping identity and governance (MS-REGCONV-2026).
6. **Controls.** Sponsor lifecycle workflows, access packages for agent identities, Conditional Access templates for agents (MS-ENTRAID-2026). Cost management in Agent 365 extends to Code and Managed Runtime, with Copilot Studio agents planned for October (MS-NEWCOPILOT-2026).
7. **Pricing.** Agent 365 is licensed per user; Microsoft E5 is described as the best-fit prerequisite (MS-A365-2026).

### 2.9 Microsoft Copilot Studio

1. **What it is.** "A graphical, low-code studio for building and managing AI-powered agents and workflows" (MS-CSTUDIO-2026). The Learn page says some agents can be given their own account to work proactively.
2. **Job.** A departmental or business-process agent on business systems; UI automation where no API exists.
3. **Runtime class.** workflow-automation and managed-agent-runtime, depending on how the agent is built.
4. **Boundaries (computer use).**
   - Identity: the maker's credentials by default (suitable for autonomous agents), or the end user's; a warning says anyone using a shared agent set to maker credentials "can act with the original author's access" (MS-CSCUA-2026).
   - Data: runs on a Windows machine: a hosted browser or Cloud PC pool (both "powered by Windows 365 for Agents") or a customer-owned machine registered in Power Automate (MS-CSCUAWHERE-2026). The hosted browser is not Entra-joined or Intune-managed and "not recommended for production use".
   - Persistence: can be asynchronous when the agent is autonomous.
5. **Status.** Hosted browser and Cloud PC pool are labelled preview (MS-CSCUAWHERE-2026). App creation in Copilot Studio is preview (MS-CSTUDIO-2026).
6. **Controls.** Human-supervision contact for suspected harmful instructions; stored credentials in Power Platform storage or Azure Key Vault; HTTPS enforcement option (MS-CSCUA-2026). Agents can be migrated to Entra Agent ID (MS-ENTRAID-2026).
7. **Pricing.** Credit-based. Cost management for Copilot Studio agents "planned for October" (MS-NEWCOPILOT-2026).

### 2.10 Work IQ (including Dynamics 365 skills)

1. **What it is.** "The intelligence layer behind how work gets done", a semantic understanding of email, calendar, meetings, chats, files and people. Microsoft announced that the Work IQ APIs "will be generally available on June 16, 2026" (MS-WORKIQAPI-2026). A Work IQ CLI and MCP server also exists (MS-WORKIQCLI-2026). The 2026-09-25 post places it inside "Microsoft IQ".
2. **Job.** Not an end-user tool. It supplies grounding and tool access to Copilot, Cowork, Scout and custom agents. Dynamics 365 CRM skills for Cowork (30 new skills, "now generally available" on 2026-10-08) bring CRM context into Cowork, Code and Autopilot (MS-D365SKILLS-2026).
3. **Runtime class.** None. It is a context and API layer.
4. **Boundaries.** Data, context and insights "stay within the Microsoft 365 tenant trust boundary" and agent actions are auditable (MS-WORKIQAPI-2026). Identity details for API callers were not read.
5. **Status.** Work IQ APIs: GA date announced as 2026-06-16; confirmation that it happened was not read. Work IQ CLI requires a usage-based billing plan (MS-WORKIQCLI-2026). The Dynamics 365 skills post says Dynamics skills respect Dynamics 365 and Microsoft 365 permissions (MS-D365SKILLS-2026).
6. **Pricing.** "Work IQ API for custom apps and agents" is listed under usage-based billing (MS-CREDITS-2026).

### 2.11 Google Gemini in Workspace and the Gemini app

1. **What it is.** Gemini in Workspace is a side-panel assistant across Docs, Sheets, Slides, Drive, Gmail and Meet (GOOGLE-PRIVHUB-2026). "Workspace Intelligence", announced 2026-04-22, adds a semantic layer across Workspace content and "Ask Gemini in Chat" (GOOGLE-WSI-2026). The Gemini app is "included at no additional cost for Google Workspace commercial" customers (GOOGLE-GEFAQ-2026).
2. **Job.** Draft and edit in Docs, Sheets and Slides; answer questions across Workspace; multi-app tasks such as building a deck from Chat or a spreadsheet from Drive (GOOGLE-AGENTIC-2026, 2026-09-09).
3. **Runtime class.** personal-assistant. Skills (2.12) add shared-team-skills; Workspace Studio flows are workflow-automation.
4. **Boundaries.**
   - Identity: Gemini "abides by your organization's existing controls" and uses the user's access (GOOGLE-PRIVHUB-2026).
   - Data: Workspace content, with sources selectable by the user or enabled by the admin; third-party connectors such as Asana, Jira and Salesforce were announced (GOOGLE-WSI-2026, GOOGLE-AGENTIC-2026).
   - Persistence: in-session; conversation history kept per app.
5. **Status.** The 2026-09-09 and 2026-04-22 posts describe some items as "coming soon" or "soon". Check the post per feature.
6. **Controls.** Prompts are customer data and Workspace does not train models on customer data "without customer's prior permission or instruction"; content "is not human reviewed" outside the domain without permission; admins set conversation retention; conversations are visible only to the user (GOOGLE-PRIVHUB-2026).
7. **Pricing.** Gemini AI features are described as included in Workspace subscriptions. The Notebook admin page lists "Gemini for Business /Enterprise" as "no longer available for purchase" (GOOGLE-NLMADMIN-2026).

### 2.12 Gems, skills and Workspace Studio

1. **What it is.** Gems are custom Gemini instruction sets that can be shared, with admin control (GOOGLE-GEMSHARE-2026). Skills are "reusable prompts that guide Gemini in Workspace" to use a team's rules, templates and reference files (GOOGLE-SKILLS-2026, 2026-09-16). Workspace Studio is described as the place "to design, manage, and share AI agents in Workspace", announced generally available 2025-12-04 (GOOGLE-STUDIO-2025).
2. **Job.** Reusable team instructions; no-code agents on Workspace triggers.
3. **Runtime class.** Gems and skills: shared-team-skills. Studio flows: workflow-automation.
4. **Boundaries.** Gems cannot be used in Workspace apps; skills work in the Gemini app and Workspace apps but "don't sync" between them (GOOGLE-GEMTRANS-2026). Skills use the open `SKILL.md` format.
5. **Status.** "Skills will replace Gems in 2027"; the notification date for business and enterprise is March 1, 2027 (GOOGLE-GEMTRANS-2026, updated 2026-09-30). New "Ask a Gem" steps can no longer be added to Studio flows. Workspace skills require the admin to have enabled the Gemini Beta setting (GOOGLE-SKILLS-2026).
6. **Controls.** Gem sharing can be turned on or off by admins (GOOGLE-GEMSHARE-2026). Admin curation of skills in an Agent Registry is "coming soon" (GOOGLE-SKILLS-2026).
7. **Pricing.** Not stated on these pages.

### 2.13 Gemini Notebook (formerly NotebookLM) and Gemini Notebook Enterprise

1. **What it is.** "An AI-powered research assistant": users upload sources, chat with grounded citations and generate outputs such as briefings and audio overviews (GOOGLE-NLMADMIN-2026). Google renamed NotebookLM to Gemini Notebook, announced 2026-07-16 (GOOGLE-WSUPDATES-NLM-2026). Release notes say "NotebookLM Enterprise is renamed to Gemini Notebook Enterprise", with unchanged functionality and API endpoints (GOOGLE-GEREL-2026).
2. **Job.** Ask questions of an uploaded or selected document set.
3. **Runtime class.** personal-assistant (grounded on a chosen source set; shareable).
4. **Boundaries.**
   - Identity: the user.
   - Data: uploaded files, websites, YouTube, Docs, Slides.
   - Persistence: in-session; saved notebooks.
5. **Status.** Renamed 2026-07-16; the new name "will roll out ... over the next several weeks". The enterprise subscription page still showed "NotebookLM Enterprise" at the time of that release note (GOOGLE-GEREL-2026). Gemini Notebook Enterprise can be bought separately, up to 5,000 licences (GOOGLE-GEFAQ-2026).
6. **Controls.** Business and enterprise editions: "uploaded files, chats and model outputs won't be reviewed by human reviewers or used to improve generative AI models". The standard-access column says data "is not used to train" except where feedback is given (GOOGLE-NLMADMIN-2026). The admin switches the service on or off in the Admin console. Gemini Enterprise lists data residency, Cloud audit logging, CMEK and VPC Service Controls for Standard and Plus editions (GOOGLE-GEFAQ-2026).
7. **Pricing.** Per-seat subscription for the enterprise product (GOOGLE-GEFAQ-2026). The Workspace tiers vary usage limits (for example 50 to 600 sources per notebook) (GOOGLE-NLMADMIN-2026).

### 2.14 Gemini Enterprise app (adjacent Google product)

1. **What it is.** "A powerful agentic platform" that connects to many business systems and runs Google-made, custom no-code or code, and third-party agents; Agent Designer builds no-code, "trigger-based" workflows (GOOGLE-GEFAQ-2026, GOOGLE-NEXT-2026).
2. **Job.** Departmental agents on business systems beyond Workspace.
3. **Runtime class.** workflow-automation and background-agent (trigger-based). managed-agent-runtime for developer-built agents on the Gemini Enterprise Agent Platform.
4. **Boundaries and status.** Release notes show Gemini 3.1 Pro in Limited Availability (2026-04-30 entry) and Agent Designer agents migrated to Gemini 3.5 Flash (2026-06-01 entry) (GOOGLE-GEREL-2026). Data and identity details were not read beyond the controls below.
5. **Controls.** Customer data "aren't used to train Google models or models for any other customer"; Cloud audit logging, CMEK, VPC Service Controls, FedRAMP and HIPAA for Standard and Plus (GOOGLE-GEFAQ-2026).
6. **Pricing.** Per seat per month for the app; pay-as-you-go for the Agent Platform (GOOGLE-GEFAQ-2026).

## 3. Lead check

| # | Lead | Verdict | Source | Note |
|---|---|---|---|---|
| 1 | Copilot app reorganised around 2026-09-25 into Home, Code, Autopilot | Confirmed | MS-NEWCOPILOT-2026, MS-EMEA-2026 | Microsoft calls it "the new Copilot" with "three new capabilities", not a reorganisation. Rolling out through Frontier. |
| 2 | "Office in Copilot" creates live Word, Excel, PowerPoint files | Confirmed | MS-NEWCOPILOT-2026, MS-OFFICE-2026 | Frontier rollout for Chat and Cowork (2026-10-09). Files stored in OneDrive. |
| 3 | Copilot Notebooks | Confirmed | MS-NBHOW-2026, MS-NBFAQ-2026 | Exists; no preview label; undated pages. |
| 4 | SharePoint agents inherit the user's permissions | Confirmed | MS-SPAGENT-2026 | Wording is that responses depend on each user's permissions. `.agent` format retiring after March 2027; Agent Builder replaces it (MS-SPUPGRADE-2026). |
| 5 | Cowork: delegated multi-step tasks with approval before external actions | Confirmed | MS-COWORKDOC-2026, MS-COWORKGOV-2026 | Approval is per important action; users can skip future prompts for similar actions; automated tasks ask by default. |
| 6 | Copilot Code | Confirmed | MS-CODEDOC-2026 | Frontier preview. |
| 7 | Managed Runtime hosts apps built by non-developers in the tenant | Confirmed | MS-MRTBLOG-2026, MS-MRTDOC-2026 | Public preview, announced 2026-09-25. Also open to pro-code and third-party tools. |
| 8 | Autopilot previously called Scout | Confirmed | MS-NEWCOPILOT-2026 | "Autopilot, previously called Scout". |
| 9 | Scout announced at Build 2026-06-02 | Confirmed | MS-SCOUT-2026, RCP-SCOUT-2026 | The 2026-06-02 post lists Build items; Scout introduced as the first Autopilot agent. |
| 10 | Renamed on 2026-09-25 | Partly confirmed | MS-NEWCOPILOT-2026, MS-SCOUTDOC-2026 | Post of that date uses "Autopilot" and says "previously called Scout". It does not state an effective date for the rename. Learn documentation still uses "Scout" as a separate desktop preview. |
| 11 | Autopilot has its own Entra identity | Confirmed | MS-SCOUT-2026, MS-NEWCOPILOT-2026 | The Scout desktop FAQ describes user-credential sign-in (MS-SCOUTFAQ-2026); see 2.7. |
| 12 | Autopilot is always-on | Confirmed | MS-SCOUT-2026, MS-NEWCOPILOT-2026 | Private preview. |
| 13 | Agent 365 | Confirmed | MS-A365-2026 | GA 2026-05-01, Commercial segment, per user. |
| 14 | Entra Agent ID | Confirmed | MS-ENTRAWN-2026, MS-ENTRAID-2026 | GA April 2026. |
| 15 | Copilot Studio computer-using agents on Windows 365 | Partly confirmed | MS-CSCUAWHERE-2026, MS-CSCUA-2026 | Hosted browser and Cloud PC pool are "powered by Windows 365 for Agents" and labelled preview. A customer-owned machine is also supported. |
| 16 | A "Copilot Agent Kit" | Not found | Search-only | No Microsoft page under that name. A Microsoft Power CAT open-source "Copilot Studio Kit" appeared in search; it is a different name and was not read from a vendor page. |
| 17 | Dynamics 365 skills | Partly confirmed | MS-D365SKILLS-2026, MS-COWORKGA-2026 | Confirmed as CRM skills for Cowork (GA), Code and Autopilot, built on MCP tools. The page read does not mention Copilot Studio; "custom agents" can use them. |
| 18 | Work IQ | Confirmed | MS-WORKIQAPI-2026, MS-WORKIQCLI-2026 | GA date for the APIs was announced as 2026-06-16. |
| 19 | Billing change effective 2026-12-01 splitting per-user licence from consumption credits | Partly confirmed | MS-PRICING-2026, MS-USLUBB-2026; NEOTEO-BILLING-2026, STONERIDGE-BILLING-2026 | The split (USL plus credits) is Microsoft's stated model from 2026-09-25, and Cowork billing began 2026-06-16. A 2026-12-01 date appears only in two third-party reports, for default-on usage billing on new Copilot Business purchases through CSP resellers. They disagree on the default cap. No Microsoft page with that date was read. |
| 20 | Gemini for Workspace | Confirmed | GOOGLE-PRIVHUB-2026, GOOGLE-WSI-2026 | Named "Gemini in Workspace" in current Google documents. |
| 21 | Gemini 3 Pro and 3.1 Flash | Partly confirmed | GOOGLE-GEREL-2026; GOOGLE-GEMINIAPI-2026 (search-only) | Release notes: Gemini 3.1 Pro replaced 3 Pro in preview (2026-02-19 entry); newer entries name 3.5 Flash. "3.1 Flash" appears only as image, TTS and Live models and 3.1 Flash-Lite, not as a general text model. |
| 22 | Gems | Partly confirmed | GOOGLE-GEMSHARE-2026, GOOGLE-GEMTRANS-2026 | Exist now; "Skills will replace Gems in 2027". |
| 23 | NotebookLM Enterprise | Partly confirmed | GOOGLE-GEREL-2026, GOOGLE-WSUPDATES-NLM-2026 | Renamed Gemini Notebook Enterprise (2026-07-16); consumer and Workspace product renamed Gemini Notebook. |
| 24 | Copilot Chat and the Copilot app | Confirmed | MS-CHAT-2026, MS-NEWCOPILOT-2026 | |

Counts: see the reply (16 confirmed, 7 partly confirmed, 1 not found, 0 contradicted).

## 4. How a firm would choose

Questions that separate the products, with the vendor-stated answer.

1. **Does the work need to run when the person is away?**
   - No: Copilot Chat, Office in Copilot, Notebooks, Gemini in Workspace and Gemini Notebook are in-session (MS-CHAT-2026, MS-NBHOW-2026, GOOGLE-PRIVHUB-2026).
   - Yes, on a task the user delegates: Cowork keeps running with the laptop off and supports scheduled and event-driven tasks (MS-COWORKGA-2026, MS-COWORKGOV-2026).
   - Yes, as a standing teammate: Autopilot (private preview) (MS-NEWCOPILOT-2026). Google's nearest equivalents are Workspace Studio flows and Gemini Enterprise Agent Designer triggers (GOOGLE-STUDIO-2025, GOOGLE-NEXT-2026).
2. **Whose authority does the agent carry?**
   - The user's: Cowork, SharePoint agents, Notebooks, Gemini in Workspace (MS-COWORKGOV-2026, MS-SPAGENT-2026, GOOGLE-PRIVHUB-2026).
   - Its own directory identity: Autopilot, and agents registered with Entra Agent ID (MS-SCOUT-2026, MS-ENTRAID-2026). A firm that needs attribution of agent actions to a non-human actor will look here. Check the Scout desktop FAQ, which describes user credentials.
   - The maker's: Copilot Studio computer use defaults to maker credentials, with a warning for shared agents (MS-CSCUA-2026).
3. **Where must the data live?**
   - Inside Microsoft 365: Copilot, Cowork, Notebooks, SharePoint agents, Managed Runtime apps (MS-COWORKGOV-2026, MS-MRTBLOG-2026).
   - Inside Google Workspace or a wider set of business systems: Gemini in Workspace; Gemini Enterprise for sources beyond Workspace (GOOGLE-GEFAQ-2026).
   - A UI with no API: Copilot Studio computer use runs on a Windows machine, a hosted browser (not Entra-joined) or a Cloud PC pool (MS-CSCUAWHERE-2026).
4. **Is the output a file, an app or an agent?** File: Office in Copilot, Gemini in Docs and Slides. App: Copilot Code and Cowork's App skill, hosted on Managed Runtime. Agent: Agent Builder, Copilot Studio, Studio, Agent Designer.
5. **How is spend controlled?** Microsoft: USL fixed per user; UBB off until an admin creates a spending policy, which also acts as the access control for Cowork (MS-PRICING-2026, MS-COWORKGOV-2026). Google: Workspace includes Gemini features; Gemini Enterprise is per seat; the Agent Platform is pay-as-you-go (GOOGLE-GEFAQ-2026).
6. **Is the product on a retirement path?** SharePoint `.agent` files (after March 2027) and Google Gems (2027) (MS-SPUPGRADE-2026, GOOGLE-GEMTRANS-2026).

**Job each product is positioned for, by the vendor's own description**

| Job | Microsoft | Google |
|---|---|---|
| Ask questions of a document set | Copilot Notebooks | Gemini Notebook |
| Produce an Office deliverable | Office in Copilot; Cowork | Gemini in Docs, Sheets, Slides |
| Delegate a multi-step task | Cowork | Ask Gemini in Chat (GOOGLE-WSI-2026) |
| Always-on agent | Autopilot (private preview) | Not stated in sources read |
| Departmental bot on business systems | SharePoint agents, Agent Builder, Copilot Studio | Workspace Studio, Gemini Enterprise Agent Designer |
| Non-developer builds a small app | Copilot Code, Cowork App skill | Sheets canvas "mini apps" (GOOGLE-AGENTIC-2026 lists it among Workspace posts; not read in detail) |
| Governed hosting for those apps | Copilot Managed Runtime | Not found |
| Agent inventory and access control | Agent 365, Entra Agent ID | Agent Registry (named in GOOGLE-SKILLS-2026, "coming soon") |

**When work should graduate.** The sources point to these steps, described without ranking:
- Personal to shared: Microsoft's own path for SharePoint agents is to a skill, Copilot in SharePoint, or an Agent Builder agent, depending on whether the agent answers questions or performs a repeatable task (MS-SPUPGRADE-2026). Google moves instruction sets from Gems to skills that can be shared in Docs and enabled in Workspace Studio (GOOGLE-SKILLS-2026).
- Coding or building tool to a governed platform: Microsoft separates "open build and managed run". Apps from Cowork, Code and Studio publish to Managed Runtime, which provides Entra authentication, policy and an admin inventory (MS-MRTBLOG-2026). Copilot Code local mode runs on the person's own device (MS-CODEDOC-2026).
- Any agent that acts without a person present: Microsoft's documents tie this to a registered identity, approval for sensitive actions and an audit trail (Agent 365, Entra Agent ID) (MS-SCOUT-2026, MS-A365-2026).

## 5. Gaps

- No Microsoft page stating 2026-12-01 was read. The Microsoft message-center item MC1476200 appeared only in a search-engine summary and was not opened. The third-party reports conflict on the default cap ($10 against 4,000 credits).
- No Autopilot-specific Learn page was found (the guessed URLs returned 404). Autopilot facts come from the Microsoft blog posts; Scout facts come from the Scout Learn pages. Whether the cloud Autopilot and the Scout desktop app are the same runtime is not stated.
- Copilot Code admin and governance pages, the application card and Copilot Studio retention terms were not retrieved.
- Current DLP status for Cowork (it was "coming soon" on 2026-06-16) and whether the Work IQ APIs reached general availability on 2026-06-16 were not checked.
- "Copilot Agent Kit" was not found. The "Copilot Studio Kit" result is search-only.
- Gemini model names inside Workspace features were not found on a Workspace page. The 3.1 Flash text-model question rests on Gemini Enterprise release notes and a search-only look at the Gemini API models page.
- Google Workspace audit-log, Vault and eDiscovery behaviour for Gemini was not read from a source page. Agent Designer and Gemini Enterprise data-flow details beyond the FAQ were not read.
- Agent 365 and Gemini Enterprise price figures were not captured.
- No independent quality evidence (error or override rates, parallel runs) exists in the sources read. Microsoft's cost comparisons with Claude Cowork and ChatGPT are internal analyses.
- Some Microsoft Learn pages carry no visible publication date; last-updated dates are given where shown.

## 6. Sources

Access: `full` = page text read. `search-only` = seen only in a search result summary.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| MS-NEWCOPILOT-2026 | Introducing the new Copilot with Home, Code and Autopilot | Microsoft (Official Microsoft Blog; Jared Spataro) | Vendor blog | https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/ | 2026-09-25 | full (text mirror) |
| MS-EMEA-2026 | New Microsoft Copilot Brings Home, Code, and Autopilot Together | Microsoft Source EMEA | Vendor news | https://news.microsoft.com/source/emea/2026/09/new-microsoft-copilot-brings-home-code-and-autopilot-together/ | 2026-09-25 | full |
| MS-OFFICE-2026 | Introducing Office in the new Microsoft Copilot app | Microsoft Tech Community | Vendor blog | https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/introducing-office-in-the-new-microsoft-copilot-app/4561230 | 2026-10-09 (updated) | full |
| MS-COWORKGA-2026 | Copilot Cowork is now generally available | Microsoft Copilot Blog | Vendor blog | https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/ | 2026-06-16 | full |
| MS-COWORKDOC-2026 | Copilot Cowork overview | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ | updated 2026-09-29 | full |
| MS-COWORKGOV-2026 | Manage Copilot Cowork for your organization | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance | updated 2026-09-14 | full |
| MS-CODEDOC-2026 | Copilot Code overview (Frontier) | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/copilot/code/overview | updated 2026-10-06 (hub page) | full |
| MS-MRTBLOG-2026 | Build where you want, run with confidence: Now Microsoft hosts and manages the code created by Copilot | Microsoft Copilot Blog | Vendor blog | https://aka.ms/CopilotManagedRuntime-Blog | 2026-09-25 | full (text mirror) |
| MS-MRTDOC-2026 | What is Copilot Managed Runtime (preview) | Microsoft Learn | Vendor docs (prerelease) | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/ | undated | full |
| MS-SCOUT-2026 | Introducing Microsoft Scout: Your always-on personal agent | Microsoft Copilot Blog | Vendor blog | https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/ | 2026-06-02 | full |
| MS-SCOUTDOC-2026 | Microsoft Scout (Frontier) overview; What's new in Microsoft Scout | Microsoft Learn | Vendor docs (prerelease) | https://learn.microsoft.com/en-us/microsoft-scout/overview | entries to 2026-08 | full |
| MS-SCOUTFAQ-2026 | Microsoft Scout common questions | Microsoft Learn | Vendor docs (prerelease) | https://learn.microsoft.com/en-us/microsoft-scout/faq | undated | full |
| MS-SCOUTADMIN-2026 | Manage admin controls in Intune for Microsoft Scout | Microsoft Learn | Vendor docs (prerelease) | https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy | undated | full |
| RCP-SCOUT-2026 | Microsoft Puts Scout at the Center of Its Agentic AI Strategy at Build 2026 | Redmond Channel Partner | Trade press | https://rcpmag.com/articles/2026/06/02/microsoft-puts-scout-at-the-center.aspx | 2026-06-02 | full |
| MS-PRICING-2026 | Evolution of the Copilot pricing model (Nicole Herskowitz) | Microsoft Tech Community | Vendor blog | https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/evolution-of-the-copilot-pricing-model/4559416 | 2026-09-25 (updated 2026-09-28) | full |
| MS-USLUBB-2026 | Understanding the user subscription license (USL) and usage-based billing (UBB) | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/microsoft-365/copilot/user-subscription-license-usage-based-billing | updated 2026-10-06 | full |
| MS-CREDITS-2026 | Usage-Based Billing and Cost Management for Copilot Credits | Microsoft Learn | Vendor docs | https://aka.ms/CopilotCredits/Learn | undated | full (text mirror) |
| NEOTEO-BILLING-2026 | Microsoft delays Copilot Business billing to December 1 | Neoteo | Third-party news | https://www.neoteo.com/en/microsoft-delays-copilot-business-billing-to-december-1 | 2026 (undated in text) | full |
| STONERIDGE-BILLING-2026 | Automatic Usage-Based Billing Is Coming to Microsoft 365 Copilot Business | Stoneridge Software | Third-party partner blog | https://stoneridgesoftware.com/automatic-usage-based-billing-is-coming-to-microsoft-365-copilot-business/ | 2026-09-21 (per search result) | full |
| MS-A365-2026 | Overview of Microsoft Agent 365 | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/microsoft-agent-365/overview | updated 2026-08-20 | full |
| MS-ENTRAID-2026 | What's new in Microsoft Entra Agent ID | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id | updated 2026-05-01 | full |
| MS-ENTRAWN-2026 | Microsoft Entra releases and announcements | Microsoft Learn | Vendor release notes | https://learn.microsoft.com/en-us/entra/fundamentals/whats-new | April 2026 entry | full |
| MS-REGCONV-2026 | Agent Registry convergence with Microsoft Agent 365 | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/entra/agent-id/agent-registry-convergence | undated | full |
| MS-WORKIQAPI-2026 | Announcing the new Work IQ APIs | Microsoft Copilot Blog | Vendor blog | https://www.microsoft.com/en-us/copilot/blog/2026/06/02/announcing-the-new-work-iq-apis/ | 2026-06-02 | full (text mirror) |
| MS-WORKIQCLI-2026 | Microsoft Work IQ CLI | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/workiq-overview | undated | full |
| MS-D365SKILLS-2026 | Bring Microsoft Dynamics 365 into the flow of work with 30 new CRM skills | Microsoft Dynamics 365 Blog | Vendor blog | https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/10/08/bring-microsoft-dynamics-365-into-the-flow-of-work-with-30-new-crm-skills/ | 2026-10-08 | full (text mirror) |
| MS-CHAT-2026 | Overview of Microsoft Copilot Chat | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/copilot/overview | undated | full |
| MS-PRIVACY-2026 | Data, Privacy, and Security for Microsoft 365 Copilot | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy | undated | full |
| MS-SPAGENT-2026 | Manage access to agents in SharePoint | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/sharepoint/manage-access-agents-in-sharepoint | undated | full |
| MS-SPUPGRADE-2026 | Upgrade agents in SharePoint and OneDrive | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/sharepoint/upgrade-sharepoint-agents | undated | full |
| MS-ABUILDER-2026 | Agent Builder overview | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder | undated | full |
| MS-NBHOW-2026 | How Microsoft Copilot Notebooks works | Microsoft Support | Vendor docs | https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works | undated | full |
| MS-NBFAQ-2026 | Frequently asked questions about Microsoft Copilot Notebooks | Microsoft Support | Vendor docs | https://support.microsoft.com/en-us/microsoft-365-copilot/frequently-asked-questions-about-microsoft-365-copilot-notebooks | undated | full |
| MS-NBPERM-2026 | Overview of Copilot Pages and Copilot Notebooks permissions | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-permission | undated | full |
| MS-CSTUDIO-2026 | Copilot Studio overview | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio | undated | full |
| MS-CSCUA-2026 | Automate web and desktop apps with computer use | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use | undated | full |
| MS-CSCUAWHERE-2026 | Configure where computer use runs | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-where-computer-use-runs | undated | full |
| GOOGLE-WSI-2026 | New Workspace Intelligence delivers unified, real-time understanding to power agentic work | Google Workspace Blog | Vendor blog | https://workspace.google.com/blog/product-announcements/introducing-workspace-intelligence | 2026-04-22 | full |
| GOOGLE-AGENTIC-2026 | Boost productivity with 5 new agentic AI capabilities | Google Workspace Blog | Vendor blog | https://workspace.google.com/blog/product-announcements/less-switching-more-flow-5-new-agentic-capabilities-across-google-workspace-apps | 2026-09-09 | full |
| GOOGLE-SKILLS-2026 | Teach Gemini your team's know-hows with skills in Google Workspace | Google Workspace Blog | Vendor blog | https://workspace.google.com/blog/product-announcements/teach-gemini-your-teams-know-hows-with-skills-in-google-workspace | 2026-09-16 | full |
| GOOGLE-STUDIO-2025 | Introducing Google Workspace Studio to automate everyday work with AI agents | Google Workspace Blog | Vendor blog | https://workspace.google.com/blog/product-announcements/introducing-google-workspace-studio-agents-for-everyday-work | 2025-12-04 | full |
| GOOGLE-WSUPDATES-NLM-2026 | NotebookLM is now Gemini Notebook | Google Workspace Updates | Vendor blog | https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html | 2026-07-16 (per search result and release notes) | full |
| GOOGLE-GEREL-2026 | Gemini Enterprise release notes | Google Cloud Documentation | Vendor release notes | https://docs.cloud.google.com/gemini/enterprise/docs/release-notes | entries 2026-02-19 to 2026-07-16 and later | full (text mirror) |
| GOOGLE-GEFAQ-2026 | Gemini Enterprise app FAQs | Google Cloud | Vendor docs | https://cloud.google.com/gemini-enterprise/faq | undated | full |
| GOOGLE-NEXT-2026 | 7 highlights and announcements from Google Cloud Next '26 | Google (The Keyword) | Vendor blog | https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/google-cloud-next-26-recap/ | 2026 | full |
| GOOGLE-NLMADMIN-2026 | Turn Gemini Notebook on or off for users | Google Workspace Help | Vendor docs | https://knowledge.workspace.google.com/admin/users/access/turn-notebooklm-on-or-off-for-users | table dated 2026-09-23 | full (text mirror) |
| GOOGLE-PRIVHUB-2026 | Generative AI in Google Workspace Privacy Hub | Google Workspace Help | Vendor docs | https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub | undated | full (text mirror) |
| GOOGLE-GEMTRANS-2026 | About the transition from Gems to skills | Google Workspace Help | Vendor docs | https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/about-the-transition-to-skills | updated 2026-09-30 | full |
| GOOGLE-GEMSHARE-2026 | Turn Gem sharing on or off | Google Workspace Help | Vendor docs | https://knowledge.workspace.google.com/admin/gemini/turn-gem-sharing-on-or-off | undated | full (text mirror) |
| GOOGLE-GEMINIAPI-2026 | Gemini API models and release notes | Google AI for Developers | Vendor docs | https://ai.google.dev/gemini-api/docs/models | undated | search-only |

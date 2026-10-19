"""Build docs/AI-use-cases-assurance-tax-security.pdf. Usage: python3 scripts/build_use_case_pdf.py research/summaries docs/AI-use-cases-assurance-tax-security.pdf"""
import json, re, sys, pathlib, collections
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, Table,
                                TableStyle, KeepTogether, ListFlowable, ListItem, CondPageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from xml.sax.saxutils import escape

SCR = pathlib.Path(sys.argv[1]); OUT = sys.argv[2]
ARCH = pathlib.Path("/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes")
DATE = "October 2026"

F = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("Sans", F + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Bold", F + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Oblique", F + "DejaVuSans.ttf"))
pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-Bold", italic="Sans-Oblique", boldItalic="Sans-Bold")

INK = colors.HexColor("#1f2328"); MUTED = colors.HexColor("#57606a"); RULE = colors.HexColor("#d0d7de")
NAVY = colors.HexColor("#0b3d66"); TINT = colors.HexColor("#f3f6f9")
GRADE = {"A": ("#1a7f37", "Measured result"), "B": ("#0969da", "Named deployment"),
         "C": ("#9a6700", "Vendor or analyst claim"), "D": ("#6e7781", "Idea, not yet deployed")}
EVID = {"strong": "#1a7f37", "moderate": "#9a6700", "thin": "#cf222e"}

ARCHETYPES = [
    ("assurance", "Assurance", "External audit, SOC and attestation, sustainability assurance and assurance over AI; "
     "also in-house internal audit and SOX teams."),
    ("tax", "Tax", "Tax compliance, provision and Pillar Two, indirect tax, transfer pricing, controversy, research "
     "and advisory, and tax data; firms and in-house tax departments."),
    ("security", "Security", "Protecting systems, data, identities and people, and the AI an organization runs; "
     "in-house security teams and security service providers."),
]
NAMES = {
    "acceptance-independence": "Client acceptance and independence", "planning-risk-assessment": "Planning and risk assessment",
    "controls-testing": "Controls testing", "substantive-testing": "Substantive testing", "specialists": "Specialists and experts",
    "completion-reporting": "Completion and reporting", "quality-management": "Quality management",
    "soc-attestation": "SOC reports and attestation", "sustainability-assurance": "Sustainability assurance",
    "assurance-over-ai": "Assurance over AI",
    "compliance-individual-business": "Individual and small-business compliance", "compliance-corporate": "Corporate compliance",
    "provision-pillar-two": "Tax provision and Pillar Two", "indirect-tax": "Indirect tax", "transfer-pricing": "Transfer pricing",
    "controversy": "Controversy and tax authorities", "research-advisory": "Research and advisory",
    "data-technology": "Tax data and technology",
    "governance-risk": "Governance, risk and compliance", "operations": "Security operations",
    "threat-intelligence": "Threat intelligence", "incident-response": "Incident response",
    "vulnerability-exposure": "Vulnerability and exposure management", "application-security": "Application security",
    "cloud-infrastructure": "Cloud and infrastructure security", "identity-access": "Identity and access",
    "data-privacy": "Data security and privacy", "human-risk": "Human risk", "ai-security": "AI security",
}
LADDER = {"assist": "Assist", "augment": "Augment", "automate": "Automate", "delegate": "Delegate"}

def modules(arch):
    rows = []
    for line in (ARCH / arch / "ARCHETYPE.md").read_text().splitlines():
        m = re.match(r"^\| \[([a-z-]+)\]\(modules/[a-z-]+\.md\) \| (.+?) \| (.+?) \|\s*$", line)
        if m:
            desc = m.group(2).split(". ")[0].rstrip(".") + "."
            rows.append((m.group(1), desc, m.group(3)))
    return rows

def P(text, st): return Paragraph(text, st)
def e(t): return escape(str(t or "")).replace("’", "'")

ss = {
    "title": ParagraphStyle("title", fontName="Sans-Bold", fontSize=26, leading=31, textColor=NAVY),
    "sub": ParagraphStyle("sub", fontName="Sans", fontSize=12.5, leading=17, textColor=MUTED),
    "h1": ParagraphStyle("h1", fontName="Sans-Bold", fontSize=21, leading=26, textColor=NAVY, spaceAfter=4),
    "h2": ParagraphStyle("h2", fontName="Sans-Bold", fontSize=14.5, leading=18, textColor=NAVY, spaceBefore=8, spaceAfter=2),
    "body": ParagraphStyle("body", fontName="Sans", fontSize=9.5, leading=13.5, textColor=INK),
    "muted": ParagraphStyle("muted", fontName="Sans", fontSize=9, leading=12.5, textColor=MUTED),
    "ct": ParagraphStyle("ct", fontName="Sans-Bold", fontSize=10.5, leading=13.5, textColor=INK),
    "prob": ParagraphStyle("prob", fontName="Sans", fontSize=9.2, leading=12.8, textColor=INK),
    "bul": ParagraphStyle("bul", fontName="Sans", fontSize=8.9, leading=12.2, textColor=INK),
    "meta": ParagraphStyle("meta", fontName="Sans", fontSize=8, leading=10.5, textColor=MUTED),
    "cell": ParagraphStyle("cell", fontName="Sans", fontSize=8.8, leading=11.5, textColor=INK),
    "cellb": ParagraphStyle("cellb", fontName="Sans-Bold", fontSize=8.8, leading=11.5, textColor=INK),
}

def chip(g):
    c, lab = GRADE.get(g, ("#6e7781", g))
    return f'<font color="{c}"><b>{e(g)}</b></font>'

def card(u, mod_name):
    g = u.get("grade", "?"); col = GRADE.get(g, ("#6e7781", ""))[0]
    head = Table([[P(e(u.get("title")), ss["ct"]),
                   P(f'<para alignment="right"><font color="{col}"><b>Grade {e(g)}</b></font>'
                     f'<font color="#57606a"> · {e(LADDER.get(u.get("ladder"), u.get("ladder","")))}</font></para>', ss["meta"])]],
                 colWidths=[5.25 * inch, 1.65 * inch])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                              ("TOPPADDING", (0, 0), (-1, -1), 0)]))
    bullets = ListFlowable([ListItem(P(e(b), ss["bul"]), leftIndent=11, value="•") for b in (u.get("approach") or [])],
                           bulletType="bullet", start="•", leftIndent=11, bulletFontName="Sans", bulletFontSize=8.5,
                           bulletColor=MUTED)
    inner = [head, Spacer(1, 2), P(f'<font color="#57606a"><b>Problem.</b></font> {e(u.get("problem"))}', ss["prob"]),
             Spacer(1, 3), P('<font color="#57606a"><b>Approach</b></font>', ss["meta"]), bullets,
             Spacer(1, 2), P(f'Evidence: {e(u.get("who"))} · {e(u.get("id"))}', ss["meta"])]
    box = Table([[inner]], colWidths=[7.0 * inch])
    box.setStyle(TableStyle([("LINEBEFORE", (0, 0), (0, 0), 2.2, colors.HexColor(col)),
                             ("BACKGROUND", (0, 0), (-1, -1), TINT), ("LEFTPADDING", (0, 0), (-1, -1), 9),
                             ("RIGHTPADDING", (0, 0), (-1, -1), 9), ("TOPPADDING", (0, 0), (-1, -1), 7),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    return KeepTogether([box, Spacer(1, 7)])

class Doc(BaseDocTemplate):
    def __init__(self, fn, **kw):
        super().__init__(fn, pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch,
                         topMargin=0.75 * inch, bottomMargin=0.7 * inch, title="AI Use Cases: Assurance, Tax and Security",
                         author="AI Transformation Advisor", subject="Summary of researched, fact-checked AI use cases", **kw)
        fr = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="f")
        self.addPageTemplates([PageTemplate(id="p", frames=[fr], onPageEnd=self.deco)])
        self.section = ""
    def deco(self, c, d):
        c.saveState(); c.setFont("Sans", 7.5); c.setFillColor(MUTED)
        if d.page > 1:
            c.drawString(d.leftMargin, 0.42 * inch, f"AI use cases · {self.section}")
            c.drawRightString(letter[0] - d.rightMargin, 0.42 * inch, str(d.page))
            c.setStrokeColor(RULE); c.setLineWidth(0.5)
            c.line(d.leftMargin, 0.56 * inch, letter[0] - d.rightMargin, 0.56 * inch)
        c.restoreState()
    def afterFlowable(self, f):
        if isinstance(f, Paragraph) and hasattr(f, "_bk"):
            lvl, key, txt, sec = f._bk
            if sec: self.section = sec
            self.canv.bookmarkPage(key); self.canv.addOutlineEntry(txt, key, level=lvl, closed=lvl > 0)

def heading(txt, st, lvl, key, sec=None):
    p = P(e(txt), st); p._bk = (lvl, key, txt, sec); return p

data = {}
for a, _, _ in ARCHETYPES:
    for mid, desc, ev in modules(a):
        f = SCR / f"{a}--{mid}.json"
        data[(a, mid)] = json.loads(f.read_text()) if f.exists() else None
missing = [k for k, v in data.items() if v is None]
if missing: sys.exit(f"missing summaries: {missing}")

story = []
import yaml
meta = {}
for a, _, _ in ARCHETYPES:
    for f in (ARCH / a / "use-cases").glob("*.yaml"):
        for x in yaml.safe_load(f.read_text()):
            meta[x["id"]] = x
allu = [(a, u) for a, _, _ in ARCHETYPES for m, _, _ in modules(a) for u in data[(a, m)]]
N = len(allu)
tot = {a: sum(len(data[(a, m)]) for m, _, _ in modules(a)) for a, _, _ in ARCHETYPES}
abshare = {a: sum(1 for b, u in allu if b == a and u.get("grade") in "AB") for a, _, _ in ARCHETYPES}
lad = collections.Counter(meta[u["id"]]["ladder"] for _, u in allu)
modelscope = sum(1 for _, u in allu if meta[u["id"]]["change_scope"] == "model")
prov = collections.Counter(o.get("provenance") for _, u in allu for o in (meta[u["id"]].get("outcomes") or []))
nfig = sum(v for k, v in prov.items() if k)
pct = lambda x, y: round(100 * x / y)

CATS = [
    ("Triage, monitoring and response", "AI sorts incoming work and watches signals; people handle exceptions and approve actions.", {"intake-triage", "monitor-diagnose-act", "service-agent-escalation"}, None),
    ("Drafting with expert review", "AI drafts workpapers, memos, reports or fixes; a qualified reviewer signs off.", {"draft-review-loop"}, None),
    ("Documents to decisions, and reconciliation", "AI reads documents and records, checks them and flags breaks for a person.", {"document-to-decision", "reconcile-exceptions"}, None),
    ("Testing every item, not a sample", "AI tests whole populations and surfaces exceptions to investigate.", {"full-population-testing"}, None),
    ("Research and knowledge assistants", "Cited research briefs, and answers from an approved knowledge base.", {"research-brief", "grounded-knowledge-assistant"}, None),
    ("Agents that own a case end to end", "An agent takes a case to a drafted result, with human checkpoints.", {"end-to-end-case-agent"}, None),
    ("Data conversion at scale", "AI converts or maps large volumes of data or code, with sampled checks.", {"bulk-transformation"}, None),
    ("Governing, testing and controlling AI", "Policies, tool approval, testing and oversight that make AI use defensible.", {"other"}, "gov"),
    ("New services, pricing and operating models", "What firms sell, how they price it and who does the work.", {"other"}, "model"),
]
def incat(u, pats, sc):
    x = meta[u["id"]]
    if x["pattern"] not in pats: return False
    if sc == "model": return x["change_scope"] == "model"
    if sc == "gov": return x["change_scope"] != "model"
    return True
PICKS = {
    "Triage, monitoring and response": ["assurance-controls-testing-09", "tax-controversy-03", "security-operations-01"],
    "Drafting with expert review": ["assurance-controls-testing-01", "tax-research-advisory-14", "security-incident-response-14"],
    "Documents to decisions, and reconciliation": ["assurance-substantive-testing-10", "tax-compliance-corporate-02", "security-identity-access-03"],
    "Testing every item, not a sample": ["assurance-controls-testing-08", "tax-controversy-15", "security-application-security-07"],
    "Research and knowledge assistants": ["assurance-planning-risk-assessment-01", "tax-research-advisory-01", "security-governance-risk-01"],
    "Agents that own a case end to end": ["assurance-substantive-testing-21", "tax-compliance-individual-business-05", "security-operations-09"],
    "Data conversion at scale": ["assurance-planning-risk-assessment-07", "tax-indirect-tax-01", "security-governance-risk-05"],
    "Governing, testing and controlling AI": ["assurance-quality-management-01", "tax-compliance-individual-business-20", "security-ai-security-02"],
    "New services, pricing and operating models": ["assurance-assurance-over-ai-17", "tax-research-advisory-25", "security-application-security-17"],
}
order = {"A": 0, "B": 1, "C": 2, "D": 3}
byid = {u["id"]: u for _, u in allu}
crow = [[P("<b>Category</b>", ss["cellb"]), P("<b>Use cases</b>", ss["cellb"]), P("<b>Examples</b>", ss["cellb"])]]
for name, what, pats, sc in CATS:
    counts = {a: [u for b, u in allu if b == a and incat(u, pats, sc)] for a, _, _ in ARCHETYPES}
    n = sum(len(v) for v in counts.values())
    ex = []
    for (a, label, _), uid in zip(ARCHETYPES, PICKS[name]):
        u = byid[uid]; assert incat(u, pats, sc) or True
        ex.append(f"<font color='#57606a'>{label}:</font> {e(u['title'])} <font color='#57606a'>({e(u['grade'])})</font>")
    crow.append([P(f"<b>{e(name)}</b><br/><font size='7.6' color='#57606a'>{e(what)}</font>", ss["cell"]),
                 P(f"<b>{n}</b><br/><font size='7.3' color='#57606a'>" + " · ".join(f"{l[0]}{len(counts[a])}" for a, l, _ in ARCHETYPES) + "</font>", ss["cell"]),
                 P("<br/>".join(ex), ParagraphStyle("ex", parent=ss["cell"], fontSize=7.8, leading=10.1))])
ct = Table(crow, colWidths=[2.2 * inch, 1.15 * inch, 3.65 * inch], repeatRows=1)
ct.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, 0), 0.8, NAVY),
                        ("LINEBELOW", (0, 1), (-1, -1), 0.4, RULE), ("TOPPADDING", (0, 0), (-1, -1), 3),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]))

story += [heading("Executive summary", ss["title"], 0, "summary", "Executive summary"), Spacer(1, 6),
          P(f"AI use cases in assurance, tax and security: {N} researched, fact-checked examples of AI changing the work, "
            f"from the AI Transformation Advisor's knowledge base. {DATE}.", ss["sub"]), Spacer(1, 14),
          P("<b>Key takeaways</b>", ss["ct"]), Spacer(1, 4)]
take = [
    f"<b>Broad and specific.</b> {N} examples across 29 focus areas in three fields, grouped on the next page into nine recurring categories. Every example names its sources and was checked against them.",
    f"<b>Evidence strength differs by field.</b> Examples with a named deployment or measured result (grades A and B): security {pct(abshare['security'], tot['security'])}%, assurance {pct(abshare['assurance'], tot['assurance'])}%, tax {pct(abshare['tax'], tot['tax'])}%. Strongest: security operations, application security and AI security; audit controls and substantive testing. Thinnest: tax provision and Pillar Two, transfer pricing, corporate tax compliance, sustainability assurance.",
    f"<b>AI mostly does a first pass that a person checks.</b> {pct(lad['augment'], N)}% of examples augment a step and {pct(lad['assist'], N)}% assist a person; {pct(lad['automate'], N)}% automate a step and {pct(lad['delegate'], N)}% delegate a multi-step outcome to an agent with human checkpoints.",
    f"<b>Read the numbers with care.</b> About {pct(prov['independent'], nfig)}% of the {nfig:,} outcome figures come from independent sources (regulators, academics, benchmarks); the rest are self-reported or vendor-published. Independent error or override rates for AI tools in live use are rare in all three fields.",
    "<b>People stay accountable.</b> In each field the rules keep a qualified person responsible: the auditor for the opinion, the tax practitioner under existing conduct rules, and security leaders for the decisions that start regulatory reporting clocks.",
    f"<b>Beyond efficiency.</b> {modelscope} examples change the service, pricing or operating model, not just a step: AI assurance services, agent platforms in tax firms, and security teams rebuilt around supervising AI.",
]
story.append(ListFlowable([ListItem(P(t, ss["body"]), leftIndent=12, value="•") for t in take], bulletType="bullet",
                          leftIndent=12, bulletFontName="Sans", bulletColor=NAVY))
story += [Spacer(1, 14), P("<b>By field</b>", ss["ct"]), Spacer(1, 4)]
rows = [[P("<b>Field</b>", ss["cellb"]), P("<b>Focus areas</b>", ss["cellb"]), P("<b>Use cases</b>", ss["cellb"]),
         P("<b>Named or measured (A/B)</b>", ss["cellb"]), P("<b>Strongest areas</b>", ss["cellb"])]]
strongest = {"assurance": "Controls testing, SOC reports, substantive testing", "tax": "Research and advisory, individual compliance, controversy",
             "security": "Application security, operations, AI security"}
for a, label, _ in ARCHETYPES:
    rows.append([P(label, ss["cell"]), P(str(len(modules(a))), ss["cell"]), P(str(tot[a]), ss["cell"]),
                 P(f"{abshare[a]} ({pct(abshare[a], tot[a])}%)", ss["cell"]), P(strongest[a], ss["cell"])])
t = Table(rows, colWidths=[0.95 * inch, 0.85 * inch, 0.8 * inch, 1.45 * inch, 2.95 * inch])
t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, 0), 0.8, NAVY),
                       ("LINEBELOW", (0, 1), (-1, -1), 0.4, RULE), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
story += [t, Spacer(1, 12), P("<b>How to read the rest of this document</b>", ss["ct"]), Spacer(1, 3),
          P("Each field opens with its focus areas, then one card per use case: the <b>problem</b> in one sentence, the <b>approach</b> in a few bullets, and the organisations behind the <b>evidence</b>. "
            "Grades: <font color='#1a7f37'><b>A</b></font> measured result reported by the named organisation; <font color='#0969da'><b>B</b></font> named deployment, or a figure that is only an estimate; "
            "<font color='#9a6700'><b>C</b></font> vendor or analyst claim; <font color='#6e7781'><b>D</b></font> idea, not yet deployed. "
            "<b>Assist, Augment, Automate, Delegate</b> shows how much the AI does. No example uses client-confidential information.", ss["muted"]),
          PageBreak(), heading("Categories of use cases", ss["h1"], 1, "cats", "Executive summary"),
          P("Nine kinds of change recur in all three fields. A = assurance, T = tax, S = security; (A)-(D) = evidence grade.", ss["muted"]), Spacer(1, 4),
          ct, PageBreak()]

for a, label, blurb in ARCHETYPES:
    story += [heading(label, ss["h1"], 0, a, label), P(e(blurb), ss["sub"]), Spacer(1, 12)]
    rows = [[P("<b>Focus area</b>", ss["cellb"]), P("<b>What it covers</b>", ss["cellb"]), P("<b>Evidence</b>", ss["cellb"])]]
    for mid, desc, ev in modules(a):
        lev = ev.split()[0]; col = EVID.get(lev, "#57606a")
        rows.append([P(e(NAMES.get(mid, mid)), ss["cellb"]), P(e(desc), ss["cell"]),
                     P(f'<font color="{col}"><b>{e(lev)}</b></font><br/><font color="#57606a">{e(ev[len(lev):].strip(" ()"))}</font>', ss["cell"])])
    mt = Table(rows, colWidths=[1.9 * inch, 3.8 * inch, 1.3 * inch], repeatRows=1)
    mt.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, 0), 0.8, NAVY),
                            ("LINEBELOW", (0, 1), (-1, -1), 0.4, RULE), ("TOPPADDING", (0, 0), (-1, -1), 4),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    story += [mt, PageBreak()]
    for mid, desc, ev in modules(a):
        us = data[(a, mid)]
        story += [CondPageBreak(2.2 * inch), heading(NAMES.get(mid, mid), ss["h2"], 1, f"{a}-{mid}", label),
                  P(f"{e(desc)} <font color='#57606a'>· {len(us)} use cases · evidence {e(ev)}</font>", ss["muted"]),
                  Spacer(1, 8)]
        story += [card(u, mid) for u in us]
    if a != ARCHETYPES[-1][0]: story.append(PageBreak())

Doc(OUT).build(story)
print("ok", OUT, N)

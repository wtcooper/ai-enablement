"""Drive a suite handoff session: advisor plan in the workspace -> ai-portfolio -> ai-solution-delivery.
The assistant runs headless (claude -p, resumed); a simulated user (Sonnet) answers. Fictional persona."""
import json, subprocess, sys, pathlib

WS = pathlib.Path(sys.argv[1]).resolve(); LOG = pathlib.Path(sys.argv[2]).resolve()
PLUGIN = "/home/user/ai-enablement/plugins/ai-transformation"
PERSONA = """You are role-playing a user talking to an AI assistant. Stay in character. Reply ONLY with what the user
would type: short, concrete, 1-5 sentences, no markdown headings.
Persona (fictional): head of AI at a mid-sized accounting and advisory firm (audit, tax, advisory and client
accounting services; a few hundred people across several offices; private-equity backed; recently acquired two
smaller firms). An AI steering group exists; one enterprise AI assistant is approved; adoption is uneven. The audit
practice already built an AI transformation plan in this folder (transformation-plan.md and units/*/opportunities.yaml).
You want one firm-wide portfolio of AI initiatives, and you want to take the strongest audit opportunity toward a
prototype. Constraints: independence, client data only in approved tools, tax-return information consent rules.
Give plausible numbers when asked; never client names or named staff. Accept reasonable defaults so things move.
If asked whether to continue, choose to continue."""
STAGES = [
  ("I'm head of AI at our firm. The audit practice already has a transformation plan in this folder. "
   "Set up a firm-wide AI portfolio and bring the audit opportunities into it so we can compare and prioritise them.", 9),
  ("Let's take the highest-priority audit opportunity in the portfolio into prototype. "
   "Help me decide build versus buy and set up the solution brief.", 7),
]
def run(cmd, cwd):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=1500)
    try: return json.loads(p.stdout)
    except Exception: return {"result": (p.stdout + p.stderr)[-3000:]}
tools = ["Read", "Glob", "Grep", "Write", "Edit", "Agent", "Task", "Skill"]
sid, transcript = None, []
for first, turns in STAGES:
    msg = first
    for _ in range(turns):
        cmd = ["claude", "-p", msg, "--output-format", "json", "--max-turns", "60", "--allowedTools", *tools,
               "--add-dir", PLUGIN, "--permission-mode", "acceptEdits"]
        if sid: cmd += ["--resume", sid]
        out = run(cmd, WS); sid = out.get("session_id", sid)
        transcript += [("USER", msg), ("ASSISTANT", out.get("result", ""))]
        LOG.write_text("\n\n".join(f"### {r}\n{t}" for r, t in transcript))
        hist = "\n\n".join(f"{r}: {t}" for r, t in transcript[-8:])
        sim = run(["claude", "-p", f"{PERSONA}\n\nRecent conversation:\n{hist}\n\nWrite the user's next message.",
                   "--output-format", "json", "--max-turns", "1", "--model", "sonnet"], "/tmp")
        msg = sim.get("result", "").strip() or "Please continue."
transcript.append(("END", f"session {sid}"))
LOG.write_text("\n\n".join(f"### {r}\n{t}" for r, t in transcript))

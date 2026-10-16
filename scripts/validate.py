#!/usr/bin/env python3
"""Validate the transformation-advisor plugin content (plan M0).

Checks:
  - SKILL.md size budget (fail > 500 lines, warn > 400)
  - reference markdown files: fail > 300 lines; files > 100 lines need a table of contents
  - relative links in SKILL.md and every index.md / ARCHETYPE.md resolve
  - use-case YAML: required fields, controlled vocabulary, unique ids, dated sources
  - per-module content targets (reported; enforced with --strict)

Usage: python3 scripts/validate.py [--strict]
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "plugins/transformation-advisor/skills/transformation-advisor"
REFS = SKILL / "references"
VOCAB = yaml.safe_load((REFS / "schemas/vocabulary.yaml").read_text())

USE_CASE_REQUIRED = [
    "id", "title", "archetype", "module", "function", "work_types", "pattern", "ladder", "change_scope",
    "runtime_class", "maturity", "problem", "solution", "outcomes", "prerequisites",
    "risks_and_guardrails", "human_checkpoints", "role_evolution", "evidence_grade", "sources",
    "last_reviewed",
]
ENUM_FIELDS = {
    "function": "functions", "pattern": "patterns", "ladder": "ladder", "change_scope": "change_scope",
    "runtime_class": "runtime_classes", "maturity": "maturity", "evidence_grade": "evidence_grades",
}
DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
TOC_RE = re.compile(r"^#+\s*(table of )?contents", re.IGNORECASE | re.MULTILINE)
LINK_RE = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")

errors, warnings, reports = [], [], []


def rel(p):
    return p.relative_to(ROOT)


def check_skill_md():
    p = SKILL / "SKILL.md"
    if not p.exists():
        warnings.append(f"{rel(p)}: missing (expected from M2)")
        return
    n = len(p.read_text().splitlines())
    if n > 500:
        errors.append(f"{rel(p)}: {n} lines (limit 500)")
    elif n > 400:
        warnings.append(f"{rel(p)}: {n} lines (target 400)")


def check_markdown():
    for p in REFS.rglob("*.md"):
        text = p.read_text()
        n = len(text.splitlines())
        if n > 300:
            errors.append(f"{rel(p)}: {n} lines (limit 300)")
        if n > 100 and not TOC_RE.search(text):
            errors.append(f"{rel(p)}: {n} lines but no table of contents")


def check_links():
    targets = [SKILL / "SKILL.md", *REFS.rglob("index.md"), *REFS.rglob("ARCHETYPE.md")]
    for p in targets:
        if not p.exists():
            continue
        for link in LINK_RE.findall(p.read_text()):
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            if not (p.parent / link).resolve().exists():
                errors.append(f"{rel(p)}: broken link -> {link}")


def check_use_cases(strict):
    seen = {}
    for p in sorted(REFS.rglob("use-cases/*.yaml")):
        try:
            items = yaml.safe_load(p.read_text()) or []
        except yaml.YAMLError as e:
            errors.append(f"{rel(p)}: invalid YAML: {e}")
            continue
        if not isinstance(items, list):
            errors.append(f"{rel(p)}: expected a list of use cases")
            continue
        grades = []
        for i, uc in enumerate(items):
            where = f"{rel(p)}[{i}] {uc.get('id', '?') if isinstance(uc, dict) else '?'}"
            if not isinstance(uc, dict):
                errors.append(f"{where}: not a mapping")
                continue
            for f in USE_CASE_REQUIRED:
                if f not in uc or uc[f] in (None, "", []):
                    errors.append(f"{where}: missing {f}")
            for f, vocab_key in ENUM_FIELDS.items():
                if f in uc and uc[f] not in VOCAB[vocab_key]:
                    errors.append(f"{where}: {f}={uc[f]!r} not in vocabulary")
            for wt in uc.get("work_types") or []:
                if wt not in VOCAB["work_types"]:
                    errors.append(f"{where}: work_type {wt!r} not in vocabulary")
            for o in uc.get("outcomes") or []:
                if isinstance(o, dict) and o.get("lever") not in VOCAB["value_levers"]:
                    errors.append(f"{where}: outcome lever {o.get('lever')!r} not in vocabulary")
                if isinstance(o, dict) and "provenance" in o and o["provenance"] not in VOCAB["provenance"]:
                    errors.append(f"{where}: outcome provenance {o['provenance']!r} not in vocabulary")
            for s in uc.get("sources") or []:
                if not isinstance(s, dict) or not s.get("url"):
                    errors.append(f"{where}: source without url")
                    continue
                if not DATE_RE.match(str(s.get("date", ""))):
                    errors.append(f"{where}: source {s.get('ref', '?')} has no valid date")
                if s.get("type") not in VOCAB["source_types"]:
                    errors.append(f"{where}: source type {s.get('type')!r} not in vocabulary")
                if "access" in s and s["access"] not in VOCAB["access"]:
                    errors.append(f"{where}: source access {s['access']!r} not in vocabulary")
            if uc.get("evidence_grade") == "D" and "idea" not in (
                str(uc.get("title", "")) + str(uc.get("notes", ""))
            ).lower():
                errors.append(f"{where}: grade D must be labelled 'idea'")
            uid = uc.get("id")
            if uid in seen:
                errors.append(f"{where}: duplicate id (also in {seen[uid]})")
            seen[uid] = rel(p)
            grades.append(uc.get("evidence_grade"))
        n = len(grades)
        ab = sum(g in ("A", "B") for g in grades)
        share = ab / n if n else 0
        msg = f"{rel(p)}: {n} use cases, {ab} graded A/B ({share:.0%})"
        reports.append(msg)
        if not (15 <= n <= 25) or share < 0.5:
            (errors if strict else warnings).append(msg + " — below targets (15–25, ≥50% A/B)")


def main():
    strict = "--strict" in sys.argv
    check_skill_md()
    check_markdown()
    check_links()
    check_use_cases(strict)
    for r in reports:
        print("INFO ", r)
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

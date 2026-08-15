#!/usr/bin/env python3
"""Validate this instruction-only Agent Skill without third-party packages."""

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def validate_frontmatter(failures: list[str]) -> None:
    text = (ROOT / "SKILL.md").read_text()
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md: missing leading YAML frontmatter", failures)
        return
    fields = dict(
        line.split(":", 1) for line in match.group(1).splitlines() if ":" in line
    )
    if fields.get("name", "").strip() != ROOT.name:
        fail("SKILL.md: name must match the repository directory", failures)
    if not fields.get("description", "").strip():
        fail("SKILL.md: description is required", failures)


def validate_links(failures: list[str]) -> None:
    for source in ROOT.rglob("*.md"):
        text = re.sub(r"```.*?```", "", source.read_text(), flags=re.DOTALL)
        for target in LINK.findall(text):
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if not clean or "://" in clean or clean.startswith("mailto:"):
                continue
            destination = (source.parent / clean).resolve()
            if not destination.exists():
                fail(f"{source.relative_to(ROOT)}: broken link {target}", failures)


def validate_json(failures: list[str]) -> None:
    for source in ROOT.rglob("*.json"):
        try:
            json.loads(source.read_text())
        except json.JSONDecodeError as error:
            fail(f"{source.relative_to(ROOT)}: {error}", failures)


def validate_hook(failures: list[str]) -> None:
    hook = ROOT / "hooks/claude-code/documentation_impact.py"
    result = subprocess.run([sys.executable, str(hook), "--self-test"], check=False)
    if result.returncode:
        fail("Claude Code hook self-test failed", failures)


def main() -> int:
    failures: list[str] = []
    validate_frontmatter(failures)
    validate_links(failures)
    validate_json(failures)
    validate_hook(failures)
    if failures:
        print("\n".join(f"FAIL: {item}" for item in failures), file=sys.stderr)
        return 1
    print("OK: skill frontmatter, local links, JSON, and hook")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

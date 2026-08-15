#!/usr/bin/env python3
"""Add a documentation-impact reminder after Claude edits a document."""

import json
import sys
from pathlib import Path
from typing import Optional


DOCUMENT_SUFFIXES = {".md", ".mdx", ".markdown", ".rst", ".adoc", ".txt"}


def response(payload: dict) -> Optional[dict]:
    path = payload.get("tool_input", {}).get("file_path", "")
    if Path(path).suffix.lower() not in DOCUMENT_SUFFIXES:
        return None
    return {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": (
                "Documentation changed. Before finishing, apply the documentation-impact "
                "checklist: confirm authority, contradictions, duplication, affected links, "
                "staleness, and whether a new file was actually necessary."
            ),
        }
    }


def self_test() -> None:
    assert response({"tool_input": {"file_path": "docs/plan.md"}})
    assert response({"tool_input": {"file_path": "src/app.py"}}) is None


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        self_test()
    else:
        result = response(json.load(sys.stdin))
        if result:
            json.dump(result, sys.stdout)

#!/usr/bin/env python3
"""beforeSubmitPrompt: block prompts that look like they contain secrets."""

from __future__ import annotations

import json
import re
import sys

SECRET_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN(?: RSA| OPENSSH| EC)? PRIVATE KEY-----"),
    re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
    re.compile(r"-----BEGIN [A-Z0-9][A-Z0-9 \-]{2,40}-----"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}"),
    re.compile(r"\bgho_[A-Za-z0-9]{20,}"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(
        r"api[_-]?key\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{20,}",
        re.IGNORECASE,
    ),
    re.compile(r"://[^\s:]+:[^\s@]+@"),
]


def _respond(continue_: bool, user_message: str | None = None) -> None:
    out: dict = {"continue": continue_}
    if user_message:
        out["user_message"] = user_message
    print(json.dumps(out))
    sys.exit(0)


def main() -> None:
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        _respond(True)

    prompt = data.get("prompt") or ""
    if not isinstance(prompt, str):
        prompt = str(prompt)

    for pat in SECRET_PATTERNS:
        if pat.search(prompt):
            _respond(
                False,
                user_message="Possible secret in prompt — remove before sending.",
            )

    _respond(True)


if __name__ == "__main__":
    main()

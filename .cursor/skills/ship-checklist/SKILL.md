---
name: ship-checklist
description: >-
  Pre-merge checklist: diff scope, tests, secrets, docs. Use before opening or
  merging a PR, when claiming ship-ready, or when the user says ship-checklist.
---

# Ship checklist

Copy and complete:

```
Ship:
- [ ] Diff matches approved plan / acceptance criteria (no drive-by)
- [ ] Tests run (stack command) — paste summary
- [ ] Lint/format run if overlay defines it
- [ ] No secrets in diff (.env, keys, tokens)
- [ ] Docs updated only if behavior/API changed (or N/A)
- [ ] reviewer findings addressed or waived with reason
- [ ] security findings addressed or waived with reason
- [ ] verifier verdict PASS (or BLOCKED explained)
```

## Output

Return the checklist with each item `done` / `fail` / `n/a` + one-line evidence. If any must-fix item fails, say **not ship-ready**.

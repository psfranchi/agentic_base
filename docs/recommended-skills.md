# Recommended skills (software development)

Skills teach **when/how** to do a recurring workflow. Agents encode **roles**. Keep skills short; put stack facts in the overlay (`stack-commands`), not in every skill.

## Already in this template

| Skill | Purpose |
|-------|---------|
| `explore-codebase` | Spawn explore for search/research; save builder context |
| `adopt-base` | Install this template into an app |
| `fill-stack-overlay` | Detect stack → `overlays/<stack>/` |
| `ship-checklist` | Pre-merge gate |
| `pr-review` | Structured review output (critical / suggestion / nit) |

Communication “caveman” / status compression is **in-repo** (`20-communication` + agent files) — not a separate skill and **not** an external pack to install.

## High-value skills to add (custom or adopt)

Create these when the pain shows up twice; don’t invent a zoo up front.

| Skill idea | When it pays off |
|------------|------------------|
| **`debug-incident`** | Reproduce → hypothesize → minimal fix → regression test; keeps debug out of random builder thrash |
| **`add-test`** | Given a behavior/bug, add the smallest failing then passing test in the project’s style |
| **`refactor-safe`** | Rename/extract only with characterization tests + no behavior change |
| **`migrate-schema`** | DB/API migration checklist (expand/contract, rollback, data backfill) |
| **`release-notes`** | Summarize commits/PR for changelog from git log + user-facing deltas |
| **`dependency-bump`** | Upgrade one dep: lockfile, changelog skim, run tests, note breaks |
| **`oncall-runbook`** | Product-specific: logs, health checks, rollback commands (per app) |
| **`api-contract`** | OpenAPI/JSON schema change + consumer impact checklist |

## Cursor / ecosystem skills worth adopting

- Stack-specific commands (your overlay’s `stack-commands` — always)
- Official Cursor skills you already use (e.g. create-rule, create-skill) — keep **personal** if not shared

## What not to skill-ify

- One-off product features (that’s planner → builder)
- Framework tutorials (link docs in overlay instead)
- Duplicate of an agent role (don’t make a “reviewer skill” that reimplements `reviewer`)

## How to add a custom skill

1. `.cursor/skills/<name>/SKILL.md` with a **trigger-rich** `description`
2. Steps + output shape; point at overlay commands for test/lint
3. Mention it in `AGENTS.md` or this file if it’s part of the default loop
4. Re-run `adopt-base` / copy into apps that need it

Rule of thumb: **agent** = who (role + permissions); **skill** = how/when for a repeatable procedure.

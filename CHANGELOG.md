# Changelog

All notable changes to this agentic template are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- README install guide tightened.

## [0.3.0] - 2026-09-15

### Added

- P2 skills: `debug-incident`, `add-test`, `migrate-schema` (stack-agnostic playbooks; commands from overlay).
- P3 docs: `docs/cloud-and-automations.md`, `docs/adopt-dry-run.md`; tiny `examples/smoke-app` for adopt dry-run (template-only, not copied into apps).
- `adopt-base` copies the new docs; notes that `examples/` stays in the template.

### Changed

- `docs/recommended-skills.md`, README skills inventory, and `AGENTS.md` mention the new repeatable skills.
- Light `.cursor/BUGBOT.md` pointer to `debug-incident` / `add-test` when relevant.

## [0.2.0] - 2026-09-15

### Changed

- Lean orchestrator loop: explore → Plan mode or planner → builder → STOP; reviewer / security / verifier on request or ship (`15-orchestrator`, `AGENTS.md`, `docs/workflow.md`).
- Architecture role removed; architecture fit lives in Plan mode / planner at design-time and builder at implement-time. Stale `architect.md` deleted on adopt upgrade.
- `fill-stack-overlay` and overlay docs: **always** copy `stack-commands` into `.cursor/skills/stack-commands/` (Cursor indexes that path reliably).

### Added

- P0 failClosed hooks: dangerous-git gate + secret scan on Write/StrReplace and on prompt (`.cursor/hooks.json`, `.cursor/hooks/`).
- Optional Bugbot notes (`.cursor/BUGBOT.md`) for ship complements.
- `docs/mcp.md` — practical MCP / integrations guide; no baked project `mcp.json` with servers.
- Template `VERSION` (`0.2.0`) and this `CHANGELOG.md`; on adopt, copied to `docs/agentic-base/` in the target app.

### Fixed

- Stack commands skill pointer documents both overlay source of truth and `.cursor/skills/` runtime path.

# Agentic base template

Tech-agnostic Cursor template: role agents, lean SDLC rules, reusable skills.

**Version:** [`VERSION`](VERSION) (`0.3.0`). History: [`CHANGELOG.md`](CHANGELOG.md). On adopt, both land under `docs/agentic-base/` (app changelog untouched).

No framework overlay ships. After install, **`fill-stack-overlay`** builds one from the app and always copies `stack-commands` into `.cursor/skills/`.

### Install

1. Put this repo next to the app (`projects/agentic_base` + `projects/my-app`).
2. Open **agentic_base** in Cursor.
3. Prompt: `Use this as the agentic template for ../my-app`
4. Agent runs **adopt-base** → **fill-stack-overlay**. Then work in **my-app**.

**Also accepts:** “install agentic base into …”, `/adopt-base`.

**Upgrade:** same prompt / re-sync; see [adopt-base Upgrade](.cursor/skills/adopt-base/SKILL.md#upgrade--re-sync). Version history: [CHANGELOG](CHANGELOG.md).

**Dry-run:** [docs/adopt-dry-run.md](docs/adopt-dry-run.md) + [examples/smoke-app](examples/smoke-app).

**What gets installed:** agents, rules, skills, hooks, BUGBOT, docs, `overlays/_template`, `docs/agentic-base` VERSION+CHANGELOG. **Not copied:** `examples/`.

**Manual copy:** same files as the [adopt-base file table](.cursor/skills/adopt-base/SKILL.md#2-install-files-agent-performs).

**Success:** after install + overlay, non-trivial work follows the lean role loop without re-explaining it. Core stays stack-agnostic; stack facts live under `overlays/<stack>/` in the app.

## What’s inside

| Area | Contents |
|------|----------|
| Contract | [`AGENTS.md`](AGENTS.md), [`VERSION`](VERSION), [`CHANGELOG.md`](CHANGELOG.md) |
| Docs | [`workflow`](docs/workflow.md), [`overlay-guide`](docs/overlay-guide.md), [`mcp`](docs/mcp.md), [`cloud-and-automations`](docs/cloud-and-automations.md), [`adopt-dry-run`](docs/adopt-dry-run.md), [`recommended-skills`](docs/recommended-skills.md) |
| Agents | [`.cursor/agents/`](.cursor/agents/) — explorer, planner, builder, reviewer, security, verifier |
| Rules | [`.cursor/rules/`](.cursor/rules/) — core, SDLC, orchestrator, communication, stack placeholder |
| Skills | [`.cursor/skills/`](.cursor/skills/) — adopt-base, fill-stack-overlay, explore-codebase, ship-checklist, pr-review, debug-incident, add-test, migrate-schema |
| Hooks / Bugbot | [`.cursor/hooks.json`](.cursor/hooks.json), [`.cursor/hooks/`](.cursor/hooks/), [`.cursor/BUGBOT.md`](.cursor/BUGBOT.md) |
| Overlay slot | [`overlays/_template/`](overlays/_template/) |
| Template-only | [`examples/smoke-app/`](examples/smoke-app/) — adopt dry-run stub (not copied into apps) |

## Roles + default loop

| Role | Job |
|------|-----|
| **explorer** | Search/map (readonly) |
| **planner** | Plan mid-Agent; architecture fit at design-time |
| **builder** | Implement approved plan |
| **reviewer** | Correctness / tests / regressions |
| **security** | OWASP / secrets |
| **verifier** | Prove acceptance criteria |

Default: explore (if searching) → plan (if non-trivial; Plan deny → planner) → build → **STOP** (suggest R/S/V). Ship: reviewer + security → verifier + ship-checklist; optional Bugbot + Cursor `/review-security`.

## Status compression (“caveman”)

In [`.cursor/rules/20-communication.mdc`](.cursor/rules/20-communication.mdc) — no third-party pack. Builder: terse status. Explorer/planner/reviewer/verifier: lite. Security, plans, errors/commits: never compressed.

## Deferred

- Format hooks — add later if needed.

See [CHANGELOG](CHANGELOG.md) for shipped work.

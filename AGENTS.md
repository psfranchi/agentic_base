# Agentic Base — Orchestration Contract

Tech-agnostic agent workflow. Stack details live in the active overlay (see Stack below).

## Roles

| Agent | Role | Edits? |
|-------|------|--------|
| `explorer` | Search, grep, map codebase; return paths + short findings | No |
| `planner` | Goals, constraints, file list, risks, test plan | No |
| `builder` | Implement approved plan only | Yes |
| `reviewer` | Adversarial correctness / tests / regressions | No |
| `security` | Injection, authz, secrets, unsafe defaults | No |
| `verifier` | Prove done: run checks, match acceptance criteria | No |

Main agent orchestrates. Prefer delegating to these subagents instead of replaying their job in the same context. Use skill **`explore-codebase`** (Task `explore`) for broad search so **builder** context stays small.

## Workflow

1. **Need to search / research the codebase?** → spawn **explorer** / Task `explore` first (skill `explore-codebase`).
2. **Non-trivial work, no approved plan yet** → **planner** first (or Plan mode). Wait for user approval when the plan changes scope or architecture.
3. **Build** → **builder** only from the approved plan. Smallest diff that satisfies it. Do not use builder as a search engine.
4. **Before claiming merge-ready** → `reviewer` + `security` (parallel OK) → then `verifier`.
5. **Ship** → use skill `ship-checklist`. Structured review output → skill `pr-review`.

## Git commits

When the user asks for a commit: use the human’s already-configured git identity only. Do not add `Co-authored-by` (or similar) for Cursor/AI. Do not change `user.name` / `user.email`. See `.cursor/rules/00-core.mdc`.

## Caveman (per role)

Status compression is defined in `.cursor/rules/20-communication.mdc` (no external skill install).

| Role | Intensity |
|------|-----------|
| builder | full (status only; never compress code/errors) |
| explorer, planner, reviewer, verifier | lite |
| security | off (normal prose) |

Drop compression for irreversible confirms and security warnings. Do not caveman-compress planner or security docs.

## Stack

No stack is pre-wired in this template. After install into an app, run skill `fill-stack-overlay` so these pointers become real:

- Overlay name: `_none_` (set to detected id, e.g. whatever `fill-stack-overlay` created)
- Stack brief: `overlays/<stack>/AGENTS.stack.md`
- Stack rules: `overlays/<stack>/rules/stack.mdc` → `.cursor/rules/90-stack.mdc`
- Commands skill: `overlays/<stack>/skills/stack-commands/`

Until then: discover commands and layout from the repo — do not invent stack facts.

To install into an app: keep this repo in the **parent folder** next to the app, then prompt “Use this as the agentic template for ../my-app” (`adopt-base`).

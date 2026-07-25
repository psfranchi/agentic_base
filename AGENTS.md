# Agentic Base — Orchestration Contract

Tech-agnostic agent workflow. Stack details live in the active overlay (see Stack below).

## Roles

| Agent | Role | Edits? |
|-------|------|--------|
| `planner` | Goals, constraints, file list, risks, test plan | No |
| `builder` | Implement approved plan only | Yes |
| `reviewer` | Adversarial correctness / tests / regressions | No |
| `security` | Injection, authz, secrets, unsafe defaults | No |
| `verifier` | Prove done: run checks, match acceptance criteria | No |

Main agent orchestrates. Prefer delegating to these subagents instead of replaying their job in the same context.

## Workflow

1. **Non-trivial work** → `planner` first (or Plan mode). Wait for user approval when the plan changes scope or architecture.
2. **Build** → `builder` only from the approved plan. Smallest diff that satisfies it.
3. **Before claiming merge-ready** → `reviewer` + `security` (parallel OK) → then `verifier`.
4. **Ship** → use skill `ship-checklist`. Structured review output → skill `pr-review`.

## Git commits

When the user asks for a commit: use the human’s already-configured git identity only. Do not add `Co-authored-by` (or similar) for Cursor/AI. Do not change `user.name` / `user.email`. See `.cursor/rules/00-core.mdc`.

## Caveman (per role)

| Role | Intensity |
|------|-----------|
| builder | full (status only; never compress code/errors) |
| planner, reviewer, verifier | lite |
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

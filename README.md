# Agentic base template

Tech-agnostic Cursor template for agentic programming: role agents, lean SDLC rules, and reusable skills.

No framework overlay is shipped. After install, skill **`fill-stack-overlay`** builds one from the app itself.

## How to use (prompt)

Clone or download this repo into the **parent folder** next to your apps (e.g. `projects/agentic_base` beside `projects/my-app`).

Open it in Cursor and prompt:

```text
Use this as the agentic template for ../my-app
```

The agent runs **`adopt-base`** then **`fill-stack-overlay`**. Continue work in the **app** project.

Same idea: “install agentic base into …”, `/adopt-base`.

## What’s inside

| Path | Purpose |
|------|---------|
| [`AGENTS.md`](AGENTS.md) | Orchestration contract — roles, workflow, stack pointers |
| [`docs/workflow.md`](docs/workflow.md) | explore → plan → build → review → secure → verify |
| [`docs/overlay-guide.md`](docs/overlay-guide.md) | How overlays are created and wired |
| [`docs/recommended-skills.md`](docs/recommended-skills.md) | Extra skills worth adding later |
| [`.cursor/agents/`](.cursor/agents/) | `explorer`, `planner`, `builder`, `reviewer`, `security`, `verifier` |
| [`.cursor/rules/`](.cursor/rules/) | Core, SDLC, **status compression** (`20-communication`), stack placeholder |
| [`.cursor/skills/`](.cursor/skills/) | `explore-codebase`, `adopt-base`, `fill-stack-overlay`, `ship-checklist`, `pr-review` |
| [`overlays/_template/`](overlays/_template/) | Empty slot used when generating a stack overlay |

## Roles (quick)

0. **explorer** (readonly, lite) — search/map; save builder context (`explore-codebase`)  
1. **planner** (readonly, lite) — plan only  
2. **builder** (writes, full status compression) — implement approved plan  
3. **reviewer** (readonly, lite) — correctness / tests / regressions  
4. **security** (readonly, normal prose) — confirmed vulns + fixes  
5. **verifier** (readonly, lite) — prove acceptance criteria  

Default loop: explore (if searching) → plan (if non-trivial, no plan yet) → build → review/secure → verify.

## Status compression (“caveman”)

Built into [`.cursor/rules/20-communication.mdc`](.cursor/rules/20-communication.mdc) and each agent file. **No** `npx skills add …` / third-party pack required.

- Builder: terse status while working  
- Explorer / planner / reviewer / verifier: lite  
- Security + plans + errors/commits: never compressed  

## Manual copy (optional)

Only if you install without the agent — same files as `adopt-base`. Still keep this repo in the parent folder so paths like `../my-app` work.

## Deferred

- Push gates, format hooks — add later if needed.

## Success check

After prompt install + overlay fill: non-trivial work uses the role loop without re-explaining it. Core stays framework-agnostic; stack facts live under `overlays/<stack>/` for that app only.

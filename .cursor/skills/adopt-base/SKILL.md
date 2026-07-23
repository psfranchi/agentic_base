---
name: adopt-base
description: >-
  Install this agentic template into an application repo by copying agents,
  rules, skills, and docs, then running fill-stack-overlay. Use when the user
  says adopt-base, install agentic base, use this as the agentic template,
  apply agentic template to …, wire Cursor agents into my app, or points at
  agentic_base as the template for another project.
---

# Adopt agentic_base

## Goal

Install this template into a target app **for the user**. Prefer doing the file copies yourself (tools) — do **not** make the user run a long `cp` script unless they ask for commands only.

Then generate the stack overlay with `fill-stack-overlay` from the target app.

## Layout assumption

This repo lives in the **parent folder** next to application repos (e.g. `…/projects/agentic_base` and `…/projects/my-app`). Targets are usually `../my-app`.

## Trigger examples (user prompts)

- “Use this as the agentic template for `../my-app`”
- “Install agentic_base into …”
- “/adopt-base” / “adopt-base”

## Steps

```
Adopt progress:
- [ ] 1. Resolve source (this template) + target app path
- [ ] 2. Copy/merge core files into the target (you do it)
- [ ] 3. fill-stack-overlay on the target
- [ ] 4. Confirm AGENTS.md Stack section
- [ ] 5. Tell user to open/continue in the app workspace
```

### 1. Paths

- **Source**: this `agentic_base` root (where these skills live).
- **Target**: path the user gave (typically a sibling under the same parent folder).

If target is unclear, ask once. If target `.cursor/` exists, ask before overwrite — merge by default (keep their extras; replace/update our named agent/rule/skill files).

### 2. Install files (agent performs)

Copy from source → target:

| From | To |
|------|----|
| `AGENTS.md` | target root (merge Stack if they already have AGENTS.md) |
| `docs/workflow.md`, `docs/overlay-guide.md` | `target/docs/` |
| `.cursor/agents/*.md` | `target/.cursor/agents/` |
| `.cursor/rules/00-core.mdc`, `10-sdlc.mdc`, `20-communication.mdc`, `90-stack-placeholder.mdc` | `target/.cursor/rules/` |
| `.cursor/skills/**` | `target/.cursor/skills/` |
| `overlays/_template/` | `target/overlays/_template/` |

Create directories as needed. Do not invent a pre-filled framework overlay.

### 3. Overlay

Follow skill **`fill-stack-overlay`** on the **target** app (detect stack, write `overlays/<stack>/`, wire `90-stack.mdc`).

### 4. Done

Summarize what was installed and the stack id. Tell the user to keep chatting in the **app** project for day-to-day work.

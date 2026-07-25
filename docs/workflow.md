# Workflow: plan → build → review → secure → verify

## When to plan

Use `planner` (or Plan mode) when any of these apply:

- Multiple files or layers change
- API / schema / auth behavior changes
- Ambiguous requirements or more than one valid approach
- Estimated work > ~15 minutes of agent work

Skip a formal plan for trivial one-file fixes with an obvious approach — still keep the change small and tested.

## Plan output (required shape)

1. Goal (one sentence)
2. Constraints / non-goals
3. Files likely touched
4. Steps (ordered)
5. Risks / unknowns
6. Test plan (commands + cases)
7. Acceptance criteria (checkable)

Do not implement during planning.

## Build

- Follow the approved plan only.
- Prefer existing patterns in the repo.
- Run the project test/lint commands from the stack overlay after meaningful changes.
- If the plan is wrong, stop and re-plan — do not silently expand scope.
- Commits (only when the user asks): sole author = configured human git identity; no AI/`Cursor` co-author trailers; never change git config.

## Review + security

Run after a coherent diff exists (feature complete or PR-ready):

- `reviewer`: correctness, missing tests, contract breaks, regressions. Not style nits.
- `security`: confirmed vulns and unsafe defaults with severity + concrete fix.

Feed findings back to `builder`. Re-run review on material fixes.

## Verify

`verifier` blocks “looks done”:

1. Acceptance criteria from the plan — each pass/fail
2. Commands from overlay actually run (or note why blocked)
3. Explicit list of remaining gaps

Only then claim merge-ready. Use `ship-checklist` before open/merge PR.

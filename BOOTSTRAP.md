# Minimal Bootstrap Prompt

Use this file as the canonical reference for starting a new session with minimal instruction overhead.

## Session Start Mode

## Operator Session Start Template

Use this short opener at the beginning of a fresh session before providing the actual task.

```md
Follow `BOOTSTRAP.md` as the session bootstrap.
Initialize only the minimal instruction context.
Do not assume a task yet.
Wait for the operator's problem description before loading additional guides, project/domain files, or task files.
```

## When To Use It
- start of a new session
- before task-specific context is known
- when you want the agent to minimize startup token usage

## Minimal Load Policy

```md
Follow `AGENTS.md` as the bootstrap router.

Load only:
- `instructions/core/session-contract.md`
- the single most relevant file from `instructions/guides/`
- `instructions/project/index.md` when it exists
- only the touched files from `instructions/project/`
- only the specific files from `instructions/skills/` that `instructions/project/` routes to
- `instructions/domain/` or `instructions/shared-domain/` only when reusable abstractions are relevant
- the active task directory in `instructions/work/` only when continuing a task, planning approved implementation, or writing a checkpoint

Keep all other instruction files cold until they are required by the task.
If the relevant guide or touched area is unclear, ask before loading more.
If the repository has no `instructions/project/` documentation yet, keep `instructions/project-template/` cold unless the operator asks for onboarding or documentation generation.
```

## Notes
- This prompt is intended for analysis-first session startup.
- The session-start opener above can be injected first, with the minimal load policy treated as the behavior it should follow.
- For implementation work, continue following the approval and planning flow defined in `instructions/core/session-contract.md`.
- Expected initial load after the opener:
  - `AGENTS.md`
  - `instructions/core/session-contract.md`
  - `instructions/project/index.md` when it exists

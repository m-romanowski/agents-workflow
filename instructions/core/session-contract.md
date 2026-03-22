# Session Contract

## Role
- Treat the agent as a technical pair-programmer.
- Treat the operator as the final decision-maker for changes, scope, and acceptance.
- Stay concise, direct, and critical where needed.
- If anything is unclear, uncertain, or conflicting, stop and ask.

## Approval
- Proposal first, execution second.
- Do not execute codebase changes, branch changes, commits, installs, or validation commands without operator approval.
- When options exist, present the intended action and the available choices before acting.
- If scope, assumptions, or approach change, ask again before continuing.
- Drafting or updating files inside `instructions/work/` for planning is allowed before implementation approval.

## Planning
- Plan every codebase change before implementation.
- For each task, create or update a dedicated directory under `instructions/work/` using `NNN-short-task-name/`.
- Keep plans small, explicit, and reviewable.
- Work from the approved `TODO.md`.
- Execute one approved step at a time.
- Update the task files before changing the main codebase if the plan or approach changes.

## Checkpoints
- After each completed and accepted step, add a checkpoint file in the active task directory.
- Keep checkpoints concise and resumable.
- Before continuing a task, verify that `TODO.md` and the latest checkpoint still match the approved state.

## Git
- Use git as the workflow for codebase changes.
- Before starting a codebase change and before any commit, check whether the current branch is appropriate.
- Do not create, switch, or commit to a default or protected branch such as `main` unless the operator explicitly approves it.
- After an accepted step, ask whether it should be committed.
- Do not commit unreviewed or unaccepted work.

## Documentation Routing
- Load only the guides and repository/domain files needed for the current task.
- Keep documentation policy files cold unless the task involves documentation maintenance or accepted work changes documented structure, commands, or domain behavior.
- Load the active task directory only when continuing existing work, planning approved implementation, or recording checkpoints.
- Keep repo-specific domain documentation in `instructions/project/` unless the operator explicitly establishes another permanent location.

# Session Contract

## Role
- Treat the agent as a technical pair-programmer.
- Treat the operator as the final decision-maker for changes, scope, and acceptance.
- Stay concise, direct, and critical where needed.
- If anything is unclear, uncertain, or conflicting, stop and ask.

## Modes

- Default mode is discussion-first: behave as `wf:discuss wf:light wf:cold wf:no-track` unless the operator says otherwise.
- Explicit mode commands override inferred intent.
- Explicit modifiers override mode defaults.
- Repository workflow and safety rules remain higher priority than optional workflow shortcuts.
- `wf:track` is implicit for `wf:plan` and `wf:implement`.
- `wf:no-track` is only valid for `wf:discuss` and `wf:review`.
- Optional aliases may be used as shorthand, but the full `wf:` forms remain canonical.

Supported aliases:

- `wf:d` -> `wf:discuss`
- `wf:p` -> `wf:plan`
- `wf:i` -> `wf:implement`
- `wf:r` -> `wf:review`
- `wf:s` -> `wf:status`
- `wf:l` -> `wf:light`
- `wf:f` -> `wf:full`
- `wf:c` -> `wf:cold`
- `wf:t` -> `wf:track`
- `wf:nt` -> `wf:no-track`

### `wf:discuss`

- Conversation, analysis, and tradeoff exploration only.
- Keep instruction loading minimal.
- Do not create or update `instructions/work/`.
- Do not edit the main codebase, switch branches, commit, install dependencies, or run validation unless the operator explicitly asks.

### `wf:plan`

- Planning and scoping mode for durable work preparation.
- Treat `wf:plan` as tracked by default and create or update `instructions/work/`.
- Do not edit the main codebase or run implementation validation.
- Keep plans explicit and reviewable before implementation starts.

### `wf:implement`

- Use approved plans to edit the main codebase.
- Treat `wf:implement` as tracked by default and work from `instructions/work/`.
- Confirm approval before starting code changes, branch changes, installs, commits, or validation commands.
- Update task records first when the approved plan changes.

### `wf:review`

- Inspect code, design, or diffs and report findings first.
- Route `wf:review` through investigation guidance unless a more specific review guide exists for the task.
- Do not edit files unless the operator explicitly asks to move from review into planning or implementation.

### `wf:status`

- Summarize the current mode, active assumptions, and next step.

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
- For tracked tasks, treat the `TODO.md` front matter as the canonical current-state record for routing and status checks.
- Use the `TODO.md` body as the operator-readable plan and ordered step list, not as the primary source for inferring current state when front matter is present.
- Execute one approved step at a time.
- Update the task files before changing the main codebase if the plan or approach changes.
- Do not create tracked planning artifacts during `wf:discuss` unless the operator explicitly switches to tracked work.

## Checkpoints
- After each completed and accepted step, add a checkpoint file in the active task directory.
- Keep checkpoints concise and resumable.
- Before continuing a task, read the `TODO.md` front matter first, then verify that the latest checkpoint still matches the approved state.

## Tracked Task Routing
- On tracked work, read the active task `TODO.md` front matter before reading any other file in the task directory.
- Treat front matter as authoritative for the current task status, mode, current step, approved steps, latest checkpoint, approval requirements, and routing boundaries.
- Do not infer current task state from prose in `README.md`, milestone files, or checkpoints when the front matter is present and complete.
- Load `README.md` only for task context, rationale, or scope details.
- Load milestone files only when milestone-level acceptance criteria or dependencies are needed.
- Load checkpoints only for accepted-history review, task resumption verification, or drift investigation.
- If front matter and markdown body disagree, front matter wins until the task record is explicitly updated.
- If the front matter is missing, incomplete, or contradictory, stop and ask the operator or repair the task record before proceeding.

## Git
- Use git as the workflow for codebase changes.
- Before starting a codebase change and before any commit, check whether the current branch is appropriate.
- Do not create, switch, or commit to a default or protected branch such as `main` unless the operator explicitly approves it.
- Use Conventional Commits for commit messages.
- After an accepted step, ask whether it should be committed.
- A completed tracked task should be committed before starting the next tracked task unless the operator explicitly chooses not to commit it yet.
- Do not commit unreviewed or unaccepted work.

## Documentation Routing
- Load only the guides and repository/domain files needed for the current task.
- Keep documentation policy files cold unless the task involves documentation maintenance or accepted work changes documented structure, commands, or domain behavior.
- Load the active task directory only when continuing existing work, planning approved implementation, or recording checkpoints.
- Keep repo-specific domain documentation in `instructions/project/` unless the operator explicitly establishes another permanent location.
- In `wf:light` mode, prefer the smallest instruction set that still supports the active mode correctly.
- In `wf:cold` mode, keep optional skills, project docs, and domain docs unloaded until routing or the operator request makes them necessary.

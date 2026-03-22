# Work Directory

Create one operator-approved subdirectory in this location for each active task.

Task naming:
- Use the format `NNN-short-task-name/`.
- Keep the numeric prefix sortable and unique.
- Keep the name short and descriptive.
- Unless the operator says otherwise, the highest numbered task directory is the latest task.

Task continuation:
- Before continuing the latest task, check its status in `TODO.md` and the latest checkpoint.
- If the latest task is completed, do not resume it automatically.
- Ask the operator whether to create a new task, reopen the completed task, or continue it with an explicit status update.
- If a completed task is resumed, update the task files first so the active status is clear.

Required minimum layout:
- `README.md`: task summary, approved scope, and accepted approach
- `TODO.md`: ordered approved steps
- at least one `milestone-xxx.md` file: milestone details and acceptance criteria
- one new `checkpoint-xxx.md` file after each accepted completed step

Exception for early discovery:
- a lightweight task may begin with only `README.md` and `TODO.md`
- add milestone files before the task grows into multiple reviewable phases or before the operator needs milestone-level approval

Minimum contents:
- `README.md`: task context, goal, scope boundaries, chosen approach, and any open questions for the operator
- `TODO.md`: ordered step list, milestone grouping, and current status of each step
- `milestone-xxx.md`: milestone goal, acceptance criteria, dependencies, and notes relevant to implementation or review
- `checkpoint-xxx.md`: completed step summary, accepted outcomes, documentation updates, follow-up items, and next planned step

For discovery-oriented tasks, `README.md` should also include:
- current architecture context
- relevant domain context
- explicit current-state observations
- proposed future-state options
- operator-accepted decisions, if any
- options and tradeoffs
- recommended direction
- assumptions and uncertainties
- blockers or missing inputs
- next milestone if the operator wants to continue

For discovery-oriented tasks, keep a clear distinction between:
- what is observed in the current codebase or documentation
- what is being proposed as a future solution
- what the operator has explicitly accepted

Keep the task files updated before changing the main codebase when operator feedback changes the plan.

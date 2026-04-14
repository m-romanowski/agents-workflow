# Work Directory

Create one operator-approved subdirectory in this location for each active task.

Task naming:
- Use the format `NNN-short-task-name/`.
- Keep the numeric prefix sortable and unique.
- Keep the name short and descriptive.
- Unless the operator says otherwise, the highest numbered task directory is the latest task.

Task continuation:
- Before continuing the latest task, read the `TODO.md` front matter first and use it as the canonical current-state source.
- Read the latest checkpoint only when verifying accepted history, resuming interrupted work, or investigating drift.
- If the latest task is completed, do not resume it automatically.
- Ask the operator whether to create a new task, reopen the completed task, or continue it with an explicit status update.
- If a completed task is resumed, update the task files first so the active status is clear.

Required minimum layout:
- `README.md`: task summary, approved scope, and accepted approach
- `TODO.md`: ordered approved steps
- at least one `milestone-xxx.md` file: milestone details and acceptance criteria
- one new `checkpoint-xxx.md` file after each accepted completed step

`TODO.md` is the operational file for tracked work.

It must begin with a compact YAML front matter block that carries the canonical current-state fields used for routing and status checks.

Exception for early discovery:
- a lightweight task may begin with only `README.md` and `TODO.md`
- add milestone files before the task grows into multiple reviewable phases or before the operator needs milestone-level approval

Minimum contents:
- `README.md`: task context, goal, scope boundaries, chosen approach, and any open questions for the operator
- `TODO.md`: ordered step list, milestone grouping, and current status of each step
- `milestone-xxx.md`: milestone goal, acceptance criteria, dependencies, and notes relevant to implementation or review
- `checkpoint-xxx.md`: completed step summary, accepted outcomes, documentation updates, follow-up items, and next planned step

Required `TODO.md` front matter fields:
- `task_id`: task directory identifier such as `002-front-matter-routing`
- `title`: short task title
- `status`: one of `draft`, `active`, `blocked`, or `completed`
- `mode`: current workflow mode for the task such as `plan` or `implement`
- `tracking`: `track`
- `current_phase`: short phase label such as `planning`, `implementation`, or `review`
- `current_step`: the only step that should be treated as active for execution; use `null` only when `status` is `completed`
- `current_milestone`: active milestone identifier
- `step_status`: mapping of step ids to `pending`, `approved`, `in_progress`, or `accepted`
- `approved_steps`: ordered list of steps approved for execution
- `latest_checkpoint`: latest accepted checkpoint filename or `null`
- `resume_from`: step id to resume from; use `null` only when `status` is `completed`
- `allowed_paths`: repo-relative path prefixes allowed for the current task scope
- `requires_operator_approval`: actions that still require explicit operator approval
- `last_updated`: date of the latest task-state update

Canonical example:

```md
---
task_id: 002-front-matter-routing
title: Front Matter Routing For Tracked Work
status: active
mode: implement
tracking: track
current_phase: implementation
current_step: step-02
current_milestone: milestone-001
step_status:
  step-01: accepted
  step-02: in_progress
  step-03: pending
approved_steps:
  - step-01
  - step-02
latest_checkpoint: checkpoint-001-example.md
resume_from: step-02
allowed_paths:
  - instructions/core/
  - instructions/work/002-front-matter-routing/
requires_operator_approval:
  - validation
  - commit
  - scope_change
last_updated: 2026-04-14
---
```

Routing rules:
- Read the `TODO.md` front matter first when continuing or resuming tracked work.
- Treat front matter as the canonical current-state source.
- Use front-matter routing only for tracked work in `/plan` or `/implement`; do not load task routing state during `/discuss /no-track` or `/review /no-track`.
- Do not scan `README.md`, milestone files, or checkpoints to infer current state when the front matter is present and complete.
- Read the `TODO.md` body for plan details and ordered steps after the front matter establishes the current state.
- Read `README.md` only when additional context, rationale, or scope explanation is needed.
- Read the latest checkpoint only when verifying accepted history, resuming interrupted work, or investigating drift.
- If front matter and the markdown body differ, front matter wins until the task file is updated.
- If front matter is missing, incomplete, or contradictory, fix the task record first or ask the operator before continuing.
- If `status` is `completed`, `current_step` and `resume_from` should be `null` and the task must not be resumed automatically.

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

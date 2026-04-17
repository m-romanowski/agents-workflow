# Code Changes

Use this guide for normal code edits, including features, bug fixes, refactors, and maintenance changes.

## Default Loop
1. Create or update the active task directory in `instructions/work/`.
2. Write or revise the plan, milestones, and `TODO.md`.
3. Ask the operator to review and approve the plan.
4. Implement one approved step only.
5. Ask the operator to review the result.
6. If feedback changes the work, update the task files first.
7. After acceptance, write a checkpoint file.
8. Ask whether the accepted step should be committed.
9. When the task is complete, commit the accepted task before starting the next tracked task unless the operator explicitly says otherwise.
10. Continue only after operator approval.

## Guide Selection
- Load any additional guides that are clearly relevant to the current task.
- If it is unclear whether another guide applies, ask the operator before proceeding.

## Constraints
- Keep steps small and independently reviewable.
- Do not batch multiple milestones into one implementation pass unless the operator explicitly approves that.
- If code changes reveal hidden issues or new scope, stop and discuss them before proceeding.

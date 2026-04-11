# Project Index

## Purpose

- repository-local routing for workflow customization documentation
- keeps optional skill and recommendation docs cold during normal implementation work

## Load By Task Type

### Workflow Customization Or Agent Setup

Load:

- `instructions/project/skill-profile.md`

Then:

- load `instructions/project/recommended-third-party-skills.md` only when the operator asks about optional or recommended third-party skills

### Normal Coding, Review, Or Investigation Tasks

- do not load workflow-customization docs by default
- load them only when the operator explicitly asks about optional skills, personal workflow extensions, or agent setup behavior

## Canonical Project Files

- `instructions/project/skill-profile.md`
- `instructions/project/recommended-third-party-skills.md`

## Notes

- optional third-party skills are never assumed installed
- operator-requested personal skills remain explicit and session-scoped
- repository workflow and safety rules remain higher priority than optional skill behavior

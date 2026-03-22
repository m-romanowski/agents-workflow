# React JS Review

## Scope

- code review cues specific to React component code, hooks usage, and UI structure

## Review Focus

- component responsibilities remain clear
- state, props, and side effects are understandable
- hooks usage is predictable and not hiding behavior
- component composition supports maintainability

## Common Findings To Look For

- components taking on too many responsibilities
- unclear state ownership or duplicated derived state
- hooks with dependency behavior that is hard to reason about
- side effects mixed too tightly with rendering concerns

## Escalate To Project Docs When

- repository-specific frontend structure rules may override generic React guidance
- the touched area is known to differ from the repository default

## Project Override Note

- repository and module docs win when they define stricter local review expectations

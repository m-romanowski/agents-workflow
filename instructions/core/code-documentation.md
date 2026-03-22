# Code Documentation

- Prefer self-explanatory code over inline comments.
- Do not add comments for routine logic, obvious control flow, or straightforward implementation details.
- Keep durable explanations in `instructions/project/`, `instructions/domain/`, or the active task files in `instructions/work/`.
- The default expectation is that source code should be understandable through naming, structure, and small focused units.

## Allowed Comment Cases
- Non-obvious constraints that cannot be expressed clearly in code alone
- External integration quirks
- Required workarounds
- Temporary notes explicitly approved by the operator

## Disallowed Comment Patterns
- Restating what the code already says
- Line-by-line narration
- Business logic explanations that belong in domain docs
- Structural or workflow notes that belong in repository documentation

## Review Rule
- If a change seems to require extensive comments to become understandable, improve the code structure first and ask the operator before relying on comments.

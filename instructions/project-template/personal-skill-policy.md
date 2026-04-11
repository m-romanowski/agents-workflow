# Personal Skill Policy Template

## Purpose

- template for documenting how repository workflow interacts with optional personal third-party skills
- keeps optional personal-skill policy separate from reusable-skill routing

## Template Rules

- keep this file cold by default
- load it only for workflow customization, agent setup, or operator-requested personal-skill usage
- keep optional personal skills explicit, session-scoped, and subordinate to repository workflow rules
- do not use this file to declare private installed-skill state, secrets, or operator-specific environment details

## Suggested Sections

- purpose
- personal skill usage
- activation pattern
- precedence
- storage model

## Usage Pattern

- optional personal third-party skills may be used only when the operator explicitly requests them
- do not assume recommended or previously used third-party skills are installed in the active agent environment
- do not load optional personal skills by default during bootstrap or normal coding work
- treat optional personal skill activation as session-scoped unless the operator explicitly states otherwise

## Precedence Pattern

- repository workflow, safety, and approval rules override optional personal skill behavior
- repository formatting and documentation rules override optional stylistic preferences from personal skills
- operator instructions override both repository docs and optional skill behavior

## Storage Model Pattern

- store actual installed third-party skills in the active agent environment, not in the repository
- store operator-level installed-skill registry or cross-agent personal skill notes outside the repository
- use repository docs only for workflow bridge and public recommendation content relevant to that codebase

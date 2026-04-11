# Personal Skill Policy

## Purpose

- define how optional personal third-party skills may be used in this repository
- keep personal skill usage explicit, session-scoped, and subordinate to repository workflow rules

## Personal Skill Usage

- optional personal third-party skills may be used only when the operator explicitly requests them
- do not assume that any recommended or previously used third-party skill is installed in the active agent environment
- do not load optional personal skills by default during bootstrap or normal coding work
- treat optional personal skill activation as session-scoped unless the operator explicitly states otherwise

## Activation Pattern

Examples of explicit activation:

- `caveman mode on`
- `$caveman`
- `use caveman for this session`

Examples of explicit deactivation:

- `caveman mode off`
- `normal mode`
- `stop using caveman`

## Precedence

- repository workflow, safety, and approval rules override optional personal skill behavior
- repository formatting and documentation rules override optional stylistic preferences from personal skills
- operator instructions override both repository docs and optional skill behavior

## Storage Model

- store actual installed third-party skills in the active agent environment, not in this repository
- store operator-level installed-skill registry or cross-agent personal skill notes outside this repository
- use this repository only for the workflow bridge and public recommendations relevant to this codebase

### Suggested Locations

- Codex installed skills: `$CODEX_HOME/skills/` such as `~/.codex/skills/`
- operator-level cross-agent registry: a personal workflow location outside the repository, such as `~/.config/agents-workflow/skills/`
- repository-local bridge and recommendation docs: `instructions/project/`

### Repository Scope

- use `instructions/project/personal-skill-policy.md` to describe how optional personal skills may be activated for work in this repository
- use `instructions/project/recommended-third-party-skills.md` to list optional public recommendations
- do not store private installation state, tokens, or environment-specific secrets in repository docs

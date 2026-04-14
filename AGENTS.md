# AGENTS.md

## Purpose
This file is the entry point for agent behavior in this repository.

Read instructions in this order:
1. `instructions/core/session-contract.md`
2. One relevant file in `instructions/guides/`
3. `instructions/project/index.md` when it exists for the repository
4. Only the relevant files in `instructions/skills/` when `instructions/project/` routes to them
5. Only the relevant files in `instructions/project/`
6. Only the relevant files in `instructions/shared-domain/` when repository-local routing or the operator request indicates shared cross-repository domain context is needed
7. Only the relevant files in `instructions/domain/` when reusable domain abstractions are needed
8. The active task directory in `instructions/work/` only when needed for continuation, approved planning, or checkpoints; for tracked work, read the active task `TODO.md` front matter first and treat it as the canonical current-state source

## Mode Commands

Use these explicit commands to control workflow and instruction loading:

- `/discuss`: conversation only; keep loading minimal and do not create task records
- `/plan`: planning mode; tracked task records are required, but do not edit the main codebase
- `/implement`: implementation mode; edit the main codebase only after explicit operator approval
- `/review`: review-only mode; route to investigation guidance and report findings without editing unless the operator asks
- `/status`: summarize the current mode, assumptions, and next expected step

Optional modifiers:

- `/light`: minimum viable instruction loading for the active mode
- `/full`: load all docs clearly relevant to the active mode
- `/cold`: keep optional docs and skills unloaded unless they become necessary
- `/track`: require durable records under `instructions/work/`
- `/no-track`: forbid durable records under `instructions/work/` for discussion or review work

Defaults when no explicit mode command is given:

- behave as `/discuss /light /cold /no-track`
- do not infer tracked work from exploratory conversation alone
- treat explicit mode commands as higher priority than inferred intent
- treat `/plan` and `/implement` as tracked modes even when `/track` is omitted

## Loading Rules
- `instructions/core/session-contract.md` always applies.
- Load one relevant guide from `instructions/guides/` based on the current phase of work.
- During bootstrap before the operator provides a task, do not load any guide yet.
- For explicit discussion mode, prefer the smallest useful guide footprint and keep task records cold.
- Route `/review` to `instructions/guides/investigation.md`.
- For hypothetical or future feature exploration, load `instructions/guides/feature-discovery.md`.
- If the applicable guide set is unclear, ask the operator.
- If the task touches a business domain shared across multiple repositories or services, use repository-local routing and the operator request to confirm which shared-domain files are relevant before loading them.
- When multiple guides apply, follow the guide that matches the current phase of work:
- Discovery and analysis first.
- Implementation only after the operator approves moving forward.
- Use `instructions/project/index.md` to decide which repository-local docs to load when that file exists.
- Use `instructions/project/index.md` and `instructions/project/skill-profile.md` to decide whether any reusable skill files in `instructions/skills/` are relevant when those files exist.
- Keep optional personal-skill policy docs under `instructions/project/` cold unless the task is about workflow customization, agent setup, or operator-requested personal skills.
- If repository project docs do not exist yet and the operator asks for onboarding or documentation generation, use `instructions/core/project-overview-preparation.md` and `instructions/project-template/` as the source pattern.
- Do not load `instructions/skills/` by default at session start.
- Load only the specific skill files routed by project docs and required by the task.
- Use `instructions/project/` for repository-local mapping of how this codebase participates in shared domains.
- Load only the project files needed for the touched area.
- Load only the domain files needed for the touched area when reusable domain abstractions are relevant.
- The operator request itself is a valid source for deciding which project and domain files are relevant.
- Load the active task directory only when continuing a task, planning approved implementation, or recording checkpoints.
- For tracked work, read only the active task `TODO.md` front matter first to determine current status, mode, current step, approvals, and routing boundaries.
- Do not scan `README.md`, milestone files, or checkpoints to infer current task state when the `TODO.md` front matter is present and complete.
- Load the `TODO.md` body only when the ordered step list or operator-readable plan details are needed.
- Load `README.md` only when task context, rationale, or scope explanation is needed.
- Load the latest checkpoint only when resuming work, verifying accepted history, or investigating drift between the current task state and prior accepted outcomes.
- If the `TODO.md` front matter is missing, incomplete, or contradictory, stop and ask the operator or repair the task record before proceeding.
- Do not load or create `instructions/work/` artifacts during `/discuss` unless the operator explicitly switches to tracked work.
- Do not treat `/no-track` as valid for `/plan` or `/implement`.
- Keep documentation-policy files in `instructions/core/` cold unless the task involves documentation maintenance or accepted work requires updating repository or domain docs.

## Directory Map
- `instructions/core/`: reusable workflow rules intended to be portable across repositories
- `instructions/guides/`: reusable task-type guidance intended to stay portable across repositories
- `instructions/skills/`: reusable technical and engineering skill guidance loaded through project routing
- `instructions/project-template/`: reusable templates for generating repository-specific files under `instructions/project/`
- `instructions/shared-domain/`: cross-repository business/domain knowledge shared by multiple systems or services
- `instructions/project/`: repository-specific references
- `instructions/domain/`: reusable domain abstractions and templates
- `instructions/work/`: active task plans, TODOs, milestones, and checkpoints

## Template Separation
- Treat `instructions/core/` and `instructions/guides/` as the shared template layer.
- Keep the shared template layer generic, reusable, and repository-agnostic.
- Do not place project-specific architecture, stack details, domain terms, or local constraints in `instructions/core/` or `instructions/guides/`.
- Keep `instructions/skills/` reusable across repositories; do not place repo-specific paths, package names, or local architecture decisions there.
- Keep `instructions/project-template/` reusable and generic; use it to generate repository-specific files, not as active project documentation.
- Put repository-specific knowledge in `instructions/project/` or the active task files in `instructions/work/`.
- Put cross-repository business knowledge in `instructions/shared-domain/` when that knowledge is intended to be reused across multiple repos or services.
- Change `instructions/core/` or `instructions/guides/` only when improving the reusable workflow for multiple repositories, not when documenting a single project.
- Change `instructions/skills/` when improving reusable technical guidance or skill routing patterns across repositories.
- Change `instructions/project-template/` when improving how repository-local project documentation is generated across repositories.
- If a proposed rule does not make sense in a different repository, it probably does not belong in the shared template layer.
- Treat `instructions/domain/` as the abstraction layer for reusable domain templates or cross-project domain structures, not as the default home for repo-specific domain notes.
- Keep repository-specific domain documentation in `instructions/project/` unless the operator explicitly introduces a different permanent location.

## Path Style
- In repository documentation, prefer repo-relative paths and relative markdown links.
- Do not write absolute local filesystem paths such as `/Users/...` into repository files unless the operator explicitly asks for environment-specific documentation.
- Keep examples portable across machines and clones.

## Priority
- Operator instructions override everything else.
- Repository-local instruction files override generic assumptions.
- If instructions conflict or anything is unclear, stop and ask the operator.

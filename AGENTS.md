# AGENTS.md

## Purpose
This file is the entry point for agent behavior in this repository.

Read instructions in this order:
1. `instructions/core/session-contract.md`
2. One relevant file in `instructions/guides/`
3. `instructions/project/index.md` when it exists for the repository
4. Only the relevant files in `instructions/skills/` when `instructions/project/` routes to them
5. Only the relevant files in `instructions/shared-domain/`
6. Only the relevant files in `instructions/project/`
7. Only the relevant files in `instructions/domain/` when reusable domain abstractions are needed
8. The active task directory in `instructions/work/` only when needed for continuation, approved planning, or checkpoints

## Loading Rules
- `instructions/core/session-contract.md` always applies.
- Load one relevant guide from `instructions/guides/` based on the current phase of work.
- For hypothetical or future feature exploration, load `instructions/guides/feature-discovery.md`.
- If the applicable guide set is unclear, ask the operator.
- If the task touches a business domain shared across multiple repositories or services, load the relevant files from `instructions/shared-domain/` first.
- When multiple guides apply, follow the guide that matches the current phase of work:
- Discovery and analysis first.
- Implementation only after the operator approves moving forward.
- Use `instructions/project/index.md` to decide which repository-local docs to load when that file exists.
- Use `instructions/project/index.md` and `instructions/project/skill-profile.md` to decide whether any reusable skill files in `instructions/skills/` are relevant when those files exist.
- If repository project docs do not exist yet and the operator asks for onboarding or documentation generation, use `instructions/core/project-overview-preparation.md` and `instructions/project-template/` as the source pattern.
- Do not load `instructions/skills/` by default at session start.
- Load only the specific skill files routed by project docs and required by the task.
- Use `instructions/project/` for repository-local mapping of how this codebase participates in shared domains.
- Load only the project files needed for the touched area.
- Load only the domain files needed for the touched area when reusable domain abstractions are relevant.
- The operator request itself is a valid source for deciding which project and domain files are relevant.
- Load the active task directory only when continuing a task, planning approved implementation, or recording checkpoints.
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

## Priority
- Operator instructions override everything else.
- Repository-local instruction files override generic assumptions.
- If instructions conflict or anything is unclear, stop and ask the operator.

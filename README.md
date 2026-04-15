# Agents Workflow

This repository defines a layered instruction system for agentic workflow.

The goal is to keep the startup context small, route the agent to only the docs it actually needs, and separate
reusable guidance from repository-specific documentation.

I know there are already very extensive repositories containing similar instructions and skill-sets, but I see this
project as an attempt to create a personalized dataset tailored to my daily workflow, which is primarily focused
on developing large, domain-oriented business applications.

Please treat this project as an experiment, not something I use daily in a production environment. It is a test of
this system's capabilities when working with an agent based on an imperative approach, in which each task is executed
under the operator's full control, with extensive domain knowledge that allows them to direct the agent like a junior
or mid-level developer, mainly for business applications with massive codebases, where I believe the key role of
experienced developers is maintaining the code, the architecture, and thinking ahead. I treat this project as a hobby
that I work on after hours, and through which I try to channel my passion for software development into an agent. It is
an attempt to understand, optimize, and implement this approach in my daily work. I don't know if this is the best
approach, but experimenting is the most fun.

I use this "skillset" to test my own personal projects, primarily with OpenAI's gpt-5.4 model and Codex. The technical
skills I've described here are fairly general in nature and are intended to provide an overview of the
architecture. I'll continue to develop them (primarily back-end - Java and Spring Boot) through further testing.

## Structure

`instructions/core/`
- reusable workflow rules and documentation-maintenance guidance

`instructions/guides/`
- task-type guidance for phases such as discovery, investigation, and code changes

`instructions/skills/`
- reusable technical skillsets
- loaded only when a repository routes to them through project docs

`instructions/project-template/`
- reusable templates for generating repository-specific docs under `instructions/project/`
- used during onboarding, not as active repo documentation

`instructions/project/`
- repository-specific documentation generated or maintained for a particular codebase
- this is the source of truth for local structure, stack, routing, and constraints

`instructions/domain/`
- reusable domain abstractions and domain-oriented templates

`instructions/shared-domain/`
- cross-repository business/domain knowledge when multiple systems share the same concepts

`instructions/work/`
- task records, plans, milestones, and checkpoints
- this is quite important because the main principle of these guidelines is full transparency and cooperation with
  the agent (as pair-programmer), rather than completely obscuring the code, which is intended to maintain control
  over the codebase. It is a changelog with checkpoints that allow the agent to summarize the current work and continue
  from a specific point, starting with a clean context
- by default, this directory is excluded from Git tracking, so it's best to remove this rule from the
  project's [.gitignore](.gitignore) file and keep the "worklog" alongside your codebase for further analysis

## Architecture Principles

- Keep bootstrap minimal.
- Keep reusable skills cold until project docs route to them.
- Keep reusable templates separate from instantiated project docs.
- Keep repository-specific facts out of the shared template layer.
- Let real work drive skill growth instead of prebuilding everything.

## Workflow Modes

Use explicit commands when you want deterministic routing and lower token usage.
Use the `wf:` prefix to keep repository workflow commands distinct from built-in slash commands.

- `wf:discuss`: default conversation mode; minimal loading, no task records
- `wf:plan`: tracked planning mode; create or update `instructions/work/`, no code edits
- `wf:implement`: tracked execution mode after approval
- `wf:review`: review mode routed through investigation guidance
- `wf:status`: summarize current mode, assumptions, and next step

Useful modifiers:

- `wf:light`: minimum viable instruction loading
- `wf:full`: load all clearly relevant docs for the active mode
- `wf:cold`: keep optional docs and skills unloaded unless needed
- `wf:track`: require `instructions/work/`
- `wf:no-track`: valid for discussion or review work only

Optional aliases:

- `wf:d` -> `wf:discuss`
- `wf:p` -> `wf:plan`
- `wf:i` -> `wf:implement`
- `wf:r` -> `wf:review`
- `wf:s` -> `wf:status`
- `wf:l` -> `wf:light`
- `wf:f` -> `wf:full`
- `wf:c` -> `wf:cold`
- `wf:t` -> `wf:track`
- `wf:nt` -> `wf:no-track`

Full `wf:` forms remain canonical in docs and defaults. Aliases are optional shorthand and may be mixed with full forms.

If no mode command is given, the default is `wf:discuss wf:light wf:cold wf:no-track`.

## How To Extend It

Add a new skill when a reusable technical pattern appears across repositories.

- Put reusable, repository-agnostic guidance in `instructions/skills/`.
- Start with a small `index.md` router and only a few narrow child files.
- Expand the skill later through real tasks, not speculative completeness.

Add new project-doc generation support when onboarding needs it.

- Put reusable file patterns in `instructions/project-template/`.
- Generate actual repo docs into `instructions/project/`.
- After generation, treat `instructions/project/` as the active source and keep templates cold.

Add repository-specific documentation when a real codebase is being onboarded or maintained.

- Keep local structure, stack, commands, and constraints in `instructions/project/`.
- Use project docs to attach the relevant reusable skills.

When adding a new backend or frontend stack family:

- Add reusable technical guidance under `instructions/skills/` only when the pattern is expected to
  repeat across repositories.
- Keep the stack entry point small with an `index.md` router and only the child files that current tasks justify.
- Update `instructions/project-template/` only when onboarding or project-doc generation needs a reusable
  source pattern for that stack.
- Keep stack-specific routing attached through `instructions/project/` so repositories opt in explicitly instead of
  loading the stack by default.
- Follow the existing separation of concerns: reusable workflow in `instructions/core/` and `instructions/guides/`,
  reusable technical guidance in `instructions/skills/`, and repository facts in `instructions/project/`.

## Token Guardrails

- Keep bootstrap files, routing files, and skill entry points short, path-first, and easy to rebuild from deeper docs.
- Put detailed examples, edge cases, and optional guidance in cold child files instead of hot-loaded routers.
- Load only one relevant guide for the current phase of work unless the active task clearly requires another.
- Prefer explicit mode commands over intent inference when you want deterministic loading behavior.
- Prefer module docs and project-local routing over broad repository-wide skill loading in mixed-architecture codebases.
- Expand reusable skills and templates through accepted tasks, not speculative completeness.

Detailed rules live in the instruction files themselves. This README is only the high-level map.

For workflow calibration examples, see [instructions/core/workflow-mode-matrix.md](instructions/core/workflow-mode-matrix.md).

If you think it would be worthwhile to develop skills related to domain design in business applications, I encourage
you to submit suggestions for changes and improvements. I try to keep an open mind toward all feedback.

## License

This project is licensed under the Apache-2.0 License.

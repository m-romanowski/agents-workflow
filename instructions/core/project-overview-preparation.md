# Project Overview Preparation

- Treat this file as the reusable standard for preparing or maintaining project overview documentation.
- Use existing repository documentation first. Do not regenerate or replace it unless the operator asks or the current documentation is clearly insufficient.
- The overview exists to help the agent and operator navigate the codebase, understand architecture and extension points, identify constraints, and support future planning.
- Keep this file generic. Project-specific findings belong in `instructions/project/` or `instructions/work/`, not in the reusable template layer.

## Modes

### Existing-project mode
- If `instructions/project/`, `instructions/domain/`, or `instructions/shared-domain/` already contain useful documentation, use those files as the primary source for navigation and planning.
- Extend or correct existing documentation incrementally.
- If the documentation and the codebase appear to disagree, surface the mismatch and ask the operator before making broad documentation changes.
- If the repository participates in a cross-repository business domain, confirm whether the canonical knowledge belongs in `instructions/shared-domain/`.

### New-project onboarding mode
- Prepare an initial overview only when the operator explicitly asks for it, or when the repository has no sufficient project documentation.
- In onboarding mode, create the project overview in a structured, reviewable way rather than relying on ad hoc notes.
- In onboarding mode, use `instructions/project-template/` as the reusable source pattern for generating repository-specific files under `instructions/project/`.
- In onboarding mode, keep the first generated documentation cut minimal and expand only when the repository evidence justifies it.

## Preparation Sequence
1. Inspect repository structure.
2. Identify entry points and runtime surfaces.
3. Identify tooling, commands, and package-manager behavior.
4. Identify architectural boundaries and extension points.
5. Identify generated, deployment-only, or fragile areas.
6. Identify domain hints conservatively.
7. Mark uncertainties and open questions.
8. Prepare or update the relevant project and domain documentation files.
9. Review the overview with the operator.

## Optional Follow-Up: Cross-Cutting Signals

- After the minimum onboarding cut is generated, the agent may propose a compact follow-up pass for cross-cutting technical signals when repository evidence suggests it would materially help future planning.
- This optional step must not expand the default onboarding cut automatically.
- Use this follow-up only when multiple modules or services, message/event types, clients, integration fixtures, or architecture diagrams indicate meaningful coordination boundaries.
- Keep the output small and review-oriented.
- Separate:
  - verified observations from code, config, tests, or diagrams
  - likely interpretations that still need confirmation
  - open questions for the operator
- Ask the operator whether the observations are correct and worth promoting into `instructions/project/` before generating or extending project documentation with those findings.
- Do not present inferred business flows or cross-service semantics as authoritative unless they are verified from approved evidence sources or confirmed by the operator.

## Approved Evidence Sources
- directory structure
- package manifests and lockfiles
- config files
- README files
- entry points
- scripts
- operator-provided context

Do not treat naming guesses or unsupported domain assumptions as authoritative.

## Required Outputs
- `instructions/project/index.md`
- `instructions/project/skill-profile.md`
- `instructions/project/personal-skill-policy.md` only when the repository needs documented optional personal-skill behavior
- `instructions/project/recommended-third-party-skills.md` only when the repository chooses to maintain a public optional recommendation index
- `instructions/project/repo-map.md`
- `instructions/project/stack-and-commands.md`
- `instructions/project/modules/<module>.md` when mixed architecture, module-specific overrides, or migration zones justify it
- `instructions/project/frontend.md` when applicable
- `instructions/project/backend.md` when applicable
- `instructions/project/testing.md` when applicable

Prepare or extend files in `instructions/domain/` only when reusable domain abstractions or template-style domain structures need to change.
Prepare or extend shared-domain files when the task affects knowledge intended to be reused across multiple repositories or services.
Use `instructions/project-template/` only as a reusable source for generating repo-specific files; do not treat it as active repository documentation.

## Documentation Rules
- Focus on architecture, boundaries, navigation, extension points, and constraints.
- Keep project documentation technical and domain documentation business-oriented.
- Include a lightweight routing file such as `instructions/project/index.md` that tells the agent which repository-local docs to load for common task types.
- Include `instructions/project/skill-profile.md` so the repository can declare which reusable skills are active and when they should be attached.
- When the repository supports optional personal third-party skills, document that behavior in a separate cold file such as `instructions/project/personal-skill-policy.md`.
- When the repository wants to share optional third-party recommendations, use a separate informational file such as `instructions/project/recommended-third-party-skills.md`.
- Use `instructions/project-template/index.md` and `instructions/project-template/skill-profile.md` as reusable starting patterns when generating those files for a new repository.
- Use `instructions/project-template/personal-skill-policy.md` and `instructions/project-template/recommended-third-party-skills.md` when those optional project files are needed.
- Use `instructions/project-template/module.md` as the reusable starting pattern when generating `instructions/project/modules/<module>.md`.
- Use the other files in `instructions/project-template/` as the reusable starting patterns for the rest of the generated project documentation.
- Keep the routing file short, path-first, and rebuildable from the rest of the project documentation.
- Treat reusable skills as cold-loaded extensions attached through project documentation rather than as default startup context.
- In new-project onboarding mode, generate only the skill attachments that are verified from the repository stack and architecture.
- Keep skill attachment conservative; if the stack is unclear, record the uncertainty instead of routing to a speculative skill.
- In mixed-architecture repositories, generate module docs for the affected areas and use those module docs before choosing architecture-specific skills.
- After generating repo-specific files from `instructions/project-template/`, stop using the template files as the active source and continue through the instantiated files in `instructions/project/`.
- Do not use the routing file to duplicate detailed architecture or domain content that belongs in the other project or domain docs.
- Separate observations, proposals, and accepted decisions when preparing planning material.
- Mark uncertainty explicitly instead of guessing.
- Do not move repository-specific discoveries into `instructions/core/` or `instructions/guides/` unless the workflow itself needs a reusable improvement.
- Do not duplicate cross-repository business knowledge into multiple repo-local files when a shared-domain location is intended.

## Minimum Onboarding Cut

For a new repository, generate the smallest project-doc set that still allows safe navigation and cold-load routing.

Default minimum cut:

- `instructions/project/index.md`
- `instructions/project/skill-profile.md`
- `instructions/project/repo-map.md`
- `instructions/project/stack-and-commands.md`

Add only when evidence justifies it:

- `instructions/project/personal-skill-policy.md`
- `instructions/project/recommended-third-party-skills.md`
- `instructions/project/modules/<module>.md`
- `instructions/project/backend.md`
- `instructions/project/frontend.md`
- `instructions/project/testing.md`

After the minimum cut is generated:

- use the new `instructions/project/` files as the active repository source
- load only the project files needed for the current task
- keep unused project-template files cold
- if cross-cutting technical signals appear important, propose the optional follow-up pass instead of expanding the minimum cut by default

## Acceptance Criteria
The overview is complete enough when the agent can answer, without guessing:
- what are the main parts of the repository
- how it is run, built, and validated
- where likely changes belong
- what architectural constraints matter
- what domain areas are known
- what still requires operator clarification

## Update Responsibility
- After each accepted task, assess whether `instructions/project/` or `instructions/domain/` should be updated.
- Update `instructions/project/` when accepted work changes structure, tooling, commands, boundaries, generated outputs, or architectural assumptions.
- Update `instructions/project/` when accepted work adds or changes repo-specific domain context needed for local planning and navigation.
- Update `instructions/domain/` only when accepted work changes reusable domain abstractions or template-style domain structures.
- Documentation should be updated before the task is considered current.

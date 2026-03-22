# Domain Documentation

- Treat `instructions/domain/` as the abstraction layer for reusable domain documentation and templates.
- Treat `instructions/shared-domain/` as the canonical place for domain knowledge intended to be shared across multiple repositories or services.
- Use `instructions/domain/` to describe reusable domain terminology structures, bounded-context templates, workflow templates, constraints templates, and other abstract domain scaffolding that can be reused across repositories.
- Domain interpretation is more sensitive than technical structure. Be conservative and prefer operator confirmation when domain meaning is unclear.
- Do not silently infer business intent from code structure alone.
- If a domain mapping is inferred from implementation and not confirmed by the operator, mark it explicitly as an inference.
- The operator request is a valid source for identifying which domain context should be loaded at the start of the task.
- For new or hypothetical features, the agent may introduce proposed bounded contexts or domain areas during planning when they help structure the discussion.
- Focus on durable domain knowledge that helps people understand the system and navigate it correctly.
- Do not record every bug fix, local adjustment, or implementation detail unless it changes the domain understanding or the mapping between domain and code.

## Suggested Content
- `instructions/shared-domain/<domain>/`
  - `glossary.md`: canonical business terms reused across repositories
  - `workflows.md`: shared business flows and state transitions
  - `constraints.md`: shared invariants, compliance concerns, and business rules
  - `integrations.md`: service boundaries, handoffs, and cross-system interaction rules
- `glossary.md`: reusable domain-term template or abstraction guidance
- `business-areas.md`: reusable bounded-context template or abstraction guidance
- `workflows.md`: reusable workflow-template guidance
- `codebase-mapping.md`: reusable mapping template when such mapping is needed
- `constraints.md`: reusable domain-constraint template or abstraction guidance

## Documentation Rules
- Keep domain descriptions focused on durable concepts, not transient implementation details.
- Separate confirmed facts from assumptions or open questions.
- Distinguish clearly between current-state observations, future-state proposals, and operator-accepted decisions.
- Use the operator's terminology as the canonical source when available.
- Prefer explicit mappings between business language and code terms when defining reusable structures.
- Keep shared-domain documentation canonical and cross-repository.
- Keep repo-specific domain documentation in `instructions/project/`.
- Keep `instructions/project/` focused on how this repository participates in or maps to a shared or abstract domain.
- When the operator may hold important domain knowledge that is not documented yet, ask explicitly for business rules, constraints, terminology, prior decisions, or missing context if that information would materially affect the recommendation.
- Do not replace generic `instructions/domain/` content with repository-specific domain details.
- If repository-specific domain findings are needed, place them in `instructions/project/` or keep them in the active task files until the operator approves a permanent location.
- Treat documentation confidence as a milestone-level review concern, tracked through operator review and task checkpoints rather than per-file status labels.
- During planning or implementation, the agent may draft or revise domain documentation based on current understanding.
- When a milestone is reviewed, the operator acceptance of that milestone also determines whether the related domain documentation updates are accepted for current use.
- If later work changes or invalidates existing domain understanding, revise the affected domain documents in the next milestone and record that update in the next checkpoint.

## Update Rules
- Update `instructions/shared-domain/` when accepted work changes cross-repository terminology, workflows, constraints, or integration rules intended to be reused by multiple systems.
- Update `instructions/domain/` whenever accepted work changes reusable domain abstractions, template structures, or generic domain guidance intended for reuse.
- After each accepted step, assess whether domain documentation changed. If unsure, ask the operator before proceeding.
- When introducing a proposed new bounded context during planning, document at least the proposed context name, rationale, responsibilities, key terms, likely codebase impact, and open domain questions.

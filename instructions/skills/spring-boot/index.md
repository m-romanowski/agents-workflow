# Spring Boot

## Purpose

- reusable guidance for Spring Boot framework structure, bean wiring, runtime boundaries, and framework-specific review

## When To Load

- the task touches Spring-managed application code, bean wiring, configuration, HTTP entry points, lifecycle/runtime boundaries, or framework-specific review concerns

## Do Not Load By Default

- `structure.md` only when structure or wiring concerns matter
- `review.md` only when the task is a code review or review-style investigation

## Child Files

- `structure.md`: framework-facing boundaries, bean wiring, configuration responsibilities, and runtime structure
- `review.md`: Spring Boot-specific review cues and common framework misuse patterns

## Related Skills

- load `instructions/skills/modular-hexagonal/` when the task is primarily about module boundaries, dependency direction, or package-level architecture
- load `instructions/skills/backend-testing/` when the task is primarily about test strategy, test scope selection, or review of backend tests

## Expected Project Overrides

- `instructions/project/index.md`
- `instructions/project/skill-profile.md`
- `instructions/project/modules/<module>.md` when local structure differs

## Loading Examples

- controller or service change: load `structure.md`
- Spring Boot code review: load `review.md`
- module-boundary refactor in a Spring app: also load `instructions/skills/modular-hexagonal/`
- Spring test-scope review: also load `instructions/skills/backend-testing/`

# Spring Boot Review

## Scope

- code review cues specific to Spring Boot code, configuration touchpoints, and framework-scoped tests

## Review Focus

- framework usage fits the intended local architecture
- controller, service, configuration, and adapter responsibilities remain clear
- bean wiring, lifecycle, and runtime behavior stay understandable
- transactional boundaries are understandable and intentional
- tests do not depend on unnecessary Spring scope

## Common Findings To Look For

- business logic embedded in controllers or configuration classes
- excessive reliance on framework defaults that obscure behavior
- framework annotations used in the wrong architectural layer
- ambiguous bean wiring or lifecycle behavior
- heavyweight Spring test setup for narrow behavior

## Escalate To Related Skills When

- the finding is mainly about module boundaries, cohesion, coupling, or dependency leaks
  - load `instructions/skills/modular-hexagonal/review.md`
- the finding is mainly about behaviour-first test strategy, test brittleness, or test-scope selection
  - load `instructions/skills/backend-testing/review.md`

## Escalate To Project Docs When

- repository-specific structure rules may override generic Spring Boot guidance
- the touched area is known to differ from the repository default

## Project Override Note

- repository and module docs win when they define stricter local review expectations

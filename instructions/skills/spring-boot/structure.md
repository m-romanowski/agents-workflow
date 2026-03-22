# Spring Boot Structure

## Scope

- structure and framework integration boundaries in Spring Boot application code

## Preferred Patterns

- keep transport concerns in controllers and adapters and keep business logic out of framework-heavy entry points
- keep framework configuration and bean wiring separate from business services where practical
- make important runtime, lifecycle, transaction, and wiring boundaries understandable
- keep framework annotations near the boundaries that need them when practical

## Risk Areas

- controllers accumulating orchestration or business logic
- configuration classes taking on unrelated responsibilities
- framework annotations leaking into code that should stay less coupled to Spring
- unclear bean wiring, lifecycle, or transactional boundaries
- framework structure guidance being used as a substitute for module architecture decisions

## Review Cues

- check whether responsibilities are split cleanly across controllers, services, configuration, and adapters
- check whether bean wiring and runtime boundaries remain understandable
- check whether framework usage supports the intended architecture instead of distorting it

## Escalate To Related Skills When

- the main concern is package-level module boundaries, dependency direction, or API shape
  - load `instructions/skills/modular-hexagonal/`
- the main concern is test strategy, test scope, or test-suite design
  - load `instructions/skills/backend-testing/`

## Project Override Note

- if project or module docs define stricter local structure rules, follow those docs

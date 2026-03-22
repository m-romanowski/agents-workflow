# Modular Hexagonal

## Purpose

- reusable guidance for modular backend architecture built around cohesive package-level modules and explicit module APIs

## When To Load

- the task touches backend module boundaries, dependency direction, module APIs, architecture-fit refactoring, or architecture-specific review concerns

## Do Not Load By Default

- `structure.md` only when module structure, dependency flow, or framework-placement concerns matter
- `review.md` only when the task is a code review or review-style investigation

## Child Files

- `structure.md`: module boundaries, API shape, dependency direction, and framework containment
- `review.md`: review cues for cohesion, coupling, dependency leaks, and boundary violations

## Expected Project Overrides

- `instructions/project/index.md`
- `instructions/project/skill-profile.md`
- `instructions/project/modules/<module>.md` when local architecture rules differ

## Loading Examples

- backend module refactor: load `structure.md`
- architecture-focused backend review: load `review.md`

# Backend Testing

## Purpose

- reusable guidance for backend test strategy, test-scope selection, and test-focused review

## When To Load

- the task touches backend test design, test selection, test writing, test refactoring, or backend test review concerns

## Do Not Load By Default

- `strategy.md` only when test scope, behaviour focus, or integration-vs-unit concerns matter
- `review.md` only when the task is a code review or review-style investigation

## Child Files

- `strategy.md`: behaviour-first testing model, test-scope selection, and common test anti-patterns
- `review.md`: testing-specific review cues for brittleness, excessive scope, and weak behavioural coverage

## Optional References

- add framework-specific references only when a concrete task needs syntax-level examples

## Expected Project Overrides

- `instructions/project/index.md`
- `instructions/project/skill-profile.md`
- `instructions/project/testing.md` when local testing rules differ
- `instructions/project/modules/<module>.md` when module-level test expectations differ

## Loading Examples

- writing backend tests for a new module behaviour: load `strategy.md`
- reviewing a slow or brittle backend test suite: load `review.md`

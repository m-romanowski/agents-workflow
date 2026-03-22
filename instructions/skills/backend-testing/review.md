# Backend Testing Review

## Scope

- code review cues for backend tests and for production changes that affect backend testing quality

## Review Focus

- tests describe behaviour clearly
- chosen test scope matches the risk being verified
- suites stay fast where fast tests are sufficient
- integration tests cover meaningful external boundaries
- tests resist internal refactoring without losing signal

## Common Findings To Look For

- tests asserting internal calls, private structure, or incidental sequencing
- slow integration-style tests used where a fast behaviour test would suffice
- integration tests that do not verify a real external or framework boundary
- missing integration coverage at boundaries where mocks would hide critical behaviour
- test names that do not describe business, module, or API behaviour
- test setup that obscures the behaviour being verified

## Escalate To Project Docs When

- the repository intentionally uses different test-layer terminology or scope rules
- local conventions define specific expectations for integration, acceptance, or module-level tests
- module docs define approved exceptions to the default testing approach

## Project Override Note

- repository and module docs win when they define stricter local testing or review expectations

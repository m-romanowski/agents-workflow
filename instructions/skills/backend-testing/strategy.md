# Backend Testing Strategy

## Scope

- strategy guidance for backend tests that prioritize behaviour, speed, and refactoring resilience

## Preferred Patterns

- test behaviour at the module or API boundary rather than class internals by default
- use fast non-IO tests as the primary confidence layer whenever behaviour can be verified without external systems
- prefer constructing the module through its public composition entry, such as a module configuration or test factory that mirrors production wiring
- prefer simple in-memory test implementations for internal collaborators when they keep the test clear and stable
- use mocks mainly for assumptions about module-to-module collaboration or real external boundaries
- add integration tests selectively for real boundaries such as persistence, transport, serialization, or framework wiring
- keep integration tests black-box by default and touch repositories directly only when the repository itself is the boundary under test
- prefer real integration surfaces in integration and acceptance tests, and keep mocks there as rare exceptions
- prefer realistic simulation tools such as WireMock, MockWebServer, or Testcontainers when a real dependency is outside the test scope but its protocol or runtime behaviour still matters
- prefer seeding integration-test state through a real public API or real fixture path instead of mocking a collaborator that belongs inside the integrated slice
- when testing integration between modules in a modular monolith, do not reach into another module's encapsulated non-API classes
- if another module needs simplified state setup for integration tests, prefer a module-provided test fixture that seeds state without exposing internal implementation details
- choose the lightest test scope that proves the required behaviour
- name tests so they describe expected behaviour or requirements
- keep tests stable across internal refactoring as long as externally visible behaviour does not change

## Testing Intent

- keep most tests runnable in milliseconds
- avoid coupling the suite to incidental implementation details
- use tests as executable requirements and living documentation
- preserve confidence without paying unnecessary framework or IO cost
- keep internal service wiring refactorable by treating the module facade and public composition entry as the stable test surface

## Risk Areas

- defaulting to one test per class or per method
- exposing module internals only to make mocking easier
- asserting internal interactions instead of meaningful behavioural outcomes
- using framework-heavy or IO-heavy tests for narrow logic
- broad integration suites that duplicate lower-level coverage
- test names and setup that describe mechanics instead of behaviour

## Scope Selection Cues

- prefer a fast unit-style test when behaviour can be driven through a module API without real IO
- prefer module configuration or a public test composition helper over direct construction of internal services
- prefer an in-memory collaborator over a mock when the collaborator is internal to the module and the behaviour matters more than the interaction
- prefer a mock when the test is checking assumptions about communication with another module or an external dependency
- prefer an integration test when the behaviour depends on a real boundary that mocks would hide
- prefer a black-box integration test over repository inspection when the behaviour is observable through a public API
- prefer WireMock or MockWebServer for HTTP integrations and Testcontainers for infrastructure dependencies when realistic simulation improves confidence
- if a dependency belongs to the integrated slice, seed it through the real application path rather than mocking it
- for modular-monolith integration tests, interact with other modules through their facade/API or through an agreed test fixture owned by that module
- avoid overlapping scopes unless each layer proves something different and necessary

## Example Patterns

- module behaviour first
  drive the test through the module facade or public API instead of calling internal services directly
- in-memory before mocking internals
  use a simple in-memory collaborator when it keeps the test behaviour-focused and avoids interaction-heavy assertions
- mock real boundaries
  use mocks mainly for external systems or explicit module-to-module assumptions, not as the default for every dependency
- integration only for real boundary value
  step up to integration tests when persistence, transport, serialization, framework wiring, or runtime behaviour is part of what must be proven

## Project Override Note

- if project or module docs define stricter testing conventions, follow those docs

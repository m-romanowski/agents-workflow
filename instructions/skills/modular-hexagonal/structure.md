# Modular Hexagonal Structure

## Scope

- structure guidance for backend code organized as cohesive package-level modules with explicit APIs and contained framework adapters

## Preferred Patterns

- treat a package-level business module as the main unit of cohesion
- expose a narrow module API and route collaboration through that API instead of internal classes
- keep module composition behind a public configuration or equivalent composition entry that can create the facade without exposing internal services
- keep module internals hidden unless broader visibility is required by the language or framework
- keep dependency direction explicit and make cross-module calls depend on public module APIs
- keep transport, persistence, and framework-heavy adapters outside core business logic where practical
- keep wiring and composition understandable through explicit configuration boundaries

## Architectural Intent

- favor high cohesion inside each module and low coupling between modules
- optimize for behaviour-oriented testing at the module API level rather than test-per-class internals
- make refactoring inside a module possible without forcing broad test rewrites
- keep framework usage supportive of the architecture instead of shaping the business model around framework defaults

## Risk Areas

- modules exposing internal classes as informal public APIs
- cross-module shortcuts that bypass the intended module API
- framework annotations or persistence concerns leaking into code that should stay closer to the domain
- configuration, controller, or adapter layers accumulating business rules
- package structure that looks modular but still couples modules through shared internals

## Review Cues

- check whether each module has a clear public entry point
- check whether module construction can happen through a public composition entry without exposing internal services
- check whether new dependencies preserve the intended direction between modules
- check whether framework-facing code stays at the boundary instead of taking over business behaviour
- check whether the structure supports fast behaviour-first tests without depending on IO-heavy setup

## Example Patterns

- public module entrypoint
  use a small facade or equivalent module API as the stable entry for other modules and adapters
- hidden composition
  keep service assembly behind module configuration or a composition entry instead of exposing internal wiring details
- boundary adapter usage
  let controllers, consumers, and other adapters call the module API rather than internal services or repositories
- avoid internal leakage
  do not make classes public only to support cross-module shortcuts, framework convenience, or narrow tests

## Project Override Note

- if project or module docs define stricter local architecture rules, follow those docs

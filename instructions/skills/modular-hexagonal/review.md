# Modular Hexagonal Review

## Scope

- code review cues for modular backend architecture based on cohesive package-level modules and explicit module APIs

## Review Focus

- module cohesion remains high
- inter-module coupling stays low and intentional
- collaboration flows through module APIs rather than internal classes
- framework and infrastructure concerns stay contained at boundaries
- test seams stay aligned with behaviour rather than implementation details

## Common Findings To Look For

- internals exposed without a clear architectural reason
- new dependencies that bypass a module's intended API
- controller, configuration, or adapter code taking on business logic
- persistence or framework concerns leaking into the core module contract
- tests coupled to internal classes or incidental structure instead of module behaviour
- package names or boundaries that no longer match actual responsibilities

## Escalate To Project Docs When

- the repository intentionally uses a different module boundary pattern
- a local module has explicit exceptions to the default dependency rules
- project docs define stricter visibility, layering, or testing expectations

## Project Override Note

- repository and module docs win when they define stricter local architecture or review expectations

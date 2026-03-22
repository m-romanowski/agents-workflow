# Module Template

## Purpose

- template for documenting a repository-local module under `instructions/project/modules/<module>.md`
- intended for modules or areas with local architectural, routing, or testing differences

## Template Rules

- describe only verified facts about the module or area
- keep the file short, path-first, and boundary-focused
- record the module's public API and important local constraints
- use this file to state local routing overrides when the repository mixes different architectures or testing conventions
- do not duplicate reusable skill guidance here; point to the relevant skills through local routing notes

## Suggested Sections

- purpose
- public API or entry points
- local architecture pattern
- routing overrides
- local testing notes
- constraints and exceptions

## Minimum Content Expectation

- enough information for the agent to decide:
  - whether this module follows the repository default
  - which local architecture or testing rules override repository defaults
  - which reusable skills are relevant for work in this module

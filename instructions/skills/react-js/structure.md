# React JS Structure

## Scope

- component structure, composition, and UI-facing boundaries in React application code

## Preferred Patterns

- keep components focused on one UI responsibility where practical
- separate rendering concerns from heavier orchestration or data-loading logic when that improves clarity
- keep state close to where it is needed without spreading ownership ambiguously
- make component boundaries and data flow understandable from local code structure

## Risk Areas

- oversized components mixing rendering, orchestration, and side effects
- unclear ownership of state or derived UI behavior
- hooks used in ways that obscure lifecycle or dependency behavior
- component hierarchies that make data flow difficult to reason about

## Review Cues

- check whether components have clear responsibilities and understandable boundaries
- check whether state and side effects are placed in a way that supports maintainability
- check whether composition helps rather than hides complexity

## Project Override Note

- if project or module docs define stricter local frontend structure rules, follow those docs

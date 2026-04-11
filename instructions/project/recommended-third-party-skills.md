# Recommended Third-Party Skills

## Purpose

- provide an informational index of optional third-party skills that may help users of this workflow
- keep recommendations separate from personal installed-skill state

## Usage Rules

- treat this file as informational only
- do not assume any listed skill is installed
- do not load or use a listed skill unless the operator explicitly requests it and the active agent environment supports it
- recommendations in this file are optional, not required
- use `instructions/project/personal-skill-policy.md` for activation rules, precedence, and storage model

## Recommended Skills

### `caveman`

- purpose: terse response style and explicit mode-based persona for low-friction sessions
- source: `https://github.com/JuliusBrussee/caveman`
- supported agents: Codex when installed in the operator environment; other agent environments only when separately supported there
- install model: external personal-skill installation, not vendored into this repository
- caveats:
  - should remain explicit and session-scoped
  - must not override repository workflow, safety, or documentation rules
  - recommendation does not imply installation or default availability

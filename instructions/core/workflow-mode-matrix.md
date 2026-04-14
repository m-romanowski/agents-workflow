# Workflow Mode Matrix

Use this file as a calibration reference for expected behavior across workflow modes.

Keep it cold during normal work. Load it when refining workflow rules, reviewing agent behavior, or diagnosing mode-selection mistakes.

## Format

For each scenario, define:

- operator input
- expected mode
- expected docs loaded
- expected forbidden actions
- expected response shape

## Scenarios

### 1. Default discussion

- Operator input: `Should we split project docs by bounded context?`
- Expected mode: `/discuss /light /cold /no-track`
- Expected docs loaded:
  - `instructions/core/session-contract.md`
  - minimum routing docs only if needed
- Expected forbidden actions:
  - do not create `instructions/work/`
  - do not edit the codebase
  - do not run validation unless explicitly requested
- Expected response shape:
  - conversational analysis
  - tradeoffs and recommendation
  - open questions only if needed

### 2. Explicit discussion

- Operator input: `/discuss should we move domain docs under project/ or shared-domain/`
- Expected mode: `/discuss`
- Expected docs loaded:
  - `instructions/core/session-contract.md`
  - one minimal discussion-relevant guide only if needed
  - only the touched routing docs
- Expected forbidden actions:
  - do not create tracked artifacts
  - do not edit files
- Expected response shape:
  - concise reasoning
  - direct recommendation

### 3. Review mode

- Operator input: `/review check whether this instruction stack has contradictions`
- Expected mode: `/review`
- Expected docs loaded:
  - `instructions/core/session-contract.md`
  - `instructions/guides/investigation.md`
  - only the files needed to support findings
- Expected forbidden actions:
  - do not edit files unless explicitly requested
  - do not create `instructions/work/` by default
- Expected response shape:
  - findings first
  - file references
  - residual risks or gaps

### 4. Planned tracked work

- Operator input: `/plan add a reusable Java backend skill router`
- Expected mode: `/plan /track`
- Expected docs loaded:
  - `instructions/core/session-contract.md`
  - relevant planning or discovery guide
  - project routing docs needed for the touched area
  - the active task `TODO.md` front matter after tracked planning starts
  - the active task `TODO.md` body only when plan details are needed
- Expected forbidden actions:
  - do not edit the main codebase
  - do not run implementation validation
- Expected response shape:
  - proposed plan
  - tracked task setup
  - approval checkpoint before implementation

### 5. Approved implementation

- Operator input: `/implement approved step 1 for the active task`
- Expected mode: `/implement /track`
- Expected docs loaded:
  - `instructions/core/session-contract.md`
  - relevant implementation guide
  - the active task `TODO.md` front matter
  - the active task `TODO.md` body only when step details are needed
  - only the project or skill docs needed for the touched area
- Expected forbidden actions:
  - do not skip approved task records
  - do not expand scope without approval
- Expected response shape:
  - short implementation update
  - code or doc changes
  - validation status

### 6. Feature exploration without tracking

- Operator input: `/discuss what is the best way to route stack-specific skills in a mixed monorepo?`
- Expected mode: `/discuss /light /cold /no-track`
- Expected docs loaded:
  - `instructions/core/session-contract.md`
  - `instructions/guides/feature-discovery.md` only if option-shaping is needed
- Expected forbidden actions:
  - do not create `instructions/work/`
  - do not load extra guides unless clearly needed
- Expected response shape:
  - options with tradeoffs
  - recommendation
  - no durable artifact creation

### 7. Investigation with optional discovery

- Operator input: `/review inspect whether the current onboarding flow causes unnecessary hot-loading`
- Expected mode: `/review`
- Expected docs loaded:
  - `instructions/core/session-contract.md`
  - `instructions/guides/investigation.md`
  - `instructions/guides/feature-discovery.md` only if the operator wants redesign options after findings
- Expected forbidden actions:
  - do not switch into planning automatically
  - do not edit docs unless asked
- Expected response shape:
  - findings
  - evidence
  - optional next-step choices

### 8. Bootstrap-only session start

- Operator input: `Follow BOOTSTRAP.md as the session bootstrap.`
- Expected mode: implicit `/discuss /light /cold /no-track`
- Expected docs loaded:
  - `AGENTS.md`
  - `instructions/core/session-contract.md`
  - `instructions/project/index.md` when it exists
- Expected forbidden actions:
  - do not load guides before task context exists
  - do not inspect `instructions/work/` unless continuing tracked work in `/plan` or `/implement`
- Expected response shape:
  - acknowledge minimal bootstrap
  - wait for the actual task

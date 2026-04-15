# Feature Discovery

Use this guide for hypothetical or future features that do not yet exist in the codebase, especially when the operator is exploring possible solutions.

## Role
- Act as a technical partner during discovery.
- Help identify the best-fit solution within the current application architecture and constraints.
- Do not assume the operator is a novice. Stay concise and direct unless the operator asks for more explanation.
- Ask explicitly for missing business requirements, domain knowledge, constraints, prior decisions, or documentation when that context would materially affect the recommendation.
- Separate informal discussion from tracked discovery unless the operator explicitly asks to record the work.

## Goals
- Understand the feature goal and business context.
- Identify architectural constraints and extension points in the current codebase.
- Present viable implementation approaches with tradeoffs.
- Recommend a direction that fits the current application and expected future evolution.
- Surface open questions that must be resolved before implementation.

## Expected Outputs
- problem statement
- current architectural context
- relevant domain context
- assumptions and uncertainties
- options with tradeoffs
- recommended direction
- explicit separation between observations, proposals, and accepted decisions
- open questions for the operator
- possible next milestones if implementation is later approved

## Discovery Modes

### Informal discovery

Use this when the operator wants to think through options without creating durable workflow artifacts.

- Default to `wf:discuss wf:light wf:cold wf:no-track`
- Keep outputs conversational and decision-oriented
- Do not create `instructions/work/`

### Tracked discovery

Use this when the operator wants durable planning artifacts for later implementation.

- Switch to `wf:plan wf:track`
- Create or update the active task directory in `instructions/work/`
- Record assumptions, options, and decisions in a reviewable form

## Recommendation Format
- recommended option
- why this option fits the current architecture
- main tradeoffs and risks
- assumptions behind the recommendation
- blockers or missing inputs
- next milestone if the operator wants to continue

## Task Structure
- Use this structure for tracked discovery only.
- Create or update the active task directory in `instructions/work/`.
- Use `README.md` for the feature summary, goals, assumptions, options, and recommendation.
- Use `TODO.md` for discovery and decision steps until implementation is approved.
- Use milestone files to separate discovery phases such as context gathering, option analysis, and architecture decision.
- Use checkpoints to record decisions, learned constraints, and remaining open questions.
- Make it explicit in the task files which statements describe the current system, which describe proposed future solutions, and which have already been accepted by the operator.

## Architecture Fit
- Evaluate each option against the current frontend structure, backend role, deployment model, content model, operational complexity, and expected maintainability.
- Prefer solutions that fit the existing architecture unless there is a clear reason to recommend a larger change.
- If a larger architectural shift is worth considering, state why and make the tradeoff explicit.
- If the recommendation depends on missing business requirements or operator domain knowledge, ask for that clarification before finalizing the recommendation.
- If key uncertainties remain after reasonable clarification attempts, make the best recommendation you can with explicit assumptions and clearly marked open questions.

## Handoff To Implementation
- Do not treat discovery output as implementation approval.
- Once the operator accepts a direction and wants to proceed, load the relevant implementation guides and revise the task files so they become implementation-oriented.

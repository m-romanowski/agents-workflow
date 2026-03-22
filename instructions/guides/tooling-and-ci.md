# Tooling And CI

Use this guide for build config, linting, scripts, automation, CI/CD, developer tooling, and repository workflow changes.

## Additional Expectations
- Call out workflow impact before implementation.
- Be explicit about environment assumptions, generated files, cache behavior, and pipeline side effects.
- Treat tooling changes as potentially cross-cutting even when the code diff is small.
- Prefer narrow, reversible steps with clear validation points.

## Execution Pattern
1. Document the intended tooling change in the active task directory.
2. Ask the operator to review the impact and approve the plan.
3. Apply one approved step.
4. Report the effect on local development, CI, or deployment behavior.
5. Update checkpoints and ask whether to commit.

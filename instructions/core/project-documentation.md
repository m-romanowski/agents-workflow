# Project Documentation

- Treat `instructions/project/` as technical repository documentation.
- Use it to describe structure, architecture, technical boundaries, generated outputs, and repository-specific navigation.
- Do not use `instructions/project/` to explain business logic or product intent.
- Prefer verified facts from manifests, config files, entry points, directory structure, and observed tooling setup.
- If something is inferred rather than directly verified, label it clearly as an inference.
- If something is unknown, record the uncertainty instead of guessing.
- Focus on information that helps future readers understand how the codebase is organized and where responsibilities live.
- Do not document every minor implementation detail, local fix, or small internal change unless it materially affects navigation or architecture.
- When useful for future feature planning, capture durable architectural constraints and extension assumptions that influence solution design.

## Required Content
- `index.md`: lightweight routing map for repository-local documentation by task type
- `repo-map.md`: directory structure, ownership, and source-vs-generated boundaries
- `stack-and-commands.md`: verified stack and runnable commands
- `frontend.md`: frontend entry points, major architectural areas, and structural conventions when applicable
- `backend.md`: backend entry points, major architectural areas, and structural conventions when applicable
- `testing.md`: test setup, config locations, and validation commands when applicable
- Include architectural preferences or constraints when they materially affect feature planning, such as backend role, content strategy, deployment model, or runtime boundaries.

## Formatting Rules
- Prefer short sections and bullets over long prose.
- Write path-first documentation whenever possible.
- Keep structure stable and reusable across repositories.
- Keep `index.md` concise and focused on routing. It should tell the agent what to load, when to load it, and where detailed information lives.
- Document only what helps navigation, maintenance, safe modification, and architectural understanding.
- Keep repository-specific technical facts in `instructions/project/`. Do not push them into the shared template layer.

## Update Rules
- Update `instructions/project/` whenever accepted work changes repository structure, technical boundaries, commands, tooling, testing setup, generated outputs, or other technical navigation assumptions.
- Keep project documentation outside the code rather than adding explanatory comments to source files unless a local code comment is truly necessary.

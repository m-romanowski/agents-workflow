# Skill Profile Template

## Purpose

- template for declaring which reusable skills are active for a specific repository

## Template Rules

- include only skills verified from the repository stack and architecture
- keep this file short and path-first
- do not attach speculative skills
- use this file to help `instructions/project/index.md` decide which reusable skill files may be loaded
- when onboarding a repository with no project docs yet, generate `instructions/project/skill-profile.md` from this template as part of the minimum onboarding cut
- treat architecture skills as conditional attachments that may vary by module or backend area
- treat module docs as the deciding layer when a repository mixes multiple backend or frontend architectures

## Suggested Sections

- active skills
- default routing
- conditional notes

## Example Routing Pattern

### Active Skills

- `instructions/skills/spring-boot/`
- `instructions/skills/modular-hexagonal/` when a documented module or backend area uses that modular architecture pattern
- `instructions/skills/backend-testing/` when backend testing tasks benefit from the reusable testing strategy and review guidance

### Default Routing

- backend implementation touching Spring-managed application code:
  - load `instructions/skills/spring-boot/index.md`
  - then load only the needed child file
- backend implementation touching modular backend boundaries or module APIs:
  - load `instructions/skills/modular-hexagonal/index.md`
  - then load only the needed child file
- backend testing task or backend test-strategy task:
  - load `instructions/skills/backend-testing/index.md`
  - then load only the needed child file
- backend code review touching Spring-managed application code:
  - load `instructions/skills/spring-boot/index.md`
  - load `instructions/skills/spring-boot/review.md`
- backend code review focused on modular architecture concerns:
  - load `instructions/skills/modular-hexagonal/index.md`
  - load `instructions/skills/modular-hexagonal/review.md`
- backend code review focused on backend tests or test strategy:
  - load `instructions/skills/backend-testing/index.md`
  - load `instructions/skills/backend-testing/review.md`
- frontend implementation touching React application code:
  - load `instructions/skills/react-js/index.md`
  - then load only the needed child file
- frontend code review touching React application code:
  - load `instructions/skills/react-js/index.md`
  - load `instructions/skills/react-js/review.md`

### Conditional Notes

- do not attach Spring Boot skills to non-Spring areas unless repository docs explicitly route there
- do not attach modular architecture skills as a repository-wide default unless the project docs explicitly say that pattern applies broadly
- for mixed-architecture backends, load the relevant module doc first and let it drive architecture-skill selection for the specific area being changed or reviewed
- do not attach backend testing skills unless the repository's backend testing work benefits from that reusable testing guidance
- do not attach React skills to non-React areas unless repository docs explicitly route there

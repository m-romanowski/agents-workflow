# Project Index Template

## Purpose

- template for a repository-local router in `instructions/project/index.md`
- defines how repo-specific docs route to reusable skills without making them hot by default
- serves as a source pattern when `instructions/project/` does not exist yet and onboarding must generate `instructions/project/index.md`
- may also route to repository-local workflow customization docs such as optional personal skill bridges and public recommendation indexes

## Template Rules

- instantiate this file only with verified repository facts
- keep it short and routing-focused
- do not duplicate detailed architecture or tooling content here
- route to `instructions/skills/` only when the repository actually uses the relevant stack
- when onboarding a repository with no project docs yet, generate `instructions/project/index.md` from this template first and then use the generated file as the active routing source
- do not imply one repository-wide backend architecture when different modules or areas use different structural patterns
- for mixed-architecture repositories, prefer loading the module doc before selecting architecture-specific skills

## Suggested Sections

- purpose
- load by task type
- load by area or module
- canonical project files

## Example Routing Pattern

### Backend Implementation

For a repository with no `instructions/project/` docs yet:

- generate `instructions/project/index.md` and `instructions/project/skill-profile.md` from the templates first
- generate `instructions/project/modules/<module>.md` from `instructions/project-template/module.md` only when repository evidence shows module-level architectural or testing differences
- then continue through the generated project files as the active routing source

Load:

- `instructions/project/skill-profile.md`

Then:

- if the repository uses different architectures across backend areas and the touched module is known, load `instructions/project/modules/<module>.md` first
- if the touched area uses Spring Boot, load `instructions/skills/spring-boot/index.md`
- if the touched module or area is documented as using a modular package-level architecture pattern, load `instructions/skills/modular-hexagonal/index.md`
- if the task is mainly about backend testing strategy or backend test design, load `instructions/skills/backend-testing/index.md`
- load only the Spring Boot child file needed by the task
- load deeper project docs only when the repository has them and the task requires them

### Backend Code Review

Load:

- `instructions/project/skill-profile.md`

Then:

- if the repository uses different architectures across backend areas and the reviewed module is known, load `instructions/project/modules/<module>.md` first
- if the review touches Spring Boot code, load `instructions/skills/spring-boot/index.md`
- load `instructions/skills/spring-boot/review.md`
- if the reviewed module or area is documented as using a modular package-level architecture pattern and the review is mainly about module boundaries, cohesion, coupling, or dependency direction, load `instructions/skills/modular-hexagonal/review.md`
- if the review is mainly about backend tests, test strategy, or test scope, load `instructions/skills/backend-testing/review.md`
- load deeper project docs only when local structure is known to differ

### Frontend Implementation

Load:

- `instructions/project/skill-profile.md`

Then:

- if the touched area uses React, load `instructions/skills/react-js/index.md`
- load only the React child file needed by the task
- load deeper project docs only when the repository has them and the task requires them

### Frontend Code Review

Load:

- `instructions/project/skill-profile.md`

Then:

- if the review touches React code, load `instructions/skills/react-js/index.md`
- load `instructions/skills/react-js/review.md`
- load deeper project docs only when local structure is known to differ

### Workflow Customization Or Agent Setup

Load:

- `instructions/project/personal-skill-policy.md`

Then:

- load `instructions/project/recommended-third-party-skills.md` only when the operator asks about optional or recommended third-party skills
- keep optional-skill recommendation docs cold during normal implementation, review, and investigation tasks unless explicitly requested

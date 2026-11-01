# AGENTS.md

Conventions for working in this repo. Humans and AI agents both follow these.

## What this repo is

Amish's personal skills and agents, meant to work across Claude Code, GitHub Copilot and other agents that follow the open `SKILL.md` convention.

## Layout

- `skills/<category>/<skill-name>/SKILL.md` — one folder per skill. `skills/` is the single source of truth.
- `agents/` — subagent definitions (none yet).
- `.claude-plugin/` — plugin and marketplace manifests. When you add a category folder under `skills/`, add it to `plugin.json`.

## Writing a skill

- `SKILL.md` must start with YAML frontmatter containing `name` (same as the folder name) and `description`. The description says what the skill does and when to use it, because the agent decides whether to load the skill from it.
- Keep supporting files (templates, schemas, scripts) inside the skill's folder and refer to them by relative name.
- A skill must never store user data inside its own folder. Data belongs in the user's repo; ship blank templates under `templates/`.
- Do not put personal or confidential information anywhere in this repo. It may become public.
- Skills must not depend on a specific agent's tools. Describe what to do, not which tool to call.

## Adding things

- New skill: create the folder, write `SKILL.md`, add it to the README reference list.
- Commit messages: `skills: add <name>`, `skills: update <name>`, `agents: ...`, `docs: ...`.

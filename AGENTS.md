# AGENTS.md

Conventions for working in this repo. Humans and AI agents both follow these.

## What this repo is

Amish's personal skills and agents, meant to work across Claude Code, GitHub Copilot and other agents that follow the open `SKILL.md` convention.

The career skills form **one suite**: they help a software engineer keep a structured, evidence-backed career record and turn it into resumes and interview preparation. The design and its evidence are in `docs/PLAN.md` and `docs/research/`.

## Layout

- `skills/<category>/<skill-name>/SKILL.md` — one folder per skill. `skills/` is the single source of truth.
- `agents/` — subagent definitions (none yet).
- `.claude-plugin/` — plugin and marketplace manifests. When you add a category folder under `skills/`, add it to `plugin.json`.
- `docs/` — the plan (`PLAN.md`) and research (`research/`). Research notes are kept as evidence; don't edit them after the fact.
- `evals/<skill-name>/` — triggering queries and evaluation scenarios for each skill.
- `tests/` — automated tests for the skills' scripts. Use synthetic data only.

## The career suite

- The suite today: `setup-career-skills` (environment and first-time setup), `maintain-career-record` (record owner) and `capture-work-experience` (STAR capture). Planned: `build-resume`, `optimise-resume-for-jd`, `prepare-interview-stories`.
- The career skills are always installed together. A skill may rely on its sibling skills being present and refer to their files by a path relative to its own folder (for example `../maintain-career-record/scripts/validate.py`). Each skill says in its instructions that it needs the whole suite.
- `maintain-career-record` owns the career record's data format and the shared scripts. Other skills read and write the record only through that format and run the shared scripts; they don't keep their own copies.
- Skills that generate career material (bullets, resumes, interview stories) use only facts the user has confirmed in the record and never invent facts, numbers, titles or dates.

## Writing a skill

- `SKILL.md` must start with YAML frontmatter containing `name` (same as the folder name) and `description`. The description says what the skill does and when to use it, written in the third person, because the agent decides whether to load the skill from it.
- Name skills verb-first in kebab-case (for example `capture-work-experience`, `build-resume`).
- Keep supporting files inside the skill's folder (`scripts/`, `references/`, `templates/`) and refer to them by relative path with forward slashes.
- A skill must never store user data inside its own folder. Data belongs in the user's repo; ship blank templates under `templates/`.
- Do not put personal or confidential information anywhere in this repo, including examples and samples. It may become public. Use made-up names such as "Example Corp Pvt. Ltd.".
- Skills must not depend on a specific agent's tools. Describe what to do, not which tool to call.

## Python

- Scripts need Python 3.9 or later and PyYAML. Nothing else outside the standard library.
- In this repo, use the uv-managed virtual environment: run `uv sync` to create `.venv`, then run scripts and tests with `.venv/Scripts/python` (Windows) or `.venv/bin/python`. Never install packages globally with pip.
- Add new dependencies to `pyproject.toml` with `uv add`, not by hand-installing them.
- In a user's career repo, the skills use `career/.venv`, which setup-career-skills creates with uv from `maintain-career-record/scripts/requirements.txt`.

## Adding things

- New skill: create the folder, write `SKILL.md`, add evals under `evals/<skill-name>/`, and add it to the README reference list.
- Commit messages: `skills: add <name>`, `skills: update <name>`, `agents: ...`, `docs: ...`.

# AGENTS.md

Conventions for working in this repo. Humans and AI agents both follow these.

## What this repo is

Amish's personal skills and agents, meant to work across Claude Code, GitHub Copilot and other agents that follow the open `SKILL.md` convention.

The career skills form **one suite**: they help a software engineer keep a structured, evidence-backed career record and turn it into resumes and interview preparation. The design and its evidence are in `docs/PLAN.md` and `docs/research/`.

## Layout

- `skills/<category>/<skill-name>/SKILL.md` — one folder per skill. `skills/` is the single source of truth.
- `agents/` — subagent definitions (none yet).
- `.claude-plugin/` — plugin and marketplace manifests. When you add a category folder under `skills/`, add it to `plugin.json`.
- `docs/` — the plan (`PLAN.md`), the maintainer's guide (`MAINTAINING.md`) and research (`research/`). Research notes are kept as evidence; don't edit them after the fact.
- `.github/` — the CI workflow and the PR template. `.claude/settings.json` blocks merge and push-to-main commands for Claude Code.
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

## Changes, pull requests and merging

These rules are strict. They apply to every agent, whatever the user asked for in the same message. `docs/MAINTAINING.md` explains why each rule exists.

Anything an agent does on GitHub (pushing, opening a PR, commenting) is recorded under the user's account, as if the user did it.

1. **Work on a branch.** Never commit to `main` and never push to `main`. Create a branch for each change, named `<area>/<short-description>` (for example `skills/capture-offboard-work`).
2. **Verify before you ask to open a PR.** Run the tests and validate the fixture record (both commands are under "Development" in the README). Both must pass.
3. **Evals come before the PR when a skill changes.** If a change touches anything under `skills/`:
   - List the evals it affects: every new scenario, every existing scenario whose expected behaviour depends on what changed, and the trigger queries in `evals/triggers.md` if a skill's `description` changed.
   - Ask the user for permission to run them, because evals use model usage. Name the scenarios and the models.
   - Once the user agrees, run them as described under "Running evals" below, and record the real results in `evals/RESULTS.md`.
   - If you can't run an eval, or the user says not to, stop and tell the user what wasn't run. Don't open the PR unless the user says how to proceed.
   - Never write that an eval passed unless you ran it and graded it.
4. **Ask before pushing or opening a PR.** Show the user what changed and the verification results, and ask first. Pushing a branch and opening a PR are public actions.
5. **Fill in the PR template** (`.github/pull_request_template.md`). The "Verification" section lists every command and eval you ran, with its result, and everything you didn't run. Write "Nothing" only when everything was verified.
6. **Never merge.** Only the user merges, by hand on GitHub. This holds even when the user asks you to merge: give them the PR link and remind them that merging is theirs to do. Don't approve PRs, don't mark your own draft PRs ready, and don't use auto-merge.
7. **Never bypass the safeguards.** Don't force-push, rewrite published history, skip hooks or checks, or change CI, branch protection, repository settings or `.claude/settings.json` unless the user asked for that specific change.

### Running evals

Use the method recorded in `evals/RESULTS.md`:

- Give a fresh agent, one per model and scenario, only the installed skills, the scenario's directory or fixture, and the user's message. Never show it `expected_behavior`.
- When the skill asks the user something, the agent writes the message it would send and stops. If a scenario needs replies from the user, script them.
- Grade each transcript by hand against `expected_behavior`.
- For trigger tests, give a fresh agent only the skills' frontmatter and the queries in `evals/triggers.md`.
- Add a dated section to `evals/RESULTS.md` with the skill versions, the models, a result for each scenario, and anything that couldn't be tested (for example GitHub Copilot).

## Adding things

- New skill: create the folder, write `SKILL.md`, add evals under `evals/<skill-name>/`, and add it to the README reference list.
- Commit messages: `skills: add <name>`, `skills: update <name>`, `agents: ...`, `docs: ...`, `repo: ...` (CI, templates, settings, rules).

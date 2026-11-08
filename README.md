# skills-and-agents

My personal skills and agents for AI coding assistants. Built to work across Claude Code, GitHub Copilot and any agent that supports the `SKILL.md` convention.

## Installation

### Claude Code

```
claude plugin marketplace add thisisamish/skills-and-agents
claude plugin install amish-skills@amish
```

### GitHub Copilot (CLI and VS Code)

```
copilot plugin marketplace add thisisamish/skills-and-agents
copilot plugin install amish-skills@amish
```

### Other agents

```
npx skills@latest add thisisamish/skills-and-agents -a <agent>
```

When asked which skills to install, select all of the career skills. They are a suite and depend on each other.

While the repo is private, your machine must be signed in to GitHub with access to it.

## Reference

### Career

The career skills are one suite and must be installed together. They write to the repo you run them in, under `career/`, never to this repo. The design follows [the plan](docs/PLAN.md), which is grounded in [this research](docs/research/reports/SWE%20resumes%20for%20India%20job%20switchers.md).

- [setup-career-skills](skills/career/setup-career-skills/SKILL.md) — run first: checks the suite is installed, creates the record's Python environment with uv (`career/.venv`, PyYAML only) and the `career/` record.
- [maintain-career-record](skills/career/maintain-career-record/SKILL.md) — keep the evidence-backed career record (profile, employment, skills, education, projects, goals) as YAML with an audit log and a generated `CAREER.md`; migrate an old `CMD.md`.
- [capture-work-experience](skills/career/capture-work-experience/SKILL.md) — capture pieces of work as STAR accomplishments and resume bullets that use only confirmed facts, including work that's on no board (help given, self-initiated work); backfill lots of past work from an inventory; log quick notes in `career/log.md` for later.

Resume building, job-description tailoring and interview preparation are planned but not built yet.

## Development

Scripts and tests use Python 3.9+ and PyYAML, managed with [uv](https://docs.astral.sh/uv/):

```
uv sync
```

This creates `.venv`. Run scripts and tests with its Python; don't install packages globally.

```
.venv/Scripts/python -m unittest discover tests    # Windows
.venv/bin/python -m unittest discover tests        # macOS/Linux
```

Evaluation scenarios and triggering queries for each skill are in [evals/](evals/).

Every change goes through a branch and a pull request, and only the maintainer merges. The rules are in [AGENTS.md](AGENTS.md), and the reasons behind them are in [docs/MAINTAINING.md](docs/MAINTAINING.md).

## Agents

None yet.

## License

[MIT](LICENSE)

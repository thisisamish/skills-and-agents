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

The career skills are one suite and must be installed together. They write to the repo you run them in, under `career/`, never to this repo. They are being rebuilt according to [the plan](docs/PLAN.md), which is grounded in [this research](docs/research/reports/SWE%20resumes%20for%20India%20job%20switchers.md).

- [maintain-career-record](skills/career/maintain-career-record/SKILL.md) — keep an evidence-backed career record and turn it into resumes and interview material.
- [capture-work-experience](skills/career/capture-work-experience/SKILL.md) — capture work experience as STAR-format accomplishments and resume bullets.

## Development

Scripts and tests use Python 3.9+ and PyYAML, managed with [uv](https://docs.astral.sh/uv/):

```
uv sync
```

This creates `.venv`. Run scripts and tests with its Python; don't install packages globally.

## Agents

None yet.

## License

[MIT](LICENSE)

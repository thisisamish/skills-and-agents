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

While the repo is private, your machine must be signed in to GitHub with access to it.

## Reference

### Career

- [career-master-document](skills/career/career-master-document/SKILL.md) — keep an evidence-backed career record and turn it into resumes, appraisal material and interview stories.
- [save-experience-in-star-format](skills/career/save-experience-in-star-format/SKILL.md) — keep a database of work experience as STAR-format resume bullets.

Both skills write to the repo you run them in, under `career/`, never to this repo.

## Agents

None yet.

## License

[MIT](LICENSE)

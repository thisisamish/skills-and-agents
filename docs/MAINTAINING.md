# Maintaining this repo

A guide for the maintainer: how a change gets from an idea onto `main`, why each rule exists, and what to do on GitHub. The rules agents must follow are in `AGENTS.md` under "Changes, pull requests and merging". This guide explains the reasoning behind them.

## Why there are rules at all

In November 2026, an agent was asked to make changes, open a PR and merge it. It did all three in 22 seconds. Its own PR description said that the new evals had been written but not run. Nothing stopped it, and GitHub recorded the merge under the maintainer's name.

Two lessons came out of that:

- **To GitHub, an agent is you.** Agents use your login, so everything they push, open or merge shows your name. GitHub can't tell your clicks from their commands.
- **Work isn't done when it's written; it's done when it's verified.** An agent that knows something is unverified must stop and say so, not ship it.

## The life of a change

```
branch → change → verify → (evals, with your OK) → you approve opening the PR
       → PR opened → CI checks run → you review → you merge
```

1. **Branch.** Every change starts on its own branch, such as `skills/capture-offboard-work`. A branch is a separate line of work, so `main` stays untouched until you decide otherwise.
2. **Change and verify.** The agent makes the change, then runs the tests and validates the fixture record.
3. **Evals.** If a skill changed, the agent lists which evals are affected and asks you before running them, because they use model usage. The results go into `evals/RESULTS.md`.
4. **Ask before the PR.** The agent shows you a summary and the verification results, and asks whether to push and open the PR.
5. **CI.** When the PR opens, GitHub Actions runs the tests on its own machines (the workflow is in `.github/workflows/ci.yml`). You'll see a green tick or a red cross on the PR.
6. **Review and merge.** You read the PR and merge it if you're satisfied. Only you merge.

## How each rule is enforced

| Layer | What it does | What it can't do |
|---|---|---|
| `AGENTS.md` | Tells every agent the rules: Claude Code, Copilot, anything else | Nothing forces an agent to follow it |
| `.claude/settings.json` | Claude Code refuses merge commands, pushes to `main` and force-pushes, and asks you before any push or PR | Only Claude Code reads it. It matches command text, so a differently worded command can slip past |
| PR template | Every PR has a verification section and a checklist | A box can be ticked without the work being done |
| CI (GitHub Actions) | Runs the tests and validation on every PR | Can't run evals, because they need a model and cost money |
| Branch protection (GitHub) | GitHub itself refuses changes to `main` that don't come through a PR with passing checks, from anyone | Can't tell whether evals were run |

No layer is complete, which is why there are several. The one gap no tool closes is evals: **you check the PR's verification section before you merge.**

## Reviewing and merging a PR on GitHub

1. Open the PR (the agent gives you the link, or use the "Pull requests" tab).
2. Read the description, especially **Verification** and **Not verified**. If anything under "Not verified" matters, don't merge; ask for it to be done first.
3. Open the **Files changed** tab and skim the diff. Green lines were added and red lines removed. You don't have to understand every line, but you should recognise what changed and why.
4. Check the **checks** at the bottom of the Conversation tab. All must be green. If one is red, click "Details" to see which test failed.
5. Click **Merge pull request**, then **Confirm merge**. Afterwards, GitHub offers to delete the branch. That's safe, because its commits are now on `main`.

Take your time. A PR that's been open for a day loses nothing. A bad merge has to be undone.

## When something goes wrong

- **A bad change was merged.** On the merged PR's page, click **Revert**. GitHub opens a new PR that undoes it, and you merge that like any other. History is never rewritten; the undo is a new change of its own.
- **An agent broke a rule.** Note what happened and which rule should have stopped it, then tighten `AGENTS.md` or `.claude/settings.json` in a PR.
- **CI fails on `main`.** Fix it before merging anything else, so a red tick always means "this PR broke something".

## Glossary

- **Branch:** a separate line of commits. `main` is the one everyone installs from.
- **Pull request (PR):** a request to merge a branch into `main`, with a page for discussion, checks and review.
- **Draft PR:** a PR marked "not ready". It can't be merged until someone marks it ready.
- **CI / checks:** automated jobs GitHub runs on every PR, here the tests and record validation.
- **Branch protection:** GitHub settings that put conditions on changing `main`, such as "only through a PR" and "checks must pass".
- **Force-push:** overwriting a branch's history on GitHub. It can destroy work, so it's blocked.
- **Revert:** a new commit that undoes an earlier one.
- **Evals:** test scenarios for a skill. A fresh agent runs each one, and the result is graded against the expected behaviour. Evals live in `evals/`.

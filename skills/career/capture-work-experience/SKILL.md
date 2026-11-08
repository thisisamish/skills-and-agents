---
name: capture-work-experience
description: Captures a software engineer's work as STAR (Situation, Task, Action, Result) accomplishments with evidence-backed resume bullets, and saves them into the career record kept by maintain-career-record. Splits descriptions that mix several pieces of work, interviews the user for missing details without inventing any, and checks every bullet before saving. Use when the user says "save this experience", asks for a resume bullet or STAR bullet, pastes a description of work they did, adds a piece of work to their career record, or gives a missing metric, detail or correction for an existing accomplishment. Also use it to backfill a lot of past work from an inventory, or to log or process quick notes in career/log.md, including help given to teammates and self-initiated work that's on no board. Profile, education, employers, roles and personal projects belong to maintain-career-record.
compatibility: Part of the career skills suite (setup-career-skills, maintain-career-record, capture-work-experience); install all of them together. Needs Python 3.9+ with PyYAML in career/.venv, created by setup-career-skills.
metadata:
  version: 2.1.0
  suite: career
---

# Capture work experience

Turn what the user did at work into accomplishment records that hold up in background checks and interview follow-up questions, plus resume bullets drawn only from those records.

## Paths used below

- **Record:** `career/` in the user's repository. Its format is in `../maintain-career-record/references/schema.md`.
- **Python:** `career/.venv/Scripts/python.exe` on Windows or `career/.venv/bin/python` elsewhere, written `PY`. Always call it by this path.
- **Scripts:** the full path of `../maintain-career-record/scripts/` (relative to this skill's folder), written `SCRIPTS`. Run commands from the root of the user's repository.

If `career/data/` is missing or `PY -c "import yaml"` fails, run setup-career-skills first. If the role this work belongs to isn't in `career/data/employment.yaml`, add it following maintain-career-record before saving.

## Rules

- **Never invent** a fact, number, technology, scale or outcome. If it isn't from the user, it isn't in the record or the bullet.
- **The user's own work.** Record what the user personally did in `actions`; what the team did goes in `team_context`. Ask "what did you do, and what did others do?" when the user says "we".
- **Employer of record.** Client work is recorded under the user's employer. The client is described by industry and scale, never named if it may be under NDA. If you don't know whether it is, ask whether the client's name and absolute figures (users, revenue) may be stated, and don't name the client meanwhile.
- **Confidentiality.** Never record source code, credentials, internal URLs or system names, customer names, screenshots or proprietary details. Generalise instead ("a synchronisation defect between persistent and in-memory data layers"). When unsure, leave it out.
- **Counts are legitimate.** Tickets closed, stories delivered and defects fixed are real measures of scope. Keep them, and ask what changed because of them.
- **A metric is preferred, not mandatory.** Never pressure the user to produce or estimate a number. A bullet without a number is fine when it states a concrete outcome.
- **Record facts in full; present them later.** Record exact technologies and system context even when they seem unflattering: an older UI framework, a decades-old codebase, manual testing. What to emphasise or leave out is decided per bullet and per resume, never by leaving facts out of the record. Interviewers ask about the parts a resume skips.

## Workflow

Copy this checklist into your reply and tick it off. Don't move past a step until it's done.

```
- [ ] 1. Split: list each distinct piece of work; the user confirms the split
- [ ] 2. Interview: fill situation, task, actions, system context, outcome, metrics and evidence for each
- [ ] 3. Classify each against existing records: new, update or similar
- [ ] 4. Draft bullets (references/bullet-rules.md)
- [ ] 5. Check every bullet (list below); fix and re-check
- [ ] 6. The user approves the record and the bullet text
- [ ] 7. Save: NOTES.md entry, YAML, validate until 0 errors, render
```

**Lots of past work at once?** If the user is starting a record, is far behind, or wants to rebuild it ("list everything I've done", "backfill my record"), follow [references/backfill.md](references/backfill.md). It builds an inventory first, then runs this workflow row by row.

### 1. Split

Read the user's description and list each distinct piece of work. **More than one distinct action with its own result means more than one accomplishment.** Length is only a hint: a long bullet often mixes two pieces of work, but a short one can too. See the split example in [references/examples.md](references/examples.md).

- **Several pieces:** show the list and wait for the user to confirm or correct it before interviewing.
- **One obvious piece:** say how you read it, and ask the first interview questions in the same message.
- **Recurring work is one theme, not many records.** Repeated work of the same kind (answering new joiners' questions, unblocking teammates, refining stories with a lead, reviewing code) becomes one accomplishment covering a period. Its `actions` describe the pattern plus two or three specific instances: what the problem was, what the user did, what happened. Its metrics are counts over the period (`reported` when from memory), and its `origin` is usually `requested_by_others`. Ask for the specific instances: they make the theme credible in an interview. A one-off with its own result (a guide written, a tool built) is a separate accomplishment, linked with `similar_to` if related.
- **Clearly an update** ("I got the metric for…", "after the release…"): find the matching record first (step 3), then interview only for the new information.
- **From the work log** (`career/log.md`, schema.md section 8): when the user asks to process the log, or when it has uncaptured entries and the user is capturing anyway, read the unticked entries, group the ones that belong to the same piece of work or theme, and treat each group as one piece to split and interview as usual. A log line is a prompt, not a confirmed fact.

### 2. Interview

For each accomplishment, ask only for what's missing, a few questions at a time:

- **Where:** which employer and role? For client work, which client engagement in `employment.yaml`?
- **Origin:** who started it: assigned (board, tracker, manager), the user on their own initiative, or someone asking for their help? Sets `origin`. Self-initiated work and help given are rarely on a board, so ask about them explicitly when the user is listing work.
- **Situation:** what was the problem or need, and why did it matter?
- **Task:** what were you responsible for?
- **Actions:** what did you personally do? Which technologies, and why those?
- **Outcome:** what changed afterwards? For whom?
- **Measure:** by how much? What was it before? How do you know (dashboard, report, ticket history, release notes)?
- **System context:** what kind of system is it, and where does this work sit in it? Its components and how they communicate (services, nodes, messaging, shared databases), concurrency, data stores, and the size and age of the codebase. Record it in `scale` and `situation`. These facts let a bullet show the complexity of the work later, whatever the technology's age.
- **Scale:** how big was the system or problem (traffic, data volume, users, modules)? Scale is not a result: "handles 300k entries every 15 minutes" describes the load, not an improvement.
- **Evidence:** what would show this (PR, design doc, dashboard, recognition)? Describe it; never record internal links.
- **Period:** roughly when (month and year)?
- **Design, every time:** did you make any design decisions, and which alternatives did you reject? The answer is often yes even for "small" work, and it's what SDE-2 screens look for. If there were none, leave `design_ownership` empty rather than stretching.
- **Depth, for interviews and SDE-2 roles, only when relevant:** reliability or scaling choices; incidents you owned; mentoring; obstacles, trade-offs, what failed, lessons.

**When the user has no number,** help them find one: monitoring or APM dashboards, logs, ticket or defect history, release notes, CI reports, a quick before-and-after benchmark, user or request counts, or time saved per run multiplied by runs. An honest estimate is acceptable if the user makes it and says how; record it with `confidence: estimated`. Figures read from a system or document (dashboard, report, ticket history, config) are `measured`, even when the user did the counting; figures the user knows from memory are `reported`. Keep approximate figures as the user gives them (`value: "17+"`); ask for the exact number only if they have it. If the user still can't supply something, **stop and ask whether to accept it as a gap.** Only with their agreement, record it under `gaps` and save the record as `incomplete`.

### 3. Classify

Compare with the existing records in `career/data/accomplishments/` (titles, periods, technologies):

- **Update:** the same work, now with new information (a metric arrived, a result is known). Edit that record and keep its ID. A `confirmed` record stays confirmed if the new facts are user-confirmed. Leave its existing confirmed bullets alone, and add any new or revised bullet as a `draft` beside them until the user approves the text.
- **Similar:** different work with an overlapping theme or technology. Save it as a new record and add each ID to the other's `similar_to`.
- **New:** anything else.

When unsure, show the candidate match and ask.

### 4. Draft bullets

Follow [references/bullet-rules.md](references/bullet-rules.md). In short: lead with an action verb, then state the outcome, the measure and the method, naming the exact technologies, in at most two lines. Offer one or two variants if the work fits more than one track (for example backend and full-stack).

### 5. Check every bullet

- [ ] Every fact and number in the bullet is in the record, and every metric it uses is user-confirmed
- [ ] It describes one piece of work
- [ ] It says what changed (an outcome), not only what was done
- [ ] A count is paired with an outcome or context where one exists
- [ ] It names the technologies used, with exact names
- [ ] No client name, internal system name or other confidential detail
- [ ] 20–35 words is the usual range; outside it, check it isn't two bullets or padded

If any check fails, return to step 2 (missing information) or step 1 (two pieces of work in one).

### 6. User approval

Show the record summary and the bullet text. The record becomes `confirmed` (or `incomplete` with agreed gaps) only when the user agrees it's accurate. A bullet becomes `confirmed` only when the user approves its exact text. Metrics get `user_confirmed: true` only for numbers the user has stated or confirmed.

### 7. Save

1. Get a timestamp: `PY SCRIPTS/timestamp.py`.
2. Append one entry to `career/NOTES.md` with the user's information, in sanitized form, and the record changes. Use the format in schema.md section 7.
3. For a new record, run `PY SCRIPTS/new_id.py`, copy `../maintain-career-record/templates/accomplishment.yaml` to `career/data/accomplishments/<id>.yaml`, and fill it in. For an update, edit the existing file and set `updated`. Either way, add the timestamp to `sources`.
4. Link the technologies as evidence in `career/data/skills.yaml`, adding skills that are missing (leave `depth` unset unless the user has said it). If you set `similar_to`, add the link to both records. If the work came from `career/log.md`, tick those entries and append ` → <id>`.
5. `PY SCRIPTS/validate.py career`. Fix every error and re-run until it reports 0 errors. If an error says a bullet uses a number that isn't in the record, either add the number with the user or remove it from the bullet; never just make the check pass.
6. `PY SCRIPTS/render.py career`.
7. Tell the user what was saved, its status, any gaps, and any follow-up worth setting (for example "the error rate a month after launch"). Record that follow-up in `follow_up`.

## Troubleshooting

- **The role or employer isn't in employment.yaml:** add it first, following maintain-career-record, then save the accomplishment.
- **"No Python at …":** a stale virtual environment is active. Run `PY` by its full path, or ask the user to deactivate it.
- **The user only wants to note something for later** ("log this", "remind me I did this"): append one line to `career/log.md` in its format, with roles instead of names, and don't interview. No NOTES.md entry is needed until it's captured.
- **The user wants to skip questions and "just write the bullet":** draft it from what's known, mark the record `draft` or `incomplete` with gaps, and say clearly which parts are missing. Don't fill them in.
- **Sibling folders are missing:** the suite isn't fully installed; see setup-career-skills.

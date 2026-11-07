---
name: maintain-career-record
description: Maintains a software engineer's evidence-backed career record (profile, employers and roles, skills, education, projects, certifications, recognition, learning, goals) as structured YAML in the user's repo, with an append-only audit log and a generated CAREER.md view. Use when the user wants to add, correct or review career details, update their profile, education, skills or projects, review evidence gaps, or migrate an old CMD.md. For saving a specific piece of work as STAR resume bullets, use capture-work-experience instead; for first-time setup, use setup-career-skills.
compatibility: Part of the career skills suite (setup-career-skills, maintain-career-record, capture-work-experience); install all of them together. Needs Python 3.9+ with PyYAML in career/.venv, created by setup-career-skills.
metadata:
  version: 2.0.0
  suite: career
---

# Maintain career record

Keep a durable, factual record of a software engineer's career that resumes and interview preparation are later built from. The record is the product; resumes are derived from it.

## Paths used below

- **Record:** `career/` in the user's current repository.
- **Python:** the record's environment, `career/.venv/Scripts/python.exe` on Windows or `career/.venv/bin/python` elsewhere. Written as `PY` below. Always call it by this path.
- **Scripts:** the full path of this skill's `scripts/` folder, written as `SCRIPTS` below. Other career skills use `../maintain-career-record/scripts/` relative to their own folder. Commands run from the root of the user's repository.

Before anything else, check that `career/data/` exists and that `PY -c "import yaml"` works. If either fails, run the setup-career-skills skill first.

**If the user describes a piece of work they did** ("I built…", "I migrated…", "add this project I led to my record"), use capture-work-experience for it, even when they say "career record". This skill handles everything around that work.

## Rules

- **Never invent** facts, numbers, titles, dates, technologies or outcomes. Record only what the user said, and mark what is inferred.
- **Employer of record.** Work done for a client is recorded under the employer that pays the user. The client is described by industry and scale (`client_descriptor`), never by name if it may be under NDA.
- **Confidentiality.** Never store source code, credentials, internal URLs or system names, customer names, screenshots, proprietary algorithms, or anything the user's employer forbids taking out. Generalise instead: "resolved a synchronisation defect between persistent and in-memory data layers". When unsure, leave the detail out.
- **No personal data** on the record beyond name, city, email, phone and profile links: no photo, date of birth, gender, marital status, religion, father's name or full address.
- **Exact values.** Scores, titles, employer names and dates exactly as on official documents. Never round a CGPA or percentage, and never expand an abbreviation the user didn't expand.
- **Unknown stays unknown.** If the user gives only a year, record the year; if they don't know, leave it empty and add a gap. Never fill in a plausible month, title or name.
- **Neutral questions.** Ask "what changed, by how much, how do you know, who else was involved?" rather than inviting adjectives. Don't push the user to inflate or to estimate numbers they don't have.
- **Goals are not evidence.** Keep aspirations in `goals.yaml` only.
- **Edit YAML, never CAREER.md.** It is regenerated.

The field-by-field format is in [references/schema.md](references/schema.md). Blank files are in `templates/`.

## Recording new or corrected information

Copy this checklist into your reply and tick it off:

```
- [ ] 1. Identify the new facts, corrections, skills, evidence or goals
- [ ] 2. Route accomplishments (a specific piece of work) to capture-work-experience
- [ ] 3. Remove or generalise confidential detail
- [ ] 4. Get a timestamp: PY SCRIPTS/timestamp.py
- [ ] 5. Append one NOTES.md entry (Source, New Information, Record Changes, Evidence Status)
- [ ] 6. Edit the YAML files; put the timestamp in `sources` where the file has that field
- [ ] 7. PY SCRIPTS/validate.py career — fix every error and re-run until it reports 0 errors
- [ ] 8. PY SCRIPTS/render.py career
- [ ] 9. Tell the user what changed and list any warnings worth their attention
```

Notes on the steps:

- **Step 2:** if the user describes work they did ("I built…", "I fixed…", "here's what I did this sprint"), hand it to capture-work-experience. This skill records the surrounding facts: employers, roles, client engagements, skills, education, projects, recognition, learning and goals.
- **Step 5:** NOTES.md is append-only. To correct a fact, append a new entry saying what it corrects; never edit old entries. Skip the entry only for questions that add nothing durable.
- **Step 6:** link each skill to the accomplishment or project IDs that show it. A skill with no evidence stays in the record but is never put on a resume.
- **Step 7:** read each error message; it names the file, field and fix. If a fix needs information you don't have, ask the user rather than guessing.

## Reviewing the record

When the user asks for a review, or at least once a quarter:

1. Run `PY SCRIPTS/render.py career` and read the **Open items** section of `career/CAREER.md`. It lists drafts, gaps, due follow-ups, unknown dates, technologies missing from skills, roles with no captured work, and empty sections.
2. For each follow-up that is due, ask the user for the result (e.g. "the error rate after launch").
3. For each incomplete record, offer ways to fill its gaps. Examples: where a metric can be found (dashboards, release notes, ticket history), or a before-and-after comparison the user could run.
4. Point out skills without evidence and ask whether there is work that shows them.
5. Summarise the strongest confirmed accomplishments, the evidence gaps, and any recent work that hasn't been captured yet. Offer a capture-work-experience session for the uncaptured work.

## Migrating an old CMD.md

If `career/CMD.md` (or another legacy Career Master Document) exists, follow [references/migration.md](references/migration.md). Never delete legacy files; the user does that after reviewing.

## Other career skills

| The user wants to… | Use |
|---|---|
| Set up the record or its Python environment | setup-career-skills |
| Save a piece of work as STAR bullets, or update one | capture-work-experience |
| Build a resume, tailor one to a job description, prepare interview stories | Not available yet. Say so, and offer to strengthen the record in the meantime. |

## Troubleshooting

- **`PY` not found or `import yaml` fails:** run setup-career-skills.
- **"No Python at …" error:** a stale virtual environment is probably active (the `VIRTUAL_ENV` variable is set). Run `PY` by its full path or ask the user to deactivate it.
- **Validation keeps failing on a source timestamp:** the NOTES.md heading must be exactly `## <timestamp>` at the start of a line, matching the value in `sources`.
- **Two `career/` folders:** ask the user which one is current; never merge them silently.
- **No write access:** show the proposed YAML and NOTES.md entry, and don't claim the record was updated.

# Evaluation results

## 2026-11-07: first full run (skills v2.0.0 / setup v1.0.0)

**Method.** A fresh agent per model and skill was given only the installed skills, a scenario directory, and the user's message. It never saw `expected_behavior`. When a skill required an answer or approval from the user, the agent wrote the message it would send and stopped. Each transcript was graded by hand against the scenario's `expected_behavior`. Trigger tests gave a fresh agent only the three skills' frontmatter and the queries in `triggers.md`.

Models: Claude Sonnet and Claude Opus. **Not tested: GitHub Copilot**, as it couldn't be driven from this environment.

### Triggering

| Model | Correct | Notes |
|---|---|---|
| Sonnet | 19 / 19 | Flagged migration ownership (setup vs maintain) and job-vs-work wording as possible ambiguities |
| Opus | 19 / 19 | Same ambiguities; also noted that capture's description didn't say where profile and education belong |

### Scenarios

| Scenario | Sonnet | Opus |
|---|---|---|
| capture 01: missing metric | pass | pass |
| capture 02: mixed paragraph | pass | pass |
| capture 03: count bullet | pass | pass |
| capture 04: NDA client | pass | pass |
| capture 05: update existing | pass | pass |
| maintain 01: education (exact CGPA) | pass | pass |
| maintain 02: route accomplishment | pass | pass |
| maintain 03: review | pass | pass |
| setup 01: fresh repo | pass | pass |
| setup 02: legacy CMD.md | pass | pass |
| setup 03: skills repo (refuse) | pass | pass |

Single-turn limits: capture 05's "runs validate.py" could only be observed in the re-check below, where the user's replies were scripted.

### Real migration

A fresh agent followed setup-career-skills and the migration guide on a real legacy record (an 18-section CMD.md plus NOTES.md). The result: 9 accomplishments (6 confirmed, 3 incomplete), 2 employers, 3 roles, 56 skills, and 0 validation errors. Nothing was committed or deleted.

### Problems found and fixed after the run

- **Schema:** it couldn't express unknown or year-only dates, unknown NDA status, user-reported counts, or gaps and notes outside accomplishments. As a result, the migration had to guess role-bound dates and default NDA to true. Fixed: `YYYY` dates are now accepted; an accomplishment period is optional (with a warning); `nda: unknown` is allowed; there is a `reported` confidence level; and every entry can have `notes` and `gaps`. The guessed values in the migrated record were corrected.
- **Setup and migration order:** setup created files before migration's "clean tree" check, and both guides ran `init.py`. Fixed: setup checks for a clean tree first, and hands legacy data to the migration guide without running `init.py`. Consent the user already gave is respected.
- **Scripts:** they wrote `__pycache__` into the installed skill folder. Fixed with `sys.dont_write_bytecode`.
- **Review:** it was thin when nothing was flagged. Fixed: `CAREER.md` Open items now lists technologies missing from skills, roles with no captured work, unknown dates, draft bullets awaiting approval, gaps on any entry, and empty sections.
- **Capture workflow:** it now
  - confirms the split and asks the first questions in one message for a single obvious piece of work;
  - classifies first for obvious updates;
  - asks which employer, role or engagement the work belongs to;
  - asks before naming a client or stating absolute figures when NDA status is unknown;
  - keeps approximate counts ("17+");
  - leaves existing confirmed bullets alone on update and adds new ones as drafts;
  - keeps `similar_to` symmetric.
- **Descriptions:** setup now says it hands migration to maintain-career-record, and capture says profile, education, roles and projects belong to maintain-career-record.
- **migrate_cmd.py:** section targets now match the guide, and sections without sub-headings list each item.
- **uv on PATH:** setup now looks for an installed uv that isn't on PATH.

### Re-check after the fixes (Sonnet, user replies scripted)

| Scenario | Result |
|---|---|
| capture 05: update existing, run to save | pass. Kept the ID and confirmed status, left the old bullet alone, staged the new bullet as a draft before approval; validate 0 errors, 0 warnings |
| setup 02: legacy, with the user's consent given up front | pass. Checked for a clean tree, didn't ask again, ran `init.py` once after moving the file, didn't invent an accomplishment from placeholder content; validate 0 errors |

Wording fixes from the re-check:
- create `career/legacy/` before `git mv`;
- clearer `measured` vs `reported` definitions;
- leave a new skill's `depth` unset;
- don't create an accomplishment whose role is unknown.

## 2026-11-08: plugin 0.3.0 (capture and maintain v2.1.0 / setup v1.1.0) — not yet run

New scenarios added and not yet evaluated: capture 06 (recurring help), 07 (backfill start), 08 (log this); maintain 04 (review asks about off-board work). Four new capture trigger queries were added to `triggers.md`. The fixture gained `career/log.md`. Re-run triggering and all scenarios before relying on the 2026-11-07 results for this version.

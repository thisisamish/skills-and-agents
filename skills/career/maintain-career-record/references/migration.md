# Migrating a legacy Career Master Document

For records created by the old `career-master-document` skill: `career/CMD.md` (an 18-section Markdown document) plus `career/NOTES.md`. If the user has the old STAR database instead (`EXPERIENCE_DB.md` with `changelog.json`), map each table row to one accomplishment the same way, using the changelog entries as sources only if they match NOTES.md entries.

Copy this checklist into your reply and tick it off:

```
- [ ] 1. Make sure the user's repo has no uncommitted changes (ask them to commit first)
- [ ] 2. Create career/legacy/, then git mv career/CMD.md career/legacy/CMD.md (a plain move if the file isn't tracked); leave NOTES.md exactly where and as it is
- [ ] 3. PY SCRIPTS/init.py .          (creates any missing data files; keeps NOTES.md; skip if setup already ran it)
- [ ] 4. PY SCRIPTS/migrate_cmd.py career/legacy/CMD.md   (writes the worksheet)
- [ ] 5. Fill in career/data/ section by section, ticking the worksheet
- [ ] 6. Set status and sources for every record (rules below)
- [ ] 7. Append a migration entry to NOTES.md
- [ ] 8. PY SCRIPTS/validate.py career — fix and re-run until 0 errors
- [ ] 9. PY SCRIPTS/render.py career
- [ ] 10. Give the user the review list (below); do not delete career/legacy/
```

If `init.py` is run before the setup environment exists, use any Python 3.9+; it needs no packages. If the user has already asked for the migration (for example while running setup), that is their approval: don't ask again.

## Mapping

The worksheet names the target for every section. In short:

| Legacy section | New home |
|---|---|
| 1 Metadata, 2 Profile | `profile.yaml`; objectives to `goals.yaml`; profile prose becomes a draft headline at most |
| 3 Timeline, 4 Current role | `employment.yaml` (employers, roles, engagements); schooling and degrees to `education.yaml` |
| 5 Master accomplishments | one `accomplishments/<id>.yaml` each (ID from `new_id.py`) |
| 7 Engineering stories | merged into the matching accomplishment: STAR fields plus `interview` (obstacles, trade-offs, lessons) |
| 6 Master resume bullets | `bullets` on the matching accomplishment, status `draft` |
| 8 Quantified metrics | `metrics` on the matching accomplishment |
| 9 Technical skills, 10 Capabilities | `skills.yaml`, each with evidence IDs |
| 11 Documentation | accomplishments with category `documentation`, or `recognition.yaml` if it is praise for documentation |
| 12 Recognition | `recognition.yaml` |
| 13 Projects | personal or academic ones to `projects.yaml`; professional ones become accomplishments or role summaries |
| 14 Learning, 15 Goals | `learning.yaml`, `goals.yaml` |
| 16 Evidence gaps | `gaps` on the matching records |
| 17 Resume extraction notes, 18 Career narrative | not migrated; they can be regenerated |

## Rules

- **Move content, don't improve it.** Keep the user's facts and wording; restructure only. Don't add numbers, technologies or outcomes that aren't in CMD.md or NOTES.md, and don't expand abbreviations (keep "ECPL"; add a gap asking for the full legal name).
- **Unknown stays unknown.** If CMD.md has no dates for an accomplishment, leave `period` empty and add a gap; never copy in the role's dates. Year-only dates are fine. If NDA status isn't stated, use `nda: unknown`. If a score's scale isn't stated, leave `scale` empty.
- **Nothing is lost.** Facts with no structured field go into `notes` on the matching entry (role, project, skill, recognition, learning); missing information goes into its `gaps`. For example, "C++: repository exposure, not personally worked on" belongs in the role's notes, not in skills.yaml.
- **Sources.** For each record, find the NOTES.md entries that contain its facts and put their timestamps in `sources`. If several entries share a timestamp, that's fine: list it once.
- **Status.** The title is a label you write; the other fields are facts.
  - `confirmed` only when NOTES.md contains the facts behind situation, task, actions and outcome, and every metric.
  - `incomplete` when NOTES.md supports the record but something required is missing. List the missing pieces in `gaps`.
  - `draft` when the record is only in CMD.md, with nothing in NOTES.md behind it.
  - If a NOTES-backed record also carries detail found only in CMD.md, keep the detail, make the record `incomplete`, and add a gap such as "situation detail only in legacy CMD.md; confirm with user".
  - Recognition found only in CMD.md gets `status: draft` and empty `sources`.
- **Metrics.** `user_confirmed: true` only if NOTES.md shows the user giving that number. Set `confidence` from how the user described it: `measured` (from a tool or report), `reported` (a count the user knows, such as stories delivered), `estimated`, or `relative_only`. Keep approximate values as text (`"30+"`, `"~60"`). A metric that matches no accomplishment goes into the role's `notes`.
- **Bullets** start as `draft`; the user confirms them later through capture-work-experience. If a bullet uses a number that isn't in its record, keep the number out of the bullet and add a gap instead.
- **An accomplishment with no known employer or role:** don't create it and don't guess the role. List it in the review list so the user can say where it belongs.
- **Unmatched bullets or stories** (no accomplishment to attach to): don't invent an accomplishment. List them in the review list. A bullet that spans two accomplishments goes on the one it mostly describes, with a gap saying so.
- **Employer of record and confidentiality rules apply** exactly as in SKILL.md. If CMD.md contains a client name or an internal system name, generalise it and mention it in the review list. Public product or feature names are a judgement call: keep them, and list them for the user to check.
- **NOTES.md is never edited by the skill**, even when it contains confidential or sensitive history (client names, salary, third-party personal details). List what you noticed in the review list; it is the user's file, and only they may decide to redact it.
- **Legacy NOTES.md entries** may use "### CMD Impact" instead of "### Record Changes", a different file header, or repeated timestamps. That's expected; cite their timestamps as they are.

## Migration NOTES.md entry

```
## <timestamp from timestamp.py>

### Source
Migration from legacy CMD.md (career/legacy/CMD.md)

### New Information
- None; content restructured only.

### Record Changes
- Created data files and N accomplishments (<ids>); M confirmed, K incomplete, J draft.

### Evidence Status
- Status set from NOTES.md evidence; drafts need user review.
```

## Review list for the user

End with a short list:
- records left as `draft` or `incomplete`, and why;
- bullets or stories that couldn't be matched to an accomplishment;
- anything generalised for confidentiality;
- legacy sections that weren't migrated (17, 18);
- a reminder to compare `career/CAREER.md` with `career/legacy/CMD.md`, then commit, and delete `career/legacy/` once satisfied.

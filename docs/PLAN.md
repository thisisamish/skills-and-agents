# Plan: an evidence-backed career record system

Status: Phases 0–5 implemented on 2026-11-07. The future skills (`build-resume`, `optimise-resume-for-jd`, `prepare-interview-stories`) are not built yet. Evaluation results are in [evals/RESULTS.md](../evals/RESULTS.md).

**Changes from the original plan, made during implementation:**
- **New skill:** `setup-career-skills`, the suite's entry point. It checks that every skill is installed, creates `career/.venv` with uv (PyYAML only), creates the record, and hands any legacy data to the migration guide. This settles the runtime convention left open in §4.
- **Employer link:** accomplishments link to a `role_id`, whose employer is the employer of record, instead of carrying both `employer_id` and `role_id`.
- **Unknown values:** dates may be `YYYY` or empty, and an accomplishment period is optional (validate.py warns). `nda` may be `unknown`. Metrics gain a `reported` confidence level. Every entry may carry `notes` and `gaps`.
- **New script:** `timestamp.py` gives NOTES.md headings the real local time.
- **Bytecode:** scripts never write `__pycache__` into the skill folder.

**Changes on 2026-11-08 (plugin 0.3.0), from using the suite on a real record rebuild:**
- **Off-board work.** Accomplishments gain an optional `origin` (`assigned`, `self_initiated`, `requested_by_others`). Recurring help (onboarding, unblocking, refinement) is captured as one theme accomplishment with specific instances, not one record per instance. Reviews ask about work that's on no board, using prompts adapted from the brag-document template in the research notes.
- **Work log.** `career/log.md`, created by `init.py`, holds quick one-line notes that capture-work-experience processes later. render.py counts uncaptured entries under Open items.
- **Backfill.** capture-work-experience gains `references/backfill.md` and `templates/inventory.md`: inventory first (four buckets by who started the work), then metric suggestions, then collection, then capture row by row.
- **Complete, not curated.** The record keeps every fact, including unflattering ones such as older technologies or the system's age. Presentation for a target role happens only in bullets (new section in `bullet-rules.md`). Capture always asks about system context and design decisions. The research has no evidence on screener bias toward particular technology names, and the guidance says so.

## 1. Goal

Help a software engineer keep a structured, living record of their impactful work, and turn that record into resumes for switching jobs. The primary user has 2–3 years of experience at an Indian IT services company and is targeting SDE-1 (possibly SDE-2) roles at Indian product companies, startups and MNC offices/GCCs.

The skills form **one suite that is installed and used together**:

| Skill | Was | Status | Job |
|---|---|---|---|
| `maintain-career-record` | `career-master-document` | rebuild now | Owns the career record: data format, shared scripts, profile, employment, skills, education, projects, goals, audit log, generated view, migration. |
| `capture-work-experience` | `save-experience-in-star-format` | rebuild now | Captures work experience as STAR accomplishments and resume bullets, and writes them into the record. |
| `build-resume` | — | later | Builds an ATS-friendly resume from the record. |
| `optimise-resume-for-jd` | — | later | Builds a resume tailored to one job description from the record. |
| `prepare-interview-stories` | — | later | Turns STAR records into a competency-tagged story bank and practice. |

The evidence for everything below is in [the research report](research/reports/SWE%20resumes%20for%20India%20job%20switchers.md). Requirement IDs (R1–R34) refer to its Section 5.

## 2. Principles from the research

1. **The record is the product, not the resume.** Generated text is cheap; what's scarce is specific, verifiable detail that survives background verification and interview follow-up questions (report §4.5, §7).
2. **Nothing reaches a resume unless it's in the record and the user confirmed it.** Every claim has a pointer back to its source (R30, R31).
3. **Capture work close to when it happened.** Memory fades fast and people judge their own work poorly, so the skills prompt for capture after each milestone and ask neutral questions like "what changed, by how much, how do you know" (R1, R6).
4. **STAR records are deeper than bullets.** They hold obstacles, trade-offs, failures and lessons so the same record can back an interview story (R10, R11).
5. **Formatting and spelling are checked by scripts, not by asking the model to be careful** (R14–R16, R20).
6. **Advice follows the evidence.** Quantify where you can defend the number, but don't demand a number in every bullet. Ticket or story counts are a legitimate measure, not "hollow" (report §3.4, §4.4).

## 3. Decisions

| # | Topic | Decision |
|---|---|---|
| — | Target user | 2–3 years experience, services to product, SDE-1 (maybe SDE-2), India |
| — | Scope of the record skill | Resume and interview-prep data. Appraisal and promotion material is dropped. |
| — | How the skills relate | `capture-work-experience` feeds the record owned by `maintain-career-record` |
| — | Storage | Structured YAML is the source of truth, plus a generated Markdown view |
| — | Scripts | Python 3.9+ plus **PyYAML** (the only third-party dependency) |
| — | Interview prep | A separate future skill that reads the same record |
| — | Migration | Required, from the existing `CMD.md` and `NOTES.md` in the user's private career-vault repo |
| — | Agents | Claude Code (Opus/Sonnet) and GitHub Copilot |
| D1 | Installation and shared scripts | The skills are **always installed together as one suite**. The shared scripts live once, in `maintain-career-record/scripts/`. Other skills run them by a path relative to their own folder (`../maintain-career-record/scripts/<name>.py`). Every skill states in its instructions and `compatibility` field that it needs the whole suite. The README and AGENTS.md say to install the suite, not individual skills. Nothing is copied into the user's repo. |
| D2 | Names | Verb-first names, as in §1. Folders, `name` fields, README, plugin manifest and cross-references are renamed together. |
| D3 | Conflicts with the user's `notes/resume-dos-donts.md` | Softened as below, accepted. |
| D4 | Python | Python is available; see §5.3 for invoking it reliably and installing PyYAML. |

**D1: why the relative path is safe.** Both install layouts keep the skills as siblings. A plugin install keeps `skills/career/<skill>/`, and a flat skills directory (`npx skills add`) has `<skills-dir>/<skill>/`. In both, `../maintain-career-record/` resolves from any other skill's folder. The skill's troubleshooting section covers a missing sibling folder ("install the full suite").

**D3: rules as softened.**

| The user's note said | Rule now |
|---|---|
| Every bullet needs "a strictly quantified metric" | Prefer a defensible metric. A bullet may go without one when no defensible number exists, and the gap is recorded. (Amazon and Columbia: not every bullet needs a number; quantification is untested, report §3.4.) |
| Leave out ticket resolution and maintenance tasks | Keep counts, and prompt for an outcome or context to pair with them (report §4.4). |
| A 2–3 line executive summary with a quantified highlight is required | Optional 1–2 line headline (report §4.1). |
| 20–35 words per bullet | Kept as a check that produces a warning, not a hard block; the evidenced rule is at most two lines. |

## 4. Open items

- **Development environment: done (2026-11-07).**
  - Python 3.14.10 and uv 0.13.7 installed with winget (user scope).
  - The repo's `.venv` was created with `uv venv --python 3.14`, and PyYAML 6.0.3 installed into it with `uv pip install`. Nothing was installed globally with pip, and the MSYS2 Python is not used.
  - Scripts and tests in this repo run with `.venv\Scripts\python.exe`.
  - Phase 0 adds a `pyproject.toml` declaring the dependency, so the environment can be rebuilt with `uv sync`.
- **The skills' own runtime convention is not decided yet.** The plan covers the Python the skills use in the user's career repo (§5.3) but not how its PyYAML is installed. To stay consistent with the decision for this repo (no global pip), the skills should tell the user to create a uv virtualenv in their career repo rather than run `pip install` globally. To be confirmed in Phase 0.
- **A stale virtualenv is active in the agent's shell.** The `storefront` virtualenv sets `VIRTUAL_ENV`, and its base Python 3.11 has been uninstalled, so `python` there fails with "No Python at …". The user's own terminal is unaffected. The troubleshooting section of every skill covers this case (§5.3).

## 5. Target architecture

### 5.1 The user's repo (the data)

```
career/
  data/
    profile.yaml            # name, city, email, phone, links, headline candidates
    employment.yaml         # employers of record, roles, titles, periods, client descriptors (industry/scale, NDA flag)
    accomplishments/
      <id>.yaml             # one file per accomplishment (STAR + metrics + evidence + bullets)
    skills.yaml             # skill -> depth, evidence (accomplishment ids)
    education.yaml          # degree, institution, year, exact CGPA/percentage
    projects.yaml           # personal/OSS projects with links
    certifications.yaml
    recognition.yaml
    learning.yaml
    goals.yaml              # aspirations, kept apart from evidence
  NOTES.md                  # append-only log of user statements and changes (kept from today's design)
  CAREER.md                 # GENERATED by render.py; do not edit
  legacy/                   # pre-migration CMD.md, kept until the user deletes it
```

The data files carry `schema_version`, so the scripts can detect old data and migrate it in future.

The chain from a claim back to its source:

```
resume bullet ──► accomplishment <id>.yaml ──► sources: [NOTES.md entry timestamp]
                                       └────► evidence: [PR / design doc / dashboard reference, sanitized]
```

`changelog.json` goes away. Its job (recording what changed) moves into the `NOTES.md` entries, which already list record IDs under their impact heading. That leaves one audit trail instead of two.

### 5.2 Accomplishment record (draft schema)

```yaml
id: 3f9c...                 # from new_id.py
schema_version: 1
status: draft | confirmed | incomplete
employer_id: emp-1          # always the employer of record, never the client (R7)
role_id: role-2
period: {start: 2025-01, end: 2025-03}
title: Short internal title
category: performance        # feature | defect | performance | reliability | refactoring | automation | ...
situation: ...
task: ...                    # the user's own responsibility
actions:                     # the user's own actions, kept apart from the team's (R3)
  - ...
team_context: ...            # what the team did, team size
technologies: [Java, Oracle, C]
outcome: ...
metrics:                     # R5
  - name: p95 latency
    before: 410
    after: 238
    unit: ms
    period: 2025-Q1
    source: monitoring dashboard (sanitized)
    confidence: measured | estimated | relative_only
    user_confirmed: true
evidence:
  - {type: pr | doc | dashboard | ticket | email | recognition, ref: "sanitized description"}
sde2_signals:                # R8
  design_ownership: ...
  alternatives_considered: ...
  reliability_or_scaling: ...
  mentoring: ...
  incident_ownership: ...
interview:                   # R10, R12 (read later by prepare-interview-stories)
  obstacles: ...
  tradeoffs: ...
  what_failed: ...
  lessons: ...
  competencies: [ownership, ambiguity]
bullets:                     # R11: every bullet belongs to one accomplishment
  - id: b-1
    text: ...
    tracks: [backend]
    status: draft | confirmed
similar_to: [<id>]
gaps: [missing metric for ingestion throughput]
follow_up: {due: 2025-06, ask: "post-launch error rate"}   # R4
sources: [2025-03-14T10:02:00+05:30]                       # NOTES.md entries
created: ...
updated: ...
```

### 5.3 Scripts (in `maintain-career-record/scripts/`, Python 3.9+, PyYAML)

| Script | What it does | Requirements |
|---|---|---|
| `init.py` | Creates `career/` from blank templates and never overwrites existing files | — |
| `new_id.py` | Prints a UUID (replaces `genID.py`) | — |
| `validate.py` | Checks the schema (hand-written, no `jsonschema` dependency), uniqueness of IDs, that `similar_to` links are symmetric, that bullet IDs belong to their accomplishment, that every `employer_id` exists, the bullet word-count warning (D3), that each `sources` entry exists in `NOTES.md`, and that metrics carry their `confidence` field. Errors are explicit and say how to fix them. | R2, R5, R7, R11, R31 |
| `render.py` | Regenerates `CAREER.md` from `data/` | — |
| `migrate_cmd.py` | Helps with the one-time migration (§7): splits the legacy `CMD.md` into sections and writes a mapping worksheet | — |

**Every skill workflow ends with:** write the data, run `validate.py`, fix any errors and repeat, then run `render.py`, then append a `NOTES.md` entry. That's the validate-and-repeat feedback loop from the best-practices guide.

**Running Python reliably.** The skills tell the agent to:
1. find a working interpreter by trying `python3 --version`, then `python --version`, then `py -3 --version`, and use the first that reports 3.9 or later;
2. check `import yaml`;
3. if the interpreter fails with "No Python at …" or a similar error, explain that a stale virtualenv is probably active (`VIRTUAL_ENV` is set). Suggest deactivating it, or using the interpreter's full path.

If PyYAML is missing, the agent tells the user how to install it and doesn't attempt to work around it.

### 5.4 This repo

```
skills/career/
  maintain-career-record/
    SKILL.md
    references/schema.md          # field-by-field reference with a table of contents
    references/confidentiality.md
    references/migration.md
    scripts/*.py                  # shared by the whole suite (D1)
    templates/data/*.yaml         # blank files
  capture-work-experience/
    SKILL.md
    references/bullet-rules.md    # research-derived rules (with D3) and worked examples
    references/examples.md        # complete input → record → bullet examples
evals/
  <skill>/triggers.md             # should-trigger and should-not-trigger queries
  <skill>/*.json                  # at least 3 scenarios in the best-practices format
tests/                            # unittest tests for the scripts, with synthetic data only
docs/
  PLAN.md
  research/                       # report and research notes
```

## 6. What each skill must do

### 6.1 `maintain-career-record` (the record owner)

- **Description.** Owns the career record and routes accomplishment capture to `capture-work-experience`. Includes a negative trigger: "for saving a specific piece of work as STAR bullets, use capture-work-experience."
- **Scope.** Profile, employment, skills, education, projects, certifications, recognition, learning, goals, the audit log, the generated view, migration, and record reviews (strongest evidence, gaps, follow-ups that are due).
- **Removed.** Performance-review and promotion material, the 18-section `CMD_FORMAT.md` (replaced by the schema), and the career-narrative and self-analysis sections, which can be regenerated.
- **Kept from today.** The confidentiality rules, the append-only `NOTES.md` with ISO 8601 timestamps, the "never invent facts" rule, and the order of preferred evidence types.
- **New.**
  - Employer-of-record rule (R7).
  - Client descriptors with an NDA flag.
  - Skills must point to the accomplishments that show them (R27 later depends on this).
  - Exact, unrounded CGPA (R32).
  - Quarterly review prompts and follow-up reminders (R1, R4).

### 6.2 `capture-work-experience` (the experience capture)

This rebuild fixes every finding from the earlier evaluation and adds the research requirements.

- **Description.** Rewritten in the third person, with the user's four phrasings as triggers: save this experience, make a resume or STAR bullet, a pasted work paragraph, and an update to an existing entry. It says it feeds the career record.
- **Workflow as a checklist the model copies into its reply:**
  1. **Check the record is set up.** Make sure `career/` exists; if not, set it up through `maintain-career-record`.
  2. **Split.** List each distinct action and result as a separate candidate. Rule: more than one distinct action or result means more than one accomplishment. Word count is only a backup signal. The user confirms the split.
  3. **Interview.** Fill each STAR field with neutral questions (R6). Ask what the user did as opposed to the team (R3), what the baseline was, and what evidence exists. Ask for SDE-2 signals when relevant (R8) and interview-depth fields (R10).
  4. **Classify** each new item against existing records: new, update, or similar. Each has explicit criteria.
  5. **Draft bullets** as outcome, plus measure, plus method, naming the technologies (R19).
  6. **Check each bullet before saving:**
     - every STAR part is filled in or recorded as a gap;
     - every number is in the record with its `confidence`;
     - nothing is in a bullet that isn't in the record (R30);
     - it describes one action;
     - a count is paired with an outcome where one exists (R9);
     - the word-count warning (D3).

     If a check fails, go back to step 2 or 3.
  7. **Save.** Write the YAML, run `validate.py` and fix any errors, run `render.py`, then append a `NOTES.md` entry.
- **Resolved contradiction.** The skill stays on steps 2–3 until the user either supplies the missing piece or explicitly accepts it as a gap. Only then is the record saved with `status: incomplete`.
- **Examples rebuilt.** Every example must pass the skill's own checks, which the old examples didn't. The rebuilt set includes a ticket-count bullet rewritten with an outcome, a client described under NDA, and a mixed paragraph split into separate accomplishments.
- **Also added:** a troubleshooting section (Python or PyYAML missing, stale virtualenv, sibling skill missing, validation errors, two `career/` folders), and the `compatibility` and `metadata.version` frontmatter fields.

### 6.3 Interfaces the future skills will rely on (designed now, built later)

| Future skill | Reads | Requirements it will implement |
|---|---|---|
| `build-resume` | profile, employment, confirmed accomplishments and bullets, skills, education, projects | R14–R22, R30–R34. Single column, text-layer PDF under 2.5 MB, spell-check gate, no personal data, one page by default, optional headline (D3). The template choice (Jake's Resume via LaTeX, or Reactive Resume) is decided when that skill is built. |
| `optimise-resume-for-jd` | the above, plus a JD file | R23–R29: select and reorder only, use exact JD technology names where the record shows them, report unsupported JD requirements as gaps, check consistency with the Naukri and LinkedIn profile. It will follow the user's existing `job-applications/<date>/<company>/` folders (there `jd.md` and `jd.xml` are mixed today; to be standardised then). |
| `prepare-interview-stories` | `accomplishments/*.yaml` `interview` and `sde2_signals` fields | R10–R13 |

## 7. Migrating the user's career-vault

The current data is `career/CMD.md` (18 sections) and `career/NOTES.md`. There's no `EXPERIENCE_DB.md` or `changelog.json`, so the STAR side has nothing to migrate.

The migration is done by the agent and checked by script, because the source is free-form prose that a parser couldn't map reliably.

1. Commit the vault's current state. Move `CMD.md` to `career/legacy/CMD.md`. `NOTES.md` stays exactly as it is, because it's append-only history.
2. Run `init.py`, then `migrate_cmd.py`, which writes a section-to-file worksheet:

| Legacy CMD section | Goes to |
|---|---|
| 1 Metadata, 2 Profile | `profile.yaml` |
| 3 Timeline, 4 Current role | `employment.yaml` (education entries go to `education.yaml`) |
| 5 Master accomplishments + 7 Engineering stories | `accomplishments/<id>.yaml` (stories merged into the matching accomplishment's STAR and `interview` fields) |
| 6 Master resume bullets | `bullets` on the matching accomplishment; bullets that don't match any accomplishment are listed for the user to resolve |
| 8 Quantified metrics | `metrics` on the matching accomplishment, with `confidence` marked from the evidence in `NOTES.md` |
| 9 Technical skills, 10 Capabilities | `skills.yaml` with evidence links |
| 11 Documentation, 12 Recognition | accomplishments or `recognition.yaml` |
| 13 Projects, 14 Learning, 15 Goals | `projects.yaml`, `learning.yaml`, `goals.yaml` |
| 16 Evidence gaps | `gaps` on the matching records |
| 17 Resume extraction notes, 18 Career narrative | dropped (they can be regenerated); still readable in `legacy/` |

3. The agent fills in the YAML and links each record's `sources` to the `NOTES.md` entries. A record is `confirmed` only when `NOTES.md` supports it; everything else is `draft` for the user to review.
4. Run `validate.py` and `render.py`. The user reviews `CAREER.md` against `legacy/CMD.md`. A migration entry is appended to `NOTES.md`.
5. The user deletes `legacy/` when satisfied.
6. Update the career-vault README, which still describes `CMD.md`.

## 8. Phases

| Phase | Work | Done when |
|---|---|---|
| 0. Foundations (**done 2026-11-07**, except confirming the skills' runtime convention in §4) | Install PyYAML (§4). Rename both skill folders and update `name` fields, README, `plugin.json` and cross-references (D2). Update AGENTS.md: suite-install rule (D1), the `docs/`, `evals/` and `tests/` layout, the Python + PyYAML dependency, the data contract. Fix the stale `$id`. Remove real employer names from the samples. | Repo conventions updated; renamed skills still load |
| 1. Data contract | Schema reference, blank templates, `init`, `new_id`, `validate`, `render`, unit tests on synthetic data | Tests pass; validate catches each planted error |
| 2. Record skill | Rewrite `maintain-career-record` as in §6.1 | Its evals pass on Opus and Sonnet |
| 3. Capture skill | Rewrite `capture-work-experience` as in §6.2 | Its evals pass (below) |
| 4. Migration | Run §7 on the career-vault | `validate.py` clean; the user has reviewed and confirmed the result |
| 5. Evaluation | Run the trigger and scenario evals on Opus, Sonnet and Copilot's model; compare against runs without the skill; iterate on what fails | Evals pass on all three; README and plugin version updated |
| Later | `build-resume`, then `optimise-resume-for-jd`, then `prepare-interview-stories` | — |

### Evals for `capture-work-experience` (from the user's observed failures)

1. **A paragraph with no metric.** The skill asks how to get one; it saves as `incomplete` only after the user accepts the gap.
2. **A paragraph covering two pieces of work.** It proposes two accomplishments and waits for the user to confirm.
3. **"Delivered 17+ user stories and resolved 11+ defects…"** It keeps the counts and asks for an outcome and scope, without rejecting them as hollow.
4. **A client named under NDA.** It records the real employer and describes the client by industry and scale.
5. **A new number appears in a draft bullet** that isn't in the record. `validate.py` or the self-check blocks it.

Triggering: the user's four phrasings should trigger `capture-work-experience`. "Update my education" or "add a project" should go to `maintain-career-record`. Unrelated coding requests should trigger neither.

## 9. Requirement traceability

| Requirements | Where they're handled |
|---|---|
| R1–R9 (capture) | `capture-work-experience` workflow and schema; record reviews in `maintain-career-record` (R1, R4) |
| R10–R13 (interview) | Schema `interview` fields now; `prepare-interview-stories` later |
| R14–R22 (resume format) | `build-resume` (later); R20 spell-check gate; R22 education fields now |
| R23–R29 (JD tailoring) | `optimise-resume-for-jd` (later); R27 skill evidence links now |
| R30–R32 (truthfulness) | Schema, `validate.py`, capture self-check, every generator |
| R33–R34 (claims, bias) | Rules in `bullet-rules.md` and the future generators |

---
name: maintain-career-record
description: Maintain an evidence-backed career record and turn it into resume bullets, resumes, performance-review material, promotion evidence, interview stories, and career-development insights. Use when the user discusses career history, engineering work, achievements, skills, goals, resumes, appraisals, promotions, or interviews.
---

# Career Master Document

Maintain a durable, factual record of a software engineer's career and use it to create career materials. This skill is for software engineers across languages, domains, companies, seniority levels, and engineering disciplines.

## Core principles

- Capture evidence of engineering value, not merely activity. Do not equate value with story points, lines of code, hours, meetings, or technology buzzwords.
- Look for delivered functionality, problems solved, complexity, ownership, reliability, maintainability, performance, customer/product impact, developer productivity, knowledge sharing, technical leadership, initiative, and applied learning.
- Never invent facts, metrics, outcomes, ownership, or proficiency. Clearly distinguish confirmed facts, user-reported claims, inferences, goals, and recommendations.
- Keep the Career Master Document comprehensive; derive tailored resumes from it rather than treating it as a resume.
- Be concise, factual, and evidence-oriented. Prefer evidence over adjectives and avoid inflated claims.

## First use and persistent files

The skill package includes `CMD_FORMAT.md` and blank starter files under `templates/`. Treat these as read-only templates; never store the user's personal career information in the installed skill package.

For ongoing tracking, keep three user-owned files together in a location the user chooses:

- `NOTES.md`: append-only source of truth and audit trail.
- `CMD.md`: current comprehensive Career Master Document.
- `CMD_FORMAT.md`: canonical structure and rules.

Default to a `career/` folder in the user's current repository. If these files do not exist, ask where the user wants them created if the available filesystem does not make an appropriate user-owned workspace obvious. Copy the blank templates there before adding personal information. Do not overwrite existing files. If file access or write permission is unavailable, provide the proposed content or changes clearly and ask the user how they want to save them; do not claim a file was updated when it was not.

When the user provides meaningful new career information:

1. Identify new facts, corrections, accomplishments, metrics, skills, evidence, or goals.
2. Check for confidential information and generalize or omit it before it enters personal files.
3. Append a timestamped entry to `NOTES.md`.
4. Update the affected `CMD.md` sections to reflect the latest verified information and preserve the canonical format.
5. Append a second audit entry to `NOTES.md` describing the CMD changes.
6. Identify useful missing evidence, when relevant, without requiring a metric where none naturally exists.

Do not create an audit entry for a general career question that contributes no durable information. `NOTES.md` is append-only: never rewrite or delete historical entries. For corrections, append a new entry identifying what is being corrected and update `CMD.md` to the latest supported version.

Use the user's local timezone when known. Use ISO 8601 timestamps (`YYYY-MM-DDTHH:MM:SS±HH:MM`); if the local offset is unknown, use UTC (`Z`) rather than guessing.

Each audit entry should follow this structure:

```markdown
## YYYY-MM-DDTHH:MM:SS±HH:MM

### Source
User conversation / user-provided document / other permitted source

### New Information
- ...

### CMD Impact
- Added/updated/removed/clarified: ...

### Evidence Status
- Confirmed by user / inferred from user statement / requires verification
```

## Confidentiality

Do not place any of the following in personal career files:

- Source code, credentials, secrets, or internal URLs
- Customer names or confidential customer information
- Proprietary algorithms, architecture details, or internal system identifiers
- Screenshots of internal systems or confidential tickets/documents
- Information whose transfer outside company systems is prohibited

Sanitize work descriptions to a transferable career-level summary. For example, describe “resolved a production defect involving synchronization between persistent and in-memory data layers” rather than naming internal modules, tables, or services. If it is unclear whether a detail is safe to retain, omit it and keep only a generalized description.

## Evidence and accomplishment capture

Prefer evidence in this order:

1. Direct measurement
2. Countable scope
3. Concrete technical scale
4. Adoption or reach
5. Qualitative recognition

Never turn an unmeasured claim into a number. For meaningful work, capture:

- **Work:** What was built, fixed, investigated, or improved?
- **Context:** What problem or requirement existed?
- **Technical scope:** Which sanitized systems, components, languages, data stores, or environments were involved?
- **Difficulty:** Why did it require engineering judgment?
- **Action:** What did the user personally do?
- **Decisions:** What technical decisions or tradeoffs did they make?
- **Outcome:** What changed as a result?
- **Evidence:** What measurement, release, document, recognition, or other evidence supports it?
- **Transferable capability:** What skill does it demonstrate?

Classify work as appropriate: feature delivery, defect/customer issue resolution, investigation/reverse engineering, refactoring, performance, reliability, security, testing, automation, developer productivity, documentation/knowledge sharing, architecture/design, production debugging, technical leadership/mentoring, collaboration, initiative, or learning.

## Resume bullets and interview stories

Maintain candidate resume bullets in `CMD.md`; they are not a final resume. Prefer:

**Action + technical scope + complexity + outcome**

Make each bullet factual, concise, evidence-backed, transferable, and free of unnecessary proprietary details. Avoid “Responsible for,” “Worked on,” unsupported impact claims, inflated leadership language, excessive jargon, and repetitive use of “legacy.” Mention older technologies only when technically relevant.

For significant accomplishments, maintain an interview-ready story covering:

1. Situation
2. Task
3. Investigation and reasoning
4. Actions
5. Technical decisions
6. Obstacles
7. Result
8. Lessons learned

Show judgment, not merely effort.

## Goals, missing evidence, and career analysis

Keep career goals separate from evidence. Goals can cover target roles/domains, compensation, technical depth, leadership, and learning; label aspirations as goals, never as current accomplishments.

When useful, suggest missing evidence such as release/version, affected component count, before/after performance, adoption, user/developer reach, customer impact, or recognition. Do not pressure the user to invent or estimate metrics.

When giving career advice, distinguish engineering capability, employability, compensation potential, performance in the current organization, and long-term development. Do not assume one activity optimizes all of them.

For periodic reviews, summarize strongest evidence, recurring strengths, growth areas, evidence gaps, resume-ready accomplishments, interview-ready stories, and changes in goals. Look for patterns over time rather than judging a career from a single event.

## Canonical document structure

Follow `CMD_FORMAT.md` for the full schema. It includes document metadata, professional profile, career timeline, current-role context, master accomplishments, candidate resume bullets, engineering stories, quantified metrics, technical skills, transferable capabilities, documentation contributions, recognition, projects, learning, career goals, evidence gaps, resume extraction notes, and career narrative.

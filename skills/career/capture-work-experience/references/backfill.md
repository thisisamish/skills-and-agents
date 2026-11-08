# Backfilling past work from an inventory

Use this when the user has a lot of uncaptured work: a new record, months or years behind, or a decision to rebuild the record from scratch. Capturing one remembered item at a time misses work and over-weights what's recent. Listing everything first, then capturing row by row, doesn't.

## Contents

1. Phase 0: build the inventory (the user)
2. Phase 1: suggest metrics (the agent)
3. Phase 2: collect metrics (the user)
4. Phase 3: capture (together)
5. Done when

Copy this checklist into your reply and tick it off:

```
- [ ] 0. Inventory created and filled by the user
- [ ] 1. Metrics suggested for each row; missing fields pointed out
- [ ] 2. The user has collected metrics or marked them [n/a]
- [ ] 3. Rows captured bucket by bucket (main workflow, steps 1–7)
- [ ] 4. Every row captured, merged or skipped; record validates
```

## Phase 0: build the inventory

1. Copy `templates/inventory.md` (this skill's folder) to `career/inventory.md`, unless the user already keeps an inventory elsewhere. In that case, use theirs and map its columns to the ones below.
2. Explain the four buckets and the question that sorts them, **who started it?**:
   - assigned work (with the bugs found in it)
   - production and customer issues
   - self-initiated work
   - help given to others

   Rows in the last two are why the inventory exists, because they're on no board. Prompt for them: "Who did you help? What did you start that nobody asked for? Which questions do people bring to you?"
3. Ground rules for the user:
   - **List first, judge later.**
   - Leave unknown dates blank.
   - Use roles, not names.
   - Note figures in summarised form, and only what the employer's policy allows: no exports, code or client names.
4. The user fills it in, often over several sessions. If the repository uses git, suggest committing after each session. Phase 0 ends when the user says the inventory is ready.

## Phase 1: suggest metrics

For every row without a `[have]` metric:

1. Suggest the one to three most persuasive measures for that kind of work, and where the user could realistically find each one: ticket or story history, defect tracker, git or PR history, release notes, logs, dashboards, their own notes. Use the measure families in [bullet-rules.md](bullet-rules.md). For help given, think about effect on others: people onboarded, time until a new joiner's first change, questions that turned into a guide. Don't force a number where a clear qualitative outcome is stronger.
2. Write the suggestions into the row's Impact cell marked `[ai]`, keeping what the user wrote. Use Details for anything long.
3. List the rows missing **When**, **Context / problem** or **My part vs team**. Capture needs these most.
4. Hand back to the user for Phase 2.

## Phase 2: collect metrics

The user turns each `[ai]` into `[have]` (with its source) or `[n/a]`. Don't estimate on their behalf. An estimate is theirs to make, with a stated method, and is recorded as `confidence: estimated`.

## Phase 3: capture

Work bucket by bucket: assigned work, then production and customer issues, then self-initiated work, then help given, then recognition. Ask before moving to the next bucket.

**Shape first.** Before capturing, propose how rows become accomplishments and get the user's agreement:

| Rows | Usual shape |
|---|---|
| An assigned item and its `-B` bugs | One accomplishment. The bugs become actions, obstacles or metrics. Split a bug out only if it was a substantial investigation of its own. |
| Small production or customer issues | Grouped into one accomplishment ("resolved N customer-raised defects across …"). Long or critical investigations stand alone. |
| A self-initiated item | One accomplishment each, unless several are really one effort. |
| Help given | One theme accomplishment per row, with its specific instances (see "Recurring work" in SKILL.md). |

**Then run the main workflow** (SKILL.md steps 1–7) for each accomplishment, using the row as the user's description. The interview still applies: the row is a starting point, not confirmed facts.

**Column mapping:**

| Inventory column | Record field |
|---|---|
| Bucket | `origin`: assigned work and production issues → `assigned` (unless the user picked it up unasked); self-initiated → `self_initiated`; help given → `requested_by_others` |
| What I did | `actions`, `title` |
| Context / problem | `situation` |
| When | `period` |
| My part vs team | `task`, `team_context` |
| Tech used | `technologies`, plus evidence links in `skills.yaml` |
| Impact | `outcome`, `metrics` (`[have]` → `measured` or `reported` by source; `[n/a]` → a gap the user accepts) |
| Evidence | `evidence` |
| Kind: Technical | `category` that fits the work (feature, defect, investigation, refactoring, performance…) |
| Kind: Documentation | `category: documentation` when it's the main work, otherwise an action |
| Kind: Behavioural:tag | `interview.competencies`, plus the matching `sde2_signals` field when it really happened |

**After each accomplishment:**
- Note in the inventory's Details section, under the row IDs, that they were captured as `<id>`.
- Mention the row IDs in the NOTES.md entry.
- If git is in use, offer to commit.

**Recognition** rows go to `recognition.yaml` through maintain-career-record, linked to the related accomplishments.

**After each bucket:**
- Validate and render.
- Tell the user how many rows became how many accomplishments, and which gaps remain.

## Done when

- Every row is captured, merged into another accomplishment, or explicitly skipped by the user. The Details section says which.
- `validate.py` reports 0 errors, and the warnings have been reviewed with the user.
- The user knows what's still open: gaps, follow-ups, and unconfirmed bullets.
- The inventory stays in the repository as history. From now on, new work goes in `career/log.md`.

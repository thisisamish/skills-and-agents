# Worked examples

All names, companies and figures here are made up.

## Contents

1. Splitting a description that mixes two pieces of work
2. Keeping counts and finding the outcome
3. Client work under NDA
4. A saved record

## 1. Splitting a description that mixes two pieces of work

**User:** "Operators were drowning in subsystem logs on the old tabular dashboard, so I designed a new dashboard in Java with C backend services on Oracle, and also optimised the insert-heavy ingestion with batching and retries so it handles up to 300k log entries every 15 minutes. About 30% of the log traffic now goes to the new dashboard."

**Split:** there are two actions, each with its own result:
1. Designed and integrated a dedicated dashboard for critical logs. Result: about 30% of log traffic redirected, so operators can see critical events.
2. Optimised the ingestion pipeline with batching and retries. Result: unknown so far. "Handles up to 300k entries every 15 minutes" is the load it has to sustain (scale), not the improvement.

**Agent:** "I see two pieces of work here: (1) the new dashboard and (2) the ingestion optimisation. Shall I capture them separately?" Then interview for each. For (2): "What was the throughput or failure rate before batching, and after? Where could you find it: ingestion logs, a DB monitoring view, a load test?"

If the user can't get the before-and-after figures and agrees to leave them as a gap, record (2) as `incomplete` with the gap "throughput or failure rate before and after the optimisation". Its bullet states the scale and method without inventing an improvement:

> Optimised a C and Oracle log ingestion pipeline with batching and retries to sustain up to 300k log entries every 15 minutes for an operator monitoring system.

(26 words; every number is in the record.)

## 2. Keeping counts and finding the outcome

**User:** "Add this: Delivered 17+ user stories and resolved 11+ defects across C/C++, Java, SQL and Bash in two mission-critical features of an enterprise energy management product."

**Don't** call the counts hollow or delete them. They're real. **Do** ask what changed:
- "Were the defects customer-reported or found internally? What happened because they were fixed: a release unblocked, an SLA met, fewer escalations?"
- "What did the two features let users do? Who used them?"
- "Which parts were yours, as opposed to the team's?"

Suppose the user confirms that the 11 defects were customer-reported and release-blocking, and that both features shipped in the quarterly release. The bullet can then be:

> Resolved 11 customer-reported, release-blocking defects and delivered 17 user stories in C++ and Java for two features of an energy management product, shipping both in its quarterly release.

(29 words.) If the user can't say what changed, keep the counts, record a gap ("effect of the defect fixes"), and save the record as `incomplete`.

## 3. Client work under NDA

**User:** "At Example Corp I worked on the BigBank account-opening portal…"

- The employer is Example Corp (from `employment.yaml`). The work goes under the user's role there, with an engagement such as `client_descriptor: "Tier-1 retail banking platform"`, `nda: true`.
- The record and bullets never contain "BigBank". If the user says the client name is public and allowed, they can add it themselves later.
- The bullet names the domain and scale: "…for a Tier-1 retail banking platform serving 2 million customers…", but only if the user gave that scale.

## 4. A saved record

`career/data/accomplishments/3f9c2b1e-7d4a-4c1e-9b2f-5a6d7e8f9012.yaml`:

```yaml
schema_version: 1
id: 3f9c2b1e-7d4a-4c1e-9b2f-5a6d7e8f9012
status: confirmed
role_id: role-1
engagement_id: eng-1
period: {start: "2025-01", end: "2025-03"}
title: Cut settlement report latency
category: performance
origin: assigned
situation: Settlement reports for the banking client's operations team took too long to use interactively.
task: Make the report endpoint fast enough for interactive use without changing its output.
actions:
  - Profiled the slowest queries and added two PostgreSQL composite indexes.
  - Rewrote two report queries to avoid full-table scans and verified output against the old version.
team_context: Team of 6; I owned the reporting service; a teammate reviewed the index changes.
scale: About 12,000 report requests per day.
technologies: [Java, Spring Boot, PostgreSQL]
outcome: Operations staff now run reports interactively instead of scheduling them overnight.
metrics:
  - name: p95 latency
    before: "410"
    after: "238"
    unit: ms
    period: "2025-Q1"
    source: service monitoring dashboard
    confidence: measured
    user_confirmed: true
evidence:
  - {type: dashboard, ref: "latency panel of the reporting service, before and after the release"}
  - {type: pr, ref: "index and query changes, reviewed by a teammate"}
sde2_signals:
  design_ownership: ""
  alternatives_considered: "Considered caching report results; rejected because reports must reflect same-day settlements."
  reliability_or_scaling: ""
  mentoring: ""
  incident_ownership: ""
interview:
  obstacles: "Report output had to stay byte-identical for downstream reconciliation."
  tradeoffs: "Indexes slowed nightly bulk inserts slightly; measured and accepted."
  what_failed: "The first index choice didn't help the second query."
  lessons: "Profile before tuning; check write-path cost of new indexes."
  competencies: [ownership, problem_solving]
bullets:
  - id: b-1
    text: Reduced p95 latency of a settlement reporting API from 410 ms to 238 ms by adding PostgreSQL composite indexes and rewriting queries across 12,000 daily requests.
    tracks: [backend]
    status: confirmed
similar_to: []
gaps: []
follow_up: null
sources: ["2025-03-14T10:02:00+05:30"]
created: "2025-03-14"
updated: "2025-03-14"
```

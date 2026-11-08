# Resume bullet rules

These rules come from employer guidance (Google, Amazon), university career centres and ATS vendor documentation. Screeners skim fast but read the whole resume, spend the most time on the experience section, and penalise vague or error-filled content. Generic polished text is cheap; specific, checkable detail is what stands out.

## Shape

**Action verb + outcome + measure + method, naming the technologies.** Google's version: "Accomplished X, as measured by Y, by doing Z". The order can vary; all three parts should be there.

- Start with a strong past-tense verb: built, designed, reduced, migrated, automated, diagnosed, led. Use present tense only for ongoing work.
- Name exact technologies (`PostgreSQL`, `Spring Boot`, `AWS Lambda`), as recruiters search for these literal terms.
- At most two lines on a page, usually 20–35 words.
- One piece of work per bullet.
- No "I", "we", "responsible for", "worked on", "helped with" or "involved in".
- No unexplained internal names or acronyms; describe what the thing is.

## Measures

Prefer a number the user can defend in an interview. Good measures for engineers:

| Kind | Examples |
|---|---|
| Speed | p95/p99 latency, response time, build or deploy time, batch duration |
| Throughput and scale | requests per second or day, records processed, data volume, users, modules |
| Reliability | uptime, error rate, failed transactions, incidents, MTTR |
| Cost | cloud spend, licence cost, hardware, hours saved |
| Quality | defects escaped, test coverage, flaky tests removed |
| Adoption | teams, users or services adopting a tool or practice |
| Counts | tickets closed, stories delivered, defects fixed, documents written |

- **Show before and after** when you have both: "from 410 ms to 238 ms".
- **Under NDA,** use relative figures ("2× faster", "cut by a third") if the user may not share absolutes. Record them as `confidence: relative_only`.
- **An estimate** must be the user's, with a stated method. Record it as `confidence: estimated`, and phrase it honestly ("about", "roughly") if the user prefers.
- **No defensible number?** Write the concrete outcome instead ("enabled operations staff to run reports interactively") and record the gap. Not every bullet needs a number.

## Counts

A count such as "resolved 11 defects" is a truthful measure of scope; don't delete or disparage it. It is stronger with what changed or with context:

- Weaker: "Resolved 11 defects and delivered 17 user stories in an energy management product."
- Stronger: "Resolved 11 customer-reported defects in C++ and Java ahead of a utility client's release, clearing the release-blocking backlog for an energy management product." This works only if the user confirmed those facts.

When a draft lists activity without saying what changed, ask the user: "What was different because of this?"

## For engineers moving from services to product companies

Product companies look for ownership, design judgement and scale. When the record supports it:

- Lead with what the user owned or decided, not with client communication or routine duties.
- Name design decisions, trade-offs and reliability or scaling choices.
- State scale (traffic, data volume, users) so the work isn't read as small maintenance.
- Describe the client by industry and scale ("Tier-1 retail banking platform"), and the employer by its real name.

Only claim SDE-2-style signals (design ownership, mentoring, incident ownership) when the record shows them.

## Presenting work for a target role

The record holds the full facts; bullets choose what to emphasise. A bullet is drafted for a track (`tracks`: backend, frontend, full_stack, platform, data…). When `goals.yaml` names target roles, draft that track's variant first.

- **Describe the system by its scale and complexity, not its age.** "A globally deployed, multi-node C and Java platform with custom messaging" and "a 35-year-old legacy codebase" can describe the same system. The first says what the work demanded, so use it when both are true.
- **Leaving out is a choice; misrepresenting is not.** A bullet may skip a technology that doesn't help the target role, or describe it neutrally ("a Java desktop client"). It must never imply a technology, scale, role or result the record doesn't show. Everything on the page has to survive "tell me more about that".
- **Broad claims need specific evidence.** "Distributed systems", "system design" or "high-performance" only where the record shows the user's own work in them (system context, `design_ownership`, metrics).
- **Help given and self-initiated work** usually earn one bullet, or half of one, beside the technical bullets ("onboarded four engineers to…"). Their main use is interview stories.

There is no published evidence on how screeners react to particular technology names; this guidance rests on accuracy and on what product-company postings ask for (ownership, design, scale).

## Quick examples (weak → stronger)

All figures in these examples are made up and are only meant to show the shape.

| Weak | Stronger |
|---|---|
| Responsible for backend API performance and database queries. | Reduced p95 latency of a settlement reporting API from 410 ms to 238 ms by adding PostgreSQL composite indexes and rewriting queries across 12,000 daily requests. |
| Worked on migrating the application to microservices. | Migrated a monolithic payment service to 18 Spring Boot microservices on AWS EKS, raising monthly availability from 99.2% to 99.95% for checkout traffic. |
| Automated the testing and deployment process. | Automated build, test and deployment for 6 Java services with GitHub Actions, cutting release preparation from 2 days to 3 hours per sprint. |

## Things never to tell the user as fact

Popular claims such as "75% of resumes are rejected by ATS" or "recruiters look for 6 seconds" come from companies selling resume services and have no published method. Don't repeat them. Formatting matters because parsers can garble layouts, not because of a hidden auto-reject score.

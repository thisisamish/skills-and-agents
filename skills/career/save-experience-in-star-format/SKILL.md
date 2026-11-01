---
name: save-experience-in-star-format
description: "Maintain a database of a software engineer's work experience in STAR format (Situation, Task, Action, Result). Use it when user asks to save work experience in bullet point(s)."
---

The task is to have a living document of everything the user has worked on in his software engineering career categorised by the organisation and saved in STAR (Situation, Task, Action, Result) format.

The database is a simple markdown file and its format has been provided to you in `EXPERIENCE_DB_FORMAT.md` (in this skill's folder). Never store user data inside the skill's folder. The database lives in the user's current repository at `career/EXPERIENCE_DB.md`; if the repository already keeps career files in another folder, use that folder instead, and if it is unclear, ask the user. There should be only one database per repository. If the file exists, add new information to it. If it doesn't exist, let the user know and create one. Ask them the name of the person for whom this DB is being created. Put that in <SWE_NAME>. Every piece of information added to `EXPERIENCE_DB.md` should be recorded in `changelog.json` next to it, for history and audit purposes. The schema of the changelog has been provided to you in `changelog_schema.json` (in this skill's folder). If the file exists, add new information to it. If it doesn't exist, let the user know and create one.

## Process

### 1. Gain complete information

Whatever the user described as having done in their career should have the following information:

1. The organisation where they did this work
2. Situation - the context behind the work
3. Task - what you were required to achieve
4. Action - what you actually did (keywords, tech stack they used)
5. Result - what was the outcome (metrics)
   If the user has not provided any of these, ask them for the complete information. Do not move forward until you have received all the information. NEVER fabricate details.

The user might give you a paragraph which might conflate multiple tasks that they did. De-tangle them and provide a clean breakdown with each individual tasks listed. Present the breakdown to the user and ask them to provide their confirmation. Do not move forward until the user says so.

### 2. Build the resume bullet points

- Every bullet point must be constructed using the STAR method (Situation, Task, Action, Result).
- The bullet must lead with a strong action verb, followed by the specific technology utilized, the scale of the system engineered, and a strictly quantified metric. Key metrics include throughput (Requests Per Second/QPS), latency reduction (in milliseconds or percentiles like p95/p99), cloud cost savings, uptime reliability (e.g., achieving 99.99% availability), and incident diagnosis time (MTTR).
- The bullet must be within 20 - 35 words. If the bullet point is longer than 35 words, it is an indication that it is conflating multiple tasks into one bullet point. Break it down into multiple bullet points and ask the user for confirmation.
- Below is a table showcasing a weak, task-based formulation of a bullet point and the corresponding optimized, impact-driven formulation using STAR method:
  | Weak, Task-Based Formulation | Optimized, Impact-Driven Formulation |
  | ---------------------------- | ------------------------------------ |
  | Responsible for backend API performance and database queries. | Engineered scalable REST APIs using Node.js and PostgreSQL, optimizing query execution to reduce p95 latency by 42% (410ms to 238ms) across 12M daily requests. |
  | Worked on migrating the application to microservices for the client. | Led the architectural migration of a monolithic payment service to 18 distinct microservices deployed on AWS EKS, improving system reliability from 99.2% to 99.95%. |
  | Reduced AWS costs for the company by managing servers. | Re-architected batch processing jobs to utilize AWS Spot Instances and right-sized EC2 instances, reducing monthly cloud infrastructure expenditure by 31% ($38K/month). |
  | Automated the testing and deployment process. | Implemented an idempotent retry and dead-letter pipeline, reducing failed payment writes by 88% and recovering $2.1M in stuck transactions. |

### 3. Save to the experience database

When each resume bullet point has been created, you should store them in the experience database present at `career/EXPERIENCE_DB.md` (or the folder chosen above) and record a changelog for history and audit purposes. If the file does not exist, create it.
It is possible that the bullet points you have just created might be updates on what already exists in the experience database. In such a case, update the existing bullet points in the database.
Another situation might be that the bullet points you just created are semantically similar to what already exists in the database. In such a situation, store the new bullet point as a new item in the database and mark it as being similar by mentioning the similar bullet points' item ID in the "Similar To" column of the new bullet point. Mention the new bullet point's item ID in the "Similar To" column of the already existing similar bullet points.
For a new bullet point, generate itemID using the `genID.py` Python script in this skill's folder.

# How to handle incomplete bullet points

It might happen that the user might not a particular information about a bullet point. For example, the user mentions that they optimized the SQL queries to use indexes but they do not have a metric of how much improvement this generated. In such a situation, advise them on how to obtain such metrics. Provide them with information about standard methods of obtaining metrics in the situation particular to the bullet point in question. The same applies to situation, task, and action part of the bullet point.
If the user is not able to provide information even after this, accept it as a gap, notify them and mark it as incomplete in the database in "Incomplete" column. Refer to EXPERIENCE_DB_FORMAT.md for the format.

# How to break down a task into multiple bullet points

Here is an example:

- **Situation:** Operators were overwhelmed by logs from a subsystem flooding an existing tabular dashboard, reducing visibility into critical events.
- **Task:** Design and integrate a new dashboard to isolate critical logs and improve operator visibility.
- **Action:** Designed and integrated a new tabular dashboard using Java for the frontend and C-based backend services over Oracle-backed infrastructure; optimized insert-heavy write paths with batching and retries to sustain upto 300k log entries every 15 minutes.
- **Result:** Redirected over 30% of log traffic to the new dashboard, improving operator visibility into critical events and reducing dashboard overload.
- **Malformed bullet point:** Redirected critical subsystem logs using Java-based dashboarding and optimized C/Oracle-backed ingestion, routing 30% of prior log volume to a dedicated tabular dashboard and improving operator visibility across high-volume telemetry.

Here, the action is two-fold: 1) designed and integrated a new dashboard, and 2) optimized the ingestion pipeline. This should be broken down into two bullet points. The Malformed bullet point combines both into one, leading to a long and unclear bullet point.
Another problem here is that the "optimization of ingestion pipeline" has incomplete data. The user should provide a metric of how optimized the pipeline became after his action. The "sustain upto 300k log entries every 15 minutes" should be a part of Task, not Result.

- **Improved bullet point 1:**
  - **Situation:** Operators were overwhelmed by logs from a subsystem flooding an existing tabular dashboard, reducing visibility into critical events.
  - **Task:** Design and integrate a new dashboard to isolate critical logs and improve operator visibility.
  - **Action:** Designed and integrated a new tabular dashboard using Java for the frontend and C-based backend services over Oracle-backed infrastructure.
  - **Result:** Redirected over 30% of log traffic to the new dashboard, improving operator visibility into critical events and reducing dashboard overload.
  - **Resume Bullet Point (in STAR format):** Designed and integrated a new tabular dashboard using Java, C and Oracle, routing 30% of prior high-volume telemetry and improving operator visibility.

- **Improved bullet point 2:**
  - **Situation:** The log ingestion pipeline was not optimized to handle high-volume telemetry, leading to performance issues.
  - **Task:** Optimize the ingestion pipeline to handle high-volume telemetry.
  - **Action:** Optimized C and Oracle based ingestion pipeline with batching and retries to sustain up to 300k log entries every 15 minutes.
  - **Result:** Improved performance by 50%.
  - **Resume Bullet Point (in STAR format):** Optimized a high-volume (up to 300k log entries every 15 minutes) C and Oracle based log ingestion pipeline with batching and retries, improving performance by 50%.

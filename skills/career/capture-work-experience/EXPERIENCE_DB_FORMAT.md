# <SWE_NAME>'s Experience DB

# Format

Experience DB is a table with the following columns:
| S. No. | Incomplete | Associated With | Resume Bullet Point (in STAR format) | Situation | Task | Action | Result | Similar To | itemID |
| ------ | ---------- | ---------- | ---------- | ----- | -------- | ---------- | ---------- | -------- | ----- |

# Column's Datatypes

1. S. No.: Number starting from 1, incremented by 1 per new row
2. Incomplete: Y/N, whether the entry is complete in STAR format or not
3. Associated With: Organisation where this bullet point is from
4. Resume Bullet Point (in STAR format): Fully formed resume bullet point ready to be used. Must be within 20 - 35 words.
5. Situation: "Situation" from Resume Bullet Point
6. Task: "Task" from Resume Bullet Point
7. Action: "Action" from Resume Bullet Point
8. Result: "Result" from Resume Bullet Point
9. Similar To: itemID of Resume Buller Points that are similar to this row
10. itemID: generated UUID uniquely identifying the row

# A Sample Experience DB

| S. No. | Incomplete | Associated With           | Resume Bullet Point (in STAR format)                                                                                                                                 | Situation                                         | Task                                                     | Action                                                                                                            | Result                                                                               | Similar To | itemID                               |
| ------ | ---------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------- | ------------------------------------ |
| 1      | N          | Example Corp Pvt. Ltd.    | Led the architectural migration of a monolithic payment service to 18 distinct microservices deployed on AWS EKS, improving system reliability from 99.2% to 99.95%. | A monolith that was becoming harder to maintain   | Architectural migration of the monolith to microservices | Identification of split boundaries in the monolith and migration to 18 distinct microservices deployed on AWS EKS | System reliability improved from 99.2% to 99.95%                                     |            | 905d190a-dd86-44e8-ba57-84207dc477ca |
| 2      | N          | Sample Tech Pvt. Ltd.     | Implemented an idempotent retry and dead-letter pipeline, reducing failed payment writes by 88% and recovering $2.1M in stuck transactions.                          | Frequent failure of payments leading to UX issues | Reduction of payment failure rate                        | Implementation of an idempotent retry and dead-letter pipeline                                                    | Reduction of failed payment writes by 88% and recovery of $2.1M in stuck transations |            | c07d7694-187f-4dd3-8ee3-5194c4cea1cf |

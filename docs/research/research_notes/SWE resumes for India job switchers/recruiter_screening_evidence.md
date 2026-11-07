# Recruiter and hiring-manager resume screening: what the evidence says (focus: software engineering, India job switchers)

**How to read these notes**

- **Evidence-strength labels**
  - **STRONG**: peer-reviewed, large sample or replicated, with real or realistic screeners.
  - **MODERATE**: peer-reviewed but one study, a small or student sample, or lab vignettes.
  - **WEAK**: commercial, unpublished or unreplicated work, or practitioner opinion.
  - **LOW (community)**: forums.
- **Verification tags**
  - **[verified]**: I read the primary text or abstract in this session.
  - **[biblio-verified]**: I confirmed the citation details in this session but did not re-read the findings; the findings come from my prior knowledge of the paper and need a quick check before anyone quotes figures.
- **Geography**: unless stated otherwise, findings come from the US or Europe. Transferability to India is discussed under Inferences.
- **Source policy**: I used no resume-builder or coaching-company source as evidence. When a well-known statistic started at such a company, the notes say where it came from.

## Q1. How long do screeners spend on a resume, and where does their attention go?

### Takeaway
The famous "6 seconds" (2012) and "7.4 seconds" (2018) figures come from Ladders, a commercial job-board and career-services company. Neither study was published with a full method or peer review. The only peer-reviewed eye-tracking resume study I found (Lahey & Oxley, JPAM 2021) measured about **16 seconds per resume** for a clerical job. In that study, screeners read the whole resume, and the employment-history section got the most viewing time. Screening time is short whichever source you believe, but "6 seconds" is a commercial figure, not a scientific constant.

### Cited Findings
- **Ladders (2012), "Keeping an Eye on Recruiter Behavior"**: about 6 seconds on the first screen of a resume. Ladders is a for-profit job-board and career-services firm that sells to job seekers, so treat this as commercially motivated. The sample size was small (reported as about 30 recruiters), and the method was not published in detail. **WEAK.** Copy of the PDF: [CSU Global hosted copy](https://csuglobal.edu/sites/default/files/blog-files/theladders-eyetracking-studyc2.pdf).
- **Ladders (2018) update**: average first screen of about 7.4 seconds. The study had two parts: a timed sorting task (recruiters were not told they were being timed) and a lab eye-tracking task. Recruiters reportedly looked mostly at job titles, section headers and subheadings, and disliked resumes with no clear section or job headers and text that "didn't flow". The release never published a headcount or recruiter profile. **WEAK.** [HR Dive summary](https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/); critique in [ERE, "Is the 6-second resume scan a myth?"](https://www.ere.net/articles/is-the-6-second-resume-scan-a-myth). ERE reports that critics see the study as essentially a how-to guide, and that many viral "resume heatmaps" are mouse-tracking data, not Ladders eye-tracking.
- **Lahey, J. N., & Oxley, D. R. (2021). Discrimination at the intersection of age, race, and gender: Evidence from an eye-tracking experiment.** *Journal of Policy Analysis and Management*, 40(4), 1083–1119. DOI: 10.1002/pam.22281. Working paper: NBER w25357. [NBER PDF](https://www.nber.org/papers/w25357.pdf); [RePEc record](https://econpapers.repec.org/RePEc:wly:jpamgt:v:40:y:2021:i:4:p:1083-1119). **MODERATE** (peer-reviewed lab study with student screeners). **[verified: NBER working-paper text]**
  - **Participants and task:** 152 participants (MBA, MPA, HR and business students; 24% had hiring experience and 11% had HR experience). Each rated 40 randomised resumes for a clerical job, for 5,960 usable resumes in total.
  - **Viewing time:** mean **16.24 s per resume (SD 10.17 s)**. The authors note this is "slightly higher than, but comparable with, the estimate of 15 seconds often given by human resource professionals when asked" (citing Lahey 2008).
  - **Where attention went:** screeners "do look at the entire resume for each applicant and do not stop reading after seeing a name or graduation date". By area of interest, employment history got the most viewing time: about 4.87 s mean in the working-paper Table 1. The column alignment in the extracted table is slightly ambiguous, so check this figure against the published table. Name and graduation-year areas got well under 1 s.
  - **Effect of resume content on time:** resumes with signals that stood out (for example, computer training on resumes of younger Black applicants) drew about 10 more seconds. Unusual profiles (applicants aged 70+) were viewed longer.
  - **Hiring experience:** having hiring experience did not change the main results. A smaller companion study with HR managers broadly replicated the patterns.
- **Bartoš, Bauer, Chytilová & Matějka (2016), "Attention discrimination", *American Economic Review* 106(6), 1437–1475** (DOI 10.1257/aer.20140571). Lahey & Oxley cite it for comparable time-on-resume results. In a Czech field setting, employers chose whether to open each CV and spent less effort reading CVs from disfavoured minority applicants. **STRONG** (field experiment, top journal). **[biblio-verified via Lahey & Oxley's citation]**

### Inferences
- The best peer-reviewed estimate (about 15–16 s) is about twice the Ladders figure. Both describe a fast first pass in which job titles, employers and section structure carry most of the signal. In practice: put the most job-relevant information (current title, employer, strongest tech-stack evidence) where a quick skim of the top half and the left-aligned headings will catch it.
- Lahey & Oxley show that screeners do read the whole resume and that the experience section gets the most attention. For a switcher with 2–3 years of experience, the content of the experience bullets is therefore where the screening decision is mostly made.
- Lahey & Oxley also found that how long screeners read depends on the applicant's group (attention discrimination). This suggests that applicants from employer types the screener sees less often (for example, IT services rather than product companies, in a product-company screen) may get less reading time. That is an inference by analogy, not a tested finding.

### Gaps
- I found no peer-reviewed eye-tracking study of resume screening for **software engineering** roles, and none conducted in **India**.
- No independent replication of Ladders exists. Its sample size and recruiter profile were never disclosed.
- Real recruiters screening inside ATS dashboards (which show parsed fields, filters and keyword search) may behave differently from lab participants reading a full PDF. I found no peer-reviewed study of that setting.

## Q2. What does peer-reviewed research say about resume length, layout and structure, readability, typos, quantified achievements, and the signalling value of content?

### Takeaway
The best evidence concerns **spelling errors**: a large recruiter vignette study and earlier replications all show clear penalties. There is **moderate** evidence that recruiters read education, work experience and extracurriculars as signals of ability and personality, and that relevant work experience and job-related content raise interview chances. Evidence on **layout** and **length** is thin: a few older studies, mostly about accounting or general graduates. I found **no peer-reviewed evidence** that quantified bullets ("reduced latency by 30%") improve callbacks, although the idea is consistent with the signalling literature.

### Cited Findings

**Typos and spelling errors (best-evidenced format feature)**
- **Sterkens, P., Caers, R., De Couck, M., Van Driessche, V., Geamanu, M., & Baert, S. (2023). Costly mistakes: Why and when spelling errors in resumes jeopardise interview chances.** *PLOS ONE*, 18(4), e0283280. DOI: 10.1371/journal.pone.0283280. [Full text](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283280). Also IZA DP 14614. **STRONG–MODERATE** (large sample of real recruiters, but hypothetical vignette decisions). **[verified]**
  - **Design:** Belgium (Flanders), data collected in April 2020. 445 HR professionals rated 1,335 vignette resumes of graduate applicants across 8 vacancies, ranging from production worker to air-traffic controller and HR manager.
  - **Main result:** relative to an error-free resume, **5 spelling errors cut interview probability by 18.5 percentage points** and **2 errors by 7.3 points**. The penalty for 5 errors was 12.2 points in the white-collar subsample.
  - **Mechanism:** about half of the penalty runs through lower perceived **mental ability (about 32%)**, **conscientiousness (about 12%)** and **interpersonal skills (about 9%)**.
  - **Moderators:** penalties were larger for jobs with heavy written-communication demands and for recruiters who rate themselves as sensitive to language. Penalties were smaller for jobs with higher educational requirements. Only spelling errors were tested, not grammar errors.
- **van Toorenburg, M., Oostrom, J. K., & Pollet, T. V. (2015). What a difference your e-mail makes: Effects of informal e-mail addresses in online résumé screening.** *Cyberpsychology, Behavior, and Social Networking*, 18(3), 135–140 (DOI 10.1089/cyber.2014.0542). Sterkens et al. cite it as reporting a **13.7-point drop in hireability for 5 spelling errors** among HR specialists, and it also found penalties for informal e-mail addresses. **MODERATE.** **[cited via Sterkens et al.; verified there]**
- **Martin-Lacroux, C., & Lacroux, A. (2017). Do employers forgive applicants' bad spelling in résumés?** *Business and Professional Communication Quarterly*, 80(3), 321–335 (DOI 10.1177/2329490616671310). French recruiters judged applications with spelling errors more harshly, and recruiters' own spelling ability moderated the penalty. **MODERATE.** **[cited via Sterkens et al.]**
- **Charney, D. H., & Rayman, J. (1989). The role of writing quality in effective student résumés.** *Journal of Business and Technical Communication*, 3(1), 36–53. Also **Charney, Rayman & Ferreira-Buckley (1992)**, *Journal of Business and Technical Communication*, 6(1), 38–74. Early evidence that recruiters weigh writing quality and mechanical errors. **MODERATE (older).** **[cited via Sterkens et al.]**

**Content signals: education, experience, activities**
- **Cole, M. S., Rubin, R. S., Feild, H. S., & Giles, W. F. (2007). Recruiters' perceptions and use of applicant résumé information: Screening the recent graduate.** *Applied Psychology: An International Review*, 56(2), 319–343. DOI: 10.1111/j.1464-0597.2007.00288.x. [DePaul record](https://scholars.depaul.edu/en/publications/recruiters-perceptions-and-use-of-applicant-r%C3%A9sum%C3%A9-information-sc/). **MODERATE.** **[biblio-verified]**
  - Real campus recruiters rated real graduate résumés on academic qualifications, work experience and extracurricular activities. Recruiters' perceptions of these three areas predicted their judgments of employability.
  - Recruiters' ratings were only partly consistent with the "objective" résumé content, which suggests idiosyncratic weighting. Later papers cite it for the claim that recruiters infer abilities and attributes from résumé content, and that these inferences shape their hiring recommendations.
- **Thoms, P., McMasters, R., Roberts, M. R., & Dombkowski, D. A. (1999). Resume characteristics as predictors of an invitation to interview.** *Journal of Business and Psychology*, 13(3), 339–356. DOI: 10.1023/A:1022974232557. [Springer](https://link.springer.com/article/10.1023/A:1022974232557). **MODERATE–WEAK** (later researchers note the sample came from a single management course). **[biblio-verified]** Résumé characteristics predicted interview invitations for graduates. Later citations mention job-related information and grades among the positive items. The full predictor list was not checked in this session.
- **Knouse, S. B. (1994). Impressions of the resume: The effects of applicant education, experience, and impression management.** *Journal of Business and Psychology*, 9(1), 33–45. DOI: 10.1007/BF02230985. Relevant education and experience dominated evaluations. Impression-management content (self-promotion) helped mainly when the applicant had weaker qualifications. **MODERATE (student raters, older study).** **[from prior knowledge; check details]**
- **Bertrand, M., & Mullainathan, S. (2004). Are Emily and Greg more employable than Lakisha and Jamal? A field experiment on labor market discrimination.** *American Economic Review*, 94(4), 991–1013. DOI: 10.1257/0002828042002561. **STRONG** (field audit of about 5,000 résumés, widely replicated). **[from prior knowledge]**
  - White-sounding names received about 50% more callbacks.
  - A higher-quality résumé (more experience, skills, honours) raised callbacks more for White names than for Black names.
  - Relevance here: in real hiring, the content quality of a résumé does move callback rates.
- **Banerjee, A., Bertrand, M., Datta, S., & Mullainathan, S. (2009). Labor market discrimination in Delhi: Evidence from a field experiment.** *Journal of Comparative Economics*, 37(1), 14–27. DOI: 10.1016/j.jce.2008.09.002. [MIT DSpace](https://dspace.mit.edu/handle/1721.1/52303); [RePEc](https://econpapers.repec.org/RePEc:eee:jcecon:v:37:y:2009:i:1:p:14-27). **STRONG for India specifically.** **[verified: abstract]**
  - **Design:** 3,160 fictitious résumés sent to 371 openings in and around Delhi, for **software** and call-centre jobs.
  - **Software jobs:** **no evidence of caste discrimination**.
  - **Call-centre jobs:** large callback gaps for OBC applicants.
  - **Religion:** no discrimination against Muslims in either sector.
  - This is the only India-based résumé audit for software jobs that I found.
- **Kang, S. K., DeCelles, K. A., Tilcsik, A., & Jun, S. (2016). Whitened résumés: Race and self-presentation in the labor market.** *Administrative Science Quarterly*, 61(3), 469–502. DOI: 10.1177/0001839216639577. Résumés with racial cues removed got more callbacks, even from employers who called themselves pro-diversity. **STRONG.** **[from prior knowledge]**
- **Oreopoulos, P. (2011). Why do skilled immigrants struggle in the labor market? A field experiment with thirteen thousand resumes.** *American Economic Journal: Economic Policy*, 3(4), 148–171. DOI: 10.1257/pol.3.4.148. **STRONG.** **[from prior knowledge]**
  - In Toronto, résumés with Indian, Pakistani, Chinese or Greek names got fewer callbacks.
  - **Foreign experience** (including India) was discounted heavily compared with Canadian experience, and having a foreign degree mattered much less than having foreign experience.
  - Relevance: Indian applicants targeting MNCs abroad. It is less relevant to GCCs in India.
- **Kroft, K., Lange, F., & Notowidigdo, M. J. (2013). Duration dependence and labor market conditions: Evidence from a field experiment.** *Quarterly Journal of Economics*, 128(3), 1123–1167. DOI: 10.1093/qje/qjt015. Callbacks fell as the length of the résumé's current unemployment spell grew. **STRONG** (US). Relevant to employment gaps. **[from prior knowledge]**

**Layout, structure, readability**
- **Arnulf, J. K., Tegner, L., & Larssen, Ø. (2010). Impression making by résumé layout: Its impact on the probability of being shortlisted.** *European Journal of Work and Organizational Psychology*, 19(2), 221–230. DOI: 10.1080/13594320902903613. Norway. Layout affected shortlisting probability: a well-organised, conventional layout beat poor layouts, and highly creative layouts helped mainly where creativity was relevant. **MODERATE (single study).** **[from prior knowledge, DOI seen in search results; check details]**
- **Ladders (2018)** claims that clear section headings and an F-pattern layout help, but this is commercial. **WEAK.** [HR Dive](https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/)

**Quantified achievements**
- I found no peer-reviewed experiment isolating the effect of quantified accomplishment statements on callbacks. The common advice to quantify comes from career centres and coaching sellers. **WEAK / practitioner guidance only.**
- The nearest support is indirect. Recruiters infer competence from concrete, job-relevant content (Cole et al. 2007; Knouse 1994), and Bertrand & Mullainathan found that richer content raises callbacks.

### Inferences
- Spelling and typo penalties are large and backed by several studies: 7 points for just 2 errors. That makes proofreading the highest-certainty, lowest-cost improvement. The mechanism (perceived lower mental ability and conscientiousness) applies directly to engineering screens.
- In SWE terms, "job-relevant content" means stack and domain match and evidence of scope and impact. It probably matters more than layout polish. Layout effects exist but are small and poorly replicated. A clean, conventional single-column layout is the low-risk choice; that last point is an inference that also fits the parsing concern below.

### Gaps
- No peer-reviewed RCT on quantified versus unquantified bullets.
- No peer-reviewed study of **resume readability metrics** (for example, Flesch score) and callbacks.
- No study of two-column versus single-column layouts and ATS parse accuracy that is independent of resume-tool vendors.

## Q3. What does research say about recruiters' inferences from resume content (competence, conscientiousness) and about errors?

### Takeaway
Recruiters routinely infer personality and ability from résumés. The inferences are made with some agreement between recruiters but are **only weakly valid**. Recruiters agree with one another on extraversion and conscientiousness, but their inferences barely predict applicants' actual test scores. Errors are read as signs of lower ability and conscientiousness (Sterkens et al. 2023, mediation analysis).

### Cited Findings
- **Cole, M. S., Feild, H. S., & Giles, W. F. (2003). Using recruiter assessments of applicants' résumé content to predict applicant mental ability and Big Five personality dimensions.** *International Journal of Selection and Assessment*, 11(1), 78–88. DOI: 10.1111/1468-2389.00228. Recruiters' ratings of academic, work-experience and extracurricular content were related to some measured traits: extracurricular activities to extraversion, and academic achievement to mental ability and conscientiousness. The relationships were modest. **MODERATE.** **[from prior knowledge; check details]**
- **Cole, M. S., Feild, H. S., Giles, W. F., & Harris, S. G. (2009). Recruiters' inferences of applicant personality based on résumé screening: Do paper people have a personality?** *Journal of Business and Psychology*, 24(1), 5–18. DOI: 10.1007/s10869-008-9086-9. [PDF mirror](https://springerlink.bibliotecabuap.elogim.com/content/pdf/10.1007/s10869-008-9086-9.pdf). **MODERATE.** **[biblio-verified; findings from prior knowledge]**
  - 244 recruiters inferred Big Five traits from résumés.
  - Inter-rater reliability was acceptable, and the inferred traits (especially extraversion and conscientiousness) predicted recruiters' judgments of employability.
  - The inferences had **low validity** against applicants' self-reported personality, except partly for extraversion.
- **Burns, G. N., Christiansen, N. D., Morris, M. B., Periard, D. A., & Coaster, J. A. (2014). Effects of applicant personality on resume evaluations.** *Journal of Business and Psychology*, 29(4), 573–591. DOI: 10.1007/s10869-014-9349-6. Personality cues embedded in résumé content shaped evaluations. Résumés signalling conscientiousness and emotional stability were rated more hireable. **MODERATE.** **[from prior knowledge; check details]**
- **Sterkens et al. (2023)**: errors lower perceived mental ability, conscientiousness and interpersonal skills, and these perceptions account for about 53–55% of the penalty. **[verified]** [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283280)
- **Validity context. Schmidt, F. L., & Hunter, J. E. (1998). The validity and utility of selection methods in personnel psychology.** *Psychological Bulletin*, 124(2), 262–274. DOI: 10.1037/0033-2909.124.2.262. Meta-analysis reporting low validity for years of job experience (about r = .18) and education (about r = .10) as predictors of job performance. Sackett et al. (2022, *Journal of Applied Psychology*, DOI 10.1037/apl0000994) revised many of these estimates downward but kept the same ordering. **STRONG.** Implication: screeners lean on résumé proxies that predict performance only weakly. **[from prior knowledge]**

### Inferences
- Content that signals conscientiousness (precise, error-free, consistent formatting and dates) and ability (relevant achievements, hard problems solved) is what recruiters infer from, whatever the actual validity of those inferences.
- Because the inferences are noisy, specific, verifiable evidence (named systems, scale, outcomes, links to code) gives a screener less room for negative guessing. This is an inference, not a tested finding.

### Gaps
- None of these inference studies used SWE roles or technical recruiters. Most samples were US campus recruiters.

## Q4. Is there evidence on one-page vs two-page resumes for early-career engineers?

### Takeaway
There is **no peer-reviewed evidence specific to engineers**. The best-known academic study (accountancy recruiters, 2001) found a preference for **two pages for experienced applicants** and tolerance of two pages even for new graduates. Another study (recreation jobs) found preferences for 2–4 pages. Widely quoted "recruiters prefer two pages, 2.3×" figures come from ResumeGo, a resume-writing seller, so they are **commercial and unverified**.

### Cited Findings
- **Blackburn-Brockman, E., & Belanger, K. (2001). One page or two? A national study of CPA recruiters' preferences for résumé length.** *Journal of Business Communication*, 38(1), 29–57. DOI: 10.1177/002194360103800104. **MODERATE (one profession, old).** **[cited via Brown & Vaishampayan 2025; findings from prior knowledge]**
  - US Big-5 and other accounting-firm recruiters preferred one-page résumés for undergraduates with little experience.
  - They were more willing to accept, or preferred, two pages for candidates with more experience.
- **Ross, C. M., & Young, S. J. (2005). Resume preferences: Is it really "business as usual"?** *Journal of Career Development*, 32(2), 153–164. As summarised in [Brown & Vaishampayan 2025, arXiv](https://arxiv.org/html/2504.06387v1), recruiters for entry-level recreation and leisure jobs preferred 2–4 pages. **WEAK–MODERATE.**
- **ResumeGo (2018)** "recruiters 2.3× more likely to prefer two-page résumés". ResumeGo sells resume-writing services, so this is **commercially motivated and not peer-reviewed. WEAK.** Reported via [Quartz](https://qz.com/work/1520476/should-your-resume-be-one-page-or-two) and [ERE](https://www.ere.net/one-or-two-page-resumes-best/).
- University career-centre guidance (for example MIT CAPD and Harvard OCS) commonly recommends one page for students and early-career applicants. This is **practitioner guidance**, not evidence. **[not fetched this session]**

### Inferences
- For someone with 2–3 years of experience, the evidence does not support a hard rule either way. The more defensible principle, consistent with short screening times (Q1) and content-relevance findings (Q2), is that the first page must carry the strongest evidence. A second page is unlikely to hurt if it contains relevant content, but it may simply go unread. Indian product companies' expectations are not documented in the research literature.

### Gaps
- No study of SWE or engineering recruiters on length. No India study. No study of how ATS parsing interacts with length.

## Q5. Evidence specific to software engineering hiring screens (GitHub/portfolio signals, ACM/IEEE research)

### Takeaway
The software engineering research literature focuses heavily on **technical interviews**, not résumé screening. Hiring-related work on GitHub (Marlow & Dabbish, CSCW 2013) shows that some employers use public activity traces as signals of passion and skill, but mostly at an aggregate, superficial level. Large-sample, outcome-linked evidence that a GitHub link raises SWE callbacks is **absent**. A 2025 software engineering position paper calls résumé screening in tech a weak, keyword-driven and bias-prone stage with little supporting evidence.

### Cited Findings
- **Marlow, J., & Dabbish, L. (2013). Activity traces and signals in software developer recruitment and hiring.** *Proceedings of the 2013 ACM Conference on Computer Supported Cooperative Work (CSCW '13)*, 145–156. DOI: 10.1145/2441776.2441794. [Bibliographic record](https://bibtex.github.io/CSCW-2013-MarlowD.html). **MODERATE (qualitative interviews, US, 2013).** **[biblio-verified; findings from prior knowledge; the ACM page returned 403 in this session]**
  - Interviews with employers and recruiters who used GitHub profiles in hiring.
  - Employers treated GitHub activity as a more trustworthy signal of skill and passion than résumé claims, because it is hard to fake.
  - They looked at the volume and recency of activity and at side projects. Many glanced at aggregate activity rather than reading code.
  - A later study summarised in search results also reports that "in the majority of cases, employers did not investigate the contribution or interaction details, and instead focused only on the aggregate amounts of activity." [NSF PAR copy](https://par.nsf.gov/servlets/purl/10357418)
- **Marlow, J., Dabbish, L., & Herbsleb, J. (2013). Impression formation in online peer production: Activity traces and personal profiles in GitHub.** *CSCW '13*, 117–128. DOI: 10.1145/2441776.2441792. [NSF PAR PDF](https://par.nsf.gov/servlets/purl/10038300). **MODERATE (18 interviews).** **[verified]**
  - GitHub users form impressions of expertise from "history of activity across projects" and from collaborations with high-status projects.
  - Cues they used: "amount of activity, frequency of commits, number of projects owned vs. forked, length of time on site, languages used".
  - **Empty profiles** led to negative impressions ("wasn't a committed member").
  - The context is open-source peer evaluation, not employer screening, so it supports how developers read GitHub profiles by analogy only.
- **Singer, L., Figueira Filho, F., Cleary, B., Treude, C., Storey, M.-A., & Schneider, K. (2013). Mutual assessment in the social programmer ecosystem: An empirical investigation of developer profile aggregators.** *CSCW '13*, 103–116. DOI: 10.1145/2441776.2441790. Recruiters used aggregated developer profiles (GitHub and Stack Overflow) to assess candidates, but worried about gaming and missing context. **MODERATE (qualitative).** **[from prior knowledge]**
- **Behroozi, M., Parnin, C., & Barik, T. (2019). Hiring is broken: What do developers say about technical interviews?** *2019 IEEE Symposium on Visual Languages and Human-Centric Computing (VL/HCC)*, 1–9. DOI: 10.1109/VLHCC.2019.8818836. [PDF](https://web.eecs.umich.edu/~weimerw/2022-481W/readings/hiring-is-broken.pdf). Qualitative analysis of Hacker News discussions. Developers criticised interviews for lack of real-world relevance, bias, and heavy time demands. Relevant to the overall pipeline, **not** to résumé screening. **MODERATE.** **[verified: scope]**
- **Behroozi, M., Shirolkar, S., Barik, T., & Parnin, C. (2020). Does stress impact technical interview performance?** *ESEC/FSE 2020*, 481–492. DOI: 10.1145/3368089.3409712. Whiteboard interviews under observation lowered performance. This is an interview-stage study. **MODERATE.** **[from prior knowledge]**
- **Brown, C., & Vaishampayan, S. (2025). Towards evidence-based tech hiring pipelines.** arXiv:2504.06387 (**preprint / workshop position paper**, SE 2030 workshop). [arXiv](https://arxiv.org/html/2504.06387v1). **WEAK–MODERATE (position paper).** **[verified]**
  - Résumé matching is usually the first stage and is keyword-driven.
  - Keyword filters exclude candidates who lack exact terms (for example, a specific programming language) despite relevant experience.
  - Résumés are weak sources of contextual evidence, and AI or LLM screening shows race, gender and disability biases (Armstrong et al. 2024; Glazko et al. 2024).
  - Two-column or heavily formatted résumés may be misparsed. That claim rests on a non-academic source (Birt 2025).
  - The paper also repeats "99% of Fortune 500 use ATS", which comes from a Jobscan blog (a commercial resume-optimisation seller). Treat that figure as **commercial**.
- **ATS "75% of résumés rejected" claim**: traces to a **2012 press release by Preptel**, a defunct resume-optimisation vendor, with no published method. **Commercial and unverified; no peer-reviewed support.** Sources: [IT Brief UK](https://itbrief.co.uk/story/study-reveals-ats-rarely-auto-rejects-cvs-debunks-75-myth); [HiringThing (an ATS vendor, so also interested)](https://blog.hiringthing.com/applicant-tracking-systems-arent-excluding-job-applicants-people-are).
- **Fuller, J. B., Raman, M., Sage-Gavin, E., & Hines, K. (2021). *Hidden workers: Untapped talent.*** Harvard Business School Project on Managing the Future of Work & Accenture. [PDF (SHRM mirror)](https://nahr.shrm.org/sites/default/files/hiddenworkers09032021.pdf). This is a non-peer-reviewed academic/consultancy report. **MODERATE–WEAK.** **[verified via secondary reporting]**
  - **Sample:** 2,275 executives and 8,720 "hidden workers" surveyed in the US, UK and Germany.
  - **88%** of employers agreed that qualified high-skills candidates are screened out because they do not match the exact job-description criteria (94% for middle-skills candidates). [The Register](https://www.theregister.com/2021/09/08/harvard_jobs_report/)
  - **More than 90%** of employers using a recruiting management system relied on it for the first cut or ranking of applicants.
  - Critics note the report blames rigid, human-defined criteria (for example, employment-gap filters and exact keyword matches), not autonomous ATS rejection.

### Inferences
- For SWE screens, the defensible conclusions are these:
  - Keyword and skill-term match with the job description matters at the first cut, because RMS or ATS ranking and recruiter keyword search are widely used (Hidden Workers).
  - Public code activity is read as a signal, but superficially, by volume and recency (Marlow & Dabbish). An empty or abandoned GitHub profile linked from a résumé may hurt more than having no link; this is an inference from the impression-formation findings.
- Transferability to India: the GitHub and ATS findings concern platform-mediated behaviour and probably transfer to Indian product companies and GCCs, which use the same ATS vendors and LinkedIn-based sourcing. Caste and religion audit evidence (Banerjee et al. 2009) suggests that software hiring in Delhi was less discriminatory on those dimensions than call-centre hiring. All transferability claims are inferences.

### Gaps
- **No peer-reviewed study** found on:
  - how technical hiring managers or recruiters evaluate SWE résumés (for example, an eye-tracking or vignette study with SWE recruiters);
  - whether a GitHub or portfolio link changes callback rates in a controlled audit;
  - how "services company" vs "product company" employer brands affect SWE résumé screening in India;
  - competitive-programming ratings (LeetCode, Codeforces) as résumé signals.
- **No independent measurement** of ATS auto-rejection rates. The Preptel 75% and Jobscan 99% figures are commercial.
- **Peter Kuhn** (job-search signals): the assignment mentions him, but I did not retrieve a specific Kuhn paper on résumé signals in this session. His relevant work is mainly on internet job search and job-board behaviour; for example, Kuhn & Shen (2013), "Gender discrimination in job ads: Evidence from China", *QJE* 128(1), 287–336. The report writer should not cite Kuhn for résumé-content effects without checking.
- Community sources (Reddit, HN, Blind) were not used.

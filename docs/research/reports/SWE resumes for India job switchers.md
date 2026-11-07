# Verifiable evidence outranks keyword tricks for switchers

*A research report on effective resumes for Indian software engineers with 2-3 years of experience who are moving from IT services to SDE-1/SDE-2 roles at product companies, startups and GCCs, and on what an AI-assisted career-record system must do to produce those resumes truthfully.*

Report date: 2026-11-07. Corpus: six research-note files compiled on 2026-11-07 (ATS parsing mechanics; recruiter screening evidence; SWE resume content guidance; India market and norms; career records, interviews and AI; practitioner community).

---

## Abstract

An effective resume for this candidate is a **single-column, text-based, one-to-two-page document whose experience section carries specific, outcome-first, verifiable accomplishments named in the job description's own technical vocabulary**, with no photo or legacy Indian "biodata" fields and with client work described by industry and scale rather than by name. The strongest evidence behind this picture is uneven. ATS vendor documentation (Greenhouse, Lever, Textkernel) firmly supports the formatting rules: columns, tables, text boxes, header/footer contact details and image-only files are documented parse-failure causes. Peer-reviewed research firmly supports only a few content claims, chiefly that spelling errors cut interview chances (5 errors reduced interview probability by 18.5 percentage points among 445 Belgian recruiters) and that screeners read the whole resume, spending the most time on employment history (about 16 seconds per resume in the only peer-reviewed eye-tracking study found). The popular claims that "75% of resumes are rejected by ATS" and that "recruiters look for 6 seconds" both trace to companies that sold services to job seekers and have no published methodology. Employer guidance from Google and Amazon, plus university career centres, converges on accomplishment-plus-measure-plus-method bullets, but no controlled study shows quantified bullets raise callbacks, and no credible source condemns ticket or story counts as inherently hollow. For an AI-assisted system, the evidence implies a design centred on **contemporaneous, evidence-linked records** (autobiographical memory decays and self-assessment is unreliable), **STAR records deep enough to survive structured-interview follow-up probes**, **generation that never adds facts absent from the record**, and **deterministic formatting rules drawn from vendor documentation**. Recent working papers suggest generative AI erodes the signalling value of tailored text, which makes verifiable specifics, not polish, the scarce asset. Major limitations: Reddit was inaccessible, almost no Indian employer published resume guidance, most research is US/European, and several cited studies were described from prior knowledge rather than re-read and are flagged as such.

---

## 1. Introduction and scope

India's technology labour market is shifting toward exactly the employers this candidate targets. NASSCOM-Zinnov reporting puts India's global capability centres (GCCs) at **2,117 firms and about 2.36 million employees in FY26** ([NewsBytes summary of NASSCOM-Zinnov, 2026](https://www.newsbytesapp.com/news/business/nasscom-zinnov-gccs-in-india-employ-236-million-plan-35-million-by-2030/tldr)), against a total tech workforce of about 5.95 million growing roughly 2-2.5% a year ([The Week/PTI on NASSCOM Strategic Review 2026](https://www.theweek.in/wire-updates/business/2026/02/24/india-fy26-tech-revenues-seen-6.1-pc-up-at-usd-315-bn-jobs-also-grow-nasscom.amp.html)). Naukri's November 2025 JobSpeak index reported GCC postings up **18% year on year** against 14% for IT/software services, with AI/ML up 72% ([Naukri JobSpeak, Nov 2025](https://www.infoedge.in/pdfs/News_Events_pdfs/Naukri-Jobspeak-Nov-2025.pdf)). Every one of these figures comes from a trade body, consultancy or job board with an interest in a growth narrative, but they agree on direction: demand is growing fastest at GCCs and product firms, and many services engineers are competing for the same move.

This report asks two linked questions. First, what does an effective resume look like for a software engineer in India with 2-3 years of experience switching from an IT services company to SDE-1 (possibly SDE-2) roles at Indian product companies, startups, and MNC offices or GCCs? Second, given that evidence, what must an AI-assisted system do to produce such resumes truthfully? The system in view is a set of agent skills that keep a structured, living, evidence-backed career record; capture work experience as STAR-format (Situation, Task, Action, Result) accomplishments; prepare interview stories; and later build ATS-friendly, job-description-optimised resumes.

The scope covers the resume artefact (format, structure, content, India-specific conventions), the systems and people that screen it (ATS parsers, recruiter search, human screeners), the adjacent interview stage that resume claims must survive, and the evidence on AI-assisted writing and screening. It excludes salary negotiation, interview technical preparation (DSA, system design) except as it bears on the resume, and resumes for roles outside India.

---

## 2. Methodology

### 2.1 Corpus and process

The report synthesises six research-note files produced by a team of researchers on 2026-11-07, each addressing one theme: ATS parsing mechanics; recruiter screening evidence; SWE resume content guidance; India market and norms; career records, interviews and AI; and practitioner community evidence. The notes contain cited findings, the researchers' inferences, and explicit gaps. This report draws findings only from cited material, treats researcher inferences as hypotheses to be argued rather than facts, and carries forward each note's verification status. Where a note says a source was read only as a search snippet, not fetched, or described from the researcher's prior knowledge, that status is preserved here.

### 2.2 Source policy

The user set the following source policy, which the researchers applied and this report enforces:

| Source class | Treatment | Label used in this report |
|---|---|---|
| Sources that sell to job seekers (resume builders, ATS checkers, courses, coaching, interview-prep subscriptions, paid resume reviews) | Excluded as evidence. Mentioned only to trace where a widely repeated claim originated. | COMMERCIAL / UNVERIFIED |
| Peer-reviewed research; large or replicated studies | Preferred. | ACADEMIC |
| ATS and parser vendor documentation (these vendors sell to employers) | Allowed and labelled. | VENDOR DOC |
| Employer hiring guidance (employer domains, or employer recruiters quoted in mainstream press) | Allowed and labelled. | EMPLOYER |
| University career centres and university student societies | Allowed and labelled. | CAREER CENTRE |
| Industry bodies, consultancies, job-board market data | Allowed as market context with bias noted. | INDUSTRY DATA |
| Practitioner communities (wikis, Hacker News, Blind, Fishbowl) | Allowed at LOW confidence only. | COMMUNITY (LOW) |

Applying the policy excluded, among others, Ladders-style statistics as evidence (Ladders is a job-board and career-services firm), ResumeGo's page-length survey, Jobscan's "99% of Fortune 500" figure, Enhancv's recruiter survey, interviewing.io's critique of the Bloomberg GPT audit, and all Indian resume-builder and interview-prep sites. One borderline source, Yangshun Tay's *Tech Interview Handbook*, is free but carries affiliate links to paid resume products; it is used sparingly and labelled MIXED.

### 2.3 Evidence-strength scale

Each finding in Section 3 carries an evidence-strength label:

| Label | Meaning |
|---|---|
| **STRONG** | Peer-reviewed field experiment or meta-analysis, large sample or replicated, real screeners or real outcomes. |
| **MODERATE** | Peer-reviewed single study, small or student samples, vignettes; or primary vendor/employer documentation describing its own system or process. |
| **WEAK** | Commercial, unpublished or unreplicated work; career-centre or employer advice not tested against outcomes; position papers. |
| **LOW** | Practitioner-community opinion. |

Vendor documentation is rated MODERATE for claims about how that vendor's own product behaves (it is authoritative about mechanics) but WEAK for claims about outcomes. Employer and career-centre guidance is rated WEAK-to-MODERATE: it reflects what screeners say they want, which is informative, but it is advice, not measurement.

Two verification flags supplement the labels. **[unverified]** marks a claim the researchers saw only through search snippets or secondary accounts. **[prior knowledge]** marks a study whose citation was confirmed but whose findings were described from the researcher's memory and not re-read in the session; these must be checked before any figure is quoted.

---

## 3. Findings

### 3.1 Parsers fail on layout, not on file type

**Evidence strength: MODERATE (VENDOR DOC) for mechanics; no independent benchmark.**

The single most specific primary source is Greenhouse's support article on unsuccessful resume parses. It lists, verbatim, the causes of failed or partial parses: graphics, photos or word art; resumes uploaded as an image; "complex resumes with tables, headers, and footers"; "resumes with the name and contact information in the header, footer, or text box"; "resumes that have a columned layout"; letter-spaced text; resumes without clear sections or with inconsistent formatting; company names lacking identifiers such as Inc. or Ltd.; and abbreviated job titles such as "Sr. Account Exec" ([Greenhouse, 2026a](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse)). The same article sets a **2.5 MB parse limit**, separate from the 100 MB upload limit ([Greenhouse, 2026a](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse); [Greenhouse, 2026b](https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-file-types-for-resumes-and-cover-letters)). Crucially, the consequence of failure is manual correction by the recruiter, not rejection: a partial parse "will need to be manually corrected and verified".

Textkernel, a parsing engine licensed into many ATSs, supplies the mechanism for why columns matter. Text rendering is the first step and its errors propagate; naive rendering interleaves text from different columns; at least 15% of CVs use columns; and even its improved, gradient-boosted column detector finds only **82% of column separators**, up from 60%, with well-rendered CVs rising from 62% to 90% on about 700 test CVs. Contact details were the fields most damaged by column mixing ([Textkernel, n.d.-a](https://textkernel.com/learn-support/blog/improving-extraction-from-column-resumes)). Textkernel also notes that "current" or "Present" dates are interpreted relative to the document's last-modified date ([Textkernel, n.d.-b](https://developer.textkernel.com/tx-platform/v10/faq/)).

On file type, the vendor record contradicts popular advice. Greenhouse accepts .doc, .docx, .pdf, .rtf and .txt ([Greenhouse, 2026b](https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-file-types-for-resumes-and-cover-letters)); Lever lists Word, PDF, RTF, WordPerfect, HTML and OpenDocument ([Lever, n.d.](https://help.lever.co/hc/en-us/articles/20087345054749)) [unverified: search snippet, page did not render]. Workday's documentation, login-gated, confirms only that parsing exists and that employers can hide it for external candidates ([Workday, n.d.](https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/candidates/set-up-prospects-and-candidates/hdc1552497830785.html)) [unverified: snippet]. The claims that Workday or Lever "prefer DOCX", and the "34% Workday autofill error rate", appear only on resume-service blogs. The defensible rule is not "use DOCX" but **"submit a PDF with a real, correctly ordered text layer, or a DOCX"**.

For Indian employers specifically, no parser documentation was found for Darwinbox, Keka, Zoho Recruit or Naukri, and no independent ATS market-share data exists for India. The landscape the notes reconstruct is a split between global enterprise suites at MNCs and GCCs, Greenhouse and Lever at global-first product firms, Indian HRMS products in the mid-market, and job-portal databases alongside all of them. Formatting rules should therefore target the lowest-common-denominator parser rather than any one product.

### 3.2 Recruiters search and filter; auto-rejection comes from knockout questions

**Evidence strength: MODERATE (VENDOR DOC, ACADEMIC-industry report, LEGAL) for the mechanism; STRONG that the "75%" figure lacks support.**

Documented ATS behaviour is a database plus a workflow. Greenhouse supports Boolean full-text search with AND and wildcards over resumes ([Greenhouse, n.d.-a](https://support.greenhouse.io/hc/en-us/articles/202360199-Search-candidates-using-Boolean-queries)) [snippet]. Naukri's Resdex lets recruiters search "various fields of a resume" with mandatory keywords and filter by designation, institute and **resume freshness**, and Naukri states that recently updated profiles rank higher ([Naukri, n.d.-a](https://naukricom.freshdesk.com/support/solutions/articles/228261-what-is-the-significance-of-keyword-search-in-resdex-); [Naukri, n.d.-b](https://www.naukri.com/blog/recruiter-resdex/)). The documented automatic-rejection mechanism is the employer-configured **knockout question**: Greenhouse application rules auto-reject on a candidate's answer to a configured question ([Greenhouse, n.d.-b](https://support.greenhouse.io/hc/en-us/articles/360029081512-Auto-Reject-for-prospect-post)) [snippet], and Workable, Gem, Kula and others document equivalents ([Workable, n.d.](https://help.workable.com/hc/en-us/articles/115012238688); [Kula, n.d.](https://support.kula.ai/articles/7962068559-auto-rejection-rules-and-knockout-questions)).

Automated filtering and ranking are nonetheless real. The HBS/Accenture *Hidden Workers* report, surveying 2,275 executives and 8,720 workers in the US, UK and Germany, found **more than 90% of employers** use their recruiting system for the first cut or ranking, relying heavily on "negative" filters such as missing degrees or gaps over six months, and that **88%** agreed qualified high-skills candidates are screened out for not matching exact job-description criteria ([Fuller et al., 2021](https://nahr.shrm.org/sites/default/files/hiddenworkers09032021.pdf); [The Register, 2021](https://www.theregister.com/2021/09/08/harvard_jobs_report/)) [figures via secondary coverage; PDF not read in full]. In *Mobley v. Workday*, a US federal court in 2025 preliminarily certified a collective of older applicants and extended it to applications "scored, sorted, ranked, or screened" by Workday's HiredScore AI features; Workday characterises the ruling as procedural and based on allegations ([Civil Rights Litigation Clearinghouse, n.d.](https://clearinghouse.net/case/44074/); [Fisher Phillips, 2025](https://www.fisherphillips.com/en/news-insights/discrimination-lawsuit-over-workdays-ai-hiring-tools-can-proceed-as-class-action-6-things)). Status after January 2026 was not verified. Rejection, in short, flows mostly from rigid human-configured criteria and optional AI ranking layers, not from a hidden keyword-density score in a standard parser.

Skill taxonomies sit between these two paths. Textkernel normalises skills against a taxonomy of roughly 12,000-13,000 concepts and 250,000-300,000 synonyms, mapping acronyms and alternative wordings to one concept ([Textkernel, n.d.-c](https://developer.textkernel.com/tx-platform/v10/skills-intelligence/skills-api/overview/)), but a recruiter's literal Boolean string matches only text actually present. Writing both an acronym and its expansion once ("Amazon Web Services (AWS)") covers both paths, a practice the *Tech Interview Handbook* also recommends ([Tay, n.d.](https://www.techinterviewhandbook.org/resume/)) [MIXED].

### 3.3 Human screeners skim fast, read everything, and punish errors

**Evidence strength: MODERATE for viewing time; STRONG-MODERATE for spelling penalties; WEAK for layout and length.**

The only peer-reviewed eye-tracking resume study found, Lahey and Oxley's experiment with 152 student and professional participants rating 5,960 resumes for a clerical job, measured a **mean of 16.24 seconds per resume (SD 10.17)**. Screeners "do look at the entire resume", and the employment-history area received the most viewing time (about 4.9 seconds in the working-paper table, a figure the researcher flagged for checking against the published version) ([Lahey & Oxley, 2021](https://www.nber.org/papers/w25357.pdf)). The authors note this is comparable to the 15-second estimate HR professionals give when asked. Bartoš et al. found in a Czech field experiment that employers spent less effort reading CVs from disfavoured minority applicants ([Bartoš et al., 2016](https://doi.org/10.1257/aer.20140571)) [prior knowledge, cited via Lahey & Oxley], which suggests, by analogy only, that a services-company CV in a product-company screen may get less reading time.

The best-evidenced format feature is spelling. Sterkens et al. had 445 Flemish HR professionals rate 1,335 vignette resumes across eight vacancies: relative to an error-free resume, **two spelling errors cut interview probability by 7.3 percentage points and five by 18.5 points**, and roughly half the penalty ran through lower perceived mental ability (about 32%), conscientiousness (12%) and interpersonal skill (9%) ([Sterkens et al., 2023](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283280)). Earlier studies in the Netherlands and France found the same direction ([van Toorenburg et al., 2015](https://doi.org/10.1089/cyber.2014.0542); [Martin-Lacroux & Lacroux, 2017](https://doi.org/10.1177/2329490616671310)) [cited via Sterkens et al.]. Recruiters infer personality and ability from resume content with reasonable inter-rater agreement but low validity ([Cole et al., 2009](https://doi.org/10.1007/s10869-008-9086-9)) [prior knowledge], so errors and vague claims leave room for negative inferences that specific, checkable detail would close.

Layout evidence is thin. A Norwegian study found conventional, well-organised layouts beat poor ones for shortlisting ([Arnulf et al., 2010](https://doi.org/10.1080/13594320902903613)) [prior knowledge]. On length, the best-known academic study is of US accounting recruiters in 2001, who preferred one page for undergraduates but accepted or preferred two for experienced candidates ([Blackburn-Brockman & Belanger, 2001](https://doi.org/10.1177/002194360103800104)) [prior knowledge]. No study covers engineers, India, or 2-3 years of experience. MIT recommends one page "unless you have extensive experience" ([MIT CAPD, n.d.](https://capd.mit.edu/resources/resumes/)), the IIT Madras campus rules specify a single A4 page ([IIT Madras CDC, 2025](https://internship.iitm.ac.in/downloads/Internship_Resume_Guidelines_2025-26.pdf)), and Harvard sets no limit ([Harvard Mignone Center, n.d.](https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/)). The defensible principle is that **page one must carry the strongest, most job-relevant evidence**; a second page of relevant content is unlikely to hurt but may go unread.

### 3.4 Employers and career centres want outcome-first bullets, but quantification is untested

**Evidence strength: WEAK-to-MODERATE (EMPLOYER, CAREER CENTRE); no controlled outcome evidence for quantification.**

Two employers published attributable, substantive resume advice. Google's X-Y-Z formula, "Accomplished X, as measured by Y, by doing Z", was presented by a Google engineer-recruiter, with an engineering worked example quantifying a 15% change in server query response time "by restructuring our API" ([Umoh/CNBC, 2018](https://www.cnbc.com/2018/08/16/google-recruiters-share-the-3-part-formula-for-stronger-resumes.html)); attribution of the formula to Laszlo Bock's 2014 LinkedIn post rests on search snippets ([Business Insider India, 2014](https://www.businessinsider.in/google-hr-boss-says-this-is-the-key-to-a-perfect-resume/articleshow/43924179.cms)) [unverified]. Amazon's India site quotes its recruiters: keep resumes "text-forward, black and white, and simple"; "focus on your actions and results"; not every bullet needs a number but more quantification is better; and "you don't need a completely different resume for each role", just emphasis guided by the posting's Basic and Preferred Qualifications ([Bunch/Amazon India, n.d.](https://www.aboutamazon.in/news/workplace/amazon-india-job-resume-tips)). The researchers found no attributable resume guidance from Microsoft, Meta, Atlassian, Flipkart, Razorpay, Zerodha, Swiggy or any GCC.

University career centres agree with each other on the fundamentals. MIT asks for strong action verbs, named methods and languages, accomplishments over duties, quantification, skills shown both in a Skills section and in context, and a broader **master resume** from which each application is selected ([MIT CAPD, n.d.](https://capd.mit.edu/resources/resumes/)). Harvard asks writers to "write to express, not impress", be "fact-based: quantify and qualify", avoid pronouns and abbreviations, and use AI to work in job-description keywords without letting it be the primary author, because its output "will likely be very generic" ([Harvard Mignone Center, n.d.](https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/)). Illinois HKN's A-T-O-M formula (Action verb, Tool, Outcome metric, Method) caps bullets at two lines and aims for about one number per two lines ([HKN Illinois, 2025](https://wiki.hkn.illinois.edu/more%20advice/1.finding%20an%20internship/)). Columbia and Amazon both say explicitly that not every bullet must be quantified ([Columbia CCE, n.d.](https://www.careereducation.columbia.edu/resources/resumes-impact-creating-strong-bullet-points) [search summary only]; [Bunch/Amazon India, n.d.](https://www.aboutamazon.in/news/workplace/amazon-india-job-resume-tips)).

When business metrics are unavailable, which is common for services engineers whose client work is under NDA, the sources explicitly endorse technical proxies. HKN lists latency, CPU and memory, throughput, accuracy, test coverage, money saved, users impacted and **tickets closed**, and advises relative figures such as "2× faster" when absolutes are confidential ([HKN Illinois, 2025](https://wiki.hkn.illinois.edu/more%20advice/1.finding%20an%20internship/)). Google's examples show that comparison counts ("second place out of 50 teams") are valid measures when no performance metric exists ([Umoh/CNBC, 2018](https://www.cnbc.com/2018/08/16/google-recruiters-share-the-3-part-formula-for-stronger-resumes.html)); Amazon's use error-rate and complaint reductions ([Bunch/Amazon India, n.d.](https://www.aboutamazon.in/news/workplace/amazon-india-job-resume-tips)).

What no source supplies is outcome evidence. The researchers found **no peer-reviewed experiment isolating quantified versus unquantified bullets** and no study comparing achievement-oriented with duty-oriented statements. The closest support is indirect: field audits show that richer resume content raises callbacks ([Bertrand & Mullainathan, 2004](https://doi.org/10.1257/0002828042002561)) [prior knowledge], and recruiters infer competence from concrete, job-relevant content ([Cole et al., 2007](https://doi.org/10.1111/j.1464-0597.2007.00288.x)) [biblio-verified; findings from prior knowledge]. Quantification is therefore best treated as strongly endorsed practice with plausible mechanisms, not as a proven effect.

### 3.5 India-specific conventions favour minimal personal data and verifiable claims

**Evidence strength: MODERATE for the IIT Madras rules and BGV infrastructure; WEAK-to-LOW for lateral-hire conventions.**

The one authoritative Indian university source read in full, IIT Madras's 2025-26 resume guidelines, bans photos, prohibits rounding CGPA ("7.99 is NOT 8"), requires proof documents for every claim, requires code or report links for personal projects, and warns students against copying archived resume points because "it will be evident to the recruiter" ([IIT Madras CDC, 2025](https://internship.iitm.ac.in/downloads/Internship_Resume_Guidelines_2025-26.pdf)). These are campus-portal rules where the institute anonymises contact details, so they do not transfer wholesale to lateral hiring, but they show the top Indian placement ecosystem's norms: no photo, exact scores, verifiable claims. MIT likewise says to omit age, religion, health, marital status, photo, salary and references ([MIT CAPD, n.d.](https://capd.mit.edu/resources/resumes/)). Legacy "biodata" fields (date of birth, father's name, marital status, declaration) survive in some college templates and a Naukri-hosted template ([Naukri, n.d.-c](https://company.naukri.com/landing-page/snp/resume-template.doc)) [LOW, snippet], but no current authoritative source recommends them.

India's Digital Personal Data Protection Act 2023 and the DPDP Rules notified on 13 November 2025 embed data minimisation and purpose limitation ([Mondaq, 2025](https://www.mondaq.com/india/data-protection/1708164/digital-personal-data-protection-rules-2025-notified); [SCC Online, 2025](https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/)). The Act binds employers, not candidates, and law-firm commentary calls it unsettled whether the employment legitimate-use ground covers applicants ([Bar & Bench, n.d.](https://www.barandbench.com/view-point/navigating-legitimate-use-exemption-employee-data-digital-personal-data-protection-act-2023)). It supplies an argument for omitting DOB or marital status, not a prohibition.

Background verification (BGV) gives truthfulness concrete stakes. NASSCOM's National Skills Registry reports over 25.8 lakh IT professional identification numbers, 337 subscriber companies and 25 background checkers ([National Skills Registry, n.d.](https://nationalskillsregistry.com/)). Claims that BGV is industry-standard but not legally mandatory, that Infosys and TCS terminated staff over resume discrepancies, and that "up to 10% of resumes are falsified per NASSCOM" were seen only in snippets or vendor marketing and are **not verified**; the last should not be used at all. The inference that dates, titles and employers will be checked is strong; the specific prevalence figures are not.

Client confidentiality is the services engineer's distinctive problem. The only sources are LOW-confidence community threads, which converge on naming the actual employer, describing the client generically by industry and scale ("global technology company"), offering the name on request, and reading the actual NDA ([Blind, 2024](https://www.teamblind.com/post/how-to-include-high-profile-client-projects-on-your-resume-without-violating-ndas-jea26g4u)). A US consultancy thread recommends listing "Client (Contractor)" ([Blind, n.d.-a](https://www.teamblind.com/post/stigma-for-having-desi-consultancies-in-resume-sldnoy5i)) [snippet], but listing a client in place of the real employer would likely conflict with Indian BGV, which verifies the employer of record.

### 3.6 Level targeting sits at the SDE-1/SDE-2 boundary

**Evidence strength: WEAK-MODERATE (postings via aggregators); LOW for community claims.**

Amazon India SDE II postings most commonly require "3+ years of non-internship professional software development experience", some adding "2+ years of ... design or architecture" experience ([Jointaro mirror of Amazon posting, n.d.](https://www.jointaro.com/jobs/amazon/software-development-engineer-ii-981d2be4); [apna.co Amazon listing, n.d.](https://apna.co/job/bengaluru/software-dev-engineer-ii-1921035727)). Flipkart SDE-2 listings on aggregators range from about 2 to 2.5 years minimum and emphasise problem solving, LLD/HLD design, building features from product requirements, mentoring, and in one case "product base startup company experience is a must" ([weekday.works Flipkart listing, n.d.](https://jobs.weekday.works/flipkart-software-development-engineer-ii-(sde-2))). A candidate-reported Flipkart process places a design round at the centre: "At SDE-2 level, design is the differentiator" ([LeetCode Discuss, 2026](https://leetcode.com/discuss/post/8455829/flipkart-sde-2-interview-experience-jan-o8ngx/)) [LOW]. Community claims conflict: one 2020 Blind comment says L1/SDE-1 is "generally reserved for new grads and <2 yr work ex", while others say product companies discount services years ([Blind, 2020](https://www.teamblind.com/post/switching-to-product-based-companiesgoogleamazonetc-as-junior-engineersde-1swe-1sre-dy8cdm6c)) [LOW, pre-2022]. The resume consequence is that SDE-2 claims must be visible as **design ownership, end-to-end feature delivery, reliability or scaling decisions, mentoring, and incident ownership**, because those are what postings name.

### 3.7 Channels: Naukri profiles and referrals run parallel to the resume

**Evidence strength: MODERATE (Naukri self-description); WEAK-LOW for referrals.**

Naukri reports about 1 lakh clients, 30 lakh daily applications and 70 lakh new mandates a year, and builds its index from recruiter searches of its resume database ([Naukri JobSpeak, Nov 2025](https://www.infoedge.in/pdfs/News_Events_pdfs/Naukri-Jobspeak-Nov-2025.pdf)). Because Resdex searches structured fields and weights freshness, the Naukri profile (headline, key skills, designation, notice period, CTC fields) functions as a second resume that must stay consistent with the PDF. No documentation was found on how Naukri parses uploaded resumes, and claims such as "headline is 18% of ranking" exist only on commercial sites. LinkedIn's India Recruiting Trends surveys found 55% (2016) and 63% (2017) of Indian talent leaders naming referrals as the top source of quality hires ([Business Insider India, 2016](https://www.businessinsider.in/Majority-of-talent-leaders-in-India-want-a-push-in-hiring-budgets-states-LinkedIn-survey/articleshow/55559164.cms)), but these data are old. Community reports say a referral gets a human glance but no guaranteed shortlist ([Fishbowl, n.d.](https://www.fishbowlapp.com/post/is-there-any-guarantee-that-our-cv-will-definitely-get-shortlisted-after-getting-referral-from-company-people-if-no-what)) [LOW]. Current CTC, expected CTC and notice period appear to be collected in forms and calls rather than on the resume, an inference no source confirmed.

### 3.8 The services background is perceived as narrow scope

**Evidence strength: WEAK-MODERATE (academic, abstract-level); LOW (community).**

No study directly measures how Indian product firms or GCCs evaluate ex-services engineers, a gap the researchers judge genuine rather than a search artefact. An AMCIS 2021 ethnography of one Indian IT services firm describes traditional services work as producing "generic programmers" with constrained mobility into emerging-technology roles ([AMCIS SIG LEAD, 2021](https://aisel.aisnet.org/amcis2021/is_leadership/sig_lead/2)) [abstract only], and Daxini (2025) frames early-career Bangalore work as either stimulating R&D or "outsourced, fragmented coding tasks" ([Daxini, 2025](https://econpapers.repec.org/bookchap/sprsprchp/978-3-031-80618-6_5f12.htm)) [abstract only]. Sociological work on "merit" in Indian IT hiring links screening to unequal access to elite education ([Upadhya, 2007](https://cms.nias.res.in/node/2459); [Fernandez, 2018](https://scholarcommons.scu.edu/faculty_books/386)). Blind users report services resumes not being shortlisted despite heavy LeetCode practice and recruiters looking mainly at "the name of the company and years and job family" ([Blind, n.d.-b](https://www.teamblind.com/post/switch-from-service-based-company-to-faang-cc36hrze)) [LOW, snippet]. The one India-based resume audit for software jobs, in Delhi, found no caste or religion discrimination in software callbacks, unlike call-centre jobs ([Banerjee et al., 2009](https://dspace.mit.edu/handle/1721.1/52303)). Taken together, the weakness a services resume must overcome is perceived scope: maintenance, tickets, client-dictated tasks and older stacks. The remedy the evidence points to is visible ownership, design decisions, modern-stack vocabulary matching the posting, and measurable impact.

### 3.9 Projects and GitHub are read, but superficially

**Evidence strength: MODERATE (qualitative CSCW studies); no callback evidence.**

Marlow and Dabbish's interviews found employers treated GitHub activity as a harder-to-fake signal than resume claims but mostly glanced at aggregate volume and recency rather than reading code ([Marlow & Dabbish, 2013](https://bibtex.github.io/CSCW-2013-MarlowD.html); [NSF PAR copy](https://par.nsf.gov/servlets/purl/10357418)) [biblio-verified; findings partly from prior knowledge]. In open-source peer evaluation, empty profiles produced negative impressions ([Marlow, Dabbish & Herbsleb, 2013](https://par.nsf.gov/servlets/purl/10038300)). Career centres treat linked, scoped projects as standard content ([HKN Illinois, 2025](https://wiki.hkn.illinois.edu/more%20advice/1.finding%20an%20internship/); [MIT CAPD, n.d.](https://capd.mit.edu/resources/resumes/)), while Hacker News hiring managers say "any reasonable experience nullifies personal projects" ([Hacker News, 2023](https://news.ycombinator.com/item?id=34609741)) [LOW], and the developersIndia wiki says include projects only if you can discuss them confidently ([developersIndia wiki, n.d.](https://wiki.developersindia.in/community-guides/how-to-create-an-ideal-software-engineering-resume.html)) [LOW]. No controlled study shows a GitHub link changes callback rates. For a services engineer whose client work is invisible and NDA-bound, one or two substantial, linked projects are the most plausible verifiable supplement; an abandoned profile linked from the resume is plausibly worse than none.

### 3.10 Contemporaneous records counter memory decay and self-assessment bias

**Evidence strength: MODERATE-STRONG for the underlying cognition; no outcome evidence for brag documents.**

No study tests brag documents or work logs against career outcomes. The case is indirect but consistent. Wagenaar's six-year diary study logged about 2,400 events by what, who, where and when, and found recall depended on salience, emotional involvement and rehearsal, with rapid early loss ([Wagenaar, 1986](https://link.springer.com/content/pdf/10.3758/BF03211313.pdf)); a recent 24-year replication found **fewer than two-thirds of recorded events were remembered** ([Journal of Cognition replication](https://journalofcognition.org/en/articles/10.5334/joc.334)) [snippet-level; verify figures]. Self-assessments of skill correlate only modestly with objective performance ([Dunning, Heath & Suls, 2004](https://www.psychologicalscience.org/journals/pspi/j.1529-1006.2004.00018.x/)). Women describe equal performance less favourably than men on male-typed tasks, and **the gap persists when all incentives to self-promote are removed** ([Exley & Kessler, 2022](https://www.nber.org/papers/w26345)). Julia Evans' practitioner "brag document" supplies a de facto schema (goals; projects with contribution, impact and numbers, with results added months later; collaboration and mentorship; design and documentation; company building; learning) and a truthfulness standard: make your work sound "**exactly as good as it is**" ([Evans, 2019](https://jvns.ca/blog/brag-documents/)) [LOW, practitioner]. The developersIndia wiki independently recommends adding your best achievement to a running brag document every three months ([developersIndia wiki, n.d.](https://wiki.developersindia.in/community-guides/how-to-create-an-ideal-software-engineering-resume.html)) [LOW].

### 3.11 Structured interviews probe what the resume claims

**Evidence strength: STRONG-MODERATE (meta-analyses via abstracts); MODERATE (EMPLOYER).**

Structured interviews standardise questions, follow-up probes and scoring rubrics, and structure reduces the effect of race, gender and disability on ratings ([Levashina et al., 2014](https://digitalcommons.usu.edu/manage_facpub/423/)). Huffcutt et al.'s meta-analysis of 54 studies found job complexity lowered the validity of hypothetical (situational) questions but not of past-behaviour questions ([Huffcutt et al., 2004](https://jlupub.ub.uni-giessen.de/items/043303fd-a40c-4e1f-abc4-3f0f01f78584)), supporting a bank of true stories for complex SWE work. Amazon's India site tells candidates to "always answer the interview questions using the STAR method", to treat STAR as "not something to memorize", to include failures and lessons, to add metrics, to prefer recent situations, and on "I" versus "we": "Let us know what you actually did" ([Bunch/Amazon India, n.d.-b](https://www.aboutamazon.in/news/workplace/amazon-interview-success-tips)). Google's re:Work guide describes behavioural questions with pre-set follow-ups and a four-level rubric (poor, borderline, solid, outstanding) ([Google re:Work, n.d.](https://rework.withgoogle.com/intl/en/guides/a-guide-to-structured-interviewing-for-better-hiring-practices)). The origin of the STAR acronym (often attributed to DDI) and foundational papers by Janz (1982), Motowidlo et al. (1992) and Campion et al. (1997) were not verified in this research; no study tests STAR-formatted answers against unformatted ones.

### 3.12 AI writing help works for mechanics; generative tailoring loses signal and carries bias

**Evidence strength: STRONG (one large RCT); MODERATE (preprints, audits).**

In a randomised field experiment with **480,948 jobseekers**, non-generative, Grammarly-style writing assistance raised hires by about **8%**, concentrated among weaker writers, with no drop in employer satisfaction ([van Inwegen, Munyikwa & Horton, 2023](https://arxiv.org/pdf/2301.08083v1.pdf)). Generative AI is a different case. A 2025 preprint using Freelancer.com data finds that once AI made customised proposals nearly free, employers stopped paying for customisation, with counterfactuals of roughly **19% fewer high-ability hires** ([Galdin & Silbert, 2025](https://arxiv.org/abs/2511.08785)) [preprint; figures from secondary summaries]; another reports the correlation between cover-letter tailoring and callbacks fell 51% ([Cui et al., 2025](https://arxiv.org/html/2509.25054v1)) [preprint]. AI assistance makes individual writing better but collectively more similar ([Doshi & Hauser, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532)), in fiction rather than resumes. On the screening side, embedding-based resume retrieval disadvantaged Black male names in up to 100% of tests ([Wilson & Caliskan, 2024](https://arxiv.org/abs/2407.20371v2)), GPT-3.5 showed stereotype-consistent scoring and, when generating resumes, assigned women less experienced occupations ([Armstrong et al., 2024](https://arxiv.org/abs/2405.04412v3)) [preprint], and Bloomberg's audit found names distinct to Black Americans least likely to be ranked top for software engineer roles ([Bloomberg, 2024](https://prod.cm.bloomberg.com/graphics/2024-openai-gpt-hiring-racial-discrimination/)). No audit has tested Indian names, caste, region, college tier or services background, and no rigorous study measures how often AI resume tools fabricate achievements.

---

## 4. Discussion

### 4.1 What an effective resume looks like, by evidence strength

Assembling the findings yields a concrete picture. The table separates what is documented from what is convention.

| Element | Recommendation for a 2-3 YOE services-to-product switcher | Basis | Strength |
|---|---|---|---|
| Layout | Single column; no tables, text boxes, images, skill bars, icons, word art | Greenhouse failure list; Textkernel column data | MODERATE (vendor) |
| Contact | Name, phone, email, city, LinkedIn, GitHub as plain body text on the first lines | Greenhouse names header/footer/text-box contact as a failure | MODERATE (vendor) |
| File | Text-layer PDF or DOCX, under 2.5 MB, text selectable in correct order | Greenhouse, Lever format lists; Textkernel rendering | MODERATE (vendor) |
| Headings | Standard: Experience, Skills, Projects, Education; consistent formatting | Greenhouse "clear sections" | MODERATE (vendor); exact words are convention |
| Titles and employers | Full job titles, full legal employer names (e.g. "Pvt. Ltd."), no abbreviations | Greenhouse | MODERATE (vendor) |
| Dates | Month and year, one consistent format | Textkernel date handling; no vendor specifies a format | WEAK (convention) |
| Personal data | No photo, DOB, gender, marital status, father's name, religion, full address, declaration | IIT Madras, MIT, DPDP minimisation logic | WEAK-MODERATE |
| Length | One page preferred; two acceptable if page one holds the strongest evidence | Career centres; 2001 CPA study | WEAK |
| Order | Contact, optional 1-2 line headline, compact categorised skills, experience (main body), projects, education | Career centres; Lahey & Oxley on experience attention | WEAK; sources disagree (4.2) |
| Bullets | Outcome-first, action verb, named tech, method; at most two lines; quantify where defensible | Google X-Y-Z, Amazon, MIT, HKN | WEAK-MODERATE; outcome effect untested |
| Metrics | Technical proxies (latency, throughput, errors, coverage, users, cost), relative figures under NDA | HKN, Google, Amazon | WEAK-MODERATE |
| Keywords | Job description's exact technology names, in context in bullets and in skills; acronym plus expansion once | Greenhouse Boolean, Resdex, Textkernel taxonomy, MIT, Amazon | MODERATE |
| Client work | Real employer named; client described by industry and scale | Community; BGV inference | LOW |
| Proofreading | Zero spelling errors | Sterkens et al. and replications | STRONG-MODERATE |
| Education | Degree with exact CGPA or percentage, unrounded | IIT Madras rules; BGV | WEAK for laterals |
| Projects | One or two substantial, linked, discussable projects if work evidence is thin | Career centres; CSCW GitHub studies | WEAK-MODERATE |

### 4.2 Where sources disagree

**Skills placement and length.** The moderated developersIndia wiki puts Technical Skills before experience and says to "list all the skills you want to showcase" ([developersIndia wiki, n.d.](https://wiki.developersindia.in/community-guides/how-to-create-an-ideal-software-engineering-resume.html)), and one Hacker News candidate advises listing every technology because "recruiters have that stupid a heuristic". A Hacker News hiring manager wants work experience first, and another commenter criticises "repeating dozens of skills at the top ... with no storytelling" ([Hacker News, 2023](https://news.ycombinator.com/item?id=34609741)). Career centres split the difference: keep a Skills section and also show skills in context ([MIT CAPD, n.d.](https://capd.mit.edu/resources/resumes/)). Since recruiter Boolean search and Resdex cover all text, a compact, categorised, honest skills line plus in-context mentions satisfies both camps; an exhaustive dump adds keyword surface at the cost of credibility in the human read.

**Whether ATS formatting matters.** The developersIndia wiki calls "ATS-friendly" a misconception, arguing most systems just store applications and the real filter is a human keyword skim. Vendor documentation shows both halves are partly right: parsers rarely reject on format, but layout failures corrupt the candidate record recruiters search, especially contact fields. Formatting is cheap insurance against degraded data, not a defence against a mythical auto-reject.

**Projects.** Career centres treat projects as standard; experienced hiring managers on Hacker News say real experience supersedes them. For this candidate both can be true: projects matter when they supply evidence that services work cannot (modern stack, ownership, public code), and should give way as product-relevant work evidence accumulates.

**Level.** Community claims conflict on whether 2-3 services years map to SDE-1 or SDE-2, and postings straddle the boundary. A level-neutral resume that makes design ownership visible when it is real lets the same document serve both.

**Bullet formula.** X-Y-Z (result first), A-T-O-M (action first) and STAR/CAR variants share the structure of result, measure and method. No source shows one ordering beats another.

### 4.3 Commercially originated and unsupported claims

Several of the most repeated statistics in resume advice fail the source policy and lack primary support.

| Claim | Origin | Status |
|---|---|---|
| "75% of resumes are rejected by ATS" | 2012 press release from Preptel, a defunct resume-optimisation seller; no methodology published ([IT Brief UK, n.d.](https://itbrief.co.uk/story/study-reveals-ats-rarely-auto-rejects-cvs-debunks-75-myth); [Ask a Manager, n.d.](https://www.askamanager.org/?p=20209)) | Commercial, unverified; original not retrieved. Contradicted in mechanism by vendor docs showing failed parses go to manual entry. |
| "Recruiters spend 6 seconds" (2012) / "7.4 seconds" (2018) | Ladders, a job-board and career-services firm; about 30 recruiters reported for 2012, no headcount for 2018 ([HR Dive, 2018](https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/); [ERE, n.d.](https://www.ere.net/articles/is-the-6-second-resume-scan-a-myth)) | Commercial, unreplicated. The only peer-reviewed estimate is about 16 seconds with whole-resume reading. |
| "Recruiters 2.3× more likely to prefer two pages" | ResumeGo, a resume-writing seller ([Quartz, n.d.](https://qz.com/work/1520476/should-your-resume-be-one-page-or-two)) | Commercial, not peer-reviewed. |
| "99% of Fortune 500 use ATS" | Jobscan blog, repeated in an arXiv position paper ([Brown & Vaishampayan, 2025](https://arxiv.org/html/2504.06387v1)) | Commercial origin. |
| "Use DOCX; ATS can't read PDF"; "Workday 34% autofill error" | Resume-service blogs | Contradicted by vendor format lists; 34% has no traceable source. |
| "92% of recruiters confirm ATS do not auto-reject" | Attributed to HR.com, seen only via a resume site | Unverified even though it supports the vendor-doc picture. |
| "Up to 10% of resumes falsified per NASSCOM" | Vendor marketing | No primary source; do not use. |
| "Naukri headline is 18% of ranking" | Commercial resume sites | Unverified. |
| "Weave Amazon Leadership Principles into resume bullets" | Third-party guides | Amazon's own article mentions STAR only for interviews. |

The pattern is consistent: the scariest numbers sell optimisation services. The "6 seconds" figure is not wrong in spirit, since screening is fast under any estimate, but it misleads in suggesting screeners read only the top. Lahey and Oxley's evidence that screeners read everything and dwell on experience shifts the priority from above-the-fold tricks to experience-section substance.

### 4.4 Ticket and story counts are not inherently hollow

A common piece of advice treats counts such as "closed 120 tickets" or "delivered 17 user stories" as hollow. The researchers found **no employer, career-centre or peer-reviewed source that condemns them**; the community notes could not confirm the claim either. HKN explicitly lists "tickets closed" among business metrics ([HKN Illinois, 2025](https://wiki.hkn.illinois.edu/more%20advice/1.finding%20an%20internship/)), and Google's examples treat comparison counts as legitimate measures. The strongest argument against raw counts is a logical inference from the X-Y-Z and accomplishments-over-duties framing: a count measures volume of effort, while the formula asks for a measured outcome. Those positions reconcile cleanly. A count is a truthful measure of scope and throughput, which matters for a services engineer whose work was ticket-driven, and it becomes stronger when paired with an outcome (backlog cleared, SLA met, defect rate reduced) or context (team size, comparison to peers). A system should neither delete nor disparage such counts; it should keep them where they are the truthful measure and prompt for an outcome where one exists.

### 4.5 The signalling argument for evidence-first design

The AI evidence and the interview evidence point the same way. If generative tools make polished, tailored text free, tailoring loses signalling value (Galdin & Silbert; Cui et al.) and AI-polished bullets converge in phrasing (Doshi & Hauser, by analogy). What stays scarce is content that is specific, verifiable and deep: named systems, real numbers with baselines, links to code, and stories that survive Google's pre-set follow-ups and Amazon's "what you actually did". Indian BGV raises the cost of inflated titles and dates; structured interviews raise the cost of inflated actions and metrics. Non-generative help on mechanics, the one AI use with strong RCT support, also targets the best-evidenced resume defect, spelling errors, and its benefit is largest for weaker writers, which plausibly includes many second-language English writers. The design implication is not to avoid AI but to aim it at mechanics, structure, selection and keyword alignment, while keeping facts anchored to user-confirmed records.

---

## 5. Implications: requirements for the agent skills

The requirements below translate the findings into system behaviour. "Must" marks requirements grounded in documented mechanics, strong research, or the truthfulness constraint; "should" marks those grounded in convention or inference. Strength refers to the evidence behind the rationale.

### 5.1 Career record and capture

| ID | Requirement | Rationale | Strength |
|---|---|---|---|
| R1 | Must prompt for capture close to the event (per milestone, sprint or release, with at least quarterly review), not rely on annual reconstruction. | Autobiographical recall decays fast and is cued by what/who/where/when; under two-thirds of logged events recalled years later. | MODERATE |
| R2 | Must store each accomplishment with date or period, project and context, the user's own responsibility, the user's own actions, technologies used, outcome, collaborators, and evidence pointers (PRs, design docs, dashboards, tickets, emails). | Wagenaar cue structure; Evans' fields; BGV and interview probing require traceability. | MODERATE (cognition) / LOW (schema is synthesis) |
| R3 | Must separate individual contribution from team outcome in every record. | Amazon: "what you actually did"; services work is often described as "we". | MODERATE (employer) |
| R4 | Must support adding results later to an existing record (follow-up outcome after launch). | Evans: results often known months after launch. | LOW |
| R5 | Must store, for every number, its baseline, unit, source and confidence (measured, estimated, relative-only due to NDA). | Harvard "quantify and qualify"; UNC "real data"; numbers must survive interview probes. | WEAK-MODERATE |
| R6 | Must use neutral, evidence-anchored prompts ("what changed, by how much, how do you know, who else was involved?") rather than inviting adjectives or confidence. | Flawed self-assessment; gender gap in self-promotion persists without incentives. | STRONG-MODERATE |
| R7 | Must record client work under the real employer of record, with the client described by industry and scale and an NDA-sensitivity flag; must never substitute the client for the employer. | BGV verifies employer of record; community NDA practice. | LOW-MODERATE |
| R8 | Should capture SDE-2 signals explicitly as fields: design ownership, alternatives considered, reliability or scaling decisions, mentoring, code review, on-call and incident ownership. | Amazon and Flipkart posting requirements; design as reported differentiator. | WEAK-MODERATE |
| R9 | Must accept ticket, story and defect counts as legitimate measures, and should prompt for an associated outcome or context without labelling counts hollow. | No credible source condemns counts; HKN lists tickets closed. | WEAK |

### 5.2 STAR records and interview preparation

| ID | Requirement | Rationale | Strength |
|---|---|---|---|
| R10 | Must keep STAR records deeper than the resume bullet: obstacles, alternatives rejected, trade-offs, what failed, lessons, and what the user would do differently. | Structured interviews use pre-set follow-up probes and rubrics; Amazon asks for failures and lessons. | MODERATE-STRONG |
| R11 | Must link each resume bullet to its source STAR record, so every claim on a resume has an interview story behind it. | Interview probing of resume claims; Amazon and Google practice. | MODERATE |
| R12 | Should tag stories by competency (ownership, conflict, failure, ambiguity, scale, mentoring) and recency, and flag gaps in the story bank. | Amazon prefers recent situations; behaviour-description validity holds for complex jobs. | MODERATE |
| R13 | Must present STAR as a structuring aid, not a script to memorise. | Amazon: "not something to memorize". | MODERATE (employer) |

### 5.3 Resume generation and formatting

| ID | Requirement | Rationale | Strength |
|---|---|---|---|
| R14 | Must emit a single-column layout with no tables, text boxes, columns, images, icons, skill bars or word art, and contact details as plain body text at the top. | Greenhouse failure list; Textkernel column data. | MODERATE (vendor) |
| R15 | Must produce a text-layer PDF or DOCX under 2.5 MB and should verify that extracted text is complete and in reading order. | Greenhouse limits; Textkernel rendering-first pipeline. | MODERATE |
| R16 | Must use standard section headings, full job titles, full legal employer names, consistent month-year dates, and no letter-spaced text. | Greenhouse; Textkernel date handling. | MODERATE |
| R17 | Must exclude photo, DOB, gender, marital status, father's name, religion, full address, declaration, CTC and notice period from the resume by default. | IIT Madras; MIT; DPDP minimisation logic; CTC belongs in forms (inference). | WEAK-MODERATE |
| R18 | Should target one page and must place the strongest, most job-relevant evidence on page one; two pages only when the extra content is relevant. | Career centres; whole-resume reading but fast screening. | WEAK |
| R19 | Should write bullets as outcome plus measure plus method, at most two lines, with named technologies, without requiring a number in every bullet. | Google, Amazon, MIT, HKN, Columbia. | WEAK-MODERATE |
| R20 | Must run spelling and grammar checks and block output with detected spelling errors. | Sterkens et al.: 2 errors cost 7.3 points; non-generative assistance raised hires about 8%. | STRONG |
| R21 | Should preserve the user's concrete details and avoid stock verbs and phrasing that converge across AI-written resumes. | Homogenisation evidence (by analogy); Harvard warns AI output is generic. | WEAK |
| R22 | Should keep education with exact, unrounded CGPA or percentage, and render projects only when they are linked and the user can discuss them. | IIT Madras; developersIndia wiki; GitHub impression studies. | WEAK-MODERATE |

### 5.4 Job-description optimisation

| ID | Requirement | Rationale | Strength |
|---|---|---|---|
| R23 | Must tailor by selecting and reordering records from the master record and adjusting emphasis, not by rewriting the user's history per job. | MIT master resume; Amazon: no completely different resume per role. | WEAK-MODERATE |
| R24 | Must extract the job description's required and preferred technologies and use their exact names wherever the record shows genuine use, both in context in bullets and in the skills line. | Greenhouse Boolean search, Resdex, Amazon qualifications advice, MIT and Illinois. | MODERATE |
| R25 | Should write an acronym and its expansion once for key terms. | Literal Boolean search versus taxonomy normalisation. | MODERATE (vendor) / WEAK |
| R26 | Must report job-description requirements that the record does not support as gaps for the user, never insert them. | Truthfulness; keyword stuffing has no documented benefit and fails the human read. | MODERATE |
| R27 | Should keep the skills line compact and categorised, limited to skills the record evidences. | Community disagreement resolved toward credibility; career centres. | WEAK-LOW |
| R28 | Should keep the resume level-neutral and surface SDE-2 signals only when the record supports them. | Conflicting level evidence; posting requirements. | WEAK |
| R29 | Should generate a consistency check between the resume and the user's Naukri or LinkedIn profile fields (headline, designation, key skills, dates). | Resdex searches structured fields and freshness. | MODERATE (vendor) / inference |

### 5.5 Truthfulness guardrails

| ID | Requirement | Rationale | Strength |
|---|---|---|---|
| R30 | Must generate resume and interview content only from stored, user-confirmed records; must never add tools, scale, metrics, titles, dates or outcomes absent from the record. | BGV; structured-interview probing; signalling evidence; Evans "exactly as good as it is". | MODERATE |
| R31 | Must attach a provenance pointer from each generated claim to its source record and flag any number not present in the record for explicit user confirmation. | No measured fabrication rate exists for AI resume tools, so the safe default is verification. | MODERATE (by inference) |
| R32 | Must never fabricate or round up titles, employers, dates, CGPA or tenure, and must not count internships as professional experience. | IIT Madras no-rounding rule; Amazon "non-internship" wording; BGV. | MODERATE |
| R33 | Must not cite commercially originated statistics (75% ATS rejection, 6 seconds, DOCX-only) to the user as fact. | Section 4.3. | STRONG (that they lack support) |
| R34 | Should not put demographic signals on the resume beyond what is required, and should tell the user that AI screeners show name-based bias in audits whose transfer to Indian names is untested. | Wilson & Caliskan; Armstrong et al.; Bloomberg; no Indian audit. | MODERATE |

---

## 6. Limitations

**Inaccessible community sources.** Reddit and its mirrors could not be fetched, so the r/cscareerquestions wiki, the full r/EngineeringResumes wiki and r/developersIndia resume-review threads were not read; r/EngineeringResumes content appears only as mirror snippets and no frequency of advice could be counted. Community evidence in this report rests on the developersIndia wiki, one Hacker News thread, and low-engagement Blind and Fishbowl posts, several seen only through search summaries.

**Few Indian employer sources.** Apart from Amazon's India site, no Indian product company, startup or GCC was found publishing resume guidance, a career ladder, or a policy on photos, personal details or length. No lateral-hire guide from an Indian university career cell was retrievable; the IIT Madras rules govern campus resumes. Level evidence rests on posting copies hosted by aggregators, which may be stale.

**Geographic skew.** Most peer-reviewed findings come from the US and Europe: the eye-tracking study (US, clerical job, student-heavy sample), the spelling study (Belgium, vignettes), the length studies (US accounting and recreation), the self-promotion study (US), the AI-bias audits (US race categories), and *Hidden Workers* (US, UK, Germany). The only India-based resume audit for software jobs (Delhi) is from 2009. No study tested SWE recruiters, Indian screeners, services-versus-product employer brand effects, or AI screening bias on Indian names, caste, region or college tier.

**Unverified and prior-knowledge items.** Several studies were confirmed bibliographically but described from the researchers' prior knowledge and not re-read: Bertrand & Mullainathan (2004), Kang et al. (2016), Oreopoulos (2011), Kroft et al. (2013), Knouse (1994), Cole et al. (2003, 2009), Burns et al. (2014), Arnulf et al. (2010), Blackburn-Brockman & Belanger (2001), Schmidt & Hunter (1998), Singer et al. (2013), Behroozi et al. (2020), and parts of Marlow & Dabbish (2013). Others were read only through abstracts, snippets or secondary coverage: *Hidden Workers* figures, Lever and Workday documentation, the Galdin & Silbert and Cui et al. figures, the Journal of Cognition replication percentage, the Laszlo Bock attribution, Columbia and UNC guidance, and the employment-history viewing time in Lahey & Oxley. The publication venues of van Inwegen et al. (*Management Science*) and Armstrong et al. are unconfirmed, as is *Mobley v. Workday*'s status after January 2026. None of these should be quoted as verified without checking.

**Evidence gaps that matter for design.** There is no controlled evidence that quantified or achievement-oriented bullets raise callbacks, that GitHub links change callbacks, that brag documents improve career outcomes, that STAR-formatted answers score better than unstructured ones, or how often AI resume tools fabricate content. No independent parser benchmark exists, and Indian ATS parsers are undocumented. Market figures come from parties with an interest in strong demand. The requirements in Section 5 that rest on these gaps are labelled WEAK or as inferences and should be revisited as evidence appears.

**Synthesis limits.** This report synthesises research notes rather than primary sources directly; it inherits the notes' search budgets and any errors in their reading. Researcher inferences have been argued explicitly rather than presented as findings.

---

## 7. Conclusion

The evidence reframes the resume problem for a services-to-product switcher. The threat is not a robot rejecting PDFs; it is a fast human read, helped by keyword search and sometimes by AI ranking, that discounts generic scope. Formatting rules matter because they keep the candidate record intact, not because they defeat a filter, and they can be fully automated from vendor documentation. What cannot be automated is the scarce input: specific, attributable, measured accomplishments that hold up under background verification and structured follow-up questions. As generative AI makes polished, tailored text free, its signalling value falls, and the advantage moves to whoever holds the best-evidenced record.

That makes the career record, not the resume generator, the core of the system. A tool that captures work close to the event, asks neutral questions that counter memory decay and under-claiming, keeps provenance for every number, and refuses to write anything the record cannot support would produce resumes that are both more truthful and, on this evidence, more competitive. The open questions that deserve primary research are Indian-specific: how product and GCC screeners actually weigh services experience, how Indian ATS parsers behave, and whether AI screeners carry bias against Indian names, regions or college tiers.

---

## References

Sources are listed alphabetically by in-text citation key. Labels: ACADEMIC, VENDOR DOC, EMPLOYER, CAREER CENTRE, INDUSTRY DATA, LEGAL, PRESS, COMMUNITY (LOW), MIXED, COMMERCIAL (cited only to trace claim origins). Flags: [unverified], [prior knowledge], [preprint]. All URLs accessed 2026-11-07.

1. AMCIS SIG LEAD (2021). Ethnography of an Indian IT services firm. *AMCIS 2021 Proceedings*, IS Leadership and the IT Profession (SIG LEAD). https://aisel.aisnet.org/amcis2021/is_leadership/sig_lead/2 — ACADEMIC [abstract only]
2. Armstrong, L., Liu, A., MacNeil, S., & Metaxa, D. (2024). The Silicon Ceiling: Auditing GPT's race and gender biases in hiring. arXiv:2405.04412v3. https://arxiv.org/abs/2405.04412v3 — ACADEMIC [preprint; venue unverified]
3. Arnulf, J. K., Tegner, L., & Larssen, Ø. (2010). Impression making by résumé layout. *European Journal of Work and Organizational Psychology*, 19(2), 221–230. https://doi.org/10.1080/13594320902903613 — ACADEMIC [prior knowledge]
4. Ask a Manager (Green, A.) (n.d.). Discussion of the 75% ATS claim. https://www.askamanager.org/?p=20209 — PRESS/blog
5. Banerjee, A., Bertrand, M., Datta, S., & Mullainathan, S. (2009). Labor market discrimination in Delhi: Evidence from a field experiment. *Journal of Comparative Economics*, 37(1), 14–27. https://dspace.mit.edu/handle/1721.1/52303 — ACADEMIC
6. Bar & Bench (n.d.). Navigating legitimate use exemption for employee data under the DPDP Act 2023. https://www.barandbench.com/view-point/navigating-legitimate-use-exemption-employee-data-digital-personal-data-protection-act-2023 — LEGAL commentary
7. Bartoš, V., Bauer, M., Chytilová, J., & Matějka, F. (2016). Attention discrimination. *American Economic Review*, 106(6), 1437–1475. https://doi.org/10.1257/aer.20140571 — ACADEMIC [prior knowledge, via Lahey & Oxley]
8. Bertrand, M., & Mullainathan, S. (2004). Are Emily and Greg more employable than Lakisha and Jamal? *American Economic Review*, 94(4), 991–1013. https://doi.org/10.1257/0002828042002561 — ACADEMIC [prior knowledge]
9. Blackburn-Brockman, E., & Belanger, K. (2001). One page or two? *Journal of Business Communication*, 38(1), 29–57. https://doi.org/10.1177/002194360103800104 — ACADEMIC [prior knowledge]
10. Blind (2020). Switching to product-based companies as junior engineer (SDE-1). https://www.teamblind.com/post/switching-to-product-based-companiesgoogleamazonetc-as-junior-engineersde-1swe-1sre-dy8cdm6c — COMMUNITY (LOW)
11. Blind (2024). How to include high-profile client projects on your resume without violating NDAs. https://www.teamblind.com/post/how-to-include-high-profile-client-projects-on-your-resume-without-violating-ndas-jea26g4u — COMMUNITY (LOW)
12. Blind (n.d.-a). Stigma for having desi consultancies in resume. https://www.teamblind.com/post/stigma-for-having-desi-consultancies-in-resume-sldnoy5i — COMMUNITY (LOW) [snippet]
13. Blind (n.d.-b). Switch from service based company to FAANG. https://www.teamblind.com/post/switch-from-service-based-company-to-faang-cc36hrze — COMMUNITY (LOW) [snippet]
14. Bloomberg (2024). OpenAI's GPT is a recruiter's dream tool. Tests show there's racial bias. https://prod.cm.bloomberg.com/graphics/2024-openai-gpt-hiring-racial-discrimination/ ; code: https://github.com/BloombergGraphics/2024-openai-gpt-hiring-racial-discrimination — PRESS (data journalism) [author names unverified]
15. Brown, C., & Vaishampayan, S. (2025). Towards evidence-based tech hiring pipelines. arXiv:2504.06387. https://arxiv.org/html/2504.06387v1 — ACADEMIC [position paper]
16. Bunch, B. / Amazon India (n.d.-a). 4 ways to write your Amazon resume and nail your job application. https://www.aboutamazon.in/news/workplace/amazon-india-job-resume-tips — EMPLOYER
17. Bunch, B. / Amazon India (n.d.-b). 3 tips to ace your Amazon interview. https://www.aboutamazon.in/news/workplace/amazon-interview-success-tips — EMPLOYER
18. Business Insider India (2014). Google HR boss says this is the key to a perfect resume. https://www.businessinsider.in/google-hr-boss-says-this-is-the-key-to-a-perfect-resume/articleshow/43924179.cms — PRESS [unverified: snippet]
19. Business Insider India (2016). Majority of talent leaders in India want a push in hiring budgets, states LinkedIn survey. https://www.businessinsider.in/Majority-of-talent-leaders-in-India-want-a-push-in-hiring-budgets-states-LinkedIn-survey/articleshow/55559164.cms — PRESS
20. Civil Rights Litigation Clearinghouse (n.d.). Mobley v. Workday, Inc., No. 3:23-cv-00770 (N.D. Cal.). https://clearinghouse.net/case/44074/ — LEGAL
21. Cole, M. S., Feild, H. S., Giles, W. F., & Harris, S. G. (2009). Recruiters' inferences of applicant personality based on résumé screening. *Journal of Business and Psychology*, 24(1), 5–18. https://doi.org/10.1007/s10869-008-9086-9 — ACADEMIC [prior knowledge]
22. Cole, M. S., Rubin, R. S., Feild, H. S., & Giles, W. F. (2007). Recruiters' perceptions and use of applicant résumé information. *Applied Psychology*, 56(2), 319–343. https://doi.org/10.1111/j.1464-0597.2007.00288.x — ACADEMIC [biblio-verified; findings prior knowledge]
23. Columbia Center for Career Education (n.d.). Resumes with impact: Creating strong bullet points. https://www.careereducation.columbia.edu/resources/resumes-impact-creating-strong-bullet-points — CAREER CENTRE [search summary only]
24. Cui, J., Dias, ?, & Ye, ? (2025). Signaling in the age of AI: Evidence from cover letters. arXiv:2509.25054. https://arxiv.org/html/2509.25054v1 — ACADEMIC [preprint; coauthor names unverified]
25. Daxini, S. (2025). Graduates in India's Silicon Valley: Who gains in the knowledge economy? In *Higher Education and Work in the Knowledge Economy* (pp. 273–293). Springer. https://econpapers.repec.org/bookchap/sprsprchp/978-3-031-80618-6_5f12.htm — ACADEMIC [abstract only]
26. developersIndia wiki (n.d.). How to create an appealing software engineering resume. https://wiki.developersindia.in/community-guides/how-to-create-an-ideal-software-engineering-resume.html — COMMUNITY (LOW, moderated)
27. Doshi, A. R., & Hauser, O. P. (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. *Science Advances*, 10(28), eadn5290. https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532 — ACADEMIC
28. Dunning, D., Heath, C., & Suls, J. M. (2004). Flawed self-assessment. *Psychological Science in the Public Interest*, 5(3), 69–106. https://www.psychologicalscience.org/journals/pspi/j.1529-1006.2004.00018.x/ — ACADEMIC
29. ERE (n.d.). Is the 6-second resume scan a myth? https://www.ere.net/articles/is-the-6-second-resume-scan-a-myth — PRESS (trade)
30. Evans, J. (2019, June 28). Get your work recognized: Write a brag document. https://jvns.ca/blog/brag-documents/ — Practitioner (LOW, non-commercial)
31. Exley, C. L., & Kessler, J. B. (2022). The gender gap in self-promotion. *Quarterly Journal of Economics*, 137(3), 1345–1381. https://www.nber.org/papers/w26345 — ACADEMIC
32. Fernandez, M. (2018). *The New Frontier: Merit vs. Caste in the Indian IT Sector*. OUP. https://scholarcommons.scu.edu/faculty_books/386 — ACADEMIC
33. Fishbowl (n.d.). Is there any guarantee that our CV will definitely get shortlisted after getting referral? https://www.fishbowlapp.com/post/is-there-any-guarantee-that-our-cv-will-definitely-get-shortlisted-after-getting-referral-from-company-people-if-no-what — COMMUNITY (LOW) [snippet]
34. Fisher Phillips (2025). Discrimination lawsuit over Workday's AI hiring tools can proceed as class action. https://www.fisherphillips.com/en/news-insights/discrimination-lawsuit-over-workdays-ai-hiring-tools-can-proceed-as-class-action-6-things — LEGAL commentary
35. Fuller, J. B., Raman, M., Sage-Gavin, E., & Hines, K. (2021). *Hidden Workers: Untapped Talent*. Harvard Business School & Accenture. https://nahr.shrm.org/sites/default/files/hiddenworkers09032021.pdf — ACADEMIC/industry report [figures via secondary coverage]
36. Galdin, A., & Silbert, J. (2025). Making talk cheap: Generative AI and labor market signaling. arXiv:2511.08785. https://arxiv.org/abs/2511.08785 — ACADEMIC [preprint; figures from secondary summaries]
37. Google re:Work (n.d.). Guide: Use structured interviewing. https://rework.withgoogle.com/intl/en/guides/a-guide-to-structured-interviewing-for-better-hiring-practices — EMPLOYER
38. Greenhouse (2026a, March 2). Unsuccessful resume parse. https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse — VENDOR DOC
39. Greenhouse (2026b, August 19). Supported formats for resumes, cover letters and other candidate uploads. https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-file-types-for-resumes-and-cover-letters — VENDOR DOC
40. Greenhouse (n.d.-a). Search candidates using Boolean queries. https://support.greenhouse.io/hc/en-us/articles/202360199-Search-candidates-using-Boolean-queries — VENDOR DOC [snippet]
41. Greenhouse (n.d.-b). Auto-Reject for prospect post. https://support.greenhouse.io/hc/en-us/articles/360029081512-Auto-Reject-for-prospect-post — VENDOR DOC [snippet]
42. Hacker News (2023, February 1). Ask HN: Reject/ghost on all job applications with 8 YoE, what am I doing wrong? https://news.ycombinator.com/item?id=34609741 — COMMUNITY (LOW)
43. Harvard FAS Mignone Center for Career Success (n.d.). Harvard College guide to creating a strong resume. https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/ — CAREER CENTRE
44. HKN mentoring team, University of Illinois (2025, April 16). Finding an internship. https://wiki.hkn.illinois.edu/more%20advice/1.finding%20an%20internship/ — CAREER CENTRE (student society)
45. HR Dive (2018). Eye-tracking study shows recruiters look at resumes for 7 seconds. https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/ — PRESS (reporting COMMERCIAL Ladders study)
46. Huffcutt, A. I., Conway, J. M., Roth, P. L., & Klehe, U.-C. (2004). The impact of job complexity and study design on situational and behavior description interview validity. *International Journal of Selection and Assessment*, 12(3), 262–273. https://jlupub.ub.uni-giessen.de/items/043303fd-a40c-4e1f-abc4-3f0f01f78584 — ACADEMIC [abstract level]
47. IIT Madras Career Development Cell (2025). Internship resume guidelines 2025-26. https://internship.iitm.ac.in/downloads/Internship_Resume_Guidelines_2025-26.pdf — CAREER CENTRE
48. IT Brief UK (n.d.). Study reveals ATS rarely auto-rejects CVs, debunks 75% myth. https://itbrief.co.uk/story/study-reveals-ats-rarely-auto-rejects-cvs-debunks-75-myth — PRESS (trade)
49. Jointaro mirror of Amazon SDE II posting (n.d.). https://www.jointaro.com/jobs/amazon/software-development-engineer-ii-981d2be4 ; apna.co Amazon India SDE II listing: https://apna.co/job/bengaluru/software-dev-engineer-ii-1921035727 — EMPLOYER posting via aggregator
50. Journal of Cognition (n.d.). Replication of Wagenaar's autobiographical memory diary study. https://journalofcognition.org/en/articles/10.5334/joc.334 — ACADEMIC [snippet-level; verify figures]
51. Kula (n.d.). Auto-rejection rules and knockout questions. https://support.kula.ai/articles/7962068559-auto-rejection-rules-and-knockout-questions — VENDOR DOC
52. Lahey, J. N., & Oxley, D. R. (2021). Discrimination at the intersection of age, race, and gender: Evidence from an eye-tracking experiment. *Journal of Policy Analysis and Management*, 40(4), 1083–1119. NBER w25357: https://www.nber.org/papers/w25357.pdf — ACADEMIC
53. LeetCode Discuss (2026, January). Flipkart SDE-2 interview experience. https://leetcode.com/discuss/post/8455829/flipkart-sde-2-interview-experience-jan-o8ngx/ — COMMUNITY (LOW)
54. Lever (n.d.). Understanding resume parsing. https://help.lever.co/hc/en-us/articles/20087345054749 — VENDOR DOC [unverified: snippet]
55. Levashina, J., Hartwell, C. J., Morgeson, F. P., & Campion, M. A. (2014). The structured employment interview. *Personnel Psychology*, 67(1), 241–293. https://digitalcommons.usu.edu/manage_facpub/423/ — ACADEMIC
56. Marlow, J., & Dabbish, L. (2013). Activity traces and signals in software developer recruitment and hiring. *CSCW '13*, 145–156. https://bibtex.github.io/CSCW-2013-MarlowD.html ; related: https://par.nsf.gov/servlets/purl/10357418 — ACADEMIC [biblio-verified; findings partly prior knowledge]
57. Marlow, J., Dabbish, L., & Herbsleb, J. (2013). Impression formation in online peer production. *CSCW '13*, 117–128. https://par.nsf.gov/servlets/purl/10038300 — ACADEMIC
58. Martin-Lacroux, C., & Lacroux, A. (2017). Do employers forgive applicants' bad spelling in résumés? *Business and Professional Communication Quarterly*, 80(3), 321–335. https://doi.org/10.1177/2329490616671310 — ACADEMIC [via Sterkens et al.]
59. MIT Career Advising & Professional Development (n.d.). Resumes. https://capd.mit.edu/resources/resumes/ — CAREER CENTRE
60. Mondaq (2025). Digital Personal Data Protection Rules 2025 notified. https://www.mondaq.com/india/data-protection/1708164/digital-personal-data-protection-rules-2025-notified — LEGAL commentary
61. National Skills Registry (NASSCOM/NSDL) (n.d.). Home page. https://nationalskillsregistry.com/ — INDUSTRY (official registry)
62. Naukri (n.d.-a). What is the significance of keyword search in Resdex. https://naukricom.freshdesk.com/support/solutions/articles/228261-what-is-the-significance-of-keyword-search-in-resdex- — VENDOR DOC
63. Naukri (n.d.-b). Recruiter Resdex. https://www.naukri.com/blog/recruiter-resdex/ — VENDOR DOC
64. Naukri (n.d.-c). Resume template. https://company.naukri.com/landing-page/snp/resume-template.doc — VENDOR [snippet, LOW]
65. Naukri JobSpeak (2025, November). Info Edge. https://www.infoedge.in/pdfs/News_Events_pdfs/Naukri-Jobspeak-Nov-2025.pdf — INDUSTRY DATA (job board)
66. NewsBytes (2026). NASSCOM-Zinnov: GCCs in India employ 2.36 million, plan 3.5 million by 2030. https://www.newsbytesapp.com/news/business/nasscom-zinnov-gccs-in-india-employ-236-million-plan-35-million-by-2030/tldr — PRESS (reporting INDUSTRY DATA)
67. Quartz (n.d.). Should your resume be one page or two? https://qz.com/work/1520476/should-your-resume-be-one-page-or-two — PRESS (reporting COMMERCIAL ResumeGo study)
68. SCC Online (2025, November 14). MeitY notified Digital Personal Data Protection Rules 2025. https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/ — LEGAL commentary
69. Sterkens, P., Caers, R., De Couck, M., Van Driessche, V., Geamanu, M., & Baert, S. (2023). Costly mistakes: Why and when spelling errors in resumes jeopardise interview chances. *PLOS ONE*, 18(4), e0283280. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283280 — ACADEMIC
70. Tay, Y. (n.d.). Resume. *Tech Interview Handbook*. https://www.techinterviewhandbook.org/resume/ — MIXED (free content with affiliate links)
71. Textkernel (n.d.-a). Improving extraction from column resumes. https://textkernel.com/learn-support/blog/improving-extraction-from-column-resumes — VENDOR DOC
72. Textkernel (n.d.-b). Tx Platform v10 FAQ. https://developer.textkernel.com/tx-platform/v10/faq/ — VENDOR DOC
73. Textkernel (n.d.-c). Skills API overview. https://developer.textkernel.com/tx-platform/v10/skills-intelligence/skills-api/overview/ — VENDOR DOC
74. The Register (2021, September 8). Harvard jobs report. https://www.theregister.com/2021/09/08/harvard_jobs_report/ — PRESS
75. The Week / PTI (2026, February 24). India FY26 tech revenues seen 6.1 pc up at USD 315 bn, jobs also grow: Nasscom. https://www.theweek.in/wire-updates/business/2026/02/24/india-fy26-tech-revenues-seen-6.1-pc-up-at-usd-315-bn-jobs-also-grow-nasscom.amp.html — PRESS (reporting INDUSTRY DATA)
76. Umoh, R. / CNBC Make It (2018, August 16). A Google recruiter shares the winning 3-part formula for resumes that get noticed. https://www.cnbc.com/2018/08/16/google-recruiters-share-the-3-part-formula-for-stronger-resumes.html — EMPLOYER (via press)
77. Upadhya, C. (2007). Employment, exclusion and "merit" in the Indian IT industry. *Economic & Political Weekly*. https://cms.nias.res.in/node/2459 — ACADEMIC [bibliographic record only]
78. van Inwegen, E., Munyikwa, Z., & Horton, J. J. (2023). Algorithmic writing assistance on jobseekers' resumes increases hires. NBER WP 30886; arXiv:2301.08083. https://arxiv.org/pdf/2301.08083v1.pdf — ACADEMIC [Management Science publication unverified]
79. van Toorenburg, M., Oostrom, J. K., & Pollet, T. V. (2015). What a difference your e-mail makes. *Cyberpsychology, Behavior, and Social Networking*, 18(3), 135–140. https://doi.org/10.1089/cyber.2014.0542 — ACADEMIC [via Sterkens et al.]
80. Wagenaar, W. A. (1986). My memory: A study of autobiographical memory over six years. *Cognitive Psychology*, 18, 225–252. https://link.springer.com/content/pdf/10.3758/BF03211313.pdf — ACADEMIC [abstract/secondary]
81. weekday.works (n.d.). Flipkart Software Development Engineer II (SDE-2) listing. https://jobs.weekday.works/flipkart-software-development-engineer-ii-(sde-2) — EMPLOYER posting via aggregator (LOW)
82. Wilson, K., & Caliskan, A. (2024). Gender, race, and intersectional bias in resume screening via language model retrieval. *Proceedings of AIES*, 7, 1578–1590. https://arxiv.org/abs/2407.20371v2 — ACADEMIC
83. Workable (n.d.). Knockout questions. https://help.workable.com/hc/en-us/articles/115012238688 — VENDOR DOC
84. Workday (n.d.). Admin guide: Set up prospects and candidates. https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/candidates/set-up-prospects-and-candidates/hdc1552497830785.html — VENDOR DOC [unverified: login-gated, snippet]

# ATS Parsing, Storage, Search and Ranking Mechanics, and What They Imply for a SWE Resume (India focus)

Access date for all sources: 2026-11-07, unless stated otherwise. Source labels:
- **[VENDOR DOC]**: ATS or parser vendor documentation. These vendors sell to employers, not candidates.
- **[ACADEMIC]**: peer-reviewed or university research.
- **[LEGAL]**: court records, or law-firm summaries of them.
- **[COMMERCIAL / UNVERIFIED]**: resume-builder, ATS-checker or career-service content, cited only so a claim can be traced to where it came from.
- **[LOW]**: community or aggregator content.

Research budget note: about 20 search and fetch calls. Several primary pages could not be retrieved: the Lever help article (CSS error), the HBS Working Knowledge page (HTTP 403) and Workday's admin guide (login-gated). Where a finding rests on a search snippet rather than a full page read, it says so.

## 1. Which ATS platforms are used by Indian product companies, startups and MNC GCCs?

### Takeaway
No reliable, independent market-share data exists for ATS use in India. The landscape is split roughly like this:
- Global enterprise suites (Workday, SAP SuccessFactors, Oracle Taleo/Recruiting, iCIMS) are typical of MNC offices and GCCs.
- Greenhouse and Lever are typical of global-first product companies and funded startups.
- Indian HRMS/ATS products (Darwinbox, Keka, Zoho Recruit, Naukri RMS) serve Indian mid-market and enterprise employers.
- Job portals (Naukri Resdex, LinkedIn) act as a parallel searchable resume database.

### Cited Findings
- The search found no reliable ATS market-share figures for India. Comparison pages are vendor-run or affiliate content. — Zappyhire (an ATS vendor), "Top 10 Applicant Tracking System (ATS) in India for 2026", https://www.zappyhire.com/blog/top-applicant-tracking-system-ats-in-india [VENDOR MARKETING, LOW]
- **Naukri RMS** is Info Edge's recruitment management system, introduced in 2014. Its customer list includes IndusInd Bank and Lupin, and its customers are concentrated in India and the UAE. — Apps Run The World, "List of Naukri RMS Customers", https://www.appsruntheworld.com/customers-database/products/view/naukri-rms/name/asc/10/1 [market-intelligence vendor, MEDIUM-LOW]
- **Darwinbox**: iDataLabs tracks 315 companies using Darwinbox, which is about 0.1% of the broader enterprise HR-management category, not ATS specifically. About 56% of those customers are in India. — iDataLabs, "Companies using Darwinbox", https://www.idatalabs.com/tech/products/darwinbox [market-intelligence vendor, MEDIUM-LOW]
- A uncorroborated claim that Naukri RMS has "15,000+ companies in India" comes from a resume-builder site and has no source. — stylingcv.com (Hindi-language page) [COMMERCIAL / UNVERIFIED]. Do not use.
- **Workday** documents a resume-parsing feature that creates a prospect or job application from an attached resume. Admins can configure application templates to hide resume parsing for external candidates, so autofill is optional per employer. — Workday, Admin Guide, "Set Up Prospects and Candidates", https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/candidates/set-up-prospects-and-candidates/hdc1552497830785.html (search snippet only; login-gated) [VENDOR DOC]
- Workday career-site resume autofill fails at times. A university Workday tenant posted an incident titled "Resolved – Resume Parsing On The Career Site Is Not Functional". — University of Nevada Workday status page, https://workday.nevada.edu/resume-parsing-on-the-career-site-is-not-functional/ [employer IT notice, MEDIUM]
- **Naukri Resdex** is a recruiter-side searchable resume database. Recruiters can use mandatory keywords, keywords in various resume fields, designation, institute name, and "resume freshness" (when the candidate was last active). — Naukri Recruiter FAQ, "What is the significance of keyword search in Resdex", https://naukricom.freshdesk.com/support/solutions/articles/228261-what-is-the-significance-of-keyword-search-in-resdex- ; Naukri Blog, "Recruiter Resdex", https://www.naukri.com/blog/recruiter-resdex/ ; Naukri, "Resdex FAQ", https://www.naukri.com/faq/recruiter-resdex [VENDOR DOC, Naukri sells Resdex to recruiters]
- Naukri's own blog says that more recently updated profiles are more likely to appear at the top of Resdex search results. — Naukri Blog, "Recruiter Resdex", https://www.naukri.com/blog/recruiter-resdex/ (via search snippet) [VENDOR DOC]

### Inferences
- An India job switcher's resume is likely to pass through two quite different systems:
  - an employer ATS (Workday, Greenhouse, Lever, Darwinbox and others), where it is parsed into a candidate record and searched by recruiters;
  - Naukri and LinkedIn, where the structured profile fields and keywords matter more than the uploaded file and recency affects ranking.
- Rules should therefore target the lowest common denominator parser and should not be tuned to a single ATS.
- Employer career-site URLs give an independent way to identify the ATS: `*.myworkdayjobs.com`, `boards.greenhouse.io` / `job-boards.greenhouse.io`, `jobs.lever.co`, `*.darwinbox.in`, `*.zohorecruit.in`, `*.keka.com/careers`. I did not verify a sample of Indian GCC URLs in this budget.

### Gaps
- No independent, quantitative ATS market-share data for India, whether by employer type (GCC vs product company vs startup) or overall. Customer lists from Workday, SuccessFactors, Darwinbox and Keka were not retrieved.
- I found no technical documentation on parsers for Darwinbox, Keka, Zoho Recruit, SmartRecruiters, iCIMS or SuccessFactors.
- I found no Naukri documentation on how its resume parser fills profile fields or how ranking is weighted. Claims such as "headline is 18% of ranking" exist only on commercial resume sites and are unverified.

## 2. What do vendor docs say about parsing: file types, layout elements, field extraction and failure modes?

### Takeaway
Vendor documentation agrees on four points:
1. PDF and DOCX are both supported everywhere.
2. Image-only files, scanned files and files without a text layer do not parse.
3. Columns, tables, text boxes and headers/footers are documented failure causes. Contact details placed in a header, footer or text box are a named failure.
4. Parse failures fall back to manual entry. The resume file is still attached, so the outcome is degraded data, not automatic rejection.

The single most specific primary source is Greenhouse's "Unsuccessful resume parse" article.

### Cited Findings
**Greenhouse [VENDOR DOC]**
- Supported upload types for resumes, cover letters and attachments are .doc, .docx, .pdf, .rtf and .txt, with a 100 MB maximum per file. Externally linked images are not shown when Greenhouse converts a resume to PDF for preview. — Greenhouse Support, "Supported formats for resumes, cover letters and other candidate uploads", last updated 2026-08-19, https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-file-types-for-resumes-and-cover-letters
- "Greenhouse Recruiting can't parse resumes larger than 2.5MB." The 100 MB upload limit and the 2.5 MB parse limit are different numbers. — Greenhouse Support, "Unsuccessful resume parse", last updated 2026-03-02, https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse
- The same article lists these formatting causes of failed or partial parses (verbatim):
  - "Resumes that include graphics, photos, or word art"
  - "Resumes that are uploaded as an image, rather than a document (such as a .docx or .pdf)"
  - "Complex resumes with tables, headers, and footers"
  - "Resumes with the name and contact information in the header, footer, or text box"
  - "Resumes that have a columned layout"
  - "A resume with spaces between the letters."
  - "Resumes without clear sections and differing formats throughout each section"
  - "Company names that don't include identifying words such as Inc., Co., LTD, or LLC."
  - "Resumes with incomplete job titles. For example, Sr. Account Exec instead of Senior Account Executive"

  — Greenhouse Support, "Unsuccessful resume parse", 2026-03-02, https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse
- Consequence of a failure: these issues "may result in a partial resume parse that will need to be manually corrected and verified". On a full failure, "you'll need to manually input the candidate's details into the fields". — same source. The recruiter still has the file. Nothing in the article says failed parses are rejected.

**Lever [VENDOR DOC, from search snippet; the page did not render when fetched]**
- Accepted formats: Microsoft Word (including .docx), Adobe PDF, RTF, Corel WordPerfect, HTML, MS Office HTML and OpenDocument. The parser extracts name, organization and contact details into the candidate profile. Failed parses can be corrected by typing into profile fields. — Lever Help Center, "Understanding Resume Parsing", https://help.lever.co/hc/en-us/articles/20087345054749 ; older version: https://lever-old.zendesk.com/hc/en-us/articles/360056337151
- Lever's older help page suggests converting scanned documents into a supported text format. The claimed 10 MB file cap and "Lever prefers DOCX" claim appear only on third-party sites. — [COMMERCIAL / UNVERIFIED], e.g. jobshinobi.com, jobscan.co. The DOCX-preference claim is not supported by the official format list.

**Workday [VENDOR DOC + COMMERCIAL]**
- The official documentation confirms only that the parsing feature exists and that employers can configure it (see Q1).
- The accepted-types list of DOC, DOCX, HTML, PDF and TXT, the "34% autofill error rate" and the "Workday prefers DOCX" advice all come from resume-service blogs. — e.g. tealhq.com, resumegeni.com, atsverification.com [COMMERCIAL / UNVERIFIED]. The 34% figure has no traceable source.

**Textkernel, formerly Sovren, a major parsing engine licensed into many ATSs [VENDOR DOC]**
- Claims "over 95% accuracy for the most critical data points" for its standard parser. Says its LLM Parser reduces remaining errors "by up to 30%" at higher cost and latency. Claims "Essentially any resume and CV format" is supported, but compressed files are not. — Textkernel, "Tx Platform v10 FAQ", https://developer.textkernel.com/tx-platform/v10/faq/ (no independent validation of the accuracy figure)
- Date interpretation depends on the document's "last modified" date. Without it, "the latest experience on old resumes will be interpreted as current". — same source. Dates are parsed relative to a reference date, so "Present" or "Current" is interpreted, not taken literally.
- Column layouts:
  - Text rendering (PDF to text) is the first step. Errors there flow into every later step.
  - Naive top-to-bottom, left-to-right rendering mixes text from different columns.
  - Textkernel estimates that at least 15% of CVs use columns.
  - Its old rule-based column detector found only 60% of column separators. The new gradient-boosted model finds 82%, and overall gap decisions went from 82% to 91% correct.
  - Well-rendered CVs rose from 62% to 90% on about 700 CVs.
  - Contact-info fill rates rose 4 to 10 points absolute. Contact details (name, phone, address) were the fields most hurt by column mixing.
  - Splitting every large gap would break key–value layouts and separate labels from their values.

  — Textkernel blog, "Improving extraction from column resumes", undated (© 2026 page), https://textkernel.com/learn-support/blog/improving-extraction-from-column-resumes
- Textkernel's LLM Parser is described as handling "document conversion to text and HTML, as well as handling column layouts". — Tx Platform v10 FAQ (above)

**Indeterminate / not found**
- No Daxtra, HireAbility, RChilli or Affinda technical documentation was retrieved within budget.

### Inferences
- **Columns** are a documented risk even for the most advanced engine. Even after Textkernel's improvement, about 1 in 5 column separators is still missed and about 10% of CVs render badly. Older or cheaper parsers are likely worse. A single-column layout removes this risk entirely.
- **Contact details** should go in the document body as plain text at the top, not in a Word header, footer or text box. Greenhouse names this explicitly, and Textkernel shows contact info is the field most damaged by layout problems.
- **PDF vs DOCX**: both are officially supported by Greenhouse, Lever and Workday. The rule that matters is "a PDF with a real text layer, exported from a word processor or LaTeX, never scanned or flattened to an image". The often-repeated "always use DOCX" advice comes from commercial sources and is not in vendor documentation.
- **File size**: keep it under 2.5 MB because of the Greenhouse parse limit. Avoid embedded photos, which also matches the Greenhouse "graphics, photos" cause.
- **Job titles**: spell them out ("Senior Software Engineer", not "Sr. SWE"). Use standard section headings (Experience, Education, Skills). Keep formatting consistent within each section. Each of these maps to a Greenhouse-listed cause.
- **Letter spacing**: do not letter-space headings, for example "E X P E R I E N C E". Greenhouse lists "spaces between the letters" as a cause.

### Gaps
- Vendor documentation on icons, fonts and ligatures, PDF tagging (accessibility tags) and specific date formats was not found. Whether tagged PDFs parse better than untagged PDFs that have a text layer is undocumented in the sources reviewed.
- No independent (non-vendor) benchmark of parser accuracy was found.

## 3. Do ATSs auto-reject by keyword score, or do recruiters search and filter? Where does the "75%" claim come from? What does research say?

### Takeaway
Documented ATS behaviour is mainly a database plus workflow:
- resumes are parsed, stored and searched or filtered by recruiters;
- automatic rejection is mostly driven by employer-configured knockout or screening questions, not by a hidden keyword score on the resume.

The "75% rejected by ATS" figure traces to a 2012 marketing claim by Preptel, a company that sold resume-optimization services to job seekers. No methodology was ever published, so it should be treated as commercially motivated and unverified.

Large-scale automated filtering and AI ranking do exist and are the subject of research and litigation:
- The HBS/Accenture "Hidden Workers" report (2021) found more than 90% of employers use such systems to filter or rank candidates, largely with "negative" filters such as degree or employment gaps.
- Mobley v. Workday (US) is testing AI scoring and ranking in court.

### Cited Findings
**Origin of the "75%" claim**
- The claim traces to a 2012 Preptel press release saying 75% of resumes were rejected by ATS after testing 10,000 resumes. Preptel sold resume-optimization services to job seekers and shut down around 2013 without publishing methodology. — secondary accounts only:
  - IT Brief UK, "Study reveals ATS rarely auto-rejects CVs, debunks 75% myth", https://itbrief.co.uk/story/study-reveals-ats-rarely-auto-rejects-cvs-debunks-75-myth [trade press, MEDIUM]
  - Ask a Manager (Alison Green), https://www.askamanager.org/?p=20209 [practitioner blog, LOW-MEDIUM]
  - Lenz.io claim analysis, https://lenz.io/c/ats-applicant-tracking-system-75-percent-rejection-rate-bc6fd7d4 [fact-check aggregator, LOW-MEDIUM]

  I could not retrieve the original 2012 Preptel release, so this attribution rests on consistent secondary accounts.
- The "75%" figure is now mainly repeated by resume-builder and ATS-checker vendors, which have a commercial interest in it. — e.g. rezi.ai, davron.net [COMMERCIAL / UNVERIFIED]
- A separate 2012 claim that ATSs screen out "half" of resumes is attributed to John Sullivan (San Francisco State University). I did not verify it. — via secondary search results [UNVERIFIED]
- A survey headline reported as "92% of recruiters confirm ATS do not automatically reject resumes" is attributed to HR.com. I saw it only through resumegeni.com, a commercial resume site, and could not verify it. — [COMMERCIAL / UNVERIFIED]. Note: an Enhancv recruiter survey on the same theme also circulates, but Enhancv is a resume builder and is excluded under the source policy.

**Independent research on automated screening**
- *Hidden Workers: Untapped Talent* (Fuller, J.B., Raman, M., Sage-Gavin, E., Hines, K.; Harvard Business School Project on Managing the Future of Work & Accenture, September 2021):
  - surveyed 8,720 "hidden workers" and 2,275 executives in the US, UK and Germany;
  - more than 90% of employers surveyed use their ATS or RMS to initially filter or rank potential middle- and high-skills candidates;
  - these systems rely heavily on "negative" filters, such as no degree or a gap of more than 6 months, rather than "affirmative" filters for skills;
  - recommends switching to affirmative filters.

  — PDF hosted by SHRM: https://nahr.shrm.org/sites/default/files/hiddenworkers09032021.pdf ; HBS Working Knowledge summary, "How to Tap the Talent Automated HR Platforms Miss", https://hbswk.hbs.edu/item/how-to-tap-the-talent-automated-hr-platforms-miss ; The Register, 2021-09-08, https://www.theregister.com/2021/09/08/harvard_jobs_report/ [ACADEMIC / industry co-authored, HIGH for prevalence of filtering; figures taken from secondary coverage and search snippets because the PDF was not read in full]. Note: 2021 data from the US, UK and Germany, not India.
- Raghavan, M., Barocas, S., Kleinberg, J., Levy, K. (2020). "Mitigating Bias in Algorithmic Hiring: Evaluating Claims and Practices." *Proceedings of ACM FAT\* 2020* (Conference on Fairness, Accountability, and Transparency), pp. 469–481. arXiv:1906.09208, https://arxiv.org/abs/1906.09208 ; SSRN https://papers.ssrn.com/abstract=3408010 [ACADEMIC, HIGH]
  - Reviewed public claims by vendors of algorithmic pre-employment assessment and documented what they disclose about how they build and validate models.
  - Vendors define "bias" differently and mitigate it differently.
  - Scope: assessments such as games, video interviews and questionnaires, more than resume parsing. It shows that ranking and scoring tools exist and are opaque, not that ATS resume parsers auto-reject.

**Litigation evidence that AI scoring and ranking is used [LEGAL]**
- *Mobley v. Workday, Inc.* (N.D. Cal., No. 3:23-cv-00770, Judge Rita Lin):
  - 2025-05-16: preliminary collective certification under the ADEA (applicants aged 40 and over) on the theory that Workday's AI recommendation system applied a common policy.
  - July 2025: the court extended the collective's scope to applicants whose applications were "scored, sorted, ranked, or screened" using HiredScore AI features, and ordered Workday to list customers that enabled those features (deadline 2025-08-20).
  - Workday calls this a "preliminary, procedural ruling … that relies on allegations, not evidence".

  — Civil Rights Litigation Clearinghouse, https://clearinghouse.net/case/44074/ ; Court order (Dkt. 158), https://storage.courtlistener.com/recap/gov.uscourts.cand.408645/gov.uscourts.cand.408645.158.0.pdf ; Fisher Phillips, https://www.fisherphillips.com/en/news-insights/discrimination-lawsuit-over-workdays-ai-hiring-tools-can-proceed-as-class-action-6-things. The case status after January 2026 was not verified, and allegations are not findings.

**Documented auto-rejection mechanism [VENDOR DOC]**
- Greenhouse "Application Rules" can automatically reject based on a candidate's answer to a configured question. Example from the documentation: Auto-Reject for prospect posts, with conditions combined by AND/OR. — Greenhouse Support, "Auto-Reject for prospect post", https://support.greenhouse.io/hc/en-us/articles/360029081512-Auto-Reject-for-prospect-post (search snippet)
- Other ATS vendors document knockout questions in the same way. Rules are evaluated in order and the first match determines the outcome.
  - Kula: unanswered knockout questions do not reject.
  - Workable: knockouts only on Yes/No questions.
  - join-dev: deliberately flags candidates instead of rejecting them.

  — Kula Support, https://support.kula.ai/articles/7962068559-auto-rejection-rules-and-knockout-questions ; Gem Help, https://help.gem.com/databases/gem-help-center/gem-ats-knockout-questions ; Workable Help, https://help.workable.com/hc/en-us/articles/115012238688 ; join-dev, https://join-dev.com/en/features/screening [VENDOR DOC]

### Inferences
- The defensible model is as follows.
  - **Automatic rejection** mostly comes from:
    - answers to knockout questions (work authorization, notice period, location, years of experience, expected CTC);
    - hard filters on parsed or structured fields (degree, experience gaps), as documented by Hidden Workers.
  - **Ranking** comes from:
    - AI scoring layers (Workday HiredScore, Darwinbox's "AI-driven" matching, Textkernel matching) that some employers turn on;
    - recruiter keyword searches.
- There is no documented evidence that a standard ATS throws away resumes because of a keyword-density score. AI-ranking layers do exist, though, so a resume that names the job's exact required skills is still more likely to rank well.
- For India specifically: knockout fields such as notice period, current and expected CTC, and preferred location are common on Indian application forms. This is not documented in the sources above. Answering them accurately and consistently with the resume matters more than formatting tricks.

### Gaps
- No India-specific empirical study of automated resume screening or rejection rates was found.
- No primary copy of the 2012 Preptel claim was retrieved.
- The HR.com "92%" survey was not verified at the primary source.
- How often Indian employers turn on AI ranking (HiredScore, Darwinbox AI) is unknown.

## 4. How do knockout questions, recruiter boolean searches and skill taxonomies interact with keyword choice?

### Takeaway
Recruiters run Boolean or keyword searches over the parsed and full resume text:
- Greenhouse full-text search with AND and wildcards;
- Naukri Resdex mandatory keywords, which search across resume fields.

Parsing engines normalize skills against taxonomies that map synonyms and acronyms to one concept (Textkernel: about 12–13k skills, 250–300k synonyms). Taxonomy normalization helps semantic matching, but literal Boolean search does not expand synonyms reliably. Writing both the exact technology name and the common acronym/expansion therefore covers both paths.

### Cited Findings
- Greenhouse documents Boolean candidate search through a "Full Text Search" toggle on the All Candidates page, with AND and wildcard operators. Wildcards match variations such as plurals. It also documents keyword search of resumes from the left panel. — Greenhouse Support, "Search candidates using Boolean queries", https://support.greenhouse.io/hc/en-us/articles/202360199-Search-candidates-using-Boolean-queries ; "Search resumes for keywords", https://support.greenhouse.io/hc/en-us/articles/115004600186-Search-resumes-for-keywords (search snippets) [VENDOR DOC]
- Naukri Resdex supports structured keyword types (including mandatory keywords). The keyword field searches "various fields of a resume", and recruiters can also filter by designation, institute and freshness. — Naukri Recruiter FAQ, https://naukricom.freshdesk.com/support/solutions/articles/228261-what-is-the-significance-of-keyword-search-in-resdex- ; Naukri Blog, https://www.naukri.com/blog/recruiter-resdex/ [VENDOR DOC]
- Textkernel's skills taxonomy has three layers: categories, language-independent skills, and language-specific synonyms ("surface forms"). Each skill is "associated with a variety of synonyms, acronyms, and alternative wordings" to harmonize data and improve search accuracy. The /normalize endpoint maps input to taxonomy skills: a confidence of 1.0 is a full match, and unmatched skills come back "unclassified". — Textkernel, Skills API overview, https://developer.textkernel.com/tx-platform/v10/skills-intelligence/skills-api/overview/ ; Normalize endpoint, https://developer.textkernel.com/SkillsIntelligence/master/skills/normalize/ ; Skills page, https://www.textkernel.com/skills [VENDOR DOC]
- Textkernel's scale figures vary by page and date:
  - FAQ: more than 13,000 skills and 250,000 synonyms in 20+ languages;
  - skills page: more than 12,000 concepts and 300,000 synonyms in 25+ languages.

  — Textkernel v9 FAQ, https://developer.textkernel.com/tx-platform/v9/faq/ ; https://www.textkernel.com/skills [VENDOR DOC]
- Greenhouse lists abbreviated job titles ("Sr. Account Exec") as a parse problem (see Q2). This is the vendor's own evidence that abbreviations reduce extraction quality. — https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse [VENDOR DOC]

### Inferences
- **Use the exact names of technologies as written in the job description**: "Kubernetes", "PostgreSQL", "React", "AWS Lambda", "CI/CD". A recruiter's literal Boolean string will match only text that is actually present.
- **Include an acronym and its expansion once**, for example "Amazon Web Services (AWS)", "Natural Language Processing (NLP)", "Site Reliability Engineering (SRE)". This covers Boolean searches on either form and helps taxonomy normalization. Greenhouse's wildcard support covers plurals but not acronym/expansion pairs.
- **Keep a dedicated "Skills" section with plain-text headings.** Parsers extract skills into structured fields that feed taxonomy matching. Also mention each key skill in context inside Experience bullets, because recruiters search across all fields (Resdex) or the full text (Greenhouse).
- **Keyword stuffing, hidden or white text, and invented skills**: there is no documented benefit. Greenhouse flags "fake or poorly disguised data", and a recruiter reads every resume that reaches a shortlist. Keywords should reflect real experience.
- **On Naukri**, keep the profile's key-skills field, headline and designation in line with the resume. Recruiters filter on those structured fields and on freshness, which Naukri says affects ranking.

### Gaps
- Recruiter-side Boolean documentation for Workday, SuccessFactors, Darwinbox and Keka was not retrieved, so it is unknown whether those systems expand synonyms during search.
- No evidence was found on how LinkedIn Recruiter matches skills between resume text and profile skills.

## 5. Concrete formatting rules supported by documentation

### Takeaway
The following rules are directly supported by vendor documentation (Greenhouse, Textkernel, Lever):
- single column;
- no tables, text boxes or header/footer content, especially for contact details;
- no images or word art;
- a text-based PDF or a DOCX under 2.5 MB;
- clear standard section headings with consistent formatting;
- full job titles and company names;
- no letter-spaced text.

Rules about specific date formats, fonts, icons and PDF tagging are not documented in the sources reviewed. Present them as low-risk conventions, not requirements.

### Cited Findings
- **Single column**: "Resumes that have a columned layout" cause partial or failed parses. — Greenhouse, https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse. Even Textkernel's improved column detector misses about 18% of column separators. — https://textkernel.com/learn-support/blog/improving-extraction-from-column-resumes [VENDOR DOC]
- **No tables, headers or footers; contact details not in a header, footer or text box.** — Greenhouse (same article) [VENDOR DOC]
- **No graphics, photos or word art; not an image file.** — Greenhouse (same article) [VENDOR DOC]. Scanned documents need converting to a supported text format. — Lever older help article, https://lever-old.zendesk.com/hc/en-us/articles/360056337151 [VENDOR DOC, search snippet]
- **File types**:
  - Greenhouse: .doc, .docx, .pdf, .rtf, .txt;
  - Lever: Word, PDF, RTF, WordPerfect, HTML, ODF.

  — https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-file-types-for-resumes-and-cover-letters ; https://help.lever.co/hc/en-us/articles/20087345054749 [VENDOR DOC]
- **Size**: under 2.5 MB to be parsed by Greenhouse. — https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse [VENDOR DOC]
- **Clear sections with consistent formatting in each section.** — Greenhouse (same article) [VENDOR DOC]
- **Full job titles, not abbreviations; company names that include identifying words (Inc., Ltd).** — Greenhouse (same article) [VENDOR DOC]. For India, this means writing "Private Limited" or "Pvt. Ltd." where accurate. This is my inference from the Greenhouse wording.
- **No letter-spaced text.** — Greenhouse (same article) [VENDOR DOC]
- **Dates**: Textkernel interprets "current" relative to the document's last-modified date. Without that date, the latest role on an old resume is treated as current. — https://developer.textkernel.com/tx-platform/v10/faq/ [VENDOR DOC]

### Inferences
- Recommended rule set for a SWE resume, ordered by how strong the evidence is:
  1. **Single-column layout** (documented).
  2. **Name, phone, email, city, LinkedIn and GitHub as plain body text on the first lines** (documented: not in a header, footer or text box).
  3. **No tables, text boxes, images, photos, skill bars, logos or word art** (documented).
  4. **Export a text-based PDF from Word, Google Docs or LaTeX, or submit DOCX. Check that the text can be selected and copied in the right order** (documented that image files fail; the copy-paste check is an inference based on Textkernel's "text rendering first" description).
  5. **Keep the file under 2.5 MB** (documented for Greenhouse).
  6. **Standard headings**: "Experience" or "Work Experience", "Education", "Skills", "Projects". Keep formatting consistent (documented: "clear sections"; the exact heading words are a convention).
  7. **Full job titles and full legal company names** (documented).
  8. **No letter-spaced headings** (documented).
  9. **Dates**: use one consistent, unambiguous format with month and year for every role, for example "Jan 2022 – Present" or "01/2022 – Present" (convention; no vendor document specifies a format). Avoid year-only ranges and season names.
  10. **Icons, special Unicode symbols and unusual fonts**: undocumented risk. Replace icons with text labels such as "Email:" and "GitHub:" (low-cost precaution, not documented).
- The following are myths or unsupported in the evidence reviewed:
  - "ATS cannot read PDFs";
  - "you must use DOCX";
  - "75% of resumes are auto-rejected";
  - "white-text keyword stuffing helps";
  - "a keyword match-rate score determines rejection".

  Each of these traces to commercial sources or lacks primary support.

### Gaps
- No vendor documentation was found on PDF tagging (accessibility structure tags), embedded fonts, ligatures (for example "fi" extracted as one glyph), hyperlinks, or the effect of a two-page vs one-page resume on parsing.
- No independent parser benchmark (academic or government) comparing PDF and DOCX accuracy was found.
- Documentation for Indian ATS parsers (Darwinbox, Keka, Zoho Recruit, Naukri) was not found. Rules are extrapolated from Greenhouse, Lever and Textkernel.

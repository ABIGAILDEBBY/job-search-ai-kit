# Plain Prompts — For claude.ai Users

No Claude Code? No problem. Copy any prompt below, paste it into claude.ai, and follow the instructions.

Each prompt will ask you questions first, then help you. That is intentional — the more context you give, the better the output.

---

## Prompt 1 — Vet a Job Posting

```
I want you to help me audit a job posting before I apply.

First, ask me:
1. To paste the full job description
2. What draws me to this role
3. Whether I have researched the company

Then run through these checks in order:
- Extract basics: company, role, location, remote status, work authorization requirements, salary
- Ghost job signals: posting age, vague language, no contact listed
- Remote legitimacy: geographic restrictions, time zone requirements, travel, in-office requirements
- Work authorization: search for visa/sponsorship/authorization language and flag any issues
- Skills alignment: compare what they want to what I tell you about my background

End with a clear recommendation: Apply, Apply with caution, Clarify before applying, or Skip.
```

---

## Prompt 2 — Check If a Remote Job Is Actually Remote

```
I want you to help me verify whether a job listed as "remote" is genuinely remote or has hidden restrictions.

Ask me to paste the job description first.

Then check:
1. Location field — is there a geographic restriction alongside "remote"?
2. Work authorization language — search for visa, sponsorship, authorized, eligible
3. Time zone requirements — explicit or absent (absence is a signal)
4. Travel requirements — any mention of in-person, travel, quarterly, on-site
5. Equipment and setup requirements that could create barriers

Give me a clear verdict: Genuinely remote / Restricted remote / Hybrid in disguise / Cannot confirm.
```

---

## Prompt 3 — Research a Company Before Applying

```
Help me vet a company before I invest time in their application process.

Ask me:
1. The company name and website
2. Whether I have already spoken to anyone there
3. Anything that made me hesitate about this company

Then guide me through:
- Company basics: industry, size, stage, founded
- Financial health signals (layoffs, funding, news)
- Remote culture check using LinkedIn employee locations
- Glassdoor signals — what to search and what to look for
- Leadership and hiring signals
- Red flags and green flags

Close with an overall risk assessment and 3-5 questions I should ask the recruiter.
```

---

## Prompt 4 — Build or Tailor My Resume

```text
You are an expert resume writer. Help me build or tailor a resume for a specific role.

Critical rules:
- Never fabricate experience I do not have
- Every bullet point must follow: action verb + what was done + how (tool or process) + result + metric where possible
- No two bullet points should start with the same action verb
- The professional summary must have a strong value proposition, not generic adjectives

Start by asking me ALL of these before writing anything:

1. What role am I applying for? (I will paste the job description)
2. How many years of professional experience do I have?
3. Am I a student or recent graduate with limited work experience?
4. List of every role I have held: company, title, dates, full/part time
5. For each role: 3-5 most impactful things I did with numbers and tools
6. Education: degree, institution, graduation year, field of study
7. Relevant coursework (if applicable to the role)
8. Technical skills, tools, platforms, languages
9. Professional strengths
10. Certifications with issuing body and year
11. Projects worth including with outcomes
12. Volunteer experience relevant to the role
13. Do I have an existing resume to improve? If so I will paste it

Then write the resume in this order:
- Professional Summary (if 2+ years experience) OR Objective Statement (if student or under 2 years)
- Work Experience with 3-6 achievement bullets per role
- Education with relevant coursework if applicable
- Skills: Technical Skills first, then Professional Skills (not "soft skills")
- Certifications, Projects, Volunteer Experience if relevant

Generate the final resume as a Python script using python-docx so I can produce a clean DOCX file.

At the end, score how well my resume matches the job description out of 100 and tell me what to improve before I submit.
```

---

## Prompt 4b — Score My Resume Against a Job Description

```text
You are an expert ATS analyst. Score how well my resume matches a specific job description and give me a clear action plan.

Ask me for:
1. The full job description
2. My current resume (I will paste it)

Then analyse and score across six areas:
- Keyword Match (25 points): which JD keywords are present vs missing in my resume
- Skills Alignment (20 points): how well my skills match what the role requires
- Experience Relevance (25 points): how directly my work history speaks to this role
- Achievement Quality (15 points): are my bullets achievement-driven with metrics or just task descriptions
- Resume Structure and ATS Safety (10 points): standard headings, no tables or columns, consistent dates, right length
- Education and Credentials Match (5 points): do I meet the stated requirements

Show me the score breakdown clearly with totals out of 100 and a rating:
- 0-49: Weak
- 50-64: Developing
- 65-79: Competitive
- 80-89: Strong
- 90-100: Exceptional

Then give me a prioritised action plan — be specific about exactly which keywords are missing and where to add them, which bullet points need rewriting, and what to fix before I apply.

Ask me at the end if I want you to rewrite specific sections based on the gaps you found.
```

---

## Prompt 5 — Write a Cold Email to a Hiring Manager

```
Help me write a cold email or LinkedIn message to a hiring manager or recruiter.

Ask me:
1. Who I am reaching out to (name, title, company)
2. How I found them
3. Whether I am targeting a specific role or making general contact
4. What is most relevant about my background for them specifically
5. Whether this is an email or a LinkedIn message

Then write a message that is:
- Under 150 words for email, under 4 sentences for LinkedIn
- Specific to this person, not generic
- Leading with why I am reaching out to them in particular
- Ending with one easy-to-answer ask

Also check it for common mistakes: generic openers, self-focused language, vague asks, overselling.
```

---

## Prompt 6 — Pre-Submit Checklist

```
Run me through a final checklist before I submit a job application.

Ask me which role and company I am applying to and whether my resume and cover letter are ready.

Then check:
- Resume: tailored to JD, professional file name, ATS-safe format, no typos, live links
- Application form: all required fields complete, salary field addressed, screening questions answered specifically
- Eligibility: work authorization, location, years of experience, required credentials
- Post-submit plan: application logged, LinkedIn connection planned, follow-up reminder set

Flag anything that needs fixing before I submit.
```

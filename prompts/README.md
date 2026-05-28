# Plain Prompts: For claude.ai Users

No Claude Code? No problem. Copy any prompt below and paste it into claude.ai. Each one replicates the full logic of the matching slash command.

They will ask you questions first, then help you. That is intentional — the more context you give, the better the output.

---

## Prompt 1: Vet a Job Posting

Matches `/vet-job`

```text
You are helping me run a full audit on a job posting before I decide to apply.

Start by asking me:
1. To paste the full job description (or share the URL)
2. What draws me to this role specifically
3. Whether I have already researched this company at all

Once you have the job description, run through all of these steps in order. Be direct. Flag problems clearly. Do not soften concerns.

STEP 1 — Extract the basics
Pull out and display:
- Company name, role title, location / remote status
- Salary range (if listed)
- Work authorization requirements (search for: authorized, visa, sponsorship, eligible, citizenship)
- Application deadline and posting date (flag if older than 60 days)

STEP 2 — Ghost job check
Flag any of: posted 60+ days ago with no updates, vague responsibilities ("assist with various tasks"), no named contact, generic templated language, same role listed under multiple titles.
Tell me clearly: "This posting shows [X] ghost job signals" or "No ghost job signals detected."

STEP 3 — Remote legitimacy check
If the role is listed as remote:
- Is there a geographic restriction alongside "remote"?
- Any required in-person time, travel, or onboarding?
- Are time zones mentioned? (Silence here is a signal — flag it.)
Tell me: "This role appears to be [fully remote / restricted remote / remote-first hybrid / misleadingly labeled remote]" and explain why.

STEP 4 — Work authorization check
Search the full description for: authorized, visa, sponsorship, eligible, citizenship, work permit.
Tell me clearly whether there is a potential authorization mismatch and what to clarify before applying.

STEP 5 — Skills alignment
Compare the required and preferred skills in the posting against what I tell you about my background.
Show a table: Required skill | In your profile? (Yes / No / Partial)
Flag any hard requirements I do not meet. Also flag if I am significantly overqualified.

STEP 6 — Red flags and green flags
List up to 3 green flags and up to 3 red flags about this posting.

STEP 7 — Recommendation
End with one of:
- Apply: strong match, no blockers
- Apply with caution: worth pursuing but verify [specific thing] first
- Clarify before applying: [specific question to ask first]
- Skip: [clear reason]

Then ask: "Would you like me to help you tailor your resume, research the company, or write a cold email to the hiring manager?"
```

---

## Prompt 2: Check If a Remote Job Is Actually Remote

Matches `/check-remote`

```text
Help me verify whether a job listed as "remote" is genuinely remote or has hidden restrictions.

Start by asking me:
1. To paste the job description (or share the URL)
2. Where I am based, and whether I need fully remote with no geographic restrictions

Then run every check below. Be direct and specific.

CHECK 1 — Location field
Read the location carefully. Does it say "Remote" alone, or does it include a country, state, or region?
Verdict: Unrestricted remote / Restricted remote / Unclear, needs confirmation

CHECK 2 — Work authorization language
Search the full description for: authorized, visa, sponsorship, eligible, citizenship, work permit, right to work.
If found, quote the exact line and flag it clearly. Tell me directly if this is a hard blocker.

CHECK 3 — Time zone requirements
Look for any mention of time zones, working hours, or overlap requirements.
If silent, flag it: "This posting does not mention time zones. This often means the team defaults to headquarters hours. Recommend asking before applying."

CHECK 4 — Travel requirements
Search for: travel, in-person, on-site, office, quarterly, annual, kickoff, headquarters.
If travel is mentioned, quote it and explain the implication — especially for international applicants.

CHECK 5 — Equipment and setup
Look for: equipment provided, must use own device, background check, specific hardware or OS requirements.
Flag anything that creates a barrier for international applicants.

CHECK 6 — Remote culture check (optional)
Ask me: "Do you want me to walk you through verifying this company's actual remote culture using their LinkedIn employee data?"
If yes, guide me to go to the company LinkedIn page, click People, look at where employees are located, and paste what I see. Interpret the geographic distribution for me.

FINAL VERDICT
Give a clear one-line verdict:
- Genuinely remote: no restrictions found
- Restricted remote: [specific restriction]
- Likely hybrid in disguise: [reason]
- Cannot confirm: [what to ask before applying]

Then offer: "Would you like me to run the full job audit on this posting?"
```

---

## Prompt 3: Research a Company Before Applying

Matches `/research-company`

```text
Help me vet a company before I invest time in their application process.

Start by asking me:
1. The company name and website
2. Whether I have already spoken to anyone there, or whether this is pre-application research
3. Whether anything specific made me hesitate about this company

Then work through every section below.

SECTION 1 — Company basics
Ask me to confirm: industry and what the company actually does (in plain terms), company size (headcount), stage (public / private / startup / scaleup / enterprise / nonprofit), founded year, headquarters location.

SECTION 2 — Financial health signals
For public companies: ask me to check recent earnings reports or news for layoffs, revenue decline, leadership changes, or strategic pivots.
For private companies: ask if I can find funding history on Crunchbase or LinkedIn. Flag if the last round was 3+ years ago with no news. Flag any recent mass layoffs.

SECTION 3 — Remote and distributed work culture
Ask me to go to the company LinkedIn page and click "People."
I should look at: where most employees are located, whether there are team members in my region or time zone, and whether the company has listed any remote-focused roles.
Interpret the data for me: if 80%+ are in one location, the company is likely office-first regardless of the job posting.

SECTION 4 — Glassdoor and employee signals
Ask me to search "[company name] remote work" on Glassdoor.
Guide me to look for: overall rating trend (improving or declining), reviews mentioning remote/flexible/distributed/micromanagement/autonomy, CEO approval rating, and whether the company responds to reviews.

SECTION 5 — Leadership and hiring signals
- Has there been recent C-suite or VP-level turnover? (check LinkedIn)
- Is the company actively hiring across many departments or only in one area?
- Are there roles posted for 90+ days? (signals a hiring freeze or internal issues)

SECTION 6 — Red flags and green flags
List up to 3 green flags and up to 3 red flags based on everything gathered.

SECTION 7 — Questions to ask the recruiter
Based on what we found, generate 3 to 5 targeted questions I should ask in the first recruiter call. Make them specific to this company, not generic.

FINAL SUMMARY
Close with: "Overall, this company appears [low risk / worth pursuing with caution / high risk] for the following reasons: [2-3 sentences]."
```

---

## Prompt 4: Build or Tailor My Resume

Matches `/tailor-resume`

```text
You are an expert resume writer. Help me build or tailor a resume for a specific role.

CRITICAL RULES — never break these:
- Never fabricate, invent, or imply experience I do not have
- Every bullet point must follow: action verb + what was done + how (tool or process) + result + metric where possible
- No two bullet points should start with the same action verb
- The professional summary must have a strong value proposition, not generic adjectives

PHASE 1 — Discovery
Ask me ALL of these in one message before writing anything:

1. What role am I applying for? (I will paste the job title and job description)
2. How many years of total professional experience do I have? (include internships, freelance, contracts)
3. Am I currently a student or recent graduate with limited work experience? (yes/no)
4. List every role I have held: company name, title, start and end dates, full/part-time/contract/internship
5. For each role: the 3-5 most impactful things I did, with numbers, tools, team sizes, and outcomes wherever possible
6. My highest level of education: degree, institution, graduation year, field of study
7. Relevant coursework (if applicable to the role)
8. All technical skills, tools, platforms, and programming languages
9. Soft skills and professional strengths
10. Certifications with issuing body and year
11. Projects worth including with outcomes
12. Volunteer experience relevant to this role
13. Do I have an existing resume to improve? If yes, I will paste it.

PHASE 2 — Assess experience level
If student or under 2 years: use an Objective Statement and lead with Education before Work Experience.
If 2+ years: use a Professional Summary (3-4 sentences: X years + core expertise + one specific high-impact achievement + what I bring to the next role).
If 10+ years or executive: use an Executive Positioning Statement (2-3 strategic sentences, not a list of adjectives).

PHASE 3 — Template selection
Present all 8 templates and highlight the 3 most appropriate for my field and experience level. Do not proceed until I confirm a template.

Recommendation logic:
- Software engineering / data engineering / ML / DevOps: 1 FAANG Classic, 4 Modern Tech, 2 Harvard Classic
- Product management: 4 Modern Tech, 5 Creative Accent, 3 Consulting Tight
- UX / UI design / creative / brand: 5 Creative Accent, 4 Modern Tech, 2 Harvard Classic
- Finance / banking / investment banking / accounting: 6 Conservative Pro, 3 Consulting Tight, 2 Harvard Classic
- Consulting (MBB, Big 4, strategy): 3 Consulting Tight, 2 Harvard Classic, 6 Conservative Pro
- Marketing / growth / content: 5 Creative Accent, 4 Modern Tech, 1 FAANG Classic
- Operations / project management / supply chain: 4 Modern Tech, 6 Conservative Pro, 3 Consulting Tight
- Healthcare / life sciences / clinical: 6 Conservative Pro, 2 Harvard Classic, 7 Entry Academic
- Legal / compliance / regulatory: 6 Conservative Pro, 2 Harvard Classic, 3 Consulting Tight
- Student / entry level (under 2 years): 7 Entry Academic, 2 Harvard Classic, 1 FAANG Classic
- Senior / director / VP / executive (10+ years): 8 Executive Strategic, 4 Modern Tech, 3 Consulting Tight

All 8 templates:

1. FAANG Classic — no color, inline skill categories (Languages / Frameworks / Cloud). Modelled on Google, Meta, and Amazon engineering resumes. Best for: SWE, data, ML, DevOps.

2. Harvard Classic — Garamond serif, ALL CAPS headings with full-width horizontal rule. Modelled on Harvard Career Services. Best for: consulting, finance, law, academia.

3. Consulting Tight — one page strict, most impressive bullet first, Interests section. Modelled on McKinsey/BCG/Bain format. Best for: consulting, finance, strategy.

4. Modern Tech — navy accent, Calibri sans-serif, inline skills. Best for: engineering, data, product, ops at tech companies and startups.

5. Creative Accent — large name, teal accent rule, portfolio URL as most prominent contact element. Best for: UX/UI design, product design, marketing, creative.

6. Conservative Pro — Georgia serif, pure black and white, no design elements. Best for: banking, IB, law, compliance, accounting, healthcare.

7. Entry Academic — centered name, dark shaded headings, education first, one page. Best for: students and recent graduates.

8. Executive Strategic — 24pt name, bold navy left-border headings, two-page spacious layout, competencies band. Best for: directors, VPs, C-suite, 10+ years.

PHASE 4 — Write the resume

Build sections in this order (Education leads if student or Template 7):

Header: Name (large), then contact line with: email (clickable), phone (clickable), LinkedIn shown as "LinkedIn Profile" (hyperlinked), GitHub shown as "GitHub Portfolio" (hyperlinked, only if provided), portfolio URL (only if provided), location (city and country only).
- Template 5: portfolio URL goes first in the contact line
- Template 8: add a subtitle line with the target role title under the name

Summary / Objective / Executive Positioning Statement (see Phase 2 rules above)

Core Competencies band — Template 8 only: 6-9 one-line strategic capabilities (e.g. "P&L ownership across $120M portfolio", not "Microsoft Excel")

Work Experience: Company | Title | Start–End | Location, followed by 3-6 bullet points per role.
- Template 3: order bullets by impact, most impressive result first
- Action verbs must be strong, non-repeating across the entire resume

Education: Degree | Institution | Year | Field. GPA only if 3.5+. Relevant coursework if applicable.

Skills: Use inline category format for all templates:
Technical Skills:  Python, SQL, dbt, Spark, Airflow
Frameworks:        TensorFlow, FastAPI
Professional Skills:  Stakeholder communication, agile delivery

Certifications: Certification name | Issuing body | Year

PHASE 5 — Generate the DOCX
Write a Python script using python-docx that generates the resume as a formatted DOCX file. The script must:
- Apply font, size, and heading style appropriate to the chosen template
- Make contact details clickable (mailto: and tel: hyperlinks)
- Use inline heading styles (not Word styles) so the output is ATS-safe
- Tell me to run: python3 resume_output.py

PHASE 6 — Score and review
After generating the resume, score how well it matches the job description out of 100 across:
- Keyword match (25 pts): JD keywords present in the resume
- Skills alignment (20 pts): skills matching the role requirements
- Experience relevance (25 pts): work history speaking to this role
- Achievement quality (15 pts): bullets with metrics vs. task descriptions
- Structure and ATS safety (10 pts): headings, no columns, consistent dates
- Education and credentials (5 pts): meets stated requirements

Then list: the 3 highest priority improvements before I submit.

End with: "Review every line before submitting. You know your own experience better than I do."
```

---

## Prompt 4b: Score My Resume Against a Job Description

Matches `/score-resume`

```text
You are an expert ATS analyst and hiring consultant. Score how well my resume matches a specific job description, identify exactly what is missing or weak, and give me a clear action plan.

Start by asking for both in one message:
1. The full job description (I will paste it, or provide the URL)
2. My current resume (I will paste it)

Refuse to proceed with scoring until you have valid content for both. Do not infer or fabricate missing content.

STEP 1 — Extract JD requirements
Parse and list:
Hard requirements (must-have): required skills, tools, technologies, minimum years of experience, required education or certifications, work authorization.
Preferred requirements (nice-to-have): additional skills, industry experience, leadership indicators.
ATS keywords: every specific tool, technology, methodology, job title, and domain term mentioned. Note frequency — keywords mentioned multiple times carry more weight.

STEP 2 — Score across six dimensions

A. Keyword Match (25 points)
Compare ATS keywords from the JD against what appears in the resume.
90-100% of keywords present: 23-25 pts | 70-89%: 18-22 pts | 50-69%: 12-17 pts | Below 50%: 0-11 pts
List every missing keyword explicitly.

B. Skills Alignment (20 points)
All hard-required skills present and prominent: 18-20 pts | Most present but some buried or missing: 12-17 pts | Significant gaps: 0-11 pts

C. Experience Relevance (25 points)
Strong overlap in responsibilities, industry, and seniority: 22-25 pts | Moderate overlap: 15-21 pts | Limited direct relevance: 0-14 pts

D. Achievement Quality (15 points)
80%+ of bullets have clear achievements with metrics: 13-15 pts | Mixed: 8-12 pts | Mostly task descriptions: 0-7 pts

E. Structure and ATS Safety (10 points)
Standard section headings (2 pts) | No tables, columns, or text boxes (2 pts) | Consistent date formatting (2 pts) | Appropriate length for experience level (2 pts) | Professional summary or objective present (2 pts)

F. Education and Credentials (5 points)
Meets stated education requirements (3 pts) | Certifications or relevant coursework present (2 pts)

STEP 3 — Display the score clearly

RESUME MATCH SCORE
Keyword Match           XX / 25
Skills Alignment        XX / 20
Experience Relevance    XX / 25
Achievement Quality     XX / 15
Structure & ATS         XX / 10
Education & Credentials XX /  5
TOTAL                   XX / 100

Rating:
0-49:   Weak — significant rework needed before applying
50-64:  Developing — will likely screen out early
65-79:  Competitive — likely to pass ATS, minor improvements needed
80-89:  Strong — well-positioned, apply with confidence
90-100: Exceptional — highly aligned

STEP 4 — Specific action plan
Give a prioritised list. Be specific — not "add more keywords" but exactly which keywords are missing and where to add them.

Priority 1 — Do this before applying:
- [Specific action]

Priority 2 — Strongly recommended:
- [Specific action]

Priority 3 — Nice to have:
- [Specific action]

STEP 5 — Offer next steps
Ask: "Would you like me to rewrite this resume fully for this role, rewrite just the professional summary, rewrite the skills section, or identify and rewrite the weakest bullet points?"
```

---

## Prompt 5: Write a Cold Email to a Hiring Manager

Matches `/cold-email`

```text
Help me write a cold email or LinkedIn message to a hiring manager or recruiter that gets read and responded to.

The goal is not to be impressive. The goal is to be specific, brief, and easy to respond to.

Start by asking me:
1. Who I am reaching out to (name, title, company)
2. How I found them (LinkedIn, the job post, a referral)
3. Whether I am targeting a specific role or making general interest contact
4. What is the one thing about my background most relevant to them specifically
5. Whether this is an email or a LinkedIn message

Then ask:
- What do I know about this person's work or background?
- Has the company had any recent news, product launches, funding, or hiring signals I am aware of?

Use this to make the message specific. Generic outreach is ignored. Specific outreach gets responses.

FOR EMAIL:
Subject line: short and specific — name the role or the specific angle.
Examples: "Data Engineer role, background in [specific tech] + question" or "Your team's [specific project], quick question"

Body structure:
- Line 1: Why I am reaching out to them specifically (not the company generally)
- Lines 2-3: One concrete, relevant thing about my background — lead with impact, not job titles
- Line 4: A single, easy-to-answer ask (not "do you have any openings" but "would a 20-minute call make sense?")
- Sign-off: name, LinkedIn URL, optionally portfolio

Keep it under 150 words. If it is longer, cut it.

FOR LINKEDIN:
- 3-4 sentences max
- Same structure: specific reason, one relevant credential, one easy ask
- No attachments in the first message

After drafting, check for:
- Generic opener ("I hope this message finds you well" — remove it)
- Self-focused language ("I am looking for..." — reframe to their perspective)
- Vague ask ("let me know if there are any opportunities" — too passive)
- Overselling ("I am the perfect candidate" — remove)
- Length over 150 words for email, over 4 sentences for LinkedIn

Also write a short follow-up version (2 sentences) for if there is no response in 5-7 business days: acknowledge the first message, add one new piece of value, ask the same simple question again.
```

---

## Prompt 6: Pre-Submit Checklist

Matches `/pre-submit`

```text
Run me through a final checklist before I submit a job application. Catch anything that could quietly disqualify my application before a human ever reads it.

Start by asking: "Which role and company are you about to apply to? Do you have the tailored resume and cover letter ready?"

Then check every item below. Mark each as PASS, FLAG, or NEEDS FIX.

RESUME CHECKS
- Resume is tailored to this specific job description (not the generic base version)
- File name is professional: FirstName-LastName-Role.pdf (not resume_final_v3_ACTUAL.pdf)
- File format is ATS-safe: .docx or clean .pdf (not an image, not a Canva export with graphics)
- No tables, columns, text boxes, or Word headers/footers that break ATS parsing
- Contact info is correct and current (email, LinkedIn, phone if relevant)
- No typos in company name, role title, or my own credentials
- Dates are consistent and no unexplained gaps
- All claimed links (LinkedIn, GitHub, portfolio) are live and up to date

APPLICATION FORM CHECKS
- Every required field is filled (no blanks left that are not explicitly optional)
- Salary field: check whether to enter a number or a range, do not leave blank
- "How did you hear about us?" — a real answer, not just "job board"
- Cover letter field: confirmed whether required, optional, or not expected
- Any screening questions answered specifically, not with generic responses

ELIGIBILITY CHECKS
- Work authorization requirement confirmed, I meet it
- Location requirement confirmed, I meet it or have a plan to address it
- Required years of experience, I meet the minimum stated
- Required certifications or degrees, I meet them or the role says "or equivalent experience"

POST-SUBMIT ACTIONS
After submitting, do these within 24 hours:
- Log the application with: company, role, date applied, status, follow-up date
- Find the hiring manager or recruiter on LinkedIn and connect with a short note
- Set a calendar reminder to follow up in 5-7 business days if no confirmation received

FINAL CHECK
Ask me: "Is there anything about this application that felt uncertain or off to you?"
If yes, address it before I submit.
If everything passes, confirm: "You are clear to submit. Good luck, and follow up in 5-7 days."
```

---

## Prompt 7: Prepare for My Interview

Matches `/prep-interview`

```text
You are an expert technical interviewer and career coach. Prepare me for a specific upcoming interview using my actual resume and the actual job description — not generic questions.

Every question you generate must be traceable to a specific claim on my resume, a requirement in the JD, or a gap between the two. Do not write model answers — a coaching note per question is enough.

CRITICAL RULES:
- Total questions across all sections: 12 to 18. Quality over volume.
- Never generate questions that could apply to any candidate.
- Flag skill gaps honestly. Do not soften mismatches.
- Calibrate technical depth to the seniority level I provide.

PHASE 1 — Gather inputs
Ask me for all three of these in one message before generating anything:
1. My tailored resume (the version I submitted for this role)
2. The full job description
3. The seniority level of this role (junior / mid / senior / lead / staff / principal / manager / people-manager)

PHASE 2 — Analyse silently before generating
Before writing any questions, extract:
- Every claim, metric, technology, and tool on my resume
- Every required and preferred skill, tool, and responsibility in the JD
- Gaps: things the JD requires that are absent or understated on my resume
- The core technical or professional domain of the role
- Seniority calibration:
  - Junior: concept understanding
  - Mid: applied, practical usage
  - Senior: design decisions and trade-offs
  - Lead / Staff / Principal: system-level thinking, team impact, cross-functional influence
  - Manager / People-Manager: team leadership, hiring and coaching, execution planning, stakeholder communication, cross-functional delivery

Do not show this analysis to me. Use it only to generate targeted questions.

PHASE 3 — Generate interview questions

SECTION 1 — Resume challenge questions (4 to 6 questions)
Drill into specific claims, achievements, numbers, and technologies I listed.
- If I stated a metric, ask how it was measured or what the biggest obstacle was.
- If I listed a tool, ask a follow-up that reveals whether I actually used it deeply.

Format each as:
Q: [question]
Coaching note: [one sentence on what the interviewer is testing and what a strong answer covers]

SECTION 2 — Technical questions (4 to 6 questions)
Test depth of knowledge on the core technologies and concepts central to this role.
- Do not ask surface-level definitions. Ask applied, scenario-based, or trade-off questions.
- Calibrate to my seniority level.
- For non-technical roles, replace with domain knowledge questions at the same depth.

Format each as:
Q: [question]
Coaching note: [one sentence on what the interviewer is testing and what a strong answer covers]

SECTION 3 — Gap questions (2 to 4 questions, only if genuine gaps exist)
Questions likely to arise from mismatches between my resume and the JD.
- Only include this section if real gaps exist. If there are none, skip it entirely.
- Name the gap plainly. Give me a framework to address it honestly without undermining my candidacy.

Format each as:
Q: [question]
Gap flagged: [name the mismatch]
Coaching note: [how to address this gap honestly]

SECTION 4 — Role-fit and behavioural questions (3 to 4 questions)
Derived from specific signals in the JD: team structure, pace, ownership, mentoring, ambiguity, stakeholder management.
- Not generic. Every question must reflect something this role specifically requires.

Format each as:
Q: [question]
Coaching note: [what the interviewer is probing for and what a strong STAR-structured answer covers]

PHASE 4 — Readiness summary
After all questions, give me a short snapshot:

Strongest areas based on my resume and this JD:
- [2 to 3 specific strengths]

Areas to prepare most carefully:
- [2 to 3 specific things to review or practise]

One thing to research before I walk in:
- [something about the company, team, or product that will make my answers more specific]

Then ask: "Would you like me to help you research the company more deeply, or run a mock interview where I ask these questions one at a time and coach your answers?"
```

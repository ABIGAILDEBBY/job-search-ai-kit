# Job Search AI Kit: Your Search Profile

This file is read automatically by Claude Code every time you open this project.
Fill in your profile once. Every command in this kit will use it.

---

## Your Profile

```
NAME: Abigail Woolley
CURRENT ROLE: Microsoft Fabric Data Engineer (Technical Lead)
CURRENT LOCATION: Accra, Ghana
TARGET ROLE(S): Data Engineer, Senior Data Engineer, Analytics Engineer, Data Officer, ML Engineer
TARGET INDUSTRIES: International Development, Tech, Finance, SaaS, Cloud
SALARY EXPECTATION: $80,000 - $130,000 USD
WORK AUTHORIZATION: Ghana-based, seeking fully remote or international relocation with sponsorship; no US work authorization currently
PREFERRED TIME ZONES TO OVERLAP WITH: UTC, UTC+1, EST (flexible)
YEARS OF EXPERIENCE: 6+
KEY SKILLS: Microsoft Fabric, PySpark, Apache Spark, Delta Lake, Medallion Architecture, ETL/ELT, Python, SQL, T-SQL, Azure, Azure Data Factory, Azure Synapse, Power BI, DAX, Dataflows Gen2, OneLake, Data Pipelines, Data Governance, Data Lineage, ML Pipeline Development, Scikit-learn, PyTorch, TensorFlow, REST APIs, Agile
EDUCATION: MS Information Technology (Data Science & Applied ML), Carnegie Mellon University, 2020; BS Computer Science, University of Ghana, 2017
RESUME FILE: resume/tailored/Abigail-Woolley-Microsoft-Fabric-Engineer.docx
LINKEDIN URL: https://www.linkedin.com/in/abigail-woolley/
PORTFOLIO/GITHUB URL: https://github.com/ABIGAILDEBBY
```

---

## How to Use This Kit

This project comes with a set of slash commands. Type `/` in Claude Code to see them all.

| Command | What it does |
|---|---|
| `/verify-opportunity` | Quick check: confirm a posting is still live, deadline not past, position not filled — run this before anything else |
| `/find-roles` | Skill-first job discovery: find roles that match your actual skills, not just your target title |
| `/vet-job` | Full audit of a job posting before you apply (includes opportunity viability check) |
| `/check-remote` | Verify if a "remote" job is actually remote |
| `/research-company` | Deep-vet a company before you invest time |
| `/tailor-resume` | Match your resume to a specific job description |
| `/score-resume` | ATS match score with a full action plan |
| `/cold-email` | Write a cold outreach email to a hiring manager |
| `/pre-submit` | Final checklist before you hit apply |
| `/prep-interview` | Targeted interview questions from your resume and the JD |

> Not using Claude Code? See `prompts/README.md` for plain copy-paste versions of every command.

---

## Project Structure

```
job-search-ai-kit/
├── CLAUDE.md                  ← your search profile (fill this in first)
├── README.md                  ← setup guide and recommended workflow
├── demo/                      ← sample profile and resume for testing
│   ├── CLAUDE.md              ← sample profile (Amaka Jenkins, Backend Engineer)
│   ├── base-resume.md         ← sample resume
│   └── sample-job.md          ← sample job description for testing
├── .claude/commands/          ← slash commands (Claude Code only)
├── jobs/                      ← one file per job you are tracking
├── resume/
│   ├── base-resume.md         ← your master resume (paste it here)
│   └── tailored/              ← JD-specific versions go here
├── cover-letters/
├── companies/
├── applications/
│   └── tracker.md
└── prompts/
    └── README.md
```

---

## Notes for Claude

- Always read this file before running any command.
- When the user pastes a job description, extract: company name, role title, location, remote status, required skills, and work authorization requirements.
- When tailoring a resume, never fabricate experience. Only reframe and reorder real experience from `demo/base-resume.md`.
- When vetting a job, always ask clarifying questions if key information is missing from the posting.
- Flag any mismatch between the user's profile above and the job requirements clearly before proceeding.


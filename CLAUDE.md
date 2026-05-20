# Job Search AI Kit — Your Search Profile

This file is read automatically by Claude Code every time you open this project.
Fill in your profile once. Every command in this kit will use it.

---

## Your Profile

```
NAME:
CURRENT ROLE:
CURRENT LOCATION (city, country):
TARGET ROLE(S):
TARGET INDUSTRIES:
SALARY EXPECTATION (range + currency):
WORK AUTHORIZATION: (e.g. "Open to work in US, UK, EU — need sponsorship" or "Ghana-based, seeking fully remote only")
PREFERRED TIME ZONES TO OVERLAP WITH:
YEARS OF EXPERIENCE:
KEY SKILLS (comma separated):
EDUCATION:
RESUME FILE: resume/base-resume.md
LINKEDIN URL:
PORTFOLIO/GITHUB URL:
```

---

## How to Use This Kit

This project comes with a set of slash commands. Type `/` in Claude Code to see them all.

| Command | What it does |
|---|---|
| `/vet-job` | Full audit of a job posting before you apply |
| `/check-remote` | Verify if a "remote" job is actually remote |
| `/research-company` | Deep-vet a company before you invest time |
| `/tailor-resume` | Match your resume to a specific job description |
| `/cold-email` | Write a cold outreach email to a hiring manager |
| `/pre-submit` | Final checklist before you hit apply |

> Not using Claude Code? See `/prompts/README.md` for plain copy-paste versions of every command.

---

## Project Structure

```
job-search-ai-kit/
├── CLAUDE.md                  ← this file — your search profile
├── README.md                  ← setup guide for new users
├── .claude/commands/          ← slash commands (Claude Code only)
├── jobs/                      ← one file per job you are tracking
│   └── _template.md
├── resume/
│   ├── base-resume.md         ← your master resume (paste it here)
│   └── tailored/              ← JD-specific versions go here
├── cover-letters/             ← drafts per application
├── companies/                 ← research notes per company
├── applications/
│   └── tracker.md             ← status tracker for all applications
└── prompts/
    └── README.md              ← plain prompts for claude.ai users
```

---

## Notes for Claude

- Always read this file before running any command.
- When the user pastes a job description, extract: company name, role title, location, remote status, required skills, and work authorization requirements.
- When tailoring a resume, never fabricate experience. Only reframe and reorder real experience from `resume/base-resume.md`.
- When vetting a job, always ask clarifying questions if key information is missing from the posting.
- Flag any mismatch between the user's profile above and the job requirements clearly before proceeding.

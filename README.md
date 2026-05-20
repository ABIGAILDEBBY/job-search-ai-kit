# Job Search AI Kit

A Claude-powered toolkit for tech and data professionals navigating international job searches.

Built alongside the **[The Job Search No One Taught You](https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7461467553941532672)** LinkedIn series by Abigail Woolley.

---

## What This Is

A structured workspace you clone once, fill in your profile, and use throughout your entire job search. It gives Claude the context it needs to help you vet jobs, tailor your resume, write cold emails, and run pre-apply checks — without you having to re-explain yourself every time.

---

## Quick Setup (2 minutes)

### If you use Claude Code (recommended)

1. Clone this repo
   ```bash
   git clone https://github.com/ABIGAILDEBBY/job-search-ai-kit.git
   cd job-search-ai-kit
   ```

2. Open it in Claude Code
   ```bash
   claude .
   ```

3. Fill in your profile in `CLAUDE.md` — name, target role, location, work authorization, skills.

4. Paste your resume into `resume/base-resume.md`.

5. Type `/` to see all available commands.

That's it. Claude now knows who you are and what you're looking for.

---

### If you use claude.ai (no code required)

Open `prompts/README.md`. Every command is available as a plain copy-paste prompt. Paste it into claude.ai, answer the questions it asks, and follow the output.

---

## Available Commands

| Command | Article | What it does |
|---|---|---|
| `/vet-job` | Articles 1-4 | Full audit of a job posting |
| `/check-remote` | Article 4 | Verify remote legitimacy |
| `/research-company` | Article 5 | Vet a company before you apply |
| `/tailor-resume` | Article 9 | Match your resume to a JD |
| `/cold-email` | Article 13 | Cold outreach to hiring managers |
| `/pre-submit` | Article 11 | Final checklist before applying |

More commands will be added as the article series progresses.

---

## Folder Structure

```
job-search-ai-kit/
├── CLAUDE.md                  ← your search profile (fill this in first)
├── README.md                  ← this file
├── .claude/commands/          ← slash commands
├── jobs/                      ← one .md file per tracked job
├── resume/                    ← your master and tailored resumes
├── cover-letters/             ← drafts per application
├── companies/                 ← research notes per company
├── applications/tracker.md   ← full application status tracker
└── prompts/                   ← plain prompts for claude.ai users
```

---

## Contributing

This repo grows with the article series. If you have suggestions for new commands or improvements, open a PR.

---

*Part of [The Job Search No One Taught You](https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7461467553941532672) — a 24-article series for tech and data professionals searching smarter.*

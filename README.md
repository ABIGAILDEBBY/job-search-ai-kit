<div align="center">

# 🔍 Job Search AI Kit

### Stop applying blind. Start searching smart.

*A Claude-powered workspace for tech and data professionals navigating international job searches*

[![Powered by Claude](https://img.shields.io/badge/Powered%20by-Claude%20AI-E8611A?style=for-the-badge&logoColor=white)](https://claude.ai)
[![Slash Commands](https://img.shields.io/badge/Slash%20Commands-8%20built--in-16B2B2?style=for-the-badge)](https://github.com/ABIGAILDEBBY/job-search-ai-kit/tree/main/.claude/commands)
[![Article Series](https://img.shields.io/badge/Article%20Series-24%20articles-FFC857?style=for-the-badge)](https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7461467553941532672)
[![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)](LICENSE)

<br/>

[**📰 Read the Series**](https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7461467553941532672) &nbsp;·&nbsp; [**⭐ Star this repo**](https://github.com/ABIGAILDEBBY/job-search-ai-kit) &nbsp;·&nbsp; [**🐛 Open an issue**](https://github.com/ABIGAILDEBBY/job-search-ai-kit/issues)

</div>

---

## What this is

You clone this repo once, fill in your profile, and use it for your entire job search. It gives Claude the context it needs to help you vet jobs, tailor your resume, write cold emails, and run pre-apply checks: without re-explaining yourself every single time.

Built alongside **[The Job Search No One Taught You](https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7461467553941532672)**: a 24-article LinkedIn series by [Abigail Woolley](https://www.linkedin.com/in/abigail-woolley/).

---

## Quick setup

> **Total time: under 2 minutes**

### Option A: Claude Code (recommended)

```bash
# 1. Clone the repo
git clone https://github.com/ABIGAILDEBBY/job-search-ai-kit.git
cd job-search-ai-kit

# 2. Open in Claude Code
claude .
```

Then:

1. Fill in your profile in `CLAUDE.md`: name, target role, location, work authorisation, skills
2. Paste your base resume into `resume/base-resume.md`
3. Type `/` to see all commands

That's it. Claude now knows who you are and what you're looking for.

### Option B: claude.ai (no setup required)

Open [`prompts/README.md`](prompts/README.md). Every command is available as a plain copy-paste prompt. Paste it into [claude.ai](https://claude.ai), answer the questions, and follow the output.

No account, no terminal, no config needed.

---

## Commands

<table>
  <thead>
    <tr>
      <th>Command</th>
      <th>What it does</th>
      <th>When to use it</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>/vet-job</code></td>
      <td>Full audit of a job posting</td>
      <td>Before you spend time applying</td>
    </tr>
    <tr>
      <td><code>/check-remote</code></td>
      <td>Verify whether a role is genuinely remote</td>
      <td>Any time "remote" appears in a JD</td>
    </tr>
    <tr>
      <td><code>/research-company</code></td>
      <td>Deep-vet a company's health and culture</td>
      <td>Before the first recruiter call</td>
    </tr>
    <tr>
      <td><code>/tailor-resume</code></td>
      <td>Rewrite your resume to match a specific JD</td>
      <td>Before every application</td>
    </tr>
    <tr>
      <td><code>/score-resume</code></td>
      <td>ATS match score with a full action plan</td>
      <td>After tailoring, before submitting</td>
    </tr>
    <tr>
      <td><code>/cold-email</code></td>
      <td>Write a cold outreach message to a hiring manager</td>
      <td>When you want in before the queue</td>
    </tr>
    <tr>
      <td><code>/pre-submit</code></td>
      <td>Final checklist before you hit apply</td>
      <td>Every single time</td>
    </tr>
    <tr>
      <td><code>/prep-interview</code></td>
      <td>Targeted interview questions from your actual resume and the JD</td>
      <td>As soon as you get an interview</td>
    </tr>
  </tbody>
</table>

> More commands will be added as the article series progresses.

---

## Recommended workflow

The commands work best in this order. Each one builds on the previous step: do not skip ahead.

```text
For every job you consider:

1. /vet-job          ← audit the posting before spending any time on it
                        catches ghost jobs, visa blockers, and skills gaps early

2. /check-remote     ← only if the role is listed as remote
                        verifies whether "remote" is genuine or geographically restricted

3. /research-company ← deep-vet the company before investing hours in your application
                        funding, culture, red flags, engineer sentiment

4. /tailor-resume    ← rewrite your resume specifically for this role and company
                        generates a formatted DOCX ready to submit

5. /score-resume     ← check your ATS match score before submitting
                        tells you exactly what to fix if the score is too low

6. /cold-email       ← optional: reach out to the hiring manager directly
                        use this alongside or instead of the standard apply button

7. /pre-submit       ← final checklist before you hit apply
                        catches the things you miss when you are in a rush

--- after you get the interview ---

8. /prep-interview   ← generate targeted questions from your actual resume and this JD
                        not generic prep: specific to what you claimed and what they need
```

> The most common mistake is jumping straight to `/tailor-resume` without vetting the job first. A great resume sent to a ghost job or a visa-blocked role is wasted time.

---

## Folder structure

```
job-search-ai-kit/
│
├── CLAUDE.md                  ← your search profile (fill this in first)
│
├── .claude/
│   └── commands/              ← all slash commands live here
│
├── resume/
│   ├── base-resume.md         ← your master resume
│   └── tailored/              ← JD-specific versions go here
│
├── jobs/                      ← one .md file per job you are tracking
├── cover-letters/             ← drafts per application
├── companies/                 ← company research notes
│
├── applications/
│   └── tracker.md             ← full status tracker
│
└── prompts/
    └── README.md              ← plain prompts for claude.ai users
```

---

## Who this is for

- Tech and data professionals searching for **international remote roles**
- Anyone applying across time zones who needs to move fast without cutting corners
- Job seekers tired of generic advice who want a repeatable, structured process

---

## Contributing

This repo grows alongside the article series. If you spot a bug, have a command idea, or want to improve an existing prompt, open a PR. Keep it focused and test your changes in Claude Code before submitting.

---

## Work with Abigail

The kit is designed to be self-sufficient and most people won't need anything beyond what's here. That said, if you want a second pair of eyes on your resume or a direct conversation about your search, I keep a few slots open each week for 1:1 sessions: [topmate.io/abigail_woolley](https://topmate.io/abigail_woolley)

---

<div align="center">

*Part of [The Job Search No One Taught You](https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7461467553941532672)*
*a 24-article series for tech and data professionals searching smarter.*

<br/>

Made with care by [Abigail Woolley](https://www.linkedin.com/in/abigail-woolley/) &nbsp;·&nbsp; [Subscribe to the series](https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7461467553941532672)

</div>

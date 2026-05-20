# /vet-job — Full Job Posting Audit

You are helping a job seeker run a full audit on a job posting before they decide to apply.

Start by asking:

1. "Please paste the full job description, or share the URL."
2. "What draws you to this role specifically?"
3. "Have you already researched this company at all?"

Once you have the job description, run through every section below in order. Be direct. Flag problems clearly. Do not soften concerns.

---

## Step 1 — Extract the basics

Pull out and display:
- Company name
- Role title
- Location / remote status
- Salary range (if listed)
- Work authorization requirements (search for: authorized, visa, sponsorship, eligible, citizenship)
- Application deadline (if listed)
- Posted date (if available — flag if older than 60 days)

---

## Step 2 — Ghost job check

Flag any of the following:
- Posted more than 60 days ago with no updates
- Extremely vague responsibilities ("support the team," "assist with various tasks")
- No named hiring manager or recruiter contact
- Generic or templated language throughout
- Role listed under multiple job titles simultaneously

Tell the user clearly: "This posting shows [X] ghost job signals" or "No ghost job signals detected."

---

## Step 3 — Remote legitimacy check

If the role is listed as remote:
- Is there a geographic restriction listed alongside "remote"? (country, state, region)
- Is there any mention of required in-person time, onboarding in-office, or travel?
- Are time zones mentioned? If not, flag the silence.
- Search for: "EST preferred," "must be located," "occasional travel," "hybrid," "in-office"

Tell the user: "This role appears to be [fully remote / restricted remote / remote-first hybrid / misleadingly labeled remote]" and explain why.

---

## Step 4 — Work authorization check

Search the full description for: authorized, visa, sponsorship, eligible, citizenship, work permit.

Cross-reference with the user's profile in CLAUDE.md.

Tell the user clearly whether there is a potential authorization mismatch and what to clarify before applying.

---

## Step 5 — Skills alignment check

Compare the required and preferred skills in the posting against the user's profile in CLAUDE.md.

Show a simple table:

| Required skill | In your profile? |
|---|---|
| ... | Yes / No / Partial |

Flag any hard requirements the user does not meet. Flag also if the user is significantly overqualified.

---

## Step 6 — Red flags and green flags

List up to 3 green flags (genuine positives about this posting) and up to 3 red flags (concerns worth investigating).

---

## Step 7 — Recommendation

End with one of:
- **Apply** — strong match, no blockers
- **Apply with caution** — worth pursuing but verify [specific thing] first
- **Clarify before applying** — [specific question to ask before investing time]
- **Skip** — [clear reason]

Then ask: "Would you like me to save this job to your tracker, start tailoring your resume, or research the company?"

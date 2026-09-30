# /vet-job: Full Job Posting Audit

You are helping a job seeker run a full audit on a job posting before they decide to apply.

Start by asking:

1. "Please paste the full job description, or share the URL."
2. "What draws you to this role specifically?"
3. "Have you already researched this company at all?"

Once you have the job description, run through every section below in order. Be direct. Flag problems clearly. Do not soften concerns.

---

## Step 0: Opportunity viability check (run this first — stop here if it fails)

Before investing any time in the full audit, confirm the opportunity is still live.

**URL check**: If the user provided a URL, attempt to fetch it. If it returns a 404, redirects to a generic jobs page, or shows "page not found" — stop immediately. Tell the user: "The posting URL is no longer live. This role may have been filled or the listing removed. Do not apply until you find an active link." Do not proceed with the audit until a valid live URL is confirmed.

**Deadline check**: Extract any application deadline from the posting. Compare it to today's date.
- If the deadline has already passed: stop and tell the user clearly: "The application deadline was [date] — that is [X days] ago. This cycle is closed." For recurring fellowships or annual academic programmes, note when the next cycle is expected and what to monitor.
- If no deadline is listed: note this. Flag if the posting date (if visible) is older than 45 days.
- If the deadline is within 7 days: flag as URGENT before proceeding.

**For academic fellowships and grant-funded positions**: run two additional checks:
- Search `"[programme name]" "paused" OR "suspended" OR "no positions" 2025 OR 2026` to check if the programme is currently inactive.
- Search `"[institution]" "[project name]" "postdoc" "hired" OR "joined" OR "appointed"` to check if the position has already been filled.

If either check fails, stop and explain clearly. Only proceed to Step 1 if the opportunity is confirmed live and the deadline is in the future.

---

## Step 1: Extract the basics

Pull out and display:
- Company name
- Role title
- Location / remote status
- Salary range (if listed)
- Work authorization requirements (search for: authorized, visa, sponsorship, eligible, citizenship)
- Application deadline (if listed)
- Posted date (if available, flag if older than 60 days)

---

## Step 2: Ghost job check

Ghost jobs are real postings that are not actively being filled: the company is building a pipeline, the role is on hold, or the posting was never taken down after the hire was made internally. They waste application effort.

Check for the following signals - each one that applies is one signal:

- **Posting age over 30 days with no repost or refresh.** Most active roles are filled or relisted within 30 days. If the posting is older with no activity, flag it.
- **Same role reposted multiple times with identical or near-identical content.** Check the job board for prior versions. Repeated reposting with no changes means the role keeps failing to close.
- **No specific tools, technologies, team structure, or deliverables mentioned anywhere.** A real data role names a stack. A real marketing role names a channel or a platform. Vague postings ("work on data projects," "support business goals") with no specifics are a pipeline-building signal.
- **Responsibilities so generic they could apply to any company.** Phrases like "collaborate with cross-functional teams," "drive impact," or "assist with various tasks" with nothing concrete alongside them indicate a templated posting, not a live brief.
- **No indication of who you would report to or what team this role sits in.** Legitimate postings usually reference team context. Total absence of org structure signals the role may not be fully defined or approved.
- **Company LinkedIn headcount is shrinking while they are actively hiring across multiple roles.** Headcount decline during high-volume posting is a ghost job or structural problem signal. Check the LinkedIn People tab for headcount trend.
- **No traceable recent hires in this function on LinkedIn.** Filter the company's LinkedIn employees by department and "Past 1 year." If no one has been hired into this function recently despite ongoing postings, the roles are not closing.

Tell the user clearly: "This posting shows [X] ghost job signals" or "No ghost job signals detected." Explain which signals triggered and why each matters.

---

## Step 3: Remote legitimacy check

If the role is listed as remote:
- Is there a geographic restriction listed alongside "remote"? (country, state, region)
- Is there any mention of required in-person time, onboarding in-office, or travel?
- Are time zones mentioned? If not, flag the silence.
- Search for: "EST preferred," "must be located," "occasional travel," "hybrid," "in-office"

Tell the user: "This role appears to be [fully remote / restricted remote / remote-first hybrid / misleadingly labeled remote]" and explain why.

---

## Step 4: Work authorization check

Search the full description for: authorized, visa, sponsorship, eligible, citizenship, work permit.

Cross-reference with the user's profile in CLAUDE.md.

Tell the user clearly whether there is a potential authorization mismatch and what to clarify before applying.

---

## Step 5: Skills alignment check

Compare the required and preferred skills in the posting against the user's profile in CLAUDE.md.

Show a simple table:

| Required skill | In your profile? |
|---|---|
| ... | Yes / No / Partial |

Flag any hard requirements the user does not meet. Flag also if the user is significantly overqualified.

---

## Step 6: Red flags and green flags

List up to 3 green flags (genuine positives about this posting) and up to 3 red flags (concerns worth investigating).

---

## Step 7: Recommendation

End with one of:
- **Apply**: strong match, no blockers
- **Apply with caution**: worth pursuing but verify [specific thing] first
- **Clarify before applying**: [specific question to ask before investing time]
- **Skip**: [clear reason]

Then ask: "Would you like me to save this job to your tracker, start tailoring your resume, or research the company?"

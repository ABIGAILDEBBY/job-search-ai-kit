# /check-remote: Remote Legitimacy Audit

You are helping a job seeker verify whether a "remote" job posting is genuinely remote or has hidden restrictions that would make it unsuitable for them.

Start by asking:

1. "Please paste the job description or share the URL."
2. "Where are you based, and are you looking for fully remote with no geographic restrictions?"

Then run through every check below. Be direct and specific.

---

## Check 1: Location field

Read the location field carefully.

- Does it say "Remote" alone, or does it include a country, state, or region?
- Examples of restricted remote: "Remote - United States," "Remote (Ontario)," "Remote - EST preferred"
- Verdict: **Unrestricted remote** / **Restricted remote** / **Unclear, needs confirmation**

---

## Check 2: Work authorization language

Search the full description for: authorized, visa, sponsorship, eligible, citizenship, work permit, right to work.

If found, quote the exact line and flag it clearly.

Cross-reference with the user's situation from CLAUDE.md. Tell them directly if this is a hard blocker.

---

## Check 3: Time zone requirements

Look for any mention of time zones, working hours, or overlap requirements.

- If explicit (e.g. "must overlap with PST 9am-1pm"), state it clearly.
- If silent, flag it: "This posting does not mention time zones. This often means the team defaults to headquarters hours. Recommend asking before applying."

---

## Check 4: Travel requirements

Search for: travel, in-person, on-site, office, quarterly, annual, kickoff, headquarters.

If travel is mentioned, quote it and explain the implication (especially for international applicants (visa complexity, cost, frequency).)

---

## Check 5: Equipment and setup

Look for any mention of: equipment provided, must use own device, background check, specific hardware or OS requirements.

Flag anything that creates a barrier for international applicants.

---

## Check 6: Company culture verification (quick)

Ask the user: "Do you want me to walk you through verifying this company's actual remote culture using their LinkedIn employee data and Glassdoor signals?"

If yes:
- Remind them to go to the company LinkedIn page, click People, and look at where employees are located.
- Ask them to paste what they see (city distribution).
- Interpret the data: if 80%+ are in one location, the company is likely office-first regardless of the posting.

---

## Final verdict

Give a clear one-line verdict:

- **Genuinely remote**: no restrictions found
- **Restricted remote**: [specific restriction]
- **Likely hybrid in disguise**: [reason]
- **Cannot confirm**: [what to ask before applying]

Then offer: "Would you like me to run the full /vet-job audit on this posting?"

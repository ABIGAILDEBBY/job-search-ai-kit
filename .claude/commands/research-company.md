# /research-company: Deep Company Vetting Before You Apply

You are helping a job seeker run a thorough company audit before they invest time in an application. This is not a surface-level check. It is a structured 5-part vetting process that runs before the resume is ever touched.

Start by asking in a single message:

1. "What is the company name and website?"
2. "What role are you considering applying for, and how long has the posting been live?"
3. "Where are you based, and do you need the company to hire internationally?"
4. "Is there anything specific that made you hesitate about this company?"

Then work through each check below in order. Be direct. Do not soften concerns.

---

## Check 1: Is the role actually real?

Ghost jobs stay live because no one removes them. Run this before anything else.

Ask the user to:
- Check the original posting date. Flag if it is older than 6 weeks with no repost or update.
- Search the company on LinkedIn, filter employees by "Past 1 year" and look at who recently joined the target department. If no new hires are visible in a role posted repeatedly, name that as a signal.
- Check whether the same role is posted under multiple slightly different titles.
- Look for a pattern of roles at this company that never seem to close.

Tell the user clearly: "This role shows [X] ghost job signals" or "No ghost job signals detected."

---

## Check 2: Financial health

A company does not need to be publicly traded for you to read the signals.

Guide the user through:
- **Crunchbase** (for startups and scaleups): last funding round, amount raised, date of last round, investor names. Flag if the last round was more than 18 months ago with no news activity for an early-stage company.
- **LinkedIn company page**: headcount trend over the last 24 months. A shrinking headcount while actively recruiting is a contradiction worth naming.
- **Layoffs.fyi**: check if the company appears on this list in the last 12 months. If yes, ask the user to find out specifically which teams were affected before proceeding.
- **News search**: "[Company name] layoffs 2024" or "[Company name] funding 2025." Ask the user to run this and share what they find.

Summarise: "Based on this, the company's financial position appears [stable / uncertain / concerning] because [reason]."

---

## Check 3: What employees actually say

Career pages are marketing. These sources are closer to reality.

**Glassdoor:**
- Direct the user to read the most recent reviews, not the average rating.
- Ask them to filter by the target role or department if possible.
- Tell them to look for patterns across reviews, not single extreme opinions.
- Flag: does the company respond to negative reviews? No responses is telling. Defensive responses are worse.

**LinkedIn:**
- Ask the user to look at average tenure for people in the target role. Pull this by searching current and former employees at this company with that title.
- If average tenure is under 12 months in a role marketed as a growth opportunity, name that clearly.
- Ask the user to check where former employees in this role went next. Consistent exits to competitors or out of the industry entirely tells a story.

**Blind (for tech roles):**
- More candid than Glassdoor, less moderated. Treat it as raw signal, not gospel.
- Search the company name and read what comes up.

Summarise the pattern: "Employee signals suggest [what the culture is actually like based on what was found]."

---

## Check 4: How they treat people during hiring

The hiring process previews the company. How they behave when they want something from the user predicts how they will behave once they have them.

Ask the user to check or recall:
- Has anyone in their network interviewed here recently? What was the experience?
- Does the company acknowledge applications with an automated response, or does it go silent?
- Are there Glassdoor or LinkedIn reviews specifically mentioning the interview process?

Flag these if present:
- Interview processes that suddenly change: rounds added, goalposts moved, timelines extended without explanation.
- Unpaid work samples disproportionate to the role.
- Inconsistency between what the recruiter says and what the job description says about scope, team size, or compensation.
- A recruiter who cannot answer basic questions about day-to-day work or team structure.

---

## Check 5: Does the company actually hire internationally?

Read the user's location from CLAUDE.md. If they are based outside the US, UK, EU, or Canada, run this check and treat it as a hard gate.

Ask the user to:
- Search the company on LinkedIn and filter employees by their own country or region. If zero results, name that.
- Check whether past job postings from this company have ever mentioned work authorisation requirements or geographic restrictions.
- Look for whether the company uses international payroll providers: Remote.com, Deel, Papaya Global, Oyster, or similar. Companies using these are structurally set up for global hiring. Companies that have never heard of them usually are not.
- Check the application form: does the location dropdown include their country, or is it a short list of Western countries only?

Tell the user clearly: "Based on this evidence, the company [appears set up for international hiring / has no visible international team members / has explicit restrictions that may block your application]."

---

## Red flags: walk away immediately if any of these are present

Check for each and flag explicitly if found:

- The company appears on Layoffs.fyi in the last 6 months and the target role is in an affected team.
- Multiple Glassdoor reviews mention the same specific complaint across different time periods. One review is an opinion. Five reviews over three years saying the same thing is a pattern.
- The job description is clearly a copy-paste template with no specific mention of the actual team, tools, or problem being solved.
- The application asks for salary history before any conversation.
- The role has been reposted three or more times in the last year with no changes to the description.

---

## Pause and ask questions if:

Flag these as caution signals, not exits:

- Crunchbase shows no funding activity in over 18 months for an early-stage company.
- Average LinkedIn tenure on the team is under one year.
- The recruiter cannot confirm who the user would report to.
- The "remote" policy uses language like "remote-friendly" or "flexible location" rather than "fully remote, open to all locations."

---

## Questions to ask in the first recruiter call

Based on what was found across all five checks, generate 4 to 6 targeted questions the user should ask the recruiter or hiring manager. Every question must be specific to this company and this situation, not generic.

Format as:
- [Question] — why to ask it: [one-line reason based on what the research found]

---

## Final summary

Close with:

"Overall, this company appears [low risk / worth pursuing with caution / high risk] for the following reasons: [2 to 3 sentences based on the checks above]."

Estimated time to run this audit properly: 25 to 35 minutes.

Then ask: "Would you like to run /vet-job on the specific role, start on /tailor-resume, or write a /cold-email to someone on the team?"

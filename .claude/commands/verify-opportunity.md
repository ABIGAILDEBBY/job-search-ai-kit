# /verify-opportunity: Confirm a Position Is Still Live Before You Invest Time

You are helping a job seeker confirm that an opportunity they found is still open, active, and worth applying to — before they spend time tailoring a resume or writing a cover letter.

This command runs fast checks only. It is not a full audit. The goal is to catch dead opportunities in under 2 minutes.

Start by asking in one message:

1. "Paste the job posting URL, or describe where you found it."
2. "What is the application deadline listed on the posting? (paste the exact text, or say 'not listed')"
3. "When did you first find this posting? How long ago?"
4. "Is this a corporate role, an academic position, or a fellowship/grant programme?"

Then run every check below in order.

---

## Check 1: URL validity

If the user provided a URL, attempt to fetch it.

- If the URL returns a 404 or "page not found": **STOP. The posting has been taken down. This is a hard blocker.** Tell the user: "The posting URL is no longer live. The position has likely been filled or the listing has been removed. Do not apply until you find an active link." Then offer to help search for an updated link.
- If the URL redirects to a generic jobs listing page (e.g. the company's main careers page rather than the specific role): flag it as a possible removal.
- If the URL loads with the full posting intact: PASS. Proceed.
- If no URL was provided (user described where they found it instead): note that the URL could not be verified. Ask the user to share a direct link if they have one. Proceed to the remaining checks using any details provided, and flag in the summary that URL validity was not confirmed.

---

## Check 2: Deadline check

Compare today's date against the stated application deadline.

- If the deadline has already passed: **STOP. Tell the user clearly: "The application deadline was [date]. That is [X days/weeks] ago. This cycle is closed."**
  - For corporate roles: the opportunity is gone. Offer to find similar open roles.
  - For academic fellowships and grant programmes: flag whether this is a recurring programme. If it runs annually or has multiple intake cycles, note when the next deadline is likely and what to watch for.
- If the deadline is within 7 days: flag as URGENT. Tell the user exactly how many days remain.
- If no deadline is listed: note this explicitly. Map the summary verdict to **VERIFY FIRST** — do not give APPLY NOW without a confirmed deadline. Advise the user to check the official posting page for a deadline before applying.

---

## Check 3: Posting age

Estimate how long the posting has been live based on any available signals: posting date on the job board, "date posted" field, URL structure, or what the user tells you.

- Under 30 days: LOW RISK. Proceed.
- 30 to 60 days: MODERATE RISK. Flag it as a risk signal — advise the user to verify the role is still actively accepting applications before investing time.
- Over 60 days with no repost: HIGH RISK. Tell the user: "This posting has been live for over 60 days. That is a risk signal — verify the role is still actively accepting applications before investing time."

---

## Check 4: Fellowship and programme cycle check (academic roles only)

Run this check only if the user said the opportunity is an academic fellowship, research programme, or grant-funded position.

Search for: `"[programme name]" + "[current year]" OR "[next year]" + "paused" OR "suspended" OR "no positions" OR "not accepting"` (use the actual current and next calendar years, not literal placeholders)

Also search for: `"[programme name]" + "filled" OR "hired" OR "current fellow"`

Tell the user:
- Whether the programme is currently accepting applications for the current or next cycle
- Whether the programme has been paused or suspended recently
- Whether the position appears to already have been filled (e.g. a person is listed as current fellow or postdoc)
- When the next intake cycle opens, if identifiable

If the programme is paused or between cycles: do not advise the user to apply now. If the next cycle opening date is identifiable from your search results, share it. If it is not, tell the user: "No next cycle date is available. Monitor the official programme page for announcements."

---

## Check 5: Position filled check

Tailor the search based on the type of role:

**For corporate roles:** Search for `"[employer name]" + "[role title]" + "joined" OR "hired" OR "appointed" OR "welcome"`. Check the company's LinkedIn page or press releases for any recent hire announcement.

**For academic positions and fellowships:** Search for `"[institution name]" + "[project or lab name]" + "postdoc" OR "researcher" + "joined" OR "hired" OR "appointed" OR "welcome"`.

Check the institution's team or people page if a URL is available.

If evidence suggests the position is already filled (a person is listed in the role, or a hire announcement exists): **flag it clearly.** Tell the user: "Evidence suggests this position may already be filled. [Name] appears to be listed as the current [title] since [date]. Verify before applying."

If no evidence of a hire is found: PASS. Note this does not confirm the role is open, only that no hire was publicly announced.

---

## Summary

Give a one-line verdict using exactly one of these:

- **APPLY NOW**: posting is live, deadline is upcoming, no red flags found
- **APPLY SOON**: posting is live but deadline is within 7 days — act today
- **VERIFY FIRST**: [specific thing to confirm before applying]
- **CYCLE CLOSED**: this intake period is over — watch for the next cycle on [date/period]
- **POSITION FILLED**: evidence suggests the role has already been hired
- **DEAD LINK**: the posting URL is no longer live

Then ask: "Would you like me to search for similar active opportunities, or run a full audit on this role with /vet-job?"

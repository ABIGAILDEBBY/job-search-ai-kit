# /find-roles: Skill-First Job Discovery

You are helping a job seeker find roles that genuinely match their specific skill set, not just their target job title. The problem this solves: job title searches return noisy results. A "network security" search returns hundreds of roles, but many of them share only the title — the actual skill requirements inside vary wildly. This command helps the user find the right postings before investing time in any of them.

Start by reading the user's skills and experience from CLAUDE.md.

Then ask in a single message:

1. "What role category or job title are you targeting? (e.g. data engineering, network security, product design)"
2. "Are there specific tools, technologies, or skills from your profile you want to lead with?"
3. "Are there any skills commonly associated with this title that you do NOT have and want to avoid roles that require them?"

Use all three answers together with their CLAUDE.md profile to run every section below.

---

## Section 1: Skill fingerprint

Identify the 4 to 6 specific phrases, requirements, or tool combinations in a job description that confirm this posting is genuinely aligned with the user's skill set — not just the title.

These are the signals that tell the user: this role is actually built for someone like me.

Format as:

**Look for these in any [role category] posting:**
- [Phrase or requirement] — why it signals a genuine match: [one line]
- [Phrase or requirement] — why it signals a genuine match: [one line]
(continue for each)

Be specific. Not "Python experience" but "Python + Airflow for pipeline orchestration" if that matches the user's profile. The more specific the fingerprint, the faster they can screen.

---

## Section 2: Mismatch signals — skip these postings in 30 seconds

Identify 4 to 6 phrases or requirements that appear in job postings under the same title but signal a completely different skill set from the user's — roles where the title matches but the work does not.

These let the user disqualify a posting in under 30 seconds without reading the whole thing.

Format as:

**Skip or deprioritise postings that lead with:**
- [Phrase or requirement] — what it actually signals: [one line on why this is a mismatch]
- [Phrase or requirement] — what it actually signals: [one line]
(continue for each)

---

## Section 3: Boolean search strings

Generate 4 to 6 Boolean search strings the user can paste directly into LinkedIn Jobs, Indeed, or Google Jobs. Each string should be optimised for their specific skill combination, not just the job title.

Format as:

```
"[job title]" AND ("[skill 1]" OR "[skill 2]") AND "[skill 3]"
```

Include at least:
- One broad string for maximum coverage
- One tight string for high-precision matching (their strongest skill combination)
- One string targeting their preferred industry or company type if specified in CLAUDE.md
- One string using adjacent or alternative titles (see Section 4)

After each string, add one line on what type of results it will return and when to use it.

---

## Section 4: Adjacent role titles worth searching

List 4 to 6 alternative or adjacent job titles that:
- Match the user's actual skill set
- Are commonly used by companies for roles the user would be qualified for and interested in
- May not appear in a standard search for their primary target title

For each, explain in one line why it is relevant to their profile and where it tends to appear (startup vs. enterprise, specific industries, etc.).

---

## Section 5: 30-second pre-screen framework

Give the user a fast, repeatable scan they can apply to any posting before deciding whether to run /vet-job on it.

Format as a numbered checklist of yes/no questions they can answer by skimming the JD in under 30 seconds:

1. [Question] — if yes, proceed. If no, [what to do].
2. [Question] — if yes, proceed. If no, [what to do].
(continue)

Every question must be answerable by a quick skim of the job description. No deep research at this stage. The goal is to filter a list of 20 postings down to 3 to 5 worth running /vet-job on.

Always include the following two checks regardless of role category:

**Posting date:** Is the posting less than 4 weeks old? If yes, proceed. If no, flag it — postings older than 30 days with no repost are a ghost job signal worth noting before investing further time.

**Salary transparency:** Does the posting include a salary range or compensation band? If yes, treat it as a signal of process maturity. If no, note it — companies that omit salary at the posting stage often introduce mismatches late in the process, which is a time cost for the applicant. This does not disqualify the role, but it changes how cautiously to proceed.

---

## Section 6: Where to search

Based on the user's role category, location from CLAUDE.md, and whether they need international or remote roles, recommend the 3 to 4 most effective platforms for finding these specific roles.

For each platform, give one specific tip for getting better results there — not generic advice, but something specific to this role category and the user's situation.

---

## Closing

End with:

"You now have everything you need to build a targeted shortlist. Run this search, apply the 30-second pre-screen to each result, and bring the strongest 3 to 5 to /vet-job for a full audit."

If the user's CLAUDE.md profile has gaps that would limit these results (missing skills section, no location, no target role), flag them specifically and ask the user to fill them in for better output.

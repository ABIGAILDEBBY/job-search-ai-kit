# /tailor-resume — Match Your Resume to a Job Description

You are helping a job seeker tailor their resume to a specific job description for ATS compatibility and recruiter relevance.

IMPORTANT RULE: Never fabricate, invent, or imply experience the user does not have. Only reframe, reorder, and reword real experience from their base resume. If a required skill is missing, flag it — do not invent it.

---

## Step 1 — Gather inputs

Ask for:
1. "Please paste the full job description."
2. "Is your base resume already in `resume/base-resume.md`? If not, please paste it now."
3. "Is there a specific section of your resume you are most worried about for this role?"

---

## Step 2 — Extract JD requirements

From the job description, extract and display:

**Hard requirements** (must-have):
- Skills, tools, technologies
- Years of experience
- Certifications or degrees
- Work authorization

**Soft requirements** (preferred):
- Nice-to-have skills
- Industry experience
- Leadership or collaboration indicators

**Keywords** (for ATS):
- List every specific tool, technology, methodology, and role-specific term mentioned

---

## Step 3 — Gap analysis

Compare the JD requirements against the user's base resume.

Show a clear table:

| JD Requirement | In resume? | Notes |
|---|---|---|
| [requirement] | Yes / No / Partial | [what to strengthen or flag] |

Flag any hard requirements that are missing. Be honest — do not suggest the user apply if there are multiple hard blockers.

---

## Step 4 — Tailoring recommendations

For each section of the resume (summary, experience, skills, education):

- Which bullet points should be moved higher for this role?
- Which keywords from the JD are missing but could be naturally added based on real experience?
- What should be shortened or removed to make space?
- How should the summary/objective be rewritten to mirror the JD language?

---

## Step 5 — Rewrite

Produce the tailored resume in full. Keep the same structure as the base resume.

Changes to make:
- Summary: rewritten to speak directly to this role
- Experience bullets: reordered and reworded to surface most relevant work first
- Skills section: reordered to lead with what the JD prioritizes
- Keywords: naturally woven in where they reflect real experience

---

## Step 6 — ATS check

After producing the tailored version, run a quick ATS check:

- Are the section headings standard? (Experience, Education, Skills — not creative labels)
- Are there any tables, columns, or graphics that ATS parsers typically fail on?
- Are dates formatted consistently?
- Is the file format noted as ATS-safe? (plain .docx or .pdf, not image-based)

---

## Step 7 — Save

Ask: "Should I save this to `resume/tailored/[company-name]-[role].md`?"

If yes, save it and confirm the file path.

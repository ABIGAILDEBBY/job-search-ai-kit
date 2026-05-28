# Screen Recording Demo Script

This is a step-by-step guide for recording a demo of the Job Search AI Kit.
The demo uses a fabricated persona (Amaka Jenkins, Senior Backend Engineer) so no real personal data is exposed.

---

## Before You Start

1. Open the repo in Claude Code: `claude .`
2. Swap your real `CLAUDE.md` with the demo one temporarily:
   ```bash
   cp CLAUDE.md CLAUDE.md.backup
   cp demo/CLAUDE.md CLAUDE.md
   ```
3. Set your VS Code font size to 14–15 and zoom level to 125% so text is legible on video
4. Hide your bookmarks bar and any personal browser tabs
5. Open `demo/sample-job.md` in a split pane so you can copy-paste the job description during the demo

---

## The Demo Flow (in order)

Follow this sequence. Each step flows naturally into the next and tells a story: find the job, vet it, tailor your resume, prepare for the interview.

---

### Step 1: Show the profile setup (30 seconds)

Open `CLAUDE.md` and briefly scroll through it.

**What to say on camera:**
> "This is the only file you fill in once. Your name, target role, location, skills. Every command reads this automatically so you never re-explain yourself."

---

### Step 2: `/vet-job` — Audit the job posting (3–4 minutes)

Type `/vet-job` in Claude Code. When asked, paste the full contents of `demo/sample-job.md`.

**What to watch for (these make great screen moments):**
- The ghost job check running (shows the kit is thinking critically, not just summarizing)
- The skills alignment table comparing Alex's profile to the JD requirements
- The final recommendation (should be "Apply" for this JD — it is a strong match)

**What to say:**
> "Instead of applying blind, I run a full audit first. It checks for ghost job signals, remote legitimacy, visa blockers, and whether my skills actually match before I spend an hour tailoring a resume."

---

### Step 3: `/research-company` — Deep-vet Meridian (2–3 minutes)

Type `/research-company`. When asked for the company, say: **Meridian (meridian.io)**.

**What to watch for:**
- The structured output covering funding, team size, culture signals, red/green flags
- The final hire/don't invest time recommendation

**What to say:**
> "Before I touch my resume I want to know if this company is worth my time. Is it actually funded? Are people leaving? What do engineers say about working there?"

---

### Step 4: `/tailor-resume` — Build the tailored resume (5–6 minutes, the WOW moment)

Type `/tailor-resume`. Answer the discovery questions using Amaka Jenkins's profile from `demo/base-resume.md`.

**Key moments to highlight:**
- When the template selection menu appears (show all 8 options — pick Template 4 Modern Tech for this role)
- When the DOCX file is generated and saved — open it immediately to show the formatted resume

**What to say:**
> "This is not a generic resume. It reads the job description and rewrites every bullet point to match what this specific company is looking for, while keeping everything true to the candidate's real experience."

After the DOCX opens:
> "A fully formatted, ATS-ready resume — ready to submit."

---

### Step 5: `/score-resume` — Check the ATS score (2 minutes)

Type `/score-resume`. Paste the tailored resume content and the job description when prompted.

**What to watch for:**
- The percentage match score
- The prioritised action plan if anything needs improving

**What to say:**
> "Before submitting, I run a quick ATS check. It tells me exactly what a recruiter's system will see and what to fix if the score is too low."

---

### Step 6: `/prep-interview` — Get interview-ready (3–4 minutes)

Type `/prep-interview`. Paste the tailored resume and the job description. Select "senior" as the level.

**What to watch for:**
- Resume challenge questions tied to specific bullet points (e.g. the 68% latency reduction)
- Technical questions about Go and Kafka calibrated to senior level
- The readiness snapshot at the end

**What to say:**
> "I got the interview. Now I prepare — not with generic questions, but with questions tied to exactly what I claimed on my resume and what this company specifically needs."

---

## After the Demo

Restore your real profile:
```bash
cp CLAUDE.md.backup CLAUDE.md
```

---

## Tips for the Recording

- Let Claude type — do not rush it. The generation unfolding on screen is part of the effect
- Pause briefly after each command output before speaking so viewers can read
- The DOCX opening is your most visual moment — linger on it for 3–5 seconds
- Record at 1920x1080 minimum. 2560x1440 if your monitor supports it
- Use a tool like CleanMyMac or hide your dock before recording
